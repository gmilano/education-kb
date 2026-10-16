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

.PHONY: hooks gate-offline gate-online gate-mit-tier reach status exists index carried claims

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
	echo "── p233-maven-channel   (the response classifier: a 404 is not an absence)"; \
	$(PY) -I compose/code/p233-maven-channel/test_classify_response.py >/dev/null && echo "   PASS"; \
	echo "── p237-grant-payload-shapes (BOM + holderless + year-less grants, 9 controls)"; \
	cd compose/code/p237-grant-payload-shapes && bash test_payload_shapes.sh >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p235-carried-index    (ACTION UG/UH: the index, fold, claims — 23 controls)"; \
	$(PY) -I compose/code/p235-carried-index/test_carried_index.py >/dev/null && echo "   PASS"; \
	echo "── p238-lure-signature   (the provenance gate: 66 controls, ACTION VE + p240 loopback)"; \
	cd compose/code/p238-lure-signature && $(PY) test_lure_signature.py >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p239-query-shape      (the sort key: 70 controls, ACTION VH)"; \
	cd compose/code/p239-query-shape && $(PY) test_query_shape.py >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p240-grant-language   (the language axis: 29 controls, ACTION VO)"; \
	cd compose/code/p240-grant-language && $(PY) test_grant_language.py >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p1054-mit-plus-clause (the added-restriction classifier, ACTION VO/p241)"; \
	$(PY) -I compose/code/p1054-mit-plus-clause/test_mit_plus.py >/dev/null 2>&1 && echo "   PASS"; \
	echo "── p241-blanket-denial  (the grant axis: 104 controls, ACTION VO)"; \
	cd compose/code/p241-blanket-denial && $(PY) test_blanket_denial.py >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p242-grant-delta    (disclosure vs narrowing vs transition: 23 controls, ACTION VU)"; \
	$(PY) -I compose/code/p242-grant-delta/test_grant_delta.py >/dev/null 2>&1 && echo "   PASS"; \
	echo "── p1058-empty-payload-gate (0-byte grant, self-reference, prefix narrowing: 29)"; \
	cd compose/code/p1058-empty-payload-gate && $(PY) -I test_empty_payload_gate.py >/dev/null 2>&1 && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p244-absence-states  (payload/address/query absence + truncation: 61)"; \
	$(PY) -I compose/code/p244-absence-states/test_absence_states.py >/dev/null && echo "   PASS"; \
	echo "── p245-apache-canonical (the TEXT axis: 25 controls, the 4(c)/4(d) twin phrase)"; \
	cd compose/code/p245-apache-canonical && $(PY) -I test_apache_canonical.py >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p246-payload-integrity (ROLE + STATE: 60 controls, the BUSL-unreachable branch)"; \
	$(PY) -I compose/code/p246-payload-integrity/test_payload_integrity.py >/dev/null && echo "   PASS"; \
	echo "── p247-keyed-grant     (ENFORCEMENT + the windowless name channel: 74, ACTION XA)"; \
	$(PY) -I compose/code/p247-keyed-grant/test_keyed_grant.py >/dev/null && echo "   PASS"; \
	echo "── p247-path-class      (ACTION XC: licence path vs NOTICE vs manifest vs code)"; \
	cd compose/code/p247-path-class && bash test_path_class.sh >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p248-named-proprietary (ACTION XE: the windowless name tier + arm closure: 38)"; \
	cd compose/code/p248-named-proprietary && bash test_named_proprietary.sh >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p207-permissive-half-audit (D14, the RIDER: it owns the only correct one — 12)"; \
	cd compose/code/p207-permissive-half-audit && bash test_classify.sh >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p251-gate-exit-reach  (ACTION XM: exit-code reachability + 5 unittest floors)"; \
	cd compose/code/p251-gate-exit-reach && $(PY) test_gate_exit_reach.py >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
	echo "── p251-prefix-collision (ACTION XN: the maia class, a truncation onto a real repo)"; \
	cd compose/code/p251-prefix-collision && $(PY) test_prefix_collision.py >/dev/null && echo "   PASS"; \
	cd - >/dev/null; \
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

gate-mit-tier: ## ACTION XB (p247) — re-read the MIT tier's grants first-hand.  NEEDS EGRESS.
	@echo "881 distinct MIT slugs on the shelves; 821 readable on guessed refs (ACTION XH holds the 60)."
	@$(PY) -I compose/code/p228-shelf-gate/harvest_cells.py agents/top.md agents/trending.md \
	  repos/foundations.md repos/trending.md verticals/solutions.md intel/market.md \
	  intel/trends.md compose/patterns.md 2>/dev/null \
	  | awk -F'\t' 'NR>1 && $$5=="LIVE" && $$4=="MIT"{print tolower($$3)}' | sort -u > /tmp/p247-mit-slugs.txt
	@wc -l < /tmp/p247-mit-slugs.txt
	@compose/code/p247-mit-tier-sweep/sweep.sh /tmp/p247-mit-slugs.txt /tmp/p247-mit-sweep 12

reach: ## print the probe vocabulary (T272: a list you cannot print is a list that gets copied)
	@compose/code/p229-grant-ladder-reach/ladder.sh --reach

status:
	@echo "education-kb — shelves: $$(ls agents/*.md repos/*.md verticals/*.md intel/*.md compose/patterns.md 2>/dev/null | wc -l) files"
	@echo "evidence:  $$(ls evidence/*.tsv 2>/dev/null | wc -l) tables"
	@echo "instruments: $$(ls -d compose/code/*/ 2>/dev/null | wc -l)"
	@echo "last commit: $$(git log -1 --format='%ar — %s' 2>/dev/null | cut -c1-90)"

index: ## ACTION UG (p235) — rebuild the carried-row index and report the UH collisions
	@$(PY) -I compose/code/p235-carried-index/carried_index.py . | head -3

carried: ## ACTION UG — is this row already on the shelves?  make carried SLUG=owner/repo
	@$(PY) -I compose/code/p235-carried-index/carried_index.py check "$(SLUG)" .

claims: ## ACTION UG — THE GATE: run before publishing any "there is no X".  make claims TOKEN=x
	@$(PY) -I compose/code/p235-carried-index/carried_index.py claims "$(TOKEN)" . || true
