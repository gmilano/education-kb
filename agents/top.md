---
industry: education
region: Global
updated: 2026-09-30
---

# 🎯 Agentes AI — education

> Agentes y herramientas AI open source para educación. Foco: MIT / Apache 2.0 / BSD.
> Verificado repo por repo vía WebFetch el 2026-09-30 (stars y licencia leídos de la página del repo).

## Agentes y herramientas destacadas

13 agentes reales verificados. Ordenados por stars.
> Bloom y OpenTutorAI-CE se agregaron en la segunda pasada del 2026-09-30.
> **Claw-ED** se agregó en la tercera pasada del 2026-09-30 — es el primer agente *teacher-facing* open source de la KB.

| Nombre | Repo | Licencia | Stars | Lenguaje | Descripción | Origen (región) |
|--------|------|----------|-------|----------|-------------|-----------------|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 40.6k | Python | Tutoría personalizada "lifelong"; workspace agent-native con 8 superficies (Chat, Partners, Co-Writer, Book, Knowledge, Space, Memory), memoria en 3 capas y RAG multi-engine. v1.6.12 del 2026-09-27, releases semanales | APAC (HKU Data Intelligence Lab, Hong Kong) |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 39.7k | TypeScript | Open Multi-Agent Interactive Classroom: convierte un tema o documento en una clase interactiva multi-agente. Agent workbench, sesiones durables de course-building, skills reutilizables, persistencia pluggable. v1.1.2 del 2026-09-28. ⚠️ **Relicenciado de AGPL-3.0 a MIT en v0.3.0 (2026-06-28)**: la licencia permisiva tiene ~3 meses, no es el historial completo del proyecto | APAC (Tsinghua / THU-MAIC, China) |
| Project NOMAD | https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | 38.8k | JavaScript | Servidor de conocimiento y educación offline-first: Wikipedia, libros, cursos, mapas y AI local opcional, todo en Docker sobre hardware propio, sin internet. ~5 GB disco, <1 GB RAM sin el módulo AI | North America (Crosstalk Solutions, EE. UU.) |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 ⚠️ | 814 | Markdown/YAML | 165 skills pedagógicas evidence-grounded en 20 dominios (pedagogía, learning science, currículo, evaluación) para orquestar agentes. Corre en Claude Code, Claude.ai vía MCP, Codex y Hermes | EMEA (autor UK) |
| py-fsrs | https://github.com/open-spaced-repetition/py-fsrs | MIT | 499 | Python | Free Spaced Repetition Scheduler: modelo DSR (Difficulty, Stability, Retrievability) con 21 parámetros optimizables. La pieza de scheduling que le falta a casi todo tutor LLM | Global (org open-spaced-repetition) |
| Educhain | https://github.com/satvik314/educhain | MIT | 389 | Python | Genera contenido educativo con GenAI: MCQs, lesson plans con 8 enfoques pedagógicos, flashcards. Ingesta desde YouTube, imágenes, URLs y PDFs | APAC (Build Fast with AI, India) |
| Bloom | https://github.com/Li-Evan/Bloom | MIT | 278 | Python | Tutor personal que genera un syllabus, entrega una lección a la vez, lee anotaciones y feedback y ajusta la siguiente lección al nivel real de comprensión. Dos modos: CLI como skill de Claude Code (sin backend) y web self-hosted (React + FastAPI, cualquier LLM OpenAI-compatible) | Sin región verificada |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 265 | JavaScript | Intelligent Tutoring System con Bayesian Knowledge Tracing para estimar mastery. Deploy en dos clicks a GitHub Pages, A/B testing incorporado, 3 libros de contenido curado (OpenStax) en JSON | North America (CAHLR, UC Berkeley) |
| OpenTutor | https://github.com/zijinz456/OpenTutor | MIT | 127 | Python | Workspace de aprendizaje adaptativo block-based que corre local: subís material → notas, quizzes, flashcards y tutor adaptativo. FSRS + detección de carga cognitiva, 10+ providers LLM | Sin región verificada |
| OpenTutorAI-CE | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 107 | Python | Plataforma de tutoría personalizada: multi-model, RAG local, interacción por voz y video, control de acceso por roles. Community Edition que sirve de base a una Enterprise Edition | Sin región verificada |
| Claw-ED | https://github.com/SirhanMacx/Claw-ED | MIT | 59 | Python | Agente CLI local-first para **docentes**: se apunta a una carpeta de lecciones viejas, infiere el estilo de enseñanza y genera bundles completos — plan de clase, handouts, versiones diferenciadas, juegos y evaluaciones — como DOCX de docente, DOCX de alumno y PPTX de slides en una sola corrida. 48+ tools, alineación a estándares estatales, cualquier provider LLM, y un bot de Telegram con la misma memoria. `pip install clawed`. v9.18.2026.1 (Beta), 778 commits | Sin región verificada |
| tutor-mcp | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 42 | Go | Servidor MCP que convierte cualquier LLM en un ITS: estado durable del aprendiz, scheduling de repaso, memoria de sesión, misconceptions, metacognición y decisiones pedagógicas auditables | Sin región verificada |
| gradescope-mcp | https://github.com/Yuanpeng-Li/gradescope-mcp | MIT | 8 | Python | Servidor MCP para Gradescope: 34 tools de gestión de cursos, batch grading, CRUD de rúbricas y regrade review. Escrituras detrás de confirmación explícita | Sin región verificada |

