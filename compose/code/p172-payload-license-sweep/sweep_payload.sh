#!/bin/bash
# P172 — Does the cession live INSIDE the data?
#
# Pass 64 measured 32 rows of agents/top.md as UNLICENSED by asking a FILE question:
# "is there a license FILE at any of 14 names?".  P172 (found in FWU-DE's ontologies, whose
# cession sits in a dct:license annotation inside src/ontology/*-edit.owl) says that question
# can return a false absence, because the cession may be declared in the PAYLOAD.
#
# This instrument asks the payload question for the same slugs.  It inherits the two
# corrections pass 64 paid for:
#   P170 — ref HEAD, never a branch list (covers main/master/develop/trunk by construction).
#   P171 — classify on the DECLARATION, never a body grep for the word "license".
#
# A declaration is a KEY WITH A VALUE, not the word appearing somewhere.  "license" inside a
# dependency name, a URL, or a sentence is NOT a cession and must not be counted as one.
#
# TSV: slug \t verdict \t path \t declaration \t class
#   PAYLOAD-LICENSED  a declaration with a value was READ in a payload file
#   PAYLOAD-SILENT    every payload path probed was 404, or present and carrying no declaration
#   UNREACHABLE       the repo could not be reached at all by this channel
slug="$1"

# Payload paths, by class.  No listing channel is needed: these are convention-named.
MANIFESTS="package.json pyproject.toml setup.py setup.cfg composer.json Cargo.toml pom.xml build.gradle codemeta.json .zenodo.json"
CITATION="CITATION.cff CITATION.bib"
MOODLE="version.php lib.php settings.php index.php"
SEMANTIC="catalog.ttl ontology.ttl context.jsonld vocab.ttl index.ttl"

emit() { printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$1" "$2" "$3" "$4"; exit 0; }

get() { # path -> body on stdout, 0 if 200
  local out code
  out=$(curl -s --max-time 25 -w $'\n%{http_code}' "https://raw.githubusercontent.com/${slug}/HEAD/$1" 2>/dev/null)
  code=$(printf '%s' "$out" | tail -1)
  [ "$code" = "200" ] || return 1
  printf '%s' "$out" | sed '$d'
}

seen_any=0

# 1. Manifests: a license KEY with a VALUE.
for f in $MANIFESTS; do
  body=$(get "$f") || continue
  seen_any=1
  case "$f" in
    *.json)
      # "license": "MIT"  |  "license": {"type": "MIT"}
      d=$(printf '%s' "$body" | grep -oiE '"licen[sc]e"[[:space:]]*:[[:space:]]*"[^"]+"' | head -1 \
          | sed -E 's/.*:[[:space:]]*"([^"]+)"/\1/')
      [ -z "$d" ] && d=$(printf '%s' "$body" | grep -oiE '"licen[sc]e"[[:space:]]*:[[:space:]]*\{[^}]*"type"[[:space:]]*:[[:space:]]*"[^"]+"' | head -1 | sed -E 's/.*"type"[[:space:]]*:[[:space:]]*"([^"]+)"/\1/')
      ;;
    *.toml)
      # license = "MIT" | license = {text = "MIT"} | classifiers License :: ...
      d=$(printf '%s' "$body" | grep -oiE '^[[:space:]]*licen[sc]e[[:space:]]*=[[:space:]]*"[^"]+"' | head -1 | sed -E 's/.*"([^"]+)"/\1/')
      [ -z "$d" ] && d=$(printf '%s' "$body" | grep -oiE '^[[:space:]]*licen[sc]e[[:space:]]*=[[:space:]]*\{[^}]*(text|file)[[:space:]]*=[[:space:]]*"[^"]+"' | head -1 | sed -E 's/.*"([^"]+)"/\1/')
      [ -z "$d" ] && d=$(printf '%s' "$body" | grep -oE 'License :: [^"]+' | head -1)
      ;;
    *.py|*.cfg)
      d=$(printf '%s' "$body" | grep -oiE '^[[:space:]]*licen[sc]e[[:space:]]*=[[:space:]]*.{0,60}' | head -1 \
          | sed -E "s/^[[:space:]]*[Ll]icen[sc]e[[:space:]]*=[[:space:]]*//; s/^['\"]//; s/['\",].*$//")
      [ -z "$d" ] && d=$(printf '%s' "$body" | grep -oE 'License :: [^"'"'"']+' | head -1)
      ;;
    *.xml|*.gradle)
      d=$(printf '%s' "$body" | grep -oiE '<name>[^<]*licen[sc]e[^<]*</name>|<licenses?>' | head -1)
      [ -z "$d" ] && d=$(printf '%s' "$body" | grep -oiE 'licen[sc]e[[:space:]]*=[[:space:]]*.{0,40}' | head -1)
      ;;
  esac
  d=$(printf '%s' "$d" | tr -d '\n' | cut -c1-70)
  [ -n "$d" ] && emit "PAYLOAD-LICENSED" "$f" "$d" "manifest"
done

# 2. CITATION.cff / .bib: a license key is part of the citation record.
for f in $CITATION; do
  body=$(get "$f") || continue
  seen_any=1
  d=$(printf '%s' "$body" | grep -oiE '^[[:space:]]*licen[sc]e[[:space:]]*:[[:space:]]*.{1,60}' | head -1 | sed -E 's/^[[:space:]]*[Ll]icen[sc]e[[:space:]]*:[[:space:]]*//')
  d=$(printf '%s' "$d" | tr -d '\n' | cut -c1-70)
  [ -n "$d" ] && emit "PAYLOAD-LICENSED" "$f" "$d" "citation"
done

# 3. Source headers.  The Moodle plugin convention puts the GPL grant in EVERY source file;
#    a plugin can therefore carry its cession with no license file at all.
for f in $MOODLE; do
  body=$(get "$f") || continue
  seen_any=1
  d=$(printf '%s' "$body" | grep -oiE 'GNU (Affero )?General Public License[^.]{0,40}' | head -1)
  [ -z "$d" ] && d=$(printf '%s' "$body" | grep -oiE '@license[[:space:]]+.{1,50}' | head -1)
  d=$(printf '%s' "$d" | tr -d '\n' | cut -c1-70)
  [ -n "$d" ] && emit "PAYLOAD-LICENSED" "$f" "$d" "source-header"
done

# 4. Semantic data: the FWU case.  dct:license / cc:license / schema:license annotation.
for f in $SEMANTIC; do
  body=$(get "$f") || continue
  seen_any=1
  d=$(printf '%s' "$body" | grep -oiE '(dct|dcterms|cc|schema|dc):licen[sc]e[[:space:]]*.{1,60}' | head -1)
  d=$(printf '%s' "$d" | tr -d '\n' | cut -c1-70)
  [ -n "$d" ] && emit "PAYLOAD-LICENSED" "$f" "$d" "semantic-annotation"
done

# Reachability control, identical in spirit to p170's: silence is only measurable on a repo
# we can actually reach.
if [ "$seen_any" = "1" ]; then
  emit "PAYLOAD-SILENT" "-" "(payload files read, no declaration)" "-"
fi
for rm in README.md README.rst readme.md README README.markdown docs/README.md; do
  if get "$rm" >/dev/null; then emit "PAYLOAD-SILENT" "-" "(reachable via $rm, no payload file at probed names)" "-"; fi
done
emit "UNREACHABLE" "-" "-" "-"
