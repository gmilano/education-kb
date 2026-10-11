#!/bin/sh
# p120 round 2 - follow the NON-CONVENTIONAL paths each address's own README or
# metadata names, plus the spec-repo conventions. Round 1 established that 10 of
# the 22 carry no grant at any conventional root path; this round tests whether
# the grant is merely somewhere else before any row is called ungranted.
set -u
OUT=${1:-evidence2}
mkdir -p "$OUT"
: > "$OUT/manifest.tsv"
for spec in \
  "OS4ED/openSIS-Classic master docs/License.txt" \
  "OS4ED/openSIS-Classic master docs/license.txt" \
  "OS4ED/openSIS-Classic master License.txt" \
  "1EdTech/openbadges-specification develop LICENSE.md" \
  "1EdTech/openbadges-specification develop CONTRIBUTING.md" \
  "1EdTech/openbadges-specification develop ob_v3p0/LICENSE" \
  "cezarc/EPESI master license.txt" \
  "cezarc/EPESI master LICENSE.TXT" \
  "cezarc/EPESI master gpl.txt" \
  "cezarc/EPESI master include/LICENSE" \
  "LearnPress/learnpress develop license.txt" \
  "LearnPress/learnpress develop readme.txt" \
  "kaushal0494/AITutor-EvalKit main LICENSE.md" \
  "qed42/ai-accessibility-checker main LICENSE.md" \
  "lovejzzz/CourseMapper main LICENSE.md" \
  "Zion-support/curriculum-alignment-checker main LICENSE.md" \
  "xGabrielCv/Auto-Matricula-SIGAA-UnB main LICENSE.md" \
  "Gnanakamalesh-M/student-dropout-early-warning main LICENSE.md" \
  ; do
  set -- $spec
  f="$OUT/$(echo "$1" | tr '/' '_')__$(echo "$3" | tr '/' '_')"
  code=$(curl -s -o "$f" -w '%{http_code}' --max-time 30 \
    "https://raw.githubusercontent.com/$1/$2/$3")
  if [ "$code" = 200 ]; then
    printf '%s\t%s\t%s\t%s\n' "$1" "$3" "$code" "$(wc -c <"$f")" >> "$OUT/manifest.tsv"
  else
    rm -f "$f"
    printf '%s\t%s\t%s\t0\n' "$1" "$3" "$code" >> "$OUT/manifest.tsv"
  fi
done
