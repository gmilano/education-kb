#!/usr/bin/env bash
# ACTION C (layer P) — read the reverse-DNS package namespace from the tree.
# A Maven <groupId>, a Gradle group, or a Java source path src/main/java/<tld>/<org>
# encodes an organisation's own domain, which is evidence of AFFILIATION rather
# than of the market a repository serves (the P800 trap layer D is exposed to).
set -uo pipefail
probe_ns() {
  local addr="$1" b p url body code
  for b in main master; do
    for p in pom.xml build.gradle build.gradle.kts; do
      url="https://raw.githubusercontent.com/${addr}/${b}/${p}"
      body="$(curl -sL --max-time 12 -w '\nHTTPCODE:%{http_code}' "$url" 2>/dev/null)"
      code="${body##*HTTPCODE:}"
      [ "$code" = "200" ] || continue
      body="${body%$'\n'HTTPCODE:*}"
      local g=""
      case "$p" in
        pom.xml)
          g="$(printf '%s' "$body" | tr -d ' \t' | grep -m1 -oP '(?<=<groupId>)[^<]+' )" ;;
        *)
          g="$(printf '%s' "$body" | grep -m1 -oE "^[[:space:]]*group[[:space:]]*=?[[:space:]]*[\"'][^\"']+" | grep -oE "[\"'][^\"']+" | tr -d "\"'")" ;;
      esac
      [ -n "$g" ] && { printf '%s\t%s\t%s\t%s\n' "$addr" "$b" "$p" "$g"; return 0; }
    done
  done
  return 0
}
export -f probe_ns
grep -vE '^\s*(#|$)' "$1" | xargs -P 32 -I{} bash -c 'probe_ns "$@"' _ {}
