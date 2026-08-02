#!/usr/bin/env python3
"""Move an existing board's content into USER-DEFINED regions.

Run this ONCE per install when a board predates the regions. After it succeeds,
the updater can conform the board's whole shape - headings, table headers,
contract prose - while leaving everything inside the regions alone.

WHY A BOARD NEEDS MIGRATING AT ALL

A board written before the regions has all of its rows in open text. The
updater cannot conform such a file, because "everything outside a MANAGED
block" is simultaneously the package's stale headings AND the install's live
rows, and nothing distinguishes them. So it swaps only the managed block and
leaves the rest frozen - which is why an install could end up with the managed
block sitting above its own H1, a duplicated directive below it, and no upgrade
able to repair either.

WHAT THIS DOES

For each `## Heading` the NEW board declares with a user region, it takes the
install's content under the SAME heading and puts it inside that region. Table
header rows and separator rows are dropped, because the new board supplies its
own; everything else is carried verbatim.

WHAT IT REFUSES TO DO

Content under a heading the new board does NOT have a region for is never
discarded and never guessed at. It is reported, and parked in the board's
`notes` region if one exists, so the migration cannot silently lose a section
somebody was using.

    python migrate_boards.py --install <dir> --new <dir> --check
    python migrate_boards.py --install <dir> --new <dir> --apply
"""

from __future__ import annotations

import argparse
import difflib
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from package_manifest import MANIFEST_NAME, parse, check_manifest_compatible  # noqa: E402
from cleanup_context_compass import user_regions, managed_blocks  # noqa: E402

HEADING = re.compile(r"^##\s+(.+?)\s*$")
TABLE_ROW = re.compile(r"^\s*\|")
SEPARATOR = re.compile(r"^\s*\|[\s|:-]+\|\s*$")


def strip_managed(text: str) -> str:
    """Remove managed blocks so their prose is not mistaken for install content."""
    for _, s, e in sorted(managed_blocks(text), key=lambda b: -b[1]):
        text = text[:s] + text[e:]
    return text


def sections(text: str) -> dict[str, list[str]]:
    """Map each `## Heading` to the lines beneath it, up to the next H2."""
    out: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.split("\n"):
        m = HEADING.match(line)
        if m:
            current = m.group(1)
            out.setdefault(current, [])
            continue
        if current is not None:
            out[current].append(line)
    return out


def is_content(line: str) -> bool:
    """A line worth carrying: not blank, not a table header or separator."""
    if not line.strip():
        return False
    if SEPARATOR.match(line):
        return False
    return True


def region_for_heading(new_text: str, heading: str) -> str | None:
    """The region name declared under `heading` in the new board, if any."""
    current: str | None = None
    for line in new_text.split("\n"):
        m = HEADING.match(line)
        if m:
            current = m.group(1)
            continue
        r = re.match(r"<!-- BEGIN USER-DEFINED(?::\s*(.+?))?\s*-->", line.strip())
        if r and current == heading:
            return (r.group(1) or "").strip()
    return None


def place(new_text: str, name: str, body_lines: list[str]) -> str:
    """Put `body_lines` inside the named region of `new_text`."""
    for rname, s, e in user_regions(new_text):
        if rname == name:
            body = "\n" + "\n".join(body_lines) + "\n" if body_lines else "\n"
            return new_text[:s] + body + new_text[e:]
    return new_text


def migrate_board(current: str, incoming: str) -> tuple[str, dict[str, int], list[str]]:
    """Return (migrated_text, {region: rows_carried}, unplaced_headings)."""
    cur_sections = sections(strip_managed(current))
    out = incoming
    carried: dict[str, int] = {}
    unplaced: list[str] = []

    for heading, lines in cur_sections.items():
        content = [l for l in lines if is_content(l)]
        # A table header row is package-supplied; drop it, keep data rows.
        content = [l for l in content
                   if not (TABLE_ROW.match(l) and l in incoming)]
        if not content:
            continue
        name = region_for_heading(incoming, heading)
        if name is None:
            unplaced.append(heading)
            continue
        out = place(out, name, content)
        carried[name or "(unnamed)"] = len(content)

    if unplaced and region_for_heading(incoming, "Notes") is not None:
        parked: list[str] = []
        for heading in unplaced:
            parked.append(f"### {heading} (carried from the pre-region board)")
            parked.extend(l for l in cur_sections[heading] if is_content(l))
            parked.append("")
        name = region_for_heading(incoming, "Notes") or ""
        existing = ""
        for rname, s, e in user_regions(out):
            if rname == name:
                existing = out[s:e].strip("\n")
        body = ([existing] if existing else []) + parked
        out = place(out, name, body)

    return out, carried, unplaced


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--install", required=True, type=pathlib.Path)
    ap.add_argument("--new", required=True, type=pathlib.Path,
                    help="the new package, whose boards declare the regions")
    ap.add_argument("--check", action="store_true", help="report only, write nothing")
    ap.add_argument("--apply", action="store_true", help="rewrite the boards")
    ap.add_argument("--diff", action="store_true", help="print a unified diff per board")
    args = ap.parse_args()

    if not (args.new / MANIFEST_NAME).is_file():
        print(f"ERROR: --new {args.new} has no {MANIFEST_NAME}")
        return 2
    if not args.check and not args.apply:
        print("Refusing to act without --apply. Use --check to see the plan.")
        return 2

    manifest_text = (args.new / MANIFEST_NAME).read_text(encoding="utf-8")
    problem = check_manifest_compatible(manifest_text, f"--new {args.new}")
    if problem:
        print(f"ERROR: {problem}")
        return 2
    manifest = parse(manifest_text)
    boards = sorted(rel for rel, (cls, _) in manifest.items() if cls == "LIVE")
    if not boards:
        print("no LIVE files in the new package's manifest - nothing to migrate")
        return 0

    changed = 0
    for rel in boards:
        cur_path, new_path = args.install / rel, args.new / rel
        if not cur_path.is_file() or not new_path.is_file():
            print(f"  SKIP {rel} (missing on one side)")
            continue
        current = cur_path.read_text(encoding="utf-8")
        incoming = new_path.read_text(encoding="utf-8")

        if user_regions(current):
            print(f"  OK   {rel} already has USER-DEFINED regions")
            continue
        if not user_regions(incoming):
            print(f"  SKIP {rel} - the new version declares no regions")
            continue

        migrated, carried, unplaced = migrate_board(current, incoming)
        total = sum(carried.values())
        print(f"  MOVE {rel}: {total} line(s) into {len(carried)} region(s)")
        for name, n in sorted(carried.items()):
            print(f"         {name}: {n}")
        if unplaced:
            print(f"         parked in `notes` (no region for these headings): "
                  f"{', '.join(unplaced)}")
        if args.diff:
            for line in difflib.unified_diff(
                    current.split("\n"), migrated.split("\n"),
                    fromfile=f"a/{rel}", tofile=f"b/{rel}", lineterm=""):
                print(f"    {line}")

        if args.apply:
            cur_path.write_bytes(migrated.encode("utf-8"))
            changed += 1

    print()
    if args.check:
        print("READY - run again with --apply, then re-run the updater.")
        return 0
    print(f"APPLIED: {changed} board(s) migrated. Re-run update_context_compass.py;")
    print("         they will now conform whole with your content preserved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
