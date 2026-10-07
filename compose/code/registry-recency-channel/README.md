---
industry: education
region: Global
updated: 2026-10-07
---

# registry-recency-channel — the instrument of the twenty-fourth pass (2026-10-07)

**Twelfth distinct discovery/metadata channel in this KB.** Previous eleven: topic, star count,
funder, ministry, institution, function, licence scope, platform name, language, MCP registry,
conformance register, named technical standard, transitional article, declared dependency, GitLab
REST API, and `git` itself (pass 23).

## What it measures, and why it is not `git-recency-channel` pointed somewhere new

Pass 23 dated every repository this KB **cites**, using `git fetch --depth 1` to read the head
commit. Pass 23 then pre-registered action **B**: *"run the recency channel over the dependency
closure pass 21 resolved (352 dependencies), not just the top-level repos."*

🔴 **That action cannot be executed as written, and saying so is the first finding.** A dependency
is a **package name**, not a git URL. `git ls-remote` has nothing to resolve. What a build installs
is a **release**, so the honest recency datum for the installed tier is the **upload date of the
latest release** in the registry that serves it:

| Tier | Instrument | Datum | Event it records |
|---|---|---|---|
| citing | `git-recency-channel` | head commit date | *any* commit — including a typo fix in a README |
| installed | **this one** | latest release upload | a **deliberate publication** |

⚠️ **The two numbers are not interchangeable, and no claim may treat them as one series.** A library
can be committed daily and unreleased for two years; a library can be released monthly from a
repository whose default branch has not moved in a year — pass 24 found exactly that case, and it
turned out to be the more important of the two findings. A comparison across the two populations
compares **commit cadence against release cadence**. It is still informative. It is not one metric.

## Endpoints

Both are proven reachable from this environment. `api.github.com`, `api.osv.dev`, `pypistats.org`
and `api.npmjs.org` are 403 at the egress proxy, and no code path depends on them.

```
pypi.org/pypi/<name>/json   -> info.version + urls[].upload_time_iso_8601
registry.npmjs.org/<name>   -> dist-tags.latest + time[<latest>]
```

## The control, which is what makes the negative results publishable

Four package names invented for this pass are swept **blind, alongside the real corpus**, and every
one must fail to resolve:

| Control | Registry | Required | Measured 2026-10-07 |
|---|---|---|---|
| `this-package-does-not-exist-xyz123-globant` | PyPI | non-OK | 🟢 `NOT-IN-REGISTRY` |
| `kolibri-oral-fluency-fake-probe-0000` | PyPI | non-OK | 🟢 `NOT-IN-REGISTRY` |
| `@globant-kb/no-such-package-zzz999` | npm | non-OK | 🟢 `NOT-IN-REGISTRY` |
| `moodle-mcp-nonexistent-control-4242` | npm | non-OK | 🟢 `NOT-IN-REGISTRY` |

**4 of 4 failed while 292 of 293 real names resolved ⇒ 🟢 the probe DISCRIMINATES.** This is the
pass-22 lesson applied: a GitLab control that `302`s on an invented slug proves nothing, so a
channel whose control cannot fail may not publish an absence.

`test_registry_recency.py` enforces the controls as a property of the published TSV, not as a
frozen count: it fails if any control resolves, if fewer than 90% of real names date, if an age does
not recompute from its own date, or if a header/placeholder string reaches a `dep` field.

## 🔴 `NOT-IN-REGISTRY` is not a defect on its own — the one false positive this instrument nearly published

The fifth non-resolving name was real: `@common/global-config`, declared by
[`CAHLR/OATutor`](https://github.com/CAHLR/OATutor)'s `package.json`. Its **spec** is
`file:./common` — a path inside the repository. A registry 404 for it is the registry answering
**correctly**.

⚠️ **Reading that 404 as an absent package would have manufactured a supply-chain defect that does
not exist**, in a flagship row of this KB. `is_local_spec()` exists because of it, the status string
is deliberately neutral, and the rule is:

> **Before reading `NOT-IN-REGISTRY` as "the package is gone", open the manifest and read the
> dependency's *spec*.** `file:`, `link:`, `workspace:`, `portal:`, `git+` and bare paths are never
> served by a registry.

🔵 **It also corrects the pass-21 closure.** `dependency-licence-closure` filed
`@common/global-config` as `UNKNOWN` licence class on an `http-404`. It is not an unknown licence —
it is **not a registry package at all**, and it carries its parent repository's MIT grant. See the
corrected `UNKNOWN` census in `agents/trending.md` (pass 24): **6 → 0**.

## Run

```sh
python3 -I registry_recency.py ../dependency-licence-closure/result.2026-10-06.tsv \
        --ref 2026-10-07 > data/recency-2026-10-07.tsv
python3 -I test_registry_recency.py        # 20 tests, controls enforced
```

`--ref` is mandatory in practice: an age computed against "today" is not reproducible, and every
figure this channel published is stated against **2026-10-07**.

## Data

`data/recency-2026-10-07.tsv` — 297 rows (293 real + 4 controls), columns
`dep, ecosystem, latest_version, release_date, age_days, status`.

## 🔴 What this instrument cannot see

1. **Transitive dependencies.** It dates the same depth-1 set the closure resolved. The closure's
   own README pre-registers depth 2; this inherits that gap.
2. **The version actually installed.** It dates the **latest** release, not the pinned one. A
   manifest pinning `foo==1.0` built in 2019 is *older* than this instrument reports, never newer,
   so every age here is a **lower bound on staleness**.
3. **Whether staleness matters.** `defusedxml` at 2,039 days is a finished security library;
   `webapp2` at 5,122 days is a Google App Engine relic. A date is not a verdict — it is what makes
   a component choice arguable.
