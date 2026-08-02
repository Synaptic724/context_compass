"""Unit tests for USER-DEFINED regions: the content an upgrade must not eat."""

from __future__ import annotations

import pytest

import cleanup_context_compass as cc

pytestmark = pytest.mark.unit


NEW = """\
# Board
<!-- BEGIN MANAGED: contract -->
NEW package prose.
<!-- END MANAGED: contract -->

## Active Items
| a | b |
| --- | --- |
<!-- BEGIN USER-DEFINED: active_items -->
<!-- END USER-DEFINED: active_items -->
"""

MINE = """\
# Board
<!-- BEGIN MANAGED: contract -->
old package prose.
<!-- END MANAGED: contract -->

## Active Items
| a | b |
| --- | --- |
<!-- BEGIN USER-DEFINED: active_items -->
| my_work | in_progress |
<!-- END USER-DEFINED: active_items -->
"""


class TestUserRegions:
    def test_finds_a_named_region_and_brackets_its_body(self):
        (name, s, e), = cc.user_regions(
            "x\n<!-- BEGIN USER-DEFINED: rows -->\nBODY\n<!-- END USER-DEFINED: rows -->\n")
        assert name == "rows"

    def test_offsets_cover_the_body_not_the_markers(self):
        text = "<!-- BEGIN USER-DEFINED: r -->\nBODY\n<!-- END USER-DEFINED: r -->"
        _, s, e = cc.user_regions(text)[0]
        assert text[s:e] == "\nBODY\n"
        assert "BEGIN" not in text[s:e] and "END" not in text[s:e]

    def test_unnamed_region_is_supported(self):
        (name, _, _), = cc.user_regions(
            "<!-- BEGIN USER-DEFINED -->\nx\n<!-- END USER-DEFINED -->")
        assert name == ""

    def test_several_regions(self):
        text = ("<!-- BEGIN USER-DEFINED: a -->\n1\n<!-- END USER-DEFINED: a -->\n"
                "<!-- BEGIN USER-DEFINED: b -->\n2\n<!-- END USER-DEFINED: b -->\n")
        assert [n for n, _, _ in cc.user_regions(text)] == ["a", "b"]

    def test_unterminated_region_raises_rather_than_guessing(self):
        """Guessing where the install's text ends is how an upgrade eats it."""
        with pytest.raises(ValueError, match="unterminated"):
            cc.user_regions("<!-- BEGIN USER-DEFINED: r -->\nBODY\n")

    def test_no_regions_is_not_an_error(self):
        assert cc.user_regions("# plain board\n") == []


class TestCarryUserRegions:
    def test_package_text_updates_and_my_rows_survive(self):
        merged, carried = cc.carry_user_regions(NEW, MINE)
        assert carried == ["active_items"]
        assert "NEW package prose." in merged
        assert "old package prose." not in merged
        assert "| my_work | in_progress |" in merged

    def test_an_install_with_no_regions_changes_nothing(self):
        merged, carried = cc.carry_user_regions(NEW, "# Board\nno regions here\n")
        assert merged == NEW and carried == []

    def test_identical_regions_report_no_carry(self):
        merged, carried = cc.carry_user_regions(NEW, NEW)
        assert carried == [] and merged == NEW

    def test_a_region_the_new_version_dropped_is_not_reattached(self):
        """Silently reattaching a body to a region that no longer exists puts
        text somewhere nobody expects. It is reported instead."""
        mine = MINE.replace("active_items", "retired_region")
        merged, carried = cc.carry_user_regions(NEW, mine)
        assert carried == []
        assert "| my_work | in_progress |" not in merged
        assert cc.orphaned_user_regions(NEW, mine) == ["retired_region"]

    def test_a_new_region_the_install_lacks_stays_empty(self):
        new = NEW.replace(
            "<!-- END USER-DEFINED: active_items -->",
            "<!-- END USER-DEFINED: active_items -->\n"
            "<!-- BEGIN USER-DEFINED: fresh -->\n<!-- END USER-DEFINED: fresh -->")
        merged, carried = cc.carry_user_regions(new, MINE)
        assert carried == ["active_items"]
        assert "<!-- BEGIN USER-DEFINED: fresh -->\n<!-- END USER-DEFINED: fresh -->" in merged

    def test_multiple_regions_carry_without_corrupting_offsets(self):
        """Back to front. Front to back invalidates every later offset the
        moment one replacement changes length.

        Asserting only that both strings appear somewhere is not enough - a
        corrupted splice leaves them present but in the wrong region, and a
        mutation flipping the sort order survived a test written that way. The
        invariant is that each region ends up holding ITS OWN body.
        """
        new = ("<!-- BEGIN USER-DEFINED: a -->\n<!-- END USER-DEFINED: a -->\n"
               "MIDDLE\n"
               "<!-- BEGIN USER-DEFINED: b -->\n<!-- END USER-DEFINED: b -->\n")
        mine = ("<!-- BEGIN USER-DEFINED: a -->\nAAA LONG CONTENT\n<!-- END USER-DEFINED: a -->\n"
                "MIDDLE\n"
                "<!-- BEGIN USER-DEFINED: b -->\nBBB LONG CONTENT\n<!-- END USER-DEFINED: b -->\n")
        merged, carried = cc.carry_user_regions(new, mine)

        assert set(carried) == {"a", "b"}
        assert "MIDDLE" in merged
        bodies = {name: merged[s:e] for name, s, e in cc.user_regions(merged)}
        assert bodies == {"a": "\nAAA LONG CONTENT\n", "b": "\nBBB LONG CONTENT\n"}

    def test_the_result_is_always_re_parseable(self):
        """A corrupted splice can produce text that still contains every
        expected substring but no longer parses into the regions it claims."""
        new = ("<!-- BEGIN USER-DEFINED: a -->\n<!-- END USER-DEFINED: a -->\n"
               "<!-- BEGIN USER-DEFINED: b -->\n<!-- END USER-DEFINED: b -->\n"
               "<!-- BEGIN USER-DEFINED: c -->\n<!-- END USER-DEFINED: c -->\n")
        mine = new
        for n in ("a", "b", "c"):
            mine = mine.replace(f"<!-- BEGIN USER-DEFINED: {n} -->\n",
                                f"<!-- BEGIN USER-DEFINED: {n} -->\n{n * 40}\n")
        merged, _ = cc.carry_user_regions(new, mine)
        assert [n for n, _, _ in cc.user_regions(merged)] == ["a", "b", "c"]
        assert {n: merged[s:e].strip() for n, s, e in cc.user_regions(merged)} == {
            "a": "a" * 40, "b": "b" * 40, "c": "c" * 40}

    def test_carry_is_idempotent(self):
        once, _ = cc.carry_user_regions(NEW, MINE)
        twice, carried = cc.carry_user_regions(NEW, once)
        assert twice == once
        assert once.count("| my_work | in_progress |") == 1

    def test_region_content_is_carried_byte_for_byte(self):
        """Including whitespace. A board row is data, not prose to tidy."""
        mine = MINE.replace("| my_work | in_progress |",
                            "|  spaced   |   row  |\n\n| second | row |")
        merged, _ = cc.carry_user_regions(NEW, mine)
        assert "|  spaced   |   row  |" in merged
        assert "| second | row |" in merged
