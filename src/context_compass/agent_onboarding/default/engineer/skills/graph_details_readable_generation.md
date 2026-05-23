# graph_details_readable_generation

## Purpose
- Define the canonical one-time generation method for:
  - `context_compass/system_docs/readable_src_graph.json`
- Keep the recipe in Markdown only.
- Do not add or keep a repo script file for this workflow.
- Use this only when the repository has opted into graph-details context
  maintenance.

## When To Use
- `readable_src_graph.json` is missing.
- `src_graph.json` changed and the readable file is stale.
- An agent needs to recreate the readable graph view from canonical storage.
- Do not use this workflow in a fresh install that has not created graph-detail
  surfaces yet.

## Required Contract
- Source:
  - `context_compass/system_docs/src_graph.json`
- Output:
  - `context_compass/system_docs/readable_src_graph.json`
- Width:
  - `220` characters maximum when a safe delimiter break exists
- Transform rule:
  - read the compressed canonical JSON as raw text
  - do not semantically reshape or pretty-print the JSON
  - only insert line breaks
  - only break at safe non-string delimiters
- Persistence rule:
  - keep the recipe in Markdown only
  - do not store a `.ps1`, `.sh`, or other code file in the repo for this
    workflow

## Safe Break Rule
Break only when not inside a JSON string and only after these delimiters:
- `,`
- `{`
- `}`
- `[`
- `]`

This keeps the output valid JSON while making it line-readable.

## PowerShell Recipe
Use this as a one-time inline command block, not as a saved script file:

```powershell
$source = 'context_compass/system_docs/src_graph.json'
$output = 'context_compass/system_docs/readable_src_graph.json'
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

## Bash Recipe
Use this as a one-time inline command block, not as a saved script file:

```bash
python - <<'PY'
from pathlib import Path

source = Path("context_compass/system_docs/src_graph.json")
output = Path("context_compass/system_docs/readable_src_graph.json")
width = 220
raw = source.read_text(encoding="utf-8")

lines = []
current = []
in_string = False
escaped = False
last_safe_break = -1

def flush(text: str) -> None:
    lines.append(text)

for ch in raw:
    current.append(ch)

    if in_string:
        if escaped:
            escaped = False
        elif ch == "\\":
            escaped = True
        elif ch == "\"":
            in_string = False
    else:
        if ch == "\"":
            in_string = True
        if ch in ",{}[]":
            last_safe_break = len(current) - 1

    if len(current) >= width and last_safe_break >= 0:
        flush("".join(current[: last_safe_break + 1]))
        current = current[last_safe_break + 1 :]
        last_safe_break = -1

if current:
    flush("".join(current))

output.write_text("\n".join(lines) + "\n", encoding="utf-8")
PY
```

## Validation
PowerShell:

```powershell
Get-Content context_compass/system_docs/readable_src_graph.json -Raw | ConvertFrom-Json | Out-Null
$max = (Get-Content context_compass/system_docs/readable_src_graph.json | ForEach-Object { $_.Length } | Measure-Object -Maximum).Maximum
$max
```

Bash:

```bash
python - <<'PY'
from pathlib import Path
import json

path = Path("context_compass/system_docs/readable_src_graph.json")
data = json.loads(path.read_text(encoding="utf-8"))
max_len = max((len(line) for line in path.read_text(encoding="utf-8").splitlines()), default=0)
print("OK_READABLE_JSON")
print(f"MAX_LINE_LEN\t{max_len}")
PY
```

## Edge Case
If one individual JSON token or string literal is itself longer than `220`
characters, safe delimiter-only reflow cannot keep that specific line under
`220` without changing the JSON payload. In that case:
- keep the readable file valid JSON
- accept the overrun temporarily
- shorten the underlying graph text later if the width contract truly matters

## Handoff Rule
When you regenerate the readable graph, report:
- source file used
- output file written
- max line length observed
- whether JSON validation passed
