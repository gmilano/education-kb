---
industry: education
region: LATAM
updated: 2026-10-12
---

# `p142-americas-disambiguation` — 🔴 this KB's ten-pass "no LATAM-owned row" finding is WITHDRAWN. There are thirteen.

## What this probe answers, and why it was not pre-registered

[`p142-origin-at-scale`](../p142-origin-at-scale/README.md) ran `ACTION DH` as written and
returned **0 LATAM of 44** — and **0 North America of 44**, from a shelf that holds two
University of Toronto connectors and a McGill one. 🔵 **The second zero is what made the first
one readable**: p141's offset table refuses any offset shared across regions, and every American
offset is shared. The channel never looked.

So the honest next step was not to publish an eleventh null. It was to answer the question with
a channel that can.

## The channel, which is p140's and already proved

p140's `ACTION CU` placed two rows on **a hostname the connector must reach to work** —
`eth-moodle-mcp` → `moodle-app2.let.ethz.ch` ⇒ EMEA. p141 generalised it as `T29`,
*"origin is in the code when the code must REACH a named host"*, and added `uk.ac.ox.ctl`, a
Maven namespace *"Oxford had to control to publish"*.

🔵 **A country-code TLD is that same evidence in that same form.** `sigaa.ufpi.br` is not
flavour: it is the address the code resolves or returns nothing, and `.br` is a namespace only a
Brazilian registrant holds. The booking rule is deliberately narrow:

1. Only rows whose offset `ACTION DH` refused **as ambiguous between North America and LATAM**
   are eligible — 19 rows. An EMEA or APAC row is already placed and is not re-litigated.
2. Hosts come from tracked source only: 🔴 no `node_modules`, no lockfiles, no vendored trees.
   A dependency's hostname places the dependency.
3. Placeholders place nothing. 🔵 **`your-institution.instructure.com` is the most common
   "hostname" on this shelf.**
4. 🔴 **A row is booked only when every country-bearing host agrees on one of the two candidate
   regions.** Disagreement is reported `SPLIT` and stays unplaced.

🔵 **And the conjunction is what makes it safe.** An offset alone under-determines; a host alone
places an *institution*. Together they close: there is no reading on which an author committing
at `-0300` to a connector hardcoded against `sigaa.ufpi.br` is in Greenland.

## Verdict: 🟢 **16 of 19 placed — 13 LATAM and 3 North America**

| region | rows | countries |
|---|---|---|
| 🟢 **LATAM** | 🟢 **13** | **Brazil 9**, **Argentina 3**, **Peru 1** |
| 🟢 **North America** | **3** | **Canada 3** |
| UNMAPPED | 3 | 2 with no country-bearing host, 1 `.edu`-only |

| row | offset | host evidence | region |
|---|---|---|---|
| `Agso-o/sigaa-calendar` | `-0300` ×71 | `sigaa.ufpi.br` | 🟢 LATAM — Brazil |
| `MatheusMach/QuantoFalta` | `-0300` | `sis.sig.uema.br` | 🟢 LATAM — Brazil |
| `RubsNeto/SigaaUI` | `-0300` ×31 | **13 hosts**, `sigaa.sistemas.ufg.br`, `ufj.edu.br` … | 🟢 LATAM — Brazil |
| `trindadetiago/sigaa-caiu` | `-0300` ×25 | **6 hosts**: `sigaa.ufrn.br`, `ufc.br`, `ufpb.br`, `unb.br` … | 🟢 LATAM — Brazil |
| `filipecalegario/auto-sigaa` | `-0300` | `sigaa.ufpe.br` | 🟢 LATAM — Brazil |
| `frjunioalves/suap-mcp` | `-0300` | `suap.ifrn.edu.br`, `suap.ifpi.edu.br` | 🟢 LATAM — Brazil |
| `joojdev/academic-tracker-mcp` | `-0300` | `suap.ifsp.edu.br` | 🟢 LATAM — Brazil |
| `fabrica-de-inovacao/expeditto` | `-0300` ×39 | **11 hosts**: `ifma.edu.br`, `ifto.edu.br`, `lattes.cnpq.br` … | 🟢 LATAM — Brazil |
| `SIU-Toba/docker-guarani` | `-0300` ×28 | `siu.edu.ar`, `colab.siu.edu.ar`, `repositorio.siu.edu.ar` | 🟢 LATAM — Argentina |
| `despedite/siu-guarani` | `-0300` ×11 | `guarani.unq.edu.ar` | 🟢 LATAM — Argentina |
| `eugeborzone/Auto_Grade_Guarani` | `-0300` ×16 | `servicios.unl.edu.ar` | 🟢 LATAM — Argentina |
| `juliancasaburi/siu-guarani-promedio-extension` | `-0300` ×59 | `documentacion.siu.edu.ar` | 🟢 LATAM — Argentina |
| 🟢 `alejooroncoy/campus-cli` | `-0500` ×570 | **16 hosts**, `aulavirtual.upc.edu.pe`, `banner.upc.edu.pe` … | 🟢 **LATAM — Peru** |
| `SleepyPandas/UofT-MCP` | `-0400` ×56 | **7 hosts**: `acorn.utoronto.ca`, `idpz.utorauth.utoronto.ca` … | North America — Canada |
| `skhdemo/uoft-quercus-mcp` | `-0400` ×21 | **5 hosts**: `q.utoronto.ca`, `api.easi.utoronto.ca` … | North America — Canada |
| `luca-dupont2/mcgill-vsb-mcp` | `-0400` | `vsb.mcgill.ca` | North America — Canada |
| 🟡 `karkarkins/BlackboardAssistantMCP` | `-0400` ×23 | only `ncat.blackboard.com` — a **vendor tenancy**, no country in the name | UNMAPPED |
| 🔴 `nitsuah/bb-mcp` | `-0400` ×191 | every host is `example.*` | UNMAPPED |
| 🟡 `ruud0/aula-virtual-mcp` | `-0400` | `aula-virtual.unav.edu` — 🔴 **Spain** | UNMAPPED |

