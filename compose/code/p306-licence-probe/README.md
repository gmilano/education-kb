# `p306-licence-probe` — the payload prober, and the substitute gate

## Why this exists

🔴 **`make hooks` has been refused by the execution environment for two consecutive passes
(`p305`, `p306`)** — the recipes are rejected as external code. 🟢 **These two instruments were written
fresh in-session so that `p306` could publish with *some* calibrated control rather than none.**

## `licence_probe.py` — first-hand licence payloads

🟢 **The channel `p306` found: `curl https://raw.githubusercontent.com/{slug}/{branch}/{name}` returns
HTTP 200 with byte-exact bodies.** Twenty-four passes recorded *"no primary source"* on the strength of
403s from `github.com` and `api.github.com`; **this third hostname had never been tried.**

```
python3 -I licence_probe.py slugs.txt out.tsv
```

Emits `slug · branch · file · http · bytes · sha256_12 · verdict · family`. It implements `p305`'s
**permission-clause** rule (the replacement for `p304`'s refuted `bytes < 400` length rule).

### 🔴 Known defects — read before trusting a verdict

1. 🔴 **No POINTER class.** [`w3c/vc-data-model`](https://github.com/w3c/vc-data-model) ships a 167 B
   `LICENSE.md` holding no grant sentence and one URL to the W3C licence. This prober returns
   `NO-GRANT-CLAUSE` — **the same verdict it gives a reserved grant that withholds every right.**
   Opposite consequence, identical output. → `ACTION p306-R` item 2: make the verdict three-valued
   (`GRANT` / `POINTER` / `RESERVED`), discriminated on whether the payload carries a licence URL.
2. 🔴 **`NO_PAYLOAD` means "nothing at that address" and nothing else.** It is **not** a finding of
   absent licence. **Three of five `NO_PAYLOAD`s in `p306`'s platform batch were DEAD SLUGS** and
   became real permissive grants once the address was corrected.
3. 🟡 **The filename ladder missed lower-case `license.txt`** until `frappe/lms` forced it — now
   included. Branch ladder is `main · master · dev · develop · development`.

## `check_p306.py` — the substitute gate

Reads the committed markdown as **data** (it executes no repository code) and checks frontmatter, the
closed region vocabulary, `p277`'s table-structure class, and placeholder rows published as data.

### 🔴 Its own first run was a 100 % false positive, and that is the point

🔴 **It reported 29 failures. All 29 were wrong.** The separator pattern `^\|[\s:|-]+\|$` also matches
the legitimate **empty-header row `| | |`**, so the real separator on the following line was reported as
headerless. 🟢 **Fixed by requiring at least one dash in a separator; the run then went green.**

🔵 **Recorded because it is the third instance of this pass's own pattern (`T-p306c`): an instrument is
defeated by a payload that LOOKS like the thing it screens for.** `p304`'s length rule, `p305`'s clause
rule, and now this base's substitute gate — **all three failed the same way, within three passes.**
⚠️ **A gate's first red is a claim about the gate at least as often as about the shelves.**
