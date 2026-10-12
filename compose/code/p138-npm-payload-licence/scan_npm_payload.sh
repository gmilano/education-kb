#!/usr/bin/env sh
# p138-npm-payload-licence — does the PUBLISHED package carry the licence its manifest claims?
#
# Executes p137's ACTION CD. Reads the registry, downloads each tarball, verifies the
# registry's own shasum against the bytes received, enumerates every path, and reports
# whether a licence FILE is present -- independently of the manifest's SPDX id.
#
# Channel note: registry.npmjs.org answers 200 here; api.github.com and codeload do not.
# Usage: scan_npm_payload.sh <package> [<package> ...]
set -eu

emit() { printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "$4" "$5" "$6" "$7"; }

emit package version published spdx_id files_field paths licence_file

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

for pkg in "$@"; do
  if ! curl -sS --max-time 30 "https://registry.npmjs.org/$pkg" > "$work/meta.json"; then
    emit "$pkg" FETCH_FAILED - - - - -
    continue
  fi

  # Registry metadata: latest version, its publish time, and its claimed tarball + shasum.
  set -- $(python3 -I - "$work/meta.json" <<'PY'
import json, sys
m = json.load(open(sys.argv[1]))
v = m["dist-tags"]["latest"]
d = m["versions"][v]["dist"]
print(v, m.get("time", {}).get(v, "-"), d["tarball"], d.get("shasum", "-"))
PY
)
  version=$1 published=$2 tarball=$3 claimed_sha=$4

  if ! curl -sS --max-time 90 -o "$work/pkg.tgz" "$tarball"; then
    emit "$pkg" "$version" "$published" - - TARBALL_FETCH_FAILED -
    continue
  fi

  # Identity: the bytes we measured must be the bytes the registry vouches for.
  actual_sha=$(sha1sum "$work/pkg.tgz" | cut -d' ' -f1)
  if [ "$claimed_sha" != "-" ] && [ "$actual_sha" != "$claimed_sha" ]; then
    emit "$pkg" "$version" "$published" - - SHASUM_MISMATCH "$actual_sha"
    continue
  fi

  paths=$(tar tzf "$work/pkg.tgz" | wc -l | tr -d ' ')

  # The question: a licence FILE in the payload, not an identifier in a manifest.
  licence_file=$(tar tzf "$work/pkg.tgz" \
    | grep -iE '(^|/)(licen[cs]e|copying|notice)([.-][a-z0-9]+)?$' \
    | paste -sd, - )
  [ -n "$licence_file" ] || licence_file=NONE

  # The manifest as PACKED, which is the one that shipped.
  rm -rf "$work/x"; mkdir -p "$work/x"
  tar xzf "$work/pkg.tgz" -C "$work/x" package/package.json 2>/dev/null || true
  if [ -f "$work/x/package/package.json" ]; then
    set -- $(python3 -I - "$work/x/package/package.json" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
f = d.get("files")
print(d.get("license") or "ABSENT", ("|".join(f) if f else "ABSENT"))
PY
)
    spdx=$1 files_field=$2
  else
    spdx=NO_MANIFEST files_field=NO_MANIFEST
  fi

  emit "$pkg" "$version" "$published" "$spdx" "$files_field" "$paths" "$licence_file"
done
