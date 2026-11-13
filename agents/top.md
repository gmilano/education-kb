---
industry: education
region: Global
updated: 2026-11-13
---

# Education AI Agents — curated, license-verified

**84 real agents** below — **74 build-safe** (MIT / Apache-2.0 / BSD / ISC) plus
**10 copyleft** — **ten rows added at the seventeenth pass (`p812`, 2026-11-13)**, and
**six rejected**.

🟢 **Seventeenth pass (`p812`) — the `LATAM 0` this shelf published one pass ago is CLOSED, with
eight rows, and the region arrived with the best CONTROL ENGINEERING in this base.** `p811`
published `LATAM 0` as a nil and called it "a published nil, not an omission." 🔴 **It was an
omission, and this pass can say exactly which one:** no search in sixteen passes had ever named a
Latin American education system. Measured on this file before this pass: `SIAGIE` `0` mentions,
`SIMAT` `0`, `SIGAA` `0`, `SUAP` `0`, `SIU-Guarani` `0`. 🟢 **Naming them returned `15`
repositories in one hour, `9` of them build-safe.**

🔵 **So `T26` holds a fifth time, in its sharpest form yet — and inverted.** `T26` says that when
this base names a platform often and shelves nothing for it, that is a search instruction. 🟢
**`p812` adds the converse: when this base has NEVER named a region's systems, a regional zero on
its shelf is a fact about the shelf.** A nil is only informed if the query that produced it was.

🟢 **COUNT DERIVATION — `ingest/derive-counts.py` reports `derived=74 claimed=74 ragged=0
nolink=0 dupes=0 · GREEN` for this file at `p812`.** Re-derived rather than carried forward:

```sh
awk '/^## Build-safe/,/^## Copyleft/' agents/top.md | grep -cE '^\|.*github\.com'   # 74 build-safe
awk '/^## Copyleft/,/^## Rejected/'   agents/top.md | grep -cE '^\|.*github\.com'   # 10 copyleft
awk '/^## Rejected/,0'                agents/top.md | grep -cE '^\|.*github\.com'   # 15 rejected (NOT agents)
python3 -I ingest/derive-counts.py                                                 # the gate
```

**Shelf by region, derived from column 5 this pass: `Global` `49` · `EMEA` `10` ·
`LATAM` `8` · `North America` `4` · `APAC` `3`.** 🔴 **`LATAM 8` replaces `LATAM 0`.**

### The finding (`T34`): LATAM's agent supply is attached to UNIVERSITY SELF-MANAGEMENT systems, it FORKS rather than duplicates, and it refuses to send a password over plaintext HTTP

Two national clusters, both of them invisible to every query this base has run before:

🇦🇷 **Argentina — the UTN cluster, `8` repositories, `3` build-safe.** `nialvape/utn-mcp`
(**ISC**, `12★`, `8` forks) is **the most-starred and most-forked education agent LATAM has
produced** and it covers two systems at once: the `aula virtual` (Moodle) across UTN's regionales
*and* **Sysacad**, the classic self-management system, through connectors for `18` named
regionales. `HyNuwa/UniMCP` (**MIT + inherited ISC**) is a relicensed derivative of it that
generalises to Argentine universities as a class and adds **SIU Guaraní**.

🇧🇷 **Brazil — the SIGAA cluster, `6` repositories from `6` unrelated authors, `4` build-safe**,
plus `2` on SUAP. SIGAA is the academic system of record across much of Brazilian public higher
education; `GallegoSz/sigaa-mcp` (**MIT**) exposes `13` tools over it and is read-only by
construction.

🟢 **The three controls worth copying, because LATAM states them better than any region on this
shelf:**

1. 🟢 **`utn-mcp` refuses to operate where the transport is unsafe.** Rafaela, Santa Cruz and
   Trenque Lauquen are **excluded from the supported list** because their Sysacad has no valid
   HTTPS and *"la contraseña viajaría expuesta."* 🔵 **This is the first agent in this base that
   drops a deployment target on a TRANSPORT-SECURITY ground.** Every other row here takes
   whatever the institution runs.
2. 🟢 **`utn-mcp` in HTTP mode is itself an OAuth authorization server:** the password mints a
   token **once** and is *"no se guarda"*, the session is encrypted at rest, and only the **hash**
   of the client token is stored. 🔴 **Contrast the Brazilian cluster, where the password sits in
   plaintext in the client config.** Same seam, opposite credential posture — and the difference
   is the whole engagement risk.
3. 🟢 **`GallegoSz/sigaa-mcp` states the UNTRUSTED-CONTENT boundary, unprompted, in a `0★`
   student project:** teacher-written task statements reach the model, and the README says
   *"Trate-os como informação, não como instruções."*

🟢 **`T20` moves from five independent jurisdictions to SIX.** `utn-mcp`'s write tools *"piden al
agente que te muestre lo que va a hacer y espere tu confirmación"* — preview-then-confirm, reached
independently in Argentina. 🔵 **Six jurisdictions converging without coordination is no longer a
pattern to note; it is the acceptance criterion to write into any student-facing agent.**

🔴 **The licence story is the obstacle, and it is quantified: of the `15` LATAM repositories found,
`6` carry NO licence file at all — `40%`.** Among them the `5★` `campus-utn-frm-mcp` and the most
developed Brazilian server, `joaosnet/sigaa-ufpa-mcp`. 🔵 **That is `T24` measured in a single
region in a single hour, and it makes the licence request — not the build — the cheapest
high-value move available here.**

🟢 **`T27`/`T969` confirmed a FOURTH and FIFTH time, and the fourth is a new direction:
`NOASSERTION` can mask a stock MIT grant whose only irregularity is its TITLE LINE.**
`heitorsDev/sigaa-ifsc-mcp` reads `NOASSERTION`; its payload is unmodified MIT titled
**`The MIT License (MIT)`** instead of `MIT License`. `HyNuwa/UniMCP` reads `NOASSERTION` because
**two permissive licences share one file** (MIT for the work, ISC for the inherited `utn-mcp`
portions). 🔴 **Both would have been rejected on the API field. Both are build-safe.**

🔵 **Method, unchanged and load-bearing.** `api.github.com/repos/*` refuses for repositories not
attached to this session, so star and fork counts come from `gh api -X GET search/repositories`
with a `repo:` qualifier, and **every licence below was byte-read over `raw.githubusercontent.com`
with its size and `sha256` prefix recorded.** 🔴 **`docs.frappe.io` does not resolve under this
session's network policy**, so the Frappe finding in `repos/foundations.md` was verified from
**source** at `raw.githubusercontent.com/frappe/frappe/develop` instead of from its documentation.

**74 real agents** below — **65 build-safe** (MIT / Apache-2.0 / BSD / ISC) plus
**9 copyleft** — **eight rows added at the sixteenth pass (`p811`, 2026-11-13)**.

🟢 **Sixteenth pass (`p811`) — this shelf is now MACHINE-READABLE for the first time, and it
carries a `Region` column.** The column header was changed to the signature
`ingest/derive-counts.py` has been looking for since `p718`
(`| Name | Repo | Licence | Stars | Region | Description |`) and the heading above the table
now carries its own count. 🔴 **That gate has reported `RED — the table cannot be located` on
this file for every pass since `p718`, which means no pass since then could prove its own row
count.** 🟢 **It now reports `derived=65 claimed=65 ragged=0 nolink=0 dupes=0 · GREEN`** —
and `dupes=0` is itself a first-hand result: no slug appears twice on this shelf.

