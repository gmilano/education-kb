---
industry: education
region: Global
updated: 2026-10-21
---

# Education — foundational repos

The systems an education engagement starts *from*, rather than the agents it adds on
top. Every row verified first-hand **2026-10-21**: liveness and default branch via
`git ls-remote --symref`, licence **read from the payload**.

**Read the default-branch column.** Education infrastructure is old software. Of the
grants on this shelf, a large share live on `master`, `develop`, `release` or a
version branch — not `main`. A tool that assumes `main` will report a live,
correctly-licensed repository as grantless. That has happened on this base before.

---

## Learning platforms (LMS / VLE)

| Platform | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Open edX LMS + Studio | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | `master/LICENSE` | **8 205** | North America |
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | `main/COPYING.txt` — 🔴 no `LICENSE` file exists | **7 507** | Global |
| Canvas LMS | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | `master/LICENSE` | **6 879** | North America |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | `develop/license.txt` — 🔴 (lower-case) | **3 328** | APAC |
| ClassroomIO | [classroomio/classroomio](https://github.com/classroomio/classroomio) | AGPL-3.0 | `main/LICENSE` | **1 726** | Global |
| Kolibri | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | `develop/LICENSE` | **1 159** | Global |
| Tutor (Open edX distro) | [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 | `release/LICENSE.txt` | **1 128** | Global |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | `master/LICENSE` | **1 016** | EMEA |
| Moodle App (mobile) | [moodlehq/moodleapp](https://github.com/moodlehq/moodleapp) | 🟢 **Apache-2.0** | 🔴 `main/COPYING.txt` | **1 002** | Global |
| Sakai | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | `master/LICENSE` | not re-derived | North America |
| OpenOLAT | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | `master/LICENSE` | not re-derived | EMEA |
| ELMS Learning Network | [elmsln/elmsln](https://github.com/elmsln/elmsln) | GPL-3.0 | `master/LICENSE.md` | **253** | North America |

🟢 **The two permissive platform rows matter disproportionately.** `OpenOLAT`
(Apache-2.0) and `kolibri` (MIT) are the only full platforms here that can be
embedded in a closed client deliverable without copyleft reach. And
`moodlehq/moodleapp` is **Apache-2.0 while Moodle core is GPL-3.0** — the mobile
client can be forked into proprietary work where the server cannot.

## Interoperability — LTI, SCORM, xAPI, Caliper

The layer that lets an agent talk to a client's existing LMS without a bespoke
connector. Almost entirely permissive, which is why this tier is the cheapest place
to start.

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Tsugi (LTI tool host) | [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | Apache-2.0 | `master/LICENSE` | **376** | North America |
| scorm-again (SCORM runtime) | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** | `master/LICENSE` | **356** | Not placed |
| Marsha (LTI LCMS) | [openfun/marsha](https://github.com/openfun/marsha) | **MIT** | `master/LICENSE` | **150** | EMEA |
| ltijs (LTI 1.3, Node) | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0 | `master/LICENSE` | not re-derived | Not placed |
| pylti1.3 (LTI 1.3, Python) | [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** | `master/LICENSE` | not re-derived | Not placed |
| lti-tool | [lti-tool/lti-tool](https://github.com/lti-tool/lti-tool) | **MIT** | `main/LICENSE` | not re-derived | Not placed |
| ltikit-sdk | [Liberate-Labs/ltikit-sdk](https://github.com/Liberate-Labs/ltikit-sdk) | **MIT** | `main/LICENSE` | not re-derived | Not placed |
| django-lti-toolbox | [openfun/django-lti-toolbox](https://github.com/openfun/django-lti-toolbox) | **MIT** | `master/LICENSE` | not re-derived | EMEA |
| CACCL (Canvas app framework) | [harvard-edtech/caccl](https://github.com/harvard-edtech/caccl) | **MIT** | `main/LICENSE.md` | not re-derived | North America |
| ltiauthenticator | [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | BSD-3-Clause | `main/LICENSE` | **73** | North America |
| Caliper analytics spec | [1EdTech/caliper-spec](https://github.com/1EdTech/caliper-spec) | 🔴 **IMS specification licence — NOT OSI** | `master/LICENSE.md` | not re-derived | North America |

## Assessment, integrity and accessibility

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Judge0 (code execution API) | [judge0/judge0](https://github.com/judge0/judge0) | GPL-3.0 | `master/LICENSE` | **4 491** | EMEA |
| Dolos (plagiarism detection) | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | `main/LICENSE` | **353** | EMEA |
| INGInious (exercise assessment) | [INGInious/INGInious](https://github.com/INGInious/INGInious) | AGPL-3.0 (*"most of the files"*) | `main/LICENSE` | **243** | EMEA |
| UDOIT (accessibility inspection) | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | GPL-3.0 | `main/LICENSE` | **117** | North America |
| Ares2 (secure grading runner) | [ls1intum/Ares2](https://github.com/ls1intum/Ares2) | **MIT** | `main/LICENSE` | not re-derived | EMEA |
| autograder | [zmievsa/autograder](https://github.com/zmievsa/autograder) | GPL-3.0 | `main/LICENSE` | not re-derived | Not placed |

## Code execution, online judges and autograding — 🆕 a whole tier this base did not have

🟢 **This tier is `p356`'s finding and it is the largest single supply discovery on
this base.** `p354` recovered [`judge0`](https://github.com/judge0/judge0) by aiming a
leg at a **function** instead of at "AI education". `ACTION ZZ-ay` asked for that leg
shape to be run across nine functions. The `"online judge"` leg alone returned **62
repositories, 12 of them verified here, and all 12 absent from this base's entire
corpus** — `archive/` and `evidence/` included — with **7 137 ★** at the head.

🔵 **Why twelve passes of agent-shaped queries could not see it.** This software is
not called an AI tool and does not describe itself as one. It is the **grading
execution substrate** underneath every programming course: a sandbox, a queue, a
verdict. An education engagement that has to run student code needs exactly this and
would otherwise build it.

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| Hydro (multi-tenant judge) | [hydro-dev/Hydro](https://github.com/hydro-dev/Hydro) | AGPL-3.0 | `master/LICENSE` | **7 137** | APAC |
| QingdaoU OnlineJudge | [QingdaoU/OnlineJudge](https://github.com/QingdaoU/OnlineJudge) | 🟢 **MIT** | `master/LICENSE` | **6 552** | APAC |
| HUSTOJ | [zhblue/hustoj](https://github.com/zhblue/hustoj) | GPL-2.0 | `master/LICENSE` | **3 813** | APAC |
| DMOJ (judge + contest platform) | [DMOJ/online-judge](https://github.com/DMOJ/online-judge) | AGPL-3.0 | `master/LICENSE` | **1 194** | North America |
| online-judge-tools | [online-judge-tools/oj](https://github.com/online-judge-tools/oj) | 🟢 **MIT** | `master/LICENSE` | **1 172** | APAC |
| DMOJ judge-server | [DMOJ/judge-server](https://github.com/DMOJ/judge-server) | AGPL-3.0 | `master/LICENSE` | **981** | North America |
| NOJ | [ZsgsDesign/NOJ](https://github.com/ZsgsDesign/NOJ) | 🟢 **MIT** | `master/LICENSE` | **942** | APAC |
| HOJ | [HimitZH/HOJ](https://github.com/HimitZH/HOJ) | 🟢 **MIT** | `master/LICENSE` | **942** | APAC |
| SYZOJ | [syzoj/syzoj](https://github.com/syzoj/syzoj) | 🟢 **MIT** | `master/LICENSE` | **923** | APAC |
| SDUOJ (microservices) | [SDUOJ/OnlineJudge](https://github.com/SDUOJ/OnlineJudge) | AGPL-3.0 | `main/LICENSE` | **556** | APAC |
| QingdaoU Judger (seccomp sandbox) | [QingdaoU/Judger](https://github.com/QingdaoU/Judger) | 🟢 **MIT** | 🔴 `newnew/LICENSE` | **496** | APAC |
| Sharif Judge (course-oriented) | [mjnaderi/Sharif-Judge](https://github.com/mjnaderi/Sharif-Judge) | AGPL-3.0 | 🔴 `Version-1/LICENSE` | **395** | EMEA |
| Otter-Grader (notebook autograder) | [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** | `master/LICENSE` | **161** | North America |
| webtech autograder | [webtech-network/autograder](https://github.com/webtech-network/autograder) | 🟢 **Apache-2.0** | `main/LICENSE` | **62** | Not placed |
| OK client (Berkeley autograder) | [okpy/ok-client](https://github.com/okpy/ok-client) | 🟢 **Apache-2.0** | `master/LICENSE` | **57** | North America |

🟢 **Read the licence column as the engagement decision.** Six of the fifteen are
**MIT, BSD-3-Clause or Apache-2.0** — [`QingdaoU/OnlineJudge`](https://github.com/QingdaoU/OnlineJudge)
at 6 552 ★ is a **complete, MIT-licensed, Docker-deployable judge**, and
[`QingdaoU/Judger`](https://github.com/QingdaoU/Judger) is its seccomp sandbox on its
own MIT grant. 🔵 Against this, `judge0` (GPL-3.0) has to be consumed over its API to
keep the boundary. **The permissive option in this tier is the bigger one**, which
reverses the assumption the `judge0`-only shelf implied one pass ago.

🟡 **Two of the three non-contest rows matter most for a client.**
[`mjnaderi/Sharif-Judge`](https://github.com/mjnaderi/Sharif-Judge) is built for
**programming courses** rather than contests — assignments, deadlines, per-student
feedback — and [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader)
grades **Python *and* R notebooks**, which is where this base's prior autograder
([`nbgrader`](https://github.com/jupyter/nbgrader), Jupyter-only) stopped.

🔴 **Two default branches in this tier are neither `main` nor `master`.**
`QingdaoU/Judger` defaults to **`newnew`** and `Sharif-Judge` to **`Version-1`**. A
licence sweep that probes `main` and `master` reports both as grantless, and one of
them is the MIT sandbox this tier's permissive path depends on.

## Content authoring, media and delivery

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| JupyterHub | [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | BSD-3-Clause | `main/LICENSE` | **8 361** | North America |
| BigBlueButton | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | `v4.0.x-develop/LICENSE` | not re-derived | North America |
| pytogether (collaborative IDE) | [SJRiz/pytogether](https://github.com/SJRiz/pytogether) | **MIT** | `main/LICENSE` | **261** | Not placed |
| Opencast (lecture capture) | [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** | `develop/LICENSE` | not re-derived | EMEA |
| H5P core | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | `master/LICENSE.txt` | not re-derived | EMEA |
| H5P CLI | [h5p/h5p-cli](https://github.com/h5p/h5p-cli) | 🟢 **MIT** | `master/LICENSE` | not re-derived | EMEA |
| Hyperbook | [openpatch/hyperbook](https://github.com/openpatch/hyperbook) | **MIT** | `main/LICENSE.md` | not re-derived | EMEA |
| yanki (markdown → Anki) | [kitschpatrol/yanki](https://github.com/kitschpatrol/yanki) | 🟡 **MIT, `package.json` only** | `main/package.json` — 🔴 *no licence file in tree* | not re-derived | Not placed |

🟢 **H5P is a split grant worth knowing:** the core library is GPL-3.0 but
[`h5p/h5p-cli`](https://github.com/h5p/h5p-cli) is **MIT**. Tooling built against
the CLI carries no copyleft; code linked into the library does.

## Administration — SIS, ERP, credentials

| Component | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| OpenEduCat (education ERP) | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | `19.0/LICENSE` | not re-derived | APAC |
| RosarioSIS (student info system) | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | `mobile/LICENSE` | not re-derived | EMEA |
| Learner Credential Wallet | [openwallet-foundation-labs/learner-credential-wallet](https://github.com/openwallet-foundation-labs/learner-credential-wallet) | **MIT** | `main/LICENSE` | not re-derived | Global |
| Terracotta (in-LMS experiments) | [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | Apache-2.0 | `development/LICENSE` | not re-derived | North America |
| 🆕 openSIS Classic (K-12 SIS) | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | GPL-2.0 | 🔴 `master/docs/License.txt` — **root carries no grant file** | **346** | Not placed |
| 🆕 FenixEdu Academic (HE SIS) | [FenixEdu/fenixedu-academic](https://github.com/FenixEdu/fenixedu-academic) | LGPL-3.0 | `master/LICENSE` | **175** | EMEA |

🟢 **`openSIS-Classic`'s grant was RECOVERED this pass, and `p354` predicted the exact
shape.** Six root rungs (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`,
`license.txt`, `GNU-AGPL-3.0.txt`) all answer **404**; the README names
`docs/License.txt`, and that path returns **17 286 bytes of GPL-2.0, BOM-prefixed**.
🔴 **Two corrections ride on reading it rather than the README:** the README says only
*"the GNU General Public License"* with no version, and the payload is **Version 2, not
Version 3** — which decides compatibility — while the leading **UTF-8 BOM** means a
classifier anchored on `^GNU` sees no match at all.

## Curriculum corpora and open courseware

| Asset | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region |
| --- | --- | --- | --- | ---: | --- |
| freeCodeCamp | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | BSD-3-Clause | `main/LICENSE.md` | **457 604** | North America |
| Open Source Society CS | [ossu/computer-science](https://github.com/ossu/computer-science) | **MIT** | `master/LICENSE` | **210 179** | Global |
| MCP for Beginners | [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) | **MIT** | `main/LICENSE` | **17 485** | North America |
| openunivcourses | [kabartay/openunivcourses](https://github.com/kabartay/openunivcourses) | **MIT** | `main/LICENSE` | **253** | Not placed |
| elimu.ai literacy webapp | [elimu-ai/webapp](https://github.com/elimu-ai/webapp) | **MIT** | `main/LICENSE` | not re-derived | EMEA |
| UIUC systems coursebook | [cs341-illinois/coursebook](https://github.com/cs341-illinois/coursebook) | 🔴 **NCSA** (code) + **CC-BY-4.0** (built PDFs) | `master/LICENSE/README.md` — 🔴 🔴 **`LICENSE/` is a DIRECTORY** — see `LICENSE/README.md` | not re-derived | North America |

🔴 **`cs341-illinois/coursebook` is this shelf's sharpest grant trap.** `LICENSE` is
not a file, it is a **directory**. Inside, `LICENSE/README.md` states three different
grants: NCSA for code contributions (`LICENSE.code`), CC-BY-4.0 for the generated
PDFs, and the original wikibook's licence for remixed material (`LICENSE.original`).
A previous pass on this base published this row as **MIT**. It is not MIT. NCSA is
permissive and usable, but it must be named correctly.

---

## Carried inventory — re-verified this pass, not promoted to the tiers above

🟢 **72 addresses, every one re-probed first-hand 2026-10-21 and every one ALIVE.** These
were held on this base's shelves from earlier passes. This pass's rewrite of the curated
tiers would have dropped them, and the `fold-identity` gate caught it — so rather than
lose verified work, they are restored here with their grants **re-read from the payload
today**, not carried on trust.

🔴 **20 of the 72 carry no grant file at the repository root on the default branch.**
Absent a licence, the default is all-rights-reserved: these are **not** usable in client
work however public the code is. Most are research artefacts from the OpenEduHub estate.

**OpenEduHub / WirLernenOnline — the largest single open-education engineering estate found on this base (EMEA, Germany)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [openeduhub/duplicate-detection](https://github.com/openeduhub/duplicate-detection) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/edu-sharing-python-client](https://github.com/openeduhub/edu-sharing-python-client) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/its-data](https://github.com/openeduhub/its-data) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/its-jointprobability](https://github.com/openeduhub/its-jointprobability) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/its-prep](https://github.com/openeduhub/its-prep) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/its-qna](https://github.com/openeduhub/its-qna) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/ki-prompt-benchmark](https://github.com/openeduhub/ki-prompt-benchmark) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/lernpfadeditor](https://github.com/openeduhub/lernpfadeditor) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/llm-judge](https://github.com/openeduhub/llm-judge) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/mappings](https://github.com/openeduhub/mappings) | GPL-3.0 | `main/LICENSE` |
| [openeduhub/metadata-agent-api](https://github.com/openeduhub/metadata-agent-api) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/metadata-agent-canvas](https://github.com/openeduhub/metadata-agent-canvas) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/metadata-browser-plugin-fuerapi](https://github.com/openeduhub/metadata-browser-plugin-fuerapi) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/metalookup](https://github.com/openeduhub/metalookup) | GPL-3.0 | `main/LICENSE.txt` |
| [openeduhub/oeh-metadata-vocabs](https://github.com/openeduhub/oeh-metadata-vocabs) | CC | `master/LICENSE` |
| [openeduhub/oeh-search-etl](https://github.com/openeduhub/oeh-search-etl) | 🔴 **no grant at root** | `master/` — none found |
| [openeduhub/oeh-search-frontend](https://github.com/openeduhub/oeh-search-frontend) | 🔴 **no grant at root** | `develop/` — none found |
| [openeduhub/python-kidra](https://github.com/openeduhub/python-kidra) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/skohub-vocabs-oeh-patched](https://github.com/openeduhub/skohub-vocabs-oeh-patched) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/text-extraction](https://github.com/openeduhub/text-extraction) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/text-statistics](https://github.com/openeduhub/text-statistics) | GPL-3.0 | `main/LICENSE` |
| [openeduhub/topic-statistics](https://github.com/openeduhub/topic-statistics) | 🔴 **no grant at root** | `main/` — none found |
| [openeduhub/tutor-chatbot](https://github.com/openeduhub/tutor-chatbot) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/wlo-quellenliste](https://github.com/openeduhub/wlo-quellenliste) | **Apache-2.0** | `main/LICENSE` |
| [openeduhub/z-api-runner](https://github.com/openeduhub/z-api-runner) | 🔴 **no grant at root** | `master/` — none found |

**Open edX ecosystem (North America)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [openedx/frontend-base](https://github.com/openedx/frontend-base) | AGPL-3.0 | `main/LICENSE` |
| [openedx/frontend-platform](https://github.com/openedx/frontend-platform) | AGPL-3.0 | `master/LICENSE` |
| [openedx/openedx-proposals](https://github.com/openedx/openedx-proposals) | CC | `master/LICENSE` |

**France Université Numérique (EMEA, France)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [openfun/ashley](https://github.com/openfun/ashley) | **MIT** | `master/LICENSE` |
| [openfun/potsie](https://github.com/openfun/potsie) | **MIT** | `main/LICENSE.md` |

**D2L Brightspace, first-party (North America)**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [Brightspace/test-reporting-node](https://github.com/Brightspace/test-reporting-node) | **Apache-2.0** | `main/LICENSE` |
| [BrightspaceUI/core](https://github.com/BrightspaceUI/core) | **Apache-2.0** | `main/LICENSE` |
| [BrightspaceUI/intl](https://github.com/BrightspaceUI/intl) | **Apache-2.0** | `main/LICENSE` |
| [BrightspaceUI/labs](https://github.com/BrightspaceUI/labs) | **Apache-2.0** | `main/LICENSE` |

**LTI libraries, additional**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [adamzammit/ltiplugin](https://github.com/adamzammit/ltiplugin) | GPL-3.0 | `master/LICENSE` |
| [annoto/ims-lti](https://github.com/annoto/ims-lti) | **MIT** | `master/LICENSE` |
| [godmartinz/node-lti-1.3-library](https://github.com/godmartinz/node-lti-1.3-library) | 🔴 **no grant at root** | `master/` — none found |
| [longsightgroup/lti-tool](https://github.com/longsightgroup/lti-tool) | **MIT** | `main/LICENSE` |
| [scormflow/scorm-engine-client](https://github.com/scormflow/scorm-engine-client) | **MIT** | `main/LICENSE` |

**Curriculum knowledge graphs**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [mizcausevic-dev/curriculum-knowledge-graph](https://github.com/mizcausevic-dev/curriculum-knowledge-graph) | **MIT** | `main/LICENSE` |
| [oseducation/knowledge-graph](https://github.com/oseducation/knowledge-graph) | 🔴 **no grant at root** | `main/` — none found |
| [razi-03/ncert-ckg](https://github.com/razi-03/ncert-ckg) | 🔴 **no grant at root** | `main/` — none found |

**Privacy, de-identification and synthetic data — the compliance toolkit for education data**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [arx-deidentifier/arx](https://github.com/arx-deidentifier/arx) | **Apache-2.0** | `master/LICENSE` |
| [greenmaskio/greenmask](https://github.com/greenmaskio/greenmask) | **Apache-2.0** | `main/LICENSE` |
| [hitsz-ids/synthetic-data-generator](https://github.com/hitsz-ids/synthetic-data-generator) | **Apache-2.0** | `main/LICENSE` |
| [meta-pytorch/opacus](https://github.com/meta-pytorch/opacus) | **Apache-2.0** | `main/LICENSE` |
| [OpenMined/PyDP](https://github.com/OpenMined/PyDP) | **Apache-2.0** | `dev/LICENSE` |
| [rizzo-ai-academy/rizzo-pii](https://github.com/rizzo-ai-academy/rizzo-pii) | **MIT** | `main/LICENSE` |
| [securitybunker/databunker](https://github.com/securitybunker/databunker) | **MIT** | `master/LICENSE` |
| [synthetichealth/synthea](https://github.com/synthetichealth/synthea) | **Apache-2.0** | `master/LICENSE` |
| [thoughtbot/top_secret](https://github.com/thoughtbot/top_secret) | **MIT** | `main/LICENSE.txt` |

**Courseware and curriculum corpora, additional**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [freeCodeCamp/curriculum-helpers](https://github.com/freeCodeCamp/curriculum-helpers) | **BSD** | `main/LICENSE` |
| [h5p/h5p-interactive-video](https://github.com/h5p/h5p-interactive-video) | 🔴 **no grant at root** | `master/` — none found |
| [openki/openki](https://github.com/openki/openki) | AGPL-3.0 | `dev/LICENSE` |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | **MIT** | `main/LICENSE` |
| [weecology/forecasting-course](https://github.com/weecology/forecasting-course) | CC | `main/LICENSE.md` |

**Learning agents, tutors and tooling, additional**

| Repo | Licence (payload) | Grant read at |
|---|---|---|
| [010ankushsharma/adaptalearn](https://github.com/010ankushsharma/adaptalearn) | 🔴 **no grant at root** | `master/` — none found |
| [chrischall/gogcli-mcp](https://github.com/chrischall/gogcli-mcp) | **MIT** | `main/LICENSE` |
| [christophblessing/quiz-recap](https://github.com/christophblessing/quiz-recap) | **MIT** | `main/LICENSE` |
| [damphuquy/agent-as-a-tutor](https://github.com/damphuquy/agent-as-a-tutor) | **MIT** | `main/LICENSE` |
| [dymchenkko/claude-study-agent](https://github.com/dymchenkko/claude-study-agent) | **MIT** | `main/LICENSE` |
| [groton-school/canvas-cli](https://github.com/groton-school/canvas-cli) | GPL-3.0 | `main/LICENSE` |
| [ibenian/algebench](https://github.com/ibenian/algebench) | **MIT** | `main/LICENSE` |
| [kyyota-wang/cloverailab](https://github.com/kyyota-wang/cloverailab) | 🔴 **no grant at root** | `main/` — none found |
| [lucasspinola/assistentes-educacionais-com-ia](https://github.com/lucasspinola/assistentes-educacionais-com-ia) | **MIT** | `main/LICENSE` |
| [molecule-dev/molecule](https://github.com/molecule-dev/molecule) | **Apache-2.0** | `main/LICENSE` |
| [mthatipamula/educational-assessment-ai-agent-platform](https://github.com/mthatipamula/educational-assessment-ai-agent-platform) | 🔴 **no grant at root** | `main/` — none found |
| [muhammedalakbarli/imparo](https://github.com/muhammedalakbarli/imparo) | **MIT** | `main/LICENSE` |
| [nichochar/ari](https://github.com/nichochar/ari) | **MIT** | `main/LICENSE` |
| [risnake/canvas-mcp-server](https://github.com/risnake/canvas-mcp-server) | 🔴 **no grant at root** | `main/` — none found |
| [smashburger-dev/argmin](https://github.com/smashburger-dev/argmin) | **MIT** | `main/LICENSE` |
| [viendinhcom/supermemo](https://github.com/viendinhcom/supermemo) | **MIT** | `master/LICENSE` |

---

## 🟢 Alias correction applied this pass

[`openedx/edx-platform`](https://github.com/openedx/edx-platform) and
[`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) return the
**identical HEAD** `7f01c42157d30cc273c06d62448b6d5a26624495`. They are one
repository. The authenticated index returns **`openedx/openedx-platform`** as the
canonical name; this base has been publishing the stale one. The table above now
carries the canonical address.

## 🔵 Grant-path distribution, re-derived AFTER this pass wrote — which is what `gate-census-currency` is for

🟢 Derived over the curated tiers of **this** tree, as the last act before the commit,
not carried from `p355`'s sentence:

| Grant filename | Rows on this shelf |
|---|---:|
| `LICENSE` | 51 |
| `LICENSE.md` | 5 |
| 🔴 `COPYING.txt` | 2 — `moodle/moodle`, `moodlehq/moodleapp` |
| `LICENSE.txt` | 2 |
| 🔴 `license.txt` (lower-case) | 1 — `frappe/lms` |
| 🔴 a **directory** | 1 — `cs341-illinois/coursebook` |
| 🔴 `package.json` field only | 1 — `kitschpatrol/yanki` |
| 🔴 🆕 **`docs/License.txt`** | 1 — `OS4ED/openSIS-Classic` |

**13 of 64 grants (20.3 %) are not at `LICENSE`.** 🔴 **The share went UP, not down, as
the shelf grew** — `p355` published 6 of 41 (15 %) and this pass added rows that are
*older* software, which is the direction `T13` predicts.

### 🔴 And the default branch is the larger hazard

| Default branch | Rows |
|---|---:|
| `master` | **31** |
| `main` | 23 |
| `develop` | 3 |
| 🔴 each of `release`, `newnew`, `Version-1`, `v4.0.x-develop`, `19.0`, `mobile`, `development` | 1 |

🔴 **A probe that assumes `main` reports 41 of 64 grants (64.1 %) as absent**, and a
probe that tries `main` then `master` still misses **10**. Two of those ten are
[`QingdaoU/Judger`](https://github.com/QingdaoU/Judger) (`newnew`) and
[`mjnaderi/Sharif-Judge`](https://github.com/mjnaderi/Sharif-Judge) (`Version-1`), both
added this pass — and the first is the MIT sandwich at the centre of Pattern 9's
permissive path. 🔵 One cause explains copyleft prevalence, grants at `COPYING.txt` and
`docs/License.txt`, and non-`main` defaults alike: **this sector's infrastructure is
older than the conventions the tooling assumes.** Published as `T13`.

## 🔵 Regional placement, counted over this shelf's own cells

🟢 **Derived as the last act before the commit, and it corrects the sentence it
replaces.**

| Region | Placed rows | `p355` published |
|---|---:|---:|
| **North America** | **19** | 🔴 11 |
| **EMEA** | **16** | 🔴 12 |
| **APAC** | **11** | 🔴 2 |
| Global | **7** | 🔴 6 |
| 🔵 Not placed | 11 | — |
| **LATAM** | **0** | 0 |

🔴 **Every figure in the right-hand column was wrong, and only the LATAM zero was
right.** Four of the five gaps predate this pass: before `p356` added a single row this
shelf carried **15** North American and **14** EMEA rows against published figures of
11 and 12. 🔵 **This is `ACTION ZZ-aw` on a third and fourth quantity** — a
*distribution* in prose, unbound by any gate, wrong on both shelves this pass audited
(`agents/top.md` was off by one on North America). The remedy is not care; it is a gate.

- **North America** leads at 19, concentrated in platforms, standards and — new this
  pass — **university autograding**: `otter-grader` (BSD-3-Clause, UC Berkeley, named in
  its own licence payload), `okpy/ok-client` (Apache-2.0, Berkeley) and the two DMOJ
  rows, placed by **`dmoj.ca` appearing ten times in their README**.
- **EMEA** holds 16: European universities built most of the open assessment, media and
  interoperability tooling (Belgium ×2, Croatia, France, Germany, Italy, Norway,
  Switzerland, Spain, Tanzania) and now **Iran** (`Sharif-Judge`, Sharif University of
  Technology) and **Portugal** (`fenixedu-academic`, Instituto Superior Técnico).
- **APAC** rises from 2 to **11** in one pass, and all nine new rows are **online judges
  and sandboxes** from Chinese and Japanese universities. 🔵 This is the repository-side
  half of `T15`: the region the prose legs cannot measure is the region building the
  infrastructure.
- **Global** holds 7 — the genuinely multi-region platforms (Moodle, Kolibri, Tutor).
- **LATAM** places **0 rows on this shelf**, for the *n*th consecutive pass and now with
  a sharper account of why. The function legs run this pass in Spanish and Portuguese
  returned **exam-content archives, not tooling** — FAMAF/UNC (Argentina), Instituto
  Tecnológico de Costa Rica. 🟢 So the regional supply that exists is **content**, and the
  platform layer genuinely has no LATAM-origin project this base can verify. An
  engagement there builds on EMEA or North American platforms with local curriculum data
  on top (`bncc-dados`, `mcp-brasil` — see `agents/top.md`), and that remains a pattern
  rather than a deficiency — see `compose/patterns.md`.
