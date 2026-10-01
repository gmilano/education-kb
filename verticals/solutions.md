---
industry: education
region: Global
updated: 2026-10-01
---

# 🏭 Verticales de partida — Education

> Plataformas verticales reales, en producción, customizables con AI.
> Modelo: partir de algo que ya funciona y que ya tiene los datos, y agregar la capa agéntica arriba.
> Verificado vía WebFetch el 2026-09-30; las capas del pase 11, el 2026-10-01.
> **Pase 11:** entra la capa **Apereo (ECL-2.0)** —Sakai, Opencast, uPortal, OpenLRW—, que diez pasadas descartaron por un filtro de licencia mal aplicado, y se documenta qué **no** proponer cuando el cliente pide *early warning*.

## Plataformas recomendadas

11 plataformas reales verificadas, más 4 en la capa SIS y **1 en la capa de autograding agregada en el pase 5**: 3 de SIS se agregaron en la segunda pasada del 2026-09-30 y **GegoK12 en la tercera**. El equivalente educativo de "Odoo para ERP" es **Moodle**: dominante, extensible, y desde 2026 con subsistema AI nativo.

| Plataforma | Licencia | URL | Stack | Caso de uso | Nota AI |
|------------|----------|-----|-------|-------------|---------|
| **Moodle** | GPL-3.0 | https://github.com/moodle/moodle | PHP + MySQL/Postgres | LMS de propósito general; el default global en K-12 y universidades públicas | **AI subsystem nativo.** Provider plugins para OpenAI, Azure OpenAI, Ollama, DeepSeek, Gemini y Amazon Bedrock. Placements: course assistant y text editor (generar texto/imagen, resumir, explicar). Moodle 5.2 salió 2026-04-20 con Gemini + Bedrock y soporte OpenTelemetry |
| **Open edX** | AGPL-3.0 | https://github.com/openedx/openedx-platform | Python/Django + React | MOOCs y cursos a escala; corporate academies | Extender con **XBlock** (Apache-2.0) — tu componente AI queda aislado del core AGPL |
| **Canvas LMS** | AGPL-3.0 | https://github.com/instructure/canvas-lms | Ruby on Rails | Higher-ed, dominante en EE. UU. | Integrar por LTI 1.3 + REST API. No forkear |
| **Oppia** | Apache-2.0 | https://github.com/oppia/oppia | Python + Angular/TS | Lecciones interactivas ("explorations") con feedback por pasos | Licencia permisiva. El modelo de explorations es el mejor *target de salida* para un agente que genera currículo |
| **Kolibri** | MIT | https://github.com/learningequality/kolibri | Python | Aprendizaje **offline-first**, sin requerir internet. Zonas de baja conectividad | MIT + offline. Combinar con un LLM local (Ollama) da tutoría sin backhaul |
| **Chamilo** | GPL-3.0 | https://github.com/chamilo/chamilo-lms | PHP | LMS liviano; fuerte en LATAM y EMEA hispano/francófona | El más simple de self-hostear: menor costo de infra por institución |
| **OpenOLAT** | Apache-2.0 | https://github.com/OpenOLAT/OpenOLAT | Java | LMS con assessment y evaluación sólidos; referencia DACH | Permisivo + assessment serio = el candidato para AI en evaluación bajo EU AI Act |
| **Frappe LMS** | AGPL-3.0 | https://github.com/frappe/lms | Python (Frappe) | LMS liviano sobre el stack Frappe | Si el cliente ya usa ERPNext, comparte stack y modelo de datos |
| **OpenEduCat** | LGPL-3.0 | https://github.com/openeducat/openeducat_erp | Python (Odoo) | **ERP educativo**: admisiones, matrícula, asistencia, exámenes, biblioteca | Es literalmente el Odoo de educación (corre como módulos Odoo). Cubre el lado administrativo que un LMS no toca |
| **BigBlueButton** | LGPL-3.0 | https://github.com/bigbluebutton/bigbluebutton | JavaScript/Node + Scala | Aula virtual en tiempo real: audio, video, pizarra, screen sharing | Fuente de transcripciones y señales de engagement para agentes de analítica |
| **Richie** | MIT | https://github.com/openfun/richie | Python/Django | CMS de portal educativo: catálogo, marketing de cursos, SEO | MIT. Complementa un LMS; es la capa pública de descubrimiento |

## Capa SIS — el lado administrativo, verificado 2026-09-30 (pases 2 y 3)

Un LMS gestiona el aprendizaje; un **SIS** (Student Information System) gestiona la institución: matrícula, legajos, asistencia, notas oficiales, facturación, disciplina. Es donde viven los datos que más valen para un agente y el área que casi ningún piloto de AI toca.

| Plataforma | Licencia | URL | Stack | Cobertura | Nota |
|------------|----------|-----|-------|-----------|------|
| **GegoK12** | **MIT** ✅ | https://github.com/Gego-K12/gegok12 | PHP 8.4 + Laravel 12 | School management / ERP completo, API-first, mobile-ready. Instalador visual o Docker | 54 ★, 97 forks, 123 commits, **último commit 2026-09-23**. **El primer SIS open source permisivo y vivo que encuentra esta KB.** Tiene sistema de plugins real, no declarativo: el repo de ejemplo [`Plugin-Hello-Teacher`](https://github.com/Gego-K12/Plugin-Hello-Teacher) (MIT, PHP/Laravel) muestra service provider para registro del plugin, migraciones y seeding propios, controllers/models/vistas Blade, archivos de rutas separados para portal docente y admin, y **hook de menú para la navegación lateral**. Es decir: hay puntos de extensión de verdad, incluida la UI. ⚠️ Open-core: ver el detalle abajo — exámenes y fees son módulos Pro pagos |
| **OpenEduCat** | LGPL-3.0 | https://github.com/openeducat/openeducat_erp | Python (Odoo) | ERP educativo completo: admisiones, matrícula, asistencia, exámenes, biblioteca | La opción **más adoptada y más completa**, y la primera a proponer cuando el alcance incluye exámenes o cobranzas sin módulo pago: corre como módulos Odoo, así que hereda todo el ecosistema Odoo. LGPL-3.0 → el agente va afuera |
| **RosarioSIS** | GPL-2.0 ⚠️ | https://github.com/francoisjacquet/rosariosis | PHP | Legajos, notas, horarios, asistencia, facturación, disciplina, comedor | 644 ★. Modular y mantenido. GPL-2.0: copyleft, **no** es AGPL, así que no alcanza el uso en red |
| **openSIS Classic** | GPL ⚠️ | https://github.com/OS4ED/openSIS-Classic | PHP (Apache + MySQL) | K-12, escuelas técnicas y superior: datos de alumnos y staff, horarios, asistencia, notas, reportes | 343 ★. La Community Edition es GPL; OS4ED vende ediciones comerciales encima |

**Lectura de esta capa — corregida en la tercera pasada del 2026-09-30.** Las dos pasadas anteriores concluyeron que el SIS open source es "PHP y copyleft, sin excepción útil", y que por lo tanto el agente **nunca** puede vivir dentro del SIS. La primera mitad sigue siendo cierta en cuanto al lenguaje: **todo el SIS open source es PHP.** La segunda mitad ya no: **GegoK12 es MIT, está activo (último commit 2026-09-23) y tiene sistema de plugins.**

Consecuencia arquitectónica, que es lo que realmente cambia:

- **Con RosarioSIS, openSIS u OpenEduCat** (todos copyleft) el agente va **afuera**, leyendo por API/DB con un servicio propio y su propia licencia. Sigue siendo el patrón por defecto, porque son los que tienen instalaciones reales.
- **Con GegoK12** el agente puede vivir **adentro, como plugin**, sin contaminar nada: MIT no impone share-alike, así que un plugin propietario sobre un core MIT es legal y limpio. Es la primera vez que la KB puede ofrecer esa opción en el lado administrativo.

No es una recomendación de reemplazo: es una opción nueva, con menos tracción que las alternativas copyleft y con una condición comercial que hay que leer antes (abajo).

### GegoK12 — leer la condición comercial antes de proponerlo

