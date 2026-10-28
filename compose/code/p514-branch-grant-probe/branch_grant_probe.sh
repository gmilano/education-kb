#!/bin/bash
# p514 — T42 / Gap 512-D closure instrument: a licence absence is enumerated over
# BRANCHES, not only over paths on one resolved default branch.
# Gap 509-B rule honoured: `curl -o` then `wc -c`. NEVER `$(curl ...)` (strips trailing \n).
# Gap 509-B control rule honoured: a known-good AND a known-bad probe gate every verdict.
set -u
OUT="$1"; shift
PATHS=(LICENSE LICENSE.md LICENSE.txt LICENSE.rst license license.md license.txt
       LICENCE LICENCE.md LICENCE.txt COPYING COPYING.txt COPYING.md NOTICE
       LICENSE-MIT LICENSE-APACHE docs/LICENSE doc/LICENSE .github/LICENSE)
TMP=$(mktemp -d)
probe () { # slug ref path -> prints "code bytes sha16"
  local slug="$1" ref="$2" p="$3" f="$TMP/pay"
  rm -f "$f"
  local code
  code=$(curl -sS -L -o "$f" -w '%{http_code}' --max-time 20 \
         "https://raw.githubusercontent.com/$slug/$ref/$p" 2>/dev/null)
  if [ "$code" = "200" ]; then
    printf '%s %s %s\n' "$code" "$(wc -c < "$f" | tr -d ' ')" "$(sha256sum "$f" | cut -c1-16)"
  else
    printf '%s - -\n' "$code"
  fi
}
printf 'slug\tref\tpath\tcode\tbytes\tsha16\n' > "$OUT"
# ---- CONTROL PAIR (Gap 509-B): must be GOOD=200 and BAD=404 or every verdict below is void
CG=$(probe "HKUDS/DeepTutor" "HEAD" "LICENSE"); CB=$(probe "HKUDS/DeepTutor" "HEAD" "p514_control_absent_xyz")
echo "CONTROL-GOOD HKUDS/DeepTutor HEAD/LICENSE -> $CG"
echo "CONTROL-BAD  HKUDS/DeepTutor HEAD/p514_control_absent_xyz -> $CB"
case "$CG" in 200*) ;; *) echo "CONTROL-GOOD FAILED — verdicts VOID"; exit 2;; esac
case "$CB" in 404*) ;; *) echo "CONTROL-BAD  FAILED — verdicts VOID"; exit 2;; esac
printf 'CONTROL\tHEAD\tLICENSE\t%s\n' "$(echo $CG | tr ' ' '\t')" >> "$OUT"
for slug in "$@"; do
  mapfile -t refs < <(timeout 40 git ls-remote --heads "https://github.com/$slug" 2>/dev/null \
                      | sed 's#.*refs/heads/##' | sort -u)
  if [ "${#refs[@]}" -eq 0 ]; then
    echo "== $slug : LS-REMOTE-EMPTY (channel, not a fact)"
    printf '%s\tLS-REMOTE-EMPTY\t-\t-\t-\t-\n' "$slug" >> "$OUT"; continue
  fi
  echo "== $slug : ${#refs[@]} head(s): ${refs[*]}"
  for ref in "${refs[@]}"; do
    for p in "${PATHS[@]}"; do
      r=$(probe "$slug" "$ref" "$p")
      set -- $r
      if [ "$1" = "200" ]; then
        echo "   HIT $slug @$ref :$p -> bytes=$2 sha16=$3"
        printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$ref" "$p" "$1" "$2" "$3" >> "$OUT"
      fi
    done
  done
done
rm -rf "$TMP"
echo "DONE -> $OUT"
