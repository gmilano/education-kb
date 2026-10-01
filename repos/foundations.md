---
industry: education
region: Global
updated: 2026-10-01
---

# 🏗️ Repos fundacionales — education

> Bases sobre las cuales construir. Verificado repo por repo vía WebFetch el 2026-09-30 (capas del pase 10, el 2026-10-01).
> Leer la columna **Licencia** antes de proponer: media KB de educación es GPL/AGPL, no permisiva.

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

5 repos, todos MIT o Apache-2.0. Cubren las tres capas de una formación seria, y conviene elegir por capa y no por estrellas:

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
