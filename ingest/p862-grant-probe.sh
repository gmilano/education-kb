#!/bin/bash
# p862 -- grant + affiliation probe, carrying 861-G1's SECOND STAGE (organisation -> country).
#
# 861-G1 said: an affiliation is not a region.  foundation50/classroom50 STATES its publisher
# and that publisher names no country.  The remedy it named: a second lookup that maps an
# ORGANISATION to a country via (a) a TLD in a stated URL, (b) a postal address in CITATION.cff,
# (c) a jurisdiction named in CODE_OF_CONDUCT / CONTRIBUTING.
#
# Its acceptance test: report TWO numbers -- STATED affiliation, and PLACED.  p861 was 9 and 8.
#
# Licence is read from the repository's OWN bytes.  GitHub's SPDX field is never consulted.
set -u
W=/tmp/claude-0/p862/clones
BOILER='Free Software Foundation|Apache Software Foundation|Open Source Initiative|<COPYRIGHT HOLDER>|copyright holder|\[fullname\]|\[name of copyright owner\]'
INST='Universit|Universidad|Universidade|Hochschule|Instituto|Institute|Polytechnic|College|Ministry|Ministerio|Minist.rio|Funda..o|Fundaci.n|Foundation|Escola|Escuela|Centro Federal|Laborat'
# ccTLD -> region, for the SECOND STAGE
tld2region(){ case "$1" in
  br|mx|ar|cl|co|pe|uy|ve|ec|bo|py|cr|gt|do|pa|cu) echo LATAM;;
  es|pt|fr|de|it|uk|ie|nl|be|ch|at|se|no|dk|fi|pl|gr|tr|za|ke|ng|eg|ma|ae|il|ru|cz|ro|hu) echo EMEA;;
  in|cn|jp|kr|sg|au|nz|my|th|id|ph|vn|tw|hk|pk|bd|lk) echo APAC;;
  us|ca) echo "North America";;
  *) echo '';; esac; }
