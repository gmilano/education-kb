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

# 🔴 p253: `set -e` DOES NOT abort these steps, measured rather than read.  bash exempts a
# command that is not the LAST in an `&&` list from errexit, so `cd d && test.py && echo PASS`
# swallows a failing `test.py`: the step prints no `PASS`, the recipe continues, and
# `ALL OFFLINE LICENCE CONTROLS PASS` prints anyway with `exit 0`.  Reproduced in isolation.
# 🔵 This is why `ACTION XM` and `XR` could audit 26 suites for failure-capability and still
# miss it: they asked whether each SUITE can signal, never whether the GATE propagates — and
# p251/p252 both recorded `make` as not runnable from their session, so neither ran it.
# 🟢 Every step therefore carries an explicit `|| exit 1`, and the banner is unreachable
# unless all of them pass.  `compose/code/p253-gate-propagation/` pins this.
gate-offline: ## no network — safe in a hook, in CI, and in a sandbox without egress
	@set -e; \
	echo "── lib/license_family.sh  (the shared classifier, P237)"; \
	cd compose/code/lib && bash test_license_family.sh >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── lib/licence_path.sh    (the shared path predicate, P441)"; \
	cd compose/code/lib && bash test_licence_path.sh >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p222-ecosystem-bound-grammar  (five grammars, the bound)"; \
	cd compose/code/p222-ecosystem-bound-grammar && $(PY) test_bound_grammar.py >/dev/null 2>&1 && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p228-shelf-gate        (the five non-grant subjects, 30 tests)"; \
	cd compose/code/p228-shelf-gate && $(PY) test_shelf_gate.py >/dev/null 2>&1 && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p229-grant-ladder-reach (reach, foreign manifest, withdrawn cells, query key)"; \
	cd compose/code/p229-grant-ladder-reach && $(PY) test_grant_ladder_reach.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p230-prose-path-ladder (greedy slug, prose paths, the lazy-quantifier lint)"; \
	$(PY) -I compose/code/p230-prose-path-ladder/test_prose_path_ladder.py >/dev/null && echo "   PASS" || exit 1; \
	echo "── p233-maven-channel   (the response classifier: a 404 is not an absence)"; \
	$(PY) -I compose/code/p233-maven-channel/test_classify_response.py >/dev/null && echo "   PASS" || exit 1; \
	echo "── p237-grant-payload-shapes (BOM + holderless + year-less grants, 9 controls)"; \
	cd compose/code/p237-grant-payload-shapes && bash test_payload_shapes.sh >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p235-carried-index    (ACTION UG/UH: the index, fold, claims — 23 controls)"; \
	$(PY) -I compose/code/p235-carried-index/test_carried_index.py >/dev/null && echo "   PASS" || exit 1; \
	echo "── p238-lure-signature   (the provenance gate: 66 controls, ACTION VE + p240 loopback)"; \
	cd compose/code/p238-lure-signature && $(PY) test_lure_signature.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p239-query-shape      (the sort key: 70 controls, ACTION VH)"; \
	cd compose/code/p239-query-shape && $(PY) test_query_shape.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p240-grant-language   (the language axis: 29 controls, ACTION VO)"; \
	cd compose/code/p240-grant-language && $(PY) test_grant_language.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p1054-mit-plus-clause (the added-restriction classifier, ACTION VO/p241)"; \
	$(PY) -I compose/code/p1054-mit-plus-clause/test_mit_plus.py >/dev/null 2>&1 && echo "   PASS" || exit 1; \
	echo "── p241-blanket-denial  (the grant axis: 104 controls, ACTION VO)"; \
	cd compose/code/p241-blanket-denial && $(PY) test_blanket_denial.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p242-grant-delta    (disclosure vs narrowing vs transition: 23 controls, ACTION VU)"; \
	$(PY) -I compose/code/p242-grant-delta/test_grant_delta.py >/dev/null 2>&1 && echo "   PASS" || exit 1; \
	echo "── p1058-empty-payload-gate (0-byte grant, self-reference, prefix narrowing: 29)"; \
	cd compose/code/p1058-empty-payload-gate && $(PY) -I test_empty_payload_gate.py >/dev/null 2>&1 && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p244-absence-states  (payload/address/query absence + truncation: 61)"; \
	$(PY) -I compose/code/p244-absence-states/test_absence_states.py >/dev/null && echo "   PASS" || exit 1; \
	echo "── p245-apache-canonical (the TEXT axis: 25 controls, the 4(c)/4(d) twin phrase)"; \
	cd compose/code/p245-apache-canonical && $(PY) -I test_apache_canonical.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p246-payload-integrity (ROLE + STATE: 60 controls, the BUSL-unreachable branch)"; \
	$(PY) -I compose/code/p246-payload-integrity/test_payload_integrity.py >/dev/null && echo "   PASS" || exit 1; \
	echo "── p247-keyed-grant     (ENFORCEMENT + the windowless name channel: 74, ACTION XA)"; \
	$(PY) -I compose/code/p247-keyed-grant/test_keyed_grant.py >/dev/null && echo "   PASS" || exit 1; \
	echo "── p247-path-class      (ACTION XC: licence path vs NOTICE vs manifest vs code)"; \
	cd compose/code/p247-path-class && bash test_path_class.sh >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p248-named-proprietary (ACTION XE: the windowless name tier + arm closure: 38)"; \
	cd compose/code/p248-named-proprietary && bash test_named_proprietary.sh >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p207-permissive-half-audit (D14, the RIDER: it owns the only correct one — 12)"; \
	cd compose/code/p207-permissive-half-audit && bash test_classify.sh >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p251-gate-exit-reach  (ACTION XM: exit-code reachability + 5 unittest floors)"; \
	cd compose/code/p251-gate-exit-reach && $(PY) test_gate_exit_reach.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p251-prefix-collision (ACTION XN: the maia class, a truncation onto a real repo)"; \
	cd compose/code/p251-prefix-collision && $(PY) test_prefix_collision.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p252-ungated-floors   (ACTION XR: the 71 ungated silent-zero suites, pinned)"; \
	cd compose/code/p252-ungated-floors && $(PY) -I test_ungated_floors.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p252-ungated-floors   (ACTION XR: verify every pinned floor still holds)"; \
	cd compose/code/p252-ungated-floors && $(PY) -I ungated_floors.py --verify >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p253-captured-body-census (ACTION XY: the P834 capture sites, graded)"; \
	cd compose/code/p253-captured-body-census && $(PY) -I test_captured_body.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p253-captured-body-census (ACTION XY: verify every pinned site still holds)"; \
	cd compose/code/p253-captured-body-census && $(PY) -I captured_body.py --verify >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p253-settled-fact-regression (p253: a pass may not re-open a settled fact)"; \
	cd compose/code/p253-settled-fact-regression && $(PY) -I test_settled_fact.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p253-settled-fact-regression (p253: the shelves' CURRENT sections, verified)"; \
	cd compose/code/p253-settled-fact-regression && $(PY) -I settled_fact.py --verify >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p253-gate-propagation (p253: a failing step may not reach the banner)"; \
	cd compose/code/p253-gate-propagation && $(PY) -I test_gate_propagation.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p254-scoped-grant-reference (P1065: a POINTER to a licence is not a GRANT)"; \
	cd compose/code/p254-scoped-grant-reference && bash test_scoped_reference.sh >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p254-exit-status-reach (ACTION XZ: a contracted recipe line must be able to fail)"; \
	cd compose/code/p254-exit-status-reach && $(PY) -I test_exit_reach.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p254-exit-status-reach (ACTION XZ: the live Makefile's own contract, verified)"; \
	$(PY) -I compose/code/p254-exit-status-reach/exit_reach.py --verify Makefile >/dev/null && echo "   PASS" || exit 1; \
	echo "── p255-channel-reachability (ACTION YE: a refusal that does not BILL is not a budget)"; \
	cd compose/code/p255-channel-reachability && $(PY) -I test_channel_map.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── pass256-ladder-closure (p256: the ladder a pass TYPES vs the paths proven)"; \
	cd compose/code/pass256-ladder-closure && $(PY) -I test_ladder_closure.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── pass256-ladder-closure (p256: the LIVE ladder's closure, verified)"; \
	cd compose/code/pass256-ladder-closure && $(PY) -I ladder_closure.py --verify >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── pass257-restriction-scan (p257: the vocabulary runs on EVERY payload, not only MIT-shaped ones)"; \
	cd compose/code/pass257-restriction-scan && $(PY) -I test_restriction_scan.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── pass258-content-licence-family (p258: the CC class the gate could not name)"; \
	cd compose/code/pass258-content-licence-family && $(PY) test_content_licence.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── pass258-content-licence-family (p258: the LIVE shelves' CC census, verified)"; \
	cd compose/code/pass258-content-licence-family && $(PY) -I content_licence.py --census ../../.. >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── pass259-grant-location-class (p259: WHERE a grant was read, and what that licenses you to conclude)"; \
	cd compose/code/pass259-grant-location-class && $(PY) test_grant_location.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── pass260-ecosystem-manifest-tier (p260: REACH is not RUN; foreign/generated/pair guards)"; \
	cd compose/code/pass260-ecosystem-manifest-tier && $(PY) test_manifest_tier.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── pass261-current-state-tier-run (p261: ZD's current-state index, ZE's (path,row) coverage, the scoped reservation)"; \
	cd compose/code/pass261-current-state-tier-run && $(PY) test_current_state.py >/dev/null && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── lazy-quantifier lint over every instrument (ACTION TB)"; \
	$(PY) -I compose/code/p230-prose-path-ladder/lazy_lint.py compose/code || exit 1; \
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

# p254 (`ACTION YB`): the SUPPLY TEST, now with a status.  `CARRIED` exits 1, `NEW` exits 0,
# so `make carried SLUG=x && <publish the row>` is finally a correct sentence.  p252 ran this
# by hand and found 0 new; p253 ran it by hand and found the one new row in sixteen passes.
carried: ## ACTION UG — is this row already on the shelves?  make carried SLUG=owner/repo
	@$(PY) -I compose/code/p235-carried-index/carried_index.py check "$(SLUG)" .

# 🔴 p254 (`ACTION XZ`): this recipe ended in `|| true` for its whole life.  `carried_index.py
# claims` returns **1 exactly when the shelves ALREADY claim the token** — exit 1 IS the STOP
# signal and the entire purpose of the recipe — and `|| true` discarded it.  The verdict still
# printed, so a human reading the terminal was fine and `make claims TOKEN=x && publish` was
# not.  🔵 Same class as p253's deaf gate, one layer out: there the gate could not HEAR its
# controls; here the gate could not SPEAK.  Pinned by `compose/code/p254-exit-status-reach/`.
claims: ## ACTION UG — THE GATE: run before publishing any "there is no X".  make claims TOKEN=x
	@$(PY) -I compose/code/p235-carried-index/carried_index.py claims "$(TOKEN)" .
