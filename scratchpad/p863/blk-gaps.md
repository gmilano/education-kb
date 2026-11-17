## 🟢 `2026-11-17` (sixty-eighth pass, `p863`) — **`4` gaps — `862-G2` and `862-G3` both DISCHARGED with their acceptance tests run, and four new limits named, one of which is a defect in this base's own shelf FORMAT**

### 🟢 `862-G2` — DISCHARGED: all nine Hispanic examination terms run, every total published, including six nils

🔴 **The gap said: Mexico, Colombia, Chile and Argentina have their own examination names and none
was queried.** 🟢 **Its acceptance test: run them, report the total for each, and publish a nil as
a measured nil WITH the terms.** 🟢 **Nine terms run on `2026-11-17`, all nine totals published**
([`term-sweep`](../evidence/term-sweep.2026-11-17-p863.tsv)), **plus five further Hispanic
assessment nouns.**

| | Result |
|---|---|
| Addresses returned | `2,142` across nine terms (`2,543` including the five assessment nouns) |
| Above five stars | `11` |
| 🔴 **On topic** | 🔴 **`5` of `11`** |
| 🟢 **Permissively granted** | 🟢 **`2`** |
| Measured nils published | 🟢 **`6`** (`COMIPEMS`, `"Saber 11"`, `PAES`, `reactivos examen`, `"opción múltiple"`, `"planeación didáctica"`, `"guía de estudio"`) |

🔵 **The gap is discharged and its PREMISE is corrected**: the thin yield is not a LATAM property
or a non-English property — the Vietnamese control returned `3` permissive rows from one term
(`T226`).

### 🟢 `862-G3` — DISCHARGED: the APAC leg returned six national positions, and the first attempt still failed

🔴 **The gap said the APAC leg returned `0` national frameworks for China, India, Japan, Korea and
Singapore.** 🟢 **Run twice.**

🔴 **The first run named all five countries inside a query that also named the framing — and
returned none of them**, surfacing Vietnam, India, Italy, Spain and Russia instead. 🟢 **The
second run dropped the region framing and asked the four ministries directly: all four
returned**, with dates, plus Vietnam's numbered instrument and India's Class-`3` mandate.

🔵 **`861-G3`'s remedy — name the jurisdiction, not the region — now holds on its THIRD
independent territory** (Africa, Canada/Mexico, APAC). 🔴 **But `p863` sharpens it: naming the
countries is not sufficient if the query ALSO carries the region token, because the region token
dominates** → `863-G2`.

---

### 🔴 `863-G1` — the `curl -sI` verification step named in this base's instructions is UNAVAILABLE on this channel, and the substitute is undeclared

🔴 **`api.github.com` and `github.com` HTML both return `403` at this session's egress proxy** —
a policy denial, not an outage, and the proxy README is explicit that such denials must be
reported rather than routed around. 🔴 **So the `curl -sI` URL check this base's own run
instructions specify could not be performed for a single address this pass.**

🟢 **Every address was instead proved over the GIT channel** (`git clone --filter=blob:none
--depth 1`), 🔵 **which is strictly stronger — it proves the repository resolves AND reads the
licence bytes in one operation** — **and search counts came from `gh api search/repositories`,
the one channel the environment sanctions.**

🔴 **The gap is that this substitution is not written down anywhere a future pass would find it.**
🟢 **Acceptance test: the next pass states, before its first row, which of the three channels
(`curl`, `gh api`, `git`) answered and which returned `403`** — 🔵 **so that a pass which silently
loses the git channel too is visible as a channel failure and not read as an empty vein.**
🔵 **`T906`'s ten blocked government and multilateral domains are the same defect class at the
policy layer; this is its code-channel twin.**

### 🔴 `863-G2` — a query that names BOTH a region and its countries returns the region

🔴 **Measured this pass, same hour, same engine**: a query naming China, India, Japan, Korea and
Singapore *and* the regional framing returned **`0` of the five**; the same five countries asked
of their ministries directly returned **`4` of `4` plus two more.**

🟢 **Acceptance test for the next pass that runs any regional leg: the query string must contain
`0` region tokens — no `APAC`, no `EMEA`, no `LATAM`, no `North America` — and the pass reports
what each jurisdiction-only query returned.** 🔵 **This is a sharper rule than `861-G3`'s and it
supersedes it: `861-G3` said ALSO name the jurisdiction; `863-G2` says name ONLY the
jurisdiction.**

### 🔴 `863-G3` — the APAC assessment vocabulary is one language deep

🟢 **`"trắc nghiệm"` returned the richest permissive tier in this pass.** 🔴 **It is the ONLY
APAC language whose assessment vocabulary has been queried.** China, Japan, Korea and Singapore
returned POLICY this pass and **`0` repositories**, because no term in their languages was run —
🔴 **and `p862`'s Chinese `作业批改` success shows the supply is there when the term is run.**

🟢 **Acceptance test: one pass that runs the assessment noun in Chinese, Japanese, Korean and
Bahasa Indonesia, reports each total, and publishes any nil WITH its term** — 🔵 **the same shape
`862-G2` used for Spanish, which worked.** 🔴 **Do not run `giáo dục AI`-style POLICY terms: that
term returned `92` addresses and `0` above five stars this pass. The policy noun does not index
code.**

### 🔴 `863-G4` — this base's shelf format has ONE licence column and two row classes need two

🔴 **Two distinct defects, both surfaced this pass, both traceable to the same single-column
format.**

🟢 **(a) Content vs code** (`T229`): [`picuino/test`](https://github.com/picuino/test) ships a
question bank under `CC-BY-SA-4.0` **and** a viewer whose code that licence does not coherently
grant. 🔴 **One column cannot say "items share-alike, code ungranted", so the row currently
overstates what is takeable.**

🟢 **(b) Refusal class** (`T230`): [`measured-unusable`](measured-unusable.md) records `NONE` for
both an uploader's own unlicensed work and a mirror of ministry copyright. 🔴 **They look
identical and need opposite remedies** — a request can fix the first and can never fix the second.
🔴 **The [`licence-requests`](licence-requests/) workflow will generate requests that cannot
succeed until the ledger carries the class.**

🟢 **Acceptance test: the next pass that writes a row with a CONTENT payload records a `code` and
a `content` grant separately, and every new `measured-unusable` entry carries `class: original`
or `class: redistribution`.** 🔵 **Both are shelf-format changes, so this gap is discharged by an
INSTRUMENT change, not by a search** — the same shape as `852-G2`, which was fixed in
`verify_row.sh` rather than by re-probing.

---

