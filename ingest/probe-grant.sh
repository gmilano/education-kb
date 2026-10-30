#!/usr/bin/env bash
# probe-grant.sh — the instrument Gap 516-A demanded (p517).
#
# WHY THIS EXISTS
#   p509 found that probing `main`/`master` mislabels repos whose default branch is
#   something else (portabilis/i-educar -> `2.12`, i-diario -> `1.6`). It wrote the
#   finding into PROSE. Six passes later p516 reproduced the identical defect, plus a
#   second one: grant files are not always named in English (bncc-dev/bncc-benchmark
#   keeps MIT in `LICENSE-CODIGO.md` and CC BY 4.0 in `LICENSE-DADOS.md`).
#   p516 wrote: "the fix belongs in the instrument, not in prose ... until the probe
#   changes, expect a fourth instance." This is the probe.
#
#   p530 FOUND THE FOURTH INSTANCE ANYWAY, in this file, in a new dimension:
#   raw.githubusercontent.com is case-sensitive on the WHOLE filename including the
#   extension, and this list carried `LICENSE.txt` but not `LICENSE.TXT`. So
#   openedx/XBlock (Apache-2.0, 471*) returned only `NOTICE.txt` and was one absent
#   file away from being filed UNRESOLVED while carrying a plain Apache licence at
#   `LICENSE.TXT`. This is the same bug class p529 recorded twice (`readme.md` vs
#   `README.md`) and did not generalise to "any channel, any case". The fix below is
#   therefore GENERATED case variants, not three more hand-written rows -- a
#   hand-written list is what failed twice.
#
#   p543 FOUND THE FIFTH AND SIXTH INSTANCES, both registered by p542:
#   542-A a SPLIT grant by material type (LICENSE-CODE + LICENSE-TEXT) read as a
#   half-grant, and 542-H a sub-100-byte CRAN stub contributing `unknown-text` to
#   the union beside the real grant. Both are fixed below, in the instrument.
#
# WHAT IT GUARANTEES
#   1. The default branch is RESOLVED (git ls-remote --symref), never assumed.
#   2. Grant filenames are probed in 14 languages before any "no licence" verdict.
#   3. It prints UNRESOLVED, never "unlicensed" — absence on this list is not absence.
#
# USAGE   ./probe-grant.sh owner/repo [owner/repo ...]
# OUTPUT  TSV: repo  live  default_branch  head_sha  grant_files  spdx_guess

set -uo pipefail

GRANT_NAMES=(
  # English (the only ones the base probed for 516 passes)
  LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENCE.txt
  COPYING COPYING.txt COPYING.md NOTICE NOTICE.txt
  # split code/data grants (bncc-dev pattern)
  LICENSE-CODIGO.md LICENSE-DADOS.md LICENSE-CODE LICENSE-CODE.md
  LICENSE-DATA LICENSE-DATA.md LICENSE-MIT LICENSE-APACHE
  # p543 / Gap 542-A: ocademy-ai/machine-learning keeps MIT at LICENSE-CODE and
  # CC-BY-4.0 at LICENSE-TEXT. LICENSE-CODE was already on this list; its partner
  # was not, so the pair read as a half-grant -- the content half was invisible.
  LICENSE-TEXT LICENSE-TEXT.md LICENSE-CONTENT LICENSE-CONTENT.md
  LICENSE-DOCS LICENSE-DOCS.md
  # Portuguese
  LICENCA LICENCA.md LICENCA.txt LICENÇA LICENÇA.md
  # Spanish
  LICENCIA LICENCIA.md LICENCIA.txt
  # German
  LIZENZ LIZENZ.md
  # Italian
  LICENZA LICENZA.md
  # Chinese
  LICENSE-CN LICENSE.zh LICENSE_zh-CN.md LICENSE-zh.md 许可证 许可证.md 协议 开源协议.md
  # Japanese
  LICENSE.ja LICENSE-ja.md ライセンス ライセンス.md
  # Korean
  LICENSE.ko LICENSE-ko.md 라이선스 라이선스.md
  # Indonesian / Malay
  LISENSI LISENSI.md
  # Russian
  ЛИЦЕНЗИЯ ЛИЦЕНЗИЯ.md
  # French
  LICENCE-FR.md
  # Arabic
  الترخيص
)

# p530: expand every ASCII name into its case variants, because the remote is
# case-sensitive and authors are not consistent.  For `LICENSE.txt` this yields
# `LICENSE.TXT`, `license.txt` and `License.txt` as well.  Non-ASCII names are
# passed through unchanged -- case folding is not meaningful for them here.
_expanded=()
for _n in "${GRANT_NAMES[@]}"; do
  _expanded+=("$_n")
  case "$_n" in
    *[!\ -~]*) continue ;;                     # skip non-ASCII (CJK, Cyrillic, Arabic)
  esac
  _up=${_n^^}                                  # LICENSE.TXT
  _lo=${_n,,}                                  # license.txt
  _ti=${_lo^}                                  # License.txt
  for _v in "$_up" "$_lo" "$_ti"; do
    case " ${_expanded[*]} " in *" $_v "*) ;; *) _expanded+=("$_v") ;; esac
  done
