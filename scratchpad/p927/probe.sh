#!/bin/bash
# 12-path licence byte-probe, per KB method (p896 extension)
PATHS="main/LICENSE master/LICENSE main/LICENSE.md master/LICENSE.md main/LICENSE.txt master/LICENSE.txt main/COPYING master/COPYING main/COPYING.txt master/COPYING.txt main/LICENSE.TXT master/LICENSE.TXT main/license main/License"
echo -e "repo\tpath\thttp\tbytes\tsha256_12\tgrant_read"
while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  found=0
  for p in $PATHS; do
    url="https://raw.githubusercontent.com/$slug/$p"
    code=$(curl -s -o /tmp/lic.$$ -w '%{http_code}' "$url")
    if [ "$code" = "200" ]; then
      bytes=$(wc -c < /tmp/lic.$$)
      sha=$(sha256sum /tmp/lic.$$ | cut -c1-12)
      grant=$(head -c 3000 /tmp/lic.$$ | tr '\n' ' ' | grep -oiE '(MIT License|Apache License|BSD[ -]?[0-9]?[ -]?Clause|Mozilla Public License|GNU AFFERO|GNU GENERAL PUBLIC|ISC License|Zero-Clause BSD|BSD Zero Clause|Creative Commons|The Unlicense|Eclipse Public|EUPL)' | head -1)
      [ -z "$grant" ] && grant="UNRECOGNISED"
      echo -e "$slug\t$p\t200\t$bytes\t$sha\t$grant"
      found=1; break
    fi
  done
  [ $found -eq 0 ] && echo -e "$slug\t-\tNONE\t0\t-\tNO_LICENCE_FILE_ON_12_PATHS"
  rm -f /tmp/lic.$$
done < scratchpad/p927/shelf-candidates.txt
