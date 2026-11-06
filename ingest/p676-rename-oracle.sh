#!/usr/bin/env bash
# p676 — rename oracle on the HTTP channel. GitHub answers a RENAMED address with
# 301 + Location: the new slug. A live, never-renamed address answers 200.
# This disambiguates 671-J's "owner indexed, repo absent" third cause:
#   301 -> renamed (Location names the truth)
#   200 -> live at its own address, merely ABSENT FROM THE SEARCH INDEX
#   404 -> gone
# TSV: slug  http  location
set -u
for slug in "$@"; do
  r=$(curl -sI --max-time 25 "https://github.com/$slug")
  code=$(printf '%s' "$r" | sed -n 's#^HTTP/[0-9.]* \([0-9]*\).*#\1#p' | head -1)
  loc=$(printf '%s' "$r" | sed -n 's#^[Ll]ocation: *##p' | head -1 | tr -d '\r')
  printf '%s\t%s\t%s\n' "$slug" "${code:-NONE}" "${loc:--}"
done
