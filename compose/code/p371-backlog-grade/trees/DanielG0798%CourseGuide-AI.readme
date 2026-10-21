# CourseGuide AI

**Team:** instruct.ai  
**Course:** CEN 4930 — AI Agent Studio, Fall 2026  
**Institution:** Florida Gulf Coast University (FGCU)

An instructor-configurable AI learning agent for higher education. CourseGuide AI helps students reason through course-specific assignments according to instructor-defined expectations, without simply producing graded answers.

## Problem (one sentence)

College students in reasoning-intensive courses increasingly have access to immediate general-purpose AI assistance, but that assistance is not automatically aligned with an instructor's course context, permitted help level, or expected reasoning process.

## What this prototype does right now

- Accepts a student question and a course/assignment identifier.
- Loads an instructor-defined policy (allowed help levels, approved sources, style constraints).
- Classifies the type of assistance requested (concept, hint, setup check, next step, analogy).
- Returns a progressively limited, course-aligned response.

## What is intentionally not implemented yet

- Multimodal inspection of student work (diagrams, handwritten equations).
- Persistent student-state memory across sessions.
- Real-time analytics dashboard for instructors.
- Authentication and enrollment integration.

## Setup and run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Copy the example environment file and fill in real keys
cp .env.example .env

# Edit .env with your BYOM or NRP credentials, then run:
python -m src.m2.agent --course physics_101 \
  --question "How do I set up this projectile motion problem?"
```

You can also use the helper script:

```bash
bash scripts/run_m2.sh
```

## Test cases

```bash
pytest tests/m2 -v
```

Or use the helper script:

```bash
bash scripts/run_tests.sh
```

See `tests/m2/test_cases.yaml` for the current inputs and expected outputs.

## Known limitations / bugs

1. The agent does not yet inspect images or handwritten work.
2. Policy matching is exact; partial course names may fall back to a generic policy.
3. Response classification uses a simple keyword tool; nuanced prompts may be mislabeled.
4. The MCP server launches over stdio; if Python is not available on PATH the connection will fail.

## What each folder and file does

Here is a simple guide to the main parts of this repo. You do not need to understand every detail right away.

- **`src/m2/`** — The first working version of the agent (Milestone 2). It takes a student question and returns a guided response based on one course policy.
- **`src/m3/`** — The next version (Milestone 3). It uses two or more agents that hand work off to each other, plus reasoning and memory layers.
- **`src/m4/`** — The final, tested version (Milestone 4). It includes the evaluation harness that scores how well the agent is doing.
- **`src/shared/`** — Code that every milestone uses, such as loading settings, talking to the language model, and reading course policies.
- **`mcp_servers/`** — Small helper programs that expose tools the agent can call. MCP is a standard way for an agent to use outside tools.
- **`config/`** — Files like `physics_101.yaml` that define what an instructor allows the agent to do for a specific course.
- **`data/`** — Sample course documents and any stored knowledge the agent can look up. Large files are ignored by Git.
- **`tests/`** — Automated checks that run the agent against example student questions and make sure the outputs look right.
- **`docs/`** — Milestone reports, interview templates, and notes the team fills in for each assignment.
- **`reports/`** — Generated results, such as evaluation scores and summaries from user testing sessions.
- **`scripts/`** — Short helper scripts for installing, running, and evaluating the project.
- **`requirements.txt`** — A list of Python libraries the project needs. `pip install -r requirements.txt` installs them all.
- **`.gitignore`** — Tells Git which files to ignore, such as secret keys, virtual environments, and large data files.

## CHANGES

- `2026-09-09` — Repository skeleton created; M2 agent scaffold and README added.
