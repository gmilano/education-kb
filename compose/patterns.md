---
industry: education
region: Global
updated: 2026-11-18
---

# Compose patterns — education

**Pass `p888`, 2026-11-18** (fifth pass of the day). **Thirty recipes** — 🔵 derived recipes: **30**.
`p888` adds **P29**, the standards-first education build, and **P30**, the licence-arity triage that
`T29`–`T31` now make mandatory before any of these recipes ships.

## P29 — the standards-first education build: source the integration surface, build only the tutor

🔵 **Why this pattern exists.** `p888` byte-verified 36 repositories and sorted them by **measured
12-month commit count**. 🔴 **The top of that list contains no AI tutors.** It contains an LTI 1.3
implementation, an xAPI/SCORM/cmi5 framework, a package validator, a university autograder and a
teaching-lab LIMS. **The integration surface a client engagement cannot avoid has live, licensed,
permissive OSS in every region; the tutor layer is fragmented, mostly unplaced and mostly
pre-traction.** So the build order most studio instincts suggest — model first, integration last —
is exactly inverted.

### The stack, all grants byte-read `2026-11-18`

| Layer | Repo | Grant | Commits 12mo | Job in this recipe |
|---|---|---|---:|---|
| **Launch / identity** | [`parler-haut-interagir-librement/lti`](https://github.com/parler-haut-interagir-librement/lti) + [`…/lti-bundle`](https://github.com/parler-haut-interagir-librement/lti-bundle) | **MIT**, `1,155 B`, `2da07e888147` (identical bytes on both) | 2 | LTI 1.3 **on both sides**: your tool launches from the client's LMS, *and* you can stand up a platform to launch it while their LMS is still being procured. |
| **Content in / out** | [`eddiethedean/lessonkit`](https://github.com/eddiethedean/lessonkit) | **Apache-2.0**, `10,174 B`, `69849221bfb9` | **389** | Emits **xAPI, SCORM and cmi5**, accessibility a stated design goal. The export side of every "can it run in our LMS?" question. |
| **Migration diagnostic** | [`jasonswrench-beep/openstage-package-doctor`](https://github.com/jasonswrench-beep/openstage-package-doctor) | **Apache-2.0**, `11,357 B`, `c71d239df917` | 9 | Opens and validates a SCORM/xAPI/cmi5 package **without the source file**. Run it in week 1 on the client's existing content — it turns a migration guess into an estimate. |
| **Authoring** | [`ad1-kamath/coursecraft`](https://github.com/ad1-kamath/coursecraft) | 🔴 **DISJUNCTIVE `MIT OR Apache-2.0`** — see **P30** | 25 | Clean-room authoring → SCORM/cmi5, Rust. **Elect MIT** and the Apache notice obligation disappears. |
| **Assessment** | [`PrairieLearn/grader-python-v2`](https://github.com/PrairieLearn/grader-python-v2) | **MIT**, `1,072 B`, `0677c780ae82` | **110** | University-maintained Python autograder. Inherit UIUC's autograding posture instead of inventing one. |
| **Platform host** | Moodle (**GPL**) or Open edX (**AGPL-3.0**) | 🔴 copyleft, unchanged by `p888` | — | **Do not replace it.** Put your UI behind it over LTI 1.3 so the platform's accessibility conformance carries the obligation (`agents/top.md`, EAA note). |
| **Tutor** | the bespoke part | — | — | The only layer you write. Compose from `agents/top.md`; keep the model endpoint **swappable** (see regional note). |

### Wiring

1. **Week 1 — measure, don't design.** Point `openstage-package-doctor` at the client's existing
   course packages. You now know how much of the estate is cmi5 vs SCORM 1.2 vs broken. 🔵 This is
   the step that most often changes the shape of the bid.
2. **Weeks 2–3 — stand up launch.** Deploy `lti` as a **platform** so there is a working launch
   target before the client's LMS integration is granted. Swap to **tool** mode when it is.
3. **Weeks 3–5 — content path.** `lessonkit` for authoring/export, `coursecraft` where the client
   wants a desktop-grade authoring tool. Both emit cmi5, so the content path is testable end to end
   before any model exists.
4. **Weeks 5–8 — assessment.** `grader-python-v2` behind a **human decision point**. 🔴 **Assessment
   is Annex III high-risk at the client in the EU** (obligations deferred to **2027-12-02**, not
   cancelled), so the human-in-the-loop is a design constraint, not a nicety.
5. **Weeks 8–12 — the tutor.** Only now. Behind the platform's UI over LTI 1.3.

### Regional elections for this same stack

- **EMEA** — assume the incumbent may be a **state** platform, not a commercial LMS; the
  `ddesignmedia/ByCS_Dashboard` shape (analytics over **ByCS** + Moodle) is the integration you will
  be asked for. Prefer **offline-first** inference: `ali-kin4/skillgraph-tutor` (**Apache-2.0**,
  `11,357 B`, `c71d239df917`) and `bishoynabilanis/jessica` (**MIT**, `1,069 B`, `b345cf910b8e`,
  **212** commits) are both built that way. Where input is **paper**, `Mahmoud-s-Khedr/qbank`
  (**MIT**, `1,070 B`, **121** commits) is the only Arabic-first scanned-workbook ingest this KB
  holds.
- **APAC** — the model endpoint must be **swappable**: `forgemorrow/Chinese-Teaching-AI-Agent` names
  a **domestic** model (MiMo), which is `T25`'s sovereignty expectation observed rather than
  inferred. For reproducibility under a ministry audit, copy
  `KananatSSN/openthaiknowledge`'s **seeded** problem-set generation (**Apache-2.0**, `11,358 B`,
  **103** commits) — of 36 rows verified this pass it is the only one stating determinism as a goal.
- **North America** — lead with institutional provenance: `grader-python-v2` (UIUC) and
  `ICICLE-ai/curriculum-generator` (**BSD-3-Clause**, NSF AI institute, **114** commits). For Canada,
  `mayuribagga/ai-worksheet-maker` is the only Ontario-aligned row this KB has.
- **LATAM** — 🔴 **do not plan to adopt local OSS; plan to build.** All eight new LATAM rows are at
  0–1 stars. Use `sabrinasiilva/pista-enem`'s rule — *"dá pistas, não respostas"*, **hints not
  answers** — and `LMS-COMPASSO/lms`'s **BNCC** alignment as **requirements documents**.
  `giovanebarcelos/ollama-classroom` shows the local-serving shape. `LabSirius/TutorIA` remains the
  most mature LATAM-origin row and is still a backend in progress.

🔴 **What this recipe does not give you.** No row in it publishes a **learning-outcome** result, and
`intel/trends.md` **`T9`**'s largest trial (2,379 undergraduates) found a **negative** effect from
course-integrated AI tutor access. **Sell the integration surface and the teacher-time saving. Do not
sell an attainment claim.** And no row added this pass publishes a **VPAT/ACR** — `lessonkit` states
accessibility as a goal, which is not a conformance document.

## P30 — licence-arity triage, to be run before any of P1–P29 ships

🔵 **`T29`–`T31` make this a precondition, not an audit step.** Three outcomes, three different
obligations, and the cheap tests that separate them — **none of which requires a clone**.

| Step | Test | Verdict |
|---|---|---|
| 1 | Metadata returns **`NOASSERTION`** while bytes return a family | 🔴 **CONJUNCTIVE candidate** (`p887`). Both families bind; compliance is the **union** of notice sets. Read **every** licence-ish path *and* scan each payload for **multiple family titles in one file** — `apereo/java-cas-client` carries two families in one 2,321-byte file, so a path-keyed map cannot express it. The key is **`(path, byte span)`**. |
| 2 | **`LICENSE-<FAMILY>` filename pair** + manifest `license` expression containing **`OR`** | 🟢 **DISJUNCTIVE** (`T29`). **Elect one family, record the election**, and you owe only that one. `ad1-kamath/coursecraft` → elect **MIT**, owe no Apache `NOTICE`. 🔴 Metadata will report only **one** of the two and will not flag the loss. |
| 3 | Family signatures matched by **presence** | 🔴 **Re-test for SUBSUMPTION** (`T31`). `BSD-2-Clause`'s signature is **clause 2 of `BSD-3-Clause`**; presence-matching reports `arity=2` on every BSD-3 file. Apply `SUBSUMES = {"BSD-3-Clause": {"BSD-2-Clause"}}` **before** reporting any arity. |
| 4 | A `NOTICE` file carries a family body | 🔵 **A `NOTICE` is not a grant by default** (`p887`), **but it must still be read** — `apereo/phpCAS`'s BSD half lives in `NOTICE` (3,914 B, `2df146a253fa`). Read it; do not count it as the grant unless it is the only payload. |
| 5 | Byte-count equality against a "pristine" reference | 🔴 **Not a valid test.** `p888` byte-read unmodified Apache-2.0 at **11,357 B** (`c71d239df917`, on four unrelated repos), **11,358 B**, **11,354 B** and the appendix-stripped **10,174 B**. **A byte-count test would have flagged three of six Apache rows as modified.** `11,357 B / c71d239df917` is a usable **positive** fingerprint; its absence proves nothing. |

🔵 **And the governing instruction from `887-G1`, which applies to every step above:** **a shelf note
is this instrument's test oracle.** Before publishing an arity verdict on a row, grep the shelves for
that slug — `p887` shipped a wrong family for `java-cas-client` with the right answer sitting two
lines below the row, and `p880` had made the same error on the same file. **Where no shelf note
exists** (every row `p888` added), **the substitute oracle is the metadata channel**: diff the byte
verdict against `license.spdx_id` and chase every disagreement to a declaration. That diff is the
`api_spdx` vs `bytes_families` column pair in
[`evidence/grant-verify-888.2026-11-18-p888.tsv`](../evidence/grant-verify-888.2026-11-18-p888.tsv),
and it is what surfaced `coursecraft`.


**Pass `p887`, 2026-11-18** (fourth pass of the day). **Twenty-eight recipes** — 🔵 derived
recipes: **28**. `p887` adds **P28**, which is `P27`'s recipe applied to the one real estate this
pass measured end to end: **the Apereo identity stack a university inherits the moment it adopts CAS
for single sign-on** — three repositories, two of them conjunctive grants, one of them dormant, and
a notice set of two families plus 21 third-party holders.

---

## 🟢 **P28** — Apereo identity + rostering + LRS for an institutional estate, with the notice set it actually owes

**When.** A university engagement that needs SSO across an existing estate (Moodle, a Sakai
remnant, a JVM portal) plus learning-record capture for AI tutoring analytics. 🔵 **This is the
single most common substrate ask in a higher-education engagement and it is the one whose licence
surface this base has now measured first-hand, every repository, every byte.**

**The components, all byte-read at `p887` with `arity_own` resolved by tree enumeration:**

| Component | Repo | Grant, byte-read | ★ | Commits 12mo | Role in the recipe |
|---|---|---|---:|---:|---|
| SSO server | https://github.com/apereo/cas | **Apache-2.0** (`LICENSE`, 11,358 B, `cfc7749b96f6`) | **11,402** | **5,530** | The CAS/SAML/OIDC server. `arity_own = 1`. Very live. |
| PHP client | https://github.com/apereo/phpCAS | 🔴 **Apache-2.0 *and* BSD-3-Clause** — `LICENSE` 11,357 B `c71d239df917` **+** `NOTICE` 3,914 B `2df146a253fa` © 2003-2007 ESUP-Portail | 802 | 🔴 **8** | How Moodle and PHP estates attach. 🔴 **Near-dormant — pin a commit, do not track `master`.** |
| JVM client | https://github.com/apereo/java-cas-client | 🔴 **Apache-2.0 *and* BSD-3-Clause in ONE 2,321 B file** (`6c21b465e3a0`) | 949 | 170 | How a JVM portal attaches. 🔴 Metadata channel says **`NOASSERTION`**. |
| Rostering reference | https://github.com/ox-it/wl-roster2 | **ECL-2.0** (`sakai-10.x/LICENSE`, 11,110 B, `6001bb8caa76`) | 0 | 🔴 **0** | 🔴 **DORMANT since 2016.** **Read it, do not depend on it** — it is Oxford's worked example of roster sync, and its value is the design, not the code. |
| Learning records | https://github.com/yetanalytics/lrsql | **Apache-2.0** (`LICENSE`, 11,357 B) | 144 | 67 | xAPI/SQL learning-record store — where tutoring interactions land. 🔴 `NOTICE` 19,985 B, **21 holders**. |

**Wiring.**

1. **`apereo/cas` as the only identity authority.** Deploy it as the CAS/OIDC server; every
   downstream service authenticates against it and none holds credentials. Apache-2.0, `arity_own = 1`
   — no licence work needed beyond the standard `NOTICE`.
2. **Attach the estate with the matching client, pinned.** PHP services (Moodle) via `phpCAS`; JVM
   services via `java-cas-client`. 🔴 **Pin both to a commit SHA.** `phpCAS` has `8` commits in 12
   months, so tracking `master` buys nothing and risks a silent change on a near-abandoned
   dependency.
3. **Take `wl-roster2` as a design document, not a dependency.** It shows how a real university
   wired roster sync into a Sakai-era estate. `0` commits in 12 months and `pushed_at 2016-06-03`:
   lift the approach, write the code against the current rostering API.
4. **Land learning records in `lrsql`.** Point the tutoring layer's xAPI statements at it; it is the
   join key between "what the AI did" and "what the student did", which is what every institutional
   evaluation of an AI tutor eventually asks for.
5. 🔴 **Produce the notice set BEFORE shipping, with `P27`'s procedure.** Run
   `compose/code/p887-grant-arity-map/arity_map.py` over the five slugs, then
   `p427-conjunctive-grant`'s `notice_obligation()` over each payload it returns.

**The notice set this estate owes, resolved rather than assumed:**

- **Apache-2.0** notice and `LICENSE` copy — for `cas`, `phpCAS`, `java-cas-client`, `lrsql`.
- **BSD-3-Clause** notice with its **no-endorsement clause naming JA-SIG, Inc.** — for *both* CAS
  clients. 🔴 **This is the obligation a single-family `Apache-2.0` label silently drops**, and this
  base carried exactly that label on `phpCAS` until `p887` byte-read its `NOTICE`.
- **ESUP-Portail consortium** copyright (© 2003-2007) — `phpCAS`.
- **JA-SIG, Inc.** copyright (© 2007) — `java-cas-client`.
- **ECL-2.0** notice — only if `wl-roster2` code is actually lifted rather than read.
- 🔴 **`lrsql`'s 21 third-party holders**, from its 19,985 B `NOTICE`. The licence is one family; the
  attribution is of 21.

**Cost.** 🟢 Everything here is permissive and build-safe — there is no copyleft in this path, which
is the point of choosing it over an AGPL-3.0 identity or LRS option. 🔵 **Budget the licence work as
real work anyway**: two of the five repositories are conjunctive, one has a dormant upstream, and the
notice set has **21 + 2** entries. That is a half-day of legal-adjacent effort that is invisible
until someone asks for an attribution file.

**Pitfall this recipe exists to prevent.** 🔴 **Reading the SPDX field.** It returns `Apache-2.0` for
`phpCAS` (true but incomplete) and **`NOASSERTION`** for `java-cas-client` (an abstention that is
easy to read as "unlicensed" and treat as all-rights-reserved). 🔵 **Both repositories are
permissive. The field cannot say so.** `T26` has the detector; `886-G5` has the cautionary case of
what happens when a base publishes an abstention as an absence.

---

**Previous pass (`p886`), retained:** **Pass `p886`, 2026-11-18** (third pass of the day). **Twenty-seven recipes** — 🔵 derived recipes:
**27**. `p886` adds **P27**, and it is the step `P23` cannot perform and `P24` silently assumed:
**resolving the ARITY of a grant, and producing the notice set a redistribution actually owes.**
`p886` also amends **`P24`**, whose base repository turns out to carry two grants rather than one.

## P27 — Resolve licence arity and produce the redistribution notice set — new in `p886`

🔵 **The problem, measured rather than asserted.** `p886` ran `885-G1`'s two-channel licence test over
all 163 shelf rows in this KB. `144` agreed (88.3%) — and **four rows carry a grant that neither
channel can express, three of which scored `AGREE`**
([`record`](../evidence/dual-channel-885G1.2026-11-18-p886.tsv)). `19 / 163` rows (**11.7%**) carry a
licence-policy document that no single-file probe reads. 🔴 **A client shipping a product built on
any of those rows is shipping an incomplete notice set, and neither GitHub's licence field nor a root
`LICENSE` read will tell them.**

🔴 **Why `P23` does not cover this.** `P23` cross-checks **three independent channels** to decide
whether *one* grant claim is true. P27 answers a different question — **how many grants are there,
and over which paths** — and it needs a channel `P23` does not use: the repository tree itself.

### Stack — every component permissive, every licence byte-read in `p886`

| Role | Component | Licence | Why this one |
|---|---|---|---|
| Tree enumeration | `git` ≥ 2.19 (`--filter=blob:none`) + [`compose/code/p215-lstree-grant-recovery`](code/p215-lstree-grant-recovery/) / `make enumerate` | GPL-2.0 (tool, not linked); modules this KB's own | The **only** complete channel: `/repos/{owner}/{repo}` is `403` from a sandboxed runner, and every path-guessing ladder finds only filenames somebody thought of. 🟡 **Reuse these, do not rebuild**: `make ladder-audit` grades 919 ladders across 510 instruments, **57** already `TREE-ENUMERATED`, and `p885` regressed by writing a new one (`886-G2`) |
| Grant classification | [`compose/code/p886-dual-channel-grant`](code/p886-dual-channel-grant/) + [`p228-shelf-gate`](code/p228-shelf-gate/) | this KB's own | Earliest-title rule; **30 controls**, incl. Iberian GNU titles, ODbL, bare-token grants and `p872`'s false-positive regression set |
| SPDX expression validation | [`spdx/tools-python`](https://github.com/spdx/tools-python) | **Apache-2.0** | Parses and validates `A AND B` / `A OR B`; the reference implementation of the expression grammar |
| SBOM assembly | [`anchore/syft`](https://github.com/anchore/syft) | **Apache-2.0** | Emits SPDX/CycloneDX per module; picks up the **per-directory** `go.mod` boundaries that make `packages/*` separable |
| Dependency-licence closure | [`compose/code/dependency-licence-closure`](code/dependency-licence-closure/) | this KB's own | Carried from earlier passes; P27 feeds it a **set** of roots instead of one |
| Orchestration | [`temporalio/temporal`](https://github.com/temporalio/temporal) | **MIT** | Re-run per release tag; a grant is a property of a **tag**, not of a repository |

### How to wire it — six steps, and step 4 is the one nobody does

1. **Enumerate, do not guess.** Per candidate repository:
   ```sh
   git clone --depth 1 --filter=blob:none --no-checkout "https://github.com/$SLUG" "$D"
   git -C "$D" ls-tree -r --name-only HEAD \
     | grep -iE '(^|/)(LICEN[CS]E|NOTICE|COPYING|COPYRIGHT)' > "$D/.licence-paths"
   ```
   On `sudosylabs/proctor` this returns **6** payloads out of **3,288** paths; a 37-entry path ladder
   returned **1**.
2. **Byte-read every payload** with `git cat-file -p HEAD:<path>` — no checkout, no working tree —
   and classify each with `classify2.py`. Record `path`, `bytes`, `sha256₁₂`, `family`.
3. **Derive the arity.** One distinct family over the whole tree → arity 1, done. More than one →
   map **family to path prefix**, which is the deliverable: *"AGPL-3.0 over `server/` and `webapp/`;
   Apache-2.0 over `packages/cache`, `packages/mail`, `packages/vfs`; BSD-3-Clause over
   `server/internal/autocert`."*
4. 🔴 **Read the policy document, and then verify it instead of believing it.** Fetch
   `LICENSING.md`, `NOTICE`, `THIRD_PARTY_NOTICES.md`. It is the only source for **`AND` vs `OR`** —
   `eduOS-rs` is `OR` (elect one), `EduWork` is `AND` (satisfy both), and **the two files look
   identical to a prober**. 🔴 Then check its claims: `proctor`'s asserts an SPDX header on every
   comment-capable file and **`0` of 65 files under `packages/` have one**. Record each claim as
   `HELD` or `REFUTED` with the command that decided it.
5. **Emit the notice set** — for `AND` and per-directory grants, *every* licence text plus *every*
   `NOTICE`, with the path scope each governs. This is the artefact that makes the engagement
   defensible, and `syft` will not produce it from metadata alone.
6. **Pin and re-run per tag.** `EduWork`'s own `LICENSING.md` states that previously distributed
   versions and npm archives **keep their existing licences**, and that the switch applies from a
   named commit (`a43a4d42`). 🔵 **"Project X is licence Y" is not a statement that survives contact
   with a specific tag** — so the Temporal workflow keys on the tag.

### What the client gets, and what to charge for

🟢 **Deliverable:** a per-path grant map, a validated SPDX expression per module, a complete notice
set, and a `HELD/REFUTED` table for every claim the project's own policy document makes — each row
carrying the byte count and `sha256₁₂` that produced it.

🔵 **Scope:** 2–3 weeks for a shortlist of 10–15 repositories. 🔵 **Sell it as the gate before a
build decision**, not as an audit after one: the finding that `packages/*` is Apache-2.0 while the
domain logic is AGPL-3.0 changes *what you build*, and it is worth nothing discovered at integration
time. 🔴 **State the limit honestly:** this produces a defensible engineering record, not a legal
opinion, and a conjunctive grant across jurisdictions (`MulanPSL-2.0 AND MIT`) is exactly the case
where counsel should see the notice set before shipping.

### 🔴 Amendment to `P24`, required by this pass

`P24` ships a branded institutional distribution on `ECNU/EduWork`. **`EduWork` is
`MulanPSL-2.0 AND MIT`, not `MulanPSL-2.0`**
(`LICENSE` 9,233 B `eb7a1d713eb9` **and** `LICENSE-MIT` 1,085 B `dc719b536b8f`;
`LICENSING.md` 3,048 B `e85e94f2cc4a`). Three line items change:

- 🔴 **The redistribution must carry BOTH licence texts and both notice sets.** The policy is
  explicit: *"Distributions combining new Mulan-licensed contributions and historical MIT code must
  retain both licenses and their notices."* Add it to the build's artefact checklist.
- 🔴 **Do not offer the client an "elect MIT" route.** The same document states the expression is
  *"not a choice of license for all code"*. A procurement team that will not clear MulanPSL-2.0 must
  still clear it; saying otherwise is the error `P27` exists to prevent.
- 🔴 **Narrow the patent claim.** `agents/top.md` credited the row with **9 patent references**; the
  policy states the relicence *"does not make historical MIT contributors grant additional patent
  rights under Mulan"*, so that peace **does not extend to the pre-`a43a4d42` baseline**.
- 🟢 **One thing gets better.** `packages/dsh-literature` **retains MIT in its entirety** — a
  wholly-permissive, separable component inside the distribution, and the cleanest unit to lift if a
  client wants the literature capability without the platform.

**Previous pass (`p885`), retained:** **Pass `p885`, 2026-11-18** (second pass of the day). **Twenty-six recipes** — 🔵 derived recipes:
**26**. `p885` adds **P26**, and it is the recipe this KB's own instruments have been accumulating
without anyone writing it down: **when the client IS the university, its own GitHub organisation is a
supply source — and `p885` measured both what that yields and what it costs to make it safe.**

- 🟢 **P26 is buildable now because this pass built the missing gate.** `884-G2` left this KB's grant
  probe blind to **5.3%** of repositories and, among permissive ones with a non-standard default
  branch, **26.5%** were reported as having no licence when they do.
  `compose/code/p885-symref-grant-ladder/fetch_grants.sh` closes that, with 13 controls.
- 🟡 **Scope honestly set by measurement, which is the part a proposal usually gets wrong.** A sweep
  of a university organisation yields **one or two liftable components and several hundred homework
  repositories** — 6,486 repositories across 33 organisations produced `362` education repos, of
  which **90.3% carry no licence at all** and `5` were permissive and live. **P26 therefore sells a
  gate and a shortlist, not a treasure hunt.**
- 🟢 **One shelved row corrected by applying this pass's own fix to it.** `ls1intum/Artemis`'s
  default branch is **`develop`**, not `main`; this KB's row says *"byte-read `main/LICENSE`"*. The
  bytes are **identical on `main`, `master` and `develop`** (`1,091 B`, `sha256₁₂ 63a0a2b4d6d9`,
  *"MIT License"*), so **the row's verdict was right and only its ref label was imprecise** —
  recorded because a correction that changes nothing still has to be visible.

---

## P26 — Harvest the client's own institutional estate, behind a grant-and-liveness gate — new in `p885`

🔵 **When to reach for this.** The engagement is with a university, a ministry or a school system
that **already publishes code** — a Sakai/Moodle/Canvas estate, a library-systems group, a research-IT
group. The client assumes its own repositories are reusable assets. **Usually they are not, and the
reason is licensing and liveness, not quality.** This pattern turns that assumption into a measured
shortlist in days, and it is the cheapest credible opening engagement this KB carries.

🔴 **The two failure modes it exists to prevent**, both measured by `p885` rather than imagined:
1. **Manufactured absence.** Probing `main` and `master` alone reports *"no licence"* on **26.5%** of
   permissive repositories whose default branch is something else. Oxford's `ECL-2.0` Sakai rostering
   component was invisible to this KB for 885 passes for exactly this reason.
2. **Manufactured presence.** `license.spdx_id` can assert a grant whose payload does not exist
   (`ox-it/OxfordIDN_Case-Studies`: `MIT` in the field, no licence file on its only branch), and a
   vendor roundup can assert MIT where the field says `NOASSERTION` (**Flowise**). **Neither channel
   alone is sufficient.**

### The wiring

| Step | Component | Licence | What it does here |
|---|---|---|---|
| 1 · Enumerate | `api.github.com/search/repositories?q=org:<handle>&per_page=100&sort=updated` **paginated to exhaustion** | — | 🔴 **Do not stop at page 1 and do not sort by stars** if the target is the tail: the cap is 100 and silent. `p885` lost `3,186` of `6,486` repositories that way. 🟡 Conversely, if the target is *liftable components*, `sort=stars` is **safe** — measured: the tail is coursework. |
| 2 · Separate education from ML | `compose/code/p884-edu-vocabulary/classify_edu.py` | KB-internal | TIER-A / TIER-B split. Essential in a university: `curriculum learning`, `gradient`, `coarse` and `example` all collide with education vocabulary. Without it a naive keyword set returns ~326 finds that are almost all false. |
| 3 · Resolve the grant | `compose/code/p885-symref-grant-ladder/fetch_grants.sh` | KB-internal | `git ls-remote --symref` → probe **that** ref → fall back to `main`/`master` → dual-file (`LICENSE-APACHE`+`LICENSE-MIT`) arm. Emits bytes + `sha256₁₂` per repo, and reports the **unresolved ref** on a miss so a 404 can never read as "no licence". |
| 4 · Resolve liveness | `git ls-remote --symref` + default-branch `HEAD` | — | 🔴 `pushed_at` **lies about activity**: it moves on any branch. `p883` found three rows with perfect licences and default branches 13–22 months stale. 🟡 Report as **`HEAD ≥ date`** — `883-G3`'s bound is still unconverged, so the figure is a lower bound, and a proposal must say so. |
| 5 · Cross-check the field | `search/repositories` `license.spdx_id` vs step 3's bytes | — | **Disagreement is a finding, not a tie to break.** Record both and escalate to a human read. |
| 6 · Wire the shortlist | https://github.com/vishalsachdev/canvas-mcp | **MIT** — `1,071 B`, `5385a26e2fac` | **334 ★**, pushed 2026-11-17. The read/write bridge to the incumbent LMS. 🔴 **Pin ≥ 1.16.0**: `GHSA-7pp5-29mw-9jq3` (CVSS 7.8, CWE-94) is a sandbox escape via `child_process` in local mode. Scope the Canvas token; `GHSA-hmr8-mvr2-mvw5` is grade-changing prompt injection. |
| 7 · Grading, if assessment is in scope | https://github.com/ls1intum/Artemis | **MIT** — `1,091 B`, `63a0a2b4d6d9` | **832 ★**, pushed 2026-11-18, default branch **`develop`**. Ten years old, OpenSSF Scorecard + Best Practices. The largest permissive education system in this KB. |
| 8 · Sandboxed execution | https://github.com/ls1intum/Ares | **MIT** | **27 ★**, JUnit 5 secure sandbox. 🔴 **Default-branch `HEAD ≥ 2025-09-11` (~14 months).** Liftable as a **frozen component you own the maintenance of** — or not at all. Do not present it as actively developed. |
| 9 · Write the mark back | https://github.com/cilt-uct/tsugi-request-gradebook-upload | **Apache-2.0** | **0 ★**, created 2026-08-06, pushed 2026-10-06. UCT's real gradebook→SIS upload scheduler (Brightspace→PeopleSoft). 🔴 **Zero stars: a reference implementation of the boundary, not a dependency.** The credit-award step stays human — see **P25**. |
| 10 · Rostering reference | https://github.com/ox-it/wl-roster2 | **`ECL-2.0`** — `11,110 B`, `6001bb8caa76` | 🟢 **Recovered by this pass.** Default branch `sakai-10.x`. Shows how a real university wired roster sync. Reference reading; Sakai-10-era. |

### What the client gets, and what to charge for

🟢 **Deliverable 1 — a licence-and-liveness register of their own estate**, every row byte-read and
`--symref`-resolved, with the disagreements between GitHub's metadata and the actual payload called
out. 🔵 **No vendor sells this and every university needs it before it can let a contractor touch its
code.** `p885` measured **76.4% no-grant in the head of the distribution and 90.3% in the tail** —
expect the client's own number to be in that band, and expect it to surprise them.

🟢 **Deliverable 2 — a shortlist of genuinely liftable components**, typically 1–5 repositories, each
with its grant, its real default-branch liveness, and an explicit *"frozen, you own maintenance"* or
*"actively developed"* verdict.

🔴 **The honest sizing, which protects the engagement.** Promise the **gate and the register**, whose
output is certain, and present the shortlist as **whatever the gate finds** — because across 33
institutions it found `5` permissive live education repositories and **none of them was an agent or
a platform.** 🔵 **A pattern that promises a treasure hunt here will fail; one that promises a clean
inventory will not.**

---

**Previous pass (`p884`), retained:** **Pass `p884`, 2026-11-18** (first pass of the day). **Twenty-five recipes** — 🔵 derived recipes: **25**.
`p884` adds **P25**, and it closes the gap this file has carried longest: every education engagement
ends at the **grade-to-record boundary**, and no recipe here addressed writing a mark back into the
system of record. 🟢 **It is buildable now because `p884` found the missing component** — a real,
permissive, institution-published implementation of a gradebook→SIS write-back
(`cilt-uct/tsugi-request-gradebook-upload`, Apache-2.0), plus the human credit-award step modelled on
Helsinki's `suoritustarkistin` (MIT, pushed 2026-11-17). 🔴 **The pattern is compliant by construction
in two jurisdictions at once:** Brazil's `Resolução CNE/CP nº 1/2026` forbids attributing a grade to
an AI assessment, and the EU's Annex III education obligations treat assessment as high-risk — keeping
the award human satisfies both, and the recipe is laid out per region.
🟢 **`Tsugi` is the other half**, newly shelved in `verticals/solutions.md`: an LTI app is a process
boundary the LMS vendor already supports, which is how this file's standing *"attach, don't fork"*
advice finally has a named mechanism.

**Previous pass (`p883`), retained:** **Pass `p883`, 2026-11-17** (thirteenth pass of the day). `p883` adds **P24**, and it is the first recipe in this file whose reference
implementation is a **university's own shipped product**: an institutional AI distribution built on an
MIT agent harness (`deepseek-ai/deepseek-harness`, 282,965 ★) rather than a plugin bolted inside a
copyleft LMS — found this pass, with the branding step already executed in public by its authors.
🟢 **`P23` is also amended**: its *liveness* channel, which `p882` could answer only with
`pushed_at`, now has a real limb — `api.github.com/search/commits` returns **default-branch** dates,
and `p883` measured `pushed_at` overstating liveness by up to **22 months** on this KB's own rows.

**Previous pass (`p882`), retained:** **Pass `p882`, 2026-11-17** (twelfth pass of the day). **Twenty-three recipes** — 🔵 derived recipes: **23**. `p882` adds **P23**, the open-source **due-diligence** recipe this KB has been
performing for 882 passes and never written down as a deliverable: a two-channel verification
harness that answers *is this repo safe to build on* in licence, liveness and identity terms, and
which exists because `p882` measured that the three channels fail **independently** and a client's
shortlist has to survive all three. It also records the layer gradient (`T20`) as the selection rule
that `P19` and `P20` were already instances of.

**Previous pass (`p879`), retained:** **Pass `p879`, 2026-11-17** (ninth pass of the day). **Twenty recipes** — `p879` adds **P19**
(Open edX capability **without** the AGPL obligation: the platform's component layer is Apache-2.0,
so the deliverable can be Globant's even when the host platform is copyleft) and **P20** (the
offline-first content supply chain, MIT end to end — `ricecooker` → `studio` → Kolibri →
`morango`, which is the piece that makes an offline programme *measurable* and therefore
renewable). It also repairs the stale `openedx/edx-platform` slug in **P16**'s table.

**Previous pass (`p878`), retained:** **Pass `p878`, 2026-11-17** (eighth pass of the day). **Eighteen recipes** — `p878` adds **P17**
(MIT auto-grading at scale, with integrity by design rather than surveillance — newly possible
because `ls1intum/Artemis` exists and is MIT) and **P18** (paper-first assessment capture for
low-bandwidth systems, built on an MIT OMR grader and Brazil's incumbent SIS, both surfaced this
pass). It also **repairs P9**, whose LATAM-origin base was chosen when this KB believed LATAM had
almost no open-source education software — a belief `p878` showed was an artefact of searching only
in English.

**Previous pass (`p877`), retained:** Pass `p877`, 2026-11-17** (seventh pass of the day). **Sixteen recipes** — `p877` adds **P15**
(the consent-and-opt-out spine, driven by a new US statute) and **P16** (permissive SIS
modernisation, newly possible), and **repairs P5**, whose offline stack was assembled without the
largest permissively licensed offline education server in the index.

> 🔴 **P5 repaired.** It specified Kiwix (**GPL-3.0**) and Internet-in-a-Box (**LGPL**) as the
> offline substrate while [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
> — **Apache-2.0, 43,849★, 4,526 forks, 813 commits/12mo** — sat unshelved in this KB's sweep logs.
> **A ministry deliverable built on the old stack inherits copyleft obligations it never needed to.**
> P5 now leads with NOMAD and keeps Kiwix/IIAB as the fallback they should always have been.

> 🔴 **No pattern in this file ever depended on PageLM, which is the only reason `p877` is not
> rewriting several of them.** PageLM's licence prohibits redistribution and requires a
> revenue-share (`intel/trends.md` **T14**) — it was in `agents/top.md` as `MIT` for fourteen months.
> 🔵 **Standing rule for this file: a component enters a stack table only with its licence
> byte-read, because a pattern is the artefact that gets handed to a client as a build plan.**

**Previous pass note (`p876`)** (sixth pass of the day). **Fourteen recipes** — `p876` adds **P14**,
the measurement spine, and **repairs the telemetry row in P1, P7 and P9**, which until this pass
pointed every measurement promise in this file at a Learning Record Store whose default branch
last moved in **November 2021**.

> 🟢 **The caveat `p875` attached to this whole file is WITHDRAWN.** It read: *"`p875` found no
> maintained permissive replacement."* Two exist, and `p875`'s own sweep had listed them:
> **`yetanalytics/lrsql`** (Apache-2.0, 144★, 67 commits in 12 months) and **`openfun/ralph`**
> (MIT, 52★, France Université Numérique, **Open edX→xAPI converters in-tree**). Both are now in
> `repos/foundations.md` and wired into the stacks below.
>
> 🔴 **What survives, and must stay in every statement of work: neither ships dashboards.**
> Learning Locker bundled a reporting UI; `lrsql` is a store and `ralph` is a store plus a
> pipeline. **Price the visualisation layer** (Aspects/Superset, or Grafana over Postgres) as a
> line item. See **P14**.

**Previous pass note (`p875`)** (fifth pass of the day). **Thirteen recipes** — `p875` adds **P12**,
a hardened OpenMAIC classroom built on the licence question this KB has now settled four ways and
on a **student-data exposure in OpenMAIC's default configuration that its own README documents**;
and **P13**, US district policy conformance sold against published state deadlines rather than
against an AI thesis.

🔴 **P11 carries a corrected date.** It was written on a literacy duty "binding since July 2026."
**The duty has applied since 2 February 2025**, and a *second* duty — transparency for chatbots and
AI-generated content — went live **2 August 2026**. **P11's argument strengthens and its dates
change**; see the corrected **T11**. Any P11 deck in circulation must be fixed.

🟡 ~~**A caveat now attaches to every pattern in this file that promises measurement** (P1, P5, P7
especially): **the xAPI Learning Record Store they route telemetry through, `LearningLocker`, has
not been pushed since May 2024.** `p875` found no maintained permissive replacement. Budget a
maintained fork explicitly, or fall back to the LMS gradebook and say so.~~ 🟢 **Superseded by
`p876`** — see the banner above. The dormancy figure was also wrong: **2021-11-16, five years.**

**Previous pass note (`p873`):** ten recipes — `p871`'s six, `p872`'s **P7**
and **P8** (and its rewrite of **P2**), plus **P9** and **P10** added by `p873`: a Spanish-language
tutor built on the LATAM-origin base this KB verified for the first time, and an
accessibility-gated public-sector bid. Every repo named below was verified
(existence via `git ls-remote`, licence via the licence bytes on the resolved default branch);
licences are stated inline because in this vertical the licence determines the architecture.
Effort estimates are studio-delivery estimates, not measurements.

---

## 🆕 `p881` · 2026-11-17 — what changed on this shelf

🟢 **One new recipe, `P22`, built on this pass's own two promotions** — `zhangl1001/civil-ai` as the
agent foundation and `wenflow-org/wenflow` as the problem-first intake, wired to platforms this shelf
already carries. It is below, with the licence boundary stated per component.

🔴 **The two components are 20 and 5 days from their last commit respectively and neither has a measured
star count**, because `api.github.com` is `403` this session. Price the maturity flags in
`agents/top.md` into any engagement that starts from `P-22`.

## 🆕 `p880` · 2026-11-17 — what changed on this shelf

🟢 **`P21` — the LMS write bridge, rebuilt**, restoring `CANVAS-TOKEN-RESIDUAL`: two mounts rather
than one, `>=1.16.0` pinned, a Node.js `22.18` floor asserted, and the token **scoped** rather than
merely upgraded, because even patched code in local sandbox mode still reaches the caller's Canvas
token. 🔴 Includes the `p880` finding that the four governing advisories are absent from the global
advisory database, so they must be entered in the client's risk register by hand.

## P1 — FERPA/LGPD-defensible self-hosted tutor

**Sell to:** North America (FERPA), LATAM (LGPD), EMEA institutions that are not renewing
commercial AI contracts. **Effort: 8–10 weeks.**

The proposition is one sentence: *student data never leaves your tenancy.* That is an
architecture claim, so every component must be self-hostable.

| Layer | Component | Licence |
|---|---|---|
| Tutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 |
| Retrieval | https://github.com/HKUDS/LightRAG (inside DeepTutor) | MIT |
| Model serving | https://github.com/ollama/ollama (pilot) → https://github.com/vllm-project/vllm (cohort scale) | MIT / Apache-2.0 |
| Model gateway | https://github.com/BerriAI/litellm | MIT |
| Ingestion | https://github.com/docling-project/docling + https://github.com/SYSTRAN/faster-whisper | MIT / MIT |
| LMS attachment | https://github.com/Cvmcosta/ltijs | Apache-2.0 |
| Telemetry | https://github.com/yetanalytics/lrsql | **Apache-2.0** |
| Telemetry reporting (price it — the LRS has no UI) | https://github.com/openedx/openedx-aspects, or Grafana over the LRS's Postgres | Apache-2.0 / AGPL-3.0 |

**Wiring.** Docling parses the institution's course PDFs and faster-whisper transcribes lecture
capture (pull the video from Opencast if the client already runs it); both feed DeepTutor's
LightRAG index. DeepTutor talks to LiteLLM, never directly to a provider — that single seam is
what lets the institution swap to a sovereign or on-prem model later without touching the
application. `ltijs` wraps the tutor as an LTI 1.3 tool so it launches from inside Moodle,
Canvas or Open edX with grade passback, which means **no fork of the AGPL/GPL platform**.
Every learner interaction is emitted as xAPI to **SQL LRS (`lrsql`)** so efficacy can be measured
instead of asserted. 🟢 **`p876` replaced Learning Locker here**: `lrsql` is Apache-2.0 (no
copyleft to contain at all), runs on the Postgres the deployment already has, and speaks OIDC so
it joins the institution's existing identity provider instead of carrying its own user table.

**Why this order:** start with Ollama for the pilot, move to vLLM only when a whole cohort hits
the tutor in one lab session. Swapping is a LiteLLM config change.

---

## P2 — AI-assisted grading with a defensible human-review trail

**Sell to:** LATAM first (LGPD already grants automated-decision review rights), then EMEA
ahead of 2 December 2027, then North America. **Effort: 10–12 weeks.**

**Revised in `p872`.** `p871` built this pattern around the absence of a grading component.
That absence is gone: **ArguLens** (`wwrwbs/AI_AWE`, Apache-2.0) is a real, verified, permissive
essay-scoring system whose **scorer is a grade-independent LightGBM model over 31 explicit
linguistic and discourse features — not an LLM.** That property is the entire compliance case,
so the scorer now replaces a prompt at the centre of this recipe.

| Layer | Component | Licence |
|---|---|---|
| **Scoring engine** | https://github.com/wwrwbs/AI_AWE (ArguLens) | **Apache-2.0** |
| Assessment substrate | https://github.com/openedx/edx-ora2 | AGPL-3.0 |
| Orchestration / policy | https://github.com/langchain-ai/langgraph | MIT |
| Model gateway | https://github.com/BerriAI/litellm | MIT |
| Rubric gold sets | https://github.com/HumanSignal/label-studio | Apache-2.0 |
| Teacher-in-the-loop review | https://github.com/argilla-io/argilla | Apache-2.0 |
| Regression / safety gates | https://github.com/promptfoo/promptfoo | MIT |
| Item rendering | https://github.com/Citolab/qti-components | GPL-3.0 |

**Wiring.** `edx-ora2` owns rubrics, submissions and staff grading — it already has the data
model and the UI. LangGraph sits beside it as an explicit graph: *draft score → confidence
check → below-threshold routes to human → human decision recorded → explanation attached to the
submission.* Model calls go through LiteLLM so the provider is auditable and swappable.
Label Studio builds the rubric-scored gold set from the institution's own historical marking;
Argilla is where teachers review and correct model output, and that correction stream is the
retraining signal. promptfoo gates every prompt change against the gold set so a regression
never reaches a learner.

**Where ArguLens goes in the graph.** Its three components are separately replaceable, which is
why it fits here rather than dictating the architecture. The **Qwen2.5-7B LoRA discourse
classifier** labels each sentence `claim`/`data`/`counterclaim`/`rebuttal` — that labelling is
itself the feedback artefact a student can argue with. The **LightGBM scorer** produces the
number, and because it reads 31 measured features it is **reproducible on re-run and inspectable
feature by feature**. The **feedback generator** (local Qwen2.5-14B-Instruct via vLLM) is the only
LLM in the scoring path, and it writes prose rather than deciding grades. Serve the classifier and
the generator through ArguLens's `vllm` backend mode; route the feedback model through LiteLLM via
its `api` backend so the provider stays auditable.

**Two work items that are not optional, priced into the 10–12 weeks.**
1. **Re-fit the scorer on the client's own graded corpus.** ArguLens ships trained on **Persuade
   2.0 — US middle-school argumentative essays**, and its README warns about training-data bias
   and generalisation. For a LATAM engagement this is decisive: **nothing in this system has been
   shown to transfer to Spanish or Portuguese.** Use Label Studio to build the local gold set
   from historical marking, then re-fit. Budget this as a work package, not a tuning step.
2. **Treat it as v0.1.0 software.** Adapter weights ship as a separate release asset and the
   README restricts the tool to "research and assistive" use. Hardening, packaging and an
   upgrade path are Globant's scope. Say so in the proposal — it is a credibility gain, and
   hardening a real Apache-2.0 base is a much cheaper proposition than greenfield.

**The critical design rule:** the model **proposes**, a human **disposes**, and the
disposition is logged with its explanation. That is simultaneously the LGPD Article 20
answer, the EU high-risk human-oversight answer, and the reason a faculty senate will approve
it. Architect it in from day one — it cannot be retrofitted.

**And it now has a third payoff, which is the strongest selling point in this file.** Vietnam's
**Decision 33/2026/QD-TTg** lists AI that conducts exams, assesses learning outcomes or ranks
learners as a high-risk education system — but reporting indicates the listings bite only where
**AI output is the sole basis for a decision without meaningful human review.** A genuine
human-disposition step therefore does not merely satisfy the high-risk obligations; it can keep
the system **out of the high-risk tier altogether**. The same architecture answers three
jurisdictions. (Vietnamese dates and the law's number are unresolved across secondary sources —
see `intel/market.md` gaps — so confirm against primary text before contracting.)

---

## P3 — Multi-agent course generation for a ministry or large programme

**Sell to:** APAC national programmes (the Accenture/Google benchmark), EMEA public sector,
LATAM ministries. **Effort: 6–8 weeks to a working pilot.**

| Layer | Component | Licence |
|---|---|---|
| Course generation | https://github.com/THU-MAIC/OpenMAIC | MIT |
| Courseware target | https://github.com/oppia/oppia | Apache-2.0 |
| Item UI | https://github.com/Khan/perseus | MIT |
| Source ingestion | https://github.com/datalab-to/marker | Apache-2.0 |
| Grounded drafting | https://github.com/stanford-oval/storm | MIT |
| Pedagogical QA | https://github.com/AI-for-Education/pedagogy-benchmark | MIT |

**Wiring.** marker converts the ministry's existing syllabus and textbook PDFs to clean
markdown. OpenMAIC generates the course — AI teacher plus AI classmate agents, project-based
milestones — and exports to PPTX and HTML; STORM drafts grounded explainer material with a
citation trail where the source corpus is thin. Rather than leaving the output in OpenMAIC,
port the validated lessons into **Oppia** explorations, because Oppia's misconception-specific
feedback model is what turns generated content into actual remediation, and it is Apache-2.0.
Render practice items with Perseus.

**The gate that makes this credible:** run `pedagogy-benchmark` against the model you intend
to use *before* generating a national curriculum with it, and publish the CDPK and SEND
scores in the proposal. Everything in this stack is permissive — the whole pattern can be
delivered as a commercial product.

---

## P4 — EU AI Act conformance retrofit (the 2027 clock)

**Sell to:** EMEA. **Effort: 4 weeks for the Article 50 slice; 12–14 weeks for high-risk
readiness.** This is time-boxed work with a date on it, which makes it an easy sale.

| Layer | Component | Licence |
|---|---|---|
| Policy orchestration | https://github.com/langchain-ai/langgraph | MIT |
| Gateway / audit log | https://github.com/BerriAI/litellm | MIT |
| Durable audit trail | https://github.com/temporalio/temporal | MIT |
| Evidence & red-teaming | https://github.com/promptfoo/promptfoo | MIT |
| Local inference (data residency) | https://github.com/ollama/ollama or https://github.com/vllm-project/vllm | MIT / Apache-2.0 |
| Human oversight UI | https://github.com/argilla-io/argilla | Apache-2.0 |

**Wiring, in the order the deadlines fall.**
1. **Already in force — audit and remove.** Article 5(1)(f) has banned emotion inference in
   education since 2 February 2025. Sweep the client's stack for engagement, attention or
   sentiment detection and remove it. This is a finding, not a feature.
2. **Live from 2 August 2026 — Article 50 disclosure.** Every learner-facing chatbot must
   declare it is AI. A LangGraph pre-node that injects and logs the disclosure, plus LiteLLM
   recording that it happened, closes this in weeks.
3. **2 December 2027 — high-risk readiness** for admissions, assessment and proctoring:
   logging, human oversight, accuracy documentation, data governance. Temporal gives a durable
   record of every automated decision and its inputs that survives restarts; Argilla is the
   human-oversight surface; promptfoo produces the accuracy and robustness evidence pack.

**Caveat to state to the client:** `eur-lex.europa.eu` is unreachable from this session, so
confirm Regulation (EU) 2026/1744's education timing against the primary text before signing
to a date.

---

## P5 — Offline-first tutoring for low-connectivity deployment

**Sell to:** LATAM (rural Brazil, Mexico, Andean region), APAC (rural India), ministry equity
programmes. **Effort: 6–8 weeks.** This is where LATAM is genuinely better served by a
different architecture rather than a cheaper version of the online one.

| Layer | Component | Licence |
|---|---|---|
| Learning platform | https://github.com/learningequality/kolibri | MIT |
| **Offline education server (lead)** 🟢 **new `p877`** | https://github.com/Crosstalk-Solutions/project-nomad | **Apache-2.0** |
| Offline server bundle (fallback) | https://github.com/iiab/iiab | LGPL |
| Offline corpus | https://github.com/kiwix/kiwix-tools | GPL-3.0 |
| Local model | https://github.com/ollama/ollama | MIT |
| Tutor | https://github.com/HKUDS/DeepTutor (ingests Kiwix archives natively) | Apache-2.0 |
| Retention scheduler | https://github.com/open-spaced-repetition/fsrs4anki | MIT |

**Wiring.** Internet-in-a-Box provides the turnkey school server on low-cost hardware; Kolibri
is the learner-facing platform with its own sync model for intermittent connectivity. Kiwix
ZIM archives supply the offline corpus — and **DeepTutor already ingests Kiwix archives**,
which is the connection that makes a genuinely offline tutor possible rather than a degraded
online one. Ollama runs a small quantised model locally. FSRS schedules review so that scarce
device time is spent on what the learner is about to forget.

🟢 **`p877` revision — lead with Project NOMAD, and the reason is the licence, not the features.**
NOMAD ships the whole offline appliance Internet-in-a-Box ships (content library, admin UI,
installer, Docker) **under Apache-2.0 instead of LGPL**, and bundles Wikipedia, books, courses,
maps **and optional local AI** in one deployable unit. For a ministry programme that is the
difference between a product you can **rebrand and redistribute as the ministry's own** and one
that carries copyleft obligations into the deliverable. **4,526 forks against 43,849 stars** is the
adoption evidence — on an appliance repo, forks are deployments.

**Revised wiring.** Project NOMAD is the school-site server and content plane. **Kolibri stays**
where the client needs its learner-progress and sync model, and **Kiwix ZIM archives stay in the
pipeline for one specific reason: DeepTutor ingests them natively**, which is what makes the tutor
genuinely offline rather than a degraded online one. Ollama runs a small quantised model on the
box; NOMAD's "optional local AI" slot is where it lands. FSRS schedules review so scarce device
time goes to what the learner is about to forget.

🟡 **Licence note to put in the statement of work:** NOMAD is Apache-2.0, but Kiwix (GPL-3.0) and
Kolibri (MIT) are separate components. **Keep them as separate processes exchanging files and HTTP
— do not statically link or vendor the GPL-3.0 pieces into a rebranded binary**, or the copyleft
you avoided by choosing NOMAD comes back at integration.

**Design constraint:** pick the model to fit the hardware first, then design the pedagogy
around its real latency. Everything syncs opportunistically when a link appears; nothing
blocks on the network.

---

## P6 — Institutional AI governance console

**Sell to:** everywhere — this is T3 turned into a product. **Effort: 8–10 weeks.**

Only ~a quarter of faculty report a formal institutional AI policy while ~8 in 10 students use
AI routinely. The gap is the product.

| Layer | Component | Licence |
|---|---|---|
| Gateway, budgets, per-user keys | https://github.com/BerriAI/litellm | MIT |
| Front door for staff & students | https://github.com/danny-avila/LibreChat | MIT |
| Policy graph per jurisdiction | https://github.com/langchain-ai/langgraph | MIT |
| Durable decision log | https://github.com/temporalio/temporal | MIT |
| Learning telemetry | https://github.com/openedx/openedx-aspects | Apache-2.0 |
| Safety regression | https://github.com/promptfoo/promptfoo | MIT |

**Wiring.** LibreChat is the sanctioned front door — self-hosted, multi-model, per-user auth —
which is what converts shadow AI use into governed use. All traffic goes through LiteLLM for
per-department budgets, rate limits and a complete call log. LangGraph holds the policy as
code with jurisdiction-specific nodes: FERPA redaction for North America, Article 50
disclosure for EMEA, content labelling for China, LGPD review rights for Brazil. Temporal
keeps the decision log durable; Aspects reports usage against learning outcomes; promptfoo
runs safeguarding checks on every policy change.

**Why LibreChat and not Open WebUI:** verified this pass, Open WebUI's licence clause 4
prohibits removing its branding above **50 end users per rolling 30 days** without an
enterprise licence. A white-labelled campus deployment would be a material breach. LibreChat
is plain MIT. This is exactly the kind of detail that only reading the licence bytes catches.

---

## P7 — Outcome-validated tutoring deployment (the pattern that survives the evidence)

**Sell to:** every region, and especially any public institution with an access mandate.
**Effort: 12–16 weeks including a measurement window.**

**This pattern exists because of a finding, not a technology.** A 2026 RCT across **2,379
undergraduates** found that access to a course-integrated GenAI tutor **reduced final grades by
0.37 SD** and LMS participation by **0.90 SD**, with **larger losses among first-generation
students**. A separate RCT found AI tutoring **combined with structured group work** produced the
largest gains of any arm. See `intel/trends.md` **T9**.

The conclusion is not "don't deploy tutors". It is that **deploy-and-measure-usage is the arm that
lost**, and it is the default motion of the entire industry. This pattern sells the arm that won.

| Layer | Component | Licence |
|---|---|---|
| Tutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 |
| Pedagogical policy as code | https://github.com/langchain-ai/langgraph | MIT |
| Model gateway | https://github.com/BerriAI/litellm | MIT |
| LMS attachment | https://github.com/Cvmcosta/ltijs | Apache-2.0 (`master`) |
| Interaction telemetry | https://github.com/yetanalytics/lrsql | **Apache-2.0** |
| Outcome analytics | https://github.com/openedx/openedx-aspects | Apache-2.0 |
| Model pedagogical capability | https://github.com/AI-for-Education/pedagogy-benchmark | MIT |
| Safeguarding gates | https://github.com/promptfoo/promptfoo | MIT |

**Wiring — and the three design decisions that distinguish it.**

1. **Build the measurement before the tutor.** `ltijs` launches the tutor inside the client's
   Moodle/Canvas/Open edX so **section-level assignment is possible** — which is what makes a
   real comparison design available instead of a satisfaction survey. **`lrsql`** captures
   every interaction as xAPI; Aspects joins it to grades and participation. Stand this up first,
   on the existing course, to get a **baseline**. Without a baseline the 0.37 SD effect is
   undetectable, and a client who cannot detect it is exposed to it.
2. **Encode the pedagogy as refusal, not availability.** The negative trial's mechanism was
   participation collapse — an always-available answer source substituting for effortful work.
   So LangGraph holds an explicit policy graph that **withholds**: hint ladders before answers,
   mastery gates before progression, attempt requirements before explanation, and escalation to a
   human teacher rather than an easier answer. DeepTutor's mastery tracking and learning paths
   supply the state these nodes read. A tutor that will not simply answer is the product.
3. **Pair it with structured human interaction.** The winning arm combined AI with group work.
   So the deliverable includes the **course design** — mandatory structured peer sessions, AI
   use integrated into them rather than offered alongside them. This is instructional-design
   scope, and it is the part a product vendor cannot sell.

**Instrument the equity question explicitly.** Disaggregate outcomes by first-generation status
and any other access category the institution tracks, from the baseline onward. The published
harm was concentrated there; a bid that raises this proactively, with a monitoring plan, wins
against competitors who have not read the literature.

**What the client buys:** not a tutor, but **evidence about their own students** — plus the
tutor. `pedagogy-benchmark` supports the model-selection claim; the trial design supports the
outcome claim. Nobody in this market is selling the second one.

---

## P8 — Vietnam / APAC high-risk de-escalation audit

**Sell to:** APAC, Vietnam first, then South Korea ahead of real enforcement.
**Effort: 4–6 weeks for the audit, then per-system remediation.**

**Vietnam has handed services firms a specification.** Decision **33/2026/QD-TTg** names **46
high-risk AI systems across six sectors**, and **education is one of them** — covering AI that
**conducts examinations, assesses learning outcomes or ranks learners**, and AI that **monitors
and analyses learner behaviour using biometric data or other automated monitoring mechanisms**.

**The leverage:** reporting indicates many listings apply only where **AI output is the sole
basis for a decision without meaningful human review**. So for each system there are two paths —
**de-escalate** it out of the tier by inserting genuine human review, or **conform** and carry the
full obligations. Deciding which, per system, is the engagement.

| Layer | Component | Licence |
|---|---|---|
| System inventory & decision log | https://github.com/temporalio/temporal | MIT |
| Policy-as-code, per jurisdiction | https://github.com/langchain-ai/langgraph | MIT |
| Human-review workflow | https://github.com/openedx/edx-ora2 | AGPL-3.0 |
| Reviewer interface | https://github.com/argilla-io/argilla | Apache-2.0 |
| Explicable scoring (replaces LLM scoring) | https://github.com/wwrwbs/AI_AWE | Apache-2.0 |
| Gateway & call audit | https://github.com/BerriAI/litellm | MIT |
| Evidence & reporting | https://github.com/openedx/openedx-aspects | Apache-2.0 |

**Wiring.** Inventory every education AI system against the three listed education categories.
For each, decide de-escalate or conform. De-escalation is concrete engineering, not paperwork:
route the decision through `edx-ora2`'s human workflow with Argilla as the reviewer surface,
replace LLM scoring with ArguLens's feature-based scorer so the human reviewer has something
inspectable to review, and record every disposition durably in Temporal so "meaningful human
review" is **evidenced** rather than asserted. LangGraph carries the per-jurisdiction policy
nodes, which is what lets the same platform serve Vietnam, Korea, the EU and Brazil — the
human-review requirement is substantially the same shape in all four.

**Biometric monitoring is the one to advise against, not remediate.** Vietnam lists it, and the
EU has **banned emotion inference in education outright since 2 February 2025** (AI Act Art.
5(1)(f)). There is no de-escalation path for a prohibited practice. Recommend removal.

**Pair it with the curriculum mandate.** **MOET Decision 2422** (with Decision 5588) requires
**12 periods per class per year of AI content for grades 1–12** — a nationwide courseware and
teacher-training demand signal, and a second, separately-funded engagement off the same client
relationship. `microsoft/ai-agents-for-beginners` (MIT) and `huggingface/agents-course`
(Apache-2.0) are white-labellable bases for the teacher-facing material.

**Caveat to carry into any proposal:** Vietnam's AI Law number (134/2025/QH15 vs 91/2025/QH15)
and its compliance dates (1 Mar 2027 / 1 Sep 2027 vs 1 Jul 2027 / 1 Jul 2029) **conflict across
secondary law-firm sources**, and this session could read none of the primary texts. Scope a
local-counsel check as the first task of the engagement.

---

## P9 — Spanish-language sovereign tutor on a LATAM-origin base

**Sell to:** LATAM ministries, public universities, rural and regional higher-education
programmes — and any client for whom *"built in the region"* is part of the evaluation.
**Effort: 8–10 weeks** to a pilot, of which **3–4 weeks is completing someone else's backend**.
New in `p873`, and it is the first pattern in this file whose core component is LATAM-origin.

🟢 **`p878` repair — this pattern was built on a 0-star repository because the KB could not see the
alternatives.** P9 chose `LabSirius/TutorIA` (MIT, **0 ★**) as its LATAM-origin core, and the
reasoning was sound given what was known: it was the only LATAM-origin education repository in the
index. 🔴 **That was an artefact of searching only in English.** `p878` ran twelve discovery legs in
Spanish and Portuguese and found **304 repositories**, so the LATAM supply picture this pattern was
designed against was wrong. **Two substitutions are now available, and they change the shape of the
engagement:**

| Instead of | Consider | Why |
|---|---|---|
| `openedx/openedx-platform` (AGPL-3.0; 🟢 `p879` corrected slug) as the records/LMS layer, in **Brazil** | **https://github.com/portabilis/i-educar** (🔴 GPL-2.0, **726 ★**, created 2013, CI, tagged releases) **as an integration target, not a base** | It is **the incumbent** in Brazilian municipal education. A pattern that ignores the incumbent and proposes a parallel system loses on procurement, not on technology. Keep the AI layer a separate service and the copyleft boundary holds. |
| `Gego-K12/gegok12` (MIT, 57 ★) where a permissive SIS is needed | **https://github.com/Antonio-Neves/Gestao-Escolar** (**MIT**, 50 ★, bilingual PT/EN, pushed 2026-10-12) | Comparable size and licence, but **LATAM-origin and already bilingual** — which is the specific thing this pattern is selling. |

🟡 **`TutorIA` remains the right core for a Spanish-language public-sector tutor** — the substitutions
above are for the records and LMS layers, not the tutor. But **the "only LATAM-origin option"
justification is retired**: it was never true, and this pattern should now be argued on fit rather
than on scarcity. 🔵 **And the LATAM shelf is almost certainly still under-counted** — `p878` ran
twelve legs, not a systematic sweep, and ran none in indigenous or regional languages.

| Layer | Component | Licence |
|---|---|---|
| Tutor backend (base) | https://github.com/LabSirius/TutorIA — **clone `feature/refactor-to-v2-requirements`, NOT `main`** | MIT |
| LMS | https://github.com/openedx/openedx-platform | AGPL-3.0 |
| LTI launch (the piece to add) | https://github.com/Cvmcosta/ltijs | Apache-2.0 |
| Local inference | https://github.com/ollama/ollama | MIT |
| Model-swap seam | https://github.com/BerriAI/litellm | MIT |
| Vector store | PostgreSQL + `pgvector` (already wired in TutorIA's `docker-compose.yml`) | PostgreSQL licence / Apache-2.0 |
| Document ingestion | https://github.com/docling-project/docling | MIT |
| Telemetry for outcome measurement | https://github.com/openfun/ralph | **MIT** (Open edX-native; TutorIA runs inside Open edX) |
| Offline variant | https://github.com/learningequality/kolibri | MIT |

**Why start from TutorIA rather than DeepTutor.** DeepTutor is far more mature and should still be
the default for most builds (see **P1**). Choose TutorIA when the engagement is **Spanish-language,
public-sector and regional**, because three things come with it that maturity cannot buy: a
Colombian public university and a **Minciencias**-funded provenance, a **named pedagogical
director** and teacher-training framework, and a design brief that is already *rural higher
education* rather than a generic tutor localised afterwards. In a ministry evaluation that
provenance is worth more than feature count.

**Wiring, in the order that de-risks fastest.**

1. **Clone the right branch.** `git clone -b feature/refactor-to-v2-requirements
   https://github.com/LabSirius/TutorIA`. **`main` contains documentation only**, and the
   `Sof1SP/tutorIA` address in the README has no code in any branch. Budget a day to confirm what
   you actually have before promising anything.
2. **Stand up the backend as-is.** `docker-compose.yml` brings up `pgvector/pgvector:pg16` plus
   Ollama with an init container. Pull `nomic-embed-text` (**768-dim, matched to
   `content_chunks.embedding`** — a different embedding model means a migration, not a config
   change). Set **`require_embedding_model: true`** in production so a misconfigured RAG stack
   fails at boot instead of silently degrading. Run Alembic; ignore the `create_all` bootstrap the
   code's own `TODO(tech-debt)` tells you to delete.
3. **Seed the pedagogy, don't hard-code it.** Prompt templates live in the database (**RF-21**,
   `python -m app.db.seed prompts`). This is where the client's pedagogical framework — and
   **P7**'s scaffolding, hint ladders and mastery gates — is expressed. Treat it as the main
   configuration surface, co-authored with the client's academics.
4. **Build the three things that are missing.** This is the honest bulk of the work: **(a)** a
   learner-facing frontend — or skip it entirely and go straight to step 5, which is usually
   better; **(b)** a real **LTI 1.3 launch** via `ltijs`, because TutorIA's existing Open edX
   integration is a **data-sync gateway (RF-22) on APScheduler, not a launchable tool**; **(c)** a
   test suite — `pytest` and `pytest-asyncio` are already declared in `requirements.txt` and there
   are no tests.
5. **Prefer LTI-in-platform over a bespoke UI.** It is less work, and it inherits the platform's
   accessibility conformance — see **P10**.
6. **Keep the model seam.** TutorIA defaults to local Ollama (`llama3.2`) through an
   OpenAI-compatible client with a `request_router` (**RF-23**). Put **LiteLLM** behind that seam
   so the same deployment can move to a bigger local model, to **Latam-GPT** weights, or to a
   hosted endpoint on one config change — which is exactly the clause ministries ask for.
7. **Instrument from day one.** **Ralph** captures xAPI so **P7**'s measurement plan has
   data — and for this pattern specifically it is the right LRS rather than merely an available
   one: TutorIA is built to run inside **Open edX**, and `ralph` ships **Open edX tracking-log →
   xAPI converters in-tree** (`src/ralph/models/edx/converters/`), so the mapping work is already
   done. It is **MIT**, and it comes from **France Université Numérique**, a public university
   consortium — provenance that reads well to a ministry. Do not skip this: the region's measured governance gap is that **9% of institutions
   evaluate their AI implementation at all**, which makes measurement the differentiator.

**Say this plainly to the client, because it converts a risk into a selling point.** TutorIA is an
early-stage backend, not a product; the work is completing a funded public-university project, and
the frontend, LTI plugin and tests are **specified by its own README and absent from its code**.
Contributing those upstream under MIT is a visible, creditable contribution to a national research
programme — a materially better story than a private fork, and one a public client can cite in its
own reporting.

**Licence note.** TutorIA is MIT, so there is no copyleft constraint on your additions. Open edX
is **AGPL-3.0**: integrate over **LTI** rather than forking `edx-platform`, and the obligation
stays on the platform side of the boundary.

---

## P10 — Accessibility-gated public-sector bid

**Sell to:** any public-sector or publicly funded buyer — US federal and state (**Section 508**),
EU and UK public bodies (**EN 301 549**, **European Accessibility Act**, in force since
**28 June 2025**), and any university procurement with a VPAT requirement. **Effort: 4–6 weeks**
as a workstream attached to another pattern, not a standalone build. New in `p873`.

**The problem this pattern exists to solve.** Across this KB's entire agent inventory, **exactly
one education-native agent publishes an accessibility conformance statement**:
`CAHLR/OATutor`. If conformance gates the procurement, a bespoke agent UI means commissioning an
audit and remediating an unknown quantity of findings — on your own budget, before you can bid.

| Layer | Component | Licence | Role in the conformance story |
|---|---|---|---|
| Conformant host UI | https://github.com/moodle/moodle | GPL-3.0 | Moodle core and mobile are **stated** to be WCAG 2.2 AA certified. **Request the VPAT/ACR** — this is a vendor claim this session could not verify |
| Launch mechanism | https://github.com/Cvmcosta/ltijs | Apache-2.0 | LTI 1.3 launch with grade passback; the agent runs as a tool *inside* the conformant UI |
| Agent with its own statement | https://github.com/CAHLR/OATutor | MIT | The fallback when the agent itself must carry conformance: Section 508 / WCAG documented, React, static-deployable |
| Accessible assessment rendering | https://github.com/Citolab/qti-components | GPL-3.0 | QTI 3 standards-compliant item rendering |
| Open-response workflow | https://github.com/openedx/edx-ora2 | AGPL-3.0 | Human-reviewed assessment rather than proctoring (see **P2**, **T8**) |
| Content conversion | https://github.com/docling-project/docling | MIT | Structured extraction — the input side of making generated content accessible |

**Wiring, and the order matters.**

1. **Decide where conformance lives before writing any UI.** Two viable answers: the agent runs
   **inside a platform that already holds a statement** (cheapest, and the default recommendation),
   or you adopt **OATutor**, the one agent carrying its own. A bespoke front end is the third
   answer and it is the expensive one.
2. **Launch over LTI 1.3 with `ltijs`.** Keep every learner-facing surface inside the platform's
   chrome. Use custom UI only for staff-facing surfaces, where the procurement bar is lower.
3. **Treat generated content as in-scope — this is the step everyone skips.** An accessible
   platform routinely serves inaccessible embedded content: the SCORM package, the PDF workbook,
   the generated slide deck. **Anything the agent emits inherits the obligation.** So constrain
   generation: alt text required for every generated image, heading structure enforced in generated
   documents, no colour-only encoding in generated charts, captions and transcripts for any
   narrated output, and reading order asserted in exported PDFs. Make these **template and
   prompt-level constraints** (in P9 that means the seeded prompt templates) and then test the
   output, not the prompt.
4. **Add the WCAG 2.2 criteria that specifically bite learning products**: target size, dragging
   movements, consistent help, accessible authentication — the last one matters because login
   puzzles and cognitive tests are common in exam flows and are now explicitly in scope.
5. **Automate what automation can catch, then stop pretending it is enough.** Wire `axe-core` into
   CI for regressions, and budget a **manual audit with assistive-technology users** for the claim
   itself. Automated tooling catches a minority of real failures; a conformance statement built
   only on it will not survive scrutiny.
6. **Produce the artifact the buyer actually asked for:** a VPAT/ACR covering the deployed
   configuration, with known limitations stated. A statement with honest exceptions wins bids;
   an overclaim fails an audit later, which is worse than losing.

**The regulatory clock, secondary-sourced** (all EU primary sources are unreachable from this
session): the **European Accessibility Act** has applied since **28 June 2025**, and the next
**EN 301 549** revision aligning it to **WCAG 2.2 AA** is reported as due in the Official Journal
in **late 2026**. Treat WCAG 2.2 AA as the target now, not 2.1.

**Pair with:** **P4** in EMEA (the same buyer, the same conformance documentation habit, the same
2027 clock) and **P9** in LATAM, where launching inside Moodle or Open edX removes the frontend
TutorIA does not have — a conformance requirement and a missing UI cancelling each other out.

---

## P11 — EU AI-literacy duty conformance pack (the clock that is already running)

**Sell to:** EMEA — EU schools, school networks, ministries and universities as **deployers**.
**Effort: 6–8 weeks.** **New in `p874`.**

**Why this exists as a separate pattern from P4.** P4 sells against the EU AI Act's education
high-risk tier, which the Digital Omnibus deferred to **2 December 2027**. This one sells against a
duty that **is already binding**: the AI Act's **AI-literacy obligation on deployers**, reported as
applying to institutions from **July 2026**. P4 is a 2027 budget line. **P11 is a 2026 one**, aimed
at the same buyer, producing the same documentation habit, and it is the natural on-ramp to P4.

**The three things that make it closeable** — all newly established in `p874`:

| Element | Value | Use in the pitch |
|---|---|---|
| Measured deficit, **one population, one instrument** | **79%** of European secondary students use AI for schoolwork; **47%** were ever shown how — a **32-point gap**. OpenAI/ThinkYoung, 5,000 students aged 13–19, 10 European countries, fieldwork Apr–May 2026 | The business case. Not a vendor projection — a measurement on the buyer's own population |
| Teacher-side corroboration | **73%** of teachers use AI for planning and materials, **67%** for tests and rubrics (European School Education Platform, Apr 2026) | Staff are already in scope; this is not a future risk |
| **Delivery standard** | **EC/OECD AILit Framework**, 18 June 2026 — **4 dimensions**, **19 competences**, learner expectations, classroom scenarios. Non-binding, product-neutral, developed with CodeAI, feeds **PISA 2029** | The spine. Converts "support AI literacy" into 19 auditable line items |

### Stack — fully permissive, every licence byte-read

| Layer | Component | Licence |
|---|---|---|
| Competence spine | **EC/OECD AILit Framework** — 19 competences, 4 dimensions | Non-binding public framework (not code) |
| LMS launch / transport | https://github.com/Cvmcosta/ltijs — **LTI 1.3 / Advantage**, branch `master` | Apache-2.0 |
| Assessment + feedback core | https://github.com/moocupv/lti-ai-grader — LLM grading, configurable prompts, multi-language templates, Open edX- and Moodle-tested | Apache-2.0 |
| Model vetting evidence | https://github.com/AI-for-Education/pedagogy-benchmark — 1,143 teacher-qualification-exam questions (CDPK 920 / SEND 223) | MIT |
| Telemetry (xAPI/analytics) | https://github.com/openedx/openedx-aspects — reusable outside Open edX | Apache-2.0 |
| **Evidence store** (the attestation record) | 🟢 **This KB's own built component: `compose/code/p292-decision-evidence-store/`** — append-only, tamper-evident, offline, **106 passing controls** | Globant-built |
| Governance register | The institutional console from **P6** | — |

### How to wire it — and the one engineering task that is not optional

1. **Map the 19 AILit competences to the institution's existing curriculum and staff-development
   plan.** Output is a matrix: competence → where it is taught → who is accountable → what evidence
   exists. **This artifact *is* the deliverable** that discharges the literacy duty; the software
   only feeds it.
2. 🔴 **Swap `lti-ai-grader`'s transport. This is the pattern's critical path.** It ships **LTI
   1.1**, which signs with **OAuth 1.0a** and is the **deprecated** generation — 1EdTech has been
   retiring it and many institutions disable it outright. Keep its genuinely reusable parts (the
   grading core, prompt configuration, multi-language templates, and the LMS-tested grade round
   trip); **replace the LTI 1.1 receiver with `ltijs`** for a 1.3/Advantage launch with **AGS**
   grade passback, NRPS rosters and Deep Linking. Budget **1.5–2 weeks**. 🔴 **Do not deliver an
   OAuth 1.0a transport into an engagement that extends past 2027** — the high-risk tier brings
   logging and traceability duties you would then be defending on deprecated plumbing.
3. **Deliver the literacy assessment and formative feedback *inside the LMS*** via the 1.3 launch,
   so students and staff meet it in Moodle, Canvas, Open edX, Blackboard or D2L rather than in a
   new tool nobody adopts. This is also what keeps the build copyleft-safe: you attach over LTI
   rather than forking Moodle (GPL-3.0) or Open edX (AGPL-3.0).
4. **Separate telemetry from attestation — they are two components and conflating them is how a
   literacy claim stops being defensible.**
   - **Telemetry:** completion and interaction events as **xAPI into Aspects**. High-volume,
     mutable, analytical. This is the same spine **P7** needs for outcome measurement — build it
     once.
   - 🟢 **Attestation: the append-only decision record, already built in this KB at
     `compose/code/p292-decision-evidence-store/`** (106 offline controls, tamper-evident, no
     network). A literacy duty is discharged by showing **who was trained on which of the 19
     competences, when, on whose decision, and on what evidence** — that is a *decision record*,
     not an event stream, and a regulator asking the question a year later needs a record that
     cannot have been quietly rewritten. 🔵 **Reuse, do not rebuild:** `p291` costed this component
     as *"the one item a client would pay for"* and it is the second recipe family in this file to
     terminate in it. Run `python3 test_decision_store.py` before shipping.
5. **Run `pedagogy-benchmark` against whichever model backs the tool** and put the score in the
   conformance pack. It is the only published instrument that lets an institution say *why* this
   model is pedagogically fit, and the **SEND** split (223 questions on special educational needs
   and disabilities) answers the access question a public buyer will ask.
6. **Register the deployment in the P6 governance console** — deployer obligations, the literacy
   matrix, the model-vetting score, the incident route — so the 2027 P4 conformance work is an
   extension rather than a restart.

### Why Globant wins this one

The hyperscalers hold the **ministry model contracts** — OpenAI's education partnerships run
through **Estonia** (*AI Leap*, ChatGPT access bundled with teacher training), **Slovakia**,
**Greece** (a May 2026 framework requiring teacher oversight and data protection) and **Italy**, a
deliberately government-first, country-level strategy. **That is precisely why the literacy,
governance and conformance layer is open:** it must be **independent of the model vendor** to be
credible to a regulator, it is **services-shaped** so it cannot be bought as a product, and it is
**product-neutral by design** because AILit itself endorses no products. A competitor reselling a
model contract cannot also be the party certifying that the deployment discharges the buyer's legal
duty.

🔴 **Scoping honesty, to be said in the room.** The **July 2026** start date for the literacy duty
is **secondary-sourced** — no EU primary text is reachable from this KB's session (`eur-lex`,
Council and Parliament hosts are all refused), and **the enforcement mechanics against a school are
unverified and may be weak**. So **do not pitch a sanction on a date.** Pitch the **measured
32-point gap** and the **published framework**, with the legal duty as context. The engagement is
justified by the measurement whether or not a penalty ever materialises — and that is a stronger
position than a compliance threat that a client's own counsel may deflate.

---

## P12 — Hardened multi-agent classroom on OpenMAIC (the one with real adoption)

**Sell to:** APAC national-curriculum programmes, EMEA and LATAM universities needing generated
course material at scale. **Effort: 6–8 weeks.** **New in `p875`.**

**Why this pattern exists.** `p875` measured the shelf (**T12**): **two** open-source education
platforms have real user communities, and OpenMAIC (**43,808 stars, MIT, pushed today**) is the
one built for *course generation* rather than one-to-one tutoring. **Its licence is now settled
beyond argument** — the project relicensed to MIT on **2026-06-28**, which is why its own site and
every pre-July listicle still say AGPL-3.0, and why a pre-relicence AGPL fork (`kolbyzhu5/OpenMAIC`)
circulates in search results. Four channels agree on MIT. **Commercial use is permitted free of
charge by the README's own words.**

| Layer | Component | Licence |
|---|---|---|
| Classroom generation | https://github.com/THU-MAIC/OpenMAIC | **MIT** |
| LMS transport | https://github.com/Cvmcosta/ltijs (LTI 1.3 + AGS passback) | Apache-2.0 |
| Model serving | https://github.com/ollama/ollama → https://github.com/vllm-project/vllm | MIT / Apache-2.0 |
| Model gateway | https://github.com/BerriAI/litellm | MIT (⚠ SPDX `NOASSERTION`) |
| Curriculum spine (optional) | https://github.com/withmarbleapp/os-taxonomy | 🔴 **ODbL-1.0 — database share-alike** |
| Ingestion | https://github.com/docling-project/docling | MIT |

### 🔴 The hardening task that makes this a pattern rather than a demo

OpenMAIC's own README states that site-wide access is gated by a single `ACCESS_CODE` variable and
that **unset is the default in `.env.example`**:

> *"When it is unset… `middleware.ts` checks no credential and every route, the API included, is
> reachable: an unconfigured deployment is not gated, and there is no second enforcement point."*

**A default OpenMAIC deployment in a school tenancy is a student-data exposure on day one.** Rate
limiting only engages behind a trusted proxy with `TRUST_PROXY_HEADERS=true`. Budget these as named
line items, not as "hardening":

1. **Provision `ACCESS_CODE`** from a secret manager; fail the deploy if unset (CI gate, not a
   runbook note).
2. **Add the second enforcement point OpenMAIC does not have** — put `ltijs` in front so the only
   path in is an authenticated **LTI 1.3 launch from the institution's LMS**, and bind the app to
   a private network so the API is not routable from the public internet.
3. **Set `TRUST_PROXY_HEADERS=true` behind the institution's reverse proxy** so rate limiting is
   actually active.
4. **Pen-test the API surface specifically**, not just the UI — the README is explicit that the API
   shares the single gate.

🔵 **Why this sells.** Every competitor demoing OpenMAIC is demoing the default configuration. **An
engagement that opens by naming this defect, with the vendor's own README as the citation, is
immediately credible** — and the fix is four tasks, not a rebuild.

🟡 **Scope honestly:** if the client plans to publish an extended curriculum database derived from
`os-taxonomy`, the **ODbL share-alike obligation attaches to that database**. Either keep
client-specific curriculum in a separate store you do not redistribute, or budget the obligation.
It is not an MIT-class component and must not be presented as one.

---

## P13 — US district AI-policy conformance, sold against a published calendar

**Sell to:** North America K-12 districts and state education agencies. **Effort: 4–6 weeks per
district, 10–12 weeks for a state model policy.** **New in `p875`.**

**Why this pattern exists.** `p875` found that the US state layer has moved from advisory guidance
to **dated mandates** (`intel/market.md`, North America). That converts an open-ended "AI strategy"
conversation into a procurement calendar with named deadlines:

| Jurisdiction | Obligation | Date |
|---|---|---|
| **Ohio** | District AI policy required | **1 Jul 2026 — already passed** |
| **North Carolina** | State model policy | **31 Dec 2026** |
| **North Carolina** | Local district policies | **30 Jun 2027** |
| **North Carolina** | Teacher training | **30 Jun 2028** |
| **Maryland** | 24 districts adopt aligned policy | **120 days** from state guidance |
| **Idaho** | Local boards set policy | **before the 2027–28 school year** |

🔵 **Ohio's passed deadline is the warmest lead in this file.** A cohort of districts is either in
breach or has adopted school-boards-association template language nobody has mapped to their actual
deployed tools. **The first deliverable is an inventory, and almost nobody has one.**

**The build.** This is a governance engagement with a small software spine — reuse **P6**'s console:

| Layer | Component | Licence |
|---|---|---|
| Governance console / inventory register | **P6** stack — https://github.com/appsmithorg/appsmith | Apache-2.0 |
| Policy-to-tool mapping store | https://github.com/qdrant/qdrant | Apache-2.0 |
| Data-boundary enforcement for any AI in scope | https://github.com/BerriAI/litellm (self-hosted gateway, logging off by default) | MIT |
| Evidence of student-data handling | district SIS + https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS | Apache-2.0 |

**Deliverables, in the order a district needs them:** (1) inventory of every AI tool actually in
use, including the ones teachers adopted without procurement; (2) mapping of each to the state's
required policy clauses; (3) a data-boundary architecture showing where student records go;
(4) board-ready policy text; (5) the teacher-training plan the 2028 clause will require.

### 🔴 Sell this in BOTH directions or lose half the market

The regulatory current is not uniformly pro-adoption. **New York** has a proposal to limit
classroom AI below ninth grade; **California AB 1159** bars using student data to train AI models;
**New Mexico** let districts opt out of a state-mandated AI reading tool after privacy backlash.
🟡 **Restriction compliance is the same engagement with the same artifacts** — inventory, mapping,
data boundaries, board text. **A North America offer that only works if the client is expanding AI
use will be unsellable in a growing list of states.** Pitch it as *"know what you are running and
prove it meets your state's rule"*, which is true whichever way the rule points.

🟡 **Source caveat to carry internally:** the state counts (~33–35 states with guidance; 134 bills
across 31 states) come from trackers, several vendor- or advocacy-run, that disagree at the
margins. **The dates above recur consistently across sources; the counts are directional. No
primary statute was readable from this session** — confirm the specific statute before a district
signs.

---

## P14 — The measurement spine (the piece every other pattern assumes and none of them built)

**New in `p876`.** Every outcome claim in this file — P1's "efficacy can be measured instead of
asserted", P7's baseline-and-comparison design, P9's answer to the region's 9%-evaluate statistic
— depends on learner telemetry reaching somewhere durable and queryable. Until this pass that
"somewhere" was a GPL project whose last commit was **2021-11-16**. P14 is that spine, built
once, reused by the rest.

**Sell it on its own.** `intel/market.md` records that **26% of LATAM universities have a formal
AI strategy and 9% evaluate how it performs**, and `intel/trends.md` **T9** records that the
largest trial of an AI tutor to date returned a **negative** effect. Those two facts together are
the pitch: **an institution that cannot measure cannot tell P7 from the negative trial**, and the
cheapest engagement that de-risks every later AI purchase is the instrumentation, not the tutor.
It is also unusually easy to scope — no pedagogy debate, no model selection, no procurement of a
learner-facing system.

### Stack — fully permissive, every licence byte-read this pass

| Layer | Repo | Licence | Note |
|---|---|---|---|
| Learning Record Store (default) | https://github.com/yetanalytics/lrsql | **Apache-2.0** | SQLite for pilot → Postgres 14–18 in production. OIDC. 67 commits in 12 months |
| LRS (Open edX / EU public sector) | https://github.com/openfun/ralph | **MIT** | FastAPI LRS + CLI + library; **Open edX tracking-log converters in-tree**; Helm chart |
| Conformance reference | https://github.com/adlnet/ADL_LRS | **Apache-2.0** | From xAPI's authors. Test against it; do not run it (0 commits/12mo) |
| Statement source — LMS | https://github.com/davidpesce/moodle-logstore_xapi | GPL-3.0 | Moodle → LRS bridge. Copyleft, but it is a **plugin inside a GPL platform**, so nothing new is conceded |
| Statement source — agent | `ltijs` launch + the tutor's own emitter | Apache-2.0 | Your code; emit xAPI directly |
| Analytics / joins | https://github.com/openedx/openedx-aspects | Apache-2.0 | Joins telemetry to grades and participation; reusable outside Open edX |
| Reporting UI | Superset (via Aspects) **or** Grafana over the LRS Postgres | Apache-2.0 / AGPL-3.0 | 🔴 **Not optional and not free — see below** |

### 🔴 The line item that must not be silently dropped

Learning Locker bundled dashboards. **Neither replacement does.** If a statement of work says
"measurement" and the stack is `lrsql` + Aspects, somebody still has to build the reports the
client will actually look at. Budget it explicitly. 🟡 Note the licence asymmetry while choosing:
**Superset is Apache-2.0, Grafana is AGPL-3.0** — fine for a self-hosted institutional
deployment, a problem the moment the dashboards become part of a distributed product.

### How to wire it

1. **Stand up `lrsql` against the institution's existing Postgres.** Point its OIDC at the same
   identity provider the LMS uses, so there is no second user directory to govern. For a pilot,
   the embedded SQLite build runs on one box.
2. **Turn on statement sources before anything AI exists.** `logstore_xapi` from Moodle (or
   `ralph`'s converters from Open edX tracking logs) gives a **pre-AI baseline from history the
   institution already has**. This is the step that makes P7's comparison design possible later,
   and it is nearly free — the data exists, it is just not flowing anywhere.
3. **Define the statement vocabulary before the first agent emits one.** Agree verbs and activity
   types up front; retrofitting a vocabulary across a year of statements is the expensive mistake
   in every xAPI project.
4. **Join to outcomes with Aspects**, then build the reports in Superset or Grafana.
5. **Only then add the agent** (P1, P7, P9). It emits into a spine that already has a baseline.

### Why Globant wins this one

It is permissive end to end, so there is no licence conversation to lose. It is **the cheapest
credible first engagement** with an institution that is not yet ready to buy a tutor, and it
**creates the evidence base that justifies the next purchase** — which makes it a land-and-expand
motion rather than a one-off. And it is defensible under every regime in `intel/market.md`: the
EU AI Act's high-risk tier, Brazil's LGPD review right and Vietnam's Decision 33/2026/QD-TTg all
ask for records of how an automated system behaved. **An LRS is that record.**

**Effort:** 4–6 weeks for the spine and a baseline on one faculty; 8–10 weeks institution-wide
with reporting. *Studio-delivery estimate, not a measurement.*

---

## P15 — Consent, opt-out and "not the primary basis": the spine US state law now requires — new in `p877`

**Sell to:** North America (Alabama first, then every state that copies it), and reusable wherever
a parental-rights or learner-consent regime appears. **Effort: 4–6 weeks** on top of an existing
deployment; **1–2 weeks** if retrofitted before an LRS goes in, which is the whole point.

**Why now.** Alabama **H.B. 1227** does two things no education AI stack is built for: it bars AI
from being **the primary basis for grading, discipline or placement**, and it gives parents an
**opt-out from student-facing AI tools**. California **AB 1159** adds a third: **student data may
not be used to train AI models**. 🔴 **These are architecture requirements, not policy documents.**
An opt-out that must reach every agent, every log line and every telemetry record cannot be bolted
on after a Learning Record Store is populated — by then the records exist.

| Layer | Component | Licence |
|---|---|---|
| Consent store (source of truth) | https://github.com/Gego-K12/gegok12 (SIS holds the per-student flag) | **MIT** |
| Policy gate in the agent graph | https://github.com/langchain-ai/langgraph | MIT |
| Model routing + **no-train enforcement** | https://github.com/BerriAI/litellm | MIT |
| Local inference (the AB 1159 answer) | https://github.com/ollama/ollama · https://github.com/vllm-project/vllm | MIT · Apache-2.0 |
| Telemetry with consent attached | https://github.com/yetanalytics/lrsql | Apache-2.0 |
| Human-review trail | https://github.com/openedx/edx-ora2 | AGPL-3.0 (self-hosted) |
| Review-queue UI | https://github.com/HumanSignal/label-studio | Apache-2.0 |
| Regression tests on the gate | https://github.com/promptfoo/promptfoo | MIT |

**Wiring.**

1. **The consent flag lives in the SIS, not in the AI stack.** `gegok12` (MIT, API-first) holds
   `ai_opt_out` per student; being permissive, you can add the field and ship the result. Every
   other component reads it over the API — one source of truth, auditable, and it survives you
   replacing the tutor.
2. **LangGraph makes the gate a node, not a prompt.** A `consent_check` node runs before any
   learner-facing generation and returns a non-AI path (teacher queue, static resource) on opt-out.
   🔵 **Expressing it as a graph node is what makes it auditable** — you can point a regulator at
   the edge, and `promptfoo` can regression-test it.
3. **"Not the primary basis" is a two-signal rule.** Any grade, placement or discipline
   recommendation must carry a second, **non-LLM** signal plus a recorded human decision.
   `edx-ora2` supplies the rubric and staff-grading workflow; `label-studio` is the reviewer UI.
   🟢 **ArguLens is the strong fit here precisely because its scorer is LightGBM over 31 explicit
   features, not an LLM** — a reproducible non-LLM signal is exactly what the statute wants, and
   its own licence NOTICE says not to use it for high-stakes decisions without human oversight.
   **Re-fit it on the client's graded corpus**: its shipped model is trained on Persuade 2.0, which
   is US middle-school essays under an academic-use grant.
4. **AB 1159 is enforced at the transport.** LiteLLM is the single egress point; pin providers
   whose terms forbid training, and for anything sensitive route to `ollama`/`vllm` so the data
   never leaves. **One config change, not an application rewrite** — which is the argument for
   putting LiteLLM in on day one even when the client starts with a hosted model.
5. **Consent must be a dimension of the telemetry, not a filter over it.** Write the consent state
   onto every xAPI statement at emission time in `lrsql`. 🔴 **Deleting records later is not
   equivalent and will not satisfy an auditor** — it cannot prove the record should never have
   existed.

**What to tell the client plainly.** North Carolina's Session Law 2026-41 sets **`2026-12-31`** for
a state model policy and **`2027-06-30`** for local policies; Alabama-shaped rules are the ones
that change the build. **Do the consent spine first.** It is cheap before the LRS and expensive
after, and it is the piece that makes the other fourteen patterns in this file sellable in a
regulated US district.

---

## P16 — Permissive SIS modernisation: records, then AI — new in `p877`

**Sell to:** any region where the deliverable must be **rebrandable** — EMEA sovereignty-scored
public bids, LATAM multi-country ministry programmes, private school groups. **Effort: 10–14 weeks.**

**Why this did not exist until now.** Every SIS this KB had verified was copyleft (Gibbon GPL-3.0,
RosarioSIS GPL-2.0, openSIS with no licence file at all), so "modernise the student-records layer
and put AI on it" could not be offered as a product a studio owns.
🟢 **[`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) is MIT** (byte-read, 1,150 B,
`sha256₁₂ b8694396d7dc`), Laravel, **API-first**, Dockerised, with Android parent and teacher apps.

| Layer | Component | Licence |
|---|---|---|
| SIS core (fork and own) | https://github.com/Gego-K12/gegok12 | **MIT** |
| Standards seam | https://github.com/Cvmcosta/ltijs | Apache-2.0 |
| K-12 data interop (US) | https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS | Apache-2.0 |
| Telemetry | https://github.com/yetanalytics/lrsql · https://github.com/openfun/ralph | Apache-2.0 · MIT |
| Early-warning signal | https://github.com/openedx/openedx-aspects | Apache-2.0 |
| Model access | https://github.com/BerriAI/litellm | MIT |
| Agent orchestration | https://github.com/langchain-ai/langgraph | MIT |
| Durable long-running jobs | https://github.com/temporalio/temporal | MIT |

**Wiring.** Fork `gegok12` and treat it as **your** codebase — that is what MIT buys, and it is the
entire reason this pattern exists. Keep its API-first contract and add the AI surface **beside** it,
not inside it: `ltijs` gives LTI 1.3 launches so the records layer and any LMS interoperate;
`Ed-Fi-ODS` is the district-facing data standard in the US; `lrsql` or `ralph` holds learner
telemetry (choose **`ralph`** for an EU bid — MIT, from France Université Numérique, with Open edX
tracking-log→xAPI converters in-tree). `openedx-aspects` supplies the analytics layer for
early-warning signals. Temporal runs the term-long and overnight jobs; LangGraph expresses the
intervention policy as auditable nodes; LiteLLM keeps the model swappable for a later sovereignty
mandate.

🔴 **State the maturity honestly, because the licence is the strength and the community is not.**
`gegok12` is **57★ with HEAD `2026-06-25`** — 113 commits in the last 12 months but nothing for
~5 months. **This is an adopt-and-own engagement, not joining a thriving upstream.** Price the
ownership: you are taking on maintenance of the records layer. 🔵 **That is also the pitch** — the
client gets a student-records system no vendor can revoke, relicense or price-raise, which is
precisely what the EU Council's "reduce dependencies on non-European technology" language asks
for and what no copyleft or SaaS option can offer.

🟡 **Do P15 before the AI layer** if the deployment is in the US; the consent flag belongs in this
SIS, and adding it here is a one-field change while it is still your fork and before telemetry
accumulates.

---

## P19 — Open edX capability without the AGPL obligation — new in `p879`

**Problem it solves.** A university, ministry or corporate client already runs Open edX, or wants
to, and needs AI-assisted capability built on top. The standing advice in this KB has been that the
engagement is then AGPL-3.0 at the platform layer and AGPL-3.0 at the operations layer (Tutor), so
anything Globant builds and hosts is exposed to §13 network-copyleft. 🔵 **`p879`'s census shows
the component layer is Apache-2.0, so the deliverable does not have to be.**

**The licence line, stated plainly before the recipe:**

| What you do | Licence consequence |
|---|---|
| Write an **XBlock** and ship it to the client | **Apache-2.0 framework; your component is yours.** No AGPL obligation attaches to the component. |
| Use **`codejail`** to sandbox execution inside your component | Apache-2.0. |
| Build the UI with **`paragon`** | Apache-2.0. |
| Put **CAS** in front | Apache-2.0. |
| 🔴 **Fork `openedx/openedx-platform` and host the modified server** | 🔴 **AGPL-3.0 §13 — source of your modifications must be offered to every network user.** |
| 🔴 **Fork Tutor (AGPL-3.0, `overhangio`) to change the deployment** | 🔴 Same. The `overhangio` estate is **3% permissive** in the census sample — there is no permissive escape there. |

🟢 **The rule: extend, never fork.** Open edX's whole plugin architecture exists so that extension
is the supported path, and the extension points are the Apache-2.0 repositories.

**Stack, all byte-read Apache-2.0:**

| Layer | Repo | ★ |
|---|---|---:|
| Component framework | https://github.com/openedx/XBlock | 471 |
| Dev workbench (no LMS needed) | https://github.com/openedx/xblock-sdk | 69 |
| Secure execution of untrusted code | https://github.com/openedx/codejail | 477 |
| Accessible UI system for learning apps | https://github.com/openedx/paragon | 141 |
| Identity / SSO / attribute release | https://github.com/apereo/cas | 11,402 |
| Mobile delivery | https://github.com/openedx/openedx-app-android · https://github.com/openedx/openedx-app-ios | 38 · 31 |
| Host platform (**client's**, unmodified) | https://github.com/openedx/openedx-platform | 8,240 (AGPL-3.0) |

**Wiring.**

1. **Develop against `xblock-sdk`, not against the client's LMS.** The workbench runs an XBlock
   standalone, so the whole build loop happens without an Open edX instance and without touching
   AGPL code.
2. **Put the model call behind the XBlock's server-side handler**, never in the browser. The
   handler is where the Art. 50 disclosure, the consent check from **P15** and the logging in
   **P14**'s measurement spine attach.
3. **Any learner-submitted code or expression runs inside `codejail`**, not in the handler's own
   process. `codejail` is the AppArmor-confined execution path Open edX itself uses for graded
   code; reusing it means the sandbox has had a decade of adversarial exposure that a new one has
   not.
4. **Register the XBlock as a CAS service** and release the minimum attribute set —
   pseudonymous id plus enrolment. The tutor then never receives a name or an email address, and
   the data-minimisation claim is a configuration file you can show an auditor.
5. **Build the UI in `paragon`** so the accessibility conformance in `verticals/solutions.md`'s
   accessibility section is inherited rather than re-litigated in the bid.
6. **Deploy as a plugin into the client's existing Tutor/Open edX install.** Globant's repository
   contains the XBlock only. 🔵 **Nothing Globant hosts is a modified Open edX, so §13 is never
   triggered.**

**Timeline:** 6–8 weeks for a first graded, sandboxed, SSO-attached XBlock in a client's staging
install, assuming the client operates Open edX already. Add 3–4 weeks if the engagement also has to
stand the platform up.

**Where it sells.** 🌎 **North America** (Open edX's origin and its largest institutional base),
🌍 **EMEA** (where the AGPL question is asked by procurement before the AI question), 🌏 **APAC**
and 🌎 **LATAM** national-platform deployments, which are overwhelmingly Open edX.

🔴 **Do not oversell this.** Apache-2.0 on the component layer does not make an Open edX engagement
copyleft-free. It makes **Globant's deliverable** copyleft-free. If the client asks Globant to host
a modified platform, P19 does not apply and the AGPL answer stands.

## P20 — Offline-first content supply chain for intermittently connected systems — new in `p879`

**Problem it solves.** A ministry, NGO or rural school system has content to distribute and
learners whose devices are online rarely and briefly. **P5** covers offline *tutoring*; it assumes
content is already on the device and says nothing about how it got there, how it is updated, or
how learner records get back. 🔵 **`p879` found that the whole pipeline exists, is MIT, and is
maintained by the organisation that built Kolibri.**

**Stack, all MIT, all byte-read:**

| Layer | Repo | ★ | Pushed |
|---|---|---:|---|
| Authoring / curation | https://github.com/learningequality/studio | 212 | 2026-11-09 |
| **Programmatic channel build** | https://github.com/learningequality/ricecooker | 32 | 2026-11-02 |
| Shared constants | https://github.com/learningequality/le-utils | 7 | 2026-11-02 |
| **Multi-peer DB replication** | https://github.com/learningequality/morango | 15 | 2026-11-13 |
| Learner-facing platform | https://github.com/learningequality/kolibri | 1,178 | 2026-11-17 |

**Wiring.**

1. **Ingest with a `ricecooker` chef.** The client's existing corpus — PDFs, videos, a ministry's
   textbook archive — becomes a Kolibri channel through a Python script, not a manual upload.
   This is the seam where AI earns its place: classification, metadata extraction, automatic
   alignment to the national curriculum and language tagging all happen **in the chef**, offline,
   before anything is published.
2. **Publish to Studio**, which gives the ministry a human review and approval step over
   machine-generated metadata. 🔵 **Keep the human gate.** `T9`'s efficacy evidence and every
   governance pattern in this file point the same way: the automated step that nobody can veto is
   the one that fails an audit.
3. **Distribute by whatever moves** — USB, local server, intermittent link. Kolibri is built for
   this and does not assume a connection.
4. **Sync records back with `morango`.** This is the part teams usually under-estimate: multi-writer
   replication between devices that are **never online simultaneously**, with conflict resolution,
   over SQLite and PostgreSQL. Reusing it instead of writing it is the difference between a 10-week
   and a 20-week engagement.
5. **Attach the measurement spine from P14** at the `morango` boundary, so efficacy data survives
   the offline hop. An offline programme that cannot measure itself cannot be renewed.

**Timeline:** 8–10 weeks for ingest → review → distribute → sync on a real corpus.

**Where it sells.** 🌎 **LATAM** (rural and public-school programmes; pairs with the Spanish-language
base in **P9**), 🌏 **APAC** (archipelagic and remote deployments), 🌍 **EMEA** (development-funded
programmes in Africa and the Middle East). 🔴 **Not** a North America pattern — connectivity there
is rarely the binding constraint, and the sale is **P13** or **P15** instead.


## P21 — The LMS write bridge, and the token nobody scopes — RESTORED and re-verified in `p880`

**Problem it solves.** Every tutoring, grading and analytics recipe in this file eventually has to
*write* to the incumbent LMS — a grade, an enrolment, a comment. **`p880` restores this pattern
because the shelf had lost both the agent and its risk envelope**: `gate-prose-claims` was reporting
`CANVAS-TOKEN-RESIDUAL` as surviving only in `archive/2026-10-31-p568-pre-rewrite/compose-patterns.md`,
and `agents/top.md` had dropped the bridge itself. 🔴 **A write pattern without its residual-risk
line reads like over-engineering, and the first thing a delivery team removes is the part it cannot
see a reason for.**

**Base**, re-measured first-hand this pass:

| Layer | Repo | Licence | ★ | Pushed |
|---|---|---|---:|---|
| LMS bridge | https://github.com/vishalsachdev/canvas-mcp | **MIT** (`1,071 B`, `5385a26e2fac`) | **333** | 2026-11-17 |
| Course shell | Moodle / Canvas / Open edX (incumbent — **never forked**) | — | — | — |
| Identity | https://github.com/apereo/cas + https://github.com/apereo/java-cas-client | Apache-2.0 / 🔵 **CONJUNCTIVE** | 11,402 / 949 | 2026-11-17 / 2026-11-16 |

**Wiring — two mounts, never one.**

1. **Mount READ and WRITE as two separate servers.** The read server gets a token scoped to the
   courses in play; the write server is **default-off**, carries a course allow-list, and requires
   `confirm=true` on any grade or enrolment call. 🔵 This is `T15` in operational form: the
   integration layer inherits the authority of the system it attaches to, **and none of its
   defences** — so the defences have to be rebuilt on the agent side.
2. **Pin `>=1.16.0`** (PyPI is at `1.18.0`) **and assert a Node.js `22.18` floor.** Below that floor
   the patched release refuses to run `execute_typescript` at all, so a deployment that upgrades the
   package and not the runtime is **not actually patched**. If the runtime cannot move, set
   `EXECUTE_TYPESCRIPT_ENABLED=false` and lose nothing this pattern needs.
3. 🔴 **Scope the token; do not merely upgrade it.** **Even patched, code executed in local sandbox
   mode can still reach the caller's Canvas token**, and outbound network blocking there is
   best-effort (issue #157). **That residual is why this pattern removes the capability and scopes
   the token rather than treating `1.16.0` as the end of the work.**
4. 🔴 **Never pass retrieved course text into a write tool's arguments without a human confirmation
   step.** `GHSA-hmr8-mvr2-mvw5` is the advisory that bites *this* pattern specifically — a
   prompt-injected assistant disclosing course data or changing grades through first-call write
   tools — and the mitigation is structural, not a prompt instruction.
5. **Put the four GHSA ids in the client's risk register by hand.** 🔴 `p880` established that all
   four are repository-level advisories **absent from the global GitHub Advisory Database**, so
   Dependabot and SCA tooling keyed on it will report an affected pin as clean. Full account and the
   calibration control: [`agents/top.md`](../agents/top.md) and
   [`evidence/advisory-globaldb.2026-11-17-p880.tsv`](../evidence/advisory-globaldb.2026-11-17-p880.tsv).

**Region.** Global. 🔵 The EU adds a reason to keep the human confirmation: under the AI Act the
education high-risk tier attaches to assessment, and a write path that can change a grade without a
person in it is the clearest possible way into that tier.

## P25 — The grade-to-record boundary: ship AI-assisted assessment into an incumbent LMS as an LTI app, with the credit-award step kept human — new in `p884`

**Sell this when** the client is a university, ministry or large training provider that already runs
Moodle, Canvas, Sakai or Brightspace, wants AI in assessment, and **cannot** replace the LMS or put
student records at risk. This is the most common education engagement there is, and until `p884` this
file had no pattern for its hardest part: **writing a grade back into the system of record.**

🔴 **Why it is the hard part.** Everything upstream of the grade is a feature; the grade write-back is
a *records* operation with legal weight. It is also the step the EU AI Act's Annex III treats as
high-risk and Brazil's `Resolução CNE/CP nº 1/2026` addresses directly by **forbidding the
attribution of a grade to an AI assessment**. A pattern that automates it is unsellable in both
jurisdictions; a pattern that *assists* it and keeps the award human is sellable in both.

### Stack — every licence byte-read, in `p884` or carried byte-read from an earlier pass

| Component | Repo | Licence (byte-read) | Role in `P25` |
|---|---|---|---|
| **LTI app framework** | https://github.com/tsugiproject/tsugi | **Apache-2.0**, 10,273 B, `sha256₁₂ 73ba74dfaa52` | The seam. Your app mounts *inside* the client's LMS over LTI; the LMS stays stock and its GPL/AGPL never reaches your code. 377 ★, pushed 2026-11-17. |
| **Grade→SIS write-back reference** | https://github.com/cilt-uct/tsugi-request-gradebook-upload | **Apache-2.0**, 11,357 B, `sha256₁₂ b40930bbcf80` | 🟢 **The row that makes this pattern concrete.** A real, permissive implementation of scheduling Brightspace gradebook items into **PeopleSoft via middleware**, written by the university that runs it. Nobody else publishes this. |
| **Human credit-award step** | https://github.com/UniversityOfHelsinkiCS/suoritustarkistin | **MIT**, 1,111 B, `sha256₁₂ 7b658dd8f1a0` | *SUOTAR* — graders **report** course completions. The reference design for "the machine prepares, the human awards". Pushed 2026-11-17. |
| **SIS ingestion** | https://github.com/UniversityOfHelsinkiCS/sis-importer | **MIT**, 1,111 B, `sha256₁₂ c54478a86110` | The read side of the student-record boundary. |
| **LMS client library** | https://github.com/KTH/canvas-api | **MIT**, 1,098 B, `sha256₁₂ 5e0ff14e95f0` | Typed Canvas API calls from your own services, maintained by the institution that uses it. |
| **Agent's LMS tool surface** | https://github.com/vishalsachdev/canvas-mcp | **MIT**, 1,071 B, `sha256₁₂ 5385a26e2fac` | The MCP server that gives the agent Canvas *tools* (courses, assignments, submissions, grades). 🔴 Read its four advisories in `agents/top.md` first. |
| **Feedback generation, not grading** | https://github.com/ls1intum/edutelligence | **MIT** | **Athena** generates *feedback suggestions for human tutors*. TUM ships it with *"instructors and tutors stay responsible for assessment decisions"* in its own README — an AI Act posture expressed as architecture. |
| **Defensibility gate** | https://github.com/AI-for-Education/pedagogy-benchmark | **MIT** | 1,143 teacher-qualification questions. How the pedagogy claim survives procurement. |

### How to wire it

1. **Build the AI feature as a Tsugi LTI app, not as an LMS plugin.** This is the whole licence
   strategy in one decision: an LTI app is a process boundary the LMS vendor already supports, so
   `T7`/`T16`'s copyleft problem never arises and the same deliverable works across the client's
   other platforms.
2. **Give the agent read-heavy access and no grade-write authority.** `canvas-mcp` for reads;
   the write path goes through step 4. 🔴 `T17`: an agent mounted on an incumbent system inherits its
   authority and none of its defences — scope the token to the courses in the engagement.
3. **Generate feedback, not marks.** Use `Athena`'s shape: the output is a *suggestion addressed to a
   human tutor*, stored against the submission, never a score committed to the gradebook.
4. **Make the credit award an explicit human action, modelled on `suoritustarkistin`.** A grader
   reviews the queue and *reports* completions; the write-back then runs as a scheduled job modelled on
   `tsugi-request-gradebook-upload`. 🔵 **Two properties fall out of this for free:** an audit trail
   that names a responsible human per award, and compliance with the Brazilian prohibition and the
   Annex III posture — with no extra work.
5. **Reconcile against the SIS, don't trust the LMS.** `sis-importer` gives you the record side;
   diff it against the gradebook before and after every write-back run.
6. **Gate release on `pedagogy-benchmark`** and publish CDPK/SEND scores in the proposal.

### Why this is sellable in all four regions

| Region | The hook |
|---|---|
| **EMEA** | Annex III education obligations land **2 Dec 2027** (🟡 secondary-sourced, `T4`). This pattern's human-award step *is* the conformance argument, and the licence audit it forces is the `p884` EMEA engagement in `intel/market.md`. |
| **LATAM** | `Resolução CNE/CP nº 1/2026` forbids attributing a grade to an AI assessment. **This pattern is already compliant by construction** — lead with that. |
| **North America** | No federal bar, but accreditation and state procurement both want an auditable grading trail; the per-award human record is the artefact. |
| **APAC** | Multi-jurisdiction deployments (Japan's MEXT guidance, Korea's AI Basic Act) differ on autonomy. One LTI app with the award step configurable per tenant covers them without a fork. |

🟡 **Maturity flags, stated because they change the estimate.** `tsugi-request-gradebook-upload` and
`tsugi-migrate-to-brightspace` are **0-star institutional tools**: correct, permissive and current,
but with no community — read them as reference implementations and budget to maintain your own copy.
`KTH/lms-nightly-sync` is frozen since 2021. Neither is a dependency you can call supported.

## P24 — Ship a branded institutional AI distribution on an MIT agent harness, instead of bolting AI onto the LMS — new in `p883`

🔵 **The engagement this is for.** A university, university system or ministry says: *"we want our
own AI assistant for staff and students — on our identity, on our models, on our data, with our
name on it."* The default proposal is a plugin inside the incumbent LMS (Moodle GPL-3.0, Open edX
AGPL-3.0), which inherits the LMS's copyleft posture, its release cadence and its browser-only
surface. 🟢 **`p883` found that the other path is already executed, in public, by a university, under
a permissive grant** — so it can be proposed with a reference rather than as a theory.

🟢 **The reference implementation.** East China Normal University publishes
**[`ECNU/EduWork`](https://github.com/ECNU/EduWork)** (376 ★, `MulanPSL-2.0`, pushed 2026-11-17) —
an education distribution of **[`deepseek-ai/deepseek-harness`](https://github.com/deepseek-ai/deepseek-harness)**
(DSH; **282,965 ★, MIT**, byte-read `master/LICENSE`, `sha256₁₂ ebb4f09972ae`) — **and**
**[`ECNU/EduWork-ECNU`](https://github.com/ECNU/EduWork-ECNU)** (29 ★), its own branded deployment
of its own distribution. 🔵 **Two repositories = the product and the worked example of
institutionalising it.**

### The stack

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| Agent runtime | [`deepseek-ai/deepseek-harness`](https://github.com/deepseek-ai/deepseek-harness) | **MIT** (byte-read `master/LICENSE`) | Plugin/skill system, tools, browser and file capabilities. **MIT means the client keeps the deliverable**; no copyleft reach into your plugins |
| Education distribution | [`ECNU/EduWork`](https://github.com/ECNU/EduWork) | **MulanPSL-2.0** (byte-read, 9,233 B) | The education plugin composition already assembled: institutional login, model discovery, knowledge studio |
| Institutional reference | [`ECNU/EduWork-ECNU`](https://github.com/ECNU/EduWork-ECNU) | MulanPSL-2.0 | What "branded for one university" looks like when its own authors do it |
| Identity | [`apereo/cas`](https://github.com/apereo/cas) | **Apache-2.0**, 11,402 ★ | The SSO layer already under much of higher education; EduWork speaks browser OIDC, so CAS's OIDC endpoint is the join |
| Model gateway | LiteLLM (EduWork ships **LiteLLM OAuth** support) | MIT | One gateway, many providers, per-faculty budgets and audit logs; keeps model choice reversible |
| Sandboxed execution (if grading) | [`openedx/codejail`](https://github.com/openedx/codejail) | **Apache-2.0** | Untrusted student code, without taking an AGPL dependency |
| Attach, don't fork | Moodle / Open edX | GPL-3.0 / AGPL-3.0 | The distribution sits **beside** the LMS and reads it over API — the copyleft stays on the far side of the boundary |

### Wiring

1. **Fork DSH? No — depend on it.** Take DSH at a pinned release (`0.2.1-rc.3` is what EduWork
   tracks). Your work is plugins, not a runtime fork; this is what keeps the MIT boundary clean.
2. **Read `EduWork`'s plugin set as the requirements document.** Institutional login + model
   discovery, knowledge studio over local materials, education skills. 🔵 It tells you which
   plugins a university actually needed, which is a month of discovery already paid for.
3. **Replace the identity plugin with the client's.** EduWork's gateway login is browser-OIDC
   against a school gateway with LiteLLM OAuth. For a CAS estate, point it at CAS's OIDC endpoint;
   for Entra/Google, the same seam. **This is the one component you always rewrite**, and it is
   the component the EU AI-literacy and transparency duties attach to (`P11`, `P19`).
4. **Put LiteLLM in front of every model call** — sovereign/self-hosted for EMEA data-residency
   (`P4`), commercial APIs elsewhere, switchable per tenant without touching plugins.
5. **Keep the LMS at arm's length.** Grades and roster over API (`vishalsachdev/canvas-mcp` for
   Canvas — 🔴 **pin ≥ 1.16.0**, see its advisory block in `agents/top.md`), never a fork.
6. **Localise.** 🟡 EduWork is Chinese-language-first with an English README. Spanish/Portuguese UI
   localisation is real work and belongs in the estimate, not in the assumptions.

### Grant posture, stated plainly

🟢 **DSH is MIT; your plugins are yours.** 🟡 **`MulanPSL-2.0` is OSI-approved and permissive with an
explicit patent grant** — functionally Apache-2.0-like for building — but it is **bilingual with the
Chinese text governing and framed under Chinese law**. Two consequences: name it explicitly in the
client's legal review, and if the client's procurement cannot accept a non-English governing text,
**take EduWork as the requirements reference and build the distribution directly on MIT DSH** —
which costs you the assembled plugin set and nothing else.

🔴 **Where this pattern does not apply.** A client whose requirement is *"inside the LMS, in the
browser, no desktop install"* — EduWork is a desktop distribution (Windows x64, macOS arm64/x64).
That client gets `P12` or the Moodle-plugin path, not this.

**Effort:** 8–12 weeks to a branded pilot on real institutional identity (identity plugin, model
gateway, localisation, one LMS read path). Add 4–6 weeks for grading with `codejail` and a
human-review trail (`P2`).

## P23 — Open-source due diligence for an education shortlist, on three independent channels — new in `p882`

🔵 **The engagement this is for.** A client arrives with a shortlist — *"we are considering Moodle,
Open edX, Artemis and DeepTutor"* — and needs, before any build decision, three answers per
candidate: **may we build on it** (licence), **is anyone still maintaining it** (liveness), and **is
this even the right repository** (identity). 🔴 This is the first week of most education
engagements, it is currently done by opening browser tabs, and `p882` measured why that is
unreliable: **the three answers come from three channels that fail independently.**

🟢 **The channel split, measured this pass** ([`record`](../evidence/channel-state.2026-11-17-p882.tsv)):

| Question | Channel | State at `p882` | What it alone cannot tell you |
|---|---|---|---|
| **Identity** — is this the canonical address? | `api.github.com/search/repositories` → `full_name` | **`200` UP** | nothing about the grant text |
| **Licence** — what does the grant actually say? | `raw.githubusercontent.com/<slug>/<branch>/LICENSE` | **`200` UP** | nothing about whether it is still maintained |
| **Liveness** — is the default ref moving? | 🆕 `api.github.com/search/commits?q=<text>+repo:<slug>` (**`200`, added `p883`**) — with `git ls-remote --symref` + `pushed_at` | **UP** | nothing about identity: a redirect answers for a *wrong* spelling. 🔴 **`p883`: `pushed_at` alone is NOT liveness** — it counts any-branch pushes and overstated three of this KB's rows by 13–22 months. Use the commits limb for the default branch, over **several free-text terms** (a one-term probe manufactures a false death), and publish the result as `HEAD ≥ date`. |

🔴 **Each channel's blind spot bit this KB in a measurable way, which is the whole argument for using
all three:**

- **Identity alone is not enough:** `p881` graded 156 published slugs against an oracle built from
  this base's own history, "fixed" two, and got one **backwards** —
  `sudosylabs/proctor` → `sudosylabs/Proctor` — because `git ls-remote` returns the *same* HEAD
  (`33db973021b3`) for both spellings. Only first-party `full_name` settles direction.
- **Metadata alone is not enough:** GitHub resolved **17 of 143** shelved repos to `NOASSERTION` or
  no licence — including `BerriAI/litellm` and `opendatalab/MinerU`. `NOASSERTION` is GitHub
  declining to classify, not a permission (`T14`), so the grant bytes must be read.
- **Stars are not liveness:** `stanford-oval/storm` carries **31,902 ★** and was last pushed
  **2025-09-30**. `LearningLocker/learninglocker` (587 ★, GPL-3.0) has been quiet since
  **2024-05-30** and is the **xAPI LRS** in this KB's analytics layer — the one component a
  learning-analytics engagement cannot route around.

### 🟢 Wiring it

**Components, all measured this pass:**

| Component | Repo | Licence (`p882`, first-party) | ★ | Pushed | Role |
|---|---|---|---:|---|---|
| licence scanner | https://github.com/aboutcode-org/scancode-toolkit | `NOASSERTION` — Apache-2.0 code over CC-BY-4.0 data, so it needs its own byte-read | 2,674 | 2026-11-11 | the industry-standard scanner: grades grant bytes against SPDX texts, including the **untitled-payload** shapes this KB hit on MIT and BSD-3 |
| the detector that produces `NOASSERTION` | https://github.com/licensee/licensee | **MIT** | 923 | 2026-11-16 | GitHub's own detector. Run it yourself and `NOASSERTION` stops being a mystery: you can see *which* rule abstained and why |
| orchestration | https://github.com/langchain-ai/langgraph | **MIT** | 45,078 | 2026-11-17 | one node per channel, so a single channel's `403` **degrades** the report instead of failing it — which is the behaviour `p881` needed and did not have |
| run record | https://github.com/temporalio/temporal | **MIT** | 24,460 | 2026-11-17 | the shortlist is re-graded on a schedule; a row that goes quiet surfaces without anyone asking |
| report surface | https://github.com/appsmithorg/appsmith | **Apache-2.0** | 41,262 | 2026-11-17 | three verdicts per candidate, for a client who will not read a TSV |
| grant-byte reader | *in-repo:* `compose/code/p881-channel-probe/probe.sh` | — | — | — | walks a path ladder (`LICENSE`, `LICENSE.txt`, `COPYING`, `docs/License.txt`, …) and emits path, byte count and `sha256₁₂`. 🔵 Deliberately **not** a GitHub row: it is 30 lines of `curl` and belongs in the engagement's own repo, not as a dependency |

🔴 **Note what the first row says about the recipe itself.** The industry-standard licence
scanner resolves to `NOASSERTION` on GitHub, for the same structural reason as nine rows on this
KB's shelves: a permissive code licence over a differently licensed data set. 🟢 **If the tool that
reads licences cannot be licence-classified by metadata alone, no shortlist can be** — which is
step 2's entire justification.

**The recipe, in the order the channels must run:**

1. **Resolve identity first, and never skip it.** `search/repositories?q=repo:<slug>` → take
   `full_name` verbatim. If it differs from the client's spelling in *any* character, the client's
   spelling is the one to correct — and record `owner.login` and `name` separately, because that is
   the evidence a redirect cannot give you.
2. **Read the grant bytes** at the resolved `full_name` and its default ref from step 1 — not at the
   spelling you were handed, and not at `main` assumed. Emit path, byte count and `sha256₁₂`. A cell
   a client can re-check is worth more than a licence name they cannot.
3. **Classify, and abstain loudly.** If the classifier cannot name a family, the verdict is
   `UNGRADED`, never `permissive`. 🔴 Three of this KB's 17 `NOASSERTION` rows still have no
   byte-read cell; that is the honest state and it is published as such.
4. **Grade liveness on two signals, not one:** `pushed_at` **and** whether the default ref's HEAD
   has moved since the last run. Flag at **>12 months** — this KB's own sweep found **7 of 143**
   over that line.
5. **Apply `T20`'s layer rule to the verdict, not just the licence.** A copyleft **platform** is a
   normal, buildable situation — attach over LTI 1.3 / xAPI / OneRoster. A copyleft **library** in
   the layer the studio is writing is the one that changes the design. Same SPDX id, opposite
   consequence, and the shortlist report should say which it is.
6. **Re-run on a schedule and keep the history.** The point is not the one-off verdict; it is the
   **delta** — a row's licence changing, or its pushes stopping, is what a client needs to hear
   about and will not notice.

🔵 **Effort and shape:** **2–3 weeks** for a 40–80 candidate shortlist including the report surface,
and it is usually the cheapest first phase a studio can sell into an education engagement, because
it de-risks every later decision and produces an artefact the client's own procurement and legal
teams can read. 🟢 **It also composes forward:** the identity and grant columns it produces are
exactly the inputs `P19` (Open edX without the AGPL obligation) and `P20` (the MIT offline supply
chain) need in order to be proposed with evidence rather than assertion.

🔴 **Do not promise a verdict the channels cannot give.** This pass could not reach `osv.dev` on
either `curl` or `WebFetch`, so **known-vulnerability coverage is not part of this recipe** in an
environment with that network policy. Say so in the report rather than leaving a column blank — an
absent channel is a finding, and a blank cell reads as a clean result.

## Pattern selection by region

| Region | Lead with | Because |
|---|---|---|
| North America | 🟢 **`p875`: lead with P13** — Ohio's district-policy deadline passed 1 Jul 2026, North Carolina's state model policy is due 31 Dec 2026 and local policies 30 Jun 2027, Maryland runs a 120-day clock and Idaho's boards must act before the 2027–28 school year. Sell against the calendar, and sell restriction-compliance too (NY sub-grade-9 proposal, CA AB 1159). Then: P1, then P6, then P7 | FERPA plus 134 bills in 31 states; MD/ID/OK/VA mandate district policy and NC's model-policy deadline is **31 Dec 2026**. Only **32%** of administrators report an institution-wide policy and **87%** of faculty wrote their own — P6 consolidates that. P7 matters because the published harm fell hardest on first-generation students, which every access-mandated institution must answer. |
| EMEA | 🟢 **P11 first**, then P4, then **P10**, then P1 | 🟢 **`p874` reorders this row: lead with P11.** The AI-literacy duty on deployers 🔴 **has applied since 2 February 2025 (`p875` correction — `p874` said July 2026)**, and **Article 50 transparency for chatbots and generated content went live 2 August 2026**, so TWO duties are already in breach today while the high-risk tier is deferred to **2 Dec 2027** — so P11 is the engagement with a *live* duty, a **measured 32-point deficit** (79% of European students use AI, 47% were shown how) and a **published standard** (EC/OECD AILit, 19 competences). It is also the on-ramp to P4 for the same buyer. Then: Article 50 disclosure is live (2 Aug 2026), the education high-risk tier lands 2 Dec 2027, and institutions are declining to renew commercial AI contracts. **P10** because the European Accessibility Act is already in force and EN 301 549 is realigning to WCAG 2.2 AA — and only one agent in this KB carries a conformance statement. For Gulf engagements, KHDA has already published school-level guidance, so lead with compliance implementation rather than policy authorship. For African engagements, the integration surfaces are Chamilo and Kolibri (**P5**), and regional code is largely unlicensed (**T10**) — so lead with licensing and partnership, not a fork. |
| APAC | **P8**, then P3, then **P12** | 🟢 **`p874` puts a dated deadline behind this row.** Vietnam's **Law No. 134/2025/QH15** has been in force since **1 Mar 2026** and existing **education** systems must comply by **1 September 2027** — **three months before the EU's 2 Dec 2027**, making it the nearest hard deadline in education AI. **Decision 33/2026/QD-TTg** (46 high-risk systems, effective 15 Aug 2026) is a published specification with a human-review carve-out, and **MOET Decision 2422** mandates 12 periods of AI content per class per year for grades 1–12. South Korea's AI Basic Act has been in force since 22 Jan 2026. P3 for national-programme scale. |
| LATAM | **P9**, then P2 and P5, then P7, then **P12** | **P9** is new and leads now: TutorIA is MIT, Colombian, Spanish-language, rural-first and ministry-funded — the only LATAM-origin base this KB has verified, and provenance counts in a public evaluation. LGPD automated-decision review is already binding. **87%** of institutions use AI, **26%** have a strategy and **9%** evaluate — so P7's measurement layer is the gap, and P2 must budget re-fitting ArguLens for Spanish and Portuguese. |
| Global | P6, then P7, then **P14** | The governance gap is universal (only **31%** of faculty are meaningfully involved in AI policy) and nobody is measuring outcomes. |

🟢 **`p877` amendments to the rows above — two regions change their lead:**

| Region | Change |
|---|---|
| **North America** | 🔴 **Insert P15 ahead of P13.** P13 sells conformance against a published calendar; **P15 is the build the calendar now requires.** Alabama H.B. 1227 (AI may not be the primary basis for grading/discipline/placement, **plus parental opt-out**) and California AB 1159 (**no training on student data**) are architecture mandates, and the consent spine is cheap before an LRS and expensive after. Sell P15, then P13 against North Carolina's `2026-12-31` / `2027-06-30` dates. |
| **LATAM** | 🟢 **P6 moves up to joint-first with P9.** `p877` quantified the arbitrage: **87% of LATAM higher-education institutions use AI, 26% have a strategy** (UNESCO IESALC, 19 countries); Brazil's schools show the same shape at **53% vs 22%** (Cetic.br). **Selling a tutor into an institution with 87% shadow adoption and no policy is selling what it already has.** Governance console first, then P9, then P5 — which `p877` repaired onto an Apache-2.0 offline base. |
| **EMEA** | Unchanged (**P11** still leads — the literacy duty is in force, high-risk is `2027-12-02`), but 🟢 **P16 is newly available** where the bid scores *rebrandability* and non-EU dependency: a **permissive** SIS now exists. |
| **APAC** | Unchanged (**P8** leads on Vietnam's 18-month education transition), with one addition: 🔴 **India's content-provenance mandate has been in force since `2026-02-20`** and binds AI-generated teaching material — scope artefact-level labelling into P3 for any India delivery. |

**If you read only one line of this file:** the two patterns no competitor is selling are **P7**
(outcome evidence about the client's own students) and **P8** (de-escalating out of a statutory
high-risk tier by design). Both are services-shaped, both are defensible with citations, and
neither can be bought as a product. **`p873` adds a third candidate: P9** — not because the
technology is novel, but because *"we are completing a Colombian public university's MIT-licensed
tutor and contributing it back"* is a position a competitor reselling a US product cannot occupy
at any price.

## P17 — MIT auto-grading at scale, with integrity by design instead of surveillance — new in `p878`

**Sell to:** higher education in **EMEA** and **North America** — technical faculties first
(computer science, engineering, data science), where submissions are code and grading is the
bottleneck. **Effort: 8–10 weeks** for a pilot on one faculty's courses; **14–18 weeks** to add the
AI feedback layer and an exam cycle.

**Why now, and why this pattern did not exist before this pass.** Three things converged.
**T8** said assessment is being redesigned rather than defended. **`p875`** measured the proctoring
category at **19 stars across six repositories, four of them zero**, and concluded the honest
advice is *"buy, or redesign the assessment."* And every permissive platform in this KB could
deliver courses but not grade them at scale — the only real grading substrate was
`openedx/edx-ora2`, **AGPL-3.0**. 🟢 **`p878` found the missing piece: `ls1intum/Artemis` is MIT,
ten years old, operated by the Technical University of Munich, and it grades.**

🔵 **The integrity argument is the commercial one.** Artemis does not watch the student. It ships
**per-student exercise variants, test runs, plagiarism checks and structured student reviews** —
integrity through assessment design. **That is sellable in jurisdictions where proctoring is
politically or legally difficult**, which now includes DC (AI barred from grading and discipline),
Florida (instructor-permission gates), the EU (grading is Annex III high-risk, see **T11**) and
every district with a parental opt-out regime (**P15**).

| Layer | Component | Licence |
|---|---|---|
| Assessment platform | https://github.com/ls1intum/Artemis | **MIT** |
| **Secure sandboxed execution** of untrusted student code | https://github.com/ls1intum/Ares | **MIT** |
| Feedback *suggestions* for human assessors (Athena) | https://github.com/ls1intum/edutelligence | **MIT** |
| LLM seam, if used standalone | https://github.com/ls1intum/Pyris | **MIT** |
| Modelling exercises | https://github.com/ls1intum/Apollon | **MIT** |
| Deployment automation | https://github.com/ls1intum/artemis-ansible-collection | **MIT** |
| Model routing, quotas, **no-train enforcement** | https://github.com/BerriAI/litellm | MIT |
| Local/sovereign inference | https://github.com/ollama/ollama · https://github.com/vllm-project/vllm | MIT · Apache-2.0 |
| Learner telemetry | https://github.com/yetanalytics/lrsql | Apache-2.0 |
| Regression tests on the feedback layer | https://github.com/promptfoo/promptfoo | MIT |
| Pedagogical quality gate on the model | https://github.com/AI-for-Education/pedagogy-benchmark | MIT |
| LTI 1.3 launch from the institution's LMS | https://github.com/Cvmcosta/ltijs | Apache-2.0 |

**Wiring.**

1. **Do not replace the institution's LMS. Launch beside it.** Artemis is the assessment platform;
   Moodle or Canvas stays the course shell. Use **`ltijs`** for an LTI 1.3 / Advantage launch with
   grade passback so the gradebook of record does not move. This is what makes the pilot
   politically survivable — nobody is asked to migrate.
2. **Stand up `Ares` first, and treat it as the security boundary.** Running untrusted student code
   is the part of auto-grading that goes wrong catastrophically rather than gradually. `Ares` is a
   JUnit 5 extension with no Artemis dependency, so it can be reviewed and pen-tested on its own
   before the platform is in place. 🔴 **`Ares2`, the second Java implementation, reports
   `NOASSERTION` — byte-read its licence before using it** (per **T14**).
3. **Turn the AI off for the first cycle.** Artemis's AI is config-gated by design. Run one full
   course cycle with automated *testing* and human grading only. This produces the baseline you
   need for step 5 and it means the first client conversation about AI happens with data.
4. **Then enable `Athena` — as suggestions, never as grades.** Athena generates feedback
   *suggestions* for a human assessor on text and modelling exercises. 🔵 **Keep that boundary
   contractual, not just architectural**: the platform's own README states *"instructors and tutors
   stay responsible for assessment decisions,"* and that sentence is the compliance posture for the
   EU AI Act's Annex III treatment of grading, DC's guidance and Alabama's "not the primary basis"
   rule all at once. Route it through `litellm` so the no-train and residency controls from **P15**
   apply unchanged.
5. **Measure what you claim.** Push competency and learning-path events into **`lrsql`** (**P14**'s
   spine) and report **time-to-feedback** and **feedback volume per assessor** — the two numbers
   that justify the project — alongside grade distributions before and after. 🔵 **Do not claim a
   learning-outcome effect.** **T9** is explicit: zero published trials evaluate any repository in
   this KB, and the largest trial of a commercial tutor is negative at the population level.
6. **Gate the model, not just the prompt.** Run `pedagogy-benchmark` against whatever model backs
   Athena and keep `promptfoo` regression tests on the feedback layer, so a model swap cannot
   silently change assessment behaviour mid-semester.

**Where it does not fit.** 🟡 Artemis is built around **university** course structures — K-12 and
corporate training will fight it; use **P12** (OpenMAIC) or **P16** instead. Java/Spring is a
heavier operational commitment than PHP or Python, so price the platform team honestly. And at
**832 stars** the community is small: **budget for reading the source, not for Stack Overflow.**

🔵 **The Apache-2.0 variant.** If counsel wants an explicit patent grant, or the scope is only
*auto-grade programming work*, substitute **https://github.com/autolab/Autolab** (Apache-2.0,
808 ★, Carnegie Mellon, created 2014) for Artemis and drop the exam, modelling and competency
layers. Smaller system, narrower promise, lighter to run.

## P18 — Paper-first assessment capture for low-bandwidth systems — new in `p878`

**Sell to:** **LATAM** ministries and state secretariats, and **EMEA**/Africa education programmes.
**Effort: 6–8 weeks** for a district pilot; **10–12 weeks** with the offline server and dashboards.

**Why now.** Every assessment pattern in this KB assumes the exam is taken on a screen. In much of
the addressable public-sector market **it is taken on paper**, and the digitisation step — not the
AI — is what blocks measurement. 🟢 **`p878` found the missing on-ramp: `Udayraj123/OMRChecker`
(MIT, 1,196 ★) grades bubble-sheets from a phone camera or a scanner.** Paired with the offline
server stack this KB already carries, it turns a paper exam into xAPI telemetry without asking a
school for bandwidth it does not have.

| Layer | Component | Licence |
|---|---|---|
| **Paper capture + grading** (phone camera or scanner) | https://github.com/Udayraj123/OMRChecker | **MIT** |
| Offline knowledge + AI server | https://github.com/Crosstalk-Solutions/project-nomad | **Apache-2.0** |
| Offline learner-facing delivery | https://github.com/learningequality/kolibri | **MIT** |
| Local inference on the same box | https://github.com/ollama/ollama | MIT |
| Records of record (Brazil: integrate, do not replace) | https://github.com/portabilis/i-educar | 🔴 **GPL-2.0** — separate service, clean process boundary |
| Permissive SIS where there is no incumbent | https://github.com/Antonio-Neves/Gestao-Escolar · https://github.com/Gego-K12/gegok12 | **MIT** · **MIT** |
| Telemetry store | https://github.com/yetanalytics/lrsql | Apache-2.0 |
| Dashboards (price explicitly — the LRS has no UI) | https://github.com/openedx/openedx-aspects | Apache-2.0 |
| Document ingestion for the item bank | https://github.com/docling-project/docling | MIT |

**Wiring.**

1. **Start from the answer sheet, not the platform.** Define the OMR template once per assessment
   programme and validate `OMRChecker` against a few hundred real sheets, including deliberately
   bad ones — creased, photographed at an angle, filled in pen. 🔵 **The accuracy of this step is
   the accuracy of the whole programme**; everything downstream inherits it. Report a measured
   per-sheet error rate, not a vendor claim.
2. **Capture at the school, process at the school.** `project-nomad` (Apache-2.0, 43,852 ★,
   4,526 forks — forks of an appliance repo are deployments) runs the pipeline and `ollama` on one
   box with no internet. Sheets are photographed, graded and stored locally; only aggregates sync
   when a connection appears.
3. **Emit xAPI from the capture step, immediately.** Write statements into **`lrsql`** at the moment
   of grading, keyed to the learner identifier the SIS already uses. This is what makes the paper
   exam a measurable event rather than a spreadsheet. 🔴 **`lrsql` ships no reporting UI** — budget
   Aspects or Grafana-over-Postgres as a named line item, as `repos/foundations.md` insists.
4. **Integrate with the records system; do not try to replace it.** 🔵 **In Brazil the incumbent is
   `portabilis/i-educar`** — GPL-2.0, 726 ★, thirteen years old, in municipal use. **Do not fork
   it.** Run the AI and capture layers as separate services that talk to it over its own interfaces,
   and the copyleft boundary stays where it is. Where there is no incumbent, `Gestao-Escolar` (MIT)
   or `gegok12` (MIT) are bases you can own outright.
5. **Add the tutor last, and only where there is a screen.** `Kolibri` (MIT) for offline delivery,
   `DeepTutor` or `OpenMAIC` on the local model if the hardware supports it — see **P5** and
   **P12**. 🟡 **The measurement is the deliverable; the tutor is the upsell.** A ministry that can
   finally see per-item results across a district has bought something defensible, and it works
   whether or not the AI layer is ever switched on.

**Honest limits.** 🔴 OMR grades **selected-response items only** — it does not touch free text, so
it narrows what the assessment can ask. 🟡 `OMRChecker` is a tool, not a platform: there is no
multi-tenant management layer, and the per-district operational wrapper is bespoke work that must be
scoped. 🟡 And the LATAM repositories above were found **this pass**, by searching in Portuguese and
Spanish for the first time — they are newly surfaced to this KB, not newly built, but nobody here
has operated them. **Treat the integration estimate as unvalidated.**


## P22 — A provider-neutral adaptive-learning foundation, with problem-first intake — new in `p881`

**Sell this when** the client wants adaptive learning they can still own in three years: a workforce or
higher-education programme where the *curriculum* will change, the *LLM provider* will change, and the
data cannot leave the device or the country. It is the pattern for a client who has been burned by a
tutoring pilot that was really a wrapper around one vendor's API.

### Stack — every licence byte-read this pass or carried byte-read from an earlier one

| Component | Repo | Licence (byte-read) | Role in `P22` |
|---|---|---|---|
| Agent foundation | https://github.com/zhangl1001/civil-ai | **MIT**, 1,066 B, `sha256₁₂ bb8885eccff8` | The spine. Provider-neutral agent execution, learner evidence, mastery projection, planning and safety boundaries, kept **separate from curriculum** by design. iOS (Capacitor) + Vue 3. |
| Problem-first intake | https://github.com/wenflow-org/wenflow | **MIT**, 1,067 B, `sha256₁₂ b6fac57d4710` | The front door. Turns *"here is my real problem"* into a learning objective, instead of asking the learner to pick a course. Develop on `develop`, not `main`. |
| Mastery comparator | https://github.com/CAHLR/OATutor | **MIT** | Bayesian Knowledge Tracing, peer-reviewed, Section 508 / WCAG conformant — the reference you grade `civil-ai`'s mastery projection against. |
| Evaluation gate | https://github.com/AI-for-Education/pedagogy-benchmark | **MIT** | 1,143 teacher-qualification questions (CDPK + SEND). This is how the pedagogy claim survives procurement. |
| Local inference | Ollama (MIT) + vLLM (Apache-2.0) | permissive | `civil-ai` is local-first; keep it that way for data-residency clients. |
| LMS mount, if required | Open edX or Moodle | **AGPL-3.0 / GPL-3.0** | 🔴 The copyleft boundary. Mount over the platform's APIs; see `P19` for keeping the deliverable Globant's. |

### How to wire it

1. **Take `civil-ai` as the foundation and delete nothing.** Its Chinese civil-service exam app is a
   *reference adapter* by the project's own README, not the product. Write a second adapter for the
   client's domain; the adapter boundary is the whole reason this repo is the base.
2. **Put `wenflow` in front of intake only.** Its contribution is the problem-clarification flow, not
   its storage or its demo deployment.
3. **Validate mastery against `OATutor`, not against vibes.** Run both on the same learner traces and
   compare the mastery curves. If `civil-ai`'s projection and BKT disagree, you have a finding to fix
   before launch, not after.
4. **Gate release on `pedagogy-benchmark`.** CDPK and SEND, scored and published in the proposal.
5. **Keep inference local** behind an OpenAI-compatible interface so the provider-neutrality claim is
   architectural rather than aspirational.

### 🔴 What is not done, and must be scoped

- **`civil-ai`'s provider-neutrality is architectural, not multi-domain-proven** — one adapter exists.
  Writing the second adapter *is* the first phase of the engagement; do not price it as integration.
- **No star or `pushed_at` figure for either repo was measurable this pass** (`api.github.com` `403`).
  Liveness is clone-measured: `civil-ai` last commit **2026-10-28**, `wenflow` **2026-11-12**.
- **Both projects are single-maintainer and primarily Chinese-documented.** There is no upstream to
  escalate to and your team will be reading `README_EN.md` at best. Price the maintenance, or fork at a
  pinned commit and own it.
- **Accessibility is unmeasured on both.** If the client is public-sector, `OATutor` is the only row in
  this stack with a published conformance document — see `P10`.
