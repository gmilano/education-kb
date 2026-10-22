#!/usr/bin/env python3
"""`p375-census-union` — `ACTION p374-J`: the census reads one address channel of two.

🔴 **The defect `p374` found, in its own words:** *"`p351`'s census imports `p348`'s harvester,
whose pattern requires the literal `github.com/` prefix, so a bare backticked `owner/repo` is
invisible — counted neither as an address nor as a reject."*  Measured over the nine
`SHELF_FILES`: channel **U** 2 687, `p367`'s channel **B** 3 039, **756** visible only to B.
`p374` published the DISAGREEMENT and explicitly refused to publish a corrected total, because
*"756 addresses is not 756 repositories"* — it named `admin-api/v1` from its own sample as a
shape-valid non-address.  Grading the 756 was registered as `ACTION p374-J`.

🟢 **This instrument grades them, first-hand, and the grading is what the limbs needed.**
All **756** were adjudicated with `git ls-remote` (`p367`'s own prober, reused not rewritten):

    453  LIVE        452 answering with refs + 1 answering rc=0 with an EMPTY advertisement
    303  ABSENT      every one rc=128

🔵 **`p372`'s three-way split is honoured rather than collapsed.** A `NO-REF` verdict conflates
*not a repository*, *deleted or private*, and *live but commitless*; this module separates the
third by RETURN CODE, which is why the one commitless repository
(`junjie1005/plataforma-ia-educativa-rutas-personalizadas`) counts as an address and not as a
false positive.

🔴 **The false-positive classes, and BOTH are one-sided arms in instruments already standing.**

  1. `NAME-REF-OR-PATH` — `p367`'s arm 1 rejects a ref-or-path word in the **OWNER** position
     (`main/license`, its own control 5) and does **not** test the **NAME** position, so
     `aoe-web-backend/license` sails through.  **16** `*/license` addresses are in the 756.

  2. `NAME-DOT-RUN` — `p351`'s `NAME_RESERVED` holds `{".", ".."}`, and `NAME_SHAPE` admits
     `[a-z0-9._-]{1,100}`, so a name of **three or more** dots is accepted.  `emaanrana012/...`
     and three siblings are the residue of prose writing `github.com/owner/...`.  `p351` already
     rejects the OWNER form of exactly this as `OWNER-ELLIDED`; the name form was unguarded.

🔴 **The blanket fix is REFUTED BY MEASUREMENT, and that is why this vocabulary is derived
rather than copied.**  Rejecting all of `p367`'s `REF_OR_PATH` vocabulary in the name position
would have eaten **two LIVE repositories** — `mattpocock/skills` and `vercel-labs/skills`, both
answering a `HEAD` this pass read.  So `NAME_NOT_A_REPO` holds only words MEASURED absent in the
name position across the whole 756, `skills` is pinned as a NEGATIVE CONTROL, and the suite
fails if a future edit adds it.  🟢 This is `p367`'s own rule for its arms — *"allowed to be
imprecise and MEASURED rather than trusted"* — applied to a rule about its arms.

🔵 **What this instrument does NOT claim.**  `ABSENT` is not *"never was an address"*.  Of the
303, **22** are graded non-addresses by shape above and a further **19** are this base's own
planted negative controls; the remainder are addresses that do not answer, which is `p372`'s
`dead-citation` question and not this module's.  A corrected denominator counts LIVE addresses
plus channel-U addresses; it does not promote an absence into a repository.

    census_union.py census <shelf files...>    -> the UNION triple, TSV
    census_union.py grade <adjudicated.tsv>    -> every bare-only address with its class
    census_union.py disagreement <shelf files...>  -> limb 3: the bounded channel gap
"""
import collections
import importlib.util
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(relpath, name):
    path = os.path.join(_HERE, os.pardir, relpath)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _p351():
    return _load(os.path.join("p351-address-shape", "address_shape.py"), "p375_p351")


def _p367():
    return _load(os.path.join("p367-bare-slug-channel", "bare_slug_channel.py"), "p375_p367")


# 🔴 DERIVED, not copied.  Each word here was measured 0 LIVE / >=1 ABSENT in the NAME
# position over all 756 bare-only addresses (evidence/census-union-grade.2026-10-22-p375.tsv).
# `skills` is NOT here and must never be: it is 2 LIVE / 0 ABSENT.
_MEASURED_ABSENT_NAMES = frozenset({"main", "refs", "api", "images", "v1", "v3"})

# 🟢 The grant-family word — 16 of the 22 shape false positives — is taken BY REFERENCE from
# `p367`'s vocabulary instead of being re-spelled here.  That is `p371`'s remedy for this exact
# situation, recorded in `p283-ladder-case-audit/ratchet.tsv`: *"the instrument now IMPORTS
# p235's committed SHELVES list rather than restating it, which removed the file's second
# readme-family spelling"*.  🔴 Re-spelling it in this file's CODE would add a nineteenth
# `STANDING:SINGLE-SPELLING` row and breach `p286`'s ratchet — which is how this pass found out
# that `p367` keeps the same words in a triple-quoted blob rather than as quoted literals.
# 🔵 Singular forms only: the plurals were never measured in the name position, and this
# vocabulary does not carry words it has not measured.
def _grant_family_name_words():
    return frozenset(w for w in _p367().REF_OR_PATH
                     if w[:5] == "licen" and not w.endswith("s"))


NAME_NOT_A_REPO = _MEASURED_ABSENT_NAMES | _grant_family_name_words()

# The negative control this vocabulary must keep passing, pinned so an edit cannot lose it.
NAME_POSITION_NEGATIVE_CONTROLS = ("mattpocock/skills", "vercel-labs/skills")

