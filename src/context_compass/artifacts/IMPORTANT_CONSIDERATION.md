# IMPORTANT_CONSIDERATION

## Metadata
- Artifact ID: ART-2026-05-03-important-consideration
- Parent Epic: EPIC-2026-05-03-general-open-questions
- Status: active
- Created: 2026-05-03T14:53:56Z
- Updated: 2026-05-08T09:55:39Z

## Purpose
Capture one critical open investigation specifically about mutation semantics.

This artifact is intentionally narrow.
It is not a broad crystallizer philosophy file.
It exists to focus on one hard question:

- how do mutation semantics behave when spells, lineages, conduits, links,
  local spellbooks, and snapshot/load flows all interact at once?

This is not settled design.
This is a high-priority semantic pressure that must be understood before we
pretend fork/reload mechanics are obvious.

## Core Concern
The system already supports:
- dynamic conduits
- links and contracts
- ownership transfer
- mutation research sessions
- stable indexes (`SpellIndex.id`) holding one active selected spell
- concrete spell versions (`spell_id`), with history owned by MutationResearch

But mutation is still unfinished.

So the main question is not:
- "can we store some mutation metadata?"

The real question is:
- how do we keep mutation semantics coherent when agents want to work on
  alternate versions of spells across one conduit or many conduits?

## What Triggered This
The immediate design pressure is:

- an agent may want to work on version 8 while version 7 still exists
- many agents may work in the same conduit or in different conduits
- another conduit may want to "work on" a spell that is already under mutation
- the system may need forks, rebases, merges, and later reintegration

That becomes hard because:
- only the current version of a spell should really be melded
- non-active versions may still need to exist in research or snapshot state
- links currently resolve through live runtime structures that expect one
  current spell version to be authoritative
- local spellbook lookup maps and spell contracts are already sophisticated
  enough that mutation updates ripple through many surfaces

## Current Runtime Anchors
The live code already gives us some constraints.

### 1. Mutation is conduit-gated
`Conduit.get_mutation_research(...)` already says mutation research is only for:
- normal conduits
- dynamic mode

So mutation is not a generic free-floating spell feature.
It is already conduit-owned in the runtime model.

### 2. Index and concrete version are separate
The current mutation code already distinguishes:
- `SpellIndex.id`
  - stable index identity (ULID); categorizes and targets spells
- the active selected spell held by `SpellIndex`
  - the one spell currently selected through the index
- `spell_id`
  - concrete SHA256-backed spell version identity

This is the right separation. Version history is owned by MutationResearch,
not by the index.
It also means mutation semantics are already beyond simple "replace one spell in
place" thinking.

### 3. Promotion already assumes new concrete versions
The mutation code already leans toward:
- build a new `Spell`
- keep the same lineage
- advance the current head later

So the current runtime does not naturally imply:
- multiple live spell versions in one simple flat space
- or trivial cross-conduit duplication of the same active spell version

### 4. Local spellbook and contract state is highly coupled
Mutation touches more than one object.
It potentially affects:
- the active selected spell held by `SpellIndex`
- local spellbook spell maps
- spell lookup keys
- contracted spell maps
- spell-contract semantics
- descriptor publication
- validation state
- ownership stamping
- creation/runtime state

That is exactly why mutation work is expected to use transactions and locking.

## The Hard Semantic Questions

### A. What can be linked?
If a spell is not the active/current version of its lineage:
- can it be linked as a reference?
- can it be linked but intentionally not melded?
- should link resolution always collapse to the current version?

This is still open.

### B. What can be melded?
The current philosophical pressure is:
- only the current/head version should be meldable as the live default

If that is true, then:
- non-active versions may still need to exist
- but they cannot behave like ordinary active runtime spells

This means we may need explicit rules for:
- linkable-but-not-meldable
- research-visible-but-not-runtime-active
- snapshot-visible-but-not-live-default

### C. What is a fork?
There may be at least two meanings:

#### research branch
- same lineage
- alternate future
- not necessarily live and callable right now

#### runtime fork
- a real new thing an agent wants to work on elsewhere
- may need distinct addressability
- may need a new lineage

This artifact does not assume those are the same operation.

### D. When does a fork need a new lineage?
Current leaning:
- if the fork is just research/state under the same lineage and is not yet
  meant to coexist as a live callable runtime version, it may stay under the
  same lineage
- if the fork must become a separately evolvable live thing, especially in
  another conduit, it may need a new lineage

This is not finalized.

### E. What happens when another conduit wants to "work on" a spell?
This is the concrete difficulty:

- does the conduit borrow the current live version?
- does it open research against the same lineage?
- does it create a forked lineage?
- does it link the spell but prohibit meld if the spell is not current?
- does it require a mutation-fork operation that creates a new object boundary?

We do not know yet.

## Why Mutation Fork Is Attractive
There is a strong intuition that direct transfer is the wrong mental model.

Why:
- one spellbook should likely own its own local spell/index state
- moving the same active version around across conduits as if it were ordinary
  cargo is semantically weak
