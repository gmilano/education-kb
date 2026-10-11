#!/usr/bin/env bash
# P118 ACTION E, verdict layer v2. Four outcomes, because three were not enough.
#
# AGREE   the tree's grant appears among the row's tokens.
# PARTIAL the tree embodies SEVERAL grants and the row names at least one. The
#         row is UNDER-SPECIFIED, which is a different defect from being wrong:
#         PrairieLearn's file puts the Community Edition under AGPL-3.0 and
#         contributed portions under MIT, so a row saying either is incomplete
#         rather than false. Counting these as WRONG would have inflated this
#         pass's headline; counting them as AGREE would have hidden a real
#         obligation. They are named separately and reported separately.
# WRONG   the tree's grant appears NOWHERE in the row. This is Gap 406.
# UNREAD  the tree gave UNKNOWN or committed no licence file: not contradicted,
#         not corroborated. Never folded into AGREE.
set -u
awk -F'\t' '
  function norm(t) { if (t=="Apache-2") return "Apache-2.0"; return t }
  NR==FNR { m[$1]=$4; next }
  {
    slug=$3; toks=$4; meas=(slug in m ? m[slug] : "ABSENT")
    multi=0
    if (meas ~ /^MULTI-GRANT:/) { multi=1; sub(/^MULTI-GRANT:/,"",meas) }
    # A field stub whose grant lives in DESCRIPTION/package manifest does not
    # contradict the row -- it just is not the grant. UNREAD, never WRONG.
    if (meas=="UNKNOWN" || meas=="NO-LICENCE-FILE" || meas=="ABSENT" || meas=="EMPTY" \
        || meas=="GRANT-IN-MANIFEST") {
      v="UNREAD"
    } else if (meas ~ /^GRANT-BY-REFERENCE/) {
      # A pointer with no licence body. Its own class: the row may well be right,
      # but nothing in the repository GRANTS anything, so neither verdict is safe.
      v="REFERENCE-ONLY"
    } else {
      hit=0; G=""; ng=split(meas, GA, ",")
      nt=split(toks, T, ",")
      for (gi=1; gi<=ng; gi++) {
        g=norm(GA[gi])
        for (ti=1; ti<=nt; ti++) {
          t=norm(T[ti])
          if (t==g) { hit++; break }
          if (t=="GPL"  && g ~ /^GPL-/)  { hit++; break }
          if (t=="AGPL" && g ~ /^AGPL-/) { hit++; break }
          if (t=="LGPL" && g ~ /^LGPL-/) { hit++; break }
          if (t=="BSD"  && g=="BSD")     { hit++; break }
          if (t ~ /^BSD-/ && g=="BSD")   { hit++; break }
          if (t ~ /^CC-/ && g ~ /^CC-/)  { hit++; break }
          if (t=="CC0"  && g ~ /^CC/)    { hit++; break }
          if (t ~ /^CC/ && g=="CC0-1.0" && t!="CC0") { hit++; break }
        }
      }
      if (hit==0)            v="WRONG"
      else if (multi && hit<ng) v="PARTIAL"
      else                   v="AGREE"
    }
    printf "%s\t%s\t%s\t%s\t%s\t%s\n", v, $1, $2, slug, toks, (multi?"MULTI-GRANT:":"") meas
  }' measured2.2026-10-11.tsv ../p119-carried-column-audit/claims.g.tsv
