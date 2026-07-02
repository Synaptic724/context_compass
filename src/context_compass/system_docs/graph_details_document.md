# Graph Details Document

## Metadata
- Doc ID: DOC-GRAPH-2026-04-19
- Status: in_progress
- Owner: codex
- Created: 2026-04-19
- Updated: 2026-06-13

## Purpose
Define the canonical graph-details contract for one chosen repo-local
source/runtime surface so agents can load a concise relationship map for
eligible source objects without replacing the existing long-form architecture
and component docs.

This document is the canonical workflow and schema reference for:
- `system_docs/src_graph.json`
- `system_docs/readable_src_graph.json`

## Canonical Artifacts
- Canonical storage file:
  - `context_compass/system_docs/src_graph.json`
- Required readable consumption file:
  - `context_compass/system_docs/readable_src_graph.json`
- Canonical workflow/spec doc:
  - `context_compass/system_docs/graph_details_document.md`
- Active editing pattern:
  - `context_compass/system_docs/patches/active/<patch_id>/src_graph.expanded.json`
- Example workflow files:
  - `context_compass/examples/example_graph_details/graph_details_document.md`
  - `context_compass/examples/example_graph_details/src_graph.expanded.json`
  - `context_compass/examples/example_graph_details/src_graph.json`
  - `context_compass/examples/example_graph_details/readable_src_graph.json`
- Generation recipe skill:
  - `agent_onboarding/default/engineer/skills/graph_details_readable_generation.md`

## Artifact Roles
- `src_graph.json`
  - compressed canonical storage artifact
- `readable_src_graph.json`
  - required readable JSON consumption artifact
  - derived from the compressed canonical file by raw-text reflow
  - used for line-based reading through viewer-style tools
- `src_graph.expanded.json`
  - whole-document editing artifact under the active patch lane
  - used for patching and line-based edit review only while a graph lane is active

## Relationship To Architecture And Components Docs
`src_architecture.md` and `src_components.md` remain the canonical long-form
explanation surfaces.

`src_graph.json` is not a third prose architecture document. Its role is:
- capture eligible source coverage for the chosen source/runtime surface
- state what each covered object/module is
- show how those covered objects/modules are wired together
- distinguish hard ownership from borrowing, creation, validation, and other
  semantic relationships

Use the graph for fast structural traversal.
Use architecture/components docs for full narrative and deeper lifecycle detail.

## Scope Boundary
The canonical graph targets one chosen source/runtime surface at a time.

In scope:
- the repo-local source/runtime surface selected for graph coverage
- example source roots may look like `src/**` or another runtime subtree
  chosen by the user

Out of scope:
- `tests/**`
- examples
- tickets
- onboarding docs
- patch docs

If test relationships matter later, they belong in a separate test-side graph
surface, not in `src_graph.json`.

## Canonical Schema
The graph uses one canonical schema only:

```json
{
  "schema_version": 1,
  "nodes": {},
  "edges": []
}
```

### Node Contract
Each node must include exactly these fields:

```json
{
  "id": "",
  "label": "",
  "kind": "",
  "file": "",
  "role": "",
  "responsibilities": [],
  "owns_state": [],
  "phases": []
}
```

Field meanings:
- `id`
  - stable canonical unique object id
  - use fully qualified code identity
  - example: `package.runtime.component.ComponentRoot`
- `label`
  - short display label
  - example: `ComponentRoot`
- `kind`
  - one of:
    - `class`
    - `component`
    - `interface`
    - `module`
- `file`
  - repo-relative file path
  - never use absolute paths
- `role`
  - one-sentence statement of what the object is
- `responsibilities`
  - short list of what it does
- `owns_state`
  - important fields/resources it owns
- `phases`
  - relevant lifecycle phases:
    - `init`
    - `validation`
    - `runtime`
    - `refresh`
    - `cleanup`

### Edge Contract
Each edge must include exactly these fields:

```json
{
  "from": "",
  "to": "",
  "relation": "",
  "why": "",
  "cardinality": "",
  "phase": [],
  "strength": ""
}
```

Field meanings:
- `from`
  - source node id
- `to`
  - target node id
- `relation`
  - plain-language UML-shaped relationship
- `why`
  - one sentence explaining what the relationship actually means
- `cardinality`
  - one of:
    - `one_to_one`
    - `one_to_many`
    - `many_to_one`
    - `many_to_many`
- `phase`
  - relevant lifecycle phases for the relationship
- `strength`
  - one of:
    - `hard`
    - `borrowed`
    - `soft`

