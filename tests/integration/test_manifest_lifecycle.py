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
