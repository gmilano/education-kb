#!/bin/bash
# p772 — probe ONE displayed address on the ref channel. Written from scratch.
s="$1"
export GIT_TERMINAL_PROMPT=0
out=$(timeout 30 git ls-remote --symref "https://github.com/$s" HEAD 2>&1)
rc=$?
sym=$(printf '%s\n' "$out" | awk '/^ref:/{print $2; exit}')
hd=$(printf '%s\n' "$out" | awk '/\tHEAD$/{print $1; exit}')
if [ -n "$hd" ]; then
  printf '%s\tRESOLVES\t%s\t%s\n' "$s" "${sym:-NONE}" "${hd:0:12}"
elif printf '%s' "$out" | grep -q "could not read Username\|Authentication failed\|Repository not found"; then
  printf '%s\tABSENT-OR-PRIVATE\t-\t-\n' "$s"
elif [ $rc -eq 124 ]; then
  printf '%s\tTIMEOUT\t-\t-\n' "$s"
else
  printf '%s\tOTHER\t-\t%s\n' "$s" "$(printf '%s' "$out" | tr '\t\n' '  ' | cut -c1-80)"
fi
