"""Bugs that actually happened, locked in.

Every test here corresponds to a real failure against a real repository, not a
hypothetical. The docstrings say what broke, because a regression test whose
reason is lost gets deleted by the next person who finds it inconvenient.
"""

from __future__ import annotations

import json
import shutil

import pytest

from conftest import GRAPH_TOOLS, TOOLS, run_tool, write

pytestmark = pytest.mark.regression

UPDATER = TOOLS / "update_context_compass.py"
CLEANUP = TOOLS / "cleanup_context_compass.py"
MANIFEST = TOOLS / "package_manifest.py"
INDEXER = TOOLS / "system_documents" / "index_document.py"
ASSEMBLE = GRAPH_TOOLS / "assemble_graph.py"


class TestCaseCollisionSweep:
    """It deleted a real install's role registry.

    The manifest lists `SKILLS.MD`. The install carried the same file under the
    name `SKILLS.md`, which looks retired, so the sweep unlinked it - and on a
    case-insensitive filesystem that is the same file the manifest name also
    resolves to, which the upgrade had just written the correct content into.
    The risk was flagged two messages before the sweep ran anyway.

    Constructing this needs care, and two obvious setups are both wrong:

    - Writing `skills.md` beside `SKILLS.MD` in one directory cannot exist on a
      case-insensitive filesystem. The second write overwrites the first, the
      updater sees one correctly-named file, and the test passes on Linux while
      exercising nothing on Windows. This is the guard FOR case-insensitive
      filesystems, so it has to be real on one.
    - Renaming `SKILLS.MD` to `skills.md` in place is not reliable either.
      Windows file tunnelling can restore the original long name - including
      its case - when a just-vacated name is reused inside the tunnel window,
      so the setup silently undoes itself.

    So the install is built with the lowercase name from its very first write
    and never holds the uppercase one, while the incoming package ships only
    the uppercase name. The two live in different directories and collide
    nowhere. No rename, no delete, no tunnelling, and the same logical state on
    every filesystem: one file on disk under a name the incoming manifest
    spells differently.
    """

    @pytest.fixture
    def install_with_lowercase_twin(self, tmp_path):
        install, new = tmp_path / "install", tmp_path / "new"

        for root, registry in ((install, "skills.md"), (new, "SKILLS.MD")):
            write(root / "AGENTS.MD", "# AGENTS\n")
            write(root / registry, "# SKILLS registry\n\n| role | path |\n")
            write(root / "tools" / "thing.py", "print('hello')\n")

        run_tool(MANIFEST, "--root", new, "--version", "2.0.0")
        run_tool(MANIFEST, "--root", install, "--version", "1.0.0")
        assert "| `SKILLS.MD` |" in (new / "MANIFEST.md").read_text()

        on_disk = [p.name for p in install.iterdir() if p.name.lower() == "skills.md"]
        assert on_disk == ["skills.md"], f"setup failed, disk shows {on_disk}"
        return install, new, install / "skills.md"

    def test_a_case_twin_is_never_swept(self, install_with_lowercase_twin):
        install, new, twin = install_with_lowercase_twin

        res = run_tool(UPDATER, "--install", install, "--new", new, "--apply")
        assert res.returncode == 0
        assert "CASE" in res.stdout
        assert "NOT swept" in res.stdout
        assert twin.exists(), "sweeping a case twin can destroy the real file"

    def test_the_twin_is_named_alongside_the_path_it_collides_with(self, install_with_lowercase_twin):
        install, new, _ = install_with_lowercase_twin

        res = run_tool(UPDATER, "--install", install, "--new", new, "--check")
        assert "skills.md" in res.stdout and "SKILLS.MD" in res.stdout
        assert "Rename by hand" in res.stdout

    def test_the_registry_content_survives_the_upgrade(self, install_with_lowercase_twin):
        """The actual damage in the real incident: the file was gone afterwards.

        Whichever name the filesystem reports, a readable role registry has to
        be there when the upgrade finishes.
        """
        install, new, _ = install_with_lowercase_twin
        run_tool(UPDATER, "--install", install, "--new", new, "--apply")

        found = [p for p in install.iterdir() if p.name.lower() == "skills.md"]
        assert found, "the role registry was destroyed by the upgrade"
        assert found[0].read_text().strip(), "the registry survived but is empty"

    def test_a_genuinely_retired_file_is_still_swept(self, manifested, tmp_path):
        """The guard must not become an excuse to stop sweeping."""
        new = tmp_path / "new"
        shutil.copytree(manifested, new)
        run_tool(MANIFEST, "--root", new, "--version", "2.0.0")
        write(manifested / "router.md", "# retired dual-router era\n")

        run_tool(UPDATER, "--install", manifested, "--new", new, "--apply")
        assert not (manifested / "router.md").exists()


