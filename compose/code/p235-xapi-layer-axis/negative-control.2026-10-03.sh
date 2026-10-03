#!/bin/bash
# Negative control for P236: the two classifiers side by side on this sector's GPL core.
# BODY  = grep the whole payload for "affero" first (the defective order)
# TITLE = read the first non-blank lines (the corrected order)
# A classifier validated only on AGPL repos scores 100% and is still broken, because
# AGPL -> AGPL is right by accident.  The failure is visible ONLY on GPL payloads.
set -u
for slug in "$@"; do
  for n in LICENSE LICENSE.md COPYING COPYING.txt; do
    o=$(curl -s --max-time 25 -w $'\n%{http_code}' "https://raw.githubusercontent.com/${slug}/HEAD/${n}" 2>/dev/null)
    [ "$(printf '%s' "$o" | tail -1)" = "200" ] || continue
    b=$(printf '%s' "$o" | sed '$d')
    low=$(printf '%s' "$b" | tr '[:upper:]' '[:lower:]')
    case "$low" in
      *"gnu affero general public license"*) body="AGPL-3.0" ;;
      *"gnu general public license"*)        body="GPL" ;;
      *) body="otro" ;;
    esac
    t=$(printf '%s' "$b" | grep -vE '^[[:space:]]*$' | head -3 | tr '\n' ' ')
    tl=$(printf '%s' "$t" | tr '[:upper:]' '[:lower:]')
    case "$tl" in
      *"affero general public license"*) title="AGPL" ;;
      *"general public license"*)        title="GPL" ;;
      *) title="otro" ;;
    esac
    v=$(printf '%s' "$t" | grep -oiE 'version [0-9]+' | head -1 | grep -oE '[0-9]+')
    [ -n "${v:-}" ] && title="$title-${v}.0"
    hits=$(printf '%s' "$low" | grep -c affero)
    verdict="OK"; [ "$body" = "AGPL-3.0" ] && [ "${title%%-*}" = "GPL" ] && verdict="FALSO-POSITIVO-AGPL"
    printf '%s\t%s\tbody=%s\ttitle=%s\tlineas_affero=%s\t%s\n' "$slug" "$n" "$body" "$title" "$hits" "$verdict"
    break
  done
done
