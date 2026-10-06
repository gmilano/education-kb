---
industry: education
region: Global
updated: 2026-10-06
---

# `gitlab-api-channel` — the only forge API this environment can reach (pass 22 of 2026-10-06)

`api.github.com` has answered **403** to this environment since pass 37. Forty-plus passes of this KB
have therefore read licence payloads and star counts and have never once been able to ask a forge a
*question*: no licence key, no topics, no copyright holder, **no commit recency**. This instrument
calls a different forge's API, which answers all of them — and the first thing it found is that one
of its answers is wrong about a row this KB already publishes.

## What it does

| Call | Endpoint | What it is for |
|---|---|---|
| discovery | `GET /api/v4/projects?search=TERM&order_by=star_count` | find candidates |
| metadata | `GET /api/v4/projects/:idEnc?license=true` | licence key, ★, forks, topics, **`last_activity_at`** |
| payload | `GET /api/v4/projects/:idEnc/repository/files/:pathEnc/raw?ref=REF` | read the grant, first-hand |
| licence set | `GET /api/v4/projects/:idEnc/repository/tree?path=LICENSES` | the REUSE case, where the root `LICENSE` is a pointer |
| holder | `GET /api/v4/users?username=` | resolve the name in a copyright line |

## Invocation

| Command | What it prints |
|---|---|
| `python3 gitlab_channel.py control` | the three controls, live |
| `python3 gitlab_channel.py search "ai tutor" "autograder"` | hits per term, with ★ and last activity |
| `python3 gitlab_channel.py resolve owner/project …` | HTTP, ★, last activity, detector key |
| `python3 gitlab_channel.py payload owner/project` | payload bytes, anchored family, detector, verdict, licence set if REUSE |
| `python3 test_gitlab_channel.py` | 🟢 **32/32** (offline, fixtures in `data/`) |
| `python3 test_gitlab_channel.py --live` | 🟢 **35/35** (adds the three live controls) |

## The three findings this instrument exists to hold

**`P-GL-1` — the forge's licence field is a classifier, and it is wrong twice in 22.**
`francoisjacquet/rosariosis` → detector `agpl-1.0`, payload **GNU GPL v2, 15,214 B**, byte-identical
to this KB's reading of the same file **on GitHub**. `olatorg/openolat-starter` → detector `ecl-2.0`,
payload **verbatim Apache-2.0** with **zero** occurrences of "Educational Community". Final tally:
**17 agree · 2 wrong · 1 silent (`other` over a plain LGPL-3.0) · 2 REUSE pointers.**

**`P-GL-2` — `license=true` is accepted and silently ignored by the *search* endpoint.** 0 licences
over 534 projects, while the same parameter resolves per-project (control:
`gitlab-org/gitlab-runner` → `mit`). **On this forge a licence-filtered discovery is not lossy, it is
impossible**, and a candidate costs two requests.

**`P-GL-3` — a licence classifier that matches names anywhere in a licence text finds every licence
in every licence.** This pass's first draft reported **6** detector errors; two were its own, because
**MPL-2.0** names the GPL in its secondary-licence clause and **GPL-2.0** names the Lesser GPL in its
closing section. `classify_payload` now accepts a name only when a line *begins* with it. ⚠️ Scanning
"the first N lines" was **not** enough — the suite's negative control proved it and is kept so the
defect stays detectable.

## 🔵 The counter-example that corrects this KB's own rule

`francoisjacquet/Grading_Scale_Generation`: payload is the plain **GPL-2.0** text, in which the
"or later" cannot be established; the detector says `gpl-2.0+`; the project's **`composer.json`
declares `GPL-2.0-or-later`**. **The detector was right and the payload was insufficient** — the
first case in this KB where payload-first *under*-reads a grant. **The rule becomes: payload first,
manifest second, detector never alone.**

## Declared limits — read these before quoting any number from here

1. 🔴 **A 200 confirms, a 302 does not refute.** `gitlab.com/<slug>` answers an unknown path with a
   **302** to sign-in. The HTML channel cannot establish absence on this forge; the API's **404**
   control can, and any withdrawal must use it.
2. 🔴 **Description-driven triage skips 27.9% of what it searched** — 149 of 534 projects carry no
   description at all. The 18 rows this pass published are a **floor, not a census**.
3. ⚠️ **The corpus is polluted.** 67 projects share 12 descriptions (RosarioSIS's own text appears
   **23×**), and **37** slugs are `ecoscan-*deletion_scheduled*` scratch clones.
4. ⚠️ **★ measures a host's audience.** RosarioSIS: 644★ on GitHub, 65★ on GitLab, one project.
5. ⚠️ **Placement is inferred unless stated.** Country attributions come from READMEs and namespaces
   (`saxionnl`, `TIBHannover`, `learntech-rwth`) — evidence, not declarations. The one LATAM-plausible
   row is placed on **Portuguese-language naming alone** and is labelled as such everywhere.
6. 🔴 **`gitlab.com` is one instance.** Every self-hosted GitLab — which is where the European public
   sector actually runs this software — is invisible to this channel. Pre-registered as action **B**
   of pass 23.

## `data/`

| File | What it is |
|---|---|
| `discovery-en.json` | 25 English terms → 534 unique projects, with ★, `last_activity_at`, description and the (always null) search-endpoint licence |
| `discovery-es-pt.json` | 16 Spanish/Portuguese terms → 141 projects, **140 invisible to the English sweep** |
| `resolved.json` | 29 single-project resolutions incl. the **404 negative control** |
| `payloads.json` | the 22 payloads, with bytes, SHA-256 prefix, anchored family and detector key |
| `tally.json` | the agree / wrong / silent / pointer partition, as computed |
| `manifest-evidence.json` | the `composer.json` that settles the `gpl-2.0+` case |
| `latam-candidates.json` | the three real LATAM education projects, **none of which declares a licence** |
