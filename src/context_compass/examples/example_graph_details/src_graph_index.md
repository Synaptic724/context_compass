# src_graph_index

Line ranges into `src_graph.md`. Emitted by the same pass that wrote the
document, so the ranges cannot have drifted from it.

Line numbers are 1-based and inclusive on both ends.

## Staleness proof

| field | value |
| --- | --- |
| document | `src_graph.md` |
| index_version | 1.0.0 |
| generated_at | 2026-08-02T09:31:52Z |
| line_count | 192 |
| line_ending | lf |
| content_sha256 | `a655ccfaee86bb59aa26613ab714da5ea770572e5b098a85f296e84d9e9a6366` |
| sections | 6 |

Recompute `line_count` and `content_sha256` before slicing. On any
mismatch the document was hand-edited: STOP, do not slice, reassemble.

## Sections

| lines | source | nodes | edges |
| --- | --- | --- | --- |
| 11-26 | `src/example/__init__.py` | 1 | 0 |
| 28-51 | `src/example/core/interfaces.py` | 2 | 0 |
| 53-78 | `src/example/core/resource.py` | 2 | 0 |
| 80-124 | `src/example/pipeline/pipeline.py` | 2 | 3 |
| 126-148 | `src/example/pipeline/stage.py` | 2 | 0 |
| 150-191 | `src/example/storage/store.py` | 2 | 1 |
