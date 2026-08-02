"""Upgrading across package versions, and refusing across format versions.

Two different numbers live in a manifest and they are routinely confused:

    package_version    the CONTENT. 2.3.1 -> 2.5.2 is an ordinary upgrade.
    manifest_version   the FORMAT. A major bump means these tools cannot read it.
"""

from __future__ import annotations

import shutil

import pytest

import package_manifest as pm
from conftest import TOOLS, run_tool, write

pytestmark = pytest.mark.integration

UPDATER = TOOLS / "update_context_compass.py"
CLEANUP = TOOLS / "cleanup_context_compass.py"
MIGRATE = TOOLS / "migrate_boards.py"
MANIFEST = TOOLS / "package_manifest.py"


class TestPackageVersionRange:
    @pytest.mark.parametrize("old_version", ["2.0.0", "2.3.1", "2.4.0", "2.5.0"])
    def test_upgrades_from_several_prior_versions(self, manifested, tmp_path, old_version):
        """The install's package_version is metadata, not a gate. An upgrade
        from any of these must work identically."""
        run_tool(MANIFEST, "--root", manifested, "--version", old_version)
        new = tmp_path / "new"
        shutil.copytree(manifested, new)
        write(new / "agent_onboarding" / "default" / "engineer" / "skills" / "new.md", "# new\n")
        run_tool(MANIFEST, "--root", new, "--version", "2.9.9")

        res = run_tool(UPDATER, "--install", manifested, "--new", new, "--apply")
        assert res.returncode == 0, res.stdout
        assert (manifested / "agent_onboarding" / "default" / "engineer"
                / "skills" / "new.md").is_file()

    def test_an_install_with_no_manifest_still_upgrades(self, mock_package, tmp_path):
        """Installs predating the manifest entirely."""
        new = tmp_path / "new"
        shutil.copytree(mock_package, new)
        run_tool(MANIFEST, "--root", new, "--version", "2.9.9")

        res = run_tool(UPDATER, "--install", mock_package, "--new", new, "--apply")
        assert res.returncode == 0
        assert (mock_package / "MANIFEST.md").is_file()

    def test_upgrading_to_an_older_package_is_allowed_and_named(self, manifested, tmp_path):
        """Downgrades are a legitimate rollback. The tool reports both versions
        and does not editorialise."""
        new = tmp_path / "new"
        shutil.copytree(manifested, new)
        run_tool(MANIFEST, "--root", new, "--version", "0.9.0")
        res = run_tool(UPDATER, "--install", manifested, "--new", new, "--check")
        assert res.returncode == 0
        assert "version 1.0.0" in res.stdout and "version 0.9.0" in res.stdout


class TestManifestFormatVersion:
    def test_current_format_is_accepted(self, manifested):
        text = (manifested / "MANIFEST.md").read_text()
        assert pm.manifest_version_of(text) == pm.MANIFEST_VERSION
        assert pm.check_manifest_compatible(text, "x") is None

    def test_a_manifest_with_no_version_field_is_accepted(self):
        """Predates the field. The format was 1.x throughout, so refusing would
        break installs over a stamp that was missing rather than wrong."""
        assert pm.manifest_version_of("## Files\n") is None
        assert pm.check_manifest_compatible("## Files\n", "x") is None

    @pytest.mark.parametrize("version", ["1.0.0", "1.4.0", "1.99.3"])
    def test_any_1_x_format_is_readable(self, version):
        text = f"| manifest_version | {version} |\n"
        assert pm.check_manifest_compatible(text, "x") is None

    @pytest.mark.parametrize("version", ["2.0.0", "3.1.0"])
    def test_an_unknown_major_is_refused_with_a_reason(self, version):
        msg = pm.check_manifest_compatible(f"| manifest_version | {version} |\n", "--new X")
        assert msg is not None
        assert version in msg and "--new X" in msg
        assert "Upgrade the tools" in msg

    def _bump_format(self, root):
        p = root / "MANIFEST.md"
        p.write_bytes(p.read_text().replace(
            f"| manifest_version | {pm.MANIFEST_VERSION} |",
            "| manifest_version | 2.0.0 |").encode())

    def test_updater_refuses_a_future_incoming_format(self, manifested, tmp_path):
        new = tmp_path / "new"
        shutil.copytree(manifested, new)
        run_tool(MANIFEST, "--root", new, "--version", "2.9.9")
        self._bump_format(new)

        res = run_tool(UPDATER, "--install", manifested, "--new", new, "--check")
        assert res.returncode == 2
        assert "manifest format 2.0.0" in res.stdout

    def test_updater_refuses_a_future_installed_format(self, manifested, tmp_path):
        new = tmp_path / "new"
        shutil.copytree(manifested, new)
        run_tool(MANIFEST, "--root", new, "--version", "2.9.9")
        self._bump_format(manifested)

        res = run_tool(UPDATER, "--install", manifested, "--new", new, "--check")
        assert res.returncode == 2
        assert "manifest format 2.0.0" in res.stdout

    def test_cleanup_refuses_a_future_format(self, manifested):
        self._bump_format(manifested)
        res = run_tool(CLEANUP, "--target", manifested, "--check")
        assert res.returncode == 2
        assert "manifest format 2.0.0" in res.stdout

    def test_migrate_boards_refuses_a_future_format(self, manifested, tmp_path):
        new = tmp_path / "new"
        shutil.copytree(manifested, new)
        run_tool(MANIFEST, "--root", new, "--version", "2.9.9")
        self._bump_format(new)

        res = run_tool(MIGRATE, "--install", manifested, "--new", new, "--check")
        assert res.returncode == 2
        assert "manifest format 2.0.0" in res.stdout

    def test_refusal_writes_nothing(self, manifested, tmp_path):
        """A refusal that half-applied would be worse than no check at all."""
        new = tmp_path / "new"
        shutil.copytree(manifested, new)
        write(new / "tools" / "brand_new.py", "x = 1\n")
        run_tool(MANIFEST, "--root", new, "--version", "2.9.9")
        self._bump_format(new)

        before = {p.relative_to(manifested).as_posix(): p.read_bytes()
                  for p in manifested.rglob("*") if p.is_file()}
        res = run_tool(UPDATER, "--install", manifested, "--new", new, "--apply")
        assert res.returncode == 2
        after = {p.relative_to(manifested).as_posix(): p.read_bytes()
                 for p in manifested.rglob("*") if p.is_file()}
        assert before == after
