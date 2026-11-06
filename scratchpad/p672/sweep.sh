#!/bin/bash
# p672 supply sweep on the git channel. English + the four non-English legs
# p664/p665 installed as standing practice. Emits one TSV of raw candidates.
set -u
OUT="$1"
printf 'leg\tslug\tstars\tspdx\tpushed_at\tdescription\n' > "$OUT"
run() {
  local leg="$1"; shift
  local q="$1"; shift
  gh api -X GET search/repositories -f q="$q" -f sort=stars -f order=desc -f per_page=25 \
    --jq ".items[] | [\"$leg\", .full_name, (.stargazers_count|tostring), (.license.spdx_id // \"none\"), (.pushed_at|tostring), ((.description // \"-\")|gsub(\"[\\t\\n]\";\" \"))] | @tsv" \
    2>/dev/null >> "$OUT"
  sleep 2
}
# English legs
run en-tutor      'AI tutor education in:name,description,readme stars:>30'
run en-topic      'topic:education topic:artificial-intelligence stars:>50'
run en-grading    'automated grading assessment AI in:name,description stars:>25'
run en-curriculum 'curriculum lesson plan generator AI in:name,description stars:>20'
run en-agentlms   'LMS agent mcp in:name,description stars:>10'
run en-studyagent 'study agent flashcards spaced repetition in:name,description stars:>40'
# Non-English legs (standing practice since p664/p665)
run de-ki         'KI Unterricht Schule in:name,description,readme'
run de-lern       'Lernplattform KI in:name,description,readme'
run fr-ia         'IA education pedagogique in:name,description,readme'
run es-ia         'IA educacion docente tutor in:name,description,readme'
run pt-ia         'IA educacao professor aluno in:name,description,readme'
run zh-edu        'AI 教育 教学 智能 in:name,description,readme stars:>30'
wc -l < "$OUT"
