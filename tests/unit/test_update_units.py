"""Unit tests for update_context_compass: YAML block scanning and config merge."""

from __future__ import annotations

import pytest

import update_context_compass as up

pytestmark = pytest.mark.unit


class TestTopLevelKeys:
    def test_finds_each_top_level_block(self):
        text = "a:\n  x: 1\nb:\n  y: 2\n"
        keys = up.top_level_keys(text)
        assert set(keys) == {"a", "b"}
        assert keys["a"] == (0, 2)
        assert keys["b"] == (2, 4)

    def test_indented_keys_are_not_top_level(self):
        keys = up.top_level_keys("a:\n  nested:\n    deep: 1\n")
        assert set(keys) == {"a"}

    def test_trailing_blank_lines_are_excluded_from_a_block(self):
        """A block that swallows the blank lines after it gets re-emitted with
        them, and each merge grows the file."""
        text = "a:\n  x: 1\n\n\nb:\n  y: 2\n"
        assert up.top_level_keys(text)["a"] == (0, 2)

    def test_last_block_runs_to_end_of_text(self):
        assert up.top_level_keys("a:\n  x: 1\nb:\n  y: 2\n")["b"][1] == 4

    def test_keys_with_underscores_and_digits(self):
        keys = up.top_level_keys("system_of_record:\n  enforce: true\nv2_thing:\n  a: 1\n")
        assert set(keys) == {"system_of_record", "v2_thing"}

    def test_comments_are_not_keys(self):
        assert set(up.top_level_keys("# note: a thing\na:\n  x: 1\n")) == {"a"}

    def test_list_items_are_not_keys(self):
        assert set(up.top_level_keys("a:\n- item: 1\n")) == {"a"}


class TestMergeConfig:
    def test_new_key_is_added(self):
        current = "a:\n  x: 1\n"
        new = "a:\n  x: 1\nb:\n  y: 2\n"
        merged, added, dropped = up.merge_config(current, new)
        assert added == ["b"] and dropped == []
        assert "b:" in merged and "y: 2" in merged

    def test_existing_value_is_never_overwritten(self):
        """The whole contract of CONFIG. Adding a key must not silently reset a
        value the user set."""
        current = "a:\n  x: MINE\n"
        new = "a:\n  x: STOCK\nb:\n  y: 2\n"
        merged, added, _ = up.merge_config(current, new)
        assert "x: MINE" in merged
        assert "x: STOCK" not in merged
        assert added == ["b"]

    def test_key_dropped_upstream_is_reported_not_deleted(self):
        current = "a:\n  x: 1\nold:\n  z: 9\n"
        new = "a:\n  x: 1\n"
        merged, added, dropped = up.merge_config(current, new)
        assert dropped == ["old"]
        assert "old:" in merged, "reported, never removed"

    def test_nothing_to_do_leaves_the_text_untouched(self):
        current = "a:\n  x: 1\n"
        merged, added, dropped = up.merge_config(current, current)
        assert (added, dropped) == ([], [])
        assert merged == current

    def test_the_comment_above_a_new_key_comes_with_it(self):
        """A key arriving without its explanation is a key nobody knows how to
        set. The merge is deliberately textual so comments survive."""
        current = "a:\n  x: 1\n"
        new = "a:\n  x: 1\n\n# what b does and why you might change it\nb:\n  y: 2\n"
        merged, added, _ = up.merge_config(current, new)
        assert added == ["b"]
        assert "# what b does and why you might change it" in merged

    def test_user_comments_and_formatting_survive_a_merge(self):
        """Reformatting someone's config is a worse outcome than not merging."""
        current = "# MY NOTES\na:\n  x: 1   # keep this inline note\n"
        new = "a:\n  x: 1\nb:\n  y: 2\n"
        merged, _, _ = up.merge_config(current, new)
        assert "# MY NOTES" in merged
        assert "# keep this inline note" in merged

    def test_merge_is_idempotent(self):
        """Running an upgrade twice must not append the same block twice."""
        current, new = "a:\n  x: 1\n", "a:\n  x: 1\nb:\n  y: 2\n"
        once, _, _ = up.merge_config(current, new)
        twice, added, _ = up.merge_config(once, new)
        assert added == []
        assert twice.count("b:") == 1


class TestShaBytes:
    def test_matches_hashlib(self):
        import hashlib
        assert up.sha_bytes(b"abc") == hashlib.sha256(b"abc").hexdigest()

    def test_byte_sensitive_to_line_endings(self):
        """CRLF and LF are different files to the manifest, which is why the
        tools write bytes explicitly rather than letting the platform choose."""
        assert up.sha_bytes(b"a\r\nb\r\n") != up.sha_bytes(b"a\nb\n")
