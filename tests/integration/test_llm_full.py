"""build_llm_full: the document, its byproduct index, and the slice contract.

The index is emitted by the same pass that writes the document, so the two
cannot disagree - but "cannot" is a claim, and this is what turns it into a
tested one.
"""

from __future__ import annotations

import hashlib
import re

import pytest

from conftest import TOOLS, run_tool, write

pytestmark = pytest.mark.integration

BUILDER = TOOLS / "build_llm_full.py"
ROW = re.compile(r"^\| (\d+)-(\d+) \| `([^`]+)` \| (\d+) \| (\d+) \|", re.M)


@pytest.fixture
def built(mock_package, tmp_path):
    out = tmp_path / "llm_full.md"
    res = run_tool(BUILDER, "--root", mock_package, "--out", out)
    assert res.returncode == 0, res.stderr
    return mock_package, out, out.with_name("llm_full_index.md")


class TestBuild:
    def test_writes_document_and_index(self, built):
        _, doc, index = built
        assert doc.is_file() and index.is_file()

    def test_every_package_file_appears_once(self, built):
        pkg, doc, index = built
        on_disk = {f"context_compass/{p.relative_to(pkg).as_posix()}"
                   for p in pkg.rglob("*") if p.is_file()}
        rows = ROW.findall(index.read_text())
        assert {r[2] for r in rows} == on_disk
        assert len(rows) == len(on_disk), "a file indexed twice"

    def test_the_builders_own_marker_is_not_counted(self, built):
        """This script ships inside the package, so it is inlined into its own
        output. A literal marker in its source is indistinguishable from a real
        delimiter - the first version emitted 443 markers for 442 files."""
        _, doc, index = built
        text = doc.read_text()
        rows = ROW.findall(index.read_text())
        assert text.count("--- START OF FILE: ") == len(rows)
        assert text.count("--- END OF FILE: ") == len(rows)

    def test_regeneration_is_idempotent(self, built):
        pkg, doc, index = built
        before = (doc.read_bytes(), index.read_bytes())
        run_tool(BUILDER, "--root", pkg, "--out", doc)
        assert (doc.read_bytes(), index.read_bytes()) == before

    def test_refuses_a_root_that_is_not_a_package(self, tmp_path):
        res = run_tool(BUILDER, "--root", tmp_path, "--out", tmp_path / "x.md")
        assert res.returncode == 2
        assert "not a package root" in res.stdout


class TestIndexAddressesTheDocument:
    def test_every_range_lands_on_its_own_markers(self, built):
        _, doc, index = built
        lines = doc.read_text().split("\n")
        for start, end, path, span, _ in ROW.findall(index.read_text()):
            assert lines[int(start) - 1] == f"--- START OF FILE: {path} ---"
            assert lines[int(end) - 1] == f"--- END OF FILE: {path} ---"
            assert int(end) - int(start) + 1 == int(span)

    def test_ranges_do_not_overlap(self, built):
        _, doc, index = built
        rows = [(int(a), int(b)) for a, b, _, _, _ in ROW.findall(index.read_text())]
        for (_, prev_end), (nxt_start, _) in zip(rows, rows[1:]):
            assert prev_end < nxt_start

    def test_a_sliced_range_round_trips_to_the_file_on_disk(self, built):
        pkg, doc, index = built
        lines = doc.read_text().split("\n")
        for start, end, path, _, _ in ROW.findall(index.read_text()):
            rel = path.split("/", 1)[1]
            body = "\n".join(lines[int(start):int(end) - 1]).strip()
            assert body == (pkg / rel).read_text().strip(), f"{path} did not round-trip"

    def test_staleness_proof_matches_the_document(self, built):
        _, doc, index = built
        raw = doc.read_text()
        text = index.read_text()
        assert hashlib.sha256(raw.encode()).hexdigest() in text
        live = len(raw.split("\n")) - (1 if raw.endswith("\n") else 0)
        assert f"| line_count | {live} |" in text


