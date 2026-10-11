#!/usr/bin/env bash
# crosstab.sh — every figure this pass publishes, enumerated from the
# committed TSV rather than counted by hand.
#
# Usage: ./crosstab.sh <result.tsv> [orgs.region.tsv]
#
# P93 (carried): a count is only a count if it ENUMERATES. Each block below
# prints the number AND the rule that produced it, so a reader can re-derive
# any figure in `intel/market.md` from this script and the committed TSV.
set -uo pipefail
cd "$(dirname "$0")"

res="${1:?result tsv}"
orgs="${2:-orgs.region.tsv}"

say() { printf '\n=== %s ===\n' "$1"; }

say "A. verdict distribution, layer 0 (the repository's OWN declaration)"
awk -F'\t' 'NR>1{v[$21]++; n++} END{
  for (k in v) printf "%-14s %4d  %5.1f %%\n", k, v[k], 100*v[k]/n
  printf "%-14s %4d\n", "TOTAL", n
}' "$res" | sort -k2 -rn

say "B. rows p115 PLACES at layer 0, by region and by EVIDENCE CLASS"
awk -F'\t' 'NR>1 && ($21=="placed" || $21=="typed"){
  r[$20]++; n++
  k = ($21=="typed" ? "typed" : $26)
  cl[k]++; rc[$20 "/" k]++
} END{
  print "-- by region --"
  for (x in r)  printf "  %-14s %4d\n", x, r[x]
  print "-- by evidence class (P115-V) --"
  for (x in cl) printf "  %-14s %4d\n", x, cl[x]
  print "-- region x class --"
  for (x in rc) printf "  %-26s %4d\n", x, rc[x]
  printf "\n%-14s %4d\n", "TOTAL PLACED", n
}' "$res"

say "C. the baseline: orgs.region.tsv (P112-L) over the same 296"
awk -F'\t' '
  FNR==NR { if ($0 !~ /^#/ && NF>=2) base[$1]=$2; next }
  FNR==1  { next }
  {
    split($1, a, "/"); o=a[1]
    b = (o in base) ? base[o] : "-"
    if (b=="-")            nun++
    else if (b ~ /\?$/)    nprov++
    else                   { nplaced++; byreg[b]++ }
    n++
  }
  END {
    printf "placed (settled)   %4d\n", nplaced
    printf "provisional (?)    %4d\n", nprov
    printf "UNPLACED           %4d\n", nun
    printf "total              %4d\n", n
    print  "-- settled, by region --"
    for (k in byreg) printf "  %-14s %4d\n", k, byreg[k]
  }' "$orgs" "$res"

say "D. Gap 403: rows the baseline leaves UNPLACED that p115 can place"
awk -F'\t' '
  FNR==NR { if ($0 !~ /^#/ && NF>=2) base[$1]=$2; next }
  FNR==1  { next }
  {
    split($1, a, "/"); o=a[1]
    b = (o in base) ? base[o] : "-"
    placed = ($21=="placed" || $21=="typed")
    if (b=="-" && placed) { nnew++; newreg[$20]++; newcl[($21=="typed"?"typed":$26)]++
      print "  NEW  " $1 "\t" $20 "\t" (($21=="typed") ? "typed country: " toupper($23) : $26 "\t" $25) }
  }
  END {
    printf "\nNEW PLACEMENTS     %4d\n", nnew+0
    for (k in newreg) printf "  region %-14s %4d\n", k, newreg[k]
    for (k in newcl)  printf "  class  %-14s %4d\n", k, newcl[k]
  }' "$orgs" "$res"

say "E. agreement where BOTH place the row"
awk -F'\t' '
  FNR==NR { if ($0 !~ /^#/ && NF>=2) base[$1]=$2; next }
  FNR==1  { next }
  {
    split($1, a, "/"); o=a[1]
    b = (o in base) ? base[o] : "-"
    if ($21!="placed" && $21!="typed") next
    if (b=="-") next
    if (b ~ /\?$/) { nprov++
      if (substr(b,1,length(b)-1)==$20) { print "  PROVISIONAL CONFIRMED  " $1 "\torgs=" b "\tp115=" $20 "\tev=" $25 }
      else { print "  PROVISIONAL CONTRADICTED  " $1 "\torgs=" b "\tp115=" $20 "\tev=" $25 }
      next }
    nboth++
    if (b==$20) { nagree++ }
    else { ndis++; print "  DISAGREE  " $1 "\torgs=" b "\tp115=" $20 "\tev=" $25 }
  }
  END {
    printf "\nboth placed        %4d\n", nboth+0
    printf "agree              %4d\n", nagree+0
    printf "CONTRADICT         %4d\n", ndis+0
    printf "provisional rows p115 also places: %d\n", nprov+0
  }' "$orgs" "$res"

say "F. layer R (README) — the CEILING, never folded into layer 0"
awk -F'\t' 'NR>1{
  if ($37=="r-placed") { rp++; rreg[$36]++ }
  if (($21!="placed" && $21!="typed") && $37=="r-placed") extra++
} END{
  printf "r-placed rows      %4d\n", rp+0
  printf "of which layer 0 did NOT place: %d\n", extra+0
  for (k in rreg) printf "  %-14s %4d\n", k, rreg[k]
}' "$res"

say "G. why the other rows do not place — the reasons, enumerated"
awk -F'\t' 'NR>1 && $21!="placed" && $21!="typed" {
  v[$21]++
  if ($21=="no-country") { st+=$12; gt+=$13; vn+=$14; qq+=$15; uk+=$16 }
} END{
  for (k in v) printf "%-14s %4d\n", k, v[k]
  printf "\nof the no-country rows, the domain classes seen:\n"
  printf "  stoplisted %d   gTLD %d   vanity %d   contested-cc %d   unknown-tld %d\n", st+0, gt+0, vn+0, qq+0, uk+0
}' "$res" | sort -k2 -rn

say "H. structural coverage of the shelf"
awk -F'\t' 'NR>1{
  n++
  if ($21=="UNREAD") { ur++; next }
  read++
  if ($5+0 > 0)  st++
  if ($6+0 > 0)  rs++
  if ($9+0 == 1) cap++
  if ($10+0 > 0) wide++
  if ($4+0 > 0)  vend++
  tf += $3+0
} END{
  printf "addresses                %4d\n", n
  printf "UNREAD                   %4d\n", ur+0
  printf "trees read               %4d\n", read+0
  printf "with a structured file   %4d\n", st+0
  printf "with one at the ROOT     %4d\n", rs+0
  printf "with a vendored path     %4d\n", vend+0
  printf "capped at 40 blobs       %4d\n", cap+0
  printf "with a minified line     %4d\n", wide+0
  printf "files seen, all trees    %4d\n", tf+0
}' "$res"
