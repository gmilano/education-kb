---
industry: education
region: Global
updated: 2026-11-16
---

## 🔴 `2026-11-16` — fifty-fourth pass (`p849`): **the TENTH consecutive nil on the vertical-platform leg, and this shelf's own row count was wrong by `2` the whole time**

🔴 **The mandated leg — `open source platform education ERP CRM MIT Apache` — was run again and
returned marketing pages for a single vendor.** 🟢 **`OpenEduCat`, already held here for many
passes: an education ERP built on the **Odoo** framework, covering admissions, SIS, academics,
attendance, finance, HR and a prospective-student CRM pipeline, with a free Community Edition and
paid enterprise modules.** 🔴 **Not one result in the leg stated a licence**, and this shelf's own
byte-read record stands: **`OpenEduCat` is `LGPL-3.0`, on an Odoo framework that is `LGPL-3.0`** —
🔵 **weak copyleft, so a studio's own modules can stay proprietary while modifications to the
platform itself must be published.** 🟡 **Usable, with that boundary drawn in the contract.**

🟢 **The closed set of seven is unchanged for a tenth pass** — Open edX (`AGPL-3.0`), Canvas LMS
(`AGPL-3.0` core), Moodle, ILIAS and Chamilo (`GPL-3.0`), Sakai (`ECL-2.0`), OpenEduCat
(`LGPL-3.0`). 🔴 **None is permissive and none has become permissive.** 🔵 **`p848` argued this leg
has stopped being a discovery instrument; `p849` agrees and acts on it — `P76` in
`compose/patterns.md` is built on the premise that the LMS is INHERITED over LTI 1.3 and never
replaced.** → `ACTION p849-E`: replace this leg's query with one that looks for what attaches to
the seven, not for an eighth.

### 🔴 The count defect, repaired

🟡 **`ingest/derive-counts.py` was reporting `RED heading claims 145, the file holds 147` on this
file, and no pass had touched it.** 🟢 **Heading corrected to `147`, derived from the gate, and
this shelf is GREEN for the first time in the window `p849` examined.** 🔵 **The same run found
`agents/top.md` stale by `3` and `repos/foundations.md` stale by `12`; the mechanism and the
five-pass history are in `agents/top.md` Finding 1.**

🟡 **Note for the next pass, not repaired here:** this file has **`12` tables carrying
`github.com` rows whose column signature is not declared to the gate**, so their rows are not in
the `147`. 🔵 **That is by design for censuses and comparison tables — but it has never been
audited row by row, and `p849` did not audit it.** → `ACTION p849-F`.

## 🟢 `2026-11-16` — fifty-third pass (`p848`): **the ninth consecutive nil on the LMS leg, and the SIS tier finally gets a permissively-licensed option**

🔴 **The mandated vertical leg was run again and returned the same seven platforms for the ninth
consecutive pass** — Open edX (`AGPL-3.0`), Sakai (`ECL-2.0`), Moodle (`GPL-3.0`), OpenEduCat
(`LGPL-3.0`), ILIAS (`GPL-3.0`), Chamilo (`GPL-3.0`), Canvas LMS (`AGPL-3.0` core, commercial
cloud). 🟢 **All held, all unchanged, none permissive.** 🔵 **This base should stop treating that
leg as a discovery instrument: nine passes is enough evidence that the open LMS market is a closed
set of seven, and the useful question is what sits BESIDE them.**

### 🟢 The SIS tier, re-stated with grants — and the hole in it is now partly filled

🔵 **The Student Information System is the system of record a school will not let a studio
replace**, which is why the licence on it decides whether an engagement can ship a derivative at
all. 🔴 **For fifty-two passes every option on this shelf was either copyleft or ungranted:**

