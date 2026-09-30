---
industry: education
region: Global
updated: 2026-09-30
---

# 🎯 Agentes AI — education

> Agentes y herramientas AI open source para educación. Foco: MIT / Apache 2.0 / BSD.
> Verificado repo por repo vía WebFetch el 2026-09-30 (stars y licencia leídos de la página del repo).

## Agentes y herramientas destacadas

**18 agentes reales verificados.** Ordenados por stars.
> Bloom y OpenTutorAI-CE se agregaron en la segunda pasada del 2026-09-30.
> **Claw-ED** se agregó en la tercera pasada del 2026-09-30 — es el primer agente *teacher-facing* open source de la KB.
> **Cuarta pasada del 2026-09-30:** +5 agentes (pyKT, FreeLingo, TutorIA, OpenDidactia, mentar) y **2 regiones cerradas** (OpenTutorAI-CE → Marruecos; Claw-ED → EE. UU.). La capa de evaluación se movió a su propia sección y se corrigió: el repo canónico es `UnifyingAITutorEvaluation` (32 ★), no `AITutor-EvalKit` (3 ★).

| Nombre | Repo | Licencia | Stars | Lenguaje | Descripción | Origen (región) |
|--------|------|----------|-------|----------|-------------|-----------------|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 40.6k | Python | Tutoría personalizada "lifelong"; workspace agent-native con 8 superficies (Chat, Partners, Co-Writer, Book, Knowledge, Space, Memory), memoria en 3 capas y RAG multi-engine. v1.6.12 del 2026-09-27, releases semanales | APAC (HKU Data Intelligence Lab, Hong Kong) |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 39.7k | TypeScript | Open Multi-Agent Interactive Classroom: convierte un tema o documento en una clase interactiva multi-agente. Agent workbench, sesiones durables de course-building, skills reutilizables, persistencia pluggable. v1.1.2 del 2026-09-28. ⚠️ **Relicenciado de AGPL-3.0 a MIT en v0.3.0 (2026-06-28)**: la licencia permisiva tiene ~3 meses, no es el historial completo del proyecto | APAC (Tsinghua / THU-MAIC, China) |
| Project NOMAD | https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | 38.8k | JavaScript | Servidor de conocimiento y educación offline-first: Wikipedia, libros, cursos, mapas y AI local opcional, todo en Docker sobre hardware propio, sin internet. ~5 GB disco, <1 GB RAM sin el módulo AI | North America (Crosstalk Solutions, EE. UU.) |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 ⚠️ | 814 | Markdown/YAML | 165 skills pedagógicas evidence-grounded en 20 dominios (pedagogía, learning science, currículo, evaluación) para orquestar agentes. Corre en Claude Code, Claude.ai vía MCP, Codex y Hermes | EMEA (autor UK) |
| py-fsrs | https://github.com/open-spaced-repetition/py-fsrs | MIT | 499 | Python | Free Spaced Repetition Scheduler: modelo DSR (Difficulty, Stability, Retrievability) con 21 parámetros optimizables. La pieza de scheduling que le falta a casi todo tutor LLM | Global (org open-spaced-repetition) |
| Educhain | https://github.com/satvik314/educhain | MIT | 389 | Python | Genera contenido educativo con GenAI: MCQs, lesson plans con 8 enfoques pedagógicos, flashcards. Ingesta desde YouTube, imágenes, URLs y PDFs | APAC (Build Fast with AI, India) |
| pyKT | https://github.com/pykt-team/pykt-toolkit | MIT | 441 | Python | Librería de **knowledge tracing** sobre PyTorch: preprocesamiento estandarizado de 7+ datasets, 5 escenarios de predicción y 10+ modelos DLKT comparables entre sí. 811 commits. **No es un agente: es la pieza que le falta a los agentes** — el modelo de estado del alumno que ningún tutor LLM tiene | APAC (Jinan University / Guangdong Institute of Smart Education, China) |
| FreeLingo | https://github.com/artcc/freelingo | **AGPL-3.0** ⚠️ | 150 | Python | Plataforma self-hosted de aprendizaje de idiomas con AI: evalúa nivel CEFR con un LLM local (Ollama) o cloud, genera plan de estudio personalizado, tutor conversacional por voz, flashcards y repetición espaciada. FastAPI + Next.js + Postgres + Redis, todo en Docker Compose | Sin región verificada (el repo no declara ubicación) |
| Bloom | https://github.com/Li-Evan/Bloom | MIT | 278 | Python | Tutor personal que genera un syllabus, entrega una lección a la vez, lee anotaciones y feedback y ajusta la siguiente lección al nivel real de comprensión. Dos modos: CLI como skill de Claude Code (sin backend) y web self-hosted (React + FastAPI, cualquier LLM OpenAI-compatible) | Sin región verificada |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 265 | JavaScript | Intelligent Tutoring System con Bayesian Knowledge Tracing para estimar mastery. Deploy en dos clicks a GitHub Pages, A/B testing incorporado, 3 libros de contenido curado (OpenStax) en JSON | North America (CAHLR, UC Berkeley) |
| OpenTutor | https://github.com/zijinz456/OpenTutor | MIT | 127 | Python | Workspace de aprendizaje adaptativo block-based que corre local: subís material → notas, quizzes, flashcards y tutor adaptativo. FSRS + detección de carga cognitiva, 10+ providers LLM | Sin región verificada |
| OpenTutorAI-CE | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 107 | Python | Plataforma de tutoría personalizada: multi-model, RAG local, interacción por voz y video, control de acceso por roles. PWA multilingüe (árabe, francés, inglés). Community Edition que sirve de base a una Enterprise Edition | **EMEA (Marruecos)** — el perfil de la organización declara `Morocco` y `opentutorai.com`. *Región cerrada en el pase 4* |
| Claw-ED | https://github.com/SirhanMacx/Claw-ED | MIT | 59 | Python | Agente CLI local-first para **docentes**: se apunta a una carpeta de lecciones viejas, infiere el estilo de enseñanza y genera bundles completos — plan de clase, handouts, versiones diferenciadas, juegos y evaluaciones — como DOCX de docente, DOCX de alumno y PPTX de slides en una sola corrida. 48+ tools, alineación a estándares estatales, cualquier provider LLM, y un bot de Telegram con la misma memoria. `pip install clawed`. v9.18.2026.1 (Beta), 778 commits | **North America (Nueva York, EE. UU.)** — *inferido de artefactos, no declarado*: el perfil no publica ubicación, pero sus otros repos son `gnps-civic-readiness` ("NYS Seal of Civic Readiness portal — built for Great Neck Public Schools") y `mr-macs-review-arcade` (repaso de **Regents** y AP). Regents + Great Neck Public Schools son instituciones del estado de Nueva York. *Cerrada en el pase 4 con este nivel de confianza declarado* |
| tutor-mcp | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 42 | Go | Servidor MCP que convierte cualquier LLM en un ITS: estado durable del aprendiz, scheduling de repaso, memoria de sesión, misconceptions, metacognición y decisiones pedagógicas auditables | Sin región verificada |
| gradescope-mcp | https://github.com/Yuanpeng-Li/gradescope-mcp | MIT | 8 | Python | Servidor MCP para Gradescope: 34 tools de gestión de cursos, batch grading, CRUD de rúbricas y regrade review. Escrituras detrás de confirmación explícita | Sin región verificada |
| TutorIA | https://github.com/LabSirius/TutorIA | MIT | 0 | Python | Tutor conversacional autónomo para **educación superior rural**, integrado dentro de Open edX y con la API de Claude como motor. Chat en lenguaje natural, respuestas en audio (TTS), avatar animado, dashboard de estadísticas para el docente y persistencia de contexto entre sesiones. Materias iniciales: Programación I (Python) e Introducción a la Matemática | **LATAM (Pereira, Colombia)** — Grupo Sirius, Universidad Tecnológica de Pereira (`sirius.utp.edu.co`) |
| OpenDidactia | https://github.com/nmarafo/OpenDidactia | CC BY-SA 4.0 ⚠️ | 0 | Markdown/YAML | Esquemas curriculares estructurados (estándar OKF) para que un agente genere **Programaciones Didácticas y Situaciones de Aprendizaje** conformes a la ley educativa española LOMLOE. Cubre las 17 comunidades autónomas y 2 ciudades autónomas, de Infantil a Bachillerato, FP y enseñanzas de régimen especial, con DUA y rúbricas analíticas. No es código: es el *esquema de salida* que hace auditable a un agente docente | EMEA (España) |
| mentar | https://github.com/avps82/mentar | **AGPL-3.0-only** ⚠️ | 1 | Python | Tutor local-first para chicos: corre entero en la máquina del hogar, sin cuentas ni datos que salgan del dispositivo. 934 nodos de concepto en 157 plantillas curriculares (Australia ACARA v9, India, Singapur, EE. UU.). **El detalle de diseño que importa:** el LLM sólo explica y un *checker determinístico* corrige cada respuesta, así que el modelo no puede darle por buena una respuesta incorrecta a un chico. Último commit 2026-08-26 | Sin región verificada (currículo AU primero, pero el repo no declara ubicación) |

