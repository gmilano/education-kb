#!/usr/bin/env bash
# p1040 limb B -- Gap 399 and the T30/P1033 denominator, through a channel
# that is actually reachable.
#
# Usage: bash packagist.sh            # two TSVs + counts on stderr
#
# Pass 105 measured moodle.org at http=000 ("CONNECT tunnel failed, response
# 403") and opened Gap 399: the Moodle plugin-directory denominator that
# T30/P1033 needs "cannot be measured here at all". Its lead #6 named
# packagist.org as the obvious candidate, never probed from this session,
# because Moodle plugins publish there as composer packages.
#
# Probed this pass: packagist.org = http=200, repo.packagist.org = http=200.
# So the channel is OPEN. What it is NOT is a mirror of the plugin directory --
# that is the finding, and it is measured here rather than assumed, by
# enumerating every moodle-* package type packagist knows and reading the
# licence each package DECLARES in its own composer.json.
#
# P1035 applies: a declared licence string is a CLAIM by the publisher, not a
# payload this KB has read. The two are reported in separate columns and never
# merged. p963's shelf-licence-agreement gate is what would reconcile them.

set -u
cd "$(dirname "$0")"

TYPES="moodle-mod moodle-local moodle-block moodle-theme moodle-filter
moodle-auth moodle-enrol moodle-format moodle-qtype moodle-report moodle-tool
moodle-atto moodle-availability moodle-assignsubmission moodle-assignfeedback
moodle-repository moodle-webservice moodle-plagiarism moodle-gradingform
moodle-message moodle-portfolio moodle-profilefield moodle-qbehaviour
moodle-quizaccess moodle-search moodle-editor moodle-admin moodle-antivirus
moodle-cachestore moodle-customfield moodle-dataformat moodle-fileconverter
moodle-h5plib moodle-media moodle-mlbackend moodle-paygw moodle-qformat
moodle-contenttype moodle-communication moodle-aiprovider moodle-aiplacement
moodle-core moodle-courseformat moodle-tinymce moodle-calendartype
moodle-mnetservice moodle-portfolio moodle-qformat"

TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

# --- B1: the type census, INCLUDING the types that return zero -------------
# A type with no packages is a measurement, not a gap in the sweep. The two
# AI-subsystem types are the reason this limb is worth running at all.
: > "$TMP/pkgs"
printf 'type\tpackages\n' > result.types-packagist.2026-10-10.tsv
for t in $(printf '%s\n' $TYPES | sort -u); do
  code=$(curl -sS --max-time 30 -o "$TMP/l" -w '%{http_code}' \
          "https://packagist.org/packages/list.json?type=$t" 2>/dev/null) || code=000
  if [ "$code" != "200" ]; then
    printf '%s\tHTTP-%s\n' "$t" "$code" >> result.types-packagist.2026-10-10.tsv
    continue
  fi
  n=$(python3 -I -c "
import sys,json
try: print(len(json.load(open('$TMP/l')).get('packageNames',[])))
except Exception: print('PARSE-ERR')
")
  printf '%s\t%s\n' "$t" "$n" >> result.types-packagist.2026-10-10.tsv
  python3 -I -c "
import json
for p in json.load(open('$TMP/l')).get('packageNames',[]): print('$t\t'+p)
" >> "$TMP/pkgs" 2>/dev/null || true
done

# --- B2: the licence each package DECLARES ---------------------------------
printf 'type\tpackage\tdeclared_licence\tpackage_type\tsource_repo\n' > result.packages-packagist.2026-10-10.tsv
while IFS=$'\t' read -r t p; do
  [ -n "${p:-}" ] || continue
  code=$(curl -sS --max-time 30 -o "$TMP/m" -w '%{http_code}' \
          "https://repo.packagist.org/p2/${p}.json" 2>/dev/null) || code=000
  if [ "$code" != "200" ]; then
    printf '%s\t%s\tHTTP-%s\t-\t-\n' "$t" "$p" "$code" >> result.packages-packagist.2026-10-10.tsv
    continue
  fi
  python3 -I -c "
import json,sys
d=json.load(open('$TMP/m'))
vs=d.get('packages',{}).get('$p') or []
if not vs:
    print('$t\t$p\tNO-VERSIONS\t-\t-'); raise SystemExit
v=vs[0]
lic=v.get('license') or []
lic='+'.join(lic) if lic else 'NO-LICENCE-FIELD'
src=(v.get('source') or {}).get('url') or '-'
print('\t'.join(['$t','$p',lic,v.get('type') or '-',src]))
" >> result.packages-packagist.2026-10-10.tsv 2>/dev/null \
  || printf '%s\t%s\tPARSE-ERR\t-\t-\n' "$t" "$p" >> result.packages-packagist.2026-10-10.tsv
done < "$TMP/pkgs"

tot=$(awk -F'\t' 'NR>1 && $2 ~ /^[0-9]+$/ {s+=$2} END{print s+0}' result.types-packagist.2026-10-10.tsv)
nz=$(awk -F'\t' 'NR>1 && $2 ~ /^[0-9]+$/ && $2>0 {n++} END{print n+0}' result.types-packagist.2026-10-10.tsv)
zero=$(awk -F'\t' 'NR>1 && $2=="0" {n++} END{print n+0}' result.types-packagist.2026-10-10.tsv)
printf 'types_probed=%d types_nonempty=%d types_zero=%d packages=%d\n' \
  "$(( $(wc -l < result.types-packagist.2026-10-10.tsv) - 1 ))" "$nz" "$zero" "$tot" >&2