Verificado en la tercera pasada del 2026-09-30. El core es MIT de verdad: el archivo `LICENSE` del repo dice `MIT License` con `SPDX-License-Identifier: MIT`, © 2025 GegoSoft Technologies. No es "open source" de marketing.

**Pero es open-core, y el corte cae en los módulos que más importan.** Son 38 módulos en total:

- **26 en el core MIT gratuito:** alumnos, admisiones, asistencia, tareas, biblioteca, staff, avisos y comunicación con padres.
- **12 son add-ons Pro pagos, entre USD 100 y 250 cada uno** (USD 1.650 los doce): **examinación, gestión de fees/cobranzas**, timetable, media files, chat room, certificados, transporte, inventario, stock, video room, alumni y generador de exámenes.

La licencia Pro es **lifetime por dominio, con código fuente incluido y acceso a Git, más 5 años de updates** — no es una suscripción por alumno, que es el modelo del que la mayoría de las instituciones quiere escapar. Eso lo hace razonable comercialmente, pero hay que decirlo de entrada.

**Cómo afecta esto a una propuesta.** Los dos módulos que quedan del lado pago — **exámenes y fees** — son exactamente los dos que un agente querría tocar primero: corrección y cobranza son los procesos con más trabajo manual en una institución. Así que:

- Si el alcance es **admisiones, asistencia, legajos o comunicación con familias**, el core MIT alcanza y el agente puede ser un plugin. Ésta es la propuesta limpia.
- Si el alcance incluye **evaluación o facturación**, hay que comprar el módulo Pro (USD 100–250) o construir esa parte. **Cotizarlo explícitamente**: descubrirlo a mitad del proyecto es el modo de falla obvio.

**Origen:** GegoSoft Technologies OPC Private Limited, **Madurai (Tamil Nadu), India** → APAC. Encaja con el patrón que la KB ya registra: India produce el stack administrativo educativo open source (Frappe LMS, OpenEduCat, y ahora GegoK12).

**Tracción:** 54 ★ y 97 forks. La proporción forks/stars casi 2:1 dice que se despliega más de lo que se estrella — señal razonable para un ERP administrativo, donde el usuario es una escuela y no un desarrollador. No es Moodle: es un proyecto chico, de un solo vendor (GegoSoft), y eso es riesgo de continuidad a declarar.

### ⚠️ Fedena — dead end verificado, no proponer

`projectfedena/fedena` (Apache-2.0, 547 ★, 559 forks, Ruby on Rails) aparece recomendado en prácticamente todo listicle de "open source school ERP", y **su licencia permisiva lo hace tentador** frente al resto de la capa SIS, que es toda copyleft.

**Está muerto. El último commit es del 2016-07-20**, y los dos últimos son "emptying content" y "deleting unwanted pids files" — o sea, el propio Foradian lo vació. Antes de eso, actividad de enero de 2013.

Un Rails de 2013/2016 significa Ruby y Rails fuera de soporte, dependencias con CVEs sin parchear y cero upstream para reportar nada. La proporción forks/stars casi 1:1 (559/547) es la firma de un repo que la gente clona para desplegar y nunca contribuye de vuelta.

**Se registra explícitamente como dead end** porque el modo de falla es concreto: alguien busca "SIS con licencia permisiva", encuentra Apache-2.0 y 547 ★, y lo propone sin ver la fecha.

> **Corregido en el pase 4 del 2026-09-30.** Este párrafo cerraba diciendo *"si hace falta SIS permisivo, hoy no existe"*. **Es una contradicción con la sección de arriba de este mismo archivo**, escrita en el pase 3, que agrega **GegoK12 (MIT, vivo, último commit 2026-09-23)** justamente como el SIS permisivo que sí existe. La frase era un resto del pase 2 que no se actualizó al retirar el gap 7.
>
> **La lectura correcta:** si hace falta un SIS permisivo, la opción es **GegoK12** (MIT, con sistema de plugins, open-core — leer arriba la condición de los 12 módulos Pro). Si además hace falta tracción y módulos de examen/cobranza sin costo extra, se va a **OpenEduCat** (LGPL-3.0) y **el agente se aísla afuera**. Lo que sigue siendo cierto es lo que este párrafo dice de **Fedena**: está muerta desde 2016 y no se propone.

## Capa de autograding — agregada en el pase 5 del 2026-09-30

Las cuatro pasadas anteriores trataron el grading sólo como un gap (no hay grading AI open source con tracción; orquestar Gradescope). Faltaba registrar que **la plomería de corrección automática ya existe, está en producción a escala y no usa AI** — que es justamente lo que la vuelve una buena base.

| Plataforma | Licencia | URL | Stack | Cobertura | Nota |
|------------|----------|-----|-------|-----------|------|
| **Autograder.io** | ⚠️ no declarada en el repo de documentación | https://github.com/eecs-autograder/autograder.io | Docker + Python | Corrección automática **por casos de test**, sandboxing con Docker, feedback configurable, entregas en grupo, hand-grading | Mantenido por el departamento de CS de la **Universidad de Michigan**, que lo corre para **~5.000 alumnos por semestre en una docena de cursos**. 79 ★ |

**Por qué está acá y no en la lista de gaps.** Es el único artefacto de la capa de corrección de toda esta KB con **volumen de producción verificable**. Y para código, el autograding determinista sigue siendo mejor que un LLM: no alucina, es reproducible y es defendible ante una apelación de nota.

**El ángulo AI correcto encima de esto** es explicación y feedback formativo *sobre tests que ya corrieron* — "por qué falló este caso y qué concepto te falta" — no reemplazar los tests por un juicio de modelo. Eso además esquiva de frente el problema regulatorio: la nota la sigue poniendo un test determinista, y el LLM sólo explica. En una jurisdicción que prohíbe la calificación automática (ver `intel/trends.md`), es la diferencia entre un producto vendible y uno que no se puede desplegar.

⚠️ **El repo enlazado es el de documentación e issues y no declara licencia**; el código vive en otros repos de la organización `eecs-autograder`. Verificar la licencia del componente concreto antes de proponerlo.

**Para la capa de juicio con LLM**, cuando haga falta construirla, el punto de partida permisivo es **`paper-instruments/rubric`** (MIT, 75 ★) — rúbricas ponderadas genéricas. No usar `llmgrader` (NYU): es el más maduro de la categoría y su licencia es de investigación, no OSI. Detalle en `repos/trending.md`, pase 5.

### Ampliación del pase 13 del 2026-10-01 — la plataforma de esta capa no es Autograder.io, es JupyterHub, y es BSD-3-Clause

El pase 5 abrió esta capa con `Autograder.io` porque era «el único artefacto de corrección de esta KB con volumen de
producción verificable», y anotó que **el repo enlazado no declara licencia**. Las dos cosas quedan corregidas: hay una
plataforma de esta capa con más despliegue, licencia permisiva declarada y **runtime de agente ya incluido**.

| Plataforma | Licencia | URL | Stack | Cobertura | Nota |
|---|---|---|---|---|---|
| **JupyterHub** | **BSD-3-Clause** ✅ | https://github.com/jupyterhub/jupyterhub | Python | Entorno de cómputo aislado **por alumno**, en el navegador, para una cohorte entera | **8.300 ★.** Es la plataforma sobre la que se monta todo lo demás de esta fila |
| **nbgrader** | **BSD-3-Clause** ✅ | https://github.com/jupyter/nbgrader | Python | Asignación, recolección, **autocorrección**, tramos de corrección **manual** y **tests ocultos**, con consolidación de notas | **1.400 ★. v0.9.6 del 2026-09-30.** Implementado desde 2014 en **UC Berkeley, Cal Poly, Universidad de Edimburgo** y **Aalto** |
| **otter-grader** | **BSD-3-Clause** ✅ | https://github.com/ucbds-infra/otter-grader | Python | Autocorrección de scripts Python y notebooks, con salida hacia varios LMS | **161 ★**, del **Data Science Education Program de UC Berkeley**. La opción cuando **no** se va a correr JupyterHub |
| **ltiauthenticator** | **BSD-3-Clause** ✅ | https://github.com/jupyterhub/ltiauthenticator | Python | **LTI 1.3 y LTI 1.1** | **73 ★.** Declara estar probado contra **Open edX, Canvas y Moodle** — las tres plataformas de la tabla de arriba de este archivo |
| **jupyter-ai** | **BSD-3-Clause** ✅ | https://github.com/jupyterlab/jupyter-ai | Python/TS | **La capa AI, y no hay que construirla** | **4.400 ★.** ACP + servidores MCP propios; autodetecta Claude, Codex, Copilot, Gemini, Goose, Kiro, Mistral Vibe y OpenCode |

