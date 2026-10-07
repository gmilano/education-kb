---
industry: education
region: Global
updated: 2026-10-07
---

# `p437-pinned-version` — pass 25's action C: the version a build installs, not the one the registry serves

**Executes pass 24's pre-registered action C**, written as:

> Date the **pinned** version of each dependency, not the latest release, by resolving the
> manifest's version specifier.
> **Prediction:** every age published this pass is a **lower bound on staleness**; expect
> OATutor's median to rise above 604 d and no repo's to fall.

## Why the two numbers differ

`registry-recency-channel` dates the **latest** release of a dependency. That is the right
datum for "is this library maintained". It is the wrong datum for "what will `pip install -r`
put on the disk", because a manifest pinning `foo==1.0` installs 1.0 however many releases
have shipped since. This instrument resolves the specifier against the registry's full release
list, takes the highest release that satisfies it — which is what pip and npm do — and dates
that.

The answer depends on the specifier class, and the class distribution is itself the result:

| Class | Example | Can it move the number? |
|---|---|---|
| `EXACT` | `==1.2.3`, `1.2.3` | 🔴 **yes** — the pinned release, at whatever age |
| `CAPPED` | `~=1.2`, `^1.2.3`, `<2` | 🔴 **yes** — the highest release under the cap |
| `FLOOR` | `>=1.2` | 🟢 no — resolves to the latest; the age equals pass 24's |
| `ANY` | `*`, no specifier | 🟢 no — same |
| `NON-REGISTRY` | `file:./common`, `workspace:*` | — not served by a registry at all |

## Measured, 2026-10-07, reference date passed explicitly

**328 `(target, manifest, dependency)` rows over the 19 manifests in
`../dependency-licence-closure/targets.tsv`; 327 resolved; 268 distinct package names.**
The one unresolved row is `CAHLR/OATutor`'s `@common/global-config  file:./common`, classified
`NON-REGISTRY` automatically — pass 24 resolved that row by hand.

