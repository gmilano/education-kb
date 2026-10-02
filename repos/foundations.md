---
industry: education
region: Global
updated: 2026-10-02
---

# 🏗️ Repos fundacionales — education

> Bases sobre las cuales construir. Verificado repo por repo vía WebFetch el 2026-09-30 (capas del pase 10, el 2026-10-01).
> Leer la columna **Licencia** antes de proponer: media KB de educación es GPL/AGPL, no permisiva.
> **Pase 50 del 2026-10-02:** 🔴 **la nota de arriba —*media KB de educación es GPL/AGPL*— se midió en la capa de AGENTES, que es donde esta base suponía permisividad, y el resultado no es el supuesto.** De **32** nombres de registro citados, **30 resuelven**: **21 permisivos**, **5 copyleft o recíproca**, **4 SIN licencia** — y 🔴 **los dos pedazos de la capa MCP de Open edX en PyPI son AGPL-3.0**, o sea copyleft de RED sobre un servidor. ⚠️ **Y los 2 que no resuelven son una corrección propia: `@tutors/xapi` y `@tutors/badges` dan 404 y esta base los citaba.** 🟢 **El defecto de instrumento que se corrige corre en los DOS sentidos** (campo sin texto **y** texto sin campo), y el control de alcanzabilidad cambia **7 falsos «sin licencia»** por **2 ciertos y 5 declarados indeterminados**. Ver **P114**.
> **Pase 49 del 2026-10-02:** 🟢 **DOS clases de cifra dejaron de ser «no re-verificables acá», y una de las dos
> cubre 326 mediciones de esta base.** El pase 48 declaró **1.836 de 3.611 (50,8 %)** fuera de alcance por canal
> cerrado. **Dos de esos canales estaban mal elegidos, no cerrados:**
> 🟢 **licencias** — `raw.githubusercontent.com/<org>/<repo>/<rama>/LICENSE` responde **200** donde
> `github.com/<org>/<repo>` responde **403**. Verificado con control positivo sobre cinco repos (`Paper2Slides`,
> `VideoAgent`, `VideoRAG`, `DeepTutor`, `OpenMAIC`): **200 por `raw` los cinco, 403 por `github.com` los cinco.**
> 🟢 **`tools` (326 cifras)** — el *tarball* de `registry.npmjs.org` se baja y la superficie se cuenta
> **estáticamente**, sin instalar el paquete ni levantar el servidor. Instrumento nuevo: `compose/code/npm-surface-probe/`,
> **19/19**.
> 🔴 **Y lo primero que midió el canal nuevo es un bloqueo comercial, no un número:** `@imazhar101/mcp-canvas-server`
> expone **227 herramientas distintas** sobre Canvas LMS —**la superficie más grande de esta KB**, verificada por **dos
> conteos independientes** (nombres en `tools/` = **227**; ocurrencias de `inputSchema` = **227**; coinciden uno a uno en
> los **18** archivos)— **y no declara licencia en ningún canal** (campo del registro, manifiesto embarcado, archivo y
> repositorio: los cuatro ausentes). El pase 35 lo excluyó por eso y tenía razón; **lo que nadie había medido es el
> tamaño de lo excluido.** 🔵 **Pedir ese `LICENSE` upstream es la gestión de mayor apalancamiento de esta base.**
> ⚠️ **Y una trampa de licencia que un *badge* no muestra:** `HKUDS/VideoRAG` es **MIT en la arquitectura** y
> **NO comercial tal como se embarca**, porque integra ImageBind (CC BY-NC-SA 4.0) — **lo dice su propio `LICENSE`**:
> *«the current complete implementation is restricted to NonCommercial use only»* (tendencia 223).
> 🔴 **Corrección de una cifra propia de este README:** las «**186** crudas / **152** no-blancas» de
> `extract_surface.py` tienen **el valor bien y la métrica mal** — **152 es no-blancas-NO-COMENTARIO; no-blancas son
> 157**. Es el gap 101 encontrado por el archivo que existe para evitarlo, **tres pases después de escribir la regla**.
> **Pase 48 del 2026-10-02:** 🟢 **el barrido de cifras pasó de UN archivo a los OCHO, y la escala cambia la lectura:
> 3.611 mediciones en total, de las que 1.836 — el 50,8 % — NO son re-verificables en este entorno** (1.042 `★`, 418
> `commits`, 326 conteos de `tools`, 50 descargas). **Más de la mitad de las cifras de esta base no se pueden refrescar
> desde acá**, y las **1.775** que sí —líneas, aserciones, rutas, métodos, archivos— son las que valen para una
> propuesta. 🔴 **Y el pase 47 barrió `compose/patterns.md` por ser el activo más citado: resultó el archivo con MENOR
> densidad de cifras de los ocho (65,3 por kilolínea, contra 184,8 de `agents/top.md` y 173,4 de `intel/market.md`).**
> `intel/market.md` + `intel/trends.md` suman **1.657 cifras — el 46 % de la base — y nunca se habían barrido.**
> 🟢 **Tres de las cuatro cifras que «no cerraban» quedan cerradas en este pase:** «175 líneas» de **P85** ya tiene
> artefacto (`compose/code/mcp-allowlist-gateway/`, **233** crudas / **196** no-blancas / **184**
> no-blancas-no-comentario, así que la cifra se **reemplaza**), y «11/11» / «23 aserciones» quedaron corregidas donde
> seguían vivas. ⚠️ **Y una corrección de este archivo:** la cifra de **20 aserciones** de `proctoring-reach-audit`
> **no llevaba su condición** (20 con la ruta a un checkout de seb-server, **19** sin ella); ya la lleva. 🔵 **El
> instrumento ahora es cruzado —`extract_figures.py --crossref` vuelve a correr las ocho suites y atribuye cada cita—
> porque el defecto real no es que una cifra se venza: es que una CORRECCIÓN NO SE PROPAGA entre archivos.**
> **Pase 47 del 2026-10-02:** 🔵 **este pase no agrega repos: le AUDITA LAS CIFRAS a los que ya están, y encontró que
> cuatro no cierran.** El instrumento quedó escrito y es repetible —`compose/code/patterns-figure-audit/`— y mide **383**
> cifras de `compose/patterns.md`, de las que **218 no son reproducibles en este entorno**: `★` (90), `commits` (46) y
> descargas (4) porque `github.com` responde **403** a `curl` acá y `api.github.com` niega en el cuerpo (pase 37), y
> `tools` (78) porque exige el paquete instalado. 🔴 **Las cuatro que no cierran:** «175 líneas» de **P85** (el código
> **no está en el repositorio** — gap 103), «11/11 checks» (hoy **37/37**), «23 aserciones» (hoy **46**) y «~115 líneas»
> (**186** crudas / **152** no-blancas: **ninguna de las dos**). ⚠️ **La regla que queda, y aplica a este archivo
> también: toda cifra sobre un repo nombra su instrumento, y para líneas hay que decir «crudas» o
> «no-blancas-no-comentario» — en la clase de SEB la diferencia es 481 vs 583 y 912 vs 1.116, entre 17 % y 22 % del
> presupuesto.** 🔵 **Y una corrección de conteo propia: `scorm-mcp-server` empaqueta 20 XSD, no 15** — 15 en `schemas/`
> y 5 en `schemas12/`, y contar sólo el primero es lo que hizo invisible el segundo dialecto de SCORM (**P106**).
> **Pase 36 del 2026-10-02:** 🔵 **este pase no agrega repos: le pone FECHA a los que ya están, y la fecha cambia tres recomendaciones.** Se midió la capa PHP de evaluación y telemetría en Packagist —el único registro de los tres que entrega descargas en este entorno (`api.npmjs.org` y `pypistats.org` dan **403 a CONNECT**)— y el resultado está en `repos/trending.md`. **Lo que hay que saber antes de proponer desde este archivo:** 🔴 **la pieza xAPI más descargada de esta base, `rusticisoftware/tincan` (Apache-2.0, 6.178 desc./mes, 863.777 totales), no publica desde el 2022-11-02**, y ⚠️ **el único MIT de esa capa, `php-xapi/client`, está parado desde el 2021-03-24** con 825 desc./mes. 🔵 **La lectura es que en xAPI/PHP lo permisivo está quieto y lo vivo es copyleft**, así que la receta de telemetría se sostiene en **Ralph (MIT)** + **`lrsql` (Apache-2.0)** + **`learnmcp-xapi` (MIT)** y no en la capa PHP. 🟢 **Del lado de evaluación, lo activo es `oat-sa/extension-tao-testqti`** (**885 versiones**, release del **2026-09-30**) **y sigue siendo GPL-2.0-only**, mientras **lo permisivo es lo nuevo**: `@longsightgroup/qti3-cli` (**MIT**, 41 releases desde el 2026-05-21, último **2026-10-01**) con **cero dependencias de terceros** — sus 4 dependencias son todas `@longsightgroup/*` pinneadas a la misma versión exacta. **Su manifiesto MCP completo de 20 tools está escrito en `compose/patterns.md` (P76).** 🔴 **Y una corrección de catálogo: `oat-sa/qti-sdk` devuelve 404 en Packagist porque es el nombre del REPO — su paquete es `qtism/qtism`** (GPL-2.0-only, 218.212 descargas totales, 315 versiones). **Nombre de repo y nombre de paquete son identificadores distintos, y confundirlos produce un 404 que parece una ausencia** — pasó igual con `1edtech/oneroster`, `imsglobal/lti-1-3-php-library` y `packbackbooks/lti-1-3-php-library`, los tres **404**, que se anotan como *«no verificado en Packagist bajo ese nombre»* y **no** como inexistentes. ⚠️ **Acción pendiente que el pase 37 tiene asignada: este archivo nunca pasó por el control de *slugs* distintos ni por el de *backlink*** — los dos que en `agents/top.md` encontraron **un duplicado** y **dos colisiones** este mismo pase.
> **Pase 11 del 2026-10-01:** aparece una licencia que las diez pasadas anteriores filtraban sin saberlo — **ECL-2.0**, con la que licencia todo Apereo (Sakai, Opencast, OpenLRW). Es Apache-2.0 con el alcance de patentes acotado, aprobada por OSI y FSF, y **es apta para construir arriba**. Ver la capa de analítica institucional, abajo.

> **Pase 26 del 2026-10-01:** entra una capa que **veinticinco pasadas no buscaron** — **la biblioteca** (ILS/OPAC) — y
> entra permisiva: **FOLIO** es **Apache-2.0** con 3.096 commits en el ensamblado de plataforma. Es la primera pieza de
> infraestructura institucional *grande* y *permisiva* de esta KB que no es ni LMS ni LRS. Y se cierra por medición el
> **lado *platform* de LTI** (gap 42): no hay implementación permisiva y productiva, medido sobre seis candidatos.
> Ver la capa de biblioteca y la de conectores, abajo.
> **Pase 25 del 2026-10-01:** cuatro capas nuevas —**evaluación** (autoría/banco/entrega QTI 3), **horarios**
> (`UniTime`, Apache-2.0, 349 ★), **aserción de competencias** (`CaSS`, Apache-2.0, con cartucho **MCP**) y la
> **decisión de estándar de analítica**— y **dos correcciones**: el lado ***platform*** de LTI **sí** se puede construir
> con licencia permisiva (`LtiAdvantagePlatform`, MIT), y la capa LTI tiene **cinco stacks**, con `ltijs` (Apache-2.0,
> **373 ★**) como la más traccionada y ausente de esta KB durante seis pases. 🔴 **Y un estándar se cayó del open source:**
> **Caliper pasó a repos privados el 2023-06-17** — desde este pase se propone **xAPI**.
> **Pase 27 del 2026-10-01:** **el gap 42 cierra** — la séptima y última candidata, la implementación de referencia de 1EdTech, **no es una implementación**: `1EdTech/ltibootcamp` es una colección de enlaces **sin licencia declarada**, y el código Ruby de la RI está **detrás de la membresía**. *«Esta KB propone la herramienta, no el aula»* queda **cerrado sobre siete candidatas**. Y entra **Open edX como la base de mayor huella pública sin puerta de agente** (**gap 48**). Ver la sección del pase 27, abajo.


> **Pase 28 del 2026-10-01:** **se ejecuta la acción 1 del pase 27 y el gap 48 queda contestado leyendo el código fuente**, no la documentación (`docs.openedx.org` y `openedx.atlassian.net` están **los dos bloqueados**; `raw.githubusercontent.com` **sí responde**, y es un canal de verificación nuevo para esta KB). **La respuesta es doble:** la API REST de Open edX **alcanza y escribe** para matrícula, roles, bloques de curso y **notas —incluido el lote—**, pero el ***authoring* de Studio está declarado experimental por el propio proyecto**. Eso parte el gap 48 en dos y abre el **gap 50**. Ver la sección del pase 28, abajo.
> **Pase 29 del 2026-10-01:** **se ejecutan las tres acciones del pase 28, y la primera refuta la conclusión del pase que la pidió.** 🔴 **El *authoring* de Open edX NO está bloqueado por estado experimental.** El aviso que el pase 28 citó vive en `v1/urls.py`, **está fechado «(Nov. 23)» y encabeza una sección sin rutas**; `v0/views/xblock.py` dice **lo contrario** (*«superseded by `XblockViewSet`… use `/api/contentstore/v1/xblock/` going forward»*) y **`v1/urls.py` registra ese `XblockViewSet` con CRUD completo** bajo los ADRs de **FC-0118** —incluido un **`?view=minimal`** (ADR 0036) que recorta el árbol del curso, que es justo lo que necesita un agente. **Deprecación circular: gana la señal vigente.** Y aparece lo que el pase 28 no vio: **cinco versiones de API montadas a la vez** (`v0`–`v4`), con las notas en **tres** de ellas. ✅ **Alta nueva de base: [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) (**Apache-2.0**, 9 ★, 180 commits)** — la implementación de referencia de **CASE 1.0 y 1.1** del propio organismo, con **CASE Provider API oficial**, versionado inmutable en archivos, Keycloak + API keys, RBAC de 4 niveles y 🔵 **endpoint propio de descubrimiento OpenAPI 3**. **Cierra el gap 51** y abre el **gap 52**. Ver la sección del pase 29, abajo.

> **Pase 35 del 2026-10-02:** **el pase que cambia el instrumento de medición de adopción de esta base.** Treinta y dos
> pases midieron con **estrellas**; el registro publica **descargas por mes**, y las series se contradicen en los dos
> sentidos: `learninglocker` **583 ★ / 0 descargas-mes** (queda cerrado, no se propone) contra `TinCanPHP` **88 ★ /
> 6.178 descargas-mes** y `oat-sa/extension-tao-testqti` **8 ★ / 844 versiones / release del 2026-09-30**. 🔴 **Dos capas
> cambian de orden:** el **QTI que el mundo despliega es GPL-2.0-only** (`oat-sa/qti-sdk`, 218.212 descargas, 293
> versiones), así que `@longsightgroup/qti3-*` (**MIT**) e `instructure/qti` (**MIT**) no son «una opción más» sino **lo
> único permisivo**; y la capa xAPI **del lado cliente resulta permisiva** —`TinCanPHP` y `TinCanPython` son
> **Apache-2.0**— que es la mitad que esta base nunca catalogó, aunque las cuatro piezas estén **congeladas**. 🟢 **Altas:**
> la pila `qti3` enumerada con **`qti3-a11y`** (matriz de prueba de accesibilidad + guiones VoiceOver/NVDA/JAWS) y
> **`qti3-pnp`** (resolutor de *Personal Needs and Preferences*, cero dependencias), **`gafapa/moodle-core-cli`** (MIT,
> sin MCP, el más barato de envolver) e **`ibge-br-mcp`** (MIT, la plantilla del **gap 69**). 🔴 **Gap 68:** la puerta
> oficial de Open edX publicó **12 releases en dos días y nada en 70**. Ver la sección del pase 33, abajo.

