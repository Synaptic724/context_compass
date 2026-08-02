
# system_document_build

Purpose
- Define the authoring format for `src_components.md` and `src_architecture.md`.
- Define how their indexes are built and kept current.

## These documents are AUTHORED, not generated

There is no build step and no codegen. `src_components.md` is the file you edit
directly. Nothing assembles it from pieces, and no script writes its prose.

That is not a convenience choice, it is a limit. A component's responsibilities,
its ownership boundaries, and why it exists cannot be derived from source. The
same wall that makes `owns_lifecycle_of` and `borrows` indistinguishable to a
parser makes "this component admits transactions into scope" underivable. If a
tool could write it, it would not be worth reading.

The only generated artifact is the **index**: a table of line ranges that lets a
reader slice the document instead of loading all of it.

| document | authored | generated |
|---|---|---|
| `src_components.md` | the document | `src_components_index.md` |
| `src_architecture.md` | the document | `src_architecture_index.md` |
| `src_graph.md` | nothing | the whole thing - see `src_graph_generation.md` |

## Why format matters

The index is only as useful as the document's heading structure, because
headings are the only thing it can cut on. This is about **addressability**, not
size: a section that cannot be named cannot be requested, however short it is.

**Every navigable unit needs its own heading at a predictable level.** If four
components share one heading, the index cannot offer them separately and a
reader wanting one must read all four.

**Names are the query.** `--slice` matches on the section name, so a section
called `Overview` in a document holding six overviews is unaddressable even
though it is indexed. Name sections after the thing they describe.

**Avoid container headings that hold nothing but other headings.** Indexing a
production `src_components.md` produces a `C3 Components Catalog` section of
**1,945 lines**: it wraps 24 components, so
its range spans all of them. An entry like that defeats the index while
appearing to use it, because a reader who selects it loads 37% of the document
believing they sliced it. Containers are fine as organisation; just never select
one when a child would do.

The same trap one level up is the document title, which is why the indexer omits
a lone `#` heading entirely.

## Heading shape: `src_components.md` and `tests_components.md`

**This skill does not declare which sections a document contains, or which
fields a component entry carries.** Those are the Required Section Contract and
the Component Entry Contract, and they live in the four `*_instructions.md`
skills. This skill covers only the heading structure the indexer depends on -
restating the section list here would create a second authority, and two lists
drift the moment one is edited.

```markdown
# <document title>                   <- exactly one H1

## <front matter sections>           <- H2, per the Required Section Contract

## C3 Components Catalog             <- H2: container. Never the read target.

### Component: <Name>                <- H3: THE navigable unit. One per component.
- <fields, per the Component Entry Contract>

## C2 Subcomponents Catalog

### Subcomponent: <Name>             <- H3, same shape
```

Rules that the index depends on:

- **Exactly one H1.** More than one and the indexer cannot identify the title,
  so it stops omitting it and you get a section spanning the whole file.
- **Every component is an H3**, never H2 and never H4. Mixed depth means mixed
  granularity in the index.
- **`Component: ` / `Subcomponent: ` prefixes are load-bearing.** They are how a
  reader greps the index for units rather than front matter.
- **Names are unique and stable.** The index is selected on name; two components
  with the same name are indistinguishable to a consumer.
- **`Key Files (C1)` lists real `src/...` paths.** This is the join to
  `src_graph.md`, and it measured 98% resolvable on the reference project. Break
  it and component-to-graph navigation stops working.

## Heading shape: `src_architecture.md` and `tests_architecture.md`

Same rules, one difference: the navigable unit is an **H2 concern**, not an H3
component, because architecture sections cut across components rather than
describing one each. These documents have no container heading at all - every H2
is selectable.

```markdown
# <document title>                   <- exactly one H1

## <Concern>                          <- H2: the navigable unit
### <Sub-topic>                       <- H3: optional, indexed too
```

The source-side and test-side documents at each level are mirrors: same section
contract, same heading shape, same index shape. If a test document's structure
diverges from its source counterpart, the divergence is the defect.

Every system document gets an index. There is no size below which one is
skipped: the index is not a size optimisation, it is how a document becomes
addressable. A small document with an index can be sliced by name; a small
document without one can only be read whole.

Section lists and entry fields:
- `agent_onboarding/default/design_engineer/skills/src_components_instructions.md`
- `agent_onboarding/default/design_engineer/skills/tests_components_instructions.md`
- `agent_onboarding/default/design_engineer/skills/src_architecture_instructions.md`
- `agent_onboarding/default/design_engineer/skills/tests_architecture_instructions.md`

## Patch documents: explicit ENTRY markers

