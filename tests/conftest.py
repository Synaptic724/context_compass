"""Shared fixtures.

Two rules this file exists to enforce.

**Nothing here touches the real package.** Every test builds a synthetic install
under pytest's `tmp_path`. The tools under test delete files, and a fixture that
pointed at `src/context_compass/` would eventually eat the thing it was testing.
`no_real_package_writes` fails any test that writes into the repository.

**The mock package is small enough to reason about.** Twelve files covering all
five ownership classes, both lane policies, and a managed block. A fixture built
by copying the real package would make every assertion depend on 440 files that
change for unrelated reasons.
"""

from __future__ import annotations

import hashlib
import pathlib
import subprocess
import sys

import pytest

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
PKG_ROOT = REPO_ROOT / "src" / "context_compass"
TOOLS = PKG_ROOT / "tools"
GRAPH_TOOLS = TOOLS / "system_documents" / "python"

# The tools are scripts, not an installed package, and they import each other by
# sitting on sys.path (cleanup and update both do `sys.path.insert` on their own
# directory). Unit tests import the same way rather than inventing a package
# layout the shipped code does not have.
for _p in (TOOLS, TOOLS / "system_documents", GRAPH_TOOLS):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))


def write(path: pathlib.Path, text: str) -> pathlib.Path:
    """Write UTF-8 with LF endings, deterministically.

    Explicit bytes because the manifest hashes bytes. Letting the platform pick
    a line ending would make every hash assertion pass on Linux and fail on
    Windows, which is the least useful kind of test.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))
    return path


def sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_tool(script: pathlib.Path, *args: object) -> subprocess.CompletedProcess:
    """Run a tool the way a user runs it: as a subprocess, through argparse.

    Integration tests use this instead of calling `main()` directly. Calling
    `main()` would skip argparse, the `sys.path` bootstrap each script performs,
    and the exit-code contract - which is the part downstream automation
    actually depends on.
    """
    return subprocess.run(
        [sys.executable, str(script), *[str(a) for a in args]],
        capture_output=True, text=True,
    )


# --------------------------------------------------------------------------
# The mock package
# --------------------------------------------------------------------------

MANAGED_BOARD = """\
# attention_board

<!-- BEGIN MANAGED: routing -->
Read SKILLS.MD, then your role chain.
<!-- END MANAGED: routing -->

## Rows
| ticket | owner |
| --- | --- |
| T-1 | mark |
"""

CONFIG_YAML = """\
# how documents are read
reading:
  slice_first: true

# system of record behaviour
system_of_record:
  enforce: true
"""


@pytest.fixture
def mock_package(tmp_path: pathlib.Path) -> pathlib.Path:
    """A synthetic install covering every ownership class and both lane policies.

    PACKAGE   AGENTS.MD, SKILLS.MD, tools/thing.py, agent_onboarding/default/...
    RESET     tickets/, system_docs/  (permissive lanes)
    INSTANCE  user_defined/, agent_onboarding/user_defined/
    LIVE      attention_board.md      (carries a managed block)
    CONFIG    config/context_compass_config.yaml
    """
    root = tmp_path / "pkg"
    write(root / "AGENTS.MD", "# AGENTS\n\nEntrypoint.\n")
    write(root / "SKILLS.MD", "# SKILLS.MD\n\n| role | path |\n| --- | --- |\n")
    write(root / "tools" / "thing.py", "print('hello')\n")
    write(root / "agent_onboarding" / "default" / "engineer" / "SKILLS.MD",
          "# SKILLS.MD - engineer\n")
    write(root / "agent_onboarding" / "default" / "engineer" / "skills" / "a.md",
          "# skill a\n")
    write(root / "attention_board.md", MANAGED_BOARD)
    write(root / "config" / "context_compass_config.yaml", CONFIG_YAML)
    write(root / "tickets" / "tasks" / "README.md", "# tasks lane\n")
    write(root / "system_docs" / ".gitkeep", "")
    write(root / "user_defined" / "README.md", "# user_defined\n")
    write(root / "agent_onboarding" / "user_defined" / "myrole" / "SKILLS.MD",
          "# SKILLS.MD - myrole\n")
    return root


@pytest.fixture
def manifested(mock_package: pathlib.Path) -> pathlib.Path:
    """`mock_package` with a current MANIFEST.md, i.e. a clean install."""
    import package_manifest as pm
    (mock_package / pm.MANIFEST_NAME).write_bytes(
        pm.build(mock_package, "1.0.0").encode("utf-8"))
    return mock_package


@pytest.fixture
def mock_source_tree(tmp_path: pathlib.Path) -> pathlib.Path:
    """A tiny Python package for the graph pipeline to extract from.

    Shaped to exercise the extractor's real decisions: a Protocol (interface),
    an ABC (deliberately NOT an interface), an Enum, a plain class with a base,
    and a class holding references that are syntactically identical whether it
    owns them or borrows them - which is the whole reason the authored tier
    exists.
    """
    src = tmp_path / "src"
    write(src / "app" / "__init__.py", "")
    write(src / "app" / "core" / "__init__.py", "")
    write(src / "app" / "core" / "iface.py", '''\
"""Contracts."""
from typing import Protocol
from abc import ABC


class IStore(Protocol):
    def get(self, key: str) -> str: ...


class BaseWorker(ABC):
    def run(self) -> None: ...
''')
    write(src / "app" / "core" / "kinds.py", '''\
from enum import Enum


class Phase(Enum):
    INIT = "init"
    RUN = "run"
''')
    write(src / "app" / "engine.py", '''\
from app.core.iface import BaseWorker


class Engine(BaseWorker):
    """Holds a stage list and a store. The AST cannot tell owned from borrowed."""

    def __init__(self, store):
        self.store = store
        self.stages = [Stage()]

    def run(self) -> None: ...

    def stop(self) -> None: ...


class Stage:
    def apply(self) -> None: ...
''')
    return src


@pytest.fixture(scope="session", autouse=True)
def no_real_package_writes():
    """Fail the run if anything modified the repository it is testing.

    The tools under test delete files and take an `--apply` flag. This is the
    net under a fixture typo that points one of them at the real package.

    Session-scoped on purpose. Per-test it hashed 445 files twice per test -
    about three minutes of the suite's runtime doing nothing but proving the
    same thing sixty times over. Once per run catches the same disaster; it just
    names the run rather than the test, which is a fair trade for a net that
    should never fire.
    """
    def snapshot() -> dict[str, str]:
        return {
            p.relative_to(REPO_ROOT).as_posix(): sha(p)
            for p in PKG_ROOT.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts
        }

    before = snapshot()
    yield
    after = snapshot()
    changed = ([f"modified {k}" for k in before.keys() & after.keys()
                if before[k] != after[k]]
               + [f"deleted {k}" for k in before.keys() - after.keys()]
               + [f"created {k}" for k in after.keys() - before.keys()])
    assert not changed, (
        "the suite wrote into the real package:\n  " + "\n  ".join(sorted(changed)))