printf 'repo\tclone\thead_date\tlicence_path\tbytes\tsha256_12\tfirst_line\tholder\taffil_axis\taffil_evidence\tregion_axis\tregion\n'
while read -r repo; do
  [ -z "$repo" ] && continue
  d="$W/$(echo "$repo" | tr '/' '_')"
  if [ ! -d "$d" ]; then
    git clone --filter=blob:none --no-checkout --depth 1 -q "https://github.com/$repo" "$d" 2>/dev/null \
      || { printf '%s\tCLONE-FAIL\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n' "$repo"; continue; }
  fi
  hd=$(git -C "$d" log -1 --format=%cs 2>/dev/null); [ -z "$hd" ] && hd='-'
  tree=$(git -C "$d" ls-tree -r --name-only HEAD 2>/dev/null)
  lp=$(echo "$tree" | grep -iE '^(LICEN[CS]E|COPYING|LICEN[CS]E\.(md|txt))$' | head -1)
  [ -z "$lp" ] && lp=$(echo "$tree" | grep -iE '(^|/)(LICEN[CS]E|COPYING)([.-][A-Za-z0-9]+)?$' | head -1)
  if [ -n "$lp" ]; then
    git -C "$d" show "HEAD:$lp" > "$d/.licence" 2>/dev/null
    by=$(wc -c < "$d/.licence" | tr -d ' ')
    sh=$(sha256sum "$d/.licence" | cut -c1-12)
    fl=$(grep -m1 -vE '^\s*$' "$d/.licence" | sed 's/^ *//' | cut -c1-60)
    ho=$(grep -i -m1 'copyright' "$d/.licence" | sed 's/^ *//' | cut -c1-70)
  else
    lp='NONE'; by=0; sh='-'; fl='-'; ho=''
  fi
  rp=$(echo "$tree" | grep -iE '^README(\.(md|rst|txt))?$' | head -1)
  RM=''; [ -n "$rp" ] && RM=$(git -C "$d" show "HEAD:$rp" 2>/dev/null | head -c 12000)
  # ---- stage 1: is an affiliation STATED?
  ax='-'; ev='-'
  if [ -n "$ho" ] && ! echo "$ho" | grep -qiE "$BOILER"; then
    if echo "$ho" | grep -qE "$INST"; then ax=holder; ev=$(echo "$ho" | sed 's/.*[Cc]opyright[^A-Za-z0-9]*//' | cut -c1-55); fi
  fi
  cf=$(echo "$tree" | grep -ixE 'CITATION\.cff' | head -1)
  if [ "$ax" = '-' ] && [ -n "$cf" ]; then
    a=$(git -C "$d" show "HEAD:$cf" 2>/dev/null | grep -iE '^\s*(affiliation|institution):' | head -1 | sed 's/.*: *//; s/^["'"'"']//; s/["'"'"']$//' | cut -c1-55)
    [ -n "$a" ] && { ax=citation; ev="$a"; }
  fi
  if [ "$ax" = '-' ] && [ -n "$RM" ]; then
    a=$(echo "$RM" | grep -oiE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(edu|ac\.[a-z]{2}|edu\.[a-z]{2})|https?://[A-Za-z0-9.-]+\.(edu|ac\.[a-z]{2}|edu\.[a-z]{2})[^ )]*' | head -1 | cut -c1-55)
    [ -n "$a" ] && { ax=domain; ev="$a"; }
  fi
  if [ "$ax" = '-' ] && [ -n "$RM" ]; then
    a=$(echo "$RM" | grep -oE "[A-Z][A-Za-z.&'-]*( [A-Z][A-Za-z.&'-]*){0,4} ($INST)[a-z]*|($INST)[a-zç~õãé]* (of|de|do|da) [A-Z][A-Za-zç~õãé.'-]*( [A-Za-zç~õãé.'-]*){0,3}" | head -1 | cut -c1-55)
    [ -n "$a" ] && { ax=readme; ev="$a"; }
  fi
  # ---- stage 2 (861-G1's remedy): organisation -> COUNTRY, independent of stage 1
  rax='-'; reg='-'
  if [ -n "$RM" ]; then
    t=$(echo "$RM" | grep -oiE 'https?://[A-Za-z0-9.-]+\.(ac|edu|gov|org|com|net)\.([a-z]{2})[/" )]|https?://[A-Za-z0-9.-]+\.([a-z]{2})[/" )]' | head -1 | grep -oE '\.[a-z]{2}[/" )]$' | tr -d './" )')
    if [ -n "$t" ]; then r=$(tld2region "$t"); [ -n "$r" ] && { rax="url-tld:.$t"; reg="$r"; }; fi
  fi
  if [ "$reg" = '-' ] && [ -n "$ev" ] && [ "$ev" != '-' ]; then
    t=$(echo "$ev" | grep -oE '\.(ac|edu)\.[a-z]{2}|\.[a-z]{2}$' | grep -oE '[a-z]{2}$')
    if [ -n "$t" ]; then r=$(tld2region "$t"); [ -n "$r" ] && { rax="affil-tld:.$t"; reg="$r"; }; fi
  fi
  if [ "$reg" = '-' ] && [ -n "$cf" ]; then
    a=$(git -C "$d" show "HEAD:$cf" 2>/dev/null | grep -iE '^\s*(country|city|address):' | head -1 | sed 's/.*: *//' | cut -c1-30)
    [ -n "$a" ] && { rax="citation-address"; reg="?$a"; }
  fi
  if [ "$reg" = '-' ]; then
    coc=$(echo "$tree" | grep -ixE 'CODE_OF_CONDUCT(\.md)?|CONTRIBUTING(\.md)?' | head -1)
    if [ -n "$coc" ]; then
      a=$(git -C "$d" show "HEAD:$coc" 2>/dev/null | grep -oiE 'laws of [A-Z][a-z]+|jurisdiction of [A-Z][a-z]+' | head -1)
      [ -n "$a" ] && { rax="coc-jurisdiction"; reg="?$a"; }
    fi
  fi
  printf '%s\tOK\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$repo" "$hd" "$lp" "$by" "$sh" "$fl" "${ho:--}" "$ax" "$ev" "$rax" "$reg"
done
