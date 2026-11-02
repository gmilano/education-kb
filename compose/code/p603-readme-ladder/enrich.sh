#!/usr/bin/env bash
# p603 enrichment: recency (treeless bare clone -> committer date + tz offset, the channel
# gate-offset-region places regions with), fabricated-path control, and the repo's OWN
# description text. github.com HTML and the GitHub API are both proxy-blocked this pass
# (403), so there is NO star-count channel: stars are therefore NOT written down.
slug="$1"; br="$2"
W=$(mktemp -d)
d="-"; tz="-"
if timeout 90 git clone --bare --filter=blob:none --depth 1 --quiet "https://github.com/$slug" "$W/b" 2>/dev/null; then
  iso=$(git --git-dir="$W/b" log -1 --format='%cI' HEAD 2>/dev/null)
  d="${iso%T*}"; tz=$(printf '%s' "$iso" | grep -oE '[+-][0-9]{2}:[0-9]{2}$')
fi
ctl=$(curl -sI -o /dev/null -w '%{http_code}' --max-time 15 \
      "https://raw.githubusercontent.com/$slug/$br/LICENSE-FABRICATED-p603-control" 2>/dev/null)
desc=$(curl -sS --max-time 20 "https://raw.githubusercontent.com/$slug/$br/README.md" 2>/dev/null \
  | sed -e 's/<[^>]*>//g' \
  | grep -vE '^\s*$|^\s*!\[|^\s*\[!\[|^\s*\||^\s*[-=]{3,}|img\.shields\.io|^\s*#{1,6}\s*$' \
  | sed -e 's/^#\{1,6\}[[:space:]]*//' -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' \
  | grep -vE '^(Table of Contents|Contents|Installation|License|Licence|Usage|Badges)$' \
  | awk 'length($0)>25' | head -2 | tr '\n' ' ' | tr -s ' ' | cut -c1-260)
rm -rf "$W"
printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$br" "$d" "${tz:--}" "$ctl" "$desc"
