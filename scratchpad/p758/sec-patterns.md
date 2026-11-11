## 🆕 `P287`–`P290` — added at p758 (2026-11-11)

🟢 **Four recipes for the lecture-media captioning and accessible-media register, and every component in them was byte-read for its grant this pass** (`T533`–`T546`). Each names its addresses, its licence and its region, and each states the thing it **cannot** do.

🔴 **Four constraints apply to all four.**
1. 🔴 **Do not price any of these against a deadline.** Three of four regional accessibility deadlines moved in `2026` and the obligations did not. In North America the date a client most likely budgeted for — **April 2026** — was extended by DOJ Interim Final Rule on `2026-04-20` to **`2027-04-26`** / **`2028-04-26`** (`T533`). **Sell remediation *capacity*; the backlog is the same size either way.**
2. 🔴 **ASR output is not a conformance deliverable.** WCAG `1.2.2` requires accuracy. Every recipe below therefore ships a **measurement stage**, and the measurement is what is billable (`T536`).
3. 🔴 **No `AGPL-3.0` component appears in any recipe.** `aeneas` and `aTrain` are the convenient tools for two of these jobs and both are excluded by Globant's delivery model in a hosted pipeline; permissive substitutes are named in place (`T546`).
4. ⚠️ **`pyannote`'s pretrained pipelines are gated by model-hub terms that are not its MIT code grant.** Read them per engagement. The MIT cell on the shelf covers the code only.

---

### 🟢 `P287` — Captioning with a conformance number attached (the one that is actually billable)

**The problem.** An institution has thousands of hours of lecture video in Opencast, a Level AA obligation, and a vendor quote per minute. It does not have a way to know whether any given caption file is good enough.

