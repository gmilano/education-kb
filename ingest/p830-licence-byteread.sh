#!/bin/bash
# p830 -- SEN / neurodivergent-learner tier: licence BYTE-READ over raw.githubusercontent.com.
# Channel A (`gh api repos/{owner}/{repo}`) is HTTP 403 for live AND invented addresses in this
# session (repo-scoped token), so it discriminates nothing and is NOT used as an oracle (T923/T970).
# Channel A' (`gh api search/repositories`, free-text) IS bidirectionally controlled and supplies
# star/push/licence-FIELD metadata; the licence BYTES come only from here.
# stdin: repo  (branch auto-probed)   stdout TSV: repo branch path code bytes sha12 titleline holder
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENCE.txt license LICENSE-MIT COPYING"
BRANCHES="main master"
while read -r repo; do
  [ -z "$repo" ] && continue
  found=0
  for br in $BRANCHES; do
    for p in $PATHS; do
      f="scratchpad/p830/$(echo "${repo}_${br}_${p}" | tr '/.' '__')"
      code=$(curl -sL --max-time 25 -o "$f" -w "%{http_code}" "https://raw.githubusercontent.com/$repo/$br/$p")
      if [ "$code" = "200" ] && [ -s "$f" ]; then
        b=$(wc -c < "$f" | tr -d ' '); s=$(sha256sum "$f" | cut -c1-12)
        tl=$(head -c 400 "$f" | tr -d '\r' | tr '\n\t' '  ' | sed 's/  */ /g;s/^ *//' | cut -c1-90)
        ho=$(grep -i -m1 'copyright' "$f" | sed 's/^ *//' | cut -c1-80)
        printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" "$repo" "$br" "$p" "$code" "$b" "$s" "$tl" "$ho"
        found=1; break
      else rm -f "$f"; fi
    done
    [ $found -eq 1 ] && break
  done
  [ $found -eq 0 ] && printf "%s\t-\t-\tNOGRANT\t-\t-\t-\t-\n" "$repo"
done
