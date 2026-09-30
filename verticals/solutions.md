---
industry: education
region: Global
updated: 2026-09-30
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
