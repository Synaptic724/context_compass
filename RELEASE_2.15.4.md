# Context Compass 2.15.4

A behaviour release. The headline change fixes a regression this package caused in
2.15.0: agents stopped reading source and started reasoning from `grep` and AST
output. Everything else here is either the cause of that, or something found while
chasing it.

32 files changed since 2.15.0 — 29 modified, 3 added.

---

## The regression, and what caused it

Agents onboarded into this package began substituting search results for reading
code. They would locate a symbol, cite the line it matched on, and describe
behaviour they had never opened the file to observe.

The cause was ours. Release 2.15.0 added a 212-line block to
`engineer/SKILLS.MD` teaching document-slicing discipline, and its whole register
was that reading is expensive:

> *"Reading everything is not diligence, it is a context budget spent before the
> work starts. Be surgical."*
> *"~8,400 for components and ~25,000 for the graph"*

All of it aimed at the large system documents. **None of it scoped to them.** The
hierarchy then ended at *"6. The code"* — the only step with no procedure attached,
sitting after five that had one. An agent that has absorbed "never whole, be
surgical, 25,000 lines" and then meets a source file does the surgical thing.
`grep` is a procedure. "Read it" was not.

Three further carriers were found, each of which made the same trade
independently:

- **`context_window_budget.md`** — a `general` baseline skill every role loads. It
  was pure read-restriction with no counterweight, and it named *"reading … large
  code trees"* as an anti-pattern. It pointed at `expansion_gate_max_files: 5`,
  which reads as *stop and ask permission after five files*. Reading a class plus
  its collaborators and tests exceeds that immediately — and **searching does not
  count as opening files.** The config actively rewarded grep.

- **The note cadence.** The microcycle said *investigate until ONE finding → stop →
  write the note → only then continue*. Reading a 400-line class produces several
  findings, so the loop forces the read to fragment. Search produces exactly one
  discrete finding at a time. **The cadence fit grep better than it fit reading.**

- **The four `*_instructions.md` authoring docs.** 39 shell verification recipes
  between them, and zero instructions to read source — in the documents that teach
  you how to write descriptions of code.

## What changed

**`engineer/SKILLS.MD`** — the hierarchy is now stated as a priority order rather
than a rationing scheme:

1. `src_architecture.md` — read it. This is what the system IS.
2. `src_components.md` — before starting on a topic, read the relevant parts.
3. `src_graph.md` — if you are going to write code, read the wiring.
4. **THE CODE** — if you are changing anything, read it. Always. No exception.

Plus two rules that did not exist: **`grep` and AST are guesses** (they locate, they
do not explain — use them to pick where to start reading, then read and trace the
call path), and **slice the DOCUMENTS, read the CODE whole** (a source file is a few
hundred lines; budget discipline exists so you arrive at the code with room to read
it properly, not so you skip it). Every scare number removed.

**`context_window_budget.md`** — Purpose now leads with keeping discovery focused
*so there is budget left to read the thing that matters*. The expansion gate counts
**scope, not files read**. Reading one unit through is **one pass, not one per
finding** — do not stop mid-file to write a note. Using search to keep an
investigation *looking* small is listed as an anti-pattern.

**`config_compass_config.yaml`** — `expansion_gate_max_files` documented as a
wandering limit, not a reading limit.

**`technical_expertise.md`** — "trace the call path" now says what tracing is:
opening each file along it. A caller list tells you where a name appears, not
whether that site holds a lock, owns the object, or runs before cleanup.

**`context_protocol.md`** — the order in one line, and step 6 named as where the
chain usually breaks.

**`unknowns_gate_reference.md`** — evidence is now tiered. A document citation is
**not** evidence for a behaviour claim; only read source is. Previously the two were
listed as alternatives, which sanctioned every doc-only claim.

**The four authoring instruction docs** — a green recipe run means the document is
well-formed. It says nothing about whether the prose is true.

Balance across the payload moved from 14 read-less / 12 read-the-code to
**8 / 23**, and all 8 are explicitly scoped to documents.

---

## Also in this release

