

# tests_architecture_instructions

## Purpose
- Define the exact build protocol for
  `context_compass/system_docs/tests_architecture.md`.
- Turn test-architecture docs from placeholder state into evidence-led C4
  system context.

## Canonical Output
- `context_compass/system_docs/tests_architecture.md`

## Example Documents (Required Read)
- `context_compass/examples/example_architecture/tests_architecture.md`
- `context_compass/examples/example_architecture/src_architecture.md`
- `context_compass/examples/example_components/tests_components.md`
- `context_compass/examples/example_components/src_components.md`

Read the two architecture examples as a pair. They share a section contract on
purpose: one maps the runtime, the other maps how the runtime is verified. If
your output makes the test map structurally different from the source map, the
divergence is the defect.

The canonical output does not ship with the package. `system_docs/` is empty in
a fresh install, so on first run you are creating this document, not editing
one. The examples above are the shape reference; this repository is the source
of truth for the content.

## Required Inputs (Read First)
- `context_compass/system_docs/tests_components.md`
- `context_compass/system_docs/src_architecture.md`
- `context_compass/system_docs/src_components.md`
- `context_compass/system_docs/src_graph.md`
- `context_compass/agent_onboarding/default/design_engineer/skills/tests_components_instructions.md`
- Active ticket and `context_compass/attention_board.md` route

## Indexing Contract (Non-Negotiable)

This document is AUTHORED. Nothing generates its prose. The only generated
artifact is its index, and the index is only as useful as the heading structure
you give it.

Regenerate the index in the SAME pass that edits the document:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/tests_architecture.md
```

Heading discipline the index depends on:
- **Exactly one H1.** A second one and the indexer cannot identify the document
  title, so it stops omitting it and emits a section spanning the whole file.
- **The navigable unit is H2 `## <Concern>`.** Consistent depth, never mixed.
- **Names unique and stable.** Index rows are selected on name; two sections
  sharing a name are indistinguishable to a consumer.
- **No container headings in this document.** Every H2 is a selectable concern,
  so there is no wrapper heading to select by mistake. Keep it that way: the
  moment an H2 exists only to group other headings, it indexes as a range
  covering all of them, and a reader selecting it loads that whole span
  believing they sliced one section. On a production `src_components.md` that
  mistake costs 37% of the document in a single slice.

Consume the index by slicing, never by reading the document whole:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/tests_architecture.md --slice "<section name>"
```

It verifies the index before returning anything, refuses on a stale index, and
lists candidates rather than guessing when a name is ambiguous. Section names
are therefore the query - keep them unique and descriptive.

Verify before trusting any range:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/tests_architecture.md --check
```

An index records `line_count`, `content_sha256`, and `line_ending`. Insert one
line near the top and every range below it is wrong while still parsing and
still returning content - the WRONG content, confidently. On mismatch: STOP,
regenerate, do not eyeball an offset.

Full format specification:
`agent_onboarding/default/engineer/skills/system_document_build.md`

## Unknowns Gate (Non-Negotiable)
- Start unknown-heavy and explicit.
- Promote to `FACT` only when direct evidence is captured.
- If evidence is incomplete, keep `UNKNOWN` and list investigation targets.

## Required Section Contract
`tests_architecture.md` must contain these sections in order:
1. `## Metadata`
2. `## Scope and Intent`
3. `## Indexing`
4. `## DO NOT ASSUME / Unknowns Gate`
5. `## Unknowns`
6. `## System Context (C4)`
7. `## System Boundary and External Interfaces`
8. `## Architecture Summary (C4)`
9. `## Entrypoints and Runtime Guardrails`
10. `## Boot and Configuration Sequence`
11. `## Data Flows and Sequences`
12. `## Operational Invariants`
13. `## Failure Modes and Error Paths`
14. `## C1 Code Map (Core Only)`
15. `## Diagrams`
16. `## Information Sources`
17. `## Context / Handoff Summary`

### The document names no path into this package

`tests_architecture.md` is committed to the repository it describes and, in a
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

Not in `## Indexing`, not in `## Information Sources`, not in a cross-reference.
This is a hard rule, and it is checked in the Quality Gate.

