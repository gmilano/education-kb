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
# p277: the enumeration suite reports WHICH control failed on stdout and exits 1.
# That report used to be redirected to /dev/null, so the gate could prove a failure
# and could not name it.  It is captured here and printed on failure instead.
GATE_LOG ?= /tmp/education-kb-gate-enumeration.log
BESPOKE_LOG ?= /tmp/education-kb-gate-bespoke-title.log
TABLE_LOG ?= /tmp/education-kb-gate-tables.log
IDENTITY_LOG ?= /tmp/education-kb-gate-identity.log
LADDER_LOG ?= /tmp/education-kb-gate-ladder.log
STORE_LOG ?= /tmp/education-kb-gate-evidence-store.log
README_LOG := $(shell mktemp)
ORACLE_LOG ?= /tmp/education-kb-gate-slug-oracle.log
PAYLOAD_LOG ?= /tmp/education-kb-gate-payload-pin.log
SHELF_LOG ?= /tmp/education-kb-gate-shelf-consistency.log
REGION_LOG ?= /tmp/education-kb-gate-region-headings.log
AFFERO_LOG ?= /tmp/education-kb-gate-affero-rung.log
FAMILY_LOG ?= /tmp/education-kb-gate-family-coverage.log
PERMISSIVE_LOG ?= /tmp/education-kb-gate-permissive-arm.log
TEMPLATE_LOG ?= /tmp/education-kb-gate-template-identity.log
UNTITLED_LOG ?= /tmp/education-kb-gate-untitled-payload.log

.PHONY: gate-untitled-payload untitled-arm gate-template-identity gate-permissive-arm permissive-arm risk-order gate-family-coverage family-coverage hooks gate-offline gate-online gate-mit-tier reach status exists index carried claims recount sweep gate-enumeration gate-tables gate-conflict gate-absence absence-census enumerate conflict-sweep gate-provenance provenance-census provenance-sweep gate-identity gate-identity-online gate-ladder-case ladder-audit gate-restatement gate-pin-grant gate-evidence-store gate-slug-oracle slug-probe gate-payload-pin gate-shelf-consistency gate-affero-rung delivery-audit affero-rung-census gate-bespoke-title bespoke-census

# 🔴 p300: `hooks` WAS A FAIL-FAST CHAIN, AND THAT MASKED SIX GATES FOR TWO PASSES.
# `gate-identity` went red at p298 on four findings that were its own false positives
# (a sibling cited in a description cell, harvested as a second recommendation).  make
# stops at the first failing prerequisite, so `gate-ladder-case`, `gate-readme-channel`,
# `gate-restatement`, `gate-pin-grant`, `gate-evidence-store` and `gate-slug-oracle` did
# not run AT ALL at p298 or p299 -- and nothing said so, because the output ended with a
# failure that looked like the whole story.  Measured at p300: all six were green, so the
# realised loss was zero and the EXPOSURE was six unrun gates for two passes.  The next
# masked gate will not be green.
#
# 🔵 The generalisable error: ORDERING A SET OF INDEPENDENT CHECKS AS A CHAIN.  These
# gates share no state and none is a precondition for another, so first-failure-stops
# buys nothing and silently sheds coverage.  `hooks` now runs EVERY gate, reports a
# per-gate verdict, and exits non-zero if any failed -- same exit-code contract, no
# masking.  A gate that cannot mask its siblings is the only kind whose green means
# anything.
HOOK_GATES = gate-offline recount gate-enumeration gate-tables gate-conflict \
             gate-absence gate-dates gate-provenance gate-identity gate-ladder-case \
             gate-readme-channel gate-restatement gate-pin-grant gate-evidence-store \
             gate-slug-oracle gate-payload-pin gate-shelf-consistency \
             gate-affero-rung gate-family-coverage gate-permissive-arm \
             gate-template-identity gate-untitled-payload gate-region-headings \
             gate-bespoke-title

# 🔴 p310: `p309` BUILT THE RIGHT MECHANISM AND GAVE IT A THREE-FAMILY CORPUS, THEN
# REPORTED `declared=11 CORRECT=11 DEFECT=0`.  One pass later the same ladder — five
# lines BELOW the rung p309 repaired — graded `aclascollege/aegis-graph`
# (CC-BY-NC-4.0, 19 347 B `41003d4a7474`) as `CC0-1.0`: a NonCommercial grant read as
# a public-domain dedication, which is the ONE error direction that puts unusable
# supply INTO a client deliverable.  p309's own defect ran the other way.
#
# 🔵 Both facts are true and the missing term is a DENOMINATOR.  A dynamic gate is a
# statement about the FAMILIES IN ITS CORPUS, and `DEFECT=0` reads as a statement
# about the classifier.  `family_coverage.py` derives the published family set from
# the shelves (22 families) and reports the uncovered remainder as exposure:
# p309 was green at 3/22 = 14 % coverage, and MIT (5 131 cells) and Apache-2.0
# (2 115) have STILL never been run through any arm.
#
# 🔴 And the remedy existed at `p124`, 186 passes earlier: `cc_version.resolve()` was
# BUILT on this exact defect and `ACTION AG` registered it as instance 3, labelled
# `DOCUMENT-TEXT`.  p309 concluded "import the discriminator, never restate it" and
# applied it to the family it was found in rather than to the mechanism.
gate-family-coverage: ## ACTION p309-R (items 1-2) — fixture coverage with a denominator, and no classifier may cross a commercial-use boundary
	@cd compose/code/p310-family-coverage && { $(PY) test_family_coverage.py > $(FAMILY_LOG) 2>&1 || { echo "🔴 p310-family-coverage FAILED — the suite's own report follows:" ; sed "s/^/   /" $(FAMILY_LOG) ; false ; } ; } && echo "── p310-family-coverage (59 controls: the refuted CC0 rung as a live negative control, p124's oracle, P250's two columns and its safe half, the three-valued POINTER class, and the four false positives this grader itself produced)" && echo "   PASS" || exit 1
	@cd compose/code/p310-family-coverage && $(PY) -I run_families.py || exit 1

