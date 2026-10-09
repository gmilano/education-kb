# SHARED distribution-payload reader — source this, do not rewrite it.
#
# Pass 76 of 2026-10-09, closing `Gap 330` limb 2.
#
# WHY THIS FILE EXISTS.  Pass 75 closed `Gap 329` (package name -> repository) and then
# payload-verified the `ltijs` runtime closure by reading the `LICENSE` from inside each
# installed npm `.tgz`.  That is the strongest form of the measurement, because the tarball
# is the file the client deploys.  `Gap 330` recorded what that pass did NOT do: the same
# read for PyPI and Packagist, where only NAME RESOLUTION had been exercised.
#
# This file is the network-free half of that read, per `P838`: split a shared instrument on
# the capability the environment DENIES, not on its calling convention.  Given an ALREADY
# EXTRACTED distribution directory, it locates the grant and measures it.  The fetch half
# lives in `lib/distpayload`.
#
# `P171` IS INHERITED, NOT REIMPLEMENTED.  Every family verdict here delegates to
# `payload_measure.sh`, which delegates to `license_family.sh`.  Pass 77's defect — a sixth
# instrument rewriting the classifier from scratch and reintroducing the GPL/AGPL section-13
# trap — is the reason this file contains no `grep` for a licence name.
#
# `P843` IS THE OUTPUT CONTRACT.  A licence DECLARATION in registry metadata and a licence
# FILE in the shipped artefact are two different measurements.  Every row this file emits
# carries both, declared first, and never lets the first stand for the second.
#
# ---------------------------------------------------------------------------------------
# API
#
# licence_paths_in <dir>            -> newline-separated relative paths of grant candidates
# notice_hits_in <dir>              -> count of files containing a copyright/licence notice
# measure_dist_dir <dir> <declared> -> TSV verdict row (see below)
#
# The verdict vocabulary, which is the point of the instrument:
#
#   PAYLOAD-<family>  a grant file ships, and this is the family read FROM IT
#   NO-NOTICE         no grant file AND no copyright notice anywhere in the payload
#                     -> the `sprightly` class (`Gap 330` limb 1): the artefact cannot
#                        satisfy the MIT/BSD condition that the notice travel with copies
#   NOTICE-ONLY       no grant FILE, but a copyright notice appears in some shipped file
#                     -> weaker defect than NO-NOTICE; attribution survives, full text does not
#   NO-PAYLOAD        the directory is empty or absent -> an instrument failure, not a finding
#
# `P827`: a caller that forgets to check still fails loudly.  `measure_dist_dir` returns
# non-zero on NO-PAYLOAD, and the front end propagates it.

# Candidate grant filenames, as a case-insensitive extended regex over the BASENAME.
# Measured, not guessed: this set is what PyPI wheels (`*.dist-info/`), PyPI sdists (root),
# Packagist zips (root) and npm tarballs (`package/`) actually use.
_DP_LICENCE_RE='^(licen[cs]e|copying|notice|copyright)([._-][a-z0-9]+)*(\.(txt|md|rst|html))?$'

# declared_from_pypi_json <metadata-json-file> -> the DECLARED licence string, or `-`.
#
# Network-free on purpose (`P838`): this is the half of the declaration read that can be
# tested offline, and it is the half that was WRONG when pass 76 first ran the fetch limb.
#
# PEP 639 FIRST, and the order is the finding.  Measured live: `jwcrypto` 1.6.1 leaves the
# legacy `license` field NULL, ships no `License ::` classifier, and carries
# `license_expression: "LGPL-3.0-or-later"`.  A reader that checks only the legacy field and
# the classifiers answers `-` for it — and `-` is the one verdict a licence audit waves
# through, so the error direction is REASSURANCE about a copyleft dependency (`P842`'s
# lesson, on a different field).
declared_from_pypi_json() {
  [ -f "$1" ] || { printf -- '-\n'; return 0; }
  python3 -I - "$1" <<'PY'
import json, sys
try:
    info = (json.load(open(sys.argv[1])) or {}).get("info") or {}
except Exception:
    print("-"); sys.exit(0)
decl = info.get("license_expression") or info.get("license") or ""
if not decl:
    for c in info.get("classifiers") or []:
        if c.startswith("License ::"):
            decl = c.split("::")[-1].strip()
            break
decl = (decl or "-").strip().splitlines()
print((decl[0] if decl else "-")[:60] or "-")
PY
}

