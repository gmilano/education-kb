#!/bin/bash
# `ACTION KU` - p178, static half. Enumerate every byte-count call site in this
# repository's instruments and classify it by CHANNEL.
#
# The rule, stated before the census ran:
#   STRIPPING - the bytes pass through a command substitution `$(...)` and are
#               then re-emitted with `printf '%s'`/`echo`. POSIX command
#               substitution deletes ALL trailing newlines, so the count is the
#               file size MINUS its trailing line feed.
#   FULL      - the bytes reach `wc -c` without a command substitution in the
#               path: `wc -c < file`, or `curl ... | wc -c`.
#
# `ACTION KU`'s falsifier: limb 1 if ONE call site explains the short counts;
# limb 2 if MORE THAN ONE does, which makes it a vocabulary defect and not a bug.
set -u
cd "$(dirname "$0")/../../.." || exit 1
printf 'channel\tfile\tline\tidiom\n'
grep -rnE "printf '%s' \"\\\$[A-Za-z_][A-Za-z0-9_]*\" *\| *wc -c|echo \"\\\$[A-Za-z_][A-Za-z0-9_]*\" *\| *wc -c" \
  --include=*.sh --include=*.py compose/code ingest 2>/dev/null \
  | sed -E 's/^([^:]+):([0-9]+):[[:space:]]*(.*)$/STRIPPING\t\1\t\2\t\3/'
grep -rnE "wc -c *< *\"?\\\$?[A-Za-z_/{.]|curl[^|]*\| *wc -c" \
  --include=*.sh --include=*.py compose/code ingest 2>/dev/null \
  | grep -vE "printf '%s'|echo \"\\\$" \
  | sed -E 's/^([^:]+):([0-9]+):[[:space:]]*(.*)$/FULL\t\1\t\2\t\3/'
