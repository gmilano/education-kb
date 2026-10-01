---
industry: education
region: Global
updated: 2026-10-01
---

# 📈 Repos trending — education

> **APPEND-ONLY.** Cada corrida agrega una sección fechada arriba y conserva la historia abajo.

## 2026-10-01 (pase 26) — el eje conector rinde por segunda vez: el conector MIT de 102 tools, la biblioteca permisiva que veinticinco pasadas no buscaron, y dos capas que se buscaron y salieron vacías

**7 repos verificados de primera mano, 6 nuevos para esta KB** (el re-verificado es `learnmcp-xapi`). Uno entra en la
tabla principal de `agents/top.md` — **se corta la racha de siete pases sin altas**.

| Repo | Licencia | ★ | Forks | Commits | Señal | Por qué importa |
|------|----------|---|-------|---------|-------|-----------------|
| https://github.com/vishalsachdev/canvas-mcp | **MIT** ✅ | **269** | 92 | 815 | El conector permisivo de LMS más grande de esta KB | **Hasta 102–103 tools** + 8 *agent skills*. Alumno **y docente**. `search_canvas_tools` para descubrimiento. *Learning Designer* con **chequeo WCAG** |
| https://github.com/folio-org/platform-complete | **Apache-2.0** ✅ | 15 | 27 | **3.096** | Ensamblado de plataforma de un consorcio de bibliotecas | **Abre la capa biblioteca/ILS**, permisiva y grande. Fija el conjunto compatible de releases + infra Docker |
| https://github.com/folio-org/mod-inventory | **Apache-2.0** ✅ | 4 | 15 | **2.402** | Módulo núcleo de FOLIO | Inventario (*instances*/*holdings*/*items*), **Kafka**, **MARC**, *authority linking*, **multi-tenant** |
| https://github.com/cassproject/CASS | **Apache-2.0** ✅ | 62 | — | — | **Cartucho MCP ejecutado** | **6 tools + 3 resource templates medidos.** `record_evidence` + `get_learner_profile` = los dos pasos de **P48**. Cierra el **gap 40** |
| https://github.com/macewan-cs/lti | **MIT** ✅ | 8 | 2 | 89 | Candidato *platform-side* **refutado** | Go, MIT — pero *«partially implements»* y **es tool-side**. El resumen de búsqueda sugería el lado LMS; la página dice que no |
| https://github.com/csmediapro/moodle-mcp-server | 🔴 **AGPL-3.0** | **0** | **0** | 57 | **Corrección de licencia** | Único conector MCP de Moodle. **Open-core:** 10 tools de lectura abiertos, *Reporting*/*Analytics*/*Directory*/*Compliance* **premium aparte** |
| https://github.com/DavidLMS/learnmcp-xapi | **MIT** ✅ | 15 | 4 | 32 | **Re-verificado: no se movió** | Idénticos ★ y commits que en el pase 6. La ficha era correcta, y el estancamiento confirma su propia advertencia |

### Lo que el eje conector devolvió por estándar, incluidos los vacíos

El pase 25 mandó cruzar `MCP server` con cada estándar inventariado. **Resultado, estándar por estándar:**

| Estándar | Resultado | Qué se registra |
|----------|-----------|-----------------|
| **xAPI** | ✅ `learnmcp-xapi` (MIT) | Ya estaba desde el pase 6. Re-verificado |
| **LTI** | ✅ `canvas-mcp` (MIT), `moodle-mcp-server` (AGPL) | Vía conectores de LMS, no del estándar en sí |
| **CASE** | 🔴 **nada verificable** | **Y el término colisiona:** la búsqueda se llena de *certificaciones* de MCP (MCPA del Linux Foundation, certs de Claude). **Segunda colisión de término medida por esta KB**, después de `education` = «cursos sobre AI» |
| **OneRoster** | 🔴 **nada** | Ni un repo. Declarado como vacío, no como no buscado |
| **QTI** | 🔴 **nada verificable** | Apareció un *Question Bank MCP Server* listado en Glama **sin repo de GitHub localizable**. **No se registra como hallazgo** (gap **44**) |

### Las dos capas que se buscaron por consigna y salieron sin permisivo

- **Admisiones:** `openSIS-Classic` (**GPL**) y **OpenEduCat** (**LGPL-3.0**) son lo que sirve, y ya estaban. Lo
  permisivo que apareció —`CollinsTatang/admissionSystem` (MIT), `OrgSchool-portfolio-project`— son **proyectos de una
  persona**, con «portfolio-project» en el nombre de uno de ellos. **No hay plataforma de admisiones permisiva y
  productiva** (gap **46**).
- ***Student success* / alumni:** **FlightPath Academics** (PHP, **GPLv3+**, liberada el **2013-03-13**, *early alerts*
  y *Academic Priority*) **no tiene repo en GitHub**; **Student Success Plan** (Unicon) y el *dashboard* de **Marist
  College** tienen referencias verificables sólo de **2013–2014**. 🔴 **Es la capa más vieja y peor abastecida de esta
  KB — y la que más presión regulatoria tiene encima** (Annex III, prohibiciones de Oklahoma y Maryland sobre la
  decisión autónoma acerca del alumno). Gap **47**, tendencia **68**.

### Nota de método: por qué acá no se verifica con `curl -sI`

**`curl -sI` contra `github.com` devuelve `403` para todas las URLs en esta sesión**, incluidas las que existen y están
en esta KB desde el pase 1 — el proxy de egreso corta el `HEAD`. Verificar con `curl` acá **fabricaría 404s falsos sobre
repos reales**, que es justamente el error que la consigna quiere evitar. **Toda verificación de este pase se hizo con
WebFetch sobre la página del repo**, leyendo licencia, ★, forks y commits de la página. Y una advertencia sobre el
umbral de estrellas: **FOLIO tiene 15 ★ y 3.096 commits.** Para software de consorcio las estrellas miden moda y los
commits miden vida — **no aplicar el umbral de estrellas a infraestructura institucional.**

## 2026-10-01 (pase 25) — la consigna del pase 24 rindió el haul más grande del eje artefacto, y corrigió dos conclusiones que el pase 24 había escrito con confianza: el repo que declaró 404 existe, y el lado *platform* sí es permisivo

**18 repos verificados de primera mano, 17 nuevos para esta KB** (el único ya conocido es `amp-up-io/qti3-item-player`, re-verificado para comparar con el QTI 3 nuevo). Ninguno es un agente —`agents/top.md` sigue en
37 filas, van **siete** pases sin altas— pero este pase **no vino a contar filas: vino a ejecutar los cuatro artefactos y
los tres estándares que el pase 24 dejó sin barrer**, y los barrió todos. Dos de los resultados son correcciones a este
mismo archivo.

### 🔴 Corrección 1 — el repo que el pase 24 declaró inexistente existe, y tiene exactamente lo que la consigna pedía

El pase 24 escribió, en la tabla de no-hallazgos de esta misma sección: *«`github.com/LongsightGroup/qti3-core` → **404**
[…] para esta KB **QTI 3 sigue siendo `amp-up-io/qti3-item-player`**»*. **Es un falso negativo, y la causa es nombrar el
paquete npm en vez del repo.** `@longsightgroup/qti3-core` es uno de los paquetes publicados; el repo es el monorepo
`qti3`, sin sufijo:

| | Lo que el pase 24 concluyó | Lo que el pase 25 midió |
|---|---|---|
| **¿Existe el QTI 3 de Longsight?** | «404. El repo con ese nombre no existe» | ✅ **https://github.com/LongsightGroup/qti3** — **MIT**, 5 ★, 2 forks, TypeScript, **667 commits**, **12 paquetes publicados** |
| **¿Hay *item bank* open source?** | Pregunta abierta de la consigna del pase 25 | ✅ **Sí, y es de este repo:** *«framework-neutral QTI-shaped authoring XML and **item-bank package writer** with typed diagnostics»* |
| **¿Hay camino desde QTI viejo?** | No registrado | ✅ **Migración `QTI 1.2` y `QTI 2.x` → ítems de autoría QTI 3**, en paquete propio |
| **¿Cuál es *el* QTI 3 de la KB?** | `amp-up-io/qti3-item-player`, único certificado | **Los dos, y no compiten: se complementan** (ver abajo) |

**El reparto, medido pieza por pieza, y es la distinción que se vende:**

| | `amp-up-io/qti3-item-player` *(ya en la KB)* | `LongsightGroup/qti3` *(nuevo)* |
|---|---|---|
| Licencia | **MIT** ✅ | **MIT** ✅ |
| ★ / forks | **30** / 6 | 5 / 2 |
| Certificación 1EdTech | ✅ **QTI 3 Basic *y* Advanced «Delivery»** | 🚫 *«The project is not certified»*, dicho por el propio README |
| Qué hace | **Sólo entrega/render.** Sin autoría ni banco de ítems | **Parseo, validación, render, *scoring*, estado, autoría, *item bank* y migración** |

🔵 **La consecuencia práctica:** el certificado sabe **entregar** y no sabe **crear**; el nuevo sabe **crear, bancar y
migrar** y no está certificado. Una propuesta que necesite las dos cosas usa los dos, y **declara cuál de los dos lleva el
sello** — porque el sello aplica a la entrega, que es lo que el cliente audita. Ver el patrón **P48**.

### 🔴 Corrección 2 — el lado *platform* de LTI no es «intención sin licencia»: hay una implementación MIT con el juego completo de servicios

El pase 24 cerró así: *«las dos únicas piezas platform-side aparecieron en este pase — **una de ellas sin licencia
declarada**. Un stack que sólo sabe ser herramienta no puede proponer el lado LMS.»* El diagnóstico del hueco era
correcto; **la conclusión de que no había con qué llenarlo, no.**

| Repo | Licencia | ★ | Forks | Lenguaje | Lado | Qué implementa | Región |
|---|---|---|---|---|---|---|---|
| https://github.com/LtiLibrary/LtiAdvantagePlatform | **MIT** ✅ | **35** | 18 | C# | 🔵 **platform** | *«Sample LTI 1.3 / LTI Advantage platform built with ASP.NET Core»*. **AGS v2** (line items, results, scores), **NRPS v2** (membresías), **Deep Linking 2.0**, launches con y sin contexto de curso. Stack **ASP.NET Core 10** + OpenIddict 7.x | sin ubicar (org `LtiLibrary`) |
| https://github.com/Citolab/lti-1p3-platform-example | ⚠️ **GPL-3.0** | 0 | 0 | C# | 🔵 **platform** | API mínima .NET que **acuña y firma el `id_token`** + página React para generar URLs de *launch*. Endpoints `/lti/auth`, `/lti/jwks`, `/api/generateLtiUrl`. *«the platform side end to end»* | EMEA ⚠️ *inferida* (Citolab = laboratorio de **Cito**, instituto de evaluación neerlandés) |
| https://github.com/oat-sa/lib-lti1p3-core | ⚠️ **GPL-2.0** | **37** | 22 | PHP | 🔵 **platform *y* tool** | *«PHP library for LTI 1.3 Core implementations as platforms and / or as tools»*. **Certificada por IMS/1EdTech:** *LTI 1.3 Advantage Complete* **y *LTI 1.3 Proctoring Services*** | EMEA (Open Assessment Technologies) |

🔵 **Lo que cambia para una propuesta:** el lado LMS **sí se puede construir con licencia permisiva, y el stack es .NET**
(`LtiAdvantagePlatform`, MIT, con AGS+NRPS+Deep Linking). La pieza **certificada** del lado *platform* existe pero es
**GPL-2.0** (`oat-sa`), así que la elección ya no es «hay o no hay» sino **«permisivo sin sello (MIT/.NET) o sello con
copyleft (GPL-2.0/PHP)»** — y eso es una decisión de cliente, no de esta KB. La pieza de la UOC que el pase 24 encontró
sin licencia (`java-lti-1.3-platform`) deja de ser la única opción y pasa a ser la peor de las tres.

### 🔴 Y el sesgo de stack era peor de lo que el pase 24 midió: faltaba la librería LTI con más estrellas de todas

El pase 24 encuadró el problema como *«toda la capa LTI de esta KB era PHP, y ahora hay Java»*. **Medido este pase, la
capa tiene cinco stacks y el que faltaba no era un stack marginal: era el líder por estrellas, y por 3×.**

| Repo | Licencia | ★ | Forks | Stack | Lado | Nota | Región |
|---|---|---|---|---|---|---|---|
| https://github.com/Cvmcosta/ltijs | **Apache-2.0** ✅ | **373** | **86** | Node / TypeScript | tool | *«Easily turn your web application into a LTI® 1.3 Learning Tool»*. Launches, **Deep Linking, AGS, NRPS y Dynamic Registration**. **Es la librería LTI más traccionada que vio esta KB** | sin ubicar |
| https://github.com/dmitry-viskov/pylti1.3 | **MIT** ✅ | **138** | 83 | Python | tool | `PyLTI1p3`, LTI 1.3 Advantage. Adaptadores **Django** y **Flask** (`DjangoOIDCLogin`, `FlaskMessageLaunch`); 178 commits. FastAPI **no** viene hecho | sin ubicar |
| https://github.com/3iPunt/wordpress-lti-1-3 | **Apache-2.0** ✅ | 6 | 3 | PHP (WordPress) | tool | LTI 1.3 Advantage **como plugin de WordPress**: SSO, roles de membresía y notas. 54 commits. Nacido en el **IMS Europe Summit 2018** | EMEA ⚠️ *inferida* (3iPunt) |

**El dato incómodo, y conviene escribirlo sin suavizar:** esta KB recomendó `1EdTech/lti-1-3-php-library` (Apache-2.0,
124 ★) **en cinco archivos, incluidos P20, P21 y `verticals/solutions.md`**, durante seis pases. `ltijs` tiene
**373 ★ — tres veces más — y la misma licencia permisiva**, y nunca apareció porque las búsquedas de esta KB entraban por
*«LTI PHP»* y por *«LTI Java»*, nunca por *«LTI»* sin stack. **No es que la pieza recomendada esté mal: es que se la eligió
sin ver el campo.** Y con `PyLTI1p3` (MIT, 138 ★) el campo permisivo queda así: **Node 373 ★ > Python 138 ★ > PHP 124 ★ >
Java 21 ★**.

### El artefacto `timetable`: la pieza permisiva grande que esta KB nunca tuvo

| Repo | Licencia | ★ | Forks | Lenguaje | Qué es | Región |
|---|---|---|---|---|---|---|
| https://github.com/UniTime/unitime | **Apache-2.0** ✅ | **349** | **213** | Java | *«Comprehensive University Timetabling System»*. **Horarios de cursos *y* de exámenes**, *event management* con salas compartidas, **asignación de alumnos a clases** y *scheduling* de docentes. Sistema **distribuido**: varios gestores departamentales coordinan un mismo horario | North America ⚠️ *inferida* (origen universitario EE. UU.) |
| https://github.com/manceras/horarios-escolares-manager | **MIT** ✅ | 0 | 0 | Python (FastAPI) + React/TS | Planificador de horarios de **primaria**: modela docentes, grupos, aulas y carga semanal y resuelve con **OR-Tools CP-SAT**. Instalador Windows y AppImage, 42 commits. ⚠️ *«Early foundation, not production-ready»*, y la UI es **sólo español** | EMEA (España) |

🔵 **UniTime es el hallazgo de volumen del pase: 349 ★, 213 forks y Apache-2.0** para un dominio —horario de cursos y de
exámenes en educación superior— que esta KB tenía **vacío**. Y el contraste de licencias del segmento vuelve a repetir la
forma que el pase 24 midió en SIS: **FET y mFET, los dos nombres históricos del timetabling escolar, son GPL/AGPL.** El
permisivo grande es UniTime; el permisivo chico y español es `horarios-escolares-manager`, y está declarado como
no-productivo por sus propios autores.

### El artefacto `competency framework`: la pieza que hace *aserciones*, no sólo hospedaje de marcos — y trae puerta de agente

| Repo | Licencia | ★ | Forks | Lenguaje | Qué es | Región |
|---|---|---|---|---|---|---|
| https://github.com/cassproject/CASS | **Apache-2.0** ✅ | **62** | **29** | JavaScript | *«Competency and Skills System»*: **autoría de marcos de competencias, registro de aserciones de logro individual y cómputo de perfiles del aprendiz**. **2.123 commits.** Editor Vue.js con *crosswalks* e import/export. Cartuchos de interoperabilidad: **IMS CASE**, **xAPI**, **CTDL-ASN**, **ASN**, **Open Badges 2.0** y **MCP** | North America ⚠️ *inferida* |

🔴 **Por qué es el hallazgo más estructural del pase, aunque no sea el de más estrellas.** La capa CASE de esta KB
—`opensalt` (MIT, 45 ★), `1EdTech/OpenCASE` (Apache-2.0, 9 ★), `compeito` (Apache-2.0, 3 ★), `conform-ed` (MIT, 2 ★)—
**sabe hospedar y validar marcos de competencias, y ninguna de sus cuatro piezas sabe decir si un alumno alcanzó una
competencia.** CaSS es **la pieza de aserción**, es Apache-2.0, y con 62 ★ es **la más traccionada de toda esa capa**.
Y el cartucho **MCP** es la primera vez que esta KB encuentra **una pieza de estándar educativo que expone puerta nativa
de agente**: es el puente que faltaba entre la capa de estándares y la capa de agentes de esta misma KB. Ver **P48** y la
tendencia **65**.

### La capa `proctoring`, barrida entera: cinco piezas y **ninguna** es permisiva y productiva a la vez

| Repo | Licencia | ★ | Forks | Lenguaje | Estado medido |
|---|---|---|---|---|---|
| https://github.com/openedx/edx-proctoring | ⚠️ **AGPL-3.0** | 68 | **95** | Python | Subsistema de exámenes supervisados de **Open edX**. Vivo, no archivado. El README **no documenta qué backends soporta** |
| https://github.com/oat-sa/lib-lti1p3-core | ⚠️ **GPL-2.0** | 37 | 22 | PHP | **La única certificada en *LTI 1.3 Proctoring Services*** de toda la base. Copyleft |
| https://github.com/vardanagarwal/Proctoring-AI | **MIT** ✅ | **635** | **352** | Python | 🔴 **Trampa de licencia (ver abajo).** Detecta rostro, *spoofing*, mirada (izq/der/arriba), apertura de boca, pose de cabeza, conteo de personas, teléfono y audio→texto. **Proyecto de investigación/demo**, por su propio README |
| https://github.com/sudosylabs/Proctor | ⚠️ **AGPL-3.0** | 0 | 0 | Go + React | 369 commits. **Declarado pre-release:** *«has not published a supported production release»* |
| https://github.com/kamlendras/OpenProctor | ⚠️ **AGPL-3.0** | 15 | 4 | Next.js / TS | 37 commits, sin releases. No productivo |

🔴 **La trampa de `Proctoring-AI`, y es la instancia con más estrellas del error que el pase 14 dejó documentado.** El
repo es **MIT** —el badge dice MIT, 635 ★— pero su propio README advierte que el modelo de *facial landmarks* está
**entrenado con datasets de uso no comercial**. **Código permisivo, pesos no comerciales:** el badge del repo es la
licencia del *código*, no la del *modelo*, y acá la diferencia es la que decide si se puede facturar. **No proponerlo en
un entregable comercial** sin reemplazar los pesos.

🔵 **La conclusión de la capa, y es de decisión, no de catálogo:** **la supervisión remota de exámenes es la única capa de
esta KB sin ninguna opción permisiva y productiva.** O AGPL/GPL —viral para un SaaS multicliente— o un demo con pesos no
comerciales. **Y es, al mismo tiempo, la capa que el regulador mira más de cerca:** el proctoring está nombrado
explícitamente en el **Annex III del EU AI Act** como alto riesgo (vigente 2027-12-02). Ver la tendencia **64**, el
**gap 39** y el patrón **P49**, que entrega integridad de examen **sin** AI de proctoring.

### Los no-hallazgos del pase, declarados en vez de omitidos

| Lo que se buscó | Resultado medido | Por qué queda escrito |
|---|---|---|
| `github.com/1EdTech/caliper-java`, `caliper-js`, `caliper-python`; `IMSGlobal/caliper-java`, `IMSGlobal/caliper-python` | **404 los cinco.** La descripción del repo `1EdTech/caliper-java` **es el aviso**: *«1EdTech will be moving Caliper to private repositories on June 17, 2023»* | 🔴 **No es un hueco de búsqueda: es una decisión del consorcio con fecha.** Es el hallazgo del estándar Caliper y está desarrollado en la tendencia **63** |
| `github.com/yetanalytics/lrspipe` | **404.** El repo real es **`yetanalytics/xapipe`** (Apache-2.0, 17 ★, 9 forks, Clojure) | Segundo falso negativo por nombre de producto ≠ nombre de repo en dos pases seguidos. **LRSPipe es el nombre del producto; `xapipe`, el del repo** |
| Un *item bank* QTI 3 con certificación 1EdTech | **No existe en open source.** El único certificado (`qti3-item-player`) es sólo entrega; el que banca (`LongsightGroup/qti3`) declara no estar certificado | Cierra la consigna del pase 24 sobre `item bank` con el límite medido, no con una fila |
| `tremby/questionbank` y `tremby/eqiat` (bancos de ítems QTI históricos) | Existen pero **archivados** | No se proponen; quedan como antecedente del dominio |

## 2026-10-01 (pase 24) — la consigna del pase 23 rindió en su primer uso: buscar por el estándar instalado destapó que la capa LTI de esta KB era íntegramente PHP, y existe una familia Java/Spring de una universidad europea

**Seis repos verificados de primera mano, cinco nuevos para esta KB.** Ninguno es un agente —la tabla de `agents/top.md`
sigue en 37 filas y van seis pases sin altas— pero todos son **infraestructura de interoperabilidad**, que es la capa por
la que un agente entra al LMS del cliente.

### Los nuevos, verificados uno por uno

| Repo | Licencia | ★ | Forks | Lenguaje | Qué es | Región |
|---|---|---|---|---|---|---|
| https://github.com/UOC/java-lti-1.3 | **MIT** ✅ | 21 | 14 | Java | Librería **LTI Advantage** completa del lado *tool*, v**1.0.0**. **La pieza con más estrellas de la familia** | EMEA (Universitat Oberta de Catalunya, Barcelona) |
| https://github.com/UOC/spring-boot-lti-advantage | **MIT** ✅ | 16 | 17 | Java | LTI Advantage para **Spring Boot**: configura Spring Security para validar los *launches*, y trae implementaciones `RestTemplate` de **AGS** (Line Item, Result, Score), **NRPS** y *Deep Linking* por el manejo del *launch* OIDC. Lado *tool* | EMEA (UOC) |
| https://github.com/UOC/java-lti-1.3-platform | ⚠️ **sin licencia declarada** | 0 | 1 | Java | *«Library that will implement a full LTI Advantage platform»* — **lado *platform*, o sea el lado del LMS**. El tiempo futuro del README es el dato: es intención, no producto | EMEA (UOC) |
| https://github.com/packbackbooks/lti-1-3-php-library | **Apache-2.0** ✅ | 53 | 25 | PHP | *Tool provider* LTI 1.3 certificable, **1.038 commits**, mantenida por Packback | North America (Packback, Chicago) |
| https://github.com/gnowledge/OpenAssessmentsClient | **Apache-2.0** ✅ | 0 | 3 | JavaScript (React) | Cliente **QTI 1.x y 2.x**: intérprete de ítems y varios tipos de pregunta. **No es QTI 3** | APAC (gnowledge) |
| https://github.com/OS4ED/openSIS-Classic | **GPL** ⚠️ (en `docs/License.txt`) | 344 | 286 | PHP | SIS completo de K-12 y superior: legajo de alumno y de personal, *course manager*, horarios, **asistencia, notas, gradebook docente y legajos/transcripts** | North America (OS4ED) |

