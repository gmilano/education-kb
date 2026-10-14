---
industry: education
region: EMEA
updated: 2026-10-14
---

# `P1058` — affect-inference screening for Article `5(1)(f)`, and the substring that accuses an innocent repository

**Pass 190 · 2026-10-14 · 19/19 tests passing · validated against three live repositories**

## The question that forced it

`ACTION NH`, pre-registered by p189 against `Gap 432`:

> does any proctoring row in this KB **infer emotion**?

It is not an academic question. **Article `5(1)(f)` PROHIBITS** inferring emotions from
biometric data in **education institutions**, it has applied since **`2` February `2025`**,
the Omnibus did **not** delay it *(it deferred Annex III duties to `2027-12-02`)*, and the
ceiling is **EUR `35`M or `7`% of worldwide turnover**. A row this KB recommends into an EU
engagement either is or is not caught, and "probably not" is not an answer.

## Verdict: **`ACTION NH` DISCHARGED, LIMB `1` FIRED — `0` affect-inference paths in `3` repositories**

| row | camera? | what it derives | CLASS A | Art. `5(1)(f)` |
|---|---|---|---|---|
| 🟢 [`VIJAYAPANDIANT/online-examination-system`](https://github.com/VIJAYAPANDIANT/online-examination-system) | 🟢 **no** — no `getUserMedia`, no `mediaDevices`, no `<video>` outside vendored trees | fullscreen + `visibilitychange` + `contextmenu`. A browser lock | `0` | 🟢 **not in scope** — no biometric data at all |
| 🟢 [`singhrajvardhan/SecureExam-Platform`](https://github.com/singhrajvardhan/SecureExam-Platform) | yes | `face_detected` as a **boolean**, `multiple_faces`, tab-switch, copy/paste | `0` | 🟢 clear |
| 🟢 [`shaheeranser/exam-proctor`](https://github.com/shaheeranser/exam-proctor) | yes | head pose *(yaw/pitch)*, iris deviation, **`face-api` identity consistency** | `0` | 🟢 clear — 🔴 **by one default** |

🔴 **The third row is clear because of a flag that is off, not a decision that was made.**
`FaceLandmarker.createFromOptions` sets `outputFacialTransformationMatrixes: true` and never
mentions **`outputFaceBlendshapes`**, which MediaPipe defaults to `false`. Those blendshapes
are the `52` expression coefficients, computed from the graph the repository **already
loads**. 🔵 **One line moves this repository from an Annex III duty that starts in
`2027` into a LIVE prohibition at the Act's maximum penalty.** That belongs in the
engagement, not in a footnote.

## 🔴 The defect this file mostly exists to record

The first draft reported **`16` CLASS A hits** in
`VIJAYAPANDIANT/online-examination-system` — the repository with **no camera**. Two causes,
both live simultaneously, each sufficient on its own to accuse a real project:

| # | cause | the bytes |
|---|---|---|
| `1` | 🔴 a case-insensitive **substring** match for `emotion` fires inside **`deviceMotionEvent`** | `devic`**`eMotionEvent`**`RotationRate` contains `emotioneventrotationrate` |
| `2` | 🔴 **vendored trees** | `node_modules/mime-db/db.json` ships the MIME type `application/emotionml+xml`; `caniuse-lite` ships the DOM event names |

🟢 **Fixed by a leading `\b` and a vendored-path skip. Re-run: `0` CLASS A in all three.**

🔵 **And the class generalises, which is why it is a finding and not a bug report.** p189
found a **substring standing in for a PATH** — `LICENSE` probed where the file was
`LICENSE.TXT`. This is **a substring standing in for a TOKEN**, one segment over in the same
stack. 🔴 **An unanchored token scan over a tree containing `node_modules` will accuse
almost any JavaScript repository of inferring emotion.** Both tests are in the suite so the
anchor cannot be quietly dropped: `test` `2` asserts that the *unanchored* pattern still
fires on the fixture, so a future edit that removes `\b` fails loudly instead of silently
widening.

## The two classes, and why conflating them is the expensive error

| class | what it catches | legal consequence |
|---|---|---|
| **CLASS A** | emotion / affect inference: `emotion*`, `affective`, `mood`, `sentiment`, `valence`, `arousal`, `facial expression`, **`blendshape*`**, `drowsi*`, `engagement_score`, `attention_score` | 🔴 **Art. `5(1)(f)` PROHIBITION.** Live now. EUR `35`M / `7`% |
| **CLASS B** | biometric capture with **no affect claim**: face detect/recognise/track/landmark, `gaze`, `head pose`, `getUserMedia`, `mediapipe`, `face-api` | 🟡 **Annex III point `3`** *(monitoring and detecting prohibited behaviour during tests)* + 🟡 **GDPR Art. `9`** when used to identify. A **duty**, from `2027-12-02` — **not** a prohibition |

🔴 **A CLASS B hit reported as a prohibition blocks a usable row. A CLASS A hit reported as a
duty ships a prohibited system.** The screen returns exactly three verdicts —
`CLASS_A_PRESENT`, `CLASS_B_ONLY`, `NO_BIOMETRIC_SIGNAL` — and never collapses them.

## Interface

```python
is_vendored(path)        -> bool                  # path SEGMENT match, not substring
scan_text(text)          -> {"a": [...], "b": [...]}
scan_file(path, text)    -> {..., "skipped": bool, "path": str}
verdict(file_hits)       -> {"verdict": "CLASS_A_PRESENT" | "CLASS_B_ONLY"
                                        | "NO_BIOMETRIC_SIGNAL",
                             "class_a": [...], "class_b": [...],
                             "vendored_files_skipped": int}
```

No network and no filesystem walk: the caller supplies paths and text *(`gap 139` — this
harness cannot install dependencies)*. That is also what makes every fixture below a
verbatim quotation rather than a re-read.

## Run

```
python3 -I test_affect_scan.py     # PASS 19/19 — P1058
```

## 🔴 What this instrument does NOT establish

- 🔴 **It is a screen, not a clearance.** It reads **tokens**. A model whose affect score
  lands in a neutrally-named variable passes it. Use it to decide **where to read**, then read.
- 🔴 **Nothing was run.** Three repositories were read as source at a pinned `HEAD`
  *(`117112b284c6`, `854a68f9acab`, `6f29a9bb8adc`)*. 🔴 **Both face models in this corpus are
  fetched at runtime from `cdn.jsdelivr.net` and `storage.googleapis.com`** — the model can
  change without the repository changing, and this screen cannot see that.
- 🔴 **Three repositories, and one is not a published row.** `shaheeranser/exam-proctor` is a
  slug from the recency census, read because it is the only one of the three that loads a
  face model at all. [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) is carried
  from an earlier token census and was **not** re-read.
- 🔴 **`0` CLASS A is evidence about `5(1)(f)` only.** All three rows do exam or behaviour
  monitoring, which is Annex III point `3` by name. Clear of the prohibition is not clear of
  the duty, and the duty has a date.
