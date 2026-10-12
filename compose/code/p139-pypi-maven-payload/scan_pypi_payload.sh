#!/usr/bin/env sh
# p139-pypi-maven-payload — does a PUBLISHED Python artefact carry the licence its metadata
# claims? `p138-npm-payload-licence` generalised to a second registry, per `ACTION CM`.
#
# Usage: scan_pypi_payload.sh <package> [<package> ...]
#
# Method, identical in shape to p138's:
#   1. read the registry's own metadata (pypi.org/pypi/<pkg>/json)
#   2. download BOTH distributions -- the wheel a client installs and the sdist
#   3. verify the bytes against the registry's own sha256 (npm gave sha1; PyPI gives sha256)
#   4. enumerate paths and look for a licence FILE, independently of any declared identifier
#
# What differs from npm, and why the comparison is still fair:
#   * PEP 639 gives Python a `License-Expression` and a `License-File` field, so a package can
#     NAME the file it ships. npm's `files` array only names what to pack.
#   * A wheel puts licence files in `<dist-info>/licenses/` (PEP 639) or directly in
#     `<dist-info>/`. Both are counted. An sdist carries them at the sdist root.
#   * `license_expression` is PEP 639; `license` is the legacy free-text field and may hold a
#     whole licence body rather than an identifier; a `License ::` classifier is a third way.
#     A package DECLARES a licence if any of the three is present.
#
# Channel: pypi.org answers 200 here. Maven Central's SEARCH apis (search.maven.org,
# central.sonatype.com) answer 403 through this proxy; repo1.maven.org itself answers, which
# is why the Maven half is driven from named coordinates in `scan_maven_payload.sh`.
set -eu

emit() { printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8"; }

emit package version declared declared_via license_file_field artefact paths licence_file

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

for pkg in "$@"; do
  # --fail matters: PyPI answers 404 with a JSON body, and without it the probe parsed
  # that body and died on a missing "info" key (observed on `codejail`, which is not a
  # PyPI package at all). A package that is absent from the registry is a row, not a crash.
  if ! curl -sSf --max-time 40 "https://pypi.org/pypi/$pkg/json" > "$work/meta.json" 2>/dev/null; then
    emit "$pkg" NOT_ON_PYPI - - - - - -
    continue
  fi

  # One python call emits one line per distribution: type, filename, url, sha256.
  python3 -I - "$work/meta.json" > "$work/dists.txt" <<'PY'
import json, sys
m = json.load(open(sys.argv[1]))
info = m["info"]
version = info["version"]

expr = info.get("license_expression") or ""
legacy = (info.get("license") or "").strip()
classifiers = [c for c in info.get("classifiers", []) if c.startswith("License ::")]

via = []
if expr:
    via.append("expression")
if legacy:
    via.append("legacy_body" if len(legacy) > 60 else "legacy_field")
if classifiers:
    via.append("classifier")

declared = expr or (legacy[:40] if legacy else "") or (classifiers[0] if classifiers else "")
lf = info.get("license_files") or []

print("\t".join([
    "META", version,
    declared.replace("\t", " ") or "ABSENT",
    "+".join(via) or "none",
    "|".join(lf) or "ABSENT",
]))
for u in m.get("urls", []):
    print("\t".join(["DIST", u["packagetype"], u["filename"], u["url"], u["digests"]["sha256"]]))
PY

  version=$(awk -F'\t' '$1=="META"{print $2}' "$work/dists.txt")
  declared=$(awk -F'\t' '$1=="META"{print $3}' "$work/dists.txt")
  via=$(awk -F'\t' '$1=="META"{print $4}' "$work/dists.txt")
  lf_field=$(awk -F'\t' '$1=="META"{print $5}' "$work/dists.txt")

  if [ -z "$(awk -F'\t' '$1=="DIST"' "$work/dists.txt")" ]; then
    emit "$pkg" "$version" "$declared" "$via" "$lf_field" NO_DISTRIBUTIONS - -
    continue
  fi

  awk -F'\t' '$1=="DIST"' "$work/dists.txt" | while IFS="$(printf '\t')" read -r _ ptype fname url sha; do
    out="$work/$fname"
    if ! curl -sS --max-time 120 -o "$out" "$url"; then
      emit "$pkg" "$version" "$declared" "$via" "$lf_field" "$ptype" FETCH_FAILED -
      continue
    fi
    actual=$(sha256sum "$out" | cut -d' ' -f1)
    if [ "$actual" != "$sha" ]; then
      emit "$pkg" "$version" "$declared" "$via" "$lf_field" "$ptype" SHA256_MISMATCH "$actual"
      continue
    fi

    case "$fname" in
      *.whl|*.zip) paths=$(unzip -Z1 "$out" 2>/dev/null) ;;
      *.tar.gz|*.tgz) paths=$(tar tzf "$out" 2>/dev/null) ;;
      *) paths="" ;;
    esac

    n=$(printf '%s' "$paths" | grep -c '' || true)

    # A licence FILE: the PEP 639 wheel location, the dist-info root, or an sdist root.
    lic=$(printf '%s\n' "$paths" \
      | grep -iE '(^|/)(licen[cs]e|copying|notice)([._-][a-z0-9.+-]*)?$|\.licen[cs]e$' \
      | head -4 | paste -sd, - )
    [ -n "$lic" ] || lic=NONE

    emit "$pkg" "$version" "$declared" "$via" "$lf_field" "$ptype" "$n" "$lic"
  done
done
