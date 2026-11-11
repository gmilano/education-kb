## 🆕 2026-11-11 (p758) — 🟢 **THE CAPTIONING SUBSTRATE IS MIT / APACHE-2.0 / BSD-2-CLAUSE ALL THE WAY DOWN, AND `757` PASSES HELD THE RECOGNISER WITHOUT A SINGLE INSTRUMENT TO MEASURE IT. 🔴 THE TWO TOOLS A EUROPEAN CLIENT ALREADY INSTALLED ARE `AGPL-3.0`.**

**`8` foundation rows · `6` platform rows · `25` licence payloads byte-read `2026-11-11` · `1` index value materially corrected (refusing direction) · `11 / 25` on a non-`main` default branch · `3` literature names resolved to non-addresses · `T533`–`T546` declared.**

### 🔴 The register, and the measurement that shows why it was missed

`p749` named this register a candidate in plain words and declined to build it. Nine passes later the mention counts explain exactly how that happens:

| Term | Mentions before `p758` |
|---|---|
| `opencast` | `472` |
| `bigbluebutton` | `233` |
| `transcription` | `98` |
| `captioning` | `51` |
| `diarization` | `20` |
| `pyannote` · `wenet` · `stable-ts` · `aeneas` · `subtitleedit` · `fstalign` · `audio description` | 🔴 **`0` each** |

🔵 **The base held the platforms heavily, the concepts moderately, and the components not at all** — a second confirmation of `748-A` (*a register can be scored and never built*), and an argument for wiring its trigger (`ACTION p758-D`).

### 🟢 Foundations — the deterministic layer a captioning agent would orchestrate

