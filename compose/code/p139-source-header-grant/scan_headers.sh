#!/usr/bin/env sh
# p139-source-header-grant — ACTION CH: when a payload ships NO licence file,
# do the grants live in SOURCE-FILE HEADERS instead?
#
# Executes p138's pre-registered ACTION CH, written as:
#   "a licence-header read showing the grants live in source files rather than licence
#    files, which would make 7 of 21 an overstatement of the defect and an understatement
#    of the obligation."
#
# Same download lane as p138-npm-payload-licence: registry.npmjs.org answers 200 here;
# api.github.com and codeload do not. Every tarball is sha1-verified against the
# registry's own shasum before a single byte is read, so the bytes measured are the
# bytes the registry vouches for.
#
# Usage: scan_headers.sh <package> [<package> ...]
set -eu

emit() {
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$9" "${10}"
}

emit package version spdx_manifest licence_file text_files own_header_grants grant_classes strongest_own_grant vendored_notices verdict

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

for pkg in "$@"; do
  if ! curl -sS --max-time 30 "https://registry.npmjs.org/$pkg" > "$work/meta.json"; then
    emit "$pkg" FETCH_FAILED - - - - - - - FETCH_FAILED
    continue
  fi

  set -- $(python3 -I - "$work/meta.json" <<'PY'
import json, sys
m = json.load(open(sys.argv[1]))
v = m["dist-tags"]["latest"]
d = m["versions"][v]["dist"]
print(v, d["tarball"], d.get("shasum", "-"))
PY
)
  version=$1 tarball=$2 claimed_sha=$3

  if ! curl -sS --max-time 120 -o "$work/pkg.tgz" "$tarball"; then
    emit "$pkg" "$version" - - - - - - - TARBALL_FETCH_FAILED
    continue
  fi

  actual_sha=$(sha1sum "$work/pkg.tgz" | cut -d' ' -f1)
  if [ "$claimed_sha" != "-" ] && [ "$actual_sha" != "$claimed_sha" ]; then
    emit "$pkg" "$version" - - - - - - - SHASUM_MISMATCH
    continue
  fi

  rm -rf "$work/x"; mkdir -p "$work/x"
  tar xzf "$work/pkg.tgz" -C "$work/x" 2>/dev/null || true

  # Is a licence FILE present? (p138's question, re-measured so the two passes agree.)
  licence_file=$(tar tzf "$work/pkg.tgz" \
    | grep -iE '(^|/)(licen[cs]e|copying|notice)([.-][a-z0-9]+)?$' \
    | paste -sd, - )
  [ -n "$licence_file" ] || licence_file=NONE

  spdx=$(python3 -I -c '
import json, sys
try:
    d = json.load(open(sys.argv[1]))
    print(d.get("license") or "ABSENT")
except Exception:
    print("NO_MANIFEST")
' "$work/x/package/package.json" 2>/dev/null || echo NO_MANIFEST)

  # The ACTION CH question, asked of the shipped source files themselves.
  python3 -I "$(dirname "$0")/headers.py" "$work/x" > "$work/h.tsv"
  read -r text_files with_grant classes strongest vendored < "$work/h.tsv"

  if [ "$licence_file" != NONE ]; then
    verdict=HAS_LICENCE_FILE
  elif [ "$with_grant" -gt 0 ]; then
    verdict=GRANT_IN_HEADERS_ONLY
  else
    verdict=NO_GRANT_IN_PAYLOAD
  fi

  emit "$pkg" "$version" "$spdx" "$licence_file" "$text_files" "$with_grant" "$classes" "$strongest" "$vendored" "$verdict"
done
