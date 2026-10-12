"""p149-placement-exclusions -- `ACTION EZ` + `ACTION FA`: two exclusions on the
institution channel, each measured on its own.

`p148` left two placement defects proved and unfixed, and pre-registered one action for
each. 🔵 **They are implemented here together and measured separately**, because they have
different falsifiers and one of them turns out to be far narrower than its own wording:

> 🟢 **`ACTION EZ`** -- drop bare-`.edu` hosts from placement, keep them as leads, and
> re-run `ACTION ER`'s comparison.
> 🔴 *Refuted if `DISAGREE` is still non-zero after the exclusion.*

> 🟡 **`ACTION FA`** -- URL shorteners and global platforms (`youtu.be`, `bit.ly`, `t.co`,
> `goo.gl`, `youtube.com`, `github.io`) are not institutions. Count how many placements move.
> 🔴 *Refuted if no placement changes.*

## 🔴 Why `ACTION FA`'s six hosts are not six

`T70` was written as though a class of platform hosts had been leaking into the region
axis. 🔴 **Under this shelf's own ccTLD map, only one of the six named hosts can place a
row at all**, and the reason is structural rather than incidental:

| host | suffix | in `CCTLD`? | can it place? |
|---|---|---|---|
| `youtu.be` | `.be` | 🔴 **yes -> EMEA** | 🔴 **yes -- this is `T70`** |
| `youtube.com` | `.com` | no | 🟢 never could |
| `bit.ly` | `.ly` | no | 🟢 never could |
| `t.co` | `.co` | no (deliberately absent -- repurposed) | 🟢 never could |
| `goo.gl` | `.gl` | no | 🟢 never could |
| `github.io` | `.io` | no (deliberately absent -- repurposed) | 🟢 never could |

🔵 **So the exclusion is worth having as a guard and not as a correction.** Five of the six
were already refused, by `CCTLD`'s decision to omit repurposed suffixes rather than by any
rule about platforms -- 🟢 **which means `p147-npm-region`'s most conservative design choice
was load-bearing in a way nobody had measured.** The sixth is a real placement and it moves.

🔴 **The guard is still not redundant.** `.be`, `.me`, `.io`, `.ly`, `.gl`, `.co` and `.to`
are sold as vanity suffixes precisely because they read as words, so the next shortener this
shelf meets is as likely to carry a mapped ccTLD as an unmapped one. 🟢 **The exclusion
names the host, not the suffix**, so it cannot cost a real `.be` institution a placement.

## 🔴 What a bare `.edu` is, and why it is a lead and not a region

`T67` demoted the bare `.edu` after `P144-V` placed `unav.edu` in **EMEA**. 🔵 `ACTION ER`
then proved it was the **sole** cause of the institution/offset channel disagreement. This
module makes the demotion a rule: a bare `.edu` 🔴 **never places a row** and 🟢 **is still
reported**, in a `lead` column, so the evidence is not thrown away.

## Reproduction control

🟢 **The pre-exclusion probe is not modified.** `p147-npm-region` stays as published, so its
figures remain reproducible, and this module drives it by substituting its host classifier
for the duration of a call. 🟢 **`--exclude none` reproduces `p147-npm-region` exactly**, and
`test_placement_exclusions.py` pins that as a test rather than asserting it in prose.

    python3 placement_exclusions.py --exclude none|edu|platform|both|noninst <root>...
    python3 test_placement_exclusions.py     # 26 tests, authored fixtures, offline
"""

import contextlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, os.pardir, "p147-npm-region"))

import npm_region  # noqa: E402  the pre-exclusion probe, driven unmodified

# 🔴 Bound at import, BEFORE any substitution. `classify` must reach the pristine
# classifier: resolving `npm_region.region_of_host` at call time means that inside
# `_classifier` it resolves to the wrapper, which calls `classify` again.
# 🟢 The first run of this module did exactly that and died in `RecursionError` --
# caught by `test_mode_none_reproduces_the_unmodified_probe_exactly`, not in review.
_PRISTINE_REGION_OF_HOST = npm_region.region_of_host

# 🔴 Named hosts, not suffixes. A suffix rule would cost a real `.be` institution its
# placement; `T70`'s defect is that `youtu.be` is a platform, not that `.be` is unsafe.
PLATFORM_HOST = frozenset({
    "youtu.be", "youtube.com", "bit.ly", "t.co", "goo.gl", "github.io",
})