### 🔴 El hallazgo de encuadre: toda la capa LTI de esta KB era PHP, y eso sesgaba lo que se podía proponer

Hasta este pase, la única vía de entrada a un LMS que registraba esta KB era `1EdTech/lti-1-3-php-library` (Apache-2.0,
124 ★) — y está en **cinco** archivos, incluidos **P20, P21** y la fila *«LTI 1.3 como vía de entrada»* de
`verticals/solutions.md`. **El problema no era la pieza: era que la KB no sabía que había alternativa de stack.** Un
cliente con plataforma Java/Spring —que en educación superior europea es la norma, no la excepción— recibía una
propuesta que le metía PHP en el diagrama por una razón que no era técnica sino de cobertura de esta KB.

**Ahora hay familia Java completa y permisiva (MIT), de una universidad pública catalana,** con 14 repos LTI en la
organización. Los dos que importan están arriba; los otros que vale nombrar son `java-lti-1.3-core` (4 ★),
`java-lti-1.3-jwt` (firma), `spring-boot-lti-advantage-jkws` (JKWS) y, fuera de Java, `django-uocLTI` e `ims_lti_py`
para stacks Python. **Las estrellas acá miden poco** —21 y 16— pero es código de una institución que lo usa en
producción para su propio campus, que es el mismo criterio por el que el pase 22 aceptó `tutor-contrib-aspects` con 14.

### ⚠️ Corrección de procedencia, y evita escribirla mal en una propuesta

Al ver `packbackbooks/lti-1-3-php-library` la hipótesis natural era que la librería de 1EdTech fuera una donación de
Packback, y que la fila de esta KB estuviera apuntando al *fork* en vez del *upstream*. **Se verificó y es falso.** El
README de `1EdTech/lti-1-3-php-library` dice textualmente:

> *«This library was initially created by @MartinLenord from **Turnitin** to help prove out the LTI 1.3 specification and
> accelerate tool development.»*

**Son dos librerías PHP de LTI 1.3 independientes, las dos Apache-2.0**: la de 1EdTech (origen Turnitin, 124 ★) y la de
Packback (53 ★, 1.038 commits). La fila de esta KB está bien apuntada; lo que faltaba era saber que existe una segunda,
que importa cuando la primera no cubre un caso o cuando hay que elegir dónde abrir un *issue*.

### El dato de `openSIS` que confirma el diagnóstico del pase 2 con números propios

El pase 2 concluyó que *«todo el SIS open source es PHP y copyleft»* y el pase 23 reforzó el hueco al mostrar que el ERP
permisivo de 12k ★ (AureusERP, MIT) **no tiene módulo educativo**. `openSIS-Classic` lo cierra con la medición que
faltaba: **344 ★ y 286 forks, PHP, GPL** — es **el SIS open source más traccionado que vio esta KB**, y es copyleft.
Al lado, el único permisivo del segmento sigue siendo **GegoK12 (MIT, 54 ★)**. **La asimetría es de un orden de
magnitud y no es un descuido de búsqueda: es la forma del mercado.**

### Los no-hallazgos, declarados en vez de omitidos

Las dos URL que las búsquedas sugerían y **no existen** — verificado, **404**, no es un 403 de proxy:

| URL que la búsqueda insinuaba | Resultado | Por qué queda escrito |
|---|---|---|
| `github.com/UOC/java-lti-1.3-provider` | **404** | El repo real es `java-lti-1.3-provider-example` (MIT, 8 ★, 12 forks, Java). El nombre sin `-example` no existe |
| `github.com/LongsightGroup/qti3-core` | **404** | Los resultados hablaban de los paquetes npm `@longsightgroup/qti3-core` y `qti3-player` y de un «QFlow»; **el repo GitHub con ese nombre no existe.** Si el código está publicado, no está ahí, y para esta KB **QTI 3 sigue siendo `amp-up-io/qti3-item-player`**, que además es el único artefacto certificado por 1EdTech de toda la base |

**Y la confirmación de precisión, que ya es costumbre:** `LongsightGroup/oneroster` apareció otra vez en el barrido
presentado como novedad (*«0.3.0 agrega REST y CSV»*). **Esta KB lo tiene desde el pase 9 con 0 ★ y 33 commits**, y con
el dato que la fuente no da: que **0 ★ significa referencia de integración, no dependencia de producción.** Tercer pase
consecutivo en que la KB está más precisa que la web sobre un repo que la web presenta como nuevo.


## 2026-10-01 (pase 23) — el módulo educativo de ERPNext existe, es una app aparte y tiene 657 ★: la pregunta que el pase 21 dejó abierta queda cerrada con el repo en la mano

**Un repo nuevo verificado, y una no-novedad que vale escribir porque llegó por la misma búsqueda.**

| Repo | Licencia | ★ | Commits | Qué es |
|---|---|---|---|---|
| **Frappe Education** · https://github.com/frappe/education | **GPL-3.0** ⚠️ — leída en **`license.txt`**, porque **la página del repo no declara licencia** | 657 | 1.091 | Gestión académica sobre Frappe Framework: alumnos y docentes, admisiones, programas y cursos, asistencia, cuotas, horarios y portal del alumno |

### Por qué este repo importa más por lo que aclara que por lo que es

El pase 21 registró ERPNext (GPL-3.0, 39,7k ★) y dejó una advertencia explícita: *«no se pudo confirmar que el módulo de
educación sea parte del core de ERPNext […] verificar primero en qué app vive el módulo»*. **Este pase lo verificó y la
sospecha era correcta:**

| | |
|---|---|
| **Dónde vive** | En `frappe/education`, una app **independiente** — no en el core de `frappe/erpnext` |
| **Desde cuándo** | **El corte es ERPNext v14.** Hasta v13 *Education* era un *domain* del core; en v14 se extrajo |
| **Cómo se instala** | `bench get-app education` + `bench --site <sitio> install-app education`, luego `bench build` / `migrate` / `restart` |
| **El síntoma que lo delata** | Los foros de Frappe acumulan hilos «Education module missing in domain list v14». **No es un error de instalación: es el split.** |
| 🔴 **El dato que cambia una propuesta** | ERPNext tiene **39,7k ★**; el módulo académico, **657**. **La tracción del ERP no se hereda al módulo que al cliente le importa**, y proponer «ERPNext para educación» implica **dos** artefactos GPL-3.0, no uno |

### La no-novedad, declarada en vez de omitida: el ERP permisivo de 12k ★ no sirve para educación

