

# tests_components_instructions

## Purpose
- Define the exact build protocol for
  `context_compass/system_docs/tests_components.md`.
- Produce evidence-backed C3/C2/C1 test component mapping aligned to test
  architecture boundaries.

## Canonical Output
- `context_compass/system_docs/tests_components.md`

## Example Documents (Required Read)
- `context_compass/examples/example_components/tests_components.md`
- `context_compass/examples/example_components/src_components.md`
- `context_compass/examples/example_architecture/tests_architecture.md`
- `context_compass/examples/example_architecture/src_architecture.md`

The canonical output does not ship with the package. `system_docs/` is empty in
a fresh install, so on first run you are creating this document, not editing
one. The examples above are the shape reference; this repository is the source
of truth for the content.

## Required Inputs (Read First)
- `context_compass/system_docs/tests_architecture.md`
- `context_compass/system_docs/src_architecture.md`
- `context_compass/system_docs/src_components.md`
- `context_compass/system_docs/src_graph.md`
- `context_compass/agent_onboarding/default/design_engineer/skills/tests_architecture_instructions.md`
- Active ticket and `context_compass/attention_board.md` route

## Indexing Contract (Non-Negotiable)

This document is AUTHORED. Nothing generates its prose. The only generated
artifact is its index, and the index is only as useful as the heading structure
you give it.

Regenerate the index in the SAME pass that edits the document:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/tests_components.md
```

Heading discipline the index depends on:
- **Exactly one H1.** A second one and the indexer cannot identify the document
  title, so it stops omitting it and emits a section spanning the whole file.
- **The navigable unit is H3 `### Component: <Name>`.** Consistent depth, never mixed.
- **Names unique and stable.** Index rows are selected on name; two sections
  sharing a name are indistinguishable to a consumer.
- **Never leave a container heading as the read target.** `## C3 Components
  Catalog` wraps only other headings, so it indexes as a range covering every
  component beneath it. Select a component, never the catalog. Measured on a
  production `src_components.md` that catalog indexes as a **1,945-line**
  section, so a reader selecting it loads 37% of the document believing they
  sliced it. The same shape applies to whatever you write here.

Consume the index by slicing, never by reading the document whole:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/tests_components.md --slice "<section name>"
```

It verifies the index before returning anything, refuses on a stale index, and
lists candidates rather than guessing when a name is ambiguous. Section names
are therefore the query - keep them unique and descriptive.

Verify before trusting any range:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/tests_components.md --check
```

An index records `line_count`, `content_sha256`, and `line_ending`. Insert one
line near the top and every range below it is wrong while still parsing and
still returning content - the WRONG content, confidently. On mismatch: STOP,
regenerate, do not eyeball an offset.

Full format specification:
`agent_onboarding/default/engineer/skills/system_document_build.md`

## Unknowns Gate (Non-Negotiable)
- New component claims default to `UNKNOWN`.
- Promote to `FACT` only with concrete evidence.
- Preserve unresolved UNKNOWNs; do not normalize into assumptions.

## Required Section Contract
`tests_components.md` must contain these sections in order:
1. `## Metadata`
2. `## Scope`
3. `## Indexing`
4. `## DO NOT ASSUME / Unknowns Gate`
5. `## Unknowns`
6. `## C3 Components Catalog`
7. `## C2 Subcomponents Catalog`
8. `## Method-Level Call Flows (C1)`
9. `## C1 Code Map (Core)`
10. `## Diagrams`
11. `## Information Sources`
12. `## Context / Handoff Summary`

### The document names no path into this package

`tests_components.md` is committed to the repository it describes and, in a
packaged project, ships inside the wheel. Every reader of that copy has the code
and does not have Context Compass. A line like
`context_compass/tools/system_documents/index_document.py` resolves for you and
for nobody downstream.

**No path in the produced document points into this package - written either
way.** `context_compass/tools/system_documents/index_document.py` and a bare
`tools/system_documents/index_document.py` are the same file; the second merely
drops the prefix because whoever wrote it was thinking install-relative. The
unprefixed form is the commoner leak and much the easier to miss, so the rule is
about the destination, not the spelling. The same goes for `agent_onboarding/`,
`system_docs/`, `patches/active/` and any tool filename.

Not in `## Indexing`, not in `## Information Sources`, not in a Key Files list,
not in a cross-reference. This is a hard rule, and it is checked in the Quality
Gate.

