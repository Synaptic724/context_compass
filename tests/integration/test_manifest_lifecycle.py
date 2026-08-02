"""package_manifest end to end: generate, check, detect drift."""

from __future__ import annotations

import pytest

from conftest import TOOLS, run_tool, write

pytestmark = pytest.mark.integration

MANIFEST = TOOLS / "package_manifest.py"


def test_generate_then_check_is_clean(mock_package):
    gen = run_tool(MANIFEST, "--root", mock_package, "--version", "1.0.0")
    assert gen.returncode == 0, gen.stderr
    assert "WROTE: MANIFEST.md" in gen.stdout

    chk = run_tool(MANIFEST, "--root", mock_package, "--check")
    assert chk.returncode == 0
    assert "OK: manifest is current" in chk.stdout


def test_check_reports_added_removed_and_changed(manifested):
    write(manifested / "tools" / "brand_new.py", "x = 1\n")
    (manifested / "tools" / "thing.py").write_bytes(b"print('changed')\n")
    (manifested / "SKILLS.MD").unlink()

    chk = run_tool(MANIFEST, "--root", manifested, "--check")
    assert chk.returncode == 1
    assert "STALE: +1 -1 ~1" in chk.stdout
    assert "added    tools/brand_new.py" in chk.stdout
    assert "removed  SKILLS.MD" in chk.stdout
    assert "changed  tools/thing.py" in chk.stdout


class TestCaseDrift:
    """A rename that only changes case is one file, not an add and a remove.

    Observed three times on `SKILLS.MD` in a single day, drifting to `SKILLS.md`
    from something outside the package. Reported as `+1 -1` it reads as
    unrelated churn, and the obvious repair - delete the removed one - destroys
    the added one, because on a case-insensitive filesystem they are the same
    file.
    """

    def _rename_case(self, path, new_name):
        tmp = path.with_name(path.name + ".__tmp")
        path.rename(tmp)
        final = path.with_name(new_name)
        tmp.rename(final)
        return final

    def test_case_only_rename_is_named_as_drift(self, manifested):
        self._rename_case(manifested / "SKILLS.MD", "SKILLS.md")
        res = run_tool(MANIFEST, "--root", manifested, "--check")
        assert res.returncode == 1
        assert "CASE DRIFT 1" in res.stdout
        assert "SKILLS.MD  ->  SKILLS.md" in res.stdout

    def test_it_is_not_double_counted_as_add_and_remove(self, manifested):
        self._rename_case(manifested / "SKILLS.MD", "SKILLS.md")
        res = run_tool(MANIFEST, "--root", manifested, "--check")
        assert "STALE: +0 -0" in res.stdout
        assert "added    SKILLS.md" not in res.stdout
        assert "removed  SKILLS.MD" not in res.stdout

    def test_it_says_to_rename_rather_than_delete(self, manifested):
        """The dangerous repair is deleting either one."""
        self._rename_case(manifested / "SKILLS.MD", "SKILLS.md")
        res = run_tool(MANIFEST, "--root", manifested, "--check")
        assert "Rename it" in res.stdout
        assert "rather than deleting either" in res.stdout

    def test_identical_contents_are_reported_as_such(self, manifested):
        self._rename_case(manifested / "SKILLS.MD", "SKILLS.md")
        res = run_tool(MANIFEST, "--root", manifested, "--check")
        assert "contents identical" in res.stdout

    def test_a_genuine_add_and_remove_are_still_reported_separately(self, manifested):
        write(manifested / "tools" / "brand_new.py", "x = 1\n")
        (manifested / "SKILLS.MD").unlink()
        res = run_tool(MANIFEST, "--root", manifested, "--check")
        assert "CASE DRIFT" not in res.stdout
        assert "added    tools/brand_new.py" in res.stdout
        assert "removed  SKILLS.MD" in res.stdout


def test_check_without_a_manifest_reports_missing(mock_package):
    chk = run_tool(MANIFEST, "--root", mock_package, "--check")
    assert chk.returncode == 1
    assert "MISSING" in chk.stdout


def test_refuses_a_root_that_is_not_a_package(tmp_path):
    """No AGENTS.MD means this is not a package root. Writing a MANIFEST.md into
    an arbitrary directory would be a confusing mess to clean up."""
    (tmp_path / "random.txt").write_bytes(b"hi\n")
    res = run_tool(MANIFEST, "--root", tmp_path)
    assert res.returncode == 2
    assert "does not look like a package root" in res.stdout


def test_version_is_carried_forward_when_not_given(manifested):
    """Regenerating after an edit must not silently reset the version to
    0.0.0 - downstream installs compare versions to decide whether to upgrade."""
    write(manifested / "tools" / "another.py", "y = 2\n")
    res = run_tool(MANIFEST, "--root", manifested)
    assert res.returncode == 0
    assert "package_version 1.0.0" in res.stdout


def test_regeneration_is_stable(manifested):
    """Same tree, same manifest. A manifest that churns produces diffs that say
    nothing happened."""
    first = (manifested / "MANIFEST.md").read_bytes()
    run_tool(MANIFEST, "--root", manifested)
    assert (manifested / "MANIFEST.md").read_bytes() == first


def test_class_counts_cover_every_ownership_class(manifested):
    text = (manifested / "MANIFEST.md").read_text()
    for cls in ("PACKAGE", "RESET", "INSTANCE", "LIVE", "CONFIG"):
        assert f"| {cls} |" in text, f"{cls} missing from the class table"


def test_manifest_records_the_lane_policy(manifested):
    """The policy is what tells a reader which directories an upgrade sweeps.
    Leaving it implicit is how a `scripts/` directory survives two upgrades."""
    text = (manifested / "MANIFEST.md").read_text()
    assert "## Lane policy" in text
    assert "| `tickets/` | permissive |" in text
    assert "| everything else | strict - swept on upgrade |" in text
