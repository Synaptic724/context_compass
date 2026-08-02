"""index_document end to end: build, verify, slice, and refuse when stale."""

from __future__ import annotations

import pytest

from conftest import TOOLS, run_tool, write

pytestmark = pytest.mark.integration

INDEXER = TOOLS / "system_documents" / "index_document.py"

DOC = """\
# Example Document

## Metadata
- Example type: test

## Scope and Intent
Some prose about scope.
More prose.

## C1 Code Map (Core Only)
- path: `src/a.py`
  start_line: 1
  end_line: 10

## Context / Handoff Summary
The end.
"""


@pytest.fixture
def doc(tmp_path):
    return write(tmp_path / "system_docs" / "example.md", DOC)


def test_build_then_check_then_slice(doc):
    build = run_tool(INDEXER, "--doc", doc)
    assert build.returncode == 0
    assert "WROTE: example_index.md" in build.stdout
    assert (doc.parent / "example_index.md").is_file()

    check = run_tool(INDEXER, "--doc", doc, "--check")
    assert check.returncode == 0
    assert "OK: example_index.md is current" in check.stdout

    sliced = run_tool(INDEXER, "--doc", doc, "--slice", "Scope and Intent")
    assert sliced.returncode == 0
    assert "## Scope and Intent" in sliced.stdout
    assert "Some prose about scope." in sliced.stdout
    assert "## Metadata" not in sliced.stdout, "slice must not bleed into a neighbour"


def test_the_document_is_never_modified(doc):
    before = doc.read_bytes()
    run_tool(INDEXER, "--doc", doc)
    assert doc.read_bytes() == before


def test_editing_the_document_makes_the_index_stale(doc):
    run_tool(INDEXER, "--doc", doc)
    doc.write_bytes(("# Example Document\n\nINSERTED LINE\n" + DOC.split("\n", 1)[1]).encode())

    check = run_tool(INDEXER, "--doc", doc, "--check")
    assert check.returncode == 1
    assert "STALE" in check.stderr


def test_slice_refuses_on_a_stale_index(doc):
    """The failure this whole design exists to prevent: an index that still
    parses, still returns content, and returns the WRONG content."""
    run_tool(INDEXER, "--doc", doc)
    doc.write_bytes((DOC.replace("# Example Document", "# Example Document\n\nSHIFT")).encode())

    sliced = run_tool(INDEXER, "--doc", doc, "--slice", "Scope and Intent")
    assert sliced.returncode == 1
    assert "INDEX STALE - refusing to slice" in sliced.stderr


def test_slice_without_an_index_refuses(doc):
    sliced = run_tool(INDEXER, "--doc", doc, "--slice", "Metadata")
    assert sliced.returncode == 1
    assert "NO INDEX" in sliced.stderr


def test_ambiguous_slice_lists_candidates_rather_than_guessing(tmp_path):
    d = write(tmp_path / "d.md", "# T\n\n## Alpha One\nx\n\n## Alpha Two\ny\n")
    run_tool(INDEXER, "--doc", d)
    sliced = run_tool(INDEXER, "--doc", d, "--slice", "Alpha")
    assert sliced.returncode == 1
    assert "2 sections match" in sliced.stderr
    assert "Alpha One" in sliced.stderr and "Alpha Two" in sliced.stderr


def test_unknown_slice_name_points_at_the_index(doc):
    run_tool(INDEXER, "--doc", doc)
    sliced = run_tool(INDEXER, "--doc", doc, "--slice", "Nonexistent")
    assert sliced.returncode == 1
    assert "no section matching" in sliced.stderr


def test_index_omits_the_document_title(doc):
    run_tool(INDEXER, "--doc", doc)
    index = (doc.parent / "example_index.md").read_text()
    assert "| Example Document |" not in index
    assert "Metadata" in index


def test_rebuild_is_idempotent(doc):
    run_tool(INDEXER, "--doc", doc)
    second = run_tool(INDEXER, "--doc", doc)
    assert "UNCHANGED" in second.stdout


def test_wrapped_heading_warns_on_stderr(tmp_path):
    d = write(tmp_path / "d.md", "# T\n\n## Router and Role Resolution (the\n  chain\nbody\n")
    res = run_tool(INDEXER, "--doc", d)
    assert "FORMAT WARNING" in res.stderr
    assert "unclosed '('" in res.stderr


def test_crlf_document_round_trips(tmp_path):
    """Their venv is on Windows. An indexer that miscounts CRLF lines produces a
    staleness proof that fails on every check."""
    d = tmp_path / "d.md"
    d.write_bytes(DOC.replace("\n", "\r\n").encode())
    assert run_tool(INDEXER, "--doc", d).returncode == 0
    check = run_tool(INDEXER, "--doc", d, "--check")
    assert check.returncode == 0, check.stderr
    assert "| line_ending | crlf |" in (tmp_path / "d_index.md").read_text()


def test_entry_markers_take_precedence_in_auto_mode(tmp_path):
    d = write(tmp_path / "patch.md",
              '# Patch\n\n<!-- BEGIN ENTRY: "Revision 1" -->\nbody\n'
              '<!-- END ENTRY: "Revision 1" -->\n')
    res = run_tool(INDEXER, "--doc", d)
    assert res.returncode == 0
    assert "sectioned by: entry markers" in res.stdout


def test_malformed_entry_markers_write_nothing(tmp_path):
    d = write(tmp_path / "patch.md", '# P\n\n<!-- BEGIN ENTRY: "R1" -->\nbody\n')
    res = run_tool(INDEXER, "--doc", d, "--mode", "entry")
    assert res.returncode == 1
    assert "ENTRY MARKERS MALFORMED" in res.stderr
    assert not (tmp_path / "patch_index.md").exists(), "nothing written on failure"


def test_missing_document_exits_two(tmp_path):
    res = run_tool(INDEXER, "--doc", tmp_path / "nope.md")
    assert res.returncode == 2
    assert "document not found" in res.stderr