- **Maintenance commands are relocated, not deleted.** The command that rebuilds
  the index lives in this skill, which is where a maintainer already is when
  they need it. The document's `## Indexing` section states that an index
  companion exists and what heading rules it depends on. A reader needs both
  facts and neither one requires naming a tool.
- **Cross-references use a logical document id**: `tests_architecture`, not
  `context_compass/system_docs/tests_architecture.md`. The id survives the
  document being vendored, renamed, or published under a different root. The
  path does not.
- **Paths into the subject stay, and stay repo-relative.** `tests/unit/test_x.py`
  in a C1 entry or a Key Files list is exactly right - that is the suite being
  documented and it is the whole point of the entry. Relative to the repository
  root, never absolute: `C:\Users\...\tests\unit\test_x.py` encodes one
  machine's checkout location into a document that gets committed and shipped,
  so it is wrong for every reader who is not you, and it breaks the moment the
  repo is cloned anywhere else. The rule bans paths into the tooling that
  produced the document, never paths into the thing it describes.

`src_graph.md` is the model to copy: it is fully generated and contains zero
install-prefixed paths.

### Sections not in the contract

The contract is a **minimum in a fixed relative order**, not a whitelist. Other
sections are permitted and are common. Measured on one real architecture
document: 44 H2 sections against its 17-section contract - read literally as
"only these sections", a recomposition deletes roughly 1,200 lines. That figure
is from the source side; the ratio is what carries over. The contract above
lists twelve, and a mature test components document will exceed it too.

If material genuinely does not belong here, it is **moved, never deleted**:

- relocate it to a named target - the patch lane
  (`system_docs/patches/active/<patch_id>/`) is the conventional destination
- name that target in `## Context / Handoff Summary`
- state plainly that until it is re-absorbed it lives in neither canonical
  document

"Delete it because the contract does not list it" is never the right answer.

### What "core" means

**Core is the deduplicated union of every `Key Files (C1)` list in the C3
catalog.** A file a component claims as its own is core by that component's own
claim, and the set maintains itself: change a component's key files and the core
set follows, so nothing new has to be tracked.

Measured on the source side of one real package: 574 modules resolved to 170
core paths - a scope an agent can actually verify, against an inventory it
cannot. The same reduction is what makes this tractable for a test tree.

An exhaustive inventory is still useful. Keep it, do not let the rename delete
it: put it beneath as `### Full Package Inventory (exhaustive, retained)`.
Narrowing a section's scope is not a licence to destroy what was there.

## Component Entry Contract (C3 Minimum)
Each C3 test component must include:
- `Purpose`
- `Responsibilities`
- `Inputs`
- `Outputs`
- `Owned State`
- `Lifecycle/Cleanup`
- `Concurrency/Threading`
- `Invariants/Guarantees`
- `Failure Modes`
- `Observability`
- `Extension Points`
- `Key Files (C1)`

**`Key Files (C1)` cites in-scope TEST paths only.** This is the mirror of the
source-side rule, and it runs the other way: `src_components.md` cites source
paths because that is what its graph is keyed by, and this document cites test
paths because test surfaces are its subject. A source path here is the same
category error as a test path there. If a test component needs to name the code
it exercises, name it in `Purpose` or `Responsibilities` as the thing under test,
not in `Key Files`.

**There is no graph to join against on this side, and that is the asymmetry.**
The source-side skill can hand you a `comm -23` recipe because every source file
has a row in `src_graph_index.md`. No equivalent index exists for the test tree,
so nothing will tell you a path here has rotted. Verify by existence and
remeasure every range on every pass:

```bash
DOC=context_compass/system_docs/tests_components.md

# Same extraction the source-side skill uses: the two contract fields that hold
# paths, not every backtick - code-fence tags are backticked too, and a check
# that reports `bash` as a missing file gets ignored by its second run.
{ grep -o 'Key Files (C1):.*' "$DOC"; grep -o '^- path: .*' "$DOC"; } \
  | grep -o '`[^`]*`' | tr -d '`' | grep -v '[*?]' | sort -u \
  | while read -r p; do [ -e "$p" ] || echo "MISSING $p"; done
```

Match `` `[^`]*` `` **including both backticks**: a lookahead form like
`` `\K[^`]+(?=`) `` resumes at the closing backtick, treats it as an opening
one, and reports the `, ` between two cited paths as a path. `grep -v '[*?]'`
drops globs - a glob is a statement about a set, not a citation that resolves to
one file. Existence is the weaker check; it catches a deleted file but not a
range that has drifted inside a file that still exists, which is why ranges here
are remeasured rather than trusted.