family-coverage: ## p310 — the coverage census alone: which published families have no pinned payload
	@cd compose/code/p310-family-coverage && $(PY) -I family_coverage.py ../../.. || true

# 🔴 p311: `ACTION p310-R` item 1 — `MIT` (5 549 cells) and `Apache-2.0` (2 335) were the two
# most-published families on this base and NO dynamic arm had ever touched either: 7 884 cells,
# 61 % of every licence cell published here, resting on rungs never executed against a real
# payload of their own family.  🟢 THE ANSWER IS ZERO DEFECTS across 9 classifiers.
#
# 🔵 And the second finding is in the PAYLOADS, not the classifiers.  This base pins every
# payload as bytes + `sha256_12`, and `p310` certified seven CC0 rows partly on *"six at the
# legalcode's exact 7 048 B"*.  Byte length and sha answer *"is this the same FILE?"*; they were
# read as answering *"is this the same GRANT?"*.  Both halves of that are refuted here on real
# payloads: the Apache pair differs by ONE LEADING NEWLINE (identical grant, unrelated shas),
# and the MIT pair's whole 34-byte delta is the HOLDER STRING.
gate-permissive-arm: ## p311 — ACTION p310-R item 1: the two most-published families, run at last, plus the payload-identity oracle
	@cd compose/code/p311-permissive-family-arm && { $(PY) -I test_p311.py > $(PERMISSIVE_LOG) 2>&1 || { echo "🔴 p311-permissive-family-arm FAILED — the suite's own report follows:" ; sed "s/^/   /" $(PERMISSIVE_LOG) ; false ; } ; } && echo "── p311-permissive-family-arm (32 controls: the four pins against the shas p310 probed, the one-leading-newline and holder-string negative controls, the refuted holder pattern kept live, the census discovery, and the two orderings' disagreement)" && echo "   PASS" || exit 1
	@cd compose/code/p311-permissive-family-arm && $(PY) -I run_permissive.py || exit 1

permissive-arm: ## p311 — the dynamic arm alone, on MIT and Apache-2.0
	@cd compose/code/p311-permissive-family-arm && $(PY) -I run_permissive.py || true

risk-order: ## p311 — the fixture queue on BOTH axes: descending cells, and what a wrong answer COSTS
	@cd compose/code/p311-permissive-family-arm && $(PY) -I risk_order.py ../../.. || true

gate-template-identity: ## p312 — ACTION p310-R item 1: MIT and Apache-2.0 identified by TEMPLATE, never by a byte band
	@cd compose/code/p312-template-identity && { $(PY) test_template_identity.py > $(TEMPLATE_LOG) 2>&1 || { echo "🔴 p312-template-identity FAILED — the suite's own report follows:" ; sed "s/^/   /" $(TEMPLATE_LOG) ; false ; } ; } && echo "── p312-template-identity (80 controls: the refuted MIT band and this module's own three wrong rungs as live negative controls, the 7-payload template collapse at a constant of 1038, Apache's prefix bimodality, and the UNKNOWN-TEMPLATE abstention contract)" && echo "   PASS" || exit 1
	@cd compose/code/p312-template-identity && $(PY) -I template_identity.py || exit 1

# 🔴 p314: EVERY ARM ON THIS BASE HAS BEEN KEYED ON A LICENCE FAMILY.  This one is keyed
# on a payload SHAPE and holds the family constant, because `p313` found a complete,
# valid `BSD-3-Clause` grant carrying NO TITLE LINE and ZERO `BSD` tokens — and could
# not run a single classifier against it, the code channel being refused in that session.
# 🔵 The shape is not rare and it is not confined to BSD: `crewAIInc/crewAI` serves the
# verbatim MIT grant with no title line and no `MIT` token, on the family that holds more
# than a third of every licence cell this base publishes.
# 🟢 Measured here: four declared classifiers read the family when the first line names it
# and ABSTAIN on the same family's grant when it does not; several others read the untitled
# payload correctly off its CLAUSE STRUCTURE, which refutes `p313`'s inference that no
# channel could.  The discriminator is whether an instrument kept a BODY FALLBACK under
# its title ladder — not the family, and not the ladder.
gate-untitled-payload: ## p314 — ACTION p313-R item 5 + items 2a and 4: the untitled-grant class, on MIT and BSD-3-Clause
	@cd compose/code/p314-untitled-payload-arm && { $(PY) test_p314.py > $(UNTITLED_LOG) 2>&1 || { echo "🔴 p314-untitled-payload FAILED — the suite's own report follows:" ; sed "s/^/   /" $(UNTITLED_LOG) ; false ; } ; } && echo "── p314-untitled-payload (19 controls: both BSD shapes pinned per item 5, the untitled-MIT headline, the substring form matching by accident inside «permit» as a live false friend, step 0c's scheme repair with its true-negative and URL-eraser bounds, and item 4's notice-vs-grant class over all four of p313's noncommercial payloads)" && echo "   PASS" || exit 1
	@cd compose/code/p314-untitled-payload-arm && $(PY) -I run_untitled.py || exit 1

untitled-arm: ## p314 — the dynamic arm alone: titled vs untitled, family held constant
	@cd compose/code/p314-untitled-payload-arm && $(PY) -I run_untitled.py

