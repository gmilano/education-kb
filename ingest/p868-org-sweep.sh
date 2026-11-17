#!/usr/bin/env bash
# p868 -- the organisation-owned discovery sweep, COMMITTED this time.
#
# WHY THIS EXISTS.  `p867` changed one search parameter (`owner.type == Organization`),
# measured `160` NEW addresses in `285` against `p866`'s `0` in `54`, and did NOT commit
# the queries.  `evidence/channel-yield.2026-11-17-p867.tsv` records the TOTALS only, so
# `867-G1`'s acceptance test -- "apply a mechanical domain predicate to the whole
# organisation-owned sweep" -- had no sweep to apply it to.  A channel that cannot be
# re-run is a measurement, not an instrument.  This is the instrument.
#
# 🔴 DECLARED: the nine veins below are a RECONSTRUCTION.  `p867`'s vein labels survive in
# `evidence/promotion-rank.2026-11-17-p867.tsv` (`v2-topic`, `v3-moodle`, `v4-analytics`,
# `v6-edtech`) and the query text does not.  The labels are kept so the two passes' rows
# are comparable; the query bodies are this pass's and are stated here rather than implied.
#
# The `owner.type` filter is POST-HOC: `search/repositories` has no `owner.type` qualifier,
# so the sweep collects and the filter discards.  Forks are excluded by the endpoint's own
# default, so every total here is a NON-FORK count.
set -uo pipefail
OUT="${1:?usage: p868-org-sweep.sh out.tsv}"
PER_PAGE="${PER_PAGE:-100}"

printf 'vein\taddress\towner_type\tstars\tforks\tlicence\tpushed\tarchived\tdefault_branch\tdescription\ttopics\n' > "$OUT"

sweep() {  # sweep <vein> <query>
  local vein="$1" q="$2"
  gh api -X GET search/repositories -f q="$q" -f sort=stars -f order=desc -f per_page="$PER_PAGE" \
    --jq ".items[] | [\"$vein\", .full_name, .owner.type, (.stargazers_count|tostring), (.forks_count|tostring), ((.license.spdx_id)//\"NONE\"), (.pushed_at[0:10]), (.archived|tostring), (.default_branch//\"-\"), ((.description//\"-\")|gsub(\"[\\t\\n\\r]\";\" \")), ((.topics//[])|join(\",\"))] | @tsv" \
    2>/dev/null >> "$OUT"
  sleep 2.5   # 30 search requests/minute; 2.5s keeps the sweep inside it without a retry loop
}

# 🔴 p868's first run capped every vein at `per_page=50` and the sweep returned 404 raw rows
# -- 9 veins x ~50, a CAP and not a population.  Raised to 100, and `topic:edtech
# topic:educational-ai` was split: two topic qualifiers in one `q` are ANDed by the endpoint
# (12 results against 5,723 and 62 separately), so the vein was measuring an intersection
# nobody asked for.
sweep v1-tutor     'AI tutor education in:name,description,readme'
sweep v2-topic     'topic:edtech'
sweep v2b-topic-ai 'topic:educational-ai'
sweep v3-moodle    'moodle AI plugin in:name,description'
sweep v4-analytics 'learning analytics AI in:name,description'
sweep v5-grading   'automated grading assessment AI in:name,description'
sweep v6-edtech    'edtech AI platform in:name,description'
sweep v7-curricula 'curriculum OR syllabus generator in:name,description'
sweep v8-lmsagent  'LMS agent MCP in:name,description'
sweep v9-openedx   'open edx xblock in:name,description'
sweep v10-eduagent 'AI education agent in:name,description'
sweep v11-assist   'student learning AI assistant in:name,description'

echo "rows: $(( $(wc -l < "$OUT") - 1 ))" >&2
