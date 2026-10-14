# `p209-masked-class-sample` — read the rows the comparator cannot see

## Why this exists

🔴 **p208 proved the p205–p208 licence comparator is BLIND on `85`% of its own column.** It
compared a row's true grant family against the union of every token on every line naming the
repository, so a repository whose true family is printed at two or more sites **cannot produce a
mismatch however wrong a single cell is**. 🟢 **`152` of `179` census rows are masked by
construction**
([`evidence/comparator-reach.2026-10-14-p208.tsv`](../../../evidence/comparator-reach.2026-10-14-p208.tsv)).

🔵 **Three passes reported that column clean. On the masked `85`% that report carried no
information: an instrument that cannot fail cannot pass either.**

🟢 **And discovery is saturated on a sixth independent reading** — `0`–`1` new qualifying education
agents per pass, `0` new foundational repos. 🔵 **So the marginal pass is worth more spent reading
shelf rows against their own repositories than running a seventh discovery sweep.** This tool
picks which rows to read.

## What it does

Ranks the masked rows by **exposure in [`compose/patterns.md`](../../patterns.md)** — recipes are
what a client engagement actually reads, and p208's one true positive
(`towardsai/ai-tutor-app`, published `MIT`, blob `Apache-2.0`) lived in exactly that population.

```sh
python3 -I rank_masked.py --limit 10                  # the batch p209 read
python3 -I rank_masked.py --limit 10 --skip-verified  # the batch p210 should read
```

Offline, deterministic, writes nothing. Inputs: the p208 census and the recipe shelf.
`--skip-verified` subtracts the rows already read first-hand in
[`evidence/masked-class-sample.2026-10-14-p209.tsv`](../../../evidence/masked-class-sample.2026-10-14-p209.tsv),
so successive batches never re-spend on the same repository.

## p209's result

🟢 **`10`/`10` grant families correct, `0` corrections to ship.** 🔴 **Not a clean bill:** with
`n = 10` and `0` errors the point estimate is `0`% and the **`95`% upper bound is `~26`%**
(rule of three), so a masked-class error rate of one row in four is still not excluded. 🟢 **What
it does exclude is the pessimistic reading of p208 — the highest-exposure masked rows are not
riddled with p208-shaped errors.**

🆕 🔴 **Side finding, and it is a trap for any automated successor:** GitHub classifies **no
licence at all** for [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) — unnamed sidebar
`License` link, and the API's `license` field is the same detection — while its blob is a verbatim
`Apache License, Version 2.0`, `197` lines / `10.7` KB. 🟢 **An unnamed sidebar licence is a prompt
to open the blob, never a finding.**

## Two honest notes on the method

🔴 **The ordering unit matters and p209's batch was picked with a different one.** p209 ranked by
**lines** containing the repo name (`grep -c`); this script ranks by **occurrences**
(`str.count`). 🟢 **The two agree on `9` of `10` rows**; the disagreement is
[`frappe/lms`](https://github.com/frappe/lms) (in p209's batch, `12` lines) versus
`openolat/OpenOLAT` (`19` occurrences). 🔵 **Occurrences is the better unit — a row named three
times on one line is exposed three times — so later batches should use this script, not `grep -c`.**

🔴 **`openolat/OpenOLAT` is the SAME repository as `OpenOLAT/OpenOLAT`, which p209 already
verified.** 🟢 **It tops the `--skip-verified` list only because the census carries both
casings as separate rows** — the known casefold defect
([`p288-agpl-casefold`](../p288-agpl-casefold/)). 🔵 **p210 should fold it, not re-read it**, and
the census itself wants a casefold pass.

## What this leaves for later passes

🟢 **`142` masked rows pending, and `58` of them appear in NO recipe at all.** 🔵 **Those `58` are
the cheapest to defer and the safest to leave unread: a wrong cell that no recipe cites cannot
reach a deliverable.** 🔴 **The `84` recipe-cited rows are the real backlog — `~8` more batches of
ten at this pass's precision, or a cheaper per-row channel.**

🔴 **`ACTION PV` *(opened in [`repos/foundations.md`](../../../repos/foundations.md) p209)* is the
other half of the job: the grant is not the only risk a row carries.
[`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) is
`Apache-2.0` and correct and has **`6`★ against `13` recipe sites** — sweep for ★`< 50` AND recipe
sites `≥ 5`, which is the shape that hides a bus-factor dependency inside a sound grant.
