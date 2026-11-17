#!/usr/bin/env bash
# p869 -- place a row on a MEASURED axis: the commit-author e-mail domains of the last 50
# commits.  A `users.noreply.github.com` majority carries no jurisdiction, so the region is
# REFUSED rather than guessed -- p868's convention, applied here unchanged.
set -u
W=$(mktemp -d); trap 'rm -rf "$W"' EXIT
printf 'address\tcommits\ttop_domains\tregion_signal\n'
while IFS= read -r a; do
  [ -z "$a" ] && continue
  d="$W/$(printf '%s' "$a" | tr '/' '_')"
  GIT_TERMINAL_PROMPT=0 timeout 180 git clone --quiet --filter=blob:none --depth 50 \
    "https://github.com/$a" "$d" >/dev/null 2>&1 || { printf '%s\t-\t-\tCLONE-FAILED\n' "$a"; continue; }
  doms=$(git -C "$d" log -50 --format='%ae' 2>/dev/null | awk -F@ 'NF>1{print tolower($2)}')
  n=$(printf '%s\n' "$doms" | grep -c .)
  top=$(printf '%s\n' "$doms" | sort | uniq -c | sort -rn | head -3 | awk '{printf "%s(%s) ",$2,$1}')
  nore=$(printf '%s\n' "$doms" | grep -c 'users.noreply.github.com')
  if [ "$n" -gt 0 ] && [ "$nore" -ge $(( n / 2 )) ]; then sig="REFUSED-noreply-majority"; else sig="MEASURABLE"; fi
  printf '%s\t%s\t%s\t%s\n' "$a" "$n" "${top% }" "$sig"
  rm -rf "$d"
done
