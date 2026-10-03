#!/bin/bash
# SUPERSEDED INSTRUMENT — this path now delegates to the corrected one.
#
# Pass 65 (2026-10-03) executed action 2 of pass 64: the license instrument lives IN the
# instrument, not in prose.  The probe that used to be here enumerated BRANCHES
# (`main`, `master`) and 4 file names, and that specification has two measured blind spots:
#
#   P170  a repo whose default branch is neither `main` nor `master` is reported as
#         unlicensed.  Measured: `frappe/education` declares in `develop/license.txt`.
#         Over the 200-row denominator the branch-limited form mislabels 7 of 160 licensed
#         repos.  `raw.githubusercontent.com` resolves the ref `HEAD` to the default branch
#         whatever it is named, so the branch dimension DISAPPEARS: 14 names x 1 ref.
#   P171  classifying by grepping the BODY labels GPL-3.0 as AGPL-3.0, because §13 of
#         GPL-3.0 is TITLED "Use with the GNU Affero General Public License".  Classification
#         is done on the TITLE (first 12 lines).
#
# The superseded probes are kept, dated, as NEGATIVE CONTROLS:
#   scan_license.SUPERSEDED-2026-10-03.sh   scan_altnames.SUPERSEDED-2026-10-03.sh
# and the two outputs can be diffed:
#   ../p170-headref-license-sweep/result.2026-10-03.tsv                (HEAD ref, authoritative)
#   ../p170-headref-license-sweep/result-branchlimited.2026-10-03.tsv  (main/master, control)
#
# A license FILE is not the only place a cession lives.  For the payload question, see
# ../p172-payload-license-sweep/ (P172): of the 32 rows this layer calls UNLICENSED, 10 declare
# a cession inside the data or the manifest.
exec "$(cd "$(dirname "$0")/../p170-headref-license-sweep" && pwd)/sweep_headref.sh" "$@"