hooks: ## the standing check: every licence instrument's OFFLINE controls, T37's re-count, p275's enumeration gate, p277's table-structure gate, p278's channel-conflict gate, p279's absence-claims gate, p223's date gate made standing, plus p280's package-provenance channel, plus p283's per-pair identity check and its ladder-case audit, plus p288's README third channel, plus p289's restatement-vs-authority grade on the curriculum layer, plus p291's submodule pin-grant axis, plus p292's decision-evidence-store controls and its recipe-citation arm, plus p293's calibrated slug-existence oracle, and p300's no-masking runner
	@rc=0; red=""; green=0; \
	for g in $(HOOK_GATES); do \
	  if $(MAKE) --no-print-directory $$g; then green=$$((green+1)); \
	  else rc=1; red="$$red $$g"; echo "🔴 $$g FAILED — continuing, so no gate can mask its siblings (p300)"; fi; \
	done; \
	echo ""; \
	echo "── p300 hooks runner — every gate ran, none masked"; \
	n=$$(echo $(HOOK_GATES) | wc -w); \
	if [ $$rc -eq 0 ]; then echo "🟢 PASS — $$green/$$n gates green."; \
	else echo "🔴 FAIL — $$green/$$n gates green; RED:$$red"; fi; \
	exit $$rc

# 🟢 p275: a negative licence verdict is only a finding if the TREE WAS ENUMERATED.
# p274 ranked "re-probe every negative verdict with ls-remote as a positive control" first.
# The control passed on all 13 slugs -- and exposed that the LADDER, not the slug, is the
# defect: os4ed/openSIS-Classic's grant sits at docs/License.txt (GPL-2.0, 17 286 B) and
# ls1intum/Athena declares MIT in 12 of 14 manifests, while the ladder probed the one
# manifest that is silent.  Both false negatives were structurally guaranteed.  No network.
gate-enumeration: ## ACTION p275 — no shelf may assert an absent grant that an enumeration refutes
	@cd compose/code/pass275-grant-enumeration && { $(PY) test_enumeration_gate.py > $(GATE_LOG) 2>&1 || { echo "🔴 pass275-grant-enumeration FAILED — the suite's own report follows (p277: this went to /dev/null for three passes, so no pass could name the failing control):" ; sed "s/^/   /" $(GATE_LOG) ; false ; } ; } && echo "── pass275-grant-enumeration (64 controls incl. the C3 positive control; vendored/icon/source paths, two-subject lines, p285 examples/IDE/html-xml exclusions)" && echo "   PASS" || exit 1
	@cd compose/code/pass275-grant-enumeration && $(PY) -I enumeration_gate.py --root ../../.. || exit 1

# 🟢 p277 (`ACTION AB`): p276 found a `|---|` separator sitting BELOW its table's first data
# row, so p274's own recovered `gegok12` row rendered as part of the HEADER -- a real row,
# published, invisible -- and recorded: "No gate on this base reads table structure."
# 🔴 p277 then found a LIVE second instance in another file and another shape: a stray BLANK
# LINE at verticals/solutions.md:50 promoted `Koha` (a real GPL-3.0 row) into a header and
# orphaned every row below it.  Two shapes, one failure mode: a row that is published and
# does not render as a row.  No network.
# 🔵 The suite's output is CAPTURED and printed on failure -- p277's own finding about
# gate-enumeration was that `>/dev/null` discards the only thing a failing gate has to say.
gate-tables: ## ACTION p277 — no shelf may publish a data row that renders as a table header
	@cd compose/code/p277-table-structure && { $(PY) test_table_structure.py > $(TABLE_LOG) 2>&1 || { echo "🔴 p277-table-structure FAILED — the suite's own report follows:" ; sed "s/^/   /" $(TABLE_LOG) ; false ; } ; } && echo "── p277-table-structure (15 controls: the empty-header, cross-table-blank and pipe-art shapes)" && echo "   PASS" || exit 1
	@$(PY) -I compose/code/p277-table-structure/table_structure.py . || exit 1

# 🟢 p278 (`p277`'s declared item 1): the CONFLICT class — which TURNED OUT TO ALREADY EXIST.
# `p277` ranked "build the payload-vs-metadata CONFLICT class" FIRST at zero searches. `p121`
# had built it on 2026-10-11: 249 addresses, 161 manifests, 104 declaring, 10 contradictions
# = 9.6 %, published in repos/trending.md with a four-value DIRECTION axis. And the instance
# `p277` reported as NEW -- open-tutor-ai-CE, BSD payload vs MIT pyproject -- is ROW 8 of that
# table, with the identical verdict.
# 🔵 `make claims TOKEN=conflict` returns `ALREADY CLAIMED … STOP` over 26 cells in
# repos/trending.md and exits 1. The gate for this error existed and was not run.
# 🟢 So what p278 owes is the half p121 never built: p121's census was a ONE-OFF, by hand, at
# one moment, with its verdicts TYPED per row. This gate re-derives every one of them from
# its own family cells through the shared classifier, so a typed verdict cannot drift from
# the evidence beside it. No network.
GATE_CONFLICT_LOG ?= /tmp/education-kb-gate-conflict.log

gate-conflict: ## ACTION p278 — no typed CONFLICT verdict may disagree with its own family cells
	@cd compose/code/p278-channel-conflict && { $(PY) -I test_direction.py > $(GATE_CONFLICT_LOG) 2>&1 || { echo "🔴 p278-channel-conflict/direction FAILED — the suite's own report follows:" ; sed "s/^/   /" $(GATE_CONFLICT_LOG) ; false ; } ; } && echo "── p278-channel-conflict/direction (p121's ten reproduced + the Commons-Clause arm)" && echo "   PASS" || exit 1
	@cd compose/code/p278-channel-conflict && { $(PY) -I test_conflict_gate.py >> $(GATE_CONFLICT_LOG) 2>&1 || { echo "🔴 p278-channel-conflict/gate-parsing FAILED — report follows:" ; sed "s/^/   /" $(GATE_CONFLICT_LOG) ; false ; } ; } && echo "── p278-channel-conflict/gate-parsing (the hyphen regression, NC-before-CC-BY ordering)" && echo "   PASS" || exit 1
	@$(PY) -I compose/code/p278-channel-conflict/conflict_gate.py --root . || exit 1

