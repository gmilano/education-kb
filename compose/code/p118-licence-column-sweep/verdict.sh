#!/usr/bin/env bash
# P118 ACTION E, verdict layer. Joins the published claim set to the measured tree.
#
# AGREE   -- the tree's licence appears among the row's tokens. A row a prior pass
#            already corrected carries both the old and new token, so it agrees.
# WRONG   -- the tree's licence appears NOWHERE in the row. This is Gap 406.
# UNREAD  -- the tree gave UNKNOWN or NO-LICENCE-FILE: the row is not contradicted,
#            but it is not corroborated either. Counted separately, never as AGREE.
set -u
awk -F'\t' '
  NR==FNR { m[$1]=$4; next }
  {
    slug=$3; toks=$4; meas=(slug in m ? m[slug] : "ABSENT")
    if (meas=="UNKNOWN" || meas=="NO-LICENCE-FILE" || meas=="ABSENT") { v="UNREAD" }
    else {
      v="WRONG"
      n=split(toks, T, ",")
      for (i=1;i<=n;i++) {
        t=T[i]
        if (t==meas) { v="AGREE"; break }
        # Family-level tolerance: a row saying "GPL" is not WRONG about GPL-3.0,
        # and "BSD" is not WRONG about BSD-3-Clause. A row saying GPL about an
        # AGPL tree IS wrong -- network copyleft is a different obligation.
        if (t=="GPL"  && meas ~ /^GPL-/)   { v="AGREE"; break }
        if (t=="LGPL" && meas ~ /^LGPL-/)  { v="AGREE"; break }
        if (t=="BSD"  && meas=="BSD")      { v="AGREE"; break }
        if (t ~ /^BSD-/ && meas=="BSD")    { v="AGREE"; break }
        if (t ~ /^CC-/ && meas=="CC")      { v="AGREE"; break }
        if (t=="CC0"  && meas=="CC")       { v="AGREE"; break }
      }
    }
    printf "%s\t%s\t%s\t%s\t%s\t%s\n", v, $1, $2, slug, toks, meas
  }' measured.2026-10-11.tsv claims.raw.tsv
