# Example Graph Details Workflow

Purpose:
- demonstrate the canonical graph-details workflow in a small self-contained
  example

Files:
- `src_graph.expanded.json`
  - expanded whole-document working copy for patch editing
- `src_graph.json`
  - compressed canonical storage form
- `readable_src_graph.json`
  - line-broken readable JSON view generated from the compressed storage form

Scope:
- this graph targets source/runtime objects only
- test objects do not belong in this file

Workflow:
1. read the compressed file
2. expand it into the patch/editing copy
3. edit the whole expanded document
   - keep it scoped to `src/` only
   - keep `__init__.py` files excluded from graph nodes
4. validate it as JSON
5. recompress it back into storage
6. regenerate `readable_src_graph.json` from the compressed storage file using
   raw-text reflow at `220` characters

The example data is intentionally small. It demonstrates structure and workflow,
not full repo coverage.
