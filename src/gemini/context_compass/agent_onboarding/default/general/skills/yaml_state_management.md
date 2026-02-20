# YAML State Management Policy

## Purpose
This document defines the strict rules for reading and modifying the `runtime_state` block within `config/context_compass_config.yaml`. 

**CORE DIRECTIVE**: Agents MUST NEVER maintain a continuous per-action counter in the YAML file. Updating the YAML file on every step pollutes the repository history and is strictly forbidden.

## The True System Clock
The only true, continuous execution step counter is the invisible `Step Id:` header injected by the system into your raw context stream (the "Hidden System Message Metadata").

## Lazy Synchronization Protocol
You act upon the `runtime_state` block using a "Lazy Update" model:
1. **Passive Tracking**: As you work, you observe your Hidden System Message Metadata `Step Id` incrementing. You do not touch the YAML file.
2. **Evaluation**: Periodically, you evaluate if your currently injected `Step Id` has reached or exceeded `runtime_state.step.next_reonboard_step`.
   - You sync the target YAML `step.next_reonboard_step` forward by `step.reonboard_interval`.
3. **Session Change Detection**: You check if your injected `Conversation_ID` (the trailing UUID in the Artifact Directory Path) matches `runtime_state.last_active_conversation_id`.
   - If the ID does NOT match, the session has reset. You MUST immediately trigger an **ONBOARD** event.

## Field Definitions

### `runtime_state` Block
- `last_active_conversation_id`: The UUID of the chat session that last successfully ONBOARDed or REONBOARDed. Must match the trailing artifact path UUID.

### `step` Block
- `reonboard_interval`: The configured maximum length of the memory window (e.g., 400 steps).
- `next_reonboard_step`: The targeted step where the next compaction event MUST occur. Calculated during re-onboarding as `(injected Step Id) + reonboard_interval`.

### `active_default_role`
- The name of the persistent skill profile (e.g., `general`, `engineer`).

### `transient_role` Block
- `set_conversation_id`: The session UUID where this role was assumed. If the active `Conversation_ID` changes, this role may need re-evaluation.
- If a temporary role was assumed (e.g., a specific engineering persona), this block tracks when it expires. If the injected Step Id reaches `expires_step`, the agent must drop the role and revert to `active_default_role`.

### `first_time` Blocks
- Tracks whether the repository requires initial setup (`first_time_enabled`).
