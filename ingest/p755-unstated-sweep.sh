#!/bin/bash
R=0; G=0; N=0
while read -r a; do
  hit=""
  for br in main master; do
    for n in LICENSE LICENSE.md LICENSE.txt LICENCE COPYING; do
      code=$(curl -sS --max-time 12 -o /tmp/s.bin -w "%{http_code}" "https://raw.githubusercontent.com/$a/$br/$n" 2>/dev/null)
      if [ "$code" = "200" ]; then
        sz=$(stat -c %s /tmp/s.bin); sha=$(sha256sum /tmp/s.bin|cut -c1-12)
        t=$(head -3 /tmp/s.bin | tr -s ' \t\n' ' ' | cut -c1-55)
        hit="$br/$n|${sz}B|$sha|$t"; break 2
      fi
    done
  done
  R=$((R+1))
  if [ -n "$hit" ]; then G=$((G+1)); printf "GRANT  %-46s %s\n" "$a" "$hit"; else N=$((N+1)); printf "NONE   %-46s (main+master x5 names)\n" "$a"; fi
done < sample40.txt
echo "---- read=$R grant-found=$G none=$N ----"
