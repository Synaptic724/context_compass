
# context_gold

Purpose
- Treat durable context as the highest priority for this repo.
- Prevent policy drift by forcing state into repository files, not chat memory.

Re-entry ritual (required)
- After context compaction OR a fresh session:
  1) Re-open `attention_board.md`.
  2) Re-open the active ticket(s) referenced there.
  3) Re-onboard/Onboard per `agent_onboarding/default/general/skills/compaction_requirements.md`.
  4) Re-read the orientation set: `system_docs/src_architecture.md` plus
     `src_architecture_index.md` and `src_components_index.md`. Compaction is
     when you lose the shape of the system, so this is the wrong place to skimp -
     and it is the narrative plus two maps, not the whole corpus.
     - `src_components.md` and `src_graph.md` are NOT re-read in bulk. You hold
       their indexes; slice them during the work, on your own initiative,
       whenever a question needs them.
     - DO NOT force-read `system_docs/*` as a box-check, and equally do not skip
       a read because nobody asked. Read what the question needs; stop there.

Behavior
- Update "Context / Handoff Summary" and `## Notes` in active tickets as you learn things.
- Keep documentation grounded in source evidence.
- Do not handwave; record UNKNOWNs and the next verification step.
- Do NOT claim you "retained" context after compaction; re-open the file instead.

References
- `agent_onboarding/default/general/skills/context_compaction.md`
- `agent_onboarding/default/general/skills/compaction_requirements.md`
