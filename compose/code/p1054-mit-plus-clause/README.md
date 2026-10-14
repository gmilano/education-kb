# `P1054` — the MIT-body-plus-a-clause trap

**Pass 187, 2026-10-14.** Opened by `ACTION MR`, which surfaced
[`willwearing/graspful`](https://github.com/willwearing/graspful) off
`topics/adaptive-learning?s=updated`.

## The finding

`graspful`'s `LICENSE.md` (`1 439` B) is titled **"O'Saasy License Agreement"**. Its
operative paragraph is MIT's, word for word — *"Permission is hereby granted, free of
charge, … to deal in the Software without restriction"* — and it then appends a second
numbered condition:

> 2. No licensee or downstream recipient may use the Software (including any modified or
> derivative versions) to directly compete with the original Licensor by offering it to
> third parties as a hosted, managed, or Software-as-a-Service (SaaS) product or cloud
> service where the primary value of the service is the functionality of the Software itself.

That is a field-of-use restriction. The file is **not** MIT and **not** open source.

🔴 **Every licence classifier on this shelf that matches the MIT body returns `MIT` for it.**
This is `P971`'s failure shape one step further on: with `P971` (an Apache header NOTICE
standing in for Apache's terms) the title block was right and the terms were absent; here
the body is right and the terms have been *narrowed*. In both cases a confident classifier
is confidently wrong, and the usability verdict inverts.

🔵 For this KB the stakes are specific: `graspful` is an *agent-first course-authoring*
repo — exactly the shape Globant would reach for — and a studio that builds a client's
hosted tutoring service on it would be in breach of clause 2 on delivery.

## The discriminator

Two signals, because either alone is weak:

| signal | what it is | why not alone |
|---|---|---|
| **size** | canonical MIT clusters at **`1 062`–`1 093`** B across the `15` genuine MIT grants verified in p187. `graspful` is `1 439` B — `368` B of added text | a licensor with a long institutional name adds bytes innocently, so size alone over-fires *(there is a test for exactly this)* |
| **restriction vocabulary** | MIT contains no notion of competition, hosting, service provision, a commercial/non-commercial split, or field of use. A hit alongside an MIT body means the grant was narrowed | a bespoke clause may use words this list does not know, so vocabulary alone under-fires |

Vocabulary **decides**; size **catches** what the vocabulary misses, downgrading such a row
to `MIT-BODY-PLUS:unclassified-addition` — flagged for a human, never published as `MIT`.

## Verdicts

- `MIT` — MIT body, in band, no restriction vocabulary. **The only verdict that may be published as `MIT`.**
- `NOT-OPEN-SOURCE:added-restriction` — MIT body plus restriction vocabulary.
- `MIT-BODY-PLUS:unclassified-addition` — MIT body, materially oversized, vocabulary silent. Read it by hand.
- `NOT-MIT-BODY` — not this instrument's business (an Apache notice lands here, by test).

## Use

```python
from mit_plus import classify, is_usable_permissive

v = classify(open("LICENSE.md").read())
# {'verdict': 'NOT-OPEN-SOURCE:added-restriction', 'bytes': 1439,
#  'mit_body': True, 'hits': ['compete', 'hosted, managed', 'saas',
#  'software-as-a-service'], 'excess': 289}

is_usable_permissive(text)   # False for anything but a clean MIT
```

`is_usable_permissive()` is the gate: **a row it returns `False` for must not reach any
page of this KB carrying the label `MIT`.**

## Tests

```sh
cd compose/code/p1054-mit-plus-clause && python3 -m unittest test_mit_plus -v
```

`14` tests, all passing. Stdlib `unittest` only, no network, no dependencies — this harness
cannot install Python packages (`gap 139`, `ACTION LC` limb `2`), so the fixtures are inline
and the instrument takes bytes rather than a URL.

🔴 **Note on `python3 -I`:** isolated mode drops the working directory from `sys.path`, so
`-I -m unittest` cannot import the module under test. Run it as above.

### End-to-end check against live bytes

Run this pass over the real files, not the fixtures:

| slug | bytes | verdict |
|---|---|---|
| [`willwearing/graspful`](https://github.com/willwearing/graspful) | `1 439` | 🔴 `NOT-OPEN-SOURCE:added-restriction`, hits `compete` / `hosted, managed` / `saas` / `software-as-a-service` |
| [`openfun/ralph`](https://github.com/openfun/ralph) | `1 094` | 🟢 `MIT` |
| [`chaz-clark/canvas-toolbox`](https://github.com/chaz-clark/canvas-toolbox) | `1 072` | 🟢 `MIT` |

## The band is an empirical claim

`MIT_CANONICAL_HIGH = 1150` carries headroom over the widest genuine row measured
(`openfun/ralph`, `1 093` B). 🔵 **If a later pass verifies a legitimate MIT grant above
`1 150` B, the band moved and `test_canonical_mit_lands_in_measured_band` is the test that
should fail first.** Widen it against measurement, never against a single inconvenient row.

Evidence: [`evidence/mit-plus-clause.2026-10-14-p187.tsv`](../../../evidence/mit-plus-clause.2026-10-14-p187.tsv).
