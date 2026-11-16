---
industry: education
region: Global
updated: 2026-11-16
---

# `P94` — three-gate candidate intake (`intake-gate.sh`)

Rejects an OSS candidate that cannot be built on, **before** it becomes a KB row or an
architecture decision. Written in pass `p842` (`2026-11-16`) after three live, active,
genuinely-new education repositories each failed for a **different** reason. See `T143`.

## Run

```bash
./intake-gate.sh owner/repo [owner/repo ...]
# exit 0 = all PASS, exit 1 = at least one REJECT  (CI-usable)
```

## The three gates, in order

| Gate | Question | Method | Why it cannot be skipped |
|---|---|---|---|
| **1. liveness** | does it exist, and **what is its real default ref**? | `git ls-remote --symref` | 🔴 **`curl -sI` returns `403` for live repos through this session's proxy** (`T124`), so an HTTP status is not a liveness signal. The symref also yields the **real** branch — see the Kolibri note below. |
| **2. grant** | is there a licence, and what does it actually say? | byte-read `LICENSE`/`LICENSE.md`/`LICENSE.txt`/`COPYING`/`LICENCE` from `raw.githubusercontent.com` **at that ref**; record bytes + `sha256₁₂` | 🔴 Badges, topic tags, aggregator columns and README prose all lie or go stale. **Absence of a licence is all-rights-reserved, not permissive.** |
| **3. substance** | does the grant cover anything **executable**? | `git clone --depth 1` + file-type inventory; reject on `0` source files | 🔴 `T143` mode 3: a **marketing page** published under a real MIT licence passes gates 1 and 2 cleanly. |

## Verified fixture corpus — measured `2026-11-16`

Run it against these five and you should reproduce exactly this. Three failures, **one per
gate-outcome**, which is what proves no gate is redundant.

| Candidate | Result | Detail |
|---|---|---|
| `Ali627miya/gradeguide-ai` | 🔴 `REJECT` `gate2-grant` | `main@f6f9238112cb` — no licence file |
| `timothyheeeee/Autonomous-Grading-Engine` | 🔴 `REJECT` `gate2-grant` | `main@f3518b6c379a` — no licence file |
| `thinkmoon/zhihui-teacher` | 🔴 `REJECT` `gate3-substance` | real `MIT`, `1066B`, `e936c2bc0ff4` — **`0` source files** |
| `vishalsachdev/canvas-mcp` | 🟢 `PASS` | `MIT`, `1071B`, `5385a26e2fac`, `main@d86ff43925d5`, `212` source files |
| `learningequality/kolibri` | 🟢 `PASS` | `MIT`, `1097B`, `3c056b34a476`, **`develop`**`@fe298f54494c`, `3145` source files |

## 🔴 The Kolibri lesson — why gate 1 feeds gate 2

**`learningequality/kolibri`'s default branch is `develop`, not `main`.** A licence probe that
hardcodes `/main/` would have received `404` and rejected **Kolibri — an MIT-licensed, `3,145`-source-file
foundation of this KB — as unlicensed.** Gate 2 must read at the ref gate 1 discovered. This is the
single most likely way to re-introduce wrong licence data into the base.

## Wiring it into an engagement

1. **Intake.** Every candidate from a discovery pass goes through the gate before it is written
   anywhere. `REJECT` rows go to `agents/trending.md` as *flagged and why*, never to `agents/top.md`.
2. **CI.** Pin the corpus of repos an engagement depends on and run the gate on a schedule: a
   dependency that silently relicenses or goes dark fails the build with the gate name attached.
3. **Client deliverable.** The `PASS` line is already an audit record — licence family, byte count,
   content hash, exact ref, source-file count — which is what a procurement or legal reviewer in an
   EU AI Act high-risk context will ask for (`intel/market.md`, EMEA).
