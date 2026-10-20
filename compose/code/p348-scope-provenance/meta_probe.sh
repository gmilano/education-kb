#!/bin/sh
# p348 -- the metadata that is first-hand without `api.github.com` (403 here) and
# without `github.com` over curl (403 here too): commits, distinct authors, last
# commit date, and the TIMEZONE DISTRIBUTION of the commit stream, which is this
# base's instrument-placed region channel.
for slug in "$@"; do
  d=$(mktemp -d)
  if git clone --filter=blob:none --no-checkout --quiet "https://github.com/$slug" "$d" 2>/dev/null; then
    c=$(git -C "$d" rev-list --count HEAD 2>/dev/null)
    a=$(git -C "$d" log --format='%an' 2>/dev/null | sort -u | wc -l)
    last=$(git -C "$d" log -1 --format='%ad' --date=short 2>/dev/null)
    first=$(git -C "$d" log --reverse --format='%ad' --date=short 2>/dev/null | head -1)
    tz=$(git -C "$d" log --format='%ad' --date=format:'%z' 2>/dev/null | sort | uniq -c | sort -rn | head -3 | awk '{printf "%s×%s ", $1, $2}')
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$c" "$a" "$first" "$last" "$tz"
  else
    printf '%s\tUNRESOLVED\t-\t-\t-\t-\n' "$slug"
  fi
  rm -rf "$d"
done