# 🟢 p279 (`p278`'s declared item 1): MAKE `make claims` A STEP, NOT AN INSTRUCTION.
# `p278`'s headline was a gate that EXISTS and WAS NOT RUN: `p277` published "no class at
# all for CONFLICT" over a class `p121` had built 157 passes earlier and shelved in 26 cells
# of repos/trending.md, and `make claims TOKEN=conflict` would have said so and exited 1.
# 🔵 `p278` registered the remedy as "the next pass should not be able to publish an absence
# without it having run" -- so the index is READ BY A GATE now, and the Makefile help string
# that documented it as "THE GATE" stops being the only thing that enforces it.
# 🔴 Two of its own predicates were wrong before it was wired in, both measured on the real
# README rather than read: it reported `p278`'s forensic QUOTATION of `p277` as a fresh
# assertion, and the first fix for that computed quote parity PER LINE, which fails on a
# hard-wrapped quote -- `p278`'s own reflow-brittleness class, one layer out.  Both are
# controls now.  No network.
ABSENCE_LOG ?= /tmp/education-kb-gate-absence.log

gate-absence: ## ACTION p279 — no pass may publish an absence the index already refutes
	@cd compose/code/p279-absence-claims && { $(PY) -I test_absence_claims.py > $(ABSENCE_LOG) 2>&1 || { echo "🔴 p279-absence-claims FAILED — the suite's own report follows:" ; sed "s/^/   /" $(ABSENCE_LOG) ; false ; } ; } && echo "── p279-absence-claims (Control Zero is p277's real sentence; the quoted and wrapped shapes)" && echo "   PASS" || exit 1
	@$(PY) -I compose/code/p279-absence-claims/absence_claims.py --root . || exit 1

absence-census: ## ACTION p279 — the whole-corpus arm: a measurement, never a failure
	@$(PY) -I compose/code/p279-absence-claims/absence_claims.py --root . --census

# 🔴 p279: `p223`'s self-claim date gate WAS NEVER WIRED IN.  It passes its controls, it
# scans the live corpus clean, and `grep -c p223 Makefile` returned **0** -- so the one
# instrument this base owns for its most-repeated factual error has been a one-off for 56
# passes.  That is the Makefile header's own opening class ("a working gate that stayed a
# one-off because it could not be invoked from the place a hook runs"), still live.
# 🟢 Standing now.  The stale claim it guards -- *"AI Act education high-risk from August
# 2026"* -- is wrong by fifteen months in the expensive direction: it tells an EMEA client
# they are bound now.  Annex III point 3 applies `2027-12-02`; `2026-08-02` is Article 50
# transparency and IS live.  No network.
DATES_LOG ?= /tmp/education-kb-gate-dates.log

gate-region-headings: ## p338 — ACTION ZP: p383's region-heading contract, WIRED.  The gate existed with a passing suite from p383 to p337 and was in no target, so `make hooks` never judged this file's region structure at all.
	@cd compose/code/p383-region-heading-gate && { $(PY) test_check_headings.py > $(REGION_LOG) 2>&1 || { echo "🔴 p383-region-heading-gate FAILED — the suite's own report follows:" ; sed "s/^/   /" $(REGION_LOG) ; false ; } ; } && echo "── p383-region-heading-gate (11 controls: MULTIPLE-BLOCKS, OUT-OF-VOCAB, MISSING-REGION, LATAM-ONLY, P541 no-input refusal)" && echo "   PASS" || exit 1
	@$(PY) -I compose/code/p383-region-heading-gate/check_headings.py intel/market.md || exit 1

# 🟢 p341 — ACTION T29: the bespoke-instrument census, WIRED.  `p340` recorded the
# question as unmeasured; the answer is 10 of 208 BESPOKE-TITLED, 16 of 208 needing a
# human, and every one already labelled correctly on the shelves.  The gate exists to
# keep the two classes `p314` paid to separate — UNTITLED (a stock grant with no title)
# and BESPOKE-TITLED (an instrument naming itself) — from fusing in a later pass, and to
# pin that `p312`'s UNKNOWN-TEMPLATE must never be read as "bespoke".  No network.
gate-bespoke-title: ## p341 — ACTION T29: a bespoke instrument is not a stock text, and UNKNOWN-TEMPLATE is not bespoke
	@cd compose/code/p341-bespoke-instrument-census && { $(PY) -I test_bespoke_census.py > $(BESPOKE_LOG) 2>&1 || { echo "🔴 p341-bespoke-instrument-census FAILED — the suite's own report follows:" ; sed "s/^/   /" $(BESPOKE_LOG) ; false ; } ; } && echo "── p341-bespoke-instrument-census (34 controls: title-form totality, the UNTITLED/BESPOKE separation, the p312 non-detector, the title-shape repair)" && echo "   PASS" || exit 1

bespoke-census: ## p341 — grade payload files offline: make bespoke-census PAYLOADS="a b"
	@$(PY) -I compose/code/p341-bespoke-instrument-census/bespoke_census.py $(PAYLOADS)

gate-dates: ## ACTION p279 — the KB may not ASSERT a date it has already refuted
	@cd compose/code/p223-selfclaim-date-gate && { $(PY) -I gate.py --self-test > $(DATES_LOG) 2>&1 || { echo "🔴 p223-selfclaim-date-gate FAILED — the suite's own report follows:" ; sed "s/^/   /" $(DATES_LOG) ; false ; } ; } && echo "── p223-selfclaim-date-gate (15 controls: ASSERTED / ATTRIBUTED / QUOTED / CORRECTED)" && echo "   PASS" || exit 1
	@$(PY) -I compose/code/p223-selfclaim-date-gate/gate.py . || exit 1


