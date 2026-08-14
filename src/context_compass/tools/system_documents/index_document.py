#!/usr/bin/env python3
"""Build a line-range index over an authored Markdown document.

For `src_components.md`, `src_architecture.md`, and any other large authored
system document. It reads the document and writes `<stem>_index.md` beside it.

**It never modifies the document.** The document is authored prose and stays
that way - there is no build step, no shards, and nothing is generated except
the index. That is the whole point: a component's responsibilities cannot be
derived from anything, so the document must remain the thing a human or agent
writes directly. This tool only makes it sliceable.

Contrast with the source graph, which IS derived from code and therefore does
have a generation pipeline under `tools/system_documents/python/`.

THE STALENESS CONTRACT
A line-offset index is more fragile than the prose it indexes. Insert one line
near the top and every range below it is wrong - while the index still parses,
still looks plausible, and still returns content. It returns the WRONG content,
confidently.

So an index is only trustworthy if it can be PROVEN current, and it carries the
proof itself: `line_count`, `content_sha256`, and `line_ending`. A consumer
recomputes all three and refuses to slice on any mismatch. An index without them
is not a weaker index, it is an unusable one.

Line numbers are 1-based and inclusive on both ends, matching `sed -n 'S,Ep'`,
the Read tool's offset/limit, and this repository's `path:start_line-end_line`
evidence convention.

Usage:
    # build or rebuild the index beside the document
    python index_document.py --doc system_docs/src_components.md
    python index_document.py --doc system_docs/src_architecture.md --max-level 3

    # verify the existing index is current; writes nothing
    python index_document.py --doc ... --check

    # read one section by NAME - verifies the index first, refuses if stale
    python index_document.py --doc ... --slice "Router and Role Resolution"

    # force sectioning strategy (default `auto`: ENTRY markers if present,
    # otherwise headings)
    python index_document.py --doc ... --mode entry
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import pathlib
import re
import sys

INDEX_VERSION = "1.1.0"
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FENCE = re.compile(r"^\s*(?:`{3}|~{3})")

# Explicit entry delimiters. Headings are inferred structure and depend on the
# author keeping levels consistent; these are declared structure and do not.
# Used by patch documents, where each entry is a distinct revision of a named
# thing and heading depth carries no meaning.
#
# The NAME lives in the marker, which is the point: it moves verbatim into the
# index, so an index row identifies the object it covers rather than a position
# in a file. A row keyed by a number is useless to anyone deciding what to read.
ENTRY_BEGIN = re.compile(r'^<!--\s*BEGIN ENTRY:\s*"?(.+?)"?\s*-->\s*$')
ENTRY_END = re.compile(r'^<!--\s*END ENTRY(?::\s*"?(.+?)"?)?\s*-->\s*$')


def write_if_changed(path: pathlib.Path, text: str, volatile: str = "generated_at") -> bool:
    """Write only when content differs ignoring the timestamp line. Returns wrote?

    Regeneration must be idempotent. If the source did not change, the index
    should not change either - otherwise every CI run or verification pass
    rewrites the file with a fresh `generated_at` and produces a diff that says
    nothing happened. A tool that churns its own output trains people to ignore
    its diffs, which is precisely when a real change slips past.
    """
    if path.exists():
        old = path.read_text(encoding="utf-8")
        strip = lambda s: "\n".join(l for l in s.split("\n") if volatile not in l)
        if strip(old) == strip(text):
            return False
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def read_lines(doc: pathlib.Path) -> tuple[bytes, str, list[str]]:
    """Return (raw_bytes, line_ending, lines). Trailing terminator is not a line."""
    raw = doc.read_bytes()
    nl = "\r\n" if b"\r\n" in raw else "\n"
    lines = raw.decode("utf-8").split(nl)
    if lines and lines[-1] == "":
        lines.pop()
    return raw, ("crlf" if nl == "\r\n" else "lf"), lines


def find_headings(lines: list[str], max_level: int) -> list[tuple[int, int, str]]:
    """Fence-aware heading scan. Returns (1-based line, level, title).

    A `#` inside a fenced code block is not a heading. Treating it as one
    produces ranges that split a code example in half.
    """
    out: list[tuple[int, int, str]] = []
    in_fence = False
    for i, line in enumerate(lines, start=1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING.match(line)
        if m and len(m.group(1)) <= max_level:
            out.append((i, len(m.group(1)), m.group(2)))
    return out


def find_entries(lines: list[str]) -> tuple[list[dict], list[str]]:
    """Scan explicit BEGIN/END ENTRY markers. Returns (entries, problems).

    Unbalanced or mismatched markers are reported rather than guessed at. A
    silently repaired entry boundary produces a range that looks fine and covers
    the wrong text.
    """
    entries: list[dict] = []
    problems: list[str] = []
    open_at: int | None = None
    open_name: str | None = None
    in_fence = False
    for i, line in enumerate(lines, start=1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        b = ENTRY_BEGIN.match(line)
        if b:
            if open_at is not None:
                problems.append(f"line {i}: BEGIN ENTRY {b.group(1)!r} while "
                                f"{open_name!r} still open at line {open_at}")
            open_at, open_name = i, b.group(1).strip()
            continue
        e = ENTRY_END.match(line)
        if e:
            if open_at is None:
                problems.append(f"line {i}: END ENTRY with nothing open")
                continue
            closing = (e.group(1) or "").strip()
            if closing and closing != open_name:
                problems.append(f"line {i}: END ENTRY {closing!r} closes "
                                f"{open_name!r} opened at line {open_at}")
            entries.append({"level": 1, "path": open_name, "title": open_name,
                            "start": open_at, "end": i})
            open_at, open_name = None, None
    if open_at is not None:
        problems.append(f"BEGIN ENTRY {open_name!r} at line {open_at} never closed")
    return entries, problems


def build_sections(lines: list[str], found: list[tuple[int, int, str]]) -> list[dict]:
    """Heading list -> sections with ranges and breadcrumb paths.

    A section runs from its own heading line to the line before the next heading
    of the SAME OR SHALLOWER depth, or to end of file for the last one.

    The document TITLE is omitted. A lone `#` heading is the document's name, not
    a navigable section, and its range necessarily spans nearly the whole file -
    an entry whose only possible use is to defeat the index while appearing to
    use it.

    The title is also stripped from every breadcrumb. Repeating the document name
    on every row is pure redundancy: on a 156-row index it measured ~1,100 tokens
    of a value that is identical on every line.
    """
    if not found:
        return []
    levels = [lv for _, lv, _ in found]
    min_level = min(levels)
    lone_title = levels.count(min_level) == 1
    root_title = found[0][2] if lone_title else None

    sections: list[dict] = []
    stack: list[tuple[int, str]] = []
    for idx, (start, level, title) in enumerate(found):
        end = len(lines)
        for nxt_start, nxt_level, _ in found[idx + 1:]:
            if nxt_level <= level:
                end = nxt_start - 1
                break
        while stack and stack[-1][0] >= level:
            stack.pop()
        crumbs = [t for _, t in stack] + [title]
        stack.append((level, title))
        if lone_title and level == min_level:
            continue                                    # the document title
        if root_title and crumbs and crumbs[0] == root_title:
            crumbs = crumbs[1:]                         # drop the repeated root
        sections.append({"level": level, "path": " > ".join(crumbs),
                         "title": title, "start": start, "end": end})
    return sections


def render(doc: pathlib.Path, raw: bytes, line_ending: str,
           lines: list[str], sections: list[dict]) -> str:
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = [
        f"# {doc.stem}_index",
        "",
        f"Line ranges into `{doc.name}`. Derived: regenerated by re-walking the",
        "document, never hand-edited. Hand-editing a range is how an index starts",
        "lying.",
        "",
        "Line numbers are 1-based and inclusive on both ends.",
        "",
        "## Staleness proof",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| document | `{doc.name}` |",
        f"| index_version | {INDEX_VERSION} |",
        f"| generated_at | {stamp} |",
        f"| line_count | {len(lines)} |",
        f"| line_ending | {line_ending} |",
        f"| content_sha256 | `{hashlib.sha256(raw).hexdigest()}` |",
        f"| sections | {len(sections)} |",
        "",
        "Recompute all three of `line_count`, `line_ending`, and `content_sha256`",
        "before slicing. On any mismatch: STOP, do not slice, do not eyeball an",
        "offset. Regenerate this index or read the document directly, and say",
        "which you did.",
        "",
        "## Sections",
        "",
        "| lines | lvl | name |",
        "| --- | --- | --- |",
    ]
    for s in sections:
        out.append(f"| {s['start']}-{s['end']} | {s['level']} | {s['path']} |")
    out.append("")
    return "\n".join(out)


def format_warnings(lines: list[str], found: list[tuple[int, int, str]],
                    sections: list[dict]) -> list[str]:
    """Format violations the index cannot repair, reported not silently accepted.

    These are documented rules in `system_document_build.md`. A tool that states
    a rule and then quietly produces a degraded index when the rule is broken is
    worse than one with no rule: the index still looks usable.

    Both conditions here were found by testing rather than assumed:

    - MULTIPLE H1: the title-omission logic needs a lone top-level heading to
      identify the title. With two, neither is omitted and one section spans
      most of the file - the exact "defeats the index while appearing to use it"
      failure the omission exists to prevent.
    - DUPLICATE NAMES: `--slice` matches on name, so two sections sharing one
      are unaddressable. The slice refuses at read time, but the author who
      created the collision is the person who can fix it, and they are here.
    - WRAPPED HEADING: a heading whose text was reflowed across physical lines
      parses as several headings. The first indexes as a one-line fragment and
      wins "narrowest match", so `--slice` hands back a stub. Observed in the
      wild spanning five physical lines. Unbalanced brackets are the reliable
      tell: prose wraps mid-parenthesis far more often than a real heading ends
      with one open.
    """
    warnings: list[str] = []
    for i, lv, title in found:
        for opener, closer in (("(", ")"), ("[", "]")):
            if title.count(opener) > title.count(closer):
                warnings.append(
                    f"line {i}: heading has an unclosed '{opener}' - "
                    f"'{title[:60]}{'...' if len(title) > 60 else ''}'. A heading "
                    f"reflowed across lines indexes as several sections and "
                    f"--slice returns a fragment. Put it on one line.")
                break
    if found:
        top = min(lv for _, lv, _ in found)
        h1s = [(i, t) for i, lv, t in found if lv == top]
        if len(h1s) > 1:
            warnings.append(
                f"{len(h1s)} level-{top} headings; expected exactly one document "
                f"title. No title will be omitted and a section will span most of "
                f"the file. Lines: " + ", ".join(str(i) for i, _ in h1s[:6]))
    seen: dict[str, list[str]] = {}
    for s in sections:
        seen.setdefault(s["title"], []).append(f"{s['start']}-{s['end']}")
    for title, ranges in seen.items():
        if len(ranges) > 1:
            warnings.append(f"duplicate section name {title!r} at {', '.join(ranges)} - "
                            f"`--slice` cannot address either")
    return warnings


def validate(lines: list[str], sections: list[dict]) -> list[str]:
    """Round-trip, monotonicity, and bounds. Checked, never assumed.

    An off-by-one is the failure mode that silently corrupts every downstream
    read, so the first sliced line of each section is compared against the title
    the index claims lives there.
    """
    problems: list[str] = []
    for s in sections:
        head = lines[s["start"] - 1]
        if s.get("kind") == "entry":
            m = ENTRY_BEGIN.match(head)
            if not m or m.group(1).strip() != s["title"]:
                problems.append(f"line {s['start']} is {head!r}, expected "
                                f"BEGIN ENTRY {s['title']!r}")
        else:
            m = HEADING.match(head)
            if not m or m.group(2) != s["title"]:
                problems.append(f"line {s['start']} is {head!r}, expected heading "
                                f"{s['title']!r}")
        if not (1 <= s["start"] <= s["end"] <= len(lines)):
            problems.append(f"{s['title']}: range {s['start']}-{s['end']} out of bounds")
    for a, b in zip(sections, sections[1:]):
        if b["start"] <= a["start"]:
            problems.append(f"non-monotonic: {a['title']} then {b['title']}")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--doc", required=True, type=pathlib.Path)
    ap.add_argument("--max-level", type=int, default=3,
                    help="deepest heading level to index (default 3)")
    ap.add_argument("--mode", choices=("auto", "heading", "entry"), default="auto",
                    help="auto uses ENTRY markers when present, else headings")
    ap.add_argument("--check", action="store_true",
                    help="verify the existing index is current; write nothing")
    ap.add_argument("--slice", metavar="NAME",
                    help="print the lines of the section whose name contains NAME "
                         "(verifies the index first; refuses on any mismatch)")
    args = ap.parse_args()

    doc: pathlib.Path = args.doc
    if not doc.is_file():
        print(f"document not found: {doc}", file=sys.stderr)
        return 2

    # Two refusals. Both exist because this tool WRITES, and a wrong target does
    # not produce a confusing message you shrug off - it produces a plausible
    # file that replaces a correct one. Reading the wrong document costs seconds;
    # writing over the right one costs the artifact.
    if doc.stem.endswith("_index"):
        print(f"refusing: {doc.name} is already an index.", file=sys.stderr)
        print("  Indexing an index produces <stem>_index_index.md, which addresses "
              "nothing. Point --doc at the document instead.", file=sys.stderr)
        return 2

    if "<!-- BEGIN FILE:" in doc.read_text(encoding="utf-8", errors="ignore"):
        companion = doc.with_name(f"{doc.stem}_index.md")
        print(f"refusing: {doc.name} is an ASSEMBLED graph, not an authored document.",
              file=sys.stderr)
        print(f"  Its index is a byproduct of assembly - `assemble_graph.py` knows each",
              file=sys.stderr)
        print(f"  range because it emitted those lines, so index and document cannot",
              file=sys.stderr)
        print(f"  disagree. Re-indexing it here would re-parse headings instead, and",
              file=sys.stderr)
        print(f"  overwrite {companion.name} with a weaker index keyed by heading",
              file=sys.stderr)
        print(f"  breadcrumb rather than source path. Run assemble_graph.py.",
              file=sys.stderr)
        return 2

    raw, line_ending, lines = read_lines(doc)
    entries, entry_problems = find_entries(lines)
    if args.mode == "entry" or (args.mode == "auto" and entries):
        if entry_problems:
            print(f"ENTRY MARKERS MALFORMED: {len(entry_problems)} problem(s). "
                  f"Nothing written.", file=sys.stderr)
            for p in entry_problems[:15]:
                print(f"  {p}", file=sys.stderr)
            return 1
        sections = [dict(e, kind="entry") for e in entries]
        mode_used = "entry markers"
    else:
        found = find_headings(lines, args.max_level)
        sections = [dict(s, kind="heading") for s in build_sections(lines, found)]
        mode_used = f"headings (level <= {args.max_level})"
    if not sections:
        print(f"no sections found in {doc.name} using {mode_used}", file=sys.stderr)
        return 2

    for w in format_warnings(lines, find_headings(lines, args.max_level), sections):
        print(f"  FORMAT WARNING: {w}", file=sys.stderr)

    problems = validate(lines, sections)
    if problems:
        print(f"VALIDATION FAILED: {len(problems)} problem(s). Nothing written.",
              file=sys.stderr)
        for p in problems[:15]:
            print(f"  {p}", file=sys.stderr)
        return 1

    index_path = doc.with_name(f"{doc.stem}_index.md")
    text = render(doc, raw, line_ending, lines, sections)

    if args.slice:
        # Verify against the index ON DISK, not against what we just computed.
        # Slicing off a freshly derived section table would prove nothing: the
        # whole point is to catch a document that moved since the index was
        # written.
        if not index_path.exists():
            print(f"NO INDEX: {index_path.name}. Generate it before slicing.",
                  file=sys.stderr)
            return 1
        on_disk = index_path.read_text(encoding="utf-8")
        want_hash = re.search(r"content_sha256 \| `([0-9a-f]{64})`", on_disk)
        want_count = re.search(r"line_count \| (\d+)", on_disk)
        live = hashlib.sha256(raw).hexdigest()
        if (not want_hash or want_hash.group(1) != live
                or not want_count or int(want_count.group(1)) != len(lines)):
            print(f"INDEX STALE - refusing to slice. Regenerate {index_path.name}.",
                  file=sys.stderr)
            return 1
        needle = args.slice.lower()

        # Resolve in three passes, narrowest first. A pure substring match makes a
        # section unreachable whenever its name is contained in another name, and
        # that is not a rare edge: measured across the six system documents in this
        # repository, 21 of 292 sections could not be addressed by name at all.
        #
        # Two families produced all of them:
        #   - a parent heading is a substring of its own children's breadcrumbs, so
        #     `C1 Code Map (Core Only)` also matched `C1 Code Map (Core Only) > ...`
        #   - `Component: X` matched `Subcomponent: X`, because the compare is
        #     lowercased and `component: x` occurs inside `subcomponent: x`
        #
        # Both are exactly resolvable: the caller typed a whole name, and a whole
        # name that equals a section's own name should win over one that merely
        # contains it. Substring stays as the last pass so partial queries still
        # work and still list candidates rather than guessing.
        exact_path = [s for s in sections if s["path"].lower() == needle]
        exact_leaf = [s for s in sections
                      if s["path"].split(">")[-1].strip().lower() == needle]
        substring = [s for s in sections if needle in s["path"].lower()]
        hits = exact_path or exact_leaf or substring

        if not hits:
            print(f"no section matching {args.slice!r}. Read {index_path.name} "
                  f"for the available names.", file=sys.stderr)
            return 1
        if len(hits) > 1:
            print(f"{len(hits)} sections match {args.slice!r} - narrow it:",
                  file=sys.stderr)
            for h in hits:
                print(f"  {h['start']}-{h['end']}  {h['path']}", file=sys.stderr)
            print("  (an exact section name wins over a partial one - copy a name "
                  "from the index verbatim)", file=sys.stderr)
            return 1
        s = hits[0]

        # Warn when the resolved section is a CONTAINER - a heading that wraps only
        # other headings and carries no prose of its own.
        #
        # This warning exists because exact-name resolution created the hazard. While
        # matching was substring-only a container also matched every child, so the
        # ambiguity list accidentally shielded a caller from selecting one. Resolving
        # exact names removed that accident: `C3 Components Catalog` now returns 1,149
        # lines, 38% of the document, to someone who believes they sliced one section.
        # That is the failure the format contract calls out by name.
        #
        # The request is still honoured - an exact name is an explicit choice, and
        # refusing it would make the container the one section nobody can read. It is
        # answered on stderr so a piped slice stays clean.
        kids = [k for k in sections
                if k is not s and s["start"] <= k["start"] and k["end"] <= s["end"]]
        if kids:
            first = min(k["start"] for k in kids)
            own = "".join(x.strip() for x in lines[s["start"]:first - 1])
            if not own:
                span = s["end"] - s["start"] + 1
                print(f"NOTE: {s['path']!r} is a container - it holds only sub-headings, "
                      f"and this returned {span} lines ({100 * span // len(lines)}% of the "
                      f"document).", file=sys.stderr)
                print(f"  Its {len(kids)} child sections are listed in {index_path.name}; "
                      f"selecting one of those is almost always what was meant.",
                      file=sys.stderr)

        print(f"<!-- {doc.name}:{s['start']}-{s['end']}  {s['path']} -->")
        print("\n".join(lines[s["start"] - 1:s["end"]]))
        return 0

    if args.check:
        if not index_path.exists():
            print(f"MISSING: {index_path.name}", file=sys.stderr)
            return 1
        current = index_path.read_text(encoding="utf-8")
        cur_hash = re.search(r"content_sha256 \| `([0-9a-f]{64})`", current)
        cur_count = re.search(r"line_count \| (\d+)", current)
        live = hashlib.sha256(raw).hexdigest()
        stale = []
        if not cur_hash or cur_hash.group(1) != live:
            stale.append("content_sha256 mismatch")
        if not cur_count or int(cur_count.group(1)) != len(lines):
            stale.append(f"line_count {cur_count.group(1) if cur_count else '?'} "
                         f"-> {len(lines)}")
        if stale:
            print(f"STALE: {index_path.name} - " + "; ".join(stale), file=sys.stderr)
            return 1
        print(f"OK: {index_path.name} is current "
              f"({len(sections)} sections over {len(lines)} lines)")
        return 0

    wrote = write_if_changed(index_path, text)
    biggest = max(sections, key=lambda s: s["end"] - s["start"])
    idx_lines = len(text.split("\n"))
    print(f"{'WROTE' if wrote else 'UNCHANGED'}: {index_path.name}")
    print(f"  {len(sections)} sections over {len(lines)} document lines")
    print(f"  index {idx_lines} lines ({100 * idx_lines // len(lines)}% of document)")
    print(f"  sectioned by: {mode_used}")
    print(f"  deepest level indexed: {max(s['level'] for s in sections)}")
    print(f"  largest section: {biggest['end'] - biggest['start'] + 1} lines "
          f"({biggest['title'][:48]})")
    print(f"  all {len(sections)} ranges validated against their own headings")
    print(f"  the document was NOT modified: {doc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
