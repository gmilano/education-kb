#!/usr/bin/env bash
# P852 — battery candidate -> shelf verdict.
# P840: word-bounded, substring count reported beside it.
# P849: validate the instrument against a token known PRESENT before believing a zero.
# P853: a probe must EXCLUDE ITS OWN ARTEFACTS from the corpus it measures, and must
#       count live shelf separately from archive/. Self-contamination biases every
#       verdict toward SHELVED — the error that SUPPRESSES a finding, the mirror of P849.
set -uo pipefail

ROOT="${1:?kb root}"
CANDS="${2:?candidates file}"
SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SELF_REL="${SELF_DIR#"$ROOT"/}"

# corpus = tracked .md/.tsv, minus .git, minus archive/, minus THIS PROBE'S OWN DIR
live_corpus() {
  find "$ROOT" \( -name '*.md' -o -name '*.tsv' \) -type f \
    -not -path "$ROOT/.git/*" \
    -not -path "$ROOT/archive/*" \
    -not -path "$SELF_DIR/*" -print0
}
archive_corpus() {
  find "$ROOT/archive" \( -name '*.md' -o -name '*.tsv' \) -type f -print0 2>/dev/null
}

count_files() { # pattern, corpus-fn
  local pat="$1" fn="$2"
  "$fn" | xargs -0 -r grep -ilwE -- "$pat" 2>/dev/null | wc -l | tr -d ' '
}
count_subs() {
  local pat="$1" fn="$2"
  "$fn" | xargs -0 -r grep -oiE -- "$pat" 2>/dev/null | wc -l | tr -d ' '
}

echo "=== P853 corpus (self-excluded: $SELF_REL) ==="
printf 'live=%s archive=%s\n' \
  "$(live_corpus | xargs -0 -r -n1 echo | wc -l | tr -d ' ')" \
  "$(archive_corpus | xargs -0 -r -n1 echo | wc -l | tr -d ' ')"

echo
echo "=== P849 positive control (must all be non-zero) ==="
ctl_fail=0
for t in "Moodle" "Open edX" "IESALC" "IDB"; do
  n=$(count_files "$t" live_corpus)
  if [ "$n" -eq 0 ]; then echo "CONTROL-FAIL	$t	0"; ctl_fail=1; else echo "CONTROL-OK	$t	$n"; fi
done
[ "$ctl_fail" -eq 0 ] || { echo "ABORT: P849 control failed; zeros uninterpretable." >&2; exit 2; }

echo
printf '%s\t%s\t%s\t%s\t%s\t%s\n' limb candidate live_files live_subs archive_files verdict
while IFS=$'\t' read -r limb label pat; do
  case "${limb:-}" in ''|'#'*) continue ;; esac
  lf=$(count_files "$pat" live_corpus)
  ls=$(count_subs  "$pat" live_corpus)
  af=$(count_files "$pat" archive_corpus)
  if   [ "$lf" -gt 0 ]; then v=SHELVED
  elif [ "$af" -gt 0 ]; then v=ARCHIVE-ONLY
  else v=UNSHELVED; fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$limb" "$label" "$lf" "$ls" "$af" "$v"
done < "$CANDS"
