---
industry: education
region: Global
updated: 2026-10-01
---

# 🏗️ Repos fundacionales — education

> Bases sobre las cuales construir. Verificado repo por repo vía WebFetch el 2026-09-30 (capas del pase 10, el 2026-10-01).
> Leer la columna **Licencia** antes de proponer: media KB de educación es GPL/AGPL, no permisiva.
> **Pase 11 del 2026-10-01:** aparece una licencia que las diez pasadas anteriores filtraban sin saberlo — **ECL-2.0**, con la que licencia todo Apereo (Sakai, Opencast, OpenLRW). Es Apache-2.0 con el alcance de patentes acotado, aprobada por OSI y FSF, y **es apta para construir arriba**. Ver la capa de analítica institucional, abajo.

## Plataformas y frameworks base

**14 repos reales verificados.** GegoK12 se agregó en la tercera pasada del 2026-09-30; **pyKT en la cuarta**.
> **Pase 5 del 2026-09-30:** esta tabla no cambió. Lo nuevo entró en dos capas propias más abajo — **modelos fundacionales educativos** (que la KB no tenía) y tres artefactos más en la **capa de medición**.

| Repo | URL | Licencia | Stars | Lenguaje | ¿Base para AI? | Origen |
|------|-----|----------|-------|----------|----------------|--------|
| Open edX platform | https://github.com/openedx/openedx-platform | AGPL-3.0 ⚠️ | 8.2k | Python | Sí — LMS + Studio de escala; extender vía XBlock en vez de tocar el core. **Repo renombrado de `edx-platform` a `openedx-platform`** | North America (MIT + Harvard origin) |
| Moodle | https://github.com/moodle/moodle | GPL-3.0 ⚠️ | 7.4k | PHP | **Sí, la mejor apuesta** — AI subsystem nativo con provider plugins (OpenAI, Azure, Ollama, DeepSeek, Gemini, Bedrock). No hay que inventar la capa de integración | APAC (Moodle HQ, Australia) |
| Oppia | https://github.com/oppia/oppia | Apache-2.0 ✅ | 6.8k | Python | Sí — licencia permisiva + modelo de "explorations" interactivas, buen fit para contenido generado por agente | North America (origen Google) |
| Canvas LMS | https://github.com/instructure/canvas-lms | AGPL-3.0 ⚠️ | 6.8k | Ruby | Sí — dominante en higher-ed de EE. UU.; integrar vía LTI/API antes que forkear | North America (Instructure) |
| Frappe LMS | https://github.com/frappe/lms | AGPL-3.0 ⚠️ | 3.3k | Python | Sí — liviano, sobre el framework Frappe (mismo stack que ERPNext) | APAC (Frappe, India) |
| GegoK12 | https://github.com/Gego-K12/gegok12 | MIT ✅ | 54 | PHP | **Sí, y es el único permisivo del lado administrativo** — school management / ERP con API-first y **sistema de plugins**, así que el agente puede vivir adentro sin contaminar IP. Activo: último commit 2026-09-23. ⚠️ Open-core: exámenes y fees son módulos Pro pagos (ver `verticals/solutions.md`) | APAC (GegoSoft Technologies, Madurai, India) |
| Kolibri | https://github.com/learningequality/kolibri | MIT ✅ | 1.1k | Python | **Sí** — offline-first sin requerir internet. Licencia permisiva. La base para mercados de baja conectividad | North America (Learning Equality) |
| Chamilo | https://github.com/chamilo/chamilo-lms | GPL-3.0 ⚠️ | 1.0k | PHP | Sí — el más liviano de self-hostear; fuerte en LATAM y EMEA hispanohablante/francófona | EMEA (Bélgica/España) |
| py-fsrs | https://github.com/open-spaced-repetition/py-fsrs | MIT ✅ | 499 | Python | Sí — scheduler de repetición espaciada (modelo DSR, 21 parámetros). Convierte un chatbot en un sistema que *retiene* | Global |
| pyKT | https://github.com/pykt-team/pykt-toolkit | MIT ✅ | 441 | Python | **Sí — y es la pieza que falta.** Toolkit de *knowledge tracing* profundo: 10+ modelos DLKT sobre 7+ datasets con preprocesamiento estandarizado y 5 escenarios de predicción. Donde `py-fsrs` programa *cuándo* repasar, pyKT modela *qué sabe* el alumno. 811 commits | APAC (Jinan University / Guangdong Institute of Smart Education, China) |
| XBlock | https://github.com/openedx/XBlock | Apache-2.0 ✅ | 470 | Python | **Sí** — el punto de extensión *permisivo* de Open edX. Tu componente AI vive acá, aislado del core AGPL | North America |
| OpenOLAT | https://github.com/OpenOLAT/OpenOLAT | Apache-2.0 ✅ | 444 | Java | Sí — LMS con licencia permisiva, evaluación y assessment sólidos. Referencia para el mercado DACH | EMEA (Suiza) |
| Richie | https://github.com/openfun/richie | MIT ✅ | 316 | Python | Sí — CMS para portales educativos (catálogo de cursos), complementa un LMS en vez de reemplazarlo | EMEA (OpenFUN, Francia) |
| H5P core | https://github.com/h5p/h5p-php-library | GPL-3.0 ⚠️ | 150 | PHP | Parcial — contenido interactivo embebible en Moodle/edX/Canvas. Útil como *target de salida* para un agente autor | EMEA (Noruega) |

## Repos de alfabetización AI (upskilling)

No son plataformas educativas, son el material con el que se forma gente en AI. Relevantes para engagements de *capability building*, que en educación corporativa es la mitad de la demanda.

6 repos, todos MIT o Apache-2.0. Cubren las tres capas de una formación seria, y conviene elegir por capa y no por estrellas (el sexto, agregado en el pase 11, cubre las tres a la vez):

- **entender el modelo** → `LLMs-from-scratch`, `minimind`
- **construir con agentes** → `ai-engineering-from-scratch` (currículum secuenciado), `learn-claude-code` (harness)
- **operar en producción** → `tiny-llm` (serving, donde se va el costo real)

| Repo | URL | Licencia | Stars | Uso |
|------|-----|----------|-------|-----|
| LLMs-from-scratch | https://github.com/rasbt/LLMs-from-scratch | Apache-2.0 ✅ | 105.8k | Implementar un LLM tipo ChatGPT en PyTorch paso a paso. El recurso de referencia para entender transformers |
| minimind | https://github.com/jingyaogong/minimind | Apache-2.0 ✅ | 63k | Entrenar un LLM de 64M parámetros desde cero en ~2h en hardware de consumo: pretraining + SFT + RL completos |
| ai-engineering-from-scratch | https://github.com/rohitg00/ai-engineering-from-scratch | MIT ✅ | 62.1k | **523 lecciones en 20 fases**, de fundamentos matemáticos a agent engineering. Exige implementar a mano antes de usar frameworks; cada lección deja un artefacto reusable (prompts, skills, agents, MCP servers). Lo más cercano a un programa de capability building listo para usar |
| learn-claude-code | https://github.com/shareAI-lab/learn-claude-code | MIT ✅ | 77.8k | Tutorial de 17 capítulos sobre cómo se construye un *harness* de agente: tools, gestión de conocimiento, sistema de tareas, coordinación de equipos. Material de referencia de facto del tema |
| tiny-llm | https://github.com/skyzh/tiny-llm | Apache-2.0 ✅ | 4.7k | Curso de **serving** e inferencia: KV cache, continuous batching, flash attention, paged attention. Construye una vLLM en miniatura sobre Qwen3. ⚠️ Usa **MLX (macOS ARM64)** — obliga a hardware Apple como material de aula |
| ai-builders-curriculum | https://github.com/ai-builders-foundation/ai-builders-curriculum | MIT ✅ | 1.4k | **Currículum vendor-neutral de AI full-stack**, de la **AI Builders Foundation (501(c)(3))**: 6 módulos (Data & Storage, Auth & Users, Functions & APIs, AI & Agents, Deploy, Transparent AI) y **3 starter kits ejecutables** (`ai-app-starter`, `rag-starter`, `glassbox`) en Node.js + SQLite sin framework. Creado el 2026-07-05 y ya en 1.4k ★. **Es el único de esta tabla pensado como programa de formación de una organización sin ánimo de lucro en vez de como libro de un autor** — y la neutralidad de proveedor es declarada y verificable en los starter kits. *Agregado en el pase 11* |

## Capa de medición — agregada en el pase 4 del 2026-09-30

Las tres pasadas anteriores listaron plataformas (dónde corre el curso) y agentes (quién habla con el alumno), pero ningún repo que respondiera **"¿esto está funcionando?"**. Es la capa que un cliente regulado pide primero y la que la KB no tenía.

| Repo | URL | Licencia | Stars | Qué mide |
|------|-----|----------|-------|----------|
| **pyKT** | https://github.com/pykt-team/pykt-toolkit | MIT ✅ | 441 | Estado de conocimiento del alumno (knowledge tracing profundo). El modelo cuantitativo de mastery |
| **MathTutorBench** | https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | 42 | Calidad **pedagógica** de un tutor LLM: 3 habilidades docentes, 7 tareas, reward models, leaderboard. EMNLP 2025 Oral |
| **UnifyingAITutorEvaluation** | https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | 32 | Taxonomía de 8 dimensiones sobre la respuesta del tutor al error del alumno + dataset MRBench (V1 192 / V2 200 / V3 300 diálogos). NAACL 2025 |
| **py-fsrs** | https://github.com/open-spaced-repetition/py-fsrs | MIT ✅ | 499 | Retención en el tiempo (scheduling de repaso, modelo DSR) |
| **pyBKT** | https://github.com/CAHLR/pyBKT | MIT ✅ | 281 | *(pase 5)* Mastery cognitivo por **Bayesian Knowledge Tracing** clásico, con parámetros individualizados por alumno y por ítem. EDM 2021. La alternativa **interpretable y de procedencia estadounidense** a pyKT |
| **EduBench** | https://github.com/ybai-nlp/EduBench | MIT ✅ | 29 | *(pase 5)* Calidad pedagógica **transversal a materia**: 9 contextos educativos, 4.000+ situaciones, 12 dimensiones. Incluye 4 escenarios docentes, entre ellos Automatic Grading. ACL 2026. **El único de esta capa que es MIT y no es de matemática** |
| **SafeTutors** | https://github.com/RadiantCrystal/SafeTutors | MIT ✅ | 0 | *(pase 5)* **Seguridad pedagógica**: 11 dimensiones de daño y 48 sub-riesgos sobre 5.955 instancias (matemática, física, química). EMNLP 2026 |
| **rubric** | https://github.com/paper-instruments/rubric | MIT ✅ | 75 | *(pase 5)* Motor genérico de **rúbricas ponderadas** para LLM-as-judge: criterio por criterio, single-pass u holístico, validación Pydantic. No es educativo — es la plomería permisiva sobre la que construir la capa de juicio |

**Cómo se usan juntas, que es el punto:** `pyKT` o `pyBKT` estiman qué domina el alumno, `py-fsrs` decide cuándo volver a preguntárselo, y `MathTutorBench` / `MRBench` / `EduBench` miden si la forma en que el agente responde es pedagógicamente buena y no sólo correcta. Las tres preguntas son distintas y hasta el pase 4 la KB sólo tenía la segunda. Ver el patrón **P10** en `compose/patterns.md`.

