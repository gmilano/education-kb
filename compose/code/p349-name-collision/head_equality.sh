#!/bin/bash
# `p349-name-collision/head_equality.sh` — the ONLINE half of `ACTION ZZ-ag`.
# Reads the bounded probe list (name <TAB> address) produced offline by
# `name_collision.py probe` and resolves each address's HEAD with `git ls-remote`.
# A group whose members answer with the SAME sha is one repository under two addresses.
#
# Three answer states, kept distinct because p346 paid for collapsing them:
#   ALIAS      — two or more addresses in the group, same HEAD sha
#   DISTINCT   — every address in the group answers with a different sha
#   UNANSWERED — the address does not resolve (gone, renamed, or private)
set -uo pipefail
IN="${1:?usage: head_equality.sh <probes.tsv>}"
printf 'name\taddress\thead\n'
tail -n +2 "$IN" | while IFS=$'\t' read -r name addr; do
  [ -z "${addr:-}" ] && continue
  sha="$(timeout 45 git ls-remote "https://github.com/$addr" HEAD 2>/dev/null | awk 'NR==1{print substr($1,1,12)}')"
  printf '%s\t%s\t%s\n' "$name" "$addr" "${sha:-UNANSWERED}"
done