**Wire it.**
1. **Ingest from the system of record** — [`opencast/opencast`](https://github.com/opencast/opencast) (`ECL-2.0`, `511★`, branch `develop`). Build the pipeline as an **Opencast workflow operation**, not a parallel system: the client adopts nothing new.
2. **Recognise** — [`SYSTRAN/faster-whisper`](https://github.com/SYSTRAN/faster-whisper) (`MIT`, `26,658★`) for throughput, or [`ggml-org/whisper.cpp`](https://github.com/ggml-org/whisper.cpp) (`MIT`, `55,080★`) when the audio may not leave the client's perimeter.
3. **Diarize** — [`pyannote/pyannote-audio`](https://github.com/pyannote/pyannote-audio) (`MIT`, `10,778★`, CNRS). Mandatory for seminars, panels and Q&A; skip it and the transcript is unusable regardless of its WER.
4. **Align to word level** — [`m-bain/whisperX`](https://github.com/m-bain/whisperX) (`BSD-2-Clause`, `25,204★`). 🔴 **Do not reach for [`jianfch/stable-ts`](https://github.com/jianfch/stable-ts)** — `MIT` and excellent, but **`ARCHIVED` since `2026-05-30`** (`T544`).
5. 🟢 **Measure — this is the stage that makes it a deliverable.** Human-transcribe a **stratified sample** (by discipline, accent, audio condition, single- vs multi-speaker), then score the machine output against it with [`revdotcom/fstalign`](https://github.com/revdotcom/fstalign) (`Apache-2.0`, branch `develop`) for per-speaker and per-tag breakdowns, and [`jitsi/jiwer`](https://github.com/jitsi/jiwer) (`Apache-2.0`, branch `master`) for the headline WER/MER/WIL in CI.
6. **Route by score** — files above threshold publish; files below enter a human-correction queue in [`SubtitleEdit/subtitleedit`](https://github.com/SubtitleEdit/subtitleedit) (`MIT`, `14,947★`). 🔵 **The threshold, not the model, is the commercial artefact.**
7. **Validate the encoded result** — [`Comcast/caption-inspector`](https://github.com/Comcast/caption-inspector) (`Apache-2.0`, North America per its `NOTICE`) where media is broadcast-derived or vendor-encoded.

**Effort.** `8`–`10` weeks to a measured pipeline over one faculty's estate, including the sampling design and the human reference set. 🔵 **The reference set is an asset the client keeps** and the reason the second faculty costs a third of the first.

🔴 **What it cannot do.** It cannot discharge WCAG `1.2.3`/`1.2.5` — audio description is a different criterion and `P290` is its recipe. It cannot certify conformance; it produces evidence a client's own accessibility office signs.

---

### 🟢 `P288` — The drift-repair sprint: the cheap half of a real backlog

**The problem.** Most institutional estates are not uncaptioned. They are **partly captioned, badly** — publisher files out of sync after a re-encode, captions from an earlier cut, timings off by seconds. Re-transcribing all of it is the expensive way to fix the cheap problem.

**Wire it.**
1. **Inventory first** — enumerate media with an existing caption/subtitle track and classify: *present and synchronised*, *present and drifting*, *absent*. 🔵 **This triage is the single highest-return day of the engagement** and it needs no AI.
2. **Repair the drifting class** — [`smacke/ffsubsync`](https://github.com/smacke/ffsubsync) (`MIT`, `7,941★`) resynchronises an existing subtitle file against its audio. No re-transcription, no new accuracy risk, and the human-reviewed wording is preserved. ⚠️ Its MIT payload has **no title line** (`T541`) — a licence scanner may flag it `UNRECOGNISED`; the grant is MIT, byte-read `1,052 B` / sha256₁₂ `98136a272a45`.
3. 🔴 **Do not use [`readbeyond/aeneas`](https://github.com/readbeyond/aeneas) for the alignment**, convenient though it is: **`AGPL-3.0`** (`T546`). Where a *script or transcript exists but has no timings*, use `whisperX`'s alignment against the known text instead.
4. **Normalise formats and re-verify** — `subtitleedit` (`MIT`) for conversion and timing repair; re-score with `jiwer` to prove the repair did not regress the text.
5. **Send only the *absent* class to `P287`.**

**Effort.** `3`–`4` weeks. 🟢 **Routinely clears `30`–`60%` of a backlog at a fraction of per-minute transcription cost**, which is what buys the credibility for the larger programme.

🔴 **What it cannot do.** It cannot improve a caption file that is accurate-but-badly-timed *and* wrong; drift repair preserves the text, including its errors. Score before and after.

---

### 🟢 `P289` — The national-language pipeline (EMEA, APAC and LATAM, where the whisper family is mediocre)

**The problem.** The register's defaults are strongest in English. A Norwegian, Indic- or Portuguese-medium institution gets materially worse WER from the same pipeline, and the gap lands exactly on the students the obligation exists to protect.

**Wire it — same spine as `P287`, different recogniser, and the choice is regional.**
- 🟢 **EMEA** — [`NbAiLab/nb-whisper`](https://github.com/NbAiLab/nb-whisper) (`Apache-2.0`, `58★`, **National Library of Norway** per its README). 🔵 **The pattern generalises past Norwegian: look for the *national library or public broadcaster* adaptation first** — it is usually permissive, usually domain-matched, and usually invisible to a star-ranked search. ⚠️ Low star counts mean you own the integration.
- 🟢 **APAC** — [`AI4Bharat/vistaar`](https://github.com/AI4Bharat/vistaar) (`MIT`, `95★`, India) for Indic languages; [`wenet-e2e/wenet`](https://github.com/wenet-e2e/wenet) (`Apache-2.0`, `5,255★`) or [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) (`Apache-2.0`, `15,870★`) for a self-hosted, fine-tunable, on-device-capable recogniser. 🔴 The literature name `AI4Bharat/IndicWhisper` is **not an address** (`T543`).
- 🟢 **LATAM** — [`Edresson/Wav2Vec-Wrapper`](https://github.com/Edresson/Wav2Vec-Wrapper) (`Apache-2.0`, `81★`) and [`lucasgris/wav2vec4bp`](https://github.com/lucasgris/wav2vec4bp) (`MIT`, `37★`) for Brazilian Portuguese. ⚠️ Both last pushed in `2022`–`2023`: usable as fine-tuning recipes, not as maintained dependencies. 🔴 **And the obvious training corpus is closed:** [`nilc-nlp/CORAA`](https://github.com/nilc-nlp/CORAA) is **`CC BY-NC-ND 4.0`** — non-commercial *and* no-derivatives, so it cannot be fine-tuned on for a client deliverable, whatever the index's `NOASSERTION` suggests (`T538`). **Budget for licensed or client-owned audio instead; this is a real line item, not a footnote.**
- 🟢 **Multilingual benchmark** — [`OpenMOSS/MOSS-Transcribe-Diarize`](https://github.com/OpenMOSS/MOSS-Transcribe-Diarize) (`Apache-2.0`, `2,270★`) as the challenger to benchmark the composed `whisper` + `pyannote` stack against before an architecture is committed.

**Effort.** `6`–`8` weeks per language, dominated by building the human reference set in that language — **not** by the model work.

🔴 **What it cannot do.** It cannot fix code-switching, which is the actual condition of a great many lectures in India, South Africa and bilingual Canada. Measure code-switched audio as its own stratum or the headline WER will flatter the pipeline.

---

### 🔴 `P290` — Audio description: the greenfield, and the only recipe here that is a *build*

**The problem.** WCAG `1.2.3` (Level A) and `1.2.5` (Level AA) require audio description of visual information. A lecture that shows a board derivation, a diagram or a lab demonstration does not discharge them with a caption track. 🔴 **Published open supply tops out at `4★`** (`T537`).

**Wire it — and accept that the middle of this pipeline does not exist yet.**
1. **Detect the candidate segments.** Scene/slide-change detection over the lecture video plus the caption track from `P287`: segments where the speech stops referring to anything nameable (*"as you can see here"*, *"this term"*) are where description is owed. 🔵 **The caption track is the cheapest detector you have** — deictic language without a referent is the signal.
2. **Draft the description** — multimodal model over the keyframe plus surrounding transcript, constrained to describe *only* what is visually present. 🔴 **This is the component Globant builds**; the two published repositories, [`audioses/omni-describer`](https://github.com/audioses/omni-describer) (`MIT`, `4★`) and [`nfreear/audio-describe`](https://github.com/nfreear/audio-describe) (`MIT`, `1★`), are worth reading for their data shapes and are **not** foundations to build a client deliverable on.
3. **Fit it to the gaps.** Standard (non-extended) description must fit the natural pauses. Use the word-level timings from `whisperX` to find them, and fall back to *extended* description (which pauses playback) only where it will not fit — that fallback is a player capability, which is what `nfreear/audio-describe` demonstrates.
4. **Human review is not optional.** A wrong description is an accessibility *harm*, not a lower score. Route every segment through review in the same queue as `P287`'s sub-threshold captions.
5. **Deliver as a separate track** — `WebVTT` descriptions plus an optional mixed audio render; publish through Opencast alongside the caption track.

**Effort.** `10`–`14` weeks to a reviewed pilot over one high-visual-content course (physics, medicine, engineering drawing, design). 🔵 **Scope it to one course deliberately**: the per-segment review cost is the thing nobody has measured, and the pilot's real output is that number.

🔴 **What it cannot do.** It cannot be sold as automated conformance. The honest offer is *"we reduce the cost per described minute and make the review queue tractable"* — and because the published alternative is `4★`, that offer has almost no competition (`ACTION p758-F`).