**Lo que agrega el pase 5 a esta capa son dos preguntas más, y las dos se venden solas en un cliente regulado:**

- **"¿enseña mal siendo amable?"** → `SafeTutors` (11 dimensiones de daño, 48 sub-riesgos). Mide revelación prematura de la respuesta, refuerzo de la idea equivocada del alumno y abandono del andamiaje. Ninguno de los benchmarks anteriores captura esto, y es el modo de falla que un docente reconoce al instante.
- **"¿esto funciona fuera de matemática?"** → `EduBench`. Los tres artefactos del pase 4 eran todos de matemática; este organiza por *escenario educativo* y cubre también los escenarios del docente.

**Y un cambio de licencia que importa:** el pase 4 tuvo que advertir que dos de sus cuatro piezas de medición eran Creative Commons con fricción (CC BY-SA en `UnifyingAITutorEvaluation`). `EduBench`, `SafeTutors`, `pyBKT` y `rubric` son **todas MIT**. Por primera vez se puede armar un stack de evaluación pedagógica completo sin pasar por legal.

⚠️ **Dos de las cuatro no son licencias de código.** MathTutorBench es CC BY 4.0 (sólo atribución) y UnifyingAITutorEvaluation es CC BY-SA 4.0 (*share-alike*: un benchmark derivado con datos del cliente hereda la obligación). Es justo el uso más probable en un engagement, así que revisarlo con legal antes de prometerlo.

## Capa de modelos fundacionales educativos — agregada en el pase 5 del 2026-09-30

Capa que la KB no tenía en ninguna de las cuatro pasadas anteriores. Tenía plataformas (dónde corre el curso), agentes (quién habla con el alumno), modelado (qué sabe el alumno) y medición (si funciona), pero **ningún modelo entrenado específicamente para educación**.

| Repo | URL | Licencia | Stars | Qué es |
|------|-----|----------|-------|--------|
| **OmniEdu** | https://github.com/haolpku/Omni-Edu | 🚫 **sin licencia declarada** | 48 | Familia de modelos fundacionales para K-12 en **tres tamaños: 4B, 9B y 27B**, sobre bases Qwen3.5/Qwen3.8. Corpus de instrucciones **público**: 69.999 ejemplos y 15,96M tokens supervisados de 100+ fuentes (60.951 educativos + 9.048 generales), organizado en cuatro capacidades — competencia en la materia, anclaje curricular, razonamiento diagnóstico y acción pedagógica/andamiaje. Origen: Universidad de Pekín + UCAS + Zhongguancun Academy |

**El dato que vale de OmniEdu** es de argumentación, no de despliegue: según el paper, **OmniEdu-27B alcanza 78,74% en el setting Scaffold de MathTutorBench** — el mismo benchmark que esta KB lista arriba. Es decir: un modelo de 27B especializado compite en tareas pedagógicas con modelos genéricos mucho más grandes. Para un ministerio o un distrito que mira el costo por alumno de inferencia, **ese es el argumento más fuerte que produjo el sector en 2026**, y se puede hacer sin depender de OmniEdu: la receta (corpus, capacidades, evaluación) está descrita.

🚫 **No desplegable, y por dos razones independientes:**

1. **El repo no declara licencia.** Sin LICENSE, el default es todos los derechos reservados. "Open Foundation Models" en el título describe que los pesos se descargan, no que se puedan usar comercialmente.
2. **Los pesos heredan la licencia del modelo base.** Están construidos sobre bases Qwen, cuyos términos varían entre tamaños y no son todos Apache-2.0. Aunque el repo adoptara MIT mañana, eso no levanta la restricción heredada.

**Tratarlo como evidencia y como receta, no como componente.** Y anotar que refuerza el **gap 4**: la concentración de la oferta en APAC ya no es sólo de agentes (DeepTutor, OpenMAIC) y de modelado (pyKT), ahora también de modelos fundacionales.

## Capa de telemetría de aprendizaje (LRS / xAPI) — agregada en el pase 6 del 2026-10-01

Segunda capa que la KB no tenía, y la más estructural de las dos. Las pasadas 1–5 cubrieron plataforma, agente, modelado del alumno, medición y modelo fundacional — y nunca registraron **dónde se escriben los eventos de aprendizaje** que alimentan todo lo demás. Esa capa está estandarizada desde hace más de una década: **xAPI**, hoy **IEEE 9274.1.1**, y su implementación se llama **Learning Record Store (LRS)**.

Un LRS guarda *statements* con forma `actor – verbo – objeto` ("María intentó el ejercicio 4 y falló"). Es el sustrato que consume cualquier modelo de knowledge tracing y la única forma estándar de que el agente de tutoría, el LMS y el SIS compartan una misma historia del alumno.

| Repo | URL | Licencia | Stars | Commits | Lenguaje | Rol |
|------|-----|----------|-------|---------|----------|-----|
| **SQL LRS (`lrsql`)** | https://github.com/yetanalytics/lrsql | **Apache-2.0** ✅ | 143 | 2.268 | Clojure | **El default de producción permisivo.** Corre sobre bases de datos que cualquier cliente ya tiene: SQLite, PostgreSQL 14–18, MariaDB 10.6–11.8, MySQL 8.0–9.5. Copyright © 2021–2026 (Yet Analytics) |
| **Ralph** | https://github.com/openfun/ralph | **MIT** ✅ | 50 | 714 | Python | LRS + CLI de pipelines + librería. **Convierte tracking logs de Open edX a xAPI de fábrica.** FastAPI, Elasticsearch, Docker/K8s. De **OpenFun** (France Université Numérique), la misma organización que publica Richie |
| **ADL_LRS** | https://github.com/adlnet/ADL_LRS | **Apache-2.0** ✅ | 331 | 1.885 | Python | Implementación **de referencia** de ADL (EE. UU.), autor del estándar. Soporta **IEEE 9274.1.1 / xAPI 2.0**. ⚠️ El repo declara ser *proof of concept* "para pocos usuarios": sirve para validar conformidad, no para producción |
| **Learning Locker** | https://github.com/LearningLocker/learninglocker | **GPL-3.0** ⚠️ | 583 | 3.254 | JavaScript | El LRS más adoptado de la categoría, desde 2014 (Learning Pool). **Es el único copyleft de los cuatro**, y justamente el que más instalaciones tiene |
| **learnmcp-xapi** | https://github.com/DavidLMS/learnmcp-xapi | **MIT** ✅ | 15 | 32 | Python | **El puente hacia los agentes.** Servidor MCP con tres tools sobre un LRS: registrar statement, consultar progreso, gestionar vocabulario de verbos. Backends: `lrsql`, Ralph, Veracity. Autor: docente del IES Rafael Alberti (España) |

**Cómo elegir, en una línea:** producción permisiva → **`lrsql`**; cliente sobre Open edX → **Ralph**; certificar conformidad con el estándar → **ADL_LRS**; el cliente ya tiene uno instalado → casi seguro es **Learning Locker**, y entonces hay que leer la GPL antes de tocarlo.

**Por qué esta capa cambia el gap 5 y no sólo agrega repos.** El pase 5 encontró cinco servidores MCP de mastery, todos con heurística propia, y concluyó que faltaba conectar `pyKT`/`pyBKT`. Faltaba eso **y** algo anterior: los cinco también inventaron su propio almacén de eventos. Con esta capa registrada, el trabajo pendiente queda acotado a una sola pieza — **el estimador de mastery** — porque el almacén (`lrsql`, Apache-2.0) y el transporte MCP (`learnmcp-xapi`, MIT) ya existen y ya hablan entre sí. Ver el patrón **P15**.

⚠️ **Lo que ninguno de los cinco hace:** estimar mastery. Son almacenes conformes al estándar y un transporte. La inferencia —BKT, DLKT, lo que sea— es **siempre** trabajo propio. La separación es correcta de diseño, pero hay que decirla en la propuesta para no vender integración donde hay desarrollo.

## Capa de datos de entrenamiento (datasets de knowledge tracing) — agregada en el pase 7 del 2026-10-01

Tercera capa que la KB no tenía, y la que corrige el optimismo de las tres anteriores. Los pases 4 y 5 concluyeron que el modelado del alumno es "integración de una librería MIT madura" (`pyKT`, `pyBKT`). Es cierto **sobre el código** y es insuficiente: un modelo de knowledge tracing **no se instala, se entrena**. Y en la capa de datos las licencias se dan vuelta.

| Dataset | URL | Licencia | Volumen | Qué tiene de particular | Origen |
|---|---|---|---|---|---|
| **EdNet** | https://github.com/riiid/ednet | ⚠️ **CC BY-NC 4.0** | **131.441.538** interacciones · **784.309** alumnos (441,2 c/u) · 13.169 problemas · 1.021 clases · 293 tipos de skill | El más grande por dos órdenes de magnitud. Cuatro niveles jerárquicos: **KT1** pregunta-respuesta, **KT2** acciones (entrar/responder/enviar), **KT3** + explicaciones y clases, **KT4** lista completa con multimedia y eventos de pago. Datos reales de la app **Santa**, recolectados 2 años desde abril 2017 | **APAC (Corea del Sur)** — Riiid |
| **XES3G5M** | https://github.com/ai4ed/XES3G5M | **MIT** ✅ | **5.549.635** interacciones · **18.066** alumnos · **7.652** preguntas · **865** conceptos | **El único grande con licencia permisiva.** El más rico en información auxiliar: texto de las preguntas, relaciones entre componentes de conocimiento, tipos de pregunta y análisis de respuestas, con KC en rutas jerárquicas. ⚠️ **Sólo en chino**, sólo matemática, tercer grado | APAC (org `ai4ed`, 61 ★ — el repo **no declara institución ni país**) |
| **FoundationalASSIST** | arXiv 2602.00070 | ⚠️ **CC BY-NC 4.0** + **gated** | **1,7M** interacciones · **5.000** alumnos | **El único en inglés que combina texto de la pregunta + la respuesta real del alumno + qué distractor eligió**, alineado a **Common Core**. Currículo *Illustrative Mathematics*, 6.º–8.º grado. Define dos familias de tarea: **Knowledge Tracing** y **Pedagogical Grounding**. Para descargarlo hay que **aceptar *Responsible Use Guidelines* y entregar datos de contacto** | **North America** — Worden, C. Heffernan, N. Heffernan (linaje **ASSISTments**) y Sonkar |
| Junyi Academy | — | no verificada en este pase | ~16M interacciones | Tupla identificador + correcto/incorrecto, sin texto | APAC (Taiwán) |
| Eedi | — | no verificada en este pase | ~20M interacciones | Texto parcial de preguntas en inglés, **sin las respuestas reales** | EMEA (Reino Unido) |

**La inversión de licencias, que es el hallazgo:** en la capa de modelado todo es MIT (`pyKT`, `pyBKT`, `py-fsrs`). En la capa de datos, **de los tres grandes sólo uno es reutilizable comercialmente**, y es chino, de matemática y de tercer grado. `NC` significa NonCommercial, y un engagement de Globant es por definición comercial.

**Las tres rutas, en orden de preferencia para una propuesta:**