🔵 **How the `Region` column is filled, because the rule decides what the number means
(`T32`):** a row is placed by **the region in which the system it integrates with is
operated**, read from the repository's own description — never by guessing the author's
nationality. A country-bound system (Schulportal Hessen, iPasen/Séneca, Waseda, NTULearn,
Ed-Fi, FCPS) places the row; a multi-region platform (Moodle, Canvas, Blackboard, Odoo,
SCORM) or an agent with no integration target is `Global`. 🔴 **Author origin is a
DIFFERENT question and this pass did not answer it: it is person-level data, the probe that
would resolve it at scale was deliberately not run, and `T941`'s block on `gh api
users/{login}` still stands.** `ArnaudGuiovanna/tutor-mcp` is French-authored and sits at
`Global` for exactly this reason.

**Shelf by region: `Global` `49` · `EMEA` `9` · `North America` `4` · `APAC` `3` ·
🔴 `LATAM` `0`.** 🔴 **The LATAM zero is a published nil, not an omission: no row on this
shelf integrates with a system operated in Latin America** — after sixteen passes, the
region with `92%` student and `79%` faculty AI use in this base's own market file has no
agent here attached to a system its institutions actually run.

🟢 **The pass's finding (`T31`): EMEA's education agent supply has appeared, and it is
attached to NATIONAL AND REGIONAL SCHOOL PLATFORMS rather than to the LMS layer.** Six of
the eight rows added this pass are of that shape and all six were pushed within five days of
each other: Schulportal Hessen 🇩🇪, DSBmobile 🇩🇪, Admentum 🇸🇪, iPasen/Séneca 🇪🇸,
`sch.gr` 🇬🇷 — plus `edu.by` 🇧🇾 and PRONOTE 🇫🇷 in the copyleft table below. 🔵 **Every one
is `0–2★` and single-maintainer.** 🟢 **Numerous, atomised, and placed** — which is the
`T24` shape, one region up.

**66 real agents** below — **59 build-safe** (MIT / Apache-2.0 / BSD / ISC) plus
**7 copyleft** — **twenty-two rows added at the fifteenth pass (`p810`, 2026-11-13)**,
by a wide margin the largest single-pass addition this base has recorded.

🔵 **Counts re-derived, not carried forward** (the discipline `repos/foundations.md` adopted
at `p807` after six miscounts): build-safe rows matching `^\| .*github\.com` inside the
build-safe section = `59`; copyleft section = `7`; rejected = `9`. 🔴 **The header sentence
through `p809` said `44`/`37` and was correct for `p809`** — it is restated here rather than
patched, so the delta is legible.

🟢 **Fifteenth pass (`p810`, 2026-11-13) — twenty-two agents added, two rejected, and the
pass's real finding is that the field this base has trusted to triage licences is WRONG IN
BOTH DIRECTIONS.** Two rows arrived carrying GitHub's `NOASSERTION`. Byte-read, one is
**unmodified Apache-2.0 and build-safe at `129★`** ([`webworn/openfoam-mcp-server`](https://github.com/webworn/openfoam-mcp-server));
the other is **PolyForm Noncommercial 1.0.0 and commercially prohibited at `35★`**
([`affromero/Sotto`](https://github.com/affromero/Sotto)) — 🔴 **while calling itself "open
source" in its own repository description.** 🟢 **Had this pass trusted the API field, it
would have rejected a usable repository AND shipped an unusable one, in the same hour.**
`NOASSERTION` is not a licence classification; it is an instruction to read the bytes (`T969`).

🟢 **The row that matters most carries `0★`:**
[`Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP`](https://github.com/Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP)
(`Apache-2.0`, pushed `2026-11-12`) is the **first education agent in this base published by a
standards body rather than by a vendor, a lab or a student** — and it ships the three-layer
control stack this base has been asking for since `p792-D`: Keycloak OAuth identity, a
`get_my_scope` authorisation tool, and a Postgres role pinned
`default_transaction_read_only = on` with `GRANT SELECT` on the analytics schema only.
🔵 **Its own README says "demonstration purposes only" — so `P810-1` ships the pattern, not the code.**

🟢 **Three platforms this base has named thousands of times and shelved nothing for are now
served:** **Sakai** (`3,937` mentions → two agents), **SCORM** (`3,434` → two producing
servers plus a validator), **Schoology/Infinite Campus** (`168` → three). 🔴 **And one is NOT:
`OneRoster`, named `3,043` times, returned ZERO MCP or agent servers on a dedicated leg** — see
Declared gaps. 🔴 **PowerSchool stays unclosed too, and for a different reason: three servers
exist and NONE carries a usable grant.** 🔵 **So `p809`'s "the gap was on the shelf, not in the
market" transform held a third and fourth time, and failed cleanly a fifth and sixth — which is
what makes it an instrument rather than a slogan** (`T973`).

🟢 **Fourteenth pass (`p809`, 2026-11-13) — the SEAM transform `p808` prescribed was
run against the remaining LMS seams, and it returned five shelf-ready agents while the
prescribed domain battery returned its SEVENTH consecutive nil.** Added:
[`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server)
(`MIT`, `67★`), [`JhostinAleck/brightspace-mcp`](https://github.com/JhostinAleck/brightspace-mcp)
(`MIT`, `16★`), [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli)
(`ISC`, `13★`), [`kingdonkatsu/ntulearn-mcp`](https://github.com/kingdonkatsu/ntulearn-mcp)
(`MIT`, `4★`) and [`Mattlo0546/blackboard-mcp`](https://github.com/Mattlo0546/blackboard-mcp)
(`MIT`, `1★`), plus one new rejection ([`bencered/d2l-mcp-server`](https://github.com/bencered/d2l-mcp-server)).

🔴 **The finding that matters more than the rows: this base has named Brightspace `171`
times and Blackboard `159` times in its own prose, and had never once carried an agent
for either.** Both are served — Brightspace by two independent MIT servers, the larger at
`67★`; Blackboard by three, one of them `ISC` with `851` commits. 🟢 **The gap was never
in the market. It was on the shelf.** This is the same defect shape the eleventh pass
found with the US state data standard (mentioned `249` times, shelved `0` times), and it
is now the *second* confirmed instance, which makes it a pattern rather than an accident:
**when this base names a platform often and shelves nothing for it, that is a search
instruction, not a market fact.**

🔵 **The reusable query shape, confirmed for a second pass.** Name the SEAM, not the
DOMAIN. `open source MCP server github MIT Blackboard Brightspace D2L LMS agent 2026`
and `"Blackboard Learn" MCP server open source github AI agent 2026` each returned
education-specific repositories on the first page; `top open source AI agents education
2026 github MIT` returned `OpenHands`, `MetaGPT`, `browser-use`, `Flowise`, `Langflow`,
`Dify` and `OpenClaw` for the seventh pass running. Seams still unqueried: `SCORM`
partially (one row found), `LRS`/`xAPI` (held), `PowerSchool`, `Schoology`,
`Infinite Campus`, `Skyward`.

🔴 **A headline star figure in this base is wrong by `183★` and is corrected here.**
`iblai/os` has been published in these files at **`821★`** (and at `654★` elsewhere).
**Measured first-hand from the rendered page on 2026-11-13: `638★`.** Stars do not fall
by that much; the `821` was never right. Nothing in this base should carry a star count
it did not read this pass.

🟢 **COUNT DERIVATION — run these, trust nothing in the prose above.** Re-derived this
pass after insertion: **MIT `27`, Apache-2.0 `6`, ISC `3`, BSD-3-Clause `1` = `37`
build-safe**; **AGPL-3.0 `4`, GPL-3.0 `2`, MPL-2.0 `1` = `7` copyleft**; **total `44`.**
🔴 **The recurring defect is that a naive `grep -cE '^\|.*github\.com'` over this file
also counts the `7` rows of `## Rejected candidates and why`, which are real
repositories but are NOT agents on this shelf.** Note the boundary: the first range must
end at `## Copyleft`, not `## Rejected`.

```sh
awk '/^## Build-safe/,/^## Copyleft/' agents/top.md | grep -cE '^\|.*github\.com'   # 37 build-safe
awk '/^## Copyleft/,/^## Rejected/'   agents/top.md | grep -cE '^\|.*github\.com'   # 7  copyleft
awk '/^## Rejected/,0'                agents/top.md | grep -cE '^\|.*github\.com'   # 7  rejected (NOT agents)
```

🔵 **Method, unchanged and load-bearing.** `api.github.com` refuses for repositories not
attached to this session, so every star count and licence below was read from the
**rendered repository page** (GitHub's own detector). Where a row says *byte-verified*,
the root `LICENSE` was additionally fetched over `raw.githubusercontent.com` and its
size, `sha256` prefix and title line recorded — that channel does resolve, and it is the
only way to catch a README-only grant. 🔴 **`glama.ai` and `oeltkit.bcltraining.com` do
not resolve under this session's network policy**, so `mcp-powerschool` (reported MIT,
FastMCP, PowerSchool) and `OELTKit` (reported Apache-2.0) could **not** be verified and
are deliberately NOT shelved. They are leads for the next pass, not findings.

## Build-safe agents (MIT / Apache-2.0 / BSD / ISC) — 74 rows

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| utn-mcp | https://github.com/nialvape/utn-mcp | **ISC — byte-verified** (`748 B`, `sha256:2ad14eb14513a4fa…`, title line `ISC License`) | 12 | LATAM | **New this pass (`p812`), the anchor row of `T34`, and on two counts the most important LATAM row this base has ever carried: it is the region's most-starred AND most-forked education agent (`12★`, `8` forks), and it has the strongest CREDENTIAL HYGIENE of any student-facing agent here.** MCP server over **UTN** (Universidad Tecnológica Nacional, Argentina) covering TWO systems: the `aula virtual` (Moodle) across its regionales, plus **Sysacad**, the classic UTN self-management system, through per-regional connectors downloaded on demand. FRBA, FRC, FRRE and FRT verified by the author; the Sysacad connector list names `18` regionales; `autogestion_*` tools (academic standing, current enrolment, finals, correlatividades) are **read-only**. 🟢 **Writes state their control in the README: *"Las tools que escriben le piden al agente que te muestre lo que va a hacer y espere tu confirmación"* — preview-then-confirm, which makes Argentina the SIXTH independent jurisdiction to converge on that gate (`T20`).** 🟢 **In HTTP mode the server is itself an OAuth authorization server: the student's password is used ONCE to mint a Moodle token and is explicitly *"no se guarda"*, the session is encrypted at rest under `store.key`, and only the HASH of the client token is kept.** 🟢 **And it REFUSES to run where the transport is unsafe — Rafaela, Santa Cruz and Trenque Lauquen are excluded because their Sysacad has no valid HTTPS and *"la contraseña viajaría expuesta"*; Avellaneda and Rosario are excluded for captcha.** 🔵 Login adapts per regional: Moodle direct, Keycloak SSO (FRBA), or Office 365 with MFA. Created `2026-10-02`, pushed `2026-11-13` — the day of this pass. 🔴 Unofficial and unaffiliated with UTN |
| UniMCP | https://github.com/HyNuwa/UniMCP | **MIT + inherited ISC — byte-verified, against GitHub's `NOASSERTION`** (`1,980 B`, `sha256:727b864af003d1e5…`: an MIT grant © MaxiFG, then a second ISC grant for *"Portions of this software are derived from utn-mcp"* © Joaquín Peñalva) | 1 | LATAM | **New this pass (`p812`), and the row that shows LATAM's supply is a LINEAGE rather than a scatter — it is a relicensed derivative of `utn-mcp` above, generalised from one university to Argentine universities as a class.** Serves the `aula virtual` (Moodle) **and SIU Guaraní**, the self-management system used across Argentine higher education: academic history with marks, results, dates and **expiry of regularidades**, enrolment, and exam sittings. 🔵 **Guaraní is read-only by necessity and the repo says why: *"Guaraní no tiene API: el servidor entra con tu usuario y lee las páginas como lo harías vos"*** — to enrol, the agent hands the student a link instead of acting. Moodle writes (forums, assignment submission) require the student's confirmation. 🟢 **Campus support is established MECHANICALLY, not asserted: each aula was probed with Moodle's `tool_mobile_get_public_config` and each Guaraní with its login page, and the method is published so a reader can repeat it.** 🔴 **Tested thoroughly only at UNJu; the rest *"faltan probarlos con usuarios reales"*** — and SAML/OAuth2 portals (several UNC faculties) are not supported. 🔴 `NOASSERTION` here means only that two permissive licences share one file; both are build-safe. Created `2026-10-19`, pushed `2026-11-13` |
| utnfrm-mcp | https://github.com/BautistaAlosMartorell/utnfrm-mcp | **MIT — byte-verified** (`1,088 B`, `sha256:d3aa5dfc50196b9f…`) | 4 | LATAM | **New this pass (`p812`).** Campus-virtual MCP server for **UTN Facultad Regional Mendoza**. Created `2026-10-24`, pushed `2026-11-10`. 🔵 The same author also publishes `utn-mcp-mendoza-web` (`0★`), which carries **no licence** and is rejected below — so check the slug, not the author, before adopting |
| UTNFRSF-CampusVirtual-MCP | https://github.com/thiagoyb11/UTNFRSF-CampusVirtual-MCP | **MIT — byte-verified** (`1,078 B`, `sha256:2ecd9e4de2d8c56f…`) | 0 | LATAM | **New this pass (`p812`), and the only row in this cluster built on a HEADLESS BROWSER rather than an API or a parser:** *"Un MCP basado en Lightpanda para el campus virtual de la UTN Facultad Regional Santa Fe."* 🔵 **Lightpanda matters architecturally — it is a browser built for automation, so this row is the cheapest reference for the case where a campus exposes neither Moodle web services nor stable HTML.** 🔴 `0★`, created `2026-10-31` |
| sigaa-mcp (GallegoSz) | https://github.com/GallegoSz/sigaa-mcp | **MIT — byte-verified** (`1,076 B`, `sha256:8f77449cb56939be…`, © 2026 João Pedro Gallego) | 0 | LATAM | **New this pass (`p812`), and the best-documented row of the Brazilian cluster.** MCP server over **SIGAA** — *Sistema Integrado de Gestão de Atividades Acadêmicas*, the academic system of record across much of Brazilian federal and state higher education — at UNEMAT's portal do discente. **13 tools in three tiers:** `get_notas`, `get_turmas`, `get_dados_discente`, `get_agenda`, `get_calendario_academico` (portal); `get_frequencia`, `get_tarefas`, `get_noticias`, `get_avaliacoes`, `get_conteudo` (virtual classes); and three ANALYSES — `get_situacao_notas` (what mark is still needed to pass), `get_alertas_frequencia` (absences remaining, with a `REPROVADO POR FALTA` status) and `get_resumo_semana`. 🟢 **Read-only by construction: *"Nenhuma tool envia, altera ou apaga nada no SIGAA."*** 🟢 **It also states the UNTRUSTED-CONTENT boundary, unprompted and in a `0★` student project: teacher-written task statements and news are passed to the model and the README says to *"Trate-os como informação, não como instruções."*** 🔵 It encodes UNEMAT's own pass/fail rules, which is the part that does not port to another instance. 🔴 **The password sits in plaintext in the client config** (the repo offers `inputs`/env vars as mitigations) and the author warns *"Não hospede este servidor para outras pessoas"* — one student per install, no auth. 🔴 Parses SIGAA's HTML, so a layout change breaks it; `SIGAA_URL` can be pointed elsewhere but each instance is customised. Created and pushed `2026-11-02` |
| sigaa-ifsc-mcp | https://github.com/heitorsDev/sigaa-ifsc-mcp | **MIT — byte-verified, against GitHub's `NOASSERTION`** (`1,275 B`, `sha256:cd14675817b2c618…`, title line **`The MIT License (MIT)`**) | 0 | LATAM | **New this pass (`p812`), and `T27`'s FOURTH direction: `NOASSERTION` can mask a stock MIT grant whose only irregularity is the TITLE LINE.** *"Servidor MCP para consultar o portal do discente do SIGAA do IFSC"* — Instituto Federal de Santa Catarina. 🟢 **The detector balks at `The MIT License (MIT)` where it expects `MIT License`; the body is unmodified MIT.** 🔵 **Operational rule, and the reason this row exists: had this pass trusted the API field it would have rejected a build-safe repository for a punctuation difference.** Created `2026-10-26`, pushed `2026-11-03` |
| sigaa-mcp (Pedromaia0) | https://github.com/Pedromaia0/sigaa-mcp | **MIT — byte-verified** (`1,067 B`, `sha256:22e8a5dddc3bfd39…`) | 0 | LATAM | **New this pass (`p812`).** A second, independent SIGAA MCP server, created and pushed `2026-10-28`. 🔴 **No repository description.** 🔵 **It is here because the CLUSTER is the finding: `sigaa mcp` returns `6` repositories from `6` unrelated authors, which is a seam being served in parallel, not one project** — and `sigaa-mcp` is a name shared by two of them, so resolve this row by the full slug (`T22`) |
| sigaa-agente | https://github.com/EduardoBidese/sigaa-agente | **MIT — byte-verified** (`1,076 B`, `sha256:da53ac6f2eef7651…`) | 0 | LATAM | **New this pass (`p812`), and the only row in this base whose integration shape is RPA rather than API or parser:** *"Use o SIGAA com um agente de IA (Claude ou Codex) no seu Firefox, pela extensão Ui.Vision."* 🔵 **It drives the real browser session the student is already signed into, so it needs no credential storage of its own and no web-service token — which is a genuinely different risk profile from the four rows above, and the only one that survives a campus with captcha or MFA on every request.** 🔴 **It also inherits RPA's weaknesses: it is bound to one browser, one extension and the rendered DOM.** `0★`, created and pushed `2026-10-02` |
| cvuex-mcp | https://github.com/rdereparadores/cvuex-mcp | **MIT — byte-verified** (`1,074 B`, `sha256:db6ddec81755f4cd…`) | 0 | EMEA | **New this pass (`p812`), and it extends `p811`'s EMEA finding one tier UP — from the national/regional SCHOOL portal to the UNIVERSITY campus virtual.** *"Servidor MCP para consultar el Campus Virtual de la Universidad de Extremadura (CVUEx)"* 🇪🇸. 🔵 **Same shape as the Argentine cluster and arrived in the same window** (created `2026-09-26`, pushed `2026-11-03`), which is what makes `T34` a cross-regional pattern rather than a LATAM curiosity. 🔴 `0★`, `0` forks, single maintainer |
| lanis | https://github.com/udondan/lanis | MIT | 2 | EMEA | **New this pass (`p811`), and the anchor row of this pass's finding (`T31`).** Unofficial SDK, CLI **and MCP server for Schulportal Hessen (Lanis)** — the student/parent portal operated by a GERMAN FEDERAL STATE, not by an LMS vendor. Created `2026-03-22`, pushed `2026-11-09`; `0` forks. 🟢 **This is the first agent in this base that attaches to a Länder-level education system**, which is exactly the altitude `ACTION p802-B` said German deployment evidence would be found at — and it was found as SOFTWARE before it was found as a statistic. 🔴 `2★` and a single-maintainer account: read it as a reference implementation of the seam, not as a dependency |
| dsbmobile | https://github.com/udondan/dsbmobile | MIT | 0 | EMEA | **New this pass (`p811`).** *Inoffizielles SDK, CLI und MCP-Server für **DSBmobile*** — substitution plans (`Vertretungspläne`), timetables, news and documents. Same maintainer and same creation date as `lanis` (`2026-03-22`), pushed `2026-11-12`. 🔵 **DSBmobile is the daily-notification layer above whatever LMS a German school runs**, so the pair `lanis` + `dsbmobile` covers portal plus timetable for one country without touching Moodle at all. 🔴 `0★`, `0` forks |
| admentum-mcp | https://github.com/andyswe/admentum-mcp | MIT | 0 | EMEA | **New this pass (`p811`), and the safest-shaped row of the `T31` cluster.** *"A **read-only** MCP server that syncs your messages from **Admentum**, the Swedish school platform, to local storage, and serves them to a personal AI agent **one item at a time**."* Created `2026-10-25`, pushed `2026-11-11`. 🟢 **Two controls stated in the description itself — read-only, and a one-item-at-a-time serving discipline that bounds how much of a child's correspondence can enter a model context in one call.** 🔵 That second control is not present in any other row in this file and is worth copying. 🔴 `0★` |
| ipasen_mcp | https://github.com/boraita/ipasen_mcp | MIT | 0 | EMEA | **New this pass (`p811`).** Unofficial MCP server for **iPasen (Séneca)** — the student/family portal of the **Junta de Andalucía**, a Spanish REGIONAL education authority: grades, absences, messages and **"confirmed actions"**. Created `2026-10-30`, pushed `2026-11-10`. 🟢 **The confirm step is in the one-line description, which makes this the FOURTH independent jurisdiction to converge on preview-then-confirm writes (`T20`)** after the three this base already recorded. 🔵 Ships an OpenClaw installer, so the distribution assumption is a consumer agent runtime, not an institutional deployment. 🔴 `0★` |
| sch-mail | https://github.com/weirdapps/sch-mail | MIT | 0 | EMEA | **New this pass (`p811`).** IMAP/SMTP MCP server for **Greek School Network (`sch.gr`)** mailboxes — the state-run network that serves Greek public schools. Created `2026-10-01`, pushed `2026-11-12`, default branch `master`. 🔵 **The seam here is not an LMS API at all — it is the national mail system**, which is a reminder that in state school systems the integration surface is often whatever the ministry actually operates. 🔴 `0★`; mail credentials in an agent's hands is the risk to raise first |
| alms-server | https://github.com/underconnor/alms-server | MIT | 0 | Global | **New this pass (`p811`).** *"ALMS self-hosted backend and **read-only MCP interface** for the bundled school SDK."* Created `2026-10-22`, pushed `2026-11-10`. 🟡 **Placed `Global` rather than in a region because the description names no country-bound system** — the rule this pass adopted for this column (`T32`) places a row by the system it integrates with, and this one does not say. 🔴 `0★`; shelved for the self-hosted-backend-plus-read-only-MCP shape, which is the topology `P23` and `P24` both ask for |
| canvas-mcp | https://github.com/boyuchengz/canvas-mcp | MIT | 119 | Global | **New this pass (`p810`) — the highest-starred education agent added since `p806`, and the first agent in this base for Canvas, the LMS this file's own platform layer has named since the third pass.** Read-only MCP server exposing courses, assignments, deadlines, grades, announcements and files from the **Canvas LMS** REST API to Claude, ChatGPT and any MCP client. `36` forks, created `2026-10-25` and pushed `2026-10-27` — 🔴 **two days of life, so treat maintenance as unproven.** 🟢 Licence **byte-verified** on the blobless-clone channel: `LICENSE` blob `5ba93171ff8f`, `1,072 B`, `MIT License / Copyright (c) 2026 Boyucheng Zhang`. 🟢 **Read-only by construction** — it holds no write path, which is the property that makes it safe to put in front of a student |
| Prototype-Semantic-Layer-with-MCP | https://github.com/Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP | Apache-2.0 | 0 | North America | **New this pass (`p810`), and the most architecturally important row in this file despite `0★` — the first education agent this base has found that is published by the STANDARDS BODY itself rather than by a vendor, a student or a lab.** Ed-Fi Alliance, LLC, pushed `2026-11-12` (one day before this pass). A PostgreSQL **semantic layer** over Ed-Fi API data plus a **read-only early-warning MCP server** scoped to the signed-in educator. Six tools: `get_my_scope`, `list_my_sections`, `find_students`, `list_students_at_risk`, `get_student_summary`, `get_attendance_trend`. 🟢 Licence byte-verified: blob `29f81d812f3e`, `11,558 B`, unmodified Apache-2.0. 🔴 **The README says "for demonstration purposes only; not intended to be a robust production solution" — ship the PATTERN, not the code.** See `P810-1` |
| openfoam-mcp-server | https://github.com/webworn/openfoam-mcp-server | **Apache-2.0 — byte-verified, against GitHub's own `NOASSERTION`** | 129 | Global | **New this pass (`p810`), and it is a row this base would have WRONGLY rejected on the API field alone.** GitHub's `license.spdx_id` returns `NOASSERTION`; the `LICENSE` bytes are **unmodified Apache-2.0** (blob `be1f2caa61c7`, `10,708 B`, `APPENDIX` present, no added restrictive clause — the three `shall not` hits are stock Apache §1 and §9). 🟢 **So it is build-safe.** An LLM-driven **OpenFOAM** CFD MCP server with Socratic questioning and expert error resolution — engineering-education specific, `24` forks. 🔴 Pushed `2026-01-18`, so it is the least recently maintained row added this pass. See `T969` |
| OpenStudy | https://github.com/OpenStudy-dev/OpenStudy | MIT | 80 | Global | **New this pass (`p810`).** Self-hostable study dashboard with a **built-in MCP server**, so an existing Claude/ChatGPT subscription becomes the study engine rather than a per-seat API spend. `14` forks, created `2026-04-17`. 🟢 **The commercial point is the inversion of the cost model** — the institution hosts the surface and the learner brings the model subscription, which is the only structure in this base that avoids per-learner inference billing entirely |
| Grader-agent | https://github.com/erictrainnlpinxihu/Grader-agent | MIT | 94 | Global | **New this pass (`p810`) — the first rubric-grading agent in this base with an auditable control structure, and the row that makes `P810-3` buildable.** Five-phase main loop `perceive→plan→act→observe→respond` driven by a harness. 🟢 **The design decision that matters: the MODEL decides only intent and confidence; routing, tool set and risk level are pinned in CODE.** That is exactly the separation Ofqual's "AI may not be the sole marker" and the EU Art. `27` FRIA both require a deployer to evidence. 🔴 `0` forks and a Chinese-language README; created `2026-09-21` |
| edumints-scorm-mcp | https://github.com/kemalyy/edumints-scorm-mcp | MIT | 9 | Global | **New this pass (`p810`).** MCP server that **assembles interactive, SCORM-compliant e-learning courses**, self-hostable, from edumints.com. `5` forks. 🟢 **SCORM is named `3,434` times across this base and until this pass had exactly one producing repo** — this is the second, and the first that an agent can drive conversationally |
| scorm-mcp-server | https://github.com/giacomomaria81/scorm-mcp-server | MIT | 6 | Global | **New this pass (`p810`).** Turns HTML, Claude Design bundles or mobile-learning exports into **LMS-ready SCORM 2004 / 1.2 packages — and validates any SCORM zip.** Offline and tracked. 🟢 **The validator is the reusable half**: it is the only SCORM conformance check in this base that runs without an LMS, which makes it a pre-delivery gate rather than a post-upload surprise |
| cubite-mcp | https://github.com/amirtds/cubite-mcp | MIT | 0 | Global | **New this pass (`p810`), and the widest tool surface of any education MCP server in this base: `137` tools.** Drives **Cubite LMS** (SCORM, xAPI, certificates, cohorts) from Claude, ChatGPT, Gemini CLI or Cursor, with OAuth sign-in. 🔴 **`0★`, `0` forks, single-vendor-bound, created and last pushed the same day (`2026-09-23`).** 🔵 Carried for the tool-surface design, not as a dependency — and read it next to [`jeffercbs/chispa-mcp`](https://github.com/jeffercbs/chispa-mcp)'s `77` tools, because a `137`-tool server at the teacher's own permission level is `p792-D`'s unclaimed risk at twice the size |
| myelinate | https://github.com/baney75/myelinate | MIT | 7 | Global | **New this pass (`p810`).** Claude Code plugin and **agent-skill suite that makes the assistant a Socratic tutor: `14` skills** for course design and teaching. 🟢 **MIT on a SKILL corpus is the licence shape this base has repeatedly failed to find** — `GarethManning/education-agent-skills` (`978★`) is CC BY-SA 4.0 and was rejected at `p802` as contaminating, so this is the first permissive skill corpus that can be cut down and shipped inside a client deliverable |
| CodeTrain (agent-skills) | https://github.com/InferHaven/agent-skills | Apache-2.0 | 4 | Global | **New this pass (`p810`).** An open-source **Socratic coding tutor that runs as an Agent Skill inside the learner's own coding agent** rather than as a separate product. 🟢 **The delivery shape is the finding: no server, no LMS, no seat** — it meets the learner where the work already happens, which is the one channel a university cannot procure its way out of |
| viable | https://github.com/VIABLE-Learning-Lab/viable | MIT | 1 | Global | **New this pass (`p810`), pushed `2026-11-11`, two days before this pass — the freshest row in this file.** "Open tools for AI that teaches the way a teacher wants": a **Harness that wraps any agent** plus an Engine. 🟢 **A lab-origin project (`VIABLE-Learning-Lab`) that separates teaching POLICY from the model** — the same control shape as `Grader-agent`, arrived at independently. 🔴 `1★`, created `2026-11-05`; this is a seed, and it is shelved as one |
| sakai-mcp | https://github.com/jtayped/sakai-mcp | MIT | 2 | Global | **New this pass (`p810`) — the first Sakai agent in this base.** Sakai is named `3,937` times across these files, more than any other LMS, and carried **zero** agents until this row. Student-account scope: courses, assignments, files, grades, notifications, tasks **and submission** — 🔴 **so it is NOT read-only; the submission path writes on the student's behalf.** Gate it. Created `2026-10-14`, pushed `2026-11-01` |
| sakai-tasks-mcp | https://github.com/sayt25606-rgb/sakai-tasks-mcp | Apache-2.0 | 1 | Global | **New this pass (`p810`).** Unofficial **local** MCP server for Sakai LMS — assignment deadlines, quizzes, announcements, course materials. 🟢 **Read-only and local**, which is the conservative counterpart to `jtayped/sakai-mcp`'s submission path: the same platform at two different risk levels, which is the first time this base can offer that choice on any LMS |
| schoology-mcp | https://github.com/riripatate/schoology-mcp | MIT | 3 | North America | **New this pass (`p810`) — the first Schoology agent in this base.** TypeScript client plus a Claude MCP skill. 🟢 **"No admin API keys needed" is the deployment property that matters**: it works from the student's own session, so a pilot needs no district IT approval — 🔴 which is also precisely why a district would want to block it. Both halves are the same fact |
| fcps-school-mcp | https://github.com/jibberswrld/fcps-school-mcp | MIT | 2 | North America | **New this pass (`p810`).** Local MCP server for **FCPS Schoology and StudentVUE**, one-command setup; pushed `2026-11-06`. 🔵 **Fairfax County Public Schools is one of the largest US districts**, and this is a pupil-built client for it — see `T974` on hyper-local supply |
| schoology-mcp (PAUSD) | https://github.com/dajun666/schoology-mcp | MIT | 1 | North America | **New this pass (`p810`).** MCP server for **PAUSD Schoology and the Infinite Campus student portal** — 🟢 **the first Infinite Campus surface in this base**, a US K-12 SIS this file has named `101` times and shelved never. Created and pushed `2026-10-08`; single-district scope |
| mcp-learning-server | https://github.com/shastripranav/mcp-learning-server | MIT | 0 | Global | **New this pass (`p810`).** MCP server for **learning analytics and SCORM/xAPI integration** — the only row in this base that spans both the packaging standard and the record standard in one server. 🔴 **`0★`, `0` forks, last pushed `2026-06-30`** — shelved for the span, not the traction |
| ashashala | https://github.com/piyushh62/ashashala | MIT | 2 | Global | **New this pass (`p810`).** **Multi-tenant, role-based agentic AI tutoring platform built for real schools**, explicitly "100% open source, zero paid APIs". 🟢 **Multi-tenant + role-based is rare at this star count** — most tutoring rows in this base are single-tenant demos, and tenancy is the thing a district pilot discovers it needs in week three |
| Tlamatini | https://github.com/XAIHT/Tlamatini | MIT | 15 | Global | **New this pass (`p810`).** "Speak an idea. Build the real thing." — voice-driven AI across code, 3D worlds and hardware with a live editor, aimed at making building teachable. 🔵 **Named for the Nahuatl *tlamatini* ("one who knows"), which SUGGESTS a Mexican or wider LATAM origin — 🔴 but `gh api users/{login}` is refused in this session (`T941`), so origin is NOT resolvable and this row is placed `LATAM?` rather than given the closed vocabulary on a guess** (`T935`). Pushed `2026-11-13`, the day of this pass |
| qiaomu-learning | https://github.com/joeseesun/qiaomu-learning | MIT | 72 | Global | **New this pass (`p810`) — APAC-origin, and the strongest Socratic-method row found this window.** Turns textbooks, screenshots, PDFs, notes or a bare topic into a **one-question-at-a-time derivation dialogue**, triggered by the learner explicitly asking not to be told the answer. `7` forks, created `2026-08-10`. 🟢 **It encodes the OECD's "pedagogy stays in control" finding as a product constraint rather than a principle** |
| tizhuang-agent-skills | https://github.com/weishao2/tizhuang-agent-skills | MIT | 39 | Global | **New this pass (`p810`) — APAC/China K-12.** Agent skill over a **20M+ item K-12 question bank** (Chinese primary and secondary past papers): free registration, item sampling, textbook/chapter/knowledge-point retrieval, practice tests and AI-assembled papers. `7` forks, pushed `2026-11-11`. 🔴 **MIT covers the SKILL code; it does NOT grant rights in the question bank the skill retrieves from** — the same corpus-versus-code split this base flagged at `P800-3`. Read the item licence before any deliverable touches it |
| scholarship-navigator | https://github.com/OmarZen/scholarship-navigator | MIT | 14 | Global | **New this pass (`p810`).** Scholarship matching with eligibility checks, fit scores, **missing-document detection** and a dated plan. `3` forks, pushed `2026-11-11`. 🟢 **The only student-finance agent in this base**, and the missing-document check is the part that generalises — it is an admissions-operations pattern, not a search box |
| brightspace-mcp-server | https://github.com/RohanMuppa/brightspace-mcp-server | MIT | 67 | Global | **New this pass (`p809`) — the highest-starred new education agent of this window, and the first D2L Brightspace agent on this shelf.** `29` tools in seven groups (courses/grades, assignments/rubrics, announcements/discussions, content, people/groups, instructor Dropbox, account). 🔴 **Strictly read-only by design** — README: *"It only reads your courses. It never submits, edits, or deletes anything."* Auth is the school's own SSO page plus the account's 2FA; the password goes to the OS keychain (Keychain/Credential Manager) and saved session state is **AES-256-GCM** encrypted. Author: ECE @ Purdue. README lists working instances in 🇺🇸 🇨🇦 🇳🇱 🇨🇴 🇸🇬. `492` commits. 🟢 `MIT` byte-verified: root `LICENSE`, `1,068 B`, `sha256:047079fbd49120ed…`, affero×`0`. |
| brightspace-mcp | https://github.com/JhostinAleck/brightspace-mcp | MIT | 16 | Global | **New this pass (`p809`) — the strongest write gate in this base, and the first LATAM-origin education agent found with a real, byte-verified grant.** `29` tools: **`26` read, `3` write** (`submit_assignment`, `post_discussion_reply`, `mark_announcement_read`). 🟢 **Writes require TWO independent opt-ins** — `writes.enabled: true` in config **and** `--enable-writes` passed to `serve` — plus a `dry_run` preview mode, a client-supplied **idempotency key** on every write, and a warning-level **audit-log** entry per write. Four auth strategies (API token; headless user+password with MFA via TOTP/Duo Push/manual; Playwright browser automation; session cookie). 🔵 Ships an `es-419` locale and an `America/Bogota` sample timezone. `452` commits. 🟢 `MIT` byte-verified: `1,070 B`, `sha256:008ec594c78e9fd5…`, affero×`0`. |
| campus-cli | https://github.com/alejooroncoy/campus-cli | ISC | 13 | Global | **New this pass (`p809`) — a Peru-origin agent and the most-developed Blackboard client found anywhere (`851` commits, `v3.1.0`).** TypeScript CLI **and** MCP server (`campus mcp`, stdio) over **UPC Aula Virtual** (Blackboard Learn); UPN also supported, Canvas and Moodle on the roadmap; repo topics include `peru`. 🔴 **Read-only against Blackboard** — the README states it does not submit assignments or change anything; submissions stay in Aula Virtual. Local writes are downloaded files and the stored authorisation only. 🔴 **Governance flag, and it is the reason this row is not a drop-in for an institution: the tool catalogue is brokered by a remote relay (`mcp.campuscli.com`) that decides which tools to offer per university**, so student credentials and traffic cross a third party. Fine for a student; a contract question for a client. 🟢 `ISC` byte-verified: `748 B`, `sha256:4ca1bd2e969c…`. |
| ntulearn-mcp | https://github.com/kingdonkatsu/ntulearn-mcp | MIT | 4 | APAC | **New this pass (`p809`) — the first Singapore-origin agent in this base.** `8` tools over **NTULearn**, Nanyang Technological University's Blackboard Learn: courses, announcements, calendar items, grades, plus course-file download into local folder structures. Python 3.12+, `28` commits. 🔴 **Auth is the `BbRouter` session cookie, auto-read out of Edge/Chrome/Firefox/Brave via `browser-cookie3`**, falling back to `NTULEARN_COOKIE` and then an OS-keychain cache, with one clear-and-retry on `401`. 🔴 **Scraping a live session cookie is unsanctioned access** — same contract risk as the three proprietary-SIS paths in this base, and it should be priced as such, not as an integration. 🟢 `MIT` byte-verified: `1,055 B`, `sha256:e6bd1450153a…`, affero×`0` (sidebar shows only a generic "License" link; the payload is the evidence). |
| blackboard-mcp | https://github.com/Mattlo0546/blackboard-mcp | MIT | 1 | Global | **New this pass (`p809`) — the only vendor-neutral Blackboard Ultra server found; the other two Blackboard rows are each bound to one university.** Python 3.10+ MCP server: reads courses, deadlines and announcements and downloads lecture slides for Claude Desktop, Cursor and Codex. Signs in through the university's SSO rather than an API key. 🔴 **Read-only on Blackboard** — README: it *"can't submit work, post or change anything on Blackboard"*; the only writes are to a local folder. 🔴 **`4` commits — the earliest-stage row on this shelf. Read it as a reference implementation, never as a dependency.** 🟢 `MIT` byte-verified: `1,067 B`, `sha256:13c8ad755224…`, affero×`0`. |
| interactive-learning | https://github.com/geekjourneyx/interactive-learning | MIT | 52 | Global | **New this pass (`p808`) — and it is a *skill package*, not a server or an app, which is why four passes of agent-shaped searching missed it.** Takes arbitrary input — text, a link, a document or a bare question — and turns it into a **verifiable learning path**, optionally emitting an HTML "checkpoint card" that makes each step checkable rather than merely read. 🟢 **The verifiability is the reason it is shelved:** every other content-generation node in this base (`educhain`, `OpenMAIC`) produces material, not a checkable path, and the gap between "generated a lesson" and "can show the learner passed it" is the one a client always asks about. Installs into Claude Code / `opencode`-style harnesses as a skill, so it composes with `canvas-mcp` or `Moodle-MCP` for delivery rather than competing with them — see `P22`. 🔴 **`52★` and `4` commits: this is a seed, not a dependency.** Read it as a design for the checkpoint card and reimplement if it must carry weight. Licence verified from the rendered sidebar (`MIT license`). |
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 58.7k | Global | Lifelong personalized tutoring; learner model persists across sessions and builds learning paths. **v1.7.2 released 2026-11-06**; 7.1k forks. Largest education-specific agent on GitHub. |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 43.4k | Global | Open Multi-Agent Interactive Classroom (Tsinghua MAIC lab). Turns a topic or document into a multi-agent classroom — teacher, peers, assistant — in one click. **README News lists v1.5.0-rc.2 on 2026-11-12; GitHub Releases is empty**, so treat the version as pre-release. Ships pt-BR and es-MX locales. |
| teacher-to-skills | https://github.com/JuneYaooo/teacher-to-skills | Apache-2.0 | 475 | Global | **New this pass.** Distills a specific teacher's materials (lecture video, notes, marked-up feedback) into a source-backed agent Skill that teaches to that teacher's standard and tapers support as the learner improves. Conclusions are tied to sources; unevidenced material is flagged, not filled in. Learner progress is stored outside the generated Skill. Runs under Claude Code / Codex / OpenClaw. 73 forks. |
| mcp-odoo (ERPipe) | https://github.com/erpipe-org/mcp-odoo | MIT | 433 | Global | **New this pass — the largest build-safe agent in this KB that reaches an open-source SIS, and it is not an education project, which is why four passes of SIS searching missed it.** 41 tools over **Odoo 16-19** (smoke-tested against 16.0/17.0/18.0/19.0): `search_records`, `read_record`, `aggregate_records`, `get_model_fields`, `list_models`, plus module helpers, diagnostics, migration, audit and cross-instance fan-out. Because the tools take the **model name as a parameter**, OpenEduCat's `op.student`, `op.admission`, `op.exam.attendees` and `op.fees` are reachable with no education-specific code. **Writes are gated by construction — this is the row's real value:** direct `create`/`write`/`unlink` are blocked, and an approved write must pass `preview_write` -> `validate_write` -> `execute_approved_write` carrying a **single-use, same-process, expiring approval token**, with `confirm=true`, live non-empty `fields_get` metadata, and `ODOO_MCP_ENABLE_WRITES=1`; `ODOO_MCP_ELICIT_WRITES=1` adds a native confirmation prompt, and `execute_method` runs allowlisted methods only. XML-RPC default, JSON-2 on Odoo 19. 198 forks, 118 commits, Releases empty. **Formerly `tuanle96/mcp-odoo`** — the old slug is what search results still return, so record the new one. **Caveat for any proposal: the maintainer sells a hosted product (ERPipe) built on this repo** — the MIT grant is real; the roadmap has a commercial owner. |
| sabis-mcp-server | https://github.com/hanifisenturk/sabis-mcp-server | ISC | 2 | EMEA | **New this pass — the third agent-to-SIS path in this KB and the first from EMEA (Türkiye).** MCP server over **SABIS**, the student information system of **Sakarya University**. One tool, `get-grades`: course codes and names, assessment types and weights, final letter grades, academic year and semester. 🔴 **Reaches the SIS by Puppeteer web scraping, not an API, and reads the student's own `USERNAME`/`PASSWORD` from environment variables** — a credential-replay design to read and *not* reproduce. README states it is unofficial, unaffiliated with the university, and for personal/educational use. 0 forks. Admitted for the regional and topological record: with `edupage-mcp` (Slovakia/Czechia, undocumented endpoints) and `mcp_hemis_student` (Uzbekistan), the pattern is three-for-three — **individual developers reaching captive national or institutional SIS products by unofficial means.** |
| DeepTutor-MCP | https://github.com/Suyutao/DeepTutor-MCP | Apache-2.0 | 1 | Global | **New this pass — the first MCP server in this base built over another education *agent's* data rather than over a platform.** 60 tools exposing a self-hosted DeepTutor install to any MCP client: status, courses, syllabus and linked resources; Mastery Paths with outlines, evidence and review settings; Question Bank and practice queues with answer checks and analytics; generated books and reading material with notes, highlights and bookmarks; notebooks; knowledge-base metadata with file search and vector passage retrieval; historical sessions and memory documents; plus an opt-in tool that posts into a DeepTutor conversation. 15 commits, no releases. **Two hard dependencies before it runs:** a reachable self-hosted DeepTutor HTTP API, and — for the Mastery tutor tools — upstream PR **`HKUDS/DeepTutor#1785`, which its README says is still open and unmerged**. Not a dependency yet; admitted as the first evidence that DeepTutor (58.7k) is growing a tool ecosystem. |
| canvas-mcp | https://github.com/vishalsachdev/canvas-mcp | MIT | 324 | Global | Canvas LMS MCP server plus 8 agent skills for students and educators. The cleanest path to making an agent act inside Canvas. **Tool count is inconsistent on its own page: README says "up to 128 tools", the sidebar About says 102.** Default profile registers fewer; feature-gated tools raise the total. 106 forks. |
| Moodle-MCP | https://github.com/Faixiang/Moodle-MCP | MIT | 206 | Global | **New this pass — closes this KB's declared Moodle gap.** Zero-dependency Python MCP server over the Moodle Web Service API. 10 **read-only** tools (courses, assignments, quizzes, deadlines, files), v1.4.0 dated 2026-11-02, docs in 10 languages, Moodle 3.x/4.x, verified by its author against Moodle 4.3.6. Read-only is a feature for a first engagement: no write path, no token escalation. |
| educhain | https://github.com/satvik314/educhain | MIT | 388 | Global | Python package for generating educational content (questions, lesson plans, flashcards) with GenAI. Library, not an app — good as a content-generation node. |
| ai-shifu | https://github.com/ai-shifu/ai-shifu | Apache-2.0 | 332 | Global | AI-guided instruction: the agent teaches and answers in a scripted, author-controlled flow rather than free chat. |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 280 | Global | Open-source Intelligent Tutoring System with Bayesian Knowledge Tracing (UC Berkeley CAHLR). React + Firebase; mastery modelling is the asset. |
| Open TutorAI (CE) | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 117 | Global | Community edition of an educational collaborative AI platform. |
| Tutor MCP | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 102 | Global | MCP server that turns any LLM into an Intelligent Tutoring System; persistent, auditable learner state and progression governed outside the model. v0.7.0 adds institutional courses, invitations, enrollment. Small star count, unusually mature design. |
| Claw-ED | https://github.com/SirhanMacx/Claw-ED | MIT | 65 | Global | **New this pass.** Local-first teaching assistant: starts from the teacher's own lesson plans, slides and assessments and drafts new lessons, student materials and decks. v9.18.2026.1 (Beta). **Explicitly single-teacher, not multi-tenant**, and student-facing features are experimental. README is honest that hosted models still receive the prompt content even though storage is local. 16 forks. |
| moodle-mcp (Rust) | https://github.com/G36maid/moodle-mcp | MIT | 29 | Global | **New this pass.** Rust MCP server: courses, assignments, forums, grades, and files-as-markdown. Author reports live verification against **Moodle 3.7, 4.5 and 5.2** — the widest version coverage of any Moodle MCP server found. |
| learnmcp-xapi | https://github.com/DavidLMS/learnmcp-xapi | MIT | 16 | Global | **New this pass — the only agent↔learner-record write path in this KB.** MCP server over any **xAPI 1.0.3**-compliant Learning Record Store. Three tools: record a statement, retrieve progress, manage activity vocabulary. Ships the `practiced` / `mastered` / `experienced` / `achieved` verbs and separates learners by an `ACTOR_UUID`, so one server serves a cohort. **Verified LRS targets: SQL LRS, Ralph, Veracity** (TinCan and xAPI Wrapper are listed as planned, not shipped). Python 3.8+, 4 forks, Releases empty, author states active development. This is what makes an agent's activity *reportable* by the institution instead of invisible. |
| AI Scoring Platform | https://github.com/wwrwbs/AI_AWE | Apache-2.0 (per README + LICENSE; sidebar shows only a generic "License" link) | 2 | Global | **New this pass — the only credible open grading system found.** Automated argumentative-essay scoring (1–6) with label-aware feedback: fine-tuned Qwen2.5-7B LoRA discourse-move classifier → LightGBM scorer over 31 linguistic/discourse features → feedback generator, with a Gradio UI for single and batch scoring. Locally deployable. **Naming trap: the arXiv paper calls this system "ArguLens"; the repository never uses that name.** Vendored TextComplexityToolkit is MIT. |
| moodle-mcp (browser-session) | https://github.com/falkenslab/moodle-mcp | MIT | 2 | Global | **New this pass.** Claims **~260 Moodle tools** including grading and quiz building — by far the largest surface found. Authenticates by opening a real browser for the user's own interactive login, so it **supports SSO and 2FA and needs no web-service token, admin rights, or Moodle plugin** ("your login, never your password"). Targets Moodle 4.5 and 5.x. 2 stars: powerful design, unproven. |
| moodle-mcp (publishing) | https://github.com/MarcosNahuel/moodle-mcp | MIT | 1 | Global | **New this pass.** Aimed at *writing* pedagogical content: 40 high-level tools plus a `ws_raw` escape hatch across courses, sections, content, quizzes, gradebook, messaging, calendar and badges. Writes are **upsert-by-`idnumber`, so republishing is idempotent** — the right primitive for generated course content. Requires companion plugin `local_italiciamcp` for the full set; self-reported ~80% operability at v0.5.2. |
| Manu (tutor-ai-agent) | https://github.com/Jeanikt/tutor-ai-agent | MIT | 0 | Global | **New this pass — the first LATAM-origin education agent this KB has found.** Voice-first math tutor **in Brazilian Portuguese**, adapting from 1st grade to university; spoken explanations render to an on-screen chalkboard. TypeScript + LiveKit Agents with a Next.js front end. In development, no public deployment. 0 stars — a seed, not a dependency. |
| EDUKAI LongView | https://github.com/Keitous/EDUKAI-LONGVIEW | ISC | 0 | Global | **New this pass — the first Africa-origin education agent this KB has found.** MCP-powered *longitudinal* learning intelligence: tracks a learner across multiple academic periods rather than single test scores, retrieves supporting evidence, flags sustained strengths and recurring difficulties, and recommends for teacher review ("agent recommends, teacher decides"). Bilingual FR/EN, author based in **Guinea**. Node.js/Express. **Synthetic data only** — a prototype. |
| EduAgentic (EduMCP) | https://github.com/kamalelafoui/Agentic-AI-EdTech-J33-J34 | MIT | 0 | Global | **New this pass — the only MCP + A2A education example found.** FastMCP server on SSE exposing six tools (`search_courses`, `get_learner_profile`, `recommend_learning_path`, `generate_quiz`, `grade_quiz`, `get_learning_statistics`) **plus an A2A orchestrator** over three named agents (Tutor, Evaluation, Orientation). Every other education agent in this table is single-agent or MCP-only; this is the one place in the set to read an agent-to-agent education topology. **French-language** repo and docs — francophone provenance; the author's country is not stated on the page and is not asserted here. 0 stars, 0 forks, no releases: a course artifact. Take the **topology**, not the code. |
| socratic-tutor (Jane Street `agent_skills`) | https://github.com/janestreet/agent_skills | MIT | 7.9k | Global | **New this pass — the largest permissively licensed education artifact in this KB, and it is not software.** Jane Street's first public agent skill: a strict Socratic tutor that runs a 3-5 question diagnostic, maps the topic into **4-10 sub-skills rated 0-5**, asks **one question at a time**, then adds spaced review and a final assessment. 510 forks, **2 commits** — it is a `SKILL.md` instruction set, so it needs an LLM host (coding agent or chatbot), ships no code and carries **no dependency or CVE surface**. Compare `education-agent-skills` (977 stars, CC BY-SA) in the rejected table: same artifact class, wrong instrument. This one is MIT and can go into a client deliverable as-is. Third-largest education agent here after DeepTutor and OpenMAIC, on two commits. |
| edupage-mcp | https://github.com/oliverhruby/edupage-mcp | MIT | 4 | EMEA | **New this pass — the first verified agent-to-SIS path in this KB.** 31 tools over **EduPage**, the school information system used across Slovakia and Czechia: timetables, grades, homework and a daily summary, plus meal ordering, multi-school discovery, role-aware student switching and **2FA**. Distributed on PyPI (`edupage-mcp-full`), Docker/GHCR and the MCP Registry. **The caveat governs adoption:** it reaches EduPage through the community `edupage-api` library, which uses **undocumented endpoints** — there is no vendor contract, so it can break on any EduPage release. Python 3.10+, 1 fork, 123 commits. Take the topology; do not ship the dependency. |
| mcp_hemis_student | https://github.com/sukhrobyangibaev/mcp_hemis_student | MIT | 0 | EMEA | **New this pass — the second agent-to-SIS path, and the first Central Asian project in this KB.** MCP server over **HEMIS** (Higher Education Management Information System), the student-information platform used by Uzbek universities: a student pulls their own academic record, schedule, grades and attendance. 9 commits, no repository description, no releases, 0 stars. Admitted **for the SIS topology only** — it is evidence that the student-record gap is closing from the national-platform direction, not a dependency. |
| mcp-education (zavora-ai) | https://github.com/zavora-ai/mcp-education | Apache-2.0 (per README; sidebar shows only a generic "License" link) | 1 | Global | **New this pass — the only Rust education MCP server found, and the only server at any star count that gates writes in its tool contract.** Canvas LMS API: courses, assignments, grades, students, announcements. **12 tools split 9 read-only + 3 write operations that require approval** — the read/write boundary is declared by the server rather than left to the host's discretion, which is the design to copy for any education MCP server that writes to a gradebook. Built for "ADK-Rust Enterprise"; Rust 1.94.1, 1 fork. |
| ai-tutor-agent | https://github.com/vulinh1704/ai-tutor-agent | MIT | 0 | Global | **New this pass — the clearest tutoring *guardrail* implementation found at any star count.** FastAPI + LangGraph, with three controls this KB has not found written down elsewhere: a **Socratic hint ladder** that escalates one level per turn up to a configurable cap; an **answer-leak guard** that regenerates a draft which reveals the final answer and substitutes a safe hint if it still leaks; and **rubric grading in which per-criterion scores are validated against the rubric and the totals are computed in code, not by the model**. A router node splits tutor / grader / clarify. SQLite checkpointing persists a session across restarts; a deterministic offline fake model runs the whole graph with no API key, which also makes it testable in CI. 0 stars — take the control design, not the repo. |
| AI-Teaching-Agent | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT | 0 | Global | **New this pass.** Compiles one Markdown teaching source into reviewable **Lab and Exam packages** plus short teaching decks, using structured DSLs, sandboxed evaluation and an MCP stdio server (`mcp_server/` with tool adapters, MCP manifest shipped in the wheel). **Nothing publishes automatically:** artifacts are validated, candidate-facing content is protected, and a human decision gates local export — the review-gate shape that `P6` (grading) and any assessment engagement needs. README states further MCP/Agent expansion is **frozen**, so treat it as a fixed reference rather than a growing project. |
| che-ntucool-mcp | https://github.com/PsychQuant/che-ntucool-mcp | MIT | 1 | APAC | **New this pass (`p806`) — the strongest write gate in this base, and the first Taiwan-origin agent in it.** MCP server over **NTU COOL**, National Taiwan University's Canvas deployment (`cool.ntu.edu.tw`), in **Swift**, Developer ID signed, Canvas token in the macOS keychain with a logged-in Safari tab as fallback auth. 10 tools: 6 read (`list_courses`, `list_assignments`, `list_announcements`, `list_submissions`, `list_files`, `list_enrollments`) and 2 write pairs. 🟢 **`post_grades` and `post_announcement` are gated twice over — an MCP elicitation dialog *plus* a single-use token bound to the previewed payload.** That is a stronger contract than `zavora-ai/mcp-education`, which this base previously called the only server gating writes in its own tool contract. 🔴 Found by audit of this base's own trending logs, not by search; `ntucool` appeared there 12 times and on no shelf. |
| Smartschool-MCP | https://github.com/maurodruwel/Smartschool-MCP | MIT | 6 | EMEA | **New this pass (`p806`) — the fourth agent-to-SIS path in this KB and the second from EMEA.** 15 tools over **Smartschool**, the dominant school platform in Flemish Belgium: results, schedule, periods, reports, planned elements, student support links, student notes, **absences**, attachments and homepage blocks. Python 3.10+, 7 forks against 6 stars. 🟢 **Read-only by construction — there is no write tool at all**, which makes it the lowest-risk row in this table to put in front of a school's data-protection officer. 🔴 **Belgium is inferred** from `school.smartschool.be` and Dutch field names (`Leerlingvolgsysteem`), not stated by the repo. |
| waseda-moodle-mcp | https://github.com/12dora/waseda-moodle-mcp | MIT | 0 | APAC | **New this pass (`p806`) — the first Japan-origin education agent in this base.** MCP server over **Waseda University's Moodle** (`wsdmoodle.waseda.jp`), authenticating with the same web-service token the official Moodle mobile app uses. **20 read tools and 11 write tools**, plus prompts (`daily_briefing`, `weekly_plan`, `exam_prep`) and `moodle://course/{id}` resources. 🟢 **Every mutation is split `prepare_*` → `confirm_action` / `cancel_action`** — nine `prepare_` verbs, one confirm, one cancel. Deploys to Cloudflare Workers or local stdio. 🔴 **Self-declared unofficial and unaffiliated with Waseda** — a reference design, not a vendor relationship. |

## Copyleft — usable, but the license propagates

| Agent | Repo | License | Stars | What it does |
|---|---|---|---|---|
| expeditto | https://github.com/fabrica-de-inovacao/expeditto | **AGPL-3.0 — byte-verified** (`34,523 B`, `sha256:0d96a4ff68ad6d4b…`, title line `GNU AFFERO GENERAL PUBLIC LICENSE`) | 1 | **New this pass (`p812`), and the only agent in this base whose user is a TEACHER doing compliance paperwork rather than a student studying.** *"Expeditto: seu segundo expediente, resolvido. Prepara o RIT do SUAP (IFMA) como rascunho, via CLI e MCP."* The **RIT** (*Registro Individual de Trabalho*) is the workload return Brazilian federal-institute teachers must file in **SUAP**, the Instituto Federal administrative suite. 🟢 **The write gate is in the product definition, not bolted on: it prepares the RIT *as a draft* (`rascunho`) and a human files it.** 🔵 **That is the cleanest statement of `P6`/`P26`'s principle found so far — the agent does the assembly and never the submission — and it is worth quoting to any client nervous about agents touching a system of record.** 🔴 **AGPL-3.0: integrate as a separate service, never derive.** 🔵 Its licence payload is byte-identical to `LearnHarness`'s (`34,523 B`, `sha256:0d96a4ff68ad6d4b…`), which corroborates both as stock AGPL-3.0 rather than a modified grant. Created `2026-09-30`, pushed `2026-10-22` |
| edu-by-agent | https://github.com/Severnbli/edu-by-agent | GPL-3.0 | 0 | **New this pass (`p811`), and the FIFTH independent instance of preview-then-confirm (`T20`).** *"CLI, MCP server and Claude Code skills for managing school websites in the **edu.by** site constructor: pages, menus, news, images – **with preview and confirmation before every write**."* `edu.by` is the Belarusian national school-website constructor. Created `2026-11-09`, pushed `2026-11-13` — the day of this pass. 🔴 **GPL-3.0, so the code propagates**: take the preview/confirm write gate, which is stated as a property of EVERY write rather than of selected verbs. 🔴 `0★`, four days old |
| pronoteConnect | https://github.com/sairo-cyber/pronoteConnect | **GPL-3.0-or-later — byte-verified, against GitHub's `NOASSERTION`** | 2 | **New this pass (`p811`), and `T27`'s third direction: `NOASSERTION` masked INHERITED copyleft.** *Connecteur **PRONOTE** open source et auto-hébergé pour ChatGPT via MCP, avec connexion **EduConnect** locale* — PRONOTE is the dominant French secondary-school information system and EduConnect is the state identity provider. Created and pushed `2026-09-08`. 🟢 **`LICENSE` read first-hand on `raw.githubusercontent.com`: line 1 is `SPDX-License-Identifier: GPL-3.0-or-later`.** 🔴 **And the file states WHY, which is the commercially important part: *"This license choice is compatible with the declared GPL-3.0-or-later license of the `@blockshub/pawnote-lts` dependency used by this prototype."*** 🔵 **The copyleft is not the author's preference, it is inherited from the only available PRONOTE client library — so a permissive French PRONOTE agent cannot be produced by relicensing this repo; it requires a clean-room client.** See `T33` |
| canvas-pilot | https://github.com/X-isdoingreat/canvas-pilot | AGPL-3.0 | 125 | **New this pass (`p808`) — the highest-starred NEW education agent found in this window, and the only one of six LMS-seam candidates with meaningful traction.** Local-first Canvas LMS agent that **learns each course's recurring assignment workflow and replays it** through an explicit `scan -> approval -> execute` cycle with a student review step before anything is submitted. 🟢 **The workflow-learning loop is the genuinely new idea in this base:** every other Canvas agent here (`canvas-mcp`, `opencode-class-agents`) exposes Canvas as tools and leaves orchestration to the model, whereas this one treats the *recurring shape of a course's work* as the persistent artifact. 🔴 **AGPL-3.0 — the network clause makes it unusable as the base of a hosted or distributed client product**, exactly as with `LearnHarness`. Take the scan/approve/execute topology, not the code. 🔴 **Traction signal is internally odd and must not be quoted without this caveat: `125★` against `1` commit.** A single-commit repository at `125★` is either a squashed initial release or externally promoted; either way the star count does not evidence sustained maintenance. Licence verified from the rendered sidebar (`AGPL-3.0 license`). |
| mcp-server-odoo | https://github.com/ivnvxd/mcp-server-odoo | MPL-2.0 | 415 | **New this pass — the governed alternative to `erpipe-org/mcp-odoo`, and the better choice where the *institution* must own the policy.** Reaches any Odoo model, so it too reaches OpenEduCat's student record. Access control lives in a **companion Odoo module** carrying a per-model allowlist with separate read / write / create / delete permissions, layered on Odoo's own access rights and record rules — so the client's Odoo administrator decides what an agent may touch, rather than an environment variable inside the agent's container. 17 tools including `create_records`/`update_records` batches, attachments, `aggregate_records`, `post_message` and (double-env-gated) `call_model_method`. Odoo 16.0+ in standard mode; JSON-2 with an API key on Odoo 19+. 190 forks. **Why it is in this table and not the one above: MPL-2.0 is *file-level* weak copyleft** — modifications to its own files must be published, but it combines freely with proprietary code, so unlike AGPL it needs a licence note in the deliverable rather than a redesign. 🔴 **Red flag to raise in every review: "YOLO mode" requires no companion module, bypasses all MCP-level access control and exposes 200+ models; full YOLO mode permits delete.** Its own README restricts it to development and testing. Never ship it, and grep for it in any inherited deployment. |
| LearnHarness | https://github.com/amosblomqvist/learnharness | AGPL-3.0 (**payload-verified this pass**: root `LICENSE`, `34,523 B`, `sha256:0d96a4ff68ad6d4b…`, affero×`16`, title line `GNU AFFERO GENERAL PUBLIC LICENSE`; sidebar agrees) | 9.1k | **New this pass — the largest NEW education repository found in this window, and the fastest-growing artifact this base has tracked.** Desktop agent *harness* for learning hard material: agents plan and teach a lesson from the learner's current understanding toward a stated goal, and a **local knowledge graph stores ideas and the links between them rather than ability ratings** — a different persistence model from `DeepTutor`'s learner model and from `OATutor`'s Bayesian Knowledge Tracing, and the reason it is worth reading even though it cannot be shipped. Bring-your-own API keys; ships for macOS, Windows and Linux. `1,202` commits, `1.2k` forks. 🔴 **AGPL-3.0 is the whole adoption story: the network clause makes this unusable as the base of a distributed or hosted client product.** Take the knowledge-graph design, not the code. 🔵 Indexed write-ups are badly stale on size — one says `1.5k★`, another `5.7k★`; the rendered page said `9.1k★` this pass. 🔴 **NAMESAKE HAZARD, added at the twelfth pass (`p807`): "LearnHarness" does not uniquely identify this repository.** A `2026-11-13` adaptive-learning search returned [`h4ksclaw/learnharness`](https://github.com/h4ksclaw/learnharness) — **a different project, not a fork**: `3★`, `1` fork, `52` commits, described as *"Open-source adaptive learning harness with FSRS, BKT, and LLM-powered knowledge graphs. Domain-agnostic."* against this row's *"Agent harness for learning difficult things."* 🔴 **Its README states its licence as the bare word `MIT` under a `## License` heading, and there is NO `LICENSE` file at all** — `raw.githubusercontent.com` returns `404` for `LICENSE` and `LICENSE.md` on **both** `main` and `master`, which is why GitHub's sidebar shows no licence. 🔵 **A prose "MIT" with no grant file is not a grant; the default is all-rights-reserved.** 🟢 **Always resolve this row by the full slug `amosblomqvist/learnharness`, never by name** — the two differ in owner, size, purpose *and* licence, and the cheap mistake (`MIT`, `3★`) is the one that looks build-safe. 🔴 This is distinct from `T966`'s two `0★` byte-identical AGPL-3.0 forks; `h4ksclaw` is a third repository and shares no bytes with either. |
| tutor-gpt | https://github.com/plastic-labs/tutor-gpt | GPL-3.0 | 933 | AI tutor driven by Theory-of-Mind reasoning about the learner. GPL-3.0: fine for internal or hosted use, a problem for a distributed client product. |
| openedx-mcp | https://github.com/blend-ed/openedx-mcp | AGPL-3.0 | 3 | Open edX admin operations as an MCP facade for staff/superusers, native platform APIs only. Very early — reference, not dependency. |
| moodle-mcp-server (csmediapro) | https://github.com/csmediapro/moodle-mcp-server | AGPL-3.0 | 2 | Moodle MCP server over Web Services; 10 core tools plus cache management and `refresh_user_field_schema`. **Open-core: additional tools ship in a paid premium plugin.** AGPL plus a commercial upsell is the wrong base for a client deliverable — note it and move on. |
| moodle-mcp-server (lmscloud) | https://github.com/lmscloud-io/moodle-mcp-server | GPL-3.0 | 1 | Runs Moodle web services for administration and analysis; installs via `uvx`, authenticates with a Moodle web-service token. No repository description, no stated tool count. |

## Rejected candidates and why

Real and active projects that are **not** open-source-licensed in a way
Globant can build a client deliverable on.

| Candidate | Repo | Actual license | Stars | Why rejected |
|---|---|---|---|---|
| Sigaa-UFRPE-MCP | https://github.com/DaviPac/Sigaa-UFRPE-MCP | **No licence — `404` for `LICENSE`, `LICENSE.md`, `LICENSE.txt` and `COPYING` at `main` AND `master`** | 0 | **New rejection this pass (`p812`).** SIGAA MCP server for UFRPE (Universidade Federal Rural de Pernambuco). Created `2026-09-05`. Default all-rights-reserved |
| sigaa-ufpa-mcp | https://github.com/joaosnet/sigaa-ufpa-mcp | **No licence — `404` at both branch roots** | 1 | **New rejection this pass (`p812`), and the most developed of the ungranted Brazilian servers:** *"Este projeto implementa um servidor MCP (Model Context Protocol) específico para automatizar o acesso ao SIGAA"* (UFPA). Pushed `2026-11-08`. 🔵 **The highest-value licence request in the Brazilian cluster** — see `intel/licence-requests/` |
| campus-utn-frm-mcp | https://github.com/ignaw05/campus-utn-frm-mcp | **No licence — `404` at both branch roots** | 5 | **New rejection this pass (`p812`), and the one that stings: at `5★` it is the second-most-starred UTN campus agent and it carries no grant at all.** Pushed `2026-11-06` |
| utn-mcp (PedroCarassale) | https://github.com/PedroCarassale/utn-mcp | **No licence — `404` at both branch roots** | 1 | **New rejection this pass (`p812`).** *"Servidor MCP para el campus virtual (Moodle) de la UTN FRLP"* (La Plata). 🔴 **Shares the bare name `utn-mcp` with the ISC-licensed `nialvape/utn-mcp` on the shelf above — the `T22` collision, and here the ungranted one is the namesake.** Pushed `2026-10-31` |
| moodle-utn-mcp | https://github.com/NicolasViruel/moodle-utn-mcp | **No licence — `404` at both branch roots** | 2 | **New rejection this pass (`p812`).** *"Agente conectado via MCP para el consumo de la informacion de la facultad."* Pushed `2026-10-19` |
| suap-mcp | https://github.com/frjunioalves/suap-mcp | **No licence — `404` at both branch roots** | 0 | **New rejection this pass (`p812`).** The only other SUAP server besides the AGPL-3.0 `expeditto`. 🔴 **So SUAP, like PowerSchool, has no permissive agent: one copyleft and one ungranted.** Pushed `2026-05-22` |
| Sotto | https://github.com/affromero/Sotto | **PolyForm Noncommercial License 1.0.0 — byte-verified, against GitHub's `NOASSERTION`** | 35 | **New rejection this pass (`p810`), and the exact mirror of `webworn/openfoam-mcp-server`.** Self-hosted open-source AI language learning: CEFR courses, adaptive listening, speaking practice; `10` forks; pushed `2026-11-13`, the day of this pass. 🔴 **`LICENSE` blob `1a71cb643975`, `4,563 B`: "Any noncommercial purpose is a permitted purpose."** PolyForm Noncommercial is **not an OSI licence** and forbids exactly what Globant does — commercial client delivery. 🔴 **It calls itself "open source" in its own description.** 🟢 Read it for the CEFR course structure; do not ship a line of it. See `T969` |
| mcp-powerschool | https://github.com/443pablo/mcp-powerschool | **No licence — GitHub reports `NONE`, no `LICENSE` in the repository** | 2 | **New rejection this pass (`p810`).** The highest-starred PowerSchool MCP server found, and it carries no grant at all. 🔴 **PowerSchool is the largest US K-12 SIS and this base has named it `382` times; the only other candidates are `zuvy/ps-mcp-server` (`NONE`) and `thesupersupersigma/powerschoolMCP` (`GPL-3.0`, copyleft).** 🟢 **So the PowerSchool gap is NOT closed this pass, and it is a LICENCE gap rather than a supply gap** — three servers exist, none is build-safe |
| d2l-mcp-server | https://github.com/bencered/d2l-mcp-server | **No LICENSE file — `404` at `main` AND `master` root; GitHub sidebar shows none** | 12 | **New rejection this pass (`p809`).** The README carries a `License` section reading `MIT`, but **no licence payload exists at either branch root** and GitHub's own detector reports nothing, so on its face the repository is default all-rights-reserved. 🔵 **This is the T6 pattern in its most deniable form, and the transmission path was identified:** an aggregator (`glama.ai`) published *"License MIT"* read off the README, and that is where the claim entered circulation — the same channel that mis-reported `RohanMuppa/brightspace-mcp-server` as `AGPL-3.0` when its payload is a byte-verified `MIT`. 🔴 **Aggregator licence fields are not evidence in either direction.** `3` commits. Re-test the payload before any future admission. |
| PageLM | https://github.com/CaviraOSS/PageLM | CaviraOSS / "PageLM Community License" — **not OSI** | 2.1k | README requires prior written permission for commercial use or resale. Marketed as "open source"; it is source-available. Do not put it in a client stack. |
| llamatutor | https://github.com/Nutlope/llamatutor | **No license file** | 2.1k | Default all-rights-reserved. Good reference implementation of an AI personal tutor on Llama 3.1; not reusable without an explicit grant. |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 | 977 | 165 evidence-grounded education skills for Claude/Codex-style agents. CC BY-SA is a **content** license with share-alike — usable as pedagogy reference material, wrong instrument for shipped software. |
| AITutor-EvalKit | https://github.com/kaushal0494/AITutor-EvalKit | **No licence file — re-verified at `HEAD` `a71078456a90` this pass** | 4 | 🔴 **Moved out of the build-safe table this pass, and the move is a correction of this base against itself.** `p801` (`T961`) established that this repository serves **no licence anywhere**, while its `EACL 2026` paper calls it *"MIT-licensed"*. The row in the build-safe table went on publishing `MIT` for a further pass. `p802` re-probed the clone channel and reproduced `T961` exactly — **same `HEAD`, still a `7`-entry tree, still no `LICENSE`, `COPYING` or equivalent in the root tree** — so the grant does not exist and the default is all-rights-reserved. Still the only pedagogy-specific eval harness found, so it remains worth reading and worth an upstream licence request; it cannot be adopted. 🔴 **This base has now carried a licence it had itself refuted for one full pass — see `ACTION p802-A`.** |
| educational-agents | https://github.com/nifalconi/educational-agents | **No license file** | 1 | **New rejection this pass.** Spanish-language teaching library ("agents in 2 lines") from the *Niñas Pro* applied-AI course for girls in **Chile** — genuinely interesting as LATAM education provenance, and the kind of project worth contributing a LICENSE file to. As published it is all-rights-reserved and cannot be adopted. v0.1.0 prototype, built on the OpenAI Agents SDK via OpenRouter. |
| AI-Grading-Tool | https://github.com/end13s/AI-Grading-Tool | **No licence file — sidebar shows none** | 0 | **New rejection this pass (`p808`).** The only *Moodle*-targeted grader found in the LMS-seam leg, and functionally the closest fit to a real client ask: imports a Moodle roster and submissions, has an LLM check each one against the instructor's rubric, routes every result through human review, then exports grades back to Moodle. 🔴 **`134` commits and no grant of any kind — the default is all-rights-reserved.** 🔵 **This is the fourth education repository in this base to be substantial and unlicensed** (`llamatutor` `2.1k★`, `AITutor-EvalKit`, `educational-agents`, now this), which is itself the finding recorded as `T24`. Worth an upstream licence request; cannot be adopted as published. |

## Declared gaps

- **🟢 CLOSED this pass (`p812`): the `LATAM 0` gap — and the reason it stood for sixteen passes
  is a search defect, stated precisely so it is not repeated.** Eight rows now attach to systems
  operated in Latin America. 🔴 **The defect: this file had never written the word `SIGAA`,
  `SIAGIE`, `SIMAT`, `SUAP` or `SIU-Guarani` once.** 🔵 **The transferable rule: a regional nil
  is only informed if a query named that region's OWN systems. Otherwise it reports the shelf,
  not the world** — and `p811` published it as a fact about the world.

- 🔴 **`SIAGIE` (Peru) — an INFORMED NIL, and now a properly evidenced one.** `gh api -X GET
  search/repositories q="siagie"` returns **`25` repositories and not one agent**: attendance
  uploaders, grade-consolidation reports, nómina tools, analytics dashboards, scrapers. 🔴
  **Every single one carries NO licence file.** 🔵 **So Peru's national K-12 system has an active
  developer community and zero agentic surface and zero grants** — the widest open slot this
  pass found, and the cheapest to enter.

- 🔴 **`SIMAT` (Colombia) — a HARD NIL.** `q="simat educacion"` returns `total_count=0`. Not a
  thin result; an empty one. Colombia's national enrolment system has no open-source presence of
  any kind on this channel.

- 🔴 **`SUAP` (Brazil) — a LICENCE gap, not a supply gap, and the second instance of the
  PowerSchool shape.** Two servers exist: `expeditto` (**AGPL-3.0**, shelved to the copyleft
  table) and `frjunioalves/suap-mcp` (**no licence**, rejected). 🔵 **Neither is build-safe, so
  SUAP joins PowerSchool as a system of record whose agents all fail the licence test rather than
  the existence test.**

- 🔴 **Q-Acadêmico (Brazil) and the Mexican, Chilean and Colombian school systems — NIL on a
  dedicated leg.** `q="q-academico mcp"`, `q="mcp server mexico universidad escuela"`,
  `q="mcp uc chile universidad"` and `q="mcp colegio escolar notas alumno"` each returned
  `total_count=0`. 🔵 **LATAM's supply is real but it is concentrated in exactly two countries —
  Argentina and Brazil.** Quote the region's eight rows as Argentine and Brazilian, never as
  "LATAM coverage."

- 🔴 **`ingest/derive-counts.py` is RED on `repos/foundations.md` and
  `verticals/solutions.md`, and this pass did NOT force it green — the diagnosis is recorded
  instead, because the fix is a judgement call.** The gate looks for ONE canonical shelf per file
  (`| Repo | Licence | Stars | Default branch | Why it is a foundation |` and
  `| Platform | Repo | Licence | Branch | Stack | Use case |`). 🔵 **Measured this pass: those two
  pages carry `13` and `13` tables respectively, deliberately organised BY LAYER** — rostering,
  LTI, xAPI, QTI, Caliper, curriculum corpus — with headers of the shape
  `| Repo | License | Stars | Notes |`. 🔴 **Flattening thirteen layered tables into one shelf to
  satisfy the gate would destroy the structure that makes those pages usable.** 🟢 **The right
  fix is to teach the gate to sum rows across a file's layer tables, as it was already taught at
  `p568` to accept family-suffixed recipe ids and at `p718` to key on column signatures instead of
  prose.** Left open deliberately, with the numbers above, so the next pass can act on evidence.

- 🔴 **`OneRoster` — an INFORMED NIL, and the cleanest one this base has produced.**
  OneRoster is named **`3,043`** times across these files and is the roster-sync standard
  every LMS/SIS integration in `compose/patterns.md` assumes. A dedicated leg
  (`gh api search/repositories q="oneroster mcp"`) returned an **empty result set — zero
  repositories, not zero good ones**. 🟢 **The standard itself is served on the
  non-agent side** — [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests)
  (`Apache-2.0`, `7★`) and [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import)
  (`GPL-2.0`, `8★`) are both shelved to `repos/foundations.md` this pass. 🔵 **So the gap is
  specifically agentic: there is a conformance suite and an importer, and nothing that lets an
  assistant read or reconcile a roster.** 🟢 **That is a buildable opening, not an absence** —
  and it is the narrowest, best-evidenced contribution target this file has ever carried.

- 🔴 **`PowerSchool` — NOT a supply gap, a LICENCE gap, and it stays open.** `382` mentions in
  this base. Three servers exist and were each checked this pass:
  [`443pablo/mcp-powerschool`](https://github.com/443pablo/mcp-powerschool) (`2★`, **no licence**,
  rejected above), `zuvy/ps-mcp-server` (`1★`, **no licence**), and
  [`thesupersupersigma/powerschoolMCP`](https://github.com/thesupersupersigma/powerschoolMCP)
  (`GPL-3.0` — copyleft, usable only where the deliverable can carry GPL). 🔵 **The largest US
  K-12 SIS has three agents and no permissive one.** A licence request is the cheap move here,
  and `intel/licence-requests/` is the place it belongs.

- 🔴 **Curriculum alignment — a THIN nil, declared rather than filled.** The leg
  `curriculum alignment ai agent` returned only `0★` repositories with **no licence file**
  (`shlomitb/curriculum_alignment_agent`, `anujgadwal-AI/SmartCurriculum-AI-agent`). 🟢 **Nothing
  was shelved from it.** 🔵 Standards-to-outcome alignment remains the highest-value unserved
  slot in this file, and it is now negatively evidenced twice.

- **🟢 CLOSED this pass (`p809`): the Brightspace gap and the Blackboard gap.** Both
  were gaps in this file, not in the world. **Brightspace/D2L** now has two shelf rows,
  `RohanMuppa/brightspace-mcp-server` (`MIT`, `67★`) and `JhostinAleck/brightspace-mcp`
  (`MIT`, `16★`). **Blackboard** has three, `alejooroncoy/campus-cli` (`ISC`, `13★`),
  `kingdonkatsu/ntulearn-mcp` (`MIT`, `4★`) and `Mattlo0546/blackboard-mcp` (`MIT`, `1★`).
  🔴 **Read the shape before quoting them: four of the five are read-only and two are
  hard-bound to a single university's tenant** (UPC/UPN, NTU). Exactly **one** agent in
  this base can write to Brightspace, and it is `JhostinAleck/brightspace-mcp` behind a
  two-opt-in gate. **Neither Blackboard nor D2L publishes an MCP server of its own**
  (checked 2026-11-13); every path above is unofficial, built on the REST API, the SSO
  session or a scraped cookie.
- **🔴 OPEN, and now the sharpest supply gap in this base: the higher-education SIS/ERP
  tier.** **Ellucian Banner**, **Ellucian Colleague** and **Workday Student** — the
  systems of record for most of North American higher education — have **no open-source
  MCP server or agent of any kind**, searched from two independent angles this pass and
  returning nothing but vendor connector pages. Ellucian documents **Ethos** (Data Model
  APIs, Business Process APIs, Ethos GraphQL) and publishes no MCP server; Workday ships
  its own proprietary *Agent-Ready Tools*. 🔵 **The only generic lead is the one that
  worked for OpenEduCat: wrap the platform API, not the vertical.** For Banner that means
  a thin server over Ethos. **Nothing in this base implements it, and an engagement that
  assumes otherwise will be wrong.**
- **🔴 The "open-source Agentic SIS" is a FRONT END, and this base came within one row of
  publishing the vendor's framing.** `iblai/sis` carries a genuine, byte-verified `MIT`
  payload (`1,089 B`, `sha256:969b7073d1c42ac2…`) — **and the README states plainly:**
  *"ibl.ai/sis is a front end for the ibl.ai platform"*, *"If you need the full backend,
  reach out at ibl.ai/contact for an enterprise license."* It writes **no backend
  endpoints of its own**; sign-in goes to `login.iblai.app`. 🟢 **The grant is real and
  it covers a Next.js client.** 🔴 **The system of record is proprietary.** Same shape as
  `iblai/lms` (`MIT`, `95★`: *"you need access to an ibl.ai backend instance"*) and
  `iblai/os` (`MIT`, `638★`: *"requires the ibl.ai backend platform … not included in
  this repository"*). **The SIS gap is NOT closed by these.** They are shelved under
  `verticals/solutions.md`, where a platform with a commercial core belongs, not here.


- **The learner-record gap is half closed, and the halves must not be
  confused.** `learnmcp-xapi` gives an agent a read/write path to the
  *learning-activity* record — xAPI statements: what the learner did, practiced
  and mastered. It does **not** reach the *student* record: enrolment,
  transcript, attendance, demographics, fees. Pattern `P9` needs the LRS
  and can be built today on permissive licenses; pattern `P8` needs the SIS.
  Scoping an advising engagement against the wrong one of
  these is the most expensive mistake available in this KB.
- **The SIS gap is CLOSED for one open-source SIS, and the reason four passes
  missed it is a search defect, not a market one (fifth pass).** The fourth pass
  withdrew "no SIS has an agent interface" and replaced it with "not one
  *open-source* SIS has an agent interface." **That is now withdrawn too.**
  OpenEduCat (LGPL-3.0, **911 stars, 789 forks** — the leading open-source
  education ERP) is a set of **Odoo addons**, and Odoo has two mature MCP servers
  whose tools take the **model name as a parameter**:
  `erpipe-org/mcp-odoo` (**MIT, 433 stars**, three-call gated writes) and
  `ivnvxd/mcp-server-odoo` (**MPL-2.0, 415 stars**, per-model allowlist in a
  companion Odoo module). `op.student`, `op.admission`, `op.exam.attendees` and
  `op.fees` are therefore reachable with no education-specific code.
  **The defect to learn from: every SIS search in four passes looked for an
  _education-specific_ server, so the largest relevant connector in the field —
  bigger than any education-specific agent in this KB except DeepTutor, OpenMAIC
  and `agent_skills` — was structurally invisible.** When a vertical gap looks
  empty, search the *platform* the vertical is built on.
- **What is still genuinely unserved, stated precisely so it can be priced.**
  **RosarioSIS** (GPL-2.0, 654 stars, PHP/Postgres, heavy LATAM K-12) and
  **Gibbon** (GPL-3.0, 638 stars, PHP/MySQL, international K-12) have **no
  agent interface and no generic connector of the Odoo kind** — searched by
  project name this pass and nothing returned. `frappe/education` (GPL-3.0, 707)
  sits on the Frappe framework, which is the next place to look for the same
  generic-connector trick. **The three servers that reach proprietary SIS
  products all do so unofficially** — `edupage-mcp` (undocumented endpoints via
  a community library), `mcp_hemis_student`, and new this pass
  `sabis-mcp-server` (Puppeteer scraping with the student's own credentials in
  environment variables). Three-for-three: **where the SIS is proprietary and
  national, the only agent paths are unsanctioned**, which is a contract risk,
  not an architecture.
- **`Gap 286` — the Odoo→OpenEduCat path is architecturally verified and has
  NOT been run.** The connectors' tools are model-generic and OpenEduCat is Odoo
  addons; both facts were read off the repository pages this pass. **No Odoo
  instance was stood up, OpenEduCat installed, and a tool called against
  `op.student`.** That run is the cheapest high-value experiment on this board.
  Until it is done, quote the path as *"the connector is generic and the SIS is
  Odoo addons"*, never as *"we have run it."*
- **Student-record *analytics* topology exists but could not be
  license-verified.** `EdyVision/student-services-mcp` (1 star) exposes 13
  tools including `fetch_student_dropout_risk`, `fetch_high_risk_students`,
  `fetch_attrition_statistics` and `fetch_attrition_feature_importance` — the
  closest thing found to a retention/early-warning tool surface, and a useful
  shape to copy for `P8`. **The rendered page shows no license field**, and it
  runs on **synthetic data** with no real SIS connection. Not admitted to the
  table: read it as a design sketch and do not adopt it without a license.
- **No pedagogy-specific eval harness at scale, and the only candidate is
  UNGRANTED.** `AITutor-EvalKit` (🔴 **no licence file — re-verified at `HEAD`
  `a71078456a90` in `p802`; the `MIT` this base published was refuted in `p801`
  and is withdrawn**, 4 stars, mathematics only) is still the only one found — unchanged across all
  three passes. Every agent in the table above claims pedagogical effect and
  none of them can be compared on it.

- **Grading is still nearly empty, but no longer absent.** `wwrwbs/AI_AWE`
  (Apache-2.0, **2 stars**) is the only credible open scoring *system* found —
  a real pipeline with a published paper behind it, at prototype scale.
  `nbgrader` (BSD-3-Clause, 1.4k) remains notebook autograding infrastructure,
  not an agent. The rest of the field is Kaggle-era TF-IDF/LSTM/DeBERTa
  coursework and single-star LLM wrappers, several of which are API-only
  (OpenAI/Azure/Cohere) and therefore unusable where data residency binds.
  **Nothing in grading is to grading what DeepTutor is to tutoring.**
- **Pedagogical evaluation is still the thinnest layer in education AI.**
  AITutor-EvalKit at 4 stars is the state of the art. Teams in every region are
  shipping tutors with no shared way to measure whether they teach.
- **The Moodle MCP field is now real but fragmented and unconsolidated.** Seven
  servers verified this pass, licenses split MIT / GPL-3.0 / AGPL-3.0, star
  counts 1–206, and **no two agree on tool surface**: 10 read-only
  (`Faixiang`), 40 idempotent-write + plugin (`MarcosNahuel`), ~260 via browser
  session (`falkenslab`), files-as-markdown in Rust (`G36maid`). There is a
  consolidation opportunity here, and in the meantime the choice is genuinely
  per-engagement — read-only vs write, token vs SSO, plugin vs no plugin.
- **LATAM and Africa now have education agents, both at 0 stars.** Manu
  (Brazil, MIT) and EDUKAI LongView (Guinea, ISC) exist and are the first this
  KB has found. They are prototypes, not foundations. The strategic reading is
  unchanged — localize permissively licensed APAC/North American agents — but
  the regional origin story has changed from *absent* to *nascent*, and a
  0-star repo by a Guinean author doing longitudinal learner analytics is worth
  watching.
- **The long tail is student coursework.** The `education-ai` GitHub topic lists
  71 repositories; the 20 most-starred run 475 down to 2 stars, and below
  `Claw-ED` (65) they are overwhelmingly single-author projects — Streamlit
  quiz generators, dropout-prediction notebooks, Chinese-language K-12 skill
  packs. Excluded here by design: a KB row implies "a studio could start from
  this."
