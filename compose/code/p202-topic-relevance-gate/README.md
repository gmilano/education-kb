---
industry: education
region: Global
updated: 2026-10-14
---

# `p202-topic-relevance-gate/` — `ACTION OO`, and the answer is neither limb

`ACTION OO` asked for a relevance gate over ranked discovery and pre-registered two
limbs: **limb 1**, it rejects all `6` known homonyms and keeps all `28` real rows, so it
becomes mandatory before ingest; **limb 2**, it drops a real row, so a topic page cannot
be ingested automatically at all.

🔴 **Both limbs assume the gate is a REJECTER. Measured over `160` rows on `8` topic
pages, it is sound in one direction only, and the directions are not symmetric.**

| | measured |
|---|---|
| rows read	| **160** (`8` vocabularies × the first `20` by stars) |
| real education rows | **137** |
| homonyms | **23** — not the `6` p201 knew |
| homonyms admitted by the gate | 🟢 **0** |
| real rows auto-kept | **117** (`85.4`%) |
| real rows sent to review | 🔴 **20** (`12.5`%) |

🟢 **So the gate may emit `KEEP` or `REVIEW`, and it has no `REJECT` verdict — that is a
contract, asserted in the suite, not a default.** A description that names no education
term is not evidence that the repo is off-topic: an OER repo names its *subject*
("Programming with R", "Image Processing with Python") and never its pedagogy, and an
empty description names nothing at all. Used as an accepter it admits zero noise and
removes `85`% of the review burden. Used as a rejecter it would have silently dropped
`9` Carpentries/lecture repositories.

## 🔴 The counter-intuitive rule this instrument exists to hold

**Bare `learning` is NOISE in an education knowledge base.** It is the most common token
in both education and machine learning, and on `topic:adaptive-learning` the ML sense
outnumbers the education sense `14` to `6`. So `learning` is only ever read inside a
bounded phrase — `e-learning`, `learning record`, `learning analytics`, `adaptive
learning` — and `machine learning`, `active learning`, `online learning` and
`reinforcement learning` are **not education terms**. Without that rule the gate keeps a
screen-brightness daemon (`max-baz/wluma`, `948★`) and a Monte Carlo library
(`cdslaborg/paramonte`, `307★`).

## 🔴 Two defects this suite found in its own gate, both of the same family

1. **`grade` matched inside `Production-grade`** — the one noise row the first version
   admitted (`theunstopabble/InterviewMinds`). A prefix with no left guard against a
   hyphen compound. Fixed with `HYPHEN_COMPOUND_PRONE`.
2. **`exam` matched inside `example`** — and *"usage example"* appears in a large share
   of all repo descriptions, so this one read half of GitHub as education. Fixed with
   `RIGHT_GUARD`.

🔵 Both are the KB's recurring boundary defect (`P248`'s family): **a prefix match is a
claim about a word, and a word has two ends.** Both are committed as regression cases.

## 🟢 The finding that actually decides how to use this: noise and recall are ANTI-correlated

| vocabulary | noise | gate recall | so |
|---|---|---|---|
| `adaptive-learning` | 🔴 **70**% | `83`% | gate MANDATORY, and it works |
| `xapi` | `15`% | `100`% | gate mandatory |
| `lti` | `15`% | `88`% | gate mandatory |
| `scorm` · `proctoring` · `learning-analytics` | `5`% | `74`–`100`% | gate useful |
| `moodle-plugin` | 🟢 **0**% | `90`% | gate optional |
| `open-educational-resources` | 🟢 **0**% | 🔴 **55**% | 🔴 **NO GATE** — it is pure cost here |

🟢 **The rule, and it is the transferable one: a vocabulary whose token is a PRODUCT NAME
(`moodle-plugin`) or a STANDARD (`scorm`) is nearly clean; a vocabulary whose token is a
generic technical phrase (`adaptive-learning`) is majority noise.** Pick the gate by the
vocabulary's class, and for a clean vocabulary the correct gate is no gate.

## Files

| file | what it is |
|---|---|
| `gate.py` | the gate. `matched_terms`, `is_education`, `verdict` → `KEEP`/`REVIEW` |
| `test_gate.py` | **44/44, OFFLINE.** The loaded cases are the `22` measured homonyms plus the two boundary regressions |
| `shelf.tsv` | the `160` rows with hand labels and an `adversarial` column. Star counts are **as the topic page displayed them** — exact below `1 000`, rounded above, because `api.github.com` returns `403` through this proxy |

🔴 **The `adversarial` column is not decoration.** Three rows are topically education and
are *attacks on it*: `Batlez/CloakBox` (`403★`, hides a VM from proctoring software),
`yoannchb-pro/MoodleGPT` (`87★`, hides ChatGPT in a Moodle quiz), and
`Totsukawaii/writeup-on-scorm-cheat` (`24★`). A relevance gate keeps all three correctly.
**Relevance is not suitability, and no gate keyed on topic can tell a studio which of the
two it just measured.**