### Allowed Relation Values
Use these values only:
- `contains`
- `specializes`
- `implements`
- `owns_lifecycle_of`
- `holds`
- `borrows`
- `creates`
- `uses`
- `used_by`
- `calls`
- `validates`
- `publishes`
- `binds`
- `binds_into`
- `queries`

Additional live relation meanings:
- `holds`
  - source keeps identity, metadata, or attached runtime state for the target
    without necessarily owning the full lifecycle
- `used_by`
  - inverse helper-facing dependency wording used when the graph wants the
    helper surface as the source node and the consuming runtime surface as the
    target node
- `binds_into`
  - source publishes or merges its local truth into the target system/state
    registry as part of aggregation or later-phase reuse

Do not invent ad hoc edge labels unless the schema is intentionally revised.

## Inclusion Rules
The graph is exhaustive for eligible files inside the chosen repo-local
about how those files are wired.

Include:
- every non-`__init__.py` file under the chosen source/runtime surface
- richer node semantics where the file exposes important classes/components
- relationships that materially improve ownership, creation, borrowing,
  validation, publication, binding, and runtime wiring comprehension
- when a file is currently scaffold-only or has no meaningful concrete class
  surface yet, represent it as a `module` node rather than omitting it from
  coverage

Do not include:
- anything under `tests/`
- `__init__.py` files as graph nodes
- import-graph noise
- long narrative prose from architecture/components docs

The graph should stay useful while still preserving exhaustive eligible-file
coverage.

## Authoring Workflow (Non-Negotiable)
The canonical storage file stays compressed.
Agents must not hand-edit the compressed storage file directly.

Required workflow:
1. Read the current compressed canonical file:
   - `context_compass/system_docs/src_graph.json`
   - treat it as a storage blob, not a line-oriented review surface
2. Expand the whole file into an active patch-lane working copy:
   - `context_compass/system_docs/patches/active/<patch_id>/src_graph.expanded.json`
3. Edit the expanded whole-document patch copy only.
   - keep the graph scoped to `src/` only
   - keep `__init__.py` files excluded from graph nodes when updating the graph
4. Validate the expanded JSON and the schema discipline.
5. Recompress the full document back into canonical storage.
6. Regenerate `readable_src_graph.json` from the compressed canonical file.
7. Validate the readable JSON view and line-width contract.
8. Keep the expanded patch copy as temporary patch-lane state only.

### Consumption Contract
The compressed canonical file is intentionally not line-readable.

Implications:
- The compressed file may be one physical line.
- The `viewer_tool_read_limit` / line-count rules are not a meaningful way to
  inspect compressed canonical JSON.
- Do not try to review or reason about the compressed canonical file by line
  number.

Required read rule:
- Use `readable_src_graph.json` as the primary line-based reading surface.
- Use `src_graph.json` as storage only.
- Use `src_graph.expanded.json` only when editing the graph.

Use the compressed file for:
- storage
- canonical overwrite target after recompression
- regeneration source for `readable_src_graph.json`

Use the readable file for:
- line-based reading
- chunked viewer consumption
- quick structural rereads without opening the expanded edit copy

Do not use the compressed file for:
- line-based review
- evidence citation by line
- direct manual patching
- partial in-place edits

### Readable JSON Generation Contract
`readable_src_graph.json` is produced by opening the compressed canonical file
as raw text and reflowing that raw JSON into `220`-character lines.

Generation rules:
- do not pretty-print by reparsing into a verbose multi-thousand-line layout
- do not change keys, values, ordering, or JSON structure
- only insert newlines
- only break at safe non-string delimiters
- keep each output line at or below `220` characters
- keep the output valid JSON

This is a text-reflow artifact, not a semantic transform.

### Required PowerShell Workflow
Expand the canonical graph into a patch-lane working copy:

```powershell
$source = 'codex/context_compass/system_docs/src_graph.json'
$working = 'codex/context_compass/system_docs/patches/active/<patch_id>/src_graph.expanded.json'
$data = Get-Content $source -Raw | ConvertFrom-Json
$data | ConvertTo-Json -Depth 100 | Set-Content $working
```

Validate the expanded working copy:

```powershell
$working = 'codex/context_compass/system_docs/patches/active/<patch_id>/src_graph.expanded.json'
Get-Content $working -Raw | ConvertFrom-Json | Out-Null
```

Recompress the expanded working copy back into canonical storage:

```powershell
$source = 'codex/context_compass/system_docs/src_graph.json'
$working = 'codex/context_compass/system_docs/patches/active/<patch_id>/src_graph.expanded.json'
$data = Get-Content $working -Raw | ConvertFrom-Json
$data | ConvertTo-Json -Depth 100 -Compress | Set-Content $source
```

Regenerate the readable JSON consumption view from the compressed canonical
graph:

