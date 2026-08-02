# Context Compass

[![PyPI](https://img.shields.io/pypi/v/contextcompass.svg)](https://pypi.org/project/contextcompass/)
[![Python](https://img.shields.io/pypi/pyversions/contextcompass.svg)](https://pypi.org/project/contextcompass/)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

**Working memory for coding agents, stored in your repo instead of a chat window.**

```bash
cd my-repo
uvx contextcompass init
```

That writes a `context_compass/` directory into your project. Point an agent at
`context_compass/AGENTS.MD`, and its tickets, decisions, evidence and handoff
state live in files you own — surviving compaction, new chats, model swaps, and
the next agent.

Context Compass exists because agent work falls apart the second the chat stops
being fresh.

You start in one thread, the context gets long, compaction happens, the model
forgets half the reasoning, another agent takes over, or you switch from GPT to
Claude to Gemini and suddenly the work has no memory of why it looks the way it
looks.

Context Compass fixes that by moving the working memory into the repo.

Instead of trusting one platform UI to remember everything, it gives the work a
place to live in files you own, commit, diff, keep on the branch, and hand to
another agent later.

## Why It Exists

Most AI-assisted work breaks for boring reasons:
- the agent forgot what it was doing
- the next chat lost the reasoning
- the important decisions stayed in chat instead of in the project
- compaction wiped the context
- a new agent took over with no reliable handoff
- the platform kept the task state, but you wanted to keep the task state

That is the real problem Context Compass solves.

It is not just a prompt pack.
It is not just a documentation template.
It is a persistence and control layer for agent work.

## What You Get

### Durable project memory
Context lives in the repo instead of only in chat.

That means:
- work survives compaction
- work survives new chats
- work survives model swaps
- work survives agent handoff
- work stays attached to the branch where it happened

### Platform-agnostic continuity
If you use GPT, Claude, Gemini, or something else later, the project memory is
still there.

The value is not tied to one vendor UI.
The value is that the working state becomes part of the repo itself.

### Repo-owned tickets and notes
If you want the tickets, the notes, the artifacts, and the handoff state to
belong to you, they need to live in your project.

Context Compass gives you that.

Instead of losing state to:
- a plan panel
- a memory tab
- a temporary task list
- a chat thread that may be compacted or archived

you keep the state in versioned files that can move with the code.

### Drift resistance
Context Compass is built to resist the common failure modes of agent work.

That includes:
- evidence before assertion
- explicit `UNKNOWN` instead of fake certainty
- structured note-taking during execution
- re-onboarding after compaction or handoff
- policy gates before action
- durable artifacts linked to durable work items
- prompt_ids shown created by agent to help with drift resistence

### Better handoffs
The package now includes mailbox support for direct agent-to-agent messages.

That matters because not every handoff should be broadcast to the main board.
Some work needs directed communication without turning the whole system into
noise.

### Reusable context packs
The package also includes optional context management.

That gives you a place to store focused reread packs for larger tasks, so an
agent does not have to rediscover the same background every time it picks work
back up.

## What Context Compass Actually Is

At a practical level, Context Compass is a Git-backed execution system for
AI-assisted work.

It gives you:
- an onboarding contract
- role maps and routed skill chains
- ticket-first execution
- durable notes and evidence
- artifact tracking
- mailbox handoff support
- optional context packs
- re-entry rules after compaction and handoff

The point is simple:
- chat memory is weak
- repository state is durable
- process should be recoverable from files, not vibes

## Install

Three ways in. They produce the **same `context_compass/` directory** in your
repo — pick whichever fits how you work.

### 1. uvx — nothing installed, nothing cloned (recommended)

```bash
cd my-repo
uvx contextcompass init
```

`uvx` fetches the package into a throwaway environment, runs it, and discards it.
Nothing lands in your project's dependency tree, because a repo-scaffolding tool
has no business there.

Pin a version for reproducibility, or track the latest:

```bash
uvx contextcompass@2.11.0 init     # exact, repeatable
uvx contextcompass@latest init     # whatever is newest
```

<details>
<summary>Don't have uv yet?</summary>

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
wget -qO- https://astral.sh/uv/install.sh | sh     # if you have no curl
```

```powershell
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

uv also installs Python itself, which is the other reason to have it:

```bash
uv python install 3.14        # or 3.12, 3.13 - whichever you want
uv python install 3.14t       # the `t` suffix is the free-threaded build
uv venv --python 3.14         # creates .venv using that interpreter
```

`uv venv` downloads the interpreter if it is missing, so the separate
`uv python install` is optional.
</details>

### 2. pip / pipx — if you would rather not use uv

```bash
pipx install contextcompass && contextcompass init    # isolated, preferred
pip install --user contextcompass && contextcompass init
```

`pipx` is recommended over plain `pip` for the same reason as `uvx`: it keeps a
scaffolding tool out of your project environment. Either works.

### 3. Clone — no Python needed at all

The package is **Markdown**. If all you want is the system, copy the folder:

```bash
git clone https://github.com/Synaptic724/contextcompass
cp -r contextcompass/src/context_compass my-repo/
```

```powershell
# Windows
git clone https://github.com/Synaptic724/contextcompass
Copy-Item -Recurse contextcompass\src\context_compass my-repo\
```

That is the whole installation — no runtime, no dependencies, no build step.
Clone when you want to read the source first, work offline, vendor a specific
commit, or modify the package before adopting it.

### What actually needs Python

Only `tools/` — the scripts that build the manifest, index documents, generate
the source graph, and upgrade an install. **Python 3.10+, stdlib only, no
dependencies ever.** An agent that has to `pip install` before it can read a
document is an agent that cannot read the document on a fresh clone.

Tested on 3.10 through 3.14 (including free-threaded 3.14t) on Linux and Windows,
on every push.

Verify an install any time:

```bash
python context_compass/tools/package_manifest.py --root context_compass --check
```

## Quickstart

```bash
cd my-repo
uvx contextcompass init          # or clone and copy - see Install
```

1. Point your agent at `context_compass/AGENTS.MD` and ask it to onboard as an
   `engineer`.
2. Approve the certification step it asks for: `CERTIFY: APPROVED`.
3. Work normally. The agent routes through `attention_board.md` and the active
   ticket, and writes findings into ticket `## Notes`.
4. Commit `context_compass/`. It is your repository's memory now, and it is meant
   to be reviewed and diffed like any other source.
5. **After every compaction or handoff, tell the next agent to re-onboard.** That
   is the whole trick — it rebuilds context from the repo instead of guessing
   from a half-remembered chat.

## What Lives In The Package

Core control files inside `src/context_compass/`:
- `AGENTS.MD`
- `SKILLS.MD`
- `config/context_compass_config.yaml`
- `attention_board.md`
- `artifact_board.md`
- `mailbox_board.md`

Execution state:
- `tickets/epics/`
- `tickets/stories/`
- `tickets/tasks/`
- `artifacts/`

Optional extended context:
- `context_management/`

Project-specific extension point:
- `special_instructions/`

System documentation:
- `system_docs/`

## How The Work Flows

The operating model is straightforward.

### 1. Onboard
The agent starts from `AGENTS.MD`, reads the policy chain, resolves the chosen
role, and reads the required baseline docs.

### 2. Certify
Before real work starts, the onboarding/certification gate is supposed to be
completed.

### 3. Route work through the repo
Active work is routed through:
- `attention_board.md`
- the linked active ticket
- ticket notes as durable execution memory

### 4. Track outputs
Artifacts are tracked separately from tickets through `artifact_board.md`.

### 5. Use mailbox when handoff is direct
If one agent needs to tell one other agent something specific, use the mailbox
instead of polluting the main routing surface.

### 6. Recover after compaction
When compaction or handoff happens, the next agent can rebuild context from the
repo state instead of guessing from a half-remembered chat.

## Core Surfaces

### `attention_board.md`
This is the routing surface.

It tells you:
- what is active
- who owns it
- what mode it is in
- what comes next

### `tickets/*`
This is where the actual work memory lives.

The ticket notes are where findings, decisions, blockers, evidence, and next
steps should be captured.

### `artifact_board.md`
This tracks outputs and what should happen to them.

### `mailbox_board.md`
This handles direct point-to-point agent communication.

### `context_management/`
This holds optional derived context packs for work that is too large or too long
to keep rediscovering from scratch.

### `special_instructions/`
This is where project-specific instructions go.

That keeps local repo rules out of the generic policy body while still making
sure agents can read them.

## Why People Use It

People use Context Compass when they are tired of re-explaining the same project
state over and over.

They use it when:
- chats reset too often
- compaction kills continuity
- another agent needs to pick work up cleanly
- they want the working memory to stay with the branch
- they want the notes and tickets to belong to the repo, not the platform
- they want a process that can survive time, tool changes, and handoffs

The key value is ownership.

You own the state.
You can review it.
You can diff it.
You can commit it.
You can hand it to another agent.
You can come back later and still know what happened.

## Role Maps And Skills

Context Compass keeps role maps because different kinds of work need different
behavior.

That lets you route an agent into:
- general software work
- design work
- platform work
- QA work
- security work
- writing and editorial roles
- user-defined overlays

The point is not to create fake personalities.
The point is to load the right guidance for the work while keeping the same
shared execution system underneath.

## Detailed Setup

### Step 1: Place Context Compass in your repo
Copy the packaged `context_compass` folder from this repository into the top
level of your own repo:
- `src/context_compass/...`

### Step 2: Keep the entrypoint intact
The main entrypoint shipped in this package is:
- `src/context_compass/AGENTS.MD`

That file should stay in place, because it is what your agent uses to begin
onboarding into the system.

### Step 3: Decide how you want the agent to work
Role maps live in:
- `src/context_compass/SKILLS.MD`
- `src/context_compass/config/context_compass_config.yaml`

For normal software work, the simplest starting point is to ask the agent to
onboard as:
- `engineer`

### Step 4: Let the agent onboard into the system
Once the files are in your repo and you have chosen the role, the agent should
read the entrypoint, resolve the role chain, and load the required baseline
skills before doing work.

### Step 5: Approve execution
Before the agent starts editing files or using tools, complete the certification
step it requests:
- `CERTIFY: APPROVED`

### Step 6: Keep the work in the repo
Once the agent is running, active work should route through:
- `attention_board.md`
- the linked active ticket

That is what keeps the working memory in the repository instead of trapped in
one chat thread.

### Step 7: Use the system the same way after compaction or handoff
If the chat is compacted, the session resets, or another agent takes over, the
next agent should re-onboard, rebuild context from the repo state, and continue
from there instead of relying on temporary chat memory.

## Upgrading An Existing Install

Your repo owns its tickets, artifacts, system docs, project instructions, and
both `user_defined/` directories. An upgrade never touches any of them. What it
does update is the package: skills, policies, templates, tools, and the boards'
package-owned text.

```bash
uvx contextcompass@latest upgrade --check     # exactly what would change
uvx contextcompass@latest upgrade --apply     # do it
```

The installed package **is** the new version, so there is no second checkout to
keep in sync. If you cloned instead, point the script at wherever your newer copy
lives:

```bash
python context_compass/tools/update_context_compass.py \
    --install context_compass --new /path/to/new/src/context_compass --check
```

Every tool here refuses to act without `--apply` and prints a full plan under
`--check`. **Read the plan.**

### How it decides what is safe to replace

One hash tells you a file changed. It cannot tell you *who* changed it, which is
the only question that matters. So three are compared — what shipped, what is on
disk, and what is incoming:

| on disk | incoming | what happens |
| --- | --- | --- |
| unchanged | changed | **replace** — clean update |
| unchanged | unchanged | skip |
| **you edited it** | unchanged | **keep yours** — nothing to conform to |
| **you edited it** | changed | **conform**, and say so by name |

Lanes that are yours outright — `tickets/`, `artifacts/`, `system_docs/`,
`special_instructions/`, `user_defined/`, `agent_onboarding/user_defined/` — are
never touched in any mode.

### Boards keep your rows

The three boards carry `USER-DEFINED` regions. Everything inside them is yours
and no tool writes there in any mode; everything outside is package structure
that gets conformed, so the boards' shape can actually improve over time.

Boards created before those regions existed hold their rows in open text, where
nothing distinguishes them from stale package headings. The updater will not
conform such a board - it says so and names the fix:

```bash
uvx contextcompass@latest migrate-boards --check --diff
uvx contextcompass@latest migrate-boards --apply
```

That moves existing content into the matching regions. Anything with no matching
region is parked under `## Notes` rather than dropped. Run it once; afterwards
upgrades are ordinary.

Migrating three real boards carrying 277 lines of live agent state moved every
line and lost **zero**, verified line-by-line against a pre-migration snapshot.

### The other tools

Everything under `context_compass/tools/`. All stdlib-only, all `--check` before
`--apply`.

| tool | what it does |
| --- | --- |
| `package_manifest.py` | what ships, who owns it, its hash. Everything else reads this. |
| `update_context_compass.py` | upgrade an install to a newer package |
| `migrate_boards.py` | one-time board migration into `USER-DEFINED` regions |
| `cleanup_context_compass.py` | repair a broken install, or reset lanes for a release |
| `build_llm_full.py` | concatenate the package into one file, plus a line-range index |
| `system_documents/index_document.py` | line-range index over an authored document |
| `system_documents/python/extract_graph.py` | derive the source graph from code |
| `system_documents/python/assemble_graph.py` | render the graph and its index |
| `system_documents/python/graph_walker.py` | state of the graph's authored tier |
| `system_documents/python/graph_semantics_tickets.py` | turn unauthored areas into tickets, on demand |
| `system_documents/python/migrate_authored_graph.py` | carry an authored graph out of the retired JSON format |

## Feed The Whole System To A Model

Sometimes you want a model to see everything at once — reviewing a change to the
onboarding contract, working out why two policies disagree, handing the system to
something that cannot browse a filesystem.

```bash
python context_compass/tools/build_llm_full.py \
    --root context_compass --out llm_full.md
```

That writes two files: `llm_full.md` (every file concatenated, ~27,000 lines) and
`llm_full_index.md` (**482 lines** saying which lines each file occupies).

**Read the index, slice what you need, never load the document whole.** The index
is 1.7% of the size and tells you exactly where everything is:

```bash
python context_compass/tools/build_llm_full.py \
    --root context_compass --out llm_full.md --slice context_compass/AGENTS.MD
```

The index is a **byproduct of the same pass** that writes the document — the
ranges were recorded by the loop that emitted the lines, so the two cannot
disagree. It also carries `line_count` and `content_sha256`, and `--slice`
recomputes both before returning anything. Edit the document by hand and the next
slice refuses rather than confidently handing back the wrong file.

## What Makes It Safe To Upgrade

The package installs into repositories that agents actively write to, so the
tooling is built around not destroying that work.

- **Ownership classes.** Every shipped file is PACKAGE, RESET, INSTANCE, LIVE or
  CONFIG, recorded with its hash in a generated `MANIFEST.md`. Derived from the
  files themselves, so it cannot drift the way a hand-bumped version stamp does.
- **`USER-DEFINED` regions.** Marked areas in boards and templates that no tool
  writes to in any mode — so the package can update the *structure* around your
  content instead of freezing forever to avoid touching it.
- **Content Preservation Gate.** Recompositions compare a line multiset before
  and after, counting a line moved to a named target as preserved and anything
  else as a defect.
- **Line-range indexes with staleness proofs.** Insert one line near the top of an
  indexed document and every range below it is wrong — while still parsing and
  still returning content. Every index carries `line_count` + `content_sha256`,
  and every consumer refuses on mismatch.
- **Config is merged by key**, never overwritten. New keys arrive with their
  comments; a value you set is never reset.
- **Nothing deletes authored work automatically.** Not a slogan — every tool that
  can remove something refuses without `--apply`, and the one that deletes
  authored prose refuses without a terminal to ask at.
- **405 tests, and mutation testing on top.** A green suite is equally consistent
  with "the code is correct" and "the tests assert nothing".
  `tests/mutation_check.py` applies 47 deliberate defects and requires that at
  least one test fails for every single one. Several survived their first run and
  each named a real gap.

```bash
uv sync && uv run pytest            # the suite
uv run python tests/mutation_check.py    # prove the suite has teeth
```

## Keeping The Source Graph Honest

Context Compass can derive a **source graph** from your code: one node per
class and module, with the relationships between them.

Half of it derives cleanly. The other half cannot, and being straight about
which is which is the whole design.

```python
self._pool = pool   # borrows
self._pool = pool   # uses
self._pool = pool   # owns_lifecycle_of
```

Three different relationships, identical syntax. The difference is design intent
that appears nowhere in the source text — measured against a hand-authored graph,
that is **68% of all edges**. A cleanup-contract heuristic was tested against a
labelled corpus of 997 authored edges and discriminated at 21% versus 21%: no
signal at all. So the graph has an **authored tier**, and nodes without one are
marked `UNSEMANTIC` rather than guessed at.

### The tier that rots

The mechanical tier self-heals — re-run the extractor and classes, bases and line
numbers are right again. **Authored prose does not.** It is written once and stays
exactly as written while the code underneath it moves, which over months produces
a graph full of confident descriptions of code that no longer works that way.

Four states, and a read-only walker to ask:

```bash
python context_compass/tools/system_documents/python/graph_walker.py \
    --descriptors <dir> --src src --report
```

| state | meaning |
| --- | --- |
| `UNSEMANTIC` | no authored fields — honest, not a defect |
| `AUTHORED` | source unchanged since the prose was written |
| `SEMANTICS_STALE` | **the source moved underneath it** — re-read before trusting |
| `RETIRED` | gone from source; prose kept for adjudication |

Staleness is tracked **per node**, not per file. A file-level hash would mark all
forty classes in a module stale because one changed, and a census that cries wolf
gets ignored.

### Deleting is an act, not a side effect

A class that disappears from source keeps its authored prose under
`nodes_retired` in the same descriptor. Clearing it needs `--reconcile`, which
lists every node and its prose, warns that only version control will have it
afterwards, and asks. **Without a terminal it refuses rather than assuming** — a
prompt that silently self-answers in CI is not a prompt.

### Turning the backlog into work, on demand

```bash
python context_compass/tools/system_documents/python/graph_semantics_tickets.py \
    --descriptors <dir> --tickets context_compass/tickets      # dry run
```

Off by default, dry-run unless you say `--create`, and a question unless you say
`--yes`. A library that writes tickets into your board unasked is doing something
hostile.

**Aggregated at the package**, which is a hard constraint rather than a
preference. Measured against a real 575-file, 1,188-node graph with 657 nodes
still unauthored:

| granularity | stories | outcome |
| --- | --- | --- |
| per node | 657 | destroys the board |
| per file | 575 | destroys the board |
| per directory | 146 | still too many |
| `--depth 4` | **36** | usable |
| `--min-nodes 5` | **46** | usable |

The last two are levers, and the tool prints them for you once the count gets
silly rather than emitting 146 stories and letting you find out. Neither loses
work — the nodes stay in the census either way; only the packaging changes.

One epic, one story per package with work, and **no tasks** — task granularity is
the working agent's judgement. Re-running updates rather than duplicating, and a
package that gets fully authored is reported `SATISFIED` so its story can close.
The loop closes in both directions or it is just a different kind of noise.

## Final Word

Context Compass is for people who want agent work to survive reality.

Not just the first good chat.
Not just the current model.
Not just one platforms memory pane.

If you want project memory that stays with the repo, survives branch work,
handles handoffs, resists drift, and still makes sense when another agent shows
up later, that is exactly what this system is for.