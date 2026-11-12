#!/bin/bash
# p783 grant grader: existence on git, grant graded on the BYTES per T822 (grade read from the title line).
slug="$1"
sym=$(GIT_TERMINAL_PROMPT=0 timeout 30 git ls-remote --symref "https://github.com/${slug}" HEAD 2>/dev/null)
if [ -z "$sym" ]; then echo "=== $slug :: GIT FAIL (no such ref) ==="; return 2>/dev/null; exit 0; fi
br=$(printf '%s' "$sym" | awk '/^ref:/{print $2}' | sed 's|refs/heads/||' | head -1)
hd=$(printf '%s' "$sym" | awk '$2=="HEAD"{print substr($1,1,12)}' | head -1)
echo "=== $slug :: branch=$br HEAD=$hd ==="
for f in LICENSE LICENSE.md LICENSE.txt COPYING LICENCE; do
  u="https://raw.githubusercontent.com/${slug}/${br}/${f}"
  code=$(curl -s -o /tmp/g.$$ -w '%{http_code}' --max-time 25 "$u")
  if [ "$code" = "200" ]; then
    printf '  GRANT %-12s %s B  sha256_12=%s\n' "$f" "$(wc -c </tmp/g.$$)" "$(sha256sum /tmp/g.$$|cut -c1-12)"
    printf '  TITLE: %s\n' "$(grep -vE '^[[:space:]]*$' /tmp/g.$$ | head -3 | tr '\n' ' / ' | cut -c1-150)"
  fi
done
rm -f /tmp/g.$$
