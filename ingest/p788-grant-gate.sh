#!/usr/bin/env bash
# p788 grant gate — implements compose/patterns.md P787-7, all 8 rules.
#   1 existence via git ls-remote, exit status read DIRECTLY (never piped)
#   2 licence bytes over 3 branches x 10 filenames on raw.githubusercontent.com
#   3 appendix-bearing licences (EUPL / CeCILL) matched FIRST            (T849)
#   4 copyleft family decided on the TITLE LINE only                    (T847, Affero-in-GPLv3)
#   5 MIT graded on its 4 clauses in EN / ES / PT / FR                  (T848)
#   6 byte length NEVER used as an integrity signal                     (T845)
#   7 controls run BEFORE any verdict is trusted
#   8 repo grant != dependency audit (see p788-dep-audit.sh)
set -u
export LC_ALL=C.UTF-8 2>/dev/null || export LC_ALL=C
BRANCHES="main master develop"
NAMES="LICENSE LICENSE.md LICENSE.txt license license.txt COPYING COPYING.txt LICENCE LICENCE.md LICENSE-MIT"

grade() { # stdin: licence bytes -> family on stdout
  local f; f=$(cat); local title
  title=$(printf '%s' "$f" | grep -m1 -v '^[[:space:]]*$' | tr -d '\r')

  # RULE 3 — appendix-bearing licences first: they NAME other licences inside themselves.
  if printf '%s' "$f" | grep -qiE 'European Union Public Licence|EUPL'; then echo "EUPL-1.2"; return; fi
  if printf '%s' "$f" | grep -qiE 'CeCILL'; then echo "CeCILL"; return; fi

  # RULE 4 (p788, REWRITTEN) — find the FIRST LINE THAT IS A LICENCE TITLE, anywhere
  # in the file. A fixed head -N window is the wrong instrument: Odoo defers to line 3,
  # INGInious to line 9 behind a prose scope caveat, and the next one will differ again.
  # Anchoring on a line that *is* a title still excludes GPL-3.0 s13's prose mention of
  # Affero, which is a clause inside a sentence and never a line of its own.
  local tl
  tl=$(printf '%s' "$f" | tr -d '\r' | sed 's/^[[:space:]]*//; s/[[:space:]]*$//' \
       | grep -m1 -iE '^(the )?(gnu )?(affero |lesser )?general public license( *,? *version [0-9.]+)?$|^apache license,? *(version [0-9.]+)?$|^educational community license,? *(version [0-9.]+)?$|^mozilla public license.*$|^bsd [0-9]-clause.*$|^mit license$|^isc license$|^licen[sc]e:? *(gnu )?(a?)gpl ?-? ?v?[0-9.]+$|^\(?the )?mit licen[sc]e\)?$')
  if [ -n "$tl" ]; then
    # abbreviations are how real files declare a grant: `License: GNU GPL V3` is 19 bytes
    # and is a grant. Matching only expanded names scored it UNGRADED.
    if printf '%s' "$tl" | grep -qiE 'affero|agpl'; then echo "AGPL-3.0"; return; fi
    if printf '%s' "$tl" | grep -qiE 'lesser|lgpl'; then echo "LGPL"; return; fi
    if printf '%s' "$tl" | grep -qiE 'general public license|gpl'; then
        if printf '%s' "$tl" | grep -qiE 'version 2|gpl ?-? ?v?2'; then echo "GPL-2.0"; else echo "GPL-3.0"; fi; return; fi
    if printf '%s' "$tl" | grep -qiE 'educational community'; then echo "ECL-2.0"; return; fi
    if printf '%s' "$tl" | grep -qiE 'apache'; then echo "Apache-2.0"; return; fi
    if printf '%s' "$tl" | grep -qiE 'mozilla'; then echo "MPL-2.0"; return; fi
  fi
  # Grant BY REFERENCE: the standard Apache/MPL short notice is a real grant, and it is
  # short. Length is never a verdict (T845) -- a 570 B Apache notice is still Apache.
  if printf '%s' "$f" | grep -qE 'Licensed under the Apache License, Version 2\.0' && \
     printf '%s' "$f" | grep -qiE 'www.apache.org/licenses/LICENSE-2.0'; then echo "Apache-2.0(by-reference)"; return; fi
  if printf '%s' "$title" | grep -qiE 'Mozilla Public License'; then echo "MPL-2.0"; return; fi
  # A grant that differs BY DIRECTORY is not one family, and reporting a family for it
  # would be the error. Name the boundary instead (cf. metabase, speckle-server).
  if printf '%s' "$f" | grep -qiE 'variously licensed|licensed under .{0,40}(or the|or a) .{0,40}commercial licen|within the .{0,30}director(y|ies)'; then
      echo "SPLIT-BY-DIRECTORY"; return; fi
  if printf '%s' "$f" | grep -qiE 'Creative Commons|CC[ -]BY'; then
      if printf '%s' "$f" | grep -qiE 'NonCommercial'; then echo "CC-NC"; else echo "CC"; fi; return; fi
  if printf '%s' "$f" | grep -qE 'Redistribution and use in source and binary forms'; then
      if printf '%s' "$f" | grep -qE 'Neither the name'; then echo "BSD-3-Clause"; else echo "BSD-2-Clause"; fi; return; fi

  # RULE 5 — MIT on its four clauses, in four languages. Length is never consulted.
  local c=0 lang=""
  if printf '%s' "$f" | grep -qE 'Permission is hereby granted'           && \
     printf '%s' "$f" | grep -qE 'substantial portions of the Software'   && \
     printf '%s' "$f" | grep -qiE 'WITHOUT WARRANTY OF ANY KIND'          && \
     printf '%s' "$f" | grep -qiE 'IN NO EVENT SHALL'; then c=4; lang="en"; fi
  # es/pt/fr: EVERY clause is matched as a set of circulating renderings. One rendering
  # per language is what made this probe score a valid Spanish MIT as UNGRADED.
  if [ $c -eq 0 ] && printf '%s' "$f" | grep -qiE 'se concede (permiso|por la presente)|Por la presente se concede|se otorga permiso' && \
     printf '%s' "$f" | grep -qiE '(porciones|partes|copias) sustanciales' && \
     printf '%s' "$f" | grep -qiE 'SIN GARANT' ; then c=4; lang="es"; fi
  if [ $c -eq 0 ] && printf '%s' "$f" | grep -qiE 'concedida.{0,30}permiss|concedida.{0,30}gratuitamente|permissao .{0,10}concedida|permiss' && \
     printf '%s' "$f" | grep -qiE '(porcoes|por..es|partes|copias|c.pias) substanciais' && \
     printf '%s' "$f" | grep -qiE 'SEM GARANTIA'; then c=4; lang="pt"; fi
  if [ $c -eq 0 ] && printf '%s' "$f" | grep -qiE "autorisation est .{0,25}accord|L'autorisation est par la pr" && \
     printf '%s' "$f" | grep -qiE '(parties|portions) substantielles' && \
     printf '%s' "$f" | grep -qiE 'SANS GARANTIE'; then c=4; lang="fr"; fi
  if [ $c -eq 4 ]; then
      if [ "$lang" = "en" ]; then echo "MIT"; else echo "MIT(translated:$lang)"; fi; return; fi

  if printf '%s' "$f" | grep -qiE 'ISC License'; then echo "ISC"; return; fi
  if printf '%s' "$f" | grep -qiE 'all rights reserved' && ! printf '%s' "$f" | grep -qiE 'Permission is hereby'; then
      echo "PROPRIETARY"; return; fi
  echo "UNGRADED"
}

