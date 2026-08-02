# example_graph_details

Shape reference for the generated source graph.

The graph is **derived from source code**, not authored. Two files are produced
by `tools/system_documents/python/`, and neither ships in `system_docs/` - a
fresh install has neither, and that is expected:

- `system_docs/src_graph.md` - one section per source file
- `system_docs/src_graph_index.md` - line ranges into it, plus staleness proof

## This example is reproducible

`src/example/` here is a real six-file Python package, and `src_graph.md` /
`src_graph_index.md` are the unmodified output of running the real pipeline over
it. Nothing was hand-written, trimmed, or annotated afterwards.

```bash
cd context_compass/examples/example_graph_details
python ../../tools/system_documents/python/extract_graph.py --src src --out /tmp/desc
python ../../tools/system_documents/python/assemble_graph.py --descriptors /tmp/desc --out /tmp/out
```

The result matches what ships here, except for the authored fields - those are
tier 3 and were added to the descriptors by hand, which is exactly the documented
workflow. That is the point of the example: it shows both what the extractor
recovers and what a human has to supply.

Because the output is unmodified, **the index actually proves the document**.
Recompute `line_count` and `content_sha256` over `src_graph.md` and they match
the staleness proof, and every range lands on its own `BEGIN FILE` / `END FILE`
delimiter. An example you can verify is worth more than one you have to trust.

## What a section looks like

Each source file gets one section, delimited by HTML comments naming the file.
Line ranges for every section live in the index; read the index and slice, never
scan the document for delimiters.

The `BEGIN FILE` / `END FILE` comments are the section boundaries. They do not
render, and the index's ranges are measured against them - a section written
without them is not addressable.

See `src_graph.md` lines 80-124 for the richest section: a class with derived
and authored edges, authored semantics, and unconfirmed candidates side by side.

## What is derived and what is authored

This distinction is the whole contract. Measured against a hand-authored graph
of 535 nodes and 997 edges:

| field | origin | recovery |
|---|---|---|
| `id`, `label`, `kind`, `file`, `lineno`, `bases`, `public_methods` | derived | 94% |
| `specializes`, `implements` | derived | 94%, targets resolved 99% |
| `creates` | **candidate only** | 57%, over-generated ~8x |
| `role`, `responsibilities`, `owns_state`, `phases` | authored | not derivable |
| `owns_lifecycle_of`, `uses`, `borrows` | authored | **not derivable** |

`owns_lifecycle_of`, `uses`, and `borrows` are syntactically identical - each is
"A holds a reference to B". Which one it is, is a design fact that appears
nowhere in the source text. That is 68% of all edges, and it is why the graph has
an authored layer at all.

You can see it in this example. `Pipeline` holds a `Stage` list and a `Store`
reference. The AST shows both as attributes; only a human knows the pipeline owns
its stages and borrows the store. The extractor emitted neither edge.

And because the claim is authored, the reason is shown next to it:

```
| `..Pipeline` | owns_lifecycle_of | `..Stage` | one_to_many | init,runtime,cleanup | authored |
| `..Pipeline` | borrows           | `..Store` | many_to_one | runtime             | authored |

- `..Pipeline` -> `..Stage`: Pipeline constructs its stages in __init__ and is the
  only object that can release them, so the stage list dies with the run.
- `..Pipeline` -> `..Store`: The store is passed in and outlives the pipeline.
  Releasing the pipeline must not close it - several pipelines share one store.
```

Derived rows carry `-` in the authored columns. That is not missing data: it is
the graph saying nobody has authored that relationship's semantics yet.

`why` sits beneath the table rather than in it, so the table stays scannable. On
this example the whole authored layer costs 3 lines out of 192, and you never pay
it on a read you did not ask for - you slice one section, not the document.

A node marked **UNSEMANTIC** carries mechanical scaffold and no meaning yet. Its
structure is trustworthy; do not infer its purpose from its name.

## Two index shapes, do not confuse them

`src_graph.md` is GENERATED, so its index is emitted by `assemble_graph.py` in
the same pass - keyed by **source path**. Authored documents get their index from
`index_document.py` by walking headings - keyed by **heading breadcrumb**.

Running `index_document.py` against `src_graph.md` produces a heading-shaped
index of `## src/...` and `### Nodes` sections. It parses, but it is the wrong
artifact: it indexes the rendering rather than the files, and every section named
`Nodes` collides. The tool will warn about the collision.

## Index shape

```markdown
| lines | source | nodes | edges |
| --- | --- | --- | --- |
| 11-26 | `src/example/__init__.py` | 1 | 0 |
| 80-124 | `src/example/pipeline/pipeline.py` | 2 | 3 |
```

The `edges` count covers derived and authored edges together, matching what that
section's `Edges out` table renders. Candidates are not counted - they are
guesses, not edges.

Every row is keyed by a name - here the source path. No index in this system uses
a bare number as identity: a row keyed by a number tells a reader nothing about
whether to read it.

## Files here

- `src/example/` - a six-file Python package, the input
- `src_graph.md` - unmodified assembler output over that package
- `src_graph_index.md` - unmodified index from the same pass
- this README

## References

- `agent_onboarding/default/engineer/skills/src_graph_generation.md` - building
- `agent_onboarding/default/engineer/skills/src_graph_usage.md` - reading
- `agent_onboarding/default/engineer/skills/system_document_build.md` -
  the authored documents and their indexes
