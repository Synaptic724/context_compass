"""cleanup_context_compass end to end: reset versus repair, and what each protects."""

from __future__ import annotations

import shutil

import pytest

from conftest import TOOLS, run_tool, write

pytestmark = pytest.mark.integration

CLEANUP = TOOLS / "cleanup_context_compass.py"


@pytest.fixture
def install_and_reference(manifested, tmp_path):
    """A clean reference package, plus an install that has drifted from it."""
    reference = tmp_path / "reference"
    shutil.copytree(manifested, reference)

    install = manifested
    write(install / "tickets" / "tasks" / "T-1" / "README.md", "# my ticket\n")
    write(install / "system_docs" / "src_architecture.md", "# my architecture\n")
    write(install / "tools" / "foreign.py", "# not ours\n")
    (install / "tools" / "thing.py").write_bytes(b"print('locally edited')\n")
    write(install / "agent_onboarding" / "user_defined" / "extra" / "SKILLS.MD", "# extra\n")
    return install, reference


class TestRefusals:
    def test_refuses_without_apply_or_check(self, manifested):
        res = run_tool(CLEANUP, "--target", manifested)
        assert res.returncode == 2
        assert "Refusing to act without --apply" in res.stdout

    def test_refuses_a_target_that_is_not_a_package(self, tmp_path):
        res = run_tool(CLEANUP, "--target", tmp_path, "--check")
        assert res.returncode == 2
        assert "not a package root" in res.stdout

    def test_refuses_without_a_manifest(self, mock_package):
        res = run_tool(CLEANUP, "--target", mock_package, "--check")
        assert res.returncode == 2
        assert "no MANIFEST.md" in res.stdout

    def test_refuses_to_restore_from_itself(self, install_and_reference):
        """If files are altered and the reference IS the target, there is
        nothing to restore them from. Proceeding would report success over a
        tree it could not fix."""
        install, _ = install_and_reference
        res = run_tool(CLEANUP, "--target", install, "--apply")
        assert res.returncode == 2
        assert "REFUSED" in res.stdout


class TestRepairMode:
    def test_repair_leaves_the_projects_work_alone(self, install_and_reference):
        install, reference = install_and_reference
        res = run_tool(CLEANUP, "--target", install, "--reference", reference,
                       "--mode", "repair", "--apply")
        assert res.returncode == 0
        assert (install / "tickets" / "tasks" / "T-1" / "README.md").is_file()
        assert (install / "system_docs" / "src_architecture.md").is_file()

    def test_repair_restores_an_edited_package_file(self, install_and_reference):
        install, reference = install_and_reference
        run_tool(CLEANUP, "--target", install, "--reference", reference,
                 "--mode", "repair", "--apply")
        assert (install / "tools" / "thing.py").read_bytes() == b"print('hello')\n"

    def test_repair_reports_but_keeps_a_foreign_file_in_a_package_lane(self, install_and_reference):
        """It is usually foreign content, but it can be a script someone added
        on purpose. Never deleted silently."""
        install, reference = install_and_reference
        res = run_tool(CLEANUP, "--target", install, "--reference", reference,
                       "--mode", "repair", "--apply")
        assert "unknown tools/foreign.py" in res.stdout
        assert (install / "tools" / "foreign.py").is_file()

    def test_repair_never_touches_user_defined(self, install_and_reference):
        install, reference = install_and_reference
        run_tool(CLEANUP, "--target", install, "--reference", reference,
                 "--mode", "repair", "--apply")
        assert (install / "agent_onboarding" / "user_defined" / "extra" / "SKILLS.MD").is_file()


