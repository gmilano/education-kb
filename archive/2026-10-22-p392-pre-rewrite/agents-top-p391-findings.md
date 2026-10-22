---
industry: education
region: Global
updated: 2026-10-22
---

# `p391`'s findings table, preserved verbatim

Moved off [`agents/top.md`](../../agents/top.md) by `p392` on 2026-10-22, unchanged, when that shelf's
live findings section became `p392`'s. Findings 1, 2, 4, 5 and 7 of `p391` stand as written; findings
3 (*the Python LTI route*), 6 (*tenancy*) and 8 (*the regulatory legs*) are revised by `p392` — see
that shelf for what replaced them.

**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p391.tsv) — **17 addresses
probed, 16 live, 1 unreadable**, every licence read from the payload at the repository's **real
default ref** · [`npm-discovery-yield`](../evidence/npm-discovery-yield.2026-10-22-p391.tsv) — the
sweep's funnel, 321 → 3 · [`channel-state`](../evidence/channel-state.2026-10-22-p391.tsv) — 17 hosts.

## What `p391` changes

| # | finding | where it bites |
|---|---|---|
| 1 | 🔴 **`p390`'s finding #1 is half wrong, and the refutation was already inside this base.** `p390` found [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) abandoned (**2,333 days** — correct) and concluded LTI 1.3 is *"a spec reference to vendor, never a dependency to install."* 🟢 **There is a maintained Apache-2.0 LTI 1.3 library, two of them:** [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) (`master` · `66d8e4e`, **2026-10-16 — 6 days**, Apache-2.0 in `LICENSE.md` *and* `composer.json`; packagist `packbackbooks/lti-1p3-tool` **v6.4.4, 68 versions, published 2026-09-23**) and, for Node, [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (`master` · `41f150c`, **2026-10-13 — 9 days**, Apache-2.0; npm `ltijs` **v7.0.7, 207 versions, published 2026-10-06**). 🔵 The packback line was already in this base's own `agents/trending.md` harvest history — dated, licence-read and registry-confirmed — and had **never reached a shelf**. Same error class as `Gap 386-C`: the shelves published an absence the base did not have. | **The LTI path is open, not closed.** Corrected on `repos/foundations.md`, `verticals/solutions.md` and in `Pattern A` / `Pattern N`. Install `ltijs` (Node) or `packbackbooks/lti-1p3-tool` (PHP); cite 1EdTech only as the spec. |
| 2 | 🔴 **And the abandoned library has an alias, which would have been double-counted.** [`IMSGlobal/lti-1-3-php-library`](https://github.com/IMSGlobal/lti-1-3-php-library) returns the **identical HEAD sha `3a192de`** — an org rename, one project at two addresses. | Counted **once**. Same identity read `p387` used for the mebis/bycs pair; `gate-alias-canonical` territory. |
| 3 | 🔴 **The Python LTI route is the one that is genuinely dead, and that is an architecture constraint.** [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT) last moved **2022-11-21 — 1,431 days**; PyPI `PyLTI1p3` **2.0.0, published 2022-11-20**, 29 releases, none since. | Almost every agent on these shelves is Python. 🆕 `Gap 391-A`: the LTI edge must be **Node or PHP fronting a Python agent over HTTP** — there is no maintained in-process Python option. |
| 4 | 🟢 **Three granted new rows from a registry sweep.** [`pipeworx-io/mcp-education-data`](https://github.com/pipeworx-io/mcp-education-data) (MIT, **1 day**) — US K-12 **district finance and child poverty**; [`intellectif/learning-kit`](https://github.com/intellectif/learning-kit) (MIT, **4 days**) — headless xAPI activity SDK with rubric and deferred grading; [`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (MIT, **1 day**) — diagnosis-first tutor that keeps **its pedagogy in a separate repository**. | New Tier 1 row below; the other two on `repos/foundations.md`. |
| 5 | 🔴 **A licence trap a badge-read and a file-existence check both miss.** [`OpenSourceAGI/qwksearch-research-agent`](https://github.com/OpenSourceAGI/qwksearch-research-agent) ships a **9,655 B `LICENSE.md`** that is **PROSPER 1.0.0**, a bespoke non-OSI licence — not MIT, not Apache. | **Refused, not shelved.** "Has a LICENSE file" is not "is granted"; `Pattern L` gains a step. |
| 6 | 🟡 **The tenancy gap is narrowed, not closed.** [`GuoMonth/dsh-multi-tenant`](https://github.com/GuoMonth/dsh-multi-tenant) (MIT, **10 days**) is real multi-tenant agent hosting — Kubernetes, **OIDC**, per-user persistent volumes, network-policy enforcement. 🔴 But it is tenancy for an **agent workspace**, not for an **LMS integration**: it has no Canvas, Blackboard, D2L or Open edX surface. | `Gap 387-A` stays open for LMS tenancy. This supplies the **hosting half** of `Pattern N`; the integration half is still unbuilt. |
| 7 | 🔵 **The registry channel is depleting, not exhausted — with a number.** 32 fresh queries returned **321 addresses absent from this base**; the domain filter left **37**; 11 probed; **3 shelvable**. That is a **0.9%** yield against `p388`'s **5.7%** (22 of 383) on the same channel. | The channel still works. What `p388` opened is largely mined, so the next pass should change **channel**, not vocabulary. |
| 8 | 🔵 **The regulatory legs produced no new fact, and that is the honest result.** All four regional legs plus a targeted EU Digital Omnibus leg returned material this base already holds more precisely (Art. 50 live 2 Aug 2026, the 2 Dec 2026 transitional marking date, high-risk 2 Dec 2027, Vietnam, Korea). 🔴 `eur-lex.europa.eu` is **DNS-unreachable** here, so the EU dates still rest on secondary corroboration, not the primary text. | No shelf change. Recorded so a later pass does not re-run the same legs expecting a finding. |

🔵 **`p390`'s own table is preserved verbatim** at
[`archive/2026-10-22-p391-pre-rewrite/agents-top.md`](../archive/2026-10-22-p391-pre-rewrite/agents-top.md),
including the nine findings of it that this pass does not touch.


🔵 **One honest non-finding.** The five "published-but-unreadable" repositories `p388` recorded
([`thanh01pmt/interactive-quiz-kit`](https://github.com/thanh01pmt/interactive-quiz-kit),
[`Mckaroff/GraphLMS`](https://github.com/Mckaroff/GraphLMS),
[`ale-alejandro/beadkit`](https://github.com/ale-alejandro/beadkit),
[`AI-Matrix-Engine/aidream`](https://github.com/AI-Matrix-Engine/aidream),
[`yokowasis/autograder`](https://github.com/yokowasis/autograder)) plus
[`santillana-ai/tutor-sdk`](https://github.com/santillana-ai/tutor-sdk) **are all still unreadable**
— they are the 13 non-live rows in this pass's evidence, together with speculative slugs this pass
tried and missed. A blobless clone cannot tell *private* from *deleted*, so these are recorded as
`DEAD-OR-PRIVATE` and **no row claims they were removed from GitHub**. Nothing changed about them;
the status is confirmed, not new.
