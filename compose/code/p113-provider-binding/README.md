---
industry: education
region: Global
updated: 2026-10-10
---

# p113-provider-binding — which model can this be made to talk to

**Pass 113, 2026-10-10.** `test_p113.sh` → **121 passed / 0 failed**, fully offline
(real git repositories committed on disk and served to the real `bind.sh` over
`file://`; no mocks). `bind.sh` read **296 of 296** addresses in **7 m 10 s**, `rc=0` on
every one, **zero unread, zero stray lines, zero capped rows**, alongside a no-body
control run over the same 296 addresses.

## The question, and why a hundred passes of prose forced it

Seven passes have measured this shelf, and every one of them asked about the repository:

| pass | axis | reads | answers | cannot say |
|---|---|---|---|---|
| p107 | tag **count** | history | how much ref traffic | it inverts at the top of the shelf |
| p108 | release **identity** | history | *can I pin it* | whether the pin is from 2019 |
| p109 | commit **recency** | history | *is it alive* | who is keeping it alive |
| p110 | author **concentration** | history | *what if they stop* | whether I can take it over |
| p111 | verification **surface** | tree | *can I tell when I broke it* | whether the check survives GitHub |
| p112 | dependency **closure** | tree | *does it resolve the same twice* | whether the pins are any good |
| **p113** | **provider binding** | tree | ***whose model does it talk to*** | what the running system is configured to do |

None of the seven asks the question a regulated buyer asks first. This KB has been
**answering** it in prose for a hundred passes without once deriving it: the EMEA pages
sell sovereignty, the LATAM pages sell cost, and both rest on the claim that this shelf
can be made to talk to a model the client controls. Before this pass, `OPENAI_API_KEY`
appeared in **zero** markdown files of this KB. The claim had never been read off a tree.

p113 is the third axis read from the TREE and the first about **egress** rather than
about a repository's own hygiene. It is the axis that decides whether p112's `pinned`
means anything in Frankfurt or São Paulo: a perfectly reproducible dependency set that
can reach exactly one hosted endpoint is reproducible and unusable.

## What it emits

Fifteen columns, one row per address:

```
slug  rc  files  stripped  selected  capped  read  anom
      local  broker  override  hosted  prose  selfname  verdict
```

The five family columns are comma-joined lists, not counts, so the TSV is auditable
without re-running it: a reader who distrusts a verdict can see the families that
produced it.

### The verdict ladder

One per row, worst to best, by the strongest form of model control the tree **declares**:

| verdict | meaning | rows | share |
|---|---|---|---|
| `UNREAD` | fetch failed; no claim made (P113-K) | 0 | — |
| `no-model` | nothing in any declaration names a model (P113-J) | **209** | 70.6 % |
| `hosted-only` | one hosted provider, no abstraction, no override — changing the model is a code change | **20** | 6.8 % |
| `override` | a configurable endpoint — can be pointed at a self-hosted OpenAI-compatible gateway | **11** | 3.7 % |
| `broker` | a provider-abstraction layer — substitutable by configuration | **17** | 5.7 % |
| `local` | a local inference runtime is declared — runs with no egress | **39** | 13.2 % |

**87 of 296 rows (29.4 %) bind to a model at all. Of those 87, 67 (77.0 %) can be pointed
at a model the client controls, and 20 (23.0 %) cannot without editing code.**

### The crossing that matters

p112 published a composable set: `pinned` on p112 **and** `checked` on p111 — 63 of 296.
p113 splits those 63 exactly:

| of p112+p111's 63 | rows |
|---|---|
| bind no model at all (specs, platforms, classical ML) | 37 |
| 🟢 **reproducible, tested, and pointable at your own model** | **17** |
| 🔴 **reproducible, tested, and locked to one vendor's endpoint** | **9** |

**17 of 296 (5.7 %)** is the set that survives all three tests.

## Disciplines

`P113-A`–`P113-D` live in `select.awk`, `P113-E`–`P113-H` and `P113-M`, `P113-Q`–`P113-S`
in `tokens.awk`, and `P113-I`–`P113-L`, `P113-N`, `P113-P` beside the driver code they
govern. Each is written where the code is, not here. The four that change how a figure
should be read:

- **`P113-I` the error direction, stated before the figures.** This reads DECLARATIONS,
  not program text. A repository that drives Ollama over plain HTTP and declares nothing
  reads `no-model`. So **`local` and `broker` are lower bounds and `hosted-only` is an
  upper bound** — the opposite direction from p111 and p112, whose textual reads could
  only ever flatter a row. The mitigations are in the instrument rather than in the prose:
  compose files are read, because an `ollama` service is a declaration, and `Modelfile` is
  selected on its NAME.
