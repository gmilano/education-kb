---
industry: education
region: Global
updated: 2026-11-23
---

# Compose patterns — education

Concrete recipes. Each names the exact repos, how they wire together, the licence posture of
the result, and a realistic build estimate. Every repo referenced is verified in
`agents/top.md`, `repos/foundations.md` or `verticals/solutions.md`.

**Fifty-five patterns, re-counted mechanically in `p927`** (`grep -cE '^## P[0-9]+' compose/patterns.md` → **55**; `P54`–`P55` added in `p927`, command run after writing them and before writing this number), **plus the new payload-address licence gate `927-G1`**, which extends `904-G1` from *probe the payload directory* to **probe the payload repository, and read the README when there is no licence file**. 🟢 **Three passes running that the re-count rule has held.** 🔵 The count is `grep -cE '^## P[0-9]+' compose/patterns.md`; **do not hand-edit it.** *(prior banner:* **Fifty-three patterns, re-counted mechanically in `p926`** (`grep -cE '^## P[0-9]+' compose/patterns.md` → **53**; `P51`–`P53` added in `p926`, command run after writing them and before writing this number). 🟢 **Two passes running that the rule has held.** 🔵 The count is `grep -cE '^## P[0-9]+' compose/patterns.md`; **do not hand-edit it.** *(prior banner:* **Fifty patterns, re-counted mechanically in `p925`** (`grep -cE '^## P[0-9]+' compose/patterns.md` → **50**; `P48`–`P50` added in `p925`, command run after writing them and before writing this number). *)* 🔴 **This line read *"Thirty-seven"* and was ten short — `P38`–`P47` were added across `p917`–`p923` and not one of those passes re-ran the command.** That is the largest drift this sentence has ever had to correct, and the fourth time it has had to. 🔵 The count is `grep -cE '^## P[0-9]+' compose/patterns.md`; **do not hand-edit it.** *(prior banner:* **Thirty-seven patterns, re-counted mechanically in `p916`** (`grep -cE '^## P[0-9]+' compose/patterns.md` → **37**; `P36`–`P37` added in `p916`, both run through the command rather than the word) (*prior banner:* **Thirty-five patterns, re-counted mechanically in `p915`** (🔴 **this line read *"Thirty-two"* and was three short — `P33` was added in `p914` and `P34`–`P35` in `p915`.** The count is `grep -cE '^## P[0-9]+' compose/patterns.md`, it is **35**, and a pass that adds one re-runs that command rather than editing the word — the same drift recurred in `intel/trends.md` this pass and is corrected there too.*)* (🔴 this line read *"Twenty-six, counted mechanically in `p907`"* and was **six short**: `P27`–`P31` were added in `p908`–`p912` and `P32` in `p913`, none of them re-counting. `p907` corrected the same line from *"twenty-three"* and wrote the rule — **a pass that adds a pattern should re-count, not increment** — and the drift resumed on the very next pass. 🔵 The count is now `grep -cE '^## P[0-9]+' compose/patterns.md`; **do not hand-edit this number**), **plus the G1 licence gate added in p897 and extended with gate `904-G1` in p904, `905-G1` in p905, `907-G1` in `p907`, `912-G1` in `p912` and `913-G1` in `p913`** (**P26 added in `p907`** — the sanctioned LMS-to-agent bridge, built from the seven per-institution user-credential bridges `intel/trends.md` **T30** measured, and the only end-to-end permissive pattern here that touches a commercial LMS) (**P22 added in `p903`** — the
national-curriculum corpus pattern, built from the Arabic-language channel's finding that the
curriculum exists at national scale and carries no grant; see `intel/trends.md` **T26**) (**P20 added in `p901`** — the first end-to-end permissive *synchronous* pattern in this file, unlocked by `p901`'s verification of `jitsi/jitsi-meet` at Apache-2.0) (**P19 added in `p900`** — the
first end-to-end permissive pattern in this file that is not offline-first, built entirely from
rows promoted out of this base's own unshelved ledger) (**P16 added in `p898`**) that runs ahead of all of them.
**p895 added P14** — offline-first literacy delivery on the one Africa-origin
permissive platform this KB has verified (`elimu-ai`), with the agent tier as studio IP because
the supply measurement leaves nothing licensed to adopt (see **T16**). **It is also the only
pattern here whose licence posture is permissive end to end.**

**p894 added P12 and P13** — the registrarial tier the KB has named as its
top opportunity for four passes, now scoped against the Apache-2.0 platform that turned out to
exist (`UniTime`), and a persona-stateless tutor design for the three regimes that have made
affective design a regulated activity for minors (see **T14**).

**Licence rule that governs all of these.** Open edX (AGPL-3.0), Canvas (AGPL-3.0) and Moodle
(GPL-3.0) are copyleft. Integrating over **LTI 1.3** or **MCP** keeps your tool a separate
work; forking the platform does not. Where a client needs a proprietary derivative, start from
**Artemis (MIT)**, **Kolibri (MIT)**, **elimu-ai/webapp (MIT)**, **Oppia (Apache-2.0)** or
**OpenOLAT (Apache-2.0)** instead.

---

## G1 — Licence pre-flight gate (run before *any* pattern below) — added p897

Every pattern here opens with a licence posture, and that posture is only as good as the licence
reading under it. **p897 byte-read the seven shelf rows whose licence was unresolved and five were
wrong as recorded** (see **T19**). This gate is the cheapest step in this file and it runs first.

### The script

[`compose/code/licence-grant-gate-p897/probe-grant.sh`](code/licence-grant-gate-p897/probe-grant.sh) —
no dependencies beyond `curl` and `sha256sum`.

```bash
./compose/code/licence-grant-gate-p897/probe-grant.sh frappe/lms OS4ED/openSIS-Classic
```

It probes **3 branches × 6 directories × 14 filenames** against `raw.githubusercontent.com` and
prints, for each hit, the **byte count and `sha256₁₂`** of the grant plus its first line. A repo
with no hit across the whole grid is reported as **unlicensed — do not ship**.

### Why the directory axis is the part people miss

GitHub's SPDX detector, and this KB's own probe until now, **classify the repository root only**.

| Repo | Root probe says | The gate finds |
|---|---|---|
| `OS4ED/openSIS-Classic` | `NONE` → reads as unlicensed | **GPL-2.0** at `master/docs/License.txt`, 17,286 B `224ac3d403e3` |
| `moodlehq/moodleapp` | `NO-LICENSE-FILE` | **Apache-2.0** at `main/COPYING.txt`, 11,358 B `cfc7749b96f6` |
| `frappe/education` | `NOASSERTION` | **GPL-3.0**, a **19-byte** `license.txt` naming the licence without reproducing it |

### 🆕 `p924` — step 0: validate the reader before you trust the bytes

🔴 **A gate that reads bytes correctly and *grades* them wrongly produces a confident, wrong legal
claim.** `p924` ran this base's own grant authority over **37 canonical licence texts** and found
**seven defects** (`intel/trends.md` **T19**). Validate the reader first — it costs one command and
no search quota:

```bash
# the cohort: SPDX serves every canonical licence text from the host we already trust
for id in AGPL-1.0-only LGPL-2.0-only Unlicense CC-BY-3.0 BSD-4-Clause BSD-3-Clause \
          BSD-2-Clause Artistic-2.0 Zlib Apache-1.1 CC-BY-NC-SA-4.0 MulanPSL-2.0; do
  printf 'spdx/license-list-data\t-\tmain\ttext/%s.txt\t200\t-\n' "$id"
done > /tmp/cohort.tsv
sed -i '1i repo\tdb\tbranch\tpath\thttp\trest' /tmp/cohort.tsv

ingest/p913-grant-authority.sh /tmp/verdicts.tsv --from-tsv /tmp/cohort.tsv
```

Any row whose verdict does not match its filename is a defect **in your scanner**, not in the
repository you were about to assess. 🔵 Run the same cohort through the client's commercial SCA tool
before you accept its output in a due-diligence report.

### 🆕 `p924` — step 0b: a bare `BSD` verdict is not a licence, and the byte count will not save you

🔴 This base carries **16 bare `BSD` cells**, and `BSD-4-Clause` is **GPL-incompatible** while
`BSD-2`/`BSD-3` are not. No canonical BSD text carries a `BSD` title, so every one of them reaches a
body fallback that cannot tell the three apart. Grade **structurally**:

```bash
# $L = the byte-read grant file
grep -qi "all advertising materials mentioning features" "$L" && echo "BSD-4-Clause — GPL-INCOMPATIBLE"
grep -qi "neither the name"                               "$L" && echo "BSD-3-Clause — non-endorsement term"
# neither -> BSD-2-Clause
```

🔴 **Do not substitute size.** Measured on this shelf: `apereo/java-cas-client` is **1,522 B and
2-clause-shaped**; `christophse/django-lti-tool` is **1,524 B and 3-clause**. Two bytes apart,
different obligations. 🔵 The same shape applies wherever a family has **no version in its title**:
grade on the clause that distinguishes the versions.

🔵 **Which of the three you have decides one concrete thing**: BSD-3's non-endorsement term governs
whether the client may put *their* brand on a derivative of the component — the exact question
`P15` (branded closed mobile client) and `P17` (grading assist over a BSD autograder) turn on.

### 🆕 `p924` — step 0c: a licence *name* is not a licence *grant*

This gate already records `frappe/education`'s **19-byte** `license.txt` that names GPL-3.0 without
reproducing it. `p924` met the class again: **`yonasab12/amharicNLP`'s entire `LICENSE` is 11 bytes
reading `MIT License`** — no copyright holder, no permission clause, no warranty disclaimer.
`search/repositories` reports **`NOASSERTION`** and is **right**.

🔵 **Rule:** below roughly 1,000 B, a grant file is a *reference* and must be reported as
`NAME-ONLY — no operative grant`, never as the family it names. A client cannot rely on it, and the
remedy is a one-line issue to the maintainer, not a legal opinion.

### The two failure modes it is built to stop

1. 🔴 **Shipping copyleft as permissive.** Several 2026 *"best open-source LMS"* comparisons list
   **Frappe LMS as MIT**. The gate reads **33,893 B of verbatim AGPL-3.0**. AGPL is
   **network-triggered** — hosting it for a client's students is a distribution event. The MIT
   belongs to `frappe/frappe`, the framework, not the LMS.
2. 🟡 **Discarding permissive options out of pessimism.** `Open-TutorAi/open-tutor-ai-CE` was
   carried as `OTHER` and therefore unusable; the gate reads **verbatim BSD-3-Clause**. In
   education, permissive is the scarce category — a false negative costs a real option.

### Gate rule

**No repo enters a client deliverable on the strength of a badge, a comparison article, or an
SPDX field.** Record the path, byte count and `sha256₁₂` of the grant next to the dependency. If
the grid returns nothing, the repo is all-rights-reserved regardless of how open it looks.
Budget: **minutes for a whole stack.**

### The payload axis, added as gate `904-G1` in p904

The directory axis above asks *where in the tree the licence file hides*. `904-G1` asks a different
question: **which licence governs the thing you are actually taking.** When a repository's payload
is data or content, the root `LICENSE` covers the code that produced it and **not** the asset.

| Repo | SPDX field says | Root byte-read says | The payload's actual grant |
|---|---|---|---|
| `bncc-dev/bncc-dados` | `MIT` | **MIT** (1,092 B) | 🔴 **CC BY 4.0** at `main/dados/LICENSE.md` (1,583 B) — **attribution required** |
| `bncc-dev/bncc-benchmark` | `NOASSERTION` | a Portuguese **index** to two files | **MIT** for `harness/`, **CC BY 4.0** for items, results and methodology |
| `bncc-dev/bncc-pacotes` | `NOASSERTION` | a Portuguese **index** to two files | **MIT** code + **CC BY 4.0** data + 🔴 **name and visual identity reserved** |

**Gate rule, additive to the one above.** Before recording a single SPDX value for a data or content
repository:

1. **Probe the payload directory for its own grant** — `dados/`, `data/`, `datasets/`, `content/`,
   `itens/`, `resultados/`, `corpus/`, `assets/`.
2. **Probe the split-licence index names** — `LICENSE-DADOS.md`, `LICENSE-CODIGO.md`,
   `LICENSE-DATA.md`, `LICENSE-CODE.md`, `LICENSE-CONTENT.md`. A root `LICENSE` that is *prose
   pointing elsewhere* is why GitHub returns `NOASSERTION`, and `p896`'s rule applies with a new
   mechanism behind it: **a `NOASSERTION` on a non-English repository is a prompt to read the file.**
3. **Ask the two questions no probe answers**: does the data licence impose **attribution** (if so it
   is a UI requirement, specified in the sprint that renders curriculum references — not a legal
   appendix), and **is the project's name or visual identity reserved** (see **T27**). A clean
   licence report is not evidence that the brand question was asked.

🔵 **Cost of skipping it, measured:** this KB's own 12-path probe would have published a 1,721-record
national-curriculum dataset as plain MIT, and a studio would have shipped a client product with an
unmet attribution obligation on its only substantive data dependency.

### The manifest axis, added as gate `905-G1` in p905

The two axes above ask which licence governs the code and which governs the payload. `905-G1` asks
the question that comes *after* both: **what else am I shipping, and can I ship it twice?** It was
written because the `p905` scan produced a wrong answer on two of its 14 targets before it produced a
right one.

**Rule 1 — an absent root manifest is not an absent dependency declaration. Probe the framework's
convention.**

| Stack | Where dependencies are actually declared | Root probe result if you skip it |
|---|---|---|
| Odoo addons (OpenEduCat, many LATAM ERP forks) | `<module>/__manifest__.py` → `depends`, and `'license'` lives here too | 🔴 no manifest at all |
| Moodle plugins | `version.php` → `$plugin->dependencies` | 🔴 no manifest at all |
| Open edX XBlocks | `setup.py` → `entry_points` | 🟡 misleading |
| Maven multi-module (Sakai) | the aggregator's `<module>` list, not the root `<dependency>` block | 🔴 undercounts |
| Python with extras (DeepTutor) | the leaves of the `-r` chain | 🔴 reports ~1 dependency |

**Rule 2 — a manifest under ~500 bytes is a pointer until proved otherwise.** Follow every `-r`,
`include:`, `extends` and `requires` to a fixed point and count at the leaves. `DeepTutor`'s
`requirements.txt` is 104 B: one comment and `-r requirements/full.txt`, which is itself 19 `-r`
lines into `requirements/modules/*.txt`. A root read gives a **floor**, never a total.

**Rule 3 — record the manifest depth beside every dependency count.** A figure without its depth is
not comparable between repositories, and that is exactly what made the largest education agent in
existence look like a one-dependency project.

**Rule 4 — read the pinning, and write it into the proposal.** Count `==` against the total:
`openedx/openedx-platform` **311/311**, `DeepTutor` **1/74**. If the base is unpinned and the client
needs a rebuildable handover, the lockfile is a **named week-one task with an estimate**, not a
footnote.

**Rule 5 — never infer a dependency-grant disclosure from a filename.** Of 14 education platforms,
`0` disclose their dependencies' grants, and the two files called `COPYRIGHT` disclose nothing: Odoo's
points at version-control history, Canvas's restates its own AGPL. **Open the file and count the
dependencies it names.** Zero is the expected answer, and it means the scan is the studio's to run
(`scancode-toolkit`, Apache-2.0) and the client's to be told about up front.

🔵 **Cost of skipping it, measured:** this pass's own scan would have published *"OpenEduCat declares
no dependencies"* and *"DeepTutor has one dependency"* — both false, both about platforms this KB
recommends — and would have handed a client the most-starred tutor in open source with no statement
that its build is not reproducible.

### The dual-file axis, added as gate `907-G1` in p907

The three axes above all assume that **when you find a licence file, it contains a licence.** `p907`
found two repositories where that assumption is false, in opposite directions, and the index
mis-reported both:

- `LJKelly3141/coursepack` — root `LICENSE` is **41 bytes**: `YEAR: 2026` /
  `COPYRIGHT HOLDER: Logan Kelly`, and **no grant**. It is the unfilled
  `usethis::use_mit_license()` R template stub. The real MIT text sits in **`LICENSE.md`** beside
  it. SPDX reports `NOASSERTION`; the repository is **MIT**.
- `dmccreary/intelligent-textbooks` — **no licence file at root at all**; `README.md` declares
  **`CC BY-NC-SA 4.0`** and points at `docs/license.md`. 🔴 `NonCommercial`: unusable in a client
  deliverable, and invisible to any root-only probe.

**Gate rule `907-G1`.** When SPDX reports `NOASSERTION` or no licence, **do not conclude "no grant"
and do not discard the row.** Read, in order: `LICENSE`, `LICENSE.md`, `LICENCE`, `COPYING`,
`LICENSE.txt`, then the `README` licence declaration, then any path the README points at. Only
after all of those return nothing is the row unlicensed. 🔵 **Why this gate differs from the other
three: they protect the client from a licence that is worse than it looks. This one protects the
*studio* from discarding permissive supply that looks worse than it is** — and in a channel whose
education ceiling is 76 ★, silently dropping `NOASSERTION` rows throws away the top of the shelf
(`swl10/pyslet`: verbatim BSD-3-Clause, byte-read, reported `NOASSERTION`).

### The classifier axis, added as gate `912-G1` in p912

The four axes above all assume that **when you read the licence text, you read it correctly.**
`p912` measured this base's own authority instrument against five granted repositories and it was
wrong on two, in opposite directions, on byte-identical payloads (`T38`):

- `Nugestudent2026/EdTech` is the **Boost Software License 1.0**. `ingest/p880-licence-byteread.sh`
  reports **MIT**, because Boost's text contains MIT's exact trigger phrase *"Permission is hereby
  granted, free of charge"*. 🔴 **A false positive on a first-match classifier.**
- `hasensaramii977-cpu/Grade-12-National-Exam-Training-Model` is **CC0-1.0**. `p880` reports
  `UNKNOWN-TEMPLATE`, because it carries **no Creative Commons detector at all**. 🔴 **A false
  negative on exactly the licence family `T25` and `T32` are about.**

**Gate rule `912-G1`.** Grant detection is a **set membership test run cumulatively, specific
before generic** — never a first match:

```
# the ordering that matters, and why
BSL-1.0   before MIT        # Boost contains MIT's trigger phrase verbatim
AGPL/LGPL before GPL        # both contain "GNU GENERAL PUBLIC LICENSE"
CC0/CC-BY/CC-BY-SA/CC-BY-NC at all   # p880 had none of them
ISC, Unlicense              # absent from p880, present in education supply
```

Run it with `ingest/p912-grant-family.sh OUT.tsv <slug>...`. It refuses empty input (`rc=2`,
the `Gap 245` class) and carries both of the above as controls. 🔵 **Two operational consequences
for a client engagement.** (1) **A Creative Commons grant on a code repository is a scope question,
not a verdict** — the instrument flags it rather than clearing it, because CC licences address
content and say little about the software built around it. (2) **A permissive verdict is not enough
to generate the notice file**: MIT and Boost are both permissive and their notice obligations
differ, so the **family**, not the permissiveness, is what the attribution step consumes.
🔴 `p880` is left in place unmodified — retiring it against these two controls is a pass of its own.

### The re-measurement axis, added as gate `913-G1` in `p913` — and it retires both instruments above

`p913` ran `912-G1`'s prescribed retirement over all **363** shelf addresses. The instrument that
`p912` built to fix `p880` **inherited `p880`'s defect in the one licence family education is built
on**: `GPL-3.0`'s own §13 is titled *"Use with the GNU Affero General Public License"*, so the
`AGPL` detector fires on a genuine GPL-3.0 payload and the `! grep AFFERO` guard then suppresses the
`GPL` branch — which means the ordering rule written above, *`AGPL/LGPL before GPL`*, **is itself
the bug**. Presence-in-body cannot discriminate this family at all; only the **title line** can
(`913-F1`, `T38`).

**Gate rule `913-G1`, and it has two limbs.**

1. **Grade on the TITLE LINE.** The body is a *marked, weaker* fallback (`BODY-` prefix), never the
   primary. This restores `ingest/licence-grade-titleline-p640.sh`'s rule, which this base made at
   `p640`, documented, and then lost at `p880`.
   ```
   true GPL-3.0  : title `GNU GENERAL PUBLIC LICENSE`         |  3 Affero mentions  | ~35,147-35,151 B
   true AGPL-3.0 : title `GNU AFFERO GENERAL PUBLIC LICENSE`  | 15 Affero mentions  |  34,523 B
   ```
2. 🔴 **A re-measurement is evidence about the INSTRUMENT before it is evidence about the shelf.**
   `912-G1` specified the discharge as *"diff the verdict column"*; executed literally that would
   have **overwritten 22 correct shelf cells with wrong ones, `moodle/moodle` among them.** When a
   new instrument disagrees with a published cell, **adjudicate per row from the payload. Recency is
   not a tie-breaker.**

Run it with `ingest/p913-grant-authority.sh OUT.tsv <slug>...`, or
`ingest/p913-grant-authority.sh OUT.tsv --from-tsv PRIOR.tsv` to re-adjudicate rows a previous
instrument already located — which makes **no search-API call at all**, because the branch and path
are facts in the input. It refuses empty input (`rc=2`, `Gap 245`) and carries **thirteen** controls,
one for every grant fix this base has ever made (listed in `repos/foundations.md`). It supersedes
`ingest/p912-grant-family.sh` and `ingest/p880-licence-byteread.sh`; both are left in place
unmodified so the `p913` diff stays reproducible.

🔵 **Four further families it detects that no prior instrument in this base could name**, each found
on this shelf: **ECL-2.0** (education's own licence — `sakaiproject/sakai`, `opencast/opencast`),
**MulanPSL-2.0** (the licence of Chinese education supply), **ODbL-1.0** (a *database* licence —
`withmarbleapp/os-taxonomy`, which the shelf had as `proprietary`), and three *shapes* rather than
families: **DUAL** (disjunctive — the licensee elects), **BY-REFERENCE** (named and linked, text not
present) and **SPLIT-BY-ASSET-TYPE** (code MIT, data CC-BY, one repository — `T25` in a single
payload). 🔴 **A single licence cell cannot express the last three**, so the gate's output is what
the notice step should consume, not the cell.

### The identity axis, added as gate `923-G1` in `p923`

Every axis above asks the grader a better question about a payload it already holds. This one asks
whether the grader can **see the family at all** — and twice in one pass, in two unrelated
families, it could not.

🔴 **Measured, on the ASF's own published texts:** `Apache-1.1` and `Apache-1.0` both graded
**`BSD / BODY-BSD`**. Apache-1.1 is titled *"The Apache Software License, Version 1.1"*; Apache-1.0
carries **no licence title at all**. Neither contains the string `apache license`, which the ASF
adopted only at 2.0, so neither ever reached the version stage that `922-F3` had just fixed.
🔴 **And independently, on a live shelf row:** `bilalabic/awesome-turkish-datasets` graded
**`CC-UNSPECIFIED`** where its bytes are `CC-BY-4.0`, because a CC legal code is titled by its
elements — *"Attribution 4.0 International"* — and never by the words *"Creative Commons
Attribution"*.

**Gate rule `923-G1`, three limbs.**

1. 🔵 **A detector keyed on a product's *current* name cannot see that product's *earlier* names.**
   Before trusting any family arm, establish the family's **earliest** published version and check
   whether its title string differs from the arm's pattern. Apache and CC are the two found; there
   is no reason to think they are the only two.
2. 🔴 **Where no version is recoverable, publish the bare root and say so — never the current
   version.** `Apache`, `MPL`, `ECL`, `MulanPSL`, `AGPL` and the CC elements are now roots that a
   table versions; a root that reaches the shelf unversioned is a *measurement*, not a default.
   This matters commercially in both directions: **Apache-1.0/1.1 are GPL-INCOMPATIBLE and carry no
   patent grant**, while a bare `BSD` cell reads as BSD-3-Clause, which is GPL-compatible — so the
   old grade understated the constraint.
3. 🔴 **Order the arms longest-element-first.** `attribution-noncommercial` preceding every
   ShareAlike arm published `CC-BY-NC-SA` as **`CC-BY-NC`** — dropping the share-alike term that
   infects a derived database, which is `T25`'s whole subject.

🟡 **And one limb about absence, from `923-F6`.** A `NO-LICENCE-FILE-FOUND` is not *"no grant"*:
`jnehring/awesome-low-resource-languages` grants **CC-BY-SA-4.0** in its README and ships no
`LICENSE` file, and both the search channel and the byte-read report nothing. 🔴 **Do not fix this
with a README grep.** A curated index's content *is* other projects' licences — measured on the four
largest ungranted catalogues, a substring grep would have invented a grant for **three of four**.
The discriminator that works is **structural** (a `## License` heading), and until it is folded into
the authority (`923-G3`) a catalogue row's absence claim should be read as *"no grant in a file"*.

Run the fixtures with `ingest/p923-adjudicator-harness.sh ingest/fixtures-p923/*.payload`. The
harness extracts `adjudicate()` **by its own delimiters**, not by line range, because a line-range
extract silently broke on this pass's first cut when the file grew.

## P1 — Licence-clean AI tutor on a permissive LMS

**For:** any client who needs to keep the result closed, or who has no incumbent LMS.
**Region:** Global. Strongest fit EMEA (EU-origin stack, sovereignty-compatible).

```
ls1intum/Artemis (MIT)                  — LMS core, exercises, cohorts
  └── ls1intum/edutelligence (MIT)      — AI service suite, already integrated
        └── ls1intum/Pyris (MIT)        — LLM microservice behind the Iris tutor
              └── BerriAI/litellm (MIT) — provider gateway + per-course budget caps
                    └── ollama (MIT) or vllm-project/vllm (Apache-2.0)  — self-hosted inference
  └── ls1intum/Ares (MIT)               — automated programming assessment
  └── qdrant/qdrant (Apache-2.0)        — per-course retrieval, payload-filtered by course_id
  └── mem0ai/mem0 (Apache-2.0)          — per-learner memory ("what this student struggled with")
```

**Wiring.** Artemis already speaks to Pyris, so the integration work is configuration, not
code. Point Pyris at `litellm` instead of a provider SDK — that one indirection is what makes
inference swappable and gives you per-course cost caps. Scope every Qdrant query by
`course_id` in the payload filter; cross-course leakage is the most common correctness bug in
education RAG.

**Result licence:** fully permissive (MIT/Apache-2.0). Proprietary extensions are clean.
**Estimate:** 6–8 weeks to a departmental pilot.

---

## P2 — Governed AI tier over an existing Moodle or Canvas (no fork)

**For:** the common case — the client already runs Moodle or Canvas and cannot replace it.
**Region:** Global. LATAM/EMEA for Moodle, North America for Canvas.

```
Incumbent: moodle/moodle (GPL-3.0)  or  instructure/canvas-lms (AGPL-3.0)
   │
   ├── LTI 1.3 route:  Cvmcosta/ltijs (Apache-2.0)        — your tool, separate work
   │     (PHP shops: tsugiproject/tsugi, Apache-2.0)
   ├── MCP route (Canvas): vishalsachdev/canvas-mcp (MIT)  — agent tools over Canvas API
   ├── apereo/cas (Apache-2.0)                             — SSO, role-based access to the AI tier
   │
   └── Your AI tier (kept outside the LMS repo):
         langchain-ai/langgraph (MIT)     — orchestration; policy checks as explicit nodes
         BerriAI/litellm (MIT)            — gateway, per-user/per-course budgets
         HKUDS/LightRAG (MIT)             — graph RAG over the course corpus
         docling-project/docling (MIT)    — PDF/slide ingestion
         SYSTRAN/faster-whisper (MIT)     — lecture transcription
         yetanalytics/lrsql (Apache-2.0)  — xAPI statements for every AI interaction
         appsmithorg/appsmith (Apache-2.0)— teacher review queue
```

**Wiring.** The LMS stays untouched; your tool is an LTI 1.3 tool provider registered in it.
Make the human-review step a LangGraph node that *blocks* — if the teacher queue is down, the
AI output does not reach the student. Emit an xAPI statement to `lrsql` for every AI
interaction, including refusals; that log is both the efficacy evidence and the compliance
artefact. Moodle HQ's own `moodlehq/wiki-rag` (BSD) is the reference for first-party Moodle RAG.

**Result licence:** your tier is permissive and separate from the GPL/AGPL core.
**Estimate:** 8–10 weeks including LTI certification and SSO.

---

## P3 — North America K-12 policy-conformant assist (50-state configurable)

**For:** US districts and K-12 vendors facing fragmented state law.
**Region:** North America.

```
virtualryder/edu-ai-agents (MIT)        — governance spine: deny-by-default authz,
                                          student-PII masking, human-in-the-loop enforcement,
                                          tamper-evident audit (FERPA/COPPA/IDEA-504/ADA)
  └── Ed-Fi-Alliance-OSS/Ed-Fi-ODS (Apache-2.0)  — the K-12 data standard across most US states
  └── Policy-config layer  (studio IP)  — per-state rules as data, not code
  └── Deterministic rubric scorer (NOT an LLM) — required by Oklahoma SB 1734
  └── openedx/edx-ora2 (AGPL-3.0) or ls1intum/Ares (MIT) — the grading workflow it feeds
  └── appsmithorg/appsmith (Apache-2.0) — teacher review and override console
  └── yetanalytics/lrsql (Apache-2.0)   — audit + parent-disclosure record
```

**Wiring.** The critical design decision is that **grading scores come from a deterministic
rubric service and the LLM only drafts narrative feedback**, which a teacher approves. That
single split satisfies Oklahoma's prohibition on AI-only grading, Idaho's bar on AI replacing
teachers, and the teacher-review mandates generally — and `virtualryder/edu-ai-agents` is
already built that way, which is why it is the spine rather than a reference.

Model each state's rules as configuration: *AI-only grading permitted (no)*, *parent opt-out
required*, *minimum grade for direct student AI use* (New York A 9190 would set grade 9),
*district framework deadline* (Ohio: 1 July 2026). A district crossing state lines flips a
config value, not a code path. This layer is the defensible studio asset.

**Result licence:** permissive apart from the `edx-ora2` option — prefer `Ares` (MIT) for a
closed derivative.
**Estimate:** 10–12 weeks for the spine plus three states; ~1 week per additional state.

---

## P4 — EMEA AI Act conformity-by-construction (admissions / assessment / proctoring)

**For:** EU institutions and edtech vendors with a hard 2 December 2027 date.
**Region:** EMEA.

```
Classify first: is the system Annex III high-risk?
  admissions · assessment & learning-outcome determination ·
  educational-level assignment · exam monitoring   → YES, obligations from 2026/1744: 2 Dec 2027
  Already banned (since Feb 2025): emotion recognition in schools — do not build it
  Already in force (Aug 2026): Article 50 — tell the student they are talking to an AI

Sovereign-by-default stack (EUA Jan 2026 favours European LLMs):
  ollama (MIT) / vllm-project/vllm (Apache-2.0)   — inference inside the institution
  BerriAI/litellm (MIT)                           — gateway; NO US-hosted API in the data path
  qdrant/qdrant (Apache-2.0)                      — vector store, self-hosted
  ls1intum/Artemis + edutelligence + Pyris (MIT)  — EU-origin, permissive platform tier
  temporalio/temporal (MIT)                       — durable runs; execution history IS the log
  yetanalytics/lrsql (Apache-2.0)                 — xAPI evidence of human oversight
  langchain-ai/langgraph (MIT)                    — oversight + disclosure as explicit nodes
  promptfoo (MIT) + AI-for-Education/pedagogy-benchmark (MIT)  — versioned eval evidence
```

**Wiring.** Three things make conformity cheap later: Article 50 disclosure as a non-bypassable
node (not a UI string), Temporal's execution history as your immutable audit record, and
`promptfoo` running `pedagogy-benchmark` in CI so you can show *when* behaviour changed and
that you tested it. Deliver the Annex III classification memo as the first artefact — it scopes
everything else and is billable on its own.

**Caveat to state to the client in writing:** confirm the 2 December 2027 date against the
Regulation (EU) 2026/1744 text. Many published sources still carry the superseded 2 August 2026
date, and this is the most commonly mis-stated fact in the sector.

**Result licence:** fully permissive, self-hostable, no US data path.
**Estimate:** 4 weeks for classification + documentation; 12–14 weeks for the governed build.

---

## P5 — LATAM governance-and-enablement retrofit (the 53/22 gap)

**For:** institutions already using AI without guidelines — 53% of Brazilian administrators use
AI, 22% have policies; 87% of regional universities use AI, 26% have a strategy.
**Region:** LATAM.

```
Week 1–2  Discovery: what AI is already in use, by whom, on what student data
Week 2–4  Policy pack: acceptable-use, disclosure, assessment-integrity, data handling
             (anchor to Brazil PL 2338/2023's pending obligations — it covers education)
Week 3–6  Technical retrofit, not replacement:
             BerriAI/litellm (MIT)         — put every existing AI call behind one gateway,
                                             with per-department budget caps and full logging
             yetanalytics/lrsql (Apache-2.0) — xAPI record of AI use (the missing evidence)
             appsmithorg/appsmith (Apache-2.0) — teacher disclosure + override console
             openfun/ralph (MIT)           — alternative LRS if Python/French-stack preferred
Week 4–8  Teacher enablement (the real deliverable; TALIS says they already use AI)
             patchy631/ai-engineering-hub (MIT) — staff upskilling material
Ongoing   Portuguese/Spanish pedagogical localisation of an APAC/EMEA-origin tutor:
             HKUDS/DeepTutor (Apache-2.0) or THU-MAIC/OpenMAIC (MIT)
Public sector (Brazil):
             portabilis/i-educar (LGPL)    — SIS built around Brazilian regulatory requirements
Low-connectivity:
             learningequality/kolibri (MIT) + iiab/iiab (LGPL) + ollama (MIT) — fully offline tutor
```

**Wiring.** The `litellm` gateway is the highest-leverage single move: it converts "AI is
happening somewhere in our institution" into a metered, logged, budgeted channel in days,
without asking anyone to stop what they are doing. Everything else builds on that visibility.

**Why localisation rather than build:** there is effectively no LATAM-origin open education
agent (only `warleysr/ankipa`, an Anki add-on). Localising DeepTutor or OpenMAIC is faster and
the pedagogical localisation is itself the billable differentiation.

**Estimate:** 6–8 weeks.

---

## P6 — APAC multi-jurisdiction deployment with content provenance

**For:** regional edtech or a multinational operating across Korea, China, India and Japan.
**Region:** APAC.

```
langchain-ai/langgraph (MIT)  — one graph, per-jurisdiction policy nodes:
    VN  → Law on AI 134/2025/QH15 + Decree 142 + Decision 33/2026/QD-TTg (eff. 15 Aug 2026):
          EDUCATION IS STATUTORY HIGH-RISK (3 of 46 listed systems — behavioural monitoring,
          learner ranking, automated assessment). Existing systems: comply by 1 Sep 2027.
          New systems: 1 Mar 2027. Notification to MOST; registration can be refused.
          *** Build this node FIRST: it is the earliest statutory deadline in the region. ***
    KR  → AI Basic Act (in force 22 Jan 2026): risk classification + oversight duties.
          2026 is a guidance-first grace period; decrees still being finalised.
    CN  → service-type rules + AI-content labelling; Cybersecurity Law AI clause (1 Jan 2026)
    IN  → IT Rules: prominent labels + provenance markers on generated content (20 Feb 2026)
    AU  → no AI statute, but TEQSA moved to a REGULATORY-LED posture in 2026 and inspects the
          genAI action plan the provider already filed (all 203 providers, 2024, 100% response).
          The client's own action plan is the requirements document — read it before scoping.
          Binding layer: Higher Education Standards Framework (Threshold Standards).
          Schools: Australian Framework for Generative AI in Schools + state additions.
    JP  → promotion-first + voluntary guidelines, NO education-specific statute (confirmed
          absence, p890) → lowest-friction pilot geography

Provenance emitted at generation time (NOT retrofitted):
    every generated item carries model, version, prompt hash, timestamp, generator identity
    yetanalytics/lrsql (Apache-2.0) — provenance + interaction record
    temporalio/temporal (MIT)       — reproducible generation runs

Content pipeline tuned for the region:
    opendatalab/MinerU (Apache-2.0)   — CJK textbooks and formulas; beats Western-trained parsers
    SYSTRAN/faster-whisper (MIT)      — multilingual lecture transcription

Tutor core (APAC-origin, permissive — partner, don't rebuild):
    HKUDS/DeepTutor (Apache-2.0)      — agentic personalised tutoring, HKU
    THU-MAIC/OpenMAIC (MIT)           — multi-agent classroom, Tsinghua, v1.4.2 (2026-11-09)
    netless-io/flat (MIT)             — interactive classroom with whiteboard
```

**Wiring.** Labelling is a dated legal requirement in two of the four markets, so provenance
metadata is emitted by the generator and stored with the artefact — retrofitting labels across
an existing content library is the expensive path. `MinerU` is the specific reason this pattern
differs from P2: CJK textbook extraction quality determines whether the whole RAG tier works.

**Mandatory non-technical workstream.** Korea attempted a national AI-digital-textbook rollout
from 2025 and reduced it to optional status within a year after teacher and parent backlash.
Budget a named teacher- and parent-consent workstream. **Cite Korea when a client wants to skip
it** — the failure was social, not technical, and it is the cheapest lesson available.

**Sequencing added in p890.** Vietnam's clock (1 March 2027 for new systems) expires **before**
the EU's 2 December 2027, so an Annex-III-grade oversight architecture built for EMEA should be
*reused* here rather than rebuilt — and it is needed sooner. Australia inverts the usual sales
motion: the provider has already written and filed a genAI plan and is now being held to it, so
the engagement is implementation of an existing commitment, not persuasion.

**Estimate:** 12–14 weeks for two jurisdictions; ~3 weeks per additional jurisdiction. Add
~2 weeks for the Vietnam node (the high-risk list is closed and specific, so classification is
quick, but notification and registration are procedural).

---

## P7 — Evidence-of-efficacy tier (attach to any of the above)

**For:** any engagement that will face a procurement office or regulator asking "did it work?"
**Region:** Global.

```
yetanalytics/lrsql (Apache-2.0)                     — xAPI statements for every interaction
  └── openfun/ralph (MIT)                           — alternative LRS (Python stack)
AI-for-Education/pedagogy-benchmark (MIT)           — pedagogical ability, not subject knowledge
EleutherAI/lm-evaluation-harness (MIT)              — subject-knowledge benchmarks, extensible
promptfoo/promptfoo (MIT)                           — CI regression gates on prompts/models
HumanSignal/label-studio (Apache-2.0)               — rubric calibration, grading gold sets
argilla-io/argilla (Apache-2.0)                     — teacher feedback collection and curation
open-spaced-repetition/fsrs4anki (MIT)              — evidence-backed review scheduling,
                                                      instead of an invented schedule
```

**Wiring.** Build the gold set with teachers in `label-studio` *before* the tutor ships; it is
both the eval baseline and the rubric-calibration artefact. Wire `promptfoo` into CI so a model
or prompt change that regresses pedagogy fails the build. Use `fsrs4anki`'s FSRS scheduler
rather than having an agent invent review intervals — there is real evidence behind it.

**Why this pattern exists.** No credible primary evidence of learning gains from AI at scale
was found in this pass; the widely quoted "42% improvement" style figures trace to blogs with
no primary study. Almost no vendor ships a measurement tier, every regulator is converging on
demanding one, and a client who can answer the question has something their competitors cannot
buy.

**Estimate:** 3–4 weeks, and it makes every other pattern defensible.

---

## P8 — Per-institution AI metering, cost attribution and exit (the Jisc specification)

**For:** any institutional engagement in the UK, and increasingly anywhere a procurement office
reviews an AI contract. **Region:** EMEA primarily; the architecture is Global.
**New in pass p890.**

**Why this pattern exists.** Jisc, with Universities UK, GuildHE and the Association of
Colleges, published what is effectively a buyer-side specification: transparent pricing,
demonstrable value, meaningful institutional choice, protection of existing functionality,
**granular usage and cost controls**, interoperability, **data portability** and safeguards
against **vendor lock-in**. The trigger is usage-based pricing replacing per-seat licences, and
institutions paying several times over for overlapping AI embedded in different platforms. A
companion Jisc/EAUC report found vendors seldom publish institution-level usage at all. Every
other pattern in this file answers a regulator; **this one answers the person who signs the
cheque**, and they have written the requirements down.

```
Request path — attribution is established before inference, not inferred afterwards:

  apereo/cas (Apache-2.0)            — SSO; the identity that carries
                                       institution / faculty / course / role claims
    └── Cvmcosta/ltijs (Apache-2.0)  — LTI 1.3 launch; course + role context from the LMS,
                                       so the tool detaches from any one platform
        └── BerriAI/litellm (MIT)    — gateway: ONE virtual key per cost centre
                                       (institution → faculty → course), hard budget caps,
                                       provider-agnostic so the model layer stays swappable
            ├── ollama/ollama (MIT)  — local inference: the zero-marginal-cost tier
            ├── vllm-project/vllm (Apache-2.0) — self-hosted at throughput
            └── hosted API           — the exception, and now a visibly priced one

Metering and export — OpenTelemetry, because OTel IS the portability answer:

  traceloop/openllmetry (Apache-2.0, 7,541★)  — PREFERRED. OTel-native LLM tracing: the
                                                usage data lands in the observability stack
                                                the institution already runs. Nothing to
                                                migrate on exit because nothing was captive.
  openlit/openlit (Apache-2.0, 3,088★)        — OTel-native alternative with cost tracking
  Helicone/helicone (Apache-2.0, 6,287★)      — gateway-level logging and cost attribution
  (langfuse/langfuse, 37,577★ — LARGEST BUT SPLIT LICENCE: "MIT Expat" core, separate
   enterprise licence on ee/, web/src/ee/, worker/src/ee/, packages/shared/src/server/ee/;
   copyright now ClickHouse, Inc. Diligence before it enters a client deliverable.)

Evidence that the spend bought something:

  yetanalytics/lrsql (Apache-2.0)             — xAPI: usage joined to learning interactions,
                                                which is how "demonstrable value" stops being
                                                a slide and becomes a query
  qdrant/qdrant (Apache-2.0)                  — embeddings in a store the CLIENT owns
```

**Wiring.**

1. **Mint one `litellm` virtual key per cost centre, not per application.** Attribution has to
   exist at request time; a report that infers which faculty spent what is the thing the Jisc
   statement is complaining about.
2. **Carry institution/faculty/course/role from CAS and the LTI 1.3 launch into the gateway
   key** — the LMS already knows the context, so do not rebuild a hierarchy beside it.
3. **Emit OTel spans, not vendor events.** This is the single decision that satisfies data
   portability: the institution can point the exporter at its own collector on day one, and
   nothing has to be extracted on exit.
4. **Set hard caps, not alerts.** Usage-based pricing without a ceiling is the exposure; a
   budget cap that returns a graceful degradation (local `ollama` model instead of a hosted
   call) keeps the service up while the cost stays bounded.
5. **Write the exit into the build:** documented export of usage data, embeddings, prompts and
   content, plus an LTI 1.3 integration that the client can repoint at another tool. Deliver it
   as a runbook, because an untested exit is not an exit.
6. **Price per learner-outcome, not per token.** The buyer has stated publicly they will not
   sign per-token exposure.

**What makes this defensible.** None of the four metering repos is built for education: they
know about users and projects, not institutions, faculties, courses and cohorts. **Mapping an
OTel LLM-metering layer onto an academic hierarchy, with LTI-derived context and per-cost-centre
budget enforcement, is genuine studio IP** — it answers a published, signed, sector-wide
requirement, and no vendor currently ships it.

**Caveat.** The Jisc statement is a request to suppliers, not a regulation. It carries no
penalty. Its force is commercial: it is signed by the bodies representing most of UK higher and
further education, and it tells you precisely what a tender will ask.

**Estimate:** 5–7 weeks on top of an existing AI tier; ~9 weeks standalone. The exit runbook
and the per-cost-centre hierarchy are the long poles, not the tracing.

---

## P9 — Integrity by assessment redesign, not detection

**For:** any higher-education or senior-secondary client currently buying, piloting or being
pressured to buy AI-detection tooling.
**Region:** Global. Strongest fit **North America (Canada especially)** and **EMEA**; also the
compliant answer to the **UAE** exam-context prohibition.
**Added:** p891. Evidence behind it: **T10** in `intel/trends.md`.

### Why this pattern exists

Detection is being removed as a control by institutional counsel, not by faculty. All six
Canadian universities in a 2026 review declined to enable or endorse AI detection, privacy
cited at four; Concordia bars staff from using online detectors outright; UBC cites a Privacy
Impact Assessment. Sending student work to a third-party detector is a disclosure event under
FOIPPA/FIPPA, GDPR, and the US state student-data statutes — **California AB 1159 bars using
student data to train AI models at all**. Meanwhile the EU Council's October 2026 conclusions
ask member states for **academic-integrity policies**, and the UAE's classroom guide bans AI
**during exams and assessments**. Every regional signal asks for a *process control*. None asks
for a *classifier*.

**Sell this as the replacement for a detection line item that is about to be cancelled.**

### Stack

```
Incumbent LMS (Moodle GPL-3.0 / Canvas AGPL-3.0 / Open edX AGPL-3.0)
  │   integrate over LTI 1.3 — never fork; keeps your work a separate work
  ├── ls1intum/Artemis (MIT) ................ where a permissive core is available:
  │     └── ls1intum/edutelligence (MIT) .... already-integrated AI tier
  │                                           exercise + rubric model to copy
  ├── Submission-process instrumentation ..... draft history, revision timeline,
  │     (LMS-native: Moodle assign plugin /    time-on-task — product evidence
  │      Canvas submission API via            replaced by process evidence
  │      vishalsachdev/canvas-mcp, MIT)
  ├── openedx/edx-ora2 (AGPL-3.0) ........... open-response + peer/self/staff grading;
  │                                           the seam for structured oral defence
  ├── CAHLR/OATutor (MIT) ................... A/B-testable tutoring instrumentation —
  │                                           use it to prove the redesign worked
  ├── langchain-ai/langgraph (MIT) .......... rubric-reasoning agent as explicit,
  │                                           auditable policy nodes (not a verdict)
  ├── AI-for-Education/pedagogy-benchmark (MIT)  eval gate before anything touches a cohort
  └── ollama (MIT) / vllm-project/vllm (Apache-2.0) + BerriAI/litellm (MIT*)
        *litellm is MIT outside `litellm/enterprise/`; that directory is separately
         licensed. Use the OSS paths — see repos/foundations.md.
        └── student work never leaves the institution — this is what makes the PIA pass
```

### The design rule that makes it defensible

**No component emits a judgement about whether a student used AI.** The agent tier grades
*reasoning against a rubric* and surfaces *process artefacts* to a human marker. The integrity
finding is always made by a person, from evidence the student can see and contest. That is what
survives a privacy review, an appeal, and EU AI Act Article 14 human-oversight design — which
is deferred to **2 December 2027** but is the standard the architecture should already meet.

### Deliverables

1. **Assessment-redesign programme** — rubrics that grade reasoning, drafts and version history
   as graded artefacts, supervised in-class components, oral defence for a sampled subset.
2. **Process-evidence instrumentation** in the incumbent LMS, over LTI 1.3.
3. **Privacy artefact** — PIA, vendor-assessment template, data-flow diagram showing inference
   is local. In Canada this is the document that unlocks procurement.
4. **Appeals runbook** — how a contested finding is reviewed, by whom, on what evidence.
5. **Efficacy measurement** — attach **P7**; OATutor's instrumentation is the cheapest route to
   a defensible before/after.

### Licence posture

Clean. Everything load-bearing is MIT/Apache-2.0 and reached over LTI 1.3, so a GPL/AGPL
incumbent LMS stays a separate work. `edx-ora2` is AGPL — use it **in place** inside an existing
Open edX deployment, do not vendor it into a proprietary derivative.

### Estimate

**8–11 weeks.** Assessment redesign with faculty is the long pole, not the engineering —
budget roughly 40% of the effort for workshops and rubric development, and expect the
privacy artefact to gate go-live in Canada and EMEA. A detection-replacement framing shortens
the sales cycle considerably, because the budget already exists.

### Where it does not apply

Where a regulator has mandated proctoring or automated assessment outright — **Vietnam**, where
automated assessment is statutorily high-risk under Decision 33/2026/QD-TTg with an 18-month
education transition. There the engagement is **P6** plus conformity work, not this pattern.

## P10 — National curriculum-mandate delivery: teacher enablement at system scale

**New in pass p892.** Written once for **India** and **Saudi Arabia** because the two
engagements are the same build with the curriculum corpus and the language swapped. Also fits
Vietnam's 12-periods-per-year mandate and, with the student tier removed, the EU Article 4
staff-literacy duty.

🆕 **`p938` adds Taiwan, and it is the cleanest fit this pattern has.** Taiwan's **AI Basic
Act** (promulgated **2026-01-14**) obliges the government to **promote AI and AI-ethics education
across schools, industries, organisations, society and public institutions**, with the central
education authority to issue **school AI-use and learning guidelines**. 🟢 **No modification to
this pattern is required** — it already assumes a state mandate, a client-owned curriculum and a
teacher-capacity constraint, and Taiwan supplies all three. 🟡 Two cautions specific to this
jurisdiction, both from `intel/market.md`'s APAC block: the **article number is contested** across
sources (7 vs 9) and the reported **2026-07-14** guideline deadline rests on a single garbled
snippet, so **neither belongs in a proposal**; and the **Ipsos Education Monitor 2026** has support
for *banning* school AI **rising** in the region (Japan 21%→29%, Korea 27%→31%, Australia
47%→52% — a majority). 🔵 **In Taiwan the risk-bearing half of this pattern is the
teacher-and-parent-facing half, not the technology**, which inverts the usual weighting: budget the
communications and consent surface as a first-class deliverable rather than a change-management
afterthought.

🔴 **And the supply side is empty.** No Taiwan-origin, permissively licensed education
repository has surfaced in this base. The curriculum corpus and the delivery platform both have to
come from elsewhere in this file (`OpenOLAT` Apache-2.0 for the institutional tier), with
localisation as studio work — priced as build, not as adoption.

### Why this pattern exists

Every other pattern in this file answers a constraint on AI *use*. This one answers a state
mandate to *teach* AI, which T11 establishes across India, Saudi Arabia, Vietnam, the UAE,
North Carolina and the African Union strategy. The distinguishing facts:

- **The curriculum already exists and the client owns it.** NCERT/CBSE in India; the National
  Curriculum Center in Saudi Arabia. **Do not author courseware.** Authoring it is both out of
  scope and politically unwinnable.
- **The constraint is teacher capacity, stated explicitly by the buyers** — 240,000 teachers in
  training in KSA (60,000 reached), and India's own commentary that adding a subject is not the
  same as preparing teachers to teach it.
- **The buyer is a ministry or board**, so evidence of coverage is a contractual artefact, not
  a nice-to-have.

### Stack

Every repo named is verified in this KB with licence and last-push date.

**1. Curriculum ingestion — the client's own documents, never a generic corpus**

| Component | Repo | Licence |
|---|---|---|
| PDF/DOCX curriculum → structured text | `docling-project/docling` | MIT |
| Heavier layout/formula extraction | `opendatalab/MinerU` | Apache-2.0 (SPDX NOASSERTION) |
| Retrieval over the ingested curriculum | `HKUDS/LightRAG` or `infiniflow/ragflow` | MIT / Apache-2.0 |
| Vector store the client owns | `qdrant/qdrant` | Apache-2.0 |

**2. Model layer — swappable, because sovereignty differs by market**

| Component | Repo | Licence |
|---|---|---|
| Gateway, per-district keys and budget caps | `BerriAI/litellm` | **MIT except `litellm/enterprise/` — do not vendor that path** |
| Local/self-hosted inference | `ollama/ollama` · `vllm-project/vllm` | MIT / Apache-2.0 |

Keep the gateway even if the first deployment calls a hosted API. It is what lets the Saudi
build answer a national-AI-company requirement and the Indian build answer a data-residency
one without re-architecture (T6).

**3. Teacher-facing generation — the actual deliverable**

| Component | Repo | Licence |
|---|---|---|
| Lesson/slide/quiz generation from curriculum | `THU-MAIC/OpenMAIC` | MIT |
| Local-first lesson-prep design reference | `SirhanMacx/Claw-ED` | MIT — **read it, do not pin it** (last push 2026-09-19) |
| Exercise/item rendering | `Khan/perseus` | MIT |
| Orchestration with explicit policy nodes | `langchain-ai/langgraph` | MIT |
| Durable long-running enrolment/cohort workflows | `temporalio/temporal` | MIT |

**4. Delivery and reach**

| Component | Repo | Licence |
|---|---|---|
| Training delivery to teachers | `oppia/oppia` (Apache-2.0) if greenfield; integrate to the client's LMS over **LTI 1.3** with `Cvmcosta/ltijs` (Apache-2.0) if not | Apache-2.0 |
| Low-bandwidth / offline cohorts | `learningequality/kolibri` | MIT |
| Admin and cohort-tracking console | `appsmithorg/appsmith` | Apache-2.0 |

**5. Evidence — the part that gets the contract renewed**

| Component | Repo | Licence |
|---|---|---|
| Pedagogical-quality eval gate on generated material | `AI-for-Education/pedagogy-benchmark` | MIT |
| Per-district/per-cohort usage and cost attribution, OTel-native | `traceloop/openllmetry` | Apache-2.0 |

### How it wires together

1. Ingest the ministry's curriculum with `docling` → chunk → embed → `qdrant`. **This corpus is
   the only authority the generation tier may cite.**
2. `langgraph` runs the generation flow with the policy checks as explicit nodes: grade-band
   check, curriculum-citation check, provenance-label emission, language check. Explicit nodes
   are what make the flow auditable to a ministry.
3. `litellm` fronts every model call, keyed per district so cost attribution exists from day one.
4. `OpenMAIC` generates the teacher's lesson, slides and quiz items; `perseus` renders items.
5. `pedagogy-benchmark` gates output on pedagogical quality before a teacher ever sees it.
6. Delivery through `oppia`, or into the client's existing LMS over LTI 1.3 via `ltijs`;
   `kolibri` carries the offline cohorts.
7. `openllmetry` emits coverage and cost per district into whatever observability stack the
   ministry already runs — which is also the portability answer (T9).

### The design rules that make it defensible

- **Retrieval over the ministry's curriculum, never training on it, and never on student or
  teacher data.** California AB 1159 forecloses the training architecture outright; building
  the no-training version once makes the same stack sellable in every market.
- **Emit provenance labels at generation time.** India's amended IT Rules require prominent
  labels and provenance markers on AI-generated content from **20 February 2026** (T7).
  Retrofitting a national content library is the expensive path.
- **Grade-banding is a policy node, not a prompt.** India's mandate is Classes III–VIII; the
  UAE prohibits under-13 and below-Grade-7 use entirely. The same deployment must be able to
  answer both, and a prompt instruction is not an answer a regulator accepts.
- **Teacher-in-the-loop is the product.** Generated material is a draft a teacher edits and
  approves, and the approval is logged. This is T1's oversight requirement and also the only
  posture that survives T8's consent problem.

### Deliverables

1. Curriculum-grounded lesson-preparation service, grade-banded, provenance-labelled.
2. Teacher training-delivery tier with per-cohort completion evidence.
3. Coverage and cost dashboard by district, exportable (the ministry's reporting obligation).
4. Policy-node configuration per jurisdiction — grade bands, prohibitions, labelling.
5. Evaluation report from `pedagogy-benchmark` on generated material, as an acceptance gate.

### Licence posture

Clean. Every component is MIT or Apache-2.0 except the carve-out in `litellm/enterprise/` (do
not vendor it) and `kolibri`'s MIT core, which is fine. **If the client's LMS is Moodle
(GPL-3.0) or Canvas (AGPL-3.0), integrate over LTI 1.3 and the deliverable stays a separate
work** — the single most important licence decision in this pattern (see `README.md`, fact 1).

### Estimate

**14–18 weeks** to a first district or regional cohort: 3–4 weeks curriculum ingestion and
retrieval quality, 4–5 weeks generation tier and policy nodes, 3–4 weeks delivery integration,
2–3 weeks evidence tier, 2 weeks evaluation and acceptance. Longer than every other pattern
here because the buyer is public-sector and acceptance is formal.

### Where it does not apply

- **Not for institutional self-service markets.** If the buyer is a single university, this is
  P2 or P8, not P10.
- **Not where no mandate exists.** Without a funded state programme this becomes speculative
  courseware, which is a product business and not a services engagement.
- **Not as a route to selling a student tutor.** The mandate is teacher capacity (T11). A
  student-facing tutor sold against it is the wrong deliverable, and every open tutor this KB
  tracks is English- or Chinese-first — in India and Saudi Arabia that is a localisation
  project, not a dependency.


## P11 — Read-only-first Moodle agent tier over MCP (added p893)

### Why this pattern exists

P2 already covers putting a governed AI tier over an existing Moodle or Canvas **without
forking it**, and it does so over LTI 1.3. p893 established that a second seam now exists and is
better suited to agents: **MCP** (see **T13**). LTI ships your tool *into* the LMS; MCP exposes
the LMS *to* your agent. P11 is the MCP half, and it exists as its own pattern because of one
property the LTI route does not have — **the community has already split read and write across
two separately-maintained MIT servers**, which makes a genuinely read-only pilot a
configuration choice rather than a promise.

Use this when the client runs Moodle (the most-installed LMS on earth), wants agent access to
real coursework, and has a data-protection function that will not approve write access to a
gradebook on day one. Which is most of them.

### Stack

Every repo named is API-verified and licence byte-read in this KB as at 2026-11-18.

**1. The LMS tool surface — staged by access posture**

| Stage | Component | Repo | Licence | ★ |
|---|---|---|---|---|
| Pilot | **Read-only** Moodle MCP — courses, assignments, quizzes, deadlines, files | `Faixiang/Moodle-MCP` | MIT | 208 |
| Pilot | Companion agent skill: diff new coursework, list unsubmitted work | `Faixiang/Moodle-Course-Watch` | MIT | 0 |
| Graduation | **Read-write** Moodle MCP — forums, grades, files-as-markdown | `G36maid/moodle-mcp` | MIT | 30 |
| Graduation (alt) | Write path with explicit idempotency guarantees | `MarcosNahuel/moodle-mcp` | MIT | 1 |
| Open edX variant | Staff/superuser admin facade (Ulmo) + Tutor plugin | `blend-ed/openedx-mcp` · `blend-ed/tutor-contrib-openedxmcp` | AGPL-3.0 | 3 · 2 |

**Do not use** `loyaniu/moodle-mcp` (58 ★) or `onbirdev/moodle-webservice_mcp` (19 ★): both
were licence-checked this pass and **have no licence file**, which means all rights reserved
regardless of how they are described elsewhere.

**2. The agent tier — unchanged from P2, reused deliberately**

| Component | Repo | Licence |
|---|---|---|
| Auditable orchestration — policy checks as explicit graph nodes | `langchain-ai/langgraph` | MIT |
| Gateway, per-institution keys, budget caps, model portability | `BerriAI/litellm` | **MIT except `litellm/enterprise/`** |
| Local / sovereign inference | `ollama/ollama` · `vllm-project/vllm` | MIT / Apache-2.0 |
| Retrieval over course material the institution owns | `qdrant/qdrant` | Apache-2.0 |

**3. The user-facing surface — still LTI, not MCP**

| Component | Repo | Licence |
|---|---|---|
| LTI 1.3 / Advantage tool provider | `Cvmcosta/ltijs` | Apache-2.0 |

MCP is how the agent reads the LMS. LTI is how the learner reaches the agent inside the LMS.
A serious build uses both; using MCP for the user surface means rebuilding auth and launch
context the LTI spec already solved.

**4. The evaluation gate — non-optional**

| Component | Repo | Licence |
|---|---|---|
| Pedagogical-ability benchmark | `AI-for-Education/pedagogy-benchmark` | MIT |
| Prompt/LLM regression testing in CI | `promptfoo/promptfoo` | MIT |

### How it wires together

1. Stand up `Faixiang/Moodle-MCP` against a **non-production Moodle clone** with a scoped
   service token. Read-only by construction, so the first conversation with the client's DPO is
   about token scope, not about what the agent might overwrite.
2. Put LangGraph in front of it. Every tool call the agent makes to the LMS passes a policy
   node — which courses, which fields, whose data — and that node writes an audit record. This
   is the part that is reusable when the client's regime changes; keep policy in configuration.
3. Expose the learner-facing surface through `ltijs` so launch, identity and course context come
   from the LTI launch rather than being reimplemented.
4. Gate every release on `promptfoo` suites plus `pedagogy-benchmark`. A tutor that regresses
   pedagogically but passes unit tests will ship otherwise.
5. **Graduate to write scope as a separate, documented decision** — swap in `G36maid/moodle-mcp`
   behind the same policy nodes. The audit trail from the read-only phase is the evidence that
   makes that approval obtainable.

### The design rules that make it defensible

- **Scope the token, not the prompt.** These servers typically run with the operator's own API
  token, so the agent inherits every permission that human has. A prompt instruction not to
  touch grades is not a control. A token without the grade capability is.
- **Read-only is a deployment artefact, not a claim.** The reason to use two separate servers
  rather than one with a flag is that a flag is a configuration error away from being wrong,
  and a server with no write code is not.
- **Keep the agent out of the gradebook of record for as long as possible.** Under the EU AI
  Act, assessment is Annex III high-risk from **2 December 2027**; under Oklahoma's rule AI-only
  grading is already barred; California AB 1159 forecloses training on student data entirely.
  Reading coursework to help a learner is a different regulatory object from writing a grade.
- **Pin versions.** Five of the seven Moodle MCP servers were created in the last six months and
  the ecosystem is unconsolidated. Vendor the one you choose.

### Deliverables

- A read-only Moodle agent tier running against the client's own course data, with a policy
  node per tool call and a complete audit log.
- A token-scoping specification and a DPO-facing note explaining why read-only is structural.
- Eval suites wired into CI with a recorded pre-deployment baseline.
- A written graduation plan to write scope, with the evidence requirements named up front.

### Licence posture

Clean. The Moodle servers, `ltijs`, LangGraph, Qdrant and both eval tools are MIT or
Apache-2.0, and nothing here forks Moodle — so Moodle's GPL-3.0 stays on Moodle's side of the
boundary and the client's tier can be closed. **Two exceptions to state explicitly:** the
Open edX variant is **AGPL-3.0** and is vendor-maintained rather than foundation-maintained, and
`litellm/enterprise/` must not be vendored.

### Estimate

**5–7 weeks** to a read-only pilot on a Moodle clone with policy nodes, audit and eval gates.
Add **3–4 weeks** for the graduation to write scope, most of it approval rather than code.

### Where it does not apply

- **Not on Canvas** — use `vishalsachdev/canvas-mcp` (MIT, read-write) or `boyuchengz/canvas-mcp`
  (MIT, read-only) in the same shape; the pattern transfers, the repos do not.
- **Not where the client wants a closed derivative of the platform itself.** That is Mentingo
  (MIT) or Artemis (MIT) and pattern **P1**, not an integration over somebody else's GPL core.
- **Not as a shortcut past LTI.** If the deliverable is a learner-facing tool inside the LMS,
  MCP alone will cost more than it saves.
- **Not where Moodle HQ support is a procurement requirement.** Moodle HQ has published no MCP
  server; every option here is community-maintained, and that must be said before signature.

## P12 — Registrarial agent tier over UniTime (the KB's named gap, scoped to what is actually missing)

### Why this pattern exists

Every pass of this KB has named the registrarial layer — enrolment, timetabling, transcripts,
financial aid — as the industry's clearest build-vs-adopt gap and the most defensible studio IP.
**p894 found that the gap was half misread**, and the half that was wrong changes the estimate by
months. The *agent* tier genuinely does not exist: a dedicated leg found only course capstones
(`aabbiisshhaa/student-support-agent`, 2 ★, no licence, Makerere University;
`vaibhav9895-lang/student-support-agent-assignment`, 0 ★, no licence;
`leechenwei/Ai-Agent-Timetable`, 0 ★, no licence, idle since 2025-02-24). But the **platform
underneath it exists, is permissive and was pushed yesterday** — `UniTime/unitime`, Apache-2.0,
360 ★, 2026-11-17 — and it had fallen out of `verticals/solutions.md` in the 2026-11-18 rewrite.

So this is not "write a registrarial platform". It is **"put an agent and a decisioning tier over
a maintained Apache-2.0 scheduler, and build only the parts that have nothing"** — which is a
10-week engagement rather than a multi-year product.

Use this where a university client has a timetabling or exam-scheduling pain, a registrar who
spends their week on conflict resolution and exception requests, and an SIS of record that is
not going to be replaced.

### Stack

Every repo named is API-measured and licence byte-read in this KB as at 2026-11-18.

**1. The registrarial core — adopt, do not build**

| Component | Repo | Licence | ★ | Note |
|---|---|---|---|---|
| Course and exam timetabling, student scheduling | `UniTime/unitime` | **Apache-2.0** | 360 | Pushed 2026-11-17. Runs standalone or interfaces to an existing SIS |
| The constraint solver underneath it | `UniTime/cpsolver` | **LGPL-3.0** | 84 | **Licence boundary — see below.** Do not static-link into a closed component |
| Small-scale permissive alternative | `GEOSOFT-GLOBAL/timetablely` | MIT | 27 | Idle since 2026-08-17; a starting point, not a dependency |
| SIS of record (LATAM public sector) | `portabilis/i-educar` | GPL-2.0 | — | Built around Brazilian regulatory requirements |
| K-12 SIS where a closed derivative is required | `Gego-K12/gegok12` | MIT | — | The only MIT-licensed SIS this KB has verified |

**2. The agent tier — this is the part you build**

| Component | Repo | Licence | Role |
|---|---|---|---|
| Orchestration with auditable policy nodes | `langchain-ai/langgraph` | MIT | Every eligibility and exception check is an explicit node, not a prompt instruction |
| Role split: registrar / scheduler / adviser / reviewer | `crewAIInc/crewAI` | MIT | Optional; use where the workflow genuinely has four hand-offs |
| K-12 data standard (North America) | `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` | Apache-2.0 | Non-negotiable for a US K-12 engagement |
| SSO and per-role access to the agent tier | `apereo/cas` | Apache-2.0 | Same foundation as UniTime; already in most higher-ed estates |
| Human review queue | `appsmithorg/appsmith` | Apache-2.0 | What makes human-in-the-loop real instead of aspirational |
| Evidence that it helped | `yetanalytics/lrsql` + `agentscope-ai/OpenJudge` | Apache-2.0 both | Decision-quality and turnaround-time measurement; see **P7** |

### How it wires together

1. **UniTime stays the system of record for schedules.** The agent never writes a timetable
   directly; it proposes, and UniTime's solver validates. This is the single most important
   decision in the pattern — it keeps feasibility guarantees in the component that has them.
2. **Exception intake is the agent's first job, not scheduling.** Room-change requests, clash
   appeals, accommodation-driven constraints and late enrolment arrive as free text; the agent
   normalises them into UniTime constraints and explains what it changed.
3. **Eligibility and decisioning are policy nodes, deterministic, with the LLM confined to
   evidence extraction.** This is the one design rule the 0 ★ grading cohort got right
   (`Atmankhyar`, `timothyheeeee`, `virtualryder/edu-ai-agents`): the model reads documents and
   cites them, a rule engine decides.
4. **Every decision carries criterion-level evidence and a regrade path** — taken from
   `asu2304/auto-assessment-agent`. An appeal procedure is not a feature here; it is what makes
   the tier lawful in the EU.
5. **Accommodation constraints merge, never override.** From `SudhanvaJ-bit/project-samarth` via
   `P496-1`: the statutory accommodation baseline enters agent state such that the model **can
   add but cannot remove** a required accommodation. A scheduler that can drop an accessibility
   constraint is a Section 504 / ADA Title II incident, not a bug.
6. **Audit and metering per institution** as in **P8**, because this tier touches the registrar's
   authority and someone will ask who changed what.

### The design rules that make it defensible

- **Never let the agent make an admissions or financial-aid decision.** Those are **EU Annex III
  high-risk** and restricted under several US state laws. Scope the agent to *scheduling,
  exceptions and explanation*, and keep decisioning as an assisted human workflow with
  deterministic rules. This is the boundary that keeps a 10-week engagement out of a conformity
  assessment.
- **Honour the LGPL boundary on `cpsolver`.** UniTime is Apache-2.0 and its solver is LGPL-3.0.
  Keep the solver behind a process or service boundary; do not static-link it into a closed
  component. State this in the licence annex before signature.
- **Do not promise registrar-grade decisioning on day one.** Read-only proposal mode first, as
  in **P11** — the pattern that got the staged-access posture right.

### Deliverables

- UniTime deployed or integrated against the client's SIS of record, with the LGPL boundary
  documented.
- An exception-intake agent in proposal-only mode, with policy nodes, criterion-level evidence
  and an appeal path.
- Accommodation-merge enforcement (`P496-1`) with a test suite that proves a required
  accommodation cannot be dropped.
- A registrar review queue, an audit trail, and turnaround-time baselines before and after.
- A licence annex covering Apache-2.0 / LGPL-3.0 / the SIS licence, written for procurement.

### Licence posture

**Clean, with one named boundary.** UniTime, Ed-Fi, CAS, Appsmith, `lrsql` and OpenJudge are
Apache-2.0; LangGraph and CrewAI are MIT; nothing forks the SIS. **`cpsolver` is LGPL-3.0** and is
the only copyleft component — keep it at arm's length. Where the client's SIS is `i-educar`
(GPL-2.0) the SIS stays on its own side of the integration boundary; where a closed SIS
derivative is the requirement, `gegok12` (MIT) is the only verified permissive base.

### Estimate

**8–10 weeks** to a proposal-only exception agent over a UniTime instance with policy nodes,
accommodation-merge enforcement, audit and a registrar queue. Add **4–6 weeks** to extend to
write-through scheduling, most of it approval and regression testing rather than code. **Do not
quote decisioning** — that is a separate engagement with a conformity assessment in it.

### Where it does not apply

- **Not for admissions or financial-aid decisioning.** Annex III high-risk; different pattern,
  different estimate, legal review first.
- **Not where the client has no timetabling pain.** UniTime earns its keep on conflict-heavy
  estates (large programme catalogues, shared rooms, exam weeks). A small college does not need
  it and `timetablely` will not sustain an engagement.
- **Not in LATAM public K-12 without checking the SIS first.** `i-educar` is the substrate there
  and it is GPL-2.0; the integration boundary has to be designed before anything is promised.
- **Not as a replacement for the SIS of record.** Every registrar in this market has one, it is
  usually proprietary, and proposing to replace it will end the conversation.

## P13 — Persona-stateless tutor for age-banded, affect-regulated markets (China, UAE, US state statutes)

### Why this pattern exists

**Added p894, from T14.** Consumer tutoring products retain learners with affective design: a
persistent named character, rapport, streaks, companion framing. **Three separate regimes now
make that design a regulated activity when it is aimed at children**, and they converge on the
same architecture:

- **China** — the **Interim Measures for the Administration of Anthropomorphic AI Interaction
  Services** (reported as CAC Order No. 21, issued 10 April 2026, **in force 15 July 2026**)
  cover services providing *sustained emotional interaction through a simulated human
  personality*. **Education is listed outside scope, but conditionally** — one analysis frames
  the carve-out as covering education services *that lack continuous emotional interaction*, and
  the Measures define neither "continuity" nor "emotional interaction". Inside scope:
  **virtual-partner/virtual-relative services may not be offered to minors at all**, guardian
  consent under 14, a minor mode with time limits, a prohibition on inducing emotional
  dependence, machine disclosure, self-harm intervention, and algorithm filing.
- **UAE** — a 25-prohibition classroom guide including an **under-13 prohibition**.
- **United States** — New York's **A 9190** (classroom AI limited to grade 9 and above, with
  diagnostic and special-education exceptions), California's **AB 1159** (no training on student
  data), and Oklahoma's and Maryland's human-oversight rules.

**The architecture that keeps a product out of China's scope is the same architecture the other
two regimes require.** That makes this one build rather than three, which is the entire point of
the pattern.

### Stack

| Component | Repo | Licence | Role |
|---|---|---|---|
| Age-banded RAG tutor over curriculum, not student data | `Zenglian990/AI_Tutor_Release` | MIT | The reference: **age-banded by design** (K-9), retrieval-over-curriculum rather than training-on-learners |
| Learner-state modelling without a character | `amosblomqvist/learnharness` | **AGPL-3.0** | **Read it, do not ship it.** The persistent knowledge graph is the capability that replaces persona continuity. AGPL — reference design only |
| Authored teaching flow that constrains the model | `ai-shifu/ai-shifu` | Apache-2.0 | A script the author controls is the control structure "no AI-only instruction" rules actually require |
| Orchestration with policy nodes | `langchain-ai/langgraph` | MIT | Age band, disclosure and session-limit checks as explicit nodes |
| Local or sovereign inference | `ollama/ollama` · `vllm-project/vllm` | MIT · Apache-2.0 | Keeps learner text in-jurisdiction; see **T6** |
| Content provenance / labelling | see **P6** | — | China content labelling and India's IT-Rules duties |

### The design rules that make it defensible

1. **Persona-stateless.** No named character, no continuity of personality across sessions, no
   simulated affect. **Pedagogical persistence lives in the learner model** — mastery, gaps,
   next item — which is strictly more useful and carries none of the regulatory surface.
2. **Disclose the machine on every surface**, not once at onboarding.
3. **Age band by construction, not by setting.** The band gates features at the orchestration
   layer; a configuration flag is not a compliance control.
4. **No dependency loops.** No streaks, no "I missed you", no engagement mechanics tuned on
   session frequency. Tune on mastery per unit of time instead — which is also what **P7**
   measures.
5. **Guardian surfaces where the regime requires them** — consent under 14, time limits, risk
   alerts — built once and switched on per jurisdiction.
6. **Self-harm routing to a human**, unconditionally, in every market.

### Deliverables

A persona-stateless tutor over the client's curriculum corpus; an age-band gate with tests; a
disclosure and guardian-surface layer switchable per jurisdiction; a jurisdiction matrix mapping
each control to the instrument that requires it; and a design note recording what was
deliberately **not** built and why — the document that answers the client's growth team when
they ask for streaks.

### Licence posture

Clean if `learnharness` stays a reading. `AI_Tutor_Release`, LangGraph and Ollama are MIT;
`ai-shifu` and vLLM are Apache-2.0. **`learnharness` is AGPL-3.0: reference design only, never
vendored.**

### Estimate

**6–8 weeks** for the tutor plus the age-band and disclosure layer on an existing curriculum
corpus. Add **2–3 weeks** per additional jurisdiction for the control mapping and guardian
surfaces — mapping, not rebuilding, if rule 5 was honoured.

### Where it does not apply

- **Not for adult corporate L&D**, where none of these regimes applies and affective design is
  simply a product choice. Use Mentingo (MIT) and **P1**.
- **Not as a substitute for counsel on a China launch.** Every source behind T14 is secondary;
  the CAC text was not reachable from this session, and no source addressed a tutoring product
  specifically. **Confirm scope before signature.**
- **Not where the client's differentiator *is* the character.** This pattern removes it; say so
  before the engagement starts rather than in week six.

---

## P14 — Offline-first literacy delivery on an Africa-origin platform, with the agent tier as studio IP (added p895)

### Why this pattern exists

**Added p895, from T16 and the first dedicated Africa supply-side leg.** Every prior Africa
entry in this KB measured demand. The supply measurement changes the shape of the engagement:

- 🟢 **There is exactly one adoptable Africa-origin platform**, and it is permissive:
  https://github.com/elimu-ai/webapp — **MIT** (byte-read `main/LICENSE`, 1,065 B),
  **41 ★ / 67 forks**, created 2016, **pushed 2026-11-17**. Early-grade literacy for
  out-of-school children, Tanzania/Kenya.
- 🔴 **There is no adoptable agent layer.** The published Africa-origin tutor
  (ACL AfricaNLP 2026's EduNaija, https://github.com/Eddy-Emmanuel/EduNaija-LLM) has **no
  licence on any of 8 candidate paths**, 1 ★, idle since 2025-12-22. The national-exam channels
  return a **~1 ★ ceiling with almost nothing licensed**.
- **So the division of labour is forced, not chosen: adopt the platform, build the agent tier.**
  The agent tier is **defensible studio IP** here, which should be reflected in how the
  engagement is priced.

**The binding constraint is connectivity, and it is the reason the obvious design fails.**
EduNaija's grounding is a **Tavily web search behind an OpenAI call** — it cannot run where this
pattern deploys. Retrieval must be local and the model must be local.

### Stack

| Component | Repo | Licence | Role |
|---|---|---|---|
| Platform core (Africa-origin) | `elimu-ai/webapp` | **MIT** (1,065 B, byte-read) | Content + Android app hosting for early-grade literacy. Regional provenance that wins a public-sector procurement |
| App delivery with no network | `elimu-ai/appstore` | **MIT** | **Installs and updates APKs with no app store and no connectivity.** The hardest part of this pattern, already solved |
| Device-level learning path | `elimu-ai/launcher` | **MIT** | Android launcher enforcing an EGRA/EGMA literacy-and-numeracy path 🟡 *(claim unverified — licence and metadata only)* |
| Levelling + recommendation | `elimu-ai/ml-storybook-reading-level` · `ml-storybook-recommender` | **MIT** | Reading-level estimation and story selection — the adaptive seam |
| Alternative / additional core | `learningequality/kolibri` | MIT | Offline-first by design; use where the deployment is not Sub-Saharan or where Kolibri's channel ecosystem is wanted |
| Pedagogy-bearing content | `oppia/oppia` | Apache-2.0 | Explorations with misconception handling — built for emerging markets |
| Local inference | `ollama/ollama` | MIT | **Mandatory, not optional.** No cloud model call is reachable at the edge |
| Local retrieval | `qdrant/qdrant` | Apache-2.0 | Curriculum corpus on-device/on-server — the FAISS-shaped component EduNaija was described as having and does not |
| Orchestration with policy nodes | `langchain-ai/langgraph` | MIT | Language routing, accommodation floor, escalation as explicit nodes |
| Eval gate | `acheamponge/wassce-benchmark` | MIT | **The only African-curriculum open evaluation asset this KB has found.** Measure before you claim |

### Wiring

```
[Android device, intermittent connectivity]
  elimu-ai/launcher  ──enforces──>  EGRA/EGMA path
         │
  elimu-ai/appstore  ──sideloads/updates──>  tutor APK   (no app store, no network)
         │
         ├── on-device: reading-level estimate (ml-storybook-reading-level)
         │              story selection       (ml-storybook-recommender)
         │
         └──[sync when a link appears]──> school/district server
                                            elimu-ai/webapp   (content + roster)
                                            ollama            (local model)
                                            qdrant            (curriculum corpus)
                                            langgraph         (tutor policy graph)
                                                 │
                                            wassce-benchmark  (pre-release eval gate)
```

**Sync is store-and-forward, and that is a design rule, not a limitation.** The tutor must be
correct with a stale corpus and no server; the server is where the model and retrieval live, the
device is where the session happens.

### Design rules

1. **Local retrieval over the client's own curriculum. Never general web search.** This is the
   specific correction the EduNaija reading produced: web grounding is both unreachable at the
   edge and unaccountable to a syllabus.
2. **Language routing is a first-class node.** EduNaija's one genuinely transferable idea is
   detect-then-answer-in-language across five Nigerian languages including **Nigerian Pidgin** —
   the language learners actually use, and the one a formal corpus omits.
3. **Keep a verifier node.** The main → verifier → escalate shape is sound; replace its web-search
   escalation with *retrieve-more-locally, then defer to a teacher*.
4. **Merge the statutory/programmatic accommodation baseline into agent state** so the model can
   add but not remove a required accommodation — `P496-1`, unchanged here.
5. 🔴 **Exclude `elimu-ai/ml-authentication` (MIT, 16 ★).** It is **student login by on-device
   face recognition — biometric identification of children**, and it is the one repo in the org
   idle since 2025-02-25. Remove it deliberately, record the removal in the design note, and use
   roster codes or teacher-mediated login instead.
6. **Gate the release on `wassce-benchmark`**, and publish the number. In a market with no
   licensed competition, a measured result is the differentiator.

### Deliverables

An offline-capable tutor over the client's curriculum corpus; a store-and-forward sync tier; the
language-routing and verifier graph; an accommodation-floor layer; a WASSCE-benchmark eval report
run before release; and a design note recording the face-recognition exclusion and the
store-and-forward contract.

### Licence posture

🟢 **Clean and permissive throughout** — MIT and Apache-2.0 only, every licence byte-read. This
is unusual for this KB: the LMS cores a studio normally inherits (Moodle GPL-3.0, Open edX and
Canvas AGPL-3.0) are copyleft, so **a closed, branded derivative is genuinely available here.**
Two cautions: `elimu-ai/web3-wiki` is **CC0-1.0** (public-domain dedication — no patent grant, no
warranty disclaimer), so do not pull it in as if it were MIT; and **nothing unlicensed from the
exam-channel census may be vendored**, above all
https://github.com/Seunope/aloc-endpoints (223 ★, no licence, third-party exam copyright).

### Estimate

**8–10 weeks** for the tutor, local retrieval and sync tier on top of a standing `elimu-ai` or
`kolibri` deployment. Add **3–4 weeks** per additional language beyond the first two (corpus
preparation dominates, not code). Add **2 weeks** for the eval gate if the client wants the
benchmark report as a deliverable.

### Where it does not apply

- **Not for urban, connected deployments** — the offline machinery is real cost. Use **P1** or
  **P2**.
- **Not for secondary-exam coaching without a licensed corpus.** The question banks that exist
  are unlicensed; a client must bring its own content or license it.
- 🟡 **`elimu-ai`'s source has not been read** (`Gap 486-J`). The licences, stars, forks and push
  dates are measured; the EGRA/EGMA path, the ML components' quality and the Aragon DAO
  governance are **descriptions, not findings**. **Read the source during scoping** — this
  pattern asserts the platform is adoptable on licence and activity evidence, not on a code
  review.
- **Not a Middle East pattern.** Despite the shared EMEA bucket, this pass found **no Middle East
  education repository at all**; Gulf demand is real and the supply leg there is untried.

---

## P15 — Branded, closed mobile client and components over the client's existing copyleft LMS (added p896)

### Why this pattern exists

**Added p896, from T17.** The commonest licence impasse in an education engagement: the client
runs **Moodle (GPL-3.0)**, **Open edX (AGPL-3.0)** or **Canvas (AGPL-3.0)**, wants a branded
product with proprietary differentiators, and legal stops the conversation at the server's
licence. The standing answers are LTI 1.3 (**P2**) and MCP (**P11**), and both are good — but
they both put your work *beside* the platform and leave the learner's actual interface untouched.

🟢 **The platform vendors publish the interface layer permissively.** Restoring 34 rows to
`repos/foundations.md` and sorting them by licence made this visible: the mobile clients, the
component frameworks, the design systems and the analytics stacks of these copyleft platforms
are **Apache-2.0 or MIT**, maintained first-party. **A closed, branded client over a copyleft
server is a supported architecture.**

### What you build on

| Layer | Repo | Licence | Role |
|---|---|---|---|
| Mobile client (Moodle) | https://github.com/moodlehq/moodleapp | **Apache-2.0** | Fork and brand; 1,007 ★, Moodle HQ-maintained. Licence at `main/COPYING.txt`. |
| Mobile client (Open edX) | https://github.com/openedx/openedx-app-android · https://github.com/openedx/openedx-app-ios | **Apache-2.0** | Same move on the other platform. |
| In-platform component | https://github.com/openedx/XBlock | **Apache-2.0** | Ship a proprietary learning component **inside** an AGPL LMS. Develop against https://github.com/openedx/xblock-sdk. |
| Design system | https://github.com/openedx/paragon · https://github.com/instructure/instructure-ui | **Apache-2.0** · **MIT** | Native-looking UI without touching platform code. |
| Interactive content | https://github.com/h5p/h5p-interactive-video · https://github.com/h5p/h5p-course-presentation · https://github.com/h5p/h5p-audio-recorder · https://github.com/h5p/h5p-speak-the-words | **MIT** (content types) | Compose the **MIT** content types; do **not** embed the **GPL-3.0** `h5p-php-library` in the closed part. |
| Content pipeline | https://github.com/h5p/h5p-cli | **MIT** | Makes generation scriptable — the step from demo to pipeline. |
| Agent tier | `ai-shifu` (Apache-2.0) or `Pyris` (MIT) behind https://github.com/Cvmcosta/ltijs | Apache-2.0 / MIT | Authored teaching flow, model layer kept swappable. |
| Analytics | https://github.com/davidpesce/moodle-logstore_xapi (**GPL-3.0**, in-platform plugin) → https://github.com/yetanalytics/lrsql (**Apache-2.0**) · https://github.com/openedx/openedx-aspects (**Apache-2.0**) | mixed | The plugin lives inside the copyleft platform where copyleft is expected; the LRS and your analysis stay permissive. |
| SSO | https://github.com/apereo/phpCAS (Moodle/PHP) · https://github.com/apereo/java-cas-client | Apache-2.0 | Join the institution's identity estate rather than minting accounts. |

### How to wire it

1. **Draw the licence boundary first, in writing.** Three zones: *copyleft server* (untouched,
   client-operated), *in-platform plugins* (`logstore_xapi`, any Moodle plugin — these are GPL
   and are published as such), and *your product* (forked Apache mobile client, Apache XBlocks,
   MIT components, the agent tier). Nothing crosses from zone 3 into zone 1 by linking.
2. **Fork the mobile client, do not rewrite it.** Rebrand, strip what the client does not need,
   add the agent surface. Keep the upstream remote: these apps track platform API changes, and
   that maintenance is the reason to start from them.
3. **Put the differentiator in an XBlock (Open edX) or a plugin-plus-LTI split (Moodle).** On
   Open edX the component runs in-platform under Apache. On Moodle, anything in-platform is GPL,
   so the proprietary part sits behind `ltijs` and only a thin GPL shim lives inside.
4. **Generate content through `h5p-cli`**, not by hand, and keep the generator in zone 3.
5. **Emit xAPI from day one** (`logstore_xapi` → `lrsql`) so **P7**'s outcome evidence exists
   without a later retrofit. On Open edX use `openedx-aspects` instead.
6. **Authenticate through the institution's CAS** before the first pilot cohort, not after.

### What makes it defensible

- 🟢 **Licence-clean by construction**, and provable: every zone-3 row above is Apache-2.0 or MIT,
  byte-read where the SPDX field was unreliable.
- 🟢 **The client keeps its system of record** — gradebook, enrolment, accreditation — so the
  engagement does not become a migration.
- 🟢 **First-party maintenance upstream.** You are forking repos maintained by Moodle HQ, the
  Open edX foundation and Instructure, not abandoned middleware.

### Estimate

**6–8 weeks** to a branded, agent-enabled mobile pilot over an existing LMS (fork, brand, agent
surface, SSO, xAPI). Add **3–4 weeks** for a first proprietary XBlock or LTI component. Add
**2 weeks** for the analytics tier if the client has no LRS.

### Where it does not apply

- 🔴 **Not where the client wants the *server* closed.** This pattern leaves the copyleft core in
  place. If a proprietary platform is the requirement, start from **Artemis**, **Kolibri**,
  **OpenOLAT** or **Mentingo** (**P1**).
- 🔴 **Not an EU proctoring or affect story.** Emotion inference in education is **prohibited in
  the EU since 2 February 2025**, and assessment/exam-access use is Annex III high-risk from
  2 December 2027 — see `verticals/solutions.md` and **P4**/**P9**.
- 🟡 **Verify the satellite licence per repo, per release.** The asymmetry is per-artefact and a
  relicence upstream closes this route for that platform (**T17** watch condition).
- 🟡 **`h5p-interactive-video` carries this KB's weakest licence evidence** — MIT on the search
  channel only, no licence file at twelve candidate paths. Confirm before it enters zone 3.

## P16 — Vernacular-medium second-language tutor, with the language relationship in the schema (added p898)

**The problem.** A client delivers instruction in a language that is neither English nor the language
being taught — a Bahasa-medium school teaching English, a Spanish-medium university teaching
Mandarin, a Portuguese-medium system teaching French. The default build (one LLM, one free-text
response field, a translated UI) collapses three distinct languages into one channel, and the
pedagogical scaffolding — *what the learner sees in their own language versus what they must produce
in the target language* — becomes a prompt convention that the model silently violates under load.

**Why this pattern exists separately from `P13`.** `P13` is persona-stateless tutoring for
age-banded, affect-regulated markets; its constraint is regulatory. This one's constraint is
**linguistic and structural**, and the fix is in the data contract. See **T20**.

### The recipe

| Tier | What to use | Licence | Why this one |
|---|---|---|---|
| **Schema contract** | [`brian901106/japanese-tutor-mugi`](https://github.com/brian901106/japanese-tutor-mugi) — **read it, reimplement it** | MIT (byte-read, 1,068 B) | The only verified implementation of target-language and native-language scaffolding as **separate typed fields**, streamed by partial-JSON parsing. Small and young — take the contract, not the codebase. |
| **Pedagogical frame** | [`Li-Evan/BloomTutor`](https://github.com/Li-Evan/BloomTutor) | MIT | Structures interaction by Bloom level, which gives the schema a second axis (cognitive level) alongside the language axis. |
| **Vernacular curriculum reference** | [`itsme-ganzu/belajar-ngoding-byGanzu`](https://github.com/itsme-ganzu/belajar-ngoding-byGanzu) | MIT | Worked example of reasoning-first drilling written natively in Bahasa Indonesia rather than translated into it. |
| **Pronunciation / production** | [`OpenPronounce/OpenPronounce`](https://github.com/OpenPronounce/OpenPronounce) | MIT | Open pronunciation assessment — the production half of a second-language loop, and the one tier where a generic LLM is weakest. |
| **Serving** | `ollama` or `vllm` + `litellm` | MIT / Apache-2.0 | Self-hosted inference. Required outright for EMEA sovereignty work and for any client that cannot export learner utterances. |
| **Learner state** | `qdrant` + a persistent store | Apache-2.0 | Carry per-learner error patterns across sessions. **`LearnHarness` is the reference design for learner-state modelling and is AGPL-3.0 — read it, do not link it.** |
| **Host platform** | Moodle (GPL) via `Faixiang/Moodle-MCP` (MIT) or `G36maid/moodle-mcp` (MIT) | MIT connectors over a GPL platform | The connector tier is permissive even where the platform is copyleft — **T17**'s third integration route. |

### The contract to implement

Every tutor turn returns **typed fields, not prose**:

- `target_text` — the utterance in the language being taught
- `native_hint` — scaffolding in the learner's own language
- `bloom_level` — the cognitive level this turn is pitched at
- `error_tags[]` — what the learner's previous production got wrong, for the state tier

🔵 **The whole point: `target_text` and `native_hint` are never the same field and never
concatenated.** That single constraint is what a translated English tutor cannot express, and it is
what makes the output renderable as two visually distinct channels, gradeable separately, and
analysable for whether the learner is actually producing target-language content or leaning on the
scaffold.

### Licence posture

🟢 **Permissive end to end** — MIT, Apache-2.0 and MIT-connectors-over-GPL. A closed, client-branded
derivative is clean, provided `LearnHarness` is read rather than linked and the Moodle tier stays on
the connector side of the boundary. This is the **second** pattern in this file (after `P14`) that is
permissive all the way down.

### Estimate and honest limits

**8–10 weeks** to a pilot on one language pair with one institution.

🔴 **What you are not getting.** Neither vernacular repo is substrate — they are a few dozen to a few
hundred stars and individually maintained. **The schema is the deliverable you are reusing; the
implementation is studio IP.** Budget accordingly, and do not price this as integration work.

🔴 **Unproven.** No learning-outcome study exists for the separate-fields contract. It is a
well-formed design argument supported by one working implementation, **not** an evidenced
intervention. Say so to the client rather than implying efficacy data that does not exist.


## P17 — AI grading assist over a BSD autograder, with the deterministic tier untouched (added p899)

### Why this pattern exists

A North American higher-ed client asking for "AI grading" is usually imagining the model marking
the work. **That is the one design that cannot be sold**, because it is simultaneously the
weakest pedagogically, the most exposed under FERPA and several US state statutes, and — from
2 December 2027 — an **EU AI Act Annex III high-risk** use if it determines learning outcomes.

🟢 **p899's measurement makes the alternative concrete: the deterministic grading substrate
already exists, under BSD, maintained by universities.** This KB previously recorded the grading
category as effectively empty; that was a keyword artefact (`898-G2`). It is not empty, and
nothing in the stack below needs to be built.

### Stack — every row licence byte-read 2026-11-18

| Layer | Repo | Licence | Why this one |
|---|---|---|---|
| **Grading platform** | https://github.com/Submitty/Submitty | **BSD-3-Clause** (`LICENSE.md@main`, `sha256₁₂ c123708cb4ef`) | 807 ★, RPI/RCOS, 12 years old, pushed 2026-11-18. Submission + autograding + **TA/manual grading with rubrics** in one system. **No copyleft, no patent clause, no enterprise carve-out — the derivative can be closed.** |
| **Notebook grading** | https://github.com/jupyter/nbgrader | BSD-3-Clause | For data-science courses; already shelved. Use instead of Submitty when the course is notebook-native |
| **Platform-free autograding** | https://github.com/ucbds-infra/otter-grader | BSD-3-Clause | Python **and R**, grades locally or in a container. Use when the client will not adopt a platform |
| **Sandboxed execution** | https://github.com/openedx/codejail *or* https://github.com/ls1intum/Ares | Apache-2.0 / MIT | **Never let an agent execute student code outside one of these** |
| **Learner model** | https://github.com/CAHLR/pyBKT | **MIT** (`LICENSE@master`, `sha256₁₂ ad0c7a38bf01`) | UC Berkeley CAHLR. Turns a response history into a per-skill mastery estimate — **the input that makes feedback adaptive rather than generic** |
| **Agent orchestration** | https://github.com/langchain-ai/langgraph | MIT | Policy checks become explicit, auditable graph nodes |
| **Rubric reference architecture** | https://github.com/virtualryder/edu-ai-agents | MIT | Deny-by-default authorisation, PII masking, HITL enforcement, tamper-evident audit, **deterministic rubric service rather than an LLM** |

🔴 **Do not reach for `PrairieLearn/PrairieLearn` here without reading `repos/foundations.md`
first.** Its Community Edition is **AGPL-3.0** and `apps/course-agent/` — the AI tier, i.e.
exactly this pattern's layer — is **proprietary Enterprise Edition**: production use needs a paid
subscription and the licence **assigns your modifications to PrairieLearn, Inc.** This KB
published that row as "MIT · Permissive" until p899.

### How it wires together

1. **Submitty grades deterministically and remains the system of record for the mark.** The agent
   never writes a grade. This is the load-bearing rule.
2. The agent reads `(submission, test results, rubric)` and drafts **feedback and a suggested
   rubric selection**, surfaced to the TA as a proposal.
3. **The TA accepts, edits or rejects** in Submitty's existing manual-grading UI. The accept/edit
   signal is the audit record *and* the evaluation dataset.
4. `pyBKT` consumes the mark history and returns per-skill mastery, which selects **what the
   feedback emphasises** — not what the mark is.
5. Every agent action is logged with the model version and prompt hash, per `edu-ai-agents`.

### The design rule that makes it defensible

🔵 **The mark is deterministic; the prose is generated; a human moves between them.** Under this
split the AI system is not "determining learning outcomes" — which keeps it out of Annex III
high-risk classification, satisfies the US state rules that prohibit AI-only grading decisions,
and gives the institution an appeal story that survives a student challenge. **It is also the
only split for which you can show the client a measured accept-rate.**

### Deliverables

- Submitty deployment + the feedback-assist service as a separate process (clean licence boundary)
- Rubric-selection evaluation harness with TA accept/edit/reject as ground truth
- `pyBKT` mastery service with a per-skill dashboard
- FERPA data-flow map and a written Annex III classification argument

### Licence posture

🟢 **Fully closable.** Submitty BSD-3-Clause, otter-grader BSD-3-Clause, nbgrader BSD-3-Clause,
pyBKT MIT, LangGraph MIT, edu-ai-agents MIT, codejail Apache-2.0. **No copyleft anywhere in the
stack**, which is rare in education and is the reason to prefer this composition over the
Open edX/`edx-ora2` route (AGPL-3.0) when the client wants to own the result.

### Estimate

**6–8 weeks** to a pilot on one course with real TAs. Add 3–4 weeks if Submitty is not already
deployed. 🔴 **Unproven:** no published study shows AI-drafted rubric feedback improves outcomes.
Sell the **TA time saved and the audit trail**, both of which you can measure in the pilot, and
do not imply learning-gain evidence that does not exist.

### Where it does not apply

K-12 in jurisdictions requiring parental opt-in before any AI touches student work (Florida's
2026 board rules), and any client who wants the mark itself generated — decline that scope and
explain why in one paragraph.

## P18 — Zero-provisioning teacher coaching over WhatsApp (added p899)

### Why this pattern exists

Every other pattern in this file assumes the learner or teacher has a provisioned device, an
account and a browser. **For a large part of the market that assumption is the project risk**, and
it is the reason public-sector education pilots stall between PoC and deployment.

🟢 **p899 verified the first open agent in this KB that removes the assumption entirely.**
https://github.com/Orenda-Project/rumi-platform (**Apache-2.0**, `LICENSE@main`, 11,287 B,
`sha256₁₂ c589d95090ce`) runs **wholly on WhatsApp**: no app to install, no login, no training
day. It delivers classroom coaching, reading assessment and lesson plans by **text and voice
note**, in **15 languages**, with voice transcription via Meta's MMS-ASR, and is explicitly built
to be cloned and run on your own API keys.

🔵 **Its target market is South Asia; the channel argument is at least as strong in LATAM**, where
WhatsApp is the dominant messaging surface and this KB has repeatedly recorded an
adoption-ahead-of-governance asymmetry among teachers (Brazil 56%, Chile 55%, Colombia 53% teacher
AI use against an OECD average of 36%).

### Stack

| Layer | Repo | Licence | Role |
|---|---|---|---|
| **Channel + agent** | https://github.com/Orenda-Project/rumi-platform | **Apache-2.0** | WhatsApp transport, voice-note handling, coaching flows. **Patent grant included** |
| **Local/sovereign inference** | https://github.com/ollama/ollama *or* vLLM | MIT / Apache-2.0 | Keeps teacher messages in-country where a ministry requires it |
| **Curriculum grounding (UK/EMEA)** | https://github.com/oaknational/oak-ai-lesson-assistant | **MIT** (code) | Curriculum-aligned lesson generation from a national curriculum body. 🟡 Content is **Open Government Licence**, trademarks excluded |
| **Curriculum grounding (Brazil)** | https://github.com/bncc-dev/bncc-pacotes | 🔴 `NOASSERTION` — **byte-read before use** | BNCC (Brazilian national curriculum) as packages + an MCP server. 10 ★ — thin, verify the grant |
| **Brazilian public data** | https://github.com/Mcp-Brasil/mcp-brasil | **MIT** | 1,865 ★. MCP over 70 Brazilian public-sector APIs — **the largest LATAM-origin asset this KB has verified** |
| **Offline fallback** | https://github.com/learningequality/kolibri | MIT | For the schools where even WhatsApp is intermittent |

### How it wires together

1. Teacher sends a voice note or text to a WhatsApp number. **No onboarding step exists.**
2. Rumi transcribes (MMS-ASR), routes to the coaching flow, and replies in the teacher's language
   — by voice if the teacher used voice.
3. Lesson-plan requests are grounded against the **national curriculum** package for that
   jurisdiction (Oak for England, `bncc-pacotes` for Brazil), not against model recall.
4. Inference runs locally via Ollama/vLLM where data residency is a procurement condition.
5. Usage is metered per school for the ministry's reporting, per **P8**.

### The design rules that make it defensible

- 🔴 **Teacher-facing only.** Do not put this channel in front of under-18 learners: WhatsApp's own
  age floor, the UAE under-13 prohibition and the US state parental-opt-in rules all land here.
  **Coaching the teacher is the defensible scope** and is also where the measured workload saving
  is (Oak reports teachers saving ~3.5 hours a week with Aila — **Oak's own figure, not
  independently verified**).
- 🔵 **Curriculum grounding is the quality control.** The reason to ground on BNCC or the Oak
  curriculum is not pedagogy theory — it is that a ministry will reject generated material that
  cannot be traced to its own standard.
- 🟡 **Meta dependency is a real risk.** The WhatsApp Business API terms and pricing are outside
  the client's control and outside this licence stack. Say so in the proposal.

### Deliverables

- Self-hosted Rumi deployment on the client's WhatsApp Business number and own API keys
- Curriculum grounding pack for the jurisdiction + traceability from reply to standard
- Teacher-cohort usage and workload-saving measurement
- Data-residency note covering transcription and inference

### Licence posture

🟢 **Closable.** Rumi Apache-2.0 (with patent grant), Ollama MIT, Kolibri MIT, mcp-brasil MIT, Oak
code MIT. 🔴 **Two conditions:** Oak's *content* is Open Government Licence and its marks are
excluded from the grant; `bncc-pacotes` reports `NOASSERTION` and **must be byte-read before it
reaches a build**.

### Estimate

**6–8 weeks** to a pilot with one teacher cohort. 🔴 **Honest limits:** Rumi is **25 ★ and young**
— this is a reference implementation and a channel argument, **not substrate**. Budget the
integration as studio IP, pin the version, and expect to maintain the fork.

---

## P19 — Standards-native assessment delivery a client can keep closed: QTI 3 in, xAPI out, no copyleft anywhere (added p900)

**The problem this solves.** A client has existing assessment content and wants an AI tier that
authors, delivers and scores items — **and wants to own the result**. Every route this file
previously offered ran through a copyleft platform: Open edX's `edx-ora2` (AGPL-3.0), Moodle
(GPL-3.0), or `Citolab/qti-components` (GPL-3.0) for the player itself. 🔵 **p900 shelved the
pieces that make an end-to-end permissive route exist for the first time.**

### The stack — every grant byte-read, every row verified 2026-11-18

| Layer | Repo | Grant | Why this one |
|---|---|---|---|
| Item format in | [`longsightgroup/qti3`](https://github.com/longsightgroup/qti3) | **MIT** (1,071 B) | Renders **and scores** QTI 3. TypeScript core with **zero third-party runtime dependencies**, plus converters for the client's older QTI. The permissive alternative to `Citolab/qti-components` (GPL-3.0) |
| Item authoring | [`satvik314/educhain`](https://github.com/satvik314/educhain) | MIT | Generates MCQs and assessments from source content. 🟡 Idle since 2026-05-29 — vendor it, do not track it |
| Learner model | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) + [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | MIT + MIT | Neural knowledge tracing **with its classical baseline beside it**. Ship both: pyBKT is what you show when the client asks whether the neural model earns its cost |
| Integrity | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | MIT | Post-hoc similarity across submissions. 🔵 **Deliberately not proctoring** — see the regulatory note below |
| Evidence out | [`adlnet/xapi-spec`](https://github.com/adlnet/xapi-spec) + [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Apache-2.0 + Apache-2.0 | The normative spec to validate against, and a SQL-backed LRS to write to |
| Legacy delivery | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | MIT | Ships the result into the client's existing LMS **without re-authoring**, because their content is already SCORM |
| Platform seam (optional) | [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | MIT | Talks to AGPL-3.0 Canvas **over its API**, so the platform's licence does not reach your code |

### Wiring

1. **Ingest** the client's QTI 1.2/2.x through `qti3`'s conversion tooling; keep QTI 3 as the
   single internal item representation. Authoring agents emit QTI 3, never a bespoke JSON.
2. **Author** with `educhain` behind a review queue. 🔴 Generated items are *drafts*: the
   human-approval step is the deliverable, not a nicety — several jurisdictions in **T1**
   regulate automated assessment decisions, not automated assessment *content*.
3. **Deliver and score** in the browser with the `qti3` Web Component. Deterministic scoring
   stays in QTI's own response processing; **the AI tier never decides the grade**, which is
   what keeps this outside the Annex III high-risk box described below.
4. **Model** the learner with `pykt-toolkit`, fed from the scored responses; hold `pyBKT` as the
   baseline in the same evaluation harness.
5. **Emit** every interaction as xAPI statements into `lrsql`, validated against `xapi-spec`.
   This is the evidence layer that answers *"did it help"*, which **T23** argues clients now ask
   for before renewal.
6. **Integrate** by either publishing a SCORM package via `scorm-again` into whatever LMS they
   run, or talking to Canvas through `canvasapi`. 🔵 **Neither path forks a copyleft platform.**

### Licence posture

🟢 **MIT and Apache-2.0 end to end. There is no GPL, AGPL or LGPL component in this pattern** —
the second pattern in this file (after **P14**) that is permissive throughout, and the first one
that is permissive throughout *at enterprise scale* rather than on a single offline platform.
The studio's agent tier, the item bank and the learner model can all be client-owned IP.

### Regulatory posture — read this before scoping

🔴 **Scoring an exam that affects progression is an EU AI Act Annex III high-risk use.** The
Digital Omnibus (**Regulation (EU) 2026/1744**) moved those obligations to **2 December 2027**,
which is scoping time, not an exemption — and **transparency duties under Article 50 already
apply**. Two design choices follow and both are in the wiring above: **deterministic scoring
owns the grade**, and **integrity is post-hoc comparison (`dolos`) rather than proctoring**,
because exam monitoring carries its own Annex III exposure and, where biometric or emotion
inference is involved, runs into an outright prohibition in EU schools.

### Estimate

**8–12 weeks** to a pilot with one course's item bank converted, authoring behind review, live
delivery and an LRS receiving statements. The QTI conversion of the client's legacy bank is the
schedule risk and the part to timebox first — `qti3`'s converter handles the common cases and
not the exotic ones, and which of those a client has is not knowable from a statement of work.


## P20 — Permissive synchronous classroom with an AI teaching assistant the client can keep closed (added p901)

**The gap this closes.** Every synchronous-delivery pattern in this file so far routes through
BigBlueButton (`LGPL-3.0`) or assumes the client already runs Zoom/Teams. `p901` verified
`jitsi/jitsi-meet` at **Apache-2.0, 30,255★, 8,134 forks, pushed 2026-11-18** — which makes an
**end-to-end permissive live classroom** buildable for the first time in this KB. This is the
second pattern here (after **P14**) whose licence posture is permissive from top to bottom, and
the first that is not offline-first.

**Who it is for.** A client who teaches live — a university running tutorials, a training
provider, a ministry running teacher CPD — who wants session transcripts, attendance and
comprehension signals turned into teaching feedback, and who intends to keep the resulting
product closed or resell it. The copyleft route makes that last part expensive; this one does not.

### The stack, with the grant on every tier

| Tier | Component | Licence | Why this one |
|---|---|---|---|
| Live classroom | [`jitsi/jitsi-meet`](https://github.com/jitsi/jitsi-meet) | 🟢 `Apache-2.0` (byte-read `12,596 B`, `eae52e200cd8`) | Finished, self-hostable conferencing app with its own mobile SDKs. `30,255★`. **Not** BigBlueButton: BBB is `LGPL-3.0` and purpose-built for classrooms, which is the better fit *unless* the client needs to ship a closed derivative |
| Recording / capture | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟡 `ECL-2.0` | `513★`, pushed `2026-11-18`. Apache-derived with a patent clause; fine alongside, keep it a separate service |
| Transcription | `faster-whisper` | 🟢 `MIT` | Already the transcription tier elsewhere in this file; feed it Opencast output or Jitsi's recording hook |
| Mastery model | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 `MIT` | UC Berkeley CAHLR Bayesian Knowledge Tracing. **Do not invent a comprehension score** — this is the evidence-backed one, and it is the tier a general-purpose campus LLM stack does not provide |
| Spaced review | [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 `MIT` | Turns the mastery estimate into a review schedule instead of a dashboard nobody reads |
| Teacher console | [`appsmithorg/appsmith`](https://github.com/appsmithorg/appsmith) | 🟢 `Apache-2.0` | Human-in-the-loop queue. The teacher approves or discards every generated signal |
| LMS of record | Moodle / Open edX / Canvas | 🔴 `GPL-3.0` / `AGPL-3.0` | **Integrate over LTI 1.3 or REST. Do not fork.** This is the `G1` gate below |
| Agent tier | Studio IP | — | Closed, because every tier above it is permissive |

### Wiring

1. **Jitsi emits, it does not host your logic.** Self-host Jitsi Meet; use its recording and
   webhook hooks to drop session artefacts into object storage. Keep your services *outside*
   the Jitsi tree — the Apache-2.0 grant is clean, and forking is what loses you that.
2. **Opencast or Jitsi recording → `faster-whisper` → a per-session transcript** with speaker
   turns. Timestamps are what later make a comprehension signal attributable to a moment.
3. **Transcript + in-session quiz responses → `pyBKT`.** Mastery is estimated per skill from
   observed responses. 🔴 **The transcript alone is not evidence of mastery** — if the client
   has no in-session questioning, add it before promising a mastery number.
4. **`pyBKT` → `fsrs4anki`** for each learner's review schedule.
5. **Everything a teacher sees lands in Appsmith first.** Generated summaries, flagged
   learners and suggested re-teach points are proposals until a human accepts them.
6. **Write back to the LMS over LTI 1.3 / REST only.** Grades and completion go back through
   the documented interface. The LMS stays unmodified and its copyleft never reaches you.

### Licence posture of the result

🟢 **The client can keep the agent tier and the console closed.** Jitsi (Apache-2.0),
`faster-whisper`, `pyBKT`, `fsrs4anki` (MIT) and Appsmith (Apache-2.0) impose attribution, not
source disclosure. 🔴 **The one gate: the LMS.** Moodle is GPL-3.0 and Open edX/Canvas are
AGPL-3.0 — integrate across a network interface and you are fine; fork or link and the
derivative-work question is live. **Run `G1` before quoting.**

🔴 **Add a CI check, not a memo** — see **T24**. If the build ever vendors a repository whose
grant is path-dependent, assert in the pipeline that the restricted paths are absent from the
artifact. For this stack that check is currently trivial (no multi-grant component), which is
exactly when it is cheap to put in place.

### Estimate

**8–10 weeks** to a production pilot for one faculty or one training programme: 2 weeks Jitsi
self-hosting and recording pipeline, 2 weeks transcription and session modelling, 2–3 weeks
`pyBKT` calibration against the client's actual assessment data (**this is the step that slips**
— it needs historical response data, and if the client has none, the model has nothing to fit),
1–2 weeks Appsmith console, 1 week LTI write-back. 🔵 Jitsi self-hosting at class scale is the
underestimated line: budget real infrastructure time for TURN/JVB capacity.

### Where it sells

🟢 **APAC, strongly** — see `intel/market.md`: an NTU-shaped client whose undergraduates already
have a frontier general-purpose stack does not need another assistant; it needs the mastery and
assessment tier that stack does not provide, which is precisely tiers 4–6 here. 🟢 **EMEA** —
the whole stack is self-hostable, which answers the data-residency and sovereignty question
(Council of the EU `14902/26`) directly, and Jitsi self-hosted keeps session content in the
client's own infrastructure. 🟡 **North America** — viable, but `pyBKT` and `Submitty` land
better where the client already runs their own LMS; check state AI-in-education rules first
(**NC Session Law 2026-41**, **NY A 9190** restricting classroom AI to grade 9+, **CA AB 1159**
on student data and model training — AB 1159 matters here because transcripts are student
data). 🟢 **LATAM** — the permissive posture and self-hostability fit the budget and the
26%-have-a-formal-AI-strategy governance gap; pair with the P14 offline-first pattern where
connectivity is the binding constraint, since **this pattern assumes live video and therefore
assumes bandwidth.**


## P21 — Notebook-native course with deterministic marking and an AI feedback tier, permissive end to end (added p902)

**The gap this closes.** Every assessment pattern in this file routes through a platform — Submitty,
PrairieLearn, Open edX ORA, Artemis. None of them addresses the case where **the artefact the student
submits is a notebook**, which is how CS, data science, engineering and quantitative social science
are actually taught. `p902` verified the whole tier (`repos/trending.md` `902-R1`), and it is the
**only tier in this KB that is permissive from top to bottom with no copyleft and no enterprise
carve-out** — compare the LMS tier, where every incumbent is GPL or AGPL.

**Who it is for.** A university faculty, a bootcamp or a corporate upskilling programme teaching
Python/R at scale, that wants per-student environments with no install day, marking that is
reproducible enough to survive an appeal, and AI feedback that a lecturer signs off — while keeping
the result as their own IP.

### The stack, with the grant on every tier

| Tier | Component | Licence | Why this one |
|---|---|---|---|
| Student environment | [`jupyterhub/binderhub`](https://github.com/jupyterhub/binderhub) | 🟢 `BSD-3-Clause` (byte-read `1,522 B`, `611f531642d5`) | `2,673★`. A git repo becomes a running environment from a URL. **No lab image, no install day** |
| Auth + persistence | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 `BSD-3-Clause` | Use **instead of** BinderHub when students need identity and persistent storage; use **both** when you want ephemeral try-it plus a graded home |
| Content as text | [`mwouts/jupytext`](https://github.com/mwouts/jupytext) | 🟢 `MIT` (title line byte-read; ★ **unmeasurable**, `902-F3`) | Notebooks as `.py`/`.md`. **This is the tier that makes the curriculum reviewable in a pull request** — without it, course content is a blob and no agent can propose a diff to it |
| Assignment flow | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 `BSD-3-Clause` | `1,370★`. Release / collect / autograde / feedback. The course standard |
| Deterministic marking | [`computationalmodelling/nbval`](https://github.com/computationalmodelling/nbval) | 🟡 `BSD-3-Clause` — **SPDX `NOASSERTION`**, resolved from clause structure; Univ. of Southampton | `453★`. Validates a notebook against stored outputs under `pytest`. 🟢 **No model in the loop, so the mark is reproducible and appealable** |
| Language-agnostic autograding | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 `BSD-3-Clause` | Add when the course is **R as well as Python**, or when submissions arrive via Canvas/Gradescope |
| Sandboxing | [`openedx/codejail`](https://github.com/openedx/codejail) | 🟢 `Apache-2.0` | **Before any agent or grader executes student code.** Non-negotiable |
| Notebook corpus | [`nbgallery/nbgallery`](https://github.com/nbgallery/nbgallery) | 🟢 `MIT` | `150★`. Sharing, search, usage analytics and health checks across the course's notebooks |
| Mastery model | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 `MIT` | Per-skill mastery from observed responses. UC Berkeley CAHLR |
| Teacher console | [`appsmithorg/appsmith`](https://github.com/appsmithorg/appsmith) | 🟢 `Apache-2.0` | The approval queue. Nothing generated reaches a student unreviewed |
| LMS of record | Moodle / Canvas / Open edX | 🔴 `GPL-3.0` / `AGPL-3.0` | **LTI 1.3 / REST only.** Grades out, roster in, no fork |
| Feedback agent | Studio IP | — | Closed, because every tier above is permissive |

🔴 **Two repos to read and not ship**, both verified this pass: `parmentelat/nbautoeval` is
**`CC-BY-SA-4.0` on executable code** (no patent grant, ShareAlike reaches derivatives — an exercise
bank built on it cannot stay closed) and `pyta-uoft/pyta` is **`GPL-3.0`**. PyTA's *idea* — linter
errors phrased for a beginner — is worth copying into the feedback prompt; its code is not worth
linking.

### Wiring

1. **Make the course a repository.** Notebooks are committed as text via `jupytext`; the `.ipynb` is
   a build artefact, never the source of truth. 🟢 This single decision is what makes every later
   step possible: diffs, review, CI, and an agent that proposes curriculum changes as pull requests.
2. **`nbgrader` owns the assignment lifecycle.** Author one source notebook per assignment with
   solution and test cells; release the student version; collect submissions.
3. **Mark deterministically first, with `nbval` under `pytest` inside `codejail`.** The numeric mark
   comes from here and **only** from here. 🔴 **Never let the model assign the grade** — this is the
   `P17` split, and in the US it is also a statutory line (**Oklahoma SB 1734** bars AI used solely
   for grading).
4. **Then, and only then, the feedback agent runs** — over the submission, the failing test output
   and the rubric — and writes *prose*, not a score: what the student got wrong, the beginner-phrased
   version of the error (the PyTA idea), and the next exercise.
5. **Every generated comment lands in the Appsmith queue** for the lecturer to accept, edit or
   discard. Acceptance rate is the metric that tells you whether the tier is working.
6. **`pyBKT` consumes the deterministic per-test outcomes**, not the model's opinion, so the mastery
   estimate stays defensible.
7. **Grades go back over LTI 1.3.** The LMS is never forked, so its copyleft never reaches the studio
   tier.
8. **`nbgallery` sits across the corpus** for search, usage analytics and health checks — and its
   health-check runner is the natural hook for an agent that *repairs* a notebook broken by a library
   upgrade rather than just flagging it. 🔵 That maintenance job is the recurring-revenue half of this
   engagement.

### Licence posture of the result

🟢 **Permissive end to end: BSD-3 (BinderHub, JupyterHub, nbgrader, nbval, otter-grader), MIT
(jupytext, nbgallery, pyBKT), Apache-2.0 (codejail, Appsmith).** Attribution only — no source
disclosure, no patent surprises, no enterprise carve-out of the kind `p899` found in PrairieLearn's
`apps/course-agent/`. **The client owns the feedback agent outright.** 🔴 **Two gates before quoting:**
the LMS stays across a network interface (`G1`), and **`riiid/ednet` must not be used to train
anything that ships** — it is `CC-BY-NC-4.0`, research only (`T25`, `902-R2`). Validate against
EdNet in a study; train on the client's own response data.

### Estimate

**6–8 weeks** to a production pilot for one course: 1 week BinderHub/JupyterHub on the client's
cluster, 1 week converting existing notebooks to `jupytext` and into git (🔵 **this is the step
clients underestimate** — the existing notebooks are usually undocumented and non-reproducible, and
fixing that is the real work), 1–2 weeks `nbgrader` + `nbval` test authoring per assignment set,
1 week `codejail` sandboxing and CI, 1–2 weeks feedback agent and Appsmith queue, 1 week LTI
write-back. `pyBKT` calibration is a further 2 weeks **and only if the client has historical response
data** — without it, leave the mastery tier out of scope rather than fitting a model to nothing.

### Where it sells

🟢 **North America, strongest** — the whole tier is built by its universities (Southampton aside:
Berkeley, Toronto, Michigan, RPI, CMU), the buyer already runs JupyterHub in most CS faculties, and
the 66%-institution-wide figure says they are past pilots and stuck on rollout. Check **CA AB 1159**
(student data must not train models) and **NY A 9190** (classroom AI restricted to grade 9+, so K-8
is out) before scoping. 🟢 **EMEA** — fully self-hostable, which answers the sovereignty question
(Council of the EU `14902/26`) without a vendor conversation; the UK's January 2026 school safety
standards are a procurement gate you can sell *against* rather than around. 🟡 **APAC** — strong in
higher ed, and the one region where the client may already have a frontier general-purpose stack
(NTU): sell the **deterministic marking and mastery** tiers, which that stack does not provide.
🟡 **LATAM** — the permissive, self-hostable posture and zero licence cost fit the ~USD 18.2M
rest-of-region market reality, but **BinderHub assumes bandwidth and a Kubernetes cluster**; where
neither holds, use `P14`'s offline-first pattern instead and keep only `nbgrader` + `nbval` as a
local marking tier.

## P22 — National-curriculum corpus as an agent-addressable skill tree, re-authored so the client owns the grant (added p903)

**When a client asks for this.** A ministry, a national exam board or a large private school group
has the curriculum — syllabus documents, approved textbooks, past papers — and wants an AI tutor
over *their* curriculum, not a generic one. `p903` found this already being done at national scale
and done in a way no studio can deliver: `revolover00/Bakloriya-AI-SKILLS` carries **Egypt's
complete approved 2026/2027 curriculum, 300 units across four stages, 28 MB**, with **no licence on
any of 12 byte-read paths** and no software at all. This pattern takes **its schema** — which is
free to copy — and supplies everything it lacks. See `intel/trends.md` **T26**.

### What you copy, and what you must not

🟢 **Copy the decomposition schema.** It is the most complete worked example of national-curriculum
sharding this base has measured, and a directory structure is not the copyrightable part:

```
skills/<stage>/<grade>/<term>/<subject>/
    SKILL.md        # routing index for the subject: the chapter tree
    glossary.md     # terms and core concepts
    patterns.md     # exam question patterns + solution keys
    cheatsheet.md   # the night-before summary
    chapters/ch01/  # one directory per teaching unit
             ch02/
```

🔴 **Do not copy the content, and do not vendor the repository.** 28 MB under default
all-rights-reserved copyright. Run **`G1`** before anything else; the corpus licence is the single
question that decides whether this engagement is an integration or a re-authoring, and for every
MENA corpus `p903` measured the answer was re-authoring.

🔴 **Do not copy its runtime, because it does not have one.** Its only control against hallucination
is a sentence in a prompt — *stay inside the syllabus, do not mix grades or terms.* That is not a
compliance story under EU Annex III or Vietnam's **Decision 33/2026/QD-TTg**, and it is the gap this
pattern's middle tier fills.

### The stack

| Tier | Component | Licence | Why this one |
|---|---|---|---|
| Corpus | **Client-owned curriculum**, re-authored into the schema above | Client's | The grant problem solved at the source. Where the client has no digital corpus, the permissive in-language assets in `repos/foundations.md` seed it: https://github.com/deeplearningturkiye/turkce-yapay-zeka-kaynaklari (**MIT**, 2,432 ★, Turkish) and https://github.com/barnamenevisi/free-resources (**MIT**, 1,297 ★, Persian) |
| Path-scoped retrieval | https://github.com/qdrant/qdrant | Apache-2.0 | **This is the tier Bakloriya does not have.** Payload filtering enforces `stage`/`grade`/`term`/`subject` as a *hard* filter, so "do not mix grades or terms" becomes a query constraint instead of a request |
| Prerequisite structure | https://github.com/HKUDS/LightRAG | MIT | A curriculum *is* a prerequisite graph; `SKILL.md`'s chapter tree is the edge list. Use it so a stuck learner is routed backwards to the missing prerequisite, not re-shown the same unit |
| Agent tier | https://github.com/langchain-ai/langgraph or https://github.com/pydantic/pydantic-ai | MIT | Explicit nodes per teaching move — explain, worked example, graded probe, distractor explanation — mirroring what `patterns.md` already encodes per subject |
| Model serving | https://github.com/ollama/ollama (on-prem) or https://github.com/vllm-project/vllm (campus scale) | MIT / Apache-2.0 | Ministry work is data-residency work. Keep inference inside the client's boundary |
| Durable loops | https://github.com/temporalio/temporal | MIT | A term-long tutoring relationship is a long-running workflow, not a chat session |
| Delivery, connected | Moodle / Open edX over **LTI 1.3** | integrate, never fork | `G1`. The corpus and agent tier stay yours across the interface |
| Delivery, offline | https://github.com/learningequality/kolibri (MIT) or https://github.com/Crosstalk-Solutions/project-nomad (Apache-2.0) | MIT / Apache-2.0 | Where connectivity is the binding constraint, ship the corpus to the device and keep the agent tier optional |
| Audit trail | xAPI / LRS tier in `repos/foundations.md` | permissive | Annex III and Decision 33/2026/QD-TTg both want *per-learner, per-decision* records. Emit them from the agent nodes, not from the LMS |

### The zero-inference tier, and why it is a separate decision

`p903` also verified https://github.com/SalehGNUTUX/GT-MISHKATKIDS (**GPL-3.0**, byte-read 34,819 B,
pushed 2026-11-18): an Arabic early-years system that is **fully local, offline, and runs no AI at
runtime**, shipped as PWA, `AppImage`/`DEB`/`RPM` and Android `APK`, with the child's data never
leaving the device. Its loop is inverted — the child teaches an amnesiac robot (the protégé effect).

🟢 **Take the architecture as a design, for the early-years band only.** For ages 4–10 a
zero-inference build is usually *better*: no API bill, no egress, nothing to sign a DPA over, and no
hallucination surface. Pair it with the corpus tier above — the corpus drives a connected tutor for
secondary, a zero-inference consolidation loop for primary.
🔴 **GPL-3.0: study and reimplement, do not embed.** It is deployable and forkable as a system; it is
not a component for a closed deliverable. And its content sits in an explicit Islamic doctrinal
frame with Qur'anic recitation as a first-class module — portable architecture, non-portable content.

### Build estimate

| Phase | Work | Duration |
|---|---|---|
| 0 | **`G1` licence pre-flight on the client's curriculum corpus** and on every seed asset | 3–5 days |
| 1 | Schema adoption + ingestion of one stage/one term as the vertical slice | 2–3 weeks |
| 2 | Path-scoped retrieval (Qdrant payload filters) + prerequisite graph from `SKILL.md` trees | 2–3 weeks |
| 3 | Agent tier: teaching-move nodes, distractor explanation, graded probes | 3–4 weeks |
| 4 | Audit trail, evaluation harness, human-review console (Appsmith) | 3–4 weeks |
| 5 | Corpus scale-out to remaining stages and terms — **the long pole, and it is curriculum-writing labour, not engineering** | 8–16 weeks, parallelisable |
| | **Engineering total to first regulated pilot** | **10–14 weeks** |

🔵 **Price phase 5 honestly and separately.** Bakloriya's 300 units are the measurement of what the
content tier actually costs: a single maintainer produced them in under a month using models, which
means the labour is real but model-assisted, and a client who already has approved syllabus
documents is most of the way there. **The engineering is the 10–14 weeks; the corpus is a content
programme**, and conflating them is how this kind of engagement is underquoted.

### Regional notes

🟢 **EMEA (MENA first).** This is the pattern for the Gulf and North Africa. `p903` measured the
supply side: Saudi Arabia's Qiyas channel returns **12 repositories, all 0 ★, none licensed**,
against a demand side of 50 new curriculum units for 2026-27 and **240,000 teachers in training**;
Egypt has a complete national corpus with no grant. **There is nothing to adopt and the demand is
funded.** What a ministry is buying is the institutional engineering MENA's single-maintainer
projects do not have — licensing, evaluation, accessibility, audit trail, maintenance. Keep
`DigComp 3.0` on the EMEA checklist as an open question (`intel/market.md`): if AI-literacy
obligations are in scope, obtain the document before quoting.
🟡 **APAC.** The same stack, with the compliance tier promoted to the front: Vietnam's
**Decision 33/2026/QD-TTg** names education uses as high-risk with a **72-hour incident clock** and
pre-deployment registration, which makes the audit trail a phase-1 deliverable rather than phase 4.
🟢 **LATAM — rewritten `p904`, and it is now the *reference* region for this pattern rather than a
localisation afterthought.** The note here read *"LATAM supply is unchanged — Brazil-only, two small
repos"*; the Spanish/Portuguese channel falsified that. **Brazil has already executed this pattern
properly**: `bncc-dev/bncc-dados` publishes the national curriculum as 1,721 verified records with
per-record provenance, a reproducible pipeline, a Zenodo DOI and an `llms.txt` agent contract, under
**MIT code + CC BY 4.0 data**. 🔵 **So in LATAM, do not re-author — adopt the spine and build the
agent tier**, which is the inverse of the MENA instruction above and the reason **P23** exists as a
separate pattern. Elsewhere in the region, `bncc-dados` is the specification to quote when telling a
ministry what "curriculum as data, done properly" means. Pair with Latam-GPT where sovereign
inference is the ask, and keep the offline delivery row for low-connectivity deployments.
🔵 **North America.** The driver is not curriculum supply but **statute**: AI-literacy standards and
model-policy deadlines (NC Session Law 2026-41, Idaho SB 1227) create demand for exactly the audit
and evaluation tiers above. The corpus is usually the district's existing scope-and-sequence.


## P23 — Curriculum-grounded tutor with a **hallucination gate** as the acceptance test (added p904)

### Why this pattern exists

Every curriculum-aligned product makes one claim that a ministry or district will test directly:
*when this system cites a curriculum objective, the objective is real and the text is right.*
**P22** is for the case where the curriculum corpus does not exist and must be re-authored. **P23 is
for the case where it does** — and `p904` measured both the substrate and the failure mode it
prevents.

The failure mode, measured rather than asserted (`bncc-dev/bncc-benchmark`, round
`oficial-seca-2026-09`, 19 models × 900 responses, **all 17,100 raw responses published**): asked for
the exact text of a national-curriculum objective **without access to the source**, models
reproduce it faithfully between **88% and 3%** of the time, and accept codes **verified not to
exist** between **0% and 42%** of the time. 🔴 **Reproducing the right text and refusing an invented
code are distinct abilities** — the models scatter rather than falling on a diagonal, and one model
reproduces text at 76% while accepting 42% of fake codes. **An accuracy number alone will not
detect this, which is why the gate is two-metric.**

🔵 **The strategic point for a studio:** this converts the most common objection in a public-sector
education sale — *"your AI makes things up about our curriculum"* — from a reassurance into a
number, measured on the client's own curriculum, with a published harness the client can re-run
after handover.

### Stack

| Layer | Component | Licence posture |
|---|---|---|
| **Curriculum spine** | https://github.com/bncc-dev/bncc-dados — 1,721 objectives, per-record `fonte` + `localizador_pdf`, SQLite/CSV derivatives, DOI `10.5281/zenodo.21625233` | 🔴 **MIT code + CC BY 4.0 data** — **attribution is a UI requirement** |
| **Agent tool surface** | https://github.com/dfdb76/bncc-mcp (**MIT**, independent) and/or the MCP worker in https://github.com/bncc-dev/bncc-pacotes; `npx -y @bncc/mcp` runs locally | MIT; 🔴 **`bncc-pacotes` reserves the project name and visual identity** |
| **Query tier** | https://github.com/eumakerdev/bncc_api (**MIT**) — REST + semantic search returning official codes as citations | MIT |
| **Acceptance gate** | https://github.com/bncc-dev/bncc-benchmark `harness/` (**MIT**) — re-run against the client's model and curriculum | MIT harness, CC BY items/results |
| **Tutor tier** | `HKUDS/DeepTutor` (Apache-2.0) or `THU-MAIC/OpenMAIC` (MIT) for the teaching loop; `matheussilvano/mooose` (Apache-2.0) as the reference for rubric-bound grading | permissive throughout |
| **Retrieval + memory** | `qdrant` (Apache-2.0) with payload filters on curriculum code; `mem0` (Apache-2.0) for learner state | permissive |
| **Serving** | `vllm` or `ollama` where sovereign/local inference is required (`intel/trends.md` **T6**) | permissive |
| **LMS seam** | `ltijs` (Apache-2.0) over LTI 1.3, or the Moodle community MCP servers (`compose/patterns.md` **P11**) | permissive tool, platform untouched |
| **Review console** | `appsmith` (Apache-2.0) for human review of flagged citations | Apache-2.0 |

### How it wires together

1. **The spine is the only source of curriculum truth.** The agent never emits a curriculum code or
   objective text from model memory. Codes are keys (`EF67LP08`, `EM13LGG103`, `EI02TS01`) resolved
   through MCP or the API, and every response carries the per-record source the dataset ships.
   `bncc-dados`'s own `llms.txt` states this contract — **use official codes as keys, never invent
   codes or skill texts, cite the source attached to each record** — so the contract is adopted, not
   invented.
2. **Two MCP paths, deliberately.** `dfdb76/bncc-mcp` and the `bncc-pacotes` worker are
   independently maintained over the same data; the packages embed the data and **work offline**.
   Pin a commit and vendor the JSONs — availability of the hosted endpoint is never on the critical
   path.
3. **The gate runs in CI, not at the end.** Fork `bncc-benchmark`'s MIT `harness/`, point it at the
   client's curriculum records and the model the engagement actually ships, and run it per release.
   Two thresholds, agreed with the client in writing: **minimum faithful-text rate** and
   **maximum fake-code acceptance**, the second strict (the published range reaches 0%, so 0% is a
   defensible target for a *grounded* system — the benchmark measures ungrounded recall, and
   grounding is precisely what this pattern adds).
4. **Flagged citations go to a human**, through the Appsmith console, with the record and source page
   attached. That queue is also the audit artefact a regulator asks for.
5. **Attribution ships in the product.** CC BY 4.0 on the data means the UI component that renders
   curriculum references carries the credit. Put it in the sprint that builds that component.

### The design rules that make it defensible

- 🔴 **Never let the model be the source of a curriculum code.** Retrieval-grounded or refused —
  there is no third behaviour, and the 42% figure is why.
- 🔵 **Measure two things, not one.** Faithfulness and refusal are separate metrics with separate
  thresholds. A single "accuracy" score hides the dangerous failure.
- 🔵 **Re-run the vendor's benchmark rather than citing it.** `bncc-benchmark` is published by the
  same organisation that maintains the dataset and the hosted endpoint whose grounding it reports as
  fixing the problem. The raw responses and methodology are public and the harness is MIT, so the
  honest use is **replication**, and saying so to the client is a credibility gain, not a loss.
- 🟡 **This pattern proves grounding, not pedagogy.** It says the system cites the curriculum
  correctly. It says nothing about whether anyone learned more — that is **P7**, and this KB's
  standing finding that there is no credible primary evidence of learning-outcome gains at scale is
  untouched by anything in this pattern.

### Deliverables

- A grounded curriculum tool surface (MCP + API) over the client's curriculum, offline-capable.
- A two-metric hallucination gate wired into CI, with thresholds agreed in writing.
- A human-review queue for flagged citations, doubling as the audit trail.
- A licence register recording the **CC BY attribution obligation** and any **reserved mark**
  (gate `904-G1`, trend **T27**).
- Replication report of the benchmark on the client's own curriculum and model.

### Estimate

| Phase | Work | Duration |
|---|---|---|
| 0 | `G1` + `904-G1` licence pre-flight on the curriculum dataset **and its payload directory** | 2–4 days |
| 1 | Spine adoption: vendor the records, pin the commit, stand up MCP locally | 1–2 weeks |
| 2 | Grounded retrieval + citation rendering with attribution | 2–3 weeks |
| 3 | Hallucination gate: fork the harness, set thresholds, wire to CI | 1–2 weeks |
| 4 | Tutor tier over the spine (DeepTutor or OpenMAIC), review console | 3–4 weeks |
| | **Total to first measured pilot** | **7–11 weeks** |

🔵 **Cheaper than P22 by design**, because the expensive part of P22 — authoring the corpus — is
already done and licensed. **Where the curriculum is not published as data, run P22 first and P23
after**; the two compose, and `bncc-dados` is the specification P22's phase 5 should aim at.

### Where it does not apply

- 🔴 **Where no published, verifiable curriculum exists.** If the "curriculum" is a PDF with no
  stable identifiers, there is nothing to key on — that is P22.
- 🔴 **Where the curriculum's own texts are under restrictive copyright.** Brazil's case works
  because BNCC normative texts are **official state acts and not copyrightable** (art. 8º, IV, Lei
  9.610/1998) and the CC BY grant covers only the compilation. **That analysis is jurisdictional and
  must be redone per country** — in several it will come out the other way, and then the corpus is a
  licensing negotiation before it is an engineering task.
- 🟡 **Outside Brazil there is currently no equivalent dataset to adopt.** `p904` searched:
  `currículo nacional dados abertos` returns nothing at or above 3 ★ in Spanish or Portuguese. Treat
  `bncc-dev` as a **template**, not as a dependency with regional equivalents waiting.

## P24 — Rebuildable handover tier: the licence inventory and pinned build no upstream will give you (added `p905`)

### Why this pattern exists

Measured `p905`: of the 14 platforms an education engagement is built on, **`0` disclose the grants of
their dependencies**, and the two most-starred education agents in existence cannot be rebuilt from
their own manifests (`DeepTutor` pins 1 of 74; `OpenMAIC` ships no lockfile). Meanwhile the
procurement specifications in **T9** and the exit requirements in **P8** both demand exactly what is
missing: *what is in this, and can we rebuild it without you.*

🔵 **This is not a pattern you sell on its own — it attaches to P1–P11 as a priced tier**, the same
way **P7** (evidence-of-efficacy) does. It is the cheapest credibility a studio can add to an
education proposal, because the client's audit will ask for it either way and no competitor bidding
the same open base will have it.

### Stack

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| Dependency-grant scanner | https://github.com/aboutcode-org/scancode-toolkit | 🟡 SPDX `NOASSERTION` → 🟢 **Apache-2.0** byte-read (`develop/apache-2.0.LICENSE`, 11,357 B) | 2,676 ★, pushed 2026-11-11. The industry-standard scanner; resolves direct **and** transitive grants. Retrieved for exactly this purpose at `p531`. 🔵 Its own `NOASSERTION` is a `T19` instance — read the file, not the badge |
| SBOM emitter | https://github.com/CycloneDX/cyclonedx-cli | Apache-2.0 (11,341 B) | 563 ★, pushed 2026-10-19. Emits the format procurement offices accept; pairs with the scanner's output |
| Python pinning | `pip-compile` (https://github.com/jazzband/pip-tools) **or** https://github.com/astral-sh/uv | BSD-3-Clause (1,522 B, byte-read) / Apache-2.0-or-MIT | `uv` is 92,203 ★, pushed 2026-11-18 — use it for speed on a 74-package tree with 36 upper bounds. 🔵 `pip-tools` is **absent from `repo:` search and `200` on `raw@main`**: apply the `905-F6` test — one query against a suspected new name — before recording either as missing |
| Node pinning | `npm ci` against a committed `package-lock.json` | — | Required for Canvas (348 npm) and OpenMAIC (178 npm), neither of which ships a lockfile on the paths probed |
| PHP / Java | `composer.lock` (already present) / Maven `dependency:tree` + `versions:lock-snapshots` | — | Moodle and Gibbon already pin; Sakai and OpenOLAT need the tree captured |
| Vendoring target | the client's own registry or a git mirror at a SHA | — | `p110`: 200 of 296 shelf rows are one maintainer, so the artefact must survive upstream disappearing |

### How it wires together

1. **Resolve once, deliberately.** Build the chosen base in a clean container, capture the resolved
   set, commit it as a lockfile in the client's repository. For `DeepTutor` this means following the
   `-r` chain to the 19 `requirements/modules/*.txt` leaves first (gate `905-G1`, rule 2) — the root
   manifest shows nothing.
2. **Scan the resolved set, not the manifest.** Point `scancode-toolkit` at the installed tree. The
   manifest names 311 or 74 packages; the resolved tree is where the copyleft and the
   non-commercial surprises actually live, and it is the only artefact that answers the audit.
3. **Emit the SBOM in CycloneDX**, attach the scanner's licence inventory, and flag three classes by
   hand because no tool reports them correctly: **per-directory grants** (the directory axis of `G1`, added `p897` / **T24**),
   **data-and-content grants** (`904-G1`/**T25**), and **reserved marks** (**T27**).
4. **Write the two known scanner false positives into the handover note before the audit runs them.**
   `OpenOLAT`'s `LICENSE` is a truncated Apache-2.0 (10,982 B vs 11,358 B canonical) and `DeepTutor`'s
   is hand-edited (`560-D`). Both are **Apache-2.0 on a clause read** and both **will** be flagged by
   a byte-identity check. An explained flag is a non-event; an unexplained one stops a deployment.
5. **Pin the rebuild in CI.** A job that rebuilds from the lockfile and fails on drift. `p111` found
   38.9% of this shelf has a live CI signal and `p112` that only 21.3% is both checked and pinned —
   this step is what moves the client's own estate into that 21.3%.

### Deliverables

- A lockfile or resolved manifest committed in the client's repository, and a container build that
  reproduces it byte-for-byte.
- A licence inventory over the **resolved** tree, with the three hand-checked classes above.
- A CycloneDX SBOM.
- A one-page handover note naming the known scanner flags and why each is benign.
- A CI job that fails on dependency drift.

### Licence posture

Every instrument in the stack is **Apache-2.0, BSD-3-Clause or MIT**, so the tier itself adds no
licence obligation to the client's product — which matters, because its whole purpose is to be the
artefact the client's legal review trusts.

### Estimate

**1.5–2.5 weeks** for a single base, including the hand-checked classes and the CI job. Add **1 week**
if the base is unpinned *and* multi-ecosystem (Canvas: npm + gems; Moodle: composer + npm). 🟢 Reuse
across engagements is high — the scanner configuration, the three hand-check classes and the handover
note template are the same for every client on the same base.

### Where it does not apply

🔴 If the client is consuming a **hosted** platform rather than deploying one, there is no tree to
scan and this tier is theatre — sell **P8** (metering, attribution and exit) instead. 🔴 And if the
engagement's base is already pinned and single-ecosystem (`openedx/openedx-platform`: 311/311, Python
only), the pinning half is already done — scope the scan alone, at roughly half the estimate, and say
so rather than billing for work upstream has done for you.

## P25 — Chinese-curriculum grading and item-bank tier, assembled from the Mandarin cohort with the AGPL kept out of the deliverable (added `p906`)

### Why this pattern exists

Every pattern above the grading tier assumes the item bank and exam delivery already exist. For a
China or Chinese-curriculum engagement they do — and until `p906` this KB could not name them,
because `repos/foundations.md` held the entire `Assessment, grading and academic integrity` tier as
North American and European across twelve verified rows while the Mandarin channel `作业 批改`
returns **347 repositories**. **P17** is the equivalent pattern over a BSD autograder for code and
structured answers. **P25 is for prose, handwriting and mathematics on paper**, which is what the
Chinese cohort is actually built for and what P17's substrate cannot mark.

🔴 **The pattern's real work is licence routing, not integration.** The cohort is mixed in a way
that matters: of the twelve repositories verified, **five are MIT, two are Apache-2.0, three are
AGPL-3.0 and two are Mulan PSL v2** — and the single most useful-looking item in the channel
(`MathCyclus`, **156 ★**, OCR → LaTeX → TikZ maths item bank) **carries no licence file at all** and
is barred. A studio that reads this cohort as "Chinese open source, permissive enough" ships AGPL
into a client's closed product. The routing below is the deliverable.

🔵 **And one row inverts the usual scanner result.** `nengdou-ai-review-helper-web` (**193 ★**) is
labelled `MulanPSL-2.0` by GitHub and is **verbatim Apache-2.0 on a byte read** (11,356 B,
`sha256₁₂ 43070e2d4e53`). **An SPDX-driven gate rejects the best repository in the tier for a
restriction that does not exist.** Run `G1` before this pattern, not after — see gate `906-G1`.

### Stack

| Layer | Component | Licence posture |
|---|---|---|
| **Item bank + exam delivery** | https://github.com/yf-team/yf-exam-lite (**MIT**, 173 ★, byte-read `main/LICENSE` 1,075 B `sha256₁₂ ecb2a17e710b`) — bank and item management, bulk import/export, automatic paper composition, wrong-answer drilling, enrolment, scoring | ✅ MIT. **Deliberately not an AI project**, which is why it is the spine: take the schema and exam delivery, add generation. 🟡 Idle since 2025-05-07 — **fork and own it**; treat it as a data model, not a live dependency. |
| **Offline/local item authoring** | https://github.com/BBkjdayup/BCTK (**MIT**, 58 ★, byte-read 1,066 B `sha256₁₂ 3e7c7c1a9f39`) — Windows desktop bank + paper composer, local-by-default storage, maths formulae, Word/Excel import-export, duplicate-question detection | ✅ MIT. The **local-first** tier: no student data leaves the machine, so no data-processing argument is needed. |
| **Marking engine (prose + handwriting)** | https://github.com/yinuoguan/nengdou-ai-review-helper-web (**Apache-2.0 on byte read**, 193 ★) — multi-subject marking with written feedback; and https://github.com/QwenStorm/xl-frontend (**MIT**, 50 ★) for **essay marking + OCR** of handwritten work | ✅ Apache-2.0 (patent grant) + MIT. 🔴 **Record the byte read in the SBOM**, or the client's own scanner will flag `nengdou` as Mulan. 🟡 `xl-frontend` was created and last pushed the same day — read the pipeline, do not depend on the repo. |
| **Error → targeted practice loop** | https://github.com/shellery1988/k12-smart-teacher (**MIT**, 16 ★, byte-read 1,074 B `sha256₁₂ 327facc37a63`) — wrong-answer analysis and generation of fresh analogous items from the specific error made (举一反三) | ✅ MIT. **The pedagogically load-bearing step** and the one every other grading row in this KB stops short of. Small — reimplement the loop, vendor nothing. |
| **Reliability signal** | The dual-agent parallel-review control read from https://github.com/ai-lingnan/econai-agent-platform (**AGPL-3.0**, 41 ★) | 🔴 **AGPL — read, do not link.** Reimplement: two independent marking passes over one submission, disagreement above threshold routes to a human. **Design, not dependency.** |
| **Item-bank-as-a-skill (optional)** | https://github.com/weishao2/tizhuang-agent-skills (**MIT**, 42 ★) — question sampling and knowledge-point retrieval exposed as an agent skill | ✅ MIT **on the skill**. 🔴 The bank itself is a **hosted third-party service**: the MIT grant does not cover availability, terms or the claimed 20M items. Contract for it separately or do not depend on it. |
| **Reasoning trace (optional)** | https://github.com/PGshen/thinking-map (**Apache-2.0**, 187 ★) | ✅ Apache-2.0, patent grant. Externalises the marking rationale as a navigable graph — the appealability surface a parent or regulator asks for. |
| **Platform reference (do not ship)** | https://github.com/youufis/SmartKBS (**AGPL-3.0**, 99 ★, pushed 2026-11-18) | 🔴 **AGPL.** The most complete single implementation of this whole tier — bank, papers, marking, live classroom, attendance, analytics. **Read it as the reference architecture; deploy-and-extend only.** A closed branded derivative is not available. |
| **Pre-flight** | `G1` licence gate, with the branch-resolution step | 🔴 **Four of the twelve cohort repos default to `master`.** A `main`-only probe reports them unlicensed — this is `884-G2`, discharged in `p885` and **recurring in `p906`'s own instrument** (`906-G3`). Resolve the default branch from `search/repositories` *before* reading bytes. |

### Wiring

1. **Fork `yf-exam-lite`** and keep only the item schema, bank CRUD and exam-delivery paths. This is
   the system of record. Nothing AI touches it yet.
2. **Put the marking tier behind a queue, not inline.** A submission produces a *marking job*;
   `nengdou`'s pipeline (Apache-2.0) and `xl-frontend`'s OCR path handle prose and handwritten work.
   Two independent passes per submission, per the `econai` control reimplemented.
3. **Gate on disagreement, not on confidence.** Where the two passes differ by more than the agreed
   band, the submission routes to a teacher. This is the only cheap, defensible reliability proxy in
   the tier, and it is what a human-in-the-loop requirement can actually trigger on.
4. **Feed every confirmed error into the `k12-smart-teacher` loop** to generate analogous practice
   from the specific mistake, written back as new items in the forked bank — so the bank grows from
   real student error rather than from generation alone.
5. **Expose the marking rationale** through a `thinking-map`-style graph. Appealability is a
   requirement in every jurisdiction this KB tracks, and a mark without a rationale is not appealable.
6. **For a local-only client, substitute `BCTK`** for steps 1 and 4 and run the model locally. The
   result needs no cross-border data-processing argument at all.

### Licence posture of the result

🟢 **Shippable closed.** The deliverable touches MIT and Apache-2.0 only. The two AGPL components
(`econai-agent-platform`, `SmartKBS`) are **read as designs and reimplemented**, which is the same
discipline P15 and P14 apply, and the two Mulan PSL v2 repositories are not in the build path.
🔴 **Two things must be written into the SBOM by hand**: the `nengdou` byte read (or the client's
scanner will report a Mulan dependency that is not there), and the fact that `MathCyclus` was
**evaluated and barred for having no grant** — because it is the first thing a competent reviewer
will find in this channel and the first thing they will ask why you did not use.

### Estimate

**8–12 weeks.** The spine is a fork, not a build, and the marking pipelines are readable. The cost
sits in three places: **Chinese-language QA** (the cohort's documentation, tests and UI are in
Chinese — budget a Mandarin-reading engineer, not a translator); **reimplementing the two AGPL
controls** cleanly enough to survive a provenance question; and **the handwriting OCR accuracy bar**,
which is the one place this pattern can fail outright and which no repository in the cohort
publishes a measurement for. 🔴 **Measure OCR accuracy on the client's own scanned work before
committing to the handwriting scope** — that is this pattern's equivalent of P23's hallucination
gate, and the cohort gives you no published number to rely on.

## P26 — Sanctioned LMS-to-agent bridge: the fastest credible demo in this KB, and the governance tier that makes it sellable (added `p907`)

**Why this pattern exists.** `intel/trends.md` **T30** records seven bridges, built in the last
eight months at four named institutions in four regions, that put an agent over a client's existing
LMS **without using any institutional surface**: they call the tenant's own REST API as the
signed-in person. No API key, no app registration, no vendor partnership — **and therefore no
procurement**, which is the slowest step in every education engagement this KB describes.

🔴 **And that is exactly why none of them is the deliverable.** A bridge acting as the signed-in
person is, from the institution's side, hard to distinguish from credential sharing. Three of the
seven declare themselves unofficial for that reason (`andrsnrua/universidad-pacifico-mcp`:
*"proyecto comunitario no oficial"*). **This pattern is the sanctioned version of an unsanctioned
pattern**: identical user-facing capability, with institutional consent and an auditable service
identity underneath.

### Stack

| Layer | Pick | Licence | Why |
|---|---|---|---|
| Reference implementation — D2L Brightspace | https://github.com/GuanmingQiao/POLITEMALL-MCP | **MIT** (byte-read `p907`) | The only D2L row in this KB. **Read it for its tool decomposition, not to deploy it** |
| Reference implementation — Blackboard Ultra | https://github.com/andrsnrua/universidad-pacifico-mcp | **ISC** (byte-read `p907`) | **70 tools / 5 prompts**, incl. local PDF/DOCX/PPTX/XLSX text extraction and private exports — the most complete tool surface in the cohort |
| Reference implementation — Moodle | https://github.com/Faixiang/Moodle-MCP (read-only) then https://github.com/G36maid/moodle-mcp (read-write) | MIT | Already shelved in `repos/foundations.md`; **these use the institutional Web Service API**, which is the posture this pattern wants |
| Reference implementation — Canvas | https://github.com/ucfopen/canvasapi | MIT | University of Central Florida's Python wrapper — a permissive seam onto an AGPL-3.0 platform |
| Rostering / identity of record | https://github.com/StevenACoffman/roster | **MIT** (byte-read `p907`) | **OneRoster v1.2**, and its authorization is enforced **in the database**, so a caller scoped to one school cannot read another's rows. This is the multi-tenant isolation the sanctioned version must build and the user-credential version gets for free |
| Agent runtime | any permissive framework already in `agents/top.md` | MIT / Apache-2.0 | Not the differentiator here |
| Audit / evidence | https://github.com/yetanalytics/lrsql | Apache-2.0 | xAPI statement per agent action: the record that distinguishes a sanctioned bridge from a scraper |

### How it wires together

1. **Replace the credential, keep the tool surface.** Take the tool decomposition from the reference
   implementation for the client's platform — the Peru server's seven tool groups (courses,
   materials/syllabi, announcements, activities/grades, calendar, participation, local library) are
   the most complete published map. Re-implement against an **institutional service identity**
   (LTI 1.3 via `Cvmcosta/ltijs`, OAuth app registration, or the platform's admin API) instead of
   the user's session.
2. **Scope the identity to the user, inside the server.** The capability users want is *my* courses
   and *my* grades. With a service identity you must enforce that yourself — which is why
   `StevenACoffman/roster`'s database-enforced authorization is the design to copy rather than
   application-layer checks.
3. **Emit an xAPI statement per tool call** into `lrsql`. This makes the bridge auditable, and it is
   also the `P7` efficacy tier for free.
4. **Run gate `G1` plus axis `907-G1`** over the whole set before shipping — four of the seven
   reference bridges carry **no licence at all** and cannot be copied from, only read.

### The design rules that make it defensible

- 🔴 **Never ship the user-credential version to a client, even as a pilot.** It is precisely what
  the institution's security review exists to stop, and discovering that in review costs the
  engagement.
- 🔴 **Read-only first.** Six of the seven reference bridges are read-only; the one read-write
  Moodle server in this KB is a separate, later step. Grade *writes* put the deployment inside the
  EU AI Act's assessment scope (**2 Dec 2027**) and inside FERPA's record-amendment rules in the US.
- 🟡 **The parent persona is a distinct product.** `cculb/schoolconnect` (MIT, PowerSchool Parent
  Portal) is the only guardian-facing agent in this KB. Guardian access has its own consent
  structure — do not treat it as a student bridge with a different login.

### Licence posture

**Permissive end to end.** Every reference implementation and infrastructure pick above is MIT, ISC
or Apache-2.0, all byte-read this pass. The client owns the bridge; nothing here forces disclosure.
🔵 **The only end-to-end permissive pattern in this file that touches a commercial LMS.**

### Estimate

**4–6 weeks** for a read-only sanctioned bridge on one platform with xAPI audit: 1 week to port the
tool surface, 1–2 weeks institutional identity and per-user scoping, 1 week audit tier, 1–2 weeks
security review and hardening. 🔵 **A throwaway demo on a staff member's own test account is 2–3
days** — which is the point of the pattern, provided the demo is labelled a demo and never quietly
becomes the pilot.

### Where it does not apply

- **Blackboard, if the client wants a licensed starting point.** The only Blackboard bridge found
  carries no licence (`bolgerru/blackboard-mcp`), so Blackboard work starts from the platform's own
  REST documentation instead.
- **Where the client has no LMS.** This pattern's value is that the system of record already exists;
  if it does not, `P1` builds the platform instead.
- **Where procurement is already solved.** If the institution will sponsor an app registration from
  day one, skip the reference implementations and build straight onto LTI 1.3 — the bridges in
  `T30` are interesting for the constraint they route around, not for their code.

## P27 — One adapter, many campuses: the multi-tenant Spanish-language LMS bridge, built from the in-language cohort (added `p908`)

### Why this pattern exists

`P26` made the *sanctioned* bridge to one institution's LMS sellable. `p908`'s code-search leg then
measured the thing `P26` cannot do: **there are now at least 30 of these bridges, each written for
exactly one campus, and across them they already speak four different LMS protocols in two
languages.** Filed in `agents/top.md` this pass: Moodle at UTN, UdeSA, UNAM, ULEAM, UNSA, UJI, UNED,
USC, UDB and TU München; **Blackboard Learn** at UPC; **Canvas** at ESPOL; and **SIU-Guaraní**, the
student-information system the Argentine national university system actually runs.

🔴 **Every one of them re-implements the same four things** — credential capture, session handling,
a course/assignment/grade model, and a write-confirmation policy — **and no two of them share a line
of code.** That is the engagement: a multi-tenant client does not want eleven forks, it wants one
adapter layer with eleven tenant profiles.

🟢 **This is the only pattern in this KB whose component rows place themselves regionally.** An agent
named after a university does not need its region inferred, so a bid for a LATAM university group can
cite working code from the exact country it is bidding into.

### Stack

**Reference implementations to read before writing anything** (grants byte-read `p908`,
[`licence-bytes.2026-11-19-p908.tsv`](../evidence/licence-bytes.2026-11-19-p908.tsv)):

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| **Credential and write-policy reference** | https://github.com/nialvape/utn-mcp | **ISC** | The best credential hygiene in the cohort: OAuth server, password never stored, preview-then-confirm on writes, and it **refuses a non-HTTPS campus** |
| **Second write-policy reference** | https://github.com/changazo/udesa-mcp | **Apache-2.0** | Preview-then-confirm, independently arrived at. Apache-2.0 brings an explicit patent grant, which is the licence to copy structure from |
| **Two-system (LMS + SIS) reference** | https://github.com/HyNuwa/UniMCP | **MIT + inherited ISC** | Moodle **and** SIU-Guaraní in one server, with **Guaraní read-only** — the right default for a system of record |
| **SIS protocol reference** | https://github.com/jpmanson/siu-guarani-mcp | **MIT** | SIU-Guaraní *autogestión docente* on its own, so the SIS surface can be read without the Moodle code around it |
| **Blackboard Learn tenant** | https://github.com/alejooroncoy/campus-cli | **ISC** | The cohort's only Blackboard implementation (UPC, Perú) |
| **Canvas tenant** | https://github.com/SebasB76/poli | **MIT** | The cohort's only Canvas implementation (ESPOL, Ecuador) |
| **Teacher-side, not student-side** | https://github.com/falkenslab/miyagi | **MIT** | Grades to the teacher's own rubric and staffs the forum — the persona that pays, since it saves staff hours rather than student hours |
| **Skill-shaped delivery** | https://github.com/Group-Active-IA/Skill-Moodle | **MIT** | Ships as a Claude Code **skill**, not a server: no deployment, no hosting, no procurement (`T22`, `T31`) |
| **Offline-first / messaging delivery** | https://github.com/MarcoXMarquez/CampusUNSA | **MIT** | PWA **plus WhatsApp/Telegram** over Classroom and Moodle with institutional SSO — the delivery surface that matters where connectivity does not hold |
| **Server-side alternative** | https://github.com/EduardoKrausME/moodle-local_mcp | 🔴 **GPL-3.0** | MCP served from **inside** Moodle. Read it for the sanctioned-integration shape; 🔴 **do not vendor it** — a Moodle plugin inherits GPL |

**Infrastructure already in this KB:** `moodle/moodle` Web Services API as the protocol of record,
`openedx/edx-ora2` where open-response grading is in scope, and
[`repos/foundations.md`](../repos/foundations.md)'s `trycua/cua` (**MIT**) as the **last resort for a
tenant whose SIS has no API at all** — drive its web UI in a sandbox rather than forge a protocol.

### How it wires together

1. **Tenant profile, not a fork.** One declarative profile per campus: base URL, protocol
   (`moodle-ws` | `blackboard-rest` | `canvas-api` | `siu-guarani`), auth method, HTTPS requirement,
   and a per-surface write policy. **Adding a campus is a profile, not a release.**
2. **Credential broker, copied from `utn-mcp`'s posture.** The agent acts **as the signed-in person**
   on their own session — which is exactly why this class proliferates without procurement (`T30`) —
   so the broker holds a short-lived session, never a stored password, and refuses a non-HTTPS
   endpoint outright.
3. **Read model normalised, write model not.** Courses, assignments, deadlines, materials and grades
   normalise cleanly across all four protocols. **Writes do not**: submission semantics differ per
   protocol and per institution, so writes stay per-tenant and per-surface.
4. **Two-tier write gate.** Reads are free; writes are preview-then-confirm (both `utn-mcp` and
   `udesa-mcp` independently chose this); **anything touching the SIS is read-only by default**, as
   `UniMCP` does with Guaraní. A grade record is a system of record, and an agent should not be the
   thing that edits it.
5. **Delivery surface chosen per engagement, not per product.** MCP server for a desktop-agent
   audience; **skill** where there is no budget to host anything (`Skill-Moodle`); **WhatsApp**
   where the students are (`CampusUNSA`). Same adapter underneath.
6. **Governance tier from `P26` bolted on unchanged**: consent record, action log, and the
   institution's own sign-off on which surfaces are writable.

### The design rules that make it defensible

- 🔴 **Do not ship a bridge the institution has not sanctioned.** The whole cohort works because it
  borrows the user's own session, which is also what makes it a governance problem at institutional
  scale: at one user it is a browser; at ten thousand it is an unapproved integration. **`P26`'s
  sanction step is a prerequisite of this pattern, not an upgrade to it.**
- 🔴 **Exclude the AGPL member of this cohort from the deliverable.** `EmilioGiordano/unsada-mcp`
  (Argentina, UNSAdA) is subject-matter-perfect and **AGPL-3.0, byte-read in `p908` at `34,523 B`, `sha256₁₂ 0d96a4ff68ad` — the same digest `p708` recorded** — network
  copyleft triggers on *deployment*, which is the one shape a hosted multi-tenant bridge cannot
  absorb. Read it; do not link it.
- 🔴 **Do not vendor the unlicensed ones.** Seven of the 30 carry **no grant at all** — including
  `PedroCarassale/utn-mcp`, `A-F-V-A/unihelp-mcp-a2a` and `MoonquantCap/agentes-ia-ucema`. They are
  real, readable, and legally unusable. 🟢 **An issue asking the author for a licence is cheap and
  has worked for this base before** — and these are students at identifiable institutions.
- 🟡 **Treat every repository here as a protocol specification, not a dependency.** Median star count
  in this cohort is **1**, several are 0, and they are written by individual students. The durable
  asset is the *protocol knowledge* they encode — which campus runs which LMS behind which auth flow.

### Licence posture of the result

🟢 **MIT, ISC and Apache-2.0 only** — every row in the Stack table above except the two explicitly
flagged ones, each grant **byte-read from the payload in `p908`**, not taken from a badge. The GPL
row is read and not vendored; the AGPL row is named and excluded; the unlicensed rows are named and
excluded. 🔵 **The CC BY-SA caution from `T32` applies if teacher-facing skill text is imported into
this build**: keep it as an attributed input layer, separate from the client's own adaptations.

### Estimate

- **Adapter + two tenant profiles + read-only SIS + governance tier:** 5–7 weeks.
- **Each additional tenant on an already-supported protocol:** 3–5 days, dominated by auth-flow
  quirks, not by code.
- **Each additional *protocol*:** 2–3 weeks. Moodle, Canvas and Blackboard all have reference
  implementations in the table; a SIS that is not SIU-Guaraní has none.

### Where it does not apply

- **A single-institution client.** Then this is `P26` with more ceremony — build the one bridge.
- **An institution that will grant a service account.** The user-credential model exists to route
  around procurement; if procurement says yes, a sanctioned server-side integration
  (`moodle-local_mcp`'s shape, GPL implications accepted) is simpler and audits better.
- **Anywhere the SIS must be written to.** No row in this cohort does it safely, and `p908` found
  none that claims to.

## P28 — Spec-first tutoring: build against the UK's published standard inside the EU's deferral window (added `p909`)

**When to reach for this.** An EMEA engagement, secondary phase, where the buyer is a ministry or
agency rather than a school — which `p909` measured as the normal case: of **390 public
AI-in-education tenders across 25 countries, central government ran 124 and individual schools,
trusts and colleges ran 11**. The commercial hook is that the **UK's AI Tutoring Tools Pioneer
Programme standard is owned by DSIT/i.AI and will be shared with the wider market**, so the
specification arrives *before* the products that must satisfy it, and the EU's Annex III education
obligations do not bite until **2 December 2027** (`T3`). This pattern builds to the published
spec during that window.

**Scope it to the buyer's own scope**, not to a generic tutor: **Years 9–10**, English, maths,
science and modern foreign languages, with pupils from underrepresented backgrounds as the
designed-for case. That is the programme's stated remit and it is a far easier acceptance
conversation than "a tutor".

### The stack — every row measured on both channels in the `p909` census (2026-11-19)

| Layer | Repo | Grant | ★ | Why this one |
|---|---|---|---|---|
| Tutor core | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 60,504 | Agentic tutoring grounded in the student's *own* material with persistent learning history — the only education-native repo at this scale with a patent grant |
| Retrieval | https://github.com/HKUDS/LightRAG | MIT | 40,763 | Same lab as the tutor core, so the idioms match; avoids an integration seam |
| Retrieval (alt) | https://github.com/infiniflow/ragflow | Apache-2.0 | 94,399 | Pick this instead when the client wants a product-shaped RAG service rather than a library |
| Curriculum ingestion | https://github.com/docling-project/docling | MIT | 70,766 | Syllabus and textbook PDFs into structured text; **prefer over `opendatalab/MinerU` (83,954 ★), which is `NOASSERTION` and needs a byte-read first** |
| Learner memory | https://github.com/mem0ai/mem0 | Apache-2.0 | 69,205 | Persistent learner state across sessions — the "lifelong" half of the tutor claim |
| Inference (server) | https://github.com/vllm-project/vllm | Apache-2.0 | 97,185 | Sovereign/in-country serving, which `T6` records as a procurement requirement rather than a preference |
| Inference (edge) | https://github.com/ollama/ollama | MIT | 187,555 | School-premises fallback where connectivity or data residency forbids the server tier |
| Institutional surface | https://github.com/boyuchengz/canvas-mcp | MIT | 118 | LMS bridge (class `T30`) — roster and coursework context without building a front end |
| Learner surface | https://github.com/geekjourneyx/interactive-learning | MIT | 52 | **Verifiable learning path + exportable HTML checkpoint card.** Added to `agents/top.md` in `p909` |
| Teacher surface | https://github.com/SirhanMacx/Claw-ED | MIT | 65 | Local-first lesson drafts, student materials and slides — the teacher-facing half the programme's remit implies |
| Assessment/standards | https://github.com/openolat/qtiworks | BSD-3-Clause | 🟡 unmeasurable | QTI engine, so items are portable to the buyer's existing assessment estate. **Star count is `unmeasurable`, not zero** (`909-F2`) |

🟢 **Every grant above is permissive.** That is deliberate and it is the whole point of the
assembly: the deliverable can be closed, relicensed or handed over, which is what a ministry
framework contract will ask for.

### How it wires together

1. **Ingest the buyer's curriculum, not the internet.** `docling` turns the awarding body's
   syllabus documents into structured text; `LightRAG` indexes **only** that corpus. The
   anti-hallucination control is corpus scoping plus the acceptance test from **`P23`** — carry
   `P23`'s hallucination gate over verbatim; do not re-derive it.
2. **Bind the tutor to a learner, not a session.** `DeepTutor` over `mem0`, so the learning
   history survives and the "personalised" claim is evidenced rather than asserted.
3. **Serve it where the data is allowed to be.** `vLLM` in-country for the institutional tier,
   `ollama` on premises for the offline tier. Decide this before architecture, not after — `T6`.
4. **Take context from the LMS, do not replace it.** `canvas-mcp` for roster and coursework.
   Where the institution runs Moodle or Canvas itself, **integrate over the API and keep
   `moodle/moodle` (GPL-3.0) and `instructure/canvas-lms` (AGPL-3.0) out of the deliverable** —
   and note that `sakaiproject/sakai` is **ECL-2.0**, an Apache-family grant, so a Sakai estate is
   the one LMS core on these shelves you *can* link into a closed deliverable.
5. **Deliver to the learner with no front end to build.** `interactive-learning` as a skill in a
   client the learner already has, with `Claw-ED` giving the teacher lesson drafts from the same
   corpus.
6. **Emit the checkpoint card on every completed path** — and this is the step that makes the
   pattern worth naming.

### 🔵 The insight: the checkpoint card *is* the compliance artefact

When Annex III lands on **2 December 2027**, a tutoring system in the EU owes **human oversight
and logging** — evidence that a person could see and correct what the system concluded about a
learner. Most teams will build that as compliance overhead nobody uses.

`interactive-learning` already exports a **shareable, reviewable HTML checkpoint card** recording
what the learner was taken through and what they demonstrated. 🔵 **Emit it per learner per path,
retain it, and the oversight and logging obligation is discharged by a feature teachers and
parents actually want to look at.** Build it now, during the deferral, and the 2027 date is a
delivery milestone rather than a re-architecture. Pair it with **Article 50 transparency, which
is already live since 2 August 2026** and is *not* deferred — disclose the AI interaction from day
one.

### 🔴 What this pattern must not do

- **No emotion or affect inference, in any form.** Inferring a learner's emotions in an education
  institution has been **prohibited in the EU since February 2025**, with only medical and safety
  carve-outs. `T14` records that affective design is exactly what drives retention metrics, which
  is why this needs saying in the architecture document and not just the legal annex.
- **No `TapXWorld/ChinaTextbook` (84,747 ★) as a content source.** It is the largest
  education-adjacent repository on these shelves and it carries **no licence at all** (`NONE`),
  which `909-F3` measures as the state of 5.3% of this shelf. Scale is not permission.
- **No `MinerU` in the deliverable until its grant is byte-read.** `NOASSERTION` at 83,954 ★ is
  the single largest unresolved licence question on the shelf, and `906-G1` measured that field
  wrong in **both** directions.
- **Do not write to the SIS.** No row in this stack does it safely; `p908` found none that claims
  to, and that verdict is unchanged.

### 🟡 Honest limits

The two learner- and teacher-facing surfaces are **small and idle** — `interactive-learning` 52 ★,
last push `2026-04-10`; `Claw-ED` 65 ★, last push `2026-09-19`. Treat them as **forkable
reference implementations**, not as upstreams to depend on; the agent-*skill* cohort's ceiling is
**126 ★** and its 1,000 ★ watch condition has never fired. The DSIT/i.AI standard itself **has not
been read** — its existence and ownership rest on the tender notice as reported by two searches,
and **no primary source could be fetched this pass**. 🔵 **The first action on a live engagement is
to obtain that standard**; this pattern is positioned for it, not validated against it.

## P29 — National-examination tutor for a market whose *corpus* cannot be licensed: build the spine, generate the items, capture the rest from the learner (added `p910`)

**Use when** the engagement is exam-outcome-driven in one of the markets `p910` measured — Japan
(JLPT), Korea (TOPIK / suneung), Hong Kong (HKDSE), Singapore (PSLE), Indonesia (SNBT / UTBK),
Malaysia (KSSM), Australia (NAPLAN), UK (GCSE) or Israel (bagrut) — and the client expects the
studio to "start from what's open". 🔴 **In six of those nine markets what's open is ungranted, and
where a national syllabus has been published machine-readably it was published
`CC BY-NC`** (`T25`, `910-F2`, `910-F3`). This pattern is the shape that survives that fact.

### 🔴 Step 0 — the exclusion list, which is the actual design decision

Run `G1` first, then **bar these by name** and record the bar in the handover (`P24`):

| Do **not** ingest | ★ | Grant, byte-read `p910` | Why it is fatal, not inconvenient |
|---|---|---|---|
| [`5mdld/anki-jlpt-decks`](https://github.com/5mdld/anki-jlpt-decks) | 3,149 | **CC BY-NC 4.0** (field: `NOASSERTION`) | The largest exam corpus in the tier. **NonCommercial bars the engagement**, and the client is paying. |
| [`davidzbot/singapore-primary-math-syllabus`](https://github.com/davidzbot/singapore-primary-math-syllabus) | 0 | **CC BY-NC 4.0** (field: `NOASSERTION`) | The MOE 2021 primary maths spine — the exact artefact this pattern needs, and unusable. |
| [`evanclan/OpenJLPT`](https://github.com/evanclan/OpenJLPT) | 82 | **CC BY-SA 4.0** | Self-describes as *"correctly-licensed"*. Share-alike propagates into the client's deliverable. |
| [`stephenmk/yomitan-jlpt-vocab`](https://github.com/stephenmk/yomitan-jlpt-vocab) | 142 | **CC BY-SA 4.0** (`LICENSE.txt`) | Same, and a one-path licence probe reports it as ungranted. |
| [`truthyblue/jlpt-max-deck`](https://github.com/truthyblue/jlpt-max-deck) | 80 | **AGPL-3.0** | Network copyleft on content. Counsel question with no upside. |
| [`summeraprx/topik-shortcut`](https://github.com/summeraprx/topik-shortcut) | 1 | **no grant** | The only AI-native TOPIK build in existence. Cannot be forked or vendored. **Rebuild it.** |
| [`jacoubsmairat/TawjihiQuiz`](https://github.com/jacoubsmairat/TawjihiQuiz) | 0 | **no grant** | Jordan's most complete exam platform. Same verdict. |

🔵 **Say this to the client in the first week.** The exclusion list is the deliverable's warranty:
it is why the thing you hand over can be sold, and it is cheaper to establish now than to unpick
after an ingest.

### 🟢 The stack, every row permissive and byte-verified

**Spine — build, do not adopt (`P22`'s method, new market).** Re-author the exam specification from
the examination authority's **own public documents** into your schema: objective → topic → item
type → marking rule. Use [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) and
[`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) as the **structural
reference** (both already on this shelf), not as content. The client owns this artefact outright —
it is the one piece no competitor can clone from GitHub.

**Exam-rule engine — adopt, per market.**
[`DeJavi08/cat-snbt-skd`](https://github.com/DeJavi08/cat-snbt-skd) (MIT) encodes Indonesia's CAT
timing and scoring for SNBT/UTBK *and* the CPNS SKD;
[`SISUBEN/DSE-ICT-Master`](https://github.com/SISUBEN/DSE-ICT-Master) (MIT) and
[`Goodbilly/BillyStreet-HKDSE-Math-Mock-Platform`](https://github.com/Goodbilly/BillyStreet-HKDSE-Math-Mock-Platform)
(MIT grant, 🟡 holder line reads `GitHub, Inc.` — `910-G2`, fix upstream before shipping) encode the
HKDSE paper split. **Take the rules, expect to rewrite the UI.**

**Portal base — fork.** [`tristcoil/hanabira.org`](https://github.com/tristcoil/hanabira.org)
(MIT, 436 ★) is the only permissive full application in the tier and covers **Japanese and Korean
in one codebase**. 🔴 20 months idle: fork it, budget the dependency upgrade, do not track upstream.

**Items — generate, never redistribute.**
[`jamsinclair/open-anki-jlpt-decks`](https://github.com/jamsinclair/open-anki-jlpt-decks) (MIT) is a
deck **build pipeline**, which is the licence-clean inverse of a deck;
[`davidluzgouveia/kanji-data`](https://github.com/davidluzgouveia/kanji-data) (MIT, `master`) and
[`AnchorI/jlpt-kanji-dictionary`](https://github.com/AnchorI/jlpt-kanji-dictionary) (MIT) are the
two permissive reference datasets. Author new items against the spine with
[`satvik314/educhain`](https://github.com/satvik314/educhain) (MIT).

**Corpus coverage — capture from the learner, which is the real answer to `910-F2`.**
[`metrovoc/immersive-memorize`](https://github.com/metrovoc/immersive-memorize) (MIT) builds cards
from subtitles in media **the learner already chose**. 🟢 Nothing licensed is redistributed, the
corpus is per-learner, and coverage grows without touching a restricted deck. **This is the
pattern's key move**: it converts a licensing dead end into a product feature.

**Retention — adopt.** [`ankitects/anki`](https://github.com/ankitects/anki) +
[`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) (both on
this shelf) for FSRS-6 scheduling; [`warleysr/ankipa`](https://github.com/warleysr/ankipa) for
pronunciation assessment where the exam has a speaking component (TOPIK, GCSE MFL).

**Reading and marking tier — adopt the pedagogy, not the model.**
[`Mocas-12/jlpt-n1-Yomitaku`](https://github.com/Mocas-12/jlpt-n1-Yomitaku) (MIT) carries
**trap-classified** explanations per item type — item-level pedagogical metadata that is otherwise
absent from open repositories, and the natural input to `P23`'s hallucination gate.
[`BaijayantaRoy/bandup`](https://github.com/BaijayantaRoy/bandup) (MIT) carries the **Singapore
PSLE / A-Level GP essay rubric**; take the rubric encoding even if you replace the implementation.

**Delivery surface — follow `T22`.**
[`aiktb/furiganamaker`](https://github.com/aiktb/furiganamaker) (MIT, 312 ★) is the reference for a
browser-extension reading-support surface: the tutor meets the learner on the page they are already
reading rather than in another portal.

**Agent runtime, grounding and sovereign inference — all already on this shelf.**
[`pydantic-ai`](https://github.com/pydantic/pydantic-ai) (MIT) or
[`langgraph`](https://github.com/langchain-ai/langgraph) (MIT) for orchestration;
[`HKUDS/LightRAG`](https://github.com/HKUDS/LightRAG) (MIT) +
[`qdrant`](https://github.com/qdrant/qdrant) (Apache-2.0) to ground every answer in the
client-owned spine; [`ollama`](https://github.com/ollama/ollama) (MIT) or
[`vllm`](https://github.com/vllm-project/vllm) (Apache-2.0) for in-country inference, which `T6`
records as a procurement requirement rather than a preference across this region.

**Acceptance gates — non-negotiable, and they are what makes it sellable.**
`P23`'s hallucination gate against the spine; `P7`'s evidence tier;
[`promptfoo`](https://github.com/promptfoo/promptfoo) (MIT) as the harness; and
[`l-yohai/suneung`](https://github.com/l-yohai/suneung) (MIT) as the **method** for an
exam-aligned eval — it scores an LLM against a real national paper, which is the only benchmark
shape a ministry buyer finds legible. 🔴 It is 3 years idle: re-implement the method, do not depend
on the harness.

### 🟢 Market-specific add-ons

- 🇭🇰 **Hong Kong:** [`JUPASCal/JUPASCal.github.io`](https://github.com/JUPASCal/JUPASCal.github.io)
  (MIT) models HKDSE → JUPAS admissions scoring. 🔴 Admissions is a **high-risk use** under the EU
  AI Act and a regulated one in several APAC jurisdictions — if the engagement touches it, run
  `P4`'s conformity track, not this pattern alone.
- 🇦🇺 **Australia:** [`nsip/nias2`](https://github.com/nsip/nias2) (Apache-2.0) is the National
  Schools Interoperability Programme's own NAPLAN validation and post-processing stack. **Start
  institutional work here** — it is the one government-adjacent permissive artefact in the region.
- 🇲🇾 **Malaysia:**
  [`lerlerchan/Prompt-libraries-for-Malaysia-Educators`](https://github.com/lerlerchan/Prompt-libraries-for-Malaysia-Educators)
  (MIT, KSSR/KSSM-aligned, local currency and scenarios) is the **entire** permissive local supply.
  Pair with `P10`'s teacher-enablement track; the 2026–2035 National Education Plan is the demand
  driver and nothing open answers it.
- 🇮🇱 **Israel:**
  [`peleg-jpg/israeli-bagrut-psychometric`](https://github.com/peleg-jpg/israeli-bagrut-psychometric)
  (MIT) covers Bagrut **and** the Psychometric entrance exam, and its two-line provenance grant is
  the model `P24` asks for.
- 🇬🇧 **UK:** [`milesberry/networx`](https://github.com/milesberry/networx) (MIT) for GCSE/A-Level
  Computer Science simulation;
  [`StudentSuite/awesome-study-resources`](https://github.com/StudentSuite/awesome-study-resources)
  (MIT, 79 forks / 39 ★) as a cheap map of what learners actually use. Sequence behind `P28` — build
  against the UK's published standard inside the EU deferral window.

### 🟡 Honest limits

🔴 **Nothing in this stack is large.** Outside `hanabira.org` (436 ★), `furiganamaker` (312 ★) and
the two deck/dataset repositories, every market-specific row is **under 10 ★ and single-author** —
`bandup` 2 ★, `cat-snbt-skd` 1 ★, `DSE-ICT-Master` 1 ★, `edubot-backend` 0 ★. 🔵 **They are adopted
for their *encodings*** — the exam's timing rules, paper structure and marking rubric — **not for
their code volume or their maintenance**. Price every one as a reference implementation to be
rewritten, and put the spine, the gates and the capture path in the quote, because that is where
the delivered value is. 🔴 **No row in this pattern was run**: the grants were byte-read and the
architectures were read, and nothing here has been executed against a live exam cohort. 🟡 Korea is
the weakest leg — the capability exists only as an ungranted repository, so a Korea engagement
starts with a rebuild and should be priced accordingly.

## P30 — Assisted marking for a national board putting essays on screen: the Nigeria WAEC/NECO window (added `p911`)

🔵 **Why this pattern and not another.** Every other pattern in this file starts from supply — a
corpus, a platform, an agent worth composing. **This one starts from a dated procurement.** WAEC and
NECO are moving Nigeria's WASSCE to **full computer-based testing, objective *and* essay
components**, reported for **May–June 2026**, delivered through **accredited `JAMB` and `NOUN` CBT
centres rather than schools** (`intel/market.md` EMEA). 🔴 **A national board putting *essay*
components on screen has, by construction, created national-scale demand for assisted marking** —
and nothing in this KB's Nigerian supply addresses it.

### What exists, byte-read, and what does not

| Layer | What exists | Grant |
|---|---|---|
| CBT delivery (practice tier) | [`Kirchhoff-dev/cbt-app-updates`](https://github.com/Kirchhoff-dev/cbt-app-updates) — **offline** JAMB/WAEC/Post-UTME simulator, 30+ subjects | 🟢 MIT · 1,071 B · `9f194f984482` |
| CBT delivery (institutional tier) | [`idrismukthar/TTL_CBT`](https://github.com/idrismukthar/TTL_CBT) — school termly examinations | 🟢 MIT · 1,087 B · `30062651a966` |
| AI-assisted CBT | [`edunelsonit/Jambora`](https://github.com/edunelsonit/Jambora) | 🟢 Apache-2.0 · 11,357 B · `c71d239df917` |
| Exam-prep content | [`ALIYUAAM10/NAIJASCHOLAR`](https://github.com/ALIYUAAM10/NAIJASCHOLAR) — JAMB/WAEC/NECO | 🟢 MIT · 1,082 B · `6fd3e72cd64d` |
| Grading engine | `ls1intum/Athena` + the permissive grading tier (`T21`) | 🟢 permissive, already shelved |
| 🔴 **Essay scoring for the target language variety** | 🔴 **nothing** | — |
| 🔴 **Board-grade delivery / marking platform** | 🔴 **nothing, under any licence** (`911-G1`) | — |

### The recipe

1. 🟢 **Start from the grading tier this KB already verified, not from the Nigerian rows.** `T21`
   records the open grading stack as mature, permissive and university-built; `ls1intum/Athena` is
   the assisted-marking core. The Nigerian rows above are **delivery and practice**, and they are
   the wrong layer for marking.
2. 🟢 **Take the item and delivery shape from the local rows.** `cbt-app-updates` is **offline-first
   across 30+ WASSCE subjects**, which matters because the CBT-centre proprietors' own stated
   objection to the transition is the **cost of networked computers**. Build to that constraint from
   the start; do not assume centre connectivity.
3. 🔴 **Price essay scoring as a build, and inherit `Gap 246`'s split.** English-medium WASSCE
   removes `Gap 239`'s Portuguese language problem, so `wwrwbs/AI_AWE` (Apache-2.0, permissive
   closure across its whole tree) **transfers architecturally** — but its feature layer is
   calibrated on a different writing population. 🔴 **The expensive part is not the model, it is the
   agreement study**: a WASSCE rubric with WAEC-graded scripts, which only the board can supply.
   **That is the contract conversation, and it is the first one to have.**
4. 🟢 **Use `001kenji/KCSE-predictor`'s method, not its predictions, for blueprint work.** A
   longitudinal corpus of a board's own past papers (Apache-2.0, 20+ years of KCSE) is the worked
   example of **blueprint and topic-coverage analysis** — the analysis a board needs before it can
   generate items, and the one transferable Kenyan asset for a Nigerian engagement.
5. 🟡 **Enter a contested market knowingly.** **Class54** (AI tools for JAMB/WAEC, *"over 300,000
   students"*, self-reported) and **EDUVATE CBT** (AI topic tutor, 49 institutions, founder's own
   post) are already there. 🔵 **The defensible position is the board side, not the student side**:
   marking, blueprinting and delivery assurance, where the incumbents are not.
6. 🔴 **Write the political risk into the plan, do not discover it.** One report refers to a **House
   of Representatives request to suspend computer-based WAEC until 2030** (*single source, not
   readable in this environment*). 🔵 **Scope the engagement so phase one is valuable even if the
   national date slips** — step 2's institutional tier (`TTL_CBT`'s shape: a school's own termly
   examinations) is that hedge, and it needs no ministry procurement at all.

### Acceptance tests

- 🟢 **Offline**: a full 30-subject objective paper delivers and scores with the network cable out.
- 🟢 **Marking**: assisted scores agree with WAEC-graded scripts at a stated, measured rate — **and
  the rate is published before the engagement claims the capability** (`P23`'s shape).
- 🔴 **Licence closure**: every dependency's grant byte-read, including the scoring model's
  artefacts — `Gap 246` is this KB's record of model artefacts carrying different terms from the
  MIT code that loads them (`pt_core_news_*` is **CC-BY-SA-4.0**; `es_core_news_*` is **GPL-3.0**).
- 🟡 **No corpus is adopted that cannot be licensed.** `910-F2` found `NOASSERTION` resolving to
  **`CC BY-NC`** twice, including a national syllabus; NC bars a paid engagement outright. If the
  WAEC item bank cannot be licensed, `P29`'s answer applies — **re-author the spine so the client
  owns the grant.**

🔵 **Honest scope.** This is a **6–10 week** discovery-and-prototype shape, not a national rollout:
steps 1, 2, 4 and 6 are deliverable from verified open supply, and step 3 is blocked on a board
agreement no amount of engineering substitutes for.

## P31 — Examination-board engagement where the board publishes nothing (measured `p912`)

**For:** a national or regional examination authority — WAEC, JAMB, NECO, NABTEB, KNEC, CENEVAL,
DEMRE, UNEB, NEAEA — or a ministry buying on one's behalf.

### Why this pattern exists

`P30` scopes building an examination platform. This pattern addresses what `p912` measured about
the **counterparty**: five of eight boards probed **hold their own GitHub namespace and have
published nothing into it**, and three more have had the namespace taken by an unrelated account
(`T37`, `verticals/solutions.md`). So there is no board-published question schema, results format
or blueprint to integrate against — while in Nigeria alone **four independent permissive CBT
implementations** are already integrating against that undocumented target (`p911`).

🔵 **The consequence is specific: the integration contract is the deliverable.** Not the tutor, not
the item generator — the **schema**. Whoever writes it first defines the market, and a board that
already owns its namespace has a publication channel sitting unused.

### Stack

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| Item and blueprint schema | **QTI 3** via https://github.com/QFlowLearn/qti3 | **MIT** (1,072 B · `00ed05b90bf8`, byte-read `p912`) | Do not invent a format. QTI is the only interoperability standard a board can be shown as prior art. This one **renders, scores, validates and migrates** QTI 3 items. 🔴 **Note the address**: this base carried it as `longsightgroup/qti3` since `p900`; it has been **renamed to `QFlowLearn/qti3`** and the old address survives only as a GitHub redirect (`912-F5`). |
| Item rendering (alternative) | https://github.com/Citolab/qti-components | 🔴 **GPL-3.0** | QTI 3 web components for item rendering. 🔴 **Copyleft, and it is a rendering library that ships to the browser** — keep it at arm's length in any proprietary build, exactly as `repos/foundations.md` records. Prefer the MIT row above unless the client's deliverable is itself GPL-compatible. |
| CBT delivery reference | https://github.com/Kirchhoff-dev/cbt-app-updates (offline, 30+ subjects) and https://github.com/edunelsonit/Jambora (Apache-2.0) | permissive | `p911`'s Nigerian cluster. Use them as the **conformance corpus** for the schema: a format three independent implementations can already emit is a format a board can adopt. |
| Past-paper corpus | https://github.com/001kenji/KCSE-predictor (Apache-2.0, 20+ years of KCSE papers), https://github.com/HostServer001/jee_mains_pyqs_data_base (MIT, 14,000 items) | Apache-2.0 / MIT | Longitudinal board papers are the input for blueprint analysis and item generation. Both byte-read. |
| Marking, deterministic | https://github.com/Udayraj123/OMRChecker (OMR) + https://github.com/openedx/edx-ora2 (response assessment) | Apache-2.0 / AGPL-3.0 ⚠️ | ⚠️ `edx-ora2` is AGPL — fine inside an Open edX deployment, a licence event in a standalone service. Read `G1` first. |
| Agent tier | evidence extraction only, scoring deterministic | — | `P9`'s rule, and Annex III's requirement. The model never holds the score. |
| Offline / low-connectivity | https://github.com/learningequality/kolibri (**MIT**) and https://github.com/iiab/iiab (🔴 **GPL-2.0**) | mixed — read before bundling | Non-negotiable for WAEC, KNEC and NEAEA catchments; `ElnatanAnbelu/ethioexam` is the market's own worked example of the same constraint. 🔴 **The two grants differ and the table says so deliberately**: Kolibri is MIT, Internet-in-a-Box is **GPL-2.0** (with LGPL components), so bundling IIAB into an appliance is a copyleft event and Kolibri alone is not. |

### How it wires together

1. **Probe the namespace before the first meeting.** `evidence/p912-board-owner-channel.2026-11-19-p912.tsv`
   has the eight already measured; re-probe on **two channels** (`912-F1`: the search index's
   `user:` arm returns the *same* `422` for a real-but-empty owner as for a nonexistent one, so the
   profile page is the channel that discriminates). 🔵 Walking in knowing the board already owns
   `github.com/<board>` changes the proposal from *"adopt a platform"* to *"publish your schema."*
2. **Normalise the examination vocabulary first.** `p912` found one Ethiopian instrument written
   `EUEE`, `ESSLCE`, `EHSLCE` and `EAES` across repositories, with the university **exit** exam
   sharing an acronym with the **entrance** exam. Build the controlled vocabulary as step one; it is
   a data-contract problem on arrival, not a later refinement.
3. **Emit QTI 3 from the existing third-party implementations** and treat agreement between them as
   the schema's acceptance test.
4. **Keep scoring deterministic and anchored per criterion, with a separate regrade path** (`P9`).
   This is what makes an appeal procedure possible, which is what the EU's Annex III, Vietnam's
   high-risk list and China's `考试评价` scope all actually require.
5. **Publish the schema under the board's own namespace**, Apache-2.0 or CC-BY, as a named
   contractual deliverable.

### The design rules that make it defensible

- 🔴 **Never price board-schema access as an engineering task.** `P30` already states that the
  board agreement is the critical path; `p912` adds that there is **no interface to reverse-engineer
  either**, so a schedule that assumes discovery from documentation is wrong by construction.
- 🟢 **Portability is the client's interest and must be in the contract.** With no published format,
  each board integration is bespoke. Commit to QTI 3 on the wire so a second board is a
  configuration, not a rebuild.
- 🔴 **Run `G1` and `912-G1` over every row above before the kickoff deck.** One AGPL component
  (`edx-ora2`) and one Creative Commons corpus question sit in this stack on purpose.

### Deliverables

A published item-and-results schema in the board's namespace; a QTI 3 conformance suite; a
deterministic marking service with per-criterion evidence anchors and a regrade path; an offline
delivery profile; and the vocabulary register from step 2.

### Estimate

**8–12 weeks** for schema, conformance suite and marking service against **one** board, assuming the
board agreement from `P30` step 3 exists. 🔴 **Without that agreement this pattern does not start**
— and unlike `P30`, no part of it is deliverable from open supply alone, because its subject is the
counterparty's own format.

### Where it does not apply

- Markets where the board **does** publish — none measured so far, but `p912` probed eight of them,
  not all.
- Any engagement where the client wants a tutor or an item generator. That is `P23` or `P29`; this
  pattern is infrastructure for the authority, and its buyer is a ministry.

## P32 — Engagement in an **OEM-occupied** national market: be the interoperability, governance and remediation tier around someone else's pilot (added `p913`)

### Why this pattern exists

`T39` measures a market shape this file had no recipe for. In Ethiopia the national AI-in-education
tier is **already occupied** — Ministry of Education and **Huawei**, national-curriculum AI teaching
assistant for **grades 9–12**, trialling since **2026-05-14** — while the open supply addressing the
*same grades* is `43` repositories of which **`81.4%` carry no licence file at all** (`p912`). Every
other pattern in this file assumes the studio builds the AI tier. 🔴 **Here that bid is already lost,
and bidding it anyway is how an engagement dies.** The work that is still open is the work the OEM
has no incentive to do.

🔵 **Apply this pattern when all three hold** — a state-run or donor-financed national AI programme
with a named vendor; local open supply that is live but ungranted; and connectivity or power as the
binding constraint. **Do not apply it** where the ministry is still specifying (use `P28`,
spec-first) or where no national programme exists (use `P29`/`P31`).

### Stack

| Layer | Repo / artefact | Licence | Why this one |
|---|---|---|---|
| Interoperability spine | `repos/foundations.md` → **OneRoster / xAPI / QTI** shelf (`1EdTech` schemas, `Learning-Locker` is **GPL**, see note) | mixed — **read the column** | The deliverable is that a ministry's systems can exchange roster, result and item data with the vendor pilot. `p913` measures the Ethiopian constraint as **fragmentation**, not bandwidth. |
| Offline / store-and-forward delivery | `P14`'s Africa-origin offline stack, plus the market's own two surfaces: an **MIT offline** Grade 9–12 practice app and an **MIT Telegram** results bot (`agents/top.md`, Ethiopia rows) | **MIT** | `21.7%` penetration and `1,500` connected schools means the delivery surface is **not a browser**. The market already chose offline and messaging; adopt its choice rather than arguing with it. |
| Evaluation / efficacy tier | `P7` attached whole | permissive | An OEM pilot will not publish its own efficacy evidence. A ministry renewing a national programme needs one, and it is a service a studio can sell to the *buyer* rather than to the vendor. |
| Governance tier | `P5`'s governance retrofit, re-aimed at a single national programme | permissive | `T1`/`T39`: here the policy is being written **after** the pilot. The 2026/27–2030 strategy revision is the document to be inside. |
| Teacher enablement | `P10` at system scale | n/a (service) | The reported complaints in comparable programmes are device management, teacher training and staffing — a **services** market, not a licence market. |
| Licence remediation | **`ingest/p913-grant-authority.sh`** over the local cohort, then `G1` | — | `81.4%` ungranted means the live local supply **cannot be contributed** into a government programme as it stands. Remediation is a cheap, concrete, highly visible first deliverable. |

### The sequencing that makes it sellable

1. **Run `G1` and `ingest/p913-grant-authority.sh` over the local cohort first.** You will be telling
   a ministry which of its own country's artefacts are safe to adopt. Nobody else has done this, it
   costs days, and it establishes standing before any build.
2. **Then the interoperability spine**, because it is the one deliverable that is strictly
   complementary to the vendor — it makes the vendor's pilot more valuable, so the vendor is not
   motivated to block it.
3. **Then evaluation and governance**, sold to the ministry, not to the vendor.
4. **Teacher enablement last and largest** — it is the biggest line item and it needs the other
   three to be credible.

### Licence posture of the result

🟢 Studio IP in the adapters, the evaluation harness and the enablement material. 🔴 **The
interoperability shelf is where the copyleft is** — `Learning-Locker` is GNU-family (re-graded
**GPL**, not AGPL, in `p913`; see `913-F1`), so an LRS deployed as a *separate service* is fine and
linking it into a proprietary deliverable is not. Run `G1` before promising either.

### Estimate

**10–14 weeks** to the first three deliverables, assuming ministry access exists. 🔴 **If it does
not, this pattern is not runnable** — there is no self-serve route into a national programme, and
that is the honest gate on it. Teacher enablement is a separate multi-quarter programme and should
be scoped and priced separately.

### Where it does not apply

🔴 Not in the EU, UK or Saudi markets, where the buyer publishes a specification first (`P28`,
`P4`). 🔴 Not where the "national programme" is a procurement notice rather than a running pilot —
then you are in `P28`'s window and should bid the build.

## P33 — Multi-**vendor** LMS agent tier, with the licence boundary drawn at the bridge (added `p914`)

**Why this pattern exists, and why it could not be written before this pass.** `P26` builds a
sanctioned bridge on **one** platform. `P27` builds one adapter across **many campuses on the same
platform**. Neither answers the shape a real group or ministry buyer actually presents: *three
faculties on Moodle, the business school on Canvas, the polytechnic arm on Brightspace, and one
board that wants one assistant.* That pattern needed a **tenant-agnostic** bridge to a commercial
LMS, and until `p914` this base had none — D2L's only row was `POLITEMALL-MCP`, bound to two
Singapore national systems. `T42` records the row that closed it.

🔵 **The design claim is about where the licence boundary goes, not about the agent.** `T42`
measured the tier's two limbs having opposite grants: **bridges are permissive because they are
written to be embedded; plugins are copyleft because they inherit from the platform they plug
into.** That is not a nuisance to route around — it is a free, principled seam. Put the closed
deliverable on the bridge side of it and nothing in the build ever forces disclosure.

### Stack

| Layer | Pick | Licence (byte-read) | Why |
|---|---|---|---|
| Bridge — D2L Brightspace | https://github.com/RohanMuppa/brightspace-mcp-server | **MIT** (`main/LICENSE`, 1,068 B, `sha256₁₂ 047079fbd491`, `p914`) | 🟢 **Tenant-agnostic** — states it works with any school. The row that makes this pattern possible |
| Bridge — Canvas | https://github.com/vishalsachdev/canvas-mcp | MIT | Largest Canvas tool surface in this base (334 ★) |
| Bridge — Canvas + campus portal in one server | https://github.com/SonAIengine/ku-portal-mcp | **MIT** (1,068 B, `aa35608133a4`, `p914`) | Read it for the *composition*: one server, two systems of record. That is this pattern's problem in miniature |
| Bridge — Moodle, read-only then read-write | https://github.com/Faixiang/Moodle-MCP → https://github.com/G36maid/moodle-mcp | MIT | Institutional Web Service API, which is the posture `P26` requires |
| Bridge — Blackboard | https://github.com/bolgerru/blackboard-mcp | 🔴 **no licence** | Read-only reference. **Cannot be copied from.** Blackboard work starts from the vendor REST docs |
| Sanctioned install path | https://github.com/Cvmcosta/ltijs | Apache-2.0 | LTI 1.3 / Advantage. One tool registration per platform, four platforms, one tool |
| Identity of record across vendors | https://github.com/StevenACoffman/roster | **MIT** | **OneRoster v1.2** with authorization enforced *in the database*. 🔴 **Non-optional here** — a multi-vendor tier is multi-tenant by construction, and application-layer scoping will leak one faculty's rows into another's |
| Moodle-side plugin work, if any | https://github.com/SaadRahman01/claude-moodle-dev | **MIT** (1,068 B, `df0b3e71710c`, `p914`) | XMLDB, Hooks API, PHPUnit, Behat, privacy/GDPR and security-review skills. 🟢 The **toolkit** is MIT even though the plugin it produces will be GPL — keep that distinction in the SBOM |
| Reference plugins to read, not to ship | https://github.com/saylordotorg/moodle-local_ai_course_assistant · https://github.com/Berserk-hub150/moodle-ai-skill-navigator | 🔴 **GPL-3.0** both | Saylor Academy's own learning coach, and the most featured AI Moodle plugin measured. **Read for scope decisions; do not vendor** |
| Agent runtime | https://github.com/langchain-ai/langgraph or https://github.com/crewAIInc/crewAI | MIT | Not the differentiator. Pick for the team's familiarity |
| Audit / efficacy | https://github.com/yetanalytics/lrsql | Apache-2.0 | One xAPI statement per tool call, across all vendors — the only place the board sees one number |

### How it wires together

1. **One tool registration per vendor, via LTI 1.3 (`ltijs`).** Four platforms, one tool. This is
   the step that makes the tier sanctioned rather than a credential-sharing scheme, and it is also
   the step procurement actually reviews — run all four registrations as one submission.
2. **Normalise to OneRoster *before* the agent, not inside it.** Put `roster` between the bridges
   and the runtime so "course", "section", "enrolment" and "term" mean one thing. 🔴 The failure
   mode this prevents is the expensive one: an agent whose prompt contains per-vendor special cases
   is a rewrite every time the client acquires another campus.
3. **Keep each bridge a thin, replaceable adapter.** One module per vendor, one interface, no
   vendor type leaking past `roster`. The MIT bridges above are *starting points to read and
   re-implement against an institutional identity* (`P26` step 1), not dependencies to pin — the
   Brightspace server is 68 ★ and one contributor.
4. **Draw the boundary.** Everything above `roster` is the studio's closed deliverable. Anything
   that must live *inside* Moodle — a block, an activity type, a local plugin — goes on the other
   side of the line as a separate **GPL-3.0** repository the client owns, talking to the closed tier
   over HTTP. 🟢 Two artefacts, two grants, no derivative-work argument, and nothing in the closed
   tier is GPL-adjacent.
5. **Emit xAPI into `lrsql` from the normalised layer**, so the statement stream is vendor-neutral
   and the board's dashboard does not need to know which campus runs what.
6. **Run gate `G1` plus `T40`'s triage order** over every address before any of it is written:
   read the `NOASSERTION` rows first, confirm the `NONE` rows are empty, and do not let a
   no-licence bridge (`blackboard-mcp`) enter the build as a "temporary" copy.

### 🔴 The content trap this pattern must route around

If the engagement includes **authoring interactive content**, `T41` applies and it is a stop:
H5P's two runtimes are GPL-3.0 with readable grants, and **both** of its authoring surfaces —
`h5p/h5p-editor-php-library` and `Lumieducation/Lumi` — carry **no licence payload at all** while
being actively maintained. Author in QTI 3 (`P19`), or author inside the client's existing Moodle
where the editor arrives as part of the platform, or scope authoring out. **Do not plan an H5P
authoring feature.**

### Licence posture

**Permissive on the deliverable, end to end.** Every pick on the studio's side of the boundary is
MIT or Apache-2.0, byte-read. The copyleft is real and it is deliberately on the client's side of
an HTTP boundary, in a repository the client owns. 🔵 The GPL-3.0 reference plugins and the
no-licence Blackboard bridge are *reading material*, and the distinction between reading and
vendoring is the one thing in this pattern a security review will check.

### Estimate

**10–14 weeks** for three vendors, read-only, with rostering normalisation and xAPI audit:
2 weeks LTI registrations and institutional identity across three platforms (the slow step is the
client's, not the studio's), 3 weeks `roster` normalisation and tenancy enforcement, 1 week per
vendor adapter, 2 weeks agent tier, 1 week audit, 2 weeks security review. 🔵 **A single-vendor
read-only demo is `P26`'s 4–6 weeks** — do that first and let it earn the multi-vendor scope.
🔴 Add 3–4 weeks per vendor that needs a Moodle-side plugin, and budget it as a separate repository
with a separate grant from day one.

### Where it does not apply

- **One LMS.** Use `P26`. The normalisation layer is overhead the engagement has not earned.
- **Many campuses, one platform, one language.** Use `P27` — it is the cheaper shape and already
  has its in-language cohort measured.
- **Blackboard-only estates.** The only Blackboard bridge in this base is unlicensed, so there is
  no permissive starting point and the adapter is written from the vendor's REST documentation.
- **Where grade *writes* are in scope on day one.** Read-only first (`P26`): writes put the tier
  inside the EU AI Act's assessment scope (**2 Dec 2027**) and inside FERPA record-amendment rules
  in the US, and a multi-vendor write path multiplies both reviews by the number of vendors.

## P34 — Ship a **closed** course-authoring deliverable, now that H5P authoring is ruled out (added `p915`)

**The problem this solves.** `914-F5` established that `h5p/h5p-editor-php-library` and
`Lumieducation/Lumi` — the two H5P authoring surfaces — carry **no licence payload at all** on a
16-filename × 3-branch ladder, while the H5P runtimes carry byte-identical GPL-3.0. The delivery
consequence was blunt: 🔴 **you may lawfully serve H5P and you may not lawfully ship a tool that
makes it.** Any engagement whose deliverable is *authoring* had nothing permissive to stand on.
`p915` measured the tier and found the answer.

**The stack.**

| Layer | Repo | Licence | Why this one |
|---|---|---|---|
| Authoring editor | https://github.com/course-code-framework/coursecode-desktop | **MIT** (1,069 B) | 🟢 The only permissively licensed authoring editor measured in this base — white-labellable outright |
| Course build / packaging | https://github.com/course-code-framework/coursecode | **MIT** (1,069 B) | Course-as-code pipeline, SCORM on output |
| SCORM runtime for playback | https://github.com/jcputney/scorm-again | permissive (in `repos/foundations.md`) | Plays the package in whatever LMS is already in the estate; no LMS fork needed |
| Content ingestion | https://github.com/docling-project/docling · https://github.com/opendatalab/MinerU | permissive | Turn the client's existing DOCX/PDF/slide estate into structured source for the pipeline |
| Generation + citation gate | `pydantic/pydantic-ai` + `P23`'s acceptance test | MIT | Draft activities from the ingested corpus; the citation trail is an output, not a prompt instruction |
| Scheduling (optional) | https://github.com/pieralukasz/true-recall (**FSRS v6**, MIT) | MIT | If the deliverable includes retention, take the scheduler rather than build it (`T43` tier) |

**Wiring.** `docling`/`MinerU` normalise the client's existing material into structured content →
`pydantic-ai` drafts activities against that corpus with `P23`'s hallucination gate in front of
publication → authors review and correct in `coursecode-desktop` → `coursecode` builds a **SCORM
package** → `scorm-again` guarantees playback, so delivery does not depend on which LMS the client
runs. 🔵 **The licence boundary is clean end to end**: every layer is permissive, so the authoring
tool itself can be branded and sold closed.

🟡 **The honest caveat, and it belongs in the pitch rather than the appendix.**
`coursecode`/`coursecode-desktop` are **7 ★ and 5 ★, created 2026-02-12**. This is not a mature
upstream and should be scoped as **a fork you will own and maintain**, not a dependency you will
track. Budget for that explicitly. 🔴 **`915-R-G1` is open:** the SCORM output was read from the
project's description, not generated and validated. **Run one package through `scorm-again` in the
client's actual LMS before signing**, because the entire interoperability claim rests on it.

🔴 **When to reach for Adapt instead.** If the deliverable may be copyleft — a hosted authoring
service, or a deploy-and-extend engagement where the client keeps the result open —
`adaptlearning/adapt_authoring` (GPL, 563 ★) is **far more capable** than CourseCode and is the
category's real anchor. GPL-3.0 has no network-use clause (`913-F1`), so **hosting** it for the
client is unaffected; only a closed, branded derivative is foreclosed.

**Estimate.** 8–10 weeks for ingestion + generation + the citation gate over an existing content
estate, assuming the authoring UI is taken as-is and extended rather than redesigned. Add 3–4 weeks
if the SCORM validation in `915-R-G1` turns up gaps.

## P35 — Rubric grading inside the institution's existing gradebook, with the human-in-the-loop control as a shipped default (added `p915`)

**The problem this solves.** `T1` records that the binding statutes regulate **use**: Oklahoma
SB 1734 bars AI used *solely* for grading, discipline or promotion, and several states require a
district AI policy before deployment. A grading pilot therefore fails on **oversight evidence**, not
on model quality — and a pilot that writes grades straight into the gradebook cannot produce that
evidence after the fact.

**The stack.**

| Layer | Repo | Licence | Role |
|---|---|---|---|
| Gradebook bridge | https://github.com/Yuanpeng-Li/gradescope-mcp | **MIT** (1,068 B) | 🟢 **Grade against a rubric, review regrade requests, manage assignments — with every write previewed before it is applied.** The oversight control is the tool's default, not a policy document |
| Alternative / additional bridges | `vishalsachdev/canvas-mcp` (MIT) · `RohanMuppa/brightspace-mcp-server` (MIT) | MIT | Same seam on Canvas and D2L, so the pattern is not single-vendor (`P33`, `T42`) |
| Deterministic grading where it is possible | https://github.com/ucbds-infra/otter-grader · https://github.com/Submitty/Submitty (BSD-3) | permissive | Anything auto-gradable should never reach a model; reserve the model for prose |
| Learner model / mastery | https://github.com/CAHLR/pyBKT | MIT | Turns a stream of graded attempts into a mastery estimate rather than a score |
| Orchestration + audit | `langchain-ai/langgraph` (MIT) · `langfuse/langfuse` | MIT | Every suggested grade, its rubric citation and the human decision, retained as the oversight record |

**Wiring.** Submissions land in Gradescope/Canvas as they already do → deterministic work routes to
`otter-grader`/`Submitty` → prose goes to the model with the **rubric as the retrieval context**, so
each suggested mark carries the rubric clause it came from → `gradescope-mcp` stages the write and
**holds it for preview** → an instructor approves, edits or rejects → `langfuse` retains suggestion,
citation, decision and identity → `pyBKT` turns the approved stream into mastery estimates.

🟢 **Why the preview step is the commercial centre of this pattern, not a nicety.** It makes "AI is
not the sole determinant" an **architectural property with a per-decision audit trail**, which is
exactly the artefact an Oklahoma, Maryland, Virginia, Idaho or North Carolina deployment has to
produce. 🔵 Sell the audit trail; the grading is the easy half.

🟡 **Caveats.** `gradescope-mcp` is **8 ★, created 2026-03-18** — permissive and small, so treat it
as a component to fork and own. Gradescope itself is a **proprietary hosted platform**: this pattern
layers on a product the client already pays for and does not replace it. 🔴 Confirm the client's
Gradescope terms permit API-driven writes before building on the bridge.

**Estimate.** 6–8 weeks for one course-shape on one gradebook with the audit trail in place; +2–3
weeks per additional LMS bridge, which is mostly configuration because the three bridges share the
seam `P33` describes.


---

## P36 — Student retention / early warning, where the whole model is studio IP (added `p916`)

**When to use it.** A higher-ed or large K-12 client wants to identify at-risk students early.
This is the most-requested application in the market literature this base holds — and `916-F5`
measured the supply side: **there is nothing to adopt.** `student dropout prediction` tops out at
**25 ★** with 20 of 23 rows carrying no licence; `"early warning" student` returns 735 repositories
whose new rows top out at **11 ★**; `dssg/student-early-warning` and `hhy37/student-early-warning`
both read `NOASSERTION` and their payloads do not resolve. **Price this as a build, not an
integration,** and say so in the first conversation — the client has usually been told otherwise.

**What you do adopt is the substrate, and all of it is permissive or client-owned:**

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| Record store | `Apereo-Learning-Analytics-Initiative/OpenLRW` | 🟢 **ECL-2.0** | xAPI/Caliper warehouse with a REST tier. **The only permissive learning-record stack in the field** (`916-R1`). ECL-2.0 permits a closed derivative. 🟡 14 months stale — fork and own it |
| Event source | the client's LMS | client's | Moodle logs, Open edX event tracking or Canvas Live Events — already running, already theirs |
| Learner model | `CAHLR/pyBKT` | 🟢 **MIT** | Bayesian knowledge tracing from UC Berkeley. 🔴 `916-F6`: **ten of ten** higher-star knowledge-tracing repos have no licence file, so this is effectively the field's only licensed primitive |
| Orchestration | `LangGraph` | 🟢 MIT | The intervention workflow — flag, route to an advisor, record the outcome, re-score |
| Advisor surface | `Kanjo-Elkamira-Ndi/Compass` (MIT) or the client's SIS | 🟢 MIT | The human tier. A flag that does not reach an advisor is not an early warning |

**Licence posture.** 🟢 **Permissive end to end.** ECL-2.0 + MIT + MIT + MIT. The risk model itself
is written for the engagement and is **studio IP** — which is the commercial upside of the supply
gap, not only its cost.

🔴 **The regulatory gate is the hard part, and it is `G1`'s sibling.** A dropout-risk score is a
prediction about a named minor or student. Run it against `T1` before architecture: **Oklahoma
SB 1734** bars AI used *solely* for discipline or promotion decisions — so the advisor action must
be recorded as a human decision, not a system one; **California AB 1159** bars student data being
used to train AI models at all, which rules out fine-tuning on the client's own cohort in
California; the **EU AI Act** lists education among Annex III high-risk uses, deferred to **2
December 2027** under Article 113(c) (`916-F10`) — an EMEA deployment shipping before then is
lawful and must still be *built* for conformity, because retrofitting logging and human-oversight
records after the fact is the expensive path. 🔵 **Design the audit trail first and the model
second.**

**Estimate.** 10–14 weeks: 3–4 to stand up `OpenLRW` and land the LMS event stream in it, 3–4 for
features and the `pyBKT` baseline, 2–3 for the intervention workflow and advisor surface, 2–3 for
the conformity and audit tier. 🔴 Add 4+ weeks if the client has no usable historical outcome
labels — and ask about labels before quoting, because most clients do not have them.

## P37 — Oral reading fluency assessment on an LMS a client already runs (added `p916`)

**When to use it.** Early-literacy, primary-education or language-learning engagements —
the highest-value K-12 application of AI that is **not** text generation. 🔵 It also survives the
grading prohibitions `T1` tracks, because a fluency score is a *measurement* offered to a teacher,
not an automated decision about a student. That distinction is what makes it sellable in Oklahoma,
Florida, North Carolina and under the EU AI Act alike.

🔴 **This pattern could not have been written before `p916`, and not because the components were
missing — because this base had published the tier as a void.** See `T44`.

**The recipe, and it has two shapes depending on what the client runs.**

**Shape A — the client is on Moodle (the common case in EMEA and LATAM public education):**

1. Deploy **`justinhunt/moodle-mod_readaloud`** (Poodll ReadAloud) — GPL-3.0-or-later, pushed
   2026-10-28. Guided fluency journey, automatic words-per-minute and accuracy scoring by speech
   recognition, optional comprehension quiz, all inside one Moodle activity.
2. 🟢 **The licence costs nothing here.** It is a Moodle plugin running inside a GPL-3.0 host that
   the client already operates. Distributing a modified plugin obliges you to offer source *to the
   client*, who is the only recipient. **This is the one configuration in which copyleft is free,
   and it is the common one** — do not reflexively route the client to a permissive rebuild.
3. 🔴 Read `916-F2` before the licence review: this plugin has **no licence file at all**. The grant
   is in the `README` and in every source-file header. A procurement checklist that greps for
   `LICENSE` will reject a correctly licensed plugin.
4. Add the speech tier the client's jurisdiction allows — on-premise `whisper`/`whisperX` where
   student voice may not leave the country, which is most of EMEA and increasingly LATAM.

**Shape B — the client needs a standalone or white-label product:**

1. Start from **`OSU-slatelab/AIRFluTe`** (🟢 **Apache-2.0**, Ohio State) — streaming models
   fine-tuned on **children's** speech, with real-time visual tracking and a prompting teacher
   model. 🟡 Idle since 2022: fork and own it.
2. Take the conversational surface from **`dungnotnull/ReadPulse-AI-Agent`** (🟢 MIT) as a
   reference implementation of a voice-agent assessor.
3. Take the **teacher workflow** — class, student, text, recording, error marking, statistics —
   from **`JambuOverflow/lepic`** (🔴 GPL-3.0, ICSE 2021 SCORE winner) as a **design reference
   only**. 🔴 Do not vendor its code into a closed product; read it, then build.
4. Licence posture: 🟢 **Apache-2.0 + MIT, permissive end to end**, provided step 3 stays a reading
   exercise.

🔴 **Data protection is the gate in both shapes.** Children's voice recordings are biometric-adjacent
personal data in every regime this base tracks. Record retention and deletion before you record
anything: under **AB 1159** the recordings cannot be used to train a model at all; under GDPR the
lawful basis for processing a minor's voice is the question procurement will ask first.

**Estimate.** Shape A: **3–5 weeks** — it is largely deployment, configuration and an on-premise
speech tier, which is why it is the one to propose first. Shape B: **12–16 weeks** to a product,
plus the data-protection tier.

## P38 — Issue a verifiable diploma from the LMS the client already runs, under Europass / eIDAS 2.0 (added `p917`)

**Who it is for.** An EMEA institution — university, polytechnic, national training agency — that
must issue credentials a third party can verify without calling the registrar, and that already runs
Moodle, Canvas or Open edX. 🔴 **This is the one pattern in this file with a statutory driver
instead of a value proposition** (`T49`): Europass plus eIDAS 2.0 make learner-held
machine-verifiable credentials a compliance target, and the European Commission publishes the
reference implementation under **Apache-2.0**, so the build-versus-adopt question is pre-answered.

### Stack

| Layer | Repo | Licence | Why this one |
|---|---|---|---|
| LMS (unchanged) | `moodle/moodle` · `openedx/edx-platform` · `instructure/canvas-lms` | GPL-3.0 / AGPL-3.0 | 🔴 Never forked. Completion data is read out over LTI 1.3, so the copyleft stays on their side of the seam |
| Launch + roster seam | `academic-innovation/django-lti` | **MIT** (byte-read 1,098 B) | 🟢 **Live** — pushed 2026-11-17. Use this, **not** `dmitry-viskov/pylti1.3`, which is 27 months idle (`917-F3`) |
| Issuer service | `eu-digital-identity-wallet/eudi-srv-pid-issuer` | **Apache-2.0** (9,425 B) | The Commission's own OpenID4VCI issuer. Deploy it to get a working credential flow before writing any code |
| Issuance library | `eu-digital-identity-wallet/eudi-lib-jvm-openid4vci-kt` | **Apache-2.0** (9,425 B) | Kotlin/JVM issuance half, for binding diploma attributes into the credential |
| Learner wallet (web) | `wwWallet/wallet-frontend` | **BSD** (1,309 B) | 🟢 Browser-first, so **no app install** — the deciding factor for a cohort that will not download anything |
| Learner wallet (mobile) | `a-sit-plus/vck` | **Apache-2.0** (11,358 B) | Kotlin Multiplatform: Android + iOS + JVM from one codebase. Pushed 2026-11-19 |
| Jurisdiction-neutral alternative | `openwallet-foundation/multipaz` | **Apache-2.0** (11,358 B) | 🔵 Swap in when the client is **not** EU-bound and the EUDI stack would over-fit |

### How it wires together

```
Moodle / Canvas / Open edX          (GPL-3.0 / AGPL-3.0 — untouched, not forked)
        │
        │  LTI 1.3 launch + Names-and-Roles + Assignment-and-Grade services
        ▼
academic-innovation/django-lti      (MIT — YOUR tool, a separate work)
        │   reads: learner id, course, completion, final grade
        ▼
your attribute-mapping service      (studio IP — the only closed component)
        │   maps LMS completion → a credential schema (Europass / ELM)
        ▼
eudi-srv-pid-issuer                 (Apache-2.0)
 + eudi-lib-jvm-openid4vci-kt       (Apache-2.0)
        │   OpenID4VCI issuance; SD-JWT VC so the holder discloses selectively
        ▼
wwWallet/wallet-frontend  (BSD)  ──or──  a-sit-plus/vck  (Apache-2.0)
        │
        ▼
employer / another institution verifies offline against the issuer's public keys
```

### Licence posture of the result

🟢 **Every component outside the LMS is Apache-2.0, MIT or BSD, and the LMS is never modified.** The
attribute-mapping service — the part that encodes *this* institution's diploma semantics — is the
studio's own work and can stay closed. This is the cleanest licence posture of any pattern in this
file, and it is clean because the whole tier is integration code, where permissiveness is a
precondition of adoption (`T48`).

🔴 **Two traps.** `Sphereon-Opensource/OID4VC`'s grant is on branch **`develop`**, not `main` — a
`main`-only licence probe reports it ungranted. And `openid/OpenID4VCI` (131 ★) is the
**specification text**, SPDX `NONE`, *not software*: it is not a dependency, and importing it as one
is how a spec repo ends up in a bill of materials.

### Sequencing that makes it sellable

1. **Weeks 1–2 — issue one credential, end to end.** Deploy `eudi-srv-pid-issuer` as shipped, issue
   a hard-coded test credential, verify it in `wallet-frontend`. No LMS involved. This is the demo
   that unlocks the budget, and it needs no integration work at all.
2. **Weeks 3–5 — attach the LMS.** `django-lti` as a registered LTI 1.3 tool; read completion for
   one course only.
3. **Weeks 6–9 — the attribute mapping.** Map that course's completion to a Europass-shaped
   credential schema. 🔵 This is where the engagement's real cost sits, and it is institution-specific
   — which is exactly why it is defensible studio IP rather than something upstream will absorb.
4. **Weeks 10–12 — the mobile wallet, only if asked.** `vck` across Android and iOS. Skip it when
   the web wallet suffices; it frequently does.

**Estimate.** **6–9 weeks** for web-only issuance against one course; **10–14 weeks** with a mobile
wallet and more than one faculty's credential schemas.

### Where it does not apply

🔴 **Outside EMEA, do not lead with this.** North America, APAC and LATAM have no equivalent
mandate, so there is no compliance driver and the pattern has to be justified on
employer-verification value, which is a much harder sale and a longer pilot. For **LATAM**
specifically, `gdgguadalajara/open-badges-platform` (AGPL-3.0, pushed 2026-08-31, Guadalajara) is the
regionally-authored starting point and carries a sovereignty story the EU stack does not — but read
its copyleft first: AGPL s.13 imposes network-use source disclosure on a hosted deployment.
🔴 **And do not propose this on top of the Mozilla badging estate.** `mozilla/openbadges-*` is
MPL-2.0 and marked *"No Longer Maintained"*; `1EdTech/openbadges-specification` is ungranted at four
layers. The badging *platforms* are an archaeological site (`p916`); the infrastructure beneath them
is not.

## P39 — Maths hints, not maths answers, inside an existing tutoring deployment (added `p917`)

**Who it is for.** A client running a maths intervention — district, tutoring provider, or a
university's developmental-maths programme — that has learner mastery data and wants scaffolded
hints rather than worked solutions.

### Stack

| Layer | Repo | Licence | Role |
|---|---|---|---|
| Hint generation | `DigitalHarborFoundation/llm-math-education` | **MIT** (byte-read 1,073 B) | 🟢 RAG for middle-school maths **question answering and hint generation**, with the retrieval corpus separable from the generator |
| Mastery estimation | `CAHLR/OATutor` | **MIT** | Bayesian Knowledge Tracing + a scaffolded-hint UI that already assumes a hint, not an answer |
| Knowledge-tracing models | `pykt-team/pykt-toolkit` | **MIT** | When BKT is too coarse and the client has enough interaction history to fit a deep KT model |
| LMS seam | `academic-innovation/django-lti` | **MIT** | Launch and roster from Moodle / Canvas / Open edX without forking either |
| Local inference | `ollama/ollama` or `vllm-project/vllm` | MIT / Apache-2.0 | 🔴 Minors' interaction data. On-premise is a procurement requirement in most of these buyers (`T6`) |

### How it wires together

```
LMS  ──LTI 1.3──▶  django-lti (MIT)
                        │  learner id + course context
                        ▼
                   OATutor (MIT) ── BKT mastery estimate per skill
                        │  "this learner is weak on fraction equivalence"
                        ▼
          llm-math-education (MIT) ── retrieves from the DISTRICT's own
                        │              curriculum corpus, generates a HINT
                        ▼
                   OATutor's scaffolded-hint UI renders it
                        │
                        ▼
              interaction logged back ──▶ pykt-toolkit (MIT) refits the model
```

🟢 **The composition is the value, and neither project knows about the other.** `OATutor` decides
*what the learner is weak on*; `llm-math-education` decides *what to say about it*. Every component
is MIT, so the result can ship closed.

🔴 **Swap the retrieval corpus before the first demo.** `llm-math-education`'s shipped corpus is
middle-school maths from one US programme. Pointing it at the client's own curriculum is a day of
work and is the difference between a demo and a pilot — and in LATAM or EMEA it is also the
difference between a standards-aligned product and an imported one.

**Estimate.** **4–6 weeks** for one skill area inside an existing OATutor deployment; **8–11 weeks**
with on-premise inference and a client-supplied curriculum corpus.

### Where it does not apply

Not for summative assessment — this is a formative-feedback pattern, and `T10`'s finding that
detection is being abandoned in favour of assessment redesign is the relevant caution: a hint
generator inside a graded assessment is an integrity problem, not a feature. And not where the
client cannot supply a curriculum corpus: without one, the retrieval tier has nothing to ground on
and the output degrades to a general chatbot, which is the pitch `T10` records as fading.

## P40 — Enter an APAC market where the local open shelf is *present but not deliverable* (added `p918`)

**The brief this answers.** A client is deploying into China, Japan, Korea, Vietnam, Indonesia or
Thailand and asks the reasonable question: *what do we adopt locally?* `918-F2` measured the answer
— **157 local repositories, and not one of them passes `918-R1`.** The naive move is to report "no
local supply" (wrong, and `p904` already had to retract that claim once for LATAM) or to adopt a
5 ★ coursework project as a dependency (worse). This pattern does neither.

### Stack

| Layer | Repo | Licence | Why this one |
|---|---|---|---|
| Tutor / classroom agent | https://github.com/HKUDS/DeepTutor | **Apache-2.0** | 60,675 ★, pushed 2026-11-18. 🔵 **Already APAC-origin (HKU)** — this is not a Western import, which matters in the room |
| Multi-agent classroom | https://github.com/THU-MAIC/OpenMAIC | **MIT** | 43,940 ★, Tsinghua. The slide/quiz/PBL generation tier |
| Live classroom | https://github.com/netless-io/flat | **MIT** | 6,443 ★, China-origin, MIT — the one place the local shelf *is* deliverable |
| LMS the client already runs | https://github.com/moodle/moodle | GPL-3.0 | Integrate over **LTI 1.3** or MCP so your tool stays a separate work (`P11`) |
| Requirements input | the `agents/top.md` APAC vernacular table | MIT ×8, Apache-2.0 ×1 | 🔵 **Read, not imported** — see below |
| Compliance tier | your own, per jurisdiction | — | Vietnam 1 Mar 2027 / Korea 2027 / TEQSA action plans |

### How it wires together

1. **Run the vernacular discovery leg first, before the kickoff.** Twelve `search/repositories` legs
   in the local language (the shapes are in `scratchpad/p918/queries-apac.tsv`). Budget: ~1 hour.
2. **Grade every hit with `918-R1`** — ≥ 50 ★, a byte-read grant that is not `NONE`, pushed within
   180 days. Expect **everything to fail**; that is the measured base rate, not a bad search.
3. **Mine the failures for requirements.** `cxkzai/ai-admissions-platform` (MIT, 5 ★) is a
   multi-role admissions advisor; `uczltw6/course-tutor` (MIT, 5 ★) distils a *named teacher's*
   style and treats token cost as a design constraint; `hapince-code/AI-EduForge` (MIT, 6 ★) emits
   PPT **and** interactive courseware **and** test papers from one brief. 🔵 **Three product
   requirements no Western repo in this KB expresses** — delivered free, as a local-language
   specification, by projects you will never ship.
4. **Build on the permissive APAC-origin anchors** — DeepTutor, OpenMAIC, Flat — so the deliverable
   is regionally credible *and* passes `918-R1`.
5. **Attach the compliance tier per jurisdiction**, because it is the earliest deadline in the
   world: **Vietnam's education-AI high-risk obligations bite 1 March 2027 for new systems**, ahead
   of the EU's 2 December 2027.

### Licence posture of the result

🟢 **Clean.** DeepTutor (Apache-2.0), OpenMAIC (MIT) and Flat (MIT) carry no copyleft and no
enterprise carve-out, so a closed client derivative is available. The vernacular repositories are
**read and never linked**, so their licences — including the two ungranted ones — never enter the
build. 🔴 If you do import one, note that `SNOOPY-alt/heuristic-learning-system` is MIT but runs on
**Dify**, which is *not* OSI-permissive: the agent is inheritable, its harness is not.

### Where it does not apply

🔴 **Indonesia and Thailand, where the vernacular leg returned zero.** There is no local shelf to
read for requirements, so step 3 yields nothing and the engagement must get its requirements from
interviews instead. Say so in the proposal rather than returning an empty slide — `918-F2` searched
and found nothing, and an informed gap is information. 🔴 Also not for a client who needs the
deliverable to *be* a local open-source contribution: this pattern produces a closed derivative of
permissive APAC-origin infrastructure, which is a different promise.


## P41 — Ship a Thai or Indonesian tutor where there is no tutor to fork (added `p919`)

**When to reach for this.** The client is in a market where `918-R1` reports the education-agent tier
as empty or `PRESENT — NOT DELIVERABLE` — measured so far for **Indonesia** and **Thailand**
(`p919`), and for Mandarin, Japanese, Korean and Vietnamese (`p918`). 🔵 The instinct on reading
*"no open supply"* is to quote a from-scratch build. **That is the wrong quote**, and `T51` is why:
the agent layer being empty says nothing about the layer underneath it, and in Thailand the layer
underneath passes the threshold outright.

**The wiring.**

| Role | Repo / agent | Licence | Why this one |
|---|---|---|---|
| Tutor runtime | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `Apache-2.0` | **60,684 ★**, pushed 2026-11-18. The anchor tutor on this shelf; it is not localised, which is the point — you localise it rather than find a local one |
| 🔴 **Thai segmentation** | [`PyThaiNLP/pythainlp`](https://github.com/PyThaiNLP/pythainlp) | 🟢 `Apache-2.0` (byte-read, 11,357 B) | **1,175 ★**, pushed 2026-11-13. **Thai has no inter-word spaces.** Free-text answer marking does not work without this. Not optional, not deferrable |
| Local inference | [`ollama/ollama`](https://github.com/ollama/ollama) | 🟢 `MIT` | Keeps student text in-country. `T6` records sovereign inference as a procurement requirement, not a preference |
| Retrieval | [`qdrant/qdrant`](https://github.com/qdrant/qdrant) | 🟢 `Apache-2.0` | Curriculum retrieval; self-hostable beside the model |
| LMS surface | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 `GPL-3.0` — **plugin boundary, do not link into your code** | Dominant in both markets. Ship as a plugin; `T17` has the permissive-extension-point route |
| Curriculum vocabulary (ID) | [`y4zh/kurikulum-merdeka-asesmen-skills`](https://github.com/y4zh/kurikulum-merdeka-asesmen-skills) | 🟢 `MIT` (byte-read, 1,065 B) | 🔵 **Read, do not depend on.** 0 ★ — its value is that it encodes `Kurikulum Merdeka` lesson-module and assessment structure by school level, already shaped as agent skills |
| Teacher console | [`appsmithorg/appsmith`](https://github.com/appsmithorg/appsmith) | 🟢 `Apache-2.0` | Review queue — nothing generated reaches a student unreviewed |

**Order of work.**

1. **Measure the substrate layer before quoting.** Run `918-R1` at the agent layer *and* at the
   language layer. A pass that reports only the first will over-quote the build.
2. **Stand up segmentation first, in Thailand.** It is the component that decides whether free-text
   marking is possible at all, and it is the cheapest thing in the stack to prove.
3. **Harvest requirements from the practitioner repositories — never a dependency.** `T52`: 6 of the
   10 Indonesian repositories carry **no licence file**, including the 115 ★ leader. Read them for
   curriculum vocabulary, assessment formats and what teachers actually generate.
4. 🔵 **If one of those repositories is genuinely needed, open an issue before forking.** A teacher
   who published a working tool and omitted a licence has usually not *refused* one. An email is
   cheaper than a reimplementation and faster than a legal review.
5. **Localise `DeepTutor` against the national curriculum**, with retrieval grounded on curriculum
   documents rather than on the model's priors.
6. **Ship behind the LMS plugin boundary** and keep the teacher approval queue in front of students.

🔴 **Two licence traps specific to this pattern.** A README that says MIT is **not a grant** —
`eldorray/modulajar-ai` claims MIT and has no `LICENSE` file on any probed path. And
`NgodingCik/modul-ajar-generator` is **`CC BY-NC 4.0`**: noncommercial *and* a content licence on a
web application, which is unusable for a client engagement in two independent ways. Byte-read every
grant in this tier; the search channel reports both of these identically as `NULL`/`NOASSERTION`.

🟡 **Rough shape.** 8–10 weeks for Thailand (segmentation is proven early and de-risks the rest);
6–8 weeks for Indonesia, where no segmentation layer is required and the curriculum vocabulary is
richer. Both assume the client already runs Moodle; add 3–4 weeks if not.

## P42 — Build a Mandarin, Japanese, Korean or Vietnamese tutor where there is no tutor to fork (added `p920`)

**When this applies.** An APAC engagement in a market where the client expects you to start from
"the local open-source thing". `p918` measured all four agent tiers as `PRESENT — NOT DELIVERABLE`
(best permissive member 36 ★, 383 days idle) and `p920` measured the substrate layer underneath them
as fully deliverable. **P40 tells you how to enter such a market; this is what you build once you
are in it.** The Thai/Indonesian version is **P41**; this is its APAC-language sibling, and the
difference that matters is the dictionary.

**The licence posture of the result is permissive end to end**, which P41 cannot promise.

### The stack

| Layer | Pick | Licence (byte-read `p920`) | Why this one |
|---|---|---|---|
| Language substrate — ZH | [`hankcs/HanLP`](https://github.com/hankcs/HanLP) | Apache-2.0, 11,357 B `sha256₁₂ c71d239df917` | 36,539 ★, pushed 2026-11-07. Segmentation → POS → dependency parse in one stack. Branch is **`doc-zh`** |
| Language substrate — JA | [`daac-tools/vibrato`](https://github.com/daac-tools/vibrato) or [`taishi-i/nagisa`](https://github.com/taishi-i/nagisa) | MIT *or* Apache-2.0 / MIT | 🔵 **Prefer `nagisa` when you want no dictionary problem at all** — it is self-contained |
| Language substrate — KO | [`bab2min/Kiwi`](https://github.com/bab2min/Kiwi) | Apache-2.0, 11,372 B | 🔴 **Not KoNLPy** — that is GPL-3.0-or-later by byte-read despite a `NOASSERTION` on the API |
| Language substrate — VI | [`undertheseanlp/underthesea`](https://github.com/undertheseanlp/underthesea) | Apache-2.0, 10,765 B | The only Vietnamese member pushed within 180 days |
| Offline / low-bandwidth KO | [`ongjin/garu`](https://github.com/ongjin/garu) | Apache-2.0, 11,358 B | 1 MB model, runs **in the browser over WASM** — put the substrate on the client when connectivity is the constraint |
| Learner-state model | `CAHLR/OATutor` (BKT) or the `pykt-team/pykt-toolkit` models | MIT | Unchanged from P41; the substrate swap does not touch this layer |
| LMS seam | **LTI 1.3** into the client's platform, **MCP** for the agent's read/write | — | Keeps your tool a separate work (README fact 1) |

### Wiring

1. **Tokenise before you prompt, not after.** The substrate's job is to turn a free-text student
   answer into tokens, lemmas and a dependency parse *before* it reaches the model, so that partial
   credit, misconception tagging and the learner-state update key on linguistic units rather than on
   whatever the tokenizer inside the LLM happened to do. This is the step that makes a vernacular
   tutor gradeable.
2. **Key the learner model on substrate output.** BKT/`pykt` skills bind to lemmas and dependency
   relations emitted in step 1, not to raw strings — otherwise every inflection is a new skill.
3. **Keep the LLM for explanation, not for parsing.** The parse is deterministic, auditable and
   free; the explanation is the part worth a model call. This also makes the audit trail the
   regulators in `intel/market.md` ask for (Article 50, Korea's AI Basic Act) a byproduct.
4. **Ship over LTI 1.3 / MCP**, as in P11 and P40.

### 🔴 The dictionary step, and why Japanese costs an extra day

If you choose a MeCab-family tokeniser you are shipping **four owners' licences**, not one:

- **MeCab itself** — `mecab/COPYING` declares **GPL-2.0 *or* LGPL-2.1 *or* BSD-3-Clause**. 🔵 **Take
  the BSD arm explicitly and record that you did**, in writing, in the build. A root-path licence
  scan returns `NO-LICENCE-FILE-FOUND` for this repository and a careless reading of the first-named
  file hands you GPL-2.0 for no reason.
- **UniDic** — `LICENSE.unidic`, BSD, © 2011-2017 The UniDic Consortium. The `LICENSE` beside it is
  MIT and covers only the packaging code.
- **IPAdic** — `mecab-ipadic/COPYING`, a bespoke NAIST/ICOT text that is **not an OSI licence** and
  requires its NO WARRANTY section to travel with every copy you distribute.
- **JumanDic** — `mecab-jumandic/COPYING`, © University of Tokyo.

🟡 And the packaging tier is **stale**: `polm/unidic-lite` is 52 ★ last pushed **2020-09-01**,
`polm/unidic-py` idle since 2025-02-26, `polm/ipadic-py` ungranted. 🔵 **So: `nagisa` or `vibrato`
when the client wants a closed product and a short licence annex; MeCab + UniDic only when you need
its specific dictionary behaviour, and then budget the triage.**

### Estimate

**8–10 weeks** to a production pilot on one language: 1 week substrate integration and tokenisation
contract, 1 week dictionary/licence triage (Japanese only — 0 for ZH/KO/VI), 3 weeks learner model
and content binding, 2 weeks LTI/MCP seam into the client platform, 2 weeks evaluation against the
client's own assessment data. 🔵 The substrate is free, permissive and maintained in all four
languages — **the cost is in the curriculum binding, not the language engineering**, which is the
opposite of what an APAC proposal usually assumes.

### 🔴 What this pattern does *not* cover

A Spanish- or Portuguese-language engagement. `920-R2`: the layer split is only load-bearing where
the language needs its own substrate. For Mexico the agent layer is the whole verdict — 74
repositories, largest 2 ★, nothing to adopt — and the substrate is the global one. Use **P41**'s
build-the-agent shape with the Nueva Escuela Mexicana vocabulary in place of Kurikulum Merdeka.

## P43 — A Türkiye or Gulf engagement: the agent tier is empty and the substrate tier is 1,379 ★ and permissive (added `p921`)

**When this applies.** A client in Türkiye or an Arabic-speaking market asks you to start from "the
local open-source thing" for a tutor that must mark **free-text answers in the local language**.
This base's own shelf said there was nothing to adopt in these languages; that was measured at the
**agent** tier (`p903`, best member 6 ★, mostly unlicensed) and it is still true. `p921` measured
the **substrate** tier and it is the opposite. **P42 is the ZH/JA/KO/VI sibling of this pattern;
the difference here is that the whole stack is one JVM library plus one Python library.**

### The stack

| Layer | Pick | Licence (byte-read `p921`) | Why this one |
|---|---|---|---|
| Language substrate — TR | [`ahmetaa/zemberek-nlp`](https://github.com/ahmetaa/zemberek-nlp) | 🟢 Apache-2.0, 572 B notice, `sha256₁₂ c55ac4a942b0` | **1,379 ★, pushed 2026-11-17.** Morphology, tokenisation, normalisation, spelling correction, NER. 🔴 **JVM** — budget a service boundary if your stack is Python. 🔴 **Do not filter it out on the index's licence field, which says `NOASSERTION`** (`T56`) |
| Pure-Python TR fallback | [`otuncelli/turkish-stemmer-python`](https://github.com/otuncelli/turkish-stemmer-python) | 🟡 Apache-2.0, 11,344 B | Only if a JVM is impossible. **631 days idle — a frozen dependency, vendor it** |
| Language substrate — AR | [`CAMeL-Lab/camel_tools`](https://github.com/CAMeL-Lab/camel_tools) | 🟢 MIT, 1,087 B | 594 ★, pushed 2026-10-14. Morphological disambiguation, **dialect identification**, diacritisation, orthographic normalisation |
| Arabic learner-facing UI reference | [`m7medVision/nakhlah.js`](https://github.com/m7medVision/nakhlah.js) | MIT | 25 ★ — small, and the only permissive Arabic education *application* this base holds. Read it for **RTL learner UI**, which is the slow part to build |
| In-language corpus — TR | [`deeplearningturkiye/turkce-yapay-zeka-kaynaklari`](https://github.com/deeplearningturkiye/turkce-yapay-zeka-kaynaklari) | MIT | 2,432 ★ — 🔴 idle since 2021: **mine it, do not depend on it** |
| Learner-state model | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | MIT | Language-independent; the substrate swap does not touch it |
| LMS seam | **LTI 1.3** into Moodle/Open edX, **MCP** for agent read/write | — | Keeps your tool a separate work from an AGPL/GPL platform |

🔴 **The one repo to refuse:** [`vngrs-ai/vnlp`](https://github.com/vngrs-ai/vnlp) (291 ★, Turkish)
is **AGPL-3.0** by byte-read. A hosted tutor calling it inherits the network-use source-disclosure
duty — which is the whole product.

### Wiring

1. **Morphology first, prompt second.** Turkish and Arabic surface forms explode (agglutination;
   clitics plus optional diacritics), so a free-text answer is lemmatised and tagged *before* it
   reaches the model. Partial credit and misconception tags then key on lemmas, not on whatever the
   LLM's tokenizer did to an inflected form. This is what makes the marking defensible to a teacher.
2. **`zemberek` behind a thin HTTP service** (it is JVM; everything else here is not). One
   `/analyze` endpoint returning lemma, POS and morpheme boundaries is the entire contract.
3. **Normalise before you compare.** `zemberek`'s normaliser and `camel_tools`' orthographic
   normalisation absorb the spelling and diacritic variation that otherwise reads as a wrong answer.
4. **Dialect-gate the Arabic path.** `camel_tools`' dialect identification decides whether to mark
   against MSA or to flag for human review — the single biggest source of unfair marking in Gulf
   deployments.
5. **Learner state and LMS seam exactly as P42.**

**Licence posture:** Apache-2.0 + MIT end to end. Your tutor can be closed and branded.
**Estimate:** 6–8 weeks to a markable free-text pilot in one subject, +2 weeks for the Arabic
dialect gate. **What you are NOT buying:** an education agent — there is none in either language;
you are buying the parsing layer and building the pedagogy.

## P44 — An Indonesian, Hindi or Brazilian-Portuguese engagement: cost it as *no substrate*, deliberately (added `p921`)

**When this applies.** The mirror image of **P43**, and the more common conversation. The market is
huge, the client assumes a local stack exists, and `p921` measured that **it does not**: Indonesian's
leader is 733 days idle, Indic's 1,034, and Portuguese's 375 ★ leader is an unlicensed list
([grading](../evidence/substrate-918R1-grading.2026-11-19-p921.tsv)). **The deliverable of this
pattern is a correctly-costed proposal**, which is worth more than a stack that has not moved in two
years.

### What you tell the client, and what you build

| Instead of | Build | Why |
|---|---|---|
| "we will adopt the national NLP toolkit" | A **multilingual model behind your own evaluation set** — 300–500 marked student answers per subject, collected from the client's own history | `T55`: these languages tokenise on whitespace, so the multilingual model absorbed the job; the toolkit was abandoned *because it was no longer needed*, not because the language is unserved |
| "the local library handles grading" | **Your own glossary and misconception list**, versioned per curriculum (`Kurikulum Merdeka`, NEP/NCF, BNCC) | The curriculum vocabulary is the asset; `919-F5`'s Indonesian supply and `920-F7`'s Mexican supply are both *teachers publishing curriculum artefacts*, which is where to source it |
| "we will fork the catalogue" | 🔴 **Nothing.** [`AI4Bharat/indicnlp_catalog`](https://github.com/AI4Bharat/indicnlp_catalog) (641 ★) and [`Wikidepia/indonesian_datasets`](https://github.com/Wikidepia/indonesian_datasets) (131 ★) carry **no licence file on any probed path** | An unlicensed catalogue is a **reading list, not a source** (`921-R3`). Its rows may be licensed; its selection and schema are not |
| — | 🟡 **One standing re-probe:** [`har07/PySastrawi`](https://github.com/har07/PySastrawi) (366 ★, MIT) is **182 days idle — two days outside `918-R1`**. One push flips the Indonesian verdict | Cheapest watch item on this base's books |

### Wiring

1. **Evaluation set before model choice.** With no substrate to anchor on, the only defensible
   artefact is a marked answer set from the client's own data; it is also the thing that survives a
   model swap.
2. **Glossary as a versioned repo, not a prompt.** Curriculum vocabulary changes by cohort; keep it
   diffable and attach the curriculum version to every marking decision.
3. **Human-in-the-loop on the first cohort, by design, and priced.** This is where the budget that
   would have gone to "adopting the local stack" actually goes.
4. **LMS seam as P43.** In LATAM the platform is overwhelmingly Moodle or Chamilo (GPL-3.0), so the
   LTI/MCP boundary is what keeps your work a separate, closeable one.

**Licence posture:** whatever you write, plus the model's terms — there is no third-party copyleft
in the path, because there is no third party.
**Estimate:** 8–10 weeks, of which ~3 are the evaluation set and glossary. 🔵 **Say this in the
proposal**: the reason it is not 6 is the absence this pattern is named for, and a competitor who
costs it at 6 is costing a library that has not been pushed since 2024.


## P45 — A Central European engagement: one MPL-2.0 binary covers Czech and ~100 other treebanks (added `p922`)

**When to use it.** A Moodle or ILIAS rollout across Czechia, Slovakia, Poland, Hungary or the
Baltics, where the client wants free-text marking, search or feedback in the local language and the
proposal must name a substrate rather than hand-wave at "a multilingual model".

**What you wire together.**

1. **Platform** — https://github.com/moodle/moodle (GPL-3.0) or
   https://github.com/ILIAS-eLearning/ILIAS (GPL-3.0), whichever the client already runs.
2. **Language substrate** — https://github.com/ufal/udpipe (**MPL-2.0**, 426 ★, byte-read 16,725 B
   `sha256₁₂ 1f256ecad192`). Tokenise, tag, lemmatise and dependency-parse from **one binary across
   ~100 Universal Dependencies treebanks** — this is the step that makes the pattern cover the
   region rather than one country. For Hungarian specifically, prefer
   https://github.com/huspacy/huspacy (Apache-2.0, 194 ★): it is a drop-in spaCy pipeline and
   permissive, so it needs no licence conversation at all.
3. **Agent tier** — https://github.com/HKUDS/DeepTutor (Apache-2.0) or
   https://github.com/crewAIInc/crewAI (MIT), reached from the LMS over **LTI 1.3** or MCP.
4. **Evaluation** — https://github.com/agentscope-ai/OpenJudge (Apache-2.0) with
   https://github.com/AI-for-Education/pedagogy-benchmark (MIT) as the education rubric, run on a
   held-out set of the client's own marked scripts.

**How to wire it so the licences hold.** Run UDPipe as a **separate process behind HTTP or MCP**,
not linked into a Moodle plugin. 🟡 MPL-2.0 is **file-level** copyleft: modifications to MPL files
must be published, your own files need not be, and MPL-2.0 is GPL-compatible by construction
(s.3.3) — so it composes with a GPL-3.0 platform where **MPL-1.1 would not**. That distinction is
the whole reason this base now reads MPL versions (`922-F3`); until this pass it published a bare
`MPL`, which is unquotable either way.

🔴 **The one check to run before quoting this.** `ufal/udpipe` was pushed **2026-06-11** — inside
`918-R1`'s 180-day window with **19 days of margin**. Re-probe the push date before the proposal
goes out; if it has crossed, the pattern degrades to P44's shape and the budget changes.

## P46 — Enter a market this base told you was dead: the Philippines, Bangladesh and Ethiopia (added `p922`)

**When to use it.** A Filipino, Bengali or Amharic engagement — three tiers that `921-R1` predicted
had no adoptable substrate and that **measurement contradicted**. Read this as the correction to
P44: it exists to stop a studio costing a from-scratch language budget where a maintained
permissive stack is already on the shelf.

**What you wire together, by language.**

| Market | Substrate (all byte-read `p922`) | What it gives you | What is still yours to build |
|---|---|---|---|
| **Philippines** (TL) | https://github.com/ljvmiranda921/calamanCy — **MIT**, 77 ★, 2026-10-05 | spaCy pipelines on Universal Dependencies + TLUnified: tokenisation, POS, NER | Domain lexicon, and the code-switching case — Taglish is the normal register in Philippine classrooms and no pipeline here handles it |
| **Bangladesh / West Bengal** (BN) | https://github.com/sagorbrur/bnlp — **MIT**, 313 ★, 2026-10-31 | Tokenisation, embeddings, POS, NER, a sentencepiece model | Curriculum alignment; the stack is general-purpose, not education-tuned |
| **Ethiopia** (AM) | https://github.com/sefineh-ai/Amharic-Tokenizer — **MIT**, 99 ★, 2026-09-24 | Ge'ez-script tokenisation — and **only** tokenisation | 🔴 Tagging, parsing and any morphological analysis. This tier passes at exactly one layer; cost it that way |

**The rest of the stack is the same in all three** and is unchanged from P42: an Apache-2.0 or MIT
agent tier (**DeepTutor**, **crewAI**), served over **LTI 1.3** into whatever LMS the client runs,
with **OpenJudge** + **pedagogy-benchmark** as the efficacy harness, and a client-specific
evaluation set built in week one rather than month six.

🔵 **The sequencing that makes this pattern cheap.** Build the evaluation set **before** the agent
tier. In all three markets the substrate gives you tokenisation and tagging and nothing about
whether a tutor's output is any good in that language — so the evaluation set is the long-lead item
and the only artefact that cannot be bought.

🔴 **And the three tiers this pattern does *not* cover, named so they are not assumed.** **Khmer,
Lao, Kiswahili and Basque are `NOT DELIVERABLE`** — best members 86 ★ at 247 days idle, 35 ★, 9 ★,
and 38 ★ at 339 days idle respectively. There, P44's costing stands: a multilingual model plus your
own evaluation set and glossary. 🟢 **Lao is the exception worth proposing to a client as goodwill**
— https://github.com/wannaphong/LaoNLP is Apache-2.0 and actively maintained and fails `918-R1` on
**star count alone**; upstreaming one engagement's work would carry the tier.

## P47 — The localisation kick-off: clear the curation you are about to copy (added `p923`)

**For:** the first two weeks of any vernacular or multi-market education engagement, before a line
of the tutor is written. **Cost:** ~3 days, no model spend.

🔵 **The thing nobody budgets for.** A localisation engagement's first act is always the same: find
the national "awesome" list for the language, and work the stack out from it. That list *is* the
deliverable you are copying — its curation is months of somebody's unpaid work — and in **13 of the
20 tiers this base has byte-read it carries no grant at all**. 🔴 In one more
(`jnehring/awesome-low-resource-languages`) the grant is **CC-BY-SA-4.0 declared only in the
README**, which means a derived index inherits **share-alike** and neither GitHub's licence field
nor a `LICENSE`-file probe will tell you.

### The three days

| Day | Do | With |
|---|---|---|
| **1** | Run the **grant gate** over every catalogue, library and corpus in the tier — not the libraries alone. Catalogues are usually missed because they look like documentation | `ingest/p913-grant-authority.sh OUT.tsv <slug>...` — gate `923-G1` |
| **2** | For every `NO-LICENCE-FILE-FOUND`, run the **structural** prose probe: a `## License` heading, then the grant string within ~6 lines of it. 🔴 **Not** a README substring grep — on the four largest ungranted catalogues that invents a grant for three of four, because a catalogue's content *is* other projects' licences | [`evidence/catalogue-prose-grant-probe.2026-11-19-p923.tsv`](../evidence/catalogue-prose-grant-probe.2026-11-19-p923.tsv) is the worked example |
| **3** | Split the result three ways and **write the email on day 3, not month 3** | below |

### The three buckets, and what each one costs

| Bucket | What it means | Action |
|---|---|---|
| 🟢 **Granted, software licence** — `crownpku/Awesome-Chinese-NLP` (Apache-2.0), `wannaphong/Awesome-Lao-NLP` (MIT) | copy the curation, keep the notice | ship it |
| 🟡 **Granted, content licence** — `taishi-i/awesome-japanese-nlp-resources`, `JousiaPiha/awesome-finnish-nlp`, `tuanone123/awesome-vietnamese-llm-dataset` (CC0-1.0); `bilalabic/awesome-turkish-datasets` (CC-BY-4.0) | CC0 obliges nothing; CC-BY obliges attribution **in the derived index**, which teams forget because an index does not feel like a work | add the attribution line to the artefact, not to a slide |
| 🔴 **Ungranted** — the ZH, KO, AR, HU, BN, HI, KM, TH, TR and PT catalogues | you have **no licence to copy the curation**, however public the repository is | **email the curator.** They are almost always one person, usually responsive, and a two-line permission is worth more than a month of legal review |

🔵 **Why the email is the pattern and not a footnote.** Four of the five catalogues `p922` probed
and nine of the fifteen `p923` probed are ungranted *because nobody decided they were software* —
a curated index is written as documentation and published without a licence choice ever being made.
🟢 **That is the opposite of a refusal**, and it is why this is a three-day task rather than a
blocker: the usual answer to "may we build on your list, and would you like a licence on it?" is
yes, plus an `MIT` or `CC-BY-4.0` commit that helps every later engagement in that tier.

🔴 **Where this pattern does not apply:** **Tagalog, Czech, Amharic, Kiswahili and Basque have no
catalogue to clear.** Four of the five have a maintained permissive *library* (P45, P46) — so go
straight to the library tier and budget the curation as **your own work product**, which is the one
case in this pattern where the curation becomes an asset you own outright.

## P48 — The regulated-market tutor: ship the evidence layer, not the agent (added `p925`)

**For:** any education engagement in EMEA, North America or Vietnam/South Korea where an agent will
touch a grade, an admission or a discipline decision. **Cost:** ~6–8 weeks for the evidence layer;
the tutor is adopted, not built. **Licence posture of the result: 🟢 fully permissive.**

🔵 **The insight is `intel/trends.md` `T60`.** Four regulatory regimes — EU AI Act high-risk
(enforcing since **2026-08-02**), US state human-oversight statutes, Vietnam's AI law (in force
**2026-03-01**), and LATAM's absent-institutional-strategy gap — are discharged by the **same four
capabilities**. None of the nineteen permissive education agents shelved in `p925` provides any of
them. So the differentiated deliverable is the layer underneath, and the tutor above it is
interchangeable.

### The wiring

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| Tutor (interchangeable) | https://github.com/lynote-ai/ai-tutor | MIT | 🟢 "Only teaches a sentence it can quote" — extractive grounding is a *product rule*, so every claim already has a citation to put in the record |
| Mastery model | https://github.com/chuma-beep/mathua | MIT | 3,015 concepts with **mastery gating**; the gate decision is the auditable event |
| Learner-model maths | https://github.com/CAHLR/pyBKT | MIT | Bayesian knowledge tracing — a defensible, inspectable mastery estimate rather than a model's opinion |
| **Evidence store** | https://github.com/yetanalytics/lrsql | Apache-2.0 | xAPI LRS. Every tutor turn, gate decision and human override becomes a statement with an actor, verb, object and timestamp |
| **Evidence pipeline** | https://github.com/openfun/ralph | Apache-2.0 | xAPI ingestion/validation; keeps malformed statements out of the record you will be audited on |
| **Outcome evidence** | https://github.com/microsoft/StudentSim | MIT | 🟢 **The piece that did not exist before `p925`.** Build per-student simulators, run the tutoring policy against them, and keep the result — this is how you answer "durable learning gains" before a child is involved |
| Human-in-the-loop UI | https://github.com/thm-mni-ii/feedbacksystem | Apache-2.0 | EMEA-origin, institution-run, **Helm chart on Artifact Hub** — the review queue a teacher actually signs off in |
| Accessibility gate | https://github.com/ucfopen/UDOIT | 🔴 GPL-3.0 | Run as a **separate service** beside the LMS, never linked in. WCAG findings are a tender line item in EMEA public procurement |

### The four capabilities, concretely

1. **Human-in-the-loop record.** Every consequential decision writes two xAPI statements to `lrsql`:
   the agent's *proposal* and the human's *disposition*. 🔴 The statute wording to satisfy is
   "AI may not be the **primary basis**" — which is a claim about process, so the record must show a
   human disposition exists for **every** proposal, not that one exists on average.
2. **Consent state.** One table, per student, with `opt_in | opt_out | not_required` and the
   jurisdiction that determined it. Hawaii H.B. 5253 requires opt-**in**; Alabama H.B. 1227 requires
   an opt-**out**; make it configuration, because `p925`'s LATAM leg found Brazil tightening toward
   the EU model while Argentina loosens.
3. **Data-flow attestation.** California AB 1159 would bar student data from training AI models.
   `lynote-ai/ai-tutor` is bring-your-own-key and self-hosted; pin the provider's no-training terms,
   and log the egress boundary so the attestation is evidence rather than a promise.
4. **Grade-band gating.** New York A 9190 would limit classroom AI to **grade 9+** with diagnostic
   and special-education exceptions. Gate at the orchestration layer, not in the tutor's prompt.

🟢 **Why it is sellable four times.** The same implementation is the EU conformity file, the US
oversight record, Vietnam's high-risk documentation and LATAM's missing institutional strategy. The
tutor is localised per market; the evidence layer is not.

🔴 **What this pattern does *not* do.** It does not make a non-deliverable tutor deliverable. If the
client has already chosen `CaviraOSS/PageLM` or `chadyi/StudyOnTV`, the grant forbids the engagement
regardless of what is logged underneath — see `925-F2`.

## P49 — The multi-tenant studio platform: one deployment, many client institutions, permissive throughout (added `p925`)

**For:** a studio that wants one platform serving several client institutions rather than a fork per
client. **Cost:** ~4–6 weeks to a first tenant. **Licence posture: 🟢 fully permissive
(Apache-2.0 + MIT).**

🔴 **Why this was impossible before `p925`.** Every LMS on this base was either copyleft (Moodle
GPL-3.0; Open edX and Canvas AGPL-3.0; Chamilo and ILIAS GPL-3.0) or permissive **and single-tenant
by design** (Artemis, Kolibri, OpenOLAT). A studio had to choose between a grant it could not ship
and a deployment per client.

### The wiring

| Layer | Component | Licence | Role |
|---|---|---|---|
| **Platform core** | https://github.com/pacewisdomhq/TutorLoom | Apache-2.0 (11,362 B, `a89039268428`) | 🟢 **Self-hosted multi-tenant LMS** — Django 6 + DRF + React; course builder, trainer and student portals, progress tracking. The **first permissive multi-tenant LMS on this base** |
| Tenancy + billing reference | https://github.com/3yangyang9/DeepTutor-AILearning | Apache-2.0 (11,408 B, `cd2f54e1e506`) | 🟢 Read this for the **four-level tenancy model** (platform → institution → campus → class) and the **billing-policy layer**. APAC-origin, and the only permissive artefact here that treats *who pays* as a first-class concern |
| Competency graph | https://github.com/iblai/lms | MIT | Competencies, not courses, as the primary object — the model a corporate-academy tenant actually wants |
| Per-tenant microsites | https://github.com/haxtheweb/haxcms-php | Apache-2.0 | 🟢 **No database.** Generate a site per cohort and discard it; carries an **OpenSSF Scorecard** badge, which is the only supply-chain posture on this shelf |
| Content as files | https://github.com/tutors-sdk/tutors | MIT | Course-as-filesystem: an agent authors content by writing files, with no API to go through |
| Live coding classroom | https://github.com/SJRiz/pytogether | MIT | Browser-based collaborative Python with shared canvas and voice — nothing installed on a student machine |
| Model serving | https://github.com/ollama/ollama + https://github.com/vllm-project/vllm | MIT / Apache-2.0 | Per-tenant model isolation |
| Metering | https://github.com/BerriAI/litellm | MIT | Per-tenant token attribution — pairs with TutorLoom's tenancy and DeepTutor-AILearning's billing model |

🔵 **The sequencing that matters.** Stand up TutorLoom first and get **two** tenants running before
adding any agent. Multi-tenancy defects are discovered at the second tenant, never the first, and
they are structural — tenant-scoped querysets, per-tenant storage prefixes, per-tenant model keys.
Adding an agent before the second tenant exists means debugging two new systems at once.

🔴 **The honest limits.** TutorLoom is **98 ★** — adopting it means being a significant fraction of
its user base, so budget for upstream contribution and read the tenancy isolation yourself rather
than assuming it. `3yangyang9/DeepTutor-AILearning` is **not** a fork of `HKUDS/DeepTutor` despite
the name: different owner, different grant, different architecture. And 🔵 **nine of these components
are region-unplaced** (`925-F7`), so none of them carries a localisation assumption you can inherit.

## P50 — The curriculum-graph decision: three assets, three grants, and only one you can ship (added `p925`)

**For:** the week in any K-12 or exam-prep engagement when someone proposes "just use the open
curriculum graph". **Cost:** 2 days to decide; weeks to months if you decide wrong.

🔴 **The trap, stated once.** The two largest open curriculum graphs in this industry have **15,000
stars between them and neither is governed by a software licence.** A pass that reads the licence
field, sees something plausible, and ships, has shipped a licence breach.

| Asset | ★ | Grant (byte-read `p925`) | Kind of licence | Can a client engagement ship it? |
|---|---|---|---|---|
| https://github.com/xiaoyang111222/cn-math-taxonomy | **8,648** | **`CC BY-NC 4.0`** (19,347 B, `41003d4a7474`) | 🔴 **content**, **NonCommercial** | 🔴 **No.** 1,644 knowledge points, 2,403 prerequisite edges, 6,723 items, aligned to the Chinese national standard, with an adaptive prerequisite diagnostic — the best structure for the region and it forbids commercial use |
| https://github.com/withmarbleapp/os-taxonomy | 7,725 | `ODbL-1.0` | 🔴 **database** | 🟡 **Yes, with share-alike on the database.** A derived or extended graph must be released under ODbL. Model the obligation before building on it |
| https://github.com/learning-commons-org/knowledge-graph | 169 | 🔵 **split: code MIT, data per dataset** (5,789 B, `d849ffef4f98`) | 🔴 **per-asset** | 🟡 **Per dataset, every time.** *Open* tiers are usable; the licence states in terms that **Open+Gated** and **Gated** content are "not covered by CC BY 4.0, CC0, or any other open license referenced here" |
| https://github.com/chuma-beep/mathua | 430 | 🟢 **MIT** (1,074 B, `6bd7c2a354d5`) | 🟢 **software**, and the graph ships inside it | 🟢 **Yes.** **3,015 concepts** with mastery gating and FSRS review, Go + Next.js, self-hostable |

### The two days

| Day | Do |
|---|---|
| **1** | **Byte-read the grant of every curriculum asset in the proposal**, not the licence field. 🔴 All three of the large ones report `NOASSERTION` on `search/repositories` — the value this base has 553 rows of experience reading as *"the detector did not recognise the text"*, which is also exactly how a NonCommercial term enters a shelf (`925-F2`). Fetch `LICENSE`/`LICENSE.md` from `raw.githubusercontent.com` and **read it**. |
| **2** | Classify into **software grant** / **database grant** / **content grant** / **per-asset**, then decide. 🟢 **Default to `chuma-beep/mathua`**: it is the only one of the four with a software licence, it is MIT, and its graph is large enough (3,015 concepts) for a real engagement. Reach for `os-taxonomy` only if you can accept ODbL share-alike on your derived graph, and for `cn-math-taxonomy` only via a licence negotiated with the author. |

🔵 **The structural fix, if the client needs Chinese-curriculum alignment specifically.** Do not copy
`cn-math-taxonomy`. Use its *public structure* as a specification — knowledge points, prerequisite
edges, curriculum-standard alignment, prerequisite diagnostic — and build the graph from the client's
own licensed textbook corpus into `mathua`'s MIT schema. 🟢 You keep the architecture, which is the
part that took judgment, and you own the data, which is the part that carries the grant.

🔵 **Why this pattern exists as a pattern.** `intel/trends.md` `T25` predicted the licence trap would
move from code to the data and content assets, where no index can see it. `p925` found the second
instance at **8,648 stars**. Two instances at seven and eight thousand stars is a regularity, and a
regularity in this position needs a standing procedure rather than a warning.

## P51 — The permissive courseware production line: a week of interactive lessons, generated, graded and delivered, with nothing copyleft in the shippable path (added `p926`)

**What it is.** A teacher names a topic and a week's worth of **interactive** courseware comes out —
slides, in-lesson activities, a quiz, and the marking for it — delivered through whatever LMS the
client already runs, with the generated artefacts and the generator both licensed for a closed,
branded deliverable.

🔴 **Why this pattern did not exist before `p926`.** `agents/top.md` recorded `frametell`
(**AGPL-3.0**) as the only open courseware-*production* agent in this KB. Every content-generation
recipe therefore had to either go copyleft or stop at tutoring. **`xingjunm/autoppt` is MIT**
(byte-read `main/LICENSE`, 1,092 B, `sha256₁₂ db50831211a3`), created 2026-11-02, 57 ★, and
generates interactive lecture slides a week at a time driven by **Claude Code or OpenAI Codex**.

**The wiring.**

| Step | Component | Licence | What it does here |
|---|---|---|---|
| 0 | **G1 licence gate** | — | Run it first, as always. Every component below is MIT or Apache-2.0; the only copyleft in this recipe is the LMS, and step 4 is what keeps it at arm's length |
| 1 | `xingjunm/autoppt` | **MIT** | Teacher gives a topic and a week's scope → interactive slide decks and in-lesson activities. Runs under Claude Code or Codex, so it is driven by the same agent runtime as the rest of the studio's tooling |
| 2 | `THU-MAIC/OpenMAIC` | **MIT**, 43,952 ★ | The multi-agent classroom tier: generates quizzes and project-based activities from the same source, and **grades quiz answers**. Already this KB's largest MIT education agent |
| 3 | `proyecto26/notebooklm-ai-plugin` (**optional**) | **MIT** | Where the client wants audio overviews or video from the same material, this reaches NotebookLM's 9 artefact types from the agent. 🟡 **It is a client for a hosted proprietary service** — the MIT grant covers the plugin, not NotebookLM. Drop this step for an air-gapped or data-resident client |
| 4 | `Cvmcosta/ltijs` | **Apache-2.0** | **LTI 1.3 tool provider.** This is the step that matters legally: the courseware is delivered to Moodle (GPL-3.0), Open edX (AGPL-3.0) or Canvas (AGPL-3.0) **as a separate work over a standard protocol**, so no copyleft reaches the generated artefacts or the generator |
| 5 | `Faixiang/Moodle-MCP` or `vishalsachdev/canvas-mcp` | **MIT** | Read-only MCP into the live LMS so the generator sees the real course structure, deadlines and roster shape before it writes anything |

**Licence posture of the result:** 🟢 **MIT/Apache-2.0 end to end in the shippable path.** The LMS
stays copyleft and stays *separate*; the client may take a proprietary derivative of everything the
studio writes.

**Build estimate:** 5–7 weeks. Most of it is step 4 and the LTI launch/grade-passback
round trip, not the generation — steps 1 and 2 work out of the box.

🔴 **The two things that will bite.** **(a)** OpenMAIC declares **178 npm packages with no lockfile
on any path probed** (`p905`) and AutoPPT is three weeks old — vendor both at a SHA and build your
own lockfile before anything is promised. **(b)** Automated marking is a **regulated act** in a
growing list of jurisdictions: Oklahoma SB 1734 bars AI used *solely* for grading, and the EU's
Annex III puts student evaluation in the high-risk tier. **Step 2's grading output must land in
front of a human with an override**, and the override must be logged — see `intel/trends.md`
**T1** and **T60**.

## P52 — The offline tutoring appliance: a tutor that never reaches the network, and measures itself anyway (added `p926`)

**What it is.** A tutoring device or app for a school with no reliable connectivity — or for a
client whose rules forbid student work leaving the premises — that diagnoses *which
misconception* a learner holds, schedules revision against it, and **produces the evidence a
regulator or a board will ask for**, all without a server.

🟢 **Why now.** `p926` shelved **two independent MIT implementations of this design from unrelated
teams on two continents** (`intel/trends.md` **T62**), plus the cold-start learner model that makes
it work on day one with no interaction history.

**The wiring.**

| Step | Component | Licence | What it does here |
|---|---|---|---|
| 1 | `ArushJain-697/namma-ai` (**SAKSHI**) | **MIT** | **The reference implementation of the whole appliance**: Raspberry Pi 5, 176×220 screen, three buttons, USB camera to photograph a worksheet. Ships **GURU-0.6B** as a release artefact, and documents its retention maths in-repo. Start here rather than from scratch |
| 2 | `siyegs/rung` | **MIT** | The phone expression of the same loop, and the better source for **the misconception-diagnosis step**: it infers which specific mistake recurs and rebuilds the plan around it, entirely on-device |
| 3 | `farroshsy/hcie-system` | **MIT** | **The cold-start learner model.** Mastery as a lagged-Kalman estimate over a prerequisite graph — **no per-learner embeddings, no GPU, no interaction history required**. This is what makes day one work; published at **AUC 0.6051**, honestly reported as on par with baselines |
| 4 | `CAHLR/pyBKT` | **MIT** | The adoptable, maintained knowledge-tracing library for the steady state once interaction history exists. Swap in behind the same interface as step 3 |
| 5 | `clementina-tom/PLRS` constraint layer | **MIT** | The **DAG prerequisite gate** — the component with the strongest published result in this KB (**0% prerequisite violations vs 81%+** for collaborative filtering). Keeps the appliance from ever recommending a topic the learner is not ready for, which is a pedagogical guarantee you can write into a contract |
| 6 | `elimu-ai/webapp` + `elimu-ai/appstore`, or `learningequality/kolibri` | **MIT** | Content delivery and **APK distribution with no app store and no network** — the tier this KB has verified for Sub-Saharan deployment |
| 7 | `mad707/masar`'s evaluation protocol | **MIT** | Not a dependency — **a method to copy**: the strict student-level, time-respecting, leak-free split. Reuse it to report your appliance's numbers so they survive scrutiny |

**Licence posture:** 🟢 **MIT end to end.** Every component, including the content-delivery tier.
This is the second end-to-end permissive pattern in this file and the first that is also
evidence-producing.

**Build estimate:** 8–10 weeks to a deployable pilot from SAKSHI's hardware design; 4–5 weeks
for the phone-only variant starting from `rung`.

🔵 **The design rule that makes this sellable.** An on-device tutor is an **unobservable** tutor, so
the measurement has to be built in at step 3, not bolted on. The appliance should write a local,
exportable interaction log in the shape masar's protocol expects — then a periodic sync (or a
physically carried file) produces exactly the outcome evidence the North American, EU and Vietnamese
regimes are all converging on, **without the student's work ever leaving the device**.

## P53 — Attaching evidence to a tutor the client already has (added `p926`)

**What it is.** The short engagement for a client who has **already bought or built** an AI tutor
and now has to defend it — to a board, a ministry, a procurement review or an EU conformity
assessment. You do not replace the tutor. You instrument it.

🔴 **The problem, measured.** `intel/trends.md` **T61**: the two largest open education agents in
existence publish **no learning-outcome study**, and neither do most commercial ones. The evidence
layer exists as a **separate, permissively licensed population** that no product cites.

**The wiring.**

| Step | Component | Licence | What it does here |
|---|---|---|---|
| 1 | `Apereo-Learning-Analytics-Initiative/OpenLRS` or an **xAPI** LRS | Apache-2.0 | Capture the interaction stream from the existing tutor. If it emits nothing, the LTI 1.3 grade-passback and the LMS MCP seams (`Faixiang/Moodle-MCP`, `vishalsachdev/canvas-mcp`, both MIT) are the two places to tap it without modifying the product |
| 2 | `mad707/masar` | **MIT** | **Copy the protocol, not the model.** Strict student-level, time-respecting split, leak-free at every rung, and a ladder of baselines — item-only, IRT, PFA logistic regression — *before* anything deep |
| 3 | `CAHLR/pyBKT` and `pykt-team/pykt-toolkit` | **MIT** | The maintained estimators to run on that stream |
| 4 | `Aditya-Ranjan1234/NS-CausalKT-Agentic-Grader` | **MIT** | Where the client needs **diagnosis rather than prediction** — a neural-symbolic design whose symbolic layer gives a defensible account of *why* a learner was marked as they were. This is the shape that survives a jurisdiction that bans AI-only grading |
| 5 | `clementina-tom/PLRS` | **MIT** | Audit the tutor's *sequencing*: measure its prerequisite-violation rate against PLRS's DAG. **81%+ for collaborative-filtering baselines** is the number to beat, and most engagement-optimised products will not |

**Licence posture:** 🟢 MIT/Apache-2.0 throughout. Nothing here is delivered to the end user, so
even the copyleft tutor underneath is untouched.

**Build estimate:** 3–4 weeks. This is the cheapest pattern in this file and, given
`intel/market.md`'s regulatory calendar, likely the most frequently needed.

🔴 **Set the expectation before step 2 runs.** The published results say the simple baseline is
competitive (**DKT ≈0.75 vs PFA 0.760**). **A fair evaluation may well show the client's tutor is
not beating logistic regression.** That is a finding worth being paid for, and it is much cheaper to
agree that in the statement of work than to discover it in the readout.


---

## 927-G1 — Payload-address licence gate (extends `904-G1`) — added `p927`

`904-G1` said: when a repository's payload is data or content, probe the **payload directory**
(`dados/LICENSE.md`) before recording an SPDX value, because a root-only probe reports the wrong
grant rather than no grant. `p927` found the same failure one level up, on a row this base
publishes.

**The case.** `CAHLR/OATutor` is **MIT**, byte-read, 283 ★, UC Berkeley, and is published in
`agents/top.md` as an intelligent tutoring system *"with open problem banks"*. The problem banks
are in **`CAHLR/OATutor-Content`** — a **different repository** — which has **no licence file on 14
probed paths** and reports SPDX `NONE`. Both channels agree, so the two-channel rule does not fire.
The grant exists **only as prose in the README**: CC BY 4.0, with attribution recorded **per JSON
record**, per hint, scaffold and problem, because the content is curated from OpenStax plus
classroom syllabi.

**Run this before writing any row whose value is content.**

- **Step 0c — find the payload's address.** Read the README of the code repository for a *Content
  Repository*, *Data*, *Corpus* or *Assets* link. If the content is not in the repository you are
  about to cite, **you are citing the wrong address.**
- **Step 0d — probe *that* address**, with the full 14-path licence probe, not the code repository's.
- **Step 0e — no licence file is not "unlicensed".** When the probe returns nothing, **read the
  README for a prose grant**. Record it as *grant stated in README prose, no licence file* — which
  is materially different from both *MIT* and *unlicensed*, and is the only honest cell.
- **Step 0f — check whether the grant is per-record.** If the project says attribution or licensing
  is recorded inside the data, that is a **delivery obligation with a build cost**: the deliverable
  has to carry attribution per item through generation, packaging and display. **Put it in the
  estimate.** No SPDX field, SBOM or scanner can represent it.

🔵 **Why this is a gate and not a note.** Three of this base's most valuable content rows —
`OATutor-Content`, `bncc-dados`, `learning-commons-org/knowledge-graph` — each fail a different
step above, and in every case the *code* repository's licence cell was correct and useless. See
`intel/trends.md` **T63**.

---

## 928-G1 — Byte-read control gate: measure the file, never the variable — added `p928`

🔴 **This gate exists because `p928` ran a control on `p927`'s 37 byte-read grants and the control
reported `32 of 36 DIVERGE`. The control was wrong. `p927` was right — all 37 reproduce exactly,
byte count and `sha256₁₂`** (`evidence/p927-byteread-control.2026-11-19-p928.tsv`).

**The defect.** The control captured the body and the status code in one `curl -w '\n%{http_code}'`
call, held the result in a shell variable, and stripped the status line with `sed '$d'`:

```sh
out=$(curl -sS -w '\n%{http_code}' "$url")     # <-- $( ) strips ALL trailing newlines
body=$(printf '%s' "$out" | sed '$d')          # <-- removes the body's last line with it
```

Every real `LICENSE` file ends in a newline. Command substitution eats it, so **every byte count
came back one low and therefore every `sha256` changed.** The corrupted run is kept at
`evidence/p928-cmdsubst-falsedivergence.2026-11-19-p928.tsv` so the signature stays readable.

🔵 **The tell, and it is the part worth memorising.** The deltas were `1073→1072`, `1129→1128`,
`1079→1078`, `1067→1066`, `1085→1084` — **uniform, across thirty unrelated repositories.** Thirty
independently maintained MIT files do not all lose exactly one byte overnight. 🔴 **A divergence set
whose deltas are all identical is an instrument fault, not a supply change**, and that test costs
nothing to apply.

**The gate.**

- **Step 1 — write the body to a file.** `curl -o "$f" -w '%{http_code}'`. Measure `wc -c < "$f"`
  and `sha256sum "$f"`. The bytes must never pass through a shell variable.
- **Step 2 — before publishing any divergence, histogram the deltas.** If one delta value covers
  most of the set, stop and audit the harness. Publish the divergence only once the deltas are
  heterogeneous.
- **Step 3 — a `200` with a changed digest is a claim about *someone else's repository*.** Hold it
  to the same two-channel standard this base applies to absence (`926-F`): confirm on the search
  channel that the repo was actually pushed since the prior read before calling it a change.

🟢 **Runnable:** `compose/code/p928-byteread-control/byteread.sh` is the corrected single-URL
reader; `test_byteread.sh` is its acceptance test — 3 controls, no network, and control 2 asserts
the defect still reproduces, so the test fails loudly if it ever stops protecting anything.

🔵 **Why this is the symmetric twin of `926-F`.** `p926` found a channel that fails toward **false
absence** — a batched query drops a row without saying so. This is a channel that fails toward
**false divergence** — a harness reports change where there is none. Both are silent, both are
produced by the measuring apparatus rather than the world, and **both would have been published as
findings about repositories.** See `intel/trends.md` `T69`.

---

## P54 — Generate the courseware, ship it as SCORM, and never touch the client's LMS — added `p927`

**The problem.** Every content pattern in this file ends at the same wall: the generated
courseware has to get **into** the client's learning platform. The routes this base has documented
— an LTI 1.3 tool, an MCP bridge, a Moodle plugin — all require the client's platform team to
install, register and maintain something, which is a procurement conversation before it is an
engineering one. For a corporate L&D buyer or an EMEA public-sector estate, it is usually the
reason the pilot does not start.

**The insight.** **SCORM 1.2 packages are ingested by every LMS in the market** — Moodle, Canvas,
Open edX, Brightspace, SuccessFactors, Cornerstone — with **no plugin, no tool registration, no
platform fork and no AGPL exposure.** It is the one delivery form that is indifferent to what the
client runs, and this base had no row for it until `p927`.

**The build.**

1. **Author.** Generate the lesson with a content agent this base already holds —
   `xingjunm/autoppt` (**MIT**, interactive lecture slides, `926-F4`) or
   `532025497/video2lesson` for video-sourced material. Output a **Markdown storyboard**.
2. **Compile.** `parthdhanani/storycraft` (**MIT**, `sha256₁₂ 51b37fff352e`) turns the Markdown
   storyboard into a **SCORM 1.2 package**.
3. **Validate and run.** `parthdhanani/scorm-kit` (**MIT**, identical grant) packages, **validates**
   and provides the SCORM runtime. Validate **before** handing anything to the client — a package
   the LMS rejects is the whole value of this pattern lost.
4. **Interactivity.** Where the lesson needs interactions rather than slides, author them as H5P
   and play them with `missing-elements/h5p-toolkit` (**MIT**) — which plays `.h5p` **with no H5P
   server**, so the interactive tier does not re-introduce the platform dependency step 1 removed.
5. **Credential the completion.** On pass criteria, issue with
   `parler-haut-interagir-librement/certificates-bundle` (**MIT**, PDF + QR verification) and
   `…/open-badges-bundle` (**MIT**), or `wonmortech/sanad` (**Apache-2.0**) where the client wants
   **W3C Verifiable Credentials 2.0**. See `intel/trends.md` **T65**.
6. **Measure.** SCORM 1.2 reports completion and score and little else. If the engagement promises
   anything about learning, add `CAHLR/pyBKT` (**MIT**) over the item responses and read
   `10kH/MisconceptDialogue` **before** agreeing the success criteria — see **P7** and `927-F8`.

**Licence posture.** 🟢 **Permissive end to end.** Every component is MIT or Apache-2.0, byte-read.
The client's LMS is never forked, never patched and never a dependency, so its AGPL or GPL status
is irrelevant to the deliverable — which is the structural reason this pattern survives a licence
review that `P11` and `P26` have to argue their way through.

**Estimate.** **5–7 weeks** for a first package pipeline with one subject and one LMS validated;
**+2 weeks** per additional interaction type. 🟡 `storycraft` and `scorm-kit` are 1–2 ★ and months
old — **read them end to end and expect to maintain them**; they are small enough that this is a
realistic plan and the plan should be stated to the client, not discovered later.

**When not to use it.** SCORM is a **one-way** package format. If the engagement needs the tutor to
read the gradebook, adapt across sessions or act on live learner state, SCORM cannot carry it —
use `P11` (MCP into the LMS) or `P26` (sanctioned LMS-to-agent bridge) instead. **P54 is for
delivery of content, not for an agent that lives inside the course.**

---

## P55 — Exam integrity that is compliant by architecture rather than by contract — added `p927`

**The problem.** A client asks for proctoring. This base's standing answer has been *"do not
propose it"*: under the EU AI Act, **inferring emotions in an education institution is a prohibited
practice, in force since 2 February 2025**, exam proctoring is **separately Annex III high-risk**
from 2 December 2027, Canadian higher education has broadly refused the tooling on privacy grounds
(`p891`), and the open tier was six repositories whose largest was 16 ★ and dormant. That answer is
correct and it loses the engagement.

**The insight (`T64`).** The prohibition is on **emotion inference**, not on video; the privacy
objection is to **student data leaving the institution**, not to monitoring as such. Both can be
answered in the **design** rather than in the DPIA. `topic:proctoring` — 176 repositories, never
asked until `p927` — contains worked examples of exactly that.

**The build.**

1. **Start from the floor, not the ceiling.** `tanzir71/tinyproctorjs` (**MIT**, 1,085 B byte-read)
   is an integratable JS agent plus session dashboard doing **browser-integrity monitoring only** —
   focus loss, tab switching, session state. 🟢 **It infers no affect at all**, so the prohibition
   is not engaged by its design rather than by its configuration. For a large share of real
   academic-integrity requirements, **this is the entire product** and nothing further is needed.
2. **Add vision only if the client can state why integrity signals are insufficient**, and add it
   **local-first**: `SHUBHJAIN139/Local-Exam-Proctoring-Engine` (**MIT**) runs WebAssembly MediaPipe
   and TF.js **in the candidate's own browser**, so **no video leaves the device**. Transmit
   **events and scores, never frames**. 🔴 Read `Aryansh909/Examshield-AI` (**MIT**, YOLOv8 +
   MediaPipe 468-point) as the capability ceiling and **do not ship 468-point landmark tracking
   without a written answer to what is computed from it** — that is the input affect inference is
   built from.
3. **Reduce what proctoring has to carry.** Randomised item generation makes copying worth less:
   `PrairieLearn` (🔴 **AGPL-3.0 community edition, with a proprietary Enterprise tier including
   `apps/course-agent/` — see `repos/foundations.md` `p899`**) or, permissively,
   `openpatch/bitflow` (**MIT**) for branching assessment flows and
   `mrlvsb/kelvin` (**MIT**, VŠB–TU Ostrava's production examinator) for code assessment.
4. **Detect at the artefact, not at the face.** `alberto2005-coder/detector-ia` (**MIT**) scores
   AI-generated text **and copying between submissions** across Jupyter, PDF, DOCX, MD and TXT.
   🔵 Cross-submission comparison is what an integrity office actually asks for, and it needs no
   camera at all.
5. **Make the human the decision-maker, auditably.** Every flag goes to review, never to an
   outcome. `Appsmith` (Apache-2.0) for the review queue; log the model version, the inputs, the
   reviewer and the decision. 🔴 **Oklahoma SB 1734 bars AI used solely for grading, discipline or
   promotion** — an automated integrity finding that reaches a student record without a human is
   the exact prohibited shape.
6. **Record the telemetry posture.** `CarlosEkRaigoza/privacy-preserving-educational-telemetry`
   (**MIT**) is a published reference design for this layer, and **California AB 1159** bars
   training models on student data outright — so the retention and training policy is a **design
   artefact**, not a contract clause.

**Licence posture.** 🟢 **Permissive end to end if `PrairieLearn` is replaced in step 3** with
`bitflow` and `kelvin`; 🔴 **`DELIVERABLE — COPYLEFT` if `PrairieLearn` stays.** Decide this at
architecture review, not at delivery.

**Estimate.** **6–8 weeks** for steps 1, 4 and 5 — integrity signals, artefact detection and
auditable human review — which is the version that is defensible in every region this base covers.
**+4–6 weeks** for local-first vision in step 2, and that increment is where the legal review
belongs.

🔴 **What this pattern does not do.** It does not change the **risk classification**: exam-access
and assessment proctoring is Annex III high-risk from 2 December 2027 whatever the architecture.
It reduces **prohibition and privacy exposure**, which is a different thing, and the client must be
told so plainly. 🟡 And the three proctoring rows are **0–1 ★ and months old** — they are
**reference designs to read**, not dependencies to pin. The studio's first offer should still be
**integrity by assessment design**; P55 exists so that the second offer is not a refusal.

## P56 — The mastery loop that updates *per answer*: permissive end to end, no retraining job — added `p928`

**The problem this solves.** Every adaptive-learning pitch in this base promises that the system
"adapts to the learner". In most delivered builds it does not: answers are logged, a batch job
retrains nightly or weekly, and the learner in front of you today gets yesterday's model. The
reason is almost never pedagogy — it is that the team reached for a batch ML stack, because that is
what is permissively available and familiar. `p928` shelved the piece that removes the excuse.

**The stack — four rows, four permissive grants, none copyleft.**

| Role | Repo | Grant |
|---|---|---|
| Per-interaction mastery estimation | https://github.com/online-ml/river | **BSD-3-Clause** |
| Asynchronous in-material retrieval practice | https://github.com/cognitive-engineering-lab/mdbook-quiz | **`MIT OR Apache-2.0`** — take it under **MIT** |
| Live, in-room formative checks | https://github.com/david-04/quiz-mate | **ISC** |
| Pedagogically coherent source chunking | https://github.com/cmlonder/notebooklm-chunker | **MIT** |
| Reference BKT implementation + scaffolded hints | https://github.com/CAHLR/OATutor | **MIT** (🔴 content is a separate repo — `927-G1`) |

### Wiring

1. **Chunk the client's material on headings, not tokens.** `notebooklm-chunker` over the source
   PDFs. A chunk boundary that splits a worked example in half produces a retrieval that reads as
   incoherent to a student, and no prompt fixes it downstream.
2. **Attach an item to each chunk.** `mdbook-quiz` questions are `.toml` files referenced from the
   book, so authoring and assessment stay in one artefact and one review cycle. Its `Tracing`
   question type (predict the program's output) is worth using as-is for anything code-adjacent.
   Use `OATutor`'s scaffolded-hint shape for item design — question, then hint, then sub-step —
   rather than inventing one.
   🔴 **Budget for response capture: `mdbook-quiz` documents no results backend.** It renders and
   grades in the page; getting the answer event to step 3 is a small piece of work you must plan,
   not a feature you inherit. This is the one integration cost in this pattern and it is the one
   teams discover late.
3. **Model mastery incrementally with `river`.** One `learn_one(x, y)` call per submitted answer.
   Start with a logistic model over `(skill, learner, item-difficulty)` as the permissive stand-in
   for BKT; add `river`'s **drift detectors** on the per-skill error stream — a drift alarm on a
   cohort is the signal that the *material* changed difficulty, not that the learner regressed.
   🔵 **This is the step that makes the loop real: the estimate that selects the next item was
   updated by the answer the student just gave.**
4. **Use `quiz-mate` for the synchronous half.** Same item bank, exported; the host drives
   questions in a live session and the responses feed the same `river` models. One mastery state,
   two delivery surfaces.
5. **Expose the state, do not hide it.** Mastery per skill, the evidence behind it, and the date it
   last moved — rendered for the learner and exportable for the institution. That export is what
   `P48` sells into a regulated market and what `P53` attaches to a tutor the client already owns.

### What to tell the client, and what it costs

- 🟢 **Licence position is clean**: BSD-3-Clause + MIT + ISC + MIT. Take `mdbook-quiz` **under its
  MIT half** and the whole path stays GPL-2.0-compatible and free of patent clauses (`T70`).
- 🟡 **`river` models the *estimate*, not the pedagogy.** It will tell you mastery moved; it will
  not tell you which item to show next. That policy is yours to write and is the deliverable the
  client is actually buying — budget design time for it, not just engineering.
- 🔴 **Do not promise a learning-outcome gain.** This base's standing caveat holds: there is no
  credible primary evidence of outcome gains from AI tutoring at scale. Sell the *loop and its
  evidence trail*, and open with `10kH/MisconceptDialogue` — the criteria decide the measured
  result, so agree the criteria with the client before measuring anything (`P7`).
- **Shape:** 5–7 weeks for a single-subject pilot with a real item bank; the item bank, not the
  code, is the long pole, and `P51`'s generation line is how you shorten it.

### 🔴 What this pattern does *not* cover

Identity, enrolment and gradebook write-back. Those are LMS concerns — take them from `P53` and the
Canvas/Moodle seams in `verticals/solutions.md`. Nothing above touches the client's LMS, which is
deliberate: it is what lets the pilot start without a procurement cycle (`T30`).

## P57 — Assessment that survives a free, MIT-licensed, cross-platform solver — added `p929`

**The situation.** `T72` measured six permissively licensed assessment-attack tools, all byte-read,
all MIT: a solver covering **Canvas, Moodle, Blackboard and Google Forms** in one extension, a
Moodle auto-solver with human-like interaction timing, two Kahoot auto-answerers, and a
counter-detection tool that **names Turnitin and GPTZero in its own description**. 🔴 `928-F5`'s
reading — *an in-browser quiz cannot be the graded artefact* — is right and insufficient: switching
platform does not help, because one tool covers all four; and falling back to a detector does not
help, because one tool exists to defeat detectors.

**Who it is for.** Any institution whose integrity policy still has *detect the output* or *ban the
tool* as its control point — which, per `T10`, is most of them.

**What to compose.** The control point moves from the artefact to the **process** and its
**evidence**.

| Move | Build it from | Licence |
|---|---|---|
| Make the trace the submission | `stegra05/Lectern` — https://github.com/stegra05/Lectern — **per-card provenance and a visible coverage map** | MIT, byte-read `1,072 B` |
| Generation the student must defend | `Lintao-Lab/faithful-lecture-notes` — https://github.com/Lintao-Lab/faithful-lecture-notes — Architect plans, Assemblers write from full source, **engineered against hallucination** | MIT, byte-read `1,066 B` |
| Gated oral / applied check | `cskwork/supertutor-skill` — https://github.com/cskwork/supertutor-skill — Feynman + Socratic behind a **deterministic gate**: no advance without a holding explanation | MIT, byte-read `1,064 B` |
| Own the live-quiz surface | `TheCodeHeist-Coder/Rexial` — https://github.com/TheCodeHeist-Coder/Rexial — self-hosted live quiz | MIT, byte-read `1,076 B` |
| Invigilation where genuinely required | `P55`'s three local-first, in-browser designs (`927-F4`) | MIT |
| Measure the measurement | `10kH/MisconceptDialogue` (`927-F8`) — evaluation criteria shape measured success | MIT |

**How to wire it.** The assessment artefact carries provenance by construction — Lectern's coverage
map is the model — so **the submission is the trace, not the answer**, and scoring weights the
defensible steps. A short Socratic check, gated, deterministic and recorded, stands in for the
invigilator on anything high-stakes. Where a live quiz carries grade weight, **self-host it** with
Rexial: an institution cannot change the mechanics of a product it does not run, and two of the six
tools in `T72` exist specifically to defeat the product most institutions do run.

🔵 **What to tell the client, in one sentence.** *The tool your policy is written against is free,
MIT-licensed, covers all four of your platforms, defeats your detector, and ships an update the week
after you block it — so the only control you own is what you ask students to produce.* 🟡 That is an
uncomfortable sentence and it is the honest one. `T10` is the trend, `T72` is the measurement behind
it, and `927-F8` is the licensed, citable argument for why a benchmark number alone will not settle
it.

**Shape.** 4–6 weeks for an assessment-redesign engagement on one faculty; the provenance pipeline
and the gated-check harness carry across faculties. 🔵 Sells naturally alongside `P55` (integrity by
architecture) and `P53` (attaching evidence to a tutor the client already has).
---

## P58 — Dependency intake gate: resolve the address, then the grant, before anything is costed

🔵 **The problem this solves.** Every other pattern in this file names repositories, and a studio
will clone them months after they were shelved. `p930` re-measured all **594** addresses this base
publishes and found **4 renamed**, **1 grant replaced outright**, **2 archived** and **53 (9.0%)
untouched for a year** — none of which announces itself. A rename never breaks a link (GitHub
redirects forever), so **a stale dependency fails silently**: the clone works, the README renders,
and the project has quietly changed hands. Run this gate at the **start** of an engagement, on
every repo the proposal names. It is about **twenty minutes** for a hundred repositories.

### The four checks, in order

**1 — Is the address still canonical?** The cheap, decisive test, because it proves identity by
commit SHA rather than inferring it from content:

```bash
# HEAD at the address you hold (git follows GitHub's rename redirect silently)
git ls-remote https://github.com/<owner>/<repo> HEAD
# does the search index know that address? 422 = no repository there NOW
curl -sG -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/search/repositories --data-urlencode "q=repo:<owner>/<repo>"
```

🔴 **A `422` with a live `ls-remote` means renamed, not unindexed.** Find the new address
(`<repo> in:name`), and confirm with **identical `HEAD` + `fork=False`** — a fork reports
`fork=True`, and two unrelated repositories do not share a commit SHA. 🔴 **Never batch `repo:`
qualifiers for this check**: `repo:a/b repo:c/d …` turns a loud per-row `422` into a **silent
omission** (`930-R1`). Batch to *survey*, re-query individually to *conclude*.
🟡 Redirects **chain**, so the address you were told to track forward may itself be stale — the
indexed one is the live one.

**2 — Read the grant from the bytes, and classify on the title line.**

```bash
curl -s https://raw.githubusercontent.com/<owner>/<repo>/HEAD/LICENSE | head -1
```

🔴 **Do not grep the body.** MPL-2.0 names the **AGPL** in its own Exhibit B and GPL-2.0 recommends
the **LGPL** in its closing paragraph, so a body-matching scanner reports `uloya1234/faq-assistant`
as AGPL-3.0 and `Automattic/sensei` as LGPL — **both wrong, and both in the direction that kills an
adoptable dependency at the review gate** (`T73`). The title line is unambiguous in every case.
🟡 `0BSD` and `ISC` share their permission sentence; only the title separates them.

**3 — Treat `NOASSERTION` as a *question*, not a verdict.** It means GitHub matched no single SPDX
id. If the payload byte-reads as a recognisable permissive licence, the usual cause is a
**concatenated multi-grant file** — `HyNuwa/UniMCP` ships MIT for its own code plus **ISC for
portions derived from `utn-mcp`** in one `LICENSE`. **The second grant governs the vendored
subtree**, which is the one a lawyer will ask about (`T40`, `930-F4`). Contrast `NONE`, which means
there is no grant and the row is refused.

**4 — Age the row against what it is.** `pushed_at` plus `archived` from the same search call.
🔵 **Apply different thresholds by layer, because they decay differently:** an *agent* untouched for
a year is abandoned; a *standards implementation* may be finished. `swl10/pyslet` (IMS/QTI, last
push 2020) and `Apereo-Learning-Analytics-Initiative/OpenLRS` (archived 2019) are still the right
**specifications to read** — and are **never** dependencies to take a floating version of.
**A foundations row older than 24 months is a spec you read and a library you vendor at a SHA.**

### Wiring it

The harness `p930` used is in **`compose/code/p930-shelf-depth/`** — `extract-rows.py` pulls
addresses out of markdown tables, `audit2.py` batches the search channel, `grant.py` byte-reads and
classifies licence payloads. Point it at the repo list in your proposal instead of at this base's
shelves. Full per-row output for the current shelf is in
`evidence/shelf-depth-audit.2026-11-19-p930.tsv`.

### 🔴 What this pattern does *not* do

**It does not replace reading the row.** `p930` ran three automated controls over a sound shelf and
every one manufactured divergences — a table parser produced **7 licence-drift candidates, 7 of 7
false**; a byte-read classifier produced **6, of which 5 were false**; `928-G1` produced **32, all
32 false**. 🟢 **One real finding survived all of it** (`nengdou-ai-review-helper-web`, Apache-2.0 →
MulanPSL-2.0, payload replaced). **Use the gate to produce a shortlist of rows to read by hand, and
never to publish a correction unread.**

## P59 — The institutional governance layer: the deliverable that *87% adoption and 26% strategy* actually implies — added `p937`

🔵 **Why this pattern exists.** Every other recipe in this file builds a *capability*. `p937`'s
regional legs say the binding constraint in 2026 is not capability (`T76`): UNESCO IESALC reports
**87% of LATAM higher-education institutions using AI and 26% with a formal strategy**; in Brazil
**22% of school administrators** report school AI guidelines; in North America **134 bills across 31
states** and a **dated** policy cascade (North Carolina model policy **2026-12-31**, district
policies **2027-06-30**); in EMEA the **EU AI Act Article 4 AI-literacy duty has bound institutions
since February 2025**. 🟢 **The client already has the tools and lacks the defensible wrapper around
them.** This pattern is that wrapper, and it is largely the *same build* in all four regions, which
is what makes it worth productising rather than bespoking.

🟢 **It is also the pattern most robust to the one thing this base cannot see.** `937-F7` records
that no primary legal text is reachable from this environment, and the EU's Annex III commencement
date is **in dispute (2026-08-02 vs 2027-12-02)**. Every component below is driven by a *requirement
that is not in dispute* — consent, an age gate, a human-decision record, an audit trail, literacy
evidence — so the build does not move when the date is settled.

### The stack, all verified on this shelf

| Layer | Repo | Grant | Why this one |
|---|---|---|---|
| **Identity + consent state** | `apereo/java-cas-client` | 🟡 **Apache-2.0 + JA-SIG BSD, conjunctive — two notice obligations** | Consent and opt-out are meaningless unless bound to the institution's real SSO identity, which in HE is usually CAS or SAML |
| **Policy enforcement point** | `BerriAI/litellm` | 🟡 **MIT — exclude `litellm/enterprise/`** | One gateway in front of every model. The **age gate** (NY A 9190's grade-9 floor) and **parental opt-out** (Alabama H.B. 1227) are enforced here **once**, not re-implemented per application |
| **Audit trail — default** | `traceloop/openllmetry` | 🟢 **Apache-2.0** | OpenTelemetry-native, so traces land in the observability stack the client **already runs**. Nothing new to operate, which is what makes it survive handover |
| **Audit trail — when a purpose-built trace UI is wanted** | `langfuse/langfuse` | 🔴 **MIT core — exclude `ee/`, `web/src/ee/`, `worker/src/ee/`, `packages/shared/src/server/ee/`.** Copyright now reads **ClickHouse, Inc.** | Richer LLM-specific UI; needs licence diligence before it enters a deliverable, and the permissive grant covers less than the repository |
| **Regression gate** | `promptfoo/promptfoo` | 🟢 **MIT** | The numeric before/after. A governance claim with no baseline is a policy document, not a control |
| **LMS seam — ship the tool in** | **LTI 1.3** into Moodle (**GPL-3.0**) / Open edX (**AGPL-3.0**) | 🟢 tool stays a **separate work** | Integrate, never fork: the whole copyleft problem disappears at the LTI boundary |
| **LMS seam — expose the LMS to the agent** | `G36maid/moodle-mcp` | 🟢 **MIT** | Read-**write** Moodle MCP. Use **both** seams — LTI ships your tool into the LMS, MCP exposes the LMS to your agent |
| **AI-literacy evidence (EU Art. 4)** | **Open Badges 3.0** | 🔴 **implement from the published 1EdTech specification** | Art. 4 requires an institution to *show* staff and student AI literacy. A verifiable credential is the natural artefact. 🔴 **`1EdTech/openbadges-specification` carries no grant at all — re-confirmed by byte-read `p937`. Read the standard; do not vendor the repo's files.** |

### Wiring

1. **CAS/SAML in front, LiteLLM behind it.** Every model call carries a resolved institutional
   identity. Consent, opt-out and age are attributes on that identity, evaluated at the gateway.
2. **Deny by default at the gateway for consequential actions.** Grading and discipline outputs are
   marked `requires_human_decision`. The gateway will emit them only with a reviewer id attached —
   which is what makes Alabama's *"not the primary basis for grading or discipline"* an
   architectural property instead of a policy promise.
3. **OpenLLMetry spans on every call**, exported to the client's existing collector. The span is
   the audit record: prompt, model, consent state, reviewer id, outcome.
4. **promptfoo in CI** against a fixed item set. Publish the delta per release; this is the
   *"proven instructional benefit"* evidence the 2026 channel keeps asking for.
5. **Ship the learner-facing tool over LTI 1.3**; pull roster, assignment and gradebook context over
   `moodle-mcp` where the client runs Moodle.
6. **Issue an Open Badge** on completion of the institution's AI-literacy path. Art. 4 discharged,
   with evidence.

### Licence posture of the result

🟢 **A closed, branded derivative is clean**, provided three exclusions hold: drop
`litellm/enterprise/`, drop every `ee/` path if Langfuse is used, and keep the LMS integration at
the **LTI/MCP boundary rather than forking Moodle or Open edX**. 🟡 Carry **two** attribution
notices for `java-cas-client`, not one. 🔴 **If `opendatalab/MinerU` is anywhere in the content
pipeline, its §2 applies to this deliverable**: an online service built on MinerU must *"clearly and
prominently"* disclose that MinerU is used, and §3 terminates the grant automatically on breach
(corrected `p937`). That disclosure requirement is incompatible with a silent white-label, so decide
it at design time, not at launch.

### Build estimate

**6–9 weeks** for the gateway, consent model, audit trail and CI gate against one LMS, assuming the
client's SSO exists and is reachable — it usually does, and that assumption is the main schedule
risk. **Add 2–3 weeks** per additional LMS seam, and **2 weeks** for the Open Badges issuance path.
🔵 **The compliance-remediation variant is shorter and more urgent**: in **Vietnam** (Law on AI in
force **2026-03-01**, education named high-risk, transition **already expired 2026-06-30**) and
**South Korea** (AI Basic Act in force **2026-01-22**) this is retrofitted onto a *running*
deployment, which is mostly steps 1–3 and lands in **4–6 weeks**.

## P497 — Vietnam education-AI conformity pack: classify first, and bill the negative answer (`p939`)

**When to reach for this.** A client sells or operates education software in **Vietnam** — or sells
into it from elsewhere in APAC — and has heard that "education is high-risk" under
`Law 134/2025/QH15` and `Decree 142/2026/ND-CP`. 🔵 **This is the only education-AI pattern in this
base that ends in a filing rather than a recommendation**, because Vietnam is the only jurisdiction
here with an enumerated high-risk list *and* a live portal (`intel/trends.md` **`T78`**).

**Why the classification step comes first, and why it is the profitable one.** The high-risk list
enumerates **46 systems across 6 categories, of which education is 3** — student assessment and
admissions. 🟢 **Most of an edtech portfolio is therefore out of scope**: tutoring, content
generation, scheduling, analytics and administrative automation are not listed. The engagement that
proves a product is *not* one of the three named systems is cheap, fast, and worth as much to the
client as a positive finding — and it is only defensible because the list is **enumerated rather
than categorical**, so a negative answer can be argued from the text instead of from judgement.

### Stage 1 — Classify (days, not weeks)

| Step | What you do | Repo / artefact |
|---|---|---|
| Inventory every AI feature in the portfolio | One row per feature: input, output, who the decision binds | Spreadsheet; no tooling needed |
| Map each row against the **3 enumerated education systems** | Assessment? Admissions? Neither? | `Decision 33/2026/QD-TTg` list |
| Separate **medium-risk** from out-of-scope | Medium- **and** high-risk must be notified to the Ministry of Science and Technology | Decree 142 notification duty |
| Produce a signed classification memo | The deliverable: per-feature in/out, with the textual basis for each | — |

🔴 **Stop here and get the client's counsel to sign the memo before building anything.** The
transition deadline for already-operating systems is **unresolved across sources** — `2027-09-01`,
`2027-03-01`, and a `2026-06-30` self-assessment date — so the *timing* is a client-side legal
determination. Scope your work against the **duties**, which every source agrees on.

### Stage 2 — Build the evidence the duties actually require

For each feature that *is* one of the three systems, Decree 142 requires pre-market **conformity
assessment**, **registration in the National AI Database**, ongoing **incident reporting**,
**transparency documentation** and **human oversight**. Wire it from parts this base already holds
with permissive grants:

| Duty | Concrete wiring | Licence |
|---|---|---|
| **Human oversight** on an assessment decision | Put a human-review gate in front of any grade or admission outcome. `CAHLR/OATutor` (**284 ★**, `MIT`, pushed 2026-11-21) is the reference implementation of transparent **BKT** mastery estimation — its per-skill state *is* the explanation a reviewer needs, unlike an opaque score | 🟢 `MIT` |
| **Transparency documentation** | Generate a model/system card per feature: inputs, training provenance, known failure modes, the oversight gate. Keep it in-repo and version it with the model | — |
| **Conformity evidence** on assessment quality | Hold out a scored set and publish measured accuracy per subgroup *before* filing, so the conformity claim is numeric. 🔵 Start here, exactly as the LATAM `piloto→producción` recipe does: **get a baseline number first** | — |
| **Incident reporting** | A logged, queryable decision trail per assessment/admission outcome, with a defined severity threshold and a named filing owner | — |
| **Registration** | File on the live portal — **`ai.dda.gov.vn`**, operated by the Ministry of Science and Technology, in operation since **2026-08-28** | — |

### Stage 3 — Keep the AI layer outside the LMS process

🔴 **Do not modify the LMS in-tree.** There is still no permissive LMS at anchor scale
(`repos/trending.md` **`939-R2`**): Open edX is `AGPL-3.0` (`openedx/openedx-platform`, **8,250 ★**),
Moodle and Chamilo are `GPL`, OpenEduCat is `LGPL-3.0`. 🟢 **Integrate across a service boundary** —
LTI / REST out of the LMS into your own assessment service — so the copyleft obligation stays with
the platform and your conformity artefacts stay in a repository you control and can hand to a
regulator. 🔵 That boundary is required by the licence tier and *also* happens to be what makes the
evidence trail auditable, which is the rare case where the legal constraint and the compliance
requirement push the same way.

🔴 **Two things not to put in the proposal.** The transition **date** (unresolved, above) and any
claim built on a byte-read of the statute: **neither `ai.dda.gov.vn` nor the Official Gazette text
resolves from this environment** (`939-F5`), so every element above is snippet-sourced from
commercial compliance guides and the duties should be confirmed against the primary text by the
client's counsel before a fixed price is quoted.

## P498 — Reproducible licence inventory: ship the command, not the digest (added `p940`)

**When to use it.** Any engagement that hands a client a licence inventory, an SBOM, an
open-source attribution file or a compliance pack — so `P24`'s rebuildable handover, and the
pre-flight gate `G1` that every other pattern here depends on. **Use it specifically when the
deliverable will be audited by someone who does not trust you**, which is the normal case in
procurement.

**The failure it prevents, measured in this base rather than imagined.** `p940` found **14
published licence fixtures** whose `sha256` could not be reproduced from the grant file as served
(`T80`). The cause was one line of shell: the payload was interpolated through command
substitution, `$(cat LICENSE)`, which strips **all** trailing newlines, so every digest was
computed over a payload one or two bytes shorter than the file anyone else would fetch. No licence
verdict was wrong. Every digest was useless. 🔴 **An auditor who re-runs your hash and gets a
different answer does not conclude "trailing newline"; they conclude the inventory was not
produced the way you said it was** — and then they re-audit the verdicts too.

### The pieces

| Role | Use | Licence (byte-read `p940`) | ★ | Why this one |
|---|---|---|---|---|
| Grant corpus | [`spdx/license-list-data`](https://github.com/spdx/license-list-data) | 🔴 **no grant file at any conventional path**; SPDX API reports `null` | 720 | Canonical licence texts to diff against — **but see the caveat below; this row is the pattern's own `T23` specimen** |
| SPDX tooling | [`spdx/tools-python`](https://github.com/spdx/tools-python) | `Apache-2.0` (11,356 B, `c5accbbd8546`) | 261 | Emits and validates the SBOM document the client keeps |
| Scanner, second channel | [`nexB/scancode-toolkit`](https://github.com/nexB/scancode-toolkit) | `Apache-2.0` (11,357 B, `c71d239df917`) at the **non-standard path `master/apache-2.0.LICENSE`** | 🔴 unmeasured — `422` | Independent licence detection; `T24` showed grants change **by directory**, which a root-only read misses |
| Dependency graph | [`anchore/syft`](https://github.com/anchore/syft) | `Apache-2.0` (11,357 B, `c71d239df917`) | 9,956 | Transitive inventory; `T28` records that the top of this shelf is unpinnable |
| Reproduction gate | `compose/code/p940-fixture-vs-payload/` | this KB | — | The two arms below, including the one that must **abstain** |

🔴 **Two caveats found while verifying this very table, and both belong in the pattern rather than
in a footnote.** 🔵 **First: the canonical grant corpus has no grant.** `spdx/license-list-data`
serves `404` on `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` and `NOTICE` on both `main` and
`master`, and the API reports `null` — so the repository everyone reaches for to *resolve* licence
questions is itself a `T23` specimen with no readable grant. Its own README states it is
**generated** output whose source is [`spdx/license-list-XML`](https://github.com/spdx/license-list-XML);
treat it as a convenience mirror, take canonical texts from `spdx.org/licenses/`, and **do not
represent it to a client as a licensed dependency.** 🔵 **Second: `nexB/scancode-toolkit` returns
`422 "resources do not exist"` from `search/repositories` on two consecutive calls**, while
`git ls-remote` resolves it and `raw.githubusercontent.com` serves its Apache grant — `p901`'s
false-absence class, recurring here on a fresh slug. **Keep both channels in the gate**: a scanner
that concludes a dependency does not exist because one API said so will silently drop rows from a
client's inventory.

### The build

1. **Fetch and hash the bytes as served — never a shell-interpolated copy.** Write the payload to
   a file and hash the file. The defect `T80` names is created entirely by passing the grant
   through a string.

   ```bash
   # correct: the file is the artefact
   curl -fsS "https://raw.githubusercontent.com/$SLUG/$REF/LICENSE" -o grant.bin
   BYTES=$(wc -c < grant.bin); SHA=$(sha256sum grant.bin | cut -d' ' -f1)

   # WRONG, and this is the p940 defect verbatim:
   #   printf '%s' "$(cat grant.bin)" | sha256sum     <- strips every trailing newline
   ```

2. **Record the reproduction command beside every digest, not just the digest.** Each inventory row
   carries `slug`, `ref` (a **commit SHA**, not a branch — `P24`'s pinning rule), `path`, `bytes`,
   `sha256`, and the literal command. The client's auditor runs the command; agreement is the
   deliverable.
3. **Gate it, and make the gate independent.** A second job re-fetches every row and fails the
   build on any mismatch. 🔴 **The gate must not be able to read the inventory's prose** — `p940`'s
   `licence-ledger-structured` recorded a wrong pair under `method = byte-read` while its own last
   column held the markdown cell it had scraped, so it agreed with the page by construction and
   reported green through three verification passes.
4. **Make the gate abstain rather than guess.** `p940`'s first sweep arm reported **1,502**
   conflicts, its second **728**, its third **322** — and all three were artefacts: cross-pairing
   several slugs and hashes on one line, and reading HTTP status codes (`200`) out of a TSV column
   as byte counts. Only the arm restricted to one-slug-one-hash rows with a **live re-fetch**
   produced data. A row the gate cannot adjudicate is reported `ABSTAIN`; it is never reported
   clean.
5. **Flag the rows that cannot discriminate.** A grant file ending without a trailing newline
   produces the same digest stripped or not — **4 of `p940`'s 37 rows** were in this state. They are
   not evidence that the instrument was correct, and they are labelled indeterminate.
6. **Re-read bespoke grants on a schedule; canonical ones need it once.** `MIT` and `Apache-2.0`
   texts are fixed by their stewards. A bespoke grant — `CaviraOSS/PageLM`'s "PageLM Community
   License", `chadyi/StudyOnTV`'s "Source Available License — Personal Use Only" — is whatever its
   author last committed, and `T25`/`T27` show the traps concentrate exactly there. Give those rows
   a re-confirm interval and an owner.

### What the client gets

A licence inventory in which **every row can be independently re-derived by a third party**, a gate
that fails the build when one cannot be, and an explicit list of rows the method cannot adjudicate.
🟢 **The commercial argument in one sentence:** an inventory whose digests reproduce converts a
licence review from an assertion about your diligence into a measurement the client's own auditor
can repeat — and that is the difference between a compliance pack that closes a procurement and one
that reopens it.

🔴 **What not to claim.** Do not present reproduction as a licence *opinion*. This pattern proves
that the bytes you read are the bytes upstream serves; it says nothing about whether the grant
permits the client's use. That judgement is `G1`'s, it is a lawyer's, and `T19`'s both-ways
metadata errors are the reason the two must stay separate deliverables.

## P499 — The licence fixture gate that actually holds: resolve the branch, then compare against the repo's own bytes — added `p941`

🔵 **What this replaces.** `P498` (`p940`) ships a reproducible licence *inventory*. This pattern is the **gate** that keeps the inventory honest over time, and it exists because `p940`'s pre-registered version of it would have failed in two specific ways that `p941` measured. Both failure modes are cheap to avoid and expensive to discover in front of a client.

### The two traps, stated before the recipe

🔴 **Trap 1 — do not compare against a canonical licence hash.** Canonical Apache-2.0 circulates in at least four byte-forms among repositories this base cites: `11,358 / cfc7749b96f6`, `11,357 / c71d239df917`, `11,356 / c5accbbd8546` (**ends `.` — no trailing newline**) and `11,362 / a89039268428`. `spdx/tools-python`'s grant is one byte shorter than the common form **and is correct**. A gate that flags `−1 B` against a constant reports it as tampered.

🔴 **Trap 2 — do not key on "a 12-hex token near a slug."** This corpus uses 12-hex prefixes for **both** a grant's `sha256₁₂` **and** a repository's git `HEAD` commit, and nothing in the shape distinguishes them. `digitalcredentials/learner-credential-wallet`'s `1c46a82ba384` is a commit, recorded as such in nine evidence files; a naive gate reports an unreproducible licence.

🟢 **The rule both traps reduce to: a published fixture is adjudicated against *that repository's own served bytes*, and against nothing else.**

### The recipe

```bash
#!/usr/bin/env bash
# p941 fixture gate. Input: slug + published (bytes, sha256_12). Output: one verdict.
set -uo pipefail
slug="$1"; pub_bytes="$2"; pub_sha="$3"

# 1. Resolve the DEFAULT BRANCH first. `master` is the plurality (50 of 61 measured),
#    and `trunk`, `develop`, `dev`, `v2` and version branches like `15.0` are all real.
br=$(git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null \
     | sed -n 's|^ref: refs/heads/\([^[:space:]]*\).*|\1|p')
[ -z "$br" ] && { echo "$slug REPO-UNRESOLVABLE"; exit 0; }

# 2. Ladder filenames AND out-of-root paths. Case matters: openSIS-Classic's own grant
#    is docs/License.txt, not docs/LICENSE. unidic-lite has TWO grants (LICENSE, LICENSE.unidic).
for f in LICENSE LICENSE.md LICENSE.txt LICENCE COPYING COPYING.LESSER NOTICE \
         LICENSE-MIT LICENSE-APACHE apache-2.0.LICENSE LICENSE.unidic \
         docs/License.txt docs/LICENSE docs/LICENSE.txt; do
  body=$(curl -fsS --max-time 25 "https://raw.githubusercontent.com/$slug/$br/$f") || continue

  # 3. Hash the payload AS SERVED. Never via $(...) — command substitution strips
  #    EVERY trailing newline and is the exact defect that produced 40 bad fixtures.
  srv_b=$(printf '%s' "$body" | wc -c)          # informational only
  read -r srv_sha _ < <(curl -fsS "https://raw.githubusercontent.com/$slug/$br/$f" \
                        | tee /tmp/g.$$ | sha256sum)
  srv_b=$(wc -c < /tmp/g.$$); srv_sha=${srv_sha:0:12}
  strip_sha=$(printf '%s' "$(cat /tmp/g.$$)" | sha256sum | cut -c1-12)
  rm -f /tmp/g.$$

  if [ "$srv_sha" = "$pub_sha" ] && [ "$srv_b" = "$pub_bytes" ]; then
    echo "$slug AS-SERVED-OK $br/$f"; exit 0
  elif [ "$strip_sha" = "$pub_sha" ]; then
    echo "$slug STRIPPED-LF $br/$f published=$pub_bytes/$pub_sha served=$srv_b/$srv_sha"; exit 1
  fi
done
echo "$slug NO-GRANT-MATCHED branch=$br"; exit 1
```

🔵 **Line 3 is the whole pattern.** `$(cat f)` and `$(curl …)` both strip every trailing newline, so a fixture computed through command substitution can never match the file a client fetches. Pipe the bytes; do not interpolate them.

### Dependencies, with grants verified this pass

| Component | Address | Grant | Role |
|---|---|---|---|
| `git` | — | GPL-2.0 | `ls-remote --symref` is the only reliable default-branch resolver here |
| `curl`, `sha256sum` (coreutils) | — | MIT / GPL-3.0 | fetch + digest |
| `anchore/syft` | https://github.com/anchore/syft | 🟢 **Apache-2.0**, 11,357 B `c71d239df917` | SBOM generation for the wider inventory (`P498`) |
| `nexB/scancode-toolkit` | https://github.com/nexB/scancode-toolkit | 🟢 **Apache-2.0**, 11,357 B `c71d239df917`, at `master/apache-2.0.LICENSE` | per-file licence detection; note the **non-root grant path** |
| `spdx/license-list-data` | https://github.com/spdx/license-list-data | 🔴 **no readable grant at any conventional path** (`p940`) | take canonical texts from `spdx.org/licenses/`, and **do not** represent this mirror to a client as a licensed dependency |

### Where to run it, and what it is worth

🟢 **Run it as a pre-commit gate on any shelf that publishes licence fixtures**, and on the dependency manifest of a client deliverable. 🔵 **Report format matters as much as the check:** emit `AS-SERVED-OK` / `STRIPPED-LF` / `NO-GRANT-MATCHED` / `REPO-UNRESOLVABLE` per row and **exempt append-only narrative files from failing the build while still reporting on them** — `p940` predicted correctly that a gate without that exemption never goes green.

🔴 **The client-facing argument for charging for this.** Of 275 published fixtures on this shelf, **248 reproduced, 26 did not, and 1 was the gate's own false positive** — a 9.5% defect rate in a corpus maintained by an instrument that was *trying* to be rigorous, with **zero** licence verdicts actually wrong. That is the honest sales line: the gate does not find mislicensed dependencies, it finds **unverifiable claims about correctly licensed ones** — and an inventory a client cannot re-derive is an inventory that will not survive their legal review.

## P500 — A ministry-grade admissions-and-entitlement agent built entirely on permissive code, with the copyleft platform kept behind LTI — added `p942`

🔵 **Why this pattern exists.** Every other platform recipe in this file has to manage a copyleft obligation, because every LMS/SIS anchor this base holds is `GPL`, `AGPL`, `LGPL` or `ECL` — `P497` exists precisely to keep the AI layer out of the platform process for that reason. **This recipe has no copyleft obligation at all on the pieces it builds *from*.** `p942` byte-read a permissive education estate that is not in the platform tier at all but in government service repositories (`T84`, `repos/foundations.md`, `intel/market.md` EMEA). It is the one recipe here a studio can relicense end to end.

🔴 **Read the honest constraint first, because it determines who this is for.** The reusable systems are **9–37 ★** repositories. They are reference implementations, not communities: nobody should present them to a client as an ecosystem, and there is no upstream to receive contributions back at scale. **They are also not an LMS** — they are workflow services. The engagement this fits is a *ministry, awarding body, regional education authority or large multi-academy trust* that needs an admissions, entitlement or establishment-data capability, where the argument is "the production reference implementation exists, is MIT, and we can start from it" rather than "this is a thriving open-source project".

### Pieces, with the licence each one actually grants (all byte-read in `p942` unless noted)

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| **Admissions workflow reference** | https://github.com/DFE-Digital/apply-for-teacher-training | 🟢 **MIT** (Crown Copyright) · `main/LICENCE`, 1,094 B `1018ba112e86` | England's *national* teacher-training admissions service — multi-provider applications, references, offers, conditions. **37 ★**, pushed `2026-11-23` |
| **Establishment reference data / entity resolution** | https://github.com/DFE-Digital/get-information-about-schools | 🟢 **MIT** (Crown Copyright) · `main/LICENCE`, 1,116 B `e18299fd1942` | The national schools and colleges register (GIAS). **This is the piece an education agent cannot do without**: a canonical establishment identifier to resolve "which school" before any reasoning happens |
| **Eligibility / entitlement rules** | https://github.com/DFE-Digital/accessing-childcare-entitlement-checker | 🟢 **MIT** · `main/LICENCE`, 1,102 B `97952c3f6069` | A worked eligibility-checking service — the rules-plus-evidence shape every entitlement question takes |
| | https://github.com/DFE-Digital/teacher-training-entitlement | 🟢 **MIT** · `main/LICENCE`, 1,091 B `af7b3fcaafcb` | Entitlement calculation |
| **Curriculum content substrate** | https://github.com/oaknational/oak-open-curriculum-ecosystem | 🟢 **MIT** · `main/LICENCE`, 1,086 B `02c5a8e84229` | Oak National Academy — the English national curriculum body's own ecosystem. **9 ★**, pushed `2026-11-23` |
| **Agent orchestration** | https://github.com/microsoft/autogen | 🟢 **MIT** | Multi-agent conversation where a caseworker-style flow needs several specialised roles; MIT keeps the permissive posture intact |
| | https://github.com/huggingface/smolagents | 🟢 **Apache-2.0** | Preferred when the flow is *one* agent calling tools, which most entitlement checks are. Smaller surface than AutoGen |
| **Explainable learner state** (only if the scope reaches tutoring) | https://github.com/CAHLR/OATutor | 🟢 **MIT** | Per-skill BKT state **is** the reviewer's explanation — the reason `P497` chose it for human-oversight evidence |
| **The platform, if one is in scope at all** | Moodle (`GPL-3.0`, `COPYING.txt`) / Open edX (`AGPL-3.0`) | 🔴 copyleft | **Stays behind an LTI 1.3 / REST boundary, in its own process.** `P497` Stage 3 |

### Wiring

1. **Resolve the establishment first.** Stand up GIAS as a read-only reference service and give the agent a single `resolve_establishment(name|URN|postcode) → URN` tool over it. 🔵 **Do not let the model guess institution identity**; every downstream rule keys on the URN, and an agent that infers "which school" from a free-text name will be wrong in exactly the cases that matter (multi-academy trusts, renamed and merged establishments).
2. **Lift the rules, not the UI.** Take the entitlement/eligibility *rule expression* from the two checker services and expose each rule as a deterministic tool the agent calls. 🔴 **The rules must not be reimplemented as prompt text** — an entitlement decision has to be reproducible and auditable, and a tool call is both where a generation is neither.
3. **Put the agent on top as orchestration only.** `smolagents` for a single tool-calling agent, `autogen` where distinct roles genuinely help (applicant-facing, caseworker-facing, reviewer). The model's job is intake, clarification, routing and explanation — **never the decision**.
4. **Keep the decision boundary explicit.** Every determination returns the rule that fired plus the evidence, so a human reviewer approves a *decision with a reason*, not a verdict. This is the human-oversight artefact a regulator asks for, and it falls out of step 2 rather than needing to be built.
5. **Integrate the LMS, if present, across LTI 1.3** — the agent and its rules stay in the permissive estate; Moodle or Open edX keeps its copyleft inside its own process. `P497` Stage 3 covers the boundary.

### Licence posture of the result

🟢 **MIT in, your choice out.** Every component above is MIT or Apache-2.0, so the deliverable may be relicensed, including commercially — **the only recipe in this file for which that is true.** 🔴 **The one obligation is attribution, and it is per repository, not per estate:** the five DfE repositories carry **three** different copyright-notice forms and two different licence titles (`repos/foundations.md`), so a single "contains DfE code" line does not satisfy MIT. Carry each notice verbatim, attributed to its repository of origin. 🔵 Ten minutes when scoped at the start; an audit finding when discovered at the end.

🟡 **Estimate.** Steps 1–2 on a defined entitlement scope: **4–6 weeks**. Adding step 3–4 orchestration and the reviewer artefact: **+3–4 weeks**. 🔴 **The estimate assumes the client's own establishment and rule data, which is the part that is never clean** — budget discovery separately and do not quote steps 1–2 against an unseen data estate.

🔵 **Verification note.** Every grant in the table was read in full in `p942`, not inferred from byte count. The first draft of the underlying shelf section published four of them on length and digest alone and they were read before commit — publishing a measured row as a read one is the error class this base has spent several passes correcting.
