#!/usr/bin/env bash
# `p845-dist-payload` — the offline suite for `lib/dist_payload.sh`.
#
# Pass 76 of 2026-10-09, closing `Gap 330` limb 2.
#
# SINGLE FILE ON PURPOSE (`Gap 300`): this suite runs however it is invoked — `bash
# test_dist_payload.sh`, from another directory, or through `distpayload --self-test` — because
# it sources only the library it tests and builds every fixture itself in a temp tree.
#
# `P841` IS THE REASON THE LIVE ROWS ARE NOT HERE.  An offline suite green on fixtures is not
# evidence the fetch limb is correct: the fixtures encode the formats the author already knew,
# and the registries hold the ones they did not.  So this file asserts the MEASUREMENT, and
# the pass that ships it must additionally re-assert every verdict class against a live
# payload and fold what it finds back in here as a regression.  The cases marked
# `[LIVE-FOLDBACK]` are exactly that: shapes found on pypi.org and repo.packagist.org by
# pass 76 and pinned here so a later edit cannot quietly lose them.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
LIB="$HERE/../lib"
. "$LIB/license_family.sh"
. "$LIB/payload_measure.sh"
. "$LIB/dist_payload.sh"

PASS=0; FAIL=0
ok()   { PASS=$((PASS+1)); printf 'PASS  %s: got=%s want=%s\n' "$1" "$2" "$3"; }
bad()  { FAIL=$((FAIL+1)); printf 'FAIL  %s: got=%s want=%s\n' "$1" "$2" "$3"; }
is()   { if [ "$2" = "$3" ]; then ok "$1" "$2" "$3"; else bad "$1" "$2" "$3"; fi; }

T="$(mktemp -d)"; trap 'rm -rf "$T"' EXIT

MIT_TEXT='MIT License

Copyright (c) 2024 Obada Khalili

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
'
APACHE_TEXT='                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
'

field() { printf '%s' "$1" | cut -f"$2"; }

printf -- '-- (A) the four verdict classes --\n'

# A1 — a root grant ships: PAYLOAD-<family>, read from the file
mkdir -p "$T/a1"; printf '%s' "$MIT_TEXT" > "$T/a1/LICENSE"; echo 'x=1' > "$T/a1/mod.py"
r=$(measure_dist_dir "$T/a1" 'MIT'); rc=$?
is 'A1 exit 0 when a grant ships' "$rc" '0'
is 'A1 verdict names the family read from payload' "$(field "$r" 2)" 'PAYLOAD-MIT'
is 'A1 declared is reported first (P843)' "$(field "$r" 1)" 'MIT'
is 'A1 grant path is the file found' "$(field "$r" 3)" 'LICENSE'
# The shared classifier's holder contract is the whole COPYRIGHT LINE, not a parsed name
# (`license_family.sh::holder_of`).  Asserted as it is rather than re-parsed here: a second
# instrument that "improves" the holder format is exactly the `P255` divergence this library
# exists to avoid (three instruments, three answers, one payload).
is 'A1 holder comes from the payload, not the metadata' "$(field "$r" 6)" 'Copyright (c) 2024 Obada Khalili'

# A2 — the `sprightly` class: declares a licence, ships no notice of any kind
mkdir -p "$T/a2/dist"; echo 'module.exports=1' > "$T/a2/dist/index.js"
r=$(measure_dist_dir "$T/a2" 'MIT'); rc=$?
is 'A2 NO-NOTICE is the sprightly class' "$(field "$r" 2)" 'NO-NOTICE'
is 'A2 notice-file count is a measured zero' "$(field "$r" 7)" '0'
is 'A2 declared survives the defect (P843)' "$(field "$r" 1)" 'MIT'

# A3 — NOTICE-ONLY: no grant file, but a copyright line ships in source
mkdir -p "$T/a3"; printf '# Copyright (c) 2025 Someone\nx=1\n' > "$T/a3/mod.py"
r=$(measure_dist_dir "$T/a3" 'MIT')
is 'A3 a shipped copyright line is weaker than a grant, not equal to none' "$(field "$r" 2)" 'NOTICE-ONLY'
is 'A3 the notice count is reported' "$(field "$r" 7)" '1'

