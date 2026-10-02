---
industry: education
region: Global
updated: 2026-10-02
---

# 🏭 Verticales de partida — Education

> Plataformas verticales reales, en producción, customizables con AI.
> Modelo: partir de algo que ya funciona y que ya tiene los datos, y agregar la capa agéntica arriba.
> Verificado vía WebFetch el 2026-09-30; las capas del pase 11, el 2026-10-01.
> **Pase 36 del 2026-10-02:** 🔵 **sin verticales nuevas, y dos datos que cambian cómo se cotiza sobre las que ya están.** 🟢 **Moodle está vivo y medido: 2.134 descargas/mes en Packagist, 485 versiones y release del 2026-10-01** —ayer—, GPL-3.0. Sigue siendo la vertical de mayor huella y la de mejor argumento de *«el cliente ya lo tiene»*. 🔴 **La capa de evaluación que se le monta encima está fechada y el orden de licencias es inverso al del resto de esta KB: lo desplegado es copyleft** (`oat-sa/extension-tao-testqti`, **885 versiones**, release del **2026-09-30**, GPL-2.0-only; `qtism/qtism`, 218.212 descargas totales, GPL-2.0-only) **y lo permisivo es lo nuevo** (`@longsightgroup/qti3-cli`, **MIT**, cero dependencias de terceros) — **su manifiesto MCP de 20 tools está escrito en `compose/patterns.md` (P76)**, con el corte **18 de lectura / 2 de escritura** medido en el paquete y el contrato de estado del modo adaptativo documentado. ⚠️ **Y el dato que hay que tener antes de prometer un portal de datos educativos públicos en Brasil: INEP no publica API.** El Censo Escolar se distribuye como **ZIP con CSV delimitado por `;`, ~2-4 GB comprimidos y 10-20 GB descomprimidos por año**, en cuatro dimensiones (**Escolas, Turmas, Matrículas, Docentes**), más ASCII con *input files* de SAS y SPSS; la única API de terceros es **GPL-2.0, cubre sólo IDEB y su dominio ya no resuelve**. 🔵 **Por eso lo que corresponde montar ahí no es un servidor fachada sobre la fuente —como `ibge-br-mcp` hace con el IBGE, que sí publica REST— sino una vertical de datos propia: ingesta → almacén columnar → capa semántica → MCP de sólo lectura, 8-12 semanas** (**P77**). **El código INEP de escuela es la clave de *join*** que ya usan los portales estaduales (el de São Paulo publica *datasets* etiquetados por *Código INEP Escola*, **CC-BY-4.0**), así que el enriquecimiento estadual es incremental.
> **Pase 26:** entra **una vertical entera que veinticinco pasadas no buscaron — la biblioteca (ILS/OPAC)** — y entra
> con una opción **permisiva y grande**: **FOLIO** (Apache-2.0, 3.096 commits, multi-tenant, bus de Kafka). Se agregan
> además **admisiones** y ***student success*** 🔴 **para decir que no hay qué proponer en permisivo**: lo que sirve es
> GPL/LGPL y lo permisivo son proyectos de portafolio; en *student success* lo open source es de **2013–2014** y no vive
> en GitHub.
> **Pase 25:** entran tres capas — **horarios institucionales** (`UniTime`, Apache-2.0, 349 ★), **aserción de
> competencias** (`CaSS`, Apache-2.0, la pieza que la capa CASE del pase 14 no tenía) y **supervisión remota de exámenes**,
> que se agrega 🔴 **para decir que no hay qué proponer**: las cinco piezas que existen son copyleft o tienen pesos de uso
> no comercial, y es justo la capa que el **Annex III** nombra de alto riesgo. La alternativa que sí se vende es **P49**.
> **Pase 23:** entra **Frappe Education** en la capa SIS y **se cierra la pregunta del pase 21 sobre dónde vive el módulo educativo de ERPNext** — es una app aparte, `frappe/education`, GPL-3.0.
> **Pase 11:** entra la capa **Apereo (ECL-2.0)** —Sakai, Opencast, uPortal, OpenLRW—, que diez pasadas descartaron por un filtro de licencia mal aplicado, y se documenta qué **no** proponer cuando el cliente pide *early warning*.
> **Pase 35 del 2026-10-02:** **la columna de la puerta de agente deja de ser escasa y pasa a ser la mejor abastecida de
> esta KB.** Canvas tiene **cinco** puertas (cuatro MIT) y la más grande es **`bruchris/canvas-lms-mcp`** —**165 tools,
> cifra citable, escribe, MCP 1.x**— con **8 ★**; Moodle tiene **cuatro** más un cliente envolvible. 🔵 **Y aparece la
> respuesta de arquitectura a la pregunta que frenaba todos los pilotos («¿y si TI no nos habilita nada?»):
> `bunizao/moodle-cli` y `moon0825/jbnu-lms-student` trabajan desde la *sesión del navegador del propio usuario*, con
> passkey y 2FA, sin token institucional** —al costo de ser de sólo lectura. 🟢 **El empaquetado LMS entra a la tabla:**
> `coursecode` expone **15 tools** y su `build` toma `format` como enum (`cmi5`/`scorm2004`/`scorm1.2`/`lti`). 🔴 **Y la
> capa de evaluación se reordena por despliegue: lo instalado es TAO y es GPL-2.0-only** (117.544 descargas, 844
> versiones), así que lo permisivo (`qti3-*`, `instructure/qti`) es **lo único proponible** — con **`qti3-a11y`** y
> **`qti3-pnp`**, que abren accesibilidad de evaluación como entregable auditable (**P72**). ⚠️ **Open edX cambia de
> recomendación: proponer con presupuesto de mantenimiento (gap 70).** Ver la sección del pase 33, abajo.

> **Pase 28 del 2026-10-01:** la columna de la puerta de agente **gana una fila y pierde una certeza**. Gana **OneRoster**, que tiene puerta **0BSD** con **164 métodos y escritura** (`trilogy-group/oneroster-ts`) — el pase 26 la había declarado vacía. Y sobre **Open edX**, el «no hay puerta» se mantiene pero **ya se sabe sobre qué se construiría**: la API **escribe matrícula y notas por lote**, y el ***authoring* de Studio está declarado experimental en el repo** (**gap 50**). Ver la sección del pase 28, abajo.
> **Pase 27 del 2026-10-01:** se agrega **la columna que faltaba en veintiséis pasadas — ¿la vertical tiene puerta de agente?** Moodle **sí** (dos conectores **MIT**, uno que escribe notas) y Canvas **sí**; 🔴 **Open edX no tiene ninguna**, y es la de mayor huella pública en LATAM e India. **Las LMS son copyleft pero las puertas son MIT**, y por eso se pueden componer. Ver la sección del pase 27, abajo.


## 🗓️🔒 Las dos plataformas institucionales que esta base nunca había listado: horarios y examen seguro (pase 41 del 2026-10-02)

**El pase 40 midió por registro que las capas de *timetabling* y *proctoring* estaban vacías de agente y mandó a medirlas
por su sitio de proyecto. Hecho, aparecen dos plataformas que encajan exactamente en el modelo de este archivo —algo que
ya funciona, que ya tiene los datos, y al que se le agrega la capa agéntica arriba— y que ninguna de las 40 pasadas
anteriores había listado.**

