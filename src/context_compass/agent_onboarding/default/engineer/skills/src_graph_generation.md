
# src_graph_generation

Purpose
- Define how to BUILD and MAINTAIN the assembled source graph.

## The pipeline

Two stages, two scripts, both stdlib-only:

```
tools/system_documents/python/extract_graph.py     source tree -> per-file descriptors
tools/system_documents/python/assemble_graph.py    descriptors -> src_graph.md + index
```

```bash
python context_compass/tools/system_documents/python/extract_graph.py \
    --src src --out context_compass/system_docs/graph

python context_compass/tools/system_documents/python/assemble_graph.py \
    --descriptors context_compass/system_docs/graph \
    --out context_compass/system_docs
```

`--check` on either script reports without writing. Run it before assuming the
graph is current.

The layout is `tools/system_documents/<language>/`. The descriptor contract is
language-neutral; only the extractor is Python-specific. A sibling directory can
implement the same contract for another language.

## Why per-file descriptors

The unit is the source file, because that is the unit that changes.

Earlier drafts sharded a single generated blob by namespace and bin-packed it to
a line budget. That produced unstable boundaries - adding one node reflowed the
packer and silently moved unrelated nodes between shards - and meaningless
names. Anchoring to the source path fixes both: a file is a file, its descriptor
mirrors its path, and touching one file dirties exactly one descriptor.

It also makes the size problem disappear. Source files are already
human-sized, so descriptors are too: median 43 lines, p90 83, none over 400,
with no budget parameter anywhere.

## The three tiers, and who owns them

This is the contract that makes regeneration safe.

| tier | owner | fields |
|---|---|---|
| mechanical | the script | `id`, `label`, `kind`, `file`, `lineno`, `bases`, `markers`, `public_methods`, `shape`, `source_sha256`, `specializes`/`implements` edges |
| curation | authored | `include` |
| semantics | authored | `role`, `responsibilities`, `owns_state`, `phases`, `edges_authored` |

**On re-run the script refreshes tier 1 and never touches tiers 2 and 3.** That
is verified behaviour, not an intention - inject an authored field, re-run, and
it survives.

## The authored schema

These are the fields you may populate. Nothing generates them and nothing
validates them, so this list is the contract.

### Node fields

| field | shape | meaning |
|---|---|---|
| `include` | bool | belongs in the composed graph. Absent means "not triaged", which is not the same as `false`. |
| `role` | prose, one line | what this object is for. |
| `responsibilities` | list of short phrases | what it is on the hook for. |
| `owns_state` | list of attribute names | fields whose lifecycle it controls. |
| `phases` | list | when in its life it matters: `init`, `validation`, `runtime`, `refresh`, `cleanup`. Open set - add one if your system needs it, but reuse these first. |

### Edge fields, under `edges_authored`

| field | shape | rendered |
|---|---|---|
| `from` | node id | yes, table |
| `to` | node id | yes, table |
| `relation` | `owns_lifecycle_of`, `uses`, `borrows`, `holds`, `owns`, `used_by` | yes, table |
| `cardinality` | `one_to_one`, `one_to_many`, `many_to_one` | yes, table |
| `phase` | list, same vocabulary as node `phases` | yes, table |
| `why` | prose, one or two sentences | yes, beneath the table |
| `strength` | `hard`, `borrowed`, `soft` | **no - see below** |

**`strength` is stored and deliberately not rendered.** Measured against a
hand-authored graph of 997 edges it is ~97% recoverable from `relation`:
`hard` is the ownership relations, `borrowed` is the reference relations. A
column that restates the column beside it costs space and adds nothing. Keep
populating it if your tooling consumes it; the document will not show it.

**`why` is rendered because it is the justification for a claim the extractor
says it cannot make.** An authored `owns_lifecycle_of` asserts ownership where
the syntax tree shows only a reference. Recording why, and showing it, is the
difference between evidence and assertion. It sits beneath the table so the
table stays scannable.

The prose does not cost you a whole-document read, because there is no such
thing here: you read the index and slice one section. A few extra lines inside
the one section you asked for is not a cost worth optimising against.

## What the script cannot do, and why

Do not expect the extractor to produce a finished graph. Measured against a
hand-authored graph of 535 nodes and 997 edges:

- node identity: **94%** recovered (matching on file + label)
- `specializes` edges: **94%** recovered with fully-qualified ids on both ends
- edge target resolution via imports: **99%**
- **68% of all edges are not derivable at all**

`owns_lifecycle_of` (205 edges), `uses` (323), and `borrows` (119) are
syntactically identical. Every one is "A holds a reference to B". Whether A owns
B's lifecycle, merely uses it, or borrows it without owning is a design fact
that does not appear anywhere in the source text. The same is true of every
`role`, `why`, `cardinality`, and `strength`.

Curation is equally underivable. The best syntactic significance rule tested
would have suppressed 419 nodes while wrongly dropping 63 that the reference
graph deliberately includes. So the script emits inventory and records `shape`
signals; the `include` field is authored. Emitting a node the author can reject
is recoverable. Silently withholding one they wanted is not.

## Maintenance loop

When you change a source file:

1. Re-run `extract_graph.py`. Only that file's descriptor changes.
2. Read the drift report. It names nodes that are `NEW`, `ORPHANED` (gone from
   source but still carrying authored semantics), or `UNSEMANTIC`.
3. Author the semantics for anything new. Resolve orphans by hand - the script
   will not delete authored prose on your behalf.
4. Re-run `assemble_graph.py` to rebuild the document and index together.

Never regenerate one without the other. They are only guaranteed consistent
because a single pass emits both.

## The index is a byproduct

`assemble_graph.py` knows each section's line range because it emitted those
lines. It does not re-parse the document to find headings.

That removes a whole class of drift. An index generated by re-walking a
document can disagree with the document, and the only defence is a hash. Here
they cannot disagree. The hash is still recorded, but it guards a different
failure: someone hand-editing the assembled file.

Every range is verified against its own header on every run. An off-by-one here
silently corrupts every downstream read, so it is checked rather than trusted.

## What this replaced

The two generated JSON graph files - a readable graph of 776 KB and a raw graph
of 768 KB - are retired. Together they were 1,544 KB that had to be read whole
or not at all, because a JSON object has no addressable interior.

The replacement is 972 KB of Markdown plus a 62 KB index, and a typical query
reads a 20-40 line slice.

**If you arrive holding a graph in the retired format, do not run the two-command
sequence and hope.** Only `specializes` and `implements` are mechanical, so a
naive re-extraction marks every node `UNSEMANTIC` and drops every authored edge.
Measured on a mature graph that was 84% of its edges. The rule generalises: the
better your existing graph, the more the naive path destroys, because a mature
graph is edge-richer than a young one. Carry the authored tier across by node id
first, then by `(file, label)`, before you assemble anything.

## Anti-patterns

- Hand-editing `src_graph.md` or `src_graph_index.md`. Edit descriptors, reassemble.
- Regenerating the document without the index, or the reverse.
- Deleting a descriptor whose node still carries authored semantics.
- Filtering descriptor files by filename prefix. An earlier version of the
  assembler skipped anything starting with `_` to avoid manifests, and silently
  swallowed 14 real files including `__init__.py` and every dunder module. A
  prefix is a naming convention, not a type.
- Promoting an edge candidate to an edge without reading the code.

References
- `agent_onboarding/default/engineer/skills/src_graph_usage.md`
- `agent_onboarding/default/engineer/skills/staleness_protocol.md`
- `agent_onboarding/default/engineer/skills/context_protocol.md`
