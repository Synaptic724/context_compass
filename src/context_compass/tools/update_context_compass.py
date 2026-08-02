#!/usr/bin/env python3
"""Upgrade an installed Context Compass to a newer version of the package.

Point it at a new package and an existing install. It decides, per file, whether
replacing is safe - and refuses rather than guessing when it is not.

THE THREE-HASH RULE

One hash tells you a file changed. It cannot tell you WHO changed it, and that is
the only question that matters when deciding whether to overwrite.

    shipped   what the installed version's manifest recorded
    current   what is on disk in the install right now
    new       what the incoming version ships

    current == shipped, new != shipped   -> clean update, replace
    current == shipped, new == shipped   -> already current, skip
    current != shipped, new == shipped   -> the user edited it, package did not:
                                            KEEP their version
    current != shipped, new != shipped   -> both moved: CONFORM to the new
                                            version, and say so.

Without `shipped` you cannot separate rows three and four from row one, so you
either overwrite the user's edits or never update anything. There is no version
of this that works with a single hash.

WHY ROW FOUR CONFORMS RATHER THAN REFUSING

Package files belong to the package. An edit to one is a divergence that has to
be re-resolved on every future upgrade, forever - so preserving it is not a
kindness, it is a debt. The install gets two directories where local work is
untouchable (`user_defined/` and `agent_onboarding/user_defined/`), plus the
RESET lanes, and that is where customisation belongs.

So the default is to conform, and to name every file it conformed. Row three
still keeps your edit when the package did not move, because there is nothing to
conform to. `--preserve-local` restores the old refusal if you are mid-migration
and not ready yet.

WHAT IS NEVER TOUCHED

    RESET lanes   tickets, artifacts, system docs, project instructions.
                  The install owns these outright. An upgrade that rewrites
                  someone's architecture map is not an upgrade.
    INSTANCE      `user_defined/` and `agent_onboarding/user_defined/`. The
                  first is a free space for anything; the second holds role
                  overlays. Never replaced, never restored, never removed - not
                  even a role the package originally shipped as a sample, because
                  by the time it is in someone's repo it is theirs to edit.

WHAT GETS SPECIAL HANDLING

    LIVE files    the boards. Only the text between MANAGED markers is swapped.
                  Routing rows are the install's, and survive.
    CONFIG        merged key by key: new keys are added with package defaults, a
                  value the user already set is never overwritten, and keys the
                  new version dropped are reported rather than deleted.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from package_manifest import (  # noqa: E402
    MANIFEST_NAME, parse, is_permissive, check_manifest_compatible,
)
from cleanup_context_compass import (  # noqa: E402
    swap_managed, carry_user_regions, orphaned_user_regions, user_regions,
)


def conform_text(new_bytes: bytes, install_path: pathlib.Path) -> tuple[bytes, list[str], list[str]]:
    """The new version's file, with the install's user regions carried across.

    Returns (bytes_to_write, carried_names, orphaned_names).

    Binary or undecodable files, and files with no user region on either side,
    pass through untouched - the fast path is also the common one.
    """
    if not install_path.is_file():
        return new_bytes, [], []
    try:
        incoming = new_bytes.decode("utf-8")
        current = install_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, ValueError):
        return new_bytes, [], []
    try:
        if not user_regions(current):
            return new_bytes, [], []
        merged, carried = carry_user_regions(incoming, current)
        orphaned = orphaned_user_regions(incoming, current)
    except ValueError:
        # An unterminated region means we cannot tell where the install's text
        # ends. Conform the file rather than splice blindly, and say so.
        return new_bytes, [], ["(malformed region - not carried)"]
    return merged.encode("utf-8"), carried, orphaned


def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def top_level_keys(yaml_text: str) -> dict[str, tuple[int, int]]:
    """Map each top-level YAML key to its (start_line, end_line_exclusive).

    Deliberately not a YAML parser. This tool only needs to know where a
    top-level block begins and ends so it can append a missing one verbatim,
    comments and all. Parsing and re-emitting would reformat the user's file and
    drop their comments, which is a worse outcome than not merging at all.
    """
    lines = yaml_text.split("\n")
    starts = [(i, m.group(1)) for i, ln in enumerate(lines)
              if (m := re.match(r"^([A-Za-z_][A-Za-z0-9_]*):", ln))]
    out: dict[str, tuple[int, int]] = {}
    for idx, (i, key) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        while end > i + 1 and lines[end - 1].strip() == "":
            end -= 1
        out[key] = (i, end)
    return out


def merge_config(current: str, new: str) -> tuple[str, list[str], list[str]]:
    """Add top-level keys the install lacks. Never overwrite one it has."""
    cur_keys = top_level_keys(current)
    new_keys = top_level_keys(new)
    new_lines = new.split("\n")

    added, dropped = [], []
    additions: list[str] = []
    for key, (s, e) in new_keys.items():
        if key not in cur_keys:
            block = "\n".join(new_lines[s:e])
            # carry the comment block immediately above the key
            lead = s
            while lead > 0 and (new_lines[lead - 1].startswith("#")
                                or new_lines[lead - 1].strip() == ""):
                lead -= 1
                if new_lines[lead].strip() == "" and lead < s - 1:
                    break
            comment = "\n".join(new_lines[lead:s]).strip("\n")
            additions.append((comment + "\n" + block) if comment else block)
            added.append(key)
    for key in cur_keys:
        if key not in new_keys:
            dropped.append(key)

    if additions:
        current = current.rstrip("\n") + "\n\n" + "\n\n".join(additions) + "\n"
    return current, added, dropped


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--install", required=True, type=pathlib.Path,
                    help="the existing install to upgrade")
    ap.add_argument("--new", required=True, type=pathlib.Path,
                    help="the new package version")
    ap.add_argument("--check", action="store_true", help="report only, change nothing")
    ap.add_argument("--apply", action="store_true", help="perform the upgrade")
    ap.add_argument("--keep-retired", action="store_true",
                    help="do NOT sweep files in strict lanes that the new version does "
                         "not ship. They are reported either way")
    ap.add_argument("--seed-instance", action="store_true",
                    help="also create INSTANCE files the manifest lists but that are "
                         "missing from disk. Repairs installs upgraded before 2.5.0, "
                         "where a new instance lane was recorded but never written. "
                         "Existing files are still never replaced; this only creates "
                         "absent ones, so pass it only if you did not delete them")
    ap.add_argument("--preserve-local", action="store_true",
                    help="do NOT conform package files you have edited; report them as "
                         "conflicts and leave them alone. Use when you deliberately "
                         "customised a package file and are not ready to move it into "
                         "user_defined/")
    ap.add_argument("--force-conflicts", action="store_true",
                    help=argparse.SUPPRESS)   # retained: conform is now the default
    args = ap.parse_args()

    install, new = args.install, args.new
    for label, root in (("install", install), ("new", new)):
        if not (root / "AGENTS.MD").is_file():
            print(f"ERROR: --{label} {root} is not a package root")
            return 2
    if not (new / MANIFEST_NAME).is_file():
        print(f"ERROR: --new {new} has no {MANIFEST_NAME} - run package_manifest.py on it")
        return 2
    if not args.check and not args.apply:
        print("Refusing to act without --apply. Use --check to see the plan.")
        return 2

    incoming_text = (new / MANIFEST_NAME).read_text(encoding="utf-8")
    problem = check_manifest_compatible(incoming_text, f"--new {new}")
    if problem:
        print(f"ERROR: {problem}")
        return 2
    incoming = parse(incoming_text)

    # An install predating the manifest has no shipped hashes, so for every file
    # that differs we cannot tell a local edit from an upstream change. Every
    # difference lands in the conform bucket and is named, so the user sees
    # exactly what the upgrade brought into line. `--preserve-local` stops it.
    first_adoption = not (install / MANIFEST_NAME).is_file()
    if not first_adoption:
        installed_text = (install / MANIFEST_NAME).read_text(encoding="utf-8")
        problem = check_manifest_compatible(installed_text, f"--install {install}")
        if problem:
            print(f"ERROR: {problem}")
            return 2
        shipped = parse(installed_text)
    else:
        shipped = {}
    if first_adoption:
        print(f"NOTE: {install} has no {MANIFEST_NAME}, so this is its first")
        print("      manifest-aware upgrade. Without shipped hashes a local edit and an")
        print("      upstream change are indistinguishable, so every differing package")
        print("      file is conformed to the new version and named below. Your lanes -")
        print("      system_docs, tickets, artifacts, special_instructions, and both")
        print("      user_defined directories - are untouched. Use --preserve-local to")
        print("      review instead of conforming.")
        print()

    def version_of(root: pathlib.Path) -> str:
        man = root / MANIFEST_NAME
        if not man.is_file():
            return "unknown (no manifest)"
        for line in man.read_text(encoding="utf-8").splitlines():
            if line.startswith("| package_version |"):
                return line.split("|")[2].strip()
        return "?"

    replace, skip, keep, conflict, added, gone = [], [], [], [], [], []
    blocks, cfg = [], None
    live_conform: list[str] = []       # boards with regions: whole file updates
    unmigrated_live: list[str] = []    # boards without: managed block only

    for rel, (cls, new_sha) in sorted(incoming.items()):
        p = install / rel
        old_sha = shipped.get(rel, (None, None))[1]

        if cls == "RESET":
            continue                                   # the install owns these
        if cls == "INSTANCE":
            # Never replaced, never removed - but a lane the package introduces
            # has to arrive once, or it never exists. Skipping INSTANCE outright
            # meant `user_defined/` was listed in the manifest of installs that
            # did not have the directory at all: a manifest describing a lane
            # nobody could find, and a free space the docs told you to use.
            #
            # `rel not in shipped` is what makes seeding safe, and it is the
            # three-hash rule doing the same job it does everywhere else. A file
            # the PREVIOUS version also shipped, now missing, was deleted by the
            # install - restoring it would resurrect something someone removed on
            # purpose. A file only the NEW version ships has never existed here,
            # so creating it takes nothing away.
            #
            # `--seed-instance` exists for one specific repair. Before 2.5.0 the
            # updater skipped INSTANCE entirely, so a lane could be recorded in
            # the install's manifest while never having been written to disk.
            # Such a file is absent AND in `shipped`, which is indistinguishable
            # from a deliberate deletion - so the flag makes the operator assert
            # which it is, rather than the tool guessing.
            if not p.exists() and (rel not in shipped or args.seed_instance):
                added.append(rel)
            continue
        if cls == "CONFIG":
            if p.is_file():
                merged, a, d = merge_config(p.read_text(encoding="utf-8"),
                                            (new / rel).read_text(encoding="utf-8"))
                cfg = (rel, merged, a, d)
            else:
                added.append(rel)
            continue
        if not p.is_file():
            added.append(rel)
            continue

        cur_sha = sha_bytes(p.read_bytes())
        if cls == "LIVE":
            # A board carrying USER-DEFINED regions can be conformed whole: the
            # package owns the headings, the table headers and the contract
            # prose, and `conform_text` carries the install's regions across. So
            # a board's SHAPE can finally be updated, which swapping only the
            # managed block never allowed - that is why an install could end up
            # with the managed block sitting above its own H1 and a duplicated
            # directive underneath, with no way for an upgrade to fix it.
            #
            # A board WITHOUT regions has all its rows outside any protected
            # area. Conforming it would delete them, so it stays on the old
            # managed-block-only path and is named as needing migration.
            try:
                migrated = bool(user_regions(p.read_text(encoding="utf-8")))
            except (UnicodeDecodeError, ValueError):
                migrated = False
            if migrated:
                (live_conform if cur_sha != new_sha else skip).append(rel)
                continue
            _, ch = swap_managed(p.read_text(encoding="utf-8"),
                                 (new / rel).read_text(encoding="utf-8"))
            if ch:
                blocks.append((rel, ch))
            unmigrated_live.append(rel)
            continue
        if cur_sha == new_sha:
            skip.append(rel)
        elif old_sha is None:
            conflict.append(rel)                       # not in the old manifest
        elif cur_sha == old_sha:
            replace.append(rel)
        elif new_sha == old_sha:
            keep.append(rel)
        else:
            conflict.append(rel)

    # Retired files: present in the install's package lanes, absent from the new
    # version. Never deleted - the package no longer shipping something is not
    # the same as the project not wanting it - but always named, because a
    # retired document left in place still gets read.
    #
    # Derived by walking the install rather than by reading the shipped manifest.
    # The manifest looks like the obvious source and is wrong twice: it is empty
    # on first adoption, and after any upgrade it lists only what the CURRENT
    # version ships - so a file retired two versions ago appears in neither
    # manifest and stays invisible forever. Walking the tree finds it either way.
    # Found by upgrading a real install that still carried `policy_router.md`
    # from the retired dual-router era.
    # A case-insensitive filesystem makes `SKILLS.md` and `SKILLS.MD` one file.
    # The manifest lists the uppercase name, so a lowercase copy looks retired -
    # and unlinking it destroys the file the manifest name also resolves to.
    # This is not hypothetical: it deleted a real install's role registry, and
    # the upgrade had just written the correct content into that same inode.
    #
    # So a path whose case-insensitive twin is in the manifest is never swept. On
    # a case-sensitive filesystem this skips a genuinely stale duplicate, which
    # costs one leftover file. The other way costs the registry.
    incoming_ci = {k.lower() for k in incoming}
    case_twins: list[str] = []
    for p in sorted(install.rglob("*")):
        if not p.is_file() or any(x in {"__pycache__", ".git"} for x in p.parts):
            continue
        rel = p.relative_to(install).as_posix()
        if rel in incoming or is_permissive(rel) or rel == MANIFEST_NAME:
            continue
        if rel.lower() in incoming_ci:
            case_twins.append(rel)
            continue
        gone.append(rel)

    # Computed before printing so --check can show it. An upgrade that only
    # reveals what it preserved AFTER writing is an upgrade you have to trust
    # rather than review.
    would_carry: list[tuple[str, list[str]]] = []
    would_orphan: list[tuple[str, list[str]]] = []
    for rel in replace + added + conflict + live_conform:
        if not (install / rel).is_file() or not (new / rel).is_file():
            continue
        _, c, o = conform_text((new / rel).read_bytes(), install / rel)
        if c:
            would_carry.append((rel, c))
        if o:
            would_orphan.append((rel, o))

    print(f"install {install}  (version {version_of(install)})")
    print(f"new     {new}  (version {version_of(new)})")
    print()
    print(f"  replace  {len(replace):>5}  package changed, install untouched")
    print(f"  skip     {len(skip):>5}  already current")
    print(f"  keep     {len(keep):>5}  locally edited, package unchanged")
    print(f"  conform  {len(conflict):>5}  package file you edited - will be conformed"
          f"{' (SKIPPED: --preserve-local)' if args.preserve_local else ''}")
    print(f"  added    {len(added):>5}  new files in this version")
    print(f"  sweep    {len(gone):>5}  in a strict lane, not in the new version"
          f"{' (KEPT: --keep-retired)' if args.keep_retired else ' - will be REMOVED'}")
    print(f"  blocks   {len(blocks):>5}  managed blocks to swap in live files")
    if live_conform:
        print(f"  boards   {len(live_conform):>5}  live files updated whole, USER-DEFINED "
              f"content carried")
    if unmigrated_live:
        print(f"  MIGRATE  {len(unmigrated_live):>5}  live files with no USER-DEFINED region "
              f"- managed block only")
        for rel in unmigrated_live:
            print(f"    migrate  {rel}")
        print("           Their rows sit outside any protected area, so the board's shape")
        print("           cannot be updated without risking them. To migrate:")
        print("             python tools/migrate_boards.py --install <dir> --new <dir> --check")
    if case_twins:
        print(f"  CASE     {len(case_twins):>5}  differ from a manifest path only by case - NOT swept")
        for rel in case_twins[:5]:
            match = next(k for k in incoming if k.lower() == rel.lower())
            print(f"    {rel}  vs manifest `{match}`")
        print("           On a case-insensitive filesystem these are ONE file and sweeping")
        print("           it would delete the real one. Rename by hand, then re-run.")
    if cfg:
        print(f"  config   {len(cfg[2])} keys to add, {len(cfg[3])} dropped upstream")
    if would_carry:
        print(f"  regions  {len(would_carry):>5}  files whose USER-DEFINED content is carried "
              f"across")
        for rel, names in would_carry[:8]:
            print(f"    keep     {rel}: {', '.join(names)}")
    if would_orphan:
        print(f"  ORPHAN   {len(would_orphan):>5}  user regions this version no longer offers "
              f"- NOT carried")
        for rel, names in would_orphan[:8]:
            print(f"    orphan   {rel}: {', '.join(names)}")
    for rel in conflict[:15]:
        print(f"    conform  {rel}")
    for rel in keep[:10]:
        print(f"    keep     {rel}")
    for rel in added[:10]:
        print(f"    added    {rel}")
    for rel in gone[:12]:
        print(f"    sweep    {rel}")
    if len(gone) > 12:
        print(f"    ... +{len(gone) - 12} more")
    for rel, ch in blocks[:10]:
        print(f"    block    {rel}: {', '.join(ch)}")
    if cfg and cfg[2]:
        print(f"    config   add keys: {', '.join(cfg[2])}")
    if cfg and cfg[3]:
        print(f"    config   dropped upstream (kept): {', '.join(cfg[3])}")

    if args.check:
        print()
        if conflict and args.preserve_local:
            print("CONFLICTS - --preserve-local will leave them untouched")
            return 1
        if conflict:
            print(f"READY - {len(conflict)} edited package files will be CONFORMED to the")
            print("        new version. Anything you need to keep belongs in user_defined/.")
        else:
            print("READY")
        return 0

    conform = not args.preserve_local
    carried_report: list[tuple[str, list[str]]] = []
    orphan_report: list[tuple[str, list[str]]] = []
    for rel in replace + added + live_conform + (conflict if conform else []):
        src, dst = new / rel, install / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        payload, carried, orphaned = conform_text(src.read_bytes(), dst)
        if carried:
            carried_report.append((rel, carried))
        if orphaned:
            orphan_report.append((rel, orphaned))
        dst.write_bytes(payload)

    for rel, _ in blocks:
        p = install / rel
        merged, _ = swap_managed(p.read_text(encoding="utf-8"),
                                 (new / rel).read_text(encoding="utf-8"))
        p.write_bytes(merged.encode("utf-8"))

    swept = 0
    if not args.keep_retired:
        for rel in gone:
            try:
                (install / rel).unlink()
                swept += 1
            except OSError as exc:
                print(f"    could not remove {rel}: {exc.strerror or exc}")
        for d in sorted((p for p in install.rglob('*') if p.is_dir()),
                        key=lambda x: len(x.parts), reverse=True):
            rel = d.relative_to(install).as_posix() + '/'
            if is_permissive(rel):
                continue
            try:
                if not any(d.iterdir()):
                    d.rmdir()
            except OSError:
                pass

    if cfg:
        rel, merged, a, _ = cfg
        if a:
            (install / rel).write_bytes(merged.encode("utf-8"))

    (install / MANIFEST_NAME).write_bytes((new / MANIFEST_NAME).read_bytes())

    print()
    print(f"APPLIED: replaced {len(replace)}, added {len(added)}, "
          f"blocks {len(blocks)}, config keys {len(cfg[2]) if cfg else 0}, "
          f"kept {len(keep)} local edits, "
          f"{'conformed' if conform else 'left'} {len(conflict)} edited package files, "
          f"swept {swept} retired")
    if carried_report:
        print(f"         user regions carried across in {len(carried_report)} file(s):")
        for rel, names in carried_report[:10]:
            print(f"           {rel}: {', '.join(names)}")
        print("         The package text around them was updated; your content was not.")
    if orphan_report:
        print(f"         {len(orphan_report)} file(s) hold a user region this version no")
        print("         longer offers. NOT carried, and the old file is gone - recover from")
        print("         version control if you need it:")
        for rel, names in orphan_report[:10]:
            print(f"           {rel}: {', '.join(names)}")
    if conflict and not conform:
        print("         Edited package files were NOT changed (--preserve-local).")
        print("         Each one is a divergence you will re-resolve on every future")
        print("         upgrade. Move what you need into user_defined/ instead.")
    if gone and args.keep_retired:
        print(f"         {len(gone)} retired files kept (--keep-retired). They are still"
              f" readable by agents.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
