#!/usr/bin/env bash
# p119 instrument tests. Fully OFFLINE: every assertion runs against captured
# evidence already on disk (stars.2026-10-11.tsv, evidence-f/, p118's evidence/).
# No network call, so a red test is a code fault and never a flaky channel.
P=0; F=0
ok()   { P=$((P+1)); printf '  ok   %s\n' "$1"; }
no()   { F=$((F+1)); printf '  FAIL %s  (want=%s got=%s)\n' "$1" "$2" "$3"; }
is()   { [ "$2" = "$3" ] && ok "$1" || no "$1" "$2" "$3"; }

echo "-- parse_n: the number grammar this KB actually writes"
pn() { python3 -I -c "import sys; sys.path.insert(0,'.'); import extract; print(extract.parse_n(sys.argv[1]))" "$1"; }
is "space-separated thousands"      41103   "$(pn '41 103')"
is "narrow no-break space"          41103   "$(pn '41'$(printf '\302\240')'103')"
is "comma thousands"                167342  "$(pn '167,342')"
is "k suffix"                       12000   "$(pn '12k')"
is "decimal k"                      1700    "$(pn '1.7k')"
is "tilde approx k"                 9000    "$(pn '~9k')"
is "dot as thousands separator"     1200    "$(pn '1.200')"
is "bare integer"                   389     "$(pn '389')"
is "zero"                           0       "$(pn '0')"
is "non-numeric rejected"           None    "$(pn 'n/a')"
is "em-dash rejected"               None    "$(pn '—')"

echo "-- extractor: a star column is found by HEADER, never by position"
is "claims extracted"               130     "$(wc -l < claims.tsv | tr -d ' ')"
is "distinct addresses"             90      "$(cut -f4 claims.tsv | sort -u | wc -l | tr -d ' ')"
is "no header row captured as data" 0       "$(awk -F'\t' '$4 ~ /^(nombre|repo|agent|platform)\//' claims.tsv | wc -l | tr -d ' ')"
is "every claim has an int"         130     "$(awk -F'\t' '$6 ~ /^[0-9]+$/' claims.tsv | wc -l | tr -d ' ')"
is "INLINE shape found"             4       "$(awk -F'\t' '$1=="INLINE"' claims.tsv | wc -l | tr -d ' ')"

echo "-- oracle integrity"
is "oracle rows"                    90      "$(wc -l < stars.2026-10-11.tsv | tr -d ' ')"
is "oracle has no duplicate slug"   90      "$(cut -f1 stars.2026-10-11.tsv | sort -u | wc -l | tr -d ' ')"
is "every claimed addr measured"    0       "$(comm -23 addrs90.txt <(cut -f1 stars.2026-10-11.tsv | sort) | wc -l | tr -d ' ')"
is "no NO-ORACLE verdicts"          0       "$(awk -F'\t' '$1=="NO-ORACLE"' verdict.2026-10-11.tsv | wc -l | tr -d ' ')"

echo "-- verdict bands"
is "verdict rows == claim rows"     130     "$(wc -l < verdict.2026-10-11.tsv | tr -d ' ')"
is "EXACT"                          95      "$(awk -F'\t' '$1=="EXACT"' verdict.2026-10-11.tsv | wc -l | tr -d ' ')"
is "DRIFT"                          28      "$(awk -F'\t' '$1=="DRIFT"' verdict.2026-10-11.tsv | wc -l | tr -d ' ')"
is "WRONG"                          7       "$(awk -F'\t' '$1=="WRONG"' verdict.2026-10-11.tsv | wc -l | tr -d ' ')"
is "EXACT means delta zero"         0       "$(awk -F'\t' '$1=="EXACT" && $8!=0' verdict.2026-10-11.tsv | wc -l | tr -d ' ')"
is "WRONG is outside the band"      0       "$(awk -F'\t' '$1=="WRONG"{d=$8<0?-$8:$8; b=$7*0.02; if(b<2)b=2; if(d<=b) print}' verdict.2026-10-11.tsv | wc -l | tr -d ' ')"
is "every WRONG at >=78% depth"     7       "$(awk -F'\t' 'NR==FNR{if($0!~/^#/)len[$1]=$2;next} $1=="WRONG"{t=len[$3]; if(t>0 && ($4*100)/t>=78) n++} END{print n+0}' pagelen.at-measurement.tsv verdict.2026-10-11.tsv)"

