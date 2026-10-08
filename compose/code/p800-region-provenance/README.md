---
industry: education
region: Global
updated: 2026-10-08
---

# `P800` — a region comes from an institution the artefact names, never from a person's name

Artefacts and suite of the **sixty-fifth pass (2026-10-08)**. 🟢 **8/8 green under `python3 -I`.**

## Why the pass needed the rule

🟢 This pass admitted three rows whose maintainers carry names a reader could file under a country
in about a second, and 🔴 **in all three the repository says nothing about where it is built or
deployed.** 🔵 `region` is a **closed field this KB filters on**, so a guess does not read as a guess
downstream — it reads as **data**.

## The contrast that makes the rule, both halves measured

| row | placed? | region | by what |
|---|---|---|---|
| `educredentials/ec-issuer` | 🟢 yes | **EMEA** | its README points deployment at `git.ia.surfsara.nl/surf-internal/…` — **SURF**, the Dutch national education-ICT cooperative — and it implements the **European Learner Model** |
| `GhaithAlHallak8/moodler-mcp` | 🔴 no | **Global** | grep returned nothing placing it |
| `Jawadh-Salih/moodle-mcp-server` | 🔴 no | **Global** | grep returned nothing placing it |
| `TanimowoObaloluwaDavid/credential-lens` | 🔴 no | **Global** | grep returned nothing placing it |

🟢 **Grepped, not assumed.** The probe looked for
`universit|ministr|government|deploy|country|region|instituti|EU|GDPR|FERPA|AI Act|.edu|.ac.`
across each README. 🔵 **An institution and a standard place a row; a surname does not.**

## 🔵 And it is not only an accuracy rule

🔴 Inferring a person's nationality from their name to fill a business field is wrong twice over:
**unreliable**, and **not this shelf's business**. 🟢 `Global` is the honest value and it costs
nothing.

## The negative control

🟢 `test_a_maintainer_name_never_moves_a_region` asserts that all three unplaced rows — each of
which **does** carry a personal name — resolve to `Global`. 🔵 If a name could place a row, that
assertion would fail. It is the file.