This is the same twelve-field minimum `src_components_instructions.md` requires.
Test components are components. If a field genuinely does not apply, say so in
the field rather than dropping it - a missing field and a deliberately empty one
look identical to a reader, and only one of them is a decision.

## C1 Flow/Map Contract
- Call-flow entries must include concrete test methods/functions/fixtures.
- C1 map entries must include:
  - `path`
  - `start_line`
  - `end_line`
  - `loc`
  - `verified_at` (UTC DateTime `YYYY-MM-DDTHH:MM:SSZ`)

**Directories are not valid C1 entries.** A directory has no line range, so a
citation to one carries no evidence and cannot be verified or remeasured. Expand
it into its constituent test files - excluding whatever the test scope already
excludes - and measure each. Do not write `UNKNOWN` for a directory: `UNKNOWN`
means "not yet verified and here is the investigation target", and a directory is
unverifiable in principle - the marker would sit there forever with nothing to
resolve it.

Ranges are measured, never estimated. If the exact range is not verified, keep
the claim `UNKNOWN` and add an investigation target in `## Unknowns` rather than
writing a plausible number.

## Build Sequence (Bottom-Up, Required)
1. Confirm active ticket route and test component scope.
2. If the document already exists, capture the Content Preservation baseline
   now, before the first edit. Captured later it proves nothing.
3. Read required example documents and extract reusable C3/C2/C1 patterns.
4. Re-read tests architecture boundaries and terminology.
5. Unwrap any heading spanning more than one physical line. A reflowed heading
   parses as several sections; the first wins "narrowest match" and `--slice`
   returns a stub. `index_document.py` warns on unclosed brackets, which is the
   usual tell, but it cannot catch every wrap - scan the heading list once
   before you trust it.
6. Draft/refresh metadata, scope, unknowns gate, and unknowns inventory.
7. Build C3 test component catalog with entry-contract fields.
8. Build C2 subcomponents and wiring/dependency notes.
9. Capture method-level C1 flows (fixtures, harnesses, execution paths).
10. Build the C1 core map with ranges, LOC, and verification timestamps.
11. Add diagrams aligned to terminology and flow.
12. If patch lane is active, confirm the component patch has not moved a
    boundary this document still describes the old way.
13. Refresh `Information Sources` and `Context / Handoff Summary`.
14. Rebuild the index in this same pass, then satisfy the Content Preservation
    Gate and the Quality Gate.

If a test component claim conflicts with `tests_architecture.md` or with the
component it verifies in `src_components.md`, log `CONFLICT` in ticket notes and
escalate before proceeding. The mismatch is the finding; resolving it silently
in either direction destroys it.

## Content Preservation Gate (Non-Negotiable)

**Structural checks cannot see content loss.** Every check in the Quality Gate
below is structural - sections present, fields present, ranges present. A
recomposition can pass all of them while having silently destroyed text.

This is not hypothetical. A real recomposition of a 2,249-line architecture
document lost ~170 lines to a regex that captured only the description text on
the same physical line as the path: fifteen wrapped descriptions truncated, two
destroyed outright, and a previous `## Context / Handoff Summary` overwritten,
taking a record of decisions in force with it. All six structural checks passed
the entire time. It was caught by a human noticing the file had shrunk.

So, before the first transform:

1. Capture a **multiset** of the document's non-blank, whitespace-normalised
   lines. Counts, not a set - a set cannot see that a line appearing three times
   now appears once.
2. Do the work.
3. Re-capture and compare. Every line from the baseline must appear either in
   the resulting document or in a **named migration target** you can point at.

```bash
# BEFORE the first transform
grep -v '^[[:space:]]*$' DOC.md | sed 's/[[:space:]]\+/ /g' | sort | uniq -c > /tmp/before.txt

# AFTER - the document PLUS every target you moved material into
cat DOC.md MIGRATION_TARGET.md ... | grep -v '^[[:space:]]*$' \
  | sed 's/[[:space:]]\+/ /g' | sort | uniq -c > /tmp/after.txt

diff /tmp/before.txt /tmp/after.txt
```

**The `after` capture must span the document and its migration targets.**
Comparing the document against itself contradicts the rule above: relocation is
explicitly allowed, so every legitimately moved line reports as loss. That fires
hardest on a recomposition that moves material - the exact case this gate exists
for - and a gate that cries wolf is disabled by the second person who hits it.

