"""update_context_compass end to end: the three-hash truth table and lane policy.

One hash tells you a file changed. It cannot tell you WHO changed it, which is
the only question that matters when deciding whether to overwrite. Each row of
the table gets its own test.
"""

from __future__ import annotations

import shutil

import pytest

from conftest import TOOLS, run_tool, write

pytestmark = pytest.mark.integration

UPDATER = TOOLS / "update_context_compass.py"
MANIFEST = TOOLS / "package_manifest.py"


def remanifest(root, version):
    res = run_tool(MANIFEST, "--root", root, "--version", version)
    assert res.returncode == 0, res.stdout
    return root


@pytest.fixture
def install(manifested):
    """v1.0.0, clean, with a manifest recording the shipped hashes."""
    return manifested


@pytest.fixture
def newpkg(manifested, tmp_path):
    """v2.0.0: a copy of the install that upstream has since moved on from."""
    new = tmp_path / "newpkg"
    shutil.copytree(manifested, new)
    return new


@pytest.fixture
def unmanifested(manifested, tmp_path):
    """A separate package root with no MANIFEST.md.

    Must be a distinct directory: `mock_package` and `manifested` are the same
    tree, so using the former as a stand-in for "no manifest" silently tests
    nothing.
    """
    old = tmp_path / "unmanifested"
    shutil.copytree(manifested, old)
    (old / "MANIFEST.md").unlink()
    return old


class TestTruthTable:
    def test_row1_package_moved_install_untouched_is_replaced(self, install, newpkg):
        (newpkg / "tools" / "thing.py").write_bytes(b"print('v2')\n")
        remanifest(newpkg, "2.0.0")

        res = run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        assert res.returncode == 0
        assert (install / "tools" / "thing.py").read_bytes() == b"print('v2')\n"
        assert "replaced 1" in res.stdout

    def test_row2_nothing_moved_is_skipped(self, install, newpkg):
        remanifest(newpkg, "2.0.0")
        res = run_tool(UPDATER, "--install", install, "--new", newpkg, "--check")
        assert res.returncode == 0
        assert "  replace      0" in res.stdout
        assert "  skip" in res.stdout

    def test_row3_user_edited_package_did_not_keeps_the_edit(self, install, newpkg):
        """Nothing to conform to, so the local edit stands."""
        (install / "tools" / "thing.py").write_bytes(b"print('MINE')\n")
        remanifest(newpkg, "2.0.0")

        res = run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        assert res.returncode == 0
        assert (install / "tools" / "thing.py").read_bytes() == b"print('MINE')\n"
        assert "kept 1 local edits" in res.stdout

    def test_row4_both_moved_conforms_by_default(self, install, newpkg):
        """Package files belong to the package. Preserving a divergence is not a
        kindness, it is a debt re-resolved on every future upgrade."""
        (install / "tools" / "thing.py").write_bytes(b"print('MINE')\n")
        (newpkg / "tools" / "thing.py").write_bytes(b"print('v2')\n")
        remanifest(newpkg, "2.0.0")

        res = run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        assert res.returncode == 0
        assert (install / "tools" / "thing.py").read_bytes() == b"print('v2')\n"
        assert "conformed 1" in res.stdout

    def test_row4_preserve_local_restores_the_refusal(self, install, newpkg):
        (install / "tools" / "thing.py").write_bytes(b"print('MINE')\n")
        (newpkg / "tools" / "thing.py").write_bytes(b"print('v2')\n")
        remanifest(newpkg, "2.0.0")

        res = run_tool(UPDATER, "--install", install, "--new", newpkg,
                       "--preserve-local", "--apply")
        assert (install / "tools" / "thing.py").read_bytes() == b"print('MINE')\n"
        assert "left 1 edited package files" in res.stdout

    def test_conform_is_named_not_silent(self, install, newpkg):
        (install / "tools" / "thing.py").write_bytes(b"print('MINE')\n")
        (newpkg / "tools" / "thing.py").write_bytes(b"print('v2')\n")
        remanifest(newpkg, "2.0.0")
        res = run_tool(UPDATER, "--install", install, "--new", newpkg, "--check")
        assert "conform  tools/thing.py" in res.stdout


class TestNewAndRetiredFiles:
    def test_a_new_file_is_added(self, install, newpkg):
        write(newpkg / "agent_onboarding" / "default" / "engineer" / "skills" / "b.md",
              "# skill b\n")
        remanifest(newpkg, "2.0.0")

        res = run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        assert (install / "agent_onboarding" / "default" / "engineer" / "skills" / "b.md").is_file()
        assert "added 1" in res.stdout

    def test_a_retired_file_in_a_strict_lane_is_swept(self, install, newpkg):
        """The real case: a `scripts/` directory left over from before the
        rename to `tools/`, still readable by agents two upgrades later."""
        write(install / "scripts" / "old_helper.py", "# retired\n")
        remanifest(newpkg, "2.0.0")

        res = run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        assert not (install / "scripts" / "old_helper.py").exists()
        assert "swept 1 retired" in res.stdout

    def test_keep_retired_leaves_it_but_still_names_it(self, install, newpkg):
        write(install / "scripts" / "old_helper.py", "# retired\n")
        remanifest(newpkg, "2.0.0")

        res = run_tool(UPDATER, "--install", install, "--new", newpkg,
                       "--keep-retired", "--apply")
        assert (install / "scripts" / "old_helper.py").is_file()
        assert "sweep    scripts/old_helper.py" in res.stdout

    def test_empty_directories_are_pruned_after_a_sweep(self, install, newpkg):
        write(install / "scripts" / "old_helper.py", "# retired\n")
        remanifest(newpkg, "2.0.0")
        run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        assert not (install / "scripts").exists()