# 🟢 p280 (`p279`'s declared items 1 and 2).
# ITEM 1 asked for "a KNOWN-THIRD-PARTY NAME channel ... this base has no such list".
# 🔴 The remedy as registered needed a list this base would have had to invent, and a name
# vocabulary can only reject the projects somebody enumerated -- `p279`'s own sentence about
# its path vocabulary, one layer out.  The residual it named,
# `Open-TutorAi/open-tutor-ai-CE  ui/static/pyodide/package.json`, DECLARES ITS OWN
# PROVENANCE: `"repository": "https://github.com/pyodide/pyodide"`, `"homepage"` the same.
# 🔵 And both halves of that channel were already on the shelf --
# `lib/package_repo.sh::normalise_repo_url` (pass 75) and `p436-fork-hypothesis` (pass 24,
# with the measured warning that a differing declaration has three innocent causes) -- so
# the instrument imports them instead of writing a third parser.
# ITEM 2: four `T229-M2` controls named real repositories and asserted payloads they do not
# serve.  The fixtures are captured now, with `slug/ref/head_sha/sha256/date`, and
# `--verify` keeps them captured.  No network.
PROV_LOG ?= /tmp/education-kb-gate-provenance.log

gate-provenance: ## ACTION p280 — a vendored manifest is identified by what it DECLARES, not by a list
	@cd compose/code/pass280-package-provenance && { $(PY) -I test_provenance.py > $(PROV_LOG) 2>&1 || { echo "🔴 pass280-package-provenance FAILED — the suite's own report follows:" ; sed "s/^/   /" $(PROV_LOG) ; false ; } ; } && echo "── pass280-package-provenance (31 controls: the residual p279 called unreachable, and the workspace packages that must NOT be rejected)" && echo "   PASS" || exit 1
	@$(PY) -I compose/code/pass280-package-provenance/invented_payload_census.py --verify || exit 1

provenance-census: ## ACTION p280 — which controls name a real repo and assert bytes nobody read?
	@$(PY) -I compose/code/pass280-package-provenance/invented_payload_census.py --census

# 🟢 p283 (`p282`'s declared item 1): THE PER-PAIR IDENTITY CHECK.
# 🔴 `p282` found `agents/top.md` recommending ONE repository as TWO build-on rows
# (`ls1intum/Iris` == `ls1intum/Pyris`: same HEAD, same 245 refs, same root tree, same
# 1 088-byte MIT payload) and six recipes in compose/patterns.md composing the two.  Every
# licence instrument was right about the row it measured: DUPLICATION IS A RELATION BETWEEN
# ROWS, and `recount` matched 27 rows to 27 because 27 rows is what the file has.
# 🔴 `p282` then proved the remedy BY HAND and left it out of this file — the failure mode
# this Makefile's own header opens with, "a working gate that stayed a one-off".
# 🔵 The OFFLINE half reads the shelved alias ledger and is in `hooks`; the ONLINE half is
# one `ls-remote` per address and stays out, per this file's standing convention.
# 🟢 It found a live residue on its first run: repos/foundations.md:66 still presented Iris
# and Pyris as two distinct MIT subsystems inside ONE cell.  p282 corrected three files and
# missed that one.
gate-readme-channel: ## ACTION p288 — a README-only grant claim or reservation is not "no channel"
	@cd compose/code/p288-readme-channel && { $(PY) -I test_readme_claim.py > $(README_LOG) 2>&1 || { echo "🔴 p288-readme-channel FAILED — the suite's own report follows:" ; sed "s/^/   /" $(README_LOG) ; false ; } ; } && echo "── p288-readme-channel (32 controls: the lowercase rung, the MIT-RAISE collision arm, the postfix/markdown-link claim, reservation-outranks)" && echo "   PASS" || exit 1

RESTATEMENT_LOG := $(shell mktemp)

# 🟢 p289: `p742` asks whether a licence file carries a GRANT BODY or only a POINTER.  A
# payload can carry operative terms and still be the LICENSEE'S RESTATEMENT of a licence
# whose authoritative text lives on a third-party host -- which is where every public-sector
# CURRICULUM grant lives (OGL v3.0, the CC suite, ministry terms).  Both grade GRANTED under
# p742; only one can be verified from the clone.  Oak's curriculum ontology publishes the
# National Curriculum for England under TWO restated payloads, and both of them require a
# DIFFERENT attribution string in their summary block from the one they prescribe in their
# terms.  No network: the fixtures are the payloads, quoted verbatim with their sha256s.
gate-restatement: ## ACTION p289 — a restatement of an unreachable authority is not a verified grant
	@cd compose/code/p289-restatement-authority && { $(PY) -I test_restatement.py > $(RESTATEMENT_LOG) 2>&1 || { echo "🔴 p289-restatement-authority FAILED — the suite's own report follows:" ; sed "s/^/   /" $(RESTATEMENT_LOG) ; false ; } ; } && echo "── p289-restatement-authority (40 controls: the OGL restatement pair, the MIT collision arm, the CC generality arm, posture keyed to MEASURED reachability)" && echo "   PASS" || exit 1

PIN_GRANT_LOG ?= /tmp/education-kb-gate-pin-grant.log

# 🟢 p291 (`p290`'s ranked item 2): `ACTION p290` wrote the submodule-boundary rule in PROSE
# and an evidence table, and recorded that until it is a gate, "a later pass can publish a
# superproject's grant as covering its submodules, which is the exact defect this pass found."
# This is that gate — and it found the defect LIVE on its first run, in a vendor-estate
# listing that counted the superproject among `9/9 MIT` repositories.
# 🔴 It also CORRECTS p290's rule: the payload is readable AT THE PINNED SHA over
# `raw.githubusercontent.com`, so `HEAD == pin` is not a condition of verification and a
# GRANTED verdict resting on a read at HEAD is rejected (control `C7`).  No network.
gate-pin-grant: ## ACTION p291 — a submodule grant is verified AT THE PIN, and no shelf may cite a superproject without the boundary
	@cd compose/code/p291-submodule-pin-grant && { $(PY) test_pin_grant.py > $(PIN_GRANT_LOG) 2>&1 || { echo "🔴 p291-submodule-pin-grant FAILED — the suite's own report follows:" ; sed "s/^/   /" $(PIN_GRANT_LOG) ; false ; } ; } && echo "── p291-submodule-pin-grant (31 controls: the read-at-HEAD rejection, the 7-submodule census, block-scoped shelf claims, append-only live-section scope)" && echo "   PASS" || exit 1
	@$(PY) -I compose/code/p291-submodule-pin-grant/pin_grant.py --root . || exit 1