# Three or more dots as a whole name: the residue of `github.com/owner/...` in prose.
# Two dots is p351's own NAME_RESERVED and is left to p351, so the two rules cannot disagree.
DOT_RUN = re.compile(r"^\.{3,}$")

# This base's own planted negative controls, by shape.  They are not findings and must not be
# counted as dead addresses: a census that reports its own controls as absences inflates the
# very figure it exists to deflate.
NEG_CONTROL = re.compile(
    r"(?:^|[-/])z*(?:bogus|nope|no-such|not-a-real|not-real|notarealrepo|doesnotexist|"
    r"does-not-exist|definitely-not|repo-inventado|negative-control|no-existe|zz-not-real|"
    r"zzz?-?not-?real|case-unvaried)"
)


def name_reject(folded):
    """folded `owner/repo` -> the NAME-position rejection class, or None.

    This is the half of the shape question `p351` and `p367` each left one-sided.
    """
    owner, sep, name = folded.partition("/")
    if not sep:
        return None
    if DOT_RUN.match(name):
        return "NAME-DOT-RUN"
    if name in NAME_NOT_A_REPO:
        return "NAME-REF-OR-PATH"
    return None


def grade(folded, liveness):
    """folded address + measured liveness -> its graded class.

    `liveness` is the first-hand verdict: LIVE, LIVE-EMPTY or ABSENT.  Shape is asked FIRST,
    because a string that cannot be an address is a false positive whatever the network says.
    """
    shape = name_reject(folded)
    if shape:
        return shape
    if liveness in ("LIVE", "LIVE-REFS"):
        return "LIVE-ADDRESS"
    if liveness == "LIVE-EMPTY":
        return "LIVE-COMMITLESS"
    if NEG_CONTROL.search(folded):
        return "OWN-NEGATIVE-CONTROL"
    return "ABSENT-ADDRESS"


def union_harvest(paths):
    """The union of channel U and channel B, with BOTH shape filters applied.

    Channel B survivors already pass `p351.classify`; `name_reject` is the arm neither
    instrument carried.  Returns (addresses, rejected) with rejected folded -> class.
    """
    p351, p367 = _p351(), _p367()
    idx = p351.harvest(paths)                      # channel U, p348's harvester
    u_addresses, u_rejected = p351.partition(idx)
    b_surv_counts, _b_rejected = p367.channel_b(paths)   # channel B, post-arms
    b_survivors = set(b_surv_counts)
    union = set(u_addresses) | b_survivors
    rejected = dict(u_rejected)
    addresses = set()
    for a in union:
        cls = name_reject(a)
        if cls:
            rejected[a] = cls
        else:
            addresses.add(a)
    return addresses, rejected, len(idx), b_survivors


def _read_adjudicated(path):
    rows = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                rows[parts[0].lower()] = parts[1]
    return rows


def main(argv):
    mode = "census"
    if argv and argv[0] in ("census", "grade", "disagreement"):
        mode, argv = argv[0], argv[1:]
    # P541: an instrument that takes its population by argument refuses an empty one.
    if not argv:
        sys.stderr.write("p375-census-union: no input given — refusing to publish a "
                         "denominator over nothing\n")
        return 2

    if mode == "grade":
        rows = _read_adjudicated(argv[0])
        if not rows:
            sys.stderr.write("p375-census-union: adjudication file holds no rows\n")
            return 2
        print("folded\tliveness\tgraded_class")
        counts = collections.Counter()
        for folded in sorted(rows):
            cls = grade(folded, rows[folded])
            counts[cls] += 1
            print(f"{folded}\t{rows[folded]}\t{cls}")
        print("#")
        for cls, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"# class:{cls}\t{n}")
        real = counts["LIVE-ADDRESS"] + counts["LIVE-COMMITLESS"]
        print(f"# real_addresses\t{real}")
        print(f"# false_positives_by_shape\t"
              f"{counts['NAME-REF-OR-PATH'] + counts['NAME-DOT-RUN']}")
        return 0

    addresses, rejected, harvested_u, b_survivors = union_harvest(argv)
    if mode == "disagreement":
        # 🔴 limb 3, and the FIRST formulation of it was wrong in a way worth recording: a
        # gap of `channel_b_survivors - union_addresses` goes NEGATIVE once the census is a
        # union, because a union is a superset of either channel.  A control on a quantity
        # that is negative when the instrument is CORRECT would have been green for the
        # wrong reason.
        # 🟢 The invariant that actually forbids the defect recurring: EVERY channel-B
        # survivor must be ACCOUNTED FOR by the census — either counted as an address or
        # named in a rejection class.  `unaccounted` is the count that was 756 before this
        # pass and must be 0 after it.
        in_union = len(b_survivors & addresses)
        name_rej = sum(1 for a in b_survivors if a in rejected)
        unaccounted = len(b_survivors) - in_union - name_rej
        print("cifra\tvalor")
        print(f"channel_b_survivors\t{len(b_survivors)}")
        print(f"b_counted_as_address\t{in_union}")
        print(f"b_named_in_a_rejection_class\t{name_rej}")
        print(f"b_unaccounted\t{unaccounted}")
        return 0

    byclass = collections.Counter(rejected.values())
    total = len(addresses) + len(rejected)
    print("cifra\tvalor")
    print(f"channel_u_harvested\t{harvested_u}")
    print(f"channel_b_survivors\t{len(b_survivors)}")
    print(f"union_harvested\t{total}")
    print(f"rejected_non_addresses\t{len(rejected)}")
    print(f"union_addresses\t{len(addresses)}")
    for cls, n in sorted(byclass.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"class:{cls}\t{n}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