# A4 — NO-PAYLOAD is an instrument failure and must exit non-zero (P827)
mkdir -p "$T/a4empty"
r=$(measure_dist_dir "$T/a4empty" 'MIT'); rc=$?
is 'A4 empty tree is NO-PAYLOAD' "$(field "$r" 2)" 'NO-PAYLOAD'
is 'A4 NO-PAYLOAD exits non-zero (P827)' "$rc" '1'
r=$(measure_dist_dir "$T/does-not-exist" 'MIT'); rc=$?
is 'A4 absent dir exits non-zero too' "$rc" '1'

printf -- '\n-- (B) P171 is inherited, not reimplemented --\n'

# The section-13 trap: GPL-3.0 names the Affero licence in a section TITLE.  A classifier
# that greps the body labels it AGPL.  This instrument must answer GPL-3.0 because it
# delegates to the hardened classifier.
mkdir -p "$T/b1"
{ printf '                    GNU GENERAL PUBLIC LICENSE\n                       Version 3, 29 June 2007\n\n'
  printf '  13. Use with the GNU Affero General Public License.\n'
  printf '  Notwithstanding any other provision of this License...\n'; } > "$T/b1/COPYING"
r=$(measure_dist_dir "$T/b1" 'GPL-3.0')
is 'B1 GPL-3.0 with a section-13 title is NOT mislabelled AGPL (P171)' "$(field "$r" 5)" 'GPL-3.0'
is 'B1 COPYING is recognised as a grant filename' "$(field "$r" 3)" 'COPYING'

mkdir -p "$T/b2"; printf '%s' "$APACHE_TEXT" > "$T/b2/LICENSE.txt"
r=$(measure_dist_dir "$T/b2" 'Apache-2.0')
is 'B2 Apache-2.0 title block classifies' "$(field "$r" 5)" 'Apache-2.0'

printf -- '\n-- (C) filename recognition, the part that decides whether a grant is FOUND --\n'

i=0
for n in LICENSE LICENCE License license.txt LICENSE.md LICENSE.rst COPYING NOTICE \
         LICENSE-MIT LICENSE.APACHE2 licence.md COPYRIGHT; do
  i=$((i+1)); d="$T/c$i"; mkdir -p "$d"; printf '%s' "$MIT_TEXT" > "$d/$n"
  r=$(measure_dist_dir "$d" 'MIT')
  is "C$i '$n' is recognised as a grant" "$(field "$r" 2)" 'PAYLOAD-MIT'
done

# And the negative control: a file that merely CONTAINS the word must not be taken as the grant.
# Measured, and the verdict is the stronger of the two available: the file names no licence
# and carries no copyright line, so it is neither a grant NOR a notice.  A pointer to a
# licence is not a licence.
mkdir -p "$T/cneg"; printf 'see LICENSE for terms\n' > "$T/cneg/README.md"
r=$(measure_dist_dir "$T/cneg" 'MIT')
is 'C-neg a README POINTING at a licence is neither grant nor notice' "$(field "$r" 2)" 'NO-NOTICE'

mkdir -p "$T/cneg2"; printf 'x\n' > "$T/cneg2/licensed_users.csv"
r=$(measure_dist_dir "$T/cneg2" 'MIT')
is 'C-neg2 licensed_users.csv is not a grant filename' "$(field "$r" 2)" 'NO-NOTICE'

printf -- '\n-- (D) the shallowest grant wins, so a vendored one cannot impersonate the root --\n'

mkdir -p "$T/d1/vendor/dep"
printf '%s' "$APACHE_TEXT" > "$T/d1/vendor/dep/LICENSE"
printf '%s' "$MIT_TEXT"    > "$T/d1/LICENSE"
r=$(measure_dist_dir "$T/d1" 'MIT')
is 'D1 the root grant is chosen over the vendored one' "$(field "$r" 3)" 'LICENSE'
is 'D1 and the family is the root family' "$(field "$r" 5)" 'MIT'

# Only a vendored grant exists: it is still reported, because the alternative is to call a
# tree with licences in it NO-NOTICE, which would be false.
mkdir -p "$T/d2/vendor/dep"; printf '%s' "$APACHE_TEXT" > "$T/d2/vendor/dep/LICENSE"
r=$(measure_dist_dir "$T/d2" 'MIT')
is 'D2 a vendored-only grant is reported with its real path' "$(field "$r" 3)" 'vendor/dep/LICENSE'
is 'D2 and declared/payload DISAGREE, which is the point of P843' \
   "$(field "$r" 1)|$(field "$r" 5)" 'MIT|Apache-2.0'

printf -- '\n-- (E) P834: the byte count includes the trailing newline run --\n'

