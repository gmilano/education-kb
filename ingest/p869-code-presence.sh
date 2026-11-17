#!/usr/bin/env bash
# p869 -- 868-G1: a CODE-PRESENCE channel for the domain predicate.
# 868-G1's mechanism: a curated list's description IS a description of its subject, so no
# word list can separate a list from a buildable thing.  The discriminating feature is
# whether the repository CONTAINS CODE.
# Channel: search/repositories reports `language` (null when the repo carries no recognised
# source) and `size` (KB).  A TREE-FREE PROXY, declared as one; p869 validates it against
# real `git ls-tree` listings on a subsample (see p869-tree-validate.sh).
#
# 🔴 DRAFT 1 OF THIS SCRIPT DEFEATED ITSELF and the defect is recorded rather than hidden:
# on an API error `gh --jq` prints multi-line error JSON to STDOUT, `cut -f1` took a brace
# as a language, and 134 inputs produced 251 output lines.  Every field is now newline-
# stripped and validated before it is printed, and one input produces exactly one row.
set -u
printf 'address\tlanguage\tsize_kb\tcode_presence\n'
while IFS= read -r a; do
  [ -z "$a" ] && continue
  raw=$(gh api -X GET search/repositories -f q="repo:$a" 2>/dev/null)
  lang=$(printf '%s' "$raw" | jq -r '(.items[0].language // "null")' 2>/dev/null | tr -d '\n\r\t' | head -c 40)
  size=$(printf '%s' "$raw" | jq -r '(.items[0].size // -1)'        2>/dev/null | tr -d '\n\r\t' | head -c 12)
  tc=$(  printf '%s' "$raw" | jq -r '(.total_count // -1)'          2>/dev/null | tr -d '\n\r\t' | head -c 12)
  case "$tc" in ''|-1|0) printf '%s\tREFUSED\t-\tUNRESOLVED\n' "$a"; continue ;; esac
  case "$lang" in
    ''|null)              cp="NO-CODE" ;;
    Markdown|TeX|CSS|Nix) cp="NO-CODE" ;;
    *)                    cp="CODE" ;;
  esac
  printf '%s\t%s\t%s\t%s\n' "$a" "${lang:-null}" "${size:--1}" "$cp"
done
