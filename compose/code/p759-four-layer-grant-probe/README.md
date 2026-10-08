# `p759-four-layer-grant-probe`

**Pass 59, 2026-10-08.** Locates licence grants across **four layers**. Registered because
`Gap 278` said this KB's pre-flights were prose, and because `P760` showed a one-layer probe
mislabels one repo in five as ungranted.

## What it refuses to do, and why that is the point

It **does not classify**. Classification goes to `compose/code/p419-copyleft-identity/`.

That boundary *is* this pass's finding (`P755`, Trend 1). Pass 59 hand-rolled a `§13 present`
test and it read **`moodle/moodle` as AGPL-3.0** — the most widely deployed education platform in
the world, moved into the one copyleft band that has a network clause. The cause is `P753`:

| payload | §13 heading as written | `grep -ci affero` |
|---|---|---|
| `moodle/moodle` `COPYING.txt` @ `f205347` (**GPL-3.0**) | `13. Use with the GNU Affero General Public License.` | **3** |
| `openedx/edx-platform` `LICENSE` @ `bf699a5` (**AGPL-3.0**) | `13. Remote Network Interaction; Use with the GNU General Public License.` | 15 |

Every GNU text names its relatives, so a body-substring test mislabels in **both** directions.
`p419` has handled this correctly since **pass 123** — title-line window in `familia()`, kinship
quarantined in `menciones_cruzadas()` (*"parentesco, nunca identidad"*), and a named regression case
(`ahmedEid1/lumen`). It did not need to be rewritten; it needed to be called.

**The rule: re-measure the data every pass; reuse the instrument.** (`P713`'s complement.)

## The four layers

| # | Layer | Named case that requires it |
|---|---|---|
| 1 | licence file, 15 filenames | most repos |
| 2 | **below a reference inside that file** | `openeducat/openeducat_erp` → LGPL-3.0 (`P742`) — `LICENSE` opens with a `COPYRIGHT` pointer that 404s, grant is underneath |
| 3 | manifest / registry — the only **dated** oracle | `PyLTI1p3` → MIT, PyPI v2.0.0 **2022-11-20** (`P741`, `P766`) |
| 4 | **source-file headers, no licence file at all** | `onbirdev/moodle-webservice_mcp` → GPL-3.0-or-later (`P757`) — 0 of 15 filenames, grant in every `.php` |

Only when all four are empty is the verdict **ALL RIGHTS RESERVED** — a verdict, not an absence
(`P476`, `P628`).

## Conventions it enforces

- **Provenance = `refs/heads` SHA from `git ls-remote`** (`P732`). `api.github.com` is `403` here,
  and `raw.githubusercontent.com` silently resolves `master` to the default branch, so a branch
  name is not provenance (`P714`).
- **Existence is never `curl -sI https://github.com/<slug>`** (`P770`). That channel returns **403
  for a real repo and 403 for an invented one** — it is blind. Existence is `ls-remote` returning a
  SHA, cross-checked against `raw` answering 200/404.
- **Stored bytes** (`P704`). Bytes identify a **text**, never a **family**: GPL-3.0 is 35 147 B and
  AGPL-3.0 is 35 136 B — **11 bytes apart** (`P754`).

## Controls (`--self-test`)

Run **4/4 green** on 2026-10-08, **from inside this cloned repository**:

```
OK   github.com HTML is blind (403 for real AND invented) -- do not use it (P770)
OK   ls-remote discriminates (real=SHA, invented=fail)
OK   P753 holds: GPL-3.0 payload names Affero 3x, and its TITLE LINE does not
OK   P757 holds: LICENSE=404 and the source header grants GPL -- layer 1 alone would say 'ungranted'
```

Control 1 is a **negative** control in the `P237` sense: it keeps the blind channel detectable, so
that anyone re-adding `curl -sI` as a verification step trips it. If github.com HTML ever starts
discriminating, the control reports `CHANGED` rather than failing — a capability change to
re-measure (`P713`), not a defect.

`P541` guard: no argument, an empty string, and a malformed slug each exit **2**.

## Usage

```bash
bash probe.sh --self-test
bash probe.sh openeducat/openeducat_erp onbirdev/moodle-webservice_mcp
```

## What it does not claim

- **No rate.** Five named samples are not a sample frame, and `P744`'s policy-layer denial of mass
  third-party slug enumeration still forbids the sweep that would build one (`Gap 277`).
- **No licence-family verdict.** See above — that is `p419`'s job.
- **No policy verdict.** A grant is one axis; whether the *function* is lawful in the deployment
  jurisdiction is a second, orthogonal one (`P764`, `Gap 278`). MIT clears the first and says
  nothing about the second: `algorithm0r/canvas-lms-mcp` is MIT and grades.
