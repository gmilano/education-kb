#!/usr/bin/env bash
# p206 regression suite. Offline: every fixture is a real licence body, fetched
# once from the repository named in its comment and committed beside this file.
cd "$(dirname "$0")" || exit 1
. ./classify.sh
pass=0; fail=0
t() { # t <fixture> <expected>
  local got; got=$(classify_grant "$(cat "fixtures/$1")")
  if [ "$got" = "$2" ]; then pass=$((pass+1)); printf '  ok   %-38s %s\n' "$1" "$got"
  else fail=$((fail+1)); printf '  FAIL %-38s got=%s want=%s\n' "$1" "$got" "$2"; fi
}

echo "D1 markdown heading breaks the ^ anchor"
t gpl-3.0-h3-heading.LICENSE        GPL-3.0      # cerpus/Edlib        "### GNU GENERAL PUBLIC LICENSE"
t gpl-2.0-markdown-heading.md       GPL-2.0      # idempiere/idempiere "<center> # GNU General Public License"
echo "D2 version pushed past a 3-line window"
t gpl-3.0-underline-heading.md      GPL-3.0      # cgrevisse/moodle-qbank_genai  title/====/blank/Version 3
echo "D3 the licence is not in English"
t agpl-3.0-portuguese.LICENSE       AGPL-3.0     # portabilis/i-diario "LICENCA PUBLICA GERAL AFFERO GNU"
echo "D4 a family absent from the table"
t elastic-2.0.LICENSE               NON-OSI-Elastic-2.0   # canyongbs/advisingapp
echo "D5 narrative grant, no title line"
t agpl-3.0-narrative-anki.LICENSE   AGPL-3.0-STATEMENT    # ankitects/anki
t gpl-3.0-narrative.LICENSE         GPL-3.0-STATEMENT     # pawtograder/assignment-action
echo "D6 a reference, not an instrument"
t gpl-3.0-oneline-statement.txt     GPL-3.0-STATEMENT     # frappe/education, 19 B
t cc-by-4.0-statement.txt           CC-BY-4.0-STATEMENT   # UD_Spanish-AnCora, 189 B
echo "D7 NOTICE is a channel: it classifies, but it is not a body path"
t apache-2.0-notice-channel.NOTICE  Apache-2.0-STATEMENT  # foradian/fedena
echo "preamble-first LGPL (p205 returned UNRECOGNISED)"
t lgpl-3.0-preamble-first.LICENSE   LGPL-STATEMENT        # untisapi/untis4j, title stripped from the payload
echo "D8 a UTF-8 BOM sits between ^ and the title"
t gpl-2.0-utf8-bom.txt              GPL-2.0      # OS4ED/openSIS-Classic  (p201 even noted the BOM)
t gpl-3.0-utf8-bom.LICENSE          GPL-3.0      # Berserk-hub150/moodle-ai-skill-navigator
echo "D10 a WRAPPED PROSE line can start with a licence name at column 0"
t gpl-3.0-wrapped-prose-line.LICENSE GPL-3.0-STATEMENT  # pawtograder/platform: "GNU General Public License for more details."
t gpl-2.0-narrative-then-body.txt    GPL-2.0            # gazpachu/hypatia: narrative header ABOVE the real instrument

echo "p205 controls — must not regress"
t gpl-3.0-control-moodle.txt        GPL-3.0      # the GPL names the AGPL in section 13
t agpl-3.0-control-frappe.txt       AGPL-3.0     # a TRUE AGPL still classifies AGPL
t mpl-2.0-control-coqui.txt         MPL-2.0      # the MPL names the AGPL in section 1.12
t ecl-2.0-control-opencast.LICENSE  ECL-2.0      # the ECL names Apache in paragraph 1
t apache-2.0-control-kaldi.txt      Apache-2.0   # ~1.5 kB of header prose above the title

echo
printf 'passed %d / %d\n' "$pass" "$((pass+fail))"
[ "$fail" -eq 0 ]
