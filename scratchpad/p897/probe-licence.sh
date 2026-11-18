#!/bin/bash
# p897 job (c): byte-read licence files for repos carried as OTHER / NO-LICENSE-FILE
REPOS="frappe/education ECNU/EduWork Open-TutorAi/open-tutor-ai-CE IIC2233/Syllabus OS4ED/openSIS-Classic moodlehq/moodleapp jupyter/nbgrader"
BRANCHES="main master develop"
NAMES="LICENSE LICENSE.md LICENSE.txt LICENSE.TXT license.txt LICENCE LICENCE.md COPYING COPYING.txt COPYING.md LICENSE.rst LICENSE-MIT LICENSE-APACHE NOTICE"
for r in $REPOS; do
  echo "=== $r ==="
  found=0
  for b in $BRANCHES; do
    for n in $NAMES; do
      url="https://raw.githubusercontent.com/$r/$b/$n"
      code=$(curl -s -o /tmp/lic.$$ -w '%{http_code}' --max-time 20 "$url")
      if [ "$code" = "200" ]; then
        sz=$(wc -c < /tmp/lic.$$)
        sh=$(sha256sum /tmp/lic.$$ | cut -c1-12)
        first=$(grep -m1 -vE '^\s*$' /tmp/lic.$$ | cut -c1-110)
        echo "  HIT $b/$n  ${sz}B  sha256_12=$sh"
        echo "      first: $first"
        found=1
      fi
    done
  done
  [ $found -eq 0 ] && echo "  NO GRANT FOUND across $(echo $BRANCHES|wc -w)x$(echo $NAMES|wc -w) probes"
  rm -f /tmp/lic.$$
done
