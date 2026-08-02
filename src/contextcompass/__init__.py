"""Context Compass - durable, file-backed execution state for coding agents.

This module is the INSTALLER and CLI. It is deliberately not named
`context_compass`, because every repository that uses Context Compass has a
directory of exactly that name at its top level. Two things claiming one import
name resolve differently depending on how Python was invoked - the local folder
wins from the repo root, the installed package wins from anywhere else - so the
name is kept distinct and no collision is possible.

The package payload (the ~440 files that get copied into a repository) ships
inside this module as `_package/`.
"""

from __future__ import annotations

import pathlib

# Single source of truth for the version. `MANIFEST.md` inside the payload
# records the same number, and a test asserts they agree - a version maintained
# in two places is a version that will disagree, which is the whole reason the
# manifest is derived rather than declared.
__version__ = "2.12.0"

INSTALL_DIRNAME = "context_compass"

_HERE = pathlib.Path(__file__).resolve().parent


def _find_payload() -> pathlib.Path:
    """Where the shipped package files live, installed or in a source checkout.

    In a wheel the build maps `src/context_compass/` to `_package/` beside this
    module. In a source tree that directory does not exist - the payload is the
    sibling `src/context_compass/`. Without this fallback the CLI works only
    after a build, so every source-run and every test would exercise a different
    code path from the one users get.
    """
    installed = _HERE / "_package"
    if (installed / "AGENTS.MD").is_file():
        return installed
    checkout = _HERE.parent / INSTALL_DIRNAME
    if (checkout / "AGENTS.MD").is_file():
        return checkout
    return installed          # report the installed path in the error message


PAYLOAD = _find_payload()

__all__ = ["__version__", "PAYLOAD", "INSTALL_DIRNAME"]
