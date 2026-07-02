# context_management

Purpose
- Hold optional derived context packs that tickets can link when reread
  bundles are useful.

Structure
- `context_board.md`
  - index of active ticket -> context artifact links
- `artifacts/`
  - derived context documents
- `context_artifact_template.md`
  - schema for creating a new context artifact

Rules
- This system is optional.
- Tickets opt into it through their `Context Management` section.
- Tickets should reference `Context ID` values from `context_board.md`.
- When a required context field is unknown, write `UNKNOWN` explicitly.
- `attention_board.md` remains ticket-only and never stores context artifact
  paths.