class TestLanePolicy:
    @pytest.mark.parametrize("rel,content", [
        ("tickets/tasks/T-9/README.md", "# my ticket\n"),
        ("system_docs/src_architecture.md", "# my architecture\n"),
        ("artifacts/finding.md", "# my finding\n"),
        ("special_instructions/rules.md", "# my rules\n"),
        ("user_defined/notes.md", "# my notes\n"),
        ("agent_onboarding/user_defined/mine/SKILLS.MD", "# my role\n"),
    ])
    def test_permissive_lanes_survive_an_upgrade(self, install, newpkg, rel, content):
        write(install / rel, content)
        remanifest(newpkg, "2.0.0")

        res = run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        assert res.returncode == 0
        assert (install / rel).read_text() == content

    def test_an_upgrade_never_rewrites_a_reset_lane_file(self, install, newpkg):
        """An upgrade that rewrites someone's architecture map is not an
        upgrade."""
        doc = write(install / "system_docs" / "src_architecture.md", "# mine\n")
        write(newpkg / "system_docs" / "src_architecture.md", "# UPSTREAM\n")
        remanifest(newpkg, "2.0.0")

        run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        assert doc.read_text() == "# mine\n"


class TestLiveAndConfig:
    def test_only_the_managed_block_is_swapped(self, install, newpkg):
        board = newpkg / "attention_board.md"
        board.write_bytes(board.read_text()
                          .replace("Read SKILLS.MD, then your role chain.", "V2 ROUTING.")
                          .encode())
        remanifest(newpkg, "2.0.0")

        res = run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        assert res.returncode == 0
        text = (install / "attention_board.md").read_text()
        assert "V2 ROUTING." in text
        assert "| T-1 | mark |" in text, "routing rows are the install's"

    def test_a_new_config_key_is_added_with_its_comment(self, install, newpkg):
        cfg = newpkg / "config" / "context_compass_config.yaml"
        cfg.write_bytes((cfg.read_text()
                         + "\n# controls the new thing\nnew_thing:\n  enabled: true\n").encode())
        remanifest(newpkg, "2.0.0")

        res = run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        assert res.returncode == 0
        merged = (install / "config" / "context_compass_config.yaml").read_text()
        assert "new_thing:" in merged
        assert "# controls the new thing" in merged

    def test_a_value_the_user_set_is_never_reset_by_a_key_addition(self, install, newpkg):
        cfg_i = install / "config" / "context_compass_config.yaml"
        cfg_i.write_bytes(cfg_i.read_text().replace("enforce: true", "enforce: false").encode())
        cfg_n = newpkg / "config" / "context_compass_config.yaml"
        cfg_n.write_bytes((cfg_n.read_text() + "\nnew_thing:\n  enabled: true\n").encode())
        remanifest(newpkg, "2.0.0")

        run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        merged = cfg_i.read_text()
        assert "enforce: false" in merged, "the user's value stands"
        assert "new_thing:" in merged


class TestContract:
    def test_refuses_without_apply_or_check(self, install, newpkg):
        remanifest(newpkg, "2.0.0")
        res = run_tool(UPDATER, "--install", install, "--new", newpkg)
        assert res.returncode == 2
        assert "Refusing to act without --apply" in res.stdout

    def test_refuses_a_new_package_with_no_manifest(self, install, unmanifested):
        """Without the incoming manifest there is nothing to compare against."""
        res = run_tool(UPDATER, "--install", install, "--new", unmanifested, "--check")
        assert res.returncode == 2
        assert "has no MANIFEST.md" in res.stdout

    def test_refuses_a_non_package_root(self, install, tmp_path):
        res = run_tool(UPDATER, "--install", install, "--new", tmp_path, "--check")
        assert res.returncode == 2
        assert "is not a package root" in res.stdout

    def test_check_changes_nothing(self, install, newpkg):
        (newpkg / "tools" / "thing.py").write_bytes(b"print('v2')\n")
        remanifest(newpkg, "2.0.0")
        before = {p.relative_to(install).as_posix(): p.read_bytes()
                  for p in install.rglob("*") if p.is_file()}

        run_tool(UPDATER, "--install", install, "--new", newpkg, "--check")
        after = {p.relative_to(install).as_posix(): p.read_bytes()
                 for p in install.rglob("*") if p.is_file()}
        assert before == after

    def test_the_manifest_is_carried_over_on_apply(self, install, newpkg):
        """Otherwise the next upgrade has no shipped hashes and every file falls
        into the conform bucket."""
        remanifest(newpkg, "2.0.0")
        run_tool(UPDATER, "--install", install, "--new", newpkg, "--apply")
        assert "| package_version | 2.0.0 |" in (install / "MANIFEST.md").read_text()

    def test_first_adoption_without_a_manifest_is_explained(self, unmanifested, newpkg):
        """No shipped hashes means a local edit and an upstream change are
        indistinguishable. Say so rather than silently conforming."""
        remanifest(newpkg, "2.0.0")
        res = run_tool(UPDATER, "--install", unmanifested, "--new", newpkg, "--check")
        assert "manifest-aware upgrade" in res.stdout
        assert "user_defined" in res.stdout, "must say which lanes are safe"

    def test_first_adoption_conforms_every_differing_file(self, unmanifested, newpkg):
        (unmanifested / "tools" / "thing.py").write_bytes(b"print('MINE')\n")
        remanifest(newpkg, "2.0.0")
        res = run_tool(UPDATER, "--install", unmanifested, "--new", newpkg, "--apply")
        assert res.returncode == 0
        assert (unmanifested / "tools" / "thing.py").read_bytes() == b"print('hello')\n"
        assert "conform  tools/thing.py" in res.stdout
