#!/usr/bin/env bash
# `ACTION KY` — p179.  WHAT SHAPE OF REPAIR DOES EACH STRIPPING SITE NEED?
#
# `ACTION KY` was pre-registered with two limbs:
#   limb 1 — a mechanical swap to `size_of_file` works at every site → one commit closes it.
#   limb 2 — at least one probe needs the capture for classification and cannot take the swap.
#
# 🔴 LIMB 1 IS FALSE, and limb 2 is true for a reason the register did not predict.  `size_of_file`
# takes a PATH.  At 11 of the 12 sites the payload never touches the disk: it is a shell variable,
# and the trailing newline run was destroyed by the command substitution ONE LINE ABOVE the line
# the gate flags.  So the gate locates the SYMPTOM (the count) and not the DEFECT (the capture),
# and no edit to the counting line can repair a payload the shell no longer holds.
#
# This instrument classifies each site by the repair it actually needs:
#
#   A  FILE-IN-HAND     the payload is on disk at the count line → `size_of_file` IS a mechanical
#                       swap.  Repairable in place, one line.
#   B  CAPTURED-BODY    `var=$(curl …)` → no file exists.  Repair = change the FETCH to write to
#                       disk (`curl -o`), then size the file.  A fetch-shape change, not a count
#                       change.
#   C  CAPTURED-BODY + STATUS-LINE   `out=$(curl -w '\n%{http_code}')` then the last line is
#                       stripped back off.  Everything in B, plus the payload/status boundary is
#                       AMBIGUOUS (see `ambiguity_proof.sh`): the trailing run is not merely lost,
#                       it is UNRECOVERABLE from the capture even in principle.
#
# Usage: bash classify_repair.sh            # TSV on stdout, reads the live tree
set -u
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"

# The 12 sites `ACTION KU`'s gate found, as file:count_line:payload_variable.
SITES='
compose/code/p560-epl-mpl-version-read/sweep_versions.sh:68:body
compose/code/p250-commercial-use-axis/sweep_commercial.sh:17:content
compose/code/p170-headref-license-sweep/sweep_headref.sh:37:content
compose/code/p206-erp-layer-license/sweep_erp.sh:54:body
compose/code/p211-case-retro-sweep/sweep_retro.sh:67:body
compose/code/p122-prose-licence-census/scan_licences.sh:24:body
compose/code/p324-corpus-upstream-cession/resolve_upstream.sh:27:body
compose/code/p784-licence-scope-map/probe.sh:91:body
compose/code/p117-second-channel/licence.sh:50:body
compose/code/p117-second-channel/title.sh:10:body
compose/code/p326-titleholder-book-license/sweep_titleholder.sh:24:raw_lic
compose/code/p326-titleholder-book-license/controls.sh:24:f
'

printf 'site\tvar\tcapture_line\tclass\trepair\n'
a=0; b=0; c=0; miss=0
for s in $SITES; do
  f="${s%%:*}"; rest="${s#*:}"; ln="${rest%%:*}"; var="${rest##*:}"
  src="$ROOT/$f"
  [ -f "$src" ] || { printf '%s\tMISSING\t-\t-\t-\n' "$f"; miss=$((miss + 1)); continue; }

  # The capture: the last assignment to $var at or above the count line.  The variable may be
  # assigned at the start of a line, after a `local`, or after a `;` — `p122` and `p324` both put
  # the status split and the body split on ONE line, which the first cut of this instrument missed
  # and reported as "none found".  A classifier that cannot see the capture cannot classify it.
  cap=$(awk -v v="$var" -v n="$ln" '
    NR <= n && $0 ~ "(^|[;[:space:]])(local[[:space:]]+)?" v "=" { line = $0; found = NR }
    END { if (found) print line }' "$src" | sed 's/^[[:space:]]*//')
  [ -n "$cap" ] || cap='(none found at or above the count line)'

  # Has the COUNT line itself already been moved to the FULL channel?  Read the count line, not
  # the capture: at a repaired `A` site the capture legitimately stays `$(cat …)`, because it
  # feeds the CLASSIFIER, and only the SIZE moved.  (`lib/payload_measure.sh` makes exactly this
  # distinction for `family_of_file`.)
  countline=$(sed -n "${ln}p" "$src")
  if printf '%s' "$countline" | grep -q 'wc -c < \|size_of_file'; then
    cls='REPAIRED'; rep='already on the FULL channel'
  elif printf '%s' "$cap" | grep -qE '=\$\(cat '; then
    cls='A'; rep='size_of_file on the path already in scope — MECHANICAL'; a=$((a + 1))
  elif printf '%s' "$cap" | grep -qE "sed '\\\$d'|%\\\$'\\\\n'|%\\\$'\\\\n'HTTPCODE|HTTPCODE"; then
    cls='C'; rep='curl -o FILE -w %{http_code}; boundary is AMBIGUOUS as written'; c=$((c + 1))
  elif printf '%s' "$cap" | grep -qE '=\$\((curl|get |payload )'; then
    # A `get()`/`payload()` helper that itself strips a status line is still C.
    helper=$(printf '%s' "$cap" | sed -n 's/.*=\$(\([a-z_]*\) .*/\1/p')
    if [ -n "$helper" ] && grep -qE "^[[:space:]]*$helper\(\)" "$src" \
       && awk -v h="$helper" '$0 ~ "^[[:space:]]*" h "\\(\\)" {f=1} f && /http_code/ {print; exit}' "$src" | grep -q http_code; then
      cls='C'; rep='helper appends %{http_code} then strips it — fetch-shape + boundary'; c=$((c + 1))
    else
      cls='B'; rep='curl -o FILE, then size_of_file — FETCH-SHAPE change'; b=$((b + 1))
    fi
  else
    cls='B'; rep='curl -o FILE, then size_of_file — FETCH-SHAPE change'; b=$((b + 1))
  fi
  printf '%s:%s\t%s\t%s\t%s\t%s\n' "$f" "$ln" "$var" "$cap" "$cls" "$rep"
done
printf '# p179: A(mechanical)=%s  B(fetch-shape)=%s  C(fetch-shape+ambiguous)=%s  missing=%s\n' \
  "$a" "$b" "$c" "$miss"