scopeflag() { # stdin: licence bytes -> SCOPE-LIMITED if the grant excludes part of the repo
  local f; f=$(cat)
  if printf '%s' "$f" | grep -qiE 'ALCANCE DE ESTA LICEN|SCOPE OF THIS LICEN|ESCOPO DESTA LIC|licen[sc]e above applies to|NO cubre|nao cobre|ne couvre pas|does not (apply to|cover) the (content|exam|data|corpus|material)'; then
      echo "SCOPE-LIMITED"; else echo "-"; fi
}

probe() { # $1 = owner/repo
  local a="$1" sha="" rc
  # RULE 1 — exit status read DIRECTLY. No pipe anywhere on this line.
  sha=$(git ls-remote "https://github.com/$a" HEAD 2>/dev/null); rc=$?
  if [ $rc -ne 0 ] || [ -z "$sha" ]; then printf '%s\tDEAD\t-\t-\t-\n' "$a"; return; fi
  sha=$(printf '%s' "$sha" | awk 'NR==1{print substr($1,1,12)}')
  local br nm url body bytes fam
  for br in $BRANCHES; do for nm in $NAMES; do
    url="https://raw.githubusercontent.com/$a/$br/$nm"
    tmp=$(mktemp); curl -sfL --max-time 25 "$url" -o "$tmp" 2>/dev/null || { rm -f "$tmp"; continue; }
    [ ! -s "$tmp" ] && { rm -f "$tmp"; continue; }
    # RULE 9 (p788) — count bytes ON THE FILE. $(curl) eats the trailing newline
    # and under-reports every licence by exactly 1 B.
    bytes=$(wc -c < "$tmp" | tr -d ' ')
    fam=$(grade < "$tmp"); scope=$(scopeflag < "$tmp"); rm -f "$tmp"
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$a" "$fam" "$bytes" "$sha" "$br/$nm" "$scope"
    return
  done; done
  printf '%s\tNO-GRANT-SERVED\t-\t%s\t%d-names-x-3-branches\t-\n' "$a" "$sha" "$(echo $NAMES | wc -w)"
}

export -f probe grade scopeflag; export BRANCHES NAMES
if [ "${1:-}" = "--controls" ]; then
  echo "== RULE 7: controls, run before any verdict is trusted =="
  for a in HKUDS/DeepTutor moodle/moodle sakaiproject/sakai frappe/lms \
           hedyorg/hedy goyanedelv/paes-mcp \
           zzz-not-a-real-org-xyz/nope-nope Priyamakeshwari/TeachGPT; do probe "$a"; done
  exit 0
fi
[ $# -eq 0 ] && { echo "usage: $0 owner/repo ... | --controls | -f file"; exit 2; }
if [ "$1" = "-f" ]; then
  tr -d '\r' < "$2" | grep -vE '^\s*(#|$)' | xargs -P 10 -I{} bash -c 'probe "$@"' _ {}
else
  for a in "$@"; do probe "$a"; done
fi
