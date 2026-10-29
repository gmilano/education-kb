"""Controls for `liveness.py`. 🔵 `p355-cwd-portability` / the Makefile's standing note: the
script's own directory is put on `sys.path` explicitly, so this suite passes under `python3 -I`
from ANY working directory, not only from inside its own folder."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from liveness import (ARCHIVED, LIVE, STALE, classify, days_between, permissive,
                      readable_grant, updated_at_is_not_liveness)

TODAY = "2026-10-29"
fails = []


def check(name, got, want):
    if got != want:
        fails.append("%s: got %r want %r" % (name, got, want))


# --- days_between -----------------------------------------------------------
check("days/same", days_between("2026-10-29", "2026-10-29"), 0)
check("days/one", days_between("2026-10-28", "2026-10-29"), 1)
check("days/leap-2028", days_between("2028-02-28", "2028-03-01"), 2)
check("days/accepts-iso-timestamp", days_between("2026-10-28T18:50:56Z", TODAY), 1)

# --- the menthor case: the whole reason this instrument exists ---------------
check("menthor/sound-grade",
      classify(True, "2024-04-21", TODAY), ARCHIVED)
check("menthor/updated_at-would-lie",
      updated_at_is_not_liveness(True, "2024-04-21", "2026-10-12", TODAY), True)

# --- a live control: kolibri ------------------------------------------------
check("kolibri/sound-grade", classify(False, "2026-10-28", TODAY), LIVE)
check("kolibri/updated_at-agrees",
      updated_at_is_not_liveness(False, "2026-10-28", "2026-10-29", TODAY), False)

# --- a genuinely stale but NOT archived repo --------------------------------
check("edrys/stale-not-archived", classify(False, "2024-08-12", TODAY), STALE)
# 🔴 and here updated_at agrees, which is why the naive reader survives most rows
check("edrys/updated_at-agrees",
      updated_at_is_not_liveness(False, "2024-08-12", "2024-08-12", TODAY), False)

# --- an archived repo with a RECENT push: archived must still win -----------
check("archived-but-fresh-push", classify(True, "2026-10-28", TODAY), ARCHIVED)

# --- boundary ---------------------------------------------------------------
check("boundary/365d-is-live", classify(False, "2025-10-29", TODAY), LIVE)
check("boundary/366d-is-stale", classify(False, "2025-10-28", TODAY), STALE)

# --- a future push is a channel error, not a grade --------------------------
try:
    classify(False, "2026-12-01", TODAY)
    fails.append("future-push: expected ValueError")
except ValueError:
    pass

# --- licence axis -----------------------------------------------------------
check("perm/MIT", permissive("MIT"), True)
check("perm/Apache", permissive("Apache-2.0"), True)
check("perm/ECL-2.0-is-apache-derivative", permissive("ECL-2.0"), True)
check("perm/AGPL", permissive("AGPL-3.0"), False)
check("perm/GPL", permissive("GPL-3.0"), False)
check("perm/LGPL", permissive("LGPL-3.0"), False)
check("perm/MPL", permissive("MPL-2.0"), False)
check("perm/NOASSERTION-is-never-permissive", permissive("NOASSERTION"), False)
check("readable/NOASSERTION", readable_grant("NOASSERTION"), False)
check("readable/NONE", readable_grant("NONE"), False)
check("readable/MIT", readable_grant("MIT"), True)

total = 21
if fails:
    print("FAIL %d/%d" % (len(fails), total))
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("OK %d/%d controls green" % (total, total))