- **Maintenance commands are relocated, not deleted.** The command that rebuilds
  the index lives in this skill, which is where a maintainer already is when
  they need it. The document's `## Indexing` section states that an index
  companion exists and what heading rules it depends on. A reader needs both
  facts and neither one requires naming a tool.
- **Cross-references use a logical document id**: `tests_components`, not
  `context_compass/system_docs/tests_components.md`. The id survives the
  document being vendored, renamed, or published under a different root. The
  path does not.
- **Paths into the subject stay, and stay repo-relative.** `tests/unit/test_x.py`
  in a C1 entry is exactly right - that is the suite being documented and it is
  the whole point of the entry. Relative to the repository root, never absolute:
  `C:\Users\...\tests\unit\test_x.py` encodes one machine's checkout location
  into a document that gets committed and shipped, so it is wrong for every
  reader who is not you, and it breaks the moment the repo is cloned anywhere
  else. The rule bans paths into the tooling that produced the document, never
  paths into the thing it describes.

`src_graph.md` is the model to copy: it is fully generated and contains zero
install-prefixed paths.

**This is `src_architecture.md`'s contract, name for name.** That is required,
not incidental: `system_document_build.md` states the pair share one section
contract and that divergence between them *is* the defect. Identical names are
what let a reader who knows one document navigate the other, and what makes the
two indexes sliceable by the same query.

The section names stay the same; their **subject** does not. `## Boot and
Configuration Sequence` here means how the test harness boots and configures,
not how the runtime does. If a section of this document would read identically
in `src_architecture.md`, it is describing the wrong system - the shared
contract is a navigation guarantee, not licence to restate the source map in
test vocabulary.

### Sections not in the contract

The contract is a **minimum in a fixed relative order**, not a whitelist. Other
sections are permitted and are common. Measured on one real architecture
document: 44 H2 sections against its 17-section contract - read literally as
"only these sections", a recomposition deletes roughly 1,200 lines. That figure
is from the source side of the pair, which shares this exact contract, so it
transfers directly: a mature test architecture will exceed seventeen too.

If material genuinely does not belong here, it is **moved, never deleted**:

- relocate it to a named target - the patch lane
  (`system_docs/patches/active/<patch_id>/`) is the conventional destination
- name that target in `## Context / Handoff Summary`
- state plainly that until it is re-absorbed it lives in neither canonical
  document

"Delete it because the contract does not list it" is never the right answer.

## C1 Code Map Contract
Each C1 core-map entry must include:
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

**There is no join to verify on this side, and that is the asymmetry.** The graph
is built from the source tree, so the source-side documents get their citations
checked against `src_graph_index.md` for free. This document cites test paths,
which appear in no graph. Nothing will tell you a path here has gone stale.
Remeasure ranges on every pass rather than assuming a tool is watching.

Ranges are measured, never estimated. If the exact range is not verified, keep
the claim `UNKNOWN` and add an investigation target in `## Unknowns` rather than
writing a plausible number.

## Diagram Contract
- Include one ASCII flow diagram.
- Include one Mermaid flow diagram.
- Keep labels operational (surface, flow, boundary), not decorative.
- Keep diagram terms aligned with section terminology.
- Diagram the verification path, not the runtime path. If this diagram could be
  dropped into `src_architecture.md` unchanged, it is describing the wrong
  system.

## Build Sequence (Discovery-First, Required)
1. Confirm active ticket route and test-system scope.
2. If the document already exists, capture the Content Preservation baseline
   now, before the first edit. Captured later it proves nothing.
3. Read required example documents and extract reusable C4 section patterns.
4. Inventory test entry surfaces (test tree, runner config, fixtures).
5. Unwrap any heading spanning more than one physical line. A reflowed heading
   parses as several sections; the first wins "narrowest match" and `--slice`
   returns a stub. `index_document.py` warns on unclosed brackets, which is the
   usual tell, but it cannot catch every wrap - scan the heading list once
   before you trust it.
6. Capture unknowns before promoting any architecture claims.
7. Define C4 boundaries and external interfaces.
8. Document lifecycle flow (setup, execution, teardown) with evidence.
9. Capture invariants and failure paths observed in sources.
10. Build the C1 core map with ranges, LOC, and verification timestamps.
11. Add ASCII + Mermaid diagrams per the Diagram Contract.
12. If patch lane is active, confirm the architecture patch has not moved a
    boundary this document still describes the old way.