done
GRANT_NAMES=("${_expanded[@]}")

spdx_of() { # read first 4KB and name the grant
  local body="$1"
  case "$body" in
    *"GNU AFFERO GENERAL PUBLIC LICENSE"*|*"LICENÇA PÚBLICA GERAL AFFERO"*|*"AFFERO"*) echo "AGPL-3.0" ;;
    *"GNU LESSER GENERAL PUBLIC"*) echo "LGPL" ;;
    *"Version 2, June 1991"*) echo "GPL-2.0" ;;
    *"Version 3, 29 June 2007"*) echo "GPL-3.0" ;;
    *"GNU GENERAL PUBLIC LICENSE"*|*"LICENÇA PÚBLICA GERAL"*) echo "GPL-?" ;;
    *"Apache License"*) echo "Apache-2.0" ;;
    *"MIT License"*|*"Permission is hereby granted, free of charge"*) echo "MIT" ;;
    *"Creative Commons Attribution-ShareAlike"*) echo "CC-BY-SA-4.0" ;;
    *"Creative Commons Attribution"*) echo "CC-BY-4.0" ;;
    *"Redistribution and use in source and binary forms"*)
        case "$body" in *"Neither the name"*) echo "BSD-3-Clause";; *) echo "BSD-2-Clause";; esac ;;
    *"Mozilla Public License"*) echo "MPL-2.0" ;;
    *"THE SOFTWARE IS PROVIDED \"AS IS\""*) echo "MIT-like" ;;
    *) echo "unknown-text" ;;
  esac
}

printf 'repo\tlive\tdefault_branch\thead_sha\tgrant_files\tspdx_guess\n'

for slug in "$@"; do
  # ---- 1. liveness + DEFAULT BRANCH, resolved not assumed -------------------
  symref=$(git ls-remote --symref "https://github.com/${slug}" HEAD 2>/dev/null)
  if [ -z "$symref" ]; then
    printf '%s\tDEAD/PRIVATE\t-\t-\t-\t-\n' "$slug"
    continue
  fi
  branch=$(printf '%s\n' "$symref" | awk '/^ref:/{print $2}' | sed 's#refs/heads/##')
  sha=$(printf '%s\n' "$symref" | awk '!/^ref:/ && $2=="HEAD"{print substr($1,1,12)}')
  [ -z "$branch" ] && branch="(detached)"

  # ---- 2. grant probe across 14 languages AT THE RESOLVED BRANCH ------------
  found=""; spdx=""
  for name in "${GRANT_NAMES[@]}"; do
    enc=$(printf '%s' "$name" | od -An -tx1 | tr -d ' \n' \
          | sed 's/../%&/g' | sed 's/%2[fF]/\//g')
    url="https://raw.githubusercontent.com/${slug}/${branch}/${enc}"
    # p543: read to a FILE, not to a command substitution. Three reasons, each
    # found by running this probe against the two cases p542 read by hand:
    #   1. `$(...)` strips trailing newlines, so a 47 B grant measured 46.
    #   2. `${#body}` counts CHARACTERS, so a grant with one multi-byte glyph
    #      measured 1 121 where the file is 1 122 B.
    #   3. `head -c 4096` caps the read, so any larger grant reported 4096 and
    #      the cap was indistinguishable from the true size.
    # The byte figure is now `wc -c` on the whole payload and matches p542's
    # hand reads exactly (47 B, 1 076 B, 1 122 B).
    tmp=$(mktemp); : >"$tmp"
    if curl -sfL --max-time 20 -o "$tmp" "$url" 2>/dev/null; then
      nb=$(wc -c <"$tmp" | tr -d ' ')
      body=$(head -c 4096 "$tmp")
    else
      nb=0; body=""
    fi
    rm -f "$tmp"
    if [ "$nb" -gt 0 ]; then
      g=$(spdx_of "$body")
      # p543 / Gap 542-H -- the CRAN R-package shape. An R package declares
      # `License: MIT + file LICENSE` in DESCRIPTION and leaves LICENSE holding
      # only a year and a copyright holder (shmercer/writeAlizer: 47 B). That is
      # a STUB, not a grant, and letting it contribute `unknown-text` to the
      # union is how a real grant at LICENSE.md gets averaged away. Education
      # research publishes heavily in R, so this is a leg of this base, not an
      # edge case. A stub is RECORDED (it is evidence of the convention) and
      # EXCLUDED from the spdx union.
      if [ "$nb" -lt 100 ] && [ "$g" = "unknown-text" ]; then
        found="${found:+$found,}${name}[STUB:${nb}B]"
      else
        found="${found:+$found,}${name}[${nb}B]"
        case ",$spdx," in *",$g,"*) ;; *) spdx="${spdx:+$spdx,}$g" ;; esac
      fi
    fi
  done

  [ -z "$found" ] && { found="UNRESOLVED-on-${#GRANT_NAMES[@]}-names"; spdx="UNRESOLVED"; }
  # a repo whose ONLY hits were stubs has no readable grant on this channel
  [ -n "$found" ] && [ -z "$spdx" ] && spdx="STUB-ONLY-no-grant-text"
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "LIVE" "$branch" "$sha" "$found" "$spdx"
done