**Por qué esto cambia la propuesta de esta capa.** El pase 5 dejó escrito que el ángulo AI correcto era «explicación y
feedback formativo sobre tests que ya corrieron». **Ese ángulo sigue siendo el correcto, y ahora el lugar donde
enchufarlo ya existe, es BSD y entra por LTI 1.3 al LMS del cliente** — sin forkear el core AGPL de Open edX ni el GPL
de Moodle, que es exactamente la regla que `repos/foundations.md` viene recomendando desde la tercera pasada. Ver el
patrón **P29**.

⚠️ **Dónde aplica y dónde no, y es el límite que decide la venta.** Esta capa corrige **trabajo ejecutable**: código,
notebooks, datos, cálculo numérico. **No corrige prosa.** Para evaluación por escrito el cuadro del pase 5 y el gap 6
siguen vigentes sin cambios: el incumbente es propietario (Gradescope/Turnitin) y el camino realista es orquestarlo
(`gradescope-mcp`). Proponer JupyterHub + nbgrader a una facultad de humanidades es un error de encaje.

⚠️ **Y hay un acoplamiento que hay que cotizar.** nbgrader está fuertemente atado al ecosistema Jupyter: fuera de
JupyterHub, el intercambio de archivos y el flujo de entrega se complican rápido. Si el cliente no va a operar
JupyterHub, la pieza correcta es `otter-grader`, no nbgrader.

## Referencia teacher-facing — Aila (pase 5)

No es una plataforma para desplegar, y se registra acá porque es la mejor referencia de arquitectura disponible para el lado docente:

**Aila / Oak AI Lesson Assistant** — https://github.com/oaknational/oak-ai-lesson-assistant — **MIT**, 35 ★, **1.188 commits**. Monorepo Turborepo con Next.js, Prisma/PostgreSQL y **pgvector**, entornos de producción y staging. De **Oak National Academy** (nonprofit educativa británica respaldada por el gobierno).

⚠️ El propio repo dice que está *"intended primarily for internal use by Oak National Academy"*: **no hay API estable, ni soporte, ni garantía de que se despliegue fuera del contexto de Oak.** La licencia MIT permite copiar piezas, y eso es el uso correcto — ver cómo un equipo real resolvió en producción el RAG curricular, la persistencia de la conversación de planificación y la generación de recursos, en vez de rediseñarlo desde cero.

## Capa de telemetría — agregada en el pase 6 del 2026-10-01

Un LMS gestiona el aprendizaje y un SIS gestiona la institución; **un LRS guarda lo que efectivamente pasó**. Es la pieza que hace que el agente, el LMS y el SIS compartan una misma historia del alumno en vez de tres parciales. Estándar: **xAPI / IEEE 9274.1.1**. El inventario completo con licencias y commits está en `repos/foundations.md`; acá va sólo la decisión de plataforma.

| Plataforma | Licencia | URL | Stack | Cuándo proponerla |
|------------|----------|-----|-------|-------------------|
| **SQL LRS (`lrsql`)** | **Apache-2.0** ✅ | https://github.com/yetanalytics/lrsql | Clojure sobre SQLite / PostgreSQL 14–18 / MariaDB / MySQL 8–9.5 | **El default.** Corre sobre la base de datos que el cliente ya opera, así que no agrega una pieza de infraestructura nueva al diagrama |
| **Ralph** | **MIT** ✅ | https://github.com/openfun/ralph | Python/FastAPI + Elasticsearch, Docker/K8s | Cuando el cliente está sobre **Open edX**: convierte los tracking logs a xAPI de fábrica. Mismo origen (OpenFun, Francia) que Richie |
| **Learning Locker** | GPL-3.0 ⚠️ | https://github.com/LearningLocker/learninglocker | Node.js + MongoDB | Rara vez por elección propia — pero es el más instalado de la categoría, así que es el que uno **se encuentra**. Copyleft: el servicio que lo modifique hereda la obligación |
| **ADL_LRS** | Apache-2.0 ✅ | https://github.com/adlnet/ADL_LRS | Python/Django | Sólo para **validar conformidad** con el estándar. El repo declara ser proof-of-concept para pocos usuarios: no proponerlo como almacén de producción |

**El par que hace la diferencia en una demo:** `lrsql` (o Ralph) + **`learnmcp-xapi`** (MIT, servidor MCP). Con esos dos, un agente de tutoría deja de tener memoria propia y empieza a escribir en el registro institucional — que es exactamente lo que pide un director académico cuando pregunta "¿y esto dónde queda guardado?". Wiring concreto en **P15**.