## Investigación / evaluación

**Reescrita en el pase 4 del 2026-09-30.** Las tres pasadas anteriores registraron un solo evaluador pedagógico (`AITutor-EvalKit`, 3 ★) y concluyeron que "no existe el LegalBench de educación". Buscando por *benchmark* en vez de por *repo de agente* aparecen tres artefactos más, y uno de ellos es diez veces más grande que el que la KB tenía anotado.

| Nombre | Repo | Licencia | Stars | Qué evalúa |
|--------|------|----------|-------|-----------|
| **pyKT** | https://github.com/pykt-team/pykt-toolkit | MIT ✅ | 441 | *(también en la tabla principal)* Benchmark de **knowledge tracing**, no de calidad conversacional: 10+ modelos DLKT sobre 7+ datasets con preprocesamiento estandarizado. Es el más maduro de esta capa por un orden de magnitud |
| **MathTutorBench** | https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | 42 | Capacidades pedagógicas *abiertas* de un tutor LLM en matemática: 3 habilidades docentes de alto nivel y 7 tareas concretas, con reward models entrenados para medir calidad de enseñanza y leaderboard publicado. **EMNLP 2025 (Oral)** |
| **UnifyingAITutorEvaluation** | https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | 32 | Taxonomía de 8 dimensiones pedagógicas para respuestas de tutor ante el error de un alumno. Publica **MRBench** en tres versiones: V1 (192 diálogos × 8 dim.), V2 (200 × 8), V3 (300 × 4). **NAACL 2025, Senior Area Chair Award** |
| AITutor-EvalKit | https://github.com/kaushal0494/AITutor-EvalKit | MIT ✅ | 3 | Implementación LoMTL (LoRA multi-task) sobre las 4 dimensiones del subconjunto MRBench. Demo en EACL 2026 (Rabat). Origen: MBZUAI, Abu Dhabi → EMEA |
| AI-Teaching-Agent | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT ✅ | 0 | Convierte fuentes en Markdown en artefactos **Lab, Exam y Grading** como DSL validado, más slides opcionales. Human review obligatorio, evaluación sandboxeada, servidor **MCP stdio**, y previews de examen "candidate-safe" que excluyen respuestas y referencias internas de corrección. *Agregado en la tercera pasada* |

