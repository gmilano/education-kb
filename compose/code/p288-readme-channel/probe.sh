#!/usr/bin/env bash
# `ACTION p288`'s ONLINE half.  P237: this file has NO classifier.  It resolves the ref,
# walks `README_PATHS` until one answers 200, and records what it found.  `readme_claim.py`
# decides what the text MEANS.
#
# usage: probe.sh <slugs-file> <out-dir>
#
# 🔴 The ladder is walked in the order `readme_claim.README_PATHS` prints it, and the
# lower-case rung is not last-resort decoration: `anastasasenov/bbmcps` answers 404 on the
# upper-case spelling across `main`, `master` and `HEAD`, and 200 on the lower-case one.
# Probed at the upper-case spelling alone, this pass published "no readme on any ref" — a
# FALSE ABSENCE that only the tree enumeration caught.  T272: the spellings live in
# `README_PATHS` and are read from it here, never re-spelled in this file, so there is one
# ladder to extend rather than two to drift apart.
set -u
export GIT_TERMINAL_PROMPT=0 GIT_ASKPASS=/bin/true
HERE="$(cd "$(dirname "$0")" && pwd)"
SLUGS="${1:?usage: probe.sh <slugs-file> <out-dir>}"
OUT="${2:?usage: probe.sh <slugs-file> <out-dir>}"
mkdir -p "$OUT"

PATHS=$(python3 -I -c "import sys;sys.path.insert(0,'$HERE');import readme_claim;print(' '.join(readme_claim.README_PATHS))")

printf 'slug\tref\thead_sha\treadme_path\thttp\tbytes\tclaim_kind\tclaim_family\n'
while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  case "$slug" in \#*) continue ;; esac

  symref=$(git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  ref=$(printf '%s' "$symref" | awk '/^ref:/{sub("refs/heads/","",$2);print $2;exit}')
  # 🔴 The `ref: refs/heads/main\tHEAD` line ALSO ends in `HEAD`, so an anchor on the
  # suffix alone reports the literal string `ref:` as the SHA.  Anchor on the OID instead.
  sha=$(printf '%s' "$symref" | awk '$1 ~ /^[0-9a-f]{40}$/ && $2=="HEAD"{print substr($1,1,12);exit}')
  [ -z "$ref" ] && { printf '%s\tNO-REF\t-\t-\t-\t-\tNO-README\t-\n' "$slug"; continue; }

  found=""
  for p in $PATHS; do
    code=$(curl -sL --max-time 30 -o "$OUT/body.tmp" \
             -w '%{http_code}' "https://raw.githubusercontent.com/$slug/$ref/$p" 2>/dev/null)
    if [ "$code" = "200" ]; then found="$p"; break; fi
  done

  if [ -z "$found" ]; then
    printf '%s\t%s\t%s\t-\t404\t-\tNO-README\t-\n' "$slug" "$ref" "$sha"
    continue
  fi

  safe=$(printf '%s' "$slug" | tr '/' '_')
  mv "$OUT/body.tmp" "$OUT/$safe.readme"
  bytes=$(wc -c < "$OUT/$safe.readme" | tr -d ' ')
  read -r kind family <<EOF
$(python3 -I -c "
import sys
sys.path.insert(0,'$HERE')
from readme_claim import readme_claim
k,f=readme_claim(open('$OUT/$safe.readme',encoding='utf-8',errors='replace').read())
print(k, f or '-')
")
EOF
  printf '%s\t%s\t%s\t%s\t200\t%s\t%s\t%s\n' "$slug" "$ref" "$sha" "$found" "$bytes" "$kind" "$family"
done < "$SLUGS"
rm -f "$OUT/body.tmp"
