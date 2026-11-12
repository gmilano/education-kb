#!/bin/bash
# p783 authoritative existence sweep: git ls-remote per T824.
# A `repo:` 422 (p780's T810) cannot distinguish deleted from not-visible; ls-remote can resolve.
slug="$1"
out=$(GIT_TERMINAL_PROMPT=0 GIT_ASKPASS=/bin/true timeout 30 git ls-remote --symref "https://github.com/${slug}" HEAD 2>&1)
rc=$?
if [ $rc -eq 0 ] && [ -n "$out" ]; then
  ref=$(printf '%s' "$out" | awk '/^ref:/{print $2}' | head -1 | sed 's|refs/heads/||')
  head=$(printf '%s' "$out" | awk '/HEAD$/{print substr($1,1,12)}' | head -1)
  printf '%s\tALIVE\t%s\t%s\n' "$slug" "${ref:-?}" "${head:-?}"
else
  reason=$(printf '%s' "$out" | tr '\n' ' ' | sed 's/\t/ /g' | cut -c1-160)
  printf '%s\tFAIL\trc=%s\t%s\n' "$slug" "$rc" "$reason"
fi