class TestPruneDoesNotAbortRepair:
    """A single PermissionError killed the process mid-repair.

    Three of six files restored, no summary, no indication of what happened. A
    tool that deletes must not partially complete on an exception.
    """

    def test_an_undeletable_directory_does_not_abort_the_run(self, manifested, tmp_path):
        """Reset mode, because that is the mode that prunes.

        Repair mode populates no prune candidates at all, so a version of this
        test written against repair passes while exercising nothing - which is
        how it was first written here.
        """
        reference = tmp_path / "reference"
        shutil.copytree(manifested, reference)
        (manifested / "SKILLS.MD").write_bytes(b"# damaged\n")
        write(manifested / "tickets" / "junk" / "leftover.md", "# junk\n")

        # Monkeypatch rmdir rather than chmod: permission semantics differ on
        # Windows, and this suite has to pass on the 3.14t venv too.
        script = tmp_path / "run_cleanup.py"
        script.write_text(
            "import pathlib, runpy, sys\n"
            "real = pathlib.Path.rmdir\n"
            "def flaky(self, *a, **kw):\n"
            "    if self.name == 'junk':\n"
            "        raise PermissionError(13, 'Permission denied')\n"
            "    return real(self, *a, **kw)\n"
            "pathlib.Path.rmdir = flaky\n"
            f"sys.argv = ['cleanup', '--target', {str(manifested)!r},"
            f" '--reference', {str(reference)!r}, '--mode', 'reset', '--apply']\n"
            f"runpy.run_path({str(CLEANUP)!r}, run_name='__main__')\n"
        )
        res = run_tool(script)

        assert res.returncode == 0, res.stderr
        assert "APPLIED" in res.stdout, "the run must complete and report"
        assert "could not be removed" in res.stdout, "and must say what it skipped"
        assert (manifested / "SKILLS.MD").read_bytes() != b"# damaged\n", \
            "the file work must have completed despite the prune failure"

    def test_the_prune_walk_stays_inside_lanes_the_run_touched(self, manifested, tmp_path):
        """The other half of the same bug: the walk covered the entire tree,
        including lanes the tool has no business touching."""
        reference = tmp_path / "reference"
        shutil.copytree(manifested, reference)
        empty_elsewhere = manifested / "agent_onboarding" / "user_defined" / "empty_role"
        empty_elsewhere.mkdir(parents=True)

        res = run_tool(CLEANUP, "--target", manifested, "--reference", reference,
                       "--mode", "repair", "--apply")
        assert res.returncode == 0
        assert empty_elsewhere.is_dir(), "repair must not prune an INSTANCE lane"


class TestIndexerRefusals:
    """A verification glob swept `src_graph.md` into `index_document.py`.

    It overwrote the assembler's byproduct index with a weaker heading-shaped
    one and produced 10 junk index files. Caught only because the manifest file
    count went 435 -> 445.
    """

    def test_refuses_to_index_an_index(self, tmp_path):
        idx = write(tmp_path / "thing_index.md", "# thing_index\n\n## Sections\n")
        res = run_tool(INDEXER, "--doc", idx)
        assert res.returncode == 2
        assert "is already an index" in res.stderr
        assert not (tmp_path / "thing_index_index.md").exists()

    def test_refuses_to_index_an_assembled_graph(self, tmp_path):
        doc = write(tmp_path / "src_graph.md",
                    "# src_graph\n\n<!-- BEGIN FILE: src/a.py -->\n\n## src/a.py\n\n"
                    "<!-- END FILE: src/a.py -->\n")
        res = run_tool(INDEXER, "--doc", doc)
        assert res.returncode == 2
        assert "ASSEMBLED graph" in res.stderr
        assert "Run assemble_graph.py" in res.stderr

    def test_the_existing_byproduct_index_is_not_overwritten(self, tmp_path):
        """The actual damage: a correct index replaced by a weaker one."""
        write(tmp_path / "src_graph.md",
              "# src_graph\n\n<!-- BEGIN FILE: src/a.py -->\n\n<!-- END FILE: src/a.py -->\n")
        good = write(tmp_path / "src_graph_index.md", "# src_graph_index\n\nBYPRODUCT\n")
        before = good.read_bytes()

        run_tool(INDEXER, "--doc", tmp_path / "src_graph.md")
        assert good.read_bytes() == before


