"""p145-origin-bots -- `ACTION DW`: strip bots and re-run the 44-row origin census.

> 🟡 **`ACTION DW`** -- strip bots from `p142-origin-at-scale` and re-run the 44-row
> census. `P144-P` shows 9 rows contaminated and one at 32.4%. Re-run `origin_scale.py`
> with the bot filter `author_window.py` already uses, and record which rows change
> `dominant_offset` or region.
> 🔴 *Refuted if no row changes its region* -- which would make bot contamination a real
> defect with no consequence, and it should be recorded as a caveat rather than fixed.

The bot list is `author_window.py`'s, carried over verbatim so the two instruments agree
rather than each having their own idea of what a robot is.
"""

import subprocess
import sys

# 🔵 Carried verbatim from `p144-author-window-strict/author_window.py`.
BOT = ("[bot]@", "dependabot", "copilot@", "github-actions")

# 🔴 An offset alone does not place a repository. These are the ones that do not
# discriminate a single region, carried from `p142`'s own reasoning.
AMBIGUOUS = {
    "-0300": "Brazil/Argentina/Uruguay (LATAM) AND Greenland/St Pierre (North America)",
    "+0000": "UTC: UK/Portugal/Iceland (EMEA) AND any CI runner anywhere",
    "-0400": "Bolivia/Paraguay/Chile (LATAM) AND US Eastern DST (North America)",
    "+0100": "Western/Central Europe (EMEA) AND West Africa (EMEA)",
}


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True,
                          text=True, timeout=300).stdout


def offsets(repo, strip_bots):
    """Histogram of author timezone offsets, optionally excluding robots."""
    out = git(repo, "log", "--format=%ae\t%aI")
    hist, bots, total = {}, 0, 0
    for line in out.splitlines():
        if "\t" not in line:
            continue
        ae, iso = line.split("\t", 1)
        total += 1
        if any(b in ae.lower() for b in BOT):
            bots += 1
            if strip_bots:
                continue
        off = iso.strip()[-6:].replace(":", "")
        if len(off) == 5 and off[0] in "+-":
            hist[off] = hist.get(off, 0) + 1
    return hist, bots, total


def dominant(hist):
    if not hist:
        return "-", 0
    off, n = max(hist.items(), key=lambda kv: (kv[1], kv[0]))
    return off, n


COLS = ["subject", "commits", "bot_commits", "bot_share", "dom_with_bots",
        "dom_no_bots", "offset_changed", "placement", "note"]


def row(subject, repo):
    with_bots, bots, total = offsets(repo, strip_bots=False)
    no_bots, _, _ = offsets(repo, strip_bots=True)
    dw, nw = dominant(with_bots)[0], dominant(no_bots)[0]
    share = (100.0 * bots / total) if total else 0.0
    placement = "AMBIGUOUS" if nw in AMBIGUOUS else ("PLACEABLE" if nw != "-" else "-")
    note = AMBIGUOUS.get(nw, "")
    if not no_bots and with_bots:
        placement, note = "BOT_ONLY", "🔴 every commit on this row is a robot's"
    return dict(zip(COLS, [subject, total, bots, "%.1f%%" % share, dw, nw,
                           "YES" if dw != nw else "no", placement, note]))


def main(argv):
    rows = [row(s.split("=")[0], s.split("=")[1]) for s in argv]
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))

    changed = [r for r in rows if r["offset_changed"] == "YES"]
    contaminated = [r for r in rows if r["bot_commits"]]
    print("", file=sys.stderr)
    print("# rows measured:            %d" % len(rows), file=sys.stderr)
    print("# rows with ANY bot commit: %d" % len(contaminated), file=sys.stderr)
    print("# rows whose DOMINANT OFFSET changes when bots are stripped: %d"
          % len(changed), file=sys.stderr)
    for r in changed:
        print("#   %-46s %s -> %s  (bots %s)"
              % (r["subject"], r["dom_with_bots"], r["dom_no_bots"], r["bot_share"]),
              file=sys.stderr)
    worst = sorted(contaminated, key=lambda r: -float(r["bot_share"].rstrip("%")))[:5]
    print("# most contaminated rows:", file=sys.stderr)
    for r in worst:
        print("#   %-46s %s of %s commits" % (r["subject"], r["bot_share"],
                                              r["commits"]), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
