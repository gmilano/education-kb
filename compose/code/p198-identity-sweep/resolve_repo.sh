#!/bin/bash
# P198 -- REACHABILITY of a declared repository, probed over a MATRIX of (ref x filename).
#
# Why a matrix and not one probe: pass 68's instruments probed `raw/<owner>/<repo>/HEAD/README.md`
# and read a 404 as "the repo does not resolve".  Measured on 2026-10-03, that probe calls
# `UCL-INGI/INGInious` DEAD -- a repo this KB QUOTES as a recommended piece, that answers 200 on
# `HEAD/LICENSE` and on `master/README.rst`.  The repo has no `README.md` AT ALL: it ships
# `README.rst`.  A one-filename probe does not measure reachability, it measures a filename
# convention, and it manufactures false tombstones (P198).
#
# A repo is declared unreachable ONLY when every cell of the matrix fails.
# Prints: the first "ref/file code" that answered 200, or ALL-404 with the number of cells tried.
owner_repo="$1"
for ref in HEAD main master; do
  for f in README.md README.rst README README.txt LICENSE LICENSE.md LICENSE.txt COPYING package.json pyproject.toml setup.py; do
    c=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 15 \
        "https://raw.githubusercontent.com/$owner_repo/$ref/$f" 2>/dev/null)
    if [ "$c" = "200" ]; then echo "RESOLVES	$ref/$f"; exit 0; fi
  done
done
echo "ALL-404	33-cells"
exit 0
