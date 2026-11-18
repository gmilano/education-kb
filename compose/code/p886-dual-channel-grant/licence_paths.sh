#!/bin/sh
# p886 — the licence-path ladder, CASE-COMPLETE.
#
# `raw.githubusercontent.com` serves paths CASE-SENSITIVELY. p885's shipped ladder
# (compose/code/p885-symref-grant-ladder/fetch_grants.sh:40) probes:
#
#   LICENSE LICENSE.md LICENSE.txt license.txt COPYING COPYING.txt COPYING.TXT LICENCE
#
# `LICENSE.TXT` (uppercase extension) and `LICENSE.rst` are both absent from that
# list. p886 ran `885-G1`'s acceptance test over 163 shelf rows and that hole
# produced a MANUFACTURED ABSENCE on `openedx/XBlock` and `openedx/xblock-sdk` --
# Apache-2.0, 11,358 B, sha256_12 cfc7749b96f6, at `master/LICENSE.TXT`.
#
# 🔴 The reason this matters more than two rows: `repos/foundations.md:408-409`
# ALREADY records both grants correctly, by that exact filename, and :758 already
# names the uppercase-extension trap. So the shelf was right and the INSTRUMENT
# built to verify the shelf could not reproduce it. An unattended two-channel gate
# of that quality reports "field asserts, payload denies" -- `885-G1`'s own error
# class -- against correct cells. The gate must be at least as good as the shelf
# before its disagreements mean anything.
#
# Ordering is by measured frequency, so the common case still exits on probe 1:
# 156 of 167 p886 rows hit within the first four entries.
LICENCE_PATHS="LICENSE LICENSE.md LICENSE.txt LICENSE.TXT
LICENCE LICENCE.md LICENCE.txt LICENCE.TXT
License License.md License.txt
license license.md license.txt
licence licence.md licence.txt
LICENSE.rst LICENCE.rst license.rst License.rst
LICENSE.text LICENSE.markdown
COPYING COPYING.md COPYING.txt COPYING.TXT COPYING.LESSER
LICENSE-MIT LICENSE-APACHE LICENSE-AGPL LICENSE-GPL
docs/LICENSE doc/LICENSE LICENSES/LICENSE .github/LICENSE
COPYRIGHT COPYRIGHT.txt"