mkdir -p "$T/e1"; printf 'MIT License\n\nCopyright (c) 2024 X\n\n\n' > "$T/e1/LICENSE"
r=$(measure_dist_dir "$T/e1" 'MIT')
want=$(wc -c < "$T/e1/LICENSE" | tr -d ' ')
is 'E1 bytes are byte-exact on disk, trailing newlines included' "$(field "$r" 4)" "$want"

printf -- '\n-- (F) [LIVE-FOLDBACK] shapes found on the registries by pass 76 --\n'

# F1 — a PyPI WHEEL puts the grant inside `*.dist-info/`, not at the root.  Found live on
# `PyLTI1p3-2.0.0-py2.py3-none-any.whl`.  A reader that only looks at the root reports
# NO-NOTICE for a package that ships its grant correctly.
mkdir -p "$T/f1/PyLTI1p3-2.0.0.dist-info" "$T/f1/pylti1p3"
printf '%s' "$MIT_TEXT" > "$T/f1/PyLTI1p3-2.0.0.dist-info/LICENSE"
printf 'x=1\n' > "$T/f1/pylti1p3/__init__.py"
r=$(measure_dist_dir "$T/f1" 'MIT')
is 'F1 a wheel grant under *.dist-info/ is found' "$(field "$r" 2)" 'PAYLOAD-MIT'
is 'F1 and its real path is reported' "$(field "$r" 3)" 'PyLTI1p3-2.0.0.dist-info/LICENSE'

# F2 — a PyPI SDIST nests everything under `<name>-<version>/`, so NOTHING is at depth 1.
mkdir -p "$T/f2/PyLTI1p3-2.0.0"
printf '%s' "$MIT_TEXT" > "$T/f2/PyLTI1p3-2.0.0/LICENSE"
r=$(measure_dist_dir "$T/f2" 'MIT')
is 'F2 an sdist grant one level down is found' "$(field "$r" 3)" 'PyLTI1p3-2.0.0/LICENSE'

# F3 — `dist-info` also carries a METADATA file naming the licence.  It must NOT be mistaken
# for the grant: it is a declaration, and `P843` forbids letting it stand for the payload.
mkdir -p "$T/f3/pkg-1.0.dist-info"
printf 'Name: pkg\nLicense: MIT\n' > "$T/f3/pkg-1.0.dist-info/METADATA"
printf 'x=1\n' > "$T/f3/mod.py"
r=$(measure_dist_dir "$T/f3" 'MIT')
# And the verdict is NO-NOTICE, not NOTICE-ONLY, which is the sharper reading of `P843`:
# MIT's condition is that the COPYRIGHT NOTICE travel with all copies.  A `License: MIT`
# field in `METADATA` names a family and cedes nothing — it is `P179`'s identifier-not-
# cession, so it cannot even be counted as the weaker attribution-survives case.
is 'F3 METADATA naming a licence is a declaration, not a grant AND not a notice' \
   "$(field "$r" 2)" 'NO-NOTICE'

# F4 — Packagist dist zips wrap the tree in `<vendor>-<pkg>-<sha>/`.  Same depth problem.
mkdir -p "$T/f4/packbackbooks-lti-1p3-tool-abc1234/src"
printf '%s' "$APACHE_TEXT" > "$T/f4/packbackbooks-lti-1p3-tool-abc1234/LICENSE"
r=$(measure_dist_dir "$T/f4" 'Apache-2.0')
is 'F4 a Packagist sha-wrapped grant is found' "$(field "$r" 5)" 'Apache-2.0'

printf -- '\n-- (H) [LIVE-FOLDBACK] the DECLARED read, which was wrong when the fetch limb first ran --\n'

# H1 — the exact shape found live on `jwcrypto` 1.6.1: PEP 639 `license_expression` set,
# legacy `license` NULL, no `License ::` classifier.  The first version of this reader
# answered `-` here, and `-` is the verdict an audit waves through.  Pinned so it cannot
# regress: the error direction is REASSURANCE about an LGPL dependency.
cat > "$T/h1.json" <<'JSON'
{"info": {"version": "1.6.1", "license": null,
          "license_expression": "LGPL-3.0-or-later",
          "license_files": ["LICENSE"], "classifiers": []}}
JSON
is 'H1 PEP 639 license_expression is read when the legacy field is null' \
   "$(declared_from_pypi_json "$T/h1.json")" 'LGPL-3.0-or-later'

# H2 — the legacy field still works, and still wins over a classifier.
cat > "$T/h2.json" <<'JSON'
{"info": {"version": "2.0.0", "license": "MIT",
          "classifiers": ["License :: OSI Approved :: BSD License"]}}
