# `p445` — publisher-class grant census: answering `Gap 444-A` at corpus scale

## The gap, verbatim

> 🔴 **Does "the institution publishes and does not licence" hold outside Brazil?** Measured
> on IFRN's three official clients (81 ★, zero grants) against two MIT student wrappers.
> 🟢 **Prescription:** probe the *institutional* GitHub orgs behind the paying platforms —
> UANL, U. de Chile, UNAL, the federal-university SIGAA operators — and count grant presence
> by publisher class, not by star count.

## Why this instrument does NOT follow the prescription literally

The prescription says *probe the institutional orgs*. That needs org enumeration, and
`api.github.com` is **403** on this host (measured, and recorded in `lib/probe_payload.sh`'s
own header), as are `github.com/search` and `codeload.github.com`. There is no channel here
that answers "list the repositories owned by `unal`".

🟢 **But the census does not need new network at all.** Every address this base has verified
first-hand over 445 passes is already on disk under `evidence/` — 1 228 TSVs. Classifying
*those* by publisher class answers the gap's QUESTION at a denominator three orders of
magnitude above the five rows the claim was built on, and costs nothing.

## Pipeline

```
evidence/*.tsv  --extract_corpus.py-->  corpus.2026-10-25-p445.tsv     (slug, verdict)
                --publisher_class.py->  classified.2026-10-25-p445.tsv (+ class, tier)
                --handlabel.tsv------>  the 36 institutional rows, hand-labelled
```

`extract_corpus.py` does **not** trust column names — the 61 `verified-repos.*.tsv` alone
carry 20+ header forms. Per row it finds the slug by pattern, decides grant presence from a
word-bounded licence-FAMILY match against this base's own absence verdicts
(`NO-PAYLOAD`, `NO-GRANT-PATH`, `ABSENCE-ENUMERATED`, `DECLARED-NOT-GRANTED`), and
**refuses to guess**: a row with neither signal is excluded and counted as excluded.

Two decisions worth naming:

* **Casefold dedupe.** `p443` measured that **no case oracle exists on this host** — every
  GitHub channel resolves `owner/repo` case-insensitively. So `CAHLR/OATutor` and
  `cahlr/oatutor` are one address, and counting them twice would inflate exactly the class
  under test.
* **Licence ids are not addresses.** The grammar censuses wrote rows like `0/agpl-3.0` into
  slug-shaped cells. Scoring them would count the classifier's own vocabulary as repositories.

## Results

| | n |
|---|---|
| evidence files read | 1 228 |
| rows scored | 18 957 |
| rows excluded as unscoreable | 26 287 |
| **distinct addresses with a first-hand grant verdict** | 🟢 **3 932** |

### By publisher class, as the classifier draws it

| class | n | grant | rate |
|---|---|---|---|
| INSTITUTIONAL | 36 | 26 | 72.2 % |
| NON-INSTITUTIONAL | 3 896 | 2 971 | 76.3 % |

Fisher exact, two-tailed: **p = 0.558**. Institutional 95 % CI **56.0 – 84.2 %**;
non-institutional **74.9 – 77.6 %**. The intervals overlap heavily.

### After hand-labelling all 36 (not a sample — the whole class)

| | n | grant | rate |
|---|---|---|---|
| false positives removed, by ADDRESS | 27 | 18 | 66.7 % |
| same data, by **PUBLISHER** (≥1 granted address) | 15 | 11 | 73.3 % |
| non-institutional, same unit | 2 914 | 2 246 | 77.1 % |

🔴 **Classifier precision on the INSTITUTIONAL class: 27/36 = 75.0 %.** The nine false
positives are in `handlabel.tsv` with a reason each; four are asserted as regression cases in
`test_publisher_class.py` (**21/21 offline**) so a successor who tightens the classifier sees
them flip instead of rediscovering the contamination.

## Verdicts against the pre-registered predictions

`scratchpad/p445/predictions.txt`, written before the census ran.

| | verdict |
|---|---|
| **P3** institutional rate < non-institutional | 🟡 **CONFIRMED in direction, every way it is cut** (72.2 / 66.7 / 73.3 % against 76.3 / 77.1 %) — **but p = 0.558, which is indistinguishable from noise** |
| **P4** p444's rate of ZERO will not reproduce | 🟢 **CONFIRMED.** The institutional rate is 66.7–73.3 %, nowhere near 0 % |
| **P5** the classifier is the binding error term | 🟢 **CONFIRMED.** Precision 75.0 %, and the arithmetic was never the weak part |

## 🔴 What this means for `Gap 444-A`, stated plainly

**"The institution publishes and does not licence" does not generalise. It is IFRN-specific,
not institution-generic.** p444's 0-of-3 was one institution, one platform, one country, and
it does not survive a denominator of 3 932.

🔴 **And the second finding is about this base, not about institutions.** Only **36 of 3 932**
addresses (**0.9 %**) have an institutional publisher at all; nine of those are
misclassifications; the surviving 27 come from **15 publishers**, of which **one — `cahlr`, a
UC Berkeley research lab — supplies 9**. The correct unit of analysis is the publisher, so the
real n is **15**, against p444's 5. 🟡 **So the honest verdict is not "answered yes" or
"answered no" but: the claim is refuted at the magnitude it was stated, and the corpus is too
thin in this class to put a sharp number on the residual.** That thinness is now measured
rather than assumed, which is what `Gap 445-A` hands forward.

🟢 **The one thing that survives:** `ifrn` + `ifrn-oficial` remain the only institutional
publisher in the whole corpus with **multiple addresses and zero grants** (3 addresses, 0
grants). It is a real and sharp fact about **IFRN**, and `Pattern AW` is still the right
response to it. It was never a fact about institutions.

## Reproduce

```sh
python3 extract_corpus.py > corpus.2026-10-25-p445.tsv
python3 publisher_class.py < corpus.2026-10-25-p445.tsv > classified.2026-10-25-p445.tsv
python3 test_publisher_class.py          # 21/21, offline
```

`probe_tranche.sh` is the network half: first-hand verification of this pass's new addresses
in the `p444` schema, sourcing `lib/probe_payload.sh` rather than re-rolling the loop (so
`P171`, `P834` and `P441` are inherited, not re-chosen). Output:
`evidence/verified-repos.2026-10-25-p445.tsv`.
