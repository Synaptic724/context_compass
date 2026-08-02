# Special Instructions

Purpose
- Users can place project-specific instruction documents in this folder.
- Agents must read and follow every Markdown document in `context_compass/special_instructions/`.

Rules
- Use relative repo paths only.
- Keep project-specific instructions here instead of embedding them directly in `AGENTS.MD` when possible.

Registration
- Documents here are picked up by a directory sweep, not by a named entry in a
  `SKILLS.MD` readset. Adding a file here is enough; nothing needs to be
  registered, and an unreferenced file in this folder is not an orphan.
- That is deliberate: project instructions are the user's to add, and requiring
  a registry edit would make the package own something it should not.
