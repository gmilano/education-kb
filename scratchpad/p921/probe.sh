#!/bin/bash
cd /home/user/education-kb || exit 1
probe() {
  hits=$(grep -rilE "$2" --include='*.md' agents repos verticals intel compose 2>/dev/null | head -3 | tr '\n' ' ')
  if [ -z "$hits" ]; then printf '%s\tNEW\t-\n' "$1"; else printf '%s\tPRESENT\t%s\n' "$1" "$hits"; fi
}
probe "NA-67pct-teachers" "67% of teachers"
probe "NA-whitehouse-framework" "White House"
probe "NA-illinois" "Illinois"
probe "NA-virginia-sb394" "SB 394|S\.B\. 394"
probe "NA-ohio" "Ohio"
probe "NA-stanford-ai-index" "AI Index"
probe "NA-nyc-guidance" "New York City|NYC"
probe "EMEA-euaiact-aug2026" "August 2026"
probe "EMEA-council-of-europe" "Council of Europe"
probe "EMEA-eurydice" "Eurydice"
probe "EMEA-oecd-outlook" "Digital Education Outlook"
probe "EMEA-fosway" "Fosway"
probe "EMEA-epson" "Epson"
probe "APAC-arizton" "Arizton"
probe "APAC-uae" "UAE|United Arab Emirates"
probe "APAC-worldbank" "World Bank"
probe "APAC-ipsos" "Ipsos"
probe "APAC-mnm-figures" "591\.6|1,848\.1"
probe "LATAM-dec-survey" "Digital Education Council"
probe "LATAM-iesalc" "IESALC"
probe "LATAM-ceibal" "Ceibal"
probe "LATAM-iadb" "IDB|Inter-American"
probe "LATAM-cepal" "CEPAL|ECLAC"
probe "REPO-education-agent-skills" "education-agent-skills"
probe "REPO-chinatextbook" "ChinaTextbook"
probe "REPO-openeducat" "[Oo]pen[Ee]du[Cc]at"
probe "REPO-genai-beginners" "generative-ai-for-beginners"
probe "REPO-flowise" "[Ff]lowise"