### Corrección: el repo canónico de MRBench no es el que la KB tenía

`AITutor-EvalKit` (3 ★) y `UnifyingAITutorEvaluation` (32 ★) son **del mismo autor** (Kaushal Kumar Maurya). El pase 1 registró el chico y no el grande. El grande es el que publica la taxonomía completa de 8 dimensiones y las tres versiones de MRBench; el chico es la implementación LoMTL sobre un subconjunto de 4 dimensiones. **Para evaluar un tutor, el punto de partida es `UnifyingAITutorEvaluation`.**

### Leer la licencia antes de usar estos benchmarks en un entregable

Tres de los cinco **no son licencias de código**:

- **MathTutorBench es CC BY 4.0** — atribución, sin share-alike. El más limpio de los tres no-código: se puede usar en un entregable cerrado citando la fuente.
- **UnifyingAITutorEvaluation es CC BY-SA 4.0** — *share-alike*. Un dataset derivado hereda la obligación. Usable para medir internamente; **revisar con legal antes de redistribuir un derivado**.
- **pyKT y AITutor-EvalKit son MIT** — sin fricción.

La distinción importa porque el uso típico de un benchmark en un engagement es *derivar* uno propio con los datos del cliente, y ahí es exactamente donde muerde el share-alike.

### Por qué `AI-Teaching-Agent` vale seguirlo con 0 estrellas