**Line-ending agnostic comparison.** The manifest hashed raw bytes, so a Windows
checkout of a repo vendoring `context_compass/` read as hundreds of local edits. In
one install that was **267 files**, each answered "you edited it, keep yours" — the
three-hash rule working correctly and silently freezing that install against every
future upgrade. Hashing now normalises line endings for text (binary passes through,
decided by UTF-8 decodability rather than an extension list), and writes match the
destination's existing convention so a CRLF tree is not rewritten wholesale.
Backward compatible: an LF file hashes to exactly what it did before.

**Three fixes promoted out of a consuming repo**, each found by using the tools:

- `index_document.py` — `--slice` used plain substring matching, so a section whose
  name was contained in another became unreachable. Measured: **21 of 292 sections
  unaddressable**. Now exact-path → exact-leaf → substring.
- `index_document.py` — exact matching then created a new hazard: a container
  heading resolves cleanly and returns 1,149 lines to someone who thinks they sliced
  one section. Now warns on stderr, still honours the request, keeps piped output
  clean.
- `extract_graph.py` — a file that failed to parse was dropped from the graph
  silently, exit 0. `--strict` makes that non-zero and names the skipped files.

**Four graph-generator defects**, three of which silently destroyed authored work:

- `assemble_graph.py` rendered `responsibilities` (prose) through the identifier
  path, so any responsibility naming a method closed its code span early. The better
  the prose, the worse it rendered. Repaired 177 nodes on reassembly.
- `graph_semantics_tickets.py` minted a new epic id every run, orphaning stories it
  did not rewrite — and it skips a story precisely when that story is SATISFIED. The
  failure targeted finished work.
- The same tool overwrote the epic wholesale to refresh one generated table,
  destroying Status, Owner and every authored note. Now splices only the generated
  block, and refuses rather than guessing if that block is absent.
- The no-work path returned early without refreshing, leaving a completed epic
  advertising outstanding nodes.

**Grandfathering removed.** The extractor auto-stamped unverified prose against
current source so it would report `AUTHORED` — asserting, on nobody's behalf, that
prose it never read matched code it never compared. `SEMANTICS_STALE: 0` was
reachable with zero nodes checked. A node with no stamp is now `SEMANTICS_STALE`,
because unverified is unverified, and only `--accept` creates a stamp. Expect a
large stale count on the first run against an existing graph: that is the truth
being reported for the first time.

**Apache 2.0 and trademarks.** `LICENSE` and a new `NOTICE` ship in the payload;
Section 6 excludes trademark rights from the grant, and `NOTICE` states the mark
explicitly. `.gitattributes` now ships too, so a consuming repo inherits the LF
policy for `context_compass/` only.

**README rebuilt** — 653 → 528 lines. Core Features and the Role Model restored, a
worked session walkthrough added, and a `Detailed Setup` section deleted that was
not merely redundant but *wrong*: it told readers to copy to `src/context_compass/`
and named the entrypoint as `src/context_compass/AGENTS.MD`, neither of which exists
in an install.

---

## Upgrading

Ordinary upgrade. Nothing in this release touches your lanes.

```bash
uvx contextcompass@latest upgrade --check
uvx contextcompass@latest upgrade --apply
```

Two things worth knowing:

**Behaviour changes on re-onboard, not immediately.** The doctrine is read at
session start. Anything mid-session is still running the previous text.

**`user_defined/` does not receive any of this.** It is INSTANCE-class and never
touched by an upgrade, in any mode. If your overlays restate reading discipline,
they keep their own copy and it will not be corrected. Same for guidance embedded in
config comments: `merge_config` only adds keys an install lacks and never rewrites
existing ones, so the `expansion_gate_max_files` comment reaches new installs only.

## Verifying it took

The tell is in the ticket notes. `EVIDENCE` ranges should cover whole functions
rather than single lines, and behaviour claims should cite source rather than a
document section. A one-line range under a behaviour claim is the signature of a
search hit pasted in place of a read — which is now written into the note contract,
so it shows up in the ticket rather than needing to be caught in the act.