> **Pase 30 del 2026-10-02:** **el gap 52 cierra leyendo cinco archivos del árbol `main` de OpenCASE, y la contradicción entre sus dos documentos tiene una regla que ninguno enuncia:** el segmento `ims/case/v1pX` aparece **sólo** cuando la operación actúa sobre una entidad del estándar CASE, nunca en las rutas de plataforma. **72 rutas contadas** (24 de lectura —el juego completo en **v1p0 y v1p1**—, 44 de management, **2 de descubrimiento** y 2 de servicio). 🔵 **Tres hallazgos abaratan P60:** hay **dos** endpoints OpenAPI (uno por versión) y **sin auth**; la lectura usa **auth opcional** (marcos públicos sin credenciales ni tenant); y aparece **CGE — CASE Global Exchange**, **11 rutas de federación** que permiten **suscribirse** a marcos del registro global en vez de cargarlos. 🔴 **Pero la escritura no es parte del estándar y lo declara el código**, así que sólo la mitad de lectura es portable. 🔴 **Open edX cambia de estado: ya tiene puerta de agente, y es AGPL-3.0 y corre EN PROCESO** (`openedx-mcp` + `tutor-contrib-openedxmcp`, 2026-07-25) — con lo que **el riesgo de adaptador de versiones del pase 29 no se paga por ese camino, y la autoría queda confirmada por implementación**. ✅ **Alta nueva:** [`instructure/qti`](https://github.com/instructure/qti) (**MIT**, 174 commits), que cubre **QTI 1.2** —el acervo legado del que parte **P48**— y que `examplary/qti` no cubría. ✅ **Y se cierran dos nombres: `.LRN` (vivo pero GPL-2.0 y en CVS) y `CK-ERP` (muerto desde 2012).** Ver la sección del pase 30, abajo.

> **Pase 34 del 2026-10-02:** entra la **capa de conformidad y simulación xAPI** (sección nueva, abajo) con dos piezas
> **Apache-2.0** verificadas de primera mano: **`yetanalytics/datasim`** —genera tráfico xAPI a escala y valida contra
> **xAPI Profile**, del **mismo mantenedor que `lrsql`**— y el **validador oficial de 1EdTech** para Open Badges y CLR.
> 🔴 **Y una no-alta declarada: `yetanalytics/persephone` queda fuera** — 10 rutas de licencia, las 10 **404**, y Docker
> parado en **2023-10-10** (**gap 70**). 🔵 **Las dos altas aparecieron por el nombre de la organización, no por término.**

> **Pase 37 del 2026-10-02:** entra **`pie-framework/pie-elements`** (**ISC**, `HEAD` **2026-09-22**, **2.226 versiones**
> publicadas desde 2019, ~50 interacciones de evaluación como *web components* con sub-paquetes `configure` y `controller`),
> y **refuta la mitad «lo permisivo es lo nuevo» de la conclusión de P69**: hay una capa de evaluación permisiva de **siete
> años** que publicó **ayer**. ⚠️ **Con el límite en la misma frase, porque decide si se propone: NO implementa QTI** (cero
> menciones en el README crudo) — tiene su propio modelo de ítem, así que por la **tendencia 29** queda en la categoría
> débil. 🔵 **El trade-off real de esta capa pasa a ser de tres patas y ninguna domina: permisivo+maduro pero modelo propio
> (`pie-elements`) · permisivo+conforme pero nuevo (`qti3-cli`) · copyleft+conforme y desplegado (`qtism`/TAO).**
> 🔴 **Y trae una contradicción de licencia de clase nueva: `LICENSE.md` tiene cuerpo ISC, el `package.json` de la raíz dice
> `MIT`, y `@pie-element/multiple-choice` no declara licencia.** **La regla del pase 10 («verificar contra el archivo
> `LICENSE`, no contra el README») se endurece: el archivo `LICENSE` le gana al MANIFIESTO, que es lo que leen los escáneres
> automáticos** (**gap 76**). 🔵 **Y la base entera queda fechada por un instrumento nuevo:** `git ls-remote` + `fetch
> --depth 1` dató las **49 filas** de `agents/top.md` por el commit de su rama por defecto — **49 de 49 respondieron, cero
> 404** — y **10 están paradas hace ≥ 6 meses**, tres de ellas load-bearing. Tabla completa en `repos/trending.md` (pase 37),
> impacto en `compose/patterns.md`.

> **Pase 45 del 2026-10-02:** **no entran repos nuevos, y el barrido lo midió: las cuatro búsquedas globales
> obligatorias devolvieron la capa genérica y material didáctico *sobre* AI, cero piezas de dominio que esta base no
> tuviera.** Lo que entra es **una re-medición de `UniTime/unitime` sobre un checkout de HOY**, y corrige el dato que
> esta base publicaba sobre su propia superficie. 🟢 **`UniTime/unitime` (Apache-2.0, `HEAD` `aeb4431` del
> **2026-10-02**, Tomáš Müller — árbol vivo, no histórico):** el barrido sobre `JavaSource` **entero** confirma
> **15 conectores API y ni uno más** (`grep -rn '@Service("/api'`), con **26 `do<Verb>(ApiHelper)` implementados**.
> 🔴 **Y aparecen tres cifras que no estaban:** (1) **las rutas HTTP vivas son 60, no 26** — 15 × 4, y las **34** sin
> *override* **responden 501 NOT_IMPLEMENTED, no 404**, porque `ApiConnector` implementa los cuatro verbos con
> `sendError(SC_NOT_IMPLEMENTED)`; (2) **la URL desplegada por omisión es `/UniTime/api/<conector>`** y no
> `/api/<conector>` — el `<url-pattern>` de `apiServlet` en `WebContent/WEB-INF/web.xml` es `/api/*` y `pom.xml:614`
> envía `<warName>UniTime</warName>`, así que **la ruta del árbol es relativa al contexto del *webapp***; (3)
> **`getName()` NO es la ruta de ningún conector** — `ApiServlet` hace `getBean(servletPath + pathInfo)`, así que
> **enruta el nombre del bean de `@Service`**, y `getName()` sólo alimenta `getCacheMode()`. **Los 15 coinciden hoy, así
> que el dato publicado era correcto y el método no.**
> 🔴 **Y una advertencia de superficie que un cliente descubre en producción si no se lee antes:**
> `ScriptConnector.doGet` **despacha por parámetro de query y dos ramas escriben** — `?script=` **llama `doPost`, o sea
> un GET ejecuta un script del servidor**, y `?delete=` borra un ítem de la cola. **Para UniTime, el verbo HTTP no es la
> frontera de escritura**, así que cualquier propuesta *read-only* sobre este upstream tiene que negar `/api/script`
> **por nombre y de forma no anulable**, nunca por verbo. ⚠️ **Y `/api/var-title-crs` devuelve 400 en un despliegue por
> omisión, también en la LECTURA:** `validateRequest()` —llamado por `doGet` y por `doPost`— exige tres
> `ApplicationProperty` seteadas. Ver las tendencias **175**–**177** y el patrón **P100**; el extractor reproducible
> está en `compose/code/unitime-mcp-gate/extract_surface.py`.
> 🟢 **`openedx/edx-platform` (AGPL-3.0, leído sobre `master`) queda con el contrato de autoría cerrado**, y con dos
> cosas que el pase 44 no tenía: **el handler exige DOS claves con subscript pelado** —`parent_locator` (832) y
> `category` (864)— **y el contrato las declara opcionales a las dos**, así que **un cuerpo sin `parent_locator` da 403
> y uno sin `category` da 500**, mientras una clave de más da **400** correctamente. 🟢 **Y una corrección a favor del
> upstream: el `create` del `v1` SÍ corre el serializer** (`@validate_request_with_serializer`,
> `rest_api/v1/views/xblock.py:239-243`) — es estricto con las claves de más y **no puede** atrapar las dos que exige,
> porque las declara opcionales. Ver las tendencias **178**–**179** y el patrón **P101**.
> **Pase 44 del 2026-10-02:** **no entran repos nuevos; los dos upstreams que sostienen los patrones de examen y de
> autoría quedan re-medidos sobre un checkout, y las dos mediciones corrigen cifras de esta propia base.**
> 🟢 **`SafeExamBrowser/seb-server` (⚠️ MPL-2.0, `HEAD` de `master` = `7f45689`, 2026-04-01):** el `HEAD` del clon
> **coincide con el commit que el pase 43 declaró medido**, así que las mediciones son comparables fila por fila — y la
> comparación da **31 controladores de producción (no 36)** y **55 constantes de endpoint (no 41)**. Ver la corrección
> en el renglón de la capa de integración de examen, abajo. 🔴 **Y una contradicción interna de esta KB queda cerrada
> leyendo el archivo: el `README.md` de `compose/code/sebserver-mcp-gate/` decía Apache-2.0 y el `LICENSE` del upstream
> dice «Mozilla Public License Version 2.0».** `repos/foundations.md` y las tendencias del pase 41/42 tenían razón; el
> README del código, no — y la argumentación comercial de la ruta SEB (**copyleft débil, publicar un valor de enum**)
> **depende de que sea MPL**. Corregido en el README y en el docstring de `gate.py`.
> 🟢 **`openedx/edx-platform` (AGPL-3.0, `HEAD` `c0048e1`, 2026-10-02 — de hoy):** la capa de *authoring* del `v1` queda
> medida sobre código vivo. **El POST de creación devuelve `{locator, courseKey}` y el `locator` es el usage key del
> bloque nuevo**, así que el árbol se construye con **1 POST por bloque y ninguna lectura intermedia**; `category`
> **no tiene enum** en un curso (`CharField(required=False)`, sin `choices`) y **sí lo tiene en una biblioteca v1**
> (`["html","problem","video"]`). 🔴 **Y lo que el `v1` NO hace, que es lo que reencuadra P55: `retrieve` devuelve un
> bloque, no un árbol** —`get_block_info` lleva escrito *«children aren't being returned until we have a use case»*—,
> así que el recorrido se hace con **`course_index/{course_id}`, que trae el outline anidado en UNA llamada**. Ver las
> tendencias **171** y **172** y el patrón **P96**.
> ⚠️ **Nota de método que vale para los dos: el instrumento de este pase fue
> `git clone --depth 1 --filter=blob:none --sparse`, no `raw.githubusercontent.com`.** Un clon disperso da el árbol
> completo, resuelve las constantes compuestas y los valores de `src/main/resources` —que es lo que `raw` no permite
> sin saber de antemano qué archivo pedir— y además **fecha el `HEAD`**. Con `raw` no se habría encontrado ninguno de
> los cuatro defectos del pase.

## 🧾 Capa de LICENCIA de la superficie npm/PyPI que esta base cita — 30 paquetes medidos, y el reparto NO es el que el archivo suponía (agregada en el pase 50 del 2026-10-02)

⚠️ **Lo que esta sección NO es:** no es la superficie de tools. La acción 1 del pase 49 pedía las dos
cosas (licencia **y** `tools`) con un `--batch` del probe, y 🔴 **este entorno negó la ejecución de
código del repositorio** (`[Code from External]`). **La licencia se puede medir sin ejecutar nada
—`registry.npmjs.org`, `pypi.org` y `raw.githubusercontent.com` responden 200—, la superficie no.**
Así que acá está la mitad medible, y la otra queda escrita como pendiente, sin rebajarla.

**La nota de cabecera de este archivo dice —*«media KB de educación es GPL/AGPL, no permisiva»*— y
hasta ahora valía para las PLATAFORMAS. Este pase la mide en la CAPA DE AGENTES, que es donde esta
base venía suponiendo permisividad, y el resultado está partido en tres:**

| Reparto de los **30** paquetes npm resueltos (de **32** citados) | Cuántos | Cuáles |
|---|---|---|
| 🟢 **Permisivas** | **21** | **16 MIT** (`@owen-x-tech/canvas-mcp`, los **7** `@longsightgroup/qti3-*`, `@longsightgroup/oneroster`, `@eduware/oneroster`, `@dendiem/caliper`, `@yunmiao/studymate`, `@nahuelalbornoz/moodle-mcp`, `@brutalsystems/tincan`, `@handsong/folio-ui-cli`, `@moinsen-dev/tool-teacher`), **4 Apache-2.0** (`@ajna-inc/openbadges`, `@genramzi/proctor`, `@stll/folio-agents`, `@stll/folio-cli`), **1 ISC** (`frappe-mcp-server`) |
| ⚠️ **Copyleft o recíproca** | **5** | `@learninglocker/xapi-agents` **GPL-3.0**, `@citolab/qti-convert-local-ai` **GPL-3.0-only**, `@universis/one-roster` **LGPL-3.0-or-later**, `@public-ui/mcp` **EUPL-1.2**, `@osu-cass/sb-components` **MPL-2.0** (y en **1.5.0-alpha.10**: *alpha*) |
| 🔴 **Sin campo de licencia** | **4** | `@superbuilders/oneroster` 0.7.0, `@timeback/caliper` 0.3.3, `@pie-element/multiple-choice` **14.0.0**, `@pie-element/rubric` **9.0.0** |

**Y los 2 que no resuelven son una corrección propia:** 🔴 **`@tutors/xapi` y `@tutors/badges`
devuelven 404 en el registro y esta base los citaba** (`intel/trends.md`, `agents/trending.md`).
*Un 404 no es un hallazgo* — y esta vez el 404 era de la KB.

### 🔴 Lo que hay que leer antes de proponer, y son cuatro cosas, no una

1. **Las 4 sin licencia no son prototipos, y en una el mecanismo está medido.**
   `@pie-element/multiple-choice` va en **14.0.0** (con **2.514** versiones publicadas) y
   `@pie-element/rubric` en **9.0.0**. 🔴 **El campo `license` nunca se declaró** —vacío en las tres
   versiones muestreadas— **y el permiso se perdió en una MIGRACIÓN DE REPOSITORIO:** las versiones
   viejas apuntan a `pie-framework/pie-elements`, que **tiene texto** (`master/LICENSE.md` → **200**,
   *«Copyright 2019 CoreSpring Inc»* — el **ISC** que este archivo registra), y la **14.0.0** apunta a
   `pie-framework/pie-elements-ng`, donde **`LICENSE`, `LICENSE.md` y `COPYING` dan 404 en `main` y en
   `master`** mientras el repo responde. ⚠️ **Corrección para cualquiera que cite el ISC de esta
   librería: ese texto es del PREDECESOR, no de lo que npm sirve hoy.**
2. 🔵 **Hay un patrón de ALCANCE, no de paquete: `@timeback/*` va 2 de 2 sin licencia y sin
   repositorio** (`oneroster` en el pase 49, `caliper` en este). **Regla de cotización: el scope
   `@timeback` no entra en una entrega sin gestión previa**, y no hace falta medir el tercero.
3. 🔴 **La capa MCP de Open edX es AGPL-3.0 en PyPI, las dos piezas** (`openedx-mcp` 0.1.5,
   `tutor-contrib-openedxmcp` 0.1.7, la segunda **sin clasificador OSI**, así que un inventario que
   lea clasificadores la cuenta como desconocida). **AGPL es copyleft de RED y un servidor MCP es
   exactamente su caso de uso previsto:** exponerlo como servicio a un tercero **alcanza al
   servicio**. **O la puerta se construye propia sobre la API, o el engagement acepta AGPL en el
   componente que mira al cliente.**
4. ⚠️ **`@public-ui/mcp` es EUPL-1.2, no «como MIT».** La EUPL tiene cláusula de reciprocidad con
   compatibilidad explícita hacia otras copyleft. **Y viene con una colisión de nombre que un
   inventario por nombre no puede ver:** su repo es `public-ui/kolibri` (**EUPL-1.2**, texto leído en
   `master/LICENSE`), **que NO es el `learningequality/kolibri` MIT que `verticals/solutions.md`
   lista** (texto leído en `master/LICENSE`: *«MIT License»*). 🔵 **La clave de un inventario de
   licencias es `org/repo`, nunca el nombre del proyecto.**

### 🟢 El defecto de instrumento que este pase corrige, y corre en los DOS sentidos

El pase 49 estableció que **un CAMPO de licencia no es TEXTO de licencia**, con dos casos en una sola
dirección (campo MIT, cero texto). **Este pase encuentra la dirección inversa:**

| Paquete | Campo de registro | Texto en el repositorio | Qué hace un filtro de una sola lectura |
|---|---|---|---|
| **`@superbuilders/oneroster`** 0.7.0 | 🔴 **ninguno** | 🟢 `trilogy-group/oneroster-ts` **`main:LICENSE` → 200** | **lo RECHAZA, y está licenciado** |
| `@timadey/proctor` (pase 49) | MIT | 🔴 ninguno | **lo APRUEBA, y no hay permiso escrito** |

⚠️ **Los dos errores son del mismo instrumento mal usado, y cada uno cuesta en su dirección:** el que
sobre-aprueba crea riesgo legal, el que sobre-rechaza descarta la pieza correcta. **La regla
operativa: los dos artefactos siempre, y la discrepancia se REPORTA en vez de resolverse a favor de
ninguno.**

### 🟢 Y el control que distingue «no hay licencia» de «no llegué al repositorio»

De **19** repositorios declarados, **12 tienen texto de licencia alcanzable** (`main` o `master`).
⚠️ **De los 7 restantes, sólo 2 permiten concluir:**

- 🔴 **Sin licencia de verdad (el repo responde):** `pie-framework/pie-elements-ng` y
  `moinsen-dev/tool-teacher` (`master/README.md` → **200** en los dos).
- ⚠️ **Indeterminados (el repo no responde en `main`/`master`/`develop`, ni `README.md` ni
  `package.json`):** `owentaylor/canvas-mcp`, `Eduware-Inc/eduware-oneroster`,
  `LearningLocker/xapi-agents`, `osu-cass/sb-components`, `appliedrelevance/frappe_mcp_server`.
  **Su campo de registro dice una licencia y el texto no se pudo ver: no se publica ninguna de las
  dos conclusiones.**

🔵 **Dos conclusiones firmes y cinco indeterminadas declaradas es un resultado mejor que siete «sin
licencia», que es lo que el instrumento habría publicado sin el control — y el control cuesta una
petición HTTP por repositorio.** Es **P104** aplicado a licencias.

## 🎓 Capa de *student success* / alerta temprana — la capa que esta base declaró la PEOR abastecida, y tiene una pieza MIT desde 2022 (agregada en el pase 40 del 2026-10-02)

El **gap 26** y la **tendencia 26** de esta base dicen, desde el pase 11, que *«la capa que decide sobre el alumno es
la más regulada del sector y la peor abastecida de open source»*, y el pase 11 lo midió buscando **predictores**. La
acción 1 del pase 39 mandó barrer esta capa por **registro de paquetes**, y el barrido devuelve **un solo nombre en
903.402 de PyPI** — pero ese nombre cambia la conclusión.

| Repo | Licencia (verificada hoy) | Medición de primera mano | Qué aporta |
|---|---|---|---|
| 🟢 [`datakind/student-success-tool`](https://github.com/datakind/student-success-tool) | 🟢 **MIT** ✅ — `LICENSE.md` **200** en `main`, *«The MIT License (MIT) · Copyright (c) 2022 DataKind»* | `HEAD` **2025-09-08** · PyPI `student-success-tool` **0.3.10**, **14 releases**, último **2025-08-05** · **181 archivos `.py`** · Python **3.10–3.12** | **La única librería de *student success* con licencia permisiva que encontró esta base en 40 pases.** *«School-agnostic lib for implementing Student Success Tool workflows.»* Pipeline completo de **advising asistido por datos**: esquema base, ingesta, *feature engineering*, EDA, definición de *targets* por punto de control, **AutoML configurado por `config.yaml`**, reporting y datos sintéticos para pruebas |

### 🟢 Por qué esta pieza vale más de lo que su tracción sugiere: trae puesto el expediente regulatorio

**El problema de esta capa nunca fue el modelo. Era el expediente.** Un modelo que predice abandono estudiantil es,
en EMEA, **Anexo III punto 3 del AI Act** (evaluación de resultados de aprendizaje), y en North America cae bajo las
leyes estatales que esta base viene registrando —**supervisión humana obligatoria y prohibición de que la AI decida
en alto impacto** (Oklahoma, Maryland)—. Construir el modelo es la parte barata; **documentarlo para que pase una
auditoría es la cara.**

**Y esta librería trae esa parte hecha, en el árbol:**

| Componente | Ruta en el repo | Para qué sirve en el expediente |
|---|---|---|
| **Model cards** | `reporting/model_card/` (`base.py`, `pdp.py`, `custom.py`, `h2o_pdp.py`, `h2o_custom.py`) | **La documentación del modelo que el regulador pide**, generada desde el modelo entrenado y no escrita a mano |
| **Secciones de sesgo** | `reporting/sections/bias_sections.py` (+ variantes `pdp/` y `custom/`) | 🟢 **Análisis de sesgo como sección de reporte de primera clase** — no un notebook aparte |
| **Secciones de atributos y evaluación** | `reporting/sections/attribute_sections.py`, `evaluation_sections.py`, `metric_sections.py`, `registry.py` | Reporte por secciones registrables, extensible por institución |
| **Validación de ingesta** | `ingestion_validation/` | Controla el dato antes de que entre al modelo |
| **Datos sintéticos** | `generation/pdp/` | Permite demostrar el pipeline **sin dato real de alumno**, que es lo que destraba un piloto |

🔵 **Y los principios de producto están escritos en el README, lo cual importa porque son exactamente los tres que un
comité de ética universitario pregunta:** *transparente* (modelo y variables se comparten con la institución),
*dedicado a la reducción de sesgo*, y 🟢 ***«humans in the loop by design»*** — las intervenciones las ejecuta un
**asesor humano**, no el algoritmo. **Eso es la forma del requisito de Oklahoma y Maryland, por diseño y no por
cláusula.**

### El encuadre institucional, y el resultado reportado

**DataKind** es una organización sin fines de lucro; el trabajo está **financiado por Google.org** y desarrollado con
un equipo de *fellows*. El README reporta un resultado de despliegue: **John Jay College informó un aumento del 32 %
en la tasa de graduación de estudiantes de último año en dos años** con su programa CUSP sobre este enfoque.
⚠️ **Es una cifra auto-reportada en el README del proyecto, no un estudio independiente** — se cita como antecedente
de despliegue, no como evidencia de eficacia.

### ⚠️ Las tres reservas, declaradas antes de que alguien la cotice

1. 🔴 **Está acoplada a `PDP` y a Databricks, y eso define a quién le sirve.** El esquema base es el del
   **Postsecondary Data Partnership** —un estándar de datos de educación superior **de Estados Unidos**— y el camino
   de ejecución documentado es **Databricks Runtime 15.4 LTS / 16.x**. 🔵 **Hay una ruta `custom/` paralela a cada
   `pdp/`** (en `reporting/sections/`, `dataio/`, `preprocessing/`, `pipelines/`), así que **la customización está
   prevista por diseño**; pero fuera de PDP hay que escribir el esquema. **Para North America es casi reuso; para
   EMEA, APAC y LATAM es adopción del armazón con esquema propio.**
2. ⚠️ **Tibia, no viva:** `HEAD` del **2025-09-08** y último release del **2025-08-05** — **~13 meses**. Cae en la
   franja que el pase 37 definió como «hay que preguntar antes de depender». **No está archivada.**
3. 🔴 **PyPI no declara su licencia y el árbol sí.** El JSON de `student-success-tool` **no trae `license`,
   `license_expression` ni clasificador de licencia**; el **MIT se leyó en `LICENSE.md` del repo**. Es el **inverso
   del gap 81**: ahí la licencia vivía sólo en el manifiesto; acá vive sólo en el árbol. **Misma lección, signo
   opuesto: una sola fuente nunca alcanza.**

## 🎥 Capa de *proctoring* — existe, es oficial, y ~~es toda copyleft~~ (agregada en el pase 40 del 2026-10-02; 🔴 **la mitad copyleft del título quedó CORREGIDA en el pase 41 del 2026-10-02 — ver la corrección al final de la sección**)

El barrido por registro del pase 40 cierra esta capa, que esta base venía nombrando en consignas desde el pase 24 sin
haberla medido. **El resultado tiene la misma forma que los pases 8 y 9 encontraron en accesibilidad y credenciales:
lo maduro es copyleft y lo permisivo es chico.**

| Repo | Licencia (verificada hoy) | Medición de primera mano | Qué aporta |
|---|---|---|---|
| 🟢 [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | **AGPL-3.0 en el paquete** ⚠️ — `LICENSE.txt` **200** en `master` (texto AGPL v3 completo) — 🟢 **PERO `edx_proctoring/backends/` está *carved-out* en Apache-2.0** (`backends/LICENSE.txt`, 11.357 b, sin la palabra «Affero»; `backends/README.txt`, 174 b: *«These modules are licensed under Apache 2.0»*). ✅ **Verificado en el pase 41 en el *wheel* Y en el árbol** | `HEAD` **2026-05-30** · PyPI `edx-proctoring` **5.2.0**, 🔴 **253 releases** pero el último del **2025-04-28** · Python | **El subsistema de *proctoring* OFICIAL de Open edX.** Es la pieza de referencia de la capa: integra proveedores de supervisión con el flujo de examen del LMS, con los estados de examen, las excepciones y la auditoría ya modelados |
| ⚠️ [`openfun/xblock-proctor-exam`](https://github.com/openfun/xblock-proctor-exam) | **AGPL-3.0** | 🔴 `HEAD` **2021-02-11** — **5,6 años** · 4 releases | *XBlock* que restringe el acceso a una prueba al proceso de monitoreo de Proctor Exam. 🔴 **Muerto.** Se registra porque es **la opción EMEA de la capa** (France Université Numérique) y porque alguien va a encontrarla: **no proponer** |
| ⚠️ `grvlms-proctoring` | **AGPL-3.0** | 🔴 PyPI **2020-11-09** — **5,9 años** · 2 releases | Plugin de *proctoring* para Grvlms. 🔴 **Muerto** |
| 🔴 `proctoru-xblock` | 🔴 **sin licencia declarada** | 🔴 PyPI **2016-08-17** — **10,1 años** · 1 release | Integración con ProctorU. 🔴 **Muerto y sin licencia: inusable por dos motivos independientes** |

### 🔴 El dato de método que esta capa aporta, y aplica a toda la KB: el repo está vivo y el registro parado

**`edx-proctoring` tiene `HEAD` del 2026-05-30 (4 meses) y su último release en PyPI es del 2025-04-28 (17 meses).**
Las dos mediciones son correctas y dicen cosas distintas:

- 🟢 **Medido por repositorio: mantenido.** Hay trabajo reciente.
- 🔴 **Medido por registro: parado hace 17 meses.** Quien lo instale con `pip` recibe código de hace año y medio.

🔵 **Esto corrige un supuesto implícito del pase 37, que fechó 49 filas por el commit de su rama principal.** Para una
dependencia que se **instala**, la fecha que gobierna el riesgo **no es la del commit: es la del artefacto
publicado**. **Hay que medir las dos y decir cuál se usa** — y para `edx-proctoring`, que llega vía Tutor/pip en un
despliegue de Open edX, la que importa es la del registro. **Regla nueva: `HEAD` mide al proyecto, el release mide a
lo que el cliente instala.**

### 🔵 La lectura comercial de la capa, y es incómoda pero clara

**La única pieza seria de *proctoring* del ecosistema open source educativo es AGPL-3.0 y es parte de Open edX** — o
sea que **no hay opción permisiva para la capa que el AI Act regula más explícitamente**. Las dos piezas MIT que el
pase 40 encontró (`mereos`, `@timadey/proctor`, en `agents/top.md`) son **SDK de detección del lado del navegador**:
resuelven la mitad de visión por computadora, **no** la mitad de integración con el examen, los estados, las
excepciones y la auditoría, que es donde está el trabajo.

**Cómo se cotiza entonces:** sobre Open edX, `edx-proctoring` es adopción y la AGPL **ya está aceptada** porque el
LMS entero es AGPL — no agrega fricción. **Fuera de Open edX, la capa de integración hay que construirla**, y los SDK
MIT sirven como la mitad cliente. ⚠️ **Y antes de cualquiera de las dos rutas va el expediente del Anexo III punto 3,
cuyo plazo es el 2027-12-02** (el *«monitoreo durante exámenes»* está nombrado en el inciso).

### 🟢 La corrección del pase 41, y cambia la cotización de esta capa en los dos extremos

**La acción 3 del pase 40 pedía medir la superficie real de `edx-proctoring` y decidir si la capa se cotiza entera o
partida. Medida, el párrafo de arriba resulta equivocado en su conclusión más importante, y por dos motivos
independientes.**

**🟢 Motivo 1 — el punto de extensión no es AGPL: es Apache-2.0, y está dicho por el upstream en 174 bytes.**

| Archivo | Licencia | Evidencia |
|---|---|---|
| `dist-info/LICENSE.txt` (el paquete) | **AGPL-3.0** | *«GNU AFFERO GENERAL PUBLIC LICENSE Version 3»* |
| 🟢 **`edx_proctoring/backends/LICENSE.txt`** | 🟢 **Apache-2.0** | **11.357 bytes**; contiene *«Apache License / Version 2.0»*; 🟢 **no contiene «Affero»** |
| 🟢 **`edx_proctoring/backends/README.txt`** | — | **174 bytes**: *«The code in this directory is licensed under a license different from the rest of the edx-proctoring repository. These modules are licensed under Apache 2.0. See LICENSE.txt.»* |

✅ **Verificado en dos canales:** dentro del *wheel* `edx_proctoring-5.2.0-py2.py3-none-any.whl` **y** en el árbol
(`raw.githubusercontent.com/openedx/edx-proctoring/master/edx_proctoring/backends/{README,LICENSE}.txt` → **200** los dos).

🔵 **Lo que esto significa: el directorio donde se escribe un backend de proveedor está deliberadamente separado para que
un tercero lo escriba sin tocar la AGPL.** No es una ambigüedad ni un descuido: es un `README.txt` cuya única función es
decirlo.

**🟢 Motivo 2 — «fuera de Open edX hay que construir la capa» también es falso: existe, es MPL-2.0 y es de ETH Zürich.**
Ver la sección de **SEB Server**, abajo. **MPL-2.0 es copyleft débil por archivo**, no AGPL: un integrador construye al
lado sin abrir su propio código.

### 🟢 La superficie de `edx-proctoring`, enumerada — la respuesta es «implementar una interfaz», no «escribir la capa»

| Qué | Cuánto |
|---|---|
| Modelos de estado de examen | **12 clases**: `ProctoredExam`, `ProctoredExamReviewPolicy`(+`History`), `ProctoredExamStudentAttempt`, `ProctoredExamStudentAllowance`(+`History`), `ProctoredExamSoftwareSecureReview`(+`History`), `ProctoredExamSoftwareSecureComment` (+2 *managers* y 1 *queryset*) |
| Rutas REST | **20** (18 bajo `edx_proctoring/v1/…` + 2 *callbacks*) |
| 🟢 Borrado de datos | **ya modelado**: `v1/retire_user/<id>`, `v1/retire_backend_user/<id>` y el método `retire_user` del proveedor |
| Punto de extensión | **`ProctoringBackendProvider`**: **18 métodos + 8 atributos de clase** |
| 🔵 **`@abstractmethod`** | 🔵 **CERO** — es una base **concreta** con implementaciones por defecto: un backend mínimo sobreescribe **sólo lo que usa** |
| Base REST ya escrita | **`BaseRestProctoringProvider`** (`backends/rest.py`, 14.460 b, **27 métodos**, 8 constructores de URL) |
| Registro | ***entry point* de Django**, grupo **`[openedx.proctoring]`** — ya vienen `mock`, `null`, `rpnow4`, `software_secure` |

🟢 **Cómo se cotiza ahora, y reemplaza al párrafo anterior:** *«sobre Open edX no se construye la capa de proctoring: se
registra un entry point en `[openedx.proctoring]` y se sobreescriben los métodos de ciclo de vida del intento. La máquina
de estados, las excepciones, la política de revisión, las 20 rutas REST y las rutas de supresión de datos ya existen —
y el directorio donde va el código propio es Apache-2.0»*. Ver **P90** en `compose/patterns.md`.

⚠️ **Lo que NO cambia, y sigue gobernando el riesgo:** el último release en PyPI es del **2025-04-28** (**17 meses**).
La regla del pase 40 sigue en pie: `HEAD` mide al proyecto, el release mide lo que el cliente instala.

### 🔵 El grafo de importación, medido — el matiz que impide sobrevender la carve-out

**¿Es autocontenido el directorio Apache-2.0?** Medido con `ast` sobre sus 6 módulos no-test: 🔴 **no.** 🟢 **Pero lo que
cruza es vocabulario, no lógica:**

| Módulo AGPL al que entra `backends/` | Tamaño | Contenido | Quién lo importa |
|---|---|---|---|
| `constants.py` | 3.003 b | **0 clases, 0 funciones, 18 asignaciones** | `backend.py` |
| `exceptions.py` | 4.524 b | **24 clases, 0 funciones** | `rest.py`, `software_secure.py` |
| `statuses.py` | 11.088 b | **5 clases, 0 funciones** | `rest.py`, `software_secure.py` |
| ⚠️ `utils.py` | 17.205 b | **26 funciones** (lógica real) | 🔵 **sólo `software_secure.py`** (backend de referencia) |
| ⚠️ `callbacks.py` | 2.428 b | 1 función | 🔵 **sólo `mock.py`** |

🟢 **Un backend propio que subclasee `BaseRestProctoringProvider` importa del lado AGPL únicamente nombres de excepción y
valores de estado.** Los dos módulos con lógica los usan **sólo los backends que ya vienen en la caja**.

⚠️ **Y el límite honesto, que no se puede cerrar con una medición:** si eso convierte al backend en obra derivada **es una
pregunta legal, no de ingeniería**. El plugin corre dentro de un proceso Open edX que es AGPL completo de todos modos.
**Para un cliente que quiera vender el backend como producto separado, esta tabla es el insumo de la consulta legal, no su
respuesta.** **Gap 88: cerrado como medición, abierto como decisión de legales.**

## 🏛️ Capa de administración académica histórica — la familia **Kuali**, cuatro repos y los cuatro muertos (agregada en el pase 42 del 2026-10-02)

**El barrido global de plataformas de este pase devolvió la *Kuali Foundation* descrita en presente** (*«consorcio de más
de dos docenas de universidades que produce ERP, SIS y administración de investigación»*). 🔴 **Esta KB tenía 0 menciones
de Kuali en 41 pases, y la razón de que no las tuviera es la correcta: no hay nada vivo que proponer.** Se mide y se
registra **para que el próximo pase no lo descubra como novedad**, que es exactamente lo que le pasó a éste.

| Repo | Licencia (leída del archivo del árbol) | Rama defecto | `HEAD` | Máx. corregido entre ramas | Antigüedad | Qué es |
|---|---|---|---|---|---|---|
| [`kuali/rice`](https://github.com/kuali/rice) | 🟢 **ECL-2.0** (*Educational Community License v2.0*) | `master` · 11 ramas | 2017-05-17 | **2018-09-01** (`rice-2.5`) | 🔴 **~8 años** | El *middleware* de la pila (workflow, IAM, formularios) |
| [`KualiCo/rice`](https://github.com/KualiCo/rice) | 🟢 **ECL-2.0** | `java11` · 13 ramas | 2020-07-01 | **2020-07-01** | 🔴 **~6 años** | El fork comercial del *middleware*, migrado a Java 11 |
| [`kuali/kc`](https://github.com/kuali/kc) | 🔴 **AGPL-3.0** | `master` · 12 ramas | 2017-01-06 | 2017-01-06 | 🔴 **~9 años** | *Kuali Coeus*: administración de investigación (*grants*, propuestas, IRB) |
| [`kuali/kfs`](https://github.com/kuali/kfs) | 🔴 **AGPL-3.0** | `master` · 35 ramas | 2018-03-22 | 2018-03-22 | 🔴 **~8 años** | *Kuali Financial System*: finanzas institucionales |

🔴 **`KualiCo/kc`, `KualiCo/kfs` y `KualiCo/kuali-student` NO existen** (`git ls-remote` falla en los tres).

🔵 **La forma de este hallazgo se repite en esta base y conviene nombrarla:** **el *middleware* es permisivo y las dos
aplicaciones que un cliente querría —investigación y finanzas— son AGPL.** Es el mismo reparto que `edx-proctoring`
(núcleo AGPL, `backends/` Apache-2.0) y que `lrsql`/`Ralph` contra Learning Locker. **La licencia usable suele estar en la
capa que no resuelve el problema del cliente.**

⚠️ **Qué se hace con esto en un *engagement*:** nada como dependencia. 🟢 **Sirve como dato de contexto en educación
superior de North America** —estos sistemas siguen en producción en universidades que los instalaron antes de 2018— y
**como argumento de migración**: un cliente con Kuali instalado tiene una pila sin mantenimiento *upstream* desde hace
6-9 años. 🔴 **No se cita como «open source disponible»: se cita como deuda.**

### ⚠️ Y la cuarta confirmación independiente de la clase `dependabot`

`KualiCo/rice` tiene su rama más nueva en `dependabot/maven/com.fasterxml.jackson.core-jackson-databind-2.9.10.7`
(**2021-01-21**), **7 meses «más fresca» que la vida real del repositorio**. **Es un repo fuera de `agents/top.md`, así que
confirma la clase que el pase 42 agregó al instrumento de vitalidad sin reusar la misma evidencia.**

## 🗓️ Capa de *timetabling* — la capa que el pase 40 midió vacía de agente tiene una base Apache-2.0 con API de conectores (agregada en el pase 41 del 2026-10-02)

**El pase 40 midió que `unitime` no devuelve ni un nombre en los 903.402 del índice de PyPI y concluyó que la capa de
*timetabling* estaba vacía.** Medida por su repositorio, la conclusión se parte en dos: **vacía de agente, sí; vacía de
software, no.**

| Repo | Licencia (leída del árbol) | Medición de primera mano | Qué aporta |
|---|---|---|---|
| 🟢 [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** — `LICENSE` + `NOTICE` (*«Copyright 2015, The Apereo Foundation»*) | `HEAD` **2026-10-01** (ayer) · **202 tags** · **4.154 archivos** · Java · `git ls-remote` + clon del árbol | **El sistema de horarios y exámenes académicos de referencia del mundo open source** (Apereo; origen Purdue University). Resuelve asignación de cursos, aulas, exámenes y *student scheduling*. 🟢 **Y lo que lo vuelve cotizable para una puerta de agente: expone una API formal con conectores CON NOMBRE** |

🟢 **La API, que es el hallazgo: `org.unitime.timetable.api`**

- **`ApiConnector`** (clase abstracta): `doGet` / `doPut` / `doPost` / `doDelete` + **`getName()`**.
- **Autenticación por token ya incluida:** `authenticateWithTokenIfNeeded()`, parámetro `?token=`, propiedad
  `ApiCanUseAPIToken`.
- *Helpers* de serialización: `JsonApiHelper`, `XmlApiHelper`, `BinaryFileApiHelper`.
- 🟢 **15 conectores registrados**, cada uno con su nombre de ruta (`/api/<nombre>`): `rooms` (**GET/POST/PUT/DELETE**),
  `buildings`, `events`, `sectioning`, `exchange`, `var-title-crs`, `json`, `curricula`, `enrollments`, `instructors`,
  `instructor-schedule`, `roles`, `student-groups`, `class-info` y 🔴 **`script`**.

🔵 **Por qué esto es mejor que cualquier LMS que esta base haya medido para envolver como MCP: el conector YA es la
unidad.** Tiene nombre propio, verbos explícitos y autenticación por token — **el mapeo a *tools* de MCP es 1:1**, sin
inferir nada del HTML ni de un cliente.

🔴 **Y la advertencia que va antes de la primera línea de código: existe un conector llamado `script` que acepta `POST`.**
Un envoltorio ingenuo de los 15 conectores **expone ejecución de scripts del servidor como una tool**. **Va en la
*denylist* del *gateway* del pase 40 (P85) antes de cualquier demo.** Ver **P88**.

## 🔒 Capa de integración de examen — SEB Server, la pieza permisiva que el pase 40 dijo que no existía (agregada en el pase 41 del 2026-10-02)

| Repo | Licencia (leída del árbol) | Medición de primera mano | Qué aporta |
|---|---|---|---|
| 🟢 [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | ⚠️ **MPL-2.0** — `LICENSE` en `master` | 🔴 `master` **2026-04-01** / 🟢 **`dev-3.0` 2026-10-01** · **108 tags** (incl. `v3.0-latest`) · **1.450 archivos** · Java (`ch.ethz.seb`) | **La capa de administración, monitoreo y *proctoring* de exámenes**. 🔴 **Re-enumerada en el pase 44 sobre `master` (`7f45689`): las dos cifras de este renglón estaban mal.** Son **31 controladores REST de producción** (no 36) y **55 constantes de *endpoint*** (no 41). El `@RestController` aparece en **35 archivos** del repo: **31** en `webservice/weblayer/api` (la superficie real), **3** en `src/test` (`*TestController`, no se despliegan) y **1** —`WebSecurityConfig`— que es `@RestController` + `ErrorController` en `src/main`, o sea el manejador de error, no un endpoint. Y de las 55 constantes, **41 son literales y 14 compuestas** (`OTRO_ENDPOINT + "/sufijo"`): **el «41» era exactamente el subconjunto que un extractor de literales puede ver** (tendencia **167**). Es el lado servidor que los SDK de navegador de `agents/top.md` no cubren. 🟢 **Enumerada en el pase 42 sobre `dev-3.0`: 1.201 archivos versionados, 313 `.java` en `webservice/servicelayer/`, 75 de *proctoring*. SPI de proveedor = `RemoteProctoringService` (14 métodos, 2 `default`, 🔴 12 obligatorios), registro ABIERTO por inyección de Spring, 🔴 tipo CERRADO (`enum ProctoringServerType{JITSI_MEET,ZOOM}`): un proveedor propio obliga a tocar 1 archivo *Covered* y a publicar ese valor de enum. `LmsType` tiene 6 valores y `LMS_FULL_INTEGRATION` sólo con Moodle+plugin** |
| 🟢 [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) | ⚠️ **MPL-2.0** — `LICENSE.txt` | 🟢 `HEAD` **2026-09-25** · **20 tags** · **1.452 archivos** · C# | **El cliente de bloqueo de escritorio (Windows)**: convierte la máquina en estación de examen y restringe funciones del sistema, sitios y aplicaciones |

⚠️ **MPL-2.0 no es MIT/Apache, y tampoco es AGPL: es copyleft DÉBIL por archivo.** Lo que se modifica de los archivos
cubiertos se publica; **lo que se agrega al lado, no.** Para un integrador es usable **sin abrir su propio código** —
que es exactamente la fricción que la AGPL de `edx-proctoring` sí impone fuera de Open edX.

🟢 **El dato que lo vuelve componible con esta KB, y no es la licencia: su `enum LmsType` ya nombra tres de las
plataformas fundacionales de este archivo.**

| `LmsType` | *Features* declaradas | ¿Ya está en esta KB? |
|---|---|---|
| **`OPEN_EDX`** | `COURSE_API`, `SEB_RESTRICTION` | 🟢 sí |
| **`MOODLE`** | `COURSE_API`, `COURSE_RECOVERY` (⚠️ `SEB_RESTRICTION` comentada en el fuente) | 🟢 sí |
| 🟢 **`MOODLE_PLUGIN`** | `COURSE_API`, `COURSE_RECOVERY`, `SEB_RESTRICTION`, 🟢 **`LMS_FULL_INTEGRATION`** | 🟢 sí — **la única con integración completa** |
| **`OPEN_OLAT`** | `COURSE_API`, `SEB_RESTRICTION` | 🟢 sí |
| `ANS_DELFT` | `COURSE_API`, `SEB_RESTRICTION` | no |

🔴 **El dato de método que esta pieza aporta, y obliga a corregir el instrumento del pase 37: la rama por defecto puede ser
la rama MUERTA de un proyecto vivo.** `master` mide **6 meses**; `dev-3.0` commiteó **ayer**. Medido con
`ls-remote --symref HEAD`, SEB Server se registraría como *«FRÍO»* y sería **falso**. Ver la tendencia **152**.

⚠️ **Lo que queda sin resolver, y es de despliegue, no de licencia: cuál rama se instala.** Hay tag `v3.0-latest` y una
`dev-3.0` activa contra un `master` de 6 meses. **Antes de proponerlo hay que decidir si el entregable se para en el
release o en la rama**, que es la misma pregunta de la tendencia 147 con las dos respuestas invertidas. Queda como
**gap 87**.


## 🧩 Capa de rostering OneRoster — el lado PROVEEDOR, que esta base nunca tuvo (agregada en el pase 38 del 2026-10-02)

**Treinta y siete pases trataron OneRoster como un problema de cliente.** La base tenía `oneroster-ts` (0BSD, 132 tools)
como *«la superficie de tools más grande de toda esta base»* y `@timeback/oneroster` declarado no-alta. El pase 37 fechó
`oneroster-ts` en **2025-06-27 — 15,2 meses sin un commit en `main`**, y lo único que se movió desde entonces fueron
cuatro ramas de Dependabot y un regenerador de SDK, **ninguna mergeada**. Este pase va a buscar reemplazo y encuentra
algo distinto de lo que buscaba: **el lado servidor del estándar, que es permisivo, está vivo y nadie en esta base había
mirado.**

| Repo | Licencia (verificada hoy) | Medición de primera mano | Qué aporta |
|---|---|---|---|
| 🟢 [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | **Apache-2.0** ✅ (`LICENSE` **200** en `main`) | `HEAD` **2026-10-01** · **86 tags**, último **v1.0.2** · 6 ★ · Node.js | **Sirve una API OneRoster 1.2 desde una base Ed-Fi ODS.** **14 endpoints GET**: `academicSessions`, `classes`, `courses`, `demographics`, `enrollments`, `orgs`, `users`, `schools`, `students`, `teachers`, `gradingPeriods`, `terms` y recuperación por id. Query params `limit`/`offset`, `sort`/`orderBy`, `filter`, `fields`. **Ed-Fi Data Standard 4.0 y 5.0/5.1/5.2.** Despliegue por **Docker** (guía de stack completo) o IIS/Windows |
| 🟢 [`CSR2017/edfi-oneroster`](https://github.com/CSR2017/edfi-oneroster) | **Apache-2.0** ✅ (`LICENSE` **200** en `main`) | `HEAD` **2026-09-22** · 8 tags · 13 ramas | Misma descripción y mismo propósito. 🔴 **Cuál de los dos es upstream NO se resolvió este pase → `gap 79`.** Hasta resolverlo, citar el de la Alliance: tiene 86 tags y commit de ayer |
| 🟢 [`TCI/OneRoster`](https://github.com/TCI/OneRoster) | **MIT** ✅ (`LICENSE.txt` **200** en `master`) | `HEAD` **2026-09-11** · 35 tags, último **v2.3.27** · 4 ★ · Ruby · 122 commits | **El lado cliente, vivo.** Wrapper de consumo (no servidor) para `students`, `teachers`, `classes`, `classrooms`, `courses`, `enrollments`, con filtrado por `sourcedId`. Publicado en rubygems. Config por `app_id`/`app_secret`/`api_url` |

### ⚠️ La rareza de gobernanza, que hay que saber antes de nombrar el proyecto en una reunión

El repo de la Alliance vive en la organización **Ed-Fi-Alliance-OSS**, pero su aviso de copyright dice **«Copyright (c)
2025 1EdTech Consortium, Inc. and contributors»**. 🔵 **Es un artefacto conjunto de los dos consorcios que esta base
venía tratando como mundos separados** —Ed-Fi del lado del dato del distrito, 1EdTech del lado del estándar de
interoperabilidad— y **es el primero de esta KB con esa doble firma** (**tendencia 135**). ⚠️ **No declara certificación
1EdTech en el repo: no afirmar que está certificado.** Que un estándar tenga implementación de referencia permisiva no
equivale a que esa implementación esté certificada, y es una distinción que un cliente de distrito sí hace.

### 🔴 El dato que decide cómo se cotiza esta capa: seis de ocho implementaciones no se pueden usar

El barrido abierto de OneRoster devuelve **ocho** implementaciones. Medidas hoy una por una:

| Repo | `HEAD` | Antigüedad | Veredicto |
|---|---|---|---|
| `Ed-Fi-Alliance-OSS/edfi-oneroster` | 2026-10-01 | 0 d | 🟢 usable |
| `CSR2017/edfi-oneroster` | 2026-09-22 | 9 d | 🟢 usable |
| `TCI/OneRoster` | 2026-09-11 | 20 d | 🟢 usable (Ruby) |
| `trilogy-group/oneroster-ts` | 2025-06-27 | 15,2 meses | 🔴 congelado (0BSD) |
| `jdolny/OneRoster.NET` | 2023-10-13 | 3,0 años | ⚫ muerto |
| `gotranseo/oneroster` | 2023-05-01 | 3,4 años | ⚫ muerto |
| `bgwdotdev/go-oneroster` | 2019-11-04 | 6,9 años | ⚫ muerto |
| `EASOL/edfi-to-oneroster` | 2016-10-19 | 10,0 años | ⚫ muerto |

🔵 **OneRoster es un estándar con mucho código escrito y poco código mantenido.** La consecuencia práctica: un barrido
por *«existe una librería para esto»* da ocho respuestas de las que **seis no se pueden poner en un entregable**, y la
diferencia sólo se ve fechando los repos. 🔴 **El residuo honesto: no hay cliente OneRoster permisivo y vivo en
TypeScript.** `oneroster-ts` está congelado, `@timeback/oneroster` ya era no-alta, y el único cliente vivo es Ruby. Eso
es candidato a **contribución *upstream* propia**, no a seguir buscando.

## 🔄 Re-fechado de la capa LRS, y es la medición que contiene el riesgo de la puerta xAPI congelada (pase 38 del 2026-10-02)

El pase 37 dejó `DavidLMS/learnmcp-xapi` congelado hace 13,1 meses con **42 menciones en `compose/patterns.md`**. La
pregunta que importa no es si el adaptador está frío, sino **si el dato del cliente queda atrapado**. No queda: la
v2.0.0 de `learnmcp-xapi` trae **sistema de plugins de LRS** (SQLite, Ralph, Veracity), o sea que el LRS se cambia **por
variable de entorno**. Y los dos LRS permisivos que esta base recomienda hace 33 pases están vivos:

| LRS | Licencia | `HEAD` medido hoy | Último semver | Motores verificados | Región |
|---|---|---|---|---|---|
| 🟢 [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** ✅ | **2026-10-01** (ayer) | **v0.9.9** | SQLite 3.42 · Postgres 14–18 · MariaDB 10.6–11.8 · MySQL 8.0.44–9.5.0 | North America (Yet Analytics, Inc.) |
| 🟢 [`openfun/ralph`](https://github.com/openfun/ralph) | **MIT** ✅ (`LICENSE.md`: *«(c) 2020-present France Université Numérique»*) | **2026-09-07** | **v5.0.1** | Elasticsearch verificado en README; los **14 extras** de `ralph-malph` ya inventariados en este archivo (pase 34) | EMEA (France Université Numérique) |

🔵 **Corrección de orden respecto de lo que este archivo afirmaba:** los **115 tags** de `lrsql` incluyen etiquetas de
pre-release, y un orden ingenuo devuelve `v1.0.0-pre_ui_testing` como «última». **El último semver limpio es `v0.9.9`.**
No citar un 1.0.0 de `lrsql`: no existe como release estable.

🟢 **La lectura de riesgo que esto habilita, y es la que va a una propuesta:** lo congelado no es la telemetría, es un
adaptador de ~32 commits sobre dos LRS vivos, permisivos, mantenidos por organizaciones **distintas** en regiones
**distintas** —una de ellas pública europea—. Costo de adopción acotado y medible, que es la condición que **P78**
pedía verificar. 🔴 **Lo que NO sirve como mitigación: el fork `ashleycribb/learnmcp-xapi`.** Tiene `main` 13 meses más
nuevo y **2 commits adelante, los dos de configuración de Cloud Run** (ver `agents/trending.md`, pase 38).


## 🧪 Capa de conformidad y simulación xAPI, y el validador oficial de credenciales — agregada en el pase 34 del 2026-10-02

**Treinta y tres pases recomendaron `lrsql` o Ralph sin tener con qué dimensionarlos.** Esta capa cierra eso. **Las dos
piezas aparecieron por el mismo instrumento —el nombre de la organización (tendencia 100)—, no por búsqueda de término.**

| Repo | Licencia | Verificación de primera mano | Qué aporta |
|---|---|---|---|
| [`yetanalytics/datasim`](https://github.com/yetanalytics/datasim) | **Apache-2.0** ✅ | `LICENSE` **200** (`master`), `README.md` **200**, `deps.edn` **200**, imagen Docker **2025-12-02** | **Genera datos xAPI simulados a escala.** *«benchmark and stress-test … with the Total Learning Architecture»* y *«evaluate the implementation of xAPI data design using the xAPI Profile specification»*. **Mismo mantenedor que `lrsql`.** Origen: **ADL Initiative** (DoD EE. UU.) |
| [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) | **Apache-2.0** ✅ | `LICENSE` **200** en `main` **y** `master` | Validador **del consorcio que escribe el estándar**, para **Open Badges** y **CLR**, con web, HTTP y API |

🟢 **Por qué `datasim` cambia una propuesta y no sólo un repo.** Permite **cargar el LRS con tráfico sintético conforme
a un xAPI Profile antes de comprometer una cifra**. Es la diferencia entre proponer una arquitectura de telemetría y
haberla probado — y como viene del mantenedor de `lrsql`, la combinación es la que el propio proyecto usa. Resuelve
además una carencia que esta base arrastraba: **los xAPI Profiles entraron en la consigna del pase 24 y el pase 25 los
buscó sin encontrar herramienta.**

🟢 **Por qué el validador de 1EdTech cierra un expediente.** Este archivo registraba que *«las implementaciones de
referencia de estos estándares ya no están»* (`badgr-server` **404**, `caliper-php` en privado). El validador **está, es
Apache-2.0, y lo publica 1EdTech**: convierte *«cumplimos Open Badges»* en una afirmación **verificable por un tercero
neutral**, que es lo que pide un área de compras. Ver **P74**.

### ⚠️ La no-alta de esta capa, declarada: `yetanalytics/persephone`

Docker Hub la describe como *«a Clojure CLI and server app for validating xAPI Statements against Profiles»* —
**exactamente** la capa de este apartado. **No entra.** Se probaron **10 rutas de licencia** (`LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `license`, `COPYING`, cada una en `main` y `master`): **las diez 404**; `project.clj` y `deps.edn`
**404**; `README.md` **404** en las dos ramas; **3 tags en Docker Hub, el último de 2023-10-10 (~3 años)**. 🔴 **Sin
licencia leída no entra a ninguna tabla de esta KB**, que es la regla que el pase 31 aplicó a Caliper. **Gap 68.**

### 🔵 Y la contribución *upstream* que esta capa deja identificada, con el sitio exacto

`ralph-malph` 5.0.1 declara **14 extras** —`backend-clickhouse`, `-es`, `-ldp`, `-lrs`, `-mongo`, `-s3`, `-swift`,
`-ws`, `backends`, `cli`, `lrs`, `dev`, `ci`, `full`— y **ninguno es MCP** (medido en `provides_extra` de PyPI, junto
con `requires_dist` sin `mcp` y **0 menciones** en la descripción). **Eso es una superficie de plugins ya empaquetada:**
un **`ralph[mcp]`** encaja en la convención del proyecto y **no requiere fork**. Ralph es **MIT** y su `LICENSE` nombra
a **France Université Numérique**, así que es también el camino con mejor argumento institucional para EMEA. Ver **P71**
y **gap 64 (cerrado en negativo)**.

## 🧮 Capa de interacciones de evaluación — permisiva, madura y de modelo propio (agregada en el pase 37 del 2026-10-02)

**Esta base tenía la capa de evaluación mal abastecida en permisivo, y lo tenía medido.** El pase 36 cerró **P69** con:
*«lo activo y desplegado es copyleft, lo permisivo es lo nuevo»* —`qtism/qtism` **GPL-2.0-only** con 218.212 descargas y
293 versiones, `oat-sa/extension-tao-testqti` **GPL-2.0-only** con 885 versiones y release de hace dos días, contra
`@longsightgroup/qti3-cli` **MIT** nacido el 2026-05-21. 🟢 **La segunda mitad de esa frase queda refutada.**

| Campo | Valor medido el 2026-10-02 |
|---|---|
| Repo | [`pie-framework/pie-elements`](https://github.com/pie-framework/pie-elements) |
| Licencia | 🟢 **ISC** por el cuerpo de `LICENSE.md` (`Copyright 2019 CoreSpring Inc`) — ⚠️ con contradicción, abajo |
| `HEAD` (rama por defecto `develop`) | 🟢 **2026-09-22** |
| Publicación | 🔵 **2.226 versiones** en npm, desde **2019-05-31**; última modificación **2026-10-01** |
| Refs en el repo | **51.410** |
| Qué contiene | Interacciones de evaluación como *web components*, cada una con sub-paquetes **`configure`** (autoría) y **`controller`** (*scoring*): `multiple-choice` (v13.4.4), `rubric` (v8.2.4), `complex-rubric` (v7.2.4), `graphing` (v10.2.5), `drawing-response` (v12.2.4), `math-inline` (v12.2.4), `extended-text-entry` (v15.2.5)… |
| Verificación | `ls-remote` + `fetch --depth 1`, `LICENSE.md` y `package.json` crudos, y los paquetes pedidos **por nombre exacto** a `registry.npmjs.org` |

### 🔵 Qué cambia, y es un trade-off de tres patas en vez de una recomendación

**Ninguna de las tres opciones domina a las otras dos, y la que se propone depende de lo que el cliente ya tenga puesto:**

| Opción | Licencia | Madurez | Conforme al estándar | Cuándo se propone |
|---|---|---|---|---|
| `pie-elements` | 🟢 **ISC** | 🟢 **7 años, 2.226 versiones, activo** | 🔴 **No — modelo de ítem propio** | Cuando el cliente construye su propio banco y no tiene que **intercambiar** ítems con nadie |
| `@longsightgroup/qti3-cli` + `qti3-item-player` | 🟢 **MIT** | ⚠️ **nuevo (2026-05-21)** | 🟢 **QTI 3** | Cuando hay que **importar o exportar** ítems, o la licitación pide QTI |
| `qtism/qtism` + TAO | 🔴 **GPL-2.0-only** | 🟢 **el más desplegado del mundo** | 🟢 **QTI 2.x** | Cuando el cliente **ya corre TAO** y el copyleft no es obstáculo |

🔴 **El motivo por el que `pie-elements` no desplaza a la pila QTI, y conviene decirlo antes de que lo pregunte el cliente:**
la **tendencia 29** de esta base —medida en cinco capas— dice que *«lo que inventa su propio modelo de dominio no escala, lo
que se conecta al estándar instalado sí»*. `pie-elements` es el caso más fuerte **a favor** que esta KB encontró
—sobrevivió siete años con modelo propio— **y sigue siendo el lado débil cuando hay interoperabilidad en el pliego.**

### 🔴 La contradicción de licencia, que es de una clase nueva para esta base: el manifiesto contra el archivo

| Canal | Qué declara |
|---|---|
| `LICENSE.md` (`develop`) | **cuerpo del texto ISC**, `Copyright 2019 CoreSpring Inc` |
| `package.json` de la raíz | 🔴 **`"license": "MIT"`** (y `"private": true`) |
| `@pie-element/{rubric,drawing-response,math-inline,graphing,extended-text-entry}` | **`ISC`** |
| 🔴 **`@pie-element/multiple-choice` v13.4.4** | 🔴 **ningún campo `license`** |

🔵 **La regla del pase 10 era «verificar contra el archivo `LICENSE`, no contra el README». Este caso la endurece: el
archivo `LICENSE` le gana al MANIFIESTO — y el manifiesto es exactamente lo que leen los escáneres de licencia
automáticos.** Un *due diligence* devuelve **MIT** si entra por la raíz, **ISC** si entra por los paquetes, y **nada** si
entra por `multiple-choice`, que es la interacción más central de cualquier evaluación.

⚠️ **Impacto comercial: chico pero no nulo.** ISC y MIT son las dos permisivas y las dos sirven, **así que el resultado no
cambia**; lo que cambia es que hay que **resolver el paquete sin campo por el `LICENSE.md` del repo** y dejarlo asentado en
el expediente. 🟢 **ISC es licencia nueva para esta KB** — la tercera «permisiva que los filtros no reconocen» después de
**ECL-2.0** (tendencia 27) y **0BSD** (pase 28), y **funcionalmente equivalente a MIT**.

### 🔴 La no-alta de esta capa, declarada: `@timeback/oneroster`

Apareció buscando reemplazo para `trilogy-group/oneroster-ts` (congelado hace **15,2 meses**). **58 versiones, última
2026-09-25** — activo. 🔴 **No declara licencia, ni repositorio, ni *homepage*.** **Sin licencia declarada no es open
source: es código publicado.** No entra (**gap 75**), y el hueco de reemplazo de OneRoster **sigue abierto**.

### ⚠️ Dos límites del buscador de npm, medidos, que explican por qué el barrido por registro rinde poco

- 🔴 **Dos palabras se resuelven como OR y se ordena por descargas:** `xapi mcp` → **110.769** resultados encabezados por
  `@modelcontextprotocol/sdk` y `@storybook/addon-mcp`; **el paquete del dominio queda sepultado**.
- 🔴 **El calificador `scope:` no está soportado:** `text=scope:pie-element` → **2.403.867** resultados, primera página
  `locate-path`, `strip-ansi`, `@types/node`.

🔵 **La regla: el registro sirve para CONFIRMAR un nombre que ya se tiene, no para DESCUBRIR.** Los nombres se descubren por
**organización** (tendencia 112), por **README crudo** o por el **árbol de refs** — los tres canales que sí rindieron
(tendencia **127**).


## 🧭 La adopción medida en descargas, no en estrellas — y tres capas de esta base cambian de orden (pase 33 del 2026-10-02)

**Treinta y dos pases midieron adopción con estrellas de GitHub. El registro de paquetes publica descargas por mes, y
las dos series no se parecen — en los dos sentidos.** Esta sección es el resultado de aplicar el instrumento nuevo a las
bases que esta KB ya tenía catalogadas, más las altas que el barrido por **nombre de proyecto implementador** trajo
(consigna del pase 32, ejecutada sobre **npm, PyPI y Packagist**).

### El instrumento, y la regla que deja

| Base | Licencia | ★ | Descargas total / mes | Último release | Lectura |
|---|---|---|---|---|---|
| `learninglocker/learninglocker` | 🔴 GPL-3.0 | **583** | 🔴 **2.960 / 0** | **2017-04-04** | **No se propone.** Cerrado por medición, no por rumor |
| `RusticiSoftware/TinCanPHP` | **Apache-2.0** ✅ | 88 | 🔵 **863.777 / 6.178** | 🔴 **2019-03-05** | El cliente xAPI más desplegado del planeta, **y es permisivo** |
| `RusticiSoftware/TinCanPython` (PyPI `tincan` 1.0.0) | **Apache-2.0** ✅ | — | 5 releases | 🔴 **2020-09-03** | Permisivo y congelado |
| `php-xapi/client` + familia `php-xapi/*` | **MIT** ✅ | 23 | 48.104 / 825 | 🔴 2021-03-24 | Pila xAPI modular MIT, congelada |
| `qtism/qtism` (`oat-sa/qti-sdk`) | 🔴 **GPL-2.0-only** | 85 | **218.212 / 3.104** | **2026-07-09** (v19.7.2, **293 versiones**) | **El QTI que el mundo despliega es copyleft** |
| `oat-sa/extension-tao-testqti` | 🔴 **GPL-2.0-only** | **8** | **117.544 / 950** | **2026-09-30** (**844 versiones**) | **8 estrellas e infraestructura desplegada.** El mejor caso de la tendencia 23 |

🔵 **La regla, y aplica a toda esta base de acá en adelante:** **las estrellas miden interés; las descargas por mes miden
despliegue.** Cuando se contradicen, la que decide una propuesta es la segunda. Y la fecha que importa para promover una
pieza a dependencia de patrón **no es la del primer release, es la del último**.

### 🔴 La capa de evaluación queda bien medida, y la conclusión es más fuerte que las dos anteriores

El pase 28 escribió *«el QTI utilizable es PHP»*; el pase 32 dijo que `qti3` lo **rompía**. **Las dos frases eran
parciales porque ninguna midió licencia y despliegue a la vez.** Medido:

- **Lo desplegado es copyleft.** `oat-sa/qti-sdk` → **GPL-2.0-only**, 218.212 descargas, 293 versiones, activo.
  `oat-sa/extension-tao-testqti` → **GPL-2.0-only**, 117.544 descargas, 844 versiones, release del **2026-09-30**.
  🔴 **No sirven para un entregable cerrado**; sirven como referencia y como aviso de que el cliente institucional grande
  probablemente **ya tiene TAO adentro**.
- **Lo permisivo es nuevo y chico, y es todo lo que hay.** `@longsightgroup/qti3-*` (**MIT**, 0.13.1 del **2026-10-01**,
  12 paquetes) para **QTI 3**, e `instructure/qti` (**MIT**, 174 commits) para el acervo **QTI 1.2**.
- 🔵 **Eso no debilita P20 ni P48: los vuelve el único camino permisivo.** Pero **obliga a declarar el riesgo de madurez
  por delante**, no a esconderlo detrás de la palabra «MIT».

### 🟢 Altas de base de este pase: la pila QTI 3 permisiva, enumerada — y dos piezas que abren la capa de accesibilidad

**`LongsightGroup/qti3` — MIT, versión 0.13.1 publicada el 2026-10-01.** El pase 32 registró «12 paquetes» sin
enumerarlos. Enumerados y verificados en el registro:

| Paquete | Licencia | Dependencias de terceros | Qué aporta |
|---|---|---|---|
| `@longsightgroup/qti3-core` | **MIT** ✅ | 🔵 **cero** | Parseo XML sin dependencias, validación, *response processing*, **scoring**, metadatos de soporte y **estado de intento serializado**. No renderiza UI ni depende de framework. Expone `parseQtiXml`, `validateAssessmentItem`, `createItemSession` (`respond`/`score`) |
| 🟢 `@longsightgroup/qti3-a11y` | **MIT** ✅ | sólo `qti3-core` | 🔵 **La pieza que P17 necesitaba y esta KB declaraba inexistente en permisivo.** `a11yContracts`, **`accessibilityProofMatrix`** y **`manualAssistiveTechnologyScripts` para VoiceOver, NVDA y JAWS**. Contratos de teclado, foco, nombre accesible y mensaje de validación por tipo de interacción: **metadato de prueba, legible por máquina** |
| 🟢 `@longsightgroup/qti3-pnp` | **MIT** ✅ | 🔵 **cero** | Resolutor de **QTI 3 *Personal Needs and Preferences***: `parseQti3PnpXml` → `normalizeQti3Pnp` → `resolveQti3Pnp` contra capacidades del *player* y catálogo QTI, con diagnósticos de perfil |
| `@longsightgroup/qti3-cli` | **MIT** ✅ | sólo paquetes hermanos | **14 comandos, todos emiten JSON** (ver abajo) |
| `@longsightgroup/qti3-transcoder` | **MIT** ✅ | — | QTI 3 → QTI 1.2 y 2.x, por perfil |
| `@longsightgroup/qti3-migrator` | **MIT** ✅ | — | QTI 1.2 / 2.x → 3 |
| `@longsightgroup/qti3-player-react` · `-player-preact` | **MIT** ✅ | — | Adaptadores TSX del *web component* del player |
| `@longsightgroup/qti3-conformance` · `-fixtures` | **MIT** ✅ | — | Corredor de *fixtures* y *fixtures* sintéticos con resultados de scoring esperados |

⚠️ **La frontera que `qti3-pnp` declara en su propio README, y conviene citarla textual en un *discovery* porque es
exactamente el presupuesto del integrador:** *«It does not fetch, store, authorize, or transmit PNP records. LMS
identity, consent, institutional policy, persistence, LTI launch handling, and AfA PNP service access belong outside this
package.»* 🔵 **Es la primera base de esta KB que escribe qué NO hace con ese nivel de precisión** — identidad, consentimiento,
política institucional, persistencia, *launch* LTI y el servicio AfA PNP **son trabajo a cotizar**, no configuración.

### 🔵 `qti3-cli`: por qué «envolvible como MCP en días» ya no es una afirmación

**`@longsightgroup/qti3-cli` 0.13.1 (MIT), `bin: { qti3 }`, cero dependencias de terceros en runtime.** Catorce comandos:

| Comando | Modo | Qué emite |
|---|---|---|
| `parse <item.xml>` | lectura | El modelo de ítem parseado, **como JSON** |
| `validate <item.xml>` | lectura | Diagnósticos de validación, **como JSON** |
| `score <item.xml> --responses <r.json>` | lectura | Resultado completo: diagnósticos, estado, respuestas, *outcomes* y puntaje |
| `score-correct <item.xml>` | lectura | Puntúa con la respuesta correcta autorada |
| `prepare-delivery` | **escritura con `--out`** | XML apto para el candidato. ⚠️ Ver la advertencia de modo, abajo |
| `inspect-package <pkg.zip>` | lectura | Inspección del zip QTI y sus referencias de ítem |
| `validate-package <pkg.zip>` | lectura | Validación estricta de paquete para conformidad |
| `certification import-basic-items` · `import-basic-tests` · `verify-validator` · `check-import-report` | lectura | Mapas de evidencia **QTI 3 Basic IMPORT** contra el árbol oficial de conformidad de 1EdTech, con `--trusted-report-sha256` |
| `support-matrix` | lectura | Metadatos de soporte, deprecación y *processing* |
| `a11y-proof` | lectura | 🔵 **La prueba de accesibilidad** — el comando que materializa `qti3-a11y` |
| `write-fixtures <dir>` | **escritura** | Escribe los *fixtures* canónicos |

🔵 **El mapeo a MCP es 1:1 y no necesita capa de parseo, porque cada comando ya devuelve JSON.** **Doce leen, dos
escriben a disco.** Eso es lo que sostiene el **gap 70** y lo que vuelve a **P67** cotizable.

⚠️ **La advertencia de cotización que el gap 60 no tenía:** `prepare-delivery` distingue **modo estático** (default, y
**rechaza** un archivo de estado) de **`server-materialized-adaptive`**, que **exige** un objeto de estado con `outcomes`
y, opcionalmente, `templateValues`. 🔴 **Lo adaptativo no es un flag: es un contrato de estado del lado servidor.** Es
integración, no configuración.

### 🔵 La capa de telemetría tenía una mitad sin catalogar, y es la permisiva

Esta base inventarió la telemetría por sus **servidores** (lrsql, Learning Locker, Veracity, OpenLRW). **Nunca por sus
clientes.** Del lado cliente:

- **`RusticiSoftware/TinCanPHP` — Apache-2.0, 863.777 descargas, 6.178 por mes, 88 ★, último tag 2019-03-05.**
- **`RusticiSoftware/TinCanPython` (PyPI `tincan` 1.0.0) — Apache-2.0, último upload 2020-09-03.**
- **Familia `php-xapi/*` — MIT** (`client`, `serializer`, `repository-api`, `exception`, `test-fixtures`,
  `json-test-fixtures`), último tag 2021-03-24, 825 descargas/mes en el cliente.

🔵 **Eso abarata todo lo que cuelga de P15**, porque el emisor de *statements* ya no hay que escribirlo ni elegirlo
copyleft. 🔴 **Y hay que decir la otra mitad en la misma frase: las cuatro están congeladas, la más fresca hace cinco
años.** Se proponen **forkeables**, no mantenidas, y el *fork* se presupuesta.

⚠️ **Nota de nombre, para que el próximo pase no lo pierda:** el repo se llama **TinCanPython** y el paquete se llama
**`tincan`**; en Packagist es **`rusticisoftware/tincan`**. Buscar por el nombre del repo en npm devuelve **0
resultados**.

### 🟢 Otras altas de base de este pase

| Base | URL | Licencia | Señal | Para qué sirve acá |
|---|---|---|---|---|
| **moodle-core-cli** | [gafapa/moodle-core-cli](https://github.com/gafapa/moodle-core-cli) | **MIT** ✅ | **11 versiones**, última 2026-09-24, **Moodle 4.5+** | ⚪ **Cero menciones de MCP, y por eso entra:** cliente Node.js limpio de *core web services*. **El candidato más barato a envolver** en la capa de entrada al LMS |
| **ibge-br-mcp** | [SidneyBissoli/ibge-br-mcp](https://github.com/SidneyBissoli/ibge-br-mcp) | **MIT** ✅ | **24 versiones**, 2026-01-18 → 2026-09-27 | 🔵 **La plantilla del gap 67.** Datos públicos brasileños (geografía, **censo**, economía, salud) servidos por MCP **con procedencia**. **Educación no está** — ver **P69** |

### 🔴 Gap 68 (nuevo) — la puerta oficial de Open edX no publicó nada en 70 días, y hay que cotizarla distinto

Leído del JSON de PyPI, y es la medición que los pases 30, 31 y 32 no hicieron:

| Paquete | Releases | Ventana | Silencio | Versión |
|---|---|---|---|---|
| `openedx-mcp` | 5 (0.1.1 → 0.1.5) | **2026-07-24 → 2026-07-25** | 🔴 **70 días** | **0.1.5** |
| `tutor-contrib-openedxmcp` | 7 (0.1.1 → 0.1.7) | **2026-07-24 → 2026-07-25** | 🔴 **70 días** | **0.1.7** |

🔴 **Doce releases en dos días y nada después, todavía en `0.1.x`: es la forma de un experimento publicado una vez.**
Nada de lo medido se invalida —35 rutas, 19 escritores, los cuatro rails—, pero **una propuesta que dependa de esta
puerta presupuesta mantenerla**. Dependencias declaradas del wheel: `Django>=4.2` y `djangorestframework`, sin más.

## 🧭 Las rutas de OpenCASE resueltas, la capa de federación que nadie vio, y dos nombres que se cierran — pase 30 del 2026-10-02

**Tres bases quedan mejor medidas en este pase y las tres por lectura de primera mano: dos leyendo código fuente y una
leyendo el registro de paquetes. Y entra una base nueva en la capa de evaluación.**

### OpenCASE — `1EdTech/OpenCASE` (Apache-2.0, 9 ★, 180 commits) → **gap 52 CERRADO**

✅ **La acción 1 del pase 29 se ejecutó leyendo cinco archivos de `main`, y la contradicción entre los dos documentos del
repo tiene una explicación que ninguno de los dos enuncia:**

> 🔵 **El segmento `ims/case/v1pX` aparece exactamente cuando la operación actúa sobre una entidad del estándar CASE.
> Nunca aparece en las rutas de plataforma.**

`FRAMEWORK_EDITOR_BACKEND_INTEGRATION.md` **es el documento correcto** (sus dos formas existen literales en el código);
`DEVELOPER.md` **está equivocado** para entidades CASE (`PUT /management/tenants/{id}/CFItems/{id}` **no existe**). El
error del doc se explica: **el *listado* de paquetes sí va sin prefijo** (`GET /management/tenants/{tenantId}/CFPackages`),
porque es plataforma y no estándar.

**La superficie, contada: 72 rutas.**

| Bloque | Rutas | Nota |
|---|---|---|
| Lectura CASE `v1p1` | **12** | `CFDocuments`, `CFItems`, `CFAssociations`, `CFItemAssociations`, `CFRubrics`, `CFSubjects`, `CFConcepts`, `CFAssociationGroupings`, `CFItemTypes`, `CFLicenses`, `CFPackages` |
| Lectura CASE `v1p0` | **12** | 🔵 **El juego completo también en 1.0** — las dos versiones del estándar están montadas enteras |
| Management | **44** | **20 con prefijo** (escritura CASE en ambas versiones) + **24 sin prefijo** (plataforma) |
| Descubrimiento OpenAPI 3 | **2** | 🔵 **Uno por versión**, y **sin autenticación** |
| `public` + `health` | 2 | `GET /public/tenant-lookup`, `GET /health` |

**Los tres datos que cambian la cotización de P60:**

1. 🔵 **Dos endpoints de descubrimiento, no uno.** Además del `v1p1` que el pase 29 registró, existe
   `GET /ims/case/v1p0/discovery/imscasev1p0_openapi3_v1p0.json`. Los dos se montan **antes** de los *middlewares* de
   auth: *«Service Discovery endpoints (no auth required)»*. **Se generan dos conectores sin pedir credenciales.**
2. 🔵 **La lectura es de autenticación OPCIONAL.** El código monta `makeOptionalAuthMiddleware` en `/ims/case`:
   *«frameworks marked public are readable without auth… IDs are globally unique so no tenantId is needed for read
   endpoints»*. **Un conector de sólo lectura sobre marcos públicos no necesita credenciales ni tenant** — el escalón de
   entrada más barato de toda esta KB. `/management` sí exige auth estricta.
3. 🔴 **La escritura NO es parte del estándar, y lo dice el código:** *«These operations are **NOT part of the CASE
   standard specification** and are provided as extended functionality.»* **La mitad de lectura del conector es portable a
   cualquier proveedor CASE certificado; la mitad de escritura es específica de OpenCASE.** Hay que decirlo antes de
   cotizar.

🔵 **Y la capa que nadie había registrado: CGE — CASE Global Exchange, 11 rutas de federación.** `credentials`
(GET/PUT/DELETE) + `credentials/test`, `frameworks` y `frameworks/{id}` contra el **registro global**, `subscriptions`
(POST/GET), `import`, `frameworks/{id}/refresh` y `cache/{docId}/items`. **Cambia el alcance de un proyecto de
competencias de «digitalizar el currículum» a «suscribirse y alinear», que es más barato y más defendible.**

| Lo demás, medido | |
|---|---|
| Stack | **Express 5**, TypeScript, Apache-2.0 (verificado en `package.json`) |
| 🔵 Spec | **`swagger-jsdoc` es dependencia: el OpenAPI se genera de anotaciones del código**, así que el código es la fuente autoritativa y el spec no puede atrasarse |
| Scopes | `case.read`, `case.write`, `case.admin`, `case.owner` (`requireScope`/`requireAnyScope`), anotados como `x-required-scopes` |
| Ciclo de vida | 🔵 `POST .../CFPackages/{id}/restore` — archivado y restauración, que el pase 29 no tenía |
| Cuerpo | 50 MB, coherente con importar paquetes CASE grandes |
| 🔴 Endurecimiento obligatorio | **`cors({ origin: true, credentials: true })`** con el comentario *«restrict in production»* **en el propio código** |

⚠️ **El límite honesto: no se levantó instancia.** Las 72 rutas son lectura de código de `main`, no tráfico observado, y
**el OpenAPI generado no se pidió al endpoint de descubrimiento**. Es la **acción 2 del pase 31**, y es una tarde con
`docker-compose up`. 🔴 **Canales: `raw.githubusercontent.com` responde; `codeload.github.com` devuelve 403** (no se puede
bajar el tarball) y la API de GitHub está cerrada para repos fuera del alcance de la sesión.

### Open edX — la base cambia de estado: **ya tiene puerta, y es AGPL y en proceso**

🔴 **`openedx-mcp` (AGPL-3.0, 0.1.5) + `tutor-contrib-openedxmcp` (AGPL-3.0, 0.1.7), publicados el 2026-07-25.** Para esta
vista de *foundations* lo que importa es la **decisión de arquitectura**, porque responde el **gap 50** que este archivo
dejó abierto:

> *«Pure Open edX: every operation is implemented against native openedx-platform **Python APIs**. No third-party stack.»*
> *«Installs into BOTH the LMS and the CMS process via the standard Open edX djangoapp plugin entry points, because
> course-authoring operations must run in the CMS (they touch the modulestore).»*

🔵 **La rotación de versiones `v0`–`v4` que el pase 29 midió y cotizó como «riesgo de adaptador» NO se paga por este
camino: el plugin no usa la API REST, corre adentro contra las APIs Python.** Esa es la respuesta del proyecto al problema
que esta KB documentó. ⚠️ **Y es la misma decisión que obliga al AGPL.** ✅ **La autoría queda confirmada por
implementación** (7 rutas en el CMS, incluida **`blocks/create-tree`**), lo que cierra en firme la refutación que el pase
29 hizo del pase 28. **El mapa de versiones REST del pase 29 sigue siendo válido y sigue siendo el camino de cualquier
conector permisivo *out-of-process*** — ver **P61**.

### Alta nueva de base: `instructure/qti` (**MIT**, 8 ★, 10 forks, 174 commits, Ruby)

**Entra porque cubre la pata que `examplary/qti` no cubre: el formato legado.**

| | `examplary/qti` (pase 28) | `instructure/qti` (este pase) |
|---|---|---|
| Versiones QTI | **3.0** (default) y 2.1 | 🔵 **1.2** y 2.1 |
| Dirección | Genera y parsea | ⚠️ **Sólo importa y parsea** |
| Lenguaje | TypeScript | Ruby |
| MCP | 🔴 No (control negativo) | 🔴 No — **0 menciones en el README crudo** |

**QTI 1.2 es el formato en que están los acervos viejos**, y **P48** empieza justamente por migrar un acervo viejo.
⚠️ **Pero conviene decir con precisión qué agrega, porque la tentación era sobrevenderlo: P48 YA nombraba herramienta para
esa pata** —`LongsightGroup/qti3` (**MIT**, 12 paquetes, 667 commits), que además **migra** QTI 1.2/2.x a autoría QTI 3—, así
que **`instructure/qti` no llena un hueco: es una alternativa de lectura en Ruby**. Sirve si el stack del cliente es Ruby, o
como **segundo parser para validar la migración contra el primero**, que en un acervo grande es trabajo real. ⚠️ **Límite medido:** los
tipos de interacción soportados son **True/False, Multiple Choice y Multiple Answer** — un banco con *matching*,
*ordering* o respuesta construida **no entra entero** y eso es alcance, no detalle.

### ✅ `.LRN` / dotLRN: el nombre se cierra, y **no por estar muerto**

La **acción 3 del pase 29** pedía verificar si estaba vivo y, si no, declararlo muerto. 🔴 **El pronóstico era el
equivocado: está vivo.** Pero el cierre igual corresponde, por otras dos razones:

| Qué se midió | Resultado (lectura de primera mano del árbol git) |
|---|---|
| Versión real | 🔵 **dotLRN 2.10.1**, con **`<release-date>2024-09-02</release-date>`** leído de `dotlrn.info`. ⚠️ **Y eso corrige la fuente secundaria Y el borrador de este pase, que decían «2.9.0 / 2.9.1 con soporte CSP»: el árbol va una menor por delante de lo que dice la web** |
| Antigüedad | **Dos años** desde la última release declarada. **Ni muerto ni vivo-y-activo: lento** |
| Licencia | ✅ **GPL-2.0 verificado en `license.txt`** (*«GNU GENERAL PUBLIC LICENSE Version 2, June 1991»*), **no por fuente secundaria**. 🔴 **No pasa el filtro permisivo, y eso basta para no proponerlo** |
| Núcleo | `openacs/openacs-core`, **GPL-2.0**, 50 ★, 19 forks, 7.600 commits. 🔵 **`acs-kernel.info` declara `6.0.0d2`** — una 6.0 en desarrollo, así que el núcleo está **más vivo** que el «5.10.1» que muestra el README (5.10.1 es la versión que dotLRN *requiere*, no la del núcleo) |
| Metadatos | `<maturity>2</maturity>`, *«A Course Management System»*, vendor **DotLRN Consortium** |
| VCS canónico | 🔴 **CVS** (`cvs.openacs.org`, `fisheye.openacs.org`), con el espejo en git. **Por eso ningún barrido de GitHub lo devuelve** |

🔴 **Y una corrección de este pase sobre sí mismo, que conviene dejar escrita porque el error es de método.** El primer
sondeo de este pase concluyó que el espejo `openacs/dotlrn` *«no es una fuente usable»* porque pidió `README.md` en `main`
y `master` y las dos dieron 404. **Es falso: el repo tiene contenido y se lee bien** — lo que no tiene es un `README.md`,
porque es un paquete **APM** de OpenACS y su metadato vive en **`dotlrn.info`**. `dotlrn.info` responde **200 en `main`,
`master`, `HEAD` y `oacs-5-10`.

> **Regla: «no hay README» no es «no hay repo».** Antes de declarar un espejo vacío hay que pedir **el archivo que ese
> ecosistema usa** —`dotlrn.info` / `*.info` en OpenACS, `*.gemspec`, `pom.xml`, `composer.json`— y no sólo `README.md`.
> **Es el mismo error de muestreo que esta KB viene corrigiendo desde el pase 25, ahora en el canal de verificación.**

**Cierre del nombre: `.LRN` está vivo pero lento (última release 2024-09-02), es GPL-2.0 verificado, y su desarrollo
canónico vive en CVS. No se propone —la licencia alcanza para eso— pero queda registrado con número de versión y fecha,
que es lo que evita volver a investigarlo entero en el próximo barrido.**

⚠️ **`openacs.org` devuelve 403 por el proxy** (dominio nuevo del registro de bloqueos, junto con `openedx.org`), así que
**todo lo de arriba sale del árbol git y no de su web.**

✅ **Y `CK-ERP` se declara muerto:** última release **v0.31.1 de abril de 2012**, SourceForge, conector para Drupal 7.12.
Tenía módulos educativos reales (*Teacher, Student, Applicant, Family, Registrar, Edu Administration*), y por eso conviene
anotarlo: **es el tipo de nombre que un barrido de «education ERP open source» va a devolver otra vez.**


## El lado plataforma de LTI queda cerrado, y Open edX queda como la base sin puerta — agregado en el pase 27 del 2026-10-01

**Dos cosas se cierran en este pase y las dos acotan qué se puede prometer sobre bases de terceros.**

### 1. El gap 42 cierra: no hay implementación *platform-side* de LTI 1.3 permisiva y productiva

El pase 26 lo midió sobre seis candidatas. Este pase verificó **la séptima y última, la implementación de referencia de
1EdTech** — y **no es una implementación**:

| Repo | Licencia | ★ | Forks | Commits | Qué es realmente |
|------|----------|---|-------|---------|------------------|
| [`1EdTech/ltibootcamp`](https://github.com/1EdTech/ltibootcamp) | 🚫 **ninguna declarada** | 127 | 19 | 47 | **Colección de enlaces.** El README dice que *«junta links que se relacionan con entender e implementar Tools y Platforms LTI»* |

El código Ruby de la implementación de referencia real de 1EdTech (platform **y** tool) vive **en el repositorio de
Contributing Members**, es decir **detrás de la membresía**. 🔴 **Conclusión, ahora completa sobre siete candidatas
incluida la referencia oficial: esta KB puede proponer la herramienta (*tool-side*) y no el aula (*platform-side*).**
El lado plataforma **se presupuesta como desarrollo**, y eso se puede decir con la evidencia entera sobre la mesa.
Ver el **gap 42**.

### 2. Open edX: la base de mayor huella pública, y la única sin puerta de agente

| Base | Licencia | Qué aporta | Estado de la puerta |
|---|---|---|---|
| **Open edX** (`openedx/openedx-platform`, antes `openedx/edx-platform` — **el repo se renombró y la URL vieja redirige**) | **AGPL-3.0** · 8.2k ★ · 4.4k forks · 68.764 commits | La plataforma de los programas educativos públicos grandes —**LATAM e India**—, con **Aspects** (Apache-2.0) como analítica y **Ralph sobre ClickHouse** por default | 🔴 **Ningún conector MCP** — pero el pase 28 midió la base: **la API alcanza para operación y notas, no para *authoring***. Gap 48 (contestado) · **gap 50** · P55 |

**Por qué entra en *foundations* y no sólo en *verticals*.** Lo que falta no es un plugin: es **la superficie de agente
de la base**.

✅ **La verificación pendiente se ejecutó en el pase 28, y el resultado parte el gap en dos.** Leyendo los `urls.py` del
árbol `master` de primera mano:

| Grupo de API | Rutas | ¿Escribe? |
|---|---|---|
| **Course Blocks** | `v1/blocks/`, `v1/blocks/{usage_key}`, `v1/block_metadata/{usage_key}` **y los tres en `v2/`** | Lectura |
| **Enrollment** | `enrollment`, `enrollment/{username},{course_key}`, `enrollments/`, **`unenroll/`**, `roles/`, **`enrollment_allowed/`** | ✅ **Sí** |
| **Grades v1** | `courses/`, `policy/courses/{course_id}/`, **`gradebook/{course_id}/`**, **`gradebook/{course_id}/bulk-update`**, **`subsection/{subsection_id}/`**, `submission_history/{course_id}/` | ✅ **Sí — y por lote** |
| 🔴 **Studio / CMS v1** | 21 rutas (`xblock/`, `course_settings/…`, `container/{usage_key}/children`, `course_rerun/…`, `proctored_exam_settings/…`) | 🔴 **El repo declara «the Authoring API is still experimental» y recomienda `v0`** |

**La lectura, que es la que se cotiza:** para **matrícula, roles, bloques y notas** la superficie está, está versionada
y **escribe** —`GradebookBulkUpdateView` es el equivalente *bulk* de `provide_assignment_feedback`, y el conector de
Moodle **no tiene lote**—, así que **ahí la ausencia del conector es puro gap 49**: nadie lo publicó, no que no se
pueda. Para ***authoring*** la ausencia **tiene causa técnica declarada por el proyecto**, y es el **gap 50**.
**P55 se cotiza por la mitad de operación y evaluación, y no promete autoría de curso en la misma frase.**

⚠️ **Lo que no se midió, dicho como tal:** **no se hizo ninguna llamada HTTP contra una instancia**. OAuth2, *scopes*,
*rate limits* y forma de las respuestas **siguen sin verificar** — levantar Open edX exige instalar dependencias de
terceros, que es el límite de entorno declarado desde el pase 27.

⚠️ **Nota de licencia que conviene tener presente al proponer sobre Open edX:** la plataforma es **AGPL-3.0**, pero
—igual que con Moodle y Canvas— **un conector que habla por API con token es un proceso aparte, no un derivado**. Las
puertas verificadas de las otras dos LMS son **MIT**. La vía permisiva existe; lo que no existe todavía es la pieza.

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
| Frappe Education | https://github.com/frappe/education | GPL-3.0 ⚠️ (leída en `license.txt`; **la página del repo no declara licencia**) | 657 | Python | Sí, pero del lado **administrativo y no del aprendizaje** — gestión académica (admisiones, programas, asistencia, cuotas, horarios, portal del alumno) sobre Frappe Framework. Es la app **separada** que ERPNext dejó de traer en el core a partir de v14 (`bench get-app education`). GPL-3.0 → el agente va afuera. *Agregado en el pase 23* | APAC (Frappe, India) |
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

#### 🟢 Estado de la capa, medido en el pase 35 del 2026-10-02 — lo que faltaba no era la licencia, era la fecha

Veintisiete pasadas registraron **licencia y rol** de estas cinco piezas y ninguna registró **cuándo se movieron por
última vez**, que es el dato que decide si entran en una propuesta. Medido por canal, en este pase:

| Pieza | Canal de verificación | Último movimiento | Veredicto para cotizar |
|---|---|---|---|
| **`lrsql`** | **`hub.docker.com/v2`** — `count: 112` tags | 🟢 **`v0.9.9` el 2026-10-01** (seis releases en 2026: v0.9.4 y v0.9.5 en abril, v0.9.6–v0.9.8 en agosto, v0.9.9 en octubre) | ✅ **Dependencia de producción.** Cadencia medida, no supuesta |
| **Ralph** | PyPI `ralph-malph` **5.0.1** + `CHANGELOG.md` | ⚠️ **Release 2024-07-11**, pero `[Unreleased]` grande y activo (CORS, baja de Python 3.8, correcciones de tipos Pydantic, mantenimiento de CI) | ⚠️ **Vivo en `main`, parado en el registro → se instala desde git, no desde PyPI.** No está abandonado; **no se cotiza como dependencia estable** |
| **Learning Locker** | npm `learning_locker` | 🔴 **`modified` 2022-06-19** (~4,3 años) | 🔴 **Copyleft *y* congelado.** La recomendación de no construir sobre él ya estaba; ahora tiene la razón medida |
| **`learnmcp-xapi`** | `raw.githubusercontent.com` (`LICENSE`, `README.md` 200) | Arquitectura de plugins leída; **fecha sin verificar** (**gap 63**) | ✅ Puente MCP vigente. 🔴 **No está en ningún registro**: PyPI **404**, npm **`total: 0`** |

🔵 **El canal nuevo, y conviene reusarlo:** `api.github.com` devuelve **403** en este entorno, así que estrellas y fechas
de release no son alcanzables. **Para una pieza que se distribuye como contenedor, `hub.docker.com/v2/repositories/<org>/<img>/tags`
responde 200 y devuelve `last_updated` por versión** — es el sustituto directo, y es lo que fechó `lrsql`.

🔴 **Y la advertencia de método que esta capa dejó, que es la más importante del pase 33:** el **gap 60** del pase 32
declaró que **xAPI/LRS no tiene puerta MCP**. **Es falso, y la refutación estaba en esta tabla** (fila `learnmcp-xapi`,
desde el pase 6). La lista de candidatos de ese barrido venía del **registro de paquetes**, y `learnmcp-xapi` no está en
ninguno — así que el instrumento **no podía verla**. Ver las tendencias **99** y **101**: *antes de declarar una
ausencia, `grep` sobre esta KB.*

**Por qué esta capa cambia el gap 5 y no sólo agrega repos.** El pase 5 encontró cinco servidores MCP de mastery, todos con heurística propia, y concluyó que faltaba conectar `pyKT`/`pyBKT`. Faltaba eso **y** algo anterior: los cinco también inventaron su propio almacén de eventos. Con esta capa registrada, el trabajo pendiente queda acotado a una sola pieza — **el estimador de mastery** — porque el almacén (`lrsql`, Apache-2.0) y el transporte MCP (`learnmcp-xapi`, MIT) ya existen y ya hablan entre sí. Ver el patrón **P15**.

### 🔴 Auditoría de borrado de esta capa — agregada en el pase 19 del 2026-10-01, y es el agujero del medio de la cadena de supresión

Dieciocho pasadas registraron esta capa por lo que **escribe**. Ninguna preguntó si sabe **borrar**. La respuesta
cambia el patrón **P38** y abre el **gap 33**, y empieza un nivel más arriba que los repos:

> **El estándar xAPI no contempla el borrado.** No es una omisión de las implementaciones: la especificación no
> define una operación de supresión de *statements*. Lo que define es ***voiding*** — un statement nuevo con el verbo
> `voided` que marca al anterior como obsoleto. **El dato original sigue ahí**, y eso es lo contrario de lo que pide
> el art. 17 del GDPR o el derecho de supresión de la Ley 21.719 chilena.

### 🔴 CORREGIDO EN EL PASE 21 — esta tabla estaba mal, y el error era el que más convenía comercialmente

> **Lo que sigue es la auditoría original (pases 6→20), hecha sobre la documentación publicada. El pase 21 clonó los
> tres LRS y leyó el código fuente, y dos de las tres filas se caen.** La tabla se conserva porque el error de método
> es el hallazgo: **un gap declarado sobre documentación no es un gap, es una lectura pendiente** — y esta KB lo dejó
> pendiente catorce pasadas, con la nota de límite ya escrita al pie.

| LRS | Licencia | ★ | Lo que afirmó la auditoría de documentación | **Lo que dice el código (pase 21)** |
|---|---|---|---|---|
| **SQL LRS (`lrsql`)** | **Apache-2.0** ✅ | 144 | 🚫 «No. Nada sobre *delete*, *erasure* ni retención» | 🔴 **REFUTADO.** `DELETE /admin/agents` borra **por `actor-ifi`** en cascada sobre **7 tablas** en una transacción. **Es el mejor primitivo de art. 17 de toda la capa.** ⚠️ viene **apagado**: `LRSQL_ENABLE_ADMIN_DELETE_ACTOR=false` por default en producción |
| **Ralph** | **MIT** ✅ | 51 | 🚫 «No. Nada sobre *delete*, endpoint DELETE ni GDPR/erasure» | ⚠️ **PARCIAL.** Confirmado que **no hay `@router.delete`** en la API del LRS, pero el *data backend* implementa `OperationType.DELETE` **por ID de statement** (hay que consultar primero). 🔴 **El backend ClickHouse lo declara no soportado** |
| **Learning Locker** | **GPL-3.0** ⚠️ | 585 | ✅ «Se le *atribuye* una API especial de borrado» (fuente secundaria) | ✅ **CONFIRMADO.** `POST /api/v2/batchdelete/initialise`, **por filtro**, worker paginado. ⚠️ **el código no se mueve desde el 2021-11-16** (HEAD = tag v7.1.1) aunque el repo **no está archivado** |

**Las rutas exactas, para que el próximo pase no tenga que volver a buscarlas:** `lrsql` →
`src/main/lrsql/admin/routes.clj:331` + `src/db/postgres/lrsql/postgres/sql/delete.sql:119`
(`delete-actor-and-dependents!`) + la migración `ON DELETE CASCADE` de `statement_to_actor` en `ddl.sql:443-456`.
Learning Locker → `api/src/controllers/BatchDeleteController.js` +
`worker/src/handlers/batchStatementDeletion/batchStatementDeletion.js` + `cli/src/scheduler/batchDelete.js`.
Ralph → `src/ralph/api/routers/statements.py` (sin DELETE) + `src/ralph/backends/data/clickhouse.py:128-131`
(`unsupported_operation_types`).

**Lo que sí sobrevive de la lectura original, y es lo único que hay que seguir diciéndole al cliente:**

1. **El estándar sigue sin contemplar el borrado.** xAPI / IEEE 9274.1.1 define *voiding*, no supresión. Todo lo que
   borra acá es **extensión propia de cada implementación**, no conformidad con el estándar — así que no es portable
   entre LRS y hay que escribirlo en el contrato.
2. **Ninguno notifica.** No hay evento ni webhook de borrado en ninguno de los tres. `lrsql` no devuelve ni el conteo;
   Learning Locker expone `total`/`deleteCount`/`processing`/`done` para **sondear**. El disparador LMS → LRS sigue
   sin existir, igual que el pase 19 lo encontró del lado de Moodle. **Eso es P40, y sigue siendo trabajo de
   integración.**
3. **El residuo real es la evidencia, no el dato.** `lrsql` borra bien y **no deja prueba**: el SQL está declarado
   `:result :affected` y **el conteo se descarta**; la respuesta es `200` con el `actor-ifi` que mandaste. Ése es el
   **gap 36**, y es el más chico y upstreameable de esta KB.

**Y el patrón de licencia de esta capa se da vuelta, que era el argumento de la tendencia 45.** La lectura anterior
decía: *«los dos LRS permisivos no borran y el único que borra es GPL-3.0»*. **Es al revés.** El que mejor borra es
**`lrsql`, Apache-2.0** —por actor, en cascada, transaccional— y el GPL-3.0 borra por filtro con un código congelado
desde 2021. Esta capa es, junto con la de privacidad (tendencia 39), **una de las dos de esta KB donde lo permisivo es
además lo mejor**. Lo que falla no es la licencia: es el default y la evidencia.

**La corrección alcanza a `learnmcp-xapi` (MIT), y a favor.** Sus backends declarados son `lrsql`, Ralph y Veracity.
El stack que esta KB recomienda —`learnmcp-xapi` + `lrsql`— **sí puede sacar la historia de aprendizaje del alumno**:
una llamada, un flag de entorno. Lo que hay que agregar es el expediente, no el borrado.

---

**Auditoría original (pases 6→20), conservada como registro del error de método:**

Auditado en este pase sobre la documentación publicada de cada backend:

| LRS | Licencia | ★ | ¿Documenta borrado de *statements*? |
|---|---|---|---|
| **SQL LRS (`lrsql`)** | **Apache-2.0** ✅ | 144 | 🚫 **No.** Nada sobre *delete*, *erasure* ni retención en la documentación publicada — 🔴 **REFUTADO POR CÓDIGO EN EL PASE 21, ver arriba** |
| **Ralph** | **MIT** ✅ | 51 | 🚫 **No.** Nada sobre *delete*, endpoint DELETE ni GDPR/erasure — ⚠️ **matizado en el pase 21: cierto para la API del LRS, falso para el data backend** |
| **Learning Locker** | **GPL-3.0** ⚠️ | 584 | ✅ **Sí** — es el único de la capa al que se le atribuye una **API especial de borrado** de statements |

**El patrón que se repite por tercera vez en esta KB, y ya no puede llamarse coincidencia.** La tendencia 45 lo
encontró en el LMS (lo que borra es copyleft) y la capa de *unlearning* parecía invertirlo (lo que desaprende es
permisivo). Acá vuelve a la forma del LMS: **los dos LRS permisivos no borran y el único que borra es GPL-3.0.**
🔴 **REFUTADO EN EL PASE 21 leyendo el código: es exactamente al revés.** El mejor primitivo de borrado de la capa es
`lrsql` (**Apache-2.0**), por actor y en cascada; el GPL-3.0 borra por filtro con código congelado desde 2021. Ver la
corrección arriba y la tendencia **54**.

**Y pega donde más duele, porque pega sobre una fila de la tabla principal de esta KB.** `learnmcp-xapi` (MIT) es el
único artefacto que conecta un agente con IEEE 9274.1.1, y sus backends declarados son **`lrsql`, Ralph y Veracity**
— es decir, **los permisivos, que son los que no borran**. Un tutor construido con el stack que esta KB viene
recomendando (`learnmcp-xapi` + `lrsql`) escribe la historia de aprendizaje del alumno en un almacén **del que no
hay forma estándar de sacarla**.
🔴 **CORREGIDO EN EL PASE 21.** Sigue siendo cierto que **no hay forma *estándar*** —xAPI no define supresión— pero
**sí hay forma**: `lrsql` expone `DELETE /admin/agents` por `actor-ifi`. El stack recomendado puede borrar; lo que le
falta es el flag encendido y el expediente de evidencia (**gap 36**).

⚠️ **Límite de verificación declarado — y es la nota que tenía razón y nadie ejecutó durante catorce pasadas.** El
«no» de `lrsql` y Ralph es **ausencia en la documentación publicada**, no
una prueba de que la operación sea imposible: las dos son bases de datos SQL/Elasticsearch y un `DELETE` a mano
siempre es posible. La afirmación exacta es: **ninguno de los dos ofrece borrado como operación soportada y
documentada**, y por lo tanto ninguno de los dos se puede poner en un expediente de privacidad como el componente
que cumple el art. 17. El `DELETE` a mano es trabajo a medida del cliente, no una propiedad del producto, y hay que
cotizarlo como tal. El «sí» de Learning Locker viene de fuente secundaria (Learning Pool) y **no se verificó contra
su API**: antes de citarlo en una propuesta hay que abrirlo.

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

### La vía de entrada al LMS deja de ser sólo PHP — agregado en el pase 24 del 2026-10-01

Hasta el pase 23 esta KB tenía **una sola** pieza de entrada LTI, y era PHP (`1EdTech/lti-1-3-php-library`). Eso aparecía
en **P20**, **P21** y en `verticals/solutions.md`, así que un cliente con plataforma Java/Spring recibía PHP en el diagrama
por una limitación de cobertura de esta base, no por una razón técnica. **Verificado de primera mano en este pase:**

| Repo | Licencia | ★ | Forks | Qué es | Lado |
|---|---|---|---|---|---|
| https://github.com/UOC/java-lti-1.3 | **MIT** ✅ | 21 | 14 | Librería **LTI Advantage** completa en Java, v**1.0.0**. La de más tracción de la familia | *tool* |
| https://github.com/UOC/spring-boot-lti-advantage | **MIT** ✅ | 16 | 17 | LTI Advantage para **Spring Boot**: Spring Security valida los *launches*; trae `RestTemplate` para **AGS** (Line Item, Result, Score), **NRPS** y *Deep Linking* | *tool* |
| https://github.com/UOC/java-lti-1.3-platform | ⚠️ **sin licencia declarada** | 0 | 1 | *«Library that **will** implement a full LTI Advantage platform»* — **lado LMS**. El tiempo futuro del README es el dato | *platform* |
| https://github.com/packbackbooks/lti-1-3-php-library | **Apache-2.0** ✅ | 53 | 25 | Segundo *tool provider* LTI 1.3 en PHP, **1.038 commits**. **Independiente** del de 1EdTech | *tool* |
| https://github.com/gnowledge/OpenAssessmentsClient | **Apache-2.0** ✅ | 0 | 3 | Cliente **QTI 1.x/2.x** en React. **No es QTI 3** — para QTI 3 sigue siendo `amp-up-io/qti3-item-player` | — |

**Las tres piezas Java son de la Universitat Oberta de Catalunya** (Barcelona, EMEA), que publica 14 repos LTI; los otros
que vale nombrar son `java-lti-1.3-core` (4 ★), `java-lti-1.3-jwt` (firma), `spring-boot-lti-advantage-jkws`, y para
stacks Python `django-uocLTI` e `ims_lti_py`. **Las estrellas miden poco acá** (21 y 16): es código que una universidad
pública usa en su propio campus, el mismo criterio por el que el pase 22 aceptó `tutor-contrib-aspects` con 14 ★.

🔴 **El asterisco que hay que leer antes de prometer el lado LMS.** De los 14 repos, **13 son *tool-side*** —construyen la
herramienta que entra al LMS— y **el único *platform-side* no declara licencia y dice que «implementará»**. Toda la
capacidad LTI que registró esta KB en nueve pases es del lado herramienta. **Si un engagement pide el lado plataforma
—ser el LMS, no entrar en él— esta KB no tiene con qué, y hay que decirlo en el *discovery*.**

⚠️ **Corrección de procedencia.** La hipótesis razonable era que la librería de 1EdTech fuera una donación de Packback y
que esta KB estuviera apuntando a un *fork*. **Es falso:** el README de 1EdTech dice que *«This library was initially
created by @MartinLenord from **Turnitin**»*. Son **dos** librerías PHP independientes, las dos Apache-2.0. La fila de
esta KB está bien apuntada.

### 🔴 CORREGIDO EN EL PASE 25 — el lado *platform* sí se puede construir con licencia permisiva, y la capa tiene cinco stacks, no dos

El párrafo de arriba cierra con *«si un engagement pide el lado plataforma […] esta KB no tiene con qué, y hay que decirlo
en el discovery»*. **El diagnóstico del hueco era correcto; la conclusión de que no había con qué llenarlo, no.** Se buscó
`LTI platform` explícitamente, que era la consigna que el pase 24 se dejó escrita, y aparecieron **tres** implementaciones
del lado plataforma —verificadas de primera mano el 2026-10-01—, **una de ellas MIT y con el juego completo de servicios**:

| Repo | Licencia | ★ | Forks | Stack | Lado | Qué implementa |
|---|---|---|---|---|---|---|
| https://github.com/LtiLibrary/LtiAdvantagePlatform | **MIT** ✅ | **35** | 18 | C# / **ASP.NET Core 10** + OpenIddict 7.x | 🔵 *platform* | **AGS v2** (line items, results, scores), **NRPS v2** (membresías), **Deep Linking 2.0**, launches con y sin contexto de curso |
| https://github.com/oat-sa/lib-lti1p3-core | ⚠️ **GPL-2.0** | **37** | 22 | PHP | 🔵 *platform* **y** *tool* | LTI 1.3 Core *«as platforms and / or as tools»*. **Certificada por 1EdTech: *LTI 1.3 Advantage Complete* y *LTI 1.3 Proctoring Services*** |
| https://github.com/Citolab/lti-1p3-platform-example | ⚠️ **GPL-3.0** | 0 | 0 | C# / .NET | 🔵 *platform* | Acuña y firma el `id_token`; endpoints `/lti/auth` y `/lti/jwks`; React para generar URLs de *launch*. *«the platform side end to end»* |

**La decisión deja de ser «hay o no hay» y pasa a ser una disyuntiva de licencia:** **permisivo sin sello**
(`LtiAdvantagePlatform`, MIT, .NET) **o sello con copyleft** (`oat-sa`, GPL-2.0, PHP, y es la única certificada del lado
plataforma de toda esta base). La pieza de la UOC sin licencia deja de ser la única opción y pasa a ser la peor de las tres.
⚠️ `LtiAdvantagePlatform` se describe a sí misma como *«Sample»*: **antes de prometerla hay que levantarla contra un *tool*
real** — es la acción que el pase 25 deja escrita para el 26.

#### Y el sesgo de stack era mayor del que midió el pase 24: faltaba la librería LTI con más estrellas de todas

| Repo | Licencia | ★ | Forks | Stack | Lado | Nota |
|---|---|---|---|---|---|---|
| https://github.com/Cvmcosta/ltijs | **Apache-2.0** ✅ | **373** | **86** | Node / TypeScript | *tool* | Launches, **Deep Linking, AGS, NRPS y Dynamic Registration**. **La librería LTI más traccionada que vio esta KB** |
| https://github.com/dmitry-viskov/pylti1.3 | **MIT** ✅ | **138** | 83 | Python | *tool* | `PyLTI1p3`. Adaptadores **Django** y **Flask**; 178 commits. ⚠️ **FastAPI no viene hecho** |
| https://github.com/3iPunt/wordpress-lti-1-3 | **Apache-2.0** ✅ | 6 | 3 | PHP (WordPress) | *tool* | LTI 1.3 Advantage **como plugin de WordPress**: SSO, roles y notas. 54 commits |

🔴 **El dato incómodo, sin suavizar.** Esta KB recomendó `1EdTech/lti-1-3-php-library` (Apache-2.0, **124 ★**) en **cinco
archivos** durante seis pases. **`ltijs` tiene 373 ★ —tres veces más— y la misma licencia permisiva**, y nunca apareció
porque las búsquedas entraban por *«LTI PHP»* y *«LTI Java»*, **nunca por «LTI» sin stack**. No es que la pieza
recomendada esté mal: **es que se la eligió sin ver el campo.** El campo permisivo del lado *tool*, ordenado:
**Node 373 ★ > Python 138 ★ > PHP 124 ★ > Java 21 ★**.

### El SIS copyleft que confirma el diagnóstico del pase 2 con números propios — agregado en el pase 24

| Repo | Licencia | ★ | Forks | Qué es |
|---|---|---|---|---|
| https://github.com/OS4ED/openSIS-Classic | **GPL** ⚠️ (en `docs/License.txt`) | 344 | 286 | SIS de K-12 y superior: legajo de alumno y de personal, *course manager*, horarios, **asistencia, notas, gradebook docente y transcripts** |

El pase 2 concluyó que *«todo el SIS open source es PHP y copyleft»*; el pase 23 mostró que el ERP permisivo de 12k ★
(**AureusERP**, MIT) **no tiene módulo educativo**. `openSIS-Classic` pone el número que faltaba: **es el SIS open source
más traccionado que vio esta KB y es copyleft.** El único permisivo del segmento sigue siendo **GegoK12 (MIT, 54 ★)**.
**La asimetría es de un orden de magnitud: no es un descuido de búsqueda, es la forma del mercado.**


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

## Capa de privacidad del dato del alumno — agregada en el pase 16 del 2026-10-01

Quince pasadas construyeron el agente, el modelado, la evaluación, la seguridad pedagógica, la telemetría, los
datos de entrenamiento, la accesibilidad, la credencial, el contenido curricular, la práctica, la voz y la
autoría. **Ninguna preguntó con qué derecho el sistema toca el dato real del alumno.** Se buscaron los términos
en los ocho archivos antes de abrir la capa: `COPPA` aparecía **0 veces**, `privacidad diferencial` y
`differential privacy` **0**, `federated` / `federado` **0**, `FERPA` **una sola vez** y de pasada, dentro de la
descripción de un repo de otra capa.

Es la capa que decide si las otras quince se pueden desplegar sobre datos reales, y estaba vacía.

### Bloque 1 — privacidad diferencial, y acá la noticia es buena

Todo lo maduro de esta capa es **permisivo**. Es la única capa de esta KB donde eso pasa.

| Repo | URL | Licencia | ★ | Forks | Commits | Lenguaje | Qué aporta |
|------|-----|----------|---|-------|---------|----------|------------|
| **PySyft** | https://github.com/OpenMined/PySyft | **Apache-2.0** ✅ | **10.0k** | 2.0k | **36.954** | Python | El más grande de la capa. El científico de datos **manda el cómputo** y el dueño del dato lo corre sobre datos privados: el dato nunca sale de la institución. v0.10+ reorganizado en paquetes (`syft-rds`, datasets, jobs, permisos). Comunidad OpenMined |
| **Google DP** | https://github.com/google/differential-privacy | **Apache-2.0** ✅ | **3.4k** | 436 | — | C++, Go, Java, Python | Librerías de building blocks DP más dos frameworks end-to-end (**Privacy on Beam** en Go, **PipelineDP4j** en JVM). Estadísticas ε- y (ε, δ)-diferencialmente privadas |
| **Opacus** | https://github.com/pytorch/opacus | **Apache-2.0** ✅ | **2.0k** | 398 | 814 | Python | Entrenar un modelo PyTorch con DP agregando ~2 líneas al pipeline. Contador de presupuesto de privacidad en tiempo real. ⚠️ Última actividad registrada en la página: **2024-12-18** |
| **TensorFlow Privacy** | https://github.com/tensorflow/privacy | **Apache-2.0** ✅ | **2.0k** | 477 | — | Python | El equivalente del anterior para TF: optimizadores DP y herramientas de análisis de privacidad. ⚠️ Última actividad registrada: **2024-02-14** (v0.9.0). No archivado |
| **diffprivlib** | https://github.com/IBM/differential-privacy-library | **MIT** ✅ | **920** | 208 | 595 | Python | DP de propósito general de IBM, con API estilo scikit-learn. Para prototipar y medir el impacto de DP sobre un modelo antes de comprometerse. *(Licencia leída en `LICENSE.md`: «MIT License», IBM Corporation 2018 — el sidebar de GitHub no la muestra)* |
| **OpenDP** | https://github.com/opendp/opendp | **MIT** ✅ | **437** | 78 | 990 | Rust (+ Python, R) | La implementación de referencia **académica**: colección modular de algoritmos estadísticos que se adhieren a la definición formal de DP. Copyright *President and Fellows of Harvard College*. Es el que un comité de ética universitario reconoce |

**La lectura de este bloque.** Para un cliente que necesita defender el tratamiento del dato ante un regulador,
`OpenDP` (Harvard) y `Google DP` son los dos nombres que no hay que explicar. Para meter DP en un pipeline que ya
existe, `Opacus` o `diffprivlib`. Las dos advertencias de actividad (Opacus 2024-12, TF Privacy 2024-02) **no son
abandono** —son librerías matemáticamente estables, no productos— pero conviene no venderlas como «activamente
mantenidas» sin mirar el repo el día de la propuesta.

### Bloque 2 — aprendizaje federado, y la capa se acaba de consolidar en un solo nombre

| Repo | URL | Licencia | ★ | Forks | Commits | Estado |
|------|-----|----------|---|-------|---------|--------|
| **Flower** | https://github.com/adap/flower | **Apache-2.0** ✅ | **7.2k** | 1.2k | **5.841** | **Activo, y es el ganador de la categoría.** Framework para sistemas de AI federada, agnóstico de framework ML (PyTorch, TensorFlow, scikit-learn) |
| **OpenFL** | https://github.com/securefederatedai/openfl | **Apache-2.0** ✅ | 843 | 237 | — | 🔴 **Deprecado.** El repo declara que el proyecto ya no está en desarrollo activo y que será archivado, y recomienda migrar a Flower |

🔴 **El dato de este bloque es la deprecación, y hay que leerla literal.** El repo de OpenFL (el framework
federado de Intel, antes *Open Federated Learning*) declara en su propia página:

> «The Open Federated Learning project (formerly known as OpenFL) is no longer under active development and will
> soon be archived. For existing users looking for ongoing support, we recommend the community transitions to
> **Flower** framework using the migration guide created in collaboration between our teams.»

O sea: la capa federada dejó de estar fragmentada entre tres o cuatro frameworks y **se consolidó en Flower, con
la bendición explícita del competidor que se retira**. Para una propuesta eso simplifica la decisión técnica a
una sola línea, y conviene aprovecharlo antes de que el cliente llegue con una comparativa vieja.

### Bloque 3 — generación de datos sintéticos, y acá está la trampa de licencia del pase

| Repo | URL | Licencia | ★ | Forks | Qué es |
|------|-----|----------|---|-------|--------|
| **SDV** (Synthetic Data Vault) | https://github.com/sdv-dev/SDV | 🔴 **Business Source License 1.1 — NO es open source** | **3.6k** | 423 | El más citado del espacio. **Nació en el Data to AI Lab del MIT (2016)** y hoy lo desarrolla **DataCebo, Inc.** |
| **synthcity** | https://github.com/vanderschaarlab/synthcity | **Apache-2.0** ✅ | **687** | 98 | 178 commits. Generadores **DP-GAN y PATEGAN** (privacidad diferencial incorporada), CTGAN, TVAE, flows, redes bayesianas, generadores LLM. Soporta series temporales y supervivencia. **Y trae métricas de evaluación de *correctness* y de *privacy*** |
| **ydata-synthetic / fg-data-synthetic** | https://github.com/ydataai/ydata-synthetic | **MIT** ✅ | **1.7k** | 257 | Datos tabulares y de series temporales con GANs y mezclas gaussianas sobre TensorFlow 2. ⚠️ **El paquete migró**: el README instruye desinstalar `ydata-synthetic` e instalar el paquete nuevo (`fg-data-synthetic`), con guía de migración |

🔴 **La trampa, y es exactamente la que un consultor pisa.** `SDV` es lo que cualquiera busca primero —es el
nombre canónico de datos sintéticos tabulares, tiene 3.6k ★ y salió del MIT—, y **ya no se puede usar en un
entregable facturado.** Leído en su archivo `LICENSE`:

| Campo de la BUSL 1.1 | Valor verificado |
|---|---|
| Licenciante | **DataCebo, Inc.** |
| Change Date | **cuatro años desde la fecha de cada release** |
| Change License | **MIT** (recién después de esos cuatro años) |
| Additional Use Grant | permite uso **no productivo**, modificaciones y obras derivadas |
| Restricción explícita | *«You may not use the Licensed Work… for a Synthetic Data Service»* — definido como cualquier oferta comercial que dé a terceros acceso a sus capacidades de especificación, transformación, ML o creación de datos sintéticos |
| Uso en producción | **prohibido** sin licencia comercial de DataCebo o sus revendedores |

**La BUSL no está aprobada por OSI**: es la misma familia a la que se mudaron Terraform y Vault. Y la restricción
de *Synthetic Data Service* está redactada de una forma que **pega de lleno en el modelo de negocio de un studio
de consultoría**: generar datos sintéticos para un cliente como parte de un servicio es literalmente el caso que
el párrafo excluye.

✅ **El reemplazo existe y es mejor para este caso de uso: `synthcity` (Apache-2.0).** No sólo es permisivo —trae
**DP-GAN y PATEGAN**, o sea privacidad diferencial *dentro* del generador, y métricas de privacidad y de utilidad
para demostrarla. `SDV` hay que saber nombrarlo (el cliente lo va a mencionar) y saber por qué no se usa.

### Bloque 4 — lo específico de educación, y acá se repite el patrón de esta KB

Los tres bloques anteriores son horizontales: sirven en salud, en finanzas y en educación. Buscando lo que es
**propio del dato educativo** —secuencias de interacción, knowledge tracing, analítica del aprendizaje— el techo
se desploma.

| Repo | URL | Licencia | ★ | Commits | Qué es |
|------|-----|----------|---|---------|--------|
| `Akulen/PrivGen` | https://github.com/Akulen/PrivGen | **MIT** ✅ | **3** | 15 | Código RNN de *Privacy-Preserving Synthetic Educational Data Generation*, **EC-TEL 2022**. Toma datos con columnas user / item / skill / correct, entrena, genera el dataset sintético y **evalúa con coeficientes IRT y con riesgo de reidentificación** |
| `hxwujinze/federated-deep-knowledge-tracing` | https://github.com/hxwujinze/federated-deep-knowledge-tracing | ⚠️ **sin licencia declarada** | **10** | 5 | Código del paper *Federated Deep Knowledge Tracing*. Módulos de datos, modelo, métricas |
| `TarunRaina/FedGNN-for-Personalized-Knowledge-Tracing` | https://github.com/TarunRaina/FedGNN-for-Personalized-Knowledge-Tracing | ⚠️ **sin licencia declarada** | **1** | 30 | **FedGKT**: grafos de conocimiento personales (722 conceptos × 7 features de mastery), Graph Attention Networks sobre **1.401 aristas de prerrequisitos anotadas por expertos**, y entrenamiento federado FedAvg/FedProx **sobre Flower**. Dataset Junyi Academy (25M interacciones) |
| `drsanjayagal/SynEdu-HEDL` | https://github.com/drsanjayagal/SynEdu-HEDL | ⚠️ **sin licencia declarada** | **1** | 2 | **20.000 registros sintéticos** de estudiantes, 180 cursos, 120.000+ eventos de LMS, ~300.000 registros de evaluación en 6 tablas relacionadas. Demografía, logs de interacción, desempeño y etiquetas de resultado (nota, riesgo de deserción, satisfacción) |

**El patrón, que es el mismo que la KB viene registrando en cinco capas:** lo horizontal es maduro y permisivo,
lo específico de educación es de 1 a 10 estrellas y **tres de los cuatro no tienen licencia**, así que no son
reutilizables aunque el código sirva. `PrivGen` es el único permisivo y tiene **3 ★**.

⚠️ **Dos verificaciones que esta sesión no pudo hacer, y se declaran.** El paper de `SynEdu-HEDL` está en
*Scientific Reports* (`nature.com/articles/s41598-026-44990-8`) y el trabajo de síntesis por cópulas en
`arxiv.org/abs/2604.04195`: **`nature.com` y `arxiv.org` están bloqueados por el proxy de egreso**. Los datos de
los repos salen de sus páginas de GitHub, que sí se leyeron; la metodología publicada **no** se verificó de
primera mano.

### Cómo se usa esta capa, en una línea por pieza

- **No podés mover el dato fuera de la institución** → `PySyft` (el cómputo viaja, el dato no) o `Flower` (el modelo viaja, el dato no).
- **Podés entrenar pero no podés exponer al individuo** → `Opacus` / `diffprivlib` / `OpenDP`.
- **Necesitás un dataset para desarrollar, demostrar o licitar sin tocar dato real** → `synthcity` (Apache-2.0, con DP adentro). **Nunca `SDV`.**
- **Es específicamente knowledge tracing federado** → `FedGKT` como **referencia de arquitectura**, no como dependencia: no tiene licencia.

## Capa de privacidad del dato en el LMS ya instalado — agregada en el pase 17 del 2026-10-01

El **pase 16** abrió la capa de privacidad por el lado de las **librerías** (DP, federado, datos sintéticos) y
cerró pidiendo lo que falta: *«No se revisó la capa de privacidad de los LMS ya instalados (Moodle, Open edX,
Canvas). Es el paso siguiente obvio: el dato del alumno ya está ahí, no en el agente.»* Esta capa es eso.

**Y la forma del hallazgo es la inversa de la del pase 16.** Ahí lo maduro era permisivo y lo educativo tenía
techo de 10 ★. Acá **lo educativo es lo maduro** —está desplegado en decenas de miles de instituciones, lleva
años en producción y tiene API— **y es todo copyleft fuerte.**

### Las piezas, verificadas vía WebFetch el 2026-10-01

| Repo | Licencia | Stars | Qué trae para privacidad |
|---|---|---|---|
| https://github.com/openedx/edx-platform | **AGPL-3.0** ⚠️ | 8.2k | `scripts/user_retirement` (6 scripts, verificados por nombre) + `lms/djangoapps/bulk_user_retirement` (`urls.py`, `views.py`, `tests`): API REST de retiro masivo. 4.4k forks |
| https://github.com/moodle/moodle | **GPL-3.0** ⚠️ | 7.5k | **Privacy API** en el núcleo, con la propiedad que ninguna otra plataforma de esta KB tiene: **obliga a los plugins** a declarar qué dato guardan y a saber exportarlo y borrarlo. 123.147 commits |
| https://github.com/instructure/canvas-lms | **AGPL-3.0** ⚠️ | 6.9k | «The open LMS by Instructure, Inc.» Es el código de la plataforma con ~41 % de la educación superior del continente. ⚠️ No se ubicó en abierto un toolset de retiro comparable al de Open edX — ver la advertencia |
| https://github.com/openeducat/openeducat_erp | **LGPL-3.0** ⚠️ | 881 | ERP educativo sobre Odoo. Entra por privacidad, no por ERP: **autohospedable**, la institución queda como responsable del dato y **no hay acuerdo con terceros** que complique FERPA en los bordes |

Los seis scripts de retiro de Open edX, leídos del árbol del repo: `get_learners_to_retire.py`,
`retire_one_learner.py`, `replace_usernames.py`, `retirement_archive_and_cleanup.py`,
`retirement_bulk_status_update.py`, `retirement_partner_report.py`. Según su `README`, fueron migrados del repo
`tubular` y pueden invocarse desde cualquier framework de automatización o despliegue continuo.

### Lo que el Privacy API de Moodle hace, y por qué es la pieza arquitectónicamente más interesante de la capa

Documentado por Moodle (ver la advertencia de verificación abajo): el API cubre **exportar y borrar** todo el dato
personal de un usuario por contexto, **detectar** qué usuarios tienen dato personal en un contexto dado, y borrar
el dato de todos los usuarios de un contexto. El cumplimiento **se extiende a los plugins instalados, incluidos
los de terceros**, que tienen que poder reportar qué guardan y responder a un pedido de borrado. Del lado
funcional, el núcleo trae dos herramientas: **Policies** (`tool_policy`) y **Data Privacy** (`tool_dataprivacy`),
que es la que da el flujo de pedidos de acceso y borrado, el rol de delegado de protección de datos y la
configuración de **período de retención**.

**Por qué importa para una propuesta y no es un detalle de ingeniería:** significa que en un despliegue Moodle,
**el plugin de AI que Studios entregue tiene la obligación de implementar un `privacy provider`.** No es opcional
ni es una buena práctica: es el contrato del punto de extensión. Un agente educativo entregado como plugin de
Moodle **sin** `privacy provider` es un plugin incompleto, y es exactamente lo que el **gap 27** midió del lado de
los agentes: ninguno de los 31 declara qué hace con el dato del alumno.

### 🔴 La buena noticia de licencia, y es la primera de dieciséis pasadas

Esta KB viene registrando el copyleft como la mala noticia de casi todas sus capas —accesibilidad, contenido,
analítica institucional, LMS—. **Acá no lo es, y conviene entender por qué para no descartar la capa por reflejo
de filtro de licencia.**

**No hay que forkear ni redistribuir la plataforma.** Las dos mecánicas son de extensión e invocación:

- **Moodle**: se implementa un *provider* **en el plugin propio**. Lo que se distribuye es el plugin. La pregunta
  de licencia se mueve del LMS al plugin — y ahí hay que elegir con cuidado, porque un plugin de Moodle que
  enlaza al núcleo GPL-3.0 es, en la lectura conservadora, obra derivada.
- **Open edX**: el retiro se **invoca** —seis scripts y un endpoint REST—. Invocar un programa AGPL desde una
  automatización no convierte la automatización en derivada. Lo entregable es **la configuración, el expediente y
  la operación**.

**La consecuencia comercial:** el entregable de esta capa **no es software**, o es muy poco software. Es
configuración, evidencia y procedimiento. Eso es más barato de construir y más difícil de copiar que un plugin,
y es lo que P36 empaqueta.

### ⚠️ Antes de cotizar nada de esta capa: el proveedor declara que no garantiza cumplimiento

La documentación de Open edX dice, textualmente: **«User retirement is not a compliance guarantee. The Open edX
software makes no claim of satisfying any law or regulation. It is a configurable toolset that site operators can
use to help meet the obligations apply to them specifically.»**

**Hay que leerla en el sentido correcto, porque no es una advertencia contra la herramienta: es la definición del
alcance vendible.** El cumplimiento es responsabilidad del **operador del sitio**. Configurar, evidenciar y operar
esa responsabilidad es trabajo, es facturable, y es la única parte que un cliente no puede bajar de GitHub.

🔴 **De dónde sale la cita, declarado:** `docs.openedx.org`, `docs.moodle.org` y `moodle.org` están **bloqueados
por el proxy de egreso de esta sesión**. La frase se leyó en el **snippet de búsqueda** de esa página, **no en un
fetch de primera mano**, y el `README` de `scripts/user_retirement` en GitHub —que sí se verificó— **no la
contiene**. Resolver contra la fuente oficial antes de ponerla en un documento para un cliente. Lo verificado de
primera mano es el **código**: los seis scripts y el Django app existen.

Por el mismo bloqueo, **el Privacy API, `tool_dataprivacy` y `tool_policy` se registran como documentados por
Moodle vía snippet, no verificados de primera mano.** Se intentó el árbol de `admin/tool/dataprivacy` dentro de
`moodle/moodle` por **cuatro rutas** (`main` y `master`, árbol y archivo) y **las cuatro dieron 404 vía
WebFetch**. Lo verificado de primera mano del repo es licencia, estrellas y commits.

### Lo que esta capa no tiene, y es el gap 29

**Ninguna de las piezas habla con un agente.** No hay servidor MCP, ni herramienta LTI, ni plugin publicado que
conecte un agente al Privacy API de Moodle o al retiro de Open edX, y no hay `privacy provider` de referencia
para un plugin de AI. Se buscó explícitamente. Es la **tercera capa consecutiva** con el mismo diagnóstico —la
infraestructura está, el puente al aula no— después de procedencia (pase 15) y privacidad horizontal (pase 16).

### Cómo se usa esta capa, en una línea por pieza

- **El cliente ya tiene Moodle y quiere un agente** → el plugin **tiene** que traer `privacy provider`. No es
  opcional. Es la primera línea del alcance, no la última.
- **El cliente ya tiene Open edX y necesita responder pedidos de borrado** → los seis scripts y el endpoint REST
  ya existen; lo que falta es orquestación, evidencia y política de retención.
- **El cliente tiene Canvas** → la plataforma es AGPL-3.0 y **no se verificó** un toolset de retiro equivalente.
  Tratarlo como trabajo a dimensionar, no como capacidad existente.
- **El cliente quiere residencia de dato y ser el responsable** → `openeducat_erp` autohospedado, y el argumento
  es FERPA en los bordes: sin SaaS de terceros no hay acuerdo de terceros que negociar.

## Capa de borrado del modelo (*unlearning* y procedencia) — agregada en el pase 18 del 2026-10-01

Esta capa responde a una pregunta que las diecisiete pasadas anteriores no hicieron: **cuando el alumno ejerce el
derecho al olvido, ¿qué pasa con el modelo que ya aprendió de él?** El pase 17 dejó la mitad resuelta —el Privacy
API del LMS borra el registro— y dejó escrito que *«borra el registro, no el modelo»*. Estas son las piezas que
borran el modelo.

**Son todas permisivas, y eso es la excepción en esta KB.** Leer la columna de licencia de los otros bloques de
este archivo: media KB educativa es GPL/AGPL. Acá, las seis con licencia verificada son **MIT o Apache-2.0**.

| Repo | Licencia | ★ | Para qué se usa en un engagement |
|---|---|---|---|
| https://github.com/tamlhp/awesome-machine-unlearning | **MIT** ✅ | 970 | **Punto de entrada.** Mapa de métodos, métricas y datasets. Respalda la survey *A Survey of Machine Unlearning*, ACM TIST 2025, DOI `10.1145/3749987` |
| https://github.com/locuslab/open-unlearning | **MIT** ✅ | 607 | **La base ejecutable si el modelo es un LLM.** Benchmarks TOFU/MUSE/WMDP y 12 métodos (`GradAscent`, `GradDiff`, `NPO`, `SimNPO`, `DPO`, `RMU`, `UNDIAL`, `AltPO`, `SatImp`, `WGA`, `CE-U`, `PDU`). 164 forks. arXiv 2506.12618. ⚠️ **Usar `locuslab`, no el fork `aflah02` de 0 ★** |
| https://github.com/chrisliu298/awesome-llm-unlearning | **Apache-2.0** ✅ | 627 | Recorte de LLM: 616 papers, 18 surveys, 3 frameworks |
| https://github.com/OPTML-Group/Unlearn-Saliency | **MIT** ✅ | 154 | **El método con mejor relación resultado/costo publicado.** SalUn, *weight saliency* por gradiente, clasificación y generación. ICLR 2024 **Spotlight**, arXiv 2310.12508 |
| https://github.com/Harry24k/machine-unlearning-pytorch | **MIT** ✅ | 12 | **La pieza que alcanza a un modelo de *knowledge tracing***. `torchunlearn`: interfaz unificada estilo PyTorch. NeurIPS 2025, *Unlearning-Aware Minimization*. Baja tracción: 12 ★, 51 commits — registrar como pieza técnica, no como dependencia con garantía de continuidad |
| https://github.com/cisco-ai-defense/model-provenance-kit | **Apache-2.0** ✅ | 104 | **La evidencia que el gap 30 pedía, por el lado del modelo.** Determina si dos modelos comparten origen con 8 señales (metadatos de arquitectura, estructura del tokenizer, *fingerprints* de pesos). Modos `compare` y `scan` contra ~150 modelos base de 45+ familias; streaming para +20 GB |
| https://github.com/Data-Provenance-Initiative/Data-Provenance-Collection | **Apache-2.0** ✅ | 281 | **La evidencia por el lado del dataset.** Auditoría de 44 colecciones / 1800+ datasets de finetuning con fuente, licencia y creador, y **generación de fichas de procedencia legibles** — el formato del entregable de **P37**. arXiv 2310.16787 |
| https://github.com/jjbrophy47/machine_unlearning | 🚫 **sin licencia declarada** | 965 | Segundo agregador por tamaño (117 forks): literatura de *unlearning* desde pre-2017 hasta 2025. **No muestra licencia** → a efectos de cotización se trata como sin licencia; lo que corresponde es abrir un *issue*. Usable como bibliografía, no como dependencia |
| https://github.com/hxxdtd/Awesome-Diffusion-Model-Unlearning | 🚫 **sin licencia declarada** | 67 | Recorte de difusión (3 forks): artículos, recursos y datasets de borrado de conceptos en modelos de difusión. **No muestra licencia** |

### Cómo se elige entre estas piezas, y lo decide el tipo de modelo, no el presupuesto

Esta KB tiene dos estimadores de dominio en sus fundacionales y **el *unlearning* los alcanza distinto**:

| Modelo de *mastery* | ¿Alcanzable por esta capa? | Qué se hace | Garantía que se puede prometer |
|---|---|---|---|
| **`pyBKT`** (MIT) — BKT ajustado por EM, **no es PyTorch** | 🚫 Ninguna librería de la tabla lo alcanza | **Reajustar desde cero sin el alumno.** Pocos parámetros, EM sobre la secuencia: es barato | ***Exact unlearning*** — la garantía más fuerte que existe. **Mejor resultado legal por menos trabajo** |
| **`pyKT`** (MIT) — deep knowledge tracing, **es PyTorch** | ✅ `torchunlearn` y `SalUn` son aplicables en principio | *Unlearning* aproximado sobre los pesos | **Aproximada.** El entregable **tiene que incluir la métrica de verificación**, no sólo el borrado |

**La regla operativa en una línea:** *si el modelo de dominio es BKT, el derecho al olvido se cumple reentrenando y
se puede probar; si es deep knowledge tracing, hay que hacer unlearning aproximado y el entregable incluye la
verificación.* Esa frase es la que decide el alcance de **P38**.


### Agregado en el pase 19 del 2026-10-01 — el ancla de la capa tiene 607 ★, es MIT, y el pase 18 no la vio

El pase 18 cerró esta capa con *«la oferta existe, es grande y es toda MIT/Apache»*. **La conclusión es correcta pero
la midió con los artefactos equivocados:** sus dos piezas ejecutables tienen **12 ★ cada una**, y lo que tenía
cientos de estrellas eran **bibliografías sin licencia**. El pase 19 encontró la pieza que falta — y es, con
diferencia, la más seria de la capa:

| Repo | Licencia | ★ | Qué es |
|---|---|---|---|
| **OpenUnlearning** · https://github.com/locuslab/open-unlearning | **MIT** ✅ | **607** | **El framework de referencia de *unlearning* de LLMs, y el ancla que faltaba.** De **Locus Lab (CMU)**. Implementa **3 benchmarks** (**TOFU**, **MUSE**, **WMDP**), **12+ métodos** (GradAscent, GradDiff, NPO, SimNPO, DPO, RMU, UNDIAL, AltPO, SatImp, WGA, CE-U, PDU), 5+ datasets, **10+ métricas de evaluación** y 7+ arquitecturas, con **450+ modelos preentrenados** publicados en HuggingFace |
| **MachineUnlearning** · https://github.com/OngWinKent/MachineUnlearning | **BSD-3-Clause** ✅ | 12 | 9 métodos en PyTorch (`gradient_ascent`, `bad_teacher`, `scrub`, `amnesiac`, `boundary`, `ntk`, `fisher`, `unsir`, `ssd`), cada uno referenciado a su paper. **© Universiti Malaya** → cierra región: **APAC (Malasia)**. Publicado 2025-03-27 |

**La métrica que importa para esta KB, y es la que convierte este repo en pieza vendible:** entre las 10+ métricas de
OpenUnlearning hay **ataques de inferencia de pertenencia (*membership inference*) y medidas de fuerza de
extracción**. Es decir: **no sólo desaprende, mide si el desaprendizaje aguanta un ataque.** Eso es exactamente lo
que un expediente de privacidad necesita para que la garantía «aproximada» de `pyKT` deje de ser una promesa y pase a
ser un número — y es lo que el pase 18 declaró como pendiente en su advertencia de **P38**.

**Y acota el gap 31 en vez de cerrarlo, con una distinción que hay que escribir bien:** OpenUnlearning es de
***unlearning* de LLMs** — TOFU, MUSE y WMDP miden olvido de *conocimiento textual* en un modelo de lenguaje.
**Ninguno de los tres mide un modelo de *knowledge tracing* ni de *cognitive diagnosis*.** Entonces:

- Para el **tutor LLM** (el agente que conversa): la capa está **resuelta y es MIT**, con benchmark y métricas de
  ataque. Es integración.
- Para el **modelo de mastery** (`pyKT`, `pyBKT`, los estimadores de dominio): **sigue sin haber nada específico con
  código**. Ése es el **gap 31**, y ahora está mejor delimitado: no falta *unlearning*, falta ***unlearning* evaluado
  sobre modelos del alumno**.

### 🔴 El pase 19 agrega el lado del ataque, que esta capa no tenía: la razón por la que esto no es un ejercicio

Toda esta capa se justificaba hasta acá por **obligación legal**. Este pase encontró el **riesgo técnico**, y viene
del mismo grupo que PrivacyCD:

> **P-MIA — *A Profiled-Based Membership Inference Attack on Cognitive Diagnosis Models*** (arXiv **2511.04716**).
> Primer trabajo que investiga de forma sistemática ataques de inferencia de pertenencia contra **CDMs**. Y su modelo
> de amenaza es el que hay que leer dos veces: es ***grey-box* y explota las funciones de explicabilidad de la
> plataforma**. Los vectores internos de estado de conocimiento **se exponen al usuario en visualizaciones —el paper
> nombra los gráficos de radar— y se pueden revertir con precisión a partir de esas visualizaciones**. Con eso, P-MIA
> combina probabilidades de predicción finales + vectores de estado reconstruidos, y **supera con claridad** a los
> baselines *black-box* sobre tres datasets reales contra CDMs mainstream.

**Por qué esto le pega a esta KB en particular, y no es un riesgo genérico:** el *dashboard de mastery* es algo que
esta KB **viene recomendando** —es la salida natural de `pyKT`/`pyBKT`, es lo que `Gnos` instrumenta y lo que la capa
predictiva del pase 11 muestra al docente—. P-MIA dice que **esa visualización es la superficie de ataque**: cuanto
mejor se explica el modelo al docente, más fácil es extraer de él quién estuvo en el entrenamiento. La
explicabilidad que el EU AI Act pide para los sistemas de alto riesgo **y** la minimización de datos que el GDPR pide
empujan en direcciones opuestas, y acá hay un paper que lo mide.

**Consecuencia operativa concreta, y va a P40:** un dashboard de mastery expuesto al alumno o a terceros necesita
**ruido o cuantización en el vector de estado**, o control de acceso por rol, y la decisión hay que **documentarla**.
No es una recomendación teórica: es la contramedida directa al vector que el paper describe.

⚠️ **Sin verificar de primera mano.** `arxiv.org` sigue bloqueado por el proxy en este pase, igual que en los pases
6, 7, 14, 16, 17 y 18. P-MIA y PrivacyCD se registran por **snippets concordantes**, con su número de arXiv anotado
**para que el próximo pase los abra**, no para citarlos ante un cliente. Lo que sí está verificado de primera mano es
OpenUnlearning y `MachineUnlearning` (licencia, estrellas, métodos leídos del repo).

### Lo que falta — gaps 31, 34, 35, 36 y 37 (el 32 se cerró en el pase 19, refutado; el 35 se abre en el pase 20 y está descrito en la capa de testing de conformidad, abajo)

- **Gap 31** — **SIGUE ABIERTO, y el pase 19 lo buscó con los términos que el pase 18 dejó escritos.** Se buscó
  `HIF unlearning cognitive diagnosis` y por los autores. **Autoría confirmada** (Mingliang Hou, Yinuo Wang, Teng
  Guo, Zitao Liu, Wenzhou Dou, Jiaqi Zheng, Renqiang Luo, Mi Tian, Weiqi Luo — los tres nombres que el pase 18
  anticipó están ahí) y **el algoritmo HIF también** (*hierarchical importance-guided forgetting*: explota que la
  importancia de parámetros en un CDM tiene estructura por capas, con un mecanismo de suavizado que combina
  importancia individual y de capa). **Pero no hay código publicado:** ni en los resultados de búsqueda ni en un
  repo localizable. **El gap 31 se mantiene, ahora con la búsqueda documentada.**

  **Y el pase 19 encontró a su gemelo, del mismo grupo y también sin código:** **P-MIA** (arXiv 2511.04716), el
  ataque. Los dos lados del mismo problema —cómo se extrae el dato del alumno de un CDM y cómo se lo saca— están
  publicados por el mismo entorno y **ninguno de los dos publica implementación**. Ver el bloque de P-MIA arriba.

- **Gap 33 (abierto en el pase 19) — 🔴 CERRADO POR REFUTACIÓN EN EL PASE 21.** La formulación original era:
  *«ningún LRS permisivo implementa el borrado, y el estándar tampoco lo contempla»*. **La primera mitad es falsa.**
  El pase 21 clonó los tres LRS y leyó el código: **`lrsql` (Apache-2.0) implementa `DELETE /admin/agents`**, borrado
  **por `actor-ifi`** en cascada sobre 7 tablas y en una transacción — **el mejor primitivo de art. 17 de la capa**,
  y **viene apagado** (`LRSQL_ENABLE_ADMIN_DELETE_ACTOR=false`). Ralph **no** lo expone en la API del LRS pero sí en
  su *data backend* por ID de statement (y **ClickHouse lo declara no soportado**). Learning Locker **sí** lo tiene,
  confirmado, con el código congelado desde el 2021-11-16.
  **La segunda mitad se sostiene y es lo único que queda:** **xAPI / IEEE 9274.1.1 no define supresión** —define
  *voiding*, que marca sin borrar—, así que todo borrado acá es **extensión propia, no portable entre LRS**. Lo que
  queda abierto es la **evidencia** (gap 36) y el **disparador** (P40), no la capacidad. Ver la corrección completa en
  la auditoría de borrado de este mismo archivo y la tendencia **54**.

- **Gap 39 (nuevo en el pase 25)** — **no hay banco de ítems que genere familias de variantes equivalentes, y es el
  único eslabón no medido de P49.** Que `LongsightGroup/qti3` (**MIT**, 667 commits) escriba **paquetes de banco de
  ítems** está verificado de primera mano; que su *writer* soporte **variantes paramétricas del mismo ítem con
  dificultad equivalente** —que es lo que vuelve innecesario el proctoring— **está inferido de la descripción de los
  paquetes, no probado**. Y la segunda mitad del gap es más grande que la primera: **la equivalencia psicométrica entre
  variantes no la cubre ninguna pieza open source de esta KB**. Hay *item banking* y hay entrega certificada; **no hay
  análisis de ítems** (TRI/IRT, calibración de dificultad) empaquetado y permisivo que cierre la cadena.
  **Por qué importa:** sin equivalencia medida, las notas entre variantes no son comparables, y un examen de
  consecuencia alta no puede usar el patrón. **Es acotado y construible:** escribir N variantes con el *writer*,
  entregarlas con `qti3-item-player` y calibrar con una librería IRT de Python. No es investigación: es una medición
  que nadie publicó para este stack. Ver **P49**.

- **Gap 40 (nuevo en el pase 25)** — **el cartucho MCP de CaSS está declarado y no está medido, y de él depende la
  tendencia 65.** `cassproject/CASS` (**Apache-2.0**, 62 ★, 2.123 commits) lista **MCP** entre sus *«pluggable
  cartridges»*, junto a IMS CASE, xAPI, CTDL-ASN, ASN y Open Badges 2.0. **Eso es todo lo que esta KB sabe:** no se
  levantó el servidor, **no se listó una sola herramienta**, y no se sabe si expone lectura de marcos, escritura de
  aserciones o las dos. Es la primera pieza de estándar educativo de esta base con puerta nativa de agente, así que la
  afirmación es valiosa **y es exactamente por eso que no se puede dejar sin medir**.
  **Qué hay que hacer, y es el gap más barato que esta KB abrió en cinco pases:** levantar CaSS, conectar el cartucho
  MCP y **listar las herramientas**. Si expone escritura de aserciones, el paso 5 de **P48** se cotiza como
  configuración; **si sólo expone lectura, el mapeo ítem→competencia sigue siendo desarrollo** y el patrón se encarece.
  Hasta entonces **no prometer el «sin adaptador»**: P48 funciona igual por xAPI o IMS CASE, que sí están verificados
  como cartuchos declarados de un proyecto con 2.123 commits.

- **Gap 36 (nuevo en el pase 21)** — **el borrado del LRS permisivo no deja evidencia.** `lrsql` borra de forma
  completa y atómica y **no devuelve ni registra nada**: el SQL está declarado `-- :result :affected`, así que **el
  conteo de filas afectadas se calcula y se descarta**, y el interceptor responde `{:status 200 :body params}` — el
  `actor-ifi` que mandaste. No hay registro de auditoría ni evento. Para un expediente del art. 17 o de **AB 1159**
  (operativa el 2027-07-01) la única prueba del borrado es un `200` con tu propio input adentro.
  **Es el gap más chico y más upstreameable de esta KB:** el dato ya existe en la capa SQL, falta devolverlo y
  registrarlo, sobre un repo **Apache-2.0**. No requiere investigación. Ver **P44**.

  **Reconfirmado por lectura independiente en el pase 22, y ahora con el sitio exacto del parche.** El pase 22 volvió
  a clonar `lrsql` y leyó el interceptor por su cuenta —un hallazgo que invierte el argumento de tres patrones merece
  una segunda lectura—: el sitio es **`src/main/lrsql/admin/interceptors/lrs_management.clj:23–33`**, donde
  `(adp/-delete-actor lrs params)` aparece **como expresión suelta cuyo valor de retorno se descarta** y la respuesta
  se arma como `{:status 200 :body params}`, siendo `params` el `::data` validado — **el `actor-ifi` que mandó el
  cliente**. La respuesta es un eco de la entrada, confirmado ahora por dos lecturas independientes.

  ⚠️ **Y queda una sub-pregunta sin contestar, que decide el tamaño del parche:** **¿`-delete-actor` ya devuelve los
  conteos de filas afectadas, o hay que plomearlos desde la capa SQL?** Si ya los devuelve, el parche es **una línea**
  (cambiar `:body params` por el valor de retorno); si no, hay que propagarlos por la implementación del protocolo
  (`protocol.clj:58`). **La traza de la implementación quedó bloqueada por el clasificador de seguridad del entorno en
  el pase 22** —dos denegaciones al explorar el árbol clonado de terceros—, así que **la pregunta no se contestó, y no
  se contestó por inferencia**. Es una sola lectura, y es lo primero que tiene que hacer el próximo pase sobre este gap.

- **Gap 37 (nuevo en el pase 22)** — **el registro de eventos que el stack oficial de Open edX conserva tras una
  retirada, ¿es de verdad anónimo?** Aspects borra la **PII** del alumno retirado (`UserRetirementSink` →
  `USER_RETIRE_LMS_MISC` → tablas de perfil en ClickHouse) y **conserva el dato de eventos**, con el argumento de que
  **queda anonimizado**. Pero un *statement* xAPI está indexado por un identificador de actor estable (el
  `actor-ifi`), y un registro **pseudonimizado —no anonimizado— sigue siendo dato personal bajo GDPR**. Si el
  identificador sobrevive a la retirada, la palabra «anonimizado» está haciendo un trabajo legal que puede no
  sostener, y el default de la plataforma educativa open source más desplegada del mundo **retiene el expediente
  conductual completo de alguien que ejerció el art. 17**.

  **Qué hay que leer para cerrarlo, y es acotado:** qué le pasa al `actor-ifi` / al identificador externo en las
  tablas de eventos cuando corre el `UserRetirementSink` — **si se borra, se rota, o se deja**. **Si se deja, hay un
  hallazgo regulatorio serio y upstreameable; si se rota o se borra, la postura de Aspects es defendible y esta KB
  tiene que escribirlo así en vez de insinuar lo contrario.** No es investigación: es leer un sink y un esquema de
  tablas. Junto al **gap 36**, es el gap más barato que esta KB tiene abierto. Ver **P45**.

- **Gap 34 (nuevo en el pase 19)** — ***unlearning* evaluado sobre modelos del alumno.** Formulación precisa, que es
  lo que queda del gap 32 después de medirlo: la capa de *unlearning* de LLMs está resuelta y es MIT
  (**OpenUnlearning**, 607 ★, con TOFU/MUSE/WMDP y métricas de *membership inference*), pero **ninguno de los tres
  benchmarks evalúa un modelo de *knowledge tracing* o de *cognitive diagnosis***. Para el estimador de mastery —que
  es el modelo que en educación contiene el dato sensible— no hay benchmark, no hay métrica de ataque publicada con
  código, y el único trabajo específico (PrivacyCD/HIF) no libera implementación. **Es el hueco más concreto y más
  construible que tiene esta KB:** existen las piezas (`pyKT` es PyTorch, `torchunlearn` es MIT, las métricas de
  ataque de OpenUnlearning son MIT) y falta el ensamblado y la medición. No es investigación de frontera: es un
  *harness* de evaluación que nadie publicó todavía.
- **Gap 32** — ✅ **CERRADO EN EL PASE 19, REFUTANDO LA HIPÓTESIS.** El gap decía que nada conecta el pedido de
  borrado del LMS con un *unlearning* del modelo, y el pase 18 dejó escrita la que llamó *«la hipótesis más barata
  que esta KB tiene abierta»*: que el Privacy API **emite un evento al aprobar un pedido** y que, si ese evento es
  observable, el puente es un `db/events.php` de diez líneas. **Se midió y es al revés.** Verificado sobre el árbol
  real de `moodle/moodle` (`main` = 5.3rc1):

  - `public/admin/tool/dataprivacy/db/events.php` registra **exactamente un** observer, y va **hacia adentro**:
    escucha `\core\event\user_deleted` para **crear** un pedido de borrado (`user_deleted_observer::create_delete_data_request`,
    y sólo si la config `automaticdeletionrequests` está activa). Es el sentido contrario al que hacía falta.
  - **`tool_dataprivacy` no emite ningún evento.** Ni uno. Recorridos los **187 archivos** del subárbol, **cero**
    llamadas a `trigger()`.
  - `api::update_request_status()` —por donde pasan `approve_data_request()` y el resto— es una **escritura de base
    de datos y nada más**: setea `status`, opcionalmente `dpo` y `dpocomment`, y llama a `$datarequest->update()`.
    **No hay evento, ni hook, ni notificación.**
  - *Control negativo, porque es un hallazgo en negativo:* el mismo `api.php` tiene **1.678 líneas** y
    `approve_data_request()` está en la línea **642**. El archivo y el grep eran válidos; la ausencia es real.

  **Entonces el puente no puede ser un observer, y hay exactamente dos formas de construirlo** (ver **P40**):
  **(a)** sondear la tabla `tool_dataprivacy_request` por cambio de `status` — la única superficie observable que
  existe; o **(b)** no esperar a Moodle y **dispararlo desde afuera**, que es lo que hace el único artefacto conocido
  de la categoría: **`local_gdpr_deleteuserdata`**, un plugin que expone el borrado del Privacy API **como
  web-service** (GPL-3.0, autor Dorel Manolescu). ⚠️ **Y hay que leerlo con la fecha puesta: es de 2018-07-08 y
  declara requerir Moodle 3.5**, mientras el núcleo va por 5.3. No se pudo verificar de primera mano —`moodle.org`
  sigue bloqueado por el proxy y **no se localizó repositorio en GitHub**—, así que se registra como
  **antecedente de diseño, no como dependencia**: ocho años sin actualización contra siete series mayores de Moodle.

  **El gap que queda abierto es más chico y más honesto, y es el gap 34.**


## Capa de analítica de plataforma — el stack oficial de Open edX, agregada en el pase 22 del 2026-10-01

**Por qué es fundacional y no una herramienta suelta:** esta KB venía razonando sobre el LRS como una **elección de
arquitectura** —`lrsql` para producción permisiva, Ralph para clientes Open edX (línea 111 de este archivo)—. Este
pase encontró que para Open edX **no es una elección: hay un stack oficial, y trae el LRS puesto**. Eso cambia el
supuesto de partida de cualquier propuesta sobre esa plataforma.

Verificado repo por repo vía WebFetch el 2026-10-01:

| Repo | Licencia | ★ | Forks | Commits | Rol en la pila |
|---|---|---|---|---|---|
| https://github.com/openedx/tutor-contrib-aspects | **Apache-2.0** ✅ | 14 | 32 | 2.269 | **Aspects**, el plugin de analítica y reporting **oficial** de Open edX. Orquesta vía Tutor: **ClickHouse** (almacén), **Apache Superset** (visualización), **Ralph** (el LRS), **Vector** (forwarding), **event-routing-backends** (transformación a xAPI), **dbt** (pipeline). Python |
| https://github.com/openedx/platform-plugin-aspects | **Apache-2.0** ✅ | 6 | 14 | 528 | Los *sinks* del lado LMS/Studio → ClickHouse, y los dashboards de Superset **embebidos en la interfaz del docente**. Contiene el `UserRetirementSink`. Python |

**Las estrellas acá no miden nada y no hay que cotizarlas como señal:** es el camino de analítica oficial de una
plataforma con decenas de miles de despliegues. La señal es **2.269 commits** y la organización que lo publica
(`openedx`), no las 14 estrellas.

### La condición de licencia, y es la arbitraje que esta KB busca

Open edX es **AGPL-3.0** —copyleft de red, el peor caso para SaaS, registrado en la nota de licencias de este
archivo—. **Su capa de analítica oficial es Apache-2.0.** O sea: la capa que un estudio customiza (dashboards,
métricas, modelos de datos, sinks) **es permisiva**, aunque el núcleo que la aloja no lo sea. Es la misma forma que el
pase 14 encontró en la capa curricular y el pase 20 en la de conformidad: **lo que hay que tocar es permisivo, lo
copyleft es el sustrato que no se forkea.**

### 🔴 Las dos consecuencias, y una corrige a esta KB mientras la otra la mejora

**(1) La configuración «imborrable» es el default, no una elección.** El pase 21 escribió en **P44** que *«con Ralph
sobre ClickHouse este patrón no se puede ejecutar»*, condicionado a *«si el cliente ya eligió ese backend»*. **Aspects
instala exactamente eso.** Un cliente Open edX con analítica no eligió el backend difícil de borrar: lo tiene de
fábrica. **El supuesto por default de un discovery sobre Open edX tiene que ser que el cliente ya está ahí.**

**(2) El disparador LMS → telemetría existe, y es Apache-2.0.** `platform-plugin-aspects` declara en su README,
verificado de primera mano: `UserRetirementSink` **escucha la señal Django `USER_RETIRE_LMS_MISC` y elimina la PII del
usuario de ClickHouse**. El pase 19 recorrió los 187 archivos de `tool_dataprivacy` de Moodle y encontró **cero**
`trigger()`: en Moodle ese disparador no existe. **En Open edX existe, es una señal del framework y el listener es
permisivo.** Para **P40** eso significa que el extremo del disparador pasa de *«no existe en ningún lado»* a
*«existe en una plataforma, y en la otra hay implementación de referencia para copiar»*.

### ⚠️ Pero borra PII, no el registro de eventos — y ahí está el gap 37

El sink borra las tablas de perfil (`user_profile`, `external_id`, `auth_user`), gobernadas por el flag
`ASPECTS_ENABLE_PII`. El **dato de eventos del usuario retirado se conserva**, con el argumento de que **queda
anonimizado**. La postura por default del stack oficial ante un art. 17, dicha sin eufemismo: **se borra el nombre y se
conserva la conducta.** Ver el **gap 37** más abajo y **P45**.

⚠️ **Verificación parcial declarada.** El sink, la señal y las tablas de PII están **verificados de primera mano** en
el README de `platform-plugin-aspects`. La afirmación *«el dato de eventos no se elimina porque queda anonimizado»*
viene de **snippets de búsqueda concordantes, no de lectura directa**: el ADR que la contiene vive en
`docs.openedx.org`, **bloqueado por el proxy de egreso en este pase**, y los dos caminos alternativos probados (el
`.rst` crudo y el listado del directorio de decisiones en GitHub) devolvieron 404. URL anotada para el próximo pase:
`https://docs.openedx.org/projects/openedx-aspects/en/latest/technical_documentation/decisions/0009_pii.html`.

### El dato de *due diligence* del pase, verificado de primera mano y con una fecha incómoda

**PR #1328 de `tutor-contrib-aspects`** — *«fix: make dump-data-to-clickhouse job respect `ASPECTS_ENABLE_PII`»*, autor
`ccantillo`. El *job* manual de *backfill* **sorteaba el flag de PII**: según la propia descripción del PR, un operador
podía volcar `user_profile` o `external_id` a ClickHouse en una instancia que había optado explícitamente por
`ASPECTS_ENABLE_PII=False`, *«sorteando exactamente la protección que ese setting existe para dar»*. El *check* existía
en el camino automático por señales y faltaba en el manual.

🔴 **El PR está CERRADO, no mergeado** — cerrado por su propio autor el **2026-09-16**. Consecuencia práctica: **el
agujero descrito puede seguir abierto**, y una propuesta que ofrezca `ASPECTS_ENABLE_PII=False` como control de
privacidad está ofreciendo un control con un camino documentado que lo sortea. **Verificar contra la versión del
cliente antes de escribirlo en un expediente de conformidad.**

### La precisión sobre ClickHouse que el pase 21 dejó demasiado absoluta

El pase 21 escribió que *«ClickHouse declara `DELETE` como operación no soportada»*. **La formulación correcta es más
estrecha:** ClickHouse no tiene `UPDATE`/`DELETE` de propósito general al estilo OLTP, pero **sí** tiene borrado
liviano sobre MergeTree detrás de un setting (`allow_experimental_lightweight_delete`) y mutaciones
`ALTER TABLE … DELETE`. La imposibilidad **práctica** se sostiene —no es transaccional, depende de versión, y el
backend ClickHouse de Ralph no lo expone en la API del LRS (`src/ralph/backends/data/clickhouse.py:128-131`,
registrado en el pase 21)—, pero la razón hay que decirla bien en una propuesta. ⚠️ **Dependiente de versión, no
verificado de primera mano en este pase.**

## Capa de testing de conformidad y evaluación regulatoria — agregada en el pase 20 del 2026-10-01

**Por qué es fundacional y no una herramienta suelta:** desde el pase 4 esta KB entrega *expedientes de conformidad*
(**P4**, **P10**, **P11**, **P17**, **P39**) y nunca registró el *harness* con el que se corren. Esta capa es ese
harness. Es la única capa de esta KB cuyos repos los publican **organismos de gobierno** y, con la capa de privacidad
del pase 16, la segunda en la que **lo maduro es permisivo**.

Verificado repo por repo vía WebFetch el 2026-10-01:

| Repo | Licencia | ★ | Forks | Rol en la pila |
|---|---|---|---|---|
| https://github.com/UKGovernmentBEIS/inspect_ai | **MIT** ✅ | 2.900 | 763 | **La base.** Framework de evals del **UK AI Security Institute**, 200+ evals pre-construidas, *model-graded evals*, diálogo multi-turno, uso de herramientas. Es el sustrato sobre el que COMPL-AI se construye |
| https://github.com/aiverify-foundation/moonshot | **Apache-2.0** ✅ | 353 | 70 | **El ejecutor.** *Benchmarking* + *red-teaming* de la AI Verify Foundation (Singapur), 2.153 commits, Python, v0.7.6 beta. Implementa el Starter Kit de IMDA como *cookbooks* |
| https://github.com/compl-ai/compl-ai | **Apache-2.0** ✅ | 211 | 37 | **El mapeo regulatorio.** 29 benchmarks organizados sobre **6 principios núcleo del EU AI Act**. ETH Zürich + INSAIT + LatticeFlow AI, 333 commits |
| https://github.com/aiverify-foundation/aiverify | **Apache-2.0** ✅ | 97 | 31 | Plataforma de *governance testing*, v2.0 modular, 3.035 commits. ⚠️ **Alcance: modelos supervisados tabulares y de imagen, no agentes LLM** |
| https://github.com/aiverify-foundation/moonshot-data | **Apache-2.0** ✅ | 45 | 41 | **El almacén de assets, y el punto de extensión de datos:** conectores (OpenAI, Anthropic, Together, HuggingFace), datasets (BigBench, CyberSecEval, **Medical LLM**, **AILuminate v1.0 DEMO** / MLCommons), métricas, *attack modules*, *cookbooks* |
| https://github.com/aiverify-foundation/moonshot-cicd | **Apache-2.0** ✅ | 14 | 4 | **La versión que se opera, no la que se demuestra:** corre en CI/CD con Docker y S3. Cuatro categorías de riesgo: alucinación, contenido indeseable, divulgación de datos, vulnerabilidad adversaria. Python 3.12 |
| https://github.com/aiverify-foundation/moonshot-ui | **Apache-2.0** ✅ | 12 | 7 | Informe **HTML con gráficos interactivos** + export JSON. Es la salida legible por un comité de ética o una inspección |
| https://github.com/aiverify-foundation/aiverify-developer-tools | **Apache-2.0** ✅ | 9 | 6 | **El punto de extensión de código:** plantillas para plugins de test y algoritmos propios (v2.x) |
| https://github.com/morganrcu/awesome-eu-ai-act | **CC0** ✅ | 21 | — | Lista curada de conformidad al AI Act. Útil como mapa: nombra Giskard (5.700 ★), DeepEval, PyRIT, Holistic AI (Apache-2.0), AI Act Companion (MIT), Regula (Apache-2.0 / EUPL-1.2), VerifyWise, AIR Blackbox, Venturalitica SDK, Inkog |

### 🔴 El hallazgo de esta capa es una ausencia, y está declarada por los propios catálogos

**No se deduce de una búsqueda: los tres catálogos declaran su cobertura y educación no está en ninguno.**
`LLM-Evals-Catalogue` (AI Verify Foundation, 23 ★, ⚠️ sin licencia declarada) tiene una categoría *domain-specific*
con **derecho, medicina y finanzas**; `compl-ai` mapea 29 benchmarks al AI Act **sin mención de educación** —aunque el
Anexo III nombra la educación de forma textual—; y `awesome-eu-ai-act` lista once herramientas open source y
**ninguna educativa**.

**Y la pieza complementaria ya está en esta KB desde el pase 4:** `EduBench` (**MIT**), `SafeTutors` (**MIT**),
`MathTutorBench` (CC BY 4.0), `UnifyingAITutorEvaluation` (CC BY-SA 4.0). **Lo que no existe es el puente.** Es el
**gap 35**, y las licencias de las dos puntas (MIT ↔ Apache-2.0) lo hacen el gap más barato de cerrar que tiene esta
KB. Ver **P42**.

### La condición de licencia, y por una vez no hay trampa

Es la capa más limpia de esta KB junto con la del pase 13 (Jupyter). **Ocho de los nueve repos son MIT, Apache-2.0 o
CC0.** La única excepción es `LLM-Evals-Catalogue`, **sin licencia declarada** — y es documentación, no código: se
puede **leer** para orientarse y **no** se puede incorporar a un entregable. Que la pieza sin licencia sea justamente
el catálogo donde falta educación es irónico pero inofensivo: lo que hay que hacer ahí es **contribuir hacia arriba**,
no copiar hacia abajo.

### El *unlearning* educativo con código, que el gap 34 venía pidiendo a medias

| Repo | Licencia | ★ | Commits | Qué es |
|---|---|---|---|---|
| https://github.com/GEMLab-HKU/Unlearn_and_Relearn | **MIT** ✅ | 4 | 22 | GEMLab, **Universidad de Hong Kong** (Jiajia Song, Zhihan Guo, Jionghao Lin). Tres etapas: *unlearning* por destilación con intervención → *relearning* (fine-tuning o enseñanza interactiva guiada por LLM) → loop **Coach / Teachable Agent / Judge**. Olvido progresivo 10–50%. Python. Paper: Springer `10.1007/978-3-032-29744-0_42`, preprint arXiv 2603.26142 |

**Lee bien para qué sirve:** aplica *unlearning* **con fin pedagógico** —fabricar un alumno novato creíble para
*learning-by-teaching*— y **no** con fin de privacidad. El **gap 34 no se cierra**; lo que cambia es que la maquinaria
difícil (borrar un concepto de un modelo de alumno y medir que se borró) **ya existe en un contexto educativo, con
licencia MIT**, y lo que falta es apuntarla al objetivo de supresión. ⚠️ 4 ★ y 0 forks: **arquitectura de referencia,
no dependencia**.

### Lo que falta en esta capa — el gap 35

- **Gap 35 (nuevo en el pase 20)** — **ningún benchmark pedagógico está empaquetado como prueba de conformidad, y
  ninguna herramienta de conformidad tiene cobertura educativa.** Las dos mitades existen, están maduras y son
  permisivas, y **nadie las unió**: no hay *recipe* ni *cookbook* de Moonshot para educación, no hay plugin educativo
  en `aiverify-developer-tools`, no hay benchmark educativo en `compl-ai`, y `EduBench` / `SafeTutors` / `MathTutorBench`
  no declaran mapeo a ningún requisito regulatorio. **No es investigación: es empaquetado.** Y a diferencia de los
  gaps 31 y 34 —que esperan que alguien publique código— éste se cierra **con trabajo de integración sobre repos que
  ya están en esta tabla**. Es el gap más construible y el de mayor valor comercial de esta KB, porque el expediente
  que habilita es el que la KB ya vende en cinco patrones.

⚠️ **Nivel de evidencia de este pase.** Los nueve repos de la tabla y el de GEMLab se verificaron **de primera mano**
(licencia, estrellas, forks, commits, alcance declarado). Lo **regulatorio y lo de plataforma estatal** viene de
**fuentes secundarias concordantes**: `moe.gov.sg`, `learning.moe.edu.sg`, `imda.gov.sg` y `arxiv.org` están
bloqueados por el proxy de egreso de esta sesión. Las fechas del marco de agentes de Singapur (22-ene-2026,
actualizaciones del 20-may y 5-jun-2026, v1.5) y los crosswalks (NIST oct-2023, ISO/IEC 42001 jun-2024) se sostienen
en múltiples fuentes independientes, **no** en la lectura de la fuente primaria.


⚠️ **Nivel de evidencia:** los repos de la tabla se verificaron de primera mano (licencia, estrellas, forks, fork
sí/no). Los metadatos de los papers vienen de **snippets concordantes**: `arxiv.org` está bloqueado por el proxy de
egreso de esta sesión, igual que `blogs.cisco.com` y `helpnetsecurity.com`.


## Capa de evaluación: autoría, banco de ítems y entrega certificada — agregada en el pase 25 del 2026-10-01

**Dos piezas MIT que no compiten: una está certificada y sólo entrega; la otra crea, banca y migra y no está
certificada.** Verificadas de primera mano el 2026-10-01.

| Repo | Licencia | ★ | Forks | Lenguaje | Qué hace | Certificación 1EdTech |
|---|---|---|---|---|---|---|
| https://github.com/amp-up-io/qti3-item-player | **MIT** ✅ | **30** | 6 | JavaScript | **Sólo entrega/render** de ítems QTI 3. Sin autoría ni banco | ✅ **QTI 3 Basic *y* Advanced «Delivery»** |
| https://github.com/LongsightGroup/qti3 | **MIT** ✅ | 5 | 2 | TypeScript | **12 paquetes, 667 commits.** Parseo con validación tipada, *player* como web component nativo, *scoring* y *response processing*, serialización y restauración de estado, **autoría XML y *writer* de paquete de banco de ítems**, **migración de QTI 1.2 y QTI 2.x a ítems de autoría QTI 3**, transcodificación por perfil | 🚫 *«The project is not certified»*, dicho por su propio README |

🔵 **La regla de propuesta que sale de acá, y es la que importa:** el sello de 1EdTech que el cliente audita cubre **la
entrega**. Entonces el *item bank* y la autoría pueden ir con la pieza no certificada **siempre que la entrega al
candidato la haga la certificada** — y eso hay que escribirlo en la propuesta, no dejarlo implícito. Ver **P48**.

⚠️ **El límite medido, y cierra la consigna del pase 24:** **no existe banco de ítems QTI 3 certificado en open source.**
Se buscó explícitamente. Los bancos QTI históricos (`tremby/questionbank`, `tremby/eqiat`) están **archivados**.

## Capa de horarios (*timetabling*) — agregada en el pase 25 del 2026-10-01

**La capa estaba vacía en esta KB, y el permisivo grande resultó ser el más traccionado del dominio.**

| Repo | Licencia | ★ | Forks | Lenguaje | Alcance | Región |
|---|---|---|---|---|---|---|
| https://github.com/UniTime/unitime | **Apache-2.0** ✅ | **349** | **213** | Java | **Horarios de cursos y de exámenes**, *event management* con salas compartidas, **asignación de alumnos a clases**, *scheduling* de docentes. **Distribuido:** varios gestores departamentales coordinan un mismo horario | North America ⚠️ *inferida* |
| https://github.com/manceras/horarios-escolares-manager | **MIT** ✅ | 0 | 0 | Python (FastAPI) + React/TS | Primaria: docentes, grupos, aulas y carga semanal con **OR-Tools CP-SAT**. Instalador Windows + AppImage, 42 commits. ⚠️ **«Early foundation, not production-ready»** por sus propios autores; UI **sólo en español** | EMEA (España) |

⚠️ **La forma del segmento repite la del SIS que midió el pase 24:** los dos nombres históricos del *timetabling*
escolar —**FET** y **mFET**— son **GPL/AGPL**. El permisivo grande y productivo es **UniTime**; el permisivo chico es
español y está declarado no-productivo. Para un cliente de educación superior, **UniTime es la respuesta y es Apache-2.0**.

## Capa de aserción de competencias — agregada en el pase 25 del 2026-10-01, y es la que le faltaba a la capa CASE

| Repo | Licencia | ★ | Forks | Lenguaje | Qué hace | Estándares |
|---|---|---|---|---|---|---|
| https://github.com/cassproject/CASS | **Apache-2.0** ✅ | **62** | **29** | JavaScript | *«Competency and Skills System»*: autoría de marcos, **registro de aserciones de logro individual** y **cómputo de perfiles del aprendiz**. 2.123 commits. Editor Vue.js con *crosswalks* e import/export | **IMS CASE**, **xAPI**, CTDL-ASN, ASN, **Open Badges 2.0** y 🔵 **MCP**, por *«pluggable cartridges»* |

🔴 **Lo que corrige de la lectura de esta KB.** La capa CASE que el pase 20 levantó —`opensalt` (MIT, 45 ★),
`1EdTech/OpenCASE` (Apache-2.0, 9 ★), `compeito` (Apache-2.0, 3 ★), `conform-ed` (MIT, 2 ★)— **sabe hospedar y validar
marcos de competencias, y ninguna de sus cuatro piezas sabe decir si un alumno alcanzó una competencia.** CaSS es la
pieza de aserción, es permisiva, y con **62 ★ es la más traccionada de toda la capa**. Y el **cartucho MCP** la vuelve
la **primera pieza de estándar educativo de esta KB con puerta nativa de agente**. Ver **P48** y la tendencia **65**.

## Capa de analítica de aprendizaje: la decisión de estándar, con fecha — agregada en el pase 25 del 2026-10-01

🔴 **De los dos estándares de analítica de aprendizaje, sólo uno se puede construir en open source.** Esto no es
preferencia técnica: es una decisión del consorcio con fecha, y se midió este pase.

| | **xAPI** (ADL / IEEE) | **Caliper Analytics** (1EdTech) |
|---|---|---|
| Especificación | https://github.com/adlnet/xapi-profiles — **Apache-2.0** ✅, **60 ★**, 33 forks, 153 commits, **no archivado** | https://github.com/1EdTech/caliper-spec — **22 ★**, bajo *«IMS Global Learning Consortium Specification Document License»* ⚠️ **no es licencia OSI** |
| Implementaciones de referencia | **Públicas y permisivas:** `yetanalytics/lrsql` (ya en esta KB) y **`yetanalytics/xapipe`** / *LRSPipe* — **Apache-2.0** ✅, 17 ★, 9 forks, Clojure | 🔴 **Privadas desde el 2023-06-17.** `caliper-java`, `caliper-js` y `caliper-python` dan **404**; la descripción del repo `1EdTech/caliper-java` **es el aviso**: *«1EdTech will be moving Caliper to private repositories on June 17, 2023»*. Acceso sólo para *Contributing Members* y *Affiliates* |
| Lo que queda público | — | `caliper-js-example` (**LGPL-3.0** ⚠️, 8 ★, ©2018) y `caliper-ontology`, **archivado** (estado del 2019-04-18) |
| Estado normativo | **Grupo de trabajo IEEE p9274.2.1 activo** tras xAPI 2.0 | Especificación viva (Caliper 1.2) con implementaciones cerradas |

**`yetanalytics/xapipe` (LRSPipe) es la pieza nueva y es la que faltaba en el medio:** *forwarder* y middleware de
sentencias xAPI **gobernado por xAPI Profiles**, con **filtrado por *statement template*** y **por *pattern***, o reenvío
total. Es decir: **decide qué telemetría sale de dónde según el perfil**, que es exactamente el control que piden los
patrones de supresión y minimización de esta KB (P40, P44, P45, P46, P47).

🔵 **La regla que esta KB adopta desde el pase 25:** **para analítica de aprendizaje se propone xAPI, no Caliper**, y
cuando un cliente pida Caliper —porque su LMS lo emite— se le dice que **la especificación es legible pero las
implementaciones no son open source desde junio de 2023**, y se cotiza el adaptador. Ver la tendencia **63**.

---
*Ver también: `verticals/solutions.md` para plataformas verticales completas y `compose/patterns.md` para el wiring concreto.*

## 📚 La capa de biblioteca — ILS/OPAC, agregada en el pase 26 del 2026-10-01

Veinticinco pasadas inventariaron el LMS, el LRS, el SIS, la evaluación, los horarios, las competencias y las
credenciales. **Ninguna buscó la biblioteca** — y es, en una universidad, uno de los dos o tres sistemas con más datos
sobre qué está estudiando realmente cada alumno. Era parte de la consigna explícita del pase 26 (*«los artefactos
`admissions`, `library`/OPAC ni `alumni`/student success: quedan como consigna del pase 26»*).

**El hallazgo es que esta capa, al contrario de casi todas las demás de esta KB, tiene una opción permisiva y grande.**

| Repo | Licencia | ★ | Forks | Commits | Lenguaje | Qué es |
|------|----------|---|-------|---------|----------|--------|
| https://github.com/folio-org/platform-complete | **Apache-2.0** ✅ | 15 | 27 | **3.096** | JavaScript | **El ensamblado de la plataforma FOLIO.** *«Complete set of Stripes modules for FOLIO»* — el `package.json` + `stripes.config.js` + `yarn.lock` que fija **el conjunto compatible de releases** y la infra Docker. Es el punto de entrada canónico, no un módulo |
| https://github.com/folio-org/mod-inventory | **Apache-2.0** ✅ | 4 | 15 | **2.402** | Java | El módulo de **inventario**: *instances*, *holdings*, *items*. Import por **Kafka**, *authority record linking*, procesamiento **MARC** bibliográfico y operaciones batch. API HTTP **multi-tenant** |
| Koha | ⚠️ **GPL-3.0+** | — | — | — | Perl | **El ILS open source más adoptado**, el primero de la categoría. OPAC, circulación, catalogación, adquisiciones, publicaciones periódicas, reservas, gestión de socios. Estándares web (XHTML/CSS/JS) |

**Cómo leer esta capa en un *engagement*, en una línea.** Si el cliente **ya tiene Koha** —y es el caso más probable,
porque es el más instalado— la capa AI se construye **contra su interfaz**, y hay que leer la **GPL-3.0** antes de
tocar el core. Si el cliente está **eligiendo** o migrando, **FOLIO es Apache-2.0** y además está diseñado como
**plataforma modular multi-tenant con bus de eventos Kafka**, que es exactamente la forma que un agente necesita para
engancharse sin parchear el core. **FOLIO es, en esta KB, el caso raro: la pieza grande, institucional y permisiva.**

⚠️ **La advertencia de lectura, porque las estrellas acá engañan y mucho.** `platform-complete` tiene **15 ★** y
`mod-inventory` **4 ★**. Con el criterio de estrellas que esta KB usa para agentes, se descartarían. **Sería un error:
3.096 y 2.402 commits, 27 y 15 forks, y un consorcio de bibliotecas universitarias detrás.** FOLIO es un proyecto de
consorcio, y los consorcios no acumulan estrellas de GitHub: acumulan **implantaciones**. Es el mismo patrón que esta KB
ya registró en Apereo y en `UniTime` — **para infraestructura institucional, los commits y los forks miden vida; las
estrellas miden moda.** Regla que conviene fijar: *no aplicar el umbral de estrellas a software de consorcio*.

🔴 **Lo que NO hay en esta capa, declarado:** **ningún conector MCP ni pieza agéntica** para biblioteca. Ni para FOLIO
ni para Koha. La búsqueda del eje conector no devolvió nada, y FOLIO —que tiene el bus de Kafka servido— es el candidato
más obvio de esta KB para construirlo. Ver el **gap 45** y el patrón **P52**.

## 🧾 Admisiones y *student success* — las dos capas que se buscaron y salieron vacías de permisivo (pase 26)

Las otras dos consignas del pase 26. **Se buscaron y se declara el resultado, que es un gap informado, no un hallazgo.**

**Admisiones / matrícula.** Lo que existe es copyleft o es un trabajo de estudiante:

| Pieza | Licencia | Lectura |
|------|----------|---------|
| `OS4ED/openSIS-Classic` | ⚠️ **GPL** | SIS de K-12/superior con el pipeline de admisión adentro. **Ya estaba en esta KB.** Copyleft |
| **OpenEduCat** | ⚠️ **LGPL-3.0** | Pipeline completo de admisiones (consulta → solicitud → verificación de documentos → entrevista → carta de oferta → alta en el SIS), self-hosted, sin fee por postulante. **Ya estaba.** Copyleft |
| https://github.com/CollinsTatang/admissionSystem | **MIT** | **MIT, sí — y tiene 4 commits, 6 ★ y 0 forks.** PHP/MySQL. Verificado de primera mano: *«allows the user to create an account and applied for admission»*. **No es base de producción, y el conteo de commits lo dice solo** |

🔴 **Conclusión: no hay plataforma de admisiones permisiva y productiva.** Las dos que sirven son **GPL y LGPL**, y lo
único permisivo verificado tiene **4 commits**.

⚠️ **Y un no-hallazgo que se declara en vez de arrastrarse:** el barrido devolvió también
`WalaEddine01/OrgSchool-portfolio-project` presentado como *«Open Source Software about student Management System»*.
**Verificado: 404.** No existe en esa ruta, así que **no se registra como hallazgo** — un 404 no es un repo, y esta KB
ya tiene registrada la regla de que *un 404 dice «no está donde preguntaste»*: si el proyecto existe con otro nombre,
hay que encontrarlo antes de citarlo. **Para un engagement de admisiones, el camino es LGPL-3.0 sobre OpenEduCat** —que
para un módulo Odoo es manejable, porque la LGPL permite el módulo propietario al lado— **o desarrollo.** Ver el **gap 46**.

***Student success* / alumni.** Peor, y con un dato de antigüedad que importa:

- **FlightPath Academics** — plataforma open source de **asesoría académica, *degree audit* y *student success*** con
  *early alerts* y *Academic Priority* para detectar alumnos en riesgo. **PHP, GPLv3+**, originada en la University of
  Louisiana at Monroe, liberada el **2013-03-13**. 🔴 **No se encontró repositorio en GitHub** — el 404 de
  `Cerebro-Tech/FlightPath` es de WebFetch. Se distribuye desde su propio sitio.
- **Student Success Plan (SSP)** — modelo de *coaching* e intervención con *case management* y *early alert*, open
  source, sostenido por **Unicon**. Las referencias verificables son de **2013–2014** (St. Petersburg College,
  Educause NGLC). **Sin señal de vida reciente.**
- **Marist College early alert dashboard** — open source, del Open Academic Analytics Initiative. **Misma época.**

🔴 **Conclusión: la capa de *student success* open source es de 2013–2014, es GPL, y no vive en GitHub.** Es la capa
**más vieja y peor abastecida** de todas las que inventarió esta KB en veintiséis pasadas — y es, simultáneamente, la
que el **Annex III** del EU AI Act y las prohibiciones de **Oklahoma y Maryland** ponen bajo más presión regulatoria,
porque *predecir qué alumno va a fracasar* es exactamente la decisión automatizada sobre el alumno que esas normas
acotan. **Hueco de mercado real y riesgo regulatorio alto en la misma celda.** Ver el **gap 47** y la tendencia **68**.

## 🔌 Conectores de LMS y el cierre del lado *platform* — pase 26

Detalle completo, tabla de los seis candidatos LTI y la medición de `ltijs` en `agents/top.md` (capa conector).
Resumen para esta vista:

| Repo | Licencia | ★ | Commits | Lado | Lectura |
|------|----------|---|---------|------|---------|
| https://github.com/vishalsachdev/canvas-mcp | **MIT** ✅ | 269 | 815 | *tool* | **Hasta 102–103 tools** + 8 skills. Alumno **y docente**. Entra en la tabla principal de `agents/top.md` |
| https://github.com/macewan-cs/lti | **MIT** ✅ | 8 | 89 | *tool* | Go. *«partially implements»*. **Verificado: es tool-side**, no el lado LMS |
| https://github.com/csmediapro/moodle-mcp-server | 🔴 **AGPL-3.0** | 0 | 57 | *tool* | **Open-core:** 10 tools de lectura abiertos, *Reporting*/*Analytics*/*Directory*/*Compliance* **premium aparte** |

**Y el dato medido sobre `ltijs` (Apache-2.0, 5.9.9), que cambia cómo se lee toda la capa LTI de esta KB:** instalado
desde npm, sus exports de primer nivel son **`[ 'Provider' ]`** — uno solo, sin clase de *platform*; y su `package.json`
se describe como *«turn your web application into a LTI 1.3 **Learning Tool**»*. **Es tool-side y nada más, medido, no
leído.** Con los seis candidatos verificados, el **gap 42** queda: **no existe implementación *platform-side* de LTI 1.3
permisiva y productiva.**

## 🧭 El mapa de versiones de la API de Studio, y la base de estándares que faltaba — pase 29 del 2026-10-01

**Dos bases quedan mejor medidas en este pase, y en las dos la medición se hizo leyendo el código o los docs del repo,
sin instancia.**

### Open edX — `openedx/openedx-platform` (AGPL-3.0, 8.2k ★, 4.4k forks, 68.764 commits)

🔴 **Corrección del pase 28, que es de esta KB sobre sí misma.** El pase 28 escribió que *«la API de *authoring* de
Studio está declarada experimental por el propio proyecto»* y de ahí concluyó que la ausencia de conector tenía **causa
técnica**. **La cita era correcta; la conclusión no.** El aviso está en `v1/urls.py`, **fechado «(Nov. 23)»**, y
**encabeza una sección vacía**. El archivo de al lado, `v0/views/xblock.py`, declara que **`v0` es el deprecado** y
manda a `/api/contentstore/v1/xblock/`. **`v1` registra ese `XblockViewSet`** y le implementa **CRUD completo**.

**El mapa completo, por versión, leído de los cinco `urls.py`:**

| Versión | Qué monta | Para qué sirve a un conector |
|---|---|---|
| **`v0`** | La *Authoring API* real: `file_assets` (CRUD), `videos/uploads`+`images`+`encodings`+`features`, `video_transcripts`, `youtube_transcripts/check`+`/upload`, `grading/`, `advanced_settings`, `tabs` (list/settings/reorder), *Course Optimizer* (`link_check`, `rerun_link_update`), `xblock/` ⚠️ deprecado | **Assets, video y transcripciones viven sólo acá**: no hay equivalente en `v1`. Un conector **tiene** que usar `v0` para eso |
| **`v1`** | 🔵 **`XblockViewSet`** (`create`/`retrieve`/`update`/`partial_update`/`destroy`, ADRs FC-0118, **`?view=minimal`**), `course_settings`, `course_details`, `course_index`, `course_team`, `course_grading`, `course_rerun`, `certificates`, `group_configurations`, `container_handler`, `container/{usage_key}/children`, `textbooks`, `proctored_exam_settings`, `proctoring_errors`, `course_waffle_flags`, `home`, `home/libraries` | **El destino de la autoría de bloques.** Es donde hay que pegar para crear y editar contenido |
| **`v2`** | `downstreams` (`DownstreamList`, `Downstream`, `DownstreamSummary`, **`SyncFromUpstream`**), `NumericalInputValidation`, `HomePageCoursesViewV2` | 🔵 **Reutilización de contenido de biblioteca**: corregir una vez y propagar a todos los cursos que heredan |
| **`v3`** | ViewSets de `home`, `course_details`, **`authoring_grading`** | Tercer domicilio de las notas |
| **`v4`** | `home/courses` (`HomeCoursesViewSet`, ADR 0028) | El listado más nuevo |

🔴 **La consecuencia operativa, y es la que se escribe en la propuesta:** **las notas viven en `v0` (`grading/`), `v1`
(`course_grading/`) y `v3` (`authoring_grading`) al mismo tiempo**, y **assets/video/transcripciones sólo en `v0`**.
**Un conector necesita un adaptador de versión por capacidad**, no una base URL. Eso es alcance cotizable y declarado,
no un imprevisto.

⚠️ **Autenticación, leída del ADR 0034:** `JwtAuthentication` + `SessionAuthenticationAllowInactiveUser` — elegido a
propósito para que un autor con sesión en verificación siga operando. **No se verificó contra una instancia**: no hay
instancia en este entorno.

### CASE — `1EdTech/OpenCASE` (Apache-2.0, 9 ★, 3 forks, 180 commits) — **alta nueva**

**La base de estándares que esta KB declaró inexistente durante cuatro pases.** No es de un tercero: es del **propio
1EdTech**, y se describe como implementación de referencia *«transparent, standards-aligned, and ready to be embedded,
extended, or deployed as-is»*.

| Componente | Qué es | Dato que importa |
|---|---|---|
| **Publishing Server** | **CASE Provider API oficial**, CASE **1.0 y 1.1**, recursos `documents`/`items`/`associations`/`rubrics`/`packages`, *field filtering*, paginación, ordenamiento y filtrado por metadatos **según la especificación**, más endpoints de descubrimiento | *«fully compatible with the 1EdTech certification requirements»* |
| **Visual Editor** | Canvas de autoría de marcos: nodos y asociaciones (*is child of*, *is related to*, *precedes*), *layout* automático, publicación directa al servidor | Es la pieza de **autoría de competencias** que `cassproject/CASS` tiene **cerrada a MCP** (0 expuestas / 13 ocultas) |
| **Identidad** | **Keycloak** (OIDC, SSO) + RBAC de 4 niveles (*Viewer*, *Author*, *Tenant Administrator*, *System Administrator*) + aislamiento por tenant forzado por token | Y además **API keys propias** (`POST /management/tenants/{tenantId}/api-keys`) |
| **Almacenamiento** | 🔵 **Archivos versionados, inmutables, sin base de datos externa.** Cada cambio es una versión nueva | *«zero external dependencies for storage»* + **auditoría completa por diseño**, que es exactamente lo que pide un expediente regulatorio |
| **Despliegue** | Un comando, Docker, HTTPS automático en servidor | Baja la barrera de una prueba de concepto a una tarde |

🔵 **Lo que la vuelve la mejor oportunidad de conector de esta KB:
`GET /ims/case/v1p1/discovery/imscasev1p1_openapi3_v1p0.json`.** **El servidor sirve su propio OpenAPI 3**, así que el
conector MCP se **genera** —el camino de `oneroster-ts`, 164 métodos con 39 commits— en vez de escribirse a mano. Ver
**P60**.

🔴 **Y la ausencia que la acompaña, medida y no inferida: MCP no aparece en el repo.** Cero menciones en el README
crudo. **La página renderizada de GitHub sí dice «MCP», y es el menú de GitHub** — quinta colisión de esta KB y la
primera por *chrome* de plataforma.

⚠️ **Lo que falta medir (gap 52): la forma exacta de las rutas.** Los dos documentos del repo se contradicen —
`DEVELOPER.md` escribe `/management/tenants/{tenantId}/CFItems/{id}` y
`FRAMEWORK_EDITOR_BACKEND_INTEGRATION.md` escribe
`/management/tenants/{tenantId}/ims/case/v1p1/CFItems/{itemId}`— y **el `FRAMEWORK_MANAGEMENT_GUIDE.md` que el README
principal ofrece como referencia completa de endpoints devuelve 404 en `main`**. **Las rutas exactas que quedan
anotadas para el pase 30, para no volver a buscarlas:**
`apps/opencase/docs/DEVELOPER.md`, `apps/opencase/docs/FRAMEWORK_EDITOR_BACKEND_INTEGRATION.md`,
`apps/opencase/docs/DataModel.md`, `apps/opencase/docs/RESTBindings.md` (1,5 MB, el binding REST oficial de CASE v1.1)
y `apps/opencase/docs/Licensing.md`.

## Capa de reutilización de contenido (Libraries v2 *upstream/downstream*) — agregada en el pase 31 del 2026-10-02

Treinta pases trataron el authoring como *«escribir en un curso»*. Leyendo `v2/urls.py` de `openedx/edx-platform`
apareció una capa que **ningún archivo de esta KB había registrado**: el curso no es el único lugar donde vive el
contenido, y **hay un mecanismo de propagación en el core**.

| Ruta (`/api/contentstore/v2/…`) | Vista | Para qué sirve |
|---|---|---|
| `downstreams/` | `DownstreamListView` | lista los bloques que consumen un *upstream* |
| `downstreams/<usage_key>` | `DownstreamView` | el vínculo de un bloque con su origen |
| `downstreams/<course_key>/summary` | `DownstreamSummaryView` | resumen por curso: qué está sincronizado y qué no |
| **`downstreams/<usage_key>/sync`** | **`SyncFromUpstreamView`** | **propaga** el cambio del origen al bloque del curso |

**Por qué importa para un agente.** Un agente autor que mantiene contenido en 40 cursos tiene dos economías posibles:
editar 40 veces, o **editar una vez en la biblioteca y sincronizar**. La segunda existe en el core, es REST, y esta KB
la estaba cotizando como trabajo manual. **Es el primitivo de propagación de P55 y P63.**

⚠️ **Lo que no se midió** (**gap 59**): si `SyncFromUpstreamView` resuelve conflictos cuando el bloque *downstream* fue
editado localmente, y si el conector oficial `openedx-mcp` expone esta capa — **sus 7 rutas CMS no la incluyen**, así
que hoy se alcanza por REST directo y no por MCP.

- Repo: [github.com/openedx/edx-platform](https://github.com/openedx/edx-platform) — **AGPL-3.0**, árbol
  `cms/djangoapps/contentstore/rest_api/v2/`. Verificado por `raw.githubusercontent.com` el 2026-10-02.

## Capa de *rostering* e identidad permisiva — agregada en el pase 31 del 2026-10-02

Hallada ejecutando la consigna del pase 30: **consultar el registro de paquetes por el nombre del estándar**, no del
protocolo. Son librerías para construir arriba, con licencia permisiva verificada en el registro.

| Repo / paquete | Licencia | Estándar | Verificación | Nota |
|---|---|---|---|---|
| [`LongsightGroup/oneroster`](https://github.com/LongsightGroup/oneroster) | **MIT** ✅ | **OneRoster 1.2** | ✅ repo + `package.json` 200 | *«Faithful OneRoster 1.2 for TypeScript — CSV and portable REST contracts»*. Cubre **los dos perfiles** del estándar (CSV y REST), que es lo que distingue una implementación completa de un cliente parcial. v0.3.0, modificado 2026-07-15 |
| [`@eduware/oneroster`](https://registry.npmjs.org/@eduware%2Foneroster) | **MIT** ✅ | OneRoster **1.1 + 1.2** | ⚠️ paquete sí, repo **404** | **Trae servidor MCP** (ver `agents/top.md`). v1.2.11, modificado 2026-07-10 |
| [`@ajna-inc/openbadges`](https://registry.npmjs.org/@ajna-inc%2Fopenbadges) | **Apache-2.0** ✅ | **Open Badges 3.0** + OAuth 2.0 | ⚠️ paquete sí, repo no declarado | **La primera pieza de OB 3.0 de esta KB.** Módulo para Credo-TS (agentes de credenciales verificables). v0.6.3, modificado 2026-05-19 |
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** ✅ | **LTI 1.3 Advantage** | ✅ repo 200 | v7.0.6, modificado **2026-09-18**. Mantenido activamente. **Sin MCP** (medido: 0 menciones en el README) |
| [`pylti1p3`](https://pypi.org/project/pylti1p3/) | MIT | LTI 1.3 Advantage (Python) | ✅ PyPI y repo (`dmitry-viskov/pylti1.3`, por `README.rst`/`setup.py`) | 🔴 **Última publicación `2022-11-20`.** El repo existe y está registrado en esta KB con 138 ★: lo detenido es **la publicación**. Ver la advertencia de mantenimiento, abajo |

### 🔴 La asimetría de mantenimiento de LTI, y es una decisión de stack

El mismo estándar obligatorio —LTI 1.3, el que toda plataforma educativa tiene que hablar— tiene:

- **lado JavaScript**: `ltijs` v7.0.6, publicado **este mes** (2026-09-18), Apache-2.0, repo verificable;
- **lado Python**: `pylti1p3` v2.0.0, última publicación **2022-11-20** — **casi cuatro años**.

**Consecuencia práctica para un *engagement*:** un tool LTI nuevo en Python arranca sobre una dependencia congelada
—sin parches de seguridad publicados desde 2022— mientras el equivalente JS está vivo. No es una nota al pie: **es un
criterio de elección de lenguaje para la capa de integración**, y conviene decirlo en la propuesta antes de que lo
descubra el *security review* del cliente.

### ⚠️ Caliper: hay código de 2026 y no se puede usar

[`@timeback/caliper`](https://registry.npmjs.org/@timeback%2Fcaliper) v0.3.3, **modificado 2026-09-25** — el paquete más
fresco de todo este pase— es un *«Caliper Analytics client SDK»* y **no declara licencia** (`license: null` en el
registro, sin repo declarado). Esta KB venía diciendo que Caliper dejó de ser open source el 2023-06-17 y que sólo
quedaban los SDK previos. **El matiz corrige la conclusión y la empeora:** no es que no haya código nuevo, es que
**hay código nuevo de 2026 y es jurídicamente inusable**. No entra como fundación. Entra como advertencia.


## Capa de *assessment* y empaquetado permisiva — agregada en el pase 32 del 2026-10-02

Hallada ejecutando la **acción 3 del pase 31** (registro de paquetes sobre los estándares sin segunda vuelta). Dos
hallazgos, y los dos **corrigen un registro propio de esta KB**: el pase 28 había medido por tres métodos que la capa QTI
utilizable era **PHP**, y la capa de empaquetado no tenía puerta de agente.

| Repo / paquete | Licencia | Estándar | ★ | Stack | Verificación | Qué aporta |
|---|---|---|---|---|---|---|
| [`course-code-framework/coursecode`](https://github.com/course-code-framework/coursecode) | **MIT** ✅ | **SCORM 1.2 + SCORM 2004 + cmi5 + LTI 1.3** | 5 | JavaScript | ✅ repo 200 + `coursecode@0.1.61` en npm (`modified` 2026-07-20) | 🟢 **La primera puerta MCP de la capa de empaquetado de esta KB.** Framework de *authoring* multi-formato por CLI con **servidor MCP incorporado** (Claude Code, Codex, Cursor, CourseCode Desktop). Cubre **cuatro estándares en una sola pieza permisiva**, con *preview* local y guías dedicadas a agentes (`COURSE_AUTHORING_GUIDE.md`, `COURSE_OUTLINE_GUIDE.md`) |
| [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | **MIT** ✅ | **QTI 3** (+ migración desde 1.2 / 2.x) | 5 | TypeScript | ✅ repo 200 + `@longsightgroup/qti3-migrator@0.13.1`, `modified` **2026-10-01** | 🔴 **Rompe el «QTI es PHP» del pase 28.** **12 paquetes** publicados: `qti3-core` (parser + validación + *scoring*, **cero dependencias de terceros**), `-player` (web component), `-player-react`, `-player-preact`, `-conformance`, `-a11y`, `-fixtures`, `-pnp`, `-writer`, `-migrator`, `-transcoder`, `-cli`. Trae `AGENTS.md`, **no MCP** |
| [`tincan`](https://pypi.org/project/tincan/) | **Apache-2.0** ✅ | **xAPI / Tin Can** (Python) | — (PyPI) | Python | ✅ PyPI 200 (`RusticiSoftware/TinCanPython`) | La implementación canónica y permisiva de xAPI en Python. **Sin MCP.** Es el nombre correcto por el que buscar esta capa (ver la colisión, abajo) |

⚠️ **Honestidad de adopción, y hay que presentarlo así en propuesta:** los dos hallazgos *headline* tienen **5 ★**. Son
hallazgos **de capacidad y de licencia, no de adopción** — resuelven un bloqueo técnico con licencia permisiva y tienen
comunidad mínima. Fijar versión y prever *fork* es el mismo requisito que esta KB ya escribió para `oneroster-ts`.

⚠️ **Y una pieza relevante que queda afuera por licencia:** `@citolab/qti-convert-local-ai` (conversión de planilla a
paquete QTI del lado del navegador) es **GPL-3.0-only**. Sirve como referencia, no como base de un entregable cerrado.

### 🔵 El método que encontró el MCP, porque el barrido estándar lo declaraba ausente

**La descripción de `coursecode` en npm no menciona MCP en ninguna parte.** Un barrido por campo `description` —el que
esta KB venía corriendo— **lo habría registrado como ausencia medida**. Apareció al **abrir el README**, que es
literalmente lo que la tendencia 89 manda y lo que el automatismo se saltea. **Regla: en esta capa, la ausencia de MCP
sólo se declara después de leer el README, nunca después de leer la descripción del paquete.**

### 🔴 La colisión del término «xAPI» — la quinta y la sexta de esta KB, y las dos son MIT

Buscar `xapi` en los registros devuelve **tres dominios distintos con el mismo nombre exacto**, y **dos de los tres no
tienen nada que ver con educación**:

| Paquete | Licencia | Qué es realmente |
|---|---|---|
| `tincan` (PyPI) / `learning_locker` (npm) | Apache-2.0 / — | ✅ **xAPI educativo** (Experience API / Tin Can), LRS |
| [`xapi-labs/xapi-cli`](https://github.com/xapi-labs/xapi-cli) → `xapi-to` | **MIT** ⚠️ | 🔴 *Marketplace* de APIs comerciales: **BlockPI RPC, Binance Web3, cripto, dominios/DNS**. README de 47.905 caracteres con **cero** menciones de *«Experience API»*, *«Tin Can»* o *«learning record»* — **y aun así se presenta como *«Agent-friendly CLI for xAPI»* e instala un skill de agente** |
| `xapi-python` (PyPI) | **MIT** ⚠️ | 🔴 **«The xStation5 API Python library»**: el API del bróker de **forex XTB** |

**Por qué esto es un riesgo de método y no una curiosidad:** las dos trampas son **MIT y activas** (`xapi-to`,
`modified` 2026-09-29), así que **el filtro de licencia no las descarta** y la que peor engaña **se anuncia como
agéntica**. Un barrido que ordene por nombre + licencia + frescura las habría promovido a la tabla de agentes.
**Buscar `"Experience API"` o `"Tin Can"`, nunca `xapi` a secas.**

- Verificado por `registry.npmjs.org`, `pypi.org/pypi/<pkg>/json` y lectura de README el **2026-10-02**.

## 🔎 La capa que apareció consultando REGISTROS en vez de GitHub — agregada en el pase 39 del 2026-10-02

**Esta sección existe por un cambio de canal, no por un cambio de criterio.** Treinta y ocho pases barrieron GitHub
buscando nombres con `mcp` y `agent`. El pase 38 descubrió, cerrando el gap 48, que la puerta que esta KB declaraba
ausente llevaba dos meses publicada **en PyPI por el propio proyecto**, y dejó escrita la acción: **consultar npm,
PyPI, Packagist y RubyGems por el nombre del PROYECTO.** Ejecutada sobre **23 términos × 4 registros**, devuelve
**ocho piezas nuevas**, **cinco homónimos** y **nueve ausencias confirmadas por segundo instrumento**.

### Lo que hay que saber del canal antes de usarlo otra vez

| Hecho medido | Consecuencia práctica |
|---|---|
| Los cuatro registros responden **200** en este entorno; `github.com` por `curl` responde **403 para todo** | La existencia se verifica con **`git ls-remote`**, no con `curl` (tendencia 131) |
| **PyPI no tiene API de búsqueda JSON**: hay que raspar `pypi.org/search/?q=` | El JSON por proyecto **confirma** un nombre, nunca lo **descubre** (tendencia 127) |
| **El campo `repository` del registro no prueba que el repo sea legible** | 2 de 8 altas tienen repo **ilegible** y 1 **no declara repo**: el tarball es el único canal de auditoría (tendencia 140) |
| El nombre del proyecto **colisiona** con proyectos ajenos más populares | `folio` → *redlining* de `.docx`; `kolibri` → *design system* alemán. **El filtro de licencia no protege contra homonimia** (tendencia 96) |

### Las piezas, por rol de infraestructura

| Pieza | Licencia | Rol en una arquitectura | Por qué es fundacional y no sólo un conector |
|---|---|---|---|
| `dasgltd/mcp-brasil` | **MIT** | **Ingesta de datos educativos públicos (BR)** | 15 datasets, 97 tools, **23 tags**, PyPI (18 releases), **canario semanal de salud de fuentes en CI**. La educación son 2 datasets y **13 tools**: ENEM y Censo Escolar, **sobre descarga de microdatos**, porque el INEP no publica API. **Es el pipeline que P77 describía, ya escrito** |
| `maxxeddev/open-badges-mcp` | **MIT** | **Emisión y verificación de credenciales** | No es un lector de spec: **firma** con `Ed25519` + `DataIntegrityProof` + `did:key` y valida contra el *schema* `ob_v3p0_achievementcredential` y los contextos de `purl.imsglobal.org`. Es la pata que la capa de credenciales de esta KB tenía declarada ausente desde el pase 9 |
| `ed-fi-sdk-mcp` | **Apache-2.0** | **Exploración del *Data Standard* de Ed-Fi** | **11 tools de esquema, cero de dato**. Es infraestructura **de desarrollo**: un agente que escribe la integración Ed-Fi la usa para no inventar endpoints. 🔴 **No es una puerta al ODS** y decirlo al revés es afirmar algo falso |
| `@ink-waffle/sisu-mcp` | ⚠️ MIT (campo npm) | **SIS de educación superior** | Cubre matrícula, derechos de estudio y expediente — **la capa administrativa que ninguna puerta de LMS de esta base toca**. Sisu es el SIS de las universidades finlandesas (Funidata, consorcio universitario) |
| `frappe-mcp-server` | ⚠️ ISC (campo npm) | **ERP académico por el framework** | Llega a **ERPNext**, **Frappe Education** y **Frappe LMS** por DocType. 🔴 `call_method` + `delete_document` = escritura total: pieza de infraestructura **que exige un *gateway* delante** |
| `suren-kk/armenian-national-library-mcp` | **MIT** | **Repositorio / biblioteca sobre DSpace** | **23 tools, todas `READ_ONLY` por construcción** (el *helper* `registerEnvelopeTool` fija la anotación). Lectura larga por *chunks* con continuación explícita. 🔴 Apuntada a una instancia: **implementación de referencia**, no conector genérico |
| `PabloPC05/mcp-usc` · `JOSETRA44/DUTIC-mcp` | **MIT** | **Puerta institucional de LMS** | Ver la clase nueva, abajo |

### 🔵 La clase que estas dos consolidan: **la puerta de agente de UNA institución**

El pase 35 admitió `jbnu-lms-mcp` (U. Nacional de Jeonbuk) anotando que era *«categoría nueva: la puerta de UNA
institución, no de un producto»*. **Con este pase la categoría ya tiene cuatro miembros y deja de ser anécdota:**

| Pieza | Institución | Región | Licencia | Tools |
|---|---|---|---|---|
| `moon0825/jbnu-lms-student` | U. Nacional de Jeonbuk (전북대학교) | **APAC** (Corea) | MIT | 25 |
| `PabloPC05/mcp-usc` | U. de Santiago de Compostela | **EMEA** (España) | MIT | **91** |
| `JOSETRA44/DUTIC-mcp` | U. Nacional de San Agustín de Arequipa | **LATAM** (Perú) | MIT | 12 |
| ⛔ `NicolasViruel/moodle-utn-mcp` | U. Tecnológica Nacional | **LATAM** (Argentina) | 🔴 **ninguna** | — |

🔵 **Las cuatro son de alumnos o personal de la propia institución, las cuatro son sobre Moodle o el LMS local, y
ninguna se publicó en un registro de paquetes.** Por eso el canal del registro **no** las encuentra: a estas se llega
por búsqueda en lenguaje natural y en el idioma local, que es el instrumento que este pase usó para LATAM.
🔴 **Y la de Argentina, la más fresca de las cuatro, no tiene licencia: no se puede usar.** Para un engagement
LATAM eso es exactamente el tipo de dato que conviene saber antes y no después.

### ⚠️ Lo que esta capa NO resuelve, dicho con el mismo detalle

- **El conector genérico de DSpace sigue sin existir.** Hay una implementación de referencia sobre una instancia.
- **El `tools/list` observado sigue sin medirse en ninguna de las ocho**: todas las cifras de este pase son de **código
  fuente o de tarball publicado**, no de protocolo. El *daemon* de Docker no corre en este entorno (**gap 80**).
- **Dos de las ocho declaran licencia sólo en el manifiesto del registro.** Entran con reserva explícita, no como
  equivalentes a las que tienen `LICENSE` textual (tendencia 129).

## 🧭 El barrido por SDK del pase 43 — **una alta real, dos confirmaciones con dato nuevo, y una premisa del handoff refutada** (2026-10-02)

Este pase ejecutó la acción que el handoff pedía: **re-medir por SDK las ausencias que esta base había declarado por
etiqueta** (tendencia 73), con el método *estándar + `SDK`/`client`/`library` + abrir el README crudo y buscar «MCP»
adentro*.

🔵 **El resultado honesto, dicho antes de la tabla: de las piezas que el barrido devolvió, esta base ya tenía casi
todas.** Eso **no** es un barrido fallido —es la confirmación de que la capa de estándares de esta KB está saturada— pero
sí obliga a escribirlo como confirmación y no como alta, porque una alta inventada es peor que un pase sin altas.

**Las licencias se leyeron del archivo `LICENSE`, no del README ni del manifiesto** (tendencia 129).

### 🟢 La única alta real del barrido

| Repo | Licencia (del `LICENSE`) | ★ / forks | Lenguaje | Por qué entra |
|---|---|---|---|---|
| [`Simon-Initiative/lti_1p3`](https://github.com/Simon-Initiative/lti_1p3) | 🟢 **MIT** (*Copyright (c) 2021 Carnegie Mellon University*) | **16** / 4 | Elixir | 🔵 **Hace el lado PLATAFORMA además del lado Tool, y eso es la rareza.** Toda la capa LTI que esta base tenía es *tool provider* —`ltijs` lo es por diseño, `pylti1p3` también—. Esta biblioteca implementa **Platform y Tool**: registros, *deployments* y validación de *launch* del lado tool, y creación de instancia de plataforma con redirección de autorización del lado platform. Es lo que hace falta para construir **el lado LMS**, no el lado de la herramienta. Del **Simon Initiative** de Carnegie Mellon (la gente de OLI/Torus) |

### Las dos confirmaciones, con el dato nuevo que aportan

| Repo | Lo que esta base ya tenía | 🔵 El dato nuevo de este pase |
|---|---|---|
| [`opensalt/opensalt`](https://github.com/opensalt/opensalt) — **MIT**, 45 ★ | Desde el **pase 14**, con la advertencia correcta: *estable **3.2.0** (sept 2023) apunta a **CASE v1.0**; v1.1 en `develop`* | **`develop` tiene 5.027 commits y 135 issues abiertos: el proyecto está activo**, y el README hoy lo presenta como **registro de LER** (*Learning and Employment Record*) —competencias, credenciales, *pathways*, empleos, emisores—, no sólo como editor de marcos. 🔴 **La divergencia estable/`develop` es el dato que se cotiza:** lo activo y lo compatible con CASE 1.1 **no está en el release**. La recomendación del pase 14 —*elegir por fecha de certificación, no por estrellas*— **se mantiene y se afila**: OpenSALT se adopta desde `develop`, con el costo de soporte que eso implica, o no se adopta |
| [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) — **Apache-2.0** | Registrado como validador de **Open Badges + CLR** | **El README dice *«primarily a validator for Open Badges 3.0»***, y que **acepta además OB 2.0**. 🔵 Eso lo precisa: esta base sabía que **CaSS implementa OB 2.0, no 3.0**, y ahora el validador de la credencial de **P84** queda nombrado como **de 3.0 primero**. **17 ★ / 12 forks** |

### 🔴 La premisa del handoff que este pase refuta

El handoff del pase 42 daba por bueno que, aunque **Caliper dejó de ser open source el 2023-06-17**, *«los SDK previos
siguen publicados»*. **Es falso para el canal público:**

* `IMSGlobal/caliper-php` → **404** en `raw.githubusercontent.com`, en `master` **y** en `main`; también **404** bajo
  `1EdTech/caliper-php`.
* ⚠️ El paquete **sí** figura en Packagist (`imsglobal/caliper`), que es exactamente la asimetría de la tendencia 127:
  **el registro confirma el nombre pero no entrega el código.**

🟢 **Y la respuesta ya estaba en esta base, que es lo que vuelve útil la refutación:** la implementación PHP de Caliper
que **sigue siendo legible** es el fork de la **Universidad de Michigan**,
[`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public) — ⚠️ **LGPL-3.0**, no
permisiva, ya registrada en `agents/top.md` desde el pase 9. **Instrumentar Caliper no se cotiza contra el repo oficial:
se cotiza contra el fork LGPL o contra la especificación, o se afilia al cliente.**

**Y la colisión de nombre, la séptima de esta KB:** buscar «Caliper» devuelve antes **`llnl/Caliper`** (instrumentación y
*profiling* de performance) y **`google/caliper`** (microbenchmarking de Java, **deprecado**). **Ninguno** tiene que ver
con analítica de aprendizaje.

### 🟢 Lo que sí es medición nueva: MCP, contado en el README crudo de cada pieza

| Pieza | Licencia (del `LICENSE`) | Menciones de `MCP` / *model context protocol* |
|---|---|---|
| `Cvmcosta/ltijs` | **Apache-2.0** ✅ | **0** |
| `Simon-Initiative/lti_1p3` | **MIT** ✅ | **0** |
| `opensalt/opensalt` | **MIT** ✅ | **0** |
| `1EdTech/digital-credentials-public-validator` | **Apache-2.0** ✅ | **0** |
| `luisgf/openbadgeslib` | 🔴 **LGPL-3.0** | **0** |

🟢 **El gap 42 queda cerrado por un canal que sí lo examinó**, y no por agotamiento de etiquetas: **CaSS sigue siendo la
única pieza de estándar educativo de esta base con puerta nativa de agente.**

⚠️ **Y la trampa de fork volvió a aparecer** (tendencia 132): la búsqueda devolvió **`kristofb/ltijs`** antes que el
canónico **`Cvmcosta/ltijs`** —el que referencia la documentación del propio proyecto—, y es el canónico el que se midió.

## 🔬 Las tres dependencias que el pase 46 midió por código, y las dos cifras de esta base que quedan confirmadas (2026-10-02)

**Este pase no agrega repos fundacionales: mide tres que ya estaban, y es la primera vez que las tres se verifican
leyendo el árbol en vez del README.** Las tres sostienen entregables concretos de esta KB, así que su estado es lo que
decide si entran en una propuesta.

| Repo | Licencia | `HEAD` / versión | Qué se midió | Veredicto |
|---|---|---|---|---|
| [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | **Apache-2.0** | `7f45689` (**2026-04-01**) | SPI de *proctoring*: 14 métodos, alcance de red transitivo | 🔴 **corrige P94** — Zoom **5 de 14**, no 2, y **0 directos** |
| [`giacomomaria81/scorm-mcp-server`](https://github.com/giacomomaria81/scorm-mcp-server) | **MIT** | `fd5f110` (**2026-09-03**), **v2.3.0** | tools, licencia, XSD, puntos de extensión | ✅ **3 tools y MIT confirmados por código**; **9** puntos de extensión legales |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | **MIT** | `main` | `services/provenance.py` completo | 🔴 **cero granularidad por tramo** — no estaba «a medias», no estaba |
| [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** | `main` | `references/provenance-policy.md` | ✅ **9 valores**, confirmados uno a uno y commiteados como *fixture* |

### `seb-server` — la fila que cambia una cotización

**`HEAD 7f45689` coincide con el que ya citaba `compose/code/seb-proctoring-validator/`**, así que la auditoría cae sobre
el mismo árbol que sostiene la cotización de *proctoring* — **reverificado, no asumido**. Lo medido:
`RemoteProctoringService.java` son **130 líneas** y **14 métodos abstractos**; `JitsiProctoringService` **481 líneas de
código** y `ZoomProctoringService` **912** — 🔵 **y la métrica queda NOMBRADA, que faltaba desde el pase 43: son
no-blancas-no-comentario; `wc -l` da 583 y 1.116.** El alcance de red transitivo da **Jitsi 1 de 14** (correcto) y
**Zoom 5 de 14 con 0 directos**. Detalle, grafo y 20 aserciones (⚠️ **20 con la ruta a un checkout de seb-server; 19 sin ella** — condición agregada en el pase 48) en
[`compose/code/proctoring-reach-audit/`](../compose/code/proctoring-reach-audit/README.md). **Para cotizar, P102.**

### `scorm-mcp-server` — la capa de empaquetado, ahora medida

**3 tools** (`scorm_package`, `scorm_validate`, `scorm_selftest`) ✅ **confirmando la cifra que esta base traía desde el
pase 32**, **3.517 líneas** de TypeScript en 6 módulos (`converter` 1.010, `tom` 652, `index` 559, `runtime` 506,
`ui` 495, `validate` 295), **15 XSD empaquetados** (14 de ADL/IMS + `xml.xsd` de W3C) que dan **conformidad offline**
porque `xsi:schemaLocation` resuelve a hermanos dentro del ZIP, y **9 checks** en `scorm_validate`.
⚠️ **`scorm_version` NO es una cuarta tool: es un campo del JSON de respuesta** — un `grep` de `"scorm_[a-z_]+"` devuelve
cuatro cadenas y sólo tres son herramientas. **Colisión de instrumento, registrada.**

🟢 **Y el hallazgo que lo vuelve pieza de cumplimiento y no sólo de empaquetado:** `metadataType` de su
`imscp_v1p1.xsd` termina en `grp.any` =
`<xsd:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>`, y **`grp.any` aparece en
NUEVE `complexType`**. 🔴 **Con una condición dura medida con `xmllint`: el marcador debe declarar su propio
*namespace*** — en el *namespace* por omisión el paquete **no valida**. Ver **P105**.

### Las dos fuentes del componente del Artículo 50(2)

- **`OpenTutor/apps/api/services/provenance.py`**: **72 líneas, 2 funciones**. `build_provenance` tiene **12
  parámetros**, `generated: bool = True` **por omisión** (🟢 falla hacia el lado seguro) y **ninguno por tramo**.
  `merge_provenance` unifica `source_labels` como conjunto ordenado y descarta `None` — **el detalle que permite
  extender el payload sin romper el merge**, y por eso la extensión del pase 46 es compatible.
- **`lineage-skill/references/provenance-policy.md`**: **9 valores** exigidos *«for every consequential claim, task
  answer, rubric rule, feedback judgment, and Personal Skill rule»*. El archivo queda **commiteado como *fixture*** en
  `compose/code/aiact-50-2-marking/fixtures-provenance-policy.md` y `test_marking.py` **asevera el vocabulario contra
  él**, así que una deriva upstream rompe la prueba en vez de aparecer en producción.
