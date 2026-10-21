# L.A.R.A.

**An offline Google Classroom for Philippine public schools (Grades 1 to 12), with paperless self-grading quizzes and a Socratic AI tutor.** It runs entirely on the classroom's own Wi-Fi with no internet. First deployment: the capstone defense plus one pilot class of about 40 learners.

| Program | Folder | Runs on |
| :--- | :--- | :--- |
| **Hub** | [`server/`](./server/) | A dedicated always-on school PC (Linux for the pilot). Database, files, quizzes, AI queue, USB export. |
| **Mobile app** | [`mobile/`](./mobile/) | Android phones (3 to 4 GB RAM budget phones are the target). Learners and teachers. |
| **Desktop app** | [`desktop/`](./desktop/) | Student laptops, lab PCs, teacher PCs. Learners and teachers, the same features as the phone on a large screen. |

What the product is, in full: [`docs/PRD.md`](./docs/PRD.md). The three things it must do well: **a classroom** (stream, handouts, videos, homework photos), **paperless timed quizzes** (auto-graded, gradebook exported to USB), **an AI tutor that never gives the answer**. All of it works with the internet unplugged.

---

## How this project is built

This is AI-native development. **You direct AI agents and your agent writes most of the code.** You are accountable for the result: a small PR that is correct, proven, and easy to try.

The people who review the project check it **as end users**: they run the app like a teacher or a learner, with the Wi-Fi router's internet unplugged. They do not read your diff first. So:

* **If they cannot see it working, it is not done.** Every PR says how to try it, in plain steps.
* **Prove it, do not claim it.** Paste real command output and a screenshot or log. Say plainly what you could not test.
* **Offline is the default.** Every screen needs an offline state, an empty state and a loading state, in English and Filipino.
* **Do not invent behavior.** If a requirement is missing or two documents disagree, ask in the issue. Do not guess.

---

## Start in 10 minutes

1. **Clone and install** what your team needs (below). Everyone needs Git and Python 3.11+ with `pip install pyyaml`.
2. **Run the Hub simulator** so you can build without waiting for anyone:
   ```bash
   python3 scripts/mock_hub.py        # REST :8080, WebSocket :8081, UDP beacon :8888
   ```
   Seed accounts (PIN `1234`): teacher `T-0001` (class code `K7M-4QX`), learner `123456789012` (enrolled), learner `123456789013` (joins with the code), admin `ADMIN-0001` (the Hub admin, not a teacher).
3. **Check your setup is healthy** (these are what CI runs):
   ```bash
   python3 -m unittest discover tests     # contracts, schema, mock hub, guardrails
   python3 scripts/verify_invariants.py   # no cloud dependencies, Filipino strings match English
   ```
4. **Take your team's next issue.** A team works one issue at a time, in step order (`2.1`, then `2.2`), both developers together, with one open PR. Find it on the [sprint board](https://github.com/users/BootlegYouki/projects/2), or filter by team: [mobile](https://github.com/BootlegYouki/L.A.R.A/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22scope%3Amobile%22) · [desktop](https://github.com/BootlegYouki/L.A.R.A/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22scope%3Adesktop%22) · [server](https://github.com/BootlegYouki/L.A.R.A/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22scope%3Aserver%22). Comment that you are taking it. Titles look like `[MOBILE 2.3]` (team, sprint, step).
5. **Give your agent the starter prompt** below, branch from `staging`, and work. Always base your branch and your PR on `staging`, never on `main`: the Lead alone decides what is promoted to `main`.

### Your team's tools

