---
industry: education
region: Global
updated: 2026-10-01
---

# 🎯 Agentes AI — education

> Agentes y herramientas AI open source para educación. Foco: MIT / Apache 2.0 / BSD.
> Verificado repo por repo vía WebFetch el 2026-09-30 (stars y licencia leídos de la página del repo).
> **Pase 10 del 2026-10-01:** para el contenido, la verificación se hizo contra el archivo `LICENSE`, no contra el README — y por eso apareció la contradicción que documenta la capa de contenido curricular, abajo.

## Agentes y herramientas destacadas

**29 agentes reales verificados.** Ordenados por stars.
> *Pase 11 del 2026-10-01:* +3 en la tabla principal (**learn**, **Gnos**, **Alvarmethod**) y una **capa predictiva / early warning** nueva al final del archivo, que es la capa peor abastecida de esta KB y la que el Anexo III del EU AI Act nombra de forma explícita.
> *Pase 12 del 2026-10-01:* +1 en la tabla principal (**Study-Mate**), +1 en la capa MCP (**anki-mcp-server**, que
> multiplica por 499 el techo de esa capa) y +1 en evaluación (**ArguLens**). Se abre la **capa de distribución por
> skills de agente** al final del archivo: es la primera capa de esta KB que se mide contra otra vertical, y la
> educación pierde 58× contra la científica en el mismo canal. El conteo de 29 de la tabla principal se verificó a
> mano en este pase y **estaba bien**.
> *Corrección de conteo del pase 10:* el encabezado decía **24** y la tabla tenía **25** filas antes de este pase. El desfasaje venía de pasadas anteriores que agregaron filas sin actualizar el total. Contado a mano: **26** con la fila que agrega el pase 10.
> Bloom y OpenTutorAI-CE se agregaron en la segunda pasada del 2026-09-30.
> **Claw-ED** se agregó en la tercera pasada del 2026-09-30 — es el primer agente *teacher-facing* open source de la KB.
> **Cuarta pasada del 2026-09-30:** +5 agentes (pyKT, FreeLingo, TutorIA, OpenDidactia, mentar) y **2 regiones cerradas** (OpenTutorAI-CE → Marruecos; Claw-ED → EE. UU.). La capa de evaluación se movió a su propia sección y se corrigió: el repo canónico es `UnifyingAITutorEvaluation` (32 ★), no `AITutor-EvalKit` (3 ★).
> **Sexta pasada del 2026-09-30:** +1 en la tabla principal (**learnmcp-xapi**, el puente MCP hacia la capa de telemetría xAPI) y +1 en evaluación (**L2-Bench**, de Oxford University Press, que cierra el sub-gap de *lengua* — ⚠️ **no verificado de primera mano**, ver la advertencia en su fila). La capa de almacenamiento (los LRS) vive en `repos/foundations.md`, no acá: no son agentes.
> **Quinta pasada del 2026-09-30:** +2 en la tabla principal (**Aila**, de Oak National Academy, y **pyBKT**), +3 en evaluación (**SafeTutors**, **EduBench**, **EduGuardBench**) y una sección nueva de servidores MCP de mastery. **El gap 8 se corrige:** la capa teacher-facing open source no era un solo repo de 59 ★.

> **Séptima pasada del 2026-10-01:** +3 en la tabla principal (**llamatutor**, **ChatTutor**, **tutor-gpt**) y +1 en evaluación (**ProHist-Bench**). Los tres nuevos entraron por un cambio de consulta, no por ser nuevos: las seis pasadas anteriores buscaron `agent`, `benchmark` y `tutoring system`, **nunca `tutor`**, que es la palabra que usa el mercado. Suman 4.3k estrellas y **ninguno se puede empaquetar en un entregable cerrado** — ver las advertencias de licencia. Se registra además una **colisión de nombres** con `Bloom` y la **capa de datos de entrenamiento** (ver `repos/foundations.md`), que es la que decide si `pyKT`/`pyBKT` sirven de verdad.

> **Octava pasada del 2026-10-01:** se abre una **capa que la KB no tenía en siete pasadas — accesibilidad y educación especial** (sección nueva abajo, 11 repos verificados). El hallazgo no es un repo: es la forma del segmento. **Lo maduro es copyleft** (OptiKey 4.4k ★ GPL-3.0, Cboard 759 ★ GPL-3.0) y **lo que es agéntico y permisivo no pasa de 15 estrellas**. Entra además **`tero`** (MIT, Chile) en la tabla principal, que es la primera pieza de esta KB que cierra tres gaps a la vez (2, 8 y 12). Ver el **gap 12** y el **trend 18** en `intel/trends.md`, y los patrones **P17** y **P18**.

> **Novena pasada del 2026-10-01:** se abre la **capa de credenciales verificables e interoperabilidad** (sección nueva abajo). Es la capa que acredita el aprendizaje cuando termina — Open Badges 3.0, W3C Verifiable Credentials, QTI, OneRoster, Caliper — y ocho pasadas no la buscaron porque no se llama «agente» ni «tutor». **El hallazgo no es un repo: es que tres implementaciones de referencia de estos estándares ya no están** (`badgr-server` 404, `caliper-php` puesto en privado por 1EdTech según el banner del fork de la U. de Michigan, `caliper-python` 404) mientras los estándares siguen siendo obligatorios. Lo que queda vivo y permisivo es de **terceros certificados y consorcios universitarios**. Ver el **trend 19**, los **gaps 13 y 14** y los patrones **P19**, **P20** y **P21**.

> **Décima pasada del 2026-10-01:** se abre la **capa de contenido curricular** — de qué lee el tutor. Nueve pasadas construyeron el agente, el modelado, la evaluación, la seguridad, la telemetría, los datos, la accesibilidad y la credencial, y **ninguna preguntó de dónde sale el material que el agente enseña**: la palabra «OER» no aparecía ni una vez en esta KB. **El hallazgo es una trampa de licencia que pega sobre el patrón P1 de esta KB**, y está verificada contra el archivo `LICENSE` de los repos: los bundles de contenido de **OpenStax publicados en GitHub dicen CC BY-NC-SA** en los tres títulos revisados, mientras el único puente agente↔contenido que existe (`openstax-mcp-server`) **anuncia en su README que el contenido es CC BY 4.0**. Entra ese puente en la tabla principal. Ver el **trend 22**, los **gaps 15 y 16** y los patrones **P22**, **P23** y **P24**.

