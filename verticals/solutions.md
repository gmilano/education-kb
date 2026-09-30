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

11 plataformas reales verificadas, más 3 en la capa SIS agregadas en la segunda pasada del 2026-09-30. El equivalente educativo de "Odoo para ERP" es **Moodle**: dominante, extensible, y desde 2026 con subsistema AI nativo.

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

## Capa SIS — el lado administrativo, verificado 2026-09-30 (pase 2)

Un LMS gestiona el aprendizaje; un **SIS** (Student Information System) gestiona la institución: matrícula, legajos, asistencia, notas oficiales, facturación, disciplina. Es donde viven los datos que más valen para un agente y el área que casi ningún piloto de AI toca.

| Plataforma | Licencia | URL | Stack | Cobertura | Nota |
|------------|----------|-----|-------|-----------|------|
| **OpenEduCat** | LGPL-3.0 | https://github.com/openeducat/openeducat_erp | Python (Odoo) | ERP educativo completo: admisiones, matrícula, asistencia, exámenes, biblioteca | Sigue siendo la primera opción: corre como módulos Odoo, así que hereda todo el ecosistema Odoo |
| **RosarioSIS** | GPL-2.0 ⚠️ | https://github.com/francoisjacquet/rosariosis | PHP | Legajos, notas, horarios, asistencia, facturación, disciplina, comedor | 644 ★. Modular y mantenido. GPL-2.0: copyleft, **no** es AGPL, así que no alcanza el uso en red |
| **openSIS Classic** | GPL ⚠️ | https://github.com/OS4ED/openSIS-Classic | PHP (Apache + MySQL) | K-12, escuelas técnicas y superior: datos de alumnos y staff, horarios, asistencia, notas, reportes | 343 ★. La Community Edition es GPL; OS4ED vende ediciones comerciales encima |

**Lectura de esta capa:** el SIS open source es **PHP y copyleft**, sin excepción útil. No hay un SIS permisivo y vivo. Consecuencia práctica: el agente nunca se construye *dentro* del SIS — se construye al lado y lee por API/DB con un servicio propio. Es el mismo patrón que ya aplica para Moodle y Canvas, y acá no es una preferencia de arquitectura sino la única opción limpia.

### ⚠️ Fedena — dead end verificado, no proponer

`projectfedena/fedena` (Apache-2.0, 547 ★, 559 forks, Ruby on Rails) aparece recomendado en prácticamente todo listicle de "open source school ERP", y **su licencia permisiva lo hace tentador** frente al resto de la capa SIS, que es toda copyleft.

**Está muerto. El último commit es del 2016-07-20**, y los dos últimos son "emptying content" y "deleting unwanted pids files" — o sea, el propio Foradian lo vació. Antes de eso, actividad de enero de 2013.

Un Rails de 2013/2016 significa Ruby y Rails fuera de soporte, dependencias con CVEs sin parchear y cero upstream para reportar nada. La proporción forks/stars casi 1:1 (559/547) es la firma de un repo que la gente clona para desplegar y nunca contribuye de vuelta.

**Se registra explícitamente como dead end** porque el modo de falla es concreto: alguien busca "SIS con licencia permisiva", encuentra Apache-2.0 y 547 ★, y lo propone sin ver la fecha. Si hace falta SIS permisivo, hoy **no existe** — hay que ir a OpenEduCat (LGPL-3.0) y aislar el agente, o construir la capa de datos propia.

## Cómo elegir

| Si el cliente necesita… | Arrancar de |
|-------------------------|-------------|
| LMS estándar, presupuesto acotado, AI ya integrable | **Moodle** (AI subsystem nativo) |
| Cursos a escala / MOOC / academia corporativa | **Open edX** + XBlock |
| Código propietario encima, sin fricción de licencia | **Oppia**, **OpenOLAT**, **Kolibri** o **Richie** |
| Operar sin internet confiable | **Kolibri** o **Project NOMAD** + Ollama |
| Gestión administrativa (admisiones, matrícula, notas) | **OpenEduCat** |
| SIS liviano para K-12, sin ERP completo | **RosarioSIS** o **openSIS** (los dos GPL — aislar el agente) |
| Evaluación que va a caer en Annex III del EU AI Act | **OpenOLAT** (permisivo + assessment auditable) |

## Cómo customizar con AI

1. **No forkear el core copyleft.** Usar el punto de extensión: plugin del AI subsystem (Moodle), XBlock (Open edX), LTI 1.3 (Canvas).
2. **El agente es un servicio aparte.** Proceso propio, licencia propia, hablando por API o MCP. Esto mantiene la lógica de negocio fuera del alcance de GPL/AGPL.
3. **Conectar los datos que la plataforma ya tiene** — progreso, intentos, submissions, transcripciones — al estado del aprendiz. Es la ventaja que un chatbot genérico no puede replicar.
4. **Agregar scheduling de retención** (`py-fsrs`) para que el sistema no sólo explique sino que haga recordar.
5. **UI conversacional encima**, no en lugar de, los flujos existentes. Los docentes rechazan el reemplazo y aceptan el asistente.

---
*Ver `compose/patterns.md` para las recetas concretas con repos y tiempos.*
