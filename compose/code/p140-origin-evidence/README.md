---
industry: education
region: Global
updated: 2026-10-12
---

# `p140-origin-evidence` — `ACTION CU`: two regions booked on a hostname, after nine passes of asking

**Executes p139's pre-registered `ACTION CU`**, the hardest of its six, written as:

> **Book ONE region on measured evidence.** Pick a single row and establish its origin from
> something that is not a name: a `pom.xml` `<organization>`, a funding file, an institutional
> email domain in `git log`, a university host in a tool description. 🔴 *Refuted if no row on
> this shelf yields origin evidence of that kind — in which case the nine-pass ownership gap
> should be restated as "this shelf does not carry origin metadata" rather than "this KB has
> not looked".*

## Verdict: **DISCHARGED — 🟢 TWO regions booked, and the falsifier's restatement is ALSO true, of a different layer**

| subject | evidence | kind | occurrences | region |
|---|---|---|---|---|
| 🟢 `eth-moodle-mcp` 1.3.3 | 🆕 `moodle-app2.let.ethz.ch` | `HOST_IN_CODE` | **4** | 🟢 **EMEA** — ETH Zürich |
| 🟢 `eth-moodle-mcp` 1.3.3 | 🆕 `safari.ethz.ch` | `HOST_IN_CODE` | 1 | 🟢 **EMEA** — ETH Zürich SAFARI |
| 🟢 `mcp-canvas-lms` 1.0.5 | 🆕 `canvas.ust.hk` | `HOST_IN_CODE` | **2** | 🟢 **APAC** — HKUST, Hong Kong |
| 🟡 `@n35da/brightspace-mcp` | `n35da.com` | `HOST_IN_CODE` | 4 | `UNMAPPED` |
| 🟡 `moodle-mcp-server-aql` | `csmediapro.com` | `HOST_IN_CODE` | 2 | `UNMAPPED` |
| 🔴 `@imazhar101/mcp-canvas-server` | — | `NONE` | 0 | — |
| 🔴 `@ink-waffle/moodle-mcp` | — | `NONE` | 0 | — |
| 🔴 `@owen-x-tech/canvas-mcp` | — | `NONE` | 0 | — |
| 🔴 `canvas-mcp-server` | — | `NONE` | 0 | — |

🔵 **Both halves of the falsifier are true, of different layers, and separating them is the
finding:**

- 🔴 **The npm METADATA layer carries essentially no origin signal.** 5 of 8 payloads declare
  no author at all; the two that do give a personal `gmail.com` address and a bare name. So
  "this shelf does not carry origin metadata" is **correct about metadata**.
- 🟢 **The CODE layer carries it plainly.** A hardcoded institutional hostname is a *binding*,
  not a label: an author field can say anything, but the server has to reach the real host to
  function. So "this KB has not looked" is **correct about code**.

🔵 **Nine passes of ownership gap were a failure of looking at the layer where looking works.**
Still: **2 of 8 rows** yield origin evidence and **6 of 8** yield none, so the gap is real —
it is just no longer total.

## `P140-C1` — `mcp-canvas-lms`: it reads `CANVAS_BASE_URL`, then ignores it

The sharper of the two. `dist/common/utils.js:4` does the configurable thing:

```js
const BASE_URL = process.env.CANVAS_BASE_URL;
```

and `dist/operations/canvas.js:58` does not:

```js
return canvasRequest("https://canvas.ust.hk/api/v1/courses", { headers: { Authorization: … } });
```

🔴 **One of this package's three tools is wired to HKUST's Canvas whatever the client
configures**, while its README advertises `CANVAS_BASE_URL` with `https://canvas.ust.hk` as
the worked example. 🔵 **The author's own institution leaked into a shipped code path** — which
is why it is origin evidence, and also a defect a client would want to know about before
connecting it.

🔵 **Same class as `eth-moodle-mcp`, one step worse.** That package at least *describes* its
ten `ddca_*` tools as scraping a course site; this one claims configurability and silently
drops it. 🔴 **Two of eight rows advertise "any instance" and hardcode one institution.**

## 🔴 The first draft booked three false regions, and the fix is structural

An earlier draft used a hand-written list of placeholder hosts, and **booked North America
three times** off `d2l.myschool.edu`, `school.edu` and `moodle.example.edu` — three regional
findings off three worked examples, which is exactly the error class p139's `T24` exists to
prevent. 🔵 **A hand list cannot work: every README invents its own placeholder.** What
distinguishes one is not its spelling but its *shape* — a generic noun standing where an
institution's name belongs. The rule is now structural (`is_placeholder`), and
[`test_origin_evidence.py`](test_origin_evidence.py) pins all eight verbatim placeholders
found in these payloads **and** asserts that the two real hosts survive it.

## 🔴 Host reachability could NOT be verified, and the cause is the environment

All three institutional hosts answer **`403` at `CONNECT`** through this environment's proxy
gateway:

```
> CONNECT canvas.ust.hk:443 HTTP/1.1
< HTTP/1.1 403 Forbidden
```

🔵 **This extends p139's diagnosis.** p139 found government hosts refused and concluded the
policy *"permits package registries and `github.com` and refuses government hosts"*. It
refuses **university hosts too** — the allowlist is registries plus GitHub, not an exclusion of
governments. 🔴 **So the evidence here is the hardcoded host, not the host's liveness**, and
that distinction is deliberate: a compiled-in hostname binds the artefact to an institution
whether or not this sandbox can reach it.

## Region vocabulary

Closed, five values, as `intel/market.md` requires: `North America`, `EMEA`, `APAC`, `LATAM`,
`Global`. 🔴 **A suffix the table does not hold returns `UNMAPPED` rather than a guess** — a
wrong region is worse than a missing one, because the filter it feeds reads as coverage. So
`n35da.com`, `csmediapro.com`, `overhang.io` and `edly.io` are `UNMAPPED`, whatever is known
about those companies from reporting. 🔵 **Secondary facts are not measurements, and this probe
publishes only measurements.** `axim.org` is the one domain mapped from an organisational
fact rather than a suffix, and it carries a note saying so.

## Reproduce

```sh
python3 -I origin_evidence.py payload/*/     # payload/ as built in p140-live-surface-bound
python3 -I test_origin_evidence.py           # 18 tests
```