class TestAssemblerVariableShadowing:
    """Naming the why-loop variable `src` clobbered the section's source path.

    The footer was emitted carrying a node id instead of the file path. The
    assembler's own range verification caught it and refused to write - which is
    the behaviour under test here, as much as the fix.
    """

    def test_footer_keeps_the_source_path_when_authored_edges_exist(self, tmp_path):
        desc = tmp_path / "desc"
        desc.mkdir()
        (desc / "a.json").write_text(json.dumps({
            "source": "src/a.py",
            "source_sha256": "0" * 64,
            "nodes": {"pkg.a.Alpha": {"id": "pkg.a.Alpha", "label": "Alpha",
                                      "kind": "class", "file": "src/a.py", "lineno": 1}},
            "edges_authored": [{"from": "pkg.a.Alpha", "relation": "uses",
                                "to": "pkg.a.Beta", "why": "needs it to run"}],
        }))
        out = tmp_path / "out"
        out.mkdir()
        res = run_tool(ASSEMBLE, "--descriptors", desc, "--out", out)
        assert res.returncode == 0, res.stderr

        doc = (out / "src_graph.md").read_text()
        assert "<!-- END FILE: src/a.py -->" in doc
        assert "<!-- END FILE: pkg.a.Alpha -->" not in doc

    def test_a_corrupted_range_refuses_to_write(self, tmp_path):
        """Verification is the last line of defence and must fail closed."""
        import assemble_graph as ag
        doc, sections = ag.assemble([{
            "source": "src/a.py", "source_sha256": "0" * 64,
            "nodes": {"x": {"id": "x", "label": "X", "kind": "class",
                            "file": "src/a.py", "lineno": 1}},
        }])
        sections[0]["end"] += 1
        assert ag.verify(doc, sections), "a shifted range must be reported"


class TestEdgeCountMatchesTheSection:
    """The index's `edges` column counted only `edges_out`.

    It undercounted exactly the edges that carry design meaning: 68% of
    relationships are not derivable, so the authored ones are the point of the
    layer. An index column that disagrees with the section it indexes is the
    failure this whole system exists to prevent.
    """

    def test_index_edge_count_equals_rendered_rows(self, tmp_path):
        desc = tmp_path / "desc"
        desc.mkdir()
        (desc / "a.json").write_text(json.dumps({
            "source": "src/a.py", "source_sha256": "0" * 64,
            "nodes": {"A": {"id": "A", "label": "A", "kind": "class",
                            "file": "src/a.py", "lineno": 1}},
            "edges_out": [{"from": "A", "relation": "specializes", "to": "B"}],
            "edges_authored": [
                {"from": "A", "relation": "owns_lifecycle_of", "to": "C"},
                {"from": "A", "relation": "borrows", "to": "D"},
            ],
        }))
        out = tmp_path / "out"
        out.mkdir()
        run_tool(ASSEMBLE, "--descriptors", desc, "--out", out)

        doc = (out / "src_graph.md").read_text()
        index = (out / "src_graph_index.md").read_text()

        rendered = sum(1 for l in doc.split("\n")
                       if l.startswith("| `") and ("| derived |" in l or "| authored |" in l))
        claimed = int([l for l in index.split("\n")
                       if "`src/a.py`" in l][0].strip("|").split("|")[-1].strip())
        assert claimed == rendered == 3


