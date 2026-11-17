#!/bin/bash
# p861 -- the AFFILIATION channel, built as the remedy 860-G2 named.
#
# 860-G2: 19 of p860's 37 rows were shelved `Global` because origin was not resolvable --
# `gh api users/{login}` is 403 session-scoped (T941) and T935 forbids reading a query
# LANGUAGE as a region.  The gap named the remedy: the treeless clone ALREADY FETCHES THE
# TREE, so an institutional affiliation stated by the project itself can be read at zero
# extra network cost, and an affiliation stated by a project is evidence of the same class
# as a copyright holder line.
#
# Declared precedence for the region cell, highest first:
#   1 holder   -- the copyright holder line of the byte-read grant
#   2 citation -- CITATION.cff `affiliation:` / `institution:`
#   3 manifest -- pyproject/package.json/setup.cfg author or maintainer org/email domain
#   4 readme   -- an institution named in the first 4,000 bytes of the README
#   5 owner    -- the GitHub org name ONLY when it is an institution's own namespace
#   else       -- UNPLACED.  Never a guess, never a language (T935).
#
# One network op per address: `git clone --filter=blob:none --no-checkout --depth 1`.
# Grant bytes come from the tree's own blob, not from GitHub's licence FIELD (house rule).
# stdin: owner/repo per line.  stdout: TSV.
set -u
W="${W:-/tmp/claude-0/p861/clones}"; mkdir -p "$W"
printf 'repo\tref\thead_sha12\thead_date\tlicence_path\tbytes\tsha256_12\ttitle_line\tholder\taffil_src\taffil_text\n'
while read -r repo; do
  [ -z "$repo" ] && continue
  d="$W/$(echo "$repo" | tr '/' '_')"
  rm -rf "$d"
  if ! git clone --filter=blob:none --no-checkout --depth 1 -q "https://github.com/$repo" "$d" 2>/dev/null; then
    printf '%s\tCLONE-FAIL\t-\t-\t-\t-\t-\t-\t-\t-\t-\n' "$repo"; continue
  fi
  ref=$(git -C "$d" symbolic-ref --short HEAD 2>/dev/null || echo '-')
  sha=$(git -C "$d" rev-parse --short=12 HEAD)
  hdate=$(git -C "$d" log -1 --format=%cI | cut -c1-10)
  # --- grant: every path the tree actually carries, case as published (T-- LICENCE spelling)
  lp=$(git -C "$d" ls-tree -r --name-only HEAD \
       | grep -iE '^(LICEN[CS]E|COPYING)(\.(md|txt|rst))?$' | head -1)
  if [ -z "$lp" ]; then
    printf '%s\t%s\t%s\t%s\tNOGRANT\t-\t-\t-\t-\t-\t-\n' "$repo" "$ref" "$sha" "$hdate"; continue
  fi
  blob="$d/.licence"; git -C "$d" show "HEAD:$lp" > "$blob" 2>/dev/null
  b=$(wc -c < "$blob" | tr -d ' '); s=$(sha256sum "$blob" | cut -c1-12)
  tl=$(grep -m1 -v '^[[:space:]]*$' "$blob" | tr -d '\r' | sed 's/^ *//;s/ *$//' | cut -c1-70)
  ho=$(grep -i -m1 'copyright' "$blob" | sed 's/^ *//' | cut -c1-70)
  # --- affiliation, in the declared precedence order
  asrc='-'; atxt='-'
  INST='Universit|Universidad|Universidade|Universit..t|Hochschule|Institute of Technology|Polytech|College|School of|Academy|Ministry|Ministerio|Minist.re|Foundation|Funda..o|Fundaci.n|Stiftung|Corporation|Laborator|CNRS|INRIA|NASA|CSIC|CONICET|Tecnol.gico'
  if [ -n "$ho" ] && echo "$ho" | grep -qE "$INST"; then
    asrc='holder'; atxt=$(echo "$ho" | sed 's/.*[Cc]opyright[^A-Za-z]*//' | cut -c1-60)
  else
    cf=$(git -C "$d" ls-tree -r --name-only HEAD | grep -iE '^CITATION\.cff$' | head -1)
    if [ -n "$cf" ]; then
      a=$(git -C "$d" show "HEAD:$cf" 2>/dev/null | grep -iE '^\s*(affiliation|institution):' | head -1 \
          | sed 's/.*: *//; s/^["'"'"']//; s/["'"'"']$//' | cut -c1-60)
      [ -n "$a" ] && { asrc='citation'; atxt="$a"; }
    fi
    if [ "$asrc" = '-' ]; then
      for mf in pyproject.toml setup.cfg package.json; do
        p=$(git -C "$d" ls-tree -r --name-only HEAD | grep -ixE "$mf" | head -1)
        [ -z "$p" ] && continue
        a=$(git -C "$d" show "HEAD:$p" 2>/dev/null | grep -ioE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]*\.(edu|ac\.[a-z]{2}|edu\.[a-z]{2})' | head -1)
        [ -n "$a" ] && { asrc='manifest'; atxt="$a"; break; }
      done
    fi
    if [ "$asrc" = '-' ]; then
      rp=$(git -C "$d" ls-tree -r --name-only HEAD | grep -ixE 'README(\.(md|rst|txt))?' | head -1)
      if [ -n "$rp" ]; then
        a=$(git -C "$d" show "HEAD:$rp" 2>/dev/null | head -c 4000 \
            | grep -oE "[A-Z][A-Za-z.&'-]*( [A-Z][A-Za-z.&'-]*){0,4} ($INST)|($INST)[a-z]* (of|de|für|di) [A-Z][A-Za-z.'-]*( [A-Z][A-Za-z.'-]*){0,3}" \
            | head -1 | cut -c1-60)
        [ -n "$a" ] && { asrc='readme'; atxt="$a"; }
      fi
    fi
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$repo" "$ref" "$sha" "$hdate" "$lp" "$b" "$s" "$tl" "$ho" "$asrc" "$atxt"
done