class TestSlice:
    def test_slices_one_file_by_path_substring(self, built):
        pkg, doc, _ = built
        res = run_tool(BUILDER, "--root", pkg, "--out", doc,
                       "--slice", "user_defined/README.md")
        assert res.returncode == 0, res.stderr
        assert "# user_defined" in res.stdout
        assert "--- START OF FILE:" in res.stdout

    def test_an_ambiguous_name_lists_candidates_rather_than_guessing(self, built):
        """`SKILLS.MD` matches three files in the mock package and 19 in the
        real one. Refusing costs a round trip; guessing costs the wrong file."""
        pkg, doc, _ = built
        res = run_tool(BUILDER, "--root", pkg, "--out", doc, "--slice", "SKILLS.MD")
        assert res.returncode == 1
        assert "files match" in res.stderr
        assert "context_compass/SKILLS.MD" in res.stderr, "candidates must be listed"

    def test_a_fully_qualified_path_disambiguates(self, built):
        pkg, doc, _ = built
        res = run_tool(BUILDER, "--root", pkg, "--out", doc,
                       "--slice", "context_compass/SKILLS.MD")
        assert res.returncode == 0, res.stderr

    def test_an_unknown_name_points_at_the_index(self, built):
        pkg, doc, _ = built
        res = run_tool(BUILDER, "--root", pkg, "--out", doc, "--slice", "nope.txt")
        assert res.returncode == 1
        assert "no file matching" in res.stderr

    def test_slice_refuses_when_the_document_moved(self, built):
        """The failure the staleness proof exists for: the index still parses,
        still returns content, and returns the WRONG content."""
        pkg, doc, _ = built
        doc.write_bytes(b"INSERTED LINE\n" + doc.read_bytes())
        res = run_tool(BUILDER, "--root", pkg, "--out", doc, "--slice", "SKILLS.MD")
        assert res.returncode == 1
        assert "INDEX STALE" in res.stderr


class TestCheck:
    def test_reports_current(self, built):
        pkg, doc, _ = built
        res = run_tool(BUILDER, "--root", pkg, "--out", doc, "--check")
        assert res.returncode == 0
        assert "are current" in res.stdout

    def test_detects_an_edited_document(self, built):
        pkg, doc, _ = built
        doc.write_bytes(doc.read_bytes() + b"\nhand-edited\n")
        res = run_tool(BUILDER, "--root", pkg, "--out", doc, "--check")
        assert res.returncode == 1
        assert "STALE" in res.stdout

    def test_detects_a_changed_package(self, built):
        pkg, doc, _ = built
        write(pkg / "tools" / "brand_new.py", "x = 1\n")
        res = run_tool(BUILDER, "--root", pkg, "--out", doc, "--check")
        assert res.returncode == 1

    def test_check_writes_nothing(self, built):
        pkg, doc, index = built
        doc.write_bytes(doc.read_bytes() + b"\nedited\n")
        before = (doc.read_bytes(), index.read_bytes())
        run_tool(BUILDER, "--root", pkg, "--out", doc, "--check")
        assert (doc.read_bytes(), index.read_bytes()) == before

    def test_missing_files_are_reported(self, built):
        pkg, doc, index = built
        index.unlink()
        res = run_tool(BUILDER, "--root", pkg, "--out", doc, "--check")
        assert res.returncode == 1
        assert "MISSING" in res.stdout


class TestSkillIsRegistered:
    def test_the_reading_skill_ships_and_is_declared(self):
        from conftest import PKG_ROOT
        skill = PKG_ROOT / "agent_onboarding/default/general/skills/llm_full_usage.md"
        registry = PKG_ROOT / "agent_onboarding/default/general/SKILLS.MD"
        assert skill.is_file()
        assert "llm_full_usage.md" in registry.read_text(encoding="utf-8")

    def test_it_is_on_demand_not_baseline(self):
        """Most installs have no llm_full.md. Teaching a procedure with nothing
        to apply it to is baseline reading spent for nothing."""
        from conftest import PKG_ROOT
        registry = (PKG_ROOT / "agent_onboarding/default/general/SKILLS.MD"
                    ).read_text(encoding="utf-8")
        head, _, tail = registry.partition("On-demand skills")
        assert "llm_full_usage.md" in tail
        assert "llm_full_usage.md" not in head
        assert "Trigger:" in tail
