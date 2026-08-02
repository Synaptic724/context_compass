

# llm_full_usage

## Purpose
- Read `llm_full.md` - the whole package concatenated into one file - without
  loading a million characters to answer a question about three of them.
- Establish that the index is the entry point and the document is not.

## What these two files are

`llm_full.md` is every shipped package file end to end. `llm_full_index.md`
records the line range each file occupies, plus a staleness proof.

They live at the REPOSITORY root, not inside `context_compass/`. They are a view
of the package, not part of it, which is why the package can be installed
without them.

Generated together by one pass:

```bash
python context_compass/tools/build_llm_full.py \
    --root context_compass --out llm_full.md
```

The index is a **byproduct of that pass**, not a re-parse. The ranges were
recorded by the loop that emitted the lines, so index and document cannot
disagree. Contrast `index_document.py`, which re-walks an authored document's
headings and therefore has to be guarded by a hash.

## The rule

**Read the index. Slice what you need. Never read the document whole.**

`llm_full.md` is ~27,000 lines and ~1.1 MB. Reading it to find one skill is not
thoroughness, it is a context-window fire. The index is ~450 lines and tells you
exactly where everything is.

## How to read one file

```bash
# 1. find it in the index
rg 'AGENTS.MD' llm_full_index.md
#    | 11-402 | `context_compass/AGENTS.MD` | 392 | 15204 |

# 2. read exactly those lines
sed -n '11,402p' llm_full.md
```

Or let the tool do both, which verifies the index first:

```bash
python context_compass/tools/build_llm_full.py \
    --root context_compass --out llm_full.md --slice context_compass/AGENTS.MD
```

**Give it enough path to be unambiguous.** `--slice` matches on substring, and
bare `AGENTS.MD` matches 19 files - the root entrypoint plus one per role. When
several match it lists them with their ranges and refuses rather than guessing,
so an ambiguous query costs you a round trip, never the wrong file:

```
3 files match 'SKILLS.MD' - narrow it:
  19-26   context_compass/SKILLS.MD
  28-32   context_compass/agent_onboarding/default/engineer/SKILLS.MD
  40-44   context_compass/agent_onboarding/user_defined/myrole/SKILLS.MD
```

That listing is usable directly - take the range you wanted and `sed` it.

## Verify before you trust a range

```bash
python context_compass/tools/build_llm_full.py \
    --root context_compass --out llm_full.md --check
```

A line-offset index is more fragile than the text it indexes. Insert one line
near the top and every range below it is wrong - while still parsing, still
returning content, and returning the WRONG content confidently. The index
carries `line_count`, `line_ending` and `content_sha256` for exactly this
reason, and `--slice` recomputes them before returning anything.

**On mismatch: STOP.** Regenerate, or read the real file under
`context_compass/`. Do not eyeball an offset. Say which you did.

## When to use this at all

Use `llm_full.md` when the relationships between files are the point: reviewing
a change to the onboarding contract, working out why two policies disagree,
handing the whole system to a model that cannot browse a filesystem.

Do NOT use it as a substitute for reading the real file. If you are working
inside a repository that has `context_compass/`, read the file directly - it is
authoritative, it is what agents actually load, and it cannot be stale. This
document is a snapshot, and a snapshot is stale the moment the package changes.

## Anti-patterns (reject)

- Reading `llm_full.md` whole because "it is only one file".
- Slicing a range without recomputing the staleness proof.
- Quoting `llm_full.md` as evidence when the real file is on disk. Cite
  `context_compass/<path>:<start>-<end>`, not a range into a generated view.
- Hand-editing either file. Both are derived; edit the package and regenerate.
- Treating a stale index as "close enough" and adjusting the offset by eye.

## References
- `agent_onboarding/default/engineer/skills/src_graph_usage.md` - the same
  index-then-slice discipline, applied to the source graph
- `agent_onboarding/default/engineer/skills/system_document_build.md` - the
  index format specification
