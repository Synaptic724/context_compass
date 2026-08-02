

# context_protocol

Purpose
- Make the system documents the primary way you NAVIGATE: they turn "somewhere in
  this repository" into a short list of files worth opening.
- Keep the code authoritative for what the system actually DOES. The documents
  describe intent as of the moment somebody wrote it down; the code is what runs.

When to use
- Before any code edits, investigations, or architectural changes.

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

