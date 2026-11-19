#!/usr/bin/env bash
# p917 — THE FILE-HEADER / MANIFEST LAYER.  Discharges `916-G2`.
#
# `916-G2` observed that `ingest/p913-grant-authority.sh` reports NO-LICENCE-FILE-FOUND for
# plainly granted ecosystem plugins, and prescribed: probe the FILE-HEADER layer (first ~40 lines
# of the primary source file) for a full GNU/Apache header block, starting with Moodle, WordPress
# and Drupal plugins where a licence is MANDATED by the ecosystem.
#
# 🔵 This script reads TWO layers below the licence file and keeps them DISTINCT, because they are
# different kinds of evidence and a later pass must not collapse them:
#   • HEADER   — a grant reproduced in a source file's comment block.  Binding, authored, per-file.
#   • MANIFEST — a `license:` field in composer.json / package.json / *.gemspec / DESCRIPTION.
#                This is `905-G1`'s axis.  It NAMES a grant without reproducing it, so it is
#                strictly weaker than a header and is reported as `MANIFEST-` to say so.
# A row with neither is reported UNGRANTED-AT-THREE-LAYERS, which is a much stronger statement
# than p913's NO-LICENCE-FILE-FOUND and is the only form in which this base should publish
# "no licence".
set -uo pipefail
OUT="${1:?usage: p917-header-layer.sh OUT.tsv slug...}"; shift
D=$(mktemp -d); trap 'rm -rf "$D"' EXIT
CAND=(version.php lib.php locallib.php index.php settings.php main.php app.php
      package.json composer.json DESCRIPTION setup.py pyproject.toml
      main.py model.py train.py run.py __init__.py
      src/index.ts src/index.js index.js lib/main.rb Rakefile)
printf 'repo\tbranch\tfile\tlayer\tfamily\tevidence\n' > "$OUT"
for slug in "$@"; do
  db=$(gh api -X GET search/repositories -f q="repo:$slug" --jq '.items[0].default_branch // ""' 2>/dev/null); sleep 2
  brs=(); [ -n "$db" ] && brs+=("$db"); for b in main master; do [ "$b" != "$db" ] && brs+=("$b"); done
  hit=0
  for br in "${brs[@]}"; do
    for f in "${CAND[@]}"; do
      code=$(curl -sS --max-time 20 -o "$D/f" -w '%{http_code}' \
             "https://raw.githubusercontent.com/$slug/$br/$f" 2>/dev/null)
      [ "$code" = "200" ] || continue
      head -c 6000 "$D/f" > "$D/h"
      fam=""; layer=""; ev=""
      # ---- HEADER layer: a grant reproduced in a comment block. ----
      if grep -qiE 'GNU Affero General Public' "$D/h"; then fam="AGPL-3.0"; layer="HEADER"
      elif grep -qiE 'GNU Lesser General Public' "$D/h"; then fam="LGPL"; layer="HEADER"
      elif grep -qiE 'GNU General Public License' "$D/h"; then
        fam="GPL"; layer="HEADER"
        grep -qiE 'either version 3|version 3 of the License|or \(at your option\) any later' "$D/h" \
          && fam="GPL-3.0-or-later"
      elif grep -qiE 'Licensed under the Apache License' "$D/h"; then fam="Apache-2.0"; layer="HEADER"
      elif grep -qE 'Permission is hereby granted, free of charge' "$D/h"; then fam="MIT"; layer="HEADER"
      elif grep -qiE 'Mozilla Public License' "$D/h"; then fam="MPL"; layer="HEADER"
      fi
      if [ -n "$fam" ]; then
        ev=$(grep -im1 -oE '.{0,70}(General Public License|Apache License|Permission is hereby granted|Mozilla Public License).{0,40}' "$D/h" | tr -d '\t\r' | cut -c1-110)
      else
        # ---- MANIFEST layer: a NAMED grant, not a reproduced one (905-G1).  Weaker. ----
        case "$f" in
          *.json)
            fam=$(python3 -I -c '
import sys,json
try: d=json.load(open(sys.argv[1]))
except Exception: sys.exit()
l=d.get("license")
if isinstance(l,dict): l=l.get("type")
if l: print(l)' "$D/f" 2>/dev/null) ;;
          DESCRIPTION) fam=$(grep -im1 '^License:' "$D/f" | sed 's/^[Ll]icense: *//' | tr -d '\r') ;;
          pyproject.toml|setup.py) fam=$(grep -im1 -oE 'license[^,)]{0,60}' "$D/f" | cut -c1-60 | tr -d '\r') ;;
        esac
        [ -n "$fam" ] && { layer="MANIFEST"; fam="MANIFEST-${fam}"; ev="named in $f, grant text NOT reproduced (905-G1) — weaker than a header"; }
      fi
      [ -n "$fam" ] || continue
      printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$br" "$f" "$layer" "$fam" "$ev" >> "$OUT"
      hit=1; break 2
    done
  done
  [ $hit -eq 0 ] && printf '%s\t-\t-\tNONE\tUNGRANTED-AT-THREE-LAYERS\tno licence file (p913), no grant header and no manifest field over %d candidate paths\n' \
      "$slug" "${#CAND[@]}" >> "$OUT"
done
