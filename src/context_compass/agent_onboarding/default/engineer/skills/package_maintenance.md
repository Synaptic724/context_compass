# package_maintenance

Purpose
- Define how to clean an install back to shipping state and how to upgrade one
  to a newer version of the package without destroying local work.

When this applies
- You are preparing the package for distribution.
- One project's content has ended up inside another install.
- A newer version of Context Compass needs to be rolled into an existing repo.

This is not the ticket cleanup workflow. `agent_onboarding/default/general/workflows/cleanup_context_compass.md`
closes tickets and syncs boards. The tools here delete and replace files.

## The manifest is the contract

`MANIFEST.md` records, for every file the package ships: its path, its ownership
class, and its sha256. It is generated, never hand-edited - a hand-maintained
version stamp drifts the moment someone forgets to bump it, and a stamp that
lies looks exactly like one that does not.

```bash
python context_compass/tools/package_manifest.py --root context_compass --version 2.1.0
python context_compass/tools/package_manifest.py --root context_compass --check
```

Regenerate it in the same pass as any change to package files. `--check` reports
added, removed and changed paths without writing.

## Ownership classes

| class | who owns it | cleanup | update |
| --- | --- | --- | --- |
| `PACKAGE` | the library | restore | replace |
| `RESET` | the project (tickets, artifacts, system docs, project instructions) | reset mode only | never touched |
| `INSTANCE` | the project (`agent_onboarding/user_defined/`) | never touched | never touched |
| `LIVE` | shared: package block + project rows | block reset | block swapped |
| `CONFIG` | shared: package schema + project values | left alone | keys merged |

Class is assigned by longest path prefix, so a `PACKAGE` directory can still hold
a `RESET` subtree. That is not hypothetical - a real cleanup found five foreign
scripts sitting inside `tools/`, which is package-owned.

## Cleaning an install

```bash
python context_compass/tools/cleanup_context_compass.py \
    --target  path/to/install/context_compass \
    --reference path/to/clean/context_compass \
    --mode repair --check
```

Two modes, because "clean" means two different things:

- **`--mode repair`** fixes a broken install and leaves the project's work alone.
  Use this on a live repository.
- **`--mode reset`** returns the working lanes to shipping state. Use this when
  preparing a release or stripping one project's content out.

Reset empties `system_docs/`, `tickets/` and `artifacts/`. On a live repository
that deletes the architecture maps, tickets and findings the project wrote.
**Run `--check` first, every time.** The tool refuses to act without `--apply`.

`system_docs/` ships EMPTY - the package seeds no architecture, component, test
or graph document, because a placeholder in a live lane gets read as repository
truth. `examples/` is the shape reference. Neither tool ever writes into
`system_docs/` or `agent_onboarding/user_defined/`.

### Cutting a release from a working install

`--mode reset` clears the working lanes but deliberately leaves role overlays
under `agent_onboarding/user_defined/` alone, because they belong to whoever
wrote them. A release should not ship them either, so there is one explicit
opt-in:

```bash
python context_compass/tools/cleanup_context_compass.py \
    --target ./release/context_compass --reference ./context_compass \
    --mode reset --purge-user-defined --check
```

`--purge-user-defined` is never implied by `--mode reset`. Deleting someone's
role because they asked to tidy a lane would break the invariant the class
exists to protect, so it has to be asked for by name. Without the flag the tool
still tells you which overlays it found and which roles they belong to.

### Config drift

Config is never rewritten by cleanup. When its manifest hash does not match, the
tool reports which top-level keys you added, removed, or retuned against the
shipped defaults:

```
config    your `config/context_compass_config.yaml` differs from stock:
            keys you added:      our_own_section
            values you changed:  system_of_record, workflow
```

That is the answer to "how does mine differ from stock", and it is why the
manifest bothers to record a hash for a file it never enforces. A hash nothing
checks is the same dead weight as a version stamp nothing bumps.

Order of operations inside the tool matters and is deliberate: remove foreign
files, prune directories that are now empty, then re-materialise every manifest
path. Pruning last leaves stale empty directories; pruning without the final
restore loses lanes whose only content was a `.gitkeep`.

## Upgrading an install

```bash
python context_compass/tools/update_context_compass.py \
    --install path/to/install/context_compass \
    --new     path/to/new/context_compass \
    --check
```

The decision is made from three hashes, not one:

| current vs shipped | new vs shipped | verdict |
| --- | --- | --- |
| same | changed | replace |
| same | same | skip |
| changed | same | keep the local edit |
| changed | changed | **conflict** - reported, not touched |

One hash tells you a file changed. It cannot tell you who changed it, and that is
the only thing that decides whether overwriting is safe. Without the shipped hash
from the install's own manifest, rows three and four are indistinguishable from
row one, so you either clobber local edits or never update anything.

Conflicts are never merged automatically. A merge is a guess, and a wrong guess
destroys work quietly. Resolve them by hand, or pass `--force-conflicts` to take
the new version and lose the local edit knowingly.

### Upgrading an install that predates the manifest

An older install has no `MANIFEST.md`, so there are no shipped hashes and a local
edit is indistinguishable from an upstream change. The tool does not guess. It
reports **every** differing file as a conflict, still skips files that match, and
still adds new ones:

```
NOTE: <install> has no MANIFEST.md, so this is its first manifest-aware upgrade.
  replace   0
  skip    331   already current
  conflict  3   BOTH changed - not touched
```

Review the conflicts, then re-run with `--force-conflicts` to take the package
version wholesale. Either way the upgrade writes the new manifest, so the next
upgrade is a normal three-hash comparison and this only happens once.

Project-owned lanes are untouched throughout: `system_docs/`, `tickets/`,
`artifacts/` and `user_defined/` survive a forced upgrade intact.

## Live files and managed blocks

The boards carry a package-owned directive above project-owned rows. The package
region is delimited:

```markdown
<!-- BEGIN MANAGED: ReminderDirective -->
...package text, replaced wholesale on upgrade...
<!-- END MANAGED: ReminderDirective -->
```

Only that region is swapped. Routing rows survive an upgrade. This is the same
marker convention as patch document `ENTRY` markers, deliberately - one dialect,
one parser. Malformed or unterminated markers refuse the operation rather than
guessing where the boundary was.

## Config

Merged key by key, never swapped wholesale. New top-level keys arrive with their
package defaults and their explanatory comments; a value already set is never
overwritten; keys dropped upstream are reported rather than deleted.

The merge is deliberately not a YAML round-trip. Parsing and re-emitting would
reformat the file and drop the user's comments, which is a worse outcome than
leaving a key unmerged and saying so.

## Anti-patterns

- Running `--mode reset` on a live repository without `--check` first.
- Comparing paths instead of content. A path-only diff reports a tree as correct
  while another project's boards and system documents sit at package paths.
- Hand-editing `MANIFEST.md`.
- Treating a conflict as something to resolve by picking the newer file.
- Upgrading without regenerating the manifest afterwards, which leaves the
  install claiming a version it is not.

References
- `agent_onboarding/default/general/workflows/cleanup_context_compass.md` (ticket
  cleanup, a different operation with a similar name)
- `agent_onboarding/default/engineer/skills/staleness_protocol.md`
