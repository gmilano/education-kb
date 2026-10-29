#!/usr/bin/env python3
"""Offline suite for p523/code_liveness.

Runs with no network. Every fixture is either a commit list read from bytes
this pass (microsoft/autogen) or a control written to pin one behaviour.

Controls carried deliberately:
  * POSITIVE: a repository that ships. Must not be called retired.
  * NEGATIVE: autogen — HEAD one day old, project retired 217 days.
  * The `p520` lesson, one layer out: a probe written to catch a false
    LIVE read must not produce a false RETIRED read. `test_docs_word_in_code_path`
    and `test_readme_shaped_code_file` are that guard.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from code_liveness import announces_retirement, classify, is_docs_only

FAILURES = []


def check(name, cond, detail=""):
    if cond:
        print(f"  ok   {name}")
    else:
        print(f"  FAIL {name} {detail}")
        FAILURES.append(name)


# ---------------------------------------------------------------- fixtures

# Read from bytes 2026-10-29 via `git log --name-only` on a deepened clone.
AUTOGEN = [
    {"date": "2026-10-28", "sha": "d07c667a",
     "subject": "docs: add archive caution to landing page (#8393)",
     "paths": ["docs/index.md", "README.md"]},
    {"date": "2026-10-16", "sha": "004749e6",
     "subject": "docs: clarify AutoGen is archived and no longer maintained- #1 (#8366)",
     "paths": ["README.md"]},
    {"date": "2026-04-06", "sha": "027ecf0a",
     "subject": "Update maintenance mode banner in readme (#7521)",
     "paths": ["README.md"]},
    {"date": "2026-03-25", "sha": "8544314f",
     "subject": "fix: restrict importlib provider loading to trusted namespaces (#7463)",
     "paths": ["python/packages/autogen-core/src/autogen_core/_component_config.py"]},
]

SHIPPING = [
    {"date": "2026-10-28", "sha": "aaaa1111", "subject": "feat: add mastery gate",
     "paths": ["src/tutor/mastery.py"]},
    {"date": "2026-10-20", "sha": "bbbb2222", "subject": "docs: fix typo",
     "paths": ["README.md"]},
]

# Ships code, but the subject happens to use the word "deprecated" about an
# API rather than about the project.
DEPRECATES_AN_API = [
    {"date": "2026-10-28", "sha": "cccc3333",
     "subject": "refactor: remove deprecated FunctionTool shim",
     "paths": ["src/tools/function_tool.py"]},
]

STALE_BUT_NOT_RETIRED = [
    {"date": "2026-10-28", "sha": "dddd4444", "subject": "docs: add install note",
     "paths": ["docs/install.md"]},
    {"date": "2026-02-01", "sha": "eeee5555", "subject": "fix: null deref",
     "paths": ["lib/parse.c"]},
]


# ---------------------------------------------------------------- tests

def test_autogen_is_notices_only():
    v = classify(AUTOGEN)
    check("autogen verdict NOTICES-ONLY", v["verdict"] == "NOTICES-ONLY", v["verdict"])
    check("autogen code date is 2026-03-25", v["code_date"] == "2026-03-25", v["code_date"])
    check("autogen gap is 217d", v["gap_days"] == 217, v["gap_days"])
    check("autogen head is docs-only", v["head_is_docs_only"] is True)
    check("autogen names its retirement 3x",
          len(v["retirement_commits"]) == 3, len(v["retirement_commits"]))


def test_positive_control_ships():
    v = classify(SHIPPING)
    check("shipping verdict SHIPPING", v["verdict"] == "SHIPPING", v["verdict"])
    check("shipping gap 0d", v["gap_days"] == 0, v["gap_days"])


def test_api_deprecation_is_not_project_retirement():
    """Deprecating an API is not retiring the project.

    🔵 The first draft matched any `deprecat*` and flagged this. The gate now
    requires the object of the verb to BE the project, so this is clean at
    both layers: the word does not match, and the HEAD is code anyway."""
    check("'remove deprecated shim' is not a retirement", announces_retirement(
        "refactor: remove deprecated FunctionTool shim") is False)
    check("'deprecate this library' IS a retirement", announces_retirement(
        "chore: deprecate this library") is True)
    v = classify(DEPRECATES_AN_API)
    check("api-deprecation still SHIPPING", v["verdict"] == "SHIPPING", v["verdict"])


def test_stale_code_without_retirement():
    v = classify(STALE_BUT_NOT_RETIRED)
    check("stale verdict STALE-CODE", v["verdict"] == "STALE-CODE", v["verdict"])
    check("stale gap 269d", v["gap_days"] == 269, v["gap_days"])


def test_docs_word_in_code_path():
    """`p520`'s class: the fix for a false-LIVE read must not make a false
    DEAD read. A source file under a directory merely NAMED like docs, or a
    source file whose name contains a docs word, is CODE."""
    check("src/docs_renderer.py is code",
          is_docs_only(["src/docs_renderer.py"]) is False)
    check("lib/readme_parser.go is code",
          is_docs_only(["lib/readme_parser.go"]) is False)
    check("docs/conf.py is docs-dir, counted docs",
          is_docs_only(["docs/conf.py"]) is True)
    check("mixed docs+code is NOT docs-only",
          is_docs_only(["README.md", "src/a.py"]) is False)


def test_readme_shaped_code_file():
    check("README.md is docs", is_docs_only(["README.md"]) is True)
    check("CHANGELOG is docs", is_docs_only(["CHANGELOG"]) is True)
    check("LICENSE is docs", is_docs_only(["LICENSE"]) is True)
    check("a .md under src is still docs",
          is_docs_only(["src/guide.md"]) is True)


def test_empty_and_degenerate():
    check("empty commit list -> no head", classify([])["head_date"] is None)
    check("empty paths is not docs-only", is_docs_only([]) is False)
    check("no retirement word", announces_retirement("feat: add thing") is False)
    v = classify([{"date": "2026-10-01", "sha": "f1", "subject": "docs: x",
                   "paths": ["README.md"]}])
    check("docs-only window with no retirement -> NO-CODE-IN-WINDOW",
          v["verdict"] == "NO-CODE-IN-WINDOW", v["verdict"])


# Read from bytes 2026-10-29. 🔴 These two commits defeated the first draft of
# `announces_retirement` and are kept as permanent negative controls: the repo
# is a 4,119-star MIT asset and the false verdict would have blocked it.
FSRS4ANKI = [
    {"date": "2026-08-14", "sha": "ff7c85c",
     "subject": "Fix broken star history chart (#753)", "paths": ["README.md"]},
    {"date": "2025-09-08", "sha": "c2d8a9d",
     "subject": "Fix/remove evaluation part (#745)",
     "paths": ["fsrs4anki_optimizer.ipynb"]},
    {"date": "2024-11-27", "sha": "30fd9aa",
     "subject": "use archive link of Chinese version of the tutorial2",
     "paths": ["README.md"]},
    {"date": "2024-11-27", "sha": "7b5348a",
     "subject": "use archive link of Chinese version of the tutorial",
     "paths": ["README.md"]},
]


def test_fsrs4anki_archive_link_is_not_retirement():
    """🔴 `p520`'s class, caught by this suite rather than shipped."""
    for sub in ["use archive link of Chinese version of the tutorial",
                "use archive link of Chinese version of the tutorial2",
                "point docs at archive.org copy",
                "switch to archived URL for the dead blog post"]:
        check(f"not a retirement: {sub[:38]!r}",
              announces_retirement(sub) is False)
    v = classify(FSRS4ANKI)
    check("fsrs4anki is NOT notices-only", v["verdict"] != "NOTICES-ONLY", v["verdict"])
    check("fsrs4anki verdict STALE-CODE", v["verdict"] == "STALE-CODE", v["verdict"])
    check("fsrs4anki code date 2025-09-08", v["code_date"] == "2025-09-08", v["code_date"])
    check("fsrs4anki gap 340d", v["gap_days"] == 340, v["gap_days"])
    check("fsrs4anki names no retirement",
          len(v["retirement_commits"]) == 0, v["retirement_commits"])


def test_retirement_phrasings_still_match():
    """The positive side of the same gate must survive the tightening."""
    for sub in ["docs: add archive caution to landing page (#8393)",
                "docs: clarify AutoGen is archived and no longer maintained- #1",
                "Update maintenance mode banner in readme (#7521)",
                "This repository is now read-only mode",
                "chore: deprecate this package in favour of the successor"]:
        check(f"is a retirement: {sub[:38]!r}", announces_retirement(sub) is True)


if __name__ == "__main__":
    for fn in [v for k, v in sorted(globals().items()) if k.startswith("test_")]:
        print(fn.__name__)
        fn()
    print()
    if FAILURES:
        print(f"RED — {len(FAILURES)} failed: {FAILURES}")
        sys.exit(1)
    print("GREEN — all checks passed")
