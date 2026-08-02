

# src_components_instructions

## Purpose
- Define the exact build protocol for
  `context_compass/system_docs/src_components.md`.
- Produce a bottom-up component contract map (C3/C2/C1) that stays aligned to
  architecture boundaries.

## Canonical Output
- `context_compass/system_docs/src_components.md`

## Example Documents (Required Read)
- `context_compass/examples/example_components/src_components.md`
- `context_compass/examples/example_components/tests_components.md`
- `context_compass/examples/example_architecture/src_architecture.md`
- `context_compass/examples/example_architecture/tests_architecture.md`

The canonical output does not ship with the package. `system_docs/` is empty in
a fresh install, so on first run you are creating this document, not editing
one. The examples above are the shape reference; this repository is the source
of truth for the content.

## Required Inputs (Read First)
- `context_compass/system_docs/src_architecture.md`
- `context_compass/system_docs/src_graph.md`
- `context_compass/system_docs/src_graph_index.md`
- `context_compass/system_docs/tests_components.md`
- `context_compass/system_docs/tests_architecture.md`
- `context_compass/system_docs/patches/active/<patch_id>/component_patch_<component>.md`
  (when patch lane is active)
- `context_compass/system_docs/patches/active/<patch_id>/code_description_patch_<component>.md`
  (when complexity trigger applies)
- `context_compass/agent_onboarding/default/design_engineer/skills/src_architecture_instructions.md`
- `context_compass/agent_onboarding/default/design_engineer/skills/patch_framework_design.md`
- `context_compass/agent_onboarding/default/design_engineer/skills/component_patch_contracts.md`
- `context_compass/agent_onboarding/default/design_engineer/skills/code_description_patch_contracts.md`
- Active ticket and `context_compass/attention_board.md` route

## Indexing Contract (Non-Negotiable)

This document is AUTHORED. Nothing generates its prose. The only generated
artifact is its index, and the index is only as useful as the heading structure
you give it.

Regenerate the index in the SAME pass that edits the document:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/src_components.md
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
  production `src_components.md` that catalog
  indexes as a **1,945-line** section, so a reader selecting it loads 37% of the
  document believing they sliced it.

Consume the index by slicing, never by reading the document whole:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/src_components.md --slice "<section name>"
```

It verifies the index before returning anything, refuses on a stale index, and
lists candidates rather than guessing when a name is ambiguous. Section names
are therefore the query - keep them unique and descriptive.

Verify before trusting any range:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/src_components.md --check
```

An index records `line_count`, `content_sha256`, and `line_ending`. Insert one
line near the top and every range below it is wrong while still parsing and
still returning content - the WRONG content, confidently. On mismatch: STOP,
regenerate, do not eyeball an offset.

Full format specification:
`agent_onboarding/default/engineer/skills/system_document_build.md`

## Unknowns Gate (Non-Negotiable)
- Default to `UNKNOWN` for unevidenced component claims.
- Promote to `FACT` only with direct evidence.
- No behavior inference from naming or folder shape.

## Required Section Contract
`src_components.md` must contain these sections in order:
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

### Sections not in the contract

The contract is a **minimum in a fixed relative order**, not a whitelist. Other
sections are permitted and are common. Measured on one real architecture
document: 44 H2 sections against its 17-section contract - read literally as
"only these sections", a recomposition deletes roughly 1,200 lines. That figure
is from the architecture side; the ratio is what carries over. The contract
above lists twelve, and a mature components document will exceed it too.

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
set follows. It is also already the join `system_document_build.md` depends on,
so nothing new has to be tracked.

On a 574-module package that resolved to 170 paths - a scope an agent can
actually verify, against an inventory it cannot.

An exhaustive inventory is still useful. Keep it, do not let the rename delete
it: put it beneath as `### Full Package Inventory (exhaustive, retained)`.
Narrowing a section's scope is not a licence to destroy what was there.

## Component Entry Contract (C3 Minimum)
Each C3 component entry must include:
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

**`Key Files (C1)` cites in-scope SOURCE paths only.** The graph is built from
the source tree, so a test path can never resolve against it - it is not a near
miss, it is a guaranteed miss. Test surfaces belong in the test-side mirror.
Measured on a real recomposition: 165 of 167 cited paths resolved, and both
misses were test files sitting in a component's key files.

Verify the join rather than assuming it:

