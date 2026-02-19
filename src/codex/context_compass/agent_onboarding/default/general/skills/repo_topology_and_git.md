

# repo_topology_and_git

Purpose
- Define the standard repo layout for this project.
- Set expectations for git handling (read-only unless explicitly requested).

Repository layout
- Repo root is the project root (this checkout).
- Primary code lives under `src/` and tests under `tests/`.
- Planning and onboarding live under `agent_onboarding/`, `tickets/epics/`, `tickets/stories/`,
  `tickets/tasks/`, `templates/`, plus per-type archives in `tickets/epics/completed/`,
  `tickets/stories/completed/`, and `tickets/tasks/completed/` (legacy `completed/` remains).

Git handling (non-negotiable)
- Git commands are allowed **only** when the user declares the session is `active` during certification.
- If the user declares `inactive`, do not run git commands and ignore git workflow requirements (user handles git).
- Certification must include the exact token `CERTIFY: APPROVED` and an explicit environment label (`active` or `inactive`).
- Do not edit `.git/config`, hooks, or `.gitattributes` unless explicitly requested.
- Do not assume git is available; if missing, report it and proceed without git metadata.

Branching workflow (active-only)
- Start work on `codex_features`.
- After acceptance of a completed ticket: switch to `dev`, merge `codex_features` into `dev`, then switch back to `codex_features`.
- Stay on `codex_features` between work units.

References
- `README.md`
- `AGENTS.MD`