| Nombre | Repo | Licencia | Stars | Lenguaje | Descripción | Origen (región) |
|--------|------|----------|-------|----------|-------------|-----------------|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 40.6k | Python | Tutoría personalizada "lifelong"; workspace agent-native con 8 superficies (Chat, Partners, Co-Writer, Book, Knowledge, Space, Memory), memoria en 3 capas y RAG multi-engine. v1.6.12 del 2026-09-27, releases semanales | APAC (HKU Data Intelligence Lab, Hong Kong) |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 39.7k | TypeScript | Open Multi-Agent Interactive Classroom: convierte un tema o documento en una clase interactiva multi-agente. Agent workbench, sesiones durables de course-building, skills reutilizables, persistencia pluggable. v1.1.2 del 2026-09-28. ⚠️ **Relicenciado de AGPL-3.0 a MIT en v0.3.0 (2026-06-28)**: la licencia permisiva tiene ~3 meses, no es el historial completo del proyecto | APAC (Tsinghua / THU-MAIC, China) |
| Project NOMAD | https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | 38.8k | JavaScript | Servidor de conocimiento y educación offline-first: Wikipedia, libros, cursos, mapas y AI local opcional, todo en Docker sobre hardware propio, sin internet. ~5 GB disco, <1 GB RAM sin el módulo AI | North America (Crosstalk Solutions, EE. UU.) |
| learn | https://github.com/amosblomqvist/learn | 🚫 **sin licencia** | 2.9k | TypeScript/Markdown | "My AI learning system": no es software, es una **configuración `.pi`** —una skill con la filosofía de enseñanza, unas extensiones chicas y definiciones de subagentes (researcher, generadores de SVG y Mermaid)— que entrega lecciones, verifica datos, hace preguntas de quiz con feedback y loguea el progreso en Markdown. **El artefacto educativo más estrellado creado en esta ventana, y tiene 2 commits.** 🚫 No reutilizable: sin archivo de licencia el default legal es todos los derechos reservados. *Agregado en el pase 11* | Sin región declarada |
| llamatutor | https://github.com/Nutlope/llamatutor | 🚫 **sin licencia** | 2.1k | TypeScript | Tutor personal sobre **Llama 3 70B + Together.ai**: Next.js + Tailwind, Exa.js para búsqueda web y Helicone para observabilidad. Es una aplicación de producción, no una librería. 132 commits. 🚫 **No reutilizable:** se pidió `/blob/main/LICENSE` y devuelve **404** — sin archivo de licencia el default legal es todos los derechos reservados, con 2.1k estrellas o con ninguna. *Agregado en el pase 7* | Sin región declarada |
| ChatTutor | https://github.com/HugeCatLab/ChatTutor | **AGPL-3.0** ⚠️ | 1.3k | TypeScript | Tutor **visual e interactivo**: canvas de matemática para ecuaciones y diagramas y mapas mentales para visualizar conocimiento, **expuestos al LLM como herramientas que usa mientras explica** — es el único agente de esta KB que le da al modelo instrumentos de pizarrón en vez de sólo texto. Desplegado en `chattutor.app` con API key del usuario. README bilingüe inglés/中文. *Agregado en el pase 7* | Sin país declarado (documentación EN/中文) |
| tutor-gpt | https://github.com/plastic-labs/tutor-gpt | **GPL-3.0** ⚠️ | 931 | TypeScript | Compañero de aprendizaje con **razonamiento de teoría de la mente**: modela el estado mental del alumno —qué entiende, qué cree mal, con qué intención pregunta— y **reescribe sus propios prompts** en función de eso. Es un eje **complementario** al knowledge tracing de `pyKT`/`pyBKT`, no un sustituto: aquél modela qué conceptos domina, éste qué está pensando. Next.js + Supabase, inferencia vía OpenRouter, personalización delegada a **`Honcho`** (ver `repos/foundations.md`). 356 commits. ⚠️ Su versión hospedada se llama **"Bloom"** — **no es el `Bloom` de esta tabla**, ver la advertencia abajo. *Agregado en el pase 7* | **North America (EE. UU.)** — el perfil de la organización declara `United States of America` y `plasticlabs.ai` |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 ⚠️ | 815 | Markdown/YAML | 165 skills pedagógicas evidence-grounded en 20 dominios (pedagogía, learning science, currículo, evaluación) para orquestar agentes. Corre en Claude Code, Claude.ai vía MCP, Codex y Hermes | EMEA (autor UK) |
| py-fsrs | https://github.com/open-spaced-repetition/py-fsrs | MIT | 499 | Python | Free Spaced Repetition Scheduler: modelo DSR (Difficulty, Stability, Retrievability) con 21 parámetros optimizables. La pieza de scheduling que le falta a casi todo tutor LLM | Global (org open-spaced-repetition) |
| Educhain | https://github.com/satvik314/educhain | MIT | 389 | Python | Genera contenido educativo con GenAI: MCQs, lesson plans con 8 enfoques pedagógicos, flashcards. Ingesta desde YouTube, imágenes, URLs y PDFs | APAC (Build Fast with AI, India) |
| pyKT | https://github.com/pykt-team/pykt-toolkit | MIT | 441 | Python | Librería de **knowledge tracing** sobre PyTorch: preprocesamiento estandarizado de 7+ datasets, 5 escenarios de predicción y 10+ modelos DLKT comparables entre sí. 811 commits. **No es un agente: es la pieza que le falta a los agentes** — el modelo de estado del alumno que ningún tutor LLM tiene | APAC (Jinan University / Guangdong Institute of Smart Education, China) |
| Gnos | https://github.com/madhvantyagi/Gnos | MIT ✅ | 304 | Python | *Teaching harness* hecho de skills, scripts y herramientas visuales: toma un objetivo de aprendizaje con preferencias de profundidad y tiempo, arma el curso con subagentes que después revisa, y genera gráficos con **JSXGraph**, búsqueda en Khan Academy, PDFs y video. **La decisión de diseño que lo hace citable:** su registro de evidencia distingue *vio la explicación* / *resolvió con ayuda* / *resolvió solo* — es la distinción que casi ningún tutor LLM instrumenta, y es la que hace falta para cualquier medición de mastery. Guía docente en archivos `SOUL.md`. 344 commits. Corre en Codex, Claude Code, OpenCode y Antigravity. *Agregado en el pase 11* | Sin región declarada |
| FreeLingo | https://github.com/artcc/freelingo | **AGPL-3.0** ⚠️ | 150 | Python | Plataforma self-hosted de aprendizaje de idiomas con AI: evalúa nivel CEFR con un LLM local (Ollama) o cloud, genera plan de estudio personalizado, tutor conversacional por voz, flashcards y repetición espaciada. FastAPI + Next.js + Postgres + Redis, todo en Docker Compose | Sin región verificada (el repo no declara ubicación) |
| Bloom | https://github.com/Li-Evan/Bloom | MIT | 278 | Python | Tutor personal que genera un syllabus, entrega una lección a la vez, lee anotaciones y feedback y ajusta la siguiente lección al nivel real de comprensión. Dos modos: CLI como skill de Claude Code (sin backend) y web self-hosted (React + FastAPI, cualquier LLM OpenAI-compatible) | Sin región verificada |
| pyBKT | https://github.com/CAHLR/pyBKT | MIT | 281 | Python | **Bayesian Knowledge Tracing en Python**, del mismo laboratorio que OATutor. Estima mastery cognitivo desde secuencias de resolución de problemas, con variantes que individualizan parámetros por alumno y tasas de aprendizaje por ítem. 379 commits, publicado en **EDM 2021** (Badrinath, Wang & Pardos). Tampoco es un agente: es la alternativa **de procedencia estadounidense** a pyKT en la capa de modelado — más interpretable, menos potente (BKT clásico vs. deep learning). *Agregado en el pase 5* | North America (CAHLR, UC Berkeley) |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 265 | JavaScript | Intelligent Tutoring System con Bayesian Knowledge Tracing para estimar mastery. Deploy en dos clicks a GitHub Pages, A/B testing incorporado, 3 libros de contenido curado (OpenStax) en JSON | North America (CAHLR, UC Berkeley) |
| Alvarmethod | https://github.com/vasanthsreeram/Alvarmethod | MIT ✅ | 160 | Shell/Markdown | **Pedagogía empaquetada como skill portable**, instalable con `npx skills add vasanthsreeram/Alvarmethod -g --all` en Claude Code, Codex, Grok, Pi, OpenCode y Cursor a la vez. Implementa un loop explícito de cuatro pasos: *probe* (MCQ calificado para ubicar el hueco), *plan* (DAG en Mermaid armado para ese alumno), *teach* (un solo paso de razonamiento por vez, con visuales opcionales) y *lock-in quiz* con remediación. **Sólo 4 commits:** es una especificación pedagógica, no un producto — y eso es justamente lo que la hace reusable. Ver la tendencia 9 en `intel/trends.md`. *Agregado en el pase 11* | Sin región declarada |
| OpenTutor | https://github.com/zijinz456/OpenTutor | MIT | 127 | Python | Workspace de aprendizaje adaptativo block-based que corre local: subís material → notas, quizzes, flashcards y tutor adaptativo. FSRS + detección de carga cognitiva, 10+ providers LLM | Sin región verificada |
| OpenTutorAI-CE | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 107 | Python | Plataforma de tutoría personalizada: multi-model, RAG local, interacción por voz y video, control de acceso por roles. PWA multilingüe (árabe, francés, inglés). Community Edition que sirve de base a una Enterprise Edition | **EMEA (Marruecos)** — el perfil de la organización declara `Morocco` y `opentutorai.com`. *Región cerrada en el pase 4* |
| Claw-ED | https://github.com/SirhanMacx/Claw-ED | MIT | 59 | Python | Agente CLI local-first para **docentes**: se apunta a una carpeta de lecciones viejas, infiere el estilo de enseñanza y genera bundles completos — plan de clase, handouts, versiones diferenciadas, juegos y evaluaciones — como DOCX de docente, DOCX de alumno y PPTX de slides en una sola corrida. 48+ tools, alineación a estándares estatales, cualquier provider LLM, y un bot de Telegram con la misma memoria. `pip install clawed`. v9.18.2026.1 (Beta), 778 commits | **North America (Nueva York, EE. UU.)** — *inferido de artefactos, no declarado*: el perfil no publica ubicación, pero sus otros repos son `gnps-civic-readiness` ("NYS Seal of Civic Readiness portal — built for Great Neck Public Schools") y `mr-macs-review-arcade` (repaso de **Regents** y AP). Regents + Great Neck Public Schools son instituciones del estado de Nueva York. *Cerrada en el pase 4 con este nivel de confianza declarado* |
| Aila (Oak AI Lesson Assistant) | https://github.com/oaknational/oak-ai-lesson-assistant | MIT | 35 | TypeScript | Asistente de **planificación de clases para docentes** de **Oak National Academy** (nonprofit educativa británica respaldada por el gobierno). Monorepo Turborepo: Next.js + Prisma/PostgreSQL con **pgvector**, entornos de producción y staging, versionado semántico. **1.188 commits** — es el único artefacto teacher-facing de esta KB que corre en producción real y publica su código. ⚠️ El repo declara que está *"intended primarily for internal use by Oak National Academy"*: úsese como **referencia de arquitectura**, no como base de producto (sin API estable ni soporte para terceros). *Agregado en el pase 5* | EMEA (Oak National Academy, Reino Unido) |
| tutor-mcp | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 42 | Go | Servidor MCP que convierte cualquier LLM en un ITS: estado durable del aprendiz, scheduling de repaso, memoria de sesión, misconceptions, metacognición y decisiones pedagógicas auditables | Sin región verificada |
| learnmcp-xapi | https://github.com/DavidLMS/learnmcp-xapi | MIT | 15 | Python | Servidor MCP que le da a un agente memoria de aprendizaje **conforme al estándar**: tres tools sobre un Learning Record Store xAPI — registrar un statement, consultar el historial de progreso y gestionar el vocabulario de verbos/actividades. Backends: `lrsql`, `Ralph`, Veracity Learning, más arquitectura de plugins. Captura el aprendizaje de forma explícita ("practiqué bucles") o **inferida de la conversación**, y después consulta ese historial para adaptar la respuesta. **Es el único artefacto de esta KB que conecta un agente con IEEE 9274.1.1 (xAPI 2.0)** en vez de inventar su propio esquema. ⚠️ 32 commits: referencia de integración o base a forkear, no dependencia de producción. *Agregado en el pase 6* | **EMEA (España)** — el autor declara pertenecer al **IES Rafael Alberti**, instituto público de secundaria. Lo escribió un docente en ejercicio, no un laboratorio |
| openstax-mcp-server | https://github.com/pythpythpython/openstax-mcp-server | MIT (código) ✅ | 1 | TypeScript | Servidor MCP que le da a un agente acceso a **40+ libros de texto de OpenStax**: búsqueda semántica con embeddings de Cloudflare AI, generación automática de notebooks `.ipynb` por módulo y creación de problemas de práctica. Corre en Cloudflare Workers con Workers KV para cachear el XML parseado. **Es el único puente agente↔contenido curricular que encontró esta KB** — el equivalente, en la capa de contenido, de lo que `learnmcp-xapi` es en la capa de telemetría. 🔴 **Y hay que leerlo con la advertencia puesta: su README declara que el contenido servido es «Creative Commons Attribution 4.0 International (CC BY 4.0)», y el archivo `LICENSE` de los bundles de OpenStax en GitHub dice CC BY-NC-SA** en los tres títulos que este pase verificó. El código es MIT y es reutilizable; **la afirmación de licencia del contenido no se puede usar como base de un entregable facturado sin verificar título por título.** 7 commits. *Agregado en el pase 10* | Sin región verificada |
| gradescope-mcp | https://github.com/Yuanpeng-Li/gradescope-mcp | MIT | 8 | Python | Servidor MCP para Gradescope: 34 tools de gestión de cursos, batch grading, CRUD de rúbricas y regrade review. Escrituras detrás de confirmación explícita | Sin región verificada |
| TutorIA | https://github.com/LabSirius/TutorIA | MIT | 0 | Python | Tutor conversacional autónomo para **educación superior rural**, integrado dentro de Open edX y con la API de Claude como motor. Chat en lenguaje natural, respuestas en audio (TTS), avatar animado, dashboard de estadísticas para el docente y persistencia de contexto entre sesiones. Materias iniciales: Programación I (Python) e Introducción a la Matemática | **LATAM (Pereira, Colombia)** — Grupo Sirius, Universidad Tecnológica de Pereira (`sirius.utp.edu.co`) |
| OpenDidactia | https://github.com/nmarafo/OpenDidactia | CC BY-SA 4.0 ⚠️ | 0 | Markdown/YAML | Esquemas curriculares estructurados (estándar OKF) para que un agente genere **Programaciones Didácticas y Situaciones de Aprendizaje** conformes a la ley educativa española LOMLOE. Cubre las 17 comunidades autónomas y 2 ciudades autónomas, de Infantil a Bachillerato, FP y enseñanzas de régimen especial, con DUA y rúbricas analíticas. No es código: es el *esquema de salida* que hace auditable a un agente docente | EMEA (España) |
| mentar | https://github.com/avps82/mentar | **AGPL-3.0-only** ⚠️ | 1 | Python | Tutor local-first para chicos: corre entero en la máquina del hogar, sin cuentas ni datos que salgan del dispositivo. 934 nodos de concepto en 157 plantillas curriculares (Australia ACARA v9, India, Singapur, EE. UU.). **El detalle de diseño que importa:** el LLM sólo explica y un *checker determinístico* corrige cada respuesta, así que el modelo no puede darle por buena una respuesta incorrecta a un chico. Último commit 2026-08-26 | Sin región verificada (currículo AU primero, pero el repo no declara ubicación) |
| tero | https://github.com/marcorojasb/tero | **MIT** ✅ | 0 | Python | Agente docente de aula para K-12 **chileno**, de terminal y **offline-first**, sobre AWS Bedrock + Strands Agents SDK. Prepara material pedagógico y **adapta contenido para alumnos con necesidades especiales**. La decisión de diseño que lo hace citable: *«el agente propone, el docente decide»* — **el modelo no escribe archivos sin aprobación humana**. Anclado a instrumentos nacionales: MINEDUC, **Decreto 83** (educación especial) y **Ley 21.719** (protección de datos). 111 commits. **0 ★: referencia de arquitectura y contraparte local, no dependencia de producto.** *Agregado en el pase 8* | LATAM (Chile) |
| Study-Mate | https://github.com/Miaotofu01/Study-Mate | **MIT** ✅ | 482 | Python | Compañero de estudio con planificación curricular, instrucción y aprendizaje por proyectos en matemática y CS. *Workflow* integrado + motor de cursos HTML; corre sobre DeepSeek Harness, Google Antigravity y plugins de ChatGPT. 298 commits | APAC |

