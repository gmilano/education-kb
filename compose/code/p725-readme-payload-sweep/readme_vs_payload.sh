#!/usr/bin/env bash
# Gap 269 instrument: README licence ASSERTION vs LICENSE PAYLOAD, read first-hand.
# Oracles: raw.githubusercontent.com only (github.com/api.github.com are 403 here).
# P713: any transient 000 is retried; success on any probe counts as success.
set -u
RAW=https://raw.githubusercontent.com

fetch() { # url -> stdout body, empty on failure; retries per P713
  local u=$1 b=""
  for i in 1 2 3; do
    b=$(curl -s --max-time 20 -w '\n%{http_code}' "$u" 2>/dev/null)
    local code=${b##*$'\n'}
    if [ "$code" = "200" ]; then printf '%s' "${b%$'\n'*}"; return 0; fi
    [ "$code" = "404" ] && return 1
  done
  return 1
}

# classify licence family from a licence-file payload.
# CRITICAL (P7xx): the discriminator is the TITLE WINDOW, not the body.
# GPL-3.0 names "GNU Affero General Public License" 3x in section 13, so a
# whole-body AGPL-first match reads EVERY GPL-3.0 payload as AGPL.
family_of_payload() {
  local t=$1
  [ -z "$t" ] && { echo "EMPTY"; return; }
  # title window: first 5 non-empty lines, lowercased, whitespace collapsed
  local title
  title=$(printf '%s' "$t" | grep -v '^[[:space:]]*$' | head -5 | tr 'A-Z' 'a-z' | tr -s ' \t\n' ' ')
  case "$title" in
    *"gnu affero general public license"*) echo "AGPL"; return;;
    *"gnu lesser general public license"*) echo "LGPL"; return;;
    *"gnu general public license"*)         echo "GPL";  return;;
    *"apache license"*)                     echo "Apache"; return;;
    *"mozilla public license"*)              echo "MPL"; return;;
    *"eclipse public license"*)              echo "EPL"; return;;
    *"mit license"*|*"the mit license"*)     echo "MIT"; return;;
    *"bsd "*|*"bsd-"*)                       echo "BSD"; return;;
    *"creative commons"*)                    echo "CC"; return;;
    *"unlicense"*)                           echo "Unlicense"; return;;
    *"do what the fuck you want"*)           echo "WTFPL"; return;;
    *"isc license"*)                         echo "ISC"; return;;
  esac
  # fall back to body only for families whose files carry no title convention
  local n; n=$(printf '%s' "$t" | tr 'A-Z' 'a-z' | tr -s ' \t\n' ' ')
  case "$n" in
    *"permission is hereby granted, free of charge"*) echo "MIT"; return;;
    *"redistribution and use in source and binary forms"*) echo "BSD"; return;;
    *"creativecommons.org/licenses"*) echo "CC"; return;;
    *"public domain"*) echo "Unlicense"; return;;
  esac
  echo "OTHER"
}

# extract a licence ASSERTION from README prose/badges
assert_of_readme() {
  local t=$1 n
  n=$(printf '%s' "$t" | tr -s ' \t' ' ')
  # badge form: license-MIT-, licence-Apache%202.0-, License-GPLv3-
  local b
  b=$(printf '%s' "$n" | grep -oiE 'licen[sc]e-[A-Za-z0-9%._+-]{2,24}-(blue|green|yellow|red|orange|brightgreen|lightgrey|informational|blueviolet|success|important|critical|inactive)' | head -1)
  if [ -z "$b" ]; then
    b=$(printf '%s' "$n" | grep -oiE 'licen[sc]ed under (the )?[A-Za-z0-9 .+-]{2,30}' | head -1)
  fi
  if [ -z "$b" ]; then
    b=$(printf '%s' "$n" | grep -oiE 'licen[sc]e:? \**(the )?[A-Za-z0-9 .+-]{2,30}' | head -1)
  fi
  if [ -z "$b" ]; then
    b=$(printf '%s' "$n" | grep -oiE 'creativecommons\.org/licenses/[a-z-]+' | head -1)
  fi
  [ -z "$b" ] && { echo ""; return; }
  local l; l=$(printf '%s' "$b" | tr 'A-Z' 'a-z')
  case "$l" in
    *agpl*|*"affero"*) echo "AGPL";;
    *lgpl*) echo "LGPL";;
    *gpl*)  echo "GPL";;
    *apache*) echo "Apache";;
    *mit*)  echo "MIT";;
    *bsd*)  echo "BSD";;
    *mpl*|*mozilla*) echo "MPL";;
    *epl*|*eclipse*) echo "EPL";;
    *"cc by"*|*cc-by*|*"creative commons"*|*"licenses/by"*|*creativecommons*) echo "CC";;
    *unlicense*|*"public domain"*) echo "Unlicense";;
    *wtfpl*) echo "WTFPL";;
    *) echo "UNPARSED";;
  esac
}