# 🟢 `ACTION p292` (p291's ranked item 1) — THE EVIDENCE STORE, BUILT.  `P45`-`P48` each
# terminate in "an append-only record of who decided what, shown what, under which rubric
# version", each said "you build it", and for four passes nothing here supplied it.
# 🔴 Building it refuted the backlog entry that asked for it: p291 said FOUR recipes need the
# identical component; the shelves carry TWO.  `P46` needs an intervention log and `P47` a
# deadline-and-evidence layer — adjacent components, not this one.  "One build" sounded like
# one thing, so it was costed as one thing and never started.  Arm `S2` makes that overclaim
# standing and fails p291's own sentence.
# 🔵 The suite is OFFLINE, so it belongs in `hooks`.  Control `C18` asserts the honest limit:
# a full rewrite of the file verifies CLEAN.  The chain is tamper-EVIDENT, not tamper-proof,
# and what closes the gap is anchoring `head()` outside the writer's reach.
gate-evidence-store: ## ACTION p292 — the decision record's own controls, and no recipe may depend on a component it does not locate
	@cd compose/code/p292-decision-evidence-store && { $(PY) test_decision_store.py > $(STORE_LOG) 2>&1 || { echo "🔴 p292-decision-evidence-store FAILED — the suite's own report follows:" ; sed "s/^/   /" $(STORE_LOG) ; false ; } ; } && echo "── p292-decision-evidence-store (106 controls: the agent-as-decider refusal, the shown-digest binding, the tamper-evident limit asserted as C18, and S2's recipe-count overclaim)" && echo "   PASS" || exit 1
	@$(PY) -I compose/code/p292-decision-evidence-store/decision_store.py --root . || exit 1

# 🟢 p293 (`p292`'s ranked item 1, and the method half that outlives the finding):
# IS A GUESSED SLUG A REPOSITORY?  `p292` probed four guessed `tokenaii/*` slugs, got an
# anonymous credential prompt on each, and recorded the result as "INCONCLUSIVE and not a
# negative".  🔴 Measured against a known-real and a known-fake control in the same session,
# that prompt DISCRIMINATES -- it is this channel's answer for "no repository I will serve
# you", and a different string from "I could not reach the host".  So three of those four
# probes were real negatives thrown away as noise.
# 🔴 THE BOUND IS A CONTROL: the same prompt answers for a PRIVATE repository, and nothing in
# this channel separates the two.  `C9` asserts that a bare `ABSENT` is not in the vocabulary.
# 🔵 The suite is OFFLINE -- every fixture is a recorded payload from p293's live probes -- so
# it belongs in `hooks`.  The ONLINE half stays out, and calibrates before it reports.
gate-slug-oracle: ## ACTION p293 — a credential prompt is a MEASUREMENT, not an inconclusive result
	@cd compose/code/p293-slug-existence-oracle && { $(PY) test_slug_oracle.py > $(ORACLE_LOG) 2>&1 || { echo "🔴 p293-slug-existence-oracle FAILED — the suite's own report follows:" ; sed "s/^/   /" $(ORACLE_LOG) ; false ; } ; } && echo "── p293-slug-existence-oracle (45 controls: p292's four discarded probes re-adjudicated, the ABSENT-OR-PRIVATE bound as C9-C11, transport-before-refusal, and the two defective controls this suite's own first draft shipped)" && echo "   PASS" || exit 1

# 🟢 p307 — `ACTION p305-R` item 1, outstanding for two passes because `make` could not be
# run, is DISCHARGED here: the permission-clause test is now a STANDING control rather than
# a thing each pass re-invents.  Nine controls, offline, and every one of them is a defect
# this instrument was actually caught on before publication: the line-wrapped Apache clause,
# GPL-2.0 recommending the Lesser licence in its own body, AGPL-3.0's title containing
# GPL-3.0's, BSD-3's discriminator sitting behind BSD-2's shared sentence, p305's reserved
# grant that closes with MIT's warranty paragraph, and p306's two pointer classes.
gate-payload-pin: ## p307 — the three-valued grant classifier (GRANT / POINTER / RESERVED), 9 offline controls
	@cd compose/code/p307-payload-pin && { $(PY) test_probe_p307.py > $(PAYLOAD_LOG) 2>&1 || { echo "🔴 p307-payload-pin FAILED — the suite's own report follows:" ; sed "s/^/   /" $(PAYLOAD_LOG) ; false ; } ; } && echo "── p307-payload-pin (9 controls: the wrapped Apache clause, GPL-2.0-not-LGPL, GPL-3.0-not-AGPL-3.0, BSD-3-not-BSD-2, p305's reserved grant, p306's two pointer classes)" && echo "   PASS" || exit 1

gate-shelf-consistency: ## p308 — ACTION p307-R item 1: no slug may carry disagreeing licence cells across the live shelves
	@cd compose/code/p308-shelf-consistency && { $(PY) -I test_shelf_consistency.py > $(SHELF_LOG) 2>&1 || { echo "🔴 p308-shelf-consistency/controls FAILED — the suite's own report follows:" ; sed "s/^/   /" $(SHELF_LOG) ; false ; } ; } && echo "── p308-shelf-consistency (52 controls: AGPL≠GPL, correction tables, retractions, comparators, possessives, quoted claims, dual grants, paired rows, scoped absences)" && echo "   PASS" || exit 1
	@{ $(PY) -I compose/code/p308-shelf-consistency/shelf_consistency.py . > $(SHELF_LOG) 2>&1 || { echo "🔴 p308-shelf-consistency/live FAILED — the disagreeing cells follow:" ; sed "s/^/   /" $(SHELF_LOG) ; false ; } ; } && echo "── p308-shelf-consistency (the live shelves, compared to EACH OTHER)" && echo "   PASS" || exit 1