# 🔴 `ACTION EZ`'s refutation named a host nobody had registered. Excluding the bare `.edu`
# moved `BetterSEQTA/DesQTA` from `INSTITUTION_CONFLICT` to 🔴 **`DISAGREE`**, placed
# **EMEA** on `sh.rustup.rs` out of `docs/development/build-deployment.md` -- 🟢 **the Rust
# toolchain installer**, whose `.rs` is Serbia's ccTLD and whose subject is Australian.
#
# 🔵 **So `T70` is a class and `ACTION FA`'s six hosts are not its boundary.** This set is
# kept SEPARATE from `PLATFORM_HOST` so that `--exclude platform` measures exactly what was
# pre-registered and nothing else; `--exclude noninst` measures the class.
DEV_TOOLING_HOST = frozenset({
    "rustup.rs", "sh.rustup.rs",
})

EDU_LEAD_PREFIX = "bare .edu"


def _host_in(host, named):
    h = (host or "").lower().rstrip(".")
    if h.startswith("www."):
        h = h[4:]
    return any(h == p or h.endswith("." + p) for p in named)


def is_platform_host(host):
    """True for a named platform host or any subdomain of one -- `ACTION FA`'s six."""
    return _host_in(host, PLATFORM_HOST)


def is_dev_tooling_host(host):
    """True for a named developer-tooling vanity host -- `ACTION EZ`'s refuting row."""
    return _host_in(host, DEV_TOOLING_HOST)


def classify(host, exclude_edu=False, exclude_platform=False, exclude_devtool=False):
    """(region, how, lead) -- `lead` carries evidence the exclusions refuse to place on."""
    region, how = _PRISTINE_REGION_OF_HOST(host)
    if region is None:
        return None, None, "-"
    if exclude_platform and is_platform_host(host):
        return None, None, "platform host %s (%s)" % (host, how)
    if exclude_devtool and is_dev_tooling_host(host):
        return None, None, "dev-tooling host %s (%s)" % (host, how)
    if exclude_edu and how and how.startswith(EDU_LEAD_PREFIX):
        return None, None, "bare .edu %s" % host
    return region, how, "-"


@contextlib.contextmanager
def _classifier(exclude_edu, exclude_platform, exclude_devtool=False):
    """Drive `npm_region` with a substituted host classifier, then restore it.

    🔵 `npm_region.evidence()` resolves `region_of_host` as a module global, so the
    substitution reaches it. The original is always restored, including on exception.
    """
    original = npm_region.region_of_host
    leads = []

    def wrapped(host):
        region, how, lead = classify(host, exclude_edu, exclude_platform, exclude_devtool)
        if lead != "-":
            leads.append(lead)
        return region, how

    npm_region.region_of_host = wrapped
    try:
        yield leads
    finally:
        npm_region.region_of_host = original


# (exclude_edu, exclude_platform, exclude_devtool)
MODES = {
    "none": (False, False, False),
    "edu": (True, False, False),          # `ACTION EZ` as registered
    "platform": (False, True, False),     # `ACTION FA` as registered -- its six hosts only
    "both": (True, True, False),          # the two registered actions together
    "noninst": (True, True, True),        # 🔵 the measured class, beyond both actions
}

COLS = ["subject", "region", "channel", "host", "how", "where", "conflict", "lead"]


def place(root, mode):
    exclude_edu, exclude_platform, exclude_devtool = MODES[mode]
    with _classifier(exclude_edu, exclude_platform, exclude_devtool) as leads:
        row = npm_region.place(root)
    row["subject"] = os.path.basename(root.rstrip("/"))
    # Deduplicate while preserving first-seen order, so the column is readable.
    seen, ordered = set(), []
    for l in leads:
        if l not in seen:
            seen.add(l)
            ordered.append(l)
    row["lead"] = " | ".join(ordered) if ordered else "-"
    return row


def main(argv):
    if len(argv) < 4 or argv[1] != "--exclude" or argv[2] not in MODES:
        print(__doc__)
        return 2
    mode, roots = argv[2], argv[3:]
    rows = [place(r, mode) for r in roots]
    placed = sum(1 for r in rows if r["region"] in npm_region.CCTLD.values())
    conflict = sum(1 for r in rows if r["region"] == "CONFLICT")
    unplaced = sum(1 for r in rows if r["region"] == "UNPLACED")
    print("# mode: --exclude %s" % mode)
    print("# population: %d" % len(rows))
    print("# placed: %d   CONFLICT: %d   UNPLACED: %d" % (placed, conflict, unplaced))
    print("#")
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