1. **Entrenar con los datos del cliente.** La única ruta limpia a escala. Su costo hay que presupuestarlo explícitamente: **arranque en frío** — sin histórico el modelo no sirve el primer día. Y acá la capa de telemetría deja de ser opcional: **un LRS xAPI desplegado en la fase 1 es lo que genera el dataset propio**. Sin eso el cold start no termina nunca.
2. **`XES3G5M` (MIT) para validar la arquitectura, no para servir al cliente.** Sirve para demostrar que el pipeline entrena, mide y responde. Que sea chino y de tercer grado es irrelevante para eso, y determinante si alguien lo confunde con el modelo de producción.
3. **`EdNet` / `FoundationalASSIST` sólo para investigación interna o un paper.** Nunca dentro de un entregable facturado.

⚠️ **Y esto extiende el gap 4 a una quinta capa, con un giro desfavorable.** La ruta alternativa que el pase 5 armó para clientes con restricción de procedencia (`pyBKT` + `Aila` + `MathTutorBench` + `SafeTutors`, todo occidental y permisivo) **se sostiene en código y se rompe en datos**: el único dataset permisivo es chino, y los dos no chinos que importan son NonCommercial. Para ese cliente, entrenar con datos propios deja de ser lo preferible y pasa a ser **lo único**. Ver **P16**.

## Capa de memoria de agente — agregada en el pase 7 del 2026-10-01

Distinta de la capa de telemetría de arriba, y conviene no confundirlas porque una sirve de evidencia ante un regulador y la otra no.

| Repo | URL | Licencia | Stars | Commits | Lenguaje | Rol | Origen |
|---|---|---|---|---|---|---|---|
| **Honcho** | https://github.com/plastic-labs/honcho | **AGPL-3.0** ⚠️ | **7.4k** | 760 | Python | Memoria para agentes con estado, **de propósito general** (no educativa). Enfoque *reasoning-first*: "extrae conclusiones de las conversaciones y los eventos, no sólo hace match de chunks". Modela a cada participante —humano o agente— como **peer de primera clase**. Es la dependencia de personalización de `tutor-gpt` | **North America (EE. UU.)** — Plastic Labs, `plasticlabs.ai` |

| | **xAPI / LRS** (pase 6) | **Honcho** (pase 7) |
|---|---|---|
| Qué guarda | **Hechos de aprendizaje** conformes a IEEE 9274.1.1: "practicó bucles", "aprobó el módulo 3" | **Conclusiones inferidas** sobre la persona: preferencias, creencias, estado mental |
| Para qué sirve | Expediente auditable, portabilidad entre sistemas, conformidad | Personalización y continuidad de la relación |
| Ante un regulador | **Es evidencia**: esquema estándar, verbos acordados, statements verificables | **No es evidencia**: son inferencias de un modelo sobre un alumno |
| Licencia | `lrsql` Apache-2.0, `Ralph` MIT ✅ | **AGPL-3.0** ⚠️ — copyleft de red |

**No son sustitutos, y un tutor serio quiere las dos.** La que va al expediente de conformidad es siempre la primera. Usar Honcho como capa de registro de aprendizaje sería exactamente el error que el pase 6 documentó en los cinco servidores MCP de mastery —inventar el almacén en vez de usar el estándar— y además con una licencia peor.

## Capa de accesibilidad y tecnología asistiva — agregada en el pase 8 del 2026-10-01

Tercera capa que la KB no tenía, y la única cuya demanda está **legalmente forzada con fecha cumplida**: el **European Accessibility Act** rige desde el **2025-06-28** y alcanza plataformas de e-learning y LMS, con **WCAG 2.1 AA** como referencia técnica (los agentes de abajo trabajan contra **WCAG 2.2 AA**, que es más exigente y por lo tanto cubre). Ver el **trend 18** y el patrón **P17**.

La capa tiene una asimetría que conviene tener presente al cotizar: **el producto asistivo maduro es copyleft y el tooling de conformidad es permisivo.** O sea que lo que se puede empaquetar es la *verificación*, no el *dispositivo*.

| Repo | URL | Licencia | Stars | Commits | Lenguaje | Rol |
|------|-----|----------|-------|---------|----------|-----|
| **accessibility-agents** | https://github.com/Community-Access/accessibility-agents | **MIT** ✅ | **419** | 374 | JavaScript | **El default de conformidad.** Agentes de revisión WCAG 2.2 AA que corren dentro de Claude Code, GitHub Copilot, Claude Desktop, Codex y Gemini CLI. Cubre código (HTML, JSX, TSX, Vue, Svelte, CSS), documentos (Word, Excel, PowerPoint, PDF, ePub), markdown y add-ons de NVDA |
| **uisight** | https://github.com/sololabstr/uisight | **MIT** ✅ | 128 | n/d | JavaScript | Medición de contraste, área táctil y *theme drift* sobre sesiones móviles y de escritorio en vivo, con **servidor MCP** para UIs web/responsive. Complemento de medición, no de revisión |
| **a11y-agents-kit** | https://github.com/weAAAre/a11y-agents-kit | **MIT** ✅ | 34 | n/d | TypeScript | Kit de skills de accesibilidad para harnesses de codificación con AI. De **weAAAre**, escuela de accesibilidad digital |
| **OptiKey** | https://github.com/OptiKey/OptiKey | **GPL-3.0** ⚠️ | **4.4k** | n/d | C# | Control de computadora y habla **con la mirada** (ELA / motoneurona). La tecnología asistiva más adoptada que registra esta KB |
| **Cboard** | https://github.com/cboard-org/cboard | **GPL-3.0** ⚠️ | 759 | 5.531 | JavaScript | **AAC** con texto-a-voz en el navegador (PWA), para parálisis cerebral y autismo. © Assistive Technology LLC; respaldo de UNICEF |

**Cómo elegir, en una línea:** acreditar conformidad y meterla en CI → **`accessibility-agents`** (MIT), con **`uisight`** (MIT) al lado cuando hace falta medición de contraste y área táctil — **los tres de conformidad son permisivos y empaquetables**; el cliente necesita el dispositivo de comunicación o de acceso → **Cboard** u **OptiKey**, desplegados **sin forkear** y con la lógica propia al lado.

⚠️ **La trampa de búsqueda de esta capa, y costó una consulta entera.** El topic `aac` de GitHub tiene 600+ repos y la abrumadora mayoría son de **Advanced Audio Coding** — codecs, demuxers, servidores de streaming — no de *Augmentative and Alternative Communication*. La sigla colisiona y el ranking por estrellas entierra lo asistivo. Hay que buscar por `assistive-technology`, `special-education` o `inclusive-education`, o por el nombre del producto. Es el mismo tipo de error que el pase 7 documentó con `tutor` y queda registrado en la nota de método.

⚠️ **Lo que esta capa no tiene, y es lo que la hace un gap y no sólo una sección:** ninguno de los cinco repos es educativo. `accessibility-agents` revisa código, `OptiKey` y `Cboard` son dispositivos de acceso. **No hay en abierto una pieza que conecte la acomodación declarada de un alumno con la adaptación automática del material** — que es el pedido real de un cliente de educación especial. Ver el **gap 12** en `intel/trends.md`.

## Capa de credenciales e interoperabilidad (1EdTech / W3C) — agregada en el pase 9 del 2026-10-01

La capa que acredita y mueve el aprendizaje entre sistemas. Cuatro estándares, y los cuatro son obligatorios en cualquier
integración institucional seria: **Open Badges 3.0 / W3C VC** (la credencial), **QTI** (el ítem de evaluación),
**OneRoster** (la matrícula y las notas), **Caliper** (la telemetría de eventos). Es hermana de la capa LRS/xAPI del pase 6
y se buscó por la misma razón: el estándar existe desde hace años y la KB no lo tenía porque no se llama «agente».

### Lo permisivo y vivo

| Repo | Licencia | Stars | Commits | Qué aporta a un proyecto |
|------|----------|-------|---------|--------------------------|
| https://github.com/1EdTech/lti-1-3-php-library | **Apache-2.0** ✅ | 124 | 110 | **LTI 1.3**: es lo que hace que un agente se monte *dentro* de cualquier LMS conforme (Moodle, Canvas, Open edX) sin integración a medida. Login OIDC, validación de mensajes, deep linking, envío de notas y lectura del roster |
| https://github.com/digitalcredentials/learner-credential-wallet | **MIT** ✅ | 88 | 1.309 | La billetera del **alumno** (React Native/Expo). W3C VC. v2.2.10, jun-2026. ⚠️ Gobernanza mudada a **OpenWallet Foundation Labs** — fijar versión |
| https://github.com/digitalcredentials/verifier-plus | **MIT** ✅ | 18 | 395 | **Verificación** y visualización de credenciales (copiar/pegar, archivo, URL o QR). Es el lado que usa el empleador |
| https://github.com/digitalcredentials/issuer-coordinator | **MIT** ✅ | 12 | 55 | **Emisión** + revocación/suspensión vía W3C **VC API**, con soporte de formato **Open Badges 3.0**. Docker Compose |
| https://github.com/amp-up-io/qti3-item-player | **MIT** ✅ | 30 | 596 | Runtime de ítems **QTI 3** con scoring y response processing. **Certificación de conformidad QTI 3 Basic y Advanced «Delivery» de 1EdTech** — el único artefacto certificado de esta KB |
| https://github.com/LongsightGroup/oneroster | **MIT** ✅ | 0 | 33 | **OneRoster 1.1/1.2**: CSV y REST, Node/Deno/navegador, provider router. 0 ★ — referencia de integración |
| https://github.com/KonstantinosPetrakis/esco-skill-extractor | **MIT** ✅ | 32 | 29 | Texto libre → competencias **ESCO** y ocupaciones **ISCO** con sentence transformers. El puente entre «terminó el módulo» y «acredita la competencia» |
| https://github.com/1EdTech/openbadges-specification | ⚠️ no declarada | 205 | 2.266 | La **especificación** (OB 3.0 / 2.1 / 2.0 + **CLR 2.0**), no código. Es el documento normativo al que hay que programar |

### Lo maduro, lo copyleft y lo archivado

| Repo | Licencia | Stars | Commits | Nota |
|------|----------|-------|---------|------|
| https://github.com/oat-sa/tao-core | **GPL-2.0** ⚠️ | 64 | **22.533** | **TAO**, plataforma de evaluación QTI/LTI de la Universidad de Luxemburgo + OAT. Por volumen de trabajo acumulado, la pieza más madura de toda esta KB. **No forkear**: desplegar y poner la inteligencia al lado |
| https://github.com/luisgf/openbadgeslib | **LGPLv3** / BSD-2-Clause ⚠️ | 1 | 404 | Ciclo completo de emisor **OB 3.0**: JWT-VC y Data Integrity, horneado en SVG/PNG, `did:web`, **Bitstring Status Lists** para revocar y suspender. v4.0.0 (2026-07-22). **404 commits, 1 estrella** |
| https://github.com/tl-its-umich-edu/caliper-php-public | **LGPL-3.0** ⚠️ | 3 | 365 | Fork de la **U. de Michigan** del cliente PHP de **Caliper**. Hoy es la implementación PHP accesible, y su banner explica por qué |
| https://github.com/european-commission-empl/European-Learning-Model | **EUPL-1.2** ⚠️ | 54 | 199 | Modelo de datos europeo de cualificaciones, acreditación y credenciales, compatible con W3C VC. 🔴 **ARCHIVADO el 2024-02-14** |
| https://github.com/european-commission-empl/european-digital-credentials | **EUPL-1.2** ⚠️ | 6 | 31 | Issuer + Viewer + Wallet de **European Digital Credentials for Learning** (Europass/EBSI). 🔴 **ARCHIVADO el 2024-02-02**, con el aviso textual: *«For the latest versions go to: https://code.europa.eu/qualifications-courses-and-credentials/»* — dominio **bloqueado por el proxy de egreso de esta sesión** (gap 14) |

