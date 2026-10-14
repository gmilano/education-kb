#!/usr/bin/env bash
# p205 — TITLE-ANCHORED licence classification.
#
# WHY THIS EXISTS. p203 shipped compose/code/p203-grant-blob-reader/classify.sh
# and p204 used it. Its branches test the WHOLE body, in an order that puts the
# AGPL first. Three licences NAME OTHER LICENCES in their own text:
#
#   * GPL-3.0  section 13 ..... "GNU Affero General Public License"
#   * MPL-2.0  section 1.12 ... "Secondary License means ... the GNU Affero
#                                General Public License, Version 3.0"
#   * ECL-2.0  paragraph 1 .... "the Apache 2.0 license, modified ..."
#
# So a body-wide search classifies GPL-3.0 and MPL-2.0 as AGPL-3.0, and would
# classify ECL-2.0 as Apache-2.0 if it reached that branch (it does not — ECL is
# absent from p203's table entirely and falls through to UNRECOGNISED).
#
# THE FIX: a licence NAMES ITSELF AT THE TOP. Classify on a title window first;
# only fall back to a body-wide search when the title decides nothing. Verified
# against 12 real bodies in ./fixtures — see test_classify.sh.
#
# NO NETWORK: sourceable and testable offline, per p203's seam.

_norm() { printf '%s' "${1-}" | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' ' '; }

# classify_grant "<licence body>" -> one family token on stdout.
classify_grant() {
  local body norm title
  norm=$(_norm "${1-}")
  [ -z "$norm" ] && { echo "EMPTY"; return; }
  title=$(printf '%s' "$norm" | cut -c1-300)

  # --- 1. TITLE LINE. A licence names itself on a line of its own. Anchoring on
  # a LINE (not a character window) survives a repo that prefixes its grant with
  # a legal notice -- kaldi-asr/kaldi puts ~1.5 kB of copyright-header prose
  # above the Apache text, which a first-300-chars window misses entirely.
  local tl n
  n=$(printf '%s\n' "${1-}" | grep -niE '^[[:space:]]*(the )?(gnu (affero |lesser )?general public license|apache license|mozilla public license|eclipse public license|educational community license|business source license|server side public license|cc0 1\.0 universal|attribution[-a-za-z0-9. ]*international|mit license|bsd [0-9]-clause)' | head -1 | cut -d: -f1)
  if [ -n "$n" ]; then
    tl=$(_norm "$(printf '%s\n' "${1-}" | sed -n "${n},$((n+2))p")")
    case "$tl" in
      *"educational community license"*)      echo "ECL-2.0";       return ;;
      *"business source license"*)            echo "NON-OSI-BSL";   return ;;
      *"server side public license"*)         echo "NON-OSI-SSPL";  return ;;
      *"gnu affero general public license"*)  echo "AGPL-3.0";      return ;;
      *"mozilla public license"*)             echo "MPL-2.0";       return ;;
      *"eclipse public license"*)             echo "EPL";           return ;;
      *"gnu lesser general public license"*)
        case "$tl" in
          *"version 3"*) echo "LGPL-3.0" ;; *"version 2.1"*) echo "LGPL-2.1" ;;
          *)             echo "LGPL" ;;
        esac; return ;;
      *"gnu general public license"*)
        case "$tl" in
          *"version 3"*) echo "GPL-3.0" ;; *"version 2"*) echo "GPL-2.0" ;;
          *)             echo "GPL-unversioned" ;;
        esac; return ;;
      *"apache license"*)                     echo "Apache-2.0";    return ;;
      *"cc0 1.0 universal"*)                  echo "CC0-1.0";       return ;;
      *"attribution-noncommercial"*)          echo "CC-BY-NC";      return ;;
      *"attribution-sharealike"*)             echo "CC-BY-SA-4.0";  return ;;
      *"attribution 4.0 international"*)      echo "CC-BY-4.0";     return ;;
      *"mit license"*)                        echo "MIT";           return ;;
    esac
  fi

  # --- 2. CC DEED. Some repos ship the human-readable SUMMARY, not the
  # instrument. It is a grant signal, but it is not the licence text, so it is
  # reported with a -DEED suffix and must not be quoted as the instrument.
  case "$norm" in
    *"human-readable summary of"*|*"not a substitute for"*)
      case "$norm" in
        *"/by-sa/"*) echo "CC-BY-SA-4.0-DEED"; return ;;
        *"/by-nc/"*) echo "CC-BY-NC-DEED";     return ;;
        *"/by/"*)    echo "CC-BY-4.0-DEED";    return ;;
        *"/zero/"*)  echo "CC0-1.0-DEED";      return ;;
      esac ;;
  esac

  # --- 3. TWO-SCOPE. A file with BOTH a content heading and a software heading
  # grants two different things under two different instruments. One token
  # cannot describe it, so refuse to emit one (this is ACTION PB's whole point).
  if [ "$(scope_headings "${1-}")" -ge 2 ]; then echo "TWO-SCOPE"; return; fi

  # --- 4. BODY FALLBACK, for short/bare grants with no title line.
  case "$norm" in
    *"permission is hereby granted, free of charge"*)  echo "MIT" ;;
    *"redistribution and use in source and binary"*)
      case "$norm" in
        *"neither the name"*) echo "BSD-3-Clause" ;;
        *)                    echo "BSD-2-Clause" ;;
      esac ;;
    *"creative commons"*)                              echo "CC-unversioned" ;;
    *"fair code"*|*"fair-code"*)                       echo "NON-OSI-faircode" ;;
    *"all rights reserved"*)                           echo "NON-OSI-proprietary" ;;
    *)                                                 echo "UNRECOGNISED" ;;
  esac
}

# scope_headings "<body>" -> count of scope headings (Carpentries two-scope shape).
scope_headings() {
  printf '%s\n' "${1-}" | grep -ciE '^#+ *(software|instructional material)' || true
}
