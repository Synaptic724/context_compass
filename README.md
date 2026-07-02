# Context Compass

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

## Quickstart

1. Clone this repo or download a copy of it.
2. Take the `context_compass` folder from `src/context_compass/` and place it at the
   top level of your own repository.
3. Direct agent to the agents.md in the `src/context_compass/` directory and ask the agent to onboard as an `engineer`.
4. That agent now has access to the core features of Context Compass.
5. After each compacting event ensure the agent re-onboards as the role you chose.

## What Lives In The Package

Core control files inside `src/context_compass/`:
- `AGENTS.MD`
- `SKILLS.md`
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
- `src/context_compass/SKILLS.md`
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

## Final Word

Context Compass is for people who want agent work to survive reality.

Not just the first good chat.
Not just the current model.
Not just one platforms memory pane.

If you want project memory that stays with the repo, survives branch work,
handles handoffs, resists drift, and still makes sense when another agent shows
up later, that is exactly what this system is for.