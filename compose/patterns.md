---
industry: education
region: Global
updated: 2026-10-26
---

## 🆕 `p453` — **Three recipes, each built only from grants read first-hand at `HEAD` this pass. 🟢 `P453-A` is the three-probe promotion gate this pass proved is necessary — because a live, MIT-granted, correctly-back-linked package can still have nothing to do with education. 🟢 `P453-B` is a US institution-intelligence engagement that is buildable for the first time. 🟢 `P453-C` is a French parent-facing agent on a closed national SIS.**

🔴 **`make hooks` DENIED** (`Code from External`) — eighth denial in nine passes. Nothing here is
gate-attested; the load-bearing contracts were re-implemented independently and all are green.

---

### 🟢 `P453-A` — The three-probe promotion gate

🔵 **The defect it closes.** `Gap 452-B` asked for a reachability probe before promotion. This pass
built it, ran it on 182 candidates — and then found
[`food-x-technologies/escolar`](https://github.com/food-x-technologies/escolar): **live** at `HEAD`,
**real MIT payload** (1 075 B `sha256₁₂ 3b443e863252`), npm record **back-linking the exact slug**,
and a surface that reads *"Replace properties in json with file contents."* 🔴 **Two probes are not
enough. Three are.**

| # | probe | instrument | what it establishes | what it CANNOT establish |
|---|---|---|---|---|
| 1 | **back-link** | `vocab_probe.norm()` — forge-qualified, case-folded | the registry record belongs to **this** address | that the address is reachable (`Gap 452-B`) or that the licence value is right (`Gap 453-A`) |
| 2 | **reachability** | `vocab_probe.live_probe()` — `raw/HEAD/{9 paths}` → `git ls-remote` | the address resolves **now** | that the repository is on-topic |
| 3 | 🆕 **surface** | first-hand `README.md` read at `HEAD` | what the project **is** | — |

🟢 **Wiring it, concretely:**

```bash
# 1+2: candidate discovery with both probes, writing the spend ledger
python3 compose/code/p453-vocabulary-ledger/run_legs.py
#   -> evidence/vocabulary-spend-ledger.2026-10-26-p453.tsv
#      columns: leg, term, verdict, package, address, reachable, licence_declared,
#               probe_leg, prior_shelf_files, novelty

# 3: grant read title-anchored + byte-exact, for every surviving address
python3 compose/code/p453-vocabulary-ledger/verify.py {owner}/{repo} ...
#   bytes from curl -w '%{size_download}'  (NOT $(...), which strips the
#   trailing newline and runs every count one short -- Gap 450-C defect (b))
#   family from the payload TITLE   (NOT a body grep, which calls every
#   GPLv3 file LGPL -- Gap 450-C defect (a))

# 3b: the probe no instrument can replace -- read the README and decide
curl -s https://raw.githubusercontent.com/{owner}/{repo}/HEAD/README.md | head -40
```

🔴 **Do not skip probe 3 because probes 1 and 2 are green.** On this pass's population that
combination was green for **157** addresses and correct for **6**.

---

### 🟢 `P453-B` — US institution intelligence, keyed to `UNITID` (North America)

🔵 **Why it is buildable only now.** `Gap 452-D` recorded that the US registry layer's *"packaged
permissive form is simply unknown here"*. Five MIT rows later it is known, so the engagement no
longer starts with a data-acquisition project.

| layer | component | grant, read first-hand |
|---|---|---|
| ingestion | [`UrbanInstitute/ipeds-scraper`](https://github.com/UrbanInstitute/ipeds-scraper) | **MIT** · `LICENSE.md` 1 058 B `bac93c5411aa` |
| warehouse | [`paulgp/ipeds-database`](https://github.com/paulgp/ipeds-database) → DuckDB, 27 M rows / 23 tables, 1997-2024 | **MIT** · 1 056 B `1126322e2cc8` |
| query layer | [`scienceforamerica/scipeds`](https://github.com/scienceforamerica/scipeds) (directory + completions, 2025 data) | **MIT** · 1 088 B `e04b31a1be21` |
| current-year disclosure | [`bolewood/collegedata-fyi`](https://github.com/bolewood/collegedata-fyi) — 4 071 archived CDS docs, 1 105-field schema | **MIT** · 1 115 B `a3a16c648652` |

🟢 **The wiring, and the one rule that makes it defensible:**

1. Build the DuckDB warehouse (`uv run python build_database.py`) — one command, ~1 GB.
2. Load the CDS extracts beside it, keyed on zero-padded `UNITID` (`ipeds_id`).
3. 🔴 **Keep the two sources in separate labelled tables and never coalesce a field.** IPEDS is the
   federal baseline; the CDS is school-authored and current-year. They disagree **by
   construction** — and `collegedata-fyi` refuses to blend them for exactly this reason.
4. Put the agent **on top of the warehouse, not on the PDFs**: retrieval over typed rows, with
   every answer citing `(source ∈ {CDS, IPEDS, Scorecard}, year, UNITID)`.

🔵 **The sellable wedge, from this pass's own NA market leg:** **10 %** of US institutions have
formal AI guidelines and **71 %** of teachers are untrained — so the first deliverable is an
institution-intelligence and governance layer, not a tutor. 🟡 All four grants are permissive, so
the deliverable can be closed-source; `collegedata-fyi`'s own figures are **self-reported** from
its 2026-08-06 audit and should be re-counted before they appear in a client deck.

---

### 🟢 `P453-C` — A parent-facing `vie scolaire` agent on a closed national SIS (EMEA / France)

🔵 **The shape.** There is no French LMS to integrate: ÉcoleDirecte holds the record and publishes
no open core, so the connector *is* the platform decision.

| layer | component | grant | why this one |
|---|---|---|---|
| SIS connector | [`androz2091/node-ecole-directe`](https://github.com/androz2091/node-ecole-directe) | 🟢 **Apache-2.0** · 11 357 B `c71d239df917` | 🟢 the **only** build-on client of the three: Élève + Famille auth, `notes`, `devoirs`, `emplois du temps`, `vie scolaire` |
| 🔴 rejected | [`papillonapp/papillon-ed-core`](https://github.com/papillonapp/papillon-ed-core) | 🔴 GPL-3.0 · 35 149 B | strong copyleft propagates into the deliverable |
| 🔴 rejected | [`louislegrain/api-ecoledirecte`](https://github.com/louislegrain/api-ecoledirecte) | 🔴 ISC declared, **no payload** | `Gap 451-C` manifest-only: nothing serves the grant's text |
| parent persona | the `p388` parent/guardian tier already on `agents/top.md` | — | the persona is shelved; only the French record was missing |
| grading | 🔴 **not the LLM** — keep marks as retrieved fields | — | Pattern BC's split-clock rule: Reg. (EU) 2026/1744 Art. 50 is live since 2026-08-02 |

🔴 **The licence step is mandatory here and is the pattern's actual lesson.** npm declares
`node-ecole-directe` as `ISC`; the repository serves **Apache-2.0**. 🟢 Build under **Apache-2.0**
— it is the more obligated reading (retain `NOTICE`, mark modified files) *and* the one that
actually governs, and it adds the patent grant `ISC` does not have. 🔵 A team that trusted the
badge would under-comply on attribution while believing it had fewer obligations.

🟡 **Scope honestly.** ÉcoleDirecte's API is undocumented and unversioned; all three clients track
it by observation. Budget for breakage on the vendor's schedule, and treat `vie scolaire` writes as
out of scope — `p448` measured that 136 of 414 connector tool declarations mutate, and a wrong
write here lands on a child's disciplinary record.

## 🆕 `p452` — **Two recipes, both built only from grants read first-hand this pass. 🟢 `P452-A` is a licence-assurance gate that encodes the one thing this pass proved — that registry corroboration works for npm and fails for PyPI — so an engagement stops treating "it's on a registry" as uniform evidence. 🟢 `P452-B` is an EMEA/Maghreb vocational-training engagement that is buildable because the institution registry finally exists.**

🔴 **`make hooks` DENIED** (`Code from External`) — seventh denial in eight passes. Nothing here is
gate-attested; the four load-bearing contracts were re-implemented by hand and all four are green.

---

### 🟢 `P452-A` — **Dependency licence assurance that knows which half of the tree it can corroborate**

🔴 **The problem it solves, measured not assumed.** `p451` made a rule standing: a registry record is
evidence for a repository only when its own metadata **back-links that exact `owner/repo`**. 🟢 This
pass swept all **71** carried registry-sourced cells and found **0** mis-attributions — but **8 that
cannot be corroborated at all**, and the mechanism is ecosystem-specific: **4 of 6 `ABSENT` plus the
only `PAGES_ONLY` are PyPI**. 🔴 So a single uniform "check the registry" step silently passes the
Node tier and silently produces nothing for the Python tier.

**Wiring, concrete:**

1. 🟢 **Back-link resolver** — [`compose/code/p452-backlink-sweep/sweep.py`](code/p452-backlink-sweep/sweep.py),
   as built and run this pass. For each dependency it reads `registry.npmjs.org/{pkg}`,
   `pypi.org/pypi/{pkg}/json` or `packagist.org/packages/{v}/{p}.json` and emits
   `AGREE` / `DISAGREE` / `FOREIGN_FORGE` / `PAGES_ONLY` / `ABSENT` / `NO_RECORD`.
   🔴 Two defects this pass had to fix in it are load-bearing and must not be reintroduced:
   the normaliser must be **forge-qualified** (a `github.com`-only matcher called PyPI `travo`'s
   exact GitLab back-link `ABSENT`), and a **GitHub Pages** URL must grade `PAGES_ONLY`, never as a
   back-link — `rusticisoftware.github.io/TinCanPython/` matches a naive `grep -i github` and is
   not evidence.
2. 🔴 **Ecosystem routing, which is the whole point.** `AGREE` on npm → accept the registry licence
   as corroboration. **Any PyPI dependency → go straight to the payload**, because the expected
   outcome is `ABSENT`. Payload read is `curl -w '%{size_download}'` against
   `raw.githubusercontent.com/{slug}/HEAD/LICENSE`, recording **bytes + `sha256₁₂`** — never shell
   command substitution, which strips the trailing newline and reads one byte low (`p450`; 11 such
   cells found on these shelves this pass).
3. 🔴 **Hard-fail list, each with a live instance from these shelves:**
   `SEE LICENSE IN LICENSE` → **not a licence, a pointer out of the registry**
   (npm `@geoalgeria/formation-professionnelle`, `@incproctor/proctoring-sdk`; and
   `ale-alejandro/beadkit`, where the repository was withdrawn and **no party can now produce the
   grant** — `Gap 451-C`). No licence field at all → `@imazhar101/mcp-canvas-server` `2.1.3`, which
   registers **227 tools of which 61 are undocumented writes** to an LMS. Version-split grants →
   `dev-cucei-itrans/siiau-api-client`, **`proprietary` on 4 of 7 versions**, so a `^1.0`
   constraint resolves *into* the proprietary band.
4. 🟢 **Store the payload at approval time.** The `geoalgeria` case is the argument: a
   `SEE LICENSE IN LICENSE` grant is recoverable **only while its repository lives**, with no notice
   and no archival copy when it is withdrawn.

🟢 **Stack:** `sweep.py` + `curl` + the repo's own CI. 🟡 **Effort:** 1–2 weeks to wire into a
pipeline. 🔵 **What it buys:** the Python half of an education stack stops being certified by a
check that structurally cannot certify it.

---

### 🟢 `P452-B` — **EMEA / Maghreb vocational-training engagement, keyed on a registry that now exists**

🔴 **Why this was not buildable before this pass.** This base could answer *"what runs a school"* —
eight platforms on [`verticals/solutions.md`](../verticals/solutions.md) — and could not answer
*"which schools exist"* for any region. 🔴 A ministry or group engagement sizes and segments the
estate **before** it picks a platform, so the missing layer was the first one needed.

**Wiring, concrete, every grant read first-hand at `HEAD` this pass or carried with a byte-exact
re-read:**

| layer | component | grant |
|---|---|---|
| 🟢 **Institution registry** *(the join key)* | [`yasserstudio/geoalgeria`](https://github.com/yasserstudio/geoalgeria) — **1 932** vocational establishments (856 CFPA, 182 INSFP, 723 private accredited, 58 DFEPs) from **MFEP / takwin.dz**, **177** MESRS higher-ed, **11 858** schools, **69** wilayas, GPS + capacity + boarding, EN/FR/AR | 🟢 **MIT**, `LICENSE` 1 101 B `sha256₁₂ 691e4ec845d7` |
| 🟡 **Delivery platform** | [`moodle/moodle`](https://github.com/moodle/moodle) — the Maghreb's installed base | 🔴 **GPL-3.0**, `COPYING.txt` 35 147 B *(re-read EXACT this pass)* — **link, don't absorb** |
| 🟢 **Agent access layer** | [`FiredMosquito831/ase-moodle-mcp`](https://github.com/FiredMosquito831/ase-moodle-mcp) — courses, assignments, grades, deadlines; the pattern proven at ASE Bucharest, i.e. **single-institution and permissive** | 🟢 **Apache-2.0**, `LICENSE` 11 358 B `sha256₁₂ cfc7749b96f6` *(re-read EXACT)* |
| 🟢 **Read-only student surface** | [`tcpassos/moodle-student-mcp`](https://github.com/tcpassos/moodle-student-mcp) — official mobile-app web service, **nothing is ever changed on Moodle**, SSO + MFA | 🟢 **MIT**, `LICENSE` 1 069 B `sha256₁₂ 322307ac9d65` |
| 🟢 **Offline tier** *(non-negotiable here)* | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT**, `LICENSE` 1 097 B *(re-read EXACT this pass)* |
| 🟢 **Session-to-documentation** | [`D4vRAM369/pbl-project-chronicler`](https://github.com/D4vRAM369/pbl-project-chronicler) — turns CFPA workshop sessions into reproducible step-by-step records; **French/Arabic instructor cohorts need the translated README path, which exists** | 🟢 **MIT**, `LICENSE` 1 066 B `sha256₁₂ 95576ceceaa3` |

**Sequence:** segment the 1 932 establishments by wilaya, type and capacity from the registry → phase
the rollout territorially against GPS and boarding capacity → stand up Moodle per establishment group
with Kolibri for low-connectivity wilayas → put `ase-moodle-mcp` on the instructor side and
`tcpassos/moodle-student-mcp` on the student side (read-only by construction, so it clears a review
that a write-capable connector does not) → chronicler on practical workshops.

🟡 **Effort:** 10–12 weeks. 🟢 **Licence posture:** the deliverable's own code sits on MIT/Apache-2.0
and only **links** the GPL-3.0 platform.

🔴 **Four cautions, stated so the recipe is not over-sold.** (1) The registry is **data, not
software** — no API, no auth, no runtime. (2) Its three tiers do **not** carry equal authority: the
vocational and higher-education tiers are ministry-sourced (MFEP, MESRS), the **11 858** schools
figure is **OpenStreetMap-derived** and is a volunteer-mapped count, not a census — they must never
be cited as one number. (3) `@geoalgeria/*` declares `SEE LICENSE IN LICENSE` on npm, so
**`P452-A` step 4 applies to this very pattern**: store the payload. (4) 🔴 **One country.** This
pattern is Algeria-specific; the rest of the Maghreb, the Gulf and sub-Saharan Africa have **no
registry asset on these shelves** (`Gap 452-E`), and nothing here should be sold as regional
coverage.

## 🆕 Pattern BD — `p451` **Grant recovery for a withdrawn dependency: how to keep shipping when the repository behind a component disappears, and how to know within one hour whether you can**

🔵 **Why this pattern.** Six addresses on these shelves were withdrawn from GitHub while their
published artifacts stayed installable. 🔴 An engagement discovers this the way `p450` did — a
`404` in CI or an audit — and the question it then has to answer is not *"is it still
installable?"* (it is) but **"do we have a grant, and can we prove it?"** 🟢 This pattern is the
measured procedure, built from the nine resolutions this pass made, and it runs in under an hour.

### 🟢 Step 1 — Establish that your probe can fail, before you trust any negative

🔴 **Do not skip this**: two instruments were caught constant-across-domain on this host, and a
third was caught on a wrong path **in this pass's own code**.

```bash
# both controls are mandatory: a live address AND a fabricated one
for slug in moodle/moodle globant-fabricated-451/does-not-exist; do
  curl -sS -o /dev/null -w "$slug raw=%{http_code}\n" \
    "https://raw.githubusercontent.com/$slug/HEAD/README.md"
  git ls-remote "https://github.com/$slug" >/dev/null 2>&1 \
    && echo "$slug lsremote=OK" || echo "$slug lsremote=FAIL"
done
# expect: moodle 200/OK, fabricated 404/FAIL.  Equal results = the probe is zero bits, STOP.
```

🔴 **Known-bad instruments on this host, each measured:** `curl -sI github.com/{slug}` → `403`
for live, dead and fabricated alike (`p450`); authenticated **GitHub MCP** `get_file_contents` →
identical access-denied for `HKUDS/DeepTutor` and for a fabricated slug (`p451`);
`repo.packagist.org/packages/{v}.json` → `404` **for `laravel/framework`** (`p451`, caught by the
positive control). 🟢 The working paths are `raw.githubusercontent`, `git ls-remote`,
`registry.npmjs.org`, `pypi.org` and **`packagist.org/packages/{v}.json`**.

### 🟢 Step 2 — Go to the registry the component actually ships on, and read the BACK-LINK

```bash
# npm — note that the scoped name may differ from the bare one:
#   thanh01pmt/interactive-quiz-kit publishes as @thanh01.pmt/interactive-quiz-kit
curl -sS "https://registry.npmjs.org/$(printf %s "@thanh01.pmt/interactive-quiz-kit" | sed 's|/|%2f|')" \
  | python3 -I -c 'import json,sys; d=json.load(sys.stdin); v=d["dist-tags"]["latest"]; m=d["versions"][v]; print(v, m.get("license"), m.get("repository",{}).get("url"))'

# PyPI — project_urls is where the back-link lives
curl -sS "https://pypi.org/pypi/unist-blackboard-mcp/json" \
  | python3 -I -c 'import json,sys; i=json.load(sys.stdin)["info"]; print(i["version"], i.get("license"), i.get("project_urls"))'

# Packagist — per-VERSION licences, which is the field that caught siiau-api-client
curl -sS "https://packagist.org/packages/dev-cucei-itrans/siiau-api-client.json" \
  | python3 -I -c 'import json,sys; p=json.load(sys.stdin)["package"]; print(p["repository"], p.get("abandoned")); [print(k, (v.get("time") or "")[:10], v.get("license")) for k,v in sorted(p["versions"].items())]'
```

🔴 **Accept the record as evidence for your address only if the back-link is that exact
`owner/repo`.** On this base's own nine, **2 of the 3 name-hits belonged to a third party** —
`blackboard-mcp` is `felipedias-ie`'s live MIT server, `autograder` is held twice by two unrelated
parties, one of them **GPL-3.0**. Taking the name would have written somebody else's licence onto
your dependency.

### 🟢 Step 3 — Classify what you got, because it decides the engagement, not just the ticket

| what the registry gave you | what you may do | worked example from these shelves |
|---|---|---|
| 🟢 SPDX identifier + matching back-link | 🟢 **Ship.** Vendor the tarball, record the registry JSON as grant evidence, pin exactly | `@thanh01.pmt/interactive-quiz-kit` **MIT** `1.4.10` · PyPI `unist-blackboard-mcp` **MIT** `0.2.0` · npm `rhizome-lms-mcp` **MIT** `0.3.1` |
| 🟡 identifier in the manifest, **no payload** ever shipped | 🟡 **Ship only with legal sign-off** — there is a declaration but no licence text to attach | `@santillana-ai/create-tutor-app` (MIT manifest, tarball carries `README` + templates only) |
| 🔴 identifier **changes across versions** | 🔴 **Pin above the boundary and prove it** | `siiau-api-client`: `proprietary` on `v1.0.0-BETA`…`v1.1.1`, **`BSD-3-Clause` from `v1.1.2`** → constrain `>=1.1.2`, never `^1.0` |
| 🔴 declaration points at a file nobody can serve | 🔴 **Do not ship. Replace the component.** | `beadkit`: npm says `SEE LICENSE IN LICENSE`; that `LICENSE` was in the deleted repo, so **no party on earth can now produce the grant** |
| 🔴 no trace on npm, PyPI **or** Packagist | 🟡 **Unresolved — not "unlicensed".** Treat as a build-or-replace decision; do not write a licence cell | `AI-Matrix-Engine/aidream` |

### 🟢 Step 4 — Replace, with named substitutes from these shelves

🔵 Withdrawal is usually not fatal to the *capability*, only to the address. For the tiers hit this
pass there are live, first-hand-verified replacements:

- **Blackboard** → [`felipedias-ie/blackboard-mcp`](https://github.com/felipedias-ie/blackboard-mcp)
  — **MIT**, `LICENSE` 1 084 B, Ultra courses/content/files/grades/deadlines over the user's own
  browser session (replaces both withdrawn Blackboard addresses).
- **Moodle, student-side** → [`tcpassos/moodle-student-mcp`](https://github.com/tcpassos/moodle-student-mcp)
  — **MIT**, `LICENSE` 1 069 B `sha256₁₂ 322307ac9d65`, official mobile-app web service,
  read-only by construction, SSO + MFA.
- **Moodle, single-institution (EMEA)** → [`FiredMosquito831/ase-moodle-mcp`](https://github.com/FiredMosquito831/ase-moodle-mcp)
  — **Apache-2.0**, `LICENSE` 11 358 B `sha256₁₂ cfc7749b96f6`, BL@ASE / `online.ase.ro`,
  Python 3.10+, CI present.
- **Quiz/assessment authoring** → `@openhpi/quiz-recap` (**MIT**,
  [`christophblessing/quiz-recap`](https://github.com/christophblessing/quiz-recap), 35 versions)
  for the recap surface; 🔴 do **not** reach for `@thanh01.pmt/curriculum-kit` as a replacement
  despite being live and MIT — it declares **no `repository` field**, so there is no address to
  audit (`p280`'s unattributable class).

### 🔴 Step 5 — Make the recovery durable, or you will repeat it next quarter

🟢 **Vendor, do not reference.** Commit the tarball (or a lockfile with integrity hashes) **and**
the registry JSON that carried the back-link and licence, into your own repository. 🔴 The
registry record is the single point of failure once the repository is gone — `beadkit` shows what
remains when the second channel goes too: an installable package with an unknowable grant. 🔵 The
dependency-closure pass still applies on top (`compose/code/dependency-licence-closure`): a
permissive root does not clear the tree (`Trend 40`).

---

## 🆕 Pattern BC — `p450` **The split-clock EU tutor: ship the Article 50 obligations that are live NOW, and isolate the Annex III surface so December 2027 is a conformity deliverable instead of a rewrite — every component's grant and ref read first-hand this pass**

🔵 **Why this pattern and not another "AI tutor" recipe.** `Reg. (EU) 2026/1744` split the EU
compliance clock in two, and no pattern on these shelves is built around the split: **Article 50
transparency has applied since 2 Aug 2026** (machine-readable marking transitional to **2 Dec
2026**), while **Annex III high-risk obligations — learner evaluation, programme assignment,
proctoring, access to qualifications — do not bite until 2 Dec 2027**. 🔴 **A build that treats
those as one deadline gets it wrong in both directions**: it ships non-compliant disclosure today,
and it over-engineers conformity work a year early. This pattern makes the split a boundary in the
code.

### 🟢 Components — grant, ref and size re-read first-hand 2026-10-26 (`evidence/licence-title-anchored.2026-10-26-p450.tsv`)

| role | component | 🟢 grant *(verified this pass)* | ref | why this one |
|---|---|---|---|---|
| Tutor / dialogue agent | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · `LICENSE` 11 408 B | `main` | permissive, so the deliverable is vendorable; the one agent-native tutor on these shelves |
| Courseware generation | [satvik314/educhain](https://github.com/satvik314/educhain) | 🟢 **MIT** · `LICENSE` 1 092 B | `main` | generates the artefacts that Art. 50(2) marking must attach to |
| 🔴 **Mastery / grading decision** | [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) + [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | 🟢 **MIT** · 1 132 B / 1 105 B | `main` | 🔴 **the Annex III surface, and it is deliberately NOT an LLM** — Bayesian Knowledge Tracing is deterministic, inspectable and reproducible |
| LMS launch seam | [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) *(py)* or [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) *(php)* | 🟢 **MIT** 1 070 B / 🟢 **Apache-2.0** 11 343 B | `master` / `main` | LTI 1.3 launch keeps the platform at arm's length — **this is the licence seam** |
| LMS read/write connector | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) · [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | 🟢 **MIT** · 1 071 B / 1 070 B | `main` | the write tier `Gap 447-B` confirmed: `create_course`, `update-syllabus`, publish toggles |
| Interactive content | [edly-io/h5pxblock](https://github.com/edly-io/h5pxblock) | 🟢 **MIT** · `LICENSE` 1 064 B | `master` | 🔴 **loads H5P as runtime content** — never link [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library), **GPL-3.0, 35 146 B** |
| Platform tier *(behind the seam)* | [moodle/moodle](https://github.com/moodle/moodle) **GPL-3.0** 35 147 B · [openedx/edx-platform](https://github.com/openedx/edx-platform) **AGPL-3.0** 35 136 B · [overhangio/tutor](https://github.com/overhangio/tutor) **AGPL-3.0** 34 523 B | 🔴 copyleft | `main` / `master` / 🔴 **`release`** | 🔴 **deployed, never forked into the deliverable** |

### 🟢 Wiring — six steps, and the two boundaries are the whole point

1. **Launch** — the LMS launches the tutor over **LTI 1.3** (`pylti1.3`). 🟢 **Boundary 1, the
   licence seam:** the tutor runs as a separate service reached by signed launch, so Moodle's
   GPL-3.0 and Open edX's AGPL-3.0 never reach the Apache/MIT deliverable. Forking the platform
   would pull copyleft into the client's product; AGPL would reach their *hosted* use.
2. **Disclose, at the first token** — a disclosure interceptor in front of DeepTutor emits the
   Art. 50(1) notice that the learner is interacting with an AI system. 🔴 **Due now, not 2027.**
3. **Generate and mark** — `educhain` produces explanations, quizzes and course outlines; every
   artefact is written with **machine-readable provenance marking** at the moment of generation
   (Art. 50(2)). 🔴 **For content already in a client's library before 2 Aug 2026 the transitional
   deadline is 2 Dec 2026** — a backfill job, and it is the nearest deadline in this pattern.
4. 🔴 **Route every grade-affecting decision to `pyBKT`, never to the model.** The LLM may explain,
   hint, rephrase and tutor; **mastery state, item selection and any score come from BKT over
   OATutor's item bank.** 🟢 **Boundary 2, the Annex III surface:** it is deterministic, replayable
   from the event log, and defensible without interpreting a model.
5. **Human in the loop on the high-stakes path** — a grade, placement or progression
   recommendation is surfaced to an instructor and **never written back as the sole basis for a
   decision**. Write-back uses the MCP connector's authoring tools, **gated on the tool's
   EFFECT, never on `read_only_hint`** (`Gap 448-B`).
6. **Content** — H5P activities render through `h5pxblock` as runtime content, keeping the GPL-3.0
   PHP library out of the link graph.

### 🟢 What step 4 and 5 buy outside the EU — the same boundary satisfies three more regimes

| region | requirement | satisfied by |
|---|---|---|
| **North America** | Oklahoma and Maryland require human oversight and bar AI as the basis of high-stakes student decisions; Charleston County's Jan-2026 policy bars AI as the **sole** basis for discipline, placement and special-education determinations | 🟢 steps **4 + 5**, unchanged |
| **APAC** | 🔴 **Vietnam is the only APAC jurisdiction naming education in its high-risk list** (automated assessment, behavioural monitoring) — and much of it binds only where output is *the sole basis without meaningful human review* | 🟢 step **5** keeps the product outside the binding case |
| **LATAM** | UNESCO IESALC: **87 % adoption, 26 % with any formal AI strategy** — the gap is governance, not capability | 🟢 the event log from step **4** *is* the governance artefact an institution cannot otherwise produce |

🔵 **So the pattern is one build with four regulatory readings**, which is what makes it sellable
beyond a single geography — and the regional cells behind it are **relayed, not first-hand**:
`eur-lex.europa.eu`, `digital-strategy.ec.europa.eu` and `www.unesco.org` are all **403 at CONNECT**
from this host class (`Gap 446-D`, sixteen hosts). 🔴 **A client-facing version of this pattern must
re-read the Official Journal text directly.**

### 🟢 Build gate — wire this pass's probe into CI, because the alternative is shipping a dead address

```bash
# Two-stage reachability + authoritative grant read. Stage 2 is not optional:
# 1 in 20 live addresses on these shelves serves no HEAD/README.md.
probe() {  # $1 = owner/repo
  code=$(curl -s -o /dev/null -w '%{http_code}' "https://raw.githubusercontent.com/$1/HEAD/README.md")
  [ "$code" = 200 ] && { echo "$1 LIVE"; return 0; }
  GIT_TERMINAL_PROMPT=0 git ls-remote --heads "https://github.com/$1" >/dev/null 2>&1 \
    && echo "$1 LIVE (no HEAD/README.md)" || { echo "$1 UNREACHABLE"; return 1; }
}
grant() {  # length is a property of the TRANSFER, never of a shell-captured string
  for p in LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt; do
    read -r c n < <(curl -s -o /tmp/g -w '%{http_code} %{size_download}' \
                      "https://raw.githubusercontent.com/$1/HEAD/$p")
    [ "$c" = 200 ] || continue
    # family from the TITLE (first 6 non-blank lines): GPLv3's closing paragraph
    # recommends the LGPL, so a whole-body grep misreads every GPLv3 file.
    grep -v '^[[:space:]]*$' /tmp/g | head -6 | grep -qi 'LESSER' && f=LGPL \
      || grep -v '^[[:space:]]*$' /tmp/g | head -6 | grep -qi 'AFFERO' && f=AGPL \
      || f=$(grep -v '^[[:space:]]*$' /tmp/g | head -6 | grep -oiE 'apache|mit|general public' | head -1)
    echo "$1 $p $f ${n}B"; return 0
  done; echo "$1 NO-GRANT-AT-5-PATHS"; return 1
}
```

🔴 **Fail the build on `UNREACHABLE` or on a copyleft family appearing in the link graph** — the
two failures this pass found on the shelves themselves: nine unreachable addresses, and one
platform graded `🟢 MIT` in one table and `🟡 GPL-3.0` in another table of the same file.

🔵 **Effort, in the shape these shelves use:** 🟢 **steps 1–3 + 6, 4–5 weeks** (launch seam,
disclosure, marking, H5P) — this is the Art. 50 deliverable and it is due now. 🟢 **Steps 4–5,
4–6 weeks** (BKT mastery, item bank, instructor review, effect-keyed write-back). 🟡 **Annex III
conformity packaging — assessment, human-oversight documentation, post-market monitoring —
scheduled against 2 Dec 2027, not now**, which is the saving the split clock pays for.

🔴 **What this pattern does not do.** It does not make an LLM safe to grade with; it removes the
LLM from grading. It does not cover proctoring or behavioural monitoring — both are Annex III and
Vietnam high-risk, and nothing permissive on these shelves does them defensibly. And it inherits
`Trend 40`: **Apache-2.0 at the root does not clear the dependency tree**, so a dependency-closure
pass (`compose/code/dependency-licence-closure`) is a prerequisite to shipping, not a follow-up.
## 🆕 Pattern BB — `p449` **The effect-keyed courseware-authoring gateway — the first pattern on these shelves that can be wired from a MEASURED write surface rather than an advertised one, plus the two-control verification pre-flight that `Gap 449-A` makes mandatory**

🟢 **Gate posture (`Gap 446-A`): `make hooks` RAN** — fourth trial after three denials; that
gap's settlement is **refuted**, the denial is **intermittent**. 🟢 Arrival **58/62 green,
4 RED**, 🔴 two new and both `p448`'s; three green on exit.

### Why this pattern is now buildable, and what changed under it

🔴 `Pattern AZ` and the patterns before it assumed the community LMS-connector tier was
**read-only** — `p447` carried that claim explicitly. 🟢 `p448` refuted it from source; 🟢 `p449`
corrects the magnitude **upward**: the category write share is **35.8 %** (136/**380**), not
32.9 %, because `p448`'s denominator counted 19 non-tool `name:` fields while its **WRITE
numerator of 62 was EXACT** against the README's own declaration. 🔵 **An agent layer here can
author and publish courseware** — and therefore must be gated.

### The recipe, named repo by repo

| layer | component | grant | first-hand cell | role |
|---|---|---|---|---|
| system of record | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | 🟢 **Apache-2.0** | `LICENSE.txt` **10 172 B** (reproduced by `p449`) | the only permissive SIS on these shelves; the NA state channel mandates API submission to it |
| LMS seam | [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | `LICENSE.TXT` **11 358 B** (reproduced by `p449`) | component boundary into a copyleft LMS without inheriting its grant |
| authoring tools | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) @ `c740624` | MIT (`LICENSE` 1 070 B) | 🟢 **188** tools, 🔴 **62 WRITE** | `create_course`, `create_module`, `create_module_item`, `create_page`, `create_new_quiz`, `grade_submission`, `enroll_user` |
| publish toggles | [`mdweaver/canvas-mcp`](https://github.com/mdweaver/canvas-mcp) | MIT | 89 tools, 🔴 **41 WRITE (46.1 %)** | `toggle-module-publish` (`src/tools/modules.ts:114`), `update-syllabus`, `post-announcement` |
| bulk grading | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | MIT | 128 tools | `bulk_grade_submissions`, `bulk_update_pages` — 🔴 **and the 55 undeclared-hint tools are exactly these** |
| adaptive core | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** (`LICENSE` 1 066 B) | — | knowledge tracing behind the authoring decisions |

### 🔴 The gateway, and the one rule that makes it safe

```
agent ──▶ mcp-allowlist-gateway ──▶ {canvas-lms-mcp, canvas-mcp, moodle-mcp}
             │
             └── keys on the TOOL'S EFFECT, resolved from source, NEVER on read_only_hint
```

🔴 **Do not key the allowlist on `read_only_hint` (`Gap 448-B`).** Measured over
`vishalsachdev/canvas-mcp`'s 128 declarations: `=True` on **72**, `=False` on **1** — and that
one is `download_course_file`, **a read** — with **55 (43.0 %) undeclared, which are exactly the
mutating tools.** 🟢 Resolve effect the way `p449` resolved `Gap 448-C`: a tool is a WRITE iff
its registry entry's enclosing object literal says so in **source**, not in a hint field.
🔵 Wire the write tier behind a human-in-the-loop approval and an audit trail — **governed
adoption is the sellable unit**, and on a 35.8 % mutating surface it is also the liability line.

### 🟢 The verification pre-flight this pattern must run, with TWO controls

🔴 `Gap 449-A`: `curl -sI https://github.com/<slug>` returns **403 on every real repository** on
this host class while `git clone` of the same address succeeds. Any pre-flight built on it fails
**closed on live rows** and would condemn all ~134 shelved addresses.

```sh
# 1 — sound existence+payload probe (NOT github.com HTML, NOT api.github.com)
curl -s -o /dev/null -w '%{http_code}|%{size_download}' \
     "https://raw.githubusercontent.com/$SLUG/$BRANCH/$LICENSE_PATH"
# 2 — control A, a negative: MUST return 404|14
curl -s -o /dev/null -w '%{http_code}|%{size_download}' \
     "https://raw.githubusercontent.com/zzz-fake-org-p449/zzz-fake-repo/main/LICENSE"
# 3 — control B, case: probe the case the SHELF RECORDED (Gap 449-B)
#     openedx/XBlock -> LICENSE.txt 404 x3, LICENSE.TXT -> 200|11358
```

🔵 **Both controls are load-bearing, and each caught a real false negative this pass.** Control A
distinguishes a dead row from a blocked host; control B stops case normalisation from
manufacturing dead rows. 🟡 **Budget:** one `curl` per row plus two controls per sweep — the
cheapest gate on these shelves, and the only one standing between a live address and a
deletion.

### 🔴 What this pattern does NOT cover, stated rather than implied

🔴 No government or analyst primary is reachable from this host (`Gap 446-D`, **thirteen** hosts,
now citing the proxy's own `connect_rejected` log), so every regulatory constraint this pattern
inherits is **relayed**, not primary. 🔴 Pin recency governs whether the cells above still hold:
`Pattern AZ` as corrected by `p448` gives **≥ 7 days → 97.4 %** survival against **48.9 %**
below, and `bruchris` @ `c740624` is **3 days** old at read time — 🟡 inside the band where
roughly **one pin in five** does not survive 24 h. Re-probe before quoting.

---

## 🆕 Pattern BA — `p448` **The CALIBRATED pin-recency pre-flight — and the correction of `Pattern AZ`, published one pass ago on n = 5, whose threshold was wrong, whose budget line was survivorship-biased, and whose refutation of commit volume had the sign backwards**

🔵 **Why this supersedes `Pattern AZ` rather than extending it.** `AZ` (`p447`) built a
pre-flight on **five** observations — one pinning per repository, i.e. one coin flip each — and
published three claims from it. `Gap 447-C` registered the calibration limit itself. `p448` paid
it: **496 observations across 36 shelved repositories**, and the pattern survives in **direction**
while **two of its three published claims do not**.

### 🟢 The instrument: a retrospective simulation, so the calibration needs no waiting

For each repository, for each offset `d` in 1…14 days, ask what a studio pinning at that moment
would have got, and whether it held 24 h later:

```bash
# one observation: would a pin taken at time T still be HEAD at T+24h?
git clone --quiet --filter=blob:none --no-checkout https://github.com/OWNER/REPO /tmp/r
PIN=$(git -C /tmp/r rev-list -1 --before="$T" HEAD)
NXT=$(git -C /tmp/r rev-list -1 --before="$T +1 day" HEAD)
AGE=$(git -C /tmp/r show -s --format=%cI "$PIN")   # how old was that commit when pinned?
[ "$PIN" = "$NXT" ] && echo HELD || echo STALE
```

🟢 **36 blobless clones → 496 observations, in one pass, with no 24-hour wait.**
🟢 **Validated before use**, against a cell this base already published: `Apomera/AlloFlow`'s
refs date to `2026-10-24T12:35:30-04:00` and `2026-10-25T18:50:44-04:00`, reproducing `p447`'s
*"pinned 10-24 12:35, HEAD 10-25 18:50"* **to the minute**.
🟢 **Pre-condition checked, not assumed:** the method needs committer dates to be monotone along
history. Measured over **9 438** adjacent commit pairs in these 36 repositories: **0
inversions**, **36 of 36** repositories clean.

### 🟢 The calibration curve — this is the pattern

| age of the commit **at the moment you pin it** | n | 🟢 P(pin still HEAD after 24 h) |
|---|---|---|
| < 1 h | 33 | 🔴 **6.1 %** |
| 1–6 h | 35 | 🔴 **20.0 %** |
| 6–24 h | 99 | 🔴 **35.4 %** |
| 1–3 d | 81 | 🟡 **71.6 %** |
| 3–7 d | 59 | 🟡 **81.4 %** |
| **7–30 d** | 100 | 🟢 **98.0 %** |
| > 30 d | 89 | 🟢 **96.6 %** |

🔴 **`Pattern AZ`'s threshold was wrong.** `AZ` said **days** → *"settled, the pin will hold,
safe to quote with its date."* At **1–3 days the pin fails 28 % of the time.** The operating
point that earns the word "settled" is **seven days**:

| rule | n above threshold | P(held) |
|---|---|---|
| 🟢 **age at pin ≥ 7 d** | 189 | 🟢 **97.4 %** |
| 🔴 age at pin < 7 d | 307 | 🔴 **48.9 %** |

🔴 **`AZ`'s biconditional was an artefact of n = 5.** It published that
`pinned_commit_date == HEAD-date` **iff** the pin held, *"in every row"*. Over the proper
denominator the biconditional **fails in 44 of the 167** observations with age < 24 h. As a
classifier, `AZ`'s 24-hour rule scores precision **73.7 %**, recall **75.9 %**, accuracy
**83.3 %** — useful, but a tendency, **not an identity**.

🔴 **`AZ`'s budget line was survivorship-biased, and this is the correction a studio will feel.**
`AZ` told engagements to expect *"17 of 18 pins survive 24 h — a cheap minority repair, not a
re-verification campaign."* Over 496 unbiased pinnings: **67.3 % survive. A third of pins die
within 24 hours.** 🔵 The 18-pin sample was drawn from pins **already carried across passes**,
i.e. already selected for having survived.

### 🔴 And the metric `AZ` told you to stop using is in fact a good one — its refutation had the sign backwards

`AZ` published: *"Do NOT grade staleness by commit volume. It is refuted by measurement"*,
because `DeepTutor` (661 commits/30 d) and `frappe/lms` (571) each held their one pin.

| | `Pattern AZ` (n = 5, one pin each) | 🟢 `p448` (n = 36 repos × 14 pinnings) |
|---|---|---|
| commits/30 d vs 24-h stale rate | 🔴 claimed **negative** ("backwards") | 🟢 **Spearman ρ = +0.886** |

| repository | commits / 30 d | `AZ`'s single pin | 🟢 `p448` stale rate over 14 pinnings |
|---|---|---|---|
| `HKUDS/DeepTutor` | **661** | 🟢 held | 🔴 **50.0 %** |
| `frappe/lms` | **571** | 🟢 held | 🔴 **71.4 %** |
| `Apomera/AlloFlow` | 417 | 🔴 stale | 🔴 **85.7 %** |
| `vishalsachdev/canvas-mcp` | 373 | 🔴 stale | 🔴 **92.9 %** |
| `withmarbleapp/os-taxonomy` | 126 | 🟢 held | 🟡 **42.9 %** |
| `Citolab/qti-convert-python`, `LongsightGroup/qti3`, `GeovaneSchmitz/sigaa-api`, `ivmelo/suapbot`, `sebassg/sia-unal-mcp`, `r-huijts`/`mdweaver`/`caleb-media-studio` `canvas-mcp` | low | — | 🟢 **0.0 %** |

🔵 **`AZ` graded each repository on one coin flip and read the noise as the signal.** The two
busiest repositories did hold *that* pin; over fourteen pinnings each they are among the worst.

🟢 **And the two predictors are the same predictor.** commits/30 d vs **mean age-at-pin**:
**ρ = −0.852**. The busiest six repositories present HEADs **3.5–41.7 h** old; the quietest six
present HEADs **555 h to 80 196 h** old. 🔵 **Volume is a repo-level proxy; recency is the
mechanism.** Use recency — it is per-pin, it needs no history window, and it is one command.

### 🟢 Wiring it into an engagement

1. **At SOW / shelving time**, for every commit about to be quoted:
   ```bash
   git clone -q --filter=blob:none --no-checkout https://github.com/OWNER/REPO /tmp/pin && \
   git -C /tmp/pin show -s --format='pin=%h pinned_commit_date=%cI' HEAD && date -u +'now=%Y-%m-%dT%H:%M:%SZ'
   ```
2. **Age ≥ 7 days** → 🟢 cite the HEAD with its commit date beside it. **97.4 %** survival.
3. **Age < 7 days** → 🔴 do **not** put the HEAD in the deliverable. Cite the **grant payload
   cell** instead, and let the HEAD appear only as *"tree seen on `<date>`"*:
   ```bash
   curl -sS "https://raw.githubusercontent.com/OWNER/REPO/HEAD/LICENSE" -o /tmp/L && \
   printf '%s B · %s\n' "$(wc -c < /tmp/L)" "$(sha256sum /tmp/L | cut -c1-12)"
   ```
   🟢 **Why the cell is the safe anchor, measured twice:** `AlloFlow` moved
   `6194e51e8f1f` → `1499a80fd362` while its `LICENSE` stayed **35 442 B · `698099632698`** at
   both refs; and `openSIS`'s `docs/License.txt` re-read this pass is **17 286 B ·
   `224ac3d403e3`**, the published cell to the digit. **Trees move; grants do not.**
4. **Budget honestly.** 🔴 Expect **~33 %** of pins to need repair at 24 h, not 6 % — unless
   every pin cleared the 7-day gate, in which case **~3 %**. 🟢 The gate is the cheap half of
   this pattern; re-verification is the expensive half. Spend on the gate.
5. 🔴 **Never** grade staleness from stars or "last updated" badges (`Trend 46`). 🟡 And do not
   grade it from commit volume either — it *works* (ρ = +0.886) but it is a 30-day
   backward-looking window standing in for a number you can read directly off the commit.

🟡 **Calibration limits, stated rather than hidden:** 496 observations, but **36 repositories,
one industry, one host, one 14-day window**, and the 24-hour horizon is the only one measured —
nothing here calibrates a 1-week or 1-quarter pin → `Gap 448-D`.

---

## 🆕 Pattern AZ — `p447` **The pin-recency pre-flight: a 60-second check that tells you whether the commit you are about to put in a client deliverable will still be there on Monday — and why the metric you would reach for first (commit volume) gets it backwards**

🔵 **The problem this solves.** A studio engagement pins commits: in an SOW appendix, a
`requirements.txt`, a vendored submodule, a slide that says *"verified at `abc123`"*. `p446`
established that a pinned HEAD is a **timestamp, not an identity**. `p447` measured how fast
that timestamp rots, and the answer is **uneven in a way that is predictable** — but not by the
obvious metric.

### 🔴 Do NOT grade staleness by commit volume. It is refuted by measurement.

| repository | commits / 30 d | pin after ~24 h |
|---|---|---|
| `HKUDS/DeepTutor` | **661** | 🟢 still exact |
| `frappe/lms` | **571** | 🟢 still exact |
| `Apomera/AlloFlow` | 417 | 🔴 **stale** |
| `vishalsachdev/canvas-mcp` | 371 | 🔴 **stale — third HEAD in 24 h** |
| `withmarbleapp/os-taxonomy` | 126 | 🟢 still exact |

🔴 The **two busiest** repositories have the **most stable** pins. A 30-day count is
**backward-looking**: it counts a burst that has already ended. `DeepTutor` logged 661 commits
and then went quiet for **seven days**.

### 🟢 The check that works, and it is one command

```bash
# Is the commit I am about to pin on a MOVING tree or a SETTLED one?
git clone --quiet --filter=blob:none https://github.com/OWNER/REPO /tmp/pin && \
git -C /tmp/pin show -s --format='pinned_commit_date=%cI' HEAD && date -u +'now=%Y-%m-%dT%H:%M:%SZ'
```

**Read the gap between `pinned_commit_date` and `now`:**

| gap | tree state | what to do |
|---|---|---|
| **minutes–hours** | 🔴 **moving** — you are pinning mid-burst | Do **not** put the HEAD in the deliverable. Pin the **payload cell** instead |
| **days** | 🟢 **settled** | The pin will hold. Safe to quote with its date |

🟢 **Measured basis:** across the five repositories above, `pinned_commit_date == HEAD date`
**iff** the pin held. Both movers were pinned while the project was still committing —
`AlloFlow` pinned 10-24 12:35 with HEAD at 10-25 18:50; `canvas-mcp` pinned 19:41 with HEAD at
**20:06 the same evening**, stale **25 minutes** after the commit it names.

### 🟢 What to pin INSTEAD, when the tree is moving — and the evidence it is sound

Pin the **grant payload cell**, not the HEAD:

```bash
curl -sS "https://raw.githubusercontent.com/OWNER/REPO/HEAD/LICENSE" -o /tmp/L && \
printf '%s B · %s\n' "$(wc -c < /tmp/L)" "$(sha256sum /tmp/L | cut -c1-12)"
```

🟢 **Why this is safe, measured this pass:** `Apomera/AlloFlow` moved
`6194e51e8f1f` → `1499a80fd362`, and its `LICENSE` is **35 442 B · `698099632698`** at **both**
refs — reproducing a cell this base published **fourteen passes ago** at `p433`, to the digit.
🔵 **The tree moved; the grant did not.** A licence verdict anchored on the cell survives
exactly the churn that invalidates a HEAD.

### 🟢 Wiring it into an engagement

1. **At shelving / SOW time** — run the recency check. Record **pin + pinned-commit-date**, never the pin alone.
2. **Moving tree** → the deliverable cites the **payload cell**; the HEAD appears only as *"tree seen on <date>"*.
3. **Settled tree** → cite the HEAD, with its commit date beside it.
4. **Before any client re-read** — re-resolve with `git ls-remote <slug> HEAD`. 🟢 Budget realistically: **17 of 18** of this base's pins survived 24 h, so this is a **cheap minority repair**, not a re-verification campaign.
5. 🔴 **Never** infer staleness from stars, commit counts or "last updated" badges. `Trend 46` showed those channels over-count supply; this pattern shows they get **churn backwards** too.

🟡 **Calibration limit, stated rather than hidden:** the date axis is **n = 5**. The pin/no-pin
split is **n = 18**. Run it over all ~134 shelved repositories before treating the recency rule
as calibrated — `Gap 447-C`.

---

## 🆕 Pattern AY — `p446` **The lineage pre-flight: a 10-minute gate that runs BEFORE you tell a client how many options they have, because `Trend 46` says the shelf over-counts and `Gap 446-B` says the pin you quoted may already be stale**

🔵 **Why this pattern exists.** Two failures this base measured in one hour, both on the question
an engagement asks first:

- 🔴 **Over-count.** Ten Canvas/Moodle MCP addresses are **six** projects. Quoting ten is a
  credibility loss on the second call, when the client's own engineer runs one `git log`.
- 🔴 **Stale pin.** `vishalsachdev/canvas-mcp`'s HEAD advanced **while this base was measuring
  it**, and `krzysztofbury/librus-mcp` is a commit past the pin this base publishes.

🟢 **The pattern is the cheap check that prevents both**, and it needs no GitHub API — which
matters, because `api.github.com`, `github.com/search` and `codeload.github.com` are all **403**
from this base's host.

### 🟢 The recipe — concrete, with the repos and the commands

**Input:** the candidate address list off `agents/top.md` for the client's platform. Worked here
on the real Canvas/Moodle set.

**Step 1 — resolve, don't trust (≈1 s each).**
```
git ls-remote https://github.com/<owner>/<repo> HEAD
```
🔴 A failure here is a finding, not an error: `Gap 444-B`'s `dev-cucei-itrans/siiau-api-client`
is how a deleted repository presents. Record the sha **with the clock time**, because
`Gap 446-B` is a live hazard on an active repository.

**Step 2 — clone blobless and take the root commit (≈1 s each).**
```
git clone --filter=blob:none <url> ./<owner>~<repo>
git -C ./<owner>~<repo> rev-list --max-parents=0 HEAD    # the project identity
git -C ./<owner>~<repo> rev-list --count HEAD            # the maintenance signal
```
🟢 **Group by root commit. That is the option count.** Here: `afe32c3e1721` ×3,
`731aa116052b` ×2, four singletons → **6 projects, 10 addresses**.

**Step 3 — grade direction inside each group, by full history.**
```
git -C <A> remote add other <url-of-B> && git -C <A> fetch --filter=blob:none other
git -C <A> merge-base --is-ancestor <B-head> <A-head>   # 0 = B adds nothing
git -C <A> rev-list --count <B-head>..<A-head>          # how far behind B is
```
🟢 Take the descendant, **whoever owns it**: in ARM-2 the fork `mdweaver/canvas-mcp` is 4 ahead
of the root `r-huijts/canvas-mcp`.

**Step 4 — grade the grant on the payload cell, not the HEAD.**
```
git -C <d> ls-tree -r --name-only HEAD | grep -iE 'licen|copying'   # the WHOLE tree
git -C <d> cat-file -s HEAD:<path>                                   # bytes
git -C <d> cat-file blob HEAD:<path> | sha256sum | cut -c1-12        # the cell
```
🔴 **Enumerate the tree, never just the root** — `krzysztofbury/librus-mcp` is MIT at the root
and ships a complete **GPL-3.0** at `legacy_reference/LICENSE` (35 149 B · `3972dc9744f6`).
🟢 **sha256-first-12 over raw bytes** is this base's cell convention, validated this pass against
a published cell (`1 071 B · 22e7ab2dbddc`).

**Step 5 — read the upstream's own provenance file if it has one.**
🟢 `krzysztofbury/librus-mcp` ships `LICENSE_REVIEW.md` (9 662 B · `6905cca1f0b4`) with a locked
dependency licence inventory and an explicit scope limit: *"not an all-MIT standalone bundle."*
🔴 **That sentence disqualifies the delivery shape a studio defaults to** — one flattened
container or single-file binary — because `lxml`'s binary wheels can carry **LGPL-2.1 iconv**
and resources the upstream describes as unlicensed. Check it **before** the build review.

### 🟢 What it costs, and what it buys

| | |
|---|---|
| **cost** | ~1 s per repository for steps 1–2, a few minutes for a 10-address list; **no API keys, no GitHub API, no rate limit** |
| **buys** | the option count a client can verify; the address to actually take; a grant verdict over the whole tree; and the one sentence that stops a GPL subtree or an LGPL relink arriving in the shipped artefact |
| **when to run** | 🟢 **before the first scoping call**, and again before the build review — `Gap 446-B` means a pin older than an hour is a date, not an identity |

🔵 **Composes with `Pattern AX`** (the per-platform licence probe): `AX` answers *what does this
platform's supply cost*, `AY` answers *how many suppliers are there really, and which one do I
take*. Run `AY` first — it shrinks `AX`'s input set, here from ten addresses to six.


## 🆕 Pattern AX — `p445` **The per-platform licence probe: a two-hour gate that runs BEFORE you quote a system-of-record integration, because `Trend 45` says you cannot carry the last platform's answer to this one**

🔵 **Why this pattern exists.** This base has now published **three incompatible answers** to
*"what licence is the integration supply around an education system of record?"* — permissive
(`Trend 42`, 8 addresses), mostly-unlicensed (`Trend 43`, 37 addresses), uniformly GPL-3.0
(`p445`, 3 addresses on SIGAA). 🟢 **They are not in conflict; they are three platforms.**
`Trend 45`'s operational form is that the licence distribution is a property of the **platform's
developer community**, so it must be measured per platform and carried across neither regions
nor publisher classes. 🔴 **And `Trend 45` also kills the shortcut that was being used instead:**
publisher class does not predict grant presence (institutional 72.2 % against a 76.3 % baseline,
Fisher p = 0.558, n = 3 932), so *"it's a university, it'll be copyleft"* and *"it's official,
it'll be unlicensed"* are both unavailable.

### Step 1 — Get the platform's NAME, not the institution's (30 minutes, a conversation)

🔴 **This is the step that decides whether the pattern works**, and `p444` recorded walking
into the failure one leg after writing the rule down. Searching the **institution's name**
returns the institution's *teaching output*: `UNMSM` returned **884** coursework repositories;
`Ceibal` returned **238**, all coursework. Searching the **system of record's name** returns its
*integration surface*.

Ask the client: *"what system do your registrar and your students actually log into?"* Known
answers, from this base's own legs:

| country | system of record | this base's finding |
|---|---|---|
| Brazil (federal universities) | **SIGAA** | 🟡 supply exists, uniformly **GPL-3.0**, stale — `Pattern AY` |
| Brazil (federal institutes) | **SUAP** | 🔴 official clients **ungranted**; third-party MIT — `Pattern AW` |
| Argentina | **SIU Guaraní** | 🟢 one MCP server (`p443`) |
| Colombia | **SIA** (UNAL) | 🔴 MCP server exists, **NO GRANT** (`sebassg/sia-unal-mcp`) |
| Mexico (UANL) | **SIASE** | 6 addresses (`p444`) |
| Mexico (UdeG) | **SIIAU** | 🔴 **zero supply** — the one SDK's repository is deleted (`p445`) |
| Chile | **UCampus**, **U-Cursos** | 🟡 thin, and the top-starred hit is a **Chinese homonym** (`p444`) |
| Peru | SIAGIE, PUCP *Campus Virtual*, UNI *SIGA* | 🔴 **twice-nil on two channels** (`p444`, `p445`) |

⚠️ **Two traps this base paid for, apply both.** (1) **The homonym:** a 4–6 letter government
acronym is usually owned by an industrial or ML namespace — `SIMAT` returns **Siemens SIMATIC**,
`SAES` returns **sparse autoencoders**, `GURI` returns an oh-my-zsh theme. Check who operates
the platform, and read the top hit's **language**, before trusting a stars-sorted rank.
(2) **Ministry vs university:** university platforms accumulate third-party supply because the
blocked parties are students who can code; ministry-run K-12 systems do not (`p444`: 6 of 8
university legs paid, **0 of 5** ministry legs did).

### Step 2 — Enumerate the grant, do not read the badge (20 minutes, scripted)

```sh
cd compose/code/lib
. ./probe_payload.sh

# Existence + REAL default ref (never assume `main`: measured counter-examples include
# GibbonEdu/core -> v31.0.00, portabilis/i-educar -> 2.12).
git ls-remote --symref https://github.com/<owner>/<repo> HEAD

# EVERY licence path in the COMPLETE tree, each payload measured where it landed.
probe_repo_all <owner>/<repo>
```

🔴 **Use `probe_repo_all`, not the filename ladder, and not the registry.** Three defects this
base has measured, each of which this step closes:
* **The second grant below the root.** `krzysztofbury/librus-mcp` sells MIT at its root and
  ships complete **GPL-3.0** at `legacy_reference/LICENSE` (35 149 B) beside 20+ `.py` files.
  12 of 134 repositories carried more than one own-grant path; **4 carried more than one
  FAMILY** (`p442`).
* **The registry disagreeing with the payload, in the dangerous direction.**
  `macielti/sigaa-cli`'s PyPI `license` field is **EMPTY** while the repository ships a complete
  **GPL-3.0** payload (35 149 B) — so every registry-reading scanner reports a strongly-copyleft
  package as unlicensed (`p445`).
* **The name without the text.** `DMontgomery40/mcp-canvas-lms` says *"MIT License — see
  LICENSE file"* and ships no such file. That is an upstream **ask**, not a refusal, and must not
  be recorded as a bare absence.

### Step 3 — Compute the distribution and pick the shape (40 minutes)

Tabulate the addresses by family, then read the shape straight off it:

| what the distribution looks like | the shape to quote |
|---|---|
| 🟢 majority **MIT / Apache-2.0 / BSD**, maintained | **vendor it** — fork and extend, shortest path |
| 🟡 majority **GPL-3.0 / AGPL-3.0** | 🔴 **never vendor.** Reimplement against the interface these repos document, on a permissive base — the repos are *specification* (`Pattern AY`) |
| 🔴 majority **no grant at all** | **integrate over an interface you own**, use the licensed third-party client, and send a written licence request upstream (`Pattern AW`) |
| 🔴 **zero addresses** (SIIAU) | **price the integration from scratch** — and say so, because this is the case most often mistaken for "we'll find something" |

🟢 **The deliverable of this pattern is one slide:** the platform's name, the address count, the
family distribution with byte sizes and SHA prefixes, and which of the four shapes follows. It
is produced by `probe_repo_all` plus `lib/measure` and costs about two hours.

🔴 **And the rule that makes it worth running every time:** `Trend 45`'s falsifiable half says a
fourth platform should return a **fourth** distribution. Until two platforms in different
countries return the same one, **the previous engagement's answer has no predictive value for
this one.**

---

## 🆕 Pattern AY — `p445` **A Brazilian federal-university engagement on SIGAA, where the integration supply is real, documented, and GPL-3.0 — so the recipe is REIMPLEMENT, and the three repos are the specification**

🔵 **The situation this answers.** A client is a Brazilian federal university — UFPB, UFRN, UFMG
and the rest of the federal network run **SIGAA** (*Sistema Integrado de Gestão de Atividades
Acadêmicas*) as their system of record. `p443` opened this channel and `p445` measured it end to
end: **the supply exists, in two languages, with a working parser and a documented endpoint
shape — and all of it is GPL-3.0 and 6–10 years old.**

| address | grant, read first-hand 2026-10-25 | HEAD | what it gives you |
|---|---|---|---|
| [`fernandobrito/cursos_ufpb`](https://github.com/fernandobrito/cursos_ufpb) | 🟡 GPL-3.0 · 35 141 B · `cbdcf32a9188` | 2017-01-26 · 168 files | the **endpoint shape** (`/api/curricula`) and the `sigaa_parser` logic |
| [`macielti/sigaa-cli`](https://github.com/macielti/sigaa-cli) | 🟡 GPL-3.0 · 35 149 B · `85b9a51f5603` | 2020-01-04 · 25 files | the **auth flow against any SIGAA instance** by configurable base URL |
| [`fernandobrito/ufpb_sigaa_api_old`](https://github.com/fernandobrito/ufpb_sigaa_api_old) | 🟡 GPL-3.0 · 35 141 B · `4fa17f22c442` | 2016-02-07 · 14 files | the reference shape for "SIGAA behind an HTTP API" |

🔴 **Read the licence column before planning:** GPL-3.0 reaches a distributed derivative. These
three are **specification, not supply.** You read them, you do not ship them.

### The stack, every row verified first-hand on 2026-10-25

| layer | component | grant, measured | why this one |
|---|---|---|---|
| **1. SIGAA adapter** | 🔴 **write it** — a clean-room HTTP client over the auth flow and endpoints the three repos above document | 🟢 **yours** | SIGAA is JSF with **no public REST API**, so the adapter is unavoidable work. Reading GPL-3.0 code to learn an *interface* and writing your own client is the standard move; a lawyer signs off on the clean-room boundary, not an engineer |
| **2. MCP wrapper** | the adapter, exposed as an MCP server | 🟢 **yours** | 🟢 This is the step that makes the whole stack agent-addressable, and `p443`/`p444` show it is the shape that is *missing* in LATAM: `siu-guarani-mcp` exists for Argentina, `sia-unal-mcp` for Colombia carries **no grant**, and there is **nothing** for SIGAA. Build it once, reuse across the federal network |
| **3. LMS** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · `LICENSE` 10 982 B | 🟢 **The only Apache-2.0 full LMS in this base's platform tier.** Take it when the client cannot accept copyleft; take Moodle (GPL-3.0) only when they can and already run it |
| **4. LMS agent surface** | [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | 🟢 **MIT** · `LICENSE` 1 063 B · Go | Only if the client is on Moodle: courses, grades, assignments, deadlines over MCP, against any instance. 🔴 If on OpenOLAT, this layer is yours too |
| **5. Knowledge tracing** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** · `LICENSE` 1 066 B | The student model that makes layer 6 honest rather than a chatbot. Feed it the attendance and assessment history the layer-1 adapter pulls |
| **6. Tutor** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · `LICENSE` 11 408 B | Agent-native personalised tutoring with persistent per-student state; runs against local models via Ollama, which matters for a public university's data posture |

### Wiring

```
SIGAA (JSF, no public API)
   │  clean-room HTTP adapter  ← specification: the 3 GPL-3.0 repos (READ, never shipped)
   ▼
your SIGAA adapter ──► your MCP server ──┐
                                         ├──► DeepTutor (Apache-2.0)  ──► student
OpenOLAT (Apache-2.0) ──► MCP surface ───┤        ▲
                                         │        │
pykt-toolkit (MIT) ◄── enrolment, grades, attendance from the adapter
```

🟢 **Why the MCP server is the centre of gravity and not the tutor.** Every agent in layers 4–6
is replaceable; the **adapter plus MCP server over the system of record** is the asset, it is
reusable across every institution in the federal network that runs SIGAA, and it is the one
component for which no licensed supply exists anywhere in LATAM. Build it once, licence it as
you choose, and the tutor becomes a swap.

### 🔴 The two gates before any of this is quoted

1. **The access gate (`P26`), which no licence probe can answer.** A grant answers the
   *copyright* question only. *May we call this system?* lives in the university's own terms of
   use and its data-protection posture, and `p444`'s SIIAU and Chile legs both show student-built
   scrapers operating in exactly that grey zone. 🔴 Get written authorisation from the registrar
   before the adapter touches production; a scraper the students tolerate is not a contract the
   university has signed.
2. **Run `Pattern AX` first.** This recipe is correct for **SIGAA**, measured. 🔴 It is not
   transferable to the next platform — that is precisely what `Trend 45` says. One institution's
   SIGAA deployment may also differ in version and endpoints from UFPB's; the adapter is
   per-instance-configurable for that reason.

---

## 🆕 Pattern AW — `p444` **A licence-clean Brazilian Instituto Federal engagement: Moodle + SUAP + an AI layer, wired from rows verified 2026-10-25 — and the gate that stops you shipping the 49 % you cannot use**

🔵 **Why this pattern and not another tutor recipe.** `p443`'s `Pattern AV` answers *"how do you
find the repositories in a country whose supply this base has never shelved"*. `p444` ran that
move at four more countries and found the next problem: **the addresses exist and half of them
carry no licence**, including the officially-published ones. So `Pattern AW` is the step after
discovery — **turn a found tier into a stack you can actually quote** — and it is built on the
one LATAM ecosystem where every layer now has a verified row.

**Target:** an Instituto Federal (Brazil's federal vocational/technical network — SUAP is its
system of record, confirmed reusable across institutions). **Duration: 8–10 weeks.**

### 🔴 Step 0 — the licence gate, BEFORE the estimate

Run this before a single component is named in a proposal. It is not diligence hygiene; on this
tranche it eliminates **49 %** of candidates, so it changes the estimate.

```bash
# 1. every grant path at the probed HEAD, not just the root row  (p442)
compose/code/p1059-latam-name-channel/probe.sh slugs.txt out/
#    -> NO-GRANT-PATH in the `path` column means NO RIGHT OF USE.  Not "permissive by default".

# 2. does the README claim a DIFFERENT grant from the payload?    (p444, Gap 443-C)
python3 compose/code/p1060-readme-vs-payload/compare.py out/
#    -> README-MORE-PERMISSIVE is the expensive verdict: ipti/br.tag says BSD-3-Clause
#       in its `## Licença` section and ships GNU GPL v2.
```

🔴 **Two gate outputs are disqualifying, not negotiable:** `NO-GRANT-PATH` (no grant exists) and
`README-MORE-PERMISSIVE` (the grant you were told about is not the grant you get). 🟡 A third,
`NO-PAYLOAD` with a live claim, means *a licence was stated and never made* — treat as
disqualifying until the author fixes it, and see Step 4.

### 🟢 Step 1 — the system of record: integrate, do not fork

| layer | row | grant, read first-hand | why this one |
|---|---|---|---|
| system of record | **SUAP** · `suap.ifrn.edu.br` | 🔴 **source not published** | Holds enrolment, grades, attendance, materials. 🔴 **Not forkable** — the only access is its documented **OAuth2** API. Budget zero hosting and zero platform-licence risk; budget *total* API dependency. |
| 🟢 **authentication** | [`django-auth-suap`](https://github.com/django-by-kelsoncm/django-auth-suap) | 🟢 **MIT** · `LICENSE.md` 1 065 B · `113d1a85e628` · HEAD **2026-09-05** | 🟢 **The keystone row.** Django OAuth2 backend for SUAP: 98 `.py`, 92 `.rst` of Sphinx docs, on **PyPI** as `django-suap-auth`, CI + Codecov + pre-commit + `SECURITY.md`, Django **5.2/6.0**, with an `audit/` submodule (middleware, migrations, `audit_archive` command). |
| read seam (PHP) | [`ivmelo/suap-api-php`](https://github.com/ivmelo/suap-api-php) | 🟢 **MIT** · 1 071 B · `8dd4b842ad4d` | 34 ★, the most-starred *licensed* SUAP address. 🔴 HEAD 2021-04-13 — read it as the worked example of the API shape, re-implement against current endpoints. |
| read seam (Ruby) | [`luizpicolo/suap_api`](https://github.com/luizpicolo/suap_api) | 🟢 **MIT** · 1 078 B · `798df9e7634a` | 🔵 Written against **IFMS**, not IFRN — **this row is the evidence that a SUAP integration is reusable across institutes**, which is what makes the engagement repeatable rather than bespoke. |

🔴 **Do NOT use, and say so in the proposal:** [`IFRN/suapi`](https://github.com/IFRN/suapi)
(29 ★), [`ifrn-oficial/cliente_suap_django`](https://github.com/ifrn-oficial/cliente_suap_django)
(29 ★), [`ifrn-oficial/cliente_suap_javascript`](https://github.com/ifrn-oficial/cliente_suap_javascript)
(23 ★). **81 ★ of official, institutionally-maintained OAuth2 client, and not one carries a
grant file** — verified path-by-path this hour. They are the obvious choice and they are the
unusable one (`Trend 44`).

### 🟢 Step 2 — the LMS seam, where GPL-3.0 is the right answer

| layer | row | grant | why |
|---|---|---|---|
| LMS | **Moodle** | GPL-3.0 | Already this base's anchor LMS row; the *AVA* in Instituto Federal usage. |
| 🟢 **LMS↔SIS bridge** | [`moodle-local_suap`](https://github.com/suap-ava-suite/moodle-local_suap) | 🟡 **GPL-3.0** · `LICENSE` 35 161 B · `54b00c9ffd02` · HEAD **2026-10-19** | 🟢 **Live, 94 files, and it is the seam this base could previously only describe for EMEA.** GPL-3.0 here is **coherent, not a cost**: it is a Moodle `local` plugin and Moodle is already GPL-3.0, so the obligation is one the host platform imposes anyway. |

🔵 **The licence boundary of the whole stack, stated plainly:** everything *inside* Moodle is
GPL-3.0 and that is unavoidable and fine; everything on the **service side** (auth, API clients,
the AI layer) is MIT and stays separable. Keep the Moodle plugin a plugin — do not let
GPL-3.0 code cross into the service, and the boundary holds.

### 🟢 Step 3 — the AI layer, from rows already on these shelves

| role | row | grant | wiring |
|---|---|---|---|
| teacher-facing generation | [`GuilhermeScarpini/agente-bncc-professores`](https://github.com/GuilhermeScarpini/agente-bncc-professores) | 🟢 **MIT** | 🟢 **Brazilian curriculum-native**: lesson plans and assessments anchored to **BNCC** codes with a hallucination gate in the product. Feed it the class/subject identifiers that `django-auth-suap` + the SUAP API already resolve. |
| student-facing tutoring | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · `LICENSE` 11 408 B · `cd2f54e1e506` | Agent-native tutoring with persistent learner memory; scope it to the enrolled-subject list from SUAP so it never answers outside the student's actual courses. |
| offline / low-connectivity delivery | **Kolibri** | 🟢 **MIT** · 1 097 B · `3c056b34a476` | Offline-first with local models via Ollama — the row for *campi* and rural extension sites without reliable connectivity. |

🔴 **The EU AI Act scoping gate (`Pattern AP`) still applies even though this is Brazil**, the
moment the institution has European partners or EU-resident students: anything that profiles a
learner — and knowledge tracing does so by construction — cannot use the **Article 6(3)**
exception, and the Annex III deadline is **2 December 2027** (`Regulation (EU) 2026/1744`), while
the **AI-literacy and transparency duties are not deferred at all**.

### 🟢 Step 4 — the one-hour move nobody on this base has tried

🔴 18 of 37 addresses in this tranche are unusable only because nobody chose a licence — among
them an **MCP server** for a Colombian national university (`sebassg/sia-unal-mcp`, live,
TypeScript) and the three IFRN clients above. 🟢 **Open one issue per address asking the author
to add a licence.** It costs an hour, it is the cheapest possible supply expansion, and
`Gap 444-C` exists because no pass here has ever measured whether it works. 🔵 For an
institution-published repository, route it through the institution's open-source or IT
governance contact rather than the GitHub issue tracker — nobody *owns* the licence decision on
`IFRN/suapi`, which is exactly why it has none.

### 🔵 Weeks

| weeks | work |
|---|---|
| 1 | 🔴 **Step 0 gate** over every candidate; disqualify on `NO-GRANT-PATH` / `README-MORE-PERMISSIVE`; open the Step 4 issues immediately so answers arrive while you build |
| 2–3 | SUAP OAuth2 via `django-auth-suap`; the `audit/` submodule wired from day one (an education SIS integration is audited by default, not later) |
| 4–5 | `moodle-local_suap` deployed against the institution's Moodle; LMS↔SIS identity and enrolment reconciliation |
| 6–8 | AI layer: `agente-bncc-professores` for teachers, `DeepTutor` scoped to enrolled subjects; `Pattern AP` scoping gate recorded in writing |
| 9–10 | Kolibri offline delivery for low-connectivity sites; handover with the grant state of **every** component listed in the deliverable |

🔵 **The deliverable includes the licence table.** On this tranche the licence state is not
background paperwork — it decided which half of the ecosystem exists for the client, and the
official components lost.

---


## 🆕 Pattern AV — `p443` **Open a national education market in one day: name the platform, not the capability** — and the four-step engagement that follows, wired from rows verified 2026-10-25

🔵 `Pattern AU` (`p442`) clears **one repository** whose grant nobody here has read.
`Pattern AV` is the step before *that*: how you find the repositories at all in a country whose
supply this base has never shelved — and then what you build from them. It was derived by doing
it: LATAM went from **5 of 116** placed rows on [`agents/top.md`](../agents/top.md) to a shelved
tier in one pass.

### Step 0 — the discovery move, and it is one line

🔴 **Do not search for the capability.** Measured this pass as a controlled pair, same index,
same minute, same platform names, only the query shape differing:

| query | result |
|---|---|
| 🔴 `SIU-Guarani OR SIAGIE OR SIMAT OR SIGAA mcp OR api OR agent`, sort `updated` | 🔴 **10 addresses, zero education.** A proxy list, a TikTok uploader, a WoW raid analyst — the capability words dominated the match and the proper nouns contributed nothing |
| 🟢 `sigaa OR "siu guarani" OR siagie`, sort `stars` | 🟢 **792 matches; 7 of the first 10 were real academic-portal tooling** |

```
# the move, stated so it transfers to any country
#   1. ask the client (or a local) WHAT SYSTEM THE INSTITUTIONS ACTUALLY RUN
#   2. search that proper noun ALONE, sorted by stars
#   3. add NO capability words — they are what a general index is densest in, so they
#      drown a proper noun
#   4. then run `Pattern AU` on every address that comes back
```

🟢 **Why it works, and why this base missed it for 440 passes.** Its EMEA line exists because
somebody searched *Librus*, *IServ*, *Smartschool*, *EduPage*, *Skola24*, *DTU Learn*. Nobody
had typed *SIGAA* or *SIU Guaraní*. 🔴 Earlier passes ran **Spanish and Portuguese** legs and
concluded *"the language was the wrong variable"* — that conclusion was right, and it hid the
correct one for another forty passes. The variable is **the proper noun of the system of
record**, and it is language-independent.

🔴 **Before searching outward, `grep` inward.** Five of the six LATAM addresses this pass
shelved were **already in this base's own append-only record**, found by earlier passes and
promoted by none, and all six are absent from the promotion ledger (`Gap 443-A`). The first
query of any new-market pass is against `agents/trending.md` and `repos/trending.md`.

### Steps 1–4 — the engagement, wired from rows verified first-hand this pass

🔴 **The constraint that shapes everything below**, measured in this tranche: of the four LATAM
platforms that hold student records, **0 of 4 carry a permissive grant**; of the 8 student-side
portal addresses, **6 do** (`Trend 42`). So the AI goes **beside** the system of record, never
inside it.

```
┌─ 1 · READ SEAM (MIT — the part you own) ──────────────────────────────────────┐
│  Argentina  jpmanson/siu-guarani-mcp      MIT  1 074 B · 53d0fa710f43        │
│             17 stdio tools over perfil Docente; READ-ONLY by construction;   │
│             PII behind include_pii=True; GUARANI_BASE_URL per institution    │
│  Brazil     PucaVaz/sigaa-tools           MIT  1 065 B · 75d9af3e2e90        │
│             the most recently maintained SIGAA reader (HEAD 2026-10-20)      │
│             reference model: GeovaneSchmitz/sigaa-api (MIT, 🔴 ARCHIVED)      │
└───────────────────────────────┬──────────────────────────────────────────────┘
                               │  MCP / HTTP — an interface, never a fork
┌──────────────────────────────▼───────────────────────────────────────────────┐
│  2 · SYSTEM OF RECORD (copyleft — integrate, NEVER vendor)                   │
│     ipti/br.tag  🔴 GPL-2.0  18 027 B · 111e1f411730                         │
│     🔴 its README says BSD-3-Clause. THE PAYLOAD GOVERNS.                     │
│     Moodle (GPL-3.0) · Open edX (AGPL-3.0) · Chamilo (GPL-3.0, deep LATAM)   │
└──────────────────────────────┬───────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────────────────────┐
│  3 · AGENT + EVIDENCE (permissive, yours to ship)                            │
│     huggingface/smolagents  Apache-2.0  11 357 B · c71d239df917              │
│     pykt-team/pykt-toolkit  MIT         1 066 B · f5f955194636               │
│       -> the knowledge-tracing layer that makes "adaptive" defensible        │
│     learningequality/kolibri MIT        1 097 B · 3c056b34a476               │
│       -> offline-first; REQUIRED where connectivity is ~50% (India: 53.9%)   │
└──────────────────────────────┬───────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────────────────────┐
│  4 · HUMAN SIGN-OFF (not optional, and already implemented upstream)         │
│     littlecookie0722/AI-Teaching-Agent  MIT — WAITING_REVIEW task per        │
│       artefact, approve/reject recorded  (Pattern AH's shape, shipped)       │
│     kaushikgunasekaren/canvas-grader-mcp MIT — draft for human sign-off      │
│       BY DEFAULT                                                             │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Why step 4 is load-bearing rather than decorative

🟢 `siu-guarani-mcp` is already read-only **by construction** — its author inspected the
attendance, topic and grade-loading forms and **deliberately does not submit them**, leaving
writes on the roadmap. 🟢 That is not a limitation to engineer around; **it is the compliance
posture, free.** Keep it: let the agent draft and let a human commit, which is what EU Annex
III (education, applying **2 Dec 2027**), Vietnam's **Decision 33/2026/QĐ-TTg** high-risk
register and the US state policies on this base's `intel/policy-matrix.tsv` each ask for in
their own words.

### Sizing, and what it is based on

| phase | weeks | what it produces |
|---|---|---|
| 0 · name-the-platform discovery + inward `grep` | **<1** | the country's address list; this pass did Brazil + Argentina in one hour |
| 1 · read seam hardened (auth, rate limits, per-institution base URL, PII gate) | 2–3 | an MCP server a tutoring or advising agent can call |
| 2 · agent + knowledge-tracing evidence layer | 3–4 | an adaptive claim with `pykt` numbers behind it |
| 3 · sign-off workflow + offline tolerance | 2–3 | the artefact a regulator or a ministry asks for |
| **total** | **8–11** | |

🟡 **Bounds, stated rather than implied.** (a) Every connector row here is **unofficial** and
scrapes a portal, so an institutional agreement is a prerequisite — the copyright question is
answered by `Pattern AU`, the **access** question is `P26` and lives in the institution's terms,
not in any payload. (b) `siu-guarani-mcp` is **1 ★ / 6 commits / single author**: read it as the
reference implementation of the seam, not as a dependency — exactly as EMEA's connectors began.
(c) `GeovaneSchmitz/sigaa-api` is **archived and read-only**: it is the best SIGAA *model* in the
open and must not be a build dependency. (d) Step 0 is bought for **Brazil and Argentina only**;
Peru, Colombia, Chile, Mexico and Uruguay are an **unverified nil** (`Gap 443-B`).

---

## 🆕 Pattern AU — `p442` **Clear a repository's licence in four steps that cannot be done in the wrong order**, and the three repositories that each break a different one

🔵 `Pattern AT` (`p441`) clears a **stack** whose grants are already known. `Pattern AU` is the
step before it: the screen you run on a repository **nobody here has read yet**, built out of
this base's four existing instruments in the one order that works. Every component is in the
clone; nothing below is new code.

### The screen

```sh
# 0 · the repository resolves, and its DEFAULT BRANCH is read, never assumed
#     (measured: GibbonEdu/core -> v31.0.00, rosariosis -> mobile, i-educar -> 2.12)
. compose/code/lib/probe_payload.sh
probe_default_branch "$SLUG"

# 1 · ENUMERATE THE TREE.  A filename list can only FIND a licence; only enumeration can
#     say which payload is the grant, or that there is none (P441).
probe_repo_all "$SLUG"            # one row per licence text: path, bytes, family, holder
                                  # ~0.7 s; blobless depth-1 clone, no GitHub API needed

# 2 · FAMILY, from the hardened owner only.  Never re-answer it in a grader (P171).
lib/measure --family <payload>

# 3 · IS THE GRANT ACTUALLY THERE?  A pointer to a licence is not a grant (P1065).
python3 -I compose/code/p439-grant-presence/grant_presence.py --family "$FAM" <payload>
python3 -I compose/code/pass258-content-licence-family/content_licence.py <payload>  # CC/content

# 4 · publish the cell with the primitive, so the row cannot carry P834
lib/measure --cell <payload>      # -> `1 069 B · 262b47ee1fff`
```

🔴 **The order is the pattern.** Step 3 on step 1's *first* answer is what this base did for
441 passes, and it is wrong in both directions: on `ucbds-infra/ottr` the first answer is a
108 B stub that no clause profile can even grade, and on `24kchengYe/human-skill-tree` it is a
notice that makes a well-licensed project look unlicensed.

### The three repositories that break three different steps — each verified 2026-10-25

| step it breaks | repository | what happens without it | what the screen returns |
|---|---|---|---|
| **1 · enumerate** | [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | the ladder returns `LICENSE` **108 B**, family `UNCLASSIFIED` (R's `YEAR:` / `COPYRIGHT HOLDER:` stub) and stops | `LICENSE` 108 B `UNCLASSIFIED` **and** `LICENSE.md` **1 555 B · `1677c5307530`** → **BSD-3, `GRANT-PRESENT`** |
| **1 · enumerate (inverse)** | [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | the root payload (1 134 B · `3fb8cda58638`) grades `GRANT-BY-REFERENCE` → reads as *"project did not grant"* | the grant is at `app/LICENSE` **34 523 B · `0d96a4ff68ad`** (AGPL-3.0) **and** the root notice offers `skills/` under **AGPL-3.0 *or* MIT at the user's option** → a permissive lane |
| **1 · enumerate (subtree copyleft)** | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) | root is MIT 1 071 B · `22e7ab2dbddc`; the row reads *permissive, vendor freely* | 🔴 **GPL-3.0 at `legacy_reference/LICENSE`, 35 149 B · `3972dc9744f6`, `GRANT-PRESENT`**, beside 20+ `.py` files → **integrate over MCP, never vendor** |
| **3 · is the grant there** | [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | `LICENSE` 1 230 B is titled CC BY-SA 4.0 and *reads* like a grant | 🔴 `CONTENT-POINTER: not-a-grant` — the payload says *"This is a human-readable notice. The full legal terms are available at …/legalcode"*; the binding text is the canonical 18 375 B one |
| **4 · publish the cell** | this base's own shelves | 19 of 162 published cells carried the capture signature (`P834`) | `cell_of_file` owns the string; `make gate-cell-reproduction` reports **162/162** |

### What to hand a client's counsel

1. The `probe_repo_all` TSV for each component — **every** licence text in the tree, not the
   first one found, with bytes and `sha256₁₂` at a named commit.
2. The `grant_presence` verdict per payload, with the **profile** that judged it
   (`GRANT-PRESENT` / `GRANT-TRUNCATED` / `GRANT-BY-REFERENCE` / `GRANT-UNCALIBRATED`).
3. A one-line disposition per component: **vendor**, **integrate over an interface**, or
   **do not use** — and for a subtree-copyleft repository the disposition is a *boundary*,
   not a yes/no.
4. 🔴 The declared blind spots, because a screen that hides them is worse than none:
   **EUPL-1.2 has no clause profile here** (`Gap 442-C`), **LGPL needs a `GRANT-BY-DESIGN`
   verdict it does not have** (`Gap 440-B`), and **`*-assets/` is not on the vendored-path
   exclusion list**, so a vendored grant in such a directory is typed as the project's own
   (`Gap 442-B`).

### When to run it

🟢 On **every** component before it enters a proposal, and the cost says you can: 134
repositories enumerated in **33 s**, measured this pass. 🔵 Where the client is the one asking
(procurement, a counsel review, an OSPO), steps 1–3 are also the deliverable — a licence
report whose every figure reproduces from a named commit is worth more than a scanner's
summary, and it is the thing this base can hand over that a scanner cannot.

## 🆕 Pattern AT — `p441` The **autograded course stack that is entirely BSD-3, verified clause-by-clause**, and the three screening rules that stop it being badge-deep

🔵 `Pattern AS` (`p440`) maps the **copyleft** obligations a hosting choice triggers.
`Pattern AT` is its permissive counterpart and it is narrower on purpose: one stack, named
repositories, verified payloads, and a CI step a client's counsel can read. 🟢 Every
component below was probed first-hand on **2026-10-25** and graded `GRANT-PRESENT`
clause-by-clause — not from a badge, a README, or a package manifest.

### The stack

| layer | repository | licence, verified 2026-10-25 | why this one |
|---|---|---|---|
| LMS entry | [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 BSD-3 · `LICENSE` 1 528 B · `08eebd9662cb` | LTI 1.1/1.3 launch from Moodle, Canvas or Open edX — the client keeps its LMS |
| compute | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3 · 1 475 B · `7069c7e8d60e` 🔴 **untitled payload** | identical environment per cohort member |
| assignment lifecycle | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3 · 1 512 B · `3a83d5b8e22c` 🔴 **untitled payload** | release → collect → autograde → return, already solved |
| autograding (Python) | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 BSD-3 · `master/LICENSE` 1 560 B · `6af203d41a01` | container-isolated execution at Berkeley cohort scale |
| autograding (R) | [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | 🟢 BSD-3 · 🔴 **`LICENSE.md` 1 555 B · `1677c5307530`**, *not* the 108 B `LICENSE` | R scripts, R Markdown and R notebooks |
| tutor surface | [`QuantStack/jupyter-ai-tutor`](https://github.com/QuantStack/jupyter-ai-tutor) | 🟢 BSD-3 · 1 532 B · `ccaa70decf0d` | version-controlled `TUTOR.md` persona — the pedagogy stays a reviewable artefact (`Pattern X`) |
| model access | [`jupyterlab/jupyter-ai`](https://github.com/jupyterlab/jupyter-ai) | 🟢 BSD-3 · 1 516 B · `a0be5735cdce` | provider-agnostic LLM plumbing inside JupyterLab |
| offline arm | [`jupyterlite/jupyterlite`](https://github.com/jupyterlite/jupyterlite) | 🟢 BSD-3 · 1 525 B · `574f8a9cab1e` | kernel in the browser, no server — **the APAC answer**: India's Class 3–8 mandate lands on schools at 63.5 % connectivity |

🟢 **One licence family across eight components.** A single obligation set (retain the notice
in source, reproduce it in binaries, no endorsement) applies to the whole stack, and nothing
in it is network-triggered — so the hosting model is **not** constrained the way an AGPL
platform constrains it (`Pattern AS`).

### The wiring

1. **Entry.** `ltiauthenticator` as JupyterHub's authenticator; the LMS stays the roster and
   the gradebook of record. No student identity is minted in the new stack.
2. **Course build.** `nbgrader` owns the assignment source; `otter-grader` (Python) and
   `ottr` (R) own execution. 🔵 Pick one per language and let `nbgrader` call it — running
   both over one assignment doubles the container surface for nothing.
3. **Tutor.** `jupyter-ai` supplies model access; `jupyter-ai-tutor` supplies the persona as
   a committed `TUTOR.md`. 🟢 The persona is reviewed like code, which is what `Pattern X`
   and Arkansas `H.B. 1958`'s *named authorised human* both require.
4. **Offline.** Build the same notebooks into `jupyterlite` for low-bandwidth deployment.
   The autograder stays server-side; only delivery goes to the browser.

### 🔴 The three screening rules — each one a defect measured on this exact stack

1. **Pass the family in; do not read it off the title.** 🔴 Three of the eight payloads
   above carry **no title line at all**, so a title-keyed classifier answers `UNKNOWN` for
   `jupyterhub`, `nbgrader` and `open-tutor-ai-CE`. Take the family from a hardened
   classifier (`compose/code/lib/license_family.sh`) and hand it to the grant check:

   ```sh
   # the family from its hardened owner, the grant from the clauses
   python3 -I compose/code/p439-grant-presence/grant_presence.py \
       --family BSD path/to/LICENSE
   ```

2. **Enumerate the tree; never take the first filename-ladder hit.** 🔴 `ottr` is an R
   package: `DESCRIPTION` says `License: BSD_3_clause + file LICENSE`, so `LICENSE` holds
   **108 B** of `YEAR:` / `COPYRIGHT HOLDER:` and the licence **text** is at `LICENSE.md`.
   A ladder that stops at the first hit reports the most adopted R autograder in this
   industry as **ungranted**. `Gap 441-A`.

3. **`GRANT-PRESENT` is not `GRANT-UNMODIFIED`.** 🔴
   [`open-webui/open-webui`](https://github.com/open-webui/open-webui) — a tempting drop-in
   for the chat surface — is stock BSD-3 **plus a branding restriction plus a Contributor
   Licence Agreement** (2 819 B against ~1 515 B). Every clause is present, so it grades
   `GRANT-PRESENT` and is still **not** an OSI-standard BSD grant. Use `jupyter-ai` for this
   layer, or take `open-webui` with the restriction written into the SOW.

### The deliverable

Run the screen in the client's CI and **commit its output**, exactly as `Pattern AR` does for
the copyleft arm:

```sh
make bsd-variant-census > evidence/licence-verdicts.$(date +%F).tsv
```

🟢 That TSV is the artefact: one row per payload, with bytes, `sha256₁₂`, the variant profile
that judged it and the verdict. 🔵 It answers *"every third-party licence was READ, not
scanned"* with a reproducible measurement rather than an assurance — and for the three
untitled payloads it is the only thing that can.

## 🆕 Pattern AS — `p440` The **copyleft obligation map**: turn "which licence" into "which obligation, triggered by which deployment choice", before the hosting model is fixed

🔵 `Pattern AR` (`p439`) makes *"every third-party licence was READ, not scanned"* a CI
artefact. 🔴 It had a hole that was invisible until this pass: its grant-presence gate
could read MIT, Apache-2.0 and ISC, and **declined on the entire copyleft tier** — which
in education is the LMS, the SIS and the video layer, i.e. the parts the client cannot
replace. `Pattern AS` is the copyleft arm, and it is a **pre-architecture** deliverable:
run before the hosting model is chosen, because after that the obligation is already
incurred.

### The problem, stated the way a client experiences it

An education client picks a platform on features and TCO, hosts it, then modifies it.
🔴 Nothing in that sequence asks *whether the modification must be published*, and the
answer is decided entirely by a clause in a file nobody opened. Open edX and Moodle look
interchangeable on a feature matrix. They are not: one obliges a hosted deployment to
offer its users the Corresponding Source, and the other does not.

### The wiring — concrete, with the repos this base has verified

**1. Resolve the payload, not the badge.** `compose/code/lib/probe_payload.sh`,
**sourced, never re-implemented** (`set +u`, per `p436`). It resolves the default branch
with `ls-remote --symref` — 🔴 three of the ten platforms verified at `p440` are not on
`main` or `master` (`GibbonEdu/core` → `v31.0.00`, `portabilis/i-educar` → `2.12`,
`francoisjacquet/rosariosis` → `mobile`), and a hardcoded branch writes all three down as
ungranted.

**2. Grade the grant against its own licence VERSION.**
`compose/code/p439-grant-presence/grant_presence.py` with `p440`'s version-aware
profiles (`AGPL-3.0`, `GPL-3.0`, `GPL-2.0` alongside MIT / Apache-2.0 / ISC).
🔴 `resolve_version()` first: a complete GPL-2.0 licence is missing four of GPL-3.0's six
operative clauses, so grading the family instead of the version condemns a valid grant.
An unresolvable version returns `GRANT-UNCALIBRATED` — publish it, never suppress it.

**3. Map verdict → obligation → deployment trigger.** This is the deliverable:

| Grant | Trigger | What the client owes | Platforms (verified 2026-10-25) |
|---|---|---|---|
| **MIT / Apache-2.0 / BSD** | — | attribution; Apache-2.0 §4(a) also a **copy of the licence** | `openedx/XBlock`, `huggingface/smolagents`, `learningequality/kolibri` |
| **GPL-2.0** | **distribution** of binaries | complete corresponding source to recipients. 🟢 **No network clause — it predates the question** | `portabilis/i-educar`, `francoisjacquet/rosariosis`, `OS4ED/openSIS-Classic` |
| **GPL-3.0** | **distribution** | corresponding source; anti-tivoisation | `moodle/moodle`, `chamilo/chamilo-lms`, `GibbonEdu/core` |
| 🔴 **AGPL-3.0** | **network interaction** (§13) | modified version's Corresponding Source offered **to the platform's own users** | `openedx/edx-platform`, `instructure/canvas-lms`, `frappe/lms`, `Chocobozzz/PeerTube` |
| 🟡 **LGPL-3.0** | — | 🔴 **not assessed** — incorporation by reference by design (`Gap 440-B`) | `BigBlueButton`, `OpenEduCat` |

**4. Place the AI work on the permissive side of the seam.** The whole point of the map
is that it tells you where to stand. On an AGPL platform, build **through the supported
extension point** rather than in the core: [`openedx/XBlock`](https://github.com/openedx/XBlock)
(Apache-2.0, `LICENSE.TXT` 11 358 B · `cfc7749b96f6`) is the Open edX seam, and the
agents this base shelves — `canvas-grader-mcp`, `littlecookie0722/AI-Teaching-Agent`,
`ls1intum/edutelligence` — are all MIT services that integrate **over an interface**.
🟢 Nothing the studio writes inherits §13.

**5. Ship the third column.** The report has **three** columns — verdict, the clauses
actually found, and what was **not assessed and why**. 🔴 A two-column report renders
"unknown" and "fine" identically (`Trend 38`), and the uncalibrated rows are exactly the
ones with the largest obligations attached.

### What it is worth, and where

🟢 **LATAM is the unexpected winner and the pitch nobody makes.** The region's SIS tier is
**GPL-2.0** — no §13, so a hosted deployment triggers no source-offer obligation to its
users. That is a real, defensible hosting advantage for `i-Educar`, `RosarioSIS` and
`openSIS`, and it is invisible to any tool that grades "GPL" as one thing.
🔵 **EMEA**: GPL-3.0 on Moodle/Chamilo keeps copyleft off the hosting model, which
composes cleanly with the 2 December 2027 Annex III runway (`Pattern AP`).
🔴 **NA and APAC** are the exposed ones — Canvas and Open edX are AGPL — and there the
XBlock/interface seam is the engagement, not a detail.

**Sizing.** 2–3 weeks for a platform estate of this size: ~1 week probing and grading,
~1 week mapping obligations to the client's actual hosting and modification plan, ~1 week
wiring the gate into CI as `Pattern AR` specifies. 🟡 It is cheap because the instruments
exist; it is valuable because it runs **before** the architecture is fixed.

---

## 🆕 Pattern AR — `p439` The **grant-presence gate in the build**: make "every third-party licence was READ, not scanned" a CI artefact, and wire the same gate a client's procurement can run

🔵 **The problem this pattern solves, measured rather than asserted.** `Pattern AQ` (`p438`)
made component clearance an auditable build artefact. 🔴 `p439` found the hole in exactly that
artefact: a licence **scan** passes a payload that contains no grant. Live specimen from
education supply, read 2026-10-25:
[`spragginsdesigns/ai-tutor-webapp`](https://github.com/spragginsdesigns/ai-tutor-webapp),
`LICENSE` **552 B** · `sha256₁₂ 5809eb2eab28`, titled Apache-2.0, holder 🔴 **Vercel, Inc.**,
licence text **not in the repository**. Every instrument on this base graded it
`PERMISSIVE / stock = True / needs_a_human = False`. A clearance report built on a scanner
would have shipped it green.

### The recipe — concrete repos, concrete wiring

🔵 **And the reason this is a pattern rather than a tip**: the principle is old and keeps not
travelling. `P1065` on this base settled in pass 254 that a pointer to a licence is not a
grant; the predicate was implemented for **Creative Commons content licences** and never
reached the instruments that grade MIT, Apache-2.0 and BSD. 🔴 In a client pipeline the same
thing happens by default — the rule lands in whichever scanner surfaced the problem, not in
the one that writes the verdict. **Wire it where the verdict is written.**

**1. The gate itself (build it once, ~1 day).**
[`compose/code/p439-grant-presence/`](./code/p439-grant-presence) in this base is the working
reference: `grant_presence.py` classifies a payload into **GRANT-PRESENT /
GRANT-BY-REFERENCE / GRANT-TRUNCATED / GRANT-UNCALIBRATED** by asking whether the family's
**operative clauses** are present, with 19 controls in `test_grant_presence.py`.

```
make gate-grant-presence     # controls, offline, committed fixtures — CAN go red
make grant-presence-census   # the live dependency set — a MEASUREMENT, always exits 0
```

🔵 **Keep that split in the client's pipeline too.** The controls block a merge; the
population only reports. A gate that goes red because the *dependency set* changed teaches a
team to disable the gate — this base learned that twice (`Gap 435-A`, `Gap 438-B`) and both
times the remedy was the same split.

**2. Wire it where the payloads already arrive.** Compose it with what this base already
carries rather than building a new scanner:

| Stage | Component | Grant | Role |
|---|---|---|---|
| Resolve branch + fetch payload | [`lib/probe_payload.sh`](./code/lib) (this base) | — | `ls-remote --symref` so a non-`main` default (`master`, `develop`, `v31.0.00`) is never read as *ungranted*; README-link rung before the filename ladder |
| Family, by title block | [`lib/license_family.sh`](./code/lib) (this base) | — | `P171`: classify by **title block**, never body substring — GPL-3.0 §13 is titled with AGPL's name |
| 🆕 **Grant presence, by clause** | `p439-grant-presence` | — | the new rung: is the granting text actually here? |
| Orchestrate per dependency | [`temporalio/temporal`](https://github.com/temporalio/temporal) | MIT | one durable workflow per component; retries and the full read history survive a crash |
| Surface the report | [`appsmith`](https://github.com/appsmithorg/appsmith) | Apache-2.0 | the procurement-facing view: filter to `GRANT-BY-REFERENCE` + `GRANT-TRUNCATED` |
| Model indirection (APAC) | [`BerriAI/litellm`](https://github.com/BerriAI/litellm) | MIT | only if the pipeline summarises clauses with an LLM — keeps sovereign models swappable |

**3. The three rungs, in this order, and the order is the whole pattern.**

```
exists?            git ls-remote            -> UNRESOLVED is not "ungranted"
what is it called? family_of (title block)  -> P171
🆕 is it HERE?     grant_presence.classify  -> Gap 439-A
```

**4. The two negative controls to copy, because they are defects this base actually had.**

- 🔴 **Do not key on "the payload says the licence is elsewhere."** That phrase appears
  **verbatim inside the full Apache-2.0 text** — the APPENDIX is part of the licence. Measured:
  the 11 357 B full text carries **all three** reference markers. Ask clauses **first**; let
  the markers only separate `TRUNCATED` from `BY-REFERENCE`.
- 🔴 **Fold typographic quotes before matching anything.** A complete MIT licence that
  typesets “AS IS” with U+201C/U+201D was graded `GRANT-TRUNCATED` by this instrument's first
  draft — a real grant condemned by a punctuation character.
- 🔴 **And do not substitute a byte floor.** BSD stock payloads span **221 B → 1 514 B** on
  this base's corpus, because BSD-0/2/3 are three lengths under one family name.

**5. What ships to the client.** Per-component: slug, resolved default branch, payload path,
bytes, `sha256₁₂`, HEAD SHA, family, **grant verdict**, and for anything not `GRANT-PRESENT`
the **named missing clauses**. 🟢 The two obligations this catches and a scanner cannot —
Apache-2.0 **§4(a)**'s duty to supply a copy of the License, and MIT's notice obligation
against a holder that resolves to nobody — are both *integrator* duties, which is precisely
why they must be found before delivery and not after.

**Effort:** ~1 day for the gate against an existing clearance pipeline (this base's reference
is ~300 lines plus 19 controls); **2–3 weeks** to stand up the whole chain from nothing.
🟡 **Where it pays**: any engagement that **vendors or redistributes** third-party components —
an LMS platform build, a white-labelled tutor, anything shipped to a public-sector buyer. For
a system the client only *calls* over a network, this ranks below `P26` (the access-rights
question, which lives in a Terms of Use and not in a licence).

---

## 🆕 Pattern AQ — `p438` The **component-clearance gate**: make "every third-party part of this stack was read, not scanned" a build artefact the client can audit

🔵 **The engagement this answers.** Any education build that assembles AI components — which
is all of them now. The client's procurement function will ask *"is this open-source stack
clean?"*, their counsel will ask it again at renewal, and the honest answer today is a
scanner report that prints one SPDX identifier per file. 🔴 `p438` measured what that report
misses on this base's own corpus: **9 of 238** committed licence payloads carry an addition
the family column does not describe, and **7 of those 9** are routed by
`bespoke_census.needs_a_human()` as needing **no** human read — `p427`'s own two-family
specimen among them. 🔴 One of the nine addresses this pass graded (**11 %**) carried a
clause, in Chinese, pushing content-copyright liability onto the operator. **On an education
engagement the operator is the school and the content is textbooks.**

🟢 **What makes this sellable rather than hygiene**: the output is not a policy document, it
is a **CI job that fails the build**, plus a signed per-component ledger. The client is buying
the evidence, and the evidence is cheap because the instruments already exist.

### 🟢 Step 1 — resolve each component's real address and grant (do not trust a badge)

Use this base's own probe, **sourced, never re-implemented** — the rule is in
`compose/code/lib/README.md` and has been broken twice on this base:

```bash
set +u                                     # the library needs it; p436 measured why
. compose/code/lib/probe_payload.sh
probe_repo <owner/repo>                    # -> repo, branch, file, bytes, family, holder
```

🔴 Three traps it closes, each measured on real education repositories, not hypothesised:
the default branch is often **not** `main` (`GibbonEdu/core` → `v31.0.00`,
`francoisjacquet/rosariosis` → `mobile`, and this pass's own `eugeniughelbur/doceo` →
`master`); the payload can live in a **subdirectory**; and British `LICENCE` exists in the
wild.

### 🟢 Step 2 — grade the payload on **three** columns, not one

```bash
make bespoke-census PAYLOADS="/path/to/LICENSE"
```

Fail the component into human review when **any** of these holds:

| column | fail condition | why |
|---|---|---|
| `titled_family` | not in {MIT, Apache-2.0, BSD-2/3-Clause, ISC} | the ordinary licence screen |
| `p1054_verdict` | contains an **addition** (e.g. `MIT-BODY-PLUS:unclassified-addition`) | 🔴 **the column `needs_a_human` ignores** — this is the step that is new |
| payload bytes | outside the family's stock band (MIT clusters at **1 055–1 079 B** on these shelves) | the band detects *that* a payload was modified; only a person learns *what* the modification says |

🔴 **Do not substitute `needs_a_human` for this table until `Gap 438-A` is discharged.** On
`p438`'s specimen it returns `no` while the row beside it says `unclassified-addition`.

### 🟢 Step 3 — read the surplus bytes **in their own language**

`p427`'s `conjunctive_grant.classify()` is the right second instrument and returns
`scope: None` here, because its `SCOPE_MARKERS` (`compose/code/p427-conjunctive-grant/conjunctive_grant.py:73`)
are English: `portions of`, `derived from`, `remain under`, `original license`, `third-party`.
🟢 **So the surplus goes to a human with the language named**, and the question put to them is
fixed and answerable in two minutes: *does this clause (a) add a notice obligation, (b) narrow
the subject matter of the grant, or (c) move a liability onto the operator?* 🔵 `p438`'s
specimen is **(b) and (c)**: the repository ships no book content, and the operator carries the
copyright liability for the material it is pointed at.

### 🟢 Step 4 — wire it as a gate and keep the ledger

One job in the client's CI, one TSV in the repository: `component, address, branch, file,
bytes, sha256₁₂, family, addition_verdict, human_read_by, date`. 🟢 `p436`'s ledger lesson
applies and is why the ledger is the artefact: **a claim with no committed row is a claim that
disappears at the next rewrite** — that pass found **176** addresses claimed promoted with no
live row behind them.

### 🟢 A concrete stack this runs over, every row already cleared first-hand on these shelves

| layer | component | grant |
|---|---|---|
| tutoring core | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0, `LICENSE` 11 408 B |
| learner modelling | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT, `LICENSE` 1 066 B |
| LMS seam (no AGPL contact) | [openedx/XBlock](https://github.com/openedx/XBlock) | Apache-2.0, `LICENSE.TXT` 11 358 B |
| offline delivery | [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT |
| pedagogy layer | [smashburger-dev/socratic-workshop](https://github.com/smashburger-dev/socratic-workshop) | MIT, `LICENSE` 1 072 B · `7f3dec641d9f` |
| learner-memory skill | [briannajzhang/personal-tutor](https://github.com/briannajzhang/personal-tutor) | Apache-2.0, `LICENSE` 11 357 B · `c71d239df917` |
| obligation check | [tomdxb0004/eu-ai-act-risk-checker](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | MIT — 🟢 the **post-Omnibus-correct** one per `p437`; `engine.js:32` encodes `2027-12-02` |

🔴 **And one row that this gate is the reason you can still use**:
[fangyuan-3149/book-learning-tutor](https://github.com/fangyuan-3149/book-learning-tutor)
(MIT, `LICENSE` 1 503 B · `54ceeac19921`). Cleared by a scanner, cleared by `needs_a_human`,
and it belongs in a build **only** with its clause in the statement of work. 🟢 Step 3 is what
turns it from a hidden liability into a priced one.

### 🔵 Price and where it goes in the engagement

**2–3 weeks** for the job, the ledger and the first full sweep of an existing estate, then
minutes per new component. 🟢 Sell it as the first phase of any education build and as a
stand-alone diligence piece into an estate someone else assembled — `Pattern AP`'s scoping
gate decides *whether* the product is high-risk; this one decides *whether its parts can be
shipped at all*, and the two are sold together.


## 🆕 Pattern AP — `p437` The **Article 6(3) scoping gate**: decide whether the client's adaptive-learning product is high-risk *before* writing the architecture

🔵 **The engagement this answers.** A client wants adaptive learning, knowledge tracing or
automated grading in the EU. The pitch everyone makes is *"Annex III moved to December 2027,
you have fourteen months"*. 🔴 **That framing loses the engagement**, because it answers the
wrong question. Two things are already true today, and one of them decides the entire
architecture:

| question | answer | when it bites |
|---|---|---|
| Is the product **prohibited**? | Emotion recognition in educational institutions is banned outright, Art. 5(1)(f), narrow medical/safety exception | 🔴 **Since 2 February 2025 — live now** |
| Does it owe **transparency**? | Art. 50: disclose AI interaction, machine-readable marking of synthetic output | 🔴 **Since 2 August 2026 — live now** |
| Is it **high-risk**? | Annex III point 3 — admission, evaluating learning outcomes, level determination, proctoring | 🟡 2 December 2027 |
| 🔵 Can it **escape** high-risk via Art. 6(3)? | Only if it meets one of (a)–(d), poses no significant risk, **and does not profile natural persons** | Decided at design time |

### 🔴 The gate, and why most education AI fails it

Article 6(3) is the only exit from Annex III classification, and the profiling condition
closes it for the architectures this base recommends most. **Knowledge tracing is profiling.**
`pykt-team/pykt-toolkit` (DKT/SAKT/BKT) and `CAHLR/OATutor` (Bayesian Knowledge Tracing), both
on the `agents/top.md` build-on tier, construct a per-learner model of a natural person in
order to work. So:

> 🔴 **If the product adapts to the individual learner, it profiles, the Art. 6(3) exception is
> unavailable, and it is high-risk — full Art. 9–15 obligations.** There is no architecture
> that keeps the adaptivity and sheds the classification.

🟢 **This is good news for the engagement, not bad.** It converts a vague compliance worry
into a fixed, quotable scope of work with a statutory deadline, and it disqualifies competitors
pitching "lightweight" adaptive learning that quietly assumes the exception applies.

### The stack, every grant read first-hand at HEAD on 2026-10-25

| Layer | Component | Grant (payload read first-hand) |
|---|---|---|
| **Scoping decision** | [`tomdxb0004/eu-ai-act-risk-checker`](https://github.com/tomdxb0004/eu-ai-act-risk-checker) — `engine.js:170-186` implements (a)–(d) + the profiling override | 🟢 **MIT** · 1 073 B · `b7b08f330649` @ `41da87feb238` |
| **Annex IV technical documentation** | [`Hiepler/EuConform`](https://github.com/Hiepler/EuConform) — report generator + CrowS-Pairs bias evaluation | 🟢 **MIT** · 1 073 B · `65335056589f` @ `011a5ad9bea2` |
| **Annex III checklist / agent controls** | [`microsoft/agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit) | 🟢 **MIT** · 1 074 B · `7df20dcdf919` @ `70a4ab8e8a04` |
| **Codebase scan** (not dates) | [`ark-forge/mcp-eu-ai-act`](https://github.com/ark-forge/mcp-eu-ai-act) | 🔴 **MIT** · 1 065 B · `002af8f9b59c` — dates superseded, scanning only |
| **The modelling layer being classified** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) · [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** · 1 066 B · `f5f955194636` / 1 105 B · `5baaaf977a28` |
| **Bias / fairness evidence for Art. 10** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) standard datasets + EuConform bias eval | 🟢 **MIT** |

### How it wires together

1. **Run the scoping decision first, before any model choice.** Open `index.html` from
   `eu-ai-act-risk-checker` (no build step, no backend). Answer as the *provider*. Record the
   tier, the article list and the per-obligation dates it returns, with its citations — this
   becomes the engagement's scoping memo.
2. **Force the profiling question explicitly.** If the product adapts per learner, set
   `profiling = true`. 🔴 Expect `profilingOverride` to fire and the Art. 6(3) exception to
   close. Do not let an optimistic reading of (a)–(d) survive this step; `engine.js:172`
   is the executable version of the rule.
3. **Gate the tool before you trust it** — three greps, because two of the five permissive
   EU-AI-Act tools on these shelves encode the superseded deadline:
   ```bash
   grep -rn '1744'                         # must match
   grep -rn '2027-12-02\|2 December 2027'  # must match
   grep -rn '2026-08-02\|2 August 2026'    # must NOT be a high-risk deadline
   ```
4. **Generate Annex IV documentation from the start.** EuConform's report generator produces
   the technical-documentation shape Art. 11/Annex IV expects. Building it at design time is
   the whole value of the December 2027 runway; retrofitting it is the thing clients pay
   double for later.
5. **Attach Art. 10 data-governance evidence to the modelling layer.** Run the bias
   evaluation over the knowledge-tracing datasets *as a CI artefact*, not a one-off report,
   so the evidence regenerates with every model change.
6. **Settle the two live obligations before go-live, not before the deadline.** Strip or
   never build emotion/affect inference (Art. 5(1)(f), prohibited since February 2025), and
   wire Art. 50 disclosure and synthetic-output marking now — both already apply.

🔵 **What this pattern deliberately does not claim.** None of these tools is legal advice, and
`eu-ai-act-risk-checker`'s own README says several conditions turn on judgements it cannot
make — significant harm, significant risk, whether AI use is obvious. The gate produces a
**defensible, cited scoping position** for counsel to sign off, which is the deliverable;
it does not replace the sign-off.

## 🆕 Pattern AO — `p436` The **assessment-interoperability** engagement: parametric items a client can author, deliver and prove, with no copyleft anywhere in the chain

🔵 **The engagement this answers.** A client with a real examination obligation — a ministry, a
board, a university consortium — needs items that are *generated per learner* (so they cannot be
shared), *delivered in a standard the regulator recognises*, and *provable after the fact*. Until
`p436` this chain could not be assembled from this base's live shelves at all: the repository it
depends on had been silently deleted.

🟢 **The stack, every grant re-read first-hand on 2026-10-25, every licence permissive:**

| layer | component | licence | why this one |
|---|---|---|---|
| 1 · author | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) `packages/core` | **MIT** `1 072` B · `00ed05b90bf8` | the only readable implementation of `qti-template-declaration` / `qti-template-processing` with a real `randomInteger` draw over min/max/step and a constraint-retry loop |
| 1b · emit | `compose/code/p533-qti3-template-emitter/` (this tree) | — | 🟢 the `Gap 238` artefact: regenerates two upstream fixtures **node-for-node**, 43 assertions, 11 of 11 mutations detected. 🔴 `qti3`'s **writer** cannot emit these elements — this is the workaround, and `Gap 240` is to contribute it upstream |
| 2 · render | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | **MIT** `1 076` B · `7faa621251d7` | QTI 3 item rendering |
| 3 · deliver | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | **BSD-3-Clause** `2 058` B · `a5c692f12090` | QTI 2.1 delivery, **JQTI+** and **MathAssess** for mathematical response processing; live to 2026-06-30 |
| 3b · PHP estate | [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | **MIT** `1 066` B · `27fb6d463569` | the route in when the estate is PHP (i.e. Moodle); published by the **Dutch national education-ICT body** |
| 4 · roster | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | **Apache-2.0** `10 173` B · `a6cba85bc92e` | OneRoster 1.2 over an Ed-Fi ODS — who sits the exam, without touching the SIS |
| 5 · connect | the restored LMS-connector tier on [`agents/top.md`](../agents/top.md) | **MIT / ISC** | push items and pull submissions from the LMS the client already runs (Canvas, Moodle, Blackboard, Classroom) |
| 6 · sign-off | `kaushikgunasekaren/canvas-grader-mcp` (already shelved) | **MIT** | **draft-for-human-sign-off by default** — the staged artefact EU, Vietnamese and US-state oversight rules all require |

### How it wires together

1. 🟢 **Author one template, not N items.** Hand-author the template XML from
   `qti3`'s `packages/fixtures/xml/random-integer-template-reference.xml` (~35 lines), **or** run
   the `p533` emitter to generate it. 🔴 **Do not plan on `qti3`'s `writer` package** — it has
   **0 of 33** exports for these elements (`Gap 39`, refuted for authoring).
2. 🟢 **Let `core` execute the draw.** It parses the declaration, draws over the declared grid,
   derives the answer key **from the draw**, and retries up to 100 times against constraints. The
   per-learner variant and its key are produced by the same pass — which is what makes the result
   defensible.
3. 🟢 **Validate transitively, not by assertion.** The emitter's output matches the fixtures
   `qti3`'s own schema gate validates against the sha256-pinned official ASI schema, so validity
   is inherited. 🔴 **Stated limit**: the official XSD could not be fetched here
   (`purl.imsglobal.org` proxy-blocked, `Gap 56` class), and `qti3`'s suite was **not executed** —
   installing a third-party repository's dependencies is not permitted in this environment.
4. 🟢 **Render and deliver** through layer 2/3, or 3b for a PHP estate.
5. 🟢 **Resolve cohort from layer 4**, so the exam roster is the SIS's answer and not a copy.
6. 🟢 **Return results through layer 5, and gate every grade through layer 6.** Nothing writes a
   grade without a human action.

### Why the licences matter here specifically

🟢 **There is no copyleft anywhere in the chain** — MIT, MIT, MIT, BSD-3-Clause, MIT, Apache-2.0.
🔵 That is unusual on this base and it is the point: the assessment boundary is the one tier where
a client most often needs to **ship a modified binary to a ministry** without publishing it, and
the AGPL platform tier (Open edX, Moodle's GPL) cannot be the carrier for that.

### Cost, and what would sink it

🟡 **Realistic shape: 8–10 weeks** — 2 to wire author→render→deliver on the fixtures, 2 for the
roster seam, 2 for the LMS connector, 2–4 for the sign-off path and the audit trail.
🔴 **What would sink it**: (a) `qti3`'s suite has **never been executed in this environment**, so
first-week work is standing the upstream suite up on a real checkout; (b) `amp-up-io`'s HEAD is
**2025-06-21** — the only stale link in the chain, and the one to re-check before committing;
(c) if the regulator requires QTI **3** delivery rather than 2.1, layer 3 does not satisfy it and
the chain is authoring-and-rendering only.

🔴 **Provenance warning, because this pattern is the reason it matters**: four of these six
components were **off every live shelf until `p436` restored them**, while `Gap 240` stayed open
pointing at one of them. 🟢 `gate-promotion-ledger`'s `C3` control now fails if any of them is
dropped again.

# 🧩 Compose patterns — Education

> Concrete recipes: named repos, named licences, and how they wire together.
> Every component below was licence-verified at a commit SHA on 2026-10-25.

## 🆕 Pattern AN — `p435` The **national school-platform connector** engagement: the EMEA build that does not ask the client to replace anything

🔵 **The engagement this base could not describe until now.** Every platform pattern here
starts by choosing a base — OpenOLAT or Kolibri if the client cannot take copyleft, Moodle
or Open edX if it can. 🔴 **A national school system is not going to migrate.** IServ runs
German state schools, Librus Synergia runs Polish gradebooks, Smartschool runs Flanders,
EduPage runs Slovakia, Skola24 runs Swedish timetables. The buyable engagement is a
**permissive agent layer over the incumbent**, and `p435`'s grade census of this base's own
backlog finally produced the addresses for it.

### The stack, with the grant on every piece — all read first-hand at HEAD on 2026-10-25

| Layer | Component | Grant (payload read first-hand) |
|---|---|---|
| **Platform connector** (pick the client's) | [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) 🇩🇪 · [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) 🇵🇱 · [`MauroDruwel/Smartschool-MCP`](https://github.com/MauroDruwel/Smartschool-MCP) 🇧🇪 · [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) 🇸🇰 · [`CarlSvejstrup/dtu-learn-mcp`](https://github.com/CarlSvejstrup/dtu-learn-mcp) 🇩🇰 · [`Kretiandpleti/skola-24-haos-integration`](https://github.com/Kretiandpleti/skola-24-haos-integration) 🇸🇪 | 🟢 **MIT** · 1 069–1 090 B · digests in `agents/top.md` |
| **Registry / reference data** | [`DFE-Digital/get-information-about-schools`](https://github.com/DFE-Digital/get-information-about-schools) 🇬🇧 · [`hyunbinseo/neis-school-info`](https://github.com/hyunbinseo/neis-school-info) 🇰🇷 | 🟢 **MIT** · `LICENCE` 1 116 B · `e18299fd1942` / 1 068 B · `e82e1769aaaf` |
| **Curriculum authority** | [`oaknational/oak-curriculum-api`](https://github.com/oaknational/oak-curriculum-api) 🇬🇧 | 🟢 **MIT** · 1 077 B · `0eeb9d32caed` |
| **Agent runtime** | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 **Apache-2.0** · 11 357 B · `c71d239df917` |
| **Teacher-facing capability** | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) (ships its own evals) · [`oaknational/oak-ai-lesson-assistant`](https://github.com/oaknational/oak-ai-lesson-assistant) | 🟢 **Apache-2.0** 11 357 B · `58d1e17ffe51` / 🟢 **MIT** 1 077 B · `d150aadcccd2` |
| **Assessment evidence** | [`kit-sdq/autograder`](https://github.com/kit-sdq/autograder) (explainable, check by check) · [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) (academic integrity) | 🟢 **MIT** · 1 068 B · `30a0bc0d48b4` / 1 084 B · `881163366572` |
| **Eval gate** | [`Teachable-AI-Lab/tutor_gym`](https://github.com/Teachable-AI-Lab/tutor_gym) · [`shuangyan123/tutorbench`](https://github.com/shuangyan123/tutorbench) | 🟢 MIT / Apache-2.0 (code) — see `repos/foundations.md` Tier 9 |
| **Obligation check** (dates) | [`tomdxb0004/eu-ai-act-risk-checker`](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | 🟢 **MIT** 1 073 B · `b7b08f330649` @ `41da87feb238` — `engine.js:32` encodes Annex III = **2027-12-02** citing Reg. (EU) 2026/1744 |
| **Obligation check** (codebase scan) | [`ark-forge/mcp-eu-ai-act`](https://github.com/ark-forge/mcp-eu-ai-act) | 🔴 **MIT** 1 065 B · `002af8f9b59c` — scanning only. **`p437`: its encoded deadline is the superseded `2026-08-02` and is test-pinned — do NOT take dates from it** |

### How it wires together

1. **Pick the connector by the client's platform, not by preference.** One of the six rows
   above, or Moodle/Canvas from `verticals/solutions.md` if that is what they run. The
   connector is read-only on first delivery — `iserv-mcp`'s single write tool
   (`mark_parentletter_read`) stays disabled until step 6.
2. **Pin the connector.** Every one of these is an *unofficial* client; fork it and pin the
   commit named in `agents/top.md`. 🔴 Do not depend on the upstream default branch for a
   system of record.
3. **Resolve the institution against the registry.** GIAS in England, NEIS in Korea; the
   school's URN or code becomes the tenancy key for everything downstream. Without this the
   deployment has no stable identifier for "which school".
4. **Anchor content to the curriculum authority** where one publishes — Oak's API for
   England. 🟢 `Trend 11` says jurisdictional curriculum content is the defensible layer;
   this is how you get it without licensing it.
5. **Run the teacher-facing capability only.** Lesson planning, differentiation, marking
   support, administration. 🔴 **No student-facing generative surface in phase 1** — see the
   age gate below.
6. **Gate every write behind the staged artefact.** Draft → named human → recorded
   approval → write. This is `Pattern AH`'s draft-and-sign, unchanged, and it is what makes
   the connector's write tools safe to enable.
7. **Ship the evidence pack with the build**, not after it: `tutor_gym` / `tutorbench` for
   the capability, `autograder`'s per-check output for the marking claim, `dolos` for the
   integrity question the buyer will ask.

### 🔴 The six things that will bite, named up front

1. 🔴 **Every connector is unofficial, and the READMEs say so.** `iserv-mcp` warns that
   instances differ and to test against the school's own installation; `dtu-learn-mcp` is a
   student project and tells you to use it with your own account only. **No API stability
   promise, no vendor escalation path.** Price a connector-maintenance line into the
   engagement; it is not a one-off integration.
2. 🔴 **An age gate is a hard requirement in two jurisdictions and a design requirement in
   all of them.** Norway prohibits generative AI for grades 1–7 from the start of the
   2026–27 school year and permits grades 8–10 only under direct teacher supervision;
   NYCPS has a 2K-8 moratorium. 🟢 `Trend 32` has the requirement table — a per-learner
   grade band enforced at the model boundary, plus **supervision mode as a distinct runtime
   state**, not a UI toggle.
3. 🔴 **The age gate needs the learner's age, which is new PII exposure.** Take the band
   from the roster system of record, never infer it, never persist it past the session, and
   never send it to the model provider. A compliance feature that creates a data-protection
   breach is the most common way this build fails its own audit.
4. 🔴 **Student credentials are the connector's authentication model.** Most of these clients
   authenticate as the *user* — a student's or parent's own login. 🔴 **An institutional
   deployment cannot hold those**, so phase 1 is teacher-account scoped and any
   student-scoped feature needs the platform vendor at the table, which returns you to
   point 1.
5. 🟡 **Germany has no federal buyer.** Education is *Länder* competence and there is no
   federal school AI strategy; sixteen Länder are sixteen procurements. 🟢 Name the Länder
   programme in the pitch — **AI4Teachers** (Rhineland-Palatinate, multiplier model) or
   Bavaria's 15 model schools — because that is the budget line that already exists.
6. 🟡 **The EU obligation clock is not the delivery clock.** Annex III for stand-alone
   education AI runs to **2 December 2027**; Article 50 transparency has applied since
   **2 August 2026**. 🔴 A teacher-facing build in scope of Article 50 has a *live*
   obligation today, which is the half that gets forgotten.

### 🟢 Why the proposal is stronger than a platform build, in one line each

- **The client's own ministry already published the code.** Udir's exam administration
  (Apache-2.0), three DfE services (MIT), Oak's curriculum API and lesson assistant (MIT) —
  a proposal can cite the buyer's own repositories rather than a vendor's case study.
- **Nothing is replaced**, so there is no migration risk line to argue away.
- **Every component is permissive**, so the derivative ships without a copyleft conversation
  — which is not true of any Moodle-based alternative.
- **The teacher-facing scope clears an age restriction by construction**, so Norway's
  prohibition and NYCPS's moratorium are not objections to be managed.

### Shape and duration

| phase | weeks | output |
|---|---|---|
| 0 — address audit (`Pattern Z`) + connector selection | 1 | the six-row table narrowed to one, pinned at a commit |
| 1 — registry + curriculum anchoring | 2 | institution resolved, curriculum reachable, tenancy key fixed |
| 2 — teacher-facing capability + eval gate | 3–4 | the capability and the evidence pack that scores it |
| 3 — age gate + supervision mode + PII review | 2 | `Trend 32`'s requirement table satisfied and reviewed |
| 4 — write path behind draft-and-sign | 2 | connector write tools enabled, approvals recorded |
| **total** | **10–11 weeks** | a permissive agent layer over the platform the client already runs |

🟡 **What this pattern does not claim.** It is a *teacher-facing* build. A student-facing
tutor over a national platform is a different engagement with a different legal surface, and
in Norwegian primary education from late August 2026 it is **not available at all**.

## 🆕 Pattern AL — `p432` The IEP drafting assistant that is **not** a system of record (the one NA special-education engagement that is legal by construction)

**Why this pattern exists.** `Pattern AH` establishes draft-and-sign as the architecture that
satisfies US state law, the EU AI Act and Vietnam's decree at once. Special education in North
America is where that architecture stops being good practice and becomes the **statutory
requirement**: IDEA and §504 make the IEP a legal instrument, Oklahoma and Maryland bar AI as the
sole basis for a high-stakes student decision, and Charleston County names special-education
determination explicitly. `Trend 28` shows this is simultaneously the thinnest-supplied surface in
the whole industry — so this is a build with no incumbent, not an integration.

### The stack, with the grant on every piece — all read at HEAD on 2026-10-25

| Layer | Component | Grant (payload, read at HEAD) | Why this one |
|---|---|---|---|
| Knowledge + boundary | [`robotros/California-IEP-AI-project-kit`](https://github.com/robotros/California-IEP-AI-project-kit) | **MIT** · `LICENSE` 1 064 B · `2524a8e74f10` @ `ff1ae0ce30e7` | Two pinned roles (CA Essential Standards analyst; IEP goal generator), Light (3 md) / Full (8 md) editions, CDE-sourced, with the "no autonomous student-record action" boundary written into its own README. |
| Deployment shell | [`67tallchris/iep-builder`](https://github.com/67tallchris/iep-builder) | **MIT** · `LICENSE` 1 068 B · `523f156051cf` @ `b39df0e9a4a1` | Svelte + Cloudflare Pages Functions + D1, **bring-your-own-key**. A per-district instance that holds no vendor key and no central student store. |
| Draft-and-sign engine | [`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp) | **MIT** · `LICENSE` 1 076 B · `2bcdae923d26` | Already produces a draft-for-review **by default**. Reuse its review-state machine; retarget the artefact from a grade to an IEP goal set. |
| Review-state audit trail | [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | **MIT** · `LICENSE` 1 069 B · `297c4cba7b33` @ `b90bd88a2899` | Raises each artefact as a `WAITING_REVIEW` task and **records the approve/reject decision**. This is the enforcement `robotros`' kit declares in prose but does not implement. |
| Progress monitoring | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) + [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** / **MIT** | An IEP goal needs *measurable* progress. BKT/DKT gives a non-LLM, auditable model of mastery — defensible to a district in a way an LLM's opinion is not. |
| Parent-facing layer | [`dougdevitre/access-to-education`](https://github.com/dougdevitre/access-to-education) | **MIT** · `LICENSE` 1 068 B · `68657618a157` @ `f8abd70707ba` | ~120 k words of IEP navigation, family–school communication and advocacy content, MIT-granted. Serves `Trend 10`'s unserved parent persona from the same deployment. |
| Offline marking | [`rwrife/rubric-desk`](https://github.com/rwrife/rubric-desk) | **MIT** · `LICENSE` 1 062 B · `ec0b7dad19a4` @ `010a44006014` | Optional. Where staff mark away from connectivity. 🟡 Created 2026-10-25 — fork it. |
| Differentiated delivery | [`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) | 🔴 **AGPL-3.0-or-later** · `LICENSE` 35 441 B · `d8d2ea7ef0a1` @ `6194e51e8f1f` | Optional, and **over HTTP only**. UDL/WCAG/AAC/TTS differentiation. Network copyleft over a hosted engine: never vendor, never link, never fork into the deliverable. |

**Seven MIT pieces and one deliberately quarantined AGPL one.** No component in the required path
carries a copyleft obligation.

### How it wires together

1. **Pin the jurisdiction first.** Load the `robotros` Full edition (8 knowledge files) for
   California, or re-author it against the state's own standards authority for anything else. The
   kit is a *template for jurisdiction pinning*, not a national answer — Arizona's `iep-builder`
   exists separately for the same reason.
2. **Stand up the shell per district.** `iep-builder`'s Cloudflare + D1 + BYOK shape, so the key
   belongs to the district and the data never transits a studio tenant.
3. **Take an authorised, de-identified baseline.** The kit requires this and warns that typed
   redaction is *not* de-identification — so de-identify in the pipeline, not in the prompt.
4. **Generate a draft goal set, never an entry.** Reuse `canvas-grader-mcp`'s draft default.
5. **Enforce the boundary in code.** Wrap every artefact in `AI-Teaching-Agent`'s
   `WAITING_REVIEW` task with a recorded approve/reject and reviewer identity. 🔵 **This step is
   the pattern.** Without it you have shipped `robotros`' disclaimer, not its discipline.
6. **Write nowhere.** The authorised commercial system of record (PowerSchool Special Programs,
   Frontline, SEIS) receives the signed output by human action. There is no open-source
   special-education system of record — `verticals/solutions.md` — so the constraint is forced, and
   it happens to be the compliant design.
7. **Monitor progress with a model you can show.** OATutor + pyKT for mastery estimates against
   each goal; an LLM narrative *on top of* those numbers, never instead of them.
8. **Serve the parent from the same instance** with the `access-to-education` corpus.

### 🔴 The six things that will bite, named up front

1. **No evaluation exists for this category.** `p431`'s tutor-evaluation tier (`tutor_gym`,
   `tutorbench`) does not score IEP goal quality, and no IEP benchmark surfaced. **Budget to build
   the eval**, and say so in the proposal — a quality claim here is currently unprovable with open
   tooling.
2. **Every component is a seed.** 0, 0 and 1 star; two created within eleven days of this pass; no
   second contributor anywhere. Fork and own, pin to the SHAs above, and price maintenance in.
3. **`robotros`' kit is prose, not a runtime.** No model is named and nothing enforces its
   boundary. Step 5 is the billable core; a client who thinks they are buying the kit is mistaken.
4. **FERPA is not certifiable by any component here**, and the kit says so explicitly. The
   authorisation path is a client-side legal workstream running in parallel — surface it in week 1,
   not at UAT.
5. **AGPL contamination risk is concentrated in one optional step.** If `AlloFlow` is adopted,
   hold it behind a network interface and write the boundary into the architecture document. The
   temptation to fork "just the differentiation bit" is how AGPL enters a deliverable.
6. 🆕 `p433` **THE JURISDICTION CHECK IS NOW THE FIRST GATE, AND NEW YORK CITY IS WHY.** This
   pattern assumes draft-and-sign is sufficient because no US rule bars an AI *draft* of an IEP —
   only AI as the *sole basis* for the decision. 🔴 **That assumption is no longer safe
   everywhere.** NYC Public Schools' **March 2026 preliminary** guidance was reported to place
   **"development of special education and 504 plans"** on its **red / prohibited** tier — not
   "not the sole basis", but prohibited. NYC then **enacted** a student-facing generative-AI
   moratorium for 2026-27 (2026-09-02, grades 2K-8, ~600,000 students). 🟡 **Whether the
   plan-development prohibition survived into the enacted policy could not be established**
   (`Gap 433-B`), and the enacted text that *is* quoted names IEP/504 only as an **exemption**
   from the ban for assistive technology — the opposite direction.
   🔵 **So the instruction is procedural, not a verdict.** Do not pitch this pattern into a
   district until its own rule is read: in the largest US district the answer may be *prohibited
   outright*, which no amount of human-sign-off architecture cures. Week 1's "jurisdiction pinning"
   (below) stops being a formality and becomes a **go/no-go**: pin the district's own AI policy,
   not just the state statute, and get the red-tier list in writing. **Charleston County and NYC
   are now two independent NA districts naming special education explicitly** — treat
   district-level prohibition as the base case to disprove, not the edge case.

   🔴 🆕 `p434` **ANSWERED, AND THE ANSWER IS THE RESTRICTIVE ONE: IN NYCPS THIS PATTERN'S CORE
   STEP IS PROHIBITED.** `Gap 433-B` is **closed**. The current NYCPS *Guidance on Artificial
   Intelligence and Screen Time* carries a **"Red: Do Not Proceed"** tier in its Traffic Light
   Approach, and that tier names **IEP and 504 plan development** with the operative sentence
   *"All special education documents are developed by qualified professionals"*, citing **IDEA**
   and **Chancellor's Regulation A-710**. A second independent outlet states that educators may
   not use AI in grading, care and counselling, behavioural monitoring, **or crafting IEPs or 504
   accommodations**. 🔵 **Two secondaries, consistent; no primary read — `Gap 433-C`'s ceiling
   applies** (`schools.nyc.gov` is 403 at this host's egress).

   🟢 **And the apparent contradiction `p433` could not resolve was never a contradiction — it is
   a SCOPE distinction, which is the part to carry into a client conversation.** The two clauses
   govern different subjects:

   | Instrument | Subject | Effect on an IEP |
   |---|---|---|
   | Red tier, Traffic Light Approach | **Staff** use of AI to *develop* the document | 🔴 **Prohibited** — a qualified professional develops it |
   | 2K-8 moratorium **exemption** | **Student-facing** assistive technology delivered *under* an existing IEP/504 | 🟢 **Exempt** from the ban — it may continue |

   🔵 So the exemption permits *delivering* accommodations a plan already grants; it says nothing
   about *writing* the plan, and the red tier forbids that. `p433` read an exemption for one
   subject as evidence about the other.

   🔴 **The consequence for this pattern, stated without softening.** In NYCPS, `Pattern AL`'s
   step 4 — *"generate a draft goal set"* — is **the prohibited act**, not a safe-harbour version
   of it. Draft-and-sign does **not** cure it, because the rule is addressed to who may *develop*
   the document rather than to who may *approve* it. 🟢 **What remains sellable in NYCPS** is the
   non-drafting surface of this same stack, and it is not small: progress monitoring (OATutor +
   pyKT against existing goals), the parent-facing `access-to-education` layer, and
   accommodation *delivery* under an already-signed plan — all three sit outside the red tier and
   the third is explicitly exempted. 🔵 **Sell the stack minus step 4**, and say why in the
   proposal rather than letting a district's counsel find it.

   🔴 **Second NA procurement fact from the same leg, and it gates timing rather than scope.** The
   NYCPS chancellor directed principals to **pause all educational-software purchases** pending
   updated AI guidance. For the largest US district the near-term motion is therefore a
   **no-cost pilot or a standards conversation**, not a purchase order — price the engagement
   accordingly instead of forecasting a close.

### Shape and duration

**10–14 weeks** to a district pilot: 2 weeks jurisdiction pinning and authorisation path, 3 weeks
shell + draft-and-sign enforcement, 3 weeks progress monitoring, 2 weeks parent layer, 2–4 weeks
evaluation build and review cycles. 🔵 Longer than `Pattern AJ` (evidence-gated tutor pilot)
because there is no incumbent base to start from — which is also why there is no incumbent vendor
to displace.

🔴 **Where this pattern does NOT apply.** It is US-shaped. England's EHCP process and the
inclusive-education mandates of Brazil, Chile and Colombia have **no open-source tooling at all**
(searched this pass; nil result). Outside North America this is a from-scratch build with the
`robotros` kit as a structural reference only.

---

## 🆕 Pattern AM — `p433` The **teacher-facing courseware factory**: the build that is legal in NYC *because* no student ever touches the model

**Why this pattern exists.** `Trend 30` establishes that the binding US rule is now the
**district's**, and that the districts prohibit by **grade band** and by **who faces the model**:
NYC bars student-facing generative AI in grades 2K-8 and companion chatbots in *every* grade, while
**explicitly retaining teacher-facing AI for lesson planning and translation**. Katy ISD draws the
same kind of line at grade 6. 🟢 **That is not a constraint to work around — it is a specification.**
A system whose only user is a teacher, and whose output is courseware a human approves before any
student sees it, is sellable into the single largest US district *today*, in the grade bands where
every student-facing product is currently barred. It is also, by construction, outside EU AI Act
Annex III: it neither scores a student nor determines access to education.

### The stack, with the grant on every piece — all read at HEAD on 2026-10-25

| Role | Component | Grant | HEAD | Payload |
|---|---|---|---|---|
| Authoring chain (the core) | [cabbage2000-lab/textbook-writer-skills](https://github.com/cabbage2000-lab/textbook-writer-skills) | **MIT** | `e2b825072ba5` | `LICENSE` 1 064 B · `0d5a33d13ca9` |
| Source-material ingest | [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | **MIT** | `f8849746d85c` | `LICENSE.md` 1 122 B · `15ce43afa44a` |
| STEM grounding (physics) | [122-syf-wcy/PhysicsOS](https://github.com/122-syf-wcy/PhysicsOS) | **Apache-2.0** | `a25c6ee26583` | `LICENSE` 11 356 B · `f1a2e5fccede` |
| Orchestration | [huggingface/smolagents](https://github.com/huggingface/smolagents) | **Apache-2.0** | `96f33faaf028` | `LICENSE` 11 357 B · `c71d239df917` |
| Delivery base — AI *inside* | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | `d073ad444fe5` | `LICENSE` 10 982 B · `6dbc5b605ed0` |
| Delivery base — offline/equity | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | `44a4e68aac3e` | `LICENSE` 1 097 B · `3c056b34a476` |
| Delivery base — Open edX client | [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** | `c73c4bb42aa7` | `LICENSE.TXT` 11 358 B · `cfc7749b96f6` |
| Did it work? | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | **MIT** | `ccbaf37b07e3` | `LICENSE` 1 066 B · `f5f955194636` |
| Regression on prompt change | [shuangyan123/tutorbench](https://github.com/shuangyan123/tutorbench) | **Apache-2.0** (code) | `f9d69c7ce3e1` | `LICENSE` 11 358 B · `cfc7749b96f6` |

🟢 **Nine components, nine permissive grants, zero copyleft in the required path** — and no
quarantined AGPL step at all, unlike `Pattern AL`. This is the cleanest licence position of any
pattern on this file.

### How it wires together

1. **Ingest** — teacher drops the syllabus, textbook chapters, slide decks and standards documents
   into `learn-from-materials`. It produces a **traceable** knowledge base: every extracted claim
   keeps a pointer back to the source page. **Keep that traceability; it is the audit artefact**
   that answers "where did this lesson come from?" later.
2. **Author** — `textbook-writer-skills` runs its gated UbD chain over that KB: teaching
   positioning → five-part gate → chapter-tree gate → four-stage chapter writing → review. 🟢 **Do
   not remove its gates.** Its verify-or-flag behaviour — recompute STEM claims, check humanities
   citations word-by-word, emit *"needs author confirmation"* where it cannot verify — is the
   single most valuable property in the stack, because it converts the model's uncertainty into a
   teacher's task queue instead of into confident prose.
3. **Ground the STEM** — for physics, route generated worked examples through `PhysicsOS`: the
   physics engine **executes** the scenario, so a wrong number is caught by simulation rather than
   by a reviewer's eye. This is the only component in this base that can falsify its own output.
   🔵 Physics only; there is no equivalent for chemistry or biology (see the limits below).
4. **Orchestrate** — `smolagents` holds the chain. Two reasons over a heavier framework: it is
   minimal enough that the gate logic stays legible in review, and it is **EU-domiciled**, which is
   a procurement answer in EMEA rather than a technical one.
5. **The approval gate — this is the pattern, not a step in it.** Nothing reaches a learner until a
   named teacher approves it. Store approver identity, timestamp, the model and version used, and
   the diff between generated and approved text. **This record is the product** in a district that
   must show AI did not decide anything.
6. **Deliver** — publish approved courseware into the base: **OpenOLAT** when the client needs a
   full LMS and can take the AI layer *inside* the platform (the only Apache-2.0 LMS, so this is
   lawful); **Kolibri** where connectivity or equity is the constraint; an **XBlock** component
   when the client is already on Open edX and the Apache-2.0 seam keeps your code out of the
   platform's AGPL reach.
7. **Measure** — `pykt-toolkit` over the resulting activity data for knowledge tracing, so the
   claim "this courseware worked" is defensible rather than rhetorical. `tutorbench` as the
   **regression** harness: re-run it on every prompt or model change, because a silent quality
   regression in a courseware factory ships to every class at once.

### 🔴 The four things that will bite

1. **`textbook-writer-skills` is 37 ★ with 12 forks and no second maintainer.** Fork it, pin
   `e2b825072ba5`, and price maintenance in. Its gates are the asset; a fork that strips them to
   "go faster" deletes the reason to choose it.
2. **`learn-from-materials` carries an author-key flag.** Its MIT payload names
   `Copyright (c) 2025 virgiliojr94` while the owner is `dmoshehun-prog` and the repository was
   created 2026-09-08. **The MIT grant stands** — but before vendoring into a client deliverable,
   raise it with the maintainer and record the answer. `agents/trending.md` `p433` has the detail.
3. **`PhysicsOS` grounds physics and nothing else.** Do not generalise its guarantee. For
   non-physics STEM the stack is back to `textbook-writer-skills`' recompute-or-flag, which is
   honest but weaker. Say which subjects are grounded in the proposal.
4. **Copyright of the *source* material is the client's problem and it will land on you.** Ingesting
   a commercial textbook into a KB and generating derived courseware is a licensing question about
   the textbook, not about any component here. Surface it in week 1. 🔵 This is the one risk in
   this pattern that no licence read on these shelves can clear.

### Shape and duration

**6–8 weeks** to a teacher-piloted factory: 1 week ingest and traceability, 2 weeks authoring chain
and gate tuning against the client's standards, 1 week STEM grounding where applicable, 1 week
approval workflow and audit record, 1–2 weeks delivery into the chosen base, 1 week measurement
wiring. 🟢 **Shorter than `Pattern AL` (10–14 weeks) for a structural reason**: there is no
jurisdiction go/no-go to clear first, because teacher-facing-with-human-approval is the lane the
restrictive districts *left open on purpose*.

🔵 **Where this pattern is the wrong answer:** a client who wants a student-facing tutor. Say so
plainly and move them to `Pattern AJ` or `Pattern AI` — and tell them which grade bands they can
sell it into, which in NYC today is high school only, and never as a companion chatbot.

## 🆕 Pattern AJ — `p431` The evidence-gated tutor pilot (the deliverable that survives a board review in NA, EMEA and APAC)

**The problem it solves.** Every tutoring pilot this base can already build stalls at the same
question: *how do you know it teaches well?* Until this pass there was no permissive answer — the
scorer was either a closed vendor or an ungranted academic benchmark. There is now. This pattern
ships the **evidence**, not the tutor, and the tutor rides along.

### The stack, with the grant on every piece — all read at HEAD on 2026-10-25

| Layer | Component | Grant | HEAD |
|---|---|---|---|
| Tutoring runtime | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** | `e24c8456e5f7` |
| Evaluation fixture | [`Teachable-AI-Lab/tutor_gym`](https://github.com/Teachable-AI-Lab/tutor_gym) | **MIT** | `772f5cdca5dd` |
| Regression engine | [`shuangyan123/tutorbench`](https://github.com/shuangyan123/tutorbench) | **Apache-2.0** (code) | `f9d69c7ce3e1` |
| Mastery measurement | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** | `ccbaf37b07e3` |
| Human-sign-off surface | [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | **MIT** | `b90bd88a2899` |
| LMS seam (if Open edX) | [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | `c73c4bb42aa7` |
| Offline delivery (if needed) | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | `44a4e68aac3e` |

**Permissive end to end.** No GPL, no AGPL, no ungranted code. The client owns the deliverable.

### How it wires together

1. **Fork `tutor_gym` on day one.** Its last commit is 2025-09-10; treat it as a fixture you now
   maintain, not a dependency you track. Pin the fork SHA in the client's repo.
2. **Stand up `OATutor` as the tutoring runtime** and point `tutor_gym`'s `oatutor` backend at it:
   `python llm_tutor_eval.py --tutor-kind oatutor --profile oa_compl-aug.prof --model <model>`.
   This is the step that normally costs adapter work and here costs none — the binding already exists.
3. **Run the *student* direction too** (`llm_stu_eval.py`). A simulated-learner run is what produces
   a defensible claim about *learning* rather than about *answer quality* — and it is the half most
   pilots skip.
4. **Wrap the scored runs in `tutorbench` as a regression suite.** This is the piece that makes the
   evidence *durable*: when a prompt, model or curriculum changes, the same scenarios re-run and the
   diff is the artefact. Wire it into CI as a merge gate.
5. **Ground mastery claims in `pykt-toolkit`** (BKT/DKT) rather than in model self-report, so the
   adaptivity claim is a measurement, not a narrative.
6. **Route every student-affecting output through `AI-Teaching-Agent`'s `WAITING_REVIEW` queue**, so
   each action carries a recorded human approve/reject. That record is the oversight evidence.
7. **Deliver the evidence pack**: scored baseline, simulated-learner results, regression suite in CI,
   human-sign-off log, and the licence read for every component.

### Why the same artefact clears three jurisdictions

| Region | What it is asked for | Which step answers it |
|---|---|---|
| **North America** | Oklahoma / Maryland: no high-stakes AI decision without human oversight; district board review | Step 6 (sign-off log) + step 7 (scored baseline) |
| **EMEA** | Article 50 transparency **from 2 Aug 2026**; Annex III conformity by **2 Dec 2027** (Reg. (EU) 2026/1744) | Steps 4 and 7 — the regression suite is the start of the conformity file |
| **APAC** | Vietnam's high-risk list names automated assessment (obligations **1 Mar 2027**); Korea's AI Basic Act **in force 22 Jan 2026** | Steps 3, 4 and 6 |
| **LATAM** | UNESCO IESALC: 87% adoption, 26% with a strategy — the governance gap | The whole pack, sold as assurance attached to the platform (`Trend 21`) |

### 🔴 The four things that will bite, named up front

1. **`tutor_gym` is 13.5 months stale.** Budget the fork in week 1. Do not present it as maintained.
2. **`tutorbench` is three licences, not one.** Apache-2.0 for the engine, **CC-BY-4.0 for the
   scenario content** (attribute it), and a **brand policy** over the name — keep “TutorBench” off
   the client's product and marketing.
3. **The harnesses are English-first** (`Gap 431-A`). For LATAM and APAC, **scope scenario
   translation as a line item**. The CC-BY-4.0 content grant makes re-authoring lawful; it does not
   make it free.
4. **This pattern scores tutoring, not grading** (`Gap 431-C`). If the client's real exposure is
   assessment — and under NA, EMEA and APAC statutes it usually is — **say so explicitly in the
   proposal** and scope a bespoke rubric harness. Do **not** reach for
   [`sdrangan/llmgrader`](https://github.com/sdrangan/llmgrader): its licence forbids commercial use.

### Shape and duration

**6–8 weeks** for a single-subject pilot with the evidence pack, assuming the client already runs an
LMS. Add **2–3 weeks** for scenario localisation outside English. The fork of `tutor_gym` is a
permanent maintenance line to hand over at the end, and the proposal should say so.

## 🆕 Pattern AH — The draft-and-sign grader (the one architecture that satisfies NA, EMEA and APAC at once)

**The problem.** Three regulatory regimes independently converged on the same requirement,
by different routes: Oklahoma and Maryland prohibit AI as the **sole basis** for high-stakes
student decisions; the EU AI Act classes **grading** as high-risk (now due 2 Dec 2027 under
Regulation (EU) 2026/1744); Vietnam's decree names **automated assessment** high-risk with
March 2027 compliance. One architecture satisfies all three — and it is cheaper than the
autonomous version, not more expensive.

**The recipe.**

| Layer | Component | Licence (verified @ 2026-10-25) | Why this one |
|---|---|---|---|
| Grading agent | [`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp) | MIT · `c47e8b3ac2ae` | **Emits a draft for human sign-off by default.** The compliance artefact is the default behaviour, not a bolt-on. |
| LMS seam (Canvas) | [`semyonfox/canvas-mcp`](https://github.com/semyonfox/canvas-mcp) | MIT · `e317c4b7bf10` | Broader Canvas surface when the grader alone is too narrow. |
| LMS seam (Open edX) | [`openedx/XBlock`](https://github.com/openedx/XBlock) | Apache-2.0 · `c73c4bb42aa7` | Keeps your code out of AGPL reach. |
| LMS seam (Google Classroom) | [`vTanco/google-classroom-mcp`](https://github.com/vTanco/google-classroom-mcp) | MIT · `9ba0070eff2f` | 🔴 **Use this address, not `pengusto`'s** — see below. |
| Defensible scoring | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | MIT · `ccbaf37b07e3` | A knowledge-tracing model you can show a regulator, behind the LLM's prose. |
| Agent runtime | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | Apache-2.0 · `96f33faaf028` | Minimal, EU-domiciled. |

**Wiring.** Agent proposes score + rationale → writes **draft** into the LMS via MCP →
instructor reviews in their normal grading UI → sign-off event is the audit record.
pyKT runs alongside to produce a mastery estimate that does **not** depend on the LLM, so
the score has a defensible basis when challenged.

🔴 **The trap this pattern exists to avoid:** `pengusto/google-classroom-mcp` was the
recommended Google Classroom lane in three earlier passes and **relicensed to proprietary
on 2026-10-23**, with a clause naming educational institutions as requiring a paid
agreement. The MIT bytes survive at `vTanco` (verified by digest equality, `a01639b20880`).
**Re-read every component licence at its SHA before an engagement commits.**

**Effort:** 6–8 weeks to a governed pilot on an existing Canvas estate.

## 🆕 Pattern AI — Offline-first tutoring where connectivity and equity are the constraint

**The problem.** Argentine AI use runs **75% in high-SES and 42% in low-SES** groups. A
cloud-dependent deployment widens a 33-point gap and the client will be measured on it.

**The recipe.** [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
(**MIT**, `44a4e68aac3e`) as the platform — the only MIT platform on the shelf and built
offline-first — with [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE)
(**BSD-3**, `196c547291da`) running local models through Ollama for the tutoring surface,
and [`satvik314/educhain`](https://github.com/satvik314/educhain) (**MIT**, `38adb1e9459d`)
generating localised Spanish/Portuguese content **ahead of deployment**, synced on the
occasional connection.

🟢 **Every component is permissive and every one runs without egress** — which is also the
data-residency story for LGPD (Brazil) and Ley 1581 (Colombia). No per-token cost is the
reason this survives a public-sector budget.

**Effort:** 8–10 weeks including content localisation.

---

## Pattern AG

### 🆕 `p408` — the India DPI engagement: MIT the whole way down, with the fork check as step 0

🔵 **When to reach for it.** An APAC/India engagement where the client is a state education
department, a DIKSHA-adjacent programme or a CBSE/NCERT-aligned private network, and the
requirement is in-country inference plus a permissive grant the client can extend without
publishing the extension. 🟢 This is the one stack on these shelves that is **MIT at every layer**.

**Step 0 — the fork-provenance check, and it is not optional here.**
🔴 `p408` found a fork of Sunbird documentation carrying **AGPL-3.0** while upstream is **MIT**,
returned *above* upstream by search. Before any Sunbird address enters a proposal, pin the grant to
the ref:
```bash
git ls-remote --symref https://github.com/<slug> HEAD          # the REAL default ref (Sunbird docs = dev, portal = master)
git clone -q --depth 1 --filter=blob:none --no-checkout https://github.com/<slug> r
git -C r cat-file -s HEAD:LICENSE                               # 1,072 B ≈ MIT · 34,520 B ≈ AGPL-3.0
git -C r fetch -q --depth=1000 origin "$(git -C r symbolic-ref --short HEAD)"
git -C r log --format='%h %cI %s' --follow -- LICENSE            # did the grant CHANGE, and in which direction?
```
🟢 The last line is the one `p404`'s gate exists for: **direction is only establishable from full
history**, and a byte-identical blob sha against upstream's pre-relicence blob proves *frozen*
rather than *re-licensed*.

**Step 1 — the platform.** [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal)
(`master`, 🟢 MIT) as the content-and-delivery spine, with
[`Sunbird-Ed/SunbirdEd-mobile-app`](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) (`main`,
🟢 MIT) where a handset is the real client. 🔴 **Budget the staleness, do not discover it:** 311 d
and 399 d since HEAD respectively. Fork at a pinned SHA, run the client's own dependency and CVE
sweep before week 1 ends, and price a maintenance line. 🔴 Do **not** name
`Sunbird-Ed/sunbird-learning-platform` in a deliverable — it does not resolve.

**Step 2 — the offline edge.** [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
(🔴 `develop`, 🟢 MIT) for low-connectivity districts, which is most of the addressable footprint
and already this shelf's most important repo for that constraint.

**Step 3 — the assessment layer.** [`Naitik-xd/CurriculumCraft-AI`](https://github.com/Naitik-xd/CurriculumCraft-AI)
(`main`, 🟢 MIT, HEAD **2026-10-03**) for CBSE/NCERT Grades 9–12 item generation. 🟢 Take its
*constraint* as the requirement, not just its code: it is built to generate without reproducing
verbatim NCERT text, which is the copyright exposure a client's counsel will actually ask about.
🔴 It is **public beta** and says so — wire it behind human review, never as the graded instrument.

**Step 4 — inference, in country.** `CurriculumCraft-AI` already targets **open-weight Gemma**, so
serve it locally rather than re-architecting: this is the APAC data-residency posture without a
sovereign-cloud contract.

**Step 5 — grounding, and the licence trap to avoid.** Use
[`crpf-mitadt/Indian-AI-for-Education`](https://github.com/crpf-mitadt/Indian-AI-for-Education) as
the **discovery index** for Indian ASR/TTS/OCR and translation assets. 🔴 **It is CC0-1.0 over the
document only** — every asset it names keeps its own grant, so each one re-enters at Step 0. Never
cite the index as the licence for anything inside it.

**Shape of the engagement.** 10–12 weeks: 1 week for Step 0 across every address plus the CVE
sweep; 4 weeks portal fork, pin and deploy; 2 weeks Kolibri edge sync; 3 weeks assessment layer
behind review; 1–2 weeks local-inference hardening.
🟡 **What this pattern does NOT give you:** multi-tenancy (no Sunbird row here claims it), a current
upstream to pull from, or a compliance story. For the last of those, Vietnam's Decision 33 and
Korea's `AI Basic Act` are the APAC instruments — see [`intel/market.md`](../intel/market.md) — and
India's own posture is a separate read this base has not closed.

## 🆕 `p406` — a standing existence check becomes a step in every pattern, and `Pattern C` gets a dated APAC variant

### 🟢 `Pattern Z` — the pre-engagement address audit, now a command rather than a habit

🔴 **Every pattern on this shelf names repositories, and 1.94 % 🔵 *(`p407`; `p406` published 2.20 %, counting 7 non-repositories as decay)* of the addresses this base carries do
not resolve.** Two of them are **inside a recipe on this very file**. 🟢 The check is now one command
and it needs no clone budget:

```bash
# offline: what the shelves name (no network)
make carried-existence-census                 # -> 2 682 addresses over nine shelves

# online: does each one still answer?  p293's control pair gates every verdict
make carried-existence-sweep                  # ~2.5 min at 12 workers, ~17 probes/s
WORKERS=6 make carried-existence-sweep        # throttling is retried serially, never
                                              # counted as decay
```

🔵 **Wire it as the first step of an engagement, before a single repo is cloned.** The channel is
`git ls-remote --symref`, so it costs **no object transfer** — which is why this is affordable where
`api.github.com` answers `403` on a scoped session and a clone-per-address does not fit any budget.

| what it returns | what to do with it |
|---|---|
| `EXISTS-PUBLIC` | 🟡 the address answers **today**; maintenance is a separate question (`p173`) |
| `EXISTS-NO-REFS` | 🔴 **an EMPTY repository.** It EXISTS and ships nothing — a 404 check passes and the dependency is still vapour |
| `ABSENT-OR-PRIVATE` | 🟡 absent, private **or MOVED** — probe a guessed successor before deleting a row |
| `CHANNEL-ERROR` | 🔵 says nothing about the slug. Retry serially; never read as decay |

🔴 **And the step this pattern must NOT skip: adjudicate by reading the sentence, not the verdict.**
All 12 unresolvable addresses on `agents/top.md` turned out to be **already documented as dead** —
cited as warnings and as specimens, not as recommendations. A sweep reads addresses, not prose
(`Gap 406-A`). 🟢 The realised loss on this base was **zero**; the instrument's value is that the
**next** one is caught the same hour rather than whenever a pass happens to clone it.

### 🟢 `Pattern AA` — repair a dead address instead of deleting the row

**Worked example, verified this pass end to end.**

```bash
# 1. the sweep flags it
grep -P '\tABSENT-OR-PRIVATE\t' evidence/carried-existence.2026-10-23-p406.tsv
#    apereo/opencast   ABSENT-OR-PRIVATE   -   agents/top.md;repos/foundations.md;...

# 2. probe guessed successors — the ORG move is the common shape
python3 -I compose/code/p293-slug-existence-oracle/slug_oracle.py --online \
        opencast/opencast apereo-opencast/opencast
#    EXISTS-PUBLIC   opencast/opencast        153d1b15c93afa5bf915ee31cdfec75ecfc5284e

# 3. read the grant at the pin — a successor's licence is NOT inherited from the row
git clone --depth 1 https://github.com/opencast/opencast /tmp/oc && head -3 /tmp/oc/LICENSE
#    Educational Community License, Version 2.0 (ECL-2.0)
```

🟢 **Result: a dead foundation row became a live one with its grant re-read**, and `repos/foundations.md`
already carried both the successor and a redirect row — so the repair was a **confirmation**, which is
the cheapest possible outcome. 🔴 **Step 3 is not optional:** `apereo/opencast` and `opencast/opencast`
are different licensors as far as this base is concerned, and ECL-2.0 is **not** on the MIT/Apache
shortlist a proposal usually prices against.

### 🟡 `Pattern C` variant — the APAC education compliance pack, priced to the RIGHT date

🔴 **This file's `Pattern C` and `intel/market.md`'s opportunity 5 both priced an education
engagement against Vietnam's `2027-03-01`. That is the all-other-sectors date.** 🟢 Education's is
**`2027-09-01`** for a system live before **2026-08-15**, and **`2027-03-01`** only for one deployed
inside the six months after Decision 33 took effect.

**The recipe, unchanged in parts and re-dated in one:**

| layer | what | why |
|---|---|---|
| **1 — system of record** | **Moodle** (GPL-3.0) or **Open edX** (AGPL-3.0); **OpenOlat** (Apache-2.0) or **Kolibri** (MIT) where copyleft is refused | 🟢 the **0 %-decay** tier — see `T83` |
| **2 — integration** | [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) *(MIT, npm)* or [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) *(MIT, crates.io)* — 🟢 **both re-probed `EXISTS-PUBLIC` this pass** | 🔴 the **5 %-decay** tier: pin a version and vendor the client, per `Pattern Z` |
| **3 — agent** | compose, don't adopt: LangGraph/CrewAI over the layer-2 tools | the volatile layer stays replaceable |
| **4 — conformity** | the **Annex III** pack from the EMEA engagement, re-mapped | 🟢 **portable** — EU → Vietnam → Mexico, adapts far cheaper than it rebuilds |

🔵 **The dated argument to a client, stated correctly:** a system **already live before 2026-08-15**
has until **2027-09-01**; a **new** one has **six months** from go-live under the post-Decision-33
clause. 🔴 **The cutoff has already passed**, so for any engagement starting now the six-month clause
governs — which is a *tighter* deadline than the one the old row quoted, reached by getting the law
right rather than by rounding toward urgency. 🟡 **Bound:** no primary text was read — every policy
host answers `ENOTFOUND` on this session — so this rests on five concurring law-firm readings.
Counsel confirms before it goes in a proposal.

### 🔵 One recipe step retired

🔴 `compose/patterns.md`'s step *"8. Re-check dead addresses. Four in common circulation do not
resolve…"* named **four** addresses and asked the reader to re-check them **by hand**. 🟢 Superseded
by `Pattern Z`: the population is **2 682**, not four, and the check is a make target.

---

## 🆕 `p405` — the layer-2 Moodle MCP choice was a GPL-or-vendor-a-commit decision, and it is not any more

🔴 **`p404` wrote this file's layer-2 decision tree and closed it with:** *"`peancor` is the only
permissive option measured here, and its **0 tags** means the pattern vendors a pinned commit rather
than tracking a release."* 🟢 **Refuted, with two addresses, both read first-hand from full clones on
2026-10-23.** 🔵 The reason `p404` could not see them is a method fact worth keeping: it measured the
slug **`moodle-mcp-server`**, and these are **`moodle-mcp`** — a different slug for the same
engagement question.

```
layer 2 of Pattern I (the network boundary), Moodle side — REVISED, pick by DEPLOYMENT not by grant:

  no Moodle-side install possible (no admin, no token, SSO/2FA in the way)
      -> falkenslab/moodle-mcp                MIT  1,067 B   npm @falkenslab/moodle-mcp
         Node + Playwright; drives a REAL BROWSER SESSION as the teacher
         + nothing to install in Moodle: no web-service token, no plugin, no administrator
         + ~230 tools; works on any Moodle 4.5 / 5.x the user can already log into
         + students pseudonymised to the model (A-7KQ2XM), de-aliased only on the operator's box
         + 6 tags v0.1.0..v0.5.0, 194 commits, HEAD 1 d        <- A PUBLISHED RELEASE
         - a browser session is a seat, not a service: it acts AS one teacher, not as the site

  Moodle Web Services available, and IT wants one binary to deploy
      -> G36maid/moodle-mcp                   MIT  1,064 B   crates.io moodle-mcp
         Rust (rmcp 3.5, edition 2024, Rust 1.88); single static binary, stdio
         + Moodle 3.7 -> 5.x via the mobile-app web service; CI + Codecov
         + 7 tags v0.1.0..v0.2.1, 163 commits, HEAD 3 d       <- A PUBLISHED RELEASE
         + SSO driver for NTUST, credentials mode verified at NTNU (Taiwan)
         - student-first tool surface: a teacher-side workflow needs the option above

  GPL-3.0 acceptable (internal tooling, or the client owns the deployment)
      -> lmscloud-io/moodle-mcp-server        GPL-3.0  35,148 B   Python/fastmcp
         + 3 tags; root commit by Marina Glancy (Moodle core provenance)
         - copyleft: it cannot sit inside a proprietary layer-3

  same Node runtime as ltijs / lti-tool, and MIT required
      -> peancor/moodle-mcp-server            MIT  1,064 B   TypeScript/Node
         - 0 tags: still vendor a pinned commit.  NO LONGER the only permissive option

  wire-up, all cases, unchanged:
      Moodle core_ai provider  ->  HTTP/MCP  ->  your layer-3 (retrieval, grounding, eval)
      ADORSYS-GIS/moodle-aiprovider_openaicompatible  is layer 1 (GPL, thin, contributed back)
```

🟢 **The decision axis changed, and that is the useful part.** `p404`'s tree branched on **grant**,
because grant was the only thing that distinguished the two addresses it had. 🔴 **With four options,
grant stops discriminating** — three of the four are MIT — and the question becomes *what can you
actually install on the client's Moodle?* 🔵 **Ask the client's LMS administrator one question before
choosing:** *can we have a web-service token?* A `no` eliminates two of the four options and makes
`falkenslab` the answer; a `yes` opens the Rust binary, which is the one a school IT department will
sign off on.

🟡 **A config line this pattern needs, same class as `p404`'s.** `falkenslab` runs a **browser session
as a real user**, so it inherits that user's permissions and **nothing narrows them server-side**.
🔴 The limits are enforced in the MCP server's own config, which means **the agent's blast radius is a
client-side setting**. 🟢 Pin it in the engagement's config, enable read-only or course-scoped mode
explicitly, and treat *"students are pseudonymised"* as a property to verify in the deployment rather
than to quote from the README.

### 🟢 New, concrete: picking an LMS MCP server when the client's LMS is NOT Moodle

🔴 **This file and [`verticals/solutions.md`](../verticals/solutions.md) have cited LMS MCP servers by
bare slug, and the slug is a name-collision group of up to 20 addresses.** 🟢 Measured
2026-10-23 — 42 addresses, 269 pairs — the heads are:

```
pick by the client's LMS; each line is a MEASURED family head, not the first search result:

  Canvas      -> vishalsachdev/canvas-mcp          MIT 1,071 B  1,089 commits  23 tags  1 d
                 + root-commit author of ELEVEN of the 20 Canvas addresses
                 ! do NOT clone bartmassey-upstream/canvas-mcp: the slug says upstream and
                   the root commit says fork (1,001 commits, DIVERGED-FORK)
                 ! r-huijts/canvas-mcp is a SEPARATE project (root 2024-12-12, Fontys NL),
                   61 commits, 3 tags, npm - keep it if you want the npm package, and know
                   that mdweaver/canvas-mcp is its 3-commit superset with 0 tags

  Blackboard  -> alanwtom/blackboard-mcp           MIT 1,065 B     26 commits   1 tag   1 d
              or felipedias-ie/blackboard-mcp      MIT 1,084 B     21 commits   3 tags  9 d
                 ! the largest Blackboard address is 28 commits: READ these, do not depend
                   on them.  Budget writing your own.
                 ! bibo242/blackboard-mcp shows 28 commits and is the ANCESTOR of
                   felipedias-ie - its extra commits are on refs unreachable from its HEAD

  Brightspace -> RohanMuppa/brightspace-mcp-server MIT 1,068 B    472 commits   6 tags  1 d
                 ! THREE of the four Brightspace addresses are this one author's lineage.
                   Price it as a single-maintainer dependency and say so in the SOW.
                   The only independent address is 7 commits, Apache-2.0, 374 d.

  Moodle      -> see the revised layer-2 tree above: TEN independent implementations,
                 the only genuinely uncollapsed supply of the four platforms.
```

🔵 **Why the "!" lines are the valuable part of this recipe.** Each one is a wrong clone a studio would
otherwise make from the search index: a fork named `upstream`, a 28-commit repository that looks newer
than its own descendant, and a four-address "ecosystem" that is one person. 🟢 Instrument, 12 controls
and all 269 graded pairs:
[`compose/code/p405-group-lineage/`](code/p405-group-lineage/README.md) ·
[`group-lineage.2026-10-23-p405.tsv`](../evidence/group-lineage.2026-10-23-p405.tsv).

---


## 🆕 `p404` — two recipes on this file named the wrong address, and the fix is one line each

🟢 **Both corrections come from full-history clones read on 2026-10-23**, with the instrument and its
9 controls at [`code/p404-fork-direction/`](code/p404-fork-direction/README.md).

| recipe cell | was | 🟢 **is** | why it matters to a build |
|---|---|---|---|
| **`Pattern I` layer 1** — the `core_ai` provider plugin | *"cloned from `ADORSYS-GIS/…` **or** `lmscloud-io/…`"*, described as two independent vendors | 🟢 **Clone [`ADORSYS-GIS/moodle-aiprovider_openaicompatible`](https://github.com/ADORSYS-GIS/moodle-aiprovider_openaicompatible)** — **8 d**, Moodle 5.0+ CI matrix, listed in the Moodle Plugins directory. `lmscloud-io` is its **origin** and is **93 d** | 🔴 *"Either"* sends half of engagements to a dormant address. The two are **one lineage** — `CONTENT-COPY`, direction `lmscloud-io` → `ADORSYS-GIS` — not a choice between vendors |
| **`Pattern` LTI/Go-JVM** — the Go options | `peregrine-lti` **679 d** and `macewan-cs/lti` **1,918 d** | 🟡 Add [`astiusa/lti`](https://github.com/astiusa/lti) — **794 d**, MIT, a **strict superset** of `macewan-cs` (89/89 commits reachable) | 🟢 The *conclusion* is unchanged — **do not put a client's identity flow on any of them** — but the file was 1,125 days out on the freshest permissive Go option, and that number is what a client challenges |

🟡 **A config line `Pattern I` now needs.** `ADORSYS-GIS` **dropped** `$plugin->supported = [500, 502]`
when it republished, keeping only `$plugin->requires = 2025041400`. 🔴 So the live plugin declares **no
Moodle upper bound** and Moodle will not warn on an untested major. 🟢 **Pin the Moodle version in the
engagement's own config** and treat the plugin's compatibility as unstated rather than open.

### 🟢 New, concrete: choosing a Moodle MCP server, which is an MIT / GPL-3.0 decision, not a name

🔴 **`moodle-mcp-server` is two independent implementations** — **0 shared commits AND 0 shared trees**
— and this base has cited the bare plugin name. The two differ in **language and in grant**, so the
name alone cannot carry a recommendation:

```
layer 2 of Pattern I (the network boundary), Moodle side — pick by grant, not by name:

  proprietary or MIT/Apache deliverable
      -> peancor/moodle-mcp-server          MIT  1,064 B 845ac6ac9e57   TypeScript/Node
         + same runtime as ltijs / lti-tool, so one Node service carries LTI *and* MCP
         - 0 tags: vendor a commit, do not "install" it; 243 d, so budget maintenance

  GPL-3.0 acceptable (internal tooling, or the client owns the deployment)
      -> lmscloud-io/moodle-mcp-server      GPL-3.0 35,148 B 8b1ba204bb69  Python/fastmcp
         + 3 tags v1.0.0..v1.0.2 - the ONLY published artefact of the two
         + root commit by Marina Glancy (Moodle core provenance) - read it either way
         - copyleft: it cannot sit inside a proprietary layer-3

  wire-up, both cases:
      Moodle core_ai provider  ->  HTTP/MCP  ->  your layer-3 (retrieval, grounding, eval)
      ADORSYS-GIS/moodle-aiprovider_openaicompatible  is layer 1 (GPL, thin, contributed back)
```

🟢 **The boundary is what makes this a free choice**: GPL-3.0 is not network copyleft, so a GPL layer-2
MCP server still leaves layer 3 ownable — 🔴 but only if the client accepts shipping a GPL component at
all. 🔵 Where they will not, `peancor` is the only permissive option measured here, and its **0 tags**
means the pattern vendors a pinned commit rather than tracking a release.

---

## 🆕 `Pattern I` — 🆕 `p403` The India engagement: an in-language tutor you can actually *prove*, with a deterministic eval gate

🔵 **The engagement this answers.** India's mandate makes **AI and computational thinking compulsory
from Class 3 from the 2026–27 academic year** (see [`intel/market.md`](../intel/market.md) → APAC). A
ministry or large-group client will ask for a tutor in Hindi and at least one other state language. 🔴
**The thing that sinks these pitches is not the tutor — it is being unable to demonstrate that the
tutor is correct in a language the buyer's own reviewers read.** An English benchmark plus
*"the model is multilingual"* is not evidence, and an LLM-judge score is not evidence a reviewer can
re-run.

🟢 **What `p403` makes newly possible:** the eval half is now available, permissive, in-language and
**rule-based**, so it runs in CI and returns the same number to the client as it does to you.

### The stack, with the grant on every piece

| role | component | grant | why this one |
|---|---|---|---|
| **Tutor runtime** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** | Lifelong learner memory + RAG grounded in the learner's own uploaded materials; the largest education-native permissive base on these shelves. Apache-2.0 keeps the patent grant a government buyer's counsel will look for. 🔵 Swap in [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) (🟢 **MIT**) instead **if** the client wants generated whole-classroom delivery and central model governance — see `Pattern Q`. |
| **🆕 Eval gate (the new piece)** | [`AI4Bharat/IndicIFEval`](https://github.com/AI4Bharat/IndicIFEval) | 🟡 **MIT** code · **`CC-BY-4.0`** dataset | **14 Indic languages + English**, verifiable **rule-based** constraints, bundled `lm-evaluation-harness`. 🟢 **Deterministic — no LLM judge** — so it belongs in CI, and the client can re-run it themselves. |
| **🆕 In-language ground truth** | [`AI4Bharat/Anudesh-Backend`](https://github.com/AI4Bharat/Anudesh-Backend) | 🟢 **MIT** | `projects → tasks → users/review` workflow with organizations and workspaces: the machinery for getting teachers to author and review in-language rubrics and answer keys, with an audit trail. 🔴 Default ref **`master`**, **0 tags** — vendor a pinned commit. |
| **Mastery model** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) + [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 **MIT** | Bayesian Knowledge Tracing the client can inspect and **re-estimate on their own logs** — "adaptive" as a parameterised model, not a prompt. |
| **Retention** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** | FSRS spaced repetition + knowledge graph, and runs on local open-weight models with no key — the data-residency path. |
| **LMS surface** | client's **Moodle** | 🔴 **GPL-3.0** | Reach it through the plugin API, **do not fork** — `Pattern A` and the GPL-adapter sandwich in `Pattern Q`. |
| **Teacher AI-literacy material** | [`matsuolab/lecture-ai-engineering-2026-hi`](https://github.com/matsuolab/lecture-ai-engineering-2026-hi) | 🔴 **NO GRANT** | 🔴 **Reference only — do not vendor, do not redistribute, do not quote into deliverables.** Read it for *sequencing*: it is U Tokyo Matsuo Lab's `AIE2026` localised Hindi-first, and students build a learning agent progressively across the course. 🟢 That progression is the useful artefact; re-author it yourself. |

### How it wires together

1. **Ingest and ground.** Client curriculum (NCERT / state board) → DeepTutor's RAG store. 🔵 There is
   no permissive **Indian** curriculum graph on these shelves — `os-taxonomy` is NGSS/Common Core and
   its data is `ODbL-1.0 AND CC-BY-SA-4.0`. 🔴 **State that as a build item in the SOW**; `Pattern H`'s
   *"ground on a curriculum graph you must not fork"* rule applies, and `p388`'s BC and BNCC servers are
   the shape to copy, not reuse.
2. **Author ground truth in Anudesh.** One `project` per subject-grade; `tasks` are prompt +
   expected-constraint sets written **by the client's own teachers**; reviewers approve. 🟢 Output is a
   constraint set in `IndicIFEval`'s verifiable form, not free-text opinions.
3. **Gate the build in CI.** Run `IndicIFEval` (`indicifeval-ground` for native items,
   `indicifeval-trans` for translated) per target language on every model or prompt change. 🔴 **Fail
   the build on per-language regression, not on an aggregate** — an aggregate hides Odia collapsing
   while Hindi improves, which is precisely the failure a state buyer will find first.
4. **Adapt and retain.** OATutor/pyBKT fit mastery on the client's real logs; OpenTutor's FSRS
   schedules review. Both MIT, both inspectable.
5. **Deliver through Moodle's plugin API.** No fork, so no GPL obligation on the client's own IP.

### 🔴 The three things that will bite, named up front

- **`CC-BY-4.0` on the benchmark data.** Commercial use is fine; **attribution is not optional**. 🟢
  Put the AI4Bhārat attribution in the eval report and in any published score — the deliverable is the
  report, so the obligation travels with it. The MIT grant on the harness does **not** cover the data
  (`T36`, fourth instance).
- **These are research assets, not products.** `IndicIFEval` has **6 refs**; `Anudesh-Backend` has **0
  tags** and a `master` default ref. 🟢 Pin commits, vendor, and own the maintenance — that *is* the
  billable value, and it should be priced as such rather than discovered in month three.
- **14 languages is the benchmark's reach, not the tutor's.** 🔴 Scoring in Marathi does not mean
  teaching in Marathi. 🟢 Use the gate to **decide which languages to promise** — ship the three that
  pass and name the rest as phase two, rather than promising fourteen and failing in public.


**🆕 Pass `p401` · reads and commit both 2026-10-23.** 🟢 **One new pattern, and it exists because
the licence census forced its shape.**

## 🆕 `Pattern Q` — the GPL-adapter sandwich: Arabic-first AI on a Moodle base without surrendering the IP

🔵 **Why this pattern and not a tutor demo.** Two measurements from this pass fix the architecture
before any product decision: the Gulf mandates are **statutory and dated** (`SA` and `AE`
`curriculum_mandate` `MANDATED`, 2025/26), and **every one of the 51 readable grants in the Moodle
plugin family is `GPL-3.0-or-later`**. 🔴 So the obvious build — put the clever part in a Moodle
plugin — gives the clever part away. 🟢 The pattern puts the GPL boundary where it costs nothing.

### The three layers, with the licence of each stated

| layer | component | licence | why it is here |
|---|---|---|---|
| **1 · in-platform adapter** *(GPL, thin, contributed back)* | A `core_ai` provider plugin, 🆕 🟢 **cloned from [`ADORSYS-GIS/moodle-aiprovider_openaicompatible`](https://github.com/ADORSYS-GIS/moodle-aiprovider_openaicompatible)** *(`p404`: the live address, **8 d**; [`lmscloud-io`](https://github.com/lmscloud-io/moodle-aiprovider_openaicompatible) is its origin and is **93 d** — `CONTENT-COPY`, direction established)* | 🟡 **GPL-3.0-or-later** *(read from `version.php`; **no licence file** at any ladder path)* | Moodle's own supported extension point, so no core patching and no upgrade debt. 🟢 Both vendors' `classes/provider.php` is **byte-identical at 3,963 B** — a de-facto standard shim. 🔵 Keep it thin: auth, request shaping, error mapping. Nothing proprietary crosses into it. |
| **2 · the boundary** | An **MCP server** the plugin calls over the network | 🟢 **Yours — MIT/Apache or closed** | 🔵 GPL-3.0 is **not** network copyleft. Code the plugin merely *calls* across a process boundary is not a derivative work of it, which is what makes layer 3 ownable. 🔴 This boundary is the entire point of the pattern; collapse it and layer 3 becomes GPL. |
| **3 · the grounding and the IP** | Arabic curriculum corpus + retrieval + evaluation | 🟢 **Yours**, seeded from **MIT** sources | Seed content from [`openaziz00-sudo/Arab-Artificial-Intelligence`](https://github.com/openaziz00-sudo/Arab-Artificial-Intelligence) (**MIT**, 1,650 Arabic prompts / 17 categories) and teacher-facing scaffolds from [`kazoya/build-your-own-agent-ar`](https://github.com/kazoya/build-your-own-agent-ar) (**MIT**). 🔴 **Do NOT seed from** [`sartaj1995/arabic-tutor`](https://github.com/sartaj1995/arabic-tutor) (100 levels, 1,367 exercises — **no grant at the ladder**) or [`michaelsboost/ArabEngo`](https://github.com/michaelsboost/ArabEngo) (**CC-BY-NC-4.0**, NonCommercial). |

### Wiring it, concretely

1. **Fork the provider plugin** and point its endpoint at your gateway, not at a model vendor.
   🔵 Read the grant from `version.php`, not from the GitHub sidebar — 27 of this family's 51
   grants have **no licence file to read**.
2. **Stand the MCP server up outside the LMS**, exposing exactly the tools the curriculum needs
   (retrieve-objective, generate-practice, grade-free-text, explain-in-Arabic). 🔵 The parent- and
   teacher-facing MCP servers already on [`agents/top.md`](../agents/top.md) are the shape to copy.
3. **Ground on the corpus you own**, aligned to the UAE MoE's **seven curriculum areas** for an
   AE engagement and to the National Curriculum Center's scope for `SA`.
4. **Keep the evaluation harness on your side of the boundary.** 🟢 It is the deliverable the EU AI
   Act's Annex III conformity assessment will want evidence of for any EMEA client whose system
   touches assessment — and the same artefacts serve a Gulf ministry procurement.
5. **Contribute layer 1 upstream.** 🔵 It is GPL anyway; contributing it buys maintenance you would
   otherwise owe, and credibility with the one platform the client already runs.

### 🔴 What this pattern does NOT claim

🔴 **There is no Arabic-first platform to start from.** The entire permissive Arabic education
supply found on 2026-10-23 is **three repositories, 4 ★ at best, all created within six weeks**
([`arabic-supply-leg`](../evidence/arabic-supply-leg.2026-10-23-p401.tsv)). 🟢 Layer 3 is **built,
not assembled**, and the pattern says so rather than implying a stack exists. 🔵 That is also the
argument for moving now: the demand is statutory and the supply is not yet anybody's.

🔴 **And the one component that would make this cheap is the one that is unlicensed.**
`sartaj1995/arabic-tutor`'s 1,367 structured exercises are the single richest Arabic content asset
this base has found, and with **no grant at any ladder path** they cannot be used. 🟢 **An email to
that maintainer asking for an explicit MIT grant is a lower-cost first move than building the
corpus** — and it is the kind of ask that succeeds, because the repository already reads as
intended-open.

**🆕 Pass `p400` · reads and commit both 2026-10-23 — sixth pass of the day.** 🔴 **No pattern
was added: the one unshelved address this pass found is unlicensed, and there is nothing to
compose with an unlicensed repository.** 🟢 **Both axes of the two-axis pre-flight got sharper
anyway, and one of them got sharper in the dangerous direction.**

🟢 **The jurisdiction axis — APAC is no longer a blank.** Every recipe here is gated on
*(licence × jurisdiction)*, and the jurisdiction axis reads
[`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv). 🔴 **Until this pass that file answered
every APAC teaching-mandate query with a single `NOT_ESTABLISHED` row** — and in a pre-flight a
blank reads as *"no rule"*, which is the dangerous direction to be wrong in. 🟢 It now answers
with **seven** rows. The two that change a build:

- 🟢 **`CN-BJ | curriculum_mandate | MANDATED | 2025-09-01`** — **≥ 8 class-hours per academic
  year across all Beijing primary and secondary schools.** 🔵 Any recipe here that ships a
  tutoring or courseware surface into Beijing acquires a **contact-hour accounting**
  obligation: the deliverable must be able to *evidence* hours delivered per learner per year,
  which is an LRS/record-layer requirement, not a model requirement. 🔵 This base already holds
  the record-layer supply problem (`p396`: one 15 ★ MIT MCP bridge, 419 days dead, is the whole
  agent↔LRS supply) — 🔴 **so the obligation now has a named instrument and the stack to satisfy
  it is still the thinnest tier on these shelves.** That pairing is the pattern-relevant fact.
- 🟡 **`IN-CBSE | curriculum_mandate | MANDATED | 2026-27`, with `IN | NOT_ESTABLISHED`** — a
  recipe aimed at Indian Classes 3–5 must deliver **into Mathematics and "The World Around
  Us"/EVS**, because that is where the curriculum puts it; a standalone "AI for Class 3" surface
  is **mis-shaped for the only instrument that binds**, and AI proper does not begin until
  Class 6. 🔴 There is **no board exam**, so no assessment-integration pressure — which removes
  a requirement most recipes here would have assumed.

🟢 **The licence axis — the gate that admits candidates to a recipe now exists as code.**
Patterns here compose named repositories, so a pattern is only as good as the claim that its
parts are real and carried. 🔴 **That claim was being made with a bare-name grep**, which is a
substring match (`400-C`). 🟢 [`p400-candidate-membership`](code/p400-candidate-membership/README.md)
answers it by exact address over **both** of this base's address channels, and reports
`NAME-SUBSTRING-ONLY` as its own class so a candidate can no longer be dropped silently.
🔵 **Use it before adding a repository to any recipe below:**

    python3 -I compose/code/p400-candidate-membership/membership.py classify owner/name

🔴 **And the honest limit, stated so the pre-flight is not oversold:** the licence axis can be
settled first-hand from this session (`raw.githubusercontent.com` → **301**, payloads served);
the jurisdiction axis **cannot** (every policy host → **000**). 🔵 So every row in
`policy-matrix.tsv` is band `reported` by construction, and a recipe gated on jurisdiction is
gated on a single-channel claim. **Say so in the engagement, and re-read the instrument from a
session with egress before a deliverable depends on it.**

**🆕 Pass `p399` · reads and commit both 2026-10-23 — fifth pass of the day.** 🔴 **No pattern
was added, because no new supply arrived to compose with** — the supply legs returned seven
candidate addresses of which six were shelved and the seventh is not education-native.

🟢 **The two-axis pre-flight gets materially better without a single pattern changing.** Every
recipe here is gated on *(licence × jurisdiction)*, and the jurisdiction axis reads
[`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv). 🔴 **Until this pass that file answered
every LATAM teaching-mandate query with a blank** — 11 rows across `ai_literacy_instruction` and
`curriculum_mandate`, none of them LATAM — 🔴 **and a blank in a pre-flight reads as "no rule",
which is the dangerous direction to be wrong in.**

🟢 **It now answers with six rows.** The one that changes a build:

- 🔴 **`CO` · `Ley 2626 de 2026` · MANDATED · binding on official schools.** Any pattern here
  delivering curriculum or AI-literacy content into Colombian **public** education now has a named
  statute to conform to, and 🔴 **a `Feb 2027` deadline for the curricular guidelines** — which is
  the date an engagement plans against, not the **2026-08-24** sanction date.
- 🔵 **`AR`, `CL`, `MX`, `BR`, `UY` · ADVISORY_NONBINDING · `PE` · ADOPTED.** These bind nothing and
  must not be pitched as compliance drivers; they are **adoption** signals, and the honest use is
  scoping a pilot's ministry alignment, not selling a compliance deliverable.

🔵 **Recorded here as a change to how the existing recipes are gated, not as a new recipe** — the
same judgement `p398` made for the `OpenMAIC` commit-pinning rule. `Gap 399-A`.

**🆕 Pass `p398` · reads and commit both 2026-10-23 — fourth pass of the day.** 🔴 **No pattern was
added or amended, because no new supply arrived to compose with.** Eight search legs returned one
address this base did not hold, and 🔴 **it is archived** — which disqualifies it as a pattern
component outright. 🔵 **The one recommendation change is a pinning rule, not a new recipe:** every
pattern here that names [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) should pin a
**commit**, not a tag — `v1.3.0-rc.1` (2026-10-22) opened while `v1.2.0-rc.1` (2026-10-04) had still
not reached stable, so a tag-based dependency on this project has nothing stable to point at. 🔵
Recorded here rather than as a new pattern because it changes **how** the existing ones are built,
not **what** they are. `Gap 398-C`.

**Pass `p397` · reads and commit both 2026-10-23 — third pass of the day.** 🟢 **`p396` ranked
re-running the xAPI 2.0 bake-off second, on the grounds that *"three claimants at 1 star between them
will move fast or die; either outcome changes the recommendation."* They moved — and they did not
move together.** One new pattern, and `Pattern AE` amended rather than restated. Evidence:
[`record-layer-redating`](../evidence/record-layer-redating.2026-10-23-p397.tsv) ·
[`shelf-lineage`](../evidence/shelf-lineage.2026-10-23-p397.tsv).

## 🟢 `Pattern AE` AMENDED — the xAPI 2.0 bake-off now has an activity ranking

🔵 `Pattern AE` told a studio to adjudicate three zero-star LRS claimants itself, because *"reputation
cannot decide this."* That still stands. 🟢 **What `p397` adds is the one signal that was missing:
which of them is actually being built.** Dated on the git channel, never on the HTML "Updated" column
(`396-G`):

| candidate | stack | `p396` | `p397` HEAD | days | reading |
|---|---|---|---|---|---|
| [`nurullahturkoglu/xapi-dotnet`](https://github.com/nurullahturkoglu/xapi-dotnet) | ASP.NET Core | "under 75 d" | `0d47d65` 2026-10-21 | 🟢 **1** | 🟢 **under active daily development** |
| [`codetakt/kiva`](https://github.com/codetakt/kiva) | Rust, F\* proofs | "under 75 d" | `addf100` 2026-10-21 | 🟢 **2** | 🟢 **also moving**; 🔵 still the only one whose README *withdraws its own conformance claim* |
| [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) | TypeScript/Hono/Postgres | "under 75 d" | `4d18e0c` 2026-08-08 | 🔴 **75** | 🔴 **has not moved at all** since `p396` measured it |

🟢 **So the "all three are under 75 days" sentence has split into two live projects and one
stalled one**, and the bake-off order changes accordingly: 🟢 **run `xapi-dotnet` and `kiva` first**,
and treat `xapi-lrs` as the control rather than a contender until it commits again.

🔴 **The tooling half of `Pattern AE` is the part that has aged, and it matters more than the
candidates.** [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
is 🟢 MIT, 78 ★ — and **`5bc232d`, 2025-09-04, 413 d**, unchanged. 🔵 **You are asked to certify
2.0 conformance with a suite that has not been touched in fourteen months**, while the implementations
it judges change weekly. 🟢 [`yetanalytics/lrs-test-runner`](https://github.com/yetanalytics/lrs-test-runner)
(Apache-2.0, **6 d**) and [`yetanalytics/xapi-schema`](https://github.com/yetanalytics/xapi-schema)
(**6 d**) are both live, so the **CI harness around the suite is maintained even though the suite is
not.** 🔴 **Quote that asymmetry to a client before you quote a pass rate.**

## 🆕 `Pattern AF` — prove provenance BEFORE you prove the licence, in two commands

**When.** Any engagement that is about to adopt, fork or warrant an open-source education component
— and especially when the candidate came out of a search result rather than a standards document.

🔴 **Why it goes first.** A licence read **cannot** tell a fork from its upstream: the payload is
usually byte-identical, so the grant channel is blind by construction (`395-A`). A star read cannot
tell a rename from a fork either: GitHub answers on the old organisation path indefinitely and shows
the same stars. 🔴 **On these shelves, 8 of 15 shared-root pairs were renames and 7 were real
forks** — and nothing short of comparing commits separates them.

**The recipe, and it needs no API, no HTML and no credentials.**

1. **Root commit** — shared root means shared ancestry:
   `git clone --filter=blob:none --no-checkout -q https://github.com/OWNER/REPO d && git -C d rev-list --max-parents=0 HEAD`
2. **HEAD** on the same clone: `git -C d rev-parse --short=12 HEAD`
3. **Adjudicate**: same root + same HEAD → **one artefact, two addresses** (fold them, cite the
   current path); same root + different HEAD → **a real fork** (now decide which side to carry);
   distinct roots → **unrelated** despite the shared name; either side unresolvable → **inconclusive**,
   never "independent".
4. 🟢 **Then date both sides**, because step 3 tells you the fork is real and nothing about whether
   anyone maintains it. `T40` is the cautionary case: `ucfopen/pylti1.3` is a genuine institutional
   fork of `dmitry-viskov/pylti1.3`, and **both are over 1 370 days dead.**
5. **Only now read the grant**, and read it by enumerating the tree
   (`git ls-files | grep -iE '(licen[cs]e|copying)'`) rather than guessing filenames — that is how
   this pass found [`gradescope/autograder_samples`](https://github.com/gradescope/autograder_samples)
   ungranted at root with vendored third-party MIT two directories down.

🟢 **Wired and runnable:** `bash compose/code/p397-shelf-fork-audit/lineage.sh OWNER_A/REPO OWNER_B/REPO`,
with `make shelf-fork-candidates` deriving the candidate pairs from the shelves themselves and
`make gate-shelf-fork` holding 11 controls. 🔴 **Stated limit:** a squashed or re-rooted fork reads as
independent — no false positives, possible false negatives.

🔵 **Cost: two blobless clones per pair, a few seconds each.** `p397` ran 21 pairs inside one pass.

### 🆕 `p402` AMENDMENT — a cheaper front door, and the missing step 3b

🟢 **Front door: `git ls-remote` needs NO clone.** Comparing the **full ref set** of two addresses
answers the identity question for the price of one network round-trip each:

```sh
git ls-remote https://github.com/OWNER/REPO | sort | sha256sum   # ref-set fingerprint
```

Identical ref set → **one repository**. 🔴 **Identical HEAD alone is NOT identity** — `p370` demoted
five pairs from `STALE` to `DISTINCT` on exactly that, because *a redirect serves ONE repository, so
a different ref set is a different repository*. `sharziki`↔`rohanmuppa` `purdue-mcp` share HEAD
`6922f1f301dd` and have **5 vs 3** refs; `Halleck45`↔`chinobv` `openpronounce` share HEAD
`74bc17ea406e` and have **10 vs 4**. 🔵 Use the clone arm (steps 1–2) when you need the **root**, to
separate a rename from an unrelated repo that merely shares a name.

🔴 **Step 3b, which this pattern was missing.** Step 3 says *"fold them, cite the current path"* and
gives **no way to find that path**. The ref set proves *one repository*; it never says *which
address is canonical*. 🟢 **The channel that does: fetch EITHER address over HTTPS and read the
header/breadcrumb of the page you LAND ON.** GitHub serves a rename or transfer as a redirect, the
fetcher follows it, and the page names the canonical owner — plus the archive banner, the licence
and any `forked from` parent in the same read.

🔴 **The trap, stated because it cost this base ~52 passes.** The redirect is followed **silently**,
so two stale addresses both report *"not a fork"* with **identical star counts** — indistinguishable
from two independent repositories. *Same stars · no fork line · two owners* is the signature.
🟢 It is how `p402` found that `ease`'s canonical address is **neither** candidate in the register
but a third owner, [`openedx-unsupported/ease`](https://github.com/openedx-unsupported/ease), and
closed `ACTION ZZ-al`.

🔵 **Engagement rule.** Warrant the **canonical** address, not the one in the search result — and
when the canonical owner is named `*-unsupported` or carries an archive banner, that **is** the
stewardship finding. Read it before promising a client a maintained dependency.

**🆕 Pass `p396` · reads and commit both 2026-10-23.** Two patterns, both built on grants and dates
read first-hand this pass:
[`record-layer-dating`](../evidence/record-layer-dating.2026-10-23-p396.tsv).

## 🆕 `Pattern AD` — the agent that writes to the institution's record, not just its own memory

**When.** The client needs to show *someone else* — an accreditor, a regulator, a district board, a
parent — what the AI did and what the learner actually demonstrated. This is every North America K-12
engagement under Oklahoma-style teacher-review and opt-out rules, every EU deployer under Article 26
logging, and the governance sale that `intel/market.md` identifies as the LATAM entry point.

🔴 **Why you cannot just use the agent's memory.** `DeepTutor`, `inno-agent` and every other tutoring
agent on this shelf keep private, vendor-shaped memory designed for conversational continuity. It is
not an evidence record, it does not survive replacing the agent, and no registrar will read it
(`T37`).

**Components, all dated this pass.**

| Role | Component | Licence | Age | Note |
|---|---|---|---|---|
| Record store (Python shop) | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 MIT | 🟢 10 d | France Université Numérique; Open edX Aspects' own LRS |
| Record store (JVM shop) | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 | 🟢 21 d | 144 ★; SQLite/Postgres/MariaDB/MySQL |
| Record store (.NET shop) | [`nurullahturkoglu/xapi-dotnet`](https://github.com/nurullahturkoglu/xapi-dotnet) | 🟢 Apache-2.0 | 🟢 1 d | 🔴 0.x, 1 ★ — gate on a conformance run |
| Platform emitter (Moodle) | [`davidpesce/moodle-logstore_xapi`](https://github.com/davidpesce/moodle-logstore_xapi) | 🔴 GPL-3.0 | 🟢 2 d | 82 ★; GPL because every Moodle plugin is |
| Agent ↔ LRS bridge | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 MIT | 🔴 **419 d** | **the weak link — see below** |
| Launch into the LMS | `packbackbooks/lti-1-3-php-library` / `ltijs` / `lti-tool` (`p395`) | 🟢 permissive | 🟢 1–9 d | pick by runtime |

**Wiring.** Agent → MCP (`learnmcp-xapi`) → LRS (`ralph` or `lrsql`); LMS → emitter
(`moodle-logstore_xapi`) → *the same* LRS; agent launched from the LMS over LTI 1.3 so the learner
identity on both paths is the same subject. 🔵 **The single design decision that makes this worth
building:** the agent's statements and the platform's statements land in **one** store against **one**
identity, so "what did the AI do for this student" and "what did this student do" are one query.

🔴 **Scope this honestly at estimate time.** `learnmcp-xapi` is 15 ★ and has not moved in fourteen
months. 🟢 It is MIT, it is small, and the xAPI statement shapes it needs are specified — so treat it
as **a reference to fork and own, budgeted as build, not as a dependency**. Anyone quoting it as
maintained third-party infrastructure will be wrong by about a year.

**Effort.** 6–8 weeks for a single-LMS, single-agent deployment on an existing Moodle or Open edX;
add 3–4 weeks to own the MCP bridge properly rather than vendoring it.

## 🆕 `Pattern AE` — choosing an xAPI 2.0 LRS when every candidate has zero stars

**When.** The client specified xAPI 2.0 / IEEE 9274.1.1 — increasingly common in defence, aviation,
regulated corporate training and any procurement written against the current standard.

🔴 **The situation, measured.** No adopted open-source LRS implements 2.0. `lrsql` (144 ★) and Ralph
(51 ★) are both 1.0.3. The three claimants hold **one star between them**: `pelotech/xapi-lrs` (0 ★,
TypeScript/Hono/Postgres), `codetakt/kiva` (0 ★, Rust, F* proofs) and `nurullahturkoglu/xapi-dotnet`
(1 ★, ASP.NET Core). 🔴 **Reputation cannot decide this**, and each project's own conformance claim
is self-reported — `kiva`'s README goes so far as to withdraw its own repository blurb, saying
equivalence with the 2025 edition *"has not been established"* and that source traceability *"does
not establish implementation conformance."*

🟢 **So adjudicate it yourself, with permissive tooling that already exists.**

1. Stand up each candidate against a **throwaway** Postgres — the suite persists data and its README
   warns it *"should not run against a production LRS endpoint."*
2. Run [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
   (🟢 MIT, 78 ★, Node) with `--xapiVersion 2.0.0`, then again with `1.0.3` — a conformant 2.0 LRS
   must still accept 1.0.x statements.
3. On the JVM, drive the same suite from CI with
   [`yetanalytics/lrs-test-runner`](https://github.com/yetanalytics/lrs-test-runner) (🟢 Apache-2.0,
   6 d) so the result is a build artefact rather than a screenshot.
4. 🟡 Read failures with judgement: a .NET implementer reports the suite *"sometimes expects more
   than the standard requires"* *(secondary)*, and the suite is **413 days old** while all three
   candidates are under 75 days. A failure is a conversation, not a disqualification.

🟢 **Hedge the choice structurally.** `pelotech/xapi-lrs` states its schema matches `lrsql` v0.9.5's
Postgres shape, so an `lrsql` database can be taken over. 🔵 This pass's fork arm confirms the two are
**independent codebases, not a fork** (distinct root commits `b1bfc0f67292` vs `f9e81c891b9a`) — so
this is genuine schema compatibility between rivals, which is the rare case where a client can start
on the 144 ★ 1.0.3 store and migrate to the 0 ★ 2.0 store without a data conversion.

**Effort.** 2–3 weeks for the bake-off and a reproducible CI conformance job; the result is reusable
across every later engagement on this layer, which is the main reason to do it once properly.


# Compose patterns — education

**🆕 Pass `p395` · reads and commit both 2026-10-23.** Two patterns, both built on grants and **dates**
read first-hand this pass: [`verified-repos`](../evidence/verified-repos.2026-10-23-p395.tsv) ·
[`lti-layer-dating`](../evidence/lti-layer-dating.2026-10-23-p395.tsv).

## 🆕 `Pattern AC` — the JVM-or-Go client's LTI edge (the one this base could not quote before)

**When.** The client's platform team owns **Java** or **Go**, and an agent has to launch from their
Moodle, Canvas, Blackboard or D2L. This is most enterprise work and much of European public sector.

🔴 **Why the obvious route is closed.** The only permissive **Java** LTI 1.3 core is
[`UOC/java-lti-1.3-core`](https://github.com/UOC/java-lti-1.3-core) (MIT) — **1,193 days dead**. The
Go options are [`StevenWeathers/peregrine-lti`](https://github.com/StevenWeathers/peregrine-lti)
(Apache-2.0, **679 d**, pre-1.0 API), [`macewan-cs/lti`](https://github.com/macewan-cs/lti) (MIT,
**1,919 d**, self-declared unstable, **deep linking unimplemented**) and 🆕
[`astiusa/lti`](https://github.com/astiusa/lti) (MIT, **794 d**, a `p404`-measured **strict superset**
of `macewan-cs` — which inherits the same instability warning, untouched by its two extra commits). 🔴 An unmaintained library doing
**OAuth 2 / JWT signing and key rotation** is a *security* dependency — the same argument that
demoted `1EdTech/lti-1-3-php-library`. Do not put a client's identity flow on any of the three.

**Wire it like this.**

1. **LTI edge — [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool)** (🟢 MIT, HEAD **1 d**,
   `@lti-tool/core` v1.3.2). Serverless-native: Lambda, Workers, Hono, with OIDC, **Assignment and
   Grade Services**, Names and Role Provisioning, Deep Linking and Dynamic Registration all
   implemented, and the session store chosen at deploy time. 🟡 Prefer
   [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (🟢 Apache-2.0, **9 d**, 207 npm releases)
   instead when the client wants a long-running Node process and already runs Mongo.
2. **The hop.** The edge validates the launch, then forwards a **signed, short-lived internal token**
   carrying only `sub`, context, roles and the resource link to the JVM/Go service. 🔵 The agent never
   parses an LTI message, which is the whole point: the standards surface stays in the runtime where
   it is maintained.
3. **The agent** stays in Java or Go — the client's own service, unchanged.
4. **Grades back** through the edge's AGS client, never direct from the agent. One component holds the
   platform credentials.

🟢 **Why this beats forking a dead library:** `lti-tool` is 1 day old and `ltijs` 9, so key rotation
and spec drift are somebody's job. 🔴 **Cost to state in the proposal:** one extra deployable and one
extra network hop — *and* `lti-tool` is **8 ★ with no production claim** (its README's
*"Production-ready security features"* heading is about the security section, not the project), so
pilot it; `ltijs` is the safer default for a ministry. 🔵 Note this is the architecture `p391`
recommended for Python and `p392` correctly withdrew when `django-lti` turned up live at 2 days. **It
stands for Java and Go because the dating says so, not because it is the usual advice.**

## 🆕 `Pattern AD` — a learner-facing agent shell with a curriculum you are actually allowed to ship

**When.** The client wants a personal tutor that remembers a learner across months, and the
deliverable must survive a legal review.

1. **Shell — [`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent)** (🟢 MIT, **1.3k ★**, HEAD
   **10 d**). You get the parts that are expensive to build: **L1** learner profile, **L2** a native
   wiki knowledge base, **L3** session records with cross-conversation retrieval, a **cron scheduler**
   for proactive check-ins, and a workspace-scoped **Practice Lab** with an in-browser terminal.
   🔵 It sits on the Pi coding-agent SDK (MIT) *without modifying its kernel*, so the upgrade path is
   npm, not a fork.
2. 🔴 **Do NOT ship its skill library.** The companion
   [`Chloris-Blaxk/inno-agent-hub`](https://github.com/Chloris-Blaxk/inno-agent-hub) — skills and
   workspace presets — is **ungranted on every arm** (no licence file, no manifest field, no README
   grant, all three enumerated). Read it for shape; author your own.
3. **Curriculum — granted sources only.** [`oppia/oppia`](https://github.com/oppia/oppia)
   (🟢 Apache-2.0) for misconception-aware lesson structure, and
   [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (🟢 MIT) when the
   deployment is offline-first. 🔴 **Avoid grounding the tutor on
   [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) without legal sign-off**
   — `ODbL-1.0 AND CC-BY-SA-4.0`, and the **CC-BY-SA half reaches generated content**, so a curriculum
   document produced from it can inherit share-alike. That is `Pattern H`'s warning, and it is the
   trap this pattern is most likely to fall into.
4. **Launch from the LMS** with `Pattern AC`'s edge, so the tutor is reachable where students already
   are.
5. 🔴 **Regulatory stop, before any design work.** The moment this agent **grades**, **assigns a
   learner to a programme**, **assesses their appropriate level**, or **monitors behaviour during a
   test**, it is **Annex III ¶3 high-risk** in the EU and needs the human-in-the-loop and
   documentation posture. 🔴 And **no emotion inference, ever, in an EU educational setting** — that is
   prohibited outright, not assessable. Keep the memory layers descriptive (what was practised, what
   was missed) and never affective.

🟡 **Honest limits.** `inno-agent` is a **single-learner companion** — there is no cohort, roster or
teacher dashboard in it, so an institutional pilot needs that built. Its IM channels ship as **Feishu
and WeChat**, so a non-APAC deployment replaces the messaging layer. And at **10 days old with a June
2026 technical report**, it is a strong pilot base, **not** a ministry platform this quarter.

**🆕 Pass `p394` · reads 2026-10-22, committed 2026-10-23.** Two new patterns, both built on grants
read at the payload this pass. 🟢 **`Pattern AB`** — the **R statistics course graded automatically**,
closing the hole `p393` named when it pointed out that this base's most-adopted *maintained*
autograder grades R
while the shelves held no R components; its delivery layer is permissive (`gradethis` MIT, `learnr`
Apache-2.0, `ottr` BSD-3) and its measurement layer is GPL behind a process boundary, and its last
step is **the only offline assessment loop in this base** (`cran/exams` NOPS: printed, scanned, marked
automatically, paper audit trail). 🟢 **`Pattern AC`** — **give teachers an assistant builder instead
of building their assistants**, on **LAMB** (GPL-3, UPC Barcelona + UPV/EHU, peer-reviewed), which
publishes each teacher-authored assistant into Moodle as an **LTI external tool** so the LMS is never
forked. 🔴 Both patterns carry a hard stop at grading: under the EU AI Act, systems that grade
learners or influence access to qualifications are **high-risk and require conformity assessment
before deployment**, so the grading step is scoped as a separate assessed workstream rather than sold
in the same phase.

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/compose-patterns.md`](../archive/2026-10-22-p383-pre-rewrite/compose-patterns.md).

Every repo named here was verified first-hand on 2026-10-22 —
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv). Licences are read from the
payload at the repository's **real default ref**, which for 13 of 58 live addresses is not `main`.

**The governing constraint for all of these:** the platform tier is copyleft, the agent tier is
permissive. Every pattern below therefore puts a **documented interop boundary** — LTI 1.3, MCP, or
web services — between client-owned code and the platform. None of them forks an LMS.

🆕 **`p389`** adds **`Pattern Q`** (the generated classroom, the greenfield answer when there is no
LMS to bolt onto), gives **`Pattern B`** a maintained mastery model, and gives **`Pattern D`** two
components that remove its server. Every repository named in those changes was **dated** this pass —
last commit at the real default ref:
[`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv). 🔵 **Read a date as a cost line:**
a permissive repository nobody has touched in eight months is something you *vendor and maintain*, not
something you *integrate* — which is why `Pattern B` vendors `pybryt` and why `Pattern Q` pins a ref.

---

## Pattern A — Tutor over the client's existing LMS (no fork, no copyleft exposure)

**For:** a client who already runs Moodle or Canvas and wants a tutor that knows the actual course.

**Wiring:**
1. **Expose the LMS.**
   - *Moodle:* install **`webservice_mcp`** from Moodle's own plugin directory (Moodle 4.5–5.2,
     latest release 23 Jul 2026). It serves Moodle's external functions as **MCP tools over
     JSON-RPC 2.0**, gated on the `webservice/mcp:use` capability. Configured inside Moodle — no
     patch to core, so **no GPL obligation reaches your agent**.
   - *Canvas:* [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (**MIT**) for courses,
     assignments, submissions, grading, rubrics, students; or the fork
     [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (**MIT**) which adds office-hour
     appointment groups, syllabus read/write, student groups and course-content copy.
   - 🆕 `p390` *Open edX:* skip the MCP hop and run **inside** the platform as an **XBlock** — and the licence maths
     works out better than it looks. The platform is **AGPL-3.0**, but the component API your plugin imports,
     [`openedx/XBlock`](https://github.com/openedx/XBlock), and the [`xblock-sdk`](https://github.com/openedx/xblock-sdk)
     you develop against are both **Apache-2.0** (`LICENSE.TXT`, both dated 2026-10-22). **So the XBlock you write can stay
     MIT or proprietary while running in an AGPL host** — no fork, no LTI hop, and full access to course state.
     [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (MIT, Colombia) is the working proof.
     🔴 **Check the boundary per package, not per org:** [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning)
     and the `frontend-app-*` MFEs are **AGPL-3.0**, so an import from those pulls network copyleft straight back in.
     Keep the plugin's dependency list to `XBlock` plus your own code and audit it in CI.
   - 🟡 **Grant status, corrected:** the plugin repo
     [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) has **no
     root licence file**, but `version.php` carries the full **GPL-3.0-or-later** header Moodle
     requires of every plugin — so it is granted, and GPL is survivable because you reach it over
     JSON-RPC rather than linking to it.
     [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) is
     **manifest-only MIT** (`package.json` declares it; the file it names is absent from the tree).
     🔴 **Do not use** [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp): no licence file
     **and** no `license` field in `pyproject.toml` — genuinely no grant to redistribute.
2. **Ground it in the course material.** [infiniflow/ragflow](https://github.com/infiniflow/ragflow)
   (**Apache-2.0**) over the course files, with
   [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)
   (**Apache-2.0**) for the PDF/DOCX/PPTX/scan reality. If the client has lecture video,
   [opencast/opencast](https://github.com/opencast/opencast) transcripts are the richest corpus
   available and nobody is using them.
3. **Give it pedagogy and memory.** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
   (**Apache-2.0**) for persistent learner memory plus material-grounded tutoring. If the client
   wants explanation *pitched* to the learner's state rather than merely retrieved, look at
   [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) — but it is **GPL-3.0**, so
   run it as a separate service, not as a library inside the deliverable.
4. **Front it.** [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**) — SSO,
   per-user quota, provider routing and the **audit log** that gets the build past a data-protection
   officer. (Not `open-webui`: its `LICENSE` is 2,819 B of BSD-3 text **plus** a branding
   restriction and a CLA.)
5. **Prove it.** [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
   (**MIT**) with [MMLU](https://github.com/hendrycks/test) (**MIT**) and
   [GSM8K](https://github.com/openai/grade-school-math) (**MIT**), scored on the client's own
   subject mix, before and after.

**Licence posture:** client-owned code is MIT/Apache/BSD throughout. The only copyleft component is
the LMS itself, reached over a published protocol. **Deliverable stays closed if the client wants it
closed.**

---

## Pattern B — Autograding that assesses the approach, not just the output

**For:** CS, data-science and engineering programmes drowning in submissions.

**Wiring:** [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) (**BSD-3**) for
identical per-cohort compute → [jupyter/nbgrader](https://github.com/jupyter/nbgrader)
(**BSD-3**) for the release/collect/autograde/return lifecycle →
[ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) (**BSD-3**, default ref
`master`) for container-isolated grading at cohort scale →
[microsoft/pybryt](https://github.com/microsoft/pybryt) (**MIT**) to check **how** the student got
there, not only whether the answer matched →
[jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) (**BSD-3**) so the LLM explains
*why* the approach was wrong, inside the notebook the student is already in.

**Why this combination:** pybryt is the piece everyone misses. An LLM that reviews output rewards
the student who guessed; pybryt's annotations let you detect the *intended method* and then have the
model give feedback on the method. **Fully permissive — BSD-3 and MIT only, zero copyleft.**

🔴 🆕 `p387` **Vendor pybryt; do not install it.** PyPI `pybryt` has shipped nothing since
**v0.7.0, 2022-04-28** — four and a half years — so a client support contract cannot rest on it as a
dependency. The pattern does not change: copy the annotation approach (and, licence permitting under
its MIT grant, the code) into the deliverable and maintain it there, with the maintained BSD-3
halves of this stack (`nbgrader`, `otter-grader`) carrying the running infrastructure. Dates:
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv).

🟢 🆕 `p388` **And the notebook-tutor half now has a maintained component, which changes what you
vendor.** [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) (**BSD-3**,
`main` · `139bb11`, **v0.3.2, 7 releases, → 2026-09-25**, from a known Jupyter-ecosystem maintainer)
replaces the ad-hoc "wire `jupyter-ai` into the grading loop" step with a component built for exactly
this job:

- A per-cell **Explain Code** button sends the cell source, the kernel language, **the error
  traceback**, and the preceding cells up to the last markdown cell **as the exercise statement** —
  so the model sees the task, not just the broken line.
- 🟢 **The tutor persona lives in a `TUTOR.md`, discovered by walking up from the notebook's
  directory to the server root.** Each course, module or folder carries its own pedagogy **in version
  control**. This is the single most useful thing on this shelf for a client engagement: *"AI must
  not give the answer"* stops being a prompt someone pasted and becomes a reviewable file in the
  course repository, diffable and auditable per cohort.
- 🟢 **`reference_solution` and `evaluation_criteria` ride in cell metadata, ROT13-encoded** so they
  are not casually readable by a student holding the notebook — the same instinct as `pybryt`'s
  annotations, shipped in a maintained package.

**Revised wiring:** `jupyterhub` → `nbgrader` → `otter-grader` for the lifecycle and
container-isolated grading (all BSD-3, all maintained) → **`jupyter-ai-tutor`** for the in-notebook
explanation layer, configured by a per-course `TUTOR.md` → **vendored `pybryt` annotations** for
approach assessment, maintained inside the deliverable as `p387` requires. 🔵 Note the division of
labour this produces, and it is the one the guardrail below wants anyway: `jupyter-ai-tutor` **explains
and never grades**, `nbgrader`/`otter-grader` grade and never explain. 🟡 It requires
`jupyter-ai-jupyternaut` (<0.1) for the agent, so pin that bound.

🟢 🆕 `p389` **And the missing third component: the mastery model.** Everything above assesses a
*submission*. Nothing in it answers the question a programme director actually asks — **which skills
has this student mastered, and what should come next** — and this base has carried that gap while
recommending a dependency that stopped shipping in 2022. The maintained answer is
[**CAHLR/pyBKT**](https://github.com/CAHLR/pyBKT) (**MIT**, real ref `master`, **last commit
2026-10-21 — 1 day**), from UC Berkeley's CAHLR, who also maintain
[**OATutor**](https://github.com/CAHLR/OATutor) (**MIT**, `main`, **1 day**) as the tutoring front end
built on it.

- **What it adds to this wiring:** fit **Bayesian Knowledge Tracing** on the client's *own*
  `nbgrader`/`otter-grader` outcome logs — one row per (student, skill, attempt, correct) — and you get
  per-skill **learn, guess, slip and forget** parameters plus a running mastery probability per student.
- 🟢 **Why it is the defensible choice and not just the available one:** those four parameters are
  **inspectable numbers a client can argue with**, re-estimated on their own cohort. "The model thinks
  Ana has not mastered partial fractions, with these parameters fitted on this data" survives a
  procurement review; "the LLM judged her weak" does not. North American and Maryland-style rules that
  bar AI from high-stakes decisions about students are satisfiable here precisely *because* the
  decision rule is a published model rather than a generation.
- **Revised wiring, end to end:** `jupyterhub` → `nbgrader` → `otter-grader` (lifecycle + isolated
  grading) → **`pyBKT`** fitted on the outcome log (mastery per skill) → **`jupyter-ai-tutor`** with a
  per-course `TUTOR.md` for in-notebook explanation → **vendored `pybryt` annotations** for approach
  assessment. 🟢 **Still fully permissive: BSD-3 and MIT only, zero copyleft.** 🔵 The sequencing
  matters: `pyBKT` decides *what to work on*, the tutor explains *why the attempt failed*, and the
  graders remain the only components that produce a grade.
- 🟡 **Cold start is the real constraint**, not the licence: BKT needs interaction history. For a new
  cohort, serve `OATutor`'s scaffolds with default parameters, log, and re-fit at the end of the first
  module — and say so in the estimate rather than discovering it in week three.

**Guardrail:** where DC-style rules apply, AI must not be the grader of record. Configure the LLM as
a **feedback generator with a human grade-of-record** and keep the audit trail; that configuration is
the deliverable, not a disclaimer. 🆕 `p389` The same rule governs the mastery model: a BKT mastery
probability is **advisory input to a human decision**, and the moment it auto-finalises anything
consequential it is the "sole basis for a decision without meaningful human review" that Vietnam's
Decision 33/2026 and EU Annex III both reach.

---

## Pattern C — Citation-grounded academic assistant (and the EU compliance story that comes free)

**For:** higher-ed research support, library services, graduate programmes.

**Wiring:** [Future-House/paper-qa](https://github.com/Future-House/paper-qa) (**Apache-2.0**) as
the answer engine → [AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar)
(**Apache-2.0**) or [allenai/ai2-scholarqa-lib](https://github.com/allenai/ai2-scholarqa-lib)
(**Apache-2.0**) for multi-paper synthesis →
[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) (**Apache-2.0**)
for ingest → [LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**) as the campus gateway.
For guided-inquiry assignments, [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
(**Apache-2.0**) as the student-facing research scaffold.

**The compliance argument:** paper-qa **declines to answer** without retrieved evidence. Under
**EU AI Act Art. 50** (transparency, live from **2 Aug 2026** — *not* delayed by Regulation (EU)
2026/1744) a system that cites its sources and refuses otherwise is dramatically easier to document
than one that generates fluently. Build the refusal behaviour in, then point at it in the
conformity file. **Fully Apache-2.0/MIT.**

---

## Pattern D — Offline-first deployment for connectivity-constrained regions

**For:** LATAM, African and rural APAC deployments — including the nine countries in the Google.org
AI-literacy rollout (Argentina, Brazil, Chile, Colombia, Dominican Republic, El Salvador, Mexico,
Peru, Uruguay).

**Wiring:** [learningequality/kolibri](https://github.com/learningequality/kolibri) (**MIT**,
default ref 🔴 `develop`) as the edge runtime — offline-first by design, not a degraded mode →
a small local model on the same device for the tutoring loop →
[FSRS](https://github.com/open-spaced-repetition/fsrs4anki) (**MIT**) for scheduling review, because
retention is the one outcome measurable without a network →
content authored in [H5P](https://github.com/h5p/h5p-php-library) — 🟡 **GPL-3.0, keep it as
runtime content, not linked code** → periodic sync to the central LMS over
[LTI 1.3](https://github.com/Cvmcosta/ltijs) (**Apache-2.0**) when a link is available. 🆕 `p392` **Use a maintained implementation, and pick it by language — all three majors have one.** **Python:** [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) (🟢 MIT, PyPI v0.10.1, HEAD 2026-10-20) **in-process** for a Django agent, or [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (🟢 BSD-3) for a JupyterHub. **Node:** `ltijs` (Apache-2.0, npm v7.0.7, 2026-10-06), or [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 MIT, npm `@lti-tool/core` v1.3.2) when the target is **Lambda or Cloudflare Workers**. **PHP:** `packbackbooks/lti-1p3-tool` (Apache-2.0, packagist v6.4.4). 🔴 **Not** the standards-body copy `p390` cited (2,333 days stale) and **not** `pylti1.3` (1,431 days) — but `p391`'s conclusion from that second fact, *"a Python agent sits behind a Node or PHP edge rather than speaking LTI itself"*, is **withdrawn**: `Gap 391-A` is closed and the extra service comes out of the budget.

**Why FSRS matters here:** it has published parameters, so "the student is retaining more" is a
number you can defend to a ministry, offline, without telemetry.

🟢 🆕 `p389` **Two components that remove a server from this pattern, which is the cost line that
actually kills offline deployments.**

1. **Lesson delivery with no application server at all.**
   [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (**MIT**, committed **0 d**) exports a
   finished classroom as **one self-contained offline HTML file that plays the lesson** (or as a PPTX
   that keeps every scene). 🔵 **So the authoring server and the delivery target separate cleanly:**
   generate lessons once where there is power and bandwidth — a ministry office, a regional hub, a
   studio — and ship HTML files to the edge, where they need nothing but a browser. That is a
   fundamentally cheaper edge than "a Kolibri server per school", and the two compose: Kolibri remains
   the catalogue, progress store and sync layer; the exported HTML is the content it serves. 🟡 The
   export is a *playback* artefact — the agentic mid-lesson chat needs the server — so scope it as
   narrated, interactive courseware, not as a tutor that answers back offline.
2. **Notebook exercises with no per-student compute.**
   [jupyterlite/jupyterlite](https://github.com/jupyterlite/jupyterlite) (**BSD-3**, 6 d) runs the
   kernel **in the browser via WebAssembly**: no container, no install, no server, and it works offline
   once the page is cached. For a CS or data-science module this deletes the single largest
   infrastructure line in `Pattern B` at the edge. 🟡 No server also means no server-side autograding —
   collect the notebook and grade it with `nbgrader` when a link is available.

🔵 **What this pattern now says to a ministry.** The old answer was "a server per school, syncing when
it can." The 2026 answer is **generate centrally, deliver as files, compute in the browser, sync
progress when a link exists** — and every component in it is MIT or BSD-3, so the ministry owns the
deliverable outright. 🔴 One licence caution unchanged: H5P content stays **runtime content** under
GPL-3.0, never linked code.

---

## Pattern E — Sovereign EMEA public-sector stack

**For:** European public-sector clients demanding both data sovereignty and code ownership.

**Wiring:** **[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, default ref `master`)**
as the platform — **the only major open-source LMS a studio can extend with closed code** →
[serlo/serlo.org](https://github.com/serlo/serlo.org) (**Apache-2.0**) or
[oppia/oppia](https://github.com/oppia/oppia) (**Apache-2.0**, default ref `develop`) for structured
content → [openfun/richie](https://github.com/openfun/richie) (**MIT**, default ref `master`) as the
public catalogue → permissive agents over LTI 1.3 → all EU-hosted.

**The alternative, when the client insists on the openDesk lineage:** **ILIAS (GPL-3.0, default ref
`release_11`) + OpenProject behind a single SSO** — the ZenDiS pattern, and ZenDiS co-develops with
France's DINUM (LaSuite). 🔴 **But do not quote "8,600 schools":** that figure traces to a single
news item, and this pass found **no school deployment of openDesk in any source**. Named users are
administrative bodies. Sell the architecture, not the number.

**Dated compliance roadmap to attach to the bid** — this is the part competitors get wrong:
| obligation | when | status |
|---|---|---|
| Art. 4 AI literacy (every organisation using AI) | **since 2 Feb 2025** | 🔴 already binding |
| Emotion recognition in education | **prohibited since 2 Feb 2025** | 🔴 design it out |
| Art. 50 transparency | **from 2 Aug 2026** | 🔴 **not delayed** |
| Stand-alone high-risk education systems (admissions, assessment, proctoring, AI-detection in assessment, path-steering personalisation) | **2 Aug 2026 → 2 Dec 2027** per **Regulation (EU) 2026/1744** (OJ 24 Jul 2026) | 🟢 14 months of runway |

---

## Pattern F — Teacher-facing instructional assistant (the pattern the market and the regulator agree on)

**For:** LATAM and ANZ especially, where student-facing generative AI is either commercially
unproven or politically restricted.

**Wiring:** [satvik314/educhain](https://github.com/satvik314/educhain) (**MIT**) for lesson plans,
quizzes and question banks → [openedx/edx-ora2](https://github.com/openedx/edx-ora2)
(**AGPL-3.0**, run as the platform's own service) for rubric-based open-response assessment with
the human grade-of-record → [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) (**MIT**) so the
prompt pipeline has a metric attached instead of being hand-tuned →
[academico-sis/academico](https://github.com/academico-sis/academico) (**MIT**, Spanish built in) or
[openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) (**LGPL-3.0**, default ref
🔴 `19.0`) where the administrative record has to move too.

**Why it sells:** HolonIQ's 2026 LATAM EdTech 100 finds regional AI concentrated in **teacher-facing
instructional tools rather than consumer tutoring**; Brazil's PL 2.338/2023 reportedly targets
**student selection**; DC bans AI in grading, discipline, IEP and teacher evaluation; ANZ shows the
highest ban support in the Ipsos 2026 data. **Teacher-facing-only must be an architectural switch,
not a retrofit.**

---

## Pattern G — Provenance and labelling in the generation path (APAC, overdue)

**For:** anything shipped into **India** (amended IT Rules: prominent labels **and provenance
markers** on AI-generated content from **20 Feb 2026**) or **China** (AI-content labelling measures
applicable from **1 Sep 2025**; 988 services filed by 30 Jun 2026).

**Wiring:** label and sign **at generation**, not at display — every artefact an education agent
emits (generated question, feedback text, summary, image) carries a label and a provenance record
from the moment it is created; the LMS stores the record alongside the artefact (Moodle web services
/ MCP, Canvas API) so an audit can reconstruct what was machine-made months later; the student-facing
surface renders the label rather than deriving it.

**Why it is a build, not a memo:** if labelling happens in the UI, every export, API call and
copy-paste strips it. The requirement is on the content, so the marker belongs in the content
record. Most tutoring products shipped into IN/CN today do not do this and are already out of time.

---

## Pattern H — 🆕 `p384` Prerequisite-aware tutoring, grounded on a curriculum graph you must **not** fork

**For:** the adaptive-learning engagement everyone pitches and nobody can substantiate — "the tutor
knows what the learner is missing". The missing ingredient was never the model; it was a
machine-readable map of what must be mastered **before** the next topic. One now exists.

🔴 **Read this first.** [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)
is licensed **ODbL** (`main/LICENSE`, 25,289 B), a **share-alike database licence**, and it has
**no code grant**. The whole pattern is built around keeping it on the right side of §4.4:

| what you do | ODbL clause | obligation |
|---|---|---|
| Tutor **output** grounded in the graph — next-topic choice, lesson plan, explanation, diagnosis | **§4.3** *Produced Work* | 🟢 **Attribution notice only.** Nothing to release. ODbL supplies the wording: *"Contains information from DATABASE NAME, which is made available here under the Open Database License (ODbL)."* |
| Shipping the graph **extended or merged** — client topics added, standards remapped, graph re-cut | **§4.4** *Derivative Database* | 🔴 **Share-alike.** Must be publicly used only under ODbL / a later ODbL / a compatible licence. §4.4(b): extracting *"the whole or a Substantial part of the Contents into a new database"* **is** a Derivative Database. |

🟢 **So the architectural rule is one sentence: join, never merge.** The client's curriculum data
stays in the client's own store; the taxonomy stays a read-only input resolved at query time. Break
that rule and the client's curriculum map becomes an ODbL obligation.

**Wiring:**
1. **Load the graph read-only, in its own store.** `data/topics.json` (1,930 micro-topics, each with
   a plain-language description, mastery **evidence** criteria, a type — conceptual / procedural /
   representational / language / meta — subject, domain and an approximate age range) and
   `data/dependencies.json` (4,102 edges, `topicId` → `prerequisiteId`, each tagged `hard`/`soft`
   with a one-line reason). 🔵 Keep it in a **separate schema or database** from anything client-
   specific, and never write client rows into it — that separation *is* the §4.4 firewall, and it
   should be visible in the deployment diagram so counsel can see it.
2. **Map the client's own curriculum to it by reference, not by insertion.** A join table
   `client_objective_id → topicId` in the **client's** store. The taxonomy's standards alignments
   (**NGSS, Common Core, UK National Curriculum**, Australian curriculum — Mathematics 442
   alignments across 325 topics, English 630/267, Science 245/131, HASS 210/124) usually give you
   the hook. 🟡 Unmapped client objectives are a **finding to report**, not a gap to paper over.
3. **Diagnose with the graph, not with the model's intuition.** Walk the DAG backwards from the
   failed topic over `hard` edges to find unmet prerequisites. This is a **graph traversal, not a
   generation** — deterministic, inspectable, and the reason the pattern can survive an audit that
   a pure-LLM "diagnosis" cannot. Treat `soft` edges as ranking hints only.
4. **Attach the tutor.** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (**Apache-2.0**) for
   persistent learner memory plus RAG over the learner's materials, with the traversal result from
   step 3 injected as the lesson objective. Teacher-facing variant: feed the same unmet-prerequisite
   list to [satvik314/educhain](https://github.com/satvik314/educhain) (**MIT**) to draft the
   remediation worksheet — which is the side of the market that is actually growing (Trend 5).
5. **Schedule the retention.** [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki)
   (**MIT**) over the mastered topics. The graph says *what* to review next; FSRS says *when*, with
   published parameters. 🟢 Together they make "personalisation" two measurable quantities instead
   of a claim.
6. **Deliver it through the client's existing LMS**, per **Pattern A** — `webservice_mcp` for
   Moodle, [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (**MIT**) for Canvas. For
   K-12 student records, [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) (**GPL-2.0**,
   ref `master`) over its API — never linked.
7. **Prove it on the prerequisite claim specifically.**
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (**MIT**) with
   [GSM8K](https://github.com/openai/grade-school-math) (**MIT**) for the multi-step maths chain.
   🟢 The honest measurement here is not a headline score: it is **whether remediating the
   prerequisite the graph identified improves the dependent topic**. That is an A/B the client has
   never been offered, and it is the whole value of the pattern.
8. **Ship the attribution notice.** §4.3 costs one line in the product's about page and the
   documentation. Put it in at step one; retrofitting a notice after a client review is avoidable
   embarrassment.

🟡 **Scope the research claim honestly.** The taxonomy's teaching-research payload
(`data/teaching-research.json`, ~24 MB) covers **1,049** topics — Science and Mathematics — and the
maintainers state that **881 topics have no research in this release**. "Research-backed guidance"
is true for roughly half the graph. Check which half a client's subject mix lands in **before** the
claim reaches a deck.

🔵 **Coverage note:** `v1` is primary/elementary and strongest on the Australian and US/UK
standards. Secondary and vocational curricula are not covered — for those, this pattern is the
*shape* to build, with the client's own map in place of the taxonomy.

**Licence posture:** client-owned code is MIT/Apache throughout. Two non-permissive components, both
held at arm's length: the **taxonomy** (ODbL, read-only input, joined never merged — §4.3 notice
only) and the **LMS/SIS** (GPL, reached over a published protocol). **Deliverable stays closed.**

---

## Pattern M — 🆕 `p385` The agent-native classroom (when the client has **no** LMS to bolt onto)

**Pattern A inverts the usual build: an agent over the client's existing LMS. Pattern M is for the
engagement where there is no LMS worth integrating** — corporate L&D, a bootcamp, a professional body,
a ministry pilot — and the deliverable is the learning loop itself, not a Moodle plugin.

**The shape.** The classroom is an **MCP server**; the agent is bring-your-own and replaceable. That
inversion is what makes it worth a pattern: the client is not buying a model, so a model swap (or a
provider outage, or a procurement decision two years out) does not invalidate the asset.

| layer | component | licence | why this one |
|---|---|---|---|
| Classroom / state | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | 🔴 AGPL-3.0 (`main`) · 🟢 MIT at `v0.1.0` | ~50 MCP tools over courses, lessons, graded exercises and a persistent learner memory. Read **Pattern L step 10 before you pick a ref** — this decision is the whole procurement question |
| Retention scheduling | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 MIT | learn-shell schedules flashcards with FSRS already; use the upstream parameters so retention is a published model, not a vendor claim |
| Course material ingest | [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | 🟢 Apache-2.0 | the client's PDFs, DOCX and slide decks are the corpus |
| Grounding | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 🟢 Apache-2.0 | document-aware retrieval over that corpus |
| Measurement | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 MIT | the before/after on the client's own subject mix, which `intel/trends.md` Trend 2 makes a procurement precondition |
| Gateway / audit | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | per-user quota and an audit log, which is what gets it past a DPO |

**Wiring.** The agent reaches learn-shell over MCP (JSON-RPC), exactly the boundary Pattern A uses to
stay clear of Moodle's GPL — so the agent code and the prompt/curriculum assets stay the client's.
`unstructured` → `ragflow` builds the grounding index; the agent writes lessons, exercises and
flashcards **into learn-shell** so the evidence of teaching outlives the context window; FSRS decides
what comes back and when; `lm-evaluation-harness` runs the before/after.

🔴 **Three things to say out loud in the pitch, because they are real:**
1. **AGPL reaches hosted use.** If you deploy `main` for the client as a service, the AGPL obligations
   attach to the deployment. The MIT `v0.1.0` tag avoids that and costs you every fix since
   2026-08-16. There is no third option, and this is the decision, not a detail.
2. **v1 is single-machine and unauthenticated by the maintainer's own description.** It is a pilot
   substrate. Multi-tenant auth, isolation and backup are *your* scope — budget them, do not discover them.
3. **It is one maintainer's project.** Weigh that against what it replaces: the alternative is building
   course/lesson/exercise/memory state from scratch, which is the part of this pattern nobody costs correctly.

🔵 **When NOT to use this.** If the client already runs Moodle, Canvas or Open edX, **Pattern A is
strictly better** — the learner records, rostering and gradebook already exist and integration beats
migration. Pattern M is for a greenfield loop, and its honest competitor is not an LMS but a spreadsheet.

## Pattern N — 🆕 `p386` Harden a student-side LMS MCP server into one an institution can deploy

**When to use it.** The client runs **Blackboard, D2L/Brightspace, Canvas or Moodle** and wants an
agent over it. As of `p386` there is a granted community MCP server for **every** one of those
platforms (see [`agents/top.md`](../agents/top.md#the-blackboard-and-d2l-supply-measured)) — so this
is never a greenfield build. 🔴 But **11 of the 12 granted Blackboard/D2L servers authenticate as the
signed-in student**: they ride the user's own browser SSO session, hold whatever rights that user
holds, and have no audit trail. **Licence-clean and still undeliverable.** This pattern is the gap
between the two.

**The parts.**

| role | pick | licence | why this one |
|---|---|---|---|
| Blackboard, institution-grade start | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | 🟢 MIT | The only server on these shelves that targets the **official Blackboard Learn REST API** and claims OAuth2, a role gate, FERPA handling, rate limiting, PII scrub and a JSON audit log. 🟡 Self-claims — **verify by execution before you quote them** |
| D2L start | [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | 🟢 MIT | Multi-strategy auth (TOTP/OAuth/browser), retry + circuit-breaker + cache, **opt-in** writes. The nearest thing to a hardening base on D2L |
| Canvas start | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | 🟢 MIT | The clean default; [mdweaver](https://github.com/mdweaver/canvas-mcp) fork adds office hours and syllabus write |
| Moodle start | [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | 🟡 GPL-3.0-or-later, header-granted | First-party route: it is in **Moodle's own plugin directory**, and the agent reaches it over JSON-RPC so GPL never reaches the agent — **Pattern A**'s boundary |
| Identity / gateway | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | SSO, per-user quota and the audit log that gets a deployment past a DPO |
| Jurisdiction gate | [`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv) | — | A granted licence does not make **grade write-back** lawful where you are deploying it |

**The work, in order — this is the whole deliverable.**

1. **Replace the session with a service identity.** Swap browser-session auth for the platform's
   own OAuth2 / API-key flow against a **service account scoped to the courses in scope**. If the
   chosen server cannot do this (most cannot), this step is a fork, and it is the reason the
   engagement exists.
2. **Scope by role, server-side.** Student / instructor / admin tool sets, enforced in the server,
   never in the prompt. A model that *can* call `update_grade` and is *asked not to* is not a
   control.
3. **Split read from write, and default write off.** Ship read-only first; put every mutation behind
   an explicit per-deployment flag. `JhostinAleck/brightspace-mcp`'s opt-in-writes design is the
   shape to copy.
4. **Gate grade write-back on the jurisdiction, before any code.** Several jurisdictions in the
   policy matrix gate or prohibit automated grading outright — Oklahoma and Maryland bar AI from
   high-stakes student decisions, the EU AI Act puts assessment in Annex III high-risk, Vietnam
   names automated assessment explicitly, and Illinois SB 2909 reaches *teacher* evaluation. 🔴 This
   gate decides the product's tool list, so run it in week one, not at security review.
5. **Add an audit trail that answers a DPO's actual question**: who (service identity + end user),
   which tool, which course, which record, when, and what the platform returned. Structured JSON to
   the client's existing log sink.
6. **Pin the contract, not the login page.** Pin the vendor API version and put contract tests
   around the tools you use; a student-side server breaks silently when the vendor restyles SSO.
7. **Carry the attribution the payload actually requires** — per **Pattern L step 11**. If you
   started from a fork-family server, the NOTICE file may owe **two** credits.
8. **Prove it before handover.** Execute the maintainer's claims rather than quoting them: run the
   role gate against an under-privileged token, confirm the audit record exists for every mutation,
   and confirm the PII scrub on a real transcript.

🟢 **Why this sells.** It is small, bounded, and the client can show the output to their
data-protection officer — and it is available on every major LMS today, because the licences are
already clear. 🔴 **Say the honest part too:** on D2L all six granted servers are student-side, so
step 1 there is a genuine build and should be costed as one, not as a configuration.

## Pattern O — 🆕 `p387` The LATAM engagement, built on what the region already shipped

**For:** a Brazilian or Spanish-speaking LATAM client — ministry, municipality, university or
school network — where the deliverable has to be in the local language, aligned to the *national*
curriculum, and deployable by an institution rather than demoed to one.

**The premise this pattern corrects:** the LATAM supply is not empty. Every component below is a
real address with a grant read first-hand on 2026-10-22.

**Wiring, Brazil (the fully-specified case):**

1. **Start from the national curriculum, not from a prompt.**
   [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores)
   (**MIT**, `main`) already anchors generation to **BNCC** skill codes and **discards an invented
   code before the teacher sees it**. Keep that gate and extend it: the gate *is* the trust story,
   and it is the same mechanism `Pattern H` specifies against a curriculum graph.
2. **Deliver through the LMS the client runs, never a new portal.** On **Moodle**, the
   `webservice_mcp` plugin per **Pattern A**; on **Open edX**, start from
   [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) (**MIT**, `main`), which is already an
   XBlock/plugin with a teacher statistics panel, TTS and cross-session context.
   🔴 **Licence boundary, non-negotiable:** TutorIA's MIT grant covers *the plugin*. Open edX is
   **AGPL-3.0** and hosting it is hosting AGPL software. Keep the agent a **separate service** the
   plugin calls over HTTP, keep the plugin thin, and the client's AGPL obligations stay exactly
   where they were before you arrived.
3. **Integrate the student-record system over its API.**
   [portabilis/i-educar](https://github.com/portabilis/i-educar) (**GPL-2.0-or-later**, real default
   ref **`2.12`**) is what a Brazilian municipality is running. Read rosters and write results
   through its API; **do not fork it** — the fork pulls GPL into the deliverable and buys nothing.
   (Its sibling `i-diario` is AGPL-3.0; check per repository, not per organisation.)
4. **Make it multi-tenant before anyone calls it a pilot.** A school network is many tenants. On
   Moodle, [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager)
   (**GPL-3.0-or-later**, in `version.php`) supplies exactly this — per-role provider routing, rate
   limits, per-tenant enable/disable, usage monitoring — and it reaches the agent over its own API,
   so the copyleft stays on the Moodle side. On Open edX, build the tenant boundary per
   **Pattern N** steps 1–5.
5. **Run it where connectivity is the constraint**, which is the actual deployment profile for
   TutorIA's own users (rural Risaralda) and for most of the nine Google.org rollout countries:
   [Kolibri](https://github.com/learningequality/kolibri) (**MIT**, default ref `develop`) per
   **Pattern D**, with a local open-weight model behind the AI manager's **Ollama** tool rather than
   a metered API.
6. **Schedule retention, in the local language.**
   [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) (**MIT**) for the scheduler; the
   content language is a data property, not a code property, so this layer ports unchanged.
7. **Measure in the language of instruction, and publish the baseline.**
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (**MIT**) with
   Portuguese/Spanish task sets built from the client's own past assessments. 🔴 Do **not** ship an
   English benchmark number as evidence for a Portuguese deployment.
8. **Say out loud what you are adding.** The agents exist and are MIT; **tenancy, support,
   governance and curriculum QA are the deliverable.** That is a defensible studio pitch and an
   honest one — and it is cheaper for the client than the rebuild a "no LATAM supply" story implies.

**Spanish-speaking variant:** swap step 1's BNCC grounding for the client's national curriculum
standard, keep TutorIA (Spanish-first) at step 2, and use
[academico-sis/academico](https://github.com/academico-sis/academico) (**MIT**, Spanish built in) or
[Chamilo](https://github.com/chamilo/chamilo-lms) (GPL-3.0) where no SIS/LMS is in place.

🟡 **Two addresses this pattern deliberately does not use, and why.**
[Daniel-ux1026/Tutor-Inteligente](https://github.com/Daniel-ux1026/Tutor-Inteligente) (Peru) is the
offline-first PWA tutor with explainable difficulty selection that step 5 would otherwise want — it
has **no grant at any of eight probed paths**, so it cannot enter a deliverable, and asking its
author to add a licence is the cheapest possible contribution to the region's supply.
[henriquebotelhogomes/educacao](https://github.com/henriquebotelhogomes/educacao) (Brazil, RAG
tutor, default ref `master`) is ungranted for the same reason.

---

## Pattern P — 🆕 `p388` The parent and guardian surface (and the FERPA line that splits it in two)

**For:** a K-12 district, school group or education provider that is being asked — by statute, by
families, or by its own board — to make a student's progress legible to parents, and an engagement
that wants a real deliverable rather than another policy PDF.

🔴 **Read this first: this is two different products, and conflating them is how the engagement
fails.** The code is the same; the obligations are not.

| | **P-1 · parent-side** | **P-2 · district-side** |
|---|---|---|
| Who holds the credential | the **parent**, for their own child | the **institution** |
| What a read is | a parent exercising their own access | a **FERPA-governed disclosure of an education record** |
| Tenancy | none needed — single user, single family | **full multi-tenant**, per-district, per-role |
| Who buys | a provider bundling it, or nobody (it is a tool, not a sale) | the district, through procurement |
| Build cost | days | the real engagement |

**Components (all verified first-hand 2026-10-22 — [`verified-repos`](../evidence/verified-repos.2026-10-22-p388.tsv)):**

- **Infinite Campus (SIS):** [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp)
  — `main` · `971d58f`, 🟢 **MIT** (1,067 B), **47 npm releases → 2026-10-19**. 20 tools over **Campus
  Parent**: schedule, assignments (`missingOnly`), grades plus a 14-day recent window, **attendance
  events with codes and comments**, behavior, food service, documents, standardized **assessment
  scores**, fees, and messaging from three distinct sources. Linked districts auto-discovered via
  **CUPS SSO**; `FeatureDisabled`-aware, so a district with a module switched off degrades instead of
  erroring — which is what makes it deployable across a group of districts rather than one.
- **Canvas (LMS):** [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp)
  — `main` · `428b78b`, 🟢 **MIT** (1,067 B), **43 releases → 2026-10-16**. 18 `canvas_*` tools held
  to the **read-only observer scope** (`canvas_list_observees` is the hinge), plus student
  self-access. Four auth modes in priority order. 🟢 Copy its download hardening rather than
  re-inventing it: host-pinned to the Canvas origin, confined to a download directory, never writes
  through a symlink, new files `0600`.

### Wiring P-1 (parent-side) — days, not weeks

1. Parent installs the MCP server locally against **their own** portal credential (token, OAuth, or
   session). Nothing is hosted; no institutional agreement is needed because no institutional
   credential is used.
2. Keep it **read-only**. Both servers are already scoped that way; do not add write tools. A parent
   agent that can submit work on a child's behalf is an academic-integrity incident waiting to be
   filed.
3. Add a **digest** rather than a chat surface: *"what changed this week, what is missing, what is
   due."* 🔵 The persona's actual job is **noticing**, not conversing — the portal already answers
   questions, badly, and nobody logs in.

### Wiring P-2 (district-side) — the real engagement

1. 🔴 **Do not host the parent-side tool for the district.** The moment the credential is
   institutional, every read is a FERPA disclosure. Build the institutional path deliberately:
2. **Put the district's own identity in front of it.** Parent identity comes from the district IdP,
   and **the parent↔student relationship is authoritative from the SIS** — never from a claim the
   agent accepts. `ic_list_students` / `canvas_list_observees` define the blast radius of the whole
   system, so that relationship check is the security boundary, not a feature.
3. **Borrow the tenancy layer that already exists.** This is the same problem `p386` identified for
   student-side LMS servers, and `Pattern A`'s answer applies unchanged: per-tenant configuration,
   per-role rate limits and usage monitoring — on Moodle,
   [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager) is the
   worked example to copy the *shape* of.
4. **Log every read as a disclosure, not as a request.** Who asked, for which student, which fields,
   under which relationship, at what time. 🔵 This log is the deliverable a district's counsel signs
   off on, and it is cheap to build on day one and near-impossible to retrofit.
5. **Keep the model away from the record where you can.** Fetch and render deterministically;
   use the model for **summary and prioritisation over data already authorised**, not as the thing
   that decides what to fetch. Smaller surface, smaller disclosure, cheaper review.
6. **Ship the translation layer — it is the actual product.** Gradebook rows are not an answer to
   *"is my kid okay?"* Convert to plain language, in the family's language, at a reading level the
   district specifies, with **no inference about the child beyond what the record states**. A tool
   that volunteers *"your child seems disengaged"* has invented an education record.

**Guardrails:**
- 🔴 **No predictions, no risk scores, no labels.** A parent-facing risk score about a student is
  the high-stakes automated decision Oklahoma and Maryland's frameworks are written to restrain, and
  under the EU AI Act Annex III it is squarely high-risk. Report the record; do not score the child.
- 🔴 **Attendance, behavior, food-service and fee data are the sensitive tail.** `infinitecampus-mcp`
  exposes all four. Free-lunch status and behavior records are the fields a district will refuse last
  and worry about most — scope them out explicitly unless the district asks for them in writing.
- 🟡 **Both servers authenticate as a person.** Treat credential custody as the top risk in the
  design review; a stored parent credential in a studio-hosted service is the worst of both worlds.
- 🔵 **Multiple children, multiple districts.** `ic_list_districts` + CUPS SSO exist because families
  span districts. Test the two-children-two-districts case before a demo; it is the common case and
  the one that breaks naive implementations.

**Why this pattern is worth having at all:** it is the only education surface this base has found
with **granted, maintained components and no incumbent vendor** — the parent portal is a feature of
the SIS, not a market. And **family transparency is already in the statutes** (Oklahoma SB 1734
names it; Maryland's Chapter 634 is built on guidance districts hand down), so the buyer has an
obligation and no product. 🔵 See `Trend 10` in [`intel/trends.md`](../intel/trends.md).

---

## Pattern Q — 🆕 `p389` The generated classroom, governed (and what it supersedes in `Pattern M`)

**For:** a client with **no usable LMS** — a corporate academy, a ministry training programme, a
vocational provider, a new institution — who needs **teachable lessons in weeks, not a platform in
quarters**. Also the fastest credible answer to the EMEA teacher-training demand recorded in
[`intel/market.md`](../intel/market.md): the UAE has **22,000 teachers and education professionals**
to train on a curriculum that became compulsory by Cabinet decision.

**The base:** [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — 🟢 **MIT** (read from the
payload at `main` @ `269fde2d991f`; `package.json` agrees), Tsinghua University, **committed
2026-10-22**, ~41.3k ★, **JCST 2026** paper, grown out of the internal **MAIC** system and validated
on **700+ students**. 🔴 **Pin `v1.2.1` (2026-10-18), not head.** Head is `v1.3.0-rc.1`, and the
project states breaking upgrade conditions with **no rollback below that release** — a pilot does not
want to be the first to find that out.

### Wiring

1. **Stand up the authoring server.** Node ≥ 22.19, pnpm ≥ 10, **PostgreSQL 16**, a long-running
   server (🔴 **not Vercel** — Vercel deployments are capped at the 1.1.x line, so "we'll host it
   serverless" is a downgrade). Generation is **server-first** from v1.2.0: it survives closed tabs and
   restarts, which is what makes it usable by teachers rather than by engineers.
2. **Write the governance file first, before any content.** `openmaic.yml` declares **providers** and
   assigns every AI use — a named **slot** (`llm`, `course.outline`, slide content, TTS, web search,
   `video`) — to one of them, with keys referenced as `${VAR}` from `.env.local`. 🟢 **Three settings
   are the compliance deliverable, not configuration:** pin each slot to the provider under the
   client's own contract; set the server to **forbid user-supplied keys**, so no teacher can route
   student work through an unvetted account; and set unused capabilities to `null` rather than leaving
   them available. 🔵 **This file is the artefact that answers a district's or ministry's AI policy
   question** — *which model saw student input, under whose contract* — in one reviewable, diffable
   page. Almost nothing else in this base can answer it at all.
3. **Ground the content in the client's curriculum, not in the model.** Feed the jurisdiction's own
   material through the **knowledge base** (v1.3.0 line) or as per-course uploads — parsed once and
   reused — and where a standards graph exists, drive the lesson plan from it rather than from a
   prompt: [`os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) (🔴 **ODbL-1.0 — a database
   licence; reach it over a service, do not fork it into the deliverable**, per `Pattern H`), or
   [`bc-curriculum-mcp-server`](https://github.com/pdg6/bc-curriculum-mcp-server) (**MIT**) for a
   North American engagement — 🟡 whose crawl is **209 days** old, so budget the re-crawl its MIT grant
   permits.
4. **Keep the record of record outside it.** 🔴 OpenMAIC has **no enrolment, no gradebook of record,
   no transcripts and no stated LTI story**. Pair it with the administration base the client already
   runs or should: [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) (GPL-2.0, over its API),
   [academico](https://github.com/academico-sis/academico) (**MIT**) at SME scale,
   [i-educar](https://github.com/portabilis/i-educar) (ref `2.12`) for Brazilian municipal work, or
   [OpenEduCat](https://github.com/openeducat/openeducat_erp) (LGPL-3.0) where an ERP is wanted.
   **Completion and scores flow out of OpenMAIC into that system; identity and enrolment flow in.**
5. **Add the mastery model it does not have.** Quiz results are events, not a mastery estimate. Fit
   [`pyBKT`](https://github.com/CAHLR/pyBKT) (**MIT**, 1 d) on the quiz log per skill, as in the
   revised `Pattern B`, and use it to choose the next lesson. 🟢 This is also what keeps the
   high-risk-assessment line on the right side: the progression decision becomes **a published model
   plus a human review step**, not a generation.
6. **Deliver to the edge as files.** Export each finished classroom as **one offline HTML file** (or
   PPTX). See `Pattern D` — authoring stays central, delivery needs only a browser.
7. **Run the models where the data has to stay.** **Lemonade** for local inference and **FunASR** for
   local ASR are supported paths, not forks — so a deployment that may not send audio or text
   off-premises is a configuration change.

### Why this supersedes `Pattern M` for institutional delivery

`Pattern M` is built on [learn-shell](https://github.com/sf-shenfeng/learn-shell), whose v1 is
explicitly **single-machine and unauthenticated**, and whose grant is **AGPL-3.0 at `main`** (MIT only
at tag `v0.1.0`). That is a fine shape for an individual learner and an impossible one for an
institution. OpenMAIC is **MIT at head**, server-first, multi-user, with central model governance and
a published security practice — five releases since September 2026 carrying SSRF, DNS-rebinding,
token-expiry and provider-redirect fixes under **GHSAs**. 🔵 **Keep `Pattern M` for the
bring-your-own-agent, one-learner case; use `Pattern Q` whenever a client is the buyer.**

### Guardrails

- 🔴 **Auto-graded quizzes are the regulated surface.** Assessment is **Annex III high-risk** in the
  EU and named explicitly in **Vietnam's Decision 33/2026/QD-TTg**. The trigger in both is a decision
  taken on the system's output **without meaningful human review**, so ship the human review step for
  anything consequential and keep its audit trail. A practice score is not consequential; a module
  pass that gates progression is.
- 🔴 **Simulated classmates must be labelled.** An AI teacher with a voice and AI peers in a classroom
  is exactly the surface **EU AI Act Art. 50** transparency and China's labelling rules address, and
  `Pattern G` already covers the mechanics. Label in the UI, not in the terms of service.
- 🟡 **Generated content is a draft until a teacher signs it.** The 2026 procurement trend is evidence
  of instructional benefit; a lesson nobody reviewed cannot be put in front of a class at a client's
  reputational risk. Make teacher review a workflow state, and bill it — it is the part of the
  engagement that is actually about teaching.
- 🟡 **Language and regional fit:** interface is **EN + zh-CN** and the provider catalogue is built for
  a market that includes DeepSeek and Kimi. For a Gulf or LATAM engagement, **localisation of the
  teaching surface is a line item**, and there is no Arabic-first alternative in the open-source supply
  (see `intel/market.md`, EMEA).

---

## Pattern V — 🆕 `p390` The spoken tutor, and the two things that make or break it

**For:** learners who cannot or will not type their way through a lesson — early grades, low typing
fluency, shared-device households, visually impaired learners, and language learning where
*pronunciation is the skill being assessed*. This is also the pattern that reaches the LATAM and
APAC households `Trend 10` describes, where the phone is the only device.

**Why it is a separate pattern:** a voice tutor is not a text tutor with TTS bolted on. Two
properties decide whether a child keeps talking to it, and neither is in the LLM:

1. **Turn-taking.** The tutor must know when the learner has stopped speaking, tolerate a
   four-second pause while a 9-year-old thinks, and **stop talking the moment it is interrupted**.
2. **Latency budget.** Past roughly a second of silence the learner starts talking over it, and the
   session degrades into collision recovery.

**Wiring:**

1. **Do not write the voice loop.** [`livekit/agents`](https://github.com/livekit/agents)
   (🟢 **Apache-2.0**, dated 2026-10-22) is the substrate: full-duplex WebRTC transport, pluggable
   STT/LLM/TTS, **turn detection, interruption and barge-in handling**. All three legs are
   provider-swappable, which is what makes step 4 possible.
2. **Start from the working reference.** [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent)
   ("Manu", 🟢 **MIT**, dated 2026-10-07) is a pt-BR maths tutor on exactly that substrate, scaling
   its explanation from 1st grade to university. 🔴 Its README says **"in development" with no public
   deployment** — take the pipeline and the prompt-scaffolding, not a production claim.
3. 🔴 **Put a symbolic checker behind any arithmetic.** Manu's correctness layer is the LLM itself.
   For a maths tutor that is the one unacceptable gap: route every numeric or algebraic claim through
   SymPy (or the client's own CAS) and have the agent *read back* the verified result. A spoken wrong
   answer is harder for a learner to catch than a written one — there is no transcript to re-read.
4. **Localise the ASR, not just the prompt.** Accent and dialect coverage is where regional voice
   tutors fail. [`mozilla/common-voice`](https://github.com/mozilla/common-voice) ships **CC0-1.0**
   corpora across ~130 language variants (pt-BR, es-419 variants, Hindi, Bengali, Kiswahili) — use
   them to *evaluate* candidate ASR models on the client's actual learner population before picking
   one, and to fine-tune where the gap is real. 🟢 CC0 means no attribution and no share-alike, so
   this is safe in a commercial deliverable. 🟡 MPL-2.0 covers the **platform code**, not the corpora.
5. **Keep the mastery model outside the voice path.** Voice is an I/O channel, not a pedagogy.
   [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) (🟢 MIT, dated 2026-10-22) holds the Bayesian
   Knowledge Tracing state so "what comes next" survives a dropped call and stays inspectable — which
   is also what makes the decision auditable under step 6.
6. 🔴 **Voice raises the compliance stakes, so settle three things before the pilot.**
   - **Biometrics.** A voice recording is biometric data under GDPR Art. 9 and most LATAM regimes
     (Brazil's LGPD included). Default to **transcribe-and-discard**, keep no audio unless the client
     has a lawful basis and a retention policy, and write that down.
   - **Emotion inference is prohibited in EU education** (AI Act, in force since 2 Feb 2025) — and
     voice is the modality vendors are most tempted to infer affect from. Do not ship it in EMEA,
     and strip it from any upstream SDK feature you enable.
   - **Disclosure.** AI Act Art. 50 applies from **2 Aug 2026**: a synthetic voice must be
     disclosed as synthetic. Say it in the first turn, in the learner's language, every session.
7. **Measure it as a tutor, not as a demo.** Score the *transcripts* with
   [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness)
   (🟢 MIT) on the client's own item bank, and track interruption rate and mean response latency
   alongside learning gain — a tutor that is pedagogically right and 1.5 s slow will still be
   abandoned.

**Licence position:** Apache-2.0 substrate + MIT reference + CC0 data + MIT mastery model — the whole
chain is permissive, so this pattern can ship as a closed client deliverable with attribution only.

**What this pattern does not solve:** there is **no granted, maintained open-source voice tutor for
an African or South Asian language** on these shelves. See `Gap 390-A`.

## Pattern W — 🆕 `p391` Qualify the district *before* the pitch (North America)

**For:** a North America K-12 engagement, at the stage before anyone has written code — choosing
which districts to approach, and pricing a pilot against a budget that actually exists. Every other
pattern here answers *what to build*; this one answers *for whom, and with whose money*.

**Why it is a pattern and not a sales note:** US school AI spending is not discretionary in the way
enterprise AI spending is. It comes from identifiable federal, state and local lines, and the
largest flexible federal line — **Title I** — is allocated on **Census child-poverty counts**, not
on enrolment. A pilot proposed without that number is priced blind, and a district with a high
poverty count and a low per-pupil spend is a different conversation from the inverse.

**Wiring:**

1. **Pull the universe.** [`pipeworx-io/mcp-education-data`](https://github.com/pipeworx-io/mcp-education-data)
   (🟢 **MIT**, HEAD 2026-10-21) — `education_find_districts` for a state returns every local
   education agency with its **LEA id**, school count, enrolment and teacher counts. The `leaid` is
   the join key for everything below.
2. **Add the budget.** `education_district_finance` on that `leaid` returns revenue split
   **federal / state / local** and expenditure by function, with **per-pupil spending computed**.
   🔴 **The survey lags the directory by 1–2 years** — quote it as "FY-whatever per-pupil", never as
   current-year, or the first CFO in the room ends the meeting.
3. **Add the federal lever.** `education_child_poverty` returns Census **SAIPE** counts and rates of
   children 5–17 in poverty by district — the figures Title I formulas run on. High poverty rate plus
   low per-pupil spend identifies districts with *federal* money and *no* incumbent vendor: the
   cheapest pilot to land and the hardest to displace later.
4. **Add the surface.** `education_find_schools` carries **charter/magnet status, grade range and
   free/reduced-price lunch counts** per school, so the pilot can be scoped to named schools rather
   than to a district abstraction.
5. **Then pick the build.** Hand the shortlist to whichever pattern fits the client's platform —
   `Pattern F` (teacher-facing, the one the market and the regulator agree on) is the usual answer at
   this budget, `Pattern N` if they run an LMS already.

🔴 **Three things to decide before the first call, not after.** The integration is **unofficial** and
not affiliated with the upstream provider — fine for your own targeting, not something to resell as a
data product. The default path is a **hosted gateway** (`gateway.pipeworx.io`): the underlying data is
public federal data, but the **query pattern is not** — which districts a studio is sizing up is
commercially sensitive, so self-host before running this against a named client list. And a scoped
endpoint lists roughly **30 shared gateway meta-tools** alongside the four that matter, so budget the
context or connect once to the full gateway rather than to several pack endpoints.

🔵 **Regional honesty.** This is a **North America–only** instrument: it is NCES/Census data and has
no EMEA, APAC or LATAM analogue on these shelves. The equivalent question in those regions is still
answered by hand — recorded as `Gap 391-B` rather than left to look like coverage.

## Pattern X — 🆕 `p391` Keep the client's pedagogy as a separate, reviewable artefact

**For:** any tutoring engagement that will be audited, handed over, or argued about — which, under
EU AI Act high-risk obligations and most North American district procurement, is all of them. Also
the pattern for a studio that wants the *teaching* it built to outlive the *runtime* it shipped on.

**Why it is a separate pattern:** in nearly every tutor on these shelves, the pedagogy is diffused
through the application — prompt fragments, conditional branches, UI copy. That makes two things
expensive that clients ask for routinely: *show me the teaching policy* and *change the teaching
policy without a release*. [`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor)
(🟢 **MIT**, HEAD 2026-10-21) is the first row here built the other way round, and it is worth copying
even where the repository itself is not used.

**The split, which is the whole point:**

| | owns | where it lives |
|---|---|---|
| [`universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) (🟢 **MIT**, → 2026-09-24) | **what to teach next**: diagnosis, teaching moves, pacing, when a check is passed, what the next step is | its own repository, versioned independently |
| [`dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (🟢 **MIT**) | **where it is kept**: learner state, the diagnosis map, structured lessons, the UI | the runtime, which contains **no teaching logic at all** |

**Wiring:**

1. **Put the pedagogy in a versioned repository of its own**, as prose and rules rather than code:
   diagnosis strategy, teaching moves, mastery criteria, escalation. This is the artefact a client
   reviews, a subject expert edits without a developer, and an auditor reads **without reading the
   application**. It is also the thing a studio can hand over at the end of an engagement.
2. **Make the runtime record decisions, never make them.** The runtime stores what the teaching layer
   decided and renders it; every pedagogical choice arrives from the policy artefact. Test this by
   grepping the runtime for teaching rules — if `if blocked, explain the prerequisite` lives in the
   application, the separation has already leaked.
3. **Put the assessment behind a pure function.** [`intellectif/learning-kit`](https://github.com/intellectif/learning-kit)
   (🟢 **MIT**, HEAD 2026-10-18) — `@intellectif/lk-core` gives schemas, a **pure scoring engine**,
   **rubric and deferred grading**, attempt plans and redaction, with no runtime dependency beyond
   Zod. Scoring that is a pure function is unit-testable by the client and readable by a regulator;
   **deferred grading keeps a human marker in the loop by construction**, which is what high-risk
   assessment obligations ask for rather than something to retrofit.
4. **Emit evidence, do not hoard it.** `lk-core`'s **xAPI builder** sends statements to the client's
   own LRS — [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) where one is needed — so the learning
   record stays the client's property and the tutor stays replaceable.
5. **Launch it from the LMS over a maintained LTI edge — in the agent's own language.** 🆕 `p392`
   For a **Django** agent, [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
   (🟢 **MIT**, PyPI `django-lti` v0.10.1, HEAD **2026-10-20**): one installed app, one middleware,
   one migration, **no second service**. For a **JupyterHub**,
   [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (🟢 **BSD-3-Clause**).
   For **Node**, [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (🟢 **Apache-2.0**, npm v7.0.7)
   or [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 **MIT**) if the deployment is
   serverless. 🔴 `p391`'s *"the edge is Node or PHP regardless of what the agent is written in"* is
   **withdrawn** — `Gap 391-A` is closed. The constraint that remains is a **licence** one: the
   best-maintained Python implementation, `openedx/xblock-lti-consumer`, is **AGPL-3.0**.

🔴 **What this pattern does not give you.** `dsh-diagnostic-tutor` is **v0.1.1 and early by its own
account**: no PDF or document ingestion, no RAG, no flashcards, no analytics, and **a route never
marks knowledge as mastered**. It also **requires DeepSeek Harness** — it is a harness extension, not
a standalone application, so an engagement that cannot adopt that harness should copy the *structure*
(steps 1–2) onto a tutor it can deploy, not adopt the repository. 🟢 Take the separation; shop for the
runtime.

## Pattern L — Clear a repository for reuse by **subtree**, not by its licence badge

**The one durable result of the `p3xx` apparatus**, kept as a procurement gate rather than a
narrative. Run it before any repo enters a client deliverable.

1. **Resolve the real default ref first.** `git ls-remote --symref https://github.com/<slug> HEAD`.
   **13 of 58 live addresses verified in `p383` are not on `main`** — `master`, `develop`, `dev`,
   `release`, `development`, `release_11`, and OpenEduCat's `19.0`; `p384` adds **openSIS-Classic
   → `master`**. A `main`-assuming read reports "no licence" for every one of them, and that false
   negative looks exactly like a real one.
2. **Probe more than one path — eight, not seven.** In order: `LICENSE`, `LICENSE.md`,
   `LICENSE.txt`, `LICENCE`, `COPYING`, `LICENSE-MIT`, `license`, and 🆕 **`docs/License.txt`**
   (with `doc/LICENSE` as its variant). Verified instances where the grant is *not* at `LICENSE`:
   **Moodle → `COPYING.txt`**, **Frappe LMS → `license.txt`** (lowercase),
   **ai-shifu → `LICENSE.txt`**, **lm-evaluation-harness → `LICENSE.md`**,
   **H5P → `LICENSE.txt`**, and 🆕 **openSIS-Classic → `docs/License.txt`** (17,286 B, stock
   GPL-2.0, *"Version 2, June 1991"*, corroborated by `"version 2 of the License"` headers in
   `index.php` and `Modules.php`). 🔵 `p384` added the eighth path because the seven-path read
   returned "ungranted" for **the most widely deployed open-source SIS in K-12** — a repository with
   a perfectly ordinary grant sitting one directory down.
3. **Check for a split grant.** **[microsoft/autogen](https://github.com/microsoft/autogen)**: root
   `LICENSE` is **CC-BY-4.0** (18,649 B, "Attribution 4.0 International"); the **code** grant is a
   separate file, `LICENSE-CODE` = **MIT**. One file read gives you the wrong answer either way.
   Conversely, confirm a split grant is **absent** before assuming one:
   [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) has **no** code grant —
   `LICENSE-CODE`, `LICENSE.code`, `CODE_LICENSE` and `licenses/LICENSE` all **404** — so its ODbL
   is the only grant on offer, for the tooling as well as the data.
4. **Compare byte length against the stock text.** A licence whose length is off is a licence that
   was edited. **[open-webui/open-webui](https://github.com/open-webui/open-webui)**: `LICENSE` is
   **2,819 B** against stock BSD-3's ~1,500 B — BSD-3 text **plus** a branding restriction and a
   CLA, self-titled "Open WebUI License". Not an OSI-standard grant.
5. **Read the manifest and the source headers before you call anything ungranted.** 🔴 **`p383`'s
   own first draft failed this step and `gate-enumeration` refused it.** Five repositories had no
   licence file at any of the seven paths; only **two** turned out to be ungranted.
   `DMontgomery40/mcp-canvas-lms` and `general-mudkip/d2l-mcp-server` declare
   `"license": "MIT"` in `package.json` (**manifest-only** — reusable, but record the line and ask
   for the file). `onbirdev/moodle-webservice_mcp` carries the full **GPL-3.0-or-later** header in
   `version.php`, as Moodle requires of every plugin — **granted, with no licence file at all.**
   Probe `package.json`, `pyproject.toml`, `composer.json`, the `README`'s licence section and the
   main source file's header before rejecting a repository;
   🆕 `p385` — **but read what that section *says*, not that it *exists*.** Two failure modes, both on
   these shelves: [moarshy/mcp-tutor](https://github.com/moarshy/mcp-tutor) has a `## License` heading whose
   entire body is *"This project is experimental and intended for educational and research purposes"* —
   which grants **nothing**, while satisfying any check that asks "is there a licence section?";
   [h9-tect/AI-Roadmaps](https://github.com/h9-tect/AI-Roadmaps) states *"provided under the
   [MIT License](LICENSE)"* and **that `LICENSE` link 404s**. A prose assertion is weaker evidence than a
   manifest field, which is weaker than the text itself — grade them separately and never as "MIT"; a file-only read would have wrongly
   rejected three of five, including the plugin Moodle's own directory distributes.
6. **Only now treat "no licence" as a hard stop — and it is a hard stop.** Two live, functional,
   actively advertised repositories survive every check above with no grant anywhere:
   `loyaniu/moodle-mcp` (no `license` field in `pyproject.toml` either) and
   `Seechange-edu/act-ai-tutor-backend` (no manifest at all). 🔵 Both were **re-probed at the new
   eighth path in `p384` and remain ungranted.** No grant means no right to redistribute, whatever
   the README invites you to do.
7. **Ask what the grant covers, not just what it is.** A valid, unmodified, correctly-recognised
   licence can still leave the part you are shipping ungranted — stock **ODbL** governs a database's
   *rights*, by its own preamble **not the contents of the database individually**. If you ship
   derivatives of the *contents* on the strength of "licence: ODbL-1.0", you have no grant for the
   part you shipped. Record the answer **per subtree** (`data/`, `docs/`, `scripts/`), and record
   "not stated" as distinct from "not granted".
   🟢 🆕 **This step was written abstractly in `p383`. `p384` gave it its first real instance** —
   `os-taxonomy`, ODbL, no code grant — and the concrete reading is now **Pattern H** below. The
   step was right in advance, which is reason to trust it on the next data artefact: education runs
   on standards, item banks and curriculum maps, so this will not be the last one.
8. **Re-check dead addresses.** Four in common circulation do not resolve: `apereo/opencast`,
   `edx/openassessment`, `openedx/openassessment`, `OpenEduCat/OpenEduCat`. Live replacements in
   [`repos/foundations.md`](../repos/foundations.md).
9. 🆕 **Confirm there is a *tree*, not just a *ref*.** `git ls-remote` on
   [projectfedena/fedena](https://github.com/projectfedena/fedena) returns two heads — and every
   content path at `master` (`README`, `README.md`, `LICENSE`, `Gemfile`, `app`) returns **404**.
   **`ls-remote` proves a ref, not a payload**, so step 1 can pass on a repository that has nothing
   in it to licence. A vendor article lists this slug as an Apache-2.0 SIS; the correct record is
   **"nothing read"** — neither granted nor ungranted. Any address census built on resolution alone
   over-counts the supply.

10. 🆕 **Read the grant at the ref you are shipping — the licence is a property of the *ref*, not of the
    repository.** [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) is **AGPL-3.0** at
    `main` (`LICENSE`, 34,523 B, stock) and **MIT** at tag **`v0.1.0`** (`LICENSE`, 1,081 B,
    *"Copyright (c) 2026 Learn Shell contributors"*). Both were read first-hand in `p385`; the project
    relicensed on **2026-08-16**. 🔵 This base already knew relicensing happens —
    `snflwr-ai/snflwr.ai` went AGPL-3.0 → proprietary (`p241`), `AIHawk` went MIT for releases after a date.
    What `p385` adds is the **direction that favours the buyer**: permissive → copyleft, with the permissive
    grant **still retrievable at a tag**. 🔴 The trap in both directions is a cached audit. "We cleared that
    repo as MIT last quarter" is a statement about a ref that has moved. Record **slug + ref + licence +
    date-read**, never slug + licence — and re-read before each release, not once per engagement.
    🟡 And when you pin a tag to keep a permissive grant, say out loud what it costs: a frozen tree, no
    upstream fixes, and a maintainer who has signalled they do not want that code used on those terms.

11. 🆕 `p386` **Classify a byte-length anomaly before you judge it — "longer than stock" has two
    opposite meanings.** Step 4 says a non-stock length means the text was edited. True, and `p386`
    found the benign half of that read, which a length check alone cannot distinguish from the
    hostile one:

    | repo | bytes | the excess is | what you do |
    |---|---|---|---|
    | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 2,819 (BSD-3 ≈1,500) | 🔴 **added restriction** — branding clause + CLA | walk away, or get written permission |
    | [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | 1,200 (MIT ≈1,065) | 🟢 **added attribution** — inline notice, *"Portions … derived from brightspace-mcp-server, Copyright (c) 2026 Rohan Muppa, used under the MIT License"* | ship it, carry the extra notice |
    | [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP) | 2,181 | 🟢 **two complete MIT grants concatenated** — its own plus `d2l-cli`, © 2026 Aaryan Kapoor | ship it, carry **both** notices |
    | [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 11,906 (Apache-2.0 ≈11,358) | 🟢 **ASF's appended notice text** | ship it, keep `NOTICE` |

    🔵 **So the test is not "is the length stock?" but "does the delta add a condition or a
    credit?"** Added conditions are procurement stops. Added credits are NOTICE-file entries — and
    they are *obligations you inherit silently*: ship `D2L-MCP` and you owe attribution to a project
    you never chose, which no SBOM built from a licence **identifier** will tell you.
    🟡 Record the delta's content, not just the byte count.

12. 🆕 `p386` **Count grants, not addresses — and never let a count of zero reads print as
    "ungranted".** For four passes [`agents/top.md`](../agents/top.md) said *"Blackboard has nine
    servers and not one verified grant; D2L has six and the only one checked is ungranted"*, and
    concluded both platforms needed a permissive server built. `p386` probed all fifteen: **6 MIT on
    Blackboard, 6 MIT on D2L**. 🔴 The grants existed; the reads did not. A harvest column headed
    *"distinct slugs"* answers **how many addresses exist**; `LIVE-GRANTED` / `LIVE-NOGRANT` answers
    **how many were read**. When the second number is zero the honest word is **unread**, and the
    cost of the wrong word here was a false build recommendation on two platforms.
    🔵 Before any shelf states a supply gap, state which census it is quoting.

13. 🆕 `p387` **Date the artefact you are about to ship, in the registry.** A grant tells you whether
    you *may* use it; a publish date tells you whether anyone is still there. Read the package name
    from the manifest at the real default ref, then:
    `curl -s https://registry.npmjs.org/<name>` → `dist-tags.latest`, `time.created`,
    `time.<latest>`, `versions.<latest>.license`, `.repository`; or
    `curl -s https://pypi.org/pypi/<name>/json` → `info.version`, `info.license`,
    `releases[*].upload_time`. 🟢 Three usable outputs: a **second, independently published grant**
    (a manifest-only MIT becomes an MIT published to a registry); a **maintenance date** that
    survives `api.github.com` being 403; and the discovery that an address ships **no artefact at
    all**, which is a different conversation with a client than "it is old". 🔴 `p387` found a
    four-and-a-half-year-stale dependency inside a pattern on this page, a 16-month-stale server
    recommended for its tool count, and an "institution-grade" server with no release.

14. 🆕 `p387` **A manifest's package name is not proof of a publication — match the registry back to
    the slug.** [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server)
    declares the npm name **`class`**, and npm's `class` is an unrelated **2013** package by
    `deadlyicon`. Keyed on the name alone, a recency sweep would have printed *"MIT, published
    2013-08-15"* onto a Google Classroom row. 🟢 **The check:** accept a registry row only when its
    `repository` field — or the links in its description — point back at the same slug; otherwise
    record `NOT PUBLISHED` and say so. The same check collapses fork families for free: four
    Blackboard addresses declare `blackboard-mcp` and **one** publication exists, its `repository`
    naming `felipedias-ie`; `mdweaver/canvas-mcp` carries upstream's scoped name
    `@r-huijts/canvas-mcp`. **Count the artefact, not the slug.**

11. 🆕 `p388` **If the repository is unreadable, read the *artefact*. The manifest is a claim; the
    tarball is the evidence.** `git ls-remote` distinguishes two states a 404 conflates: a
    **credentials prompt means the repository exists and is closed**, not absent. For such a package
    — and **6 of 32 addresses probed in `p388` are in this state while publishing to npm
    normally** — the published tarball is still readable and is **the licence that actually ships**:
    ```
    curl -s https://registry.npmjs.org/<pkg> | jq -r '.versions[.["dist-tags"].latest].dist.tarball'
    curl -s <tarball> | tar -tz | grep -i -E 'license|copying'      # is a grant shipped at all?
    ```
    🔴 **This is how `p388` established that a major publisher's tutoring SDK is ungranted.**
    `@santillana-ai/typescript-tutor-sdk` — **115 published versions** — has **no `license` field in
    `package.json`**, **no licence file anywhere in its 896,006-byte tarball**, and **no `repository`
    field at all**; its sibling scaffolder claims `"license": "MIT"` in the manifest while shipping
    **no licence file either**. Neither the repo (private) nor the badge (absent) could have settled
    it; the artefact did.
    🔵 **Three sub-rules:**
    **(a)** A manifest reading **`"SEE LICENSE IN LICENSE"` that points into an unreadable
    repository is not a grant** — it is a circular reference
    — [ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit) is the worked example, and 🆕 `p390` re-confirmed its repository is **still unreadable**, so the circle is still closed.
    **(b)** Steps 1–10 clear a repository **by subtree**; when there is no readable subtree, *this*
    step is the only one available, and it can only ever yield 🟡 manifest-only or 🔴 ungranted —
    **never a clean clearance**.
    **(c)** 🔴 Check **which** package in a scope carries the grant. Here the MIT claim sits on the
    *scaffolder* and the **dependency a client's code would actually import carries nothing**. Read
    the licence of the package you will `import`, not of the one you will `npx` once.

**Channel note, so this is reproducible:** `curl -sI https://github.com/...` returns **403** through
this sandbox's agent proxy and `api.github.com` returns **403**. `git ls-remote --symref` and
`raw.githubusercontent.com` both work, and together they are a stronger check than a HEAD request —
one proves the address and its real ref, the other reads the grant itself.

🟢 🆕 `p389` **Step 11, and it makes steps 1–10 one command.** A **blobless shallow clone** does the
whole gate in ~1.2 s, from the payload, with no API and no credentials:

```bash
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/&lt;owner&gt;/&lt;repo&gt; r
git -C r symbolic-ref --short HEAD    # the real default ref (step 1)
git -C r ls-tree --name-only HEAD     # is there a LICENSE at all, and where (steps 2-3)
git -C r show HEAD:LICENSE            # the grant text itself (step 4)
git -C r show HEAD:package.json       # the manifest that must agree with it (step 5)
git -C r log -1 --format='%H %cI'     # ← NEW: who still works on this, and when
```

🔵 **Why the last line belongs in a procurement gate and not just in a research note.** The gate has
only ever answered *may we use this*. It now also answers *will we be alone on it* — and the two
produce different estimates. **A permissive grant plus an eight-month-old HEAD is a vendoring
decision with a maintenance line**, which is precisely the call this base made for `pybryt` after
reading a *registry* date; the clone reads it for any repository, published package or not. 🟡 Read
the date against the artefact: a release branch can trail a default ref
([instructure/canvas-lms](https://github.com/instructure/canvas-lms), `master` **175 days** behind its
moving `stable/*` branches), and a finished specification is not decaying. 🔴 And the limit, **re-measured at `p392` and narrower than it was**: the `git` channel itself gives no
stars, forks or releases — but `github.com/{owner}/{repo}` answers **200 via WebFetch** (403 via
curl), so **stars, forks, commit counts and release tags are readable again**, and `api.github.com`
answers **200** while refusing **by scope** rather than outright (`/search/*` is closed by design).
**Discovery** remains web search and package registries; **verification** is first-hand; and
**popularity** is back, per tool. See [`channel-state`](../evidence/channel-state.2026-10-22-p392.tsv).

## Pattern Y — 🆕 `p392` Exam integrity the client can defend, without becoming a high-risk deployer

**For:** a client — a university, a certification body, a bootcamp — who asks for proctoring, and
whose actual requirement is *"we must be able to defend a result if it is challenged"*.

🔴 **Read this first, because it is the whole pattern.** For four passes these shelves said proctoring
had *"no credible permissive open-source option"*. That was wrong (`Gap 391-C`, closed this pass). But
the granted supply covers **deterministic lockdown and event telemetry**, while the **inference**
layer — identity matching, gaze, multi-face, behavioural scoring — is absent, roadmapped, or the
proprietary service an AGPL workflow brokers (`Trend 20`). 🟢 **That asymmetry is a gift, not a
shortfall:** the half you can build permissively is the half that is explainable in an appeal, and the
half you cannot is the half that makes the client a **deployer of an Annex III high-risk system** with
standalone obligations from **2 Dec 2027**.

**Wiring:**
1. **Signals in the browser, permissively.**
   [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) (🟢 **MIT**, 1,069 B,
   manifest agrees, HEAD **2026-09-28**, npm v0.5.1): tab-switch, right-click, DevTools shortcuts,
   clipboard events, camera state, **faces**, audio loudness, and **virtual-camera / loopback /
   screen-share detection**. Face detection is `@vladmandic/face-api` 1.7.15 on TF.js, **in the
   browser**. 🔴 **Two things to change before a pilot:** self-host the model weights (it loads
   face-api **and** its weights from jsDelivr by default — a supply-chain and data-residency defect in
   any EU or public-sector deployment, and the README documents the self-hosted path), and read all
   46 commits — this is **1 ★ and one maintainer**, so vendor it and own it.
   🟡 *Alternative when you need lockdown rather than detection:*
   [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) — 398 commits,
   HEAD **2026-10-13** — blocks copy/paste/cut, right-click, selection and shortcuts and reports eight
   named violation types. 🔴 Its grant is a **CONFLICT** (Apache-2.0 in the payload, `ISC` in
   `package.json` and on npm): both readings are permissive, so it is usable, but get the two files
   reconciled before a client depends on it. 🔴 And its AI features are marked *"(To be Done)"* — do
   not quote them.
2. **Keep the record, not the video.** Both components POST to an endpoint **you** build. Store the
   **event trail** (what happened, when, on which element) and resist storing webcam frames: snapshots
   are off by default in `proctoring.js`, and leaving them off is a defensible default, not a
   limitation. Audio is analysed in memory and discarded — say so in the privacy notice.
3. **Put the decision in a human's hands, in the workflow.** The attempt/review state machine already
   exists: [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) (🔴 **AGPL-3.0**,
   253 releases, `master` HEAD **2026-10-22** — re-read first-hand this pass) if the client runs Open edX — brokered over the platform boundary, not forked — or
   [`intellectif/learning-kit`](https://github.com/intellectif/learning-kit)'s (🟢 **MIT**)
   **deferred grading** when you are building the assessment surface yourself. **No automatic
   flagging decides anything**; a flagged attempt opens a review task.
4. **Launch and report over LTI 1.3, in the agent's own language.**
   [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) (🟢 MIT) for a
   Django service, [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 MIT) for a
   serverless one — so the integrity result lands in the gradebook of record as an **LTI AGS score**
   with a reviewable note attached, rather than in a side system nobody audits.
5. **Write the Art. 50 and Annex III position down before you build.** Students are told, in advance,
   which signals are collected and what a flag does; the review path and the appeal path are named; the
   retention period is set. 🟢 This is cheap here **because** step 1 does no inference — the honest
   disclosure is short.

**Effort:** 4–6 weeks for steps 1–4 on an existing assessment surface; step 5 is a day of writing and
the thing that gets the deployment approved.

🔴 **What this pattern refuses to build, and tell the client why:** automated cheating *verdicts*,
identity verification from a webcam, and gaze or emotion scoring. The permissive supply does not have
them, the obligations land on the client rather than on us, and a flag that cannot be explained in an
appeal is a liability dressed as a feature.

## Pattern Z — 🆕 `p392` Size and price a Brazilian education engagement before the first meeting

**For:** a LATAM pitch — a municipal or state network, a private group — where the honest answer to
*"how big is this?"* has until now been *"we will need to scope it."* `Pattern W` does this for a US
district; this is the Brazilian instrument, and it is the closure of `Gap 391-B` for one country.

**Wiring:**
1. **Install the access layer.** [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil)
   (🟡 **MIT — code only**, 1,072 B; PyPI **`mcp-brasil` v0.14.0**, 18 releases; HEAD **2026-08-18**):
   an MCP server over **70 Brazilian public sources**, 533 tools, **66 of them keyless**, with large
   datasets cached locally and queried through embedded **DuckDB**. No procurement, no API key, no
   vendor.
2. **Query the school census.** `censo_escolar` (INEP) is the per-school base: network, enrolment,
   infrastructure. Build the target list — how many schools, which bands, which municipalities — and
   put a **per-school number** in the proposal instead of a range. `enem` adds outcome context where
   the engagement is secondary-level.
3. **Match it to the platform the client already runs.**
   [`portabilis/i-educar`](https://github.com/portabilis/i-educar) (🔴 GPL-2.0-or-later, real default
   ref **`2.12`**) is the municipal SIS a Brazilian engagement actually meets;
   [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) (GPL-3.0) for Portuguese/Spanish
   course delivery. Integrate **over the boundary** — web services or LTI 1.3 — so the copyleft stays
   on their side of it (`Pattern A`).
4. **Put the agent in Portuguese, from the shelf.** Tier 4 of [`agents/top.md`](../agents/top.md)
   holds the LATAM-native, Portuguese-first granted agents; `Pattern O` is the full regional build.
5. 🔴 **State the three limits in the proposal, in writing.** The bundled INEP data is a **2023
   snapshot** — currency is the risk, not the licence; the project's own `SOURCES.md` asks you to
   **validate a sample to confirm anonymisation**; and `mcp-brasil` is **not an official government
   service**, so a ministry-facing document cites **INEP** as the source and this as the access path.
   🟢 Its LGPD handling is genuinely documented: education is graded *RISCO ALTO*, the 2022 withdrawal
   and 2024 anonymised resumption are recorded, and `COLUNAS_DISTINCT_PERMITIDAS` whitelists aggregate
   columns only — no `NU_INSCRICAO`, name or CPF.

**Effort:** 2–3 days to a priced, school-level proposal; the integration in step 3 is the engagement.

🔴 **And know what you are walking into.** `Trend 21`: five live 2026 LATAM tenders, **none asking for
open source** — they buy subscriptions and licences. This pattern makes the *total-cost* argument
possible; it does not make the procurement ask for it.

## Pattern AA — 🆕 `p393` The LATAM SME delivery stack, entirely permissive, with billing already in it

**When to reach for this.** A LATAM client — a training provider, a professional body, a private
school group, a corporate academy — needs to **deliver and sell courses in Spanish** and wants to own
closed extensions. Every incumbent regional base is copyleft: **Chamilo** GPL-3.0, **i-educar**
GPL-2.0-or-later, **Moodle** GPL-3.0, **frappe/lms** AGPL-3.0. Until `p393` this shelf had to answer
either *"take the GPL"* or *"build a platform."*

🟢 **The base, and it is new to these shelves:**
[`bmosoluciones/now-lms`](https://github.com/bmosoluciones/now-lms) — **Apache-2.0**, payload read
first-hand (10,915 B, `sha256`₁₆ `a9c4042d767d`, © 2021–2024 BMO Moreno Berroteran Ortiz Soluciones,
**S.A., Nicaragua**), `main` · `53dcb60`, HEAD **2026-08-31 — 52 d**, **676 files, 505 commits, 57
releases**, PyPI `now-lms` v2.0.4. Flask/Python; courses, delivery, certificates and **monetisation**
in the box.

### The stack

| layer | component | grant | why this one |
|---|---|---|---|
| **Platform** | [`bmosoluciones/now-lms`](https://github.com/bmosoluciones/now-lms) | 🟢 **Apache-2.0** | The only Spanish-language LMS on these shelves you can fork, extend and **ship closed**. Flask — a studio reads the whole thing in a day. |
| **Tutor / agent** | the LATAM-native agent tier on [`agents/top.md`](../agents/top.md) | 🟢 MIT | Three granted regional options; one ships as an Open edX plugin, so prefer the standalone ones here. |
| **Interop edge** | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) 🟢 MIT, + [`…/django-lti-dynamic-registration`](https://github.com/Harvard-University-iCommons/django-lti-dynamic-registration) 🟢 MIT | 🟢 MIT | 🔴 **Django, and `now-lms` is Flask** — see the honest caveat below. Needed only when the client must appear **inside someone else's LMS**. |
| **Autograding** (technical courses) | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) 🟢 BSD-3 (**161 ★**, 197 releases) + [`edulinq/autograder-py`](https://github.com/edulinq/autograder-py) 🟢 MIT | 🟢 permissive | Grading and submission halves respectively. Both Python, both beside the platform's own runtime. |
| **Assessment import** | [`vosslab/qti_package_maker`](https://github.com/vosslab/qti_package_maker) | 🟡 **LGPL-3.0** | Ingest existing question banks as QTI. 🟡 **Link it, do not fork it** — LGPL permits the first and not the second. |
| **Public-data sizing** | [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | 🟡 MIT (code only) | For a **Brazilian** engagement, size the market from INEP `censo_escolar` before the first meeting — `Pattern Z`. |

### Wiring it

1. **Fork `now-lms`, pin the Apache-2.0 payload into the delivery record.** Record bytes and
   `sha256`, per `Pattern L` step 1. The appendix is **filled in**, not narrowed — that is the benign
   non-stock case, and worth noting in the record so a later reviewer does not re-raise it.
2. **Keep the agent out of the platform process.** The tutor talks to `now-lms` over HTTP and holds
   its own store. 🔵 This is `Pattern A`'s rule and it survives here for a different reason: not
   copyleft containment, but so the platform fork stays rebaseable onto a 57-release upstream.
3. **Add autograding only for the courses that need it.** `otter-grader` runs containerised; invoke
   it as a job, not in the request path.
4. **Decide the interop edge explicitly, and this is where the caveat bites** (below).
5. **Bill through the platform's own monetisation**, which is the reason to pick this base over
   `academico`. Verify it against the client's local payment rails before promising it — Nicaraguan
   defaults are not Brazilian or Mexican ones.

### 🔴 The caveats, because this base's own history says to write them next to the recipe

- 🔴 **21 ★, and that is the real risk, not the licence.** One company, 505 commits, no multi-tenancy
  claim. **Fork it and plan to own it** — budget maintenance as if upstream may stop. Do not put a
  ministry on it; `Pattern O` and Chamilo remain the public-sector answer.
- 🔴 **The LTI edge is Django and `now-lms` is Flask.** All five Python LTI implementations
  (`p393`, refuting `Gap 391-A` a second time) are **Django** apps or JupyterHub authenticators. If
  the client must launch from a third-party LMS, the edge is a **separate Django service** beside the
  Flask app. 🔵 Note what this is and is not: `p391` published *"the interop edge must be a separate
  runtime"* as a **language** claim and was wrong; here it is a **framework** claim about one specific
  pairing, and it is a deployment line to cost, not an architecture verdict.
- 🟡 **Three of the four non-platform components are copyleft or weak-copyleft** once assessment import
  enters. Keep QTI conversion (`Citolab`, GPL-3.0) and packaging (LGPL-3.0) as **arm's-length tools**
  invoked by a pipeline; nothing copyleft links into the delivered fork.
- 🔴 **Do not reach for the `timeback-*` OneRoster/QTI clients**, however well they fit on paper:
  147 releases, MIT **declared**, and a **source repository that does not resolve** (`Gap 393-B`,
  `Trend 23`). You cannot warrant a grant you cannot read.

🟢 **What the client gets that they cannot buy:** a Spanish-language delivery platform they own
outright, with billing, autograding and an AI tutor — assembled from **four permissive grants read at
the payload**, on a base whose entire source a studio can audit in an afternoon.

## Pattern AB — 🆕 `p394` The statistics and data-science course, graded automatically, including where the network is not

**When to reach for this.** The client teaches **R** — statistics, biostatistics, econometrics,
data science, any quantitative methods course — and wants automated feedback at cohort scale.
🔵 `p393` flagged that this base's most-adopted *maintained* autograder **grades R** while the shelves held no R
components at all; this pattern is the hole closed. 🟢 **And its last step is the only offline
assessment loop in this entire base**, which is what makes it worth reaching for in LATAM and APAC
rather than only in a well-connected university.

**The components, and the licence boundary runs between steps 3 and 5.**

| # | step | component | grant |
|---|---|---|---|
| 1 | Serve identical compute to the cohort | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3-Clause |
| 2 | Author the tutorial the student works inside | [`rstudio/learnr`](https://github.com/rstudio/learnr) | 🟢 **Apache-2.0** *(10,472 B, `60a581bccd57`)* |
| 3 | Grade the exercise and answer back | [`rstudio/gradethis`](https://github.com/rstudio/gradethis) | 🟢 **MIT** *(1,078 B, `48c18e68ffed`)* |
| 4 | Batch-autograde submitted scripts and notebooks | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) + [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | 🟢 BSD-3-Clause both |
| 5 | **Generate the exam** in the LMS's own format | [`cran/exams`](https://github.com/cran/exams) | 🔴 **GPL-2 \| GPL-3 — service boundary** |
| 6 | Calibrate the items after the fact | [`philchalmers/mirt`](https://github.com/philchalmers/mirt) · [`cran/catR`](https://github.com/cran/catR) · [`ShinyItemAnalysis`](https://github.com/patriciamar/ShinyItemAnalysis) | 🔴 **GPL — service boundary** |
| 7 | Carry the generated exam into the LMS | QTI 2.1 / Moodle XML, per `p393`'s **Tier 8** standards layer | per that tier |

**Wiring it.**

1. **Steps 1–4 are your product and they are permissive.** `learnr` renders the tutorial, `gradethis`
   supplies the per-exercise predicate (`grade_this_code()` against a model solution for mechanical
   exercises; `grade_this()` where you must inspect the student's actual object), `ottr` handles
   batch submission. 🟢 A closed-source product may embed all four.
2. **Steps 5–6 run as a separate service, invoked over a process boundary.** 🔴 `cran/exams`, `mirt`,
   `catR` and `ShinyItemAnalysis` are **GPL**; call them as a job — stdin/stdout, a queue, an HTTP
   worker — and never link them into the product. 🔵 Same discipline `Pattern A` and `Pattern O` apply
   to Moodle and Open edX, applied here for the same reason.
3. **Record the disjunctive choice once, in writing.** `cran/exams` is **GPL-2 *or* GPL-3 at the
   licensee's election**. Pick a rung, write down which and why, and keep it with the engagement's
   licence register — downstream compatibility differs between the two, and "GPL" alone is not an
   answer a client's counsel will accept.
4. **Step 5's output is the integration point, and it is wide.** `exams2qti21()`, `exams2moodle()`,
   `exams2canvas()`, `exams2blackboard()`, `exams2ilias()`, `exams2openolat()` — verified from the
   `R/` source filenames in the clone. 🟢 So one authored item bank feeds **whichever** LMS the client
   already runs, which is the opposite of the usual per-platform rewrite.
5. 🟢 **Then NOPS, which is the step nothing else here can do.** `cran/exams` emits a standardised PDF
   that is **printed, sat on paper, scanned, and marked automatically**. 🔵 Use it where the network
   is unreliable, where invigilation must be physical, or where the institution needs a **paper audit
   trail** it can produce years later. 🔴 It is also the honest answer to the finding on
   [`intel/market.md`](../intel/market.md) that **assessment is the lowest-adoption AI use case among
   LATAM faculty**: if the reluctance is about connectivity, invigilation and auditability rather than
   about AI, NOPS addresses the actual objection instead of arguing with it.

🔴 **Two things this pattern does not claim.** **(1)** `ottr` has **3 ★** — the adoption sits on the
Python parent, so you are deploying a lightly-used component and should budget to read its source.
**(2)** `learnr`'s HEAD is **343 days** old. That reads as stable rather than abandoned — the movement
is in `gradethis` (**126 d**) — but it is a dependency whose maintenance a studio should check before
year three, not a vendor commitment.

🔴 **And a provenance warning that will bite at review.** `cran/exams`, `mirt`, `catR`, `TAM` and
`ShinyItemAnalysis` carry **no licence file at any path** — their grant is the `License:` field in
`DESCRIPTION`, which is what CRAN enforces. 🔵 **GitHub's sidebar therefore shows no licence for any of
them**, so a reviewer checking the UI will report five granted GPL packages as unlicensed. Put the
`DESCRIPTION` line in the licence register, not a screenshot of the repository page (`Gap 394-B`).

## Pattern AC — 🆕 `p394` Give teachers an assistant builder instead of building their assistants (EMEA, Moodle)

**When to reach for this.** The client is a **university or school group already running Moodle**,
their teachers keep asking for subject-specific AI assistants, and a studio cannot profitably build
one assistant per course. 🟢 **LAMB inverts the unit of delivery**: the studio delivers the *builder*
and governs it; teachers author the assistants themselves, with no code.

**The components.**

| # | step | component | grant |
|---|---|---|---|
| 1 | The assistant builder and manager | [`Lamb-Project/lamb`](https://github.com/Lamb-Project/lamb) | 🔴 **GPL-3.0** *(35,349 B, `17fe6d0ffa96`)* |
| 2 | Publish each assistant into the LMS | **LTI external tool** — LAMB's own publishing path | 1EdTech LTI |
| 3 | Graded assignments against an assistant | [`Lamb-Project/lamba`](https://github.com/Lamb-Project/lamba) | 🔴 **GPL** |
| 4 | The LMS itself | Moodle | 🔴 GPL-3 |
| 5 | Models, where sovereignty is required | open-weights served locally — LAMB states it shares no user information with model providers and can run on *"open source and open weights models running on your compute"* | per model |

**Wiring it.**

1. **The whole stack is copyleft and that is fine here**, because nothing in it is a product a studio
   resells. 🟢 Moodle is GPL-3, LAMB is GPL-3, LAMBA is GPL — the engagement is **deployment,
   integration, governance and training**, not licensing. 🔵 This is the one shape where the copyleft
   frontier on [`repos/foundations.md`](../repos/foundations.md) costs nothing.
2. **Step 2 is why this is a pattern and not a tool.** Assistants arrive in Moodle as **LTI external
   tools**, so the LMS stays untouched: no plugin to maintain against Moodle's upgrade cycle, no
   fork, and the assistant can be withdrawn without a migration. 🟢 Same architecture `Pattern A`
   prescribes for every agent going into a copyleft LMS, except here the upstream project already
   did it.
3. **Read the tree before you read the badge.** 🔴 LAMB carries **three grants**: root GPL-3,
   `lamb-kb-server-stable/` with its own stock GPL payload, and a **vendored `open-webui/` under
   verbatim BSD-3-Clause** (1,510 B, `6c4b8d8034b9`). `Pattern L` is the procedure; this repository is
   why `Pattern L` exists. 🔵 Check the vendored Open WebUI copy's licence **at the pin you deploy** —
   upstream Open WebUI added branding restrictions in later releases, and the copy vendored here is
   the plain BSD-3 one.
4. **Sovereignty is a configuration, not a port.** Step 5 is the reason to shortlist LAMB for an
   EMEA engagement at all: it is designed to run against locally-served open-weights models and
   states that no user information reaches a model provider. 🟢 That answers the EU AI Act data
   questions in the architecture rather than in a DPA annex.
5. 🔴 **Size it as a high-risk deployment the moment it touches grading.** `lamba` grades assignments.
   Under the EU AI Act, systems that **grade learners, assign them to programmes or influence access
   to qualifications** are **high-risk and need a conformity assessment before deployment** (see
   *EMEA* on [`intel/market.md`](../intel/market.md)). 🟢 So: ship step 2 (assistants that tutor and
   explain) first and get it in front of teachers; treat step 3 (assistants that grade) as a
   **separate, later, assessed workstream**. Selling them as one phase is how an integration project
   becomes a compliance project mid-delivery.

🔴 **The maturity caveat, stated here and not only in the evidence file.** LAMB's own Moodle.org thread
(Feb 2026) describes it as *"at a very beta stage"* with *"a few universities running pilots"*, and the
repository is **one squashed commit** with HEAD **2 d**. 🟢 It is university-authored, peer-reviewed in
*Computer Standards & Interfaces*, and visibly active — **a strong pilot base**. 🔴 It is **not** a
ministry-scale platform, there is no multi-tenancy claim this base has verified, and an engagement
that needs one should read `Pattern O`'s tenancy discussion first. 🔵 Propose it as a pilot with a
named exit, and say so to the client in the first meeting rather than the third.
