# `p531-ledger-gate` — the control in front of the address ledger

**`Gap 530-C`.** `p530` built [`../../../ingest/address-ledger.py`](../../../ingest/address-ledger.py),
declared it the control that runs in front of every pass, and ran its only
correctness check — section-pass monotonicity — **by hand, once, inline in the
pass write-up**. Nine passes of instruments had gone unattested. This is that
check as a test.

## What it found on its first automated run

`530-C` asked for the four known monotonicity violations to be **allowlisted**.
🔴 **Two of the four were not history. They were the instrument.**

| `530-C`'s "known violation" | Verdict |
|---|---|
| `intel/open-gaps.md:17901` — `## Actions opened by p133` | 🔴 **Instrument.** A roll-up heading counted as a pass section. `NOT_A_SECTION` excluded `gaps opened` and `Gaps CLOSED` **by name** and missed this dialect. |
| `repos/trending.md:16626` — `## 2026-10-17 (pass 277) — … refuted `p276`'s …` | 🔴 **Instrument.** `\bPass\s+` was case-sensitive, so the lower-case `pass 277` was invisible and the first token matched was the `p276` **cited in the same title**. |
| `agents/trending.md:45140` — `pase 126` | 🟢 **Genuine** — below a `## History (earlier passes, preserved verbatim)` divider. |
| `repos/trending.md:36223` — `pase 126` | 🟢 **Genuine** — same rewrite boundary. |

🔴 **The second one is not an edge case.** `## … (pass N) …` and
`## Live gaps declared by pass N` account for **234 `##` headings** across the
three history files and the instrument matched **none** of them. A heading it
does not recognise does not reset the section pointer, so every address first
described under one was attributed to the **newer pass above it**. Counting them
correctly takes the corpus from **1 128 sections to 1 340** — **212 sections,
15.8%, carried the wrong pass.**

🔵 **And one proposed fix was refuted by this gate's own `C1`, before it shipped.**
The obvious repair is a blanket `re.I` on the dialect regex. Run that way, the
section count went to **1 375** and the violation set from 4 to **13**, with
"ascents" to `p795`, `p865`, `p1024`. Those are **proposal** numbers: this base
writes passes lower-case (`p530`) and proposals upper-case (`P553`), two
namespaces separated **by the case of one letter**. So only the *word* forms may
be case-folded; the bare `pNNN` token must stay case-sensitive.

🔴 **A third defect, in this gate, found by running it twice.** `C1`'s allowlist
was first keyed `(file, line, prev, this)`. It failed on `p531`'s **own** write:
these files are **append-only at the top**, so every pass shifts every line below
its new section and a line-keyed allowlist goes stale **once per pass**. 🔵 A gate
that cries wolf on every run teaches the next pass to ignore it, which is worse
than no gate. The key is now the **pass pair at the boundary** — the invariant —
and the line number is reported as context. `test_ledger_gate.py` refuses an
allowlist entry that looks like it carries a line number.

## Controls

| | Asserts |
|---|---|
| `C1` | the **2** genuine ascending violations reproduce **exactly** — none missing (the check still works), none extra (no new disorder, no new mis-read dialect) |
| `C2` | no roll-up or forward-registration heading is counted as a section |
| `C3` | a heading whose own pass reads `(pass NNN)` resolves to `NNN`, even when it cites another `pNNN` in the same line |
| `C4` | a known-**filed** address reports `filed_on` non-empty |
| `C5` | a known **history-only** address reports `-`. The fixture is AGPL-3.0, so no pass can shelve it and the control cannot rot |
| `C6` | **RATCHET** — the ledger's address count never falls between passes without a stated reason (`LEDGER_RATCHET_REASON=…`) |

## Running it

```
make gate-ledger                 # wired into `make hooks`
python3 -I compose/code/p531-ledger-gate/ledger_gate.py --repo-root .
python3 -I compose/code/p531-ledger-gate/ledger_gate.py --bless-ratchet   # raise C6's floor
cd compose/code/p531-ledger-gate && python3 test_ledger_gate.py           # the unit controls
```

🟡 **Attestation, stated exactly.** `p531` ran `ledger_gate.py` against the real
files and it **passes, 6/6**, and ran `test_ledger_gate.py`'s synthetic controls.
🔴 **It was not run through `make hooks`:** that session could not execute
repo-resident code, so the recipe wiring below is written and unexercised. The
first pass that can run `make hooks` should confirm it, and say so.
