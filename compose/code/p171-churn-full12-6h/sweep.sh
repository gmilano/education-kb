#!/usr/bin/env bash
# ACTION JJ - full-12 >=6 h churn sweep. Primary channel: git ls-remote.
# Emits "repo<TAB>sha12". Avoids the T173 instrument fault by NOT using --symref:
# `git ls-remote URL HEAD` emits one record "sha<TAB>HEAD", so there is no alternating-line parse.
set -u
while read -r repo; do
  [ -z "$repo" ] && continue
  sha=$(git ls-remote "https://github.com/${repo}" HEAD 2>/dev/null | awk 'NR==1{print substr($1,1,12)}')
  printf '%s\t%s\n' "$repo" "${sha:-UNREACHABLE}"
done < "$1"