| | Latest release (pass 24's basis) | **Pinned release** | Ratio |
|---|---|---|---|
| median age | 57 d | 🔴 **220 d** | **3.9×** |
| mean age | 366 d | 570 d | 1.6× |
| cold > 1 yr | 27.2% | 🔴 **42.5%** | 1.6× |
| cold > 2 yr | 15.0% | 23.2% | 1.5× |
| released in 2026 | 70.3% | 53.2% | 0.76× |

**122 of 327 rows (37.3%) are older at the pin than at the latest release. 204 are identical.
One is newer** — see the exception below.

### By specifier class — the whole effect lives in two of the five

| Class | n | median pinned | median latest | median delta | max delta |
|---|---|---|---|---|---|
| `EXACT` | **159** | 327 d | 54 d | **+83 d** | **+3,419 d** |
| `CAPPED` | 97 | 347 d | 125 d | 0 d | +2,586 d |
| `FLOOR` | 51 | 73 d | 73 d | 0 d | 0 d |
| `ANY` | 19 | 9 d | 9 d | 0 d | 0 d |

🔵 **52% of this corpus is exactly pinned.** That is why the effect is large here and why it
would be near zero in a corpus of `>=` manifests. **Quote the class distribution with the
ratio or the ratio does not transfer.**

### By target repository — the prediction, repo by repo

| Repo | n | median pinned | median latest | × | cold > 1 yr, pinned → latest |
|---|---|---|---|---|---|
| `CAHLR/OATutor` | 35 | 🔴 **1,839 d** | 604 d | **3.0×** | 29 → 21 of 35 |
| `ronantakizawa/a11ymcp` | 5 | 🔴 **686 d** | 14 d | **49×** | 3 → 0 of 5 |
| `peancor/moodle-mcp-server` | 2 | 366 d | 22 d | **16.6×** | 1 → 0 of 2 |
| `oppia/oppia` | 152 | 334 d | 60 d | 5.6× | 74 → 40 of 152 |
| `HKUDS/DeepTutor` | 44 | 120 d | 106 d | 1.1× | 13 → 12 |
| `SirhanMacx/Claw-ED` | 21 | 101 d | 35 d | 2.9× | 8 → 5 |
| `ankimcp/anki-mcp-server` | 24 | 68 d | 20 d | 3.4× | 7 → 7 |
| `huggingface/smolagents` | 6 | 122 d | 122 d | 1.0× | 1 → 1 |
| `vishalsachdev/canvas-mcp` | 7 | 12 d | 12 d | 1.0× | 2 → 2 |
| `towardsai/ai-tutor-app` | 20 | 9 d | 9 d | 1.0× | 0 → 0 |
| `moarshy/mcp-tutor` | 10 | 6 d | 6 d | 1.0× | 1 → 1 |
| `microsoft/agent-framework` | 1 | 5 d | 5 d | 1.0× | 0 → 0 |

🟢 **Prediction confirmed on both clauses. OATutor's median rises from 604 d to 1,839 d — it
triples. No repository's median falls.**

🔴 **And the row the prediction did not anticipate is `ronantakizawa/a11ymcp`.** Pass 24 filed
it as **the cleanest row in the corpus** — *"0 of 5 cold, oldest dependency `@axe-core/puppeteer`
at 57 d"*. It pins `puppeteer` and `puppeteer-core` at **`13.5.0`, released 2022-03-05, 1,675
days ago**, against a current `25.12.0` from 14 days ago: **twelve major versions behind**, on
the component that drives a headless browser. The cleanest row in pass 24's table is a
49× understatement.

### The one row where the pin is NEWER than the latest release

`oppia/oppia` pins `webapp2==3.0.0b1` — a **pre-release**, published 2016-09, **3,676 d**.
The registry's latest *stable* `webapp2` is **2.5.2 from 2012-09-28, 5,122 d**. Pass 24
published 5,122 d and called it *"a relic of a dead platform"*. The verdict stands; the figure
does not. 🔵 **So pass 24's "every age is a lower bound" holds in 326 of 327 rows, and the
single exception is a project pinning a pre-release that postdates the last stable.**

## Reservations

- ⚠️ **This resolves the manifest, not the lock file.** Where a `package-lock.json` or
  `poetry.lock` exists it is more authoritative still, and it is not read here.
- ⚠️ **`CAPPED` is resolved against the registry's release list, not against a solver.** A real
  install also has to satisfy every *other* package's constraint on the same name, which can
  only move the chosen version **down**. So the `CAPPED` figures remain lower bounds.
- ⚠️ **Version comparison is PEP 440-lite and semver-lite** (numeric segments, pre-releases
  demoted). Epochs, local versions and npm range syntax beyond `||`, `^`, `~` and the
  comparators are not implemented; no row in this corpus used them.

## The controls (`test_pinned.py`, 47/47, offline)

Every specifier class carries a version that must be **rejected** as well as one that must be
accepted, so an evaluator returning `True` always fails. Four controls exist because the first
build got them wrong:

- **`"pyjwt[crypto]>=2.8,<3"`** — a `.*?\]` scan to the first `]` closes on the **extra's**
  bracket, and the parser returned an empty list for a five-dependency manifest. Now matched by
  bracket depth.
- **`"faiss-cpu>=1.8.0; python_version < '3.14'"`** — a `["\']([^"\']+)["\']` pattern splits at
  the **inner** quotes of the environment marker and emits `3.14` as a dependency. The first run
  published exactly that for `HKUDS/DeepTutor`.
- **`webencodings==0.5.1 \`** — a hash-pinned `requirements.txt` continues each line with a
  backslash; carrying it into the specifier made `==0.65b0` and `==3.0.0b1` resolve to
  `NO-SATISFYING-RELEASE` for two versions PyPI **does** serve.
- **`vkey("1.10.0") > vkey("1.9.0")`** — numeric, not lexicographic.

## Run

```sh
python3 test_pinned.py                                                  # 47/47, offline
python3 -I pinned.py ../dependency-licence-closure/targets.tsv 2026-10-07 > result.tsv
```

## Files

- `pinned.py` — specifier parsing, resolution and dating
- `test_pinned.py` — 47 controls, no network
- `result.2026-10-07.tsv` — 328 rows (**authoritative**)