```powershell
$source = 'codex/context_compass/system_docs/src_graph.json'
$output = 'codex/context_compass/system_docs/readable_src_graph.json'
$width = 220
$raw = Get-Content $source -Raw
$sb = New-Object System.Text.StringBuilder
$current = New-Object System.Text.StringBuilder
$inString = $false
$escaped = $false
$lastSafeBreak = -1

function Flush-Line {
    param([string]$Text)
    $null = $sb.Append($Text)
    $null = $sb.Append("`r`n")
}

for ($i = 0; $i -lt $raw.Length; $i++) {
    $ch = $raw[$i]
    $null = $current.Append($ch)

    if ($inString) {
        if ($escaped) {
            $escaped = $false
        } elseif ($ch -eq '\') {
            $escaped = $true
        } elseif ($ch -eq '"') {
            $inString = $false
        }
    } else {
        if ($ch -eq '"') {
            $inString = $true
        }
        if ($ch -eq ',' -or $ch -eq '{' -or $ch -eq '}' -or $ch -eq '[' -or $ch -eq ']') {
            $lastSafeBreak = $current.Length - 1
        }
    }

    if ($current.Length -ge $width -and $lastSafeBreak -ge 0) {
        $line = $current.ToString().Substring(0, $lastSafeBreak + 1)
        Flush-Line $line
        $remainder = $current.ToString().Substring($lastSafeBreak + 1)
        $current.Clear() | Out-Null
        $current.Append($remainder) | Out-Null
        $lastSafeBreak = -1
    }
}

if ($current.Length -gt 0) {
    Flush-Line $current.ToString()
}

Set-Content -Path $output -Value $sb.ToString() -Encoding utf8
```

Validate the readable JSON view:

```powershell
Get-Content codex/context_compass/system_docs/readable_src_graph.json -Raw | ConvertFrom-Json | Out-Null
$max = (Get-Content codex/context_compass/system_docs/readable_src_graph.json | ForEach-Object { $_.Length } | Measure-Object -Maximum).Maximum
$max
```

This is a whole-document edit workflow. Do not patch a subset of the compressed
canonical file in place.

## Maintenance Rules
Update `src_graph.json` when any of these change:
- a new important system object becomes part of the canonical mental model
- object ownership changes
- creation responsibility changes
- borrowing vs hard lifecycle responsibility changes
- validation/publication/binding relationships change
- architecture/components docs are updated with new canonical wiring

When graph changes are made:
- update the expanded patch copy
- recompress to canonical storage
- regenerate `readable_src_graph.json`
- keep architecture/components docs aligned if the graph reflects a real
  architectural delta

## Validation Expectations
At minimum, validate:
- compressed canonical graph parses as JSON
- expanded working graph parses as JSON
- readable consumption graph parses as JSON
- readable consumption graph stays at `220` characters or less per line
- node ids are unique
- every edge target/source exists as a node
- relation values stay inside the allowed vocabulary

Recommended commands:

```powershell
Get-Content codex/context_compass/system_docs/src_graph.json -Raw | ConvertFrom-Json | Out-Null
Get-Content codex/context_compass/system_docs/readable_src_graph.json -Raw | ConvertFrom-Json | Out-Null
Get-Content codex/context_compass/system_docs/patches/active/<patch_id>/src_graph.expanded.json -Raw | ConvertFrom-Json | Out-Null
Get-Content codex/context_compass/examples/example_graph_details/src_graph.json -Raw | ConvertFrom-Json | Out-Null
Get-Content codex/context_compass/examples/example_graph_details/readable_src_graph.json -Raw | ConvertFrom-Json | Out-Null
Get-Content codex/context_compass/examples/example_graph_details/src_graph.expanded.json -Raw | ConvertFrom-Json | Out-Null
```

## Anti-Patterns (Reject)
- editing the compressed canonical file directly
- treating the compressed canonical file as the primary line-based read surface
- regenerating the readable view by semantic reshaping instead of raw-text
  reflow
- splitting graph details and graph network into separate competing canonical files
- using absolute paths
- adding `tests/` objects into `src_graph.json`
- adding `__init__.py` files as graph nodes
- using non-unique object names as ids
- duplicating long-form architecture/components prose into the graph
- treating the graph as a whole-repo file inventory outside the agreed
  chosen source/runtime scope
- adding relation labels that are not in the controlled vocabulary without
  intentionally revising the schema

## Context / Handoff Summary
This document defines the canonical graph-details schema and the required
expand-edit-compress workflow for maintaining `src_graph.json`. The graph is
exhaustive over eligible files in the chosen source/runtime surface, relationship-focused, and
complementary to
`src_architecture.md` and `src_components.md`, not a replacement for them.
