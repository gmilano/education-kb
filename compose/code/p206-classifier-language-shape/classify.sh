#!/usr/bin/env bash
# p206 — LANGUAGE- AND SHAPE-TOLERANT licence classification.
#
# Drop-in replacement for ../p205-grant-classifier-fix/classify.sh, which this
# file keeps honest: p205's title-LINE anchoring is correct and is retained.
# What p206 adds is everything the title line can be WEARING.
#
# MEASURED DEFECTS IN p205 (all reproduced on real bodies in ./fixtures):
#
#   D1 MARKDOWN HEADING   "### GNU GENERAL PUBLIC LICENSE" does not match a
#                         regex anchored at ^[[:space:]]*. The probe skipped the
#                         title and matched the PREAMBLE sentence instead, which
#                         carries no version -> "GPL-unversioned".
#                         cerpus/Edlib, idempiere/idempiere.
#   D2 NARROW WINDOW      A markdown underline ("====") or a blank line pushes
#                         "Version 3, 29 June 2007" to line 4. p205 read n..n+2.
#                         -> "GPL-unversioned" on 13 Moodle-plugin rows.
#   D3 LANGUAGE           The AGPL in PORTUGUESE titles itself "LICENCA PUBLICA
#                         GERAL AFFERO GNU". p205 returns UNRECOGNISED.
#                         portabilis/i-diario, portabilis/pre-matricula-digital.
#                         This is the licence-channel half of ACTION PJ: the
#                         same English-only assumption hid Brazil's national
#                         AI-education policy from the market channel.
#   D4 MISSING FAMILY     Elastic License 2.0 is absent from p205's table, and
#                         it is NON-OSI -- the most commercially consequential
#                         family to return UNRECOGNISED. canyongbs/advisingapp.
#   D5 NARRATIVE GRANT    A body with no title line at all: "Anki is licensed
#                         under the GNU Affero General Public License, version 3
#                         or later". ankitects/anki, pawtograder/assignment-action.
#   D6 STATEMENT, NOT BODY  19 bytes: "License: GNU GPL V3". A grant REFERENCE.
#                         Reported with a -STATEMENT suffix, exactly as p205
#                         reports a CC deed with -DEED: it names a family but it
#                         is not the instrument, so it must not be quoted as one.
#                         frappe/education, UniversalDependencies/UD_Spanish-AnCora.
#
# NOT A CLASSIFIER DEFECT, recorded here because p206's own probe caused it:
#   D7 NOTICE IS A CHANNEL, NOT A BODY. An Apache NOTICE is an attribution file.
#      It carries a grant STATEMENT and belongs in p204's channel taxonomy
#      beside package.json -- it is not a licence body and must not be probed as
#      one. p206 removed NOTICE from the body path list after foradian/fedena
#      returned it. See ./README.md.
#
# NO NETWORK: sourceable and testable offline, per p203's seam.