### 🔴 Tres URL canónicas que ya no resuelven

`https://github.com/concentricsky/badgr-server` (**404**; la búsqueda de repos de la organización por `badgr` devuelve
*«No repositories matched your search»*; la organización hoy verifica el dominio **instructure.com**),
`https://github.com/1EdTech/caliper-php` (**404**) y `https://github.com/IMSGlobal/caliper-python` (**404**).

El banner del fork de la U. de Michigan nombra la causa de uno de los tres, **textual**:
*«This had been archived, but has been unarchived following 1EdTech making its caliper-php private.»*

**La regla operativa que esto deja:** en esta capa, **verificar la URL antes de citarla en una propuesta** no es
formalidad — tres de las referencias que la documentación del sector sigue repitiendo no existen. Ver **P21**.

## Capa de contenido curricular (OER) y su licencia — agregada en el pase 10 del 2026-10-01

La capa de la que **lee** el tutor. Nueve pasadas no la buscaron: la palabra «OER» no aparecía ni una vez en esta KB.
El patrón es el mismo que el pase 7 encontró en los datasets y el pase 8 en accesibilidad, **y una vuelta peor**: acá no
sólo la licencia del contenido es restrictiva, sino que **la licencia declarada a nivel de repo contradice la del archivo
`LICENSE`** (ver `agents/top.md`, capa de contenido curricular).

### Herramientas de autoría y repositorio — lo maduro es copyleft, con una excepción

| Repo | Licencia | Stars | Forks | Commits | Qué aporta |
|------|----------|-------|-------|---------|------------|
| https://github.com/DSpace/DSpace | **BSD-3-Clause** ✅ | 1.1k | **1.5k** | **25.385** | **La excepción permisiva, y es la pieza más madura de la capa.** Repositorio institucional (digital asset management) que sostiene los repositorios de universidades. Java. Es el lugar donde se guarda el corpus con su metadato de licencia, que es exactamente lo que pide **P22** |
| https://github.com/pressbooks/pressbooks | **GPL-3.0 or later** ⚠️ | 458 | 136 | 6.058 | Autoría de libros abiertos sobre WordPress multisite. PHP. El directorio público declara **7.042 libros de acceso abierto de 186 organizaciones**. Desplegar, no forkear |
| https://github.com/ManifoldScholar/manifold | **GPL-3.0** ⚠️ | 260 | 33 | **7.305** | Publicación académica como «obras digitales vivas». Útil como *target de salida* de un agente autor, igual que H5P |
| https://github.com/LibreTexts/Libretext | **GPL-3.0** ⚠️ | 29 | 9 | 1.699 | La plataforma LibreTexts: *«the primary repository for LibreTexts Javascript integrations and modifications»*. Contenido en biología, química, matemática, física, estadística, humanidades y **formación profesional** — que es la materia del gap 10 |
| https://github.com/openstax/openstax-cms | **AGPL-3.0** ⚠️⚠️ | 110 | 18 | 2.513 | El CMS de OpenStax (Wagtail sobre Django). **AGPL: el copyleft alcanza el uso en red.** Si se modifica y se sirve por SaaS hay obligación de publicar el fuente |

### El hallazgo útil: el *tooling* de LibreTexts es MIT aunque su plataforma sea GPL

| Repo | Licencia | Stars | Commits | Por qué sirve |
|------|----------|-------|---------|---------------|
| https://github.com/LibreTexts/shapeshift | **MIT** ✅ | 0 | 339 | *«A scalable, distributed system for extracting and transforming LibreTexts content into various export formats.»* **Es la pieza de ingesta y transformación de corpus** — el paso 1 de cualquier RAG curricular — con licencia limpia. 0 ★ y 339 commits: se forkea, no se depende de él |
| https://github.com/LibreTexts/conductor | **MIT** ✅ | 4 | 2.274 | Monorepo de la plataforma Conductor + LibreCommons + Campus Commons. TypeScript. **2.274 commits con 4 estrellas** |
| https://github.com/LibreTexts/davis | **MIT** ✅ | 0 | 133 | Librería de componentes **accessibility-first** para React y Vue sobre HeadlessUI. Es la pieza que une esta capa con la **capa de accesibilidad del pase 8**: el contenido accesible necesita componentes accesibles, y éste es MIT |
| https://github.com/LibreTexts/LibreOne | **MIT** ✅ | 1 | — | Gestión de identidad y autenticación central de LibreTexts |

**La lectura:** la organización publica su plataforma como GPL-3.0 y **sus herramientas periféricas como MIT**. Para un
engagement eso es mejor que parece: lo que se necesita de LibreTexts no es la plataforma —el cliente ya tiene un LMS— sino
**el extractor de contenido**, y ése es MIT.

### ⚠️ La capa de descubrimiento también es NonCommercial, y eso no estaba previsto

**OER Commons** (de **ISKME**) es la biblioteca pública de OER de referencia, con catálogo buscable de K-16. No publica
código reutilizable, y el dato que importa es otro: **ISKME comparte el metadato del catálogo con una licencia
NonCommercial**, por decisión explícita de tratar la educación como bien público.

**Consecuencia directa para una propuesta:** no se puede construir un recomendador, un buscador curricular ni una capa de
*discovery* comercial sobre el metadato de OER Commons. **No es el contenido el que está bloqueado: es el catálogo.** Y el
catálogo es justamente lo que uno querría para no tener que curar a mano. Ver el **gap 16**.

### El contrapunto APAC del pase 11, y es permisivo donde el europeo no lo es

| Repo | Licencia | Stars | Qué es |
|---|---|---|---|
| https://github.com/DECK6/korean-elementary-learning-map | **MIT** ✅ | 117 | Ontología curricular completa de la **educación primaria coreana (currículo revisado 2022)**: **620 anclas de estándares de logro, 1.956 temas de aprendizaje, 2.293 relaciones de prerrequisito y 152 clusters** sobre **11 materias** (coreano, matemática, ciencias, ciencias sociales, inglés como lengua extranjera, ética, artes prácticas/IT, materias integradas, arte, música y educación física) de **1.º a 6.º grado**. Sale en **JSON y RDF/Turtle**, con pipeline de validación, *competency questions* en **SPARQL** y restricciones **SHACL**. 17 commits. ⚠️ **Construcción independiente, no producto oficial del Ministerio de Educación**, armada desde fuentes curriculares públicas |

**Por qué esto cambia algo concreto.** Hasta este pase, el único esquema curricular nacional de la KB era
`OpenDidactia` (España, LOMLOE) y es **CC BY-SA 4.0** — share-alike, es decir, derivar el esquema del cliente
dispara la obligación. El coreano es **MIT**, y además viene con el grafo de prerrequisitos y la validación formal
que al español le faltan. **Para el patrón de "agente que genera planificación conforme al currículo nacional", APAC
tiene hoy la mejor pieza y es la más barata de licenciar.** Y hay una lectura de método: dos pasadas distintas
encontraron el mismo artefacto en dos regiones, lo que sugiere que el resto de los currículos nacionales también
están ahí y nadie los buscó. Ver el gap 19.

## Capa de infraestructura pública desplegada — agregada en el pase 10 del 2026-10-01

Dos plataformas que esta KB no tenía en nueve pasadas, **las dos permisivas**, y las dos invisibles a una búsqueda
ordenada por estrellas. Ver la nota de método del pase 10 en `intel/trends.md`: el indicador de esta capa es el
**cociente forks/stars**, no las estrellas.

### Sunbird — la plataforma educativa más grande del mundo es MIT, y tiene 41 estrellas

| Repo | Licencia | Stars | Forks | Commits | Qué es |
|------|----------|-------|-------|---------|--------|
| https://github.com/Sunbird-Ed/SunbirdEd-portal | **MIT** ✅ | **41** | **317** | **38.046** | *«Web Portal for sunbird software.»* El portal web completo. TypeScript/JavaScript (Angular + Node). Versiones estables por tag; master es el último release estable |
| https://github.com/project-sunbird/sunbird-devops | **MIT** ✅ | 62 | **392** | — | El despliegue: es lo que un ministerio ejecuta para levantar su instancia. Jinja |
| https://github.com/Sunbird-Ed/SunbirdEd-mobile-app | **MIT** ✅ | 10 | 92 | — | App Android (Cordova) con **consumo offline y online** del material. Relevante para el patrón P3 |
| https://github.com/project-sunbird/sunbird-telemetry-sdk | **MIT** ✅ | 4 | 46 | — | SDK de telemetría. **Conecta con la capa LRS/xAPI del pase 6** |
| https://github.com/Sunbird-Ed/SunbirdEd-consumption-ngcomponents | **MIT** ✅ | 3 | 64 | — | Librería Angular de componentes de consumo (cards, collections) |
| https://github.com/project-sunbird/sunbird-lms-mw | **MIT** ✅ | 6 | 41 | — | Middleware del LMS sobre el framework de actores **Akka**. Java |

**Qué es Sunbird.** Bloques modulares, configurables y extensibles de infraestructura digital de aprendizaje, de la
**EkStep Foundation** (India, cofundada por Nandan y Rohini Nilekani). Arquitectura de microservicios: gestión de
contenido, autenticación, rutas de aprendizaje, analítica y notificaciones como servicios desplegables por separado.
Reconocida **Digital Public Good** por la Digital Public Goods Alliance. Las organizaciones suman **64 + 88 repos**.

**La escala, que es el argumento de venta.** Sunbird sostiene **DIKSHA**, la plataforma oficial de educación escolar de
India: **180 millones+ de alumnos inscriptos**, **290.000+ contenidos** en **36 idiomas** y **4.950 millones+ de sesiones
de aprendizaje** acumuladas. ⚠️ Las cifras de DIKSHA vienen de fuentes secundarias y del material de EkStep y DPI Global;
**lo verificado de primera mano en este pase es el repo** (licencia, stars, forks, commits).

**Por qué nueve pasadas no lo vieron, y es el dato de método del pase.** **41 estrellas y 317 forks, con 38.046 commits.**
Una búsqueda ordenada por estrellas lo entierra debajo de cualquier tutor de fin de semana. Se forkea porque **cada estado
indio levanta su propia instancia** — el fork *es* el modelo de adopción, no una señal de interés.

### Ed-Fi — el estándar de datos de alumnos de K-12 en EE. UU., Apache-2.0

| Repo | Licencia | Stars | Forks | Commits | Qué es |
|------|----------|-------|-------|---------|--------|
| https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS | **Apache-2.0** ✅ | 28 | **47** | 1.053 | *«the core code for the Ed-Fi Operational Data Store (ODS) and Ed-Fi ODS API.»* El almacén operativo y su API |
| https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard | **Apache-2.0** ✅ | 46 | 13 | 370 | *«the foundation for enabling interoperability among secure education data systems.»* El modelo de datos |

Iniciativa de la **Michael & Susan Dell Foundation**. Pasó de licencia propietaria a **Apache-2.0 en abril de 2020**, y con
ese cambio los repos privados se hicieron públicos.

**Dónde encaja, y es un hueco real de la capa del pase 9.** El pase 9 cubrió OneRoster (matrícula y notas), Caliper
(eventos), QTI (ítems) y Open Badges (credencial), **y no cubrió el expediente longitudinal del alumno**, que en EE. UU.
es Ed-Fi y está adoptado a nivel estatal. **Es la pieza que un proyecto K-12 en North America necesita antes que
cualquier agente**, y es permisiva. Ver **P24**.

