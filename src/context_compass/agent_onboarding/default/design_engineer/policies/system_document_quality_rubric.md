

# system_document_quality_rubric

Purpose
- Score the four system documents on whether they *say* anything, not merely
  whether their required fields exist.
- Give downstream work a threshold it can refuse on.

Scope
- Applies to `system_docs/src_architecture.md`, `src_components.md`,
  `tests_architecture.md`, and `tests_components.md`, whenever one is created,
  recomposed, or reviewed.
- One rubric, four profiles. The criteria and weights below are shared; only the
  anchors change per document. Two rubric idioms in one repository drift apart,
  and then neither is trusted.
- Vocabulary is deliberately the same as
  `agent_onboarding/default/engineer/policies/ctx_autonomy_rubric.md`: weighted
  criteria, 0/3/5 anchors, 0-100 bands, a refusal threshold. Learn it once.

## The hole this fills

Every other gate in this system is binary. The Quality Gate asks whether
`Concurrency/Threading` is present. It is present, so the gate passes:

> Concurrency/Threading: Uses a lock.

That scores identically to:

> Concurrency/Threading: Single writer lock held across the flush; readers take
> the snapshot instead. Acquired before the queue lock, never after - the
> reverse order deadlocked under concurrent flush and drain.

Both satisfy the contract. Only one is worth reading. Structural gates verify a
field exists; nothing until now verified it carries information. That gap is the
difference between a document that satisfies a contract and one a reader can act
on after compaction.

This rubric does not replace the Quality Gate or the Content Preservation Gate.
Those are pass/fail and come first. A document that fails either is not scored -
it is fixed.

## Ranking model (0-100)

Score each criterion 0-5, then compute `sum((score / 5) * weight)`.

| criterion | weight |
| --- | --- |
| Fidelity to source | 30 |
| Contract completeness | 15 |
| Depth | 15 |
| Addressability | 15 |
| Join integrity | 15 |
| Mirror agreement | 10 |

Fidelity carries double weight because every other criterion is recoverable by
editing. A confidently wrong claim is not - it propagates into decisions before
anyone tests it.

## Shared anchors (0/3/5)

**Fidelity to source**
- 5: every non-obvious claim carries a file or symbol reference a reader can
  open. Claims match what is there.
- 3: mostly accurate; some claims plausible but uncited.
- 0: claims contradicted by the sources, or inferred from names alone. Naming
  inference is the specific failure - `*_manager` does not establish that a
  thing manages anything.

**Contract completeness**
- 5: every required section and field present, in contract order, and each one
  populated with content specific to this subject.
- 3: all present, one or more hollow - a field restating its own name.
- 0: required sections missing, or reordered so a reader cannot navigate by
  contract.

Scoring note: a field deliberately marked not-applicable, with the reason, is a
5. A field left blank is a 0. They look identical to a reader, and only one of
them is a decision.

**Depth**
- 5: names the mechanism, the ordering it depends on, and the failure it
  prevents. Testable as written.
- 3: correct but one clause; a reader knows *that* something happens, not how or
  why it must.
- 0: aspirational or decorative. "Handles errors gracefully."

**Addressability**
- 5: exactly one H1; navigable units at consistent depth; every section name
  unique; no wrapped headings; no container heading usable as a read target.
- 3: unique and unwrapped, but a container heading exists that a reader could
  select by mistake.
- 0: duplicate section names, or a heading spanning two physical lines. Both
  return content on a slice - the wrong content, confidently.

**Join integrity**
- 5: every cited path resolves, and every range was measured on this pass.
- 3: paths resolve; ranges carried forward from a previous pass without
  remeasuring.
- 0: unresolvable citations, a stale index, or ranges that parse and point
  somewhere else.

The join differs by side and the difference is not cosmetic - see the profiles.

**Mirror agreement**
- 5: the document pairs with its counterpart - same section contract shape, same
  terms for the same things, no boundary described one way here and another way
  there.
- 3: structurally aligned, terminology drifted.
- 0: the pair contradict each other, or one is current and the other describes a
  boundary that moved.

`system_document_build.md` already declares these are mirrors and that
divergence *is* the defect. That makes this scoreable in both directions: when a
pair disagree, both documents lose the points, because the rubric cannot tell
which one is wrong and neither can a reader.

## Score bands

- 90-100: A - trusted as an input to design decisions
- 75-89: B - usable
- 60-74: C - usable, schedule a refresh before high-risk work
- 40-59: D - weak
- 0-39: F - unusable

Actions:
- **< 60: refuse downstream work that depends on this document.** Refresh it
  first. Do not synthesize a higher-level claim from it, and do not cite it as
  evidence in a ticket.
