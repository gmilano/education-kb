# `p223-selfclaim-date-gate` — does this KB assert what it has already refuted?

**Pass:** 223 · **Date:** 2026-10-15 · **Status:** wired, tested, fires on real cells

## Why it exists

This KB has flagged the claim *"EU AI Act high-risk for education, full effect
August 2026"* as stale **four times** — p196, p198, and twice more in sources
logged in `README.md`. Every one of those flags was aimed at an **inbound
source**. None of them asked whether the KB **itself** says it.

It does. `intel/market.md:48` — p222's live EMEA opportunity paragraph, the
sentence a studio reads before pricing an EMEA engagement — states it as the
KB's own instrument line, unqualified, three passes *after* the same file
recorded Reg. (EU) `2026/1744` moving Annex III education to `2027-12-02`.

The correction existed. It was ~`900` lines below the error.

## What it does

For every `*.md` outside `archive/`, a line is a **candidate** when it carries
both an AI-Act/high-risk/Annex-III token and an *August-2026 full-application*
token. Candidates are then **classified rather than dumped**:

| verdict | meaning | build |
|---|---|---|
| `CORRECTED` | the right date or an explicit verdict is on the same line | 🟢 clean |
| `QUOTED` | the span sits inside quotation marks — the KB reporting a source | 🟢 clean |
| `QUOTED-MULTILINE` | unpaired quote char on one side: the quotation opened or closes on another line | 🟢 clean |
| `ATTRIBUTED` | a reporting verb governs it, but no verdict follows | 🟡 warn |
| `ASSERTED` | none of the above — the KB is stating it | 🔴 fail |

Two dates that look similar are deliberately **not** caught: Article `50`
transparency really is in force `2026-08-02`, and *entry into force* in July
`2026` is not *application*. Both are controls.

## The defect this instrument made itself, and the rule that came out of it

The first draft exonerated any line containing a quote character **anywhere**.
`market.md:48` contains the phrase `"EMEA readiness"` — so the headline defect
was invisible to the gate built to find it.

🔴 **The unit is the matched SPAN, not the line.** Same shape as p215
(`ABSENT` meant *not at the path probed*) and p222 (a token vs its ecosystem
grammar). Seventh unit-mismatch in this KB's own instruments.

## Run it

```bash
python3 -I compose/code/p223-selfclaim-date-gate/gate.py --self-test   # 11 controls
python3 -I compose/code/p223-selfclaim-date-gate/gate.py .             # TSV, exit 1 on ASSERTED
```

`11`/`11` controls pass; `7` of them must **not** fail the build. Evidence from
the run that motivated the corrections:
[`sa-selfclaim-dates.2026-10-15-p223.tsv`](../../../evidence/sa-selfclaim-dates.2026-10-15-p223.tsv).

## Wiring it into `make hooks`

```make
hooks: ## fail the build on a self-asserted refuted date
	python3 -I compose/code/p223-selfclaim-date-gate/gate.py . || exit 1
```

## Generalising it (what the next pass should do, not this one)

The date is hard-coded because the defect was. The reusable shape is a
`(subject, refuted-claim, correction)` table read from a file, so that the next
refuted cell — a licence range, a market figure, a ministry date — gets a gate
without new code. `ACTION SA` registers that.
