#!/usr/bin/env bash
# p870 -- 869-G1: HEAD-sha identity as a duplicate detector over the FULL counted population.
# Channel: git ls-remote, which p869 grounded as this base's existence predicate (the metadata
# index is ~82% false-absent when it reports an absence, so it cannot be the identity channel).
# Prints one row per address.  Grouping is done downstream so the raw record stays auditable.
set -u
probe() {
  a="$1"
  s=$(GIT_TERMINAL_PROMPT=0 timeout 60 git ls-remote "https://github.com/$a" HEAD 2>/dev/null \
        | awk 'NR==1{print $1}')
  if [ -z "$s" ]; then
    # one retry at 3s spacing -- p869 measured that an unpaced sweep MANUFACTURES absence
    sleep 3
    s=$(GIT_TERMINAL_PROMPT=0 timeout 60 git ls-remote "https://github.com/$a" HEAD 2>/dev/null \
          | awk 'NR==1{print $1}')
  fi
  [ -z "$s" ] && s="NO-HEAD"
  printf '%s\t%s\n' "$a" "$s"
}
export -f probe
tail -n +2 "$1" | cut -f1 | sort -u | xargs -P 4 -I{} bash -c 'probe "$@"' _ {}
