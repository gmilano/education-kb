<p align="center">
  <img src="assets/logo/opentutor-hero-512.png" alt="OpenTutor" width="180">
</p>

<h1 align="center">OpenTutor</h1>

<p align="center">
  <strong>Compounding deliberate curiosity.</strong><br>
  A personal tutor for whatever you're curious about: on the web, on Telegram, or inside your AI agent.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/node-%3E%3D22-brightgreen.svg" alt="Node >= 22">
</p>

---

https://github.com/user-attachments/assets/721a646c-04e7-4618-a527-b43dde64d088

<sub>Music: "Equatorial Complex" Kevin MacLeod ([incompetech.com](https://incompetech.com)), licensed under [Creative Commons: By Attribution 4.0](https://creativecommons.org/licenses/by/4.0/). Excerpted, faded and synchronized with this video.</sub>

OpenTutor teaches one short lesson at a time. It asks before it explains, works on
what you keep getting wrong, and brings ideas back days later in a new form.

It ships with 293 courses, from game theory to bread chemistry, and can build a new
one for any topic you name.

## Try it

**[opentutor-gg.vercel.app](https://opentutor-gg.vercel.app)**: browse every
course and answer an example question, no account needed.

Create an account for 3 free lessons. After that, connect your own
[OpenRouter](https://openrouter.ai) account to keep going; you pay OpenRouter
directly for what you use. You can delete your account and data at any time
([privacy](https://opentutor-gg.vercel.app/privacy.html)).

## Run it on your computer

You need Node 22 or later and a model to teach with: an API key for an AI provider,
a local model through Ollama, or Claude Code.

```bash
git clone https://github.com/LEARNableLabs/opentutor
cd opentutor && npm install

export OPENTUTOR_LLM=openrouter OPENROUTER_API_KEY=sk-or-...
npm run web
```

Open http://localhost:3000/learn.html. Your progress is saved on your computer, in
`workspace/`. Lesson text goes to the AI provider you chose.

- **Set the variables in your shell.** `npm run web` does not read `.env`. To use a
  file, run `node --env-file=.env scripts/web/server.js` instead.
- **Other providers:** use `claude-sdk` with `ANTHROPIC_API_KEY`, `openai` with
  `OPENAI_API_KEY`, `ollama` for local models, or `cli` for Claude Code with no key.

**On Telegram:** put `TELEGRAM_BOT_TOKEN` and the same provider settings in `.env`
(the bot reads it), then run `npm run bot`. See
[Telegram on a separate host](docs/deployment.md#telegram-on-a-separate-host).

**In your AI agent:** run `npx skills add LEARNableLabs/opentutor`, then follow the
guide for [Claude Code](claude-code/README.md), [Codex](codex/README.md),
[Claude Web](claude-web/README.md), [Hermes](hermes/README.md),
[OpenClaw](openclaw/README.md), [NemoClaw](nemoclaw/README.md) or
[NanoClaw](nanoclaw/README.md).

## How it teaches

- **It asks before it explains.** A lesson is a short conversation: a question about
  what you already think, a follow-up, then a real situation where you explain why.
- **It comes back to what you missed.** On the website and Telegram, a rules-based
  check (no AI) runs after each lesson and notes the concepts you're still unsure
  of. One that is still shaky three lessons after it was flagged comes back as a retest at the
  start of a lesson; after five, the next lesson is a review of it.
- **On Telegram it adapts further.** The same check also raises or lowers the
  difficulty and changes the kind of question, and each idea gets its own review
  schedule that stretches as you remember it.

Lessons take a few minutes. On Telegram you can say "skip" at any point. In an AI
agent, the agent itself follows the method in the skill's instructions.
[docs/methodology.md](docs/methodology.md) explains the method, the research behind
it, and where it falls short.

## Where the courses come from

The 293 shipped courses live in [`skills/tutor/domains/`](skills/tutor/domains/),
5 to 40 lessons each; the website lists them all. They are AI-generated and have
not all been rebuilt or approved by the current pipeline. Their citations and
resource lists have not been systematically verified and can contain invented
or dead links. A working link alone does not establish that it identifies the
cited work or supports the lesson's claims.

For a new topic, OpenTutor searches public sources (arXiv, Semantic Scholar,
OpenAlex, Wikipedia, course syllabi, YouTube and GitHub), plans a course, and has a
second AI pass review it, with up to three build/review rounds (the initial draft
and at most two revisions). Sources can be
unavailable, and a course can remain unapproved after the third round. On the
website and Telegram, five starter lessons are ready straight away while the
full course is built. On the hosted site, new topics need your own OpenRouter
account.

## Host it for others

- **A website anyone can sign up to** (Vercel and Supabase): follow
  [docs/self-deploy.md](docs/self-deploy.md), and run the four migrations in
  `supabase/migrations/` before deploying. Sign-up opens automatically once Supabase
  is configured. The free trial runs on your key, capped at 300 model calls a day
  (`OPENTUTOR_TRIAL_CALLS_PER_DAY`); see
  [free trial and students' own keys](docs/deployment.md#free-trial-and-students-own-openrouter-keys).
- **A small group on one server:** run `npm run host`. The first run writes a
  learner password and a different admin password to `.env`, readable only by you
  (on Windows, which ignores that, restrict the file yourself), and says where they
  are without printing them; later runs reuse them. The
  learner password opens the shared workspace; the admin one opens `/admin.html`,
  where you add students. Each student gets a one-time access token to enter at
  `/login.html` ("Have an existing access token?"), and their own progress. Signing
  in and every lesson send a password or a token, so serve it over HTTPS: put a web
  server such as Caddy or nginx in front. Without a password, OpenTutor only answers the
  computer it runs on.

## Documentation

| Read this | For |
|---|---|
| [docs/methodology.md](docs/methodology.md) | How it teaches, and the research behind it |
| [docs/architecture.md](docs/architecture.md) | How it works: the agents, the lesson flow, the course files |
| [docs/self-deploy.md](docs/self-deploy.md), [docs/deployment.md](docs/deployment.md) | Hosting on Vercel and Supabase, Telegram, local development |
| [CLAUDE.md](CLAUDE.md), [AGENTS.md](AGENTS.md) | Working on the code: every change gets an issue and a PR, reviewed by CodeRabbit and Codex |

## License

MIT. See [LICENSE](LICENSE).