## Capa de analítica institucional (Apereo) y la licencia que esta KB no tenía — agregada en el pase 11 del 2026-10-01

### 🔴 Primero la licencia, porque cambia el filtro con que se leyó esta KB diez pasadas

Las diez pasadas anteriores filtraron por **MIT / Apache-2.0 / BSD**. Ese filtro deja afuera, en silencio, al
**stack completo de Apereo Foundation** — la fundación que sostiene la infraestructura open source de la educación
superior en EE. UU. y Europa — porque Apereo no licencia con Apache: licencia con **ECL-2.0**.

**ECL-2.0 (Educational Community License 2.0) es Apache-2.0 con una sola modificación: el alcance de la concesión de
patentes de la sección 3.** Está **aprobada por OSI y por la FSF**, salió del *Licensing and Policy Summit* de 2006
convocado por la comunidad académica, y existe porque las universidades no podían conceder el paquete de patentes
amplio que pide Apache-2.0 sobre código escrito con fondos de investigación.

**Lo que esto significa operativamente, y conviene decirlo con precisión:**

- **Para usar, modificar, redistribuir y cerrar un derivado:** se comporta como Apache-2.0. No es copyleft. No hay
  obligación de publicar el derivado. ✅ **Globant puede construir arriba.**
- **Para la *patent peace*:** la concesión es más angosta — cubre la contribución en sí, no las combinaciones. El
  propio README de `LearningAnalyticsProcessor` lo describe como *"a slightly less permissive Apache2"*. ⚠️ **En un
  cliente con due diligence de patentes, esto es una pregunta de legal, no una respuesta.**

**La regla operativa para esta KB:** ECL-2.0 entra en la misma categoría que MIT/Apache/BSD para cotizar trabajo
derivado, y se marca con ⚠️ únicamente cuando el entregable incluya cesión de patentes.

### Y ahora el hallazgo, que no es bueno: la capa de analítica institucional de Apereo está abandonada

La organización `Apereo-Learning-Analytics-Initiative` tiene **21 repos**. Verificado uno por uno el 2026-10-01:

| Repo | Licencia | Stars | Último push | Estado |
|---|---|---|---|---|
| https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW | **ECL-2.0** ✅ | **62** | **2026-08-04** | ✅ **La única pieza viva.** *Learning record warehouse* en Java compatible con **xAPI, IMS Caliper e IMS OneRoster** a la vez — es el único artefacto de esta KB que habla los tres estándares. 424 commits, badge *"Apereo incubating"*, lista `openlrs-user@apereo.org` |
| https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor | **ECL-2.0** ✅ | 23 | 2023-01-19 | ⚠️ **Dormido.** El *workflow manager* de analítica en Java. 25 forks. Es la pieza que debería orquestar el pipeline predictivo, y no se toca desde enero de 2023 |
| https://github.com/Apereo-Learning-Analytics-Initiative/Larissa | **Apache-2.0** ✅ | 8 | 2025-09-18 | ⚠️ LRS alternativo. Permisivo y con señal de vida, pero 8 estrellas |
| https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS | n/d | 47 | 2023-01-28 | 🔴 **Archivado por sus autores, y su descripción es literalmente la palabra `Deprecated`** |
| https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy | n/d | 47 | — | 🔴 **`(Deprecated)`** en la propia descripción. El framework de visualización de la capa |
| https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-ux | n/d | 1 | **2020-02-29** | 🔴 El reemplazo de OpenDashboard. **Creado el 2020-02-12, último movimiento 17 días después.** Front React |
| https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api | n/d | 0 | **2020-03-09** | 🔴 La otra mitad del reemplazo. Mismo patrón: creado el 2020-02-12, abandonado en marzo |
| https://github.com/Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider | n/d | 11 | 2024-11-30 | Integración xAPI para Sakai |
| https://github.com/Apereo-Learning-Analytics-Initiative/LAP-Sakai-Extractor | **Apache-2.0** ✅ | 2 | 2016-11-09 | 🔴 El extractor de datos de Sakai hacia el procesador. 2016 |

**Lo que hay que leer de esa tabla, y no es la lista:** el reemplazo del dashboard —las dos mitades, `-ux` y `-api`—
se creó el mismo día de febrero de 2020 y se abandonó dentro del mes siguiente. **La capa no se murió de a poco:
se intentó reescribir una vez y el intento duró tres semanas.**

**Y falta la pieza más citada del segmento:** *Student Success Plan* (SSP), el producto de *case management* de
advising que Apereo sostuvo con despliegues reales (St. Petersburg College, Sinclair Community College, soporte
comercial de Unicon). 🔴 **No tiene repositorio localizable en 2026 y el rastro público se corta alrededor de
2014-2015, en SSP 2.4.** Se registra como ausencia verificada, no como omisión.

### La capa que sí está viva de Apereo, y es la que conviene proponer

| Repo | Licencia | Stars | Forks | Último push | Qué es |
|---|---|---|---|---|---|
| https://github.com/sakaiproject/sakai | **ECL-2.0** ✅ | **1.234** | 1.014 | **2026-09-30** | **El LMS que a esta KB le faltaba después de diez pasadas.** Suite de enseñanza, investigación y colaboración en Java, usada por universidades de investigación. Mantiene **dos ramas a la vez**: tags `25.2` (2026-06-02) de la línea nueva y `23.5` (2026-06-30) de mantenimiento. ⚠️ No publica *GitHub Releases*: la versión se lee en los tags |
| https://github.com/opencast/opencast | **ECL-2.0** ✅ | 505 | 260 | **2026-09-30** | Captura y distribución automatizada de **video de clase** a escala. Es la capa multimodal que ningún otro repo de esta KB cubre: si el entregable incluye transcripción, indexado o resumen de clases grabadas, este es el punto de partida y no hay que construirlo |
| https://github.com/uPortal-Project/uPortal | **Apache-2.0** ✅ | 286 | 278 | 2026-09-22 | Portal empresarial de educación superior. Es la superficie donde una universidad ya expone sus servicios al alumno — el lugar natural donde montar un agente sin pedirle al alumno otra aplicación |

## Capa de datos de deserción — agregada en el pase 11 del 2026-10-01, y da vuelta el diagnóstico del gap 11

El gap 11 (pase 7) dice que **los datasets con que se entrena el modelado del alumno son NonCommercial**. Es cierto
para *knowledge tracing*. **Para predicción de abandono es al revés, y el dato es bueno.**

| Dataset | Licencia | Tamaño | Procedencia | Estado de verificación |
|---|---|---|---|---|
| **OULAD** — Open University Learning Analytics Dataset · `https://analyse.kmi.open.ac.uk/open_dataset` | **CC BY 4.0** ✅ *(uso comercial permitido)* | **22 cursos, 32.593 alumnos, 10.655.280 registros diarios de clicks en el VLE**, más demografía y resultados de evaluación | **EMEA (The Open University, Reino Unido — Knowledge Media Institute).** Publicado en *Scientific Data* (2017) | 🔴 **No verificado de primera mano:** el proxy de egreso de esta sesión bloquea `analyse.kmi.open.ac.uk`. Licencia y cifras provienen de múltiples fuentes secundarias coincidentes |
| **UCI 697** — *Predict Students' Dropout and Academic Success* · `https://archive.ics.uci.edu/dataset/697` | CC BY 4.0 ⚠️ **confirmar** | **4.424 instancias × 36 features**; clasificación en 3 clases (*dropout* / *enrolled* / *graduate*) al final de la duración normal de la carrera | **EMEA (Portugal).** Datos de una institución de educación superior sobre agronomía, diseño, educación, enfermería, periodismo, gestión, servicio social y tecnologías; financiado por el programa **SATDAP – Capacitação da Administração Pública**, grant `POCI-05-5762-FSE-000191` | 🔴 `archive.ics.uci.edu` **bloqueado por el proxy**. Tamaño, features y procedencia verificados contra el descriptor de datos publicado; **la licencia exacta hay que confirmarla en la ficha de UCI antes de facturar** |

**Por qué esto importa para una propuesta.** El `4.424` que aparece en decenas de los 110 repos MIT de la capa
predictiva es *este* dataset: la capa entera está entrenada sobre 4.424 alumnos portugueses de hace una década.
**Para un cliente de otra región eso no es un modelo, es un punto de partida metodológico** — y el trabajo real,
el que se cotiza, es re-entrenar sobre los datos del cliente. La buena noticia es que la licencia no lo bloquea.

**Y hay un benchmark nuevo de esta capa que conviene conocer:** *A Unified Survival Benchmark for Temporal Dropout
Risk Prediction in Learning Analytics* (arXiv **2604.08870**, Eastern University; v1 2026-04-10, v3 2026-07-21),
que corre sobre OULAD y compara dos familias de modelos —semanales dinámicos en representación *person-period*
contra estáticos de ventana temprana—. **Su conclusión es la más vendible del pase:** en ablación y
explicabilidad, todos los modelos convergen en que **la señal predictiva dominante es temporal y conductual, no
demográfica ni estructural.** Eso es exactamente el argumento que necesita un comité de ética o un DPO para
aprobar un sistema de riesgo: se puede predecir sin usar los atributos protegidos. 🔴 **No verificado de primera
mano** (`arxiv.org` sigue bloqueado por el proxy en este pase) y **las fuentes localizadas reportan que el link al
repositorio del paper está roto**, así que no hay código que auditar.

## Capa de empaquetado de conocimiento en *skills* (estándar Agent Skills) — agregada en el pase 12 del 2026-10-01

Las once pasadas anteriores buscaron *plataformas* (lo que se despliega), *modelos* (lo que infiere), *datasets* (con
qué se entrena) y *estándares* (con qué se interopera). Falta la capa que convierte **conocimiento de dominio en algo
que un agente carga**: el estándar **Agent Skills** —bundles de instrucciones, referencias y scripts que el agente
carga sólo cuando la tarea los pide—, que leen Claude Code, Codex, Cursor, Antigravity, Gemini CLI y Copilot CLI.

No es una capa educativa: es infraestructura genérica, y por eso va acá y no en `agents/top.md`. Lo que sí es
educativo —los paquetes pedagógicos— está en `agents/top.md`, sección «Capa de distribución por skills de agente».

### Los repos fundacionales, verificados vía WebFetch el 2026-10-01

| Repo | Licencia | Stars | Lenguaje | Por qué es fundacional acá |
|---|---|---|---|---|
| https://github.com/K-Dense-AI/scientific-agent-skills | **MIT** ✅ | **47.2k** | Python | **La arquitectura de referencia de una biblioteca vertical de skills**, y es MIT: 181 skills + 100+ bases de datos + 70+ workflows de paquetes. Para esta KB vale por su *estructura*, no por su contenido: es el molde de lo que la educación no construyó |
| https://github.com/virgiliojr94/book-to-skill | **MIT** ✅ | **33.2k** | Python | **Pipeline de contenido → skill**: convierte PDF/EPUB/DOCX en skill estructurada (SKILL.md con modelos mentales ~4k tokens, un archivo por capítulo on-demand, glosario, patrones, cheatsheet). Es la pieza que conecta la **capa de contenido curricular del pase 10** con esta capa, y procesa local |
| https://github.com/ankimcp/anki-mcp-server | **MIT** ✅ | **499** | TypeScript | Puente MCP hacia **Anki**, el SRS instalado de facto. Crear, leer y revisar mazos en lenguaje natural. v0.22.0, beta declarada, 254 commits |

