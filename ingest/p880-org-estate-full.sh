#!/usr/bin/env bash
# p880 — the FULL org estate, not a top-40 sample.
#
# WHY THIS EXISTS. p879 published a per-organisation permissive/copyleft table over 571
# repositories and attached this caveat to it:
#
#     "These are samples, not totals: the search endpoint returns at most 40 per query [...]
#      Percentages are of the sample. Do not quote them as org-wide."
#
# 🔴 The endpoint does not return at most 40. `per_page` accepts 100, and `page` walks the
# rest: `user:openedx` is total_count=174 and returns 100 + 74. The 40 was p879's OWN
# parameter. The denominator it declared unavailable was one flag away.
#
# WHAT IT MEASURES. For each owner: every repository the search index holds, paged to
# exhaustion, with licence/stars/liveness per row. Two arms, because they answer different
# questions:
#   SOURCES  — `user:<org>`            GitHub repo search EXCLUDES forks by default.
#                                      This is what the org BUILT: the right denominator.
#   +FORKS   — `user:<org> fork:true`  sources+forks, so the fork load is a measured number
#                                      rather than an assumption.
#
# Search is rate-limited at 30/min; every request sleeps.
set -uo pipefail

OUT="${1:?usage: p880-org-estate-full.sh OUT.tsv [orgs-file]}"
ORGS_FILE="${2:-}"
SLEEP="${SLEEP:-3}"

if [ -n "$ORGS_FILE" ]; then
  mapfile -t ORGS < <(grep -vE '^\s*(#|$)' "$ORGS_FILE")
else
  # Arm A: the 19 owners p879 sampled.  Arm B: owners never swept by any pass, chosen to
  # put EMEA / APAC / LATAM integrators on the same measured axis as the US/EU cores.
  ORGS=(
    openedx moodlehq ls1intum learningequality jupyterhub jupyter h5p edx chaoss
    bigbluebutton HKUDS apereo overhangio oppia ILIAS-eLearning sakaiproject moodle
    autolab openeducat
    instructure chamilo OpenOlat 1EdTech frappe mitodl openfun eduNEXT edly-io
    IONISx cmmedu raccoongang
  )
fi

printf 'org\tarm\tfull_name\tstars\tspdx\tpushed\tcreated\tarchived\tfork\tlanguage\tdescription\n' > "$OUT"
: > "${OUT%.tsv}.totals.tsv"
printf 'org\tarm\ttotal_count\trows_collected\tpages\n' > "${OUT%.tsv}.totals.tsv"

jqf='.items[] | [$org,$arm,.full_name,(.stargazers_count|tostring),(.license.spdx_id // "NONE"),
     ((.pushed_at // "")[0:10]),((.created_at // "")[0:10]),(.archived|tostring),(.fork|tostring),
     (.language // ""),((.description // "")|gsub("[\t\n\r]";" "))] | @tsv'

for org in "${ORGS[@]}"; do
  for arm in sources withforks; do
    if [ "$arm" = "sources" ]; then q="user:$org"; else q="user:$org fork:true"; fi

    total=""; rows=0; page=1
    while : ; do
      resp=$(gh api -X GET search/repositories -f q="$q" -f per_page=100 -f page="$page" 2>/dev/null)
      rc=$?
      sleep "$SLEEP"
      if [ $rc -ne 0 ] || [ -z "$resp" ]; then
        echo "🔴 $org/$arm page$page REQUEST-FAILED" >&2
        break
      fi
      tc=$(printf '%s' "$resp" | jq -r '.total_count // "ERR"')
      [ -z "$total" ] && total="$tc"
      n=$(printf '%s' "$resp" | jq -r '.items | length')
      [ "$n" = "0" ] && break
      printf '%s' "$resp" | jq -r --arg org "$org" --arg arm "$arm" "$jqf" >> "$OUT"
      rows=$((rows+n))
      # search caps the result set at 1000 regardless of total_count
      if [ "$rows" -ge "$tc" ] || [ "$rows" -ge 1000 ] || [ "$n" -lt 100 ]; then break; fi
      page=$((page+1))
    done
    printf '%s\t%s\t%s\t%s\t%s\n' "$org" "$arm" "${total:-ERR}" "$rows" "$page" \
      >> "${OUT%.tsv}.totals.tsv"
    echo "  $org/$arm total=${total:-ERR} collected=$rows" >&2
  done
done
echo "🟢 wrote $OUT and ${OUT%.tsv}.totals.tsv" >&2
