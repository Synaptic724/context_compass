"""Unit tests for index_document: heading scan, sectioning, warnings, validation."""

from __future__ import annotations

import pytest

import index_document as idx

pytestmark = pytest.mark.unit


def lines_of(text: str) -> list[str]:
    out = text.split("\n")
    if out and out[-1] == "":
        out.pop()
    return out


class TestFindHeadings:
    def test_basic_scan(self):
        found = idx.find_headings(lines_of("# T\n\n## A\n\n### B\n"), max_level=3)
        assert found == [(1, 1, "T"), (3, 2, "A"), (5, 3, "B")]

    def test_max_level_is_respected(self):
        found = idx.find_headings(lines_of("# T\n## A\n### B\n"), max_level=2)
        assert [t for _, _, t in found] == ["T", "A"]

    def test_hash_inside_a_fence_is_not_a_heading(self):
        """A `#` in a code block is a comment or a shell prompt.

        Treating it as a heading splits the code example in half and produces a
        section whose range starts mid-fence.
        """
        doc = "# T\n\n## Real\n\n```bash\n# not a heading\ngrep -n '^## ' f.md\n```\n\n## Also Real\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        assert [t for _, _, t in found] == ["T", "Real", "Also Real"]

    def test_tilde_fences_count_too(self):
        doc = "# T\n\n~~~\n# nope\n~~~\n\n## Yes\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        assert [t for _, _, t in found] == ["T", "Yes"]

    def test_trailing_whitespace_is_stripped_from_titles(self):
        found = idx.find_headings(lines_of("# T\n## A   \n"), max_level=3)
        assert found[1][2] == "A"


class TestBuildSections:
    def test_lone_h1_is_omitted_as_the_document_title(self):
        """The title's range spans the whole file. Indexing it gives a reader a
        row whose only use is to load everything while believing they sliced."""
        doc = "# Title\n\n## A\n\n## B\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        sections = idx.build_sections(lines_of(doc), found)
        assert [s["title"] for s in sections] == ["A", "B"]

    def test_section_runs_to_the_line_before_the_next_peer(self):
        doc = "# T\n\n## A\nbody\nbody\n\n## B\ntail\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        a, b = idx.build_sections(lines_of(doc), found)
        assert (a["start"], a["end"]) == (3, 6)
        assert (b["start"], b["end"]) == (7, 8)

    def test_deeper_headings_nest_rather_than_terminate(self):
        doc = "# T\n\n## A\n\n### A1\nx\n\n## B\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        sections = idx.build_sections(lines_of(doc), found)
        a = next(s for s in sections if s["title"] == "A")
        assert a["end"] == 7, "H3 must not close its parent H2"

    def test_breadcrumbs_drop_the_repeated_document_title(self):
        doc = "# Title\n\n## A\n\n### A1\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        sections = idx.build_sections(lines_of(doc), found)
        assert [s["path"] for s in sections] == ["A", "A > A1"]

    def test_last_section_runs_to_end_of_file(self):
        doc = "# T\n\n## A\nx\ny\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        assert idx.build_sections(lines_of(doc), found)[0]["end"] == 5

    def test_no_headings_yields_no_sections(self):
        assert idx.build_sections(["just prose"], []) == []

    def test_two_h1s_means_neither_is_treated_as_the_title(self):
        doc = "# One\n\n## A\n\n# Two\n\n## B\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        titles = [s["title"] for s in idx.build_sections(lines_of(doc), found)]
        assert "One" in titles and "Two" in titles


class TestFormatWarnings:
    def test_unclosed_bracket_flags_a_wrapped_heading(self):
        """A reflowed heading parses as several sections; the first wins
        `--slice`'s narrowest match and returns a one-line stub. Unbalanced
        brackets are the reliable tell."""
        doc = "# T\n\n## Router and Role Resolution (the chain\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        sections = idx.build_sections(lines_of(doc), found)
        warnings = idx.format_warnings(lines_of(doc), found, sections)
        assert any("unclosed '('" in w for w in warnings)

    def test_balanced_brackets_do_not_warn(self):
        doc = "# T\n\n## C1 Code Map (Core Only)\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        sections = idx.build_sections(lines_of(doc), found)
        assert idx.format_warnings(lines_of(doc), found, sections) == []

    def test_unclosed_square_bracket_also_warns(self):
        doc = "# T\n\n## Something [see also\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        sections = idx.build_sections(lines_of(doc), found)
        assert any("unclosed '['" in w
                   for w in idx.format_warnings(lines_of(doc), found, sections))

    def test_multiple_h1_warns(self):
        doc = "# One\n\n# Two\n\n## A\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        sections = idx.build_sections(lines_of(doc), found)
        assert any("level-1 headings" in w
                   for w in idx.format_warnings(lines_of(doc), found, sections))

    def test_duplicate_names_warn_because_slice_cannot_address_them(self):
        doc = "# T\n\n## Nodes\nx\n\n## Nodes\ny\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        sections = idx.build_sections(lines_of(doc), found)
        assert any("duplicate section name" in w
                   for w in idx.format_warnings(lines_of(doc), found, sections))