- 60-74: proceed if necessary, and record the score and the weak criterion in
  the active ticket so the next reader inherits the caveat rather than the
  false confidence.
- 75+: proceed.

## Profiles

### src_architecture

- **Navigable unit**: the H2 concern.
- **Depth** means boundaries, invariants and failure paths stated concretely
  enough to test. A boundary claim scores 5 when a reader can name what crosses
  it and what is refused.
- **Join integrity** is the C1 map: cited paths resolve into the graph index,
  ranges measured.
- **Mirror**: pairs with `tests_architecture.md`.

### src_components

- **Navigable unit**: the H3 component entry.
- **Depth is assessed per entry across the twelve fields**, then averaged - not
  judged from the document as a whole. One excellent entry does not lift eleven
  hollow ones, and a document-level impression is exactly how hollow entries
  survive review.
- **Join integrity** is `Key Files (C1)`, verified with the recipe in
  `src_components_instructions.md`, not assumed.
- **Mirror**: pairs with `tests_components.md`.

### tests_architecture

Mirror of the source architecture profile, plus one criterion that overrides
Fidelity when it fails:

- **Does it describe the test system's own boundaries, layers and harness
  ownership** - or does it restate source architecture in test vocabulary? A
  document whose diagram could be dropped into `src_architecture.md` unchanged
  is describing the wrong system, and scores 0 on Fidelity regardless of how
  accurate its sentences are. It is accurate about the wrong subject.

- **Join integrity is weaker here, and knowing that is the point.** The graph is
  built from the source tree, so source-side citations are checked against
  `src_graph_index.md` for free. This document cites test paths, which appear in
  no graph. Nothing will tell you a path here has rotted. Score 5 only when
  existence was checked and ranges were remeasured on this pass; carried-forward
  ranges cap this criterion at 3.

### tests_components

Mirror of the source components profile, plus:

- **Does each test surface name what it validates and who owns it?** An entry
  that describes a harness without naming the behaviour it protects scores at
  most 3 on Depth. "Runs the suite" is not a responsibility.
- **`Key Files (C1)` cites test paths**, and the join is existence plus
  remeasurement, per `tests_components_instructions.md`.

## Weight the test side equally, and expect it to score lower

The test profiles carry the same weights as the source profiles. Not because the
two halves are equally mature - they are usually not - but because weighting the
test side lower encodes the neglect instead of measuring it.

Expect lower scores at first. In the repository this rubric was developed
against, both source indexes had been maintained and both test indexes were
stale. That asymmetry is the normal case: the test-side documents are written
once, during a push, and then nothing forces them forward, because no build
breaks when they rot.

A rubric that scores all four surfaces makes that visible on every pass rather
than letting it sit. The first run against an established repository should be
read as a baseline, not an indictment - what matters is the second run.

## Scoring discipline

- **Score against the document, not your memory of building it.** Re-read it.
- **Cite what you scored.** A criterion scored below 5 needs a `path:line`
  example of the weakness, otherwise the score is unactionable and the next
  reader re-derives it from scratch.
- **Score the whole document once, not each section separately**, except where a
  profile says otherwise - the components profiles average per entry precisely
  because whole-document impressions hide hollow entries.
- **Do not score your own work as the last step of building it.** The build pass
  and the scoring pass want opposite postures. If the same agent must do both,
  score from the file on disk after the index rebuild, never from the draft in
  context.
- Record the total, the per-criterion scores, and the band in the active ticket.
  A score with no record is a score nobody can challenge.

## Anti-patterns (reject)

- Scoring 5 on Fidelity because nothing looked wrong. Absence of a caught error
  is not evidence of accuracy.
- Rounding a document up to clear the 60 threshold so work can continue. The
  threshold exists to stop exactly that.
- Treating a high Contract completeness score as a proxy for quality. It is 15
  points of 100, and it is the one criterion a structural gate already covers.
- Averaging the four documents into a single repository score. They are read
  separately, they rot separately, and a strong source half will mask a
  worthless test half.

## References
- `agent_onboarding/default/engineer/policies/ctx_autonomy_rubric.md`
- `agent_onboarding/default/engineer/skills/system_document_build.md`
- `agent_onboarding/default/design_engineer/skills/src_architecture_instructions.md`
- `agent_onboarding/default/design_engineer/skills/src_components_instructions.md`
- `agent_onboarding/default/design_engineer/skills/tests_architecture_instructions.md`
- `agent_onboarding/default/design_engineer/skills/tests_components_instructions.md`
