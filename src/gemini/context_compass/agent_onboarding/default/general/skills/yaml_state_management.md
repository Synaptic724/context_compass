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
3. **The Synchronization Event**: ONLY when that threshold is breached, do you open the YAML file and perform a batch synchronization:
   - You sync `step.current` to exactly match your current injected `Step Id`.
   - You trigger the `COMPACTION_EVENT` (e.g., setting `pending_reonboard: true`).

## Field Definitions

### `step` Block
- `current`: A lazy snapshot of the system step. **DO NOT increment this during normal work.** Only update this when a compaction event is triggered.
- `reonboard_interval`: The configured maximum length of the memory window (e.g., 400 steps).
- `next_reonboard_step`: The targeted step where the next compaction event MUST occur. Calculated during re-onboarding as `current + reonboard_interval`.

### `compaction` Block
- `mode`: The strategy used (e.g., `sliding_window`).
- `pending_reonboard`: A boolean lock. When `true`, all tactical work must stop until the agent completes the strict re-onboarding ritual defined in `compaction_requirements.md`.
- `last_compaction_step`: The step at which the last successful compaction summary was written.

### `onboarding` / `reonboarding` Blocks
These blocks are **Historical Snapshots**, not active trackers.
- `last`: A record of exactly when and who completed the last ritual.
- `next`: The "Alarm Clock" setting. `due_step` records the target calculated *at the completion of the last ritual*. It holds this value statically until the alarm goes off.

### `transient_role` Block
- If a temporary role was assumed (e.g., a specific engineering persona), this block tracks when it expires. If `expires_step` is reached, the agent must drop the role. If `clear_on_reonboard` is true, the role is wiped during the next compaction event.
