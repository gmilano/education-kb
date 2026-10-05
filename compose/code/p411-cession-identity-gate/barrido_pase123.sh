#!/bin/bash
# Corre la compuerta contra los PAYLOADS REALES del pase 123.
cd "$(dirname "$0")"
while IFS=$'\t' read -r slug br fn; do
  # 🆕 `P417`: NO usar `payload=$(curl …)` + `printf '%s'`. La sustitucion de comando y el
  # `printf` COMEN todos los saltos de linea finales, asi que el conteo sale 1-2 B corto y el
  # `sha256` no reproduce el del corpus. Se canaliza el payload CRUDO por un archivo temporal.
  tmp=$(mktemp)
  curl -s --max-time 25 "https://raw.githubusercontent.com/$slug/$br/$fn" -o "$tmp"
  res=$(python3 gate_cesion.py < "$tmp" 2>/dev/null | head -1)
  rm -f "$tmp"
  printf "%-46s %s\n" "$slug" "$res"
done <<'EOF'
DaRL-GenAI/instructional_agents	main	LICENSE
beltromatti/get-it	main	LICENSE
menthorlabs/menthor	main	LICENSE
jcputney/scorm-again	master	LICENSE
tsugiproject/tsugi	master	LICENSE
CaviraOSS/PageLM	main	LICENSE.md
canyongbs/advisingapp	main	LICENSE
leemonade/leemons	main	LICENSE.md
Berserk-hub150/moodle-ai-skill-navigator	main	LICENSE
JudgePeach/math-question-bank	main	LICENSE
adilmohak/django-lms	main	LICENSE
SkyCascade/SkyLearn	main	LICENSE
EOF
