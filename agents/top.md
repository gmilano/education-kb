---
industry: education
region: Global
updated: 2026-10-02
---

# 🎯 Agentes AI — education

> Agentes y herramientas AI open source para educación. Foco: MIT / Apache 2.0 / BSD.
> Verificado repo por repo vía WebFetch el 2026-09-30 (stars y licencia leídos de la página del repo).
> **Pase 25 del 2026-10-01:** **la tabla sigue en 37 filas — séptimo pase consecutivo sin altas**, y el barrido completo
> obligatorio (cuatro búsquedas globales + cuatro regionales, con el año **calculado**) devolvió por tercera vez la capa
> genérica y el material didáctico *sobre* AI. **El hallazgo de agente del pase no es un agente: es una puerta.**
> `cassproject/CASS` (**Apache-2.0**, 62 ★) expone **MCP** entre sus cartuchos — **la primera pieza de estándar educativo
> de esta KB con puerta nativa de agente**, y la que además hace las **aserciones** de competencia que las cuatro piezas
> CASE de esta base no hacían. Ver la tendencia **65**, el patrón **P48** y el **gap 40** (está declarado, no medido).
> **Pase 26 del 2026-10-01:** **la tabla pasa a 38 filas — se corta la racha de siete pases sin altas**, y se corta
> por donde el pase 25 dijo que había que buscar: **el conector, no el agente.** Entra `vishalsachdev/canvas-mcp`
> (**MIT**, 269 ★, 815 commits, **hasta 102–103 tools** + 8 *agent skills*), que es **el conector permisivo de LMS más
> grande que vio esta KB** y el primero que cubre el lado docente además del del alumno. Y el **gap 40 se cierra
> ejecutando**: el cartucho MCP de CaSS **genera 6 tools y 3 resource templates** medidos con el propio generador del
> proyecto — entre ellos `record_evidence` y `get_learner_profile`, que son **exactamente los dos pasos que el patrón
> P48 necesitaba**. Ver la tendencia **66**, el **gap 40 (CERRADO)** y la sección nueva de la capa conector, abajo.
> **Pase 10 del 2026-10-01:** para el contenido, la verificación se hizo contra el archivo `LICENSE`, no contra el README — y por eso apareció la contradicción que documenta la capa de contenido curricular, abajo.
> **Pase 27 del 2026-10-01:** **la tabla pasa de 38 a 41 filas**, y las tres altas son conectores: 🔴 **el pase 26 declaró que Moodle no tenía conector MCP permisivo (gap 43) y es falso** — hay **dos MIT**, y `peancor/moodle-mcp-server` **escribe nota y devolución** (`provide_assignment_feedback`), la primera pieza permisiva que toca el **gap 6** desde el pase 2. Entra también `scorm-mcp-server` (MIT, offline). El hueco real del eje conector **es Open edX**, el único LMS grande sin puerta de agente (**gap 48**). Y la superficie MCP de CaSS queda medida por adaptador: **CASE, CEASN y Open Badges están enteros fuera de MCP**, y el Open Badges de CaSS es **OB 2.0, no 3.0**. Ver la capa de conectores, abajo.

