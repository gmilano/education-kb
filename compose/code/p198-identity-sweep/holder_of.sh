#!/bin/bash
# Stage 2 of P198 -- how much IDENTITY does the sha256 of a LICENSE actually carry?
#
# P193 (pass 68) says sha256(LICENSE) UNITES a package to its tree, and calls itself a lower
# bound.  This stage measures the bound: a hash identifies a TREE only when the text carries a
# distinguishing HOLDER.  A pristine SPDX boilerplate (Apache-2.0, AGPL-3.0, MIT with no name)
# hashes to the same value for every project on earth that ships it unmodified, so the hash
# carries ZERO identity information -- and this sweep found a live collision between two
# DISTINCT PyPI packages.
#
# Prints: bytes · sha256(12) · copyright line found (or NO-HOLDER-LINE)
pkg="$1"; chan="$2"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
enc=$(printf '%s' "$pkg" | sed 's|/|%2F|')
if [ "$chan" = "npm" ]; then
  tgz=$(curl -sf --max-time 30 "https://registry.npmjs.org/$enc" \
    | python3 -c "import json,sys;d=json.load(sys.stdin);v=d['dist-tags']['latest'];print(d['versions'][v]['dist']['tarball'])" 2>/dev/null)
  [ -z "$tgz" ] && { echo "$pkg: NO-TARBALL"; exit 0; }
  curl -sf --max-time 60 "$tgz" -o "$TMP/p.tgz" || { echo "$pkg: TARBALL-UNREACHABLE"; exit 0; }
  ent=$(tar tzf "$TMP/p.tgz" 2>/dev/null | grep -iE '/(licen[sc]e|copying|notice|unlicense)([.-][a-z0-9]+)?$' | head -1)
  [ -z "$ent" ] && { echo "$pkg: NO-LICENSE-IN-ARTEFACT"; exit 0; }
  tar xzf "$TMP/p.tgz" -O "$ent" > "$TMP/L"
else
  url=$(curl -sf --max-time 30 "https://pypi.org/pypi/$pkg/json" \
    | python3 -c "
import json,sys
d=json.load(sys.stdin)
u=''
for f in d['urls']:
    if f['packagetype']=='sdist': u=f['url']; break
if not u and d['urls']: u=d['urls'][0]['url']
print(u)" 2>/dev/null)
  [ -z "$url" ] && { echo "$pkg: NO-SDIST"; exit 0; }
  curl -sf --max-time 60 "$url" -o "$TMP/s.bin" || { echo "$pkg: SDIST-UNREACHABLE"; exit 0; }
  case "$url" in
    *.whl|*.zip) python3 - "$TMP/s.bin" "$TMP/L" <<'PY' >/dev/null 2>&1
import zipfile,sys,re
z=zipfile.ZipFile(sys.argv[1])
for n in z.namelist():
    if re.search(r'(^|/)(licen[sc]e|copying|notice)([.-][a-z0-9]+)?$', n, re.I):
        open(sys.argv[2],'wb').write(z.read(n)); break
PY
      ;;
    *) ent=$(tar tzf "$TMP/s.bin" 2>/dev/null | grep -iE '/(licen[sc]e|copying|notice)([.-][a-z0-9]+)?$' | head -1)
       [ -n "$ent" ] && tar xzf "$TMP/s.bin" -O "$ent" > "$TMP/L" ;;
  esac
  [ ! -s "$TMP/L" ] && { echo "$pkg: NO-LICENSE-IN-ARTEFACT"; exit 0; }
fi
b=$(wc -c < "$TMP/L" | tr -d ' '); s=$(sha256sum "$TMP/L" | cut -c1-12)
# a holder line is a copyright line that names something beyond a year
h=$(grep -iE '^[[:space:]]*(Copyright|\(c\))' "$TMP/L" | grep -viE 'Copyright \(C\) [0-9]{4} Free Software Foundation' | head -2 | tr '\n' ' | ' | sed 's/[[:space:]]\+/ /g')
[ -z "$h" ] && h="NO-HOLDER-LINE"
printf '%s\t%s\t%s\t%s\n' "$pkg" "$b" "$s" "$h"