Patch documents under `system_docs/patches/` do not section cleanly by heading.
Each entry is a distinct revision of a named thing, and heading depth carries no
meaning there - two revisions of the same component are peers regardless of how
deep their headings happen to sit.

So patches declare their boundaries instead of implying them:

```markdown
<!-- BEGIN ENTRY: "PipelineScope: stage admission" -->
## Revision 1

Introduces `PipelineScope` as the single admission point for stage
registration. Callers stop constructing `Stage` directly.

- affects: `src/example/pipeline/`
- risk: high, changes an admission gate
<!-- END ENTRY: "PipelineScope: stage admission" -->
```

**The name in the marker is the point.** It moves verbatim into the index, so a
row identifies the object it covers:

```
| lines | lvl | name |
| 6-14  | 1   | PipelineScope: stage admission |
| 16-23 | 1   | StoreHandle: contract delegation |
```

A row keyed by a number tells a reader nothing about whether to read it. Every
index this system produces is keyed by a name - breadcrumb path for authored
documents, source path for the graph, entry name for patches. There are no
anonymous rows anywhere, and there must not be.

Rules:

- `BEGIN ENTRY` and `END ENTRY` are HTML comments, so they do not render.
- Quotes around the name are optional; the name is trimmed either way.
- `END ENTRY` may repeat the name or omit it. If it repeats it, it must match.
- Entries do not nest. Opening one while another is open is an error.
- **Malformed markers refuse to index.** Unbalanced or mismatched markers are
  reported and nothing is written. A silently repaired boundary produces a range
  that looks correct and covers the wrong text.

Markers work in any document. `--mode auto` (the default) uses them when
present and falls back to headings when not, so a document that adopts markers
gets entry-based sectioning with no flag change.

## Building the index

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/src_components.md

python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/src_architecture.md

