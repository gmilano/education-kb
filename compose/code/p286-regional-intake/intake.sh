#!/usr/bin/env bash
# p286 — LICENCE INTAKE over the gap-directed legs (East Africa, Indonesia, Vietnam).
#
# 🟢 Channel, measured by p285 and re-used unchanged: `raw.githubusercontent.com` 200,
# `git ls-remote` OK, `git clone --depth 1 --filter=blob:none` OK, while
# `api.github.com/repos/{owner}/{repo}` is refused by SESSION REPO SCOPE (permanent).
# So: identity + default ref from ls-remote, grant from raw payload, and ABSENCE only
# from a blobless tree enumeration -- never from a path ladder (p275).
#
# 🔵 The ladder below is p229's TIER_A **as widened by this pass**, which is the point of
# running intake after the fix rather than before: `COPYING.TXT` and `copying` are in it.
set -uo pipefail
LADDER="LICENSE-CODE LICENSE LICENSE.md LICENSE.txt LICENSE.TXT LICENCE LICENCE.txt
licence.txt COPYING COPYING.txt COPYING.TXT COPYING.md COPYING.LESSER license.txt
license.md License.txt copying copying.txt LICENSE.rst NOTICE NOTICE.txt NOTICE.TXT
notice.txt License licenses MIT-LICENSE MIT-LICENSE.txt LICENSE-MIT LICENSE-APACHE
APACHE-LICENSE-2.0.txt"
OUT="${1:?usage: intake.sh <out.tsv> <slugs...>}"; shift
printf 'slug\thead_sha\tdefault_ref\tgrant_path\tbytes\tfamily\tverdict\n' > "$OUT"
fam_of() {  # crude family read of a payload; the shelf verdict is read by hand after
  local f="$1"
  grep -qiE 'MIT License' "$f" && { echo MIT; return; }
  grep -qiE 'Apache License.*Version 2' "$f" && { echo Apache-2.0; return; }
  grep -qiE 'GNU AFFERO GENERAL PUBLIC' "$f" && { echo AGPL-3.0; return; }
  grep -qiE 'GNU LESSER GENERAL PUBLIC' "$f" && { echo LGPL; return; }
  grep -qiE 'GNU GENERAL PUBLIC LICENSE' "$f" && { echo GPL; return; }
  grep -qiE 'BSD 3-Clause|Redistributions of source code' "$f" && { echo BSD; return; }
  grep -qiE 'Mozilla Public License' "$f" && { echo MPL-2.0; return; }
  grep -qiE 'CC BY|Creative Commons' "$f" && { echo CC; return; }
  echo UNKNOWN-BODY
}
for slug in "$@"; do
  sym=$(GIT_TERMINAL_PROMPT=0 timeout 45 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  if [ -z "$sym" ]; then
    printf '%s\t-\t-\t-\t0\t-\tDOES_NOT_RESOLVE\n' "$slug" >> "$OUT"; continue
  fi
  ref=$(printf '%s' "$sym" | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  # 🔴 the first draft matched /HEAD$/, which also matches the `ref:` line of --symref
  # output, so every row carried the literal `ref:` as its identity.  Match the SHA shape.
  sha=$(printf '%s' "$sym" | awk '$1 ~ /^[0-9a-f]{40}$/{print substr($1,1,12); exit}')
  [ -n "$ref" ] || ref=main
  found=""
  for p in $LADDER; do
    t=$(mktemp)
    code=$(curl -sS -o "$t" -w '%{http_code}' --max-time 25 \
           "https://raw.githubusercontent.com/$slug/$ref/$p" 2>/dev/null || echo 000)
    if [ "$code" = "200" ] && [ -s "$t" ]; then
      b=$(wc -c < "$t" | tr -d ' ')
      printf '%s\t%s\t%s\t%s\t%s\t%s\tGRANT_READ\n' "$slug" "$sha" "$ref" "$p" "$b" "$(fam_of "$t")" >> "$OUT"
      found=1; rm -f "$t"; break
    fi
    rm -f "$t"
  done
  [ -n "$found" ] && continue
  # 🔴 No ladder rung paid out.  p275: that is NOT an absence until the tree is enumerated.
  d=$(mktemp -d)
  if GIT_TERMINAL_PROMPT=0 timeout 240 git clone -q --depth 1 --filter=blob:none \
       "https://github.com/$slug" "$d/r" >/dev/null 2>&1; then
    hits=$(git -C "$d/r" ls-files | grep -iE '(^|/)(licen[sc]e|copying|notice|copyright)([.-][A-Za-z0-9]+)*$' | head -5)
    n=$(git -C "$d/r" ls-files | wc -l | tr -d ' ')
    if [ -n "$hits" ]; then
      printf '%s\t%s\t%s\t%s\t0\t-\tENUMERATED_CANDIDATE\n' "$slug" "$sha" "$ref" "$(echo $hits | tr '\n' ',')" >> "$OUT"
    else
      printf '%s\t%s\t%s\t-\t0\t-\tVERIFIED_ABSENT(%s files)\n' "$slug" "$sha" "$ref" "$n" >> "$OUT"
    fi
  else
    printf '%s\t%s\t%s\t-\t0\t-\tENUMERATION_FAILED\n' "$slug" "$sha" "$ref" >> "$OUT"
  fi
  rm -rf "$d"
done
cat "$OUT"