## ⚠️ Colisión de nombres: hay dos "Bloom" y son proyectos distintos (pase 7)

| Cuál | Repo / marca | Licencia | Stars | Qué es |
|---|---|---|---|---|
| **El `Bloom` de esta tabla** | https://github.com/Li-Evan/Bloom | **MIT** ✅ | 278 | Tutor que genera un syllabus y entrega una lección por vez, ajustando al nivel real de comprensión |
| **El otro "Bloom"** | marca de la versión hospedada de **`tutor-gpt`** (Plastic Labs) | **GPL-3.0** ⚠️ | 931 | Compañero de aprendizaje con razonamiento de teoría de la mente |

Las dos aluden a Benjamin Bloom, así que la colisión va a seguir apareciendo en búsquedas y en prensa.

**La trampa concreta:** buscar "Bloom AI tutor" devuelve material de los dos indistintamente, y es fácil citar **la arquitectura de uno con la licencia del otro** — y las licencias son MIT y GPL-3.0, que es la diferencia entre empaquetable y no empaquetable.

**Convención de esta KB:** `Bloom` sin más es siempre **`Li-Evan/Bloom` (MIT, 278 ★)**. Al otro se lo nombra **`tutor-gpt`**, nunca por su marca.

## Investigación / evaluación

**Reescrita en el pase 4 del 2026-09-30.** Las tres pasadas anteriores registraron un solo evaluador pedagógico (`AITutor-EvalKit`, 3 ★) y concluyeron que "no existe el LegalBench de educación". Buscando por *benchmark* en vez de por *repo de agente* aparecen tres artefactos más, y uno de ellos es diez veces más grande que el que la KB tenía anotado.

| Nombre | Repo | Licencia | Stars | Qué evalúa |
|--------|------|----------|-------|-----------|
| **pyKT** | https://github.com/pykt-team/pykt-toolkit | MIT ✅ | 441 | *(también en la tabla principal)* Benchmark de **knowledge tracing**, no de calidad conversacional: 10+ modelos DLKT sobre 7+ datasets con preprocesamiento estandarizado. Es el más maduro de esta capa por un orden de magnitud |
| **MathTutorBench** | https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | 42 | Capacidades pedagógicas *abiertas* de un tutor LLM en matemática: 3 habilidades docentes de alto nivel y 7 tareas concretas, con reward models entrenados para medir calidad de enseñanza y leaderboard publicado. **EMNLP 2025 (Oral)** |
| **ArguLens** | https://github.com/wwrwbs/AI_AWE | Apache-2.0 ✅ | 2 | **Scoring automático de ensayo argumentativo + feedback *label-aware***, descompuesto en tres piezas auditables: clasificador de *discourse moves* (Qwen2.5-7B con LoRA), scorer LightGBM sobre 31 features lingüísticas y generador de feedback (Qwen2.5-14B). UI Gradio con scoring por lote y desglose descargable. Respaldo: arXiv 2608.17356. ⚠️ **2 ★ y 2 commits — grado investigación, no producción**; su valor es la arquitectura separada scorer/feedback, no el repo |
| **UnifyingAITutorEvaluation** | https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | 32 | Taxonomía de 8 dimensiones pedagógicas para respuestas de tutor ante el error de un alumno. Publica **MRBench** en tres versiones: V1 (192 diálogos × 8 dim.), V2 (200 × 8), V3 (300 × 4). **NAACL 2025, Senior Area Chair Award** |
| **EduBench** | https://github.com/ybai-nlp/EduBench | MIT ✅ | 29 | **El primer benchmark pedagógico de esta KB que no es de matemática y no tiene fricción de licencia.** 9 contextos educativos y 4.000+ situaciones, evaluadas en 12 dimensiones agrupadas en adaptabilidad al escenario, exactitud factual/razonamiento y aplicación pedagógica. Cinco escenarios de alumno (QA, corrección de error, provisión de ideas, apoyo personalizado, apoyo emocional) y **cuatro de docente**, entre ellos generación de preguntas y **Automatic Grading**. Publica modelo (`DirectionAI/EDU-Qwen2.5-7B`) y dataset. **ACL 2026**. *Agregado en el pase 5* |
| **SafeTutors** | https://github.com/RadiantCrystal/SafeTutors | MIT ✅ | 0 | **Seguridad pedagógica**, categoría nueva: no mide si el tutor acierta, mide si enseña mal siendo amable. Taxonomía de **11 dimensiones de daño y 48 sub-riesgos** derivada de ciencias del aprendizaje, sobre **5.955 instancias** (3.135 single-turn + 2.820 diálogos multi-turn) en matemática, física y química. 11 modelos evaluados (10 open-weight, 1 cerrado), de 3.8B a 72B. **EMNLP 2026**. *Agregado en el pase 5* |
| **EduGuardBench** | https://github.com/YL1N/EduGuardBench | ⚠️ **sin licencia declarada** | 4 | Daño docente y seguridad adversaria del LLM *como docente simulado* — transversal a materia. Dos datasets: preguntas *Select All That Apply* para diagnosticar déficits de enseñanza, y prompts adversarios con jailbreak basado en personas centrados en **mala conducta académica**. 14 modelos. Reporta un *Educational Transformation Effect* (los modelos más seguros convierten el pedido dañino en momento de enseñanza) y que el modo de falla dominante es la **incompetencia**, no la toxicidad. ⚠️ Sin LICENSE no es reutilizable. *Agregado en el pase 5* |
| **L2-Bench** 🔴 | arXiv 2607.08842 · dataset en HuggingFace bajo `OUP/` · sitio `benchmarks.elt.edu.oup.com` | **código MIT ✅ / dataset y rúbricas CC BY-SA 4.0** ⚠️ | n/d | **Cierra el sub-gap de *lengua*: es el primer benchmark pedagógico de esta KB para enseñanza de segunda lengua.** De **Oxford University Press** con la Universidad de Oxford. Según las fuentes: **1.000+ tareas docentes auténticas**, marco de **12 competencias con 31 sub-habilidades**, rúbricas con descriptores expertos y validación de **200+ educadores de 45+ países**. Paper metodológico compañero: arXiv 2603.20088. 🔴 **NO VERIFICADO DE PRIMERA MANO** — el proxy de egreso de la sesión bloquea `arxiv.org`, `huggingface.co` y `oup.com`, que son los tres lugares donde vive. Licencia y contenido vienen de resultados de búsqueda. **Abrirlo y confirmar antes de cualquier entregable.** *Agregado en el pase 6* |
| **ProHist-Bench** (en `ABench`) | https://github.com/inclusionAI/ABench | **Apache-2.0** ✅ | 30 *(de ABench)* | **Investigación histórica, NO enseñanza de la historia** — y la distinción es el punto. **400 preguntas** núcleo en 4 tipos de tarea con **10.891 rúbricas redactadas por historiadores** sobre **9 dimensiones de capacidad** (versión extendida: 504 preguntas), sobre materiales del **examen imperial chino**. Vive dentro de `ABench`, suite multi-dominio con seis datasets (Física 500 problemas, Actuaría, Lógica, Psicología, Derecho y éste). Paper: arXiv 2604.24690. **No cierra el sub-gap de ciencias sociales**, que es pedagógico: esto mide si el modelo *sabe hacer* historia, no si *sabe enseñarla*. Sí aporta la pieza más cara de construir —10.891 rúbricas de expertos, Apache-2.0— como **capa de exactitud factual** debajo de una capa pedagógica que hay que traer aparte. ⚠️ Procedencia: `inclusionAI` es la organización open source de **Ant Group** (verificado en el perfil: `inclusion-ai.org`, 68 repos) → **APAC/China**, lo que extiende el gap 4. *Agregado en el pase 7* |
| AITutor-EvalKit | https://github.com/kaushal0494/AITutor-EvalKit | MIT ✅ | 3 | Implementación LoMTL (LoRA multi-task) sobre las 4 dimensiones del subconjunto MRBench. Demo en EACL 2026 (Rabat). Origen: MBZUAI, Abu Dhabi → EMEA |
| AI-Teaching-Agent | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT ✅ | 0 | Convierte fuentes en Markdown en artefactos **Lab, Exam y Grading** como DSL validado, más slides opcionales. Human review obligatorio, evaluación sandboxeada, servidor **MCP stdio**, y previews de examen "candidate-safe" que excluyen respuestas y referencias internas de corrección. *Agregado en la tercera pasada* |