class TestResetMode:
    def test_reset_empties_the_working_lanes(self, install_and_reference):
        install, reference = install_and_reference
        res = run_tool(CLEANUP, "--target", install, "--reference", reference,
                       "--mode", "reset", "--apply")
        assert res.returncode == 0
        assert not (install / "tickets" / "tasks" / "T-1" / "README.md").exists()
        assert not (install / "system_docs" / "src_architecture.md").exists()

    def test_reset_removes_a_foreign_file_from_a_package_lane(self, install_and_reference):
        install, reference = install_and_reference
        run_tool(CLEANUP, "--target", install, "--reference", reference,
                 "--mode", "reset", "--apply")
        assert not (install / "tools" / "foreign.py").exists()

    def test_reset_keeps_the_seeded_lane_files(self, install_and_reference):
        install, reference = install_and_reference
        run_tool(CLEANUP, "--target", install, "--reference", reference,
                 "--mode", "reset", "--apply")
        assert (install / "tickets" / "tasks" / "README.md").is_file()

    def test_reset_does_not_imply_purging_user_defined(self, install_and_reference):
        """Deleting someone's role because they asked to tidy a lane would be a
        betrayal of the invariant. It has to be asked for by name."""
        install, reference = install_and_reference
        res = run_tool(CLEANUP, "--target", install, "--reference", reference,
                       "--mode", "reset", "--apply")
        assert (install / "agent_onboarding" / "user_defined" / "extra" / "SKILLS.MD").is_file()
        assert "kept" in res.stdout

    def test_purge_user_defined_is_explicit_and_works(self, install_and_reference):
        install, reference = install_and_reference
        res = run_tool(CLEANUP, "--target", install, "--reference", reference,
                       "--mode", "reset", "--purge-user-defined", "--apply")
        assert "WILL BE DELETED" in res.stdout
        assert not (install / "agent_onboarding" / "user_defined" / "extra" / "SKILLS.MD").exists()


class TestContentDetection:
    def test_a_file_at_the_right_path_with_wrong_content_is_found(self, manifested, tmp_path):
        """A path-only diff reports this as present and correct. Only the hash
        finds it - and on the cleanup this tool was written for, 11 files were
        exactly this shape."""
        reference = tmp_path / "reference"
        shutil.copytree(manifested, reference)
        (manifested / "SKILLS.MD").write_bytes(b"# SOMEONE ELSE'S REGISTRY\n")

        res = run_tool(CLEANUP, "--target", manifested, "--reference", reference,
                       "--mode", "repair", "--check")
        assert res.returncode == 1
        assert "repair  SKILLS.MD" in res.stdout

    def test_check_on_a_clean_install_reports_clean(self, manifested):
        res = run_tool(CLEANUP, "--target", manifested, "--check")
        assert res.returncode == 0
        assert "already at manifest state" in res.stdout

    def test_check_changes_nothing(self, install_and_reference):
        install, reference = install_and_reference
        before = {p.relative_to(install).as_posix(): p.read_bytes()
                  for p in install.rglob("*") if p.is_file()}
        run_tool(CLEANUP, "--target", install, "--reference", reference,
                 "--mode", "reset", "--check")
        after = {p.relative_to(install).as_posix(): p.read_bytes()
                 for p in install.rglob("*") if p.is_file()}
        assert before == after


class TestManagedBlocks:
    def test_repair_swaps_the_block_and_keeps_the_rows(self, manifested, tmp_path):
        reference = tmp_path / "reference"
        shutil.copytree(manifested, reference)
        (reference / "attention_board.md").write_bytes(
            (manifested / "attention_board.md").read_text()
            .replace("Read SKILLS.MD, then your role chain.", "UPDATED ROUTING.")
            .encode())

        res = run_tool(CLEANUP, "--target", manifested, "--reference", reference,
                       "--mode", "repair", "--apply")
        assert res.returncode == 0
        board = (manifested / "attention_board.md").read_text()
        assert "UPDATED ROUTING." in board
        assert "| T-1 | mark |" in board, "the install's rows must survive"


class TestConfigDrift:
    def test_config_divergence_is_reported_by_key_and_never_rewritten(self, manifested, tmp_path):
        reference = tmp_path / "reference"
        shutil.copytree(manifested, reference)
        cfg = manifested / "config" / "context_compass_config.yaml"
        cfg.write_bytes((cfg.read_text() + "\nmine:\n  custom: 1\n").encode())
        mine = cfg.read_bytes()

        res = run_tool(CLEANUP, "--target", manifested, "--reference", reference,
                       "--mode", "repair", "--apply")
        assert "keys you added:      mine" in res.stdout
        assert cfg.read_bytes() == mine, "config is never rewritten here"