# declared_from_packagist_json <metadata-json-file> <vendor/name> -> declared, or `-`.
# Packagist's `license` is an ARRAY, and a package may declare a disjunction ("MIT or
# GPL-2.0"), which is information a single string would destroy — so they are joined.
declared_from_packagist_json() {
  [ -f "$1" ] || { printf -- '-\n'; return 0; }
  NAME="${2:-}" python3 -I - "$1" <<'PY'
import json, os, sys
try:
    d = json.load(open(sys.argv[1])) or {}
except Exception:
    print("-"); sys.exit(0)
pkgs = (d.get("packages") or {}).get(os.environ.get("NAME", "")) or []
rel = None
for p in pkgs:
    if "dev" not in str(p.get("version", "")):
        rel = p
        break
rel = rel or (pkgs[0] if pkgs else {})
lic = rel.get("license") or []
print(",".join(lic) if lic else "-")
PY
}

# licence_paths_in <dir> -> relative paths, one per line, sorted.  Empty output is a result.
licence_paths_in() {
  local d="$1"
  [ -d "$d" ] || return 0
  # -print rather than -printf: BusyBox find has no -printf, and this has to run anywhere.
  find "$d" -type f 2>/dev/null \
    | while IFS= read -r f; do
        local b
        b=$(basename "$f" | tr 'A-Z' 'a-z')
        if printf '%s' "$b" | grep -qE "$_DP_LICENCE_RE"; then
          printf '%s\n' "${f#"$d"/}"
        fi
      done | LC_ALL=C sort
}

# notice_hits_in <dir> -> number of files carrying a copyright or licence-name notice.
# This is the control that distinguishes NO-NOTICE from NOTICE-ONLY.  Word-bounded per
# `P831`/`P299`: "mit" is a substring of permit/submit/limit/commit/omit, so a bare
# substring test would report a notice in any file that says "submitted".
notice_hits_in() {
  local d="$1"
  [ -d "$d" ] || { printf '0\n'; return 0; }
  grep -rliE '(^|[^a-z0-9])(copyright|MIT License|Apache License|BSD License|SPDX-License-Identifier)([^a-z0-9]|$)' \
    "$d" 2>/dev/null | wc -l | tr -d ' '
}

# measure_dist_dir <dir> <declared-licence> -> TSV:
#   declared <TAB> verdict <TAB> grant-path <TAB> bytes <TAB> family <TAB> holder <TAB> notice-files
#
# Fields that do not apply read `-`.  `P834` is inherited: `size_of_file` measures the file
# on disk, so a trailing-newline run is counted rather than stripped by `$(…)`.
measure_dist_dir() {
  local d="$1" declared="${2:--}"
  local paths first bytes family holder notices

  if [ ! -d "$d" ] || [ -z "$(find "$d" -type f 2>/dev/null | head -1)" ]; then
    printf '%s\tNO-PAYLOAD\t-\t-\t-\t-\t-\n' "$declared"
    return 1
  fi

  notices=$(notice_hits_in "$d")
  paths=$(licence_paths_in "$d")

  if [ -n "$paths" ]; then
    # The shallowest candidate wins: a root LICENSE is the distribution's own grant, while a
    # deeper one may belong to a vendored dependency.  Ties break alphabetically via sort -k.
    first=$(printf '%s\n' "$paths" | awk -F/ '{print NF"\t"$0}' | LC_ALL=C sort -k1,1n -k2,2 | head -1 | cut -f2-)
    bytes=$(size_of_file "$d/$first")
    family=$(family_of_file "$d/$first")
    holder=$(holder_of_file "$d/$first")
    [ -n "$family" ] || family='UNCLASSIFIED'
    [ -n "$holder" ] || holder='-'
    printf '%s\tPAYLOAD-%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$declared" "$family" "$first" "$bytes" "$family" "$holder" "$notices"
    return 0
  fi

  if [ "$notices" -gt 0 ]; then
    printf '%s\tNOTICE-ONLY\t-\t-\t-\t-\t%s\n' "$declared" "$notices"
  else
    printf '%s\tNO-NOTICE\t-\t-\t-\t-\t0\n' "$declared"
  fi
  return 0
}