### Seguridad pedagógica — la categoría que el pase 5 agregó

El pase 4 dejó escrito que el sub-gap pendiente era **"un benchmark pedagógico fuera de matemática"**. Se cae: `EduBench` es transversal a materia por diseño (organiza por *escenario educativo*, no por dominio) y `EduGuardBench` evalúa al modelo como docente simulado, lo que es independiente de la materia. Hay además dos benchmarks descritos en papers sin repo localizable — **EduFrameTrap** (arXiv 2605.14604, TUM/MCML, seis materias incluyendo economía y biología, con los subtipos de sycophancy CS-SYC / AUTH-SYC / FACE-SYC / DIR-SYC) y **ELBench** (arXiv 2608.09548, cuatro módulos bajo protocolo común).

**Lo que hace vendible a esta categoría** es que nombra un riesgo que el cliente reconoce y que los benchmarks de exactitud no capturan: el tutor que revela la respuesta antes de tiempo, que le da la razón al alumno porque el alumno insistió, o que abandona el andamiaje. En un cliente regulado eso no es una métrica de calidad, es el expediente de conformidad.

**El dato de arquitectura, de ELBench:** entre los modelos evaluados, el módulo de *safety* aparece **anti-correlacionado con el de enseñanza práctica** — los más seguros enseñan peor. Si se sostiene, no hay un modelo que resuelva las dos cosas y hay que componer: modelo docente + gate de seguridad medido aparte. Ver el patrón **P11**.

⚠️ **Lo que sigue faltando:** benchmark pedagógico de **lengua, ciencias sociales o formación profesional**. Ninguno de los cinco los cubre.

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

## Capa MCP de mastery — cinco reinvenciones del mismo patrón (pase 5)

El pase 4 cerró el gap 5 diciendo: *"El hueco exacto es `pyKT` detrás de MCP, y no existe."* Buscando por la pieza técnica aparecen **cinco servidores MCP independientes** que exponen estado de mastery a un agente. Ninguno tiene tracción y **ninguno usa una librería de knowledge tracing entrenable** — todos implementan su propia heurística.

| Repo | Licencia | Stars | Commits | Qué implementa |
|------|----------|-------|---------|----------------|
| https://github.com/zcsabbagh/knowledge-graph-mcp | MIT ✅ | 1 | 8 | FastMCP + SQLite. Grafo de conceptos con prerequisitos, **SM-2** para repaso, mastery multidimensional con fórmula fija `0.3×recall + 0.4×application + 0.3×explanation`, detección de misconceptions |
| https://github.com/woodstocksoftware/student-progress-tracker | MIT ✅ | 1 | 9 | Perfiles, inscripciones, resultados de evaluación, mastery por tema, detección de learning gaps, recomendación de foco. Telemetría a nivel de pregunta |
| https://github.com/tejpalvirk/student | MIT ✅ | 1 | 6 | Grafo de conocimiento académico (cursos, trabajos, exámenes, conceptos) con persistencia entre sesiones |
| https://github.com/znecho9/knowledge-forest-mcp | Apache-2.0 ✅ | 0 | 3 | Árboles de prerequisitos + **mastery con evidencia obligatoria**: exige desempeño novedoso, sin asistencia y a libro cerrado antes de declarar dominio |
| https://github.com/radhepa/Teacher-MCP | MIT ✅ | 0 | 2 | MCP-first con memoria SQLite persistente, personas docentes y andamiaje en tres niveles. Incluye un Claude Skill que corre solo o contra el server |
| https://github.com/ankimcp/anki-mcp-server | **MIT** ✅ | **499** | 254 | Puente MCP hacia **Anki**, el SRS de facto: crear, leer y revisar mazos en lenguaje natural. TypeScript, v0.22.0, en beta declarada. **No es un servidor de mastery: es el único de esta capa con tracción real** |

> **Agregado en el pase 12 del 2026-10-01 — el techo de esta capa no era 1 ★, y la diferencia es de qué lado está el estándar.** Las cinco reinvenciones de mastery no pasan de 1 ★; `anki-mcp-server` tiene **499 ★ y 254 commits**. La diferencia no es calidad de código: es que los cinco **inventan** su modelo de dominio (grafo propio, SM-2 propio, esquema propio) mientras Anki **ya es el estándar instalado** de repetición espaciada y el MCP sólo lo expone. Leído junto con `py-fsrs` (MIT, en la tabla principal, que es el algoritmo moderno que reemplaza a SM-2), la lectura para un studio se invierte: **no construir el motor de mastery, conectarse al que el alumno ya usa.** Ver el patrón **P28**.

**Cómo leerlo.** Cinco autores sin relación llegaron al mismo patrón en la misma ventana: eso es **validación de mercado**, no ruido. Y el hueco de ingeniería queda mejor documentado que antes: los tres más grandes suman **3 estrellas y 23 commits**, y se verificó de primera mano en este pase que **`pyKT` sigue sin mencionar MCP ni interfaz de serving** (441 ★, 811 commits).

El gap 5 pasa entonces de *"nadie lo intentó"* a **"cinco lo intentaron y ninguno conectó la librería buena"**. Con `pyBKT` (MIT, 281 ★, publicado) en la mesa, hacerlo bien es integración, no investigación. Ver **P12**.

### Lo que el pase 6 le agrega a esta sección: los cinco reinventaron dos cosas, no una

El diagnóstico del pase 5 fue que ninguno de los cinco servidores MCP de mastery usa una librería de knowledge tracing entrenable. Es cierto, y está incompleto. **Los cinco también inventaron su propio almacén de eventos de aprendizaje**, cuando existe un estándar IEEE con cuatro implementaciones maduras (ver la capa LRS/xAPI en `repos/foundations.md`).

`learnmcp-xapi` —agregado a la tabla principal en este pase— es el primero que no comete ese segundo error: no guarda el progreso en un esquema propio, lo escribe como statements xAPI en un LRS conforme. Sigue **sin** estimar mastery, así que no reemplaza a ninguno de los cinco en lo que a ellos les falta; pero resuelve la mitad que los cinco resolvieron mal.

**Para una propuesta, la lectura es:** el componente a construir es un estimador (`pyBKT` o `pyKT`) detrás de un LRS que ya existe, expuesto por un MCP que ya existe. No es una plataforma. Ver **P15** en `compose/patterns.md`.

## Advertencias de licencia

**Actualizado en el pase 4:** la tabla principal ya **no** es "todo MIT o Apache-2.0". Al agregar agentes nuevos entraron dos AGPL y dos Creative Commons, y eso cambia qué se puede empaquetar en un entregable cerrado.

| Licencia | Repos | Qué implica para un entregable de cliente |
|----------|-------|-------------------------------------------|
| MIT / Apache-2.0 / BSD-3 ✅ | DeepTutor, OpenMAIC, Project NOMAD, py-fsrs, Educhain, pyKT, **pyBKT**, Bloom, OATutor, OpenTutor, OpenTutorAI-CE, Claw-ED, **Aila**, tutor-mcp, gradescope-mcp, TutorIA, **EduBench**, **SafeTutors**, y los 5 servidores MCP de mastery | Sin fricción. Construible y redistribuible cerrado |
| **AGPL-3.0** ⚠️ | **FreeLingo**, **mentar**, **ChatTutor**, y **`Honcho`** (la dependencia de memoria de `tutor-gpt`) | Copyleft **de red**: si se modifica y se sirve por SaaS, hay obligación de publicar el fuente modificado. No forkear para un producto cerrado; usar como referencia de arquitectura o desplegar sin modificar |
| **CC BY-SA 4.0** ⚠️ | **education-agent-skills**, **OpenDidactia**, **UnifyingAITutorEvaluation** | Contenido con *share-alike*: los derivados heredan la obligación. Usable como referencia pedagógica o para medir internamente; **revisar con legal antes de empaquetarlo en un entregable cerrado** |
| **CC BY 4.0** | **MathTutorBench** | Sólo atribución, sin share-alike. El más limpio de los no-código |
| **GPL-3.0** ⚠️ | **tutor-gpt** *(pase 7)* | Copyleft fuerte, pero **no de red**: a diferencia de AGPL, servirlo por SaaS sin modificarlo no dispara la obligación. Modificarlo y **distribuir el binario o el código** sí. Para un entregable cerrado, no; como referencia de arquitectura de teoría de la mente, sí |
| **GPL-2.0** ⚠️ | **TAO** (`oat-sa/tao-core`) *(pase 9)* | Copyleft fuerte, sin cláusula de red. La plataforma de evaluación QTI más madura que encontró esta KB (22.533 commits) **no se puede forkear para un producto cerrado**. Se despliega tal cual y la inteligencia va al lado — la misma receta que Moodle y Open edX |
| **LGPLv3 / LGPL-3.0** ⚠️ | **openbadgeslib** (librería), **caliper-php-public** (U. de Michigan) *(pase 9)* | Copyleft **débil**: enlazar desde un producto cerrado es admisible si el usuario puede reemplazar la librería; **modificarla y distribuirla, no**. Muerde justo donde uno querría tocar, porque los perfiles de badge son específicos de cada cliente. ⚠️ `openbadgeslib` tiene **licencia partida**: LGPLv3 la librería, BSD-2-Clause el CLI |
| **EUPL-1.2** ⚠️ | **european-digital-credentials**, **European-Learning-Model** *(pase 9)* | Licencia pública de la Unión Europea, copyleft con cláusula de compatibilidad. Los dos repos están **archivados** (feb-2024) y el código vivo se mudó a `code.europa.eu`, que **esta sesión no puede alcanzar** (ver gap 14). No cotizar sobre lo archivado |
| **Sin licencia declarada** 🚫 | **EduGuardBench**, **OmniEdu** (`haolpku/Omni-Edu`), **awesome-ai-llm4education**, y **llamatutor** *(pase 7, el caso más caro: 2.1k ★)* | *Agregado en el pase 5, ampliado en el pase 7.* Sin archivo LICENSE el default legal es **todos los derechos reservados**, por mucho que el título diga "open". **Los cuatro** se pueden leer y citar; **ninguno se puede empaquetar**. Se verificó que `/blob/main/LICENSE` devuelve **404** tanto en `awesome-ai-llm4education` (pase 5) como en `llamatutor` (pase 7) |
| **Licencia de investigación custom** 🚫 | **llmgrader** (`sdrangan/llmgrader`) | *Agregado en el pase 5.* "PySilicon Research License", © 2026 Sundeep Rangan — **leída en el archivo**. No es OSI. Es el grading agéntico más maduro que encontró esta KB (240 commits, en producción en NYU, con MCP e integración a Gradescope) y **no se puede usar en un entregable**. Ver `repos/trending.md`, pase 5 |