El gap 6 de esta KB dice que no existe grading open source y que el camino realista es orquestar al incumbente propietario (`gradescope-mcp` sobre Gradescope). Este repo es el primer intento que vemos de la otra estrategia: **generar el artefacto de corrección como DSL auditable** en vez de llamar a un grader externo. El diseño es el correcto para EU AI Act y para los estatutos de EE. UU. que prohíben grading automático — DSL validado, revisión humana en el medio, preview sin respuestas. **No usarlo todavía:** 0 estrellas y 30 commits es un proyecto de una persona sin garantía de continuidad. Registrarlo como la señal de que la categoría empezó a moverse, y re-verificarlo el próximo ciclo.

⚠️ **Varios de esta sección son pre-tracción** (3, 0 y 0 stars). Se incluyen porque son los únicos artefactos open source que encontramos para evaluación pedagógica y grading estructurado, no porque tengan adopción. Ver los gaps 1, 6 y 9 en `intel/trends.md`.

## Advertencias de licencia

**Actualizado en el pase 4:** la tabla principal ya **no** es "todo MIT o Apache-2.0". Al agregar agentes nuevos entraron dos AGPL y dos Creative Commons, y eso cambia qué se puede empaquetar en un entregable cerrado.

| Licencia | Repos | Qué implica para un entregable de cliente |
|----------|-------|-------------------------------------------|
| MIT / Apache-2.0 / BSD-3 ✅ | DeepTutor, OpenMAIC, Project NOMAD, py-fsrs, Educhain, pyKT, Bloom, OATutor, OpenTutor, OpenTutorAI-CE, Claw-ED, tutor-mcp, gradescope-mcp, TutorIA | Sin fricción. Construible y redistribuible cerrado |
| **AGPL-3.0** ⚠️ | **FreeLingo**, **mentar** | Copyleft **de red**: si se modifica y se sirve por SaaS, hay obligación de publicar el fuente modificado. No forkear para un producto cerrado; usar como referencia de arquitectura o desplegar sin modificar |
| **CC BY-SA 4.0** ⚠️ | **education-agent-skills**, **OpenDidactia**, **UnifyingAITutorEvaluation** | Contenido con *share-alike*: los derivados heredan la obligación. Usable como referencia pedagógica o para medir internamente; **revisar con legal antes de empaquetarlo en un entregable cerrado** |
| **CC BY 4.0** | **MathTutorBench** | Sólo atribución, sin share-alike. El más limpio de los no-código |

**La trampa concreta:** `FreeLingo` aparece como MIT en artículos de prensa y agregadores. **La página del repo dice AGPL-3.0.** Se verificó en el pase 4 y se registra acá porque es el modo de falla típico — citar la licencia del listicle en vez de la del repo.

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
