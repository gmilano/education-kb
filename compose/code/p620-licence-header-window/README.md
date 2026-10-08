---
industry: education
region: Global
updated: 2026-10-08
---

# `p620` — the header window is measured on **plain text**, and `.md` / `.html` payloads fall outside it

🆕 **Pass 51 of 2026-10-08.**

## What `P419` got right, and this folder does not touch

`p419-copyleft-identity` established the rule this folder depends on: **the licence family
is read from the HEADER** — title plus `Version N`, the first two non-empty lines — and
never from the body, because a pristine licence text *names its relatives* (GPL-3.0 §13
names AGPL; GPL-2.0 closes naming the Lesser GPL). `p419`'s own suite refuted a wider
window: at `n=6` the §13 heading re-enters it and the instrument recommits the defect it
was built to fix. **`n=2` is measured, not chosen, and this folder keeps it.**

## 🔴 The defect

`n=2` was measured against payloads whose first two lines *are* `TITLE` + `Version N`.
A `LICENSE.md` need not be one. `idempiere/idempiere` ships `HEAD/LICENSE.md` whose first
non-empty line is `<center>`, so the window admits `<center>` and the title — and
`Version 2, June 1991`, the third non-empty line, falls **outside** it. `familia()`
answers `GPL-?`: *"names GPL without a version — not inferred (`P286`)"*.

🔵 **Nothing went red, because `GPL-?` is a legal answer.** It is also the answer that
stops a commercial verdict: GPL-2.0 and GPL-3.0 differ on the patent grant and on
Apache-2.0 compatibility, which is exactly the column a client contract reads.

🔵 **And the axis is not "Markdown".** A `#` heading does *not* break the window —
`_encabezado` collapses whitespace, so `# GNU General Public License` / `Version 3` still
reads `GPL-3.0`. What breaks it is **any extra non-empty line between the title and the
version**, which `<center>` is. The suite carries that correction as a case, because this
folder's first draft asserted the wrong cause.

## The repair, and what it deliberately does not fix

A **pre-stage**: drop markup-only lines, strip inline tags and Markdown lead markers, then
hand the text to `p419`'s **unmodified** `familia()` (`P126` — import, do not rewrite). The
rule still names the family; only what counts as a "line" changes.

🔴 **Declared blind spot, published rather than cured.** `idempiere/idempiere` also ships
`HEAD/license.html`, whose first heading is **`Compiere Public License`** and whose second
is `GNU General Public License`. Raw, that window matches no family at all —
`UNCLASSIFIED`. Unwrapped, the two lines are two licence **titles**, so the version is
*still* outside the window and the verdict is `GPL-?`. That case is classed
**`WINDOW-STILL-SHORT`** and left red-flagged. **Widening the window to `n=3` would pass
it and re-admit body text, reintroducing `P419`'s original defect** — tuning until green,
which this corpus has already caught itself doing once.

## Measured over the shelf

Every `.md` / `.html` licence payload in
`p444-root-vs-tree-family/payloads.licensed.2026-10-07.tsv` — **26 of 412 rows (6.3 %)** —
re-fetched at `HEAD` on 2026-10-08, plus the two `idempiere` payloads this pass found.
**28 payloads, all 200.**

| Verdict | n | What it means |
|---|---|---|
| `AGREE` | **22** | no markup in the window; the repair is a no-op |
| 🟢 `REPAIRED` | **5** | a licence **version** recovered that the shelf did not have |
| 🔴 `WINDOW-STILL-SHORT` | **1** | `idempiere/idempiere` `license.html` — the declared blind spot |

The five repaired rows, and what each gains:

| Row | `p444` family | 🟢 Read here | Recorded payload size |
|---|---|---|---|
| [`idempiere/idempiere`](https://github.com/idempiere/idempiere) `LICENSE.md` | — (not on the shelf before this pass) | 🟢 **GPL-2.0** | 15,057 B |
| [`caiocarvalhofre/moodle-mod_maici`](https://github.com/caiocarvalhofre/moodle-mod_maici) | `GPL` | 🟢 **GPL-3.0** | 35,178 B |
| [`cgrevisse/moodle-qbank_genai`](https://github.com/cgrevisse/moodle-qbank_genai) | `GPL` | 🟢 **GPL-3.0** | 35,178 B |
| [`yedidiaklein/moodle-local_aiquestions`](https://github.com/yedidiaklein/moodle-local_aiquestions) | `GPL` | 🟢 **GPL-3.0** | 35,178 B |
| [`michael-milette/moodle-local_aiid`](https://github.com/michael-milette/moodle-local_aiid) | `GPL` | 🟢 **GPL-3.0** | 32,477 B |

🔵 **The two axes turn out to be one.** Those four Moodle plugins are exactly the
**size outliers** in the shelf's GPL distribution (35,178 ×3 and 32,477 against a modal
35,149). They are outliers *because they are Markdown wrappers* — the same property that
cost them their version. The size column never carried a file-format axis, so the
outliers read as unexplained variance.

🟡 **Honest limit, measured not argued:** 7 payloads answer `UNCLASSIFIED` both raw and
unwrapped, two of which `p444`'s body-reading `family_of` calls `CC-BY`
(`Jona-Zwetsloot/Somtoday-Mod`, `sign/translate`). That is not this repair failing — a
header rule cannot name a grant that has no title line, and the two instruments answer
different questions. It is recorded so the `22 AGREE` is not read as `22 identified`.

## Reproduce

```sh
cd compose/code/p620-licence-header-window
python3 test_window.py                  # 🟢 30/30 — no network
python3 probe_window.py <payload> ...   # the per-payload read; result.2026-10-08.tsv
```

The suite is offline: every case is a literal payload fragment, and two are **negative
controls** — a GPL payload with no version anywhere (the repair must still answer `GPL-?`
and must not invent one) and a GPL-3.0 whose body names AGPL (the repair must still answer
`GPL-3.0`, proving it did not widen the window). Two further assertions per case check
that the strip neither **invents** a word nor **deletes** a family-naming one.

🔵 **The suite's first run was 16/24, and three of the eight failures were this folder's
own mis-specifications, not code defects** — the word-conservation control split on
whitespace, so `<pre>Copyright` → `Copyright` looked like an invented word; the HTML case
was predicted as `REPAIRED` and is actually worse (`UNCLASSIFIED` raw); and the
"Markdown breaks the window" cause was wrong. All three are kept in the file as comments,
because the corrected expectation is the finding.