class TestValidate:
    def test_clean_sections_validate(self):
        doc = "# T\n\n## A\nx\n"
        found = idx.find_headings(lines_of(doc), max_level=3)
        sections = [dict(s, kind="heading")
                    for s in idx.build_sections(lines_of(doc), found)]
        assert idx.validate(lines_of(doc), sections) == []

    def test_off_by_one_start_is_caught(self):
        """The failure that silently corrupts every downstream read."""
        doc = "# T\n\n## A\nx\n"
        sections = [{"level": 2, "path": "A", "title": "A",
                     "start": 4, "end": 4, "kind": "heading"}]
        problems = idx.validate(lines_of(doc), sections)
        assert problems and "expected heading" in problems[0]

    def test_out_of_bounds_range_is_caught(self):
        doc = "# T\n\n## A\nx\n"
        sections = [{"level": 2, "path": "A", "title": "A",
                     "start": 3, "end": 99, "kind": "heading"}]
        assert any("out of bounds" in p for p in idx.validate(lines_of(doc), sections))

    def test_non_monotonic_sections_are_caught(self):
        doc = "# T\n\n## A\n\n## B\n"
        sections = [
            {"level": 2, "path": "B", "title": "B", "start": 5, "end": 5, "kind": "heading"},
            {"level": 2, "path": "A", "title": "A", "start": 3, "end": 3, "kind": "heading"},
        ]
        assert any("non-monotonic" in p for p in idx.validate(lines_of(doc), sections))


class TestEntryMarkers:
    def test_entries_are_found_and_named(self):
        doc = ('# Patches\n\n<!-- BEGIN ENTRY: "Revision 1" -->\nbody\n'
               '<!-- END ENTRY: "Revision 1" -->\n')
        entries, problems = idx.find_entries(lines_of(doc))
        assert problems == []
        assert entries[0]["title"] == "Revision 1"
        assert (entries[0]["start"], entries[0]["end"]) == (3, 5)

    def test_unclosed_entry_is_reported_not_guessed(self):
        doc = '<!-- BEGIN ENTRY: "R1" -->\nbody\n'
        _, problems = idx.find_entries(lines_of(doc))
        assert any("never closed" in p for p in problems)

    def test_mismatched_close_is_reported(self):
        doc = '<!-- BEGIN ENTRY: "R1" -->\n<!-- END ENTRY: "R2" -->\n'
        _, problems = idx.find_entries(lines_of(doc))
        assert any("closes" in p for p in problems)

    def test_nested_begin_is_reported(self):
        doc = ('<!-- BEGIN ENTRY: "R1" -->\n<!-- BEGIN ENTRY: "R2" -->\n'
               '<!-- END ENTRY: "R2" -->\n')
        _, problems = idx.find_entries(lines_of(doc))
        assert any("still open" in p for p in problems)

    def test_stray_end_is_reported(self):
        _, problems = idx.find_entries(lines_of('<!-- END ENTRY: "R1" -->\n'))
        assert any("nothing open" in p for p in problems)


class TestReadLines:
    def test_crlf_is_detected(self, tmp_path):
        p = tmp_path / "d.md"
        p.write_bytes(b"# T\r\n\r\n## A\r\n")
        _, ending, lines = idx.read_lines(p)
        assert ending == "crlf"
        assert lines == ["# T", "", "## A"]

    def test_lf_is_detected(self, tmp_path):
        p = tmp_path / "d.md"
        p.write_bytes(b"# T\n\n## A\n")
        _, ending, lines = idx.read_lines(p)
        assert ending == "lf"
        assert lines == ["# T", "", "## A"]

    def test_trailing_terminator_is_not_a_line(self, tmp_path):
        """`line_count` is a staleness proof. Counting a phantom final line
        makes every freshly written index disagree with its own document."""
        p = tmp_path / "d.md"
        p.write_bytes(b"a\nb\n")
        assert idx.read_lines(p)[2] == ["a", "b"]


class TestWriteIfChanged:
    def test_identical_content_is_not_rewritten(self, tmp_path):
        p = tmp_path / "i.md"
        assert idx.write_if_changed(p, "| generated_at | T1 |\nbody\n") is True
        assert idx.write_if_changed(p, "| generated_at | T1 |\nbody\n") is False

    def test_timestamp_only_change_is_not_a_rewrite(self, tmp_path):
        """Otherwise every verification pass produces a diff that says nothing
        happened, and people stop reading index diffs."""
        p = tmp_path / "i.md"
        idx.write_if_changed(p, "| generated_at | T1 |\nbody\n")
        assert idx.write_if_changed(p, "| generated_at | T2 |\nbody\n") is False

    def test_real_change_is_written(self, tmp_path):
        p = tmp_path / "i.md"
        idx.write_if_changed(p, "| generated_at | T1 |\nbody\n")
        assert idx.write_if_changed(p, "| generated_at | T1 |\nDIFFERENT\n") is True