- mutation already wants explicit version and transaction semantics

So `mutation_fork` is attractive because it could mean:
- do not directly transfer the same live active spell object
- create a new derived object boundary for the target work context
- preserve ancestry explicitly instead of pretending there is no branch

But the current system does not yet prove that this works cleanly.

## Why We Cannot Pretend This Is Solved
We do not know whether `mutation_fork` works yet because mutation is not done.

We do not know:
- how a non-active spell should be represented in another conduit
- whether links should target current head only
- how local spellbook lookup structures behave across forked futures
- how contracted spells should behave when lineages branch
- how merge/rebase should affect bind addresses and live topology

So the right posture is:
- keep this as an investigation
- do not freeze semantics too early

## Related Runtime Hygiene Pressure
This mutation pressure is not only about lineage semantics. It also depends on
honest lifecycle boundaries across the runtime surfaces that mutation touches.

Why this matters:
- mutation work already ripples through spellbook state, contracts, ownership,
  publication, and runtime state
- if a facade or root delegates into an associated object after that associated
  object has been cleaned, the runtime can cross a boundary dishonestly
- that makes mutation behavior harder to trust because a branch/fork/reload
  discussion can get polluted by basic lifecycle drift

That is why a separate parked later-work epic now exists:
- `tickets/epics/backlog/2026-05-08_audit_facade_check_cleaned_delegation_contracts_epic.md`

The point of that parked epic is narrow:
- audit major roots/facades such as `Conduit`, `ConduitWard`, `Spellbook`,
  `Spell`, `Aether`, `Nexus`, and `Rift`
- verify delegated method chains land on callee methods that call
  `check_cleaned()` where the live-object contract requires a fail-fast
  boundary
- preserve hosted-root ownership so inner objects do not sever outer-host
  bindings during their own cleanup

The important boundary rule is:
- this is not about making outer facades pre-screen inner-object liveness
- it is about making the real delegated-to object throw from its own method
  when that object is already cleaned

Example shape:
- `Aether` can delegate honestly into `Nexus`
- if `Nexus` is cleaned, the called `Nexus` method should throw from its own
  `check_cleaned()` boundary
- `Aether` does not need to babysit that state ahead of the call

This is intentionally related but separate work:
- this artifact stays focused on mutation semantics
- the parked epic later hardens the lifecycle/delegation floor those semantics
  rely on

## Relationship To Conduit Snapshots
This investigation matters directly to conduit snapshots.

If a conduit snapshot is supposed to be a real world slice, and mutation is
present, then the snapshot likely needs to carry:
- the relevant spell/module world
- the mutation manifest / research state
- enough lineage/head information to rehydrate the mutation system honestly

That does not mean the snapshot solves branch semantics by itself.
It means the snapshot cannot ignore mutation if it claims to recreate the
world faithfully.

## Relationship To SpellCrystal
This artifact is specifically not trying to make `SpellCrystal` solve all of
mutation.

What `SpellCrystal` can reasonably do:
- provide a durable module/spell-artifact manifestation for persistence
- provide the source/dependency truth that mutation research may refer to
- help loaders reactivate the module world

What `SpellCrystal` should not absorb by itself:
- full branch/head/fork semantics
- all live spellbook/contract mutation behavior
- the entire transaction choreography of mutation

That belongs to MutationResearch and conduit/runtime semantics.

## Practical Open Rules To Decide Later

### Rule candidate 1
- only current/head version is meldable by default

### Rule candidate 2
- non-active versions may be visible to mutation and snapshot systems without
  being ordinary live runtime spells

### Rule candidate 3
- direct "work on this elsewhere" may require `mutation_fork` rather than raw
  transfer semantics

### Rule candidate 4
- if a fork becomes a separately live callable entity, it likely needs
  distinct runtime addressability and possibly a new lineage

### Rule candidate 5
- mutation operations must remain transaction-driven and heavily locked because
  updates ripple through many internal surfaces

These are not final rules.
They are the current pressure points.

## Source Anchors
- `src/melder/aether/conduit/conduit.py`
  - mutation gating and conduit-owned mutation access
- `src/melder/spellbook/mutations/mutation_research.py`
  - high-level mutation manager semantics
- `src/melder/spellbook/mutations/research/research.py`
  - lineage + root-version session model and version promotion hook
- `src/melder/spellbook/mutations/research/spell/spell_research.py`
  - spell-oriented research-line behavior
- `src/melder/spellbook/mutations/research/creation/creation_research.py`
  - creation-oriented research-line behavior
- `src/melder/spellbook/mutations/research/spell/node/spell_mutation_node.py`
  - spell mutation-node representation

## Current Best Summary
The important unresolved issue is not "how do we store mutation data?"

It is:
- how do multiple versions of one spell lineage behave across one conduit or
  many conduits,
- what is allowed to be linked,
- what is allowed to be melded,
- when do we stay within one lineage,
- and when do we create a new lineage through fork semantics?

This is still open and should stay open until mutation is more fully built.