python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/patches/active/<patch_id>/architecture_patch.md
```

`--max-level` sets the deepest heading indexed (default 3). `--mode` forces
`heading` or `entry` sectioning. `--check` verifies the existing index is
current and writes nothing - run it before trusting any range.

The tool **never modifies the document**. It reads, validates, and writes
`<stem>_index.md` beside it.

It refuses two targets outright, because it writes and a wrong target does not
produce a confusing message you shrug off - it produces a plausible file that
replaces a correct one:

- **an `*_index.md` file.** Indexing an index yields `<stem>_index_index.md`,
  which addresses nothing.
- **an assembled graph** (any document containing `<!-- BEGIN FILE:`). Its index
  is a byproduct of assembly and cannot disagree with it. Re-indexing here would
  re-parse headings and overwrite that with a weaker index keyed by heading
  breadcrumb rather than source path. Run `assemble_graph.py`.

Both refusals came from doing it: a convenience glob over `examples/example_*/*.md`
swept in the generated graph and every existing index, overwrote the graph's
byproduct index, and left ten junk files behind. The counts caught it, not the
output - which is the argument for the refusal being in the tool rather than in a
sentence someone is supposed to remember.

Every range is validated against its own heading before anything is written. An
off-by-one silently corrupts every downstream read, so it is checked rather than
trusted, and a failed validation writes nothing.

## Slicing: how the index is consumed

An index exists to be sliced. The workflow is three steps, and step two is not
optional:

1. Find the section by NAME in the index.
2. Verify the index is current.
3. Read only those lines.

The tool does all three:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/system_docs/src_components.md \
    --slice "Router and Role Resolution"
```

It verifies `line_count` and `content_sha256` against the index ON DISK before
returning anything, and prints the range as a header so the output carries its
own citation:

```
<!-- src_components.md:74-94  C3 Components Catalog > Component: Router and Role Resolution Engine -->
### Component: Router and Role Resolution Engine
- Purpose: resolve the selected role chain deterministically.
...
```

That is real output from the document shipped in this package - run the command
and you get it back.

Behaviour that matters:

- **A stale index refuses to slice.** Edit the document without regenerating and
  you get `INDEX STALE - refusing to slice`, not wrong content.
- **An ambiguous name lists the candidates rather than guessing.** Asking for
  `Catalog` against the shipped `src_components.md` matches 7 sections; it prints them
  with their ranges so you can narrow.
- **A missing index refuses too.** Generate before you slice.

This is why section names must be unique and descriptive. `--slice` matches on
the name, so the name is the query - a section called `Overview` in a document
with six overviews is unaddressable.

## Regenerate whenever the document changes

The index records `line_count`, `content_sha256`, and `line_ending`. Insert one
line near the top and every range below it is wrong - while the index still
parses, still looks plausible, and still returns content. It returns the WRONG
content, confidently.

So: edit the document, regenerate the index, in the same pass. A consumer that
finds a mismatch must refuse to slice; see
`agent_onboarding/default/engineer/skills/src_graph_usage.md` for the
verification procedure, which is identical.

## The document has to survive leaving this repository

`src_architecture.md`, `src_components.md`, `tests_architecture.md`,
`tests_components.md` and `src_graph.md` describe a codebase. They get committed
to that codebase, reviewed with it, and in a packaged project they ship inside
the wheel - some projects publish one as a module attribute so a consumer can
read the architecture without leaving the interpreter.

None of those readers have Context Compass. It is a helper repository that
produced the document; it is not a dependency of the document. So a line like

```
python context_compass/tools/system_documents/index_document.py --doc ...
```

is correct for you, at this moment, in this checkout, and is dead text for every
other reader the document will ever have.

**The rule: a produced system document contains no path that points into this
package.** No tool invocation, no pointer at a skill file, no cross-reference by
path.

State it by destination, not by spelling. The install prefix is often absent,
because an agent authoring from inside the install writes what it sees:

```
python tools/system_documents/index_document.py --doc system_docs/src_architecture.md
Spec: `agent_onboarding/default/engineer/skills/system_document_build.md`
```

Not one of those lines contains the string `context_compass`, and every one of
them is a path into this package. A check that looks only for the prefix passes
a thoroughly leaked document. The markers that matter are `context_compass/`,
`agent_onboarding/`, `tools/system_documents/`, `system_docs/`,
`patches/active/`, and any tool filename such as `index_document.py`.

What replaces each kind of reference:

| you want to write | write instead |
| --- | --- |
| `python tools/system_documents/index_document.py ...` | nothing - the command lives in the role skill, where a maintainer already is |
| `system_docs/src_components.md`, prefixed or not | `src_components` - the logical document id |
| `` Spec: `agent_onboarding/.../<skill>.md` `` | nothing - the document does not cite its own tooling |
| `patches/active/<patch_id>/...` | the patch id alone, if the reader needs it at all |
| the file being documented | `src/<pkg>/engine.py` - keep it, repo-relative |

Two things this rule does **not** ban, and both matter:

- **Paths into the documented source.** A C1 entry naming `src/<pkg>/engine.py`
  or `tests/unit/test_engine.py` is the entire value of the entry. Reference the
  source, always.
- **Naming a sibling system document.** A reader benefits from knowing
  `src_components` goes deeper than `src_architecture` on the same subject.
  Use the id, not the path - the id survives the pair being vendored into
  another repository, published under a different root, or renamed.

Absolute paths are banned for the same reason and are worse:
`C:\Users\...\src\<pkg>\engine.py` is correct on exactly one machine and wrong
the moment the repository is cloned. Repo-relative, always.

`src_graph.md` is the model. It is fully generated, it cites the source tree
constantly, and it contains zero install-prefixed paths - so the generator
already gets this right and is the thing to copy.

## Anti-patterns

- Generating any part of these documents. They are authored.
- Hand-editing an index. Regenerate it.
- Editing the document and leaving the index stale.
- Selecting a container section (`C3 Components Catalog`) when a component
  section would answer the question.
- Adding a second H1, or nesting components at inconsistent depths.
- Renaming a component without checking who cited it.
- Omitting `Key Files (C1):`, which silently severs the join to `src_graph.md`.
- Restating a section list or entry contract here. This skill owns heading shape
  and index mechanics; the `*_instructions.md` skills own what goes in them.
- **Writing a path into this package into a produced document.** The commonest
  form is a helpful `## Indexing` section that pastes in the regeneration
  command. It reads as documentation and is an anti-pattern: it welds a document
  that ships to a tool that does not.
- **Assuming the leak says `context_compass`.** It usually does not. An agent
  authoring from inside the install writes `tools/system_documents/...` and
  `system_docs/...`, no prefix, and a prefix-only check calls that clean.
- **Citing a skill file from a produced document.** The document is the output;
  the skill is the process. A reader holding the wheel has one and never the
  other.
- **Absolute paths anywhere in a produced document.** Repo-relative only.

References
- `system_docs/system_docs_read_first.md` (what a fresh install is allowed to be
  missing, and which example docs set the bar before you author anything)
- `agent_onboarding/default/engineer/skills/src_graph_usage.md`
- `agent_onboarding/default/engineer/skills/src_graph_generation.md`
- `agent_onboarding/default/design_engineer/skills/src_components_instructions.md`
- `agent_onboarding/default/design_engineer/skills/src_architecture_instructions.md`
