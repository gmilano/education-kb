#!/usr/bin/env bash
# `p370-git-tree-payload` — the ONLINE half: read a grant by ENUMERATING the tree.
#
# WHY A FOURTH TRANSPORT. Measured at p370 on 2026-10-21, from this session:
#   github.com (HTML)          403 at the proxy
#   api.github.com/repos/...   403 at the proxy  (api.github.com/rate_limit answers 200)
#   raw.githubusercontent.com  200 — but only for a path you can already NAME
#   git over https             200, clone and ls-remote both
# p368 lost the payload channel to a 403 and substituted metadata. p369 had raw and
# used it. p370 has raw too, and still does not probe it FIRST, because raw cannot
# list a directory: every raw licence probe is a GUESS AT A FILENAME, and p369's one
# honest non-result (`openedx/XBlock`, "404 on every path probed") is what a guess
# looks like when it loses. The file is `LICENSE.TXT`. The git tree SAYS so.
#
# Transport: a blobless partial clone at depth 1 — no checkout, no blobs until asked.
# That is one tree object and one commit per slug, then exactly the licence blobs.
#
# Usage: ./probe_tree.sh <slug-file> <outdir>
set -uo pipefail
slugs="${1:?file of owner/repo lines}"; out="${2:?outdir}"
mkdir -p "$out"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

printf 'slug\tstatus\thead\trefs\tlicence_paths\treadme\n'
while read -r slug; do
  [ -z "$slug" ] && continue
  case "$slug" in \#*) continue;; esac
  key="$(printf '%s' "$slug" | tr '/' '%')"
  d="$work/$key"

  refs="$(timeout 60 git ls-remote "https://github.com/$slug" 2>/dev/null | wc -l)"
  if [ "$refs" -eq 0 ]; then
    printf '%s\tNO-REMOTE\t-\t0\t-\t-\n' "$slug"
    printf 'NO-REMOTE\n' > "$out/$key.tree"
    continue
  fi

  if ! timeout 180 git clone --quiet --depth 1 --filter=blob:none --no-checkout \
        --single-branch "https://github.com/$slug" "$d" >/dev/null 2>&1; then
    printf '%s\tCLONE-FAILED\t-\t%s\t-\t-\n' "$slug" "$refs"
    printf 'CLONE-FAILED\n' > "$out/$key.tree"
    continue
  fi

  head="$(git -C "$d" rev-parse HEAD 2>/dev/null)"
  # 🟢 THE ENUMERATION. Every root entry name, verbatim. No guessing.
  git -C "$d" ls-tree --name-only HEAD > "$out/$key.tree" 2>/dev/null

  # licence-looking ROOT entries, selected from the enumeration, case-insensitive
  paths="$(grep -iE '^(licen[cs]e|copying|notice|unlicen[cs]e)' "$out/$key.tree" \
    | tr '\n' ',' | sed 's/,$//')"
  [ -z "$paths" ] && paths="-"

  # read the bytes of each candidate, pinned at this sha
  if [ "$paths" != "-" ]; then
    IFS=',' ; for p in $paths; do
      sz="$(git -C "$d" cat-file -s "HEAD:$p" 2>/dev/null || echo 0)"
      git -C "$d" cat-file -p "HEAD:$p" > "$out/$key--$(printf '%s' "$p" | tr '/' '%').payload" 2>/dev/null
      printf '%s\t%s\t%s\t%s\n' "$slug" "$p" "$sz" "$head" >> "$out/_payload-index.tsv"
    done ; unset IFS
  fi

  # the README, for the DOMAIN check (Gap 475) — same clone, no second transport
  rd="$(grep -iE '^readme' "$out/$key.tree" | head -1)"
  if [ -n "$rd" ]; then
    git -C "$d" cat-file -p "HEAD:$rd" 2>/dev/null | head -c 20000 > "$out/$key.readme"
  else
    rd="-"
  fi

  printf '%s\tOK\t%s\t%s\t%s\t%s\n' "$slug" "${head:0:12}" "$refs" "$paths" "$rd"
  rm -rf "$d"
done < "$slugs"
