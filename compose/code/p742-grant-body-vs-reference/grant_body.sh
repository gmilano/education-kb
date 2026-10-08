#!/usr/bin/env bash
# p742-grant-body-vs-reference
#
# Decides whether a repository's licence file carries an actual GRANT BODY,
# rather than whether a reference inside it resolves.
#
# Why this exists (P742): pass 57 filed `openeducat/openeducat_erp` as having no
# grant because its LICENSE defers to a COPYRIGHT file that returns 404 at all
# three spellings. The 404s are real. The conclusion was wrong: line 4 of the
# same LICENSE reads "published under the GNU LESSER GENERAL PUBLIC LICENSE,
# Version 3 (LGPLv3), as included below" -- and it is included below, 8241 B of
# it. Resolving the reference and detecting the grant are different tests, and
# they disagree precisely on repos that separate ATTRIBUTION from GRANT, which
# is the GNU house convention. So the false negatives concentrate in the
# copyleft family (P730a) -- the expensive direction (P701).
#
# NAMED-SAMPLE SHAPE, deliberately (P744). This takes slugs as arguments. It
# does NOT enumerate a shelf: in this environment the request classifier denies
# bulk enumeration of third-party slugs even though raw.githubusercontent.com
# answers 200 on every probe. Reachability and permission are orther axes.
# Consequence: results from this tool are a convenience sample, so it prints
# counts and REFUSES to print a rate (see the footer).
#
# Usage:  ./grant_body.sh owner/repo [owner/repo ...]
#         ./grant_body.sh --self-test
#
# Oracles: raw.githubusercontent.com (payload), git ls-remote (existence).
# github.com and api.github.com are unusable here -- the latter answers 200 on
# its bare host and 403 on every third-party /repos/ endpoint, with a
# nonexistent-repo control that is ALSO 403, so it cannot even confirm
# existence (P745).

set -uo pipefail

RAW="https://raw.githubusercontent.com"
TIMEOUT="${GRANT_BODY_TIMEOUT:-25}"

# 19 filenames. COPYING/COPYING.txt per P727; lowercase license.txt per P747b.
FILENAMES=(
  LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md License license license.txt
  COPYING COPYING.txt COPYING.md COPYING.LESSER COPYRIGHT
  LICENSE-MIT LICENSE-APACHE NOTICE LICENSE.rst licence.txt LICENSE.html
)

# Grant-body phrases: a licence TITLE, or an operative granting clause.
# Matched case-insensitively. A file containing none of these asserts no grant.
GRANT_RE='GNU AFFERO GENERAL PUBLIC LICENSE|GNU LESSER GENERAL PUBLIC LICENSE|GNU GENERAL PUBLIC LICENSE|Apache License|MIT License|BSD .{0,20}License|Mozilla Public License|Eclipse Public License|Business Source License|Creative Commons|ISC License|The Unlicense|Permission is hereby granted|Redistribution and use in source and binary forms|Licensed under the Apache License|TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION'

# Family is read from the TITLE WINDOW (first 40 lines), never the whole body:
# GPL-3.0 section 13 names the Affero licence three times, so a whole-body
# AGPL-first match inverts every GPL-3.0 file (P726).
TITLE_WINDOW=40

