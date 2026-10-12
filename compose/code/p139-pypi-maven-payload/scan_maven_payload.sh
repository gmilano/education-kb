#!/usr/bin/env sh
# p139-pypi-maven-payload, Maven half — does a PUBLISHED jar carry the licence its POM declares?
#
# Usage: scan_maven_payload.sh <groupId:artifactId> [...]
#
# Channel constraints that shape this script, recorded because they bound the result:
#   🔴 search.maven.org/solrsearch and central.sonatype.com/api both answer 403 through this
#      proxy, so there is NO search: coordinates must be named, and every coordinate here is
#      tied to a repository this KB already cites.
#   🔴 repo1.maven.org answers 200 but RATE LIMITS this shared egress IP with HTTP 429
#      ("Your ip has exceeded rate limits"). Hence the sleep between requests and the retry.
#
# Method, as p138's: read the manifest (the POM's <licenses>), fetch the artefact a client
# actually puts on its classpath (the jar), verify bytes against the repository's own sha1,
# and look for a licence FILE inside -- independently of what the POM declares.
#
# Maven convention puts a licence at META-INF/LICENSE or META-INF/LICENSE.txt inside the jar.
set -u

SLEEP=${MAVEN_SLEEP:-4}

emit() { printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "$4" "$5" "$6" "$7"; }

fetch() {   # fetch <url> <out> -- one retry after a 429, then give up and say so
  url=$1; out=$2
  code=$(curl -sS --max-time 60 -o "$out" -w '%{http_code}' "$url" 2>/dev/null || echo 000)
  if [ "$code" = "429" ]; then
    sleep $((SLEEP * 3))
    code=$(curl -sS --max-time 60 -o "$out" -w '%{http_code}' "$url" 2>/dev/null || echo 000)
  fi
  echo "$code"
}

emit coordinate version pom_license jar_paths licence_in_jar sha1 notes

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

for coord in "$@"; do
  group=$(printf '%s' "$coord" | cut -d: -f1 | tr '.' '/')
  artifact=$(printf '%s' "$coord" | cut -d: -f2)
  base="https://repo1.maven.org/maven2/$group/$artifact"

  code=$(fetch "$base/maven-metadata.xml" "$work/meta.xml")
  if [ "$code" != "200" ]; then
    emit "$coord" "HTTP_$code" - - - - "metadata unavailable"
    sleep "$SLEEP"
    continue
  fi

  # Latest RELEASE, falling back to the last <version> listed.
  version=$(sed -n 's:.*<release>\(.*\)</release>.*:\1:p' "$work/meta.xml" | tail -1)
  [ -n "$version" ] || version=$(sed -n 's:.*<version>\(.*\)</version>.*:\1:p' "$work/meta.xml" | tail -1)
  if [ -z "$version" ]; then
    emit "$coord" NO_VERSION - - - - "metadata has no version"
    sleep "$SLEEP"
    continue
  fi

  sleep "$SLEEP"
  code=$(fetch "$base/$version/$artifact-$version.pom" "$work/pom.xml")
  if [ "$code" = "200" ]; then
    # An XML parser, not a regex: see pom_license.py's docstring for the three
    # developer names the sed version published as licences.
    pom_license=$(python3 -I "$(dirname "$0")/pom_license.py" "$work/pom.xml" \
      | cut -f1 | paste -sd'+' - | cut -c1-70)
    [ -n "$pom_license" ] || pom_license=NONE_DECLARED
  else
    pom_license="POM_HTTP_$code"
  fi

  sleep "$SLEEP"
  code=$(fetch "$base/$version/$artifact-$version.jar" "$work/a.jar")
  if [ "$code" != "200" ]; then
    emit "$coord" "$version" "$pom_license" - - - "jar HTTP_$code (packaging may be pom/war)"
    sleep "$SLEEP"
    continue
  fi

  # Identity: the repository publishes a .sha1 beside the artefact.
  sleep "$SLEEP"
  scode=$(fetch "$base/$version/$artifact-$version.jar.sha1" "$work/a.sha1")
  actual=$(sha1sum "$work/a.jar" | cut -d' ' -f1)
  if [ "$scode" = "200" ]; then
    claimed=$(cut -d' ' -f1 < "$work/a.sha1" | tr -d '\r\n ')
    if [ "$claimed" != "$actual" ]; then
      emit "$coord" "$version" "$pom_license" - - "$actual" "SHA1_MISMATCH vs $claimed"
      sleep "$SLEEP"
      continue
    fi
    shanote="sha1 verified"
  else
    shanote="sha1 unavailable (HTTP_$scode)"
  fi

  paths=$(unzip -Z1 "$work/a.jar" 2>/dev/null | grep -c '' || echo 0)
  lic=$(unzip -Z1 "$work/a.jar" 2>/dev/null \
    | grep -iE '(^|/)(licen[cs]e|copying|notice)([._-][a-z0-9.+-]*)?$|\.licen[cs]e$' \
    | head -4 | paste -sd, - )
  [ -n "$lic" ] || lic=NONE

  emit "$coord" "$version" "$pom_license" "$paths" "$lic" "$actual" "$shanote"
  sleep "$SLEEP"
done