one() {
  local url=$1 slug
  slug=${url#https://github.com/}
  local rd="" ; rd=$(fetch "$RAW/$slug/HEAD/README.md") || rd=""
  [ -z "$rd" ] && { rd=$(fetch "$RAW/$slug/HEAD/readme.md") || rd=""; }
  local assert=""; [ -n "$rd" ] && assert=$(assert_of_readme "$rd")

  local pay="" pf="" pname=""
  # Filename list: COPYING.txt is the GNU convention. Omitting it biases the
  # sweep's blind spot INTO the copyleft family — the dangerous direction.
  for f in LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt COPYING.md copying.txt \
           LICENCE LICENCE.txt LICENSE-MIT LICENSE-APACHE LICENSE.rst \
           license license.txt license.md licence LICENSE.html COPYRIGHT; do
    pay=$(fetch "$RAW/$slug/HEAD/$f") && { pname=$f; break; } || pay=""
  done
  if [ -n "$pay" ]; then pf=$(family_of_payload "$pay"); else pf="NONE"; fi

  # P704: STORED convention. Command substitution strips the trailing newline,
  # so bytes are re-measured with curl's own size_download, never from $pay.
  local bytes=0
  if [ -n "$pname" ]; then
    bytes=$(curl -s --max-time 20 -o /dev/null -w '%{size_download}' "$RAW/$slug/HEAD/$pname")
  fi
  local verdict
  if [ -z "$rd" ]; then verdict="NO_README"
  elif [ -z "$assert" ]; then verdict="NO_ASSERTION"
  elif [ "$pf" = "NONE" ]; then verdict="UNGRANTED"
  elif [ "$assert" = "UNPARSED" ]; then verdict="UNPARSED_ASSERTION"
  elif [ "$assert" = "$pf" ]; then verdict="AGREE"
  elif [ "$assert" = "CC" ] && { [ "$pf" = "MIT" ] || [ "$pf" = "Apache" ] || [ "$pf" = "BSD" ] || [ "$pf" = "GPL" ] || [ "$pf" = "AGPL" ]; }; then
    # README asserts a CONTENT licence, payload grants the CODE: two layers,
    # both can be correct. Flagging this MISGRANTED manufactures a false mismatch.
    verdict="DUAL_LAYER"
  else verdict="MISGRANTED"
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$assert" "$pf" "$pname" "$bytes" "$verdict"
}

if [ $# -lt 1 ]; then
  echo "usage: $0 <file-of-github-urls> [--jobs N]" >&2
  echo "  reads one https://github.com/owner/repo per line; writes TSV to stdout" >&2
  exit 2
fi
IN=$1
[ -s "$IN" ] || { echo "refusing: input '$IN' is empty or missing" >&2; exit 2; }
export -f one fetch family_of_payload assert_of_readme
export RAW
JOBS=${3:-12}
printf 'slug\treadme_assert\tpayload_family\tpayload_file\tbytes\tverdict\n'
grep -E '^https://github\.com/' "$IN" | xargs -P "$JOBS" -I{} bash -c 'one "$@"' _ {}
