"""Unit tests for cleanup_context_compass: managed blocks and config diffing."""

from __future__ import annotations

import pytest

import cleanup_context_compass as cc

pytestmark = pytest.mark.unit


REF = """\
# attention_board

<!-- BEGIN MANAGED: routing -->
NEW routing text.
<!-- END MANAGED: routing -->

## Rows
"""


class TestManagedBlocks:
    def test_finds_a_block_with_its_bounds(self):
        text = "a\n<!-- BEGIN MANAGED: x -->\nbody\n<!-- END MANAGED: x -->\nz\n"
        (name, start, end), = cc.managed_blocks(text)
        assert name == "x"
        assert text[start:end] == "<!-- BEGIN MANAGED: x -->\nbody\n<!-- END MANAGED: x -->"

    def test_finds_several(self):
        text = ("<!-- BEGIN MANAGED: a -->\n1\n<!-- END MANAGED: a -->\n"
                "<!-- BEGIN MANAGED: b -->\n2\n<!-- END MANAGED: b -->\n")
        assert [n for n, _, _ in cc.managed_blocks(text)] == ["a", "b"]

    def test_unterminated_block_raises_rather_than_guessing(self):
        """Guessing the end of a managed block means swapping text the package
        does not own."""
        with pytest.raises(ValueError, match="unterminated"):
            cc.managed_blocks("<!-- BEGIN MANAGED: x -->\nbody\n")

    def test_no_blocks_is_not_an_error(self):
        assert cc.managed_blocks("plain text\n") == []

    def test_end_marker_must_match_its_own_name(self):
        """`END MANAGED: other` does not close `x`, so `x` is unterminated."""
        with pytest.raises(ValueError, match="unterminated"):
            cc.managed_blocks("<!-- BEGIN MANAGED: x -->\n<!-- END MANAGED: other -->\n")


class TestSwapManaged:
    def test_block_is_replaced_and_named(self):
        current = ("# attention_board\n\n<!-- BEGIN MANAGED: routing -->\n"
                   "OLD routing text.\n<!-- END MANAGED: routing -->\n\n## Rows\n")
        out, changed = cc.swap_managed(current, REF)
        assert changed == ["routing"]
        assert "NEW routing text." in out
        assert "OLD routing text." not in out

    def test_instance_content_outside_the_block_survives(self):
        """The whole point of a LIVE file: the package owns the block, the
        install owns the rows."""
        current = ("# attention_board\n\n<!-- BEGIN MANAGED: routing -->\nOLD\n"
                   "<!-- END MANAGED: routing -->\n\n## Rows\n| T-1 | mark |\n")
        out, _ = cc.swap_managed(current, REF)
        assert "| T-1 | mark |" in out

    def test_identical_block_reports_no_change(self):
        out, changed = cc.swap_managed(REF, REF)
        assert changed == []
        assert out == REF

    def test_missing_block_is_inserted_after_the_h1(self):
        out, changed = cc.swap_managed("# attention_board\n\n## Rows\n", REF)
        assert changed == ["routing (inserted)"]
        assert out.split("\n")[0] == "# attention_board"
        assert "NEW routing text." in out

    def test_missing_block_without_an_h1_goes_to_the_top(self):
        out, changed = cc.swap_managed("no title here\n", REF)
        assert changed == ["routing (inserted)"]
        assert out.startswith("<!-- BEGIN MANAGED: routing -->")

    def test_block_the_reference_does_not_have_is_left_alone(self):
        """Deleting text the package no longer manages is not this tool's
        business - it is the install's content now."""
        current = ("# b\n\n<!-- BEGIN MANAGED: routing -->\nOLD\n<!-- END MANAGED: routing -->\n"
                   "<!-- BEGIN MANAGED: mine -->\nKEEP ME\n<!-- END MANAGED: mine -->\n")
        out, changed = cc.swap_managed(current, REF)
        assert "KEEP ME" in out
        assert "mine" not in changed

    def test_multiple_blocks_swap_without_corrupting_offsets(self):
        """Blocks are replaced back-to-front. Front-to-back invalidates every
        later offset the moment the first replacement changes length."""
        ref = ("<!-- BEGIN MANAGED: a -->\nAAAA-LONGER\n<!-- END MANAGED: a -->\n"
               "<!-- BEGIN MANAGED: b -->\nBBBB-LONGER\n<!-- END MANAGED: b -->\n")
        current = ("<!-- BEGIN MANAGED: a -->\na\n<!-- END MANAGED: a -->\n"
                   "MIDDLE\n"
                   "<!-- BEGIN MANAGED: b -->\nb\n<!-- END MANAGED: b -->\n")
        out, changed = cc.swap_managed(current, ref)
        assert set(changed) == {"a", "b"}
        assert "AAAA-LONGER" in out and "BBBB-LONGER" in out
        assert "MIDDLE" in out


SHIPPED_CFG = """\
reading:
  slice_first: true

system_of_record:
  enforce: true

logging:
  level: info
"""


class TestDiffConfigKeys:
    def test_identical_config_reports_nothing(self):
        assert cc.diff_config_keys(SHIPPED_CFG, SHIPPED_CFG) == ([], [], [])

    def test_added_key_is_reported(self):
        added, removed, retuned = cc.diff_config_keys(
            SHIPPED_CFG + "\nmine:\n  x: 1\n", SHIPPED_CFG)
        assert added == ["mine"] and removed == [] and retuned == []

    def test_removed_key_is_reported(self):
        current = "reading:\n  slice_first: true\n\nsystem_of_record:\n  enforce: true\n"
        added, removed, retuned = cc.diff_config_keys(current, SHIPPED_CFG)
        assert removed == ["logging"]

    def test_changed_value_is_reported(self):
        current = SHIPPED_CFG.replace("enforce: true", "enforce: false")
        added, removed, retuned = cc.diff_config_keys(current, SHIPPED_CFG)
        assert retuned == ["system_of_record"]

    def test_comment_and_blank_line_changes_are_not_drift(self):
        """A reformat is not a retune. Reporting it teaches people to ignore
        the config drift line."""
        current = "# my note\nreading:\n\n  slice_first: true\n\n" \
                  "system_of_record:\n  enforce: true\n\nlogging:\n  level: info\n"
        assert cc.diff_config_keys(current, SHIPPED_CFG) == ([], [], [])

    def test_nested_keys_are_not_mistaken_for_top_level(self):
        """Only column-zero keys are top level. An indented `enforce:` must not
        register as its own block."""
        current = "reading:\n  slice_first: true\n  enforce: true\n"
        added, removed, _ = cc.diff_config_keys(current, "reading:\n  slice_first: true\n")
        assert added == [] and removed == []