| Repo | Licence (byte-read `2026-11-11`) | ★ | Branch | Note |
|---|---|---|---|---|
| [`openai/whisper`](https://github.com/openai/whisper) | 🟢 `MIT` — `1,062 B`, `dd5444f43eb2` | `112,382` | `main` | 🟢 **Re-measured: the shelf cell was stale at `111,975` since `p661` (`+407`).** `ACTION p757-E` earning its cost. |
| [`SYSTRAN/faster-whisper`](https://github.com/SYSTRAN/faster-whisper) | 🟢 `MIT` — `1,063 B`, `4a4e89b114f4` | `26,658` | `master` | 🟢 The implementation you deploy. Pushed `2026-11-10`. |
| [`ggml-org/whisper.cpp`](https://github.com/ggml-org/whisper.cpp) | 🟢 `MIT` — `1,077 B`, `3468798dd4eb` | `55,080` | `master` | 🟢 The on-premise / air-gapped answer, and therefore the EMEA answer. |
| [`m-bain/whisperX`](https://github.com/m-bain/whisperX) | 🟢 **`BSD-2-Clause`** — `1,296 B`, `359060689ed0` | `25,204` | `main` | 🔵 **Not MIT** — this base's logs have called this family "the MIT whisper family"; this row is BSD-2-Clause. |
| [`pyannote/pyannote-audio`](https://github.com/pyannote/pyannote-audio) | 🟢 `MIT` — `1,060 B`, `055ea897e901` | `10,778` | `main` | 🟢 First appearance on any shelf. Holder *CNRS* → **EMEA**. ⚠️ Pretrained pipelines gated by separate model-hub terms. |
| [`jitsi/jiwer`](https://github.com/jitsi/jiwer) | 🟢 `Apache-2.0` — `11,338 B`, `e7fed65c1700` | `944` | `master` | 🔴 WER / MER / WIL. **The missing conformance instrument.** |
| [`revdotcom/fstalign`](https://github.com/revdotcom/fstalign) | 🟢 `Apache-2.0` — `11,345 B`, `fccc8c717e8f` | `170` | **`develop`** | 🟢 FST alignment, NLP-aware normalisation, per-speaker breakdowns. The sharper instrument. |
| [`SubtitleEdit/subtitleedit`](https://github.com/SubtitleEdit/subtitleedit) | 🟢 `MIT` — `1,070 B`, `ed3918f9b6e1` | `14,947` | `main` | 🟢 The human-review step, permissively licensed. Pushed `2026-11-10`. |

### 🟢 Regional recognisers — and the LATAM corpus that is closed

| Repo | Licence (byte-read) | ★ | Region, and the channel that placed it |
|---|---|---|---|
| [`NbAiLab/nb-whisper`](https://github.com/NbAiLab/nb-whisper) | 🟢 `Apache-2.0` — `11,356 B`, `43070e2d4e53` | `58` | 🟢 **EMEA** — README names the *National Library of Norway* |
| [`wenet-e2e/wenet`](https://github.com/wenet-e2e/wenet) | 🟢 `Apache-2.0` — `11,356 B`, `43070e2d4e53` | `5,255` | 🔵 **Global** — ⚠️ no holder line, `NOTICE` `404`; org name is not evidence |
| [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) | 🟢 `Apache-2.0` — `11,357 B`, `58d1e17ffe51` | `15,870` | 🔵 **Global** — unplaceable; pushed `2026-11-11` |
| [`OpenMOSS/MOSS-Transcribe-Diarize`](https://github.com/OpenMOSS/MOSS-Transcribe-Diarize) | 🟢 `Apache-2.0` — `11,356 B`, `43070e2d4e53` | `2,270` | 🔵 **Global** — unplaceable from its artifacts |
| [`AI4Bharat/vistaar`](https://github.com/AI4Bharat/vistaar) | 🟢 `MIT` — `1,066 B`, `f73b770f26b0` | `95` | 🟢 **APAC** — holder *AI4Bhārat* + README (*India*) |
| [`Edresson/Wav2Vec-Wrapper`](https://github.com/Edresson/Wav2Vec-Wrapper) | 🟢 `Apache-2.0` — `11,346 B`, `1ffce9198d80` | `81` | 🟢 **LATAM** — README (*Brazilian Portuguese*). ⚠️ Last push `2023-05-20` |
| [`lucasgris/wav2vec4bp`](https://github.com/lucasgris/wav2vec4bp) | 🟢 `MIT` — `1,081 B`, `d7aa2e6ecb5e` | `37` | 🟢 **LATAM** — holder *Lucas Rafael Gris* + README. ⚠️ Last push `2022-07-15` |
| 🔴 [`nilc-nlp/CORAA`](https://github.com/nilc-nlp/CORAA) | 🔴 **`CC BY-NC-ND 4.0`** — `19,125 B`, `cb6303892198` · **index says `NOASSERTION`** | `68` | 🔴 **LATAM — and BLOCKED.** Non-commercial *and* no-derivatives: cannot be fine-tuned on, cannot be shipped (`T538`) |

### 🔴 Two `AGPL-3.0` rows filed as warnings, not as starting points

| Repo | Licence (byte-read) | ★ | Why it is a warning |
|---|---|---|---|
| [`readbeyond/aeneas`](https://github.com/readbeyond/aeneas) | 🔴 `AGPL-3.0` — `34,519 B`, `91b65277959e` | `2,876` | The only mature forced aligner in the register. Permissive routes: `whisperX`, `ffsubsync` |
| [`aTrainTranscription/aTrain`](https://github.com/aTrainTranscription/aTrain) | 🔴 `AGPL-3.0` — `34,522 B`, `20b067f86de3` | `1,238` | 🔵 **The thing a European client already installed** (University of Graz per README). Its architecture *is* `faster-whisper` + `pyannote` — i.e. the permissive rebuild is a known quantity. **`develop`** |

### 🟢 Also verified, and placed honestly

[`opencast/opencast`](https://github.com/opencast/opencast) — 🟢 **`ECL-2.0`** (`11,339 B`, `e91f7c95c749`), `511★`, branch **`develop`**, pushed `2026-11-10`. 🔴 **Read the licence name: the Educational Community License is *not* Apache-2.0** — it is Apache-2.0 with a narrowed patent grant, and it is routinely missing from automated allowlists, which is how a legal review stalls on a green dependency.

[`Zackriya-Solutions/meetily`](https://github.com/Zackriya-Solutions/meetily) — 🟢 `MIT` (`LICENSE.md`, `1,074 B`, `4a7c284ffd75`), **`32,609★`**, pushed `2026-11-10`. Local-first meeting transcription; the largest permissive holding found in the register this pass, though its subject is meetings rather than lectures. [`izwi-ai/izwi`](https://github.com/izwi-ai/izwi) — 🟢 `Apache-2.0` (`11,357 B`, `58d1e17ffe51`), `451★`, holder *Izwi AI* per `NOTICE`; local-first voice AI server. ⚠️ Both are general-purpose: cite them as substrate, not as education products.

### 🔴 Three names from the literature that are not addresses

`AI4Bharat/IndicWhisper` → search `ABSENT` + raw `404`; the code is `AI4Bharat/vistaar`. `KBLab/kb-whisper` → `ABSENT` + `404`; **not a GitHub repository at all** — a genuine nil. `pbs/caption-inspector` → `ABSENT` + `404`; canonical is `Comcast/caption-inspector`. 🟢 **The third was this pass's own wrong guess, caught by the probe before it reached a shelf** (`T543`).

### 🔴 The platform-shaped nil, written down

The mandated `open source platform {industry} ERP CRM MIT Apache` leg returned **no education platform under MIT or Apache-2.0**, for the fourth consecutive pass: OpenEduCat `LGPL-3.0`, ERPNext `GPL-3.0`, Apache OFBiz `Apache-2.0` but with no education module, Krayin and iDURAR `MIT` with no education features. 🔵 **A stable property of the market, not a gap in the search: the education administrative *suite* layer is copyleft, and Globant's permissive surface in education is the *component* layer.**
