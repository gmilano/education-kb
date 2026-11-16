#!/usr/bin/env bash
# P94 — three-gate candidate intake for education OSS.
# Usage: ./intake-gate.sh owner/repo [owner/repo ...]
# Exit 0 = every candidate PASSed. Exit 1 = at least one REJECTed.
# Gates run in order and short-circuit: liveness -> grant -> substance.
set -uo pipefail

SRC_EXT='py|ts|tsx|js|jsx|java|go|rb|rs|kt|swift|cs|cpp|c|h|php|scala|ex|dart|vue|svelte|ipynb'
rc=0

for repo in "$@"; do
  printf '%s\t' "$repo"

  # ---- GATE 1: liveness at a REAL ref. Never trust curl -sI here: this proxy
  # returns 403 for live repos (T124), so an HTTP status is not a liveness signal.
  symref=$(timeout 60 git ls-remote --symref "https://github.com/$repo" HEAD 2>/dev/null)
  if [ -z "$symref" ]; then
    printf 'REJECT\tgate1-liveness\tno ls-remote response\n'; rc=1; continue
  fi
  ref=$(printf '%s' "$symref" | awk '/^ref:/{print $2}')
  sha=$(printf '%s' "$symref" | awk '$2=="HEAD"{print $1}' | cut -c1-12)
  branch=${ref#refs/heads/}
  [ -n "$branch" ] || branch=main

  # ---- GATE 2: grant, BYTE-READ from the repo at that ref. Not a badge, not an
  # aggregator, not a topic tag, not the README's prose.
  lic=""; bytes=""; hash=""
  for f in LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt LICENCE; do
    tmp=$(mktemp)
    code=$(curl -sL -o "$tmp" -w '%{http_code}' \
      "https://raw.githubusercontent.com/$repo/$branch/$f")
    if [ "$code" = "200" ] && [ -s "$tmp" ]; then
      lic=$f; bytes=$(wc -c < "$tmp" | tr -d ' ')
      hash=$(sha256sum "$tmp" | cut -c1-12)
      spdx=$(grep -m1 -oiE 'MIT License|Apache License|BSD [0-9]-Clause|GNU (Affero |Lesser )?General Public|Educational Community License|Mozilla Public' "$tmp")
      rm -f "$tmp"; break
    fi
    rm -f "$tmp"
  done
  if [ -z "$lic" ]; then
    printf 'REJECT\tgate2-grant\t%s@%s: no licence file (all-rights-reserved)\n' "$branch" "$sha"
    rc=1; continue
  fi

  # ---- GATE 3: substance. A grant over docs and media is not a usable asset
  # (T143 mode 3). Require executable source in the tree.
  wt=$(mktemp -d)
  if ! timeout 300 git clone --depth 1 -q "https://github.com/$repo" "$wt/r" 2>/dev/null; then
    printf 'REJECT\tgate3-substance\tclone failed\n'; rm -rf "$wt"; rc=1; continue
  fi
  nsrc=$(find "$wt/r" -type f -not -path '*/.git/*' \
    | grep -ciE "\.($SRC_EXT)$")
  rm -rf "$wt"
  if [ "$nsrc" -eq 0 ]; then
    printf 'REJECT\tgate3-substance\t%s %sB %s: 0 source files (grant covers no code)\n' \
      "${spdx:-unknown}" "$bytes" "$hash"
    rc=1; continue
  fi

  printf 'PASS\t%s\t%s %sB sha12=%s ref=%s@%s src=%s\n' \
    "$lic" "${spdx:-unknown}" "$bytes" "$hash" "$branch" "$sha" "$nsrc"
done
exit $rc