shelf-census: ## p308 — where the DATED shelves disagree with the live answer.  A backlog, never a failure.
	@$(PY) -I compose/code/p308-shelf-consistency/shelf_consistency.py . --census || true

# 🔴 ONLINE half — one `git ls-remote` per slug, and it CALIBRATES FIRST.  OUT of `hooks`.
# An uncalibrated read of this channel is exactly what produced p292's "inconclusive" row, so
# a control-pair failure reports NO verdict rather than a guess.
slug-probe: ## ACTION p293 — is it a repository?  make slug-probe SLUGS="owner/a owner/b"
	@test -n "$(SLUGS)" || { echo 'usage: make slug-probe SLUGS="owner/name owner/other"'; exit 2; }
	@$(PY) -I compose/code/p293-slug-existence-oracle/slug_oracle.py --online $(SLUGS) --out evidence/p293-slug-oracle-$$(date +%F).tsv

gate-identity: ## ACTION p283 — no shelf may recommend one repository under two live rows
	@cd compose/code/p283-repo-identity && { $(PY) test_identity_gate.py > $(IDENTITY_LOG) 2>&1 || { echo "🔴 p283-repo-identity FAILED — the suite's own report follows:" ; sed "s/^/   /" $(IDENTITY_LOG) ; false ; } ; } && echo "── p283-repo-identity (17 controls: withdrawn-in-place, the cross-table index, both halves in one cell, plus p300's subject scope — the description-cell false positive, the cell-1 overfit guard and the preserved alias arm)" && echo "   PASS" || exit 1
	@$(PY) -I compose/code/p283-repo-identity/identity_gate.py --root . || exit 1

# 🟢 p283 (`p282`'s declared item 2): CASE-CLOSE EVERY PATH LADDER, NOT JUST THE LICENCE ONE.
# 🔴 `P1057` (p189) established that raw.githubusercontent.com is CASE-SENSITIVE and that a
# one-spelling path list "has not looked for the file; it has looked for one spelling of it".
# `pass256-ladder-closure` keeps the LICENCE ladder closed against p229's TIER_A — and
# `p282` found `README.MD` on ls1intum/Pyris after `p268` published "neither repository
# serves a README" off a four-rung ladder with no uppercase extension in it.
# 🔵 Measured here, 2026-10-18: of 580 ladders in 332 instruments only 20 are CASE-CLOSED.
# By family, the share carrying ANY uppercase extension is licence 11.1 %, copying 15.4 %,
# readme 5.3 %, NOTICE 0.0 % — p1057's fix reached the family it was built for and no other.
# 🔵 The census is a BACKLOG, printed and not failed, exactly as gate-enumeration treats its
# QUEUE rows.  The controls DO fail: they pin the two overclaims this instrument's own first
# draft made (a distant `.lower()` read as immunity; a four-rung ladder called "single").
# 🔴 Registered, not built: a RATCHET over these counts.  Stated so it is not mistaken for done.
gate-ladder-case: ## ACTION p283 — which path ladders can find an uppercase extension?
	@cd compose/code/p283-ladder-case-audit && { $(PY) test_ladder_case.py > $(LADDER_LOG) 2>&1 || { echo "🔴 p283-ladder-case-audit FAILED — the suite's own report follows:" ; sed "s/^/   /" $(LADDER_LOG) ; false ; } ; } && echo "── p283-ladder-case-audit (29 controls: the distant-fold and multi-rung overclaims, p284's generator verdict, p286's COMMENT-ONLY, shell-generator, method-attribute and alternation arms, p288's IMPORTED-LADDER arm with its overclaim guard, and the RATCHET)" && echo "   PASS" || exit 1
	@$(PY) -I compose/code/p283-ladder-case-audit/ladder_case.py --root . | tail -2

ladder-audit: ## ACTION p283 — the full per-ladder table.  make ladder-audit FAMILY=readme
	@$(PY) -I compose/code/p283-ladder-case-audit/ladder_case.py --root . $(if $(FAMILY),--family $(FAMILY),) --out evidence/ladder-case-audit-$$(date +%F).tsv

# 🔴 ONLINE half — one `git ls-remote` per live build-on address.  OUT of `hooks`.
# A HEAD collision is a FINDING, not a verdict: two distinct forks share a HEAD on the day
# one is forked from the other.  Adjudicate, then shelve the pair in `aliases.tsv`.
gate-identity-online: ## ACTION p283 — ls-remote every address; equal HEAD == one repository
	@$(PY) -I compose/code/p283-repo-identity/identity_gate.py --root . --online --out evidence/repo-identity-$$(date +%%F).tsv

# 🔴 ONLINE half — needs a blobless clone + raw.githubusercontent.com.  OUT of `hooks`.
provenance-sweep: ## ACTION p280 — grade every manifest in a slug list: make provenance-sweep SLUGS=f
	@test -n "$(SLUGS)" || { echo "usage: make provenance-sweep SLUGS=path/to/slugs.txt"; exit 2; }
	@compose/code/pass280-package-provenance/measure.sh "$(CURDIR)/$(SLUGS)"

# 🔴 ONLINE-ADJACENT half (`ACTION SH`, registered since p226): the same table, run against
# a file of INBOUND research text rather than the KB's own prose.  Takes a file, so it stays
# out of `hooks`; exit 1 is `make claims`'s STOP polarity.
inbound-claims: ## ACTION SH — run the refuted-claims table over a research file BEFORE writing it up
	@test -n "$(FILE)" || { echo "usage: make inbound-claims FILE=evidence/....txt"; exit 2; }
	@$(PY) -I compose/code/p223-selfclaim-date-gate/gate.py --inbound "$(FILE)"

