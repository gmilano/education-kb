#!/usr/bin/env bash
# defbranch.sh — read each address's DEFAULT BRANCH from the remote HEAD symref.
# Sizes P109-E: p107's head_sha40 fell back to refs/heads/main then
# refs/heads/master, so it is the wrong commit for every repo whose default
# branch is neither. `ls-remote --symref` states the default branch outright.
# Output TSV: slug rc default_branch has_main has_master
set -uo pipefail
cd "$(dirname "$0")"
printf 'slug\trc\tdefault_branch\thas_main\thas_master\n'
while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  out=$(GIT_TERMINAL_PROMPT=0 timeout 60 git ls-remote --symref \
        "https://github.com/$slug" HEAD 'refs/heads/main' 'refs/heads/master' 2>/dev/null); rc=$?
  if [ $rc -ne 0 ]; then printf '%s\t%s\t-\t-\t-\n' "$slug" "$rc"; continue; fi
  db=$(printf '%s\n' "$out" | awk '/^ref: /{sub("refs/heads/","",$2); print $2; exit}')
  hm=$(printf '%s\n' "$out" | grep -cE $'\trefs/heads/main$')
  hM=$(printf '%s\n' "$out" | grep -cE $'\trefs/heads/master$')
  printf '%s\t0\t%s\t%s\t%s\n' "$slug" "${db:--}" "$hm" "$hM"
done < "${1:-addresses.txt}"