```bash
DOC=context_compass/system_docs/src_components.md
IDX=context_compass/system_docs/src_graph_index.md

# Pull paths from the two contract fields that hold them, not from every
# backtick in the document - code-fence tags are backticked too, and a check
# that reports `bash` as a missing file gets ignored by its second run.
{ grep -o 'Key Files (C1):.*' "$DOC"; grep -o '^- path: .*' "$DOC"; } \
  | grep -o '`[^`]*`' | tr -d '`' | grep -v '[*?]' | sort -u > /tmp/cited.txt

# The index keys rows by source path in the second cell.
grep -o '^| [0-9]*-[0-9]* | `[^`]*`' "$IDX" \
  | sed 's/.*`\(.*\)`/\1/' | sort -u > /tmp/graph.txt

comm -23 /tmp/cited.txt /tmp/graph.txt   # anything here does not resolve
```

Two details that matter more than they look. Match `` `[^`]*` `` **including both
backticks** - a lookahead form like `` `\K[^`]+(?=`) `` resumes scanning at the
closing backtick, treats it as an opening one, and reports the `, ` between two
cited paths as a path. And `grep -v '[*?]'` drops globs: a glob is a deliberate
statement about a set, not a citation that can resolve to one file. No source
root is hardcoded anywhere here, because `src/`, `lib/`, `app/` and a flat root
are all normal and the index already knows which one this repository uses.

## C1 Flow/Map Contract
- Method-level call flows must include concrete method/function names.
- C1 map entries must include:
  - `path`
  - `start_line`
  - `end_line`
  - `loc`
  - `verified_at` (UTC DateTime `YYYY-MM-DDTHH:MM:SSZ`)

**Directories are not valid C1 entries.** A directory has no line range, and the
join to `src_graph.md` is keyed by source file, so a directory citation can never
resolve. Expand it into its constituent source files - excluding whatever the
graph's scope already excludes - and measure each.
Do not write `UNKNOWN` for a directory: `UNKNOWN` means "not yet verified and
here is the investigation target", and a directory is unverifiable in principle -
the marker would sit there forever with nothing to resolve it.

Ranges are measured, never estimated. If the exact range is not verified, keep
the claim `UNKNOWN` and add an investigation target in `## Unknowns` rather than
writing a plausible number.

## Build Sequence (Bottom-Up, Required)
1. Confirm active ticket route and component scope.
2. If the document already exists, capture the Content Preservation baseline
   now, before the first edit. Captured later it proves nothing.
3. Read required example documents and note reusable structure patterns.
4. Re-read architecture boundaries and terms.
5. Unwrap any heading spanning more than one physical line. A reflowed heading
   parses as several sections; the first wins "narrowest match" and `--slice`
   returns a stub. `index_document.py` warns on unclosed brackets, which is the
   usual tell, but it cannot catch every wrap - scan the heading list once
   before you trust it.
6. Draft/refresh `Metadata`, `Scope`, `Unknowns Gate`, and `Unknowns`.
7. Build C3 component catalog using the entry contract.
8. Build C2 subcomponent catalog with ownership and wiring.
9. Capture method-level C1 call flows for core paths.
10. Build C1 map entries with ranges, LOC, and verification timestamps.
11. Add/refresh diagrams aligned to catalog terminology.
12. If patch lane is active, verify component/code-description patch updates
    are complete and linked in tickets.
13. Refresh `Information Sources` and `Context / Handoff Summary`.
14. Rebuild the index in this same pass, then satisfy the Content Preservation
    Gate and the Quality Gate.

If a component claim conflicts with architecture, log `CONFLICT` in ticket
notes and escalate before proceeding.

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
- [ ] C1 call flows use concrete method/function names.
- [ ] C1 map entries include path, range, LOC, and verified_at.
- [ ] Architecture terminology and boundaries are consistent.
- [ ] Information Sources support all promoted FACT claims.

Passing this gate means the document is structurally sound, not that it is good.
Every check above is binary: "Every C3 entry includes the minimum contract
fields" passes on twelve fields that each restate their own name. Score the
document with
`agent_onboarding/default/design_engineer/policies/system_document_quality_rubric.md`
(src_components profile - Depth is scored per entry and averaged, so hollow
entries cannot hide behind good ones) and record the total in the active ticket.
Below 60 it is not usable as evidence downstream.

## Validation Commands
- `rg -n '^#{1,6} .*[([][^)\]]*$' context_compass/system_docs/src_components.md` - headings with an unclosed bracket, the usual sign of a wrap
- `rg -n "^## " context_compass/system_docs/src_components.md`
- `rg -n "C3 Components Catalog|C2 Subcomponents Catalog|Method-Level Call Flows|C1 Code Map" context_compass/system_docs/src_components.md`
- `rg -n "path|start_line|end_line|loc|verified_at" context_compass/system_docs/src_components.md`

## Staleness Triggers (When Update Is Mandatory)
- Component ownership/wiring changed.
- Lifecycle/cleanup ordering changed.
- Core method-level flows changed.
- Architecture boundaries/terms changed.
- `src_graph.md` changed because documented source wiring or
  ownership relationships changed.
- `src_graph_index.md` changed because canonical object relationships or ownership
  moved.
- C1 ranges became stale from code edits.
- Active component/code-description patch docs changed for the same patch id.

## Anti-Patterns (Reject)
- Component summaries without ownership/lifecycle details.
- C1 call flows without concrete methods.
- C1 map entries missing verification fields.
- Architecture mismatch left undocumented.

## Handoff Rule
- End with a concise `Context / Handoff Summary` that states:
  - what component contracts changed,
  - what is still unknown,
  - which subsystem should be verified next.
