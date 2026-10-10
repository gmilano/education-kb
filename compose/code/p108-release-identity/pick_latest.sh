#!/usr/bin/env bash
# pick_latest.sh — reduce `git ls-remote --tags` output to a PINNABLE RELEASE
# IDENTITY. Reads ls-remote output on stdin, writes TAB-separated:
#
#   tags_uniq  stable_n  prerel_n  latest_stable  latest_stable_sha40
#              prefix_n  latest_prefix  latest_prefix_sha40  class
#
# class is the decision column:
#   semver   — a bare vN.N.N tag exists; pin it
#   prefixed — no bare semver, but a <project>-N.N.N tag exists; pin that
#   stamp    — tags exist but none carries a version; NOT pinnable by version
#   none     — no tags at all
#
# Five rules are load-bearing; each was a wrong answer before it was a rule.
#
# P108-A  `^{}` dereferenced rows go first (inherited from P107-C), else an
#         annotated tag counts twice AND its peeled row can win the sort.
# P108-B  A STABLE tag is `^v?N.N(.N)?$` and nothing else. A suffix (-rc1,
#         -beta, .post1) makes it a PRE-RELEASE: counted, never pinned.
#         "Latest tag" and "latest pinnable release" are different questions.
# P108-C  Ranking is `sort -V`, never `sort`. Lexically v9.0.0 > v10.0.0, so a
#         lexical max hands you a two-major-stale pin and looks right doing it.
# P108-D  A repo with tags and no semver is NOT automatically unreleased. Two
#         different things live there: CI DEPLOY STAMPS
#         (`va-green-dev-2026-08-08T22_31_36+00_00`) which carry no version,
#         and PROJECT-PREFIXED releases (`OpenOLAT_20.3.3`, `dspace-7.6`)
#         which carry a perfectly good one. Collapsing them slanders the second
#         group — and OpenOLAT is an Apache-2.0 LMS, so the slander has a cost.
# P108-E  The prefix lane must anchor the version at END of ref and require a
#         separator, else `green-dev-1791293242` parses as version 1791293242.
# P108-F  Case-duplicate addresses are one repo, not two (github owner/repo is
#         case-insensitive). Handled in census.sh's address list, not here.
# P108-G  A trailing year is a DATE, not a version. `production_16.01.2017`
#         parses as 16.1.2017 and `sort -V` then crowns it the latest release
#         of a repo that has never cut one. CalVer is still honoured because
#         CalVer puts the year FIRST (`dados-2026.07.1`); a date puts it LAST.
#         So: reject when the final numeric component is >= 1900.
set -uo pipefail

in=$(cat)

tags=$(printf '%s\n' "$in" | grep $'\trefs/tags/' | grep -v '\^{}$' || true)
tags_uniq=$(printf '%s\n' "$tags" | grep -c . || true)
names=$(printf '%s\n' "$tags" | sed 's#.*\trefs/tags/##' || true)

sha_of() { printf '%s\n' "$tags" | awk -F'\t' -v t="refs/tags/$1" '$2==t{print $1; exit}'; }

# ---- lane 1: bare semver (P108-B) ----------------------------------------
stable=$(printf '%s\n' "$names" | grep -E '^v?[0-9]+\.[0-9]+(\.[0-9]+)?$' || true)
stable_n=$(printf '%s\n' "$stable" | grep -c . || true)
prerel=$(printf '%s\n' "$names" | grep -E '^v?[0-9]+\.[0-9]+' \
         | grep -vE '^v?[0-9]+\.[0-9]+(\.[0-9]+)?$' || true)
prerel_n=$(printf '%s\n' "$prerel" | grep -c . || true)

latest_name="-"; latest_sha="-"
if [ "${stable_n:-0}" -gt 0 ]; then
  v=$(printf '%s\n' "$stable" | sed 's/^v//' | sort -V | tail -1)   # P108-C
  if printf '%s\n' "$stable" | grep -qx "v$v"; then latest_name="v$v"; else latest_name="$v"; fi
  latest_sha=$(sha_of "$latest_name"); [ -n "$latest_sha" ] || latest_sha="-"
fi

# ---- lane 2: project-prefixed releases (P108-D) ---------------------------
# Require: a non-numeric project prefix, a [-_] separator, then a version that
# ENDS the ref (P108-E). Two dot-components minimum, so a bare build number
# like green-dev-1791293242 cannot qualify.
prefix=$(printf '%s\n' "$names" \
         | grep -E '^[A-Za-z][A-Za-z0-9]*([-_.][A-Za-z0-9]+)*[-_]v?[0-9]+\.[0-9]+(\.[0-9]+)?$' \
         | awk -F'[-_]' '{n=split($NF,p,"."); if(p[n]+0 < 1900) print}' || true)
prefix_n=$(printf '%s\n' "$prefix" | grep -c . || true)

latest_px="-"; latest_px_sha="-"
if [ "${prefix_n:-0}" -gt 0 ]; then
  # Rank on the trailing version only, then recover the full ref name.
  best=$(printf '%s\n' "$prefix" \
         | sed -E 's/^(.*[-_])v?([0-9]+\.[0-9]+(\.[0-9]+)?)$/\2\t\1\2/' \
         | sort -V -k1,1 | tail -1 | cut -f2)
  # cut -f2 lost a leading v if there was one; match back against the real list.
  latest_px=$(printf '%s\n' "$prefix" | grep -E "^$(printf '%s' "$best" | sed 's/[][\.*^$/]/\\&/g')$" | head -1)
  [ -n "$latest_px" ] || latest_px=$(printf '%s\n' "$prefix" | sed -E 's/^(.*[-_])v?([0-9]+\.[0-9]+(\.[0-9]+)?)$/\2\t&/' | sort -V -k1,1 | tail -1 | cut -f2)
  latest_px_sha=$(sha_of "$latest_px"); [ -n "$latest_px_sha" ] || latest_px_sha="-"
fi

# ---- class ----------------------------------------------------------------
if   [ "${tags_uniq:-0}" -eq 0 ];  then class="none"
elif [ "${stable_n:-0}"  -gt 0 ];  then class="semver"
elif [ "${prefix_n:-0}"  -gt 0 ];  then class="prefixed"
else                                    class="stamp"
fi

printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
  "${tags_uniq:-0}" "${stable_n:-0}" "${prerel_n:-0}" "$latest_name" "$latest_sha" \
  "${prefix_n:-0}" "$latest_px" "$latest_px_sha" "$class"
