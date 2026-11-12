#!/usr/bin/env bash
# p798 — ACTION p797-E's missing half: a DENOMINATOR for T931.
#
# p797 ran the es/pt discovery legs on the SEARCH channel, found 5 LATAM-origin education agents,
# and recorded that 5 of 5 serve no grant. Five hand-reached rows cannot tell you whether the grant
# gap is a property of the population or of the sample. This runs the same question on the
# `gh api search/repositories` channel — the one that returns `license.spdx_id` as DATA rather than
# as prose — over a set of in-language query legs, and reports the rate with its denominator.
#
# Why this channel and not WebSearch: the search channel does not state a licence at all, so every
# p797 row needed a second read. Here the grant arrives with the address, which is what makes a
# census affordable.
#
# ONLINE (gh api). Out of `make hooks` by the `carried-existence-sweep` rule.
#
# Usage: ingest/p798-latam-grant-census.sh OUT_TSV
set -uo pipefail
OUT="${1:?output tsv}"

# In-language legs. Education-agent vocabulary as a LATAM author would actually write it.
# `es`/`pt` only: the point is origin, and an English query returns the global shelf (T883).
LEGS=(
  'es|agente educativo IA pushed:>2026-06-01'
  'es|tutor inteligente estudiantes pushed:>2026-06-01'
  'es|asistente docente IA pushed:>2026-06-01'
  'es|plataforma educativa IA agente pushed:>2026-06-01'
  'es|evaluacion automatica estudiantes IA pushed:>2026-06-01'
  'es|chatbot educativo universidad pushed:>2026-06-01'
  'pt|agente educacional IA pushed:>2026-06-01'
  'pt|tutor inteligente alunos pushed:>2026-06-01'
  'pt|assistente professor IA pushed:>2026-06-01'
  'pt|plataforma educacional IA agente pushed:>2026-06-01'
)

printf 'addr\tleg\tstars\tgithub_spdx\tgrant_class\tpushed\tdescription\n' > "$OUT"
TMP=$(mktemp)
for L in "${LEGS[@]}"; do
  leg="${L%%|*}"; q="${L#*|}"
  gh api -X GET search/repositories -f q="$q" -f sort=stars -f per_page=30 \
    --jq ".items[]|[.full_name,\"$leg\",.stargazers_count,(.license.spdx_id//\"NONE\"),(.pushed_at[0:10]),((.description//\"\")|gsub(\"[\\t\\n\\r]\";\" \")|.[0:120])]|@tsv" \
    >> "$TMP" 2>/dev/null
  sleep 2
done

# Dedupe on address, keep the first leg that found it. Then classify the GRANT, not the file.
sort -u -t$'\t' -k1,1 "$TMP" | while IFS=$'\t' read -r addr leg stars spdx pushed desc; do
  case "$spdx" in
    MIT|Apache-2.0|BSD-3-Clause|BSD-2-Clause|ISC|0BSD|Unlicense|BSL-1.0|MIT-0) cls='PERMISSIVE' ;;
    GPL-*|AGPL-*|LGPL-*|MPL-*|EUPL-*|OSL-*|EPL-*)                             cls='COPYLEFT' ;;
    CC-BY-NC*|CC-BY-ND*|CC-BY-SA*|CC-BY-4.0|CC0-1.0)                          cls='CREATIVE-COMMONS' ;;
    NONE)                                                                      cls='NO-LICENCE-FILE' ;;
    NOASSERTION)                                                               cls='UNGRADED-BY-GITHUB' ;;
    *)                                                                         cls="OTHER:$spdx" ;;
  esac
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$addr" "$leg" "$stars" "$spdx" "$cls" "$pushed" "$desc" >> "$OUT"
done
rm -f "$TMP"

echo "rows: $(($(wc -l < "$OUT")-1))"
echo "--- grant_class distribution ---"
tail -n +2 "$OUT" | cut -f5 | sort | uniq -c | sort -rn