- **`P113-A` a declaration and a sentence are not the same evidence.** Manifests,
  environment templates, compose files and Modelfiles set verdicts. A README cannot; it
  lands in `prose`. This is p742 and p752 applied to binding instead of to licences.
- **`P113-R` a provider name that is also the repository's own name is flagged, never
  suppressed.** `aiverify-foundation/moonshot` is Singapore's red-teaming toolkit and
  binds to no vendor; `nextcloud/integration_openai` IS the OpenAI integration. No rule
  separates them, so the instrument refuses to try and a human adjudicates on the record.
- **`P113-L` the no-body control is part of the pass.** `P113_NO_BODY=1` runs the same
  tree walk and skips every body read. Measured, not asserted: **86 of 296 rows change
  verdict**, and the control finds `local` on exactly **one** row of the whole shelf
  (`sngdtechnologies/ai-moodle-security`, the only repository here that ships a
  `Modelfile`). Without the body stage this KB would publish 1 local instead of 39 and
  no brokers at all.

## Faults this instrument found in its own code before it found any on the shelf

Six, every one caught against a real payload rather than reasoned about:

1. 🔴 **`FS = "\t"` in `BEGIN`.** The batch header `<sha> blob <size>` is **space**
   separated, so `$3` was empty, every payload size read as 0, and every content line
   landed in `anom`. Caught by a smoke test before the suite existed.
2. 🔴 **The record separator is optional (`P113-M`).** Git writes one newline after each
   payload; when the payload already ends in a newline that is a blank line, and when it
   does not, there is none. Consuming it unconditionally ate the next **header** on every
   file without a trailing newline. `learningequality/kolibri` reported 47 of 59 files
   read and **474** stray lines until this was fixed.
3. 🔴 **Containment, four times over (`P113-Q`).** `"one coherent run"` → `cohere` in
   `apache/ofbiz-framework`; `"autogenerated by uv"` → `autogen` in `ls1intum/Artemis`;
   `"bedrockagentcore"` → `bedrock` in `temporalio/temporal`; and `replicate` is an
   ordinary English verb. **The Artemis one changed a verdict**: a uv lockfile's header
   comment promoted an LMS to `broker`.
4. 🔴 **A generic word used as a token, inside a vendored tree (`P113-S`).** `autogen.js`
   — a test-script name in a committed copy of Chart.js under `lib/` — promoted
   `GibbonEdu/core`, a PHP school platform, to `broker`. Fixed at the root: AutoGen ships
   as `pyautogen`/`autogen-core`/`autogen-agentchat`, so the bare word is gone from the
   table. Chasing the extension would have left the word there for the next filename.
5. 🔴 **A self-name rule that suppressed a real binding (`P113-R`).** The first cut
   `continue`d on a collision, and `nextcloud/integration_openai` lost its only binding
   and dropped to `no-model`. Flag, never suppress.
6. 🔴 **The cap bound on the rows that matter, twice (`P113-D`).** At 60 it clipped nine
   rows — among them `instructure/canvas-lms`, `moodle/moodle`, `sakaiproject/sakai`,
   `kuali/rice` and `leemonade/leemons`, every one reporting `no-model` off a TRUNCATED
   read. At 400, canvas-lms and sakai were still clipped. The selectable set was then
   MEASURED rather than guessed — canvas-lms 551, sakai 498, moodle 64 — and the default
   is 800, with the published run verified at `capped = 0` on all 296 rows.

## Files

| file | what it is |
|---|---|
| `bind.sh` | the driver: fetch, select, read, verdict. Single-threaded and testable |
| `select.awk` | tree → the bounded set of blobs whose bodies decide the row |
| `tokens.awk` | bodies → families, byte-exact stream parse, ordered-removal matching |
| `run.sh` | the census N chunks wide, parallel **by process** (`P113-N`), output byte-identical to a serial run |
| `test_p113.sh` | 121 checks, fully offline, real git repositories over `file://` |
| `addresses.txt` | the 296 shelf addresses, as p112 carried them |
| `orgs.region.tsv` | the committed org → region placement (`P112-L`) |
| `result.2026-10-10.tsv` | the published run |
| `result-nobody.NEGATIVE-CONTROL-2026-10-10.tsv` | the same 296 with the body stage disabled |

## Reproducing

```sh
./test_p113.sh                                     # 121 passed / 0 failed, offline
./run.sh addresses.txt 6                           # the census, ~7 min
P113_NO_BODY=1 ./run.sh addresses.txt 6            # the control
```

`P113_BASE` repoints the fetch (the suite serves `file://`), `P113_CAP` the per-row blob
cap, `P113_WORK` the scratch directory.
