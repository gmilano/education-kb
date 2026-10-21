#!/usr/bin/env python3
"""`p371-backlog-grade` controls — the denominator `Gap 477` published without a list.

🔴 WHY A GATE AND NOT A ONE-OFF. `Gap 477` reads *"63 of the 2 311-address promotion
backlog are now graded; **2 248** are not."* 🟢 Derived at `p371` from the same shelves,
the remainder is **1 859**. Neither figure is wrong *as arithmetic* — `2 311 - 63 = 2 248`
— but the 2 311 counted strings that are not addresses and addresses that the live
shelves already carry. 🔵 **A quantity published without the list it was counted from
cannot be checked, and this base has a rule for exactly that (`T37`/`recount`): every
registered quantity must be re-derivable from the rows.** This suite makes the
denominator re-derivable.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_backlog import shape_ok, fold  # noqa: E402

FAILED = []


def check(name, got, want):
    if got != want:
        FAILED.append(f"{name}\n      got  {got!r}\n      want {want!r}")


def t_a_real_address_passes():
    for slug in ["HKUDS/DeepTutor", "openedx/XBlock", "ls1intum/Artemis",
                 "open-spaced-repetition/py-fsrs", "oat-sa/tao-core",
                 "3121n/nor-data-udir-mcp", "h5p/moodle-mod_hvp"]:
        check(f"real[{slug}]", shape_ok(slug), True)


def t_D1_a_relative_path_is_not_an_address():
    """🔴 **D1, found by this instrument's own first run.** `.../archive` passed every
    other test and entered the denominator as address number one, because it has exactly
    one slash and two non-empty sides. 🟢 It came from a RELATIVE PATH in prose, not from
    a URL: a GitHub name cannot begin with a dot or contain `..`."""
    for bad in [".../archive", "../evidence", "./compose", "..%2Fx", "x/..", "../.."]:
        check(f"relative-path[{bad}]", shape_ok(bad), False)


def t_a_tree_path_is_not_an_address():
    """`p351`'s own class: a `blob`/`tree` URL names a FILE inside a repository."""
    for bad in ["openedx/blob", "x/tree", "x/raw", "x/releases", "x/issues", "x/pull",
                "x/commits", "x/wiki", "x/actions"]:
        check(f"tree-path[{bad}]", shape_ok(bad), False)


def t_a_github_product_page_is_not_an_address():
    for bad in ["topics/education", "search/x", "sponsors/x", "marketplace/x",
                "features/copilot", "explore/x", "collections/x", "trending/x"]:
        check(f"product-page[{bad}]", shape_ok(bad), False)


def t_a_dot_git_suffix_is_the_same_address_not_another_one():
    """`p367`'s `.git` fold, restated as a shape rule so it cannot double-count."""
    check("dotgit", shape_ok("HKUDS/DeepTutor.git"), False)


def t_a_three_part_path_is_not_an_address():
    check("three-part", shape_ok("openedx/XBlock/blob"), False)
    check("no-slash", shape_ok("DeepTutor"), False)
    check("empty-side", shape_ok("/x"), False)
    check("empty-side2", shape_ok("x/"), False)


def t_case_folds_so_one_repository_is_one_backlog_ROW():
    """`ACTION UH`: `OpenOLAT/OpenOLAT` and `openolat/OpenOLAT` are one address, and a
    denominator that counts both is inflated by construction."""
    check("fold", fold("OpenOLAT/OpenOLAT"), fold("openolat/openolat"))
    check("fold-trailing-punct", fold("x/y)."), "x/y")


def t_a_dot_inside_a_name_is_legal_and_must_not_be_rejected():
    """🟡 D1's fix must not overreach: `socket.io`-style names are legal on GitHub and
    this corpus carries them."""
    for ok in ["x/socket.io", "x/py-fsrs", "x/a.b.c", "x/v1.0", "a.b/c"]:
        check(f"legal-dot[{ok}]", shape_ok(ok), True)


def main():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("t_") and callable(v)]
    for t in tests:
        t()
    if FAILED:
        print(f"🔴 FAIL — {len(FAILED)} control(s) of {len(tests)}:")
        for f in FAILED:
            print(f"  - {f}")
        return 1
    print(f"🟢 PASS — {len(tests)}/{len(tests)} controls, p371-backlog-grade")
    return 0


if __name__ == "__main__":
    sys.exit(main())