class TestDelimiterIsNotSelfDescribing:
    """A validator counted 576 sections where 575 existed.

    The preamble documented the delimiter format inline, so the description of
    the marker was indistinguishable from an instance of it. A file's own
    documentation must not be parseable as its own data.
    """

    def test_preamble_prose_is_not_countable_as_a_section(self, tmp_path):
        desc = tmp_path / "desc"
        desc.mkdir()
        for name in ("a", "b"):
            (desc / f"{name}.json").write_text(json.dumps({
                "source": f"src/{name}.py", "source_sha256": "0" * 64,
                "nodes": {name: {"id": name, "label": name.upper(), "kind": "class",
                                 "file": f"src/{name}.py", "lineno": 1}},
            }))
        out = tmp_path / "out"
        out.mkdir()
        run_tool(ASSEMBLE, "--descriptors", desc, "--out", out)

        doc = (out / "src_graph.md").read_text()
        index = (out / "src_graph_index.md").read_text()
        claimed = int([l for l in index.split("\n") if "| sections |" in l]
                      [0].split("|")[2].strip())
        assert doc.count("<!-- BEGIN FILE:") == claimed == 2


class TestInstanceLanesAreNeverTouched:
    """`user_defined/` exists so an upgrade never has to choose between the
    user's work and the new version. Verified in both tools, in every mode."""

    @pytest.mark.parametrize("mode", ["reset", "repair"])
    def test_cleanup_leaves_top_level_user_defined_alone(self, manifested, tmp_path, mode):
        reference = tmp_path / "reference"
        shutil.copytree(manifested, reference)
        mine = write(manifested / "user_defined" / "my_script.py", "# mine\n")

        res = run_tool(CLEANUP, "--target", manifested, "--reference", reference,
                       "--mode", mode, "--apply")
        assert res.returncode == 0
        assert mine.read_text() == "# mine\n"

    def test_updater_leaves_top_level_user_defined_alone(self, manifested, tmp_path):
        new = tmp_path / "new"
        shutil.copytree(manifested, new)
        run_tool(MANIFEST, "--root", new, "--version", "2.0.0")
        mine = write(manifested / "user_defined" / "my_script.py", "# mine\n")

        run_tool(UPDATER, "--install", manifested, "--new", new, "--apply")
        assert mine.read_text() == "# mine\n"

    @pytest.mark.parametrize("mode", ["reset", "repair"])
    def test_a_deleted_instance_file_is_not_resurrected(self, manifested, tmp_path, mode):
        """Found by mutation testing, not by review.

        Removing the `INSTANCE` guard from the manifest loop let a *listed*
        instance file fall through to the "missing, therefore restore" branch.
        Every existing test used unmanifested instance files, so the branch was
        never reached and the mutation survived the whole suite.

        Restoring a file the user deliberately deleted is the same betrayal as
        overwriting one they edited: the package has no claim on this lane.
        """
        reference = tmp_path / "reference"
        shutil.copytree(manifested, reference)

        listed = manifested / "user_defined" / "README.md"
        role = manifested / "agent_onboarding" / "user_defined" / "myrole" / "SKILLS.MD"
        assert "user_defined/README.md" in (manifested / "MANIFEST.md").read_text()
        listed.unlink()
        role.unlink()

        res = run_tool(CLEANUP, "--target", manifested, "--reference", reference,
                       "--mode", mode, "--apply")
        assert res.returncode == 0
        assert not listed.exists(), "a deleted INSTANCE file must stay deleted"
        assert not role.exists(), "a deleted role overlay must stay deleted"

    def test_purge_user_defined_does_not_reach_the_top_level_lane(self, manifested, tmp_path):
        """`--purge-user-defined` is documented as clearing role overlays under
        `agent_onboarding/user_defined/`. The top-level free space is a
        different lane and is not implied."""
        reference = tmp_path / "reference"
        shutil.copytree(manifested, reference)
        mine = write(manifested / "user_defined" / "my_script.py", "# mine\n")
        role = write(manifested / "agent_onboarding" / "user_defined" / "r" / "SKILLS.MD",
                     "# r\n")

        run_tool(CLEANUP, "--target", manifested, "--reference", reference,
                 "--mode", "reset", "--purge-user-defined", "--apply")
        assert not role.exists(), "role overlays are the documented target"
        assert mine.exists(), "the top-level free space is a different lane"