# 🔴 ONLINE half — needs raw.githubusercontent.com + git ls-remote.  OUT of `hooks`.
conflict-sweep: ## ACTION p278 — re-read BOTH channels for a slug list: make conflict-sweep SLUGS=f
	@test -n "$(SLUGS)" || { echo "usage: make conflict-sweep SLUGS=path/to/slugs.txt"; exit 2; }
	@compose/code/p278-channel-conflict/sweep.sh "$(CURDIR)/$(SLUGS)"

# 🔴 ONLINE half — stays OUT of `hooks` so the standing check runs without egress.
enumerate: ## ACTION p275 — enumerate trees for a slug list: make enumerate SLUGS=slugs.txt
	@test -n "$(SLUGS)" || { echo "usage: make enumerate SLUGS=path/to/slugs.txt"; exit 2; }
	@cd compose/code/pass275-grant-enumeration && ./enumerate.sh < "$(CURDIR)/$(SLUGS)"

# 🟢 p274: T37 was written as an amendment in p272 and violated by the two passes after it.
# An amendment that is not built is not an amendment, so it is a target now.  No network.
recount: ## ACTION p274 — T37 as code: re-derive every registered quantity from the rows
	@$(PY) -I compose/code/p274-quantity-recount/recount.py --root . || exit 1
	@echo "   (STALE rows above are NOT a failure signal yet — see the register's own note)"

# 🟢 p274: the window sweep, T32 v3.  Zero searches, zero network, 28 market cells.
sweep: ## ACTION p274 — classify every market cell PASS / ROUNDING / WINDOW_FIX / SPLICE
	@$(PY) -I compose/code/p274-window-sweep/window_sweep.py || exit 1

# 🔴 p253: `set -e` DOES NOT abort these steps, measured rather than read.  bash exempts a
# command that is not the LAST in an `&&` list from errexit, so `cd d && test.py && echo PASS`
# swallows a failing `test.py`: the step prints no `PASS`, the recipe continues, and
# `ALL OFFLINE LICENCE CONTROLS PASS` prints anyway with `exit 0`.  Reproduced in isolation.
# 🔵 This is why `ACTION XM` and `XR` could audit 26 suites for failure-capability and still
# miss it: they asked whether each SUITE can signal, never whether the GATE propagates — and
# p251/p252 both recorded `make` as not runnable from their session, so neither ran it.
# 🟢 Every step therefore carries an explicit `|| exit 1`, and the banner is unreachable
# unless all of them pass.  `compose/code/p253-gate-propagation/` pins this.
delivery-audit: ## p332 — which rows did evidence/ measure that no shelf ever offered?
	@$(PY) -I compose/code/p332-delivery-audit/delivery_audit.py || true

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
	echo "── p332-delivery-audit   (evidence -> shelf delivery, 40 controls)"; \
	$(PY) -I compose/code/p332-delivery-audit/test_delivery_audit.py >/dev/null && echo "   PASS" || exit 1; \
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
	echo "── p329-grant-link-resolution (p329: a claim that points at its OWN missing grant)"; \
	cd compose/code/p329-grant-link-resolution && $(PY) -I test_grant_link.py >/dev/null && echo "   PASS" || exit 1; \
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
	echo "── pass257-restriction-scan (129 controls: p257 runs the vocabulary on EVERY payload; p287 makes it MULTILINGUAL, adds UNREADABLE-BODY, and anchors an untitled MIT body)"; \
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
	echo "── pass262-scoped-reservation-audit (p262: ACTION ZI — the STEWARD reservation, the X11 grant, and a row's state is not what it QUOTES)"; \
	cd compose/code/pass262-scoped-reservation-audit && $(PY) test_reservation_audit.py >/dev/null 2>&1 && echo "   PASS" || exit 1; \
	cd - >/dev/null; \
	echo "── p798-proxy-refusal-ledger (p294: the INVENTED host is in the ledger too — 22 controls)"; \
	cd compose/code/p798-proxy-refusal-ledger && $(PY) -I test_ledger.py >/dev/null 2>&1 && echo "   PASS" || exit 1; \
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

# 🔴 p309: THE TWO INSTRUMENTS THAT GRADED A REAL GPL-3.0 PAYLOAD AS AGPL-3.0.
# `p306-licence-probe` emitted four AGPL verdicts in its life, all at p309, and two
# were GPL-3.0 by title — `GatorEducator/gatorgrader` (35 191 B) and
# `five-plus-one/AI-Marker-Suite` (35 154 B).  The rung was `"affero" in low` over
# the whole body, ordered before the GPL rung, and GPL-3.0 §13 is TITLED "Use with
# the GNU Affero General Public License".
#
# 🔵 `p150-gpl-affero-discrimination` refuted that test 159 passes earlier and keeps
# it as its own negative control.  `p306` and `p191` RESTATED it.  `p308` learned
# "import the canonical list, never restate it" for SHELF DATA; this is the same
# rule for CLASSIFIERS.  Both now import `p150`, and this gate RUNS every declared
# classifier on first-hand payloads rather than reading its source: the static
# screen was wrong 34 times out of 36, the live run decided all 11.
gate-affero-rung: ## ACTION p308-R (adjacent) — no classifier may read GPL-3.0 as AGPL-3.0
	@cd compose/code/p309-affero-rung-census && { $(PY) test_rung_census.py > $(AFFERO_LOG) 2>&1 || { echo "🔴 p309-affero-rung-census FAILED — the suite's own report follows:" ; sed "s/^/   /" $(AFFERO_LOG) ; false ; } ; } && echo "── p309-affero-rung-census (36 controls: the §13 discriminator, the family matcher, the version-after-name rung, ladder order and its scope bug, the title window, p471's Spanish window, declared-token grammars, and GPL-3.0-inside-AGPL-3.0)" && echo "   PASS" || exit 1
	@cd compose/code/p309-affero-rung-census && $(PY) -I run_classifiers.py || exit 1

affero-rung-census: ## p309 — the static screen alone: a ranked backlog with a denominator
	@cd compose/code/p309-affero-rung-census && $(PY) -I rung_census.py .. || true
