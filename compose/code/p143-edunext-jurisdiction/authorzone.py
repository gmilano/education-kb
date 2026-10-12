"""p143-edunext-jurisdiction, per AUTHOR -- the unit the pooled test got wrong.

The pooled DST test returned `MIXED` on 5 of 5 eduNEXT repositories: both `-0500` and
`-0400` appear in both the DST window and outside it. 🔵 **Pooling was the wrong unit.**
A repository's commits come from many people, and a mixture of two zones pools into
exactly the shape a single ambiguous zone would.

🟢 **An AUTHOR is the unit that carries a timezone.** For each author:

  * offsets `{-0500}` only, with commits in BOTH the DST window and outside it
    => a zone that does NOT observe DST and sits at -0500 year round.
    🔵 Colombia, Peru and Ecuador. 🔴 NOT US Eastern, which would go to -0400 in July.
  * offsets `{-0500, -0400}` with -0400 inside the window and -0500 outside
    => US Eastern (or any DST-observing -0500 standard zone).
  * offsets `{-0500}` but commits in only ONE window
    => UNDETERMINED. There is no evidence either way and it is reported as such
      rather than assigned to the majority.

🔴 **What this probe CANNOT do, stated before its results are read.** A year-round -0500
author is Colombia, Peru or Ecuador -- the channel does not separate those three. It also
cannot exclude US CENTRAL, which is -0500 during DST: an author committing only between
April and October at -0500 may be in Chicago. 🔵 **That is why the BOTH-WINDOWS condition
is required**: -0500 in January rules out US Central, and -0500 in July rules out US
Eastern. 🟢 **Only an author satisfying both is booked**, and the count of those authors
is the finding.

Run: python3 -I authorzone.py name=path [name=path ...]
"""

import os
import subprocess
import sys

DST_IN = {4, 5, 6, 7, 8, 9, 10}
DST_OUT = {1, 2, 12}

SEP = "\x1f"


def commits(repo):
    out = subprocess.run(
        ["git", "-C", repo, "log",
         "--format=%ae" + SEP + "%ad", "--date=format:%m " + SEP + "%z"],
        capture_output=True, text=True, timeout=300).stdout
    for line in out.splitlines():
        parts = line.split(SEP)
        if len(parts) != 3:
            continue
        email, mon, off = parts[0].strip(), parts[1].strip(), parts[2].strip()
        if mon.isdigit():
            yield email.lower(), int(mon), off


COLS = ["author_domain", "commits", "offsets", "in_dst_offsets", "out_dst_offsets",
        "verdict"]


def main(argv):
    # author -> {"n":int, "off":set, "in":set, "out":set}
    authors = {}
    for spec in argv:
        name, path = spec.split("=", 1)
        if not os.path.isdir(path):
            continue
        for email, mon, off in commits(path):
            a = authors.setdefault(email, {"n": 0, "off": set(), "in": set(),
                                           "out": set()})
            a["n"] += 1
            a["off"].add(off)
            if mon in DST_IN:
                a["in"].add(off)
            elif mon in DST_OUT:
                a["out"].add(off)

    print("\t".join(COLS))
    tally = {}
    for email, a in sorted(authors.items(), key=lambda kv: -kv[1]["n"]):
        off, ins, outs = a["off"], a["in"], a["out"]
        if off == {"-0500"} and ins and outs:
            v = "NO_DST_AT_MINUS5_BOTH_WINDOWS"
        elif "-0500" in off and "-0400" in off and "-0400" in ins and "-0500" in outs:
            v = "DST_OBSERVING_US_EASTERN_SHAPE"
        elif off == {"-0400"} and ins and outs:
            # 🔵 A constant -0400 across both windows is NOT "mixed" -- it is its own
            # finding, and the first draft of this probe buried three authors and 201
            # commits under a label that said the opposite of what the data showed.
            # -0400 in January rules out US Eastern; -0400 in July rules out Atlantic
            # Canada (which goes to -0300). Venezuela and Bolivia remain.
            v = "NO_DST_AT_MINUS4_BOTH_WINDOWS"
        elif off == {"-0500"}:
            v = "UNDETERMINED_minus5_one_window_only"
        elif off == {"-0400"}:
            v = "UNDETERMINED_minus4_one_window_only"
        elif off & {"-0500", "-0400"}:
            v = "UNDETERMINED_mixed_multi_zone"
        else:
            v = "NOT_AMERICAN_OFFSET"
        tally[v] = tally.get(v, 0) + 1
        # publish the mail DOMAIN, not the address: the jurisdiction question is about
        # the organisation, and a contributor's personal address is not this KB's to post.
        dom = email.split("@")[-1] if "@" in email else "(none)"
        print("\t".join([dom, str(a["n"]), ",".join(sorted(off)),
                         ",".join(sorted(ins)) or "-", ",".join(sorted(outs)) or "-", v]))

    print("\n# distinct authors: %d" % len(authors), file=sys.stderr)
    for k, n in sorted(tally.items(), key=lambda kv: -kv[1]):
        print("# %-38s %d" % (k, n), file=sys.stderr)
    booked = [e for e, a in authors.items()
              if a["off"] == {"-0500"} and a["in"] and a["out"]]
    print("#", file=sys.stderr)
    print("# 🟢 authors at -0500 in BOTH windows with NO -0400 ever: %d" % len(booked),
          file=sys.stderr)
    print("#    (a non-DST -0500 zone: Colombia, Peru or Ecuador -- NOT US Eastern, "
          "NOT US Central)", file=sys.stderr)
    print("#    commits from them: %d of %d"
          % (sum(authors[e]["n"] for e in booked),
             sum(a["n"] for a in authors.values())), file=sys.stderr)
    east = [e for e, a in authors.items()
            if "-0500" in a["off"] and "-0400" in a["off"]
            and "-0400" in a["in"] and "-0500" in a["out"]]
    print("# 🔴 authors with the US Eastern DST shape: %d (commits %d)"
          % (len(east), sum(authors[e]["n"] for e in east)), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
