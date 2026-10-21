# Harrington

**A family learning platform built around interests, projects, and clear paths
to mastery.**

Harrington is a family-specific fork of
[Homestead](https://github.com/tbh-23/Homestead). It keeps the useful learning
mechanics while we test a much smaller proof of concept: can Marble's connected
curriculum help parents see progress and possible paths to mastery without making
the child's day feel school-like, score-led, or predetermined?

Start with the [Harrington proof-of-concept brief](docs/POC.md) and its
[small learning spine](docs/POC-SPINE.md). Work is tracked in Linear on the
[Harrington](https://linear.app/karatgurk/team/HAR/overview) team; see
[docs/LINEAR.md](docs/LINEAR.md). Homestead remains an upstream code reference,
not a Harrington deployment or service dependency.

## Current self-hosted preview

Harrington no longer requires an external account. Its own Node server stores
family state, lesson caches, and recordings in a family-controlled data
directory. Lesson generation is optional: it stays fail-closed until you point
Harrington at a local OpenAI-compatible endpoint (Ollama is the documented
example).

This preview binds to the local computer only by default. To use it from the
family's other devices, follow [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md): one
host runs the server, every other device is a browser. Use synthetic learner
names until encrypted backups are implemented.
Never send a real child's name into a model prompt. Generators say “your child”,
and names of learners in this app are replaced with “the child” in the browser
before a request is built (accents, hyphens and apostrophe variants included).
When an AI provider is configured, this is what still leaves the machine:

- topic names, descriptions and statuses, and mastery percentages;
- the topic's age from the curriculum (lessons, explanations, quizzes,
  printables, activities, recall cards, topic and section tests, challenges);
- the learner's exact age (or “age unknown”) for whole-subject tests,
  discussion analyses and progress reviews;
- record counts by type, the topics they link to and the average confidence rating;
- a discussion transcript, when the parent asks for an analysis;
- the parent's notes, only when they tick “Include my notes in this request”
  for that one request (record titles are never sent).

Nicknames, and other people's names in a transcript, are sent as spoken.

## What works without an AI provider

Out of the box, with no AI provider configured, Harrington runs on this
computer only and these work:

- **Learners** — add, edit and switch learners (name, birth month and year,
  color).
- **Dashboard** — Today's path with the daily literacy and numeracy choices,
  stepping stones to try next, subject progress, recent growth and evidence.
- **Child view** — the garden, story time and number time picks, and "Tell
  about my day", with no scores.
- **Map** — the world map, per-domain skill trees with the quest log, and the
  list drill-down, showing required and helpful foundations.
- **Growth stages and manual mastery** — Seed, Sprout, Bud and Bloom; you set
  a topic's status from the quest log or the topic page.
- **Calendar** — the day-by-day plan on your chosen home days, with breaks:
  move topics, mark days done, add extras.
- **Records and recordings** — notes, observations and voice recordings saved
  on this computer. The live transcript uses your browser's speech service,
  which may send audio to the browser vendor.
- **Insights** — subject summaries and recommended next topics.

Lessons, print & go sheets, mastery tests, challenges, recall cards, activity
instructions, discussion analysis, progress reviews and adaptive suggestions
need a local AI provider (see [Optional local model](#optional-local-model-ollama)).
Without one, those buttons are replaced by a quiet "Needs a local AI provider"
link (and left out of the child view). The curriculum is downloaded once on
first start and does not update on its own.

## Highlights

- **Mastery ladder** — Topics → Sections → Subjects, each gated at 90%+ so
  learning always builds on solid foundations.
- **Curriculum graph** — parents start at a subject and drill into domains,
  age-banded sections, and topics. Prerequisites and unlocks stay visible;
  mastery stays in the parent view.
- **Ready-to-teach lessons** — **Open full lesson** calls the family-controlled
  `/api/ai` adapter, then caches the result once per topic (`topic:{id}`) on the
  family server. Unconfigured servers keep returning 503. Do not pre-generate the
  whole taxonomy.
- **Verified tests (retained)** — generation and independent re-solving require
  a future AI provider adapter; digital and printable test mechanics remain.
- **Active recall (retained)** — generated memory cards require the same future
  provider adapter; the spaced-review mechanics remain.
- **Spaced practice** — mastery-test questions a child misses are queued and
  resurfaced on an expanding review schedule until they stick, extending spaced
  repetition from facts to problem-solving.
- **Adaptivity** — timed challenges and parent-approved difficulty increases when
  a child excels.
- **Adaptive daily calendar** — a day-by-day plan you can reschedule, mark done,
  and add extra practice to.
- **Records & voice capture** — log observations and store lesson recordings on
  the family server. AI coaching is disabled in this preview.
- **Daily pick-one choices** — Today's path offers a short literacy choice and
  a short numeracy choice, two options each, drawn from the POC focus domains
  (see docs/POC-SPINE.md). In-progress work and domains that have gone quiet
  come first. The child picks one on the dashboard or in the child view, and
  the day's offers and picks are saved with the family's data.
- **Growth stages instead of scores** — progress is shown as a plant: Seed
  (foundations not yet in place), Sprout (ready to start), Bud (being learned)
  and Bloom (mastered). Parents see the stage beside the underlying numbers;
  the child view shows only plants and words.
- **Child view** — opened from the dashboard header, it shows the child's
  garden, big activity buttons and "Tell about my day", with no levels, XP or
  percentages. The inherited XP, levels, badges and celebration effects remain
  in the codebase for evaluation.
- **Insights & notifications**, a **streak tracker**, and a **downloadable guide**.

## Research-Backed Evidence

Harrington is built on learning-science foundations, not ad hoc design choices.
Each one below comes with its main caveat too — the lab effect and the
classroom effect aren't always the same size.

- **Mastery learning** — requiring students to reach a high level of
  proficiency (Harrington uses 90%+) on one unit before advancing to the next
  produces large, consistent achievement gains, especially for struggling
  learners. See Kulik, Kulik & Bangert-Drowns (1990), *Effectiveness of
  Mastery Learning Programs: A Meta-Analysis*, Review of Educational
  Research — [SAGE Journals](https://journals.sagepub.com/doi/10.3102/00346543060002265).
  *Caveat:* the largest effect sizes come mostly from shorter studies using
  experimenter-made tests aligned to the intervention; effects measured with
  independent, standardized tests over full courses tend to be smaller
  (though still positive). Mastery gating also only helps if there's a real
  remediation loop behind it, not just a repeated pass/fail gate.
- **Active recall (retrieval practice)** — testing yourself on material,
  rather than re-reading or re-watching it, produces stronger and more
  durable learning than nearly every other studied technique. See Dunlosky
  et al. (2013), *Improving Students' Learning With Effective Learning
  Techniques*, Psychological Science in the Public Interest —
  [APS summary](https://www.psychologicalscience.org/publications/journals/pspi/learning-techniques.html).
  *Caveat:* the effect is strongest for material tested the same way it was
  practiced (facts, definitions, recall-type questions); it transfers less
  reliably to novel problem-solving or far-transfer tasks, which is part of
  why Harrington also spaces problem-solving retries, not just flashcards.
- **Spaced (distributed) practice** — spreading study of the same material
  over expanding intervals, instead of massing it into one session, is the
  other top-rated technique alongside testing. See Cepeda, Pashler, Vul,
  Wixted & Rohrer (2006), *Distributed Practice in Verbal Recall Tasks: A
  Review and Quantitative Synthesis*, Psychological Bulletin 132(3):
  354–380 — [author's copy](https://www.yorku.ca/ncepeda/publications/CPVWR2006.html)
  — and Hattie & Donoghue (2021), *A Meta-Analysis of Ten Learning
  Techniques*, Frontiers in Education —
  [open access](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2021.581216/full).
  Harrington's memory cards use a Leitner-style expanding schedule, and
  missed mastery-test questions are now queued for spaced retry the same
  way, extending the effect from facts to problem-solving.
  *Caveat:* the effect is less bulletproof in real classrooms than in the
  lab. A 2025 study in real primary-school settings found the retrieval
  (testing) effect held up, but the spacing-interval manipulation itself
  did not reach significance for those students — see [Retrieval practice
  enhances learning in real primary school settings, whether distributed or
  not](https://pmc.ncbi.nlm.nih.gov/articles/PMC12372469/).

## Tech

- Browser app: HTML + CSS + vanilla JavaScript (ES modules), styled with a
  locally built Tailwind stylesheet and vendored Lucide icons.
- Dependency-free Node server for static files, family state, lesson caches, and
  recordings.
- No external account or application bundler. `server.mjs` is the entry point;
  the committed browser assets are regenerated with `npm run build`.
- Marble remains an open runtime curriculum source. AI is optional and
  fail-closed until `HARRINGTON_AI_BASE_URL` and `HARRINGTON_AI_MODEL` are set.

## Running locally

Install and start Harrington:

```bash
npm install
npm start
```

Then open `http://127.0.0.1:4173`. No login is required. Private preview data is
written under `data/private/` and excluded from Git.

### Optional local model (Ollama)

Lesson generation stays off until both of these are set. There is no default
cloud URL or API key.

```bash
# Install Ollama from https://ollama.com, then pull one instruction model:
ollama pull llama3.2

export HARRINGTON_AI_BASE_URL=http://127.0.0.1:11434/v1
export HARRINGTON_AI_MODEL=llama3.2
# Optional. Ollama usually needs none; some reverse proxies want Bearer:
# export HARRINGTON_AI_API_KEY=your-proxy-token

npm start
```

Restart Harrington after changing these variables. `/api/health` reports
`aiConfigured: true` only when both the base URL and model are set. The browser
sends only the messages; every request uses `HARRINGTON_AI_MODEL`.

Local models can take a while to write lesson JSON. The adapter waits up to
three minutes (`HARRINGTON_AI_TIMEOUT_MS` to override) and then fails closed.

Docker on the same machine as Ollama typically needs
`HARRINGTON_AI_BASE_URL=http://host.docker.internal:11434/v1`. Do not publish a
key or a cloud endpoint in `compose.yaml`.

### URL-swap priming (same adapter, no batch job)

The adapter is URL-swappable. Point `HARRINGTON_AI_BASE_URL` at any
OpenAI-compatible `/v1` (Ollama, llama.cpp, vLLM, or a vendor/LiteLLM endpoint
on the family server) without code changes.

Do **not** pre-generate all ~1,590 Marble topics. The lesson cache is
generate-once per topic the family actually opens. If a local model's JSON is
weak, you may temporarily point at a stronger endpoint to fill **only the
topics you open** (or a small focus band later), then switch back to Ollama.
A cloud or vendor endpoint means topic text leaves the house. Never use Puter.
Never put learner names in prompts.

There is no chat. The inherited Harrington Helper and Commune views were never
reachable in Harrington and were removed on 2 October 2026 (HAR-23); a fail-closed
Commune stub remains only so the isolation test can prove nothing calls out.

Docker is also supported:

```bash
docker compose up --build
```

## Backup and restore

Everything the family has created lives in `data/private/` (or
`HARRINGTON_DATA_DIR`): `family-state.json` holds learners, progress, records,
plans and settings; `audio/` holds recordings; `lessons/` and `taxonomy/` are
caches. **That directory is the complete backup set.** Copy it somewhere safe,
or run:

```bash
npm run backup
```

which writes `backups/harrington-<timestamp>.tar.gz` (Git ignores `backups/`).
To restore, stop Harrington, replace `data/private/` with the archive's
contents (`tar -xzf backups/harrington-<timestamp>.tar.gz -C data`), and start
it again. With Docker, back up the `harrington-data` volume instead.
Set `HARRINGTON_BACKUP_DIR` to write somewhere else; the server reads the same
variable, and the notification bell reminds you when the newest archive there
is more than 7 days old. With no archive at all it shows "No backup recorded"
once, with a link to this section; under Docker, where backups are of the
volume, dismiss it and it stays quiet for 30 days.

In the app, **Export** in the sidebar's family box (on a phone, at the bottom
of the learner selector) downloads
`harrington-family-<date>.json`: the full family document plus `exportedAt`
and `taxonomyVersion`. **Import** checks a file, previews its learners and
record counts, and after you confirm replaces the family data on this server.
The JSON file does not contain recordings, so keep a `data/private/` backup too.
The child-view PIN is stored and exported only as a salted SHA-256 hash; a
plain PIN in an older file is hashed when it is loaded or imported.

Saves are versioned: if another tab or device saved first, Harrington reloads
the latest data and says so instead of overwriting it. Changes still pending
when a tab is hidden or closed are sent with `navigator.sendBeacon`; browsers
cap beacons at about 64 KB, so a larger family document falls back to a normal
save, which a closing tab may cut short. `/api/health` reports
`stateVersion` and `stateBytes`; saves are limited to 5 MB and a banner
appears if the family data grows past that. Export then downloads this tab's
copy, marked `unsavedChanges: true`.

## Deployment

**[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)** is the runbook for using
Harrington from tablets, phones and other computers. The short version: one
always-on host runs `node server.mjs` with one data directory; every other
device is a browser; never run two servers against a synced folder.

- `HARRINGTON_HOST` (default `127.0.0.1`) chooses the bind address.
- `HARRINGTON_ACCESS_TOKEN` makes every `/api/*` request except
  `/api/health` need a sign-in cookie; each device signs in once at `/login`.
  Once shared, Harrington answers only to the family's host names and IP
  addresses (`HARRINGTON_ALLOWED_HOSTS` adds names).
- The microphone needs HTTPS on every device other than the host. The
  recommended setup is a WireGuard mesh such as Tailscale with its HTTPS
  certificates; a local reverse proxy with its own certificate authority
  (Caddy `tls internal`) also works. Harrington does not terminate TLS itself.

The included container stores private data in the `harrington-data` volume and
publishes only to `127.0.0.1:4173`. Do not expose Harrington to the public
internet.

## The curriculum data

The curriculum is **not** committed to Git. The local Harrington server fetches
the open-source **Marble Skill Taxonomy** once, caches it under
`data/private/taxonomy/`, and serves it to the browser at `/api/taxonomy/*`:

- https://github.com/withmarbleapp/os-taxonomy

The first launch needs the network for that download. Later launches use the
on-disk cache; it does not update on its own.

## Licensing

Harrington is derived from Homestead under the MIT License. The original
copyright and licence notice are preserved, and Homestead remains configured as
the `upstream` Git remote for future comparison and selective updates.

- **Application code:** MIT — see [`LICENSE`](LICENSE).
- **Curriculum data:** licensed separately by its authors (ODbL 1.0 for the
  database, CC BY-SA 4.0 for the text) and **must be attributed**. See
  [`NOTICE`](NOTICE) and [`DATA-LICENSE.md`](DATA-LICENSE.md) for details and
  obligations.

Using the taxonomy inside this app is a "produced work," so the MIT license on
the code is compatible — you only owe attribution (and share-alike if you ever
redistribute a *modified copy of the dataset itself*).

### Required attribution

> Marble Skill Taxonomy (v1) · © Generative Spark, Inc. (Marble) ·
> https://withmarble.com · licensed under ODbL 1.0 (database) and
> CC BY-SA 4.0 (content).

## Contributing

Work is tracked in Linear, not GitHub Issues. See [`docs/LINEAR.md`](docs/LINEAR.md).
Pull requests are welcome. By contributing, you agree your contributions are
licensed under the MIT License. Please don't commit copies of the taxonomy
dataset into this repository — Harrington caches it locally at runtime.
