---
industry: education
region: Global
updated: 2026-10-01
---

# 🏭 Verticales de partida — Education

> Plataformas verticales reales, en producción, customizables con AI.
> Modelo: partir de algo que ya funciona y que ya tiene los datos, y agregar la capa agéntica arriba.
> Verificado vía WebFetch el 2026-09-30.

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

## Cómo elegir

| Si el cliente necesita… | Arrancar de |
|-------------------------|-------------|
| LMS estándar, presupuesto acotado, AI ya integrable | **Moodle** (AI subsystem nativo) |
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
7. **Separar la nota del modelo.** Donde haya calificación, que la decisión la tome un componente determinista (test, rúbrica, checker) y que el LLM explique. Es lo que hace `mentar` con su checker, lo que hace Autograder.io por diseño, y lo que exigen las jurisdicciones que prohíben el grading automático.

---
*Ver `compose/patterns.md` para las recetas concretas con repos y tiempos.*