### Por qué estos tres cambian una decisión de arquitectura de esta KB

El patrón **P1** y los que lo siguen asumen que un piloto de tutoría empieza por **desplegar algo** (Moodle + plugin,
OpenMAIC, un LMS). Esta capa ofrece un camino que no despliega nada:

1. **`book-to-skill`** toma el material del cliente —o un corpus OER con licencia apta, de los que el pase 10
   identificó— y lo convierte en skill con carga por capítulo.
2. La skill se instala en el harness que el cliente **ya paga** (Claude Code, Codex, Copilot CLI: los tres leen el
   mismo `SKILL.md`).
3. **`anki-mcp-server`** le da persistencia de repaso del lado del alumno sin que nadie opere un backend.

**El costo de infraestructura de ese piloto es cero** y el *lock-in* también: el artefacto es Markdown portable entre
harnesses. Es el contrapunto más barato que tiene esta KB frente a la capa de plataformas.

⚠️ **Y la contracara, que hay que decir antes de cotizarlo.** No hay *runtime* que garantice nada: sin eval, sin
versionado semántico y sin telemetría, una skill no produce evidencia de aprendizaje. Todo lo que esta KB construyó en
las capas de **telemetría (pase 6)**, **evaluación (pase 4)** y **credenciales (pase 9)** sigue haciendo falta, y
ninguna de las siete skills educativas verificadas lo tiene conectado. Un piloto de skills es barato de empezar y
**no es acreditable tal como viene**.

### La regla de verificación que este pase agrega, y vale para toda la KB

En esta categoría **los agregadores de estrellas de terceros van ~2× atrasados**: los dos repos de arriba dieron
**26.5k** y **13.7k** vía agregadores y **47.2k** y **33.2k** en la página del repo, el mismo día. Con `book-to-skill`
sumando +6.3k ★/mes, el dato de tercero no está viejo, **está mal**. Sólo vale la página del repo.

Y una advertencia operativa sobre el entorno: **`curl` hacia github.com devuelve 403 en este entorno** —se probaron las
**164 URLs de GitHub de esta KB y las 164 dieron 403**, uniformemente—. Es el proxy, no *link rot*. La verificación de
primera mano se hace con **WebFetch**. **Esas 164 URLs no quedaron revalidadas en este pase.**

## Capa de práctica y corrección desplegada (Jupyter) — agregada en el pase 13 del 2026-10-01

**Doce pasadas preguntaron qué hace el agente. Ninguna preguntó dónde hace el alumno el trabajo.** Esta KB documentó el
tutor, el modelado de conocimiento, la evaluación pedagógica, la seguridad, la telemetría, los datos, la accesibilidad,
la credencial, el contenido, la predicción y el empaquetado en skills. **Nunca documentó el entorno donde el alumno
escribe la respuesta y donde esa respuesta se corrige.** En educación superior y en formación técnica ese entorno tiene
un nombre, está desplegado desde 2014, y **toda su pila es BSD-3-Clause**.

No aparecía en esta KB porque no se llama «educación» ni «agente». Se llama **notebooks**.

### La pila, verificada repo por repo vía WebFetch el 2026-10-01

| Repo | Licencia | Stars | Qué aporta |
|---|---|---|---|
| https://github.com/jupyterhub/jupyterhub | **BSD-3-Clause** ✅ | **8.300** | Servidor multiusuario: entorno de cómputo por alumno, aislado, en el navegador. Python. La capa que hace que «entorno de práctica» sea operable para una cohorte entera |
| https://github.com/jupyterlab/jupyter-ai | **BSD-3-Clause** ✅ | **4.400** | **El runtime de agente de esta capa, y es el hallazgo del pase.** «Connects AI agents to computational notebooks in JupyterLab». Habla **Agent Client Protocol (ACP)** y **servidores MCP propios**, y detecta automáticamente los agentes instalados: Claude, Codex, GitHub Copilot, Gemini, Goose, Kiro, Mistral Vibe y OpenCode. Diseñado explícitamente sobre estándares abiertos para no quedar atado a un proveedor |
| https://github.com/jupyter/nbgrader | **BSD-3-Clause** ✅ | **1.400** | «A system for assigning and grading Jupyter notebooks». Celdas autocorregidas, tramos de corrección manual y **tests ocultos**, en un solo flujo: generar la versión del alumno, recolectar, autocorregir y consolidar notas. **v0.9.6 publicada el 2026-09-30** (incluye correcciones de *path traversal*). 3.477 commits |
| https://github.com/ucbds-infra/otter-grader | **BSD-3-Clause** ✅ | 161 | Autograder modular y liviano del **Data Science Education Program de UC Berkeley**, para scripts Python y notebooks, con salida hacia varios LMS. 3.820 commits. Es la alternativa cuando no se quiere el acoplamiento de nbgrader a JupyterHub |
| https://github.com/jupyterhub/ltiauthenticator | **BSD-3-Clause** ✅ | 73 | **El puente hacia el LMS que esta KB ya tenía documentado.** Implementa **LTI 1.3 y LTI 1.1**, y declara estar probado contra **Open edX, Canvas y Moodle** — exactamente las tres plataformas de `verticals/solutions.md`. Python |

**Cinco repos, 14.334 ★, una sola familia de licencia.**

### Por qué esto es el hallazgo de licencia más limpio de toda la KB

Las doce pasadas anteriores construyeron un diagnóstico consistente: en educación **lo desplegable es copyleft** (Moodle
y Chamilo GPL-3.0, Open edX y Canvas AGPL-3.0), **lo permisivo es de juguete** (los tutores de LATAM a 0–3 ★), **los
datos son NonCommercial** (gap 11), **el contenido tiene trampa de licencia** (pase 10) y **la accesibilidad es
copyleft** (pase 8).

**Esta capa rompe el patrón entero, y es la única que lo rompe:**

- Es **permisiva de punta a punta** — BSD-3-Clause en los cinco repos, sin AGPL, sin *share-alike*, sin NonCommercial.
- Está **desplegada de verdad**, no en estrellas: nbgrader está implementado desde 2014 en **UC Berkeley, Cal Poly,
  Universidad de Edimburgo** y **Aalto**, que publica su propia documentación de autograding para instructores.
- Está **viva**: la release de nbgrader es del **día anterior a este pase**.
- **Ya tiene runtime de agente con MCP**, que es precisamente la pieza que esta KB viene buscando capa por capa desde el
  pase 5 — y acá no hay que construirla.
- **Se conecta por un estándar que esta KB ya documentó.** La «Nota sobre licencias» de este mismo archivo recomienda
  desde la tercera pasada integrar «por LTI 1.3 / REST» para no forkear el core copyleft. `ltiauthenticator` es
  exactamente eso, hacia esta capa, y nadie lo había conectado.

### Lo que esto corrige, y hay que decirlo con precisión

El **gap 6** de esta KB dice, desde el pase 2 y sin cambios en once pasadas: *«no hay agente de grading open source con
tracción; la capa de grading sigue siendo propietaria —Gradescope (Turnitin), Codio, Kangaroos AI—; no prometer
reemplazar Gradescope, prometer orquestarlo»*. Esa conclusión se apoyaba en `gradescope-mcp` (8 ★), `classmoji`
(83 ★, AGPL-3.0), `rubric` (0 ★) y `llmgrader` (licencia de investigación).

**La formulación era más amplia que la evidencia.** Corregida:

| Tipo de trabajo del alumno | Estado real de la corrección open source |
|---|---|
| **Código, notebooks, datos, cálculo numérico** | **Resuelto, permisivo y desplegado.** nbgrader + otter-grader, BSD-3-Clause, en universidades desde 2014. No hay que construirlo ni orquestar a un propietario |
| **Prosa — ensayo, respuesta abierta, trabajo escrito** | **El gap 6 sigue en pie, y es ahí donde vive el incumbente.** Gradescope y Turnitin son dueños de esto; lo open source sigue siendo `papers` y repos pre-tracción |

Es una diferencia que cambia la propuesta. Para un cliente de **STEM, ciencia de datos o formación técnica**, decirle
«la corrección open source no existe, orquestemos Gradescope» es **falso y además caro**: la pila existe, es BSD y está
probada a escala de cohorte. Para un cliente de **humanidades o de evaluación por escrito**, el gap 6 original se
mantiene intacto.

⚠️ **Lo que esta capa no es.** No es un tutor, no modela el conocimiento del alumno y **no evalúa pedagogía**:
autocorrige contra tests que escribió el docente. Lo que aporta es el **sustrato de ejecución y evidencia** —el lugar
donde el trabajo ocurre y queda registrado— debajo de las capas que esta KB ya tiene. El `pyBKT` del gap 5 estima el
mastery, el LRS del pase 6 guarda la evidencia, y **esta capa es la que la produce**. Ver el patrón **P29**.

⚠️ **El acoplamiento es real y hay que cotizarlo.** nbgrader está fuertemente acoplado al ecosistema Jupyter: fuera de
JupyterHub, el intercambio de archivos y el flujo de entrega se complican rápido. Si el cliente no va a correr
JupyterHub, `otter-grader` es la pieza correcta, no nbgrader.

## Capa de esquema curricular nacional — agregada en el pase 14 del 2026-10-01, y cierra el gap 19

El gap 19 (pase 11) decía que los esquemas curriculares nacionales *«existen, son la pieza más cara de construir, y
esta KB encontró dos de casualidad en dos pasadas distintas»*, y dejó una acción explícita: buscarlos por país, en el
idioma del país. **Este pase lo hizo. De las cinco candidatas que el pase 13 listó, cuatro existen y una no.**

Es la pieza más cara de cualquier agente docente: el mapa de qué se enseña, en qué grado, en qué orden y con qué
prerrequisitos. **Ningún cliente quiere pagarla dos veces, y en cuatro países ya está publicada.**

