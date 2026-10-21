# SynthEd: From synthetic data to simulated learners

[![GitHub release](https://img.shields.io/github/v/release/theaiagent/SynthEd)](https://github.com/theaiagent/SynthEd/releases/latest)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/theaiagent/SynthEd/actions/workflows/ci.yml/badge.svg)](https://github.com/theaiagent/SynthEd/actions/workflows/ci.yml)
[![pytest](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/theaiagent/cbf1abd6cdc2134e7e26374de286f2c9/raw/synthed-test-badge.json)](#test-suite)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![codecov](https://codecov.io/gh/theaiagent/SynthEd/graph/badge.svg)](https://codecov.io/gh/theaiagent/SynthEd)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19334118.svg)](https://doi.org/10.5281/zenodo.19334118)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Agent-based simulation environment for Open & Distance Learning (ODL) research.** SynthEd generates learning trajectories by combining persona-driven agent modeling with 10 theoretical anchors. Built for researchers in learning analytics, educational data mining, and dropout prediction.

```bash
pip install synthedu
python -c "from synthed.pipeline import SynthEdPipeline; SynthEdPipeline().run(n_students=200)"
```

The repository scripts and development setup are shown in [Quick Start](#quick-start). The `main` branch can contain changes beyond the latest published package; see [Unreleased](CHANGELOG.md#unreleased) before reproducing results across versions.

SynthEd models each student's evolving motivations, decisions, and life context. Calibration fits selected aggregate outcomes; passing validation checks does not establish that every simulated trajectory matches a real learner.

---

## Why SynthEd?

| Research need | SynthEd support |
|---------------|-----------------|
| **Access to learner data** | Generate fictional agents from configurable population distributions |
| **Dropout scenarios** | Adjust model parameters or estimate a base rate from measured targeting curves |
| **Longitudinal data** | Generate weekly interactions from evolving persona, memory and network state |

---

## Key Features

### Simulation Engine
- **10 Theory Modules** -- Tinto, Bean & Metzner, Kember, SDT, Garrison CoI, Moore, Rovai, Baulke, Epstein & Axtell, Gonzalez (+ unavoidable withdrawal mechanism)
- **TheoryModule Protocol** -- 4-phase dispatch (individual, network, post-peer, engagement). Phase-method classes with no-argument constructors are auto-discovered; engagement-only classes require engine instantiation and inclusion in the engagement dispatch list
- **Continuous Persona Spectrum** -- Employment intensity, family responsibility and internet reliability use [0,1] scales. Employment and family responsibility combine zero-valued groups with Beta-distributed positive levels; the model also retains categorical states and decision thresholds
- **Multi-Semester Simulation** -- Carry-over mechanics for engagement, GPA, coping, dropout phases
- **Grade Feedback Loop** -- Raw perceived mastery informs cost-benefit, non-fit perception and competence beliefs; transcript GPA separately applies the configured grade floor

### Calibration & Validation
- **Sobol Sensitivity** -- 68-parameter sensitivity analysis identifying dominant dropout/engagement drivers
- **NSGA-II Calibration** -- Multi-objective optimization with Pareto front, parallel `--workers N` support, adaptive parameter bounds
- **5-Level Validation Suite** -- Checks across distributions, correlations, temporal coherence, synthetic-record uniqueness and backstories. Pipeline validation receives actual outcome labels and persona text; missing evidence is reported as `not_assessed` ([scope](docs/THEORY.md#-validation-suite)). Available data and reference statistics determine assessment coverage; grades summarize assessed check pass rates, not external validity

### Configuration
- **InstitutionalConfig** -- 5 institution-level quality parameters that modulate theory constants. `support_services_quality` scales 13 Baulke dropout phase thresholds
- **GradingConfig** -- Beta/Normal/Uniform grade distributions, dual-hurdle pass requirements, exam-only and continuous assessment modes, relative grading with t-score cohort normalization
- **EngineConfig** -- 70 frozen engine constants with validation, overridable via `dataclasses.replace()`
- **PipelineConfig** -- Frozen dataclass grouping 16 pipeline params; JSON reload automatically restores event-week keys and custom carry-over objects for reproducibility ([example](docs/GUIDE.md#pipelineconfig-recommended))

### Data & Integration
- **OULAD Schema Export** -- 7 CSV tables with OULAD column names and ordering; mapped attributes and heuristic click counts do not establish statistical or semantic equivalence to OULAD
- **Optional LLM Enrichment** -- Persona-grounded narrative backstories via OpenAI, Ollama, or any compatible provider
- **Benchmark Reports** -- Customizable default profile with CLI report generation (`--benchmark`)

---

## Quick Start

```bash
git clone https://github.com/theaiagent/SynthEd.git
cd SynthEd
pip install -e ".[dev]"              # Dev install (no LLM)
pip install -e ".[dev,llm]"          # Dev install with LLM support
python run_pipeline.py              # 200 students, 14 weeks
python run_pipeline.py --n 500      # Custom population
python run_pipeline.py --oulad      # OULAD-compatible export
python run_pipeline.py --benchmark  # Run default benchmark profile
python run_calibration.py --workers 4  # Parallel NSGA-II calibration
```

```python
from synthed.pipeline import SynthEdPipeline
from synthed.pipeline_config import PipelineConfig

config = PipelineConfig(output_dir="./output", seed=42)
pipeline = SynthEdPipeline(config=config)
report = pipeline.run(n_students=300)
print(f"Dropout: {report['simulation_summary']['dropout_rate']:.1%}")
```

---

## Use Cases

1. **Dropout Prediction** -- Generate labeled training data with known ground-truth trajectories
2. **Intervention Simulation** -- Model "what-if" scenarios by adjusting population parameters
3. **Synthetic Benchmarking** -- Share clearly labeled simulated datasets and their configurations for reproducible research

---

## Documentation

| Document | Content |
|----------|---------|
| **[User Guide](docs/GUIDE.md)** | Installation, configuration, calibration pipeline, OULAD export, LLM enrichment, troubleshooting |
| **[Theory & Architecture](docs/THEORY.md)** | 10 theoretical anchors, factor clusters, architecture diagram, project structure, validation suite, test inventory |
| **[Dropout Targeting](docs/DROPOUT_TARGETING.md)** | Horizon-specific curves, measurement provenance, held-out seed checks and targeting limits |
| **[Calibration Methodology](docs/CALIBRATION_METHODOLOGY.md)** | Sobol and NSGA-II settings, sampling uncertainty and identifiability limits |
| **[Long-Horizon Diagnosis](docs/LONG_HORIZON_DIAGNOSIS.md)** | Engagement trajectories, mechanism ablations and the next calibration steps |
| **[Contributing](CONTRIBUTING.md)** | Development checks, theory registration and review requirements |

---

## Roadmap

- [x] Multi-semester simulation with carry-over
- [x] 10 theory modules (Tinto, Bean & Metzner, Kember, SDT, Garrison, Moore, Rovai, Baulke, Epstein & Axtell, Gonzalez)
- [x] Trait-based calibration (Sobol + Optuna + OULAD validation)
- [x] Benchmark reports with CLI (`--benchmark`)
- [x] OULAD-compatible 7-table export
- [x] LLM enrichment with cost control and streaming
- [x] Disability severity (Beta distribution)
- [x] InstitutionalConfig (5 quality parameters modulating theory constants)
- [x] NSGA-II multi-objective calibration with Pareto front
- [x] GradingConfig (configurable grading policy: Beta/Normal/Uniform, dual-hurdle, exam-only)
- [x] EngineConfig (70 frozen engine constants with validation)
- [x] Relative grading (t-score cohort normalization)
- [x] PipelineConfig (frozen pipeline configuration with JSON serialization)
- [x] TheoryModule Protocol (phase-based dispatch with auto-discovery)
- [x] Engine modularization (state.py, grading.py, statistics.py)
- [x] Engagement protocol unification (4th phase: `contribute_engagement_delta`)
- [x] Spectrum refactoring (binary → continuous for employment/family/internet)
- [ ] GraphRAG integration (curriculum modeling)
- [ ] LLM-augmented mode (forum posts, assignment text)
- [ ] Parquet/Arrow export
- [x] PyPI package publication (`pip install synthedu`)
- [x] Interactive dashboard (Shiny + Plotly, dark/light themes, presets, validation)

---

## Legal Disclaimer

> **SynthEd's default generator produces fictional personas.** Outputs are intended for research, development, and educational purposes. Custom input data and optional LLM outputs need their own privacy review; the built-in checks are not a formal privacy guarantee. SynthEd is under active development -- APIs and output formats may change between versions.

See full [Legal Disclaimer](docs/GUIDE.md#-legal-disclaimer) and [Responsible Use](docs/GUIDE.md#-responsible-use) guidelines.

---

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and review requirements.

```bash
ruff check synthed/ tests/ --select E,F,W --ignore E501
python -m pytest tests/ -q --tb=short
python -m synthed.doc_facts
```

## Test Suite

With the development dependencies installed, pytest runs in parallel with up to
4 workers. Use `python -m pytest tests/ -n 0 -q --tb=short` for serial debugging;
see [CONTRIBUTING.md](CONTRIBUTING.md#development-setup) for worker controls.

[THEORY.md](docs/THEORY.md#-test-suite) contains the generated test inventory. `python -m synthed.doc_facts` checks the source-derived inventory and documented parameter counts. Actual pytest collection and skips depend on installed optional dependencies and browser availability. The CI badge uses a JUnit total that includes skipped entries; consult the CI job summary for the passed/skipped breakdown.

---

## License

MIT License. See [LICENSE](LICENSE).

## Citation

If you use SynthEd in your research, please cite using the [CITATION.cff](CITATION.cff) file or the Zenodo DOI above.

## Contributors

| Contributor | Role |
|-------------|------|
| [Halis Aykut Cosgun](https://orcid.org/0000-0003-0166-6237) | Lead Developer, Data Scientist & AI Engineer, Researcher -- Yozgat Bozok University |
| [Evrim Genc Kumtepe](https://orcid.org/0000-0002-2568-8054) | Research Advisor -- Anadolu University |
| [Claude](https://claude.ai) (Anthropic) | AI pair programmer -- implementation, testing, code review |

## Acknowledgments

Conceptually inspired by [TinyTroupe](https://github.com/microsoft/tinytroupe) (Microsoft), [MiroFish](https://github.com/666ghj/MiroFish), and [Agent Lightning](https://github.com/microsoft/agent-lightning). OULAD reference data: [Kuzilek et al. (2017)](https://doi.org/10.1038/sdata.2017.171).
