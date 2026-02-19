

# Artifacts Store

Purpose
- Canonical storage root for ticket-linked supporting artifacts.
- Hold transient evidence snapshots, reports, and generated support files.
- Keep durable execution memory in tickets; artifacts support tickets.

Canonical protocol
- Artifact associations are indexed in `context_compass/artifact_board.md`.
- `attention_board.md` remains ticket-routing-only and does not carry artifact
  pointers.
- If a ticket has artifacts, the ticket must include an `Artifact Links`
  section with artifact paths and disposition.

Storage contract
- Root: `context_compass/artifacts/`
- Naming: use date-first filenames with descriptive slugs.
- Preferred pattern: `YYYY-MM-DD_<slug>.<ext>`
- Every artifact must map to exactly one active ticket path.

Lifecycle contract
- Default disposition is `delete_on_close`.
- Allowed dispositions:
  - `delete_on_close`
  - `retain_as_reference`
  - `promote_to_documentation`
- Ticket closure must record artifact disposition and reason.
- Retained artifacts must keep ticket linkage and explicit retention rationale.

Security
- Never store secrets in artifacts.
- Mask or omit credentials and private material in captured outputs.

Historical note
- Archived/completed tickets may still reference removed historical artifacts.
- Those links remain historical context and do not define current protocol.