| Platform | ★ | Grant | What that means for a studio |
|---|---|---|---|
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `654` | `GPL-2.0` | 🔴 Mature and actively pushed (`2026-11-13`), but a derivative **inherits `GPL-2.0`** and cannot ship inside a closed product |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | `351` | 🔴 **No grant reported** | 🔴 Self-describes as "commercial grade"; the open repository carries no licence this base can verify. **Treat as proprietary until a grant is byte-read** |
| [`hassanhabib/OtripleS`](https://github.com/hassanhabib/OtripleS) | `342` | 🔴 **No grant reported** | 🔴 Also unpushed since `2024-07-18`. **Stale and ungranted** |
| 🟢 [`jobic10/student-management-using-django`](https://github.com/jobic10/student-management-using-django) | `394` | 🟢 **MIT — byte-read** (`1,075 B`, `sha256₁₂ 92be33e226c0`) | 🟢 **NEW this pass.** Permissive. A derivative can ship closed |

🟢 **What the new row actually gives you.** Role-separated administration out of the box — admin,
staff and student surfaces — with attendance capture, result entry, leave request and approval,
course/subject/session modelling, feedback routing, and per-role summary dashboards, on Django with
an AdminLTE front end.

🔴 **What it does NOT give you, stated plainly so no engagement is scoped on a misreading.** Its
own `README` calls it *"a Simple Student Management System Developed While Learning Django"*. There
is **no multi-tenancy**, **no SIS interchange format** (no OneRoster, no Ed-Fi, no SIF), no
timetabling engine, no fees or finance module, and no identity integration. 🟡 **`1` open issue on
`394★` indicates a quiet repository, not a well-maintained one.**

🔵 **So file it correctly: it is a licence-clean SCAFFOLD, not a product.** 🟢 **The honest
engagement shape is "we build the client's SIS, starting from a permissive skeleton that already
models the five entities every school has" — which is a materially better starting position than
either re-implementing role-based school administration from zero or inheriting `GPL-2.0`.**
🔵 **`202` forks against `394★` (`1:1.95`, the highest ratio on this shelf) is independent evidence
that this is how other people are already using it.**

### 🟡 Still unfilled on this shelf

- 🔴 **No permissively-licensed LMS.** Nine passes, seven platforms, zero permissive. The
  compose patterns continue to pair a copyleft LMS with permissive AI services across a process
  boundary rather than embedding in it — see `compose/patterns.md`.
- 🔴 **No open SIS with an interchange format.** OneRoster / Ed-Fi support is absent from every
  open option above, which makes rostering integration bespoke work in every engagement.
- 🔴 **No education-specific MCP server** above `100★` (`0` results this pass).
## 🟢 `2026-11-16` — fifty-second pass (`p847`): **the vertical nil ENDS — not with another LMS, but with the tier beneath every LMS pattern on this shelf: where the learner's code runs**

🔵 **The mandated vertical leg was run globally and returned the same seven platforms as `p846`
(Open edX, Sakai, Moodle, OpenEduCat, ILIAS, Chamilo, Canvas LMS), all already held, all copyleft
except Sakai's `ECL-2.0`.** 🟢 **The eighth consecutive nil on that leg is therefore confirmed —
and `p847` stopped re-running it and asked a different question: what does a studio deploy when
the deliverable is a COURSE rather than an institution?**

### 🟢 The CLASSROOM-COMPUTE tier — customisable, permissive, and absent from this shelf for `51` passes

| Platform | Repo | Licence | ★ | Region | Scale it is built for | Where the AI layer goes |
|---|---|---|---|---|---|---|
| **The Littlest JupyterHub** | [`jupyterhub/the-littlest-jupyterhub`](https://github.com/jupyterhub/the-littlest-jupyterhub) | 🟢 **BSD-3-Clause — byte-read** (`1,510 B`, `a9d15a91664e`) | `1,147` | Global | 🟢 **`1`–`100` users on ONE server — a class, not a campus** | Above it: the agent reads submitted notebooks, runs them, and writes feedback. The GRADE comes from execution (`P84`), the model writes only the explanation. |
| **Plasma** | [`plasmabio/plasma`](https://github.com/plasmabio/plasma) | 🟢 **BSD-3-Clause — byte-read** (`1,527 B`, `2bb2635332c1`) | `42` | EMEA | A course, with its environment as a versioned artifact | 🔵 **EU-origin component for a European public bid.** The agent proposes environment changes as pull requests against the course definition. |

🔵 **Why this tier matters commercially.** 🔴 **Every LMS on this shelf is copyleft, so the
institution's platform choice is made before Globant arrives and the licence boundary has to be
engineered around (`P100`, `P101`).** 🟢 **The compute tier is permissive, and it is the part the
studio actually builds. A faculty-level engagement can therefore be delivered end-to-end on a
licence the client owns outright, with the LMS reached only through LTI (`P87`) — no copyleft
boundary crossed at all.**

### 🟢 The DOMAIN-TRAINING tier — finished, permissive platforms to put an agent beside

| Platform | Repo | Licence | ★ | Region | Why it is a vertical starting point |
|---|---|---|---|---|---|
| **CrypTool 2** | [`CrypToolProject/CrypTool-2`](https://github.com/CrypToolProject/CrypTool-2) | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `c71d239df917`) | `169` | EMEA | A complete visual-workflow cryptography and cryptanalysis lab with decades of German academic provenance. 🟢 **The subject matter, the exercises and the pedagogy already work** — a security-training engagement adds adaptivity and assessment, and invents none of it. |
| **wrench** | [`ryukzak/wrench`](https://github.com/ryukzak/wrench) | 🟢 **BSD-3-Clause — byte-read** (`1,466 B`, `8a9b41684109`) | `45` | EMEA | CPU simulator + assembler + **auto-grading toolkit**. 🟢 **The deterministic-grading reference**: the student's program either runs correctly on the simulated machine or it does not. 🔵 Pairs with `wixette/8800-simulator` (`Apache-2.0`) for the browser-side lab. |
| **Server Survival** | [`pshenok/server-survival`](https://github.com/pshenok/server-survival) | 🟢 **MIT — byte-read** (`1,079 B`, `e86ab27fe716`) | `6,498` | Global | A tower-defence game that teaches cloud architecture. 🟢 **`6,498★` for a corporate-training subject nobody clicks a course on — the strongest evidence on this shelf that the learning-by-play delivery model ships.** Reusable as the engagement-model demo in an upskilling pitch. |

### 🔴 A vertical that looks adoptable and is NOT — recorded here because it will be proposed again

| Estate | What it looks like | 🔴 What it is |
|---|---|---|
| `4GeeksAcademy` auto-graded exercise estate + the `learnpack` runtime | `9` canonical repositories, `~1,300★`, `634` forks on one, `4` pushed within `60` days, interactive auto-graded courseware in Python / JavaScript / HTML / CSS — i.e. precisely the vertical this base's declared grading gap has been waiting for | 🔴 **Not open source.** Content `LICENSE.md` is a `954 B` Breathe Code **terms-of-service** document (`# TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION`); GitHub reports `Other`. The npm runtime declares `"license": "https://learnpack.co/terms"` — a URL where an SPDX identifier belongs. `learnpack/learnpack-cli`, the repo npm names, **`404`s on both branches and is absent from the search index**. The visible `learnpack/*` repositories (`10★`, `2★`, `1★`) carry **no licence at all**. 🟡 The terms page was unreachable from this environment (`403` at the proxy) and is therefore not characterised here. |

🔵 **The transferable rule, because this will recur in every vertical:** when an education estate's
traction sits on CONTENT, the reusability question lives in the RUNTIME — different repository,
often different owner, sometimes not open at all. 🔴 **Resolve the runtime's grant to bytes before
costing anything.** → `T159`, `P990`, `P94`.

---

## 🔴 `2026-11-16` — fifty-first pass (`p846`): **the vertical leg nilled an eighth time, and the pass instead CORRECTED two platform licences this shelf has been quoting wrong**

🟢 **The mandated vertical-platform leg was run globally and returned seven named platforms. All
seven are already on this shelf, checked against the file:**

| Platform returned by the leg | Licence as the leg reported it | Held here |
|---|---|---|
| Open edX | `AGPL-3.0` | 🟢 Yes |
| Sakai | `Apache-2.0` | 🟢 Yes — 🔴 **and the licence is WRONG, see below** |
| Moodle | `GPL-3.0` | 🟢 Yes |
| OpenEduCat | `LGPL-3.0` | 🟢 Yes |
| ILIAS | `GPL-3.0` | 🟢 Yes |
| Chamilo | `GPL-3.0` | 🟢 Yes |
| Canvas LMS | `AGPL-3.0` | 🟢 Yes |

🔴 **The leg also reproduced, for an eighth consecutive pass, the standing structural fact: there
is NO MIT-, Apache- or BSD-licensed integrated education ERP/SIS.** 🟢 **Sakai is the only
permissive LMS of real scale returned, and this pass establishes that it is not Apache-2.0
either.** 🔵 **An informed nil on new platforms; the yield went to the licence field.**

### 🔴 Correction 1 — Sakai is `ECL-2.0`, not `Apache-2.0`, and a client scanner will not treat them as the same

| | This shelf said | 🟢 GitHub reports `2026-11-16` |
|---|---|---|
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `Apache-2.0` | 🟡 **`ECL-2.0`** · `1,238★` |

🔵 **`ECL-2.0` is the Educational Community License: Apache-2.0 with a narrowed patent grant
scoped to the contributor's own institutional contribution rather than the whole work.** 🟢 **It
is OSI-approved and permissive, so nothing on this shelf becomes unusable.** 🔴 **What changes is
the bid**: an SPDX scanner matching `Apache-2.0` will flag `ECL-2.0` as an unrecognised licence,
and a client whose policy enumerates permitted licences by name will have to add it.
🟢 **Quote `ECL-2.0` explicitly wherever Sakai is proposed, and say why it exists — it is a
university-sector licence and that is a selling point in a higher-education bid, not a defect.**

### 🟡 Correction 2 — `chimple/bahama` is `MPL-2.0`, not `Apache-2.0` — permissive → weak copyleft

🔴 **The difference is operational, not theoretical. MPL-2.0 is FILE-LEVEL copyleft: a modified
source file must be published, while the larger proprietary work around it need not be.**
🟢 **Still shippable inside a client product — but the modified files go back out, and a team that
believed it held Apache-2.0 will not have planned for that.** 🔵 Chimple's early-literacy tree is
exactly the kind of asset a LATAM or African foundation-phase engagement forks heavily.
🔴 **Sibling note from the same sweep: [`chimple/jamaica`](https://github.com/chimple/jamaica) is
`Apache-2.0` and ARCHIVED since `2019-05-20`.**

### 🟢 Correction 3 — `AsTeRICS Grid` is ALIVE, and this shelf's own caveat predicted the mechanism

🔵 **The row already carried an unusual admission:** 🔴 *"Star count deliberately left as `not
retrieved` rather than guessed: the free-text search channel does not return this repository at
all, although its `LICENSE` byte-reads `200`."*

🟢 **`p846` confirms the row was right and names the mechanism.** `repo:asterics/AsTeRICS-Grid`
returns `422`; the owner `asterics` enumerates fully at `51` of `51` repositories and the name is
absent; and `raw.githubusercontent.com` serves `LICENSE` (`34,523 B`) and `README.md`
(`10,862 B`) on `master`. 🔴 **Under `p844`'s and `p845`'s rules this row would have been killed
this pass. Under `P100` it stands.**

🟢 **The row's name-integrity warning also survives intact and is now better evidenced:**
`astericsfree/AsTeRICS-Grid` serves the SAME `34,523 B` `AGPL-3.0` blob but a DIFFERENT `README`
(`10,494 B` against `10,862 B`), pushed `2026-09-25`. 🔵 **Same licence, divergent content — a
copy, not a redirect.** 🔴 **For an AAC deliverable, cite `asterics/` and treat `astericsfree/` as
an unverified mirror.** 🟢 The permissive way in is unchanged: `fjrodl/astericsgrid_ros`
(`Apache-2.0`).

### 🟢 Correction 4 — the LTI 1.3 PHP row gains its upstream and its maintained fork

🔵 **`packbackbooks/lti-1-3-php-library` is ALIVE** (search-invisible; `README.md` `3,397 B` on
`master`). 🟢 **Two addresses are added beside it rather than replacing it**, because for an LMS
integration the three play different roles:

| Address | Licence | Pushed | Role in a PHP LMS engagement |
|---|---|---|---|
| https://github.com/1EdTech/lti-1-3-php-library | 🟢 `Apache-2.0` (`944c6521f810`) | `2024-08-20` | 🟢 **Certification provenance.** The body that writes LTI 1.3 publishes it; `111` forks. |
| https://github.com/packbackbooks/lti-1-3-php-library | 🟢 `Apache-2.0` | 🟡 de-indexed | 🟢 **The PHP-FIG-compliant rewrite**, and the tree this shelf has always cited. 🔵 **Composer package is `packbackbooks/lti-1p3-tool` — the package name is NOT the repository name**, which matters when a dependency audit tries to map one to the other. |
| https://github.com/talis/lti-1-3-php-library | 🟢 `Apache-2.0` (byte-identical) | 🟢 **`2026-11-10`** | 🟢 **Current maintenance.** A UK higher-education software house, `1★`, pushed six days ago. |

🔴 **Why this matters for Moodle and Chamilo clients specifically:** both are PHP, both speak LTI
1.3, and the tool-provider side is where a Globant deliverable usually sits. 🟢 **Pin `talis`,
cite `1EdTech` in the compliance annex, and read `packbackbooks` for the implementation.**

## 🟡 `2026-11-16` — fiftieth pass (`p845`): **vertical-platform leg run and NILLED, with the denominator stated**

🟢 **The mandated vertical leg was run globally and returned four named platforms. All four are
already on this shelf, and the check was made against the file rather than from memory:**

| Platform returned by the leg | Licence as the leg reported it | Held here |
|---|---|---|
| OpenOLAT | `Apache-2.0` | 🟢 Yes |
| `frappe/lms` (Frappe Learning) | `MIT` | 🟢 Yes |
| RosarioSIS | 🔴 `GPL-2.0` — copyleft, demand signal only | 🟢 Yes |
| Moodle · Open edX · Canvas | `GPL-3.0` / `AGPL-3.0` | 🟢 Yes |

🔴 **One claim from the leg is explicitly NOT adopted:** a secondary source described Open edX as
*"AGPL v3 (platform), Apache 2.0 (some components)."* 🔴 **This base holds Open edX as `AGPL-3.0`
and nothing in the leg byte-read a component licence.** 🟡 **Recorded as an unverified
third-party claim, not promoted to the shelf.** 🔵 **A per-component licence split is exactly the
shape that `T134` warns about — it must be byte-read per component before a client deliverable
leans on it.**

🔴 **The permissively licensed SIS tier remains EMPTY, and that is an informed gap rather than a
silence.** 🟢 **The leg searched for MIT/Apache student-information systems specifically and
returned exactly one SIS — RosarioSIS, `GPL-2.0`.** 🔵 **So the standing shape holds: the LMS tier
has permissive options (OpenOLAT, `frappe/lms`), the SIS tier does not, and an engagement needing a
build-safe SIS still has to budget for one rather than adopt one.**

## 🟢 Forty-ninth pass (`p844`, 2026-11-16) — **`1` row: the LATAM national education data portal filed as a SYSTEM OF RECORD, because that is what it is in a ministry engagement**

🔵 **Why this belongs on the vertical shelf and not only in foundations.** This
base files LMS, SIS and ERP as systems of record. 🟢 **In a LATAM ministry
engagement the system of record that decides the work is neither of those — it is
the national statistical portal**, because enrolment, outcomes and equity
reporting are produced from it and every evidence claim in the bid is traced to it.

| System | Operator | Region | Access | Licence posture | Note |
|---|---|---|---|---|---|
| **National education data portals — LATAM** (INEP/`dados.gov.br` 🇧🇷 · `datos.gov.co`/ICFES 🇨🇴 · `datos.gob.mx` 🇲🇽 · `datos.gob.ar`/`data.educacion.gob.ar` 🇦🇷 · MINEDUC 🇨🇱) | State statistical and assessment bodies | **LATAM** | 🟢 Bulk download + catalogue APIs; 🟢 Brazil additionally via [`basedosdados/sdk`](https://github.com/basedosdados/sdk) (`MIT`, `433★`) | 🔴 **NOT uniform — four attribution-only, Colombia `CC BY-SA 4.0`** | 🔴 **No agent surface exists for any of them.** The buyer is a ministry, the route is public tender, and the integration target is a download, not an API with an auth story |

🔴 **The seam, stated plainly.** 🟢 Every other system-of-record family on this
shelf has acquired an agent surface in the last six passes — Moodle, Sakai,
Canvas, Schoology, Ed-Fi, the EMEA national school portals. 🔴 **This family has
none, in any of the five countries.** 🔵 **And unlike the PowerSchool case, the
blocker is not a licence** — four of the five publishers grant attribution-only
reuse. 🔵 **Unlike the OneRoster case, the data is not missing either.** 🟢 **It
is simply unbuilt**, and `P96` is the build.

## 🟢 Forty-eighth pass (`p843`, 2026-11-16) — **`0` new platform rows. The ERP/CRM leg is vendor-captured for the forty-eighth time, and this pass found the first ARCHIVED agent seam into the administrative core.**

🟢 **Leg run verbatim:** `open source platform education ERP CRM MIT Apache`.
🔴 **Result: unchanged and vendor-captured.** Ten of ten returned hits were
`openeducat.org` pages — glossary pages in `es`, `fr`, `ar`, `de`, `pt-BR`,
`zh`, `vi` and English, plus the school-management and institute-management
feature pages. 🔵 **A leg that returns one vendor's SEO surface in eight
languages is not measuring a market**, and that remains the finding.

🟢 **`OpenEduCat` stays shelved exactly as it is**: LGPL-3.0 (Community) /
commercial (Enterprise), built on the **Odoo** framework, which is itself
LGPL-based. The leg's own sources restate that licence, so the row is
corroborated, not revised. 🔴 **No MIT-, Apache- or BSD-licensed education
ERP/CRM platform surfaced, again.**

### 🔴 What is new: the MIT seam into ERPNext was ARCHIVED last month

The `P95` sweep measured every repository behind this file's recommended
architecture. One result changes a recommendation:

| Repo | Licence | Stars | Status 2026-11-16 |
|---|---|---|---|
| [`frappe/mcp`](https://github.com/frappe/mcp) | **MIT** | 171★ | 🔴 **ARCHIVED upstream**, last push 2026-10-27 |
| [`rakeshgangwar/erpnext-mcp-server`](https://github.com/rakeshgangwar/erpnext-mcp-server) | MIT | — | 🟡 live, but no push since 2026-04-25 |

🔵 **This matters more than its star count.** The architecture this base
recommends is: *copyleft administrative core, permissive agent-facing
integration tier on top*. `frappe/mcp` was the cleanest example of that tier
against an open ERP — Frappe's own MIT-licensed MCP server. 🔴 **Frappe has
stopped maintaining it.** The tier still holds; the exemplar needs replacing,
and a fork is the realistic answer because the licence permits it.

🟢 **The standing architecture, re-confirmed with first-party licence data:**
the administrative core is a copyleft estate — `OpenEduCat` LGPL-3.0,
`Odoo` LGPL, `Moodle` GPL-3.0, `Open edX` AGPL-3.0, `BigBlueButton` LGPL-3.0 —
while the layer Globant can ship without reciprocity is the **agent-facing
integration tier** (`vishalsachdev/canvas-mcp` and its fork family,
`loyaniu/moodle-mcp`, `jtayped/sakai-mcp`, `kingdonkatsu/ntulearn-mcp` —
the last one's MIT grant **byte-read for the first time this pass**,
`1,055 B`, `sha256₁₂ e6bd1450153a`) and the **content tier**
(`Kolibri` MIT, `H5P` MIT).

🟡 **One platform-level signal worth recording, from the EMEA regulatory leg:**
the UAE Ministry of Education's *Safe and Responsible Use of Artificial
Intelligence in Classrooms 2026* guide names an **approved-platform annex** and
bars unapproved generative-AI tools from classrooms outright. 🔵 **That turns
"which LLM does your tutor call?" into a procurement gate**, and it is an
argument for the self-hostable, provider-neutral end of this shelf —
`Kolibri`, `OpenMAIC` (MIT), `Ollama`-backed deployments — over anything that
can only reach a hosted frontier endpoint. Detail and provenance in
`intel/market.md`.

## 🔴 Forty-seventh pass (`p842`, 2026-11-16) — **`0` new platform rows; the ERP/CRM leg returned ONE platform and `13`-of-`17` hits were its own marketing domain**

🟢 **Leg run verbatim:** `open source platform education ERP CRM MIT Apache`.

🔴 **The leg is now measurably vendor-captured.** Of roughly `17` returned hits, **`13` were
`openeducat.org` pages** — glossary pages in eight languages (`es`, `fr`, `ar`, `de`, `pt-BR`, `zh`,
`vi`, plus English), feature pages, and the site's own `llms-full.txt`. 🔵 **A search leg whose
results are mostly one vendor's SEO surface is not measuring the market**, and that is the finding
to carry forward rather than any claim from those pages.

🟢 **`OpenEduCat` is already shelved below at `LGPL-3.0` (Community) / commercial (Enterprise), built
on the `Odoo` framework, and this pass changes nothing about that row.** The leg's own sources
restate the same licence, so the row is corroborated, not revised.

🔴 **The leg returned no MIT-, Apache- or BSD-licensed education ERP/CRM platform.** This is the
standing structural fact of this vertical and should be sold as such: 🔵 **the education
administrative core — SIS, enrolment, fees, HR — is a copyleft estate** (`OpenEduCat` LGPL-3.0,
`Odoo` LGPL-based, `Moodle` GPL-3.0, `Open edX` AGPL-3.0, `BigBlueButton` LGPL-3.0). The
permissively-licensed layer that Globant can ship without reciprocity obligations is the
**agent-facing integration tier** (`vishalsachdev/canvas-mcp` and its fork family,
`loyaniu/moodle-mcp`, `jtayped/sakai-mcp` — all MIT) and the **content tier** (`Kolibri` MIT,
`H5P` MIT). 🟢 **That split is the architecture this base keeps recommending, and `p842` re-confirms
it from a fresh leg.**

🔴 **Nothing from the vendor pages was promoted into a row.** `OpenEduCat`'s marketing claims about
module coverage and deployment options are unverified by this pass and stay out of the table
(`T124`-adjacent discipline: a vendor page is not a measurement).

## 🔴 Forty-sixth pass (`p841`, 2026-11-16) — **`0` new vertical rows (`172` → `172`); one licence-label conflict DECLARED and deliberately not applied**

🔴 **The mandated LMS/SIS leg returned only platforms already on this shelf** — `OpenOlat`,
`OpenEduCat`, `RosarioSIS`, `openSIS`, Moodle, Open edX, Canvas, Sakai. **`0` rows added.**

🟡 **Declared, not applied:** secondary sources on this leg disagree on **Sakai** —
`Apache-2.0` per one aggregator, **`ECL-2.0`** per another. 🟢 **`ECL-2.0` is the correct family**
(Apache-2.0 with the patent grant narrowed to educational institutions). 🔴 **The shelved row was
NOT edited, because this pass did not byte-read Sakai's `LICENSE`.** 🟡 Sources also omitted the
licence entirely for `RosarioSIS`, `openSIS` and `OpenEduCat` — 🔴 **the field an engagement turns
on is the field aggregators drop most often.** 🟢 **Action for the next pass: byte-read Sakai's
grant and either confirm or correct the label.**


## 🟢 Forty-fifth pass (`p840`, 2026-11-16) — **`5` rows (`167` → `172`): the OFFICIAL platform-vendor substrate, which this base had skipped while filing hundreds of third-party wrappers around it**

🟢 **Every grant byte-read `2026-11-16` at the real default ref.**

🔴 **The structural finding first, because it is a curation defect and not a discovery.** 🔵 This
base already files **hundreds** of third-party Moodle/Canvas connectors — the `*-moodle-mcp` and
`*-canvas-mcp` long tail runs to many dozens of distinct owners. 🔴 **It did NOT file the platform
vendors' own build substrate: `moodlehq/*` and `openedx/*` repositories that the connectors all sit
on top of.** 🟢 **One query each — `user:moodlehq`, `user:openedx` — surfaced them.** 🔵 The wrappers
were discoverable by keyword; the substrate was only discoverable by owner.

### 🟢 What moved onto the vertical shelf

| Platform / plugin | Repo | Grant, byte-read `2026-11-16` | ★ / forks | Ref · pushed | What it is, and the licence boundary it imposes |
|---|---|---|---|---|---|
| **STACK** (assessment for mathematics) | [`maths/moodle-qtype_stack`](https://github.com/maths/moodle-qtype_stack) | 🟡 **`GPL-3.0`** — `COPYING.txt` `35,146 B` `sha256₁₂:c53a65c2fd56` | `173★` / `183` | `master` · **`2026-11-15`** | 🟢 **The real thing for STEM assessment, and it is ALIVE** — `version.php` reads `release 4.14.0 for Moodle 4.2+`, `version 2026101500`. 🟢 From its own `doc/en/About`: *"an assessment system for mathematics, science and related disciplines"* where **students answer with a mathematical expression**, graded by CAS, plus free-text mathematical argument. 🟢 **Runs on Moodle AND ILIAS, and exposes an API to serve questions as a web service** — that API is the seam a non-GPL agent can call without linking. → `P92` |
| **GCompris** (early childhood) | [`gcompris/gcompris-qt`](https://github.com/gcompris/gcompris-qt) | 🟡 **`GPL-3.0-or-later`** — 🔴 **not at the repo root.** `COPYING` → `404`, `COPYING.md` → `404`; the grant is at `LICENSES/GPL-3.0-or-later.txt` → `200` (REUSE convention). 🔴 **GitHub label: `NONE`** | `266★` / `184` | `master` · **`2026-11-13`** | 🟢 **The early-childhood tier, which this base barely covers** — Qt Quick activity suite for young learners, actively pushed. 🔵 A mirror of `invent.kde.org/education/gcompris`, so **upstream is KDE and GitHub is downstream**: file issues upstream. 🔴 Copyleft: deploy and customise, never re-licence. |
| **Custom certificates** (credentialing) | [`mdjnelson/moodle-mod_customcert`](https://github.com/mdjnelson/moodle-mod_customcert) | 🟡 **`GPL-3.0`** — `LICENSE.md` `35,146 B` `sha256₁₂:c53a65c2fd56` 🟢 **(byte-identical GPL-3 text to STACK's — a useful cross-check that both reads are clean)** | `115★` / `205` | `main` · **`2026-11-14`** | 🟢 **Dynamically generated, fully customisable certificates.** 🟢 **Inverted fork ratio `1.8:1` — deployed far more than it is starred**, which is the signature of an operations plugin rather than a demo. The issuance end of a credentialing line. → `P92` |
| **Moodle plugin scaffolder** | [`moodlehq/moodle-tool_pluginskel`](https://github.com/moodlehq/moodle-tool_pluginskel) | 🟡 **`GPL`** — `LICENSE.md` `35,178 B` `sha256₁₂:ccb349b4132e`. 🔴 **GitHub label: `NOASSERTION`** | `60★` / `47` | `main` · `2026-05-27` | 🟢 **The VENDOR's own generator of Moodle plugin skeletons.** 🔵 Unglamorous and decisive: it is what makes an AI-plugin engagement start from a conformant tree instead of a hand-rolled one. → `P92` |
| **Moodle reference architecture** | [`aws-samples/aws-refarch-moodle`](https://github.com/aws-samples/aws-refarch-moodle) | 🟢 **`Apache-2.0`** — `LICENSE` `11,357 B` `sha256₁₂:58d1e17ffe51` | `150★` / `142` | `master` · 🔴 **`2025-05-07`** | 🟢 **The one Apache-2.0 artefact in this group** — Moodle at scale with CloudFormation templates, so the infrastructure layer is separable from Moodle's GPL. 🔴 **`18` months without a push: treat as a REFERENCE to read, not a template to apply unreviewed.** → `P92` |

### 🔵 The licence boundary this group forces a studio to state out loud

🔴 **Four of the five rows are copyleft, and that is not incidental — it is Moodle's platform
requirement propagating.** 🟢 **The usable split, stated once so an estimate can rely on it:**

- 🔴 **Inside the Moodle plugin tree → GPL, and the deliverable ships GPL.** Scaffolder, question
  type and certificate module are all in this zone.
- 🟢 **Outside it → free.** The `Apache-2.0` infrastructure layer and any external agent
  orchestration stay separable.
- 🟢 **The seam is STACK's web-service API** — an agent that calls assessment over HTTP has not
  linked to it. 🔵 **That one sentence is what makes a mixed-licence education engagement
  estimable.** → `P92`

## 🟢 Forty-fourth pass (`p839`, 2026-11-16) — **`3` rows (`164` → `167`): the PAPER-EXAM tier opens, and two school-management systems are filed with their fork ratios read rather than their stars**

🟢 **Every grant byte-read `2026-11-16` at the real default ref.**

| Platform | What institutions run it | Agent surface | Licence, re-read `2026-11-16` | Posture |
|---|---|---|---|---|
| **CorrectExam** — https://github.com/correctexam/corrigeExamFront + https://github.com/correctexam/corrigeExamBack | 🟢 **A deployable platform for administering and grading IN-CLASS PAPER assessments, long or short — the collection mode that still carries most of the world's summative marks and that this shelf had no entry for.** Angular 20 front, Quarkus/Java back, Rust server-side image processing (`deskewandcachecreator`), a LaTeX exam template, and install documentation published at `correctexam.readthedocs.io`. French academic lineage; created `2022-03-09`, both halves pushed `2026-11-15` (day of measurement). Enumerating the owner returned `15` repositories — the two starred ones plus the deployable estate around them. | 🟢 **The model's job here is bounded by design, which is why it survives a procurement review: automatic scan alignment, handwritten name recognition on the sheet, per-question zone identification, and reusable per-question comments carrying a bonus or malus. 🔵 The MARK stays with the marker and the pen; the machine does registration and recognition.** 🔵 **The whole pipeline runs IN THE BROWSER — OpenCV.js (WASM), TensorFlow.js and ONNX Runtime in Web Workers, Dexie/IndexedDB and SQLite-Wasm caches — so pupil handwriting never leaves the marker's machine to be aligned or recognised.** `P90`. | 🟢 **MIT** — front `main/LICENSE.md` and back `deploy/LICENSE.md`, both **`1,068 B`**, both `sha256:44ed794595f6…`, © *2022 correctexam*. One org, one grant, byte-identical payloads. | 🟢 **For an EMEA public-sector or university pitch this is the strongest data-residency story on this shelf: the privacy argument is architectural, not contractual.** 🔴 **Stated limits: `24★`/`13` forks on the front and `12★`/`10` on the back — argue from the four-year maintenance record and the mechanism, never the popularity. 🔴 The back repo's real default ref is `deploy`, NOT `main`, so an automated grant or dependency check pointed at `main` reads a `404` and records a false nil. 🔴 JHipster-generated lineage upgraded manually from `7.7.0`; Node ≥ `22.9`.** |
| **School Management System (node/express)** — https://github.com/iamtonmoy0/node-express-school-management-system | 🟡 **A ready-to-use school-management system — teacher, student and administrative management — JavaScript on Node/Express.** Created `2023-10-14`, pushed `2026-11-12`. | 🟡 **No agent surface ships with it, and that is why it is on THIS shelf rather than the agent shelf: it is a system of record to READ.** 🔵 Every analytics recipe on these shelves needs an administrative substrate, and this is a small, legible, permissively licensed one. | 🟢 **MIT** — `main/LICENSE`, **`1,083 B`**, `sha256:987261cd8b0b…`. 🔴 **The payload's copyright line reads © *2014-2017* — an inherited boilerplate header on a repository created in `2023`. The GRANT is unambiguous MIT; the date in it is not evidence of anything.** | 🟡 **`45★` / `22` forks — a `2:1` ratio, so it is being taken and run.** 🔴 **Treat it as a starting schema, not a product: no multi-tenancy claim, no stated auth review, no deployment documentation of the kind CorrectExam publishes. 🟢 Useful precisely because it is small enough to read end to end before trusting it with pupil data.** |
| **ระบบบริหารงานโรงเรียน (Thai school administration)** — https://github.com/goragodwiriya/sms | 🟢 **A school-administration system written for THAI schools, in Thai, by a Thai author — nine years of continuous maintenance (created `2017-09-23`, pushed `2026-11-13`).** JavaScript. | 🔴 **No agent surface.** 🔵 **Filed for its REGIONAL and LONGEVITY value: it is a working administrative system aligned to one APAC jurisdiction's own school-administration conventions, which is the part of a localisation that costs the most and transfers the least.** | 🟢 **MIT** — `main/LICENSE`, **`1,071 B`**, `sha256:d5b1933acb07…`, © *2026 Goragod Wiriya*. | 🟢 **`26★` / `30` forks — a ratio BELOW `1:1`, the strongest deployment signal of any row added this pass: more people have taken a copy to run than have starred it.** 🔴 **The interface, the documentation and the domain vocabulary are Thai. 🟢 That is a feature for a Thailand engagement and a hard stop elsewhere — the administrative MODEL is portable as a reference, the artefact is not.** 🔴 Single-author across nine years: a continuity risk to state plainly. |

---

## 🟢 Forty-third pass (`p838`, 2026-11-16) — **`7` rows (`157` → `164`): ENGLAND'S national curriculum platform joins the shelf, and with it the first row whose agent surface is maintained by the curriculum's own publisher**

🟢 **Every grant byte-read `2026-11-16` at the real default ref.**

| Platform | What institutions run it | Agent surface | Licence, re-read `2026-11-16` | Posture |
|---|---|---|---|---|
| **Oak National Academy** — https://github.com/oaknational/Oak-Web-Application | 🟢 **England's publicly funded national curriculum body: the teacher- and pupil-facing web estate serving Oak's curriculum nationally, free at the point of use.** TypeScript; created `2022-02-23`, pushed `2026-11-13`. The platform is one repo of a deliberately open estate — `oak-curriculum-ontology` (the curriculum as RDF/OWL/SKOS), `oak-curriculum-api` (the query surface), `oak-open-curriculum-ecosystem` (MCP app + TS SDK + semantic search), `oak-components` (React design system), `oak-consent-client` (consent API client). | 🟢 **Unlike every other row on this shelf, the agent surface is published BY THE CURRICULUM OWNER: `Aila` for lesson planning, `oak-agent-skills` for shared agent behaviour, `oak-ai-plugins` to reach teachers inside ChatGPT/Claude/Copilot/Gemini.** 🔵 **So for an England engagement the question is what to EXTEND — the `P85` doctrine this base wrote for India's Sunbird, now with a second instance.** `P87`. | 🟢 **MIT** — `main/LICENSE`, **`1,081 B`**, `sha256:d40d8b747c4f…`. 🔵 The estate is MIT with British-spelled `LICENCE` files on the newer repos and **OGL-UK-3.0 on the DATA**. | 🟢 **A state-funded curriculum authority publishing its platform, its ontology, its API and its agent layer under permissive terms is the strongest procurement story in this file** — the incumbent is open, so a client is extending public infrastructure rather than buying a replacement. 🔴 **Stated limits: `27★`/`9` forks — small numbers for a national platform, so argue from provenance not popularity; Aila's README declares itself internal-use-oriented; the ontology is `v0.1.3` "early release, subject to change"; and the curriculum encodes ENGLAND's National Curriculum, so it does not transfer to another jurisdiction without re-mapping.** |
| **CrownLabs** — https://github.com/netgroup-polito/CrownLabs | 🟢 **Kubernetes-based remote, on-demand environments for teaching labs, assessment and research — VMs and containers — built and run by Politecnico di Torino's NetGroup and used to deliver university lab courses at scale.** Go; created `2020-03-09`, pushed `2026-11-15` (day of measurement). | 🟢 **The agent surface is the LAB ITSELF as a disposable, reproducible target: an agent can be given a real machine per student with no risk to anything else, which is the missing substrate for autograding that must RUN code rather than read it.** 🔵 Pairs with `tmc-cli-rust`/`RiceChecks`/`Drop Project` — they grade, this is where grading safely executes. `P89`. | 🟢 **Apache-2.0** — `master/LICENSE`, **`11,356 B`**, `sha256:22f773775976…`. 🔴 Default ref **`master`**, not `main`. | 🟢 **The largest and most actively maintained row added this pass: `136★` / `76` forks, a `1.8:1` ratio that says real deployments.** 🟢 **Six years of continuous use at an operating university under Apache-2.0.** 🔴 **It is a Kubernetes platform: the engagement cost is cluster operation, and a client without K8s capability is buying an operating burden, not just software.** |
| **octolib.org** — https://github.com/yamanidev/octolib.org | 🟡 **A student-managed library for ESI Sidi Bel Abbès (École Supérieure en Informatique), hosting lessons, labs and past exams.** Astro; created `2023-07-23`, pushed `2026-11-15`. | 🟡 **The agent surface is retrieval over an institution's OWN past papers and lab sheets — the corpus a tutor must be grounded in for exam preparation to be credible, and the corpus almost no platform exposes.** | 🟢 **MIT** — `main/LICENSE`, **`1,080 B`**, `sha256:c6e635a40028…` | 🟢 **Filed as the first AFRICAN (Algeria) institutional row in this file, and it is a student-built one — which is the honest shape of the supply there.** 🔴 **`31★` / `2` forks, single-institution scope, French/Arabic-context content: adopt the pattern (institutional corpus as a static, versioned site), not the deployment.** 🔵 **Recorded against `T135`: EMEA is not only the EU, and the non-EU EMEA supply this base finds is institutional and small rather than absent.** |
| **上课 (shangkeschedule)** — https://github.com/qiqqqqq517/shangkeschedule | 🟡 **An open-source, ad-free course-timetable app for Chinese students — Kotlin Multiplatform + Compose Multiplatform, so one codebase serves Android/iOS/desktop.** Created `2026-08-25`, pushed `2026-11-09`. | 🟡 **Thin but real: the timetable is the student's actual daily entry point, and an agent that knows what class is next is the cheapest useful personalisation an institution can ship.** 🔵 Complements `P77` (timetabling where the solver decides) from the institution side. | 🟢 **Apache-2.0** — `main/LICENSE`, **`11,393 B`** (a DIFFERENT byte-length from the `11,337`/`11,352`/`11,356`/`11,357` stock Apache payloads also read this pass), `sha256:f7da4a65bd5a…` | 🟡 **`38★` / `3` forks, three months old.** 🟢 **Filed as APAC student-facing supply that is genuinely licensed and genuinely cross-platform — rarer in the Chinese-language channel than the volume suggests, since `T135` finds most of that channel is coursework.** 🔴 Chinese-language UI and timetable conventions (课程表 formats) are assumptions, not configuration. |
| **LessonsApp** — https://github.com/ChurchApps/LessonsApp | 🟡 **The web front end for viewing and subscribing to structured lesson series — TypeScript, created `2021-06-18`, pushed `2026-11-15`.** Part of the ChurchApps estate (a multi-application open platform for congregational organisations). | 🟡 **Curriculum DELIVERY and subscription rather than authoring: the agent surface is adaptation of a prepared lesson to a specific group, plus scheduling.** | 🟢 **MIT** — `main/LICENSE`, **`1,067 B`**, `sha256:1b7227343b83…` | 🟡 **`15★` / `9` forks.** 🟢 **Filed because non-formal education — faith, community and volunteer-run teaching — is a real and under-served delivery segment, and this is the only row in the file built for it.** 🔴 Domain assumptions are congregational; MIT, so adaptable. |
| **IITP-DABT Job Matching** — https://github.com/sweetk-dev/03-IITP-DABT-JobMatching | 🟡 **A customised education and job-recommendation module (맞춤형 교육 및 일자리 추천) delivered under Korea's IITP (Institute of Information & Communications Technology Planning & Evaluation) programme.** Python; created `2025-06-20`, pushed `2026-09-01`. | 🟡 **Recommendation across a TRAINING-TO-EMPLOYMENT boundary — the shape `P86` describes, where the engagement is funded from the workforce rail rather than the education rail.** | 🟢 **MIT** — `main/LICENSE`, **`1,086 B`**, `sha256:200f31db9392…` | 🟡 **`12★` / `7` forks.** 🟢 **Filed as the first KOREAN row in this file, and it matters because Korea's AI Basic Act (in force `2026-01-22`) names education a high-impact sector — so a Korean engagement now has both a regulatory trigger and a government-funded reference module in the open.** 🔴 Korean-language, and a research-programme deliverable: read it as provenance for the domain model, not as a maintained product. |
| **dapodiksq** — https://github.com/GANNER-STUDIO/dapodiksq | 🔴 **Real-time access to Dapodik (Data Pokok Pendidikan) — Indonesia's national school-level education data system.** Created `2026-11-02`, pushed `2026-11-04`. Sibling: `mrizalbasri/Equora` (🟢 MIT, `1,088 B`, `sha256:1630acba72ea…`, `0★`, Svelte) — an Indonesian education-data platform for regional exploration and MCDA priority analysis. | 🟡 **Both are the DATA floor beneath any Indonesian agent: school rolls, regional coverage, priority ranking.** | 🟢 **MIT** — `main/LICENSE`, **`1,070 B`**, `sha256:563368177a58…` | 🔴 **`1★` / `0` forks, two days of commits, no declared language.** 🔴 **Filed explicitly as an INFORMED GAP rather than a recommendation — `T135`.** 🟢 **The honest statement for an Indonesian engagement: the national data layer is being opened by individuals at `0–1★`, there is no institutional open platform equivalent to Sunbird or Oak, and a studio entering that market is building the layer, not extending it.** |

---


## 🔴 Forty-second pass (`p837`, 2026-11-16) — **INDIA'S NATIONAL EDUCATION STACK IS RESTORED TO THIS FILE, after being dropped from it in a rewrite on `2026-11-12` while this base went on publishing it as filed**

🟢 **`10` rows (`147` → `157`): `3` RESTORATIONS and `7` new. Every grant byte-read `2026-11-16` on
the real default branch.**

🔴 **The admission this pass owes, and it is this file's defect rather than a gap in the world.**
`p677` published `sunbird-ed/sunbirded-portal` as *filed to `verticals/solutions.md`*, having
re-measured its payload first-hand. **It is not in this file, and `sunbird` appears `0` times in
every curated shelf in this base.** 🟢 **The reasoning survived — `54` and `115` mentions across the
two append-only trending files, including `T126`'s licence census that measures the Sunbird estate
at `196/212 = 92.5%` permissively licensed, the highest of any education authority anywhere in
this base.** 🔴 **Only the ROW died.** The dating, the census and the `ACTION` that makes the check
mechanical are in [`repos/foundations.md`](../repos/foundations.md) `D837-1`; the rule is `T130`.

### 🟢 `3` rows RESTORED — payloads reproduce `p677`'s published figures exactly, ten days on

| Platform | What institutions run it | Agent surface | Licence, re-read `2026-11-16` | Posture |
|---|---|---|---|---|
| **Sunbird ED** — https://github.com/Sunbird-Ed/SunbirdEd-portal | 🟢 **India's national public digital infrastructure for education — the platform family behind DIKSHA, serving all `36` states and union territories in `30+` languages.** One of a multi-repository stack: `Sunbird-Knowlg/knowledge-platform` (content, taxonomy, DIAL codes), `Sunbird-Lern/userorg-service` (identity, tenancy, enrolment — **channel isolation is why one deployment serves `36` boards**), `Sunbird-inQuiry/editor-v2` and `player-v2` (QuML authoring and delivery). | 🟢 **For an APAC public-sector engagement this is the INCUMBENT, so the question is what to EXTEND, not what to build.** The surface is agent-per-role on top of an existing system of record: content tagging against the national taxonomy, DIAL-code resolution, multilingual lesson adaptation, enrolment triage. `P85`. | 🟢 **MIT** — `master/LICENSE`, **`1,072 B`**, `sha256:7dde06716f25…`, © *2018 Project Sunbird*. 🟢 **Exact reproduction of the figure `p677` published.** | 🟢 **The most permissively licensed platform of its deployment size anywhere in this base, and `T126` says that is a PROCUREMENT DOCTRINE rather than an accident.** 🔴 **Read the fork column, not the star column: `41★` against `318` forks — `7.8:1`, the most extreme ratio on these shelves. Nobody forks a web portal `318` times to read it.** 🔴 **Delivery warnings, stated: the portal's own last push is `2026-02-21`, so the motion is in the siblings; the default ref is `master`, not `main`; and `SunbirdEd-mobile-app` release branches `release-2.6.0`/`2.7.0` carry NO grant at `25` root paths while the project is MIT on `main` — an engagement that pins an old Sunbird release, which India engagements do, pins a branch with no licence file on it.** |
| **AureusERP** — https://github.com/aureuserp/aureuserp | 🟢 **A full open ERP on Laravel/Filament — the money-and-people half of an institution, which an LMS does not provide.** `12,239★` / `627` forks. | 🟢 **`Pattern D`: the academic system of record stays, the ERP carries finance, HR, procurement and inventory, and the agent sits across the seam** — fee reconciliation, purchase-request triage, payroll exception explanation. | 🟢 **MIT** — `master/LICENSE`, `1,077 B`, `sha256:c6dca3b0db5b…`, © *2010-2025 Webkul Software*. 🟢 Exact reproduction. | 🟢 **Build-safe and genuinely large: `12.2k★` makes it the most-starred MIT ERP on these shelves, against `OpenEduCat` at LGPL-3.0 and the whole Frappe education family at GPL/AGPL.** 🔴 Default ref `master`. 🔵 Not education software — it is the half of an education institution that education software ignores. |
| **Agora Flat** — https://github.com/netless-io/flat | 🟢 **An open-source interactive online classroom: real-time whiteboard, multi-party video, recording and replay.** `6,445★` / `877` forks, pushed `2026-11-10`. | 🟢 **The SYNCHRONOUS surface this file is thin on.** Everything else here is asynchronous — LMS, SIS, MOOC, assessment. The agent surface is live: transcription, in-session summarisation, and the replay artefact that `P83`'s tutoring evaluation can actually be scored against. | 🟢 **MIT** — `main/LICENSE`, `1,062 B`, `sha256:8fa1566550df…`, © *2021 Agora*. 🟢 Exact reproduction. | 🟢 **Build-safe, maintained, and the client is cross-platform (Windows, macOS, web).** 🔴 **The MIT grant covers the CLIENT; the real-time transport behind it is Agora's commercial RTC service — the licence is not the bill.** Say that at proposal time. |

### 🟢 `7` NEW rows

| Platform | What it is | Licence, byte-read `2026-11-16` | ★ / forks · ref · pushed | Region & posture |
|---|---|---|---|---|
| **Tuantuan Cloud Study** — https://github.com/yang-jiacheng/selfstudy-server | 🟢 **A deployed online self-study platform (Java), server side of a mobile product — "study anytime, anywhere".** The most-starred new vertical row this pass. | 🟢 **Apache-2.0** — `master/LICENSE`, `11,343 B`, `sha256:3391ea6318f0…` | `101★` / `8` · 🔴 `master` · `2026-11-03` | **APAC — China.** 🟢 **Filed because this file's China tier was one university LMS (`p813`) and nothing consumer-side.** 🔴 Single author; documentation is Chinese-first. |
| **ÉTSMobile (Notre-Dame)** — https://github.com/ApplETS/Notre-Dame | 🟢 **The 4th-generation student mobile gateway for École de technologie supérieure, Montréal — grades, schedule, account, campus services in one Flutter app.** Student-run club (`ApplETS`), six years of history. | 🟢 **Apache-2.0** — `master/LICENSE.md`, `11,356 B`, `sha256:43070e2d4e53…` | `46★` / `13` · 🔴 `master` · `2026-11-05` | **North America — Canada (Québec).** 🟢 **The STUDENT-FACING mobile tier, which this file had only in Europe and India.** 🔵 It is also a French-language Canadian build, which is the rarer thing on these shelves. 🔴 Volunteer-maintained against one institution's SIS — the value is the pattern and the seam list. |
| **UKit** — https://github.com/KAE-Lab/UKit | 🟢 **Companion app for students in Bordeaux, iOS and Android.** | 🟢 **Apache-2.0** — `main/LICENSE`, `11,363 B`, `sha256:4983e1b71316…` | `11★` / `0` · `main` · `2026-11-15` | **EMEA — France.** 🟡 **`11★`, `0` forks, pushed the day before this pass — an early bet, sold as one.** 🟢 Filed as the second data point in a pair with ÉTSMobile: the student-companion app is a repeatable, locally-built shape, and a studio proposing one should be able to name two working precedents on two continents. |
| **HSC Stack** — https://github.com/hscstack/platform | 🟢 **A curated resource platform for HSC and SSC students of Bangladesh, "built by members, for everyone".** Vue. | 🟢 **Apache-2.0** — `main/LICENSE`, `11,357 B`, `sha256:c71d239df917…` (stock) | `13★` / `2` · `main` · `2026-11-09` | **APAC — Bangladesh.** 🟢 **A national-examination-cohort platform built by the cohort itself, under a permissive grant — the shape this base has for Brazil and England and did not have for South Asia outside the Sunbird estate.** 🔴 `13★`, five months old. |
| **vagaLume** — https://github.com/PedroCamargoLINCE/vagaLume | 🟢 **Aggregates every internship, research programme, fellowship and summer school open to students, collected and refreshed on a schedule.** Python, from a Brazilian university lab (LINCE). | 🟢 **Apache-2.0** — `main/LICENSE`, `11,358 B`, `sha256:cfc7749b96f6…` | `13★` / `4` · `main` · `2026-11-15` | 🟢 **LATAM — Brazil, and it matters disproportionately.** 🔴 **`T126`'s authority census measured LATAM education authorities at `0` permissively licensed repositories against Sunbird's `196`.** 🟢 **This is not an authority, it is a university lab — and it is a live, permissive, LATAM-authored education platform row, which this file has had almost none of.** 🔴 **One month old, `13★` — filed on provenance and gap-fit, and the gap is the argument.** |
| **GEAR (WebXR for VET)** — https://github.com/blagojevicboban/GEAR | 🟢 **An open WebXR platform designed specifically for Vocational Education and Training** — the simulated-workshop shape, delivered in a browser instead of a headset-only app. TypeScript. | 🟢 **MIT** — `main/LICENSE`, `1,073 B`, `sha256:0ccee16b71b8…` | `0★` / `0` · `main` · `2026-11-11` | **EMEA.** 🟡 **`0★`, `0` forks.** 🟢 **Filed for ONE reason, stated plainly: this base has declared the vocational platform tier a measured gap in five languages (`p829`, `T114`, `T118`), and the single thing a VET programme needs that a general LMS cannot give it is a safe simulated workshop.** 🔴 **Do not propose this as a product. Propose it as evidence that the browser-delivered route exists, and price the build.** `P86`. |
| **exam-proctor (LTI 1.3 in Moodle)** — https://github.com/shaheeranser/exam-proctor | 🟢 **A proctoring platform that runs INSIDE Moodle over LTI 1.3** — React/TS client, Express service. | 🟢 **Apache-2.0** — `main/LICENSE`, `11,358 B`, `sha256:c95bae1d1ce0…` | `0★` / `0` · `main` · `2026-10-11` | **APAC.** 🟢 **Filed for its ARCHITECTURE, not its traction: it is the only row in a population of `540` permissively licensed proctoring repositories that mounts through the standards layer this file already documents, rather than asking an institution to adopt a second system.** 🔴 **`0★`, four months old, one author.** 🔵 **The integration CONTRACT it implements is better documented by `openedx/mockprock` — Apache-2.0 per GitHub's licence field and `NO-GRANT-AT-ROOT` in the bytes, so recorded here as a contract to read and NOT as a dependency to ship (`agents/top.md` this pass).** |

### 🔴 Declared nils and placements, so silence is not read as coverage

- 🔴 **Indonesia — a national platform with NO open-source estate.** `Rumah Pendidikan`, Indonesia's
  unified digital education platform (an ITU WSIS Prizes 2026 entry, with `Merdeka Mengajar` now
  reached through the `Ruang GTK` space inside it), publishes **no repository and no licence**.
  Enumerated this pass: **`user:kemdikbud` → `1` repository** (`Kemdikbud/kemdikbud`, `0★`, **no
  licence**, last pushed `2025-08-27`), and `user:pusdatin` → `3` repositories, all unrelated
  office tooling from 2015–2016. `user:kemendikbudristek` does not resolve. 🔵 **The ministry's
  announced AI work is a Pusdatin partnership on Google Gemini — proprietary.** 🟢 **So the fourth
  most populous country in the world runs a national education platform a studio cannot start
  from, and an Indonesian engagement must IMPORT build-safe supply from these shelves and localise
  it.** Same conclusion `p836` reached for Vietnam, Korea and the Gulf, now measured for Indonesia.
- 🟡 **The UAE's `25` generative-AI prohibitions for schools (February 2026) surfaced on the APAC
  leg and is recorded under EMEA**, which is where this base's closed region vocabulary puts the
  Gulf. 🔵 **Noted because the query leg and the region field disagreed, and the field wins.**
- 🔴 **UDL (Universal Design for Learning) remains a TRUE nil, now measured with a better
  instrument:** `universal design for learning accessibility education in:name,description
  license:mit` returns **`0` repositories**. 🟢 **Two of this base's three standing nils fell this
  pass; this one did not.** `T128`.

## 🟢 `2026-11-15` (forty-first pass, `p836`) — **the ACCESSIBILITY-CONFORMANCE vertical enters this file with `0` prior rows, and the TIMETABLING system a school runs every term**

🟢 **`2` rows added (`145` → `147`), both **MIT**, both byte-read `2026-11-15` on the default
branch.** The three engine-layer rows from the same sweep went to `repos/foundations.md`.

🔴 **Measured state of this file before this pass: `0` mentions of ADA Title II, `0` of WCAG, `1`
of "accessib-" across `145` rows.** 🟢 **That is now corrected, and it matters because accessibility
is the one education-AI obligation that is already binding with named dates and a named enforcer
in two of this base's four regions** — see `intel/market.md` this pass for the dates and the
correction they carry.

🔵 **Why these two rows and not more.** The sweep returned eleven accessibility-adjacent and
timetabling-adjacent candidates; **nine were already filed by slug or had no locatable grant** (see
the probe ledger in `repos/foundations.md` this pass). 🟢 **Two survived. Two rows are written.**

| Platform | What institutions run it | Agent surface added this pass | License | Risk posture |
|---|---|---|---|---|
| **Ace by DAISY (desktop)** — https://github.com/daisy/ace-gui | **Publishers, university disability-services and accessible-media units, and ministry textbook programmes** — the desktop application a non-engineer on staff actually opens to check a digital textbook. Ships for **Windows, macOS and Linux**; latest version stated in the README as **`v1.4.6`**; default branch `master`. 🟢 **This is the human end of the same engine `repos/foundations.md` filed as a library this pass** (`daisy/ace`), which is why a studio can hand the checking back to the client's own staff instead of owning it forever. | 🟢 **The reviewer's console in `P76`.** Automated EPUB conformance is decidable for the machine-testable subset only; **alt-text adequacy, reading order and image-description quality are not.** The agent surface is: a VLM proposes alt text and long descriptions at catalogue scale, **this GUI is where a human accepts, edits or rejects each one**, and the accepted text is written back to the package. 🔴 **Do not automate the accept step** — a wrong description that passes an automated check is worse than a flagged gap, because it reports conformance while misinforming the student who depends on it. | 🟢 **MIT — byte-read `2026-11-15`** (`master/LICENSE`, **`1,073 B`**, `sha256:4c8aeea93ee9…`, title line `MIT License`, `Copyright (c) 2018 DAISY Consortium`; rendered sidebar states `MIT License`) | 🟢 **Build-safe, and re-brandable.** MIT permits a studio to fork, re-skin and ship this as part of a client-facing remediation console. 🔵 **`25★`** — 🔴 **traction is low and says nothing about fitness here:** this is the DAISY Consortium's own reference GUI for a W3C-recommended standard, and `T109`'s inversion (traction concentrated in copyleft, build-safe rows sitting near zero) applies to the whole accessible-publishing tier. 🟡 **No release date was visible on the rendered page; version taken from the README.** |
| **Timetabler** — https://github.com/sukrutrao/Timetabler | **Schools, colleges and university departments building a term timetable** — described by the project as "a customizable timetabling software for educational institutions". It encodes timetabling constraints as a **SAT formula** and solves them with a **MaxSAT solver**; default branch `master`, `345` commits. 🔵 **The institutional job it does is the one every term starts with and no LMS, SIS or MOOC row on these `147` shelves touches.** | 🟢 **A solver, not a chatbot, and that is the point.** The agent surface is **constraint ELICITATION, not constraint solving**: an LLM turns a department's prose rules — "no two courses sharing a cohort in one slot", "lab blocks stay contiguous", "this teacher is part-time on Fridays" — into the solver's declared constraint format, and the **MaxSAT solver** decides. 🔴 **Never let the model produce the timetable itself.** A solver returns a certificate: either the hard constraints are satisfiable or they are not. A model returns a plausible grid with a double-booked cohort inside it, and the failure surfaces in week one. See `P77`. | 🟢 **MIT — byte-read `2026-11-15`** (`master/LICENSE`, **`1,087 B`**, title line `MIT License`, `Copyright (c) 2017-2018 Sukrut Rao, Prateek Kumar`) | 🟢 **Build-safe.** 🔴 **Maintenance posture is the real risk, and it is stated plainly: `43★`, copyright line ends `2018`, and this is a two-author academic project** — treat it as a **reference model and constraint vocabulary** to lift, not as a dependency to pin a delivery to. 🟢 **The production-grade alternatives on these shelves are already filed and permissive:** `google/or-tools` (**Apache-2.0**, CP-SAT, stable `v9.15`, `2026-01-12`), `timefoldai/timefold-solver` (Apache-2.0 core), and `UniTime/cpsolver` with its examination-timetabling extension. 🔵 **`P77` wires `Timetabler` as the model and OR-Tools CP-SAT as the engine for anything that must survive a term.** |

🔴 **Declared nil, so silence is not read as coverage:** the timetabling sweep
(`open source exam timetabling constraint solver school scheduling github Apache 2026`) returned
**no mature, maintained, education-specific timetabling PLATFORM under a permissive licence.**
What exists is **general-purpose Apache-2.0 solvers** (OR-Tools, Timefold) plus **student and
academic projects** (`pl-sch/its-exam-timetabling`, `budrus123/GraduationProject`,
`HeerRana/Exam-timetabling-GeneticAlgorithm`, `CarolinaBianchi/ETPsolver` — licences not located).
🟢 **That gap is itself the commercial opening, and `P77` is written against it.**


## 🟢 `2026-11-15` (thirty-ninth pass, `p834`) — **the EXAMINATION-PLATFORM vertical enters this file, `38` passes late, and it was always there**

🟢 **`5` rows added (`140` → `145`): `3` build-safe (MIT ×2, Apache-2.0 ×1) and `2` AGPL-3.0 filed
as reference platforms with the posture stated per row.**

🔴 **The admission this pass owes: this shelf has carried LMS, SIS, MOOC, AAC and early-grade
measurement platforms, and never once an EXAMINATION platform — the system a school runs whenever
it assesses anyone.** 🟢 **`在线考试系统` returns `1,766` repositories.** 🔵 **The vertical was
invisible for the same reason the grading gap was (`T114`, `T118`): every sweep that would have
found it ran in English.**

🔴 **And the traction is inverted against the licence, again (`T109`): the leaders are
AGPL-3.0 at `3,915★` and `91★`, while the three rows a studio can actually ship sit at
`0`, `0` and `1★`.**


## 🟢 `2026-11-15` (thirty-eighth pass, `p833`) — **`ACTION p832-C` DISCHARGED: both carried licence conflicts settled by bytes, and one of them had no answer at all**

🟢 **`p832` registered two conflicts rather than guessing at them and asked for byte-reads with
branch resolution. Both were run. Both are settled. The result is one correction and one honest
nil.**

### 🟢 Open edX — **`AGPL-3.0`. The `MIT` limb is FALSE.**

`openedx/edx-platform` → **`GRANT at master/LICENSE`**, byte-read `35,136 B`,
`sha256:e12d78569742…`, opening line `GNU AFFERO GENERAL PUBLIC LICENSE / Version 3, 19 November
2007`. Ref set probed: [`master` `2u/project-theseus` `2u/release` + `3` more].

🔴 **The likely origin of the `MIT` limb is an institution name read as a licence name** — Open edX
came out of MIT and Harvard, and a search summary carried `MIT` into the licence column. 🔵 **This
base's other sections already had it right** (`AGPL-3.0` at three separate places in this file), 🔴
**which is the actual lesson: the conflict was INTERNAL, and an inbound summary was allowed to
contradict a shelf that was already correct.**

🔵 **Build consequence, and it is the reason this mattered.** AGPL's network clause reaches a
HOSTED derivative: a client-facing Open edX fork delivered as a service must offer its source to its
users. 🟢 **Every pattern in `compose/patterns.md` that puts Open edX under a deliverable inherits
that obligation, and it is a conversation to have at proposal time rather than at delivery.**

### 🔴 Forma LMS — **NEITHER `LGPL` NOR `GPL` is in the repository. Recorded as unverifiable-at-source.**

`formalms/formalms` → **`NO-GRANT-AT-ROOT`**, probed `10` case-aware filenames × `2` resolved heads
(`master`, `dev`) = `20` probes, all `404`. `composer.json` `404`s. The `README.md` (`6,198 B`,
byte-read) contains **no occurrence of the string `licen`**. GitHub's own licence field:
`NOASSERTION`.

🟢 **So the dispute this base carried was between two claims that are both OUTSIDE the
repository** — project-website prose on one side, a comparison article on the other. 🔵 **`T81`
says only the bytes settle it; here the bytes say nothing, and *that* is the finding.** 🔴 **Forma
LMS is therefore recorded on the same footing as `OS4ED/openSIS-Classic`: a deploy-and-configure
platform, nothing to fork or redistribute, until someone obtains a grant in writing.** 🔵 **Not
resolved to the likelier answer, which is what `p832` explicitly asked for.**

🟡 **Method note, and it is the reusable part.** This is the probe described in `D833-1` — heads
resolved from `git ls-remote --heads` BEFORE the filename loop, and the probed ref set printed
inside the verdict. 🔴 **`p832` showed that one wrong branch argument nils every filename at once
and produces a verdict byte-identical to a true absence; `3` of this base's standing absence claims
were false for exactly that reason.** 🟢 **The two verdicts above are falsifiable without re-running
them, because the refs they probed are in the verdict.**

## 🔴 `2026-11-15` (thirty-seventh pass, `p832`) — **`0` platform rows added, and the nil is the measurement: the LMS/SIS vertical leg returned nothing this base does not already hold**

🟢 **The mandated vertical leg ran (`open source platform education LMS SIS MIT Apache
self-hosted`) and every platform it named was checked against this base's `7,125`-slug known set:**
`frappe/lms`, `OpenOLAT/OpenOLAT`, `openeducat/openeducat_erp`, `francoisjacquet/rosariosis`,
`openedx/edx-platform`, `instructure/canvas-lms`, `moodle/moodle`, `apereo/opencast`, `oppia/oppia`,
`h5p/h5p-php-library`. 🔴 **All ten already held.** 🔵 **`T99`'s LMS-tier finding and `T63`'s
saturation finding both hold; the vertical shelf is at `140` rows and this leg has stopped
producing.**

🔴 **The eleventh name was not a repository at all.** The search summary named **openSIS** as a K-12
SIS option; the obvious address `OpenSIS-Classic/OpenSIS-Classic` returns **`HTTP 422` — it does not
exist**. 🟢 **The real address is `OS4ED/openSIS-Classic` (`351★`, pushed `2026-10-26`), already
held.** 🔵 **Recorded because inferring a slug from prose is precisely how an invented row enters a
base, and this base has a gate class for exactly that.**

🔴 **And it is ungranted, confirmed rather than assumed.** `OS4ED/openSIS-Classic` was re-probed
this pass **with branch resolution** (`D832-1`) across `6` resolved heads including `master` and
`Version_8.0`, against the full `31`-name case-aware filename list: **`NO-GRANT-AT-ROOT` on every
one.** 🟢 **A CONFIRMED true absence** — which matters, because the same sweep found `3` of this
base's standing absence claims to be FALSE (`T112`). 🔵 **A `351★` SIS with no grant of any kind is
a deploy-and-configure platform only; nothing may be forked or redistributed from it.**

🟡 **One licence conflict carried forward from the global leg and NOT resolved this pass:** the
search summaries disagree about **Open edX**, listing it as both `AGPL` and `MIT`, and about
**Forma LMS** (`LGPL` vs `GPL`). 🔵 **Both are `CITED, NOT READ`. This base's `T81` rule says the
FIELD errs in both directions and only the bytes settle it** — registered as `ACTION p832-C` rather
than guessed at here.

# Education vertical platforms — real systems to customize AI on top of

## 🟢 The FOUNDATIONAL-MEASUREMENT tier — **the instrument the early-grade evidence is actually collected on** (new, thirty-sixth pass `p831`) (5 rows)

🔴 **The gap this tier closes is the oldest kind in this base: a name repeated and never shelved.**
`Tangerine-Community/Tangerine` is named `6` times in `repos/trending.md` across `35` passes. It
was never filed anywhere. It is the platform EGRA and EGMA — the Early Grade Reading and Early
Grade Mathematics Assessments, the two instruments every ministry and every donor in
`intel/market.md` reports against — are administered on, it works **offline by design**, and it was
pushed `2026-11-12`.

🔵 **Why these five are here and not on `agents/top.md`: every one is copyleft.** 🟢 **That is the
tier's defining fact, and it inverts the usual posture.** The child-facing PRACTICE layer
(`agents/top.md`, `p831`) is Apache-2.0 and BSD-2-Clause throughout; the MEASUREMENT layer is
GPL-3.0, AGPL-3.0 and MPL-2.0 throughout. 🔴 **A studio can fork the game. It cannot quietly fork
the gradebook.**

| Platform | What institutions run it | Agent surface added this pass | License | Risk posture |
|---|---|---|---|---|
| **Tangerine** — https://github.com/Tangerine-Community/Tangerine | Ministries, USAID/FCDO-funded programmes and research teams running **EGRA / EGMA** and other early-grade assessments in low-resource settings; offline-first on shared Android tablets | 🟢 **`119★`, pushed `2026-11-12` — the live instrument of the whole foundational tier.** An AI surface attaches at the SCORING-AID boundary (transcribing an oral reading fluency recording, flagging an enumerator's inconsistent entries) and must stop short of the score itself | 🔴 **`GPL-3.0` — byte-read `LICENSE.txt`, `35,147 B`, `sha256:8ceb4b9ee5ad…`** | 🔴 **Strong copyleft on a SERVER-SIDE platform.** Modifications that are distributed must be published under GPL-3.0. 🟢 **Deploy-and-configure is clean; a forked, redistributed Tangerine is not.** 🔴 **And the sharper constraint is not the licence**: under the EU AI Act Annex III point `3`, assessing learning outcomes is high-risk by construction, so an engagement builds the TRANSCRIPTION and leaves the SCORE to the instrument |
| **tangy-form** — https://github.com/Tangerine-Community/tangy-form | The form runtime inside every Tangerine deployment — the component an integrator actually touches | 🟢 **`16★`, pushed `2026-11-10`.** Web-component form engine with offline storage; the natural insertion point for an authoring assistant that DRAFTS an assessment form for human approval | 🔴 **`GPL-3.0` — byte-read `LICENSE.txt`, `35,147 B`, `sha256:8ceb4b9ee5ad…`** | 🔴 Same posture as its parent, byte-identical grant. 🔵 **Filed separately because it is separable**: a programme that wants Tangerine's form model without Tangerine's server takes this and inherits the same obligation |
| **Chimple (bahama)** — https://github.com/chimple/bahama | The current Chimple Learning App — the maintained successor to the `2019` Apache-2.0 XPRIZE build shelved in `agents/top.md` | 🟢 **`8★`, pushed `2026-10-13`.** The live line of a field-trialled early-grade curriculum | 🟡 **`MPL-2.0` — byte-read `16,725 B`, `sha256:1f256ecad192…`** | 🟡 **Weak, FILE-LEVEL copyleft.** Modified MPL files must stay MPL and be published; new files beside them need not be. 🟢 **The most workable copyleft posture in this tier** — a studio can add proprietary modules and must publish its changes to Chimple's own files |
| **Chimple (cuba)** — https://github.com/chimple/cuba | Chimple's current web/app delivery surface, pushed `2026-11-13` | 🟢 The newest code in the Chimple line, and the one an integration would actually meet | 🔴 **`AGPL-3.0` — byte-read `LICENSE.md`, `34,522 B`, `sha256:20b067f86de3…`** | 🔴 **Network copyleft: serving it over a network is distribution.** A hosted deployment for a client triggers the source obligation even with nothing shipped. 🔵 **This row and the one above it are the evidence for `T108`'s second half — the Chimple corpus moved Apache-2.0 → MPL-2.0 → AGPL-3.0 as it moved `2019` → `2026`** |
| **Linguaculturalists (Phoenicia)** — https://github.com/XPRIZE/GLEXP-Team-The-Linguaculturalists | A Global Learning XPRIZE finalist stack; the mirror `mhall119/Phoenicia` carries the same lineage | 🟡 **`14★`, unpushed since `2017-04-19` — filed as an ARCHIVE, not a platform.** Its value is the curriculum model and the field data shape, not the code | 🔴 **`GPL-3.0` — byte-read `COPYING`, `35,147 B`, `sha256:8ceb4b9ee5ad…`** | 🔴 Strong copyleft, and byte-identical to Tangerine's grant — **three repositories from three unrelated publishers shipping one `sha256`, which is `T41`'s bound and not a lineage claim** |

## 🟢 The ASSISTIVE-TECHNOLOGY PLATFORM tier — **the AAC systems institutions already run** (new, thirty-fifth pass `p830`) (3 rows)

🔴 **This shelf held `0` rows for assistive technology across `34` passes.** `grep -ci` for
`cboard`, `arasaac`, `pictogram` and `assistive` over `verticals/solutions.md` returned **`0`**,
while `agents/trending.md` had discussed `AAC` on `24` lines since `p621`. The platforms were
known to this base and never placed where a delivery team looks for them.

🔴 **Read the licence column before the star column.** This is the first tier on this shelf where
**the two most-deployed platforms are both copyleft** — which does not make them unusable, it makes
them INTEGRATION targets rather than fork targets. The build-safe asset in the tier is the
government-granted PICTOGRAM SET, not the runtime.

| Platform | Repo | Licence | Stars | What it is |
|---|---|---|---|---|
| **ARASAAC** (Gobierno de Aragón) | https://github.com/juanda99/arasaac-frontend | 🟢 **MIT — byte-read** (`LICENSE.md`, `1,084 B`, `sha256:1db6216968f9…`, holder **`2016 Gobierno de Aragón`**) | 16 | **Region: EMEA — placed on a GOVERNMENT holder line, the strongest placement this base accepts.** 🟢 The Aragonese Portal of Augmentative and Alternative Communication: the pictogram set and front-end that most Spanish-language AAC software in BOTH hemispheres draws on. 🔵 **Its reach is the point for a LATAM engagement** — an EMEA public body publishing under MIT is what gives a Colombian or Mexican build a symbol vocabulary it does not have to commission. 🔵 **Re-measured this pass: `16★` at `p622` → `16★` today, but pushed `2026-10-24` → `2026-11-14`** — flat traction, live development, the signature of a funded public asset rather than a product. Consume it through `kitsteam/pictosearch` (MIT, `repos/foundations.md` `p830`) |
| **cboard** (UNICEF-backed) | https://github.com/cboard-org/cboard | 🔴 **`GPL-3.0` — byte-read** (`LICENSE.txt`, `35,141 B`, `sha256:589ed823e9a8…`) | 768 | **Region: Global.** 🟢 **The most-deployed open AAC communicator there is**, browser-based with text-to-speech, UNICEF support and `5,531` commits. 🔴 **`GPL-3.0`: the licence propagates.** A studio may deploy, host and configure it for a client and may contribute back; it may NOT fold it into a proprietary product. 🔵 **The build-safe pattern is an ADAPTER, not a fork** — talk to it, import/export its board format, keep your own code out of the combined work. 🔵 Re-measured this pass: `759★` at `p621` (`2026-11-02`) → **`768★`** today, `+1.2 %` in `13` days |
| **AsTeRICS Grid** | https://github.com/asterics/AsTeRICS-Grid | 🔴 **`AGPL-3.0` — byte-read** (`34,523 B`, `sha256:8486a10c4393…`) | *not retrieved* | **Region: EMEA** (AsTeRICS is an EU-funded Austrian lineage). 🟢 Offline-capable AAC grid system with device control. 🔴 **`AGPL-3.0` is the stricter case: network use counts as distribution.** Hosting it for a client triggers the source obligation. 🔵 **The permissive way in is `fjrodl/astericsgrid_ros` (Apache-2.0)** — a bridge, shelved this pass in `repos/foundations.md`. 🔴 **Star count deliberately left as `not retrieved` rather than guessed: the free-text search channel does not return this repository at all**, although its `LICENSE` byte-reads `200`. 🔴 **And a name-integrity warning: the channel DOES return `astericsfree/AsTeRICS-Grid`, `astericsgridfree/AAC-Grid-Let-Me-Talk-Asterics-LogoRemakeFour` and `logoremakefour8/Asterics-Grid-AAC-LRF-LogoRemakeFour` — low-star look-alikes outranking the canonical project. Resolve this brand by byte-read only** |


## Thirty-fourth pass (`p829`, 2026-11-15) — `0` rows added, and the vocational PLATFORM tier is declared a measured gap

🔴 **`p829` added NO rows to this shelf, and the gap it looked for is now measured rather than
assumed.** The pass went looking for the vocational/TVET equivalent of Moodle — a training-provider
or apprenticeship-management platform a studio could customise AI on top of — and the mandated
platform leg (`open source platform education ERP CRM MIT Apache vocational training`) returned
**`OpenEduCat` and nothing else**, on its own vendor pages, declared `LGPL-3.0` Community Edition.
🔵 **`OpenEduCat` is already on this shelf and its marketing page does list vocational training
institutes among its targets — but a vendor page is not a grant and a general school ERP is not an
apprenticeship-management system.**

🔴 **The declared gap, stated so a later pass does not mistake silence for coverage:** this base
holds **`0` open-source platforms for apprenticeship or vocational-training ADMINISTRATION** —
no training-provider system, no end-point-assessment platform, no competency-record system. 🟢 **What
`p829` did find at that tier is NOT a platform but four single-purpose tools and one reference
dataset (`T102`), filed to `agents/top.md` and `repos/foundations.md`.** 🔵 **The reading is that the
vocational platform layer is proprietary (the German IHK and English EPAO markets are served by
closed vendors) and that `P69` therefore ASSEMBLES one from permissive parts rather than adopting
one — which is why `P69` is written as a build.**

🔵 **Named candidates refused, so they are not re-probed:** `elevate-for-humanity/Elevate-lms`
(`NOASSERTION`, `1★`) and `ApprenticeshipStandardsDotOrg` (`CC0-1.0` over a Rails application,
`T78`) — the second with regret, since it is the only North American artefact in the tier.

## Thirty-second pass (`p827`, 2026-11-15) — `0` rows added, and the reason is recorded rather than padded

🔴 **`p827` added NO rows to this shelf.** The mandated ERP/platform leg ran and returned the set
this base has held since `p805` — `OpenEduCat` (LGPL-3.0), `openSIS` (GPL-2.0/3.0), `RosarioSIS`
(GPL-2.0), `frappe/education` (GPL-3.0), `ERPNext` (GPL-3.0) — with no new entrant and no licence
change. 🟢 **The education platform tier remains overwhelmingly copyleft and `p827` found no new
permissive alternative.**

🔵 **Two candidates surfaced and BOTH were refused, which is the useful part.** **GegoK12** is
described as MIT on its own vendor page, with a free/paid module split the page does not itemise;
**Fedena** is listed as Apache-2.0 only inside a *competitor's* comparison table. 🔴 **Both licence
claims originate in marketing pages rather than in a repository, and neither resolved to a
verifiable `LICENSE` file on the channel available this pass.** 🟢 **A vendor page is not a grant.**
Shelving either would have grown the row count and put an unverified permissive claim in front of a
client — the exact failure `T93` and `T96` describe.

🔴 **Channel limit, which is why no re-verification was possible either:** `curl` to `github.com`
returned `403` on every attempt this pass, so **no byte-read over `raw.githubusercontent.com` ran in
`p827`**. Every licence cited this pass is read from the rendered GitHub sidebar via `WebFetch` on
`2026-11-15`. 🔴 **`ingest/derive-counts.py` could not be executed** (the runner declined to run
repository-provided code), so counts in this pass are direct `grep` heading tallies and are marked
as such rather than claimed GREEN.

🟢 **One re-measurement:** [`frappe/education`](https://github.com/frappe/education) reads `711★` /
`1,097` commits against `709★` held — drift only. 🔴 **Its licence is not visible on the rendered
page; the GPL-3.0 classification rests on `p824`'s byte-read of `license.txt` and was NOT
re-verified this pass.**

## 🟢 The NATIONAL SCHOOL SYSTEM-OF-RECORD tier — **the platform layer a European family actually logs into, and the one no query containing the word "education" can find** — added `p826` (9 rows)

🟢 **`T95`, as a platform table.** These are not education platforms a studio would propose: they are the systems a ministry or a school board already bought, which every parent in the country already has an account on, and which have no public API. 🔵 **The open agent surface over them is being written by individual parents and students, one country at a time, and `p826` is the first pass of this base to enumerate it.**

🔴 **`7` of the `12` repositories found in this tier carry no `LICENSE` file at all.** 🟢 **The `9` rows below are the ones worth naming — the `4` build-safe anchors, plus the unlicensed rows that mark a real platform whose only open surface cannot be used.** 🔵 **For an EMEA or LATAM engagement the cheapest move is not to write a connector: it is to ask a named developer for a licence.**

| Platform | Incumbent where | Open agent surface found | License | Stars |
|---|---|---|---|---|
| **WebUntis** (Untis GmbH) | 🇦🇹🇩🇪🇨🇭 The default timetabling and absence system across DACH K-12 | https://github.com/toughIQ/webuntis-mcp — 🟢 **the upstream of the tier's largest lineage**, read-only, explicitly parent-facing | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:2c0b8069fc10…`) | 0 |
| **WebUntis** (Untis GmbH) | 🇦🇹🇩🇪🇨🇭 as above | https://github.com/DenizCiger/untis-mcp — 🟢 **a SECOND, independent lineage** in Rust; `8` tools, all annotated read-only with output schemas; `find_free_rooms` is the tier's only registrar-facing tool | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:04314fb25dd9…`) | 0 |
| **Pronote** (Index Éducation) **+ ÉcoleDirecte + Skolengo** | 🇫🇷 Between them, essentially the whole French K-12 parent/student portal market | https://github.com/jujukingg/edu-mcp — 🟢 **the only row in this file that reaches a NATIONAL market rather than a school or a vendor**: three back ends behind one MCP server, published on PyPI, bilingual docs | 🟢 **MIT — byte-read** (`1,080 B`, `sha256:2ede3d997023…`) | 0 |
| **Librus Synergia** | 🇵🇱 The dominant Polish K-12 school register | https://github.com/ljarochowski/librus-mcp — 🟢 **the tier's only HEXAGONAL implementation**: `domain/` (`Child`, `Grade`, `Homework`, `CalendarEvent`), `ports/`, `adapters/`, so the Librus scraper is a swappable adapter and the domain model ports to every other country here | 🟢 **MIT — byte-read** (`1,079 B`, `sha256:be00e61b6328…`) | 0 |
| **Magister** (Iddink Group) | 🇳🇱 The dominant Dutch K-12 school portal | https://github.com/israelroldan/unofficial-magister-mcp — schedules, drop-off and pick-up times; names its own non-affiliation in the README | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:bd7dc91514e6…`) | 6 |
| **Blackboard Learn Classic 3900** | 🇨🇳 CUHK-Shenzhen (`bb.cuhk.edu.cn`); Blackboard Classic remains widely run across APAC higher education | https://github.com/changshenhan/bb-mcp — `9` tools, headless, 🔴 **WRITE-CAPABLE (submits homework)**, ships its own academic-integrity boundary in prose | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:aec9afda396f…`) | 4 |
| **FAM student portal** (Faculdade de Americana) | 🇧🇷 One private São Paulo institution; the shape is the LATAM norm — server-rendered, no API | https://github.com/Petri-Hub/fam-mcp — read-only, signs in as the student, returns typed JSON; answers *"what is due this week?"* across assignments, exams, forums AND invoices | 🟢 **MIT — byte-read** (`1,065 B`, `sha256:a659ef421023…`) | 4 |
| **SIGA** (Centro Paula Souza) | 🇧🇷 The academic system of São Paulo state's Fatec and Etec technical network — a PUBLIC system at state scale | https://github.com/KaioBorgesDev/siga-mcp — exposes academic data over MCP | 🔴 **NO LICENCE FILE — byte-probe returned nothing on `main` or `master`.** 🔴 **Not build-safe. The largest institutional footprint in this table and its only open surface cannot be used** | 0 |
| **Ellucian Banner Student Self-Service** | 🇺🇸🇨🇦 One of the two dominant North American higher-ed SIS products | https://github.com/Jayb1u3/andrews-ssb-mcp — a single-campus MCP server against Andrews University's SSB | 🔴 **NO LICENCE FILE.** 🔴 **Not build-safe — and at `4 KB` it is a sketch, so it is shelved as EVIDENCE that the Banner seam is being probed, not as a component** | 0 |

## The vendor-platform tier with an OPEN template catalogue — added `p825` (2 rows)

🟢 **Thirtieth pass (`p825`, 2026-11-15): `2` rows added (`120` → `122`), and they are a platform
SHAPE this page has not carried.** 🔵 **Every platform above is open-source software an institution
runs. These two are the inverse: a CLOSED, hosted vendor platform whose agent templates are
published openly under MIT — so the customisation surface is public while the runtime is not.**

🔴 **Why that shape matters commercially, and why it belongs on this page rather than in
`agents/top.md` alone.** `T86` found `74` MIT education agents under one vendor brand; `T89`
established that the framework beneath them is MIT and installable but wheel-only with an empty
source repository. 🟢 **The consequence for an engagement: the catalogue is a free, detailed map of
what a well-resourced vendor believes the `173` buyable education workflows ARE — written as
specifications with acceptance tests — and reading it costs nothing even if you never touch the
platform.** 🟡 **Treat it as competitive intelligence that happens to be MIT-licensed, which is
`P61`'s whole argument.**

| Platform | What institutions run it | Agent surface found this pass | License | Risk posture |
|---|---|---|---|---|
| **AGENTIC STAR** (SoftBank, 🇯🇵) | 🔴 **Not institution-run — a hosted commercial agent platform**, developer docs at `developers.fd.agenticstar.tm.softbank.jp`, homepage `agenticstar.io`. 🟢 Its runtime SDKs `agenticstar-agentcore` (`1.0.3`) and `agenticstar-platform` (`3.3.0`, `80` releases) are public on PyPI and MIT by their wheel metadata | 🟢 **`74` MIT education agent templates, `54` catalogue ids `EDU-C2-004`…`EDU-C2-173`** — reference row [`sbdnakashima/agentic-star-iep-section-drafting-agent`](https://github.com/sbdnakashima/agentic-star-iep-section-drafting-agent), `EDU-C2-028`, byte-read MIT (`1,074 B`, HEAD `71c442ebd88e`) | 🟢 **MIT** (templates and both SDKs, all byte- or metadata-verified) | 🟡 **Adopt the SPECS, not the runtime.** 🔴 Templates raise `PlatformRequired` at graph compile without a SoftBank deployment; all `74` are `0★`, unmaintained since October; the framework's advertised source repo has **zero commits** (`T89`); hard `==` pins on `langgraph`/`langchain`/`fastapi`. 🟢 **Tests run without the platform — harvest per `P61`** |
| **AgentCore graph scaffold** (the catalogue's shared architecture) | 🔵 Not a product — the uniform structure under all `74` templates: `config/agent.yaml` manifest (`required_trust_level`, declared secrets), `src/graph/`, `src/nodes/`, `src/schemas/state.py`, `docs/02_design.md`, `docs/03_test_spec.md`, `tests/proof_of_boundary/` | 🟢 Domain nodes differ completely between ids — byte-compared across three repositories this pass: `iep_section_generator`/`regulatory_compliance` vs `affected_material_analysis`/`stakeholder_mapping` vs `bloom_level`/`difficulty_score`. Reference row [`haidang024/agentic-star-education-curriculum-change-impact-briefing-agent`](https://github.com/haidang024/agentic-star-education-curriculum-change-impact-briefing-agent) (`EDU-C2-046`, `45` files) | 🟢 **MIT** (`1,067 B`, `sha256:b22b7ca45c04…`, HEAD `ae3eea9ac056`) | 🟢 **This is the reusable asset.** 🔵 One scaffold, `54` real domain implementations — so a studio gets a uniform, inspectable architecture across `54` education workflows instead of `54` unrelated codebases. 🔴 The scaffold's base class ships only in the binary wheel; re-implement on LangGraph (now on `repos/foundations.md`) |

## Education vertical platforms — 147 rows

### Filed by `p834` (2026-11-15) — `5` rows: the EXAMINATION-PLATFORM vertical, and the two AGPL rows are the traction leaders

🔴 **This shelf has carried LMS, SIS, AAC, MOOC and measurement platforms for thirty-eight passes
and has never carried an EXAMINATION platform**, which is the system a school actually runs when it
assesses anybody. 🟢 **The vertical exists, it is large (`在线考试系统` → `1,766` repositories), and
its traction leaders are copyleft.**

🔵 **Risk posture stated per row rather than once: `3` rows are build-safe (MIT / Apache-2.0),
`2` are AGPL-3.0 and are filed as REFERENCE platforms a studio reads and never links against.**
🟢 **All five byte-read `2026-11-15` on the DEFAULT branch.**

| Platform | Repo | Licence | Stars | What it is |
|---|---|---|---|---|
| 魔课考试系统 (mokexamsys) | https://github.com/xhgzs1314/mokexamsys | 🟢 **MIT — byte-read** (`1,072 B`, `sha256:876b0fd6f66a…`, `master/LICENSE` [DEFAULT], refs=[`master`]) | 0 | **Region: APAC.** 🟢 **New this pass (`p834`) — the most COMPLETE build-safe examination platform found in any language, and the row that flips this base's PROCTORING nil.** One self-hosted PHP + MySQL deployment covering the whole loop: teacher authoring → student sitting → **live invigilation** → automatic AND manual marking → result publication → electronic certificate issue. `24.8 MB`, pushed `2026-11-07`. 🔴 **`0★`.** 🔵 **`T118` is the point: this base declared proctoring a nil and held that nil for passes, because the nil was declared in English. The supply was always there, written in Chinese, under MIT.** |
| smart-exam-system (智慧在线考试) | https://github.com/Quanda666/smart-exam-system | 🟢 **MIT — byte-read** (`1,114 B`, `sha256:4a4252b5f68b…`, `main/LICENSE` [DEFAULT], refs=[`main`]) | 1 | **Region: APAC.** 🟢 **New this pass (`p834`) — the ANTI-CHEAT AUDIT-LOG row.** Vue 3 + Spring Boot + MySQL across three consoles, with question bank, paper, sitting, marking and result analysis — and a 防作弊日志, an append-only anti-cheat event log. 🔵 **Filed for the log rather than the detection: an evidence trail a human can adjudicate is defensible under every assessment regime in this base's policy matrix, whereas an automatic cheating VERDICT is a high-risk decision about a learner under EU AI Act Annex III point `3`.** 🔴 **That distinction is the whole sellable difference and `P74` carries it.** Pushed `2026-06-24` |
| ExamOnline (HarmonyOS) | https://github.com/deceiver-djw/ExamOnline | 🟢 **Apache-2.0 — byte-read** (`11,356 B`, `sha256:c5accbbd8546…`, `master/LICENSE` [DEFAULT], refs=[`master`]) | 0 | **Region: APAC.** 🟢 **New this pass (`p834`) — the only HarmonyOS-native education artefact on these shelves.** ArkTS/ArkUI front end over a Spring Boot back end: question bank, automatic paper assembly, sitting, anti-cheat monitoring, AI marking, publication. `30.5 MB`, pushed `2026-09-16`. 🔵 **Filed for the DEVICE axis: a China K-12 engagement increasingly means a domestic tablet estate, and this is the one row in the base that already targets that runtime.** 🔴 **`0★` — filed on platform coverage, not traction.** |
| xzs (学之思开源考试系统) | https://github.com/mindskip/xzs | 🔴 **AGPL-3.0 — byte-read** (`34,520 B`, `sha256:76a97c878c9c…`, `master/LICENSE` [DEFAULT], refs=[`master`]) | 3915 | **Region: APAC.** 🟢 **New this pass (`p834`) — the TRACTION LEADER of the Chinese examination vertical by two orders of magnitude** (`3,915★` against the MIT rows' `0`–`1★`). Spring Boot + Vue, student and admin consoles, question bank, exams, practice, wrong-answer book. Pushed `2026-11-12`. 🔴 **AGPL-3.0: a hosted derivative must publish its source. NOT build-safe for a proprietary delivery and it is filed as a REFERENCE platform only.** 🔵 **The pattern `T109` keeps producing: the most-starred thing in a vertical is the thing a studio may not ship, and the shippable rows are the unstarred ones beside it.** |
| SmartKBS | https://github.com/youufis/SmartKBS | 🔴 **AGPL-3.0 — byte-read** (`34,834 B`, `sha256:2086e7eae183…`, `master/LICENSE` [DEFAULT], refs=[`master` `release/7.4` … `release/8.1`]) | 91 | **Region: APAC.** 🟢 **New this pass (`p834`) — the most COMPLETE teaching platform found this pass, and the one with a real release train** (`master` plus `release/7.4` through `release/8.1`). General-subject AI teaching platform for primary, junior and senior secondary: question bank and intelligent paper assembly, examinations, practice, homework, **automatic marking**, and live classroom modes (闯关 / 抢答 / 抽问). `91★`, pushed `2026-11-15`. 🔴 **AGPL-3.0 — reference only, same posture as `xzs`.** 🔵 **Read for the classroom-interaction model: no build-safe row in this base implements timed whole-class question modes at all.** |

### Filed by `p828` (2026-11-15) — `1` row, and it is the only PERMISSIVE LMS on this shelf

🔴 **Every other LMS here is GPL or AGPL** (Moodle, Open edX, Canvas, Chamilo, Frappe LMS), which
means a derived platform is copyleft. 🟢 **An MIT, AI-native LMS can be forked and shipped
commercially — a strategically different option, not merely another row.**

| Platform | Repo | Licence | Stars | What it is |
|---|---|---|---|---|
| mentingo | https://github.com/Selleo/mentingo | 🟢 **MIT — byte-read** (`1,062 B`, `sha256:ceb97717de1f…`) | 109 | **Global.** 🟢 **New this pass (`p828`) — an AI-NATIVE LMS, MIT, `109★` / `30` forks** (🇵🇱 Selleo). Self-hosted, positioned against Moodle, Docebo, TalentLMS, Thinkific, Teachable and Open edX, with an AI Mentor and role-play built in. 🔵 **Every other LMS on this shelf is GPL/AGPL. A permissively-licensed, AI-native LMS is rare enough to be a strategic option on its own: it can be forked and shipped commercially, which Moodle and Open edX cannot.** |


🟢 **Twenty-sixth pass (`p821`, 2026-11-15): `1` row added — `111` → `112`.** 🔴 **NOT gate-confirmed:
`make hooks` was refused by the sandbox classifier for a **FOURTH** consecutive pass, so the figure
is the carried `111` plus one row, stated as a DELTA rather than as a fresh absolute recount.**
🔵 **`ACTION p821-B` carries the real-gate run forward.**

🟢 **The mandated vertical leg ran in full and returned the same eight platforms as `p820` —
`moodle`, `edx-platform`, `OpenEduCat`, `frappe/lms`, `OpenOLAT`, `rosariosis`, `openSIS-Classic`,
`chamilo-lms` — all `8` already on this page, a `36`th consecutive nil on that leg.** 🟢 **The row
below came from a different channel entirely: recency-ranked (`sort=updated`, `created:` window,
**no star floor**), which is the setting this base had never run (`T70`).**

🔵 **Why this row belongs in `verticals/` and not in `agents/`:** it ships no agent. It ships the
thing an agent in this vertical is always missing — a **national curriculum encoded as addressable
content**, with a stable short code per learning outcome. That is the substrate, not the product.

| Platform | Repo | Licence | Stars | What it is |
|---|---|---|---|---|
| EduTrace (curriculum layer) | https://github.com/mohanvd/edutraceapp | 🟢 **MIT** (`raw.githubusercontent.com/mohanvd/edutraceapp/main/LICENSE`, `1,065 B`, `sha256:88765a78…`, first line `MIT License`) | 28 | **Region: EMEA.** 🟢 **New this pass (`p821`) — the first 🇪🇬 Egypt-placed platform in this file, and placement rests on the repository's OWN topic string `egypt` plus the README's *"Open-source STEM curriculum viewer for Egyptian high school students"*, not on an inference.** The open-source curriculum layer of the EduTrace platform for Egyptian **STEM Grades 10–11**: every Learning Outcome, the MDX lesson content, and an **LO short-code routing system** that resolves a path like `/PH.1.01` to the outcome it names. 🔵 **The short code is the reusable asset.** It gives an agent a stable, curriculum-native address for *"what is this student supposed to be able to do"* — the same join `mawta` makes against Peru's `CNEB` and `k12-qbank` makes against 人教版 (`T70`). Full MDX rendering with KaTeX and highlighted code, plus iframe-friendly `/embed/[code]` lesson views, which is how it mounts inside an LMS without the LMS adopting it. Next.js 15 + TypeScript 5.9, created `2026-05-23`, pushed `2026-11-12`. ⚠️ `28★`, single maintainer; the content is Grades 10–11 only. |

🟢 **Twenty-fifth pass (`p820`, 2026-11-15): `0` rows added, and `111` is CONFIRMED again — this
time by a SECOND, independently written reimplementation of the gate.** Gate output for this file:
`tables=20 rows=113 distinct=111 graded=111 claimed=111 ragged=0 nolink=0 dupes=2` → **GREEN**.
🔴 **`ingest/derive-counts.py` was refused by the sandbox classifier for a THIRD consecutive pass.**
🟢 **`p820`'s substitute was written from the gate's source independently of `p819`'s and
reproduced all five of `p819`'s figures exactly before this pass changed anything.**
🔵 **`ACTION p820-B` carries the real-gate run forward.**

🔴 **`0` platform rows is a MEASUREMENT with a denominator:** the mandated vertical leg returned
`moodle`, `edx-platform`, `OpenEduCat`, `frappe/lms`, `OpenOLAT`, `rosariosis`, `openSIS-Classic`
and `chamilo-lms`, and **all `8` are already on this page.** 🔵 **Disposition table in
`repos/trending.md`.**

🟢 **What DID move for this file is regulatory, and it changes how one of these platforms may be
configured in one country.** `T67`: under `Parecer CNE/CP nº 15/2026` a Brazilian basic-education
deployment must bar generative and conversational AI through `5º ano` entirely. 🔴 **That is not a
platform setting on any system on this page — it is a routing decision above the platform**, which
is why it is written as `P50` rather than as a note in a row.

🟢 **Twenty-fourth pass (`p819`, 2026-11-15): `0` rows added, and the figure above is CONFIRMED by a
running gate rather than by a hand count.** Gate output for this file:
`tables=20 rows=113 distinct=111 graded=111 claimed=111 ragged=0 nolink=0 dupes=2` → **GREEN**.

🟡 **How it was run, stated because it is not the repository's own gate.**
`ingest/derive-counts.py` was refused by the sandbox classifier again this pass, exactly as in
`p818`. 🟢 **It was therefore REIMPLEMENTED from its source in a session scratchpad** — same column-
header signatures, same declared exclusions, same `'## <name> — N rows'` singleton claim rule, same
distinct-subject grading for multi-signature files. 🟢 **It reproduces four of `p818`'s five inline
figures exactly, including this file's `111`**, which is the evidence that the substitute is
faithful. 🔴 **It refutes `p818` on the fifth: the agent shelf held `166`, not `183`, because
`p818`'s inline rule excluded the rejection tables but not the COPYLEFT table (`17` rows). See
`T62` and `agents/top.md`.** 🔴 **`ACTION p819-B` carries the real-gate run forward.**

🔴 **`0` rows is a MEASUREMENT this pass, not an unrun leg.** `14` distinct star-ranked
`gh api search/repositories` queries returned `54` results; `52` were already held in this base's
`5,390`-address ledger and the `2` new ones are APPLICATIONS, shelved in `agents/top.md` and wired
in `P49`. 🟢 **Written up as `T63`: this channel has saturated and now returns a flow rather than a
backlog, so it should keep running every pass but can no longer be a pass's primary leg.**
🔵 **The layers added since `p813` were all found by naming an institutional tier first and querying
second; none of them came off a star ranking.**

🟢 **Twentieth pass (`p815`, 2026-11-15): six platform rows added under a new tier — the
ASSESSMENT ENGINE — and the figure above is the gate's output.** 🔵 **The gate caught the draft
again: it read `86` and `ingest/derive-counts.py` returned *"RED heading claims 86, the file
holds 92"* before the commit. Gate output after insertion:
`tables=17 rows=94 distinct=92 graded=92 claimed=92 ragged=0 nolink=0 dupes=2`.**


🟢 **Eighteenth pass (`p813`, 2026-11-13): this file is gradeable for the first time since
`p718`,** for the reason set out in `repos/foundations.md` — `ACTION p811-A` option (a),
implemented with uncounted-table detection. Gate output:
`tables=15 rows=83 distinct=81 graded=81 claimed=81 ragged=0 nolink=0`.

🔵 **And it earned its keep inside the hour it was written.** The first draft of this heading
claimed `70` — the pre-insertion figure — and the gate rejected it: *"RED heading claims 70, the
file holds 81."* 🟢 **That is precisely the drift `compose/patterns.md` has had to confess four
times in prose. It is now caught by a program instead of by the next pass's reader.**

## 🟢 Twenty-ninth pass (`p824`, 2026-11-15) — `4` new rows, and they END this file's standing claim that the education platform tier is copyleft

🟢 **`4` platform rows added (`116` → `120`) — the first non-nil on this file in two passes, and
gate-confirmed: `python3 ingest/derive-counts.py` returns GREEN.**

🔴 **The mandated vertical leg nilled for a `37`th consecutive time.** Run in full
(`open source platform education ERP CRM MIT Apache student information system`): it returned
`OpenEduCat` (LGPL, built on Odoo) and `eduTrac SIS` (GPL-3.0) and nothing else — both already on
this page, both copyleft, and the search summary itself concluded *"the results didn't cover MIT-
or Apache-licensed education ERP or CRM options."* 🟢 **That conclusion is FALSE, and this pass
disproves it from the index rather than from an opinion.**

### 🟢 The finding (`T85`): the permissive platform tier EXISTS — it is simply not where the star mass is

🟢 **One query, run at `sort=stars` with a `pushed:>2026-09-01` recency floor and no star floor:**

| Query | Total | What the top of the list is | What is underneath it |
|---|---|---|---|
| `school management system pushed:>2026-09-01` | **`4,840`** | 🔴 `frappe/education` `711★` `NOASSERTION`, `rosariosis` `654★` GPL-2.0, `Django-School-Management` `599★` NONE, `openSIS-Classic` `351★` NONE | 🟢 **`skuul` `481★` MIT — fourth by stars, first by grant** |
| `student information system pushed:>2026-06-01` | **`4,137`** | 🔴 `rosariosis` GPL-2.0, `openSIS-Classic` NONE | 🟢 **`etsis` `46★` MIT, `SIMS` `29★` Apache-2.0** |
| `open source learning management system pushed:>2026-09-01` | `37` | 🔴 `frappe/lms` `3,423★` AGPL-3.0, `tadreeblms` `35★` AGPL-3.0 | 🟢 **`tutors-mono-repo` `5★` MIT** |

🔵 **The copyleft reading was a STAR-RANK artefact.** Every incumbent this file has named since
`p805` is copyleft or unlicensed and sits in the top four of its query; the permissive tier sits
immediately below it, is actively maintained — three of the four rows below were pushed on the day
of this pass — and had never been read because no leg ever looked past the ceiling.

🟢 **And `T59`'s vintage rule GENERALISES beyond the library tier where it was published.** `T59`
found research-library platforms splitting `1999–2007` GPL / `2013-onward` permissive. The four
rows below were created `2015`, `2020`, `2021` and `2026` — **all post-2013, all permissive** —
while the copyleft incumbents above them were created `2013` (`rosariosis`), `2018`
(`openSIS-Classic`), `2019` (`Django-School-Management`) and `2021–2022` (`frappe/*`, AGPL by house
policy rather than by vintage). 🔵 **So the rule is: outside a vendor with a house licence policy,
an education platform's grant is predicted better by its birth year than by its category.**

| Platform | Repo | Licence | Stars | What it is |
|---|---|---|---|---|
| skuul | https://github.com/yungifez/skuul | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:91e9aaa8…`, holder `Ebuka Ifezue`, 2022) | 481 | 🟢 **New this pass (`p824`) — the highest-starred PERMISSIVE education platform in this file, and the row that ends the copyleft claim.** *"A multi school management system"* — multi-tenant by design, Laravel, `20 MB`, created `2021-11-03`, pushed `2026-11-15`. 🔵 **Multi-tenancy is the property that matters commercially: `P55`'s multi-tenant campus connector needs a host that already models "many schools, one deployment", and every copyleft incumbent above it models one institution per install.** 🔵 **It is also the first African-authored platform on this page.** 🔴 **What it is NOT: a standards client** — no OneRoster, no LTI, no Ed-Fi surface found; integration work is a build, not a configuration |
| etSIS | https://github.com/nomadicjosh/etsis | 🟢 **MIT — byte-read** (`LICENSE.md`, `1,113 B`, `sha256:8d66d7d7…`, holder `Joshua Parker`, 2022) | 46 | 🟢 **New this pass (`p824`) — the only permissively licensed HIGHER-EDUCATION SIS this base has found in twenty-nine passes.** Self-described as *"the most advanced open source student information system for higher education"*; `37 MB`, created `2015-08-01`, pushed `2026-11-15`. 🔵 **Eleven years of continuous development is the signal, not the `46★`: this file's higher-ed SIS tier has been `RosarioSIS` (GPL-2.0, K-12-shaped) and `openSIS` (no licence) for twenty-nine passes, and `P8` had to be scoped around both.** 🟢 **`P8` now has a permissive host for the first time** 🔴 PHP; verify the upgrade path before quoting a migration |
| SIMS (Student Information Management System) | https://github.com/bcgov/SIMS | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:58d1e17f…`, stock text) | 29 | 🟢 **New this pass (`p824`) — a GOVERNMENT-OPERATED platform under a patent-granting licence, and the only North American platform row `p824` produced.** Post-secondary **student financial aid** for the Government of British Columbia 🇨🇦, `54 MB`, pushed `2026-11-13`. 🔵 **Fourth instance of the `p810` Ed-Fi / `p818` Riksarkivet pattern — the body that OPERATES the record ships the code — and the first one in North America that is an operational system rather than a standard.** 🔵 **Financial aid is a tier no other row in this file covers, and it is the one education workflow where an agent's error is a money error: treat it as `P14`-registry work with a human decision gate, never as an advisory chatbot** |
| Tutors | https://github.com/tutors-sdk/tutors-mono-repo | 🟢 **MIT — byte-read** (`1,082 B`, `sha256:f4cbe9e7…`, holder `Tutors Open Source Project`, 2022) | 5 | 🟢 **New this pass (`p824`) — the newest-generation LMS on this page and the only one built as a COURSE READER rather than as an administrative system.** Svelte 5 + SvelteKit + TypeScript, `19 MB`, created `2026-07-27`, pushed `2026-11-15`. 🔵 **The course-reader shape is the one an agent composes with most cheaply: content is addressable markdown rather than rows behind an institutional login, which is the whole constraint `T77` found on the Moodle/Canvas tier.** 🔴 `5★` and four months old — a technology bet, not an incumbent replacement |

🔴 **Named and NOT shelved, with the reason.** [`frappe/education`](https://github.com/frappe/education)
(`711★`) and [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) (`57★`) both report
`NOASSERTION`; per `T52` that means the matcher failed and the bytes must decide, and per `T81` the
bytes can say three different things. Neither was byte-read this pass and neither is shelved on the
field alone. 🔴 [`TareqMonwer/Django-School-Management`](https://github.com/TareqMonwer/Django-School-Management)
(`599★`) and [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) (`351★`) carry no
licence field at all — `openSIS` is already recorded on this page as the unlicensed incumbent.

## 🔴 Twenty-eighth pass (`p823`, 2026-11-15) — `0` new platform rows, and the measurement that explains why: the integration population targets CLOSED systems

🔴 **`0` platform rows added this pass. `116` unchanged, gate-confirmed
(`verticals/solutions.md shelf: tables=22 rows=118 distinct=116 graded=116 claimed=116`).**
🟢 **This is a MEASUREMENT with its denominator published, not an unrun leg.**

🟢 **`p823`'s discovery leg was the richest in this base's history — `21` build-safe agent rows —
and almost none of it landed here. The reason is the finding.** `T77` identified a population of
`20`+ institution-pinned LMS agents. This file asks a different question of each one: *what system
does it integrate with, and is that system open-source and shelvable?*

**The systems named by the `p823` population, graded for this file:**

| System | Institution / region | Open source? | Already shelved? |
|---|---|---|---|
| Moodle | many, all regions | 🟢 yes (GPL-3.0) | 🟢 yes — the host-systems tier |
| Canvas | many, North America | 🟢 yes (AGPL-3.0 open edition) | 🟢 yes |
| Artemis | TUM 🇩🇪 | 🟢 **yes — MIT, `832★`, pushed `2026-11-15`** | 🟢 **yes, already on this shelf** |
| 🔴 Omnivox | Québec CEGEPs 🇨🇦 | 🔴 **no — proprietary (Skytech)** | ❌ no repo to shelf |
| 🔴 Brightspace / Valence | many, North America + APAC | 🔴 **no — proprietary (D2L)** | ❌ no repo to shelf |
| 🔴 Ed | Monash 🇦🇺 and AU/US universities | 🔴 **no — proprietary** | ❌ no repo to shelf |
| 🔴 CIS | NORDAKADEMIE 🇩🇪 | 🔴 **no — in-house campus system** | ❌ no repo to shelf |
| 🔴 БРС / СДО / Пульс | RTU MIREA 🇷🇺 | 🔴 **no — in-house** | ❌ no repo to shelf |
| 🔴 教学云 | BUPT 🇨🇳 | 🔴 **no — in-house** | ❌ no repo to shelf |
| 🔴 ENT/CAS | Université de Montpellier 🇫🇷 | 🟡 CAS protocol is open; the ENT deployment is not a product | ❌ nothing distinct to shelf |

🔵 **So the platform tier did not grow because `6` of the `10` systems driving this pass's agent
supply have no source to shelve at all, and the `3` that do were already here.**

🟢 **And that is commercially the most useful thing this file can say this pass.** This base's
standing advice is to build on the open platform tier. **`T77` shows where that advice stops:** the
moment an engagement reaches a real campus, the integration surface is a mix of one open LMS and
several closed in-house or vendor portals, and **no amount of open-source platform selection
removes the closed half.** The connector fleet in `P55` is priced accordingly — it is adapter
maintenance against systems whose owners can restyle them without notice, which is exactly why the
per-campus volunteer repos in `T77` cannot be the long-term answer.

🔴 **Open gap, carried forward:** this file still has **no row for a Québec/CEGEP-tier or Nordic
in-house campus portal**, because open equivalents were searched for and not found. 🟢 **An informed
nil, re-testable: the `p824` query is `student portal` / `campus portal` with no star floor, ranked
by recency, restricted to the SYSTEM layer rather than the agent layer** — the setting that broke
`T31` and `T77` open.

## 🟢 Twenty-seventh pass (`p822`, 2026-11-15) — the platform tier that provisions the LAB, and the first institution-authored platform in this file archived by Software Heritage

🔵 **Twenty-six passes have asked what system a learner logs into, reads in, is graded by and is
judged by. `p822` asks what system RUNS THE EXERCISE** — the sandbox a student is given when the
course is practical rather than discursive. 🔴 **This file had no row for that tier at all**, which
is a gap with a cost: every vocational, IT and engineering engagement needs it, and the default
answer in procurement is a per-seat cloud lab product.

🟢 **The answer found is `MyDocker`, and three things make it unusual on this shelf.** It is
authored by an INSTITUTION rather than a vendor or an individual — CentraleSupélec, whose own
README calls it *"CentraleSupélec's virtual lab platform"*. It is **MIT**, where this file's
platform tier is overwhelmingly copyleft (`Moodle` GPL-3.0, `Open edX` AGPL-3.0, `OpenEduCat`
LGPL-3.0). And it is archived in **Software Heritage** with a `swh:1:dir:` identifier in its README
badge — the first row in this file carrying an independent archival guarantee, which is a real
procurement argument when the client asks what happens if the upstream disappears.

🟢 **Three further platform rows, each placed on a quoted locative rather than an inferred one.**
`csm_web` is UC Berkeley's Computer Science Mentors running their own section signup and attendance
— the North American instance of the university-self-management pattern `T34` found in LATAM, and
evidence it is a SHAPE rather than a regional workaround. `schoolz` is a US district parent portal
naming its district in prose (*"Cherry Hill Public Schools"*). `Plan ₿ Network` is a community LMS
whose interesting property is architectural, not topical: **the platform and the educational
CONTENT live in two separate repositories**, which is exactly the split `P43` tells a studio to
impose on a client who wants courseware without forking an LMS.

🔵 **Licence byte-hash, used as `T37` intends.** `schoolz`'s Apache-2.0 payload hashes to
`sha256:c71d239df917…` — byte-identical to the payload already recorded on this base's
`Ed-Fi-SDK-for-AI-Assistants` row. Same stock text, no holder line, two unrelated projects:
the hash de-duplicates a licence, it does not imply a lineage.

| Platform | Repo | Licence | Stars | What it is |
|---|---|---|---|---|
| MyDocker | https://github.com/CentraleSupelec/mydocker | 🟢 **MIT — byte-read** (`LICENSE.md`, `1,081 B`, `sha256:394ccfb071f6…`, stock text, holder `2023-prese…`) | 16 | 🟢 **New this pass (`p822`), and the first VIRTUAL LAB row in this file.** *"A scalable virtual labs provider based on Docker with simple integration to your LMS"* — hundreds of Docker-based lab environments launched directly from Moodle, scheduled on cloud resources, with lecturers updating lab images without an IT ticket and student data kept off third-party infrastructure. `37,653 KB` of TypeScript, pushed `2026-11-10`, Software Heritage archived. 🔵 **EMEA, placed on the author: CentraleSupélec. This is the component an AI skills-training offer needs and the one studios usually buy** |
| CSM Scheduler (`csm_web`) | https://github.com/csmberkeley/csm_web | 🟢 **MIT — byte-read** (`1,081 B`, `sha256:53e957827340…`, stock text, holder `2019 Computer Scie…`) | 20 | 🟢 **New this pass (`p822`).** Section signup and attendance for UC Berkeley's Computer Science Mentors — Django + Python `3.9`, React front end, Postgres, Docker compose, pushed `2026-11-10` after seven years. 🔵 **North America, placed on a quoted locative (*"Berkeley"*).** 🔵 **Its value here is comparative: `T34` found LATAM universities building their own self-management systems and read it as a regional adaptation. The same shape at Berkeley says it is a UNIVERSITY shape, and a studio can reuse the LATAM patterns on a North American campus** |
| Plan ₿ Network | https://github.com/PlanB-Network/bitcoin-learning-management-system | 🟢 **MIT — byte-read** (`1,076 B`, `sha256:0f6ce0948634…`, stock text, holder `2023-2026 Pla…`) | 28 | 🟢 **New this pass (`p822`) — a permissively licensed, running LMS, which this tier is short of.** A Turbo monorepo with Docker development, community-driven, *"free, open-source"*. 🟢 **The architecture is the transferable part: the PLATFORM is this repository and the educational CONTENT is a separate one (`bitcoin-educational-content`), so courseware is versioned and governed apart from the system that serves it — the separation `P43` prescribes, already implemented.** 🔵 **Placed Global: no locative statement in the README, and the subject matter is not a location** |
| schoolz | https://github.com/sitenaut/schoolz | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:c71d239df917…`, stock text, no holder) | 1 | 🟢 **New this pass (`p822`).** *"One public, bookmarkable page per school"* — it consolidates the school-day information a district scatters across sites, needs no account for almost everything, and is explicitly *"built to be handed to a district"*, data model, scans and tests included. 🔵 **North America, placed on a quoted locative: Cherry Hill Public Schools.** 🔴 **`1★` and unproven as a product — carried for the DELIVERY POSTURE, which is the one most civic-edtech pilots get wrong: public by default, login only for personalisation** |

## 🟢 Twenty-third pass (`p818`, 2026-11-15) — the RESEARCH side of the institution, and the first tier in this file where the permissive option is the BETTER product rather than the fallback

🔴 **Twenty-two passes of this file named the systems an institution runs to TEACH. Not one named
a system it runs to do RESEARCH** — and in a university the library services platform, the
institutional repository and the journal platform carry budgets comparable to the LMS.

🟢 **The tier's licence profile is the finding (`T59`), and it is the most useful one this file has
produced for a procurement conversation.** 🔴 **Every platform in this tier built between 1999 and
2007 is GPL: Koha, OJS, VuFind, Omeka S, EPrints.** 🟢 **Every platform built from 2013 onward is
permissive: FOLIO (Apache-2.0), InvenioRDM (MIT, CERN), Samvera Hyrax (Apache-2.0), DOAJ
(Apache-2.0), ROR (MIT), SciELO (BSD-2).** 🔵 **In every other tier in this file the permissive row
was a consolation — a smaller, younger, less-deployed alternative to the copyleft incumbent. Here
the permissive rows are FOLIO and InvenioRDM, which are the modern products, and the copyleft rows
are the ones being migrated away from.**

🔴 **Count note: `ingest/derive-counts.py` could not be executed this pass — the sandbox classifier
refused the repository's Python gates — so the heading figure was re-derived inline**
(`rows=113 distinct=111` after insertion; `104`/`102` before, the two repeats being this file's
deliberate cross-tier entries — `frappe/education` and `frappe/lms`). 🔴 **Degraded channel,
flagged.** 🟢 **And the inline derivation earned its keep exactly as the gate does: this heading's
first draft read `110` because the pass counted its own new rows as eight when it had written
nine. Re-derived before commit, not after.**

| Platform | Repo | Licence | Stars | What it is |
|---|---|---|---|---|
| FOLIO (platform-complete) | https://github.com/folio-org/platform-complete | 🟢 **Apache-2.0** (`11,356 B`, `sha256:43070e2d…`) | 15 | **Region: Global.** 🟢 **New this pass (`p818`) — the permissive library services platform, and the answer to the Koha licence problem this file has carried since `p814`.** Built by a consortium of academic libraries with EBSCO and Index Data expressly to end LSP lock-in. 🔵 **Microservice architecture behind the `okapi` gateway, so an AI module is a FOLIO module rather than a fork — the cleanest extension story of any platform in this file** |
| InvenioRDM | https://github.com/inveniosoftware/invenio-app-rdm | 🟢 **MIT** (`1,243 B`, `sha256:ccb5c2a3…`, holder `CERN`) | 187 | **Region: EMEA.** 🟢 **New this pass (`p818`) — the row that should change what this base recommends for an institutional repository.** The platform CERN runs **Zenodo** on. 🔵 **MIT, maintained, turnkey, with DOI minting and research-data management built in. Propose this where a client would otherwise fork DSpace or keep EPrints alive** 🟢 Pushed `2026-11-13` |
| Samvera Hyrax | https://github.com/samvera/hyrax | 🟢 **Apache-2.0** (`11,564 B`, `sha256:40c35ac3…`) | 201 | **Region: North America.** 🟢 **New this pass (`p818`).** Repository front-end for the Samvera community, deployed at large North American research libraries. 🔴 **Rails plus Fedora: the highest integration cost in this tier.** 🟢 **Shelved because the institutions running it are exactly the ones with research-office AI budgets** |
| SciELO OPAC | https://github.com/scieloorg/opac | 🟢 **BSD-2-Clause** (`1,292 B`, `sha256:493da013…`, holder `SciELO ORG`) | 10 | **Region: LATAM.** 🟢 **New this pass (`p818`) — the first LATAM-OPERATED platform in this file, and it is permissive (`T58`).** The public catalogue of the SciELO network: Brazil, Chile, Colombia, Mexico, Argentina, Peru, Cuba, Uruguay, Bolivia, Costa Rica, Paraguay, Ecuador, Venezuela, plus Portugal, Spain and South Africa. 🔴 **Operated centrally by BIREME/FAPESP rather than installed per-institution, so the buyer is the NETWORK — a different sale from every other row in this file, and a far larger one** |
| SciELO Manager | https://github.com/scieloorg/scielo-manager | 🟢 **BSD-2-Clause** (`1,328 B`, `sha256:c0182a8e…`, holder `SciELO`) | 16 | **Region: LATAM.** 🟢 **New this pass (`p818`).** Journal and article cataloguing for the network, offered in a SaaS model. 🔵 **The editorial workflow surface — where an AI assist for metadata, language and standards conformance would actually sit** 🔴 Pushed `2026-03-03` |
| DOAJ | https://github.com/DOAJ/doaj | 🟢 **Apache-2.0** (`11,323 B`, `sha256:6dc0e068…`) | 67 | **Region: Global.** 🟢 **New this pass (`p818`).** The Directory of Open Access Journals application. 🔵 **A research office uses DOAJ membership to decide whether a publication counts toward an evaluation — so an agent reading it is answering a policy question, which is a different and better-funded job than search** 🟢 Pushed `2026-11-13` |
| VuFind | https://github.com/vufind-org/vufind | 🔴 **GPL-2.0** (`15,045 B`, `sha256:8f4b368d…`) | 307 | **Region: Global.** 🔴 **New this pass (`p818`), filed as a FLAG.** The most-deployed open-source discovery layer. 🔴 **GPL-2.0 — the one licence in this tier that is also incompatible with GPL-3.0-only code, which matters if it sits next to Koha extensions.** 🟢 **Do not propose it; it is here so a client already running it meets a correct reading** 🟢 Pushed `2026-11-13` |
| Omeka S | https://github.com/omeka/Omeka-S | 🔴 **GPL-3.0** (`35,146 B`, `sha256:c53a65c2…`) | 530 | **Region: Global.** 🔴 **New this pass (`p818`), filed as a FLAG.** Digital collections and exhibit publishing, heavily used in digital-humanities teaching. 🔵 **The platform most likely to be already running in a humanities faculty when an AI engagement begins** 🟢 Pushed `2026-11-13` |
| EPrints | https://github.com/eprints/eprints | 🔴 **GPL-3.0** (`32,421 B`, `sha256:37d3866d…`, `COPYING`) | 67 | **Region: EMEA.** 🔴 **New this pass (`p818`), filed as a WARNING.** The original institutional-repository platform (Southampton, 2000), still in production at UK and European institutions. 🔴 **Last pushed `2023-07-31` — unmaintained for over two years.** 🟢 **The migration proposal writes itself: EPrints → InvenioRDM, GPL-3.0 → MIT, abandoned → CERN-maintained, same job** |

## 🟢 Twenty-second pass (`p817`, 2026-11-15) — the platform tier that issues a record the learner CARRIES AWAY, and the identity layer every other tier in this file authenticates through

🔵 **Two tiers, and the second is an omission rather than a discovery.** 🟢 **The credential tier
issues something a third party can verify without calling the institution back — the only tier in
this file whose output outlives enrolment.** 🔴 **The identity tier is the one twenty-one passes
walked past: every LMS, SIS, LRS and portal already named in this file authenticates through it.**

| Platform | Repo | Licence | Stars | What it is |
|---|---|---|---|---|
| Apereo CAS | https://github.com/apereo/cas | 🟢 **Apache-2.0** (`11,358 B`, `sha256:cfc7749b…`) | 11399 | **Region: Global.** 🟢 **New this pass (`p817`) — the most-starred repository in this entire knowledge base, education or otherwise.** Enterprise SSO for higher education. 🔴 **That twenty-one passes never shelved it is the finding: this base harvested what agents TALK TO and skipped what every one of those systems TRUSTS.** 🔵 **On an engagement it answers the question that otherwise stalls agent projects — *how does the agent act as the user without holding the user's password* — and the institution is usually already running it** |
| uPortal | https://github.com/uPortal-Project/uPortal | 🟢 **Apache-2.0** (`11,359 B`, `sha256:5d7a4884…`) | 287 | **Region: Global.** 🟢 **New this pass (`p817`).** *“Enterprise open source portal built by and for the higher education community.”* Pushed `2026-11-14`. 🔵 **The surface a university puts in front of its systems — and the place staff and students will expect an agent to appear, rather than in a separate chat product** |
| DCC Admin Dashboard | https://github.com/digitalcredentials/dcc-admin-dashboard | 🟢 **MIT** (`1,094 B`, `sha256:0f6a5db4…`, holder `Massachusetts Institute of Technology`) | 12 | **Region: North America.** 🟢 **New this pass (`p817`) — the registrar's surface for verifiable credentials.** Upload, manage, issue, collect, notify. 🔵 **The piece that makes `P44` a procurement item rather than a demo: it matches a workflow a registrar already performs** |
| DCC VerifierPlus | https://github.com/digitalcredentials/verifier-plus | 🟢 **MIT** (`1,087 B`, `sha256:85569d7e…`) | 19 | **Region: North America.** 🟢 **New this pass (`p817`).** The relying-party surface — where an employer or institution checks a credential. 🔴 **Routinely under-budgeted: issuing is an afternoon, being trusted is the project** |
| Learner Credential Wallet | https://github.com/digitalcredentials/learner-credential-wallet | 🟢 **MIT** (`1,092 B`, `sha256:1032f65d…`, holder `Digital Credentials Consortium`) | n/a | **Region: North America.** 🟢 **New this pass (`p817`).** Cross-platform iOS/Android holder wallet. 🔴 **Stars `n/a` because the repository is ABSENT from the search index while live on raw — see `T55`. Cite this address, never the `91★` mirror the index returns** |
| Europass / European Learning Model | https://github.com/european-commission-empl/European-Learning-Model | 🔴 **EUPL-1.2 — reciprocal** (`13,865 B`, `sha256:6e5399ad…`) | 54 | **Region: EMEA.** 🔴 **New this pass (`p817`), filed as a WARNING.** The data model behind Europass Digital Credentials, from DG EMPL. 🔴 **ARCHIVED; last pushed `2024-02-14`.** 🟢 **Use as a conformance SPECIFICATION and implement with the MIT rows above — do not fork it (`T56`, `P44`)** |
| Learning Locker | https://github.com/LearningLocker/learninglocker | 🔴 **GPL-3.0** (`35,141 B`, `sha256:589ed823…`) | 587 | **Region: Global.** 🔴 **New this pass (`p817`), filed as a FLAG.** The most-starred LRS on this channel, last pushed `2024-05-30`. 🔴 **This base had shelved two of the same org's small MIT satellites at `p805` and skipped its flagship — because the flagship is where the copyleft is.** 🟢 **Do not propose it; it is here so a client already running it meets a correct licence reading** |

## 🟢 Twenty-first pass (`p816`, 2026-11-15) — the platform tier a learner opens WITHOUT being told to, and the first tier in this file where the permissive platform is a real alternative rather than a consolation

🔴 **This file has named `92` platforms across twenty passes and every one of them is procured —
an LMS, an SIS, an ERP, a parent portal, an exam lockdown client, a national school portal. A
procurement decision is made by an institution, so every row so far has had an institutional buyer.**
🟢 **The retention tier has no buyer. A learner installs it, and that is the whole adoption
funnel.**

🔵 **Why that is a commercial observation and not a curiosity:** the retention platform is the
only education system in this base with DAILY voluntary engagement, and an institution that wants
retention evidence about its own cohort cannot get it from a system it does not run. 🟢 **That gap
is `P42`, and it is the reason this tier is worth naming even though no institution buys any row in it.**

🔴 **The incumbent is `ankitects/anki` (`32,804★`, AGPL-3.0-or-later with per-file exceptions —
already shelved in this file, and six licences rather than two per `ACTION AH`).** 🟢 **The three
rows below are the alternatives, and unlike `p815`'s assessment tier — where the permissive option
sat at a fifth of the incumbent's attention — two of these are permissive and in the same order of
magnitude as each other.**

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| **Memo** — programming-oriented spaced-repetition app (Flutter, iOS + Android) | https://github.com/olmps/memo | 🟢 **BSD-3-Clause — byte-read** (`1,515 B`, `sha256:ae042264…`, holder `Olympus`) | 1869 | 🟢 **New this pass (`p816`), and the most permissively licensed complete APPLICATION in the education stack this base has measured — BSD-3-Clause, which is more permissive than any LMS, SIS or assessment platform in this file.** `163` forks. 🔵 **Flutter, so one codebase ships iOS and Android, which is the delivery shape a consumer-facing education engagement actually needs and which none of the copyleft rows offer.** 🔴 **STALE AND THAT IS THE DECIDING FACT: pushed `2024-07-29`, over two years before this reading. Treat it as a FORK BASE, not a dependency — the grant permits exactly that, and `P40` assumes the studio owns the fork** |
| **Orbit** — spaced-repetition platform for embedding review INSIDE prose | https://github.com/andymatuschak/orbit | 🟡 **SPLIT GRANT — byte-read** (`457 B`, `sha256:86b93fd1…`): 🟢 **Apache-2.0 for all sources and compiled binaries, EXCEPT** 🔴 **`packages/app` and `packages/backend`, which are AGPL-3.0-or-later OR BUSL-1.1 at the licensee's choice** — 🔴 **GitHub's licence field says `NOASSERTION`** | 1839 | 🟢 **New this pass (`p816`), and the most interesting licence structure in this base.** *"Experimental spaced repetition platform for exploring ideas in memory augmentation."* Andy Matuschak; pushed `2026-10-20`. 🔵 **The idea is genuinely distinct from every other row: review prompts are embedded in the TEXT a learner is already reading, so there is no separate app to open and no deck to maintain — which is the right shape for an OER textbook or a corporate course.** 🔴 **But the split falls in the worst possible place for a product: the libraries are Apache-2.0 and the APP and BACKEND — the parts that constitute a deployable system — are AGPL-or-BUSL, and BUSL-1.1 is NOT an open-source licence at all.** 🟢 **Usable posture: take the Apache-2.0 libraries and the interaction design, implement the app and backend yourself. 🔴 Do NOT deploy `packages/backend` for a client without a licence decision made in writing** 🔵 **`P1057` NOW HAS AN INSTANCE ON THE LIVENESS CHANNEL, not just the licence one: this pass's liveness sweep returned `404` for `README.md@master` and `200` for **`Readme.md`** — the repo is live and its own grant text points at that spelling. `raw.githubusercontent.com` is case-sensitive, so a liveness probe with one spelling of a filename has not checked liveness; it has checked a spelling. `ACTION p816-E` carries the generalisation** |
| **Hashcards** — plain-text spaced-repetition system | https://github.com/eudoxia0/hashcards | 🟢 **Apache-2.0 — byte-read** (`11,358 B`, `sha256:cfc7749b…`) | 1193 | 🟢 **New this pass (`p816`), and the cleanest row in the tier: a complete SRS whose entire corpus format is plain text under Apache-2.0.** `74` forks, pushed `2026-11-09` — maintained, unlike `memo`. 🔵 **Plain text is the property that matters commercially: the cards are diffable, reviewable and version-controlled, so a client's subject-matter experts can author them in the same pipeline they already use for documentation, and there is no proprietary deck format to migrate out of later.** 🟢 **The `11,358 B` payload is the same verbatim Apache-2.0 object this base byte-read at `LIST-LUXEMBOURG/eagle-aig` and `openedx/XBlock` — `T41`'s instrument, third independent agreement** |

## 🟢 Twentieth pass (`p815`, 2026-11-15) — the platform tier that produces the GRADE, and the one place in this file where the permissive option is the SECOND-most-starred rather than the first

🔴 **This file has named `86` platforms across nineteen passes — LMS, SIS, ERP, parent portals,
national school portals, university self-management, the research library — and not one of them
is the system that runs a student's code, compares it against the cohort, locks down the exam, or
places the timetable.**

🟢 **The licence headline, and it is the inverse of `p814`'s.** With the research library, the
permissive platform (`DSpace`, BSD-3-Clause) was also the structurally central one. 🔴 **Here the
central platform is `Judge0` (`4,519★`) and it is GPL-3.0, while the permissive platform is
`Autolab` (`808★`, Apache-2.0) at a fifth of the attention.** 🔵 **So for the first time in this
file the recommendation diverges from the star order — and `T44` is the argument for saying so to
a client out loud, rather than quietly shipping the popular one.**

🟢 **Every platform below is a system institutions ALREADY RUN and already staff.** 🔴 **What
they do NOT have, measured this pass, is an agent layer: `q="autograder mcp"` returns
`total_count=1`.**

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| **Autolab** — course management + autograded programming assignments | https://github.com/autolab/Autolab | 🟢 **Apache-2.0 — byte-read** (`11,323 B`, `sha256:6dc0e068…`) | 808 | 🟢 **New this pass (`p815`), and the one assessment platform here a studio can fork, embed and ship with no source obligation.** Carnegie Mellon 🇺🇸 origin, maintained since `2014-10-25`, pushed `2026-11-11`. 🔵 **It is a PLATFORM and not a plugin — roster, submissions, autograding and scoreboards in one — so it competes with the LMS for the assessment job rather than extending it. That is a procurement conversation, not a technical one: propose it where the LMS is weak at programming assessment, not as an LMS replacement.** 🔵 **Customisation slot: it has no agent surface at all, which with `bruchris/canvas-lms-mcp` as the topology reference is `P37`'s build.** 🟡 **Prerequisite the studio does NOT own: an autograding execution host (containers, resource limits), which is an infrastructure line item on every engagement using it** |
| **Judge0** — sandboxed code-execution service | https://github.com/judge0/judge0 | 🔴 **GPL-3.0 — byte-read** (`34,525 B`, `sha256:aafb5908…`) | 4519 | 🟢 **New this pass (`p815`) — the most-starred education platform in this base after Zotero, and nineteen passes never wrote its name.** *"Robust, fast, scalable, and sandboxed online code execution system for humans and AI."* 🔴 **GPL-3.0, and it is exactly the component a studio wants inside a product — the squeeze `T44` names.** 🟢 **The only clean posture: deploy it as a separate service behind an HTTP boundary alongside the deliverable, never link it in. Its own API-first design makes that the natural shape anyway, which is why this is a workable recommendation rather than a reluctant one.** 🔵 **Note the *"and AI"* in its own positioning: it is already the de-facto sandbox for agent tool-use, so an engagement can justify it twice over** |
| **Safe Exam Browser** — exam lockdown client + central configuration server | https://github.com/SafeExamBrowser/seb-win-refactoring | 🟡 **MPL-2.0 — byte-read** (`16,725 B`, `sha256:c76f740d…`); 🔴 **the macOS/iOS client `seb-mac` (`150★`) has NO licence payload** | 369 | 🟢 **New this pass (`p815`).** ETH Zürich 🇨🇭; the de-facto exam-lockdown client in European higher education and the one Moodle's quiz integration expects. Pair with `SafeExamBrowser/seb-server` (`98★`, MPL-2.0) for cohort-wide configuration and monitoring. 🟡 **MPL-2.0 is file-level copyleft — shippable beside proprietary code, with changes to MPL files published. Materially better than GPL for a packaged deliverable.** 🔴 **`T45`: `school-cheating/SEBPatch` (`210★`) is a licence-compliant MPL fork of this client with a BYTE-IDENTICAL payload, and the AGPL bypass `nxvvvv/safe-exam-browser-bypass` (`400★`) OUTSTARS the client itself.** 🔴 **And coverage is not platform-uniform: a cohort on iPads cannot be given the same licence answer as one on Windows laptops — `seb-mac`'s README says *"not for building own versions of SEB."*** 🔵 **Customisation slot: integrity EVIDENCE and audit trail around it, which is `P37`'s appeal-survivable record — not better lockdown** |
| **UniTime** — university course, exam and student timetabling | https://github.com/UniTime/unitime | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:58d1e17f…`) | 358 | 🟢 **New this pass (`p815`), and the only constraint-solver platform in this base.** *"A distributed system that allows multiple university and departmental schedule managers"*; README states deployment at *"universities in North America and Europe."* 🟢 **Apache-2.0 — forkable and shippable.** 🔵 **The commercial read: timetabling is a real optimisation problem with a hard deadline every single term, the incumbents are expensive proprietary schedulers, and an LLM is the WRONG tool for the solve. The value a studio adds sits ON TOP of the solver — natural-language constraint capture and explanation of why a request could not be met. That is `P39`, and it is the cheapest credible "AI" engagement in this file because the hard part is already solved and Apache-licensed.** 🟡 **For schools rather than universities, `GEOSOFT-GLOBAL/timetablely` (`27★`, MIT) is the smaller permissive option** |
| **Dolos** — source-code plagiarism and collusion detection | https://github.com/dodona-edu/dolos | 🟢 **MIT — byte-read** (`1,083 B`, `sha256:9e2ceeed…`, holder `Team Dolos <dolos@ugent.be>`) | 357 | 🟢 **New this pass (`p815`), and the single most useful row in the layer for a product build.** Ghent University 🇧🇪, pushed `2026-11-14`. 🟢 **It does `jplag/JPlag`'s job — structural token-based similarity across a cohort with a visual report — under MIT instead of GPL-3.0.** 🔵 **It is a MEASUREMENT instrument, not an LLM judge, which is the property that lets an integrity finding survive a student appeal. `omerfarooq223/AutoGrader-Agent` LLM-judges plagiarism; replace that step with this before anyone's academic record depends on it.** 🔵 **Customisation slot: the cohort-level review workflow and the evidence pack — the detector is done** |
| **Pressbooks** — OER authoring and publishing | https://github.com/pressbooks/pressbooks | 🔴 **GPL-3.0 — byte-read at `dev/LICENSE.md`** (`35,146 B`, `sha256:c53a65c2…`); 🔴 **`LICENSE` `404`s at both `main` and `master` — default branch is `dev`** | 462 | 🟢 **New this pass (`p815`) — the OER production platform this file had never named, and `T46`'s specimen.** WordPress-based; turns a manuscript into EPUB, PDF and web at once; `BCcampus` 🇨🇦 runs `pressbooks-textbook` on it for a provincial open-textbook programme. 🔵 **Customisation slot, and it is the strongest AI fit in this section: open textbooks are the one corpus an institution owns outright, so retrieval, summarisation, question generation and translation over them carry NO `T40` source-legality exposure at all.** 🔴 **GPL-3.0 and it is a WordPress platform — deploy and extend via plugins, do not fork into a product** |

## 🟢 Nineteenth pass (`p814`, 2026-11-13) — the platform tier this file had never named: the RESEARCH LIBRARY, and the only permissively licensed platform in the education stack

🔴 **This file has named `81` platforms across eighteen passes — LMS, SIS, ERP, parent portals,
national school portals, university self-management — and not one of them is the system a
graduate student, a doctoral candidate or a researcher logs into.** 🟢 **Every row below is a
system institutions ALREADY RUN and already staff, with a published REST API and a build-safe
agent surface shelved in `agents/top.md` this pass.**

🟢 **The licence headline: `DSpace` is BSD-3-Clause.** 🔴 **Moodle is GPL-3.0, Open edX AGPL-3.0,
Koha GPL-3.0, OJS GPL-3.0, OpenEduCat LGPL-3.0, Sakai Apache-2.0.** 🔵 **So of the platforms a
university runs, DSpace is the one a studio can fork and ship inside a deliverable — and the
budget sits with the library, not with the IT department that owns the LMS.**

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| **DSpace** — institutional repository (theses, datasets, open-access output) | https://github.com/DSpace/DSpace | 🟢 **BSD-3-Clause — byte-read** (`1,504 B`, `sha256:baf9ee18…`) | 1111 | 🟢 **New this pass (`p814`).** The thesis and research-output repository of most universities worldwide; DSpace 7+ ships a published REST API. 🟢 **Agent surface in two regions, both MIT and both read-only: `mpasternak/dspace-mcp` 🇵🇱 (*"Read-only by construction, not by promise"*) and `suren-kk/armenian-national-library-mcp` 🇦🇲 (DSpace 9, rights check BEFORE retrieval, writes not implemented).** 🔵 **Customisation slot: discovery and summarisation over a corpus the institution already owns outright — no `T40` source-legality exposure at all, because the institution IS the rights holder** |
| **Zotero** — reference manager (the researcher's own library) | https://github.com/zotero/zotero | 🟡 **AGPL-3.0 — byte-read at `COPYING`** (`35,358 B`, `sha256:5b7dc919…`); 🔴 the API reports `NOASSERTION` | 15942 | 🟢 **New this pass (`p814`) — the densest agent surface in education: `348` repositories on one query.** Local-first desktop app with a Web API v3 and, on Zotero 10+, a local API. 🔵 **Customisation slot: `oscardvs/zoteus` (MIT) already does versioned writes, reversible trash, CSL citation formatting and `zotero_check_citations` for invented citations and misquotes — fork that, do not start from scratch.** 🔴 **AGPL upstream, so integrate over the protocol and never derive** |
| **Open Journal Systems (OJS)** — scholarly publishing | https://github.com/pkp/ojs | 🔴 **GPL-3.0 — byte-read** (`35,148 B`, `sha256:8b1ba204…`) | 1053 | 🟢 **New this pass (`p814`).** Runs the university-published journal, editorial workflow and peer review; heavily deployed in 🇧🇷 Brazil and 🇲🇽 Mexico. 🟢 **Agent surface `mpasternak/ojs-mcp` (MIT) with `OJS_ALLOW_WRITES=1` OFF by default.** 🟡 **Prerequisite the studio does NOT own: `api_key_secret` in `config.inc.php`, set by the institution's OJS admin, or every token request returns `401`** |
| **Koha** — integrated library system (the catalogue and circulation) | https://github.com/Koha-Community/Koha | 🔴 **GPL-3.0 — byte-read** (`35,150 B`, `sha256:9edff973…`) | 601 | 🟢 **New this pass (`p814`).** The public and academic library ILS, strongest in 🇮🇳 India and APAC. 🟢 **Its REST API supports OAuth2 `client_credentials` — the only non-password auth any agent in this base uses.** Agent surface `asjolaviral/koha-mcp-server` (MIT). 🟡 **Prerequisite: REST API enabled plus an OAuth2 key pair, issued by the library** |
| **Aldine** — self-hosted collaborative LaTeX (where the thesis is written) | https://github.com/trahloff/Aldine | 🔴 **AGPL-3.0 — byte-read** (`34,522 B`, `sha256:4df3c306…`) | 126 | 🟢 **New this pass (`p814`) — the AUTHORING end of the layer, and an Overleaf alternative.** 🔵 **Self-hosting is the whole value for an institution that cannot send unpublished research to a SaaS — a procurement argument, not a technical one.** 🔵 **Composes directly with `PedroSmaxY/abnt-mcp` 🇧🇷 (norm audit) and `oscardvs/zoteus` (citations into the draft).** 🔴 **AGPL-3.0 and it is a network service by design, so offering it to students triggers the source obligation: deploy it, do not fork it into a product** |

## 🟢 Eighteenth pass (`p813`, 2026-11-13) — the two platform tiers this file had never named: 🇨🇳 China's university LMS, and 🇺🇸 the North American K-12 parent portal

🔴 **Every section of this file written before `p813` assumes Moodle, Canvas, an SIS vendor, a
European school portal or a LATAM self-management system.** 🟢 **Two whole incumbent tiers were
missing, and both were found with the same instrument that closed EMEA at `p811` and LATAM at
`p812`: name the system, never the language or the region.**

### 🇨🇳 The Chinese university LMS tier — the densest agent cluster this base has measured

| Platform | Incumbent where | Open agent surface found | License | Stars |
|---|---|---|---|---|
| **Chaoxing / 学习通** (Xuexitong) | 🇨🇳 Chinese higher education, very widely deployed | [`DanMo661/xuexitong-cli`](https://github.com/DanMo661/xuexitong-cli) is the anchor; `19` repositories on one query, `12` build-safe, `17` of `19` created since `2026-09-11` | **MIT** ×10, **Apache-2.0** ×1 | `24`, `15`, `3`, `1` … |
| **雨课堂** (Rain Classroom / Yuketang, Tsinghua) | 🇨🇳 lecture delivery and in-class interaction | [`ahdaolma/yuketang-mcp`](https://github.com/ahdaolma/yuketang-mcp) — course + courseware, auto key-point capture, annotation, Q&A | **MIT** | `0` |
| **TronClass** (WisdomGarden) | 🇹🇼 Taiwanese universities (NTOU, FJU observed) | `5` repositories — [`cantpr09ram`](https://github.com/cantpr09ram/TronClass-MCP), [`markbee66`](https://github.com/markbee66/tronclass-mcp), [`RX5950XT`](https://github.com/RX5950XT/FJU-TronClass-MCP), [`JasonWu55`](https://github.com/JasonWu55/tronclass-mcp), [`rlongdragon`](https://github.com/rlongdragon/tronclass-mcp) | 🔴 **NONE — `0` of `5` carry any licence**, while all `5` return `200` on `README.md` | `3`, `1`, `1`, `1`, `0` |
| **SIAKAD** (*Sistem Informasi Akademik*) | 🇮🇩 Indonesian universities, per-institution | [`alfa-yohannis/siakad-mcp`](https://github.com/alfa-yohannis/siakad-mcp) (Universitas Pradita) — **`1` repository on the whole query** | **MIT** | `0` |
| **NEIS** (나이스) | 🇰🇷 Korean national education information system | [`arapodcho/mcp_server_neis_api`](https://github.com/arapodcho/mcp_server_neis_api) over the `open.neis.go.kr` open-data portal | **MIT** | `0` |

🔵 **The decision rule this tier forces, and it is new.** 🔴 **The best-engineered agent in the
Chaoxing cluster is the one a studio must refuse** — see `T36` and the `DeliciousBuding/chaoxing`
row in `agents/top.md`. Its scope list includes automated attendance sign-in and coursework
submission. 🟢 **Scope a Chinese higher-ed engagement on the Tier-1 read-only anchor
(`DanMo661/xuexitong-cli`, which declines the abuse case in its own README) and treat the
integrity boundary as a written deliverable, not an implementation detail.**

🟢 **And NEIS is the counter-example that sets the target.** It is the only platform in this
pass's entire harvest that **publishes an official API**, and its agent correspondingly needs no
scraping, no reverse-engineered login and no learner credential at all. 🔵 **Where a ministry
operates the system, "ask them to publish the API" is a real engagement option and a far cheaper
one than maintaining a scraper** (`P32`).

### 🇺🇸 The North American K-12 parent/student portal tier — built by families, not vendors

🔴 **A US K-12 engagement does not start at the LMS either. It starts at the SIS portal the parent
logs into** — and that tier had `0` mentions in this file before `p813`.

| Platform | Incumbent where | Open agent surface found | License | Stars |
|---|---|---|---|---|
| **Infinite Campus** (Campus Parent) | 🇺🇸 large US districts | [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) — `20` tools, **multi-district via CUPS SSO auto-discovery**, exactly one write/IO-gated tool | **MIT** | `5` |
| **StudentVUE** (Edupoint Synergy) | 🇺🇸 very widely deployed K-12 SIS | [`coolcrazycid/studentvue-mcp`](https://github.com/coolcrazycid/studentvue-mcp) (headless browser against the student site) and [`meowgoober/studentvue-mcp`](https://github.com/meowgoober/studentvue-mcp) (mobile-app API) — **opposite routes to the same system** | **MIT** ×2 | `0`, `0` |
| **Schoology** (PowerSchool) | 🇺🇸 K-12 LMS | `11` repositories; [`coolcrazycid/schoology-mcp`](https://github.com/coolcrazycid/schoology-mcp), [`obfuscated-tm/dewey`](https://github.com/obfuscated-tm/dewey), [`riripatate/schoology-mcp`](https://github.com/riripatate/schoology-mcp) | **MIT** (several); `dewey` MIT under a GitHub `NOASSERTION` | `2`, `3` |
| **Skyward** | 🇺🇸 K-12 SIS, strong in the Midwest | [`caleb-media-studio/skyward-mcp`](https://github.com/caleb-media-studio/skyward-mcp) — user-hosted, OAuth 2.1 + PKCE, **"the first release is deliberately read only"** | **MIT** | `0` |
| **Blackbaud Financial Edge NXT** | 🇺🇸 independent schools and non-profits | [`CDataSoftware/blackbaud-fe-nxt-mcp-server-by-cdata`](https://github.com/CDataSoftware/blackbaud-fe-nxt-mcp-server-by-cdata) — **the only VENDOR-published connector in the tier** | **MIT** | `0` |
| **PowerSchool SIS** | 🇺🇸 the largest US K-12 SIS | [`zuvy/ps-mcp-server`](https://github.com/zuvy/ps-mcp-server) — **`1` repository, unlicensed** | 🔴 **NONE** | `1` |

🔵 **Two scoping consequences a bid depends on.**
🟢 **(1) The supply is FAMILY-BUILT, and it shows in the architecture.** The strongest credential
posture in this pass comes from this tier and from an unpaid author:
[`obfuscated-tm/dewey`](https://github.com/obfuscated-tm/dewey) needs **no password at all** — it
reuses the Schoology session Chrome already holds. 🔴 **But family-built also means
single-district, single-child and unmaintained by default; only `chrischall/infinitecampus-mcp`
handles multiple districts, and no repository in the tier has an institutional owner.**
🔴 **(2) PowerSchool — the largest SIS in the tier by installed base — has exactly one agent and
it carries no licence.** 🟢 **That is the widest open slot `p813` found in North America**, and it
is the same shape as the SIAGIE nil `p812` found in Peru.

## 🟢 Seventeenth pass (`p812`, 2026-11-13) — the second open-source education ERP gains an agent surface, and LATAM's university systems gain one for the first time

### Frappe Education — reachable with no education-specific code, on a FIRST-PARTY MIT connector

🟢 **This file has said since `p807` that OpenEduCat is the cheapest SIS engagement in this KB
because Odoo has generic connectors. There is now a second, and its connector is better.**

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| **Frappe Education** | https://github.com/frappe/education | 🔴 GPL-3.0 (byte-read `license.txt`, `19 B`) | 709 | Students, programs, enrolment, assessment, fees, on the Frappe framework. `494` forks. 🟢 **Reachable through Frappe Framework's BUILT-IN MCP server (MIT) with no education-specific code** — `13` DocType-generic tools, discovery included. 🔴 Copyleft core: integrate, never derive |
| **Frappe Framework** | https://github.com/frappe/frappe | **MIT** | 11.1k | The substrate. 🟢 **The connector is first-party, reuses the site's REST v2 permissions, labels `update`/`delete` with `destructiveHint: True`, and is OFF until `enable_mcp` is set.** 🔵 **Unlike Odoo, no third-party connector and no "YOLO mode" to grep for** |
| **Frappe LMS** | https://github.com/frappe/lms | 🔴 AGPL-3.0 | 3.4k | Same substrate, same connector, `1,593` forks. 🔴 Network clause — hosted delivery needs legal review |

🔵 **The decision rule, now that there are two.** Odoo/OpenEduCat (`P12`) where the client already
runs Odoo or needs its finance and procurement depth; **Frappe Education (`P29`) where the client
is greenfield or already on Frappe/ERPNext** — because its connector is first-party and MIT, which
removes the third-party-connector risk that `P12` has to manage.

### 🇦🇷🇧🇷 The LATAM university self-management tier — a platform layer this file had never named

🔴 **Every section below assumes Moodle, Canvas, an SIS vendor or a European school portal.** 🟢
**Across Argentina and Brazil the system a student actually logs into is a national or
institutional self-management platform, and `p812` found agent surfaces for three of them.**

| Platform | What institutions run it | Agent surface found this pass | License | Risk posture |
|---|---|---|---|---|
| **SIGAA** (*Sistema Integrado de Gestão de Atividades Acadêmicas*) | 🇧🇷 Brazilian federal and state universities and institutes (UNEMAT, IFSC, UFRPE, UFPA observed) | [`GallegoSz/sigaa-mcp`](https://github.com/GallegoSz/sigaa-mcp) (`13` tools), [`heitorsDev/sigaa-ifsc-mcp`](https://github.com/heitorsDev/sigaa-ifsc-mcp), [`Pedromaia0/sigaa-mcp`](https://github.com/Pedromaia0/sigaa-mcp), [`EduardoBidese/sigaa-agente`](https://github.com/EduardoBidese/sigaa-agente) | MIT ×4 | 🟢 **read-only by construction** 🔴 **plaintext password in client config; HTML parsing; one student per install** |
| **Sysacad + UTN aula virtual** | 🇦🇷 Universidad Tecnológica Nacional, `18` regionales named | [`nialvape/utn-mcp`](https://github.com/nialvape/utn-mcp) (`12★`, `8` forks) | **ISC** | 🟢 **OAuth server; password never stored; token hashed; session encrypted; preview-then-confirm writes; REFUSES campuses without valid HTTPS** |
| **SIU Guaraní** | 🇦🇷 most Argentine national universities | [`HyNuwa/UniMCP`](https://github.com/HyNuwa/UniMCP) (Moodle + Guaraní) | **MIT + inherited ISC** | 🟢 **Guaraní read-only — *"Guaraní no tiene API"*, the server reads the G3W pages** 🔴 tested thoroughly only at UNJu |
| **SUAP** | 🇧🇷 Institutos Federais | [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) — prepares the teacher's RIT as a **draft** | 🔴 AGPL-3.0 | 🟢 draft-not-submit 🔴 copyleft; the only other SUAP server has no licence |
| **SIAGIE** | 🇵🇪 Peruvian national K-12 | 🔴 **NONE — `25` repositories, zero agents, zero licences** | — | 🔴 **widest open slot found this pass** |
| **SIMAT** | 🇨🇴 Colombian national enrolment | 🔴 **NONE — `total_count=0`** | — | 🔴 hard nil |

🔵 **Scoping consequence, and it is the kind that decides a bid.** A Brazilian or Argentine
university engagement does **not** start at the LMS. It starts at SIGAA, Sysacad or Guaraní —
**none of which publishes an API** (Guaraní's own integrator says so outright), so every path
above is an unofficial parser, scraper or RPA driver against an authenticated session. 🔴 **That
is a contract and data-protection question before it is an architecture one**, exactly as `p810`
concluded for the proprietary national SIS products in EMEA.

## 🟢 Sixteenth pass (`p811`, 2026-11-13) — a whole PLATFORM LAYER this file had never named: the national and regional school portal

🔴 **Every section below this one assumes the institution's system of record is an LMS or an
SIS.** 🟢 **In European state school systems it very often is neither.** What a parent and a
pupil actually log into is a portal operated by a ministry, a federal state or a regional
authority — and `p811` found an agent surface for five of them, all published within five
days of each other, all permissive, all tiny.

| Platform | Operated by | Country | Agent surface found this pass | Licence | Stars |
|---|---|---|---|---|---|
| **Schulportal Hessen (Lanis)** | the federal state of Hesse | 🇩🇪 Germany | [`udondan/lanis`](https://github.com/udondan/lanis) — SDK + CLI + MCP server | MIT | 2 |
| **DSBmobile** | schools via the DSB substitution-plan service | 🇩🇪 Germany | [`udondan/dsbmobile`](https://github.com/udondan/dsbmobile) — SDK + CLI + MCP server | MIT | 0 |
| **Admentum** | the Swedish school-platform vendor | 🇸🇪 Sweden | [`andyswe/admentum-mcp`](https://github.com/andyswe/admentum-mcp) — **read-only**, one item per call | MIT | 0 |
| **iPasen / Séneca** | Junta de Andalucía (regional education authority) | 🇪🇸 Spain | [`boraita/ipasen_mcp`](https://github.com/boraita/ipasen_mcp) — grades, absences, messages, **confirmed actions** | MIT | 0 |
| **Greek School Network (`sch.gr`)** | the Greek Ministry of Education | 🇬🇷 Greece | [`weirdapps/sch-mail`](https://github.com/weirdapps/sch-mail) — IMAP/SMTP MCP server | MIT | 0 |
| **edu.by site constructor** | the Belarusian national school-web service | 🇧🇾 Belarus | [`Severnbli/edu-by-agent`](https://github.com/Severnbli/edu-by-agent) — CLI + MCP + skills, **preview and confirmation before every write** | 🔴 GPL-3.0 | 0 |
| **PRONOTE** (with EduConnect) | Index Éducation; EduConnect is the state identity provider | 🇫🇷 France | [`sairo-cyber/pronoteConnect`](https://github.com/sairo-cyber/pronoteConnect) — self-hosted MCP connector | 🔴 GPL-3.0-or-later (byte-verified against `NOASSERTION`) | 2 |

🔵 **Why this is a market fact and not a curiosity.** Four of these are operated by a STATE
BODY. That changes who the buyer is (a ministry or a Land, not a university CIO), what the
procurement looks like (public tender), and which regulation binds first (for the EU ones,
Art. 27 FRIA duties fall on PUBLIC deployers). 🟢 **It also answers `ACTION p802-B` from the
supply side:** this base has twice failed to find German classroom deployment STATISTICS,
and has now found German classroom INTEGRATION CODE instead — at the Land level, which is
where `p810` predicted the evidence would sit.

🔴 **Do not mistake any of these for a product.** Every one is `0–2★`, single-maintainer,
self-declared unofficial, and built against an undocumented or semi-documented portal API.
🟢 **What they are worth is the seam**: they prove the integration is possible and they show
which verbs the portal actually exposes, which is normally the expensive unknown in a
public-sector education bid.

🟢 **And one genuinely new system of record, from the same window:**

| Platform | Repo | Licence | Stars | What it is |
|---|---|---|---|---|
| **Chalk** | [`usechalk/chalk`](https://github.com/usechalk/chalk) | 🔴 AGPL-3.0 | 2 | **New this pass (`p811`).** *"The open-source **K-12 IT stack**: mixed-fleet device tracking (ChromeOS, Intune, Jamf), help desk, 1:1 lifecycle, **rostering, SSO**, and Google/AD/Entra provisioning **in one Rust binary**. Self-host free, or we host it."* Pushed `2026-11-09`. 🟢 **It is the only artifact in this base that puts rostering and device lifecycle in the same system** — which is what a district IT director actually buys. 🔴 **AGPL-3.0 with a hosted commercial offering: the classic open-core posture, and the network clause rules it out as the base of a hosted deliverable.** 🔵 Read it for the data model of a district IT stack; propose integration, never derivation |


## 🟢 Fifteenth pass (`p810`, 2026-11-13) — three platforms institutions actually run gain an agent surface, and one gains a SECOND at a different risk level

🔵 **This file's premise is that an AI engagement means adding an agent layer to a system the
institution already runs.** 🟢 **`p810` added that layer for three such systems, and for the
first time can offer one platform at two risk postures.**

| Platform | What institutions run it | Agent surface added this pass | License | Risk posture |
|---|---|---|---|---|
| **Sakai** | Higher ed, heavily US/consortium; named `3,937` times in this base — more than any other LMS — and carried **zero** agents until now | [`jtayped/sakai-mcp`](https://github.com/jtayped/sakai-mcp) | `MIT` | 🔴 **WRITE — includes submission on the student's behalf. Gate it** |
| **Sakai** | " | [`sayt25606-rgb/sakai-tasks-mcp`](https://github.com/sayt25606-rgb/sakai-tasks-mcp) | `Apache-2.0` | 🟢 **READ-ONLY and local** |
| **Canvas** | The largest higher-ed LMS in North America | [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp) `119★` | `MIT` (byte-verified, blob `5ba93171ff8f`) | 🟢 **Read-only by construction — no write path exists** |
| **Schoology** | US K-12 districts | [`riripatate/schoology-mcp`](https://github.com/riripatate/schoology-mcp) | `MIT` | 🟡 Student-session scope; **no admin API key needed** |
| **Schoology + StudentVUE** | FCPS (one of the largest US districts) | [`jibberswrld/fcps-school-mcp`](https://github.com/jibberswrld/fcps-school-mcp) | `MIT` | 🟡 Single-district |
| **Schoology + Infinite Campus** | PAUSD | [`dajun666/schoology-mcp`](https://github.com/dajun666/schoology-mcp) | `MIT` | 🟡 🟢 **First Infinite Campus surface in this base** |
| **Cubite LMS** | Vendor-hosted LMS (SCORM, xAPI, certificates, cohorts) | [`amirtds/cubite-mcp`](https://github.com/amirtds/cubite-mcp) | `MIT` | 🔴 **`137` tools at the signed-in user's permission level** |

🟢 **The Sakai pair is the genuinely new capability.** 🔵 **Same platform, same week, opposite
postures** — quote the read-only local server to a cautious district and the submission-capable
one only behind a write gate. 🔴 **This base has never before been able to offer that choice on
any LMS**, and it is the single most common objection in an education pilot conversation.

🔴 **`137` tools is a governance object, not a feature.** [`amirtds/cubite-mcp`](https://github.com/amirtds/cubite-mcp)
runs at the teacher's own permission level — the same unclaimed risk `p792-D` raised over
[`jeffercbs/chispa-mcp`](https://github.com/jeffercbs/chispa-mcp)'s `77` tools, **at nearly
twice the surface.** 🟢 **The counter-example now exists and it is in this base:** the Ed-Fi
prototype exposes **six** tools behind a read-only database role (`T28`). 🔵 **Tool count is a
design choice, and the standards body chose six.**

## 🟢 Student information systems — the layer this file has been thinnest on

🟢 **New this pass:** [`FenixEdu/fenixedu-academic`](https://github.com/FenixEdu/fenixedu-academic)
(`LGPL-3.0`, `175★`, `111` forks) — a full academic SIS from **Instituto Superior Técnico,
Lisbon 🇵🇹**: curricular plans, enrolment, degrees, grading, theses. 🟢 **The largest dedicated
open-source SIS in this base, and the only named EMEA-origin institutional system in it.**
🔴 **Dormant since `2023-06-14`** — an architecture reference and a migration source, not a
platform to deploy. 🔴 **LGPL-3.0 is weak copyleft: linking is fine, modifications to the
library itself must be released.**

🔵 **Rostering is the layer BETWEEN the SIS and the LMS, and `p810` added it to
[`repos/foundations.md`](../repos/foundations.md):** OneRoster now has a conformance suite
([`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests),
`Apache-2.0`), an importer ([`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import),
🔴 `GPL-2.0`) and a Go server ([`bgwdotdev/go-oneroster`](https://github.com/bgwdotdev/go-oneroster),
`MIT`, 🔴 stale since `2020`). 🔴 **And no agent at all** — a dedicated leg returned an empty
result set. 🟢 **Use the conformance suite as a contractual acceptance gate on any roster
integration**, whoever builds it.

The education equivalent of "Odoo for ERP". These are the systems institutions
already run; an AI engagement almost always means **adding an agent layer to one
of these**, not replacing it. All licenses and star counts verified from the
repository page (2026-11-13, with the LTI and Moodle-MCP rows verified this
pass).

### What changed this pass (thirteenth pass, `p808`, 2026-11-13) — nothing was added, and one licence was independently re-verified

🔴 **Zero new platforms this pass — the vertical leg returned this shelf's own contents
for a NINTH consecutive pass.** `open source platform education ERP CRM MIT Apache`
returned `OpenEduCat`, `Krayin`, `Huly` and `ERPNext`. 🟢 **All four are already held**,
and `p807`'s structural reading of this nil — *every education ERP/CRM in the open is
copyleft, every permissive one is general-purpose* — was **reproduced exactly** by this
window rather than contradicted. `OpenEduCat` `LGPL-3.0`, `ERPNext` `GPL-3.0`,
against `Krayin` `MIT` and `Huly` `Apache-2.0`, both horizontal. 🔵 **A finding that
survives a ninth independent reproduction should now be treated as a property of this
market, not an observation about it.**

🟢 **One licence independently re-verified, and it carries a trap worth recording.**
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) was re-read
from its rendered repository page this pass: **`LGPL-3.0`**, **`911★`**, *"Comprehensive
Open Source ERP for Educational Institutes"*. 🟢 **This matches the row below exactly —
nothing changed.** 🔴 **But the GitHub sidebar renders no SPDX licence name for this
repository**; the `LGPL-3.0` appears only in the README body and a badge, and the
search-tier result for it stated **no licence at all**. 🔵 **So an automated licence
scrape of this repository returns EMPTY, not wrong** — and `OpenEduCat` is the single
most load-bearing platform on this shelf (it is the only open-source SIS in this base
with a working agent surface). 🟢 **A future pass that sees a blank licence field here
must not read it as a regression, a relicensing or grounds for rejection.** The LGPL-3.0
obligation on a client deliverable is unchanged: dynamic linking and module-level
separation keep it manageable, modifying its own files does not.

<details>
<summary>Prior pass (<code>p807</code>, twelfth) — a new section, because the saturated vertical leg finally said something</summary>

### What changed at the twelfth pass (`p807`, 2026-11-13)

🟢 **One new section, three new rows, no changes to any existing row:
`## Admissions and enrolment CRM`.** The prescribed vertical-platform leg has now
returned this shelf's own contents **eight passes running**. 🔵 **This pass the nil was
read instead of recorded:** the leg keeps pairing education platforms that are copyleft
with permissive platforms that are not educational, and that pairing is a structural
fact about the market rather than a failure of the query.

🟢 **Consequence: admissions is CRM-shaped work and this base had no CRM.** Added
`krayin/laravel-crm` (**MIT**, `24.1k★` — the largest permissively licensed CRM this base
has found), `cortezaproject/corteza` (**Apache-2.0**, `2.2k★`) and `apache/ofbiz-framework`
(**Apache-2.0**, `1.2k★`, listed with a caution). All three verified from the rendered
repository page this pass.

🔴 **One claim was withdrawn before publication** — Corteza's origin — and the withdrawal
is recorded in the section rather than quietly dropped.

### What changed this pass (eleventh pass, `p806`, 2026-11-13) — two rows, and the second one changes the altitude of every North American engagement

🟢 **`numbas/Numbas` (Apache-2.0, `217★`/`130` forks) is the largest permissively
licensed education platform of EMEA origin this base has found.** Browser-based
e-assessment with an emphasis on mathematics, built by **Newcastle University's School
of Mathematics, Statistics and Physics**. It matters because this file's `T7`-shaped
problem — *the platform layer is copyleft, so the client's host system constrains
everything* — **does not apply to it.** TAO is GPL-2.0; Moodle is GPL; Canvas CE and
Open edX are AGPL-3.0. Numbas is Apache-2.0, which means a studio can fork it, embed it
and ship it.

🔴 **`Ed-Fi` is the bigger finding, and it is an indictment of this base rather than a
discovery.** US K-12 student data does not move school-by-school; it moves through the
**Ed-Fi** standard, which state education agencies run their reporting on. Every pattern
in this KB that touches a student record reaches it through an LMS or through one
institution's SIS — **the wrong altitude for North America.** 🔴 **This base mentioned
Ed-Fi `249` times in its append-only trending logs and `0` times in any file a studio
reads.** It is now shelved in `repos/foundations.md` under a new K-12 data-standard
layer, and summarised in the standards table below.

🔵 **Neither row came from a search.** Both came from a scripted audit of this base
against itself (`scratchpad/p806/propagation-audit.sh`), because the prescribed search
battery returned nil on new platforms for a **seventh consecutive pass** — every
vertical leg returns Moodle, Canvas, Open edX, Sakai, Chamilo, OpenEduCat and RosarioSIS,
which is this file's own contents.

### What changed this pass (tenth pass, `p805`, 2026-11-13) — three SIS rows, none of them new

🔴 **The prescribed search battery returned nil on supply for the third consecutive
pass.** 🟢 **So this pass audited what the base had already verified and never
shelved, and the student-information table was where the damage was.** Three
systems — `Gego-K12/gegok12` (**MIT**), `SVWS-NRW/SVWS-Server` (**BSD-3-Clause**)
and `portabilis/i-educar` (**GPL-2.0**) — were license-verified in earlier passes,
recorded in the append-only trending log, and **written to no shelf file at all**.
One of them had been described in that log as already being on this shelf. All
three were re-verified live before being added below.

### Unresolved this pass (ninth pass, `p804`, 2026-11-13) — an informed gap, not a finding

🔴 **The Open edX stewardship and licence question was raised this pass and could not
be closed.** The LMS search leg returned vendor comparisons asserting, variously, that
Open edX is **AGPL**, that it is stewarded by **Axim Collaborative** (a nonprofit
founded by Harvard and MIT), and — in one case — that Canvas's community edition is
**ECL-2.0** rather than AGPL-3.0. 🔴 **`openedx.org` does not resolve from this session
(`getaddrinfo ENOTFOUND`, outside the allowed network domains), so none of it could be
verified at the source.**

🟢 **Nothing in the table below was changed on the strength of it.** The Open edX and
Canvas rows retain the grants this file verified from the repository page in earlier
passes. 🔵 **Recorded here because a vendor blog disagreeing with a verified row is
exactly the kind of noise that becomes wrong data if a later pass reads it without the
context that it was checked and rejected.** `ACTION p804-V` tracks re-verification of
the stewardship claim when the host is reachable.

</details>

## The decision that governs every education engagement

**Do not fork the LMS — but the "no permissive LMS exists" half of that rule is
withdrawn this pass.** 🔴 **Correction (sixth pass, 2026-11-13):** every earlier
edition of this file said *"only Sakai is permissive, ECL-2.0."* That is wrong.
**OpenOLAT is Apache-2.0** — read verbatim from the repository's `LICENSE` file,
which opens *"Apache License / Version 2.0, January 2004"* — and it is a mature
platform (32,338 commits, 451 stars, 165 forks, Java), not a toy. GitHub's
sidebar shows only a generic "License" link and the org listing renders it as
**"Other"**, which is exactly why four passes of license-field reads missed it.
**There are two permissive LMS platforms, not one**, and the second one is the
more interesting of the pair because of what it ships natively (below).

The rest of the rule stands: six of the eight significant open-source LMS
platforms are GPL-3.0 or AGPL-3.0. A fork
makes the client's derived platform copyleft. Instead mount the AI layer as an
**LTI 1.3 tool** or an **MCP server** against the platform's API, keep that
layer MIT/Apache, and emit **xAPI** or **Caliper** events so the institution can
report on it. Every pattern in `compose/patterns.md` follows this shape.

**Update (fifth pass, 2026-11-13): there is now a third mounting surface, and it
is the one that reaches the student record.** Where the incumbent system is built
on a **general-purpose platform**, the agent surface may already exist as a
*platform* connector rather than an education one. **OpenEduCat is Odoo addons,
and Odoo has two mature MCP servers whose tools take the model name as a
parameter** — so the leading open-source education ERP is agent-reachable today
with no education-specific code. See the SIS table below. 🔵 **The general rule
to carry into any engagement: before concluding a platform has no agent surface,
check the platform it is *built on*.**

**Both halves of that sentence now have verified implementations.** LTI 1.3:
`Cvmcosta/ltijs` (Apache-2.0, 373 stars, full LTI Advantage). MCP: Canvas via
`canvas-mcp` (MIT, 324) and — new this pass — **Moodle via `Faixiang/Moodle-MCP`
(MIT, 206)**. The previous edition of this file said Moodle had no significant
MCP server. It does.

## Learning management — the host systems

| Platform | Repo | License | Stars | Where it is the incumbent | AI customization surface |
|---|---|---|---|---|---|
| Moodle | https://github.com/moodle/moodle | GPL-3.0 | 7.6k | Global, strongest in EMEA, LATAM, APAC public education | Mature plugin API; LTI 1.3; web services REST API. **MCP now available: `Faixiang/Moodle-MCP` (MIT, 206) read-only; `falkenslab/moodle-mcp` (MIT) ~260 tools via browser SSO; `MarcosNahuel/moodle-mcp` (MIT) idempotent content publishing** |
| Open edX | https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | MOOCs, corporate academies, national platforms | **`openedx-ai-extensions`** is the official AI plugin point; XBlocks; deploy via `tutor`. MCP only via `openedx-mcp` (AGPL-3.0, 3 stars) |
| Canvas LMS | https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | North American higher ed (dominant) | Rich REST API + LTI 1.3; **`canvas-mcp` (MIT, 324) — README claims up to 128 tools, sidebar says 102** |
| Frappe LMS | https://github.com/frappe/lms | AGPL-3.0 | 3.4k | SMB/corporate training, India | Frappe framework hooks; shares a stack with ERPNext |
| Sakai | https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | Research universities | **Permissive license** — a platform a studio can extend without copyleft reaching the product. `Simon-Initiative/lti_1p3` (MIT, Elixir) comes from adjacent higher-ed work |
| **OpenOLAT** | https://github.com/OpenOLAT/OpenOLAT | **Apache-2.0** | 451 | **German-speaking EMEA** — Swiss and German universities, vocational and public sector. Origin: OLAT at the University of Zurich; maintained by **frentix GmbH** (Switzerland) and the community | 🟢 **New this pass, and it changes the EMEA answer. The only LMS in this table that ships a first-party, provider-pluggable AI layer in-tree** — you do not have to mount an agent to get AI into it. `org/olat/core/commons/services/ai/` defines an SPI (`AiSPI`, `AiEmbeddingSPI`, `AiApiKeySPI`) with **four provider implementations: `anthropic`, `generic` (any OpenAI-compatible endpoint), `localonnx`, `openAI`**. Five features are declared in the `AiFeature` enum — `mc-question-generator`, `image-description-generator`, `essay-generation`, `essay-grading`, `taxonomy-matching` — of which two are user-controlled (a learner can switch them off over the admin default). Ships `AiUsageLog` (per-call token/cost accounting) and `AiUserPreference`. **Apache-2.0 + `generic` provider = point the whole thing at a self-hosted vLLM and nothing leaves the institution.** See `compose/patterns.md` `P13` |
| Chamilo | https://github.com/chamilo/chamilo-lms | GPL-3.0 | 1.0k | LATAM, francophone Africa, Spain | Web services API; accessibility-first. PHP — pair with `packbackbooks/lti-1-3-php-library` (Apache-2.0) |
| ILIAS | https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | 510 | German-speaking EMEA, vocational and public sector | Plugin slots; SCORM/xAPI |

## The integration layer — build once, mount everywhere

| Library | Repo | License | Stars | Use when |
|---|---|---|---|---|
| ltijs | https://github.com/Cvmcosta/ltijs | Apache-2.0 | 373 | Default choice. Node.js, full LTI Advantage (launches, Deep Linking, AGS, NRPS, Dynamic Registration) |
| lti-1-3-php-library | https://github.com/packbackbooks/lti-1-3-php-library | Apache-2.0 | 54 | The client is a PHP shop (Moodle, Chamilo); roster via NRPS, grade writeback via AGS |
| lti_1p3 | https://github.com/Simon-Initiative/lti_1p3 | MIT | 16 | Elixir stack, or you need to act as **Platform** as well as Tool |
| lti-tool | https://github.com/lti-tool/lti-tool | MIT | 8 | Serverless target (Lambda, Cloudflare Workers); early but the only one of its shape |

## Student information systems and institutional ERP

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| OpenEduCat | https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 911 | **SIS + LMS + finance as Odoo modules** — the literal "Odoo for education", and **the only open-source SIS with a working agent surface (new finding, fifth pass)**. 789 forks; branch/tag `19.0`; modules `openeducat_core`, `_admission`, `_exam`, `_fees`, `_attendance`, `_timetable`, `_parent`, `_library`, `_activity`, `_assignment`, `_classroom`, `_facility`. **Because it is Odoo addons, it is reachable by a generic Odoo MCP server** — `erpipe-org/mcp-odoo` (MIT, 433★, three-call gated writes) or `ivnvxd/mcp-server-odoo` (MPL-2.0, 415★, per-model allowlist in a companion module) — so `op.student`, `op.admission`, `op.exam.attendees` and `op.fees` need no new connector. 🔴 **Architecturally verified, not yet run against a live instance (`Gap 286`).** If the client already runs Odoo this is now the shortest path **by a wide margin**. |
| Frappe Education | https://github.com/frappe/education | GPL-3.0 | 707 | **New this pass.** Admissions, fees, scheduling, exams, attendance on the Frappe framework. **The one-framework play: pair with `frappe/lms` (AGPL-3.0) and ERPNext for SIS + LMS + ERP on a single stack** — but the two halves carry *different* licenses (GPL-3.0 vs AGPL-3.0), which matters the moment anything is network-served. License read from `license.txt`, not GitHub's sidebar. Strong India/SMB footprint. |
| RosarioSIS | https://github.com/francoisjacquet/rosariosis | GPL-2.0 | 654 | K-12 school management; widely deployed in LATAM, Spanish/French/Portuguese localization in core. |
| Gibbon | https://github.com/GibbonEdu/core | GPL-3.0 | 638 | Flexible school management; strong in international K-12 schools. |
| openSIS Classic | https://github.com/OS4ED/openSIS-Classic | GPL (README) | 351 | Student information system; commercial editions available from OS4ED. |
| **GegoK12** | **https://github.com/Gego-K12/gegok12** | **MIT** | 56 | 🟢 **The first genuinely MIT school ERP/SIS in this base, and this pass is the one that put it on the shelf.** Laravel/PHP 8.4+, 123 commits, API-first with a mobile app. Covers student management, attendance, timetables and fees. 🔴 **The licence had to be read from the file: GitHub's classifier returns `NOASSERTION` because the `1,150 B` grant carries `<!-- SPDX-License-Identifier: MIT -->` on line 3 and curly quotes in the operative text.** Confirmed first-hand this pass — the file opens `MIT License`, SPDX `MIT`, *"Copyright (c) 2025 GegoSoft Technologies and GegoK12 Contributors."* 🔵 **Region: APAC** — `.env.example` ships `TIMEZONE = 'Asia/Kolkata'` and `config/app.php` resolves from it, which is a stronger placement signal than an owner profile because a deployer inherits it without choosing it. 🔴 **56 stars: this is a real but small project.** Vendor pages also market a cloud edition, so read the repo, not the marketing. |
| **SVWS-NRW** | **https://github.com/SVWS-NRW/SVWS-Server** | **BSD-3-Clause** | 42 | 🟢 **A state-government school-administration server, permissively licensed — new to this shelf this pass.** *Schulverwaltungssoftware Nordrhein-Westfalen*: the SIS the German state of **North Rhine-Westphalia** builds for its own schools, Java + TypeScript, **10,015 commits**. 🔵 **Region: EMEA.** 🔴 **The index reads `NOASSERTION`; BSD-3-Clause is stated in the README** (*"lizenziert unter der BSD 3-Clause Lizenz"*). 🟢 **Engagement reading: commit count says this is a maintained production system, not a pilot, and a BSD-3 grant on public-sector education software is rare enough to be the reason to look at EMEA public K-12 at all.** German-language domain model — budget for that, not for the licence. |
| **i-educar** | **https://github.com/portabilis/i-educar** | **GPL-2.0** | 725 | 🟢 **The largest free-software school-management system in Brazil, and the most-starred SIS in this table.** PHP/Laravel, **34,951 commits** on branch `2.12`, 555 forks; first built by the Itajaí (SC) city government and now deployed by municipalities across Brazil. 🔵 **Region: LATAM.** 🔴 **GPL-2.0 — copyleft, so this is a system a client self-hosts and you extend, not a tree a studio derives a product from.** Companion `i-diario` (AGPL-3.0) is the class-diary/attendance-and-grades surface from the same vendor. 🔴 **Correction recorded this pass: the trending log has claimed since `p667` that this row was "carried on the verticals shelf", and it was not — it had never been written to any shelf file.** |

🔴 **Agent surface across the SIS row, stated plainly because it decides which
client you can serve this quarter.** **OpenEduCat: yes**, via the Odoo
connectors above. **Frappe Education and Frappe LMS: unknown and worth one
search** — they sit on the Frappe framework, which is the next place to look for
the same generic-connector trick, and nobody has checked. **RosarioSIS
(PHP/Postgres) and Gibbon (PHP/MySQL): no agent interface and no generic
connector of the Odoo kind** — searched by project name this pass, nothing
returned. Those two are the genuinely unserved incumbents, and they are
precisely the ones that dominate **LATAM K-12** (RosarioSIS) and
**international K-12** (Gibbon). 🔴 **Amended this pass: naming
RosarioSIS as what dominates LATAM K-12 understated the field — `portabilis/i-educar`
is larger by stars, forks and commits and is deployed by Brazilian municipalities,
and it had never been written to this shelf.** 🔵 **Engagement reading: a LATAM K-12 client on
RosarioSIS is a build; a private-education or India/LATAM SMB client on
OpenEduCat is a configuration.**

🟢 **The licence picture of this table changed this pass, and it is the most
consequential thing on this page.** Every SIS row above used to be copyleft —
LGPL-3.0, GPL-3.0, GPL-2.0 — which meant the standing advice was *integrate,
never derive*. **`GegoK12` is MIT and `SVWS-NRW` is BSD-3-Clause.** Both are
small next to OpenEduCat or i-educar, so this is not a recommendation to replace
them; it is the first time a studio has **a permissive SIS tree it can actually
fork and ship** when the engagement calls for a product rather than an
integration. 🔵 **Placed: `GegoK12` → APAC, `SVWS-NRW` → EMEA, `i-educar` →
LATAM, OpenEduCat → APAC/LATAM SMB, RosarioSIS → LATAM, Canvas/Open edX →
North America.** 🔴 **Both permissive rows are under 60 stars; verify
maintenance before committing a client to either.**

## Open-core platforms — a real MIT grant over a commercial system of record (new, `p809`)

🔴 **Read this section before quoting any ibl.ai repository to a client.** The estate is
genuinely `MIT` — every payload below was fetched and hashed this pass — **and every
application in it is a front-end client whose backend is not in the repository and is
sold under an enterprise licence.** Both halves of that sentence are true at once, and
this base has twice come close to publishing only the first half.

| Platform | Repo | License (payload-verified) | Stars | What you actually get | What you do NOT get |
|---|---|---|---|---|---|
| ibl.ai SIS | https://github.com/iblai/sis | MIT (`1,089 B`, `969b7073d1c42ac2`) | 1 | Next.js 16 + Tauri 2 student information **front end**: students/staff directory, enrolment, grades & GPA, credentials, guardians, course runs, rosters, gradebook, terms/periods/rooms, reports, messaging, ⌘K palette. **4 languages** (en/es/fr/zh), native shells for macOS/Windows/Linux/iOS/Android. | 🔴 The system of record. README: *"a front end for the ibl.ai platform"*; *"If you need the full backend, reach out at ibl.ai/contact for an enterprise license."* Writes **no backend endpoints of its own**; sign-in goes to `login.iblai.app`; requires ibl.ai Data Manager + Open edX with ibl plugins + Studio. |
| ibl.ai LMS | https://github.com/iblai/lms | MIT (`1,063 B`, `f1269b7b2313456a`) | 95 | Skills-intelligence learning platform: course discovery, **skill-growth tracking, digital credentials, learning paths**, admin analytics, multi-tenant branding. `1,071` commits. 🟢 The closest open artefact in this base to the skills-first direction `T23` describes. | 🔴 README: *"To use this app, you need access to an ibl.ai backend instance"* — skills/course API, EdX delivery, auth, data platform, optional AI-mentor API. |
| ibl.ai OS | https://github.com/iblai/os | MIT (`1,070 B`, `13029f084e13d864`) | **638** | Agent platform: institution-defined agents bound to their own documents, multi-provider routing, voice, analytics, SSO, embeddable widgets. | 🔴 README: *"requires the ibl.ai backend platform for authentication, AI agent APIs, and data services"*, *"not included in this repository"*. |
| ibl.ai Ontology | https://github.com/iblai/ontology | MIT (`1,063 B`, `f1269b7b2313456a`) | 12 | 🟢 **The one piece of the estate that stands alone.** On-premise knowledge layer making **PeopleSoft, Snowflake, Canvas and Salesforce** queryable by agents **over MCP** — *"no data extraction, your data stays in your network"*. `97` commits. | — |

🔴 **Star correction carried into this file: `iblai/os` is `638★`. This base published
`821★`.** Measured from the rendered page, 2026-11-13.

🟢 **How to use this honestly in an engagement.** These are high-quality front ends under
a permissive grant — forking and white-labelling `sis` or `lms` is legitimate and fast.
🔴 **But the SIS gap in this base does not close here**, because the record these clients
display lives in a proprietary backend. If the client needs to own the system of record,
the open paths remain OpenEduCat-on-Odoo (LGPL-3.0 addons + `MIT`/`MPL-2.0` Odoo MCP
servers), or building on Frappe. Say which one you mean.

## Brightspace and Blackboard — the two incumbents this file had no agent surface for (new, `p809`)

🔴 **Both platforms were named repeatedly across this KB and carried zero connector
rows.** Corrected this pass. Neither vendor publishes an MCP server of its own (checked
2026-11-13), so **every path below is unofficial** — REST API, SSO session, or scraped
cookie — which is a contract question before it is an architecture one.

| Platform | Incumbent where | Open agent surface found | License | Stars |
|---|---|---|---|---|
| **D2L Brightspace** | Canadian & US higher ed, Dutch, Singaporean, Colombian institutions | https://github.com/RohanMuppa/brightspace-mcp-server — `29` tools, **read-only by declaration**, SSO + 2FA, OS keychain, AES-256-GCM session state | MIT | 67 |
| **D2L Brightspace** | — | https://github.com/JhostinAleck/brightspace-mcp — `29` tools (`26` read / `3` write), **two-opt-in write gate + `dry_run` + idempotency key + audit log**, 4 auth strategies, `es-419` locale | MIT | 16 |
| **Blackboard Learn** | LATAM private universities (UPC, UPN — Peru) | https://github.com/alejooroncoy/campus-cli — CLI **and** MCP server, `851` commits. 🔴 **Tools are brokered by a remote relay (`mcp.campuscli.com`)**: credentials cross a third party | ISC | 13 |
| **Blackboard Learn** | APAC (NTU Singapore) | https://github.com/kingdonkatsu/ntulearn-mcp — `8` tools. 🔴 Auth is a **`BbRouter` session cookie auto-read from the browser** | MIT | 4 |
| **Blackboard Learn (Ultra)** | Vendor-neutral | https://github.com/Mattlo0546/blackboard-mcp — read-only, university SSO, Python. 🔴 **`4` commits — reference only** | MIT | 1 |

## Admissions and enrolment CRM — where the permissive option is general-purpose, not educational

🟢 **New section at the twelfth pass (`p807`, 2026-11-13).** The prescribed
vertical-platform leg (`open source platform education ERP CRM MIT Apache`) has returned
this shelf's own contents for **eight consecutive passes**. 🔵 **This pass it returned
them again — but the shape of the nil is itself the finding, and it had never been
written down.**

🔴 **The structural fact: every education-specific ERP/CRM in the open is copyleft, and
every permissive ERP/CRM is general-purpose.** There is no MIT or Apache-2.0 system in
existence that ships an *education* admissions pipeline. The leg confirms it from the
other direction each time it runs — `OpenEduCat` (LGPL-3.0), `Frappe Education`
(GPL-3.0), `ERPNext` (GPL-3.0) on the education side; `Apache OFBiz`, `Corteza`,
`Krayin`, `Huly`, `iDURAR` on the permissive side, none of them educational.

🔵 **Why this matters more than it sounds.** Admissions and enrolment is **CRM-shaped
work, not SIS-shaped work** — pipelines, stages, campaigns, attribution, nurture — and a
studio that reaches for the SIS table above to serve it is reaching for the wrong tool
and inheriting copyleft for no reason. 🟢 **The correct move is a permissive general CRM
with an education domain model built on top**, which is a configuration exercise plus an
agent, not a platform build.

| Platform | Repo | License | Stars | Why it is the right base for education admissions |
|---|---|---|---|---|
| **Krayin CRM** | https://github.com/krayin/laravel-crm | **MIT** | 24.1k | 🟢 **The largest permissively licensed CRM this base has found, by a wide margin — `24.1k★`, `1.7k` forks.** Laravel/PHP, built for lead, customer and sales management; the lead→opportunity→stage model maps onto enquiry→application→offer→enrolment with no structural violence. 🔵 **MIT means a studio can fork it and ship an admissions product**, which is impossible anywhere on the SIS table except `GegoK12` (`56★`). 🔴 **Nothing in it is education-aware** — no applicant, programme, intake or qualification entity — so budget the domain model as net-new. 🟢 **Shares a stack with `i-educar` (PHP/Laravel), which makes a LATAM pairing unusually cheap.** |
| **Corteza** | https://github.com/cortezaproject/corteza | **Apache-2.0** | 2.2k | 🟢 **Low-code platform for data-driven business apps and workflows — Apache-2.0, `532` forks, not archived.** Where Krayin gives a CRM to bend, Corteza gives a **modeller**: define the admissions entities and the workflow, rather than inherit a sales one. 🔵 **The better choice when the institution's process is unusual** (multi-intake, competitive programmes, ministry reporting) and the worse choice when it is ordinary. 🟡 Materially smaller community than Krayin — read the release cadence before committing. |
| **Apache OFBiz** | https://github.com/apache/ofbiz-framework | **Apache-2.0** | 1.2k | 🟡 **Listed for completeness and with a caution.** Java enterprise automation spanning ERP, CRM, e-commerce, SCM and manufacturing, `764` forks. 🔴 **Its breadth is the problem, not the attraction** — an admissions pipeline uses a thin slice and pays the whole framework's learning curve. Reach for it only where the client already runs OFBiz. |

🔴 **Agent surface: none of the three ships one, and no MCP server for any of them was
found this pass.** 🟢 **That is a smaller obstacle here than on the SIS table**: all three
are API-first with conventional REST/GraphQL surfaces, so an MCP wrapper over an
admissions subset is days of work, not a connector project. See `compose/patterns.md`
`P21`.

🔵 **Placement, and one correction made before this page was written.** `Krayin`'s GitHub
organisation states its location as **India** → 🟢 **APAC-origin**, though the product is
deployment-neutral. 🔴 **`Corteza` was drafted here as "EMEA-origin (Slovenia)" from
recollection and that claim was withdrawn on checking:** the `cortezaproject` organisation
states its location as **"International"**, and `cortezaproject.org` is outside this
session's allowed network domains, so **no origin is asserted** → `Gap 807-D`. `OFBiz` is
an ASF project with no regional centre. 🟢 **None of the three carries a regional
constraint — unlike the SIS table, where the incumbent decides the region for you.**

## Content, delivery and classroom

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| Kolibri | https://github.com/learningequality/kolibri | **MIT** | 1.2k | Offline-first learning platform. The right base for low-connectivity deployments (rural LATAM, Sub-Saharan Africa, remote APAC). Permissive. |
| Oppia | https://github.com/oppia/oppia | **Apache-2.0** | 7.0k | Interactive lesson "explorations" with built-in misconception handling. Permissive and substantial. |
| H5P | https://github.com/h5p/h5p-php-library | GPL-3.0 | 155 | The de facto interactive-content format; renders inside Moodle, Canvas, Open edX. |
| Khan Perseus | https://github.com/Khan/perseus | **MIT** | 1.6k | Khan Academy's exercise editor/renderer. MIT — drop real exercise rendering into any product. |
| BigBlueButton | https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.3k | Virtual classroom with LTI into Moodle/Canvas; recordings feed transcript pipelines. |
| Opencast | https://github.com/opencast/opencast | ECL-2.0 | 511 | Lecture capture at scale — the upstream source for transcript/summarization agents. |
| Anki | https://github.com/ankitects/anki | AGPL-3.0 | 32.8k | Spaced-repetition scheduling; the algorithm is the asset for retention features. |

## Teaching, grading and learning-data infrastructure

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| JupyterHub | https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | Multi-user notebooks; the standard for CS/data-science teaching. |
| nbgrader | https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | Assignment release and autograding for notebooks. **The grading substrate to wrap an agent around.** |
| pyKT | https://github.com/pykt-team/pykt-toolkit | **MIT** | 461 | Deep knowledge-tracing benchmarks — real mastery estimation to pair with an LLM tutor. |
| ODK Collect | https://github.com/getodk/collect | Apache-2.0 | 805 | Offline Android form collection; used for education field assessment at national scale. |
| AI Scoring Platform | https://github.com/wwrwbs/AI_AWE | Apache-2.0 (README) | 2 | Essay scoring + label-aware feedback, locally deployable. Prototype scale, but the only open grading *system* found. |
| Numbas | https://github.com/numbas/Numbas | **Apache-2.0** | 217 | **New this pass (`p806`) — the largest permissively licensed education platform of EMEA origin in this base.** *"A completely browser-based e-assessment/e-learning system, with an emphasis on mathematics."* Built by **Newcastle University** (UK). This repo is the standalone **Python 3 compiler**; the authoring editor is `numbas/editor` in the same org. `130` forks. 🟢 **Apache-2.0 is the whole point of the row:** TAO is GPL-2.0 and every LMS in the table above is GPL or AGPL, so Numbas is the only assessment platform here a studio can fork, embed and ship inside a proprietary client deliverable. 🔵 Strongest fit is STEM formative assessment, where its maths-expression engine and randomised question generation are the differentiator — **not** a general item bank; pair with the QTI 3 player for interchange. 🔴 Promoted by audit — `39` mentions in the trending logs, never shelved. |
| TAO | https://github.com/oat-sa/tao-core | GPL-2.0 | 64 | **New this pass — the one assessment *platform* with real item banking that a client may already be running.** Long-standing open e-testing system. 🔴 **Two constraints decide whether it fits: the open-source edition is QTI 2.2-based, not QTI 3, and it ships no Results Management** — a QTI 3 contract or a reporting requirement lands outside it. GPL-2.0: a host to extend, not a base to embed. |
| QTI 3 item player | https://github.com/amp-up-io/qti3-item-player | **MIT** | 30 | **New this pass — the delivery surface for assessment, and the only QTI repo claiming conformance certification** (QTI 3 Basic *and* Advanced "Delivery"). 🔴 Vue 2.6, which is end-of-life. Pair with `LongsightGroup/qti3` (MIT) for authoring, scoring and migration — **no single repo does both**. |
| Caliper spec | https://github.com/1edtech/caliper-spec | IMS spec-document license | 22 | Learning analytics event spec. Implement it; do not vendor the repo. **Implementations now exist — see the two rows below and `repos/foundations.md`.** |
| caliper-ts | https://github.com/CarnegieLearningWeb/caliper-ts | **MIT** (read from `LICENSE`; sidebar shows only a generic link) | 0 | **New this pass — the only permissively licensed Caliper sensor found anywhere.** TypeScript Sensor API, Caliper **1.1**. 🔴 Published to the **GitHub Package Registry** as `@imaginelearning/caliper-ts`, not public npm, and 0 stars — budget to carry it. |
| Moodle Caliper logstore | https://github.com/open-lms-open-source/moodle-logstore_caliper | GPL-3.0 | 1 | **New this pass — the only Caliper emitter for a real LMS, at any licence.** Moodle logstore plugin: Expander → Translator → Emitter, immediate or batched, Moodle **2.7+**. 🟢 GPL-3.0 is correct for a Moodle plugin and does **not** reach a separately deployed MIT/Apache AI layer. |

## Standards that make the above interchangeable

| Standard | Why it decides the architecture |
|---|---|
| **LTI 1.3 / LTI Advantage** | Build the AI tool once as an LTI tool provider and it mounts in Moodle, Canvas, Open edX, Sakai, and ILIAS. Highest-leverage single investment in an education engagement — and `ltijs` means you do not write it from scratch. |
| **Ed-Fi** 🆕 | 🔴 **The standard this base missed for eleven passes.** The US K-12 data-interoperability model that **state education agencies** run their reporting on. It decides the architecture of any North American K-12 engagement, because an agent that speaks Ed-Fi reaches a *state*, not a school — while an agent that speaks one SIS reaches one district. 🟢 **Permissively implemented and deployable today:** `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` (Apache-2.0, v7.x) and `Ed-Fi-Alliance-OSS/Data-Management-Service` (Apache-2.0, **v8 — build against this one**). 🔴 **There is no Ed-Fi MCP server anywhere in this base and none was found: the agent edge is unbuilt (`Gap 806-A`), and it is a build that must be priced as one.** Region: **North America**. |
| **xAPI** | Learner-activity telemetry; what an agent should emit so the institution can report on it. |
| **Caliper Analytics** | The 1EdTech-native alternative to xAPI; common in North American higher ed. **Updated fifth pass: six implementations now verified — an MIT sensor, a GPL-3.0 Moodle emitter, an Apache-2.0 analysis layer and LGPL-3.0 reference sensors — but NO permissively licensed event store, and 1EdTech's reference code is member-gated.** Free choice → still xAPI. Contract names Caliper → you write the store and nothing else. Ask which Caliper **version**: the only 1.2 implementation found is unlicensed. |
| **QTI** | Assessment item interchange — matters as soon as item banks must move between systems. **Updated fifth pass: seven implementations verified, five of them MIT — but scoring, item banking and *certified delivery* live in different repos, so every QTI engagement is a pairing exercise.** `qti3-item-player` (MIT) is certified delivery-only; `LongsightGroup/qti3` (MIT) authors, scores and migrates but claims no certification. 🔴 Confirm which **branch** a QTI licence was read from: `Learnosity/learnosity-qti` is MIT on `master` and GPL-2.0 on its default `develop`. |
| **SCORM** | Legacy but ubiquitous in corporate and vocational training; still the delivery format many EMEA/APAC clients require. |

## Declared gaps

- 🔴 **`Gap 806-A` — no Ed-Fi agent interface exists, and this is the best-shaped
  contribution opportunity in this file.** Ed-Fi is Apache-2.0, exposes a conventional
  REST API with a published specification, and reaches US state education agencies
  rather than single districts. Every ingredient for an MCP server over it is already
  on a shelf in this KB: the spec, the Apache-2.0 reference implementation, and **three
  independent MIT write-gating designs** to copy from `agents/top.md`
  (`che-ntucool-mcp`'s elicitation-plus-single-use-token, `waseda-moodle-mcp`'s
  `prepare_*`/`confirm_action` split, `Smartschool-MCP`'s read-only posture). 🔵 **The
  gating design is not optional here** — a write path into a state longitudinal data
  system is the highest-consequence write surface in this entire knowledge base.

- **No permissively licensed LMS at deployment scale** except Sakai. Surface
  this constraint in week one of any engagement that needs a proprietary
  derived platform.
- **MCP coverage is no longer absent for Moodle — it is fragmented.** Seven
  Moodle MCP servers verified, 1–206 stars, licenses split MIT/GPL/AGPL, and no
  two agree on tool surface or auth model (web-service token vs interactive
  browser SSO vs companion plugin). Canvas, by contrast, has consolidated on
  one 324-star MIT server. **Open edX remains the real gap**: `openedx-mcp`
  (AGPL-3.0, 3 stars) is the only option and it is reference-grade at best.
- 🟢 **SIS MCP: CLOSED for OpenEduCat, corrected again 2026-11-13 (fifth
  pass).** The fourth-pass correction below said SIS servers exist "but not for
  any SIS in this table." **That is now withdrawn too.** OpenEduCat **is in this
  table** and is reachable by a generic Odoo MCP server (`erpipe-org/mcp-odoo`,
  MIT, 433★; `ivnvxd/mcp-server-odoo`, MPL-2.0, 415★), because it is Odoo addons
  and those servers address models by name. 🔴 **Architecturally verified, not
  run (`Gap 286`).** What stays true: **RosarioSIS and Gibbon have neither an
  agent interface nor a generic connector** — they are the unserved rows, and
  they are the LATAM K-12 and international K-12 incumbents respectively.
  🔵 **The method worth institutionalising: when a vertical system has no agent
  surface, check the general-purpose platform underneath it.**
- **SIS MCP servers exist — but not for any SIS in this table. Superseded by the
  bullet above; kept for the record (fourth pass).** The previous three editions of this file said "no
  MCP server for any SIS" and called it a confirmed absence. That claim was
  **over-generalized and is now withdrawn.** Two verified MCP servers do reach a
  student information system: `oliverhruby/edupage-mcp` (MIT, 4 stars, **31
  tools**) over **EduPage**, the SIS used across Slovakia and Czechia, and
  `sukhrobyangibaev/mcp_hemis_student` (MIT, 0 stars) over **HEMIS**, the
  higher-education SIS used by Uzbek universities. **What remains true, and is
  the sharper statement:** OpenEduCat, RosarioSIS, Gibbon, openSIS and
  `frappe/education` — every *open-source* SIS in this table — still have **no**
  agent interface. The integration is happening against **national proprietary
  SIS products with captive markets**, built by individual developers, not
  against the open-source platforms a studio would deploy. Two consequences for
  an engagement: the topology is proven (so `P8` is no longer greenfield), and
  **EduPage's server reaches the SIS through a community library on undocumented
  endpoints** — a pattern to learn from, not a dependency to ship.
- **The learning-record store, by contrast, is now solved and permissive.** New
  this pass: `yetanalytics/lrsql` (Apache-2.0, 144) and `openfun/ralph` (MIT,
  51) as LRS implementations, with `DavidLMS/learnmcp-xapi` (MIT, 16) as the
  agent interface. **An LRS is not an SIS** — it holds learning *activity*, not
  the student record — so this closes the telemetry gap and leaves the advising
  gap exactly where it was.
