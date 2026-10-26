#!/bin/bash
# Two-stage verifier: ls-remote for liveness+ref, then licence payload read at that ref.
# Negative controls included deliberately.
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.txt COPYING COPYING.txt license LICENSE-MIT LICENSE.rst"
while read -r slug; do
  [ -z "$slug" ] && continue
  ref=$(timeout 25 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  if [ -z "$ref" ]; then echo -e "$slug\tADDRESS_DEAD\t-\t-\t-\t-"; continue; fi
  found=0
  for p in $PATHS; do
    out=$(timeout 25 curl -s -w '%{http_code} %{size_download}' -o /tmp/claude-0/-home-user-globant-kb/662047f6-193c-5829-a4c4-0cfed5121702/scratchpad/lic.bin \
       "https://raw.githubusercontent.com/$slug/$ref/$p" 2>/dev/null)
    code=$(echo "$out" | awk '{print $1}'); size=$(echo "$out" | awk '{print $2}')
    if [ "$code" = "200" ]; then
      dg=$(sha256sum /tmp/claude-0/-home-user-globant-kb/662047f6-193c-5829-a4c4-0cfed5121702/scratchpad/lic.bin | cut -c1-12)
      fam=$(head -c 2500 /tmp/claude-0/-home-user-globant-kb/662047f6-193c-5829-a4c4-0cfed5121702/scratchpad/lic.bin | tr -d '\r' | tr '\n' ' ' | grep -ioE 'MIT License|Apache License|GNU AFFERO GENERAL PUBLIC LICENSE|GNU GENERAL PUBLIC LICENSE|GNU LESSER GENERAL PUBLIC|BSD 3-Clause|BSD 2-Clause|Mozilla Public License|ISC License|Creative Commons' | head -1)
      [ -z "$fam" ] && fam="UNNAMED"
      echo -e "$slug\tPAYLOAD_READ\t$ref\t$p\t$size\t$dg\t$fam"
      found=1; break
    fi
  done
  [ $found -eq 0 ] && echo -e "$slug\tREPO_LIVE_NO_GRANT\t$ref\t-\t-\t-\t-"
done