## Investigación / evaluación

| Nombre | Repo | Licencia | Stars | Nota |
|--------|------|----------|-------|------|
| AITutor-EvalKit | https://github.com/kaushal0494/AITutor-EvalKit | MIT | 3 | Framework de evaluación de la calidad *pedagógica* de tutores LLM en matemática: 4 dimensiones (Mistake Identification, Mistake Location, Providing Guidance, Actionability), modelo LoMTL (LoRA multi-task), dataset MRBench (491 diálogos). Demo en EACL 2026 (Rabat). Origen: MBZUAI, Abu Dhabi → EMEA |
| AI-Teaching-Agent | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT | 0 | Convierte fuentes en Markdown en artefactos **Lab, Exam y Grading** como DSL validado, más slides opcionales. Human review obligatorio, evaluación sandboxeada, servidor **MCP stdio** con adaptadores de tools, y previews de examen "candidate-safe" que excluyen respuestas y referencias internas de corrección. Python, 30 commits. *Agregado en la tercera pasada del 2026-09-30* |

⚠️ **Los dos son pre-tracción: 3 y 0 stars.** Se incluyen porque son los únicos artefactos open source que encontramos para evaluación pedagógica y para grading estructurado respectivamente, no porque tengan adopción. Ver los gaps 1 y 6 en `intel/trends.md`.

**Por qué `AI-Teaching-Agent` vale seguirlo con 0 estrellas.** El gap 6 de esta KB dice que no existe grading open source y que el camino realista es orquestar al incumbente propietario (`gradescope-mcp` sobre Gradescope). Este repo es el primer intento que vemos de la otra estrategia: **generar el artefacto de corrección como DSL auditable** en vez de llamar a un grader externo. El diseño es el correcto para EU AI Act y para los estatutos de EE. UU. que prohíben grading automático — DSL validado, revisión humana en el medio, preview sin respuestas. **No usarlo todavía:** 0 estrellas y 30 commits es un proyecto de una persona sin garantía de continuidad. Registrarlo como la señal de que la categoría empezó a moverse, y re-verificarlo el próximo ciclo.

## Advertencias de licencia

- **education-agent-skills es CC BY-SA 4.0**, no una licencia de código permisiva. Es contenido con *share-alike*: los derivados de esas skills heredan la obligación de licenciarse igual. Usable como referencia pedagógica; **revisar con legal antes de empaquetarlo en un entregable cerrado de cliente.**
- Todo el resto de la tabla principal es MIT o Apache-2.0 → construible por Globant sin fricción.

## Corrección sobre ciclos anteriores

Los star counts registrados en ciclos previos de esta KB estaban **inflados por el pipeline**, no medidos. Valores reales verificados hoy contra los que se habían registrado antes:

| Repo | Registrado antes | Real 2026-09-30 |
|------|------------------|-----------------|
| Educhain | ~12k ★ | **389 ★** |
| OATutor | ~1.5k ★ | **265 ★** |
| OpenTutor | ~900 ★ | **127 ★** |
| DeepTutor | ~24k ★ | **40.6k ★** (subestimado) |
| OpenTutorAI-CE | ~600 ★ y Apache-2.0 | **107 ★ y BSD-3-Clause** (stars y licencia, las dos mal) |

Los tres primeros estaban sobreestimados entre 7x y 30x, y en OpenTutorAI-CE el pipeline además reportó la licencia equivocada. Tratar cualquier cifra de ciclos anteriores no re-verificada como no confiable — y verificar la licencia junto con las stars, porque el error no se limitó a los números.

---
*Verificado manualmente vía WebFetch, no por el pipeline automático. Última verificación: 2026-09-30.*
