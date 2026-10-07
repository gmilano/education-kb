---
industry: education
region: Global
updated: 2026-10-07
---

# `p439-case-collision-gate` — one repository, two spellings, two entities

GitHub resolves `owner/repo` case-insensitively. `github.com/LearningEquality/kolibri` and
`github.com/learningequality/kolibri` serve the same repository, both links work, and nothing
in a browser ever shows that anything is wrong. **A compiler keying entities on the reference
string emits two** — two licences, two dates, two star counts to keep in sync — and a filter on
either spelling silently misses the rows written under the other.

## Measured, 2026-10-07, before this gate existed

the six non-append-only shelf files carried **503 distinct reference strings naming 494 distinct
repositories**, and **9 of those 494 were written both ways — 18 references for 9
repositories**:

| Repository | Spellings found | Canonical | Decided by |
|---|---|---|---|
| kolibri | `LearningEquality/kolibri` ×6 · `learningequality/kolibri` ×10 | `learningequality/kolibri` | PyPI homepage |
| ricecooker | `LearningEquality/ricecooker` ×4 · lowercase ×1 | `learningequality/ricecooker` | PyPI homepage |
| studio | `LearningEquality/studio` ×2 · lowercase ×3 | `learningequality/studio` | README self-link |
| SunbirdEd mobile app | `Sunbird-Ed/SunbirdEd-mobile-app` ×2 · `sunbird-ed/sunbirded-mobile-app` ×1 | `Sunbird-Ed/SunbirdEd-mobile-app` | README self-link |
| SunbirdEd ngcomponents | same shape, ×2 / ×1 | `Sunbird-Ed/SunbirdEd-consumption-ngcomponents` | README self-link |
| E-EVAL | `AI-EDU-LAB/E-EVAL` ×4 · lowercase ×1 | `AI-EDU-LAB/E-EVAL` | README self-link |
| OpenEMIS core | `OpenEMIS/core` ×1 · `openemis/core` ×1 | `OpenEMIS/core` | README self-link |
| Kuali Rice | `KualiCo/rice` ×2 · `kualico/rice` ×1 | `KualiCo/rice` | ⚠️ **majority, not evidence** |
| tool13demo | `Unicon/tool13demo` ×3 · `unicon/tool13demo` ×1 | `Unicon/tool13demo` | ⚠️ **majority, not evidence** |

**Resolution order, because "pick the prettier one" is how the next collision is introduced:**

1. the **package registry's declared homepage**, for a repository that publishes a package;
2. the repository's **own self-link** in `README.md` or `package.json`;
3. failing both, the KB's **majority spelling** — recorded as a majority decision, not as
   evidence.

⚠️ **`KualiCo/rice`'s README links to `kuali/rice`, which is a THIRD, genuinely different
repository** — different owner, head commit 2017-05-17 against `KualiCo/rice`'s 2020-07-01. Rule
2 does not apply when the self-link points somewhere else, and conflating the two is the error
the second negative control forbids.

## Scope

The **append-only** files (`agents/trending.md`, `repos/trending.md`) are not scanned. History
records the spelling that was published; editing it is the error this KB forbids everywhere else.

## The controls (`test_case_gate.py`, 9/9, offline)

| | Case |
|---|---|
| positive | the real 2026-10-07 kolibri collision, spanning two files |
| positive | the **repo name's** case counts, not only the owner's |
| negative | one spelling repeated three times is not a collision — without this, a gate flagging every repeated reference would also pass the positives |
| negative | `kuali/rice` vs `KualiCo/rice`: two repositories, not one misspelt |
| negative | a spelling surviving only in append-only history is out of scope |
| negative | **a zero denominator is a path fault, not a clean tree.** The first build pointed two directories up instead of three, found nothing and printed *"0 findings"* over the real repository — the failure mode **P355** exists to name. The gate now exits 2 on an empty denominator |
| negative | `github.com/search/repositories` is a **site path**, not a repository, and must not enter the denominator |
| negative | `owner/repo.git` is the **same repository** as `owner/repo` — counting the clone URL separately would report a case collision that does not exist |

## Run

```sh
python3 test_case_gate.py       # 9/9, offline
python3 case_gate.py            # 0 = clean, 1 = findings, 2 = wrong root
```

**Current state: 495 distinct repositories cited, 0 findings.** (495, not 494, because this pass
added `treeverse/dvc` to the text of the rename finding.)