**La trampa concreta:** `FreeLingo` aparece como MIT en artículos de prensa y agregadores. **La página del repo dice AGPL-3.0.** Se verificó en el pase 4 y se registra acá porque es el modo de falla típico — citar la licencia del listicle en vez de la del repo.

**La trampa del pase 7, que es la inversa y más cara:** `llamatutor` tiene **2.1k estrellas** y **ningún archivo de licencia**. Se verificó pidiendo `/blob/main/LICENSE` y devuelve **404**. Un repo popular, con README cuidado y demo desplegada, se lee como open source y legalmente **no lo es**: sin LICENSE el default es todos los derechos reservados. **Las estrellas no son una licencia**, y es el único indicador que un listicle reporta.

**Y la advertencia que este pase agrega sobre toda la tabla:** las tres entradas nuevas son 🚫 / AGPL-3.0 / GPL-3.0. Al día de hoy, **las únicas bases de tutor open source permisivas y de escala siguen siendo las dos de APAC** — `DeepTutor` (Apache-2.0, 40.6k ★) y `OpenMAIC` (MIT, 39.7k ★). Eso ya no es una suposición por falta de búsqueda: está medido contra las alternativas.

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

## Capa de accesibilidad y educación especial — agregada en el pase 8 del 2026-10-01

Siete pasadas construyeron el stack por capas —agente, modelado, evaluación, seguridad, telemetría, datos— y **ninguna miró al alumno con discapacidad**. Es el hueco de cobertura más grande que tenía esta KB, y no es un nicho: en la UE la accesibilidad de una plataforma de aprendizaje dejó de ser una característica y pasó a ser **condición de acceso al mercado** (European Accessibility Act, en vigor desde el **2025-06-28**). Ver el **trend 18**.

**El hallazgo no es un repo, es la forma del segmento.** Se parte limpio en dos mitades y ninguna sirve sola:

### Mitad 1 — la tecnología asistiva madura, y es toda copyleft

| Repo | Licencia | Stars | Lenguaje | Qué es |
|------|----------|-------|----------|--------|
| https://github.com/OptiKey/OptiKey | **GPL-3.0** ⚠️ | **4.4k** | C# | Teclado en pantalla y control total de Windows **con la mirada**, para ELA / enfermedad de motoneurona. Es la pieza de tecnología asistiva más adoptada que encontró esta KB en cualquier capa |
| https://github.com/cboard-org/cboard | **GPL-3.0** ⚠️ | **759** | JavaScript | Sistema **AAC** (comunicación aumentativa y alternativa) con texto-a-voz, PWA, para parálisis cerebral y autismo. 5.531 commits. © Assistive Technology LLC; respaldado por la iniciativa **«For every child, a voice» de UNICEF** |

⚠️ **Las dos son GPL-3.0, y eso decide la arquitectura entera de un engagement de accesibilidad.** No se forkean para meterles un agente adentro. Se despliegan tal cual y la inteligencia propia va al lado — exactamente la misma receta que esta KB ya aplica a Moodle y Open edX.

### Mitad 2 — lo agéntico y permisivo, y no pasa de 15 estrellas

| Repo | Licencia | Stars | Commits | Qué implementa | Origen |
|------|----------|-------|---------|----------------|--------|
| https://github.com/AyushBinjola1/Swar-Setu | **MIT** ✅ | 15 | 4 | Detección temprana y apoyo multilingüe de **dislexia, disgrafia y discalculia**: evaluaciones interactivas, soporte por voz, dashboards por rol (padre / docente) | APAC (India — *«Built with ❤️ for India»*) |
| https://github.com/open-behavior-analysis/aba-clinical-agent | **AGPL-3.0** ⚠️ | 7 | 7 | **29 Claude Code Skills** + base Obsidian para supervisión clínica **ABA** de punta a punta (de-identificación, intake, análisis funcional de conducta, plan de tratamiento, supervisión de staff, reporte de hitos). Es la mejor ilustración del **trend 9** — la pedagogía empaquetada como skills — fuera del aula ordinaria | Sin región declarada (© Jiamei Zhang, BCBA) |
| https://github.com/ronda-ai/Ronda-App | **GPL-3.0** ⚠️ | 3 | 17 | Asistente pedagógico generativo para aula inclusiva: participación, coaching docente, gestión de seguridad. **Soberanía de datos por diseño** (self-hosting + cifrado en reposo). Anclado al **Marco para la Buena Enseñanza (MBE)** chileno | LATAM (Chile) |
| https://github.com/Noggin-Labs/noggimigo | **MIT** ✅ | 1 | 19 | Motor de tutoría **socrática local** para necesidades educativas especiales, con diagnóstico de misconceptions y seguimiento de latencia de respuesta — la latencia como señal de carga cognitiva es un diseño que no aparece en ningún otro repo de la KB | Sin región declarada (Noggin Labs) |
| https://github.com/100205ivan/EyeEP | 🚫 **sin licencia** | 1 | 12 | Gestión de **IEP** (programa educativo individualizado) asistida por AI para docentes de educación especial. Sin LICENSE no es reutilizable | APAC (Taiwán — *inferido del README en chino tradicional, no declarado*) |
| https://github.com/SabioTechTeam/Teacher-Hub | **MIT** ⚠️ *(ver advertencia)* | 0 | 156 | Proyecto **«UnStuck»**: sistema adaptativo de matemática K-6 con test adaptativo computarizado (CAT), modelo vivo del alumno, verificación determinística de dominio y **parsing de acomodaciones IEP / 504** | Sin región declarada |
| https://github.com/Autism-Technology-Research-Syndicate/SEALApplication | **GPL-3.0** ⚠️ | 10 | 321 | Currículo de educación especial personalizado para autismo analizando respuesta del alumno con visión por computadora. 🚫 **El repo está marcado como deprecado** | North America (AUTRS, EE. UU.) |
| https://github.com/classifiedstudentkabir/Sign-Language-Interpreter | 🚫 **sin licencia** | 60 | 8 | *SignLens* — reconocimiento de **lengua de señas** a texto en el navegador con MediaPipe. Es el repo con más estrellas del topic `inclusive-education` y **no tiene licencia**: el default legal es todos los derechos reservados | Sin región declarada (hackathon HackNova) |

⚠️ **Trampa de licencia verificada en `Teacher-Hub`, y vale como advertencia general.** El README dice literalmente *«MIT License — free for educational and non-commercial use»*. **Las dos mitades de esa frase se contradicen:** la MIT permite uso comercial sin restricción. No se sabe si el autor quiso MIT o quiso una no-comercial, y esa ambigüedad **es** el riesgo. Antes de cualquier entregable hay que leer el archivo `LICENSE` y, si sigue sin cerrar, pedirle al autor que lo aclare por escrito. Anotado porque es la segunda vez que esta KB encuentra una declaración de licencia que el texto no sostiene (la primera fue OpenTutorAI-CE, donde el pipeline reportó Apache-2.0 y era BSD-3).

### La pieza transversal, y es la única con tracción y licencia limpia

| Repo | Licencia | Stars | Commits | Qué implementa |
|------|----------|-------|---------|----------------|
| https://github.com/Community-Access/accessibility-agents | **MIT** ✅ | **419** | 374 | Agentes de revisión de accesibilidad que **corren dentro del harness de codificación**: Claude Code, GitHub Copilot, Claude Desktop, Codex, Gemini CLI. Seis skills de entrada que rutean a especialistas sobre ARIA, teclado, foco, formularios, contraste, modales, live regions, encabezados, tablas, carga cognitiva, i18n, móvil, email y visualización de datos. Cubre también documentos (Word, Excel, PowerPoint, PDF, ePub) y add-ons de NVDA. **Propósito declarado: que las herramientas de AI dejen de generar código inaccesible** |
| https://github.com/sololabstr/uisight | **MIT** ✅ | 128 | n/d | Medición de contraste, área táctil y *theme drift* en sesiones en vivo, expuesta como **servidor MCP** |
| https://github.com/weAAAre/a11y-agents-kit | **MIT** ✅ | 34 | n/d | Kit de skills de accesibilidad para harnesses de codificación con AI, de **weAAAre** (escuela de accesibilidad digital) |

**Por qué `accessibility-agents` es el hallazgo comercial del pase 8 y no los tutores.** Es MIT, tiene 419 ★ y 374 commits — más tracción que **cualquier** pieza de educación especial de este pase y que la mayoría de la capa de evaluación — y ataca la obligación que **ya está vigente** (EAA, WCAG 2.2 AA) en vez de la que está prohibida (redacción de IEP, ver abajo). **No es un repo educativo**, y por eso ninguna búsqueda de los siete pases anteriores lo iba a encontrar. Ver el patrón **P17**.

### El dato que da vuelta la lectura comercial del segmento en North America

El open source de educación especial que apareció en este pase apunta mayoritariamente a **redactar o gestionar el IEP** (`EyeEP`, el parsing de IEP/504 de `Teacher-Hub`). Y esa es, específicamente, **la tarea que las jurisdicciones de EE. UU. están prohibiendo**: la guía de **Delaware** prohíbe usar AI para objetivos de IEP, evaluación docente y calificación subjetiva, y el marco de **Nueva York** prohíbe usar AI para el desarrollo de planes **IEP o 504**.

**La oferta open source está apuntando al único paso del flujo que no se puede automatizar.** Lo vendible es el resto del flujo — preparar material, diferenciar contenido, adaptar lectura, documentar evidencia — con el docente como autor de la decisión. El diseño de referencia para eso ya está en esta KB y es **`tero`**: *el agente propone, el docente decide*, sin escritura de archivos sin aprobación humana. Ver el patrón **P18** y el **gap 12**.

## Capa de credenciales verificables e interoperabilidad — agregada en el pase 9 del 2026-10-01

Ocho pasadas construyeron el stack del alumno —agente, modelado, evaluación, seguridad, telemetría, datos, accesibilidad— y **ninguna miró qué pasa cuando el aprendizaje termina y hay que acreditarlo.** Es la capa de la *credencial*: quién emite el certificado, con qué formato, cómo se verifica sin llamar a la institución emisora, y cómo viajan la matrícula y el ítem de examen entre sistemas.

Existe, es un estándar con certificación de conformidad, y **esta KB nunca la buscó porque no se llama «agente» ni «tutor»** — se llama Open Badges 3.0, W3C Verifiable Credentials, QTI, OneRoster y Caliper. Es la cuarta vez que se aplica la regla del pase 6: *cuando falta una capa, preguntarse si tiene un nombre que uno no está usando.*

