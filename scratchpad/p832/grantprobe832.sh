#!/bin/bash
# p832 probe. Body written to FILE (never $(...)) so trailing newlines survive -> P834-safe.
# Case-aware filename list per D9. Default branch probed in addition to main/master.
probe() {
  slug="$1"
  for br in main master develop; do
    for fn in LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt \
              license license.md license.txt licence LICENSE-MIT MIT-LICENSE NOTICE; do
      if curl -sfL --max-time 20 "https://raw.githubusercontent.com/$slug/$br/$fn" -o body.bin 2>/dev/null \
         && [ -s body.bin ]; then
        b=$(wc -c < body.bin | tr -d ' '); s=$(sha256sum body.bin | cut -c1-12)
        if   grep -qi 'Apache License' body.bin; then L=Apache-2.0
        elif grep -qi 'GNU AFFERO' body.bin; then L=AGPL-3.0
        elif grep -qi 'GNU LESSER' body.bin; then L=LGPL
        elif grep -qi 'GNU GENERAL PUBLIC' body.bin; then L=GPL
        elif grep -qi 'Mozilla Public License' body.bin; then L=MPL-2.0
        elif grep -qi 'CC0 1.0\|Creative Commons' body.bin; then L=CC
        elif grep -qi 'Permission is hereby granted, free of charge' body.bin; then
             grep -qi 'BUT NOT LIMITED TO THE WARRANTIES' body.bin && L=MIT || L=MIT-MODIFIED
        elif grep -qi 'Redistribution and use in source and binary' body.bin; then L=BSD
        else L=UNRECOGNISED; fi
        printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$L" "$b" "$s" "$br/$fn"; return
      fi
    done
  done
  printf '%s\tNOGRANT\t-\t-\t-\n' "$slug"
}
for s in "$@"; do probe "$s"; done
