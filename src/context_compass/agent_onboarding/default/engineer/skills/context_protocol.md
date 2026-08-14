

# context_protocol

Purpose
- Make the system documents the primary way you NAVIGATE: they turn "somewhere in
  this repository" into a short list of files worth opening.
- Keep the code authoritative for what the system actually DOES. The documents
  describe intent as of the moment somebody wrote it down; the code is what runs.

When to use
- Before any code edits, investigations, or architectural changes.

The order, in one line
`src_architecture.md` → the relevant parts of `src_components.md` → the wiring in
`src_graph.md` if you are going to code → **then the code itself, always, before you
change anything.** The documents narrow the search. Only the code settles what is
true, because only the code cannot be out of date.

`grep` and AST are guesses - they find a name, they do not explain a function. Use
them to pick where to start reading, then read and trace the call path.

Required flow - descend the hierarchy, do not enter in the middle
1. `system_docs/src_architecture.md` - which part of the system. Baseline read;
   you already hold it.
2. `system_docs/src_components_index.md` - look up the subsystem name the
   architecture gave you. Take the section name and range.
3. `system_docs/src_components.md` - **slice** that section. It gives you the
   component's responsibilities, owned state, and its `Key Files (C1)`.
4. `system_docs/src_graph_index.md` - look up the node names the component named.
5. `system_docs/src_graph.md` - **slice** those nodes for wiring: ownership,
   creation, publication, validation, borrowing, callers.
6. **The code.** Open the files the graph just handed you and read them.

**Step 6 is not optional and it is where the chain usually breaks.** Steps 1-5 are
a lookup service whose entire output is a shortlist of files. An agent that stops
at step 3 or 5 has produced a *location*, then described behaviour it never
observed - fluently, because the documents are well written, and wrongly whenever
the code has moved since they were.

Two specific stops to refuse:
- **Stopping at the documents.** The component map says what a component owns; it
  does not say what the method you are about to change currently does.
- **Substituting search for step 6.** A `grep`/`rg` hit is step 5's job - it
  narrows. It is not a read. See "A SEARCH HIT IS NOT A READ" in
  `agent_onboarding/default/general/skills/unknowns_gate_reference.md`.

You have completed step 6 when you could describe the function's contract without
looking at any document: what it takes, what it returns, what it mutates, what it
locks, and how it fails.

**Why this warning exists at all, and why it grows as the documents improve.**
This is not a shortcut agents take because they are lazy. It is the direct
consequence of the system documents being good. A weak component map gets ignored;
a strong one answers so fluently that opening the source starts to feel redundant -
and the better the maps get, the stronger that pull becomes. The hierarchy above
was built to make lookup cheap, and cheap lookup is exactly what makes stopping
early tempting.

So treat the quality of these documents as a hazard as well as an asset. They are
accurate about the day they were written and silent about every commit since. The
moment a document feels like enough, that is the moment you owe the code a read.

**This is not an argument for using them less.** Read them more, and slice them
often - `src_architecture.md`, `src_components.md` and `src_graph.md` are the
fastest route from "somewhere in this repository" to four files worth opening, and
an agent that skips them searches blind and burns its context finding what an index
would have handed over in one lookup. The rule is about what each thing DECIDES:

| the documents | the code |
| --- | --- |
| tell you WHERE to look, and WHY the design is shaped that way | tells you WHAT it does today |
| are how you navigate, scope, and avoid sprawl | is the only thing that settles a behaviour question |
| are evidence of intent | is evidence of behaviour |

Use them for everything in the left column, freely. Never let the left column
answer a question in the right one - and changing an implementation is always a
question in the right one.

Every step is a lookup keyed on a name the previous step produced. That is why the
order matters: enter at the graph with no name in hand and you are searching tens of
thousands of lines for something you cannot yet describe.

The index is the ENTRY POINT to a large document, not a fallback for when something
goes wrong. `src_components.md` and `src_graph.md` are never read whole - they are
sliced through their indexes, every time. See
`agent_onboarding/default/engineer/skills/src_graph_usage.md`.
- For system-impacting changes, apply the mandatory gate in
  `agent_onboarding/default/engineer/skills/patch_framework_gating.md` before
  implementation.
- For patch-lane work, follow
  `agent_onboarding/default/engineer/skills/patch_artifact_consumption.md`
  before code edits.
- Review `attention_board.md` first, then open the linked active ticket(s) for current intent.
- **Read the code you are about to change.** Always. The documents told you which
  file; they did not tell you what that file does today.
- If a document and the source disagree, the source wins and the document is stale.
  Record the contradiction - it is a finding, not a detail to smooth over - and fix
  or file it.

Rules
- Always prefer documented context over assumptions. Prefer the source over both.
- **The hierarchy has a floor, and the floor is the code.** Descending it partway
  and stopping is worse than not using it, because you arrive at a confident answer
  with a citation attached. If you cite a document for a behaviour claim, or cite a
  one-line search hit for anything, you have not finished.
- Treat UNKNOWN as default until evidence is attached. A document is evidence of
  intent; only the source is evidence of behaviour.
- Keep architecture/components docs in sync with actual boundaries.
- Read `src_components.md` and `src_graph.md` by slice through their indexes. Never
  whole. That is a rule about HOW, not WHETHER - slice them freely and often.
- Read what the task needs and no more. These documents scale with the repository;
  loading all of them is not thoroughness, it is a spent context budget. See
  `agent_onboarding/default/general/skills/context_window_budget.md`.
- Block implementation when patch-framework entry-gate artifacts are missing for
  system-impacting work.
- If a doc is missing, create it before implementing related changes.

Precedence
- This protocol and `agent_onboarding/default/engineer/SKILLS.MD` define how system
  documents are read. **A workflow does not get to override it.** A workflow may say
  which documents a lane cares about; it may not instruct you to read a large
  document whole, to skip an index, or to treat the raw document as the primary
  surface. If one does, follow the hierarchy and say the workflow is stale.

Examples
- `agent_onboarding/default/general/README.md`

