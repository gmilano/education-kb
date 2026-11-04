#!/usr/bin/env bash
# p640 — grade on the TITLE LINE, not substring-over-payload. Both p639's grader and p640's
# first grader failed on the GNU family because GPL-3.0 names AFFERO 3x (s.13) and AGPL-3.0
# names "GNU GENERAL PUBLIC LICENSE" 5x. Title-line grading is the only sound discriminator.
# Plus a SIZE BAND: a title/body matched MIT outside ~1000-1250B is a narrowed derivative.
set -uo pipefail
B=$(mktemp); trap 'rm -f "$B"' EXIT
while IFS=$'\t' read -r slug path bytes _old; do
  [ "$path" = "NO-PAYLOAD" ] && { printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$path" "$bytes" "NO-PAYLOAD" "needs existence channel"; continue; }
  p=${path#HEADER:}
  curl -s --max-time 25 -o "$B" "https://raw.githubusercontent.com/$slug/$p"
  title=$(head -c 200 "$B" | tr -d '\357\273\277' | tr '\n' ' ' | sed 's/  */ /g;s/^ //')
  t=$(printf '%s' "$title" | tr '[:upper:]' '[:lower:]')
  g=UNGRADED; note=""
  case "$t" in
    *"gnu affero general public license"*) g="AGPL-3.0";;
    *"gnu lesser general public license"*) g="LGPL";;
    *"gnu general public license"*)        g="GPL-3.0";;
    *"apache license"*)                    g="Apache-2.0";;
    *"educational community license"*)     g="ECL-2.0";;
    *"elastic license"*)                   g="Elastic-2.0";;
    *"mozilla public license"*)            g="MPL-2.0";;
    *"mit license"*)                       g="MIT";;
    *"creative commons"*|*"attribution"*)  g="CC-family";;
    *"cc0 1.0"*)                           g="CC0-1.0";;
    *)
      # no licence title -> bespoke/declaration/consortium. Fall back to body, then SIZE-BAND it.
      if   grep -qi 'non-commercial\|noncommercial' "$B"; then g="BESPOKE-NONCOMMERCIAL"; note="title is a project name; body bars commercial use"
      elif grep -qi 'permission is hereby granted, free of charge' "$B"; then
             if [ "$bytes" -ge 1000 ] && [ "$bytes" -le 1250 ]; then g="MIT"; else g="MIT-PHRASED-DERIVATIVE"; note="MIT phrase at ${bytes}B, outside the 1000-1250B MIT band"; fi
      elif grep -qi 'cc0 1.0 universal' "$B"; then g="CC0-1.0"
      elif [ "$bytes" -lt 100 ]; then g="DECLARATION-ONLY"; note="$(head -c 80 "$B" | tr -d '\n')"
      else g="UNGRADED-bespoke-or-consortium"; note="title: $(printf '%s' "$title" | head -c 60)"; fi;;
  esac
  # cross-check: MIT grade must sit in the measured MIT band
  if [ "$g" = "MIT" ] && { [ "$bytes" -lt 1000 ] || [ "$bytes" -gt 1250 ]; }; then
     g="MIT-TITLE-OUT-OF-BAND"; note="${bytes}B"; fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$path" "$bytes" "$g" "$note"
done
