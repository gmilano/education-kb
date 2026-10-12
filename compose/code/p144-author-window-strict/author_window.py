"""p144-author-window-strict -- `ACTION DT`.

Places a repository by per-author UTC offset, the channel that placed eduNEXT in p143.

🔴 **The window definition is the whole instrument, and p143's was not stated.** A split at
Apr-Oct / Nov-Mar puts **March and November inside the "winter" bucket**, and both months
contain a DST transition in the northern hemisphere. A developer in US Eastern commits at
`-0400` for most of March and the first days of November, so the crude split reports winter
`-0400` commits for a US Eastern author and the row reads as year-round `-0400` -- Bolivia,
Paraguay or Venezuela. 🔵 **That is a LATAM placement manufactured by the bucket boundary.**

This instrument uses only months in which no northern DST transition occurs:

    STD  = Dec, Jan, Feb   -- standard time everywhere in the northern hemisphere
    SUM  = Jun, Jul, Aug   -- summer time wherever it is observed

March, April, May, September, October and November are DISCARDED, not reassigned. An author
with no commits in one of the two windows is reported as `BOTH_WINDOWS=no` and places nothing,
because the discriminator IS the comparison:

    -0400 in SUM and -0500 in STD  -> US Eastern            (North America)
    -0400 in SUM and -0400 in STD  -> Bolivia/Paraguay/Amazonas (LATAM, no DST)
    -0300 in SUM and -0400 in STD  -> Atlantic Canada       (North America)
    -0300 in STD and -0400 in SUM  -> Chile                 (LATAM, southern DST phase)

🔵 **Chile and Atlantic Canada share both offsets and are separated only by PHASE**, which is
why the hemisphere's DST direction has to be read rather than the offset set.

Run: python3 -I author_window.py <repo-dir> [<repo-dir> ...]
"""
import collections
import os
import subprocess
import sys

STD_MONTHS = {12, 1, 2}
SUM_MONTHS = {6, 7, 8}
BOT = ("[bot]@", "dependabot", "copilot@", "github-actions")


def windows(repo):
    out = subprocess.run(
        ["git", "-C", repo, "log", "--pretty=format:%ae|%ad", "--date=format:%m|%z"],
        capture_output=True, text=True, check=False).stdout
    per = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    for line in out.splitlines():
        if not line.strip():
            continue
        ae, mo, off = line.split("|")
        if any(b in ae.lower() for b in BOT):
            continue          # a bot's offset is not a person's location
        mo = int(mo)
        w = "STD" if mo in STD_MONTHS else ("SUM" if mo in SUM_MONTHS else None)
        if w:
            per[ae][w][off] += 1
    return per


def main(argv):
    print("\t".join(["repo", "author", "both_windows", "std_offsets", "sum_offsets",
                     "verdict"]))
    for repo in argv:
        per = windows(repo)
        if not per:
            print("\t".join([os.path.basename(repo), "-", "no", "-", "-",
                             "NO_HUMAN_COMMIT_IN_EITHER_WINDOW"]))
            continue
        for ae, w in sorted(per.items(), key=lambda kv: -sum(
                sum(c.values()) for c in kv[1].values())):
            both = "STD" in w and "SUM" in w
            print("\t".join([
                os.path.basename(repo), ae, "YES" if both else "no",
                ",".join("%s=%d" % kv for kv in sorted(w.get("STD", {}).items())) or "-",
                ",".join("%s=%d" % kv for kv in sorted(w.get("SUM", {}).items())) or "-",
                "PLACEABLE" if both else "UNPLACEABLE_SINGLE_WINDOW"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
