# tero

**your sources, your judgment — the agent proposes, the educator decides**

```
╭─ tero ─────────────────────────────────╮
│ offline · conversación                 │
╰────────────────────────────────────────╯
      ▄▄▄▄▄      ▄▄▄▄▄
    ▄████████  ▀▀▀▀▀▀▀▀▀▀
  ▀▀▀▀███████              tero
       ██████              tus fuentes, tu criterio
       ██████▄
      ██████████▄
╭─ mensaje ──────────────────────────────╮
│ Pregunta, explora o crea…              │
╰────────────────────────────────────────╯
```

A conversational AI teacher agent for Chilean K-12 classrooms. **Strands Agents** +
**Amazon Bedrock** behind an **OpenTUI** shell. The terminal speaks Chilean Spanish
(it is built for those teachers); the repository, docs and this README are English.

**[Live demo](https://marcorojasb.github.io/tero/)** (with embedded HD interactive player: Spanish 2:33, English 2:32; if it 404s on a fresh fork,
enable it once in [Settings → Pages](https://github.com/marcorojasb/tero/settings/pages),
source **GitHub Actions**) · **[Video demo (YouTube)](https://www.youtube.com/watch?v=bNAf-q34lg8)** ·
**[Builder post](https://builder.aws.com/content/3JHLe06HvCuE7EBJm4R59FBHSqA/agents-for-humans-building-tero-with-strands-and-bedrock)** ·
**[Judge quickstart](docs/hackathon/JUDGES-EN.md)** · **[Benchmark paper](docs/EVALUATION-PAPER.md)** · MIT

![tero OpenTUI home](site/assets/tero-og.png)

## What it does

The teacher writes once, in plain Spanish. tero infers the intent:

| Intent | Ask | Result |
| --- | --- | --- |
| **a) Answer** | *"What do I have in my folder?"* | Replies using the folder and the official curriculum bank. Writes nothing. |
| **b) Create** | *"Prepare a 45-minute reading guide"* | Proposes a planificación / guía / evaluación / pauta / actividad **in memory**, with a summary and a full preview. |
| **c) Edit or adapt** | *"Adapt the guide for a student with NEE"* | Proposes a **new version** referencing `origen:`, with Decreto 83 special-education criteria. The original is untouched. |

If something is missing (grade, topic, which file to adapt), tero **asks**.

## The human gate

1. The model has **no write tool**: tools read and propose in memory.
2. Before writing, tero shows **what it will do + the preview**.
3. The teacher approves with `y` or by typing (*"dale"*, *"sí"*), discards with `n`
   (*"no, gracias"*), or asks for a change in the same breath (*"mejor para 2° básico"*).
4. Only the host writes, only into `derivados/`. Editing always creates a new file.
5. Warnings (`thin_evidence`, `unverified_citation`, `paci_no_oficial`) inform. They
   **never block** the decision — there is no magic override, because the decision is
   the teacher's. See [docs/PUERTA-Y-PR8.md](docs/PUERTA-Y-PR8.md).

## Run it

Track A — offline, no keys (~2 min):

```bash
git clone https://github.com/marcorojasb/tero.git && cd tero
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
python -m tero demo --offline --yes
```

Drop `--yes` for the interactive gate. The scripted model is labeled `tero-offline`:
it does not fake Bedrock.

Track B — live Bedrock: `cp .env.example .env`, set `TERO_OFFLINE=0` and your AWS
credentials, then test credentials and models with `python -m tero check-aws --all-models`.
Default model `amazon.nova-lite-v1:0` in `us-east-1` (with automatic fallback to `us.amazon.nova-lite-v1:0`
via `ModelRouter`); no Model access page, serverless models self-enable on first invoke.
Then launch: `python -m tero tui`.

TUI needs [Bun](https://bun.sh): `python -m tero tui --offline`.
Keys: `y` approve · `n` discard · `r` retry · `?` help · `[` `]` evidence ·
`/export md|docx|latex`.

## Multi-Agent Architecture & Bedrock Trio

tero uses **Strands Multi-Agent Graph** (`strands.multiagent.GraphBuilder`) with native
**OpenTelemetry tracing** (`StrandsTelemetry`):

1. **`pedagogical_drafter` node:** reads sources and bank, drafts in-memory artifacts.
2. **`quality_gate_auditor` node:** verifies curriculum coverage and Decreto 83 criteria.
3. **`ModelRouter` + `FallbackStrategy`:** routes inference and handles regional failover.

Benchmarked on Bedrock across four pedagogical journeys
([method and numbers](docs/EVALUATION-PAPER.md)):

| Model | Success | Mean latency | Use |
| --- | :---: | :---: | :--- |
| `amazon.nova-lite-v1:0` | 100% | 10.0 s | Default router: serverless, cheapest, densest official citations |
| `zai.glm-4.7-flash` | 100% | 10.6 s | Fastest tool calling, strictest Decreto 83 NEE schema |
| `minimax.minimax-m2.5` | 100% | 39.5 s | Richest classroom prose, reading passages and rubrics |

Verify live AWS connectivity and the model trio anytime:
```bash
python -m tero check-aws --all-models
```

## Grounding and privacy

- **Official curriculum bank:** a read-only HTTP API (`https://apibegonia.patagua.dev`,
  espejo v0.4) over curated MINEDUC items and teacher guidances. Citations use
  `banco:<id>`; grounded artifacts record `banco_snapshot` for provenance.
  Disabled by default (`TERO_BEGONIA_URL`); tero degrades to the local folder
  and says so.
- **Chile's Ley 21.719:** gradebooks, rosters, attendance and health reports are
  never indexed or sent to the model; files are left untouched, with one
  non-blocking advisory. `TERO_DATOS_SENSIBLES=incluir` opts out.
- **Exports:** markdown / docx / LaTeX filled from JSON schemas. The model never
  emits TeX.

## Verify

```bash
pytest                                        # 390 passed, 1 skipped, 0 xfailed (100% green)
ruff check . && ruff format --check .
cd tui && bun install && bun test src         # 50 passed
```

## Layout

| In scope | Out of scope |
| --- | --- |
| The teacher's folder as system of record | Electron / TipTap / Meridian |
| Conversational intents (answer, create, adapt) | Cloud runtime as the product |
| Decreto 83 NEE accommodations | iPhone companion |
| Evidence panel: local files + official bank | SQLite session DB as product |
| Ley 21.719 student-data guard | Ollama as default |
| LaTeX/PDF via JSON templates | Secrets in git |

Docs index: [docs/README.md](docs/README.md) · Architecture:
[ARCHITECTURE.md](ARCHITECTURE.md) · Protocol:
[docs/CONVERSACIONAL.md](docs/CONVERSACIONAL.md).

## Disclosure

New public MIT project for [Agents for Humans](https://agentsforhumans.devpost.com/)
(track **Professional Agents**). The product thesis (sources as system of record;
agent proposes cited material; teacher approves before anything lands in
`derivados/`) builds on prior private desktop work by the same author; no code was
copied from that predecessor. The offline demo is scripted on purpose so no
recording pretends to be a live Bedrock call. See [docs/NORMAS.md](docs/NORMAS.md).
