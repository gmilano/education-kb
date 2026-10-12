---
industry: education
region: LATAM
updated: 2026-10-12
---

# `p143-cctld-url-context` — `ACTION DN`: the four-country hole is closed, and it changed no row

🟢 **Falsifier silent: 19 of 19 regions reproduced, all 16 placed rows retained.** The two
rules can both hold. 🔴 **And zero rows changed region**, because the only row carrying a
re-admitted ccTLD was already placed by another country.

## What was registered

> 🟡 **`ACTION DN`** — close the four-country hole: re-admit `.py`, `.do`, `.cu` and `.cl`
> behind a URL-context requirement (`://` or `www.` immediately preceding), then re-run the
> 19-row eligible population.
> 🔴 **Refuted if requiring URL context loses any of the 16 rows already placed** — which
> would mean the two rules cannot both hold and the homograph exclusion must stand as a
> permanent limit.

## The hole

p142 excluded four ccTLDs outright, each a homograph of a filename extension:

| ccTLD | country | collides with |
|---|---|---|
| `.py` | Paraguay | Python — `scraper.py` |
| `.do` | Dominican Republic | Struts/JSP — `logar.do`, and **SIGAA itself uses it** |
| `.cu` | Cuba | CUDA |
| `.cl` | Chile | OpenCL |

🔴 **The declared cost: this KB could not place a repository in Paraguay, the Dominican
Republic, Cuba or Chile at all** — and Chile is the one LATAM country this KB already cites
a national AI policy for.

## The rule

A host bearing one of the four is admitted **only** when the match is immediately preceded
by `://` or `www.`. Everything else of p142's booking rule is unchanged: ≥3 labels, no
placeholders, tracked source only, no `node_modules` or lockfiles, and a row books only
when every country-bearing host agrees on one region.

🔵 **This is `T29` applied literally rather than a heuristic bolted on.** `import scraper.py`
and `redirect("logar.do")` never carry a scheme; `https://www.una.py/sistema` does. The
scheme is what makes a string *an address the code must reach*.

🔴 **The 15 unrestricted ccTLDs keep p142's rule and do NOT require URL context**, because
`sigaa.ufpi.br` is unambiguous without one and demanding a scheme would drop it. 🔵 **That
asymmetry is the entire content of this probe.**

## Falsifier check — region by region

🟢 **19 of 19 reproduced, 0 changed, 16 placed both times.**

| region | p142 | p143 |
|---|---|---|
| LATAM | 13 | 🟢 **13** |
| North America | 3 | 🟢 **3** |
| UNMAPPED | 3 | 🟢 **3** |

(The 3 `UNMAPPED` here are p142's; `ACTION DK` separately places one of them, which is a
different channel and is not folded into this table.)

## 🟢 The rule works, demonstrated on real hosts

`alejooroncoy/campus-cli` now yields two hosts the restricted list had been refusing:

| host | country | admitted on |
|---|---|---|
| 🆕 `juris.pjud.cl` | 🟢 **Chile** — the Judicial Branch's jurisprudence service | `://` |
| 🆕 `revistas.uh.cu` | 🟢 **Cuba** — Universidad de La Habana journals | `://` |

🟢 **And the same row shows the refusal working**: `revistas.uh.cu` appears **5 further
times without a scheme** — as `url.hostname === 'revistas.uh.cu'` comparisons — and those
five are correctly refused while the one true URL is admitted. 🔵 **Both halves of the rule
fire on the same host in the same file**, which is the cleanest validation available.

## 🔴 What it did not do

**Zero rows changed region.** `campus-cli` was already LATAM on 30 Peruvian hosts, so
adding Chile and Cuba changed the country list and not the booking.

🔴 **And Paraguay and the Dominican Republic remain unexercised.** No host under `.py` or
`.do` with URL context occurs anywhere in the 19-row population. 🔵 **So the capability is
demonstrated for two of the four countries and merely *unblocked* for the other two** —
which is a different claim from "the hole is closed", and this file makes it rather than
the stronger one.

## The honest note on reproduction

🔵 **This run is not byte-identical to p142's.** The clones are fresh, and
`alejooroncoy/campus-cli` (581 commits, HEAD 2026-10-11) has grown — p142 read 16 Peruvian
hosts where this reads 30. 🟢 **The falsifier is about REGION, and every region reproduced**;
the host counts differ because the repositories moved, not because the rule did.

## Run it

```
python3 -I cctld_urlctx.py subject=clone=offset [...]   # result.2026-10-12-p143.tsv
```