JSON
is 'H2 legacy license field is read' "$(declared_from_pypi_json "$T/h2.json")" 'MIT'

# H3 — an SPDX expression OUTRANKS the legacy field, because it is the normative one.
cat > "$T/h3.json" <<'JSON'
{"info": {"version": "1.0", "license": "see LICENSE file",
          "license_expression": "Apache-2.0"}}
JSON
is 'H3 license_expression outranks a prose legacy field' \
   "$(declared_from_pypi_json "$T/h3.json")" 'Apache-2.0'

# H4 — classifier fallback, which is how `PyLTI1p3` itself would be read if it had no field.
cat > "$T/h4.json" <<'JSON'
{"info": {"version": "1.0", "license": "",
          "classifiers": ["Programming Language :: Python",
                          "License :: OSI Approved :: MIT License"]}}
JSON
is 'H4 classifier fallback still works' "$(declared_from_pypi_json "$T/h4.json")" 'MIT License'

# H5 — nothing declared at all is `-`, and `-` must be visibly different from a real answer.
printf '{"info": {"version": "1.0"}}\n' > "$T/h5.json"
is 'H5 no declaration is a visible dash, not an empty string' \
   "$(declared_from_pypi_json "$T/h5.json")" '-'
is 'H5 a missing metadata file is also a dash, not an error' \
   "$(declared_from_pypi_json "$T/absent.json")" '-'
printf 'not json at all\n' > "$T/h6.json"
is 'H6 unparseable metadata is a dash, never a crash' \
   "$(declared_from_pypi_json "$T/h6.json")" '-'

# H7 — Packagist declares an ARRAY, and a disjunction must survive the read.
cat > "$T/h7.json" <<'JSON'
{"packages": {"v/p": [{"version": "1.2.0", "license": ["Apache-2.0"],
                       "dist": {"url": "https://example.invalid/x.zip"}}]}}
JSON
is 'H7 Packagist single licence reads' "$(declared_from_packagist_json "$T/h7.json" 'v/p')" 'Apache-2.0'
cat > "$T/h8.json" <<'JSON'
{"packages": {"v/p": [{"version": "2.0.0", "license": ["MIT", "GPL-2.0-only"]}]}}
JSON
is 'H8 a Packagist disjunction is NOT collapsed to one licence' \
   "$(declared_from_packagist_json "$T/h8.json" 'v/p')" 'MIT,GPL-2.0-only'

# H9 — a dev release must not be preferred over a stable one.
cat > "$T/h9.json" <<'JSON'
{"packages": {"v/p": [{"version": "dev-main", "license": ["WTFPL"]},
                      {"version": "1.0.0", "license": ["Apache-2.0"]}]}}
JSON
is 'H9 the newest STABLE release is read, not dev-main' \
   "$(declared_from_packagist_json "$T/h9.json" 'v/p')" 'Apache-2.0'

printf -- '\n-- (G) licence_paths_in / notice_hits_in are usable on their own --\n'

mkdir -p "$T/g1/a/b"
printf '%s' "$MIT_TEXT" > "$T/g1/LICENSE"
printf '%s' "$MIT_TEXT" > "$T/g1/a/b/COPYING"
n=$(licence_paths_in "$T/g1" | wc -l | tr -d ' ')
is 'G1 both grants are listed' "$n" '2'
is 'G1 output is relative, not absolute' "$(licence_paths_in "$T/g1" | head -1)" 'LICENSE'
is 'G1 an absent dir lists nothing and does not error' "$(licence_paths_in "$T/nope" | wc -l | tr -d ' ')" '0'

# `P831`/`P299`: "submitted" contains "mit".  A substring test would count this as a notice.
mkdir -p "$T/g2"; printf 'this patch was submitted upstream\n' > "$T/g2/notes.txt"
is 'G2 "submitted" is not a licence notice (P299)' "$(notice_hits_in "$T/g2")" '0'
mkdir -p "$T/g3"; printf 'SPDX-License-Identifier: MIT\n' > "$T/g3/mod.py"
is 'G3 an SPDX header IS a notice' "$(notice_hits_in "$T/g3")" '1'

printf -- '\n%s checks run\n' "$((PASS+FAIL))"
if [ "$FAIL" -eq 0 ]; then printf 'ALL CHECKS PASSED\n'; exit 0; fi
printf '%s FAILED\n' "$FAIL"; exit 1