**El hallazgo del pase no son los repos nuevos: es que las implementaciones de referencia de estos estándares se están apagando mientras los estándares siguen siendo obligatorios.** Ver el **trend 19** y el **gap 14**.

### Lo que está vivo, verificado y es permisivo

| Nombre | Repo | Licencia | Stars | Commits | Lenguaje | Descripción | Origen (región) |
|--------|------|----------|-------|---------|----------|-------------|-----------------|
| learner-credential-wallet | https://github.com/digitalcredentials/learner-credential-wallet | **MIT** ✅ | 88 | 1.309 | TypeScript | Billetera móvil (React Native + Expo) para que el **alumno** reciba, guarde y presente credenciales verificables de formación y empleo. Implementa la *Learner Credential Wallet specification* del Digital Credentials Consortium sobre W3C VC. v2.2.10 (junio 2026). **Es la pieza de esta capa con más commits y la única pensada desde el lado del alumno y no del emisor.** ⚠️ Ver el cambio de gobernanza abajo | **North America (EE. UU.)** — el consorcio declara sede en el **MIT**; contacto `lcw-support@mit.edu`, financiamiento inicial del **U.S. Department of Education** |
| verifier-plus | https://github.com/digitalcredentials/verifier-plus | **MIT** ✅ | 18 | 395 | TypeScript | App Next.js que **verifica y muestra** credenciales verificables, con almacenamiento y links públicos compartibles. Acepta la credencial por copiar/pegar, subida de archivo, URL o **QR**. Es el lado «¿esto es auténtico?» del circuito, que es el que pregunta el empleador | North America (EE. UU., Digital Credentials Commons) |
| issuer-coordinator | https://github.com/digitalcredentials/issuer-coordinator | **MIT** ✅ | 12 | 55 | JavaScript | App Express que **emite** credenciales verificables firmadas criptográficamente y después las puede **revocar o suspender**. Orquesta un servicio de firma y un servicio de estado vía Docker Compose. Implementa **W3C VC API** (endpoints de emisión y de actualización de estado) y soporta el formato **Open Badges 3.0** por integración de contexto. v1.0.0 | North America (EE. UU., Digital Credentials Commons) |
| qti3-item-player | https://github.com/amp-up-io/qti3-item-player | **MIT** ✅ | 30 | 596 | JavaScript (Vue 2.6) | Reproductor de ítems de evaluación **QTI 3**: carga QTI XML, maneja la sesión del ítem, procesa respuestas y ejecuta el *response processing* con scoring completo, ítems adaptativos y *template processing*. **Tiene certificación de conformidad QTI 3 Basic y QTI 3 Advanced «Delivery» de 1EdTech** — es el único artefacto de toda esta KB con certificación de conformidad de un organismo de estándares. Licencia leída en el archivo: `Copyright (c) 2022-2024 Amp-up.io, LLC` | Sin región declarada (Amp-up.io, LLC) |
| esco-skill-extractor | https://github.com/KonstantinosPetrakis/esco-skill-extractor | **MIT** ✅ | 32 | 29 | Python | Extrae **competencias y ocupaciones** de texto libre (avisos de trabajo, CV, descripciones de curso) y las mapea a la taxonomía europea **ESCO** y a ocupaciones **ISCO**, con *sentence transformers* y similitud cosena. **Es la única pieza que encontró esta KB que traduce lenguaje natural a un vocabulario de competencias normalizado** — el paso que convierte «el alumno terminó el módulo» en «el alumno acredita esta competencia». ⚠️ No declara versión de ESCO | Sin región declarada (autor Konstantinos Petrakis) |
| oneroster (TypeScript) | https://github.com/LongsightGroup/oneroster | **MIT** ✅ | 0 | 33 | TypeScript | Parsea, valida y escribe **paquetes CSV de OneRoster** y habla la **REST API** en las versiones **1.1 y 1.2**. Corre en Node, Deno y navegador; incluye cliente REST de lectura de roster y de notas del *gradebook*, y un *provider router* neutral al framework para construir servicios OneRoster. Declara validación contra las especificaciones oficiales y las suites de certificación. **0 ★: referencia de integración, no dependencia de producción** | Sin región declarada (Longsight Group) |
| lti-1-3-php-library | https://github.com/1EdTech/lti-1-3-php-library | **Apache-2.0** ✅ | 124 | 110 | PHP | Librería oficial de 1EdTech para construir *tool providers* **LTI 1.3**: flujo de login OIDC, validación de mensajes, respuestas de *deep linking* e integración con los servicios de la plataforma (envío de notas, lectura del roster de miembros). **Es la pieza de esta capa con más estrellas que sigue pública y permisiva**, y es la que hace que un agente se pueda montar dentro de cualquier LMS conforme | Global (1EdTech, `1edtech.org`) |
| openbadges-specification | https://github.com/1EdTech/openbadges-specification | ⚠️ **no declarada en la página** | 205 | 2.266 | HTML | La **especificación** de Open Badges, no una implementación: versiones **3.0, 2.1 y 2.0** en directorios separados (`ob_v3p0`, `ob_v2p1`, `ob_v2p0`), más **Comprehensive Learner Record (CLR) 2.0**. Ramas `main` (estable) y `develop`. Es el documento normativo al que hay que programar; **para el código hay que ir a terceros**, que es exactamente el problema de esta capa | Global (1EdTech) |

### Lo maduro y lo copyleft — la misma forma que el pase 8 encontró en accesibilidad

| Repo | Licencia | Stars | Commits | Lenguaje | Qué es |
|------|----------|-------|---------|----------|--------|
| https://github.com/oat-sa/tao-core | **GPL-2.0** ⚠️ | 64 | **22.533** | PHP | Extensión fundacional de **TAO**, plataforma de evaluación basada en QTI y LTI: integración por webhooks, control de acceso por roles, *feature flags*, colas de tareas, middleware y manejo de CSRF. **22.533 commits** — es, por volumen de trabajo acumulado, la pieza más madura de toda esta KB en cualquier capa. Creada en la **Universidad de Luxemburgo**, mantenida por Open Assessment Technologies. ⚠️ **GPL-2.0: no se forkea para un producto cerrado.** Se despliega tal cual y la inteligencia va al lado |
| https://github.com/luisgf/openbadgeslib | **LGPLv3** (librería) **/ BSD-2-Clause** (CLI) ⚠️ | 1 | 404 | Python | Librería y CLI para el ciclo completo de **emisor Open Badges 3.0**: emite W3C VC como **JWT-VC** o Data Integrity (LDP), las *hornea* dentro de SVG/PNG, las verifica, y **revoca o suspende** con **W3C Bitstring Status Lists** y `did:web`. Claves RSA-2048 (RS256), ECC P-256 (ES256) y Ed25519 (EdDSA). Soporta además OB 2.0 estricto y OB 1.0 legacy. v4.0.0 del **2026-07-22**. Autores: Luis González Fernández y Jesús Cea Avión. **404 commits y 1 estrella: el código más completo de emisión OB 3.0 que encontró esta KB, y nadie lo usa** |
| https://github.com/tl-its-umich-edu/caliper-php-public | **LGPL-3.0** ⚠️ | 3 | 365 | PHP | Fork de la **Universidad de Michigan** del cliente PHP de **Caliper Analytics** (la API de sensores de telemetría de 1EdTech), con `Options::setHttpHeaders()` agregado para uso propio. **Es hoy la implementación PHP de Caliper que sigue accesible** — ver abajo por qué |

⚠️ **`openbadgeslib` tiene licencia partida y hay que leerla antes de cotizar.** La **librería es LGPLv3** y las **herramientas CLI son BSD-2-Clause**. Enlazar la librería desde un producto cerrado es admisible bajo LGPL si se respeta la posibilidad de reemplazarla; **modificarla** y distribuirla, no. La distinción importa porque es la pieza que uno querría tocar (los perfiles de badge son específicos de cada cliente). Ninguna fuente secundaria que describe este proyecto menciona su licencia.

### 🔴 El hallazgo del pase: tres implementaciones de referencia que ya no están

Esto es lo que vale de esta pasada, y no es un repo nuevo. Los estándares de esta capa siguen vigentes y obligatorios; **su código de referencia se está retirando.**

| Qué era | URL canónica que todavía citan los listicles | Estado verificado 2026-10-01 |
|---|---|---|
| **Badgr** — la implementación de referencia de Open Badges que cita toda la documentación del sector | `https://github.com/concentricsky/badgr-server` | 🔴 **404.** Y la búsqueda de repositorios de la organización `concentricsky` con el término `badgr` devuelve literalmente **«No repositories matched your search»**. La organización hoy **verifica el dominio `instructure.com`** (Eugene, Oregón). Badgr pasó a ser **Canvas Credentials** de Instructure y después se plegó en **Parchment Digital Badges** |
| **caliper-php** — cliente PHP oficial de Caliper Analytics | `https://github.com/1EdTech/caliper-php` | 🔴 **404.** El fork de la Universidad de Michigan declara el motivo en su propio banner, **citado textual**: *«This had been archived, but has been unarchived following 1EdTech making its caliper-php private.»* Es decir: **el propio organismo de estándares puso en privado su implementación de referencia**, y una universidad tuvo que desarchivar su fork para no quedarse sin cliente |
| **caliper-python** — implementación de referencia de la Sensor API en Python | `https://github.com/IMSGlobal/caliper-python` | 🔴 **404** |

**Cómo leerlo con rigor.** Un 404 en GitHub no distingue entre *borrado*, *renombrado* y *puesto en privado*: desde afuera son indistinguibles. Lo que está verificado de primera mano es que **las tres URL canónicas no resuelven** y que, en el caso de `caliper-php`, **el mantenedor del fork nombra la causa** (1EdTech lo hizo privado). Para `badgr-server` hay además una segunda señal independiente: la búsqueda dentro de la organización no devuelve nada.

**Por qué importa comercialmente, y es más que una molestia de ingeniería.** La obligación de interoperar no desapareció con el código: un cliente que compra «credenciales digitales» o «analítica de aprendizaje conforme» sigue necesitando OB 3.0, Caliper o QTI. Lo que cambió es **de dónde sale el código**: ya no del organismo ni del vendor de referencia, sino de **terceros certificados** (`qti3-item-player`, MIT, con certificación de conformidad), **consorcios universitarios** (`digitalcredentials/*`, MIT) y **forks de universidad** (`caliper-php-public`, LGPL-3.0). Eso es a la vez el riesgo y la oportunidad: el riesgo es construir sobre una URL que mañana no está; la oportunidad es que **el integrador que sabe cuál de estas piezas sigue viva vale más que el que sabe el estándar.** Ver el patrón **P21**.