| Team | Install | Run and check (the same commands CI runs) |
| :--- | :--- | :--- |
| **Mobile** | JDK 17, Android Studio with an SDK and an emulator | In `mobile/`: `./gradlew lintDebug testDebugUnitTest`, and `./gradlew installDebug` to run it. An emulator reaches your PC at `10.0.2.2`, so connect to the mock hub by typing `10.0.2.2` port `8080` (the emulator cannot auto-discover the Hub). |
| **Desktop** | Node 20, Rust stable, [Tauri 2 system dependencies](https://v2.tauri.app/start/prerequisites/) | In `desktop/`: `npm ci`, `npm run tauri dev` to run it, `npm run lint`, `npm run build`. |
| **Server** | Rust stable, the Tauri 2 system dependencies for the window | In `server/backend/`: `cargo check --all-targets` and `cargo test`. |

Team guides with the details: [`mobile/README.md`](./mobile/README.md), [`desktop/README.md`](./desktop/README.md), [`server/README.md`](./server/README.md).

### Starter prompt for your agent

Paste this at the start of every session, with your issue name:

```text
You are working on L.A.R.A, an offline LAN classroom app. Task: [TEAM x.y] <title>.
Before writing code, read in this order: AGENTS.md, then <team>/AGENTS.md, the issue text, the
PRD requirement and the contracts it names, the rules/ file for its area, and <team>/docs/TECH_SPEC.md
for file names and patterns. The issue is the whole scope: its sub-tasks, Target Files and acceptance criteria. Then:
- Change only my team's folder. Never edit contracts/, rules/, design-system/, scripts/, tests/ or .github/.
- If the API, an event or a column must change, stop and tell me: that needs its own contract-change PR first.
- No internet at runtime: no Firebase, Google Play Services, CDNs, Google Fonts or analytics. Fonts and icons come from design-system/assets/.
- All user text in English and Filipino. Touch targets at least 52dp on phones (56dp for primary actions), 40px buttons on desktop. Design tokens only.
- Build against scripts/mock_hub.py. Handle the Hub being unreachable without crashing or losing data.
- Never put answer keys, PIN data or other learners' LRNs where a client can see them.
- Make the smallest change that satisfies the issue. If a requirement is missing or two documents
  disagree, ask me instead of guessing.
- If you think the plan is wrong or could be better, do not change it in code: open a Design Proposal issue (type:proposal) with evidence and keep building by the plan until the Lead answers.
- Use the names and patterns already in the code and the Tech Spec. Do not invent a second name for something that exists.
- When done, run the team commands and verify_invariants.py, show the evidence for each acceptance criterion,
  and write the "How to test" steps for a non-programmer.
```

Skills for your stack (Compose, Tauri, Rust, and L.A.R.A rules) are in [`.agents/skills/`](./.agents/skills/README.md); the README there shows how to turn them on.

---

## Rules of the road

| Rule | What it means |
| :--- | :--- |
| **One issue = one team = one PR** | Keep it small. Do not touch another team's folder. |
| **Contract first** | [`contracts/`](./contracts/) is the only thing the three programs share. Never change an endpoint, event or column in code before it exists there, in the mock hub and in the tests. |
| **Branch flow** | Branch from `staging`, open the PR to `staging`. Never base work on `main`: the Lead decides what goes to `main`, and it only receives `staging`. CI flags anything else. |
| **One issue at a time per team** | The three teams work in parallel. Inside a team, both developers work the same issue, in step order, and open one PR. Start the next issue when that PR is merged. |
| **Docs travel with code** | Update your folder's `docs/` (purpose, key files, data flow, gotchas). |
| **Disagree with the plan?** | Say so: open a *Design Proposal* issue (`type:proposal`) with evidence. The Lead decides; the documents change first, then the code. |
| **Children's data** | Never log PINs, tokens or LRNs. Never export learner data off the Hub. |

Full rules: [`CONTRIBUTING.md`](./CONTRIBUTING.md), [`rules/`](./rules/), and for agents [`AGENTS.md`](./AGENTS.md).

## Your PR is done when

- [ ] The build, lint and tests pass, and `verify_invariants.py` passes. Paste the output.
- [ ] It works with the Hub unreachable and with the router's internet unplugged.
- [ ] English and Filipino text, design tokens only, touch targets at least 52dp on phones and 40px buttons on desktop.
- [ ] **"How to test" is filled in**: steps a teacher could follow, with what they should see.
- [ ] A screenshot or log of it running, and an honest "Not verified" list.
- [ ] CI is green. CI is the floor, not the proof: it does not run your app on a phone.

## What the reviewer will do

Read the PR description, run your "How to test" steps like an end user, then try to break the offline cases: airplane mode, Hub stopped, a learner who is not enrolled, a quiz running while the AI is opened. Anything that fails goes back to you with the step number. Make those steps easy.

---

## Where things are

| Path | What |
| :--- | :--- |
| [`contracts/`](./contracts/) | REST (`openapi.yaml`), WebSocket events, SQL schemas, naming rules. The source of truth. |
| [`rules/`](./rules/) | Invariants for networking, sync, quizzes, AI, UI, tooling. |
| [`design-system/`](./design-system/) | Tokens, components and the Google Classroom layout reference. Open `showcase.html` (components) and `prototype.html` (the reference for the desktop Home, Stream and quiz) offline. |
| [`docs/`](./docs/README.md) | PRD, templates, and the documentation map. |
| [`scripts/`](./scripts/) and [`tests/`](./tests/) | The mock hub, the guardrail scanner, and their tests. |
| `server/`, `desktop/`, `mobile/` | One program each, with its own `AGENTS.md` and `docs/`. |

When two documents disagree, the higher one wins: `contracts/`, then `AGENTS.md` and `rules/`, then `design-system/`, then `docs/PRD.md`, then team docs and issues.
