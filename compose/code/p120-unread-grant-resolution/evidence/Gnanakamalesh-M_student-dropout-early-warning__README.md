# Student Dropout Early-Warning & Intervention System

[![CI](https://github.com/Gnanakamalesh-M/student-dropout-early-warning/actions/workflows/ci.yml/badge.svg)](https://github.com/Gnanakamalesh-M/student-dropout-early-warning/actions/workflows/ci.yml)

Estimates, at six fixed checkpoints through a university course, the probability
that a student withdraws within the next 30 days — with the factors that drove
each estimate and the support actions they suggest.

Built on [OULAD](https://analyse.kmi.open.ac.uk/open_dataset) (Open University
Learning Analytics Dataset): 32,593 students, 10,655,280 clickstream events, seven
modules across four presentations.

**The headline result, stated the way it should be read:** PR-AUC **0.089**
[0.079, 0.099] against a **2.9%** base rate. At a 5%-of-cohort alert budget that
is **26% recall at 12.2% precision** — the model finds about one in four students
who go on to withdraw, and roughly seven in eight students it flags were not
about to. That is a real improvement over the best single heuristic (PR-AUC
0.048) and it is nowhere near good enough to make a decision about a person.

This system is designed to route limited staff attention. It is not designed to
be right about individuals, and nothing in the interface claims it is.

---

## What is actually here

| | |
|---|---|
| Prediction target | P(withdraws within 30 days) as of course-relative day *t* |
| Checkpoints | days 30, 60, 90, 120, 150, 180 — one row per (student, checkpoint) |
| Rows | 150,938 checkpoint rows, 4,559 positive (3.02%) |
| Features | 37, allowlisted in `features.yaml`, no protected attributes |
| Models | logistic regression → random forest → XGBoost (calibrated) |
| Splits | chronological by presentation, grouped by student: 65,443 / 32,076 / 43,407 |
| API | FastAPI, 19 paths / 20 operations, RBAC + audit logging |
| Dashboard | React 18 + TypeScript, 7 pages |
| Tests | 536 total — see [Checks](#checks) for the two selections and their measured numbers |

Documentation is in [`docs/`](docs/README.md) — task spec, data card, EDA
findings, feature dictionary, model card, ethics, fairness audit, monitoring,
deployment, API, database, frontend, and five ADRs.

---

## Why this is not another dropout-prediction notebook

The difference is in what the project refuses to do.

**A leakage guarantee, as a property test.** The core invariant is
`build(full_history, as_of=t) == build(truncated_history, as_of=t)` — exact
equality, checked with Hypothesis plus adversarial fixtures, in its own CI job.
`date_unregistration` is the column the label is computed from; a single test
guards the one function that removes it, because if that regresses every metric
becomes excellent and the failure looks like success.

**Splits that respect both time and students.** Chronological by presentation,
grouped on `id_student`. Building that revealed 7.9% of students appear in more
than one presentation — 664 were in both train and validation. ADR-0003 was
amended rather than the finding buried.

**A capacity-first operating point.** The obvious framing — "pick a threshold for
80% recall" — turns out to flag **47% of the cohort**, which no institution can
staff. So the operating control is an *alert budget*: the share of students staff
can actually contact. The recall-first table is still published, because the
number that killed the idea is worth showing.

**Confidence intervals by cluster bootstrap**, resampling students rather than
rows, because one student contributes six correlated rows. I documented that this
would give "visibly wider" intervals, then measured a design effect of **0.93**,
and corrected the claim.

**Findings that contradicted my own plan, kept.** Trend features — which the plan
called "the part that carries the project" — contribute within fold noise. Tuned
XGBoost does **not** beat untuned random forest on PR-AUC (0.089 vs 0.095); it is
preferred for calibration and SHAP speed, and the model card says so. My
pre-registered PR-AUC prediction of 0.10–0.12 came in at 0.089.

**SMOTE rejected by measurement, not argument.** 22.1% of synthetic rows were
arithmetically impossible — nested windows violated, day caps exceeded, binary
indicators fractional. Class weights won.

**Explanations audited before being shown.** TreeSHAP attribution stability was
measured (0.902 mean top-3 overlap for the high-risk group) *before* SHAP was
wired to any UI. The panel is headed "Factors the model weighted", not "Reasons",
and a test asserts the word "reasons" never heads it.

---

## Results

### Model comparison (test presentation, 43,407 rows)

| Model | PR-AUC | Brier | ROC-AUC |
|---|---:|---:|---:|
| Dummy (base rate) | 0.029 | 0.028 | 0.500 |
| Best single heuristic (inverse `clicks_28d`) | 0.048 | — | — |
| Logistic regression | 0.072 | 0.209 | 0.731 |
| Random forest | **0.095** | 0.063 | 0.742 |
| XGBoost, tuned + isotonic (**shipped**) | 0.089 | **0.027** | 0.747 |

Brier is lower-is-better. Logistic regression's 0.209 is an artefact of
`class_weight="balanced"`, which fits against an effectively 50/50 base rate: its
mean predicted probability is 0.41 against a true 0.029, and dropping the weights
gives Brier 0.028 at the same PR-AUC — the weighting distorts the probabilities,
not the ranking.

The random forest scores higher. XGBoost ships because it calibrates better and
explains faster, and that tradeoff is documented rather than hidden behind a
leaderboard.

### The operating point

At a 5% alert budget: **26% recall, 12.2% precision, 74% of withdrawing students
missed.** A 4.2× lift over the base rate, and still a system that misses three
students in four. Both numbers belong in the same sentence.

### Fairness

No false-negative gap survives a confidence-interval overlap check on any of
gender, age band, deprivation band, disability, or region. **That is an absence of
evidence of disparity, not evidence of fairness** — a 17-point regional gap that
fails the check has not been ruled out, it is unresolvable at this sample size.
The overall miss rate is ~74% in every group.

One directional finding is recorded rather than buried: the model **understates**
risk for students declaring a disability (predicted 3.32% vs observed 4.65%) —
small, not significance-tested, and the only result whose direction would deny
support if it grew. See [`docs/ETHICS.md`](docs/ETHICS.md).

### Drift

Measured on the real train→test cohort pair. All 7 majorly-drifted features are
assessment-derived, and the cause is in the source data: module BBB went from 12
assessments to 6. **Test performance held anyway, and calibration slightly
improved.** That is why `DriftSummary` exposes `requires_review` and deliberately
has no `requires_retraining`.

Measuring this also caught PSI itself: on two samples from the *same*
distribution, median PSI is 0.18 at n=50 and 1.31 at n=25 — noise alone clears
the conventional "major drift" band. Bin count now adapts to sample size. See
[`docs/MONITORING.md`](docs/MONITORING.md).

---

## Quickstart

Python **3.10** is required (ADR-0004: SHAP/XGBoost wheels on 3.13+ are
unreliable).

```bash
git clone https://github.com/Gnanakamalesh-M/student-dropout-early-warning.git
cd student-dropout-early-warning
py -3.10 -m venv .venv && .venv/Scripts/activate    # Windows
# python3.10 -m venv .venv && source .venv/bin/activate   # macOS/Linux
pip install -e ".[dev,viz,api]"
cp .env.example .env
```

Then, in order:

```bash
python scripts/download_data.py          # OULAD (UCI mirror; canonical URL 404s)
python scripts/build_dataset.py          # checkpoint rows + population report
python scripts/run_eda.py                # every table and figure in reports/
python scripts/build_features.py         # 37-feature matrix + splits
python scripts/train_baselines.py        # LR, RF, dummy, trivial rules
python scripts/train_model.py            # tune, calibrate, register XGBoost
python scripts/run_explainability.py     # SHAP importance + stability
python scripts/run_fairness_audit.py     # subgroup error rates
python scripts/run_drift_report.py --pooled
```

Serve it:

```bash
alembic -c backend/alembic.ini upgrade head
python scripts/seed_db.py && python scripts/score_cohort.py
uvicorn backend.app.main:app --reload --port 8000
cd frontend && npm ci && npm run dev     # :5173
```

Or with containers. Built and run locally (Docker 29.8.2, Compose v5.5.1) with
all three services healthy and real scoring requests served from the container;
`models/` and `data/` are mounted read-only, so build them first:

```bash
docker compose up --build
```

### Checks

```bash
ruff check . && ruff format --check . && mypy        # all clean
pytest --cov                                          # 535 passed, 1 skipped, 91%
pytest -m "not integration" --cov                     # 471 passed, 65 deselected, 87%
pytest tests/ml -m ml                                 # 85 — the leakage guarantees alone
cd frontend && npm run lint && npm run typecheck && npm test && npm run build   # 37 tests
```

Both pytest numbers above were measured on this machine and both are correct —
they select different sets, so **quote the command with the number**. 536 tests
are collected in total:

| Selection | Result | Coverage |
|---|---|---:|
| `pytest --cov` | 535 passed, 1 skipped | 91% |
| `pytest -m "not integration" --cov` (what CI runs) | 471 passed, 65 deselected | 87% |

`tests/unit` 294 · `tests/ml` 85 · `tests/api` 92 · `tests/integration` 65.

### The integration tests, and the one skip

The 65 `integration`-marked tests are in `tests/integration/`:
`test_database.py` (41), `test_api_over_database.py` (12),
`test_oulad_real_data.py` (12). They cover the SQLAlchemy schema, cascades and
constraints; the API driven over the database backend rather than Parquet; and
assertions against the real OULAD extract.

**64 of the 65 run with no database server** — they use SQLite, so plain `pytest`
runs them and they are included in the 535. Only **one** genuinely needs
PostgreSQL, and it reports itself rather than passing quietly:

```
SKIPPED tests/integration/test_database.py:681: running against SQLite;
set TEST_DATABASE_URL to a PostgreSQL DSN to verify JSONB, partial indexes
and server-side defaults
```

To run that one, point at a real PostgreSQL:

```bash
docker run -d --name ews-pg -e POSTGRES_USER=ews -e POSTGRES_PASSWORD=ews   -e POSTGRES_DB=ews_test -p 5432:5432 postgres:16
TEST_DATABASE_URL=postgresql+psycopg://ews:ews@localhost:5432/ews_test   pytest tests/integration -m integration
```

Measured locally against `postgres:16-alpine` on port 55432: **65 passed, 0
skipped**, and the migration round trip (`upgrade → downgrade → upgrade`) applies
cleanly — PostgreSQL reports transactional DDL where SQLite reports
non-transactional, so the rollback path is genuinely exercised. CI's `database`
job runs the same thing.

---

## Layout

```
src/dropout_ews/      data loading, features, models, evaluation,
                      explainability, interventions, monitoring
backend/app/          FastAPI app, SQLAlchemy models, repositories, migrations
frontend/src/         React dashboard
scripts/              one entry point per pipeline stage
tests/                unit / ml (leakage) / api / integration
docs/                 specs, cards, findings, ADRs
reports/              generated — every number in the docs traces to a file here
```

---

## Honest limitations

These are the ones that would change how you read the results, not a
disclaimer list.

1. **One institution, one dataset, 2013–2014 distance learning.** Nothing here
   transfers without re-validation.
2. **The label is formal de-registration**, so a student who stops engaging but
   never withdraws is labelled negative. The target under-counts disengagement,
   and probably not uniformly across groups — which biases every subgroup rate in
   a direction the fairness audit cannot measure.
3. **Most withdrawing students are missed.** 74% at the shipped operating point.
4. **Explanations are attributions, not causes.** SHAP reports what the model
   weighted. The UI says "contributed to this prediction", never "caused".
5. **Risk-band thresholds are policy, not science.** They come from an alert
   budget. Nothing validates that "High" means the same thing across institutions.
6. **Synthetic data is labelled as such, everywhere.** A synthetic cohort exists
   for demo purposes; `docs/DATA_CARD.md` states its generating DAG and the
   circularity that makes performance on it meaningless.
7. **The container stack is verified locally and in CI**, including a real
   SHAP-explained scoring request inside the container. Building it for the first
   time found four bugs that all produced a *healthy-looking* failure — see
   `docs/DEPLOYMENT.md`. CI still runs without a trained model, so its green
   badge proves wiring, not scoring.
8. **No Kubernetes manifests, TLS termination, rate limits, or retention
   policy.** Each would be guesswork here, and guesswork presented as deployment
   config is worse than its absence.

---

## Ethics

The model is an early-warning **support** tool. It must never be presented as
determining a student's future.

- Protected attributes are **not features**. `evaluation/fairness.py` is their
  only consumer, and a test asserts none reaches the allowlist. This does not make
  the model fair — proxies exist — which is why error rates are measured.
- **Human review before any intervention**, enforced in config: settings
  validators make `require_human_review_before_intervention=False` and
  `auto_punitive_actions_permitted=True` unrepresentable.
- **Support, not punishment.** A keyword guard blocks punitive language in
  recommendations. Both the punitive denylist and the causal-language lint had
  false positives when first written, and each now has a guard-the-guard test.
- **Every risk figure carries its model version, calibration status, and a
  disclaimer.** The API schema requires all three, and the frontend types make
  them non-optional so a generator cannot quietly relax it.
- RBAC, audit logging of individual-record reads, and data minimisation.

Full detail: [`docs/ETHICS.md`](docs/ETHICS.md).

---

## License

Code: MIT. OULAD is CC BY 4.0 and is **not** redistributed here —
`scripts/download_data.py` fetches it, and `.dockerignore` keeps it out of any
image.