classify_family() {
  local f="$1" head_txt
  head_txt="$(head -n "$TITLE_WINDOW" "$f")"
  if   grep -qiE 'GNU AFFERO GENERAL PUBLIC LICENSE' <<<"$head_txt"; then echo AGPL
  elif grep -qiE 'GNU LESSER GENERAL PUBLIC LICENSE' <<<"$head_txt"; then echo LGPL
  elif grep -qiE 'GNU GENERAL PUBLIC LICENSE'        <<<"$head_txt"; then echo GPL
  elif grep -qiE 'Apache License'                    <<<"$head_txt"; then echo Apache
  elif grep -qiE 'MIT License|Permission is hereby granted' <<<"$head_txt"; then echo MIT
  elif grep -qiE 'Mozilla Public License'            <<<"$head_txt"; then echo MPL
  elif grep -qiE 'Eclipse Public License'            <<<"$head_txt"; then echo EPL
  elif grep -qiE 'Business Source License'           <<<"$head_txt"; then echo BSL
  elif grep -qiE 'Creative Commons'                  <<<"$head_txt"; then echo CC
  elif grep -qiE 'Redistribution and use in source'  <<<"$head_txt"; then echo BSD
  elif grep -qiE 'ISC License'                       <<<"$head_txt"; then echo ISC
  elif grep -qiE 'The Unlicense'                     <<<"$head_txt"; then echo Unlicense
  else echo OTHER
  fi
}

# Does the file merely POINT somewhere, without granting anything itself?
has_reference() { grep -qiE 'please see|refer to|see the .{0,20}file|included in the file' "$1"; }

n_total=0; n_grant=0; n_refonly=0; n_nopayload=0; n_absent=0

printf 'slug\tfile\tbytes\tfamily\tgrant_body\treference\tverdict\n'

for slug in "$@"; do
  n_total=$((n_total+1))
  found=""
  for fn in "${FILENAMES[@]}"; do
    tmp="$(mktemp)"
    code="$(curl -sS -o "$tmp" -w '%{http_code}' -m "$TIMEOUT" "$RAW/$slug/HEAD/$fn" 2>/dev/null)"
    if [ "$code" = "200" ] && [ -s "$tmp" ]; then found="$tmp:$fn"; break; fi
    rm -f "$tmp"
  done

  if [ -z "$found" ]; then
    # Distinguish "exists but ungranted" from "does not exist" -- ls-remote is
    # the ONLY existence oracle available here (P745).
    if git ls-remote "https://github.com/$slug" >/dev/null 2>&1; then
      printf '%s\t-\t0\tNONE\tno\t-\tUNGRANTED\n' "$slug"; n_nopayload=$((n_nopayload+1))
    else
      printf '%s\t-\t0\t-\tno\t-\tREPO_ABSENT\n' "$slug"; n_absent=$((n_absent+1))
    fi
    continue
  fi

  tmp="${found%%:*}"; fn="${found##*:}"
  bytes="$(wc -c < "$tmp" | tr -d ' ')"
  ref=no; has_reference "$tmp" && ref=yes

  if grep -qiE "$GRANT_RE" "$tmp"; then
    fam="$(classify_family "$tmp")"
    # THE P742 CASE: a reference present AND a grant body present. Pass 57 read
    # the reference and stopped; the grant is what governs.
    if [ "$ref" = yes ]; then
      printf '%s\t%s\t%s\t%s\tyes\tyes\tGRANTED_DESPITE_REFERENCE\n' "$slug" "$fn" "$bytes" "$fam"
    else
      printf '%s\t%s\t%s\t%s\tyes\tno\tGRANTED\n' "$slug" "$fn" "$bytes" "$fam"
    fi
    n_grant=$((n_grant+1))
  else
    # A licence-named artefact with no grant in it: the genuine
    # "reference-to-nothing" / filename-without-content shape (P725b).
    printf '%s\t%s\t%s\tNONE\tno\t%s\tARTEFACT_WITHOUT_GRANT\n' "$slug" "$fn" "$bytes" "$ref"
    n_refonly=$((n_refonly+1))
  fi
  rm -f "$tmp"
done

{
  echo
  echo "# n=$n_total  granted=$n_grant  artefact_without_grant=$n_refonly  ungranted=$n_nopayload  repo_absent=$n_absent"
  echo "# NO RATE IS PRINTED. Slugs are supplied by name, so this is a convenience"
  echo "# sample, not a draw from the shelf (P744). Publishing a percentage from it"
  echo "# would invite exactly the inference pass 57 was careful to avoid when it"
  echo "# published its sweep's 31% false-positive rate alongside its count."
} >&2
