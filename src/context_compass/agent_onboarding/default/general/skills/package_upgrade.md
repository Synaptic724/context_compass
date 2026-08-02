# package_upgrade

Purpose
- Take an existing `context_compass/` folder and bring it up to a newer version
  of the package without destroying the project's work.
- Give you enough of the algorithm to reimplement it if Python is unavailable.

This is the general-audience skill. `engineer/skills/package_maintenance.md`
covers cleanup, release preparation, and the manifest generator in more depth.

## The shape of the operation

```bash
python context_compass/tools/update_context_compass.py \
    --install path/to/your-repo/context_compass \
    --new     path/to/new/context_compass \
    --check
```

- `--install` is **yours**. It is modified in place.
- `--new` is **read-only**. Nothing is ever written to it, so ten repositories
  can point at the same downloaded copy.
- `--check` prints the plan and writes nothing. Run it first, every time.
- `--apply` performs it.

The direction is one-way. It never pushes your changes back upstream. If you
improved a default role locally and want it in the package, that is a manual
copy.

## What decides each file

`MANIFEST.md` in your install records the sha256 of every file **as it shipped**.
Three hashes, four outcomes:

| current vs shipped | new vs shipped | verdict |
| --- | --- | --- |
| same | changed | replace - the package moved, you did not |
| same | same | skip - already current |
| changed | same | **keep yours** - you moved, the package did not |
| changed | changed | **conflict** - reported, not touched |

One hash tells you a file changed. It cannot tell you WHO changed it, and that
is the only question that decides whether overwriting is safe. Conflicts are
never merged automatically; a merge is a guess and a wrong guess destroys work
silently. Resolve by hand, or pass `--force-conflicts` to take the package
version and lose the local edit knowingly.

## What is never touched

| lane | why |
| --- | --- |
| `system_docs/` | your architecture, component and test maps |
| `tickets/` | your work |
| `artifacts/` | your findings |
| `context_management/` | your context board |
| `special_instructions/` | your project rules |
| `agent_onboarding/user_defined/` | your role overlays |

An upgrade that rewrites someone's architecture map is not an upgrade.

Two lanes get partial handling:

- **the boards** carry a package-owned block between `<!-- BEGIN MANAGED: ... -->`
  and `<!-- END MANAGED: ... -->`. Only that block is swapped; your routing rows
  below it survive.
- **`config/context_compass_config.yaml`** is merged key by key. New top-level
  keys arrive with package defaults and their comments; a value you already set
  is never overwritten; keys dropped upstream are reported, not deleted.

## First upgrade of an older install

An install predating the manifest has no shipped hashes, so a local edit and an
upstream change are indistinguishable. The tool does not guess: it reports
**every** differing file as a conflict, still skips identical files, and still
adds new ones. Review, then `--force-conflicts` if you want the package version.
Either way it writes the manifest, so this happens exactly once.

## If Python is not available

The tools are stdlib-only Python, but nothing about the algorithm requires
Python. Reimplement it in PowerShell, bash, or whatever the environment has.
**Do not skip the three-hash rule to make the port easier** - a port that
compares only current-vs-new will silently overwrite local edits, which is worse
than no tool.

What a port must do:

1. **Parse `MANIFEST.md`.** Rows under `## Files` are
   `| path | class | sha256 |`. Read both manifests: the install's (shipped) and
   the new version's (incoming).
2. **Skip by class.** `RESET` and `INSTANCE` are never touched. `CONFIG` is
   merged, never replaced. `LIVE` gets only its `MANAGED` block swapped.
3. **For every `PACKAGE` file**, hash the install's copy and apply the table
   above. Report conflicts; do not resolve them.
4. **Copy new files** the install does not have.
5. **Report files dropped upstream** that are still present locally. Do not
   delete them - the package no longer ships it, which is not the same as the
   project not wanting it.
6. **Write the new manifest** into the install, last.

Minimum viable shell version, in outline:

```bash
# sha256 of a file, portable enough
sha() { sha256sum "$1" 2>/dev/null | cut -d' ' -f1 || shasum -a 256 "$1" | cut -d' ' -f1; }

# read "path class sha" triples out of a manifest
rows() { grep '^| `' "$1" | tr -d '`' | awk -F'|' '{print $2, $3, $4}'; }
```

```powershell
function Get-Sha { param($p) (Get-FileHash -Algorithm SHA256 $p).Hash.ToLower() }
```

Then implement the table. It is a dozen lines of branching, not a project.

**Verify the port before trusting it** by constructing the four cases
deliberately: a file only the package changed, a file only you changed, a file
both changed, and an identical file. If your port does not keep the second and
refuse the third, it is not finished.

## Anti-patterns

- Running `--apply` without reading a `--check` plan first.
- Comparing current against new only, with no shipped hash. That is the
  single-hash trap: it cannot see the difference between your edit and an
  upstream change, so it either clobbers you or never updates.
- Auto-resolving conflicts by taking the newer file.
- Upgrading `--new` by accident. It is the source, not the target.
- Forgetting the release step: a package published without running
  `tools/package_manifest.py` has no manifest, and nothing can upgrade from it.

References
- `agent_onboarding/default/engineer/skills/package_maintenance.md`
- `agent_onboarding/default/general/skills/configuration_standards.md`
