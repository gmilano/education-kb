## The delivery-format tier — SCORM, credentials, H5P and the fourth LMS — added `p927`

🟢 **Why this section exists.** This base's integration story has been **LTI 1.3** and **MCP** —
both excellent, both requiring the client's platform to cooperate. It had **no row for SCORM**, which
is what corporate L&D and most of the EMEA public-sector LMS estate actually ingests; **no row for
credential issuance** that is not blockchain; **no row for H5P without an H5P server**; and **no row
for D2L Brightspace**, the fourth major commercial LMS. `topic:scorm` (247 repositories),
`topic:open-badges` (37) and `topic:lti` (190) had **never been asked** before `p927`. All grants
byte-read 2026-11-19 across 14 probed paths; **36 probed, 36 resolved, 0 404s**
(`evidence/grant-byte-read.2026-11-19-p927.tsv`).

🟡 **Star counts here are low and the rows are young.** They are shelved as **seams** — the shape of
the integration, verified to exist and verified permissive — not as dependencies to pin. Where a row
is days old, it says so.

| Repo | Licence (byte-read) | Role |
|---|---|---|
| https://github.com/parthdhanani/scorm-kit | **MIT** (`LICENSE@main`, 1,070 B, `sha256₁₂ 51b37fff352e`) | 🟢 **SCORM 1.2 packaging, validation and runtime toolkit**, 2 ★, created 2026-05-24, pushed 2026-11-07. **The one delivery form that is indifferent to which LMS the client runs**: a SCORM package drops into Moodle, Canvas, Open edX, Brightspace, SuccessFactors or Cornerstone with **no plugin, no LTI tool registration, no platform fork and no AGPL exposure**. For a studio that generates content with the agents in `agents/top.md`, this is the last mile. |
| https://github.com/parthdhanani/storycraft | **MIT** (`LICENSE@main`, 1,070 B, **identical** `sha256₁₂ 51b37fff352e`) | **Markdown storyboard → SCORM 1.2 package compiler**, 1 ★, same owner and same grant as `scorm-kit`. Together the two are a complete *author-to-package* pipeline under one licence. `compose/patterns.md` **P54** wires them to this base's content-generation rows. |
| https://github.com/wonmortech/sanad | **Apache-2.0** (`LICENSE@main`, 11,337 B, `sha256₁₂ 2dfd7238870e`) | 🟢 **Verifiable certificates and badges under W3C Verifiable Credentials 2.0**, pushed 2026-11-17, created 2026-11-13. 🔵 The 2026 trend commentary records **blockchain credentialing among the fading trends**; this is the non-blockchain answer to the same requirement, standing on a W3C recommendation rather than a ledger. 🟡 Days old — shelved for the standard it implements. |
| https://github.com/parler-haut-interagir-librement/open-badges-bundle | **MIT** (`LICENSE@main`, 1,155 B, `sha256₁₂ 2da07e888147`) | **Open Badges issuance as a Symfony bundle**: issuer configured once, its profile and keys published, revocation handled. Pushed 2026-11-19. The operational half of credentialing that `sanad` leaves to the integrator. |
| https://github.com/parler-haut-interagir-librement/certificates-bundle | **MIT** (identical grant, `sha256₁₂ 2da07e888147`) | Certificates of completion from course **pass criteria**, rendered to PDF with a **QR verification link**. 🔵 Pairs with the row above: badges for the machine-readable claim, PDFs for the one a learner emails to an employer. |
| https://github.com/missing-elements/h5p-toolkit | **MIT** (`LICENSE@main`, 1,073 B, `sha256₁₂ 18f305a9c256`) | 🟢 **Self-hosted H5P with no H5P server** — a player web component that plays `.h5p` files **offline**, 10 ★, pushed 2026-11-19. H5P is the interactive-content format already inside most Moodle and Canvas deployments; this decouples it from the platform that normally has to host it, which is exactly the constraint `compose/patterns.md` **P14** hits in offline-first delivery. |
| https://github.com/jonsorr/D2L_Brightspace_APIs | **MIT** (`LICENSE@main`, 1,074 B, `sha256₁₂ 9d02fbcfc698`) | 🟢 **First D2L Brightspace row in this base.** Ready-to-use tools on the Brightspace API, each a single self-contained script. 🔵 This base's LMS tier has been Moodle / Open edX / Canvas; **Brightspace is the fourth major commercial LMS and had no row in any file.** 🟡 Created 2026-11-16 — shelved as the seam, not as a dependency. |
| https://github.com/openpatch/bitflow | **MIT** (`LICENSE.md@main`, 1,069 B, `sha256₁₂ 6c8866c27129`) | **Library for building and conducting dynamic, flow-based assessments**, 44 ★, created 2021-03-29, pushed 2026-10-31. 🔵 The highest-star and longest-maintained row in this section, and the only one that models assessment as a *flow* — branching on the learner's response — rather than as a fixed form. |
| https://github.com/mrlvsb/kelvin | **MIT** (`LICENSE@master`, 1,063 B, `sha256₁₂ d94b8adebb28`) | **The code examinator VŠB–TU Ostrava runs in production**, 35 ★, created 2020-01-10, pushed 2026-11-18. 🟢 The `p896` class exactly: institution-maintained plumbing that a star filter buries and an engagement touches on day one. Complements `otter-grader` and `nbgrader` above by being a full examination *service* rather than a grading library. |
| https://github.com/artevelde-uas/canvas-lms-app | 🟢 **ISC** (`LICENSE@main`, 771 B, `sha256₁₂ 4291d4cd3e71`) | **Framework for building custom JS and CSS Canvas LMS themes**, 12 ★, created 2018-10-04, maintained by **Artevelde University of Applied Sciences** (Belgium). 🟢 **This is `T17` in production**: a permissively licensed branding layer, owned by a university, sitting on an **AGPL-3.0** LMS. `T17` was derived from sorting licences; this is the first row in this base that *is* the architecture, maintained for eight years. 🔵 ISC is functionally MIT with shorter wording. |
| https://github.com/dbosk/canvaslms | **MIT** (`LICENSE@master`, 1,074 B, `sha256₁₂ 37f4cab1bcf3`) | **Command-line interface to Canvas LMS**, 9 ★, created 2020-09-08, pushed 2026-11-19, maintained from **KTH**. 🔵 The scriptable half of the Canvas seam — what an agent actually calls when the task is bulk gradebook or enrolment work rather than a UI. |

## Knowledge tracing, continued — the row that measures the measurement, added `p927`

`926-F3` shelved seven knowledge-tracing repositories under *Knowledge tracing with a measured
result attached*, and observed that the three most useful reported results that were **modest or
negative**. `p927` adds the row that sits upstream of all of them.

| Repo | Licence (byte-read) | Role |
|---|---|---|
| https://github.com/10kH/MisconceptDialogue | **MIT** (`LICENSE@main`, 1,129 B, `sha256₁₂ 1d987d9bdc2a`) | 🟢 **The artefact for an AACL-IJCNLP 2026 paper — *"Evaluation Criteria Shape Measured Success in LLM Math Tutoring"***, 1 ★, pushed 2026-11-14. 🔵 **For a knowledge base whose standing caveat is *"no credible primary evidence of learning-outcome gains from AI at scale"*, this is the strongest available answer when a client asks for a number** — because it does not supply one. It argues that the *criteria* decide the measured result, which reframes the client question from *"what is the gain"* to *"against which criteria, chosen by whom"*. That second question is one a studio can scope, price and deliver; the first is not. Use it as the opening reference for `compose/patterns.md` **P7**. |