# Fold accents to ASCII before any case-insensitive match. `tr` and `grep -i`
# are byte-oriented here, so "LICENCA" case-folds and "LICENÇA" does not --
# the defect compose/code/p288-agpl-casefold/ first recorded, met again in a
# second alphabet. Folding first makes one ASCII pattern match every variant.
_fold() {
  # Per-character substitutions, NOT a bracket class: sed here is byte-oriented,
  # so [Çç] would match the individual BYTES of a UTF-8 sequence and corrupt the
  # text instead of folding it. Each accented letter is spelled out.
  # A UTF-8 BOM is not [[:space:]], so `^[[:space:]]*` never reaches a title it
  # precedes -- OS4ED/openSIS-Classic and Berserk-hub150/moodle-ai-skill-navigator
  # both ship one and both lost their GPL version to it. Strip it first.
  printf '%s' "${1-}" | sed -e 's/\xef\xbb\xbf//g' \
    -e 's/\xc3\x87/c/g; s/\xc3\xa7/c/g' \
    -e 's/\xc3\x81/a/g; s/\xc3\x80/a/g; s/\xc3\x82/a/g; s/\xc3\x83/a/g; s/\xc3\x84/a/g' \
    -e 's/\xc3\xa1/a/g; s/\xc3\xa0/a/g; s/\xc3\xa2/a/g; s/\xc3\xa3/a/g; s/\xc3\xa4/a/g' \
    -e 's/\xc3\x89/e/g; s/\xc3\x88/e/g; s/\xc3\x8a/e/g; s/\xc3\x8b/e/g' \
    -e 's/\xc3\xa9/e/g; s/\xc3\xa8/e/g; s/\xc3\xaa/e/g; s/\xc3\xab/e/g' \
    -e 's/\xc3\x8d/i/g; s/\xc3\x8c/i/g; s/\xc3\x8e/i/g; s/\xc3\x8f/i/g' \
    -e 's/\xc3\xad/i/g; s/\xc3\xac/i/g; s/\xc3\xae/i/g; s/\xc3\xaf/i/g' \
    -e 's/\xc3\x93/o/g; s/\xc3\x92/o/g; s/\xc3\x94/o/g; s/\xc3\x95/o/g; s/\xc3\x96/o/g' \
    -e 's/\xc3\xb3/o/g; s/\xc3\xb2/o/g; s/\xc3\xb4/o/g; s/\xc3\xb5/o/g; s/\xc3\xb6/o/g' \
    -e 's/\xc3\x9a/u/g; s/\xc3\x99/u/g; s/\xc3\x9b/u/g; s/\xc3\x9c/u/g' \
    -e 's/\xc3\xba/u/g; s/\xc3\xb9/u/g; s/\xc3\xbb/u/g; s/\xc3\xbc/u/g' \
    -e 's/\xc3\x91/n/g; s/\xc3\xb1/n/g'
}
_norm() { _fold "${1-}" | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' ' '; }

# Strip the costume a title line can wear: markdown heading hashes, bold stars,
# blockquote markers, centring HTML, and leading punctuation. D1.
_undress() {
  _fold "${1-}" |
    sed -e 's/<[^>]*>//g' -e 's/&[a-z]\{2,6\};/ /g' \
        -e 's/^[[:space:]]*[#>*_=-]\{1,8\}[[:space:]]*//'
}

TITLE_RE='^[[:space:]]*(the )?(gnu (affero |lesser )?general public license|licenca publica geral|licencia publica general|apache license|mozilla public license|eclipse public license|educational community license|elastic license|business source license|server side public license|cc0 1\\.0 universal|attribution[-a-za-z0-9. ]*international|mit license|bsd [0-9]-clause)'

# classify_grant "<licence body>" -> one family token on stdout.
classify_grant() {
  local body norm n tl undressed
  norm=$(_norm "${1-}")
  [ -z "$norm" ] && { echo "EMPTY"; return; }
  undressed=$(_undress "${1-}")

  # --- 1. TITLE LINE, undressed, with a SIX-line window (D1 + D2). Six lines
  # covers title / underline / blank / version and the two-line FSF address
  # block that sometimes sits between them. Still a window, not a body search:
  # GPL section 13 is ~600 lines down and can never reach it.
  # D10: "GNU General Public License for more details." is a WRAPPED PROSE line
  # that begins at column 0, and p205's `head -1` took it as the title -- window
  # lines 12..17 carry no version, so the family lost its number. A title line
  # names the licence and stops; a prose line keeps going. Walk the candidates
  # and take the first that carries no sentence-continuation marker.
  local cand
  n=""
  for cand in $(printf '%s\n' "$undressed" | grep -niE "$TITLE_RE" | cut -d: -f1); do
    case " $(_norm "$(printf '%s\n' "$undressed" | sed -n "${cand}p")") " in
      *" for "*|*" as "*|*" is "*|*" of the "*|*" under "*|*" see "*|\
      *" more "*|*" details"*|*" along with"*|*" published by"*|\
      *" either "*|*" program "*|*" copy of "*|*" terms "*) continue ;;
    esac
    n="$cand"; break
  done
  if [ -n "$n" ]; then
    tl=$(_norm "$(printf '%s\n' "$undressed" | sed -n "${n},$((n+5))p")")
    case "$tl" in
      *"educational community license"*)      echo "ECL-2.0";       return ;;
      *"elastic license"*)                    echo "NON-OSI-Elastic-2.0"; return ;;
      *"business source license"*)            echo "NON-OSI-BSL";   return ;;
      *"server side public license"*)         echo "NON-OSI-SSPL";  return ;;
      # D3: Portuguese/Spanish AGPL. "affero" is the discriminating token in
      # every translation the FSF publishes, so test it before the plain GPL.
      *"licenca publica geral affero"*|*"licencia publica general affero"*|\
      *"gnu affero general public license"*)  echo "AGPL-3.0";      return ;;
      *"licenca publica geral"*|*"licencia publica general"*)
        case "$tl" in
          *"versao 3"*|*"version 3"*|*"versions 3"*) echo "GPL-3.0" ;;
          *) echo "GPL-unversioned" ;;
        esac; return ;;
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

  # --- 2. CC DEED (p205, unchanged).
  case "$norm" in
    *"human-readable summary of"*|*"not a substitute for"*)
      case "$norm" in
        *"/by-sa/"*) echo "CC-BY-SA-4.0-DEED"; return ;;
        *"/by-nc/"*) echo "CC-BY-NC-DEED";     return ;;
        *"/by/"*)    echo "CC-BY-4.0-DEED";    return ;;
        *"/zero/"*)  echo "CC0-1.0-DEED";      return ;;
      esac ;;
  esac

  # --- 3. TWO-SCOPE (p205, unchanged).
  if [ "$(scope_headings "${1-}")" -ge 2 ]; then echo "TWO-SCOPE"; return; fi

  # --- 4. STATEMENT / NARRATIVE (D5 + D6). A body with no title line that NAMES
  # a family in its OPENING is a grant reference, not the instrument. The window
  # is 15 lines, not a byte count: it is the same principled bound as the title
  # window and for the same reason -- GPL section 13 is ~600 lines down and can
  # never reach it, so a quoting licence cannot poison this branch either.
  # The -STATEMENT suffix is load-bearing, exactly as p205's -DEED is: it names
  # the family without letting anyone quote the text as the licence.
  local head15
  head15=$(_norm "$(printf '%s\n' "$undressed" | sed -n '1,15p')")
  case "$head15" in
    *"affero general public license"*)  echo "AGPL-3.0-STATEMENT"; return ;;
    *"lesser general public license"*)  echo "LGPL-STATEMENT";     return ;;
    *"general public license"*|*"gpl v3"*|*"gpl 3"*|*"gplv3"*)
      case "$head15" in
        *"version 3"*|*"gpl v3"*|*"gplv3"*|*"gpl 3"*) echo "GPL-3.0-STATEMENT" ;;
        *"version 2"*|*"gpl v2"*|*"gplv2"*)           echo "GPL-2.0-STATEMENT" ;;
        *)                                            echo "GPL-STATEMENT" ;;
      esac; return ;;
    *"apache license"*)                 echo "Apache-2.0-STATEMENT"; return ;;
    *"creative commons license attribution 4.0"*|\
    *"creative commons attribution 4.0"*) echo "CC-BY-4.0-STATEMENT"; return ;;
  esac

  # --- 5. BODY FALLBACK (p205, unchanged).
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
