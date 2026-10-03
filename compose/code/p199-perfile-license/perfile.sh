#!/bin/bash
# P186, finally built -- the license of a piece whose LICENSE file bounds ITSELF.
#
# Two pieces in this KB declare a scope narrower than the tree and delegate the exceptions to the
# files: `UCL-INGI/INGInious` ("Most of the files ... are distributed under the GNU AGPL v3 licence.
# If it is not the case, this is clearly indicated in the files.") and
# `1EdTech/openbadges-specification` (one version ceded, two silent in the same tree).  For both,
# "the license of the repo" is a MALFORMED phrase, and this KB was quoting INGInious as AGPL-3.0
# entire.
#
# Scope, as action 3 of pass 69 bounded it: do NOT walk whole trees -- directory listing is only
# open through WebFetch and is not scriptable.  Read the HEADERS of the ENTRY files and publish the
# MOST RESTRICTIVE license found as the quotable one.
#
# TSV: repo · path · http · header_license · note
repo="$1"; shift
for f in "$@"; do
  body=$(curl -sf --max-time 15 "https://raw.githubusercontent.com/$repo/HEAD/$f" 2>/dev/null)
  if [ -z "$body" ]; then printf '%s\t%s\t404\t-\t-\n' "$repo" "$f"; continue; fi
  head40=$(printf '%s' "$body" | head -40)
  lic=$(printf '%s' "$head40" | grep -oiE '(AGPL[- ]?v?3|GNU Affero[A-Za-z ]*|Apache License[, ]*Version 2\.0|Apache-2\.0|MIT License|MIT licen[cs]e|BSD[- ][0-9]-Clause|LGPL[- ]?v?[0-9]|GPL[- ]?v?[0-9]|CC[ -]BY[A-Z-]*|public domain)' | head -1)
  [ -z "$lic" ] && lic="NO-HEADER-LICENSE"
  note=$(printf '%s' "$head40" | grep -oiE 'see the LICEN[CS]E|under the terms of|SPDX-License-Identifier:[^ ]*' | head -1)
  [ -z "$note" ] && note="-"
  printf '%s\t%s\t200\t%s\t%s\n' "$repo" "$f" "$lic" "$note"
done