> **Pase 28 del 2026-10-01:** **la tabla pasa de 41 a 43 filas**, y la alta que importa **refuta otra ausencia declarada**: 🔴 **el pase 26 dijo que OneRoster no tenía conector MCP y es falso** — `trilogy-group/oneroster-ts` es **0BSD** (la primera licencia 0BSD de esta KB) y expone **164 métodos como MCP tools, con escritura**, que es **la superficie de herramientas más grande de toda esta base**. Y **la regla del pase 27 no habría alcanzado para encontrarlo**: el repo **no se llama `*-mcp`**, es un **SDK** que agrega MCP en una línea del README. **Cuarta corrección consecutiva por muestreo.** Entra también `paulocymbaum/ed-tech-system-mcp` (MIT, 18 tools, LangGraph, sin LMS). **QTI queda como la única ausencia medida por tres métodos** y **CASE queda sin medir por colisión de término** (cuarta de esta KB: `case` → *case study* / *use case*, **gap 51**). Ver la capa de conectores, abajo.
> **Pase 29 del 2026-10-01:** **la tabla pasa de 43 a 44 filas**, y el valor del pase no está en el alta sino en **dos ausencias que se dan vuelta leyendo el código**. 🔴 **El pase 28 concluyó que el *authoring* de Open edX está «declarado experimental» y que por eso había causa técnica para la ausencia del conector. Es falso, y la causa fue leer un solo archivo.** El aviso *«the Authoring API is still experimental… use the v0 versions»* vive en `v1/urls.py`, **está fechado «(Nov. 23)» y encabeza una sección vacía**; mientras tanto `v0/views/xblock.py` declara **lo contrario** —*«superseded by `XblockViewSet`… use `/api/contentstore/v1/xblock/` going forward»*— y **`v1/urls.py` registra efectivamente ese `XblockViewSet` con CRUD completo** (`create`/`retrieve`/`update`/`partial_update`/`destroy`) bajo un programa de ADRs con nombre (**FC-0118**). **Es una deprecación circular, y la señal nueva gana: la autoría es cotizable.** Ver el **gap 50 (REENCUADRADO)** y **P55**. ✅ **Y el gap 51 queda medido:** CASE **sí** tiene implementación de referencia permisiva —[`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE), **Apache-2.0**, 9 ★, 180 commits, CASE **1.0 y 1.1**— **y sigue sin conector MCP**, ahora por medición y no por colisión. 🔴 **La colisión número cinco de esta KB es de un tipo nuevo: el «MCP» que aparecía en la página de OpenCASE es el menú de GitHub** (*AI CODE CREATION → MCP Registry*), **no el repo** — el README crudo tiene **cero** menciones. **Regla nueva: la presencia de MCP se verifica en el README crudo, nunca en la página renderizada.** Ver las tendencias **78**, **79** y **80**, el **gap 51 (CERRADO)** y el patrón nuevo **P60**.

> **Pase 30 del 2026-10-02:** **la tabla pasa a 47 filas, y la alta más importante cierra la mejor oportunidad que tenía esta KB — en contra.** 🔴 **El gap 48 («Open edX es el único LMS grande sin puerta de agente») lo cerró el propio proyecto:** `openedx-mcp` + `tutor-contrib-openedxmcp`, publicados en PyPI el **2026-07-25**, los dos **AGPL-3.0**. **35 endpoints medidos leyendo el código del sdist** (28 LMS + 7 CMS), **con autoría incluida** —lo que confirma por implementación la refutación del pase 29— y con **cuatro rails contra «agente en bucle»** que son el artefacto más reutilizable que encontró esta base: *dry run* + **confirm token atado a una huella del payload**, rate limit por (key, tool), re-chequeo de autoridad vivo y **auditoría append-only previa a la escritura**. 🔴 **Pero rompe la tesis del pase 27:** esta puerta **corre en proceso** como plugin Django dentro del LMS y del CMS, así que *«las LMS son copyleft pero las puertas son MIT»* **deja de valer para Open edX**. Ver **P55 (reencuadrado)** y **P61**. ✅ **Y la acción 2 del pase 29 queda cumplida ejecutando el servidor:** `tools/list` de `oneroster-ts` devuelve **132 tools** (72 lectura / 60 escritura), y el «164» por fin se explica — **132 operaciones distintas + 32 alias cruzados**, **cero supresión**, el 100 % de lo que el SDK tiene. Entra además `asfai-education` (**Apache-2.0**), la primera pieza con **cinco estándares 1EdTech a la vez**. Ver las tendencias **81**–**87**, los **gaps 52 (CERRADO)**, **53 (medido y corregido)** y **54**–**56**.
> **Pase 32 del 2026-10-02:** **la tabla pasa a 48 filas, y el alta corta ocho pases sin agentes nuevos.** Entra [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) (**Apache-2.0**, 448 ★), que **destila el material de un docente en Agent Skills con trazabilidad a la fuente** — el eslabón que esta base declaraba vacío entre las skills escritas a mano y los tutores. El resto del pase es de **medición y de corrección**: 🔴 **el gap 57 cierra invirtiendo la conclusión del pase 31 — crear un curso en Open edX *sí* es una llamada HTTP** (`POST course_handler` → `_create_or_rerun_course`), **no vive en el árbol REST versionado** y pide **`is_content_creator(user, org)`, no `GlobalStaff`**; el *bootstrap* con curso plantilla de **P63** era innecesario. ✅ **El gap 59 cierra a favor:** el `sync` de biblioteca **preserva las personalizaciones del docente por omisión** (`override_customizations` = `False`). 🟢 **Aparece la primera puerta MCP de la capa de empaquetado:** `coursecode` (**MIT**, SCORM 1.2/2004 + cmi5 + LTI 1.3, **servidor MCP incorporado**) — y **apareció en el README, no en la descripción del paquete**, que es el canal que el barrido automático se saltea. 🔴 **Colisiones 5 y 6, las dos llamadas «xapi»:** `xapi-to` (cripto/Web3) y `xapi-python` (forex XTB) son **MIT y activas**, así que el filtro de licencia no las descarta. 🔴 **Y el gap 56 resuelve contra la propia argumentación EMEA de esta base:** educación es **Anexo III**, cuya fecha **se movió de 2026-08-02 a 2027-12-02**. Ver las tendencias **95**–**98** y los patrones **P65**–**P66**.
> **Pase 33 del 2026-10-02:** **la tabla se queda en 48 filas, y por una vez eso es el hallazgo: la pieza que este pase fue a buscar ya estaba acá.** 🔴 **La mitad xAPI del gap 60 es FALSA, y la refutación estaba en cuatro archivos de esta base:** `DavidLMS/learnmcp-xapi` (**MIT**, 3 tools — **1 escribe, 2 leen**) es la puerta MCP de xAPI, está en esta tabla **desde el pase 6** y el mapa por estándar de abajo lo dice con la frase *«desde el pase 6»* escrita al lado. **El pase 32 declaró ausente algo que esta KB listaba como presente.** ✅ **La mitad QTI, en cambio, se CONFIRMA por un segundo instrumento independiente** — y es la única ausencia de esta base medida por dos instrumentos (tendencia **101**). 🔴 **La causa está medida y es el instrumento, no el rigor:** `learnmcp-xapi` **no está en ningún registro de paquetes** (PyPI **404**, npm **`total: 0`**; se instala desde el código) y `lrsql` se distribuye por **Docker Hub**, así que un barrido que arma candidatos en npm/PyPI/Packagist **no puede verlas** (tendencia **99**). **Regla nueva y barata: antes de declarar una ausencia, `grep` sobre estos ocho archivos.** 🟢 **Lo nuevo del pase es el estado, que es lo que decide si una dependencia entra en una propuesta:** `lrsql` (**Apache-2.0**) publicó **`v0.9.9` el 2026-10-01 — ayer**, con **112 tags** y seis releases en 2026; **Ralph** (**MIT**, *«Copyright (c) 2020-present France Université Numérique»*) está **vivo en `main` y parado en el registro** (último release **2024-07-11**, `[Unreleased]` activo) → **se instala desde git, no desde PyPI**. ✅ **`coursecode` medido en el artefacto publicado: 15 tools definidas / 15 casos de dispatch, sin aliasing ni supresión, y DOS escriben** — `_build`, con **`enum: ['cmi5','scorm2004','scorm1.2','lti']` en el `inputSchema`** (los cuatro estándares dejan de ser prosa del README y pasan a ser **contrato de tool**), y `_narration`, que escribe MP3 llamando a un **TTS pago**. 🟢 **Y trae la primitiva del pase 30 reinventada por otro mecanismo, con una asimetría que hay que cotizar:** `openedx-mcp` frena **en el servidor** (confirm token) y `coursecode` frena **en el contrato** (anotaciones MCP + `dryRun`) — **sólo el primero frena solo** (tendencia **102**). ✅ **Gap 51 CERRADO en negativo, medido en tres registros:** `opencase` da **7 / 404 / 665** con **cero del dominio** (cajas de skins, `opencage`, `opencast`) y `cass` da **26.726** en Packagist; el instrumento que funciona es **el nombre de la organización** (tendencia **100**). ⚠️ **Y una corrección de atribución:** el `LICENSE` de `learnmcp-xapi` dice **`Copyright (c) 2025 David Romero`** —una persona—, no una institución; el argumento de soberanía europea de EMEA conviene apoyarlo en **Ralph**, cuyo titular institucional sí está en el archivo de licencia. Ver las tendencias **99**–**102**, los **gaps 62**–**64** y los patrones **P67**–**P69**.

## Agentes y herramientas destacadas

**47 filas contadas en el archivo** (**44 → 47 en el pase 30**: entran `openedx-mcp` y `tutor-contrib-openedxmcp` —los dos **AGPL-3.0**— y `asfai-education` —**Apache-2.0**). ⚠️ **Y se deja asentada la diferencia en vez de heredarla:** el encabezado anterior declaraba «43 filas» cuando el archivo tenía **44 filas de datos**. El conteo de este pase es **programático sobre el archivo** (filas entre el separador y la primera línea que no empieza con `|`), así que **47 es el número verificable**; «43» era el conteo a mano del pase 19. **Es la quinta vez que esta KB se pelea con este número y la primera en que se mide en vez de contarse.** (**41 → 43 en el pase 28**: entran `trilogy-group/oneroster-ts` — **0BSD** — y `paulocymbaum/ed-tech-system-mcp` — MIT.) (37 → 38 en el pase 26: entra `canvas-mcp`; **38 → 41 en el pase 27**: entran `peancor/moodle-mcp-server`, `MarcosNahuel/moodle-mcp` y `scorm-mcp-server` — las tres son **conectores MCP**, y las tres son **MIT**.) Ordenados por stars. El conteo se hizo a mano en el pase 19 y
se explica abajo, porque es la cuarta vez que esta KB se pelea con este número.

> *Pase 25 del 2026-10-01:* **séptimo pase sin altas, y el eje de búsqueda que el pase 23 diagnosticó sigue siendo el que
> rinde — pero rinde infraestructura, no agentes.** Se ejecutaron los siete ítems de la consigna del pase 24 (`item bank`,
> `proctoring`, `timetable`, `competency framework`/CASE, y los estándares Caliper, CASE y xAPI Profiles, más
> `LTI platform`): **18 repos verificados de primera mano, 17 nuevos para esta KB, y ninguno es un agente.** Van a `repos/foundations.md` y
> `verticals/solutions.md`. **La lectura, a esta altura, es estructural y conviene no repetirla como queja:** en educación
> el open source produce **capas de interoperabilidad, evaluación y administración**, y los **agentes** que se usan son los
> genéricos de la industria, customizados. Esta tabla de 37 filas es el inventario de lo que sí existe; el crecimiento de
> esta KB está en **cómo se componen**, no en cuántos hay. Ver **P48** y **P49**.

> *Pase 23 del 2026-10-01:* **la tabla sigue en 37 filas — quinto pase consecutivo sin altas, y este identificó la causa
> estructural en vez de volver a declarar el agotamiento.** Se corrió el barrido completo obligatorio (cuatro búsquedas
> globales + cuatro regionales, con el año **calculado**). Los dos repos nuevos del pase **no son agentes**:
> `frappe/education` (GPL-3.0, 657 ★) es plataforma y va a `verticals/solutions.md`, y `aureuserp` (MIT, 12k ★) **no tiene
> módulo educativo** y queda como no-hallazgo declarado en `repos/trending.md`.
> 🔴 **La causa, medida:** en GitHub el término **`education` está capturado por el material didáctico *sobre* AI**
> (`AI Agents for Beginners` y `AutoGen`, 56k ★ cada uno; cursos de DeepLearning.AI) **y no por software que educa**. Los dos
> sentidos comparten la palabra y el primero tiene **dos órdenes de magnitud más de estrellas**, así que sepulta al segundo en
> cualquier ranking. **La consigna para el próximo pase corrige la del 22:** no alcanza cambiar el sustantivo — hay que
> **evitar la palabra `education`** y buscar por el **artefacto del dominio** (`gradebook`, `rubric`, `item bank`,
> `enrolment`, `attendance`, `IEP`, `transcript`) o por el **estándar instalado** (QTI, OneRoster, xAPI, LTI), que es cómo
> aparecieron las capas de los pases 6, 9, 11 y 22. **Nota de método: no se agregó ninguna fila de relleno.** 37 filas reales
> siguen siendo mejores que 40 con tres dudosas.
> **El hallazgo del pase está en la capa de evidencia, no acá:** se ejecutó la acción que el pase 22 dejó escrita y el
> **gap 36 quedó dimensionado** — los conteos de borrado **existen** en los tres backends de `lrsql`, pero la evidencia
> **no es portable entre motores de base de datos**, lo que contradice la razón por la que esta KB recomienda `lrsql` por
> default. Ver la tendencia **60** y el patrón **P46**.

> *Pase 22 del 2026-10-01:* **la tabla sigue en 37 filas, y es el cuarto pase consecutivo sin altas — el primero que
> mide el agotamiento en vez de declararlo.** Se corrió el barrido completo (cuatro búsquedas globales + cuatro
> regionales) y **los dos únicos candidatos que trajo ya estaban acá, con más precisión que la fuente**: `OpenMAIC`
> (la web lo da como «v1.0.0, MIT» y omite que **se relicenció de AGPL-3.0 a MIT en v0.3.0 del 2026-06-28**) y
> `AITutor-EvalKit` (que esta KB ya corrigió en el pase 4: el repo canónico del mismo autor es
> `UnifyingAITutorEvaluation`, 32 ★). El detalle candidato por candidato está en `agents/trending.md`.
> **El hallazgo del pase está en la capa de infraestructura, no acá:** el stack de analítica **oficial** de Open edX
> (**Aspects**, Apache-2.0, 2.269 commits) instala **Ralph sobre ClickHouse** —la configuración que el pase 21 declaró
> imborrable, que resulta ser el **default de la plataforma** y no una elección del cliente— y a la vez **trae el
> disparador de supresión LMS → telemetría que el pase 19 probó inexistente en Moodle** (`UserRetirementSink`,
> escuchando la señal Django `USER_RETIRE_LMS_MISC`). Corrige una advertencia de **P44**, cambia el estado de **P40**
> y abre el **gap 37**. Además se **reconfirmó el gap 36 por lectura independiente del código de `lrsql`**, con el
> sitio exacto del parche (`interceptors/lrs_management.clj:23–33`) y con una sub-pregunta que quedó **sin contestar
> y declarada**, no inferida.

> *Pase 21 del 2026-10-01:* **la tabla principal sigue en 37 filas, y es el tercer pase consecutivo que no agrega
> agentes a propósito.** Este pase ejecutó la acción que el pase 19 dejó escrita como «la pregunta de mayor rendimiento»
> y que el pase 20 no tomó: **confirmar el borrado en la capa de telemetría (gap 33)**. Se ejecutó **clonando los tres
> LRS y leyendo el código fuente**, y 🔴 **el gap 33 se cierra refutado**: `lrsql` (**Apache-2.0**), el almacén que esta
> KB recomienda como default para **P1**, **P10**, **P14** y **P15**, expone `DELETE /admin/agents` —borrado **por
> `actor-ifi`**, en cascada sobre 7 tablas, transaccional— y **viene apagado de fábrica**. Durante catorce pasadas esta
> KB afirmó lo contrario **leyendo documentación en vez de código**, y tenía la nota de límite escrita al pie que lo
> advertía. Lo que queda abierto es la **evidencia** (**gap 36**, el más chico y upstreameable de esta KB) y el
> **disparador LMS→LRS** (**P40**), no la capacidad. Entra **ILIAS** a `verticals/solutions.md`, cuyo Feature Wiki
> documenta ese mismo agujero por escrito. Se reverificó **DeepTutor** de primera mano (**40.6k ★**, Apache-2.0,
> **v1.6.12** del 2026-09-27), coincidente con el pase 20. Ver las tendencias **54**, **55** y **56**, el **gap 36** y
> el patrón **P44**.

> *Pase 20 del 2026-10-01:* **no se agregó ninguna fila a la tabla principal — la tabla sigue teniendo 37 filas**, y
> eso es deliberado. Este pase no buscó tutores: buscó **la máquina que prueba que un tutor cumple**, que es lo que
> esta KB viene prometiendo en `P4`, `P10`, `P11`, `P17` y `P39` desde el pase 4 **sin tener registrada una sola
> herramienta de testing**. La máquina existe, es **Apache-2.0**, la publica **un regulador nacional** (IMDA de
> Singapur, vía la AI Verify Foundation) y trae *benchmarking* + *red-teaming* con un **Starter Kit v1.0 de enero de
> 2026** detrás. Y el hallazgo es lo que **no** tiene: su propio catálogo de evaluaciones cubre **derecho, medicina y
> finanzas — educación no está**. Se abre la **capa de testing de conformidad** al final de este archivo, se abre el
> **gap 35**, y entra **Singapur** a esta KB, que en diecinueve pasadas la nombró una sola vez y de pasada. Ver las
> tendencias **51**, **52** y **53** y los patrones **P42** y **P43**.

> *Conteo del pase 19, con la regla del pase 17 aplicada de forma consistente:* la tabla tiene **37 filas**. Dos no son
> agentes sino **bibliotecas de skills** — `education-agent-skills` (165 skills en 20 dominios) y **`human-skill-tree`**
> (33 skills, nuevo en este pase) —: son catálogos de pedagogía empaquetada, no un tutor. Las otras tres piezas nuevas
> entregadas como skill (**universal-examprep-skill**, **universal-diagnostic-tutor-skill**, **algo-sensei**) **sí** cuentan
> como agentes, por el mismo criterio con el que esta KB ya contaba a `Alvarmethod` y `Gnos`: cada una es **un** tutor
> coherente con su propio loop pedagógico, no un catálogo. **37 = 35 + 2.**
> *Pase 11 del 2026-10-01:* +3 en la tabla principal (**learn**, **Gnos**, **Alvarmethod**) y una **capa predictiva / early warning** nueva al final del archivo, que es la capa peor abastecida de esta KB y la que el Anexo III del EU AI Act nombra de forma explícita.
> *Pase 12 del 2026-10-01:* +1 en la tabla principal (**Study-Mate**), +1 en la capa MCP (**anki-mcp-server**, que
> multiplica por 499 el techo de esa capa) y +1 en evaluación (**ArguLens**). Se abre la **capa de distribución por
> skills de agente** al final del archivo: es la primera capa de esta KB que se mide contra otra vertical, y la
> educación pierde 58× contra la científica en el mismo canal. El conteo de 29 de la tabla principal se verificó a
> mano en este pase y **estaba bien**.
> *Pase 19 del 2026-10-01:* **+5 en la tabla principal** (**human-skill-tree**, **universal-examprep-skill**,
> **algo-sensei**, **universal-diagnostic-tutor-skill**, **lumen**) y **una región cerrada** (lumen → Alemania).
> Pero el trabajo principal de este pase es **corregir al pase 18, y en tres cosas distintas**, porque su hallazgo
> central se apoyaba en una causa falsa. Verificado con `git ls-remote` y con un clon *sparse* del árbol real:
>
> 1. 🔴 **`moodle/moodle` SÍ tiene rama `main`.** El pase 18 escribió textualmente que *«no tiene rama `main` ni rama
>    `master`»* y con eso explicó los cuatro 404 del pase 17. **Es falso:** `refs/heads/main` existe y apunta a
>    `85af0b5` = **Moodle 5.3rc1**. La causa real de los 404 es otra y es más útil: **Moodle movió su *webroot* al
>    subdirectorio `public/` en la serie 5.x.** La ruta no es `ai/provider/ollama/...` sino
>    `public/ai/provider/ollama/...`. Los 404 midieron **la ruta**, no la rama.
> 2. 🔴 **No son tres `privacy provider` de AI: son siete**, más uno del subsistema y dos de *placement* = **10
>    archivos**. Los siete son `anthropic`, `awsbedrock`, `azureai`, `deepseek`, `gemini`, `ollama` y `openai`.
> 3. 🔴 **Y los siete no sirven de plantilla de borrado, porque no borran nada.** Auditados uno por uno: 70–78 líneas
>    cada uno, **cero** llamadas a `delete_records`/`DELETE FROM`/`add_database_table`, y **exactamente un**
>    `add_external_location_link`. Todos sus métodos de borrado tienen **el cuerpo vacío** y están marcados
>    `@codeCoverageIgnore`. La plantilla real existe pero es **otra**: `public/ai/classes/privacy/provider.php`
>    (`core_ai`), ~800 líneas, **6 tablas** —incluidas `prompt` y `generatedcontent`— con `delete_records_list` de
>    verdad. El pase 18 nombró a los shims y no a la plantilla.
>
> **Lo que esto significa, y es el hallazgo del pase:** los siete shims no son un descuido, son una **declaración**.
> Lo único que hacen es declarar que el *prompt* del alumno y el modelo **salen hacia un tercero**. El núcleo de
> Moodle documenta así, en siete lugares, el punto donde su propia maquinaria de supresión **se queda sin nada que
> suprimir**. Ver las tendencias **48**, **49** y **50**, los patrones **P40** y **P41**, y el **gap 32**, que este
> pase **cierra refutándolo**.
> *Pase 18 del 2026-10-01:* se cierra el **gap 29** y **no lo cierra un tercero: lo cierra el núcleo de Moodle**, que
> trae **tres** `privacy provider` de referencia para plugins de AI (`openai`, `azureai`, `ollama`). Se corrige por qué
> el pase 17 no los vio —**`moodle/moodle` no tiene rama `main` ni `master`**, y sus cuatro 404 midieron el nombre de
> la rama, no una ausencia— y con eso el Privacy API pasa de *documentado por snippet* a **verificado de primera
> mano**. Se abre además la **capa de *unlearning***, que ejecuta la segunda acción escrita del pase 17 y confirma su
> predicción: la oferta existe, es grande y es **toda MIT/Apache**, al revés que la capa de borrado del LMS. La pieza
> más completa de `privacy provider` de toda la capa es **brasileña** (`local_aihub`), lo que mueve el **gap 2** otra
> vez. Se abren el **gap 31** y el **gap 32**. Ver las tendencias **45**, **46** y **47**, y los patrones **P38** y **P39**.
> *Pase 17 del 2026-10-01:* **no se agregó ninguna fila a la tabla principal.** Se contó a mano y **la tabla tiene
> 32 filas, no 31** — pero el encabezado es defendible y conviene registrar por qué, porque es la tercera vez que
> esta KB se pelea con este conteo: **una de las 32 filas no es un agente.** `education-agent-skills` es una
> biblioteca de Markdown/YAML y está además listada en la capa de distribución por *skills* de este mismo archivo.
> **32 filas = 31 agentes + 1 paquete de skills duplicado de otra capa.** Se deja la fila donde está (sirve de
> puntero) y se deja anotado que no cuenta como agente. Se **cierra el gap 20**: ya existe skill educativa con *eval* publicada, es **Apache-2.0** y son
> dos repos co-desarrollados (`anthropics/k12-teacher-skills` **541 ★**, nuevo en esta KB, y
> `learning-commons-org/agent-skills` **35 ★**, que **ya estaba** en la enumeración del gap 20 y sí tiene
> `evals/` — el gap lo había dado por carente). Los dos con carpeta `evals/` verificada. Entran en la **capa de distribución por skills** al final del archivo,
> que sube su techo permisivo de **299 a 541 ★**. Se reverificó **DeepTutor**: **40.6k ★**, v1.6.12 del
> **2026-09-27** — la fila ya estaba correcta. Y se refina el encuadre COPPA del pase 16: ver la corrección abajo.
> Se abren el **gap 29** y el **gap 30**. Ver las tendencias **42**, **43** y **44**, y los patrones **P36** y **P37**.
> *Pase 16 del 2026-10-01:* **no se agregó ninguna fila a la tabla principal; el conteo de 31 se mantiene.**
> Se abre la **capa de privacidad del dato del alumno** en `repos/foundations.md` —DP, federado y datos
> sintéticos—, y **no entra acá a propósito: no son agentes, son librerías horizontales**, y ése es parte del
> hallazgo. Lo que sí es de esta tabla: **ninguno de los 31 agentes declara qué hace con el dato del alumno**, y
> desde el **2026-04-22** la **voz de un menor es dato biométrico regulado** bajo la regla COPPA enmendada, lo que
> le pone encuadre legal a la capa de voz que abrió el pase 14. Se abren el **gap 27** y el **gap 28**. Ver las
> tendencias **39**, **40** y **41**, y los patrones **P34** y **P35**.
> *Pase 15 del 2026-10-01:* **no se agregó ninguna fila a la tabla principal; el conteo de 31 se mantiene.**
> Se abre la **capa de autoría y procedencia** al final del archivo —la mitad que le faltaba a la capa de
> integridad académica del pase 8, que era sólo *proctoring*—. **El hallazgo es un error propio:** desde el pase 4
> esta KB le vende a EMEA el deadline de *watermarking* del **2026-12-02** y **nunca registró una implementación**.
> Existe, es **Apache-2.0** y viaja dentro de Hugging Face Transformers (**SynthID-Text**). Se abren el **gap 25**
> (la detección no se puede usar para acusar: **61,3 %** de falsos positivos sobre no nativos de inglés) y el
> **gap 26**. Ver las tendencias **36**, **37** y **38**, y el patrón **P33**.
> *Pase 14 del 2026-10-01:* **no se agregó ninguna fila a la tabla principal; el conteo de 31 se mantiene.**
> Este pase abre dos capas nuevas al final del archivo —**lectura oral y pronunciación** (la primera capa de voz
> de esta KB) y **puente agente↔currículo nacional** (que mueve el gap 15)— y cierra el **gap 19** con cuatro
> esquemas curriculares nacionales verificados, que viven en `repos/foundations.md`.
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

> **Pase 13 del 2026-10-01:** +2 en la tabla principal (**jupyter-ai** y **Shiksha Copilot**) y +1 en evaluación
> (**pedagogy-benchmark**). Se abre en `repos/foundations.md` la **capa de práctica y corrección desplegada (Jupyter)**:
> doce pasadas preguntaron qué hace el agente y ninguna preguntó **dónde hace el alumno el trabajo**. La respuesta son
> cinco repos **BSD-3-Clause**, 14.334 ★, desplegados en universidades desde 2014, con runtime de agente y MCP ya
> incluido — y **corrige el gap 6**, que en once pasadas afirmó que la corrección open source no existía. Los otros dos
> hallazgos del pase son de encuadre: **pedagogy-benchmark** es MIT y está construido sobre **exámenes de habilitación
> docente del Ministerio de Educación de Chile**, y **Shiksha Copilot** documenta **1.043 docentes** con **9 estrellas**.
> Ver los **trends 30, 31 y 32**, los **gaps 21 y 22** y los patrones **P29** y **P30**.

| Nombre | Repo | Licencia | Stars | Lenguaje | Descripción | Origen (región) |
|--------|------|----------|-------|----------|-------------|-----------------|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 40.6k | Python | Tutoría personalizada "lifelong"; workspace agent-native con 8 superficies (Chat, Partners, Co-Writer, Book, Knowledge, Space, Memory), memoria en 3 capas y RAG multi-engine. v1.6.12 del 2026-09-27, releases semanales | APAC (HKU Data Intelligence Lab, Hong Kong) |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 39.7k | TypeScript | Open Multi-Agent Interactive Classroom: convierte un tema o documento en una clase interactiva multi-agente. Agent workbench, sesiones durables de course-building, skills reutilizables, persistencia pluggable. v1.1.2 del 2026-09-28. ⚠️ **Relicenciado de AGPL-3.0 a MIT en v0.3.0 (2026-06-28)**: la licencia permisiva tiene ~3 meses, no es el historial completo del proyecto | APAC (Tsinghua / THU-MAIC, China) |
| Project NOMAD | https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | 38.8k | JavaScript | Servidor de conocimiento y educación offline-first: Wikipedia, libros, cursos, mapas y AI local opcional, todo en Docker sobre hardware propio, sin internet. ~5 GB disco, <1 GB RAM sin el módulo AI | North America (Crosstalk Solutions, EE. UU.) |
| jupyter-ai | https://github.com/jupyterlab/jupyter-ai | **BSD-3-Clause** ✅ | 4.4k | Python/TypeScript | **El runtime de agente del entorno donde el alumno efectivamente trabaja**, y la pieza que doce pasadas de esta KB no vieron. «Connects AI agents to computational notebooks in JupyterLab»: habla **Agent Client Protocol (ACP)** y **servidores MCP propios**, y autodetecta los agentes instalados (Claude, Codex, GitHub Copilot, Gemini, Goose, Kiro, Mistral Vibe, OpenCode). No es un tutor: es el lugar donde el tutor se enchufa al cuaderno del alumno. Su pila de corrección y despliegue —JupyterHub, nbgrader, otter-grader, ltiauthenticator— está en `repos/foundations.md` y es **toda BSD-3-Clause**. *Agregado en el pase 13* | Global (proyecto Jupyter / NumFOCUS) |
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
| Shiksha Copilot | https://github.com/microsoft/Shiksha-Copilot | **MIT** ✅ | 9 | Python/TypeScript | **El despliegue docente más grande documentado en esta KB, y tiene 9 estrellas.** De **Microsoft Research India** (iniciativa VELLM): genera planes de clase alineados al currículo, ejemplos, analogías, actividades y evaluaciones formativas y sumativas. Pipeline de ingesta curricular (MinerU, SmolDocLing, OlmOCR), datastores vectorial + grafo + documental, frontend React y backend FastAPI. Investigación publicada sobre **1.043 docentes de Karnataka (India)** trabajando en **inglés y kannada**. 149 commits. ⚠️ **El propio repo declara que es un prototipo de investigación, «not extensively tested for production use», con supervisión humana obligatoria y no apto para despliegue comercial sin validación extensa** — citarlo como evidencia de que la categoría funciona a escala, no cotizarlo como componente. *Agregado en el pase 13* | APAC (India — Microsoft Research India, despliegue en Karnataka) |
| tutor-mcp | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 42 | Go | Servidor MCP que convierte cualquier LLM en un ITS: estado durable del aprendiz, scheduling de repaso, memoria de sesión, misconceptions, metacognición y decisiones pedagógicas auditables | Sin región verificada |
| learnmcp-xapi | https://github.com/DavidLMS/learnmcp-xapi | MIT | 15 | Python | Servidor MCP que le da a un agente memoria de aprendizaje **conforme al estándar**: tres tools sobre un Learning Record Store xAPI — registrar un statement, consultar el historial de progreso y gestionar el vocabulario de verbos/actividades. Backends: `lrsql`, `Ralph`, Veracity Learning, más arquitectura de plugins. Captura el aprendizaje de forma explícita ("practiqué bucles") o **inferida de la conversación**, y después consulta ese historial para adaptar la respuesta. **Es el único artefacto de esta KB que conecta un agente con IEEE 9274.1.1 (xAPI 2.0)** en vez de inventar su propio esquema. ⚠️ 32 commits: referencia de integración o base a forkear, no dependencia de producción. 🟢 **Pase 33 — lo que la ficha no registraba, leído del README (293 líneas):** la selección de LRS es **por variable de entorno** (`LRS_PLUGIN=lrsql \| ralph \| veracity`) con configuración por backend en `config/plugins/<backend>.yaml` (endpoint, credenciales, `retry_attempts`), Basic Auth y **OIDC** según lo que pida el LRS, y **privacidad por diseño**: un `ACTOR_UUID` por alumno con la afirmación *«No personal information is stored — only learning activities and progress indicators»*. 🔴 **Y una medición que cambia cómo se la busca: no está publicada en ningún registro de paquetes** — PyPI **404**, npm **`total: 0`** — así que se instala **desde el código** (*from source*, `venv` o `uv`). **Por eso el barrido del gap 60 no la encontró** (tendencia **99**). ⚠️ **Gap 63:** fuentes secundarias mencionan un **`2.0.0`** con *«complete redesign with a modular LRS plugin system»*, que dejaría vencido el *«no se movió»* del pase 25; **sin verificar** (`github.com/releases` da 403 y no hay `pyproject.toml` en la raíz de `main`). *Agregado en el pase 6; medido de nuevo en el pase 33* | ⚠️ **EMEA (España), con el matiz del pase 33.** El autor declara pertenecer al **IES Rafael Alberti**, instituto público de secundaria — lo escribió un docente en ejercicio, no un laboratorio. **Pero el `LICENSE` del repo dice textualmente `Copyright (c) 2025 David Romero`: el titular verificable es una persona, no la institución.** Las dos cosas son compatibles; para el argumento de soberanía europea en licitación conviene **Ralph** (France Université Numérique), cuyo titular institucional sí está en el archivo de licencia |
| openstax-mcp-server | https://github.com/pythpythpython/openstax-mcp-server | MIT (código) ✅ | 1 | TypeScript | Servidor MCP que le da a un agente acceso a **40+ libros de texto de OpenStax**: búsqueda semántica con embeddings de Cloudflare AI, generación automática de notebooks `.ipynb` por módulo y creación de problemas de práctica. Corre en Cloudflare Workers con Workers KV para cachear el XML parseado. **Es el único puente agente↔contenido curricular que encontró esta KB** — el equivalente, en la capa de contenido, de lo que `learnmcp-xapi` es en la capa de telemetría. 🔴 **Y hay que leerlo con la advertencia puesta: su README declara que el contenido servido es «Creative Commons Attribution 4.0 International (CC BY 4.0)», y el archivo `LICENSE` de los bundles de OpenStax en GitHub dice CC BY-NC-SA** en los tres títulos que este pase verificó. El código es MIT y es reutilizable; **la afirmación de licencia del contenido no se puede usar como base de un entregable facturado sin verificar título por título.** 7 commits. *Agregado en el pase 10* | Sin región verificada |
| gradescope-mcp | https://github.com/Yuanpeng-Li/gradescope-mcp | MIT | 8 | Python | Servidor MCP para Gradescope: 34 tools de gestión de cursos, batch grading, CRUD de rúbricas y regrade review. Escrituras detrás de confirmación explícita | Sin región verificada |
| TutorIA | https://github.com/LabSirius/TutorIA | MIT | 0 | Python | Tutor conversacional autónomo para **educación superior rural**, integrado dentro de Open edX y con la API de Claude como motor. Chat en lenguaje natural, respuestas en audio (TTS), avatar animado, dashboard de estadísticas para el docente y persistencia de contexto entre sesiones. Materias iniciales: Programación I (Python) e Introducción a la Matemática | **LATAM (Pereira, Colombia)** — Grupo Sirius, Universidad Tecnológica de Pereira (`sirius.utp.edu.co`) |
| OpenDidactia | https://github.com/nmarafo/OpenDidactia | CC BY-SA 4.0 ⚠️ | 0 | Markdown/YAML | Esquemas curriculares estructurados (estándar OKF) para que un agente genere **Programaciones Didácticas y Situaciones de Aprendizaje** conformes a la ley educativa española LOMLOE. Cubre las 17 comunidades autónomas y 2 ciudades autónomas, de Infantil a Bachillerato, FP y enseñanzas de régimen especial, con DUA y rúbricas analíticas. No es código: es el *esquema de salida* que hace auditable a un agente docente | EMEA (España) |
| mentar | https://github.com/avps82/mentar | **AGPL-3.0-only** ⚠️ | 1 | Python | Tutor local-first para chicos: corre entero en la máquina del hogar, sin cuentas ni datos que salgan del dispositivo. 934 nodos de concepto en 157 plantillas curriculares (Australia ACARA v9, India, Singapur, EE. UU.). **El detalle de diseño que importa:** el LLM sólo explica y un *checker determinístico* corrige cada respuesta, así que el modelo no puede darle por buena una respuesta incorrecta a un chico. Último commit 2026-08-26 | Sin región verificada (currículo AU primero, pero el repo no declara ubicación) |
| tero | https://github.com/marcorojasb/tero | **MIT** ✅ | 0 | Python | Agente docente de aula para K-12 **chileno**, de terminal y **offline-first**, sobre AWS Bedrock + Strands Agents SDK. Prepara material pedagógico y **adapta contenido para alumnos con necesidades especiales**. La decisión de diseño que lo hace citable: *«el agente propone, el docente decide»* — **el modelo no escribe archivos sin aprobación humana**. Anclado a instrumentos nacionales: MINEDUC, **Decreto 83** (educación especial) y **Ley 21.719** (protección de datos). 111 commits. **0 ★: referencia de arquitectura y contraparte local, no dependencia de producto.** *Agregado en el pase 8* | LATAM (Chile) |
| Study-Mate | https://github.com/Miaotofu01/Study-Mate | **MIT** ✅ | 482 | Python | Compañero de estudio con planificación curricular, instrucción y aprendizaje por proyectos en matemática y CS. *Workflow* integrado + motor de cursos HTML; corre sobre DeepSeek Harness, Google Antigravity y plugins de ChatGPT. 298 commits | APAC |
| human-skill-tree | https://github.com/24kchengYe/human-skill-tree | **AGPL-3.0** ⚠️ (dir. `skills/` en doble licencia MIT/AGPL-3.0) | 562 | TypeScript/Markdown | 33 skills de agente que convierten ChatGPT, Claude, Gemini y compatibles en acompañantes de aprendizaje estructurado, de K-12 a desarrollo profesional. Repetición espaciada y *active recall* explícitos, simulación de aula multi-agente, tutores socráticos y quizzes adaptativos. Declara cobertura de **15 sistemas educativos nacionales y 800+ materias** — es la pieza de mayor alcance curricular declarado de esta tabla. 36 commits. ⚠️ **La licencia es el dato que decide el uso:** el repo es AGPL-3.0 y sólo el directorio `skills/` está en doble licencia MIT/AGPL-3.0. Para un entregable cerrado **sólo es utilizable el subárbol de skills**, y conviene verificarlo archivo por archivo antes de facturar. *Agregado en el pase 19* | Sin región declarada (documentación bilingüe EN/中文) |
| universal-examprep-skill | https://github.com/ZeKaiNie/universal-examprep-skill | **MIT** ✅ | 299 | Python | Skill de preparación de exámenes que ingiere slides, apuntes, tareas y exámenes viejos (PDF, PPTX, DOCX, Markdown) y enseña **citando `archivo p.N` en cada concepto**, extrae figuras, examina con las preguntas reales de la materia, registra errores y arma guías de estudio. Memoria entre sesiones. Instalable con `npx skills add ZeKaiNie/universal-examprep-skill` en Claude Code, Cursor, Windsurf, Codex, Antigravity, Gemini CLI y 40+ agentes. 181 commits. **La propiedad que lo hace citable, y no es pedagógica sino regulatoria:** declara **citación obligatoria con número de página y 100 % de abstención fuera de alcance**, que es exactamente lo que pide el inciso (a) de la Decisión 33 de Vietnam —contenido de autoaprendizaje con *fuentes de datos no controladas* es alto riesgo—. Ver el patrón **P41**. *Agregado en el pase 19* | Sin región declarada |
| algo-sensei | https://github.com/karanb192/algo-sensei | **MIT** ✅ | 281 | Markdown (multi-lenguaje: Python, Java, C++, JS, Go) | Mentor de estructuras de datos y algoritmos que **se niega a dar la solución**: sistema de pistas de **cinco niveles** escalonados —desde la observación más suave hasta el esqueleto en pseudocódigo—, entrenamiento en reconocimiento dinámico de patrones (no plantillas memorizadas), método socrático declarado (*«learn through questions, not lectures»*) y cinco modos (Tutor, Hint, Review, Interview, Pattern Mapper). Su filosofía escrita es *«productive struggle with guidance»*. Corre en Claude Code y Claude.ai. **Sólo 8 commits:** es una especificación pedagógica, no un producto — el mismo perfil que `Alvarmethod`, y el andamiaje graduado es la contraparte operativa de lo que `Gnos` instrumenta como evidencia. *Agregado en el pase 19* | Sin región declarada |
| universal-diagnostic-tutor-skill | https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill | **MIT** ✅ | 235 | Markdown | Tutor *diagnosis-first* para STEM, matemática, programación y AI/CS: antes de enseñar **determina dónde está trabado el alumno**, con un ciclo de clarificar objetivo → localizar el hueco en cuatro niveles (materia → sistema de conocimiento → subtema → conceptos núcleo) → instrucción mínima dirigida → verificación → decisión de avance por mastery demostrada. Continuidad entre conversaciones mediante **«Learning State Cards» visibles** —el estado del alumno es inspeccionable por el alumno, no sólo por el sistema—, enrutamiento en lenguaje natural sin menús de modo y análisis cualitativo de error. v2.0.0 reduce ~41 % el contexto respecto de v1.9.2. Skill oficial de DeepSeek Harness, con variante *Lite Prompt* para chat estándar. 57 commits. *Agregado en el pase 19* | Sin región declarada |
| lumen | https://github.com/ahmedEid1/lumen | **GPL-3.0** ⚠️ | 88 | Python/TypeScript | Plataforma donde el alumno describe su objetivo y un orquestador multi-agente propio (**sin LangChain**) le construye el curso. **Modelo *learner-owned* declarado:** *«every signed-in user runs the whole loop themselves; `admin` only moderates and configures»* — el alumno define, construye, aprende, comparte y remezcla en un catálogo moderado. RAG **con alcance por curso y citación, detrás de un único autorizador**, con aislamiento explícito para que cursos privados y clonados no filtren datos. BYOK con credenciales cifradas, servidor MCP con 9 tools, PostgreSQL 17 + pgvector, decisiones del agente auditables en una tabla `llm_calls`. 828 commits, 1.421 tests de backend y 468 de frontend. **La decisión que lo hace citable:** su *eval harness* **publica también los puntajes malos** — es el único artefacto de esta KB que documenta sus propias debilidades medidas. ⚠️ GPL-3.0: referencia de arquitectura y despliegue propio, no base de un entregable cerrado. *Agregado en el pase 19* | **EMEA (Essen, Alemania)** — el perfil del autor (Ahmed Hobeishy) declara `Essen, Germany`. *Región cerrada en el pase 19* |
| canvas-mcp | https://github.com/vishalsachdev/canvas-mcp | **MIT** ✅ | 269 | TypeScript | **El conector permisivo de LMS más grande de esta KB.** Servidor MCP sobre la API de Canvas con **hasta 102–103 tools** (el README dice «up to 102» en el encabezado y «up to 103» en el resumen: se transcribe la ambigüedad del propio repo) y **8 *agent skills***. Es el primero de esta base que cubre **las dos puntas**: lado alumno (entregas, notas, TODO, *peer review*) y **lado docente** (gestión de tareas, corrección, analítica de alumnos, mensajería), más módulos, páginas, archivos, y un *Learning Designer* que incluye **escaneo de accesibilidad y chequeo WCAG** — la capa del pase 8 llega al conector. Trae `search_canvas_tools` para **descubrimiento de tools**, que es la respuesta a tener 100+: el agente busca la herramienta en vez de recibir las cien. 815 commits, 92 forks. ⚠️ Es *tool-side* sobre la API de Canvas: **no reemplaza el lado LMS** (ver el cierre del lado *platform*, abajo). *Agregado en el pase 26* | Sin región verificada |
| moodle-mcp-server (peancor) | https://github.com/peancor/moodle-mcp-server | **MIT** ✅ | 43 | TypeScript | **La primera pieza permisiva de esta KB que escribe nota y devolución dentro de un LMS de producción**, y por eso la primera que toca el **gap 6** (corrección, abierto desde el pase 2) del lado del verbo correcto. **8 tools, cuatro de escritura:** `get_courses`, `list_students`, `get_assignments`, `get_student_submissions`, **`provide_assignment_feedback`** (pone nota y comentario en la tarea), `get_quizzes`, `get_quiz_attempts`, **`provide_quiz_feedback`**. Habla **Moodle Web Services** por token: **no se modifica el LMS**. 13 forks, 10 commits. ⚠️ **10 commits no son una base de producción** — es el punto de partida del último tramo, no el sistema de corrección. 🔴 Desmiente el **gap 43** del pase 26, que lo declaraba inexistente. *Agregado en el pase 27* | Sin región verificada |
| moodle-mcp (MarcosNahuel) | https://github.com/MarcosNahuel/moodle-mcp | **MIT** ✅ | 1 | TypeScript | **El conector MCP de Moodle más completo que existe, y tiene 1 estrella** — el caso más puro del **gap 49** (los directorios rankean por promoción, no por capacidad). **40 tools** en 10 dominios: Curso (crear, actualizar, duplicar, archivar), Secciones, Contenido (publicar material, generar video), Evaluación (configurar quiz, importar GIFT), Alumnos (matrícula, grupos, roles), Gradebook, Comunicación (mensajería, anuncios de foro), Calendario, Badges — **más `ws_raw`, un escape hatch a Web Services crudo** que es la decisión de diseño que conviene portar. v0.5.2 (wrapper) + v0.5.0 (plugin); el README declara **«~80 % operable desde un agente LLM»** y deja salvedades abiertas en subida de archivos y creación de secciones. 59 commits, 1 fork. ⚠️ **Pre-producción declarada por el propio autor.** *Agregado en el pase 27* | Sin región verificada |
| scorm-mcp-server | https://github.com/giacomomaria81/scorm-mcp-server | **MIT** ✅ | 6 | TypeScript | **El puente al LMS que el cliente ya tiene instalado, en el formato que ese LMS ya sabe importar.** Convierte HTML (o *bundles* de diseño) en paquetes **SCORM 2004 4.ª edición y SCORM 1.2**, versión elegible por parámetro. **3 tools:** `scorm_package`, `scorm_validate` (conformidad de un paquete existente), `scorm_selftest`. **Inlinea cada asset —CSS, fuentes, JS, imágenes— como data URI, así que el paquete corre 100 % offline**, e inyecta el *runtime* que reporta *completion*, progreso, tiempo y **resume entre sesiones**. Autohospedable; la demo online es opcional. 0 forks, 11 commits. **Es la pieza de salida que a la capa generativa de esta KB (OpenMAIC, Educhain) le faltaba para aterrizar en un LMS sin integrarse con él.** Ver **P56**. *Agregado en el pase 27* | Sin región verificada |
| oneroster-ts | https://github.com/trilogy-group/oneroster-ts | **0BSD** ✅ | 10 | TypeScript | 🔴 **Refuta el «OneRoster vacío» del pase 26, y es la superficie de tools más grande de esta KB: 🔵 132 tools SERVIDAS, medidas ejecutando `tools/list` en el pase 30** (72 de lectura y 60 de escritura, en 19 grupos). **El «164 métodos» del pase 28 era el conteo del SDK y ya está explicado: son 132 operaciones distintas + 32 alias listados bajo dos grupos a la vez, así que no hay nada oculto —el 100 % de las operaciones se sirve—, al revés de CaSS (6 de 61).** 164 métodos documentados** sobre 21 recursos OneRoster (`academicSessions`, `classes`, `courses`, `enrollments`, `results`/`lineItems`, `orgs`, `schools`, `users`, `demographics`, `scoreScales`…), **expuestos como MCP tools con lectura y escritura** (`createUser`, `updateClass`, `deleteEnrollment`, `postAcademicSession`). OneRoster **v1p2**, paginación por offset y `filter` de 1EdTech. **0BSD es la licencia más permisiva que vio esta KB** — dominio público de hecho, sin obligación de atribución. 🔵 **Y el pase 30 mejora el veredicto legal del pase 29:** `package.json` **omite el campo `license`** (de ahí el `license: None` del registro), **pero el tarball publicado SÍ trae un `LICENSE` completo con el texto 0BSD** (*Copyright (c) 2025 Bjorn Pagen*, que es uno de los *maintainers* de npm, así que la procedencia cierra): **el defecto es de metadatos, no de licencia.** 🔴 **En cambio la antigüedad era peor de lo registrado:** el pase 29 leyó `time.modified` (mutación de metadatos) y escribió «2026-05-04»; la última **versión** publicada es `0.7.0` del **2025-06-27**, o sea **quince meses**, con 9 de las 10 versiones en una ráfaga de tres días. **Fijar un fork sigue siendo el requisito, ahora por abandono y no por licencia.** 🔴 Riesgo nuevo: el README usa como token de ejemplo el IdP Cognito de **un operador concreto** (`alpha-auth-production-idp…`), así que el SDK se generó contra **un despliegue**: hay que sobreescribir `--server-url`/`--token-url`. 🔵 A favor: **cero dependencias de runtime** y un flag **`--tool`** que permite servir un subconjunto de las 132, que es el control de ventana de contexto que hace falta. ⚠️ **No se llama `*-mcp`: es un SDK que expone MCP en una línea del README**, y por eso tres pases no lo encontraron (**gap 49 / gap 50**). 3 forks, 39 commits. *Agregado en el pase 28* | Sin región verificada |
| ed-tech-system-mcp | https://github.com/paulocymbaum/ed-tech-system-mcp | **MIT** ✅ | 0 | Python | Servidor MCP *domain-driven* para flujos de ed-tech, con **18 tools respaldadas por agentes LangGraph**: `content_generation`, `author_lesson_pipeline`, `validate_lesson`/`validate_quiz`/`validate_project`, `search_graph_nodes` (grafo de currícula), `generate_mock_test_structure`, **`socratic_tutor`**, `collect_project_review_context` + `project_review`, `search_youtube`. Arquitectura limpia + DDD declaradas. ⚠️ **Early-stage declarado por el autor** (backlog «23 done, 6 deferred») y 🔴 **sin integración a ningún LMS**: persiste en backend propio sobre Supabase, así que **no sustituye a un conector de Moodle/Canvas, se compone con uno**. **0 ★ con 132 commits — otro caso puro del gap 49.** *Agregado en el pase 28* | Sin región verificada |
| openedu-mcp | https://github.com/Cicatriiz/openedu-mcp | **MIT** ✅ | 13 | Python | **La capa de descubrimiento de recursos abiertos, que es la que esta KB no tenía en formato de agente.** Servidor MCP sobre **OpenLibrary + Wikipedia + arXiv** con filtrado educativo y adecuación por nivel de grado. **21 nombres de tool leídos del README crudo, de los cuales 20 son de dominio y 1 es transporte** (`handle_stdio_input` no es una herramienta: es el loop de stdio que se filtró a la lista). Los cuatro bloques: libros (`search_educational_books`, `get_book_details_by_isbn`, `search_books_by_subject`, `get_book_recommendations`), artículos (`search_educational_articles`, `get_article_summary`, `get_article_content`, `get_featured_article`, `get_articles_by_subject`), vocabulario (`get_word_definition`, `get_vocabulary_analysis`, `get_word_examples`, `get_pronunciation_guide`, `get_related_vocabulary`) e investigación (`search_academic_papers`, `get_paper_summary`, `get_recent_research`, `get_research_by_level`, `analyze_research_trends`). ⚠️ **No toca ningún LMS ni ningún estándar**: es contenido, no sistema institucional — **no reemplaza un conector**. 21 commits y **10 forks sobre 13 ★**, una relación fork/estrella alta que es señal de uso temprano, no de madurez. Licencia verificada en el archivo `LICENSE` (*MIT, Copyright (c) 2025 OpenEdu MCP Team*), no en el README | Sin determinar — el `owner` no declara ubicación y no se inventa |
| openedx-mcp | https://pypi.org/project/openedx-mcp/ | 🔴 **AGPL-3.0** | — (PyPI, 5 releases) | Python/Django | 🔴 **La puerta oficial de Open edX, y la que cierra el gap 48 que esta KB tenía como su mejor oportunidad.** *«Open edX admin operations exposed as an MCP facade for staff/superusers (Ulmo)»*. **35 endpoints medidos leyendo el sdist 0.1.5: 28 en el LMS + 7 en el CMS (autoría).** Escritura real: `enroll`/`unenroll`/`bulk-enroll`, `users/create`, `roles/set`, `access/instructor`, `students/reset-attempts`, certificados (generar, regenerar, invalidar), reportes asíncronos y **`retirement/request`**; autoría en el CMS con `blocks/create`, 🔵 **`blocks/create-tree`** (árbol entero en una llamada), `update`, `publish`, `delete`. **9 scopes** (`read`, `write:enrollment`, `write:users`, `write:roles`, `grant:admin`, `write:certificates`, `write:reports`, `write:courses`, `destructive`) y **18 tools de escritura con rate limit por tool**. 🔵 **Cuatro rails contra «agente en bucle»: re-chequeo de autoridad vivo, rate limit, confirm token con dry-run atado a huella del payload, y auditoría append-only previa a la escritura.** 🔴 **Corre EN PROCESO como plugin Django dentro del LMS y del CMS, y es AGPL-3.0: no hay escotilla de «proceso separado», así que rompe la tesis de composición del pase 27.** ⚠️ `0.1.5`, apunta a Open edX **Ulmo**; `tools/list` **no observado** (no se levantó instancia). Verificado en **PyPI JSON + código del sdist**; `openedx.org` está bloqueado por el proxy. *Agregado en el pase 30* | Global (proyecto Open edX) |
| tutor-contrib-openedxmcp | https://pypi.org/project/tutor-contrib-openedxmcp/ | 🔴 **AGPL-3.0** | — (PyPI, 7 releases) | Python | **La mitad de despliegue del par anterior:** *«Tutor plugin: MCP server + openedx-mcp Django app for staff/superuser admin (Ulmo)»*. Instala el app Django y **corre el servidor MCP**; soporta **Tutor local y Kubernetes**. `0.1.7`, publicado el **2026-07-25**. **Sin este paquete, `openedx-mcp` es sólo la fachada REST interna: el servidor MCP vive acá.** *Agregado en el pase 30* | Global (proyecto Open edX) |
| asfai-education | https://github.com/redbeard-26/asfai-education | **Apache-2.0** ✅ | 2 | TypeScript | **La primera pieza de esta KB que declara cinco estándares 1EdTech a la vez**, y la única que presenta una arquitectura de evidencia y maestría completa en permisivo: *«Open, standards-based architecture and reference implementation for AI-mediated learning, evidence, and mastery»*. **9 gateways MCP:** `asfai_capability` (descubre capacidades y entrega guía de workflow), `asfai_graph` (grafo de aprendizaje: vecinos, fronteras, caminos), `asfai_run` (trabajo versionado con contratos de revisión), `asfai_session` (diálogo reanudable + quizzes formativos), `asfai_lesson` (autoría→validación→revisión→publicación), `asfai_evidence` (evaluaciones y observaciones justificadas), `asfai_resource`, `asfai_storage`, `asfai_classroom` (conecta proveedores de aula). Estándares nombrados: **QTI** (ítems y resultados portables), **xAPI / IEEE 9274.1.1**, **CASE** (competencias K–12), **LTI + OneRoster** y **CLR + Open Badges**. ⚠️ **2 ★ y 42 commits: es un mapa de capas, no una dependencia** — no va a un entregable de cliente como pieza instalada. ⚠️ **No refuta la ausencia de QTI**: declara QTI como formato, no es un conector MCP de QTI. MCP y licencia verificados en el **README crudo** y el archivo `LICENSE`. *Agregado en el pase 30* | Sin región verificada |
| lineage-skill | https://github.com/JuneYaooo/lineage-skill | **Apache-2.0** ✅ | 448 | Python | 🟢 **El primer alta de agente en ocho pases, y entra por el eslabón que esta KB declaraba vacío: convertir el material de un docente en la metodología ejecutable de un agente.** Destila **videos, PDFs, transcripciones y apuntes** en *Agent Skills* docentes **con trazabilidad a la fuente**: extrae activos de capacidad —diagnósticos, flujos de trabajo, **rúbricas**, plantillas, reglas de transferencia y **modos de falla**—, emite paquetes de conocimiento compatibles con **OKF**, y **fusiona varios cursos preservando campos de habilidad**. Corre sobre Codex, Claude Code, OpenClaw y Hermes. **Por qué importa y no es otra skill de estudio:** las piezas que esta tabla ya tenía o son skills *escritas a mano* (`education-agent-skills`, `human-skill-tree`) o son tutores que consumen material; esta **produce la skill desde el material del docente**, que es el paso que faltaba entre uno y otro. La trazabilidad a la fuente es además la contraparte técnica del hallazgo regional de LATAM (**65 % de los estudiantes teme que la AI vuelva superficial el aprendizaje**): una metodología citable es la respuesta a esa objeción. *Agregado en el pase 32* | Sin región verificada (documentación bilingüe EN/中文) |


## Capa de conectores MCP por LMS y por estándar — agregada en el pase 27 del 2026-10-01

**Lo que este pase corrige antes de agregar nada.** El pase 26 cerró afirmando que **Moodle no tenía conector MCP
permisivo** (gap 43) y construyó el patrón **P51** sobre eso. **Es falso**, y lo desmintió una búsqueda. La tabla de
arriba suma las tres piezas nuevas; acá queda el mapa completo, que es lo que se lleva a una conversación con cliente.

### El mapa, por LMS

| LMS | Licencia del LMS | Conector MCP | Licencia | Escribe | Madurez |
|---|---|---|---|---|---|
| **Canvas** | AGPL-3.0 | `vishalsachdev/canvas-mcp` | **MIT** ✅ | Sí | El más maduro. Ver la advertencia de cifra, abajo |
| **Moodle** | GPL-3.0+ | `peancor/moodle-mcp-server` | **MIT** ✅ | **Sí — nota y devolución** | 43 ★, 13 forks, **10 commits** |
| **Moodle** | GPL-3.0+ | `MarcosNahuel/moodle-mcp` | **MIT** ✅ | Sí, 40 tools | 59 commits, **1 ★**, pre-producción declarada |
| **Moodle** | GPL-3.0+ | `csmediapro/moodle-mcp-server` | ⚠️ **AGPL-3.0** | No (lectura) | Capas útiles = **plugins premium de pago** |
| 🟡 **Open edX** | **AGPL-3.0** | **`openedx-mcp` + `tutor-contrib-openedxmcp`** (oficial del proyecto, PyPI) | ⚠️ **AGPL-3.0** — corre **en proceso** como plugin Django | **Sí — 19 escrituras en 6 scopes** | **La fila cambia de «hueco» a «existe y es copyleft» (pase 30), y el pase 31 la mide desde el wheel publicado:** **35 rutas** (28 LMS + 7 CMS), **19 herramientas de escritura**, **11 con *confirm token* y 8 sin él**. AGPL-3.0 **leída del `LICENSE` del artefacto**, no de la metadata. 🔴 **Ninguna de las 19 crea un curso** — y tampoco lo hace ninguna de las **cinco** versiones REST (`v0`–`v4`): el `v0` de authoring está **deprecado en favor del `v1`** con `DeprecationWarning` en runtime, y el único primitivo de nivel curso es **`course_rerun`** (clona). Ver **gap 50 (cerrado)**, **gap 55 (medido)**, **gap 57** y **P63** | Gap 48 y **gap 50** cerrados · gap 55 medido · **gap 57** · P55 · **P63** |
| **SCORM** (formato) | — | `giacomomaria81/scorm-mcp-server` | **MIT** ✅ | Genera paquetes | 3 tools, offline. **P56** |

⚠️ **Advertencia de cifra sobre `canvas-mcp`, y vale como regla.** La fila de la tabla principal registra **269 ★,
815 commits y «102–103 tools»**, verificado de primera mano en el pase 26. Este pase **no reconfirmó esas cifras** y
encontró que **el conteo de tools varía según la versión** que se consulte: se declaran **40+**, **80+** y **116** en
distintos puntos. 🔴 **El número de tools de este repo no es citable como cifra fija en un entregable** — se cita la
capacidad («más de cuarenta herramientas, lado alumno y lado docente»), no el número.

### El mapa, por estándar educativo — y acá la medición es de primera mano sobre el código

Cruzando `MCP server` con cada estándar que esta KB inventarió. **Lo nuevo de este pase es la columna de la derecha:
qué decidió exponer, y qué decidió ocultar, el proyecto de referencia de cada estándar.**

| Estándar | Conector MCP de terceros | En `cassproject/CASS` (medido por anotación) |
|---|---|---|
| **xAPI** | ✅ `learnmcp-xapi` (desde el pase 6) — 🔴 **y el pase 33 tuvo que reconfirmarlo porque el gap 60 del pase 32 declaró esta celda vacía.** Está acá desde el pase 6 y sigue siendo **MIT, 3 tools (1 escribe, 2 leen)**. **La lección está en la tendencia 101: una ausencia no se declara sin hacer `grep` sobre esta KB** | **1 expuesta** (`record_evidence`) / 4 ocultas — **un statement por llamada** |
| **Competencias / perfil** | — | **1 expuesta** (`get_learner_profile`) / 0 ocultas |
| 🔴 **CASE** | **nada** (y el término está capturado, gap 44) | **0 expuestas / 13 ocultas** — autoría de marcos **cerrada a MCP** |
| 🔴 **CEASN** | **nada** | **0 expuestas / 6 ocultas** |
| 🔴 **Open Badges** | **nada del estándar** — lo que aparece es SaaS comercial (`IssueBadge`) y generadores de *badges* de README (**tercera colisión de término**) | **0 expuestas / 5 ocultas**, y **ancladas a `w3id.org/openbadges/v2` → OB 2.0, no 3.0** |
| 🔴 **Caliper** | **nada**, consistente con que dejó de ser open source el **2023-06-17**. **La ausencia está escrita, no inferida** | — |
| ✅ **OneRoster** | 🔴 **La ausencia del pase 26 era falsa.** `trilogy-group/oneroster-ts` (**0BSD**, 10 ★) expone **164 métodos como MCP tools, con escritura**, sobre OneRoster **v1p2**. **No está en ningún directorio de MCP y no se llama `*-mcp`** | — |
| 🔴 **QTI** | **nada, y es la única ausencia de esta KB medida por tres métodos independientes**: directorio, patrón de nombre, y **apertura del SDK permisivo** (`examplary/qti`, MIT, QTI 3.0 + 2.1 — **MCP no se menciona**). La otra pieza, `oat-sa/qti-sdk`, es **PHP**, donde el ecosistema MCP es marginal: **eso explica la ausencia, no sólo la registra**. Ver **P59** | — |
| ✅⁄🔴 **CASE** (medido en el pase 29) | ✅ **La plataforma existe y es permisiva; el conector sigue sin existir — y ahora las dos mitades están medidas.** [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) (**Apache-2.0**, 9 ★, 3 forks, 180 commits) implementa **CASE 1.0 y 1.1** con la **CASE Provider API oficial**, CRUD de escritura sobre `CFDocuments`/`CFItems`/`CFAssociations`/`CFPackages` en **v1p0 y v1p1**, Keycloak (OIDC) **más API keys**, RBAC de cuatro niveles y multi-tenencia. 🔴 **MCP: cero menciones en el README crudo** — la ausencia pasa de *«sin medir por colisión»* (gap 51) a **medida**. 🔵 **Y es la ausencia más barata de cerrar de esta KB, porque el servidor publica su propio OpenAPI 3** (`GET /ims/case/v1p1/discovery/imscasev1p1_openapi3_v1p0.json`): **el conector se genera, no se escribe** — el mismo camino por el que `oneroster-ts` llegó a 164 métodos. Ver **P60** | **0 expuestas / 13 ocultas** en `cassproject/CASS` — la autoría de marcos sigue **cerrada a MCP** del lado de CaSS, que es justo lo que OpenCASE abre por REST |

**Las dos frases que esto habilita, y las dos que prohíbe.** Habilita: *«la evidencia de aprendizaje entra por MCP, de
a un statement»* y *«el perfil de competencia se lee por MCP»*. 🔴 Prohíbe: *«emitimos insignias por MCP»* y
*«autoramos el marco de competencias por MCP»* — **las dos están excluidas a propósito** por el proyecto de
referencia, y van por REST **fuera** de la superficie de agente. Y si el cliente pide credenciales **OB 3.0 / W3C VC**,
**CaSS no es la pieza que las emite**.

### La trampa de despliegue que decide si hay superficie MCP o no

Leído de primera mano en `src/main/server/cartridge/adapter/mcp.js`: el adaptador **no lee el spec del disco**, lo pide
**por loopback** — `fetch(CASS_LOOPBACK + '/swagger.json')`, default **`http://localhost/api/`**, puerto **80**. Si ese
`fetch` falla o no devuelve `ok`, el adaptador **loguea y hace `return`**: 🔴 **la ruta `/api/mcp` no se monta, y el
servidor arranca normalmente.** Con proxy, puerto no estándar o HTTPS mal resuelto, **la superficie de agente
desaparece en silencio**. Se apaga además con `DISABLED_ADAPTERS=mcp`. **Es lo primero que hay que mirar si un cliente
reporta que no ve herramientas.**
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
| **pedagogy-benchmark** | https://github.com/AI-for-Education/pedagogy-benchmark | **MIT** ✅ | 12 | **Conocimiento pedagógico del modelo, medido con exámenes reales de habilitación docente — y los exámenes son chilenos.** 1.143 preguntas en dos componentes: **CDPK** (920, conocimiento pedagógico general transversal a materias, grupos de edad y subdominios pedagógicos) y **SEND** (223, *Special Educational Needs and Disabilities*). El repo acredita las preguntas a la **Agencia de la Calidad de la Educación** y al **CPEIP del Ministerio de Educación de Chile**. Paper: arXiv 2506.18710. De la organización **AI-for-Education** («Empowering Education in LMICs with AI»). Python, 5 commits. **Es la primera pieza de la capa de evaluación de esta KB construida sobre un instrumento estatal latinoamericano, y la primera con componente de educación especial con licencia permisiva.** *Agregado en el pase 13* |
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

### El hallazgo de encuadre del pase 13: el aporte de LATAM a esta capa no es el repo, es el instrumento de medición

`pedagogy-benchmark` (**MIT**, 12 ★) obliga a releer dos gaps de esta KB a la vez.

**Contra el gap 4.** Desde el pase 7 esta KB viene anotando que **las piezas de evaluación con licencia limpia son todas
chinas**: `XES3G5M` (MIT, el único dataset de knowledge tracing permisivo), `ProHist-Bench` dentro de `ABench`
(Apache-2.0, de `inclusionAI` = Ant Group), `EduBench` (MIT). El pase 12 cerró con la concentración APAC «sin moverse».
**Se mueve acá, y no por donde se la buscaba.** El benchmark es de una organización enfocada en **LMICs**, su código es
MIT, y **sus 1.143 preguntas salen de los exámenes de habilitación docente del Estado chileno** — el repo acredita
explícitamente a la **Agencia de la Calidad de la Educación** y al **CPEIP del Ministerio de Educación de Chile**.

**Contra el gap 2.** Ocho pasadas midieron la oferta LATAM contando *repos* y el resultado fue siempre el mismo: techo
de 0–3 estrellas, proyectos que mueren en el día 90. La conclusión del pase 6 —«no falta talento ni diseño, falta
continuidad»— sigue siendo verdadera, **pero estaba midiendo la cosa equivocada.**

El activo educativo exportable de LATAM que esta KB encontró con tracción real **no es software**. Es un **instrumento
de medición pedagógica producido por el Estado**: estandarizado, validado, con décadas de aplicación, y lo
suficientemente bueno como para que un laboratorio enfocado en países de renta baja y media lo use como vara para medir
el conocimiento pedagógico de los LLM del mundo. Chile no puso el repo. **Puso la pregunta con la que se evalúa al
modelo**, que es la pieza más cara y la más difícil de replicar de cualquier benchmark — el pase 7 ya lo había dicho de
las 10.891 rúbricas de `ProHist-Bench`.

**Y abre un sub-gap que no estaba.** `SEND` (223 preguntas de *Special Educational Needs and Disabilities*) es, con
licencia MIT, **la primera pieza de evaluación de educación especial de esta KB**. El pase 8 había dejado escrito que en
accesibilidad y educación especial «lo maduro es copyleft y lo agéntico y permisivo no pasa de 15 estrellas», y que la
capa no tenía forma de **medirse**. Ahora tiene una, es permisiva, y nadie la está usando: 12 estrellas. Ver el **gap 22**
y el patrón **P30**.

⚠️ **Dos límites, y hay que decirlos.** (a) **12 estrellas y 5 commits**: es un artefacto de investigación, no una
dependencia de producto — se usa como vara de medición en un entregable, no se empaqueta. (b) Mide **conocimiento
pedagógico declarativo** del modelo —responder un examen de habilitación docente— que **no es lo mismo que calidad de
enseñanza en diálogo**, que es lo que miden `MathTutorBench` y `UnifyingAITutorEvaluation`. Son complementarios, y
presentarlo como sustituto sería el mismo error que el pase 7 marcó con `ProHist-Bench`. 🔴 El paper (arXiv 2506.18710)
**no se pudo abrir en este pase**: `arxiv.org` sigue bloqueado por el proxy de egreso. Licencia, conteos, composición y
la atribución a Chile **sí** están verificados de primera mano en la página del repo.

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

### Corrección del pase 17 — la voz del menor sí está regulada, pero no por la vía que el pase 16 escribió

El **pase 16** anotó, acá arriba y en el **gap 28**, que *«desde el 2026-04-22 la voz de un menor es dato
biométrico regulado bajo la regla COPPA enmendada»*. **La conclusión práctica es correcta y la vía no.** La
distinción cambia qué se escribe en un expediente de cumplimiento, así que se corrige en vez de dejarla pasar:

- **Lo que sí hizo la regla enmendada:** agregó a la definición de información personal *«a biometric identifier
  that can be used for the automated or semi-automated recognition of an individual»*, y la enumeración **incluye
  `voiceprints`** junto con huellas, patrones de retina e iris, datos genéticos, marcha, plantillas faciales y
  *faceprints*. Exigible en pleno desde el **2026-04-22**.
- **Lo que la FTC explícitamente NO incluyó:** los datos **derivados** de voz, de rostro y de marcha
  (*voice-derived, facial-derived, gait-derived data*). Estaban propuestos en el NPRM de 2024 y **se quitaron de
  la regla final** tras los comentarios por amplitud excesiva.
- **Y el dato que vuelve más vieja la exposición, no más nueva:** un **archivo de audio con la voz de un chico ya
  estaba cubierto** como categoría propia de información personal bajo **16 CFR 312.2 antes de las enmiendas**.

**Las dos consecuencias operativas:**

1. **`voiceprint` ≠ grabación de voz.** Un *voiceprint* es una plantilla para reconocer a la persona. Un tutor de
   lectura oral que transcribe y puntúa pronunciación **sin construir ni almacenar plantilla de identificación**
   no entra por la puerta biométrica — entra por la de audio del menor, que es la que ya existía.
2. **La fecha a citar no es el 2026-04-22 para todo.** Para la grabación de voz la obligación **precede** a las
   enmiendas; lo que el 2026-04-22 agrega es la **política escrita de retención**, la **prohibición de retención
   indefinida** y el borrado una vez cumplido el propósito. Vender «esto es nuevo desde abril» es vender mal: en
   la mitad que más importa, el cliente **ya estaba incumpliendo antes**.

⚠️ **Lo que no cambia:** si el despliegue construye plantillas de identificación por voz, o toca **Illinois**
(**BIPA**, consentimiento escrito, daños estatutarios de 1.000–5.000 USD por violación), el encuadre del pase 16
aplica entero. El **gap 28** se mantiene abierto con esta precisión incorporada.


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

### La vía de entrada deja de ser sólo PHP, y el lado LMS sigue vacío — agregado en el pase 24 del 2026-10-01

**Sexto pase sin agentes nuevos** (la tabla principal sigue en 37 filas reales, sin relleno), pero el barrido por
**estándar instalado** —la consigna que dejó el pase 23— destapó un sesgo de esta KB que afectaba a tres patrones:
**toda la capacidad LTI registrada era PHP**, porque la KB sólo había encontrado `1EdTech/lti-1-3-php-library`.

| Nombre | Repo | Licencia | ★ | Forks | Lenguaje | Qué es | Región |
|---|---|---|---|---|---|---|---|
| java-lti-1.3 | https://github.com/UOC/java-lti-1.3 | **MIT** ✅ | 21 | 14 | Java | Librería **LTI Advantage** completa, v**1.0.0**. La de más tracción de la familia UOC | EMEA (Universitat Oberta de Catalunya, Barcelona) |
| spring-boot-lti-advantage | https://github.com/UOC/spring-boot-lti-advantage | **MIT** ✅ | 16 | 17 | Java | LTI Advantage para **Spring Boot**: Spring Security valida los *launches* y trae `RestTemplate` de **AGS** (Line Item, Result, Score), **NRPS** y *Deep Linking* por el *launch* OIDC | EMEA (UOC) |
| java-lti-1.3-platform | https://github.com/UOC/java-lti-1.3-platform | ⚠️ **sin licencia declarada** | 0 | 1 | Java | *«Library that **will** implement a full LTI Advantage platform»* — **el lado LMS**. El tiempo futuro del README es el dato: es intención | EMEA (UOC) |
| lti-1-3-php-library (Packback) | https://github.com/packbackbooks/lti-1-3-php-library | **Apache-2.0** ✅ | 53 | 25 | PHP | Segundo *tool provider* LTI 1.3 en PHP, **1.038 commits**. **Independiente** del de 1EdTech, no un fork | North America (Packback, Chicago) |
| OpenAssessmentsClient | https://github.com/gnowledge/OpenAssessmentsClient | **Apache-2.0** ✅ | 0 | 3 | JavaScript (React) | Cliente **QTI 1.x y 2.x**. **No es QTI 3**: para QTI 3 sigue siendo `amp-up-io/qti3-item-player`, el único artefacto certificado por 1EdTech de esta KB | APAC (gnowledge) |

🔴 **El asterisco, y es el que hay que levantar en el *discovery*.** De los 14 repos LTI de la UOC, **13 son *tool-side***
—construyen la herramienta que entra al LMS— y **el único *platform-side* no declara licencia y dice que «implementará»**.
Lo mismo vale para todo lo que esta KB registró en nueve pases: es capacidad de **entrar** a un LMS, no de **ser** uno.
**Si el engagement pide el lado plataforma, esta KB no tiene con qué y hay que decirlo antes de la propuesta, no después.**

**Por qué entran con 21 y 16 estrellas.** Es código que una universidad pública europea usa en su propio campus — el mismo
criterio por el que el pase 22 aceptó `tutor-contrib-aspects` con 14 ★. Para un cliente de educación superior europea con
stack Java/Spring, **la alternativa era meterle PHP al diagrama por una limitación de esta base de conocimiento.**

⚠️ **Corrección de procedencia verificada en este pase.** La hipótesis natural —que la librería de 1EdTech fuera una
donación de Packback y que esta KB apuntara al *fork*— **es falsa**: el README de 1EdTech dice que *«This library was
initially created by @MartinLenord from **Turnitin**»*. Son dos librerías PHP independientes, las dos Apache-2.0. La fila
de la KB está bien apuntada; lo que faltaba era saber que hay una segunda, que importa para decidir dónde abrir un *issue*.


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
| https://github.com/anthropics/k12-teacher-skills | **Educación** | **Apache-2.0** ✅ | **541** | 4 skills K-12 **+ carpeta `evals/`**. «Skills and eval rubrics for K-12 teachers, co-developed with Learning Commons». *Agregado en el pase 17 — nuevo techo permisivo del canal educativo* |
| https://github.com/learning-commons-org/agent-skills | **Educación** | **Apache-2.0** ✅ | 35 | Las mismas 4 skills del lado del consorcio, con `evals/` de rúbricas de pedagogía, rigor, formato y andamiaje. *Agregado en el pase 17* |

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

---

## Capa de lectura oral y pronunciación — agregada en el pase 14 del 2026-10-01

Trece pasadas construyeron agente, modelado, evaluación, seguridad, telemetría, datos, accesibilidad, credenciales,
contenido, predicción, *skills* y práctica. **Todas asumieron que el alumno escribe.** En alfabetización inicial —y en
enseñanza de idiomas, que es el otro gran mercado de esta vertical— lo que se evalúa es que el alumno **hable**.

| Pieza | Repo | Licencia | ★ | Qué mide |
|---|---|---|---|---|
| **OpenPronounce** | [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | **MIT** ✅ | **85** | Fonema a fonema contra el texto esperado: puntaje 0-100, *phoneme error rate*, *word error rate*, confianza por palabra (0-1), distancia acústica por DTW, prosodia (F0 y energía). Wav2Vec2 + XLSR por idioma. **Local, sin API key ni nube** |
| **speechocean762** | [`jimbozhang/speechocean762`](https://github.com/jimbozhang/speechocean762) | ⚠️ **sin `LICENSE`** | **198** | Corpus de referencia: 5.000 oraciones, **mitad de hablantes son niños**, L1 mandarín. Exactitud, completitud, **fluidez** y prosodia en tres niveles |
| **Kaldi** | [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | **Apache-2.0** ✅ | **15.5k** | ASR genérico de grado industrial. Base de los tutores de lectura de la literatura. **No es educativo** |
| **Carrera Lectora** | [`vilcaaguilerandrea-oss/carrera-lectora`](https://github.com/vilcaaguilerandrea-oss/carrera-lectora) | 🔴 **SIN LICENCIA** | **0** | PWA chilena, 1.º-4.º básico: **PPM y exactitud** sobre 40 textos graduados, pedagogía intercultural, Web Speech API en dispositivo, sin telemetría. **No reutilizable** |

### Por qué OpenPronounce es la pieza vendible y no el corpus ni Kaldi

Tiene **85 ★** —no es tracción— pero es la única de la capa que cumple las cuatro condiciones a la vez: **licencia
permisiva** (MIT), **métrica que un docente entiende** (fonema mal pronunciado, con transcripción IPA), **ejecución
local** —que es lo que vuelve proponible un despliegue con menores de edad bajo Anexo III del EU AI Act y bajo los
estatutos de privacidad estudiantil de EE. UU.— y **cobertura multilingüe** por XLSR.

**El posicionamiento comercial es explícito en el propio repo: es la alternativa autoalojada a Azure Pronunciation
Assessment.** Eso es exactamente el tipo de sustitución que esta vertical sabe vender: el incumbente es un servicio
de nube por uso, y el reemplazo es un componente MIT que corre en la infraestructura del cliente.

### 🔴 Lo que esta capa no tiene, y es el gap que abre el pase 14

**Ningún agente de los 31 de la tabla principal tiene entrada ni salida de voz.** Se verificó contra la tabla: ni
DeepTutor, ni Educhain, ni OpenTutor, ni OpenTutorAI-CE, ni Bloom. **La capa de habla y la capa de agente no se
tocan** — y tampoco hay ningún servidor MCP que exponga evaluación de pronunciación, aunque el patrón MCP ya está
probado en esta KB (ver `bncc-mcp`, abajo, del mismo pase). Es el gap 24.

**Y para español y portugués no hay nada utilizable.** `carrera-lectora` es pedagógicamente lo más fino de la región
—y no tiene licencia—; el corpus de referencia es inglés con L1 mandarín. **~600 millones de hablantes sin pieza
permisiva de evaluación de fluidez.**

---

## Capa de puente agente↔currículo nacional — agregada en el pase 14 del 2026-10-01

El gap 15 (pase 10) decía que *«ningún puente agente↔contenido curricular tiene tracción, y el único que existe
declara mal la licencia de lo que sirve»*. **Este pase encuentra el puente que faltaba, es MIT, y es de LATAM.**

| Pieza | Repo | Licencia | ★ | Qué expone |
|---|---|---|---|---|
| **bncc-mcp** | [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) | **MIT** ✅ | **14** | Servidor **MCP** de la BNCC brasileña, cinco herramientas: `bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_mapa_de_foco`, `bncc_estatisticas`. **1.717 habilidades** (1.408 Fundamental, 104 Infantil, 205 Médio), 141 de Computação por ejes, y **396 habilidades priorizadas por el Mapa de Foco del Instituto Reúna** con capa pedagógica |
| **curriculum-bncc** | [`aprincar/curriculum-bncc`](https://github.com/aprincar/curriculum-bncc) | ⚠️ **AGPL-3.0** | **0** | *Crosswalk* de IDs propios a referencias BNCC con cuatro relaciones: `direct`, `partial`, `supports`, `prerequisite`, validado contra catálogos versionados |

**Lo que hace valioso a `bncc-mcp` no es el currículo: es el Mapa de Foco.** Exponer 1.717 habilidades por MCP es
un trabajo de ingeniería; exponer **cuáles 396 son prioritarias y con qué capa pedagógica** es un **juicio curricular
de una institución** (Instituto Reúna). Eso es la clase de activo que un cliente no puede generar solo y que ningún
modelo puede inventar sin alucinar. **Con 14 ★ no es tracción — es la pieza que faltaba, y está en la región de origen
de Globant.**

⚠️ **`curriculum-bncc` es AGPL-3.0 y tiene 0 ★:** sirve como referencia de **cómo modelar** un *crosswalk* (los cuatro
tipos de relación son el diseño correcto), **no como dependencia** de un producto comercial.

---

## Capa de autoría y procedencia — agregada en el pase 15 del 2026-10-01

La KB tenía media capa de integridad académica desde el pase 8: **proctoring, y registrado como roadmap**. Esta es
la otra mitad —**cómo se prueba quién escribió el trabajo**— y es la pregunta que todo cliente hace primero.
Son tres familias de herramienta. **Las tres son permisivas. Sólo dos sirven.**

### Familia 1 — marcado en el origen (*watermarking*): es lo que cumple el Artículo 50, y la KB lo vendía sin tenerlo

| Pieza | Repo | Licencia | ★ | Qué hace |
|---|---|---|---|---|
| **SynthID-Text** | `huggingface/transformers` → `src/transformers/generation/watermarking.py` | **Apache-2.0** ✅ | viaja en Transformers | Marcado **y** detección en el mismo paquete. Clases verificadas en el archivo: `SynthIDTextWatermarkLogitsProcessor`, `SynthIDTextWatermarkDetector`, `BayesianDetectorModel`, `BayesianDetectorConfig`, `BayesianDetectorWatermarkedLikelihood`. Copyright **HuggingFace + Google DeepMind** |
| **MarkLLM** | [`THU-BPM/MarkLLM`](https://github.com/THU-BPM/MarkLLM) | **Apache-2.0** ✅ | **1.100** | **23+ algoritmos** de watermarking y **12 herramientas de evaluación** (detectabilidad, robustez, impacto en calidad del texto). EMNLP 2024 Demo. 95 forks, 185 commits |

**Cuál usar y por qué.** **SynthID-Text** es el de producción: no agrega un proveedor, agrega un
`WatermarkingConfig` a la llamada de generación que el proyecto ya hace. **MarkLLM** es la herramienta de
**evaluación y comparación** — es con lo que se demuestra, en un expediente de conformidad, que el marcado
elegido es *«effective, interoperable, robust and reliable»* como pide el Artículo 50(2). Se usan los dos:
uno marca, el otro prueba que el marcado aguanta.

### Familia 2 — procedencia del artefacto (C2PA): el estándar que el Code of Practice europeo canonizó

| Pieza | Repo | Licencia | ★ | Commits | Qué hace |
|---|---|---|---|---|---|
| **c2pa-rs** | [`contentauth/c2pa-rs`](https://github.com/contentauth/c2pa-rs) | **MIT *y* Apache-2.0** (dual) ✅ | **424** | **1.907** | SDK Rust del core C2PA: crear, firmar, validar e incrustar manifiestos de procedencia. Claims **C2PA v2**, spec **2.4**, *CAWG identity assertion*, API en C |
| **c2pa-python** | [`contentauth/c2pa-python`](https://github.com/contentauth/c2pa-python) | **Apache-2.0 *y* MIT** (dual) ✅ | 105 | 344 | Binding Python, **3.10+**. Es la vía realista para un pipeline educativo que ya es Python |

**Por qué esto no es opcional en EMEA.** El **Code of Practice** europeo sobre marcado y etiquetado de contenido
generado por AI —voluntario, pero la vía más clara para demostrar cumplimiento del Artículo 50— **adopta las
*Content Credentials* de C2PA como estándar técnico de facto** del metadato incrustado, en un esquema **por
capas: metadato + watermarking**, con *fingerprinting* y *logging* como medidas de apoyo. Las familias 1 y 2 **no
son alternativas: son las dos capas del mismo esquema.**

### Familia 3 — detección forense: real, permisiva, publicada en ICLR/ICML/ACL, y no se puede usar para acusar

| Repo | Licencia | ★ | Qué es |
|---|---|---|---|
| [`baoguangsheng/fast-detect-gpt`](https://github.com/baoguangsheng/fast-detect-gpt) | **MIT** ✅ | **434** | **ICLR 2024**. Zero-shot por curvatura de probabilidad condicional, **340× más rápido que DetectGPT**. AUROC **0,9887** (5 modelos) / **0,9338** (ChatGPT/GPT-4) |
| [`ahans30/Binoculars`](https://github.com/ahans30/Binoculars) | **BSD-3-Clause** ✅ | **420** | **ICML 2024**. Zero-shot sin datos de entrenamiento; dos modelos de pesos abiertos en inferencia |
| [`liamdugan/raid`](https://github.com/liamdugan/raid) | **MIT** ✅ | **216** | **ACL 2024**. El benchmark: **10M+ documentos**, 11 LLMs, 11 dominios, 4 decodificaciones, **12 ataques adversarios**. Leaderboard `raid-bench.xyz` |
| [`NLP2CT/LLM-generated-Text-Detection`](https://github.com/NLP2CT/LLM-generated-Text-Detection) | **MIT** ✅ | **252** | Survey vivo, ~100+ papers y 17+ datasets. *Computational Linguistics* **51(1), 2025** |
| [`pablocaeg/sloptotal`](https://github.com/pablocaeg/sloptotal) | **MIT** ✅ | 39 | Ensamble de **23 motores** auto-hospedado que **corre en CPU** (incluye Fast-DetectGPT y Binoculars). Acepta texto, PDF, DOCX y URLs |
| [`Lendarixon/awesome-ai-detection`](https://github.com/Lendarixon/awesome-ai-detection) | **CC0-1.0** ✅ | 0 | Catálogo con los **modos de falla medidos** |
| [`yonatanlop/detectoria`](https://github.com/yonatanlop/detectoria) | 🚫 **Sin licencia** | 0 | El único detector pensado para **español**: estilometría + perplejidad con `mrm8488/spanish-gpt2` + rank/entropía estilo GLTR + traducción `Helsinki-NLP/opus-mt-es-en` con `roberta-base-openai-detector`. **No proponerlo** |

### 🔴 Antes de poner cualquier cosa de la familia 3 en un entregable

| Medición | Valor |
|---|---|
| FPR sobre escritura de **no nativos de inglés** (TOEFL, 7 detectores) | **61,3 %** |
| FPR sobre universitarios **nativos**, mismos detectores | ~2,9 % |
| FPR sobre 1.180 abstracts académicos **anteriores a 2018** | **5,85 %** + 20 % «incierto» |
| Umbral de longitud por debajo del cual el score no sirve | **~80 palabras**; estabiliza en ~200 |
| Efecto de la paráfrasis | **caídas grandes de exactitud** (RAID) |

**Binoculars lo dice en su propio README:** *«more proficient in detecting English language text compared to other
languages»*, *«for academic purposes only»*, con **supervisión humana** requerida.

**La regla, y vale para toda la KB:** un score de detección es **evidencia, no prueba**. Sirve para **priorizar una
conversación docente**; nunca para disparar una sanción automática. Sobre alumnos que escriben inglés como segunda
lengua —el alumno modal de LATAM, de EMEA no anglófona y de buena parte de APAC— el **61,3 %** convierte la
herramienta en **pasivo legal antes que en producto**. Vanderbilt lo resolvió con una cuenta: 1 % de FPR sobre
75.000 trabajos son **~750 acusaciones injustas por año**, y desactivó el detector. **Más de 50 universidades**
de EE. UU., Reino Unido, Canadá, Australia y Sudáfrica hicieron lo mismo. Ver el **gap 25**.

### La pieza que cambia la arquitectura, y es una pregunta distinta

*«¿Esto lo escribió una AI?»* no tiene respuesta confiable y no la va a tener. *«¿Esto lo escribió **nuestro**
tutor?»* **sí la tiene**, y es una verificación criptográfica, no una estimación. **La institución que provee el
agente puede marcar su salida en el origen.** Eso saca la integridad del terreno forense y la mete en el terreno
de la procedencia, donde el stack es Apache-2.0 y está maduro. Es el patrón **P33**, y es la misma forma que la
tendencia 29 describe para otras cinco capas de esta KB.

⚠️ **Y el límite honesto del marcado:** sólo cubre texto que generó **tu propio sistema**. No resuelve el ensayo
escrito con un modelo de fuera de la institución. Lo que hace es convertir un problema sin solución —detección
universal— en uno con solución parcial pero **cierta**, más un régimen de **declaración** para el resto. En LATAM
ese régimen **ya es la norma legal** (ver `intel/market.md`), y por eso ahí el stack alcanza hoy.

### El puente que no existe, y es el gap barato de este pase

**Ninguna de las nueve piezas de arriba tiene integración educativa.** No hay plugin de LMS, herramienta LTI ni
servidor MCP que marque o verifique la salida de un tutor. Lo que existe en el directorio de Moodle son
**envoltorios de servicios propietarios**: Compilatio (plugin **GPL-3.0**, 821 instalaciones, release 2026-06-25),
Originality.ai (Moodle 3.9–5.0, release 2026-07-02) y Copyleaks — plugin libre, **detector pago**. El puente es
trabajo de días sobre infraestructura Apache-2.0. Ver **P33** y el **gap 25**.


## Postura de privacidad de los agentes — agregada en el pase 16 del 2026-10-01

Se revisó la tabla principal agente por agente buscando una declaración de **qué hace con el dato del alumno**:
dónde lo guarda, si lo usa para entrenar, si se puede desplegar sin que el dato salga de la institución.

**Ninguno de los 31 la tiene.** No es que declaren una política mala — no declaran ninguna. Lo más cercano es la
capa de memoria (DeepTutor tiene memoria en tres capas, `learnmcp-xapi` persiste contra un LRS), que describe
**dónde** queda el dato pero nunca **bajo qué base legal** ni con qué retención.

**Por qué importa ahora y no antes:**

| Régimen | Qué exige | Estado |
|---|---|---|
| **COPPA enmendada** (North America) | Biométricos —**voiceprints**, faceprints, huellas— son información personal; consentimiento parental verificable; política escrita de retención y borrado; prohibida la retención indefinida | 🔴 **Cumplimiento exigible desde 2026-04-22** |
| **FERPA** (North America) | El dato cedido al proveedor sólo sirve para el fin cedido; **entrenar modelos comerciales generales con él es violación** | Vigente |
| **GDPR Art. 35** (EMEA) | **DPIA obligatorio** antes de usar la herramienta; EDPB pide *balancing test* documentado | Vigente |
| **DPDP Act § 9** (APAC, India) | Consentimiento parental verificable; sin seguimiento conductual; hasta **₹200 crore** por infracción con datos de menores | Vigente |
| **LGPD Art. 14 + ECA Digital** (LATAM, Brasil) | Consentimiento específico y destacado de un responsable; informes semestrales de impacto a la ANPD para plataformas con +1M de usuarios menores | Vigente |

**La consecuencia práctica, y es un criterio de selección nuevo para esta KB:** cuando un agente de la tabla se
proponga para menores, la postura de privacidad **hay que construirla en el proyecto** — no viene con el repo. El
presupuesto de un despliegue educativo con datos reales incluye esa capa, y hasta este pase esta KB la daba por
gratis. Las piezas están en `repos/foundations.md` y el wiring en **P34** y **P35**.

## Capa de borrado efectivo — agregada en el pase 18 del 2026-10-01

El **gap 29** (pase 17) pedía una pieza concreta: *«ningún `privacy provider` de referencia para un plugin de AI,
que es justamente lo que el núcleo de Moodle exige de cualquier plugin que guarde dato del alumno»*. **Existe, y no
la escribió un tercero: la escribió Moodle.** El núcleo trae **tres** implementaciones de referencia, una por cada
proveedor de AI que embute. El gap se cierra, y se cierra con la pieza más defendible posible ante un cliente: la
del propio vendor.

### 🔴 El hallazgo del pase: la referencia estaba en el núcleo, y el pase 17 no la vio por una razón mecánica

El pase 17 dejó escrito que intentó el árbol de `admin/tool/dataprivacy` dentro de `moodle/moodle` *«por cuatro
rutas (`main` y `master`, árbol y archivo) y las cuatro dieron 404»*, y por eso registró el Privacy API como
**documentado por snippet, no verificado de primera mano**. La causa es trivial y conviene dejarla escrita porque
afecta a cualquier pase futuro:

> 🔴 **[FALSO — refutado en el pase 19, ver abajo]** **`moodle/moodle` no tiene rama `main` ni rama `master`.** Sus ramas son `MOODLE_XXX_STABLE`. Cualquier fetch
> contra `main` o `master` da 404 **con independencia de que el archivo exista**. Los cuatro 404 del pase 17 no
> midieron ausencia: midieron el nombre de la rama.

Verificado en este pase por código HTTP contra `raw.githubusercontent.com`, rama por rama:

| Ruta en `moodle/moodle` | `main` | `master` | `MOODLE_405_STABLE` | `MOODLE_500_STABLE` |
|---|---|---|---|---|
| `ai/provider/openai/version.php` | 404 | 404 | **200** | **200** |
| `ai/provider/openai/classes/privacy/provider.php` | 404 | 404 | **200** | **200** |
| `admin/tool/dataprivacy/version.php` | — | — | — | **200** |
| `admin/tool/policy/version.php` | — | — | — | **200** |

**Entonces se corrige el registro de evidencia del pase 17:** el Privacy API, `tool_dataprivacy` y `tool_policy`
pasan de *«documentados por snippet»* a **verificados de primera mano en el núcleo**.


### 🔴 CORRECCIÓN DEL PASE 19 (2026-10-01) — la rama existe, y la causa real es mejor que la que se escribió

**Lo de arriba es falso en su premisa y hay que leerlo con esta corrección puesta.** Verificado con `git ls-remote`
—que lista refs, no adivina— y después con un clon *sparse* del árbol real:

```
$ git ls-remote --heads https://github.com/moodle/moodle | grep -v 'MOODLE_[0-9]*_STABLE$'
85af0b5dc354bf03c73db60079c232f004e01433    refs/heads/main
```

> **`moodle/moodle` SÍ tiene rama `main`,** y apunta a `85af0b5` = **Moodle 5.3rc1**. Lo que no tiene es `master`.

**Y la causa real de los 404 es más útil que la falsa, porque se repite:** **Moodle movió su *webroot* al
subdirectorio `public/` en la serie 5.x.** En `main` no existe `ai/` en la raíz; existe `public/ai/`. Por eso
`ai/provider/openai/version.php` da 404 en `main` **y** 200 en `MOODLE_405_STABLE` y `MOODLE_500_STABLE`: en esas
ramas `ai/` todavía estaba en la raíz. **La tabla de evidencia del pase 18 es correcta; su explicación no.** Los 404
midieron **la ruta**, no el nombre de la rama — y cualquier referencia a rutas de Moodle que esta KB escriba tiene
que decir contra qué serie se resolvió, porque la 5.x las movió todas.

**Lo que hay que corregir del conteo y de la lista:**

| Lo que escribió el pase 18 | Lo verificado en el pase 19 (clon sparse de `main` = 5.3rc1) |
|---|---|
| «El núcleo trae **tres** implementaciones» | **Siete** proveedores con `privacy/provider.php`, más **1** del subsistema (`core_ai`) y **2** de *placement* = **10 archivos** |
| `ai/provider/bedrock` → «404, no está en el núcleo» | **Sí está**, y el nombre es `awsbedrock`, no `bedrock`. El 404 midió el nombre |
| `ai/provider/anthropic` → «404, no está en el núcleo» | **Sí está**: `public/ai/provider/anthropic/classes/privacy/provider.php` |

Los siete, auditados uno por uno sobre el fuente:

| Proveedor (`public/ai/provider/…`) | Líneas | `delete_records` / `DELETE FROM` / `add_database_table` | `add_external_location_link` |
|---|---|---|---|
| `anthropic` | 78 | **0** | 1 |
| `awsbedrock` | 76 | **0** | 1 |
| `azureai` | 77 | **0** | 1 |
| `deepseek` | 70 | **0** | 1 |
| `gemini` | 77 | **0** | 1 |
| `ollama` | 74 | **0** | 1 |
| `openai` | 76 | **0** | 1 |

**Lo que el pase 18 sí acertó, y conviene no perderlo en la corrección:** su lectura de que los métodos vacíos son
*«vacíos a propósito»* y que ésa es la forma correcta para un plugin que sólo transmite **es exacta**, y la
verificación de este pase la confirma (los siete, idénticos, con `@codeCoverageIgnore`). Lo que estaba mal es el
titular: **siete shims de declaración no son «implementaciones de referencia» de un `privacy provider`**, porque lo
que un plugin que guarda dato necesita copiar es precisamente lo que ellos no tienen.

### ✅ La plantilla real, que el pase 18 no nombró: `core_ai`

`public/ai/classes/privacy/provider.php` — **~800 líneas**, y es el artefacto que el **gap 29** pedía:

- **6 tablas declaradas** en `get_metadata()`: `ai_policy_register`, `ai_action_register`,
  `ai_action_generate_image`, `ai_action_generate_text`, `ai_action_summarise_text`, `ai_action_explain_text`.
  Entre sus campos están **`prompt`**, **`generatedcontent`**, `responseid`, `fingerprint`, `prompttokens`,
  `completiontokens`, `model` y `courseid`.
- `get_contexts_for_userid()` con **SQL real** (5 consultas, una por tipo de acción), no un `contextlist` vacío.
- `export_user_data()` que escribe de verdad vía `writer::with_context()`.
- **Borrado real** en las tres variantes: `delete_data_for_user()` (:496), `delete_data_for_users()` (:695) y
  `delete_data_for_all_users_in_context()` (:378), con `delete_records_list()`.

**Eso es lo que hay que copiar en un plugin de AI que guarde dato del alumno** (ver **P39**, que mejora con esto), y
lo que hay que citar ante un cliente cuando pregunte si Moodle sabe borrar lo que su AI generó. Los dos *placement*
(`courseassist`, `editor`) son `null_provider`: declaran explícitamente que no guardan nada.

**El hallazgo de encuadre, que es el que viaja a `intel/trends.md`:** la línea divisoria dentro del propio núcleo de
Moodle no es técnica, es de **arquitectura de dato**. `core_ai` guarda el prompt y la respuesta y por eso sabe
borrarlos. Los siete proveedores **no guardan: transmiten** — y lo único que pueden hacer es declararlo. El núcleo
documenta así, en siete archivos idénticos, **el punto exacto donde su maquinaria de supresión se queda sin nada que
suprimir**, porque el dato ya está en OpenAI, Anthropic, Google, AWS, Azure, DeepSeek o en el Ollama de alguien. Ver
la tendencia **48**.

### ~~Las tres referencias del núcleo~~ — ⚠️ SUPERADA POR EL PASE 19: son siete, y ninguna de las siete es la plantilla (se conserva por la cadena de idioma de `ollama`, que sigue siendo válida y citable)

Verificadas leyendo el archivo fuente, no la página del repo. Las tres implementan las mismas tres interfaces
—`metadata\provider`, `request\core_userlist_provider`, `request\plugin\provider`— con `#[\Override]`, copyright
**2024 Matt Porritt (moodle.com)**, licencia **GPL-3.0-or-later**:

| Proveedor en el núcleo | ¿Trae `privacy/provider.php`? | Qué declara `get_metadata()` |
|---|---|---|
| `ai/provider/openai` | ✅ **200** | `add_external_location_link` con `prompttext`, `model`, `numberimages`, `responseformat` |
| `ai/provider/azureai` | ✅ **200** | ídem patrón |
| `ai/provider/ollama` | ✅ **200** | `add_external_location_link` con `prompttext`, `model` |
| `ai/provider/bedrock` | 🚫 **404** — no está en el núcleo | — |
| `ai/provider/anthropic` | 🚫 **404** — no está en el núcleo | — |

**El patrón canónico, y es contraintuitivo:** los seis métodos de export y borrado están **vacíos a propósito**, y
`get_contexts_for_userid()` devuelve un `contextlist` vacío. No es código sin terminar. Es la forma correcta para un
plugin que **no guarda nada localmente y sólo transmite**: lo único que tiene que declarar es el envío externo. Un
plugin de AI que *sí* guarde —un log de uso, una nota, una conversación— **no puede copiar esta forma**: tiene que
implementar los seis.

### 🔴 La línea que hay que leer antes de poner cualquiera de las tres en un expediente de privacidad

`aiprovider_ollama` es el caso que importa, porque es el que un cliente elige **justamente** para que el dato no
salga. Y aun así el núcleo le declara un envío externo. La cadena de idioma, citada literal:

> `privacy:metadata` → «The Ollama API provider plugin does not store any personal data.»
>
> `privacy:metadata:aiprovider_ollama:externalpurpose` → «This information is sent to the Ollama API in order for a
> response to be generated. Your Ollama account settings may change how Ollama stores and retains this data. **No
> user data is explicitly sent** to Ollama or stored in Moodle LMS by this plugin.»

**La palabra que carga el peso es «explicitly».** El plugin no adjunta identidad —no manda `userid`, ni nombre, ni
email— y en ese sentido la frase es verdadera. Pero `prompttext` **sí** se declara como lo que viaja, y el prompt
lleva lo que el alumno escribió, que puede ser cualquier cosa. **La declaración del núcleo es exacta sobre la
identidad y silenciosa sobre el contenido.** En un expediente de privacidad (ver **P35**) esa distinción se escribe
en una línea y evita la discusión entera: *«el plugin no envía identificadores; el cuerpo del prompt no está
acotado por el plugin y su contenido es responsabilidad de la actividad que lo construye»*.

### Lo que la comunidad construyó arriba, y sólo tres piezas de seis tienen `privacy/provider.php`

Verificado abriendo `classes/privacy/` en cada repo. Ordenado por completitud de la implementación, no por estrellas.

| Pieza | Repo | Licencia | ★ | Interfaces en `privacy/provider.php` | Región del autor | Nota |
|---|---|---|---|---|---|---|
| **local_aihub** | https://github.com/jeanlucio/moodle-local_aihub | **GPL-3.0** ⚠️ | 0 (1 fork, 60 commits) | **Cuatro** — `metadata\provider`, `core_userlist_provider`, `plugin\provider` y **`user_preference_provider`** | **LATAM** — Jean Lúcio, **Instituto Federal do Sertão Pernambucano, Brasil** | **La implementación más completa de la capa, y es la única que declara las tres cosas a la vez:** tabla de base (`local_aihub_log`, 9 columnas), **6 preferencias de usuario** y **4 enlaces externos** (`deepseek`, `google_gemini`, `groq`, `openai_compatible`). Broker BYOK con *SSRF guard*, escalera de proveedores y *key store*; «the hub never contacts a provider on its own»; la API key es opcional y el plugin instala y funciona sin ninguna. Trae `.github/workflows/`, `tests/` y `docs/` |
| **aiprovider_gemini** | https://github.com/Universita-di-Ferrara/moodle-aiprovider_gemini | **GPL-3.0** ⚠️ | 3 (3 forks, 12 commits) | Tres — las mismas del núcleo | **EMEA** — Andrea Bertelli, **Università di Ferrara, Italia** | Moodle **4.5+**; v2.2.0 agrega Gemini 3 e imagen nativa. **Es una adaptación casi literal del `provider.php` del núcleo**: mismos cuatro campos (`prompttext`, `model`, `numberimages`, `responseformat`), misma estructura, y el docblock **todavía dice «Privacy provider implementation for OpenAI provider»**. No es una crítica: es la prueba de que el patrón del núcleo es el que la comunidad copia, y de que copiarlo funciona |
| **mod_aigradedassign** | https://github.com/alvarogregori/moodle-ai-graded-assignment | 🚫 **sin archivo `LICENSE`** — el header del fuente dice GPL-3.0-or-later | 0 (0 forks, 14 commits) | Tres — `metadata\provider`, `plugin\provider`, `core_userlist_provider` (`final class`) | No declarada en el perfil | Actividad de entrega en texto plano con feedback automático (Mistral, OpenAI, Anthropic, endpoints compatibles, y un *mock* determinista local). **Es el único de la capa que corre sobre dato de alumno de verdad** y lo declara: con proveedor remoto salen «the student submission, activity instructions, private rubric, and private evaluated examples». Gate de validación docente: el resultado de la AI **no afecta nota ni compleción hasta que un tutor aprueba o edita** — el diseño de **P18**. ⚠️ **Tercer caso de licencia de esta KB:** no está en el sidebar ni en el README, sólo en el header del archivo. Ver la advertencia de método abajo |
| **ai-moodle-security** | https://github.com/sngdtechnologies/ai-moodle-security | **BSD-2-Clause** ✅ | 0 (0 forks, 103 commits) | 🚫 **No tiene `classes/privacy/`** | No declarada (autor: SOB NGHAMI Gilles Descartes; prototipo de tesis de maestría) | **La única licencia permisiva de la capa, y la única pieza sin privacy provider.** No es un plugin: es una **arquitectura de despliegue** — Phi-3-mini vía Ollama 100% on-site, 7 contenedores, 5 redes Docker, sólo el proxy expuesto (443), Moodle y Ollama en redes internas **sin egreso a internet**, Caddy + WAF Coraza (OWASP CRS). Vale por el diagrama de red, no por el código |
| **tool_aiconnect** | https://github.com/marcusgreen/moodle-tool_aiconnect | 🚫 licencia no mostrada | 10 (4 forks, 37 commits) | 🚫 No se vio directorio `privacy/` | **EMEA** — nota de consultoría a **Catalyst EU** (Moodle Partner) | Fork de `local_ai_connector` para múltiples proveedores LLM incluido Ollama; quita generación de imagen; se integra con `moodle-qtype_aitext` |
| **tool_dataprivacy** (el repo) | https://github.com/moodlehq/moodle-tool_dataprivacy | **GPL-3.0** ⚠️ | 8 (11 forks, 199 commits) | — (es la máquina, no un plugin de AI) | EMEA — `moodlehq` | 🔴 **ARCHIVADO el 2020-09-24, read-only.** No está muerto: **se mudó al núcleo**. Moodle 3.3.8 / 3.4.5 / 3.5 y posteriores ya lo traen de fábrica, y por eso `admin/tool/dataprivacy/version.php` da 200 en `MOODLE_500_STABLE`. **No proponer este repo como dependencia** — proponer la versión del núcleo |

### ⚠️ Advertencia de método — el tercer lugar donde puede estar la licencia

Esta KB ya aprendió dos veces que la licencia no se lee donde parece. El pase 10 pasó del README al archivo
`LICENSE`; el pase 16 encontró dos casos (`diffprivlib`, `SDV`) donde el sidebar de GitHub no alcanzaba.
`mod_aigradedassign` agrega el tercero: **no hay `LICENSE`, no hay licencia en el sidebar, no hay nota en el
README — y el header de cada archivo `.php` declara GPL-3.0-or-later.** Para un plugin de Moodle eso es lo
esperable (el núcleo lo exige), pero **un header de archivo no es una concesión de licencia del repositorio**.
Regla operativa: **si no hay `LICENSE`, se trata como sin licencia a efectos de cotización**, y lo que corresponde
es abrir un *issue* pidiendo el archivo. Es el mismo movimiento de dos líneas que el pase 13 recomendó para el
gap 20.

### ⚠️ Y la nota de diseño sobre `local_aihub`, porque es la pieza que esta KB va a recomendar

El provider declara **6 preferencias de usuario** que incluyen las claves BYOK (`local_aihub_deepseek_key`,
`local_aihub_gemini_key`, `local_aihub_groq_key`, `local_aihub_openai_key`) vía `add_user_preference`. Declararlas
es **lo correcto** —son dato personal del usuario y el Privacy API las tiene que conocer—, pero tiene una
consecuencia que conviene prever: **un pedido de exportación de datos devuelve al usuario sus propias claves de
API en el export**. No es una vulnerabilidad y el diseño es honesto; es una consideración de manejo del artefacto
de export, que en un despliegue institucional circula por correo o por descarga. Se anota, no se descuenta.

---

## Capa de *unlearning* — agregada en el pase 18 del 2026-10-01

El **gap 30** (pase 17) dejó una acción textual: *«buscar procedencia de dato de entrenamiento por los términos del
dominio de ML, no de educación… **`machine unlearning` es el término que este pase no buscó** y es el que podría
tener oferta madura»*. Se buscó. **La predicción era correcta: la oferta existe, es madura y es toda permisiva.**

Y produce el contraste más limpio de esta KB. El pase 17 midió que la máquina para **borrar el registro** del
alumno está instalada en el LMS y es **toda copyleft**. Esta capa borra la otra mitad —**la influencia del dato
sobre el modelo**— y es **toda MIT o Apache-2.0**. Las dos mitades del derecho al olvido tienen licencias
opuestas, y la permisiva es la que la educación no usa.

### Lo horizontal: real, permisivo, publicado y con tracción

| Pieza | Repo | Licencia | ★ | Qué es |
|---|---|---|---|---|
| **awesome-machine-unlearning** | https://github.com/tamlhp/awesome-machine-unlearning | **MIT** ✅ | 970 (79 forks) | El mapa de la capa: artículos, metodologías y **datasets**. Respalda la survey *«A Survey of Machine Unlearning»*, **ACM TIST 2025**, DOI `10.1145/3749987` (arXiv 2209.02299). Es el punto de entrada |
| **machine_unlearning** | https://github.com/jjbrophy47/machine_unlearning | 🚫 **sin licencia declarada** | 965 (117 forks) | Literatura existente sobre *unlearning*, de pre-2017 a 2025 (AAAI, ACL, CVPR, NeurIPS). Segundo agregador por tamaño. **No muestra licencia** → bibliografía sí, dependencia no |
| **awesome-llm-unlearning** | https://github.com/chrisliu298/awesome-llm-unlearning | **Apache-2.0** ✅ | 627 (33 forks) | 616 papers, 18 surveys, 3 frameworks. Es el recorte de LLM |
| **open-unlearning** | https://github.com/locuslab/open-unlearning | **MIT** ✅ | **607** (164 forks, 90 commits, Python) | **El framework ejecutable de la capa.** Benchmarks **TOFU, MUSE, WMDP**; métodos `GradAscent`, `GradDiff`, `NPO`, `SimNPO`, `DPO`, `RMU`, `UNDIAL`, `AltPO`, `SatImp`, `WGA`, `CE-U`, `PDU`; 5+ datasets, 10+ métricas, 7+ arquitecturas. Reporte técnico arXiv **2506.12618** |
| **Unlearn-Saliency (SalUn)** | https://github.com/OPTML-Group/Unlearn-Saliency | **MIT** ✅ | 154 (29 forks) | *Weight saliency* por gradiente para *unlearning*, en clasificación **y** generación (difusión, Stable Diffusion). **ICLR 2024 Spotlight**, arXiv 2310.12508. Es el método con mejor relación resultado/costo publicado |
| **torchunlearn** | https://github.com/Harry24k/machine-unlearning-pytorch | **MIT** ✅ | 12 (2 forks, 51 commits) | *«A PyTorch library for efficient machine unlearning — make your models forget, on demand.»* Interfaz unificada estilo PyTorch sobre algoritmos del estado del arte. **NeurIPS 2025**, *«Unlearning-Aware Minimization»* (Kim et al.). **Es la pieza de esta tabla que alcanza a un modelo de *knowledge tracing*** — ver abajo |
| **model-provenance-kit** | https://github.com/cisco-ai-defense/model-provenance-kit | **Apache-2.0** ✅ | 104 (22 forks) | **Cisco AI Defense.** Toolkit y CLI en Python que determina si dos modelos comparten origen: metadatos de arquitectura, estructura del tokenizer y *fingerprints* a nivel de pesos, **8 señales agregadas en un score**. Modos `compare` (par a par) y `scan` contra una base de ~**150 modelos base de 45+ familias**. *Streaming* para modelos de +20 GB |
| **Data-Provenance-Collection** | https://github.com/Data-Provenance-Initiative/Data-Provenance-Collection | **Apache-2.0** ✅ | 281 (48 forks) | Auditoría de **44 colecciones / 1800+ datasets** de *finetuning* con metadatos de fuente, licencia y creador; genera **fichas de procedencia legibles**. arXiv 2310.16787 |

🔴 **Y una trampa de verificación que este pase casi escribe mal.** La primera búsqueda devolvió
`aflah02/open-unlearning` como el repo de la librería. **Es un fork con 0 ★ y 0 forks**; el canónico es
`locuslab/open-unlearning` con **607 ★**. Un buscador devuelve el fork y el fork se ve idéntico al original: mismo
README, misma licencia, misma lista de métodos. **Lo único que lo delata es el campo «forked from» y el contador
de estrellas en cero.** Es la misma clase de error que el pase 7 cometió con MRBench y el pase 12 con la
distribución por *skills*. Regla: **ningún repo entra a una tabla de esta KB sin mirar si es fork.**

### 🔴 El hallazgo del pase: el algoritmo que la educación necesita existe, es exactamente de su capa de *mastery*, y no publica código

Buscando *unlearning* contra educación aparece **PrivacyCD** — *«PrivacyCD: Hierarchical Unlearning for Protecting
Student Privacy in Cognitive Diagnosis»*, **arXiv 2511.03966**. Y no es un paper tangencial:

- Se declara **el primer estudio sistemático del problema de *data unlearning* para modelos de *cognitive
  diagnosis***, y los modelos de CD son **la misma capa de estimación de dominio** que esta KB viene documentando
  desde el pase 4 con `pyBKT` y `pyKT`.
- El argumento de partida es exactamente el que esta KB necesitaba verificar: *«aplicar directamente algoritmos de
  *unlearning* de propósito general es subóptimo, porque no logran balancear completitud del olvido, utilidad del
  modelo y eficiencia frente a la estructura heterogénea de los modelos de CD»*.
- Aporta **HIF** (*hierarchical importance-guided forgetting*): la importancia de los parámetros en modelos de CD
  tiene características **por capa**, y un mecanismo de suavizado combina importancia individual y de capa para
  distinguir mejor los parámetros asociados al dato a olvidar. Evaluado en **tres datasets reales**.
- Autores: Mingliang Hou, Yinuo Wang, Teng Guo, Zitao Liu, Wenzhou Dou, Jiaqi Zheng, Renqiang Luo, Mi Tian,
  Weiqi Luo.

**No se ubicó repositorio público.** Se buscó explícitamente por el nombre del método y del paper. Es el patrón
que esta KB ya nombró en la capa predictiva (pase 11) y en la de contenido (pase 10): **la pieza más específica y
más valiosa es la que no publica código.**

Hay más literatura en la misma dirección, y conviene registrarla como señal de que la categoría se está formando:
*«Making AI Forget You: Removing Educational Data from Intelligent Education Models»* (capítulo Springer, DOI
`10.1007/978-981-95-1525-7_8`), *«Exploring Fairness in Educational Data Mining in the Context of the Right to be
Forgotten»* (arXiv 2405.16798), *«Trustworthy Intelligent Education: A Systematic Perspective»* (arXiv 2601.21837)
y *«Lifting Data-Tracing Machine Unlearning to Knowledge»* (OpenReview `ScvUCNMdYN`).

⚠️ **Nivel de evidencia:** `arxiv.org` está **bloqueado por el proxy de egreso de esta sesión** (mismo bloqueo que
el gap 17; también cayeron `blogs.cisco.com` y `helpnetsecurity.com`). Los metadatos de estos papers vienen de
**snippets de búsqueda concordantes, no de la fuente primaria**. Los repos de la tabla de arriba **sí** se
verificaron de primera mano, incluida la condición de fork y la ausencia de licencia donde se declara.
No citar un número de paper en material de cliente sin abrir el PDF.

### La conclusión de ingeniería, y es la que decide qué se puede prometer

Esta KB tiene dos estimadores de *mastery* en su tabla de fundacionales, y **el *unlearning* los alcanza de forma
distinta**:

- **`pyKT` (MIT) es PyTorch.** Entonces `torchunlearn` y `SalUn` son **aplicables en principio**: hay una interfaz
  y un conjunto de pesos sobre los cuales operar. Es integración con riesgo técnico, no investigación.
- **`pyBKT` (MIT) no es un modelo PyTorch** — es BKT ajustado por EM. **Ninguna librería de esta tabla lo
  alcanza**, y la respuesta honesta para `pyBKT` **no es *unlearning*: es reajustar desde cero sin el alumno**.
  Para BKT eso es barato —pocos parámetros, EM sobre la secuencia— y además es *exact unlearning*, que es la
  garantía más fuerte que existe. **Es mejor resultado legal por menos trabajo.**

**La regla operativa, en una línea:** *si el modelo de dominio es BKT, el derecho al olvido se cumple
reentrenando y se puede probar; si es deep knowledge tracing, hay que hacer unlearning aproximado y el entregable
incluye la métrica de verificación, no sólo el borrado.*

### Lo que esta capa no tiene, por región, y es un gap informado

El barrido regional de esta capa da un resultado desparejo que conviene escribir en vez de dejar en silencio:

- **North America** — es donde vive la oferta: `locuslab` (CMU), `OPTML-Group` (Michigan State),
  `cisco-ai-defense`, `Data-Provenance-Initiative` (MIT Media Lab).
- **APAC** — la segunda concentración, y es la que tiene **lo específicamente educativo**: `torchunlearn` (Corea),
  `tamlhp` (Australia) y los autores de **PrivacyCD**. Extiende el patrón que el gap 4 viene anotando desde el
  pase 7.
- **EMEA** — 🚫 **no se encontró ninguna pieza de *unlearning*** en este barrido. Se declara **no encontrada, no
  inexistente**. Es llamativo porque EMEA es la región donde el **derecho de supresión (GDPR art. 17)** es
  directamente exigible: el régimen más fuerte del mundo y cero oferta propia de la tecnología que lo cumple.
- **LATAM** — 🚫 **no se encontró ninguna pieza de *unlearning***. Pero LATAM **sí** aporta a la otra mitad de este
  pase, y es la pieza más completa de toda la capa de `privacy provider`: **`local_aihub`, de un instituto federal
  brasileño**. Ver el **gap 2**, que este pase vuelve a mover.

Ver los **gaps 31 y 32**, las tendencias **45**, **46** y **47**, y los patrones **P38** y **P39**.


## Capa de testing de conformidad regulatoria — agregada en el pase 20 del 2026-10-01

Esta es la capa que esta KB **debía tener desde el pase 4** y no tenía. Desde entonces se vende un *expediente de
conformidad* (**P4** para el Anexo III europeo, **P10** para probar que el tutor enseña, **P11** para el gate de
seguridad pedagógica, **P17** para accesibilidad, **P39** para privacidad) y en ningún pase se registró **con qué
herramienta se corre la prueba**. La respuesta es que la herramienta existe, está madura, es permisiva, y la publican
reguladores.

**Verificado repo por repo vía WebFetch el 2026-10-01.** Nueve repos, todos reales, licencia leída en la página del
repo:

| Repo | Licencia | ★ | Forks | Qué es, y qué prueba |
|---|---|---|---|---|
| https://github.com/UKGovernmentBEIS/inspect_ai | **MIT** ✅ | 2.900 | 763 | **Lo más grande y más limpio de la capa.** Framework de evaluación de LLMs del **UK AI Security Institute** (organismo del gobierno británico). Trae **200+ evaluaciones** pre-construidas, *prompt engineering*, uso de herramientas, diálogo multi-turno y *model-graded evals*. Python |
| https://github.com/aiverify-foundation/moonshot | **Apache-2.0** ✅ | 353 | 70 | **La pieza central para un agente educativo.** *Benchmarking* **y** *red-teaming* en una sola herramienta, de la **AI Verify Foundation** (Singapur). Implementa el **Starter Kit de IMDA** como *cookbooks* pre-armados. Web UI + CLI. Python, v0.7.6 (**beta**), 2.153 commits |
| https://github.com/compl-ai/compl-ai | **Apache-2.0** ✅ | 211 | 37 | **La contraparte EMEA, y la única mapeada al AI Act.** Framework de evaluación organizado sobre **6 principios núcleo del EU AI Act** y sus requisitos técnicos, con **29 benchmarks** (y creciendo). De **ETH Zürich + INSAIT + LatticeFlow AI**, construido sobre Inspect. Python, 333 commits |
| https://github.com/aiverify-foundation/aiverify | **Apache-2.0** ✅ | 97 | 31 | La plataforma de *governance testing* de AI Verify: tests estandarizados contra principios reconocidos internacionalmente. ⚠️ **Lee con cuidado el alcance: evalúa modelos de aprendizaje supervisado sobre datos tabulares e imágenes**, no agentes LLM. v2.0 modular, 3.035 commits |
| https://github.com/aiverify-foundation/moonshot-data | **Apache-2.0** ✅ | 45 | 41 | Los *assets* de Moonshot: conectores (OpenAI, Anthropic, Together, HuggingFace), *datasets* (BigBench, CyberSecEval de PurpleLlama, benchmarks de tamil, **Medical LLM**, **AILuminate v1.0 DEMO** vía MLCommons), métricas, *attack modules*, *cookbooks* y plantillas de prompt |
| https://github.com/aiverify-foundation/LLM-Evals-Catalogue | ⚠️ **sin licencia declarada** | 23 | — | **El repo que contiene el hallazgo del pase.** Catálogo colaborativo de frameworks, benchmarks y papers de evaluación de LLMs en 7 categorías, con una de ellas *domain-specific*: **derecho, medicina y finanzas**. **Educación no figura** |
| https://github.com/aiverify-foundation/moonshot-cicd | **Apache-2.0** ✅ | 14 | 4 | La versión GA de Moonshot **para pipeline**: corre dentro de CI/CD, con Docker y soporte S3 nativo y guía de despliegue en AWS CodeBuild. Prueba cuatro categorías de riesgo: **alucinación, contenido indeseable, divulgación de datos y vulnerabilidad adversaria**. Python 3.12 |
| https://github.com/aiverify-foundation/moonshot-ui | **Apache-2.0** ✅ | 12 | 7 | La interfaz web de Moonshot (Next.js). Importa para un entregable: el informe sale en **HTML con gráficos interactivos** y export JSON, que es lo que un comité de ética o una inspección educativa puede leer sin consola |
| https://github.com/aiverify-foundation/aiverify-developer-tools | **Apache-2.0** ✅ | 9 | 6 | **La pieza que vuelve construible el gap 35:** plantillas para escribir **plugins de test y algoritmos propios** compatibles con el toolkit (v2.x). Es el punto de extensión por donde entraría una prueba pedagógica |

### 🔴 El hallazgo del pase, y son tres catálogos independientes diciendo lo mismo

No es una impresión de búsqueda: tres artefactos distintos, de tres jurisdicciones distintas, declaran su cobertura
por dominio y **ninguno incluye educación**.

1. **`LLM-Evals-Catalogue`** (AI Verify Foundation, Singapur) — categoría *domain-specific*: **derecho, medicina,
   finanzas**. Educación ausente.
2. **`compl-ai`** (ETH Zürich / INSAIT / LatticeFlow) — 29 benchmarks mapeados a los 6 principios del AI Act. **Sin
   mención de educación**, aunque el Anexo III del propio AI Act nombra la educación como alto riesgo de forma
   explícita.
3. **`morganrcu/awesome-eu-ai-act`** (**CC0**, 21 ★) — lista curada de herramientas de conformidad al AI Act:
   Giskard (5.700 ★), DeepEval, PyRIT, Inspect AI (MIT), Holistic AI (Apache-2.0), AI Act Companion (MIT), Regula
   (Apache-2.0 / EUPL-1.2), VerifyWise, AIR Blackbox, Venturalitica SDK, Inkog. **Ninguna herramienta específica del
   sector educativo.**

**Y del otro lado, esta KB tiene desde el pase 4 justo lo que falta ahí:** `EduBench` (**MIT**), `SafeTutors`
(**MIT**), `MathTutorBench` (CC BY 4.0), `UnifyingAITutorEvaluation` (CC BY-SA 4.0), `EduGuardBench` (sin licencia),
`AITutor-EvalKit` (MIT). Benchmarks pedagógicos premiados en EMNLP, NAACL y ACL — **y ninguno está mapeado a un
requisito regulatorio ni empaquetado como *recipe* de ninguna de estas herramientas.**

**Ése es el gap 35, y es el más construible que tiene esta KB**, por una razón de licencia: las dos puntas son
permisivas. `EduBench` y `SafeTutors` son MIT; Moonshot, `moonshot-data` y `aiverify-developer-tools` son Apache-2.0;
Inspect es MIT; COMPL-AI es Apache-2.0. **No hay fricción legal en el ensamblado.** Lo que falta es el ensamblado.
Ver **P42**.

### Lo que esta capa NO es, y conviene no sobrevenderlo

- **Ninguna de estas herramientas certifica nada.** `aiverify` lo dice por escrito: *no define estándares éticos de
  AI y no garantiza que ningún sistema evaluado esté libre de riesgos o sesgos, ni que sea completamente seguro*. Es
  **evidencia**, no conformidad.
- **El marco de Singapur es voluntario.** El **Model AI Governance Framework for Agentic AI** no tiene cláusula de
  penalidad, ni registro obligatorio, ni mecanismo de *enforcement*. El europeo sí. Mezclar los dos en una propuesta
  es un error de encuadre: Moonshot sirve como **herramienta** en Europa, no como **cumplimiento** europeo.
- **No hay crosswalk directo de AI Verify al EU AI Act.** Lo que hay verificado son dos mapeos: a **NIST AI RMF**
  (octubre 2023 — el único ejercicio gobierno-a-gobierno del mundo) y a **ISO/IEC 42001:2023** (junio 2024). La vía
  hacia el AI Act es **indirecta, por ISO 42001**. Para un expediente europeo la pieza mapeada es **COMPL-AI**, no
  Moonshot.
- **`aiverify` no evalúa agentes.** Evalúa modelos supervisados tabulares y de imagen. Para un tutor LLM la pieza es
  **Moonshot**, **Inspect** o **COMPL-AI**. Proponer "AI Verify" a secas para un agente educativo es prometer la
  herramienta equivocada.

### El *unlearning* educativo, que llegó por la puerta de al lado

| Repo | Licencia | ★ | Commits | Qué es |
|---|---|---|---|---|
| https://github.com/GEMLab-HKU/Unlearn_and_Relearn | **MIT** ✅ | 4 | 22 | **El primer repo de esta KB que aplica *machine unlearning* a un modelo de alumno, con código publicado.** De GEMLab, **Universidad de Hong Kong** (Jiajia Song, Zhihan Guo, Jionghao Lin). Tres etapas: *unlearning* por destilación con intervención, *relearning* (fine-tuning o enseñanza interactiva guiada por LLM) y un loop de tres partes **Coach / Teachable Agent / Judge**. Olvido progresivo configurable del **10 al 50%**. Python |

🔴 **Y la distinción es el hallazgo, porque decide si mueve el gap 34 o no: no mueve.** Este repo **no usa
*unlearning* para privacidad**. Lo usa **al revés y a propósito**: para volver *tonto* a un modelo que sabe
demasiado, de modo que pueda hacer de **alumno novato creíble** en una dinámica de *learning-by-teaching* — el
problema real que ataca es que un LLM al que se le pide "actuá como principiante" se escapa igual hacia
explicaciones de experto y arruina el ejercicio. Mide si el agente **recupera** el conocimiento borrado cuando el
alumno humano se lo enseña.

**Entonces:** el **gap 34** (*unlearning* evaluado sobre modelos de alumno **por supresión de dato personal**) sigue
abierto, y ahora con un matiz que vale escribir — **la técnica que el gap 34 pide ya está en educación, con código y
licencia MIT; lo que no está es el uso de privacidad.** Es la misma maquinaria con el objetivo invertido. Para quien
construya el *harness* del gap 34, esto es la mejor noticia posible: hay un precedente educativo funcionando del que
salen las dos mitades difíciles (cómo se borra un concepto de un modelo y cómo se mide que se borró), y lo único que
hay que cambiar es qué se borra y para qué. Ver **P43**, que lo usa por su lado pedagógico, que es el que está listo.

⚠️ **4 estrellas y 0 forks.** Es un repo de laboratorio, no una dependencia. Vale como **arquitectura de
referencia**, igual que `tero` en el pase 8.

### La nota de método del pase, y explica dos pasadas de búsquedas fallidas

Los pases 18 y 19 buscaron *unlearning* sobre *knowledge tracing* y no encontraron código. **Hay una colisión de
terminología que lo explica, y conviene dejarla escrita porque va a volver a pasar.** La frase «*knowledge tracing*»
tiene **dos significados incompatibles** en la literatura que devuelve esa búsqueda:

- el de esta KB y de `pyKT`: **modelar el estado de conocimiento del alumno** a lo largo del tiempo;
- el de la literatura de *unlearning* (p. ej. *Lifting Data-Tracing Machine Unlearning to Knowledge-Tracing for
  Foundation Models*): **rastrear qué conocimiento de un modelo fundacional vino de qué dato de entrenamiento**.

Buscar «unlearning + knowledge tracing» devuelve el segundo sentido y **entierra el primero**. La búsqueda que sí
funcionó fue por **escenario educativo** (*novice student simulation*), no por técnica — que es exactamente la regla
que el pase 5 ya había aprendido para los benchmarks y que esta KB vuelve a redescubrir en otra capa.

### Lo que esta capa tiene por región

- **APAC** — **es donde vive la oferta, y por primera vez con un regulador adentro**: toda la pila AI Verify /
  Moonshot es de **Singapur** (IMDA + AI Verify Foundation), y el único *unlearning* educativo con código es de
  **Hong Kong**. Extiende el **gap 4** a una capa más, y con un signo distinto a las anteriores: acá lo APAC no es
  un prototipo sin licencia, es **infraestructura de un Estado con Apache-2.0**.
- **EMEA** — **la única pieza mapeada al régimen que sí es exigible**: `compl-ai` (ETH Zürich + INSAIT +
  LatticeFlow, Apache-2.0, 211 ★) e `inspect_ai` (UK AISI, **MIT**, 2.900 ★). Es el patrón que el **gap 3** viene
  anotando desde el pase 4 —EMEA produce la capa que mide, no el tutor— y acá se cumple de forma casi caricaturesca.
- **North America** — aporta **el puente de interoperabilidad**, no la herramienta: el **NIST AI RMF** es el marco
  contra el que AI Verify se mapeó en 2023. La oferta de herramienta propia en esta capa es privada (LatticeFlow es
  suiza; Giskard, francesa).
- **LATAM** — 🚫 **no se encontró ninguna herramienta de testing de conformidad de origen LATAM** en este barrido.
  Se declara **no encontrada, no inexistente**. Y duele más que en otras capas, porque **Brasil, Chile y México
  tienen los tres obligaciones de auditoría algorítmica escritas o en trámite** (ver `intel/market.md`): la región
  está legislando la auditoría y no está construyendo la herramienta que la ejecuta.

Ver el **gap 35**, las tendencias **51**, **52** y **53**, y los patrones **P42** y **P43**.

## 🔌 La capa conector — agregada en el pase 26 del 2026-10-01

Veinticinco pasadas buscaron **agentes**. Esta buscó **la puerta por la que el agente entra al sistema instalado**, que
es lo que el pase 25 dejó escrito como eje (*«cambiar el eje de búsqueda al conector»*). Es la primera vez que esta KB
mide una capa en vez de inventariarla: **el cartucho MCP de CaSS se ejecutó**, y el resultado cierra el gap 40.

### El cartucho MCP de CaSS, medido — el gap 40 se cierra

El pase 25 registró que CaSS *declara* MCP entre sus cartuchos y marcó el **gap 40** porque nadie había levantado el
servidor ni listado una sola herramienta. **Este pase las listó.** No levantando el servidor —que necesita Elasticsearch
y en este entorno **no hay demonio de Docker**— sino por el camino que la propia arquitectura del proyecto permite:
el adaptador genera las tools con `generateTools(spec)` sobre el OpenAPI que `swagger-jsdoc` construye desde los
comentarios del código, **y eso corre sin base de datos**. Se reprodujeron las opciones exactas de `src/main/server.js`,
se generó el spec, se validó con el mismo `openapi-schema-validator` que el servidor usa al arrancar, y se ejecutó el
generador real del repo.

**Resultado medido:** spec de **51 paths**, **0 errores de validación**, y **6 tools + 3 resource templates**.

| Tool | Método y path | Parámetros | Requeridos | `readOnlyHint` |
|------|---------------|------------|------------|----------------|
| `server_status` | `GET /api/ping` | `fields` | — | ✅ true |
| `search_data` | `GET /api/data/` | `q`, `start`, `size`, `index_hint` | — | ✅ true |
| `get_object` | `GET /api/data/{uid}` | `uid`, `history` | `uid` | ✅ true |
| `save_object` | `POST /api/data/{uid}` | `uid` | `uid` | ❌ false |
| `record_evidence` | `POST /api/xapi/statement` | *(body)* | `body` | ❌ false |
| `get_learner_profile` | `GET /api/profile/latest` | `frameworkId`, `subject`, `flushCache`, `cache`, `targetDateTime` | — | ✅ true |

Resource templates: `CaSS JSON-LD Object`, `CaSS JSON-LD Object (Versioned)`, `CaSS Object by UID`.

**Por qué esto cambia el patrón P48 y no sólo cierra un gap.** Las dos tools que importan son `record_evidence`
(`POST /api/xapi/statement`) y `get_learner_profile` (`GET /api/profile/latest`): **entrar evidencia xAPI y sacar
perfil de competencia, por MCP, bajo Apache-2.0.** Ésos son exactamente los dos pasos que el paso 4 de **P48** tenía
inferidos desde una línea de README. La descripción que el propio repo le pone a `get_learner_profile` —*«use this tool
to answer the question "what does this person know?"»*— es la operación que esta KB viene describiendo desde el pase 14
sin tener con qué ejecutarla. Ver la tendencia **66** y el patrón **P50**.

**Y hay un hallazgo de diseño que corrige una suposición razonable.** De los **51 paths** del spec, el cartucho expone
**6**. No es una limitación: son **45 paths marcados `x-mcp-ignore: true`** uno por uno en el código, con anotaciones
`x-mcp-tool-name` y `x-mcp-description` escritas a mano en los 6 que sí salen. **La superficie MCP de CaSS está curada,
no volcada.** Lo que queda deliberadamente afuera incluye `POST /api/xapi/statements` (el *bulk* del LRS),
`GET /api/xapi/endpoint`, el `multiPut`/`multiDelete`/`multiGet` de skyRepo y todo `skyId`. **Consecuencia práctica:**
por MCP se escribe **un statement por llamada**, no lotes — quien cotice ingestión masiva de telemetría por esta puerta
está cotizando mal. Ver el **gap 41**.

⚠️ **Lo que esta medición NO es.** No se levantó el servidor HTTP ni se hizo *handshake* MCP con un cliente real: se
midió la **generación** de las tools, que es determinista y pura sobre el spec, no su **invocación**, que necesita
Elasticsearch. Las 13 aserciones de `5.mcp.json-schema-to-zod.test.js` pasan (13/13); `5.mcp.openapi-to-tools.test.js`
**no se pudo correr tal cual** porque su `before` hace `fetch` a `localhost:80/api/swagger.json`. El conteo de 6 coincide
con lo que ese test afirma (*«generates exactly 6 tools from the current spec»*) y con las **6** anotaciones
`x-mcp-tool-name` del árbol. **Tres fuentes independientes dan 6.** Queda como acción del pase 27 el *handshake* real.

### El lado *platform* (LMS) se cierra por medición, y la respuesta es que no existe permisivo

El pase 25 dejó como acción *«levantar `LtiAdvantagePlatform` (MIT) contra `ltijs` y medir si el launch OIDC cierra»*.
**La ejecución está bloqueada por el entorno y hay que decirlo:** `LtiAdvantagePlatform` es **ASP.NET Core 10**, en esta
sesión **no hay `dotnet`**, y no se puede instalar — `https://dot.net/v1/dotnet-install.sh` responde
**`CONNECT tunnel failed, 403`** por el proxy de egreso. El *launch* de punta a punta sigue sin medirse.

**Pero la pregunta de fondo sí se pudo contestar, y por primera vez con evidencia de primera mano en los seis
candidatos.** Se instaló `ltijs` desde npm (**5.9.9, Apache-2.0**) y se inspeccionaron sus exports:

```
top-level exports: [ 'Provider' ]
```

**Un solo export, `Provider`.** No hay clase de *consumer*/*platform*. Y su propio `package.json` dice
*«Easily turn your web application into a LTI 1.3 **Learning Tool**»*. **`ltijs` es tool-side y nada más**, medido, no
leído de la documentación.

| Pieza | Licencia | ★ | Lado | Estado real |
|------|----------|---|------|-------------|
| `ltijs` | **Apache-2.0** ✅ | 373 | *tool* | Producción. **Sólo exporta `Provider`** (medido en el pase 26) |
| `oat-sa/lib-lti1p3-core` | ⚠️ **GPL-2.0** | 37 | *platform* **y** *tool* | **El único completo y certificado 1EdTech** — y copyleft |
| `macewan-cs/lti` | **MIT** ✅ | 8 | *tool* | Go. *«partially implements»*, **tool-side** — no es el lado LMS |
| `LtiLibrary/LtiAdvantagePlatform` | **MIT** ✅ | — | *platform* | Se describe **«Sample»**. ⛔ No ejecutable acá: sin `dotnet`, dot.net bloqueado |
| `Citolab/lti-1p3-platform-example` | ⚠️ **GPL-3.0+** | — | *platform* | *«example»* en el nombre. .NET + React |
| `UOC/java-lti-1.3-platform` | ⚠️ **sin licencia** | 0 | *platform* | *«**will** implement»* (pase 24) |

🔴 **La conclusión, dicha sin suavizar: no hay implementación *platform-side* de LTI 1.3 que sea permisiva **y**
productiva.** Las dos permisivas se autodenominan *«Sample»* y *«example»*; la única completa y certificada por 1EdTech
es **GPL-2.0**; la única que prometía serlo en Java no declara licencia y habla en futuro. **Esta KB no puede proponer
el lado LMS con licencia permisiva**, y ahora eso está **medido sobre seis candidatos**, no supuesto. Para un
*engagement* que necesite el lado plataforma la salida honesta es una de tres: aceptar **GPL-2.0** (TAO, certificada),
integrarse como *tool* contra un LMS que el cliente ya tiene (que es donde esta KB sí es fuerte: `ltijs` + `canvas-mcp`),
o presupuestar el lado plataforma como **desarrollo**, no como integración. Ver el **gap 42** y la tendencia **67**.

### Los conectores de LMS que trajo el eje, y la corrección de licencia que hay que leer antes de proponer

| Pieza | Licencia | ★ | Forks | Commits | Tools | Lectura |
|------|----------|---|-------|---------|-------|---------|
| `vishalsachdev/canvas-mcp` | **MIT** ✅ | 269 | 92 | 815 | **hasta 102–103** + 8 skills | **Entra en la tabla principal.** Las dos puntas (alumno y docente), descubrimiento de tools, escaneo WCAG |
| `csmediapro/moodle-mcp-server` | 🔴 **AGPL-3.0** | **0** | **0** | 57 | **10**, sólo lectura | ⛔ **No proponer.** Ver la corrección abajo |
| `DavidLMS/learnmcp-xapi` | **MIT** ✅ | 15 | 4 | 32 | 3 | Ya estaba (pase 6). **Re-verificado: idénticos 15 ★ y 32 commits** → el proyecto no se movió |

🔴 **La corrección de licencia del pase, y es sobre el único conector de Moodle que existe.** El resumen de búsqueda
presentaba `moodle-mcp-server` como *«open-source MCP server, plugin-extensible, LLM-agnostic»* e invitaba a instalarlo
con `npx`. **La página del repo dice otra cosa en dos frentes:** la licencia es **AGPL-3.0** —no permisiva, y la AGPL es
la que más molesta en un entregable SaaS— y el modelo es **open-core**: los diez tools abiertos son **sólo de lectura**
(`list_courses`, `get_course`, `list_course_users`, `list_assignments`, `list_categories`, `get_site_info`, `get_user`,
`list_user_courses`, `search_users`, `search_courses_by_name`) y las capas que un cliente pediría —*Advanced Reporting*,
*User Analytics*, *User Directory*, *Compliance Pack*— son **plugins premium que se venden aparte**. Súmese **0 ★ y 0
forks**: no hay adopción que respalde el riesgo. **Moodle es el LMS más instalado del mundo y su único conector MCP es
AGPL con las partes útiles cerradas.** Ése es el hueco, y es un hueco de oportunidad: ver el **gap 43** y el patrón **P51**.

⚠️ **Nota de método sobre la verificación de URLs en este pase.** La consigna pide `curl -sI` por URL. **En esta sesión
`curl -sI` contra `github.com` devuelve `403` para *todas* las URLs** —incluidas las que existen y están en esta KB desde
el pase 1— porque el proxy de egreso corta el `HEAD`. Verificar con `curl` acá produciría **404s falsos sobre repos
reales**, que es el error que la consigna quiere evitar. Por eso **toda verificación de este pase se hizo con WebFetch
sobre la página del repo** (licencia, ★, forks, commits leídos de la página), y el único 404 que se reporta —
`Cerebro-Tech/FlightPath` — es un 404 **de WebFetch**, no de `curl`.

## Capa de conectores de *rostering* y estándares — medida en el registro de paquetes, pase 31 del 2026-10-02

Treinta pases buscaron conectores **por nombre de protocolo** (`*-mcp`, `mcp-*`). El pase 30 demostró que eso deja
ausencias mal medidas y dejó la consigna de **preguntarle al registro de paquetes por el nombre del proyecto o del
estándar, y abrir el README a buscar «MCP» adentro**. Este pase la ejecutó contra `registry.npmjs.org` y `pypi.org`.
**Rinde: aparece una segunda puerta MCP de OneRoster y es MIT.**

| Agente / conector | Paquete verificado | Versión | Licencia | Sirve MCP | Qué escribe |
|---|---|---|---|---|---|
| **`@eduware/oneroster`** | [registry.npmjs.org](https://registry.npmjs.org/@eduware%2Foneroster) | 1.2.11 | **MIT** ✅ | ✅ **sí — ejecutable `mcp` empaquetado** | OneRoster **1.1 y 1.2** completo + perfil `ClassLink` de sólo lectura |
| `@superbuilders/oneroster` (= `trilogy-group/oneroster-ts`) | [github.com/trilogy-group/oneroster-ts](https://github.com/trilogy-group/oneroster-ts) | 0.7.0 | 0BSD ✅ | ✅ sí (ya registrado, 132 tools medidas en el pase 30) | OneRoster con escritura |
| `openedx-mcp` (oficial Open edX) | [pypi.org/project/openedx-mcp](https://pypi.org/project/openedx-mcp/) | 0.1.5 | ⚠️ **AGPL-3.0** | ✅ sí (35 rutas) | matrícula, usuarios, roles, certificados, reportes, **authoring de bloques** |

**Lo que dice el README de `@eduware/oneroster`, textual:** *«the included MCP server for tool-based integrations»* y
*«The package includes an MCP server that exposes SDK operations as tools»*. 13 versiones publicadas, creado
**2026-01-23**, última modificación **2026-07-10**.

⚠️ **Y la advertencia que va con el alta:** su repo declarado, `Eduware-Inc/eduware-oneroster`, **devuelve 404** por
`raw.githubusercontent.com`. **El paquete es verificable en el registro; el repo es una afirmación que no se puede
comprobar.** Se cita por registro a propósito. Es el **gap 58**, y da una regla nueva para esta KB: **el paquete
publicado y el repo público son dos verificaciones distintas, y la que importa para construir es la del paquete.**

### Lo que se midió y salió vacío — ausencias informadas, no silencios

| Candidato | Qué se midió | Resultado |
|---|---|---|
| **`ltijs`** v7.0.6 (Apache-2.0, repo verificado, modificado **2026-09-18**) | README completo leído, grep de `MCP` / `Model Context Protocol` | **0 menciones.** El SDK LTI 1.3 de referencia está vivo y mantenido **y no tiene puerta de agente**. El **gap 42 sigue cerrado**, ahora por medición y no por etiqueta |
| **`pylti1p3`** v2.0.0 (MIT) | PyPI: 29 releases, **última publicación `2022-11-20`** | Sin MCP, y 🔴 **casi cuatro años sin release**. ✅ El repo (`dmitry-viskov/pylti1.3`) **sí existe** —`README.rst`, `setup.py` y `LICENSE` responden 200— y esta KB ya lo tenía registrado con 138 ★: el abandono es **de publicación en PyPI**, no del repo |
| **`@timeback/caliper`** v0.3.3 | registro: licencia y repo | 🔴 **No declara licencia.** Código **de 2026-09-25** y jurídicamente inusable. Ver advertencias de licencia |
| **`openbadges`** en npm | familia `openbadges-validator*`, `openbadges-bakery*` | Herramientas de validación y *baking*, **OB 2.0**, sin MCP |

### 🟢 Una pieza que faltaba y entra permisiva: OpenBadges **3.0**

| Pieza | Paquete | Versión | Licencia | Qué aporta |
|---|---|---|---|---|
| **`@ajna-inc/openbadges`** | [registry.npmjs.org](https://registry.npmjs.org/@ajna-inc%2Fopenbadges) | 0.6.3 | **Apache-2.0** ✅ | *«OpenBadges v3.0 module for Credo-TS with OAuth 2.0 provider support»*, modificado 2026-05-19 |

Esta KB tenía registrado que **CaSS implementa OB 2.0 y no 3.0**, y no tenía **ninguna** pieza de OB 3.0. Ya la tiene, y
es permisiva. ⚠️ No declara repo, así que se cita por registro (mismo criterio que `@eduware`).

