#!/usr/bin/env bash
# p612 grant gate. Same five steps p611 documented, reimplemented here:
#  1 real default branch (p559)  2 ladder of grant paths (p610-E)
#  3 grade on the TITLE LINE only (p611-B)  4 flag a named upstream (p610-A)
#  5 fabricated control in-run (p608-A)
set -uo pipefail
S="$(dirname "$0")"  # grade.py lives beside this script as p612-grade-title-line.py
LADDER=(LICENSE LICENSE.md LICENSE.txt license license.md license.txt LICENCE LICENCE.md licence COPYING COPYING.txt COPYING.md copying LICENSE-MIT LICENSE-APACHE MIT-LICENSE MIT-LICENSE.txt)
probe() {
  local r="$1" br path code size g tmp
  tmp=$(mktemp)
  br=$(timeout 45 git ls-remote --symref "https://github.com/$r" HEAD 2>/dev/null \
       | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  if [[ -z "$br" ]]; then printf '%s\tUNREACHABLE\t-\t0\tNO-SUCH-ADDRESS\n' "$r"; rm -f "$tmp"; return; fi
  for path in "${LADDER[@]}"; do
    read -r code size < <(curl -sL --max-time 40 -o "$tmp" -w '%{http_code} %{size_download}' \
      "https://raw.githubusercontent.com/$r/$br/$path")
    if [[ "$code" == "200" && "$size" -gt 100 ]]; then
      g=$(python3 -I "$S/p612-grade-title-line.py" < "$tmp")
      printf '%s\t%s\t%s\t%s\t%s\n' "$r" "$br" "$path" "$size" "$g"
      rm -f "$tmp"; return
    fi
  done
  rm -f "$tmp"
  printf '%s\t%s\tNO-GRANT\t0\tUNGRANTED-LADDER-EXHAUSTED\n' "$r" "$br"
}
printf 'address\tdefault_branch\tgrant_path\tbytes\tgrade\n'
for r in "$@"; do probe "$r"; done
for c in "openai/totally-not-real-edu-repo-p612" "anthropics/fabricated-control-p612-$(date +%s)"; do
  cr=$(probe "$c" | cut -f2)
  printf '%s\t%s\t-\t-\tFABRICATED-CONTROL\n' "$c" "$cr"
  [[ "$cr" == "UNREACHABLE" ]] || { echo "GATE UNTRUSTWORTHY: control resolved" >&2; exit 2; }
done
