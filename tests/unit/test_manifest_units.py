"""Unit tests for package_manifest: classification, lane policy, parse."""

from __future__ import annotations

import pytest

import package_manifest as pm

pytestmark = pytest.mark.unit


class TestClassify:
    """Ownership class assignment. Longest matching prefix wins."""

    @pytest.mark.parametrize("rel,expected", [
        ("AGENTS.MD", "PACKAGE"),
        ("tools/package_manifest.py", "PACKAGE"),
        ("agent_onboarding/default/engineer/SKILLS.MD", "PACKAGE"),
        ("tickets/tasks/README.md", "RESET"),
        ("artifacts/finding.md", "RESET"),
        ("system_docs/src_graph.md", "RESET"),
        ("user_defined/notes.md", "INSTANCE"),
        ("agent_onboarding/user_defined/myrole/SKILLS.MD", "INSTANCE"),
        ("attention_board.md", "LIVE"),
        ("artifact_board.md", "LIVE"),
        ("mailbox_board.md", "LIVE"),
        ("config/context_compass_config.yaml", "CONFIG"),
    ])
    def test_each_class(self, rel, expected):
        assert pm.classify(rel) == expected

    def test_instance_overlay_beats_the_package_default(self):
        rel = "agent_onboarding/user_defined/synaptic/skills/deep.md"
        assert pm.classify(rel) == "INSTANCE"

    def test_longest_prefix_wins_not_declaration_order(self, monkeypatch):
        """The documented rule: "a PACKAGE directory can still contain a RESET
        subtree".

        No pair of shipped rules currently overlaps, so the real CLASS_RULES
        cannot distinguish longest-prefix from first-match - a mutation flipping
        the comparison survived the whole suite. This drives the branch with a
        genuine overlap so the guarantee is tested rather than assumed, and so
        adding a nested rule later cannot quietly break it.
        """
        monkeypatch.setattr(pm, "CLASS_RULES", (
            ("", "PACKAGE"),
            ("tools/", "PACKAGE"),
            ("tools/generated/", "RESET"),
            ("tools/generated/pinned/", "INSTANCE"),
        ))
        assert pm.classify("tools/build.py") == "PACKAGE"
        assert pm.classify("tools/generated/out.md") == "RESET"
        assert pm.classify("tools/generated/pinned/mine.md") == "INSTANCE"

    def test_declaration_order_does_not_affect_the_result(self, monkeypatch):
        """Same rules, shuffled. Longest match must still win."""
        monkeypatch.setattr(pm, "CLASS_RULES", (
            ("tools/generated/pinned/", "INSTANCE"),
            ("", "PACKAGE"),
            ("tools/generated/", "RESET"),
            ("tools/", "PACKAGE"),
        ))
        assert pm.classify("tools/generated/pinned/mine.md") == "INSTANCE"
        assert pm.classify("tools/generated/out.md") == "RESET"

    def test_reset_subtree_inside_package_directory(self):
        """A RESET lane nested under a PACKAGE tree still classifies RESET."""
        assert pm.classify("system_docs/patches/active/p1/architecture_patch.md") == "RESET"

    def test_unknown_path_defaults_to_package(self):
        """Unlisted means package-owned, which is the strict default."""
        assert pm.classify("some/new/thing.md") == "PACKAGE"

    def test_prefix_must_be_a_directory_boundary(self):
        """`tickets_archive/` is not inside `tickets/` and must stay PACKAGE.

        Naive `startswith("tickets")` would classify it RESET and an upgrade
        would stop conforming it.
        """
        assert pm.classify("tickets_archive/old.md") == "PACKAGE"


class TestLanePolicy:
    @pytest.mark.parametrize("rel", [
        "tickets/anything.md",
        "artifacts/x/y.md",
        "system_docs/src_architecture.md",
        "context_management/board.md",
        "special_instructions/rules.md",
        "user_defined/whatever.txt",
        "agent_onboarding/user_defined/role/SKILLS.MD",
    ])
    def test_permissive_lanes_keep_unmanifested_files(self, rel):
        assert pm.is_permissive(rel) is True

    @pytest.mark.parametrize("rel", [
        "AGENTS.MD",
        "tools/leftover.py",
        "scripts/old_script.py",
        "agent_onboarding/default/engineer/skills/retired.md",
        "router.md",
    ])
    def test_strict_lanes_do_not(self, rel):
        """These are the paths an upgrade sweeps. All four examples are real:
        a `scripts/` directory left from before the rename to `tools/`, a root
        `router.md` from the retired dual-router era, and retired skills that
        agents kept reading for two upgrades because reporting them was not
        enough."""
        assert pm.is_permissive(rel) is False


class TestParse:
    def test_build_then_parse_round_trips(self, mock_package):
        text = pm.build(mock_package, "1.2.3")
        entries = pm.parse(text)

        on_disk = {p.relative_to(mock_package).as_posix()
                   for p in mock_package.rglob("*") if p.is_file()}
        assert set(entries) == on_disk

    def test_parse_recovers_class_and_hash(self, mock_package):
        entries = pm.parse(pm.build(mock_package, "1.0.0"))
        cls, digest = entries["attention_board.md"]
        assert cls == "LIVE"
        assert len(digest) == 64
        assert digest == pm.sha(mock_package / "attention_board.md")

    def test_parse_ignores_the_lane_policy_table(self, mock_package):
        """`## Lane policy` renders backtick-quoted rows above `## Files`.

        Parsing must not start collecting until `## Files`, or lane names land
        in the entry map as paths that do not exist - and cleanup then reports
        them as missing and tries to restore them.
        """
        text = pm.build(mock_package, "1.0.0")
        assert "| `tickets/` | permissive |" in text, "fixture assumption changed"

        entries = pm.parse(text)
        assert "tickets/" not in entries
        assert not any(cls == "permissive" for cls, _ in entries.values())

    def test_parse_requires_a_64_char_hash(self):
        text = "## Files\n\n| path | class | sha256 |\n| --- | --- | --- |\n" \
               "| `a.md` | PACKAGE | `tooshort` |\n"
        assert pm.parse(text) == {}

    def test_manifest_never_hashes_itself(self, mock_package):
        (mock_package / pm.MANIFEST_NAME).write_bytes(b"# MANIFEST\n")
        entries = pm.parse(pm.build(mock_package, "1.0.0"))
        assert pm.MANIFEST_NAME not in entries

    def test_pycache_is_skipped(self, mock_package):
        (mock_package / "tools" / "__pycache__").mkdir(parents=True)
        (mock_package / "tools" / "__pycache__" / "x.pyc").write_bytes(b"\x00")
        entries = pm.parse(pm.build(mock_package, "1.0.0"))
        assert not any("__pycache__" in k for k in entries)

    def test_version_is_recorded(self, mock_package):
        assert "| package_version | 9.9.9 |" in pm.build(mock_package, "9.9.9")

    def test_build_is_deterministic(self, mock_package):
        """Same tree, same bytes. A manifest that reorders itself produces a
        diff on every run and trains people to ignore manifest diffs."""
        assert pm.build(mock_package, "1.0.0") == pm.build(mock_package, "1.0.0")
