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
    body=$(curl -sfL --max-time 20 "$url" 2>/dev/null | head -c 4096)
    if [ -n "$body" ]; then
      found="${found:+$found,}$name"
      g=$(spdx_of "$body")
      case ",$spdx," in *",$g,"*) ;; *) spdx="${spdx:+$spdx,}$g" ;; esac
    fi
  done

  [ -z "$found" ] && { found="UNRESOLVED-on-${#GRANT_NAMES[@]}-names"; spdx="UNRESOLVED"; }
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "LIVE" "$branch" "$sha" "$found" "$spdx"
done