La búsqueda de plataforma (`open source platform education ERP CRM MIT Apache`) devolvió **AureusERP**
(https://github.com/aureuserp/aureuserp) en posición alta, y es **el candidato más tentador que vio esta KB en la capa
administrativa**: **MIT** ✅, **12k ★**, **3.794 commits**, PHP sobre Laravel 13 + FilamentPHP 5, arquitectura de plugins.
Es decir: todo lo que la KB viene pidiendo desde el pase 2, cuando concluyó que *«todo el SIS open source es PHP y
copyleft»*.

🔴 **Y no sirve, por una razón que sólo aparece abriendo el repo: no tiene módulo educativo.** Sus plugins cubren
finanzas, operaciones, RRHH, gestión de clientes y proyectos — **no hay nada académico**: ni matrícula, ni programas, ni
asistencia, ni cuotas de alumno, ni legajo. Es un ERP genérico de PyME que aparece en búsquedas de *education ERP*
porque el listicle que lo cita las agrupa, no porque cubra el dominio.

**Queda registrado como no-hallazgo con su razón**, y no como silencio, por dos motivos: (1) va a volver a aparecer en la
primera búsqueda de ERP permisivo que haga cualquier pase futuro, y (2) **el hueco que deja es exactamente el que GegoK12
(MIT, 54 ★) ocupa solo** — y saber que el segundo permisivo de la categoría tiene 12k ★ y ningún módulo académico es lo
que explica por qué un SIS permisivo con 54 estrellas sigue siendo la única opción, en vez de parecer un descuido de
búsqueda.

## 2026-10-01 (pase 22) — el stack de analítica oficial de Open edX es Apache-2.0, trae el LRS que el pase 21 declaró imborrable, y trae además el disparador LMS→telemetría que el pase 19 probó que no existe

**Dos repos nuevos, los dos Apache-2.0, los dos de la organización `openedx`.** Entre los dos corrigen una advertencia
de **P44** y cambian el estado de **P40**. Verificados de primera mano vía WebFetch en este pase:

| Repo | Licencia | ★ | Forks | Commits | Qué es |
|---|---|---|---|---|---|
| https://github.com/openedx/tutor-contrib-aspects | **Apache-2.0** ✅ | 14 | 32 | 2.269 | **Aspects**: el plugin de analítica y reporting **oficial** de Open edX. Instala y orquesta vía Tutor un stack completo: **ClickHouse** (almacén), **Apache Superset** (visualización), **Ralph de OpenFUN** (el LRS), **Vector** (forwarding), **event-routing-backends** (transformación a xAPI) y **dbt** (pipeline). Python |
| https://github.com/openedx/platform-plugin-aspects | **Apache-2.0** ✅ | 6 | 14 | 528 | Los *sinks* del lado LMS/Studio: empujan dato de la plataforma a ClickHouse y **embeben dashboards de Superset dentro de la interfaz del docente**. Python |

**Por qué entran a esta KB con 14 y 6 estrellas.** Las estrellas acá no miden nada: es el camino de analítica oficial de
una plataforma con decenas de miles de despliegues, y los **2.269 commits** del primero son la señal que importa. Es
infraestructura de plataforma, no un proyecto que compite por atención.

### 🔴 El hallazgo: la configuración que el pase 21 declaró imposible de borrar **es la instalación por default**

El pase 21 escribió en las advertencias de **P44**: *«Con Ralph sobre ClickHouse, este patrón no se puede ejecutar»*, y
lo planteó como un riesgo **condicional** — *«si el cliente ya eligió ese backend por analítica, la decisión hay que
revisarla»*. **No es condicional, y hay que corregir el encuadre:** `tutor-contrib-aspects` es el camino oficial de
analítica de Open edX y **Ralph sobre ClickHouse es exactamente lo que instala**. Un cliente con Open edX y analítica
no *eligió* ese backend — lo tiene porque es lo que trae la plataforma.

Dicho operativamente: **el supuesto por default de una propuesta sobre Open edX tiene que ser que el cliente ya está
en la configuración difícil de borrar**, y eso hay que levantarlo en el *discovery*, no al llegar al expediente de
privacidad. Es el mismo movimiento que el pase 21 hizo con el flag apagado de `lrsql`, al revés: ahí la buena noticia
venía desactivada de fábrica, acá la mala viene activada.

### Y el mismo stack trae lo que el pase 19 declaró inexistente: el disparador de supresión LMS → telemetría

`platform-plugin-aspects` declara en su README, **leído de primera mano en este pase**:

> `UserRetirementSink` — escucha la señal Django `USER_RETIRE_LMS_MISC` y **elimina la información PII del usuario de
> ClickHouse**.

**Esa es exactamente la pieza que el pase 19 buscó en Moodle y probó que no existe.** El pase 19 recorrió los 187
archivos de `tool_dataprivacy` y encontró **cero** llamadas a `trigger()`: Moodle no emite ningún evento al aprobar un
pedido de supresión, así que el disparador de **P40** había que construirlo por sondeo de tabla. **En Open edX el
disparador existe, es una señal del framework, y el listener que la consume es Apache-2.0.**

**Lo que esto le hace a P40:** deja de ser *«no hay evento, en ningún lado»* y pasa a ser *«hay evento en una
plataforma y no en la otra»*. Para un cliente **Open edX** el extremo del disparador es **configuración más
verificación**. Para un cliente **Moodle**, el `UserRetirementSink` es la **implementación de referencia** —el diseño
ya está resuelto, es permisivo y está en producción— y lo que falta sigue siendo la mitad observable del lado Moodle.

### ⚠️ Pero hay que leer bien **qué** borra, porque la mitad que importa se queda

El sink borra **PII** —las tablas de perfil: `user_profile`, `external_id`, `auth_user`—, **no el registro de
eventos**. La documentación de Aspects sostiene que el dato de eventos del usuario retirado **no se elimina, porque
queda anonimizado**, y el almacenamiento de PII se gobierna con un flag propio, `ASPECTS_ENABLE_PII`.

Dicho sin eufemismo, la postura por default del stack de analítica oficial de Open edX ante un pedido del art. 17 es:
**se borra el nombre y se conserva la conducta.** Eso abre el **gap 37**.

⚠️ **Verificación parcial, y hay que declararla.** El `UserRetirementSink`, la señal y las tablas de PII están
**verificados de primera mano** en el README de `platform-plugin-aspects`. La afirmación de que *el dato de eventos no
se elimina porque queda anonimizado* viene de **snippets concordantes de búsqueda, no de lectura directa**: el ADR que
la contiene vive en `docs.openedx.org`, **bloqueado por el proxy de egreso en este pase** —igual que `arxiv.org` en los
pases 6, 7, 14, 16–19 y `moodle.org` en el 19—, y los dos caminos alternativos que se probaron (el `.rst` crudo y el
listado del directorio de decisiones en GitHub) devolvieron **404**. **La URL exacta queda anotada para que el próximo
pase la abra:**
`https://docs.openedx.org/projects/openedx-aspects/en/latest/technical_documentation/decisions/0009_pii.html`.

### El dato de *due diligence* que vale más que las estrellas, y está verificado de primera mano

**PR #1328 de `tutor-contrib-aspects`** — *«fix: make dump-data-to-clickhouse job respect `ASPECTS_ENABLE_PII`»*, de
`ccantillo`. La descripción dice que el *job* manual de *backfill* **pasaba por encima del flag de PII**:

> un operador corriendo el *job* manual de *backfill* podía volcar `user_profile` o `external_id` a ClickHouse en una
> instancia que había explícitamente optado por no recolectar PII vía `ASPECTS_ENABLE_PII=False`, **sorteando
> exactamente la protección que ese setting existe para dar**.

El *check* de PII existía en el camino automático por señales y **faltaba en el camino manual**. 🔴 **Y el PR está
CERRADO, no mergeado** — cerrado por su propio autor el **2026-09-16**. O sea: **el agujero descrito puede seguir
abierto**, y si una propuesta se apoya en `ASPECTS_ENABLE_PII=False` como control de privacidad, **ese control tiene
un camino documentado que lo sortea y el parche no entró**. Hay que verificarlo contra la versión del cliente antes de
escribirlo en un expediente.

### La precisión sobre ClickHouse, que el pase 21 dejó demasiado absoluta

El pase 21 escribió que *«ClickHouse declara `DELETE` como operación no soportada»*. **La formulación correcta es más
estrecha:** ClickHouse no tiene `UPDATE`/`DELETE` de propósito general al estilo OLTP, y sí tiene **borrado liviano**
sobre tablas MergeTree detrás de un setting (`allow_experimental_lightweight_delete`) más las mutaciones
`ALTER TABLE … DELETE`. La diferencia importa para una propuesta: **no es «el motor no puede», es «el motor puede por
una vía que no es transaccional, que depende de versión y que el backend de Ralph no expone en la API del LRS»**. La
imposibilidad práctica se sostiene; la razón hay que decirla bien. ⚠️ **Dependiente de versión y no verificado de
primera mano en este pase** — queda para el próximo, contra la versión de ClickHouse que fija Aspects.

### Gap 37 (nuevo en este pase) — ¿el registro de eventos que queda es de verdad anónimo?

**Formulación:** Aspects conserva el dato de eventos del alumno retirado **sobre la base de que queda anonimizado**.
Pero un *statement* xAPI está indexado por un identificador de actor estable (el `actor-ifi`), y un registro
pseudonimizado —no anonimizado— **sigue siendo dato personal bajo GDPR**. Si el identificador sobrevive a la retirada,
la palabra «anonimizado» está haciendo un trabajo legal que puede no sostener, y el default del stack oficial retiene
el expediente conductual completo de alguien que ejerció el art. 17.

**Qué hay que leer para cerrarlo, y es acotado:** qué le pasa al `actor-ifi` / al identificador externo en las tablas
de eventos cuando corre el `UserRetirementSink` — si se borra, se rota o se deja. **Si se deja, hay un hallazgo
regulatorio serio sobre la plataforma educativa open source más usada del mundo; si se rota o se borra, la postura de
Aspects es defendible y esta KB tiene que escribirlo así.** No es investigación: es leer un sink y un esquema de
tablas. Es, junto al **gap 36**, el gap más barato que tiene esta KB abierto.

### Y es el tercer proveedor que documenta el mismo agujero por escrito

El pase 21 registró que el Feature Wiki de **ILIAS** declara que al borrar un objeto xAPI/cmi5 el dato personal
**persiste en el LRS** y que ILIAS no tiene forma de borrarlo (tendencia **55**). Con Aspects son **dos plataformas
que documentan el límite** —y en el caso de Aspects, lo documenta la plataforma **en su propia decisión de
arquitectura**—. Eso es lo que vuelve defendible el argumento en una propuesta: **no es una carencia que invente esta
KB, es la postura escrita de los proveedores.**

## 2026-10-01 (pase 21) — el LRS permisivo que esta KB recomienda sí sabe borrar, tiene el mejor primitivo de borrado de toda la capa, y viene apagado de fábrica: seis pasadas afirmaron lo contrario leyendo documentación en vez de código

**Cero repos nuevos en esta sección, y es el punto.** Este pase no buscó repos: **ejecutó la acción 1 que dejó escrita
el pase 19** —«confirmar la API de borrado de Learning Locker (gap 33)», declarada ahí como *la pregunta de mayor
rendimiento del pase*— y que el pase 20 no tomó. Se ejecutó **clonando los tres LRS y leyendo el código**, no la
documentación. Los tres resultados contradicen lo que esta KB tiene escrito, y el más importante lo contradice **al
revés de lo que convenía**.

### Lo que dice la tabla del gap 33 en `repos/foundations.md`, y lo que dice el código

| LRS | Lo que esta KB afirmó (pases 6→20) | Lo que dice el código, leído en este pase | Veredicto |
|---|---|---|---|
| **`lrsql`** (Apache-2.0) | 🚫 «Nada sobre *delete*, *erasure* ni retención» | ✅ **`DELETE /admin/agents`**, borrado **por actor IFI** en cascada sobre **7 tablas**, en **una transacción** | 🔴 **REFUTADO.** Es el mejor primitivo de la capa |
| **Learning Locker** (GPL-3.0) | ✅ «Se le *atribuye* una API especial de borrado» (fuente secundaria, sin verificar) | ✅ **`POST /api/v2/batchdelete/initialise`**, borrado **por filtro**, worker paginado | ✅ **CONFIRMADO**, con cuatro condiciones operativas |
| **Ralph** (MIT) | 🚫 «Nada sobre *delete*, endpoint DELETE ni GDPR/erasure» | ⚠️ **No hay DELETE en la API del LRS** (sólo GET/PUT/POST), pero el *data backend* implementa `OperationType.DELETE` **por ID de statement** | ⚠️ **PARCIAL** — y el backend elegido decide si se puede borrar |

**Verificado de primera mano, clonando y leyendo el archivo** (`git clone --depth 1 --filter=blob:none`), no vía
WebFetch ni documentación:

- **`lrsql`** — HEAD `2d24f2d` del **2026-09-04**. Ruta en `src/main/lrsql/admin/routes.clj:331`
  (`["/admin/agents" :delete …]`), interceptor en `admin/interceptors/lrs_management.clj`, implementación en
  `system/lrs.clj:459`, y el SQL en **`src/db/postgres/lrsql/postgres/sql/delete.sql:119`**
  (`delete-actor-and-dependents!`).
- **Learning Locker** — HEAD `5fec948` = tag **v7.1.1**, del **2021-11-16**. Ruta en
  `api/src/routes/HttpRoutes.js:277`, controlador `api/src/controllers/BatchDeleteController.js`, worker
  `worker/src/handlers/batchStatementDeletion/batchStatementDeletion.js`, modelo `lib/models/batchDelete.js`,
  scheduler `cli/src/scheduler/batchDelete.js`.
- **Ralph** — HEAD `53cc58c` del **2026-09-07**. `src/ralph/api/routers/statements.py` declara **sólo**
  `@router.get`, `@router.put` y `@router.post` — **no existe `@router.delete` en ningún router**. El borrado vive en
  `src/ralph/backends/data/mongo.py:403` (`_bulk_delete`) y `es.py:397`.

### El primitivo de `lrsql`, que es el hallazgo que da vuelta la lectura de la capa

`delete-actor-and-dependents!` recibe **un solo parámetro, `:actor-ifi`** —el identificador xAPI del alumno— y borra en
cascada, dentro de una transacción (`jdbc/with-transaction`), de **siete tablas**:

```
statement_to_statement   (aristas ancestor_id y descendant_id)
statement_to_activity
attachment
xapi_statement
agent_profile_document
state_document
actor
```

**Y la octava tabla se borra sola, por diseño explícito.** `statement_to_actor` —la tabla que mapea statement → actor,
o sea **la que contiene el IFI del alumno junto a cada statement**— no aparece en la lista, y la primera lectura
sugería un residuo de privacidad. **No lo es:** el DDL trae una migración con guarda
(`check-statement-to-actor-cascading-delete` / `add-statement-to-actor-cascading-delete!`, `ddl.sql:443-456`) que
cambia la FK a **`ON DELETE CASCADE`**, con el comentario del mantenedor diciendo para qué:
*«Adds a cascading delete to delete st2actor entries when corresponding statements are deleted»*. O sea: **alguien en
Yet Analytics pensó este caso y lo cerró.** Se registra el camino completo porque la tentación era escribir el residuo.

⚠️ **Viene apagado.** `resources/lrsql/config/prod/default/webserver.edn:36` define
`:enable-admin-delete-actor #boolean #or [#env LRSQL_ENABLE_ADMIN_DELETE_ACTOR false]` — **default `false` en
producción** (en la config de test está en `true`). La ruta **no se registra** si el flag está apagado
(`routes.clj:407`). **Es una variable de entorno, no un desarrollo:** `LRSQL_ENABLE_ADMIN_DELETE_ACTOR=true`.

### Learning Locker: la API existe, y las cuatro condiciones que hay que poner en el contrato

`POST /api/v2/batchdelete/initialise` con un `filter` en el body crea un job `BatchDelete` y lo publica en la cola
`BATCH_STATEMENT_DELETION_QUEUE`. El worker hace `Statement.deleteMany` **por páginas** (`pageSize`, default **1000**)
y se re-encola hasta que `deletedCount === 0`. Es un borrado duro de Mongo, no un flag. Las cuatro condiciones:

1. **Flag de entorno.** `ENABLE_STATEMENT_DELETION` (default `true`) se chequea en **la API, el worker y el
   scheduler**. En `false`, la API rechaza con error, pero **el worker descarta el job en silencio** (`jobDone()` sin
   trabajo y sin error).
2. **Ventana UTC.** `batchDeleteWindowUTCHour` / `…UTCMinutes` / `…DurationSeconds` (default **3600 s**) en
   `SiteSettings`. Fuera de ventana el worker **abandona el job y no lo re-encola**. Lo rescata el **scheduler del
   CLI**, que al inicio de la ventana siguiente re-publica todo `{done:false, processing:false}` — así que
   **el proceso scheduler es una dependencia de cumplimiento, no un detalle de despliegue**: sin él, un pedido hecho
   fuera de ventana no se reintenta nunca. Con hora y minuto en `null` (el default) `inWindow` devuelve `true`, o sea
   que de fábrica la ventana está siempre abierta.
3. **`done: true` NO significa «borrado».** Tres caminos marcan el job como terminado **sin borrar nada**: filtro
   imparseable, filtro vacío y `NoAccessError` de scope — los tres llaman `markDone` y dejan `deleteCount` en `null`.
   **Para evidenciar un borrado hay que comparar `deleteCount` contra `total`,** no leer `done`.
4. **`terminate` no es un rollback.** `POST /batchdelete/terminate/:id` pone `done: true` y detiene las páginas
   siguientes; **lo ya borrado queda borrado.**

**Progreso consultable, no notificado.** El documento `BatchDelete` expone `total`, `deleteCount`, `processing` y
`done` — o sea **se puede sondear**, pero **no hay evento, webhook ni callback de finalización**. Es exactamente la
misma forma que el pase 19 encontró en Moodle, y confirma el diagnóstico de **P40** por el otro extremo de la cadena.

### 🔴 Ralph: el backend que elegirías para analítica es el único que no puede borrar

Ralph **no expone borrado en la API del LRS**. Lo que tiene es una operación `DELETE` en la capa de *data backend*,
**por ID de statement** (`collection.delete_many({"_source.id": {"$in": batch}})`) — así que para cumplir el art. 17
hay que **primero consultar** los statements del alumno y **después** pasar esos IDs a un `write`. No existe un
«borrar donde actor = X». Y el detalle que decide una arquitectura:

| Backend de Ralph | `OperationType.DELETE` |
|---|---|
| MongoDB | ✅ soportado (`mongo.py:285`) |
| Elasticsearch | ✅ soportado (`es.py:397`) |
| **ClickHouse** | 🚫 **declarado en `unsupported_operation_types`** (`clickhouse.py:128-131`), junto con `APPEND` y `UPDATE` |

El docstring lo dice textual: *«BackendParameterException: If the `operation_type` is `APPEND`, `UPDATE` or `DELETE`
as it is not supported»*. **ClickHouse es el backend orientado a analítica** —el que se elige para learning analytics
a escala— **y es el que no puede borrar.** La elección de backend de Ralph es una decisión de cumplimiento, y en esta
KB no estaba escrita.

### «No archivado» no es lo mismo que «mantenido»: el estado real de Learning Locker

Learning Locker **no está archivado** y su README no tiene aviso de fin de vida — habla de oferta comunitaria y
comercial de Learning Pool (585 ★, 294 forks, GPL-3.0, verificado vía WebFetch el 2026-10-01). Pero
**`git log` dice que el código no se mueve desde el 2021-11-16**, y `HEAD` coincide con el tag **v7.1.1**, el último.
Son casi **cinco años**. La capacidad de borrado existe y funciona; el software que la implementa no recibe
mantenimiento. **Las dos cosas hay que decirlas juntas**, y es la contracara de la regla del pase 8: ahí fue *leer el
`LICENSE`, no el badge*; acá es **leer el `git log`, no el banner de archivado**.

### La lección de método, que es la quinta de esta serie y la más cara hasta ahora

Pase 5 — buscar la pieza técnica, no la categoría. Pase 7 — buscar la palabra del mercado, no la del paper. Pase 8 —
buscar por quién es el alumno. Pase 9 — buscar el final del recorrido, no el principio. **Pase 21 — leer el código, no
la documentación.**

El gap 33 nació en el pase 6 y sobrevivió hasta el 20 con una nota de límite escrita por la propia KB
(`foundations.md`): *«El "no" de `lrsql` y Ralph es ausencia en la documentación publicada, no [ausencia en el
código]»*. **La nota estaba bien y nadie la ejecutó durante catorce pasadas.** El costo no fue un repo que faltaba:
fue **vender a un cliente la ausencia de una capacidad que el producto recomendado tenía**, y construir sobre esa
ausencia una tendencia (**49**), un gap (**33**), un patrón (**P40**) y un argumento de mercado en EMEA y LATAM.
**Un gap declarado sobre documentación no es un gap: es una tarea de lectura pendiente.**

## 2026-10-01 (pase 20) — el repo de testing de conformidad más grande de esta capa es MIT, tiene 2.900 ★ y lo mantiene un gobierno; el catálogo que lo acompaña cubre derecho, medicina y finanzas y no educación

**Diez repos nuevos, verificados uno por uno vía WebFetch el 2026-10-01.** Ninguno se presenta como educativo, y es
exactamente el motivo por el que veinte pasadas no los vieron.

### Los repos nuevos, con licencia leída en la página del repo

| Repo | Licencia | ★ | Forks | Qué es |
|---|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | **MIT** ✅ | **2.900** | 763 | Framework de evals del **UK AI Security Institute**. 200+ evals pre-construidas. **Es el segundo repo con más estrellas de toda esta KB** |
| `aiverify-foundation/moonshot` | **Apache-2.0** ✅ | 353 | 70 | *Benchmarking* + *red-teaming* en una herramienta. AI Verify Foundation (Singapur). 2.153 commits, v0.7.6 beta |
| `compl-ai/compl-ai` | **Apache-2.0** ✅ | 211 | 37 | 29 benchmarks mapeados a **6 principios del EU AI Act**. ETH Zürich + INSAIT + LatticeFlow AI. 333 commits |
| `aiverify-foundation/aiverify` | **Apache-2.0** ✅ | 97 | 31 | Plataforma de *governance testing*, 3.035 commits. ⚠️ tabular/imagen supervisado, **no agentes** |
| `aiverify-foundation/moonshot-data` | **Apache-2.0** ✅ | 45 | 41 | Conectores, datasets (BigBench, CyberSecEval, Medical LLM, AILuminate v1.0 DEMO / MLCommons), métricas, *attack modules* |
| `aiverify-foundation/LLM-Evals-Catalogue` | ⚠️ **sin licencia declarada** | 23 | — | Catálogo de evals en 7 categorías. **El hallazgo del pase está acá adentro** |
| `morganrcu/awesome-eu-ai-act` | **CC0** ✅ | 21 | — | Lista curada de herramientas de conformidad al AI Act |
| `aiverify-foundation/moonshot-cicd` | **Apache-2.0** ✅ | 14 | 4 | Moonshot GA para CI/CD: Docker, S3, AWS CodeBuild. Python 3.12 |
| `aiverify-foundation/moonshot-ui` | **Apache-2.0** ✅ | 12 | 7 | UI Next.js; informe HTML con gráficos + export JSON |
| `aiverify-foundation/aiverify-developer-tools` | **Apache-2.0** ✅ | 9 | 6 | Plantillas de **plugins de test propios** (v2.x) |
| `GEMLab-HKU/Unlearn_and_Relearn` | **MIT** ✅ | 4 | 0 | *Unlearning* + *relearning* sobre modelo de alumno. **Universidad de Hong Kong**. 22 commits |

### 🔴 El hallazgo del pase: la ausencia está declarada, no inferida

Esta KB ya se equivocó midiendo capas por búsqueda (pases 4, 12, 18, 19). Acá no hace falta inferir: **los tres
catálogos declaran su propia cobertura por dominio.**

- **`LLM-Evals-Catalogue`** — categoría *domain-specific*: **derecho, medicina, finanzas**. **Educación ausente.**
- **`compl-ai`** — 29 benchmarks sobre los 6 principios del AI Act, **sin mención de educación**. Y el **Anexo III del
  propio AI Act nombra la educación como alto riesgo de forma textual**: el framework mapeado al AI Act no cubre uno
  de los dominios que el AI Act nombra.
- **`awesome-eu-ai-act`** — once herramientas open source listadas (Giskard 5.700 ★, DeepEval, PyRIT, Inspect,
  Holistic AI Apache-2.0, AI Act Companion MIT, Regula Apache-2.0/EUPL-1.2, VerifyWise, AIR Blackbox, Venturalitica
  SDK, Inkog). **Ninguna del sector educativo.**

**Y el complemento está en esta KB desde el pase 4:** `EduBench` (MIT), `SafeTutors` (MIT), `MathTutorBench` (CC BY
4.0), `UnifyingAITutorEvaluation` (CC BY-SA 4.0) — premiados en ACL, EMNLP y NAACL, **sin un solo mapeo regulatorio ni
empaquetado como *recipe***. Es el **gap 35**: lo que falta no es un repo, es **el puente entre dos mitades que ya
están construidas y son licencia-compatibles** (MIT ↔ Apache-2.0). Ver **P42**.

### La forma de esta capa, y rompe el patrón de las diecinueve pasadas anteriores

Las capas 8, 9, 10, 14 y 16 de esta KB tienen todas la misma forma: **lo maduro es copyleft, lo permisivo no pasa de
15 estrellas**. Esta capa la invierte por completo:

| | Capas 8/9/10/14/16 | Esta capa (pase 20) |
|---|---|---|
| Lo más grande | copyleft (GPL-3.0 / AGPL-3.0) | **MIT, 2.900 ★** (`inspect_ai`) |
| Lo permisivo | techo de 10–15 ★ | **Apache-2.0 con 353, 211 y 97 ★** |
| Quién lo publica | autor individual o laboratorio | **UK AISI, IMDA Singapur, ETH Zürich** |
| Cobertura educativa | parcial | **cero, y declarada** |

**La lectura comercial es directa:** no hay que pelear licencia ni madurez en esta capa. Hay que pelear **cobertura de
dominio**, que es trabajo de integración y es lo que Globant hace. Y hay una asimetría a favor: la capa es tan
permisiva que la contribución educativa puede ir **hacia arriba**, a los repos del regulador, lo que convierte un
entregable de cliente en posicionamiento público.

### El lado del *unlearning*, que el pase 19 dejó abierto y este acota

El pase 19 cerró el gap 32 refutándolo y dejó el **gap 34** (*unlearning* evaluado sobre modelos de alumno). Este pase
encuentra el primer repo educativo de *unlearning* **con código publicado** —`GEMLab-HKU/Unlearn_and_Relearn`, MIT— y
**no cierra el gap**, porque el objetivo está invertido: borra para **fabricar un alumno novato** creíble (y medir
cuánto recupera cuando se le enseña), no para **proteger** a un alumno real. **El gap 34 queda abierto con mejor
diagnóstico:** la maquinaria existe en educación y es MIT; falta apuntarla a la supresión.

### 🔴 La nota de método, y vale para toda la KB

Los pases 18 y 19 buscaron código de *unlearning* sobre *knowledge tracing* y no lo encontraron. **La causa es una
colisión de terminología, no una ausencia.** «Knowledge tracing» significa dos cosas distintas: en esta KB y en `pyKT`
es *modelar el conocimiento del alumno*; en la literatura de *unlearning* es *rastrear qué conocimiento de un modelo
vino de qué dato de entrenamiento* (*Lifting Data-Tracing Machine Unlearning to Knowledge-Tracing for Foundation
Models*). La búsqueda por técnica devuelve el segundo sentido y entierra el primero. **Lo que funcionó fue buscar por
escenario educativo** — la regla del pase 5, redescubierta en otra capa. Tercera vez que esta KB paga el mismo peaje.

### Lo que esta pasada buscó y no encontró

- 🚫 **Ninguna *recipe*, *cookbook* ni plugin educativo** en `moonshot-data`, `aiverify-developer-tools` ni `compl-ai`.
  Revisado el contenido declarado de los tres. **El gap 35 está medido, no supuesto.**
- 🚫 **Ningún caso de uso educativo documentado** de AI Verify o Moonshot.
- 🚫 **Ninguna herramienta de conformidad de origen LATAM**, en una región donde Brasil, Chile y México tienen
  obligaciones de auditoría algorítmica escritas o en trámite. No encontrada, **no inexistente**.
- ⚠️ `imda.gov.sg`, `moe.gov.sg`, `learning.moe.edu.sg` y `arxiv.org` **bloqueados por el proxy de egreso**: todo lo
  regulatorio y lo de plataforma estatal de este pase es de **fuentes secundarias concordantes**.

## 2026-10-01 (pase 19) — el ancla de la capa de *unlearning* tiene 607 ★ y es MIT, y el pase 18 midió la capa con los repos equivocados

El pase 18 cerró la capa de borrado del modelo con una frase correcta — *«la oferta existe, es grande y es toda
MIT/Apache»* — sostenida por los artefactos equivocados. **Sus dos piezas ejecutables tienen 12 ★ cada una**, y lo que
tenía cientos de estrellas (`jjbrophy47/machine_unlearning`, **965 ★**, reverificado en este pase: **sigue sin archivo
de licencia**) es una **bibliografía**, no código. La pieza seria de la capa no estaba registrada.

### El repo que faltaba, y los dos que cierran licencia

| Repo | Licencia | ★ | Qué es |
|---|---|---|---|
| **OpenUnlearning** · https://github.com/locuslab/open-unlearning | **MIT** ✅ | **607** | **El framework de referencia de *unlearning* de LLMs.** **Locus Lab (CMU)**. 3 benchmarks (**TOFU**, **MUSE**, **WMDP**), **12+ métodos** (GradAscent, GradDiff, NPO, SimNPO, DPO, RMU, UNDIAL, AltPO, SatImp, WGA, CE-U, PDU), 5+ datasets, **10+ métricas**, 7+ arquitecturas, **450+ modelos preentrenados** en HuggingFace |
| **MachineUnlearning** · https://github.com/OngWinKent/MachineUnlearning | **BSD-3-Clause** ✅ | 12 | 9 métodos PyTorch (`gradient_ascent`, `bad_teacher`, `scrub`, `amnesiac`, `boundary`, `ntk`, `fisher`, `unsir`, `ssd`). **© Universiti Malaya → APAC (Malasia)** |
| **machine-unlearning-pytorch** (`torchunlearn`) · https://github.com/Harry24k/machine-unlearning-pytorch | **MIT** ✅ | 12 | Reverificado: **20 algoritmos** (15 de entrenamiento + 5 sin entrenamiento, incluidos SalUn, SCRUB, SISA, FisherForget). NeurIPS 2025, *Unlearning-Aware Minimization* |
| **machine_unlearning** · https://github.com/jjbrophy47/machine_unlearning | 🚫 **sin licencia** | 965 | Reverificado en este pase: **sigue sin `LICENSE`**. Bibliografía 2017–2025, no código. Usable como fuente, no como dependencia |

**La métrica que convierte a OpenUnlearning en pieza vendible y no en herramienta de laboratorio:** entre sus 10+
métricas hay **ataques de inferencia de pertenencia (*membership inference*) y medidas de fuerza de extracción**. No
sólo desaprende: **mide si el desaprendizaje aguanta un ataque.** Eso es exactamente lo que el pase 18 declaró
pendiente en la advertencia de **P38** — convertir la garantía «aproximada» de `pyKT` en un número.

**Y acota el gap 31 con una distinción que hay que escribir bien, porque es la diferencia entre vender integración y
vender investigación:** TOFU, MUSE y WMDP miden olvido de **conocimiento textual en un LLM**. **Ninguno mide un modelo
de *knowledge tracing* ni de *cognitive diagnosis*.** Entonces el tutor LLM está cubierto y es MIT; **el estimador de
mastery no**. Eso es el **gap 34**, nuevo en este pase y el más construible que tiene esta KB: las piezas existen
(`pyKT` es PyTorch, `torchunlearn` es MIT, las métricas de ataque son MIT) y falta el ensamblado.

### 🔴 El lado del ataque, que esta capa no tenía: por qué el dashboard de mastery es el problema

Hasta este pase, toda la capa se justificaba por **obligación legal**. Ahora hay **riesgo técnico medido**, y viene del
mismo grupo que PrivacyCD:

> **P-MIA** — *A Profiled-Based Membership Inference Attack on Cognitive Diagnosis Models* (arXiv **2511.04716**).
> Primer trabajo sistemático de inferencia de pertenencia contra **CDMs**. Modelo de amenaza ***grey-box* que explota
> las funciones de explicabilidad de la plataforma**: los vectores internos de estado de conocimiento se exponen al
> usuario en visualizaciones —**el paper nombra los gráficos de radar**— y **se pueden revertir con precisión desde esas
> visualizaciones**. Combinando probabilidades de predicción + vectores reconstruidos, **supera con claridad** a los
> baselines *black-box* sobre tres datasets reales.

**Le pega a esta KB en particular, no de forma genérica:** el dashboard de mastery es la salida natural de
`pyKT`/`pyBKT`, es lo que `Gnos` instrumenta y lo que la capa predictiva del pase 11 le muestra al docente. **Esta KB
lo viene recomendando.** P-MIA dice que esa visualización **es la superficie de ataque**: cuanto mejor se explica el
modelo, más fácil es extraer de él quién estuvo en el entrenamiento. **La explicabilidad que el Anexo III del EU AI
Act exige y la minimización que el GDPR exige empujan en direcciones opuestas**, y ahora hay un paper que lo mide.
Contramedida concreta, documentada en **P40**: ruido o cuantización en el vector de estado expuesto, o control de
acceso por rol, **y la decisión escrita en el expediente**.

### Y la auditoría que faltaba desde el pase 6: los LRS no borran

Trece pasadas registraron la capa de telemetría por lo que **escribe**. Ninguna preguntó si sabe **borrar**. Empieza
un nivel arriba de los repos: **el estándar xAPI no define una operación de supresión de *statements*** — define
***voiding***, un statement nuevo que marca al anterior como obsoleto **dejando el original en su lugar**. Eso es lo
contrario del art. 17 del GDPR.

| LRS | Licencia | ★ | ¿Documenta borrado? |
|---|---|---|---|
| **SQL LRS (`lrsql`)** | **Apache-2.0** ✅ | 144 | 🚫 **No** |
| **Ralph** | **MIT** ✅ | 51 | 🚫 **No** |
| **Learning Locker** | **GPL-3.0** ⚠️ | 584 | ✅ **Sí** (API especial de borrado) |

**Tercera aparición del mismo patrón en esta KB, y ya no es coincidencia: lo permisivo no borra y lo que borra es
copyleft.** La tendencia 45 lo encontró en el LMS; la capa de *unlearning* parecía invertirlo; acá vuelve a la forma
del LMS. **Y pega sobre una fila de la tabla principal:** `learnmcp-xapi` (MIT) declara como backends `lrsql`, Ralph y
Veracity — **los permisivos, los que no borran**. El stack que esta KB recomienda escribe la historia del alumno en un
almacén del que **no hay forma estándar de sacarla**. Ver el **gap 33**.

⚠️ **Límite declarado:** el «no» es **ausencia en la documentación publicada**, no imposibilidad — las dos son bases
SQL/Elasticsearch y un `DELETE` a mano siempre es posible. La afirmación exacta: **ninguno ofrece el borrado como
operación soportada y documentada**, y por eso ninguno se puede poner en un expediente de privacidad como el
componente que cumple el art. 17. El `DELETE` a mano es trabajo a medida y se cotiza como tal. El «sí» de Learning
Locker es de fuente secundaria y **no se verificó contra su API**. `arxiv.org` sigue bloqueado: P-MIA y PrivacyCD van
por snippets concordantes, con número de arXiv anotado para que el próximo pase los abra.

## 2026-10-01 (pase 18) — la capa que borra la influencia del dato sobre el modelo es toda permisiva, tiene 2.700+ estrellas combinadas y no menciona educación

Este pase ejecuta la segunda acción escrita por el pase 17 y la confirma. La capa existe, es grande, es
**permisiva** —al revés que todo lo que esta KB encontró en privacidad del LMS— y **la educación no la toca**.

### Los repos nuevos, verificados uno por uno

| Repo | Licencia | ★ | Forks | Qué aporta |
|---|---|---|---|---|
| https://github.com/tamlhp/awesome-machine-unlearning | **MIT** ✅ | **970** | 79 | Mapa de la capa + datasets. Survey **ACM TIST 2025**, DOI `10.1145/3749987` |
| https://github.com/jjbrophy47/machine_unlearning | 🚫 **sin licencia declarada** | 965 | 117 | Segundo agregador por tamaño: literatura de *unlearning* desde pre-2017 hasta 2025 (AAAI, ACL, CVPR, NeurIPS). **No muestra licencia** → no cotizar sobre él; corresponde abrir un *issue* pidiendo el archivo |
| https://github.com/chrisliu298/awesome-llm-unlearning | **Apache-2.0** ✅ | 627 | 33 | 616 papers, 18 surveys, 3 frameworks |
| https://github.com/locuslab/open-unlearning | **MIT** ✅ | **607** | 164 | **El framework ejecutable.** TOFU/MUSE/WMDP, 12 métodos, 10+ métricas, 7+ arquitecturas. arXiv 2506.12618 |
| https://github.com/Data-Provenance-Initiative/Data-Provenance-Collection | **Apache-2.0** ✅ | 281 | 48 | Auditoría de 44 colecciones / 1800+ datasets de finetuning; **fichas de procedencia** legibles. arXiv 2310.16787 |
| https://github.com/OPTML-Group/Unlearn-Saliency | **MIT** ✅ | 154 | 29 | **SalUn**, *weight saliency* para unlearning. **ICLR 2024 Spotlight**, arXiv 2310.12508 |
| https://github.com/cisco-ai-defense/model-provenance-kit | **Apache-2.0** ✅ | 104 | 22 | **Cisco AI Defense.** 8 señales de procedencia en un score; `compare` y `scan` contra ~150 modelos base de 45+ familias; streaming +20 GB |
| https://github.com/Harry24k/machine-unlearning-pytorch | **MIT** ✅ | 12 | 2 | **torchunlearn.** Interfaz unificada estilo PyTorch. **NeurIPS 2025**, *Unlearning-Aware Minimization* |
| https://github.com/hxxdtd/Awesome-Diffusion-Model-Unlearning | 🚫 **sin licencia declarada** | 67 | 3 | Recorte de difusión: artículos, recursos y datasets de *unlearning* de conceptos en modelos de difusión. **No muestra licencia** |

**2.700+ estrellas combinadas, ocho de nueve piezas con licencia verificada y las seis con licencia leída son MIT o
Apache-2.0.** Es la segunda capa de esta KB —después de la de privacidad horizontal del pase 16— donde lo maduro
es permisivo. En las otras once, lo maduro es copyleft.

### Lo que cambia en el núcleo de Moodle, verificado por código HTTP

| Ruta en `moodle/moodle` | `main` | `master` | `MOODLE_405_STABLE` | `MOODLE_500_STABLE` |
|---|---|---|---|---|
| `ai/provider/openai/classes/privacy/provider.php` | 404 | 404 | **200** | **200** |
| `ai/provider/azureai/classes/privacy/provider.php` | — | — | — | **200** |
| `ai/provider/ollama/classes/privacy/provider.php` | — | — | — | **200** |
| `ai/provider/bedrock/version.php` | — | — | — | **404** (no está en el núcleo) |
| `ai/provider/anthropic/version.php` | — | — | — | **404** (no está en el núcleo) |
| `admin/tool/dataprivacy/version.php` | — | — | — | **200** |
| `admin/tool/policy/version.php` | — | — | — | **200** |

🔴 **`moodle/moodle` no tiene rama `main` ni `master`.** Los cuatro 404 que el pase 17 registró midieron el nombre
de la rama, no una ausencia. Con esto, `tool_dataprivacy` y `tool_policy` pasan de *documentados por snippet* a
**verificados de primera mano en el núcleo**, y el **gap 29 se cierra**.

Y una baja que hay que registrar: **`moodlehq/moodle-tool_dataprivacy` está ARCHIVADO desde el 2020-09-24**
(GPL-3.0, 8 ★, 11 forks, 199 commits, read-only). No está muerto —**se mudó al núcleo** en Moodle 3.3.8/3.4.5/3.5—
pero **no se propone como dependencia**: se propone la versión del núcleo. Es la segunda vez que esta KB encuentra
implementaciones de referencia apagándose mientras el estándar sigue vivo; la primera fue el pase 9 con las
credenciales europeas.

### Lo que esta capa NO tiene, y es el gap 31

**Ninguna de las nueve piezas menciona educación, dato de alumno ni knowledge tracing.** Verificado buscando los
términos en los dos agregadores grandes (970 ★ y 627 ★): cero apariciones. Lo específicamente educativo es
**PrivacyCD** (arXiv 2511.03966), que ataca exactamente los modelos de *cognitive diagnosis* —la capa de `pyBKT` y
`pyKT`— con el algoritmo **HIF**, y **no publica código**.

**El reparto regional de la capa, declarado:** **North America** concentra la oferta (`locuslab`/CMU,
`OPTML-Group`/Michigan State, `cisco-ai-defense`, `Data-Provenance-Initiative`/MIT Media Lab); **APAC** es segunda
y tiene lo único educativo (`torchunlearn` Corea, `tamlhp` Australia, autores de PrivacyCD); **EMEA** 🚫 **nada
encontrado**, lo que es llamativo porque es donde el derecho de supresión del **GDPR art. 17** es directamente
exigible; **LATAM** 🚫 **nada encontrado** en unlearning, aunque aporta el mejor `privacy provider` de la capa
hermana (`local_aihub`, Brasil). Declarado como **no encontrado, no inexistente**.

---

## 2026-10-01 (pase 17) — la máquina de privacidad del dato del alumno ya estaba instalada en el LMS, es toda copyleft, y el proveedor canónico declara por escrito que no garantiza cumplimiento

El pase 16 abrió la capa de privacidad y la midió **del lado de las librerías** —DP, federado, datos sintéticos— y
cerró con una acción escrita: *«No se revisó la capa de privacidad de los LMS ya instalados (Moodle, Open edX,
Canvas). Es el paso siguiente obvio: el dato del alumno ya está ahí, no en el agente.»* **Este pase ejecutó esa
acción**, y además la que el **gap 26** había dejado escrita. Las dos pagaron, y van dos pases seguidos (14 y 17)
en que ejecutar una acción escrita por un gap anterior rinde más que inventar la pregunta de cero.

**El hallazgo da vuelta la forma del pase 16.** Ahí, lo maduro era permisivo (ocho librerías horizontales,
26.000+ ★, Apache-2.0/MIT) y lo educativo tenía techo de 10 ★. Acá es exactamente al revés: **lo educativo es
maduro, está desplegado en decenas de miles de instituciones, y es todo copyleft.**

### Los repos nuevos, verificados vía WebFetch el 2026-10-01

**Seis repos.** No son seis hallazgos independientes: son las tres plataformas que concentran el dato real del
alumno, más la pieza administrativa, más los dos paquetes de *skills* que cierran el gap 20.

| Repo | Licencia | Stars | Qué aporta a esta capa |
|---|---|---|---|
| https://github.com/openedx/edx-platform | **AGPL-3.0** ⚠️ | 8.2k | *«version 3 of the AGPL unless otherwise noted»*. Trae el toolset de retiro de usuario más completo del sector: `scripts/user_retirement` (seis scripts) + `lms/djangoapps/bulk_user_retirement` (API REST). 4.4k forks |
| https://github.com/moodle/moodle | **GPL-3.0** ⚠️ | 7.5k | *«version 3 of the GNU General Public License»*. 123.147 commits. El **Privacy API** es núcleo y **obliga a los plugins**, que es la propiedad que ninguna otra plataforma de esta KB tiene |
| https://github.com/instructure/canvas-lms | **AGPL-3.0** ⚠️ | 6.9k | «The open LMS by Instructure, Inc.» El código del LMS con ~41 % de la educación superior del continente — y el del incidente del 2026-04-29 (ver abajo) |
| https://github.com/openeducat/openeducat_erp | **LGPL-3.0** ⚠️ | 881 | ERP educativo sobre Odoo. Entra en esta capa por una razón de privacidad, no de ERP: **autohospedado, la institución sigue siendo el responsable del dato** y no hay acuerdo de terceros que complique FERPA en los bordes |
| https://github.com/anthropics/k12-teacher-skills | **Apache-2.0** ✅ | **541** | «Skills and eval rubrics for K-12 teachers, co-developed with Learning Commons». Cuatro skills **y una carpeta `evals/`** |
| https://github.com/learning-commons-org/agent-skills | **Apache-2.0** ✅ | 35 | Las mismas cuatro skills del lado del consorcio educativo, con `evals/` de rúbricas de **pedagogía, rigor, formato y andamiaje del modelo** |

### 🔴 El hallazgo de licencia, y es el que decide si esta capa se puede proponer

**Las tres plataformas que tienen el dato son copyleft fuerte: GPL-3.0, AGPL-3.0, AGPL-3.0.** Y AGPL-3.0 es la
licencia que esta KB viene marcando como la más difícil de toda su «Nota sobre licencias», porque la cláusula de
red alcanza al servicio, no sólo al binario distribuido.

**Pero acá el copyleft no bloquea el entregable, y conviene decir por qué**, porque es el único caso de dieciséis
pasadas en que el copyleft **no** es la mala noticia: no hay que forkear ni redistribuir la plataforma. El Privacy
API de Moodle es un **punto de extensión** —se implementa un *provider* en un plugin— y el retiro de Open edX se
**invoca**: seis scripts y un endpoint REST. Lo que se entrega es el plugin, el expediente y la operación, no una
derivada del LMS. La pregunta de licencia se mueve del LMS al plugin, y ahí sí hay que elegir.

### Lo que esta capa NO tiene, y es el gap 29

Ninguna de las seis piezas habla con un agente. **No hay servidor MCP, ni herramienta LTI, ni plugin que conecte
un agente al Privacy API de Moodle ni al retiro de Open edX.** Se buscó explícitamente. Es la misma forma que el
pase 15 encontró en procedencia —la infraestructura está, el puente al aula no— y van tres capas seguidas con
exactamente ese diagnóstico.

### ⚠️ La advertencia que hay que leer antes de cotizar: el proveedor declara que no garantiza cumplimiento

La documentación de Open edX dice, textualmente: **«User retirement is not a compliance guarantee. The Open edX
software makes no claim of satisfying any law or regulation. It is a configurable toolset that site operators can
use to help meet the obligations apply to them specifically.»**

Es la frase más útil de este pase para una propuesta, y hay que usarla en el sentido correcto: **no dice que la
herramienta sea mala, dice que el cumplimiento es del operador del sitio.** Eso es precisamente el alcance que se
vende —configurar, evidenciar y operar— y es la razón por la que P36 existe.

🔴 **Y hay que declarar de dónde sale la cita.** `docs.openedx.org`, `docs.moodle.org` y `moodle.org` están
**bloqueados por el proxy de egreso de esta sesión**. La frase se leyó en el snippet de búsqueda que devuelve esa
página, **no en un fetch de primera mano**, y el `README` del directorio `scripts/user_retirement` en GitHub —que
sí se verificó— **no la contiene**. Antes de ponerla en un documento para un cliente, resolverla contra la fuente
oficial. Lo verificado de primera mano es el **código**: los seis scripts y el Django app existen y están
nombrados arriba.

### Lo que esta pasada buscó y no encontró

- **Un plugin de LMS que haga gobernanza de AI** (registro de qué modelo tocó qué dato de qué alumno): no existe
  en abierto, ni en Moodle ni en Open edX. Lo que hay en el directorio de Moodle para privacidad es
  **cumplimiento de GDPR del dato propio del LMS**, no del dato que sale hacia un modelo.
- **Un `privacy provider` de referencia para un plugin de AI**: no se encontró ninguno publicado. Es la pieza más
  chica y más vendible de esta capa, y la nombra P36.
- **Equivalente de retiro de usuario en Canvas**: no se ubicó en abierto un toolset comparable al de Open edX. Se
  declara como no encontrado, no como inexistente: `canvas-lms` es un repo de 6.9k ★ y no se auditó su árbol
  completo en este pase.

### Nota de método de este pase

**`curl -sI` no sirve para verificar en esta sesión y hay que dejar de intentarlo.** Se probó contra tres repos
reales y contra uno deliberadamente inexistente
(`github.com/this-definitely-does-not-exist-xyz123/nope`): **los cuatro devolvieron 403.** El proxy responde 403
antes de llegar a GitHub, así que un 403 no distingue un repo vivo de uno que no existe. El pase 16 ya lo había
anotado; este pase lo probó con un control negativo. **La verificación de este pase es WebFetch contra la página
del repo**, y cuatro dominios dieron bloqueo de egreso: `moodle.org`, `docs.moodle.org`, `docs.openedx.org`,
`privacyrights.org`, `calmatters.org` y `leginfo.legislature.ca.gov`.

**Y una corrección de alcance sobre el propio pase:** se intentó verificar el árbol de `admin/tool/dataprivacy`
dentro de `moodle/moodle` por cuatro rutas distintas (`main` y `master`, árbol y archivo) y **las cuatro dieron
404 vía WebFetch**. Por eso este pase **no afirma de primera mano** la existencia de ese directorio: afirma lo que
verificó —licencia, estrellas y commits del repo— y registra el Privacy API y el plugin Data Privacy como
**documentados por Moodle vía snippet de búsqueda**, con el mismo descuento que la cita de Open edX.

## 2026-10-01 (pase 16) — la capa que decide si las otras quince pueden tocar dato real: lo horizontal es maduro y permisivo, lo educativo tiene techo de 10 estrellas, y la herramienta canónica dejó de ser open source

Dieciséis pasadas. Esta KB tiene agente, modelado, evaluación, seguridad, telemetría, datos, accesibilidad,
credencial, contenido, práctica, voz y autoría. **Ninguna pasada preguntó con qué derecho el sistema toca el dato
real del alumno.** Se midió antes de abrir la capa, sobre los ocho archivos: `COPPA` **0 apariciones**,
`differential privacy` / `privacidad diferencial` **0**, `federated` / `federado` **0**, `FERPA` **1**, y esa
única aparición estaba dentro de la descripción de un repo de otra capa.

### Los quince repos nuevos, verificados vía WebFetch el 2026-10-01

**Bloque 1 — privacidad diferencial. Es la única capa de esta KB donde todo lo maduro es permisivo:**

| Repo | Licencia | ★ | Forks | Commits | Qué es |
|---|---|---|---|---|---|
| https://github.com/OpenMined/PySyft | **Apache-2.0** ✅ | **10.0k** | 2.0k | **36.954** | El cómputo viaja al dato, no al revés. v0.10+ modular (`syft-rds`, datasets, jobs, permisos) |
| https://github.com/google/differential-privacy | **Apache-2.0** ✅ | **3.4k** | 436 | — | Building blocks DP en C++/Go/Java/Python + Privacy on Beam + PipelineDP4j |
| https://github.com/pytorch/opacus | **Apache-2.0** ✅ | **2.0k** | 398 | 814 | DP en PyTorch con ~2 líneas; contador de presupuesto en vivo. ⚠️ última actividad **2024-12-18** |
| https://github.com/tensorflow/privacy | **Apache-2.0** ✅ | **2.0k** | 477 | — | Optimizadores DP para TF. ⚠️ última actividad **2024-02-14** (v0.9.0); no archivado |
| https://github.com/IBM/differential-privacy-library | **MIT** ✅ | **920** | 208 | 595 | DP de propósito general con API scikit-learn. Licencia leída en `LICENSE.md`, no en el sidebar |
| https://github.com/opendp/opendp | **MIT** ✅ | **437** | 78 | 990 | Rust + Python/R. *President and Fellows of Harvard College*. La referencia académica formal |

**Bloque 2 — federado, y la categoría se consolidó en un solo nombre entre pasadas:**

| Repo | Licencia | ★ | Forks | Commits | Estado |
|---|---|---|---|---|---|
| https://github.com/adap/flower | **Apache-2.0** ✅ | **7.2k** | 1.2k | **5.841** | Activo. Agnóstico de framework ML |
| https://github.com/securefederatedai/openfl | **Apache-2.0** ✅ | 843 | 237 | — | 🔴 **Deprecado, y remite a Flower por nombre** |

El repo de OpenFL lo dice él mismo: *«no longer under active development and will soon be archived… we recommend
the community transitions to **Flower** framework using the migration guide created in collaboration between our
teams»*. **Un competidor que se retira y nombra al ganador no es ruido de mercado: es la decisión técnica ya
tomada.**

**Bloque 3 — datos sintéticos, y acá está el hallazgo del pase:**

| Repo | Licencia | ★ | Forks | Qué es |
|---|---|---|---|---|
| https://github.com/sdv-dev/SDV | 🔴 **Business Source License 1.1 — no es open source** | **3.6k** | 423 | El canónico del espacio. Nació en el **Data to AI Lab del MIT (2016)**; hoy lo desarrolla **DataCebo, Inc.** |
| https://github.com/vanderschaarlab/synthcity | **Apache-2.0** ✅ | **687** | 98 | **DP-GAN y PATEGAN** adentro, más CTGAN/TVAE/flows/bayesianas/LLM. Series temporales y supervivencia. **Métricas de *correctness* y de *privacy*** |
| https://github.com/ydataai/ydata-synthetic | **MIT** ✅ | **1.7k** | 257 | Tabular y series temporales con GANs sobre TF2. ⚠️ el paquete **migró** a `fg-data-synthetic`, con guía de migración en el README |

**Bloque 4 — lo específico de educación, donde se cae todo:**

| Repo | Licencia | ★ | Commits | Qué es |
|---|---|---|---|---|
| https://github.com/Akulen/PrivGen | **MIT** ✅ | **3** | 15 | RNN de generación sintética educativa, **EC-TEL 2022**. Evalúa con **IRT** y con **riesgo de reidentificación** |
| https://github.com/hxwujinze/federated-deep-knowledge-tracing | ⚠️ **sin licencia** | **10** | 5 | Código del paper *Federated Deep Knowledge Tracing* |
| https://github.com/TarunRaina/FedGNN-for-Personalized-Knowledge-Tracing | ⚠️ **sin licencia** | **1** | 30 | **FedGKT**: 722 conceptos, **1.401 aristas de prerrequisito anotadas por expertos**, GAT + FedAvg/FedProx **sobre Flower**, dataset Junyi (25M interacciones) |
| https://github.com/drsanjayagal/SynEdu-HEDL | ⚠️ **sin licencia** | **1** | 2 | **20.000 alumnos sintéticos**, 180 cursos, 120k+ eventos LMS, ~300k evaluaciones, 6 tablas |

### 🔴 Por qué este pase no termina en «ya tenemos con qué cumplir»

**Primero: la herramienta que el cliente va a nombrar ya no se puede usar.** `SDV` es el nombre canónico de datos
sintéticos tabulares y salió del MIT, pero su `LICENSE` es **BUSL 1.1**: licenciante **DataCebo, Inc.**, *Change
Date* a **cuatro años de cada release**, *Change License* **MIT** recién entonces, uso en producción **prohibido**
sin licencia comercial, y una restricción redactada así: *«You may not use the Licensed Work… for a Synthetic Data
Service»*, definido como toda oferta comercial que dé a terceros acceso a sus capacidades de generación de datos
sintéticos. **La BUSL no está aprobada por OSI** —es la familia de Terraform y Vault— y ese párrafo describe con
precisión incómoda lo que hace un studio de consultoría. El reemplazo es **`synthcity`** (Apache-2.0), que además
trae DP *dentro* del generador y métricas para demostrarlo.

**Segundo: el patrón de las cinco capas anteriores se repite exacto.** Lo horizontal —DP y federado— es maduro,
tiene decenas de miles de estrellas y es todo Apache-2.0 o MIT. Lo que es **específicamente educativo** tiene
techo de **10 ★** y **tres de los cuatro repos no declaran licencia**, así que no son reutilizables por mucho que
el código sirva. El único permisivo de la capa educativa, `PrivGen`, tiene **3 ★**.

**Y lo que eso significa para una propuesta:** la infraestructura de privacidad **no hay que construirla** —está
hecha, es permisiva y es de Harvard, Google, Meta e IBM—. Lo que no existe es **el puente entre esa
infraestructura y el dato educativo**, y ese puente es trabajo de integración, que es exactamente lo que un studio
vende. `FedGKT` muestra que es factible (ya corre sobre Flower) y muestra por qué no alcanza: 1 estrella y sin
licencia.

⚠️ **Dos fuentes bloqueadas por el proxy de egreso, y se declaran:** `nature.com` (el paper de `SynEdu-HEDL` en
*Scientific Reports*, `s41598-026-44990-8`) y `arxiv.org` (`2604.04195`, síntesis por cópulas con marginales
empíricas). Los números de los repos salen de sus páginas de GitHub, que sí se leyeron; **la metodología publicada
no se verificó de primera mano.**

Ver los **trends 39, 40 y 41**, los **gaps 27 y 28** y los patrones **P34** y **P35**.

## 2026-10-01 (pase 15) — la capa que prueba la autoría: la detección es permisiva y no se puede usar, el marcado es permisiva y nadie lo usa, y el estándar que Europa canonizó tiene 1.907 commits

Quince pasadas. La capa de integridad académica existía en esta KB desde el pase 8 **y era sólo proctoring** —
registrado explícitamente como *roadmap, no componente*. La mitad que falta, la de **autoría**, es la que decide
si un entregable de evaluación sumativa se puede defender. Este pase la abre y la verifica repo por repo.

### Los diez repos nuevos, verificados vía WebFetch el 2026-10-01

**Bloque 1 — marcado en el origen (*watermarking*), que es el que cumple el Artículo 50:**

| Repo | Licencia | ★ | Forks | Commits | Qué es |
|---|---|---|---|---|---|
| `huggingface/transformers` → `src/transformers/generation/watermarking.py` | **Apache-2.0** ✅ | — | — | — | **SynthID-Text en producción.** Clases leídas en el archivo: `SynthIDTextWatermarkLogitsProcessor`, `SynthIDTextWatermarkDetector`, `BayesianDetectorModel`, `BayesianDetectorConfig`, `BayesianDetectorWatermarkedLikelihood`. Cabecera: *«Copyright 2024 The HuggingFace Inc. team and Google DeepMind»* |
| https://github.com/THU-BPM/MarkLLM | **Apache-2.0** ✅ | **1.100** | 95 | 185 | Toolkit de watermarking: **23+ algoritmos** (KGW, Unigram, SWEET, UPV, EWD, SIR, X-SIR, DiPmark, SemStamp, k-SemStamp, EXP/EXPGumbel, **SynthID-Text**, MorphMark…) y **12 herramientas de evaluación** en detectabilidad, robustez e impacto en calidad. EMNLP 2024 Demo |

**Bloque 2 — procedencia del artefacto (C2PA), que es lo que el Code of Practice europeo canonizó:**

| Repo | Licencia | ★ | Forks | Commits | Qué es |
|---|---|---|---|---|---|
| https://github.com/contentauth/c2pa-rs | **MIT *y* Apache-2.0** (dual) ✅ | **424** | 192 | **1.907** | SDK Rust del core C2PA: crear, firmar, validar e incrustar manifiestos. Claims **C2PA v2**, spec **2.4**, *CAWG identity assertion*, API en C, callbacks de progreso y cancelación |
| https://github.com/contentauth/c2pa-python | **Apache-2.0 *y* MIT** (dual) ✅ | 105 | 35 | 344 | Binding Python del anterior, **Python 3.10+**. Leer/validar manifiestos y crear/firmar/adjuntar. Mantenido |

**Bloque 3 — detección forense, toda permisiva y toda con el mismo problema:**

| Repo | Licencia | ★ | Forks | Commits | Qué es |
|---|---|---|---|---|---|
| https://github.com/baoguangsheng/fast-detect-gpt | **MIT** ✅ | **434** | 85 | 76 | **ICLR 2024**. Zero-shot por curvatura de probabilidad condicional, **340× más rápido que DetectGPT**. AUROC **0,9887** (5 modelos) y **0,9338** (ChatGPT/GPT-4). Python 3.8 / PyTorch 1.10, probado en A100 80 GB |
| https://github.com/ahans30/Binoculars | **BSD-3-Clause** ✅ | **420** | 67 | 54 | **ICML 2024**. Zero-shot sin datos de entrenamiento; dos modelos de pesos abiertos en inferencia. Devuelve score + binario |
| https://github.com/liamdugan/raid | **MIT** ✅ | **216** | 98 | **378** | **ACL 2024**. El benchmark compartido: **10M+ documentos**, 11 LLMs (ChatGPT, GPT-4, GPT-3, GPT-2 XL, Llama 2 70B, Cohere, MPT-30B, Mistral 7B), **11 dominios** (arXiv, recetas, Reddit, resúmenes de libros, noticias, poesía, reseñas, Wikipedia, código), 4 estrategias de decodificación y **12 ataques adversarios**. Leaderboard `raid-bench.xyz` |
| https://github.com/NLP2CT/LLM-generated-Text-Detection | **MIT** ✅ | **252** | 16 | 40 | Survey vivo con ~100+ papers, 17+ datasets (HC3, CHEAT, DetectRL, DetectRL-X), métodos y **ataques adversarios**. Paper en *Computational Linguistics* **51(1), 2025** |
| https://github.com/pablocaeg/sloptotal | **MIT** ✅ | 39 | 8 | 58 | Ensamble auto-hospedado de **23 motores** que **corre en CPU**: 8 clasificadores neuronales, 6 estadísticos (Log-Rank, GLTR, perplejidad, cross-perplejidad, **Fast-DetectGPT**, **Binoculars**, DivEye) y 7 heurísticas lingüísticas. Acepta texto, PDF, DOCX y URLs |
| https://github.com/Lendarixon/awesome-ai-detection | **CC0-1.0** ✅ | 0 | 0 | 4 | Catálogo con los **modos de falla medidos**, que es lo único que no se consigue en el README de los detectores |

### 🔴 Por qué este pase no termina en «ya tenemos detección»

Los seis repos del bloque 3 son reales, permisivos y están publicados en ICLR, ICML y ACL. **Y ninguno se puede
poner en un entregable que produzca una consecuencia para un alumno.** Los números son de los propios autores:

| Medición | Valor | Fuente |
|---|---|---|
| FPR sobre escritura de **no nativos de inglés** (ensayos TOEFL, 7 detectores) | **61,3 %** | Liang et al. |
| FPR sobre universitarios **nativos**, mismos detectores | ~2,9 % | Liang et al. |
| FPR sobre 1.180 abstracts académicos **anteriores a 2018** | **5,85 %**, más 20 % en «incierto» | `awesome-ai-detection` |
| Texto humano mal marcado por el ensamble de 23 motores | 1 de 66 | README de SlopTotal |
| Umbral de longitud por debajo del cual el score no sirve | **~80 palabras**; estabiliza en ~200 | README de SlopTotal |
| Efecto de la paráfrasis sobre la exactitud | **caídas grandes** | RAID |

Y **Binoculars lo dice en su propio README**: *«more proficient in detecting English language text compared to
other languages»*, *«for academic purposes only»*, con **supervisión humana** requerida.

**La aritmética de Vanderbilt es la que hay que llevar a la reunión:** 1 % de FPR sobre 75.000 trabajos son
**~750 acusaciones injustas por año**. Vanderbilt desactivó el detector de AI de Turnitin; **más de 50
universidades** de EE. UU., Reino Unido, Canadá, Australia y Sudáfrica lo desactivaron, restringieron o lo
abandonaron (Johns Hopkins, Yale, Waterloo, Curtin, Australian Catholic University), **al menos 12 instituciones
grandes a marzo de 2026**.

**La regla que este pase deja escrita para toda la KB:** un score de detección es **evidencia, no prueba**.
Sirve para **priorizar una conversación docente**, nunca para disparar una sanción. Y sobre alumnos que escriben
inglés como segunda lengua —es decir, el alumno modal de LATAM, EMEA no anglófona y buena parte de APAC— el
61,3 % lo vuelve **pasivo legal antes que producto**. Ver el **gap 25**.

### El contraste que hace útil este pase, y es el mismo patrón del pase 14 con el signo cambiado

| | **Detectar** (post-hoc, forense) | **Marcar** (en el origen, procedencia) |
|---|---|---|
| Licencia | MIT / BSD-3 / Apache-2.0 ✅ | **Apache-2.0 / MIT dual** ✅ |
| Madurez | ICLR, ICML, ACL; 216–434 ★ | **1.907 commits** (c2pa-rs); dentro de Transformers |
| ¿Funciona? | **No de forma defendible**: 61,3 % FPR en no nativos, se rompe con paráfrasis | **Sí, con certeza criptográfica** |
| Límite real | Es un **juicio probabilístico sobre texto ajeno** | Sólo cubre texto que **generó tu propio sistema** |
| Estado regulatorio EMEA | Ninguno | **Obligatorio: Art. 50(2), 2026-12-02** |
| Uso en educación open source | Ninguno integrado | **Ninguno** — y es el gap barato |

**La lectura de arquitectura, y es el aporte conceptual del pase:** la pregunta *«¿esto lo escribió una AI?»* no
tiene respuesta confiable y nunca la va a tener. La pregunta *«¿esto lo escribió **nuestro** tutor?»* **sí**, y
la respuesta es una verificación, no una estimación. **Una institución que provee el agente puede marcarlo en el
origen**, y entonces la integridad deja de ser forense. Es exactamente el patrón que esta KB ya tiene desplegado
en otras cinco capas (tendencia 29: *lo que se conecta al estándar instalado escala*), aplicado a la autoría.
El recetario está en **P33**.

### El repo que no entra en ninguna tabla y hay que registrar igual

**`ervin-mo/humanizar-es`** (https://github.com/ervin-mo/humanizar-es, **MIT**, 0 ★, 6 commits) reescribe texto
en español para evadir detectores, usando **Binoculars y Fast-DetectGPT sobre Qwen2.5-0.5B** como guía local, y
está empaquetado como **`SKILL.md` para Claude Code, Codex, OpenCode, Antigravity, DeepSeek Harness y Gemini
CLI**. El autor declara 100 % → 0 % en un párrafo y 39 % en un ensayo completo, acota que la evidencia es **un
solo ensayo** y aclara que **no está pensado para entregar trabajo calificado**.

**No es el repo, es el canal.** El pase 12 midió que la educación perdió el canal de *skills* de agente frente a
la vertical científica (815 ★ *share-alike* contra 47,2k ★ MIT). Acá aparece ese canal **ocupado en el dominio
educativo, por el lado adversario, en español y con licencia MIT**. Es el **gap 26**.

### Lo que esta pasada buscó y no encontró

- **Cualquier integración educativa de watermarking.** Cero. Ni plugin de LMS, ni herramienta LTI, ni servidor
  MCP que marque o verifique la salida de un tutor. La infraestructura es Apache-2.0 y madura; **el puente al
  aula no existe**.
- **Integridad académica open source de punta a punta en Moodle.** Lo del directorio son **envoltorios de
  servicios propietarios**: Compilatio (plugin **GPL-3.0**, 821 instalaciones, release 2026-06-25),
  Originality.ai (Moodle 3.9–5.0, release 2026-07-02), Copyleaks. Plugin libre, **detector pago**.
- **Evidencia de proceso en abierto.** Nada: GPTZero Authorship, Grammarly Authorship, Turnitin Clarity y
  Draftback son todos propietarios.
- 🔴 **Nota de verificación — tres dominios bloqueados por el proxy de egreso en este pase:** `arxiv.org`
  (quedaron sin abrir 2601.17280 sobre *timing-forgery* contra detección por pulsaciones, y 2608.26710 sobre
  estilo como confusor en escritura de no nativos), `zenodo.org` (el dataset de políticas de integridad de las
  15 universidades LATAM mejor rankeadas en THE 2026) y `huggingface.co`. **Todo lo de GitHub de este pase sí se
  abrió y se leyó en la página del repo.** Las afirmaciones regulatorias vienen de resultados de búsqueda:
  `digital-strategy.ec.europa.eu`, `artificialintelligenceact.eu` e `iptc.org` también están bloqueados.
- 🔴 **Discrepancia de fecha sin resolver:** el **Code of Practice** europeo sobre marcado y etiquetado de
  contenido AI aparece con fecha de publicación **10 de junio de 2026** en una fuente y **20 de julio de 2026**
  en otra. **Resolver contra la fuente oficial antes de citarla a un cliente.** Lo que sí es consistente:
  Artículo 50 en vigor **2026-08-02**, marcado legible por máquina para sistemas ya en mercado **2026-12-02**, y
  **C2PA Content Credentials como estándar técnico de facto** del metadato incrustado, en esquema por capas
  (metadato + watermarking, con fingerprinting y logging de apoyo).

---

## 2026-10-01 (pase 14) — el gap 19 se cerró a propósito: las cuatro piezas que el pase 13 dejó sin verificar existen, y la capa ya tenía un estándar de interoperabilidad que catorce pasadas no vieron

Este pase hizo lo que el gap 19 pedía textualmente: *«buscar explícitamente `curriculum ontology`, `achievement
standards`, `learning map` y `prerequisite graph` por país, en el idioma del país, en vez de esperar que aparezcan
buscando agentes.»* Se buscó así. **Las cuatro candidatas que el pase 13 listó como "sin verificar" existen las cuatro**,
y aparecieron dos cosas que el gap no anticipaba.

### 🔴 El hallazgo del pase: esta capa no es un conjunto de artefactos sueltos, es un estándar con implementaciones certificadas

El gap 19 trataba los esquemas curriculares como artefactos nacionales independientes —el coreano, el español— y la
acción que proponía era coleccionarlos país por país. **Eso era la mitad del problema.** La otra mitad es que
**1EdTech publica desde hace años el estándar que define cómo se publica e intercambia un marco curricular
—CASE®, *Competencies and Academic Standards Exchange*— y tiene implementaciones open source certificadas.**

Catorce pasadas no lo vieron, y el pase 9 pasó al lado: abrió la capa 1EdTech de **credenciales** (Open Badges, CLR) y
no miró la de **competencias y estándares**, que es la misma familia de especificaciones.

| Repo | Licencia | ★ | Qué es | Estado de conformidad |
|---|---|---|---|---|
| [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | **MIT** ✅ | **45** | *Standards Alignment Tool*: autoría, gestión, alineación y *crosswalk* de marcos de competencias. PHP/Symfony, MySQL, Docker | ⚠️ Último estable **3.2.0 (sept 2023)**, apunta a **CASE v1.0**; v1.1 en rama `develop` |
| [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) | **Apache-2.0** ✅ | **9** | Servidor + editor visual CASE del propio organismo de estándares. Multi-tenant, API de publicación | ✅ **v0.2 certificado para CASE Service v1.0 y CASE v1.1, certificaciones con fecha 2026-02-17** |
| [`infosign/compeito`](https://github.com/infosign/compeito) | **Apache-2.0** ✅ | **3** | Servidor CASE v1.1 moderno: Python 3.12/FastAPI, PostgreSQL, HTMX, import/export CSV compatible OpenSALT, Docker | ✅ Endpoints *Provider* CASE v1.1; importa CFPackages de OpenSALT y OpenCASE |
| [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) | **MIT** ✅ | **2** | Herramienta de verificación de conformidad a **once** estándares educativos a la vez | ✅ CASE 1.1, xAPI (1.0.3 + IEEE 2.0), QTI 2.1/2.2/3.0.1, LTI 1.3 (+DL/AGS/NRPS/Proctoring), OneRoster 1.2, Common Cartridge 1.3/1.4, CLR 2.0, Open Badges 3.0, Caliper 1.2, cmi5, W3C VC 2.0 |

**Y la distribución de estrellas repite exactamente el patrón que el pase 10 encontró con Sunbird (41 ★) y el pase 9 con
los estándares de interoperabilidad: la pieza con más estrellas es la que está más atrás del estándar.** OpenSALT tiene
**45 ★** y su último estable es de **septiembre de 2023** contra **CASE v1.0**; OpenCASE tiene **9 ★** y está
**certificado contra v1.1 con fecha de febrero de 2026**. Un filtro por popularidad elige la pieza vieja. Es la tercera
vez que esta KB mide lo mismo, y conviene dejar de llamarlo coincidencia.

### Las cuatro piezas que el pase 13 dejó sin verificar, verificadas una por una

| Artefacto | Región | País | Licencia | Contenido verificado | ★ |
|---|---|---|---|---|---|
| [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | **LATAM** | Brasil | **MIT** (código) + **CC BY 4.0** (datos) ✅ | **1.721 aprendizagens** en JSON, SQLite y CSV — 1.580 de las tres etapas de educación básica + **141 de Computação** (Parecer CNE/CEB 2/2022). Desglose: 93 Educação Infantil, 1.304 Fundamental, 183 Médio, 5 perfiles de referencia, 20 marcos legales. **Proveniencia por registro** y pipeline de extracción reproducible, verificado carácter por carácter contra el documento oficial del MEC | **19** |
| [`fh-yarbouh/oak-curriculum-ontology`](https://github.com/fh-yarbouh/oak-curriculum-ontology) | **EMEA** | Inglaterra | **OGL-3.0** (ontología/datos) + **MIT** (código) ✅ | Oak National Academy alineado al *National Curriculum for England (2014)*. **50.948 *key learning points*, 11.207 *misconceptions*, 7.432 prerrequisitos, 12.517 *pupil lesson outcomes*, 13.012 *keywords*, 160 *threads* de progresión, 12 materias.** 31 clases, 75 propiedades, **38 *shapes* SHACL**. Turtle, JSON-LD, RDF/XML, N-Triples, SQLite y JSONL de grafo de propiedades | **0** |
| [`commonstandardsproject/api`](https://github.com/commonstandardsproject/api) | **North America** | EE. UU. | **Apache-2.0** ✅ | Estándares académicos de **los 50 estados** más organizaciones, distritos y escuelas, en JSON formateado para empresas de tecnología educativa K-12. **API en vivo** en `api.commonstandardsproject.com` con alta de API keys | **44** |
| **MRAC** — *Machine Readable Australian Curriculum* (ACARA) | **APAC** | Australia | ⚠️ **NO VERIFICABLE EN ESTA SESIÓN** | Currículo australiano **v9.0** publicado en RDF/XML, manifiestos JSON y endpoint SPARQL en `rdf.australiancurriculum.edu.au/api/sparql` | n/a |

🔴 **La cuarta no se pudo verificar y se declara en vez de callarse:** `www.australiancurriculum.edu.au` está
**bloqueado por el proxy de egress de esta sesión**. La existencia, los formatos y el endpoint SPARQL están
confirmados por fuentes secundarias coincidentes; **la licencia de reuso no**. Es el mismo tipo de hueco que el
pase 9 declaró como gap 14, y tiene la misma regla: **no cotizar MRAC sin abrir antes los términos de uso de ACARA.**

### Los dos puentes agente↔currículo de Brasil, y uno de ellos mueve el gap 15

| Repo | Licencia | ★ | Qué hace |
|---|---|---|---|
| [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) | **MIT** ✅ | **14** | **Servidor MCP** de la BNCC con cinco herramientas: `bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_mapa_de_foco`, `bncc_estatisticas`. **1.717 habilidades** (1.408 Fundamental, 104 Infantil, 205 Médio), **141 de Computação** por ejes, y **396 habilidades priorizadas** por el **Mapa de Foco del Instituto Reúna** con capa pedagógica |
| [`aprincar/curriculum-bncc`](https://github.com/aprincar/curriculum-bncc) | ⚠️ **AGPL-3.0** | **0** | *Crosswalk* de IDs de habilidad propios a referencias BNCC con cuatro tipos de relación: `direct`, `partial`, `supports`, `prerequisite`, validado contra catálogos versionados |

**`bncc-mcp` es el dato comercial del pase.** El gap 15 dice que *«ningún puente agente↔contenido curricular tiene
tracción, y el único que existe declara mal la licencia»*. Acá hay un puente **MIT**, con **proveniencia declarada**,
que expone un currículo nacional completo por MCP **y además la capa de priorización pedagógica** —que es un juicio
curricular, no un dato—. Con **14 ★** no es tracción, pero **sí es la pieza que faltaba**, y es de **LATAM**.

### Lo que esta pasada buscó y no encontró

- **Singapur:** el gap 19 lo listaba como candidato. **No aparece ningún esquema curricular singapurense estructurado y
  publicado abiertamente.** Es el único de los cinco candidatos del pase 13 que **no** se confirmó.
- **México, Colombia, Argentina, Chile, Perú:** se buscó en español por currículo nacional estructurado. **Nada.**
  Brasil es, por ahora, **el único país de LATAM con su currículo nacional publicado como datos abiertos verificados.**
  Eso convierte a `bncc-dados` en el modelo replicable, no en el caso aislado.
- **Un esquema curricular publicado *como* marco CASE por un ministerio.** Las piezas que publican CASE son
  herramientas; los marcos nacionales que encontramos se publican en RDF (Australia, Inglaterra, Corea) o en JSON
  propio (Brasil, EE. UU.). **Nadie cerró el círculo**, y ese es el gap 23 que abre este pase.
- **`arxiv.org` sigue bloqueado por el proxy** —igual que en el pase 13—, así que la literatura de ASR infantil
  (incluido `arXiv 2606.31508`, solución ASR para lectura infantil en bambara) **no se pudo verificar en origen** y
  queda registrada como referencia secundaria, no como hallazgo.

## 2026-10-01 (pase 13) — el repo con más estrellas de toda esta KB no se presenta como educativo, y es el aula de STEM desde 2014

Decimotercera corrida. El pase 10 cambió el indicador (estrellas → despliegue real), el 11 cambió el filtro (licencias
más allá de MIT/Apache/BSD) y el 12 cambió la unidad de análisis (repos → canal de distribución). **Este pase cambia la
consulta**: en vez de buscar «agente educativo» o «grading», busca **dónde ocurre materialmente el trabajo del alumno**.
Y ahí aparece la capa con más estrellas, mejor licencia y mayor despliegue real de toda esta KB.

### Los cinco repos nuevos, verificados vía WebFetch el 2026-10-01

| Repo | Licencia | Stars | Forks | Señal |
|---|---|---|---|---|
| https://github.com/jupyterhub/jupyterhub | **BSD-3-Clause** ✅ | **8.300** | 2.100 | **Es el repo con más estrellas de toda esta KB**, y no figuraba. Servidor multiusuario de notebooks: un entorno aislado por alumno |
| https://github.com/jupyterlab/jupyter-ai | **BSD-3-Clause** ✅ | **4.400** | 528 | «Connects AI agents to computational notebooks». **ACP + MCP**, autodetección de Claude, Codex, Copilot, Gemini, Goose, Kiro, Mistral Vibe y OpenCode. Declara estándares abiertos explícitamente para evitar *lock-in* de proveedor |
| https://github.com/jupyter/nbgrader | **BSD-3-Clause** ✅ | **1.400** | 342 | **v0.9.6 publicada el 2026-09-30** — el día anterior a este pase, con *fixes* de *path traversal*. 3.477 commits. Autocorrección + tramos manuales + tests ocultos |
| https://github.com/ucbds-infra/otter-grader | **BSD-3-Clause** ✅ | 161 | 81 | **UC Berkeley, Data Science Education Program.** 3.820 commits. La opción sin acoplamiento a JupyterHub |
| https://github.com/jupyterhub/ltiauthenticator | **BSD-3-Clause** ✅ | 73 | 56 | **LTI 1.3 y 1.1**, probado contra **Open edX, Canvas y Moodle**. Es el puente hacia el stack que esta KB ya tenía |

**14.334 ★ en una sola familia de licencia permisiva.** Para comparar con lo que esta KB venía midiendo: la capa de
evaluación pedagógica tiene techo de 42 ★, la capa MCP de mastery techo de 42 ★, la capa predictiva techo de 6 ★ y la
capa de *skills* educativas techo de 815 ★ con *share-alike*.

### El contraste que hace útil este pase

Las doce pasadas anteriores produjeron un diagnóstico muy consistente y, visto desde acá, **sesgado por la consulta**:

| Lo que la KB concluyó, pase tras pase | Qué pasa en esta capa |
|---|---|
| «Lo desplegable es copyleft» (Moodle GPL, Open edX y Canvas AGPL) | **BSD-3-Clause en los cinco repos** |
| «Lo permisivo es de juguete» (tutores LATAM 0–3 ★) | **8.300 ★ y despliegue universitario desde 2014** |
| «Los datos son NonCommercial» (gap 11) | No aplica: la evidencia la genera el alumno del cliente |
| «El runtime de agente hay que construirlo» | **Ya existe, con MCP, y es BSD** |
| «El grading open source no existe» (gap 6, once pasadas) | **Existe para trabajo computacional, y es el incumbente real** |

### Los otros dos repos nuevos del pase

| Repo | Licencia | Stars | Señal |
|---|---|---|---|
| https://github.com/microsoft/Shiksha-Copilot | **MIT** ✅ | **9** | **9 estrellas, 1.043 docentes de Karnataka.** Microsoft Research India / VELLM. Inglés y kannada. 149 commits, 12 forks. ⚠️ El repo se autodeclara prototipo de investigación no apto para producción sin validación extensa |
| https://github.com/AI-for-Education/pedagogy-benchmark | **MIT** ✅ | 12 | 1.143 preguntas de **exámenes de habilitación docente del Ministerio de Educación de Chile** (Agencia de la Calidad + CPEIP). Incluye **SEND**, 223 preguntas de educación especial. arXiv 2506.18710. 5 commits |

La organización **AI-for-Education** («Empowering Education in LMIC's with AI», `AI-for-education.org`) tiene **21
repos** y su techo es de **12 ★** — otros: `fabdata-llm` (9 ★, interfaz a APIs de LLM y gestión de chatbots),
`edu-qurating` (3 ★), `fabdata-parsedoc` (2 ★). **Es el único actor que esta KB encontró con una línea de trabajo
explícitamente orientada a países de renta baja y media, y está entero por debajo de las 12 estrellas.**

### Lo que esta pasada buscó y no encontró

- **Un análogo de esta capa para materias no ejecutables.** Es el **gap 21**, nuevo: no existe el «notebook de la prosa».
- **Un autograder open source de ensayo con tracción.** Sigue sin existir (mitad no cerrada del gap 6).
- **nbgrader o equivalente en formación profesional.** La capa vive en educación superior STEM. **Gap 10 abierto.**
- **Un repo de esta capa originado en LATAM, EMEA o APAC.** Los cinco son de **North America** (Jupyter/NumFOCUS,
  UC Berkeley). La adopción sí es global y verificada —Edimburgo (EMEA), Aalto (EMEA)—, **pero la autoría no lo es.**
- **Alternativas de ERP/SIS nuevas.** La búsqueda de plataformas devolvió lo que la KB ya tiene (OpenEduCat LGPL-3.0,
  ERPNext, RosarioSIS, openSIS) más **Gibbon**, que es GPL-3.0 y no cambia el cuadro: **la capa administrativa sigue
  siendo copyleft salvo GegoK12**. Sin hallazgo nuevo que reportar acá.

## 2026-10-01 (pase 12) — el repo educativo que más crece no es una plataforma ni un tutor: es un archivo Markdown, y la vertical científica ya ocupó ese canal

Duodécima corrida. El pase 10 cambió el indicador (estrellas → despliegue real) y el 11 cambió el filtro (licencias
permisivas más allá de MIT/Apache/BSD). **Este pase cambia la unidad de análisis: deja de contar repos que se
despliegan y empieza a contar repos que se *cargan*.**

### 🔴 El hallazgo del pase, y es una comparación entre verticales

El estándar **Agent Skills** —bundles de instrucciones que el agente carga on-demand, leídos por Claude Code, Codex,
Cursor, Antigravity, Gemini CLI y Copilot CLI— es hoy el canal de distribución de conocimiento de dominio con la
barrera de entrada más baja que existe: **sin backend, sin despliegue, sin dependencias.** Verificado contra la página
de cada repo el 2026-10-01:

| Repo | Vertical | Licencia | Stars | Velocidad |
|---|---|---|---|---|
| https://github.com/K-Dense-AI/scientific-agent-skills | Ciencia | **MIT** ✅ | **47.200** | Lanzado en octubre de 2025; declara 160.000+ científicos usuarios |
| https://github.com/virgiliojr94/book-to-skill | Genérico | **MIT** ✅ | **33.200** | **+6.300 ★ en 30 días** |
| https://github.com/GarethManning/education-agent-skills | **Educación** | CC BY-SA 4.0 ⚠️ | **815** | 149 commits, mantenimiento activo |
| https://github.com/ZeKaiNie/universal-examprep-skill | **Educación** | **MIT** ✅ | **299** | — |

**La vertical científica construyó acá una biblioteca MIT de 47.200 ★ con 181 skills y 100+ bases de datos. La
educativa tiene 815 ★ con *share-alike*.** Es 58×, y 158× contra el mejor educativo empaquetable.

### Por qué un repo de 33.200 ★ que "sólo convierte PDFs" es el hallazgo estructural

`book-to-skill` convierte PDF/EPUB/DOCX en una skill estructurada —`SKILL.md` con modelos mentales (~4k tokens), un
archivo por capítulo cargado on-demand, glosario, patrones, cheatsheet— y **procesa local, sin subir la fuente**.

Puesto al lado de lo que esta KB ya sabe, cierra un circuito que estaba abierto:

- El **pase 10** encontró la capa de contenido curricular (OER) y su trampa de licencia: los bundles de OpenStax en
  GitHub dicen **CC BY-NC-SA** en los tres títulos revisados.
- El **pase 12** encuentra la máquina que convierte ese contenido en artefacto de agente.
- **Y la trampa del pase 10 se vuelve más cara acá, no menos:** `book-to-skill` es la vía más rápida para convertir un
  libro en skill, y por eso es también la vía más rápida para **empaquetar contenido NonCommercial dentro de un
  entregable de cliente sin que se note**. El output es Markdown: no arrastra el archivo `LICENSE` de la fuente.
  **Regla operativa: la licencia se verifica en la fuente antes de convertir, porque después de convertir no se ve.**

### El segundo hallazgo: la capa MCP de mastery tenía techo de 1 ★ porque se buscó mal

El pase 5 registró cinco servidores MCP de mastery (0–1 ★ cada uno) y concluyó "cinco reinvenciones del mismo patrón".
Correcto y parcial: existe **https://github.com/ankimcp/anki-mcp-server — MIT, 499 ★, 254 commits, v0.22.0**.

Los cinco **inventan** el modelo de dominio (grafo propio, SM-2 propio, esquema propio). Anki **ya está instalado** en
la máquina del alumno y el MCP sólo lo expone. Con `py-fsrs` (MIT, el algoritmo moderno que reemplaza SM-2, ya en la
KB), la recomendación se invierte: **no construir el motor de repaso, conectarse al que el alumno ya usa.** Ver **P28**.

### Nota de método, y corrige cómo se leyeron las cifras en pasadas anteriores

| Repo | Agregador de terceros | Página del repo (mismo día) | Error |
|---|---|---|---|
| `K-Dense-AI/scientific-agent-skills` | 26.500 ★ (ossinsight) | **47.200 ★** | −44% |
| `virgiliojr94/book-to-skill` | 13.700 ★ (sourcepulse) | **33.200 ★** | −59% |

**En una categoría que suma +6.300 ★/mes, el dato del agregador no está viejo: está mal.** Sólo vale la página del repo.

Y el entorno: **`curl` hacia github.com devuelve 403 acá.** Se pasaron las **164 URLs de GitHub de toda esta KB** y
**las 164 dieron 403**, uniformemente — proxy, no *link rot*. **Esas 164 URLs quedan sin revalidar en este pase**: no
hay evidencia de que estén caídas ni de que estén vivas. La verificación de primera mano se hace con **WebFetch**.

## 2026-10-01 (pase 11) — el LMS que faltaba estaba a la vista y lo escondía una línea de licencia: ECL-2.0

Undécima corrida. El pase 10 cambió el indicador —de estrellas a despliegue real— y encontró Sunbird y Ed-Fi.
**Este pase cambia el filtro, no el indicador, y el resultado es peor de admitir:** había infraestructura de primera
línea que esta KB nunca registró **porque su licencia no estaba en la lista de permitidas**, aunque es permisiva.

### 🔴 El hallazgo del pase, y es un error de método de diez pasadas

Esta KB filtra por **MIT / Apache-2.0 / BSD**. La **Apereo Foundation** —la fundación que sostiene la infraestructura
open source de la educación superior en EE. UU. y Europa— no usa ninguna de las tres: usa **ECL-2.0, Educational
Community License 2.0**, que es **Apache-2.0 con el alcance de la concesión de patentes de la sección 3 acotado**,
nacida en el *Licensing and Policy Summit* académico de 2006 y **aprobada por OSI y por la FSF**. No es copyleft: se
puede usar, modificar, cerrar el derivado y redistribuir.

Lo que ese filtro dejaba afuera, verificado el 2026-10-01:

| Repo | Licencia | Stars | Forks | Último push | Qué es |
|---|---|---|---|---|---|
| https://github.com/sakaiproject/sakai | **ECL-2.0** ✅ | **1.234** | 1.014 | **2026-09-30** | LMS de educación superior en Java, con **dos ramas mantenidas a la vez**: tags `25.2` (2026-06-02) y `23.5` (2026-06-30). ⚠️ No publica *GitHub Releases*; la versión se lee en los tags |
| https://github.com/opencast/opencast | **ECL-2.0** ✅ | 505 | 260 | **2026-09-30** | Captura y distribución automatizada de **video de clase** a escala. **La capa multimodal que ningún otro repo de esta KB cubre** |
| https://github.com/uPortal-Project/uPortal | **Apache-2.0** ✅ | 286 | 278 | 2026-09-22 | Portal empresarial de educación superior: la superficie donde la universidad ya le habla al alumno |
| https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW | **ECL-2.0** ✅ | 62 | 25 | 2026-08-04 | *Learning record warehouse* que habla **xAPI, IMS Caliper e IMS OneRoster a la vez** — el único artefacto de esta KB con los tres |

**Sakai es un LMS de 1.234 estrellas con 1.014 forks y push de ayer. No faltaba por no haber buscado: faltaba por una
regla de licencia aplicada sin leerla.** La regla corregida está en `repos/foundations.md`.

### El cementerio: la capa de analítica institucional de Apereo, repo por repo

La organización `Apereo-Learning-Analytics-Initiative` tiene **21 repos** y uno solo está vivo:

| Repo | Stars | Último push | Estado |
|---|---|---|---|
| `OpenLRW` | 62 | **2026-08-04** | ✅ Vivo, *Apereo incubating*, 424 commits |
| `LearningAnalyticsProcessor` | 23 | 2023-01-19 | ⚠️ Dormido — y es el orquestador del pipeline predictivo |
| `Larissa` (LRS alternativo, Apache-2.0) | 8 | 2025-09-18 | ⚠️ Señal de vida, 8 ★ |
| `OpenLRS` | 47 | 2023-01-28 | 🔴 **Archivado. Su descripción es la palabra `Deprecated`** |
| `OpenDashboard-legacy` | 47 | — | 🔴 **`(Deprecated)`** declarado |
| `OpenDashboard-ux` | 1 | **2020-02-29** | 🔴 Creado el 2020-02-12 |
| `OpenDashboard-api` | 0 | **2020-03-09** | 🔴 Creado el 2020-02-12 |
| `LAP-Sakai-Extractor` | 2 | 2016-11-09 | 🔴 El extractor desde Sakai |

**El dato que hay que llevar a una propuesta:** el reemplazo del dashboard se creó en dos repos el mismo día de
febrero de 2020 y se abandonó dentro del mes. Y **Student Success Plan** (SSP), el producto de advising de Apereo con
despliegues reales y soporte comercial de Unicon, **no tiene repositorio localizable en 2026**: el rastro público se
corta cerca de 2014-2015, en SSP 2.4. Ausencia verificada, no omitida.

### La capa predictiva, medida en vez de descrita

| Consulta en GitHub, 2026-10-01 | Resultado | Techo |
|---|---|---|
| `topic:learning-analytics stars:>50` | **2 repos en todo GitHub** | 169 ★, y es un blog de notas de papers |
| `dropout prediction student license:mit pushed:>2026-01-01` | **110 repos** | **6 ★** |

Los tres que importan de esos 110 están en `agents/top.md`. El resumen: el tope es MIT y **entrena con datos
sintéticos**; el más estrellado en absoluto (`dssg/student-early-warning`, 70 ★, del Data Science for Social Good de
la Universidad de Chicago) tiene licencia **"Other" (NOASSERTION)** y último push de **2018**; y la entrega del
**Smart India Hackathon 2026** con el mejor stack del grupo no tiene licencia.

### Lo que da vuelta el gap 11, y es la mejor noticia del pase

El gap 11 dice que los datasets del modelado del alumno son **NonCommercial**. **En esta capa son CC BY 4.0.**

| Dataset | Licencia | Tamaño | Región |
|---|---|---|---|
| **OULAD** (The Open University, UK) | **CC BY 4.0** ✅ | 22 cursos, **32.593 alumnos, 10.655.280 registros de clicks** | EMEA |
| **UCI 697** *Predict Students' Dropout and Academic Success* | CC BY 4.0 ⚠️ confirmar | **4.424 × 36 features**, 3 clases | EMEA (Portugal, grant `POCI-05-5762-FSE-000191`) |

🔴 **Los dos están sin verificar de primera mano:** `analyse.kmi.open.ac.uk` y `archive.ics.uci.edu` están bloqueados
por el proxy de egreso de esta sesión. Tamaños y procedencia salen de fuentes secundarias coincidentes y del
descriptor de datos publicado; **la licencia de UCI hay que confirmarla en la ficha antes de facturar.**

**Y el dato de método que esto obliga a decir en una propuesta:** el número `4.424` que aparece en decenas de esos
110 repos es *el mismo* dataset portugués. **La capa entera está entrenada sobre 4.424 alumnos de una institución
europea de hace una década.** Para cualquier otra región eso es un punto de partida metodológico, no un modelo.

### Dos repos chicos que confirman el patrón de derivación

| Repo | Licencia | Stars | Por qué |
|---|---|---|---|
| https://github.com/terracotta-education/terracotta | **Apache-2.0** ✅ | 21 | RCTs dentro del LMS con consentimiento y anonimización resueltos. 2.572 commits, push del 2026-09-30. **La pieza que convierte "creemos que funcionó" en evidencia** |
| https://github.com/GoogleCloudPlatform/aira | **Apache-2.0** ✅ | 24 | Evaluación automática de **fluidez lectora** (Pre-reader / Reader / Advanced) por Education Engineers de Google Cloud. ⚠️ El repo declara ser *proof-of-concept only*, no producto soportado, **sin datos personales y no para menores de 13** — en una herramienta de alfabetización inicial |

### Nota de método de este pase

- **Canal de verificación:** metadatos (estrellas, licencia SPDX, `archived`, último push, forks) leídos vía la API de búsqueda de GitHub; licencias y README confirmados abriendo la página del repo. `curl` directo a `api.github.com` está restringido al repositorio de la sesión, así que **no se usó**: cada cifra de esta sección viene de una de esas dos vías.
- **Las dos consultas cuantitativas se dejan escritas con su sintaxis exacta** para que la próxima pasada pueda repetirlas y ver la serie, que es lo que un "110 repos, techo 6 ★" vale: nada la primera vez, mucho la tercera.
- **Bloqueado por el proxy en este pase:** `arxiv.org`, `eur-lex.europa.eu`, `digital-strategy.ec.europa.eu`, `archive.ics.uci.edu`, `zenodo.org`, `en.wikipedia.org`. Todo lo que dependa de esas fuentes está marcado 🔴.

## 2026-10-01 (pase 10) — la infraestructura educativa más desplegada del mundo es permisiva, y tiene 41 estrellas

Décima corrida. Las nueve anteriores ordenaron por estrellas. **Este pase cambia el indicador y aparecen dos plataformas
que la KB no tenía**, las dos permisivas, las dos sosteniendo sistemas educativos nacionales enteros.

### El dato que obliga a cambiar el método

| Repo | Licencia | Stars | Forks | Commits | Forks/Stars |
|---|---|---|---|---|---|
| `Sunbird-Ed/SunbirdEd-portal` | **MIT** ✅ | **41** | **317** | **38.046** | **7,7×** |
| `project-sunbird/sunbird-devops` | **MIT** ✅ | 62 | **392** | — | **6,3×** |
| `Sunbird-Ed/SunbirdEd-consumption-ngcomponents` | **MIT** ✅ | 3 | 64 | — | **21×** |
| `project-sunbird/sunbird-telemetry-sdk` | **MIT** ✅ | 4 | 46 | — | **11,5×** |
| `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` | **Apache-2.0** ✅ | 28 | 47 | 1.053 | 1,7× |
| `DSpace/DSpace` | **BSD-3-Clause** ✅ | 1.1k | **1.5k** | **25.385** | 1,4× |
| — comparación — `HKUDS/DeepTutor` | Apache-2.0 | **40,6k** | — | — | ≪1 |

**La regla que deja este pase, y es de método, no de mercado:** en la capa de **infraestructura pública desplegada**, el
fork no es una señal de interés — **es la unidad de adopción**. Cada estado indio forkea Sunbird para levantar su
instancia; cada distrito forkea Ed-Fi. Un proyecto con 38.046 commits y 41 estrellas no es un proyecto muerto: es un
proyecto que **nadie mira y todo el mundo usa**. Nueve pasadas ordenando por estrellas lo iban a seguir enterrando.

### Sunbird / DIKSHA — el hallazgo del pase

**MIT**, EkStep Foundation (India), **Digital Public Good** reconocido por la DPGA. Microservicios: contenido,
autenticación, rutas de aprendizaje, analítica, notificaciones. **64 repos** en `Sunbird-Ed` + **88** en `project-sunbird`.

Sostiene **DIKSHA**, la plataforma escolar oficial de India: **180 M+ alumnos**, **290.000+ contenidos**, **36 idiomas**,
**4.950 M+ sesiones**. ⚠️ Esas cifras son de fuentes secundarias (EkStep, DPI Global); **lo verificado de primera mano es
el repo**: licencia MIT, 41 ★, 317 forks, 38.046 commits en master.

**Por qué cambia una propuesta en APAC, LATAM y África.** Hasta este pase, la respuesta de la KB a «plataforma de
ministerio» era Moodle (GPL-3.0) u Open edX (AGPL-3.0) — las dos copyleft, las dos con el agente obligado a vivir afuera.
**Sunbird es MIT y está diseñado para que un gobierno lo forkee.** Ver **P23**.

### Ed-Fi — el expediente longitudinal que faltaba en la capa del pase 9

`Ed-Fi-ODS` (**Apache-2.0**, 28 ★, 47 forks, 1.053 commits) y `Ed-Fi-Data-Standard` (**Apache-2.0**, 46 ★, 370 commits),
de la **Michael & Susan Dell Foundation**, **relicenciados de propietario a Apache-2.0 en abril de 2020**.

El pase 9 cubrió OneRoster, Caliper, QTI y Open Badges y **dejó afuera el expediente longitudinal del alumno**, que en
EE. UU. es Ed-Fi y está adoptado a nivel estatal. Es anterior a cualquier agente en un proyecto K-12 norteamericano. Ver **P24**.

### La capa de contenido: lo maduro es copyleft otra vez, y van cuatro pases seguidos

| Repo | Licencia | Stars | Commits |
|---|---|---|---|
| `DSpace/DSpace` | **BSD-3-Clause** ✅ | 1.1k | 25.385 |
| `pressbooks/pressbooks` | GPL-3.0+ ⚠️ | 458 | 6.058 |
| `ManifoldScholar/manifold` | GPL-3.0 ⚠️ | 260 | 7.305 |
| `openstax/openstax-cms` | **AGPL-3.0** ⚠️⚠️ | 110 | 2.513 |
| `LibreTexts/Libretext` | GPL-3.0 ⚠️ | 29 | 1.699 |

**Y el hallazgo aprovechable:** el *tooling* de LibreTexts **sí es MIT** — `shapeshift` (0 ★, 339 commits, extracción y
transformación de contenido a formatos de exportación), `conductor` (4 ★, 2.274 commits), `davis` (componentes
*accessibility-first*, que es el puente con la capa del pase 8) y `LibreOne`. **Lo que un engagement necesita de LibreTexts
es el extractor, no la plataforma, y el extractor es permisivo.**

### 🔴 Lo que este pase encontró y no es un repo: una contradicción de licencia entre dos fuentes de primera mano

Los bundles de contenido de OpenStax en GitHub dicen **CC BY-NC-SA** en su archivo `LICENSE` —verificado en
`osbooks-calculus-bundle`, `osbooks-biology-bundle` y `osbooks-college-physics-bundle`, **3 de 3**— mientras
`CAHLR/OATutor` y `pythpythpython/openstax-mcp-server` declaran **CC BY 4.0** en su README. OATutor cura problemas de
**Calculus Volume 1**, uno de los títulos NC-SA.

No se resuelve acá: `openstax.org` está **bloqueado por el proxy** (gap 17). Lo que sí queda es la regla: **la licencia del
contenido se lee en el ítem, no en el badge del repo.** Ver `agents/top.md` y **P22**.

### Nota de método de este pase

`curl -sI` contra `github.com` **sigue devolviendo 403**, y `api.github.com` también **403** — igual que en los pases 5 a 9.
Toda verificación de repos se hizo con WebFetch contra la página del repo, y para contenido **contra el archivo `LICENSE`**,
que es lo que hizo visible la contradicción. **Bloqueados por el proxy en este pase:** `openstax.org`,
`openscied.org` y `support.thenational.academy` — los tres lugares donde vive la licencia declarada *por el editor* del
contenido, que es justamente la otra mitad de la contradicción. Ver el **gap 17**.

---

## 2026-10-01 (pase 9) — los estándares de interoperabilidad siguen obligatorios y su código de referencia se está retirando

Novena corrida. Los pases 4–8 construyeron el stack del alumno capa por capa y el patrón repetido fue *la pieza es
permisiva, el trabajo es integración*. Este pase mira la capa que falta al final —**acreditar** el aprendizaje— y
encuentra el patrón inverso, que es el hallazgo: **la especificación está viva y el código de referencia se está apagando.**

### Lo que no resuelve, verificado URL por URL

| Qué era | URL canónica | Estado 2026-10-01 |
|---|---|---|
| Badgr — implementación de referencia de Open Badges | `concentricsky/badgr-server` | 🔴 **404** + búsqueda de la organización por `badgr` → *«No repositories matched your search»*. La organización verifica hoy **`instructure.com`** |
| caliper-php — cliente PHP oficial de Caliper Analytics | `1EdTech/caliper-php` | 🔴 **404.** Causa nombrada por el fork de la U. de Michigan, textual: *«unarchived following 1EdTech making its caliper-php private»* |
| caliper-python — Sensor API de referencia | `IMSGlobal/caliper-python` | 🔴 **404** |
| European Digital Credentials (Issuer/Viewer/Wallet) | `european-commission-empl/european-digital-credentials` | 🔴 **Archivado 2024-02-02** (EUPL-1.2, 6 ★, 31 commits). Aviso textual: *«For the latest versions go to: https://code.europa.eu/qualifications-courses-and-credentials/»* |
| European Learning Model (modelo de datos) | `european-commission-empl/European-Learning-Model` | 🔴 **Archivado 2024-02-14** (EUPL-1.2, 54 ★, 199 commits) |

Un 404 no distingue borrado de privado de renombrado: lo afirmado es que **las URL no resuelven**, con la señal
independiente en `badgr-server` y la causa nombrada por un tercero en `caliper-php`. Nada más.

### Los repos que sostienen la capa hoy

| Repo | Licencia | Stars | Commits | Por qué está acá |
|------|----------|-------|---------|------------------|
| https://github.com/1EdTech/openbadges-specification | ⚠️ no declarada | **205** | **2.266** | La **especificación** OB 3.0 / 2.1 / 2.0 + **CLR 2.0**. Es el repo con más estrellas de la capa, y **no es código** |
| https://github.com/1EdTech/lti-1-3-php-library | **Apache-2.0** ✅ | 124 | 110 | **LTI 1.3** — la pieza oficial que sigue pública y permisiva |
| https://github.com/digitalcredentials/learner-credential-wallet | **MIT** ✅ | 88 | **1.309** | Billetera del alumno. ⚠️ Último release como DCC at MIT (v2.2.10, jun-2026) → **OpenWallet Foundation Labs** |
| https://github.com/oat-sa/tao-core | **GPL-2.0** ⚠️ | 64 | **22.533** | **TAO** (U. de Luxemburgo + OAT). Por volumen de trabajo, la pieza más madura de toda esta KB |
| https://github.com/KonstantinosPetrakis/esco-skill-extractor | **MIT** ✅ | 32 | 29 | Texto → competencias **ESCO** / ocupaciones **ISCO** |
| https://github.com/amp-up-io/qti3-item-player | **MIT** ✅ | 30 | 596 | **QTI 3** con **certificación de conformidad Basic y Advanced «Delivery» de 1EdTech** |
| https://github.com/digitalcredentials/verifier-plus | **MIT** ✅ | 18 | 395 | Verificación y visualización (incluido QR) |
| https://github.com/digitalcredentials/issuer-coordinator | **MIT** ✅ | 12 | 55 | Emisión + revocación por **W3C VC API**, formato **OB 3.0** |
| https://github.com/tl-its-umich-edu/caliper-php-public | **LGPL-3.0** ⚠️ | 3 | 365 | Fork de la **U. de Michigan**; hoy es el cliente PHP de Caliper accesible |
| https://github.com/luisgf/openbadgeslib | **LGPLv3** / BSD-2-Clause ⚠️ | **1** | **404** | Emisor OB 3.0 completo: JWT-VC, `did:web`, **Bitstring Status Lists**. v4.0.0 (2026-07-22) |

### La distribución de estrellas de esta capa dice algo que conviene leer

El repo más estrellado es **una especificación** (205 ★) y no código. El de más commits es **copyleft GPL-2.0** (22.533).
El emisor OB 3.0 más completo tiene **404 commits y 1 estrella**. Y la pieza con **certificación de conformidad de 1EdTech**
tiene **30 estrellas**.

**Cómo leerlo para una propuesta:** esta capa **no se elige por popularidad** — la señal de calidad acá no son las
estrellas, es la **certificación de conformidad** y el **conteo de commits**. Es la primera capa de esta KB donde eso pasa,
y es coherente con que su consumidor sea institucional y no un desarrollador que la descubre en GitHub Trending.

### Por qué esto cambia una propuesta, y no es un detalle de ingeniería

La obligación de interoperar no se fue con el código. Un cliente que compra «credenciales digitales» o «analítica
conforme» sigue necesitando OB 3.0, Caliper, QTI y OneRoster. Lo que cambió es **de dónde sale la implementación**: de
terceros certificados, consorcios universitarios y forks de universidad. Eso convierte en entregable vendible algo que
antes era obvio y gratis: **saber cuál de estas piezas sigue viva, con qué licencia y con qué certificación.** Ver **P21**.

### Nota de método de este pase

`curl -sI` contra `github.com` **sigue devolviendo 403** a través del proxy de egreso, y `api.github.com` también **403**
—igual que en los pases 5 a 8—, así que toda verificación se hizo con **WebFetch contra la página del repo**, y en dos
casos contra el archivo (`LICENSE` de `qti3-item-player`, `README.md` del fork de Michigan). Se marcaron como no
verificadas las afirmaciones que dependen de dominios bloqueados: **`code.europa.eu`** (donde vive hoy el stack europeo
de credenciales), **`moodle.org`**, y los tres sitios de prensa con el detalle de precios de Instructure
(`constellationr.com`, `nasdaq.com`, `aijourn.com`). Ver `intel/trends.md`, gap 14 y la nota de método del pase 9.

## 2026-10-01 (pase 8) — la capa de conformidad de accesibilidad: más tracción que la de evaluación pedagógica, licencia limpia, y no es educativa

Octava corrida. Los pases 4–7 construyeron el stack de medición —modelado (`pyKT`, `pyBKT`), evaluación (`EduBench`, `MathTutorBench`), telemetría (`lrsql`, `Ralph`) y datos de entrenamiento— y el patrón repetido fue: *la pieza es permisiva, el trabajo es integración*. El pase 7 encontró el agujero (los datasets son NonCommercial).

Este pase encuentra algo distinto: **una capa entera, con obligación legal ya vencida y presupuesto de cliente ya asignado, cuya mejor herramienta tiene más estrellas que casi todo lo que la KB registra — y que no aparece en ninguna búsqueda educativa porque no es un repo educativo.**

### Capa de accesibilidad y tecnología asistiva

| Repo | Licencia | Stars | Commits | Rol |
|---|---|---|---|---|
| https://github.com/Community-Access/accessibility-agents | **MIT** ✅ | **419** | **374** | **El default de conformidad.** Revisión **WCAG 2.2 AA** desde adentro de Claude Code / Copilot / Claude Desktop / Codex / Gemini CLI. Cubre código, documentos (**PDF y ePub**, donde vive el material didáctico), markdown y add-ons de NVDA |
| https://github.com/sololabstr/uisight | **MIT** ✅ | 128 | n/d | Medición de contraste, área táctil y *theme drift*, con **servidor MCP** |
| https://github.com/weAAAre/a11y-agents-kit | **MIT** ✅ | 34 | n/d | Kit de skills de accesibilidad para harnesses de AI, de **weAAAre** |
| https://github.com/OptiKey/OptiKey | **GPL-3.0** ⚠️ | **4.4k** | n/d | Control de computadora con la mirada (ELA / motoneurona) |
| https://github.com/cboard-org/cboard | **GPL-3.0** ⚠️ | 759 | 5.531 | AAC con texto-a-voz (PWA). © Assistive Technology LLC; respaldo de UNICEF |

**La asimetría que define cómo se cotiza esta capa: el producto asistivo maduro es copyleft y el tooling de conformidad es permisivo.** Lo que se puede empaquetar es la **verificación**, no el **dispositivo**.

### Por qué la pieza MIT es la vendible y no los tutores

| | Capa de tutoría | Capa de evaluación pedagógica | **Conformidad de accesibilidad** |
|---|---|---|---|
| Incumbente open source | DeepTutor 40.6k ★, OpenMAIC 39.7k ★ | academia (EMNLP, NAACL) | **ninguno** |
| Obligación legal | no | parcial (AI Act escalonado) | **sí, y venció el 2025-06-28** |
| Presupuesto del cliente | innovación | hay que crearlo | **ya existe** (cumplimiento / compras) |
| Licencia de la pieza clave | Apache-2.0 / MIT | MIT, **datasets NonCommercial** | **MIT, sin dataset de por medio** |

Es el único renglón de esta KB donde las cuatro filas salen a favor. Ver **P17**.

### Capa de integridad académica — registrada como roadmap, no como componente

**Open edX Proctoring Toolset** — propuesta con release objetivo **Verawood**, por Elizabeth Gordon, Ali Hugo y Arunmozhi Periasamy (**Arizona State University** + **OpenCraft**). Proctoring nativo con APIs estándar del navegador, verificación de identidad, revisión asistida por AI e integración opcional con **Safe Exam Browser**.

**El argumento que importa:** la propuesta declara que la ausencia de proctoring integrado y gratuito **afecta desproporcionadamente a instituciones del Sur Global y de bajo presupuesto**, hoy obligadas a Respondus, Wheebox o ProctorU. 🔴 **Es una propuesta, no código desplegable** — no cotizarla; sí sirve para recomendarle a un cliente sobre Open edX que **no firme tres años de proctoring propietario ahora**.

⚠️ **Lo que hay fuera de Open edX no es proponible:** la búsqueda de proctoring open source devuelve mayoritariamente trabajos finales con YOLO y seguimiento de mirada, sin licencia clara, sin mantenimiento y **sin evaluación de sesgo** — y vigilancia biométrica sobre alumnos es exactamente el alto riesgo del Annex III del EU AI Act.

⚠️ **Verificación:** los cinco repos de la tabla se abrieron vía WebFetch (licencia, stars y commits leídos en la página). **`uisight` y `a11y-agents-kit` resultaron MIT**, así que la capa de conformidad es permisiva de punta a punta. La API de GitHub sigue bloqueada en esta sesión, así que no hay fechas de último commit.

---

## 2026-10-01 (pase 7) — la capa que hace falta para que las librerías MIT sirvan: los datos, y casi todos son NonCommercial

Séptima corrida. El pase 4 encontró la capa de modelado (`pyKT`, MIT), el pase 5 le sumó la alternativa occidental (`pyBKT`, MIT) y el pase 6 agregó la capa de telemetría (xAPI/LRS). Las tres conclusiones fueron la misma: **la pieza es MIT, el trabajo es integración, no investigación.**

Este pase encuentra el agujero en ese razonamiento. Un modelo de knowledge tracing **no es software que se instala, es software que se entrena**. La KB nunca registró con qué. Y cuando se mira, la licencia se da vuelta: **la capa de modelado es permisiva y la capa de datos no lo es.**

### Los datasets de knowledge tracing, con su licencia

| Dataset | Licencia | Volumen | Contenido | Origen |
|---|---|---|---|---|
| **EdNet** — https://github.com/riiid/ednet | ⚠️ **CC BY-NC 4.0** | **131.441.538** interacciones, **784.309** alumnos (441,2 por alumno), 13.169 problemas, 1.021 clases, 293 tipos de skill | Cuatro niveles jerárquicos: **KT1** (pregunta-respuesta), **KT2** (acciones: entrar, responder, enviar), **KT3** (+ actividades de aprendizaje y explicaciones), **KT4** (lista completa, incl. multimedia y eventos de pago). Recolectado durante 2 años desde abril de 2017 | **APAC (Corea del Sur)** — Riiid, desde su app **Santa**, 780k+ usuarios reales |
| **XES3G5M** — https://github.com/ai4ed/XES3G5M | **MIT** ✅ | **5.549.635** interacciones, **18.066** alumnos, **7.652** preguntas de matemática, **865** conceptos de conocimiento | El más rico en información auxiliar: **texto de las preguntas**, relaciones entre componentes de conocimiento, tipos de pregunta y análisis de respuestas, con los KC en rutas jerárquicas. ⚠️ **Sólo en chino** y sólo matemática de tercer grado | APAC (org `ai4ed`, 61 ★ — la página del repo **no declara institución ni país**) |
| **FoundationalASSIST** — arXiv 2602.00070 | ⚠️ **CC BY-NC 4.0** + **acceso condicionado** | **1,7M** interacciones, **5.000** alumnos | **El único en inglés que combina texto de la pregunta + la respuesta real del alumno + qué distractor eligió**, con alineación a **Common Core**. Currículo *Illustrative Mathematics*, 6.º a 8.º grado. Define dos familias de tarea: **Knowledge Tracing** y **Pedagogical Grounding** (si el LLM entiende qué hace efectivo a un ítem de evaluación) | **North America** — Eamon Worden, Cristina Heffernan, Neil Heffernan (el linaje **ASSISTments**) y Shashank Sonkar |
| Junyi Academy | no verificada en este pase | ~16M interacciones | Tupla identificador + correcto/incorrecto | APAC (Taiwán) |
| Eedi | no verificada en este pase | ~20M interacciones | Texto parcial de preguntas en inglés, **sin las respuestas reales** | EMEA (Reino Unido) |

### Por qué esto cambia una propuesta, y no es un detalle legal

Las seis pasadas anteriores dejaron escrito, con razón, que `pyKT` y `pyBKT` son **MIT** y que por lo tanto el modelado de alumno es "integración de una librería madura". **Eso sigue siendo cierto sobre el código y es insuficiente**, porque un modelo DLKT sin datos de entrenamiento no predice nada, y de los tres datasets grandes:

- **EdNet** (el más grande por dos órdenes de magnitud) es **NonCommercial**.
- **FoundationalASSIST** (el único en inglés con respuestas reales y distractores) es **NonCommercial** *y además* **gated**: hay que aceptar unas *Responsible Use Guidelines* y **entregar datos de contacto** para descargar.
- **XES3G5M** es **MIT**, y es el único que se puede usar en un entregable comercial. Es también **chino, de matemática y de tercer grado**.

**Las tres rutas reales para un engagement, dichas en orden de preferencia:**

1. **Entrenar con los datos del cliente.** Es la única ruta limpia a escala, y tiene un costo que hay que presupuestar explícitamente: **arranque en frío**. No hay histórico, así que el modelo no sirve el primer día — y acá es donde la capa del pase 6 deja de ser opcional. Un LRS xAPI desplegado desde el día uno (`lrsql` o `Ralph`) **es el que genera el dataset propio**. Sin eso, el cold start no termina nunca.
2. **`XES3G5M` (MIT) para validar la arquitectura**, no para servir al cliente: sirve para probar que el pipeline entrena, mide y responde. Que sea chino y de matemática de tercer grado no importa para eso; importa muchísimo si alguien lo confunde con el modelo de producción.
3. **`EdNet` o `FoundationalASSIST` sólo para investigación interna o un paper**, nunca dentro de un entregable facturado. `NC` significa NonCommercial y un engagement de Globant es, por definición, comercial.

**La frase que hay que poder decir en una propuesta:** *"el modelo de mastery se entrena con los datos del cliente, y por eso el Learning Record Store va en la fase 1 y no en la 3"*. Sin la capa de datos, el LRS parecía una pieza de conformidad; con ella, es la pieza que hace posible el producto. Ver **P16**.

### Y el gap 4 se extiende a una quinta capa

El gap 4 (concentración de la oferta en instituciones chinas) venía creciendo capa por capa: agente (DeepTutor, OpenMAIC), modelado (`pyKT`), modelo fundacional (`OmniEdu`), evaluación (`EduBench`). Este pase agrega la quinta, y con un giro desfavorable:

**el único dataset de knowledge tracing con licencia permisiva es chino.** Los dos de procedencia no china que importan —EdNet (Corea) y FoundationalASSIST (EE. UU.)— son los dos NonCommercial.

La ruta alternativa que el pase 5 había armado para un cliente con restricción de procedencia (`pyBKT` + `Aila` + `MathTutorBench` + `SafeTutors`, todo occidental y permisivo) **se sostiene en código y se rompe en datos**. Para ese cliente la ruta 1 —entrenar con datos propios— deja de ser la opción preferible y pasa a ser la única.

### ProHist-Bench — ciencias sociales sigue siendo un gap, y ahora se sabe por qué no se cierra solo

Buscando el benchmark pedagógico de ciencias sociales que el pase 6 dejó pendiente, lo que aparece es **ABench** (https://github.com/inclusionAI/ABench, **Apache-2.0** ✅, 30 ★): suite multi-dominio con seis datasets —Física (500 problemas), Actuaría, Lógica, Psicología, Derecho y **ProHist-Bench**.

**ProHist-Bench**: **400 preguntas núcleo** en 4 tipos de tarea, **10.891 rúbricas redactadas por historiadores** sobre **9 dimensiones de capacidad**; versión extendida de 504 preguntas. Construido sobre materiales del **examen imperial chino**. Paper: arXiv 2604.24690.

**El sub-gap NO se cierra, y la distinción es la parte útil:** ProHist-Bench mide si el modelo **sabe hacer investigación histórica** — no si **sabe enseñar historia**. Es la diferencia que el gap 1 viene sosteniendo desde el pase 4 entre un benchmark de dominio y un benchmark pedagógico: `MathTutorBench` no mide si el modelo resuelve la ecuación, mide si andamía al alumno que no la resuelve. ProHist-Bench es del primer tipo.

**Qué se puede hacer igual con él, que no es poco:** 10.891 rúbricas de expertos sobre 9 dimensiones es la pieza más cara de construir en cualquier evaluación, y es **Apache-2.0**. Para un engagement de humanidades sirve como **capa de exactitud factual** debajo de una capa pedagógica que hay que aportar (`UnifyingAITutorEvaluation` para la taxonomía, `SafeTutors` para el daño). Lo que no se puede es presentarlo como evaluación de enseñanza.

⚠️ **Procedencia, y pega otra vez en el gap 4:** `inclusionAI` es **la organización open source de Ant Group** — verificado en el perfil, que declara `inclusion-ai.org` y 68 repos. **APAC/China.** La única pieza de evaluación en humanidades con licencia limpia que encontró esta KB es, también, china.

### Un repo chico que confirma el patrón de derivación

https://github.com/dhakalaashish/knowledge_tracing_foundationalASSIST — **CC-BY-NC-4.0** ⚠️, **0 ★** (verificado de primera mano en este pase). Integra una dimensión cognitiva a knowledge tracing y diagnóstico cognitivo **sobre el código base de FoundationalASSIST**, con carpetas de código, datos y resultados precomputados.

**Vale anotarlo por su licencia, no por su tamaño, y es la mejor prueba disponible de que el problema del `NC` no es teórico: el derivado heredó el `NC`.** Nadie lo eligió — se hereda. Un derivado académico así está perfectamente bien; **el mismo derivado dentro de un entregable facturado, no**, y la cadena de herencia es exactamente por donde entraría sin que nadie lo note.

De paso confirma de primera mano las cifras de `FoundationalASSIST` que el resto de este pase tomó de resultados de búsqueda: **1,7M interacciones**, **5.000 alumnos** con 211–421 problemas cada uno, y **224 skills** de matemática distintos, sobre currículo *Illustrative Mathematics* de 6.º a 8.º grado, provenientes de **ASSISTments**.

### Nota de método de este pase

- **`curl -sI` contra github.com sigue devolviendo 403 a través del proxy**, como en los pases 4–6. Toda verificación de repo se hizo con WebFetch contra la página del repo. La verificación de licencia de `llamatutor` se hizo pidiendo `/blob/main/LICENSE` directamente: **404**, que es la confirmación positiva de que no hay archivo de licencia.
- **`arxiv.org`, `huggingface.co` y los dominios de OUP siguen bloqueados** (se reintentaron los tres en este pase). Por eso `FoundationalASSIST`, `EduZone`, `AIriskEval-edu`, `ProHist-Bench` (el paper) y `L2-Bench` quedan con cifras de **resultados de búsqueda, no de fuente primaria**. Lo alojado en github.com —ABench, XES3G5M, EdNet, Honcho, tutor-gpt, ChatTutor— **sí está verificado de primera mano**.
- **La API de GitHub vía MCP sirve para buscar y no para leer archivos de terceros**: está restringida a los repos de la sesión, así que `get_file_contents` sobre `Nutlope/llamatutor` fue denegado. Es la razón por la que la verificación de licencias siguió haciéndose con WebFetch.
- **Límite de la búsqueda de GitHub que conviene dejar escrito:** `in:name` **no respeta límites de palabra**. Buscar `tutor in:name` devuelve 276 resultados dominados por `tutorial`, y un `OR` entre términos degrada la consulta entera. Para encontrar los tres tutores de este pase sirvió buscar por **descripción**, no por nombre.

## 2026-10-01 (pase 6) — la capa de datos de aprendizaje, que estaba en un estándar IEEE y no en la KB

Sexta corrida del día. El hallazgo de repos de este pase no es un proyecto nuevo y llamativo: es **una capa entera de infraestructura madura que las cinco pasadas anteriores no registraron**, porque se buscaba por "agente", "tutor" y "benchmark", y esta capa no se llama así. Se llama **Learning Record Store**.

### Por qué no había aparecido antes

Las pasadas 1–5 construyeron el stack de arriba hacia abajo: plataforma (Moodle, Open edX) → agente (DeepTutor, OpenMAIC) → modelado (pyKT, pyBKT) → medición (MathTutorBench, EduBench) → modelo fundacional (OmniEdu). Nunca se preguntó **dónde se escriben los eventos** que alimentan el modelado. La respuesta lleva quince años estandarizada: **xAPI**, hoy **IEEE 9274.1.1**.

Es la misma lección de método del pase 3 con GegoK12, en otra forma: buscar la categoría que uno tiene en la cabeza devuelve lo que uno ya sabe. **Acá el error no fue la consulta sino el mapa** — faltaba una capa en el modelo mental del stack, así que nunca se buscó.

### Los cuatro LRS verificados

Todos verificados de primera mano en GitHub en este pase (licencia, stars y commits leídos del repo):

| Repo | Licencia | Stars | Commits | Lenguaje | Mantenedor | Por qué importa |
|---|---|---|---|---|---|---|
| https://github.com/LearningLocker/learninglocker | **GPL-3.0** ⚠️ | 583 | 3.254 | JavaScript | Learning Pool | El canónico de la categoría, desde 2014. El más adoptado — y copyleft, así que el servicio que lo toque hereda la obligación |
| https://github.com/adlnet/ADL_LRS | **Apache-2.0** ✅ | 331 | 1.885 | Python | **ADL** (EE. UU.), autor del estándar | Implementación **de referencia**, con soporte IEEE 9274.1.1 / xAPI 2.0. ⚠️ El repo declara ser *proof of concept* para pocos usuarios |
| https://github.com/yetanalytics/lrsql | **Apache-2.0** ✅ | 143 | 2.268 | Clojure | Yet Analytics | **El candidato de producción permisivo.** Corre sobre SQLite, PostgreSQL 14–18, MariaDB y MySQL 8–9.5. Copyright © 2021–2026: mantenimiento vivo |
| https://github.com/openfun/ralph | **MIT** ✅ | 50 | 714 | Python | **OpenFun** (France Université Numérique) | El único MIT, y el que **convierte tracking logs de Open edX a xAPI** de fábrica. Mismo origen que Richie, que esta KB ya listaba |

**Tres de los cuatro son permisivos.** Después de cinco pasadas peleando con AGPL en plataformas y CC BY-SA en benchmarks, esta capa se puede adoptar sin pasar por legal — con la salvedad de que el más adoptado (Learning Locker) es justamente el copyleft.

### El dato de arquitectura que cambia una propuesta

`Ralph` viene de **OpenFun**, la misma organización francesa que publica `Richie` (MIT), ya listada en `verticals/solutions.md`. Para un engagement EMEA sobre Open edX eso significa que **la capa pública (Richie), la plataforma (Open edX) y la telemetría (Ralph) tienen integración probada entre sí**, y dos de las tres son MIT. Es la primera vez que esta KB puede ofrecer una cadena vertical coherente y de un mismo origen regional.

### Un repo más, chico, que cierra el circuito

https://github.com/DavidLMS/learnmcp-xapi — **MIT**, **15 ★**, 32 commits, Python. Servidor MCP que expone un LRS a un agente (registrar statement / consultar progreso / gestionar vocabulario), con backends para `lrsql` y `Ralph`, los dos permisivos de la tabla de arriba. Autor: docente del **IES Rafael Alberti** (España). Detalle completo en `agents/trending.md` de este mismo pase.

Es chico y hay que decirlo: **15 estrellas y 32 commits no es una dependencia de producción**. Pero a diferencia de los cinco servidores MCP de mastery del pase 5 —que sumaban 3 estrellas y 23 commits **entre los tres más grandes** e implementaban cada uno su propia heurística— este no reinventa el almacén: se apoya en el estándar. Como referencia de integración vale; como base a forkear, también, porque es MIT y son 32 commits que se leen en una tarde.

### Lo que se buscó y no apareció en este pase

- **`pyKT` o `pyBKT` expuestos detrás de MCP o de un LRS**: siguen sin existir. El gap 5 se mantiene abierto, pero más chico (ver `intel/trends.md`).
- **Un LRS con estimación de mastery incorporada**: ninguno de los cuatro la tiene. Son almacenes conformes al estándar, no motores de inferencia. La separación es correcta desde el diseño, pero significa que el estimador **siempre** es trabajo propio.
- **Repos de FP (formación profesional) con tracción**: 24 repos en total, techo de 2 ★. Detalle en `agents/trending.md`.
- **Repos educativos LATAM con tracción**: se volvió a medir, en español. 20 repos, **ninguno pasa de 1 estrella**. Detalle en `intel/trends.md`, gap 2.

## 2026-09-30 (pase 5) — un modelo fundacional educativo abierto, y la capa de grading deja de ser un hueco vacío

Quinta corrida del día. Dos hallazgos de repo que no son incrementales: **aparece una familia de modelos fundacionales open para K-12** (capa que la KB no tenía en absoluto: tenía plataformas, agentes, modelado y medición, pero ningún modelo entrenado para educación), y **la capa de grading deja de ser un gap puramente vacío** — aunque lo que aparece obliga a leer licencias con más cuidado que en cualquier pasada anterior.

### OmniEdu — modelos fundacionales abiertos para K-12, y sin licencia declarada

| Repo | Licencia | Stars | Commits | Qué es |
|---|---|---|---|---|
| https://github.com/haolpku/Omni-Edu | ⚠️ **sin licencia declarada** | 48 | 2 | Familia de modelos fundacionales para enseñanza y aprendizaje K-12. **Tres checkpoints: 4B, 9B y 27B** |

Lo verificado de primera mano en el repo:

- Los checkpoints se construyen sobre **Qwen3.5-4B-Base, Qwen3.5-9B-Base y Qwen3.8-27B**, y los pesos están alojados en HuggingFace bajo `lhpku20010120/`.
- La mezcla de instrucciones es **pública**: 69.999 ejemplos y 15,96M tokens de respuesta supervisada, de 100+ fuentes (60.951 específicos de educación + 9.048 de propósito general).
- La supervisión se organiza en cuatro capacidades: competencia en la materia, anclaje curricular, razonamiento diagnóstico y acción pedagógica/andamiaje.
- Origen: **Universidad de Pekín, University of the Chinese Academy of Sciences y Zhongguancun Academy** (Hao Liang, Qihan Lin et al.).

Dato de conexión con la KB: según el paper, **OmniEdu-27B alcanza 78,74% en el setting Scaffold de MathTutorBench** — el benchmark que el pase 4 agregó a `repos/foundations.md`. Es la primera vez que un artefacto de esta KB se evalúa contra otro artefacto de esta KB.

⚠️ **Dos problemas de licencia, no uno, y los dos son bloqueantes hasta que se resuelvan:**

1. **El repo no declara licencia.** Sin archivo LICENSE, el default legal es "todos los derechos reservados", por mucho que el título diga *Open Foundation Models*. "Abierto" acá significa *los pesos se pueden descargar*, no *se pueden usar comercialmente*.
2. **Los pesos heredan la licencia del modelo base.** Están construidos sobre bases Qwen, cuyas licencias no son uniformes entre tamaños y no son todas Apache-2.0. Aun si el repo declarara MIT mañana, eso no levantaría la restricción del base model.

**Cómo tratarlo en una propuesta:** como la mejor evidencia disponible de que **un modelo chico y especializado puede competir con uno grande y genérico en tareas pedagógicas** —que es un argumento de costo muy fuerte para un ministerio o un distrito— y **no** como un componente desplegable. Si el cliente necesita un modelo educativo propio, esto es la receta a replicar (el corpus y las cuatro capacidades están descritos), no el artefacto a instalar. Refuerza además el **gap 4**: la concentración APAC ya no es sólo de agentes y de modelado, ahora también de modelos fundacionales.

### La capa de grading: tres repos nuevos y ninguno limpio

El gap 6 (y su actualización, el gap 9) viene diciendo desde el pase 2 que **no hay grading open source con tracción** y que la recomendación operativa es *orquestar Gradescope, no reemplazarlo*. Esta pasada buscó por licencia y stack en vez de por categoría. Lo que apareció **no cierra el gap, pero lo vuelve mucho más preciso**:

| Repo | Licencia | Stars | Commits | Estado real |
|---|---|---|---|---|
| https://github.com/paper-instruments/rubric | **MIT** ✅ | **75** | 64 | Librería de evaluación con **rúbricas ponderadas**: scoring criterio por criterio, single-pass y juicio holístico, validación con Pydantic, cualquier proveedor LLM. **No es educativa** — es genérica de LLM-as-judge. Es la pieza permisiva más útil de la tabla |
| https://github.com/sdrangan/llmgrader | ⚠️ **PySilicon Research License** (custom, no OSI) | 2 | **240** | Autograder para cursos de ingeniería: derivaciones multi-paso, trade-offs de diseño, justificación abierta. Problemas y rúbricas como **XML estructurado**, trazas de corrección transparentes, **servidor MCP** para autoría asistida e **integración con Gradescope**. De Sundeep Rangan (NYU), **desplegado en un curso de maestría real** |
| https://github.com/Dmoayad/essay-grader-llm | GPL-3.0 ⚠️ | 1 | 12 | Corrección de ensayos con rúbrica + RAG comparando contra material de referencia, FastAPI/Gradio/LangChain. Incluye detección de plagio |

**El hallazgo incómodo es `llmgrader`.** Es, de largo, el grading agéntico más maduro que esta KB encontró en cinco pasadas: 240 commits, en producción en un curso de NYU, con MCP y con la integración a Gradescope que el gap 6 recomienda construir. Y su licencia es una **"PySilicon Research License" propia, © 2026 Sundeep Rangan** — verificado leyendo el archivo LICENSE. **No es OSI, no es MIT/Apache/BSD, y no se puede usar en un entregable de cliente.**

Que el proyecto más avanzado de la categoría tenga licencia de investigación custom **explica por qué el gap 6 se sostuvo cuatro pasadas**: no es que nadie construyera grading agéntico, es que quien lo construyó bien no lo liberó de forma reutilizable. Es una corrección de diagnóstico que vale tanto como un repo nuevo.

**La recomendación operativa cambia poco pero se vuelve más concreta:** seguir orquestando Gradescope (vía `gradescope-mcp`, MIT, 8 ★), y cuando haya que construir la capa de juicio, **construirla sobre `paper-instruments/rubric` (MIT, 75 ★)** en vez de desde cero. Es genérica, así que la pedagogía hay que aportarla — y para eso ahora están EduBench y SafeTutors (ver `agents/trending.md`, pase 5).

### Contexto: la infraestructura de autograding clásica ya existe y no es AI

Verificado en esta pasada porque conviene no confundir capas en una propuesta:

| Repo | Licencia | Stars | Commits | Qué es |
|---|---|---|---|---|
| https://github.com/eecs-autograder/autograder.io | ⚠️ no declarada en este repo (es el repo de documentación e issues) | **79** | 61 | Sistema de autograding **basado en casos de test, no en LLM**. Sandboxing con Docker, feedback configurable, entregas en grupo, hand-grading. Mantenido por el departamento de CS de la **Universidad de Michigan**, que lo usa para **~5.000 alumnos por semestre en una docena de cursos** |

No es un competidor de Gradescope con AI: es la plomería determinista sobre la que una capa AI podría montarse. Es relevante porque tiene **volumen real verificable** —el dato de 5.000 alumnos/semestre es el único número de escala de producción de toda la capa de grading de esta KB— y porque para código, el autograding determinista sigue siendo mejor que un LLM. El ángulo AI correcto acá es **feedback y explicación sobre tests que ya pasaron o fallaron**, no reemplazar los tests.

### Nota de método

- **`curl -sI` contra github.com devuelve 403** a través del proxy de egreso (confirmado otra vez en este pase, ya lo había anotado el pase 4). Verificación por WebFetch contra la página del repo.
- **Dominios bloqueados por el proxy en esta corrida:** `arxiv.org`, `openreview.net`, `aclanthology.org`, `huggingface.co`, `ojs.aaai.org`, `mcml.ai`, `unu.edu`, `coe.int`, `digitaleducationcouncil.com`, `mcpservers.org`. Todo lo de esta sección que sale de github.com está verificado; los números de papers y los pesos en HuggingFace no pudieron abrirse en la fuente primaria.
- **Licencias leídas en el archivo, no inferidas del badge**, en los dos casos donde importaba: `llmgrader` (PySilicon Research License) y `awesome-ai-llm4education` (404, no existe LICENSE). En los dos, el badge o la apariencia del repo sugería algo distinto de lo que dice el archivo. **Leer el LICENSE sigue siendo la única verificación válida.**

## 2026-09-30 (pase 4) — aparece la capa de medición, y tenía cuatro años de antigüedad

Cuarta corrida del día. El hallazgo principal de esta ventana **no es un repo nuevo**: es un repo maduro que la KB nunca había mirado porque buscaba en la categoría equivocada.

### pyKT — 441 ★, MIT, y el gap 5 lo estaba pidiendo desde el pase 1

https://github.com/pykt-team/pykt-toolkit · **MIT** · **441 ★** · Python · 811 commits

El gap 5 de `intel/trends.md` viene diciendo desde la primera pasada: *"No hay integración madura entre knowledge tracing y agentes LLM. `py-fsrs` y OATutor resuelven retención y mastery; los agentes grandes resuelven conversación. Nadie los cosió bien."*

La segunda mitad sigue siendo cierta — **nadie los cosió**. La primera mitad estaba mal planteada: la KB tenía como única pieza de mastery a **OATutor** (265 ★, un ITS completo con BKT adentro) y a **py-fsrs** (499 ★, scheduling). Faltaba la librería de *knowledge tracing* propiamente dicha, y existe desde 2022:

- **10+ modelos DLKT** comparables entre sí (DKT, SAKT, AKT, simpleKT y demás), no un solo algoritmo embebido en un producto.
- **7+ datasets** con preprocesamiento estandarizado y **5 escenarios de predicción** — o sea, resultados reproducibles, que es lo que hace falta para defender una afirmación de eficacia ante un cliente.
- Publicado en **NeurIPS 2022** (Liu, Liu, Chen, Huang, Tang, Luo) y mantenido: 811 commits.
- **MIT**, sin fricción de licencia.

**Origen: Jinan University, Guangdong Institute of Smart Education (China) → APAC.** Zitao Liu es Profesor y Decano de ese instituto; el trabajo tuvo apoyo del Key Laboratory of Smart Education of Guangdong. Refuerza el gap 4 (concentración APAC de la oferta), ahora también en la capa de modelado y no sólo en tutores.

**Por qué importa más que sus 441 estrellas.** Es la diferencia entre un tutor que *parece* adaptativo y uno que puede demostrar que lo es. Bajo EU AI Act, un sistema de educación en Anexo III tiene que documentar cómo decide; "el LLM decidió" no es documentación, y una curva de mastery de un modelo DLKT publicado sí lo es. Ver el nuevo patrón **P10**.

### Los dos benchmarks pedagógicos que faltaban

| Repo | URL | Licencia | Stars | Venue |
|------|-----|----------|-------|-------|
| **MathTutorBench** | https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | 42 | EMNLP 2025 (Oral) |
| **UnifyingAITutorEvaluation** | https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | 32 | NAACL 2025 (Senior Area Chair Award) |

El segundo es **del mismo autor que `AITutor-EvalKit`**, el repo de 3 ★ que la KB venía citando como "el único evaluador pedagógico que existe". Era el repo chico del mismo trabajo. Corregido en `agents/top.md`.

### Lo demás de la ventana

- **FreeLingo** (https://github.com/artcc/freelingo, **AGPL-3.0**, 150 ★): Duolingo self-hosted con Ollama, CEFR, voz y repetición espaciada. Stack moderno (FastAPI + Next.js + Postgres + Redis en Docker Compose). **AGPL**, así que sirve como referencia de arquitectura, no como base de producto cerrado.
- **mentar** (https://github.com/avps82/mentar, AGPL-3.0, 1 ★, último commit 2026-08-26): 934 nodos de concepto en 157 plantillas curriculares (Australia ACARA v9, India, Singapur, EE. UU.). Idea de diseño que vale robar aunque el repo no se use: **el LLM sólo explica y un checker determinístico corrige**, de modo que el modelo no puede validar una respuesta incorrecta. Es la respuesta más simple que vimos al riesgo de alucinación en corrección.
- **TutorIA** (https://github.com/LabSirius/TutorIA, MIT, 0 ★) y **OpenDidactia** (https://github.com/nmarafo/OpenDidactia, CC BY-SA 4.0, 0 ★): cubiertos en `agents/trending.md` — mueven los gaps 2 (LATAM) y 3 (EMEA).
- **Sin movimiento en los grandes:** DeepTutor sigue en 40.6k ★ y OpenMAIC en 39.7k ★, idénticos al pase 3 de hoy. Se registra el dato plano para no dejar hueco en la serie.

### Nota de método — `curl -sI` no sirve para verificar en este entorno

El procedimiento estándar de esta KB es verificar cada URL con `curl -sI` antes de escribirla. **En esta corrida devuelve `403` para *todas* las URLs de github.com**, incluidas las de repos que sabemos vivos (DeepTutor, OpenMAIC, el propio `gegok12` verificado en el pase 3). O sea: el proxy de salida bloquea el `HEAD`, y un 403 uniforme **no distingue un repo real de uno inexistente** — usarlo como verificación daría falsos negativos en todo.

La verificación de este pase se hizo con **WebFetch contra la página del repo**, y se comprobó que el canal sí discrimina: una URL deliberadamente inexistente devolvió `HTTP 404 Not Found`, mientras que las 13 URLs reales devolvieron la página. **`api.github.com` también está fuera de alcance** (responde que el repo no está habilitado para la sesión), así que stars y licencia se leen de la página renderizada, no de la API.

---

## 2026-09-30 (pase 3) — un gap declarado se cae: aparece un SIS permisivo y vivo

Tercera corrida del día. El hallazgo principal no es un repo trending: es que **el gap 7 de `intel/trends.md` estaba mal** y hay que retirarlo.

### GegoK12 — el SIS open source permisivo que las dos pasadas anteriores dijeron que no existía

| Repo | URL | Licencia | Stars | Forks | Último commit | Stack |
|------|-----|----------|-------|-------|---------------|-------|
| **GegoK12** | https://github.com/Gego-K12/gegok12 | **MIT** ✅ | 54 | 97 | **2026-09-23** | PHP 8.4 + Laravel 12 |

Verificación: el archivo `LICENSE` del repo dice `MIT License`, con `SPDX-License-Identifier: MIT`, © 2025 GegoSoft Technologies and GegoK12 Contributors. 123 commits, 11 issues abiertos. School management / ERP completo, API-first, mobile-apps-ready, instalador visual en `/public/installer` o Docker. La organización mantiene además `gegok12-documentation` y **`Plugin-Hello-Teacher`** — o sea, **tiene sistema de plugins**, actualizado el 2026-09-23.

**Lo que esto retira.** El pase 2 declaró el gap 7 así: *"No hay SIS open source permisivo y vivo… en el lado administrativo el agente **siempre** va afuera, leyendo por API. No es preferencia de diseño, es la única opción limpia."* La conclusión era incorrecta. Con un core MIT y un punto de extensión por plugins, **el agente puede vivir adentro del SIS**, y como MIT no impone share-alike, ese plugin puede ser propiedad del cliente. Es la primera vez que la KB puede ofrecer eso en el lado administrativo. Patrón nuevo: **P9** en `compose/patterns.md`.

⚠️ **Y la condición que hay que leer antes de proponerlo: es open-core.** De 38 módulos, **26 están en el core MIT** (alumnos, admisiones, asistencia, tareas, biblioteca, staff, avisos, comunicación con padres) y **12 son add-ons Pro pagos, USD 100–250 cada uno** (USD 1.650 los doce): **examinación, gestión de fees**, timetable, media files, chat room, certificados, transporte, inventario, stock, video room, alumni y generador de exámenes. La licencia Pro es lifetime por dominio, con fuente incluido y 5 años de updates — no suscripción por alumno, que es razonable, pero **exámenes y cobranzas son justo los dos procesos que un agente querría automatizar primero**. Cotizarlos de entrada.

**Tracción, sin maquillaje:** 54 ★ con 97 forks. La proporción ~2:1 de forks sobre stars dice que se despliega más de lo que se estrella, lo cual es esperable en un ERP administrativo cuyo usuario es una escuela y no un desarrollador. Pero es un proyecto chico de un solo vendor (GegoSoft): riesgo de continuidad a declarar. **OpenEduCat (LGPL-3.0), más adoptado y con el agente afuera, sigue siendo la opción conservadora** y está bien elegirla.

### Por qué el gap se sostuvo dos pasadas — nota de método

Las dos pasadas anteriores buscaron la categoría ("SIS open source", "open source school ERP") y recibieron el consenso de los listicles, que repiten Fedena / RosarioSIS / openSIS y no incluyen GegoK12 porque es reciente. **Lo que lo encontró fue buscar por licencia y stack** — "school ERP MIT Laravel self-hosted" — no por categoría.

Regla que conviene aplicar al resto de la KB: **un gap de la forma "no existe X con licencia permisiva" hay que re-buscarlo con la consulta invertida.** Buscar la categoría devuelve el consenso establecido; buscar la licencia y el stack devuelve los proyectos nuevos, que son exactamente los que un gap de este tipo puede estar tapando. Candidatos a re-buscar así el próximo ciclo: el gap 1 (evaluador pedagógico) y el gap 6 (grading).

### Lo demás de la ventana: sin movimiento medible

Los cinco repos de la sección del pase 1 de hoy siguen en los mismos valores (LLMs-from-scratch 105.8k ★, minimind 63k, DeepTutor 40.6k, OpenMAIC 39.7k, NOMAD 38.8k) y los tres del pase 2 también (learn-claude-code 77.8k, ai-engineering-from-scratch 62.1k, tiny-llm 4.7k). Tres pasadas en un día no mueven star counts: la cadencia útil de este archivo es semanal, no horaria. **La próxima corrida conviene que priorice categorías sin cubrir antes que re-medir los mismos repos.**

Adyacente que apareció y **no** pasa a `foundations.md` por no ser de educación: `microsoft/mcp-for-beginners` — currículum open source de MCP con ejemplos en .NET, Java, TypeScript, JavaScript, Rust y Python. Es material de AI literacy técnica genuinamente útil para un track de formación, pero es de protocolo, no de educación, y no verificamos licencia ni stars de primera mano. Pista para la próxima corrida.

## 2026-09-30 (pase 2) — pistas pendientes, resueltas

La pasada anterior dejó tres repos anotados como "pista para la próxima corrida" porque no había podido verificar licencia y stars de primera mano. **Los tres son reales, permisivos y grandes.** Verificados vía WebFetch contra la página del repo.

| Repo | URL | Licencia | Stars (2026-09-30) | Lenguaje | Qué es |
|------|-----|----------|--------------------|----------|--------|
| learn-claude-code | https://github.com/shareAI-lab/learn-claude-code | MIT | **77.8k** | Python | Tutorial progresivo de 17 capítulos sobre cómo se construye un *harness* de agente: tools, gestión de conocimiento, sistema de tareas, coordinación de equipos. Tesis explícita del repo: "agency comes from model training, not external orchestration" |
| ai-engineering-from-scratch | https://github.com/rohitg00/ai-engineering-from-scratch | MIT | **62.1k** | Python | Curriculum de AI engineering: **523 lecciones en 20 fases**, de fundamentos matemáticos a agent engineering. Exige implementar los algoritmos a mano antes de usar frameworks de producción; cada lección deja un artefacto reusable (prompts, skills, agents, MCP servers) |
| tiny-llm | https://github.com/skyzh/tiny-llm | Apache-2.0 | 4.7k | Python | Curso de **serving** de LLMs para ingenieros de sistemas: KV cache, continuous batching, flash attention, paged attention, sobre APIs de arrays MLX y sin capas de red neuronal de alto nivel. Construye una vLLM en miniatura con Qwen3 |

**Lo que estos tres cambian para la KB.** La sección de AI literacy de `repos/foundations.md` tenía dos entradas (`LLMs-from-scratch`, `minimind`), las dos sobre *entrenar* un modelo. Estos tres cubren las capas que faltaban y que son las que un cliente corporativo realmente necesita:

- **`ai-engineering-from-scratch`** → el currículum completo, ya secuenciado en 20 fases. Es lo más cercano a un programa de capability building listo para usar que hay en abierto con licencia MIT.
- **`learn-claude-code`** → cómo se construye la infraestructura de agentes. 77.8k ★ lo vuelve el material de referencia de facto del tema.
- **`tiny-llm`** → operar e inferir eficientemente, que es donde se va el costo en producción. Nota: usa **MLX (macOS ARM64)**, así que como material de aula obliga a hardware Apple — verificar antes de comprometerlo en un programa.

Los tres son MIT o Apache-2.0: curricularizables sin fricción legal.

## 2026-09-30 — GitHub trending, ventana de septiembre 2026

Verificado vía WebFetch más agregadores de trending (`agents-radar`, `gittok`) para la ventana 2026-09-22 → 2026-09-30.

| Repo | URL | Licencia | Stars | Por qué aparece |
|------|-----|----------|-------|-----------------|
| LLMs-from-scratch | https://github.com/rasbt/LLMs-from-scratch | Apache-2.0 | 105.8k | El recurso de referencia para entender arquitectura transformer. Base de cualquier programa de AI literacy serio |
| minimind | https://github.com/jingyaogong/minimind | Apache-2.0 | 63k | LLM de 64M params entrenado desde cero en ~2h en hardware de consumo. Convierte "entrenar un modelo" en un ejercicio de aula |
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 40.6k | Trending sostenido; v1.6.12 del 2026-09-27 |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 39.7k | v1.1.2 del 2026-09-28 |
| Project NOMAD | https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | 38.8k | Servidor educativo offline-first con AI embebida; ~38.1k–38.8k en los conteos de esta semana |

Adyacentes que aparecieron en trending de educación AI sin que pudiéramos verificar licencia/stars de primera mano, y que por lo tanto **no pasan a `top.md`**: `shareAI-lab/learn-claude-code` (~77.8k ★ reportado), `rohitg00/ai-engineering-from-scratch`, `tiny-llm`. Registrados acá como pista para la próxima corrida.

## 2026-07-02 — pipeline automático (histórico, sin verificar)

⚠️ Salida cruda del pipeline. Conservada como historia. Idéntica a la de `agents/trending.md` de esa fecha — el pipeline escribía el mismo contenido en ambos archivos. Mayoría de repos con 0–24 estrellas. No usar como recomendación.

| Nombre | Licencia | Descripción | Stars |
|--------|----------|-------------|-------|
| [ai4kids](https://github.com/alfredang/ai4kids) | ? | 🤖 AI Kids Academy — a kids' AI learning portal (ages 4–16): gamified AI storyte | 1 |
| [flashcards-open-source-app](https://github.com/kirill-markin/flashcards-open-source-app) | MIT | AI-powered flashcards app built for serious daily study on iOS, Android, and the | 24 |
| [vacademy_platform](https://github.com/Vacademy-io/vacademy_platform) | AGPL-3.0 | Open source comprehensive e-learning platform with a focus on educational conten | 14 |
| [Edyfra](https://github.com/marsley01/Edyfra) | ? | Edyfra is a modern, modular web application built primarily in TypeScript and Ja | 2 |
| [claude-war-room](https://github.com/digestionadiabaticprocess828/claude-war-room) | MIT | Orchestrate six specialized AI agents to analyze code features from multiple ang | 2 |
| [PS-HK19_MindForge_MindForge](https://github.com/iqiipo-dev/PS-HK19_MindForge_MindForge) | ? | Provide context-based, accurate answers to syllabus questions using AI powered b | 2 |
| [unlimited-ai-platform](https://github.com/Ahmed-html/unlimited-ai-platform) | MIT | Build and deploy a Next.js AI chat platform with authentication, role management | 1 |
| [LearnX-Radar](https://github.com/Yusuprozimemet/LearnX-Radar) | MIT | LearnX-Radar is an automated “daily learning radar” for developers that tracks t | 0 |
| [STUTIFY](https://github.com/myxineglutinosameniere4389/STUTIFY) | ? | Convert text into natural speech with this automated stuttering and fluency tool | 0 |
| [aulalibre](https://github.com/loqganesh-hue/aulalibre) | MIT | Access Denmark's Aula with Rust tools, a CLI, and a FUSE mount for messages, fil | 0 |

---
*Historia conservada. Append-only: agregar arriba, nunca sobrescribir.*