### El cambio de gobernanza de la billetera, que hay que saber antes de proponerla

`learner-credential-wallet` es MIT, tiene 1.309 commits y es la pieza más trabajada de esta capa — y **acaba de cambiar de manos.** La página del repo declara, sobre la v2.2.10 de junio de 2026, que *es el último release como Digital Credentials Consortium at MIT*, y que el proyecto pasa a alojarse bajo **OpenWallet Foundation Labs**.

Hay una segunda señal del mismo movimiento: la organización de GitHub ya no se presenta como «Digital Credentials Consortium» sino como **Digital Credentials Commons** (`dccommons.org`, EE. UU., **124 repositorios públicos**).

**Qué significa para una propuesta.** No es un abandono — un traspaso a una fundación neutral es, en general, señal de madurez y de continuidad (es lo mismo que esta KB registró para `goose` al pasar a la Linux Foundation). Pero **sí significa que la cadena de custodia cambió en los últimos cuatro meses**, y que la documentación, los issues y la hoja de ruta van a mudar de lugar. Al proponer esta pieza hay que **fijar la versión y confirmar dónde vive el mantenimiento activo**, no citar el repo del MIT como si nada hubiera pasado.

### Lo que esta capa **no** tiene, y es el gap que abre el pase 9

Se buscó explícitamente un agente que **emita o consuma** credenciales verificables, y no existe. Ninguno de los 25+ agentes de la tabla principal escribe un Open Badge, y ninguna de las piezas de credenciales tiene interfaz de agente ni servidor MCP.

**El stack del alumno y el stack de la credencial no se tocan en ningún punto** — y la pieza que los conectaría es justamente la que ya está documentada en esta KB desde el pase 6: el Learning Record Store. El LRS registra la evidencia (xAPI), el estimador de mastery decide si hay dominio (`pyBKT`/`pyKT`, gap 5), y **nadie convierte esa decisión en una credencial verificable**, que es el artefacto que el alumno puede llevarse y el empleador puede verificar. Ver el **gap 13** y el patrón **P19**.

## Capa de contenido curricular — agregada en el pase 10 del 2026-10-01

Nueve pasadas preguntaron *qué hace el agente* y nunca *de qué lee*. Esta sección es la respuesta, y el hallazgo no es un
repo: es que **la licencia del contenido no es la licencia del código, y en esta capa casi nunca coincide**.

### 🔴 El hallazgo del pase: dos fuentes de primera mano que se contradicen, y las dos están en la KB

| Fuente verificada | Qué dice, textual | Dónde vive la afirmación |
|---|---|---|
| `openstax/osbooks-calculus-bundle` | *«Calculus Volume 1, Calculus Volume 2, and Calculus Volume 3 are available under the Creative Commons Attribution-NonCommercial-ShareAlike License»* | archivo **`LICENSE`** |
| `openstax/osbooks-biology-bundle` | *«Creative Commons Attribution-NonCommercial-ShareAlike License»* (Biology 2e, Concepts of Biology, Biology for AP®) | archivo **`LICENSE`** |
| `openstax/osbooks-college-physics-bundle` | *«College Physics 2e and College Physics for AP® Courses 2e are available under the Creative Commons Attribution-NonCommercial-ShareAlike License»* | archivo **`LICENSE`** |
| `CAHLR/OATutor` | *«All content in this repository is made available under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. Attribution is given within each json file, indicating the authoring organization and license for each hint, scaffold, and problem»* | **README** |
| `pythpythpython/openstax-mcp-server` | el contenido servido está *«licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)»* | **README** |

**Las tres primeras filas son `LICENSE`; las dos últimas son README.** Y OATutor declara curar problemas de
**Calculus Volume 1**, que es exactamente uno de los títulos cuyo `LICENSE` dice **NonCommercial-ShareAlike**.

**Lo que este pase afirma, y nada más:** las cinco citas están verificadas de primera mano, y **no son compatibles entre
sí para material derivado** — ShareAlike obliga a licenciar la derivación igual, y NonCommercial prohíbe exactamente el uso
que tiene un entregable facturado. Lo que este pase **no** afirma es cuál de las dos es la correcta. `openstax.org`, donde
vive el catálogo con la licencia por título, está **bloqueado por el proxy de egreso de esta sesión** (ver el gap 17), así
que la discrepancia se registra sin resolver.

### La regla operativa, y es barata de aplicar

El propio README de OATutor dice dónde está la respuesta: **la licencia está declarada por ítem, dentro de cada JSON**
(*«indicating the authoring organization and license for each hint, scaffold, and problem»*). Entonces:

1. **No usar la licencia declarada a nivel de repo** para contenido. Ni la del README, ni la del badge.
2. **Leer el campo de licencia del ítem** que se va a ingestar, y guardarlo junto al ítem. Ese manifiesto es el entregable
   (ver **P22**).
3. **Un corpus mezclado es del color del ítem más restrictivo**, no del promedio.

⚠️ **Esto pega directamente sobre el patrón P1 de esta KB**, que recomienda *«la lógica de BKT de OATutor + su contenido
curado de OpenStax en JSON»*. **El código MIT de OATutor no está en discusión; el contenido sí.** P1 queda corregido en
`compose/patterns.md`.

### Los dos corpus grandes con licencia apta para uso comercial

| Corpus | Licencia | Estado de verificación | Por qué importa |
|---|---|---|---|
| **Oak National Academy** (currículo completo, Reino Unido) | **Open Government Licence v3.0** — permite uso comercial explícitamente | ⚠️ **parcial**: `support.thenational.academy` está **bloqueado por el proxy**. La licencia y el permiso comercial vienen de prensa educativa británica (*Schools Week*), no del documento de licencia | **Es el único caso de esta KB donde el código y el contenido son los dos utilizables**: `Aila` es MIT y ya está en la tabla principal desde el pase 5, y el currículo que Aila sirve es OGL. ⚠️ Hay indicios de **restricción geográfica al Reino Unido** en la cobertura de prensa: verificar antes de proponerlo fuera de UK |
| **OpenStax** (40+ títulos) | 🔴 **en disputa** — ver el cuadro de arriba | ⚠️ verificado en GitHub (**NC-SA** en 3 de 3), no verificado en el catálogo oficial | Es el corpus que todo el mundo asume CC BY. **Asumirlo es el riesgo.** |

### Lo que esta capa no tiene, y es el gap que abre el pase 10

Un puente agente↔contenido con tracción. Hay **uno** (`openstax-mcp-server`, 1 ★, 7 commits) y **declara mal la licencia
de lo que sirve**. El segundo candidato, `moarshy/mcp-tutor` (**0 ★**, 26 commits, 🚫 **sin licencia** — el repo sólo dice
*«This project is experimental and intended for educational and research purposes»*), convierte **repositorios de
documentación** en cursos con DSPy y los expone por MCP: es un tutor de documentación técnica, no de currículo escolar.
Ver el **gap 15**.

---

---
*Verificado manualmente vía WebFetch, no por el pipeline automático. Última verificación: 2026-10-01 (pase 10).*
*Nota de método del pase 5: `curl -sI` contra github.com devuelve **403** a través del proxy de egreso, así que toda verificación se hizo con WebFetch contra la página del repo. Están bloqueados `arxiv.org`, `openreview.net`, `aclanthology.org`, `huggingface.co` y `ojs.aaai.org`, por lo que **los venues, conteos de ítems y hallazgos de los papers no pudieron verificarse en la fuente primaria** — sólo lo alojado en github.com está verificado de primera mano.*

## Capa predictiva / early warning — agregada en el pase 11 del 2026-10-01

Diez pasadas preguntaron qué hace el agente, de qué lee, dónde escribe, cómo se lo mide y cómo se acredita al alumno.
Ninguna preguntó por la capa que **decide sobre el alumno**: el scoring de riesgo de abandono, el *early alert*, el
*student success* que toda universidad compra. Es la capa con más presupuesto asignado del sector y la más regulada
—el Anexo III del EU AI Act la nombra literalmente— y es **la peor abastecida de open source de toda esta KB.**

### 🔴 El hallazgo del pase, y es una medición, no una impresión

Dos consultas acotan la oferta entera:

| Consulta (GitHub, 2026-10-01) | Resultados | Máximo de estrellas |
|---|---|---|
| `topic:learning-analytics stars:>50` | **2 repos en todo GitHub** | 169 ★ — y es `AkihikoWatanabe/paper_notes`, un blog de notas de papers, no un sistema |
| `dropout prediction student license:mit pushed:>2026-01-01` | **110 repos** | **6 ★** |

Es decir: **el único repo real con más de 50 estrellas en el topic de learning analytics es `OpenLRW`** (62 ★, ver
`repos/foundations.md`), que es un almacén de datos, no un predictor. Y la capa predictiva propiamente dicha son
110 repos MIT activos en 2026 cuyo techo es **6 estrellas**.

### El repo que está arriba de esos 110, y por qué el dato importa

| Repo | Licencia | Stars | Qué es, y la advertencia |
|---|---|---|---|
| https://github.com/Aliipou/Student-Retention-Prediction | MIT ✅ | 6 | El tope de la capa. Predice riesgo de abandono con señales de engagement disponibles **a la semana 4** (logins al LMS, asistencia, entrega de trabajos), con **SHAP** para que el tutor entienda por qué se marcó a un alumno. Declara 137 tests y 100% de cobertura. 22 commits, actividad hasta 2026-09-15. ⚠️ **Y entrena con datos sintéticos generados por el propio repo** (`python -m src.train_pipeline`): no hay dataset real detrás, y no hay auditoría de fairness. Como *andamio de ingeniería* sirve; como modelo, no predice nada todavía |
| https://github.com/dssg/student-early-warning | ⚠️ **"Other" (NOASSERTION)** | 70 | El más estrellado de la capa en términos absolutos, de **Data Science for Social Good** (Universidad de Chicago): early warning de abandono en secundaria, en R. **Último push 2018-08-22.** Sin licencia SPDX reconocible, así que legal no lo va a aprobar sin revisión manual. Valor real: su *metodología* y su feature engineering, no su código |
| https://github.com/novatrix-2030/SIH-2026 | 🚫 **sin licencia** | 0 | "DropGuard": plataforma de early warning explicable para instituciones de la India. Stack serio —Next.js 14 / React 19, FastAPI, LightGBM + XGBoost, **SHAP**, Groq con Llama-3.3-70B, Postgres, Docker—. Es una entrega del **Smart India Hackathon 2026** (PS Code `SIH-2026-13-002`, categoría *Smart Education*), 17 commits. 🚫 Sin licencia. **Es el patrón del gap 2 (LATAM) repetido en APAC:** buen problema, buen diseño, cero continuidad |