| Plataforma | Qué es | Licencia | Estado medido | Puerta de agente | Región de origen |
|---|---|---|---|---|---|
| 🟢 **UniTime** — [`UniTime/unitime`](https://github.com/UniTime/unitime) | **Horarios académicos y de exámenes**: asignación de cursos, aulas y exámenes, *student scheduling* en línea | 🟢 **Apache-2.0** (Apereo Foundation) | 🟢 `HEAD` **2026-10-01**, **202 tags**, Java | 🔴 **NO existe** — y **sí hay API formal**: 15 conectores con nombre, verbos y token (ver `repos/foundations.md`) | **North America** (Apereo; origen Purdue University) |
| 🟢 **SEB Server** — [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | **Administración, monitoreo y *proctoring* de exámenes**: plantillas de examen, configuración del cliente, indicadores, monitoreo en vivo | ⚠️ **MPL-2.0** (copyleft **débil**, por archivo) | ⚠️ `master` **2026-04-01** / 🟢 `dev-3.0` **2026-10-01**, **108 tags** | 🔴 **NO existe** — **36 controladores REST / 41 endpoints** sin envolver | **EMEA** (ETH Zürich, Suiza) |
| 🟢 **Safe Exam Browser** (cliente) — [`seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) | **Bloqueo de escritorio para examen**: convierte la máquina en estación controlada | ⚠️ **MPL-2.0** | 🟢 `HEAD` **2026-09-25**, **20 tags**, C# | n/a (es cliente de escritorio) | **EMEA** (ETH Zürich, Suiza) |

🟢 **Por qué SEB Server es la incorporación más fuerte de este archivo en varios pases, y no es por su licencia: ya está
integrado con tres de las plataformas que este archivo recomienda.** Su `enum LmsType` nombra **`OPEN_EDX`**,
**`MOODLE`**, **`MOODLE_PLUGIN`** (la única combinación con `LMS_FULL_INTEGRATION`) y **`OPEN_OLAT`** — las tres están
listadas acá como verticales de partida desde los primeros pases. **El trabajo no es integrar: es configurar
`MOODLE_PLUGIN` y escribir la puerta de agente.**

🔵 **Y la diferencia de licencia que hay que saber decir en una propuesta:** la capa de *proctoring* de Open edX es
**AGPL-3.0** (aunque su directorio de *backends* está *carved-out* en **Apache-2.0** — ver `repos/foundations.md`),
mientras **SEB es MPL-2.0: copyleft débil por archivo.** Se publica lo que se modifica de los archivos cubiertos; **lo
que se construye al lado queda del integrador.** **Son dos rutas con dos perfiles legales distintos para el mismo
requisito**, y hasta este pase esta base sólo tenía una.

⚠️ **Las dos advertencias que viajan con estas filas:**
1. 🔴 **UniTime expone un conector `script` que acepta `POST`** — ejecución de scripts del servidor. Cualquier envoltorio
   MCP lo pone en la *denylist* antes de la primera demo (**P88**).
2. ⚠️ **En SEB Server, la rama por defecto (`master`) tiene 6 meses y la de desarrollo commiteó ayer.** Antes de
   proponerlo hay que decidir **si el entregable se para en el release o en la rama** (**gap 87**).

🔴 **Y el encuadre regulatorio que estas dos filas arrastran, porque es el que decide el precio:** el *«monitoreo durante
exámenes»* está **nombrado en el Anexo III punto 3 del AI Act** (plazo **2027-12-02**) y **Vietnam nombra la
*«monitorización del comportamiento»* en evaluación** entre sus seis sectores de alto riesgo (**cumplimiento desde
2027-03-01**). **Es la única capa de esta KB nombrada por el regulador en DOS regiones** — y es la que acaba de medirse
sin competencia agéntica. Ver `intel/trends.md`, tendencia **156**.

## 🧾 Las capas administrativas de esta vertical, medidas por registro: admisiones tiene una pieza APAC viva, y la biblioteca gana su primera puerta de agente (pase 40 del 2026-10-02)

El barrido por registro del pase 40 fue a las capas administrativas que esta vertical lista como módulos de ERP pero
nunca había medido por separado. **Dos resultados: una alta en admisiones y la puerta de agente de una plataforma que
este archivo lleva 30 pases listando sin una sola.**

### 🟢 Admisiones: el nicho se abastece con *addons* de Odoo, y el único vivo es de Indonesia

| Pieza | Licencia | Última señal | Qué aporta | Región |
|---|---|---|---|---|
| 🟢 `odoo14-addon-ssi-school-admission` (+ `-lead`, `-operating-unit`) | **AGPL-3** ⚠️ | PyPI **2026-05-01** · 6 releases | **Admisión escolar como módulo de Odoo 14**, con submódulos separados para **gestión de *leads*** (el embudo previo a la matrícula) y para **unidad operativa** (multi-sede). Publicado por **Simetri Sinergi Indonesia** (`simetri-sinergi.id`) | **APAC** (Indonesia) |
| ⚠️ `odoo9-addon-openeducat-admission` / `odoo10-addon-openeducat-admission` | LGPL-3.0 | 🔴 Odoo **9 y 10** — versiones EOL | El módulo de admisiones de **OpenEduCat**, empaquetado para Odoo 9/10. 🔴 **El JSON de PyPI de los dos devuelve sin metadatos** y las versiones de Odoo son históricas: **usar el módulo desde el repo de OpenEduCat, no desde el registro** | APAC (India) |

🔵 **El patrón que esto confirma, y ya es el tercero igual en esta vertical:** la capa administrativa educativa se
construye **como módulo de un ERP generalista** (Odoo, Frappe) y **no como producto educativo**, y quien la publica es
un integrador regional de APAC — igual que **GegoK12** (India) y **Frappe Education** (India). **Para un engagement de
admisiones la pregunta correcta no es «¿qué plataforma de admisiones open source hay?» sino «¿el cliente ya corre
Odoo o Frappe?»** — porque si la respuesta es sí, la capa es un *addon* y la AI va arriba.

⚠️ **Y la advertencia de licencia que esta vertical ya tiene escrita para su tabla de ERP aplica igual acá:** AGPL-3 y
LGPL-3 son copyleft, así que **el agente va afuera**, leyendo por API, con su propia licencia (ver el patrón de la
tabla de plataformas y el **gap 46**).

### 🟢 Koha: la vertical de biblioteca estrena puerta de agente, y llega de costado

**`Koha` —el ILS open source más desplegado del mundo— no tenía ninguna pieza agéntica en esta KB.** El pase 40
encuentra la primera, y no es un conector de Koha: es **la mitad biblioteca de `DUTIC-mcp`** (MIT, Perú), que resuelve
su catálogo contra **un *gateway* de Koha propio** en `src/biblioteca/infrastructure/koha/` (`kohaGateway.ts`,
`kohaHttp.ts`, `kohaParsers.ts`, `kohaUrls.ts`), con base overridable por `DUTIC_LIBRARY_URL`.

| | Antes del pase 40 | Después |
|---|---|---|
| **Koha** (ILS, GPL) | 🔴 sin puerta de agente | ⚠️ **gateway MIT extraíble** de `DUTIC-mcp` (2 tools: `dutic_library_search`, `dutic_library_record`) |
| **DSpace** (repositorio) | 🔴 sin puerta (hasta el pase 39) | ⚠️ `armenian-national-library-mcp` (MIT, 23 tools, todas de lectura) — apuntado a **una** instancia |

🔵 **Las dos tienen la misma forma y conviene nombrarla porque decide cómo se cotiza: son implementaciones de
referencia apuntadas a una institución, no conectores genéricos.** Lo que se reusa es **el parser y el mapeo del
protocolo** —que es el trabajo— y lo que se reescribe es el destino. ⚠️ **En el caso de `DUTIC-mcp` hay una reserva
extra: el catálogo se resuelve contra una instancia de Supabase del autor** (`SAAS_SUPABASE_URL`), así que **extraer
el *gateway* de Koha es más limpio que adoptar la pieza entera**.

### 🔴 Lo que estas capas NO tienen, confirmado por doble canal

**Ni *timetabling*, ni *proctoring*, ni admisiones, ni *student success*, ni accesibilidad tienen puerta MCP de
educación en ninguno de los cuatro registros de paquetes.** Y en dos de ellas la pieza canónica **no está en ningún
registro**: 🔴 **`UniTime`** (el planificador de horarios universitario de referencia) y 🔴 **Safe Exam Browser**
devuelven **cero nombres** en los 903.402 de PyPI. **No es que no existan: es que se distribuyen fuera del canal que
este barrido mide**, que es exactamente lo que la tendencia 23 de esta base dice sobre la infraestructura educativa
realmente desplegada.

🔵 **La consecuencia práctica para esta vertical:** para *timetabling* y *proctoring* el inventario hay que hacerlo
**por sitio del proyecto**, no por registro — y para *proctoring* la respuesta ya está medida y es
**`openedx/edx-proctoring`, AGPL-3.0** (ver `repos/foundations.md`).

## 🟢 La fila roja de Moodle se cierra con TRES opciones MIT, y aparece el lado proveedor de OneRoster (pase 38 del 2026-10-02)

El pase 37 dejó esta vertical con **tres filas rojas en la tabla de puertas**: Moodle-que-pone-nota (`peancor`, frío
7,3 m), xAPI (`learnmcp-xapi`, congelado 13,1 m) y OneRoster (`oneroster-ts`, congelado 15,2 m). Este pase fue a buscar
reemplazo para las tres. **Dos se cierran; una no, y se puede decir por qué sin perder la propuesta.**

### 🟢 Moodle: la fila roja pasa a verde, y con mejor diseño que el original

| LMS | Puerta | Licencia (verificada) | `HEAD` | Qué se puede prometer |
|---|---|---|---|---|
| **Moodle** | 🟢 **`toshieji/moodle-grading-mcp`** | **MIT** ✅ | 🟢 **2026-09-07** | 🟢 **Se propone, y es la que hay que proponer cuando el cliente es una institución.** **9 tools.** Pone nota y devolución **en borrador** (`workflowstate=readyforreview`): **el docente sigue siendo quien publica**. Allowlist de cursos, `MOODLE_ALLOW_WRITE=1`, audit trail JSONL, sin notificación al alumno, pie de declaración de AI |
| **Moodle** | 🟢 **`NiccoloSalvini/mcp-moodle-teacher`** | **MIT** ✅ | 🟢 **2026-09-25** | 🟢 **Se propone cuando hace falta superficie amplia.** **22 tools** (15 lectura / 3 escritura / 4 utilidad): nota con devolución, anuncios, **asistencia** y `students_at_risk`. Toda escritura pide confirmación. ⚠️ **Se está renombrando a `mcp-moodle-staff`** |
| **Moodle** | 🟢 `Dymayo/moodler-mcp` | **MIT** ✅ | 🟢 **2026-09-19** | ✅ **Enumeradas en el pase 39: 38 tools (30 lectura · 6 escritura de alumno · 2 docente), Python.** 🔴 **Pero PUBLICA la nota** (`workflowstate=""`): para alto riesgo, `moodle-grading-mcp` le gana |
| **Moodle** | ⛔ `csmediapro/moodle-mcp-server` | 🔴 **AGPL-3.0** | 🟢 2026-10-01 | ⛔ **No proponer para producto.** Es **el más activo de la capa** y sólo lee: la fecha tienta y la licencia lo descarta |
| **Moodle** | ⛔ `loyaniu/moodle-mcp` | 🚫 **sin licencia** | 2026-06-28 | ⛔ **No proponer.** `LICENSE`/`.md`/`.txt`/`COPYING` en `main` y `master`: **404 en los 8** |

🔵 **Lo que esto cambia en una frase de reunión:** hasta ayer, *«corregir dentro de Moodle con software permisivo»* tenía
**una** respuesta y estaba fría hace siete meses. Hoy tiene **tres**, todas MIT, todas con commit del último mes, y la
mejor de las tres **no publica notas: las deja en borrador**. 🟢 **Eso deja de ser una limitación técnica y pasa a ser el
argumento de cumplimiento**: el régimen de alto riesgo del AI Act para evaluación de alumnos, y las reglas de supervisión
humana de Oklahoma y Maryland, piden exactamente eso —que la decisión final la publique una persona— y acá viene
**impuesto por el servidor**, no prometido en una política. Ver `intel/trends.md`, **tendencias 133 y 134**.

### 🟢 OneRoster: la vertical gana el lado proveedor, que es una plataforma, no una librería

| Pieza | Licencia | `HEAD` | Rol | Qué aporta a un entregable |
|---|---|---|---|---|
| 🟢 **`Ed-Fi-Alliance-OSS/edfi-oneroster`** | **Apache-2.0** ✅ | 🟢 **2026-10-01** | **Servidor** | **Expone OneRoster 1.2 (14 endpoints GET) sobre una base Ed-Fi ODS que el distrito ya tiene.** Ed-Fi DS 4.0 y 5.0/5.1/5.2, Docker o IIS. **86 tags**, v1.0.2 |
| 🟢 `CSR2017/edfi-oneroster` | **Apache-2.0** ✅ | 🟢 2026-09-22 | Servidor | Misma función. 🔴 Relación upstream sin resolver → `gap 79` |
| 🟢 `TCI/OneRoster` | **MIT** ✅ | 🟢 2026-09-11 | **Cliente** (Ruby) | Consumo de `students`/`teachers`/`classes`/`courses`/`enrollments`. v2.3.27 |
| 🔴 `trilogy-group/oneroster-ts` | 0BSD | 🔴 2025-06-27 | Cliente (TypeScript) | 🔴 **Congelado 15,2 m.** Sigue siendo la única opción **en TypeScript**, y no tiene sucesor |

🔵 **El cambio de encuadre para esta vertical, y es el que importa comercialmente:** OneRoster venía tratado acá como
*«una librería que hay que envolver»*. **Con `edfi-oneroster` pasa a ser una plataforma desplegable** —Docker, API HTTP
estándar, sobre el ODS que el distrito ya corre— de la misma clase que Moodle u OpenEduCat en la tabla de plataformas
recomendadas: **se instala y se le pone AI arriba**, en vez de escribirle un cliente. ⚠️ **Dato de gobernanza:** el repo
vive en la org **Ed-Fi-Alliance-OSS** y su copyright dice **«1EdTech Consortium, Inc.»** — artefacto conjunto de los dos
consorcios, el primero de esta base. **No declara certificación 1EdTech: no prometerla.**

🔴 **Y el dato que hay que tener a mano antes de cotizar rostering:** de las **ocho** implementaciones de OneRoster que
devuelve un barrido abierto, **cinco llevan ≥ 3 años sin un commit** (`jdolny/OneRoster.NET` 3,0 a · `gotranseo/oneroster`
3,4 a · `bgwdotdev/go-oneroster` 6,9 a · `EASOL/edfi-to-oneroster` 10,0 a) y una sexta está congelada. **Quedan tres
usables.** Es la capa de esta base donde la selección pesa más.

### 🔴 xAPI: la fila sigue roja, y así es como se dice sin perder el proyecto

`DavidLMS/learnmcp-xapi` sigue **congelado hace 13,1 meses** y no tiene sucesor en la capa de puerta. ⚠️ **El fork que
aparece primero en cualquier búsqueda —`ashleycribb/learnmcp-xapi`, `main` de 2026-09-17— NO es sucesión: está 2 commits
adelante y los dos son configuración de Cloud Run.** 🟢 **Pero el riesgo está contenido, y la contención es verificable:**
el LRS de abajo se cambia por variable de entorno (plugins de la v2.0.0), y los dos LRS permisivos están vivos —
`yetanalytics/lrsql` (Apache-2.0, `HEAD` **2026-10-01**, v0.9.9) y `openfun/ralph` (MIT, **v5.0.1**, `HEAD` 2026-09-07,
**pública europea**). Lo congelado son ~32 commits de adaptador; el dato del cliente vive en el LRS. **Se propone por
`P78`**, con fork mínimo y contrato de mantenimiento, **no como riesgo sin dimensionar**.


## 🔴 La columna «puerta de agente» de esta vertical, fechada: tres de las puertas que esta KB propone están paradas (pase 37 del 2026-10-02)

**El pase 27 abrió en este archivo la columna *«¿la vertical tiene puerta de agente?»*, y los pases 30 y 33 la llenaron
hasta declararla «la capa mejor abastecida de esta KB». Sigue siendo cierto en número de puertas. Este pase les puso fecha,
y en tres casos la fecha cambia lo que se puede prometer.**

**El instrumento:** `git ls-remote` + `git fetch --depth 1` del sha de `HEAD` + `git log -1 --format=%cI`, sobre las 49
filas de `agents/top.md`. **49 de 49 respondieron, cero 404.** Detalle completo en `repos/trending.md` (pase 37).

### La capa de conectores, por LMS, con la fecha del último commit en la rama por defecto

| LMS / estándar | Puerta | Licencia | `HEAD` | Estado | Qué se puede prometer |
|---|---|---|---|---|---|
| **Canvas** | `bruchris/canvas-lms-mcp` | **MIT** | 🟢 **2026-09-20** | 🟢 activo, 69 tags | 🟢 **Se propone sin reservas.** 165 tools, escribe |
| **Canvas** | `vishalsachdev/canvas-mcp` | **MIT** | 🟢 **2026-10-01** | 🟢 activo, 22 tags | 🟢 Se propone. El más traccionado (269 ★) |
| **Moodle** | `bunizao/moodle-cli` | **MIT** | 🟢 **2026-10-02** | 🟢 **el más activo de la capa** | 🟢 Se propone. Lado alumno, sin token de admin |
| **Moodle** | `MarcosNahuel/moodle-mcp` | MIT | ⚠️ **2026-05-03** | ⚠️ tibio (5,0 m) | Se propone con reserva |
| **Moodle** | 🔴 `peancor/moodle-mcp-server` | **MIT** | 🔴 **2026-02-22** | 🔴 **frío (7,3 m)** | 🔴 **Es la única pieza permisiva que PONE NOTA y devolución dentro de un LMS** (el tramo final del gap 6, **P54**/**P55**). **Se sigue proponiendo, pero el mantenimiento se cotiza** |
| **Open edX** | `openedx-mcp` + `tutor-contrib-openedxmcp` | 🔴 **AGPL-3.0** | — (PyPI) | 🔴 **gap 68**: 12 releases en 2 días y nada en 70 | Oficial, en proceso, **copyleft y en proceso Django** |
| **xAPI / LRS** | 🔴 `DavidLMS/learnmcp-xapi` | **MIT** | 🔴 **2025-08-29** | 🔴 **CONGELADO (13,1 m)**, **1 sola rama** | 🔴 **Es «la única puerta» del gap 64 y la pieza más citada de esta base (42 menciones).** Ver abajo |
<!-- pase 39 del 2026-10-02: las nueve filas siguientes salen del barrido por REGISTRO de paquetes (npm/PyPI/Packagist/RubyGems) por nombre de PROYECTO, no de protocolo. Licencia leída del archivo o del tarball; vitalidad por `git ls-remote` + commit de la rama por defecto; tools contadas en el código. Ver `repos/trending.md` y `agents/trending.md` del mismo pase. -->
| **Moodle** | `PabloPC05/mcp-usc` | **MIT** | 🟢 **2026-08-27** | 🟢 activo (1,2 m) | 🟢 **91 tools y 22 gemelos `preview_*`: el único freno de escritura imponible desde afuera.** ⚠️ Mitad institucional (USC) |
| **Moodle** | `JOSETRA44/DUTIC-mcp` | **MIT** | 🟢 **2026-09-24** | 🟢 activo (8 d) | 🟢 **Única puerta LATAM con licencia verificada** (UNSA, Perú). 12 tools + biblioteca. ⚠️ `encuesta_fill_all` es escritura discutible |
| **Moodle** | `Dymayo/moodler-mcp` | **MIT** | 🟢 **2026-09-19** | 🟢 activo (13 d), **0 tags** | ⚠️ **38 tools (30/8), pero PUBLICA la nota** (`workflowstate=""`). Huella grande: `playwright` |
| **Sisu (SIS, educación superior)** | `@ink-waffle/sisu-mcp` | ⚠️ **MIT** sólo por campo de npm | 🟢 **2026-09-17** (release) | ⚠️ 1 release, **sin repo público** | 🟢 **La única puerta de SIS de esta KB**: *attainments*, *study rights*, matrícula, horarios, planes |
| **Ed-Fi (Data Standard)** | `ed-fi-sdk-mcp` (oficial, npm `edfi`) | **Apache-2.0** | 🔴 **2025-10-03** (release) | 🔴 **1 release, 12 meses**, repo ilegible | ⚠️ **11 tools de ESQUEMA, cero de dato de alumno.** Sirve para escribir la integración, no para consultar el distrito |
| **Frappe (ERPNext / Education / LMS)** | `frappe-mcp-server` | ⚠️ **ISC** sólo por campo de npm | 🔴 **2025-07-30** (release) | 🔴 **14 meses**, repo ilegible | 🔴 **21 tools de DocType con `call_method` y `delete_document`: escritura total.** No proponer sin *gateway* que recorte tools |
| **DSpace (repositorio / biblioteca)** | `suren-kk/armenian-national-library-mcp` | **MIT** | 🟢 **2026-08-10** | 🟢 activo (1,7 m) | 🟢 **23 tools, todas de lectura por construcción.** 🔴 Apuntado a UNA instancia: referencia para generalizar |
| **Open Badges 3.0 (credenciales)** | `maxxeddev/open-badges-mcp` | **MIT** | ⚠️ **2026-06-10** | ⚠️ tibio (3,7 m), 5 tags | 🟢 **Cierra la ausencia de puerta MCP de credenciales**: spec + emisión + **firma Ed25519/`DataIntegrityProof`** + validación |
| **INEP / datos educativos (BR)** | `dasgltd/mcp-brasil` | **MIT** | 🟢 **2026-08-18** | 🟢 activo (1,5 m), **23 tags** | 🟢 **13 tools de ENEM + Censo Escolar sobre ingesta de microdatos, con whitelist LGPD de 8 columnas** |
| **OneRoster** | 🔴 `trilogy-group/oneroster-ts` | **0BSD** | 🔴 **2025-06-27** | 🔴 **CONGELADO (15,2 m)**, 5 ramas de bot sin mergear | 🔴 **132 tools, la superficie más grande de esta KB — y nadie la atiende** |
| **SCORM** | `giacomomaria81/scorm-mcp-server` | MIT | 🟢 **2026-09-03** | 🟢 activo, 6 tags | 🟢 Se propone. Offline |
| **Open edX (Tutor)** | `ArnaudGuiovanna/tutor-mcp` | — | 🟢 **2026-10-01** | 🟢 activo, 7 tags | 🟢 Se propone |
| **Gradescope** | `Yuanpeng-Li/gradescope-mcp` | — | ⚠️ **2026-05-13** | ⚠️ tibio (4,6 m) | Con reserva |
| **CaSS / CASE** | `cassproject/CASS` | Apache-2.0 | (fuera de esta tabla) | — | Ver **P50**, **P57**, **P60** |

### 🔴 Lo que esto cambia en una conversación con cliente, en tres frases

1. 🟢 **La capa Canvas y la capa Moodle del lado alumno están sanas** — cuatro puertas MIT con commits de las últimas dos
   semanas. **Un proyecto que entra por Canvas o por Moodle-alumno no tiene riesgo de dependencia.**
2. 🔴 **La capa de telemetría tiene un problema que hay que poner en la propuesta, no esconder.** `learnmcp-xapi` es
   **MIT**, hace exactamente lo que **P67** y **P68** necesitan (3 tools: 1 escribe, 2 leen), y **no recibe un commit desde
   el 2025-08-29**. Tiene **una sola rama**, así que no hay desarrollo en otro lado. ⚠️ **No es una razón para no
   proponerlo** —es 3 tools sobre una API estándar, la superficie más chica y estable de toda esta KB, y el estándar xAPI
   no se mueve— **pero el mantenimiento pasa a ser una línea del presupuesto en vez de un supuesto.** 🟢 **El resto de la
   receta P67/P68 está sano:** `lrsql` (Apache-2.0) publicó **`v0.9.9` el 2026-10-01** y **Ralph** (MIT) sigue vivo en
   `main`.
3. 🔴 **La capa OneRoster es la que peor está, y es la de entrada a cualquier proyecto con SIS.** `oneroster-ts` es
   **0BSD** —la licencia más permisiva que existe, **se puede forkear sin ninguna obligación**— con **132 tools** y
   **quince meses sin que un humano toque la rama principal**. 🔵 **Que sea 0BSD es justamente lo que vuelve esto
   manejable: el fork no tiene costo legal.** Lo que no hay es reemplazo: el único candidato activo del registro
   (`@timeback/oneroster`) **no declara licencia** (**gap 75**).

### 🔵 La distinción de método que hay que aplicar al leer cualquier tabla como ésta

**La actividad de bot no es mantenimiento.** `oneroster-ts` tiene un ref de hace cuatro meses, pero son **cuatro ramas
`dependabot/*` y un `speakeasy-sdk-regen-*`, ninguna mergeada**. `educhain` tiene su tip más nuevo en una rama
**`claude/*`** sin mergear, con `main` parado desde el **2025-12-03**. 🔵 **Se fecha el tip de la rama por defecto, nunca el
ref más nuevo** — un barrido que tomara el ref más nuevo declara vivos a los dos (**gap 72**, tendencia **124**).


## 🎖️ La vertical de credenciales tiene por fin una implementación **OB 3.0 completa** — y es copyleft de red: `Certo` — pase 34 del 2026-10-02

**Esta base venía diciendo que la capa de credenciales no tenía con qué partir:** `badgr-server` da **404**, el Open
Badges de CaSS es **OB 2.0 y no 3.0**, y CaSS deja **CASE, CEASN y Open Badges enteros fuera de MCP**. **Existe una
plataforma OB 3.0 entera, y no estaba en ninguno de los ocho archivos de esta KB.**

| Plataforma | Licencia | Stack | Estándares | Puerta de agente |
|---|---|---|---|---|
| [`Schroedinger-Hat/certo`](https://github.com/schroedinger-hat/certo) | ⚠️ **AGPL-3.0** — leída del `LICENSE` (**200**): *«GNU AFFERO GENERAL PUBLIC LICENSE Version 3»* | **Strapi 5.x** (backend) + **Nuxt 3** (frontend) | **Open Badges 3.0**, **W3C Verifiable Credentials**, **DIDs** | 🔴 **No** — ninguna puerta MCP (reconfirmado por segundo instrumento en este pase) |
| [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) | **Apache-2.0** ✅ (`LICENSE` **200** en `main` y `master`) | — | **Open Badges** + **CLR** | — (validador: web, HTTP y API) |

**Qué hace Certo, leído del README y no de una reseña:** los emisores crean **plantillas de insignia (*Achievements*)**
con criterios y habilidades asociadas; emiten **individualmente o en lote por CSV**; los receptores las ven en su panel;
**cualquiera verifica la autenticidad en una página pública**; y el receptor comparte a **LinkedIn**. Casos de uso que
el propio proyecto declara: instituciones educativas, organizaciones de formación, eventos, empresas, comunidades open
source y asociaciones profesionales.

🔴 **La licencia decide cómo se propone, y hay que decirlo antes de cotizar.** **AGPL-3.0 en un servicio de red obliga a
ofrecer la fuente a los usuarios del servicio.**

- ✅ **Como plataforma desplegada para el cliente** —el cliente la opera, la customiza y asume la obligación— **sirve, y
  es la única opción OB 3.0 completa que esta KB conoce.**
- 🔴 **Como componente embebido en un producto propietario de Globant, no sirve.** La obligación alcanza al derivado.

🟢 **Y la pieza Apache-2.0 es la que vuelve el expediente defendible.** El validador de **1EdTech** permite verificar la
credencial emitida **contra el consorcio que publica el estándar**, sin depender del emisor ni de Certo. **Esa
separación —emisor copyleft desplegado del lado del cliente, validador permisivo del lado del expediente— es lo que
convierte «cumplimos Open Badges» en una afirmación que un área de compras puede comprobar.** Ver **P74**.

⚠️ **Y la advertencia de barrido que este pase deja sobre esta vertical:** el candidato que *parecía* la puerta de
agente de esta capa —`quizlar/mcp-server`, **MCP, educativo, `LICENSE` MIT**— **no tiene código**: su `server.json`
declara `remotes` contra `https://mcp.quizlar.app/mcp/` detrás de una API key. **Es un servicio propietario con un
manifiesto MIT.** Ver **colisión 9** en `agents/trending.md` y la tendencia **104**.
## 🟢 La columna de la puerta de agente deja de ser escasa — y la capa de conectores pasa a ser la mejor abastecida de esta KB (pase 33 del 2026-10-02)

**El pase 27 agregó esta columna para decir que casi no había puertas. El pase 30 cerró el último «no». Este pase mide la
columna completa y el resultado es el contrario del de seis pases atrás: hay puertas de sobra, son casi todas permisivas,
y el problema ya no es encontrarlas sino elegirlas.**

| Vertical | Licencia de la plataforma | Puertas de agente | Licencias | Arquitectura | Cuál proponer |
|---|---|---|---|---|---|
| **Canvas** | AGPL-3.0 | 🟢 **Cinco** (4 usables) | **MIT** ×4 · 🔴 **1 sin licencia** | Proceso aparte, habla REST | 🔵 **`bruchris/canvas-lms-mcp`** — **165 tools, cifra citable, escribe, MCP 1.x, 62 versiones**. `vishalsachdev/canvas-mcp` queda como la de más tracción (269 ★) **pero con cifra de tools inestable** |
| **Moodle** | GPL-3.0 | 🟢 **Cuatro** + 1 cliente envolvible | **MIT** ×3 · ⚠️ **AGPL-3.0** ×1 | Proceso aparte, Web Services por token — **salvo `moodle-cli`** | **Docente que califica:** `peancor/moodle-mcp-server` (MIT, escribe nota y devolución). 🔵 **Cliente que no quiere tocar su Moodle:** **`bunizao/moodle-cli`** — trabaja desde la **sesión del navegador del usuario**, **sin token de administrador ni habilitación de Web Services** |
| **Open edX** | AGPL-3.0 | ✅ Una, **oficial** | 🔴 **AGPL-3.0** | 🔴 **EN PROCESO: plugin Django dentro del LMS *y* del CMS** | ⚠️ **Proponer con presupuesto de mantenimiento (gap 70): 12 releases en dos días de julio y nada en los 70 siguientes, todavía `0.1.x`** |
| 🔵 **LMS institucional** (categoría nueva) | la de la institución | ✅ Una, **no oficial** | **MIT** | STDIO local; **login por el navegador del usuario, passkey y 2FA** | **`moon0825/jbnu-lms-student`** (Corea, **25 tools, sólo lectura**). **No es pieza instalable para un cliente: es la arquitectura de referencia** de «agente sobre el LMS que ya existe, sin pedirle nada a TI» |
| 🟢 **Empaquetado LMS** (SCORM 1.2/2004 + cmi5 + LTI 1.3) | — | ✅ Una | **MIT** | Proceso aparte, local | **`coursecode`** — **15 tools** y **`coursecode_build` con `format` como enum**: el empaquetado está detrás de MCP. Supera a `scorm-mcp-server` (3 tools), que queda como la opción mínima *offline* |
| **OneRoster** (estándar) | — | ✅ Una | **0BSD** | SDK + servidor MCP | `trilogy-group/oneroster-ts`, **132 tools medidas por protocolo** |
| **CASE** (estándar) | Apache-2.0 (OpenCASE) | 🔴 **Ninguna** | — | — | **Sigue siendo la mejor oportunidad: el servidor publica su propio OpenAPI 3** → **P60** |
| 🔴 **QTI** (estándar) | MIT (`qti3-*`, `instructure/qti`) · 🔴 **GPL-2.0-only lo desplegado** | 🔴 **Ninguna** | — | — | 🔵 **La segunda mejor oportunidad, y ahora medida: `qti3-cli` tiene 14 comandos que emiten JSON y cero dependencias** → **gap 70**, **P70** |
| 🔴 **xAPI / LRS** (estándar) | **Apache-2.0** del lado cliente | 🔴 Sólo `learnmcp-xapi` | — | — | ⚠️ Clientes permisivos **pero congelados** (`TinCanPHP` 2019, `TinCanPython` 2020, `php-xapi/*` 2021) |

### 🔵 Lo que cambia en una conversación con cliente, en tres frases

1. **«¿Hay que construir el conector?»** — Para **Canvas y Moodle, no**: hay nueve puertas entre las dos y ocho son
   permisivas. Lo que se cotiza es **elegir, auditar y mantener**, no escribir.
2. 🔵 **«¿Y si TI no nos habilita nada?»** — Es la pregunta que frenaba todos los pilotos de esta KB, y ahora tiene
   respuesta de arquitectura: **`bunizao/moodle-cli` y `moon0825/jbnu-lms-student` trabajan desde la sesión del navegador
   del propio usuario** —passkey y segundo factor incluidos—, así que **el piloto no depende de un token institucional**.
   ⚠️ **Y su límite es el mismo que su virtud: son de sólo lectura / lado alumno.** Sirven para demostrar valor, no para
   cerrar el circuito de calificación.
3. ⚠️ **«¿El estándar tiene puerta?»** — **OneRoster sí, el empaquetado sí, CASE no, QTI no, xAPI casi no.** Y la frase
   *«CaSS tiene puerta MCP»* 🔴 **es cierta del servidor y falsa del SDK npm** (`cassproject` 5.0.19: cero menciones de
   MCP). Quien integre por npm **no hereda la puerta**.

### 🟢 Capa de evaluación conforme a estándar: lo que se propone cambió, y no por novedad sino por medición

**Antes de este pase esta KB proponía QTI sin saber qué estaba desplegado.** Medido en Packagist y npm:

- 🔴 **Lo instalado en el cliente institucional grande es TAO, y es GPL-2.0-only.** `oat-sa/extension-tao-testqti`:
  **117.544 descargas, 844 versiones, release del 2026-09-30**, con **8 estrellas**. `qtism/qtism` (`oat-sa/qti-sdk`):
  **218.212 descargas, 293 versiones**. ⚠️ **No van a un entregable cerrado** — y hay que **preguntar en el *discovery*
  si ya está adentro**, porque cambia el punto de partida.
- ✅ **Lo proponible es MIT y es nuevo:** `@longsightgroup/qti3-*` (QTI 3, 0.13.1 del **2026-10-01**) e
  `instructure/qti` (QTI 1.2). **Declarar la madurez por delante.**
- 🟢 **Y aparece una vertical que esta KB no tenía: la prueba de accesibilidad del ítem de evaluación.**
  `@longsightgroup/qti3-a11y` entrega **`accessibilityProofMatrix`** y **guiones manuales para VoiceOver, NVDA y JAWS**,
  y `@longsightgroup/qti3-pnp` resuelve **Personal Needs and Preferences** contra las capacidades del *player*. **Las dos
  son MIT.** Es la primera vez que esta base puede proponer **accesibilidad de evaluación como entregable auditable y
  permisivo** → **P72**.

⚠️ **El límite de `qti3-pnp`, textual del README, porque es el presupuesto del integrador:** *«It does not fetch, store,
authorize, or transmit PNP records. LMS identity, consent, institutional policy, persistence, LTI launch handling, and
AfA PNP service access belong outside this package.»*

## 🔴 La columna de la puerta de agente se cierra: **Open edX ya la tiene, es oficial, y es AGPL en proceso** — pase 30 del 2026-10-02

**El pase 27 agregó la columna «¿la vertical tiene puerta de agente?» y dejó a Open edX como el único «no» entre las LMS
grandes. Ese «no» caducó, y lo caducó el propio proyecto.**

| Vertical | Licencia de la plataforma | ¿Puerta de agente? | Licencia de la puerta | Arquitectura de la puerta |
|---|---|---|---|---|
| **Moodle** | GPL-3.0 | ✅ Sí, **dos** | **MIT** (ambas) | **Proceso aparte**, habla Web Services por token |
| **Canvas** | AGPL-3.0 | ✅ Sí | **MIT** | **Proceso aparte**, habla REST |
| **Open edX** | AGPL-3.0 | ✅ **Sí, desde el 2026-07-25 — y es oficial** | 🔴 **AGPL-3.0** | 🔴 **EN PROCESO: plugin Django dentro del LMS *y* del CMS** |
| **SCORM (formato)** | — | ✅ Sí | **MIT** | Proceso aparte, *offline* |
| **OneRoster (estándar)** | — | ✅ Sí | **0BSD** | SDK + servidor MCP, **132 tools medidas** |
| **CASE (estándar)** | Apache-2.0 (OpenCASE) | 🔴 **No** | — | **La mejor oportunidad que queda: el servidor publica su propio OpenAPI** → **P60** |

🔴 **Por qué esto es la corrección más consecuente del pase y no un cambio de celda.** La frase con la que el pase 27
organizó tres pases de trabajo era: *«las LMS son copyleft pero las puertas son MIT, y por eso se pueden componer»*. Esa
frase no describía una coincidencia de licencias: describía una **arquitectura**. Moodle y Canvas se pueden componer porque
sus puertas son **procesos separados** que hablan un protocolo, así que llevan su propia licencia y el copyleft del LMS no
las alcanza.

**La puerta de Open edX no es un proceso separado.** Es un plugin Django que se instala **dentro** de los procesos del LMS
y del CMS —tiene que ser así, porque la autoría toca el *modulestore*— y es **AGPL-3.0**. **No queda escotilla.** Para un
cliente que corre Open edX:

- ✅ **La puerta oficial es gratis, está mantenida por el proyecto y es más capaz que lo que esta KB iba a cotizar** (35
  endpoints, autoría incluida, y cuatro rails de seguridad de escritura que ningún conector MIT de esta base tiene).
- 🔴 **Entra con AGPL-3.0 en el núcleo de la plataforma.** Si el cliente ya corre Open edX, **ya está en AGPL**, así que
  para un despliegue interno esto normalmente **no agrega una restricción nueva** — y conviene decirlo así, sin
  dramatizar. **Donde sí importa es si el cliente pensaba ofrecer la plataforma como servicio a terceros con
  modificaciones propias**: ahí el artículo 13 del AGPL alcanza a la obra combinada y el análisis legal es obligatorio,
  no opcional.
- **Lo que queda para vender no es el conector.** Es: **criterio** (qué scopes se habilitan y cuáles no —`grant:admin` y
  `destructive` existen y son separables—), **endurecimiento** (la caché compartida que los rails necesitan en
  producción), **operación** y **la capa pedagógica arriba**. Ver **P61**.

⚠️ **Y el límite de esta fila, declarado:** es `0.1.x`, apunta a Open edX **Ulmo**, y **no se levantó una instancia**, así
que las 35 rutas son lectura del código del sdist y **no hay `tools/list` observado**.

### ✅ Dos nombres que esta vertical cierra, para no volver a encontrarlos en cada barrido

- **`.LRN` / dotLRN** — 🔴 **el pronóstico del pase 29 era el equivocado: está vivo**, y la medición de primera mano del
  árbol git da números que **también corrigen a la fuente secundaria**: `dotlrn.info` declara **dotLRN 2.10.1** con
  **`<release-date>2024-09-02</release-date>`** (la web decía «2.9.0 / 2.9.1»), `<maturity>2</maturity>`, vendor
  *DotLRN Consortium*, *«A Course Management System»*. **Dos años desde la última release: ni muerto ni activo, lento.**
  **Igual no se propone, y la razón alcanza sola:** ✅ **GPL-2.0 verificado en `license.txt`** (*«GNU GENERAL PUBLIC
  LICENSE Version 2, June 1991»*), **fuera del filtro permisivo**. Y su **VCS canónico es CVS**
  (`cvs.openacs.org`, `fisheye.openacs.org`), que es **por qué ningún barrido de GitHub lo devuelve**. El núcleo
  `openacs/openacs-core` es GPL-2.0, 50 ★, 19 forks, 7.600 commits, y 🔵 **su `acs-kernel.info` declara `6.0.0d2`** — una
  6.0 en desarrollo, así que el núcleo está **más vivo** que el «5.10.1» del README (5.10.1 es la versión que dotLRN
  *requiere*, no la del núcleo). ⚠️ **Y una corrección de este pase sobre sí mismo: el primer sondeo declaró el espejo git
  «sin contenido usable» porque pidió `README.md` y dio 404. Es falso** — es un paquete **APM** y su metadato vive en
  `dotlrn.info`, que responde 200 en cuatro refs. **«No hay README» no es «no hay repo».**
  ⚠️ `openacs.org` da **403 por el proxy**, así que nada de esto sale de su web.
- **`CK-ERP`** — ✅ **muerto**: última release **v0.31.1, abril de 2012**, en SourceForge, con conector para Drupal 7.12.
  Tenía módulos educativos reales (*Teacher, Counsellor, Student, Applicant, Family, Registrar, Edu Administration*), que
  es exactamente lo que lo hace reaparecer en los barridos de «education ERP open source». **Anotado como muerto.**

### ⚠️ El barrido vertical de este pase: **séptimo pase consecutivo saturado**

`open source platform education ERP CRM MIT Apache` devolvió **sólo plataformas ya inventariadas** —**OpenEduCat** (LGPL,
sobre Odoo), **ERPNext/Frappe**, Moodle, Sakai, Chamilo, Kolibri, openSIS, RosarioSIS, Fedena, Open edX, OpenOLAT— más el
único nombre nuevo, **CK-ERP**, que quedó declarado muerto arriba. **Cero altas de vertical por esta vía.**
🔵 **Lo nuevo de este pase no vino del barrido de verticales sino del de conectores y del código**, que es el quinto pase
consecutivo en que eso pasa. **La consecuencia de método ya es estable y conviene dejarla escrita: en educación la capa de
plataforma está inventariada y la capa que se mueve es la de la puerta.**


## La columna que faltaba en este archivo: ¿la vertical tiene puerta de agente? — agregada en el pase 27 del 2026-10-01

Veintiséis pasadas inventariaron **qué plataformas se pueden customizar**. Ninguna anotó **si existe ya la puerta por
la que entra el agente** — y es lo que decide si el proyecto empieza integrando o empieza construyendo el conector.
**El pase 27 la midió para las verticales de LMS**, y el resultado corrige la lectura del pase 26.

| Vertical | Plataforma | Licencia | Puerta MCP existente | Licencia de la puerta | Qué significa para un proyecto |
|---|---|---|---|---|---|
| **LMS** | **Moodle** | GPL-3.0+ | ✅ **Sí, dos permisivas** — `peancor/moodle-mcp-server`, `MarcosNahuel/moodle-mcp` | **MIT** ✅ | **Se empieza integrando.** Una de las dos **escribe nota y devolución**: ver **P54** |
| **LMS** | **Canvas** | AGPL-3.0 | ✅ Sí — `vishalsachdev/canvas-mcp` | **MIT** ✅ | La más madura de la capa |
| **LMS** | 🔴 **Open edX** | **AGPL-3.0** | 🔴 **No. Ninguna** | — | **Se empieza construyendo la puerta — y el pase 28 midió con qué.** La API **escribe matrícula y notas (con lote)**; el ***authoring* es experimental por declaración del proyecto**. Gap **48** (contestado) · **gap 50** · **P55** |
| **Contenido empaquetado** | **SCORM** (2004 4.ª ed. / 1.2) | estándar | ✅ Sí — `giacomomaria81/scorm-mcp-server` | **MIT** ✅ | **La vía sin integración:** el LMS importa, no se conecta. **P56** |
| **Rostering / SIS** | **OneRoster** (estándar 1EdTech) | estándar | ✅ **Sí — y el pase 28 lo encontró donde tres pases no miraron:** `trilogy-group/oneroster-ts` | **0BSD** ✅ | **164 métodos con escritura** sobre matrícula, clases, usuarios y resultados. **No es un conector: es un SDK que expone MCP.** **P59** |
| **Competencias** | **CaSS** | Apache-2.0 | ⚠️ **Parcial** — 6 operaciones de 61 | Apache-2.0 | Evidencia y perfil sí; **insignias y autoría de marcos no**. **P57** |
| **Biblioteca / ILS** | **FOLIO** | Apache-2.0 | 🔴 No, **pero publica eventos en Kafka** | — | El agente entra **como consumidor**, sin parchear el core. **P52** (pase 26) |
| **ERP / SIS** | **OpenEduCat** | LGPL-3.0 | 🔴 No | — | Módulo Odoo al lado; la LGPL lo admite (gap 46) |

🔴 **La asimetría que hay que leer antes de elegir plataforma en una propuesta.** Las tres LMS son copyleft —GPL o
AGPL— **pero las puertas son MIT**, y eso es lo que las vuelve utilizables: el conector es un proceso aparte que habla
por API con token, **no un derivado del LMS**. Es la misma forma que esta KB encontró en accesibilidad (pase 8) y en
credenciales (pase 9): **lo maduro es copyleft, lo que se compone es permisivo**. Y aplica en concreto: se puede
entregar un conector propietario sobre Moodle o Canvas **sin tocar la licencia del LMS**.

**Lo que esto cambia para el cliente que ya eligió plataforma.** Si corre **Moodle o Canvas**, el proyecto arranca en
la semana uno sobre una puerta existente. Si corre **Open edX** —y es el caso de la huella pública grande de **LATAM e
India**— **hay una fase previa que hay que cotizar**, y conviene decirlo al principio y no al medio. La alternativa que
evita esa fase por completo es **P56**: entregar el contenido como paquete SCORM, que Open edX importa igual que
cualquier LMS.

## Plataformas recomendadas

**12** plataformas reales verificadas (**ILIAS** entra en el pase 21), más **5** en la capa SIS (**Frappe Education** entra en el pase 23) y **1 en la capa de autograding agregada en el pase 5**: 3 de SIS se agregaron en la segunda pasada del 2026-09-30 y **GegoK12 en la tercera**. El equivalente educativo de "Odoo para ERP" es **Moodle**: dominante, extensible, y desde 2026 con subsistema AI nativo.

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
| **ILIAS** | GPL-3.0 | https://github.com/ILIAS-eLearning/ILIAS | PHP | LMS maduro de referencia en **DACH** (universidades y administración pública alemanas, suizas y austríacas); rama `release_11`, **76.385 commits**, 506 ★ / 426 forks | **Agregado en el pase 21.** Sin subsistema AI nativo comparable al de Moodle: se integra por LTI. 🔴 **Su propio Feature Wiki documenta el agujero de P40**: al borrar un objeto xAPI/cmi5, el dato personal de los *statements* **persiste en el LRS** y ILIAS *«no tiene forma de borrar datos en el LRS»* (⚠️ fuente secundaria: `docu.ilias.de` está bloqueado por el proxy) |
| **Richie** | MIT | https://github.com/openfun/richie | Python/Django | CMS de portal educativo: catálogo, marketing de cursos, SEO | MIT. Complementa un LMS; es la capa pública de descubrimiento |


## ⚠️ Moodle 5.x movió su *webroot* a `public/` — agregada en el pase 19 del 2026-10-01, y rompe toda referencia de ruta

**El dato operativo, verificado con un clon del árbol real (`main` = **Moodle 5.3rc1**, commit `85af0b5`):** en la serie
5.x **el código servido vive bajo `public/`**. La raíz del repo tiene `admin/`, `lib/`, `bin/`, `scripts/` y **`public/`**,
y es dentro de `public/` donde están `ai/`, `admin/tool/`, `mod/` y el resto.

| Serie | Ruta del subsistema de AI | Ruta del Privacy API |
|---|---|---|
| **4.5 / 5.0** | `ai/provider/...` | `admin/tool/dataprivacy/...` |
| **5.1+ (incl. 5.3)** | **`public/ai/provider/...`** | **`public/admin/tool/dataprivacy/...`** |

**Por qué está en este archivo y no sólo en una nota de método:** cualquier guía de despliegue, script de instalación,
`Dockerfile`, regla de *vhost* o documento de customización que esta KB produzca y que apunte a rutas de Moodle **tiene
que declarar contra qué serie se resolvió**. Una ruta correcta para 5.0 da 404 en 5.3. Esta KB ya pagó el costo: **dos
pasadas consecutivas (17 y 18) leyeron mal el mismo conjunto de 404** — la 17 como ausencia de la pieza, la 18 como
nombre de rama, y la causa era esta reestructuración. Ver la nota de método del pase 19 en `intel/trends.md`.

> **Y la herramienta correcta para la pregunta de la rama, que cuesta un segundo:** `git ls-remote --heads` **lista
> refs; no las infiere**. `moodle/moodle` **tiene** `refs/heads/main` (y no tiene `master`). Preguntarle a una página
> renderizada cuál es la rama por defecto es adivinar con buena suerte.

### Corrección de la fila de Moodle de la tabla de arriba — son siete proveedores de AI, y en 5.3 están todos en el núcleo

La fila dice *«Provider plugins para OpenAI, Azure OpenAI, Ollama, DeepSeek, Gemini y Amazon Bedrock»* (seis). En
**5.3rc1 son siete**, verificados sobre el árbol: **`anthropic`**, `awsbedrock`, `azureai`, `deepseek`, `gemini`,
`ollama`, `openai`. **`anthropic` es el que faltaba en el registro de esta KB.** Y los *placements* siguen siendo dos
(`courseassist`, `editor`).

### 🔴 Lo que hay que saber antes de prometerle a un cliente que «Moodle borra el dato de su AI»

Los **siete** proveedores traen `classes/privacy/provider.php`, y **los siete tienen todos sus métodos de borrado
vacíos** (70–78 líneas, cero `delete_records`, exactamente un `add_external_location_link`). **No es un defecto: es
correcto**, porque un proveedor no guarda nada localmente — **transmite**. Lo que borra es el subsistema:
**`public/ai/classes/privacy/provider.php`** (`core_ai`), ~800 líneas, **6 tablas** —`ai_policy_register`,
`ai_action_register` y las de `generate_text`, `generate_image`, `summarise_text`, `explain_text`, con **`prompt`** y
**`generatedcontent`** entre sus campos— y `delete_records_list()` real.

**La frase exacta que se le puede decir a un cliente:** *«Moodle borra el prompt y la respuesta que guardó en su propia
base. Lo que ya se envió al proveedor está fuera del alcance del Privacy API, y el propio núcleo lo declara así en los
siete plugins de proveedor.»* Ésa es la frontera, y conviene escribirla en el expediente (**P35**) en vez de descubrirla
en una auditoría. Ver la tendencia **48** y el patrón **P39**.

### 🔴 El eslabón de telemetría SÍ borra — matriz corregida en el pase 21, leyendo el código de los tres LRS

> **Esta matriz decía lo contrario hasta el pase 20, y era el dato más consultado de este archivo.** Se rehizo
> clonando los tres repos y leyendo el código fuente, no la documentación. **Dos de las tres filas cambian.**

| LRS | Licencia | ★ | ¿Borra? | Granularidad | Lo que hay que configurar o saber |
|---|---|---|---|---|---|
| **SQL LRS (`lrsql`)** | **Apache-2.0** ✅ | 144 | ✅ **Sí — el mejor de la capa** | **por `actor-ifi`** (el alumno), cascada sobre 7 tablas, transaccional | ⚠️ **viene apagado**: `LRSQL_ENABLE_ADMIN_DELETE_ACTOR=true`. El conteo que devuelve es el del **primer** `DELETE` y vale **`0`** para el alumno típico (**gap 36**, medido en el pase 24). 🔴 **En MariaDB/MySQL el borrado FALLA ENTERO** si una variable de entorno apagó `allowMultiQueries` (**gap 38**) |
| **Ralph** | **MIT** ✅ | 51 | ⚠️ **No en la API del LRS** | **por ID de statement**, vía *data backend* — hay que consultar primero | 🔴 **con backend ClickHouse es imposible**: declara `DELETE` como no soportado. Con Mongo o Elasticsearch, sí |
| **Learning Locker** | **GPL-3.0** ⚠️ | 585 | ✅ **Sí**, confirmado por código | **por filtro** de statements | ⚠️ código **congelado desde el 2021-11-16**; flag `ENABLE_STATEMENT_DELETION`; ventana UTC; **`done:true` no significa borrado** |

**Lo que sigue siendo cierto, y es lo único que hay que advertirle al cliente:** **el estándar xAPI / IEEE 9274.1.1 no
define una operación de supresión** — define *voiding*, que marca sin borrar. Así que **todo borrado de esta tabla es
extensión propia de cada implementación**: funciona, pero **no es portable entre LRS** y hay que escribirlo en el
contrato como dependencia de producto, no como conformidad con el estándar.

**Consecuencia para la elección de plataforma, que es lo que decide este archivo, y cambió de signo.** Si el proyecto
tiene obligación de supresión (art. 17 del GDPR, **AB 1159** operativa el 2027-07-01, Ley 21.719 chilena):
**elegir `lrsql` y encender el flag** — es la opción permisiva, la más granular y la única que borra por identidad del
alumno en una sola llamada. Lo que hay que cotizar **no es el borrado**, es el **expediente de evidencia** (gap 36) y
el **disparador desde el LMS** (**P40**), que sigue sin existir en ninguno de los tres. **Si el cliente pide
ClickHouse para analítica, el borrado deja de ser posible por esa vía** y hay que decidirlo antes de la arquitectura,
no después. Ver el **gap 33** (cerrado por refutación), el **gap 36** y **P44**.

## Capa SIS — el lado administrativo, verificado 2026-09-30 (pases 2 y 3)

Un LMS gestiona el aprendizaje; un **SIS** (Student Information System) gestiona la institución: matrícula, legajos, asistencia, notas oficiales, facturación, disciplina. Es donde viven los datos que más valen para un agente y el área que casi ningún piloto de AI toca.

| Plataforma | Licencia | URL | Stack | Cobertura | Nota |
|------------|----------|-----|-------|-----------|------|
| **GegoK12** | **MIT** ✅ | https://github.com/Gego-K12/gegok12 | PHP 8.4 + Laravel 12 | School management / ERP completo, API-first, mobile-ready. Instalador visual o Docker | 54 ★, 97 forks, 123 commits, **último commit 2026-09-23**. **El primer SIS open source permisivo y vivo que encuentra esta KB.** Tiene sistema de plugins real, no declarativo: el repo de ejemplo [`Plugin-Hello-Teacher`](https://github.com/Gego-K12/Plugin-Hello-Teacher) (MIT, PHP/Laravel) muestra service provider para registro del plugin, migraciones y seeding propios, controllers/models/vistas Blade, archivos de rutas separados para portal docente y admin, y **hook de menú para la navegación lateral**. Es decir: hay puntos de extensión de verdad, incluida la UI. ⚠️ Open-core: ver el detalle abajo — exámenes y fees son módulos Pro pagos |
| **OpenEduCat** | LGPL-3.0 | https://github.com/openeducat/openeducat_erp | Python (Odoo) | ERP educativo completo: admisiones, matrícula, asistencia, exámenes, biblioteca | La opción **más adoptada y más completa**, y la primera a proponer cuando el alcance incluye exámenes o cobranzas sin módulo pago: corre como módulos Odoo, así que hereda todo el ecosistema Odoo. LGPL-3.0 → el agente va afuera |
| **RosarioSIS** | GPL-2.0 ⚠️ | https://github.com/francoisjacquet/rosariosis | PHP | Legajos, notas, horarios, asistencia, facturación, disciplina, comedor | 644 ★. Modular y mantenido. GPL-2.0: copyleft, **no** es AGPL, así que no alcanza el uso en red |
| **openSIS Classic** | GPL ⚠️ | https://github.com/OS4ED/openSIS-Classic | PHP (Apache + MySQL) | K-12, escuelas técnicas y superior: datos de alumnos y staff, horarios, asistencia, notas, reportes | 343 ★. La Community Edition es GPL; OS4ED vende ediciones comerciales encima |
| **Frappe Education** | **GPL-3.0** ⚠️ (leída en `license.txt`, no en el README) | https://github.com/frappe/education | Python (Frappe Framework) | Gestión académica: alumnos y docentes, admisiones, programas y cursos, asistencia, cuotas, horarios y portal del alumno | 657 ★, 1.091 commits, rama `develop`. **Agregado en el pase 23: es la app que contesta la pregunta que el pase 21 dejó abierta sobre ERPNext** (ver abajo). Es una app *aparte*, no un módulo del core de ERPNext: se instala con `bench get-app education`. GPL-3.0 → el agente va afuera, igual que OpenEduCat y RosarioSIS |

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
| **SQL LRS (`lrsql`)** | **Apache-2.0** ✅ | https://github.com/yetanalytics/lrsql | Clojure sobre SQLite / PostgreSQL 14–18 / MariaDB / MySQL 8–9.5 | **El default para almacenar.** Corre sobre la base de datos que el cliente ya opera, así que no agrega una pieza nueva al diagrama. ⚠️ **Pero esa portabilidad no se extiende al cumplimiento:** ver la advertencia de abajo — en MariaDB/MySQL la supresión del alumno depende de un parámetro de driver (**gap 38**, pase 24) |
| **Ralph** | **MIT** ✅ | https://github.com/openfun/ralph | Python/FastAPI + Elasticsearch, Docker/K8s | Cuando el cliente está sobre **Open edX**: convierte los tracking logs a xAPI de fábrica. Mismo origen (OpenFun, Francia) que Richie |
| **Learning Locker** | GPL-3.0 ⚠️ | https://github.com/LearningLocker/learninglocker | Node.js + MongoDB | Rara vez por elección propia — pero es el más instalado de la categoría, así que es el que uno **se encuentra**. Copyleft: el servicio que lo modifique hereda la obligación |
| **ADL_LRS** | Apache-2.0 ✅ | https://github.com/adlnet/ADL_LRS | Python/Django | Sólo para **validar conformidad** con el estándar. El repo declara ser proof-of-concept para pocos usuarios: no proponerlo como almacén de producción |

**El par que hace la diferencia en una demo:** `lrsql` (o Ralph) + **`learnmcp-xapi`** (MIT, servidor MCP). Con esos dos, un agente de tutoría deja de tener memoria propia y empieza a escribir en el registro institucional — que es exactamente lo que pide un director académico cuando pregunta "¿y esto dónde queda guardado?". Wiring concreto en **P15**.

🟢 **Pase 33 del 2026-10-02 — las tres piezas de este bloque quedan fechadas, y eso cambia cómo se instalan (no cuál se elige):**

| Pieza | Último movimiento medido | Qué cambia en el despliegue |
|---|---|---|
| **`lrsql`** | 🟢 **`v0.9.9` el 2026-10-01**, **112 tags** en Docker Hub, seis releases en 2026 | Nada: **se confirma como el default de producción**, y ahora con cadencia medida en vez de supuesta. **Se instala por imagen de contenedor** |
| **Ralph** | ⚠️ Release PyPI **2024-07-11**; `[Unreleased]` grande y activo en `CHANGELOG.md` | 🔴 **Se instala desde `main` de git, no desde PyPI.** Sigue siendo la pieza correcta sobre Open edX y sigue siendo MIT, pero **el `pip install ralph-malph` trae código de hace ~2,2 años**. Decirlo en la estimación del *onboarding* |
| **Learning Locker** | 🔴 npm `modified` **2022-06-19** | Refuerza lo que ya decía esta fila: **es el que uno se encuentra, no el que uno elige.** Copyleft **y** congelado hace ~4,3 años |

🔵 **Y el canal de verificación que esto deja instalado:** `api.github.com` devuelve **403** en este entorno, así que para
una vertical que se distribuye **como contenedor** la fecha sale de
`hub.docker.com/v2/repositories/<org>/<imagen>/tags` (200, con `last_updated` por versión). Es el método que fechó
`lrsql` y sirve para cualquier otra vertical dockerizada de este archivo.

**Nota sobre ERPNext, con una corrección de matiz.** Las búsquedas de "ERP educativo open source" devuelven consistentemente **ERPNext** (https://github.com/frappe/erpnext) junto a OpenEduCat, y el material comercial de Frappe lo presenta *for education*. Verificado de primera mano en el repo: **GPL-3.0, 39,7k ★**. Cae del mismo lado que OpenEduCat y RosarioSIS — copyleft, el agente va afuera.

✅ **CERRADO EN EL PASE 23 (2026-10-01) — la sospecha del pase 21 era correcta, y ahora el repo tiene nombre.** El pase 21 dejó escrito que había que *«verificar primero en qué app vive el módulo»* porque *«la funcionalidad educativa de ERPNext fue históricamente una app aparte»*. **Lo es, y sigue siéndolo:** el módulo de gestión académica vive en **`frappe/education`** (https://github.com/frappe/education), una app independiente — **657 ★, 1.091 commits, Python, GPL-3.0 leída en `license.txt`** (la página del repo no muestra licencia: hay que abrir el archivo, que es exactamente la regla de método del pase 10). **El corte es la versión 14 de ERPNext:** hasta v13 *Education* era un *domain* del core; desde v14 se extrajo y hay que instalarla con `bench get-app education` + `bench --site <sitio> install-app education`. Por eso los foros de Frappe están llenos de «Education module missing in domain list v14» — no es un bug de instalación, es el split. **Consecuencia operativa para una propuesta:** proponer ERPNext *for education* implica **dos** artefactos (`erpnext` + `education`), los dos GPL-3.0, no uno; y el módulo académico tiene **657 ★ frente a los 39,7k de ERPNext**, así que la tracción del ERP **no se hereda** al módulo que al cliente le importa. Sigue sin desplazar a GegoK12 (MIT, el único permisivo) ni a OpenEduCat.

## 🔴 Capa de analítica de Open edX — agregada en el pase 22 del 2026-10-01, y cambia el supuesto de partida de la fila de Open edX

**Lo que esta KB suponía hasta acá:** que el LRS es una **elección de arquitectura** y que para un cliente Open edX
«se recomienda Ralph» (la fila de Ralph en la capa de telemetría, arriba). **Lo que este pase encontró:** para Open edX
no hay elección — **hay un stack de analítica oficial y trae el LRS puesto.**

| Pieza | Licencia | ★ | Commits | Qué instala / qué hace |
|---|---|---|---|---|
| **Aspects** · https://github.com/openedx/tutor-contrib-aspects | **Apache-2.0** ✅ | 14 | 2.269 | El plugin de analítica y reporting **oficial** de Open edX. Orquesta vía Tutor: **ClickHouse** + **Apache Superset** + **Ralph** (LRS) + **Vector** + **event-routing-backends** (xAPI) + **dbt** |
| **platform-plugin-aspects** · https://github.com/openedx/platform-plugin-aspects | **Apache-2.0** ✅ | 6 | 528 | Los *sinks* LMS/Studio → ClickHouse y los dashboards de Superset **embebidos en la interfaz del docente**. Trae el `UserRetirementSink` |

**El arbitraje de licencia, y es el que esta KB busca:** Open edX es **AGPL-3.0**, pero **su capa de analítica oficial
es Apache-2.0**. Lo que un estudio customiza —dashboards, métricas, modelos de datos, sinks— es **permisivo**; lo
copyleft es el sustrato que no se forkea. Misma receta que el resto de este archivo, ahora con una capa entera a favor.

### Lo que hay que levantar en el *discovery*, y es lo que cambió

1. **Si el cliente tiene Open edX con analítica, ya está en la configuración difícil de borrar.** El pase 21 declaró
   que **Ralph sobre ClickHouse** no puede ejecutar el borrado del alumno (**P44**), y lo planteó como un riesgo *«si
   el cliente eligió ese backend»*. **Aspects instala exactamente eso, de fábrica.** No fue una elección: es el
   default. Hay que preguntarlo en el discovery, no al llegar al expediente de privacidad.
2. **Pero el disparador de supresión existe, y en Moodle no.** `UserRetirementSink` **escucha la señal Django
   `USER_RETIRE_LMS_MISC` y borra la PII del usuario de ClickHouse** (verificado de primera mano en el README). El
   pase 19 probó que Moodle **no emite ningún evento** al aprobar un pedido de supresión —cero `trigger()` en los 187
   archivos de `tool_dataprivacy`—. **En esta dimensión Open edX está por delante de Moodle, y es Apache-2.0.**
3. ⚠️ **Y borra el nombre, no la conducta.** El sink borra las tablas de perfil (`user_profile`, `external_id`,
   `auth_user`, gobernadas por `ASPECTS_ENABLE_PII`) y **conserva el dato de eventos**, con el argumento de que queda
   **anonimizado**. Es el **gap 37**: un *statement* xAPI indexado por un `actor-ifi` estable es **pseudonimizado, no
   anónimo**, y eso bajo GDPR sigue siendo dato personal. **No prometer «derecho al olvido» sobre Open edX + Aspects
   sin haber leído qué pasa con el identificador del actor.**
4. **El control de privacidad tiene un camino documentado que lo sortea, y el parche no entró.** El **PR #1328** de
   `tutor-contrib-aspects` describe que el *job* manual de *backfill* volcaba `user_profile` / `external_id` a
   ClickHouse **aun con `ASPECTS_ENABLE_PII=False`**, *«sorteando exactamente la protección que ese setting existe para
   dar»*. 🔴 **Cerrado por su autor el 2026-09-16 sin mergear.** Si una propuesta se apoya en ese flag como control,
   **verificarlo contra la versión del cliente**.

**Y es el segundo proveedor que documenta el mismo límite por escrito.** El pase 21 registró que el Feature Wiki de
**ILIAS** declara que al borrar un objeto xAPI/cmi5 el dato personal **persiste en el LRS** y que ILIAS no tiene forma
de borrarlo (tendencia **55**). Con Aspects, la plataforma lo documenta **en su propia decisión de arquitectura**. Eso
es lo que vuelve el argumento defendible en una propuesta: **no es una carencia que invente esta KB, es la postura
escrita de los proveedores.** Ver **P45**.

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
| **LTI 1.3 en Java/Spring** | https://github.com/UOC/spring-boot-lti-advantage | **MIT** ✅ | LTI Advantage del lado *tool* para Spring Boot: valida los *launches* con Spring Security, y trae **AGS** (notas), **NRPS** (roster) y *Deep Linking* | **La alternativa cuando el cliente es Java y no PHP** — educación superior europea, típicamente. Agregado en el pase 24; antes esta KB sólo tenía la vía PHP y se la proponía por cobertura, no por criterio técnico. Hermana: `UOC/java-lti-1.3` (MIT, 21 ★) |
| **OneRoster para matrícula y notas** | https://github.com/LongsightGroup/oneroster | **MIT** ✅ | OneRoster 1.1/1.2 por CSV y REST, Node/Deno/navegador | Sincroniza alumnos, cursos, secciones y notas con el SIS sin integración a medida. 0 ★ — tratarlo como referencia y fijar la versión |


### 🔴 Antes de proponer `lrsql` con MariaDB o MySQL — agregado en el pase 24 del 2026-10-01

Esta KB recomienda `lrsql` como default desde el pase 18, con esta razón textual: *«corre sobre la base de datos que el
cliente ya opera»*. **Sigue siendo cierto para almacenar. Para borrar, en dos de los cuatro motores soportados, hay que
verificar una cosa antes de prometer nada** — medido en el pase 24 sobre MariaDB 10.11.14 + Connector/J 3.4.1:

| | |
|---|---|
| **El síntoma** | Con `allowMultiQueries` en el default del driver (`false`), `delete-actor-and-dependents!` **no se degrada: falla entera**, con error **1064 / SQLState 42000** en el segundo de los siete `DELETE` |
| **Por qué pasa** | lrsql trae el parámetro, pero como *fallback* de aero: `:db-properties #or [#env LRSQL_DB_PROPERTIES "allowMultiQueries=true"]`. El `#or` **no fusiona** — si el operador define `LRSQL_DB_PROPERTIES` por cualquier motivo, su string **reemplaza** al default y el parámetro desaparece. `LRSQL_DB_JDBC_URL` tiene el mismo efecto |
| **Por qué nadie lo nota** | El borrado de actor es **la única operación del producto** que manda varias sentencias en un paquete. Ingesta, consultas y documentos siguen funcionando: el despliegue pasa el *health check* |
| **Cuándo se nota** | **La primera vez que alguien ejerce el derecho al olvido** — o sea con expediente abierto y plazo corriendo |
| **La documentación juega en contra** | `doc/env_vars.md` la llama *«Optional **additional** DB properties»* con default *«Not set»* — **inexacto en los dos campos** para estos backends. Y `doc/postgres.md` enseña a usar esa misma variable para fijar `currentSchema` |

**Las tres preguntas de *discovery*, y son de cinco minutos:** ¿el backend es MariaDB/MySQL? ¿está definida
`LRSQL_DB_PROPERTIES`? ¿está definida `LRSQL_DB_JDBC_URL`? Si la primera es sí y alguna de las otras dos también,
**la supresión del alumno está apagada en ese despliegue y el cliente no lo sabe.** El arreglo es re-agregar
`allowMultiQueries=true` **al string del operador**, no en lugar de él. Ver el **paso 0 de P47** y la tendencia **62**.


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

## Capa de operación de privacidad sobre el LMS instalado — agregada en el pase 17 del 2026-10-01

La capa del pase 16 (privacidad y datos sintéticos) resuelve **cómo entrenar sin exponer**. Esta resuelve lo
anterior: **el dato del alumno ya está en el LMS, y el LMS ya tiene la máquina para gobernarlo.** Lo que no tiene
es operación, evidencia ni conexión con el agente.

### Las plataformas y lo que ya traen

| Plataforma | Licencia | Stars | Capacidad de privacidad instalada |
|---|---|---|---|
| **Moodle** — https://github.com/moodle/moodle | GPL-3.0 ⚠️ | 7.5k | **Privacy API en el núcleo**, que **obliga a los plugins** (incluidos los de terceros) a exportar y borrar. Más `tool_dataprivacy` (flujo de pedidos, delegado de protección de datos, período de retención) y `tool_policy` |
| **Open edX** — https://github.com/openedx/edx-platform | AGPL-3.0 ⚠️ | 8.2k | **User retirement**: 6 scripts + API REST de retiro masivo. Borra u ofusca PII a través de LMS, foros, credenciales y las demás IDAs, y puede alcanzar sistemas externos |
| **Canvas** — https://github.com/instructure/canvas-lms | AGPL-3.0 ⚠️ | 6.9k | ⚠️ **No verificado.** No se ubicó en abierto un toolset de retiro equivalente. Dimensionar como trabajo, no asumirlo como capacidad |
| **OpenEduCat** — https://github.com/openeducat/openeducat_erp | LGPL-3.0 ⚠️ | 881 | Autohospedado: **la institución es el responsable del dato**. Sin SaaS de terceros no hay acuerdo de terceros que negociar — el argumento FERPA más corto de esta KB |

### 🔴 El disparador comercial de esta capa no es la regulación: es la brecha de Canvas

Esta KB viene vendiendo capas de cumplimiento contra **fechas** —Artículo 50, Anexo III, COPPA—. Esta se vende
contra un **hecho ya ocurrido**, y es la primera así:

- **2026-04-29**: primer incidente en Instructure. **2026-05-07**: segundo, con cambios no autorizados en páginas
  de Canvas. Interrumpió clases y exámenes finales en EE. UU., incluidas varias **HBCU**.
- **ShinyHunters** reclamó ~**275 millones de registros** de alumnos, docentes y personal. Lo expuesto, según lo
  reportado: **nombres, correos, números de identificación de alumno y mensajes privados** de Canvas. **No** hay
  indicio de números de seguridad social, fechas de nacimiento ni contraseñas.
- Canvas sostiene ~**41 %** de las instituciones de educación superior del continente y **miles de distritos
  K-12**, lo que lo vuelve el incidente de mayor alcance que haya tocado al sector.
- **2026-05-11**: Instructure informó haber **llegado a un acuerdo con los atacantes** para que la información
  robada fuera devuelta y destruida, y declaró que recibió *«shred logs»* como prueba de borrado permanente.

⚠️ **Y cómo se usa este dato en una conversación con un cliente, porque usarlo mal es contraproducente.** No se
vende como «su proveedor es inseguro»: se vende como **la pregunta que el incidente dejó sin respuesta**. Un
acuerdo con el atacante y un log de borrado **no son verificables por la institución**: el responsable del dato
sigue siendo la institución, y no tiene forma propia de probar qué se exfiltró de *sus* alumnos ni qué se borró.
Lo vendible es la capacidad que la institución **no** tenía el 2026-04-29: saber qué dato de qué alumno vive en
qué sistema, poder exportarlo y poder borrarlo con evidencia. Eso es exactamente el Privacy API de Moodle y el
retiro de Open edX, operados.

### ⚠️ Lo que NO hay que proponer en esta capa

- **No prometer cumplimiento como producto.** Open edX lo dice por escrito: *«User retirement is not a compliance
  guarantee. The Open edX software makes no claim of satisfying any law or regulation.»* El cumplimiento es del
  operador del sitio. Vender «lo dejamos compliant» es vender algo que el propio proveedor del software niega.
  (Cita tomada de snippet de búsqueda; `docs.openedx.org` está bloqueado en esta sesión — resolver contra la
  fuente oficial antes de citarla a un cliente.)
- **No proponer un fork del LMS para agregar privacidad.** No hace falta y es el camino caro: Moodle se extiende
  con un plugin, Open edX se invoca. Un fork de AGPL-3.0 es el peor resultado posible de esta capa.
- **No asumir que Canvas tiene lo que tiene Open edX.** No se verificó. Si el cliente está en Canvas, el retiro
  es alcance a dimensionar.
- **No prometer borrado de lo que ya salió hacia un modelo.** Si el dato del alumno se usó para entrenar, el
  Privacy API del LMS no lo alcanza: borra el registro, no el modelo. Esa es la razón de P37 y del gap 30.

### La regla de esta capa, y es la que la hace defendible

**El entregable es configuración, evidencia y procedimiento — casi no es software.** Es más barato de construir
que un plugin, más difícil de copiar, y es lo único de esta capa que el cliente no puede bajar de GitHub. Para un
despliegue Moodle hay una excepción, y es obligatoria: **el plugin de AI que se entregue tiene que traer su
`privacy provider`**, porque el núcleo lo exige a todos los plugins. Esa línea va primera en el alcance.

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

## El subsistema de AI del LMS instalado y su postura de privacidad — agregado en el pase 18 del 2026-10-01

El pase 17 documentó que la máquina de privacidad del alumno ya está instalada en el LMS. Este pase verifica **qué
trae el núcleo del lado del subsistema de AI**, que es lo que decide el alcance de un engagement sobre Moodle.

### Moodle (GPL-3.0) — el subsistema de AI del núcleo trae tres proveedores, y los tres traen `privacy provider`

Verificado por código HTTP contra `raw.githubusercontent.com`, rama `MOODLE_500_STABLE` (y confirmado en
`MOODLE_405_STABLE` para OpenAI):

| Proveedor en el núcleo | ¿Está en el núcleo? | ¿`classes/privacy/provider.php`? |
|---|---|---|
| `aiprovider_openai` | ✅ | ✅ declara `prompttext`, `model`, `numberimages`, `responseformat` |
| `aiprovider_azureai` | ✅ | ✅ |
| `aiprovider_ollama` | ✅ | ✅ declara `prompttext`, `model` |
| `aiprovider_bedrock` | 🚫 **404** | — |
| `aiprovider_anthropic` | 🚫 **404** | — |

**Las dos consecuencias prácticas para una propuesta:**

1. **Si el cliente quiere OpenAI, Azure OpenAI u Ollama, el conector ya está en el núcleo** y ya viene con su
   declaración de privacidad. No se cotiza. Lo que se cotiza es la actividad pedagógica arriba.
2. **Si el cliente quiere Bedrock o Anthropic, el proveedor no está en el núcleo** y hay que traerlo de terceros o
   construirlo — **y entonces el `privacy provider` es alcance propio y obligatorio**, porque el núcleo lo exige a
   todo plugin. El patrón a copiar es `ai/provider/openai/classes/privacy/provider.php`, que es exactamente lo que
   hizo la Università di Ferrara para Gemini (ver `agents/top.md`).

🔴 **Y la línea de `aiprovider_ollama` que hay que leer antes de prometer «el dato no sale del cliente».** Aun el
proveedor local declara un envío externo, y su cadena de idioma dice: *«No user data is **explicitly** sent to
Ollama or stored in Moodle LMS by this plugin.»* El plugin no adjunta identidad; **`prompttext` sí viaja y el
prompt lleva lo que el alumno escribió**. La declaración del núcleo es **exacta sobre la identidad y silenciosa
sobre el contenido**, y acotar el contenido del prompt es responsabilidad de la actividad que lo construye — o
sea, del entregable. Esa frase va en el expediente de **P35**.

### La arquitectura que sí deja el dato adentro, y es BSD-2-Clause

`sngdtechnologies/ai-moodle-security` (**BSD-2-Clause**, 0 ★, 103 commits) no es un plugin y no tiene privacy
provider: es un **diagrama de despliegue** y vale por eso. Phi-3-mini vía Ollama **100% on-site**, 7 contenedores,
5 redes Docker, **sólo el proxy expuesto en 443**, Moodle y Ollama en redes internas **sin egreso a internet**,
Caddy + WAF Coraza (OWASP CRS). Es un prototipo de tesis de maestría, con lo que eso implica de continuidad —pero
es la referencia de red que vuelve verdadera, y no sólo declarada, la promesa de residencia del dato. Combina con
el argumento FERPA en los bordes que esta KB ya hace para `openeducat_erp` autohospedado.

### La corrección sobre qué repo proponer

**`moodlehq/moodle-tool_dataprivacy` está archivado desde el 2020-09-24 y es read-only.** La funcionalidad **se
mudó al núcleo** (Moodle 3.3.8 / 3.4.5 / 3.5 y posteriores), y se verificó: `admin/tool/dataprivacy/version.php` y
`admin/tool/policy/version.php` dan **200** en `MOODLE_500_STABLE`. **No proponer el repo archivado como
dependencia.** La máquina de pedidos de acceso y borrado, el delegado de protección de datos y la política de
retención **ya están instalados** en cualquier Moodle soportado.

### Lo que sigue sin existir, por plataforma

- **Moodle** → el `privacy provider` ya tiene referencia (tres, en el núcleo). **Lo que falta es el disparador:**
  nada conecta un pedido de borrado aprobado con un reajuste del modelo de *mastery*. Es el **gap 32**.
- **Open edX** (AGPL-3.0) → los seis scripts de retiro y la API REST de retiro masivo existen (pase 17). **No
  tiene equivalente de `privacy provider` para un plugin de AI** porque no tiene un subsistema de AI en el núcleo
  comparable al de Moodle 4.5+. Tratarlo como alcance a dimensionar.
- **Canvas** (AGPL-3.0) → sigue **no verificado** un toolset de retiro equivalente. El pase 17 lo declaró no
  encontrado y este pase **no lo auditó tampoco**. Se mantiene como *no encontrado, no inexistente*.


## Capa de testing de conformidad sobre la vertical — agregada en el pase 20 del 2026-10-01

Todas las capas anteriores de este archivo responden *qué se despliega*. Ésta responde **con qué se prueba lo
desplegado**, que es lo que hacía falta para que los expedientes de `compose/patterns.md` (**P4**, **P10**, **P11**,
**P17**, **P39**) dejaran de ser un documento y pasaran a ser una corrida reproducible.

| Herramienta | Licencia | ★ | Qué prueba sobre la vertical | Cuándo se propone |
|---|---|---|---|---|
| https://github.com/aiverify-foundation/moonshot | **Apache-2.0** ✅ | 353 | *Benchmarking* + *red-teaming* del tutor: alucinación, contenido indeseable, **divulgación de datos** y vulnerabilidad adversaria | Es el *default* para un agente educativo. Informe HTML vía `moonshot-ui` |
| https://github.com/aiverify-foundation/moonshot-cicd | **Apache-2.0** ✅ | 14 | Lo mismo, **dentro del pipeline**: Docker + S3, corre en cada actualización de modelo | Cuando el cliente ya tiene CI y el tutor va a cambiar de modelo más de una vez |
| https://github.com/compl-ai/compl-ai | **Apache-2.0** ✅ | 211 | 29 benchmarks mapeados a **6 principios del EU AI Act** | **La pieza del expediente europeo.** Es la única de la capa con mapeo al AI Act |
| https://github.com/UKGovernmentBEIS/inspect_ai | **MIT** ✅ | 2.900 | Sustrato de evals (200+ pre-construidas), *model-graded*, multi-turno | Cuando hay que escribir una prueba pedagógica propia desde cero |
| https://github.com/aiverify-foundation/aiverify-developer-tools | **Apache-2.0** ✅ | 9 | Nada por sí mismo: es el **punto de extensión** para un plugin de test propio | Cuando el entregable incluye la prueba educativa que hoy no existe (gap 35) |

### ⚠️ Lo que NO hay que proponer en esta capa, y son cuatro errores fáciles

1. **No decir «certificamos».** `aiverify` declara por escrito que **no garantiza** que el sistema evaluado esté libre
   de riesgos o sesgos, ni que sea seguro. Lo que se entrega es **evidencia reproducible**, que es mucho — y no es un
   certificado.
2. **No mezclar Singapur con Europa.** El *Model AI Governance Framework for Agentic AI* de Singapur es **voluntario**:
   sin penalidad, sin registro, sin *enforcement*. El EU AI Act no. Moonshot es una **herramienta** válida en un
   proyecto europeo; no es **cumplimiento** europeo.
3. **No prometer un crosswalk que no existe.** AI Verify está mapeado a **NIST AI RMF** (oct-2023) y a **ISO/IEC
   42001:2023** (jun-2024). **Al EU AI Act no hay mapeo directo** — se llega indirecto por ISO 42001. Para el
   expediente europeo la pieza es **COMPL-AI**.
4. **No proponer `aiverify` para un tutor.** Evalúa modelos supervisados **tabulares y de imagen**. Un tutor LLM se
   prueba con **Moonshot**, **Inspect** o **COMPL-AI**. Confundirlos es prometer la herramienta equivocada en la
   primera reunión técnica.

### La regla de esta capa, en una línea

**Lo que falta no es herramienta: es cobertura educativa.** Los tres catálogos de la capa declaran su alcance por
dominio —**derecho, medicina y finanzas**— y **educación no está en ninguno**, mientras los benchmarks pedagógicos que
esta KB tiene desde el pase 4 (`EduBench` y `SafeTutors`, **MIT**) no están empaquetados como prueba de nada. Las dos
mitades son licencia-compatibles. Ver el **gap 35** y **P42**.

## Capa de plataforma estatal instrumentada — Singapur / SLS — agregada en el pase 20 del 2026-10-01

Esta KB nombró a Singapur **una vez en diecinueve pasadas** y de pasada ("el agente vive dentro del SLS"). Es poco,
porque el **Student Learning Space** del MOE es probablemente **el despliegue educativo de AI más instrumentado del
mundo**: no es un piloto ni un chatbot, son **ocho funciones de AI en producción nacional, seis de ellas usadas
directamente por el alumno**, curadas, alineadas al currículo y supervisadas por el docente.

| Función (SLS) | Sigla | Quién la usa | Alcance declarado |
|---|---|---|---|
| Adaptive Learning System | **ALS** | Alumno | **Matemática** (primaria superior y secundaria inferior) y **Geografía** (secundaria superior) |
| Learning Assistant | **LEA** | Alumno | Asistente de aprendizaje dentro de la plataforma |
| Feedback Assistant – Mathematics | **FA-Math** | Alumno | Devolución automática en matemática |
| Annotated Feedback Assistant | **AFA** | Alumno | Devolución anotada sobre el trabajo del alumno |
| Short Answer Feedback Assistant | **SAFA** | Alumno | Devolución sobre respuestas breves |
| Speech Evaluation Tool | **SET** | Alumno | **Evaluación del habla** |

⚠️ **Nivel de evidencia: fuentes secundarias concordantes, no el MOE.** `moe.gov.sg` y `learning.moe.edu.sg` están
**bloqueados por el proxy de egreso** de esta sesión. Los nombres y siglas de las seis funciones y el alcance de ALS
aparecen de forma coincidente en varias fuentes; **las otras dos de las ocho no quedaron nombradas**. Antes de usar
esta tabla en material de cliente hay que abrir la fuente del MOE.

### 🔴 Por qué esto importa para dos capas que esta KB declaró desabastecidas

- **La capa de lectura oral del pase 14.** Ese pase escribió que *la habilidad que más se evalúa en primaria en el
  mundo es la lectura oral y esta KB no tenía una sola pieza para medirla*. **Singapur la tiene desplegada a escala
  nacional (SET)** — propietaria y estatal, no open source, así que **no cierra la capa**. Lo que cambia es el
  argumento: deja de ser una apuesta y pasa a ser **una función que un sistema educativo nacional ya considera
  indispensable**. Eso se usa en una propuesta.
- **El gap 6 (grading), intacto desde el pase 2.** Tres de las seis funciones son **asistentes de devolución**
  (FA-Math, AFA, SAFA). El gap 6 dice que no hay *grading* open source con tracción y que hay que orquestar al
  incumbente propietario; Singapur confirma la demanda y **no aporta oferta open source**: lo construyó el Estado con
  GovTech, cerrado. **El gap 6 no se mueve.**

### La condición de arquitectura, que ya estaba escrita y ahora se entiende mejor

El requisito que esta KB registró —**el agente tiene que vivir adentro del SLS**— no es una preferencia de compra: es
coherente con una política de uso por nivel. Según las fuentes localizadas, **los alumnos de primaria inferior no usan
AI directamente**, y **desde 4.º grado (Primary 4)** el uso es *estructurado, limitado, en clase y bajo supervisión
docente*. Para un proyecto eso significa que **el producto SaaS suelto está descartado de entrada** y que el
entregable es un componente integrado con control de nivel y traza de supervisión. Es el mismo requisito que el
**trend 52** describe y que **P5** ya implementaba sin conocer su fundamento.

**Y conecta con el pase 16:** un *Speech Evaluation Tool* usado por menores es exactamente el caso que el pase 16
levantó —la voz de un menor como dato regulado—, resuelto por Singapur con **plataforma estatal + supervisión docente**
en vez de con consentimiento. Es una tercera vía que esta KB no tenía registrada.



## Capa de horarios institucionales (*timetabling*) — agregada en el pase 25 del 2026-10-01

**La plataforma de esta capa es UniTime, y es Apache-2.0.** Verificada de primera mano el 2026-10-01.

| Plataforma | Repo | Licencia | ★ | Forks | Stack | Qué resuelve en producción |
|---|---|---|---|---|---|---|
| **UniTime** | https://github.com/UniTime/unitime | **Apache-2.0** ✅ | **349** | **213** | Java | *«Comprehensive University Timetabling System»*: **horario de cursos y de exámenes**, *event management* con salas compartidas, **asignación de alumnos a clases individuales** y *scheduling* de docentes. **Sistema distribuido:** varios gestores departamentales coordinan y modifican un mismo horario |
| **horarios-escolares-manager** | https://github.com/manceras/horarios-escolares-manager | **MIT** ✅ | 0 | 0 | Python (FastAPI) + React/TS | Primaria: docentes, grupos, aulas y carga semanal, resuelto con **OR-Tools CP-SAT**. Instalador Windows y AppImage |

🔵 **Cómo se propone, en una línea:** para educación superior, **UniTime** es la base y es permisiva, así que el agente
puede vivir adentro; la capa AI que tiene sentido arriba **no es generar el horario** —CP-SAT y los *solvers* de UniTime
ya lo hacen mejor que un LLM— sino **traducir la restricción en lenguaje natural a restricción del modelo** («esta
docente no puede los viernes», «este laboratorio necesita 90 minutos seguidos») y **explicar por qué un horario no tiene
solución**, que es la pregunta que hoy nadie puede responder y consume semanas de secretaría académica.

⚠️ **Lo que NO hay que proponer en esta capa.** **FET** y **mFET**, los dos nombres históricos del *timetabling* escolar,
son **GPL/AGPL** — repiten la forma del segmento SIS que midió el pase 24. Y `horarios-escolares-manager` está declarado
**«Early foundation, not production-ready»** por sus propios autores y su interfaz es **sólo en español**: sirve como
referencia de modelado CP-SAT y para un piloto de primaria en España o LATAM, **no como base de un entregable**.

## Capa de aserción de competencias — agregada en el pase 25 del 2026-10-01

| Plataforma | Repo | Licencia | ★ | Forks | Qué hace que la capa CASE del pase 20 no hacía |
|---|---|---|---|---|---|
| **CaSS** (*Competency and Skills System*) | https://github.com/cassproject/CASS | **Apache-2.0** ✅ | **62** | **29** | **Registra aserciones de logro individual y computa el perfil del aprendiz.** Autoría de marcos con *crosswalks* e import/export en editor Vue.js. 2.123 commits. Cartuchos: **IMS CASE**, **xAPI**, CTDL-ASN, ASN, **Open Badges 2.0** y 🔵 **MCP** |

🔴 **Por qué entra como plataforma y no como librería.** La capa de publicación de competencias del pase 14 —`opensalt`,
`OpenCASE`, `compeito`, `conform-ed`— **hospeda y valida marcos**: responde *«¿existe esta competencia y está bien
formada?»*. **Ninguna de las cuatro responde «¿este alumno la alcanzó?»**, que es la pregunta que paga el proyecto. CaSS
responde las dos, es permisiva y es **la más traccionada de la capa**.

🔵 **Y es la primera plataforma de estándares de esta KB con puerta nativa de agente.** El cartucho **MCP** significa que
un tutor de la tabla de `agents/top.md` puede **leer el marco de competencias y escribir la aserción sin adaptador
escrito a mano**, y que la evidencia queda como aserción en un servidor de estándares en vez de como texto en un chat.
Ver **P48**.

## Capa de supervisión remota de exámenes (*proctoring*) — agregada en el pase 25 del 2026-10-01

🔴 **Esta capa se agrega para decir que NO hay qué proponer, y es la única capa de esta KB en esa condición.** Se barrió
entera —era la consigna del pase 24— y las cinco piezas que existen fallan todas el mismo filtro:

| Pieza | Licencia | ★ | Por qué no se propone |
|---|---|---|---|
| https://github.com/vardanagarwal/Proctoring-AI | **MIT** ✅ | **635** | 🔴 **Trampa de licencia.** Código MIT, pero el modelo de *facial landmarks* está **entrenado con datasets de uso no comercial**, según su propio README. Y es **proyecto de investigación/demo** |
| https://github.com/openedx/edx-proctoring | ⚠️ **AGPL-3.0** | 68 | Copyleft fuerte. Vivo, pero su README **no documenta qué backends soporta** |
| https://github.com/oat-sa/lib-lti1p3-core | ⚠️ **GPL-2.0** | 37 | **La única certificada en *LTI 1.3 Proctoring Services*** de toda la base — y es copyleft |
| https://github.com/sudosylabs/Proctor | ⚠️ **AGPL-3.0** | 0 | *«has not published a supported production release»*, dicho por el repo |
| https://github.com/kamlendras/OpenProctor | ⚠️ **AGPL-3.0** | 15 | 37 commits, sin releases |

**La conclusión de capa, y es doble:**
1. **No existe proctoring open source permisivo y productivo.** O AGPL/GPL —viral para un SaaS multicliente— o pesos no comerciales.
2. **Es, además, la capa que el regulador mira más de cerca:** el proctoring está nombrado **explícitamente en el Annex III del EU AI Act** como alto riesgo (aplicable **2027-12-02**), y Corea del Sur ya lo alcanza como *high-impact AI* desde el 2026-01-22.

🔵 **Qué se propone en su lugar, y es mejor negocio:** **integridad de examen sin AI de vigilancia** — banco de ítems con
variantes y aleatorización (`LongsightGroup/qti3`, MIT), entrega certificada (`amp-up-io/qti3-item-player`, MIT),
devolución de notas por **AGS** y evidencia de proceso en **xAPI**. Saca el entregable del Annex III y elimina la
discusión de licencia. Es el patrón **P49**, y el **gap 39** registra lo que falta para que exista la alternativa completa.

---
*Ver `compose/patterns.md` para las recetas concretas con repos y tiempos.*

## 📚 Biblioteca — ILS / OPAC (agregada en el pase 26 del 2026-10-01)

**La vertical que faltaba, y es de las que más datos tiene.** En una universidad, el sistema de biblioteca sabe qué
está leyendo realmente cada alumno — y veinticinco pasadas de esta KB no lo buscaron. Es la vertical clásica de
"partir de algo que ya funciona, que ya tiene los datos, y agregar la capa agéntica arriba", que es el modelo de este
archivo.

| Plataforma | Licencia | Señal | Cómo se le pone AI arriba |
|-----------|----------|-------|---------------------------|
| **FOLIO** (`folio-org/platform-complete`) | **Apache-2.0** ✅ | 3.096 commits, 27 forks, consorcio de bibliotecas universitarias | **La opción permisiva.** Plataforma **modular y multi-tenant** con **bus de eventos Kafka** en `mod-inventory`. La capa agéntica se engancha **como módulo y como consumidor de Kafka — sin parchear el core**. Es la forma que un agente necesita |
| **Koha** | ⚠️ **GPL-3.0+** | El ILS open source más adoptado y el primero de la categoría | **El caso más probable en un cliente instalado.** OPAC, circulación, catalogación, adquisiciones, seriadas, reservas, socios. La capa AI se construye **contra su interfaz**, y hay que leer la **GPL-3.0** antes de tocar el core |

**La regla de decisión, en una línea.** Cliente **con Koha instalado** → capa AI por fuera, contra la interfaz, con la
GPL leída. Cliente **eligiendo o migrando** → **FOLIO**, porque es Apache-2.0 **y** porque su arquitectura de módulos
+ Kafka es la única de esta vertical que admite un agente sin tocar el núcleo.

⚠️ **No aplicar el umbral de estrellas acá.** `platform-complete` tiene **15 ★** y `mod-inventory` **4 ★**, con 3.096 y
2.402 commits. **Es software de consorcio: las estrellas miden moda, los commits y las implantaciones miden vida.**
Mismo patrón que Apereo y `UniTime` en esta KB.

🔴 **Y el hueco, declarado: no existe ninguna pieza agéntica ni conector MCP de biblioteca.** Ni FOLIO ni Koha tienen
uno. FOLIO —que ya publica eventos en Kafka— es **el candidato más obvio de toda esta KB** para construirlo. Ver el
**gap 45** y el patrón **P52**.

## 🧾 Admisiones (agregada en el pase 26 🔴 para decir que no hay permisivo)

Se buscó por consigna del pase 26. **El resultado es un gap informado.**

| Plataforma | Licencia | Lectura |
|-----------|----------|---------|
| **OpenEduCat** | ⚠️ **LGPL-3.0** | Pipeline completo: consulta → solicitud online → verificación de documentos → entrevista → carta de oferta → alta en el SIS. Self-hosted, **sin fee por postulante**. Módulo **Odoo** |
| **openSIS Classic** (`OS4ED/openSIS-Classic`) | ⚠️ **GPL** | SIS de K-12/trade/superior con la admisión adentro. Requiere Apache 2.4+ |
| https://github.com/CollinsTatang/admissionSystem | **MIT** | **Permisivo, sí — y tiene 4 commits, 6 ★, 0 forks.** PHP/MySQL, verificado de primera mano. No es base de producción |

🔴 **No hay plataforma de admisiones permisiva y productiva.** **La salida practicable es LGPL-3.0 sobre OpenEduCat**, y
para un módulo Odoo eso es manejable: la **LGPL permite el módulo propietario al lado** sin contaminar, que es
exactamente la forma en que se entrega un módulo Odoo. Es la recomendación de este archivo para la vertical. La
alternativa es presupuestar **desarrollo**. Ver el **gap 46**.

## 🎓 *Student success* / alumni (agregada en el pase 26 🔴 y es la peor abastecida de esta KB)

| Plataforma | Licencia | Estado real |
|-----------|----------|-------------|
| **FlightPath Academics** | ⚠️ **GPLv3+** | Asesoría académica, *degree audit*, *student success*, ***early alerts*** y *Academic Priority* para alumnos en riesgo. PHP. Liberada el **2013-03-13** (University of Louisiana at Monroe). 🔴 **Sin repositorio en GitHub** — se distribuye desde su sitio |
| **Student Success Plan (SSP)** | open source (Unicon) | *Case management* + *early alert* con modelo de coaching. **Referencias verificables sólo de 2013–2014** |
| **Marist College early alert dashboard** | open source | Open Academic Analytics Initiative, Educause NGLC. **Misma época** |

🔴 **La lectura incómoda, y es doble.** Esta vertical es **la más vieja y peor abastecida** de las que inventarió esta
KB: lo que existe es de **2013–2014**, es **GPL**, y **no vive en GitHub**. Y es, al mismo tiempo, **la que tiene más
presión regulatoria encima**: predecir qué alumno va a fracasar es precisamente la decisión automatizada sobre el alumno
que el **Annex III** del EU AI Act clasifica de alto riesgo y que **Oklahoma y Maryland prohíben** tomar de forma
autónoma (ver `intel/market.md`). **Hueco de mercado grande y riesgo regulatorio alto en la misma celda** — que es
justamente el perfil donde un *studio* agrega valor, porque el entregable que se puede defender no es el modelo
predictivo sino el flujo **con humano decidiendo**. Ver el **gap 47**, la tendencia **68** y el patrón **P53**.

## 🧩 Infraestructura de estándares de competencias, desplegable como vertical — agregada en el pase 29 del 2026-10-01

**Esta KB venía tratando a CASE como un estándar y no como una vertical, y eso ocultaba que hay una plataforma entera,
permisiva y desplegable con un comando.**

| Plataforma | Repo | Licencia | ★ | Qué es | Por qué entra como vertical y no como estándar |
|---|---|---|---|---|---|
| **OpenCASE** | [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) | **Apache-2.0** ✅ | 9 | Servidor de publicación de marcos de competencias (**CASE 1.0 y 1.1**, *CASE Provider API* oficial) **+ editor visual de marcos + identidad multi-tenant (Keycloak) + reverse proxy**, todo en Docker con **un solo comando** y HTTPS automático | **No es una librería: es un producto operable.** Tiene usuarios con roles (*Viewer*/*Author*/*Tenant Administrator*/*System Administrator*), tenencia múltiple, auditoría y una UI de autoría. **Es customizable con AI arriba, que es el criterio de esta sección** |

**Qué se customiza arriba, concretamente:**

- **Autoría asistida de marcos.** El editor publica al servidor por REST; un agente puede proponer items y asociaciones
  (*is child of*, *is related to*, *precedes*) y dejar que el humano las acepte en el canvas. 🔵 **El versionado es
  inmutable y por archivos**, así que **cada propuesta del agente queda como una versión auditable** sin construir nada:
  la compuerta humana y el registro de evidencia que esta KB pide en **P49** y **P54** vienen de fábrica.
- **Alineación de contenido a estándar.** Es el caso de uso que el propio 1EdTech pone adelante: conectar recursos
  digitales con los estándares que les aplican. Con los marcos en una API consultable, eso es un agente de
  *tagging* con verificación contra una fuente, no una clasificación a ciegas.
- **Importación de marcos existentes.** Hay superficie para eso (`cge/import`, `cge/subscriptions`, `cge/credentials`),
  así que el currículo de un ministerio no hay que tipearlo.

⚠️ **Lo que no se promete todavía:** **no se levantó una instancia en este pase** y **las rutas exactas están en
contradicción entre dos documentos del repo** (**gap 52**). La plataforma se propone; el número de semanas del conector
se cotiza después de resolver eso. Ver **P60**.

🔴 **Y el dato de madurez, dicho de frente: 9 ★ y 180 commits.** Es un proyecto del organismo de estándares, no de una
comunidad grande. **Apache-2.0 permite fijar un fork**, y para un entregable de cliente es lo que corresponde hacer.

### ⚠️ El barrido de verticales de este pase salió vacío, y se escribe porque el silencio se confunde con cobertura

`open source platform education ERP CRM MIT Apache` + variantes de SIS/LMS devolvió **únicamente plataformas que esta KB
ya tiene inventariadas**: **OpenEduCat** (LGPL, sobre Odoo), **ERPNext/Frappe**, **Moodle**, **RosarioSIS**, **Sakai**,
**Chamilo**, **Kolibri**, **openSIS**, **Fedena**, **Open edX** y **OpenOLAT**. **Cero altas por esta vía — sexto pase
consecutivo en que la capa vertical está saturada.**

**Un solo nombre apareció que no está en esta base: `.LRN` / dotLRN**, LMS nacido en el **MIT** sobre **OpenACS**.
🔴 **No se verificó en este pase y por lo tanto no se cita ante un cliente**: la señal disponible sugiere un proyecto de
los 2000 y hay que medir si está vivo antes de proponerlo. **Es la acción 3 del pase 30**, y la razón de anotarlo es
que, si está muerto, conviene declararlo muerto una vez y dejar de encontrarlo en cada barrido.

## 🟡 La puerta de agente de Open edX, medida: authorea todo **adentro** del curso — 🟢 **y el «no crea el curso» quedó refutado en el pase 32** — pase 31 del 2026-10-02

El pase 30 cerró la columna *«¿la vertical tiene puerta de agente?»* para Open edX: **la tiene, es oficial y es
AGPL-3.0**. Este pase la **midió desde el artefacto publicado** (el wheel de PyPI `openedx_mcp-0.1.5`, 46.685 bytes,
subido 2026-07-25) y midió además **las cinco versiones del API REST** por `raw.githubusercontent.com`. Lo que cambia
para quien cotiza un proyecto sobre Open edX:

| Pregunta de cotización | Respuesta medida |
|---|---|
| ¿El agente puede crear contenido? | **Sí.** 7 rutas CMS en el conector: `outline`, `courses/settings/`, `blocks/create/`, **`blocks/create-tree/`**, `blocks/update/`, `blocks/publish/`, `blocks/delete/` |
| ¿Puede crear secciones, subsecciones y unidades? | **Sí, y en una llamada.** `blocks/create-tree/` crea **un árbol**; por REST crudo el `XblockSerializer` acepta `parent_locator` + `category` (`chapter` / `sequential` / `vertical` / componente) |
| ¿Puede crear **el curso**? | 🔴 **No.** Ninguna de las **19 escrituras** del conector ni ninguna de las **cinco** versiones REST (`v0`–`v4`) crea un curso. El único primitivo de nivel curso es **`course_rerun`** (clona uno existente) |
| ¿Puede matricular, calificar, emitir certificados? | **Sí.** `WRITE_ENROLLMENT` (3), `WRITE_CERTIFICATES` (3), `WRITE_ROLES` (2), `WRITE_USERS` (4), `WRITE_REPORTS` (1), `WRITE_COURSES` (6) |
| ¿Qué licencia asume el cliente? | ⚠️ **AGPL-3.0**, leída del `LICENSE` dentro del wheel. El conector **corre en proceso** como plugin Django: no hay frontera de proceso que aísle la obligación |
| ¿Trae frenos propios? | **Parcialmente: 11 de 19 escrituras piden *confirm token*, 8 no.** Ver abajo |

### 🔴 El freno existe y es asimétrico: protege contra la operación masiva, no contra la repetida

| Escriben **sin** confirmación (8) | Piden confirmación (11) |
|---|---|
| `create_xblock` (×2), `update_xblock`, `update_course_settings`, `enroll_user`, **`unenroll_user`**, `generate_certificate`, `submit_report` | `bulk_enroll`, `create_user`, `deactivate_user`, `delete_xblock`, `instructor_access`, `invalidate_certificate`, `publish_xblock`, `regenerate_certificates`, `request_retirement`, `reset_attempts`, `set_role` |

`bulk_enroll` pide token; **`unenroll_user` de a uno, no**. Un agente en bucle no desmatricula un curso entero en una
llamada **y sí puede desmatricular 500 alumnos en 500 llamadas sin un solo token**. La asimetría es deliberada —está en
el decorador `@audited_write`— y **es una condición de despliegue que el proyecto tiene que cubrir afuera del
conector**: cuota por sujeto y por ventana, no sólo por operación. Ver **P63**.

### 🔵 Y el primitivo que cambia la economía del mantenimiento: *upstream/downstream*

`v2` del API de contentstore expone `downstreams/` con cuatro vistas, incluida
**`downstreams/<usage_key>/sync` (`SyncFromUpstreamView`)**: contenido que vive en una biblioteca y se **propaga** a los
cursos que lo consumen. **Un agente que mantiene material en 40 cursos edita una vez y sincroniza**, en vez de editar
40. ⚠️ **El conector MCP no expone esta capa** —no está entre sus 7 rutas CMS—, así que hoy se alcanza por REST directo
(**gap 59**).

**Consecuencia para la fila de Open edX en la tabla de arriba:** el supuesto de partida pasa de *«LMS con la huella
pública más grande de LATAM e India y sin puerta de agente»* a *«LMS con puerta oficial, copyleft, que authorea todo
menos la cáscara del curso»*. **Es cotizable entero** con un bootstrap declarado — curso plantilla + `course_rerun`
(**gap 57**: falta confirmar que `course_rerun` acepta un plantilla vacío como origen).


## 🟢 Corrección del pase 32 (2026-10-02): Open edX **sí crea cursos por HTTP**, y la fila de arriba hay que leerla con esto

La tabla de la sección anterior dice, en la fila *«¿Puede crear **el curso**?»*: **🔴 No**. **Esa respuesta era correcta
sobre lo que midió y falsa sobre lo que concluyó**, y la corrección cambia una cotización, así que va acá y no en una nota
al pie.

Lo que el pase 31 midió fueron **las 19 escrituras del conector MCP** y **los cinco árboles REST `v0`–`v4`**. Ninguno de
los dos crea cursos, y eso sigue siendo cierto. Pero **el árbol REST versionado no es toda la superficie HTTP de
Studio**: la creación vive en la vista **legacy**, leída de primera mano sobre `master` el 2026-10-02.

| Pregunta de cotización | Respuesta corregida (pase 32) |
|---|---|
| ¿Puede crear **el curso**? | 🟢 **Sí.** `POST /course/` con `Accept: application/json` → `_create_or_rerun_course` (`cms/djangoapps/contentstore/views/course.py:342` → **:1184**). **Sin `source_course_key` crea de cero** (`create_new_course`); **con `source_course_key` clona** (`rerun_course`) |
| ¿Hace falta un curso plantilla creado a mano? | 🟢 **No.** Era el *bootstrap* que **P63** cotizaba como tarea manual de una vez. **Se elimina del presupuesto** |
| ¿Qué permiso pide? | 🟢 **`is_content_creator(user, org)`** — **no `GlobalStaff`**. Para multi-tenant es decisivo: **el alta se delega por organización**. `GlobalStaff` sólo gatea las dos vistas **GET** de formulario (`CourseRerunView` REST `v1` y `course_rerun_handler`), que **no escriben** |
| ¿Es sincrónico? | ⚠️ **Mitad y mitad.** La **clave** vuelve en la respuesta; el **copiado** del clon va a **Celery** (`rerun_course_task.delay`, **:1375**) y se sigue por **`CourseRerunState`** (`FAILED`/`SUCCEEDED`). Hay que **pollear antes de escribir** en el curso nuevo |
| ¿Trampas? | 🔴 `rerun_course` lee **`fields['display_name']`** sin guarda (**:1359**) y `_create_or_rerun_course` sólo la puebla `if display_name is not None` → **omitirlo al clonar levanta `KeyError`**. El clon **resetea** `advertised_start`, `enrollment_start`, `enrollment_end`, `video_upload_pipeline`, y **`add_instructor`** deja de instructor a quien clonó |

🔵 **La lección que esta sección se lleva, y aplica a cualquier vertical de esta KB:** **la columna «¿tiene puerta de
agente?» no se contesta midiendo sólo el conector y el API versionado.** Un proyecto con años encima suele tener la
escritura en el handler viejo. Ver la **tendencia 95**.

🟢 **Y el `gap 59` de la sección anterior queda cerrado, también a favor:** `SyncFromUpstreamView` **preserva las
personalizaciones del docente por omisión** (`override_customizations` = `False`, con `keep_custom_fields` para
granularidad), y `downstreams/` tiene **cuatro escrituras**, no una —incluido **`DELETE .../sync` para que el docente
rechace** la actualización—. ⚠️ Con dos caveats que van en la propuesta: las cuatro clases están rotuladas
**`[ 🛑 UNSTABLE ]`**, y en bloques **`video`** el `sync` llama **`clear_transcripts` antes de copiar**, de modo que **si el
upstream no trae transcripciones, se pierden** — y eso es accesibilidad, no cosmética. Ver **P65**.

## 🧾 El barrido de ERP/CRM del pase 32, y lo que confirma (2026-10-02)

La búsqueda obligatoria `open source platform education ERP CRM MIT Apache` volvió a devolver, por séptimo pase,
**plataformas que esta KB ya tiene inventariadas**: **OpenEduCat** (LGPL-3.0, sobre Odoo), **ERPNext** y **Frappe
Education** (GPL-3.0, leída en `license.txt`), **Moodle**, **Sakai**. **Es saturación medida, no falta de búsqueda**, y
conviene registrarla como tal.

La única pieza **no inventariada** que apareció, verificada el 2026-10-02:

| Plataforma | Repo | Licencia | ★ | Stack | Para qué sirve acá |
|---|---|---|---|---|---|
| **Apache OFBiz** | [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | **Apache-2.0** ✅ | 1.1k | Java (30.444 commits) | ERP/CRM/e-commerce/SCM **genérico**, no educativo. Entra como **sustrato administrativo permisivo** cuando el bloqueo del proyecto es la licencia del ERP, no la funcionalidad educativa |

⚠️ **Cómo hay que leer esto, para no vendérselo mal al cliente:** OFBiz **no es un SIS ni un LMS** y no trae admisiones,
*gradebook* ni asistencia. Lo que aporta es lo que a esta KB le faltaba en esa capa: **licencia Apache-2.0 con comunidad
grande**. El inventario educativo de la capa ERP sigue siendo **copyleft en su totalidad** (OpenEduCat LGPL, ERPNext y
Frappe GPL), así que la decisión real no cambia: **o se acepta el copyleft con el agente afuera** (como esta KB ya
escribió para RosarioSIS, openSIS y OpenEduCat), **o se construye sobre un sustrato permisivo genérico** —OFBiz— **y la
funcionalidad educativa se desarrolla**, que es más caro y hay que cotizarlo como tal. **No hay ERP educativo permisivo y
productivo: el gap sigue abierto después de siete barridos.**
