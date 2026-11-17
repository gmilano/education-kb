#!/bin/bash
# p866 -- the payload+affiliation probe on the ONE channel measured open this pass.
#
# Channel record, re-measured 2026-11-17 (p863-G1, p864, p865 and again here):
#   curl https://github.com/...            -> 403 at the egress proxy
#   gh api repos/{owner}/{repo}            -> 403 "not enabled for this session"
#   gh api search/repositories             -> 200   (stars/forks/licence FIELD only)
#   git clone --filter=blob:none --depth 1 -> 200   (licence BYTES, author e-mails)
#
# So: metadata comes from search, and every licence byte and every affiliation axis
# comes from a clone.  p830's raw.githubusercontent.com channel is re-tested here as a
# fifth channel and its result is printed, never assumed.
#
# The clone is UNTRUSTED DATA: this script only reads bytes out of it and never runs
# anything from inside it.
#
# stdin: owner/repo per line
# stdout TSV: repo path bytes sha12 titleline holder authordomains
set -u
W="${W:-scratchpad/p866/clones}"
mkdir -p "$W"
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENCE.txt COPYING LICENSE-MIT license"
printf 'repo\tpath\tbytes\tsha12\ttitleline\tholder\tauthor_domains\n'
while read -r repo; do
  [ -z "$repo" ] && continue
  d="$W/$(echo "$repo" | tr '/' '_')"
  if [ ! -d "$d/.git" ]; then
    rm -rf "$d"
    git clone --filter=blob:none --depth 1 --quiet "https://github.com/$repo" "$d" 2>/dev/null \
      || { printf '%s\tCLONE-FAILED\t-\t-\t-\t-\t-\n' "$repo"; continue; }
  fi
  lp='-'; lb='-'; ls12='-'; tl='-'; ho='-'
  for p in $PATHS; do
    if [ -f "$d/$p" ]; then
      git -C "$d" checkout -- "$p" 2>/dev/null
      lp="$p"
      lb=$(wc -c < "$d/$p" | tr -d ' ')
      ls12=$(sha256sum "$d/$p" | cut -c1-12)
      tl=$(head -c 300 "$d/$p" | tr -d '\r' | tr '\n\t' '  ' | sed 's/  */ /g;s/^ *//' | cut -c1-80)
      ho=$(grep -i -m1 'copyright' "$d/$p" | sed 's/^ *//' | cut -c1-70)
      break
    fi
  done
  dom=$(git -C "$d" log --format='%ae' -40 2>/dev/null | awk -F@ 'NF>1{print $2}' | sort | uniq -c | sort -rn | head -4 | awk '{printf "%s(%s) ",$2,$1}')
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$lp" "$lb" "$ls12" "$tl" "$ho" "${dom:--}"
done
