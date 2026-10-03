#!/bin/bash
# P172, semantic-data layer — read the cession where an ontology or a DCAT/VOID dataset
# description actually declares it, inside the data file.
#
# Extraction is delegated to extract_license.py, which carries a named control for each of the
# three serialization defects this pass found (D1 predicate-as-URI, D2 blank-node indirection,
# D3 depth).  See that file and test_extract.py.
#
# Depth: a header-only range request reports a FALSE ABSENCE (D3), so the default read is
# 400 KB.  Pass a smaller size as $3 only to probe a known-shallow header cheaply.
# TSV: repo \t file \t verdict \t license_uri
repo="$1"; file="$2"; bytes="${3:-400000}"
here="$(cd "$(dirname "$0")" && pwd)"
out=$(curl -s --max-time 60 -r "0-${bytes}" "https://raw.githubusercontent.com/${repo}/HEAD/${file}" -w $'\n%{http_code}' 2>/dev/null)
code=$(printf '%s' "$out" | tail -1)
case "$code" in 200|206) ;; *) printf '%s\t%s\tUNREACHABLE(%s)\t-\n' "$repo" "$file" "$code"; exit 0;; esac
uri=$(printf '%s' "$out" | sed '$d' | python3 "$here/extract_license.py")
if [ "$uri" != "-" ]; then printf '%s\t%s\tLICENSED-IN-PAYLOAD\t%s\n' "$repo" "$file" "$uri"
else printf '%s\t%s\tNO-DECLARATION\t-\n' "$repo" "$file"; fi
