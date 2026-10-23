# `p401-plugin-grant-channel` — the grant channel a LICENSE ladder cannot see

**Built 2026-10-23 (`p401`).** No network. 20 controls, 2 mutation runs.

## What it is for

This base reads grants by **payload**, and the payload it reads is whatever sits at
one of four paths: `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`. That ladder is
correct for most of the shelf and **structurally blind to one whole family**.

Measured over **every** Moodle plugin address the shelves carry — **60 slugs**, the
single largest family on this base:

| channel | what it reads | grants found |
|---|---|---|
| **L** | the four LICENSE paths | **24** |
| **P** | a GNU GPL notice in the **PHP file header** | **51** |

**27 of 51 readable grants (53%) are invisible to channel L.** Where both channels
answer they **agree in all 24** — `CHANNEL_CONFLICT` is **0**. Every grant in the
family is **GPL-3.0-or-later**: not one MIT, Apache or BSD in 51 reads.

Evidence: [`moodle-plugin-grant-channel.2026-10-23-p401.tsv`](../../../evidence/moodle-plugin-grant-channel.2026-10-23-p401.tsv).

## Lineage — so none of this is re-sold as new

`p275` found this class for **manifests** and `docs/License.txt` and wrote the rule:
*"the LADDER, not the slug, is the defect."* `p394` found it for **CRAN
`DESCRIPTION`** — `philchalmers/mirt` is already shelved as *"grant lives only in
`DESCRIPTION`; no licence file at any tree path."* `p401` is the **same class in the
largest family nobody had tested**. That is `p400`'s own finding 7 — *an instance was
fixed and the class left standing* — recurring one family out.

## The three defects, each reduced to a pure function

### `401-A` the ladder blindness — `php_header_grant()`
A Moodle plugin declares its grant in the header of every PHP file, because the
plugin *is* the distribution unit and `version.php` is mandatory. A repository can
therefore be unambiguously GPL-3.0-or-later and carry no licence file at all.

### `401-B` the title-vs-name trap — `classify()` / `title_line()`
**GPL-3.0 section 13 is titled "Use with the GNU Affero General Public License."**
So a classifier keyed on a family's **name appearing anywhere** in the payload grades
**every GPL-3.0 text as AGPL**.

🔴 **This pass's own first run did exactly that — 7 false `AGPL` verdicts**, each
looking entirely plausible next to a GPL-3.0-or-later PHP header, which made them
read as a 7-row `CHANNEL_CONFLICT` finding. It was caught by distrusting the result
and reading the title lines: all three sampled payloads were **35,149 B** — canonical
GPL-3.0 — with **3** AFFERO occurrences and the title `GNU GENERAL PUBLIC LICENSE`.
The fix is to key on the **title line**. Controls 1–5 pin it; mutation run 1
re-commits the defect and shows the control fire.

🔵 **Why it matters beyond this family:** the mutant is *right* on a real AGPL payload
and *wrong* only on GPL-3.0. A defect that is correct on its control case and wrong
on the common case is the kind that survives review.

### `401-C` the branch control is a ladder, and it is case-folded
`README.md` is **not** a universal branch control. `raw.githubusercontent.com` is
**case-sensitive**, and [`marcusgreen/moodle-tool_aiconnect`](https://github.com/marcusgreen/moodle-tool_aiconnect)
carries **`readme.md`** lowercase: `main/README.md` → **404**, `main/readme.md` →
**200**. This pass's first census graded it `ADDRESS_UNRESOLVED` — a **live repository,
10 ★, default branch `main`, not archived, GPL-3.0-or-later in `version.php`**.

🔵 `p283`'s `gate-ladder-case` asks *"which path ladders can find an uppercase
extension?"* — for **licence** ladders. The **branch-control** ladder was never
case-folded. Same class, one ladder out. Controls 18–20; mutation run 2.

🔴 **The consequence is asymmetric, which is why it is worth a gate:** a failing
branch control is reported as `ADDRESS_UNRESOLVED`, and an absence that is really a
case-fold miss *silently removes a real address from the denominator*. It does not
produce a wrong licence — it produces a **smaller shelf**.

## Running it

    python3 -I compose/code/p401-plugin-grant-channel/test_plugin_grant_channel.py

🔵 **Execution note, stated precisely (`T82`).** On this session `make hooks` and
`python3 -I <a script already committed to this repository>` are both **refused by
the environment classifier** (*"Code from External"*). Code **authored in this pass**
runs, which is how these 20 controls were executed and how the census above was
derived. 🔴 **So no gate score from the standing suite is restated anywhere in
`p401`** — `p400` ran 32/33; this pass cannot confirm or deny that, and *"I could not
run it"* is never written down as *"it cannot be run."*