13. Refresh `Information Sources` and `Context / Handoff Summary`.
14. Rebuild the index in this same pass, then satisfy the Content Preservation
    Gate and the Quality Gate.

Do not skip sequence order. If blocked, write a `BLOCKER` note in the active
ticket before expanding scope. If a test-architecture claim conflicts with
`src_architecture.md`, log `CONFLICT` in ticket notes and escalate before
proceeding - the mismatch is the finding, and resolving it silently in either
direction destroys it.

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
- [ ] Unknowns are explicit and tied to investigation targets.
- [ ] Interfaces, lifecycle, and invariants are evidence-backed.
- [ ] C1 map entries include path, range, LOC, and verified_at.
- [ ] Diagrams and narrative use consistent terms.
- [ ] No path in the document begins with the install directory, and every path
      into the documented suite is repo-relative rather than absolute.

Passing this gate means the document is structurally sound, not that it is good.
Every check above is binary, and none of them notice a document that restates
source architecture in test vocabulary while satisfying every section. Score it
with
`agent_onboarding/default/design_engineer/policies/system_document_quality_rubric.md`
(tests_architecture profile - describing the wrong system scores 0 on Fidelity
however accurate the sentences are) and record the total in the active ticket.
Below 60 it is not usable as evidence downstream. Expect a lower score here than
on the source side on a first pass; that gap is the finding, not an excuse.

## Validation Commands
- `rg -n '^#{1,6} .*[([][^)\]]*$' context_compass/system_docs/tests_architecture.md` - headings with an unclosed bracket, the usual sign of a wrap
- `rg -n "^## " context_compass/system_docs/tests_architecture.md`
- `rg -n "UNKNOWN|System Context|Data Flows|C1 Code Map|Information Sources" context_compass/system_docs/tests_architecture.md`
- `rg -n "path|start_line|end_line|loc|verified_at" context_compass/system_docs/tests_architecture.md`

Two that must return nothing. These are the portability rule, and unlike the
others a hit is a defect rather than a thing to eyeball:

- `rg -n "context_compass/|agent_onboarding/|tools/system_documents/|index_document\.py|system_docs/|patches/active/" context_compass/system_docs/tests_architecture.md` -
  any hit is a path into this package that a downstream reader cannot resolve.
  Note the alternation. Checking only for `context_compass/` finds nothing on a
  real leaked document, because an agent writing from inside the install writes
  `python tools/system_documents/index_document.py --doc system_docs/tests_architecture.md`
  with no prefix at all. That is the same file and the same defect.
- `rg -n "([A-Za-z]:\\\\|^\s*-?\s*path:\s*[\`']?/)" context_compass/system_docs/tests_architecture.md` -
  absolute paths, Windows or POSIX, which encode one machine's checkout location

## Staleness Triggers (When Update Is Mandatory)
- Test runner/configuration behavior changed.
- Fixture lifecycle behavior changed.
- Test boundary/interfaces changed.
- C1 ranges became stale from test-file edits.
- `tests_components.md` introduces term/boundary changes.
- `src_architecture.md` changed a boundary this document verifies. The source
  map moving without the test map moving is the most common way these two drift.
- `src_graph.md` changed because documented source wiring or ownership
  relationships changed.
- `src_graph_index.md` changed because canonical object relationships or
  ownership moved.
- Active `architecture_patch.md` changed for the same patch id.

## Anti-Patterns (Reject)
- Generic "tests do X" statements without evidence.
- Missing unknown inventory in partially mapped docs.
- C1 map entries without verification fields.
- Copying src architecture claims into tests architecture without proof.
- **Naming Context Compass anywhere in the document.** A `context_compass/...`
  path, a tool invocation, a pointer at a skill file. The document ships with
  the codebase; the tooling does not ship with it. Reference the documented
  suite instead, and put maintenance commands in this skill.
- **Absolute paths in C1 entries or Information Sources.** Repo-relative only.
  An absolute path is correct on exactly one machine.

## Handoff Rule
- End with `Context / Handoff Summary` covering:
  - evidence-backed state,
  - unresolved unknowns,
  - next discovery target.

