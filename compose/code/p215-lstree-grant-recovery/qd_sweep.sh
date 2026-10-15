#!/usr/bin/env bash
# ACTION QD (p215): re-read the 94 ABSENT rows through the `git ls-tree` channel.
# Treeless shallow clone => complete file inventory with NO blob transfer.
# Writes one line per repo: slug <TAB> status <TAB> npaths <TAB> own_paths <TAB> ambig_paths <TAB> vendored_paths
set -u
SCRATCH="$(cd "$(dirname "$0")" && pwd)"
SLUGS="$SCRATCH/absent_slugs.txt"
WORK="$SCRATCH/qd-clones"
OUT="$SCRATCH/qd_raw.tsv"
TREES="$SCRATCH/qd-trees"
mkdir -p "$WORK" "$TREES"
: > "$OUT"

# licence-bearing filenames (basename test, case-insensitive)
LIC_RE='^(licen[cs]e|copying|copyright|notice|unlicense|mit-licen[cs]e|apache-licen[cs]e|gpl|lgpl|agpl|bsd|licen[cs]e[-_.a-z0-9]*)(\.(txt|md|rst|html|text))?$'
# manifest files that can carry a grant
MAN_RE='^(package\.json|composer\.json|setup\.py|setup\.cfg|pyproject\.toml|description|cargo\.toml|.*\.gemspec|pom\.xml|build\.gradle|.*\.cabal|.*\.nuspec|pubspec\.yaml|.*\.podspec)$'
# vendored / third-party path segments  (QD's filter, plus the obvious extras)
VEND_RE='(^|/)(vendor|vendors|node_modules|third_party|third-party|thirdparty|bower_components|site-packages|\.venv|venv|external|externals|deps|dist|build|jquery[^/]*|fckeditor|ckeditor|tinymce|bootstrap|font-?awesome|wp-content/plugins|wp-includes)(/|$)'
# ambiguous: generic code dirs that MAY hold the project's own grant (p214 recovered
# formalms from html/lib/System/license/) -- QD's filter rejects these outright, so
# measure them separately instead of discarding them.
AMB_RE='(^|/)(lib|libs|public/javascripts|static|assets|resources|html/lib)(/|$)'

clone_one() {
  slug="$1"
  safe="${slug//\//__}"
  dir="$WORK/$safe"
  rm -rf "$dir"
  if ! timeout 120 git clone --filter=blob:none --no-checkout --depth 1 \
        --quiet "https://github.com/$slug" "$dir" 2>/dev/null; then
    printf '%s\tCLONE_FAIL\t0\t\t\t\n' "$slug" >> "$OUT"
    rm -rf "$dir"; return
  fi
  tree="$TREES/$safe.txt"
  if ! git -C "$dir" ls-tree -r HEAD --name-only > "$tree" 2>/dev/null; then
    printf '%s\tLSTREE_FAIL\t0\t\t\t\n' "$slug" >> "$OUT"
    rm -rf "$dir"; return
  fi
  n=$(wc -l < "$tree" | tr -d ' ')
  own=""; amb=""; ven=""
  while IFS= read -r p; do
    base="$(basename "$p")"
    lb="$(printf '%s' "$base" | tr 'A-Z' 'a-z')"
    lp="$(printf '%s' "$p" | tr 'A-Z' 'a-z')"
    if printf '%s' "$lb" | grep -qE "$LIC_RE" || printf '%s' "$lb" | grep -qE "$MAN_RE"; then
      if printf '%s' "$lp" | grep -qE "$VEND_RE"; then ven="$ven$p;"
      elif printf '%s' "$lp" | grep -qE "$AMB_RE"; then amb="$amb$p;"
      else own="$own$p;"; fi
    fi
  done < "$tree"
  printf '%s\tOK\t%s\t%s\t%s\t%s\n' "$slug" "$n" "$own" "$amb" "$ven" >> "$OUT"
  rm -rf "$dir"
}

export -f clone_one
export WORK OUT TREES LIC_RE MAN_RE VEND_RE AMB_RE

# modest parallelism: 4 concurrent smart-HTTP ops
pids=()
while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  clone_one "$slug" &
  pids+=($!)
  while [ "$(jobs -rp | wc -l)" -ge 4 ]; do sleep 0.3; done
done < "$SLUGS"
wait
echo "DONE rows=$(wc -l < "$OUT")"
