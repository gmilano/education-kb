---
industry: education
region: Global
updated: 2026-10-31
---

# Measured / Unusable — the ungranted-domestic-supply register

**Opened at `p544` · 2026-10-30, closing [`Gap 543-D`](../agents/trending.md#-gap-543-a--gap-543-f-registered).**

🔵 **Why this file exists.** An artefact can be **real, live, education-specific
and still unusable**, because it carries **no grant at all**. Such an artefact is
neither a shelf row (nothing licenses us to build on it) nor a reject (it is not
mis-described, mis-licensed or off-sector — it is *correctly* described and
*genuinely* absent a licence). `Gap 543-D` was registered because the class had
no published home: three Vietnamese agents had been found, filed only in a
trending entry, and were on course to be **re-discovered a fourth time**.

🔴 **The rule this register encodes:** *supply is not the same as usable supply.*
A region can have domestic AI-in-education engineering and offer Globant nothing
to build on. Counting artefacts without reading grants overstates every regional
supply claim on this base.


## `p572` (2026-10-31) — six additions, three of them high-star repositories that read as open source

| address | ★ | what the grant actually says | verdict |
| --- | --: | --- | --- |
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | 2,100 | **"PageLM Community License"**, 8,563 B, bespoke and non-OSI. Grant is for *"personal, educational, or non-commercial research purposes"* only. **"Redistribution of the Software, in whole or in part, in source or binary form, is strictly prohibited"** without written permission. Commercial use requires a **revenue-sharing agreement executed in advance**; absent one, use is *"material breach and immediate termination"*. The licence is **revocable**. | ⛔ **HARD BLOCK.** Cannot be shipped, redistributed, hosted commercially, or bundled. 🔴 Seen **59×** in this base's history with its licence never recorded. |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | 5,600 | **CC BY-NC 4.0** (19,347 B). Covers the asset that *is* the product: 1,644 knowledge points, 2,403 prerequisite edges, 6,723 curriculum-aligned items. | ⛔ **BLOCK for commercial delivery.** NonCommercial. 🔵 Usable as a *reference schema* for a graph built from scratch; the edges themselves cannot ship. Seen **36×**, never shelved. |
| [`chewyenhan/malaysia-uec-teacher-workflow`](https://github.com/chewyenhan/malaysia-uec-teacher-workflow) | 2 | `LICENSE.md`, **2,876 B**, is a **path table**, and the first line says "MIT". `SKILL.md`, `README.md`, `agents/`, `references/`, `evals/`, `examples/` → **CC BY-NC-SA 4.0**. Only `scripts/`, `tests/` → MIT. Explicitly grants no rights to textbooks, school templates or student data, and reserves separate commercial licensing. | ⛔ **BLOCK on the substance**, MIT on the glue. 🔴 **Fifth distinct split-grant mechanism in this KB — a path table — and it defeated the scope-clause regex while the byte count caught it.** |
| [`githubharald/DeslantImg`](https://github.com/githubharald/DeslantImg) | 156 | `LICENSE.md` is a clean **MIT**, 1,071 B. `requirements.txt` pins **`Py-BOBYQA>=1.3`**, verified first-hand as **GPL-3.0** (35,147 B, title "GNU GENERAL PUBLIC LICENSE", Version 3). Imported in-process. | ⚠️ **LINK-ONLY / avoid in distributed work.** Distributing a combined work triggers GPL-3.0. No §13, so hosting alone is not the trigger. 🟢 Substitute: `WordDetector` + `CTCDecoder`, same author, permissive throughout. |
| [`deepseek-harness-java/teacher-workbench`](https://github.com/deepseek-harness-java/teacher-workbench) | 2 | **No grant at 40 probes** — 4 branches (`main`, `master`, `develop`, `trunk`) × 10 filenames including case variants, all 404. | ⛔ **UNGRANTED** → exclusive copyright. Read the feature taxonomy; ship nothing. |
| [`0x454447415244/HandwritingRecognitionSystem`](https://github.com/0x454447415244/HandwritingRecognitionSystem) | 465 | **No grant at 40 probes.** A 465★ CNN-RNN handwriting system with no licence file on any probed branch. | ⛔ **UNGRANTED** → exclusive copyright. The most-starred ungranted row in this KB. |

### 🟡 Held back from the shelf on provenance, not licence

- [`abmarkguo/medical-exam-teacher-toolkit`](https://github.com/abmarkguo/medical-exam-teacher-toolkit) —
  **MIT**, 1,098 B (body read: the `+28 B` over standard is only a longer copyright
  line, no carve-out). 🔴 **`41` commits, every one dated `2026-07-27`, and the
  repository's first commit is `Add CITATION.cff`.** Not `570-A`-grade synthetic —
  the dates are not internally contradictory — but a repository does not begin with
  its citation file, and 41 same-day commits is an import, not a history.
  **Licence clean, provenance unestablished.**

### 🔵 A convention worth recording

- [`MyScript/MyScriptJS`](https://github.com/MyScript/MyScriptJS) — 355★, **ARCHIVED**,
  `LICENSE` is **570 B**. 🔵 **The Apache-2.0 licence text is 11,358 B; a ~570 B
  "Apache" file is the boilerplate *header notice*, not a grant.** Treat an
  Apache claim under ~1 kB as an assertion to verify, not a licence to rely on.
  (Compare this pass's genuine Apache grants: 11,340 / 11,343 / 11,357 / 11,358 B.)

## The register

| Address | Origin (region) | What it is | Grant, probed at the resolved default ref | Head read at (pass · ref · sha) |
|---|---|---|---|---|
| 🆕 [`ceanjonnube-negra/docente-ia`](https://github.com/ceanjonnube-negra/docente-ia) | 🟢 **LATAM (Mexico)** — *stated*, but **not in the README**: `ESTADO_PROYECTO.md` describes a *"Herramienta de consulta oficial **SEP**"* restricted to **`.gob.mx`** domains (calendar, `planes y programas`, `acuerdos SEP/DOF`) and `PROJECT_MAP.md` carries the schema flag `es_sep` | **245 commits** — the most substantial artefact `p547` found, and architecturally the most interesting: **two tool mechanisms held deliberately apart**, *"el Tool Registry determinista … **nunca pasa por Claude**"* beside Claude's native function-calling. 🔴 **Its `README.md` is 1 450 B of untouched `create-next-app` boilerplate** — the concrete instance of `Gap 544-B`'s README-only limit doing damage (`Gap 547-D`) | 🔴 **`UNRESOLVED`** — nothing licence-shaped in the tree at `HEAD` and **no grant declared** in `README`, `package.json` or any `*.md` | `main` · `p547`, last commit `2026-10-28` |
| 🆕 [`jrsaguas/DocenteAgent`](https://github.com/jrsaguas/DocenteAgent) | 🔴 **UNPLACED** — no country evidence read first-hand. Commit timezone `-06:00` is a **hint, not evidence**, and `p545`'s rule forbids placing an `es` artefact on its language | Teacher-administration agent (syllabus, planning, attendance, exams, grades) with a stated human gate — *"Acciones externas sensibles requieren autorización humana **inicialmente**"*. 🔴 **Read `inicialmente`:** the gate is declared provisional, and `biometría después` is on the roadmap, with `docs/ATTENDANCE_BIOMETRICS_ROADMAP.md` and `docs/MOODLE_AUTH_SECURITY.md` in tree. 🔵 Biometric attendance in schools is the one function that would move an engagement from Annex III high-risk into the AI Act's **prohibited** tier if it drifted into emotion inference | 🔴 **`UNRESOLVED`** — nothing licence-shaped in tree, none declared in `README` (1 231 B) | `master` · `p547`, last commit `2026-09-29` |
| 🆕 [`lehrer-tools/lehrer-agent`](https://github.com/lehrer-tools/lehrer-agent) | 🟢 **EMEA (Germany)** — *stated* in the tree itself: `rahmenlehrplan.md` for **all 16 Bundesländer** plus their school law and `Verwaltungsvorschriften` | 🔴 **A different class from the rows above, filed here so it is not re-discovered.** The best regional fit `p547` found — 16-Länder curricula, `Förderschwerpunkt` differentiation (ESE · Hören · Lernen) × five subjects, `.docx`/OMML output, 103 files — and **unusable twice over**: 🔴 *declared-but-unserved* (`"license": "MIT"` in `plugin.json` **and** `## Lizenz` in README, **no licence file at any path**, holder `{"name": "anonym"}` so MIT's notice clause cannot be satisfied even in principle — `Gap 547-A`); 🔴 *circumvention-blocked* (`bin/bibox` decrypts **AES-256-CTR**, `bin/cornelsen` **AES-128-CBC** — UrhG § 95a / InfoSoc Art. 6, `Gap 547-B`). 🟢 **`bin/klett` performs no decryption** and is the one reusable third | 🔴 **`DECLARED_UNSERVED`** — not `UNRESOLVED`: a bare `UNRESOLVED` would lose the fact that the author asserted MIT twice | `main` · `3ddcfbbabc56`, last commit `2026-04-06`. 🔴 Mirror: [`NikolasSchaeffner/lehrer-agent`](https://github.com/NikolasSchaeffner/lehrer-agent) is the **same tree at the same sha** |
| [`MaiQuangPhuoc/edu_agents`](https://github.com/MaiQuangPhuoc/edu_agents) | 🟢 **APAC (Vietnam)** — *stated*: grade-10 **GDPT 2018** national curriculum | Grade-10 curriculum agent. 🟢 **Architecturally the most interesting artefact four language legs returned:** it chooses a **deterministic pipeline over ReAct** for the education domain and **bounds the LLM to the textbook** to suppress invention. | 🔴 **`UNRESOLVED`** — 10 filenames at `main`, plus sidebar and README at `p543` | `main` · `03e43219c66a` |
| [`dungptt-dng/smart-ict-classroom`](https://github.com/dungptt-dng/smart-ict-classroom) | 🟢 **APAC (Vietnam)** — *stated*: **Vietnam AI in Education Pioneer Award 2026** entry | A computer lab with **fewer machines than groups**: fair turn scheduling and four rotating in-group roles. A constraint a LATAM or APAC public-school engagement meets constantly and no shelf row addresses. | 🔴 **`UNRESOLVED`** — as above | `main` · `a9c56b3b7496` |
| [`minhdevtry/AI-Teacher-Assistant-Agent`](https://github.com/minhdevtry/AI-Teacher-Assistant-Agent) | 🟢 **APAC (Vietnam)** — *stated*: Vietnamese, **Zalo** Bot | *ZaloAgent* — class management over Zalo, the domestic messenger, with fee capture by text **and image OCR**. | 🔴 **`UNRESOLVED`** — as above | `main` · `f3bcc636da1d` |
| 🆕 [`fairyofmiracle/edu_course_agent`](https://github.com/fairyofmiracle/edu_course_agent) | 🟡 **EMEA (Russia)** — *inferred, and the inference is named*: README and UI are **Russian**, the LLM gateways are **Cloud.ru** and **GigaSchool** (both Russian services), and the output is Russian **ДПО** professional-development paperwork. The page itself states no country. | A methodologist's workstation: builds a professional-development programme from an **ACR template**, and exports **DOCX / PPTX / JSON**. 🟢 **It refuses to invent the order number (`наказ`/приказ) and the labour-function code** — the artefact's whole value is that two legally-load-bearing identifiers are *not* generated. 196 commits, **0★, 0 forks**. | 🔴 **`UNRESOLVED`** — 10 filenames at `main`; sidebar shows no licence and does not say "no licence" | `main` · `c425a51c2512` |

🔴 **Four artefacts, two languages of origin, zero grants.** The Vietnamese trio
came off `p543`'s `vi` leg; the Russian row came off `p544`'s **`uk`** leg. The
class is now **stable across two unrelated origins**, which is what makes it a
class rather than a Vietnamese peculiarity.

## 🟢 What a studio may still do with a row here

🔵 Nothing in this register may be **vendored, forked or shipped** — there is no
licence to do so. What it is legitimately good for:

1. **Read the architecture, write your own.** `MaiQuangPhuoc/edu_agents`'s
   deterministic-pipeline-over-ReAct choice and textbook-bounded generation are
   *design* findings. A design is not a derivative work.
2. **Name the requirement.** `smart-ict-classroom`'s fewer-machines-than-groups
   scheduling is a **real constraint of public-school delivery** that no granted
   shelf row covers.
3. **Ask.** 🟢 The cheapest action available: open an issue requesting an
   explicit licence. `ACTION p417-A` already prescribes this for a LATAM address;
   the same move applies to all four here, and a single `LICENSE` commit would
   move a row onto the shelf.

🔴 **What must not happen:** a row here being quoted as regional "supply" in a
market slide. It is supply that cannot be used, and the register exists so the
distinction survives the next pass.