| Artefacto | Región | País | Licencia | ★ | Contenido |
|---|---|---|---|---|---|
| [`fh-yarbouh/oak-curriculum-ontology`](https://github.com/fh-yarbouh/oak-curriculum-ontology) | **EMEA** | Inglaterra | **OGL-3.0** (datos) + **MIT** (código) ✅ | 0 | **50.948 *key learning points*, 11.207 *misconceptions*, 7.432 prerrequisitos, 12.517 *outcomes*, 13.012 *keywords*, 160 *threads*, 12 materias.** 31 clases, 75 propiedades, **38 *shapes* SHACL**. Turtle / JSON-LD / RDF-XML / N-Triples / SQLite / JSONL |
| [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | **LATAM** | Brasil | **MIT** (código) + **CC BY 4.0** (datos) ✅ | 19 | **1.721 aprendizagens** (1.580 de educación básica + **141 de Computação**, Parecer CNE/CEB 2/2022): 93 Infantil, 1.304 Fundamental, 183 Médio, 5 perfiles, 20 marcos legales. JSON / SQLite / CSV, **proveniencia por registro** y pipeline reproducible |
| [`commonstandardsproject/api`](https://github.com/commonstandardsproject/api) | **North America** | EE. UU. | **Apache-2.0** ✅ | 44 | Estándares académicos de **los 50 estados** + organizaciones, distritos y escuelas. JSON pensado para proveedores K-12. **API en vivo** (`api.commonstandardsproject.com`) |
| [`DECK6/korean-elementary-learning-map`](https://github.com/DECK6/korean-elementary-learning-map) *(pase 11)* | **APAC** | Corea del Sur | **MIT** ✅ | — | 620 anclas de estándares de logro, 1.956 temas, **2.293 relaciones de prerrequisito**, 152 clusters, 11 materias, grados 1-6. JSON y RDF/Turtle con *competency questions* SPARQL y restricciones SHACL |
| [`nmarafo/OpenDidactia`](https://github.com/nmarafo/OpenDidactia) *(pase 3)* | **EMEA** | España | ⚠️ **CC BY-SA 4.0** *share-alike* | — | Programación Didáctica y Situación de Aprendizaje para 17 comunidades + 2 ciudades autónomas, de Infantil a Bachillerato, FP y régimen especial |
| **MRAC** (ACARA) — `rdf.australiancurriculum.edu.au` | **APAC** | Australia | 🔴 **no verificable en esta sesión** | n/a | Currículo australiano **v9.0** en RDF/XML, manifiestos JSON y endpoint SPARQL (`/api/sparql`) |

### Lo que el pase 14 le agrega a la lectura de esta capa

**El artefacto inglés es el más rico del mundo en lo que de verdad cuesta, y tiene 0 estrellas.** Las 11.207
*misconceptions* y los 7.432 prerrequisitos de `oak-curriculum-ontology` son **conocimiento pedagógico de diagnóstico**:
qué se equivoca típicamente un alumno en cada punto del currículo. Eso no se deriva de un documento oficial con un
*script* — se construye con docentes. **Es, con diferencia, el artefacto más caro de reproducir de toda esta KB, y
está publicado con licencia que permite uso comercial** (OGL-3.0 para datos, MIT para el código).

**Y la comparación de licencias corrige la lección del gap 19.** El gap decía que el coreano (MIT) era «mejor
técnicamente y más barato legalmente» que el español (CC BY-SA), y lo tomaba como espejo del gap 4 (concentración en
APAC). Con cuatro artefactos más medidos, **el patrón ya no es regional**: hay permisivo apto para uso comercial en
las cuatro regiones —Inglaterra (OGL-3.0+MIT), Brasil (MIT+CC BY 4.0), EE. UU. (Apache-2.0), Corea (MIT)— y **el único
*share-alike* es el español**. La conclusión útil no es «APAC gana», es: **esta capa es, por licencia, la más limpia de
toda la KB, y hay que dejar de asumir que lo curricular es copyleft.**

### ⚠️ La regla de esta capa, y no es la misma que la del resto de la KB

**La licencia del código y la licencia de los datos son dos licencias distintas, y acá casi siempre difieren.**
`bncc-dados` es MIT en código y **CC BY 4.0** en datos; `oak-curriculum-ontology` es MIT en código y **OGL-3.0** en
ontología. Las dos combinaciones permiten uso comercial **con atribución**, que es una obligación de entregable, no un
detalle: hay que acreditar al MEC y a Oak National Academy en el producto. El pase 10 ya había abierto esta distinción
para contenido (OER); **este pase la confirma como la regla general de todo lo curricular.**

---

## Capa del estándar CASE (1EdTech) — agregada en el pase 14 del 2026-10-01

Lo que el gap 19 no anticipaba: **esta capa ya tiene un estándar de interoperabilidad con implementaciones
certificadas.** CASE® (*Competencies and Academic Standards Exchange*) define cómo se publica, se versiona y se
intercambia un marco de competencias o de estándares académicos, y cómo se alinea contenido contra él. El pase 9 abrió
la familia 1EdTech por el lado de las **credenciales** (Open Badges, CLR) y no miró el de los **estándares**.

| Repo | Licencia | ★ | Stack | Conformidad verificada |
|---|---|---|---|---|
| [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | **MIT** ✅ | **45** (27 forks) | PHP/Symfony, MySQL, Docker, Node/Yarn | ⚠️ Estable **3.2.0 (sept 2023)** → **CASE v1.0**; v1.1 en `develop` |
| [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) | **Apache-2.0** ✅ | **9** (3 forks) | Servidor + editor visual, multi-tenant | ✅ **v0.2 certificado CASE Service v1.0 y CASE v1.1 — certificaciones 2026-02-17** |
| [`infosign/compeito`](https://github.com/infosign/compeito) | **Apache-2.0** ✅ | **3** | Python 3.12, FastAPI, SQLAlchemy async, PostgreSQL, HTMX, Tailwind, Docker | ✅ *Provider* CASE v1.1; importa CFPackages de OpenSALT y OpenCASE; CSV compatible OpenSALT |
| [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) | **MIT** ✅ | **2** | Verificador de conformidad | ✅ **Once estándares:** CASE 1.1, xAPI 1.0.3 + IEEE 2.0, QTI 2.1/2.2/3.0.1, LTI 1.3 (+DL/AGS/NRPS/Proctoring), OneRoster 1.2, Common Cartridge 1.3/1.4, CLR 2.0, Open Badges 3.0, Caliper 1.2, cmi5, W3C VC 2.0 |

### 🔴 Por qué esta capa cambia una decisión de arquitectura, y no es un detalle de ingeniería

**Primero, el filtro por estrellas elige mal, y es la tercera vez que esta KB lo mide.** OpenSALT tiene 45 ★ y su
último estable es de septiembre de 2023 contra **CASE v1.0**. OpenCASE tiene 9 ★ y está **certificado contra v1.1 en
febrero de 2026**. Si el criterio de selección es popularidad, se elige la implementación que está una versión mayor
atrás del estándar. Es el mismo error que el pase 10 documentó con Sunbird (41 ★ sirviendo 180 millones de alumnos) y
el pase 11 con Apereo. **Regla: en capas de estándar, el criterio es la fecha de certificación, no la estrella.**

**Segundo, `conform-ed` es la pieza transversal más útil que apareció en catorce pasadas, y tiene 2 estrellas.**
Verifica **once** estándares de los que esta KB ya depende en cuatro capas distintas: xAPI (pase 6, patrón P15),
QTI (pase 9, patrón P20), Open Badges y W3C VC (pase 9, patrón P19), OneRoster y Common Cartridge (capa SIS, pases
2-3) y ahora CASE. **Hasta este pase, el "due diligence de interoperabilidad" del patrón P21 era trabajo manual.**
Con `conform-ed` es un *pipeline* ejecutable — y es MIT.

**Tercero, resuelve el problema de publicación que la capa curricular tiene abierto.** Los cuatro esquemas nacionales
verificados se publican cada uno en su formato (RDF el inglés y el coreano, JSON propio el brasileño y el
estadounidense). Un cliente que quiera **un** currículo consumible por sus herramientas no quiere cuatro parsers:
quiere un endpoint CASE. **Ese es exactamente lo que OpenCASE y `compeito` sirven**, y `compeito` además importa CSV
compatible con OpenSALT, que es el formato en que viven los estándares estatales de EE. UU.

---

## Capa de habla y lectura oral — agregada en el pase 14 del 2026-10-01

Trece pasadas asumieron que el alumno **escribe**. En alfabetización inicial la medición que usan los sistemas
educativos es que el chico **lea en voz alta** y se le midan palabras por minuto y exactitud. Esta capa es la
infraestructura para eso, y es nueva en esta KB.

| Repo | Licencia | ★ | Qué aporta |
|---|---|---|---|
| [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | **Apache-2.0** ✅ *(archivo `COPYING`; el badge de GitHub no lo muestra)* | **15.5k** | *Toolkit* ASR de grado industrial (C++/CUDA, Android, WASM). Es la base sobre la que la literatura construye tutores de lectura. **Genérico: no sabe nada de pedagogía** |
| [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | **MIT** ✅ | **85** | Evaluación **fonema a fonema** contra texto esperado, con Wav2Vec2 (`wav2vec2-lv-60-espeak-cv-ft` fonemas, `wav2vec2-large-960h` palabras, XLSR por idioma). Devuelve puntaje 0-100, **PER y WER**, confianza por palabra, distancia acústica por **DTW** y **prosodia (F0 y energía)**. **Corre local, sin API key** |
| [`jimbozhang/speechocean762`](https://github.com/jimbozhang/speechocean762) | ⚠️ **sin archivo `LICENSE`** | **198** | Corpus de referencia de la tarea: **5.000 oraciones, la mitad de hablantes son niños**, L1 mandarín. Puntajes de exactitud, completitud, **fluidez** y prosodia a nivel fonema/palabra/oración |

### ⚠️ Antes de usar nada de esta capa

- **`speechocean762` no tiene archivo de licencia.** El README afirma disponibilidad *«for both commercial and
  non-commercial purposes»*. **Eso es prosa, no un instrumento auditable** — es la misma trampa que el pase 10
  documentó para contenido abierto. Pedir los términos a SpeechOcean por escrito antes de cotizar.
- **OpenPronounce es la única pieza permisiva, educativa y utilizable de la capa**, y tiene 85 ★: se usa como
  componente con el commit pineado, no como dependencia de producto sin revisar.
- **El corpus es inglés con L1 mandarín.** Para español y portugués **no hay corpus permisivo verificado**; los
  puntajes de un modelo evaluado contra `speechocean762` **no son transferibles** a un despliegue en LATAM sin
  recalibración. Declararlo antes de prometer precisión.
- **Kaldi es Apache-2.0 y es lo que hay de maduro**, pero todo lo pedagógico hay que construirlo arriba.

## Capa de marcado y procedencia de contenido generado — agregada en el pase 15 del 2026-10-01, y es la que el Artículo 50 exige

Es la capa que esta KB venía **recomendando comercialmente desde el pase 4 sin tener una sola pieza registrada**.
`compose/patterns.md` anota desde entonces *«Watermarking de contenido generado → 2026-12-02»* como la oferta de
entrada a EMEA. La implementación existe, está madura y es permisiva.

### Las dos capas del esquema, y no son alternativas

El **Code of Practice** europeo sobre marcado y etiquetado de contenido generado por AI define un esquema **por
capas: metadato incrustado + watermarking**, con *fingerprinting* y *logging* como medidas de apoyo — y **adopta
las *Content Credentials* de C2PA como estándar técnico de facto** del metadato. Hay que desplegar las dos.

| Capa | Pieza | Repo | Licencia | ★ | Commits |
|---|---|---|---|---|---|
| **Watermark (texto)** | **SynthID-Text** | `huggingface/transformers` → `src/transformers/generation/watermarking.py` | **Apache-2.0** ✅ | viaja en Transformers | — |
| **Watermark (evaluación)** | **MarkLLM** | https://github.com/THU-BPM/MarkLLM | **Apache-2.0** ✅ | **1.100** (95 forks) | 185 |
| **Metadato / procedencia** | **c2pa-rs** | https://github.com/contentauth/c2pa-rs | **MIT *y* Apache-2.0** (dual) ✅ | **424** (192 forks) | **1.907** |
| **Metadato / procedencia (Python)** | **c2pa-python** | https://github.com/contentauth/c2pa-python | **Apache-2.0 *y* MIT** (dual) ✅ | 105 (35 forks) | 344 |

**Lo que hay dentro de `watermarking.py`, leído en el archivo:** `SynthIDTextWatermarkLogitsProcessor` (marca
durante la generación), `SynthIDTextWatermarkDetector`, `BayesianDetectorModel`, `BayesianDetectorConfig` y
`BayesianDetectorWatermarkedLikelihood`. Cabecera de copyright: *«Copyright 2024 The HuggingFace Inc. team and
Google DeepMind»*, bajo Apache-2.0.

### Por qué esta capa es distinta de todas las demás de esta KB

En las catorce capas anteriores el trabajo era **integración**: la pieza existía y había que conectarla. Acá el
trabajo es **todavía menor**. Un tutor construido sobre Transformers —que es casi cualquier tutor de esta KB— no
incorpora un proveedor nuevo ni un servicio: **agrega un `WatermarkingConfig` a la llamada de generación que ya
hace, y el detector sale del mismo paquete**. El costo de cumplir el Artículo 50(2) en el lado del texto es, para
ese caso, un parámetro.

**C2PA es el que sí requiere ingeniería**, y es donde está el valor del entregable: firmar manifiestos implica
decidir **con qué identidad** se firma (la *CAWG identity assertion* de la spec 2.4 existe para eso), dónde viven
las claves y cómo se valida en el otro extremo. Eso es un proyecto chico y real, no un parámetro.

### Qué rol juega **MarkLLM** y por qué no es redundante con SynthID

SynthID-Text marca. MarkLLM **mide si el marcado aguanta**: sus **12 herramientas de evaluación** cubren
detectabilidad, **robustez** e impacto en la calidad del texto, sobre **23+ algoritmos** (KGW, Unigram, SWEET,
UPV, EWD, SIR, X-SIR, DiPmark, SemStamp, k-SemStamp, EXP/EXPGumbel, MorphMark y el propio SynthID-Text). El
Artículo 50(2) exige que el marcado sea *«effective, interoperable, robust and reliable»*; **MarkLLM es con lo
que se produce la evidencia de que lo es**. En un expediente de conformidad, esa evidencia es el entregable.

⚠️ **Lo que esta capa NO resuelve, y hay que decirlo antes de cotizar.** El marcado sólo cubre el texto que
generó **el sistema propio**. Un ensayo escrito con un modelo externo no lleva marca y nunca la va a llevar. La
capa convierte un problema irresoluble (detección universal) en uno **parcial pero cierto** (verificación de lo
propio) más un **régimen de declaración** para el resto. Ver el **gap 25** y `agents/top.md`.

---

## Capa de detección forense de texto generado — agregada en el pase 15 del 2026-10-01, y se registra con su contraindicación

Está mejor abastecida de lo que esta KB suponía y **toda con licencia apta**. Se registra completa **porque un
cliente va a preguntar por ella**, y porque la respuesta profesional requiere conocerla, no ignorarla.

| Repo | Licencia | ★ | Forks | Commits | Qué es |
|---|---|---|---|---|---|
| https://github.com/baoguangsheng/fast-detect-gpt | **MIT** ✅ | **434** | 85 | 76 | **ICLR 2024**. Zero-shot por curvatura de probabilidad condicional; **340× más rápido que DetectGPT**. AUROC **0,9887** / **0,9338**. Python 3.8 + PyTorch 1.10, probado en A100 80 GB |
| https://github.com/ahans30/Binoculars | **BSD-3-Clause** ✅ | **420** | 67 | 54 | **ICML 2024**. Zero-shot sin entrenamiento; dos modelos de pesos abiertos en inferencia |
| https://github.com/liamdugan/raid | **MIT** ✅ | **216** | 98 | **378** | **ACL 2024**. Benchmark: **10M+ documentos**, 11 LLMs, **11 dominios**, 4 decodificaciones, **12 ataques adversarios**. Leaderboard `raid-bench.xyz` |
| https://github.com/NLP2CT/LLM-generated-Text-Detection | **MIT** ✅ | **252** | 16 | 40 | Survey vivo: ~100+ papers, 17+ datasets (HC3, CHEAT, DetectRL, DetectRL-X), métodos y ataques. *Computational Linguistics* **51(1), 2025** |
| https://github.com/pablocaeg/sloptotal | **MIT** ✅ | 39 | 8 | 58 | Ensamble de **23 motores** auto-hospedado, **corre en CPU**. Texto, PDF, DOCX y URLs |
| https://github.com/Lendarixon/awesome-ai-detection | **CC0-1.0** ✅ | 0 | 0 | 4 | Catálogo con los **modos de falla medidos** |
| https://github.com/yonatanlop/detectoria | 🚫 **Sin licencia** | 0 | 0 | 7 | El único pensado para **español**. Cuatro métodos, diseñado para el *Always Free* de Oracle Cloud. **Registrar, no proponer** |

### 🔴 La contraindicación, con los números de los propios autores

| Medición | Valor | Fuente |
|---|---|---|
| FPR sobre escritura de **no nativos de inglés** (TOEFL, 7 detectores) | **61,3 %** | Liang et al. |
| FPR sobre universitarios **nativos** | ~2,9 % | Liang et al. |
| FPR sobre 1.180 abstracts académicos **pre-2018** | **5,85 %** + 20 % «incierto» | `awesome-ai-detection` |
| Texto humano mal marcado por el ensamble de 23 motores | 1 de 66 | README de SlopTotal |
| Longitud mínima para que el score sirva | **~80 palabras**; estabiliza en ~200 | README de SlopTotal |
| Efecto de la paráfrasis | **caídas grandes de exactitud** | RAID |

**Y es estructural, no un defecto de versión:** la explicación propuesta para el 61,3 % es la **baja perplejidad**
del texto de no nativos, por menor variabilidad léxica. Un detector mejor entrenado sigue viendo lo mismo.

**La regla de uso que este pase fija para toda la KB:** un score de detección es **evidencia, no prueba**. Se usa
para **priorizar una conversación docente**; **nunca** para disparar una sanción automática, y **nunca** como
único insumo de una decisión disciplinaria. Para clientes cuyos alumnos escriben inglés como L2 —LATAM, EMEA no
anglófona, buena parte de APAC— es **pasivo legal antes que producto**. Ver el **gap 25**.

### El precedente institucional, que es el argumento más corto

Vanderbilt calculó que **1 % de FPR sobre 75.000 trabajos son ~750 acusaciones injustas por año** y desactivó el
detector de AI de Turnitin. **Más de 50 universidades** de EE. UU., Reino Unido, Canadá, Australia y Sudáfrica
—Johns Hopkins, Yale, Waterloo, Curtin, Australian Catholic University— lo desactivaron, restringieron o lo
abandonaron; **al menos 12 instituciones grandes a marzo de 2026**. El reemplazo que están adoptando es
**evidencia de proceso, escritura en clase, defensa oral y consignas que integran AI**.

⚠️ **Y ahí hay una colisión con la capa de accesibilidad del pase 8 que hay que registrar:** *«mostrá el historial
de versiones»* **no lo puede producir un alumno que escribe hablando**. Un entregable que exija evidencia de
proceso necesita **una vía alternativa documentada**, o es un problema de accesibilidad disfrazado de política de
integridad. Ver la capa de accesibilidad y la capa de habla (pase 14).

---

## Nota sobre licencias — leer antes de cotizar

El núcleo de las plataformas educativas open source es **copyleft fuerte**: Open edX, Canvas y Frappe LMS son AGPL-3.0; Moodle, Chamilo y H5P son GPL-3.0. AGPL alcanza el uso en red: si se modifica el core y se sirve por SaaS, hay obligación de publicar el fuente modificado.

**Matiz agregado en el pase 7, y es el más importante para cotizar:** la capa de **datos de entrenamiento** es la única donde lo permisivo es la excepción. `EdNet` y `FoundationalASSIST` son **CC BY-NC** (NonCommercial) y el segundo además **gated**; sólo `XES3G5M` es **MIT**, y es chino, de matemática y de tercer grado. **Consecuencia directa:** no se puede prometer un modelo de mastery entrenado "sobre datos públicos" en un entregable facturado. Se entrena con datos del cliente, y por eso el LRS va en la fase 1. Sumado a esto, la capa de **memoria de agente** entra copyleft de red (`Honcho`, AGPL-3.0, 7.4k ★). El riesgo de licencia se movió otra vez de capa.

**Matiz del pase 10, y es el que más caro sale:** hasta acá la KB leyó la licencia **del código**. La capa de **contenido
curricular** tiene su propia licencia, distinta, y **el repo la declara mal**. Los bundles de OpenStax en GitHub dicen
**CC BY-NC-SA** en su archivo `LICENSE` (3 de 3 títulos verificados: Calculus, Biology, College Physics), mientras el
puente MCP que los sirve y el ITS que los curó declaran **CC BY 4.0** en su README. **NonCommercial prohíbe exactamente el
uso de un entregable facturado, y ShareAlike obliga a abrir la derivación.** La regla que queda: **para contenido, leer el
campo de licencia del ítem, no el badge del repo** — y entregar el manifiesto como artefacto (**P22**). Sumado a esto, el
**metadato** del catálogo de referencia del sector (OER Commons / ISKME) es también **NonCommercial**, así que la capa de
descubrimiento está bloqueada aunque el contenido no lo esté.

**Matiz agregado en el pase 6:** la **capa de telemetría (LRS/xAPI)** entra mayoritariamente limpia — `lrsql` y `ADL_LRS` son Apache-2.0, `Ralph` y `learnmcp-xapi` son MIT. La excepción es la que más duele: **Learning Locker, el LRS más adoptado, es GPL-3.0**. O sea que el patrón habitual se invierte — acá lo permisivo es lo nuevo y lo copyleft es lo instalado. Si el cliente ya tiene un LRS, lo más probable es que haya que convivir con GPL; si se elige de cero, no hay razón para no ir a `lrsql` o Ralph.

**Matiz agregado en el pase 5:** en la **capa de medición y modelado** el panorama es el inverso al del LMS — `pyBKT`, `pyKT`, `EduBench`, `SafeTutors`, `rubric` y `py-fsrs` son **todas MIT**. Donde hay que mirar con lupa ahora es en los **modelos** (OmniEdu: sin licencia + herencia de Qwen) y en el **grading** (`llmgrader`: licencia de investigación custom). El riesgo de licencia se movió de capa, no desapareció.

**Matiz agregado en la tercera pasada del 2026-09-30:** eso sigue siendo cierto del **LMS**, pero ya no del **lado administrativo**. **GegoK12 es MIT y tiene sistema de plugins**, así que ahí el agente puede ir adentro con un plugin propietario. Dos pasadas anteriores de esta KB afirmaron que en el SIS el agente *siempre* tenía que ir afuera; era incorrecto y está corregido en `verticals/solutions.md` y en el gap 7 de `intel/trends.md`. La condición: GegoK12 es open-core y los módulos de exámenes y fees son pagos.

El patrón que evita el problema:

1. **No forkear el core copyleft.** Integrar por los puntos de extensión: XBlock (Apache-2.0) en Open edX, plugins del AI subsystem en Moodle, LTI 1.3 / REST en Canvas.
2. **La lógica propietaria vive en un servicio aparte** — el agente es un proceso separado con su propia licencia, hablando por API/MCP.
3. Cuando la propiedad del código importa, arrancar de **Oppia, OpenOLAT, Kolibri o Richie** (Apache-2.0 / MIT) del lado del aprendizaje, y de **GegoK12** (MIT) del lado administrativo.

---
*Ver también: `verticals/solutions.md` para plataformas verticales completas y `compose/patterns.md` para el wiring concreto.*