**The baseline must be captured BEFORE the first edit.** Captured afterwards it
proves nothing - it describes the document you already built, which is the exact
trap that makes "I verified it" feel true while content is gone.

**Reformatting reads as loss under a line comparison.** Rewrapping prose or
changing a record's shape leaves the content intact and the line text different,
so this recipe flags it. When a pass deliberately reshapes entries, compare
extracted content - the paths, the field values, the claims - rather than raw
lines, or the gate fails on work that lost nothing. Do not respond by relaxing
the gate; respond by comparing the right thing.

A line legitimately removed is fine. A line you cannot account for is a defect,
and this gate fails until you can name where it went.

## Quality Gate (Pass/Fail)
Pass only when all checks are true:
- [ ] Content Preservation Gate satisfied: every baseline line is present
      in this document or in a named migration target.
- [ ] Required section order exists and is complete.
- [ ] Every C3 entry includes the minimum contract fields.
- [ ] C1 call flows include concrete methods/functions/fixtures.
- [ ] C1 map entries include path, range, LOC, and verified_at.
- [ ] Terminology aligns with `tests_architecture.md`.
- [ ] Information Sources support promoted FACT claims.
- [ ] No path in the document begins with the install directory, and every path
      into the documented suite is repo-relative rather than absolute.

Passing this gate means the document is structurally sound, not that it is good.
Every check above is binary: an entry reading "Runs the suite" satisfies the
contract fields and names no behaviour it protects. Score the document with
`agent_onboarding/default/design_engineer/policies/system_document_quality_rubric.md`
(tests_components profile - Depth is scored per entry and averaged) and record
the total in the active ticket. Below 60 it is not usable as evidence
downstream. Expect a lower score here than on the source side on a first pass;
that gap is the finding, not an excuse.

## Validation Commands
- `rg -n '^#{1,6} .*[([][^)\]]*$' context_compass/system_docs/tests_components.md` - headings with an unclosed bracket, the usual sign of a wrap
- `rg -n "^## " context_compass/system_docs/tests_components.md`
- `rg -n "C3 Components|C2 Subcomponents|Method-Level Call Flows|C1 Code Map" context_compass/system_docs/tests_components.md`
- `rg -n "path|start_line|end_line|loc|verified_at" context_compass/system_docs/tests_components.md`

Two that must return nothing. These are the portability rule, and unlike the
others a hit is a defect rather than a thing to eyeball:

- `rg -n "context_compass/|agent_onboarding/|tools/system_documents/|index_document\.py|system_docs/|patches/active/" context_compass/system_docs/tests_components.md` -
  any hit is a path into this package that a downstream reader cannot resolve.
  Note the alternation. Checking only for `context_compass/` finds nothing on a
  real leaked document, because an agent writing from inside the install writes
  `python tools/system_documents/index_document.py --doc system_docs/tests_components.md`
  with no prefix at all. That is the same file and the same defect.
- `rg -n "([A-Za-z]:\\\\|^\s*-?\s*path:\s*[\`']?/)" context_compass/system_docs/tests_components.md` -
  absolute paths, Windows or POSIX, which encode one machine's checkout location

## Staleness Triggers (When Update Is Mandatory)
- Test component ownership/wiring changed.
- Fixture or harness lifecycle changed.
- Method-level test flow changed.
- C1 ranges became stale from test-file edits.
- `tests_architecture.md` changed boundaries or terminology.
- `src_components.md` changed a component this document verifies. The source
  map moving without the test map moving is the most common way these two drift.
- `src_graph.md` changed because documented source wiring or ownership
  relationships changed.
- `src_graph_index.md` changed because canonical object relationships or
  ownership moved.
- Active component/code-description patch docs changed for the same patch id.

## Anti-Patterns (Reject)
- Test component entries without lifecycle/ownership detail.
- C1 call flows with generic statements and no concrete symbols.
- C1 map entries missing verification fields.
- Divergence from tests architecture terminology without escalation.
- **Naming Context Compass anywhere in the document.** A `context_compass/...`
  path, a tool invocation, a pointer at a skill file. The document ships with
  the codebase; the tooling does not ship with it. Reference the documented
  suite instead, and put maintenance commands in this skill.
- **Absolute paths in C1 entries, Key Files, or Information Sources.**
  Repo-relative only. An absolute path is correct on exactly one machine.

## Handoff Rule
- End with `Context / Handoff Summary` that states:
  - what component mapping is verified,
  - what remains unknown,
  - which test subsystem should be mapped next.

