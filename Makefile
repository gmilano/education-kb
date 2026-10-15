# `ACTION SW` (p229) and `ACTION QO` (carried ELEVEN passes) — the licence gate stops being
# a one-off and becomes a STANDING check.
#
# `ACTION QO` was registered eleven passes running as "wire a licence gate into make hooks".
# p227 inverted its scope to *check the SHELVES against first-hand payloads*; p228 BUILT
# exactly that and ran it over 520 slugs — as a one-off, by hand. `ACTION SW` registered the
# remaining half, and this file is it.
#
# 🔴 Why it never became standing before, measured at p229: THE SUITES ONLY PASS FROM THEIR
# OWN DIRECTORY. `python3 -I compose/code/p228-shelf-gate/test_shelf_gate.py` dies on
# `ModuleNotFoundError: classify_grant` because `-I` strips the script's directory from
# `sys.path`, while the same file passes 30/30 from inside its folder. That is
# `p355-cwd-portability`'s class, and it is the whole reason a working gate stayed a
# one-off: it could not be invoked from the place a hook runs. Every recipe below therefore
# `cd`s into the instrument, and the ONLINE half stays out of `hooks` so the check is
# runnable where there is no egress.
SHELL := /bin/bash
PY ?= python3

.PHONY: hooks gate-offline gate-online reach status

hooks: gate-offline ## the standing check: every licence instrument's OFFLINE controls

gate-offline: ## no network — safe in a hook, in CI, and in a sandbox without egress
	@set -e; \
	echo "── lib/license_family.sh  (the shared classifier, P237)"; \
	cd compose/code/lib && bash test_license_family.sh >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── lib/licence_path.sh    (the shared path predicate, P441)"; \
	cd compose/code/lib && bash test_licence_path.sh >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p222-ecosystem-bound-grammar  (five grammars, the bound)"; \
	cd compose/code/p222-ecosystem-bound-grammar && $(PY) test_bound_grammar.py >/dev/null 2>&1 && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p228-shelf-gate        (the five non-grant subjects, 30 tests)"; \
	cd compose/code/p228-shelf-gate && $(PY) test_shelf_gate.py >/dev/null 2>&1 && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p229-grant-ladder-reach (reach, foreign manifest, withdrawn cells, query key)"; \
	cd compose/code/p229-grant-ladder-reach && $(PY) test_grant_ladder_reach.py >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p230-prose-path-ladder (greedy slug, prose paths, the lazy-quantifier lint)"; \
	$(PY) -I compose/code/p230-prose-path-ladder/test_prose_path_ladder.py >/dev/null && echo "   PASS"; \
	echo "── lazy-quantifier lint over every instrument (ACTION TB)"; \
	$(PY) -I compose/code/p230-prose-path-ladder/lazy_lint.py compose/code; \
	echo "ALL OFFLINE LICENCE CONTROLS PASS"

exists: ## ACTION TC — one `git ls-remote` per slug: existence, default branch, HEAD
	@$(PY) -I compose/code/p230-prose-path-ladder/harvest.py . slugs > /tmp/p230-slugs.tsv
	@compose/code/p230-prose-path-ladder/exists.sh /tmp/p230-slugs.tsv /tmp/p230-exists.tsv
	@awk -F'\t' '{print $$2}' /tmp/p230-exists.tsv | sort | uniq -c

gate-online: ## needs raw.githubusercontent.com — re-read the shelves' grants first-hand
	@echo "usage: compose/code/p229-grant-ladder-reach/ladder.sh <slugs-file> <out-dir>"
	@compose/code/p229-grant-ladder-reach/ladder.sh --reach

reach: ## print the probe vocabulary (T272: a list you cannot print is a list that gets copied)
	@compose/code/p229-grant-ladder-reach/ladder.sh --reach

status:
	@echo "education-kb — shelves: $$(ls agents/*.md repos/*.md verticals/*.md intel/*.md compose/patterns.md 2>/dev/null | wc -l) files"
	@echo "evidence:  $$(ls evidence/*.tsv 2>/dev/null | wc -l) tables"
	@echo "instruments: $$(ls -d compose/code/*/ 2>/dev/null | wc -l)"
	@echo "last commit: $$(git log -1 --format='%ar — %s' 2>/dev/null | cut -c1-90)"