## 🟢 The control that matters: the probe reproduces a placement made by another channel

`alejooroncoy/campus-cli` is already on `agents/top.md` as **"LATAM (Peru) … targets UPC's Aula
Virtual"**, placed passes ago by *reading its README*. This probe places it in Peru from
sixteen hardcoded `upc.edu.pe` hosts, without being told. 🟢 **An instrument that independently
reproduces a known answer on a known row is one that can be trusted on the twelve unknown ones.**

## 🔴 What this probe CANNOT do, declared because it is a LATAM-shaped hole

Four ccTLDs are excluded outright, because each is a homograph of a filename extension that
appears in ordinary source trees, and **each produced a false booking in this probe's first
draft**:

| ccTLD | country | collides with | the false booking it produced |
|---|---|---|---|
| 🔴 `.py` | Paraguay | **Python source** | `scraper.py` placed `BlackboardAssistantMCP` in LATAM; `synth.py` placed `bb-mcp`; six `*.py` "hosts" split the Canadian `UofT-MCP` row |
| 🔴 `.do` | Dominican Republic | **Struts/JSP action** — 🔵 *and SIGAA itself uses it* | `logar.do`, `vertelalogin.do` |
| 🔴 `.cu` | Cuba | CUDA source | — |
| 🔴 `.cl` | Chile | OpenCL source | — |

🔴 **So this instrument cannot place a repository in Paraguay, the Dominican Republic, Cuba or
Chile at all.** On the question this KB has been asking for ten passes that is a real hole, and
a probe that books Paraguay off `auth.py` is worse than one that admits the gap.

🔵 **A second guard does the heavy lifting and costs nothing real:** a host must have **three or
more labels**. A registrable name is `name.tld`; a host code must reach is `service.name.tld`.
That single rule separated every true positive from every false positive in this population —
dropping `scraper.py`, `logar.do`, `http.us`, `campus.edu` and the bare public suffixes
`edu.br` / `gov.br` / `edu.ar`, while keeping `sigaa.ufpi.br`, `guarani.unq.edu.ar`,
`vsb.mcgill.ca` and `aulavirtual.upc.edu.pe`.

## 🔵 `.edu` is not a US signal, and this population proves it rather than assuming it

`.edu` registration has been restricted to accredited US institutions since 2001, which looks
like exactly the `uk.ac.ox` argument p141 accepted. 🔴 **But `ruud0/aula-virtual-mcp` hardcodes
`BASE_URL = "https://aula-virtual.unav.edu"` — the Universidad de Navarra, in Spain** — on a
pre-restriction registration, and names *Navarra* and *Spain* in its own source. One
counterexample inside the subject set settles it: `.edu` is recorded as corroboration and never
booked. 🟡 **That row is EMEA on a prose channel and `UNMAPPED` on this one, and it is left
`UNMAPPED` rather than quietly upgraded.**

## 🟡 One row names an institution without naming a country, and that is a third channel

`karkarkins/BlackboardAssistantMCP` reaches `ncat.blackboard.com` — a **tenancy subdomain of the
vendor's own `.com`**. It identifies an institution precisely and carries no country, so placing
it needs an institution→country lookup this probe does not have and will not guess at.
Registered as `ACTION DK` rather than booked.

## Reproduce

```sh
python3 -I americas.py "owner/repo=/path/to/clone=-0300" ...
python3 -I test_americas.py     # 12 tests, including all four homograph regressions
```

Committed: [`result.2026-10-12-p142.tsv`](result.2026-10-12-p142.tsv),
[`detail.2026-10-12-p142.txt`](detail.2026-10-12-p142.txt).
