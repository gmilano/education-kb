#!/bin/bash
# p689 — ACTION p275/p276 compliant grant enumeration.
# A negative licence verdict is only a finding if the TREE was enumerated AND the
# MANIFEST channel was read.  A path ladder (probing candidate filenames) is not an
# enumeration, and p689's first draft made exactly that mistake.
# Tree is enumerated with a treeless partial clone: full file list, no blob download.
OUT=/tmp/claude-0/-home-user-globant-kb/aba297b6-0b74-5ede-bc03-3a3f55b6c0f1/scratchpad/enum
mkdir -p "$OUT"
for slug in "$@"; do
  d="$OUT/$(echo "$slug" | tr '/' '_')"
  rm -rf "$d"
  if ! git clone -q --filter=blob:none --no-checkout --depth 1 "https://github.com/$slug" "$d" 2>/dev/null; then
    echo -e "$slug\tCLONE-FAILED\t-\t-"; continue
  fi
  tree=$(git -C "$d" ls-tree -r --name-only HEAD 2>/dev/null)
  n=$(printf '%s\n' "$tree" | grep -c .)
  # TREE CHANNEL: any path whose basename looks like a grant, anywhere in the tree
  cand=$(printf '%s\n' "$tree" | grep -iE '(^|/)(licen[cs]e|licencia|licenca|licença|copying|copyright|notice|unlicense|eula|terms)(\.[a-z0-9]+)?$' | paste -sd, -)
  # MANIFEST CHANNEL: read only the manifests, from the partial clone
  man=""
  for m in package.json pyproject.toml setup.py setup.cfg composer.json Cargo.toml build.gradle pom.xml *.gemspec; do
    f=$(printf '%s\n' "$tree" | grep -ixE "$m" | head -1)
    [ -z "$f" ] && continue
    body=$(git -C "$d" show "HEAD:$f" 2>/dev/null | grep -inE '^[^#]*licen[cs]e' | head -3 | tr '\n' ';')
    [ -n "$body" ] && man="$man[$f] $body"
  done
  if [ -n "$cand" ]; then v="TREE-HAS-CANDIDATE"
  elif [ -n "$man" ]; then v="MANIFEST-DECLARES"
  else v="VERIFIED-ABSENT-BOTH-CHANNELS"; fi
  echo -e "$slug\t$v\tfiles=$n\ttree:${cand:--}\tmanifest:${man:--}"
done