**Nota sobre ERPNext, con una corrección de matiz.** Las búsquedas de "ERP educativo open source" devuelven consistentemente **ERPNext** (https://github.com/frappe/erpnext) junto a OpenEduCat, y el material comercial de Frappe lo presenta *for education*. Verificado de primera mano en el repo: **GPL-3.0, 39,7k ★**. Cae del mismo lado que OpenEduCat y RosarioSIS — copyleft, el agente va afuera.

⚠️ **Lo que no se pudo confirmar, y hay que confirmarlo antes de proponerlo:** que el módulo de educación sea **parte del core de ERPNext**. En el repo lo único con ese nombre que aparece es *Frappe School*, que es una plataforma de cursos sobre el propio framework, no un módulo de gestión académica. La funcionalidad educativa de ERPNext fue históricamente una app aparte. **Registrarlo como candidato sólo cuando el cliente ya corre ERPNext** (evita meter un segundo ERP), y verificar primero en qué app vive el módulo. No desplaza a GegoK12 ni a OpenEduCat.

## Tutores desplegables — agregada en el pase 7 del 2026-10-01

Esta KB venía listando tutores en `agents/top.md` sin separar los que **se despliegan y se customizan** (que es de lo que trata este archivo) de los que son librerías o referencias. El pase 7 encontró tres tutores con tracción que no estaban registrados, y los tres son **self-hosted con interfaz de usuario completa** — o sea candidatos de esta capa, no de la de agentes.

**Y los tres tienen fricción de licencia.** Es la razón por la que se registran acá con la condición adelante y no en la lista de recomendados.

| Tutor | Licencia | Stars | URL | Cuándo proponerlo |
|---|---|---|---|---|
| **ChatTutor** | **AGPL-3.0** ⚠️ | 1.3k | https://github.com/HugeCatLab/ChatTutor | Cuando lo que vende la demo es **interacción visual**: canvas de matemática y mapas mentales **expuestos al LLM como herramientas**. Es el único de la KB que le da al modelo instrumentos de pizarrón. **Desplegar sin modificar**; si se modifica y se sirve por SaaS, la AGPL obliga a publicar el fuente |
| **tutor-gpt** | **GPL-3.0** ⚠️ | 931 | https://github.com/plastic-labs/tutor-gpt | Como **referencia de arquitectura** de modelado del estado mental del alumno (teoría de la mente + reescritura del propio prompt). GPL-3.0 no es copyleft de red: servirlo sin modificar no dispara obligación; modificarlo y distribuirlo sí. Procedencia **EE. UU.** (Plastic Labs), útil cuando hay restricción de origen |
| **llamatutor** | 🚫 **sin licencia** | 2.1k | https://github.com/Nutlope/llamatutor | **No proponer.** Verificado en el pase 7: `/blob/main/LICENSE` devuelve **404**, así que el default legal es todos los derechos reservados. Sirve para mirar cómo resolvieron la UX, nada más |

**Cómo se lee esto junto con las plataformas de arriba.** El patrón recomendado de este archivo no cambia: **no forkear el core copyleft, poner la lógica propietaria en un servicio aparte y hablar por API/MCP.** Aplicado a estos tres, significa desplegar `ChatTutor` tal cual y poner la inteligencia propia al lado, en vez de forkearlo — que es exactamente la misma receta que para Moodle y Open edX.

⚠️ **Lo que sigue sin tener alternativa permisiva de escala.** Si el requisito es **empaquetar un tutor en un entregable cerrado**, las únicas bases open source de escala siguen siendo las dos de APAC: **`DeepTutor`** (Apache-2.0, 40.6k ★) y **`OpenMAIC`** (MIT, 39.7k ★). El pase 7 lo midió contra las alternativas en vez de suponerlo, y la conclusión no cambió. Para un cliente con restricción de procedencia, eso es una tensión real que hay que poner sobre la mesa temprano — ver el gap 4 en `intel/trends.md`.

## Capa de integridad académica — agregada en el pase 8 del 2026-10-01

Capa que la KB no tenía y que aparece en toda conversación de evaluación sumativa. El estado es claro: **la integridad académica open source con calidad de producción no existe todavía, y el actor que la está construyendo es Open edX.**

| Pieza | Estado | Licencia | Qué es |
|-------|--------|----------|--------|
| **Open edX Proctoring Toolset** | 🔴 **Propuesta, no release** — target **Verawood** | Será la de Open edX (**AGPL-3.0**) ⚠️ | Proctoring **nativo** en la plataforma usando APIs estándar del navegador: verificación de identidad, grabación por webcam con revisión manual o asistida por AI, dashboards para el instructor, e integración opcional con **Safe Exam Browser** para bloqueo de dispositivo. Autores: Elizabeth Gordon, Ali Hugo y Arunmozhi Periasamy (**Arizona State University** + **OpenCraft**) |

**El dato de posicionamiento, y es el que vale.** La motivación declarada de la propuesta es que Open edX no tiene hoy una opción de proctoring integrada y gratuita, y que esa carencia **afecta desproporcionadamente a instituciones del Sur Global y a las de bajo presupuesto**, que quedan obligadas a contratar Respondus LockDown Browser, Wheebox o ProctorU. Para una propuesta en **LATAM** o en **África** eso es exactamente el argumento de costo que convierte una discusión técnica en una decisión presupuestaria.

⚠️ **Cómo tratarlo hoy: como roadmap, no como componente.** Es una propuesta con release objetivo, no código que se pueda desplegar. No ponerlo en un diagrama de solución ni cotizarlo. Sí sirve para dos cosas concretas: **(a)** decirle al cliente que la categoría va a dejar de ser propietaria y que conviene no firmar tres años de proctoring cerrado ahora, y **(b)** posicionarse como el equipo que lo va a integrar cuando salga.

⚠️ **Lo que hay fuera de Open edX no es proponible.** La búsqueda de proctoring open source devuelve mayoritariamente **proyectos de estudiante y de trabajo final** — detección de rostro y de objetos con YOLO, seguimiento de mirada, bloqueo de pestañas — sin licencia clara, sin mantenimiento y sin evaluación de sesgo. **Y el sesgo es el punto que hunde la categoría entera:** un sistema de vigilancia biométrica sobre alumnos es, bajo el EU AI Act, exactamente el tipo de sistema de **alto riesgo** del Annex III en acceso y evaluación educativa. Proponer un proctoring sin expediente de conformidad es ofrecerle al cliente el riesgo regulatorio, no la solución. Ver **P4**.

### La otra mitad de esta capa, agregada en el pase 15 del 2026-10-01 — autoría, no vigilancia

Lo de arriba es **proctoring**: vigilar el examen. Pero la pregunta que el cliente hace primero no es esa, es
**«¿cómo sé quién escribió el trabajo?»** — y con el 92 % de los alumnos usando AI, es la que decide si la
evaluación sumativa se puede defender. El pase 15 abre esa mitad. El inventario completo está en
`agents/top.md` y `repos/foundations.md`; acá va **qué se despliega y qué no**.

| Enfoque | Qué hay en abierto | ¿Proponible? |
|---|---|---|
| **Marcar en el origen** (*watermarking* de la salida del propio tutor) | **SynthID-Text** (Apache-2.0, dentro de `huggingface/transformers`), **MarkLLM** (Apache-2.0, 1.100 ★) para evaluar robustez | 🟢 **Sí, y es lo primero.** Costo: un `WatermarkingConfig` en la llamada de generación que el tutor ya hace |
| **Procedencia del artefacto** (manifiesto firmado) | **c2pa-rs** (MIT + Apache-2.0 dual, 424 ★, **1.907 commits**), **c2pa-python** (dual, 105 ★) | 🟢 **Sí.** Es el estándar que el **Code of Practice** europeo adopta de facto para el metadato incrustado. Es el tramo con ingeniería real: identidad de firma, custodia de claves, validación |
| **Detección forense** del texto entregado | `fast-detect-gpt` (MIT, 434 ★), `Binoculars` (BSD-3, 420 ★), `RAID` (MIT, 216 ★), `sloptotal` (MIT, 39 ★) | 🔴 **No como mecanismo de sanción.** **61,3 % de falsos positivos** sobre escritura de no nativos de inglés. Sirve para **priorizar una conversación docente**, nada más |
| **Evidencia de proceso** (pulsaciones, historial de versiones) | **Nada en abierto** — GPTZero Authorship, Grammarly Authorship, Turnitin Clarity y Draftback son propietarios | 🔴 **No.** Y choca con accesibilidad: el alumno que escribe hablando no puede producir ese artefacto |

**La receta de esta capa, y es la misma de siempre en esta KB invertida una vez.** En el resto de los casos la
regla es *desplegar el estándar instalado y poner la inteligencia al lado*. Acá la regla es: **mover la pregunta**.
*«¿Esto lo escribió una AI?»* no tiene respuesta confiable. *«¿Esto lo escribió **nuestro** tutor?»* sí, y es una
verificación criptográfica. Una institución que **provee** el agente puede marcar su salida y dejar de adivinar.
El wiring concreto está en **P33**.

⚠️ **Lo que hay en el directorio de Moodle no es open source de punta a punta.** Los plugins de integridad son
**envoltorios de servicios propietarios**: **Compilatio** (el plugin es **GPL-3.0**, 821 instalaciones, release
2026-06-25), **Originality.ai** (Moodle 3.9–5.0, release 2026-07-02) y **Copyleaks**. El código del plugin es
libre; **el detector detrás es un servicio pago**, y es el mismo tipo de producto que 50 universidades
desactivaron. No presentarlos como la opción abierta.

🔴 **Verificación de estos tres:** `moodle.org` está **bloqueado por el proxy de egreso**, así que licencia,
cantidad de instalaciones y fechas de release salen de resultados de búsqueda, **no de la página del
directorio**. Confirmarlas ahí antes de ponerlas en un comparativo para un cliente. Lo que sí es de primera
mano en esta capa son los **nueve repos de GitHub**, leídos página por página vía WebFetch el 2026-10-01.

🟢 **Y la nota regional que conviene tener a mano.** **México, Colombia y Chile exigen que el alumno declare el
uso de AI**, con sanción por uso fraudulento y en algunos casos **entrega de los prompts**. Un régimen de
**declaración** se satisface con procedencia —marcar, firmar, registrar— y **no requiere acertar un juicio
forense**. Es el único de los cuatro regímenes regionales que el stack permisivo de hoy **puede cumplir
completo**. Y lo que está instalado en UNAM, Tec de Monterrey, UAM, BUAP y UdeG es **Turnitin Originality**, o
sea detección. Esa distancia entre la norma y la herramienta es la propuesta. Ver `intel/market.md` → LATAM.

## Capa de credenciales y evaluación conforme a estándar — agregada en el pase 9 del 2026-10-01

Plataformas reales que se despliegan y se customizan con AI al lado, para el tramo que acredita el aprendizaje.
Es la misma receta que esta KB aplica a Moodle y Open edX, y acá es **obligatoria** porque las dos piezas maduras son copyleft.

| Plataforma | Repo | Licencia | Qué cubre | Cómo se customiza con AI |
|-----------|------|----------|-----------|--------------------------|
| **TAO** | https://github.com/oat-sa/tao-core | **GPL-2.0** ⚠️ | Plataforma de evaluación **QTI + LTI** completa: autoría de ítems, entrega de exámenes, scoring, control de acceso por roles, webhooks, feature flags, colas de tareas. **22.533 commits**, origen Universidad de Luxemburgo, mantenida por Open Assessment Technologies | **Desplegar tal cual, no forkear.** La generación de ítems (`Educhain`, MIT) y el gate de calidad pedagógica (`EduBench`/`SafeTutors`, MIT) corren **afuera** y entregan QTI XML. La integración es por webhooks y LTI, que TAO ya expone |
| **Reproductor QTI 3 embebible** | https://github.com/amp-up-io/qti3-item-player | **MIT** ✅ | Runtime de ítems QTI 3 con response processing y scoring, ítems adaptativos, template processing. **Certificación de conformidad QTI 3 Basic y Advanced «Delivery» de 1EdTech** | **Es la alternativa a TAO cuando la licencia importa.** No es una plataforma: es el componente de entrega. Se embebe en producto propio y se le agrega autoría e inteligencia arriba, **sin fricción de licencia y con conformidad certificada** |
| **Stack de credenciales DCC** | `digitalcredentials/issuer-coordinator` + `verifier-plus` + `learner-credential-wallet` | **MIT** ✅ (los tres) | Emisión (W3C **VC API**, formato **Open Badges 3.0**), revocación y suspensión, verificación con QR, y billetera móvil del alumno | Es el único tramo **enteramente MIT** de esta capa. La AI no va adentro: va **antes**, decidiendo si corresponde emitir (ver **P19**) |
| **Emisor OB 3.0 en Python** | https://github.com/luisgf/openbadgeslib | **LGPLv3** / BSD-2-Clause ⚠️ | Ciclo completo de emisor: JWT-VC y Data Integrity, horneado en SVG/PNG, `did:web`, **Bitstring Status Lists** para revocar y suspender. Soporta OB 3.0, 2.0 estricto y 1.0 legacy | Alternativa al `issuer-coordinator` cuando el stack es Python. ⚠️ **LGPL: enlazar sí, modificar y distribuir no** — y los perfiles de badge son justo lo que uno quiere modificar |
| **LTI 1.3 como vía de entrada** | https://github.com/1EdTech/lti-1-3-php-library | **Apache-2.0** ✅ | Tool provider LTI 1.3: login OIDC, deep linking, envío de notas, lectura del roster | **Es el modo correcto de meter un agente en un LMS que no es nuestro.** Evita el fork de Moodle/Canvas/Open edX por completo: el agente es una herramienta externa conforme |
| **OneRoster para matrícula y notas** | https://github.com/LongsightGroup/oneroster | **MIT** ✅ | OneRoster 1.1/1.2 por CSV y REST, Node/Deno/navegador | Sincroniza alumnos, cursos, secciones y notas con el SIS sin integración a medida. 0 ★ — tratarlo como referencia y fijar la versión |

### ⚠️ Lo que no hay que proponer en esta capa

- **Badgr** (`concentricsky/badgr-server`) — **404 verificado**, y la búsqueda de repos de la organización por `badgr` no
  devuelve nada. Es **Canvas Credentials** de Instructure y después **Parchment Digital Badges**: propietario. Toda la
  documentación del sector lo sigue citando como «la implementación open source de Open Badges». **Ya no lo es.**
- **European Digital Credentials** (`european-commission-empl/*`) — **archivados** (feb-2024, EUPL-1.2). El código vivo
  está en `code.europa.eu`, que **esta sesión no puede alcanzar**: para un cliente europeo hay que abrirlo y verificarlo
  antes de cotizar (gap 14).
- **Caliper** vía las URL oficiales (`1EdTech/caliper-php`, `IMSGlobal/caliper-python`) — las dos **404**. Para PHP, la
  pieza accesible hoy es el fork de la **Universidad de Michigan** (`tl-its-umich-edu/caliper-php-public`, LGPL-3.0).
  Para telemetría nueva, **preferir xAPI y un LRS** (`lrsql`, `Ralph` — ver `repos/foundations.md`), que es la capa
  hermana y está viva.

### La regla de esta capa, y es distinta a la del resto de la KB

En las ocho capas anteriores la señal de calidad eran las estrellas y los commits. Acá no: el repo más estrellado es
**una especificación** (205 ★, no código), el de más commits es **GPL-2.0**, y la pieza con **certificación de
conformidad de 1EdTech tiene 30 estrellas**. **En credenciales e interoperabilidad se elige por conformidad certificada
y por licencia, no por popularidad** — y se **verifica que la URL resuelva** antes de ponerla en una propuesta.

## Capa de plataforma de sistema educativo nacional — agregada en el pase 10 del 2026-10-01

Las nueve pasadas anteriores respondían «plataforma de ministerio» con **Moodle** (GPL-3.0) u **Open edX** (AGPL-3.0): las
dos copyleft, con el agente obligado a vivir afuera. Hay una tercera opción, es **MIT**, y sostiene el sistema escolar más
grande del mundo.

| Plataforma | Repo | Licencia | Qué cubre | Cómo se customiza con AI |
|-----------|------|----------|-----------|--------------------------|
| **Sunbird** (base de DIKSHA) | https://github.com/Sunbird-Ed/SunbirdEd-portal | **MIT** ✅ | Infraestructura modular de aprendizaje en microservicios: gestión de contenido, autenticación, rutas de aprendizaje, analítica, notificaciones. Portal web + **app Android con consumo offline**. **38.046 commits.** Reconocida **Digital Public Good** por la DPGA. Sostiene **DIKSHA** (India): 180 M+ alumnos, 290.000+ contenidos, 36 idiomas | **Es la única plataforma de escala nacional de esta KB que se puede forkear sin fricción de licencia.** El modelo de adopción *es* el fork: **317 forks contra 41 estrellas**, porque cada estado indio levanta su instancia. El agente va adentro, no al lado. La telemetría ya existe (`sunbird-telemetry-sdk`, MIT) y se conecta con la capa LRS/xAPI del pase 6 |
| **Ed-Fi ODS + API** | https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS | **Apache-2.0** ✅ | Almacén operativo de datos de alumnos (ODS) y su API, más el **Ed-Fi Data Standard** (modelo de datos). Michael & Susan Dell Foundation. **Relicenciado de propietario a Apache-2.0 en abril de 2020** | **En un proyecto K-12 de EE. UU. es anterior al agente.** El expediente longitudinal del alumno vive acá, no en el LMS. Se expone por su API y el agente consume; no se forkea el ODS. Es la pieza que el pase 9 no cubrió: OneRoster mueve matrícula y notas, **Ed-Fi guarda la trayectoria** |

**El criterio de elección entre las tres, que es nuevo en esta KB:**

| Si el cliente es… | Plataforma | Por qué |
|---|---|---|
| Ministerio o sistema educativo público, APAC / LATAM / África | **Sunbird** | MIT, diseñado para forkear por jurisdicción, offline-first en el móvil, multilingüe por diseño (36 idiomas en producción) |
| Distrito o estado de EE. UU., K-12 | **Ed-Fi** primero, LMS después | Apache-2.0, es el estándar de datos que el estado probablemente ya exige |
| Universidad o corporativo | **Moodle / Open edX / OpenOLAT** | Lo que ya estaba en esta KB. La decisión no cambia |

## Capa de contenido y repositorio — agregada en el pase 10 del 2026-10-01

De dónde sale el material que el agente enseña, y con qué licencia. **Leer esta sección antes de prometer un corpus.**

| Plataforma | Repo | Licencia (código) | Qué cubre | Cómo se usa |
|-----------|------|-------------------|-----------|-------------|
| **DSpace** | https://github.com/DSpace/DSpace | **BSD-3-Clause** ✅ | Repositorio institucional (digital asset management). **25.385 commits**, 1.1k ★ / **1.5k forks** | **La pieza permisiva y madura de la capa.** Es donde se guarda el corpus **con su metadato de licencia por ítem**, que es el entregable de **P22** |
| **Pressbooks** | https://github.com/pressbooks/pressbooks | GPL-3.0+ ⚠️ | Autoría de libros abiertos sobre WordPress multisite. Su directorio público declara **7.042 libros** de 186 organizaciones | Desplegar, no forkear. Sirve como *target de salida* de un agente autor |
| **Extractor de LibreTexts** | https://github.com/LibreTexts/shapeshift | **MIT** ✅ | *Extracting and transforming LibreTexts content into various export formats* | **Es lo que un engagement necesita de LibreTexts** — la ingesta del corpus — y es permisivo, aunque la plataforma sea GPL-3.0 |
| **Manifold** | https://github.com/ManifoldScholar/manifold | GPL-3.0 ⚠️ | Publicación académica como obras digitales vivas. 7.305 commits | Igual que Pressbooks: salida, no base |

### ⚠️ Lo que no hay que prometer en esta capa

- **«Usamos contenido abierto de OpenStax, así que no hay problema de licencia.»** Los bundles de OpenStax en GitHub dicen
  **CC BY-NC-SA** en su archivo `LICENSE` (verificado en Calculus, Biology y College Physics: **3 de 3**), mientras el ITS
  que los curó y el servidor MCP que los sirve declaran **CC BY 4.0** en su README. **NonCommercial prohíbe el uso en un
  entregable facturado y ShareAlike obliga a abrir la derivación.** La contradicción está registrada sin resolver en
  `agents/top.md`: `openstax.org` está bloqueado por el proxy (gap 17).
- **Un recomendador o buscador curricular sobre el catálogo de OER Commons.** El **metadato** de ISKME es **NonCommercial**
  por decisión explícita. El contenido puede estar libre y **el catálogo no lo está** (gap 16).
- **Un corpus «mezclado» sin manifiesto.** Un corpus es del color de su ítem más restrictivo, no del promedio.

### El caso limpio, y conviene conocerlo de memoria

**Oak National Academy**: currículo completo bajo **Open Government Licence v3.0**, que permite uso comercial de forma
explícita, y su asistente `Aila` es **MIT**. **Es el único caso de esta KB donde el código y el contenido son los dos
utilizables en un entregable facturado.** ⚠️ Dos reservas: `support.thenational.academy` está **bloqueado por el proxy**
(la licencia viene de prensa británica, no del documento), y hay indicios de **restricción geográfica al Reino Unido** que
hay que confirmar antes de proponer el corpus fuera de UK.

## Capa Apereo — LMS, video y portal de educación superior (ECL-2.0) — agregada en el pase 11 del 2026-10-01

Esta capa no estaba por un error de filtro, no por falta de madurez: **Apereo licencia con ECL-2.0**, que es
Apache-2.0 con la concesión de patentes acotada, aprobada por OSI y FSF y **no copyleft** (ver `repos/foundations.md`).
Son plataformas en producción en universidades de investigación, customizables con AI arriba.

| Plataforma | Repo | Licencia | Stars | Para qué partir de acá |
|---|---|---|---|---|
| **Sakai** | https://github.com/sakaiproject/sakai | **ECL-2.0** ✅ | 1.234 | LMS completo de educación superior en Java, con **dos ramas mantenidas en paralelo** (`25.2` del 2026-06-02 y `23.5` del 2026-06-30) y push del 2026-09-30. Alternativa a Moodle y Canvas **sin la fricción GPL/AGPL del primero y sin el vendor del segundo**. ⚠️ La diferencia que decide: **no tiene un subsistema de AI como el de Moodle 4.5+** — sobre Moodle la AI se configura, sobre Sakai se construye. Eso es trabajo facturable, y también es riesgo de plazo |
| **Opencast** | https://github.com/opencast/opencast | **ECL-2.0** ✅ | 505 | Captura, procesamiento y publicación automatizada de **video de clase** a escala. **Si el entregable incluye transcripción, indexado semántico, búsqueda dentro de la clase grabada o resumen automático, esta es la capa de ingestión y ya existe.** Es la única pieza multimodal de esta KB |
| **uPortal** | https://github.com/uPortal-Project/uPortal | **Apache-2.0** ✅ | 286 | Portal institucional: la superficie donde la universidad ya expone servicios al alumno. **El lugar más barato para montar un agente** — no hay que conseguir que el alumno adopte otra aplicación |
| **OpenLRW** | https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW | **ECL-2.0** ✅ | 62 | *Learning record warehouse* que habla **xAPI + IMS Caliper + IMS OneRoster** a la vez. Complementa la capa de telemetría del pase 6: los LRS de ahí almacenan xAPI; éste además consume Caliper y el roster, que es lo que una universidad realmente tiene |

### ⚠️ Lo que NO hay que proponer en la capa predictiva, y es casi todo

La capa de *early warning* / *student success* es la que el cliente pide por nombre y **no tiene open source
proponible.** Verificado en el pase 11:

| Lo que un cliente va a nombrar | Estado real | Qué decir |
|---|---|---|
| **Apereo Student Success Plan (SSP)** | 🔴 **Sin repositorio localizable.** Rastro público hasta ~2014-2015 (SSP 2.4, Unicon, St. Petersburg College, Sinclair) | No existe como componente. Si el cliente lo menciona, está citando bibliografía de hace una década |
| **Apereo OpenDashboard** | 🔴 `-legacy` declarado *(Deprecated)*; el reemplazo (`-ux` + `-api`) **abandonado un mes después de crearse, en 2020** | No proponerlo ni como base a forkear |
| **Apereo LearningAnalyticsProcessor** | ⚠️ 23 ★, **sin push desde 2023-01** | Sólo como referencia de arquitectura de pipeline |
| **Los 110 repos MIT de dropout prediction** | ⚠️ Techo **6 ★**; el tope entrena con **datos sintéticos**; el más estrellado en absoluto es de 2018 con licencia `NOASSERTION` | Son andamios y notebooks, no productos. Útiles para feature engineering; no para prometer un sistema |
| **Analítica predictiva de Moodle** | ✅ **Existe y es lo más sólido disponible:** la *Analytics API* del core define modelos como *indicadores + target*, los evalúa y entrena internamente, con el target de alumno en riesgo incluido. GPL-3.0 (es el core de Moodle) | **Es la respuesta correcta a esta necesidad hoy.** Se extiende por los puntos de extensión del core y la lógica propietaria vive afuera (ver la nota de licencias en `repos/foundations.md`) |

**La regla de esta capa:** cuando el cliente pide *early warning*, **la base es la Analytics API de Moodle o el
pipeline propio sobre OpenLRW**, nunca un repo de la capa predictiva de GitHub. Y el entregable que se vende no es el
modelo: es el **expediente de conformidad** del modelo, porque el Anexo III lo exige. Ver el patrón **P25**.

### Y la pieza que vuelve defendible cualquier propuesta de esta capa

| Plataforma | Repo | Licencia | Stars | Para qué |
|---|---|---|---|---|
| **Terracotta** | https://github.com/terracotta-education/terracotta | **Apache-2.0** ✅ | 21 | Plug-in de LMS para **ensayos controlados aleatorizados dentro del aula**: variantes de tratamiento por tarea, asignación al azar, **consentimiento informado oculto al docente**, filtrado de no-consintientes en los reportes y remoción de identificadores en las exportaciones. 2.572 commits, push del 2026-09-30 |

**Por qué importa comercialmente y no sólo metodológicamente:** todo proyecto de esta capa se vende prometiendo que
la intervención reduce el abandono, y **casi ninguno puede probarlo** porque no hay grupo de control. Terracotta trae
el diseño experimental *y* la protección de datos del comité de ética ya resueltos. Convierte un entregable de
opinión en un entregable con evidencia, y el costo de agregarlo es un plug-in.

## Capa de repetición espaciada (SRS) desplegada — agregada en el pase 12 del 2026-10-01

Once pasadas registraron el LMS (Moodle, Open edX, Sakai, Canvas), el SIS (OpenSIS, RosarioSIS, GegoK12), el
autograding, la telemetría, el video y el portal. **Ninguna registró la pieza que el alumno abre todos los días por
decisión propia:** el sistema de repetición espaciada. Es la única plataforma de esta KB cuya adopción no la decide la
institución.

### La plataforma, verificada el 2026-10-01

| Plataforma | Repo | Licencia | Stars | Qué es | Superficie de customización |
|---|---|---|---|---|---|
| **Anki** | https://github.com/ankitects/anki | **AGPL-3.0-or-later** ⚠️ (porciones de contribuyentes bajo BSD-3; verificado en el archivo `LICENSE`, no en el README) | **31.7k** | El SRS de facto: active recall + repetición espaciada. Rust + Python + TypeScript. **+3 M de usuarios sólo en Android** | **AnkiConnect** (add-on, v25.11.9.0 del 2025-11-02): API HTTP local sobre la que hablan las integraciones externas |
| **anki-mcp-server** | https://github.com/ankimcp/anki-mcp-server | **MIT** ✅ | **499** | Puente MCP: crear, leer y revisar mazos en lenguaje natural desde un agente. TypeScript, v0.22.0, 254 commits | Es él mismo la capa de integración |

### 🔴 La condición de licencia, y es la que decide si esto se puede proponer

**Anki es AGPL-3.0-or-later.** Eso, en el resto de esta KB, sería motivo de advertencia fuerte (ver la «Nota sobre
licencias» en `repos/foundations.md`). Acá no lo es, y la razón es arquitectónica, no legal-creativa:

- **No se forkea Anki ni se enlaza contra su código.** Se le habla por **AnkiConnect**, que es una API HTTP sobre
  `localhost`, desde un **proceso separado** (`anki-mcp-server`, MIT).
- Esa es exactamente la regla 2 que esta KB ya tenía escrita: *«la lógica propietaria vive en un servicio aparte — el
  agente es un proceso separado con su propia licencia, hablando por API/MCP»*.
- **Anki corre en la máquina del alumno, no en infraestructura del cliente.** No hay distribución de un derivado y no
  hay servicio de red operado por el cliente: los dos disparadores de la AGPL quedan afuera.

⚠️ **Lo que sí hay que revisar con legal:** empaquetar, redistribuir o preinstalar Anki (o un derivado, o un *fork* con
marca del cliente) como parte del entregable. Ahí la AGPL aplica de lleno. Proponerlo como **cliente que el alumno ya
tiene instalado** es otra cosa.

### Por qué esta capa conecta con dos piezas que la KB ya tenía sueltas

1. **`py-fsrs` (MIT) ya estaba en `agents/top.md` y no tenía dónde enchufarse.** FSRS —el *Free Spaced Repetition
   Scheduler*, que reemplaza a SM-2— **está integrado en Anki desde la versión 23.10 (2023)** como opción del
   programador. Es decir: el algoritmo moderno que esta KB venía citando **ya está desplegado en millones de
   dispositivos**, y `py-fsrs` sirve para razonar/simular del lado del servidor, no para reimplantarlo.
2. **La capa MCP de mastery del pase 5 tenía techo de 1 ★.** Sus cinco repos inventan grafo, scheduler y esquema
   propios. `anki-mcp-server` (499 ★) no inventa nada: expone el que ya existe. **Es la corrección práctica del gap 5.**

### Cómo se propone, en una línea

Como **capa de retención del alumno** encima de cualquiera de los LMS de esta KB: el LMS acredita, el agente enseña, y
**Anki es donde el conocimiento se queda** — sin que el cliente opere un servidor más. Ver el patrón **P28**.

## Capa de publicación de competencias conforme a CASE — agregada en el pase 14 del 2026-10-01

Esta es la capa que convierte «tenemos el currículo en un JSON» en «el currículo está publicado en un endpoint que
cualquier herramienta educativa certificada puede consumir». El estándar es **CASE® (1EdTech)** y hay tres servidores
open source, uno de ellos certificado este año.

| Plataforma | Licencia | ★ | Stack | Cuándo proponerla |
|---|---|---|---|---|
| [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) | **Apache-2.0** ✅ | 9 | Servidor + editor visual, multi-tenant | ✅ **Opción por defecto.** Es del organismo de estándares y está **certificado para CASE Service v1.0 y CASE v1.1 (2026-02-17)**. Cuando el entregable tiene que pasar una auditoría de conformidad |
| [`infosign/compeito`](https://github.com/infosign/compeito) | **Apache-2.0** ✅ | 3 | Python 3.12 / FastAPI / PostgreSQL / HTMX / Docker | ✅ Cuando el equipo del cliente es Python y hay que **importar** marcos existentes: lee CFPackages de OpenSALT y OpenCASE, e importa/exporta CSV compatible OpenSALT |
| [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | **MIT** ✅ | 45 | PHP / Symfony / MySQL / Docker | ⚠️ Cuando pesa la **autoría y el *crosswalk*** con interfaz madura y el cliente ya es PHP. **Su último estable (3.2.0, sept 2023) apunta a CASE v1.0**; v1.1 está en `develop` |

### 🔴 La regla de selección de esta capa, y contradice el criterio del resto de la KB

**Acá no se elige por estrellas: se elige por fecha de certificación.** OpenSALT tiene **5× más estrellas** que
OpenCASE y está **una versión mayor del estándar más atrás**. Si el cliente necesita CASE v1.1 —y lo necesita si va a
interoperar con herramientas certificadas recientes— la elección es OpenCASE o `compeito`, y OpenSALT entra sólo como
herramienta de autoría.

Es la tercera capa de esta KB donde la popularidad apunta a la pieza equivocada (Sunbird con 41 ★ en el pase 10,
Apereo en el pase 11). **Conviene tratarlo como regla y no como anécdota.**

### La pieza que vuelve auditable cualquier propuesta de esta capa, y de otras cuatro

[`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) — **MIT**, 2 ★. Verifica conformidad contra
**once** estándares: CASE 1.1, xAPI (1.0.3 e IEEE 2.0), QTI 2.1/2.2/3.0.1, LTI 1.3 con *Deep Linking*, AGS, NRPS y
*Proctoring*, OneRoster 1.2, Common Cartridge 1.3/1.4, CLR 2.0, Open Badges 3.0, Caliper 1.2, cmi5 y W3C Verifiable
Credentials 2.0.

**No es una pieza de esta capa: es la pieza de cinco capas de esta KB a la vez** — telemetría (pase 6), credenciales
y evaluación QTI (pase 9), SIS/OneRoster (pases 2-3) y currículo (este pase). Convierte el *due diligence* de
interoperabilidad del patrón **P21** de revisión manual en *pipeline* ejecutable. **Con 2 ★ se usa con el commit
pineado, pero se usa.**

---

## Capa de lectura oral — agregada en el pase 14 del 2026-10-01

No hay una «plataforma» de lectura oral open source desplegable, y conviene decirlo así en vez de inventarla.
**Lo que hay es un componente y un *toolkit*:**

| Pieza | Licencia | ★ | Rol |
|---|---|---|---|
| [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | **MIT** ✅ | 85 | **Componente de evaluación.** Se despliega autoalojado como reemplazo de Azure Pronunciation Assessment. Corre local: puntaje, PER/WER, confianza por palabra, DTW y prosodia |
| [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | **Apache-2.0** ✅ | 15.5k | **Infraestructura ASR.** Para cuando hay que entrenar o adaptar modelos a un idioma o a voz infantil |

### ⚠️ Lo que no hay que prometer en esta capa

- **No hay plataforma.** No existe el «Moodle de la lectura oral». Lo que se propone es un componente dentro del
  LMS o de la app del cliente, no un sistema llave en mano.
- **No hay corpus permisivo en español ni en portugués.** El de referencia (`speechocean762`, 198 ★) es inglés con
  L1 mandarín **y no tiene archivo de licencia**. **No prometer cifras de precisión para un despliegue en LATAM**
  basadas en resultados publicados sobre ese corpus: hay que recalibrar con datos locales, y eso es alcance y
  presupuesto propios.
- **La pieza más fina de la región no se puede usar.** `carrera-lectora` (Chile, 1.º-4.º básico, PPM y exactitud,
  procesamiento en dispositivo) **no tiene licencia**. No proponerla; a lo sumo, pedir que la pongan.

## Capa de privacidad y datos sintéticos — agregada en el pase 16 del 2026-10-01

No es una plataforma vertical: es la capa que decide si las plataformas de arriba pueden procesar dato real de
menores. Se incluye acá porque **se propone junto con la plataforma, no después**.

| Pieza | Licencia | ★ | Cuándo se propone |
|---|---|---|---|
| **PySyft** | Apache-2.0 ✅ | 10.0k | El dato **no puede salir** de la institución y hay varias instituciones. El cómputo viaja al dato |
| **Flower** | Apache-2.0 ✅ | 7.2k | Entrenar un modelo across escuelas/campus **sin centralizar interacciones**. La categoría se consolidó acá: OpenFL se deprecó y remite a Flower por nombre |
| **OpenDP** | MIT ✅ | 437 | Hay comité de ética, DPO o regulador que va a pedir garantía **formal**. Es de Harvard y eso pesa en el expediente |
| **Opacus** | Apache-2.0 ✅ | 2.0k | Ya hay un pipeline PyTorch y hay que agregarle DP sin rehacerlo |
| **diffprivlib** | MIT ✅ | 920 | Prototipar y **medir el costo de utilidad** de DP antes de comprometerse |
| **synthcity** | Apache-2.0 ✅ | 687 | Hace falta un dataset para desarrollar, demostrar o **licitar** sin tocar dato real. Trae DP-GAN/PATEGAN y métricas de privacidad y utilidad |

### 🔴 Lo que NO hay que proponer en esta capa

- **`SDV` (Synthetic Data Vault), por mucho que el cliente lo nombre.** 3.6k ★ y origen en el **Data to AI Lab del
  MIT**, pero hoy es **Business Source License 1.1** de **DataCebo, Inc.** — no aprobada por OSI. Prohíbe el uso en
  producción sin licencia comercial y excluye explícitamente usarlo *«for a Synthetic Data Service»*, definido como
  toda oferta comercial que dé a terceros acceso a sus capacidades de generación de datos sintéticos. **Eso
  describe el trabajo de un studio.** Revierte a MIT cuatro años después de cada release. Alternativa directa:
  **`synthcity`**.
- **`OpenFL` como base nueva.** Apache-2.0 y 843 ★, pero su propia página declara que **ya no está en desarrollo
  activo y que será archivado**, recomendando migrar a Flower. Si el cliente ya lo tiene, el camino es la guía de
  migración; si se elige de cero, no hay motivo.
- **Los tres repos educativos sin licencia** (`SynEdu-HEDL`, `federated-deep-knowledge-tracing`,
  `FedGNN-for-Personalized-Knowledge-Tracing`). Sirven como **referencia de arquitectura** — `FedGKT` es la mejor
  que hay, y ya corre sobre Flower — pero sin licencia declarada no son dependencia de producto.
- **`ydata-synthetic` por la ruta vieja.** Es MIT, pero el paquete **migró**: hay que seguir la guía de migración
  del README, no instalar el nombre viejo.

### La regla de esta capa, y es distinta a la del resto de la KB

En las demás capas de esta KB la regla es *lo maduro es copyleft y lo permisivo no tiene tracción*. **Acá se
invierte: lo maduro es permisivo** —Apache-2.0 y MIT, de Harvard, Google, Meta e IBM— **y lo que falta no es
licencia sino integración con el dato educativo**. El techo de lo específicamente educativo es de **10 estrellas**,
y el único permisivo del grupo tiene **3**.

Eso convierte esta capa en la de mejor relación esfuerzo/defensa de toda la KB: la infraestructura no se construye,
se conecta.

## Cómo elegir

| Si el cliente necesita… | Arrancar de |
|-------------------------|-------------|
| LMS estándar, presupuesto acotado, AI ya integrable | **Moodle** (AI subsystem nativo) |
| **Sistema educativo nacional / ministerio (APAC, LATAM, África)** | **Sunbird** — MIT, pensado para forkear por jurisdicción *(pase 10)* |
| **Distrito o estado de EE. UU., K-12** | **Ed-Fi ODS + API** (Apache-2.0) antes que el LMS *(pase 10)* |
| **Corpus curricular con licencia auditable** | **DSpace** (BSD-3) + `shapeshift` (MIT) + manifiesto por ítem — ver **P22** *(pase 10)* |
| Cursos a escala / MOOC / academia corporativa | **Open edX** + XBlock |
| Código propietario encima, sin fricción de licencia | **Oppia**, **OpenOLAT**, **Kolibri** o **Richie** |
| Operar sin internet confiable | **Kolibri** o **Project NOMAD** + Ollama |
| Gestión administrativa (admisiones, matrícula, notas) | **OpenEduCat** |
| SIS liviano para K-12, sin ERP completo | **RosarioSIS** o **openSIS** (los dos GPL — aislar el agente) |
| SIS donde el agente pueda vivir **adentro** como plugin, sin fricción de licencia | **GegoK12** (MIT) — verificar antes si el alcance necesita los módulos Pro de exámenes o fees |
| Evaluación que va a caer en Annex III del EU AI Act | **OpenOLAT** (permisivo + assessment auditable) |
| Autograding de código a escala, con AI sólo en el feedback | **Autograder.io** (determinista) + capa de explicación encima *(pase 5)* |
| Herramienta para **docentes** (no para alumnos) | Referencia de arquitectura: **Aila** (MIT). Producto desplegable: **Claw-ED** (MIT, local-first) *(pase 5)* |

## Cómo customizar con AI

1. **No forkear el core copyleft.** Usar el punto de extensión: plugin del AI subsystem (Moodle), XBlock (Open edX), LTI 1.3 (Canvas).
2. **El agente es un servicio aparte.** Proceso propio, licencia propia, hablando por API o MCP. Esto mantiene la lógica de negocio fuera del alcance de GPL/AGPL.
3. **Conectar los datos que la plataforma ya tiene** — progreso, intentos, submissions, transcripciones — al estado del aprendiz. Es la ventaja que un chatbot genérico no puede replicar.
4. **Agregar scheduling de retención** (`py-fsrs`) para que el sistema no sólo explique sino que haga recordar.
5. **UI conversacional encima**, no en lugar de, los flujos existentes. Los docentes rechazan el reemplazo y aceptan el asistente.
6. **Medir antes de entregar, y medir seguridad pedagógica además de exactitud** *(agregado en el pase 5)*. Un tutor que acierta y a la vez revela la respuesta antes de tiempo o le da la razón al alumno equivocado está fallando en lo que importa. Correr `EduBench` (MIT, transversal a materia) y `SafeTutors` (MIT, 11 dimensiones de daño) contra el agente **antes** de la entrega, y guardar el resultado: en un cliente regulado eso no es QA, es el expediente. Ver el patrón **P11**.
7. **Verificar la licencia del *contenido*, no sólo la del código** *(agregado en el pase 10)*. Son dos licencias
   distintas y en esta capa casi nunca coinciden. Se lee el **campo de licencia del ítem** —no el badge del repo ni el
   README— y se guarda junto al ítem. Esta KB tiene el caso verificado: los bundles de OpenStax en GitHub dicen
   **CC BY-NC-SA** en su `LICENSE` mientras dos repos que los consumen declaran **CC BY 4.0** en su README. Ver **P22**.
8. **Separar la nota del modelo.** Donde haya calificación, que la decisión la tome un componente determinista (test, rúbrica, checker) y que el LLM explique. Es lo que hace `mentar` con su checker, lo que hace Autograder.io por diseño, y lo que exigen las jurisdicciones que prohíben el grading automático.

---
*Ver `compose/patterns.md` para las recetas concretas con repos y tiempos.*
