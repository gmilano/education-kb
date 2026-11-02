#!/usr/bin/env bash
# p602 held-address set builder — the CONTROL this pass bought the hard way.
#
# 🔴 p602's first sweep built its held set with ONLY the URL form
# (`github.com/<owner>/<repo>`) and measured 3 679 addresses.  The true set at the same
# commit is 6 083: this base writes most addresses as a BACKTICKED BARE SLUG in table
# cells (`| `a-ariff/canvas-mcp` | Canvas | ... |`), not as a link.  2 404 held addresses
# — 39.5 % of the set — were therefore invisible, novelty was reported as 55.0 % when it
# is 50.4 %, and SIX rows were drafted as new finds that this base already held.
#
# 🟢 So a held-set probe must read BOTH forms.  Never grep for `github.com/` alone.
#
# 🔴 And do NOT loosen this to a bare `<word>/<word>` match: that pattern also hits every
# relative path in the prose (`compose/code`, `intel/market.md`) and inflates HELD, which
# is the same error with the opposite sign.  The backtick (or link) delimiter IS the
# discriminator between "an address this base holds" and "a path in a sentence".
#
#   heldset.sh <repo-root> > held.txt
set -uo pipefail
ROOT="${1:?repo root}"
cd "$ROOT"
{
  grep -rhoE 'github\.com/[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*' \
       agents repos verticals intel compose --include=*.md --include=*.tsv 2>/dev/null \
    | sed 's#.*github\.com/##'
  grep -rhoE '`[A-Za-z0-9][A-Za-z0-9._-]{0,38}/[A-Za-z0-9][A-Za-z0-9._-]{0,60}`' \
       agents repos verticals intel compose --include=*.md --include=*.tsv 2>/dev/null \
    | tr -d '`'
} | tr 'A-Z' 'a-z' | sed 's#\.git$##' | sort -u
