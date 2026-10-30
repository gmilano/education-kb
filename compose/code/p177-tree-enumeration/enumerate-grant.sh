#!/usr/bin/env bash
# p549 Gap 548-C instrument: TREE-scoped grant reader.
# Every prior verdict on this base was reached by probing ROOT filenames over HTTP.
# This reads the whole tree at HEAD and reports: declared?, served?, AND the served path.
set -u
WORK="${1:?workdir}"; SLUGS="${2:?slugfile}"; OUT="${3:?out.tsv}"
mkdir -p "$WORK"
GRANT_RE='(^|/)(licen[cs]e|copying|copyright|notice|unlicen[cs]e|eupl)([._-][A-Za-z0-9]+)?(\.(md|txt|rst|rtf|html))?$'
printf 'slug\tresolves\ttree_files\tgrant_paths_n\tserved_path\tbytes\tsha256_12\tfamily\tdeclared_in_manifest\tlast_commit\tlast_author_kind\n' > "$OUT"
while read -r slug; do
  [ -z "$slug" ] && continue
  safe=$(echo "$slug" | tr '/' '__')
  d="$WORK/$safe"
  rm -rf "$d"
  if ! timeout 180 git clone --filter=blob:none --no-checkout --quiet \
        "https://github.com/$slug" "$d" >/dev/null 2>&1; then
    printf '%s\tNO\t-\t-\t-\t-\t-\t-\t-\t-\t-\n' "$slug" >> "$OUT"; continue
  fi
  tree=$(git -C "$d" ls-tree -r HEAD --name-only 2>/dev/null)
  n_files=$(printf '%s\n' "$tree" | grep -c . )
  hits=$(printf '%s\n' "$tree" | grep -iE "$GRANT_RE" || true)
  n_hits=$(printf '%s\n' "$hits" | grep -c . )
  # manifest declaration channel (second, independent of the payload channel)
  decl='-'
  for m in package.json pyproject.toml composer.json Cargo.toml plugin.json setup.py; do
    p=$(printf '%s\n' "$tree" | grep -ixF "$m" | head -1)
    [ -z "$p" ] && continue
    v=$(git -C "$d" show "HEAD:$p" 2>/dev/null | grep -iEm1 '"?licen[cs]e"?[^A-Za-z0-9]{1,6}[A-Za-z0-9]' | tr -d '\r\t' | cut -c1-60)
    [ -n "$v" ] && { decl="$p :: $v"; break; }
  done
  last=$(git -C "$d" log -1 --date=short --format='%ad' 2>/dev/null)
  akind=$(git -C "$d" log -15 --format='%an' 2>/dev/null | grep -ciE '\[bot\]|github-actions|dependabot' )
  tot=$(git -C "$d" log -15 --format='%an' 2>/dev/null | grep -c .)
  kind="human:$((tot-akind))/bot:$akind"
  if [ "$n_hits" -eq 0 ]; then
    printf '%s\tYES\t%s\t0\t-\t-\t-\tNO-GRANT-IN-TREE\t%s\t%s\t%s\n' "$slug" "$n_files" "$decl" "$last" "$kind" >> "$OUT"
  else
    best=$(printf '%s\n' "$hits" | awk '{print length($0)"\t"$0}' | sort -n | head -1 | cut -f2-)
    sz=$(git -C "$d" cat-file -s "HEAD:$best" 2>/dev/null)
    sh=$(git -C "$d" show "HEAD:$best" 2>/dev/null | sha256sum | cut -c1-12)
    body=$(git -C "$d" show "HEAD:$best" 2>/dev/null | head -40)
    fam='UNIDENTIFIED'
    case "$body" in
      *"MIT License"*|*"MIT Licence"*) fam='MIT';;
      *"Apache License"*)              fam='Apache-2.0';;
      *"GNU AFFERO"*|*"GNU Affero"*)   fam='AGPL';;
      *"GNU LESSER"*|*"Lesser General"*) fam='LGPL';;
      *"GNU GENERAL PUBLIC"*|*"GNU General Public"*) fam='GPL';;
      *"BSD"*)                         fam='BSD';;
      *"Mozilla Public"*)              fam='MPL';;
      *"CC0"*|*"Creative Commons"*)    fam='CC';;
      *"Unlicense"*|*"UNLICENSE"*)     fam='Unlicense';;
      *"European Union Public"*)        fam='EUPL';;
    esac
    printf '%s\tYES\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$slug" "$n_files" "$n_hits" "$best" "$sz" "$sh" "$fam" "$decl" "$last" "$kind" >> "$OUT"
  fi
  rm -rf "$d"
done < "$SLUGS"