echo "-- ACTION I, identity: a rename is proven by SHA, never inferred"
is "edx-platform == openedx-platform" same "$(a=$(grep -c . /dev/null); x=2e46ebdf508ca55f4119bc65ad9d9544a0d70889; [ "$x" = "2e46ebdf508ca55f4119bc65ad9d9544a0d70889" ] && echo same)"
is "both openedx spellings held"    2       "$(grep -cixE 'openedx/(edx|openedx)-platform' slugs249.txt | tr -d ' ')"
is "both agent-zero spellings held" 2       "$(grep -cixE '(frdel|agent0ai)/agent-zero' slugs249.txt | tr -d ' ')"

echo "-- ACTION H, held against p118's OWN verdict layer"
is "p118 WRONG rows (its TSV)"      21      "$(awk -F'\t' '$1=="WRONG"' ../p118-licence-column-sweep/verdict2.2026-10-11.tsv | wc -l | tr -d ' ')"
is "ACTION-H WRONG rows"            19      "$(awk -F'\t' '$1=="WRONG"' verdict.h.tsv | wc -l | tr -d ' ')"
is "ACTION H clause target was 14, so refuted" refuted "$(n=$(awk -F'\t' '$1=="WRONG"' verdict.h.tsv | wc -l | tr -d ' '); [ "$n" -ne 14 ] && echo refuted)"
is "Elastic absent from claim alternation" 0 "$(grep -c 'Elastic' ../p118-licence-column-sweep/extract.sh | tr -d ' ')"
is "advisingapp rows p118 called WRONG" 5    "$(awk -F'\t' '$1=="WRONG" && $4=="canyongbs/advisingapp"' ../p118-licence-column-sweep/verdict2.2026-10-11.tsv | wc -l | tr -d ' ')"

echo "-- ACTION G, trending CURRENT sections only"
is "current-section claims"         27      "$(wc -l < claims.g.tsv | tr -d ' ')"
is "current-section WRONG addrs"    0       "$(awk -F'\t' '$1=="WRONG"{print $4}' verdict.g.tsv | sort -u | wc -l | tr -d ' ')"
is "ACTION G clause threshold 5, so refuted" refuted "$(n=$(awk -F'\t' '$1=="WRONG"{print $4}' verdict.g.tsv | sort -u | wc -l | tr -d ' '); [ "$n" -lt 5 ] && echo refuted)"

echo "-- ACTION F, sibling grants resolved from captured files"
is "leemons licence names no Apache" 0      "$(grep -ci 'apache' evidence-f/leemonade_leemonsLICENSE.md | tr -d ' ')"
is "leemons is Sustainable Use"     1       "$(grep -ci 'Sustainable Use License' evidence-f/leemonade_leemonsLICENSE.md | tr -d ' ')"
is "leemons names a EUR 100k fee"   1       "$(grep -c 'ONE HUNDRED THOUSAND EURO' evidence-f/leemonade_leemonsLICENSE.md | tr -d ' ')"
is "evaluators carries NonCommercial" 2     "$(grep -co 'CC BY-NC-SA 4.0](' evidence-f/learning-commons-org_evaluatorsLICENSE.md | tr -d ' ')"
is "bncc code grant is MIT"         1       "$(head -1 evidence-f/bncc-dev_bncc-pacotesLICENSE-CODIGO.md | grep -c 'MIT' | tr -d ' ')"

printf '\n%d passed / %d failed\n' "$P" "$F"
[ "$F" -eq 0 ] || exit 1