### Lo que sí es utilizable de esta capa, y no son predictores

| Repo | Licencia | Stars | Para qué sirve en un engagement |
|---|---|---|---|
| https://github.com/terracotta-education/terracotta | **Apache-2.0** ✅ | 21 | Plug-in de LMS para correr **ensayos controlados aleatorizados dentro del aula**: diferencia el contenido de una tarea en variantes de tratamiento, asigna alumnos al azar, y trae consentimiento informado oculto al docente, filtrado de no-consintientes en los reportes y eliminación de identificadores en las exportaciones. 2.572 commits, actividad al 2026-09-30. **Es la única pieza permisiva de esta KB que permite demostrar que una intervención funcionó** en vez de afirmarlo — y la privacidad ya viene resuelta, que es la mitad cara de un comité de ética |
| https://github.com/GoogleCloudPlatform/aira | **Apache-2.0** ✅ | 24 | Evaluación automática de **fluidez lectora**: clasifica al alumno en Pre-reader / Reader / Advanced y puntúa la performance, sobre la plataforma AI de Google Cloud. Escrito por *Education Engineers* de Google Cloud. ⚠️ **Y hay que leer su propia advertencia antes de proponerlo:** el repo declara que es "an experiment (proof-of-concept only)", **no un producto soportado de Google**, que no se usen datos personales ni sensibles, y que **no debe usarlo un menor de 13 años** — en una herramienta cuyo caso de uso es la alfabetización inicial. Como referencia de arquitectura es buena; como base de un entregable con alumnos reales, no |

### La corrección de encuadre que este pase le hace a la KB

La KB viene sosteniendo, desde el pase 7, que el cuello de botella del modelado del alumno **es el dato**: los
datasets de knowledge tracing son NonCommercial (gap 11). **En esta capa es exactamente al revés, y conviene no
exportar la conclusión de una capa a la otra.** Ver `repos/foundations.md`, capa de datos de deserción: los dos
corpus canónicos de predicción de abandono son **CC BY 4.0**, con uso comercial permitido. Acá no falta el dato:
**falta el software, y falta quien lo mantenga.**

## Capa de distribución por *skills* de agente — agregada en el pase 12 del 2026-10-01

Las pasadas 7 y 8 anotaron dos veces, al pasar, que había pedagogía distribuida **como skill de agente** en vez de
como producto (`education-agent-skills` primero, `Bloom` en modo CLI después), y las dos veces lo trataron como la
anécdota de un repo. **Este pase la trata como una capa y la mide.** El resultado es un número, no una impresión.

### 🔴 El hallazgo del pase: la vertical científica construyó en este canal una biblioteca de 47.2k ★ con MIT; la educativa tiene 815 ★ y es *share-alike*

Mismo estándar (**Agent Skills**), mismos harnesses (Claude Code, Codex, Cursor, Antigravity, Gemini CLI), misma
mecánica de distribución —un repo de Markdown, sin backend, sin despliegue, sin dependencias que auditar—. Verificado
de primera mano contra la página de cada repo el 2026-10-01:

| Biblioteca | Vertical | Licencia | Stars | Contenido |
|---|---|---|---|---|
| https://github.com/K-Dense-AI/scientific-agent-skills | Ciencia | **MIT** ✅ | **47.2k** | 181 skills + 100+ bases de datos científicas + 70+ workflows de paquetes Python. Declara 160.000+ científicos usuarios |
| https://github.com/virgiliojr94/book-to-skill | Genérico (libro → skill) | **MIT** ✅ | **33.2k** | Convierte PDF/EPUB/DOCX en skill estructurada con carga por capítulo y cheatsheet |
| https://github.com/GarethManning/education-agent-skills | **Educación** | **CC BY-SA 4.0** ⚠️ | **815** | 165 skills pedagógicas evidence-grounded en 20 dominios |
| https://github.com/ZeKaiNie/universal-examprep-skill | **Educación** | **MIT** ✅ | **299** | Tutor de examen que enseña desde las diapositivas de la cátedra, con cita de página |

**Los dos números del pase son 58× y 158×.** La biblioteca de skills de la vertical científica tiene **58 veces** las
estrellas de la educativa, y **158 veces** las del mejor artefacto educativo con licencia permisiva. No es que el
canal no funcione para educación: es que **la educación no lo ocupó.**

**Y el techo educativo es justamente el que no se puede empaquetar.** `education-agent-skills` —815 ★, 165 skills, el
activo más grande de esta capa— es **CC BY-SA 4.0**: *share-alike*, los derivados heredan la obligación. Esta KB ya lo
tenía marcado en «Advertencias de licencia», pero no había registrado la consecuencia estructural: **el mejor activo
de la capa de distribución más barata de la industria es el que no entra en un entregable cerrado**, y el mejor
permisivo es un orden de magnitud más chico.

### Los paquetes educativos verificados, y seis de los siete son nuevos en esta KB

Todos verificados vía WebFetch contra la página del repo el 2026-10-01 (licencia, stars y descripción leídas de
primera mano):

| Nombre | Repo | Licencia | Stars | Lenguaje | Qué hace | Origen (región) |
|---|---|---|---|---|---|---|
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 ⚠️ | 815 | Markdown/YAML | 165 skills pedagógicas en 20 dominios. El dominio 20 es *student-facing*, el resto apunta a docentes y diseñadores | EMEA (autor UK) — *ya estaba en la KB* |
| human-skill-tree | https://github.com/24kchengYe/human-skill-tree | **AGPL-3.0** ⚠️ | 562 | TypeScript | 33 skills de K-12 a carrera e inteligencia social, sobre ciencia cognitiva. Híbrido: skills **+** app web (aula multi-agente, repetición espaciada). v2.0 del 2026-03-18 | APAC |
| universal-examprep-skill | https://github.com/ZeKaiNie/universal-examprep-skill | **MIT** ✅ | 299 | Markdown | Enseña desde las diapositivas de la cátedra **citando página**, recorta figuras, evalúa con la práctica real y mantiene memoria entre sesiones. Optimizado para modelos chicos y baratos | Global (bilingüe EN/zh; material de MIT 6.006 y Yale PSYC 110) |
| algo-sensei | https://github.com/karanb192/algo-sensei | **MIT** ✅ | 281 | Markdown | Mentor de algoritmos y DSA: pistas progresivas y reconocimiento de patrones en vez de la solución. Mock interviews, code review, 5 lenguajes | Global |
| universal-diagnostic-tutor-skill | https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill | **MIT** ✅ | 234 | Markdown | Tutor *diagnosis-first* para STEM y CS: decide el próximo paso útil, verifica comprensión y construye dominio. Sin menú de modos ni comandos | Global |
| kaogong-skill | https://github.com/KeWang0622/kaogong-skill | **MIT** ✅ | 147 | Markdown | Tutor para el **examen de servicio civil chino**: aptitud, redacción, entrevista, actualidad. Declara compatibilidad con 40+ clientes de agente | APAC (China) |
| agent-skills (Learning Commons) | https://github.com/learning-commons-org/agent-skills | **Apache-2.0** ✅ | 35 | — | Skills para que un asistente produzca material docente **alineado a estándares K-12**. Cada skill empaqueta instrucciones, referencias y *guardrails* de un workflow docente | North America (foco estándares K-12 de EE. UU.) |

**Cinco de los siete son MIT o Apache-2.0 y suman 996 ★.** Son empaquetables. El problema no es la licencia del
conjunto: es que **el único que tiene cobertura curricular ancha (165 skills) es el que tiene *share-alike*.**

### La forma del segmento, y repite el patrón de los pases 8 y 9 con el signo invertido

Los pases 8 (accesibilidad) y 9 (credenciales) encontraron la misma figura: *lo maduro es copyleft, lo permisivo es
diminuto*. Esta capa la repite —`education-agent-skills` (815 ★, CC BY-SA) y `human-skill-tree` (562 ★, AGPL-3.0)
arriba; MIT abajo—, **pero con una diferencia que la vuelve la capa más accionable de la KB:** acá el costo de
construir el activo permisivo que falta no es una plataforma ni un dataset. Es **Markdown**. La biblioteca científica
de 47.2k ★ es texto estructurado, y su estructura es pública y MIT: se puede copiar la arquitectura sin copiar el
contenido.

### La nota de método del pase, y hay que dejarla escrita porque va a volver a pasar

Dos advertencias de verificación, las dos verificadas contra la fuente:

1. **Los agregadores de estrellas van atrasados, y en esta categoría el atraso es de ~2×.** Para los dos repos
   baseline, la búsqueda web devolvió cifras de terceros (ossinsight, sourcepulse) de **26.5k** y **13.7k**, mientras
   la página del repo —leída el mismo día— dice **47.2k** y **33.2k**. En una categoría que crece a +6.3k ★/mes,
   **la cifra del agregador no es una cifra vieja: es una cifra equivocada.** Regla: en esta capa, sólo vale la página
   del repo.
2. **`curl` no sirve para verificar URLs en este entorno, y un 403 no es un 404.** Se corrieron las **164 URLs de
   GitHub de toda esta KB** por `curl -sL`: **las 164 devolvieron 403**, uniformemente — es el proxy del entorno
   bloqueando `curl` hacia github.com, no *link rot*. **No hay ninguna evidencia de que esas 164 URLs estén caídas, y
   tampoco se las revalidó en este pase.** La verificación de primera mano en esta KB se hace con **WebFetch**, que
   sí resuelve. Un pase futuro que vea 403 masivos no debe interpretarlos como enlaces muertos.

### Lo que esta capa no tiene, y es el gap que abre el pase 12

**No hay una sola skill educativa con *eval* publicada.** Los siete paquetes son texto de prompt sin versionado
semántico, sin suite de regresión y sin medición de efecto pedagógico. La capa de evaluación que esta KB mapeó en el
pase 4 (MathTutorBench, UnifyingAITutorEvaluation, EduBench, EduGuardBench) **nunca se aplicó a una skill**: evalúa
tutores con backend. Es decir: la capa más barata de distribuir es también la única sin control de calidad, y las
herramientas para medirla ya existen en esta misma KB y no están conectadas. Ver el patrón **P27**.
