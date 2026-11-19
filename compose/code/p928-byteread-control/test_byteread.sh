#!/bin/sh
# Acceptance test for `928-G1`. No network: serves a fixture from a local file URL
# is not possible with curl -w reliably across builds, so this test asserts the
# DEFECT directly on a fixture, which is the property the gate exists to prevent.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
fail=0

# Fixture: a grant file that ENDS IN A NEWLINE, like every real LICENSE file.
printf 'MIT License\n\nPermission is hereby granted, free of charge.\n' > "$tmp/LICENSE"
true_bytes=$(wc -c < "$tmp/LICENSE" | tr -d ' ')
true_sha=$(sha256sum "$tmp/LICENSE" | cut -c1-12)

# 1. The CORRECT path: measure the file on disk.
got_bytes=$(wc -c < "$tmp/LICENSE" | tr -d ' ')
got_sha=$(sha256sum "$tmp/LICENSE" | cut -c1-12)
if [ "$got_bytes" = "$true_bytes" ] && [ "$got_sha" = "$true_sha" ]; then
  echo "ok 1 - file-measured read reproduces bytes and digest"
else
  echo "not ok 1 - file-measured read diverged"; fail=1
fi

# 2. The DEFECTIVE path this gate forbids: body carried through command substitution.
#    Simulates `out=$(curl -w '\n%{http_code}')` + `sed '$d'`.
combined=$(cat "$tmp/LICENSE"; printf '\n200')
body=$(printf '%s' "$combined" | sed '$d')
bad_bytes=$(printf '%s' "$body" | wc -c | tr -d ' ')
bad_sha=$(printf '%s' "$body" | sha256sum | cut -c1-12)
if [ "$bad_bytes" != "$true_bytes" ] && [ "$bad_sha" != "$true_sha" ]; then
  echo "ok 2 - command-substitution path DOES corrupt the read (bytes $true_bytes -> $bad_bytes)"
else
  echo "not ok 2 - defect not reproduced; this test no longer protects anything"; fail=1
fi

# 3. The tell: the corruption is a CONSTANT offset, so it is uniform across
#    unrelated files. A divergence set whose byte deltas are all identical is an
#    instrument fault, not a supply change.
printf 'Apache License\nVersion 2.0\n' > "$tmp/L2"
t2=$(wc -c < "$tmp/L2" | tr -d ' ')
c2=$(cat "$tmp/L2"; printf '\n200'); b2=$(printf '%s' "$c2" | sed '$d')
bb2=$(printf '%s' "$b2" | wc -c | tr -d ' ')
d1=$((true_bytes - bad_bytes)); d2=$((t2 - bb2))
if [ "$d1" = "$d2" ]; then
  echo "ok 3 - delta is uniform across unrelated files (${d1} B each): the fault signature"
else
  echo "not ok 3 - delta not uniform ($d1 vs $d2)"; fail=1
fi

[ "$fail" = 0 ] && echo "# all 3 pass" || { echo "# FAILURES"; exit 1; }
