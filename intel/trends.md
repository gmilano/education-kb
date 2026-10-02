---
industry: education
region: Global
updated: 2026-10-02
---

# 📡 Tendencias — education

> Ventana de investigación: septiembre 2026. Verificado 2026-09-30; el pase 11, el 2026-10-01.
> **Pase 47 del 2026-10-02:** **se ejecutan las tres acciones del pase 46, las tres rinden, y la primera rinde
> CORRIGIENDO la conclusión del pase anterior.** 🔴 **El gap 97 era verdadero para SCORM 2004 y falso para SCORM 1.2:**
> el mismo `buildManifestFor` emite dos dialectos y el comodín de 1.2 es **`processContents="strict"`**, así que un
> marcador foráneo sin declaración **invalida el paquete** en vez de pasar inadvertido. 🔴 **Y de paso aparece un
> defecto que no es del marcador: `scorm_validate` rechaza un paquete con metadatos LOM ESTÁNDAR de SCORM 1.2**, porque
> su `wrapper12.xsd` importa 2 de los 3 *namespaces* que el propio repo empaqueta — **arreglo de una línea**. 🔴 **La
> acción 2 encuentra que P85 se cita como entregable en dos tablas de solución y su código no está en el
> repositorio** (gap 103), más dos cifras vencidas y una que no coincide con ningún instrumento. 🔴 **La acción 3
> responde NO: 0 de 33 filas expuestas emiten un límite dentro del texto que generan**, y las tres candidatas resultan
> límites de ENTRADA al abrirlas. Tendencias **197**–**210**.
> **Pase 45 del 2026-10-02:** **se ejecutan las tres acciones del pase 44, las tres rinden, y dos dejan código que corre en este repositorio.** 🔴 **El hallazgo que manda es de la abstracción y no del dato: en UniTime el verbo HTTP NO es la frontera de escritura.** `ScriptConnector.doGet` despacha por parámetro de query y dos ramas escriben —`?script=` **llama `doPost`, así que un GET ejecuta un script del servidor**, y `?delete=` borra un ítem de la cola—, de modo que **la partición lectura/escritura que es el corazón de las DOS puertas de esta KB no es sólida** (tendencia **176**). La política ya negaba `script` por nombre, así que **el resultado era correcto y el motivo documentado no lo era**; desde este pase el rechazo es un **piso y no una política**. 🔴 **Y el control (b) del pase 44 FALLABA en la otra puerta por un motivo que el pase 42 no podía ver: `getName()` no es la ruta** — `ApiServlet` hace `getBean(servletPath + pathInfo)`, así que **la ruta es el nombre del bean de Spring**, los 15 coinciden hoy y por lo tanto **el dato era correcto y el método no** (tendencia **175**). **46 aserciones en verde** (eran 23), **gap 93 CERRADO**. 🟢 **El costo de P55 queda cerrado con fórmula:** `llamadas = 1 + bloques`, en `profundidad` olas, hermanos en paralelo — **18 llamadas y 4 olas** para un curso de 17 bloques, con **33 aserciones** contra un *stub* que reproduce los cuatro comportamientos reales del endpoint (**gap 94 CERRADO**, tendencia **179**); y por el camino apareció que **un cuerpo mal formado se reporta con TRES estatus distintos y sólo uno es el correcto: el 403 de Open edX es un error de payload disfrazado de credenciales** (tendencia **178**). 🟢 **Y la medición del Artículo 50(2) contradice lo que el pase 44 predijo** (**gap 91 CERRADO**): **32 de las 66 filas —el 48 %— ponen contenido sintético delante de una persona**, **0 de 33 repos** tiene artefacto o dependencia de marcado en **24.202 archivos** y **26 manifiestos**, **pero hay UNA bandera legible por máquina** —`OpenTutor` emite `{"generated": true}` al cliente, con default `True`— y **la granularidad que le falta está en otra fila de la misma tabla** (`lineage-skill`, 9 valores por afirmación, 4 sintéticos), **y ninguna de las dos sabe de la otra** (tendencias **180**–**182**). ⚠️ **Y una trampa de barrido medida: 13 de los 15 hits de «procedencia» son procedencia de FUENTE y no sintética — confundirlas sobreestima el cumplimiento 13× sobre esta misma muestra.** 🔵 **El encuadre de calendario que hay que corregir aunque la fecha esté bien: el 2026-12-02 es el plazo de gracia de lo ya desplegado, no el inicio; para un desarrollo nuevo el Artículo 50(2) rige desde el 2026-08-02 y ya está vencido — y el deber recae en el PROVEEDOR, no en el *deployer*** (tendencia **183**). 🔴 **Gap 92 ampliado a cuatro dominios bloqueados.** Ver las tendencias **175**–**183** y los patrones **P99**–**P101**.
> **Pase 44 del 2026-10-02:** **se ejecutan las tres acciones del pase 43, las tres rinden, y la primera rinde encontrando que la medición del pase anterior describía rutas que no existen.** 🔴 **El hallazgo que manda: ninguna ruta de la puerta de SEB Server era una URL.** Los **30** controladores mapeados del servicio cuelgan de una propiedad de Spring —**27** de `"${sebserver.webservice.api.admin.endpoint}" + API.X_ENDPOINT`—, **no hay una sola ruta base literal**, y el valor que trae el árbol es `/admin-api/v1`: lo que la tabla llamaba `/exam` **es `/admin-api/v1/exam`**, así que una puerta que proxea el sufijo **da 404 en el 100 % de las llamadas** (tendencia **166**). ✅ **Acción 1 CUMPLIDA sobre el servicio entero: de 79 operaciones sobre 4 controladores a 341 sobre los 31 `@RestController`**, 30 endpoints, **170 escrituras**, y `test_gate.py` de 11 a **37 aserciones, 37 en verde** — más `extract_surface.py`, que regenera las tablas contra un checkout en vez de transcribirlas. 🔴 **Y los otros tres defectos son del instrumento, no del upstream: (a) `endpoints.tsv` tenía 41 de 55 constantes y las 14 que faltaban eran EXACTAMENTE las compuestas** —`OTRO_ENDPOINT + "/sufijo"`, 14 de 14 sin excepción— **y lo perdido es la superficie de autenticación completa** (`/oauth/token`, `/oauth/revoke-token`, `/oauth/jwttoken`, `/oauth/jwttoken/verify`) **más `/admin-api/v1/monitoring/proctoring`**, la capa que esta base nombra como alto riesgo bajo dos reguladores (tendencia **167**); **(b) el extractor contaba la DECLARACIÓN DE CLASE como una operación**, así que cada controlador con mapeo de clase venía inflado en una fila fantasma —`/batch-action` figuraba con `1 own` y `BatchActionController` **no declara ninguna**— (tendencia **168**); **(c) `ActivatableEntityController` aporta 4 rutas heredadas y no 3**: faltaba `deactivate` (`API.PATH_VAR_INACTIVE`), así que todo controlador activable sub-reportaba una escritura. 🔵 **El matiz que afila el argumento de la puerta: `ReadonlyEntityController` niega 4 de las 5 escrituras a nivel de ruta y la quinta —`forceHardDelete`, `DELETE /{id}/force`— queda VIVA y se frena una capa más abajo**, por el override de `checkWriteAccess`; y «force» significa que saltea `validForDelete`, **no** la autorización (tendencia **169**). 🔴 **Una ruta en el árbol no es una ruta en ejecución: `LightController` está detrás de `@ConditionalOnExpression` y seb-server envía `light.setup=false`** (tendencia **170**). ✅ **Acción 2 CUMPLIDA y las tres preguntas tienen número: `create_xblock_response` devuelve `{locator, courseKey}` y el `locator` ES el usage key del bloque nuevo —el árbol es recursable sin un GET extra—; `category` no tiene restricción en un curso (`CharField(required=False)`, sin `choices`) y el único enum del árbol es `["html","problem","video"]` para bibliotecas; y `?view=minimal` es sólo de `retrieve`** (tendencia **171**). 🔴 **Pero la premisa de la pregunta estaba invertida: NO hay hijos que recorrer.** `get_block_info` lleva escrito *«children aren't being returned until we have a use case»*, así que el docstring del `v1` que llama *«tree-shaped»* a esa respuesta **es falso**, **2 de los 6 campos que promete la vista mínima son claves que el handler no emite**, y la única forma de obtener hijos es la combinación **no documentada** `?fields=customReadToken&view=minimal`, que da un nivel y **descarta `parent` en silencio** (tendencia **172**). 🟢 **Y el costo de P55 queda fijado porque el instrumento correcto es otro endpoint: `course_index/{course_id}` devuelve el outline anidado en UNA llamada; escribir es 1 POST por bloque**, paralelizable entre hermanos. ✅ **Acción 3: las dos fechas del pase 43 quedan CONFIRMADAS por un segundo canal independiente —Anexo III 2027-12-02, Anexo I 2028-08-02, Reglamento (UE) 2026/1744 publicado el 2026-07-24 y en vigor el 2026-07-27—, así que la recomendación comercial de EMEA NO hay que revertirla.** 🔴 **Pero NO contra el texto consolidado: `eur-lex.europa.eu` Y `artificialintelligenceact.eu` dan los dos `403` a CONNECT**, y el segundo es una **instancia nueva y no institucional del gap 65** (**gap 92**). 🟢 **Y el pase encuentra un plazo más cercano y más firme que el que esta base venía planificando: el Artículo 50(2) vence el 2026-12-02 —61 días desde hoy— para los sistemas generativos ya en el mercado antes del 2026-08-02**, con 50(1), 50(3) y 50(4) en vigor desde el 2026-08-02 y **sin prórroga**, confirmado por el 9.º plenario del Consejo Europeo de IA del 2026-09-17 (tendencia **173**, **gap 91**). 🔵 **`issuebadge/mcp-server` re-medido como el pase 43 pidió: sigue FUERA de la tabla** —4 commits, dependencia de `app.issuebadge.com`, no implementa OB 3.0— **pero ahora tiene v2.1.0, 1.106 líneas y 168 casos de test**, **no está en npm** (invisible al barrido por registro, como `learnmcp-xapi`) y **aporta la QUINTA variante de primitiva anti-bucle, la más débil: delega el freno en la API del proveedor, y el valor por omisión lo anula** —`idempotency_key` se genera por llamada, así que un reintento sin arrastrar la clave **emite un segundo certificado** (tendencia **174**, **P97**). ⚠️ **Y el barrido global devolvió por segunda vez consecutiva la capa genérica y material didáctico sobre AI: cero altas de agente, el canal está saturado.** Ver las tendencias **166**–**174**, los gaps **91**–**94** y los patrones **P96**–**P98**.
> **Pase 42 del 2026-10-02:** **se ejecutan las tres acciones del pase 41, las tres por EJECUCIÓN y no por lectura, y el resultado corrige la recomendación comercial que el pase 41 dejó escrita.** 🔴 **El hallazgo que manda: la ruta MPL-2.0 que el pase 41 prefirió *«porque no arrastra AGPL»* cuesta MÁS código que la AGPL** — `RemoteProctoringService` de `seb-server` es una **interfaz desnuda con 12 métodos obligatorios de 14**, mientras `ProctoringBackendProvider` de `edx-proctoring` es una **clase concreta con 0 obligatorios de 18**: no son rutas equivalentes con distinta licencia, son **distinto trabajo** (tendencia **157**). 🟢 **Y lo que vuelve cotizable la ruta SEB igual, medido archivo por archivo: su obligación de publicar es UN valor de enum.** El registro del proveedor es **abierto** (Spring inyecta `Collection<RemoteProctoringService>`, la fábrica no se toca) pero el **tipo está cerrado** (`enum ProctoringServerType{JITSI_MEET,ZOOM}`), así que un tercero obliga a tocar **1 de los 10 archivos *Covered*** que mencionan el enum — y por el copyleft **por archivo** de MPL-2.0 §1.10(a), **lo único que hay que publicar es ese valor**; el proveedor propio es archivo nuevo y queda propietario (tendencia **158**). ⚠️ **Hueco medido que se escribe en la propuesta y no se descubre en UAT: el validador de SEB cae a `return true` ante un tipo desconocido — tu proveedor pasa SIN validación de campos** (tendencia **159**). 🔴 **Corrección al pase 41: `LmsType` tiene SEIS valores con matriz de *features*, no cuatro, y `LMS_FULL_INTEGRATION` NO está en `OPEN_EDX` —sólo en `MOODLE_PLUGIN`—, mientras `MOODLE` a secas tiene `SEB_RESTRICTION` COMENTADA en el fuente: el LMS del cliente manda más que la licencia** (tendencia **160**, patrón **P91**). 🟢 **Acción 1 CUMPLIDA Y PROBADA: la puerta MCP de UniTime existe** — 26 tools generados del árbol (15 conectores × verbos reales), **13 expuestos**, y **23 aserciones en verde**, entre ellas la que importa: 🔴 **0 de 9 llamadas retenidas llegaron al upstream**, `script.post` incluido, que ejecuta un script del servidor (tendencia **161**, patrón **P92**). 🟢 **Acción 2 CUMPLIDA: 61 filas re-fechadas sobre 472 ramas, cobertura 61/61** — y el gap 89 tenía razón en las dos direcciones: **4 veredictos se promueven** (`algo-sensei` de FRÍO a ACTIVO porque **commiteó hoy**, más `gradescope-mcp`, `TutorIA` y `open-badges-mcp`) **y 2 se SOSTIENEN gracias al filtro** (`oneroster-ts` seguiría CONGELADO aunque el máximo ingenuo lo promovería 10 meses con un **commit vacío de bot**). 🟢 **Reparto corregido: 78,7 % activas contra el 69,4 % del pase 37 — la tabla está más viva de lo que esta base venía diciendo** (tendencia **162**). 🔴 **Las tres clases de «no es vida de proyecto» del pase 41 son SEIS, y la que más cuentas cambia es la que faltaba: `dependabot`** — `armenian-national-library-mcp` tiene **10 ramas dependabot** y parece 7 semanas más fresco de lo que es (tendencia **163**). 🔵 **Y el hallazgo de método es sobre un defecto de ESTE pase: mi primer filtro descartaba el tip de la rama por defecto, y `OpenTutor` y `Shiksha-Copilot` quedaban SIN fecha de vida. La regla que queda: el tip de la rama por defecto cuenta SIEMPRE —es historia mergeada—; los filtros sólo deciden si una rama no-defecto agrega vida encima** (tendencia **164**). 🔴 **La familia `Kuali` entra como registro histórico, no como dependencia: 4 repos, los cuatro muertos (6 a 9 años), *middleware* ECL-2.0 y las dos aplicaciones de verdad AGPL-3.0 — y esta KB tenía 0 menciones en 41 pases** (tendencia **165**). 🔴 **Fuente primaria nueva identificada y BLOQUEADA: el Consejo de Europa tiene una *2nd Working Conference* sobre las dimensiones REGULATORIAS de la AI en educación este mes, y `coe.int` da `EGRESS_BLOCKED` — instancia nueva del gap 65, y la de mayor autoridad para EMEA** (tendencia **166**). ⚠️ **Y la fecha vencida del AI Act reapareció por NOVENA vez, otra vez en el barrido de North America: deja de ser el error de una fuente y pasa a ser una propiedad del canal.** Ver las tendencias **157**–**166** y los patrones **P91**–**P92**.
> **Pase 41 del 2026-10-02:** **se ejecutan las tres acciones del pase 40, las tres rinden, y la de mayor valor comercial CORRIGE un veredicto que esta base había publicado como cerrado.** 🟢 **El hallazgo que manda estaba en un `README.txt` de 174 bytes dentro del paquete: `edx_proctoring/backends/` está *carved-out* en Apache-2.0 dentro de un repo AGPL-3.0** — verificado en el *wheel* y en el árbol — **así que el directorio donde se escribe un backend de *proctoring* propio no arrastra la AGPL** (tendencia **150**). 🔴 **El gap 84 (*«proctoring no tiene opción permisiva»*) queda corregido por DOS motivos independientes:** ése, y que **existe una capa de integración de examen fuera de Open edX, `seb-server` de ETH Zürich, MPL-2.0 — copyleft débil — con `OPEN_EDX`, `MOODLE`, `MOODLE_PLUGIN` y `OPEN_OLAT` ya escritos en su `enum LmsType`** (tendencia **149**). 🟢 **Y la pregunta comercial de la acción 3 se responde contando un cero: `ProctoringBackendProvider` tiene 18 métodos y CERO `@abstractmethod`, o sea es una base concreta — integrar *proctoring* propio en Open edX es implementar una interfaz (12 modelos, 20 rutas y las 2 rutas de supresión de datos ya existen), no escribir la capa** (tendencia **151**). 🔵 **El matiz que impide sobrevenderlo, medido con `ast` en el mismo pase: la carve-out NO es autocontenida, pero lo que cruza hacia la AGPL es vocabulario —constantes, nombres de excepción y valores de estado— y no lógica** (**gap 88**). 🔴 **Hallazgo de método que obliga a re-correr el pase 37: la rama por defecto puede ser la rama MUERTA de un proyecto vivo —`seb-server` mide 6 meses en `master` y commiteó AYER en `dev-3.0`— y la prueba de validez sobre las 10 filas paradas sostiene 10 de 10 veredictos, pero sólo al LEER EL AUTOR: el commit más nuevo de `oneroster-ts` es un commit VACÍO de un bot y el de `educhain` es un refactor firmado por un AGENTE, sin mergear** (tendencias **152** y **153**). ✅ **Gap 83 CERRADO por la historia de dos archivos, y baja de bloqueante a anotación: las dos licencias en conflicto son permisivas OSI** (tendencia **154**). ⚠️ **Gap 81 PARTIDO EN DOS clases con riesgo y acción distintos: `@timadey/proctor` declara MIT tres veces en el árbol y le falta el archivo; `sisu-mcp` tiene UNA declaración en todo el mundo** (tendencia **155**). 🔵 **Y el hallazgo de síntesis, que es el más vendible: el *proctoring* es la única capa de esta base nombrada como alto riesgo por DOS reguladores de dos regiones —Anexo III punto 3 de la UE (2027-12-02) y los seis sectores de Vietnam (2027-03-01, NUEVE MESES ANTES)— y es la que este pase midió sin NINGUNA competencia agéntica: 404 en 8 de 8 nombres de npm y 0 en los 46,6 MB del índice de PyPI** (tendencia **156**, **gap 86**). Ver las tendencias **149**–**156** y los patrones **P88**–**P90**.
> **Pase 40 del 2026-10-02:** **se ejecutan las tres acciones del pase 39 y las tres rinden, pero la primera rinde descubriendo que el instrumento del pase anterior está roto — y roto de la peor manera, devolviendo `200`.** 🔴 **`pypi.org/search/` responde `HTTP 200` con una página de desafío anti-bot en 28 de 28 términos**: un barrido corrido con el procedimiento del pase 39, sin control de contenido, **habría publicado 28 ausencias falsas y las habría llamado medición** (tendencia **141**). 🟢 **El reemplazo es mejor que el original y queda documentado: `pypi.org/simple/` devuelve 200 con 46.675.078 bytes y 903.402 nombres de paquete** — descubrimiento completo, sin ranking ni paginación (tendencia **142**). 🔴 **Y el barrido sobre las cuatro capas de administración académica devuelve el resultado más fuerte del pase, que es un vacío: no existe NI UNA puerta MCP de educación para *proctoring*, *timetabling*, admisiones, *student success* ni accesibilidad, en ninguno de los cuatro registros** — la única traza es `ucleeds-mcp-tester`, **el cliente de prueba de un MCP de *timetabling* cuyo servidor nunca se publicó** (tendencia **144**). 🟢 **La mejor alta en varios pases cierra la capa que esta base declaró la peor abastecida desde el pase 11: `datakind/student-success-tool` es MIT, y lo que la vuelve vendible no es el modelo sino que trae *model cards* y secciones de análisis de sesgo en el árbol**, con *«humans in the loop by design»* escrito en el README — la forma exacta del requisito estatal de North America (tendencia **148**). 🟢 **La capa de *proctoring* queda cerrada y la respuesta es copyleft:** `openedx/edx-proctoring` (**AGPL-3.0**), 🔴 **con `HEAD` de 4 meses y último release de 17** — de donde sale la regla de que **`HEAD` mide al proyecto y el release mide lo que el cliente instala** (tendencia **147**). ✅ **Acción 2 cumplida y el resultado es opuesto en las dos piezas por UNA línea de código: `mcp-usc` es 88 % portable (80 de 91 tools) porque su host es `os.getenv`; `DUTIC-mcp` es 8 % (1 de 12) porque el suyo es `export const HOST`** (tendencia **145**). 🔵 **Y al medirla apareció el mejor dato de LATAM en varios pases: la telemetría de `DUTIC-mcp` está escrita contra la Ley 29733 y la nombra en el código.** ✅ **Acción 3 cumplida y PROBADA, no descrita: el *gateway* de partición de tools existe, son 175 líneas de stdlib, y se verificó que recorta `tools/list` de 7 a 3, bloquea `delete_document` y `call_method` con `-32601` sin que lleguen al upstream, y que con allowlist vacía expone cero tools** (**P85**). 🔴 **Dos clases de evidencia nuevas: la licencia que se CONTRADICE entre el manifiesto y el árbol** (`exam-guard`: ISC contra Apache-2.0 — distinto del gap 81, y peor) y **la colonización del vocabulario: «proctor» ya significa supervisar al AGENTE, y «caliper» tiene seis homónimos no educativos y una sola pieza educativa** (tendencias **143** y **146**). 🔵 **Y el hallazgo de síntesis, que es el más accionable: en LATAM la dimensión menos adoptada es ADMINISTRACIÓN (34,1 %) — justo la capa que este pase midió vacía de open source. La brecha de oferta y la de adopción son la misma brecha.** Ver las tendencias **141**–**148** y los patrones **P85**–**P87**.
> **Pase 38 del 2026-10-02:** **se fue a buscar SUCESIÓN para las tres dependencias congeladas del pase 37 y el resultado es asimétrico: dos cierran con piezas permisivas vivas (tres MIT para Moodle, Apache-2.0 + MIT para OneRoster) y la tercera no — y el fork que parecía salvarla está 2 commits adelante, los dos de configuración de Cloud Run** (tendencias **132** a **135**, `gap 78` y `gap 79`).
> **Pase 34 del 2026-10-02:** **el pase completa el hallazgo del 33 en la dirección contraria y el resultado es una regla sobre el instrumento, no sobre un repo.** El pase 33 probó que el registro **no ve** open source real (`learnmcp-xapi`, invisible en PyPI y npm). 🔴 **Este pase encontró el falso positivo: `quizlar/mcp-server` es MCP, educativo, activo y su `LICENSE` dice MIT — y no tiene una línea de código.** Su `server.json` declara **`remotes` → `https://mcp.quizlar.app/mcp/`** detrás de una API key `sk-qz-<32>`: **la MIT licencia el manifiesto, la implementación es un servicio alojado propietario.** Es la **colisión 9** y es de **clase nueva** —colisiona la **superficie de la licencia**, no el nombre— y el control que la descarta **es un campo** (tendencias **103** y **104**). ✅ **Acción 1 del pase 33 ejecutada sobre las cuatro ausencias del mapa por estándar: Caliper, CASE y CEASN quedan CONFIRMADAS con los dos instrumentos** —y la de CEASN es **más** robusta porque **el buscador no reconoce la sigla**—, 🟢 **mientras la de Open Badges era MITAD FALSA**: la puerta MCP no existe, pero **sí existe la implementación OB 3.0 que esta base declaraba inexistente** (`Schroedinger-Hat/certo`, ⚠️ **AGPL-3.0**, OB 3.0 + W3C VC + DIDs) **y el validador oficial del consorcio** (`1EdTech/digital-credentials-public-validator`, **Apache-2.0** ✅). ✅ **Gap 64 CERRADO en negativo con tres instrumentos: ningún LRS publica puerta MCP propia** (Docker Hub de `yetanalytics` **6 imágenes, ninguna MCP**; `lrsql` **0 menciones**; `ralph-malph` **14 extras, ninguno MCP**) — 🟢 **y el instrumento regaló el sitio del upstream: un `ralph[mcp]` encaja en la convención sin fork** (**P71**). 🟢 **Dos altas por el nombre de la organización, no por término: `yetanalytics/datasim` (Apache-2.0) es la pieza que permite PROBAR un LRS antes de cotizarlo**, y cubre los xAPI Profiles que el pase 25 buscó sin encontrar; 🔴 **y una no-alta declarada, `persephone`, con 10 rutas de licencia en 404 y Docker parado en 2023** (**gap 70**). 🟢 **Gap 63 partido: arquitectura CERRADA por evidencia de archivo** (los tres `config/plugins/*.yaml` en **200**), **fecha RECLASIFICADA** — **8 rutas portadoras de versión, las 8 en 404: el proyecto no se versiona en su árbol**, así que no es el proxy. 🟢 **Y aparece la TERCERA variante de la primitiva anti-bucle, que frena en la CONFIGURACIÓN** (`RATE_LIMIT_PER_MINUTE=30`, `MAX_BODY_SIZE=16384`): **frena solo, cuesta dos variables de entorno, y la lección es que el mecanismo correcto depende de la FORMA DEL DAÑO** —confirmación para el daño irreversible y discreto, techo de caudal para el acumulativo— (tendencia **109**). ✅ **P69 DECIDIDO, y gana la licencia contra el número de adopción: `qtism/qtism` tiene ~10× las descargas (218.212 / 3.104 al mes) pero es GPL-2.0-only en LAS 293 RELEASES**, y `@longsightgroup/qti3-cli` es **MIT, con cero dependencias de terceros y además el más rápido** (41 releases desde 2026-05-21, última modificación **2026-10-01**). 🔴 **Y el hallazgo estructural que obliga a releer todo `intel/`: las primarias multilaterales son inalcanzables POR CLASE — 0 de 11 contra 5 de 5 comerciales.** Toda cifra de mercado y toda fecha regulatoria de esta base se apoya en secundarias comerciales **por construcción del entorno**; el **gap 56 pasa de acción pendiente a límite de clase**, y lo que hay que pedir por fuera vale más que el AI Act: el *working paper* de **UNESCO IESALC** sobre **200 instituciones en 19 países** (tendencia **106**, **gap 65**).
> **Pase 33 del 2026-10-02:** **el hallazgo es de consistencia interna y es incómodo: el gap 60 del pase 32 se contradecía con cuatro archivos de esta propia base.** 🔴 **Mitad xAPI del gap 60 FALSA: `DavidLMS/learnmcp-xapi` (MIT, 3 tools — 1 escribe, 2 leen) es la puerta MCP de xAPI, y estaba acá desde el pase 6**, con la frase *«desde el pase 6»* escrita al lado en el mapa por estándar. ✅ **Mitad QTI CONFIRMADA por un segundo instrumento independiente** — y ésa es la única ausencia de esta KB que cumple el requisito de dos instrumentos (tendencia **101**). 🔴 **La causa está medida, y es el instrumento: `learnmcp-xapi` no está en ningún registro de paquetes** (PyPI **404**, npm **`total: 0`**, se instala desde el código) y **`lrsql` se distribuye por Docker Hub**, así que un barrido que arma su lista de candidatos en npm/PyPI/Packagist **tiene cero probabilidad de verlas** (tendencia **99**). ✅ **Gap 51 CERRADO en negativo y medido en tres registros:** `opencase` devuelve **7 / 404 / 665** resultados con **cero del dominio** —son cajas de skins de videojuego, `opencage` y `opencast`— y `cass` devuelve **26.726** en Packagist (Cassandra, **USPS CASS**); el instrumento que sí funciona es **el nombre de la organización** (tendencia **100**). 🟢 **Las tres piezas de la capa de telemetría quedan FECHADAS: `lrsql` (Apache-2.0) publicó `v0.9.9` el 2026-10-01 —ayer—, 112 tags y seis releases en 2026**; **Ralph (MIT, France Université Numérique) está vivo en `main` y parado en el registro** (último release 2024-07-11 con `[Unreleased]` activo: **se instala desde git, no desde PyPI**); y **`hub.docker.com` entra como canal de verificación nuevo**, que es el sustituto de `api.github.com` —403— para lo que se distribuye como contenedor. ✅ **`coursecode` medido en el artefacto: 15 tools definidas / 15 dispatch, sin aliasing, y DOS escriben** (`_build` con **`enum: ['cmi5','scorm2004','scorm1.2','lti']` en el `inputSchema`** — los cuatro estándares pasan de prosa del README a contrato de tool— y `_narration`, que escribe MP3 llamando a un TTS pago). 🟢 **Y aparece la misma primitiva de seguridad del pase 30 reinventada por otro mecanismo, con una asimetría que hay que cotizar: `openedx-mcp` frena en el servidor (confirm token) y `coursecode` frena en el contrato (anotaciones MCP + `dryRun`) — sólo el primero frena solo** (tendencia **102**). 🟢 **`qti3-cli` (MIT) tiene cero dependencias de terceros en toda su cadena: un wrapper MCP agrega exactamente una** (**P69**). ⚠️ **Gap 56: la acción se ejecutó y el resultado es negativo — `eur-lex.europa.eu` y `data.europa.eu` están BLOQUEADOS por el proxy.** Van **siete fuentes secundarias concordantes y cero primarias**: Anexo III → **2027-12-02**, art. 50 → **2026-08-02** vigente. **No citar como primaria.** ⚠️ **Sin permiso de ejecución en este entorno: instalar dependencias de terceros** — por eso `tools/list` de `coursecode` quedó sin correr (**gap 62**) y toda medición de este pase es lectura de artefacto o de registro, nunca de proceso.
> **Pase 33 del 2026-10-02:** **el hallazgo es de consistencia interna y es incómodo: el gap 60 del pase 32 se contradecía con cuatro archivos de esta propia base.** 🔴 **Mitad xAPI del gap 60 FALSA: `DavidLMS/learnmcp-xapi` (MIT, 3 tools — 1 escribe, 2 leen) es la puerta MCP de xAPI, y estaba acá desde el pase 6**, con la frase *«desde el pase 6»* escrita al lado en el mapa por estándar. ✅ **Mitad QTI CONFIRMADA por un segundo instrumento independiente** — y ésa es la única ausencia de esta KB que cumple el requisito de dos instrumentos (tendencia **109**). 🔴 **La causa está medida, y es el instrumento: `learnmcp-xapi` no está en ningún registro de paquetes** (PyPI **404**, npm **`total: 0`**, se instala desde el código) y **`lrsql` se distribuye por Docker Hub**, así que un barrido que arma su lista de candidatos en npm/PyPI/Packagist **tiene cero probabilidad de verlas** (tendencia **107**). ✅ **Gap 51 CERRADO en negativo y medido en tres registros:** `opencase` devuelve **7 / 404 / 665** resultados con **cero del dominio** —son cajas de skins de videojuego, `opencage` y `opencast`— y `cass` devuelve **26.726** en Packagist (Cassandra, **USPS CASS**); el instrumento que sí funciona es **el nombre de la organización** (tendencia **112**). 🟢 **Las tres piezas de la capa de telemetría quedan FECHADAS: `lrsql` (Apache-2.0) publicó `v0.9.9` el 2026-10-01 —ayer—, 112 tags y seis releases en 2026**; **Ralph (MIT, France Université Numérique) está vivo en `main` y parado en el registro** (último release 2024-07-11 con `[Unreleased]` activo: **se instala desde git, no desde PyPI**); y **`hub.docker.com` entra como canal de verificación nuevo**, que es el sustituto de `api.github.com` —403— para lo que se distribuye como contenedor. ✅ **`coursecode` medido en el artefacto: 15 tools definidas / 15 dispatch, sin aliasing, y DOS escriben** (`_build` con **`enum: ['cmi5','scorm2004','scorm1.2','lti']` en el `inputSchema`** — los cuatro estándares pasan de prosa del README a contrato de tool— y `_narration`, que escribe MP3 llamando a un TTS pago). 🟢 **Y aparece la misma primitiva de seguridad del pase 30 reinventada por otro mecanismo, con una asimetría que hay que cotizar: `openedx-mcp` frena en el servidor (confirm token) y `coursecode` frena en el contrato (anotaciones MCP + `dryRun`) — sólo el primero frena solo** (tendencia **114**). 🟢 **`qti3-cli` (MIT) tiene cero dependencias de terceros en toda su cadena: un wrapper MCP agrega exactamente una** (**P69**). ⚠️ **Gap 56: la acción se ejecutó y el resultado es negativo — `eur-lex.europa.eu` y `data.europa.eu` están BLOQUEADOS por el proxy.** Van **siete fuentes secundarias concordantes y cero primarias**: Anexo III → **2027-12-02**, art. 50 → **2026-08-02** vigente. **No citar como primaria.** ⚠️ **Sin permiso de ejecución en este entorno: instalar dependencias de terceros** — por eso `tools/list` de `coursecode` quedó sin correr (**gap 62**) y toda medición de este pase es lectura de artefacto o de registro, nunca de proceso.
> **Pase 36 del 2026-10-02:** **se ejecutaron las TRES acciones que el pase 35 dejó escritas y las tres rindieron — pero el hallazgo que manda es que el instrumento del pase 35 resultó ser más angosto de lo que se creía, y su sustituto es mejor.** 🔴 **«Descargas por mes» NO es un instrumento general en este entorno: `api.npmjs.org` y `pypistats.org` responden 403 a CONNECT, así que las descargas sólo se miden en Packagist — y las cuatro cifras del pase 35 eran todas de PHP.** 🟢 **El sustituto está en los tres canales y distingue algo que las descargas no: el *span* de releases** (primera → última publicación), que separa **mantenimiento sostenido** de **ráfaga y silencio** — `TinCanPHP` tiene **6.178 descargas/mes y su último release es de 2022-11-02** (⚠️ **corrección a la cifra del pase 35**, que escribió «congelada desde 2019»): las descargas miden **base instalada**, el *span* mide **vida del proyecto** (tendencia **115**). ✅ **Acción 1 cumplida sobre las 49 filas, no seis, y da vuelta las dos puntas que el pase 35 pidió buscar:** 🟢 **`Claw-ED` tiene 60 ★ y 240 releases en PyPI con *backlink* verificado** —la cadencia más alta del archivo con uno de los conteos de estrellas más bajos—, **`canvas-lms-mcp` confirma su promoción por segundo instrumento** (62 releases, MIT **leído en el registro**); 🔴 **y del otro lado `pykt-toolkit` (441 ★) no publica desde 2022-10-16 y `educhain` (389 ★) desde 2025-12-03**, pieza que esta KB viene citando como viva desde el ciclo 2. 🔴 **Y el pase encontró un defecto de la propia KB que ningún pase podía ver con el instrumento que usaba: `Claw-ED` estaba DOS VECES en la tabla** (59 ★ y 60 ★), porque **un conteo de FILAS no puede detectar una fila repetida** — el conteo pasa a **51 filas = 49 repos distintos + 2 entradas de PyPI**, y el control adoptado es **contar *slugs* distintos** (**gap 71**, tendencia **116**). ✅ **Acción 2 cumplida y cierra el gap 70: el manifiesto MCP de `qti3-cli` está ESCRITO** (**P76**) — 🔴 **y corrige tres cosas: 17 comandos y no 14, 20 tools y no 14 (`certification` tiene CUATRO subcomandos), y el `USAGE` del propio CLI documenta sólo 2 de esos 4**, así que un envoltorio generado del texto de ayuda nace con **el 30 % de la superficie afuera** (tendencia **117**). **Hay exactamente 2 rutas de escritura en el paquete entero → 18 de 20 tools son de lectura**, y el contrato de estado adaptativo **sólo admite `outcomes` y `templateValues`: cualquier otra clave es error duro**. 🟢 **Aparece la CUARTA variante de primitiva de seguridad, y extiende el eje de la tendencia 109: las tres anteriores frenan una ACCIÓN del agente, ésta ancla la PROCEDENCIA de un insumo** (`--trusted-report-sha256`, `--require-validator-evidence`) — la única de las cuatro que sirve para firmar un expediente (tendencia **118**). 🔴 **Dos colisiones nuevas, y de clase más peligrosa que las nueve anteriores porque NO hubo búsqueda: el nombre vino del manifiesto del propio repo** — `tero` → `djaodjin/drop` (**colisión 10**) y **`mcp-server`**, genérico y tomado por un tercero (**colisión 11**); **la genericidad del nombre declarado es un predictor evaluable sin red** (tendencia **119**). ✅ **Acción 3 cumplida y la respuesta es negativa donde importa: INEP NO publica API** — Censo Escolar es **ZIP/CSV de 10-20 GB descomprimidos en 4 dimensiones**, y la única API de terceros es **GPL-2.0, sólo IDEB y con el dominio SIN RESOLVER** (caída, no bloqueada). 🔵 **Por eso la mejor oportunidad de LATAM se recotiza: pipeline de ingesta de 8-12 semanas, no fachada de 2-3** (**P77**, tendencias **123** y **122**) — **abierto y consultable no son lo mismo, y la diferencia es un proyecto entero.** 🟢 **Y el método que este pase aporta: `getent hosts` separa «bloqueado» de «inexistente»** — `dados.gov.br` **resuelve** (403 de política), `api.dadosabertosinep.org` **no resuelve** (muerta), con control positivo y negativo en la misma corrida. 🔴 **Del barrido regional, el dato de mayor riesgo comercial, y este pase lo publica junto con el error que estuvo a punto de cometer: el AI Act tiene DOS fechas —2027-12-02 (Anexo III) y 2028-08-02 (Anexo I)— y la lectura intuitiva de que educación cae en la segunda por entregarse «embebida en un LMS» es FALSA.** **Educación está nombrada en el Anexo III**; el **Anexo I son dispositivos médicos, maquinaria y vehículos**, y **un LMS no es un producto regulado**. **El plazo de educación es el 2027-12-02 y la segunda fecha no da prórroga al sector.** 🔵 **La lección es de método y es la que vale: el error tenía el signo peligroso —hacer creer que falta MÁS tiempo— y esos no se descubren solos** (tendencia **121**). Ver las tendencias **115**–**123**, los gaps **71**–**73** y los patrones **P76**–**P77**.
> **Pase 35 del 2026-10-02:** **se ejecutan las tres acciones del pase 32 otra vez y en paralelo a los pases 33 y 34 (ver la nota de concurrencia en la tabla de gaps); dos rinden y la tercera da un resultado estructural.** 🔵 **El hallazgo del pase es un instrumento, no un repo: las descargas por mes del registro.** Treinta y dos pases midieron adopción con estrellas y la tendencia 23 se escribió sin con qué medir lo que escondían; medido, las series **se contradicen en los dos sentidos** —`learninglocker` **583 ★ / 0 descargas-mes** contra `TinCanPHP` **88 ★ / 6.178** y `oat-sa/extension-tao-testqti` **8 ★ / 950 / 844 versiones** (tendencia **107**). 🔴 **Y la inversión llega a la fila que más importa: el conector de LMS más grande de esta KB tiene 8 estrellas** —`bruchris/canvas-lms-mcp`, **MIT, 165 tools con cifra citable, escribe, MCP 1.x**— y desplaza a `vishalsachdev/canvas-mcp` (269 ★, cifra inestable); la capa de conectores pasó de escasa a **saturada: nueve puertas entre Canvas y Moodle, ocho permisivas** (tendencia **112**). ✅ **Acción 2 cumplida CONTRA la expectativa: `coursecode` SÍ es la pieza de salida** — **15 tools** (9 lectura / 6 escritura, 1 destructiva) y **`coursecode_build` toma `format` como enum `cmi5|scorm2004|scorm1.2|lti`**, así que el empaquetado LMS está detrás de MCP; y **`qti3-cli` queda medido: 14 comandos, cero dependencias, todos emiten JSON** (**gap 70**). ✅ **Acción 3 cumplida, y el método del pase 32 funciona a medias con regla que lo explica:** el nombre del implementador desambigua **sólo si el publicador usó el prefijo de organización** (`cassproject`, `@longsightgroup/*`); `OpenCASE` y `cass` **colisionan igual que el estándar** (🔴 **colisiones 7, 8 y 9: OpenCage, Apache Cassandra y —otra vez cripto— Censo Custody en Solana**). 🔴 **Acción 1 NO cumplida y ahora se sabe por qué: `eur-lex.europa.eu` y `data.europa.eu` responden 403 a CONNECT** — el dominio legal europeo completo es inalcanzable desde este entorno (**gap 65**, que el pase 34 planteó como clase y este confirma en el caso europeo), aunque la afirmación sube de fecha a **inciso: Artículo 113**. 🔴 **Gap 68: la puerta oficial de Open edX publicó 12 releases en dos días y nada en 70** (tendencia **109**). 🟢 **Y aparece la pieza que P17 esperaba desde el pase 8: `qti3-a11y` (MIT) entrega matriz de prueba de accesibilidad y guiones VoiceOver/NVDA/JAWS** (tendencia **114**). 🔵 **LATAM deja de estar en silencio con una oportunidad con nombre: Brasil tiene capa MCP nacional de datos públicos y educación es el único dominio grande que falta** (**gap 69**, tendencia **114**). Ver las tendencias **107**–**114** y los patrones **P72**–**P75**.
> **Pase 31 del 2026-10-02:** **se ejecutan las tres acciones del pase 30 más la acción 1 pendiente del pase 29, y las cuatro rinden — la de más valor comercial rinde *contra* la premisa con la que estaba escrita.** 🔴 **Gap 56 RESUELTO, y es la corrección de mayor riesgo comercial descargado de esta KB: las dos fechas del Anexo III son reales y gobiernan obligaciones distintas.** El **2026-08-02** entró en vigor la aplicabilidad general (art. 50 transparencia, art. 4 alfabetización, art. 5 prohibiciones, GPAI, gobernanza y sanciones); el **Anexo III —el inciso que nombra educación— rige desde el 2027-12-02**, diferido 16 meses por el **Reglamento (UE) 2026/1744** (Consejo, 2026-06-29; en vigor 2026-07-27). **El pase 28 confundió una con otra y esta KB le vendió a EMEA una urgencia inexistente: la conformidad del Anexo III NO está vencida, faltan ~14 meses** (tendencia **92**). ✅ **Gap 50 CERRADO leyendo código, invirtiendo la consigna: el `v0` de *authoring* de Open edX está DEPRECADO en favor del `v1`**, con directiva `.. deprecated::` y `DeprecationWarning` emitido en runtime en las cinco operaciones; el comentario que mandaba usar `v0` es de **noviembre de 2023** y encabeza una sección vacía (**confirma al pase 29, corrige al pase 30**; tendencia **88**). 🔵 **Y el bloqueo real estaba una capa más arriba: NINGUNA de las cinco versiones REST (`v0`–`v4`) crea un curso**, y **ninguna de las 19 escrituras del conector oficial tampoco** — tres mediciones independientes, misma conclusión; el bootstrap es curso plantilla + **`course_rerun`** (**gap 57**, **P63**). ✅ **Gap 55 MEDIDO sin Docker, bajando el wheel de PyPI: 35 rutas** (28 LMS + 7 CMS), **19 escrituras en 6 scopes**, **AGPL-3.0 leída del `LICENSE` del artefacto**, y 🔴 **11 escrituras piden *confirm token* y 8 no** — el freno protege contra la operación masiva y **no contra la repetida** (`bulk_enroll` pide token, `unenroll_user` de a uno no; tendencia **93**). ✅ **Gap 54: la consigna del registro de paquetes rinde — aparece una SEGUNDA puerta MCP de OneRoster y es MIT** (`@eduware/oneroster` v1.2.11, ejecutable `mcp` empaquetado; tendencia **89**). 🟢 **Entra OpenBadges 3.0 permisivo** (`@ajna-inc/openbadges`, Apache-2.0) — la pieza que faltaba desde que se midió que CaSS es OB 2.0. ✅ **Gap 42 sigue cerrado pero ahora medido en los dos lenguajes:** `ltijs` v7.0.6 (Apache-2.0, 2026-09-18) tiene **0 menciones de MCP**, y `pylti1p3` **lleva casi cuatro años sin release** (tendencia **90**). 🔵 **Capa nueva que treinta pases no vieron: el *upstream/downstream* de Libraries v2** (`SyncFromUpstreamView`) — editar una vez y propagar a N cursos (tendencia **91**, **gap 59**). ⚠️ **Caliper tiene código de 2026-09-25 y no declara licencia:** no es que no haya código, es que es inusable. ⚠️ **Y una regla de verificación nueva: `github.com`, `www.npmjs.com` y `api.github.com` devuelven 403 en este entorno; `raw.githubusercontent.com`, `registry.npmjs.org` y `pypi.org` responden 200 — así que este pase no publica ni una estrella, y un repo declarado por un paquete real da 404 en las ocho rutas de metadatos probadas** (**gap 58**, tendencia **94**). 🔵 **Y el pase se autocorrigió sobre la marcha: una primera lectura declaró 404 a `pylti1.3` por pedirle `README.md` a un repo Python que publica `README.rst` — el error que la tendencia 87 del pase 30 ya había descrito. Existe, y esta KB lo tenía registrado con 138 ★.**
> **Pase 30 del 2026-10-02:** **se ejecutan las tres acciones del pase 29, las tres rinden, y el hallazgo que manda no salió de ninguna: salió de volver a preguntar por el gap 48.** 🔴 **Open edX ya tiene puerta de agente, es oficial del proyecto y es AGPL-3.0** (`openedx-mcp` + `tutor-contrib-openedxmcp`, PyPI, 2026-07-25; **35 endpoints leídos del código**, autoría incluida). **Eso cierra el gap 48 y rompe la tesis del pase 27:** esta puerta **corre en proceso** como plugin Django, así que *«las LMS son copyleft pero las puertas son MIT»* deja de valer, y la regla que lo reemplaza es que **la licencia de un conector la decide su arquitectura** (tendencias **81** y **82**, **gap 54**). 🔵 **El regalo del hallazgo son los cuatro rails de escritura**, con el modelo de amenaza escrito en el código —*«a looping agent… a retry storm that mass-enrols or deletes»*— y con la primitiva que P53 y P54 venían describiendo en prosa: ***dry run* + confirm token atado a una huella del payload** (tendencia **84**). ✅ **Gap 52 CERRADO leyendo cinco archivos de OpenCASE: 72 rutas, la regla del prefijo, dos endpoints OpenAPI y una capa CGE de federación que nadie había visto.** ✅ **Gap 53 medido ejecutando el servidor: 132 tools, y el «164» era *aliasing*, no supresión** —el 100 % de las operaciones se sirve (tendencia **83**)—, aunque 🔴 **la antigüedad era peor de lo registrado por leer `time.modified` en vez de `time[version]`** (tendencia **86**). ✅ **`.LRN` cerrado: vivo pero GPL-2.0 y en CVS**; **`CK-ERP` muerto desde 2012**. **Dos altas:** `asfai-education` (Apache-2.0, cinco estándares 1EdTech) e `instructure/qti` (MIT, QTI **1.2** legado). ⚠️ **Un falso positivo evitado, y da regla nueva: la capacidad que sólo vive en un *pull request* abierto no está en el producto** (tendencia **85**). 🔴 **Y se declara una contradicción interna de esta KB sobre el calendario del Anexo III: hay dos fechas publicadas en esta base y no son conciliables** (**gap 56**). ⚠️ **Dominios nuevos bloqueados por el proxy: `openacs.org`, `openedx.org` y `codeload.github.com`.**
> **Pase 28 del 2026-10-01:** se ejecutan las acciones 1 y 2 del pase 27 y las dos rinden. **El gap 48 queda
> contestado leyendo el código fuente de Open edX** —no la documentación, que está bloqueada— y **se parte en dos**:
> la API **escribe matrícula, roles y notas, y las notas por lote** (más que el conector MIT de Moodle, que escribe de
> a una), **pero el *authoring* de Studio está declarado experimental por el propio proyecto** (tendencia **74**,
> **gap 50**). 🔴 **Y la regla de búsqueda que el pase 27 dejó escrita resultó insuficiente**: `OneRoster` **sí tenía
> conector** —`trilogy-group/oneroster-ts`, **0BSD**, **164 métodos con escritura**— y **no se llama `*-mcp`**: es un
> **SDK** que declara MCP en una línea del README. **La puerta de agente ya no es un producto, es una *feature* del
> SDK** (tendencia **73**), y eso deja mal medidas todas las ausencias declaradas por etiqueta. **QTI queda medido por
> tres métodos** (ausencia real) y **CASE queda sin medir** por la **cuarta colisión de término** de esta KB
> (**gap 51**). En EMEA **el Annex III dejó de ser una fecha: rige desde el 2026-08-02** y la demanda de conformidad
> está **vencida** (tendencia **75**). Se corrige la regla de estrellas: **los agregadores no inflan, atrasan**
> (tendencia **76**). 🔵 **Hallazgo de método: `raw.githubusercontent.com` responde**, así que se puede leer código sin
> clonar ni instalar — es lo que hizo posible medir Open edX. Ver la nota de método del pase 28.
> **Pase 27 del 2026-10-01:** el eje conector rinde por **tercera vez**, y esta vez lo que devuelve es una
> **corrección del pase anterior**: el **gap 43** afirmaba que el único conector MCP de Moodle era AGPL-3.0 con
> las partes útiles cerradas, y **es falso** — hay **dos MIT**, y uno **escribe notas y devoluciones**
> (`provide_assignment_feedback`), que es la primera pieza permisiva que toca el **gap 6** desde el pase 2
> (tendencias **69** y **70**). El hueco real **se corre a Open edX**, el único LMS grande sin puerta de agente
> (tendencia **71**, gap **48**). La superficie MCP de CaSS queda medida por anotación —**6 expuestas, 55 ocultas,
> 61 operaciones**— lo que **corrige el «45» del pase 26** (era `51 − 6`, y `x-mcp-ignore` se declara por
> operación) y revela que **CASE, CEASN y Open Badges están enteros fuera de MCP** (tendencia **72**). El
> **gap 42 cierra** por agotamiento y se abre el **gap 49**, que es de método: los directorios de MCP rankean por
> promoción. 🔴 **El *handshake* MCP sigue sin hacerse y el bloqueo cambió de naturaleza** — ya no es Docker, es
> que este entorno no permite instalar dependencias de terceros: ver la nota de método del pase 27.
> **Pase 26:** se ejecuta la consigna del pase 25 (**cambiar el eje al conector**) y rinde en su primer uso por segunda
> vez consecutiva: **el gap 40 se cierra ejecutando** —el cartucho MCP de CaSS genera **6 tools y 3 resource templates**
> medidos con el generador del propio proyecto, y dos de ellos (`record_evidence`, `get_learner_profile`) son
> **exactamente los dos pasos que P48 tenía inferidos** (tendencia **66**)—; el **lado *platform* de LTI se cierra por
> medición y la respuesta es que no existe permisivo y productivo**, sobre seis candidatos (tendencia **67**, gap **42**);
> y entran **tres verticales nuevas**: biblioteca/ILS **con opción permisiva y grande** (FOLIO, Apache-2.0), y
> **admisiones** y ***student success*** 🔴 **sin ninguna** — la segunda es de **2013–2014** y es la que el regulador
> aprieta más (tendencia **68**, gaps **45**, **46**, **47**).
> **Pase 25:** se ejecuta **entera** la consigna del pase 24 (cuatro artefactos y tres estándares) y el eje rinde por tercera vez:
> **Caliper dejó de ser open source el 2023-06-17** —repos movidos a privado por 1EdTech— así que de los dos estándares de
> analítica de aprendizaje **sólo xAPI se puede construir** (tendencia **63**); la capa de **proctoring** es la única de esta
> KB **sin ninguna opción permisiva y productiva**, y es justo la que el **Annex III** nombra de alto riesgo (tendencia **64**,
> patrón **P49**, gap **39**); y aparece la **primera pieza de estándar educativo con puerta MCP** —CaSS, Apache-2.0— que
> además hace las **aserciones** de competencia que las cuatro piezas CASE de esta KB no hacían (tendencia **65**, patrón **P48**).
> ⚠️ **Y dos no-hallazgos del pase 24 eran falsos negativos:** `LongsightGroup/qti3` existe (y trae el *item bank* que la
> consigna pedía) y `yetanalytics/xapipe` es el repo de *LRSPipe*. Ver la nota de método del pase 25.
> **Pase 24:** se ejecuta la acción del pase 23 **midiendo en vez de leyendo**, y el resultado **corrige** al pase 23:
> el desglose por tabla de un borrado **ya viaja por el cable** y se descarta, así que el **gap 36** no es refactor de SQL
> sino de la capa que recoge el resultado — pero el conteo único disponible es el del **primer** `DELETE` y vale **`0`**
> para el alumno típico (tendencia **61**). Y aparece el **gap 38**, el primero cuyo síntoma es la ausencia del borrado y
> no de su prueba: en MariaDB/MySQL la supresión **falla entera** (error 1064) si una variable de entorno no relacionada
> apaga `allowMultiQueries` (tendencia **62**, patrón **P47**).
> **Pase 23:** se ejecuta la acción que el pase 22 dejó escrita y **el gap 36 queda dimensionado**: los conteos de borrado existen en los tres backends de `lrsql`, pero **la evidencia no es portable entre motores de base de datos** — y eso contradice la razón por la que esta KB lo recomienda por default (tendencia **60**, patrón **P45**).
> **Pase 12:** la educación pierde **58×** contra la vertical científica en el canal de distribución más barato de la
> industria (tendencia 28), se nombra el patrón *estándar instalado vs. modelo propio* que se repite en cinco capas
> (tendencia 29), se abre el **gap 20** y se registran dos advertencias de verificación: los agregadores de estrellas
> están mal por ~2× y **un 403 de `curl` no es un 404**. Ver la nota de método del pase 12.
> **Pase 11:** el Digital Omnibus es derecho vigente (tendencia 25), aparece la capa predictiva y está vacía (tendencia 26), y se corrige un error de método de diez pasadas sobre licencias permisivas (tendencia 27).

## 1. El giro agéntico ya pasó de generativo a autónomo

El mercado se movió de aplicaciones experimentales de GenAI al despliegue de **workflows agénticos autónomos**: corrección, scheduling y tareas administrativas. La evidencia en el código, no en los informes: los tres repos educativos más grandes de esta ventana son todos agent-native, no chatbots.

- **DeepTutor** (Apache-2.0, 40.6k ★) — 8 superficies integradas, memoria en 3 capas, RAG multi-engine. Releases semanales, v1.6.12 del 2026-09-27.
- **OpenMAIC** (MIT, 39.7k ★) — aula multi-agente, sesiones durables de course-building, skills reutilizables. v1.1.2 del 2026-09-28, y es un **release de seguridad**: la señal de que el proyecto entró en régimen de producción.
- 83% de las instituciones declara planes de desplegar AI teaching assistants en 2026.

## 2. El LMS se volvió host de AI, y eso cambia la economía del proyecto

**Moodle tiene AI subsystem nativo** con provider plugins para OpenAI, Azure OpenAI, Ollama, DeepSeek, Gemini y Amazon Bedrock. Moodle 5.2 salió 2026-04-20 con Gemini + Bedrock y OpenTelemetry.

Consecuencia práctica: **la capa de integración dejó de ser trabajo facturable.** Conectar un LLM a Moodle es configuración. El valor se movió a la pedagogía, el estado del aprendiz, la evaluación y el compliance. Un presupuesto que todavía cotiza "integrar AI al LMS" está cotizando algo que viene incluido.

## 3. Offline-first con AI local es una categoría real

**Project NOMAD** (Apache-2.0) pasó de ~34.4k ★ en julio a **38.8k** ahora: Wikipedia, libros, cursos, mapas y AI local en Docker, sobre hardware propio, sin internet. ~5 GB de disco y <1 GB de RAM sin el módulo AI. **Kolibri** (MIT) sostiene el mismo modelo desde antes.

Esto importa donde la conectividad es el factor limitante — LATAM rural, África, Asia del Sur — y también donde la **residencia de datos** lo es: un tutor que corre sin salir de la red de la escuela resuelve el problema regulatorio europeo de paso.

## 4. Regulación: tres relojes distintos (corregido en el pase 3 — eran dos)

| Región | Estado |
|--------|--------|
| **EMEA** | El Annex III del EU AI Act — que **incluye AI en evaluación** — se corrió de 2026-08-02 a **2027-12-02** (Digital Omnibus on AI). Alto riesgo: corrección automática, aprendizaje adaptativo, proctoring, predicción de deserción. Las escuelas deben auditar |
| **North America** | 134 proyectos de ley en 31 estados en 2026; 24 estados con normas desde 2025; **cero estándares federales vinculantes** a mayo 2026. Ejes: privacidad de datos de alumnos (CA AB 1159), supervisión humana obligatoria (OK, MD), AI en créditos de CS (GA, MS), framework estatal completo (ID SB 1227) |
| **APAC** | **Corea del Sur tiene la ley más avanzada del mundo en vigor para AI educativa** (AI Basic Act, desde 2026-01-22, con educación como *high-impact AI*) — ver la tendencia 10. Vietnam sancionó ley nacional de AI en dic-2025, vigente marzo 2026. China con el marco más restrictivo (tres leyes fundacionales); Japón con segundo AI Basic Plan (14 de julio) y AI Promotion Act deliberadamente flexible; India señaló en julio 2026 posible legislación dedicada |
| **LATAM** | Todo en formación y hacia gobernanza por riesgo. Brasil: PL 2.338/2023 pendiente con penalidades severas; acuerdo de regulación AI con la UE en junio 2026. México: opt-out de decisiones automatizadas en su ley de datos |

**Patrón:** el diferimiento europeo a diciembre de 2027 no relaja nada — define una ventana de 26 meses de trabajo de conformidad que se vende ahora. Y el acuerdo Brasil–UE indica que LATAM converge al modelo europeo, así que el expediente es reutilizable.

**Corrección del pase 3: no son dos relojes, son tres, y el que suena primero es el coreano.** Las pasadas anteriores contrastaron EMEA (regula primero) contra Norteamérica (adopta primero) y trataron APAC como un mosaico sin fecha. Es incorrecto: **Corea del Sur tiene obligaciones sustantivas exigibles sobre AI educativa desde el 2026-01-22**, mientras el Annex III europeo recién aplica el 2027-12-02. El régimen vinculante más exigente para un tutor o un sistema de evaluación hoy no está en Bruselas: está en Seúl. Ver la tendencia 10.

## 5. AI literacy se está volviendo currículo obligatorio

La Comisión Europea, con la OCDE y aval del G7, publicó un borrador de **AI Literacy Framework** para primaria y secundaria. En EE. UU., Georgia y Mississippi ya embuten AI en créditos de computer science; Idaho exige estándares de AI literacy y formación docente por ley.

Del lado del material, hay recursos Apache-2.0 listos: **LLMs-from-scratch** (105.8k ★) y **minimind** (63k ★, entrena un LLM de 64M en ~2h en hardware de consumo). El cuello de botella es el currículo y la formación docente, no el contenido técnico.

## 6. La pedagogía se está empaquetando como skills de agente

**education-agent-skills** (814 ★) publica 165 skills pedagógicas evidence-grounded en 20 dominios, consumibles por Claude Code, Claude.ai vía MCP, Codex y Hermes. Y **tutor-mcp** (MIT, Go) expone ciencia cognitiva como servidor MCP: estado durable del aprendiz, scheduling de repaso, misconceptions, metacognición, decisiones pedagógicas **auditables**.

Es un cambio de forma: la pedagogía deja de vivir en el prompt y pasa a ser una interfaz versionada y auditable. Lo cual es exactamente lo que pide el EU AI Act.

⚠️ `education-agent-skills` es **CC BY-SA 4.0** — contenido con share-alike, no código permisivo. Revisar con legal antes de empaquetarlo en un entregable cerrado.

## 7. El colapso de los negocios educativos basados en SEO

Chegg, Course Hero, Quizlet y Study.com — que dominaron el ranking de Google en consultas educativas por una década — quedaron **fuera del top 15** del AI Visibility Index 2026, con colapsos de tráfico documentados y atribuidos a AI Overviews. Los que crecieron tienen relación institucional (Khanmigo: 68k → 1.4M usuarios, 45 → 380+ distritos) o loop de producto (Duolingo: >$1B revenue, 47.7M DAU).

Lección para el pitch: en educación, el foso es la **integración institucional y el dato de progreso del alumno**, no el contenido ni el tráfico.

## 8. El mandato de política escrita choca con un 82% de incumplimiento (agregado 2026-09-30, pase 2)

El hallazgo más accionable de esta pasada sale de cruzar dos datos que circulan por separado:

- **Oklahoma S.B. 1734** obliga a **cada distrito** a tener una política de AI **escrita** antes del ciclo escolar **2027-28**. Maryland (S.B. 720) exige política distrital alineada más un **AI coordinator** designado; Idaho (S.B. 1227) exige framework estatal completo.
- **Sólo 18% de los docentes de EE. UU. reporta tener alguna política escrita** sobre uso de AI (marzo 2026).

Un mandato con fecha contra **82% de incumplimiento**, en un país donde además hay **77 proyectos de ley sobre AI en instrucción de aula en 27 estados** en 2026. La demanda no hay que crearla: está legislada.

**Lo que esto cambia en la forma de vender.** El entregable no es un tutor. Es un **policy pack**: política escrita defendible, formación docente, y — la parte que sólo un studio puede hacer — los **gates de human-in-the-loop efectivamente configurados en el LMS** con evidencia de auditoría. Oklahoma prohíbe explícitamente que la AI sea base primaria de calificación, disciplina o placement: eso es una restricción de *arquitectura*, no un párrafo de un documento. Quien entrega el documento sin el gate técnico no cumple, y no puede demostrar que cumple.

Es además el trabajo más replicable de la KB: mismo pack, distrito por distrito, con variación por estado. Ver **P7** en `compose/patterns.md`.

## 9. La pedagogía se distribuye como skill, y el harness se vuelve el producto (agregado 2026-09-30, pase 2)

La tendencia 6 (pedagogía empaquetada como skills) se confirmó con un segundo caso independiente y más fuerte: **Bloom** (MIT, 278 ★) se distribuye como **skill de Claude Code sin backend**, además de como app web self-hosted.

El patrón importa por economía, no por novedad técnica: si la tutoría viaja como skill, el costo de un piloto baja de "desplegar y operar una plataforma" a "instalar una skill". Para un studio eso cambia el punto de entrada de un engagement — se puede demostrar valor pedagógico antes de discutir infraestructura. La contracara es que el diferenciador se corre: si el harness es commodity, lo defendible es la pedagogía y los datos del aprendiz, no el código del agente.

## 10. Corea del Sur ya tiene en vigor el régimen que Europa todavía no aplica (agregado 2026-09-30, pase 3)

El hallazgo regulatorio más importante de esta pasada, y el punto ciego más grande que tenía la KB. Las pasadas anteriores describían APAC como regulación heterogénea y decían de Corea sólo que tiene "protección de datos estricta". Es mucho más que eso.

**La AI Basic Act coreana** (*Act on the Development of Artificial Intelligence and Establishment of Trust*) **está en vigor desde el 2026-01-22.** Corea es la **segunda jurisdicción del mundo después de la UE** con una ley horizontal e integral de AI, y **la primera de APAC**.

**Lo que la vuelve directamente relevante para educación:** la ley crea una categoría de **"high-impact AI"** y **la educación está explícitamente dentro** — junto con salud, empleo, servicios financieros y seguridad pública. Las tres obligaciones cabeza de un operador de high-impact AI son:

1. **Explicación con sentido** de los resultados del sistema a las personas afectadas.
2. **Plan de protección del usuario**, creado y desplegado.
3. **Mecanismo de intervención y supervisión humana** sobre las decisiones del sistema.

Hay un **período de gracia de un año sobre las multas administrativas** (hasta ~2027-01-22, con excepciones para casos de daño social grave), pero **las obligaciones sustantivas de cumplimiento aplican desde el 2026-01-22**. Gracia sobre la sanción no es gracia sobre el deber.

**Por qué esto cambia el orden de prioridades.** La KB venía vendiendo el EU AI Act como el reloj que importa, con Annex III el 2027-12-02. Comparado con Corea:

| | Corea del Sur | Unión Europea |
|---|---|---|
| Obligaciones sustantivas sobre AI educativa | **ya exigibles (2026-01-22)** | 2027-12-02 (Annex III) |
| Educación como categoría de alto riesgo/impacto | sí, explícita | sí (evaluación, aprendizaje adaptativo, proctoring) |
| Sanciones | multas en gracia hasta ~2027-01-22 | régimen ya operativo desde 2026-08-02 para el resto |

**Consecuencias prácticas:**

1. **El trabajo de conformidad coreano es ahora, no en 2027.** Cualquier institución o edtech que opere en Corea con tutoría, evaluación adaptativa u orientación ya está bajo obligación.
2. **Las tres obligaciones coreanas son casi exactamente el diseño del patrón P4 y del P7** — explicabilidad, plan de protección, gate de intervención humana. El expediente que la KB ya sabe construir para EU AI Act **se reusa en Corea con adaptación, no con rediseño.** Eso amplía la tesis de "vender el expediente una vez y cobrarlo varias" de LATAM a APAC.
3. **Corea deja de ser sólo mercado de demanda y pasa a ser el mercado donde la conformidad se exige primero.** Para un studio con presencia global es el mejor lugar para producir la primera referencia auditada y después portarla a EMEA, que la va a pedir en 2027.
4. **Vietnam refuerza el patrón:** ley nacional de AI sancionada en diciembre de 2025 y vigente desde marzo de 2026. APAC dejó de ser "soft law".

**Contrapunto de sentimiento público que conviene tener a mano:** el Ipsos Education Monitor 2026 encuentra **menor apoyo a prohibir la AI en las escuelas en los mercados asiáticos**, mientras **Australia y Nueva Zelanda registran apoyo más alto a prohibirla**. O sea: dentro de APAC, la resistencia social está en ANZ y la apertura en Asia, lo cual no coincide con dónde está la regulación más dura. Vale para ajustar el discurso por país, no sólo por región.

## 11. El Digital Omnibus no pospuso el AI Act: pospuso la mitad cara y dejó corriendo la mitad barata (agregado 2026-09-30, pase 4)

El **Digital Omnibus on AI entró en vigor el 2026-07-27** y corrió las obligaciones de alto riesgo del **Annex III — que incluye educación** — de 2026-08-02 a **2027-12-02**, y las del Annex I a 2028-08-02. El titular que circuló es "el AI Act se retrasó".

**Lo que no se movió, y es lo que tiene fecha cercana:**

- El **Artículo 50** (transparencia y divulgación de que hay AI) **está en vigor desde el 2026-08-02**, sin cambios.
- El **deadline de watermarking del 2026-12-02** tampoco se movió. Faltan **dos meses**.

El efecto práctico es una inversión de prioridades que la mayoría de los clientes europeos todavía no hizo: creen que tienen hasta 2027 y tienen una obligación activa hoy y un vencimiento en diciembre. **Lo que exigía ingeniería pesada — gestión de riesgo, gobernanza de datos, evaluación de conformidad para corrección automática, aprendizaje adaptativo, proctoring y predicción de deserción — se corrió 16 meses. Lo que exige decirle al usuario que está hablando con una AI y etiquetar lo que la AI generó, no.**

Para un studio esto es la mejor forma de entrada que hay en EMEA ahora mismo: alcance chico, urgencia real, fecha verificable, y deja instalado el expediente técnico que en 2027-12-02 va a hacer falta completo. Ver P4 en `compose/patterns.md`.

**Consecuencia de segundo orden, que importa más a mediano plazo:** los 16 meses de gracia europeos llegan justo cuando **APAC pone tres regímenes en vigor** (Corea del Sur enero 2026, **Taiwán 2026-01-14**, y **Vietnam con evaluación automatizada y monitoreo de comportamiento tipificados como alto riesgo**). La secuencia se dio vuelta respecto de lo que esta KB asumía en los pases 1 y 2: **la conformidad exigible hoy está en Asia, no en Europa.** Quien construya el expediente en un despliegue coreano o taiwanés llega a diciembre de 2027 con el trabajo hecho y reutilizable.

> 🔴 **CORREGIDO EN EL PASE 14 DEL 2026-10-01 — Taiwán no cuenta, y este párrafo lo contaba.** La afirmación de arriba
> lista **tres** regímenes «en vigor» y recomienda construir el expediente «en un despliegue coreano **o taiwanés**».
> **Para Taiwán es incorrecto, y la fecha 2026-01-14 —que es correcta— lo hace parecer exigible.** Verificado: la
> *AI Basic Act* taiwanesa fue aprobada por el Yuan Legislativo el **2025-12-23** y promulgada el **2026-01-14**, pero
> **(a)** son **20 artículos de ley marco sin ninguna disposición sancionatoria**; **(b)** el artículo 5 exige etiquetar
> las aplicaciones de alto riesgo pero **ningún artículo define «alto riesgo»**: la tarea está delegada al **MODA** por
> el artículo 16 y **el marco de clasificación de riesgo todavía no existe** (MODA apuntaba a Q1 2026); **(c)** lo único
> específico de educación es la consideración del interés superior de niños y adolescentes.
>
> **Consecuencia operativa, y es la inversa de lo que el párrafo recomienda:** un despliegue taiwanés **no** produce hoy
> expediente de conformidad reutilizable, porque **no hay contra qué conformar**. **Corea del Sur y Vietnam sí** —el
> coreano con alcance extraterritorial, evaluación de riesgo, supervisión humana y documentación desde enero de 2026;
> el vietnamita con **evaluación automatizada y monitoreo de comportamiento tipificados como alto riesgo**, en vigor
> desde marzo de 2026—. **Los regímenes exigibles de APAC son dos, no tres. Taiwán se sigue, no se vende.**

> **Actualizado en el pase 11 del 2026-10-01 — identificadores citables.** El instrumento es el **Reglamento (UE) 2026/1744**: propuesto por la Comisión el **2025-11-19**, aprobado por el Parlamento Europeo el **2026-06-16**, adoptado por el Consejo el **2026-06-29**, **en vigor el 2026-07-27**. Modifica, entre otros, los artículos **9, 17, 18, 28, 43 y 50** del Reglamento (UE) 2024/1689. La fecha del Anexo III *stand-alone* es **2027-12-02** y la del alto riesgo embebido en productos regulados, **2028-08-02**. Ver la tendencia **25** para la tabla completa y el nivel de evidencia.

## 12. La seguridad pedagógica se volvió medible, y la métrica que importa no es la exactitud (agregado 2026-09-30, pase 5)

**Lo que cambió.** Hasta 2026 evaluar un tutor LLM significaba medir si acertaba. En esta ventana aparece una categoría entera —con cuatro publicaciones en venues top y datasets liberados— que mide algo distinto: **si el tutor enseña mal siendo amable**.

El riesgo no es la toxicidad. Es revelar la respuesta antes de tiempo, reforzar la idea equivocada del alumno porque el alumno insistió, y abandonar el andamiaje cuando el alumno se frustra. Un modelo puede tener 95% de exactitud y ser un desastre pedagógico, y hasta ahora no había forma de demostrarlo con un número.

**Los artefactos:** `SafeTutors` (MIT, EMNLP 2026 — 11 dimensiones de daño, 48 sub-riesgos, 5.955 instancias), `EduGuardBench` (⚠️ sin licencia — daño docente + prompts adversarios sobre mala conducta académica, 14 modelos), `EduBench` (MIT, ACL 2026 — 9 contextos, transversal a materia), y dos benchmarks descritos en papers sin repo: `EduFrameTrap` (TUM/MCML — sycophancy bajo presión de autoridad y social, 6 materias) y `ELBench`.

**Los tres hallazgos que cambian decisiones de arquitectura:**

1. **La seguridad está anti-correlacionada con la enseñanza práctica** (ELBench, 9 modelos). Los modelos más seguros enseñan peor. Si se sostiene, **no existe el modelo que resuelva las dos cosas y hay que componer**: modelo docente + gate de seguridad medido aparte. Es la respuesta técnica a "¿por qué no usamos el modelo más grande?".
2. **El modo de falla dominante es la incompetencia, no la toxicidad** (EduGuardBench, 14 modelos). El riesgo real en educación es pedagógico, no reputacional — y eso reordena qué se audita.
3. **La *Reasoning-Sycophancy Paradox*** (EduFrameTrap): un modelo que resiste un ataque de cambio de marco igual capitula ante presión de autoridad ("mis apuntes dicen que tengo razón") o de salvar la cara ("por favor no me digas que me equivoqué"). La capacidad de razonar **no protege** contra la adulación social.

**Por qué es una tendencia y no un detalle académico.** Es el primer artefacto de la ola de evaluación educativa que un comprador regulado reconoce inmediatamente como su problema. En un sistema de Annex III del EU AI Act, una taxonomía de 11 dimensiones de daño derivada de ciencias del aprendizaje **no es una métrica de calidad: es la estructura del análisis de riesgos**. Y por primera vez el stack completo de evaluación es MIT (`EduBench`, `SafeTutors`, `pyBKT`, `rubric`), así que se puede usar en un entregable cerrado sin pasar por legal — lo que no pasaba con los artefactos del pase 4, dos de ellos Creative Commons con share-alike.

**El contraste que hay que tener presente al venderlo:** los benchmarks pedagógicos premiados en EMNLP y NAACL tienen 42 y 32 estrellas. La academia produjo el estándar y la industria no lo adoptó (ver gap 1). Eso es exactamente la oportunidad: **integrar y operacionalizar lo que ya existe**, que es un proyecto de semanas.

## 13. El modelo educativo chico y especializado empieza a discutirle al genérico grande (agregado 2026-09-30, pase 5)

`OmniEdu` (Universidad de Pekín + UCAS + Zhongguancun Academy, septiembre 2026) publica una familia de modelos fundacionales para K-12 en **4B, 9B y 27B**, con el corpus de instrucciones abierto (69.999 ejemplos, 15,96M tokens supervisados de 100+ fuentes) organizado en cuatro capacidades: competencia en la materia, anclaje curricular, razonamiento diagnóstico y acción pedagógica/andamiaje.

El número que importa: según el paper, **OmniEdu-27B alcanza 78,74% en el setting Scaffold de MathTutorBench**. Un modelo de 27B especializado compitiendo en tareas pedagógicas con genéricos mucho más grandes.

**Por qué es una tendencia con consecuencia comercial directa.** En un despliegue a escala de sistema educativo —un ministerio, un estado, una red de distritos— la variable que decide no es la calidad marginal sino el **costo por alumno de inferencia**. Un modelo de 4B–27B que se puede correr on-premise cambia el orden de magnitud de esa cuenta, y además resuelve de paso los dos problemas que la KB ya tiene documentados: **soberanía de datos** (APAC y EMEA) y **operación con conectividad pobre** (LATAM rural, África).

⚠️ **Y el artefacto concreto no es usable:** `haolpku/Omni-Edu` **no declara licencia** y sus pesos heredan la licencia de las bases Qwen. La tendencia es real y el repo no es un componente. Lo aprovechable es **la receta** —el corpus y las cuatro capacidades están descritos— para entrenar un modelo propio con currículo del cliente. Esa es la propuesta, no "desplegamos OmniEdu".

## 14. El agente educativo tiene un estándar de memoria desde hace una década y casi nadie lo usa (agregado 2026-10-01, pase 6)

Cada tutor LLM open source que esta KB registró en seis pasadas guarda el progreso del alumno en un esquema inventado por su autor. DeepTutor tiene memoria en tres capas propia. OpenTutor tiene la suya. Los cinco servidores MCP de mastery del pase 5 tienen cinco. Ninguno escribe en **xAPI**, que es un estándar **IEEE (9274.1.1)** con cuatro implementaciones open source maduras y quince años de despliegue en formación corporativa y militar.

La consecuencia no es estética. Un tutor con memoria propietaria:

- no puede entregarle el historial al LMS ni al SIS sin un ETL a medida,
- no deja evidencia auditable en el formato que un regulador o un auditor ya conoce,
- y obliga a rehacer la capa de datos en cada engagement.

**Dónde está el borde del cambio:** `learnmcp-xapi` (MIT, 15 ★) es el primer artefacto que le da a un agente tools MCP sobre un LRS conforme en vez de una tabla propia. Es chico —32 commits— pero marca la dirección correcta.

**Por qué es una tendencia y no una curiosidad técnica:** las tres presiones regulatorias que esta KB viene siguiendo —EU AI Act, mandatos distritales de EE. UU. con supervisión humana obligatoria, y ahora Vietnam clasificando la evaluación automatizada como alto riesgo— **piden exactamente lo que un LRS produce**: registro inmutable de qué decidió el sistema, cuándo y con qué evidencia. La adopción de xAPI en tutoría con AI va a venir empujada por cumplimiento, no por elegancia de arquitectura.

**Qué hacer con esto en una propuesta:** proponer el LRS como **capa 0**, antes del agente. Es barato (`lrsql`, Apache-2.0, corre sobre el Postgres que el cliente ya tiene), es estándar, y convierte "confíe en nuestro tutor" en "acá está el registro". Ver **P15**.

## 15. El submercado de tutores crece más lento que el mercado que lo contiene (agregado 2026-10-01, pase 6)

Dato del pase 6: **AI tutors es USD 2,7 B en 2026 y proyecta USD 17,7 B a 2033, CAGR 30,5%.** El agregado de AI en educación crece a ~35%. El producto más visible de la categoría es **el que crece por debajo del promedio de su propia categoría**.

Eso significa que el crecimiento está en las capas que no son el tutor: administración, analítica, evaluación, cumplimiento y telemetría. Y es justo donde esta KB viene documentando huecos de oferta open source pasada tras pasada — grading (gaps 6 y 9), SIS permisivo (gap 7, parcialmente resuelto), evaluación pedagógica adoptada en producción (gap 1), y ahora el estimador de mastery sobre LRS (gap 5).

**La conclusión de posicionamiento, y contradice el instinto:** entrar por el tutor es competir en el segmento más disputado (MagicSchool, Khanmigo, Duolingo, más los tutores chinos de 40k ★) y de menor crecimiento relativo. **Entrar por la capa que registra, mide y acredita es competir donde el mercado crece más rápido y la competencia open source es más débil o inexistente.** Todos los patrones de esta KB que venden esa capa —P4, P7, P10, P11, P14 y el nuevo P15— están mejor apuntados que P1.

## 16. La librería es MIT y los datos no: el cuello de botella del tutor adaptativo se movió de capa (agregado 2026-10-01, pase 7)

Las pasadas 4 a 6 construyeron un argumento coherente: `pyKT` es MIT, `pyBKT` es MIT, `lrsql` es Apache-2.0, `learnmcp-xapi` es MIT — por lo tanto el tutor adaptativo es **integración de piezas permisivas**, no investigación. El argumento es correcto sobre el código y estaba incompleto, porque **un modelo de knowledge tracing no se instala: se entrena.**

De los tres datasets de knowledge tracing que importan (ver `repos/foundations.md`):

- **EdNet** (131,4M interacciones, 784k alumnos, Corea) → **CC BY-NC 4.0**.
- **FoundationalASSIST** (1,7M interacciones, el único en inglés con respuestas reales y distractores, EE. UU.) → **CC BY-NC 4.0** *y* con acceso condicionado.
- **XES3G5M** (5,5M interacciones, China) → **MIT**, y es chino, de matemática y de tercer grado.

**O sea: el único dataset grande que se puede usar en un entregable facturado es también el menos aplicable.** La capa que parecía resuelta —modelado— lo está en código y no en datos.

**Lo que esto cambia en la práctica, y es una buena noticia disfrazada de problema.** Si no hay dataset público reutilizable, el modelo se entrena con los datos del cliente. Y entonces **el Learning Record Store deja de ser una pieza de conformidad y pasa a ser la pieza que hace posible el producto**: es lo que genera el histórico. El pase 6 vendía el LRS como expediente auditable ante un regulador; el pase 7 le agrega un argumento comercial que no depende de ninguna regulación. **El LRS va en la fase 1 porque sin él el arranque en frío no termina nunca.** Ver **P16**.

**Y la lección de método, que es transversal a esta KB:** verificar la licencia del repo dejó de ser suficiente. Hay que verificar la licencia de **los datos con que ese repo se vuelve útil**. Es una capa que ninguna de las seis pasadas anteriores había mirado.

## 17. La ola regulatoria de APAC dejó de ser Corea del Sur sola (consolidado 2026-10-01, pase 7 — el hallazgo es del pase 6)

⚠️ **Nota de atribución, porque importa para no contar dos veces el mismo hallazgo:** este trend **no es un descubrimiento del pase 7**. Las tres jurisdicciones ya estaban registradas en `intel/market.md` por el **pase 6**. El pase 7 las encontró de forma independiente en búsqueda regional, confirmó las fechas, y las trae acá por una razón de estructura: **`intel/trends.md` seguía teniendo sólo el trend 10 ("Corea del Sur ya tiene en vigor el régimen que Europa todavía no aplica"), que presenta a Corea como excepción cuando ya es regla.** Lo que sigue corrige esa formulación.

| Jurisdicción | Instrumento | Vigencia | Qué dice sobre educación |
|---|---|---|---|
| **Corea del Sur** | AI Basic Act | **2026-01-22** | Marco integral (trend 10) |
| **Taiwán** | Basic Law on Artificial Intelligence | **2026-01-14** | Ley marco vigente, no borrador |
| **Vietnam** | Ley nacional de AI, sancionada **dic. 2025** | **marzo 2026** | **Alto riesgo en seis sectores, uno es educación** — nombra explícitamente **evaluación automatizada** y **monitoreo de comportamiento** |

**El trend 10 queda corregido en su encuadre:** Corea no es el país que se adelantó, es el primero de tres. Y mientras eso pasaba, **Europa corrió el Annex III a 2027-12-02** (trend 11). La consecuencia es contraintuitiva y conviene decirla sin rodeos: **a fines de 2026, la obligación de conformidad para un tutor agéntico es exigible antes en APAC que en la UE.**

**Por qué Vietnam es el caso que más pesa de los tres.** Nombra *evaluación automatizada* y *monitoreo de comportamiento*, que son las dos funciones que un tutor agéntico implementa sin proponérselo: calificar y observar al alumno para adaptarse. No es una categoría de riesgo que se pueda esquivar con una decisión de diseño; es la descripción del producto.

**La contradicción que es la oportunidad, ya medida en `intel/market.md`:** tres leyes vigentes, y **sólo el 10%** de las instituciones de un relevamiento de 450+ en APAC tiene lineamientos formales, con **93%** de los educadores diciendo que hacen falta regulaciones. Obligación legal arriba, capacidad de cumplirla ausente abajo.

**Para el patrón P5** eso significa que la orquestación multi-jurisdicción deja de ser un patrón para grupos regionales multinacionales y pasa a ser **el patrón por defecto de cualquier despliegue APAC serio**: el mismo tutor tiene que demostrar conformidad bajo tres regímenes con calendarios distintos, ante un comprador con menos capacidad instalada que su par europeo para producir ese expediente solo.

## 18. La accesibilidad dejó de ser una característica y pasó a ser condición de acceso al mercado (agregado 2026-10-01, pase 8)

Las seis obligaciones regulatorias que esta KB viene siguiendo —EU AI Act, Corea, Vietnam, los mandatos estatales de EE. UU., el Digital Omnibus, el Decreto 83 chileno— tienen algo en común: **regulan cómo se usa la AI**. El **European Accessibility Act** es de otra clase y la KB no lo tenía: no regula la AI, **regula la plataforma**, y alcanza a cualquiera que ofrezca e-learning o un LMS en la UE.

Lo que lo hace distinto de todo lo demás de esta lista:

- **La fecha ya pasó.** En vigor desde el **2025-06-28**. No hay período de gracia que esperar, a diferencia del Annex III del AI Act.
- **Es binaria, no graduada.** Referencia técnica **WCAG 2.1 AA**. Se cumple o no se cumple; no hay «enfoque basado en riesgo» que module la obligación.
- **Alcanza por mercado, no por domicilio.** Una empresa fuera de la UE que sirva usuarios de la UE está adentro — el mismo mecanismo extraterritorial del GDPR.
- **El presupuesto ya existe.** Vive en cumplimiento y en compras, no en innovación. Es la diferencia práctica con la evaluación pedagógica, que hay que explicar antes de venderla.

**Y la oferta open source que lo resuelve no es educativa**, que es por qué siete pasadas de esta KB no la encontraron. `accessibility-agents` (**MIT, 419 ★, 374 commits**) revisa WCAG 2.2 AA desde adentro de Claude Code, GitHub Copilot, Codex y Gemini CLI, sobre código y sobre documentos — PDF y ePub incluidos, que es donde vive el material didáctico. Tiene más tracción que cualquier pieza de educación especial registrada en el pase 8 y que casi toda la capa de evaluación pedagógica.

**La lectura de negocio, y es contraintuitiva respecto del resto de la KB.** Los diecisiete trends anteriores empujan hacia el tutor, el modelado y la medición — territorio disputado, con incumbentes de 40k ★ en APAC. Este empuja hacia un trabajo que **no tiene incumbente open source, no tiene que desplazar a nadie, tiene obligación legal vigente y partida presupuestaria asignada**. Es el trabajo menos glamoroso y el de ciclo de venta más corto. Ver el patrón **P17**.

⚠️ **Lo que no hay que confundir, y es la mitad del trend.** WCAG mide **acceso técnico**: que el lector de pantalla llegue, que el contraste alcance, que el teclado navegue. **No mide si el contenido es comprensible para un alumno con discapacidad cognitiva.** Esa segunda mitad no tiene oferta open source — es el **gap 12** — y es la que un cliente de educación especial realmente pide. Venderlas juntas es prometer de más; venderlas en ese orden es un camino.

## 19. Los estándares de interoperabilidad educativa siguen siendo obligatorios y su código de referencia se está retirando (agregado 2026-10-01, pase 9)

Es el trend más incómodo de esta KB porque va en contra de la dirección que llevan los dieciocho anteriores. En todas las
capas anteriores la historia era *aparece oferta open source nueva*. Acá la historia es **se retira oferta open source que
existía**, y los estándares que esa oferta implementaba siguen siendo condición de compra institucional.

Verificado URL por URL el 2026-10-01:

| Qué era | URL que la documentación del sector sigue citando | Estado |
|---|---|---|
| **Badgr**, la implementación de referencia de Open Badges | `concentricsky/badgr-server` | **404**, y la búsqueda de repos de la organización por `badgr` devuelve *«No repositories matched your search»*. La organización verifica hoy el dominio **`instructure.com`**: Badgr → **Canvas Credentials** → **Parchment Digital Badges** |
| **caliper-php**, cliente oficial de Caliper Analytics | `1EdTech/caliper-php` | **404.** Causa nombrada por el fork de la **Universidad de Michigan**, textual: *«This had been archived, but has been unarchived following 1EdTech making its caliper-php private.»* |
| **caliper-python**, Sensor API de referencia | `IMSGlobal/caliper-python` | **404** |
| **European Digital Credentials** (Issuer/Viewer/Wallet) y **European Learning Model** | `european-commission-empl/*` | **Archivados** (2024-02-02 y 2024-02-14, EUPL-1.2), con aviso de mudanza a `code.europa.eu` — fuera de GitHub |

**El rigor que corresponde:** un 404 no distingue borrado de renombrado de privado. Lo afirmado es que **las URL no
resuelven**, con una señal independiente en `badgr-server` y la causa nombrada por un tercero en `caliper-php`.

**Lo que esto significa, y es lo vendible.** La obligación de interoperar no se fue con el código. El cliente que compra
credenciales digitales o analítica de aprendizaje conforme sigue necesitando **OB 3.0, QTI, OneRoster y Caliper**. Lo que
cambió es de dónde sale la implementación: ya no del organismo de estándares ni del vendor de referencia, sino de
**terceros certificados** (`amp-up-io/qti3-item-player`, MIT, con certificación de conformidad de 1EdTech),
**consorcios universitarios** (`digitalcredentials/*`, MIT) y **forks de universidad** (`caliper-php-public`, LGPL-3.0).

**El corolario de método, que vale para cualquier propuesta de esta capa:** acá **la señal de calidad no son las
estrellas**. El repo más estrellado de la capa (205 ★) es **una especificación, no código**; el de más commits (22.533)
es **GPL-2.0**; el único con **certificación de conformidad** tiene **30 ★**; y el emisor OB 3.0 más completo tiene
**404 commits y 1 estrella**. Se elige por conformidad y por licencia leída en el archivo. Ver **P21**.

## 20. La credencial es la vía por la que la formación profesional entra por fin a esta KB (agregado 2026-10-01, pase 9)

El **gap 10** lleva tres pasadas diciendo que la formación profesional no tiene *nada* open source con tracción: ni
plataforma, ni agente, ni benchmark. Cero de tres. Eso sigue siendo cierto **si se busca «plataforma de FP»**.

Buscando por el instrumento que la FP realmente usa —la **microcredencial**— el segmento no está vacío: tiene estándar
(**Open Badges 3.0 / W3C VC**), tiene vocabulario de competencias (**ESCO/ISCO**), tiene implementaciones **MIT** de
emisión, verificación y billetera, y tiene demanda medida. **46% de las instituciones de LATAM y el Caribe ya ofrecen
microcredenciales.** Y los tres obstáculos declarados del segmento son **estandarización (82%)**, **preparación
institucional (76%)** y **reconocimiento formal (71%)** — los tres se atacan con conformidad al estándar.

**Política pública que lo empuja, por región.** En **APAC**: Filipinas tiene microcredenciales en TVET vía **TESDA** y un
marco de la **CHED** en consulta pública; el consorcio **MICROCASA** articula España, Italia, Indonesia, Malasia y
Filipinas. En **EMEA**: el stack de credenciales es política europea (Europass/EBSI) y hay un **Micro-credentials
Masterclass** (Ámsterdam, 24–26 de febrero de 2026) con reguladores y proveedores de FP; **AI4VET**, Erasmus+ KA210-VET
2026, publica un curso de upskilling docente abierto probado en Portugal y Rumania. La **OCDE** publicó un informe sobre
desarrollar FP con AI, de mapeo de competencias a redacción asistida de currículo.

**Cómo reformula el gap 10 sin cerrarlo.** El gap era «no hay oferta». La formulación correcta es: **la oferta existe en
la capa de acreditación y no en la capa de aprendizaje**. Para un cliente de FP, el producto defendible hoy no es un
tutor de oficios —eso sigue sin existir— sino **acreditar de forma verificable y reconocible lo que el cliente ya
enseña**. Es un alcance más chico, más barato y mucho más vendible. Ver **P19**.

## 21. El fin del período gratuito de AI del incumbente abre una ventana de compra, y se cerró ayer (agregado 2026-10-01, pase 9)

🔴 **No verificado de primera mano — leer la advertencia antes de usarlo con un cliente.**

Según resultados de búsqueda concordantes, **Instructure** lanzó **IgniteAI Agent** para Canvas el **2026-03-15**,
construido sobre **Amazon Bedrock**: arma módulos, diseña páginas, genera rúbricas, revisa discusiones y organiza flujos
de trabajo docentes y administrativos. Y reestructuró Canvas en tres niveles —**Canvas Core, Canvas Plus y Canvas
Next**— donde las capacidades agénticas avanzadas viven en los dos de arriba.

**El dato con fecha:** el acceso gratuito a las funciones avanzadas (IgniteAI Grading Assistance y IgniteAI Agent)
terminó el **2026-06-30 en EE. UU.** y el **2026-09-30 en el resto del mundo**. Después hace falta subir a Canvas Plus o
Canvas Next.

**Hoy es el 2026-10-01.** Si el dato es correcto, la ventana se cerró **ayer** a nivel mundial, y hay una población de
instituciones que acaba de descubrir que la AI que venía usando sin costo ahora es una línea de presupuesto. Eso es un
momento de conversación —no un argumento de reemplazo del LMS, que nadie quiere— sobre **qué parte de esa capacidad se
puede cubrir con piezas MIT al lado del Canvas que ya tienen**: P8 para material docente, P14 para corrección sin que
califique el modelo, P20 para evaluación conforme por LTI.

**Y el hilo que conecta este trend con el 19, que es lo más interesante:** el mismo vendor que acaba de poner su AI
detrás de un nivel de pago es el que absorbió **Badgr**, la implementación de referencia de Open Badges que hoy devuelve
404. **La capa de credenciales y la capa de AI del mismo incumbente se cerraron en la misma ventana de tiempo.** Para una
propuesta, ese es un argumento de soberanía, no de precio.

⚠️ **Por qué está marcado como no verificado.** Los tres sitios con el detalle —`constellationr.com`, `nasdaq.com` y
`aijourn.com`— están **bloqueados por el proxy de egreso de esta sesión**. Fechas, nombres de niveles y condiciones
vienen de texto de resultados de búsqueda concordantes entre sí, **no de leer la fuente**. Es el dato más accionable del
pase y el peor verificado: **confirmarlo en el anuncio oficial de Instructure antes de llevarlo a un cliente.**

## 22. La licencia del contenido no es la licencia del código, y en educación abierta casi nunca coinciden (agregado 2026-10-01, pase 10)

Nueve pasadas de esta KB leyeron la licencia **del software**. El contenido curricular tiene **su propia licencia**, y es la
que decide si un entregable se puede facturar. Verificado en este pase contra el archivo `LICENSE`:

| Artefacto | Licencia declarada | Nivel de la página |
|---|---|---|
| `openstax/osbooks-calculus-bundle` | **CC BY-NC-SA** | `LICENSE` |
| `openstax/osbooks-biology-bundle` | **CC BY-NC-SA** | `LICENSE` |
| `openstax/osbooks-college-physics-bundle` | **CC BY-NC-SA** | `LICENSE` |
| `CAHLR/OATutor` (cura problemas de Calculus Volume 1) | **CC BY 4.0** | README |
| `pythpythpython/openstax-mcp-server` | **CC BY 4.0** | README |

**Las dos condiciones del lado NC-SA pegan exactamente donde duele:** *NonCommercial* prohíbe el uso en un entregable
facturado, y *ShareAlike* obliga a licenciar la derivación igual — o sea, a abrir el corpus construido para el cliente.

**Lo que el trend afirma** es que **la fuente secundaria y el README son sistemáticamente menos confiables que el archivo
`LICENSE`**, y que en la capa de contenido la diferencia cambia la viabilidad comercial del proyecto. **Lo que no afirma** es
cuál de las dos licencias de OpenStax es la vigente: `openstax.org` está bloqueado por el proxy (gap 17).

**La regla, y es barata:** el README de OATutor dice dónde está la respuesta — la licencia se declara **por ítem**, dentro de
cada JSON. Se lee el ítem, se guarda el campo junto al dato, y **el manifiesto de licencias es el entregable** (**P22**).
Corolario: **un corpus mezclado es del color de su ítem más restrictivo**, no del promedio.

**Es la tercera vez que esta KB encuentra el mismo patrón en tres capas distintas:** pase 7, los datasets de knowledge
tracing son NonCommercial; pase 8, la tecnología asistiva madura es copyleft; pase 10, el contenido es NC-SA y **el metadato
del catálogo también** (gap 16). **El riesgo de licencia en educación no está en el código: está en todo lo que el código
necesita para funcionar.**

## 23. Las estrellas de GitHub esconden la infraestructura educativa que está realmente desplegada (agregado 2026-10-01, pase 10)

Hallazgo de método, y es el que más cambia cómo se construye esta KB. Nueve pasadas ordenaron por estrellas. Con ese orden,
**la plataforma educativa más grande del mundo era invisible**.

| Repo | Stars | Forks | Commits | Forks/Stars |
|---|---|---|---|---|
| `Sunbird-Ed/SunbirdEd-portal` (sostiene DIKSHA, 180 M+ alumnos) | **41** | **317** | **38.046** | **7,7×** |
| `project-sunbird/sunbird-devops` | 62 | **392** | — | **6,3×** |
| `Sunbird-Ed/SunbirdEd-consumption-ngcomponents` | 3 | 64 | — | **21×** |
| `DSpace/DSpace` | 1.1k | **1.5k** | **25.385** | 1,4× |
| `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` | 28 | 47 | 1.053 | 1,7× |
| `HKUDS/DeepTutor` (comparación) | **40,6k** | — | — | ≪1 |

**La explicación es el modelo de adopción, no la calidad:** en infraestructura pública **el fork es la unidad de
despliegue**. Cada estado indio forkea Sunbird para levantar su instancia; cada distrito forkea Ed-Fi. La estrella mide
*atención de desarrolladores*; el fork mide *organizaciones que lo pusieron en producción*. **Son métricas de cosas
distintas, y para vender a un ministerio importa la segunda.**

**Un proyecto con 38.046 commits y 41 estrellas no está muerto: nadie lo mira y todo el mundo lo usa.**

**La regla operativa para esta KB:** en las capas de **plataforma institucional, estándar e infraestructura pública**,
ordenar por **forks y commits**, no por estrellas. Es hermana de la regla del pase 6 (*si un gap sobrevive, revisar el
nombre que no se está usando*) y del criterio del pase 9 (*en credenciales se elige por conformidad certificada, no por
popularidad*). **Las tres dicen lo mismo: el indicador por defecto de GitHub mide mal lo institucional.**

## 24. Hay una tercera vía para la plataforma de sistema educativo nacional, y es permisiva (agregado 2026-10-01, pase 10)

Hasta este pase, la respuesta de esta KB a «plataforma para un ministerio» era **Moodle** (GPL-3.0) u **Open edX**
(AGPL-3.0): las dos copyleft, con el agente obligado a vivir afuera o a asumir obligación de apertura. **Sunbird** cambia eso:
**MIT**, microservicios (contenido, autenticación, rutas de aprendizaje, analítica, notificaciones), app Android con consumo
**offline**, reconocida **Digital Public Good** por la DPGA, y **38.046 commits** de trabajo acumulado.

**Y en North America el equivalente de la capa de datos ya es permisivo también:** **Ed-Fi** pasó de licencia propietaria a
**Apache-2.0 en abril de 2020**, y con ese cambio sus repos privados se hicieron públicos.

**La consecuencia para el posicionamiento, que es lo vendible:** el argumento de «open source para soberanía educativa» dejó
de tener la contradicción de licencia que tenía. Antes había que explicarle a un ministerio que la plataforma abierta que le
proponíamos lo obligaba a publicar sus modificaciones. **Con Sunbird y Ed-Fi no.** Ver **P23** y **P24**.

## 25. El Digital Omnibus dejó de ser propuesta y es derecho vigente: el Anexo III vence el 2027-12-02 (agregado 2026-10-01, pase 11)

La tendencia 11 (pase 4) ya registró que el Digital Omnibus entró en vigor el 2026-07-27 y que corrió la mitad cara
del AI Act dejando corriendo la barata. **Esa lectura se confirma y no se corrige.** Lo que este pase agrega es lo
que faltaba para poder citarlo en un documento de cliente: **el número de reglamento, la cronología legislativa
completa y los artículos modificados.**

**Reglamento (UE) 2026/1744** — *Digital Omnibus on AI*:

| Hito | Fecha |
|---|---|
| Propuesta de la Comisión Europea | **2025-11-19** |
| Aprobación del Parlamento Europeo | **2026-06-16** |
| Adopción final del Consejo | **2026-06-29** |
| **Entrada en vigor** | **2026-07-27** |

Modifica, entre otros, los artículos **9, 17, 18, 28, 43 y 50** del Reglamento (UE) 2024/1689, y también el
Reglamento (UE) 2018/1139 (seguridad aérea) y el 2023/1230 (máquinas).

**Lo que se movió y lo que no:**

| Obligación | Antes | Ahora |
|---|---|---|
| **Anexo III alto riesgo *stand-alone*** — incluye evaluación de resultados de aprendizaje, screening de postulantes y monitoreo de exámenes | 2026-08-02 | **2027-12-02** |
| Alto riesgo embebido en productos regulados | 2027-08-02 | **2028-08-02** |
| **Prácticas prohibidas**, entre ellas el **reconocimiento de emociones en instituciones educativas** | vigente | **vigente, sin cambio** |
| **Alfabetización en AI** (art. 4) | desde 2025-02-02 | **vigente, sin cambio** |

**Por qué esto no es "hay más tiempo" sino lo contrario, comercialmente.** 16 meses de corrimiento sobre la mitad
cara del expediente es exactamente el plazo en que un comprador institucional aprueba y contrata un programa de
conformidad. Antes del Omnibus, la fecha estaba tan encima que el comprador la trataba como imposible y la ignoraba;
ahora es alcanzable, y por lo tanto exigible internamente. **La ventana de compra se abrió al correrse la fecha, no
se cerró.** Y lo que ya es exigible —prohibiciones y alfabetización— sigue siendo la puerta de entrada barata al
mismo cliente. Ver **P4** y el patrón nuevo **P25**.

🔴 **Nivel de evidencia:** verificado en **múltiples fuentes legales secundarias independientes y coincidentes**
(firmas de abogados y publicaciones de cumplimiento que citan el número de reglamento, las fechas de votación y las
nuevas fechas de aplicación). **El texto primario no se leyó:** `eur-lex.europa.eu` y
`digital-strategy.ec.europa.eu` están bloqueados por el proxy de egreso de esta sesión. **Confirmar en EUR-Lex antes
de poner la fecha en un documento de cliente.**

## 26. La capa que decide sobre el alumno es la más regulada del sector y la peor abastecida de open source (agregado 2026-10-01, pase 11)

Once pasadas de esta KB describieron capas con oferta chica. **Esta es distinta: acá la oferta no es chica, es
inexistente, y se puede demostrar con dos consultas.**

| Consulta en GitHub, 2026-10-01 | Resultado | Techo de estrellas |
|---|---|---|
| `topic:learning-analytics stars:>50` | **2 repos en todo GitHub** | 169 ★, y es un blog de notas de papers |
| `dropout prediction student license:mit pushed:>2026-01-01` | **110 repos** | **6 ★** |

El único repo real del primer resultado es **`OpenLRW`** (62 ★), que almacena datos y no predice nada. El tope del
segundo entrena con **datos sintéticos**. Y el stack institucional que esta capa tuvo —la **Apereo Learning
Analytics Initiative**— está archivado: `OpenLRS` dice `Deprecated` en su descripción, `OpenDashboard-legacy` dice
`(Deprecated)`, el reemplazo (`-ux` y `-api`) **se creó el 2020-02-12 y se abandonó dentro del mes**, y
*Student Success Plan* —el producto de advising con despliegues reales— **no tiene repositorio localizable** desde
alrededor de 2015.

**La asimetría que hay que leer.** En todas las capas anteriores de esta KB, la ausencia de open source coincidía con
ausencia de demanda o con demanda incipiente. Acá no: *student success* es **categoría de compra consolidada**, con
incumbentes propietarios y presupuesto asignado en cada universidad. **Es la única capa de esta KB donde la demanda
está madura, el presupuesto existe, y la oferta open source es cero.**

**Y la segunda asimetría, que es la útil:** el cuello de botella **no es el dato**. Los dos corpus canónicos de la
capa —**OULAD** (32.593 alumnos, 10.655.280 registros de clicks, The Open University) y **UCI 697** (4.424 × 36,
Portugal)— son **CC BY 4.0, con uso comercial permitido**. Es lo contrario del diagnóstico del gap 11 para knowledge
tracing, y la conclusión de una capa no se puede exportar a la otra. **Acá falta el software y falta quien lo
mantenga: las dos cosas que una consultora vende.**

Una nota técnica que vale para la propuesta: el benchmark de supervivencia sobre OULAD (arXiv 2604.08870, Eastern
University) reporta que, en ablación y explicabilidad, **la señal predictiva dominante es temporal y conductual, no
demográfica ni estructural**. Es el argumento que hace aprobable un sistema de riesgo ante un DPO o un comité de
ética: **se puede predecir sin apoyarse en atributos protegidos.** 🔴 Sin verificar de primera mano (`arxiv.org`
bloqueado) y las fuentes reportan que el link al repositorio del paper está roto.

## 27. ECL-2.0: una licencia permisiva que los filtros de licencia descartan por desconocida (agregado 2026-10-01, pase 11)

**Esta tendencia es un error propio documentado, y por eso es la más reutilizable del pase.** Diez pasadas de esta KB
filtraron por **MIT / Apache-2.0 / BSD** y, al hacerlo, descartaron en silencio el stack completo de la **Apereo
Foundation**, que licencia con **ECL-2.0 (Educational Community License 2.0)**.

**Qué es ECL-2.0, con precisión:** Apache-2.0 con **una** modificación — el alcance de la concesión de patentes de la
sección 3, acotado a la contribución en vez de a las combinaciones. Salió del *Licensing and Policy Summit*
convocado por la comunidad académica en 2006, porque las universidades no podían conceder el paquete amplio de
Apache-2.0 sobre código escrito con fondos de investigación. **Aprobada por OSI y por la FSF. No es copyleft.** El
propio README de `LearningAnalyticsProcessor` la describe como *"a slightly less permissive Apache2"*.

**Lo que el filtro dejaba afuera:** `sakaiproject/sakai` (**1.234 ★**, 1.014 forks, push del 2026-09-30, dos ramas
mantenidas), `opencast/opencast` (**505 ★**, la única capa de video de clase open source a escala),
`Apereo-Learning-Analytics-Initiative/OpenLRW` (62 ★, el único artefacto de esta KB que habla xAPI, Caliper y
OneRoster a la vez). **Un LMS de educación superior de primera línea no apareció en diez pasadas por una línea de
licencia que nadie leyó.**

**La generalización, y es la parte que sirve fuera de educación.** Un filtro de licencias por lista blanca de nombres
produce falsos negativos silenciosos, y los falsos negativos de un filtro no dejan rastro: no hay forma de notar lo
que no apareció. **La regla correcta no es "MIT / Apache / BSD" sino "permisiva, aprobada por OSI, sin obligación de
publicar el derivado"** — y cuando aparece una licencia desconocida, se lee en vez de descartarse. En educación esto
pega más fuerte que en otros sectores, porque los sectores con fundaciones académicas tienen licencias propias:
educación tiene ECL, y es probable que haya equivalentes en salud e investigación que esta KB tampoco vio.

**La contracara honesta que hay que decirle al cliente:** la concesión de patentes más angosta es real. Para uso,
modificación, cierre del derivado y redistribución, ECL-2.0 se comporta como Apache-2.0 ✅. **Para un entregable con
cesión de patentes o un cliente con due diligence de patentes, es una pregunta de legal, no una respuesta.** ⚠️

## 28. La educación perdió el canal de distribución más barato de la industria, y la vertical científica se lo quedó (agregado 2026-10-01, pase 12)

El estándar **Agent Skills** —bundles de instrucciones, referencias y scripts que un agente carga sólo cuando la tarea
los pide, leídos por Claude Code, Codex, Cursor, Antigravity, Gemini CLI y Copilot CLI— es hoy la vía de distribución de
conocimiento de dominio con la barrera de entrada más baja que existe: **sin backend, sin despliegue, sin dependencias
que auditar.** Un repo de Markdown.

**Las once pasadas anteriores de esta KB midieron la educación contra sí misma.** Esta la mide contra otra vertical en
el mismo canal, y el resultado es el peor número registrado. Verificado contra la página de cada repo el 2026-10-01:

| Biblioteca | Vertical | Licencia | Stars | Contenido |
|---|---|---|---|---|
| `K-Dense-AI/scientific-agent-skills` | Ciencia | **MIT** ✅ | **47.200** | 181 skills + 100+ bases de datos + 70+ workflows. Declara 160.000 científicos usuarios |
| `virgiliojr94/book-to-skill` | Genérico | **MIT** ✅ | **33.200** | Pipeline documento → skill. **+6.300 ★ en 30 días** |
| `GarethManning/education-agent-skills` | **Educación** | CC BY-SA 4.0 ⚠️ | **815** | 165 skills pedagógicas en 20 dominios |
| `ZeKaiNie/universal-examprep-skill` | **Educación** | **MIT** ✅ | **299** | Tutor de examen con cita de página |

**58× contra el activo educativo más grande; 158× contra el mejor educativo empaquetable.**

**Y la asimetría de licencia es el núcleo de la tendencia, no un detalle.** El activo educativo más grande de la capa
es **CC BY-SA 4.0** —*share-alike*, el derivado hereda la obligación— mientras el científico equivalente es **MIT**. Es
decir: la vertical científica publicó su conocimiento como **software**, y la educativa como **obra cultural**. Las dos
decisiones son coherentes con su cultura de origen, y sólo una de las dos se puede empaquetar en un entregable cerrado.

**Por qué esto es una tendencia y no una anécdota de estrellas.** Las once pasadas anteriores documentaron que lo bueno
en educación es caro de desplegar (plataformas), copyleft (accesibilidad, pase 8), archivado (analítica institucional,
pase 11) o de licencia trampa (contenido OER, pase 10). **Este canal no tiene ninguno de esos problemas** y la
educación igual no lo ocupó. La conclusión incómoda: el retraso de la capa educativa no se explica por barreras
técnicas ni de licencia, porque acá no hay ninguna. Ver `agents/top.md` y el **gap 20**.

## 29. El patrón que se repite en cinco capas de esta KB: lo que inventa su propio modelo de dominio no escala, lo que se conecta al estándar instalado sí (agregado 2026-10-01, pase 12)

El pase 5 registró **cinco servidores MCP de mastery** y concluyó "cinco reinvenciones del mismo patrón", con techo de
**1 ★**. El pase 12 encuentra el término de comparación que faltaba:
**`ankimcp/anki-mcp-server` — MIT, 499 ★, 254 commits, v0.22.0.**

| Enfoque | Repos | Techo |
|---|---|---|
| **Inventar** el modelo de dominio (grafo propio, scheduler propio, esquema propio) | los 5 MCP de mastery del pase 5 | **1 ★** |
| **Exponer** el estándar ya instalado (Anki, AGPL-3.0, +3 M de usuarios sólo en Android) | `anki-mcp-server` | **499 ★** |

Son ~500× con la misma tecnología (MCP), la misma licencia permisiva y la misma ventana temporal. La diferencia es de
dónde está el modelo de dominio.

**Y el patrón ya había aparecido cuatro veces en esta KB sin que se lo nombrara:**

- **Pase 9, credenciales:** las implementaciones de referencia de los estándares se retiran (`badgr-server`,
  `caliper-php`, `caliper-python`) y **el estándar sigue obligatorio**. Lo que sobrevive es lo que habla el estándar,
  no lo que lo reimplementa.
- **Pase 10, infraestructura desplegada:** Sunbird (MIT) tiene **41 ★** y 180 M de alumnos. La adopción no vive en la
  estrella; vive en el despliegue.
- **Pase 11, analítica institucional:** de los 21 repos de Apereo el único vivo es **`OpenLRW`**, y es precisamente el
  que habla **xAPI + Caliper + OneRoster a la vez**. Los que inventaban dashboard propio están archivados.
- **Pase 12, FSRS:** el algoritmo moderno de repetición espaciada **ya está integrado en Anki desde la versión 23.10
  (2023)**. `py-fsrs` (MIT, en esta KB) sirve para razonar y simular del lado del servidor, **no para reimplantarlo**.

**La regla operativa que esto deja, y aplica a cualquier propuesta de esta KB:** antes de construir el motor de un
subsistema educativo —mastery, repaso, credencial, telemetría, datos de alumno— verificar si existe el estándar
instalado y si hay un puente hacia él. **El valor del studio está en el puente y en la pedagogía, no en el motor.**
Ver **P28**.

## 30. La capa donde el alumno efectivamente trabaja estaba fuera del mapa, y es la de mejor licencia de todo el sector (agregado 2026-10-01, pase 13)

Doce pasadas de esta KB construyeron el mapa desde el agente hacia afuera: el tutor, el modelado del conocimiento, la
evaluación, la seguridad, la telemetría, los datos, la accesibilidad, la credencial, el contenido, la predicción y la
distribución. **Nunca apareció el entorno donde el alumno escribe la respuesta** — y en educación superior STEM y
formación técnica ese entorno está estandarizado desde 2014.

Es **Jupyter**, y la pila completa es **BSD-3-Clause**: `jupyterhub` (8.300 ★), `jupyter-ai` (4.400 ★), `nbgrader`
(1.400 ★, **v0.9.6 del 2026-09-30**), `otter-grader` (161 ★, UC Berkeley DSEP) y `ltiauthenticator` (73 ★, LTI 1.3
probado contra Open edX, Canvas y Moodle). **14.334 ★, una sola familia de licencia.**

**Por qué es un trend y no sólo un hallazgo de catálogo.** Esta capa viola, sola, los cinco patrones estructurales que
esta KB documentó pase tras pase:

| Patrón documentado por la KB | Esta capa |
|---|---|
| Lo desplegable es copyleft (Moodle GPL, Open edX y Canvas AGPL) | **Permisiva de punta a punta** |
| Lo permisivo es pre-tracción (tutores LATAM 0–3 ★) | **8.300 ★ y despliegue universitario de una década** |
| Los datos de entrenamiento son NonCommercial (gap 11) | **No aplica**: la evidencia la produce el alumno del cliente |
| El runtime de agente con MCP hay que construirlo | **Ya existe, BSD, con ACP y MCP** |
| El contenido tiene trampa de licencia (pase 10) | **No aplica**: el artefacto lo escribe el docente |

**La lectura comercial es un cambio de orden de operaciones.** Esta KB venía proponiendo *construir* el agente y después
buscarle dónde enchufarlo. En cualquier cliente de STEM, ciencia de datos, ingeniería o formación técnica **la
infraestructura ya está instalada o es trivial de instalar, es permisiva, y el trabajo facturable es la capa pedagógica
encima** — feedback formativo sobre tests que ya corrieron, estimación de mastery, evidencia hacia el LRS. Eso es más
barato de vender y mucho más defendible que una plataforma nueva.

**Y la causa de los doce pases de ceguera es metodológica, no de disponibilidad.** Jupyter no se presenta como producto
educativo: se presenta como herramienta de cómputo científico. Buscar «agente educativo», «tutor», «LMS» o «grading» no
lo devuelve nunca. Es la quinta vez que esta KB registra que **la consulta equivocada costó pasadas** (ver la nota de
método del pase 7). La regla que queda: **buscar también por el artefacto material del alumno —el cuaderno, el
entregable, el entorno de ejecución— y no sólo por el rol del software.**

## 31. Vietnam puso en vigor lo que Europa posterga, y su texto nombra exactamente el patrón base de esta KB (agregado 2026-10-01, pase 13)

El **trend 10** registró que Corea del Sur ya tenía en vigor el régimen que Europa no aplicaba, y el **trend 17**
consolidó que «la ola regulatoria de APAC dejó de ser Corea del Sur sola». **Vietnam la extiende, y con el texto más
específico que esta KB encontró para educación.**

- La **Ley de Inteligencia Artificial** fue aprobada por la Asamblea Nacional el **2025-12-10** y está **en vigor desde
  el 2026-03-01**. Es la primera ley integral y autónoma de AI del país, de enfoque **basado en riesgo**.
- El Gobierno publicó una **lista sectorial de 46 sistemas de AI de alto riesgo en seis sectores**, y **educación es uno**.
- En educación, alto riesgo incluye explícitamente tres cosas: **(a)** sistemas que entregan contenido de
  autoaprendizaje **a partir de fuentes de datos no controladas**; **(b)** sistemas que **evalúan, califican o rankean
  alumnos automáticamente**; **(c)** sistemas que **monitorean o analizan la conducta del alumno con datos biométricos**
  —reconocimiento facial, seguimiento de mirada—.
- Obligaciones: **evaluación de conformidad antes del despliegue** (y después de cada modificación significativa),
  documentación técnica, gestión de riesgo a lo largo del ciclo de vida, **supervisión humana** y transparencia. Para
  ciertos sistemas designados la evaluación **debe hacerla un organismo registrado o reconocido**; para el resto se
  admite autoevaluación del proveedor.
- **Las dos fechas que hay que llevar a una propuesta:** los sistemas de educación **ya en operación antes del
  2026-08-15** tienen período transitorio con vencimiento **2027-09-01**.

**Por qué esto reordena el reloj regulatorio de esta KB.** El vencimiento educativo de Vietnam (**2027-09-01**) cae
**antes** que el del Anexo III europeo (**2027-12-02**, trend 25). Por tercera vez, **APAC exige antes que EMEA** — y
esta vez con un texto más explícito que el europeo sobre qué arquitectura queda alcanzada.

**Y acá está el punto que ninguna otra regulación de esta KB había escrito.** El inciso (a) —contenido de
autoaprendizaje **desde fuentes de datos no controladas**— es, literalmente, la descripción de un **tutor RAG sobre
corpus abierto**, que es el **patrón P1** de esta KB y lo que el pase 10 documentó al abrir la capa de contenido
curricular. En Vietnam eso no es una buena práctica: **es la condición que mete al sistema en alto riesgo**. El
entregable que el pase 10 inventó para un problema de licencia —el **manifiesto de procedencia por ítem** del patrón
**P22**— resulta ser también el expediente que vuelve demostrable el control de la fuente. **El mismo artefacto sirve
para dos obligaciones distintas en dos regiones distintas**, y eso lo vuelve mucho más fácil de justificar.

El inciso (c), de paso, confirma el diagnóstico del pase 8 sobre proctoring: **la vigilancia biométrica del alumno queda
en alto riesgo también en Vietnam.** Van tres jurisdicciones (EU Anexo III, Corea, Vietnam) donde la categoría entera
nace con expediente de conformidad obligatorio.

## 32. LATAM dejó de tener un problema de adopción y tiene uno de gobernanza, y ahora hay número institucional (agregado 2026-10-01, pase 13)

El pase 4 de esta KB trajo la encuesta del Digital Education Council (92% de estudiantes y 79% de docentes de LATAM
usando AI) y concluyó que **«la región no tiene un gap de adopción; tiene un gap de oferta open source propia»**. Ahora
hay una medición institucional, de fuente multilateral, que precisa **dónde** está el déficit.

**UNESCO IESALC, publicado el 2026-09-09 durante la UNESCO Digital Learning Week 2026**, sobre **200 instituciones de
educación superior de 19 países** de América Latina y el Caribe:

| Indicador | Valor |
|---|---|
| Instituciones que usan AI en al menos un área | **87%** |
| Que la usan en enseñanza y aprendizaje | **74%** (mayormente con herramientas de propósito general: ChatGPT, Copilot, Gemini) |
| Que la usan para análisis de datos e investigación | **57%** |
| **Que tienen una estrategia formal de AI** | **26%** |

Y el estudio señala la causa de la brecha: **el uso lo empujan docentes, investigadores y estudiantes, no las políticas
institucionales.** Es adopción de abajo hacia arriba, sin marco.

**La brecha 87 → 26 es el dato comercial del pase**, y conviene leerla junto con la cifra comparativa del pase 8: **~70%
de las instituciones de Europa y North America tienen o están desarrollando guías de AI, contra 45% en América Latina y
el Caribe.** La región no está atrasada en uso —está por encima de varias—; **está atrasada en gobernanza, que es
precisamente lo que se contrata.**

**Qué vende esto, concretamente.** No una plataforma: **un marco de gobernanza de AI institucional con inventario de uso
real.** El 87% que ya usa AI con herramientas de propósito general significa que en esas 200 instituciones hay *shadow
AI* docente sin registrar, sin política de datos y sin criterio de evaluación. El primer entregable no es un tutor: es
el **inventario + la política + el criterio de evaluación pedagógica** (patrones **P10**, **P11** y **P13**). Es un
proyecto corto, repetible en 19 países, y es la puerta de entrada al resto.

## 33. La capa curricular tenía un estándar de interoperabilidad desde antes que esta KB existiera, y catorce pasadas lo saltearon (agregado 2026-10-01, pase 14)

El gap 19 trataba los esquemas curriculares nacionales como artefactos sueltos a coleccionar país por país. Esa era
la mitad del problema. La otra mitad: **1EdTech publica CASE® (*Competencies and Academic Standards Exchange*), el
estándar que define cómo se publica, versiona e intercambia un marco de competencias o de estándares académicos, y
tiene implementaciones open source certificadas.**

El pase 9 abrió la familia 1EdTech por las **credenciales** (Open Badges, CLR) y no miró los **estándares**, que son
la misma familia de especificaciones. Catorce pasadas después, la capa aparece completa:

| Repo | Licencia | ★ | Conformidad |
|---|---|---|---|
| `opensalt/opensalt` | MIT | **45** | ⚠️ estable 3.2.0 (sept 2023) → **CASE v1.0** |
| `1EdTech/OpenCASE` | Apache-2.0 | **9** | ✅ **certificado CASE Service v1.0 y CASE v1.1 — 2026-02-17** |
| `infosign/compeito` | Apache-2.0 | **3** | ✅ *Provider* CASE v1.1 |
| `conform-ed/conform-ed` | MIT | **2** | ✅ **once estándares a la vez** |

**Y es la tercera vez que esta KB mide el mismo fenómeno: la pieza con más estrellas es la que está más atrás del
estándar.** OpenSALT tiene 45 ★ y su último estable es de septiembre de 2023 contra CASE v1.0; OpenCASE tiene 9 ★ y
está certificado contra v1.1 con fecha de febrero de 2026. El pase 10 lo midió con Sunbird (41 ★ sirviendo 180
millones de alumnos) y el pase 11 con Apereo. **Deja de ser anécdota y pasa a ser regla de método: en capas de
estándar el criterio de selección es la fecha de certificación, no la estrella.**

**La consecuencia de arquitectura, que es lo que importa comercialmente:** los cuatro esquemas curriculares
nacionales verificados se publican cada uno en su formato —RDF el inglés y el coreano, JSON propio el brasileño y el
estadounidense—. Un cliente no quiere cuatro parsers: quiere un endpoint. **CASE es ese endpoint, y hay dos
servidores Apache-2.0 que lo sirven.**

---

## 34. La capa donde el alumno habla no existía en esta KB, y es la que decide si un tutor sirve en primaria (agregado 2026-10-01, pase 14)

Trece pasadas buscaron por el rol del software, por la capa y por el alumno. **Ninguna buscó por el canal**, y todo
lo que esta KB tenía asumía un alumno que **escribe**: el notebook del pase 13, el SRS del pase 12, el LRS del pase 6.

**En alfabetización inicial, la medición que usan los sistemas educativos no es un cuestionario: es que el chico lea
en voz alta y se le midan palabras por minuto y exactitud.** Es la métrica de las evaluaciones de lectura en las
cuatro regiones, y hasta este pase esta KB —31 agentes, catorce capas— no tenía una sola pieza para capturarla.

La capa, medida:

- **`Halleck45/OpenPronounce` (MIT, 85 ★)** es la única pieza permisiva, educativa y utilizable: evaluación fonema a
  fonema con Wav2Vec2, PER/WER, confianza por palabra, DTW y prosodia (F0 y energía), **corriendo local sin API key**.
  Se posiciona explícitamente como la alternativa autoalojada a Azure Pronunciation Assessment.
- **`kaldi-asr/kaldi` (Apache-2.0, 15.5k ★)** es lo maduro, y es ASR genérico: no sabe nada de pedagogía.
- **`jimbozhang/speechocean762` (198 ★)** es el corpus de referencia —5.000 oraciones, **mitad niños**— y **no tiene
  archivo de licencia**.
- El resto de la capa son *papers*.

**Es el patrón base de esta KB otra vez, con un signo que mejora el caso:** lo maduro es genérico y lo educativo es
chico, igual que en accesibilidad (pase 8) y en *skills* (pase 12) — pero acá **la pieza educativa chica es MIT y corre
local**, así que el obstáculo no es la licencia ni la soberanía del dato. Es que nadie la empaquetó para un sistema
educativo.

**Y hay un hueco de mercado que conviene nombrar con número: ~600 millones de hispanohablantes y lusohablantes sin
pieza permisiva de evaluación de fluidez lectora.** El corpus de referencia es inglés con L1 mandarín; lo único de
LATAM (`carrera-lectora`, Chile) no tiene licencia. **Los puntajes publicados sobre `speechocean762` no son
transferibles a un despliegue en español o portugués sin recalibración**, y eso es alcance y presupuesto propios, no
un detalle de implementación.

---

## 35. Lo curricular no es copyleft, y esta KB lo venía asumiendo mal (agregado 2026-10-01, pase 14)

Cuatro pases seguidos (8, 9, 10 y 11) encontraron la misma forma: **lo maduro es copyleft, lo permisivo no tiene
tracción.** Accesibilidad (OptiKey GPL-3.0, Cboard GPL-3.0), interoperabilidad, contenido abierto (donde además
apareció el agravante NonCommercial), analítica institucional. El gap 19 leyó la capa curricular con ese mismo filtro
y sacó una conclusión regional: el coreano es MIT y el español CC BY-SA, *ergo* «el artefacto de APAC es mejor
técnicamente y más barato legalmente», espejo del gap 4.

**Con cuatro artefactos más verificados, el patrón se cae, y en el buen sentido:**

| País | Artefacto | Licencia de datos | Uso comercial |
|---|---|---|---|
| Inglaterra | `oak-curriculum-ontology` | **OGL-3.0** | ✅ con atribución |
| Brasil | `bncc-dados` | **CC BY 4.0** | ✅ con atribución |
| EE. UU. | `commonstandardsproject/api` | **Apache-2.0** | ✅ |
| Corea del Sur | `korean-elementary-learning-map` | **MIT** | ✅ |
| España | `OpenDidactia` | ⚠️ CC BY-SA 4.0 | ⚠️ *share-alike* |

**Hay permisivo apto para uso comercial en las cuatro regiones, y el único *share-alike* es el español.** La
conclusión útil no es «APAC gana»: es que **la capa curricular es, por licencia, la más limpia de toda esta KB**, y
que el filtro mental de los pases 8-11 —«si es educativo y maduro, va a ser copyleft»— **produce falsos negativos
caros** en esta capa.

**La regla nueva que este pase agrega, y vale para toda la KB:** en artefactos de datos, **la licencia del código y
la del dato son dos licencias distintas y casi nunca coinciden.** `bncc-dados` es MIT en código y CC BY 4.0 en datos;
`oak-curriculum-ontology` es MIT en código y OGL-3.0 en ontología. Leer sólo el badge del repo —que muestra la del
código— hace creer que el dato es MIT. **No lo es, y la atribución es una obligación de entregable.**

---

## 36. La pregunta «¿lo escribió una AI?» no tiene respuesta, y la industria educativa está terminando de aceptarlo (agregado 2026-10-01, pase 15)

No es una opinión sobre la tecnología: es el resultado convergente de los propios autores de los detectores, de
sus benchmarks y del comportamiento de las instituciones.

**El número que lo decide, y es el que importa para una empresa global:** siete detectores evaluados sobre
ensayos TOEFL dan **61,3 % de falsos positivos sobre escritura de no nativos de inglés**, contra **~2,9 %** sobre
universitarios estadounidenses nativos. La explicación propuesta —**baja perplejidad** del texto de no nativos por
menor variabilidad léxica— implica que **es estructural**: un detector mejor entrenado sigue midiendo lo mismo.

**Y el resto de los modos de falla están medidos:**

| Medición | Valor | Fuente |
|---|---|---|
| FPR sobre 1.180 abstracts académicos **anteriores a 2018** | **5,85 %**, más 20 % en «incierto» | `Lendarixon/awesome-ai-detection` |
| Texto humano mal marcado por un ensamble de 23 motores | 1 de 66 | README de `sloptotal` |
| Longitud mínima para que el score signifique algo | **~80 palabras**; estabiliza en ~200 | README de `sloptotal` |
| Efecto de la paráfrasis sobre la exactitud | **caídas grandes** | benchmark RAID (ACL 2024) |
| Transferencia a modelos más nuevos | falla | `awesome-ai-detection` |

**`Binoculars` (ICML 2024) lo escribe en su propio README:** *«more proficient in detecting English language text
compared to other languages»*, *«none are perfect and can have multiple failure modes»*, **«for academic purposes
only»**, con supervisión humana requerida.

**El comportamiento institucional ya se movió.** Vanderbilt hizo la cuenta —**1 % de FPR sobre 75.000 trabajos
son ~750 acusaciones injustas por año**— y desactivó el detector de AI de Turnitin. **Más de 50 universidades**
de EE. UU., Reino Unido, Canadá, Australia y Sudáfrica (Johns Hopkins, Yale, Waterloo, Curtin, Australian
Catholic University) lo desactivaron, restringieron o lo abandonaron; **al menos 12 instituciones grandes a marzo
de 2026**. Y el criterio que quedó escrito en las políticas de 2026 es que **un score de detección no es prueba
autónoma de mala conducta**: hace falta un segundo detector, revisión humana y derecho de apelación.

**Qué significa para una propuesta.** No significa que la categoría desaparezca: significa que **cambia de uso**.
Un detector sirve para **priorizar una conversación docente**, nunca para disparar una sanción. Vender detección
como mecanismo disciplinario a un cliente cuyos alumnos escriben inglés como L2 —LATAM, EMEA no anglófona, buena
parte de APAC— es venderle el **61,3 %**. Ver el **gap 25**, la capa en `agents/top.md` y el patrón **P33**.

---

## 37. La integridad se está moviendo de la detección a la procedencia, y la procedencia es Apache-2.0, obligatoria en EMEA y no la usa nadie en educación (agregado 2026-10-01, pase 15)

Es la contracara de la tendencia 36 y es donde está el trabajo vendible.

**La pregunta cambia de forma.** *«¿Esto lo escribió una AI?»* es un juicio probabilístico sobre texto ajeno y no
tiene respuesta confiable. *«¿Esto lo escribió **nuestro** tutor?»* es una **verificación**, y la respuesta es
cierta. Una institución que **provee** el agente puede marcar su salida en el origen; la integridad deja de ser
forense. Es exactamente la forma que describe la **tendencia 29** —lo que se conecta al estándar instalado
escala— aplicada a la autoría.

**Las piezas existen, están maduras y son permisivas:**

| Capa | Pieza | Licencia | Señal de madurez |
|---|---|---|---|
| Watermark de texto | **SynthID-Text**, dentro de `huggingface/transformers` | **Apache-2.0** | En producción en Transformers; copyright HuggingFace + **Google DeepMind** |
| Evaluación del watermark | **MarkLLM** | **Apache-2.0** | **1.100 ★**, 23+ algoritmos, 12 herramientas de evaluación, EMNLP 2024 Demo |
| Procedencia del artefacto | **c2pa-rs** / **c2pa-python** | **MIT *y* Apache-2.0** (dual) | **1.907 commits**; spec C2PA 2.4 con *CAWG identity assertion* |

**Y en EMEA dejó de ser opcional.** El **Artículo 50** está en vigor desde el **2026-08-02**, y los sistemas de
AI generativa **ya en el mercado** antes de esa fecha tienen hasta el **2026-12-02** para cumplir el marcado
legible por máquina del **Artículo 50(2)**: el contenido debe estar marcado de forma *«effective, interoperable,
robust and reliable»*. El **Code of Practice** sobre marcado y etiquetado —voluntario, pero la vía más clara para
demostrar cumplimiento— define un esquema **por capas (metadato + watermarking**, con *fingerprinting* y
*logging* de apoyo) y **adopta las *Content Credentials* de C2PA como estándar técnico de facto** del metadato.

🔴 **Dos cosas que hay que decir con honestidad.** Primero: **esta KB venía recomendando esta oferta desde el
pase 4 sin tener una sola pieza registrada** — `compose/patterns.md:106` anota el deadline del 2026-12-02 desde
entonces, y `watermark` aparecía cinco veces en la KB, **todas en prosa comercial, ninguna apuntando a código**.
Queda corregido. Segundo: **ningún proyecto educativo open source usa nada de esto.** No hay plugin de LMS,
herramienta LTI ni servidor MCP que marque o verifique la salida de un tutor. La infraestructura está lista; **el
puente al aula no está construido**, y es trabajo de días. Ver **P33** y el **gap 25**.

⚠️ **El límite honesto:** el marcado sólo cubre el texto que generó el sistema propio. No resuelve el ensayo
escrito con un modelo externo. Convierte un problema irresoluble en uno **parcial pero cierto**, más un régimen
de **declaración** para el resto — que es, justamente, lo que LATAM ya exige por norma (tendencia 38).

---

## 38. LATAM tiene el régimen regulatorio que el open source puede cumplir hoy, y tiene instalada la herramienta que no lo cumple (agregado 2026-10-01, pase 15)

Las cuatro regiones resolvieron la integridad académica de forma distinta, y **la latinoamericana es la única que
el stack permisivo existente satisface completo**. Es la primera vez en quince pasadas que la lectura regional
sale a favor de LATAM por el lado de la **norma** y no por el del talento.

| Región | Régimen dominante | ¿Lo cumple el open source de hoy? |
|---|---|---|
| **North America** | Vacío federal, parches estatales (Colorado, Texas, Idaho SB 1227). **El abandono de la detección nació acá** | Parcial. No hay obligación que cumplir; hay un hueco que llenar |
| **EMEA** | **Obligación legal con fecha**: Art. 50 en vigor 2026-08-02, marcado legible por máquina 2026-12-02 | **Sí** — y es obligatorio. SynthID-Text + C2PA |
| **APAC** | Fragmentado, sin marco común. Japón cauteloso con marco estatal; China centralizado *top-down*; **Australia: 26 de 35 universidades (73 %) ubican la política de AI dentro de la de integridad académica** | Parcial, caso por caso |
| **LATAM** | **Declaración obligatoria** del uso de AI en **México, Colombia y Chile**, con sanción por uso fraudulento y en algunos casos **entrega de los prompts** | 🟢 **Sí, completo.** Un régimen de divulgación se satisface con procedencia, no con forense |

**El punto es la distancia entre la norma y la herramienta.** La regla latinoamericana **no pide detectar: pide
declarar**. Eso se cumple marcando, firmando y registrando — exactamente lo que SynthID-Text y C2PA producen, con
certeza y sin acusar a nadie. **Y lo que está instalado es detección:** UNAM, Tec de Monterrey, UAM, BUAP y UdeG
usan **Turnitin Originality** como herramienta principal — el mismo tipo de producto que 50 universidades
anglófonas desactivaron, aplicado sobre alumnos que escriben **español**, donde está aún menos validado, y en una
región donde el **61,3 %** de la tendencia 36 pega de lleno.

**Y el contexto institucional lo vuelve urgente:** **más del 80 % de las instituciones de educación superior de
México no tiene marco normativo claro** sobre uso ético y académico de la tecnología. O sea: la norma nacional
existe en tres países, la mayoría de las instituciones no la bajó a reglamento, y la herramienta que compraron no
la sirve. Es una ventana de definición, no sólo de venta. Ver **P33** y `intel/market.md` → LATAM.

⚠️ **Pendiente de verificación, y es la pista más valiosa que deja este pase:** hay un dataset en Zenodo
(`zenodo.org/records/22661179`) con las políticas institucionales de integridad académica y lineamientos de AI
generativa de las **15 universidades latinoamericanas mejor rankeadas en THE 2026** (USP, Unicamp, PUC Chile,
UFRJ, UNESP…). **`zenodo.org` está bloqueado por el proxy de egreso: no se pudo verificar licencia ni contenido.**
Si tiene licencia abierta, es el mapa de la norma institucional de la región servido en bandeja.

## 39. La infraestructura de privacidad es la única capa de esta KB donde lo maduro es permisivo, y la educación no la usa (agregado 2026-10-01, pase 16)

Quince pasadas registraron la misma forma una y otra vez: lo que está desplegado es copyleft o propietario, y lo
permisivo no pasa de unas pocas estrellas. En la capa de privacidad del dato **esa forma se invierte**.

| Pieza | Licencia | ★ |
|---|---|---|
| PySyft (OpenMined) | Apache-2.0 | 10.0k |
| Flower | Apache-2.0 | 7.2k |
| Google DP | Apache-2.0 | 3.4k |
| Opacus (PyTorch/Meta) | Apache-2.0 | 2.0k |
| TensorFlow Privacy | Apache-2.0 | 2.0k |
| diffprivlib (IBM) | MIT | 920 |
| synthcity | Apache-2.0 | 687 |
| OpenDP (Harvard) | MIT | 437 |

**Más de 26.000 estrellas, todas Apache-2.0 o MIT, de Harvard, Google, Meta e IBM.** No hay fricción de licencia,
no hay riesgo de procedencia, no hay que construir nada.

**Y la educación no la toca.** Lo específicamente educativo de esta capa es `PrivGen` (MIT, **3 ★**),
`federated-deep-knowledge-tracing` (**10 ★**, sin licencia), `FedGKT` (**1 ★**, sin licencia) y `SynEdu-HEDL`
(**1 ★**, sin licencia). El techo es **10 estrellas** y **tres de los cuatro no son reutilizables** por no
declarar licencia.

**La lectura, y es la tendencia:** el cuello de botella de esta capa no es tecnológico ni de licencia — es de
**integración**. La distancia entre `Flower` y un modelo de knowledge tracing federado la recorrió un repo de 1
estrella usando piezas que cualquiera tiene disponibles. Es la capa de mejor relación esfuerzo/defensa de toda
esta KB, y es la que nadie recorrió.

## 40. El reloj de privacidad de Norteamérica ya venció, y es el primero de esta KB que se vende como exposición y no como preparación (agregado 2026-10-01, pase 16)

Esta KB viene administrando relojes regulatorios futuros: el Artículo 50 del EU AI Act **vence el 2026-12-02**, el
Anexo III **el 2027-12-02**, Vietnam y Corea con sus propias fechas. Todos se venden igual: *falta tanto, hay
ventana de consultoría*.

**La regla COPPA enmendada de la FTC rompe ese patrón porque ya pasó.**

| Hito | Fecha |
|---|---|
| FTC anuncia las enmiendas finalizadas | enero de 2025 |
| Publicación en el *Federal Register* | 2025-04-22 |
| Entrada en vigor | 2025-06-23 |
| 🔴 **Fecha de cumplimiento general** | **2026-04-22** |

Es la primera actualización sustantiva de COPPA en **doce años**, y lo que agregó es exactamente lo que le pega a
esta KB:

- **Identificadores biométricos** —**voiceprints**, faceprints, huellas dactilares y de palma— pasan a ser
  **información personal**. Eso alcanza a toda la **capa de voz** que el pase 14 abrió, y a cualquier función de
  reconocimiento facial.
- **Consentimiento verificable separado** antes de compartir dato de menores con terceros.
- **Prohibida la retención indefinida**: hace falta **política escrita** de retención y borrado en plazo.

Y debajo, el régimen estatal que ya existía: **SOPIPA** (California) prohíbe vender dato de alumnos y la
publicidad dirigida sin vía de consentimiento que lo habilite; **SOPPA** (Illinois) impone requisitos
contractuales, plazos de notificación de brecha y transparencia pública; **Nueva York** prohíbe el reconocimiento
facial en escuelas; y **BIPA** (Illinois) exige consentimiento escrito para biométricos con daños estatutarios de
**1.000 a 5.000 USD por violación**.

**Por qué cambia el argumento comercial:** con un reloj futuro se vende un plan. Con un reloj vencido se vende
**remediación**, el comprador es otro (jurídico y no innovación), el ciclo es más corto y la objeción «esperemos a
ver cómo queda la norma» no existe. Es, de las cuatro regiones, la única donde esta KB puede decir hoy que el
plazo ya se cumplió.

## 41. El dato de aprendizaje empezó a nombrarse como perfilado dañino, y eso toca la capa predictiva que esta KB declaró desabastecida (agregado 2026-10-01, pase 16)

El pase 11 abrió la capa predictiva —*early warning*, riesgo de deserción— y la registró como **la única capa de
esta KB donde la demanda está madura y la oferta open source es cero** (gap 18). El encuadre era de oferta. Lo que
el pase 16 agrega es que **la demanda de esa capa está empezando a tener techo regulatorio en tres regiones a la
vez**, y por el mismo motivo.

- **APAC (India).** Bajo la **DPDP Act 2023**, toda escuela que procese dato digital de alumnos es *Data
  Fiduciary*, y la **Sección 9** aplica por tratarse de menores: consentimiento parental verificable, sin
  seguimiento conductual ni publicidad dirigida, y nada de tratamiento que pueda causar daño. Sanciones de hasta
  **₹200 crore** por infracción con datos de menores. La lectura de los analistas regionales es explícita: una
  analítica que etiqueta a un alumno como *«de bajo potencial»* o que predice problemas de conducta sin
  salvaguardas **puede tratarse como perfilado dañino**.
- **EMEA.** El Anexo III del EU AI Act ya clasificaba la predicción de deserción como alto riesgo; el GDPR le suma
  el **DPIA obligatorio del Artículo 35** antes del despliegue.
- **LATAM (Brasil).** El **Referencial** del MEC (2026-03-12) advierte sobre la necesidad de transparencia
  algorítmica y sobre el riesgo de **sesgo algorítmico que reproduce y amplifica desigualdades sociales presentes
  en las bases que alimentan estos sistemas** — que es la descripción exacta de un modelo de riesgo de deserción
  entrenado con datos históricos.

**La síntesis que importa para una propuesta:** la capa predictiva no está sólo desabastecida de código — está
quedando **condicionada a una arquitectura**. Un modelo centralizado entrenado con histórico de alumnos y que
emite una etiqueta de riesgo por persona es exactamente el objeto que las tres regiones están nombrando. Lo que
sobrevive a ese encuadre es la versión federada, con DP, con humano en el lazo y con el dato quieto — o sea,
**P25 más P34**.

Y hay un matiz que corrige la lectura del pase 11 sobre esta misma capa. El pase 11 anotó como debilidad que el
repo tope de la capa (`Aliipou/Student-Retention-Prediction`, MIT, 6 ★) **entrena con datos sintéticos**. Visto
desde este pase, entrenar con sintéticos no es la debilidad: **es la decisión correcta**. La debilidad es que lo
hace **sin garantía de privacidad declarada y sin evaluación de utilidad** — que es precisamente lo que
`synthcity` aporta de fábrica con sus métricas de *correctness* y *privacy*.


---

## 42. La máquina para gobernar el dato del alumno ya estaba instalada, lleva años en producción y es toda copyleft (agregado 2026-10-01, pase 17)

Es la tendencia que da vuelta la del pase 16, y las dos juntas describen la capa completa.

**La tendencia 39 dijo**: la infraestructura de privacidad es la única capa de esta KB donde lo maduro es
permisivo, y la educación no la usa. Eso era cierto **de las librerías horizontales** —DP, federado, sintéticos—.

**Lo que faltaba mirar es el LMS**, y ahí la forma es la inversa: **Moodle** (GPL-3.0, 7.5k ★, 123.147 commits)
tiene un **Privacy API en el núcleo que obliga a todos los plugins** a saber exportar y borrar el dato que
guardan; **Open edX** (AGPL-3.0, 8.2k ★) tiene un toolset de retiro de usuario con seis scripts y API REST de
retiro masivo que alcanza LMS, foros, credenciales y las demás IDAs. **No es incipiente: está desplegado en
decenas de miles de instituciones y lleva años en producción.**

**Por qué esto cambia el diagnóstico de la KB y no sólo lo amplía.** Dieciséis pasadas trataron la privacidad
educativa como una capa **faltante**. No falta: **falta operarla.** El `grep` del pase 16 sobre los ocho archivos
—`COPPA` 0, `differential privacy` 0, `federated` 0, `FERPA` 1— medía correctamente la ausencia en la KB, y de
ahí se concluyó ausencia en el sector. **Era ausencia de la KB.**

**Y el copyleft, por única vez en dieciséis pasadas, no es la mala noticia.** No hay que forkear: Moodle se
**extiende** (un `privacy provider` en el plugin propio) y Open edX se **invoca** (scripts y un endpoint). Lo que
se entrega es plugin, configuración, evidencia y operación — no una derivada del LMS. El entregable de esta capa
**casi no es software**, y eso la hace más barata de construir y más difícil de copiar. Ver **P36**.

⚠️ **El límite, y está declarado por el propio proveedor:** *«User retirement is not a compliance guarantee. The
Open edX software makes no claim of satisfying any law or regulation. It is a configurable toolset that site
operators can use to help meet the obligations apply to them specifically.»* El cumplimiento es del **operador
del sitio** — que es precisamente el alcance vendible, y la razón por la que esta capa es servicio y no producto.

## 43. Norteamérica pasó del mandato de política a la prohibición de entrenamiento, y es la primera ley que le toca el modelo de negocio al sector (agregado 2026-10-01, pase 17)

Las tendencias 8 y 40 registraron el reloj regulatorio de Norteamérica como **obligación de tener política
escrita** (COPPA enmendada, 2026-04-22) y como **exposición ya vencida**. Este pase registra el salto siguiente, y
es de otra naturaleza.

**California AB 1159** (Asambleísta **Dawn Addis**) pasó la Legislatura el **2026-08-31** y **el gobernador la
firmó el 2026-09-13**. Lo que hace:

- **Prohíbe** usar información cubierta del alumno —**incluidos identificadores únicos persistentes**— para
  **entrenar sistemas de AI generativa o desarrollar modelos de AI**, *salvo* que el uso sea **estrictamente en
  función de un propósito educativo y en beneficio de la institución educativa correspondiente**.
- **Prohíbe la venta** de datos de alumnos, y pone límites de compartición y retención.
- Crea la **HESIPA** (*Higher Education Student Information Protection Act*), que **entra en vigor el
  2027-07-01** y extiende por primera vez el régimen a **educación superior**: ~**2,9 millones** de estudiantes
  universitarios de California.
- Mejora **KOPIPA** y **ELPIPA**, y protege categorías sensibles: **estatus migratorio, identidad LGBTQ+ y salud
  reproductiva**.

**Por qué esto es distinto de todo el reloj regulatorio que esta KB tiene registrado.** El AI Act europeo, la ley
coreana y la vietnamita regulan **cómo** se usa el sistema: expediente de conformidad, supervisión humana,
transparencia. **AB 1159 prohíbe un insumo.** No pide documentar el entrenamiento sobre dato del alumno: lo
prohíbe, con una excepción acotada.

🔴 **Y le pega a un patrón propio de esta KB.** El **P16** —entrenar el estimador de *mastery*— y el **P1** —tutor
adaptativo con retención real— se apoyan en entrenar modelado del alumno con dato del alumno. **A partir del
2027-07-01 en California eso es ilícito salvo que se pruebe la excepción**, y la excepción no es «es educativo»
en abstracto: es **propósito educativo estricto y beneficio de esa institución**. Entrenar un modelo central con
dato de muchas instituciones para servir a todas **no cae obviamente dentro**, y es la arquitectura por defecto
de la industria.

**La lectura comercial, y es buena noticia para la arquitectura que esta KB ya eligió:** la excepción es
exactamente lo que el **aprendizaje federado** y el **entrenamiento on-premise** permiten defender —el dato no
sale de la institución y el beneficio es de la institución—. El pase 16 abrió esa capa (tendencia 39, **P34**) sin
saber que dieciocho días antes se había firmado la ley que la vuelve obligatoria en el mercado educativo más
grande de los Estados Unidos. Ver **P37** y el **gap 30**.

## 44. El incidente de Canvas movió el presupuesto de privacidad educativa más que cualquier fecha regulatoria (agregado 2026-10-01, pase 17)

Esta KB vende cumplimiento contra fechas. Esta tendencia registra que, en Norteamérica, **lo que abrió el
presupuesto fue un hecho consumado**.

**2026-04-29** y **2026-05-07**: dos incidentes en **Instructure**, con cambios no autorizados en páginas de
Canvas en el segundo. Interrumpió clases y exámenes finales en EE. UU., incluidas varias **HBCU**.
**ShinyHunters** reclamó ~**275 millones de registros** de alumnos, docentes y personal: nombres, correos,
**números de identificación de alumno** y **mensajes privados**. Sin indicio de SSN, fechas de nacimiento ni
contraseñas. **2026-05-11**: Instructure informó un **acuerdo con los atacantes** para devolución y destrucción
del dato, con *«shred logs»* como prueba de borrado.

**Canvas sostiene ~41 % de la educación superior del continente y miles de distritos K-12.** Por alcance, es el
incidente más consecuente que haya tocado al sector.

**Lo que esto cambia en una conversación de venta, y conviene no usarlo mal.** El argumento no es «su proveedor
es inseguro». Es que **el incidente dejó una pregunta sin respuesta que la institución no puede contestar sola**:
un acuerdo con el atacante y un log de borrado **no son verificables por la institución**, que sigue siendo la
responsable del dato y no tiene forma propia de saber qué se exfiltró de *sus* alumnos. La capacidad que faltaba
el 2026-04-29 —saber qué dato de qué alumno vive en qué sistema, exportarlo y borrarlo con evidencia— es
exactamente el Privacy API de Moodle y el retiro de Open edX, **operados**.

**Y el contexto que lo vuelve estructural, no anecdótico:** sólo el **11 %** de los distritos de EE. UU. aplica
medidas rigurosas de evaluación de privacidad antes de adoptar una herramienta de AI, y la violación de FERPA más
común de 2026 es **docentes pegando dato de alumnos en herramientas de AI de propósito general** sin acuerdo de
tratamiento — que no ocurre por imprudencia, sino porque **no hay herramienta conforme disponible en el
distrito**. El incidente de Canvas puso presupuesto donde ya había exposición.

## 45. Las dos mitades del derecho al olvido tienen licencias opuestas, y la permisiva es la que la educación no usa (agregado 2026-10-01, pase 18)

El pase 17 midió que la máquina para **borrar el registro** del alumno está instalada en el LMS y es **toda
copyleft**. Este pase midió la otra mitad —**borrar la influencia del dato sobre el modelo**— y es **toda
permisiva**. El contraste es exacto y es la tendencia:

| Mitad del derecho al olvido | Dónde vive | Licencia | ¿La usa la educación? |
|---|---|---|---|
| Borrar **el registro** | Instalado en el LMS: Privacy API de Moodle, `tool_dataprivacy`, `tool_policy`, retiro de Open edX | **Toda GPL-3.0 / AGPL-3.0** | Sí, viene de fábrica |
| Borrar **la influencia sobre el modelo** | Librerías horizontales de ML: `awesome-machine-unlearning` (MIT, 970 ★), `open-unlearning` (MIT, 607 ★), `awesome-llm-unlearning` (Apache-2.0, 627 ★), `SalUn` (MIT, 154 ★), `torchunlearn` (MIT, 12 ★), `model-provenance-kit` (Apache-2.0, 104 ★), `Data-Provenance-Collection` (Apache-2.0, 281 ★) | **Toda MIT / Apache-2.0** | **No. Cero.** |

**2.700+ estrellas combinadas, licencias que Globant puede usar para construir, y cero menciones de educación.**
Verificado buscando «education», «student» y «knowledge tracing» en los dos agregadores grandes (970 ★ y 627 ★):
ninguna aparición.

**Por qué esto es una tendencia y no un dato aislado:** es la **segunda** capa de esta KB donde lo maduro es
permisivo —la primera fue la privacidad horizontal del pase 16, con 26.000+ ★— y en las otras once lo maduro es
copyleft. Las dos capas permisivas son, las dos, **de cumplimiento**, **horizontales** y **sin adaptador
educativo**. Eso ya no describe una casualidad: describe dónde está el trabajo disponible. La industria de ML
resolvió el cumplimiento de forma reutilizable y **nadie lo trajo al aula**.

## 46. La ausencia que se registró por un nombre de rama, y cuesta una pasada entera (agregado 2026-10-01, pase 18)

El pase 17 declaró el **gap 29** —*«ningún `privacy provider` de referencia para un plugin de AI»*— después de
buscarlo y de registrar honestamente cuatro 404 contra `moodle/moodle`. **La referencia existía, estaba en el
núcleo y eran tres.** La causa del error no fue de criterio:

> **`moodle/moodle` no tiene rama `main` ni rama `master`.** Sus ramas son `MOODLE_XXX_STABLE`. Cualquier fetch
> contra `main` o `master` devuelve **404 con independencia de que el archivo exista**.

Medido por código HTTP en este pase: `ai/provider/openai/classes/privacy/provider.php` da **404 en `main`**, **404
en `master`**, **200 en `MOODLE_405_STABLE`** y **200 en `MOODLE_500_STABLE`**.

**Por qué merece ser una tendencia de la KB y no sólo una nota al pie:** esta KB mide ausencias y las vende como
información —*«un gap informado es información; el silencio se parece demasiado a la cobertura»*—. Entonces **el
método de medir ausencias es parte del producto**, y acá falló de una forma que se repite: un 404 contra un repo
grande, vivo y con releases versionadas es, con alta probabilidad, **un 404 sobre la rama**. La regla queda
escrita: **antes de declarar que algo no existe en un repo con releases, probar la rama de release.** El pase 17
tenía razón sobre terceros y se equivocó sobre el núcleo, y el costo fue una pasada entera de un gap mal abierto.

**Y el saldo positivo:** con las rutas correctas, `admin/tool/dataprivacy/version.php` y
`admin/tool/policy/version.php` dan **200**, con lo que el pase 17 deja de depender de snippets y la máquina de
privacidad del LMS queda **verificada de primera mano**.

## 47. LATAM produjo la mejor implementación de su capa y tiene cero estrellas, y esta vez el gap 2 no explica por qué (agregado 2026-10-01, pase 18)

El **gap 2** dice desde el pase 2 que *«LATAM produce agentes educativos, pero ninguno sale de la fase cero»*, y el
pase 13 lo reencuadró diciendo que el aporte real de LATAM no era el repo sino el instrumento de medición. **Este
pase encuentra el caso que no entra en ninguna de las dos lecturas.**

`jeanlucio/moodle-local_aihub` —Jean Lúcio, **Instituto Federal do Sertão Pernambucano, Brasil**— es, de las seis
piezas de la capa de `privacy provider` de la comunidad, **la más completa, y por margen**:

- **Cuatro** interfaces del Privacy API, incluida `user_preference_provider`, que ninguna otra implementa (las
  tres referencias del núcleo de Moodle implementan tres).
- Declara **las tres cosas a la vez**: tabla de base (`local_aihub_log`, 9 columnas), **6 preferencias de usuario**
  y **4 enlaces de ubicación externa** (`deepseek`, `google_gemini`, `groq`, `openai_compatible`).
- Diseño defendible: broker **BYOK** con *SSRF guard*, escalera de proveedores y *key store*; la API key es
  opcional y el plugin funciona sin ninguna; *«the hub never contacts a provider on its own»*.
- Disciplina de ingeniería que el resto de la capa no tiene: `.github/workflows/`, `tests/`, `docs/`, 60 commits.

**Tiene 0 estrellas y 1 fork.** Frente a: Ferrara (Italia) 3 ★ con tres interfaces, `tool_aiconnect` (Catalyst EU)
10 ★ sin provider visible, y una pieza de 0 ★ sin archivo `LICENSE`.

**Por qué el gap 2 no lo explica.** El gap 2 describe proyectos que no salen de la fase cero *por falta de
continuidad y de disciplina* —«buen problema, buen diseño, cero continuidad», como lo formuló el pase 11 para el
caso de la India—. **Acá la continuidad y la disciplina están**, y lo que falta es **visibilidad**: un repo con CI,
tests, docs y la implementación más completa de su categoría, invisible. La formulación correcta para este caso es
distinta y hay que escribirla aparte: **LATAM no sólo produce prototipos sin continuidad; también produce trabajo
mejor que el del promedio de su capa y no lo distribuye.** La acción no es construir: es **señalar**. Para esta KB
es la recomendación más barata que puede hacer —`local_aihub` es la referencia que **P39** usa cuando el plugin
guarda dato—, y para el autor, dos líneas en el directorio de plugins de Moodle.

**La lectura comercial, por región.** Un cliente de **EMEA** o **North America** que pida un plugin de AI con
expediente de privacidad va a recibir como referencia técnica una pieza **brasileña**, mantenida por un instituto
federal público. Eso es exactamente el argumento de *nearshore* de Studios con evidencia en vez de con
presentación.

## 48. El núcleo de Moodle documenta, en siete archivos idénticos, el punto donde su propia maquinaria de borrado se queda sin nada que borrar (agregado 2026-10-01, pase 19)

**El dato.** Moodle 5.3rc1 trae **siete** proveedores de AI en el núcleo (`anthropic`, `awsbedrock`, `azureai`,
`deepseek`, `gemini`, `ollama`, `openai`), y los siete traen `classes/privacy/provider.php`. Auditados sobre el
fuente, los siete son **idénticos en forma**: 70–78 líneas, **cero** llamadas a `delete_records`, `DELETE FROM` o
`add_database_table`, y **exactamente un** `add_external_location_link`. Todos sus métodos de borrado y export tienen
**el cuerpo vacío**, marcados `@codeCoverageIgnore`.

**La lectura correcta, que no es «están sin terminar».** Es la forma canónica para un plugin que **no guarda nada
localmente y sólo transmite**: lo único que tiene que declarar es el envío externo. Y por eso mismo **no sirven de
plantilla** para un plugin que sí guarde — ésa es otra, y está en el mismo árbol:
`public/ai/classes/privacy/provider.php` (`core_ai`), ~800 líneas, 6 tablas con `prompt` y `generatedcontent` entre
sus campos, y `delete_records_list()` real en las tres variantes de borrado.

**La tendencia, y es la que importa para una propuesta.** La línea divisoria dentro del propio núcleo de Moodle **no
es técnica, es de arquitectura de dato**: `core_ai` guarda el prompt y la respuesta, y por eso sabe borrarlos. Los
siete proveedores **no guardan: transmiten** — y lo único que pueden hacer es declararlo. Es decir: **el LMS más
desplegado del mundo documenta, siete veces, el punto exacto donde el derecho de supresión deja de ser ejecutable**,
porque el dato ya está en OpenAI, Anthropic, Google, AWS, Azure, DeepSeek o en el Ollama de un tercero.

**Por qué esto se vende y no sólo se anota.** Cualquier institución que active la AI de Moodle hereda esa frontera sin
decidirla. Un cliente que tiene que responder un pedido de supresión necesita saber **qué parte de la cadena alcanza
su Privacy API y qué parte no**, y la respuesta está escrita en el núcleo con nombre de archivo. Eso es un expediente
(**P35**) y un plugin (**P39**), no una discusión de principios.

> ⚠️ **Y la frase del propio núcleo que hay que leer antes de citar esto como tranquilizador** (se conserva del pase
> 18 porque sigue siendo exacta): `aiprovider_ollama` —el proveedor que un cliente elige **justamente** para que el
> dato no salga— declara «*No user data is **explicitly** sent*». El plugin no adjunta identidad; `prompttext` **sí**
> viaja, y el prompt lleva lo que el alumno escribió. **La declaración es exacta sobre la identidad y silenciosa
> sobre el contenido.**

## 49. La cadena de supresión tiene el agujero en la telemetría, y el estándar es el que lo abre (agregado 2026-10-01, pase 19)

**El dato, de arriba hacia abajo.** Esta KB venía construyendo una cadena de borrado de tres eslabones. Medidos los
tres en este pase:

| Eslabón | ¿Sabe borrar? | Con qué |
|---|---|---|
| **LMS** (el registro) | ✅ Sí | Privacy API de Moodle, `core_ai` con `delete_records_list()` — **GPL-3.0** |
| **Telemetría** (la historia del aprendizaje) | 🔴 **No** | **El estándar xAPI no define supresión.** Define *voiding*: marca sin borrar |
| **Modelo** (la influencia del dato) | ✅ Sí | OpenUnlearning (**MIT**, 607 ★), `torchunlearn` (MIT) — pero **no para modelos del alumno**: ver gap 34 |

**El eslabón del medio es el que falla, y falla en la especificación, no en las implementaciones.** xAPI —hoy IEEE
9274.1.1— no tiene operación de borrado de *statements*. Tiene ***voiding***: un statement nuevo con verbo `voided`
que declara obsoleto al anterior **dejándolo donde está**. Eso es exactamente lo contrario del art. 17 del GDPR, de
la Ley 21.719 chilena y del derecho de supresión que Vietnam, Corea y Brasil reconocen.

**Y abajo del estándar, el reparto de licencias repite por tercera vez el patrón de la tendencia 45:**

| LRS | Licencia | ★ | ¿Borra? |
|---|---|---|---|
| `lrsql` | **Apache-2.0** ✅ | 144 | 🚫 No documentado |
| Ralph | **MIT** ✅ | 51 | 🚫 No documentado |
| Learning Locker | **GPL-3.0** ⚠️ | 584 | ✅ Sí (API especial) |

**Lo permisivo no borra; lo que borra es copyleft.** Tres capas, tres veces el mismo reparto.

**Y hay que decirlo en primera persona, porque pega sobre el stack que esta KB recomienda.** `learnmcp-xapi` (MIT, en
la tabla principal) es el único artefacto de esta KB que conecta un agente con IEEE 9274.1.1, y declara como backends
**`lrsql`, Ralph y Veracity**: los permisivos. Un tutor armado con el stack recomendado por esta KB escribe la
historia del alumno en un almacén **del que no hay forma estándar de sacarla**. Eso no invalida el patrón: lo
convierte en un patrón con una obligación de diseño explícita (**P40**), y en una línea que hay que escribir en el
expediente antes de firmar.

**Consecuencia comercial, que es la parte útil.** La pregunta *«¿y si un padre pide que borren todo?»* no se contesta
con el LMS. Se contesta con **tres sistemas, tres licencias y un eslabón que hay que construir a medida** — y eso es
alcance facturable, no un riesgo que se esconde.

## 50. El dashboard que el regulador pide es la superficie de ataque que el regulador prohíbe (agregado 2026-10-01, pase 19)

**El dato.** **P-MIA** (arXiv 2511.04716) es el primer trabajo sistemático de inferencia de pertenencia contra
**modelos de *cognitive diagnosis***. Su modelo de amenaza es ***grey-box* y explota las funciones de explicabilidad
de la plataforma**: los vectores internos de estado de conocimiento **se exponen al usuario en visualizaciones —el
paper nombra los gráficos de radar— y se pueden revertir con precisión a partir de ellas**. Con probabilidades de
predicción + vectores reconstruidos, **supera con claridad** a los baselines *black-box* sobre tres datasets reales
contra CDMs mainstream. Mismo grupo que **PrivacyCD/HIF**; **ninguno de los dos publica código**.

**La tensión, dicha sin adornos.** El Anexo III del EU AI Act clasifica la evaluación automatizada como alto riesgo y
exige **transparencia y explicabilidad**. El GDPR exige **minimización**. P-MIA mide el costo de la primera en
términos de la segunda: **cuanto mejor le explicás el modelo al docente, más fácil es extraer de él quién estuvo en el
entrenamiento.** Las dos obligaciones aplican al mismo sistema y empujan en direcciones opuestas.

**Por qué le pega a esta KB y no es un riesgo genérico.** El dashboard de mastery **es algo que esta KB viene
recomendando**: es la salida natural de `pyKT` y `pyBKT`, es lo que `Gnos` instrumenta con su distinción
*vio / resolvió con ayuda / resolvió solo*, y es lo que la capa predictiva del pase 11 le muestra al docente. La
tendencia no es «hay un ataque nuevo»: es que **el artefacto que esta KB propone como entregable tiene un vector de
ataque publicado**.

**Lo que se hace al respecto, y es concreto:** ruido o cuantización en el vector de estado que se expone, o control de
acceso por rol de forma que el vector completo no salga nunca del lado docente — **y la decisión escrita en el
expediente de privacidad**, porque la elección entre explicabilidad y minimización es exactamente el tipo de decisión
que el Anexo III quiere ver justificada. Ver **P40**.

**Y el contrapeso, que es la buena noticia del pase:** la misma ventana trajo **OpenUnlearning** (MIT, 607 ★, CMU),
cuyas métricas **incluyen ataques de inferencia de pertenencia**. Es decir: **ya existe, con licencia permisiva, la
herramienta para medir si una defensa aguanta.** Lo que no existe es su aplicación a modelos del alumno — ése es el
**gap 34**, y es ensamblado, no investigación.

## 51. La industria construyó la máquina que prueba que una AI cumple, la publicó permisiva, y su catálogo de dominios cubre derecho, medicina y finanzas — educación no está (agregado 2026-10-01, pase 20)

Esta KB vende *expedientes de conformidad* desde el pase 4 —**P4** para el Anexo III europeo, **P10** para probar que
el tutor enseña, **P11** para el gate de seguridad pedagógica, **P17** para accesibilidad, **P39** para privacidad— y
en **diecinueve pasadas no registró una sola herramienta con la que ejecutarlos**. El pase 20 fue a buscarla y existe,
madura, permisiva, y publicada por organismos de gobierno:

- **`inspect_ai`** — **MIT**, **2.900 ★**, 763 forks, del **UK AI Security Institute**. 200+ evals pre-construidas.
- **`moonshot`** — **Apache-2.0**, 353 ★, de la **AI Verify Foundation** (Singapur, con IMDA). *Benchmarking* **y**
  *red-teaming*, con el **Starter Kit de IMDA v1.0 (enero 2026)** implementado como *cookbooks*.
- **`compl-ai`** — **Apache-2.0**, 211 ★, de **ETH Zürich + INSAIT + LatticeFlow AI**. **29 benchmarks mapeados a los
  6 principios núcleo del EU AI Act.**

**Y el hallazgo es la ausencia, declarada por los propios catálogos y no inferida de una búsqueda.** Tres artefactos de
tres jurisdicciones distintas publican su cobertura por dominio:

| Catálogo | Dominios que cubre | Educación |
|---|---|---|
| `LLM-Evals-Catalogue` (AI Verify Foundation) | **derecho, medicina, finanzas** | **ausente** |
| `compl-ai` (ETH Zürich / INSAIT / LatticeFlow) | 29 benchmarks sobre 6 principios del AI Act | **sin mención** |
| `awesome-eu-ai-act` (**CC0**) | 11 herramientas de conformidad open source | **ninguna educativa** |

**El contraste con lo que esta KB ya tiene es lo que convierte esto en oportunidad y no en queja.** Desde el pase 4
están registrados `EduBench` (**MIT**, ACL 2026, 9 contextos educativos), `SafeTutors` (**MIT**), `MathTutorBench`
(CC BY 4.0, EMNLP 2025 Oral) y `UnifyingAITutorEvaluation` (CC BY-SA 4.0, NAACL 2025): **benchmarks pedagógicos
premiados en los venues principales, y ninguno mapeado a un requisito regulatorio ni empaquetado como *recipe* de
ninguna herramienta.**

**Las dos mitades existen, están maduras, y son licencia-compatibles — MIT de un lado, Apache-2.0 del otro.** Lo que no
existe es el puente. Ése es el **gap 35**, y es distinto de todos los gaps técnicos de esta KB en un punto que decide
su valor: los gaps 31 y 34 esperan que alguien publique código; **el 35 se cierra con trabajo de integración sobre
repos que ya están verificados en esta KB.** No es investigación: es empaquetado. Y es el gap de mayor valor comercial
de esta KB, porque el expediente que habilita es el que ya se vende en cinco patrones. Ver **P42**.

⚠️ **Lo que este trend no dice, y es importante para no sobrevenderlo.** Ninguna de estas herramientas **certifica**:
`aiverify` declara por escrito que no define estándares éticos y **no garantiza** que el sistema evaluado esté libre de
riesgos o sesgos. El marco de Singapur es **voluntario** (sin penalidad, sin registro, sin *enforcement*), el europeo
no. No hay **crosswalk directo de AI Verify al EU AI Act** —sólo a **NIST AI RMF** (oct-2023) y a **ISO/IEC 42001:2023**
(jun-2024), y al AI Act se llega indirecto por ISO 42001—. Y `aiverify` evalúa **modelos supervisados tabulares y de
imagen, no agentes**: para un tutor LLM la pieza es Moonshot, Inspect o COMPL-AI.

## 52. Singapur tiene el despliegue educativo de AI más instrumentado del mundo y esta KB lo nombró una vez en diecinueve pasadas (agregado 2026-10-01, pase 20)

La KB registró de Singapur una sola línea: *«el agente tiene que vivir adentro del Student Learning Space»*. Es poco
para lo que hay. El **SLS** del MOE corre **ocho funciones de AI en producción nacional, seis de ellas usadas
directamente por el alumno**: **ALS** (Adaptive Learning System, matemática de primaria superior y secundaria inferior
+ geografía de secundaria superior), **LEA** (Learning Assistant), **FA-Math** (Feedback Assistant–Mathematics),
**AFA** (Annotated Feedback Assistant), **SAFA** (Short Answer Feedback Assistant) y **SET** (**Speech Evaluation
Tool**). Todas curadas, alineadas al currículo y supervisadas por docente, desarrolladas por **MOE + GovTech**.

**Y pega sobre tres cosas que esta KB tenía escritas:**

1. **La capa de lectura oral del pase 14, que se declaró desabastecida.** Ese pase escribió que la habilidad más
   evaluada en primaria en el mundo es la lectura oral y que **la KB no tenía una sola pieza para medirla**. Singapur
   la tiene desplegada a escala nacional (**SET**). **No cierra la capa** —es software estatal cerrado, no open
   source— pero cambia el argumento de venta: deja de ser una apuesta y pasa a ser **una función que un sistema
   educativo nacional ya considera indispensable**.
2. **El gap 6 (grading), intacto desde el pase 2.** Tres de las seis funciones del alumno son **asistentes de
   devolución** (FA-Math, AFA, SAFA). Singapur **confirma la demanda y no aporta oferta open source**: lo construyó el
   Estado, cerrado. **El gap 6 no se mueve** — pero deja de poder decirse que la demanda no está probada.
3. **La voz del menor del pase 16.** Un *Speech Evaluation Tool* usado por chicos es exactamente el caso que el pase 16
   levantó como regulado. Singapur lo resuelve con **plataforma estatal + supervisión docente** en vez de con
   consentimiento individual: **es una tercera vía de arquitectura que esta KB no tenía registrada.**

**La consecuencia arquitectónica, que ya estaba en la KB y ahora se entiende por qué.** El requisito de que el agente
viva **dentro** del SLS no es preferencia de compra: se corresponde con una política por nivel — según las fuentes
localizadas, **los alumnos de primaria inferior no usan AI directamente**, y **desde 4.º grado** el uso es
*estructurado, limitado, en clase y bajo supervisión docente*. Para un proyecto: **el SaaS suelto está descartado de
entrada**, y el entregable es un componente integrado con **control de nivel y traza de supervisión**.

⚠️ **Nivel de evidencia: secundario.** `moe.gov.sg` y `learning.moe.edu.sg` están **bloqueados por el proxy de egreso**
de esta sesión. Los nombres de las seis funciones y el alcance de ALS vienen de varias fuentes concordantes; **las otras
dos de las ocho no quedaron nombradas**. Hay que abrir la fuente del MOE antes de usar esto con un cliente.

## 53. El *machine unlearning* llegó a la educación, y entró por la puerta pedagógica en vez de por la de privacidad (agregado 2026-10-01, pase 20)

Los pases 18 y 19 abrieron la capa de *unlearning* buscando **la forma de cumplir el derecho al olvido sobre el modelo
del alumno** —borrar la influencia del dato, no sólo el registro— y dejaron el **gap 34**: *unlearning* evaluado sobre
modelos de alumno, con la nota de que `OpenUnlearning` (MIT, 607 ★) resuelve la técnica para LLMs pero **ninguno de sus
tres benchmarks evalúa un modelo de knowledge tracing o de cognitive diagnosis**.

El pase 20 encuentra el **primer repo educativo de *unlearning* con código publicado** —**`GEMLab-HKU/Unlearn_and_Relearn`**,
**MIT**, 4 ★, 22 commits, Universidad de Hong Kong— y **no cierra el gap 34, porque usa la técnica con el objetivo
invertido.**

**No borra para proteger a un alumno: borra para fabricar uno.** El problema que ataca es real y específico: un LLM al
que se le pide *«actuá como principiante»* se escapa igual hacia explicaciones de experto, y eso arruina las dinámicas
de *learning-by-teaching*, donde el alumno humano aprende enseñándole a un agente que **de verdad** no sabe. Entonces
aplica *unlearning* por destilación con intervención para volverlo novato de forma **configurable (10–50% de olvido)**,
y después mide cuánto **recupera** cuando el humano le enseña, con un loop de tres partes **Coach / Teachable Agent /
Judge**.

**Lo que esto cambia, y es más de lo que parece:**

- **El gap 34 sigue abierto** —falta el uso de **privacidad**— pero cambia de diagnóstico: **la maquinaria difícil ya
  existe en un contexto educativo y es MIT.** Borrar un concepto del modelo de un alumno y medir que se borró está
  implementado y funcionando. Lo que falta es **apuntarlo al objetivo de supresión**, no inventarlo.
- **Aparece una capacidad pedagógica que esta KB no tenía:** el **alumno simulado creíble**, que es la pieza que faltaba
  para evaluar un tutor sin poner chicos reales adelante — y eso conecta directo con **P10** y con el **gap 1** (el
  estándar de evaluación existe y no se adopta). Ver **P43**.
- ⚠️ **4 ★ y 0 forks: arquitectura de referencia, no dependencia.** Mismo criterio con el que el pase 8 trató a `tero`.

**🔴 Y la lección de método, que ya costó tres pasadas.** Los pases 18 y 19 buscaron este código y no lo encontraron por
una **colisión de terminología**: «knowledge tracing» significa dos cosas incompatibles. En esta KB y en `pyKT` es
*modelar el estado de conocimiento del alumno*; en la literatura de *unlearning* es *rastrear qué conocimiento de un
modelo fundacional vino de qué dato de entrenamiento* (p. ej. *Lifting Data-Tracing Machine Unlearning to
Knowledge-Tracing for Foundation Models*). **Buscar por la técnica devuelve el segundo sentido y entierra el primero.**
Lo que funcionó fue buscar por **escenario educativo** (*novice student simulation*) — exactamente la regla que el pase
5 aprendió para los benchmarks. **Tercera vez que esta KB paga el mismo peaje: cuando una búsqueda técnica no devuelve
nada en educación, hay que rehacerla por escenario antes de declarar el vacío.**

## Gaps declarados

Huecos confirmados tras buscar, no ausencias por no haber buscado. Un gap informado es información; el silencio se parece demasiado a la cobertura.

1. ~~**No hay evaluador pedagógico open source con tracción.**~~ → **GAP REFORMULADO en el pase 4 del 2026-09-30.** Los pases 1–3 registraron un solo evaluador, `AITutor-EvalKit` (MIT, MBZUAI, **3 ★**), y concluyeron que "no existe el LegalBench de educación". **La medición estaba mal hecha y la conclusión era más fuerte de lo que los datos permitían.**

   Lo que hay, verificado en el pase 4:

   - **`UnifyingAITutorEvaluation`** (https://github.com/kaushal0494/UnifyingAITutorEvaluation, CC BY-SA 4.0, **32 ★**) — **del mismo autor que `AITutor-EvalKit`**. Es el repo canónico: taxonomía de **8 dimensiones** pedagógicas y el dataset **MRBench** en tres versiones (V1 192 diálogos × 8 dim., V2 200 × 8, V3 300 × 4). **NAACL 2025, Senior Area Chair Award.** La KB había registrado el repo chico del mismo trabajo.
   - **`MathTutorBench`** (https://github.com/eth-lre/mathtutorbench, CC BY 4.0, **42 ★**) — no estaba en la KB. 3 habilidades docentes de alto nivel, 7 tareas, **reward models entrenados** para medir calidad de enseñanza y **leaderboard público**. **EMNLP 2025 (Oral).**
   - **`pyKT`** (MIT, **441 ★**) mide la otra mitad del problema: el estado de conocimiento del alumno, no la calidad de la respuesta del tutor.

   **La formulación correcta del gap:** el estándar **existe, está publicado en los dos venues principales de NLP, y nadie lo está usando en producción.** 42 y 32 estrellas para benchmarks premiados en EMNLP y NAACL es señal de que la academia los produjo y la industria no los adoptó. Eso sigue siendo una oportunidad — pero es "integrar y operacionalizar lo que ya existe", no "construir lo que falta", y son propuestas muy distintas. Ver el patrón **P10**.

   ⚠️ **Y hay que leer la licencia:** MathTutorBench es CC BY 4.0 y UnifyingAITutorEvaluation es **CC BY-SA 4.0** (*share-alike*). El uso típico en un engagement — derivar un benchmark propio con datos del cliente — es exactamente lo que dispara la obligación del share-alike.

   ~~**Lo que sigue sin existir:** un benchmark pedagógico **fuera de matemática**.~~ → **SUB-GAP CERRADO EN EL PASE 5 DEL 2026-09-30.** El pase 4 escribió que los tres artefactos eran de matemática y que "para lengua, ciencias sociales o formación profesional no hay nada". Buscando por *escenario educativo* en vez de por dominio aparecen tres más:

   - **`EduBench`** (https://github.com/ybai-nlp/EduBench, **MIT**, 29 ★, **ACL 2026**) — **transversal a materia por diseño**: organiza la evaluación en **9 contextos educativos** y 4.000+ situaciones sobre 12 dimensiones, con cinco escenarios de alumno y **cuatro de docente** (generación de preguntas, **Automatic Grading**, generación de material, contenido personalizado). Publica dataset y modelo.
   - **`EduGuardBench`** (https://github.com/YL1N/EduGuardBench, ⚠️ **sin licencia declarada**, 4 ★) — evalúa al modelo *como docente simulado*, lo cual es independiente de la materia. 14 modelos.
   - **`EduFrameTrap`** (arXiv 2605.14604, TUM/MCML) — **seis materias**: matemática, física, **economía, química, biología y ciencias de la computación**. Sin repo localizable.

   **Y el dato de licencia es la mejor parte:** `EduBench` y `SafeTutors` son **MIT**. Hasta el pase 4 toda la capa de evaluación pedagógica tenía fricción (CC BY, CC BY-SA con *share-alike*). Ahora se puede armar el stack de evaluación completo sin pasar por legal.

   ~~**Lo que sigue sin existir, más acotado:** benchmark pedagógico específico de **lengua, ciencias sociales o formación profesional**.~~ → **ACOTADO OTRA VEZ EN EL PASE 6 DEL 2026-09-30: cae *lengua*, quedan ciencias sociales y FP.**

   **`L2-Bench`** — *An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education* (arXiv 2607.08842), de **Oxford University Press** con la Universidad de Oxford. Según las fuentes localizadas: **1.000+ tareas docentes auténticas**, marco de **12 competencias docentes con 31 sub-habilidades**, rúbricas con descriptores expertos, y validación de **200+ educadores de 45+ países**. Código de evaluación **MIT ✅**; dataset y rúbricas **CC BY-SA 4.0 ⚠️**. Paper metodológico compañero: arXiv 2603.20088.

   🔴 **Marcado como no verificado, y es una diferencia importante respecto de todo lo demás de este pase.** El proxy de egreso de la sesión bloquea `arxiv.org`, `huggingface.co` y `oup.com` — los tres lugares donde vive L2-Bench. Licencia, tamaño y autoría vienen de resultados de búsqueda, **no de leer el artefacto**. Se registra porque un benchmark de segunda lengua producido por OUP con 200+ validadores es exactamente lo que el sub-gap pedía, y omitirlo sería peor que anotarlo con la advertencia; **pero hay que abrirlo y confirmarlo antes de cualquier entregable**.

   Si se confirma, hay algo más que anotar: **L2-Bench sería el primer benchmark de esta capa producido por una editorial educativa comercial y no por un laboratorio académico.** Eso importa para el diagnóstico central de este gap — significa que la medición pedagógica empezó a tener demanda de mercado y no sólo interés de investigación.

   **Lo que sigue sin existir, tercera acotación:** benchmark pedagógico de **ciencias sociales** y de **formación profesional** (ver el **gap 10**, nuevo en este pase, que mide el vacío de FP con números). Y el diagnóstico central del gap 1 **no cambia**: el estándar existe, está publicado en los venues principales, y sigue sin adoptarse en producción.

   **Medido otra vez en el pase 7 del 2026-10-01 — ciencias sociales no se cierra, y ahora se sabe por qué no se cierra solo.** Buscando el benchmark pedagógico de ciencias sociales aparece **`ProHist-Bench`**, dentro de **`ABench`** (https://github.com/inclusionAI/ABench, **Apache-2.0** ✅, 30 ★): **400 preguntas** núcleo en 4 tipos de tarea con **10.891 rúbricas redactadas por historiadores** sobre **9 dimensiones de capacidad** (extendida: 504 preguntas), sobre materiales del examen imperial chino. Paper: arXiv 2604.24690.

   **No cierra el sub-gap, y la distinción es exactamente la que este gap viene sosteniendo desde el pase 4:** ProHist-Bench mide si el modelo **sabe hacer investigación histórica**, no si **sabe enseñar historia**. Es un benchmark de dominio, no pedagógico — la misma diferencia por la que `MathTutorBench` no mide si el modelo resuelve la ecuación sino si andamía al alumno que no la resuelve.

   **Lo que sí aporta, y no es poco:** 10.891 rúbricas de expertos con licencia **Apache-2.0** es la pieza más cara de construir en cualquier evaluación. Para un engagement de humanidades sirve como **capa de exactitud factual** debajo de una capa pedagógica que hay que traer aparte (`UnifyingAITutorEvaluation` para la taxonomía, `SafeTutors` para el daño). Lo que no se puede es presentarlo como evaluación de enseñanza.

   ⚠️ **Y pega otra vez en el gap 4:** `inclusionAI` es la organización open source de **Ant Group** — verificado en el perfil (`inclusion-ai.org`, 68 repos). La única pieza de evaluación en humanidades con licencia limpia que encontró esta KB es, también, china.

   **Dos benchmarks de seguridad más en este pase, los dos sin repo localizable:** **EduZone** (arXiv 2608.02024, 2026-08-03, **KAIST** → APAC) — **6 categorías de riesgo y 28 subcategorías**, cubre **alumno y docente**, dataset de **2.600 prompts adversarios single-turn + 2.600 multi-turn**, y reporta que los guardrails existentes no cubren los riesgos específicos de educación ni el multi-turn dinámico; y **AIriskEval-edu** (arXiv 2607.01934), riesgo en explicaciones educativas mediadas por AI en K-12. 🔴 **Sin verificar de primera mano: `arxiv.org` sigue bloqueado por el proxy en este pase.**

   **Lo que sigue sin existir, cuarta acotación:** benchmark **pedagógico** de **ciencias sociales** y de **formación profesional**. El diagnóstico central del gap 1 **no cambia** en siete pasadas: el estándar existe, está publicado en los venues principales, y sigue sin adoptarse en producción.
2. **LATAM produce agentes educativos, pero ninguno sale de la fase cero.** *Refinado en el pase 2 del 2026-09-30: antes decía "cero repos".* Buscando explícitamente en español y portugués aparecen iniciativas reales y técnicamente ambiciosas — `H1bertto/professor-agent` (Brasil, MIT, **0 ★**) y `ANTONIOALGMAR/StudyAgent` (Brasil, **sin licencia**, 2 ★, tutor multimodal local completo sobre Ollama) — y **ninguna pasa de 2 estrellas**; una no tiene licencia, así que no es reutilizable. `studyield/studyield` **da 404**. Latam-GPT sigue siendo un modelo fundacional, no un framework de tutoría. La conclusión no cambia y el diagnóstico mejora: **no falta interés de constructores, falta masa crítica y gobernanza de proyecto** (empezando por poner una licencia). Espacio abierto, y ahora con evidencia de que hay gente intentándolo.

   **Actualizado en el pase 4 del 2026-09-30 — el gap baja de categoría.** Buscando en español apareció **TutorIA** (https://github.com/LabSirius/TutorIA, **MIT**, **0 ★**, Python): tutor conversacional autónomo **integrado dentro de Open edX**, con TTS, avatar animado, dashboard docente y persistencia de contexto, apuntado a **educación superior rural en Risaralda, Colombia**. Materias iniciales: Programación I e Introducción a la Matemática.

   Sigue teniendo **0 estrellas**, así que el gap de tracción se mantiene intacto. Lo que cambia son las **dos causas** que el pase 2 había identificado:

   | Diagnóstico del pase 2 | Estado en el pase 4 |
   |---|---|
   | "Falta gobernanza de proyecto, empezando por poner una licencia" | **Resuelto en este caso:** TutorIA es MIT |
   | "Falta respaldo institucional" | **Resuelto en este caso:** Grupo Sirius, **Universidad Tecnológica de Pereira** (`sirius.utp.edu.co`; el perfil de la organización declara Pereira, Colombia) |
   | "Falta masa crítica" | **Sin resolver.** 0 estrellas |

   **La lectura para un engagement LATAM:** dejó de ser cierto que la región sólo produce prototipos de autor individual sin licencia. Hay un laboratorio universitario colombiano publicando MIT e integrando contra Open edX, con un caso de uso específico (ruralidad, por eso el TTS y el avatar) en vez de un tutor genérico. **Como contraparte técnica local eso es utilizable hoy; como dependencia de producto no, y no hay que presentarlo como si lo fuera.**

   Y hay un dato de mercado del mismo pase que reencuadra el gap entero: la encuesta del Digital Education Council (30.000+ respuestas, 29 instituciones) da **92% de estudiantes y 79% de docentes de LATAM usando AI**. **La región no tiene un gap de adopción; tiene un gap de oferta open source propia.** Ver `intel/market.md`.

   **Medido otra vez en el pase 6 del 2026-10-01, y da lo mismo con más evidencia.** Búsqueda directa en GitHub en español (`tutor educativo IA`): **20 repos, ninguno pasa de 1 estrella.** Los más sustantivos, todos nuevos para esta KB y todos en fase cero:

   | Repo | País | Qué es | Stars |
   |---|---|---|---|
   | `dev-deivis/aprendia` | México | Tutor Flutter para **adultos en rezago educativo** que terminan primaria/secundaria vía **INEA**. Voz, avatar animado, y una decisión de diseño correcta: **guía en vez de dar la respuesta** | 0 |
   | `i-fretes/tutor-fpuna-ai` | Paraguay | Tutor de Aritmética y Álgebra para el ingreso a **FP-UNA**, con RAG y **verificación simbólica** del resultado. Creado 2026-09-25 | 0 |
   | `yago-jnp/kez.ia` | Brasil | Juez online + tutor de IA para Python y algoritmos: evalúa código, explica errores y personaliza listas de ejercicios | 0 |
   | `matematiccj/red-funciones-lineales` | Sin país declarado (español) | Recurso STEAM de funciones lineales con **tutor socrático offline** | 0 |

   **Lo que agrega el pase 6 al diagnóstico, y es lo más útil del gap.** Las causas del pase 2 eran "falta licencia, falta respaldo institucional, falta masa crítica". El pase 4 mostró con TutorIA que las dos primeras se resuelven caso por caso. El pase 6 muestra algo más específico: **ninguno de estos proyectos es un tutor genérico — cada uno ataca un problema local real y bien elegido** (rezago educativo adulto en México vía INEA, ingreso universitario en Paraguay, ruralidad en Colombia con TutorIA). **El déficit de la región no está en identificar el problema ni en diseñar el producto. Está en la continuidad y en la comunidad:** nadie los sostiene después del primer release.

   **Y eso cambia qué puede aportar Globant acá:** no "construir el tutor que falta" —hay varios, y bien pensados— sino **aportarle a uno de ellos la ingeniería, la gobernanza de proyecto y la evaluación que le falta**. Sale más barato, es más defendible ante un ministerio, y produce un caso regional con autoría local en vez de una importación.

   **Medido una tercera vez en el pase 7 del 2026-10-01, y el diagnóstico del pase 6 se confirma con el mejor ejemplo posible.** Búsqueda en GitHub por `tutor IA educativo español`: **197 resultados, techo de 3 estrellas entre los que realmente son tutores.** Nuevos respecto del pase 6:

   | Repo | Qué es | Stars | Estado |
   |---|---|---|---|
   | `Javi111003/OlivIA-RAG` | Tutor RAG para preparar el ingreso universitario en matemática | **1** | ⚠️ **sin licencia**; último movimiento 2025-07 |
   | `jrobador/finetuned-llama3.2-3B_mat-IA` | Llama 3.2 3B afinado para matemática; **segundo puesto del *Llama Impact Pan-LATAM Hackathon*** | **3** | 🚫 **sin actividad desde 2024-11** |

   **El segundo es la ilustración exacta del diagnóstico:** un finalista de un hackathon regional de Meta, con reconocimiento público, **abandonado dos meses después**. No falta talento, ni idea, ni visibilidad. **Falta continuidad.** El déficit de LATAM no está en el día 1 de un proyecto, está en el día 90.

   **Y hay un cambio institucional del pase 7 que reencuadra la oportunidad entera:** el **Observatorio de IA en Educación para América Latina y el Caribe** de UNESCO (lanzado **2026-04-14** en la sede de la CEPAL, Santiago) crea por primera vez una **contraparte regional permanente** con CAF, CENIA, Cetic.br/NIC.br, Fundación Ceibal, Tec de Monterrey, ProFuturo e IRCAI. Ver `intel/market.md`. Eso es precisamente el tipo de estructura que puede sostener un proyecto más allá del día 90 — que es lo único que a estos repos les falta.

   **Medido una cuarta vez en el pase 8 del 2026-10-01 — y por primera vez el gap tiene una geografía adentro.** Buscando accesibilidad y educación especial (ángulo que esta KB nunca había usado) aparecen **dos repos chilenos**, y no son dos proyectos de autor suelto:

   | Repo | Licencia | Stars | Commits | Anclaje normativo nacional |
   |---|---|---|---|---|
   | `marcorojasb/tero` | **MIT** ✅ | 0 | **111** | MINEDUC, **Decreto 83** (educación especial), **Ley 21.719** (protección de datos) |
   | `ronda-ai/Ronda-App` | GPL-3.0 ⚠️ | 3 | 17 | **Marco para la Buena Enseñanza (MBE)** |

   **Lo que esto agrega al diagnóstico, que venía siendo «falta continuidad, no talento».** Los dos están anclados a **instrumentos normativos nacionales reales** en vez de a un currículo genérico, y `tero` además resuelve bien el problema de gobernanza que los pases anteriores señalaron: es MIT, tiene 111 commits, y su postura de diseño —*el agente propone, el docente decide*, sin escritura de archivos sin aprobación humana— es **la arquitectura que la regulación de EE. UU. está forzando** (ver gap 12). Un repo de 0 ★ de Chile llegó por restricción local a la misma conclusión de diseño que Delaware y Nueva York están imponiendo por norma.

   **Y junto con lo que la KB ya tenía, Chile se está volviendo el nodo técnico de LATAM:** Latam-GPT (CENIA), el **Observatorio UNESCO lanzado en la sede de la CEPAL en Santiago**, y ahora dos repos educativos con anclaje normativo. Ninguno tiene tracción — el gap 2 **no se cierra** — pero por primera vez hay una concentración geográfica en vez de iniciativas dispersas, y eso cambia dónde conviene buscar contraparte. Ver `intel/market.md`.
3. **EMEA no produce tutores: produce la capa que los mide y los acredita** *(reformulado en el pase 4; antes decía "produce plataformas")*. La formulación anterior era correcta pero pobre — agrupaba todo lo no-agéntico como "plataformas". Con lo del pase 4 el patrón es más nítido y más útil:

   - **Plataformas:** OpenOLAT (Suiza), Chamilo (Bélgica/España), Richie (Francia), H5P (Noruega).
   - **Evaluación:** **MathTutorBench** (org `eth-lre`, CC BY 4.0, 42 ★, EMNLP 2025 Oral) y **UnifyingAITutorEvaluation** + AITutor-EvalKit (MBZUAI, Abu Dhabi, NAACL 2025).
   - **Esquemas de conformidad curricular:** **OpenDidactia** (España, CC BY-SA 4.0, 0 ★) — esquemas OKF para generar Programaciones Didácticas conformes a **LOMLOE** en las 17 comunidades autónomas. No es un agente: es el *formato de salida auditable* que un agente docente necesita para ser aceptable ante una inspección educativa.
   - **Skills pedagógicas:** education-agent-skills (UK, CC BY-SA 4.0, 814 ★).
   - **Tutores, la excepción:** **OpenTutorAI-CE** (BSD-3-Clause, 107 ★) — **región cerrada en el pase 4: Marruecos**, lo que explica su soporte multilingüe árabe/francés/inglés.

   **Que EMEA produzca medición y conformidad mientras APAC produce tutores no es casualidad: es el reflejo de dónde muerde la regulación.** Para una propuesta europea eso es favorable — el artefacto local disponible es justamente el que pide el EU AI Act. Lo que EMEA no tiene es un tutor open source de escala, y hay que ir a buscarlo a APAC con el riesgo de procedencia que eso implica (gap 4).

   **Ampliado en el pase 5:** EMEA también produce **la mejor referencia teacher-facing que existe en abierto** — **`Aila`** (https://github.com/oaknational/oak-ai-lesson-assistant, **MIT**, 35 ★, **1.188 commits**), el asistente de planificación de clases de **Oak National Academy** (Reino Unido), **en producción**. Y en la capa de evaluación se suma **EduFrameTrap** (TUM/MCML, Alemania). La formulación se afina una vez más: **EMEA produce todo lo que rodea al tutor —medición, conformidad, currículo, herramientas docentes— y no produce el tutor.** ⚠️ `Aila` declara ser para uso interno de Oak: referencia de arquitectura, no base de producto.

   **África, que faltaba entera en este gap.** EMEA se venía leyendo como Europa + MBZUAI + Marruecos. Hay evidencia propia: **AfriLabs + WISE** (nov 2025, 3.875 encuestados, 47 instituciones, 199 empresas edtech), **North-West University** como primera universidad sudafricana con política oficial de AI (2026-01-15), MoU **DHET–Microsoft SA** (2025-10-07), y **N-ATLAS** (Nigeria), LLM multilingüe open source. El patrón de compra africano es **ministerio + MoU con big tech**, no adquisición institucional. Ver `intel/market.md`.
4. **La oferta de agentes está concentrada en APAC.** DeepTutor (HKU) y OpenMAIC (Tsinghua) son ~80k ★ combinadas y las dos vienen de instituciones chinas. Para un cliente con restricciones de procedencia de software, esto es un riesgo a declarar temprano, no a descubrir en due diligence.

   **Agravado y a la vez mitigado en el pase 5, y las dos mitades importan.**

   *Agravado:* la concentración ya no es sólo de agentes. Con **`OmniEdu`** (Universidad de Pekín + UCAS + Zhongguancun Academy — modelos fundacionales 4B/9B/27B) y **`EduBench`** (ACL 2026), **las cuatro capas del stack educativo open source tienen su artefacto de referencia en instituciones chinas**: modelo (OmniEdu), modelado del alumno (pyKT), agente (DeepTutor, OpenMAIC) y evaluación (EduBench).

   *Mitigado:* por primera vez hay una **ruta alternativa completa** para un cliente con restricción de procedencia — **`pyBKT`** (MIT, 281 ★, CAHLR/UC Berkeley, EDM 2021) en modelado, **`Aila`** (MIT, Reino Unido) como referencia teacher-facing, **`MathTutorBench`** (ETH Zúrich) y **`SafeTutors`** (MIT) en evaluación, y `OpenOLAT` / `Kolibri` / `Oppia` en plataforma. El pase 4 había dejado el gap en su peor momento (descubrió que también el modelado era chino); esto lo revierte parcialmente.

   **Lo que hay que decir al proponer la ruta alternativa:** existe, y **no es gratis**. Se paga en capacidad de modelo (pyBKT es BKT clásico, pyKT es deep learning con 10+ modelos DLKT) y en madurez de agente (no hay equivalente occidental a DeepTutor con 40.6k ★). La ventaja compensatoria de pyBKT es la **interpretabilidad**, que ante un regulador que pregunta por qué el sistema decidió lo que decidió vale más que la potencia.

   **Extendido a una quinta capa en el pase 7 del 2026-10-01, y acá la ruta alternativa se rompe.** Las capas chinas de referencia eran cuatro: modelo (`OmniEdu`), modelado del alumno (`pyKT`), agente (DeepTutor, OpenMAIC) y evaluación (`EduBench`). La quinta es **los datos de entrenamiento**, y el patrón es peor que en las otras cuatro:

   | Dataset de knowledge tracing | Licencia | Origen |
   |---|---|---|
   | **XES3G5M** (5,5M interacciones) | **MIT** ✅ — *el único permisivo* | **China** |
   | **EdNet** (131,4M interacciones) | ⚠️ CC BY-NC | APAC (Corea) |
   | **FoundationalASSIST** (1,7M, inglés) | ⚠️ CC BY-NC + gated | North America |

   **El único dataset de knowledge tracing con licencia permisiva es chino.** Los dos de procedencia no china son los dos NonCommercial.

   La ruta alternativa que el pase 5 armó para un cliente con restricción de procedencia (`pyBKT` + `Aila` + `MathTutorBench` + `SafeTutors`) **se sostiene en código y se rompe en datos**. Para ese cliente, entrenar con los datos propios deja de ser la opción preferible y pasa a ser **la única**, con el costo de arranque en frío que eso implica. Y se suma un dato de la capa de evaluación en humanidades: **`ProHist-Bench` / `ABench` también es chino** (Ant Group). Ver **P16**.
5. **No hay integración madura entre knowledge tracing y agentes LLM** *(el gap se mantiene; el inventario estaba incompleto — corregido en el pase 4)*. La conclusión —**nadie los cosió bien**— sigue siendo correcta y es el hueco técnico concreto del patrón P1. Lo que estaba mal era el inventario de piezas disponibles: los pases 1–3 listaban sólo `py-fsrs` (MIT, 499 ★, scheduling) y OATutor (BKT embebido en un ITS completo).

   Falta agregar la pieza central: **`pyKT`** (https://github.com/pykt-team/pykt-toolkit, **MIT**, **441 ★**, 811 commits) — librería de *knowledge tracing* profundo sobre PyTorch con **10+ modelos DLKT** comparables, **7+ datasets** con preprocesamiento estandarizado y 5 escenarios de predicción. Publicada en **NeurIPS 2022** y mantenida. Origen: **Jinan University / Guangdong Institute of Smart Education, China → APAC** (refuerza el gap 4, ahora también en la capa de modelado).

   **Por qué la corrección importa aunque el gap no se cierre:** con el inventario viejo, coser tracing a un agente parecía "implementar BKT a mano o extraerlo de OATutor". Con `pyKT` en la mesa, el trabajo es **integración de una librería MIT madura**, no investigación. Eso cambia la estimación de un proyecto de meses a semanas, y cambia lo que se puede prometer: un modelo DLKT publicado y reproducible es evidencia defendible de eficacia adaptativa ante un regulador; "el LLM decidió" no lo es. Ver el patrón nuevo **P10**.

   **Lo que sigue faltando literalmente:** un repo que exponga un modelo de knowledge tracing **como tool o servidor MCP** para que el agente consulte el estado de mastery antes de decidir qué preguntar. `tutor-mcp` (MIT, 42 ★, Go) es lo más cercano — implementa BKT y repetición espaciada detrás de MCP — pero usa su propio BKT, no una librería DLKT entrenable. **El hueco exacto es `pyKT` detrás de MCP**, y no existe.

   **Reformulado en el pase 5 del 2026-09-30 — el patrón existe cinco veces; la ingeniería, ninguna.** La afirmación "no existe" era demasiado fuerte. Buscando por la pieza técnica aparecen **cinco servidores MCP independientes** que exponen mastery a un agente: `zcsabbagh/knowledge-graph-mcp` (MIT, 1 ★, 8 commits — SM-2 + fórmula de pesos fija), `woodstocksoftware/student-progress-tracker` (MIT, 1 ★, 9 commits), `tejpalvirk/student` (MIT, 1 ★, 6 commits), `znecho9/knowledge-forest-mcp` (Apache-2.0, 0 ★, 3 commits — mastery con evidencia a libro cerrado obligatoria) y `radhepa/Teacher-MCP` (MIT, 0 ★, 2 commits).

   **Las dos lecturas, y las dos son útiles:**

   - **Señal de mercado:** cinco autores sin relación entre sí llegaron al mismo patrón en la misma ventana. El problema es real y sentido por muchos; el patrón está validado sin que Globant tenga que evangelizarlo.
   - **El hueco de ingeniería sigue intacto, y mejor documentado:** **ninguno de los cinco usa una librería de knowledge tracing entrenable** — todos implementan su propia heurística. Los tres más grandes suman **3 estrellas y 23 commits**. Verificado de primera mano en el pase 5: `pyKT` sigue en 441 ★ / 811 commits y **su documentación no menciona MCP ni interfaz de serving**.

   **Y ahora hay dos librerías candidatas, no una:** a `pyKT` (MIT, 441 ★, deep learning, APAC) se suma **`pyBKT`** (https://github.com/CAHLR/pyBKT, **MIT**, **281 ★**, 379 commits, **EDM 2021**, CAHLR/UC Berkeley — el mismo laboratorio de Zachary Pardos que produjo OATutor, que esta KB ya listaba sin haber mirado el resto del laboratorio). Para un primer engagement regulado pyBKT es probablemente la mejor elección: BKT bayesiano es menos potente que DLKT y **mucho más fácil de defender ante un regulador**.

   **El gap pasa de "nadie lo intentó" a "cinco lo intentaron y ninguno conectó la librería buena".** Es una propuesta mejor: el trabajo dejó de ser inventar el patrón y pasó a ser hacerlo bien una vez. Ver el patrón nuevo **P12**.

   **Reformulado otra vez en el pase 6 del 2026-10-01 — el problema estaba mal partido, y el trabajo pendiente es más chico de lo que la KB venía estimando.**

   Los cinco servidores MCP del pase 5 no fallaron sólo por no usar una librería de knowledge tracing entrenable. **También inventaron, cada uno, su propio almacén de eventos de aprendizaje.** Y ese almacén no hay que inventarlo: es **xAPI / IEEE 9274.1.1**, con cuatro implementaciones open source maduras que ninguna de las cinco pasadas anteriores había registrado — porque se buscaba por "agente", "tutor" y "benchmark", y esta capa se llama **Learning Record Store**.

   | Pieza del patrón | Diagnóstico hasta el pase 5 | Estado real tras el pase 6 |
   |---|---|---|
   | Almacén de eventos de aprendizaje | "cada servidor MCP se lo inventa" | **Resuelto y estandarizado.** `lrsql` (Apache-2.0, 143 ★, Postgres 14–18) o `Ralph` (MIT, 50 ★, conversión nativa de Open edX) |
   | Transporte MCP hacia ese almacén | No registrado | **Resuelto.** `learnmcp-xapi` (MIT, 15 ★) — y ya habla con los dos anteriores |
   | **Estimador de mastery entrenable detrás** | "no existe" | **Sigue sin existir.** `learnmcp-xapi` registra y recupera; **no infiere mastery** |

   **La formulación correcta del hueco, sexta versión:** no es "construir un servidor MCP de mastery" (se hizo cinco veces) ni "construir el almacén" (es un estándar con cuatro implementaciones). Es **enchufar `pyBKT` o `pyKT` como estimador detrás de un LRS que ya existe, expuesto por un MCP que ya existe**. Eso es **un componente, no una plataforma** — y cambia la estimación de un proyecto otra vez, ahora hacia abajo.

   **La lección de método, que es la tercera vez que esta KB tropieza con la misma piedra en otra forma.** El pase 3 aprendió que un gap "no existe X permisivo" hay que re-buscarlo por licencia y stack, no por categoría. El pase 6 agrega el caso complementario: **acá la consulta no estaba mal, estaba mal el mapa.** Faltaba una capa entera en el modelo mental del stack, así que nunca se buscó. Cuando un gap sobrevive cinco pasadas, conviene preguntarse no sólo *cómo* se buscó sino **si la cosa que falta tiene un nombre que uno no está usando**.

   **Completado en el pase 7 del 2026-10-01 — la pieza que falta no es sólo código, es el dataset con que se entrena.**

   Seis pasadas acotaron el gap hasta dejarlo en una sola pieza: **un estimador de mastery** (`pyBKT` o `pyKT`) detrás de un LRS que ya existe, expuesto por un MCP que ya existe. Eso sigue siendo correcto. Lo que faltaba decir es que **ese estimador hay que entrenarlo**, y que los datasets de knowledge tracing disponibles son mayoritariamente **NonCommercial** (ver el **gap 11** y el **trend 16**).

   | Pieza del patrón | Estado tras el pase 7 |
   |---|---|
   | Almacén de eventos (LRS xAPI) | **Resuelto.** `lrsql` (Apache-2.0) o `Ralph` (MIT) |
   | Transporte MCP | **Resuelto.** `learnmcp-xapi` (MIT) |
   | Librería de estimación | **Resuelto.** `pyBKT` (MIT) o `pyKT` (MIT) |
   | **Datos para entrenar la estimación** | ⚠️ **Es el cuello de botella real.** Sólo `XES3G5M` es permisivo, y es chino / matemática / tercer grado. `EdNet` y `FoundationalASSIST` son CC BY-NC |
   | Integración | **Sigue siendo trabajo propio** — ninguno de los cinco servidores MCP lo hizo bien |

   **El gap pasa de "cinco lo intentaron y ninguno conectó la librería buena" a su formulación final: la integración es trabajo de semanas y el dato de entrenamiento es trabajo del cliente.** Es la mejor versión del gap porque es la que se puede cotizar sin sorpresas: el LRS entra en la fase 1 justamente porque es el que fabrica el dataset. Ver **P16**.

   Ver el patrón nuevo **P15**.

6. **No hay agente de grading open source con tracción** *(agregado en el pase 2)*. Se buscó específicamente corrección y assessment automatizado con licencia permisiva. La capa de grading sigue siendo **propietaria**: Gradescope (Turnitin), Codio, Kangaroos AI. En abierto hay *papers* (arXiv 2601.00730, 2607.02432, 2506.07955), no repos con adopción. Consecuencia directa para propuestas: **no prometer reemplazar Gradescope; prometer orquestarlo** — por eso `gradescope-mcp` (MIT, 8 ★) vale seguirlo pese a su tamaño. Es el camino realista hacia grading agéntico hoy.

   **🔴 CORREGIDO EN EL PASE 13 DEL 2026-10-01 — el gap se parte en dos y una mitad estaba mal.** Once pasadas repitieron esta formulación. La evidencia que la sostenía era `gradescope-mcp` (8 ★), `classmoji` (83 ★, AGPL-3.0), `rubric` (0 ★) y `llmgrader` (licencia de investigación) — toda la capa medida **por el lado del agente**. Buscando por **el entorno donde el alumno hace el trabajo** aparece una pila entera que esta KB no tenía:

   | Tipo de trabajo del alumno | Estado real de la corrección open source |
   |---|---|
   | **Código, notebooks, datos, cálculo numérico** | **Resuelto, permisivo y desplegado.** `nbgrader` (**BSD-3-Clause**, 1.400 ★, **v0.9.6 del 2026-09-30**) y `otter-grader` (**BSD-3-Clause**, 161 ★, UC Berkeley DSEP), sobre `jupyterhub` (**BSD-3-Clause**, 8.300 ★), con `jupyter-ai` (**BSD-3-Clause**, 4.400 ★, ACP+MCP) como capa de agente y `ltiauthenticator` (**BSD-3-Clause**, LTI 1.3 contra Open edX/Canvas/Moodle) como puente al LMS. Implementado desde 2014 en **UC Berkeley, Cal Poly, Edimburgo y Aalto** |
   | **Prosa — ensayo, respuesta abierta, trabajo escrito** | **El gap 6 sigue intacto, y es ahí donde vive el incumbente.** Gradescope y Turnitin son dueños de esto; lo open source sigue siendo *papers* y repos pre-tracción |

   **Consecuencia para propuestas, corregida:** para un cliente de **STEM, ciencia de datos, ingeniería o formación técnica**, decirle «la corrección open source no existe, orquestemos Gradescope» es **falso y además más caro que la alternativa**. Para un cliente de **humanidades o evaluación por escrito**, la recomendación original se mantiene sin cambios. Ver el **trend 30** y el patrón **P29**.

   ⚠️ **Lo que esta corrección no dice:** nbgrader no evalúa pedagogía ni modela al alumno — autocorrige contra tests que escribió el docente. El **gap 1** (nadie usa los benchmarks pedagógicos que existen) y el **gap 5** (nadie conectó una librería de knowledge tracing entrenable) **no se tocan**.

7. ~~**No hay SIS open source permisivo y vivo**~~ → **GAP RETIRADO en el pase 3 del 2026-09-30.** El pase 2 declaró que toda la capa SIS open source era PHP y copyleft, que la única opción permisiva (**Fedena**, Apache-2.0, 547 ★) estaba **muerta desde el 2016-07-20**, y concluyó que en el lado administrativo el agente **siempre** tiene que ir afuera. **La conclusión era incorrecta y se corrige.**

   **GegoK12** (https://github.com/Gego-K12/gegok12) es **MIT** — verificado en el archivo `LICENSE` del repo, `SPDX-License-Identifier: MIT`, © 2025 GegoSoft Technologies — con **54 ★, 97 forks, 123 commits y último commit el 2026-09-23**. Está vivo, es PHP 8.4 + Laravel 12, API-first, y **tiene sistema de plugins** (`Plugin-Hello-Teacher`). O sea: en el lado administrativo el agente **sí puede vivir adentro**, como plugin, sin contaminar IP, porque MIT no impone share-alike.

   **Lo que sigue siendo cierto:** todo el SIS open source es PHP, Fedena sigue muerta y no hay que proponerla, y para RosarioSIS / openSIS / OpenEduCat (los tres copyleft, y los tres con más instalaciones reales) el agente sigue yendo afuera. **Lo que cambia:** dejó de ser "la única opción limpia" y pasó a ser "el patrón por defecto, con una alternativa".

   **La condición que hay que leer:** GegoK12 es **open-core**. De 38 módulos, 26 están en el core MIT (alumnos, admisiones, asistencia, tareas, biblioteca, staff, avisos, comunicación con padres) y **12 son Pro pagos, USD 100–250 cada uno** — entre ellos **examinación y gestión de fees**, que son justo los dos procesos que un agente querría automatizar primero. Licencia Pro lifetime por dominio con fuente incluido, no suscripción por alumno. Detalle completo en `verticals/solutions.md`.

   **Por qué este gap se sostuvo dos pasadas.** Las dos anteriores buscaron "SIS open source" y encontraron los listicles, que repiten Fedena/RosarioSIS/openSIS y no incluyen a GegoK12 porque es reciente. La lección de método: **un gap de la forma "no existe X permisivo" hay que re-buscar con la consulta invertida** — por licencia y stack ("school ERP MIT Laravel"), no por categoría. Buscar la categoría devuelve el consenso de los listicles; buscar la licencia devuelve los proyectos nuevos.


8. **La capa teacher-facing es propietaria, con una sola excepción open source** *(agregado en el pase 3)*. `intel/market.md` ya observaba que las herramientas *para docentes* son "el ángulo menos disputado" y que MagicSchool lidera ahí. Buscando el equivalente open source aparece que el segmento entero es cerrado: **MagicSchool, Brisk, Diffit, Curipod, Eduaide.AI, SchoolAI, Taskade**. ~~La única entrada open source que encontramos es **Claw-ED** (MIT, **59 ★**).~~ → **CORREGIDO EN EL PASE 5 DEL 2026-09-30.** La afirmación "una sola excepción open source" era incorrecta:

   | Repo | Licencia | Stars | Commits | Qué es |
   |---|---|---|---|---|
   | **Aila** — https://github.com/oaknational/oak-ai-lesson-assistant | MIT ✅ | 35 | **1.188** | Asistente de planificación de clases de **Oak National Academy** (nonprofit educativa británica respaldada por el gobierno), **en producción**. Next.js + Prisma/PostgreSQL con pgvector |
   | **Claw-ED** — https://github.com/SirhanMacx/Claw-ED | MIT ✅ | 59 | **778** | Agente CLI local-first. *Sin cambios en stars desde el pase 3, pero activo: v9.18.2026.1* |
   | **ai-lesson-planner** — https://github.com/saniales/ai-lesson-planner | GPL-3.0 ⚠️ | 20 | 2 | Workflow multi-agente con salida a slides MARP |

   **Lo que cambia la propuesta:** el mejor artefacto teacher-facing abierto ya no es un proyecto de autor individual — es **código de producción de una institución educativa nacional, con 1.188 commits y licencia MIT**. Como referencia de arquitectura (RAG curricular, persistencia de la conversación de planificación, generación de recursos) vale más que todo lo demás junto.

   ⚠️ **Y la condición hay que leerla:** `Aila` declara estar *"intended primarily for internal use by Oak National Academy"* — sin API estable, sin soporte, sin garantía de despliegue externo. Es **referencia, no base de producto**. Para desplegar, el candidato sigue siendo Claw-ED.

   **Lo que no cambia:** el segmento sigue dominado por propietarios (MagicSchool, Brisk, Diffit, Curipod, Eduaide.AI, SchoolAI, Taskade). Ver el patrón **P8**.

9. **Sigue sin haber grading open source con tracción, pero la categoría se movió** *(actualizado en el pase 3)*. El gap 6 se mantiene: Gradescope (Turnitin), Codio y Kangaroos AI siguen siendo propietarios y no apareció ningún reemplazo con adopción. Lo nuevo es **AI-Teaching-Agent** (MIT, **0 ★**, 30 commits): genera artefactos **Lab / Exam / Grading como DSL validado**, con revisión humana obligatoria, evaluación sandboxeada, servidor MCP y previews de examen sin respuestas. Es la primera vez que vemos la estrategia de *generar el artefacto de corrección auditable* en vez de orquestar al incumbente — y el diseño es exactamente el que piden el EU AI Act y los estatutos de EE. UU. que prohíben grading automático. **Con 0 estrellas no se usa: se sigue.** La recomendación operativa del gap 6 no cambia (orquestar Gradescope vía `gradescope-mcp`).

   **Actualizado en el pase 5 — por fin sabemos *por qué* este gap se sostuvo cuatro pasadas, y la respuesta no es que nadie lo haya construido.**

   | Repo | Licencia | Stars | Commits | Estado |
   |---|---|---|---|---|
   | `sdrangan/llmgrader` | 🚫 **PySilicon Research License** (custom, no OSI) | 2 | **240** | Autograder para ingeniería: derivaciones multi-paso y justificación abierta, rúbricas en **XML**, trazas de corrección, **servidor MCP** e **integración con Gradescope**. De Sundeep Rangan (NYU), **desplegado en un curso de maestría real** |
   | `paper-instruments/rubric` | **MIT** ✅ | **75** | 64 | Rúbricas ponderadas genéricas para LLM-as-judge. No es educativo, es la plomería |
   | `Dmoayad/essay-grader-llm` | GPL-3.0 ⚠️ | 1 | 12 | Corrección de ensayos con rúbrica + RAG + detección de plagio |
   | `eecs-autograder/autograder.io` | ⚠️ no declarada (repo de docs) | 79 | 61 | Autograding **determinista por casos de test**, Docker sandbox. U. de Michigan, **~5.000 alumnos/semestre** |

   **`llmgrader` es el hallazgo incómodo:** es de largo el grading agéntico más maduro que esta KB encontró en cinco pasadas, y su licencia es una **"PySilicon Research License" propia, © 2026 Sundeep Rangan** — verificada leyendo el archivo LICENSE, no el badge. **No es OSI y no se puede usar en un entregable.**

   **La corrección de diagnóstico, que vale tanto como un repo nuevo:** el gap no era *"nadie construyó grading agéntico"* sino **"quien lo construyó bien no lo liberó de forma reutilizable"**. Son gaps distintos y llevan a propuestas distintas.

   **La recomendación operativa se vuelve más concreta:** (1) seguir orquestando Gradescope vía `gradescope-mcp`; (2) cuando haya que construir la capa de juicio, construirla sobre **`paper-instruments/rubric`** (MIT) en vez de desde cero, aportando la pedagogía con `EduBench` y `SafeTutors`; (3) para código, **no reemplazar el autograding determinista** — el ángulo AI correcto es explicación y feedback formativo sobre tests que ya corrieron, que además esquiva de frente la prohibición de calificación automática. Ver **P14**.


10. **La formación profesional no tiene nada open source con tracción — y ahora está medido** *(agregado en el pase 6 del 2026-10-01)*. El pase 5 dejó "formación profesional" como parte del sub-gap de benchmarks pedagógicos. Buscándolo directamente, el vacío es más grande que un benchmark faltante: **es el segmento entero**.

    Búsqueda en GitHub por `vocational education AI`: **24 repos en total, el más grande con 2 estrellas.** Casi todos son trabajos de curso, portfolios o apps de autor. Los dos únicos con forma de producto:

    - `edufeedai/edufeedai` (Java, **0 ★**, 9 issues abiertos) — recuperación, evaluación y generación de feedback sobre entregas de alumnos de FP. Sin tracción.
    - `straussbastian/ai_flashcards_for_school` (Python, **1 ★**) — flashcards generadas por un agente vía **MCP** para *Berufsschule* alemana: el docente arma el bundle, la clase entra con un link de tres palabras, **sin login y sin almacenar resultados**. El diseño de privacidad es interesante y replicable; el tamaño es irrelevante.

    **Por qué este gap importa más que su tamaño aparente.** La FP es el segmento con mayor presión de reskilling en las cuatro regiones y el que más rápido compra cuando hay presupuesto público — y no tiene ni plataforma, ni agente, ni benchmark open source con adopción. Cero de tres.

    **Consecuencia directa para una propuesta de FP:** hay que **presupuestar construcción, no integración**. Es lo contrario del resto de esta KB, donde la recomendación casi siempre es componer artefactos existentes. Decirlo temprano evita comprometer plazos de integración sobre una base que no existe. La contrapartida es que **quien construya ahí no tiene competencia open source**, que es la otra cara del mismo dato.

11. **Los datasets con que se entrena el modelado del alumno son NonCommercial, y la KB no lo había mirado en seis pasadas** *(agregado en el pase 7 del 2026-10-01)*. No es un gap de oferta: es un gap de **método** de esta KB, y corrige una afirmación que los pases 4, 5 y 6 repitieron.

    Las tres pasadas anteriores verificaron la licencia de los **repos** (`pyKT` MIT, `pyBKT` MIT, `lrsql` Apache-2.0, `learnmcp-xapi` MIT) y concluyeron que el tutor adaptativo es integración de piezas permisivas. Nunca verificaron la licencia de **los datos sin los cuales esos repos no hacen nada**. Al mirarla:

    | Dataset | Licencia | Reutilizable en un entregable facturado |
    |---|---|---|
    | **XES3G5M** | **MIT** ✅ | **Sí** — pero es chino, sólo matemática, tercer grado |
    | **EdNet** (el más grande, 131,4M interacciones) | ⚠️ CC BY-NC 4.0 | **No** |
    | **FoundationalASSIST** (el único en inglés con respuestas reales) | ⚠️ CC BY-NC 4.0 + gated | **No** |

    **Lo que el gap obliga a cambiar en una propuesta:** no se puede ofrecer un modelo de mastery "entrenado sobre datasets públicos del estado del arte". Se entrena con los datos del cliente, **y hay que presupuestar el arranque en frío**. La contrapartida es que eso convierte al Learning Record Store de la fase 1 (gap 5, pase 6) en una dependencia dura del producto y no en un anexo de conformidad — que es un argumento más fuerte, no más débil. Ver **P16**.

    **La lección de método, que vale para las otras once entradas de esta lista:** verificar la licencia del repo es necesario y no suficiente. Para cualquier pieza que **se entrene** —modelos de mastery, graders, clasificadores de riesgo— hay que verificar además la licencia del dataset, y el riesgo vive ahí con más frecuencia que en el código.

12. **La educación especial y la accesibilidad son la capa peor abastecida de esta KB — lo maduro es copyleft, lo permisivo no tiene tracción, y el open source apunta a la tarea que se está prohibiendo** *(agregado en el pase 8 del 2026-10-01)*. Siete pasadas construyeron agente, modelado, evaluación, seguridad, telemetría y datos, y **ninguna buscó al alumno con discapacidad**. Buscado directamente, el vacío está medido:

   | Señal | Medición |
   |---|---|
   | Topic `special-education` | **20 repos**, techo **10 ★** — y ese techo (`SEALApplication`) está **marcado como deprecado** y es GPL-3.0 |
   | Topic `inclusive-education` | **30 repos**, techo **60 ★** (`Sign-Language-Interpreter`) — y ese techo **no tiene licencia** |
   | Búsqueda `IEP individualized education program AI` | **1 repo** en todo GitHub (`EyeEP`, 1 ★, **sin licencia**) |
   | Lo agéntico y permisivo | techo **15 ★** (`Swar-Setu`, MIT, India) |
   | Lo maduro | **todo copyleft**: OptiKey (GPL-3.0, 4.4k ★), Cboard (GPL-3.0, 759 ★) |

   **Las tres consecuencias, en orden de importancia comercial:**

   **(a) La demanda está regulada y la oferta no la sigue.** El **European Accessibility Act** rige desde el **2025-06-28** sobre plataformas de e-learning y LMS, e **IDEA** obliga en EE. UU. desde hace décadas. Es el único segmento de esta KB donde la obligación legal **ya venció** y la oferta open source sigue en fase cero. La única pieza con tracción y licencia limpia — `accessibility-agents`, **MIT, 419 ★** — **no es un repo educativo**, y por eso ninguna consulta de los siete pases anteriores la iba a encontrar.

   **(b) El open source apunta justo al paso prohibido.** Lo poco que hay de educación especial agéntica apunta a **redactar o gestionar el IEP** (`EyeEP`; el parsing de IEP/504 de `Teacher-Hub`). La guía de **Delaware** prohíbe usar AI para objetivos de IEP, evaluación docente y calificación subjetiva; el marco de **Nueva York** prohíbe usar AI para desarrollar planes **IEP o 504**. **Un producto que redacta IEPs es invendible en los distritos más grandes de EE. UU.** Lo vendible es el resto del flujo con el docente como autor — patrón **P18**.

   **(c) Falta la pieza del medio, y es la que el cliente pide.** `accessibility-agents` resuelve acceso técnico; `Cboard` y `OptiKey` resuelven el dispositivo. **No existe en abierto la pieza que conecta la acomodación declarada de un alumno con la adaptación automática del material.** Eso no es investigación — es integración sobre piezas MIT que ya existen — pero hoy no está hecho por nadie.

   **El detalle de licencia que hay que mirar antes de cotizar:** `Teacher-Hub` declara *«MIT License — free for educational and non-commercial use»*, y **las dos mitades se contradicen** (MIT permite uso comercial). Segunda vez que esta KB encuentra una declaración de licencia que el texto no sostiene. Leer el `LICENSE` y pedir aclaración por escrito antes de cualquier entregable.

   **Lo que sí cambia respecto del gap 2:** de los repos nuevos de este pase, **dos son chilenos** — `tero` (MIT) y `Ronda` (GPL-3.0) — y los dos están anclados a instrumentos nacionales reales (Decreto 83, Ley 21.719, Marco para la Buena Enseñanza) en vez de a un currículo genérico. Ver la actualización del gap 2 y `intel/market.md`.

13. **Ningún agente open source emite ni consume credenciales verificables — el stack del alumno y el stack de la credencial no se tocan** *(agregado en el pase 9 del 2026-10-01)*. Se buscó explícitamente. Ninguno de los 25+ agentes de la tabla principal de `agents/top.md` escribe un Open Badge ni una credencial W3C VC, y ninguna de las ocho piezas de la capa de credenciales tiene interfaz de agente ni servidor MCP.

    **Por qué este gap es mejor noticia que los anteriores.** Las dos puntas existen y son **MIT**: del lado de la decisión, `pyBKT` (281 ★) y `pyKT` (441 ★) sobre un LRS conforme (pase 6); del lado de la emisión, `issuer-coordinator`, `verifier-plus` y `learner-credential-wallet`. Falta **el pegamento**, y el pegamento es una regla de umbral más un mapa de competencias —no es investigación. La pieza que traduce objetivos de aprendizaje a vocabulario **ESCO/ISCO** también existe y es MIT (`esco-skill-extractor`, 32 ★).

    **La formulación precisa del gap, para que la próxima pasada lo mida y no lo repita:** no falta tecnología, falta **un artefacto que convierta una estimación de dominio en una credencial verificable** con el umbral declarado y auditable. Eso es exactamente **P19**, y es el patrón más corto de construir de los tres que agrega este pase.

14. **El stack europeo de credenciales salió de GitHub y esta sesión no puede verificarlo** *(agregado en el pase 9 del 2026-10-01)*. No es un gap de oferta: es un **gap de verificación**, y se declara en vez de callarlo porque afecta directamente a cualquier propuesta en EMEA.

    Los dos repos de la Comisión Europea —`european-digital-credentials` (Issuer, Viewer, Wallet; EUPL-1.2, 6 ★, 31 commits) y `European-Learning-Model` (EUPL-1.2, 54 ★, 199 commits)— están **archivados** (2024-02-02 y 2024-02-14) y declaran, textual: *«For the latest versions go to: https://code.europa.eu/qualifications-courses-and-credentials/»*.

    **`code.europa.eu` está bloqueado por el proxy de egreso de esta sesión** (`EGRESS_BLOCKED`, verificado). Así que del stack europeo de credenciales esta KB puede afirmar **sólo lo que quedó archivado en GitHub**: que existe, su licencia EUPL-1.2, su modelo de datos compatible con W3C VC, y que el código vivo está en otro lado. **Versión actual, estado de mantenimiento y licencia vigente no están verificados.**

    **La consecuencia de método, que generaliza.** El pase 6 dejó escrito que *el proxy de egreso decide qué se puede afirmar*, y el pase 7 agregó que *también decide qué se puede cerrar*. Este pase agrega la tercera forma: **también decide qué regiones se pueden cubrir bien.** El stack europeo de credenciales es, muy posiblemente, la oferta más relevante del mundo para P19 en EMEA, y es la que esta sesión no puede mirar. Un cliente europeo exige abrir `code.europa.eu` **antes** de cotizar.


15. **Ningún puente agente↔contenido curricular tiene tracción, y el único que existe declara mal la licencia de lo que
    sirve** *(agregado en el pase 10 del 2026-10-01)*. Se buscó explícitamente un servidor MCP o adaptador que le dé a un
    agente acceso a contenido curricular abierto. Hay **dos**, y los dos son fase cero:

    | Repo | Licencia | Stars | Commits | Problema |
    |---|---|---|---|---|
    | `pythpythpython/openstax-mcp-server` | **MIT** (código) ✅ | **1** | 7 | Sirve 40+ libros de OpenStax con búsqueda semántica y generación de notebooks. 🔴 **Declara en su README que el contenido es CC BY 4.0; el `LICENSE` de los bundles de OpenStax en GitHub dice CC BY-NC-SA** (3 de 3 títulos verificados) |
    | `moarshy/mcp-tutor` | 🚫 **sin licencia** | **0** | 26 | Convierte repositorios de **documentación técnica** en cursos con DSPy. No es currículo escolar. El repo sólo dice: *«This project is experimental and intended for educational and research purposes»* |

    **Es exactamente la misma forma que el pase 6 encontró en telemetría y el pase 9 en credenciales:** la capa existe desde
    hace años, el estándar existe, y **el puente hacia el agente es un repo de una estrella**. Va tres capas seguidas con el
    mismo diagnóstico, y eso ya no es casualidad: **el trabajo que falta en educación abierta no es construir capas, es
    conectarlas.** Para Globant es el hueco más barato de llenar y el más defendible de cobrar — es integración verificable,
    no investigación.

    **Y hay un segundo hueco adentro del mismo gap:** ninguno de los **26 agentes** de la tabla principal de `agents/top.md`
    **emite el metadato de licencia del material que genera o deriva**. El agente produce el artefacto sin la pieza que lo
    hace usable ante un tercero — el mismo patrón que el gap 13 encontró con las credenciales.

16. **La capa de descubrimiento de contenido abierto es NonCommercial a nivel de metadato, así que el catálogo está bloqueado
    aunque el contenido no lo esté** *(agregado en el pase 10 del 2026-10-01)*. **OER Commons**, de **ISKME**, es la
    biblioteca de referencia de OER (catálogo buscable K-16). **ISKME comparte el metadato del catálogo con licencia
    NonCommercial**, por decisión explícita de tratar la educación como bien público.

    **Consecuencia directa:** no se puede construir un recomendador curricular, un buscador ni una capa de *discovery*
    comercial sobre ese catálogo. Y el catálogo es precisamente lo que uno querría para no curar a mano. **El cuello de
    botella no es el contenido: es el índice.**

    **Lo que queda como camino, y hay que decirlo en la propuesta:** curar un corpus propio y acotado al dominio del cliente,
    con manifiesto de licencia por ítem (**P22**), guardado en un repositorio permisivo (`DSpace`, BSD-3-Clause) e ingestado
    con herramienta permisiva (`LibreTexts/shapeshift`, MIT). Sale más caro que apoyarse en el catálogo abierto, **y es la
    única variante que se puede facturar.**

17. **La licencia declarada por el editor del contenido no es verificable desde esta sesión, y es la mitad que falta de la
    contradicción del trend 22** *(agregado en el pase 10 del 2026-10-01)*. No es un gap de oferta: es un **gap de
    verificación**, y se declara porque afecta a la afirmación más accionable del pase. Están **bloqueados por el proxy de
    egreso**: `openstax.org` (catálogo con la licencia por título), `openscied.org` (que vende una **licencia comercial**
    sobre contenido abierto — señal de mercado que valía confirmar) y `support.thenational.academy` (documento de licencia de
    Oak National Academy, incluida la posible restricción geográfica al Reino Unido).

    **Lo verificado de primera mano es el lado GitHub de cada afirmación** (archivo `LICENSE` de tres bundles de OpenStax,
    README de OATutor y del servidor MCP). **Lo que falta es el lado del editor.** Antes de llevar a un cliente cualquier
    afirmación de licencia de contenido de este pase, abrir esos tres dominios y confirmarla en la fuente del editor.

18. **No existe un sistema de early warning / student success open source mantenido, en ninguna región — y es la única capa de esta KB donde la demanda está madura y la oferta es cero** *(agregado en el pase 11 del 2026-10-01)*. No es un gap de tracción como el 1 ni de licencia como el 11: es **ausencia de producto**, medida.

    **Lo que se buscó y lo que devolvió, con la sintaxis exacta para que la próxima pasada pueda repetirlo:**

    | Consulta en GitHub, 2026-10-01 | Resultado | Techo de estrellas |
    |---|---|---|
    | `topic:learning-analytics stars:>50` | **2 repos en todo GitHub** | 169 ★ — `AkihikoWatanabe/paper_notes`, un blog de notas de papers |
    | `dropout prediction student license:mit pushed:>2026-01-01` | **110 repos** | **6 ★** |

    **El estado de los tres artefactos que importan** (detalle en `agents/top.md`): `Aliipou/Student-Retention-Prediction` (MIT, 6 ★) es el tope de la capa y **entrena con datos sintéticos generados por el propio repo**, sin auditoría de fairness; `dssg/student-early-warning` (70 ★, Data Science for Social Good, Universidad de Chicago) tiene licencia **`NOASSERTION`** y **último push 2018-08-22**; `novatrix-2030/SIH-2026` ("DropGuard", Smart India Hackathon 2026) tiene el mejor stack del grupo —LightGBM + XGBoost + SHAP + Groq— y **ninguna licencia**.

    **Y el stack institucional que la capa tuvo está archivado**, verificado repo por repo en los 21 de la organización `Apereo-Learning-Analytics-Initiative`: `OpenLRS` **archivado con la descripción `Deprecated`**; `OpenDashboard-legacy` **`(Deprecated)`**; el reemplazo `OpenDashboard-ux` + `OpenDashboard-api` **creado el 2020-02-12 y abandonado dentro del mes** (1 ★ y 0 ★); `LearningAnalyticsProcessor`, que es el orquestador del pipeline, **sin push desde 2023-01-19**; y **`OpenLRW` como única pieza viva** (62 ★, ECL-2.0, push del 2026-08-04). Falta además **Student Success Plan (SSP)**, el producto de *case management* de advising de Apereo con despliegues reales (St. Petersburg College, Sinclair Community College, soporte de Unicon): 🔴 **sin repositorio localizable en 2026; el rastro público se corta cerca de 2014-2015, en SSP 2.4.**

    **Por qué este gap es el más vendible de los 19, y no el más preocupante.** En todos los demás, la ausencia de oferta acompaña a una demanda incipiente. Acá la demanda está **presupuestada**: *student success* es categoría de compra consolidada en educación superior, con incumbentes propietarios. Y las dos condiciones que normalmente bloquean un engagement **no se cumplen**: los datos de referencia son **CC BY 4.0** con uso comercial (OULAD y UCI 697, ver `repos/foundations.md`) y la base técnica existe en el core de Moodle (*Analytics API*, GPL-3.0, con el target de alumno en riesgo incluido) o sobre OpenLRW. **Lo que falta es exactamente lo que se factura: ingeniería, mantenimiento y expediente de conformidad.** Ver **P25**.

    ⚠️ **La trampa que hay que evitar al cotizar:** el número `4.424` aparece en decenas de esos 110 repos porque **es el mismo dataset portugués de hace una década**. La capa entera está entrenada sobre 4.424 alumnos de una institución europea. Para un cliente de cualquier otra región, eso es un punto de partida metodológico y **no un modelo que se pueda presentar como funcionando**.

    **Y la dimensión regional, que reencuadra el gap 2.** Esta capa falta en las cuatro regiones, pero falta distinto: **North America** tiene el mercado y su único aporte open source es de 2018 con licencia irreconocible; **EMEA** tiene la regulación que lo exige y los dos datasets CC BY; **APAC** produce el repo con mejor stack y lo abandona después del hackathon; **LATAM** produce el **método publicado y revisado por pares** —revisión sistemática de 11 estudios 2022-2026 sobre riesgo de evasión en primaria (UFPE), tesis de UNIFEI, estudios de caso en institutos federales con Random Forest y XGBoost, ausentismo como predictor dominante— **y ningún repositorio**. El gap 2 dice que LATAM produce repos sin comunidad; en esta capa produce ciencia sin código. **Son los dos lados del mismo déficit, y juntos dicen que el problema no es regional: es que nadie convierte el resultado en artefacto mantenido.**
19. ~~**Los esquemas curriculares nacionales existen, son la pieza más cara de construir, y esta KB encontró dos de casualidad en dos pasadas distintas**~~ → **GAP CERRADO EN EL PASE 14 DEL 2026-10-01.** Se ejecutó la acción que este gap pedía (buscar por país, en el idioma del país). **De las cinco candidatas, cuatro existen y están verificadas** —Brasil (`bncc-dados`, MIT+CC BY 4.0), Inglaterra (`oak-curriculum-ontology`, MIT+OGL-3.0, con **11.207 *misconceptions***), EE. UU. (`commonstandardsproject/api`, Apache-2.0, los 50 estados) y Corea del Sur (ya registrada)—; **Australia (MRAC/ACARA) existe pero su licencia no se pudo verificar** (dominio bloqueado por el proxy) y **Singapur no apareció**. Además aparecieron dos cosas que el gap no anticipaba: **el estándar CASE con implementaciones certificadas** (tendencia 33) y **que esta capa no es copyleft** (tendencia 35, que corrige la lectura regional de abajo). El inventario completo está en `repos/foundations.md`. **Lo que queda abierto pasa al gap 23.** El texto original se conserva: **Los esquemas curriculares nacionales existen, son la pieza más cara de construir, y esta KB encontró dos de casualidad en dos pasadas distintas** *(agregado en el pase 11 del 2026-10-01)*. No es un gap de oferta: es un **gap de búsqueda**, y se declara para que la próxima pasada lo cierre a propósito.

    Lo que hay, sin haberlo buscado sistemáticamente:

    | Artefacto | Región | Licencia | Contenido |
    |---|---|---|---|
    | `nmarafo/OpenDidactia` *(pase 3)* | EMEA (España, LOMLOE) | **CC BY-SA 4.0** ⚠️ *share-alike* | Esquemas de Programación Didáctica y Situación de Aprendizaje para 17 comunidades + 2 ciudades autónomas, de Infantil a Bachillerato, FP y régimen especial |
    | `DECK6/korean-elementary-learning-map` *(pase 11)* | APAC (Corea del Sur, currículo revisado 2022) | **MIT** ✅ | **620 anclas de estándares de logro, 1.956 temas, 2.293 relaciones de prerrequisito, 152 clusters**, 11 materias, grados 1-6, en JSON y RDF/Turtle con *competency questions* SPARQL y restricciones SHACL |

    **Dos pasadas separadas por ocho ciclos encontraron el mismo tipo de artefacto en dos regiones distintas, y ninguna lo estaba buscando.** Eso es evidencia de que el resto probablemente exista: el *Common Core* y los estándares estatales de EE. UU., el *National Curriculum* británico, la BNCC de Brasil, los currículos de ACARA (Australia, que `mentar` ya consume en 157 plantillas) y de Singapur. **Si están publicados en formato estructurado, cada uno vale lo mismo que estos dos: es la pieza más cara de cualquier agente docente y la que ningún cliente quiere pagar dos veces.**

    **Y la comparación entre los dos que hay es la lección de método:** el coreano es **MIT** y trae el grafo de prerrequisitos y la validación formal; el español es **CC BY-SA** y no trae ninguna de las dos. **El artefacto de APAC es mejor técnicamente y más barato legalmente**, lo cual es el espejo del gap 4 — pero acá, por una vez, la concentración en APAC juega a favor del cliente y no en contra.

    **La acción para el próximo pase:** buscar explícitamente `curriculum ontology`, `achievement standards`, `learning map` y `prerequisite graph` por país, en el idioma del país, en vez de esperar que aparezcan buscando agentes.


20. ~~**Ninguna skill educativa del mundo tiene *eval* publicada, y esta KB tiene las herramientas para medirlas sin usarlas**~~ → **GAP CERRADO EN EL PASE 17 DEL 2026-10-01**, ejecutando la acción que el **gap 26** había dejado escrita (*buscar por `SKILL.md` + dominio educativo, no por repos educativos*). Ya existe skill educativa con *eval* publicada y es **Apache-2.0**:

    - **`anthropics/k12-teacher-skills`** (https://github.com/anthropics/k12-teacher-skills, **Apache-2.0**, **541 ★**) — *«Skills and eval rubrics for K-12 teachers, co-developed with Learning Commons»*. Cuatro skills y una carpeta **`evals/`** con el framework de evaluación y cómo adaptarlo. **Nuevo en esta KB, y es el nuevo techo permisivo del canal educativo: 541 ★ contra los 299 ★ de `universal-examprep-skill`.**
    - **`learning-commons-org/agent-skills`** (https://github.com/learning-commons-org/agent-skills, **Apache-2.0**, **35 ★**) — las mismas cuatro skills del lado del consorcio, con `evals/` de rúbricas de **pedagogía, rigor, formato y andamiaje del modelo**.

    Las cuatro skills: `k12-lesson-plan-creation`, `k12-lesson-differentiation`, `k12-lesson-prep` y `k12-check-for-understanding` (chequeos formativos de 1–3 ítems para estándares de matemática, con distractores y guía docente).

    ⚠️ **Y el gap se cierra con una corrección propia incorporada, no limpiamente.** Este gap **ya enumeraba** `learning-commons-org/agent-skills` entre sus siete paquetes y lo declaraba *«texto de prompt sin versionado semántico, sin suite de regresión y sin medición de efecto pedagógico»*. **Ese repo tiene `evals/`.** El pase 17 no pudo datar la carpeta, así que **no se sabe si el pase 12 la pasó por alto o si es posterior al pase 12** — se registra la duda en vez de resolverla a favor propio. Lo inequívocamente nuevo es el repo de 541 ★.

    **Lo que el cierre de este gap NO cierra:** el **gap 26** sigue abierto. *«No hay eval publicada»* es falso desde este pase; *«la educación no ocupó el canal»* sigue siendo cierto — **541 ★ contra las 47.200 ★ de `scientific-agent-skills` (MIT) son 87×**, peor que el 58× que midió el pase 12 contra el activo *share-alike*. Y el conjunto nuevo es chico: **cuatro** skills, **K-12**, con el chequeo formativo acotado a **matemática**. El valor es la **licencia y la eval**, no la cobertura.

    *Texto original del gap, conservado:* Los **siete** paquetes pedagógicos verificados en el pase 12 —`education-agent-skills` (815 ★), `human-skill-tree` (562 ★), `universal-examprep-skill` (299 ★), `algo-sensei` (281 ★), `universal-diagnostic-tutor-skill` (234 ★), `kaogong-skill` (147 ★), `learning-commons-org/agent-skills` (35 ★)— Los **siete** paquetes pedagógicos verificados en este pase —`education-agent-skills` (815 ★), `human-skill-tree` (562 ★), `universal-examprep-skill` (299 ★), `algo-sensei` (281 ★), `universal-diagnostic-tutor-skill` (234 ★), `kaogong-skill` (147 ★), `learning-commons-org/agent-skills` (35 ★)— son **texto de prompt sin versionado semántico, sin suite de regresión y sin medición de efecto pedagógico.**

    Y lo que lo vuelve un gap y no una queja: **la capa de evaluación para medirlos ya está en esta KB desde el pase 4** —MathTutorBench, UnifyingAITutorEvaluation, EduBench, EduGuardBench— construida para **tutores con backend** y **nunca aplicada a una skill**. Las dos piezas están en el mismo repositorio de conocimiento y no se tocan.

    **Es el gap más barato de cerrar de los veinte declarados**: no requiere plataforma, dataset licenciado ni implementación de estándar certificada. Requiere correr benchmarks que ya existen contra artefactos que ya existen. Es también el diferencial de la propuesta LATAM del pase 12 (ver `intel/market.md`, `### LATAM`) y del patrón **P27**.

21. **No existe el «notebook de la prosa»: fuera de las materias ejecutables no hay capa de práctica y corrección** *(agregado en el pase 13 del 2026-10-01)*. Es el gap que abre el hallazgo principal de este pase, y se declara **junto con** la buena noticia porque sin él la buena noticia se sobrevende.

    El pase 13 encontró que para trabajo **ejecutable** —código, notebooks, datos, cálculo— la capa está resuelta, permisiva y desplegada desde 2014: `jupyterhub` + `nbgrader` + `otter-grader` + `jupyter-ai` + `ltiauthenticator`, **14.334 ★, todo BSD-3-Clause**. Funciona porque el trabajo del alumno **se puede correr**: hay un artefacto ejecutable contra el que un test se evalúa de forma determinística.

    **Para un alumno de derecho, historia, lengua, filosofía o ciencias sociales no hay análogo de nada de eso.** Buscado explícitamente en este pase, no existe un entorno open source que ofrezca, para trabajo en prosa, el conjunto que Jupyter ofrece para código: entorno de trabajo por alumno, entrega versionada, corrección parcial automática, tramo de corrección manual integrado en el mismo flujo, y conexión por LTI 1.3 al LMS.

    | Pieza del flujo | Trabajo ejecutable | Trabajo en prosa |
    |---|---|---|
    | Entorno de trabajo por alumno | **JupyterHub** (BSD, 8.300 ★) | **No existe** |
    | Entrega y recolección | **nbgrader** (BSD) | El *assignment* del LMS, sin estructura |
    | Corrección automática parcial | **nbgrader / otter-grader** (BSD) | **No existe en abierto** — Gradescope/Turnitin, propietarios |
    | Corrección manual en el mismo flujo | **nbgrader** | Rúbrica suelta, fuera de la herramienta |
    | Capa de agente | **jupyter-ai** (BSD, ACP+MCP) | `ArguLens` (Apache-2.0, **2 ★**) es lo único, y es scoring de ensayo argumentativo, no entorno |

    **Es la mitad del gap 6 que este pase no cierra, vista desde el lado de la oferta en vez del de la corrección.** Y es un gap de **ausencia de producto**, como el 18: no es que lo haya y no se adopte (gap 1), ni que la licencia moleste (gap 11). No está construido.

    ⚠️ **Y hay una razón para no apurarse a construirlo.** En EMEA (Anexo III, 2027-12-02), Corea y ahora **Vietnam** (trend 31), la evaluación automática del alumno es **alto riesgo con expediente de conformidad obligatorio**. Un entorno de corrección de prosa es exactamente eso. La forma defendible es la del patrón **P14** —calificar sin que califique el modelo— y la del **P29**: el agente explica y evidencia, el docente decide. Construir el autograder de ensayo «a secas» es construir el pasivo regulatorio.

22. **La educación especial ya tiene con qué medirse, es permisiva, y nadie la está midiendo** *(agregado en el pase 13 del 2026-10-01)*. El pase 8 abrió la capa de accesibilidad y educación especial y dejó dos conclusiones: **lo maduro es copyleft** (OptiKey 4.4k ★ GPL-3.0, Cboard 759 ★ GPL-3.0) y **lo agéntico y permisivo no pasa de 15 estrellas**. Faltaba una tercera que no se buscó: **la capa no tenía ninguna forma de evaluarse.**

    Ahora la tiene. **`SEND`**, el segundo componente de `pedagogy-benchmark` (https://github.com/AI-for-Education/pedagogy-benchmark, **MIT** ✅, 12 ★), son **223 preguntas de *Special Educational Needs and Disabilities*** tomadas de exámenes de habilitación docente, con licencia permisiva y publicadas con paper (arXiv 2506.18710).

    **Es la primera pieza de evaluación de educación especial de esta KB, y tiene 12 estrellas.** O sea: la forma del gap es la del **gap 1**, no la del 18. No falta el artefacto — **falta que alguien lo use**. Y eso lo vuelve barato de cerrar: medir un asistente de educación especial contra `SEND` es integración, no investigación.

    **Por qué importa más que su tamaño.** El pase 8 documentó que en North America redactar el IEP con AI está prohibido o restringido en varios estados, y que por eso el patrón **P18** pone el límite adelante (el agente propone, el docente decide). El problema de ese patrón siempre fue **cómo demostrarle al distrito que el asistente es competente** sin tocar la decisión protegida. `SEND` es exactamente ese instrumento: mide **conocimiento pedagógico de educación especial del modelo**, que es lo que se puede acreditar, y no la decisión sobre el alumno, que es lo que no se puede automatizar. Ver el patrón **P30**.

    ⚠️ **Los límites, y son los mismos de todo `pedagogy-benchmark`:** mide conocimiento **declarativo** (responder un examen de habilitación), no calidad de intervención con un alumno real; son 12 ★ y 5 commits, así que es vara de medición en un entregable, **no dependencia de producto**; y el paper no se pudo abrir en este pase (`arxiv.org` bloqueado por el proxy), aunque licencia, conteos y composición **sí** están verificados en la página del repo.


23. **Ningún ministerio publica su currículo nacional *como* marco CASE, y es el último tramo que falta de la capa que el pase 14 cerró** *(agregado en el pase 14 del 2026-10-01)*. Es el gap que abre el cierre del gap 19, y es chico, concreto y caro de ignorar.

    Los cuatro esquemas curriculares nacionales verificados se publican **cada uno en su propio formato**: RDF/Turtle el inglés y el coreano, JSON propio el brasileño, JSON para proveedores K-12 el estadounidense. Las implementaciones de **CASE** que existen (`OpenCASE` Apache-2.0 certificado v1.1, `compeito` Apache-2.0, `opensalt` MIT) son **herramientas de publicación sin marcos nacionales publicados en ellas**.

    **Nadie cerró el círculo.** El estándar existe, los datos existen, las dos cosas no se tocan — y es exactamente la misma forma del gap 13 (*«ningún agente open source emite ni consume credenciales verificables: el stack del alumno y el stack de la credencial no se tocan»*). **Dos capas distintas, el mismo diagnóstico: la KB tiene las piezas y nadie las conectó.**

    **Por qué es una oportunidad y no una queja:** publicar la BNCC o los estándares de un estado de EE. UU. como marco CASE conforme es trabajo de **días**, no de meses — los datos están en JSON con proveniencia y el servidor es Apache-2.0 con certificación de febrero de 2026. El resultado es un activo reutilizable en todo el país y auditable contra un estándar. Es el patrón **P31**.

24. **La capa de habla y la capa de agente no se tocan: ninguno de los 31 agentes de esta KB tiene voz** *(agregado en el pase 14 del 2026-10-01)*. Se verificó contra la tabla principal de `agents/top.md`, agente por agente: **ni DeepTutor, ni Educhain, ni OpenTutor, ni OpenTutorAI-CE, ni Bloom, ni ninguno de los demás tiene entrada ni salida de voz.**

    Y tampoco existe el puente: **no hay ningún servidor MCP que exponga evaluación de pronunciación o de fluidez lectora**, aunque el patrón está probado en esta misma KB y en este mismo pase (`bncc-mcp`, MIT, expone un currículo nacional completo por MCP).

    **Las dos mitades existen y son permisivas:** `OpenPronounce` (MIT, 85 ★) mide fonema a fonema con prosodia y corre local; los agentes de la tabla saben conversar, planificar y recordar. **Lo que no existe es el servidor MCP de cinco herramientas que los une** — y es, por tamaño de trabajo, comparable al que `bncc-mcp` ya resolvió para currículo con 14 ★.

    **Es, después del gap 20 y del pedido de licencia a `carrera-lectora`, el tercer vacío más barato de cerrar de los veinticuatro declarados**, y el único que habilita una vertical entera que esta KB no puede atender hoy: **alfabetización inicial y enseñanza de idiomas.** Sin voz, un tutor no sirve en los primeros años de escolaridad, que es donde los sistemas educativos de las cuatro regiones ponen la mayor parte del presupuesto de evaluación.

25. **Nada en el ecosistema educativo open source marca ni verifica la procedencia de lo que genera, y en EMEA eso es obligatorio en 62 días** *(agregado en el pase 15 del 2026-10-01)*. Es el gap con **fecha legal más cercana** de los veinticinco declarados, y el único que esta KB venía **vendiendo sin tener implementación**.

    **Lo que falta no es la tecnología.** La infraestructura está lista y es permisiva: **SynthID-Text** (Apache-2.0, dentro de `huggingface/transformers`, con `SynthIDTextWatermarkLogitsProcessor` y `SynthIDTextWatermarkDetector`), **MarkLLM** (Apache-2.0, 1.100 ★, 23+ algoritmos y 12 herramientas de evaluación), **c2pa-rs** y **c2pa-python** (MIT + Apache-2.0 dual, 1.907 y 344 commits).

    **Lo que falta es el puente al aula, y no existe en ninguna forma:** ni plugin de LMS, ni herramienta LTI, ni servidor MCP, ni XBlock que marque la salida de un tutor o verifique un manifiesto C2PA en una entrega. Se buscó explícitamente. Lo único que hay en el directorio de Moodle son **envoltorios de servicios propietarios** —Compilatio (plugin GPL-3.0, 821 instalaciones), Originality.ai, Copyleaks—, que además hacen lo contrario: **detectan** en vez de marcar.

    **Y la mitad forense del problema no se puede usar para cerrarlo.** La capa de detección existe, es permisiva y está publicada en ICLR, ICML y ACL (`fast-detect-gpt` MIT 434 ★, `Binoculars` BSD-3 420 ★, `RAID` MIT 216 ★, `sloptotal` MIT 39 ★) — y tiene **61,3 % de falsos positivos sobre escritura de no nativos de inglés**, **5,85 %** sobre abstracts académicos anteriores a 2018, y se rompe con paráfrasis. **Un score es evidencia, no prueba.** Ver la tendencia 36.

    **Por qué es el gap más barato con fecha más dura.** El **Artículo 50** está en vigor desde el **2026-08-02** y los sistemas ya en mercado tienen hasta el **2026-12-02** para el marcado legible por máquina del 50(2). Para un tutor construido sobre Transformers —casi cualquiera de esta KB— el lado del texto es **un `WatermarkingConfig` en la llamada de generación**. El trabajo real está en C2PA (identidad de firma, custodia de claves, validación) y en el puente al LMS. Es un proyecto de semanas, no de meses, con obligación legal detrás.

    ⚠️ **Y la deuda propia que hay que registrar:** desde el pase 4 esta KB recomienda *«vender el Artículo 50 antes que el Anexo III»* con el deadline bien puesto. **Once pasadas con la oferta escrita y cero implementación detrás.** El gap se declara con la corrección incluida para que no vuelva a pasar: **cuando la KB recomiende cumplir una obligación, tiene que nombrar el código que la cumple.**

    🔴 **Sin resolver en este pase:** la fecha de publicación del **Code of Practice** europeo sobre marcado y etiquetado aparece como **10 de junio de 2026** en una fuente y **20 de julio de 2026** en otra. `digital-strategy.ec.europa.eu`, `artificialintelligenceact.eu` e `iptc.org` están **bloqueados por el proxy de egreso**. Resolver contra la fuente oficial antes de citarla a un cliente. Lo consistente en todas las fuentes: vigencia 2026-08-02, marcado 2026-12-02, C2PA como estándar de facto del metadato en un esquema por capas.

26. **La educación no usa el canal de distribución de *skills* de agente, pero la evasión de detectores sí — en español y con licencia MIT** *(agregado en el pase 15 del 2026-10-01)*. Es la continuación medida del gap que abrió el pase 12, y le da la vuelta desagradable.

    El pase 12 midió que la vertical científica construyó en el canal de *skills* de agente una biblioteca de **47,2k ★ con MIT** mientras la educativa tiene **815 ★ y es *share-alike*** — 58× de diferencia en el canal de distribución más barato de la industria. La conclusión fue que la educación **no estaba usando el canal**.

    **Lo está usando. Del lado adversario.** **`ervin-mo/humanizar-es`** (https://github.com/ervin-mo/humanizar-es, **MIT**, 0 ★, 6 commits) reescribe texto en **español** generado por AI para que los detectores dejen de marcarlo sin cambiar lo que dice, usando **Binoculars y Fast-DetectGPT sobre Qwen2.5-0.5B** como guía local — y está empaquetado como **`SKILL.md` para Claude Code, Codex, OpenCode, Antigravity, DeepSeek Harness y Gemini CLI**. El autor declara un párrafo pasando de **100 % a 0 % de «AI»**, acota que la evidencia es **un solo ensayo** y aclara que **no está pensado para entregar trabajo calificado**.

    **No es el repo —tiene 0 estrellas— es la asimetría.** La evasión se distribuye como *skill* instalable en **seis harnesses**, en español, gratis, con los detectores de esta KB adentro. La integridad se distribuye como **plugin propietario de LMS con servicio pago detrás**. Un lado tiene costo marginal cero y alcance global; el otro tiene ciclo de compra institucional.

    **Por qué esto cierra el argumento de la tendencia 36 en vez de abrir uno nuevo:** cualquier estrategia de integridad basada en detección compite contra una herramienta de evasión que **usa el mismo detector como función objetivo** y que se instala en un comando. Esa carrera no se gana. La que sí se puede ganar es la de **procedencia**, porque marcar en el origen no es un clasificador que se pueda optimizar en contra. Ver el **gap 25** y **P33**.

    **La acción para la próxima pasada:** medir el canal otra vez, pero buscando por **`SKILL.md` + dominio educativo** en vez de por repos educativos — que es el error de método que el pase 12 ya documentó y que este pase confirma desde el otro lado. Si la evasión llegó al canal, la pedagogía puede.


27. **Ningún agente educativo open source declara una postura de privacidad, y ninguna pieza de privacidad habla educación** *(agregado en el pase 16 del 2026-10-01)*. Es un gap de doble filo y las dos mitades se midieron en este pase.

    *Mitad A — los agentes.* Se revisaron los **31** de la tabla principal de `agents/top.md` buscando una declaración de qué hacen con el dato del alumno: dónde queda, si se usa para entrenar, si se puede desplegar sin que salga de la institución. **Ninguno la tiene.** No declaran una política mala: no declaran ninguna. Lo más cercano es la capa de memoria —DeepTutor con memoria en tres capas, `learnmcp-xapi` persistiendo contra un LRS— que describe **dónde** queda el dato pero nunca bajo **qué base legal** ni con qué retención. Eso importa porque desde el **2026-04-22** la regla COPPA enmendada exige política **escrita** de retención y prohíbe la retención indefinida.

    *Mitad B — las piezas de privacidad.* Las ocho librerías maduras de la capa (26.000+ ★ combinadas, todas Apache-2.0 o MIT) son **horizontales**: ninguna trae un adaptador educativo, ni plugin de LMS, ni servidor MCP, ni ejemplo con datos de knowledge tracing. Lo específicamente educativo son cuatro repos con techo de **10 ★**, y **tres no declaran licencia**.

    **Por qué este gap es distinto a los otros 26:** no es falta de oferta ni trampa de licencia. La oferta existe, es enorme y es permisiva. **Lo que falta es un puente de integración de tamaño conocido**, y hay prueba de que es factible: `FedGKT` ya corre knowledge tracing federado sobre Flower con grafos de prerrequisitos anotados por expertos. Lo hizo **un repo de 1 estrella sin licencia**. Es el gap más barato de cerrar de esta KB y el que mejor se defiende ante un regulador. Ver **P34**.

28. **La capa de voz que el pase 14 abrió es dato biométrico regulado en Norteamérica, y esta KB la registró sin ese encuadre** *(agregado en el pase 16 del 2026-10-01)*. Es un gap de **método propio**, como el 11 y el 25, y se declara en vez de corregirlo en silencio.

    El **pase 14** abrió la capa de lectura oral y pronunciación —la primera capa de voz de esta KB— y dejó el **gap 24** anotando que ninguno de los 31 agentes tiene voz. El análisis fue íntegramente de producto: qué repos hay, qué licencia tienen, qué resuelven en primaria. **No registró que la voz de un menor ya es información personal regulada.**

    Lo que faltaba: la regla COPPA enmendada agregó los **identificadores biométricos** a la definición de información personal, y la enumeración incluye **voiceprints** junto con faceprints, huellas dactilares y de palma. **Cumplimiento exigible desde el 2026-04-22.** Si el despliegue toca **Illinois**, **BIPA** suma consentimiento escrito con daños estatutarios de **1.000 a 5.000 USD por violación** — por alumno, en un producto cuyo caso de uso natural es un aula entera.

    **Lo que no cambia:** la capa de voz sigue siendo una buena oportunidad y los repos del pase 14 siguen siendo los que son. **Lo que cambia es el presupuesto y el orden:** un piloto de lectura oral en Norteamérica necesita el consentimiento parental verificable y la política de retención **antes** del piloto, no después, y eso es alcance que el pase 14 no contabilizó. Ver **P35**, que lo empaqueta como entregable propio.

    ⚠️ **Y la generalización que conviene hacer, porque va a volver a pasar:** esta KB abre capas por *capacidad* —qué sabe hacer el software— y recién después, si alguien pregunta, por *régimen*. Pasó con el watermarking en el pase 15 (la KB vendía un deadline sin implementación) y pasó acá al revés (la KB registró una implementación sin su deadline). **Toda capa nueva que toque a un menor necesita las dos lecturas en la misma pasada.**


29. **La máquina de privacidad del LMS no habla con ningún agente, y es la tercera capa consecutiva con ese mismo diagnóstico** *(agregado en el pase 17 del 2026-10-01)*. No es un gap de oferta ni de licencia: es un **gap de puente**, del tamaño conocido, y es el tercero idéntico seguido.

    Lo que existe y está maduro: el **Privacy API** de Moodle en el núcleo, que **obliga a todos los plugins** —incluidos los de terceros— a declarar qué dato guardan y a saber exportarlo y borrarlo, más `tool_dataprivacy` (flujo de pedidos, delegado de protección de datos, retención) y `tool_policy`. Y el **user retirement** de Open edX: seis scripts verificados por nombre más `lms/djangoapps/bulk_user_retirement` (API REST de retiro masivo), que alcanza LMS, foros, credenciales y las demás IDAs.

    **Lo que no existe, buscado explícitamente en este pase:** ningún servidor MCP, ninguna herramienta LTI, ningún plugin publicado que conecte un agente al Privacy API de Moodle o al retiro de Open edX. Y —la pieza más chica y más vendible— **ningún `privacy provider` de referencia para un plugin de AI**, que es justamente lo que el núcleo de Moodle exige de cualquier plugin que guarde dato del alumno.

    **Por qué es la tercera vez:** el pase 15 encontró la misma forma en procedencia (SynthID-Text y C2PA existen y son permisivos; el puente al aula no existe) y el pase 16 en privacidad horizontal (ocho librerías maduras, 26.000+ ★, ningún adaptador educativo). **Tres capas seguidas donde la infraestructura está resuelta y lo que falta es integración de tamaño acotado.** Eso ya no es una coincidencia de tres capas: es la descripción del mercado en el que Studios entra. Ver **P36**.

    ⚠️ **Y la mitad que este pase no pudo cerrar:** no se ubicó en abierto un toolset de retiro equivalente para **Canvas** (AGPL-3.0, 6.9k ★). Se declara **no encontrado, no inexistente** — no se auditó el árbol completo del repo en este pase.

30. **Ninguna pieza open source puede probar con qué dato se entrenó un modelo educativo, y California acaba de convertir eso en el requisito que decide si el modelo es legal** *(agregado en el pase 17 del 2026-10-01)*. Es el gap con la **consecuencia arquitectónica más directa** sobre los patrones propios de esta KB, y el primero que nace de una ley ya firmada en lugar de una fecha futura.

    **El requisito.** **California AB 1159**, firmada el **2026-09-13**, prohíbe usar información cubierta del alumno —incluidos **identificadores únicos persistentes**— para **entrenar AI generativa o desarrollar modelos**, *salvo* que el uso sea **estrictamente en función de un propósito educativo y en beneficio de la institución educativa correspondiente**. La **HESIPA** extiende el régimen a **educación superior** desde el **2027-07-01** (~2,9 millones de estudiantes).

    **Lo que falta, y se buscó:** no hay en abierto ninguna pieza que produzca **procedencia del dato de entrenamiento a nivel de alumno y de institución** — ni *manifest* por corrida de entrenamiento, ni atestación de qué registros entraron, ni forma de demostrar que un modelo entrenado se benefició *de esa* institución y no de un agregado multi-institución. El **Privacy API del LMS no alcanza**: borra el registro, **no el modelo**.

    🔴 **Y le pega a dos patrones propios.** **P1** (tutor adaptativo con retención real) y **P16** (entrenar el estimador de *mastery*) se apoyan en entrenar modelado del alumno con dato del alumno. La arquitectura por defecto de la industria —un modelo central entrenado con dato de muchas instituciones para servir a todas— **no cae obviamente dentro de la excepción**. Esta KB tiene que dejar de ofrecer P1 y P16 en California sin la cláusula de procedencia adelante.

    **La buena noticia, y es que la arquitectura ya estaba elegida antes de conocerse la ley.** La excepción es exactamente lo que el **aprendizaje federado** y el **entrenamiento on-premise** permiten defender: el dato no sale de la institución y el beneficio es de la institución. El pase 16 abrió esa capa (**P34**) **dieciocho días después** de que se firmara la ley que la vuelve obligatoria en el mercado educativo más grande de EE. UU., y sin registrarla. Lo que falta no es la arquitectura: es **la evidencia**. Ver **P37** y la tendencia **43**.


31. **La capa que borra la influencia del dato sobre el modelo es grande, madura y permisiva, y no menciona educación en ninguna parte** *(agregado en el pase 18 del 2026-10-01)*. Este gap **reemplaza la formulación del gap 30 por el lado del modelo** y nace de ejecutar la acción que el pase 17 dejó escrita.

    **Lo que se encontró, y la predicción del pase 17 era correcta.** Buscando por `machine unlearning` —el término que el pase 17 anotó como no buscado— aparece una capa de **2.700+ estrellas combinadas** y **toda permisiva**: `tamlhp/awesome-machine-unlearning` (**MIT, 970 ★**), `jjbrophy47/machine_unlearning` (965 ★, **sin licencia declarada**), `chrisliu298/awesome-llm-unlearning` (**Apache-2.0, 627 ★**), `locuslab/open-unlearning` (**MIT, 607 ★**, 12 métodos, TOFU/MUSE/WMDP), `Data-Provenance-Initiative/Data-Provenance-Collection` (**Apache-2.0, 281 ★**), `OPTML-Group/Unlearn-Saliency` (**MIT, 154 ★**, ICLR 2024 Spotlight), `cisco-ai-defense/model-provenance-kit` (**Apache-2.0, 104 ★**) y `Harry24k/machine-unlearning-pytorch` (**MIT, 12 ★**, NeurIPS 2025).

    **Lo que falta.** **Ninguna menciona educación, dato de alumno ni knowledge tracing.** Verificado buscando los términos en los dos agregadores grandes: cero apariciones. Y el único trabajo específico de la industria —**PrivacyCD**, arXiv **2511.03966**, que se declara *el primer estudio sistemático de data unlearning para modelos de cognitive diagnosis* y aporta el algoritmo **HIF**— **no publica código**. Es la tercera capa de esta KB donde la pieza más específica es la que no publica, después de contenido curricular (pase 10) y predictiva (pase 11).

    **Por qué este gap es más barato de lo que parece, y es una conclusión de ingeniería.** Los dos estimadores de *mastery* de esta KB se comportan distinto: **`pyKT` es PyTorch** → `torchunlearn` y `SalUn` son aplicables en principio, y es integración con riesgo técnico; **`pyBKT` no es PyTorch** (BKT por EM) → ninguna librería lo alcanza, y la respuesta correcta **no es unlearning sino reajustar sin el alumno**, que para BKT es barato y además es ***exact unlearning*** — la garantía más fuerte que existe. **Mejor resultado legal por menos trabajo.** Ver **P38**.

    🚫 **El barrido regional de esta capa, declarado en vez de omitido:** **North America** concentra la oferta (`locuslab`/CMU, `OPTML-Group`/Michigan State, `cisco-ai-defense`, `Data-Provenance-Initiative`/MIT Media Lab); **APAC** es segunda y tiene lo único educativo (`torchunlearn` Corea, `tamlhp` Australia, autores de PrivacyCD); **EMEA** y **LATAM**: **ninguna pieza encontrada**, declarado como *no encontrado, no inexistente*. El caso de EMEA es el llamativo: es la región donde el **derecho de supresión del GDPR art. 17** es directamente exigible, y no tiene oferta propia de la tecnología que lo cumple.

    ⚠️ **Nivel de evidencia:** los repos se verificaron de primera mano. Los metadatos de los papers vienen de **snippets concordantes**, no de la fuente primaria: `arxiv.org` está bloqueado por el proxy de esta sesión (igual que `blogs.cisco.com` y `helpnetsecurity.com`). Ver el gap 17.

32. ~~**Nada conecta el pedido de borrado del LMS con el borrado en el modelo**~~ → ✅ **CERRADO EN EL PASE 19 DEL 2026-10-01, REFUTANDO LA HIPÓTESIS DEL PASE 18** *(agregado en el pase 18 del 2026-10-01)*.

    **El pase 18 dejó escrita «la hipótesis más barata que esta KB tiene abierta»:** que el Privacy API **emite un evento al aprobar un pedido** y que, si ese evento es observable, el puente sería un `db/events.php` de diez líneas. **Se midió sobre el árbol real de `moodle/moodle` (`main` = 5.3rc1) y la hipótesis es falsa en su dirección:**

    - `public/admin/tool/dataprivacy/db/events.php` registra **exactamente un** observer, y va **hacia adentro**: escucha `\core\event\user_deleted` para **crear** un pedido de borrado (`user_deleted_observer::create_delete_data_request`, gated por la config `automaticdeletionrequests`). **Es el sentido contrario al que hacía falta.**
    - **`tool_dataprivacy` no emite ningún evento.** Recorridos los **187 archivos** del subárbol: **cero** llamadas a `trigger()`.
    - `api::update_request_status()` —por donde pasa `approve_data_request()`— es **una escritura de base de datos y nada más**. Sin evento, sin hook, sin notificación.
    - *Control negativo:* el mismo `api.php` tiene **1.678 líneas** y `approve_data_request()` está en la línea **642**. El archivo existía y el grep era válido: **la ausencia es real.**

    **Lo que el gap deja como resultado utilizable, y es más valioso que un «sigue abierto»:** el puente **no puede ser un observer**, y por lo tanto hay exactamente dos formas de construirlo (ver **P40**) — **(a)** sondear `tool_dataprivacy_request.status`, la única superficie observable que existe, o **(b)** disparar desde afuera vía web-service. **Eso convierte el gap en alcance cotizable con mecanismo conocido**, que es justo lo que un gap debería producir. Lo que queda de investigación abierta se reformuló como **gap 34**.

    ⚠️ **Y lo que este gap no promete** (se conserva del pase 18, sigue vigente): para deep knowledge tracing el *unlearning* es **aproximado** y queda residuo medible. El entregable es el borrado **más la métrica de verificación** — que desde el pase 19 tiene herramienta permisiva: las métricas de *membership inference* de **OpenUnlearning** (MIT). No vender «olvido garantizado» sobre un modelo deep.


    **Las dos puntas existen y están verificadas.** Del lado del LMS: el **Privacy API** de Moodle, `admin/tool/dataprivacy` y `admin/tool/policy` **en el núcleo** (verificado por código HTTP en `MOODLE_500_STABLE`), más los `privacy provider` de AI del núcleo (⚠️ **el pase 19 corrigió esto: son siete, no tres, y ninguno de los siete borra nada — la plantilla real es `core_ai`; ver la tendencia 48**) y el retiro de usuario de Open edX. Del lado del modelo: la capa permisiva de *unlearning* del gap 31.

    **Lo que no existe, y se buscó:** ningún *hook*, plugin, herramienta LTI ni servidor MCP que, a partir de un pedido de supresión **aprobado** en el LMS, dispare el reajuste o el *unlearning* del estimador de *mastery*. El flujo del LMS termina en el borrado de filas. **El modelo no se enteró.**

    **Por qué es la quinta vez, y a esta altura es la descripción del mercado.** Pase 15: procedencia (SynthID-Text y C2PA existen y son permisivos; el puente al aula no). Pase 16: privacidad horizontal (ocho librerías, 26.000+ ★, ningún adaptador educativo). Pase 17: privacidad del LMS (la máquina instalada, ningún agente que la use). Pase 18, dos veces: la capa de *unlearning* sin educación (gap 31) y **este disparador ausente**. **Cinco capas seguidas donde la infraestructura está resuelta y lo que falta es integración de tamaño acotado.** Esa es la forma del trabajo que Studios puede vender en esta industria, y conviene dejar de tratarla como un hallazgo por pase.

    ⚠️ **Y lo que este gap no promete.** Para deep knowledge tracing el *unlearning* es **aproximado**: queda residuo medible. El entregable es el borrado **más la métrica de verificación**. No vender «olvido garantizado» sobre un modelo deep; si el cliente necesita garantía absoluta, la respuesta honesta es reentrenar — o elegir BKT desde el principio, que es la recomendación de **P38**.

33. ~~**Ningún LRS permisivo implementa el borrado, y el estándar xAPI tampoco lo contempla**~~ 🔴 **CERRADO POR REFUTACIÓN EN EL PASE 21** *(abierto en el pase 19 del 2026-10-01, cerrado el 2026-10-01)*.

    🔴 **La primera mitad era falsa, y se detectó leyendo el código en vez de la documentación.** **`lrsql` (Apache-2.0) implementa `DELETE /admin/agents`**: borrado **por `actor-ifi`** —la identidad xAPI del alumno— en cascada sobre **7 tablas** y dentro de **una transacción**, más una migración `ON DELETE CASCADE` puesta a propósito para que no quede residuo en `statement_to_actor`. ⚠️ **Viene apagado**: `LRSQL_ENABLE_ADMIN_DELETE_ACTOR=false` por default en producción. **Learning Locker** también borra (por filtro), confirmado. **Ralph** no en la API del LRS, pero sí en su *data backend* por ID de statement — y 🔴 **con backend ClickHouse es imposible**.

    **La segunda mitad se sostiene, y es lo único que queda del gap:** **xAPI / IEEE 9274.1.1 no define supresión** (define *voiding*), así que todo borrado acá es **extensión propia de cada implementación y no es portable entre LRS**. Lo que queda abierto es la **evidencia** (**gap 36**) y el **disparador LMS→LRS** (**P40**, ahora con la limitación declarada por escrito por ILIAS — ver tendencia **55**), **no la capacidad**. Ver las tendencias **54**, **55** y **56**, el patrón **P44**, y la corrección completa en `repos/foundations.md`.

    **El registro original del pase 19 se conserva abajo, porque el error de método es el hallazgo:** un gap declarado sobre documentación no es un gap, es una lectura pendiente.

    **Formulación original (pase 19):** Es el **eslabón del medio** de la cadena de supresión que esta KB venía construyendo, y el único que falla.

    **Empieza arriba de los repos, en la especificación.** **xAPI —hoy IEEE 9274.1.1— no define una operación de supresión de *statements*.** Define ***voiding***: un statement nuevo con verbo `voided` que declara obsoleto al anterior **dejándolo donde está**. Eso es lo contrario del art. 17 del GDPR, de la Ley 21.719 chilena y del derecho de supresión que reconocen Vietnam, Corea y Brasil.

    **Y abajo, el reparto de licencias repite por tercera vez el patrón de la tendencia 45:** `lrsql` (**Apache-2.0**, 144 ★) 🚫 no documenta borrado; Ralph (**MIT**, 51 ★) 🚫 tampoco; **Learning Locker (GPL-3.0, 584 ★)** ✅ es el único al que se le atribuye API de borrado. **Lo permisivo no borra; lo que borra es copyleft.**

    **Por qué este gap es de esta KB y no del mercado:** `learnmcp-xapi` (MIT) está en la tabla principal como el único puente agente↔IEEE 9274.1.1, y declara como backends **`lrsql`, Ralph y Veracity** — los permisivos. **El stack que esta KB recomienda escribe la historia del alumno en un almacén del que no hay forma estándar de sacarla.** No invalida el patrón: le agrega una obligación de diseño explícita (**P40**) y una línea en el expediente.

    ⚠️ **Límite de la afirmación.** El «no» es **ausencia en la documentación publicada**, no imposibilidad: las dos son bases SQL/Elasticsearch y un `DELETE` a mano siempre es posible. La afirmación exacta: **ninguno ofrece el borrado como operación soportada y documentada**, y por eso ninguno puede figurar en un expediente como el componente que cumple el art. 17 — el `DELETE` a mano es trabajo a medida y se cotiza como tal. El «sí» de Learning Locker es de fuente secundaria y **sigue sin verificarse contra su API**: es la acción 1 que este pase deja escrita.

34. ***Unlearning* evaluado sobre modelos del alumno** *(agregado en el pase 19 del 2026-10-01)*. Es lo que queda del gap 32 después de medirlo, y es **el hueco más construible que tiene esta KB**.

    **La asimetría, en una tabla de dos filas.** Para el **tutor LLM** la capa está resuelta y es permisiva: **OpenUnlearning** (MIT, **607 ★**, Locus Lab / CMU) trae TOFU, MUSE y WMDP, 12+ métodos y **10+ métricas que incluyen ataques de inferencia de pertenencia**. Para el **estimador de mastery** —que en educación es el modelo que contiene el dato sensible— **no hay nada**: ninguno de los tres benchmarks evalúa *knowledge tracing* ni *cognitive diagnosis*, y el único trabajo específico (**PrivacyCD/HIF**, arXiv 2511.03966) **no libera código**, igual que su contraparte de ataque (**P-MIA**, arXiv 2511.04716).

    **Por qué es construible y no investigación de frontera:** las tres piezas existen y las tres son permisivas. `pyKT` es **MIT** y es PyTorch; `torchunlearn` es **MIT** y trae 20 algoritmos; las métricas de ataque de OpenUnlearning son **MIT**. **Falta el ensamblado y la medición, no el método.** El entregable es exactamente el número que hoy **P38** no puede prometer, y convierte «olvido aproximado» en «olvido aproximado con residuo medido». Es la acción 2 que este pase deja escrita.

    ⚠️ **Y la razón por la que vale la pena construirlo ahora, que es nueva en este pase:** **P-MIA** mide que el **dashboard de mastery** —el artefacto que esta KB propone como entregable— **es la superficie de ataque**, porque los vectores de estado de conocimiento se pueden revertir desde las visualizaciones de radar. Ver la tendencia **50**. Sin métrica de verificación, un *unlearning* sobre `pyKT` es una promesa; con las métricas de OpenUnlearning, es un número.


35. **Ningún benchmark pedagógico está empaquetado como prueba de conformidad, y ninguna herramienta de conformidad tiene cobertura educativa** *(agregado en el pase 20 del 2026-10-01)*. **Es el gap más construible y de mayor valor comercial de esta KB**, y es de naturaleza distinta a todos los demás: no espera que nadie publique nada.

    **Las dos mitades existen, están maduras, y son licencia-compatibles.** Del lado de la **herramienta**: `inspect_ai` (**MIT**, 2.900 ★, UK AI Security Institute), `moonshot` (**Apache-2.0**, 353 ★, AI Verify Foundation / IMDA Singapur), `compl-ai` (**Apache-2.0**, 211 ★, ETH Zürich + INSAIT + LatticeFlow, **29 benchmarks mapeados a los 6 principios del EU AI Act**), más los puntos de extensión: `moonshot-data` (**Apache-2.0**, datasets y *cookbooks*) y `aiverify-developer-tools` (**Apache-2.0**, plugins de test propios). Del lado del **benchmark pedagógico**, ya en esta KB desde el pase 4: `EduBench` (**MIT**, ACL 2026), `SafeTutors` (**MIT**), `MathTutorBench` (CC BY 4.0, EMNLP 2025 Oral), `UnifyingAITutorEvaluation` (CC BY-SA 4.0, NAACL 2025), `AITutor-EvalKit` (**MIT**).

    **La ausencia está declarada por los propios catálogos, no inferida de una búsqueda** — y eso es lo que la vuelve citable: `LLM-Evals-Catalogue` (AI Verify Foundation, 23 ★, ⚠️ sin licencia declarada) publica su categoría *domain-specific* con **derecho, medicina y finanzas** y **educación no figura**; `compl-ai` mapea 29 benchmarks al AI Act **sin una mención de educación**, aunque el **Anexo III del propio AI Act nombra la educación como alto riesgo de forma textual**; y `awesome-eu-ai-act` (**CC0**, 21 ★) lista once herramientas de conformidad open source y **ninguna del sector educativo**.

    **Por qué es distinto de los gaps 31 y 34:** ésos esperan que un grupo de investigación libere código. **Éste se cierra con trabajo de integración sobre repos que ya están verificados en esta KB** — empaquetar `EduBench` y `SafeTutors` como *recipe* de Moonshot y como benchmark mapeado de `compl-ai`. **No es investigación: es empaquetado.** Y habilita exactamente el expediente que esta KB ya vende en cinco patrones (**P4**, **P10**, **P11**, **P17**, **P39**). Ver **P42**.

    **La acción escrita, para el pase que la ejecute:** las dos puntas son MIT y Apache-2.0, así que la contribución puede ir **hacia arriba** —a repos de un regulador nacional y de ETH Zürich—, lo que convierte un entregable de cliente en posicionamiento público. ⚠️ **Y los cuatro límites que no hay que cruzar:** ninguna de estas herramientas **certifica** (`aiverify` declara por escrito que no garantiza ausencia de riesgo o sesgo); el marco de Singapur es **voluntario** y el europeo no; **no hay crosswalk directo de AI Verify al EU AI Act** (sólo a **NIST AI RMF**, oct-2023, y a **ISO/IEC 42001:2023**, jun-2024 — al AI Act se llega indirecto por ISO 42001); y `aiverify` evalúa **modelos supervisados tabulares y de imagen, no agentes**.


40. ~~**El cartucho MCP de CaSS está declarado, no medido.**~~ → 🟢 **GAP CERRADO EN EL PASE 26 DEL 2026-10-01, y cerrado ejecutando.** El pase 25 lo abrió porque toda la tendencia 65 y el paso 4 de **P48** descansaban en una línea del README de CaSS entre sus *pluggable cartridges*. **Este pase corrió el generador.** No se levantó el servidor —necesita Elasticsearch y en este entorno **no hay demonio de Docker**: el CLI está, `/var/run/docker.sock` no existe— sino por donde la arquitectura del proyecto lo permite: las tools se generan con `generateTools(spec)` sobre el OpenAPI que `swagger-jsdoc` arma desde los comentarios del código, **y eso es puro y corre sin base de datos**. Se replicaron las opciones exactas de `src/main/server.js`, se validó el spec con el mismo `openapi-schema-validator` del arranque y se ejecutó el generador real del repo. 🔴 **REABIERTO EN SU TRAMO DE INVOCACIÓN EN EL PASE 27 DEL 2026-10-01.** Lo que está cerrado es el **catálogo**, y ahora por **dos canales independientes**: el pase 26 corrió `generateTools(spec)`; el pase 27 contó las anotaciones `x-mcp-tool-name` en el árbol clonado y obtuvo **los mismos seis nombres**. Lo que sigue **sin medir es la invocación**: nadie hizo `initialize` + `tools/list` contra **`POST /api/mcp`**. El bloqueo **cambió de naturaleza** y hay que decirlo: el pase 26 no pudo por **falta de demonio de Docker**; el pase 27 localizó el camino (el *probe* de `util.js` sólo pide `GET /` y salud `yellow`/`green`, y `server.js:452` carga los cartuchos en el evento `listening`, **antes** de que termine la migración) pero **no pudo instalar el árbol de dependencias de un repositorio de terceros en este entorno**, y `artifacts.elastic.co` responde **403** por el proxy. **No es un límite de red ni de infraestructura: es del entorno de ejecución**, y se levanta corriendo el pase donde esté permitido instalar y ejecutar código de terceros. **Consecuencia para cotizar:** el catálogo se cita; la latencia, la forma de respuesta y el comportamiento de sesión **no**.

    **Medido: 51 paths, 0 errores de validación, 6 tools, 3 resource templates.** `server_status` (`GET /api/ping`), `search_data` (`GET /api/data/`), `get_object` (`GET /api/data/{uid}`), `save_object` (`POST /api/data/{uid}`), **`record_evidence`** (`POST /api/xapi/statement`) y **`get_learner_profile`** (`GET /api/profile/latest`). Resource templates: `CaSS JSON-LD Object`, `… (Versioned)`, `… by UID`. Tabla completa con parámetros y `annotations` en `agents/top.md`.

    **Las dos últimas son las que importan: entrar evidencia xAPI y sacar perfil de competencia, por MCP, bajo Apache-2.0** — los dos pasos exactos que **P48** tenía inferidos. Ver la tendencia **66** y el patrón **P50**.

    ⚠️ **Lo que esta medición no es, dicho con precisión:** se midió la **generación** de las tools, determinista y pura sobre el spec, **no su invocación**, que necesita Elasticsearch. Las 13 aserciones de `5.mcp.json-schema-to-zod.test.js` pasan **13/13**; `5.mcp.openapi-to-tools.test.js` **no corre tal cual** porque su `before` hace `fetch` a `localhost:80/api/swagger.json`. El conteo de **6** coincide con lo que ese test afirma literalmente (*«generates exactly 6 tools from the current spec»*) y con las **6** anotaciones `x-mcp-tool-name` del árbol: **tres fuentes independientes dan 6.** El *handshake* MCP real queda como acción del pase 27.

41. **Por MCP, CaSS escribe un statement por llamada: la superficie está curada y el *bulk* queda afuera a propósito** *(agregado en el pase 26 del 2026-10-01)*. De los **51 paths** del spec el cartucho expone **6**, y no por inmadurez: hay **45 `x-mcp-ignore: true`** puestos **uno por uno** en el código, con `x-mcp-tool-name` y `x-mcp-description` escritos a mano en los seis que salen. Lo excluido incluye **`POST /api/xapi/statements`** (el *bulk* del LRS), `GET /api/xapi/endpoint`, el `multiPut`/`multiGet`/`multiDelete` de skyRepo y **todo `skyId`**. **Consecuencia de cotización, y es la que importa:** quien presupueste **ingestión masiva de telemetría por la puerta MCP** está cotizando mal — por ahí entra **un statement por llamada**. Para lotes hay que ir a la API REST por fuera de MCP. **No es un defecto: es una decisión de diseño que conviene citar como tal**, porque muestra que el proyecto pensó la superficie de agente en vez de volcar su API. 🔴 **CORREGIDO EN EL PASE 27 DEL 2026-10-01: las ocultas son 55, no 45, y el error es conceptual.** El 45 era **`51 paths − 6 tools`** —aritmética, no conteo—, y **`x-mcp-ignore` se declara por operación, no por path**: un path con `GET`, `POST` y `DELETE` lleva **tres** anotaciones. El conteo real de `x-mcp-ignore: true` sobre `src/main` (excluyendo la librería que *lee* la anotación) da **55**, de modo que los **51 paths contienen 61 operaciones**: **6 expuestas + 55 ocultas**. **La corrección refuerza la lectura de este gap en vez de debilitarla:** son **55 decisiones de exclusión escritas a mano**. El desglose por adaptador —y el hallazgo de que **CASE (13), CEASN (6) y Open Badges (5) están enteros fuera de MCP**— está en la tendencia **72**. **Todo lo que este gap afirma sobre el *bulk* de xAPI sigue en pie:** `record_evidence` es la única puerta de evidencia y entra **un statement por llamada**.

42. **No existe implementación *platform-side* (lado LMS) de LTI 1.3 que sea permisiva *y* productiva** *(agregado en el pase 26 del 2026-10-01, medido sobre seis candidatos)*. El pase 24 lo sospechó con dos piezas; este pase lo midió con seis. **`ltijs` (Apache-2.0, 5.9.9) exporta `[ 'Provider' ]` y nada más** —sin clase de *platform*— y su `package.json` dice *«turn your web application into a LTI 1.3 **Learning Tool**»*: **tool-side, medido, no leído**. `macewan-cs/lti` (**MIT**, 8 ★) resultó **tool-side** también, contra lo que sugería el resumen de búsqueda. Las dos permisivas del lado plataforma se autodenominan **«Sample»** (`LtiLibrary/LtiAdvantagePlatform`, MIT) y **«example»** (`Citolab/lti-1p3-platform-example`, **GPL-3.0+**). La única **completa y certificada por 1EdTech** es `oat-sa/lib-lti1p3-core`, **GPL-2.0**. Y `UOC/java-lti-1.3-platform` **no declara licencia** y habla en futuro. → 🟢 **GAP CERRADO POR AGOTAMIENTO EN EL PASE 27 DEL 2026-10-01.** Se verificó la última candidata sin mirar, la **implementación de referencia de 1EdTech en Ruby on Rails**, y **no es una implementación**: [`1EdTech/ltibootcamp`](https://github.com/1EdTech/ltibootcamp) (**127 ★, 19 forks, 47 commits**) es una **colección de enlaces** —su README dice que *«junta links que se relacionan con entender e implementar Tools y Platforms LTI»*— y **no declara licencia en la página**. El código Ruby de la RI real de 1EdTech (platform *y* tool) está **en el repositorio de Contributing Members**, es decir **detrás de la membresía**. Con eso el *«no existe permisivo y productivo del lado plataforma»* pasa de **medido sobre seis** a **cerrado sobre siete, incluida la referencia oficial**, y habilita decirle a un cliente **«el lado plataforma se presupuesta como desarrollo»** con la evidencia completa sobre la mesa.

    **La salida para un engagement, y son tres, ninguna gratis:** aceptar **GPL-2.0** (TAO, certificada); integrarse **como *tool*** contra el LMS que el cliente ya tiene —donde esta KB sí es fuerte: `ltijs` + `canvas-mcp`—; o presupuestar el lado plataforma **como desarrollo, no como integración**. ⛔ **La verificación del *launch* OIDC de punta a punta sigue pendiente y está bloqueada por el entorno:** `LtiAdvantagePlatform` es **ASP.NET Core 10**, acá **no hay `dotnet`** y no se puede instalar — `https://dot.net/v1/dotnet-install.sh` responde **`CONNECT tunnel failed, 403`** por el proxy.

43. ~~**Moodle es el LMS más instalado del planeta y su único conector MCP es AGPL-3.0 con las partes útiles cerradas**~~ → 🔴 **GAP RETIRADO EN EL PASE 27 DEL 2026-10-01: LA AFIRMACIÓN ERA FALSA.** No es que el gap se haya cerrado construyendo nada — **el cuantificador estaba mal y una sola búsqueda lo desmintió**. Existen al menos **tres** conectores MCP de Moodle, y **dos son MIT**: [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) (**MIT**, **43 ★, 13 forks**, 10 commits, TypeScript, **8 tools de las cuales cuatro escriben** — incluidas **`provide_assignment_feedback`** y **`provide_quiz_feedback`**) y [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) (**MIT**, 1 ★, 1 fork, 59 commits, TypeScript, **40 tools** en 10 dominios **+ `ws_raw`**, v0.5.2, *«~80 % operable desde un agente LLM»*). **Las dos afirmaciones subsidiarias también caen:** que *«los tools abiertos son sólo de lectura»* (hay cuatro de escritura) y que *«no hay nada equivalente a `canvas-mcp` para Moodle»* (40 tools es el orden del escalón bajo de `canvas-mcp`). **Lo que sigue siendo cierto** es lo que el pase 26 leyó bien del repo que sí encontró: `csmediapro/moodle-mcp-server` **es** AGPL-3.0 con capas de pago. **El error fue de muestreo, no de lectura**, y está declarado como **gap 49**: los directorios de MCP rankean por promoción. 🔴 **El patrón P51 se construyó sobre esta premisa y quedó corregido en el mismo pase.** El hueco real del eje conector **se corre a Open edX** (**gap 48**). Ver las tendencias **69**, **70** y **71** y los patrones **P54** y **P55**. El texto original se conserva arriba tachado, con su registro de origen: *(agregado en el pase 26 del 2026-10-01)*.

44. **El eje conector tiene dos estándares vacíos y uno con colisión de término** *(agregado en el pase 26 del 2026-10-01)*. Cruzando `MCP server` con cada estándar inventariado: **xAPI** ✅ (`learnmcp-xapi`, ya estaba), **LTI** ✅ (vía conectores de LMS), **OneRoster** 🔴 **nada**, **QTI** 🔴 nada verificable —apareció un *Question Bank MCP Server* listado en Glama **sin repo de GitHub localizable, y no se registra como hallazgo**—, **CASE** 🔴 nada **y con el término capturado**: la búsqueda se llena de *certificaciones* de MCP (MCPA de Linux Foundation, certs de Claude). **Es la segunda colisión de término que mide esta KB**, después de `education` = «cursos sobre AI» (pase 23). **Regla de método que deja: antes de concluir que una capa está vacía, verificar que la palabra no esté capturada por otro mercado.** Con `education` costó siete pases descubrirlo.

45. **La vertical biblioteca no tiene ninguna pieza agéntica, y es la que tiene el bus de eventos servido** *(agregado en el pase 26 del 2026-10-01)*. Se abrió la capa biblioteca/ILS y **tiene opción permisiva y grande** —**FOLIO**, Apache-2.0, 3.096 commits en `platform-complete`, **multi-tenant, modular y con Kafka** en `mod-inventory`— pero **no existe conector MCP ni agente** ni para FOLIO ni para Koha (GPL-3.0+). **FOLIO es el candidato más obvio de toda esta KB para construir uno**, porque ya publica eventos en Kafka: el agente se engancha como consumidor **sin parchear el core**. Ver el patrón **P52**.

46. **No hay plataforma de admisiones open source permisiva y productiva** *(agregado en el pase 26 del 2026-10-01)*. Lo que sirve es copyleft y ya estaba en esta KB: **OpenEduCat** (**LGPL-3.0**, pipeline completo de consulta → solicitud → verificación documental → entrevista → oferta → alta en SIS, sin fee por postulante) y `OS4ED/openSIS-Classic` (**GPL**). Lo único permisivo verificado es `CollinsTatang/admissionSystem` (**MIT**, **4 commits**, 6 ★, 0 forks, PHP/MySQL): no es base de producción, y el conteo de commits lo dice solo. ⚠️ **Y un no-hallazgo declarado:** el barrido ofreció `WalaEddine01/OrgSchool-portfolio-project` como *«Open Source Software about student Management System»* y **verificado da 404** — **no se registra**, porque un 404 no es un hallazgo. **La salida practicable es LGPL-3.0 sobre OpenEduCat**, y para un módulo Odoo es manejable porque **la LGPL admite el módulo propietario al lado**; la alternativa es desarrollo.

47. **La capa de *student success* open source es de 2013–2014, es GPL, no vive en GitHub — y es la que el regulador aprieta más** *(agregado en el pase 26 del 2026-10-01)*. **FlightPath Academics** (asesoría académica, *degree audit*, ***early alerts***, *Academic Priority*) es **PHP, GPLv3+**, liberada el **2013-03-13** por la University of Louisiana at Monroe, y **no tiene repositorio en GitHub** (el 404 de `Cerebro-Tech/FlightPath` es de WebFetch). **Student Success Plan** (Unicon) y el *dashboard* de **Marist College** tienen referencias verificables sólo de **2013–2014**. 🔴 **Es la capa más vieja y peor abastecida de las veintiséis pasadas** — y simultáneamente la que concentra más presión regulatoria, porque *predecir qué alumno va a fracasar* es exactamente la decisión automatizada sobre el alumno que el **Annex III** clasifica de alto riesgo y que **Oklahoma y Maryland** prohíben tomar de forma autónoma. **Hueco de mercado grande y riesgo alto en la misma celda.** Ver la tendencia **68** y el patrón **P53**.

48. 🔴 **Open edX es el LMS grande sin conector MCP, y es el de la huella pública más grande** *(agregado en el pase 27 del 2026-10-01)*. Búsqueda **en modo extendido** de `"Open edX" MCP server github repository connector tools Studio API`: **nada**. Es el hueco que el **gap 43 creía tener en Moodle** y que resultó falso: Canvas tiene `vishalsachdev/canvas-mcp` (**MIT**), Moodle tiene **dos conectores MIT** (`peancor/moodle-mcp-server`, `MarcosNahuel/moodle-mcp`), SCORM tiene `giacomomaria81/scorm-mcp-server` (**MIT**) — **Open edX no tiene ninguno**. **Por qué es el mejor perfil de oportunidad de esta KB:** es el stack de los programas públicos grandes de **LATAM e India**, y esta KB ya tiene registrado que si el cliente corre Open edX con analítica **corre Aspects → Ralph sobre ClickHouse sin haberlo elegido** (pase 22) — o sea, llega con una configuración de telemetría impuesta y sin puerta de agente. Y es **barato**, porque la arquitectura está resuelta dos veces: `MarcosNahuel/moodle-mcp` publica la decisión a portar —**fachadas de alto nivel sobre la API, más un `ws_raw` de escape**, en vez de volcar cientos de endpoints. ~~**Lo que falta medir antes de cotizar:** si Open edX expone una superficie REST estable y versionada equivalente a los Web Services de Moodle. Es la **acción 1** de este pase.~~ → ✅ **MEDIDO EN EL PASE 28 DEL 2026-10-01, Y EL GAP SE PARTE EN DOS.** Leyendo los `urls.py` de `master`: *Course Blocks* en **`v1` y `v2`**; *Enrollment* con **escritura** (`unenroll/`, `enrollment_allowed/`, `roles/`); *Grades v1* con **escritura y por lote** (**`gradebook/{course_id}/bulk-update`**, *course_grade_overrides*) — **más capaz que el conector MIT de Moodle, que escribe de a una**. 🔴 **Pero la API de *authoring* de Studio está declarada experimental por el proyecto** y es el **gap 50**. **Conclusión: para operación y evaluación la ausencia es puro gap 49; para autoría de curso hay causa técnica.** La AGPL **no es el obstáculo** (el conector es otro proceso que habla REST, igual que las puertas MIT de Canvas y Moodle). Ver las tendencias **71**, **73** y **74** y el patrón **P55**.

49. **Los directorios de MCP rankean por promoción, y esta KB midió tres capas con ese sesgo** *(agregado en el pase 27 del 2026-10-01)*. No es un gap de oferta: es un **gap de método**, y se declara porque ya produjo una conclusión falsa publicada. El **gap 43** afirmó *«el único conector MCP de Moodle»* tras consultar un directorio que devolvió **un** candidato — el único de los tres con **sitio comercial propio, paquete npm con nombre de producto y *premium plugins***. Los dos MIT, con **1 ★ y 43 ★ y cero marketing**, no aparecieron. 🔴 **Las capas que el pase 26 declaró vacías por el mismo canal y que por lo tanto están sin medir de verdad: `OneRoster`, `QTI` y `CASE`** (gap 44). **La regla:** cuando una búsqueda de directorio devuelve un único candidato y ese candidato es además el único con presencia comercial, **la capa no está medida — está mal muestreada**; hay que repreguntar al *host* del repositorio por patrón de nombre (`*-mcp`, `mcp-*`, `mcp-server` + estándar). Es la **acción 2** de este pase. Ver la tendencia **69**. → 🔴 **CONFIRMADO POR SEGUNDA VEZ EN EL PASE 28, Y LA REGLA DEL PASE 27 RESULTÓ INSUFICIENTE.** De las tres capas, **OneRoster sí tenía conector** —[`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts), **0BSD**, **164 métodos como MCP tools con escritura**, OneRoster v1p2— y **no se encontró por patrón de nombre**: el repo **no tiene `mcp` en el nombre**, es un **SDK** que declara el servidor en una línea del README. **La regla se extiende: hay que buscar el estándar + `SDK`/`client`/`library` y leer el README por dentro.** **QTI** quedó medido por los tres métodos (ausencia real, ver **P59**) y **CASE sigue sin medir** por colisión de término (**gap 51**). Ver la tendencia **73**.
50. 🔴 **La API de *authoring* de Open edX está declarada experimental por el propio proyecto, y es el tramo que un conector de agente más necesita** *(agregado en el pase 28 del 2026-10-01)*. Medido leyendo `cms/djangoapps/contentstore/rest_api/v1/urls.py` del árbol `master`: hay **21 rutas** (`xblock/`, `container_handler/{usage_key}`, `container/{usage_key}/children`, `course_settings/…`, `course_details/…`, `course_grading/…`, `course_rerun/…`, `certificates/…`, `group_configurations/…`, `proctored_exam_settings/…`), **y el repo avisa que «the Authoring API is still experimental» y recomienda usar las versiones `v0`**. **Por qué es un gap y no un detalle:** este pase contestó el **gap 48** mostrando que *Enrollment* y *Grades* **están versionados y escriben** —`unenroll/`, `enrollment_allowed/`, **`gradebook/{course_id}/bulk-update`**, *course_grade_overrides*—, así que ahí la ausencia del conector es puro **gap 49**. **El *authoring* es el único tramo donde la ausencia tiene causa técnica real:** replicar lo que hace `MarcosNahuel/moodle-mcp` (crear curso, secciones, publicar material, armar quiz) obligaría a apoyarse en la parte que el mantenedor marca inestable, mientras el de Moodle se apoya en Web Services, estables desde hace más de una década. **Lo que falta medir antes de descartarlo:** si los endpoints **`v0`** —los que el repo recomienda— cubren lo que el `v1` experimental promete. Es la **acción 1 del pase 29**. Ver las tendencias **73** y **74** y el patrón **P55**. → 🔵 **REENCUADRADO EN EL PASE 29 DEL 2026-10-01, Y LA PREMISA DE ESTE GAP ERA UN ERROR DE MUESTREO PROPIO.** La **acción 1** pedía medir si los endpoints `v0` cubren lo que el `v1` experimental promete. **La pregunta estaba mal planteada, porque el tráfico va al revés.** Leído el paquete completo: el aviso *«the Authoring API is still experimental… use the v0 versions»* está en `v1/urls.py`, **fechado «(Nov. 23)»**, y **encabeza una sección sin una sola ruta**; mientras `v0/views/xblock.py` declara que **`v0` es el deprecado** (*«superseded by `XblockViewSet`… use `/api/contentstore/v1/xblock/` going forward»*, con `DeprecationWarning` en sus 5 vistas) y **`v1/urls.py` registra efectivamente `XblockViewSet`** (`_router.register(r'xblock', XblockViewSet, …)`), implementado con **CRUD completo** (`create`/`retrieve`/`update`/`partial_update`/`destroy`) contra los ADRs de **FC-0118** (0025, 0026, 0028, 0029, 0034, 0036). 🔵 **ADR 0036 agrega `?view=minimal`, que recorta la respuesta en árbol a campos estructurales — justo el problema de ventana de contexto que tiene un agente sobre un curso grande.** **Conclusión: la autoría NO está bloqueada por estado experimental; la ausencia del conector de Open edX es gap 49 en los tres tramos (operación, evaluación y autoría), y el conector completo es cotizable.** **Lo que queda no es inestabilidad sino rotación de versiones** (`v0`–`v4` montadas a la vez, notas en tres de ellas, assets/video/transcripciones sólo en `v0`): es riesgo de **adaptador**, no de viabilidad. Ver las tendencias **78**, **79** y **80** y el patrón **P55**.

51. ⚠️ **La ausencia de conector MCP para CASE no está medida, y se declara como no medida por colisión de término** *(agregado en el pase 28 del 2026-10-01)*. La **acción 2 del pase 27** pedía repreguntar por patrón de nombre las tres capas que el pase 26 declaró vacías vía directorio. **De las tres, dos quedaron resueltas y una no:** OneRoster **tenía** conector (**gap 49 confirmado por segunda vez**, ver tendencia **73**), QTI **no lo tiene y ahora está medido por tres métodos** (directorio + patrón de nombre + **apertura del SDK permisivo**, `examplary/qti` MIT, donde MCP no se menciona), y **CASE no se pudo medir**. 🔴 **La causa es una colisión de término, la cuarta de esta KB:** `case-mcp` / `mcp-case` devuelve **`09-CaseStudy` de `microsoft/mcp-for-beginners`**, **`Casys-AI/mcp-server`** y **`mcp-usecase`**, porque ***case study*** y ***use case*** son dos de los términos más frecuentes de la documentación de MCP. Y **el método que sí funcionó con OneRoster —abrir el SDK y leer el README adentro— no se pudo aplicar, porque CASE no tiene un SDK permisivo y traccionado que abrir**. **Lo que sí está medido** (pases 26–27) es que **`cassproject/CASS` tiene las 11 operaciones de su adaptador CASE con `x-mcp-ignore: true`**, o sea excluidas a propósito. **El registro de colisiones de esta KB, que ya es un activo de método:** `education` → material didáctico *sobre* AI (pase 23); `Bloom` → dos proyectos homónimos (pase 7); `MCP` + *badges* → generadores de *badges* de README (pase 27); **`case` → *case study* / *use case* (pase 28)**. **La acción:** medir CASE por el *host* del repositorio con el nombre **completo y desambiguado** del estándar (`"Competencies and Academic Standards Exchange"`), no por la sigla. Ver la tendencia **73**. → ✅ **CERRADO EN EL PASE 29 DEL 2026-10-01, Y LAS DOS MITADES QUEDARON MEDIDAS.** La acción pedía medir CASE por el **nombre completo desambiguado** del estándar en vez de la sigla. **Funcionó, y devolvió lo que cuatro pases no habían visto:** [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) — **Apache-2.0** (verificado en el archivo `LICENSE`), **9 ★**, 3 forks, **180 commits**, del **propio organismo de estándares** —, que implementa **CASE 1.0 y 1.1** con la **CASE Provider API oficial** *«fully compatible with the 1EdTech certification requirements»*, con **CRUD de escritura** sobre `CFDocuments`/`CFItems`/`CFAssociations`/`CFPackages` en **v1p0 y v1p1**, editor visual de marcos, Keycloak (OIDC) **+ API keys propias**, RBAC de cuatro niveles, multi-tenencia y **versionado inmutable en archivos sin base de datos externa**. 🔴 **Y la ausencia de MCP pasa de «sin medir» a MEDIDA: cero menciones de `MCP` o `Model Context Protocol` en el README crudo.** ⚠️ **La trampa que casi produjo un falso positivo, y que genera la quinta colisión de esta KB —la primera por *chrome* de plataforma—: la página renderizada de GitHub de OpenCASE SÍ dice «MCP», en su menú de navegación (*AI CODE CREATION → MCP Registry*), que es interfaz de GitHub y no contenido del repositorio.** **Regla nueva y retroactiva: la presencia de MCP se verifica en el README crudo, nunca en la página renderizada.** 🔵 **Y el cierre deja la mejor oportunidad de la KB:** el servidor **publica su propio OpenAPI 3** en `GET /ims/case/v1p1/discovery/imscasev1p1_openapi3_v1p0.json`, así que **el conector se genera, no se escribe** — el camino por el que `oneroster-ts` llegó a 164 métodos con 39 commits. Ver la tendencia **80** y el patrón **P60**.

52. ⚠️ **La forma exacta de las rutas de OpenCASE no está medida, y la causa es que los dos documentos del repo se contradicen entre sí** *(agregado en el pase 29 del 2026-10-01)*. El **gap 51** quedó cerrado en lo que afirma —la plataforma existe, es Apache-2.0 y no tiene MCP—, pero **la superficie quedó medida en forma, no en detalle**. Las dos fuentes del propio repositorio no coinciden: `apps/opencase/docs/DEVELOPER.md` escribe las rutas de gestión **sin** el prefijo del estándar (`PUT /management/tenants/{tenantId}/CFItems/{id}`, `DELETE /management/tenants/{tenantId}/CFDocuments/{id}`), y `apps/opencase/docs/FRAMEWORK_EDITOR_BACKEND_INTEGRATION.md` las escribe **con** prefijo y versión (`PUT /management/tenants/{tenantId}/ims/case/v1p1/CFItems/{itemId}`, `POST /management/tenants/{tenantId}/ims/case/v1p1/CFPackages/import`). 🔴 **Y el documento que el README principal ofrece como «Complete endpoint reference» —`apps/opencase/FRAMEWORK_MANAGEMENT_GUIDE.md`— devuelve 404 en `main`**: el enlace está roto en la rama por defecto. **Por qué importa y no es un detalle de documentación:** un conector generado desde una ruta equivocada falla en la primera llamada, y **el OpenAPI que el servidor publica es la única fuente que no puede estar desactualizada** porque la sirve el propio sistema. **Lo que falta:** resolverlo leyendo el código del servidor —el método que funcionó con Open edX— o pidiéndole el spec a `GET /ims/case/v1p1/discovery/imscasev1p1_openapi3_v1p0.json` con una instancia levantada. **Es la acción 1 del pase 30.** ⚠️ **Mientras esté abierto, P60 se propone con la arquitectura y el costo relativo, no con rutas literales.** Ver la tendencia **80**. → ✅ **CERRADO EN EL PASE 30 DEL 2026-10-02, LEYENDO EL CÓDIGO, Y LA CONTRADICCIÓN TIENE UNA REGLA QUE NINGUNO DE LOS DOS DOCUMENTOS ENUNCIA.** Se leyeron cinco archivos del árbol `main` (`package.json`, `src/main.ts`, `src/interfaces/http/server.ts`, `http-management/routes.ts` y `http-public/v1p1/routes.ts` más su gemelo `v1p0`). **La regla: el segmento `ims/case/v1pX` aparece exactamente cuando la operación actúa sobre una entidad del estándar CASE, y nunca en las rutas de plataforma.** Por lo tanto **`FRAMEWORK_EDITOR_BACKEND_INTEGRATION.md` es correcto** (sus dos formas existen literales) y **`DEVELOPER.md` está equivocado** para entidades CASE: `PUT /management/tenants/{id}/CFItems/{id}` **no corresponde a ninguna ruta registrada**. El error del doc se explica porque **el *listado* de paquetes sí va sin prefijo** (`GET /management/tenants/{tenantId}/CFPackages`), al ser operación de plataforma. ✅ **Confirmado además el 404 de `FRAMEWORK_MANAGEMENT_GUIDE.md` en `main`.** **Superficie contada: 72 rutas** — 12 de lectura en `v1p1` + **12 en `v1p0` (el juego completo en las dos versiones)** + **44 de management** (20 con prefijo, 24 sin) + **2 de descubrimiento** + `public/tenant-lookup` + `health`. 🔵 **Tres hallazgos nuevos que abaratan P60:** (a) hay **dos** endpoints OpenAPI 3, uno por versión, y los dos **sin autenticación**; (b) la lectura usa **auth opcional** —*«frameworks marked public are readable without auth… no tenantId is needed for read endpoints»*—, así que **un conector de sólo lectura no necesita credenciales**; (c) aparece **CGE — CASE Global Exchange**, **11 rutas de federación** (credenciales + `test`, `frameworks`, **`subscriptions`**, `import`, `refresh`, `cache/{docId}/items`) que permiten **suscribirse** a marcos del registro global en vez de cargarlos. 🔴 **Y el límite que hay que decir antes de cotizar: la escritura NO es parte del estándar y lo declara el código** (*«NOT part of the CASE standard specification»*), así que **sólo la mitad de lectura del conector generado es portable a otro proveedor CASE**. 🔴 **Hallazgo de seguridad para cualquier entregable: `cors({origin:true, credentials:true})`, con el comentario *«restrict in production»* en el propio código.** ⚠️ **Lo que sigue sin medirse: no se levantó instancia, así que el OpenAPI generado no se pidió al endpoint de descubrimiento. Es la acción 2 del pase 31** (una tarde con `docker-compose up`). ⚠️ **Canales: `codeload.github.com` da 403 y la API de GitHub está cerrada; `raw.githubusercontent.com` responde.** Ver las tendencias **81** y **83** y el patrón **P60**.

53. 🔴 **El paquete npm de `oneroster-ts` no declara licencia, mientras el repositorio es 0BSD — y es el artefacto que un cliente instalaría** *(agregado en el pase 29 del 2026-10-01)*. Medido en el registro de npm: **`@superbuilders/oneroster`**, última versión **`0.7.0`**, 10 versiones, devuelve **`license: None`** tanto en la raíz del paquete como en la versión publicada, **mientras el repositorio `trilogy-group/oneroster-ts` declara 0BSD**. **Por qué es un gap y no una curiosidad de metadatos:** esta KB recomienda esta pieza por su licencia —0BSD es la más permisiva que inventarió— y **el artefacto que se instala con `npm add` no respalda esa recomendación por sí mismo**. Es lo primero que mira el área legal de un cliente. ⚠️ **Dos datos de procedencia que van en la misma conversación:** los *maintainers* de npm (`abhi-superbuilders`, `hbauer`, `bjornpagen`, `supersterling`, `ameeralns`) **no son la organización del repositorio**, aunque ✅ **la procedencia es rastreable** porque el `repository.url` del paquete apunta de vuelta a `git+https://github.com/trilogy-group/oneroster-ts.git`; y **el último publicado es del 2026-05-04**, casi cinco meses antes de este pase, en una versión **pre-1.0**. **La mitigación ya estaba escrita y ahora tiene fundamento concreto: fijar un fork del repositorio —0BSD lo permite sin ninguna obligación— y no depender del paquete publicado.** **Lo que falta medir:** el `tools/list` real del servidor MCP, que es lo único que convierte «164 métodos de SDK contados» en «N tools servidas». **Es la acción 2 del pase 30.** Ver **P58**. → 🔵 **MEDIDO EN EL PASE 30 DEL 2026-10-02 EJECUTANDO EL SERVIDOR, Y LAS DOS MITADES DEL GAP SE MUEVEN EN DIRECCIONES OPUESTAS.** **(1) La mitad de licencia mejora:** medido **dentro del tarball publicado**, `package.json` **omite el campo `license` por completo** —de ahí el `None` del registro— **pero el paquete SÍ incluye un archivo `LICENSE` completo con el texto de la BSD Zero Clause License**, *«Copyright (c) 2025 Bjorn Pagen»*. **El defecto es de metadatos, no de licencia: el artefacto viaja con su 0BSD.** ✅ **Y cierra la duda de procedencia de este mismo gap:** `bjornpagen` es uno de los *maintainers* de npm que se anotaron como «no son la organización del repositorio», y es **el titular del copyright del LICENSE**, así que la cadena cierra. **(2) 🔴 La mitad de antigüedad empeora, y por un error de método de esta KB:** el «último publicado 2026-05-04» era **`time.modified`**, que es **mutación de metadatos** (un *dist-tag*, un cambio de dueño, una deprecación), **no una publicación**. La última **versión** publicada es **`0.7.0` del 2025-06-27**: **quince meses**, no cinco. **Y el patrón importa más que la fecha: 9 de las 10 versiones salieron en una ráfaga de tres días** (2025-04-29 → 2025-05-01), después `0.7.0`, y nada en quince meses — **perfil de generador corrido una vez, no de proyecto mantenido**. **Fijar un fork sigue siendo el requisito, ahora por abandono y no por licencia.** **(3) ✅ El `tools/list` que faltaba, medido:** `initialize` + `tools/list` por stdio contra `bin/mcp-server.js` devuelve **132 tools** (72 de lectura, 60 de escritura, 19 grupos) y el servidor se identifica como **`OneRoster 0.7.0`**. 🔵 **La brecha 164 → 132 NO es supresión: es *aliasing*.** El SDK documenta 164 métodos pero sólo **132 nombres distintos**, porque **32 operaciones están listadas bajo dos grupos a la vez**. **Cero anotaciones de supresión: se sirve el 100 % de las operaciones distintas**, al revés de CaSS (6 de 61). **La frase citable es «132 tools servidas, el 100 % de las operaciones del SDK».** 🔴 **Riesgo nuevo medido: el README usa como `--token-url` de ejemplo el IdP Cognito de producción de un operador concreto (`alpha-auth-production-idp…amazoncognito.com`), así que el SDK se generó contra UN despliegue** — hay que sobreescribir `--server-url`/`--token-url` y no suponer cobertura de cualquier proveedor OneRoster. 🔵 **Dos datos a favor: cero dependencias de runtime, y un flag `--tool` que permite servir un subconjunto de las 132** (control de ventana de contexto). Ver las tendencias **83** y **86** y el patrón **P58**.

54. 🔴 **La ausencia de conector sobre una plataforma con fundación grande no es una oportunidad estable, y esta KB lo aprendió perdiendo la suya** *(agregado en el pase 30 del 2026-10-02)*. El **gap 48** («Open edX es el único LMS grande sin puerta de agente») se mantuvo abierto en los pases 27, 28 y 29, y esta base invirtió en él su esfuerzo principal: midió la superficie REST leyendo cinco `urls.py`, reencuadró el **gap 50**, y cotizó **P55** encima. 🔴 **El 2026-07-25 el propio proyecto publicó la puerta** —`openedx-mcp` y `tutor-contrib-openedxmcp`, los dos **AGPL-3.0**, verificados en PyPI y en el código del sdist—, **dos meses antes de que este pase lo notara**. **Por qué es un gap de método y no sólo una oportunidad perdida:** el criterio con el que esta KB priorizaba —*«buscar la ausencia de mayor huella pública»*— **selecciona justamente los casos donde el dueño de la plataforma tiene más incentivo y mejor posición para cerrarla él**, porque puede correr en proceso contra las APIs internas y saltearse la superficie REST versionada que un tercero está obligado a usar. **La regla que lo reemplaza:** las ausencias que son oportunidad estable son **las de los estándares** (CASE, QTI, el lado *platform* de LTI), porque **ningún organismo de estándares publica software de integración** — y la contrastación está en esta misma base: las tres plataformas con fundación (Moodle, Canvas, Open edX) **ya tienen puerta**; los tres estándares **siguen sin ella** desde que se midieron. **Lo que falta:** reordenar la cola de oportunidades por *tipo de dueño* y no por huella, y **revisar si alguna otra ausencia declarada de esta KB ya fue cerrada por su propio proyecto sin que el barrido lo note**. **Es la acción 1 del pase 31.** Ver las tendencias **81** y **82**.

55. ⚠️ **No hay `tools/list` observado del conector oficial de Open edX, así que sus 35 rutas son superficie REST interna y no superficie de agente** *(agregado en el pase 30 del 2026-10-02)*. Lo medido de primera mano es el **código del sdist `openedx-mcp` 0.1.5**: **28 rutas en el LMS** (`whoami`, `analytics/overview`, `courses`, `users`, `grades`, `enroll`/`unenroll`/`bulk-enroll`, `users/create`, `roles/set`, `access/instructor`, `students/reset-attempts`, seis de certificados, tres de reportes asíncronos y dos de **retiro de cuenta**) y **7 en el CMS** (`outline`, `courses/settings`, `blocks/create`, **`blocks/create-tree`**, `update`, `publish`, `delete`), más **9 scopes** y **18 tools de escritura decoradas con `audited_write`**. 🔴 **Pero el servidor MCP no vive en este paquete: vive en `tutor-contrib-openedxmcp`**, y **no se levantó ninguna instancia**, así que **no se sabe cuántas tools expone ni con qué nombres**. **Por qué importa y no es un detalle:** esta KB acaba de aprender con `oneroster-ts` y con CaSS que **la distancia entre «rutas del backend» y «tools servidas» puede ser aliasing (sin pérdida) o supresión deliberada (con pérdida del 90 %)**, y que **la diferencia cuesta un `tools/list`**. Mientras no se mida, la cifra citable es **«35 endpoints de fachada REST»**, nunca «35 tools». ⚠️ **Dos límites más del mismo bloque:** es **`0.1.x`** y apunta a Open edX **Ulmo**, y **`openedx.org` está bloqueado por el proxy de egreso**, así que el anuncio oficial no se leyó —todo sale de PyPI y del código—. **Lo que falta:** `tutor plugins enable openedxmcp`, levantar el stack y hacer `initialize` + `tools/list`. **Es la acción 2 del pase 31**, junto con la de OpenCASE, y las dos son la misma tarde de trabajo. Ver las tendencias **81**, **83** y **84** y el patrón **P61**.

56. 🔴 **El calendario del Anexo III del AI Act tiene tres lecturas en circulación y esta KB sostiene dos de ellas en archivos distintos** *(agregado en el pase 30 del 2026-10-02)*. Se declara como gap porque **es la primera pregunta que hace un cliente europeo** y porque **la contradicción es interna, no de las fuentes**. Las tres lecturas: **(a)** el pase 11 registró el Anexo III corrido a **2027-12-02** por el **Reglamento (UE) 2026/1744** (en vigor 2026-07-27), y lo registró **leyendo la norma**; **(b)** el pase 28 escribió en `intel/trends.md` que *«el Annex III dejó de ser una fecha: rige desde el 2026-08-02»* y que la demanda de conformidad está **vencida**, y sobre esa lectura construyó argumentación comercial de EMEA; **(c)** las fuentes de prensa de este pase dicen que el marco entra **progresivamente desde agosto de 2026**. 🔴 **(a) y (b) no son conciliables: una dice que falta más de un año y la otra que ya rige**, y las dos están publicadas en esta base. **Por qué no se resuelve eligiendo la más conservadora:** si rige, la oportunidad de cumplimiento está **vencida y caliente** y eso cambia el orden de la propuesta; si no rige hasta 2027-12-02, vender urgencia es un error que un área legal detecta. ⚠️ **Mientras esté abierto, la regla operativa es: ante un cliente se cita la norma y no la prensa, y se verifica la fecha aplicable al caso de uso concreto** (el Anexo III tiene incisos, y educación es uno). **Lo que falta:** resolverlo contra el **texto consolidado** del Reglamento y fechar cada afirmación de esta KB con el inciso que le corresponde. **Es la acción 3 del pase 31**, y es la que más riesgo comercial descarga. Ver el bloque EMEA de `intel/market.md`.


## 54. El almacén permisivo que esta KB recomienda sabe borrar al alumno desde antes de que esta KB existiera, y seis pasadas vendieron lo contrario por leer documentación en vez de código (agregado 2026-10-01, pase 21)

**Ésta no es una tendencia del mercado: es una corrección de esta KB, y se registra como tendencia porque cambia el
argumento de venta de tres patrones y de dos regiones.**

Desde el pase 6, esta KB sostiene que la cadena de supresión del dato del alumno **se rompe en la telemetría**. Sobre
esa afirmación construyó la tendencia **49**, el **gap 33**, el patrón **P40**, media argumentación de EMEA y la
contraparte LATAM en `intel/market.md`. El pase 19 la midió del lado de Moodle y dejó escrita la acción:
*«Confirmar la API de borrado de Learning Locker (gap 33). Es la pregunta de mayor rendimiento del pase.»* El pase 20
no la tomó. **El pase 21 la ejecutó, y la afirmación es falsa.**

**Lo que hay, leído en el código fuente de los tres LRS:**

| LRS | ¿Borra? | Granularidad | Dónde está |
|---|---|---|---|
| **`lrsql`** (**Apache-2.0**) | ✅ **Sí, y es el mejor primitivo de la capa** | **por `actor-ifi`** — la identidad xAPI del alumno | `DELETE /admin/agents` → `delete-actor-and-dependents!` |
| **Learning Locker** (GPL-3.0) | ✅ Sí | por **filtro** de statements | `POST /api/v2/batchdelete/initialise` + worker paginado |
| **Ralph** (MIT) | ⚠️ No en la API del LRS | por **ID de statement** | `write(operation_type=DELETE)` en el *data backend* |

**El primitivo de `lrsql` es exactamente la forma del art. 17.** Recibe **un solo parámetro** y borra en cascada,
dentro de una transacción, de **siete tablas** —`statement_to_statement`, `statement_to_activity`, `attachment`,
`xapi_statement`, `agent_profile_document`, `state_document`, `actor`—. Y la octava, `statement_to_actor`, que es la
que **contiene el IFI del alumno junto a cada statement**, se borra por una **`ON DELETE CASCADE`** que una migración
con guarda agrega a propósito, con el comentario del mantenedor explicando para qué. **Alguien pensó este caso y lo
cerró**, años antes de que esta KB declarara que no existía.

⚠️ **Y viene apagado de fábrica:** `LRSQL_ENABLE_ADMIN_DELETE_ACTOR` es **`false`** por default en la configuración de
producción, y la ruta **no se registra** con el flag apagado. **Eso no es un desarrollo: es una variable de entorno.**

**Por qué esto es una tendencia y no una errata.** El error no estuvo en la búsqueda: estuvo en **confundir el silencio
de la documentación con la ausencia de la capacidad** — y esta KB lo tenía anotado. La nota de límite al pie de la
tabla del gap 33 decía, textual, que el «no» era *«ausencia en la documentación publicada, no una prueba de que la
operación sea imposible»*. **La nota tenía razón y nadie la ejecutó durante catorce pasadas.** El costo no fue un repo
que faltaba en una tabla: fue **venderle a un cliente la ausencia de una capacidad que el producto recomendado ya
tenía**, y cobrarle como alcance propio una intervención de almacén que son dos líneas de configuración.

**La regla que queda, y es la quinta de la serie de método de esta KB:** pase 5 — buscar la pieza, no la categoría;
pase 7 — la palabra del mercado, no la del paper; pase 8 — por quién es el alumno; pase 9 — el final del recorrido;
**pase 21 — leer el código, no la documentación. Un gap declarado sobre documentación no es un gap: es una tarea de
lectura pendiente, y hay que marcarla como tal para que no se cotice como ausencia.**

**Lo que esto no arregla, y es lo que queda vendible.** El borrado existe; **la evidencia y el disparador no.** Ningún
LRS de los tres emite evento de finalización, y `lrsql` **no devuelve ni el conteo de lo borrado** (**gap 36**). Y
arriba de los tres, **xAPI / IEEE 9274.1.1 sigue sin definir supresión**: todo esto es extensión propia de cada
implementación, **no portable**. Ver **P44**, y la corrección completa en `repos/foundations.md`.


## 55. El agujero de la cadena de borrado no está en el almacén: está en el enlace LMS → LRS, y lo documenta por escrito un LMS europeo de primera mano (agregado 2026-10-01, pase 21)

Con la tendencia 54, el diagnóstico de la cadena de supresión se reordena entero, y **el hueco se corre un eslabón**:

```
LMS (Moodle, Open edX, ILIAS)     LRS (lrsql, Learning Locker)     Modelo (pyKT / mastery)
   ✅ aprueba y ejecuta      ──?──▶   ✅ sabe borrar por actor    ──?──▶   🚫 gap 34
   el borrado del registro          (pase 21: existe y funciona)         (unlearning sin
   (pase 19: Privacy API)                                                 benchmark educativo)
                                 ▲
                      🔴 ACÁ está el agujero: no hay disparador,
                         no hay evento, y no es un problema de
                         capacidad sino de integración
```

**Lo nuevo de este pase es que el eslabón faltante está documentado por una de las partes.** El Feature Wiki de
**ILIAS** —LMS GPL-3.0 de referencia en DACH, 506 ★, 426 forks, rama `release_11` con **76.385 commits**— dice que al
borrar un objeto xAPI/cmi5 **el dato personal de los *statements* persiste en el LRS**, que una vez comunicado el dato
al LRS **ILIAS no tiene control sobre su borrado**, y que **no hay forma de borrar datos del LRS desde ILIAS**.

**Por qué vale más que un hallazgo de repo.** Hasta ahora el gap de propagación era **inferencia de esta KB**: el pase
19 lo midió en el árbol de Moodle y no encontró evento. Ahora hay **un segundo LMS, independiente, que lo declara por
escrito en su propia documentación de producto**. Dos implementaciones distintas, misma conclusión, y una de las dos
la publica como limitación conocida. **Eso convierte P40 de hipótesis técnica en limitación reconocida por el
proveedor** — que es exactamente lo que se necesita para ponerlo en el alcance de una propuesta sin que suene a
invento.

**Y hay una segunda mitad, puramente técnica, que decide arquitecturas antes de escribirlas.** En **Ralph** el borrado
no depende del LRS sino **del backend de datos elegido**: Mongo y Elasticsearch lo soportan, y
🔴 **ClickHouse lo declara explícitamente no soportado**, junto con `APPEND` y `UPDATE`. ClickHouse es el backend que
se elige **para analítica de aprendizaje a escala**. O sea: **el backend que se elige por performance es el que vuelve
imposible el art. 17**, y la decisión se toma al principio del proyecto, cuando nadie está mirando el GDPR.

⚠️ **Límite de verificación:** `docu.ilias.de` **está bloqueado por el proxy de egreso** de esta sesión. Lo de ILIAS
viene de **resultados de búsqueda sobre su Feature Wiki**, no de la página abierta; el repo sí se verificó de primera
mano vía WebFetch. **Antes de citar la limitación de ILIAS ante un cliente hay que abrir el wiki.** Lo de Ralph,
Learning Locker y `lrsql` está leído en el código y no tiene esa marca.


## 56. «No archivado» no es «mantenido»: el LRS más instalado del sector tiene cinco años sin un commit y se presenta como producto vivo (agregado 2026-10-01, pase 21)

**Learning Locker** es, según esta KB desde el pase 6, *«el LRS más adoptado de la categoría»*. Su repositorio
**no está archivado**, no tiene aviso de fin de vida, su README describe *«The Open Source Learning Record Store.
Started in 2014»* y remite a la oferta **comunitaria y comercial de Learning Pool** (585 ★, 294 forks, GPL-3.0,
verificado vía WebFetch el 2026-10-01).

**Y `git log` dice que el código no se mueve desde el 2021-11-16.** `HEAD` coincide exactamente con el tag **v7.1.1**,
el último publicado. Son **casi cinco años** — y en esos cinco años pasaron el art. 17 aplicado a EdTech, la COPPA
enmendada, el EU AI Act, AB 1159 y el incidente de Canvas.

**Las dos cosas son verdad al mismo tiempo y hay que decirlas juntas:** la API de borrado de Learning Locker
**existe, es correcta y este pase la verificó línea por línea**; y el software que la implementa **no recibe
mantenimiento**. Un cliente que ya lo tiene instalado —que es el caso más probable, por eso está en esta KB— tiene la
capacidad de cumplir el art. 17 y **no tiene a quién reportarle un bug de seguridad**.

**La regla, que es la contracara de la del pase 8.** Ahí la lección fue *leer el archivo `LICENSE`, no el badge*,
porque el badge mentía. **Acá es: leer el `git log`, no el banner de archivado.** GitHub marca «archivado» sólo cuando
el mantenedor decide marcarlo, y **el abandono silencioso no tiene insignia**. Para toda pieza que esta KB proponga
como **infraestructura instalada** —no como librería que se copia— la fecha del último commit es un dato de
elegibilidad, no un detalle de color. Es el mismo problema que el pase 12 encontró con `Continue` archivado y el pase
9 con las tres implementaciones de referencia de credenciales retiradas, pero **invertido**: ahí el proyecto avisó;
acá no.

36. **El borrado del LRS permisivo no deja evidencia de haber ocurrido** *(agregado en el pase 21 del 2026-10-01)*. Es lo que queda del gap 33 después de refutarlo, y es **el gap más chico, más concreto y más upstreameable que tuvo esta KB en veintiún pasadas.**

    **El hallazgo, leído en el código.** `lrsql` borra de forma completa y atómica — y **no devuelve ni registra nada sobre lo que borró**. El SQL `delete-actor-and-dependents!` está declarado `-- :result :affected`, así que **el conteo de filas afectadas se calcula y se descarta**; el interceptor responde `{:status 200 :body params}`, que es **el `actor-ifi` que mandó el cliente**. No hay registro de auditoría, no hay evento, no hay conteo. Learning Locker está un escalón mejor —expone `total`, `deleteCount`, `processing` y `done` para **sondear**— pero tampoco notifica, y 🔴 **su `done:true` no significa «borrado»**: tres caminos de error marcan el job terminado con `deleteCount` en `null`.

    **Por qué importa comercialmente, y es la parte que no es técnica.** El art. 17 del GDPR, **AB 1159** (California, operativa el **2027-07-01**) y la Ley 21.719 chilena no piden borrar: piden **poder demostrar que se borró**. Con `lrsql` tal como viene, la única prueba de una supresión es **un `200` con el input del propio pedido adentro**. Eso no es un expediente: es un recibo que el cliente se escribió a sí mismo.

    **Por qué es distinto de los gaps 31, 34 y 35.** Los gaps 31 y 34 esperan que un grupo de investigación libere código; el 35 es empaquetado de dos mitades que existen. **Éste es un parche de pocas líneas sobre un repo Apache-2.0**: el dato ya está calculado en la capa SQL y se tira. **No requiere investigación, no requiere ensamblado, y se contribuye hacia arriba** — a Yet Analytics, con lo que un entregable de cliente se convierte en posicionamiento público, igual que el camino que el pase 20 identificó para el gap 35. Ver **P44**.

    ⚠️ **Y los dos límites de alcance, para no venderlo más grande de lo que es.** Primero: devolver el conteo **no** resuelve el disparador LMS→LRS, que sigue siendo integración (**P40**). Segundo: el conteo de filas afectadas **no es** una prueba criptográfica de borrado — es telemetría de la operación. Para un régimen de alto riesgo hay que combinarlo con el registro del pedido en el LMS (`tool_dataprivacy`, pase 19) y con el expediente de **P35**.

## 57. La capa de analítica del LMS open source más desplegado es permisiva mientras su núcleo es AGPL — y trae el LRS puesto, así que la «elección de arquitectura» que esta KB suponía no existe (agregado 2026-10-01, pase 22)

**El dato.** **Aspects** (`openedx/tutor-contrib-aspects`, **Apache-2.0**, 14 ★, 32 forks, **2.269 commits**) es el
plugin de analítica y reporting **oficial** de Open edX, e instala vía Tutor un stack entero: **ClickHouse** +
**Apache Superset** + **Ralph** (el LRS) + **Vector** + **event-routing-backends** (xAPI) + **dbt**. Su complemento del
lado LMS/Studio, `openedx/platform-plugin-aspects` (**Apache-2.0**, 528 commits), empuja el dato a ClickHouse y
**embebe dashboards de Superset dentro de la interfaz del docente**.

**Por qué es tendencia y no una ficha de repo.** Dos cosas, y las dos cambian decisiones:

1. **El arbitraje de licencia se repite por tercera vez en esta KB.** Open edX es **AGPL-3.0** —el peor caso para
   SaaS—, pero **la capa que un estudio efectivamente customiza es Apache-2.0**. Es la misma forma que el pase 14
   encontró en la capa curricular y el pase 20 en la de conformidad: **lo que se toca es permisivo, lo copyleft es el
   sustrato que no se forkea.** Ya no es una casualidad: es el patrón de cómo se gobierna el open source educativo
   maduro —núcleo protegido, periferia abierta— y es a favor de quien construye.
2. **Para Open edX, el LRS no es una decisión.** Hasta el pase 21 esta KB razonaba el almacén como elección de
   arquitectura (`lrsql` para producción permisiva, Ralph para Open edX). **Si hay analítica oficial y trae el LRS
   puesto, el cliente no eligió: hereda.** Y hereda, específicamente, la configuración que el pase 21 declaró
   imposible de borrar. **El discovery tiene que preguntar qué stack de analítica corre, no qué LRS eligieron.**

⚠️ **Las estrellas de esta capa no miden nada** (14 y 6) y no hay que leerlas como tracción: es infraestructura de
plataforma, no un proyecto que compite por atención. La señal son los commits y la organización que publica.

## 58. Los dos LMS open source grandes divergen en la plomería del art. 17: en Moodle el disparador de supresión no existe, en Open edX es una señal del framework con listener permisivo (agregado 2026-10-01, pase 22)

**El dato, medido en los dos lados y en dos pases distintos:**

| | Moodle | Open edX |
|---|---|---|
| ¿Emite evento al aprobar/ejecutar una supresión? | 🚫 **No.** Pase 19: **187 archivos** de `tool_dataprivacy`, **cero** `trigger()`. `api::update_request_status()` es una escritura de base y nada más | ✅ **Sí.** Señal Django **`USER_RETIRE_LMS_MISC`** |
| ¿Hay listener que propague a la telemetría? | 🚫 No en el núcleo. El único antecedente (`local_gdpr_deleteuserdata`, GPL-3.0) **es de 2018 y pide Moodle 3.5** contra un núcleo en 5.3 | ✅ **`UserRetirementSink`** en `platform-plugin-aspects`, **Apache-2.0**, que borra la PII del usuario de ClickHouse |
| Cómo se construye el puente | **Sondeo** de `tool_dataprivacy_request.status` — la única superficie observable | **Ya construido.** Configuración y verificación |

**Por qué importa más que como detalle técnico.** Esta KB venía diciendo, desde el pase 19 y en **P40**, que el
disparador LMS → telemetría **no existe**. Dicho así es falso: **no existe en Moodle.** En Open edX existe, está en el
núcleo del ecosistema oficial y es permisivo. Consecuencias comerciales directas:

- **La elección de LMS del cliente ahora tiene una consecuencia de cumplimiento medible**, y es un argumento que se
  puede poner sobre la mesa en una evaluación de plataforma. No es preferencia: es cuánto cuesta el expediente del
  art. 17 sobre cada una.
- **Para un proyecto Moodle, el diseño ya no hay que inventarlo:** el `UserRetirementSink` es la implementación de
  referencia, permisiva y en producción, del extremo que recibe.

⚠️ **Y la simetría no es completa, así que no hay que venderla como tal:** el sink de Open edX borra **PII**, no el
registro de eventos. Ver la tendencia 59.

## 59. «Anonimizado» se está volviendo el argumento de retención por default: borrar el nombre y conservar la conducta, y ya son dos plataformas que lo documentan por escrito (agregado 2026-10-01, pase 22)

**El dato.** Ante un pedido de supresión, el stack oficial de Open edX borra las tablas de **PII**
(`user_profile`, `external_id`, `auth_user`, gobernadas por el flag `ASPECTS_ENABLE_PII`) y **conserva el dato de
eventos del usuario retirado**, con el argumento de que **queda anonimizado**. Y el pase 21 registró que el Feature
Wiki de **ILIAS** declara por escrito que al borrar un objeto xAPI/cmi5 el dato personal **persiste en el LRS** y que
ILIAS no tiene forma de borrarlo (tendencia **55**).

**Por qué es tendencia.** Son **dos proveedores europeos/globales de LMS que documentan el mismo límite en su propia
documentación de arquitectura**, en vez de ocultarlo. Eso tiene dos lecturas y las dos se usan:

- **A favor de una propuesta:** la carencia **no la inventa esta KB** — está escrita por el proveedor. Un argumento de
  cumplimiento que cita la decisión de arquitectura del propio producto es defendible ante un comité.
- **Como riesgo que hay que acotar:** un *statement* xAPI está indexado por un identificador de actor estable
  (`actor-ifi`). Un registro **pseudonimizado no es anónimo**, y bajo GDPR sigue siendo dato personal. **Si el
  identificador sobrevive a la retirada, «anonimizado» está haciendo un trabajo legal que puede no sostener** — y lo
  que queda retenido es el expediente conductual completo de alguien que ejerció el art. 17. Ése es el **gap 37**.

**ACTUALIZACIÓN DEL GAP 36 EN EL PASE 24 DEL 2026-10-01 — queda contestado con número, y el tamaño baja por segunda vez.**
El pase 23 lo dejó dimensionado *por lectura* y estimó *«un cambio en 4 archivos de 3 backends más el interceptor»*, porque
concluyó que en PostgreSQL y MariaDB el desglose por tabla exigía **partir el SQL**. **Se midió ejecutando, y no hace falta
partir nada:** pgjdbc y MariaDB Connector/J **parten ellos mismos** la cadena multi-sentencia y entregan **los siete
conteos, uno por tabla, en orden** (`[7, 2, 3, 8, 5, 6, 1]`) por el bucle `getMoreResults()` de JDBC estándar. El SQL no se
toca y los tres backends quedan simétricos: **lo único que hay que cambiar es la capa que recoge el resultado**, que lee un
conteo y nunca pide el siguiente.

Y aparece una trampa que el gap no tenía anotada: **el conteo único que hoy está disponible es el del PRIMER `DELETE`**, que
es el de `statement_to_statement` — **vale `0` para cualquier alumno sin sub-sentencias, que es el caso normal**. Medido: 25
filas borradas, el número disponible dice `0`. **Cablear ese conteo "porque ya está" produce un expediente que afirma algo
falso**, y eso es peor que el `200` vacío del pase 21. El gap 36 ya no es *«falta el número»*: es **«está el desglose, hay
que recogerlo entero y no confundirlo con el primero»**. Ver la tendencia **61** y el patrón **P47**.

38. **La supresión del alumno en MariaDB/MySQL cuelga de un parámetro de driver que una variable de entorno documentada apaga en silencio** *(agregado en el pase 24 del 2026-10-01)*. **Medido en este pase:** con `allowMultiQueries` en su default (`false`), `delete-actor-and-dependents!` **no se degrada, falla entera** — error **1064 / SQLState 42000** en el segundo de los siete `DELETE`. lrsql trae el parámetro, pero como *fallback* de **aero**: `:db-properties #or [#env LRSQL_DB_PROPERTIES "allowMultiQueries=true"]`, así que **cualquier** uso de `LRSQL_DB_PROPERTIES` —y `doc/postgres.md` enseña a usarla para `currentSchema`— **lo reemplaza entero y lo apaga**; `LRSQL_DB_JDBC_URL` hace lo mismo. Y `doc/env_vars.md` la describe como *«Optional **additional** DB properties»* con default *«Not set»*: **inexacto en los dos campos** para estos backends.

    **Por qué es el gap más accionable de esta KB sobre este repo, y el más barato de los siete pases que lleva mirándolo.** No hay que tocar SQL ni lógica, y no requiere investigación ni ensamblado: son **dos líneas de documentación mal escritas**, una advertencia ausente en `doc/mariadb.md`, y una decisión de diseño de configuración —**fusionar** en vez de reemplazar, o, más barato todavía y sin cambiar semántica de aero, **fallar al arrancar** cuando el backend es MariaDB/MySQL y `allowMultiQueries` no quedó activo—. Es *upstream* puro a Yet Analytics, igual que el gap 36, y se contribuye con un test de regresión que hoy no existe.

    **Y es el único gap de esta KB cuyo síntoma es la ausencia de un borrado en vez de la ausencia de su prueba.** Los gaps 36 y 37 son sobre **evidencia**; éste es sobre **capacidad**: el despliegue ingiere, consulta y pasa el *health check* con normalidad, porque el borrado de actor es la única operación del producto que manda varias sentencias en un paquete. **El fallo se manifiesta la primera vez que alguien ejerce el art. 17** — el día en que hay expediente abierto y plazo corriendo. Ver la tendencia **62** y el patrón **P47**.

    ⚠️ **Lo declarado y no verificado:** que ésa sea la *única* consulta multi-sentencia del producto no se enumeró — el clasificador de seguridad del entorno bloqueó el recorrido masivo del árbol clonado. Si una migración de arranque también lo fuera, el síntoma sería **más** visible y por lo tanto menos peligroso que lo descrito.

**La consecuencia práctica, que es de redacción de propuesta.** Sobre Open edX + Aspects la frase correcta **no es**
*«cumplimos el derecho al olvido»*; es *«se suprime la identificación directa y se conserva el registro de actividad
pseudonimizado, cuya base legal de retención se declara»*. La primera no se sostiene en una inspección; la segunda sí.
Ver **P45**.

⚠️ **Verificación declarada:** el `UserRetirementSink`, la señal y las tablas de PII están **verificados de primera
mano** (README de `platform-plugin-aspects`). La afirmación de que *el dato de eventos se conserva porque queda
anonimizado* viene de **snippets concordantes de búsqueda, no de lectura directa**: el ADR que la contiene está en
`docs.openedx.org`, **bloqueado por el proxy de egreso** en este pase, y los dos caminos alternativos probados
devolvieron 404. URL anotada para el próximo pase:
`https://docs.openedx.org/projects/openedx-aspects/en/latest/technical_documentation/decisions/0009_pii.html`.

## 60. La capacidad de probar un borrado no es portable entre bases de datos, y eso contradice la razón por la que esta KB recomienda su LRS por default (agregado 2026-10-01, pase 23)

**El pase 22 dejó escrita una sub-pregunta y declaró que no la pudo contestar** (el clasificador de seguridad del entorno
bloqueó la traza del árbol clonado): *«¿`-delete-actor` ya devuelve los conteos de filas afectadas, o hay que plomearlos
desde la capa SQL? Si ya los devuelve, el parche es una línea; si no, hay que propagarlos.»* Este pase clonó
`yetanalytics/lrsql` y leyó **los tres backends**. **La respuesta es ninguna de las dos opciones, y la diferencia es
arquitectónica, no de tamaño.**

Los conteos **ya existen en los tres backends**: toda sentencia de borrado de actor está declarada `-- :result :affected`.
Lo que no existe es **una sola forma de recogerlos**:

| Backend | Cómo está escrito el borrado | Cuántos conteos hay disponibles | Qué devuelve hoy |
|---|---|---|---|
| **SQLite** · `src/db/sqlite/lrsql/sqlite/record.clj:169–176` | **Siete queries HugSQL con nombre propio** (`delete-actor-st2st`, `-st2activ`, `-attachments`, `-statements`, `-agent-profile`, `-state-document`, `-actor`), cada una con `:result :affected` | **Siete, uno por tabla** | **Uno solo.** El cuerpo las invoca como siete expresiones sueltas en secuencia, así que Clojure **devuelve el valor de la séptima** (`delete-actor-actor`) y **descarta las otras seis** — y la séptima es la menos informativa de todas: el borrado de la fila del propio actor, que es 0 o 1 |
| **PostgreSQL** · `postgres/record.clj:135–136` | **Un único nombre HugSQL** (`delete-actor-and-dependents!`) cuyo cuerpo son **siete `DELETE` separados por `;`** bajo un solo `:command :execute` / `:result :affected` | **Uno** | Ese uno, que el interceptor igual descarta |
| **MariaDB** · `mariadb/record.clj:116–117` | Idéntico a PostgreSQL: un nombre, siete `DELETE` adentro | **Uno** | Ídem |

🔴 **Las dos consecuencias, y la segunda es la que importa comercialmente.**

**1. El parche del gap 36 no es de una línea en ningún backend, y no es el mismo parche en ninguno.** En **SQLite** es
mecánico pero no trivial: hay que envolver las siete llamadas en un `let` y devolver un mapa por tabla (~8 líneas) — el dato
ya está, sólo se está tirando. En **PostgreSQL y MariaDB** *no se puede obtener el desglose por tabla sin partir el SQL* en
siete queries con nombre, como SQLite ya las tiene: deja de ser plomería y pasa a ser **refactor del SQL**. Con eso, la
estimación honesta del gap 36 sube de *«una línea»* a **un cambio en 4 archivos de 3 backends más el interceptor**, y sigue
siendo chico y upstreameable, pero hay que presupuestarlo como tal.

**2. Y acá está el hallazgo que da vuelta un argumento de esta KB.** La fila de `lrsql` en `verticals/solutions.md` lo
recomienda como **«el default»** con esta razón textual: *«corre sobre la base de datos que el cliente ya opera, así que no
agrega una pieza de infraestructura nueva al diagrama»*. Eso sigue siendo cierto para **almacenar**. **Para *probar* un
borrado no lo es:** la evidencia disponible depende del motor que el cliente eligió por motivos que no tienen nada que ver
con privacidad. **Un despliegue sobre SQLite puede dar hoy un desglose de siete tablas con ~8 líneas; el mismo producto
sobre PostgreSQL no puede dar más de un número sin tocar el SQL.** Para un expediente del **art. 17** o de **AB 1159**
(operativa el **2027-07-01**), donde lo que se audita es la *prueba*, eso significa que **la portabilidad de base de datos
—la ventaja que vendemos— es también una asimetría de cumplimiento que hay que declarar en la propuesta.**

**La regla operativa que deja este pase:** cuando el alcance incluya evidencia de supresión, **el motor de base de datos
deja de ser una decisión de infraestructura del cliente y pasa a ser una decisión de cumplimiento del proyecto.** Hay que
preguntarlo en el *discovery*, no descubrirlo en la auditoría. Ver **P45**.

⚠️ **Verificación declarada.** Los tres `record.clj`, los tres `delete.sql`, `ops/command/statement.clj`,
`system/lrs.clj:459–463`, `admin/protocol.clj:58` y `admin/interceptors/lrs_management.clj:23–33` están **leídos de primera
mano sobre el árbol clonado** (`git clone --depth 1`, HEAD del 2026-10-01). **Lo que NO se verificó ejecutando:** qué número
devuelve exactamente el driver JDBC para un `:execute` multi-sentencia en PostgreSQL y MariaDB — si el del primer `DELETE`,
el del último o la suma. La lectura del código prueba que **hay un solo valor disponible**, que es lo que sostiene el
argumento; **cuál de los siete es ese valor no se midió y no se infiere.** Es la acción que este pase deja escrita: levantar
`lrsql` sobre PostgreSQL, borrar un actor con datos en las siete tablas y leer el valor. Es una tarde de trabajo y cierra el
gap 36 con número en vez de con lectura.

## 61. El desglose de un borrado no hay que construirlo: ya viene en el cable y se descarta — y el número que la aplicación sí puede leer es `0` para el alumno típico (agregado 2026-10-01, pase 24)

**El pase 23 dejó escrita una acción concreta y acotada:** *«levantar `lrsql` sobre PostgreSQL, borrar un actor con datos en
las siete tablas y leer el valor. Es una tarde de trabajo y cierra el gap 36 con número en vez de con lectura.»*
**Se ejecutó en este pase, y el resultado corrige la conclusión arquitectónica del pase 23, no la confirma.**

### Cómo se midió (y por qué el fixture está armado así)

| | |
|---|---|
| **Árbol** | `yetanalytics/lrsql` clonado, HEAD `cb794e4` |
| **Esquema** | Las tablas creadas **con el DDL propio de lrsql**, extraído de `src/db/postgres/lrsql/postgres/sql/ddl.sql` — no un esquema equivalente escrito a mano |
| **Migración aplicada** | `add-statement-to-actor-cascading-delete!`, así que el fixture es un despliegue **migrado**, como el de producción. Verificado en `pg_constraint`: `statement_fk … REFERENCES xapi_statement(statement_id) ON DELETE CASCADE` |
| **SQL bajo prueba** | El cuerpo literal de `delete-actor-and-dependents!` de `delete.sql`, con `:actor-ifi` sustituido por `?` — **las 8 ocurrencias**, que es lo que emite HugSQL |
| **Motor y driver** | PostgreSQL **16.14** + **pgjdbc 42.7.4**; y MariaDB **10.11.14** + **Connector/J 3.4.1** |
| **El truco del fixture** | Se sembró un conteo **distinto por tabla** (7, 2, 3, 8, 5, 6, 1) para que el número que vuelve sea **identificable**: primero=7, último=1, suma=32, máximo=8, todos distintos entre sí |

### Lo que devolvió, medido

```
MODE=prepared  execute()->hasResultSet=false
  getUpdateCount() INMEDIATAMENTE DESPUÉS de execute()  = 7
  TODOS los conteos vía el bucle getMoreResults()        = [7, 2, 3, 8, 5, 6, 1]
  first=7  last=1  sum=32  max=8
MODE=executeUpdate  returned = 7
```

🔴 **Hallazgo 1 — y corrige al pase 23.** El pase 23 escribió que en PostgreSQL y MariaDB *«no se puede obtener el desglose
por tabla sin partir el SQL»*, y que por eso el gap 36 *«deja de ser plomería y pasa a ser refactor del SQL»*.
**Es falso, y se mide arriba:** pgjdbc **parte él mismo** la cadena multi-sentencia y expone **los siete conteos, uno por
tabla, en el orden de los siete `DELETE`**, a través del bucle `getMoreResults()` que es JDBC estándar desde 1997.
**El desglose por tabla ya viaja por el cable.** Lo mismo, idéntico, en MariaDB con `allowMultiQueries=true`:
`[7, 2, 3, 8, 5, 6, 1]`.

**Entonces el gap 36 vuelve a bajar de tamaño, y por segunda vez.** No es un refactor del SQL ni hay que partir
`delete-actor-and-dependents!` en siete queries con nombre: lo que hay que cambiar es **la capa que recoge el resultado**,
que lee un conteo y nunca pide el siguiente. El SQL no se toca y los tres backends quedan simétricos.

🔴 **Hallazgo 2, y es el que hay que llevar a la reunión.** El único número que hoy queda disponible —el que
`getUpdateCount()` devuelve, y el mismo que devuelve `executeUpdate()`— **es el del PRIMER `DELETE`**, no el del último
ni la suma. Y el primer `DELETE` de la secuencia es el de **`statement_to_statement`**: la tabla de aristas entre
sentencias, que **sólo tiene filas si las sentencias del alumno tienen anidamiento o *voiding***.

**Para el alumno corriente, que no tiene sub-sentencias, ese número es `0`.** Medido, borrando el mismo actor con el
fixture sin filas en `statement_to_statement`:

```
  getUpdateCount() INMEDIATAMENTE DESPUÉS de execute()  = 0
  TODOS los conteos vía el bucle getMoreResults()        = [0, 2, 3, 8, 5, 6, 1]
  first=0  last=1  sum=25  max=8
```

**Veinticinco filas borradas, y el único testigo disponible dice `0`.** Esto cambia el consejo del pase 23 en un punto
que importa: **el parche del gap 36 hecho de la manera obvia —cablear el conteo que ya está— produce un expediente que
afirma «0 filas borradas» sobre una supresión exitosa.** Un oficial de privacidad que lea eso concluye, con razón, que
no se borró nada. **Un número incorrecto es peor que el `200` vacío que el pase 21 denunció**, porque el `200` vacío no
afirma nada y el `0` afirma algo falso. El parche correcto es el bucle completo, no el conteo único.

### Hallazgo 3 — la tabla que une a la persona con su rastro no se borra nunca de forma explícita, y por eso no aparece en ningún conteo

Los siete `DELETE` **no incluyen `statement_to_actor`**, que es justamente la tabla que vincula al alumno con sus
sentencias. Las cuatro primeras sentencias **la leen** en subconsultas, pero nadie la borra. Sus filas desaparecen
**sólo por `ON DELETE CASCADE`** desde `xapi_statement`, y **las filas borradas en cascada no se cuentan en ningún
*update count* de JDBC**. En el fixture eran **10 filas** (8 del alumno y 2 del docente que aparecía en las mismas
sentencias) y **ninguna de las dos mediciones las ve**.

Y el camino por el que existe esa cascada **no es el mismo en los dos motores**, lo que importa para auditar un
despliegue ajeno:

| Motor | Cómo llega la cascada | Consecuencia operativa |
|---|---|---|
| **MariaDB** | **Nativa en la definición de la tabla** (`statement_fk_stactor`, verificado `CASCADE` en `information_schema.referential_constraints`) | Está desde la creación del esquema |
| **PostgreSQL** | **Por migración**: `add-statement-to-actor-cascading-delete!`, condicionada por `check-statement-to-actor-cascading-delete` | **Depende de que `-update-all!` haya corrido.** En un despliegue viejo sin migrar, la cascada no está |

**La regla operativa:** incluso con el bucle completo de siete conteos, **el expediente sigue subdeclarando el borrado**,
porque la tabla de vínculo se va en silencio. Un expediente honesto tiene que contar las filas en cascada aparte —con un
`SELECT` previo— o decir explícitamente que no las cuenta. Ver **P47**.

⚠️ **Verificación declarada.** Todo lo de arriba está **ejecutado en este pase**, no leído: PostgreSQL 16.14 y MariaDB
10.11.14 levantados localmente, esquema creado con el DDL de lrsql, los conteos impresos por un arnés JDBC propio sobre
los drivers oficiales. **Lo que NO se midió:** (1) el valor que entrega `next.jdbc` con `:result :affected` *dentro* de
lrsql —el repositorio de artefactos Clojure (`repo.clojars.org`) responde **403** a través del proxy de egreso de esta
sesión, así que no se pudo resolver `next.jdbc` ni el adaptador de HugSQL y **la cadena se midió a la altura del driver,
que es donde estaba la pregunta abierta**; la lectura del pase 23 sobre el interceptor que descarta el valor sigue en
pie y no se repitió. (2) **Cuántas otras consultas multi-sentencia tiene lrsql**: el clasificador de seguridad del
entorno bloqueó el recorrido masivo del árbol clonado, así que el *blast radius* de la tendencia **62** queda sin
enumerar y se declara como tal.


## 62. La supresión del alumno en el LRS que esta KB recomienda depende de un parámetro de driver que una variable de entorno no relacionada apaga en silencio (agregado 2026-10-01, pase 24)

Esta tendencia **no se buscó**: salió de armar el fixture de la tendencia **61** sobre MariaDB. Es el hallazgo más
accionable del pase y el único que puede dejar una supresión del **art. 17** sin ejecutar.

### El síntoma, medido

Con el **driver en su configuración por default** —`allowMultiQueries` sin tocar, que en MariaDB Connector/J es
`false`— la consulta `delete-actor-and-dependents!` **no se degrada: falla entera**:

```
driver: MariaDB Connector/J 3.4.1   db: MariaDB 10.11.14
  SQLException: java.sql.SQLSyntaxErrorException
  message: You have an error in your SQL syntax; ... near
           'DELETE FROM statement_to_activity WHERE statement_id IN ( SELECT statement_...' at line 11
  SQLState: 42000   vendorCode: 1064
```

El servidor corta en el **segundo** `DELETE` de los siete. Con `allowMultiQueries=true` en la URL, la misma consulta
sobre el mismo esquema y los mismos datos funciona y devuelve `[7, 2, 3, 8, 5, 6, 1]`. **El parámetro es la diferencia
entre borrar y no borrar.**

### Por qué eso no es un bug de lrsql, y es peor que un bug

🔴 **lrsql sí trae el parámetro puesto — pero como *fallback*, no como base.** En
`resources/lrsql/config/prod/mariadb/database.edn:5` (y el equivalente de `mysql`), leído de primera mano:

```clojure
:db-properties #or [#env LRSQL_DB_PROPERTIES "allowMultiQueries=true"]
```

El `#or` de **aero** devuelve **el primer valor no nulo**. O sea: **si el operador define `LRSQL_DB_PROPERTIES` por
cualquier motivo, su string REEMPLAZA al default completo** y `allowMultiQueries=true` **desaparece**. No se fusiona.
No avisa. Y hay un segundo camino con el mismo efecto: `LRSQL_DB_JDBC_URL`, que —según `doc/env_vars.md`— *«overrides
the above properties if set»*, así que una URL JDBC entregada a mano también se lleva el parámetro puesto.

**Y la documentación empuja al operador exactamente hacia ahí.** `doc/env_vars.md` describe `LRSQL_DB_PROPERTIES` como
*«Optional **additional** DB properties»* con default *«Not set»*. **Las dos cosas son inexactas para MariaDB y MySQL:**
no es *additional* —es reemplazo— y el default **no** es *not set*, es `allowMultiQueries=true`. Peor: el propio
`doc/postgres.md` le enseña al lector a usar `LRSQL_DB_PROPERTIES` para fijar `currentSchema`, y `doc/mariadb.md`
**no menciona el tema en ninguna línea**. Un operador de MariaDB que quiera fijar un timeout, un `sessionVariables` o
TLS hace lo que la documentación le enseñó y **apaga la supresión del alumno sin enterarse**.

### Por qué no se nota hasta el peor momento posible

La consulta del borrado de actor es **la única operación del producto que depende de enviar varias sentencias en un
paquete**. Todo lo demás —ingesta de sentencias, consultas, documentos de estado, credenciales— es de una sentencia por
viaje y **sigue funcionando perfecto**. Así que el despliegue se ve sano: ingiere, consulta, responde, pasa el
*health check*. **El fallo aparece la primera vez que alguien ejerce el derecho al olvido**, que es, por definición, el
día en que hay un expediente abierto y un plazo corriendo.

⚠️ **El alcance exacto queda declarado, no afirmado.** Que el borrado de actor sea la *única* consulta multi-sentencia
de lrsql es lo que se desprende de las lecturas de los pases 21 a 23 y de este, **pero no se enumeró**: el clasificador
de seguridad del entorno bloqueó el recorrido masivo del árbol clonado. Si alguna migración de arranque también fuera
multi-sentencia, el síntoma sería más visible (fallaría al levantar) y por lo tanto **menos** peligroso que lo descrito.
Lo que sí está medido es que **con el default del driver, el borrado falla**, y que **lrsql no lo documenta**.

### Lo que esto cambia en la postura comercial

| | |
|---|---|
| **Lo que esta KB venía diciendo** | `lrsql` es el LRS por default porque corre sobre la base que el cliente ya opera (ver `verticals/solutions.md`) |
| **Lo que agrega el pase 23** | La *evidencia* de un borrado no es portable entre motores (tendencia **60**) |
| 🔴 **Lo que agrega este pase** | En MariaDB y MySQL, **la capacidad misma de borrar** cuelga de un parámetro de driver que una variable de entorno documentada y no relacionada apaga en silencio |

**Es, además, el *upstream* más chico y más defendible que encontró esta KB en siete pases sobre este repo:** no requiere
tocar SQL ni lógica. Son tres cosas —corregir dos líneas de `doc/env_vars.md`, advertirlo en `doc/mariadb.md`, y
**fusionar** `LRSQL_DB_PROPERTIES` con el default en vez de reemplazarlo (o, más barato y sin cambiar semántica,
**fallar al arrancar** si el backend es MariaDB/MySQL y `allowMultiQueries` no quedó activo)—. Ese es el **gap 38**.
Ver **P47**.


## Fuentes

### Pase 24 (2026-10-01) — medición propia y fuentes del barrido

**Medición de primera mano (ejecutada en este pase, no leída).** `yetanalytics/lrsql` HEAD `cb794e4`; esquema creado con el
DDL propio del proyecto (`src/db/{postgres,mariadb}/lrsql/*/sql/ddl.sql`); SQL bajo prueba: el cuerpo literal de
`delete-actor-and-dependents!` de `delete.sql` con las 8 ocurrencias de `:actor-ifi` como `?`. Motores: **PostgreSQL 16.14**
(pgjdbc **42.7.4**) y **MariaDB 10.11.14** (Connector/J **3.4.1**). Configuración leída en
`resources/lrsql/config/prod/mariadb/database.edn`, `resources/lrsql/config/prod/postgres/database.edn`,
`src/main/lrsql/system/util.clj` (`make-jdbc-url`), `doc/env_vars.md`, `doc/postgres.md`, `doc/mariadb.md`.

**Repos verificados vía WebFetch** (y no por `curl`: el proxy de egreso de esta sesión devuelve **403 a todo github.com**,
que es la advertencia del pase 12 —*un 403 de `curl` no es un 404*— y por eso la verificación de URL se hace con WebFetch,
que distingue contenido real de un 404 real): [UOC/java-lti-1.3](https://github.com/UOC/java-lti-1.3) ·
[UOC/spring-boot-lti-advantage](https://github.com/UOC/spring-boot-lti-advantage) ·
[UOC/java-lti-1.3-platform](https://github.com/UOC/java-lti-1.3-platform) ·
[UOC/java-lti-1.3-provider-example](https://github.com/UOC/java-lti-1.3-provider-example) ·
[packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) ·
[1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) (atribución a Turnitin) ·
[gnowledge/OpenAssessmentsClient](https://github.com/gnowledge/OpenAssessmentsClient) ·
[OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic). **404 confirmados:** `UOC/java-lti-1.3-provider`,
`LongsightGroup/qti3-core`.

**Barrido de mercado.** MarketsandMarkets (North America AI in education) · Technavio · azumo (compilación de estadísticas) ·
[Consejo de Europa — 2.ª conferencia de trabajo sobre regulación de AI en educación](https://coe.int/web/education) ·
QS (2026 Europe EdTech 200+) · [itnews.asia — AI sovereignty in Asia Pacific 2026](https://www.itnews.asia/news/ai-sovereignty-will-set-the-pace-for-asia-pacific-in-2026-623233) ·
[UNU/UNESCO — AI implementation in higher education in LAC](https://unu.edu/publication/ai-implementation-higher-education-latin-america-and-caribbean) ·
[BID/IADB — An Enabling Regulatory Framework for AI in LAC](https://publications.iadb.org/publications/english/document/An-Enabling-Regulatory-Framework-for-Artificial-Intelligence-in-Latin-America-and-the-Caribbean.pdf).


### Verificación del pase 23 (2026-10-01)

🟢 **Verificado de primera mano leyendo el código fuente**, con `git clone --depth 1` sobre el árbol real (no vía WebFetch,
no vía documentación): [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) — **Apache-2.0**. Leídos en este pase:
**`src/db/sqlite/lrsql/sqlite/record.clj:169–176`** (las siete llamadas secuenciales y el retorno de la séptima),
**`src/db/postgres/lrsql/postgres/record.clj:135–136`** y **`src/db/mariadb/lrsql/mariadb/record.clj:116–117`** (el nombre
único `delete-actor-and-dependents!`), los tres **`sql/delete.sql`** (siete `DELETE` en cada backend; `:result :affected`
declarado en **todas** las sentencias, y en SQLite **siete nombres HugSQL separados** frente a **uno** en Postgres/MariaDB),
`src/main/lrsql/ops/command/statement.clj:74–76` (`delete-actor!` es *pass-through* a `bp/-delete-actor!`),
`src/main/lrsql/system/lrs.clj:459–463`, `src/main/lrsql/admin/protocol.clj:58` (`-delete-actor` pertenece a
`AdminLRSManager`), `src/main/lrsql/backend/protocol.clj:42` y
`src/main/lrsql/admin/interceptors/lrs_management.clj:23–33`. **Esto contesta la sub-pregunta que el pase 22 dejó abierta y
no pudo responder** (ver tendencia **60** y **P46**).

🟢 **Verificado vía WebFetch** (licencia, estrellas, commits y lenguaje leídos en la página del repo el 2026-10-01):
[frappe/education](https://github.com/frappe/education) — **657 ★, 1.091 commits, Python, rama `develop`**; la licencia **no
aparece en la página** y se leyó en **`license.txt` (HTTP 200): «GNU GPL V3»**, aplicando la regla de método del pase 10
(verificar contra el archivo de licencia, no contra el README) · [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp)
— **MIT, 12k ★, 3.794 commits, PHP (Laravel 13 + FilamentPHP 5)**, y **sin ningún módulo educativo** entre sus plugins.

⚠️ **Nota de método, que reconfirma la del pase 12 y conviene no volver a olvidar.** `curl -sI` contra `github.com` devolvió
**HTTP 403** para los tres repos de este pase. **Un 403 del proxy de egreso no es un 404 y no invalida un repo**: los tres se
verificaron por vías más fuertes —`lrsql` **clonado**, los otros dos **leídos en la página vía WebFetch**— y
`raw.githubusercontent.com` sí responde **200**. **La regla operativa: cuando `curl` da 403, cambiar de herramienta, no
descartar el hallazgo.**

🔴 **No verificado, y declarado como tal:** cuál de los siete `DELETE` reporta el driver JDBC en el `:execute`
multi-sentencia de PostgreSQL y MariaDB (el primero, el último o la suma). **No se midió ejecutando y no se infiere.** La
lectura del código prueba que hay **un solo valor disponible**, que es lo que sostiene la tendencia 60; el valor exacto es la
acción escrita que este pase deja para el próximo. **Todo lo regulatorio de este pase viene de resultados de búsqueda** —los
134 proyectos en 31 estados, Idaho SB 1227, Oregon S.B. 1546, Washington H.B. 2225, el AI Basic Act coreano (2026-01-22), la
Decisión 33/2026/QD-TTg de Vietnam y CONPES 4144—: **hay que abrir el texto normativo antes de usarlos con un cliente.**

Cadena de borrado en la capa de telemetría — **pase 21 (2026-10-01)**. 🟢 **Verificado de primera mano leyendo el
código fuente**, clonando cada repo con `git clone --depth 1 --filter=blob:none` y leyendo los archivos citados (no vía
WebFetch, no vía documentación):

- [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) — **Apache-2.0**, HEAD `2d24f2d` del **2026-09-04**.
  Leídos: `src/main/lrsql/admin/routes.clj` (ruta `["/admin/agents" :delete …]`, línea 331, y el registro condicional
  de la línea 407), `src/main/lrsql/admin/interceptors/lrs_management.clj` (la respuesta
  `{:status 200 :body params}`), `src/main/lrsql/spec/admin.clj` (`delete-actor-spec`, un solo campo `actor-ifi`),
  `src/main/lrsql/system/lrs.clj` (`-delete-actor`, dentro de `jdbc/with-transaction`),
  `src/main/lrsql/ops/command/statement.clj` (`delete-actor!`),
  **`src/db/postgres/lrsql/postgres/sql/delete.sql`** (`delete-actor-and-dependents!`, las 7 sentencias `DELETE` y la
  declaración `-- :result :affected`), `src/db/postgres/lrsql/postgres/sql/ddl.sql` (DDL de `statement_to_actor` y la
  migración `check-statement-to-actor-cascading-delete` / `add-statement-to-actor-cascading-delete!`),
  `resources/lrsql/config/prod/default/webserver.edn` (**`LRSQL_ENABLE_ADMIN_DELETE_ACTOR` default `false`**) y
  `LICENSE`.
- [LearningLocker/learninglocker](https://github.com/LearningLocker/learninglocker) — **GPL-3.0**, HEAD `5fec948`,
  que **coincide con el tag `v7.1.1`**, del **2021-11-16** (verificado con `git log -1` y `git ls-remote --tags`).
  Leídos: `api/src/routes/HttpRoutes.js`, `lib/constants/routes.js` (las rutas
  `/batchdelete/initialise|terminate/:id|terminate/all`), `api/src/controllers/BatchDeleteController.js`,
  `worker/src/handlers/batchStatementDeletion/batchStatementDeletion.js` (`Statement.deleteMany`, el `markDone` de los
  tres caminos de error, el re-encolado por páginas), `lib/models/batchDelete.js` (`total`, `deleteCount`,
  `processing`, `done`, `pageSize` 1000, y las funciones de ventana), `lib/models/siteSettings.js` (los tres campos
  `batchDeleteWindow*`) y `cli/src/scheduler/batchDelete.js` (el rescate de los jobs fuera de ventana).
- [openfun/ralph](https://github.com/openfun/ralph) — **MIT** (`LICENSE.md`, France Université Numérique), HEAD
  `53cc58c` del **2026-09-07**. Leídos: `src/ralph/api/routers/statements.py` (**sólo `@router.get`, `@router.put` y
  `@router.post`; no existe `@router.delete` en ningún router**), `src/ralph/backends/data/base.py`
  (`BaseOperationType`), `src/ralph/backends/data/mongo.py` (`_bulk_delete`, `unsupported_operation_types`),
  `src/ralph/backends/data/es.py` y **`src/ralph/backends/data/clickhouse.py`** (`DELETE` dentro de
  `unsupported_operation_types` y el docstring que lo declara).

Verificado vía **WebFetch** el 2026-10-01 (estrellas, forks, licencia y estado del repo leídos en la página):
[learninglocker](https://github.com/LearningLocker/learninglocker) (585 ★, 294 forks, GPL-3.0, **no archivado y sin
aviso de fin de vida** — ver tendencia 56) · [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS)
(506 ★, 426 forks, **GPL-3.0**, PHP, rama `release_11`, 76.385 commits) ·
[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (reverificación independiente: **40.6k ★**, Apache-2.0,
**2.386 commits**, **v1.6.12 del 2026-09-27** — coincide con el pase 20).

🔴 **No verificado de primera mano en el pase 21:** la limitación de **ILIAS** sobre xAPI/cmi5 y el LRS
(*«el dato personal de los statements persiste en el LRS»*, *«no hay forma de borrar datos en el LRS desde ILIAS»*)
viene del **Feature Wiki de ILIAS vía resultados de búsqueda**: **`docu.ilias.de` está bloqueado por el proxy de
egreso** (`EGRESS_BLOCKED`, reintentado en este pase). Es la afirmación que sostiene la mitad documental de la
tendencia **55** y **hay que abrir el wiki antes de citarla ante un cliente**. Contexto adicional sobre xAPI y GDPR
tomado de fuentes secundarias concordantes: [Learning Pool — cómo xAPI ayuda con
GDPR](https://learningpool.com/how-xapi-helps-solve-for-gdpr-requirements) · [Watershed — GDPR, xAPI y
herramientas](https://www.watershedlrs.com/blog/product/news/what-is-gdpr/) · [Rustici — GDPR en SCORM
Cloud](https://rusticisoftware.com/products/gdpr/).

Barrido regional del pase 21 (🔴 **ninguna fuente abierta de primera mano; todo de resultados de búsqueda**):
[MarketsandMarkets — North America AI in Education](https://www.marketsandmarkets.com/Market-Reports/geography/ai-in-education-market/North-America) ·
[Technavio — AI en el sector educativo](https://technavio.com/report/artificial-intelligence-market-in-the-education-sector-industry-analysis) ·
[CompTIA — tendencias EMEA 2026](https://www.comptia.org/en/blog/five-tech-trends-shaping-emeas-it-strategy-in-2026/) ·
[Consejo de Europa — dimensiones regulatorias de la AI en educación](https://coe.int/web/education/-/key-stakeholders-across-europe-will-explore-the-regulatory-dimensions-of-ai-in-education-at-the-2nd-working-conference-in-october) ·
[QS — Europe EdTech 200 y London EdTech Week 2026](https://newsletters.qs.com/announcing-the-2026-europe-edtech-200-plus-london-edtech-week-ai-skills-and-policy-moves/) ·
[IntelligentCIO APAC — brechas de gobernanza de AI en directorios APAC 2026](https://www.intelligentcio.com/apac/2025/12/09/ai-governance-gaps-widen-as-apac-boards-prioritise-innovation-for-2026/) ·
[UNU/UNESCO — AI en educación superior en LAC](https://unu.edu/publication/ai-implementation-higher-education-latin-america-and-caribbean) ·
[BID — marco regulatorio habilitante para AI en LAC](https://publications.iadb.org/publications/english/document/An-Enabling-Regulatory-Framework-for-Artificial-Intelligence-in-Latin-America-and-the-Caribbean.pdf) ·
[Barchart — adopción de AI en LATAM, expectativas 2026](https://www.barchart.com/story/news/36012717/industry-demand-is-driving-ai-adoption-from-the-ground-up-in-latin-america-heres-what-to-expect-in-2026)

## 63. De los dos estándares de analítica de aprendizaje, uno dejó de ser open source — con fecha, y hace tres años (agregado 2026-10-01, pase 25)

**El hallazgo:** 1EdTech **movió los repositorios de Caliper Analytics a privado el 2023-06-17**, y el acceso quedó para
*Contributing Members* y *Affiliates*. No es una inferencia: **la descripción del repo `1EdTech/caliper-java` es
literalmente el aviso** — *«NOTICE: 1EdTech will be moving Caliper to private repositories on June 17, 2023. Access to
the repositories will be available for 1EdTech Contributing Members and Affiliates.»*

Medido contra el otro estándar de la misma función:

| | **xAPI** (ADL → IEEE) | **Caliper Analytics** (1EdTech) |
|---|---|---|
| Especificación pública | `adlnet/xapi-profiles` — **Apache-2.0** ✅, 60 ★, 33 forks, 153 commits, viva | `1EdTech/caliper-spec` — 22 ★, **IMS Specification Document License** ⚠️ **no OSI** |
| Implementación de referencia | **Pública y permisiva:** `yetanalytics/lrsql` + **`yetanalytics/xapipe`** (Apache-2.0, 17 ★) | 🔴 **Privada.** `caliper-java`, `caliper-js`, `caliper-python`: **404** |
| Lo que queda público | — | `caliper-js-example` (**LGPL-3.0**, 8 ★, **©2018**) y `caliper-ontology`, **archivado** en 2019 |
| Trabajo normativo | **IEEE p9274.2.1 activo** tras xAPI 2.0 | Caliper 1.2, con implementaciones cerradas |

**Por qué es una tendencia y no un dato de catálogo.** Es la instancia más nítida del patrón *«estándar instalado vs.
modelo propio»* que esta KB nombró en la **tendencia 29**, y con una vuelta nueva: acá **el estándar sigue instalado
—los LMS siguen emitiendo Caliper— pero su implementación dejó de ser construible.** Eso **traslada costo al integrador**:
el cliente tiene un LMS que habla Caliper y un proveedor que, si no es miembro del consorcio, **tiene que escribir el
adaptador**. Y explica hacia atrás por qué toda la capa de telemetría que esta KB levantó en diez pases es xAPI: **no fue
una preferencia de esta base, fue el único lado del que había código.**

🔵 **La regla operativa, desde el pase 25:** se propone **xAPI**. Cuando el cliente pida Caliper, se le dice que **la
especificación es legible pero las implementaciones no son open source desde junio de 2023** y se cotiza el adaptador
como trabajo, no como configuración. Y `yetanalytics/xapipe` (*LRSPipe*) es la pieza que faltaba en el medio: **filtra
telemetría por *statement template* y por *pattern* de un xAPI Profile**, que es el control de minimización que piden
P40, P44, P45, P46 y P47.

## 64. La única capa de esta KB sin ninguna opción permisiva y productiva es, exactamente, la que el regulador nombró de alto riesgo (agregado 2026-10-01, pase 25)

Se barrió la capa de *proctoring* completa —era consigna del pase 24— y el resultado es simétrico y vale como advertencia
de propuesta: **las cinco piezas que existen fallan el mismo filtro, por dos caminos distintos.**

- **Camino copyleft:** `openedx/edx-proctoring` (**AGPL-3.0**, 68 ★), `oat-sa/lib-lti1p3-core` (**GPL-2.0**, 37 ★ — y es **la única certificada en *LTI 1.3 Proctoring Services*** de toda la base), `sudosylabs/Proctor` (**AGPL-3.0**, pre-release declarado), `kamlendras/OpenProctor` (**AGPL-3.0**, 37 commits).
- **Camino de los pesos:** `vardanagarwal/Proctoring-AI` es **MIT y tiene 635 ★ / 352 forks** —la pieza más traccionada de la capa— **pero su modelo de *facial landmarks* está entrenado con datasets de uso no comercial**, por su propio README, y el proyecto se declara de investigación.

🔴 **Y acá está la tendencia, que es la coincidencia:** el *proctoring* es **la única función educativa que el Annex III
del EU AI Act nombra de forma explícita** entre las de alto riesgo (aplicable **2027-12-02**), y Corea del Sur ya la
alcanza como *high-impact AI* desde el **2026-01-22**. O sea: **la capa con más exigencia regulatoria del sector es la
que tiene cero opciones permisivas y productivas en open source.** Las dos cosas no son independientes — el riesgo
regulatorio y de reputación es justamente lo que mantiene a los proveedores serios en modelo cerrado y deja el open
source en manos de demos y de copyleft institucional.

**La consecuencia comercial, y conviene decirla al revés de como la pide el cliente:** cuando un cliente pide
*«proctoring con AI»*, la respuesta rentable **no es buscar la pieza**: es **sacar el entregable del Annex III**. Se
entrega integridad de examen con **banco de ítems variabilizado y aleatorización** (`LongsightGroup/qti3` → ver
corrección en **P49**), **entrega certificada**, **notas por AGS** y **evidencia de proceso en xAPI**. Menos riesgo
regulatorio, licencias permisivas y un expediente defendible. Ver **P49** y el **gap 39**.

## 65. Apareció la primera pieza de estándar educativo con puerta nativa de agente, y la capa de competencias de esta KB no sabía hacer aserciones (agregado 2026-10-01, pase 25)

**Dos hallazgos que van juntos, los dos en `cassproject/CASS`** (Apache-2.0, 62 ★, 29 forks, 2.123 commits, verificado de
primera mano):

**(1) La capa de competencias de esta KB estaba incompleta y no lo sabía.** El pase 14 y el pase 20 levantaron la capa
CASE —`opensalt` (MIT, 45 ★), `1EdTech/OpenCASE` (Apache-2.0, 9 ★), `compeito` (Apache-2.0, 3 ★), `conform-ed` (MIT,
2 ★)— y las cuatro piezas **hospedan y validan marcos de competencias**. Ninguna **registra si un alumno alcanzó una
competencia**. CaSS hace las dos: autoría de marcos **y aserciones de logro individual con cómputo de perfil del
aprendiz**. Con 62 ★ es, además, **la más traccionada de toda la capa**. La pregunta que paga un proyecto de competencias
no es *«¿existe este marco?»* sino *«¿qué sabe este alumno?»*, y esta KB no tenía con qué responderla.

**(2) Y trae cartucho MCP.** Entre sus *«pluggable cartridges»* —**IMS CASE**, **xAPI**, CTDL-ASN, ASN, **Open Badges
2.0**— hay uno de **MCP**. 🔵 **Es la primera vez en 25 pases que esta KB encuentra una pieza de estándar educativo que
expone puerta nativa de agente.** La diferencia es de arquitectura, no de comodidad: un tutor de `agents/top.md` **lee el
marco y escribe la aserción sin adaptador escrito a mano**, y lo que devuelve **queda como aserción en un servidor de
estándares, no como texto en un chat** — o sea, queda auditable, exportable a Open Badges y comparable entre cohortes.

**Por qué es tendencia:** siete pases buscando *«agentes educativos»* devolvieron agentes genéricos (ver
`agents/trending.md`). Este pase encontró el valor en el lado opuesto del cable: **no un agente nuevo, sino el enchufe
estandarizado por donde entran los que ya hay.** Si el patrón se repite —estándares educativos publicando servidores MCP—
la capa de integración entera de esta KB se vuelve herramientas de agente, y eso es la consigna de búsqueda del pase 26.

## 66. El estándar de competencias con puerta de agente pasó de promesa a capacidad medida, y las dos tools que expone son exactamente los dos pasos que esta KB tenía inferidos (agregado 2026-10-01, pase 26)

La tendencia **65** (pase 25) registró que `cassproject/CASS` **declaraba** MCP entre sus cartuchos. Era una línea de
README, y el pase 25 fue honesto al marcarla como **gap 40**: *«está declarado, no medido»*. **Este pase la midió, y el
resultado es mejor que la promesa.**

**6 tools y 3 resource templates**, generados sobre un spec de **51 paths** que valida con **0 errores**. Y las dos que
deciden si esta capa sirve:

- **`record_evidence`** → `POST /api/xapi/statement`. *«Record evidence that a person has demonstrated (or failed to
  demonstrate) a competency»*, en palabras del propio repo. **Entra evidencia xAPI.**
- **`get_learner_profile`** → `GET /api/profile/latest`, con `frameworkId`, `subject`, `flushCache`, `cache` y
  `targetDateTime`. Su descripción es literalmente *«use this tool to answer the question "what does this person
  know?"»*. **Sale perfil de competencia computado.**

**Por qué esto es una tendencia y no un hallazgo de repo.** Desde el pase 14 esta KB sostiene que la pregunta que paga
un proyecto de competencias no es *«¿existe este marco?»* sino *«¿qué sabe este alumno?»*, y durante doce pasadas no
tuvo con qué responderla: la capa CASE (`opensalt`, `OpenCASE`, `compeito`, `conform-ed`) **hospeda y valida marcos y no
registra logro**. Ahora existe la pieza que lo registra **y la expone por MCP, bajo Apache-2.0** — es decir, **un agente
puede escribir evidencia y leer mastery sin que nadie escriba un *adapter***. El paso 4 de **P48** deja de ser inferido.

**Y hay una lectura de segundo orden que vale para toda esta KB.** CaSS no expone su API: **expone una superficie
curada** — 6 de 51 paths, con 45 `x-mcp-ignore` puestos a mano y descripciones escritas para que las lea un modelo
(*«Hints:»* incluidos). **La tendencia real es ésa: los estándares educativos están empezando a publicar superficie de
agente diseñada, no pasarelas automáticas sobre REST.** Es la diferencia entre un proyecto que agregó MCP y uno que
pensó qué debe poder hacer un agente. Para elegir sobre qué estándar construir, **la calidad de la superficie MCP ya es
un criterio de selección** — y conviene mirarla antes que las estrellas. Ver el **gap 40 (cerrado)**, el **gap 41** y
el patrón **P50**.

## 67. Esta KB puede proponer la herramienta y no el aula: el lado LMS de LTI no tiene implementación permisiva y productiva, y ahora está medido sobre seis candidatos (agregado 2026-10-01, pase 26)

El pase 24 encontró las dos primeras piezas *platform-side* de LTI y sospechó el problema. El pase 25 dejó escrita la
acción de medirlo. **Este pase lo cerró, con un resultado negativo que vale más que un repo nuevo:**

| Pieza | Licencia | Lado | Estado real |
|------|----------|------|-------------|
| `ltijs` | **Apache-2.0** ✅ | *tool* | **Exporta `[ 'Provider' ]` y nada más** (medido). *«Learning Tool»* en su propio `package.json` |
| `oat-sa/lib-lti1p3-core` | ⚠️ **GPL-2.0** | *platform* **y** *tool* | **La única completa y certificada 1EdTech.** Copyleft |
| `macewan-cs/lti` | **MIT** ✅ | *tool* | **Refutado como lado LMS.** *«partially implements»* |
| `LtiLibrary/LtiAdvantagePlatform` | **MIT** ✅ | *platform* | **«Sample»** en su propia descripción. ⛔ Sin `dotnet` acá |
| `Citolab/lti-1p3-platform-example` | ⚠️ **GPL-3.0+** | *platform* | **«example»** en el nombre |
| `UOC/java-lti-1.3-platform` | ⚠️ **sin licencia** | *platform* | *«**will** implement»* |

**La asimetría es estructural y conviene nombrarla así.** El ecosistema open source de LTI está construido para que
**mucha gente haga herramientas que entren a pocos LMS**. Por eso el lado *tool* es abundante, permisivo y maduro, y el
lado *platform* es escaso, copyleft o ejemplar: **los LMS grandes no necesitaban publicar el suyo**, y quien lo publicó
lo hizo como material de referencia. **No es una laguna del open source: es la forma del mercado.**

**Qué significa comercialmente, dicho sin adorno.** Esta KB es fuerte proponiendo **la herramienta que entra al LMS del
cliente** (`ltijs` Apache-2.0 + `canvas-mcp` MIT, y con el pase 26 el lado docente también). **No puede proponer el aula
misma con licencia permisiva.** Si un *engagement* pide el lado plataforma, las opciones son **GPL-2.0 certificada**,
integración como *tool*, o **desarrollo presupuestado** — y la peor de las cuatro es prometerlo como integración y
descubrirlo después. Ver el **gap 42** y el patrón **P51**.

## 68. La capa que el regulador aprieta más es la más vieja y peor abastecida del inventario, y la distancia es de doce años (agregado 2026-10-01, pase 26)

El pase 25 registró en la tendencia **64** que *proctoring* era la única capa sin opción permisiva y productiva, y que
era justo la que el **Annex III** nombra de alto riesgo. **Este pase encuentra una peor, y por un margen amplio.**

***Student success* / *early warning*.** Lo que existe open source: **FlightPath Academics** (GPLv3+, PHP, liberada el
**2013-03-13**, con *early alerts* y *Academic Priority* para alumnos en riesgo) **sin repositorio en GitHub**;
**Student Success Plan** de Unicon y el *dashboard* de **Marist College**, los dos con referencias verificables de
**2013–2014**. **Doce años sin renovación en la capa que predice el fracaso del alumno.**

**Y es exactamente la capa que la regulación acotó mientras el open source se quedaba quieto.** El **Annex III** del EU
AI Act la clasifica de alto riesgo; **Oklahoma y Maryland prohíben la decisión autónoma sobre el alumno** (pase 23);
**Delaware y Nueva York** prohíben el IEP automatizado (pase 3); **Colorado y Texas** agregaron requisitos *piecemeal*
(pase 26). **Seis estados y un reglamento europeo sobre una capa cuyo software libre es de 2013.**

**La inferencia que esta tendencia habilita, y es la más valiosa del pase para una propuesta.** Cuando el software
disponible es viejo y la regulación es nueva, **el entregable defendible no es el modelo predictivo: es el flujo con
humano decidiendo.** Un *early warning* que **ordena una cola de revisión humana** y deja expediente de por qué el
alumno entró en ella es vendible en las cuatro regiones y **no cae en la prohibición de decisión autónoma**; el mismo
modelo conectado a una acción automática es ilegal en dos estados y de alto riesgo en EMEA. **Es la misma pieza técnica
con dos envoltorios, y sólo uno se puede facturar.** Ver el **gap 47** y el patrón **P53**.

**Y el contraste que ordena el inventario de verticales de esta KB, ahora que son varias:** la biblioteca —abierta en
este pase— **tiene** opción permisiva, grande y moderna (**FOLIO**, Apache-2.0, 3.096 commits, Kafka) **y no tiene
presión regulatoria**; *student success* **no tiene** opción y **tiene toda la presión**. **La regla que se puede sacar:
en esta industria, el abastecimiento open source y el riesgo regulatorio están inversamente correlacionados** — lo que
el regulador nombró de alto riesgo es, sistemáticamente, lo que el open source no construyó. Vale para *proctoring*
(tendencia 64), para la capa predictiva (ésta) y para el modelado del alumno (gap 5). **Donde hay más riesgo hay menos
pieza, y por eso hay más proyecto.**

## 69. El «no existe» más citado de los últimos dos pases era un error de muestreo, y lo que existe escribe notas (agregado 2026-10-01, pase 27)

El pase 26 cerró con una afirmación fuerte y muy accionable: *«Moodle es el LMS más instalado del planeta y su único
conector MCP es AGPL-3.0 con las partes útiles cerradas»*. Sobre eso construyó el **gap 43** y el patrón **P51**, cuyo
título es, literalmente, *«el conector MCP de Moodle que no existe»*. **Este pase la desmintió en una búsqueda.**

| Lo que el pase 26 afirmó | Lo que está verificado ahora |
|---|---|
| *«El único conector MCP de Moodle»* | **Hay al menos tres.** Dos son **MIT** |
| *«AGPL-3.0, partes útiles cerradas»* | Cierto **de `csmediapro`**, falso de la capa |
| *«Los 10 tools abiertos son sólo de lectura»* | **`peancor/moodle-mcp-server` (MIT, 43 ★, 13 forks) tiene cuatro tools de escritura**, dos de ellas de **nota y devolución** |
| *«Nada equivalente a `canvas-mcp` para Moodle»* | **`MarcosNahuel/moodle-mcp` (MIT) expone 40 tools** en 10 dominios **+ `ws_raw`** — el mismo orden de magnitud que el escalón bajo de `canvas-mcp` |

**La causa, que es lo que hay que llevarse:** las tres veces se consultó un **directorio de MCP**, y los directorios
**rankean por promoción**. `csmediapro` tiene sitio propio, paquete npm con nombre de producto y *premium plugins* —
aparece primero. Los dos MIT tienen **1 ★ y 43 ★ y cero marketing**. 🔴 **Regla operativa nueva: si una búsqueda de
directorio devuelve un único candidato y ese candidato es además el único con sitio comercial, la capa no está medida,
está mal muestreada.** Hay que repreguntar por el *host* del repositorio y por patrón de nombre.

Es el tercer pase consecutivo en que el error estuvo en el **muestreo** y no en la fuente: pase 25 (dos falsos
negativos propios), pase 26 (el término `CASE` capturado por otro mercado), pase 27 (el directorio que rankea por
promoción). **La KB está aprendiendo más de cómo busca que de lo que encuentra.**

## 70. El gap 6 —corrección y devolución, abierto desde el pase 2— tiene por primera vez una pieza permisiva que escribe, y aterriza justo donde el regulador exige que firme una persona (agregado 2026-10-01, pase 27)

Veinticinco pasadas sostuvieron el **gap 6** con la misma forma: *la demanda de corrección está probada —Singapur la
construyó cerrada, tres de sus seis funciones del alumno son asistentes de devolución— y la oferta open source es
nula*. **Este pase encuentra la primera excepción permisiva**, y es pequeña pero del lado correcto del verbo:

`peancor/moodle-mcp-server` (**MIT**, 43 ★, 13 forks, 10 commits, TypeScript) expone ocho tools y **cuatro escriben**:

- `get_student_submissions` → leer la entrega
- **`provide_assignment_feedback`** → **poner nota y comentario en la tarea**
- `get_quiz_attempts` → leer el intento
- **`provide_quiz_feedback`** → **comentar el intento**

**Por qué es la pieza que faltaba y no sólo un repo más.** La capa de corrección open source que esta KB venía
inventariando era toda **lectura y análisis**: evaluaba, puntuaba, estimaba *mastery* — y después **el resultado no
volvía al expediente del alumno**. El *«último tramo»* —escribir la nota en el LMS de producción— se cotizaba como
desarrollo. **Ahora hay un artefacto MIT que lo hace sin tocar el LMS**, por Web Services.

🔴 **Y encaja exactamente con la restricción regulatoria de North America, que es lo que lo hace vendible.** Oklahoma y
Maryland **prohíben que la AI tome decisiones de alto impacto sobre un alumno**; la tendencia 26 y el bloque regional
vienen diciendo que el entregable rentable es *«el sistema instruye el expediente y la persona firma»*. Una tool
llamada `provide_assignment_feedback` **es precisamente el punto donde se mete la compuerta de aprobación humana**: el
agente prepara, el docente confirma, la escritura queda registrada. **No cierra el gap 6** —ocho tools no son un
sistema de corrección, y 10 commits no son una base de producción— pero **deja de ser verdad que no hay nada permisivo
del lado de la escritura**. Ver **P54**.

## 71. El hueco del eje conector no estaba en Moodle: está en Open edX, y es el único LMS grande sin puerta de agente (agregado 2026-10-01, pase 27)

Con Moodle corregido, el mapa del eje conector por LMS queda así —y la asimetría es el hallazgo:

| LMS | Licencia del LMS | Conector MCP | Licencia | Estado |
|---|---|---|---|---|
| **Canvas** | AGPL-3.0 | `vishalsachdev/canvas-mcp` | **MIT** ✅ | El más maduro de la capa. ⚠️ El conteo de tools **varía por versión** (40+, 80+, 116): **no es cifra citable** |
| **Moodle** | GPL-3.0+ | `peancor/moodle-mcp-server` · `MarcosNahuel/moodle-mcp` | **MIT** ✅ ×2 | Existe, con escritura. Pre-producción |
| **Moodle** | — | `csmediapro/moodle-mcp-server` | AGPL-3.0 | Núcleo abierto, capas útiles de pago |
| 🔴 **Open edX** | **AGPL-3.0** | **ninguno** | — | **Búsqueda extendida: nada.** Ver **gap 48** |
| **SCORM** (formato, no LMS) | — | `giacomomaria81/scorm-mcp-server` | **MIT** ✅ | 3 tools, offline. Ver **P56** |

**Por qué la ausencia de Open edX importa más que la de Moodle que resultó falsa.** Open edX es la plataforma de los
despliegues públicos grandes: es el stack sobre el que se montan los programas nacionales, y esta KB ya tiene
registrado que **si el cliente corre Open edX con analítica, corre Aspects y por lo tanto Ralph sobre ClickHouse sin
haberlo elegido**. Es decir: **el LMS con la huella institucional más grande en LATAM e India es el único sin puerta de
agente**, y además el que llega con una configuración de telemetría impuesta por default. **Hueco de oferta y
necesidad concreta en la misma celda** — que es el perfil de oportunidad más limpio que puede registrar esta KB.

El dato adicional que lo hace barato: **la arquitectura ya está resuelta dos veces** (Canvas y Moodle), y
`MarcosNahuel/moodle-mcp` publica la decisión de diseño que importa portar — **fachadas de alto nivel sobre Web
Services, más un `ws_raw` como escape hatch**, en vez de volcar cientos de endpoints como tools. Ver **P55**.

## 72. Lo que un estándar educativo decide *no* exponer a los agentes es información de producto, y en Open Badges la puerta está cerrada a propósito (agregado 2026-10-01, pase 27)

El pase 26 abrió esta idea (*«CaSS no expone su API: expone una superficie curada»*). Este pase la midió entera, por
conteo de anotaciones sobre el árbol de `cassproject/CASS` v1.7.7: **6 operaciones expuestas y 55 excluidas, 61 en
total**. Y el desglose por estándar dice algo que ninguna cifra agregada mostraba:

| Estándar / capa en CaSS | Expuesto a MCP | Oculto | Lectura |
|---|---|---|---|
| **xAPI** | 1 (`record_evidence`) | 4 | La puerta de evidencia está abierta, **de a un statement** |
| **Perfil de competencia** | 1 (`get_learner_profile`) | 0 | Íntegro |
| **CRUD JSON-LD** | 3 | 3 | Mitad |
| 🔴 **CASE** (`caseAdapter` + `caseIngest`) | **0** | **13** | **Autoría de marcos: cerrada** |
| 🔴 **CEASN** | **0** | 6 | Cerrada |
| 🔴 **Open Badges** | **0** | **5** | **Cerrada, y anclada a OB 2.0** |

**Las dos consecuencias de cotización:**

1. **Un entregable que prometa emisión de insignias o autoría de marcos de competencia «por MCP» sobre CaSS está
   prometiendo algo que el proyecto excluyó deliberadamente.** Eso va por REST, **fuera** de la superficie de agente.
   La pregunta *«¿hay conector MCP de Open Badges?»* tiene ahora una respuesta mejor que *«no se encontró»*: **la pieza
   existe en el proyecto de referencia y la puerta está cerrada por diseño.**
2. **El adaptador de Open Badges de CaSS es `w3id.org/openbadges/v2` — OB 2.0, no 3.0.** Para un cliente que pide
   credenciales verificables al día (W3C VC / OB 3.0), **CaSS no es la pieza que lo emite**. Es la clase de detalle que
   sólo aparece leyendo el `@context` en el código, y que cambia una propuesta.

**La regla de método que generaliza:** cuando un proyecto anota exclusiones una por una, **la lista de exclusiones es
una declaración de alcance más confiable que su README** — y conviene leerla antes de las estrellas. Es la misma
lectura del pase 26, ahora con el desglose que permite usarla por capa.

## 73. La puerta de agente dejó de ser un producto propio y pasó a ser una característica del SDK que ya hablaba el estándar — y eso invalida buscar conectores por nombre (agregado 2026-10-01, pase 28)

**Es la tendencia más accionable de este pase porque cambia el método, no el inventario.**

El pase 26 declaró **OneRoster sin conector MCP** consultando un directorio. El pase 27 diagnosticó el sesgo
(**gap 49**) y dejó la regla: preguntarle al *host* del repositorio por **patrón de nombre** — `*-mcp`, `mcp-*`,
`mcp-server` + el estándar. Este pase ejecutó eso y encontró el repo. 🔴 **Pero no lo encontró por el patrón:**
[`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) **no tiene `mcp` en el nombre**, no está
en ningún directorio de MCP, y declara su servidor **en una línea del README**:

> *«This SDK is also an installable MCP server where the various SDK methods are exposed as tools that can be invoked
> by AI applications.»*

**Y lo que hay detrás de esa línea es la superficie de herramientas más grande de esta KB: 164 métodos** sobre 21
recursos OneRoster, **con escritura** (`createUser`, `updateClass`, `deleteEnrollment`, `postAcademicSession`), sobre
**v1p2**, con paginación y el `filter` de 1EdTech. Para comparar: `canvas-mcp` declara entre 40 y 116 según versión, y
`MarcosNahuel/moodle-mcp` declara 40. **Licencia: 0BSD** — la más permisiva que vio esta base, sin obligación de
atribución.

**La forma económica de esto, que es el punto:** escribir un conector MCP desde cero es trabajo; **agregarle un
*transport* MCP a un SDK que ya cubre el estándar entero es casi gratis**, porque los métodos ya existen y el mapeo es
mecánico. Entonces el incentivo no está en publicar `foo-mcp`: está en que **cada SDK maduro de cada estándar sume la
puerta como una *feature* menor de su release**. Es exactamente lo que pasó acá, y es la razón por la que el conector
tiene **10 ★**: nadie lo anuncia como conector porque **no es un conector, es un SDK**.

**La regla de método que reemplaza la del pase 27 (no la corrige: la extiende):**

> **Para medir si un estándar tiene puerta de agente hay que buscar el estándar + `SDK` / `client` / `library`, abrir
> el README y buscar «MCP» adentro.** El nombre del repositorio **no es un índice de capacidad**, igual que el
> directorio no era un índice de licencia. **Tres métodos en tres pases, y los dos primeros dieron falsos negativos.**

🔴 **Consecuencia que hay que asumir sin suavizarla: todas las ausencias de puerta que esta KB declaró consultando
nombres o directorios están mal medidas por construcción.** La única que sobrevive en este pase es **QTI**, y
sobrevive porque **se abrió el SDK permisivo y se miró adentro** (`examplary/qti`, MIT, QTI 3.0 + 2.1: MCP no se
menciona). Ver el **gap 50**, el **gap 51** y **P59**.

## 74. El gap 48 no era un gap: eran dos con la misma cara — Open edX escribe notas por lote y declara experimental su *authoring* (agregado 2026-10-01, pase 28)

El pase 27 abrió el **gap 48** —Open edX es el único LMS grande sin conector MCP— y dejó como acción medir **si la
plataforma expone una API REST suficiente**, con el encuadre honesto de que *«si no la hay, ésa es la razón de la
ausencia y es un hallazgo igual de bueno»*. **Se midió leyendo los `urls.py` del árbol `master`, de primera mano.** La
respuesta no es una de las dos: **es un corte por la mitad de la plataforma.**

**La mitad que alcanza, y escribe:** *Course Blocks* está en **`v1` y `v2`**; *Enrollment* expone `enrollment`,
**`unenroll/`**, `roles/` y `enrollment_allowed/`; y *Grades v1* expone **`gradebook/{course_id}/bulk-update`**
(`GradebookBulkUpdateView`) y **`subsection/{subsection_id}/`** (*course_grade_overrides*).

🔵 **El dato que mejora la cotización respecto de lo que el pase 27 suponía: Open edX escribe notas por lote, y el
conector MIT de Moodle no tiene lote.** `provide_assignment_feedback` es de a una. O sea que en la capacidad que más
importa para el **gap 6**, **la plataforma sin puerta es más capaz que la que ya tiene dos puertas.**

🔴 **La mitad que no alcanza, y lo declara el proyecto:** la API de *authoring* de Studio/CMS `v1` —21 rutas, entre
ellas `xblock/`, `container/{usage_key}/children`, `course_settings/…`, `course_rerun/…`— **viene con el aviso de que
«the Authoring API is still experimental» y la recomendación de usar `v0`**.

**La lectura, y es la que separa un hallazgo de una excusa:**

> **Para matrícula, roles, bloques y notas, la ausencia del conector de Open edX es puro gap 49** —nadie lo publicó, no
> que no se pueda—. **Para *authoring*, la ausencia tiene causa técnica declarada por el propio proyecto**, y es el
> **gap 50**. Un conector que replicara lo que hace `MarcosNahuel/moodle-mcp` (crear curso, secciones, publicar
> material, armar quiz) **tendría que apoyarse en la única parte de la plataforma que su mantenedor marca como
> inestable**, mientras el de Moodle se apoya en Web Services, estable desde hace más de una década.

⚠️ **La licencia no es el obstáculo, y es la primera pregunta del cliente:** Open edX es **AGPL-3.0**, pero un conector
que habla REST desde otro proceso **no deriva de la plataforma y no hereda la AGPL**. Es la configuración ya verificada
dos veces en esta KB —`canvas-mcp` (MIT) contra Canvas, los dos `moodle-mcp` (MIT) contra Moodle GPL-3.0—: **las LMS
son copyleft y las puertas son permisivas.** **P55** queda reescrito con el corte: se cotiza operación y evaluación, no
autoría.

## 75. El Annex III dejó de ser una fecha en el calendario: rige desde el 2026-08-02, y la demanda de conformidad en EMEA está **vencida**, no anticipada (agregado 2026-10-01, pase 28)

Esta KB viene registrando el reloj regulatorio europeo en futuro desde el pase 11, y el pase 25 construyó **P49**
sobre que el **Annex III** nombra la educación y los exámenes como alto riesgo. **Hoy el reloj se terminó:** el AI Act
entró en vigor el **2024-08-01**, y el **2026-08-02 es la fecha en que aplica plenamente a los sistemas de alto
riesgo**. A la fecha de este pase **lleva dos meses vigente**.

Lo que un proveedor de AI educativa en la UE debe tener **ahora**: **gestión de riesgos continua**, **documentación
técnica** exhaustiva, **mecanismos de supervisión humana**, **evaluación de conformidad antes de la puesta en el
mercado** y **registro en la base de datos de la UE**.

**Por qué es tendencia y no sólo un dato de EMEA.** El desajuste que el pase 20 nombró como el más explotable de esta
KB —**la región legisla la auditoría algorítmica y no construye la herramienta que la ejecuta**— cambia de tiempo
verbal. **Deja de ser una oportunidad anticipada y pasa a ser un incumplimiento en curso.** Y los cinco requisitos son
**artefactos de ingeniería, no de legal**: la gestión de riesgos es un proceso con evidencia, la supervisión humana es
una compuerta en el flujo —que es literalmente la forma de **P54** y **P49**—, y la documentación técnica se genera
desde el pipeline. 🔴 **Con el agravante de que la capa de *proctoring*, que es la que el Annex III nombra más
directamente, sigue sin ninguna opción permisiva y productiva (gap 39).**

⚠️ **Y alcanza fuera de la UE por la puerta de atrás:** el régimen toca a instituciones de educación superior de
**EE. UU.** con colaboración académica o programática con instituciones europeas. Es el argumento que vuelve vendible
la gobernanza en North America, donde **no hay regulador sectorial** (tendencia de este pase en `intel/market.md`).

## 76. Los agregadores de estrellas no inflan: están **viejos**, y el signo del error depende de la velocidad del repo (agregado 2026-10-01, pase 28)

Corrección de método de esta KB, y vale porque la regla anterior estaba escrita al revés.

El pase 22 y el pase 4 del `technology`-KB encontraron agregadores **sobreestimando** estrellas, y la KB venía
operando con *«los agregadores inflan»*. El pase 27 vio pasar un *«Hermes Agent, MIT, 180.000+ ★»* y **se negó a
escribirlo**, dejando la instrucción de verificarlo si reaparecía. **Reapareció en el barrido global de este pase, con
tres cifras distintas en tres fuentes: 180.000, 212.000 y 230.000.** La página del repo
([`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent), **MIT**) dice **250,6k ★ y 53,6k forks**.

🔴 **Las tres estaban mal, y las tres estaban mal por debajo** — en la dirección contraria a la que la regla predecía.

> **La formulación correcta: un agregador no sesga, atrasa.** En un repo que crece rápido el error cae **del lado
> bajo**; en uno estancado, del **lado alto**. **Por lo tanto la regla útil no es sobre la dirección del error sino
> sobre la fuente: la cifra se lee de la página del repo, o no se escribe.** Es la misma conclusión que la KB ya
> aplicaba, con el fundamento arreglado.

**Nota de alcance:** Hermes Agent **no entra en el inventario educativo** de esta KB — es un agente de propósito
general, sucesor de OpenClaw. Se registra por el método y como nota de sucesión.

## 77. La AI PC entra al presupuesto educativo, y es la primera cifra de *hardware* de esta KB (agregado 2026-10-01, pase 28)

El barrido global trae un dato de canal que esta base no tenía en 27 pasadas: las **AI PC** serían el **15 % de los
envíos de PC educativas en 2026** y se acercarían al **50 % de penetración en 2030**.

**Por qué importa para una KB de software open source.** Fija el **piso de capacidad de cómputo local** del aula, y por
lo tanto decide si los patrones que esta KB recomienda corren **en el dispositivo** o exigen nube. Esta base ya tiene
inventariada la capa offline-first —`Project NOMAD` (Apache-2.0), `Kolibri` (MIT), y el empaquetado SCORM 100 %
offline de `scorm-mcp-server` (**P56**)— y los recomendaba por **conectividad**, que es el argumento de LATAM, África
y despliegue rural. **El dato de AI PC agrega el segundo argumento, que es el de las regiones ricas:** inferencia local
por **costo y por privacidad del dato del menor**, no por falta de red. ⚠️ **Dicho con la cautela que corresponde:
viene de una consultora de canal, es una proyección, y no se verificó contra una segunda fuente** — se registra como
señal de dirección, no como base de cotización.

## 78. Cuando dos avisos del mismo repositorio se contradicen, el que gana es el que tiene rutas registradas — y esta KB acaba de pagar por no mirar los dos (agregado en el pase 29 del 2026-10-01)

**Es la tendencia más útil de este pase porque es una regla de lectura, y nació de un error propio.**

El pase 28 leyó `cms/djangoapps/contentstore/rest_api/v1/urls.py` de Open edX, encontró el comentario *«the Authoring
API is still experimental and the v0 versions should be used»*, **lo transcribió bien** y concluyó que la autoría de
Studio tenía **causa técnica** para no tener conector MCP. **La cita era verdadera y la conclusión falsa**, y para
verlo alcanzaba abrir un archivo más del mismo paquete.

| Señal | Qué dice | Respaldo | Fecha |
|---|---|---|---|
| Comentario en `v1/urls.py` | *«Do not use under v1 yet… still experimental… use the v0 versions»* | 🔴 **Ninguno: encabeza una sección sin una sola ruta** | **Nov. 2023** |
| Docstring de `v0/views/xblock.py` | *«DEPRECATED… superseded by `XblockViewSet`… use `/api/contentstore/v1/xblock/` going forward»* | ✅ **`v1/urls.py` registra ese `XblockViewSet`; `v1/views/xblock.py` implementa CRUD completo; las 5 vistas de `v0` emiten `DeprecationWarning`** | Vigente |

**La regla, generalizable a cualquier base que esta KB mida:** un comentario es una **declaración de intención**, y
puede quedar años sin actualizarse; **una ruta registrada es un hecho verificable**. 🔵 **Cuando los dos se contradicen,
se le cree al código ejecutable y se fecha el comentario.** Y el corolario operativo: **un aviso de «experimental» sin
rutas debajo no describe el estado del proyecto — describe el estado de una sección vacía.**

**Por qué es tendencia y no anécdota:** es la **quinta corrección consecutiva por muestreo** de esta KB (pases 25 a 29),
y la primera en que la fuente mal muestreada **era un repositorio que ya estaba abierto**. Las cuatro anteriores fueron
por consultar el canal equivocado (directorios de MCP, agregadores de estrellas, patrón de nombre). **Ésta fue por
leer un archivo donde hacían falta dos**, y es la más barata de prevenir de todas.

## 79. La rotación de versiones de API es el costo real de integrar una plataforma educativa grande, y es cotizable por separado (agregado en el pase 29 del 2026-10-01)

**El hallazgo colateral del pase 29 resultó más útil para una propuesta que el hallazgo que se fue a buscar.**

`cms/djangoapps/contentstore/rest_api/urls.py` de Open edX monta **cinco versiones a la vez**: `v0/`, `v1/`, `v2/`,
`v3/` y `v4/`. **No es un residuo: cada una tiene capacidades que las otras no tienen.**

🔴 **La medida concreta del costo, en una sola capacidad: las notas viven en tres versiones simultáneas** — `grading/`
(`v0`, `AuthoringGradingView`), `course_grading/` (`v1`, `CourseGradingView`) y `authoring_grading` (`v3`,
`AuthoringGradingViewSet`). Y **assets, video y transcripciones existen únicamente en `v0`**, que es la versión que el
propio proyecto está deprecando para `xblock`.

**Lo que eso significa para un proyecto, dicho sin adornos:** **no hay una "API de Studio" contra la que programar.**
Hay cinco superficies parcialmente solapadas, y **un conector serio necesita un adaptador de versión por capacidad**.
🔵 **Eso es bueno para la propuesta, no malo:** es alcance identificable, explicable y facturable **antes** de empezar,
en vez de aparecer como sorpresa en la semana cuatro. **La frase que habilita:** *«el conector incluye una capa de
resolución de versión, porque la plataforma tiene cinco vivas; acá está la lista»*.

⚠️ **Y la contracara, que esta KB debe aplicarse a sí misma:** el pase 28 midió *«Course Blocks en v1 y v2»* y lo leyó
como señal de madurez (*«versionado en dos versiones»*). **Con cinco versiones montadas, la misma observación se lee al
revés**: no es madurez de versionado, es **migración sin terminar**. **El mismo dato cambia de signo según cuántas
versiones se hayan mirado**, que es exactamente el error de muestreo del trend 78.

## 80. El estándar que publica su propio OpenAPI es el que tiene el conector de agente más barato, y eso reordena la cola de oportunidades (agregado en el pase 29 del 2026-10-01)

**Esta KB venía ordenando las oportunidades de conector por tamaño de huella instalada. Este pase sugiere un criterio
mejor: por cómo se construye el conector.**

**El caso que lo muestra es el único que ya ocurrió.** `trilogy-group/oneroster-ts` llegó a **164 métodos sobre 21
grupos de recurso con 39 commits** — una proporción imposible a mano. **No se escribió: se generó** desde la
especificación, por Speakeasy, y el servidor MCP salió de regalo como un modo del SDK.

🔵 **Y `1EdTech/OpenCASE` está en la misma posición, pero todavía nadie lo hizo:** el servidor **publica su propio
OpenAPI 3** en `GET /ims/case/v1p1/discovery/imscasev1p1_openapi3_v1p0.json`. **La especificación no hay que
reconstruirla leyendo docs: la sirve el propio sistema al que hay que conectarse.**

**La cola de oportunidades, reordenada por costo de construcción en vez de por huella:**

| Objetivo | Cómo se construye el conector | Costo relativo |
|---|---|---|
| **CASE / OpenCASE** | 🔵 **Generado** desde el OpenAPI que el servidor publica | **El más bajo de esta KB.** Ver **P60** |
| **Open edX** | ⚠️ **A mano, con adaptador de versión** (cinco versiones, trend 79) y sin OpenAPI publicado encontrado | Medio-alto, pero es la huella pública más grande de LATAM e India |
| **QTI** | 🔴 **A mano y desde cero**: no hay SDK permisivo con puerta, y el ecosistema permisivo está en PHP | El más alto. Ver **P59** |

**La regla que queda escrita:** antes de estimar un conector, **buscar si el sistema expone su propia especificación
máquina-legible** (OpenAPI, Swagger, un endpoint de *discovery*). 🔵 **Si la expone, el trabajo deja de ser "escribir
160 funciones" y pasa a ser "generar, revisar la capa de auth y elegir qué exponer"** — que es un proyecto de otra
magnitud. **Y si no la expone, eso es lo que explica el precio**, y conviene decirlo en esos términos.

⚠️ **La cautela que la propia KB ya aprendió, y vale como contrapeso de esta tendencia:** generar no es exponer.
**CaSS genera su catálogo y después oculta 55 de 61 operaciones con `x-mcp-ignore: true`.** **La decisión de qué se
expone sigue siendo de producto, y no la resuelve el generador** — es, de hecho, la parte del trabajo que hay que
cobrar.


## 81. Cuando una ausencia es una buena oportunidad, el que la cierra primero es el proyecto dueño de la plataforma — y la licencia de la puerta no se hereda de la licencia del conector típico (agregado en el pase 30 del 2026-10-02)

**Esta KB sostuvo tres pases que Open edX era el único LMS grande sin puerta de agente (gap 48) y lo trató como su mejor
oportunidad comercial, con un patrón cotizado encima (P55). El 2026-07-25 el proyecto publicó la puerta.** Dos paquetes en
PyPI, los dos **AGPL-3.0**: `openedx-mcp` (0.1.5, 5 releases) y `tutor-contrib-openedxmcp` (0.1.7, 7 releases).

**La lección no es «llegamos tarde». Es una regla de pronóstico que esta KB puede aplicar a las ausencias que todavía
tiene abiertas:**

> 🔵 **Una ausencia de conector sobre una plataforma con fundación y comunidad grandes no es una oportunidad estable: es
> una carrera contra el propio proyecto, y el proyecto tiene mejor posición** —puede correr en proceso, usar las APIs
> internas y saltearse la superficie REST versionada—. **Las ausencias que sí son oportunidad estable son las de los
> *estándares*, porque ningún organismo de estándares publica software de integración.**

**La contrastación está en esta misma KB y es limpia:** Moodle, Canvas y Open edX —las tres plataformas con fundación—
tienen hoy puerta. **CASE, QTI y la mitad *platform* de LTI —los tres estándares— siguen sin ella**, y llevan así todos los
pases en que se midieron. **La cola de oportunidades se reordena a favor de los estándares y en contra de las
plataformas**, que es lo contrario del orden que esta base usó entre los pases 27 y 29.

🔴 **Y el corolario de licencia, que es el que desarma una tesis propia** (ver tendencia **82**): el pase 27 escribió que
*«las LMS son copyleft pero las puertas son MIT, y por eso se pueden componer»*, y esa regularidad no era una coincidencia
de licencias sino **una consecuencia de que las puertas de terceros son procesos separados**. Cuando la puerta la escribe
el proyecto, **la escribe adentro**, y la licencia de la plataforma la alcanza.

## 82. La licencia de un conector la decide su arquitectura, no su autor: *in-process* hereda el copyleft, *out-of-process* no (agregado en el pase 30 del 2026-10-02)

**Es la regla que esta KB necesitaba tener explícita, y que venía usando sin enunciar.** Medido sobre las cinco puertas
que esta base tiene inventariadas:

| Puerta | Arquitectura | Licencia de la plataforma | Licencia de la puerta |
|---|---|---|---|
| `moodle-mcp-server`, `moodle-mcp` | **Proceso aparte** (Web Services por token) | GPL-3.0 | **MIT** |
| `canvas-mcp` | **Proceso aparte** (REST) | AGPL-3.0 | **MIT** |
| `oneroster-ts` | **Proceso aparte** (SDK + servidor) | — (estándar) | **0BSD** |
| `scorm-mcp-server` | **Proceso aparte** (formato) | — | **MIT** |
| 🔴 `openedx-mcp` | **EN PROCESO** (plugin Django en LMS y CMS) | AGPL-3.0 | 🔴 **AGPL-3.0** |

**La regla, para usar antes de prometerle composición permisiva a un cliente:**

> **Preguntar primero cómo se instala la puerta, no qué licencia declara.** Si se instala *dentro* del proceso de la
> plataforma —plugin, módulo, *entry point*—, **va a tener la licencia de la plataforma y no hay forma de evitarlo**. Si
> habla un protocolo desde afuera, **la licencia es libre y la composición es real.**

**Y la razón técnica por la que el proyecto eligió adentro está en su propio código, y es buena:** la autoría de curso
*«must run in the CMS (they touch the modulestore)»*. 🔵 **El beneficio es grande: corriendo adentro no se paga la rotación
de versiones `v0`–`v4` que el pase 29 midió y cotizó como riesgo de adaptador.** **Capacidad y copyleft son, en este caso,
la misma decisión.** Quien quiera una puerta permisiva de Open edX tiene que aceptar el camino REST versionado — y eso
sigue siendo construible, con el mapa del pase 29 (ver **P61**).

## 83. «Declara N operaciones» y «sirve N tools» difieren por dos causas opuestas —supresión y *aliasing*—, y hay que decir cuál antes de cotizar (agregado en el pase 30 del 2026-10-02)

Esta KB aprendió con CaSS a no confiar en el conteo declarado: **61 operaciones, 6 expuestas, 55 con `x-mcp-ignore`**. Esa
lección se aplicó —bien— como cautela sobre `oneroster-ts` («164 métodos de SDK contados, no 164 tools»). **Este pase midió
y la causa resultó ser la opuesta.**

Ejecutado el servidor (`initialize` + `tools/list`, transporte stdio), **`OneRoster 0.7.0` sirve 132 tools**: 72 de lectura
y 60 de escritura, en 19 grupos. **Y la brecha 164 → 132 está explicada por conteo, no por hipótesis:** el SDK documenta
164 métodos pero sólo **132 nombres distintos**, porque **32 operaciones están listadas bajo dos grupos a la vez**
(`getStudentsForClass` en `classes` y en `students`; los cinco métodos de *course components* en `coursecomponents` y en
`courses`; etc.). **32 alias, 32 entradas de más, una tool por operación.**

| | CaSS | `oneroster-ts` |
|---|---|---|
| Operaciones | 61 | **132 distintas** (164 con alias) |
| Tools servidas | **6** | 🔵 **132 — el 100 %** |
| Causa de la brecha | 🔴 **Supresión deliberada** (`x-mcp-ignore`) | 🔵 **Aliasing de documentación** |

> **La regla: las dos brechas se ven igual en una tabla y significan lo contrario.** Supresión = **la capacidad no está**,
> y lo que falta hay que construirlo. Aliasing = **la capacidad está entera** y el número declarado estaba inflado por
> duplicación. **Distinguirlas cuesta un `tools/list`, y es la diferencia entre cotizar un desarrollo y cotizar una
> integración.**

🔵 **Dato operativo del mismo tipo, y el que hace usable una superficie de 132:** el servidor acepta `--tool`, así que se
puede **servir un subconjunto**. Una superficie de 132 tools no se le da entera a un agente —es ventana de contexto
desperdiciada y riesgo de elección errónea—: **se sirve el recorte que el caso de uso necesita**, y eso es decisión de
diseño, no limitación.

## 84. El rail de escritura de un agente ya tiene forma canónica, y está implementada: *dry run* + token atado a una huella del payload (agregado en el pase 30 del 2026-10-02)

**Esta KB venía describiendo «compuerta humana» en prosa en P53 y P54. Este pase la encontró implementada como primitiva
de protocolo**, en `guards.py` de `openedx-mcp`, con el modelo de amenaza escrito en el código y nombrado:

> *«An MCP key is driven by an autonomous agent, not a human clicking a button. The failure mode designed against is a
> *looping* agent — a retry storm that mass-enrols or deletes.»*

**Los cuatro rails:**

1. **Autoridad re-chequeada viva en cada request.** *«A key does not cache privilege — demote the user and every key they
   hold dies on the next call. `scopes` on a key only narrow, never widen.»*
2. **Rate limit por (key, tool)**, ventana fija: *«turns a runaway loop into ~N calls»*. Medido: `bulk_enroll` **5/300 s**,
   `regenerate_certificates` **5/600 s**, `request_retirement` **5/600 s**, y `create_xblock`/`update_xblock` **200/60 s**
   — **el límite codifica el riesgo de cada operación, no un número global.**
3. 🔵 **Confirm token.** Una escritura **sin** token **no escribe**: hace **dry run** y devuelve un *preview* más un token
   **de un solo uso atado a una huella del payload exacto**. Se reenvía con el token para aplicar, y **cambiar el payload
   invalida el token**. TTL **300 s**.
4. **Auditoría *append-only* previa:** la intención se registra **antes** de la escritura y **la escritura se rechaza si el
   registro no se puede persistir**.

**Por qué el rail 3 es el hallazgo y no los otros tres.** Rate limit y auditoría son prácticas conocidas. **El confirm
token resuelve el problema que hace inseguro a un agente con permiso de escritura: que «confirmar» y «hacer» sean el mismo
acto.** Separarlos con un token **atado a la huella del payload** vuelve imposible el *bait-and-switch* —el agente no puede
hacerse aprobar un *preview* y aplicar otra cosa— **sin poner un humano en cada llamada**. Es la pieza que convierte
«agente con permiso de escritura» en algo que un comité de riesgo puede aprobar.

🔴 **Y el requisito de despliegue que está en el código y no en la documentación:** *«The confirm-token store and
rate-limit counter use the ambient Django cache. In production that must be a shared backend (Redis/memcached); under
LocMemCache (dev) both are per-process.»* **Un despliegue multi-worker con la caché por defecto degrada los rails 2 y 3 en
silencio** — el límite cuenta por proceso y el token puede no encontrarse. **Es una línea de infraestructura obligatoria y
es cotizable.**

⚠️ **El código es AGPL-3.0; el patrón se puede reimplementar.** Un diseño no es código, y esta KB lo propone como diseño en
**P61**.

## 85. Cuando el buscador devuelve un *pull request* como evidencia de una capacidad, la capacidad no está en el producto (agregado en el pase 30 del 2026-10-02)

**Regla hermana de la del pase 29 («la presencia de MCP se verifica en el README crudo, nunca en la página
renderizada»), y este pase la necesitó para no publicar un falso positivo.**

El barrido devolvió `tutors-sdk/tutors-mono-repo` (**MIT**, 4 ★, 5 forks, **813 commits**) asociado a **xAPI** y
**Open Badges 3.0**. **Verificado en el README crudo: 0 menciones de xAPI, 0 de Open Badges, 0 de MCP.** Todo eso vive en
el **PR #341**, que está **ABIERTO** (última actualización 2026-09-30): `@tutors/xapi`, `@tutors/badges` (credenciales
OB 3.0 desde un `badges.yaml`) y un `compose.yaml` con **Yet Analytics SQL LRS (Apache-2.0)** y el **DCC signing service
(MIT)**.

> **La regla: un PR abierto es intención, no capacidad.** Se anota como **vigilancia** con número de PR, y la pieza entra
> al inventario como lo que su rama principal sostiene — en este caso **un *course reader* / LMS MIT con 813 commits**, que
> ya es un alta legítima por sí misma.

**El registro de trampas de muestreo de esta KB, que a esta altura es un activo de método:** colisión de término
(`education`, `Bloom`, `MCP`+*badges*, `case`); *chrome* de plataforma (el menú «MCP Registry» de GitHub, pase 29); **el
campo de fecha equivocado** (`time.modified` de npm, este pase); y **la señal que vive en un PR y no en el producto** (este
pase).

## 86. En npm la antigüedad se lee en `time[version]`, nunca en `time.modified` — y la diferencia fue de diez meses (agregado en el pase 30 del 2026-10-02)

**Corrección de este pase sobre el 29, y es un error de método con nombre propio.** El pase 29 escribió que el último
publicado de `@superbuilders/oneroster` era del **2026-05-04**, *«casi cinco meses»* antes. Ese valor es **`time.modified`**
del registro, que cambia por un *dist-tag*, un cambio de dueño o una deprecación — **sin que se publique una línea de
código**. La última **versión** publicada es **`0.7.0` del 2025-06-27**: **quince meses**.

**Y el patrón de publicación, que es el dato que vuelve obligatorio fijar un fork:** **9 de las 10 versiones salieron en
una ráfaga de tres días** (2025-04-29 → 2025-05-01), después `0.7.0`, y **nada en quince meses**. **Ráfaga y silencio es el
perfil de un generador corrido una vez, no de un proyecto mantenido.**

🔵 **En la dirección contraria, el mismo pase mejora el veredicto de licencia:** el pase 29 concluyó que *«el artefacto que
se instala no respalda la recomendación de 0BSD»*. Medido dentro del tarball: **`package.json` no trae el campo `license`
en absoluto** (de ahí el `None` del registro) **pero el paquete publicado SÍ incluye un `LICENSE` completo con el texto de
la BSD Zero Clause License** (*Copyright (c) 2025 Bjorn Pagen*). ✅ **Y cierra la procedencia que el pase 29 dejó abierta:**
`bjornpagen` es uno de los *maintainers* de npm que ese pase marcó como «no son la organización del repositorio», y es el
titular del copyright del LICENSE. **El defecto es de metadatos, no de licencia.**

> **Las dos reglas juntas: la licencia se verifica en el archivo `LICENSE` del artefacto publicado, y la antigüedad en
> `time[version]`. Ninguna de las dos se lee en el resumen del registro.**


## Nota de método del pase 28 (2026-10-01) — el pase que encontró el canal de lectura de código sin instalar nada, y el que descubrió que su propia regla de búsqueda del pase anterior era insuficiente

**Lo que se hizo:** el barrido obligatorio completo —**cuatro búsquedas globales y cuatro regionales**, con el año
**calculado** (2026)— más las **tres acciones** que el pase 27 dejó escritas. **Dos se ejecutaron y rindieron; la
tercera sigue bloqueada por el mismo límite de entorno, y se declara sin intentar eludirlo.**

### 🔵 El hallazgo de método del pase: `raw.githubusercontent.com` responde, y eso abre la lectura de código sin clonar ni instalar

El pase 27 cerró con un límite nuevo y duro: **no se puede instalar el árbol de dependencias de un repositorio de
terceros en este entorno**, lo que bloqueó el *handshake* MCP y la verificación del *launch* LTI. Ese límite sigue.
**Pero este pase necesitaba medir la API de Open edX y encontró que se podía hacer sin ejecutar nada**, y conviene
registrar el canal porque sirve para los pases siguientes:

| Canal | Estado en este entorno |
|---|---|
| `docs.openedx.org` (documentación oficial de la API) | 🔴 **`EGRESS_BLOCKED`** — dominio **5** de la lista |
| `openedx.atlassian.net` (wiki de arquitectura) | 🔴 **`EGRESS_BLOCKED`** — dominio **6** |
| **`raw.githubusercontent.com`** | ✅ **Responde.** Devuelve el archivo fuente crudo |
| `github.com` vía WebFetch | ✅ Responde (confirmado desde el pase 23) |
| `curl -sI` contra `github.com` | 🔴 **403 para todo**, no discrimina — ver pase 27 |

**La consecuencia práctica, y es la parte que vale heredar:** cuando la documentación está bloqueada o es ambigua,
**la declaración está en el código y el código es legible sin clonar**. Las cuatro mediciones de Open equis de este
pase son lecturas de `urls.py` del árbol `master`. **No permite ejecutar —no reemplaza el *handshake*— pero para medir
superficie de API declarada es el canal correcto y además el más preciso**, porque no depende de que la documentación
esté al día.

⚠️ **Y trae su propia trampa, que este pase casi pisó.** El `urls.py` de *Enrollment* **no lleva la versión adentro**:
la monta el *URL conf* padre (`/api/enrollments/v1/`). Leer el archivo aislado invita a concluir *«la API de matrícula
no está versionada»*, **que es falso**. **Leer código esquiva el error de la documentación vieja y agrega el error del
fragmento sin contexto.** Se deja anotado porque el canal se va a usar más.

### 🔴 El falso negativo propio, que es el resultado más importante del pase

**La regla que el pase 27 dejó escrita no alcanzaba, y lo descubrió al usarla.** La regla era: no preguntarle a un
directorio de MCP, preguntarle al *host* del repositorio por **patrón de nombre** (`*-mcp`, `mcp-*`, `mcp-server` +
estándar). Se ejecutó sobre las tres capas pendientes y **encontró `trilogy-group/oneroster-ts`, que no cumple el
patrón**: no tiene `mcp` en el nombre, es un **SDK**, y declara el servidor MCP **en una línea del README**.

**Tres pases, tres métodos, dos falsos negativos:**

| Método | Pase | Resultado sobre OneRoster |
|---|---|---|
| Consulta a directorio MCP | 26 | 🔴 Falso negativo |
| Patrón de nombre del repositorio | 27 | 🔴 Habría dado falso negativo también |
| **Estándar + `SDK`/`client`/`library`, y abrir el README** | **28** | ✅ **Encuentra el repo** |

**La lección, dicha sin suavizarla:** esta KB lleva **cuatro pases consecutivos** en que el error estuvo en el
muestreo y no en la fuente (24→25 falsos negativos, 26→27 el cuantificador de Moodle, 27→28 el patrón de nombre). **No
es mala suerte: es que medir ausencias es más difícil que medir presencias, y cada método de muestreo tiene su propio
punto ciego.** La forma de la regla que sobrevive a los tres es: **una ausencia sólo se declara cuando se buscó por
capacidad —abriendo el artefacto— y no por etiqueta.** Es lo que hace que la ausencia de **QTI** se pueda firmar y la
de **CASE** no (**gap 51**).

### Lo que se verificó y cómo

**5 repos de primera mano, todos por WebFetch sobre la página o por `raw` sobre el archivo.** `oneroster-ts` (0BSD,
10 ★, 3 forks, 39 commits), `ed-tech-system-mcp` (MIT, 0 ★, 132 commits, 18 tools), `examplary/qti` (MIT, 1 ★, 32
commits — **control negativo: MCP no aparece**), `openedx/openedx-platform` (AGPL-3.0, 8.2k ★, 4.4k forks, 68.764
commits) y `NousResearch/hermes-agent` (MIT, **250,6k ★**, 53,6k forks).

✅ **El control negativo es deliberado.** `examplary/qti` se abrió **esperando encontrar MCP adentro** —por analogía
con `oneroster-ts`— y **no lo tiene**. Ése es el dato que convierte la ausencia de QTI en medida en vez de muestreada.
**Un no-hallazgo buscado donde debería estar vale más que diez búsquedas donde no.**

⚠️ **La corrección de catálogo que NO se hizo, y por qué importa.** `verticals/solutions.md` citaba
`openedx/openedx-platform` y `repos/foundations.md` citaba `openedx/edx-platform`; parecía un error de una de las dos.
**Se verificaron las dos URLs antes de "arreglar" ninguna: las dos resuelven, el repo se renombró y la vieja
redirige.** **Corregir por parecido habría metido un error donde no había.** Se unificó al canónico y se dejó la nota.

### Lo que este pase NO hizo, declarado como tal

- 🔴 **No hizo ninguna llamada HTTP contra una instancia de Open edX.** Todo lo de la tendencia **74** es **superficie
  declarada en el código**, no comportamiento observado. **OAuth2, *scopes*, *rate limits* y forma de las respuestas
  siguen sin verificar.** No se puede levantar una instancia sin instalar dependencias de terceros.
- 🔴 **No cerró el tramo de invocación del gap 40** (*handshake* `initialize` + `tools/list` contra `POST /api/mcp` de
  CaSS): **mismo límite de entorno del pase 27, sin cambios.** No se intentó eludir.
- 🔴 **No midió los endpoints `v0` de *authoring* de Open edX**, que son los que el propio repo recomienda sobre el
  `v1` experimental. Es lo que decide si el **gap 50** es un bloqueo o un desvío.
- 🔴 **No midió CASE** (**gap 51**): colisión de término, y sin SDK permisivo que abrir.
- **No verificó los 164 métodos de `oneroster-ts` uno por uno**: el número es el que declara el README, y **no se
  ejecutó el servidor**. Se cita como *«declara 164 métodos»*, no como conteo propio. Es la misma cautela que la KB
  aplica a `canvas-mcp`.
- **No verificó fecha de último commit** de ninguno de los repos nuevos: la página no la expone de forma legible por
  este canal. Señales de vida usadas: commits totales, forks y ★.
- **No cerró los gaps 36 y 38** (cadena de `lrsql`): siguen necesitando ejecución de dependencias de terceros.
- **La cifra de AI PC (tendencia 77) no se verificó contra una segunda fuente**: es proyección de una consultora de
  canal y está marcada como señal de dirección, no base de cotización.

### Los dominios bloqueados, que ya son **seis**, y una precisión nueva sobre el bloqueo de LATAM

`unu.edu`, `publications.iadb.org`, `coe.int`, `www.iesalc.unesco.org`, **`docs.openedx.org`** y
**`openedx.atlassian.net`** (los dos últimos, nuevos en este pase).

⚠️ **La precisión nueva:** este pase intentó `unu.edu` **por WebFetch**, no sólo por `curl`, y devolvió el mismo
**`EGRESS_BLOCKED`**. 🔴 **El bloqueo es independiente del canal: es del proxy de egreso, no de la herramienta de
verificación.** Van **tres pases con la base de evidencia primaria de LATAM inalcanzable** —incluido el *working
paper* de UNU *«AI Implementation in Higher Education in Latin America and the Caribbean»*, que es exactamente la
fuente que falta—. **Es un límite del entorno, no una laguna de investigación**, y las cifras regionales de LATAM de
este pase son **de barrido secundario**: hay que levantar esas cuatro fuentes desde una red sin este proxy antes de
usarlas con un cliente.

### El barrido obligatorio, y por qué su rendimiento ya es estructural y no una queja

Las cuatro búsquedas globales devolvieron **por cuarto pase consecutivo** la capa genérica de agentes
(`openclaw`/Hermes, `browser-use`, Mem0, AutoGen, Dify, Flowise) y **material didáctico *sobre* AI**
(`ai-engineering-from-scratch`, Karpathy, *AI Agents for Beginners*). **Es la tendencia 29 y el diagnóstico del pase
23 funcionando como se predijo:** en GitHub el término `education` está capturado por el material que enseña AI, no por
el software que educa, y el primero tiene dos órdenes de magnitud más de estrellas. **Cero agentes educativos nuevos
por esa vía, por cuarta vez.** Las dos altas de este pase salieron **las dos del eje conector/estándar**, que es el
único que viene rindiendo desde el pase 25. **No se agregó ninguna fila de relleno:** 43 filas reales.

## 136. Apareció una pieza permisiva por región grande cuyo DISEÑO encodea el estatuto de esa región, y las tres se pueden mostrar como código (agregado en el pase 39 del 2026-10-02)

El pase 38 encontró la primera: `toshieji/moodle-grading-mcp` **no publica la nota**, la deja en
`workflowstate=readyforreview`, y eso es exactamente lo que el régimen de alto riesgo del AI Act y las reglas de
supervisión humana de Oklahoma y Maryland piden del software. **Lo anotó como un caso.** Este pase, midiendo otras dos
piezas, encuentra que **no es un caso: es un patrón, y ya hay un miembro por cada región donde esta KB vende.**

| Región | Pieza (permisiva) | Estatuto | Mecanismo, leído en el código |
|---|---|---|---|
| **North America** | `bruchris/canvas-lms-mcp` (MIT) | **FERPA** | `CANVAS_PSEUDONYMIZE_STUDENTS=true` seudonimiza; la reversión exige **una segunda bandera**; `resolve_pseudonym` **sólo se registra en stdio**, como tool 166 |
| **EMEA** | `toshieji/moodle-grading-mcp` (MIT) | **AI Act, Anexo III §3** | `save_grade_draft` → `readyforreview`: **la persona publica**. Allowlist de cursos, audit trail JSONL, sin notificación al alumno |
| **LATAM** | `dasgltd/mcp-brasil` (MIT) | **LGPD** | `COLUNAS_DISTINCT_PERMITIDAS`: *frozenset* de **8 columnas agregadas**. `SOURCES.md` clasifica educación como **RISCO ALTO**, documenta el retiro de microdatos de 2022 y remite a **SEDAP**; re-identificación vedada |

🟢 **Por qué esto cambia una conversación comercial y no sólo el catálogo.** La objeción de cumplimiento en educación
no se contesta bien con una cláusula ni con una promesa de *roadmap*: se contesta mostrando **el mecanismo**. Las tres
piezas son permisivas, así que el mecanismo se puede **leer, auditar y copiar** delante del cliente. 🔵 **Y la
asimetría que hay que saber: en las tres, el mecanismo de cumplimiento le cuesta superficie a la herramienta.**
`moodle-grading-mcp` tiene 9 tools y `moodler-mcp` tiene 38, pero la de 38 **publica la nota**. **Más tools no es más
proponible en un dominio regulado**, y esta es la primera vez que esta base lo puede demostrar con dos piezas del mismo
rol, el mismo LMS y la misma licencia.

## 137. `preview_*` es el primer freno de escritura de esta base que se impone PARTIENDO el conjunto de tools, no confiando en el servidor (agregado en el pase 39 del 2026-10-02)

Esta KB venía catalogando mecanismos para que un agente no escriba de más, y llevaba cinco: `confirm=true`,
*elicitation* / resolución de aprobación del SDK, `readOnlyHint`/`destructiveHint`, cuota por sujeto y ventana, y
anclaje de confianza en un artefacto externo. **Los cinco tienen el mismo punto ciego: se cumplen DENTRO de la tool.**
Confiar en ellos es confiar en que el servidor hace lo que dice su anotación.

`PabloPC05/mcp-usc` (MIT, 91 tools) introduce el sexto y es de otra clase: **cada escritura tiene un gemelo
`preview_*` que es una tool separada** — 22 de ellas (`preview_submit_assignment` / `submit_assignment`,
`preview_start_quiz` / `start_quiz`, `preview_save_quiz_answers`, `preview_remove_submission`,
`preview_replace_submission_files`, `preview_reply_forum_post`, `preview_message`,
`preview_mark_course_self_completed`, `preview_update_activity_completion_status_manually`, …).

🟢 **La consecuencia es de arquitectura, no de prolijidad:** a un cliente al que se le entrega **sólo** la mitad
`preview_*` más las de lectura, **la escritura no le está prohibida: le es inalcanzable, porque la tool no está en su
lista**. Es el único de los seis mecanismos que **no requiere confiar en el servidor** y el único que un integrador
puede imponer **desde afuera**, con un *gateway* que filtre nombres. 🔵 **Y es barato de replicar:** quien escriba un
conector nuevo puede ofrecer el par en vez de un *flag*, y se vuelve proponible en instituciones que no aceptan
escritura de agente en absoluto. Ver **P82**.

## 138. Dos repos con el mismo commit inicial y cero commits divergentes no son dos proyectos: son uno y un espejo — y el buscador lista primero al atrasado (agregado en el pase 39 del 2026-10-02)

El pase 38 aprendió, con `ashleycribb/learnmcp-xapi`, que **un fork con `main` más nuevo no es un mantenedor** hasta
contar qué agrega. **Este pase aprende el caso inverso, y lo vive dos veces en el mismo barrido:**

| Par | `merge-base` | Adelante / atrás | Qué hay que citar |
|---|---|---|---|
| `Ed-Fi-Alliance-OSS/edfi-oneroster` vs `CSR2017/edfi-oneroster` | **el tip exacto de `CSR2017`** (`937248b`); primer commit idéntico `02cbad5` | **3 / 0** a favor de la Alliance | **La Alliance** (86 tags contra 8; el tip de `CSR2017` es un commit de *bot*) |
| `dasgltd/mcp-brasil` vs `marcellodesales/mcp-brasil` | historia común | **`marcellodesales`: 0 adelante, 8 atrás** | **`dasgltd`** (`HEAD` 2026-08-18 contra 2026-04-26) |

🔴 **Y el dato incómodo del método: en los dos casos el buscador listó PRIMERO al atrasado.** El orden de resultados
no es evidencia de vitalidad, de ninguna de las dos direcciones. **La regla completa, que ahora tiene las dos mitades:**
ante dos repos con el mismo nombre, medir `merge-base` y `rev-list --left-right --count`; **si uno tiene 0 commits
divergentes, no es una alternativa, es un espejo, y se cita al que está adelante.** Es una medición de dos comandos y
en este pase **cerró el gap 79** y **evitó citar una línea de `mcp-brasil` cuatro meses vieja**.

## 139. Un proyecto puede envolver `server.registerTool` en su propio *helper*, y entonces un `grep` de la API del SDK SUBCUENTA las tools (agregado en el pase 39 del 2026-10-02)

🔴 **Este pase se equivocó y se corrigió antes de publicar, y la corrección vale más que el dato.** La primera
medición de `suren-kk/armenian-national-library-mcp` dio **«8 tools»** con nombres que no eran tools (`packed`,
`package`, `missing_item_error`): eran cadenas sueltas que el `grep` de `name: "…"` levantó. Un `grep` de
`registerTool(` daba **1**.

**La cifra correcta es 23**, y para llegar a ella hay que ver que el proyecto define **su propio *helper***,
`registerEnvelopeTool(server, "nombre", …)`, en `src/tools/tool-registration.ts`, y registra desde tres módulos:
descubrimiento (10), contenido (10), API cruda (2), más `get_repository_info`. **El *helper* además fija
`annotations: READ_ONLY` para todas**, lo que convierte *«es de sólo lectura»* de una afirmación de README en una
propiedad del código.

🔵 **La regla, y es hermana de la tendencia 117** (*«la superficie real de un CLI está en el dispatch, no en el texto de
ayuda»*): **la superficie real de un servidor MCP está en el punto de registro del PROYECTO, no en la llamada del
SDK.** El procedimiento barato que funciona en los dos casos: buscar el archivo que importa el SDK, ver **qué función
propia exporta**, y contar las llamadas a esa función. 🔴 **Un conteo publicado sin ese paso puede estar corto por un
orden de magnitud** — acá fue 1 contra 23.

## 140. El campo `repository` de un registro no prueba que el repo exista ni que sea legible, y en esta capa falla en 3 de 8 (agregado en el pase 39 del 2026-10-02)

El canal nuevo de este pase (registros de paquetes) trae su propio modo de falla, y es grave porque **parece
verificación**: el paquete declara una URL de GitHub, la URL se ve bien, y no hay repo detrás.

| Paquete | `repository` declarado | `git ls-remote` |
|---|---|---|
| `ed-fi-sdk-mcp` (Apache-2.0, *maintainer* `edfi`) | `github.com/Ed-Fi-Alliance-OSS/Ed-Fi-SDK-MCP.git` | 🔴 **no legible** |
| `frappe-mcp-server` (ISC) | `github.com/appliedrelevance/frappe_mcp_server.git` | 🔴 **no legible** |
| `@ink-waffle/sisu-mcp` (MIT) | **no declara repo** | — |

🔵 **Lo que esto cambia en la práctica, y no es que las piezas se descarten:** las tres son **instalables** y dos
traen licencia permisiva verificable (una con `LICENSE` **dentro del tarball**, que es evidencia de primera clase). **Lo
que se pierde no es el uso: es la auditoría del fuente, el *issue tracker* y la vía de PR.** Para una propuesta eso se
traduce en una frase concreta: *«se puede usar y no se puede arreglar»*, y en el caso de `frappe-mcp-server` —que trae
`call_method` y `delete_document`— **eso basta para exigir un *gateway* delante.**

🔴 **Y el caso de gobernanza que hay que saber decir en una reunión:** el consorcio **Ed-Fi** publicó su servidor MCP
oficial en npm bajo **Apache-2.0** hace **doce meses**, con **un solo release**, y **su repositorio no es públicamente
legible**. No es un proyecto abandonado por una persona: es un artefacto oficial de un consorcio grande, y aun así
**el único canal de auditoría que queda es el tarball**. ⚠️ **Verificar siempre con `git ls-remote`, nunca con `curl`**
(que devuelve 403 para todo, exista o no — tendencia 131).

## 141. El instrumento que falla devolviendo `200` es peor que el que falla devolviendo `403`, y esta base acaba de perder uno así (agregado en el pase 40 del 2026-10-02)

El pase 39 documentó su procedimiento de barrido por registro y dejó escrito, para PyPI, que *«no hay API de búsqueda:
hay que raspar el HTML de `/search/`»*. **Ese raspado ya no funciona.**

| Medición del pase 40 | Valor |
|---|---|
| Términos consultados contra `pypi.org/search/?q=` | **28** |
| Respuestas con código `HTTP 200` | **28 / 28** |
| Respuestas cuyo `<title>` es **`Client Challenge`** | 🔴 **28 / 28** |
| Paquetes extraídos del HTML | **0** |
| Peso típico de la respuesta | **3.038 bytes** |
| Control positivo (`pypi.org/pypi/<nombre>/json`) | 🟢 **200 con datos reales**, 3 de 3 |

🔴 **El problema no es que PyPI haya puesto una protección anti-bot. El problema es el modo de falla.** Esta base
tiene registrados muchos bloqueos —`github.com` 403, `eur-lex.europa.eu` 000, `arxiv.org` inalcanzable (gaps 58, 65,
72)— y **todos se notan**: devuelven un error y el pase lo anota como límite de entorno. **Este devuelve `200` y una
página válida con cero resultados**, que es indistinguible de *«busqué y no hay nada»*.

🔵 **Y ahí está el daño concreto, porque es exactamente la frase que el pase 39 usó:** el 39 cerró **nueve ausencias**
calificándolas de *«confirmadas por segundo instrumento»*, y uno de sus dos instrumentos era éste. **Un barrido
corrido hoy con el procedimiento del 39, sin mirar el contenido, habría publicado 28 ausencias falsas presentándolas
como medición.** Es la forma de error que el encabezado de la sección de gaps de este archivo nombra desde el primer
pase: *un gap informado es información; el silencio se parece demasiado a la cobertura.* **Acá el silencio venía
firmado con un `200`.**

**La regla que deja, y es de dos líneas:** **todo raspado de HTML lleva un control de CONTENIDO, no sólo de código de
estado.** Un *assert* sobre un elemento que la página de resultados real siempre tiene —en este caso
`package-snippet__name`— convierte un falso negativo silencioso en un fallo ruidoso. **Y una ausencia sólo se declara
cuando el instrumento que la midió pasó su propio control positivo en la misma corrida.**

## 142. El índice completo de un registro es un mejor instrumento de descubrimiento que su buscador, y es el que nadie usa (agregado en el pase 40 del 2026-10-02)

Roto el buscador de PyPI (tendencia 141), el reemplazo no fue otra búsqueda: fue **bajarse la lista entera**.

| Instrumento | Endpoint | Resultado medido |
|---|---|---|
| 🔴 Búsqueda | `pypi.org/search/?q=<t>` | 200 + desafío, **0 resultados** |
| 🟢 **Descubrimiento** | **`pypi.org/simple/`** | **200**, **46.675.078 bytes**, **903.402 nombres** |
| 🟢 Confirmación | `pypi.org/pypi/<nombre>/json` | 200 con licencia, releases, fechas |

**El índice `simple` es la lista de todos los paquetes de PyPI en una sola respuesta.** No trae descripciones, así que
no sustituye una búsqueda semántica — **pero la consigna del pase 39 era buscar por *nombre de proyecto*, y para eso
es estrictamente superior al buscador**: es completo, no tiene ranking que sesgue el orden, no pagina, no se puede
bloquear por término y **se consulta localmente, así que barrer 28 términos cuesta una descarga en vez de 28
peticiones**.

🔵 **La generalización, que es lo que vale para los próximos pases:** varios registros publican su índice completo o
su volcado, y **el índice es inmune a las tres cosas que arruinan un barrido por buscador** —el ranking, la
paginación y la protección anti-bot—. **Cuando se busca por nombre, hay que pedir el índice; cuando se busca por
descripción, hay que usar el buscador y controlarlo.**

🔴 **Y el primer dato que el índice entregó es un par de ceros que valen como hallazgo:** **`unitime`** —el
planificador de horarios universitario de referencia— y **`safe-exam-browser`** devuelven **cero nombres en los
903.402**. **Las piezas canónicas de dos de las capas barridas no están en el registro en absoluto.** No es que no
existan: **se distribuyen fuera del canal**, que es la misma forma que la tendencia 23 describió para la
infraestructura educativa realmente desplegada. **Para esas dos capas el inventario hay que hacerlo por sitio del
proyecto.**

## 143. El mundo de los agentes se quedó con el vocabulario de esta vertical: «proctor» ya significa supervisar al AGENTE (agregado en el pase 40 del 2026-10-02)

Esta base lleva una cuenta de colisiones de nombre desde el pase 7, y el pase 39 la dejó en **nueve**. El pase 40 suma
**once**, y el hallazgo no es la cantidad: es que **dos términos centrales de la vertical educativa fueron
reutilizados por el propio ecosistema agéntico para significar otra cosa.**

**«Proctor», en un registro de paquetes de 2026, casi nunca es un examen:**

| Paquete | Qué significa «proctor» ahí |
|---|---|
| `proctor-mcp` | *«Human oversight for MCP agents. The human-in-the-loop the MCP spec asks for and does not provide»* |
| `proctor-skill` | interroga al desarrollador sobre cambios de rama **antes de permitir `git push`** |
| `@genramzi/proctor` | *«Audit what coding agents said against what they actually did»* |
| `proctor-ai` (MIT) | framework de *prompt engineering* |
| `agentproctor`, `sqlproctor`, `onion-proctor` | supervisión de agentes, de SQL, de red |
| `matthewproctor-postcodes` | 🔵 **un apellido** — códigos postales australianos |

🔵 **El desplazamiento semántico es lógico y conviene entenderlo porque va a empeorar: «proctor» es la palabra inglesa
para quien supervisa a alguien que podría hacer trampa, y en 2026 el que podría hacer trampa es el agente.** La
vertical educativa perdió la palabra ante su propio caso de uso invertido.

**«Caliper» tiene seis homónimos no educativos y UNA pieza educativa:**

| Paquete | Qué es | Licencia |
|---|---|---|
| `caliper-reader` | *profiling* de HPC de **Lawrence Livermore** | BSD |
| `caliper-ai` | costo de los *coding agents* | MIT |
| `caliper-py` | *tracker* de experimentos de ML | MIT |
| `caliper-sdk` | observabilidad de LLM | GPL-3.0 |
| `caliper` | medición de cambios en paquetes | MPL-2.0 |
| `@dendiem/caliper` | MCP de revisión de UI | — |
| 🟢 **`timeback-caliper`** | **cliente del estándar Caliper de analítica educativa** | ⚠️ MIT (sólo registro) |

🔴 **Uno a seis, y la educativa es la que tiene la evidencia más débil del grupo** (su repositorio declarado no es
legible: tendencia 140). **Para el estándar de analítica de 1EdTech, buscar por «caliper» en un registro es
inutilizable**; hay que desambiguar con el nombre largo, igual que el pase 35 estableció para CASE
(*«Competencies and Academic Standards Exchange»*, no la sigla).

**Y dos homónimos más, de dominio adyacente, que son los peligrosos porque son verosímiles:** ⛔ `sih-br-mcp` son
**admisiones HOSPITALARIAS** de Brasil (DATASUS SIH/SUS) y entra limpio en un barrido por `admissions`; ⛔
`timetable-api-node` son **horarios del transporte público de Lviv** y entra limpio por `timetable`. 🔵 **Regla: en
esta vertical, un término administrativo sin un token educativo al lado no es un término de búsqueda.** Medido:
filtrando `accessib|a11y|wcag` junto con términos educativos, npm devolvió **256 candidatos y prácticamente todos eran
herramientas de accesibilidad web genéricas**; exigiendo token de dominio educativo bajaron a **22**, de los cuales
**11 eran homónimos**.

## 144. Las cuatro capas de administración académica no tienen ni una puerta de agente, y de una de ellas sólo existe el cliente de prueba (agregado en el pase 40 del 2026-10-02)

**Barridas por registro las capas que el pase 39 no había barrido —*proctoring*, *timetabling*, admisiones, *student
success* y accesibilidad— en npm, PyPI (por índice), Packagist y RubyGems: no hay NI UNA puerta MCP de educación en
ninguna de las cinco.** Lo que existe son **librerías de aplicación**, que es otra cosa y se cotiza distinto.

**Y es una ausencia medida, no una ausencia por no haber buscado:** el canal npm/Packagist/RubyGems respondió con
resultados reales en los 28 términos, y el canal PyPI se rehízo con el índice completo (tendencia 142) después de
detectar que el buscador estaba roto (tendencia 141). **Los dos canales coinciden.**

🔵 **La única traza de un MCP de *timetabling* que existe en los cuatro registros es su mitad cliente, y es el dato
más elocuente del pase:** **`ucleeds-mcp-tester`** (**MIT**, npm, **un solo release del 2025-04-25**, **sin
repositorio**) se describe a sí mismo como *«Test client for UCLeeds Timetabling MCP integration»*. **Alguien
construyó el servidor, le escribió un cliente de prueba, publicó el cliente y no publicó el servidor.** Es la
evidencia más limpia que esta base tiene de que la pieza que falta **se construyó y se quedó adentro de una
institución**.

🔴 **Y el contraste con la capa de conectores de LMS ordena la oportunidad entera de esta KB.** El pase 35 declaró esa
capa *«saturada: nueve puertas entre Canvas y Moodle, ocho permisivas»*. Estas cinco capas tienen **cero**.

| Capa | Puertas de agente | Estado |
|---|---|---|
| Conectores de LMS (Canvas, Moodle) | **9** (8 permisivas) | 🔴 **saturada** |
| *Proctoring* | **0** | 🟢 vacía — y la librería base es AGPL |
| *Timetabling* | **0** (+1 cliente de prueba huérfano) | 🟢 vacía |
| Admisiones | **0** | 🟢 vacía — hay *addons* de ERP (APAC) |
| *Student success* | **0** | 🟢 vacía — y ahora hay librería MIT (tendencia 148) |
| Accesibilidad | **0** | 🟢 vacía |

🔵 **Y el dato que convierte esto de observación en oportunidad con nombre viene del barrido regional del mismo pase:
en LATAM la dimensión institucional MENOS adoptada es administración (34,1 %), muy por debajo de enseñanza y
aprendizaje (73,5 %).** **La capa con menos adopción institucional es la misma que tiene cero competencia open
source.** La brecha de oferta y la brecha de demanda son la misma brecha, y eso es inusualmente accionable: **entrar
por administración es entrar donde no hay producto instalado ni alternativa gratuita.**

## 145. La portabilidad de una puerta institucional la decide una línea: `os.getenv` contra `export const` (agregado en el pase 40 del 2026-10-02)

El pase 39 admitió dos puertas institucionales y dejó escrito que no sabía qué fracción de cada una era reusable. El
pase 40 lo midió leyendo el árbol, y **el resultado es opuesto en las dos piezas por una diferencia de una línea.**

| | `mcp-usc` (USC, España) | `DUTIC-mcp` (UNSA, Perú) |
|---|---|---|
| Tools | 91 | 12 |
| **Portables** | 🟢 **80 (88 %)** | 🔴 **1 (8 %)**, +2 con configuración |
| Host de la institución | 🟢 `os.getenv("USC_MOODLE_URL", "https://cv.usc.es")` | 🔴 `export const HOST = "aulavirtual.unsa.edu.pe"` |
| Candado | **2 archivos** (`settings.py`, `security.py`) | repartido por el árbol |

🔵 **En `mcp-usc` los nombres de host de la universidad aparecen en exactamente dos archivos de todo el proyecto**, y
en uno de los dos **ya son un *default* de variable de entorno**. El otro es un par de `frozenset` de hosts
permitidos. **Portar la mitad genérica es editar dos conjuntos.** En `DUTIC-mcp` el host es **constante de
compilación**, lo que mueve la pieza de «configurable» a «fork» antes de mirar una sola tool.

**La regla de cotización que deja, y es barata de aplicar:** antes de estimar el reuso de una puerta institucional,
**buscar el nombre de dominio de la institución en el árbol y mirar en cuántos archivos aparece y en qué forma.**
Si aparece como *default* de variable de entorno en uno o dos archivos, **la pieza es configuración**. Si aparece como
constante exportada, **es un fork**. **Es una medición de dos comandos y decide la diferencia entre cotizar reuso y
cotizar desarrollo.**

🟢 **Y la medición encontró de paso el activo que nadie había contado, que es el más caro de construir de toda la
capa:** `mcp-usc` lleva en `student_capabilities.py` **un catálogo de 306 funciones de Moodle Web Services**
clasificadas por acceso (`read`/`action`), con redacción de claves secretas y cotas de tamaño de argumento
(`MAX_ARGUMENT_NODES`, `MAX_ARGUMENT_DEPTH`, `MAX_RESULT_BYTES`), sobre **327 nombres de función WS** referenciados en
el árbol. **Saber qué función de Moodle existe, qué hace y si escribe es el trabajo lento de cualquier puerta de
Moodle — y está MIT.** 🔵 **La pieza no se propone como «la puerta de la USC»: se propone como la puerta de Moodle con
el catálogo y los límites ya escritos, a la que se le cambia el destino.**

## 146. La licencia que se contradice entre el manifiesto y el árbol es una clase de evidencia distinta de la que falta, y es peor (agregado en el pase 40 del 2026-10-02)

El pase 39 abrió el **gap 81** para las piezas cuya licencia **vive sólo en el manifiesto del registro** y no en el
árbol (`@ink-waffle/sisu-mcp`, `frappe-mcp-server`). El pase 40 encuentra el caso siguiente, y **no es el mismo
problema**.

| Pieza | Campo del registro | Archivo del árbol | Clase |
|---|---|---|---|
| `@timadey/proctor` | MIT | 🔴 **no existe** | **gap 81** — falta una de las dos fuentes |
| `datakind/student-success-tool` | 🔴 **no declara ninguna** | **MIT** (`LICENSE.md`) | **gap 81 invertido** — falta la otra fuente |
| 🔴 **`exam-guard`** | **ISC** | 🔴 **Apache-2.0** | **CONTRADICCIÓN** — las dos existen y **discrepan** |

🔴 **La contradicción es peor que la ausencia por una razón operativa:** cuando falta una fuente, el pase anota la
reserva y la cierra con un correo al autor. **Cuando las dos existen y dicen cosas distintas, cualquiera de las dos
licencias es citable de buena fe por un tercero** — y mientras eso siga así, **la pieza tiene dos licencias según
dónde mire quien la audite**.

**Y la diferencia no es cosmética en este caso concreto: ISC y Apache-2.0 difieren en la cláusula de patentes**, que
es justo lo que revisa el departamento legal de un cliente grande. **El criterio que esta base adopta: manda el
archivo del árbol** (es el instrumento que el pase 39 ya había sancionado como superior al manifiesto), **pero la
pieza no se usa en un entregable hasta que el autor resuelve la discrepancia.**

🔵 **La regla general que las tres filas de arriba dejan, y es la misma con tres signos: una sola fuente de licencia
nunca alcanza.** Hay que leer **el manifiesto y el archivo**, y **cuando discrepan, eso es el hallazgo**.

## 147. `HEAD` mide al proyecto; el release mide lo que el cliente instala — y para una dependencia son 13 meses de diferencia (agregado en el pase 40 del 2026-10-02)

El pase 37 fechó las 49 filas de esta base **por el commit de su rama principal**, y con eso encontró 10 piezas
paradas hace más de seis meses. **El pase 40 encuentra el caso que muestra que ese instrumento, solo, no alcanza.**

| `openedx/edx-proctoring` | Valor | Antigüedad al 2026-10-02 |
|---|---|---|
| `HEAD` de la rama principal | **2026-05-30** | 🟢 **4 meses — mantenido** |
| Último release en PyPI (5.2.0) | **2025-04-28** | 🔴 **17 meses — parado** |
| Releases publicados en total | **253** | — |

**Las dos mediciones son correctas y dicen cosas distintas.** Medido por repositorio, el proyecto está vivo y hay
trabajo reciente. Medido por registro, **quien lo instale con `pip` —que es como llega en un despliegue de Open edX
vía Tutor— recibe código de hace año y medio.**

🔵 **La regla que esto deja, y corrige un supuesto implícito del pase 37:** para una pieza que se **instala**, la
fecha que gobierna el riesgo **no es la del commit: es la del artefacto publicado**. **`HEAD` mide la salud del
proyecto; el release mide la exposición del cliente.** Hay que medir las dos y **decir explícitamente cuál se está
citando** — y en una conversación con cliente, la que vale es la del artefacto que va a instalar.

⚠️ **Y el caso inverso también aparece en este pase, lo que confirma que la divergencia va en los dos sentidos:**
`maxxeddev/open-badges-mcp` (pase 39) está **adelante del registro** (`package.json` 0.4.0 contra npm 0.3.2), mientras
`mereos` y `@timadey/proctor` tienen **repo y registro en la misma fecha**, que es lo sano y lo menos frecuente.

## 148. A la capa más regulada del sector no le faltaba el modelo: le faltaba el expediente — y lo tiene MIT desde 2022 (agregado en el pase 40 del 2026-10-02)

El **gap 26** de esta base dice desde el pase 11 que *«la capa que decide sobre el alumno es la más regulada del
sector y la peor abastecida de open source»*, y lo midió buscando **predictores**: encontró 110 repos de *knowledge
tracing* y ningún producto. **El pase 40 la barrió por nombre de proyecto en el registro y encontró un solo nombre en
903.402 — pero ese nombre reformula el gap.**

**`datakind/student-success-tool`** — **MIT** (`LICENSE.md`, *«Copyright (c) 2022 DataKind»*), 181 archivos Python,
financiado por **Google.org**, `HEAD` 2025-09-08.

🔵 **Y el hallazgo no es que exista una librería de predicción. Es QUÉ trae además del modelo:**

| Componente | Ruta | Para qué sirve |
|---|---|---|
| ***Model cards*** | `reporting/model_card/` (5 módulos) | La documentación del modelo **generada desde el modelo entrenado**, no escrita a mano |
| **Secciones de sesgo** | `reporting/sections/bias_sections.py` (+ `pdp/`, `custom/`) | 🟢 Análisis de sesgo como **sección de reporte de primera clase** |
| **Validación de ingesta** | `ingestion_validation/` | Controla el dato antes de que entre al modelo |
| **Datos sintéticos** | `generation/pdp/` | Demostrar el pipeline **sin dato real de alumno** |

🔴 **Esto reformula el gap 26 igual que el pase 4 reformuló el gap 1, y en la misma dirección: lo que falta no es
construir, es adoptar.** El cuello de botella de esta capa **nunca fue entrenar el clasificador** —hay 110 repos que
lo hacen—: era **documentarlo para que sobreviva una auditoría**. Un modelo que predice abandono es **Anexo III punto
3** en EMEA (evaluación de resultados de aprendizaje, plazo **2027-12-02**) y cae bajo la **supervisión humana
obligatoria** que Oklahoma y Maryland ya exigen en North America. **El artefacto caro es el expediente, y acá viene
en el repo.**

🟢 **Y el principio de producto está escrito en el README, que es lo que lo hace citable ante un comité de ética:
*«humans in the loop by design»* — las intervenciones las ejecuta un asesor humano, no el algoritmo.** Es la misma
forma que el `readyforreview` de `moodle-grading-mcp` y la seudonimización de `bruchris/canvas-lms-mcp`: **el
requisito regulatorio contestado por diseño en vez de por cláusula** (tendencia 136).

⚠️ **Las tres reservas, para no sobrevenderla:** está **acoplada a PDP** (estándar de datos de educación superior de
EE. UU.) **y a Databricks**, aunque tiene una ruta `custom/` paralela a cada `pdp/`, o sea que **la customización está
prevista por diseño**; lleva **~13 meses sin release** (franja tibia, no archivada); y **PyPI no declara su licencia
—el MIT se leyó en el árbol—**, que es el gap 81 invertido (tendencia 146). 🔵 **Para North America es casi reuso;
para EMEA, APAC y LATAM es adopción del armazón con esquema propio.**

## 149. La capa que un registro mide «vacía» puede estar vacía de AGENTE y llena de SOFTWARE, y la diferencia vale una propuesta entera (agregado en el pase 41 del 2026-10-02)

**El pase 40 barrió los 903.402 nombres del índice de PyPI y midió que `unitime` y `safe-exam-browser` devuelven cero.**
De ahí concluyó que las capas de *timetabling* y *proctoring* estaban **vacías**. Medidas por repositorio, las dos tienen
plataforma madura, viva y con API formal:

| Capa | Pieza | Licencia | `HEAD` | Tags |
|---|---|---|---|---|
| *Timetabling* | `UniTime/unitime` (Apereo) | 🟢 **Apache-2.0** | **2026-10-01** | **202** |
| Integración de examen | `SafeExamBrowser/seb-server` (ETH Zürich) | ⚠️ **MPL-2.0** | **2026-10-01** (`dev-3.0`) | **108** |
| Cliente de examen | `SafeExamBrowser/seb-win-refactoring` | ⚠️ **MPL-2.0** | **2026-09-25** | **20** |

🔵 **La lección de método no es «el registro miente»** —el pase 40 ya había medido eso en los dos sentidos (tendencias
140 y 142)— **sino que la palabra «vacío» necesita un sustantivo.** *«La capa de timetabling está vacía»* es falso;
*«la capa de timetabling no tiene puerta de agente»* es verdadero y es **vendible**: significa que el software que
administra los horarios de una universidad existe, es Apache-2.0, y **nadie le puso todavía una puerta de agente.**

🟢 **Y es una clase de hueco, no un caso:** el software institucional viejo **no se distribuye por npm ni por PyPI**.
Java, C# y PHP institucionales se instalan por WAR, por instalador o por paquete del sistema. **Un barrido que sólo mira
registros de lenguaje moderno es ciego a la mitad desplegada del sector** — y es justo la mitad que tiene los datos.

## 150. El punto de extensión de la pieza más regulada del sector está *carved-out* en Apache-2.0 dentro de un repo AGPL, y lo dice un `README.txt` de 174 bytes (agregado en el pase 41 del 2026-10-02)

**El pase 40 cerró la capa de *proctoring* con un veredicto comercial: *«la única pieza seria es AGPL-3.0, así que fuera
de Open edX la capa hay que construirla»*. La mitad del veredicto es falsa, y la evidencia estaba dentro del paquete.**

| Archivo | Licencia |
|---|---|
| `edx_proctoring-5.2.0.dist-info/LICENSE.txt` | **AGPL-3.0** (*«GNU AFFERO GENERAL PUBLIC LICENSE Version 3»*) |
| 🟢 **`edx_proctoring/backends/LICENSE.txt`** | 🟢 **Apache-2.0** — 11.357 b, contiene *«Apache License / Version 2.0»*, **cero ocurrencias de «Affero»** |
| 🟢 **`edx_proctoring/backends/README.txt`** | **174 b**: *«The code in this directory is licensed under a license different from the rest of the edx-proctoring repository. These modules are licensed under Apache 2.0.»* |

✅ **Verificado en el *wheel* y en el árbol (`master`), los dos con 200.**

🔵 **Por qué esto es una tendencia y no una curiosidad: es un patrón de diseño de licencia que un filtro automático no
ve.** Cualquier herramienta de *compliance* que clasifique repos por el `LICENSE` de la raíz —o por el clasificador de
PyPI— **marca este paquete AGPL y lo descarta entero**, cuando el directorio donde un tercero escribe su integración está
deliberadamente abierto en permisiva. 🔴 **Esta base acaba de descartar esa capa por esa razón exacta, durante un pase
completo.** **Regla nueva y barata: antes de descartar un repo por copyleft, buscar `LICENSE` y `README` en los
subdirectorios de extensión** (`backends/`, `plugins/`, `providers/`, `contrib/`).

### 🔵 El grafo de importación, medido en este mismo pase — y es lo que impide sobrevender el hallazgo

**La pregunta que faltaba: ¿el directorio Apache-2.0 es autocontenido?** Respuesta medida con `ast` sobre los 6 módulos
no-test de `backends/`: 🔴 **no lo es.** Pero **lo que cruza la frontera es vocabulario, no lógica**, y eso es lo que
hace la diferencia:

| Módulo AGPL al que entra el directorio Apache-2.0 | Tamaño | Contenido medido | Qué es |
|---|---|---|---|
| `edx_proctoring/constants.py` | **3.003 b** | **0 clases, 0 funciones, 18 asignaciones de módulo** | 🔵 **constantes puras** |
| `edx_proctoring/exceptions.py` | **4.524 b** | **24 clases, 0 funciones** | 🔵 **taxonomía de excepciones** |
| `edx_proctoring/statuses.py` | **11.088 b** | **5 clases, 0 funciones** | 🔵 **valores de estado** |
| ⚠️ `edx_proctoring/utils.py` | 17.205 b | 26 funciones | 🔴 **lógica real** — pero sólo la usa `software_secure.py` (`decode_and_decrypt`) |
| ⚠️ `edx_proctoring/callbacks.py` | 2.428 b | 1 función | sólo la usa `mock.py` |

🟢 **Un backend que subclasea `BaseRestProctoringProvider` importa exactamente tres cosas del lado AGPL:
`ProctoringBackendProvider` (que es Apache-2.0), `edx_proctoring.exceptions` y `edx_proctoring.statuses`** — o sea
**nombres de excepción y valores de estado.** 🔴 **Los dos módulos con lógica (`utils`, `callbacks`) los importan
únicamente los backends de referencia que ya vienen en la caja, no el que uno escribiría.**

🔵 **Cómo se dice esto con honestidad, que es lo que importa:** *«el contrato que se implementa está en Apache-2.0; lo
que se cruza hacia AGPL son constantes, nombres de excepción y valores de estado, no implementación»*. ⚠️ **Y lo que
esta base NO puede decir, porque es una opinión legal y no una medición: si eso convierte al backend en obra derivada.**
**La medición es ésta; la decisión es de legales**, y el plugin corre **dentro** de un proceso Open edX que es AGPL de
punta a punta de todos modos. **Para un cliente que quiera vender el backend como producto separado, este párrafo es el
insumo de la consulta legal, no su respuesta.**

## 151. «Implementar una interfaz» o «escribir la capa» no es una opinión de arquitecto: se decide contando `@abstractmethod` (agregado en el pase 41 del 2026-10-02)

**La acción 3 del pase 40 preguntaba si integrar un *proctoring* propio en Open edX es implementar una interfaz existente
o escribir la capa desde cero. La respuesta salió de cinco mediciones, y la más informativa es un cero:**

| Medición | Valor | Qué implica |
|---|---|---|
| Modelos de estado de examen ya definidos | **12 clases** | la máquina de estados, las excepciones y la auditoría **no se diseñan** |
| Rutas REST ya expuestas | **20** | la superficie HTTP **no se escribe** |
| Rutas de supresión de datos | **2** (+ método `retire_user`) | el expediente de borrado **se cablea, no se construye** |
| Métodos del punto de extensión | **18** (+8 atributos) | el contrato está escrito |
| 🔵 **`@abstractmethod` en `ProctoringBackendProvider`** | 🔵 **0** | 🟢 **es una base CONCRETA: un backend mínimo sobreescribe sólo lo que usa** |
| Base REST ya provista | `BaseRestProctoringProvider`, **27 métodos** | hasta los constructores de URL vienen hechos |
| Mecanismo de registro | *entry point* `[openedx.proctoring]` | **una línea de `setup.py`** |

🔵 **El cero es el dato que cambia la estimación.** Una interfaz con 18 `@abstractmethod` obliga a implementar 18 métodos
para que el programa arranque; **una base concreta con 18 métodos con default obliga a implementar los que el caso use.**
**Son dos presupuestos muy distintos y la diferencia no se ve en el README: se ve contando decoradores.**

🟢 **Generalización para esta base:** cuando una pieza declara «punto de extensión», hay tres números que deciden si es
adopción o construcción — **cuántos métodos abstractos, cuántos backends de referencia ya vienen (acá 4: `mock`, `null`,
`rpnow4`, `software_secure`) y si hay una base intermedia ya escrita** (acá sí, y es REST).

## 152. La rama por defecto puede ser la rama MUERTA de un proyecto vivo, y el instrumento de fechado de esta base lo registra como «frío» (agregado en el pase 41 del 2026-10-02)

**El pase 37 fechó 49 filas por «el commit de su rama principal» con `ls-remote --symref HEAD`. El instrumento es
correcto y el supuesto es frágil: supone que la rama por defecto es donde se trabaja.**

| Rama de `seb-server` | Último commit | Qué es |
|---|---|---|
| 🔴 **`master`** (apuntada por `HEAD`) | 🔴 **2026-04-01** — **6 meses** | la rama de *release* |
| 🟢 **`dev-3.0`** | 🟢 **2026-10-01** — **ayer** | donde desarrolla; tag `v3.0-latest` publicado |
| 🟢 `development` | **2026-09-30** | |

🔴 **Medido como el pase 37 mide, SEB Server entra a esta base como «FRÍO, 6 meses» — y es falso: commiteó ayer.**
El proyecto tiene **14 ramas** y un flujo `dev-N.N` → `master`.

🟢 **La corrección del instrumento es de una línea: `ls-remote --heads` y tomar el máximo, no `--symref HEAD`.** Cuesta
lo mismo. 🔵 **Y el patrón tiene nombre en el sector: el flujo *git-flow*, que la plataforma institucional europea de
Java usa mucho más que el *trunk-based* de los proyectos de agentes que esta base venía midiendo.** **El instrumento
estaba calibrado para una cultura de desarrollo y se aplicó a otra.**

## 153. Medir todas las ramas cambia 3 de 10 veredictos, y leer el AUTOR los devuelve: un commit vacío de bot y un refactor firmado por un agente no son vida de proyecto (agregado en el pase 41 del 2026-10-02)

**La corrección de la tendencia 152 obliga a una prueba de validez: se re-midieron las 10 filas que el pase 37 declaró
paradas, contra TODAS sus ramas.** El resultado tiene dos mitades y la segunda es la importante.

**Primera mitad — en 7 de 10 la rama por defecto ES la más nueva**: el veredicto del pase 37 se sostiene sin matices
(`openedu-mcp`, `learnmcp-xapi`, `openstax-mcp-server`, `ChatTutor`, `moodle-mcp-server`, `human-skill-tree` y
—por otro motivo— `algo-sensei`).

**Segunda mitad — en 3 de 10 hay una rama más nueva, y al leer quién firmó se desarman dos:**

| Repo | Rama más nueva | Autor | Qué es realmente |
|---|---|---|---|
| ⛔ `trilogy-group/oneroster-ts` | `speakeasy-sdk-regen-1746144633` (**+10,5 meses**) | 🔴 **`speakeasy-github[bot]`** | *«empty commit to trigger [run-tests] workflow»* — **un commit VACÍO de un bot generador de SDK** |
| ⛔ `satvik314/educhain` | `claude/relaxed-curie-mNW2l` (**+5,9 meses**) | 🔵 **`Claude`** | *«Refactor to Educhain 1.0: drop LangChain, build on the OpenAI SDK»* — **una rama escrita por un AGENTE, sin mergear** |
| ⚠️ `plastic-labs/tutor-gpt` | `vineeth/elysia` (**+3,2 meses**) | humano | rama de *feature* parada hace 7,5 meses, entre **49** ramas |

🟢 **Conclusión, y es a favor del pase 37: en 10 de 10 el veredicto sobre el desarrollo HUMANO en la rama principal se
sostiene.** 🔴 **Pero los dos primeros casos habrían entrado como «proyecto reactivado» con sólo mirar la fecha**, y uno
de los dos es literalmente **un commit sin contenido cuyo propósito declarado es patear el CI.**

🔵 **La regla que queda, y es nueva para esta base: medir todas las ramas, y después leer el autor y el mensaje.** Hay
**tres clases de commit que NO son vida de proyecto** y ya tienen instancia medida acá: **el commit vacío de bot**, **la
regeneración automática de SDK** (tendencia 138) y **la rama escrita por un agente y no mergeada**.

🔵 **Y el tercer caso vale aparte, porque es una señal de producto que ninguna fecha capturaba:** la rama que un agente
dejó escrita en `educhain` —alta de los pases 2 y 3 de esta base— **dice hacia dónde iba la 1.0: sacar LangChain y
apoyarse en el SDK de OpenAI.** Está sin mergear desde el 2026-05-29. **Es dirección, no release.**

## 154. La contradicción de licencia se resuelve por la HISTORIA del archivo, y en este caso resulta que no bloqueaba nada (agregado en el pase 41 del 2026-10-02)

**El pase 40 abrió el gap 83 con `exam-guard`: ISC en el manifiesto contra Apache-2.0 en el árbol, y dejó escrito que la
pieza «no se usa en un entregable hasta que el autor resuelva». Resuelto en dos comandos de `git log`, y el veredicto se
invierte.**

| Evidencia | Dato |
|---|---|
| 🔴 Cuándo entró el `LICENSE` Apache-2.0 | **en el commit *«Initial commit»*, 2024-09-10T01:20 — y era el ÚNICO archivo del commit** (201 líneas) |
| Cuándo entró `package.json` con ISC | el commit **siguiente**, *«feat: add base code»*, 2024-09-10T15:39 |
| `LICENSE` modificado desde entonces | 🔴 **nunca** |
| `package.json` modificado desde entonces | **sí, hasta 2025-10-09** |
| ISC en el registro | 🟢 **113 de 113 versiones**, 2024-09-12 → 2026-01-22 |

🟢 **Lectura: el `LICENSE` Apache-2.0 es el artefacto de creación del repositorio** —la casilla *«add a license»* de
GitHub produce exactamente eso, un commit inicial que contiene sólo ese archivo— **y la intención expresada y
re-afirmada 113 veces es ISC.**

🔵 **Y el dato que el pase 40 no había notado, que es el que decide: las dos candidatas son permisivas y OSI.** La
diferencia entre Apache-2.0 e ISC **no es permisiva contra copyleft: es la cláusula de patentes** (Apache-2.0 la concede
expresamente, ISC no la menciona). **La contradicción no bloquea el uso; obliga a anotar cuál se asume.** **El gap 83
baja de bloqueante a anotación.**

🟢 **La regla generalizable, y es barata: antes de tratar una contradicción de licencia como bloqueo, hacer dos
preguntas — ¿las dos candidatas permiten lo que vamos a hacer?, y ¿qué dice la HISTORIA de cada archivo sobre cuál
expresa la intención viva?** Un `LICENSE` del commit inicial que nunca se tocó **pesa menos** que un campo editado
decenas de veces. ⚠️ **Lo cual no quiere decir que el `LICENSE` del árbol deje de ser el documento operativo para un
tercero: quiere decir que hay que pedirle al autor que los alinee, sin que eso frene el trabajo.**

## 155. «Licencia declarada sólo en el manifiesto» eran dos clases de riesgo muy distintas bajo una sola etiqueta (agregado en el pase 41 del 2026-10-02)

**El gap 81 metía en la misma bolsa a `@timadey/proctor` y `@ink-waffle/sisu-mcp`. Medidas de primera mano, no se
parecen — y la diferencia es de acción, no de matiz.**

| Pieza | Declaraciones de licencia que existen | Dónde | Clase real |
|---|---|---|---|
| ⚠️ `Timadey/proctor` | 🟢 **TRES** | manifiesto npm + **`package.json` del árbol** + **README del árbol** (badge *«License: MIT»* **y** *«licensed under the MIT License — see the [LICENSE] file for details»*) | 🟢 **ARCHIVO FALTANTE.** El árbol **apunta** al archivo que no existe. Medido con `git log --all --name-only`: **0 coincidencias de `licen|copying` en toda la historia, en todas las ramas** |
| 🔴 `@ink-waffle/sisu-mcp` | 🔴 **UNA, en todo el mundo** | sólo el campo `license` de npm | 🔴 **SIN SEGUNDA FUENTE POSIBLE.** Tarball de 44.781 b con 17 `dist/*.js`, **sin `LICENSE` y sin README**; sin `repository` ni `homepage` |

🟢 **La consecuencia práctica es que una se desbloquea y la otra no.** Para `@timadey/proctor` **la intención es
inequívoca y está escrita tres veces**: lo que falta es el texto, y **se cierra con un PR de un archivo** —el aporte
*upstream* más barato que esta base identificó, y deja a Globant como contribuyente. Para `sisu-mcp` **no hay dónde
buscar una segunda declaración**, y sigue siendo **la única puerta de SIS de educación superior de esta base**: sigue sin
poder proponerse.

🔵 **La regla que queda: la clase de evidencia de una licencia se mide CONTANDO declaraciones independientes y mirando si
alguna vive en el árbol**, no con la etiqueta binaria *«tiene `LICENSE` / no tiene»*. **Tres declaraciones en el árbol
apuntando a un archivo ausente es un descuido demostrable. Una sola declaración en un registro es un dato sin
corroborar.**

## 156. El *proctoring* es la única capa de esta base nombrada como alto riesgo por DOS reguladores de dos regiones, y es la que acaba de medirse sin competencia agéntica (agregado en el pase 41 del 2026-10-02)

**Las dos mitades de este pase se cruzan en un punto, y el cruce es la oportunidad.**

| Regulador | Instrumento | Qué nombra | Fecha de cumplimiento |
|---|---|---|---|
| 🇪🇺 **EMEA** | AI Act, **Anexo III punto 3** | *«monitoreo durante exámenes»*, además de acceso, admisión y evaluación de resultados | **2027-12-02** |
| 🇻🇳 **APAC** | Lista de 6 sectores de alto riesgo de **Vietnam** | **evaluación automatizada y *monitorización del comportamiento*** en educación | **2027-03-01** — ⚠️ **9 meses ANTES que la UE** |

**Y el estado de la oferta en esa misma capa, medido este pase:**

| Pieza | Licencia | Puerta de agente |
|---|---|---|
| `openedx/edx-proctoring` | AGPL-3.0 (🟢 `backends/` **Apache-2.0**) | 🔴 **no existe** |
| `SafeExamBrowser/seb-server` | MPL-2.0 | 🔴 **no existe** (36 controladores sin envolver) |
| `UniTime/unitime` | Apache-2.0 | 🔴 **no existe** (15 conectores sin envolver) |
| npm: 8 nombres `*-mcp` probados | — | 🔴 **404 en 8 de 8** |
| PyPI: índice completo (46,6 MB) | — | 🔴 **0 nombres** |

🔵 **La lectura comercial, y es la más fuerte que esta base produjo en varios pases: la capa con el plazo regulatorio más
cercano de dos regiones distintas es también la que no tiene competencia agéntica open source.** Y **ya no hay excusa de
licencia**: la ruta Open edX tiene su punto de extensión en Apache-2.0 y la ruta independiente es MPL-2.0.

⚠️ **Y el orden correcto de la conversación con el cliente, que este pase no cambia: primero el expediente, después el
agente.** Vietnam vence **antes** que la UE, así que para un cliente con operación en los dos lados **la fecha que manda
es marzo de 2027**. 🔴 **Fuente, declarada: canal del buscador, fuentes secundarias comerciales — las primarias
multilaterales y de la UE siguen bloqueadas en este entorno (gap 65).** **Antes de poner la fecha vietnamita en un
documento contractual hay que verla en su boletín oficial.**

## 🔵 Estado de gaps al cierre del pase 44 del 2026-10-02

**Este pase ejecutó las TRES acciones del pase 43. Las tres rindieron, y la primera rindió encontrando cuatro defectos
en la medición del pase anterior — ninguno en el upstream.**

| Gap | Estado | Resolución |
|---|---|---|
| **Acción 1** (completar `operations.tsv` con los controladores que faltaban) | ✅ **CUMPLIDA sobre el servicio entero, y además EJECUTADA** | **79 → 341 operaciones**, **4 → 31 controladores**, **30 endpoints**, **170 escrituras**, `endpoints.tsv` **42 → 55**; `test_gate.py` **11 → 37 aserciones, 37/37 en verde**. 🔵 **Y queda reproducible, no transcrito:** `extract_surface.py` regenera las dos tablas contra un checkout (tendencias **166**–**170**) |
| **Acción 2** (costo de *authoring* del `v1` de Open edX) | ✅ **CUMPLIDA — las tres preguntas con número, y la premisa de una era falsa** | `create_xblock_response` → **`{locator, courseKey}`**, y el `locator` **es** el usage key ⇒ **1 POST por bloque, cero lecturas intermedias**. `category`: **sin enum** en curso, **`["html","problem","video"]`** en biblioteca v1. `?view=minimal`: **sólo `retrieve`** — 🔴 **y no hay hijos que recorrer**, así que el recorrido va por `course_index` **en una llamada** (tendencias **171**, **172**; **P96**) |
| **Acción 3** (fechas del AI Act contra el texto consolidado) | ⚠️ **CUMPLIDA A MEDIAS por límite de entorno, y el resultado es A FAVOR** | ✅ **Anexo III 2027-12-02 y Anexo I 2028-08-02 CONFIRMADAS por segundo canal independiente** (Reg. (UE) 2026/1744, OJ 2026-07-24, en vigor 2026-07-27): **la recomendación de EMEA NO se revierte**. 🔴 **No contra el texto consolidado:** los dos canales dan **403** (**gap 92**) |
| 🟢 **91 (NUEVO)** — el plazo que vence primero no estaba en esta KB | 🟢 **ABIERTO como oportunidad con fecha, no como hueco** | **Art. 50(2): 2026-12-02, 61 días**, para generativos **ya en el mercado** antes del 2026-08-02; 50(1)/(3)/(4) **en vigor desde el 2026-08-02**. ✅ Confirmado sin prórroga por el **9.º plenario del Consejo Europeo de IA (2026-09-17)**. **La acción 3 del pase 45 es medir cuántas de las 66 filas de `agents/top.md` quedan expuestas** (tendencia **173**) |
| 🔴 **92 (NUEVO)** — el gap 65 alcanza también a los agregadores legales **privados** | 🔴 **ABIERTO, y es de clase más ancha de lo que esta base creía** | `eur-lex.europa.eu` **y `artificialintelligenceact.eu`** dan los dos **`403` a CONNECT** (`EGRESS_BLOCKED` confirmado por el relay). El segundo **no es institucional ni multilateral**, así que **«las fuentes primarias multilaterales son inalcanzables» era una descripción demasiado angosta del bloqueo** |
| 🔴 **93 (NUEVO)** — la OTRA puerta de esta base se construyó con el extractor defectuoso | 🔴 **ABIERTO, y es la acción 1 del pase 45** | `compose/code/unitime-mcp-gate/` se escribió en el pase 42 **con el mismo método** que produjo los cuatro defectos de SEB Server, y **antes de que existieran los cuatro controles**. **De las dos puertas que esta KB entrega, una está verificada y la otra no** |
| 🟢 **94 (NUEVO)** — el generador de curso está cotizado pero no escrito | 🟢 **ABIERTO, y es la acción 2 del pase 45** | Con **P96** el costo ya tiene número (N POSTs, camino crítico 4, hermanos en paralelo). Falta el artefacto: un generador + *stub* que asevere el encadenado `locator → parent_locator`, los lotes de hermanos y el rechazo de `category` **en el cliente** (porque el servidor da **500, no 400**) |
| ✅ **86** (capa de examen completa) | ✅ **SIGUE CERRADO, y ahora cubre el servicio** | El pase 43 lo cerró con 4 endpoints; este pase lo lleva a **30 endpoints y 341 operaciones**. 🔴 **Pero con una corrección de licencia que lo sostiene: SEB Server es MPL-2.0 y el README de la puerta decía Apache-2.0** — y la ruta recomendada (publicar **un** valor de `enum`) **sólo vale bajo MPL** |
| ✅ **71** (contar filas no detecta una fila repetida) | ✅ **EL CONTROL SIGUE PASANDO — y encontró otra cosa** | **66 filas, 61 slugs de GitHub, los 61 distintos, 0 duplicados**, más 5 entradas de registro. 🔴 **Lo que falló fue la aritmética, no el control: esta base venía publicando «63 filas»** |
| ⚠️ **65** (fuentes primarias inalcanzables) | ⚠️ **REFORMULADO Y AMPLIADO por el gap 92** | Deja de ser *«los dominios institucionales multilaterales»* y pasa a ser *«el dominio legal, institucional o privado, es inalcanzable por política del proxy»*. **Toda afirmación regulatoria de esta KB se apoya en fuentes secundarias comerciales por construcción del entorno**, y hay que decirlo cada vez que se cite una fecha |
| ⚠️ **81** / **83** (licencia sólo en el manifiesto / contradictoria) | ⚠️ **SIN CAMBIO — la acción que falta es hacia afuera** | El PR de un archivo a `Timadey/proctor` y el contacto a `@ink-waffle/sisu-mcp` **siguen siendo acciones con destinatario humano**: esta corrida tampoco le escribe a terceros |
| 🔴 **57** (crear un curso no está en el árbol REST versionado) | 🔴 **SIN CAMBIO, y P96 lo deja explícito** | `course_handler` + `course_rerun` siguen fuera de `/api/contentstore/v1/`. **P96 cotiza el árbol, no el *bootstrap* del curso** |

⚠️ **Nota de concurrencia:** este pase corrió con el `HEAD` de `education-kb` en `ba960bf` (pase 43). Si otra corrida
tocó los mismos ocho archivos en paralelo, el *merge* manda sobre la numeración de tendencias y gaps.

## 🔵 Estado de gaps al cierre del pase 41 del 2026-10-02

**Este pase ejecutó las TRES acciones del pase 40. Las tres rindieron, y la de mayor valor comercial corrigió un
veredicto que esta base había publicado como cerrado.**

| Gap | Estado | Resolución |
|---|---|---|
| **Acción 1** (inventariar *timetabling* y *proctoring* por sitio de proyecto) | ✅ **CUMPLIDA — 3 repos medidos desde el árbol** | `UniTime/unitime` (🟢 **Apache-2.0**, `HEAD` **2026-10-01**, 202 tags) y la familia SEB (⚠️ **MPL-2.0**: `seb-server` + `seb-win-refactoring`). 🟢 **Y la respuesta a «¿hay API envolvible?» es SÍ en los dos: 15 conectores con nombre en UniTime, 36 controladores / 41 endpoints en SEB Server** (tendencia **149**) |
| **Acción 2** (resolver las tres contradicciones de licencia) | ✅ **CUMPLIDA en lo medible; 1 parte queda con destinatario humano** | **Gap 83 CERRADO** por historia de archivo (tendencia **154**). **Gap 81 PARTIDO EN DOS** clases con acciones distintas (tendencia **155**). ⚠️ **No se abrió *issue* ni se mandó correo a ningún autor: es una acción hacia afuera y no la decide una corrida automática** |
| **Acción 3** (superficie real de `edx-proctoring`) | ✅ **CUMPLIDA — y corrige el veredicto del pase 40** | **12 modelos, 20 rutas, 18 métodos de proveedor, 🔵 0 `@abstractmethod`, base REST de 27 métodos, *entry point* `[openedx.proctoring]` con 4 backends.** 🟢 **Es implementar una interfaz, no escribir la capa** (tendencia **151**) |
| 🔴 **84** (*proctoring*: no hay opción permisiva) | 🔴 **CORREGIDO — era falso por DOS motivos independientes** | 🟢 **(1) `edx_proctoring/backends/` está *carved-out* en Apache-2.0** dentro del repo AGPL, declarado en un `README.txt` de 174 b y verificado en el *wheel* y en el árbol. 🟢 **(2) Existe una capa de integración de examen permisiva fuera de Open edX: `seb-server`, MPL-2.0 (copyleft débil), de ETH Zürich, con `OPEN_EDX`/`MOODLE`/`MOODLE_PLUGIN`/`OPEN_OLAT` ya en su `enum LmsType`** (tendencias **150** y **149**) |
| ✅ **83** (licencia contradictoria manifiesto/árbol) | ✅ **CERRADO — y baja de bloqueante a anotación** | El `LICENSE` Apache-2.0 de `exam-guard` entró en el ***«Initial commit»* como único archivo** y nunca se tocó; `package.json` declara **ISC** y se editó hasta 2025-10-09; **ISC en 113/113 versiones**. 🔵 **Las dos candidatas son permisivas OSI: la contradicción NO bloquea el uso**, sólo cambia la cláusula de patentes (tendencia **154**) |
| ⚠️ **81** (licencia sólo en el manifiesto) | ⚠️ **REFORMULADO — eran dos clases, no una** | 🟢 **`Timadey/proctor`: TRES declaraciones, todas en el árbol** (`package.json`, badge del README y sección *«see the LICENSE file»*), y **0 coincidencias de licencia en toda la historia de todas las ramas** → **archivo faltante, demostrable, se cierra con un PR de un archivo**. 🔴 **`@ink-waffle/sisu-mcp`: UNA declaración en todo el mundo**, tarball sin `LICENSE` **y sin README**, sin repo → **sigue sin poder proponerse** (tendencia **155**) |
| ✅ **85** (*timetabling*: el servidor que nunca se publicó) | ✅ **CERRADO en su mitad de inventario** | `unitime` **no está en PyPI porque no se distribuye por PyPI**: es Java institucional. 🟢 **Medido por repositorio existe, está vivo (commit de ayer) y es Apache-2.0.** 🔴 **La mitad de puerta de agente sigue vacía y pasa al gap 86** |
| 🟢 **NUEVO 86** (no existe puerta de agente para ninguna de las dos capas) | 🔴 **ABIERTO — y es la oportunidad mejor medida de este pase** | **npm: 404 en 8 de 8** nombres probados (`unitime-mcp`, `mcp-unitime`, `seb-mcp`, `mcp-seb`, `safeexambrowser-mcp`, `sebserver-mcp`, `timetable-mcp`, `timetabling-mcp`). **PyPI, índice completo de 46,6 MB: 0 nombres.** 🟢 **Dos capas con despliegue institucional, licencia usable, API formal — y cero competencia.** Ver **P88** y **P89** |
| ⚠️ **NUEVO 87** (¿qué rama de SEB Server se instala?) | ⚠️ **ABIERTO — es de despliegue, no de licencia** | `master` **2026-04-01** (6 meses) contra `dev-3.0` **2026-10-01** (ayer), con tag `v3.0-latest`. **Hay que decidir si el entregable se para en el release o en la rama** antes de proponerlo |
| 🔵 **NUEVO 88** (¿es autocontenido el directorio Apache-2.0?) | 🔵 **CERRADO COMO MEDICIÓN, abierto como decisión de legales** | 🔴 **No es autocontenido**, pero 🟢 **lo que cruza es vocabulario y no lógica**: `constants.py` (0 clases, 0 funciones, 18 asignaciones), `exceptions.py` (24 clases, 0 funciones) y `statuses.py` (5 clases, 0 funciones). **Los dos módulos con lógica (`utils`, `callbacks`) los importan sólo los backends de referencia.** ⚠️ **Si eso hace obra derivada es pregunta legal, no de ingeniería** |
| ⚠️ **NUEVO 89** (el instrumento de fechado mide la rama equivocada) | ⚠️ **ABIERTO — y hay que re-correr el pase 37 entero** | 🔴 **`ls-remote --symref HEAD` toma la rama de *release*, no la de trabajo: SEB Server se registraría como «FRÍO 6 meses» y commiteó ayer** (tendencia **152**). La prueba de validez sobre las 10 filas paradas **sostiene 10 de 10 veredictos al leer el autor** (tendencia **153**), **pero las 39 filas restantes no se re-midieron con el instrumento corregido** |
| **147** (`HEAD` mide al proyecto, el release mide lo que el cliente instala) | ⚠️ **CONFIRMADO y con el caso INVERSO** | `exam-guard` tiene el **registro DOS *majors* adelante del repo**: árbol en **8.1.0** (`HEAD` 2025-10-09) contra **10.0.4** publicada el **2026-01-22**. 🔴 **No se puede leer el fuente de lo que el cliente instalaría** — la regla vale en los dos sentidos |
| **131** (`curl` sobre `github.com` devuelve 403 para todo) | ✅ **RE-CONFIRMADO con control negativo explícito** | **4 de 4 iguales (403)** en dos repos reales y dos inventados; **`git ls-remote` acierta 4 de 4**. **Toda URL de GitHub de este pase se verificó clonando el árbol**, que es evidencia más fuerte que un `HEAD` de HTTP |
| **26** (capa que decide sobre el alumno) | 🟢 **sigue reformulado a favor desde el pase 40** | Sin avance deliberado este pase: las tres acciones del 40 tenían prioridad |
| **60** / **61** / **68** / **65** / **80** / **82** | 🔴 **ABIERTOS, sin avance deliberado** | El **65** (primarias legales y multilaterales) y el **80** (sin *daemon* de Docker) siguen siendo **límites de entorno**, no de método. **No insistir por esas vías** |

## 🔵 Tendencias 157–166 — el pase 42 del 2026-10-02

### 157 — 🔴 La licencia permisiva cuesta más código que la copyleft, y es al revés de lo que se supone

**Medido en las dos rutas de *proctoring* de esta base.** `edx-proctoring` expone `ProctoringBackendProvider` como **clase
concreta: 18 métodos, 0 `@abstractmethod`** — se hereda y se sobreescribe lo que haga falta. `seb-server` expone
`RemoteProctoringService` como **interfaz desnuda: 14 métodos, 2 `default`, 12 obligatorios**. 🔵 **La ruta cuya licencia
es más cómoda (MPL-2.0, copyleft débil, por archivo) es la que pide más trabajo; la que arrastra AGPL regala la
implementación base.** **Regla para cotizar: la licencia dice qué podés publicar, no cuánto vas a escribir. Son dos
preguntas y hay que medir las dos.**

### 158 — 🟢 El copyleft más barato que esta base cotizó: un valor de enum

**MPL-2.0 es copyleft por ARCHIVO** (§1.10(a): *«cualquier archivo … que resulte de una adición, eliminación o
modificación del contenido de *Covered Software*»*). En `seb-server` el registro de un proveedor de *proctoring* es
**abierto** —`RemoteProctoringServiceFactory(Collection<RemoteProctoringService>)`, inyección de Spring, la fábrica no se
toca— pero `getType()` devuelve un **enum con exactamente dos valores**. **10 archivos *Covered* mencionan el enum; sólo
1 hay que modificar.** 🟢 **La divulgación obligatoria es un valor de enum, y la lógica del proveedor —archivo nuevo, sin
*Covered Software* dentro— queda propietaria.** 🔵 **Es un dato que cambia una conversación de licenciamiento con un
cliente, y se obtuvo contando referencias, no leyendo la licencia.**

### 159 — ⚠️ El validador que no rechaza: un tipo desconocido pasa SIN validar

`ProctoringSettingsValidator.isValid()` pregunta `if (serverType == JITSI_MEET || serverType == ZOOM)` y **cae a
`return true`**. **Un tercer proveedor no es rechazado: pasa sin validación de campos.** 🔵 **No es un bloqueo, es
trabajo**: hay que escribir la validación de los campos propios. ⚠️ **Y es la clase de detalle que, no dicho, aparece en
UAT como un defecto del integrador.** **Se escribe en la propuesta.**

### 160 — 🔴 El `enum` del LMS decide más que la licencia, y el pase anterior lo leyó incompleto

`LmsSetup.java` (`dev-3.0`) declara **seis** `LmsType`, cada uno con su `EnumSet<Features>`: `MOCKUP`, `OPEN_EDX`,
`MOODLE`, `MOODLE_PLUGIN`, `ANS_DELFT`, `OPEN_OLAT`. 🔴 **`LMS_FULL_INTEGRATION` —las llamadas del LMS *hacia* SEB
Server— existe sólo en `MOCKUP` y `MOODLE_PLUGIN`: NO en `OPEN_EDX`.** 🔴 **Y `MOODLE` a secas tiene `SEB_RESTRICTION`
comentada en el fuente.** **El pase 41 había leído cuatro valores y ninguna matriz.** 🔵 **La consecuencia comercial: la
pregunta que decide la ruta no es *«qué licencia tolera el cliente»* sino *«qué LMS tiene»*.** Ver **P91**.

### 161 — 🟢 La primera puerta de agente de esta KB que se entrega PROBADA, y lo que la vuelve proponible es lo que retiene

**26 tools generados del árbol de `UniTime/unitime`** (15 conectores × verbos leídos de los `do*` sobreescritos),
montados sobre el *gateway* del pase 40. **23 aserciones, 23 en verde.** 🔴 **La que importa: `0 de 9` llamadas retenidas
llegaron al upstream** —entre ellas `script.post`, que arma un `ExecuteScriptRpcRequest` y **ejecuta un script del
servidor**. 🔵 **Un envoltorio ingenuo de los 15 conectores publica ejecución remota como tool de un agente.** **La
diferencia entre una demo y un entregable es la allowlist, y se prueba con un *stub* que registra cada llamada recibida —
no con un *prompt* que pide no usar la herramienta.** Ver **P92**.

### 162 — 🟢 La tabla de esta KB está más viva de lo que la KB venía diciendo, y el instrumento anterior la subestimaba

**61 filas, 472 ramas, cobertura 61/61.** Reparto corregido: **48 activas (78,7 %)**, 3 tibias, 7 frías, 3 congeladas.
El pase 37, midiendo por rama por defecto, decía **69,4 %**. 🔵 **El gap 89 tenía razón en las DOS direcciones:** cuatro
veredictos se promueven (`algo-sensei` FRÍO → ACTIVO, `gradescope-mcp` y `TutorIA` tibio → ACTIVO, `open-badges-mcp`
tibio → ACTIVO) **y dos se sostienen sólo porque el filtro los sostiene.** ⚠️ **Matiz honesto sobre `algo-sensei`: el
pase 37 no se equivocó al medirlo —el proyecto commiteó hoy, después de esa medición.** **Una fila fría no es una fila
muerta: es una fila que hay que volver a mirar.**

### 163 — 🔴 La clase que faltaba en el filtro de vitalidad, y es la más común de todas: `dependabot`

El pase 41 nombró tres clases que no son vida de proyecto (commit vacío de bot, regeneración de SDK, rama de agente sin
mergear). **Medidas 472 ramas, son seis**, y la que más cuentas cambia es la que faltaba: **ramas de `dependabot` /
`renovate` con un *bump* de dependencia — 4 repos, 18 ramas.** `suren-kk/armenian-national-library-mcp` tiene **10**, y
hace parecer el repo **7 semanas** más fresco de lo que es. **Las otras dos nuevas: `bot-other` (autor `[bot]` en rama no
defecto) y `auto-content`** (`OATutor` → `content-staging`, *«Automated content update»*, autor `Generic User`: un
*pipeline* de contenido no es desarrollo). 🟢 **Confirmación independiente en un repo fuera de la tabla: `KualiCo/rice`
también tiene su rama más nueva en `dependabot/`.**

### 164 — 🔵 Un filtro de más no se nota, porque se parece exactamente a un proyecto muerto

**Defecto encontrado en el instrumento de ESTE pase, no del anterior.** La primera versión aplicaba los seis filtros a
todas las ramas, **incluida la de defecto**. Resultado medido: `jupyterlab/jupyter-ai` perdía 3 meses (el tip de su `main`
lo firma un `[bot]`), y **`zijinz456/OpenTutor` y `microsoft/Shiksha-Copilot` quedaban sin NINGUNA fecha de vida.**
🟢 **La regla que queda: el tip de la rama por defecto cuenta SIEMPRE como vida —es historia mergeada, y un commit de
release firmado por un bot en `main` sigue siendo el proyecto publicando—; los filtros deciden únicamente si una rama
NO-defecto agrega vida por encima de ella.** ⚠️ **Es la misma familia de error que el `200` de PyPI del pase 40 y el
`403` de `curl` del 37: el instrumento falla hacia el lado que se confunde con el resultado esperado.** **Tercera vez que
el instrumento del pase anterior se corrige al EJECUTARLO en vez de leerlo.**

### 165 — 🔴 El reparto de licencias que se repite: el *middleware* es permisivo y la aplicación que el cliente quiere es copyleft

**La familia `Kuali`, medida en este pase y ausente de esta KB durante 41 pases:** `kuali/rice` y `KualiCo/rice` son
**ECL-2.0** (*Educational Community License v2.0*, derivada de Apache-2.0, aprobada por la OSI) y son el **middleware**;
`kuali/kc` (administración de investigación) y `kuali/kfs` (finanzas) son **AGPL-3.0** y son las **aplicaciones**.
🔴 **Los cuatro están muertos: entre 6 y 9 años sin commits reales.** 🔵 **Pero la forma importa porque se repite:**
`edx-proctoring` (núcleo AGPL, `backends/` Apache-2.0), `lrsql`/`Ralph` contra Learning Locker, y ahora Kuali.
**La licencia usable suele estar en la capa que no resuelve el problema del cliente.** ⚠️ **Y el barrido global devolvió
Kuali descrito en PRESENTE: una propuesta escrita desde el buscador lo habría ofrecido como opción viva.**

### 166 — 🔴 La primaria de mayor autoridad para EMEA existe, es de este mes, y está bloqueada

El barrido EMEA identificó la ***2nd Working Conference*** del **Consejo de Europa** sobre las **dimensiones regulatorias
de la AI en educación**, **octubre de 2026**. 🔴 **`coe.int` responde `EGRESS_BLOCKED` en este entorno.** Se conocen
título, convocante y mes; **no** fechas exactas, sede ni si cita un instrumento jurídico por nombre o número. 🔵 **Es
una instancia NUEVA del gap 65 y la más valiosa: hasta ahora el gap se sostenía en EUR-Lex y en las tres primarias de
LATAM.** 🟢 **Queda como acción con destinatario humano: alguien con acceso a `coe.int` lo cierra en diez minutos.**
⚠️ **Y en el mismo barrido —el de North America— la fecha vencida del AI Act reapareció por NOVENA vez.** **Nueve
reapariciones en veinticuatro pases dejan de ser el error de una fuente: son una propiedad del canal, y la regla es no
citar nunca la fecha del AI Act desde un buscador.**

## 🔵 Estado de gaps al cierre del pase 42 del 2026-10-02

**Este pase ejecutó las TRES acciones del pase 41. Las tres rindieron, y la primera corrigió una recomendación comercial
que esta base ya había publicado.**

| Gap | Estado | Resolución |
|---|---|---|
| **Acción 1** (escribir y probar la puerta MCP de UniTime) | ✅ **CUMPLIDA Y PROBADA** | **26 tools del árbol → 13 expuestos. 23 aserciones en verde**, entre ellas **0 de 9 llamadas retenidas llegaron al upstream** y *allowlist* vacía → **0 tools**. Probada además **extremo a extremo por stdio real**. Ver **P92** |
| **Acción 2** (re-fechar con el instrumento corregido) | ✅ **CUMPLIDA — 61/61, 472 ramas** | **4 veredictos promovidos, 2 sostenidos por el filtro.** Reparto **78,7 % activas** contra 69,4 % del pase 37. 🔴 **Las tres clases de no-vida son SEIS: falta `dependabot`, y es la más común** |
| **Acción 3** (enumerar `seb-server` al nivel de `edx-proctoring`) | ✅ **CUMPLIDA — y corrige al pase 41** | **313 `.java` en `servicelayer/`, 75 de *proctoring*.** SPI `RemoteProctoringService`: **12 obligatorios de 14**. Registro abierto, **tipo cerrado**. **Divulgación obligatoria = 1 valor de enum.** Ver **P91** |
| **89** (la rama por defecto puede ser la rama muerta) | ✅ **CERRADO — y tenía razón en las dos direcciones** | Medido sobre 472 ramas. **El número publicado estaba mal en la dirección peligrosa en 4 filas** (subestimaba vida) **y el filtro evitó 2 promociones falsas** |
| **86** (las dos capas institucionales sin puerta de agente) | 🟢 **CERRADO A MEDIAS — la mitad UniTime tiene puerta** | **La puerta de UniTime existe y está probada (P92).** 🔴 **La de `seb-server` sigue sin existir**: queda como la mitad abierta del gap |
| **87** (`master` de `seb-server` tiene 6 meses) | ⚠️ **CONFIRMADO y usado como regla** | `dev-3.0` commiteó **2026-10-01** (`Andreas Hefti`, *«code cleanup»*); `master`, 2026-04-01. **Todo lo enumerado en este pase está medido en `dev-3.0`, y se declara** |
| **NUEVO 90** (el validador de SEB no valida a un tercero) | ⚠️ **ABIERTO como trabajo cotizable, no como bloqueo** | `ProctoringSettingsValidator` cae a `return true`. **Es alcance que hay que incluir en la propuesta** (tendencia **159**) |
| **NUEVO 91** (`LMS_FULL_INTEGRATION` no está en Open edX) | 🔴 **ABIERTO como límite de producto** | Sólo `MOCKUP` y `MOODLE_PLUGIN` lo declaran. **Para un cliente Open edX la ruta SEB no da integración plena**, y eso no se arregla con código propio: está en el `enum` del upstream (tendencia **160**) |
| **65** (primarias legales / multilaterales) | 🔴 **ABIERTO — y con un dominio bloqueado NUEVO y de alta autoridad** | 🔴 **`coe.int` → `EGRESS_BLOCKED`**, y era la primaria regulatoria educativa de EMEA (tendencia **166**). 🟢 **Avance parcial en LATAM: la primaria de IESALC aparece por un SEGUNDO canal (UNU), con 200 instituciones y 5 dimensiones confirmadas.** ⚠️ **La fecha del AI Act reapareció por NOVENA vez y sigue sin verse en EUR-Lex** |
| **81** (licencia sólo en el manifiesto) / **83** (licencia contradictoria) | ⚠️ **SIN CAMBIO — y la acción que falta es hacia afuera** | El PR de un archivo a `Timadey/proctor` y el contacto a `@ink-waffle/sisu-mcp` **siguen siendo acciones con destinatario humano**: este pase tampoco le escribe a terceros |
| **40** (el cartucho MCP de CaSS) / **60** (mitad QTI) / **61** (curso origen vacío) / **68** / **80** (sin Docker) | 🔴 **ABIERTOS, sin avance deliberado** | Las tres acciones del 41 tenían prioridad. **El 80 no se reintenta: el pase 39 dejó escrito «no insistir por esta vía»** |
| **26** (capa predictiva) | 🟢 **SIN CAMBIO — sigue reformulado a favor** | `datakind/student-success-tool` (MIT) sigue siendo la respuesta, y el barrido de North America de este pase **refuerza por qué**: sin regulador federal, *«humans in the loop by design»* es argumento comercial |

## Nota de método del pase 43 (2026-10-02) — el pase que ejecutó las tres acciones **y encontró que la premisa de una cuarta estaba invertida**

**Lo que se hizo:** el barrido obligatorio completo —**cuatro búsquedas globales y cuatro regionales**, con el año
**calculado** (`date +%Y` → **2026**)— más **las tres acciones que el pase 42 dejó escritas**. 🟢 **Las tres se
ejecutaron y las tres dieron resultado**, dos de ellas con código que compila y corre en este repositorio. Y además se
cerró **el gap 50**, que venía de un bloque de acciones anterior y cuya premisa resultó **falsa**.

🔴 **La corrección que encabeza el pase, porque cambia una cotización:** el handoff que dejó el gap 50 decía que había
que medir el `v0` de *authoring* de Open edX **«que son los que el propio repo recomienda sobre el `v1` experimental»**.
**Es al revés.** Ver la tendencia **157**.

## 157. El `v0` de *authoring* de Open edX está **deprecado en favor del `v1`**, y esta base lo tenía al revés — la banda de deprecación es la fuente, no la memoria (agregado en el pase 43 del 2026-10-02)

El archivo `cms/djangoapps/contentstore/rest_api/v0/views/xblock.py`, leído de primera mano sobre `master` por
`raw.githubusercontent.com` el **2026-10-02**, abre así:

```
Public rest API endpoints for the CMS API — v0 xblock (DEPRECATED).

.. deprecated::
    These views are superseded by ``XblockViewSet`` in
    ``cms.djangoapps.contentstore.rest_api.v1.views.xblock``.
    Use ``/api/contentstore/v1/xblock/`` going forward.
    These v0 endpoints will be removed in a future release.
```

Y cada método del `v0` emite `warnings.warn(_DEPRECATION_MSG, DeprecationWarning)`.

🔵 **El `v1` no es «el experimental»: es el canónico, y trae más de lo que el `v0` tenía.** `XblockViewSet` está
construido sobre los **ADR de la FC-0118** y eso es lo que se cotiza:

| Lo que aporta el `v1` | ADR | Por qué se cotiza |
|---|---|---|
| CRUD consolidado en un `ViewSet` vía `DefaultRouter` | **0028** | Un solo recurso, cinco verbos: `POST /`, `GET/PUT/PATCH/DELETE /{usage_key}/` |
| Sobre de error **estandarizado** | **0029** | El manejo de error del cliente se escribe una vez, no por endpoint |
| `authentication_classes` y `permission_classes` explícitos | **0026**, **0034** | `JwtAuthentication` + `SessionAuthenticationAllowInactiveUser`; **sin** `BearerAuthentication` ni `OAuth2Authentication` |
| **`?view=minimal`** | **0036** | Devuelve sólo `id`, `display_name`, `category`, `children`, `has_children`, `studio_url`. 🔵 **Es el que hace barato recorrer el árbol de un curso**: la respuesta completa trae `data`, `metadata`, `student_view_data` y OLX |
| Tag OpenAPI **`openedx-platform-sdk`** | **0027** | El `ViewSet` está declarado para **generación de SDK**, no sólo para Swagger |

⚠️ **La trampa que viene con el `v1` y hay que escribir en la propuesta:** `?fields=` **no** es un selector de subconjunto
de campos como sugiere el ADR 0036. Es un **pass-through legacy** que selecciona *tipo de respuesta*
(`?fields=graderType`, `?fields=ancestorInfo`, `?fields=customReadToken`). El repo decidió **no** reutilizar el nombre
para no romper clientes, y lo documenta como deprecado. **Quien use `?fields=` esperando ADR 0036 recibe otra cosa.**

🔵 **La lección de método, que es la que vale más allá de Open edX:** esta base tenía la recomendación invertida porque la
tomó de prosa de documentación y no del **encabezado del módulo**. La banda `.. deprecated::` y el `DeprecationWarning`
son **datos del árbol**, con la misma autoridad que el archivo `LICENSE` en la tendencia 129. **Se leen antes de elegir
versión de API.**

## 158. **Gap 50, CERRADO:** en Open edX la sección, la subsección, la unidad y el componente son **el mismo endpoint** — el árbol vive en el cuerpo, no en la ruta (agregado en el pase 43 del 2026-10-02)

La pregunta del gap 50 era si el *authoring* por HTTP cubre **crear/actualizar curso, secciones y componentes**. Medido
endpoint por endpoint sobre `master`, la respuesta es de tres partes y conviene darla separada porque **se cotiza
distinto**:

| Nivel | ¿Cubierto por HTTP? | Dónde |
|---|---|---|
| **El curso** | 🔴 **No en el árbol versionado** (ni `v0` ni `v1`) | ✅ **Sí en la vista legacy**: `POST /course/`, como ya midió el pase 32. El `v1` sólo tiene **`course_rerun`**, que **clona** un curso existente |
| **Sección (`chapter`), subsección (`sequential`), unidad (`vertical`)** | 🟢 **Sí** | `POST /api/contentstore/v1/xblock/` |
| **Componente (bloque hoja)** | 🟢 **Sí** | `POST /api/contentstore/v1/xblock/` — **el mismo endpoint** |

🔵 **El hallazgo que simplifica el *wiring*, y es el que esta base no tenía escrito:** **no hay un endpoint por nivel de
jerarquía.** En Open edX la sección, la subsección y la unidad **son XBlocks**, igual que un componente, así que los
cuatro se crean con la misma llamada. Lo que distingue un nivel de otro son **dos campos del cuerpo**, leídos del
`XblockSerializer`:

* **`parent_locator`** — de quién cuelga. El `ViewSet` lo extrae del cuerpo crudo (`request._request.body`, no
  `request.data`, para no consumir el *stream* WSGI) y de ahí deriva el `course_key` **antes** de que DRF corra los
  permisos.
* **`category`** — qué es (`chapter`, `sequential`, `vertical`, o el tipo de bloque).

El serializer es **estricto** (`StrictSerializer`: tipos validados y **ningún campo inesperado admitido**) y los campos
disponibles son `id`, `parent_locator`, `display_name`, `category`, `data`, `metadata`, `has_changes`, `children`,
`fields`, `has_children`, `edited_on`, `published` y el grupo `video_sharing_*`.

🔵 **Consecuencia de cotización, en una línea:** generar un curso entero —esqueleto y contenido— es **un solo cliente de
un solo endpoint recorriendo un árbol**, más **una** llamada legacy para crear el curso. El gap 50 **no era un bloqueo
ni un desvío de versión**: era una pregunta mal planteada, porque suponía una ruta por nivel.

## 159. Los controladores *read-only* de SEB Server **conservan las rutas de escritura** y rechazan recién en el cuerpo: el descubrimiento de rutas no sirve para construir una allowlist (agregado en el pase 43 del 2026-10-02)

Medido en `webservice/weblayer/api/ReadonlyEntityController.java` sobre `master`:

```java
@Override
@RequestMapping(method = RequestMethod.PUT, ...)
public T savePut(@Valid @RequestBody final T modifyData) {
    throw new AccessDeniedException(ONLY_READ_ACCESS);
}
```

Las tres escrituras heredadas (`PUT`, `POST`, `DELETE`) están **sobrescritas conservando la anotación
`@RequestMapping`** y lanzando `AccessDeniedException("Only read requests available for this entity")`.

🔴 **Por qué es una trampa y no una curiosidad:** la ruta **existe y se anuncia**. Un generador de manifiesto MCP que lea
las anotaciones —que es la forma obvia de automatizarlo— **emite tools de escritura que parecen legítimas** sobre una
entidad que es de sólo lectura. El rechazo ocurre **en tiempo de ejecución, adentro del controlador**, no en la capa de
ruteo.

🔵 **La conclusión de diseño, y es la que justifica el patrón P85 en vez de sólo usarlo:** **la allowlist se construye por
NOMBRE, nunca por descubrimiento.** Es el segundo argumento independiente a favor de P85 que esta base encuentra.

**Y un segundo motivo, medido en el mismo pase:** `ExamAdministrationController` declara un **`PATCH`**, verbo que **no
existe** en la superficie CRUD de `EntityController`. Un manifiesto armado sólo con las **10** operaciones de la clase
base **se lo pierde en silencio**.

## 160. 🔴 `RemoteProctoringService` tiene **14 métodos obligatorios, no 12** — y la cifra que importa para cotizar no es la cantidad de métodos (agregado en el pase 43 del 2026-10-02)

**Primero la corrección.** **P91** dice, en la celda *«Métodos obligatorios»*: **«12 de 14»**. Son **14 de 14**, y hay
**tres** evidencias independientes del mismo árbol:

1. La interfaz **no tiene ningún `default` ni ningún `static`** — los 14 métodos son abstractos.
2. `JitsiProctoringService` y `ZoomProctoringService` **implementan `RemoteProctoringService` directamente**
   (`implements`, no `extends`): **no hay clase base intermedia** que pudiera aportar dos implementaciones gratis, que es
   la única forma en que «12 de 14» podría haber sido correcto.
3. `JitsiProctoringService` tiene **exactamente 14 `@Override`**, uno por método de la interfaz.

🔴 **Así que no hay dos métodos opcionales: hay que escribir los 14.** Los 14: `getType`, `testExamProctoring`, `getProctorRoomConnection`, `getClientRoomConnection`,
`createJoinInstructionAttributes`, `disposeServiceRoomsForExam`, `newCollectingRoom`, `newBreakOutRoom`,
`disposeBreakOutRoom`, `getDefaultReconfigInstructionAttributes`, `mapReconfigInstructionAttributes`,
`notifyBreakOutRoomOpened`, `notifyCollectingRoomOpened`, `clearRestTemplateCache`.

**Y ahora el número que el pase 42 pedía: el costo.** Las dos implementaciones de referencia, medidas método por método:

| | **Jitsi** | **Zoom** |
|---|---|---|
| Líneas de código de la clase (sin comentarios ni blancos) | **481** | **912** |
| Líneas dentro de los 14 métodos de la interfaz | **107** | **212** |
| **Porcentaje de la clase que son los 14 métodos** | 🔴 **22 %** | 🔴 **23 %** |
| Líneas **fuera** de la interfaz | **374** (77 %) | **700** (76 %) |
| Métodos privados de apoyo | 2 | **8** |
| Clases internas | 0 | 1 |
| Métodos que hablan con el servicio remoto | **1** (`testExamProctoring`) | **2** (`testExamProctoring`, `clearRestTemplateCache`) |
| Métodos triviales (≤6 líneas, sin red) | **10** de 14 | **6** de 14 |
| *Imports* de terceros | 17 | **38** |
| Criptografía obligatoria | **`Mac.getInstance` + `HmacSHA256` + `Base64`** | **idem** |

🔵 **La lección, que es la que corrige la forma de cotizar de esta base:** *«implementar una interfaz de 14 métodos»*
**subestima el trabajo por un factor de ~4,5**. Los 14 métodos son **22-23 %** de cada clase de referencia —y el
porcentaje es asombrosamente estable entre las dos, que no se parecen en nada—. El otro **77 %** es lo que nadie pone en
el presupuesto: *helpers*, DTOs, caché de `RestTemplate`, construcción de tokens.

🔴 **Y el dato que cambia el perfil de riesgo, no sólo el tamaño:** **las dos implementaciones firman tokens con
HMAC-SHA256 a mano.** La criptografía **no es opcional** en este puerto; es parte del contrato de los dos proveedores de
referencia. Eso **sube el nivel de revisión** que la propuesta tiene que presupuestar, porque un error ahí no es un bug
funcional.

**Que sólo 1 de 14 (Jitsi) hable con la red** parece abaratar, y no abarata: significa que **el resto es lógica de
dominio del proveedor** —ciclo de vida de salas, instrucciones de reconfiguración, mapeo de atributos—, que es
exactamente lo que no se puede copiar de la otra implementación.

## 161. 🟢 **Gap 90, CERRADO con código:** el validador de SEB Server acepta un proveedor de terceros con **todos** los campos vacíos, y el reemplazo está escrito y probado (agregado en el pase 43 del 2026-10-02)

`webservice/servicelayer/validation/ProctoringSettingsValidator.java` valida campos **sólo** si el `serverType` es
`JITSI_MEET` o `ZOOM`, y termina en **`return true`**. Como `ProctoringServerType` tiene hoy exactamente **dos** valores,
la rama parece inalcanzable. **Lo deja de ser en el momento exacto en que se integra un tercer proveedor**, que es el
único momento en que a alguien le importa.

🔵 **Esto ya no es una advertencia: es una pieza.** En
`compose/code/seb-proctoring-validator/` queda el reemplazo, y **la prueba corre con JDK puro, sin instalar ninguna
dependencia de terceros** (`./run_test.sh`, **21/21 checks**):

* **El defecto se reproduce por ejecución, no se afirma:** una copia fiel del validador actual recibe un settings de
  `BIGBLUEBUTTON` con **todos los campos en `null`**, devuelve **`true`** y levanta **cero** violaciones.
* El reemplazo lo **rechaza**, con las plantillas `proctoringSettings:serverURL:notNull` y
  `proctoringSettings:appSecret:notNull` — **las mismas plantillas de siempre**, así que las claves de UI e i18n no se
  tocan.
* **Trata el espacio en blanco como ausencia**, no como valor.
* Con un solo campo faltante levanta **una sola** violación, sobre ese campo.
* El settings completo se acepta **sin violaciones** y **sin** deshabilitar la violación por defecto.
* **Sin regresión** en `JITSI_MEET` ni en `ZOOM`, en los dos sentidos (completo acepta, incompleto rechaza con las cinco
  plantillas de Zoom).

🔴 **Y la parte que de verdad cierra el gap, que no es validar el proveedor nuevo:** el *fall-through* **falla cerrado**.
Un `serverType` no reconocido se rechaza con `proctoringSettings:serverType:typeNotSupported`. **Sin eso, el próximo
valor del enum reabre el agujero idéntico** — y la pieza valdría sólo para BigBlueButton en vez de para todos los
proveedores futuros.

⚠️ **El alcance, dicho sin ambigüedad:** valida **presencia** de campos, no **corrección**. Que el `serverURL` responda y
que el secreto sea aceptado lo verifica `testExamProctoring`, que es el único método de la interfaz que habla con el
servicio remoto (tendencia 160).

## 162. **Gap 86, CERRADO:** la capa de examen queda completa —horario **y** supervisión— con las dos puertas escritas y probadas (agregado en el pase 43 del 2026-10-02)

Con el *gateway* de `compose/code/sebserver-mcp-gate/` (ver **P93**), las dos capas institucionales de examen de esta KB
tienen puerta de agente permisiva:

| Capa | Proyecto | Licencia | Puerta |
|---|---|---|---|
| Horarios | UniTime | Apache-2.0 | `compose/code/unitime-mcp-gate/` (**P85**, 26 tools) |
| Supervisión | SEB Server | Apache-2.0 | `compose/code/sebserver-mcp-gate/` (**P93**, 79 tools, 36 expuestas) |

**Medido por ejecución** (`python3 test_gate.py`, **11/11 checks**, sin levantar SEB Server): **79** operaciones leídas
del árbol → **79** tools, **36** expuestas; las **37** escrituras de `/exam`, `/lms-setup`, `/useraccount` y
`/batch-action` responden **`-32601`**; las **11** tools de `/batch-action` quedan fuera **incluidas las lecturas**; y
**ninguna** llamada retenida llegó al *upstream* — afirmado sobre el contador del propio *stub*, no sobre el mensaje de
error.

⚠️ **El alcance, para que nadie lo lea como más de lo que es:** `operations.tsv` cubre **los cuatro endpoints que el
handoff del pase 42 nombró para verificación**, medidos controlador por controlador. Los **26** controladores concretos
restantes (**30** en total, más **3** bases abstractas) **no** están en la tabla, y la tendencia 159 es justamente la
razón por la que **no se pueden adivinar** por el nombre del endpoint.

🔴 **Dos correcciones de conteo del mismo árbol, porque esta base tenía otras cifras:** las constantes `*_ENDPOINT` de
`gbl/api/API.java` son **42** en `master` (y **47** en `development`), no 41; y los controladores son **30 concretos + 3
bases = 33**, no 36. La rama por defecto de `seb-server` es **`master`**, verificada con `git ls-remote --symref`.

**Y una colisión de rutas que un generador ingenuo colapsa:** `EXAM_ADMINISTRATION_ENDPOINT` y
`LMS_FULL_INTEGRATION_EXAM_ENDPOINT` **valen las dos `/exam`**. Un manifiesto indexado por **path** los une; uno indexado
por **constante y controlador** no.

## 163. La premisa de que «los SDK previos de Caliper siguen publicados» es **falsa**, y la respuesta ya estaba en esta base: el fork LGPL de Michigan (agregado en el pase 43 del 2026-10-02)

El handoff del pase 42 mandó re-medir Caliper dando por bueno que, aunque **el estándar dejó de ser open source el
2023-06-17**, *«los SDK previos siguen publicados»*. **Medido, es falso para el canal público:**

* `IMSGlobal/caliper-php` → **404** en `raw.githubusercontent.com`, en `master` **y** en `main`. Igual bajo
  `1EdTech/caliper-php`.
* 1EdTech lo confirma por su lado: los repos de **Sensor API** son **para miembros *Contributing* y *Affiliate*** con
  acceso solicitado — que es lo que esta base **ya tenía registrado** para `caliper-java`, `caliper-js` y
  `caliper-python` desde el pase que leyó el aviso textual del repo (*«1EdTech will be moving Caliper to private
  repositories on June 17, 2023»*).

⚠️ **La asimetría del registro, otra vez** (tendencia 127): el paquete **sí** figura en Packagist (`imsglobal/caliper`).
**El registro confirma el nombre y no entrega el código.**

🟢 **Y lo que convierte esto en algo más que una confirmación: la respuesta ya estaba en esta KB.** La implementación PHP
de Caliper que **sigue siendo legible** es el fork de la **Universidad de Michigan**,
`tl-its-umich-edu/caliper-php-public` — ⚠️ **LGPL-3.0**, registrado en `agents/top.md` desde el **pase 9**. 🔵 **La lección
de método es sobre esta base, no sobre Caliper:** el handoff pidió buscar afuera algo que la propia KB ya tenía resuelto
adentro. **Antes de un barrido externo, conviene consultar la base.**

🔴 **Consecuencia de cotización, sin cambio de signo pero con el camino nombrado:** instrumentar Caliper **no** se cotiza
contra el repo oficial. Se cotiza **contra el fork LGPL-3.0** —con la restricción de copyleft débil que eso impone—,
contra la especificación, o afiliando al cliente a 1EdTech. Sigue **trasladando costo al integrador** en las cuatro
regiones.

**Y la colisión de nombre, la séptima de esta KB:** `llnl/Caliper` (instrumentación y *profiling* de performance) y
`google/caliper` (microbenchmarking de Java, **deprecado**) ganan la búsqueda. **Ninguno** tiene que ver con analítica de
aprendizaje.

## 164. El barrido por SDK confirma la ausencia de MCP en la capa de estándares, ahora **por el canal correcto** — y devuelve **una sola alta real**, no cinco (agregado en el pase 43 del 2026-10-02)

El handoff del pase 42 pedía re-medir por SDK las ausencias que esta base había declarado **por etiqueta**, porque el
método de etiqueta no prueba nada. Hecho, leyendo el **README crudo** de cada pieza y contando menciones de `MCP` /
*model context protocol*:

| Pieza | Licencia (del archivo `LICENSE`) | Menciones de MCP en el README |
|---|---|---|
| `Cvmcosta/ltijs` | **Apache-2.0** ✅ | **0** |
| `Simon-Initiative/lti_1p3` | **MIT** ✅ | **0** |
| `opensalt/opensalt` | **MIT** ✅ | **0** |
| `1EdTech/digital-credentials-public-validator` | **Apache-2.0** ✅ | **0** |
| `luisgf/openbadgeslib` | 🔴 **LGPL-3.0** | **0** |

🟢 **El gap 42 queda cerrado por una vía que sí lo examinó**, no por agotamiento de etiquetas: ninguna de las cinco
bibliotecas de estándares expone MCP. **CaSS sigue siendo la única pieza de estándar educativo de esta base con puerta
nativa de agente.**

🔴 **Y el dato que hay que escribir aunque incomode: de las cinco piezas, esta base ya tenía cuatro.** `opensalt`
(pase 14), `digital-credentials-public-validator`, `openbadgeslib` y `ltijs` estaban todas registradas. **La única alta
real del barrido es `Simon-Initiative/lti_1p3`** (MIT, Elixir, **Platform y Tool**, no sólo Tool). Las otras entran como
**confirmaciones con dato nuevo**, no como altas — ver `repos/foundations.md`. 🔵 **Eso no es un barrido fallido: es la
señal de que la capa de estándares de esta KB está saturada**, y de que las altas siguen viniendo del canal de conector,
no del de biblioteca.

⚠️ **Y la trampa de fork que la tendencia 132 anticipó, aparecida otra vez en el mismo barrido:** la búsqueda devolvió
**`kristofb/ltijs`** antes que el canónico. El canónico es **`Cvmcosta/ltijs`** —es el que la documentación del propio
proyecto referencia— y es el que se midió.

## 166. 🔴 Un servicio puede no tener **ni una** ruta base literal, y entonces una tabla de rutas no es una tabla de URLs (agregado en el pase 44 del 2026-10-02)

Esta base publicó durante dos pases una tabla con `/exam`, `/lms-setup`, `/useraccount`, `/batch-action`. **Ninguna de
las cuatro es una URL de SEB Server.** Los 30 controladores mapeados del paquete `weblayer/api` cuelgan todos de una
propiedad de Spring:

* **27** de `"${sebserver.webservice.api.admin.endpoint}" + API.X_ENDPOINT`
* **3** de `${…api.exam.endpoint.discovery}`, `${…api.exam.endpoint.v1}` y `${…lms.api.endpoint}`
* **0** de una cadena literal

Los valores vienen en `src/main/resources` del propio repo: `admin` = **`/admin-api/v1`**, `exam` = **`/exam-api`**,
`lms` = **`/lms-api/v1`**. Así que `/exam` **es `/admin-api/v1/exam`**, y una puerta que proxea el sufijo medido
**da 404 en el 100 % de las llamadas** — sin un solo error en el código de la puerta.

🔵 **La regla que queda, y es generalizable más allá de SEB Server:** cuando se mide la superficie de un servicio Java
o Spring para proponérsela a un cliente, **el mapeo de clase hay que resolverlo, no leerlo**. Un `@RequestMapping` que
empieza con `"${` no es una ruta: es una variable, y su valor vive en otro archivo del mismo repo. **El control barato
es una aserción: ninguna ruta de la tabla puede contener `${`, y ninguna puede dejar de empezar con `/`.** Las dos están
ahora en `test_gate.py`.

## 167. 🔴 Una constante **compuesta** es invisible a un extractor de literales, y lo que se pierde es la superficie de autenticación (agregado en el pase 44 del 2026-10-02)

`gbl/api/API.java` define **55** constantes `*_ENDPOINT`. El pase 43 registró **42** (41 de ellas constantes reales más
una que no es `*_ENDPOINT`). La causa está medida y es determinista: **41 están definidas como literal** (`= "/exam"`) y
**14 como composición** (`= OTRO_ENDPOINT + "/sufijo"`). Un extractor que casa `String X = "…"` ve las 41 y **pierde las
14 — 14 de 14, sin una excepción**.

Lo perdido no es aleatorio, y ahí está el riesgo:

| Constante compuesta ausente | Resuelve a |
|---|---|
| `OAUTH_TOKEN_ENDPOINT` | `/oauth/token` |
| `OAUTH_REVOKE_TOKEN_ENDPOINT` | `/oauth/revoke-token` |
| `OAUTH_JWT_TOKEN_ENDPOINT` | `/oauth/jwttoken` |
| `OAUTH_JWT_TOKEN_VERIFY_ENDPOINT` | `/oauth/jwttoken/verify` |
| `SPS_OAUTH_JWT_TOKEN_ENDPOINT` | `/oauth/jwttoken` |
| `EXAM_PROCTORING_ENDPOINT` | `/monitoring/proctoring` |
| `SEB_SETTINGS_ENDPOINT` | `/exam/seb-settings` |
| `VIEW_ENDPOINT` | `/orientation/view` |
| `PRIVILEGES_ENDPOINT` | `/info/privileges` |
| `CURRENT_USER_ENDPOINT` | `/useraccount/me` |

**La superficie de autenticación completa estaba afuera**, y con ella `/monitoring/proctoring` —la capa que esta base
nombra como alto riesgo bajo **dos** reguladores (Anexo III punto 3 de la UE y los seis sectores de Vietnam)—. Una
allowlist construida sobre la tabla de 42 **nunca consideró los endpoints de token**: no los negaba, es que no sabía que
existían. Ahora los cinco de OAuth están en la tabla y `/oauth/jwttoken/verify` —el único con controlador en este
paquete, `AdminJWTAccess`— está en `DENY_ENDPOINTS` por nombre.

⚠️ **Y el matiz que evita sobrevender el hallazgo:** de las cinco constantes de OAuth, **sólo una tiene controlador
aquí**; las otras cuatro las sirve la configuración de Spring Security, fuera de `weblayer/api`. La tabla de operaciones
tiene por eso **una** fila de OAuth, no cinco. **Estar en el inventario de endpoints y estar servido por un controlador
son dos cosas distintas**, y confundirlas es el error simétrico al que este hallazgo corrige.

## 168. 🔴 El extractor contaba la **declaración de clase** como una operación: cada controlador venía inflado en una fila fantasma (agregado en el pase 44 del 2026-10-02)

El patrón del pase 43 buscaba un `@RequestMapping` seguido de `public|protected|private`. En Java eso casa también
`@RequestMapping(…)` + `public class Foo … {`, que es **el mapeo de la clase**, no una operación. Resultado: **todo
controlador con mapeo de clase sumaba exactamente una fila que no existe**.

El caso que lo prueba sin ambigüedad es `BatchActionController`: la tabla vieja le daba **`1 own`** y el archivo
**no declara ninguna** operación propia — su único `@RequestMapping` es el de la clase (línea 31). Lo mismo explica las
otras diferencias: `/exam` pasa de 22 a **21** operaciones propias, `/useraccount` de 7 a **6**.

🔵 **El discriminador, que es barato: una operación tiene tipo de retorno.** `public class Foo` no lo tiene; `public
EntityProcessingReport hardDelete(` sí. El patrón nuevo exige `(public|protected) <tipo> <nombre>(` y por construcción
**no puede** casar una declaración de clase. 🔴 **Y la primera versión del patrón nuevo tenía su propio defecto, del
mismo tamaño y en la dirección contraria: excluía el punto del juego de caracteres del tipo de retorno**, así que
perdía los métodos con tipo cualificado y la cuenta daba **129 `own` en vez de 135**. Se detectó porque las cuatro filas
viejas y las nuevas tenían que coincidir salvo por los fantasmas — **un control de regresión contra la medición
anterior, aunque la anterior sea la que se está corrigiendo**.

## 169. 🔵 Un controlador «sólo lectura» niega 4 de 5 escrituras en la ruta; la quinta queda viva y se frena una capa más abajo (agregado en el pase 44 del 2026-10-02)

`EntityController` expone cinco escrituras. `ReadonlyEntityController` sobrescribe **cuatro** —`savePut` (`PUT /`),
`create` (`POST /`), `hardDelete` (`DELETE /{id}`), `hardDeleteAll` (`DELETE /`)— y lanza `AccessDeniedException` en el
cuerpo, conservando el `@RequestMapping`. **No sobrescribe `forceHardDelete`**, así que **`DELETE /{id}/force` queda viva
y entra al cuerpo heredado de la superclase.**

Sigue negada, y el mecanismo es el dato: ese cuerpo hace `.flatMap(this::checkWriteAccess)`, y `checkWriteAccess`
**está** sobrescrito para lanzar `PermissionDeniedException`. O sea:

* **4 rutas** se niegan **en la ruta** (el cuerpo tira de entrada, sin tocar el modelo),
* **1 ruta** se niega **en el guardia** (corre el cuerpo heredado y lo detiene un override de la superclase).

**Para cotizar importa porque las dos clases se rompen distinto.** Las cuatro primeras siguen negadas aunque alguien
cambie `checkWriteAccess`; la quinta depende de que ese override siga ahí. La tabla distingue las clases
(`inherited-denied`, 16 filas = 4 controladores × 4, contra `inherited-guarded`, 4 filas) y la puerta retiene ambas
**sea cual sea la política de lectura/escritura**, no sólo cuando `read_only=True`.

🔵 **Y queda medido qué significa «force» en este código, que no es lo que el nombre sugiere:** `hardDelete` corre
`checkWriteAccess` **y** `validForDelete`; `forceHardDelete` corre `checkWriteAccess` y **saltea `validForDelete`**.
**Evita la validación referencial, no la autorización.** Un generador que lea el nombre y asuma «force = sin permisos»
se equivoca en los dos sentidos a la vez.

## 170. 🔴 Una ruta en el árbol no es una ruta en ejecución: el `@ConditionalOn*` decide, y el valor por omisión puede ser «no existe» (agregado en el pase 44 del 2026-10-02)

`LightController` tiene `@RestController`, mapeo de clase y dos `@RequestMapping` propios. Un generador que lea
anotaciones emite sus dos tools. Pero el archivo también tiene:

```java
@ConditionalOnExpression("'${sebserver.webservice.light.setup}'.equals('true')")
```

y `src/main/resources` de seb-server envía **`sebserver.webservice.light.setup=false`**. **Las dos rutas existen en el
fuente y no existen en un despliegue por omisión.**

🔵 **La regla: las anotaciones de ruta dicen qué PUEDE existir; las de condición dicen qué existe.** Hay que leer las dos
o se proponen tools que dan 404 en producción — y es el peor 404, porque el código que lo justifica está en el repo y
parece correcto. La tabla lleva ahora una columna `condition`, la puerta excluye del allowlist por omisión toda fila
condicionada, y `test_gate.py` lo asevera.

⚠️ **Nota de alcance honesta: este pase midió el conditional de clase, no el de método.** Spring admite
`@ConditionalOn*` también sobre `@Bean`, y propiedades que apagan funcionalidad sin apagar la ruta. Lo que se afirma es
lo medido: **un controlador condicionado, `LightController`, y su valor por omisión `false`**.

## 171. ✅ El `locator` que devuelve la creación de un xblock **es** el usage key: el árbol de Open edX es recursable sin un GET extra (agregado en el pase 44 del 2026-10-02)

La pregunta de la acción 2 era si `create_xblock_response` devuelve lo que hace recursable el recorrido. **Lo devuelve.**
`view_handlers.py:894` arma:

```python
response = {"locator": str(created_block.location), "courseKey": str(created_block.location.course_key)}
```

`created_block.location` es el `UsageKey` del bloque nuevo, y `parent_locator` del POST siguiente **toma exactamente ese
string**. Así que generar un curso entero es **1 POST por bloque y ninguna lectura intermedia**: secuencial bajando una
rama (el hijo necesita el `locator` del padre), **paralelizable entre hermanos**.

Las variantes del cuerpo, medidas en el mismo archivo: *paste* de clipboard agrega `static_file_notices` y `upstreamRef`
(4 claves); import de biblioteca v2 agrega `upstreamRef`, `static_file_notices` y `parent_locator` (5); el camino de
duplicado devuelve las mismas 2. **En ningún caso devuelve el `XBlockInfo` completo** — y no hace falta.

🔵 **Y sobre `category`, la respuesta es que casi no hay contrato, lo cual es a la vez la facilidad y el riesgo:**
`XblockSerializer.category` es un `CharField(required=False, allow_null=True)` **sin `choices`**, así que el serializer
no valida el tipo de bloque; se resuelve en runtime contra los *entry points* de XBlock instalados. **El único enum del
árbol** es `["html", "problem", "video"]`, y sólo cuando el padre es un `LibraryUsageLocator`
(`view_handlers.py:867`). `chapter` y `sequential` tienen trato especial bajo el toggle `ENTRANCE_EXAMS`.

⚠️ **Defecto de validación que conviene saber antes de escribir el cliente:** el serializer declara `category`
**opcional**, pero `_create_block_core` hace `request.json["category"]`. Un POST sin `category` (y sin
`staged_content="clipboard"`) **levanta `KeyError` → 500, no 400**. La validación no te lo dice: el 500 sí.

## 172. 🔴 `?view=minimal` poda un árbol que no viene: el docstring del `v1` llama «tree-shaped» a una respuesta de un solo bloque (agregado en el pase 44 del 2026-10-02)

La tercera pregunta de la acción 2 era si `?view=minimal` está sólo en `retrieve` o también al recorrer `children`.
**Está sólo en `retrieve`** —es la única acción que llama `_apply_minimal_view`, y el comentario del parámetro OpenAPI lo
dice— **pero la pregunta tenía la premisa invertida: no hay `children` que recorrer.**

`retrieve_xblock_response` llama `get_block_info`, y `get_block_info` lleva escrito (`view_handlers.py:710`):

```python
# Note that children aren't being returned until we have a use case.
```

y nunca pasa `include_child_info`. **La respuesta del `v1` es un bloque, no un árbol**, así que el docstring del propio
`v1` —*«Retrieve an xblock (and, by default, its nested tree)»*— **es falso para este endpoint**.

Tres consecuencias concretas, todas verificables sin levantar nada:

1. `_MINIMAL_VIEW_FIELDS` promete `{id, display_name, category, children, has_children, studio_url}` y
   `_apply_minimal_view` es un `project()` **de primer nivel**. Como `children` y `has_children` no están en el cuerpo,
   **la vista mínima devuelve a lo sumo 4 de los 6 campos que documenta.**
2. **La única manera de sacar hijos de este endpoint es una combinación no documentada:**
   `?fields=customReadToken&view=minimal`. Da `children` como identificadores `{block_type, block_id}` —**un nivel**— y
   **descarta `parent` en silencio**, porque `parent` no figura en `_MINIMAL_VIEW_FIELDS`.
3. 🟢 **El instrumento correcto para el árbol es otro endpoint**, y encontrarlo es lo que fija el costo de **P55**:
   `GET /api/contentstore/v1/course_index/{course_id}` devuelve **`course_structure`**, el outline anidado, **en una
   llamada**; `GET /api/contentstore/v1/container/{usage_key}/children` devuelve **un nivel** con nombre y tipo.

🔵 **La lección de método, que es la que vale más allá de Open edX: el docstring y el `OpenApiParameter` describen la
intención; el handler describe el producto.** Las dos estaban en el mismo archivo y se contradecían, y la que gana es la
que corre. Es la misma clase de error que el pase 29 encontró con la deprecación circular del `v0`, ahora en la
dirección opuesta: antes el aviso desactualizado escondía una capacidad real, acá el docstring promete una que no está.

## 173. 🟢 El plazo del AI Act que de verdad aprieta no es 2027: el Artículo 50(2) vence el 2026-12-02 y no se prorrogó (agregado en el pase 44 del 2026-10-02)

Esta base lleva varios pases planificando contra el **2027-12-02** (Anexo III, alto riesgo autónomo, donde educación
está nombrada). La fecha es correcta y este pase la confirma. **Pero no es la primera que vence**, y la que vence antes
cae exactamente sobre el producto que un estudio de AI entrega:

| Obligación | Fecha | Estado |
|---|---|---|
| Art. 50(1), 50(3), 50(4) — transparencia | **2026-08-02** | **en vigor**, sin prórroga |
| **Art. 50(2) — marcado legible por máquina** | **2026-12-02** | **vence en 61 días**; ventana transitoria de 4 meses para los sistemas generativos **ya en el mercado antes del 2026-08-02** |
| Anexo III — alto riesgo autónomo (educación) | **2027-12-02** | diferido por el Reglamento (UE) 2026/1744 |
| Anexo I — alto riesgo embebido en producto regulado | **2028-08-02** | diferido |

**El 50(2) es el que muerde ya**, y por dos razones: aplica a **lo que ya está desplegado** —no a lo nuevo— y el
remedio es *retrofit* de marcado en sistemas en producción, que es trabajo de ingeniería con fecha, no un expediente.
Un tutor generativo entregado antes de agosto entra de lleno.

✅ **Y está confirmado que no se movió:** el **9.º plenario del Consejo Europeo de IA (2026-09-17)** trató coordinación
de supervisión y pruebas de ciberseguridad de modelos frontera **sin fijar fecha nueva ni conceder alivio** sobre el
marcado. El Digital Omnibus que diferió el Anexo III **dejó el Artículo 50 intacto**.

🔵 **Para la propuesta, la consecuencia es de orden: el entregable de cumplimiento más cercano no es el expediente de
alto riesgo, es el marcado.** Y conviene decirlo antes de que lo diga el cliente, porque la fecha ya está dentro del
trimestre.

## 174. 🔴 La quinta variante de primitiva anti-bucle delega el freno en la API del proveedor — y el valor por omisión lo anula (agregado en el pase 44 del 2026-10-02)

Esta base viene catalogando cómo cada pieza frena a un agente en bucle: **en el servidor** (`openedx-mcp`, *confirm
token* atado a una huella del payload), **en el contrato** (`coursecode`, anotaciones MCP + `dryRun`), **en la
configuración** (`learnmcp-xapi`, `RATE_LIMIT_PER_MINUTE`) y **anclando la procedencia** (`qti3-cli`,
`--trusted-report-sha256`). `issuebadge/mcp-server` aporta la quinta, y es la más débil de las cinco:
**`idempotency_key`, cuyo cumplimiento vive en la API del proveedor.**

La descripción de la tool lo dice con todas las letras: *«a reused key is rejected by the API»*. **El freno no está en el
código que se auto-hospeda**, y el README ofrece auto-hospedar el worker — así que un despliegue propio **hereda la forma
de la protección sin la protección**.

🔴 **Y hay un defecto peor, en el valor por omisión.** `src/issuebadge.ts:117`:

```javascript
const idempotency_key = input.idempotency_key || `mcp-${crypto.randomUUID()}`;
```

La clave se genera **por llamada**. Un agente que reintente `issue_badge` sin arrastrar la clave del intento anterior
obtiene un UUID nuevo y **emite un segundo certificado**. La tool **devuelve** la clave en su `outputSchema` (está en
`required`), así que la información para reintentar bien se entrega — **y no se recuerda**. La protección es cooperativa
con el cliente, y **el camino por omisión es la doble emisión**.

Para emisión de credenciales eso no es cosmético: el producto es un certificado que se manda por mail al alumno con URL
pública de verificación. Dos llamadas idénticas = dos certificados = dos URLs válidas para el mismo logro.

🔵 **Lo que se adopta es la primitiva corregida, no la pieza:** la idempotencia es **la** forma correcta de frenar un
reintento en una operación que crea algo irreversible hacia afuera, y las otras cuatro variantes de esta base no la
tienen. Pero hay que **derivarla del contenido** (`hash(badge_id + recipient + logro)`), no de un UUID por llamada, y
hay que **hacerla cumplir del lado que uno controla**. Ver **P97**.

## 165. Apareció la primera puerta MCP de **emisión de credenciales**, y no sirve para el camino de estándar: la puerta es a una **API de proveedor** (agregado en el pase 43 del 2026-10-02)

`issuebadge/mcp-server` es **MIT** (*Copyright (c) 2025-2026 IssueBadge*), TypeScript, y expone **4 tools**:
`validate_key`, `get_all_badges`, `issue_badge` y —sólo en modo local/stdio— `create_badge`. Corre como **HTTP remoto**
(`streamable-http`, con OAuth 2.1 además de API key, para *hosts* que no pueden mandar cabecera) o por **stdio**
(`npx issuebadge-mcp-server`); es además **plugin de Claude Code** con una *skill* que enseña el flujo
*listar → confirmar → emitir*, y el servidor remoto es **auto-hospedable**. `issue_badge` trae un **widget MCP Apps**
(`ui://widget/certificate.html`).

🔴 **Y ahora lo que lo descalifica para el patrón P84, dicho sin vueltas:** el código es MIT, pero **la emisión depende de
`app.issuebadge.com` y de una API key del proveedor**. No implementa **Open Badges 3.0** como estándar: emite
«certificados y credenciales verificables» **del producto**. 🔵 **La distinción que esta base necesita mantener:** existe
la capa MCP de credenciales, **no** existe la capa MCP de credenciales *conforme al estándar y sin proveedor*. Para
**P84** —cerrar el curso emitiendo un Open Badges 3.0 **firmado**— esta pieza **no sustituye** nada.

⚠️ **Y la madurez, con el número a la vista: 0 ★ y 4 commits.** **No entra a la tabla de `agents/top.md`** por eso, y se
registra acá con la cifra visible para que el próximo pase la vuelva a medir en vez de heredar un juicio.

## 175. 🔴 `getName()` no es la ruta: en UniTime enruta el nombre del bean de Spring, y una puerta construida sobre el otro campo acierta por coincidencia (agregado en el pase 45 del 2026-10-02)

`ApiServlet.getConnector()` de `UniTime/unitime` (Apache-2.0, `HEAD` `aeb4431` del 2026-10-02) hace:

```java
protected String getReference(HttpServletRequest request) {
    return request.getServletPath() + request.getPathInfo();
}
protected ApiConnector getConnector(HttpServletRequest request) {
    return (ApiConnector) applicationContext.getBean(getReference(request));
}
```

**La ruta es el nombre del bean.** Los 15 conectores lo declaran con `@Service("/api/rooms")`, y
`ApiConnector.getName()` —el campo que esta base venía publicando como ruta— **no participa del enrutado**: su único uso
es `getCacheMode()`, que lo pasa a `ApplicationProperty.ApiCacheMode.value(getName())`.

🔵 **Los 15 coinciden hoy** (`@Service` vale exactamente `/api/` + `getName()` en **15 de 15**), **así que el dato
publicado era correcto y el método no.** Esa es la forma del defecto que importa: una puerta construida sobre el campo
equivocado **acierta por coincidencia** y se rompe **en silencio** el día que un conector registre un bean con otro
nombre. Es la misma clase que el defecto del pase 44 en SEB Server —**la ruta inferida en vez de leída**— con el signo
invertido: allá la inferencia daba 404 en el 100 % de las llamadas, acá da el resultado correcto y **no se puede
distinguir de la suerte**.

🔴 **Y la ruta absoluta tampoco era la URL.** `getServletPath()` es relativo al contexto del *webapp*. El
`<url-pattern>` de `apiServlet` en `WebContent/WEB-INF/web.xml` es **`/api/*`** y `pom.xml:614` envía
**`<warName>UniTime</warName>`**, así que la URL desplegada por omisión es **`/UniTime/api/<conector>`**. La puerta
publicaba `/api/<conector>` **pegado en una f-string de Python**, no leído de ninguna parte.

**La regla de método que deja esta tendencia, y es hermana de la del pase 44:** cuando una pieza enruta por un
mecanismo de *framework* (bean de Spring, `@RequestMapping` con propiedad, `url-pattern` de servlet), **la ruta hay que
leerla del mecanismo que la resuelve, no del campo que se le parece.** Y la prueba tiene que **aseverar la ruta como
dato**: desde este pase `load_connectors()` **levanta `StaleTable`** si recibe una tabla sin columna de ruta, en vez de
volver a inferir.

## 176. 🔴 El verbo HTTP no es la frontera de escritura: un GET que despacha por parámetro de query ejecuta un script del servidor (agregado en el pase 45 del 2026-10-02)

Ésta es la quinta clase de defecto de las puertas de esta base, y es la primera que **no es del extractor: es de la
abstracción**. `ScriptConnector.doGet` de UniTime despacha por **parámetro de query**, y dos de sus ramas escriben:

```java
} else if (helper.getParameter("delete") != null) {
    Boolean ret = solverServerService.getQueueProcessor().remove(helper.getParameter("delete"));
} else if (helper.getParameter("script") != null) {
    doPost(helper);
}
```

**`GET /UniTime/api/script?script=…` ejecuta un script del servidor** y **`?delete=…` borra un ítem de la cola**, las
dos detrás del mismo `checkPermission(Right.Scripts)` del encabezado del método.

🔴 **La consecuencia alcanza a las DOS puertas de esta KB:** la política *«exponer sólo lecturas»* —que es el corazón de
**P85**, **P92** y del *gateway* de SEB Server— **presupone que el verbo es la frontera**. Para UniTime no lo es. La
política por defecto ya negaba `script` **por nombre**, así que **el resultado era correcto y el motivo documentado no
lo era**: decía *«se niega porque ejecuta scripts»* cuando lo que corresponde decir es *«se niega porque su GET es una
escritura, y por lo tanto ninguna allowlist de lectura/escritura puede protegerlo»*.

🟢 **Lo que se adopta, y es la corrección de diseño:** el rechazo pasa de **política** a **piso**. `hard_deny()` niega
el tool con `-32601` **incluso si un operador lo nombra explícitamente en `UNITIME_ALLOW`**, y la decisión se registra
como `floor` y no como `withheld`, para que el log distinga *«la política no lo abrió»* de *«no se puede abrir»*.
Aseverado por ejecución, in-process y por **stdio real**. Ver **P100**.

⚠️ **Barrido completo, para que no quede como impresión:** se revisaron **los 15 `doGet`** del paquete buscando
mutaciones. El único cruce real es `ScriptConnector`; `EventsConnector:170` casa el patrón y **es un falso positivo**
(`Iterator.remove()` sobre una lista en memoria, no estado persistido).

## 177. 🔵 Una ruta sin *override* no devuelve 404: la clase base responde 501, así que la superficie HTTP es 2,3× la superficie implementada (agregado en el pase 45 del 2026-10-02)

`ApiConnector` implementa **los cuatro** `do<Verb>(ApiHelper)` con `helper.sendError(SC_NOT_IMPLEMENTED)`. Entonces en
UniTime hay **15 conectores × 4 verbos = 60 rutas HTTP vivas**, de las cuales **26 están implementadas** y las otras
**34 responden 501**, no 404.

🔵 **Por qué esto es información y no trivia:** un inventario de superficie que cuenta *handlers* mide **26** y un
escáner que prueba verbos mide **60**. Las dos cifras son correctas y responden preguntas distintas —*«qué puedo
usar»* contra *«qué está publicado»*— y mezclarlas es lo que hace que un informe de superficie no cuadre con el de
nadie más. El manifiesto de la puerta expone **26** (no hay nada que ofrecer detrás de un 501), y la tabla registra
**60** para que el dato de encuadre exista.

⚠️ **Y el análogo del `LightController` del pase 44 existe acá, condicionando una LECTURA.**
`VariableTitleCourseConnector.validateRequest()` —llamado por `doGet` **y** por `doPost`— lanza
`IllegalArgumentException` si `VariableTitleConfigName`, `VariableTitleDefaultLimit` o
`VariableTitleInstructionalType` no están seteadas. Así que **`GET /UniTime/api/var-title-crs` devuelve 400 en un
despliegue por omisión**. 🔵 **La lección de método: UniTime no condiciona el bean, condiciona el handler**, así que el
control *«toda clase condicionada está excluida»* del pase 44 **pasa y no alcanza** — hay que buscar el guarda **dentro
del método y en los que llama**, que es lo que mide la columna `guarded` del extractor nuevo.

## 178. 🔴 Tres estatus para un mismo defecto, y sólo uno es el correcto: el 403 de Open edX es un error de payload disfrazado de credenciales (agregado en el pase 45 del 2026-10-02)

Medido leyendo `openedx/edx-platform` sobre `master`. Un cuerpo mal formado en
`POST /api/contentstore/v1/xblock/` se reporta de **tres** maneras:

| Cuerpo | Estatus | Mecanismo, con el sitio exacto |
|---|---|---|
| sin `parent_locator` | 🔴 **403** | `XblockViewSet.initial()` deriva `course_key` **del cuerpo crudo**; si falta queda `None`, y `HasCourseAuthorAccess.has_permission` hace `if not course_key: return False` (`rest_api/v1/views/permissions.py:25-27`) |
| sin `category` | 🔴 **500** | el serializer declara **todos** sus campos `required=False`, así que valida; después `_create_block_core` hace el subscript pelado `request.json["category"]` (`view_handlers.py:864`) |
| con una clave de más | 🟢 **400** | `XblockSerializer` extiende `StrictSerializer`, que lanza `ValidationError` por clave inesperada (`rest_api/serializers/common.py:40-49`) |

🔴 **El 403 es el peligroso**, y no por severidad sino por **diagnóstico**: manda al operador a revisar credenciales,
JWT y permisos de autoría cuando el problema es **una clave ausente en el JSON**. En un *engagement*, eso es una tarde.

🔵 **Precisión que afina el hallazgo: `category` se lee DOS veces** — `request.json.get("category")` en la línea 834,
que alimenta el chequeo de permisos, y el **subscript pelado** en la 864. Así que un POST sin `category` **pasa el
control de autorización** y revienta después. Y **`parent_locator` también es un subscript pelado** (línea 832), pero
**no llega a ejecutarse**: el 403 del `permission_class` lo frena antes.

🟢 **Y una corrección a favor del upstream, porque la lectura fácil es injusta:** el `create` del `v1` **sí** corre el
serializer — lleva `@validate_request_with_serializer` además de `@expect_json_in_class_view`
(`rest_api/v1/views/xblock.py:239-243`). **El serializer se ejecuta y es estricto con las claves de más.** Lo que no
puede hacer es atrapar las dos claves que el handler exige, **porque las declara opcionales a las dos**. El defecto no
es *«no valida»*: es **que la declaración del contrato y el uso del contrato discrepan en dos campos.**

**La consecuencia de diseño:** un cliente generador tiene que validar `parent_locator`, `category`, el orden de niveles
y la lista blanca de campos **antes de emitir**. No es defensa en profundidad — es que **dos de los tres estatus del
servidor son diagnósticos falsos**. Ver **P55** y `compose/code/openedx-course-generator/`.

## 179. 🟢 El costo de generar un curso tiene fórmula, y es cotizable sin levantar la plataforma (agregado en el pase 45 del 2026-10-02)

Tres hechos medidos, y los tres juntos dan la fórmula:

1. El POST devuelve **`{"locator", "courseKey"}`** y `locator` **es el usage key del bloque nuevo**
   (`view_handlers.py:895-897`), así que el recorrido del árbol es **recursable sin un GET extra**.
2. Leer el curso entero es **UNA llamada**: `GET /api/contentstore/v1/course_index/{course_id}` devuelve
   `course_structure`, el *outline* anidado (`rest_api/v1/urls.py:82-84`).
3. Un hijo necesita el `locator` de su padre; **los hermanos no dependen entre sí.**

🟢 **La fórmula: `llamadas = 1 + bloques`, en `profundidad` olas secuenciales, con los hermanos paralelizables dentro de
cada ola.** Para un curso de 2 módulos / 3 secuencias / 4 verticales / 8 componentes = **17 bloques**: **18 llamadas, 4
olas, ola más ancha de 8.**

🔵 **Por qué esto es el entregable y no la observación:** *«generar un curso en Open edX»* era hasta este pase una
promesa de **P55** sin número. Ahora es un artefacto con **33 aserciones en verde** que asevera, contra un *stub* que
reproduce los **cuatro** comportamientos reales del endpoint (400/403/500/200), que **ningún POST se emite antes de
tener el `locator` de su padre**, que **los hermanos se agrupan en olas** y que **un cuerpo que el servidor
mal-reportaría se rechaza en el cliente**. Eso es lo que entra en una propuesta: no *«se puede»*, sino **«18 llamadas,
4 olas»**.

⚠️ **Y el límite declarado:** `category` **no se puede validar contra los XBlocks instalados**, porque **el servidor
tampoco lo hace** — `XblockSerializer.category` es un `CharField(required=False)` **sin `choices`**, y el único enum del
árbol (`["html","problem","video"]`) aplica **sólo** si el padre es un `LibraryUsageLocator`. La lista de categorías
hoja del generador es **una convención de esta KB**, declarada como tal.

## 180. 🔴 El 48 % de las piezas de esta KB pone contenido sintético delante de una persona, y 0 de 33 puede marcarlo (agregado en el pase 45 del 2026-10-02)

Clasificadas las **66** filas de `agents/top.md` por una sola pregunta —**¿genera contenido sintético que un alumno o un
docente va a ver?**—: **24 `gen` + 7 `gen-ind` + 1 `gen-cond` = 32 filas, el 48 %**, más **1 `pack`**
(`scorm-mcp-server`, que no genera pero es **donde el contenido generado se vuelve el curso que el alumno abre**) y
**33 `no`**.

Barridos los **33** repos expuestos con `--filter=blob:none` —**ningún blob se descarga**— y leídos sus manifiestos de
raíz:

| Magnitud | Valor |
|---|---|
| Archivos listados | **24.202** |
| Artefactos de marcado (`c2pa`, `watermark`, `synthid`, `content-credentials`, `imwatermark`) | 🔴 **0** |
| Manifiestos de raíz leídos | **26** |
| Dependencias de marcado | 🔴 **0** |
| Repos con **0 de todo** | **28 de 33** |

🔵 **La cifra que hay que llevarse es el 48 %, no el 0.** El cero era previsible —el pase 44 lo predijo— y no cambia
ninguna decisión. **Que sea la mitad de la tabla sí la cambia:** el Artículo 50(2) no es un problema de un rincón de
esta KB, es **un problema estructural de su mitad generativa**, y cualquier *engagement* que combine dos o tres de estas
piezas lo hereda completo.

## 181. 🟢 Existe UNA bandera legible por máquina de contenido generado en toda esta KB, y la granularidad que le falta está en otra fila (agregado en el pase 45 del 2026-10-02)

**El pase 44 predijo que la respuesta a la pregunta del marcado sería «ninguna». Hay una.**

🟢 **`zijinz456/OpenTutor` (MIT, 127 ★):** `services/provenance.py` → `build_provenance(..., generated: bool = True,
...)` arma un payload con **`"generated": true`** y un `source_labels` que incluye `"generated"`;
`services/agent/turn_pipeline.py:144-173` lo llama con esos valores **fijos** en el camino del turno del agente, con el
docstring *«for UI and persistence»*; **`routers/chat.py:214` lo manda al cliente** y `schemas/task.py:59` lo declara en
el esquema de tarea. **Se persiste y se sirve: no es telemetría interna.** Y el valor por omisión es `True`, o sea
**falla hacia el lado seguro**.

🔴 **Las tres cosas que le faltan, y son las tres que se cotizan:**

1. **Es un campo JSON al lado del contenido, no una marca dentro.** Si el texto se copia, se exporta o se reenvía, **la
   marca no viaja**. El Artículo 50(2) pide que la salida esté marcada y sea **detectable**; esto es detectable sólo
   mientras no se separe del sobre.
2. **Marca el turno, no el tramo.** `generated=True` está fijo en ese camino, así que no distingue **una cita textual de
   una fuente** de **una síntesis del modelo**.
3. **No está firmado.** Nada ata la bandera al contenido, así que no es resistente a manipulación — que es exactamente a
   lo que apunta *«effective, interoperable, robust and reliable»*.

🟢 **Y la granularidad que le falta está en OTRA fila de la misma tabla.** `JuneYaooo/lineage-skill` (Apache-2.0, 448 ★)
trae `references/provenance-policy.md`: un **vocabulario cerrado de 9 valores** obligatorio *«para toda afirmación
consecuente, respuesta de tarea, regla de rúbrica, juicio de feedback y regla de Personal Skill»*, del cual **cuatro son
literalmente «esto lo produjo el modelo»** — `source_grounded_synthesis`, `cross_source_synthesis`, `mentor_inference`,
`external_general_knowledge` — más `unsupported`. Y la política ya dice *«High-impact inference needs a visible label
and human review when evidence is thin»*. 🔴 **Lo que no es: legible por máquina.** Es **prosa dirigida al modelo**.

🔵 **Son mitades complementarias del mismo componente y ninguna de las dos sabe de la otra.** Una tiene **el campo y el
transporte**; la otra, **la etiqueta y la granularidad**. Y la capa que firma **ya existe en esta KB y es permisiva**
(`MarkLLM`, SynthID-Text Apache-2.0, **P33**). **El componente no hay que inventarlo: hay que conectarlo.** Ver **P99**.

## 182. ⚠️ Procedencia de fuente no es procedencia sintética: 13 de 15 hits miden otra cosa, y confundirlos sobreestima el cumplimiento 13× (agregado en el pase 45 del 2026-10-02)

El barrido del Artículo 50(2) encontró **15 artefactos de «procedencia» en 5 repos**. Es la cifra que un informe
apurado convertiría en *«cinco piezas ya tienen procedencia»*. **Dos lo son en el sentido útil; trece no.**

| Repo | Hits | Qué mide de verdad |
|---|---|---|
| 🟢 `zijinz456/OpenTutor` | 1 | **procedencia sintética**: `"generated": true` servido al cliente |
| 🟢 `JuneYaooo/lineage-skill` | 1 | **procedencia por afirmación**, con 4 de 9 valores sintéticos |
| 🔴 `ZeKaiNie/universal-examprep-skill` | 8 | *fixtures* de workspace inválido y *drift* de **procedencia de fuente** |
| 🔴 `HKUDS/DeepTutor` | 3 | *fixtures* y un componente de UI de indexado: **de qué documento salió el fragmento** |
| 🔴 `ahmedEid1/lumen` | 2 | una migración de Alembic: **de qué clon salió la fila** |

🔵 **La regla que deja esta tendencia, y aplica a cualquier barrido por palabra:** *«de dónde viene el material»* y
*«quién escribió el material»* **comparten la palabra `provenance` y responden preguntas distintas.** Saber que un
párrafo salió del capítulo 3 del libro **no dice** que el párrafo lo redactó un modelo. Un barrido que no separa las dos
acepciones **sobreestima el cumplimiento del Artículo 50(2) por un factor de 13** sobre esta misma muestra.

## 183. 🔵 El 2026-12-02 es el plazo de gracia, no el inicio: para un desarrollo nuevo el Artículo 50(2) ya está vencido — y el deber es del proveedor, no del *deployer* (agregado en el pase 45 del 2026-10-02)

Confirmado en este pase por un **tercer canal secundario independiente**, concordante con lo que esta base ya tenía bien
desde el pase 44:

| Obligación | Fecha | Estado al 2026-10-02 |
|---|---|---|
| Art. 50 transparencia | **2026-08-02** | 🔴 **vigente, vencida hace 2 meses** |
| **Art. 50(2) marcado** — sistemas puestos en el mercado **desde** el 2026-08-02 | **2026-08-02** | 🔴 **YA VIGENTE** |
| **Art. 50(2)** — *backstop* de sistemas **ya en el mercado antes** del 2026-08-02 | **2026-12-02** | ⏳ **61 días** |

🔴 **La corrección de ENCUADRE, aunque la fecha esté bien:** el 2026-12-02 **no es «cuándo empieza el Artículo 50(2)»** —
es **el plazo de gracia de lo que ya estaba desplegado**. Para **cualquier sistema nuevo** —y un *engagement* que
entrega un tutor construido sobre las piezas de esta KB **es** un sistema nuevo— **la obligación rige desde el
2026-08-02 y ya está vencida al momento de entregar.** Decir *«faltan 61 días»* sobre un desarrollo nuevo es
**tranquilizar con la fecha equivocada**, y es el error que esta misma base habilitaba al publicar una sola fecha.

🟢 **Y el dato de responsabilidad que esta KB no tenía, que es el que decide quién paga:** el deber del Artículo 50(2)
recae en el **proveedor** —quien desarrolla el sistema generativo y lo pone en el mercado, **incluidos los proveedores de
GPAI**— **no en el *deployer* ni en el usuario final.** Para un *engagement*: si Globant **construye y entrega**, el
deber viaja con el entregable; si el cliente sólo **despliega** algo de un tercero, está **aguas arriba**. 🔵 **Es una
pregunta de *discovery* de una línea** —*«¿quién pone este sistema en el mercado?»*— **y hoy no está en ningún
checklist de esta base.**

⚠️ **Límite de fuente, otra vez y por cuarto dominio: gap 92 ampliado.** A `eur-lex.europa.eu`,
`artificialintelligenceact.eu` y `data.europa.eu` se suma **`digital-strategy.ec.europa.eu`**, la página oficial del
*Code of Practice on Transparency of AI-generated Content*, probada por **los dos canales** disponibles (`curl` →
`connect_rejected`, WebFetch → `EGRESS_BLOCKED`). **Tres canales secundarios concordantes, cero primarias.**
## 184. 🔴 «Métodos que hablan con el remoto» se venía contando con el instrumento equivocado: Zoom son 5 de 14, no 2 — y 0 directos (agregado en el pase 46 del 2026-10-02)

P94 publica *«Métodos que hablan con el remoto: Jitsi **1**, Zoom **2**»*. Medido sobre `HEAD 7f45689` de
`SafeExamBrowser/seb-server` con **cerradura transitiva** del grafo de llamadas: **Jitsi 1 de 14 (correcto), Zoom
5 de 14**. Los cinco: `testExamProctoring` (d=2), `newCollectingRoom` (d=3), `newBreakOutRoom` (d=3),
`disposeBreakOutRoom` (d=3), `disposeServiceRoomsForExam` (**d=4**).

🔴 **Y el dato que explica por qué la cuenta anterior no podía acertar: en Zoom, CERO métodos de la interfaz llaman a la
red directamente.** Los cinco la alcanzan por helpers privados (`createAdHocMeeting`, `deleteAdHocMeeting`) y por la
jerarquía interna `ZoomRestTemplate`. **Un barrido que mire el cuerpo del método puntúa 0.** La magnitud que se cotiza
—«llamar a este método provoca un viaje HTTP»— es **transitiva por naturaleza**, y la asimetría real entre la ruta
barata y la realista es **1 contra 5**, no 1 contra 2. Reproducible en
`compose/code/proctoring-reach-audit/` (20/20, regeneración byte a byte aseverada).

## 185. 🔴 El método que P94 tenía como local es el único sin tope: `disposeServiceRoomsForExam` son `2 × N` peticiones dentro de un `forEach` (agregado en el pase 46 del 2026-10-02)

`disposeServiceRoomsForExam` itera las salas del examen (`remoteProctoringRoomDAO.getRooms(examId).forEach`) y llama a
`disposeBreakOutRoom` **por cada una**; cada una baja a `deleteAdHocMeeting`, que hace **dos** peticiones
(`deleteMeeting` + `deleteUser`). **No es un viaje HTTP: son `2 × N`, con N = salas, y no hay tope en el código.**

🔵 **Y la de al lado tiene el mismo problema en la dirección de creación: crear una sala cuesta TRES llamadas**, no una
—`createUser` + `applyUserSettings` + `createMeeting` (líneas 543/554/558)—, porque **`createAdHocMeeting` crea un
usuario ad-hoc en Zoom por sala.** Para la propuesta: éstos son los dos métodos que hay que probar con carga, y P94 los
contaba como locales.

## 186. 🟢 Todo el HTTP de Zoom sale por un único `exchange` privado con *circuit breaker*: es el artefacto más reutilizable de esta ruta (agregado en el pase 46 del 2026-10-02)

Las siete operaciones de la API de Zoom (`createUser`, `applyUserSettings`, `createMeeting`, `deleteMeeting`,
`deleteUser`, `testServiceConnection`, y el `getAccessToken` de OAuth) **convergen en un solo método privado**
`exchange` (línea 940) que envuelve `restTemplate.exchange` en `circuitBreaker.protectedRun(...)` y degrada los ≥400 a
*warning* con el cuerpo preservado.

🟢 **Para un proveedor propio eso es la buena noticia del pase: hay UN punto donde poner reintentos, *timeouts* y el
*circuit breaker*, y conviene copiar la forma en vez de inventarla.** 🔴 **Con una excepción que no pasa por ahí:**
`getZoomRestTemplate` valida el template cacheado con `oAuth2RestTemplate.getAccessToken()` (línea 1027), que **pide el
token al endpoint de Zoom**. **Validar la caché es tráfico, y es el viaje HTTP menos evidente de la clase.**

## 187. 🔴 Tercera pieza, tercer acierto del mismo control: el control (c) atrapa constructores emitidos como métodos, y el defecto es del MÉTODO de extracción (agregado en el pase 46 del 2026-10-02)

La primera corrida del extractor de `proctoring-reach-audit` emitió **8 constructores como métodos**:
`JitsiProctoringService`, `ZoomProctoringService`, `ZoomRestTemplate`, `OAuthZoomRestTemplate`, y `Context`,
`Features`, `JWTContext` y `User` de las clases internas. Es **exactamente** el defecto que el control (c) encontró en
las tablas de rutas de `sebserver-mcp-gate` (pase 44) y `unitime-mcp-gate` (pase 45).

🔵 **Tres artefactos distintos, tres lenguajes de declaración distintos, el mismo falso positivo: la conclusión es que
el defecto no es de un árbol, es del método de extracción basado en expresiones regulares sobre declaraciones.** La
regla que queda: **toda tabla derivada de un árbol necesita una columna `kind`**, y el nombre de un tipo declarado en el
archivo es el discriminador más barato.

## 188. 🔴 El verbo no identifica una petición HTTP: el RECEPTOR sí — y `Map.put` costó 16 llamadas de red fantasma (agregado en el pase 46 del 2026-10-02)

Un detector de primitivas de red con lista de verbos que incluya `put` y `delete` puntúa `attributes.put(...)` —un
`Map.put` corriente— como petición HTTP. Medido: **6** llamadas falsas en `createJoinInstructionAttributes` de Jitsi y
**10** en el de Zoom, **dos métodos que no tocan un socket**.

🔴 **Y la corrección obvia tampoco alcanza:** exigir un receptor *parecido* a un template (`\w*restTemplate\w*`)
acepta `restTemplatesCache`, que es un `LinkedHashMap`, y le regala **2** llamadas fantasma a `getZoomRestTemplate`. **El
receptor tiene que TERMINAR en `restTemplate`.** 🔵 **Y la decisión explícita en la dirección contraria: construir un
`RestTemplate` NO es una petición** —Jitsi construye uno en la 162 y la llamada real es el `getForEntity` de la 163—;
contar el constructor habría inflado la misma cifra que había que corregir. **Las tres reglas son del instrumento, y las
tres se encontraron porque la cifra no cerraba con la lectura a mano.**

## 189. 🔵 El mapeo de los 9 valores de procedencia al booleano del Artículo 50(2) son CINCO sintéticos, no cuatro: `unsupported` es autoría por eliminación (agregado en el pase 46 del 2026-10-02)

El pase 45 contó *«cuatro valores son literalmente ‘esto lo produjo el modelo’»*
(`source_grounded_synthesis`, `cross_source_synthesis`, `mentor_inference`, `external_general_knowledge`). El componente
del pase 46 marca **cinco**, y el criterio queda escrito: **`synthetic` es verdadero cuando el MODELO escribió las
palabras** — no cuando la afirmación es falsa, ni cuando está mal fundada. **Son ejes distintos y confundirlos es cómo
este campo se llena mal.**

*«No adequate evidence is available»* habla de **evidencia**, no de autoría, así que `unsupported` se lee como una
quinta categoría y no como un quinto `true`. **Se marca igual, por eliminación: si ninguna fuente sustenta la
afirmación, ninguna fuente la escribió tampoco, y el único autor que queda es el modelo.** Marcarlo `false` produce
exactamente el caso que el Artículo 50(2) existe para evitar — **prosa del modelo sin fuente llegando a un alumno con
`synthetic: false` adosado**.

## 190. ⚠️ El error simétrico del marcado, que esta base conviene decir en voz alta: marcar como AI un tramo del ALUMNO es dato incorrecto, no cautela (agregado en el pase 46 del 2026-10-02)

Cuatro de los nueve valores son de autoría **humana**: `direct_source` (lo escribió la fuente del docente),
`learner_hypothesis` y `learner_observation` (lo escribió **el alumno**) y `real_world_evidence` (un hecho del mundo
transportado). **Los cuatro devuelven `synthetic: false` a propósito.**

⚠️ **Marcar `learner_observation` como generado por AI le estaría diciendo a un estudiante que su propia oración la
escribió una máquina** — y en un contexto educativo eso no es una imprecisión de metadato, es una acusación de autoría.
🔵 **La distinción con el *fail-closed*:** fallar cerrado aplica a **lo desconocido** (una etiqueta fuera del
vocabulario se marca `true` y se señala con `flags: ["unknown_provenance"]`); **no** aplica a lo conocido-humano.
***«Por las dudas marco todo»* no es una política conservadora: es una política equivocada**, y degrada el valor
informativo de la marca para los tramos que sí la necesitan.

## 191. 🟢 OpenTutor no tenía la granularidad «a medias»: no la tenía — y esta base queda más estricta que su propia fuente (agregado en el pase 46 del 2026-10-02)

`apps/api/services/provenance.py` leído de primera mano: **72 líneas, dos funciones**. `build_provenance` tiene **12
parámetros** y **ninguno por tramo** — ni `spans`, ni desplazamientos, ni etiqueta por afirmación. 🔵 **La granularidad
que esta base describía como faltante no estaba incompleta: estaba ausente.**

🟢 **Y la extensión resulta más estricta que el upstream, que no es lo que se esperaba.** `turn_pipeline.py` fija
`generated=True` en el camino del agente, así que **no puede representar un turno que sólo cita fuentes y relata lo que
dijo el alumno**. Con el booleano como **OR sobre los tramos**, el turno de ejemplo mide **1 de 3 tramos sintéticos, 81
de 170 caracteres**, y un turno sin síntesis reporta `generated: false` **porque se midió**. 🟢 **Compatibilidad
preservada a propósito:** `generated` y `source_labels` conservan el significado que `routers/chat.py:214` ya sirve y
`schemas/task.py:59` ya persiste, así que un consumidor que sólo entiende el turno sigue funcionando.

## 192. 🟢 `metadataType` de SCORM termina en `grp.any`: hay NUEVE puntos de extensión legales, no uno (agregado en el pase 46 del 2026-10-02)

Leído del `imscp_v1p1.xsd` que **empaqueta `scorm-mcp-server`** (15 XSD, conformidad offline): `metadataType`
(línea 267) es `schema?` + `schemaversion?` + `<xsd:group ref="grp.any"/>`, y `grp.any` (línea 141) es
`<xsd:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>` — **cualquier cantidad de
elementos de cualquier otro *namespace*, validados laxamente.**

🔵 **Y `grp.any` aparece en NUEVE `complexType`:** `manifestType`, `metadataType`, `organizationsType`,
`organizationType`, `itemType`, `resourcesType`, `resourceType`, `fileType` y `dependencyType`. **El marcado del
Artículo 50(2) no tiene un punto de inyección legal: tiene nueve**, y `<metadata>` del manifiesto es el de mayor alcance
(cubre el paquete entero) mientras `itemType` y `resourceType` permiten marcar **por SCO**.

## 193. 🔴 La condición dura del marcado en SCORM es el *namespace*, y está medida con `xmllint`, no razonada desde `lax` (agregado en el pase 46 del 2026-10-02)

Tres casos corridos contra los XSD del propio repo:

| Caso | Resultado |
|---|---|
| manifiesto 2004 base | `validates` |
| `<m:aiGenerated xmlns:m="urn:globant:aiact:50-2">` en `<metadata>` | 🟢 **`validates`** |
| `<bogus>x</bogus>` (*namespace* por omisión) en `<metadata>` | 🔴 **`fails to validate`** |

🔵 **La pregunta del gap 97 era si marcar en el `pack` ROMPE la conformidad. No la rompe — con la condición de que el
marcador declare su propio *namespace*.** Un `<synthetic>` sin prefijo **invalida el paquete**, y es el error que
cualquiera cometería primero. 🔵 **Consecuencia de diseño que esto decide:** el componente se inyecta **UNA vez en el
empaquetado** y no **32 veces** en cada generador expuesto. Y `scorm_validate` no agrega veto propio: sus **9 checks**
son estructurales (`zip-readable`, `manifest-at-root`, `manifest-parses`, `version-detected`, `organization`,
`launch-resource`, `entry-exists`, `files-exist`) más `schema-valid`, que es justamente el `xmllint` de arriba.

## 194. ⚠️ El punto de inyección es legal pero no tiene gancho: el `<metadata>` de `scorm-mcp-server` es un literal de cadena (agregado en el pase 46 del 2026-10-02)

`buildManifest` (línea 535) y `buildManifest12` (línea 576) de `src/converter.ts` arman el manifiesto como **plantilla
de cadena**, con `<schema>ADL SCORM</schema>` y `<schemaversion>` **fijos** y **ningún parámetro de extensión**:
`buildManifestFor` recibe `identifier`, `title`, `language`, `entryHref`, `extraFiles` y `masteryScore` — **nada para
metadatos arbitrarios**.

⚠️ **O sea: el estándar admite el marcador (tendencia 192), el validador lo acepta (193), y el generador no lo puede
emitir.** Inyectar exige **parchear el generador** (un parámetro opcional que se concatene antes de `</metadata>`) **o
post-procesar el ZIP** reescribiendo `imsmanifest.xml`. **La segunda no toca upstream y es la barata; la primera es un
PR de pocas líneas y es la que sirve a todos.** Queda como **gap 100**.

## 195. 🟢 El gap 92 se MATIZA y no se cierra: los dominios institucionales aparecen con título legible en el buscador, aunque sigan sin responder al *fetch* (agregado en el pase 46 del 2026-10-02)

El barrido regional de este pase devolvió, como resultados con título y ruta,
`coe.int/web/education/-/key-stakeholders-across-europe-will-explore-the-regulatory-dimensions-of-ai-in-education-at-the-2nd-working-conference-in-october`
y `unu.edu/publication/ai-implementation-higher-education-latin-america-and-caribbean` — **los dos dominios que el gap
65 registra como bloqueados**.

🔵 **Hay que decirlo con precisión, porque la tentación de cerrar el gap es alta y sería incorrecto: eso NO es acceso a
la fuente primaria.** Es el buscador devolviendo **metadatos** (título y URL), no el documento. **Lo que sí mejora: el
título y la fecha del evento del Consejo de Europa ahora provienen del propio dominio**, en vez de la paráfrasis de un
tercero — un grado más de autoridad sobre **el hecho de que el evento existe y cuándo**, y cero grados sobre **su
contenido**. **El gap 92 queda matizado: el canal de información y el canal de *fetch* fallan por separado**, que es la
tendencia 130 confirmada por un segundo camino.

## 196. ⚠️ Décima aparición de la fecha vencida del AI Act, y las secundarias comerciales se contradicen justo en la fecha que no se puede verificar contra primaria (agregado en el pase 46 del 2026-10-02)

El barrido de North America volvió a afirmar que el AI Act *«toma efecto pleno en agosto de 2026»* clasificando
educación como **alto riesgo**. 🔴 **Esta base lo corrigió en el pase 32: educación es Anexo III y la fecha se movió a
2027-12-02.** Es la **décima** aparición y la enésima en el **mismo** barrido regional.

⚠️ **El encuadre que importa para cualquier afirmación regulatoria de esta KB:** la fecha vencida aparece en el canal
comercial **de forma sistemática**, mientras el texto consolidado del Reglamento (UE) 2024/1689 sigue inalcanzable por
**cuatro** canales (gap 92). **O sea: la única fecha que esta base no puede verificar contra primaria es exactamente la
que sus fuentes secundarias publican mal.** La regla operativa no cambia y conviene repetirla cada vez que se cite:
**las fechas están confirmadas por tres canales secundarios independientes y concordantes, no por fuente primaria, y
eso se dice en la propuesta.**

## 🔵 Las tendencias 197–210, del pase 47 del 2026-10-02

**Las catorce salen de ejecutar las tres acciones del pase 46 y el barrido obligatorio. Siete corrigen afirmaciones de
esta base.**

| # | Tendencia | Evidencia |
|---|---|---|
| **197** | 🔴 **Un estándar de empaquetado puede tener dos dialectos cuyos comodines XSD no coinciden, y el generador que los emite no avisa.** `buildManifestFor` despacha a 2004 (`lax`) y a 1.2 (`strict`) con la misma firma | `src/converter.ts:603`; `grep -A6 'name="grp.any"'` sobre los dos XSD |
| **198** | 🔴 **Bajo `processContents="strict"`, «desconocido» significa «inválido».** Un elemento foráneo sin declaración global no se tolera: se rechaza | `xmllint`: *«No matching global element declaration available, but demanded by the strict wildcard»* |
| **199** | 🔵 **El mismo conteo puede necesitar dos instrumentos distintos en dos archivos del mismo repo.** Los 9 puntos de extensión se cuentan con `ref = "grp.any"` en 2004 y con `ref="grp.any"` en 1.2: **el espaciado difiere** | `grep -c` sobre cada uno |
| **200** | 🔴 **Un validador de conformidad puede rechazar los metadatos del propio estándar que valida.** `wrapper12.xsd` importa 2 de los 3 *namespaces* que el repo empaqueta y deja afuera el de LOM | `src/validate.ts:49-52`; `xmllint` sobre un manifiesto 1.2 con `<imsmd:lom>` |
| **201** | 🟢 **Y el arreglo de un defecto así puede ser de UNA línea sobre un archivo que ya está en el repo.** Agregar el `import` de `imsmd_rootv1p2p1.xsd` hace validar los cinco casos | medido con el *wrapper* parcheado |
| **202** | 🔵 **Marcado tipado y marcado portátil son objetivos en conflicto.** El portador que valida en los dos dialectos (`<imsmd:lom><imsmd:classification>`) obliga a codificar los tramos como cadenas | matriz de 2×3 casos en `compose/code/aiact-50-2-pack/` |
| **203** | 🔴 **Una sección de patrón puede titularse «escrito y probado» y no tener código en el repositorio.** P85 publica «175 líneas» y su variable documentada vive sólo en la prosa | `grep -rl MCP_ALLOWLIST compose/code/` → vacío |
| **204** | 🔴 **Una cifra de una suite propia se vence cuando la suite crece, y nadie lo nota.** Dos de este archivo estaban vencidas por uno y por dos pases | 11/11 → **37/37**; 23 → **46** |
| **205** | ⚠️ **Una cifra condicional citada sin su condición es irreproducible aunque sea correcta.** Dos suites dan un número distinto según el argumento o la variable de entorno | 19/19 vs **20/20**; 23/23 vs **24/24** |
| **206** | 🔵 **Un instrumento que audita cifras puede tener el defecto que audita.** `\b` tras un carácter que no es de palabra nunca dispara: se perdían el 44 % de las mediciones | 205 reportadas vs **368** reales, sobre el mismo archivo |
| **207** | 🔴 **Cero de 33 piezas educativas expuestas emiten un límite dentro del texto que generan.** El clasificador por tramo del Artículo 50(2) es desarrollo nuevo, no integración | `compose/code/aiact-50-2-spans/result.2026-10-02.tsv` |
| **208** | 🔵 **El vocabulario de procedencia está en todas partes y apunta al lado equivocado.** 16 de 33 repos hablan de `citation`/`chunk`/`grounding`: todos describen **de dónde vino el contexto**, ninguno **qué escribió el modelo** | ídem; confirma con lectura de código lo que el pase 45 vio en nombres de archivo |
| **209** | ⚠️ **Un barrido por tokens produce falsos positivos que se parecen a hallazgos.** `toc_end_index = min(5, len(images))` es paginado de PDF, y un `chunk_index` con `UniqueConstraint` es una columna | los tres `HANDLE`, abiertos uno por uno |
| **210** | 🟢 **El canal multilateral del gap 65/92 devolvió, por primera vez, la RUTA de un PDF y no sólo un título** — el BID, *An Enabling Regulatory Framework for AI in LAC*. ⚠️ **Y el *fetch* sigue bloqueado: `000`, ni un código HTTP** | barrido regional LATAM; `curl -s -o /dev/null -w '%{http_code}'` sobre la URL del PDF |

## 🔵 Estado de gaps al cierre del pase 47 del 2026-10-02

| Gap | Estado | Evidencia |
|---|---|---|
| **99** — nadie asigna las etiquetas por tramo | ✅ **CERRADO con un NO** | **0 de 33** filas expuestas emiten un límite en el texto generado. 24.206 archivos listados, 3.249 candidatos, **432 leídos** (tope 25/repo). Los **3** `HANDLE` son límites de **entrada** y uno es falso positivo |
| **100** — el generador SCORM no tiene gancho de metadatos | ✅ **CERRADO con código** | `compose/code/aiact-50-2-pack/`, **27/27** sin `xmllint` y **37/37** con los dos directorios de esquemas. Las cuatro aserciones que pidió la acción, más la matriz de dialectos |
| **101** — cifras publicadas sin nombrar su métrica | ✅ **CERRADO con un script repetible** | `compose/code/patterns-figure-audit/`: **383** mediciones (**368** antes de que este pase agregara P106–P108), **165** reproducibles acá, **4** que no cierran, **todas corregidas en su lugar** |
| **97** — ¿el `pack` es el punto barato de marcado? | 🔄 **REABIERTO y matizado** | El **lugar** era correcto; la **forma** no. `strict` en SCORM 1.2 exige un portador distinto. Cerrado otra vez por **P106** |
| **102** (nuevo) 🔴 | **`scorm_validate` rechaza metadatos LOM estándar de SCORM 1.2** | `wrapper12.xsd` importa 2 de 3 *namespaces*. Arreglo de **una línea**; es un **PR corto a upstream** y esta base no lo puede abrir desde acá |
| **103** (nuevo) 🔴 | **el código de las «175 líneas» de P85 no está en este repositorio** | `MCP_ALLOWLIST` sólo en `compose/patterns.md`. **Dos tablas de solución lo citan como resuelto.** Dos caminos: escribir la pieza genérica, o reemplazar las citas por las dos puertas concretas (hecho en su lugar, provisionalmente) |
| **98** 🔴 | **la firma sigue sin existir** | `sign_hook()` sigue declarada y vacía. Sin cambios en este pase |
| **92** ⚠️ | texto consolidado del Reglamento (UE) 2024/1689 inalcanzable | Cuatro canales. 🟢 **Matizado otra vez: el BID devolvió URL de PDF** (tendencia 210), así que el canal multilateral mejora un grado más; el de EUR-Lex no |

## 🔵 Las tres acciones que el pase 47 deja escritas para el pase 48

**Las tres son ejecutables en este entorno: ninguna necesita Docker, ni instalar dependencias de terceros, ni la API de
GitHub. La primera es la de más valor comercial porque cierra la única promesa que este pase dejó a medias; la segunda es
la más barata y la que más reputación protege; la tercera es la que decide si el tramo medio de P108 se puede cotizar.**

1. 🔴 **Resolver el gap 103 escribiendo la pieza genérica de P85, o degradando P85 a patrón** (**gap 103**). Este pase
   encontró que **«175 líneas, escrito y probado»** no tiene código acá, y arregló las citas **provisionalmente**
   apuntándolas a las dos puertas concretas. Eso no es una solución: **P60, P92 y P93 se apoyan en P85**, y las dos
   puertas que existen son **específicas** de SEB Server y de UniTime. **La acción concreta:** extraer de
   `compose/code/sebserver-mcp-gate/gate.py` y `compose/code/unitime-mcp-gate/gate.py` —que ya comparten el
   comportamiento y miden **145** líneas no-blancas **cada una**— el *gateway* genérico que P85 describe, con
   `MCP_ALLOWLIST` como nombre de variable tal como está documentado, el `hard_deny()` como **piso** del pase 45, y la
   matriz de casos que P85 publica convertida en aserciones. 🔵 **El valor: cierra la única fila de esta base que le
   promete a un cliente un artefacto inexistente, y lo hace con código que ya está escrito dos veces.**
2. 🔵 **Barrer las cifras de los OTROS siete archivos con el instrumento del pase 47** (**extiende gap 101**). La acción
   2 barrió `compose/patterns.md` porque es el activo más citado, y encontró **cuatro** fallas en las **368** mediciones que tenía el archivo al empezar —
   un **1,0 %**, con una de ellas grave. **`intel/trends.md` tiene 894 KB y `intel/market.md` 548 KB, y ninguno fue
   barrido.** **La acción concreta:** correr `extract_figures.py` sobre los ocho archivos (es un parámetro de ruta),
   publicar el inventario por archivo, y verificar a mano **las cifras sobre código propio de esta base**, que son las
   reproducibles. 🔵 **El valor: es casi gratis —el instrumento existe y está probado— y el pase 47 ya demostró que la
   tasa de falla no es cero.** ⚠️ **Y arreglar primero el `\b` en cualquier patrón nuevo que se agregue: ese defecto
   costó el 44 % del inventario.**
3. ⚠️ **Medir si el tramo MEDIO de P108 se puede cotizar, leyendo `project-nomad` de punta a punta** (**gap 104**,
   nuevo). P108 promete *«`synthetic` por turno, separando `direct_source` del resto, 3-4 semanas»* **sobre una sola
   pieza y sobre una sola lectura**: `rag_service.ts:1137` mete `chunk_index` + `source` + `document_id` en el
   `metadata` del resultado de recuperación. **Falta la mitad del camino: que eso llegue a la respuesta que ve el
   alumno.** **La acción concreta:** seguir el `metadata` desde `rag_service.ts` hasta el *handler* que sirve la
   respuesta, y contestar **una** pregunta: ¿el cliente recibe la identidad de la fuente, o se consume adentro para
   *ranking* y se descarta? 🔵 **El valor: si llega, el tramo medio es integración y los 3-4 semanas se sostienen; si se
   descarta, P108 tiene que bajar la promesa antes de que alguien la cotice.**

⚠️ **Y las acciones hacia afuera que esta corrida sigue sin poder ejecutar, declaradas para no perderlas:** el `LICENSE`
que falta en `Timadey/proctor` (**un PR de un archivo**); la licencia sin segunda fuente de `@ink-waffle/sisu-mcp`
(**bloqueante: sigue siendo la única puerta de SIS de educación superior de esta base**); el acceso de miembro a los
repositorios de Caliper Sensor API de 1EdTech; 🔴 **y ahora DOS PR a `giacomomaria81/scorm-mcp-server`: el gancho de
metadatos en `buildManifestFor`** (gap 100, camino largo) **y el `import` de una línea en `wrapper12.xsd`** (gap 102,
**el más barato y el que arregla un rechazo de paquetes conformes**); y 🔵 **el texto consolidado del Reglamento (UE)
2024/1689, inalcanzable por CUATRO canales** (gap 92, matizado por las tendencias **195** y **210**).

## 🔵 Estado de gaps al cierre del pase 46 del 2026-10-02

| Gap | Estado | Evidencia |
|---|---|---|
| **95** — componente transversal de marcado del Art. 50(2) especificado y sin código | ✅ **CERRADO con código** | `compose/code/aiact-50-2-marking/`, **24/24** aserciones, sólo stdlib. Las tres que pidió la acción: cita textual **no** marcada, `mentor_inference` **sí**, y la marca **sobrevive** `dumps`→`loads` del artefacto separado del sobre con los desplazamientos intactos (rango `(50, 131)`) |
| **96** — la tercera pieza de código sin auditar con los controles | ✅ **CERRADO, y corrige P94** | `compose/code/proctoring-reach-audit/`, **20/20**. Control (c) **falló** (8 constructores); control (e) **falló contra P94**: Zoom 5 de 14 y 0 directos |
| **97** — ¿el `pack` es el punto de marcado más barato? | ✅ **CERRADO a favor** | `metadataType` termina en `grp.any` (**9** puntos de extensión); `xmllint`: *namespace* propio **valida**, por omisión **falla**. Se inyecta **1 vez**, no 32 |
| **98** (nuevo) 🔴 | **la firma sigue sin existir** | `sign_hook()` es una costura **declarada y vacía**. La marca viaja **con** el texto tras `detach_artifact`, pero **no está EN** el texto: copiar sólo el texto la pierde. `MarkLLM`/SynthID (**P33**) necesitan el decodificador y este módulo corre después |
| **99** (nuevo) 🔴 | **nadie asigna las etiquetas por tramo** | El componente **mapea, transporta y asevera**; **no clasifica**. Falta medir si alguna de las 32 filas expuestas emite algo mapeable a los 9 valores, o si el clasificador hay que escribirlo entero |
| **100** (nuevo) ⚠️ | **el generador SCORM no tiene gancho de metadatos** | `buildManifest`/`buildManifest12` son literales de cadena sin parámetro de extensión (tendencia **194**). Dos caminos: PR de pocas líneas a upstream, o post-procesar el ZIP |
| **101** (nuevo) 🔵 | **cifras publicadas sin nombrar su métrica** | P94 decía «481 / 912 líneas» y **era correcto** — son **no-blancas-no-comentario**, mientras `wc -l` da **583 / 1.116**. La cifra acertaba y **la métrica no estaba escrita** durante tres pases. Hay que barrer las demás cifras numéricas de `compose/patterns.md` y nombrarles el instrumento |

## 🔵 Las tres acciones que el pase 46 deja escritas para el pase 47

**Las tres son ejecutables en este entorno: ninguna necesita Docker, ni instalar dependencias de terceros, ni la API de
GitHub. La primera convierte el hallazgo del gap 97 en entregable; la segunda es la más barata y la que más cuentas
corrige; la tercera es la que decide si el componente del pase 46 sirve o queda de adorno.**

1. 🟢 **Escribir el post-procesador que inyecta el marcado en un paquete SCORM ya construido, y validarlo con
   `xmllint`** (**gap 100**). El pase 46 probó que el marcador es legal y que el generador no lo puede emitir. **La
   acción concreta:** un módulo en `compose/code/` que tome un `.zip` SCORM, reescriba `imsmanifest.xml` insertando el
   fragmento de `manifest_metadata_fragment()` **antes de `</metadata>`**, y **asevere cuatro cosas**: que el ZIP
   resultante sigue validando contra `imscp_v1p1.xsd`, que el `imsmanifest.xml` original **sin** marcador también
   validaba (control de que la prueba mide algo), que **re-inyectar es idempotente** (no duplica el elemento), y que un
   paquete **sin** `<metadata>` se rechaza con un error claro en vez de corromperse. 🔵 **El valor: cierra el único
   tramo que falta entre «esta KB tiene el componente» y «esta KB marca un curso entregable», sin tocar upstream.**
2. 🔵 **Barrer las cifras numéricas de `compose/patterns.md` y nombrarle el instrumento a cada una** (**gap 101**). El
   caso del pase 46 es el aviso: **«481 líneas» era correcto y su métrica no estaba escrita**, así que durante tres
   pases nadie podía reproducirla —`wc -l` da 583— y una propuesta que la citara habría defendido un número que no
   cerraba. **La acción concreta:** listar toda cifra de `compose/patterns.md` que sea una **medición** (líneas, tools,
   métodos, porcentajes, descargas), y para cada una escribir **con qué comando se obtiene**; marcar las que no se
   puedan reproducir hoy. 🔵 **El valor: es la acción más barata del backlog y toca el activo más citado — los
   patrones son lo que se pega en una propuesta.**
3. 🔴 **Medir si existe alguna fuente de procedencia POR TRAMO en las 32 filas expuestas, o si el clasificador hay que
   escribirlo entero** (**gap 99**). El pase 45 encontró **15 artefactos de procedencia en 5 repos** y advirtió que
   **13 de 15 son procedencia de FUENTE, no sintética**. El componente del pase 46 necesita que alguien **asigne** una
   de las 9 etiquetas a cada tramo, y hoy no se sabe si algo lo hace. **La acción concreta:** sobre los repos ya
   listados en `compose/code/aiact-50-2-exposure/rows.tsv`, buscar en el árbol (`--filter=blob:none --sparse`) si algún
   generador emite **límites de tramo** —*offsets*, *citations* con rango, *chunk ids* en la respuesta— y responder
   **una** pregunta: ¿hay por dónde agarrar el tramo, o la salida es un bloque de texto opaco? 🔵 **El valor: si la
   respuesta es «opaco» en las 32, el componente del pase 46 exige un clasificador propio y eso cambia el presupuesto;
   si alguna emite *offsets*, esa fila es el piloto.**

⚠️ **Y las acciones hacia afuera que esta corrida sigue sin poder ejecutar, declaradas para no perderlas:** el
`LICENSE` que falta en `Timadey/proctor` (**un PR de un archivo**); la licencia sin segunda fuente de
`@ink-waffle/sisu-mcp` (**bloqueante: sigue siendo la única puerta de SIS de educación superior de esta base**); el
acceso de miembro a los repositorios de Caliper Sensor API de 1EdTech; 🟢 **el PR de pocas líneas a
`giacomomaria81/scorm-mcp-server` para que `buildManifestFor` acepte metadatos de extensión** (**gap 100**, camino
largo); y 🔵 **el texto consolidado del Reglamento (UE) 2024/1689, que sigue inalcanzable por CUATRO canales** (gap 92,
matizado por la tendencia **195**: el buscador devuelve título y URL de `coe.int` y `unu.edu`, el *fetch* sigue
bloqueado).

## 🔵 Las tres acciones que el pase 45 deja escritas para el pase 46

**Las tres son ejecutables en este entorno: ninguna necesita Docker, ni instalar dependencias de terceros, ni la API de
GitHub. La primera es la de más valor comercial y es la que este pase dejó armada sin ejecutar.**

1. 🟢 **Escribir el componente transversal de marcado del Artículo 50(2), que este pase dejó especificado y sin código**
   (**gap 95**). Las tres piezas están identificadas y ninguna hay que inventarla: **el campo y el transporte** los
   tiene `OpenTutor` (`build_provenance`, `"generated": true`, servido en `routers/chat.py:214`); **la etiqueta y la
   granularidad por afirmación** las tiene `lineage-skill` (vocabulario cerrado de 9 valores, 4 de ellos sintéticos); y
   **la firma** la tiene la capa forense permisiva de esta KB (`MarkLLM`, SynthID-Text Apache-2.0, **P33**).
   **La acción concreta:** escribir en `compose/code/` un módulo que (a) **mapee los 9 valores de `lineage-skill` a un
   booleano `synthetic` más el valor original**, porque esa es la decisión de diseño que nadie tomó todavía; (b) emita
   el payload de `OpenTutor` **extendido con el tramo** (`spans`, no sólo el turno); y (c) **asevere tres cosas**: que
   un tramo citado textualmente de una fuente **no** se marca como sintético, que un tramo de `mentor_inference` **sí**
   se marca, y que la marca **sobrevive a un `json.dumps` → `json.loads`** del artefacto separado del sobre.
   🔵 **El valor: convierte «esta KB no cumple el Artículo 50(2)» en «esta KB tiene el componente», y el hueco está
   medido en 32 filas.**
2. 🔴 **Re-auditar la TERCERA pieza de código de esta base con los cinco controles, que es la única que queda sin
   pasar** (**gap 96**). `compose/code/seb-proctoring-validator/` se escribió en el pase 43 y **nunca se midió con los
   controles**, que no existían. **La acción concreta:** correr sobre él las cinco aserciones —(a) ninguna ruta con
   `${`, (b) toda ruta absoluta **y con contexto**, (c) ninguna fila de una declaración de clase, (d) todo guarda
   condicional registrado **incluido el de runtime dentro del método**, (e) **ningún verbo de lectura que escriba**— y
   en particular **(e), que es el control nuevo**: el validador afirma qué métodos de `RemoteProctoringService` son
   triviales y cuáles hablan con el remoto, **y esa clasificación es exactamente la que el control (e) pone en duda**.
   🔵 **El valor: de las tres piezas de código de esta KB, dos quedarían auditadas y la tercera es la que sostiene la
   cotización de proctoring.**
3. 🟢 **Medir si el `pack` del Artículo 50(2) es el punto de marcado más barato, leyendo `scorm-mcp-server`**
   (**gap 97**). Este pase lo clasificó como **el único `pack`** —*«donde el contenido generado se vuelve el curso que
   el alumno abre»*— **por razonamiento, no por medición**. **La acción concreta:** leer el árbol de
   `giacomomaria81/scorm-mcp-server` (**MIT**, 3 tools) y responder **dos preguntas que hoy no tienen número**: si el
   `imsmanifest.xml` que emite admite **metadatos arbitrarios** (y en qué elemento, porque SCORM 2004 tiene
   `<adlcp:location>` y perfiles de LOM), y si `scorm_validate` **rechazaría** un paquete con un metadato extra — porque
   si lo rechaza, marcar en el empaquetado **rompe la conformidad** y el punto barato no existe.
   🔵 **El valor: decide si el componente de la acción 1 se inyecta UNA vez en el empaquetado o 32 veces en cada
   generador.**

⚠️ **Y las acciones hacia afuera que esta corrida sigue sin poder ejecutar, declaradas para no perderlas:** el `LICENSE`
que falta en `Timadey/proctor` (**un PR de un archivo**); la licencia sin segunda fuente de `@ink-waffle/sisu-mcp`
(**bloqueante: sigue siendo la única puerta de SIS de educación superior de esta base**); el acceso de miembro a los
repositorios de Caliper Sensor API de 1EdTech; y 🔵 **el texto consolidado del Reglamento (UE) 2024/1689, que este pase
volvió a intentar y que sigue inalcanzable, ahora por CUATRO canales** —`eur-lex.europa.eu`,
`artificialintelligenceact.eu`, `data.europa.eu` y `digital-strategy.ec.europa.eu`, los cuatro `connect_rejected` o
`EGRESS_BLOCKED` (**gap 92, ampliado**)—. **Las fechas quedan confirmadas por tres canales secundarios independientes y
concordantes, no por fuente primaria, y eso hay que seguir diciéndolo cada vez que se citen.**
## 🔵 Las tres acciones que el pase 44 deja escritas para el pase 45

**Las tres son ejecutables en este entorno: ninguna necesita Docker, ni instalar dependencias de terceros, ni la API de
GitHub. Las dos primeras son el mismo gesto —clonar con `--sparse` y leer— sobre dos capas distintas.**

1. 🔴 **Re-auditar las OTRAS dos puertas escritas por esta base con los cuatro controles que el pase 44 tuvo que
   inventar** (**gap 93**). El defecto de las rutas relativas no era del upstream: era del extractor, y
   **`compose/code/unitime-mcp-gate/` se construyó con el mismo método en el pase 42**, antes de que existieran los
   controles. **La acción concreta:** correr sobre `connectors.tsv` de UniTime las cuatro aserciones que ahora están en
   `test_gate.py` —(a) ninguna ruta contiene `${`, (b) toda ruta empieza con `/`, (c) ninguna fila proviene de una
   declaración de clase, (d) toda clase condicionada está excluida— y, si UniTime también cuelga de una propiedad,
   corregir sus 26 tools. 🔵 **El valor: las dos puertas son el entregable más concreto de esta KB, y una de las dos
   está verificada y la otra no.**
2. 🟢 **Cerrar el costo de P55 escribiendo el generador de curso y probándolo contra el contrato medido, sin levantar
   Open edX** (**gap 94**). El pase 44 fijó las tres piezas que faltaban: el POST devuelve `locator`, el árbol se lee de
   `course_index` en una llamada y `category` no tiene enum en un curso. **La acción concreta:** escribir en
   `compose/code/` un generador que tome un outline (capítulo → secuencia → vertical → bloques) y emita **la secuencia
   exacta de POSTs** con el encadenado `locator → parent_locator`, más un *stub* del endpoint que devuelva `locator`
   sintéticos, y **asevere tres cosas**: que ningún POST se emite antes de tener el `locator` de su padre, que los
   hermanos se agrupan en lotes paralelizables, y que un POST sin `category` **se rechaza en el cliente** —porque el
   servidor devuelve 500 y no 400—. 🔵 **El valor: convierte «cotizar la generación de un curso» en un artefacto con
   número de llamadas, que es lo que se pone en una propuesta.**
3. 🔴 **Medir cuántas de las 63 filas de `agents/top.md` quedan expuestas al Artículo 50(2) del 2026-12-02, que vence en
   61 días** (**gap 91**). Es la única de las tres que no es técnica y es la que más valor comercial tiene, porque el
   plazo está dentro del trimestre y esta base no lo tenía. **La acción concreta:** clasificar las 63 filas por una sola
   pregunta —**¿genera contenido sintético que un alumno o un docente va a ver?**— y para las que sí, registrar si el
   repo tiene alguna forma de marcado (C2PA, metadatos, marca de agua, o nada). 🔵 **El resultado esperado es un vacío y
   conviene medirlo antes de que lo pregunte un cliente:** ninguna pieza de esta KB se eligió por su capacidad de
   marcado, así que la respuesta probable es «ninguna», y eso **es** el hallazgo — más una oportunidad de componente
   transversal.

⚠️ **Y las acciones hacia afuera que esta corrida sigue sin poder ejecutar, declaradas para no perderlas:** el `LICENSE`
que falta en `Timadey/proctor` (**un PR de un archivo**); la licencia sin segunda fuente de `@ink-waffle/sisu-mcp`
(**bloqueante: sigue siendo la única puerta de SIS de educación superior de esta base**); el acceso de miembro a los
repositorios de Caliper Sensor API de 1EdTech; y 🔵 **el texto consolidado del Reglamento (UE) 2024/1689, que este pase
volvió a intentar y que sigue inalcanzable por los DOS canales probados** —`eur-lex.europa.eu` y
`artificialintelligenceact.eu`, ambos `403` a CONNECT (**gap 92**)—. **Las fechas quedan confirmadas por segundo canal,
no por fuente primaria, y eso hay que seguir diciéndolo cada vez que se citen.**

## 🔵 Las tres acciones que el pase 43 deja escritas para el pase 44

**Las tres son ejecutables en este entorno: ninguna necesita Docker, ni instalar dependencias de terceros, ni la API de
GitHub.**

1. 🟢 **Completar `operations.tsv` del *gateway* de SEB Server con los 26 controladores que faltan, midiendo la clase
   base de cada uno.** Es la mitad declarada de la tendencia 162, y **la tendencia 159 es la razón por la que no se puede
   adivinar**: hay que leer el `extends` de cada controlador, porque `ReadonlyEntityController` conserva las rutas de
   escritura. **La acción concreta:** un `curl` por controlador a `raw.githubusercontent.com`, extraer `extends` y los
   `@RequestMapping` propios con el mismo script de este pase, y **volver a correr `test_gate.py`** —que debe seguir
   dando verde con una tabla ~6× más grande—. 🔵 **El valor: con eso la puerta de SEB Server deja de cubrir cuatro
   endpoints y cubre el servicio, que es lo que se le propone a un cliente.**
2. 🟢 **Medir el costo de *authoring* del `v1` de Open edX como se midió el de proctoring, y cotizar P55 entero.** Hoy la
   tendencia 158 dice *qué* endpoint usar; falta *cuánto pesa* el cliente. **La acción concreta:** leer
   `cms/djangoapps/contentstore/rest_api/v1/views/xblock.py` completo (ya está en el entorno) más
   `xblock_storage_handlers/view_handlers.py`, y responder **tres preguntas que hoy no tienen número**: qué devuelve
   exactamente `create_xblock_response` (¿el `usage_key` del bloque nuevo, que es lo que hace recursable el recorrido del
   árbol?), qué valores de `category` acepta sin configuración extra, y si `?view=minimal` está disponible en `retrieve`
   únicamente —el docstring dice que sí— o también al recorrer `children`. 🔵 **El valor: es lo único que falta para
   cotizar la generación de un curso entero sin asterisco.**
3. 🟢 **Verificar las fechas revisadas del EU AI Act contra el texto consolidado**, que es la única cifra importante de
   este pase que es de **segunda fuente** (ver la corrección en `intel/market.md`, sección EMEA). **La acción concreta:**
   `eur-lex.europa.eu` por el Reglamento (UE) 2024/1689 y confirmar o refutar **2 de diciembre de 2027** (alto riesgo
   autónomo) y **2 de agosto de 2028** (alto riesgo embebido). 🔴 **Si las fechas no se confirman, la recomendación
   comercial de EMEA de este pase hay que revertirla**, porque está construida sobre el plazo extra. **Es la acción de
   mayor riesgo pendiente**, no la de mayor valor: el resto del pase no depende de ella.

⚠️ **Y las acciones hacia afuera que esta corrida sigue sin poder ejecutar, declaradas para no perderlas:** el `LICENSE`
que falta en `Timadey/proctor` (**un PR de un archivo**); la licencia sin segunda fuente de `@ink-waffle/sisu-mcp`
(**bloqueante: sigue siendo la única puerta de SIS de educación superior de esta base**); el programa de la *2nd Working
Conference* del Consejo de Europa en `coe.int`; y 🔵 **una nueva: pedir acceso de miembro a los repositorios de Caliper
Sensor API de 1EdTech** (tendencia 163), que es el único camino para leer esa capa y hoy **no** está abierto.

## 🔵 Las tres acciones que el pase 42 deja escritas para el pase 43

**Las tres son ejecutables en este entorno: ninguna necesita Docker, ni un host bloqueado, ni el buscador roto de PyPI,
ni la API de GitHub.**

1. 🟢 **Cerrar la mitad abierta del gap 86: escribir y PROBAR la puerta MCP de `seb-server`, que es la única de las dos
   capas institucionales que sigue sin puerta.** El trabajo ya está acotado por este pase: **36 controladores, 41
   constantes de *endpoint*, y los nombres de los cuatro APIs de integración de LMS.** **La acción concreta:** generar el
   manifiesto desde `gbl/api/API.java` (las constantes `*_ENDPOINT`, que son datos, no prosa), montarlo sobre el mismo
   *gateway* de **P85**, y 🔴 **verificar ejecutando que los *endpoints* de escritura de `/exam`, `/lms-setup` y
   `/useraccount` quedan fuera con `-32601`**, además de los de `/batch-action`. ⚠️ **Contra un *stub*, igual que P92:
   no hace falta levantar SEB Server.** 🔵 **El valor: con las dos puertas escritas, esta base puede proponer la capa de
   examen completa —horarios y supervisión— con licencia usable y sin competencia agéntica.**
2. 🟢 **Medir el COSTO de los 12 métodos obligatorios de `RemoteProctoringService`, que es el número que falta para
   cotizar P91.** Hoy esta base sabe *cuántos* métodos hay que escribir pero no *cuánto pesan*. **La acción concreta:**
   leer `JitsiProctoringService` y `ZoomProctoringService` —las dos implementaciones de referencia— y **contar líneas por
   método, dependencias externas por método y cuántos de los 12 son triviales** (devuelven un `Map` de constantes, como
   `getDefaultReconfigInstructionAttributes`) **contra cuántos hablan con un servicio remoto**. 🔵 **El valor es directo:
   P91 hoy dice «12 métodos» y una propuesta necesita «12 métodos, de los cuales N triviales y M con integración
   remota».** **Las dos implementaciones están en el clon y no hace falta red.**
3. 🟢 **Cerrar el gap 90 con código, no con una advertencia: escribir la validación de campos que SEB no aplica a un
   proveedor de terceros.** El pase midió que el validador cae a `return true`. **La acción concreta:** escribir el
   `ConstraintValidator` propio para un `ProctoringServerType` nuevo, siguiendo la forma exacta de
   `ProctoringSettingsValidator` (plantillas `proctoringSettings:<campo>:notNull`), y **probar por ejecución que un
   settings incompleto es rechazado y uno completo aceptado**. 🔵 **El valor: convierte el gap 90 de «alcance que hay que
   avisar» en «pieza que ya existe», que es la diferencia entre una advertencia y un entregable.**

⚠️ **Y las dos acciones hacia afuera que esta corrida sigue sin poder ejecutar, declaradas para no perderlas:** el
`LICENSE` que falta en `Timadey/proctor` (**un PR de un archivo**, y el árbol ya dice MIT tres veces) y la licencia sin
segunda fuente de `@ink-waffle/sisu-mcp` (**bloqueante: es la única puerta de SIS de educación superior de esta base**).
🔵 **Se suma una tercera, nueva y de alto valor: pedirle a alguien con acceso a `coe.int` el programa de la *2nd Working
Conference* del Consejo de Europa** — es la primaria regulatoria educativa de EMEA y este entorno no la alcanza.


## 🔵 Las tres acciones que el pase 41 deja escritas para el pase 42

**Las tres son ejecutables en este entorno: ninguna necesita Docker, ni un host bloqueado, ni el buscador roto de PyPI, ni
la API de GitHub.**

1. 🟢 **Escribir y PROBAR la puerta MCP de UniTime, que es el hueco que este pase midió vacío y la pieza de mayor valor
   comercial pendiente.** El trabajo ya está acotado por la medición: **15 conectores con nombre registrado, verbos
   conocidos y autenticación por token** (`?token=`). **La acción concreta:** generar el manifiesto de *tools* (uno por
   conector × verbo), **montarlo sobre el *gateway* de allowlist que el pase 40 dejó probado (P85)** y 🔴 **verificar
   ejecutando que `script` y los verbos de escritura de `rooms`, `buildings` y `events` quedan fuera con `-32601` sin
   llegar al upstream.** 🔵 **El valor: es el único entregable de esta base que llega a una capa con cero competencia
   agéntica, licencia Apache-2.0 y despliegue institucional real.** ⚠️ **Se prueba contra un *stub* que imite la API de
   conectores, igual que el pase 40 probó su *gateway*: no hace falta levantar UniTime.**
2. 🟢 **Re-fechar las 39 filas que faltan con el instrumento corregido, porque el gap 89 dice que el número publicado
   puede estar mal en la dirección peligrosa.** El pase 37 fechó 49 filas por la rama por defecto; este pase probó que
   eso registra como *«frío»* un proyecto que commiteó ayer. **La acción concreta:** correr `ls-remote --heads`,
   **tomar el máximo entre TODAS las ramas y después leer el autor y el mensaje del commit más nuevo**, descartando las
   tres clases que no son vida de proyecto (**commit vacío de bot**, **regeneración de SDK**, **rama de agente sin
   mergear**). 🔵 **El valor es defensivo y es grande: esta base tiene 10 filas marcadas CONGELADO/FRÍO que se usan para
   NO recomendar, y el instrumento que las marcó mide la rama equivocada.**
3. 🟢 **Enumerar la superficie de `seb-server` al nivel que este pase enumeró `edx-proctoring`, para poder cotizar la
   ruta MPL-2.0 contra la ruta Open edX.** Hoy esta base tiene los **36 controladores y los 41 endpoints por nombre**,
   pero **no** tiene lo que sí tiene de la otra ruta: los modelos de estado, el contrato de extensión de proveedor de
   *proctoring* (`ExamProctoringController` sugiere que existe) y si hay *entry point* o interfaz de plugin. **La acción
   concreta:** clonar `dev-3.0` —**no `master`, por el gap 87**— y enumerar las interfaces de
   `webservice/servicelayer/` (empezando por `FullLmsIntegrationAPI`, `SEBRestrictionAPI`, `CourseAccessAPI` y
   `LmsAPITemplate`, que ya aparecieron en el listado de archivos). 🔵 **El valor: hoy se puede cotizar la ruta Open edX
   con números y la ruta SEB sólo con adjetivos, y la ruta SEB es la que no arrastra AGPL.**

⚠️ **Y una acción que esta corrida NO puede ejecutar, que queda con destinatario humano y conviene no perderla:** el
`LICENSE` que falta en `Timadey/proctor` y la licencia sin segunda fuente de `@ink-waffle/sisu-mcp` **se cierran
escribiéndole a sus autores** (un *issue* o un correo). **Es una acción hacia afuera, sobre el repositorio de un tercero,
y no la decide un pase automático.** 🟢 **Para `Timadey/proctor` el pedido es trivial y además es una contribución: el
árbol ya dice MIT tres veces y apunta al archivo que falta — es un PR de un archivo.** 🔴 **Para `sisu-mcp` es
bloqueante y vale la pena: es la única puerta de SIS de educación superior de esta base.**

## 🔵 Estado de gaps al cierre del pase 40 del 2026-10-02

**Este pase ejecutó las TRES acciones del pase 39. Las tres rindieron, y la primera rindió descubriendo que el
instrumento que iba a usar estaba roto.**

| Gap | Estado | Resolución |
|---|---|---|
| **Acción 1** (barrer por registro las capas no barridas) | ✅ **CUMPLIDA — y con el instrumento rehecho a mitad de camino** | **28 términos × 4 registros.** 🔴 **El procedimiento de PyPI del pase 39 está roto y devuelve `200`** (tendencia **141**); 🟢 **reemplazado por `pypi.org/simple/` — 903.402 nombres** (tendencia **142**). **6 altas, 11 homónimos rechazados, 5 capas confirmadas vacías de agente** |
| **Acción 2** (fracción portable de `mcp-usc` y `DUTIC-mcp`) | ✅ **CUMPLIDA — y el resultado es opuesto en las dos** | **`mcp-usc`: 80 de 91 (88 %) genéricas**, candado en 2 archivos, host en `os.getenv`. **`DUTIC-mcp`: 1 de 12 (8 %)**, host en `export const`. 🟢 **Y aparece el activo no contado: catálogo de 306 funciones de Moodle WS, MIT** (tendencia **145**) |
| **Acción 3** (*gateway* de partición de tools) | ✅ **CUMPLIDA Y PROBADA, no descrita** | **175 líneas, sólo stdlib.** Verificado contra un upstream que imita `frappe-mcp-server`: `tools/list` **7 → 3**, `delete_document` y `call_method` **bloqueados con `-32601` sin llegar al upstream** (1 ejecución total), **allowlist vacía → 0 tools**. Log JSONL con `exposed`/`withheld`. Ver **P85** |
| **NUEVO 82** (el buscador de PyPI falla con `200`) | 🔴 **ABIERTO como límite de entorno — pero MITIGADO** | A diferencia de los gaps 58, 65, 72 y 80, **éste tiene reemplazo y mejor que el original**: el índice `simple`. **Lo que queda abierto es la búsqueda por DESCRIPCIÓN en PyPI**, que el índice no cubre. **Regla nueva obligatoria: todo raspado lleva control de contenido, no sólo de código de estado** |
| **NUEVO 83** (licencia contradictoria entre manifiesto y árbol) | ⚠️ **ABIERTO como clase de evidencia — y es distinta del 81** | `exam-guard`: **ISC** en npm contra **Apache-2.0** en el árbol. **Difieren en la cláusula de patentes.** Manda el árbol; la pieza **no se usa en un entregable** hasta que el autor resuelva. El **gap 81 invertido** también aparece: `student-success-tool` **no declara licencia en PyPI** y es **MIT** en el árbol (tendencia **146**) |
| **26** (capa predictiva / que decide sobre el alumno, «la peor abastecida») | 🟢 **REFORMULADO — y la reformulación es a favor** | **No faltaba el modelo: faltaba el expediente.** `datakind/student-success-tool` (**MIT**, Google.org) trae ***model cards*, secciones de análisis de sesgo, validación de ingesta y datos sintéticos** en el árbol, con *«humans in the loop by design»*. **Pasa de «construir lo que falta» a «adoptar y adaptar el esquema»**, que es una propuesta muy distinta (tendencia **148**) |
| **NUEVO 84** (*proctoring*: no hay opción permisiva) | 🔴 **ABIERTO, y medido** | La capa queda cerrada y **la única pieza seria es `openedx/edx-proctoring`, AGPL-3.0**. Las dos piezas MIT (`mereos`, `@timadey/proctor`) son **SDK de detección del lado navegador**: resuelven la visión por computadora, **no** la integración con estados de examen, excepciones y auditoría. **Sobre Open edX la AGPL no agrega fricción; fuera de Open edX la capa de integración hay que construirla** |
| **NUEVO 85** (*timetabling*: el servidor que nunca se publicó) | 🔴 **ABIERTO, con una pista concreta** | `ucleeds-mcp-tester` (**MIT**, 1 release 2025-04-25, sin repo) es *«Test client for UCLeeds Timetabling MCP integration»*. **El cliente se publicó, el servidor no.** Y 🔴 **`unitime` no está en PyPI** (0 de 903.402): el inventario de esta capa hay que hacerlo **por sitio de proyecto** |
| **81** (licencia sólo en el manifiesto) | ⚠️ **ABIERTO y con una instancia más** | `@timadey/proctor` (**MIT** sólo en npm, sin `LICENSE` en 5 rutas × 2 ramas). Entra con reserva explícita, igual que `sisu-mcp` y `frappe-mcp-server` |
| **140** (el campo `repository` no prueba que el repo exista) | ⚠️ **CONFIRMADO con una cuarta instancia** | `timeback-caliper` (**55 releases**, MIT declarada) declara `superbuilders/timeback-dev-python` y **`git ls-remote` falla**. **Se registra, no se recomienda** |
| **56** (tendencia: el LRS más instalado está congelado) | ✅ **CONFIRMADO por un TERCER canal independiente** | `@learninglocker/xapi-agents`: **última publicación 2019-07-11**. Antes se había medido por repo y por sitio; ahora también **por registro de paquetes** |
| **65** (primarias legales / multilaterales) | 🔴 **ABIERTO, sin avance deliberado** | Las tres acciones del 39 tenían prioridad. **El calendario del AI Act se citó otra vez por el canal del buscador**, y 🔴 **la fecha vencida reapareció por OCTAVA vez** en el barrido de North America. **El número de reglamento sigue sin verse en EUR-Lex** |
| **60** (mitad QTI) / **61** (curso origen vacío) / **68** (release de la puerta de Open edX) / **80** (sin Docker) | 🔴 **ABIERTOS, sin avance deliberado** | Las tres acciones del 39 tenían prioridad. **El 80 no se reintenta: el pase 39 dejó escrito «no insistir por esta vía»** |

## 🔵 Las tres acciones que el pase 40 deja escritas para el pase 41

**Las tres son ejecutables en este entorno y ninguna depende de un host bloqueado, de Docker ni del buscador roto de
PyPI.**

1. 🟢 **Cerrar el inventario de las dos capas cuyas piezas canónicas NO están en ningún registro, por sitio de
   proyecto en vez de por registro.** El pase 40 midió que **`unitime` y `safe-exam-browser` devuelven cero nombres en
   los 903.402 de PyPI** y que la capa de *timetabling* sólo deja como traza un cliente de prueba huérfano
   (**gap 85**). **La acción concreta:** ir a **UniTime** y a **Safe Exam Browser** por su repositorio, medir licencia
   del archivo, `HEAD`, tags y superficie de API, **y responder si alguno expone una API envolvible como MCP**. 🔵 **El
   valor es que son las dos capas donde esta base acaba de probar que no hay competencia agéntica**, y las dos tienen
   despliegue institucional real. **Es el barrido que la tendencia 142 dejó pendiente por construcción: el índice de
   un registro no encuentra lo que no está en el registro.**
2. ⚠️ **Resolver las dos contradicciones de licencia abiertas, que son baratas y bloquean entregables.** Son tres
   piezas y tres acciones distintas: (a) **`exam-guard`** → la contradicción **ISC contra Apache-2.0** (gap 83) se
   resuelve leyendo **el `package.json` del árbol** —no el del registro— y el historial de ese archivo, para saber
   **cuál de las dos es la intención actual del autor**; (b) **`@timadey/proctor`** y (c) **`@ink-waffle/sisu-mcp`**
   (gap 81) → abrir *issue* o correo pidiendo el `LICENSE` en el árbol. 🔵 **El valor es de desbloqueo: `sisu-mcp` es
   la única puerta de SIS de educación superior de esta base y hoy no se puede proponer por un archivo que falta.**
3. 🟢 **Medir la superficie real de `edx-proctoring` y decidir si la capa de *proctoring* se cotiza entera o partida,
   que es la acción de mayor valor comercial pendiente.** El pase 40 estableció que es la **única pieza seria de la
   capa** y que es **AGPL-3.0 con 17 meses sin release** (gap 84, tendencia 147). **La acción concreta:** bajar el
   *wheel* de PyPI —que es el método que el pase 31 dejó probado para Open edX, sin Docker y sin instalar
   dependencias— y **enumerar sus modelos de estado de examen, sus endpoints REST y sus puntos de extensión de
   proveedor**, para responder **si integrar un *proctoring* propio es implementar una interfaz existente o escribir
   la capa desde cero**. 🔵 **De eso depende si la capa se propone sobre Open edX (adopción, AGPL ya aceptada) o fuera
   (desarrollo), y hoy esta base no lo sabe.** ⚠️ **Y antes de cualquiera de las dos rutas va el expediente del Anexo
   III punto 3, cuyo plazo es el 2027-12-02**: el *«monitoreo durante exámenes»* está nombrado en el inciso.

## 🔵 Estado de gaps al cierre del pase 39 del 2026-10-02

**Este pase ejecutó dos de las tres acciones del pase 38 completas, y la tercera la frenó el entorno, no el método.**

| Gap | Estado | Resolución |
|---|---|---|
| **54** (¿hay ausencias ya cerradas por su propio proyecto?) | ✅ **CERRADO — la acción 1 rindió ocho altas** | **El canal faltante era el registro consultado por nombre de PROYECTO.** 23 términos × 4 registros → **8 piezas que 38 pases de GitHub no vieron**, **5 homónimos rechazados** y **9 ausencias confirmadas por segundo instrumento**. 🔴 **Y la corrección que trajo: la ausencia de educación en la capa MCP brasileña era falsa** |
| **56** (calendario del Anexo III) | ✅ **CERRADO — y las «dos fechas incompatibles» nunca estuvieron en conflicto** | Ver abajo: fechan **dos obligaciones distintas**. Educación es **Anexo III, punto 3**; el aplazamiento es **Reglamento (UE) 2026/1744** (DOUE **2026-07-24**, en vigor **2026-07-27**): Anexo III → **2027-12-02**, Anexo I → **2028-08-02**. 🔴 **El Artículo 50 NO se aplazó y rige desde el 2026-08-02** |
| **69 / tendencia 114** (educación ausente de la capa MCP brasileña) | 🔴 **CORREGIDO — la afirmación era falsa en su mitad de ausencia** | `dasgltd/mcp-brasil` (**MIT**) tiene **2 de 15 datasets** en educación y **13 tools** de ENEM y Censo Escolar. 🟢 **La mitad de arquitectura sí era correcta y queda confirmada por una implementación:** no hay API del INEP, se descargan los ZIP de microdatos. **P77 deja de ser presupuesto de construcción y pasa a adopción + extensión** |
| **79** (¿cuál `edfi-oneroster` es *upstream*?) | ✅ **CERRADO en dos comandos** | `merge-base` = tip de `CSR2017`; **3 adelante / 0 atrás** a favor de `Ed-Fi-Alliance-OSS`. **`CSR2017` es un espejo estrictamente atrasado**, 8 tags contra 86, y su tip es un commit de bot (tendencia 138) |
| **Residuo del pase 38** (`moodler-mcp` sin enumerar) | ✅ **CERRADO, con dos correcciones** | **38 tools = 30 lectura + 6 escritura de alumno + 2 docente.** 🔴 **Es Python, no TypeScript** (la fila decía mal). 🔴 **Y publica la nota** (`workflowstate=""`), al revés de `moodle-grading-mcp` |
| **NUEVO 80** (sin *daemon* de Docker) | 🔴 **ABIERTO — límite de entorno, como el 65 y el 72** | **La acción 2 del pase 38 no se pudo ejecutar**: `/var/run/docker.sock` no existe (el binario `docker` sí). Los **gaps 52 y 55** siguen medidos **en papel y en código fuente, no en protocolo**. **Sustituto adoptado y ya en uso: contar en el tarball publicado o en el árbol** (tendencias 94 y 139). **No insistir por esta vía** |
| **65** (primarias legales / multilaterales) | 🔴 **ABIERTO — y este pase lo extiende a una TERCERA clase** | **Las fuentes legales primarias de la UE** quedan confirmadas bloqueadas con el instrumento del pase 36: `eur-lex.europa.eu`, `ai-act-service-desk.ec.europa.eu`, `digital-strategy.ec.europa.eu` y `artificialintelligenceact.eu` **resuelven DNS y devuelven 000**, con control positivo (`registry.npmjs.org` → 200). **El dato del AI Act de este pase vino por el buscador** (tendencia 130) |
| **70** (envoltorio MCP de QTI) | ✅ **sigue cerrado como especificación — y ahora se sabe que nadie se adelantó** | El barrido de `qti assessment` en los **cuatro** registros devuelve **un solo hit y es homónimo**. **Las 20 tools de P76 siguen siendo la contribución *upstream* más limpia identificada por esta base** |
| **60** (mitad QTI) / **61** (curso origen vacío) / **68** (release de la puerta de Open edX) | 🔴 **ABIERTOS, sin avance deliberado** | Las dos acciones ejecutables del 38 tenían prioridad. El 68 se **reconfirmó de paso**: `tutor-contrib-openedxmcp` sigue en **0.1.7 del 2026-07-25** (**69 días**), **AGPL-3.0** |
| **NUEVO 81** (licencia declarada sólo en el manifiesto del registro) | ⚠️ **ABIERTO como clase de evidencia, no como falla** | `@ink-waffle/sisu-mcp` (MIT) y `frappe-mcp-server` (ISC) **no traen `LICENSE` en el tarball ni repo legible**. **Entran con reserva explícita** y no como equivalentes a las que tienen texto (tendencia 129). **Para `sisu-mcp` se cierra con un correo al autor**, que es la única puerta de SIS de esta base |

## 🔴 El gap 56, resuelto — y la lección es que el error nunca estuvo en las fechas

**Esta base tenía publicadas dos fechas y las trataba como contradictorias:** *«2027-12-02»* (pase 11, luego pase 36) y
*«rige desde 2026-08-02»* (pase 28), **y sobre la segunda se construyó argumentación de venta para EMEA.** El pase 38
dejó escrito que había que fechar cada afirmación **por el inciso del Anexo III** que le corresponde.

🟢 **Hecho eso, las dos fechas son correctas y fechan obligaciones DISTINTAS. No había contradicción: había una
afirmación sin calificar.**

| Obligación | Fecha de aplicación | Estado |
|---|---|---|
| **Artículo 50** — transparencia (interacción con IA, marcado de contenido sintético, *deepfakes*, reconocimiento de emociones) | **2026-08-02** | 🟢 **EN VIGOR. NO se aplazó.** Es **independiente del nivel de riesgo**: alcanza al chatbot educativo aunque no sea de alto riesgo |
| **Anexo III** — alto riesgo autónomo, **educación es el punto 3** (acceso y admisión, asignación de alumnos, evaluación de resultados de aprendizaje y exámenes, **monitoreo durante exámenes**) | **2027-12-02** (antes 2026-08-02) | ⚠️ **APLAZADO** por el **Reglamento (UE) 2026/1744** |
| **Anexo I** — alto riesgo embebido en producto ya regulado (dispositivos médicos, maquinaria, vehículos) | **2028-08-02** | ⚠️ Aplazado. 🔴 **Un LMS no es Anexo I**: *«embebido en un LMS»* **no mueve el plazo** |

**El aplazamiento es derecho vigente, no propuesta** — y esta es la parte que faltaba fechar: el *Digital Omnibus on
AI* fue **aprobado por el Parlamento Europeo el 2026-06-16**, **adoptado por el Consejo el 2026-06-29**, firmado el
**2026-07-08**, **publicado en el DOUE el 2026-07-24** y **en vigor desde el 2026-07-27**, como **Reglamento (UE)
2026/1744**. El motivo declarado por la Comisión: ni la industria ni **CEN/CENELEC** llegaban con las normas
armonizadas, y la infraestructura de evaluación de conformidad que el Reglamento presupone no había madurado.

🔵 **Cómo se dice esto en una propuesta EMEA, que es para lo que importa:** *«hoy ya le aplica una obligación de
transparencia (Art. 50, vigente desde agosto de 2026) y tiene hasta diciembre de 2027 para la conformidad de alto
riesgo del Anexo III punto 3»*. 🔴 **Lo que NO se puede seguir diciendo es «el alto riesgo rige desde agosto de
2026»**, y lo que tampoco conviene decir es *«tiene tiempo»*: la seudonimización de `bruchris/canvas-lms-mcp` y el
`readyforreview` de `moodle-grading-mcp` **ya existen hoy en piezas MIT** (tendencia 136), así que la pregunta
razonable del cliente es por qué no están puestas.

🔴 **Límite de fuente, declarado:** las cuatro fuentes primarias (DOUE/EUR-Lex y la Comisión) **están bloqueadas en
este entorno** (gap 65) y el texto consolidado **no se leyó**. Lo anterior viene del **canal del buscador**
(tendencia 130), con **la coincidencia de varias fuentes secundarias independientes** sobre el número de reglamento,
las fechas del procedimiento y las dos fechas de aplicación. **Antes de citar el número de reglamento en un documento
contractual, hay que verlo en EUR-Lex desde una red sin este bloqueo.**

## 🔵 Las tres acciones que el pase 39 deja escritas para el pase 40

**Las tres son ejecutables en este entorno y ninguna depende de un host bloqueado ni de Docker.**

1. 🟢 **Correr el barrido por REGISTRO sobre las capas que este pase NO barrió, porque el canal ya demostró que
   encuentra lo que GitHub esconde.** Este pase gastó sus 23 términos en LMS, SIS, estándares y biblioteca. **Quedan
   sin barrer por registro: *proctoring*, *timetabling*, analítica de aprendizaje (Caliper/xAPI por nombre de
   herramienta, no de estándar), admisiones, *student success* y accesibilidad** — y las dos últimas son, por
   declaración propia de esta base, **las peor abastecidas de toda la KB**. **El procedimiento está escrito y es
   repetible** (cuatro endpoints, en `repos/trending.md` de este pase); lo único que falta es la lista de términos.
2. ⚠️ **Medir qué fracción de `mcp-usc` y `DUTIC-mcp` es PORTABLE, porque de eso depende si se reusan o sólo se leen.**
   Las dos son institucionales (USC, UNSA) y las dos mezclan **tools genéricas de Moodle Web Services** con **tools
   atadas a fuentes locales** (`list_usc_degrees`, `get_my_official_exam_schedule`, `dutic_semester_discover`). **La
   acción concreta: clasificar las 91 + 12 tools en «sólo Web Services» contra «fuente institucional», que se lee en
   el import de cada módulo.** 🔵 **El valor es de cotización: la fracción genérica es reuso y la otra es desarrollo**,
   y hoy esta base no sabe la proporción en la pieza de 91 tools que acaba de admitir.
3. 🟢 **Escribir el *gateway* de partición de tools que la tendencia 137 vuelve posible, porque es chico y desbloquea
   los casos donde hoy no se puede proponer escritura.** El patrón `preview_*` de `mcp-usc` demuestra que **un filtro
   por nombre de tool es un control de cumplimiento real**, no cosmético. **Lo que falta es la pieza intermedia:** un
   *proxy* MCP que reexporte sólo las tools de una allowlist y **registre cada llamada bloqueada**. Sirve para las
   nueve puertas de LMS de esta base, **y es obligatorio delante de `frappe-mcp-server`**, que trae `call_method` y
   `delete_document` sin partición por rol. Ver **P82**, **P83** y **P84**.

## 🔵 Las tres acciones que este pase deja escritas para el siguiente

1. **Medir los endpoints `v0` de *authoring* de Open edX** (**gap 50**), que son los que el propio repo recomienda sobre
   el `v1` experimental. Concretamente: leer `cms/djangoapps/contentstore/rest_api/v0/urls.py` y los `views/` que
   cuelgan, por `raw.githubusercontent.com`, y responder **si `v0` cubre crear/actualizar curso, secciones y
   componentes**. Es lo que decide si el **gap 50** es un bloqueo real o un desvío de versión — y con eso **P55 se
   cotiza entero o se cotiza partido**. **Es la acción de mayor valor comercial pendiente**, porque Open edX es la base
   de la huella pública grande de **LATAM e India**.
2. **Re-medir con el método nuevo las ausencias que esta KB declaró por etiqueta** (tendencia **73**). El método que
   funciona es **estándar + `SDK`/`client`/`library` + abrir el README y buscar «MCP» adentro**. Prioridad por valor:
   **Open Badges** (`openbadges` SDK/validator — y esta KB ya sabe que CaSS lo excluye a propósito y que su
   implementación es **OB 2.0, no 3.0**), **Caliper** (aunque el estándar dejó de ser open source en 2023-06-17, los
   SDK previos siguen publicados) y **LTI** (`ltijs`, `pylti1p3` — si alguno sumó MCP, el **gap 42**, cerrado por
   agotamiento en el pase 27, **se reabre por una vía que nadie revisó**). Y **CASE por nombre desambiguado**
   (`"Competencies and Academic Standards Exchange"`, no la sigla) para cerrar el **gap 51**.
3. **Cerrar el tramo de invocación del gap 40 donde esté permitido instalar dependencias de terceros**, sin cambios
   respecto del pase 27: `npm install` en `cassproject/CASS`, un Elasticsearch en `:9200`, **verificar primero la
   trampa del loopback** (`CASS_LOOPBACK`, porque si el `fetch` falla la ruta no se monta y el síntoma parece otro), y
   después `initialize` + `tools/list` contra **`POST /api/mcp`**. **Comparar con las 6 declaradas.** Si coinciden,
   **P50, P54 y P57 se cotizan sin asterisco**. 🔵 **Y agregar al mismo entorno la verificación de `oneroster-ts`**:
   `npx` el SDK como servidor MCP y contar las tools reales contra los **164 métodos declarados**, que es la única
   cifra grande de este pase que no es de primera mano.

## Nota de método del pase 27 (2026-10-01) — el pase que no pudo ejecutar y por eso midió lo mismo por otro canal, y el que corrigió la premisa de su propio pase anterior

**Lo que se hizo:** el barrido obligatorio completo —**cuatro búsquedas globales y cuatro regionales**, con el año
**calculado** (2026)— más las **tres acciones** que el pase 26 dejó escritas. Dos se ejecutaron y dieron resultado; la
primera quedó bloqueada **por un límite nuevo**, y es lo primero que hay que declarar.

### 🔴 El bloqueo de la acción 1 se movió, y el nuevo límite no es de infraestructura

El pase 26 no pudo hacer el *handshake* MCP porque **no hay demonio de Docker** y Elasticsearch no se podía levantar.
Este pase localizó el camino —`src/main/server/util.js` muestra que el *probe* sólo pide `GET /` y
`GET /_cluster/health` en `yellow`/`green`, y `src/main/server.js:452` muestra que **los cartuchos se cargan en el
evento `listening`, antes de que la migración termine**, así que la ruta podía existir mientras el *probe* reintenta—
pero **se detuvo antes**: para arrancar el servidor hay que instalar el árbol de dependencias de CaSS, y en este
entorno **instalar dependencias de un repositorio de terceros no está permitido** (la operación fue rechazada como
*código externo*). **No se intentó eludirlo.**

**Es un límite distinto del de todos los pases anteriores, y conviene anotarlo como tal:** los bloqueos registrados
hasta acá eran **del proxy de egreso** (dominios inalcanzables) o **de infraestructura** (sin Docker). Éste es **del
entorno de ejecución**, y **no se levanta consiguiendo una red mejor**: se levanta corriendo el pase donde esté
permitido instalar y ejecutar código de terceros. Lo mismo bloqueó, de paso, la verificación del *launch* LTI.
**`artifacts.elastic.co` responde 403** por el proxy, así que la vía del tarball tampoco estaba.

### Lo que se hizo en su lugar, y por qué el resultado vale

En vez de dejar la acción sin resultado, se midió **la misma cosa por el canal que sí estaba disponible**: **contar las
anotaciones `x-mcp-*` en el código fuente clonado**. Eso da:

- ✅ **Las seis tools confirmadas nombre por nombre**, por un método independiente del que usó el pase 26
  (conteo estático vs. ejecución del generador). **Dos canales, el mismo resultado.**
- ✅ **Una corrección**: las ocultas son **55**, no 45. El 45 era **`51 paths − 6 tools`**, y `x-mcp-ignore` se declara
  **por operación**. 61 operaciones en 51 paths.
- ✅ **El desglose por adaptador**, que la ejecución del generador no daba y que es lo que se cotiza (tendencia 72).
- ✅ **Una trampa de despliegue** que nadie había registrado: el adaptador carga el spec **por loopback**
  (`CASS_LOOPBACK`, default `http://localhost/api/`) y **si ese `fetch` falla hace `return` sin montar `/api/mcp`**,
  con el servidor arrancando normalmente. Falla **en silencio**.

**Lo que sigue sin estar medido, dicho sin ambigüedad:** **nadie hizo `initialize` + `tools/list` contra
`POST /api/mcp`.** La superficie está confirmada **por declaración en el código, dos veces**; **no por invocación**.
Para P50, P54 y P57 eso alcanza para cotizar el catálogo y **no** alcanza para prometer latencia, forma de respuesta ni
comportamiento de sesión.

### Canal de verificación — confirmado otra vez, y con un control negativo

🔴 **`curl -sI` no verifica nada contra `github.com` en este entorno, y este pase lo probó con un control negativo que las pasadas anteriores no tenían.** Se chequearon cuatro URLs: las **tres reales** y la **inexistente** (`Snaw80/mcp-moodle`). **Las cuatro devolvieron `403`.** Es decir: el 403 del proxy **no distingue un repo vivo de uno que no existe**, y usarlo como verificación habría registrado un repo fantasma como hallazgo. **WebFetch sí discrimina**: devolvió la página real de las tres y **`HTTP 404 Not Found`** de la cuarta. **Toda la verificación de este pase se hizo por WebFetch**, y la regla de la KB —verificar antes de escribir— se cumple por ese canal, no por `curl`. Confirma lo que los pases 23 a 26 venían anotando, ahora con la prueba en los dos sentidos.

### Las dos acciones que sí se ejecutaron

**Acción 2 (eje conector), ejecutada entera y es la que corrigió al pase anterior.** Open Badges, SCORM, Caliper y el
equivalente de Open edX. Resultado: **dos conectores MIT de Moodle que el pase 26 no vio** (tendencia 69), **uno de
SCORM** (MIT, 3 tools, offline), **ausencia confirmada en Open edX** por búsqueda extendida (gap 48), **ausencia en
Caliper** —consistente con que dejó de ser open source el 2023-06-17— y **ausencia en Open Badges por búsqueda, pero
exclusión deliberada medida en CaSS** (tendencia 72). **Tercera colisión de término de esta KB**: `MCP` + *badges*
devuelve generadores de *badges* de README.

**Acción 3 (gap 42), ejecutada y el gap cierra.** `1EdTech/ltibootcamp` (127 ★, 19 forks, 47 commits) **no es la
implementación de referencia**: es una **colección de enlaces**, y **sin licencia declarada**. El código Ruby de la RI
de 1EdTech está **detrás de la membresía de Contributing Members**. Con eso, *«no existe implementación platform-side
permisiva y productiva»* pasa de **medido sobre seis** a **cerrado**.

### Lo que este pase NO hizo, declarado como tal

- **No hizo el *handshake* MCP** (arriba). El gap 40 **vuelve a abrirse en su tramo de invocación**.
- **No verificó `edumints SCORM MCP`**: aparece listado en un directorio **sin repositorio de GitHub localizable**, y
  por la regla de la KB **no se registra como hallazgo**.
- **No verificó estrellas, forks ni commits de `vishalsachdev/canvas-mcp`** de primera mano en este pase: se
  re-verificó que es **MIT** y que **el conteo de tools varía por versión**. Las cifras «269 ★, 815 commits,
  102–103 tools» del pase 26 **quedan sin reconfirmar**, y el conteo de tools **no debe citarse como número fijo**.
- **No midió el *bulk* de Open Badges ni de CASE por REST**: se midió que **no están en MCP**, no cómo se comportan por
  fuera.
- **No cerró los gaps 36 y 38** (cadena de `lrsql`): sin ejecución de dependencias de terceros, siguen bloqueados.
- **`Snaw80/mcp-moodle` dio 404** y no se registra. Es el **segundo falso positivo del canal de búsqueda** en dos
  pases (el pase 26 tuvo `WalaEddine01/OrgSchool-portfolio-project`).

## 🔵 Las tres acciones que este pase deja escritas para el siguiente

1. **Construir el conector MCP de Open edX, o medir por qué nadie lo hizo** (gap 48). Es la acción de mayor valor
   comercial de esta KB en este momento: **el LMS con la huella pública más grande de LATAM e India es el único sin
   puerta de agente**, y la arquitectura **ya está resuelta dos veces** (Canvas y Moodle). Lo concreto para el próximo
   pase: **verificar si Open edX expone una API REST suficiente** —`openedx/edx-platform`, APIs de *Course Blocks*,
   *Enrollment*, *Grades* y Studio (CMS)— y **si existe el equivalente de los Web Services de Moodle como superficie
   estable y versionada**. Si lo hay, **P55** se cotiza; si no lo hay, **esa es la razón de la ausencia** y es un
   hallazgo igual de bueno.
2. **Repetir el eje conector con la regla de muestreo nueva** (tendencia 69), que es lo único que este pase probó que
   funciona: **no preguntarle a un directorio de MCP, preguntarle al host del repositorio por patrón de nombre.**
   Concretamente, repetir **OneRoster, QTI y CASE** —las tres que el pase 26 declaró vacías **consultando un
   directorio**— buscando `*-mcp`, `mcp-*` y `mcp-server` + el nombre del estándar. **Dos de las tres ausencias de ese
   pase podrían ser del mismo tipo que la de Moodle**, y cuesta una búsqueda descubrirlo.
3. **Cerrar el tramo de invocación del gap 40 donde esté permitido instalar dependencias de terceros**: `npm install`
   en `cassproject/CASS`, un Elasticsearch cualquiera en `:9200` (el *probe* sólo pide `GET /` y salud
   `yellow`/`green`), `CASS_LOOPBACK` apuntado al puerto real —**y verificar primero la trampa del loopback**, porque
   si ese `fetch` falla la ruta no se monta y el síntoma parece otro— y después `initialize` + `tools/list` contra
   **`POST /api/mcp`**. **Comparar con las 6 declaradas.** Si coinciden, P50, P54 y P57 se cotizan sin asterisco.

## Nota de método del pase 26 (2026-10-01) — el pase que ejecutó sin poder levantar el servidor, y el que midió un «no existe» sobre seis candidatos en vez de sospecharlo sobre dos

**Dos resultados de método, y el segundo vale más que el primero.**

**1. Cuando la ejecución está bloqueada, hay que buscar el eslabón puro y ejecutar ése.** El **gap 40** pedía levantar
el cartucho MCP de CaSS. El camino obvio —arrancar el servidor— está cerrado: necesita Elasticsearch y en este entorno
**no hay demonio de Docker** (el CLI está instalado, `/var/run/docker.sock` no existe). El pase 25 habría escrito
*«bloqueado»* y habría tenido razón. **Pero la generación de tools no depende del servidor:** `generateTools(spec)` es
una función pura sobre el OpenAPI, y el OpenAPI lo arma `swagger-jsdoc` leyendo los comentarios del código, **sin base
de datos**. Replicando las opciones exactas de `src/main/server.js` y validando con el mismo
`openapi-schema-validator` del arranque, el generador real corrió y devolvió **6 tools y 3 resource templates**.

**La regla que deja, y es la contracara de la regla del pase 24:** el pase 24 estableció que *cuando una conclusión
depende del comportamiento de una pieza de terceros, la inferencia no alcanza y hay que ejecutar*. Este pase agrega la
otra mitad: **cuando ejecutar el todo está bloqueado, hay que preguntarse qué parte del todo es pura — y ejecutar esa.**
Casi siempre existe un eslabón determinista (un generador, un parser, un validador) que no necesita la infraestructura
que falta. **No es una medición de segunda: las tres fuentes independientes —el generador ejecutado, la aserción del
test del propio repo (*«exactly 6 tools»*) y las 6 anotaciones `x-mcp-tool-name` del árbol— dan el mismo número.** Lo
que no se midió se dice: el *handshake* MCP real, que sí necesita Elasticsearch.

**2. Un «no existe» sólo vale si se midió el espacio completo, y hay que decir cuántos candidatos.** El pase 24 vio dos
piezas *platform-side* de LTI y escribió, con razón, que la capa estaba sesgada a *tool-side*. Este pase verificó
**seis** candidatos uno por uno —incluyendo instalar `ltijs` desde npm y **leer sus exports** en vez de su
documentación— y pudo pasar de *«parece que no hay»* a **«no hay, sobre seis, y éstas son las razones de cada uno»**.
**La diferencia es comercial, no académica:** lo primero no se puede decir en una reunión; lo segundo es un argumento
con evidencia que justifica presupuestar desarrollo. **Un gap sin denominador es una impresión. Con denominador es un
hallazgo.** Y de paso corrigió un falso positivo del resumen de búsqueda: `macewan-cs/lti` es **MIT** pero es
**tool-side**, no el lado LMS que el resumen sugería.

### Lo que trajo el barrido obligatorio, y es la octava pasada seca para la tabla de agentes

Cuatro búsquedas globales y cuatro regionales, con el año **calculado** (2026). **Cero agentes nuevos por octava vez
consecutiva.** Lo global devolvió la capa genérica (openclaw 385k ★, browser-use, Mem0, AutoGen, dify) y **material
didáctico *sobre* AI** (`ai-engineering-from-scratch`, `free-ai-agents-resources`, listas de repos para «aprender AI
en 2026»). **Ocho pases confirman la medición del pase 23 y conviene sacar la conclusión operativa: el canal de
descubrimiento por la palabra `education` está agotado y seguir pagándolo es desperdicio.** Las altas de las últimas
tres pasadas vinieron, todas, de ejes que no usan esa palabra: **artefacto** (pase 24), **estándar** (pase 25) y
**conector** (pase 26).

⚠️ **Y una cifra del barrido que NO se registró, con el motivo.** El barrido global devolvió un *«Hermes Agent, MIT,
180.000+ ★ desde su lanzamiento en febrero de 2026, el framework OSS de más rápido crecimiento de 2026»*. **No se
registra:** no es educativo, viene de un agregador sin verificación de primera mano, y **esta KB ya se quemó con
conteos de estrellas inflados por el canal** (la corrección del pase 4 del `technology`-KB y la del pase 22 acá). Si
aparece otra vez, se verifica contra la página del repo antes de escribirlo.

### La advertencia de método sobre la verificación de URLs, que contradice la consigna y hay que decir por qué

**La consigna pide verificar cada URL con `curl -sI`. En esta sesión eso produce datos falsos y no se usó.**
`curl -sI` contra `github.com` devuelve **`403` para todas las URLs** —se probó contra cinco, incluidas
`cassproject/CASS` y `DavidLMS/learnmcp-xapi`, que existen y están en esta KB desde los pases 25 y 6— porque el proxy
de egreso corta el `HEAD`. **Verificar con `curl` acá habría marcado como 404 a repos reales**, que es exactamente el
error que la consigna quiere prevenir. **Toda la verificación de este pase se hizo con WebFetch sobre la página del
repo**, leyendo licencia, ★, forks y commits de la página. El único 404 reportado —`Cerebro-Tech/FlightPath`— es un 404
**de WebFetch** sobre una URL que este pase **conjeturó** (FlightPath no publica en GitHub), no la refutación de una
URL citada por una fuente.

### Los dominios bloqueados, que ya son cuatro y sostienen afirmaciones regionales

`unu.edu` (**`EGRESS_BLOCKED`**), **`publications.iadb.org`** (**`EGRESS_BLOCKED`**, nuevo en este pase),
`coe.int` (**HTTP 000**) y `www.iesalc.unesco.org`. 🔴 **Van dos pases con la base de evidencia primaria de LATAM
inalcanzable**, y el dominio que se agregó dolía: el barrido ubicó *«An Enabling Regulatory Framework for Artificial
Intelligence in Latin America and the Caribbean»* (**BID**), que es **la fuente primaria regulatoria regional que esta
KB no tiene**. **Es un límite del entorno, no una laguna de investigación** — y hay que levantarlo desde una red sin
este proxy antes de usar esas cifras con un cliente.

### Lo que este pase NO hizo, declarado como tal

- **No hizo *handshake* MCP** contra el cartucho de CaSS (necesita Elasticsearch → Docker). Se midió generación, no
  invocación.
- **No midió el *launch* LTI de punta a punta**: sin `dotnet`, y `dot.net` bloqueado por el proxy (`CONNECT … 403`).
- **No verificó fecha de último commit** de ninguno de los repos nuevos: la página no la expone de forma legible vía
  WebFetch en esta sesión. Señales de vida usadas: commits totales, forks y ★.
- **No buscó conector MCP para Open edX**, que es el hueco simétrico del **gap 43**. Queda como consigna.
- **No verificó la implementación de referencia de 1EdTech en Ruby on Rails** (platform + tool), que apareció en el
  barrido. Es la última candidata no mirada del **gap 42**.
- **No cerró los gaps 36 y 38** (la cadena de `lrsql`): siguen necesitando `next.jdbc` resuelto, y
  `repo.clojars.org` sigue respondiendo **403** por el proxy, igual que en el pase 25.

## 🔵 Las tres acciones que este pase deja escritas para el siguiente

1. **Hacer el *handshake* MCP real contra el cartucho de CaSS**, que es lo único que falta para que el cierre del gap 40
   sea de punta a punta. **El punto exacto a destrabar está localizado:** el log se detiene en
   *«SkyrepMigrate Waiting for Elasticsearch to appear at http://localhost:9200»* — todos los endpoints ya se bindean
   antes de eso, así que **sólo falta satisfacer ese *probe***. Con un entorno con demonio de Docker
   (`docker compose up -d elasticsearch-cass`, que el repo ya trae) o un ES embebido, levantar el server, hacer
   `initialize` + `tools/list` contra **`POST /api/mcp`** y comparar con las **6** medidas acá. **Si coinciden, P48 y
   P50 se cotizan sin asterisco.**
2. **Seguir el eje conector, que rindió dos veces seguidas, en lo que quedó sin barrer:** `MCP server` +
   **Open Badges**, + **SCORM**, + **Caliper** (acá el hallazgo esperable es la **ausencia**, porque Caliper dejó de ser
   open source el 2023-06-17 — y hay que **escribir la ausencia**). Y **buscar `canvas-mcp` como patrón, no como repo:**
   si existe un conector MIT de 102 tools para Canvas, preguntar explícitamente por el equivalente de **Open edX** (que
   **no se buscó**) — para Moodle ya se sabe que no existe (gap 43).
3. **Cerrar el gap 42 por agotamiento** verificando la **implementación de referencia de 1EdTech en Ruby on Rails**
   (platform **y** tool), que es la última candidata no mirada. Si también es copyleft o material de referencia, el
   *«no existe permisivo y productivo del lado LMS»* pasa de **medido sobre seis** a **cerrado**, y eso habilita decirle
   a un cliente *«el lado plataforma se presupuesta como desarrollo»* con la evidencia completa puesta sobre la mesa.

## Nota de método del pase 25 (2026-10-01) — el pase que ejecutó la consigna entera y volvió con dos falsos negativos propios: el eje artefacto rinde, y lo que más rinde es declarar límites

**Lo que se hizo:** el barrido obligatorio completo —**cuatro búsquedas globales y cuatro regionales**, con el año
**calculado** (2026), no fijado— **más los siete ítems de la consigna del pase 24**: los artefactos `item bank`,
`proctoring`, `timetable` y `competency framework`/CASE, los estándares **Caliper**, **CASE** y **xAPI Profiles**, y la
instrucción específica de *«buscar `LTI platform` explícitamente»*. **Se ejecutaron los siete.**

**Resultado: 18 repos verificados de primera mano, 17 nuevos para esta KB**, 3 tendencias nuevas (**63, 64, 65**), 2 patrones nuevos
(**P48, P49**), 2 gaps nuevos (**39, 40**) y **dos correcciones a conclusiones del pase 24**.

### 🔴 Los dos falsos negativos del pase 24, y los dos tienen la misma causa

| Lo que el pase 24 escribió | Lo que el pase 25 midió | La causa |
|---|---|---|
| *«`LongsightGroup/qti3-core` → **404** […] el repo GitHub con ese nombre no existe»* | ✅ **`LongsightGroup/qti3` existe** — MIT, 667 commits, 12 paquetes, **con *writer* de banco de ítems y migración QTI 1.2/2.x→3** | Se buscó **el nombre del paquete npm** (`@longsightgroup/qti3-core`), no el del repo. El monorepo no lleva sufijo |
| *«`yetanalytics/lrspipe`»* (citado como la pieza de *forwarding*) | **404.** El repo real es **`yetanalytics/xapipe`** (Apache-2.0, 17 ★) | Se buscó **el nombre del producto** (*LRSPipe*), no el del repo |

🔵 **La regla que este pase agrega, y vale para toda la KB:** **el nombre del producto y el nombre del paquete no son el
nombre del repo.** Antes de escribir un 404 como no-hallazgo hay que probar **el nombre corto de la organización** —sin
sufijos (`-core`, `-platform`) y sin el nombre comercial—. Dos de los cuatro no-hallazgos que el pase 24 declaró eran
repos reales, y uno de ellos tenía justamente lo que la consigna del pase 25 estaba buscando. Un no-hallazgo mal medido
**es peor que no buscar**, porque cierra la pregunta.

### ⚠️ Advertencia 1 — dos dominios institucionales bloqueados, y los dos sostienen cifras regionales

`unu.edu`, `coe.int` y `www.iesalc.unesco.org` están **bloqueados por el proxy de egreso** de esta sesión. Eso afecta
directamente a dos datos que van a `intel/market.md`:

- Las cifras del estudio **UNESCO IESALC / UNU-IAS** sobre AI en educación superior en LAC (**87 %**, **74 %**, **45 % vs. 70 %**) vienen de **resúmenes de buscador concordantes**, **no** de la lectura de la fuente primaria. Están etiquetadas como tales en `market.md`.
- La **2.ª conferencia de trabajo del Consejo de Europa** sobre las dimensiones regulatorias de la AI en educación **no se pudo verificar**: queda registrada como **señal sin verificar**, con el dominio bloqueado dicho por su nombre.

### ⚠️ Advertencia 2 — una tensión de fechas en la fuente LATAM que no hay que copiar mal

El mismo estudio aparece con **dos fechas** según el canal: el **trabajo de campo** se declara entre **agosto y octubre de
2025**, y el **lanzamiento** fue durante la **Digital Learning Week 2026** en la sede de UNESCO en París. **Las dos son
correctas y no son la misma cosa.** Una propuesta que cite *«datos 2026»* para una encuesta de campo de **2025** está
sobredatando la evidencia en un año, que en adopción de AI es mucho. Escribir: *«encuesta de 2025, publicada en 2026»*.

### ⚠️ Advertencia 3 — la coincidencia de cifras LATAM es aparente, y mezcla dos poblaciones

El barrido LATAM devolvió **87 %** (instituciones de educación superior con AI en al menos un área, IESALC) junto a
**«100 % de las empresas usará AI en al menos una actividad»** y **«85 % de las empresas la integra nativamente»**. **No
son la misma medición ni la misma población:** una es de **universidades**, las otras de **empresas**. Promediarlas o
usarlas de refuerzo mutuo en una propuesta es un error de lectura. La cifra que sirve para un *engagement* educativo es
la de **instituciones**.

### Lo que este pase NO hizo, declarado como tal

- **No levantó `LtiLibrary/LtiAdvantagePlatform` contra un *tool* real.** Es **MIT, con AGS v2 + NRPS v2 + Deep Linking 2.0 y ASP.NET Core 10**, pero **se describe a sí misma como *«Sample»***. Que el *launch* cierre de punta a punta **está leído, no medido** — y es la acción barata que el pase 26 tiene que ejecutar antes de que esta KB prometa el lado LMS.
- **No verificó la fecha del último commit** de ninguno de los 12 repos: la página de GitHub no la expuso de forma legible vía WebFetch en esta sesión. Las señales de vida usadas son **commits totales, releases y forks**, que son más débiles.
- **No midió si el cartucho MCP de CaSS funciona.** Está **declarado en el README** entre los *pluggable cartridges*; no se levantó el servidor ni se listó una sola herramienta. Toda la tendencia **65** y el paso 4 de **P48** descansan en una declaración del propio proyecto. **Es el gap 40.**
- **No buscó** los artefactos `admissions`, `library`/OPAC ni `alumni`/*student success*: quedan como consigna del pase 26.

### 🔵 Las tres acciones que este pase deja escritas para el siguiente

1. **Levantar `LtiAdvantagePlatform` (MIT) contra `ltijs` (Apache-2.0, 373 ★) y medir si el *launch* OIDC cierra**, con AGS devolviendo una nota. Si cierra, esta KB puede proponer **el lado LMS con licencia permisiva** — capacidad que no tuvo en 24 pases. Si no cierra, escribirlo: *«Sample»* está en su propia descripción.
2. **Levantar el cartucho MCP de CaSS y listar sus herramientas** (gap 40). Es la verificación que convierte la tendencia 65 de promesa en capacidad, y la que decide si **P48** se puede cotizar.
3. **Cambiar el eje de búsqueda al conector**, que es donde este pase mostró tracción: `MCP server` + cada estándar que esta KB ya inventarió (**OneRoster, CASE, xAPI, QTI, LTI**). CaSS valió por sus cartuchos, no por su núcleo.

## Nota de método del pase 24 (2026-10-01) — el pase que dejó de leer código y lo ejecutó, y por eso pudo corregir al pase anterior

**Los pases 21, 22 y 23 leyeron `lrsql`. Este lo corrió.** Es la primera vez en veinticuatro pasadas que esta KB levanta
un motor de base de datos, crea el esquema con el DDL del proyecto y mide lo que devuelve un driver. **Y el resultado
invirtió una conclusión que la KB había escrito con confianza**: el pase 23 dedujo, de la forma del SQL, que el desglose
por tabla era inalcanzable sin partir las consultas; la medición muestra que los siete conteos ya vuelven por el bucle
estándar de JDBC. **La lectura del código era correcta y la inferencia sobre el driver no**, y sólo ejecutar podía
distinguir una cosa de la otra.

**La regla de método que deja, y vale más que el hallazgo:** cuando una conclusión de esta KB dependa del
**comportamiento de una pieza de terceros** —un driver, un runtime, un planificador— y no del código que se está
leyendo, **la inferencia no alcanza y hay que marcarla como pendiente de ejecución.** El pase 23 hizo lo correcto al
declarar explícitamente *«lo que NO se verificó ejecutando»* y dejar la acción escrita; sin esa declaración este pase
no habría sabido qué medir. **La cadena funcionó: declarar la ignorancia con precisión es lo que la vuelve resoluble.**

### Lo que trajo el barrido obligatorio, y es la sexta pasada seca para la tabla de agentes

Se corrieron las cuatro búsquedas globales y las cuatro regionales con el año **calculado** (2026). **Cero agentes nuevos
por sexta vez consecutiva.** Lo global devolvió, otra vez, la capa genérica (openclaw 385k ★, AutoGen, browser-use,
Mem0) y **material didáctico sobre AI** (`ai-engineering-from-scratch`, `free-ai-agents-resources`) — confirmando la
medición del pase 23: en GitHub el término `education` está capturado por *cursos sobre AI*, no por *software que educa*.

**Pero la consigna del pase 23 sí rindió, y rindió donde dijo que iba a rendir.** La instrucción era **evitar la palabra
`education`** y buscar por el **artefacto del dominio** o por el **estándar instalado**. Las cuatro búsquedas de
artefacto/estándar (`gradebook`+OneRoster+LTI, QTI 3 *item bank*, IEP, SIS/matrícula/asistencia/legajo) trajeron **seis
repos verificados de primera mano, cinco nuevos para esta KB**, y el hallazgo de encuadre del pase: **la capa LTI de esta
KB era íntegramente PHP, y existe una familia Java/Spring completa** publicada por una universidad europea. Ver
`repos/trending.md` y la sección nueva de `agents/top.md`.

**La consigna para el pase 25, y es una continuación, no un cambio de eje:** el eje artefacto/estándar **no está agotado**
— rindió en su primer uso. Quedan sin barrer los artefactos **`item bank`/banco de ítems**, **`proctoring`**,
**`timetable`/horario** y **`competency framework`/CASE**, y los estándares **Caliper**, **CASE** y **xAPI Profiles**.
Y queda una pregunta de método abierta: las dos únicas piezas *platform-side* (lado LMS) que vio esta KB aparecieron en
este pase y **una no declara licencia**; conviene buscar explícitamente `LTI platform`, porque toda la capa registrada
hasta ahora es *tool-side* y eso sesga lo que se puede proponer.

### La acción que este pase deja escrita

Dos, y las dos son chicas y de primera mano:

1. **Medir qué devuelve `next.jdbc` con `:result :affected`** sobre una consulta multi-sentencia, que es el único eslabón
   de la cadena del gap 36 que sigue inferido. **Este pase no pudo:** `repo.clojars.org` responde **403** por el proxy de
   egreso, así que no se pudo resolver `next.jdbc` ni `hugsql-adapter-next-jdbc`. Se puede hacer con el jar bajado por
   fuera o con `clojure-tools` oficial instalado. **Lo que hay que mirar** es si `execute!` llama `getMoreResults()`: si
   no lo llama —y la medición del driver sugiere que no, porque lrsql ve un solo número— el parche del gap 36 vive en el
   adaptador o en el interceptor, y no en lrsql.
2. **Enumerar las consultas multi-sentencia de lrsql** para dimensionar el *blast radius* del gap 38. Este pase lo
   intentó y **el clasificador de seguridad del entorno bloqueó el recorrido masivo del árbol clonado** — el mismo límite
   que frenó al pase 22. Con el árbol a mano fuera de este entorno es una tarde.


## Nota de método del pase 22 (2026-10-01) — el pase que midió su propio agotamiento, y encontró el hallazgo en la búsqueda que no era sobre agentes

**Qué se ejecutó.** El barrido obligatorio completo —cuatro búsquedas globales y cuatro regionales (North America,
EMEA, APAC, LATAM)— más la reconfirmación independiente del **gap 36** leyendo el código de `lrsql`.

**Resultado del barrido: agotado por cuarta vez consecutiva, y por primera vez medido candidato por candidato.**

- **Cero agentes nuevos.** Los dos únicos candidatos que trajo la búsqueda ya estaban en la KB **y la KB los tenía más
  precisos que la fuente**: `OpenMAIC` (la web lo da como «v1.0.0, MIT» y omite el **relicenciamiento de AGPL-3.0 a MIT
  en v0.3.0 del 2026-06-28**, que es exactamente el dato que hunde una propuesta) y `AITutor-EvalKit` (ya corregido en
  el pase 4: el repo canónico del mismo autor es `UnifyingAITutorEvaluation`, 32 ★).
- **Cero cifras de mercado nuevas.** Las ocho que devolvió el barrido regional —global $7,52B→$10,6B al 40,9% y los
  $79,6B a 2034; North America $951M→$2.303,2M al 15,9%; APAC $591,6M→$1.848,1M al 20,9%; la encuesta LATAM 2026 del
  Digital Education Council con 92%/79% y la grilla de gobernanza 26,0/18,5/9,0; el programa educativo de OpenAI con 8
  socios y los USD 169 M— **ya estaban todas en `intel/market.md`, con fuente y con las discrepancias metodológicas
  declaradas**. Se reconfirman, no se agregan.
- **Y una donde la KB le gana en precisión a la web, que conviene saber porque el cliente leyó la web:** las fuentes
  generalistas dicen que el EU AI Act *«entra plenamente en vigor en agosto de 2026»* clasificando educación como alto
  riesgo. **El calendario real que esta KB tiene es más fino** —en vigor 2026-07-27, aplicación por el AI Office desde
  2026-08-02, **Anexo III (educación) el 2027-12-02**— y la diferencia es de **16 meses de margen** sobre la obligación
  que al cliente más le preocupa. Hay que llevar el calendario, no la nota de prensa.

**Lo que esto dice sobre el método, y es la conclusión operativa del pase.** Los tres pases que movieron la tabla lo
hicieron **cambiando el sustantivo de la búsqueda**, no la región: el pase 4 buscó *benchmark* en vez de *repo de
agente*, el pase 17 buscó `SKILL.md` + dominio educativo, y **este pase encontró lo que encontró buscando
`plataforma / LMS open source` — no buscando agentes**. El barrido regional lleva cuatro pasadas dando confirmación.
**El rendimiento está en cambiar el eje, no en insistir con el mismo y rotar el país.**

**Qué se verificó de primera mano.** `tutor-contrib-aspects` y `platform-plugin-aspects` (licencia, estrellas, forks,
commits, lenguaje, y el `UserRetirementSink` leído en el README); el **PR #1328** (título, autor, estado **cerrado sin
mergear** el 2026-09-16, y la descripción del bypass del flag de PII); y el interceptor de `lrsql`
(`interceptors/lrs_management.clj:23–33`, `routes.clj:331` y `:407`, `protocol.clj:58`) por lectura directa del árbol
clonado.

**Qué NO se pudo verificar, y queda declarado en vez de inferido.** Dos cosas, las dos con su causa:

1. **El ADR de PII de Aspects** —la fuente de la afirmación *«el dato de eventos no se elimina porque queda
   anonimizado»*— vive en `docs.openedx.org`, **bloqueado por el proxy de egreso**, igual que `arxiv.org` en los pases
   6, 7, 14, 16–19 y `moodle.org` en el 19. Los dos caminos alternativos (el `.rst` crudo y el listado del directorio
   de decisiones en GitHub) dieron **404**. La afirmación se registra por snippets concordantes, con la URL anotada.
2. **Si `-delete-actor` ya devuelve los conteos de filas afectadas** —la sub-pregunta que decide si el parche del
   **gap 36** es de una línea o necesita plomería—. **La traza de la implementación quedó bloqueada por el clasificador
   de seguridad del entorno** (dos denegaciones al explorar el árbol clonado de terceros). **No se contestó por
   inferencia**, que era la tentación obvia teniendo el resto del archivo a la vista.

**La regla que este pase agrega a las de los pases 5 y 12.** El pase 5 escribió que *«el proxy de egreso decide qué se
puede afirmar»*. Este pase agrega la otra mitad: **el entorno también decide qué se puede investigar, y cuando bloquea
una lectura la respuesta correcta es declarar la pregunta abierta con su coordenada exacta, no completarla con lo que
probablemente diga el código.** Las dos veces que esta KB se equivocó en grande —el gap 33 y las estrellas de los
ciclos 1–3— fue por afirmar sin leer.

## Nota de método del pase 21 (2026-10-01) — el pase que ejecutó la acción escrita hace dos pasadas, y encontró que la KB se había equivocado a su propio favor comercial

**Lo que se hizo distinto, y es la razón por la que funcionó.** Veinte pasadas verificaron repos **abriendo su página en
GitHub**: licencia, estrellas, forks, commits, descripción. Eso alcanza para saber **qué es** un repo y **no alcanza
para saber qué hace**. Este pase **clonó tres repositorios y leyó el código fuente**, que es lo que el pase 19 había
hecho una sola vez —sobre el árbol de Moodle— y que resultó, las dos veces, el método más productivo de esta KB.

**El resultado incómodo, dicho sin suavizar.** El **gap 33** —vigente desde el pase 19, citado en la tendencia 49, en
**P38**, en **P40**, en `verticals/solutions.md`, en `repos/foundations.md` y en los argumentos de EMEA y LATAM de
`intel/market.md`— **era falso en su mitad principal**. El LRS permisivo que esta KB recomienda como default
(`lrsql`, Apache-2.0) tiene el mejor primitivo de borrado de toda la capa, y lo tenía desde antes de que esta KB
existiera. **Y la propia KB tenía escrita la nota que lo advertía**, al pie de la tabla: *«el "no" es ausencia en la
documentación publicada, no una prueba de que la operación sea imposible»*. **La nota tenía razón y sobrevivió catorce
pasadas sin que nadie la ejecutara.**

**Por qué el error fue en esta dirección y no en otra, que es lo que conviene no repetir.** Un gap declarado es
**vendible**: justifica alcance, justifica horas, justifica un patrón. Una capacidad que ya existe en el producto
recomendado **no factura nada**. No hubo mala fe —hubo una tabla construida sobre documentación y una nota al pie que
nadie convirtió en tarea— pero el sesgo es estructural: **los gaps se revisan menos que los hallazgos, porque nadie
tiene incentivo para cerrar uno.** La contramedida concreta, para los pases que vienen: **todo gap cuya evidencia sea
"no está documentado" se marca como lectura pendiente, no como ausencia**, y no entra a un entregable de cliente hasta
que alguien haya leído el código.

**Qué está verificado y con qué fuerza, en tres niveles distintos.**

1. 🟢 **Leído en el código fuente** (la evidencia más fuerte que produce esta KB): todo lo que afirman las tendencias
   **54** y **56**, la mitad técnica de la **55**, el **gap 36**, la matriz corregida de `verticals/solutions.md`, la
   tabla corregida de `repos/foundations.md` y el patrón **P44**. Incluye las rutas, los nombres de archivo y los
   números de línea, para que el próximo pase pueda contradecirlo sin volver a buscar.
2. 🟡 **Leído en la página del repo vía WebFetch**: estrellas, forks, licencias y el hecho de que Learning Locker
   **no** está archivado. La reverificación de **DeepTutor** coincide con la del pase 20 — dos lecturas independientes
   concordantes, que es lo más cerca de "confirmado" que llega esta KB sin la API.
3. 🔴 **Resultados de búsqueda, sin fuente primaria**: la limitación de **ILIAS** (`docu.ilias.de` bloqueado) y
   **todo el barrido regional**. No usar en material de cliente sin abrir la fuente.

**El barrido regional dio el mismo resultado que en los pases 19 y 20, y por tercera vez consecutiva se registra como
gap informado y no como silencio.** Las cuatro búsquedas regionales (`AI {industry} {region} 2026 adoption regulation
players`) devolvieron **AI empresarial, no educativa**: prioridades de CIO, gobernanza de directorios, soberanía de
infraestructura, inversión en *reskilling* corporativo. **La consulta regional genérica está agotada para esta
vertical** — y la regla del pase 20 sigue siendo la salida: *si la región no devuelve nada, el nombre que falta es el
de un país*. Lo poco aprovechable apareció así: Reino Unido con **£200M+** comprometidos en adopción de AI (del cual
£100M a Bridge AI y £53M a iniciativas regionales), el **Europe EdTech 200** y la London EdTech Week como mapa de
*players* de EMEA, y la constatación de que **APAC y LATAM no tienen cifra de mercado educativo propia en esta
ventana**. Se detalla por región en `intel/market.md`.

**Una limitación de entorno que cambió, y conviene registrarla.** Veinte pasadas anotaron que `curl -sI` devuelve 403
contra `github.com` y que la API de GitHub está fuera de alcance. **Las dos siguen siendo verdad, y las dos dejaron de
importar para lo que decide este archivo:** `git clone --depth 1 --filter=blob:none` **funciona a través del proxy**,
y leer un archivo del árbol clonado es evidencia más fuerte que cualquier cosa que devuelva la API. **La verificación
de capacidad se hace clonando, no consultando.** Es la recomendación de método más reutilizable de este pase.

Testing de conformidad y evaluación regulatoria — **pase 20 (2026-10-01)**. Repos verificados de primera mano vía WebFetch (licencia, estrellas, forks, alcance declarado): [inspect_ai (UK AISI)](https://github.com/UKGovernmentBEIS/inspect_ai) · [moonshot](https://github.com/aiverify-foundation/moonshot) · [compl-ai](https://github.com/compl-ai/compl-ai) · [aiverify](https://github.com/aiverify-foundation/aiverify) · [moonshot-data](https://github.com/aiverify-foundation/moonshot-data) · [LLM-Evals-Catalogue](https://github.com/aiverify-foundation/LLM-Evals-Catalogue) · [awesome-eu-ai-act](https://github.com/morganrcu/awesome-eu-ai-act) · [moonshot-cicd](https://github.com/aiverify-foundation/moonshot-cicd) · [moonshot-ui](https://github.com/aiverify-foundation/moonshot-ui) · [aiverify-developer-tools](https://github.com/aiverify-foundation/aiverify-developer-tools) · [organización aiverify-foundation](https://github.com/aiverify-foundation)

*Unlearning* educativo — **pase 20**, verificado vía WebFetch: [GEMLab-HKU/Unlearn_and_Relearn](https://github.com/GEMLab-HKU/Unlearn_and_Relearn) (MIT, 4 ★, 22 commits; GEMLab, Universidad de Hong Kong — Jiajia Song, Zhihan Guo, Jionghao Lin). Paper: Springer `10.1007/978-3-032-29744-0_42`, preprint `arXiv 2603.26142` (🔴 **arxiv.org y link.springer.com no se abrieron: bloqueados / no verificados de primera mano**). Colisión de terminología documentada contra *Lifting Data-Tracing Machine Unlearning to Knowledge-Tracing for Foundation Models* (`arXiv 2506.11253`, 🔴 sin verificar).

Marco regulatorio y plataforma estatal de Singapur — **pase 20**. 🔴 **Todo de fuentes secundarias concordantes: `imda.gov.sg`, `moe.gov.sg` y `learning.moe.edu.sg` están bloqueados por el proxy de egreso de esta sesión.** *Model AI Governance Framework for Agentic AI* v1.5 (anunciado 2026-01-22 en el WEF; actualizado 2026-05-20 y 2026-06-05), *Starter Kit for Testing LLM-Based Applications for Safety and Reliability* v1.0 (enero 2026), crosswalks a NIST AI RMF (oct-2023) y a ISO/IEC 42001:2023 (jun-2024), y las ocho funciones de AI del Student Learning Space (seis nombradas: ALS, LEA, FA-Math, AFA, SAFA, SET). **Antes de usar cualquiera de estos datos con un cliente: abrir la fuente del MOE y de IMDA.**

Regulación regional — **pase 20**, fuentes secundarias concordantes: North America (**134 proyectos de ley en 31 estados**, California AB 1159, Idaho SB 1227, Oklahoma y Maryland, Georgia y Mississippi; RAND 25%→53% en planificación docente) · EMEA (AI Act en vigor 2026-07-27, aplicación desde 2026-08-02, Anexo III 2027-12-02, Anexo I 2028-08-02) · LATAM (Brasil **PL 2338/2023**, Chile **Ley 21.719** + proyecto de cuatro niveles, México **85 iniciativas** y auditoría anual de alto riesgo; auditorías técnicas de detectores en el sector educativo mexicano con tasas de error altas).

Borrado, telemetría y *unlearning* — **pase 19 (2026-10-01)**. Verificado de primera mano sobre el árbol de Moodle (clon `--depth 1 --filter=blob:none --sparse`, `main` = **5.3rc1**, commit `85af0b5`): [moodle/moodle](https://github.com/moodle/moodle) — `public/ai/classes/privacy/provider.php`, los siete `public/ai/provider/*/classes/privacy/provider.php`, `public/admin/tool/dataprivacy/db/events.php`, `public/admin/tool/dataprivacy/classes/event/user_deleted_observer.php` y `public/admin/tool/dataprivacy/classes/api.php`. Rama verificada con `git ls-remote --heads`. Repos verificados vía WebFetch: [open-unlearning](https://github.com/locuslab/open-unlearning) · [machine-unlearning-pytorch (`torchunlearn`)](https://github.com/Harry24k/machine-unlearning-pytorch) · [OngWinKent/MachineUnlearning](https://github.com/OngWinKent/MachineUnlearning) · [jjbrophy47/machine_unlearning](https://github.com/jjbrophy47/machine_unlearning) · [lrsql](https://github.com/yetanalytics/lrsql) · [ralph](https://github.com/openfun/ralph) · [learninglocker](https://github.com/LearningLocker/learninglocker) · [topic `ai-tutor`](https://github.com/topics/ai-tutor)

Agentes nuevos — pase 19, verificados vía WebFetch: [human-skill-tree](https://github.com/24kchengYe/human-skill-tree) · [universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) · [algo-sensei](https://github.com/karanb192/algo-sensei) · [universal-diagnostic-tutor-skill](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) · [lumen](https://github.com/ahmedEid1/lumen)

Regulación — pase 19: **Vietnam, Ley de IA N.º 134/2025/QH15 y Decisión 33** (46 sistemas de alto riesgo en 6 sectores, 3 en educación; [Allen & Gledhill](https://www.allenandgledhill.com/vn/publication/articles/33374/identifies-high-risk-ai-systems-across-six-sectors), [Vietnam Briefing](https://www.vietnam-briefing.com/news/46-high-risk-ai-systems-to-face-enhanced-regulatory-oversight-in-vietnam.html), [Tilleke & Gibbins](https://www.tilleke.com/insights/vietnam-introduces-sectoral-list-of-high-risk-ai-systems/2/)) · **Digital Omnibus / Reglamento (UE) 2026/1744 y la confirmación de que el Art. 50 no se movió** ([Usercentrics](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/), [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/), [Jones Walker](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon)) · **California AB 1159 / HESIPA**, firma **2026-09-10**, operativa **2027-07-01** ([F3 Law](https://www.f3law.com/insights/new-california-law-limits-technology-companies-use-of-student-data-in-ai-systems-102o16i/), [Privacy Rights Clearinghouse](https://privacyrights.org/resources-tools/articles/governor-signs-prc-sponsored-ab-1159-law-strengthening-privacy-protections)) · **gobernanza docente en EE. UU.** ([MultiState](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session), [AI for Education: guía estatal](https://www.aiforeducation.io/ai-resources/state-ai-guidance)) · **adopción LATAM** ([Digital Education Council, encuesta LATAM 2026](https://www.digitaleducationcouncil.com/dec-insights/92-of-students-and-79-of-faculty-actively-engaging-with-ai-findings-from-ai-in-higher-education-latam-survey-2026)) · **borrado en xAPI** ([Learning Pool: xAPI y GDPR](https://learningpool.com/how-xapi-helps-solve-for-gdpr-requirements))

⚠️ *Del pase 19: **`arxiv.org` sigue bloqueado por el proxy de egreso**, igual que en los pases 6, 7, 14, 16, 17 y 18 — **PrivacyCD (arXiv 2511.03966)** y **P-MIA (arXiv 2511.04716)** se registran por **snippets concordantes**, con su número anotado para que el próximo pase los abra, **no para citarlos ante un cliente**. **`moodle.org` también sigue bloqueado**: `local_gdpr_deleteuserdata` (GPL-3.0, 2018-07-08, Moodle 3.5) **no se verificó de primera mano y no se localizó repositorio en GitHub** — se registra como antecedente de diseño, no como dependencia. La **API de borrado de Learning Locker** viene de fuente secundaria y **no se verificó contra su API**: es la acción 1 que este pase deja escrita.*


Privacidad del dato en el LMS instalado y canal de *skills* — pase 17 (2026-10-01), repos verificados vía WebFetch: [edx-platform](https://github.com/openedx/edx-platform) y su [scripts/user_retirement](https://github.com/openedx/edx-platform/tree/master/scripts/user_retirement) y [lms/djangoapps/bulk_user_retirement](https://github.com/openedx/edx-platform/tree/master/lms/djangoapps/bulk_user_retirement) · [moodle](https://github.com/moodle/moodle) · [canvas-lms](https://github.com/instructure/canvas-lms) · [openeducat_erp](https://github.com/openeducat/openeducat_erp) · [k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) · [learning-commons-org/agent-skills](https://github.com/learning-commons-org/agent-skills) · [DeepTutor](https://github.com/HKUDS/DeepTutor) · [education-agent-skills](https://github.com/GarethManning/education-agent-skills)

Regulación y incidentes — pase 17: **California AB 1159 / HESIPA** (firmada 2026-09-13; [comunicado de la oficina de la asambleísta Addis](https://addis.asmdc.org/press-releases/20260910-addis-bill-bolstering-student-data-protection-signed-law), [análisis del comité APCP](https://apcp.assembly.ca.gov/system/files/2026-01/ab-1159-addis-apcp-analysis.pdf), [Golden Data](https://medium.com/golden-data/ab-1159-extending-student-data-privacy-protections-to-higher-education-8676161660e1), [Captain Compliance](https://captaincompliance.com/education/california-ab-1159-a-landmark-student-privacy-bill-that-fixes-the-past-while-struggling-to-catch-the-present/)) · **COPPA enmendada, precisión del pase 17** ([Finnegan](https://www.finnegan.com/en/insights/articles/the-ftcs-updated-coppa-rule-redefining-childrens-digital-privacy-protection.html), [National Law Review](https://natlawreview.com/article/ftc-publishes-final-coppa-rule-amendments), [promise.legal](https://blog.promise.legal/coppa-april-2026-amendments-edtech/)) · **incidente Instructure/Canvas** abril–mayo 2026 ([TechRepublic](https://www.techrepublic.com/fr/article/news-canvas-breach-hackers-deal-275m-records-stolen/), [JD Supra](https://www.jdsupra.com/legalnews/client-alert-instructure-data-breach-7807251/), [Nasdaq](https://www.nasdaq.com/articles/canvas-parent-instructure-hit-cyberattack)) · **Anexo III del AI Act diferido al 2027-12-02** ([Reed Smith](https://www.reedsmith.com/our-insights/blogs/technology-law-dispatch/102nfi5/eu-ai-act-next-level-applies-as-of-2-august-2026/), [sota.io para EdTech](https://sota.io/blog/eu-ai-act-edtech-educational-software-developer-compliance-2026)) · **gobernanza de AI en educación en EE. UU.** ([informe Kiteworks 2026](https://www.kiteworks.com/sites/default/files/resources/kiteworks-report-education-ai-governance-data-security-compliance-2026-report.pdf), [MultiState: cómo los estados regulan la AI en educación](https://multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session)) · **adopción LATAM** ([Digital Education Council, encuesta LATAM 2026](https://www.digitaleducationcouncil.com/post/92-of-students-and-79-of-faculty-actively-engaging-with-ai-findings-from-ai-in-higher-education-latam-survey-2026)) · **directrices éticas de la Comisión Europea para docentes** ([BABL AI](https://babl.ai/european-commission-updates-ai-ethics-guidelines-to-help-teachers-navigate-ai-and-data-use-in-schools/))

⚠️ *Del pase 17: **`moodle.org`, `docs.moodle.org`, `docs.openedx.org`, `privacyrights.org`, `calmatters.org` y `leginfo.legislature.ca.gov` están bloqueados por el proxy de egreso.** En consecuencia: (a) la cita «User retirement is not a compliance guarantee…» viene de **snippet de búsqueda**, no de fetch de primera mano, y el `README` del directorio en GitHub no la contiene; (b) el **Privacy API de Moodle**, `tool_dataprivacy` y `tool_policy` están **documentados por Moodle vía snippet**, no verificados de primera mano —el árbol de `admin/tool/dataprivacy` dio 404 por cuatro rutas distintas—; (c) **AB 1159** no se leyó en la fuente legislativa oficial: fechas, autoría y texto de la prohibición provienen de múltiples fuentes concordantes. **`curl -sI` devolvió 403 incluso para un repo deliberadamente inexistente**, así que no verifica nada en esta sesión; ver la nota de método del pase 17.*

Privacidad y datos del alumno — pase 16 (2026-10-01), repos verificados vía WebFetch: [PySyft](https://github.com/OpenMined/PySyft) · [Flower](https://github.com/adap/flower) · [OpenFL (deprecado)](https://github.com/securefederatedai/openfl) · [Google DP](https://github.com/google/differential-privacy) · [Opacus](https://github.com/pytorch/opacus) · [TensorFlow Privacy](https://github.com/tensorflow/privacy) · [diffprivlib](https://github.com/IBM/differential-privacy-library) · [OpenDP](https://github.com/opendp/opendp) · [synthcity](https://github.com/vanderschaarlab/synthcity) · [ydata-synthetic](https://github.com/ydataai/ydata-synthetic) · [SDV](https://github.com/sdv-dev/SDV) y su [LICENSE (BUSL 1.1)](https://github.com/sdv-dev/SDV/blob/main/LICENSE) · [PrivGen](https://github.com/Akulen/PrivGen) · [FedGKT](https://github.com/TarunRaina/FedGNN-for-Personalized-Knowledge-Tracing) · [federated-deep-knowledge-tracing](https://github.com/hxwujinze/federated-deep-knowledge-tracing) · [SynEdu-HEDL](https://github.com/drsanjayagal/SynEdu-HEDL)

Regulación de privacidad educativa — pase 16: COPPA enmendada ([White & Case](https://www.whitecase.com/insight-alert/unpacking-ftcs-coppa-amendments-what-you-need-know), [Privacy & Data Security Insight](https://www.privacyanddatasecurityinsight.com/2026/04/enforcement-begins-soon-for-significant-coppa-rule-amendments/)) · FERPA y AI ([AFS Law](https://www.afslaw.com/perspectives/ai-law-blog/the-development-ai-and-protecting-student-data-privacy)) · DPDP Act India ([ORF](https://www.orfonline.org/research/governing-learner-data-risks-in-india-the-dpdp-act-and-the-case-for-edtech-specific-regulation), [medianama](https://www.medianama.com/2026/09/223-microsoft-student-data-ai-training-schools-india/)) · Brasil: Referencial do MEC ([O Tempo](https://www.otempo.com.br/educacao/2026/3/13/mec-recomenda-veto-de-ia-na-educacao-infantil-e-desaconselha-reconhecimento-facial-nas-escolas), [Jeduca](https://jeduca.org.br/noticia/ia-na-educacao-entenda-o-novo-referencial-do-mec-e-pontos-de-atencao)), ANPD y biometría en Paraná ([Data Privacy Brasil](https://www.dataprivacybr.org/anpd-suspende-o-uso-de-reconhecimento-facial-em-escolas-publicas-do-parana/), [Convergência Digital](https://convergenciadigital.com.br/governo/anpd-exige-suspensao-imediata-do-tratamento-de-dados-biometricos-na-frequencia-escolar-no-parana/)), LGPD na educação ([Confidata](https://confidata.com.br/blog/lgpd-educacao-2026-impacto-eca-digital))

⚠️ *Del pase 16: se abrieron de primera mano sólo los enlaces a `github.com`. **`nature.com` y `arxiv.org` están bloqueados por el proxy de egreso**, así que el paper de `SynEdu-HEDL` (Scientific Reports `s41598-026-44990-8`) y el de síntesis por cópulas (`arXiv 2604.04195`) **no se verificaron de primera mano**. El `Referencial` del MEC se leyó vía cobertura periodística, no desde el PDF oficial. `curl -sI` devolvió **403 en los catorce repos consultados** — ninguno era un 404; ver la nota de método del pase 16.*


Nuevo en el pase 15 — capa de marcado y procedencia (verificado vía WebFetch el 2026-10-01): [SynthID-Text en transformers](https://github.com/huggingface/transformers/blob/main/src/transformers/generation/watermarking.py) · [MarkLLM](https://github.com/THU-BPM/MarkLLM) · [c2pa-rs](https://github.com/contentauth/c2pa-rs) · [c2pa-python](https://github.com/contentauth/c2pa-python)

Nuevo en el pase 15 — capa de detección forense (verificado vía WebFetch el 2026-10-01): [fast-detect-gpt](https://github.com/baoguangsheng/fast-detect-gpt) · [Binoculars](https://github.com/ahans30/Binoculars) · [RAID](https://github.com/liamdugan/raid) · [LLM-generated-Text-Detection (survey)](https://github.com/NLP2CT/LLM-generated-Text-Detection) · [sloptotal](https://github.com/pablocaeg/sloptotal) · [awesome-ai-detection](https://github.com/Lendarixon/awesome-ai-detection) · [detectoria (sin licencia)](https://github.com/yonatanlop/detectoria) · [humanizar-es (evasión, skill de agente)](https://github.com/ervin-mo/humanizar-es)

Nuevo en el pase 15 — Artículo 50 y Code of Practice de marcado (⚠️ **todo de fuentes secundarias: los dominios oficiales están bloqueados por el proxy**, y las dos primeras discrepan en la fecha de publicación del Code of Practice —10 de junio vs. 20 de julio de 2026—): [IPTC — European AI Office releases Code of Practice on Transparency of AI-Generated Content](https://iptc.org/news/eu-ai-transparency-code-of-practice-june-2026/) · [Lewis Silkin — the EU's new AI labelling rules](https://www.lewissilkin.com/insights/2026/07/24/the-eus-new-ai-labelling-rules-what-every-organisation-needs-to-know-102ne35) · [Paul Weiss — EU finalises transparency rules for AI-generated content](https://www.paulweiss.com/insights/client-memos/eu-finalises-transparency-rules-for-ai-generated-content) · [artificialintelligenceact.eu — guía del Artículo 50 (🔴 bloqueado, no abierto)](https://artificialintelligenceact.eu/transparency-rules-article-50/)

Nuevo en el pase 15 — abandono institucional de la detección: [Más de 50 universidades desactivaron la detección de AI de Turnitin](https://www.aiplagguides.com/blog/universities-disabling-turnitin-ai-detection) · [Diplo — universidades dejan de usar detectores](https://www.diplomacy.edu/updates/universities-stop-using-ai-detection-tool-such-as-turnitin/) · [GPT detectors are biased against non-native English writers (🔴 arxiv bloqueado, citado vía resultados de búsqueda)](https://arxiv.org/html/2304.02819)

Nuevo en el pase 15 — integridad académica en LATAM: [Infobae — México, Colombia y Chile: declaración obligatoria del uso de AI](https://www.infobae.com/educacion/2025/08/26/las-claves-de-mexico-colombia-y-chile-para-incorporar-a-la-inteligencia-artificial-en-la-universidad/) · [Educación y Tecnología — IA en la educación en México 2026](https://educacionytecnologia.com/inteligencia-artificial-educacion-mexico-estudio-2026/) · [UNESCO ESS — autoría e integridad académica ante la IA generativa](https://ess.iesalc.unesco.org/index.php/ess3/article/view/1174) · [Zenodo — políticas de integridad de las 15 universidades LATAM mejor rankeadas en THE 2026 (🔴 bloqueado, licencia sin verificar)](https://zenodo.org/records/22661179)

Nuevo en el pase 15 — plugins de integridad en Moodle (envoltorios de servicios propietarios; ⚠️ **`moodle.org` está bloqueado por el proxy: licencia, instalaciones y fechas de release provienen de resultados de búsqueda, no de la página del directorio**): [Compilatio (plugin GPL-3.0)](https://moodle.org/plugins/plagiarism_compilatio) · [Copyleaks](https://moodle.org/plugins/plagiarism_copyleaks) · [Originality.ai](https://marketplace.moodle.com/plugins/plagiarism_origai)

Nuevo en el pase 13 — capa de práctica y corrección desplegada (verificado vía WebFetch el 2026-10-01): [jupyterhub](https://github.com/jupyterhub/jupyterhub) · [jupyter-ai](https://github.com/jupyterlab/jupyter-ai) · [nbgrader](https://github.com/jupyter/nbgrader) · [nbgrader releases v0.9.6](https://github.com/jupyter/nbgrader/releases) · [otter-grader](https://github.com/ucbds-infra/otter-grader) · [ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) · [jupyterhub-deploy-teaching](https://github.com/jupyterhub/jupyterhub-deploy-teaching) · [Aalto Scientific Computing — autograding](https://scicomp.aalto.fi/aalto/jupyterhub-instructors/autograding/) · [Aalto — nbgrader basics](https://scicomp.aalto.fi/aalto/jupyterhub-instructors/nbgrader/)

Nuevo en el pase 13 — evaluación pedagógica y docente: [pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) · [AI-for-Education (organización)](https://github.com/AI-for-Education) · [microsoft/Shiksha-Copilot](https://github.com/microsoft/Shiksha-Copilot) · [Shiksha Copilot — sitio del proyecto](https://deeshib.github.io/shiksha-copilot/) · [Microsoft Research — diseño con docentes de India](https://www.microsoft.com/en-us/research/blog/teachers-in-india-help-microsoft-research-design-ai-tool-for-creating-great-classroom-content/)

Nuevo en el pase 13 — regulación de Vietnam (educación como alto riesgo): [Allen & Gledhill — marco basado en riesgo, en vigor 2026-03-01](https://www.allenandgledhill.com/vn/publication/articles/32667/s-new-law-on-artificial-intelligence-risk-based-regulatory-framework-in-force-1-march-2026) · [Allen & Gledhill — lista sectorial de alto riesgo, seis sectores](https://www.allenandgledhill.com/perspectives/articles/33373/vnkh-vietnam-identifies-high-risk-ai-systems-across-six-sectors) · [China Briefing — 46 sistemas de alto riesgo](https://www.china-briefing.com/china-outbound-news/46-high-risk-ai-systems-to-face-enhanced-regulatory-oversight-in-vietnam) · [Baker McKenzie](https://www.bakermckenzie.com/en/insight/publications/2026/02/vietnam-artificial-intelligence-law-foundation-and-outlook) · [Tilleke & Gibbins](https://www.tilleke.com/insights/a-closer-look-at-vietnams-new-ai-law-what-it-means-for-ai-businesses/51/) · [VILAF — obligaciones desde 2026-03-01](https://www.vilaf.com.vn/blog/vietnam-enacts-its-first-law-on-artificial-intelligence-key-regulatory-obligations-from-1-march-2026/)

Nuevo en el pase 13 — LATAM institucional y regulatorio: [UNESCO IESALC — estudio 2026-09-09](https://www.iesalc.unesco.org/en/articles/new-unesco-iesalc-study-reveals-widespread-ai-adoption-higher-education-across-latin-america-and) 🔴 *dominio bloqueado por el proxy; las cifras vienen de resultados de búsqueda* · [UNESCO Digital Learning Week 2026](https://www.unesco.org/en/weeks/digital-learning) · [Plan Nacional de IA de México — ATDT (PDF)](https://www.portal.atdt.gob.mx/wp-content/uploads/2026/06/Plan-Nacional-de-IA.pdf) · [Polifonía — olas regulatorias LATAM 2026-2030](https://polifonia.org/2026-2030-regulacion-ia-en-america-latina/)

Nuevo en el pase 13 — North America, legislación educativa: [MultiState — tendencias de política estatal 2026](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session) · [NASBE — gobernanza del uso de AI en escuelas](https://www.nasbe.org/states-take-next-steps-on-governing-ai-use-in-schools/) · [ExcelinEd — hitos de política K-12 2026](https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/) · [AI for Education — guía estatal](https://www.aiforeducation.io/ai-resources/state-ai-guidance)

Mercado y players: [Grand View Research](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-education-market-report) · [Research and Markets](https://www.researchandmarkets.com/reports/5896034/ai-in-education-market-report) · [AI Tutors Market](https://www.grandviewresearch.com/industry-analysis/ai-tutors-market-report) · [5WPR EdTech AI Visibility Index 2026](https://www.5wpr.com/research/edtech-ai-visibility-index-2026/) · [Khan Academy / Duolingo agents](https://callsphere.ai/blog/ai-agents-education-khan-academy-duolingo-autonomous-tutoring)

Capa predictiva, Apereo y licencia ECL-2.0 — agregado en el pase 11: [sakai](https://github.com/sakaiproject/sakai) · [opencast](https://github.com/opencast/opencast) · [uPortal](https://github.com/uPortal-Project/uPortal) · [OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) · [LearningAnalyticsProcessor](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) · [OpenLRS (archivado)](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS) · [OpenDashboard-legacy](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy) · [OpenDashboard-ux](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-ux) · [OpenDashboard-api](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) · [Larissa](https://github.com/Apereo-Learning-Analytics-Initiative/Larissa) · [terracotta](https://github.com/terracotta-education/terracotta) · [aira](https://github.com/GoogleCloudPlatform/aira) · [Student-Retention-Prediction](https://github.com/Aliipou/Student-Retention-Prediction) · [student-early-warning](https://github.com/dssg/student-early-warning) · [SIH-2026 / DropGuard](https://github.com/novatrix-2030/SIH-2026) · licencia: [SPDX ECL-2.0](https://spdx.org/licenses/ECL-2.0.html)

Nuevos en el pase 11 — agentes, currículo y plataformas: [Gnos](https://github.com/madhvantyagi/Gnos) · [Alvarmethod](https://github.com/vasanthsreeram/Alvarmethod) · [learn](https://github.com/amosblomqvist/learn) · [korean-elementary-learning-map](https://github.com/DECK6/korean-elementary-learning-map) · [ai-builders-curriculum](https://github.com/ai-builders-foundation/ai-builders-curriculum) · [classmoji](https://github.com/classmoji/classmoji) · [Milky-institute-online](https://github.com/jude-miller-dev/Milky-institute-online) · [tadreeblms](https://github.com/Tadreeb-LMS/tadreeblms) · [dsh-openmaic](https://github.com/THU-MAIC/dsh-openmaic)

Datos de deserción — agregado en el pase 11 (🔴 ninguno leído de primera mano, dominios bloqueados por el proxy): OULAD · `https://analyse.kmi.open.ac.uk/open_dataset` · UCI 697 · `https://archive.ics.uci.edu/dataset/697` · benchmark de supervivencia · `arXiv 2604.08870`

Regulación del pase 11 (🔴 fuentes secundarias coincidentes; primarias bloqueadas): Reglamento (UE) 2026/1744 (Digital Omnibus on AI) · EU AI Act Anexo III · legislación estatal de EE. UU. 2026 (134 proyectos en 31 estados; MD, ID, OK, VA; California AB 1159; Idaho SB 1227) · Ley Básica de IA de Taiwán (en vigor 2026-01-14) · sectores de alto riesgo de Vietnam · UNESCO IESALC (200 instituciones, 19 países) · Digital Education Council LATAM 2026 (30.000+ respuestas, 29 instituciones)

Credenciales verificables e interoperabilidad — agregado en el pase 9: [learner-credential-wallet](https://github.com/digitalcredentials/learner-credential-wallet) · [verifier-plus](https://github.com/digitalcredentials/verifier-plus) · [issuer-coordinator](https://github.com/digitalcredentials/issuer-coordinator) · [qti3-item-player](https://github.com/amp-up-io/qti3-item-player) · [esco-skill-extractor](https://github.com/KonstantinosPetrakis/esco-skill-extractor) · [oneroster (TypeScript)](https://github.com/LongsightGroup/oneroster) · [lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) · [openbadges-specification](https://github.com/1EdTech/openbadges-specification) · [tao-core](https://github.com/oat-sa/tao-core) · [openbadgeslib](https://github.com/luisgf/openbadgeslib) · [caliper-php-public (U. de Michigan)](https://github.com/tl-its-umich-edu/caliper-php-public) · [European Learning Model (archivado)](https://github.com/european-commission-empl/European-Learning-Model) · [European Digital Credentials (archivado)](https://github.com/european-commission-empl/european-digital-credentials) · [Open Badges 3.0 — guía de implementación 1EdTech](https://standards.1edtech.org/open-badges/guides/standards/v3p0/impl) · [Europass — información para desarrolladores](https://europass.europa.eu/en/information-developers)

Evaluación y seguridad pedagógica — agregado en el pase 5: [SafeTutors (repo)](https://github.com/RadiantCrystal/SafeTutors) · [EduBench (repo)](https://github.com/ybai-nlp/EduBench) · [EduGuardBench (repo)](https://github.com/YL1N/EduGuardBench) · [EduFrameTrap / sycophancy (arXiv 2605.14604)](https://arxiv.org/abs/2605.14604) · [ELBench (arXiv 2608.09548)](https://arxiv.org/abs/2608.09548) · [SafeTutors (arXiv 2603.17373)](https://arxiv.org/abs/2603.17373) · [EduGuardBench (arXiv 2511.06890)](https://arxiv.org/abs/2511.06890)

Modelado y modelos — agregado en el pase 5: [pyBKT](https://github.com/CAHLR/pyBKT) · [OmniEdu (repo)](https://github.com/haolpku/Omni-Edu) · [OmniEdu (arXiv 2609.23088)](https://arxiv.org/abs/2609.23088)

Teacher-facing y grading — agregado en el pase 5: [Aila / Oak National Academy](https://github.com/oaknational/oak-ai-lesson-assistant) · [rubric](https://github.com/paper-instruments/rubric) · [llmgrader](https://github.com/sdrangan/llmgrader) · [Autograder.io](https://github.com/eecs-autograder/autograder.io)

Mercado y regulación — agregado en el pase 5: [UNESCO IESALC / UNU — AI Implementation in Higher Education in LAC](https://unu.edu/publication/ai-implementation-higher-education-latin-america-and-caribbean) · [Times Higher Education — uneven AI adoption in Latin America](https://www.timeshighereducation.com/node/744954) · [Council of Europe — 3rd Working Conference & Compass for AI and Education](https://www.coe.int/en/web/education/-/artificial-intelligence-and-education-third-working-conference) · [MarketsandMarkets — North America AI in Education](https://www.marketsandmarkets.com/Market-Reports/geography/ai-in-education-market/North-America) · [AfriLabs / WISE — Harnessing AI for Higher Education in Africa](https://www.afrilabs.com/?p=7452)

Capa de datos de entrenamiento (KT datasets) — agregado en el pase 7: [EdNet](https://github.com/riiid/ednet) · [XES3G5M](https://github.com/ai4ed/XES3G5M) · [FoundationalASSIST (arXiv 2602.00070)](https://arxiv.org/abs/2602.00070) · [XES3G5M (OpenReview)](https://openreview.net/pdf?id=Mn9oHNdYCE)

Tutores y memoria de agente — agregado en el pase 7: [tutor-gpt](https://github.com/plastic-labs/tutor-gpt) · [Honcho](https://github.com/plastic-labs/honcho) · [ChatTutor](https://github.com/HugeCatLab/ChatTutor) · [llamatutor](https://github.com/Nutlope/llamatutor) · [ABench / ProHist-Bench](https://github.com/inclusionAI/ABench) · [ProHist-Bench (arXiv 2604.24690)](https://arxiv.org/abs/2604.24690)

Seguridad pedagógica — agregado en el pase 7: [EduZone (arXiv 2608.02024)](https://arxiv.org/abs/2608.02024) · [AIriskEval-edu (arXiv 2607.01934)](https://arxiv.org/abs/2607.01934) · [L2-Bench (arXiv 2607.08842)](https://arxiv.org/abs/2607.08842) · [L2-Bench (sitio OUP)](https://benchmarks.elt.edu.oup.com/)

Capa de contenido curricular (OER) — agregado en el pase 10: [osbooks-calculus-bundle](https://github.com/openstax/osbooks-calculus-bundle) · [osbooks-biology-bundle](https://github.com/openstax/osbooks-biology-bundle) · [osbooks-college-physics-bundle](https://github.com/openstax/osbooks-college-physics-bundle) · [openstax-mcp-server](https://github.com/pythpythpython/openstax-mcp-server) · [mcp-tutor](https://github.com/moarshy/mcp-tutor) · [DSpace](https://github.com/DSpace/DSpace) · [Pressbooks](https://github.com/pressbooks/pressbooks) · [Manifold](https://github.com/ManifoldScholar/manifold) · [openstax-cms](https://github.com/openstax/openstax-cms) · [LibreTexts/shapeshift](https://github.com/LibreTexts/shapeshift) · [LibreTexts/conductor](https://github.com/LibreTexts/conductor) · [Creative Commons — Using CC-Licensed Works for AI Training](https://creativecommons.org/using-cc-licensed-works-for-ai-training-2/) · [Schools Week — Oak will allow commercial use of its lessons](https://schoolsweek.co.uk/oak-national-academy-will-allow-commercial-use-of-its-lessons/)

Infraestructura pública desplegada — agregado en el pase 10: [SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) · [Sunbird-Ed (org)](https://github.com/Sunbird-Ed) · [project-sunbird (org)](https://github.com/project-sunbird) · [Ed-Fi-ODS](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) · [Ed-Fi-Data-Standard](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) · [Ed-Fi — what is Ed-Fi](https://www.ed-fi.org/what-is-ed-fi/) · [DPI Global — DIKSHA](https://dpi.global/globaldpi/diksha) · [EkStep — DIKSHA learnings](https://ekstep.org/)

Mercado y política por región — agregado en el pase 10: [Technavio — AI in the education sector](https://technavio.com/report/artificial-intelligence-market-in-the-education-sector-industry-analysis) · [Azumo — AI in education statistics 2026](https://azumo.com/artificial-intelligence/ai-insights/ai-in-education-statistics) · [TechWire Asia — India AI curriculum from Class 3](https://techwireasia.com/2025/11/india-ai-curriculum-schools-2026/) · [TechWire Asia — mandatory AI literacy: China joins UAE and India](https://techwireasia.com/2026/04/ai-literacy-national-education-workforce/) · [ABC News — why some countries are moving fast on AI in schools](https://www.abc.net.au/news/2026-05-31/schools-in-asia-embracing-ai/106703054) · [Council of Europe — AI and education](https://www.coe.int/en/web/education/artificial-intelligence-and-education) · [CompTIA — five tech trends shaping EMEA IT strategy 2026](https://www.comptia.org/en/blog/five-tech-trends-shaping-emeas-it-strategy-in-2026/) · [UNU/UNESCO — AI implementation in higher education in LAC](https://unu.edu/publication/ai-implementation-higher-education-latin-america-and-caribbean) · [BID — An Enabling Regulatory Framework for AI in LAC](https://publications.iadb.org/publications/english/document/An-Enabling-Regulatory-Framework-for-Artificial-Intelligence-in-Latin-America-and-the-Caribbean.pdf)

Regulación y mercado por región — agregado en el pase 7: [MultiState — AI in Education Legislation: 2026 State Policy Trends](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session) · [ExcelinEd — State K-12 AI Policy in 2026](https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/) · [NASBE — States Take Next Steps on Governing AI Use in Schools](https://www.nasbe.org/states-take-next-steps-on-governing-ai-use-in-schools/) · [AASA — National framework for AI from students in all 50 states](https://www.aasa.org/news-media/news/2026/08/03/students-produce-national-framework-for-ai-in-america's-schools) · [Latham & Watkins — AI Regulation in APAC](https://www.lw.com/en/insights/ai-regulation-in-apac-diverging-approaches-across-the-region) · [CX Network — How 9 APAC countries are regulating AI](https://www.cxnetwork.com/artificial-intelligence/articles/ai-regulation-in-apac-current-developments-and-key-areas) · [Ken Research — Asia-Pacific AI in Education Market](https://www.kenresearch.com/industry-reports/asia-pacific-ai-in-education-market) · [UNESCO — Observatory on AI in Education for LAC](https://www.unesco.org/en/articles/unesco-launches-observatory-artificial-intelligence-education-latin-america-and-caribbean) · [UNESCO — Public–private partnership advances the Regional Observatory](https://www.unesco.org/en/articles/public-private-partnership-advances-regional-observatory-artificial-intelligence-education-led) · [EU AI Act — regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

Accesibilidad y educación especial — agregado en el pase 8: [accessibility-agents](https://github.com/Community-Access/accessibility-agents) · [OptiKey](https://github.com/OptiKey/OptiKey) · [Cboard](https://github.com/cboard-org/cboard) · [tero](https://github.com/marcorojasb/tero) · [Ronda App](https://github.com/ronda-ai/Ronda-App) · [noggimigo](https://github.com/Noggin-Labs/noggimigo) · [Swar-Setu](https://github.com/AyushBinjola1/Swar-Setu) · [aba-clinical-agent](https://github.com/open-behavior-analysis/aba-clinical-agent) · [Teacher-Hub / UnStuck](https://github.com/SabioTechTeam/Teacher-Hub) · [EyeEP](https://github.com/100205ivan/EyeEP) · [SEALApplication](https://github.com/Autism-Technology-Research-Syndicate/SEALApplication) · [Sign-Language-Interpreter](https://github.com/classifiedstudentkabir/Sign-Language-Interpreter)

Accesibilidad — regulación y mercado, pase 8: [European Accessibility Act — impacto en e-learning (BESA)](https://www.besa.org.uk/news/the-european-accessibility-act-eaa-and-its-impact-on-e-learning-what-you-need-to-know/) · [EAA y LMS (Synergy Learning)](https://synergy-learning.com/blog/european-accessibility-act-eaa-lms/) · [EAA para e-learning (ReadSpeaker)](https://www.readspeaker.com/blog/european-accessibility-act-e-learning/) · [US ED — Final Priority on Advancing AI in Education (Federal Register, 2026-04-13)](https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing) · [AI for Education — State AI Guidance tracker](https://www.aiforeducation.io/ai-resources/state-ai-guidance) · [NYC Public Schools — AI guidance for educators (2026-03-24)](https://www.schools.nyc.gov/home/2026/03/24/new-york-city-public-schools-announces-release-of-ai-guidance-for-educators-and-school-leaders) · [CIDDL — Navigating AI in IEP Development](https://ciddl.org/navigating-ai-in-iep-development-a-framework-for-ethical-practice/) · [Open edX — Proctoring UI proposal](https://openedx.atlassian.net/wiki/spaces/OEPM/pages/5336334337/Proposal+Proctoring+UI+A+Free+Open+Source+Browser-Lockdown+and+AI-Assisted+Exam+Integrity+Tool) · [Ipsos Education Monitor 2026 — APAC](https://www.ipsos.com/en-th/different-rules-different-technologies-how-asia-pacific-thinking-about-education-ai-and-future)

⚠️ *Del pase 8: los doce enlaces a `github.com` se abrieron de primera mano (licencia, stars, commits y descripción leídos en la página del repo). Los enlaces de **regulación y mercado provienen de resultados de búsqueda, no de la página abierta** — incluidas las fechas del EAA y las prohibiciones de IEP de Delaware y Nueva York. **Confirmar el texto normativo antes de citarlo en material de cliente.***


⚠️ *Del pase 7: se abrieron de primera mano sólo los enlaces a `github.com`. `arxiv.org`, `huggingface.co`, `benchmarks.elt.edu.oup.com` y `aivet-training.eu` están **bloqueados por el proxy de egreso** (reintentados en este pase); las fuentes de regulación y mercado provienen de resultados de búsqueda, no de la página abierta. Se dejan los enlaces para que una corrida con otra configuración de red los verifique.*

⚠️ *De las fuentes del pase 5, sólo los enlaces a `github.com` pudieron abrirse: `arxiv.org`, `unu.edu`, `coe.int`, `aclanthology.org` y `huggingface.co` están bloqueados por el proxy de egreso de este entorno. Se dejan los enlaces para que una corrida con otra configuración de red los verifique.*

Regulación — agregado en el pase 3: [Korea AI Basic Act guide (Casrai)](https://casrai.org/guides/korea-ai-basic-act) · [Latham & Watkins — AI regulation in APAC](https://www.lw.com/en/insights/ai-regulation-in-apac-diverging-approaches-across-the-region) · [KJK — Ohio's July 1 2026 school AI policy deadline](https://kjk.com/2026/06/12/ohios-july-1-2026-school-ai-policy-deadline-what-districts-educators-and-parents-need-to-know/) · [EdWeek — Ohio requires AI policies for all K-12 schools](https://marketbrief.edweek.org/regulation-policy/ohio-is-requiring-ai-policies-for-all-k-12-schools-will-other-states-follow/2025/08) · [Ohio DEW model AI policy (PDF)](https://education.ohio.gov/getattachment/Topics/AI-in-Ohio-s-Education/Model-Policy/AI-In-Education-Model-Policy.pdf.aspx?lang=en-US) · [Williams Mullen — Virginia AI guidance for schools](https://www.williamsmullen.com/insights/news/legal-news/virginia-establish-guidance-artificial-intelligence-schools) · [VPM — HB 1186 / SB 394](https://www.vpm.org/general-assembly/2026-03-25/hb1186-sb394-ai-guidance-schools-pekarsky-rasoul-spanberger-heny/) · [FutureEd — 2026 state AI in education bill tracker](https://www.future-ed.org/legislative-tracker-2026-state-ai-in-education-bills/)

Repos y verticales — pase 3: [Claw-ED](https://github.com/SirhanMacx/Claw-ED) · [GegoK12](https://github.com/Gego-K12/gegok12) · [AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent)

Mercado regional — pase 3: [Azumo — AI in education statistics 2026](https://azumo.com/artificial-intelligence/ai-insights/ai-in-education-statistics) · [EdTech Hub — AI in education in MENA](https://docs.edtechhub.org/lib/EPJAMMH9/download/BHXDDPBB) · [Ipsos — APAC education, AI and the future](https://www.ipsos.com/en-th/different-rules-different-technologies-how-asia-pacific-thinking-about-education-ai-and-future)

Regulación: [MultiState — AI in education legislation 2026](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session) · [ExcelinEd — K-12 AI policy 2026](https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/) · [EU AI Act in education](https://aiadopt.eu/en/insights/eu-ai-act-education) · [Uniwise — Annex III diciembre 2027](https://uniwise.eu/resources/blog/the-eu-ai-act-and-assessment-december-2027-is-not-a-snooze-button) · [Xenoss — APAC AI regulations](https://xenoss.io/blog/asia-pacific-apac-ai-regulations) · [FPF — AI regulation in Latin America](https://fpf.org/blog/ai-regulation-in-latin-america-overview-and-emerging-trends-in-key-proposals/) · [Baker McKenzie — LATAM AI regs](https://connectontech.bakermckenzie.com/emerging-ai-regulations-in-latin-america-what-multinationals-need-to-know/)

Plataformas y repos: [Moodle AI tools docs](https://docs.moodle.org/502/en/AI_tools) · [Moodle AI plugin types](https://moodledev.io/docs/5.0/apis/plugintypes/ai) · [Moodle 5.2 release](https://edzlms.com/moodle-5-2-release-ai-integration-smarter-courses-elearning/) · [AITutor-EvalKit (arXiv 2512.03688)](https://arxiv.org/abs/2512.03688) · [Latam-GPT / CENIA](https://www.opensourceforu.com/2026/02/chile-launches-open-source-latam-gpt-to-power-latin-americas-ai-sovereignty/)

LATAM: [Nivelics — impacto AI empresas LATAM 2026](https://www.nivelics.com/en/blog/impacto-ia-empresas-latam-2026) · [VuraOS — mapa de adopción LATAM](https://vuraos.com/en/blog-mapa-adopcion-latam)

**Agregado en el pase 4 (2026-09-30):**

Regulación EMEA — Digital Omnibus: [Gibson Dunn — EU AI Act Omnibus agreement, postponed high-risk deadlines](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) · [Usercentrics — EU AI Act high-risk delay, Article 50 transparency](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/) · [Uniwise — December 2027 is not a snooze button (assessment)](https://uniwise.eu/resources/blog/the-eu-ai-act-and-assessment-december-2027-is-not-a-snooze-button) · [European Commission — AI Act regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

Regulación APAC: [Latham & Watkins — AI regulation in APAC](https://www.lw.com/en/insights/ai-regulation-in-apac-diverging-approaches-across-the-region) · [CX Network — how 9 APAC countries regulate AI](https://www.cxnetwork.com/artificial-intelligence/articles/ai-regulation-in-apac-current-developments-and-key-areas) · [OneTrust — where AI regulation is heading in 2026](https://www.onetrust.com/blog/where-ai-regulation-is-heading-in-2026-a-global-outlook/)

Regulación North America: [MultiState — AI in education legislation, 2026 state policy trends](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session) · [NASBE — states take next steps on governing AI use in schools](https://www.nasbe.org/states-take-next-steps-on-governing-ai-use-in-schools/) · [ExcelinEd — K-12 AI policy 2026 milestones](https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/) · [AASA — students from all 50 states produce national AI framework](https://www.aasa.org/news-media/news/2026/08/03/students-produce-national-framework-for-ai-in-america's-schools)

Mercado LATAM: [Digital Education Council — AI in Higher Education LATAM Survey 2026](https://www.digitaleducationcouncil.com/dec-insights/92-of-students-and-79-of-faculty-actively-engaging-with-ai-findings-from-ai-in-higher-education-latam-survey-2026) · [DEC — AI adoption nearly universal among students](https://www.digitaleducationcouncil.com/post/ai-adoption-is-nearly-universal-among-students-but-confidence-is-not)

Mercado APAC y global: [Ken Research — Asia-Pacific AI in education market to 2030](https://www.kenresearch.com/industry-reports/asia-pacific-ai-in-education-market) · [HolonIQ — 2026 education trends snapshot](https://www.holoniq.com/notes/2026-education-trends-snapshot) · [Azumo — AI in education statistics 2026](https://azumo.com/artificial-intelligence/ai-insights/ai-in-education-statistics)

Repos y benchmarks: [MathTutorBench](https://github.com/eth-lre/mathtutorbench) · [UnifyingAITutorEvaluation](https://github.com/kaushal0494/UnifyingAITutorEvaluation) · [pyKT](https://github.com/pykt-team/pykt-toolkit) · [TutorIA](https://github.com/LabSirius/TutorIA) · [OpenDidactia](https://github.com/nmarafo/OpenDidactia) · [FreeLingo](https://github.com/artcc/freelingo) · [mentar](https://github.com/avps82/mentar)

Capa de telemetría (LRS / xAPI) — agregado en el pase 6, **todo verificado de primera mano en GitHub**: [lrsql (Yet Analytics)](https://github.com/yetanalytics/lrsql) · [Ralph (OpenFun)](https://github.com/openfun/ralph) · [ADL_LRS (ADL)](https://github.com/adlnet/ADL_LRS) · [Learning Locker](https://github.com/LearningLocker/learninglocker) · [learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) · [ERPNext](https://github.com/frappe/erpnext)

Evaluación — agregado en el pase 6, 🔴 **no verificado de primera mano** (dominios bloqueados por el proxy): L2-Bench (arXiv 2607.08842) · metodología de L2-Bench (arXiv 2603.20088) · `benchmarks.elt.edu.oup.com` · dataset en HuggingFace bajo `OUP/`

Regulación y mercado por región — agregado en el pase 6: [MultiState — AI in Education Legislation: 2026 State Policy Trends](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session) · [NASBE — States Take Next Steps on Governing AI Use in Schools](https://www.nasbe.org/states-take-next-steps-on-governing-ai-use-in-schools/) · [ExcelinEd — State K-12 AI Policy in 2026](https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/) · [Latham & Watkins — AI Regulation in APAC](https://www.lw.com/en/insights/ai-regulation-in-apac-diverging-approaches-across-the-region) · [Xenoss — APAC AI regulations](https://xenoss.io/blog/asia-pacific-apac-ai-regulations) · [UNESCO — Observatory on AI in Education for LAC](https://www.unesco.org/en/articles/unesco-launches-observatory-artificial-intelligence-education-latin-america-and-caribbean) · [Compliance & Risks — LATAM AI legislation](https://www.complianceandrisks.com/blog/shaping-the-future-ai-legislative-initiatives-across-latin-america/) · [IDB — An Enabling Regulatory Framework for AI in LAC](https://publications.iadb.org/publications/english/document/An-Enabling-Regulatory-Framework-for-Artificial-Intelligence-in-Latin-America-and-the-Caribbean.pdf) · [Azumo — AI in Education Statistics 2026](https://azumo.com/artificial-intelligence/ai-insights/ai-in-education-statistics) · [Grand View Research — AI Tutors Market](https://www.grandviewresearch.com/industry-analysis/ai-tutors-market-report) · [EdTech Hub — AI in Education in MENA](https://docs.edtechhub.org/lib/EPJAMMH9/download/BHXDDPBB)

## Nota de método del pase 19 (2026-10-01) — el pase que ejecutó las dos acciones escritas, y las dos dieron "no" (que es un resultado)

Tres pases consecutivos ejecutaron acciones escritas por el anterior. Éste también, y es **el primero en el que las
dos devuelven negativo** — una refutada y una no encontrada. Las dos se registran como hallazgo, porque un negativo
medido con control es información y el silencio se parece demasiado a la cobertura.

### Acción 1 — «buscar si PrivacyCD publicó código (gap 31)» → **NO. Gap 31 sigue abierto, con la búsqueda documentada**

Se buscó por los términos que el pase 18 dejó escritos. **Lo que confirmó:** la autoría completa (Mingliang Hou,
Yinuo Wang, Teng Guo, Zitao Liu, Wenzhou Dou, Jiaqi Zheng, Renqiang Luo, Mi Tian, Weiqi Luo — los tres nombres que el
pase 18 anticipó están en la lista) y el algoritmo **HIF** (*hierarchical importance-guided forgetting*: explota que
la importancia de parámetros en un CDM tiene estructura por capas, con suavizado que combina importancia individual y
de capa; experimentos sobre tres datasets reales). **Lo que no apareció: código.** Ni repo localizable ni enlace en
los resultados.

**Y la búsqueda devolvió algo que no se buscaba, que es el verdadero aporte de esta acción:** **P-MIA** (arXiv
2511.04716), del mismo grupo — el **ataque** correspondiente al **defensa** de PrivacyCD. Los dos lados del mismo
problema, publicados por el mismo entorno, **y ninguno de los dos libera implementación**. Ver la tendencia **50**.

### Acción 2 — «medir el disparador del gap 32 por el lado del evento» → **REFUTADA. La hipótesis era al revés, y el gap 32 se cierra**

El pase 18 llamó a esto *«la hipótesis más barata que esta KB tiene abierta»*: que el Privacy API **emite un evento al
aprobar un pedido** y que, si es observable, el puente es un `db/events.php` de diez líneas. **Se midió sobre el árbol
real y es falso.** Verificado con clon *sparse* de `moodle/moodle` en `main` (= 5.3rc1):

- `public/admin/tool/dataprivacy/db/events.php` registra **exactamente un** observer, y va **hacia adentro**: escucha
  `\core\event\user_deleted` para **crear** un pedido de borrado
  (`user_deleted_observer::create_delete_data_request`, y sólo si la config `automaticdeletionrequests` está activa).
  **Es el sentido contrario al que hacía falta.**
- **`tool_dataprivacy` no emite ningún evento.** Recorridos los **187 archivos** del subárbol: **cero** llamadas a
  `trigger()`.
- `api::update_request_status()` —por donde pasa `approve_data_request()`— es **una escritura de base de datos y nada
  más**: setea `status`, opcionalmente `dpo` y `dpocomment`, y llama a `$datarequest->update()`. **Sin evento, sin
  hook, sin notificación.**

**Control negativo, porque la conclusión es una ausencia:** el mismo `api.php` tiene **1.678 líneas** y
`approve_data_request()` está en la **línea 642**. El archivo existía y el grep era válido; **la ausencia es real, no
un error de ruta** — que es precisamente el error que este pase tuvo que corregirle al anterior.

**El gap 32 se cierra refutado, y deja dos caminos** (ver **P40**): **(a)** sondear `tool_dataprivacy_request.status`,
la única superficie observable que existe, o **(b)** disparar desde afuera, como hace el único antecedente conocido,
**`local_gdpr_deleteuserdata`** (GPL-3.0, expone el borrado del Privacy API como web-service). ⚠️ Antecedente, **no
dependencia**: es de **2018-07-08**, declara requerir **Moodle 3.5** —el núcleo va por 5.3—, `moodle.org` está
bloqueado por el proxy y **no se localizó repositorio en GitHub**.

### Lo que se verificó de primera mano, y con qué herramienta

Este pase cambió de instrumento, y conviene dejar escrito por qué: **WebFetch infiere, `git` lista.** Preguntado por
la rama por defecto de `moodle/moodle`, WebFetch contestó «main» leyendo la página renderizada — y acertó por
casualidad, porque la misma consulta sobre rutas devolvió dos 404 que no significaban ausencia.

- ✅ **`git ls-remote --heads`** sobre `moodle/moodle`: `refs/heads/main` → `85af0b5`. **Lista refs, no infiere.** Es
  la herramienta correcta para la pregunta de la rama y cuesta un segundo.
- ✅ **Clon `--depth 1 --filter=blob:none --sparse`** de `moodle/moodle`: el árbol real, `main` = **Moodle 5.3rc1**.
  Sobre él se auditaron los 10 archivos de privacidad, los 7 shims (línea por línea), `core_ai` (~800 líneas),
  `db/events.php`, `api.php` y los 187 archivos de `tool_dataprivacy`.
- ✅ **WebFetch** sobre los repos de GitHub: licencia, estrellas, commits y descripción de los 5 agentes nuevos,
  OpenUnlearning, `MachineUnlearning`, `torchunlearn`, `jjbrophy47/machine_unlearning`, Ralph, `lrsql` y Learning
  Locker.

### ⚠️ Advertencia 1 — un 404 nunca dice «no existe»; dice «no está donde preguntaste». Tercera vez.

El pase 17 leyó sus 404 como **ausencia de la pieza**. El pase 18 los leyó como **nombre de rama** y escribió una
afirmación falsa (*«`moodle/moodle` no tiene rama `main` ni `master`»*). La causa real era una **tercera**: Moodle
movió su *webroot* a **`public/`** en la serie 5.x, así que en `main` la ruta es `public/ai/...` y no `ai/...`. Los
mismos 404 del pase 18 son consistentes con esto: 404 en `main` (ruta movida) y 200 en `MOODLE_405_STABLE` y
`MOODLE_500_STABLE`, donde `ai/` todavía estaba en la raíz. **Su tabla de evidencia era correcta; su explicación no.**

**Dos consecuencias operativas, para no repetirlo:**

1. **Toda ruta de Moodle que esta KB escriba tiene que decir contra qué serie se resolvió.** La 5.x las movió todas.
2. **Dos de los tres «404 = no está en el núcleo» del pase 18 medían un nombre, no una ausencia:** `anthropic` **sí**
   está, y `bedrock` se llama **`awsbedrock`**.

### ⚠️ Advertencia 2 — «la oferta es grande» se midió con los repos equivocados, y el error es de tamaño, no de signo

El pase 18 cerró la capa de *unlearning* con *«la oferta existe, es grande y es toda MIT/Apache»*. La conclusión es
correcta; la medición no. **Sus dos piezas ejecutables tienen 12 ★ cada una**, y lo que tenía cientos de estrellas
(`jjbrophy47/machine_unlearning`, 965 ★, reverificado: **sigue sin licencia**) es una **bibliografía**. La pieza seria
de la capa —**OpenUnlearning**, MIT, **607 ★**, CMU, con TOFU/MUSE/WMDP y métricas de *membership inference*— **no
estaba registrada en esta KB**. Lección: **contar estrellas sin separar código de bibliografía produce una conclusión
correcta por accidente**, y la próxima vez puede producir una incorrecta.

### ⚠️ Advertencia 3 — el barrido regional sigue saturado, y esta vez hay un dato nuevo igual

El pase 12 declaró saturación del barrido regional y el pase 17 la confirmó. Este pase la confirma otra vez: las
cuatro consultas regionales devolvieron **cifras que la KB ya tenía** (134 proyectos en 31 estados, 92 %/79 % del
Digital Education Council, Reglamento (UE) 2026/1744 con el Anexo III en 2027-12-02, AB 1159). **Se registra como
confirmación, no como hallazgo.** Lo único genuinamente nuevo es **APAC**, y es preciso: la **Ley de IA de Vietnam
N.º 134/2025/QH15** y su **Decisión 33** (ver `intel/market.md`). La KB tenía la clasificación de Vietnam en términos
generales desde el pase 5; no tenía **el instrumento, los tres incisos ni las dos fechas de cumplimiento**.

### Lo que este pase NO hizo, declarado como tal

- **No se leyó ningún paper en fuente primaria.** `arxiv.org` sigue bloqueado por el proxy, igual que en los pases 6,
  7, 14, 16, 17 y 18. **P-MIA (2511.04716) y PrivacyCD (2511.03966) vienen de snippets concordantes** y se anotan con
  su número **para que el próximo pase los abra**, no para citarlos ante un cliente.
- **No se verificó la API de borrado de Learning Locker.** El «sí» viene de una fuente secundaria (Learning Pool). Es
  el único «sí» de la tabla del gap 33 y **es el que más conviene confirmar**, porque es el que decide si la única
  salida de la capa de telemetría es copyleft.
- **No se probó el sondeo de `tool_dataprivacy_request`.** P40 describe el mecanismo leyendo el esquema y el flujo de
  `update_request_status()`; **no se ejecutó contra una instancia de Moodle**. Es diseño verificado en el fuente, no
  integración probada.
- **No se verificó `local_gdpr_deleteuserdata` de primera mano** ni se localizó su repositorio. `moodle.org` sigue
  bloqueado y el directorio oficial de plugins sigue sin auditarse — es la cuarta pasada consecutiva con esta misma
  limitación.
- **No se auditó el árbol de `canvas-lms`.** Cuarta pasada que lo declara **no buscado, no inexistente**.
- **No se verificó archivo por archivo la doble licencia de `human-skill-tree`.** El repo declara AGPL-3.0 con el
  directorio `skills/` en doble MIT/AGPL; **eso se tomó del README**, y antes de facturar hay que leer los encabezados
  del subárbol.

### 🔵 Las tres acciones que este pase deja escritas para el siguiente

1. **Confirmar la API de borrado de Learning Locker** (gap 33). Es la pregunta de mayor rendimiento del pase: si el
   «sí» se confirma, la única forma estándar de borrar telemetría de aprendizaje es **GPL-3.0**, y eso es una
   restricción de arquitectura que hay que decirle al cliente **antes** de elegir LRS. Buscar por
   `learninglocker statement delete API`, por su documentación de administración y por el repo de `xapi-service`.
2. **Construir el *harness* del gap 34**, que es lo más construible que tiene esta KB y no requiere investigación:
   tomar `pyKT` (MIT, PyTorch), aplicarle un método de `torchunlearn` (MIT) y **medirlo con las métricas de
   *membership inference* de OpenUnlearning** (MIT). Las tres piezas son permisivas y ya existen. El entregable es el
   número que hoy **P38** no puede prometer.
3. **Abrir P-MIA (2511.04716) y PrivacyCD (2511.03966) en fuente primaria** si algún pase consigue `arxiv.org`, o
   buscar sus versiones en otro alojamiento. La tendencia 50 sostiene una recomendación de diseño —ruido o
   cuantización en el vector de estado expuesto— sobre **snippets**, y esa recomendación va a llegar a una propuesta.
## Nota de método del pase 18 (2026-10-01) — el tercer pase que ejecuta acciones escritas, y el primero que descubre que una ausencia de la KB era un error de rama

Este pase ejecutó **las dos acciones** que el pase 17 dejó escritas, y las dos dieron resultado. Conviene registrar
que es el tercer pase consecutivo donde una acción escrita por el pase anterior se convierte en hallazgo verificado
(pases 14, 17 y 18): **el mecanismo de dejar acciones textuales está funcionando** y vale protegerlo.

### Acción 1 — «construir y medir el `privacy provider` de referencia para un plugin de AI de Moodle (gap 29)»

No hubo que construirlo. **Existe, y son tres, y están en el núcleo de Moodle.** Lo que este pase sí tuvo que hacer
fue entender **por qué el pase 17 no los encontró**, y la respuesta es mecánica y reutilizable: **`moodle/moodle` no
tiene rama `main` ni `master`**. Los cuatro 404 que el pase 17 registró con honestidad midieron el nombre de la
rama, no una ausencia.

### Acción 2 — «buscar procedencia por los términos del dominio de ML; `machine unlearning` es el término que este pase no buscó»

Se buscó y **la predicción del pase 17 se cumplió literalmente**: hay una capa de 2.700+ ★, toda MIT/Apache-2.0, y
contiene librerías aplicables a *knowledge tracing*. El gap 30 cambia de forma, como el pase 17 anticipó, y se
reformula en los **gaps 31 y 32**.

### Lo que se verificó de primera mano

1. **Siete rutas de `moodle/moodle` probadas por código HTTP** contra `raw.githubusercontent.com` en cuatro ramas
   (`main`, `master`, `MOODLE_405_STABLE`, `MOODLE_500_STABLE`). De ahí sale la corrección del pase 17 y el cierre
   del gap 29.
2. **Tres `privacy provider` leídos en el archivo fuente crudo**, no en la página rendida: el del núcleo
   (`aiprovider_openai`), el de Ferrara (`aiprovider_gemini`) y el brasileño (`local_aihub`). Se leyeron las
   declaraciones de clase, las interfaces, los nombres de método y el contenido de `get_metadata()`.
3. **Las cadenas de idioma de privacidad de `aiprovider_openai` y `aiprovider_ollama`**, citadas literal. De ahí
   sale la lectura de la palabra «explicitly», que es el aporte más accionable del pase para un expediente de
   cliente.
4. **`classes/privacy/` abierto en seis repos de la comunidad** para contar cuántos tienen `provider.php`: tres sí,
   tres no.
5. **Nueve repos de la capa de *unlearning* y procedencia** abiertos uno por uno para licencia, estrellas, forks y
   condición de fork.

### ⚠️ Advertencia 1 — la página rendida contradijo al fuente, y el fuente ganó

El resumen de la página de `Universita-di-Ferrara/moodle-aiprovider_gemini` afirmaba que **todos** los métodos del
provider estaban vacíos y que por tanto el plugin **no declaraba** el envío externo a Google. **Eso iba a escribirse
como el hallazgo del pase**: un defecto de cumplimiento en una pieza universitaria europea. **Leyendo el `.php`
crudo, el plugin declara `add_external_location_link` con cuatro campos** (`prompttext`, `model`, `numberimages`,
`responseformat`) y un propósito. La afirmación habría sido **falsa y acusatoria**.

**La regla que queda:** para una afirmación de **cumplimiento** —positiva o negativa— se lee el fuente, no el
resumen de la página. Es la tercera variante del mismo problema de método en esta KB (pase 10: README vs `LICENSE`;
pase 16: sidebar vs archivo de licencia; ahora: página rendida vs fuente).

### ⚠️ Advertencia 2 — el primer resultado de búsqueda fue un fork con 0 estrellas

Buscando `open-unlearning` el primer resultado fue **`aflah02/open-unlearning`**: README idéntico, licencia
idéntica, misma lista de métodos, **0 ★ y 0 forks**. El canónico es **`locuslab/open-unlearning`, 607 ★ y 164
forks**. Lo único que distingue a uno del otro es el campo «forked from» y el contador. **Ningún repo entra a una
tabla de esta KB sin mirar si es fork** — es el mismo error que el pase 7 cometió con MRBench.

### ⚠️ Advertencia 3 — el tercer lugar donde puede estar la licencia

`alvarogregori/moodle-ai-graded-assignment` **no tiene archivo `LICENSE`, no muestra licencia en el sidebar y no la
menciona en el README** — y el header de cada `.php` declara GPL-3.0-or-later. Para un plugin de Moodle es lo
esperable, pero **un header de archivo no es una concesión de licencia del repositorio**. Regla operativa: **sin
`LICENSE`, se trata como sin licencia a efectos de cotización.**

### Lo que este pase NO hizo, declarado como tal

- **No se auditó el árbol de `canvas-lms`.** Igual que el pase 17, la ausencia de un toolset de retiro comparable
  se declara **no encontrada, no inexistente**.
- **`jjbrophy47/machine_unlearning` (965 ★) y `Awesome-Diffusion-Model-Unlearning` (67 ★) no muestran licencia.**
  Se abrieron y se confirmó que existen y que **ninguno declara licencia** — están en las tablas como *sin licencia
  declarada*, usables como bibliografía y no como dependencia. Lo que corresponde es un *issue* pidiendo el archivo.
- **No se leyó ningún paper en la fuente primaria.** `arxiv.org` está bloqueado por el proxy. Todo lo que se afirma
  de PrivacyCD, SalUn, torchunlearn y la survey de ACM TIST viene de **snippets concordantes**. Los números de
  arXiv se registran para que el próximo pase los abra, no para citarlos ante un cliente.
- **No se probó `torchunlearn` sobre `pyKT`.** La afirmación de que es «aplicable en principio» se basa en que
  ambos son PyTorch, **no en una integración ejecutada**. P38 lo dice en su advertencia en vez de prometer que
  funciona.
- **No se buscó jurisprudencia ni sanciones aplicadas** sobre el derecho de supresión aplicado a modelos. Se
  registró qué exige cada régimen, no cómo se está aplicando.
- **No se revisó el directorio de plugins de Moodle**: `moodle.org` sigue bloqueado. El conteo de seis piezas de la
  comunidad es de lo encontrado en GitHub, no del directorio oficial.

### 🔵 Las dos acciones que este pase deja escritas para el siguiente

1. **Buscar si PrivacyCD publicó código** (gap 31). Buscar por `HIF unlearning cognitive diagnosis`, por los
   nombres de los autores (**Zitao Liu**, **Weiqi Luo**, **Teng Guo** — el mismo grupo publica herramienta open
   source con frecuencia) y por la organización de `pyKT`, que es del mismo entorno. **Si aparece, P38 mejora y el
   gap 31 se cierra.** Si no aparece, verificar las licencias pendientes de `jjbrophy47/machine_unlearning` y
   abrir *issues* de licencia en `mod_aigradedassign` y `tool_aiconnect`.
2. **Medir el disparador del gap 32 por el lado del evento, no del borrado.** Este pase buscó «quién borra el
   modelo» y no encontró puente. La próxima consulta tiene que ser por el **mecanismo de evento de Moodle**:
   `moodle event observer privacy delete`, `core_privacy delete_data_for_user hook external`, y por el lado del
   LRS, `xAPI delete statements forget`. El Privacy API **emite un evento al aprobar un pedido**, y si ese evento
   es observable, el gap 32 deja de ser investigación y pasa a ser un `db/events.php` de diez líneas. **Esa es la
   hipótesis más barata que esta KB tiene abierta.**

## Nota de método del pase 17 (2026-10-01) — el segundo pase que ejecuta una acción escrita por un gap anterior, y van dos de dos

El pase 14 dejó registrado que **no tuvo que inventar la pregunta**: el gap 19 se la había dejado escrita, y
cerrarla funcionó. Este pase repitió el método **con dos acciones escritas a la vez**, y las dos pagaron:

1. **La del gap 26 (pase 15):** *«medir el canal otra vez, pero buscando por `SKILL.md` + dominio educativo en
   vez de por repos educativos».* Resultado: **el gap 20 se cerró** y el techo permisivo del canal educativo pasó
   de 299 a 541 ★.
2. **La del cierre del pase 16:** *«No se revisó la capa de privacidad de los LMS ya instalados (Moodle, Open
   edX, Canvas). Es el paso siguiente obvio: el dato del alumno ya está ahí, no en el agente.»* Resultado: una
   **capa nueva** y dos gaps nuevos (29 y 30).

**La conclusión de método, y ya tiene tres pasadas de evidencia (14, 17 y el fracaso relativo de las que
inventaron la pregunta):** cuando un gap deja escrita una acción concreta, ejecutarla rinde más que abrir una capa
nueva por intuición. **Conviene que cada pase cierre dejando una acción textual**, y este pase deja dos, abajo.

### Lo que se verificó de primera mano

Vía **WebFetch contra la página del repo** el 2026-10-01: `openedx/edx-platform` (AGPL-3.0, 8.2k ★, 4.4k forks) y
su árbol `scripts/user_retirement` (seis scripts leídos por nombre) y `lms/djangoapps/bulk_user_retirement` ·
`moodle/moodle` (GPL-3.0, 7.5k ★, 123.147 commits) · `instructure/canvas-lms` (AGPL-3.0, 6.9k ★) ·
`openeducat/openeducat_erp` (LGPL-3.0, 881 ★) · `anthropics/k12-teacher-skills` (Apache-2.0, 541 ★, `evals/`) ·
`learning-commons-org/agent-skills` (Apache-2.0, 35 ★, `evals/`) · `HKUDS/DeepTutor` (Apache-2.0, **40.6k ★**,
v1.6.12 del **2026-09-27** — **la fila de la KB ya estaba correcta**).

### ⚠️ Advertencia 1 — `curl -sI` no verifica nada en esta sesión, y ahora está probado con control negativo

El pase 16 anotó que `curl -sI` devolvió 403 en catorce repos y que ninguno era un 404. **Este pase lo probó
bien:** se consultaron tres repos reales (`instructure/canvas-lms`, `openedx/edx-platform`, `moodle/moodle`) y
**uno deliberadamente inexistente** (`github.com/this-definitely-does-not-exist-xyz123/nope`). **Los cuatro
devolvieron 403.** El proxy responde antes de llegar a GitHub, así que **un 403 no distingue un repo vivo de uno
que no existe** y `curl` no puede usarse para cumplir la regla de «verificar toda URL». La verificación válida en
esta sesión es **WebFetch contra la página del repo**. Dejar de intentar `curl` ahorra tiempo en cada pase.

### ⚠️ Advertencia 2 — seis dominios bloqueados, y dos afectan a citas que van a una propuesta

Bloqueados por el proxy de egreso en este pase: **`moodle.org`**, **`docs.moodle.org`**, **`docs.openedx.org`**,
**`privacyrights.org`**, **`calmatters.org`** y **`leginfo.legislature.ca.gov`**.

Las dos consecuencias que importan:

- **La cita de Open edX** (*«User retirement is not a compliance guarantee…»*) se leyó en el **snippet de
  búsqueda** de `docs.openedx.org`, **no en un fetch de primera mano**, y el `README` del directorio en GitHub
  —que sí se verificó— **no la contiene**. Se usa en tres archivos de esta KB: resolver contra la fuente oficial
  antes de ponerla en un documento para un cliente.
- **El Privacy API de Moodle, `tool_dataprivacy` y `tool_policy`** quedan registrados como **documentados por
  Moodle vía snippet**, no verificados de primera mano. Se intentó el árbol de `admin/tool/dataprivacy` por
  **cuatro rutas** (`main` y `master`, árbol y archivo) y **las cuatro dieron 404 vía WebFetch**. Del repo se
  verificó licencia, estrellas y commits.
- **AB 1159** no se pudo leer en `leginfo.legislature.ca.gov` ni en las dos fuentes de la organización
  patrocinante. Fechas, autoría, el texto de la prohibición y la vigencia de HESIPA provienen de **búsqueda
  extendida con múltiples fuentes concordantes** (incluido el comunicado de la oficina de la asambleísta), no de
  la fuente legislativa oficial. **Antes de citar la ley en un contrato, leer el texto chaptered.**

### ⚠️ Advertencia 3 — dos correcciones de este pase son sobre la propia KB, no sobre el mercado

- **El conteo de `agents/top.md`.** El encabezado dice 31 y la tabla tiene **32 filas**. No es un error nuevo: es
  la tercera vez que esta KB se pelea con este conteo (ver la corrección del pase 10). **La reconciliación es que
  una fila no es un agente:** `education-agent-skills` es una biblioteca de Markdown/YAML y está además en la capa
  de distribución por *skills* del mismo archivo. **32 filas = 31 agentes + 1 duplicado de otra capa.**
- **El encuadre COPPA del pase 16.** *«La voz de un menor es dato biométrico regulado desde el 2026-04-22»* tiene
  la conclusión correcta y la vía equivocada: la FTC **excluyó explícitamente** de la regla final los datos
  *derivados* de voz, rostro y marcha (estaban en el NPRM de 2024 y se quitaron por amplitud excesiva), mientras
  **`voiceprints` sí está en la enumeración**. Y un **archivo de audio con la voz de un chico ya estaba cubierto
  bajo 16 CFR 312.2 antes de las enmiendas** — la exposición es **más vieja**, no más nueva. Ver la corrección
  completa en `agents/top.md`.

### Lo que este pase NO hizo, declarado como tal

- **No se auditó el árbol de `canvas-lms`.** La ausencia de un toolset de retiro comparable al de Open edX se
  declara como **no encontrada**, no como inexistente.
- **No se verificó si `learning-commons-org/agent-skills` tenía `evals/` al momento del pase 12.** No se pudo
  datar la carpeta. Por eso el cierre del gap 20 registra la duda en vez de culpar al pase 12 o absolverlo.
- **No se midió el costo de cumplir AB 1159 sobre una arquitectura federada.** Se sabe que la excepción de la ley
  y el federado encajan conceptualmente; **cuánto cuesta producir la evidencia nadie lo midió acá**, y P37 lo dice
  en su advertencia en vez de prometer números.
- **No se buscó jurisprudencia ni sanciones aplicadas** — igual que el pase 16, se registró qué exige cada régimen
  y desde cuándo, no cómo se está aplicando.
- **No se revisó el directorio completo de plugins de Moodle.** `moodle.org` está bloqueado; lo que se afirma del
  ecosistema de plugins viene de snippets.

### 🔵 Las dos acciones que este pase deja escritas para el siguiente

1. **Construir y medir el `privacy provider` de referencia** para un plugin de AI de Moodle (gap 29). Es la pieza
   más chica de la capa, el núcleo la **exige** a todos los plugins, y no existe publicada. Buscar primero
   `moodle privacy provider ai plugin` y `moodle local plugin privacy provider example` antes de darla por
   inexistente.
2. **Buscar procedencia de dato de entrenamiento** (gap 30) por los términos del dominio de ML, no de educación:
   `training data provenance`, `dataset attestation`, `model card training data lineage`, `machine unlearning`.
   **`machine unlearning` es el término que este pase no buscó** y es el que podría tener oferta madura: si existe
   una librería permisiva de *unlearning* aplicable a modelos de knowledge tracing, el gap 30 cambia de forma.

## Nota de método del pase 16 (2026-10-01) — dieciséis pasadas preguntando qué sabe hacer el software, y la pregunta que faltaba era con qué derecho toca al alumno

Este pase no buscó una tecnología: buscó un **régimen**. El disparador fue medir el vocabulario de la propia KB
antes de investigar nada, sobre los ocho archivos:

| Término buscado | Apariciones antes del pase 16 |
|---|---|
| `COPPA` | **0** |
| `differential privacy` / `privacidad diferencial` | **0** |
| `federated` / `federado` | **0** |
| `FERPA` | **1**, de pasada, dentro de la descripción de un repo de otra capa |
| `sintétic` | 10, **todas como crítica** a un repo de la capa predictiva, ninguna como capacidad |

Quince pasadas y cinco de los seis términos que definen el tratamiento legal del dato de un menor no aparecían.
Ese conteo es el hallazgo del pase tanto como los repos.

### Lo que se verificó de primera mano

1. **Quince repos abiertos uno por uno vía WebFetch** para licencia, estrellas, forks, commits y lenguaje. Dos
   licencias **no estaban en el sidebar de GitHub y hubo que abrir el archivo**: `diffprivlib` (`LICENSE.md` →
   «MIT License», IBM Corporation 2018) y `SDV` (`LICENSE` → «Business Source License 1.1», licenciante DataCebo,
   Inc.). **En los dos casos la conclusión habría sido distinta leyendo sólo la página del repo.**
2. **El texto de la BUSL de SDV leído campo por campo** —*Change Date*, *Change License*, *Additional Use Grant*,
   la exclusión de *Synthetic Data Service*— porque de ahí sale la recomendación de no usarlo, y una recomendación
   negativa necesita la cita, no el resumen.
3. **La deprecación de OpenFL citada literal** desde su propia página, incluida la recomendación de migrar a
   Flower.
4. **Las cuatro fechas de la regla COPPA enmendada** (anuncio enero 2025, publicación 2025-04-22, vigencia
   2025-06-23, cumplimiento **2026-04-22**) cruzadas entre varias fuentes secundarias coincidentes.

### ⚠️ Advertencia 1 — `curl -sI` dio 403 en los catorce repos, y ninguno era un 404

El pase 12 ya había dejado escrito que **un 403 del proxy no es un 404**. Volvió a pasar, esta vez en el 100 % de
los casos: `curl -sI` contra `github.com` devolvió **403 en los catorce** URLs candidatas que se le pasaron, incluidas las de
10.000 y 7.200 estrellas. **Verificar con `curl` desde esta sesión produce una tasa de falsos negativos del 100 %
sobre GitHub.** La verificación válida es WebFetch sobre la página del repo. Queda anotado por tercera vez porque
es el error que más barato sale cometer y más caro sale publicar.

### ⚠️ Advertencia 2 — el badge de licencia no alcanza, y acá cambió dos conclusiones

Relacionado con lo anterior pero distinto: en `SDV` el README dice *«publicly available under the Business Source
License»* y el proyecto se presenta con origen en el **MIT Data to AI Lab**, lo que invita a leerlo como permisivo.
**No lo es.** En `diffprivlib` pasa lo contrario: GitHub no muestra licencia en el sidebar y el archivo dice MIT.
**Para cualquier pieza de la que dependa una recomendación, abrir el archivo de licencia.**

### ⚠️ Advertencia 3 — dos dominios bloqueados, y los dos afectan a la metodología, no a los datos

`nature.com` (el paper de `SynEdu-HEDL` en *Scientific Reports*, `s41598-026-44990-8`) y `arxiv.org`
(`2604.04195`, síntesis por cópulas con marginales empíricas) están **bloqueados por el proxy de egreso**. Los
números de los repos salen de GitHub y están verificados; **la metodología publicada detrás de esos dos
artefactos, no**. Importa poco para la recomendación —ninguno de los dos se propone como dependencia— y se declara
igual.

### Lo que este pase NO hizo, declarado como tal

- **No se agregó ningún agente a `agents/top.md`.** El conteo sigue en **31** y se verificó que la tabla no cambió.
  Lo encontrado son librerías, no agentes.
- **No se buscó jurisprudencia ni sanciones aplicadas.** Se registró qué exige cada régimen y desde cuándo, no cómo
  se está aplicando. Para una propuesta real eso hay que mirarlo.
- **No se evaluó el costo de utilidad de DP sobre modelos de knowledge tracing.** Se sabe que DP cuesta exactitud y
  que `diffprivlib` sirve para medirlo; **cuánto cuesta sobre `pyKT` o `pyBKT` nadie lo midió en este pase**, y
  P34 lo dice en su advertencia en vez de prometer números.
- **No se revisó la capa de privacidad de los LMS ya instalados** (Moodle, Open edX, Canvas). Es el paso siguiente
  obvio: el dato del alumno ya está ahí, no en el agente.

## Nota de método del pase 14 (2026-10-01) — el primer pase que ejecutó la acción que un gap anterior le dejó escrita, y funcionó

Los pases 8 a 13 abrieron una capa nueva cada uno preguntándose qué no se había preguntado todavía. **Este pase no
tuvo que inventar la pregunta: el gap 19 la había dejado escrita en el pase 11**, con la acción textual *«buscar
explícitamente `curriculum ontology`, `achievement standards`, `learning map` y `prerequisite graph` por país, en el
idioma del país, en vez de esperar que aparezcan buscando agentes»*.

**Se ejecutó literalmente, y el rendimiento fue el más alto por búsqueda de los catorce pases:** cuatro de cinco
candidatas confirmadas, más un estándar de interoperabilidad con cuatro implementaciones que nadie había visto, más
una corrección de encuadre que afecta a cómo se leyeron cuatro pases anteriores. **La lección de método es que un gap
bien escrito es más productivo que una pregunta nueva**, y conviene que los próximos pases revisen la lista de gaps
antes de buscar un ángulo inédito: los gaps **20** (medir las *skills* educativas con los benchmarks que esta KB ya
tiene), **23** y **24** están escritos con el mismo nivel de detalle y siguen abiertos.

### Lo que este pase buscó por canal y no por rol, y por eso encontró la capa de voz

El segundo hallazgo (capa de habla y lectura oral, tendencia 34) salió de una pregunta distinta y vale registrarla:
**no «qué hace el software» ni «quién es el alumno», sino «por qué canal entra y sale el trabajo del alumno».**
Trece pasadas asumieron texto. Preguntado por el canal, aparece que la habilidad más evaluada en los primeros años
de escolaridad del mundo —leer en voz alta, medida en palabras por minuto y exactitud— **no tenía una sola pieza en
esta KB.**

### ⚠️ Advertencia 1 — una fecha correcta puede sostener una conclusión falsa, y pasó con Taiwán

El pase 13 escribió que *«la conformidad exigible hoy está en Asia»* y recomendó construir el expediente en un
despliegue **«coreano o taiwanés»**, listando Taiwán con la fecha **2026-01-14**. **La fecha es correcta: la ley se
promulgó ese día.** La conclusión no, porque la ley **no tiene sanciones y no define «alto riesgo»** — delega la
clasificación al MODA y ese marco todavía no existe.

**La trampa es específica y va a volver a pasar:** en seguimiento regulatorio, *promulgada* no es *exigible*, y una
fecha de promulgación verificada le da a una afirmación una solidez que el contenido de la ley no respalda. **Regla
para los próximos pases: junto a cada fecha regulatoria hay que registrar (a) si hay régimen sancionatorio y (b) si
las definiciones operativas están publicadas o delegadas.** Con esos dos campos, Taiwán se habría registrado bien en
el pase 13. Corregido en la tendencia 11 y en `intel/market.md` → `### APAC`.

### ⚠️ Advertencia 2 — el badge de licencia del repo es la licencia del código, no la del dato

En artefactos de datos las dos licencias son distintas y casi nunca coinciden: `bncc-dados` es **MIT en código y
CC BY 4.0 en datos**; `oak-curriculum-ontology` es **MIT en código y OGL-3.0 en la ontología**. **Leer sólo el badge
hace creer que el dato es MIT.** Las dos combinaciones permiten uso comercial, pero **con atribución**, y eso es una
obligación que viaja al entregable. Es la continuación directa de la trampa que el pase 10 documentó para OER, y
ahora se declara como regla general de la KB (tendencia 35).

### ⚠️ Advertencia 3 — dos dominios bloqueados por el proxy, y los dos afectan a entregables

- **`www.australiancurriculum.edu.au` bloqueado:** existencia, formatos (RDF/XML, JSON, SPARQL) y versión (9.0) del
  MRAC están confirmados por fuentes secundarias coincidentes; **la licencia de reuso no se pudo leer**. No cotizar
  MRAC sin abrir antes los términos de ACARA.
- **`arxiv.org` bloqueado, igual que en el pase 13:** la literatura de ASR infantil —incluido el caso en bambara
  (`arXiv 2606.31508`, 55 horas de lectura de 60 niños con *benchmark* público declarado)— **no se pudo verificar en
  origen** y queda como pista, no como hallazgo. Es la única vía que vimos hacia evaluación de fluidez en lenguas
  africanas, así que conviene que un pase futuro con otro proxy la abra.
- **`curl` contra `github.com` devuelve 403 por el proxy, no 404.** La verificación de los catorce repos de este pase
  se hizo íntegramente vía WebFetch, leyendo estrellas y licencia de la página del repo. **El pase 12 ya dejó escrita
  esta advertencia y sigue vigente: un 403 no es un repo inexistente.**

### Lo que este pase NO hizo, declarado como tal

- **No agregó ninguna fila a la tabla principal de `agents/top.md`.** El conteo de **31** se mantiene y se verificó.
  Las piezas nuevas entran como capas al final del archivo, porque no son agentes: son componentes y datos.
- **No verificó Singapur como ausencia definitiva.** Se buscó y no apareció esquema curricular estructurado y
  publicado abiertamente; eso es «no encontrado», no «no existe».
- **No abrió los términos de uso de ACARA** (dominio bloqueado), así que MRAC queda registrado sin licencia verificada.
- **No midió el efecto pedagógico de ninguna pieza de la capa de voz.** `OpenPronounce` devuelve métricas acústicas
  (PER, WER, prosodia); **que esas métricas mejoren el aprendizaje de lectura es una hipótesis, no un dato de este
  pase.** El gap 20 y los benchmarks del pase 4 siguen siendo el camino para medirlo.
- **No replicó el pipeline de `bncc-dados` para ningún otro país de LATAM.** Se verificó que ninguno lo tiene; que sea
  replicable es una lectura razonada del pipeline publicado, no una prueba de ejecución.

## Nota de método del pase 13 (2026-10-01) — trece pasadas buscando por el rol del software, y la pregunta que faltaba era dónde trabaja el alumno

El pase 7 dejó escrita una regla: *«cuando un gap sobrevive varias pasadas, revisar si la pieza que falta existe con otro
nombre»*. Este pase la aplica al gap que más había sobrevivido —el **6**, once pasadas sin cambios— y encuentra que la
pieza no sólo existía: **era el repo con más estrellas de toda la KB.**

**Qué cambió en la consulta, y es replicable.** Las doce pasadas anteriores buscaron por **el rol del software**:
«tutor», «agente educativo», «LMS», «grading», «early warning», «skills pedagógicas». Este pase buscó por **el artefacto
material del alumno**: dónde escribe, qué entrega, dónde se ejecuta. Esa consulta devuelve Jupyter, que no se presenta
como producto educativo y por eso nunca apareció. **Es la quinta vez que esta KB registra que la consulta equivocada
costó pasadas** (pases 4, 5, 6, 7 y 13).

**La regla que agrega este pase, para la pasada 14 y las siguientes:** buscar al menos una vez por **el objeto físico o
digital que el alumno produce** —el cuaderno, el entregable, el examen, el portfolio, el instrumento de medición— y no
sólo por el rol del software que lo rodea. Las dos veces que esta KB lo hizo encontró capas enteras: el **contenido**
(pase 10, «de qué lee el tutor») y la **práctica** (este pase, «dónde trabaja el alumno»).

### ⚠️ Advertencia 1 — una fuente secundaria hizo regresar la fecha del EU AI Act, y hay que no copiarla

Una guía comercial sobre el AI Act en educación, consultada en este pase, afirma que la fecha de aplicación general fue
el **2026-08-02**. **El trend 25 de esta KB documenta, con fuentes primarias, que el Digital Omnibus on AI entró en vigor
el 2026-07-27 y corrió el Anexo III —que es el que cubre educación— al 2027-12-02.** La discrepancia se registra
explícitamente: **la fecha operativa sigue siendo 2027-12-02**, y una pasada futura que cite esa clase de guía sin
contrastarla va a hacer regresar el dato más importante del archivo.

### ⚠️ Advertencia 2 — el hallazgo del pase es grande y conviene no sobrevenderlo

La pila Jupyter es real, permisiva y está desplegada, pero **corrige una mitad del gap 6, no el gap entero**. Lo que
corrige: corrección de trabajo **ejecutable**. Lo que **no** corrige: prosa (sigue propietario), evaluación
**pedagógica** (gap 1, intacto), modelado del alumno (gap 5, intacto) y formación profesional (gap 10, intacto). Y
`nbgrader` está **fuertemente acoplado a JupyterHub**: fuera de ahí el flujo de entrega se complica, y la pieza correcta
pasa a ser `otter-grader`. Un entregable que presente «resolvimos el grading con open source» sin esas cuatro
limitaciones va a fallar en la primera facultad de humanidades.

### Lo que este pase NO hizo, declarado como tal

- **No revalidó las 179 URLs de GitHub preexistentes de esta KB.** Se verificaron de primera mano, vía WebFetch, **las
  7 nuevas** (los 5 de la pila Jupyter, `pedagogy-benchmark` y `Shiksha-Copilot`) más la organización `AI-for-Education`.
  La advertencia del pase 12 sigue vigente: **`curl` a github.com devuelve 403 en este entorno por el proxy, no por *link
  rot***, y la verificación de primera mano se hace con WebFetch.
- **No abrió el paper de `pedagogy-benchmark`** (arXiv 2506.18710): `arxiv.org` sigue bloqueado. Licencia, conteos,
  composición CDPK/SEND y la atribución al Ministerio de Educación de Chile **sí** están leídos de la página del repo.
- **No abrió el estudio de UNESCO IESALC**: `www.iesalc.unesco.org` está bloqueado por el proxy. Las cifras del trend 32
  (87% / 74% / 57% / 26%, 200 instituciones, 19 países, 2026-09-09) vienen de **resultados de búsqueda concordantes**,
  no del documento. Están marcadas como tales en `intel/market.md`.
- **No verificó de primera mano el despliegue de 1.043 docentes de Shiksha Copilot** — viene de la literatura
  secundaria y del sitio del proyecto, no de un documento del Gobierno de Karnataka. Lo que **sí** está verificado en la
  página del repo es licencia MIT, 9 ★, 12 forks, 149 commits y la advertencia de no-producción.
- **No buscó la capa de práctica para materias no ejecutables más allá de confirmar que no existe** (gap 21). Queda
  explícitamente para la pasada 14.

## Nota de método del pase 12 (2026-10-01) — doce pasadas comparando la educación consigo misma, y dos advertencias de verificación que van a volver a pasar

**El cambio de método del pase.** Las once pasadas anteriores compararon artefactos educativos **entre sí**: de ahí
salieron todos los "techos" de esta KB (el techo de la capa predictiva, el de accesibilidad permisiva, el de los MCP de
mastery). Este pase cambió el denominador y comparó **la vertical educativa contra otra vertical en el mismo canal de
distribución**. Es lo que produjo la tendencia 28, y no se podía ver desde adentro de la vertical.

**Qué se verificó de primera mano.** Los **diez repos nuevos** de este pase (los siete paquetes pedagógicos, los dos
baseline de otras verticales y `anki-mcp-server`), más Anki y DeepTutor: licencia, estrellas, lenguaje y descripción
leídos vía **WebFetch contra la página del repo** el 2026-10-01. La licencia de Anki se verificó **en el archivo
`LICENSE`**, no en el README —**AGPL-3.0-or-later**, con porciones de contribuyentes bajo BSD-3—, siguiendo la regla
que el pase 10 dejó escrita.

### ⚠️ Advertencia 1 — los agregadores de estrellas de terceros están mal, no viejos

| Repo | Agregador de terceros | Página del repo (mismo día) | Error |
|---|---|---|---|
| `K-Dense-AI/scientific-agent-skills` | 26.500 ★ (ossinsight) | **47.200 ★** | **−44%** |
| `virgiliojr94/book-to-skill` | 13.700 ★ (sourcepulse) | **33.200 ★** | **−59%** |

En una categoría que suma **+6.300 ★/mes**, el dato del agregador no es una cifra vieja: es una cifra equivocada, y por
un factor cercano a 2. **Regla: en esta capa sólo vale la página del repo.** Esto concuerda con la corrección que
`rotation.json` ya registraba sobre ciclos anteriores de esta KB ("star counts were pipeline-inflated"): el problema
nunca fue el sentido del error, fue confiar en una fuente intermedia.

### ⚠️ Advertencia 2 — un 403 de `curl` no es un 404, y acá son 164

Se pasaron **las 164 URLs de GitHub de toda esta KB** por `curl -sL` para auditar enlaces muertos. **Las 164 devolvieron
403**, uniformemente — incluidas las de repos que el mismo día se verificaron vivos vía WebFetch (`HKUDS/DeepTutor`,
`moodle/moodle`, `instructure/canvas-lms`). Es **el proxy del entorno bloqueando `curl` hacia github.com**, no *link
rot*.

Dos consecuencias que hay que dejar escritas:

1. **Esas 164 URLs quedan sin revalidar en este pase.** No hay evidencia de que estén caídas **ni de que estén vivas**.
   La auditoría masiva de enlaces de esta KB sigue pendiente.
2. **Un pase futuro que vea 403 masivos no debe interpretarlos como enlaces muertos** ni borrar filas por eso. La
   verificación de primera mano en este entorno se hace con **WebFetch**, que sí resuelve github.com. Es la misma
   restricción que el pase 5 registró sobre el proxy de egreso, ahora medida.

### Lo que este pase NO hizo, declarado como tal

- **No revalidó el inventario histórico de la KB** (ver advertencia 2).
- **No encontró nada nuevo en el barrido regulatorio de North America, EMEA ni LATAM.** Las cuatro consultas regionales
  se corrieron y devolvieron lo que la KB ya tenía registrado. El único hallazgo regulatorio nuevo de las cuatro
  regiones es **la oficialización del libro de texto digital en Japón** (ver `intel/market.md`, `### APAC`). Esto se
  registra como **saturación de la capa regulatoria para esta cadencia**, no como cobertura: doce pasadas en dos días
  sobre las mismas cuatro consultas devuelven lo mismo. **Recomendación: bajar el barrido regulatorio a frecuencia
  semanal** y gastar las corridas en capas sin cubrir.
- **No se midió el tamaño de la capa de skills con una consulta de GitHub Search.** La página `github.com/topics/agent-skills`
  declara **28.111 repos** con ese topic, pero la cifra viene de la misma página cuyos conteos de estrellas resultaron
  inflados, así que **se registra como no verificada y no se usa para ninguna conclusión**. Las conclusiones del pase
  descansan sólo en los repos leídos uno por uno.
- **`github.com/topics/claude-skill` devuelve 404** — ese topic no existe; el canónico es `agent-skills`.

## Nota de método del pase 11 (2026-10-01) — once pasadas preguntando qué hace el software, y la pregunta que faltaba era qué decide

**El cambio de pregunta.** El pase 10 cambió el indicador (de estrellas a despliegue real). Este pase cambia el
**sujeto**: las diez pasadas anteriores preguntaron qué hace el software *con* el alumno —le enseña, lo mide, lo
acredita, lo hace accesible—. Ninguna preguntó qué software **decide sobre** el alumno. Esa es la capa de riesgo de
abandono y *student success*, es la que la institución ya tiene presupuestada, es la que el Anexo III del EU AI Act
nombra literalmente, y está vacía. Ver el gap 18 y las tendencias 25 y 26.

**El error propio que este pase encontró, y es más importante que el hallazgo.** La KB filtraba por **MIT /
Apache-2.0 / BSD**. Ese filtro descartó durante diez pasadas el stack completo de Apereo —**Sakai, 1.234 ★, push de
ayer**— porque su licencia es **ECL-2.0**, que es permisiva, aprobada por OSI y FSF, y no estaba en la lista.
**Un filtro por lista blanca de nombres produce falsos negativos que no dejan rastro:** lo que no apareció no se
puede auditar. La regla corregida está en `repos/foundations.md` y la generalización en la tendencia 27.

**Canales de verificación de este pase, en orden de confianza:**

1. **Metadatos de repo** (estrellas, licencia SPDX, `archived`, último push, forks, fecha de creación) leídos vía la **API de búsqueda de GitHub**. Es la fuente de todas las cifras de repos de este pase. ⚠️ `curl` directo a `api.github.com/repos/...` está **restringido al repositorio de la sesión**, así que no se usó para nada: eso también significa que **no se pudo leer el archivo `LICENSE` por API** en repos de terceros.
2. **Página del repo abierta y leída** para licencia exacta, README, conteo de commits y advertencias del autor. Así se confirmaron ECL-2.0 en Sakai, Opencast, OpenLRW y LearningAnalyticsProcessor, el *proof-of-concept only* de `aira`, y los datos sintéticos de `Student-Retention-Prediction`.
3. **Consultas cuantitativas con sintaxis registrada**, para que valgan como serie y no como anécdota: `topic:learning-analytics stars:>50` y `dropout prediction student license:mit pushed:>2026-01-01`. La próxima pasada debería repetirlas tal cual.
4. **Fuentes secundarias múltiples y coincidentes**, para lo regulatorio y de mercado. Marcado 🔴 cuando es el único canal disponible.

**🔴 Bloqueado por el proxy de egreso en este pase** — todo lo que dependa de estas fuentes está marcado como no
verificado de primera mano: `eur-lex.europa.eu` y `digital-strategy.ec.europa.eu` (texto del Reglamento (UE)
2026/1744), `archive.ics.uci.edu` (licencia exacta del dataset UCI 697), `analyse.kmi.open.ac.uk` (ficha de OULAD),
`arxiv.org` (benchmark de supervivencia 2604.08870), `zenodo.org`, `en.wikipedia.org`.

**Lo que este pase afirma con menos fuerza de la que parecería, a propósito:**

- **La licencia del dataset UCI 697** se registra como "CC BY 4.0 ⚠️ confirmar". El tamaño, las features y la procedencia están verificados contra el descriptor publicado; la licencia, no. **Es la clase de dato que el pase 10 aprendió a no dar por bueno** (ver la tendencia 22).
- **Las fechas del Reglamento (UE) 2026/1744** son consistentes en todas las fuentes secundarias consultadas, con número de reglamento, fechas de votación y fechas de aplicación coincidentes. Aun así: **confirmar en EUR-Lex antes de ponerlas en un documento de cliente.**
- **El benchmark de supervivencia** se registra con su conclusión (señal temporal y conductual, no demográfica) porque es exactamente el argumento que un DPO necesita, y **con la advertencia de que su repositorio está reportado como link roto**: no hay código que auditar.

**Lo que no se buscó y se declara como tal:** los esquemas curriculares nacionales (gap 19). Este pase encontró el
coreano **de casualidad**, igual que el pase 3 encontró el español. Dos hallazgos accidentales del mismo tipo de
artefacto en dos regiones son suficiente evidencia para buscarlo a propósito, y no se hizo en esta corrida.

## Nota de método del pase 10 (2026-10-01) — diez pasadas preguntando qué hace el agente, y la pregunta que faltaba era de qué lee

**Lo que este pase hizo distinto.** Las nueve anteriores buscaron por **capa técnica** (agente, modelado, evaluación,
telemetría, datos), por **categoría de producto** (tutor, plataforma, benchmark), por **población de alumnos** (pase 8) y por
**el final del recorrido** (pase 9, la credencial). Ninguna buscó **la entrada**: el material que el agente enseña. La palabra
**«OER»** no aparecía ni una vez en 549 KB de KB.

Es la **quinta** aplicación de la regla del pase 6 —*cuando un gap sobrevive varias pasadas, revisar si la pieza que falta
tiene un nombre que uno no está usando*— y el nombre era **Open Educational Resources**. Sigue siendo la regla más productiva
de esta KB.

**Y este pase agrega una regla propia, que es el otro hallazgo:** *cuando una capa parece vacía, revisar si el indicador con
el que se la está midiendo sirve para esa capa.* Ordenando por estrellas, **Sunbird —la plataforma que sostiene la educación
escolar de India, 180 M+ alumnos, MIT— tiene 41 estrellas y era invisible.** Tiene **317 forks y 38.046 commits**. En
infraestructura pública el **fork es la unidad de despliegue**, no una señal de interés. Ver el **trend 23**.

**Verificado de primera mano** (WebFetch contra la página del repo, y contra el archivo `LICENSE` donde la afirmación es de
licencia): los tres bundles de contenido de OpenStax (`osbooks-calculus-bundle`, `osbooks-biology-bundle`,
`osbooks-college-physics-bundle`, **CC BY-NC-SA en los tres**), el README de `CAHLR/OATutor` y el de
`pythpythpython/openstax-mcp-server` (**CC BY 4.0 en los dos**), `moarshy/mcp-tutor` (sin licencia), los repos de Sunbird
(`SunbirdEd-portal`, `SunbirdEd-mobile-app`, `SunbirdEd-consumption-ngcomponents`, `sunbird-client-services`,
`SunbirdEd-forms`, `sunbird-devops`, `sunbird-telemetry-sdk`, `sunbird-lms-mw`), los dos de Ed-Fi (`Ed-Fi-ODS`,
`Ed-Fi-Data-Standard`, **Apache-2.0**), y la capa de contenido (`DSpace` BSD-3-Clause, `pressbooks` GPL-3.0+,
`ManifoldScholar/manifold` GPL-3.0, `openstax/openstax-cms` **AGPL-3.0**, y el tooling MIT de LibreTexts: `shapeshift`,
`conductor`, `davis`, `LibreOne`).

**Lo que NO está verificado, y está marcado donde aparece:**

1. **La licencia que declara el editor del contenido.** `openstax.org`, `openscied.org` y `support.thenational.academy` están
   **bloqueados por el proxy**. Es la mitad que falta de la contradicción del trend 22, y por eso **la contradicción se
   registra sin resolver**. Ver el **gap 17**.
2. **Las cifras de DIKSHA** (180 M+ alumnos, 290.000+ contenidos, 36 idiomas, 4.950 M+ sesiones) vienen de EkStep y DPI
   Global, fuentes secundarias. Lo verificado es el repo.
3. **La licencia de Oak National Academy** (OGL v3.0 con uso comercial permitido) viene de prensa educativa británica, no del
   documento de licencia. Lo mismo la posible **restricción geográfica al Reino Unido**.
4. **Las cifras de mercado** de este pase (41,7% del crecimiento global en NA, USD 169 M, programa de OpenAI con 8 socios
   nacionales, £200 M+ del Reino Unido, 38%/94% de EMEA) salen de resultados de búsqueda, no de los informes originales.
5. `curl -sI` contra `github.com` **sigue devolviendo 403**, y `api.github.com` también **403** — probado otra vez en este
   pase, igual que en los pases 5 a 9. No hubo forma de confirmar fechas de último commit; se registran **conteos de commits
   y de forks**, que sí aparecen en la página.

**La lección de método que deja la contradicción de licencia, y extiende la del pase 9.** El pase 9 dejó escrito que
*«descripción, banner, README y archivo `LICENSE` son cuatro fuentes distintas con cuatro grados de autoridad distintos»*.
Este pase lo confirma con un caso donde la diferencia **cambia la viabilidad comercial del proyecto**: el README dice CC BY
4.0 y el `LICENSE` dice CC BY-NC-SA, sobre el mismo contenido. **La regla se endurece: para contenido, el README no es
fuente.** Y en este caso ni el `LICENSE` del repo alcanza, porque la licencia real está declarada **por ítem** dentro de cada
JSON — que es lo que hace del manifiesto por ítem un entregable y no una formalidad (**P22**).

**Una tentación que se evitó, y vale registrarla.** Con tres bundles de OpenStax diciendo NC-SA, lo cómodo era escribir
«OpenStax es NonCommercial y la industria lo viene citando mal». Eso es **una interpretación**: tres títulos no son el
catálogo, y el catálogo no se pudo abrir. Lo que se afirma es lo que se leyó —**tres de tres bundles revisados dicen
NC-SA**— y lo que falta se declara como gap.

**Gap regional declarado, también de método.** La búsqueda regional genérica de APAC devolvió **AI empresarial, no
educativa** (gobernanza de directorios, soberanía de infraestructura). **APAC no tiene cifra de mercado educativo propia en
esta ventana.** Lo que sí tiene —India con mandato nacional, Singapur con integración controlada en el Student Learning
Space, Japón en espera evaluativa, China sumándose a la alfabetización obligatoria— apareció buscando **por país**. La regla
del pase 6 aplicada a la geografía: *si la región no devuelve nada, el nombre que falta puede ser el de un país.*

## Nota de método del pase 9 (2026-10-01) — nueve pasadas buscando el principio del recorrido, y la capa que faltaba era el final

**Lo que este pase hizo distinto.** Las ocho pasadas anteriores buscaron por **capa técnica** (agente, modelado,
evaluación, telemetría, datos), por **categoría de producto** (tutor, plataforma, benchmark) y, en el pase 8, por
**población de alumnos**. Ninguna buscó por **el final del recorrido**: qué pasa cuando el aprendizaje termina y hay que
acreditarlo ante un tercero. Esa capa existe desde hace más de una década, tiene estándares con certificación de
conformidad, y no estaba en la KB porque **no se llama «agente» ni «tutor»** — se llama Open Badges 3.0, W3C Verifiable
Credentials, QTI, OneRoster y Caliper.

Es la **cuarta** aplicación de la regla que dejó escrita el pase 6: *cuando un gap sobrevive varias pasadas, revisar si la
pieza que falta tiene un nombre que uno no está usando.* La regla sigue siendo la más productiva de esta KB.

**Verificado de primera mano** (WebFetch contra la página del repo en github.com, y en dos casos contra el archivo):
las ocho piezas vivas de la capa (`learner-credential-wallet`, `verifier-plus`, `issuer-coordinator`,
`qti3-item-player`, `esco-skill-extractor`, `LongsightGroup/oneroster`, `lti-1-3-php-library`,
`openbadges-specification`), las cuatro copyleft/archivadas (`tao-core`, `openbadgeslib`, `caliper-php-public`, los dos
de la Comisión Europea), el **archivo `LICENSE`** de `qti3-item-player` (`Copyright (c) 2022-2024 Amp-up.io, LLC`), el
**banner y la descripción** del fork de la Universidad de Michigan, y las **tres URL que devuelven 404**
(`concentricsky/badgr-server`, `1EdTech/caliper-php`, `IMSGlobal/caliper-python`), más la búsqueda de repositorios de la
organización `concentricsky` por el término `badgr`, que devuelve *«No repositories matched your search»*.

**Lo que NO está verificado, y está marcado en rojo donde aparece:**

1. **Todo el trend 21** (IgniteAI, niveles de Canvas, fechas de fin del acceso gratuito). Los tres sitios con el detalle
   —`constellationr.com`, `nasdaq.com`, `aijourn.com`— están **bloqueados por el proxy**. Es el dato más accionable del
   pase y el peor verificado.
2. **El estado actual del stack europeo de credenciales**: `code.europa.eu` está bloqueado (gap 14).
3. **`moodle.org`** está bloqueado, así que el plugin `enrol_oneroster` de Moodle se menciona sólo como contexto de que
   la integración OneRoster existe en el LMS, sin verificar licencia ni versión.
4. `curl -sI` contra `github.com` **sigue devolviendo 403** y `api.github.com` también **403**, igual que en los pases
   5 a 8. No hubo forma de confirmar fechas de último commit; se registran los **conteos de commits**, que sí aparecen
   en la página.

**La honestidad que exige un 404.** Un repo que devuelve 404 en GitHub puede estar borrado, renombrado o puesto en
privado, y desde afuera son indistinguibles. Este pase afirma únicamente que **las URL no resuelven** — y donde hay más,
lo cita: en `caliper-php` el mantenedor de un fork **nombra la causa**, y en `badgr-server` hay una **segunda señal
independiente**. La tentación era escribir «1EdTech y Instructure retiraron su código open source»; eso es una
interpretación, y sólo una de las dos mitades tiene a alguien que la respalde por escrito.

**Una corrección de proceso que vale registrar.** La primera lectura de la página del fork de Michigan devolvió la
afirmación sobre 1EdTech, pero una segunda lectura **dirigida al `README.md`** no la encontró. En vez de escribirla como
verificada o descartarla, se hizo una tercera consulta dirigida a la **descripción «About» y al banner** del repo, que es
donde efectivamente está, y recién entonces se citó textual. **El nivel de la página en que vive una afirmación importa:**
descripción, banner, README y archivo `LICENSE` son cuatro fuentes distintas con cuatro grados de autoridad distintos.


## Nota de método del pase 8 (2026-10-01) — una población entera que siete pasadas no buscaron, y una sigla que colisiona

**Lo que se hizo distinto.** Los pases 1–7 buscaron por **capa técnica** (agente, modelado, evaluación, seguridad, telemetría, datos) y por **palabra de mercado** (la lección del pase 7: `tutor`, no `agent`). Este pase buscó por **población de alumnos**, y apareció un segmento completo — accesibilidad y educación especial — que **ninguna de las dos estrategias anteriores podía encontrar**, porque sus repos no se describen como «tutor» ni como «agente educativo» y la pieza con más tracción (`accessibility-agents`, MIT, 419 ★) **ni siquiera es educativa**.

**La lección de método, que es la tercera de esta serie:** pase 5 — buscar la pieza técnica, no la categoría; pase 7 — buscar la palabra del mercado, no la del paper; **pase 8 — buscar por quién es el alumno, no por qué hace el software.** Las tres veces el hueco no estaba en el mercado: estaba en la consulta.

**La colisión de siglas, anotada para que no se repita.** El topic `aac` de GitHub tiene 600+ repos y casi todos son de **Advanced Audio Coding** — codecs, demuxers, servidores de streaming. *Augmentative and Alternative Communication* queda enterrado bajo el ranking por estrellas. Los topics que sí sirven son `assistive-technology`, `special-education` e `inclusive-education`.

**Qué está verificado de primera mano en este pase.** Los **doce repos** de la capa nueva se abrieron con WebFetch contra su página de GitHub: licencia, stars, commits, lenguaje y descripción leídos ahí. `uisight` (128 ★) y `a11y-agents-kit` (34 ★) entraron por listado de búsqueda y se abrieron después para cerrar la licencia: **las dos son MIT**, así que **las tres piezas de P17 son permisivas** y no queda ninguna licencia abierta en la capa de conformidad.

**Qué no está verificado, y es la parte que más pesa comercialmente.** La **API de GitHub sigue bloqueada** en esta sesión (`api.github.com` responde que el repo no está habilitado para la sesión; `curl -sI` contra github.com devuelve 403), así que no hubo forma de confirmar fechas de último commit — se registran los conteos de commits, que sí aparecen en la página. Y **todo lo regulatorio de este pase viene de resultados de búsqueda**: la fecha de entrada en vigor del **EAA (2025-06-28)**, el nivel **WCAG 2.1 AA**, y las prohibiciones de IEP de **Delaware** y **Nueva York**. Son las tres afirmaciones sobre las que se apoyan `P17`, `P18` y el `gap 12`, así que **hay que abrir el texto normativo antes de usarlas con un cliente.**

**Una corrección de licencia detectada leyendo, no buscando.** `Teacher-Hub` declara *«MIT License — free for educational and non-commercial use»*. Las dos mitades se contradicen. Es la segunda declaración de licencia internamente inconsistente que encuentra esta KB (la primera fue OpenTutorAI-CE). **Leer la frase completa de licencia, no sólo el nombre del badge.**

## Nota de método del pase 7 (2026-10-01) — la consulta equivocada costó seis pasadas, y la licencia del dataset no se había mirado nunca

**Dos errores de método propios, los dos corregidos en este pase, y los dos vale dejarlos escritos porque se repiten.**

**1. Se buscó la palabra del gremio, no la del mercado.** Las seis pasadas anteriores buscaron `agent`, `tutoring system`, `benchmark` y `MCP`. Nunca `tutor`. Buscando por descripción con esa palabra aparecen tres repos que suman **4.3k estrellas** y que la KB no tenía: `llamatutor` (2.1k), `ChatTutor` (1.3k) y `tutor-gpt` (931). Ninguno es nuevo; eran invisibles a la consulta. **Regla:** para cada capa, buscar también con el término que usaría quien compra, no sólo el que usa quien construye.

**2. Se verificó la licencia del código y nunca la de los datos.** Los pases 4–6 afirmaron que el modelado del alumno es "integración de una librería MIT". Cierto sobre `pyKT` y `pyBKT`, e insuficiente: los datasets con que se entrenan son **CC BY-NC** salvo uno. Ver el **gap 11**. **Regla:** para toda pieza que se entrene, verificar la licencia del dataset junto con la del repo.

**Límite técnico de la búsqueda de GitHub que conviene registrar:** `in:name` **no respeta límites de palabra** — `tutor in:name` devuelve 276 resultados dominados por `tutorial`, y un `OR` entre términos degrada la consulta entera (`vocational OR berufsschule OR apprenticeship AI tutor` → 24.481 resultados, casi todos irrelevantes). Lo que funcionó fue buscar por **descripción**.

**Qué está verificado de primera mano en este pase (WebFetch contra la página del repo):** `DeepTutor` (40.582 ★, Apache-2.0, push 2026-09-27), `OpenMAIC` (39.7k ★, MIT, 652 commits, v1.1.2 del 2026-09-28), `tutor-gpt` (GPL-3.0, 931 ★, 356 commits), `ChatTutor` (AGPL-3.0, 1.3k ★), `Honcho` (AGPL-3.0, 7.4k ★, 760 commits), `ABench` (Apache-2.0, 30 ★), `XES3G5M` (MIT, 61 ★), `EdNet` (CC BY-NC 4.0, 385 ★), los perfiles de organización de `plastic-labs` (declara **EE. UU.**) y de `inclusionAI` (declara **Ant Group**), y la **ausencia** de licencia en `llamatutor` (`/blob/main/LICENSE` → **404**).

**Qué NO está verificado y por qué.** El proxy de egreso sigue bloqueando `arxiv.org`, `huggingface.co` y los dominios de OUP — **se reintentaron los tres en este pase**. Quedan con cifras de resultados de búsqueda, no de fuente primaria: **`FoundationalASSIST`** (arXiv 2602.00070), **`EduZone`** (2608.02024), **`AIriskEval-edu`** (2607.01934), el paper de **`ProHist-Bench`** (2604.24690) y **`L2-Bench`**. También está bloqueado `aivet-training.eu`, por lo que AIVET queda como pista, no como hallazgo.

**Sobre `L2-Bench`, que arrastra la marca 🔴 desde el pase 6:** este pase obtuvo **más detalle** de resultados de búsqueda — taxonomía de 12 competencias y 31 subcompetencias validada por **200+ practicantes expertos** con puntajes de autenticidad de tarea **4,42/5,00** y adecuación de criterios **4,18/5,00**, y resultados por modelo (el mejor frontier model en **85,5%**, cayendo a **69,9–73,4%** en tareas difíciles). **Dos pasadas independientes que coinciden en las cifras es evidencia circunstancial, no verificación.** La marca 🔴 **se mantiene**: el artefacto sigue sin abrirse. No usar esas cifras en un entregable sin leer la fuente.

**Nota sobre la API de GitHub:** `get_file_contents` vía MCP está restringido a los repos de esta sesión, así que no sirve para leer el LICENSE de un tercero (se intentó con `Nutlope/llamatutor` y fue denegado). La verificación de licencias se hizo con WebFetch. `curl -sI` contra github.com sigue devolviendo **403** a través del proxy, como en los pases 4–6.

## Nota de método del pase 6 (2026-10-01) — qué se verificó, qué no, y una capa que faltaba en el mapa

**Verificado de primera mano** (leyendo el repo en GitHub: licencia, stars, commits, y en varios casos el texto del README): los cinco artefactos de la capa LRS/xAPI, ERPNext, y la recuenta de `EduBench`. Los conteos de repos que sostienen los gaps 2 y 10 (20 repos en español, ninguno >1 ★; 24 repos de FP, techo 2 ★) salen de consultas directas a la API de búsqueda de GitHub, no de listicles.

**No verificado, y marcado en rojo donde aparece:** **L2-Bench**. El proxy de egreso de esta sesión bloquea `arxiv.org`, `huggingface.co` y `oup.com`, que son exactamente los tres lugares donde vive. Se registró igual, con la advertencia pegada a cada mención, porque cerraba un sub-gap declarado hacía dos pasadas; pero **no debe entrar en un entregable sin abrirlo antes**. El pase 5 ya había dejado escrito que "el proxy de egreso decide qué se puede afirmar"; este pase lo confirma y agrega un matiz: **también decide qué se puede cerrar**. Un gap que se cierra con una fuente no verificable no está cerrado, está anotado.

**Lo que este pase aprendió sobre buscar, y es la parte reutilizable.** Los pases 3 y 5 concluyeron que un gap terco hay que re-buscarlo con la consulta invertida (por licencia y stack, no por categoría). El pase 6 encontró el caso complementario: **la consulta estaba bien y el mapa estaba mal.** La capa de Learning Record Store existe desde hace más de una década, es un estándar IEEE, tiene cuatro implementaciones maduras y una de ellas con 583 ★ — y no apareció en cinco pasadas porque la KB buscaba "agente", "tutor", "benchmark" y "plataforma", y esto no se llama así.

La regla que queda: **cuando un gap sobrevive varias pasadas, revisar si la pieza que falta tiene un nombre que uno no está usando.** Buscar mejor no alcanza si el mapa no tiene el casillero.

## Nota de método del pase 5 (2026-09-30) — el proxy de egreso decide qué se puede afirmar

Esto no es color: cambia qué de este archivo se puede citar en material de cliente.

**Lo que funcionó.** WebFetch contra `github.com`. Todo lo que este pase afirma sobre repos —licencia, stars, lenguaje, commits— se leyó de la página del repo o del archivo LICENSE.

**Lo que no funcionó.** `curl -sI` contra github.com devuelve **403** a través del proxy (confirma lo que ya anotó el pase 4: **no sirve para verificar URLs en este entorno**). Y están **bloqueados por el proxy de egreso**: `arxiv.org`, `openreview.net`, `aclanthology.org`, `huggingface.co`, `ojs.aaai.org`, `mcml.ai`, `unu.edu`, `coe.int`, `digitaleducationcouncil.com`, `mcpservers.org`.

**La consecuencia, dicha sin adornos.** Todo lo que en este pase viene de **papers, datasets de HuggingFace, cifras de mercado y documentos de organismos** está tomado de **resúmenes de búsqueda y no pudo verificarse contra la fuente primaria**. Eso incluye: los conteos de ítems de SafeTutors (5.955) y de EduBench (4.000+), los subtipos de EduFrameTrap, **el hallazgo de anti-correlación de ELBench**, el 78,74% de OmniEdu en MathTutorBench, los venues (ACL 2026, EMNLP 2026, AAAI), **todas las cifras de UNESCO IESALC** y las fechas del Consejo de Europa.

Se registran porque son útiles, internamente consistentes y provienen de fuentes independientes que coinciden. **No citarlos en un entregable sin abrir el paper o el informe.** Los tres hallazgos de ELBench y de EduGuardBench que este archivo usa como argumento de arquitectura (trend 12) son justamente los que más conviene confirmar antes de ponerlos en una slide.

**Lo que sí se verificó leyendo el archivo y no el badge**, porque en los dos casos el badge sugería otra cosa: `llmgrader` → **PySilicon Research License** (no MIT), y `awesome-ai-llm4education` → **`/blob/main/LICENSE` devuelve 404**, no tiene licencia. Leer el LICENSE sigue siendo la única verificación válida.

**Una corrección de premisa propia**, que se registra para que no se repita: este pase buscó una Working Conference del Consejo de Europa de **octubre de 2026** y **no existe** — la última realizada es la 3ª, de **octubre de 2025**. La búsqueda corrigió la suposición; si no se hubiera verificado, habría entrado a la KB un evento inventado.

## Nota de método del pase 4 (2026-09-30) — cómo se verificó y qué no se pudo

**Verificado de primera mano:** los 7 repos nuevos y los 6 ya registrados que se re-chequearon, todos vía **WebFetch contra la página del repo** — stars, licencia, lenguaje y, donde estaba, fecha de último commit.

**Tres limitaciones del entorno que conviene dejar escritas, porque cambian el procedimiento:**

1. **`curl -sI` no verifica nada acá.** El procedimiento estándar de esta KB es chequear cada URL con `curl -sI` antes de escribirla. En esta corrida devuelve **403 para todas las URLs de github.com**, incluidos repos que sabemos vivos. Un 403 uniforme no distingue un repo real de uno inexistente. Se reemplazó por WebFetch, y **se comprobó que ese canal sí discrimina**: una URL deliberadamente inexistente devolvió `HTTP 404 Not Found` mientras las 13 reales devolvieron su página.
2. **`api.github.com` está fuera de alcance** para esta sesión (responde que el repo no está habilitado). Stars y licencia se leen de la página renderizada, no de la API — así que son valores mostrados, redondeados por GitHub en el caso de los repos grandes (40.6k, 39.7k).
3. **`arxiv.org` está bloqueado por el proxy de salida.** Consecuencia concreta: **la afiliación institucional de MathTutorBench no se pudo verificar de primera mano.** Se le asigna EMEA/Suiza por el handle de la organización (`eth-lre`) y por el venue, **no por el paper**. Es la atribución regional menos firme de este pase y hay que tratarla como tal. Lo mismo con `EduFair-Bench` (arXiv 2609.12949): se conoce por la búsqueda, no se le encontró repo, y no se lo registra como hallazgo.

**Atribuciones con confianza declarada, no binaria.** Dos regiones se cerraron en este pase con niveles de evidencia distintos, y se registran distinto: **OpenTutorAI-CE → Marruecos** está *declarado* en el perfil de la organización; **Claw-ED → Nueva York** está *inferido de artefactos* (repos hermanos sobre NYS Regents y Great Neck Public Schools), no declarado. Tres agentes —**Bloom, OpenTutor y tutor-mcp**— se buscaron explícitamente y **no declaran ubicación en ningún lado**: quedan como gap, no como silencio.

## Nota de método — qué está verificado de primera mano y qué no (pase 3, 2026-09-30)

Esta KB ya se quemó una vez con datos que el pipeline reportó sin medir (ver la tabla de corrección en `agents/top.md`). Así que conviene ser explícito sobre el nivel de evidencia de cada cosa, porque **en esta corrida no fue uniforme**.

**Verificado de primera mano (fuerte).** Todo lo que es repo: licencia, stars, forks, commits, fecha del último commit, releases. Se leyó la página del repo vía WebFetch, y en el caso de GegoK12 además el archivo `LICENSE` crudo (`SPDX-License-Identifier: MIT`). Aplica a Claw-ED, AI-Teaching-Agent, GegoK12, `Plugin-Hello-Teacher`, OpenMAIC y DeepTutor.

**Corroborado pero no leído en la fuente (medio).** Todas las afirmaciones **regulatorias y de tamaño de mercado** del pase 3: la AI Basic Act coreana, la ley vietnamita, el deadline de Ohio del 2026-07-01, Virginia SB 394 / HB 1186 y su pilot de USD 2M, los 35+ estados con guía oficial, y las cifras de Europa y MENA. El proxy de egreso de esta sesión **bloquea el acceso directo** a esos dominios (`lw.com`, `multistate.us`, `casrai.org`, `kjk.com`, `edweek.org`, `education.ohio.gov`, `gegok12.com` y otros), y `curl` no sirve como verificador acá — devuelve 000 o 403 incluso para páginas que existen. Cada afirmación de este grupo se sostiene en **múltiples resultados de búsqueda independientes que concuerdan** (el deadline de Ohio aparece en 6+ medios distintos; la fecha coreana del 2026-01-22 y la inclusión de educación como *high-impact*, en 5+), no en la lectura de la página.

**Qué hacer con eso.** Son datos suficientemente sólidos para orientar prioridades y construir propuestas, y **no** suficientes para citarse textualmente en un entregable de cliente sin abrir la fuente primaria. Antes de usar cualquier cifra regulatoria de esta sección en material de cliente: **leer el estatuto o la guía oficial**. Las URLs quedan listadas arriba para eso, pero están sin verificar a nivel HTTP en esta corrida.

**Lo que explícitamente no se pudo verificar y queda marcado como tal:** el conteo de MultiState de "cuatro estados con leyes de 2026 que exigen guía estatal más política distrital obligatoria (Maryland, Idaho, Oklahoma, Virginia)". Ohio y Virginia se corroboraron por separado; el conteo de cuatro queda atribuido a MultiState y sin verificar uno por uno.

---
*Repos (stars, licencias, releases) verificados uno por uno vía WebFetch el 2026-09-30, no por el pipeline. Afirmaciones regulatorias y de mercado del pase 3: corroboradas por múltiples fuentes concordantes, con las fuentes primarias inaccesibles desde esta sesión — ver la nota de método arriba.*

## 87. «No hay README» no es «no hay repo»: cada ecosistema tiene su archivo de metadatos, y pedir el equivocado produce un falso negativo (agregado en el pase 30 del 2026-10-02)

**Tercera regla de método de este pase, y la única que corrige un error cometido dentro del mismo pase.**

Verificando `.LRN`, este pase pidió `README.md` al espejo `openacs/dotlrn` en `main` y en `master`, recibió **404 en las
dos** y escribió que *«el espejo no es una fuente usable»*. **Es falso.** El repositorio tiene contenido y se lee
perfectamente: lo que no tiene es un `README.md`, porque **es un paquete APM de OpenACS y su metadato vive en
`dotlrn.info`** — que responde **200 en `main`, `master`, `HEAD` y `oacs-5-10`**, y que resultó **la mejor fuente de todas**:
declara `version name="2.10.1"`, `<release-date>2024-09-02</release-date>`, `<maturity>2</maturity>` y el vendor.
🔵 **Ese archivo corrigió además a la fuente secundaria, que decía «2.9.0 / 2.9.1».**

> **La regla: antes de declarar un repositorio vacío o un espejo inútil, pedir el archivo que su ecosistema usa.**
> `*.info` en OpenACS/APM, `*.gemspec` en Ruby, `pom.xml` en Java, `composer.json` en PHP, `pyproject.toml`/`setup.py` en
> Python, `package.json` en Node, `Cargo.toml` en Rust. **`README.md` es una convención de GitHub, no un requisito de
> empaquetado**, y los proyectos más viejos —justo los que esta KB evalúa para declararlos vivos o muertos— son los que
> menos probablemente lo tengan.

**Y el corolario, que es el que más valor tiene:** el archivo de empaquetado **es mejor evidencia que el README y que la
web del proyecto**, porque **es el que el gestor de paquetes lee** y por lo tanto el que no puede estar decorativo. En este
pase el mismo principio rindió tres veces por tres canales distintos: `dotlrn.info` para la versión de dotLRN,
`license.txt` para su GPL-2.0, y el `LICENSE` **dentro del tarball de npm** para el 0BSD de `oneroster-ts` que el registro
declaraba ausente (tendencia **86**).

**El registro de canales de verificación de esta KB, consolidado en este pase:**

| Canal | Estado | Para qué sirve |
|---|---|---|
| `raw.githubusercontent.com` | ✅ **Responde** | Leer código y metadatos sin clonar. **El caballo de batalla desde el pase 28** |
| Registros de paquetes (PyPI, npm) | ✅ **Responden** | Licencia **del artefacto**, versiones y fechas reales. **El canal que descubrió el conector de Open edX** |
| Tarball del paquete | ✅ **Responde** | **El `LICENSE` que el registro no declara**, y el código del servidor para ejecutarlo |
| `codeload.github.com` | 🔴 **403** | Bajar el repo entero. **No disponible: hay que leer archivo por archivo** |
| API de GitHub | 🔴 **Cerrada** fuera del alcance de la sesión | — |
| `openacs.org`, `openedx.org` | 🔴 **403** | Documentación y anuncios oficiales. **No disponibles** |

## 88. Cuando dos señales del mismo repo se contradicen, gana la que el runtime ejecuta — no la que el comentario afirma (agregado en el pase 31 del 2026-10-02)

El pase 29 encontró dos documentos contradictorios en `openedx/edx-platform` sobre qué versión del API de *authoring*
usar. El pase 30 convirtió esa contradicción en una consigna que elegía **el lado equivocado**: *«medir los endpoints
`v0`, que son los que el propio repo recomienda»*. Se midieron, y el `v0` **está deprecado en favor del `v1`**.

**La diferencia entre las dos señales no es de antigüedad, es de naturaleza:**

| Señal | Dónde | Qué es |
|---|---|---|
| *«Do not use under v1 yet (Nov. 23). The Authoring API is still experimental and the v0 versions should be used»* | comentario al **final** de `v1/urls.py`, después del `register`, encabezando una sección **vacía** | una **afirmación** de noviembre de 2023 que nadie borró |
| `.. deprecated::` + `_DEPRECATION_MSG` + `warnings.warn(..., DeprecationWarning)` en las 5 operaciones | `v0/views/xblock.py` | **código que se ejecuta** y le avisa al que llama |

**La regla:** un comentario es una opinión fechada; un `DeprecationWarning` emitido es un hecho observable. Cuando hay
que elegir, **se verifica cuál de las dos señales el programa ejecuta** — y si ninguna, se mira cuál está dentro de la
ruta que el router monta. Esta KB se equivocó dos pases seguidos por leer prosa en vez de flujo de control, y le costó
una consigna entera.

**Corolario operativo para el barrido:** cuando un repo dice «experimental», hay que preguntar **¿sigue diciéndolo el
código, o sólo el comentario?** Son dos preguntas distintas y dan respuestas opuestas más seguido de lo que parece.

## 89. La puerta MCP de un estándar no es única: donde hay una, suele haber varias, y la licencia varía entre ellas (agregado en el pase 31 del 2026-10-02)

El pase 28 descubrió que OneRoster **sí** tenía conector —`oneroster-ts`, 0BSD— y la KB lo registró como *«el»*
conector de OneRoster. El pase 31 preguntó al registro de npm por el **nombre del estándar** y encontró **al menos
seis implementaciones**, **dos de ellas sirviendo MCP**:

| Paquete | Licencia | MCP |
|---|---|---|
| `@eduware/oneroster` v1.2.11 | **MIT** | ✅ ejecutable `mcp` empaquetado |
| `@superbuilders/oneroster` v0.7.0 (= `trilogy-group/oneroster-ts`) | 0BSD | ✅ (132 tools medidas en el pase 30) |
| `@longsightgroup/oneroster` v0.3.0 | **MIT** | no |
| `@universis/one-roster` v2.30.2 | — | no |
| `@timeback/oneroster` v0.3.3 | — | no |
| `@eduware`/otros clientes parciales | varias | no |

**Por qué importa y no es trivia:** la KB venía razonando *«OneRoster tiene puerta, y es 0BSD»*. La realidad es
**«OneRoster tiene al menos dos puertas, y una es MIT»**, lo que cambia la conversación de licencia con un cliente que
rechaza 0BSD por desconocimiento o por política de *procurement*. **Una ausencia se cierra con un hallazgo; una
abundancia se administra comparando.** Y la regla de muestreo que la produjo —preguntar por el estándar, abrir el README,
buscar «MCP» adentro— hay que repetirla **después** de encontrar el primero, no sólo antes.

## 90. El mismo estándar obligatorio puede estar mantenido en un lenguaje y abandonado en otro, y eso decide el stack (agregado en el pase 31 del 2026-10-02)

LTI 1.3 Advantage es obligatorio de hecho: toda plataforma educativa grande lo habla. Su implementación de referencia
tiene **dos lados con salud opuesta**:

| Lado | Paquete | Licencia | Última publicación |
|---|---|---|---|
| JavaScript | `ltijs` v7.0.6 | Apache-2.0 | **2026-09-18** (este mes) |
| Python | `pylti1p3` v2.0.0 | MIT | 🔴 **2022-11-20** (casi 4 años) |

**Treinta pases trataron la madurez como propiedad del *estándar*.** Es propiedad del **par estándar × lenguaje**. Un
tool LTI nuevo en Python arranca sobre una dependencia sin releases —y por lo tanto sin parches publicados— desde 2022,
mientras el equivalente JS está vivo. **Eso es un criterio de elección de lenguaje para la capa de integración, y
pertenece a la propuesta**, no al descubrimiento tardío del *security review* del cliente.

**Generalización para el barrido:** cuando esta KB diga «el SDK de X está maduro», tiene que decir **en qué lenguaje**.
La afirmación sin lenguaje es la mitad de una medición.

## 91. El authoring de un agente no se cotiza por curso: el core ya trae propagación, y nadie la estaba usando (agregado en el pase 31 del 2026-10-02)

`v2` del API de contentstore de Open edX expone `downstreams/` con cuatro vistas, incluida
**`downstreams/<usage_key>/sync` → `SyncFromUpstreamView`**: es la reutilización de **Libraries v2**, donde un bloque
vive en una biblioteca (*upstream*) y los cursos que lo consumen (*downstream*) **se sincronizan**.

**La consecuencia es económica, no técnica.** Un agente que mantiene material en 40 cursos tiene dos cotizaciones
posibles:

- **sin la capa:** 40 ediciones por cambio, y el costo crece con el catálogo;
- **con la capa:** una edición + N `sync`, y el costo crece con el **número de cambios**, no de cursos.

Esta KB venía cotizando la primera. ⚠️ **Y el conector MCP oficial no expone esta capa** —no está entre sus 7 rutas
CMS—, así que hoy se alcanza por REST directo: **el agente necesita dos canales** (MCP para operación, REST para
propagación), que es un dato de arquitectura y de esfuerzo (**gap 59**).

## 92. Un régimen con varias fechas no tiene «una» fecha de vigencia, y confundirlas es el error de conformidad más caro que cometió esta KB (agregado en el pase 31 del 2026-10-02)

El **gap 56** nació porque esta base publicó dos fechas incompatibles para el Anexo III del EU AI Act. Resuelto contra
el texto consolidado: **las dos son correctas y gobiernan obligaciones distintas.**

| Fecha | Qué rige | ¿Educación / Anexo III? |
|---|---|---|
| **2026-08-02** | aplicabilidad general: **art. 50** (transparencia), **art. 4** (alfabetización en AI), **art. 5** (prohibiciones), reglas **GPAI**, gobernanza y sanciones (AI Office + autoridades nacionales) | **no** |
| **2027-12-02** | **obligaciones de alto riesgo *autónomo* del Anexo III — el inciso que nombra educación** | **sí** |
| **2028-08-02** | alto riesgo **embebido** en productos regulados (Anexo I) | no |

**Instrumento:** *Digital Omnibus* = **Reglamento (UE) 2026/1744**; aprobación final del Consejo **2026-06-29**, en
vigor **2026-07-27**; diferimiento del Anexo III **16 meses** (del 2026-08-02 al 2027-12-02). **El art. 50 no se
postergó.**

🔴 **El error concreto, y por qué es el más caro:** el pase 28 escribió *«en EMEA el Annex III dejó de ser una fecha:
rige desde el 2026-08-02 y la demanda de conformidad está vencida»*, y **sobre eso se construyó argumentación de
venta**. Un comprador europeo con asesoría legal detecta eso en la primera reunión, y **lo que se pierde no es el
argumento: es la credibilidad de todas las otras cifras de la propuesta**.

**La regla que queda:** toda afirmación de vigencia en esta KB tiene que citar **el artículo o el inciso**, no el
reglamento. «El AI Act rige desde X» es una oración sin valor operativo: el AI Act rige **por tramos**, y educación cae
en el tramo que vence **último**.

🟢 **Y el reencuadre, que además vende mejor porque es verdadero:** hay **dos tiempos**. Obligación **vigente y barata
ahora** —transparencia del art. 50 y alfabetización del art. 4, que conecta con la tendencia 5 y con **P6**— y
**conformidad cara con ~14 meses de pista** (Anexo III, 2027-12-02). Catorce meses es el horizonte de un **programa**,
no de un parche: es una mejor venta que una urgencia falsa.

## 93. Un rail de escritura puede estar bien diseñado contra la operación masiva y abierto a la repetida — y la asimetría no se ve en la documentación (agregado en el pase 31 del 2026-10-02)

El pase 30 citó el modelo de amenaza escrito en el código del conector oficial de Open edX: *«a looping agent… a retry
storm that mass-enrols or deletes»*, y registró los cuatro rails como un acierto de diseño. **Lo son.** Pero midiendo
las 19 escrituras una por una aparece lo que la prosa no dice: **11 exigen *confirm token* y 8 no.**

| Sin confirmación (8) | Con confirmación (11) |
|---|---|
| `create_xblock` (×2), `update_xblock`, `update_course_settings`, `enroll_user`, **`unenroll_user`**, `generate_certificate`, `submit_report` | `bulk_enroll`, `create_user`, `deactivate_user`, `delete_xblock`, `instructor_access`, `invalidate_certificate`, `publish_xblock`, `regenerate_certificates`, `request_retirement`, `reset_attempts`, `set_role` |

**La asimetría es deliberada y está en el decorador `@audited_write`:** la operación *masiva* (`bulk_enroll`) pide
token; la operación *unitaria* equivalente (`unenroll_user`) no. Un agente en bucle **no** puede desmatricular un curso
entero en una llamada, y **sí** puede desmatricular 500 alumnos en 500 llamadas sin un solo token.

**La regla general para evaluar cualquier conector de escritura:** no alcanza con verificar *que* hay rails; hay que
**contar qué fracción de las escrituras los atraviesa**, y mirar específicamente si el rail está puesto en la
**cardinalidad de la llamada** o en el **efecto acumulado sobre el sujeto**. El primero es fácil y el segundo es el que
protege al alumno. Lo que falta se cubre afuera del conector: **cuota por sujeto y por ventana de tiempo** (**P63**).

## 94. El paquete publicado y el repo público son dos verificaciones distintas, y para construir manda la del paquete (agregado en el pase 31 del 2026-10-02)

Este pase intentó cumplir la regla *«verificá cada URL con `curl -sI`»* y descubrió que **el canal obvio no verifica
nada en este entorno**:

| Canal | Resultado | Sirve para verificar |
|---|---|---|
| `github.com/<owner>/<repo>` (HEAD) | **403** para todos, incluido `openedx/edx-platform` | ❌ no |
| `api.github.com/repos/...` | **403** (*«not enabled for this session»*) | ❌ no — **y por eso este pase no publica ni una estrella** |
| `www.npmjs.com/package/...` | **403** | ❌ no |
| `raw.githubusercontent.com/<o>/<r>/HEAD/README.md` | **200** si existe, **404** si no | ✅ **sí — es el test de existencia válido** |
| `registry.npmjs.org/<pkg>` | **200** con licencia, versiones, fechas y README completo | ✅ sí |
| `pypi.org/pypi/<pkg>/json` + `files.pythonhosted.org` | **200**, y el artefacto se baja y se abre | ✅ sí, **y es el canal que mide de verdad** |

🔵 **El hallazgo de método más útil: se puede medir una licencia y una superficie de herramientas sin instalar ni
levantar nada.** El conector oficial de Open edX se midió bajando su wheel de PyPI, abriéndolo como ZIP y leyendo
`dist-info/licenses/LICENSE` (AGPL-3.0, de primera mano) y los decoradores de sus vistas (19 escrituras). **Es el
sucesor del truco del pase 26** (ejecutar el eslabón puro cuando el servidor no se puede levantar): cuando no hay
Docker, **hay artefacto publicado**.

🔴 **Y el hallazgo incómodo, después de corregir el propio instrumento: un paquete real, verificable y con licencia
permisiva declara un repo que no existe públicamente** — `@eduware/oneroster` → `Eduware-Inc/eduware-oneroster`, con **ocho rutas de metadatos probadas y las
ocho en 404**. **No son hallazgos falsos: el paquete es el producto, el repo es una afirmación sobre el paquete.** La regla de
esta KB —*«todo hallazgo con URL de repo real»*— tiene que admitir **la URL del registro** cuando es la que verifica, y
**decir cuál de las dos se comprobó** (**gap 58**).


### 🔴 El subcaso que este pase vivió en carne propia: el test de existencia de un solo archivo no es un test

La primera verificación de este pase usó **sólo** `README.md` y declaró 404 para dos repos. Corriendo el mismo test
sobre `openedx/edx-platform` —cuyo código este pase **ya había leído archivo por archivo**— **también dio 404**, porque
publica `README.rst`. El 404 era del instrumento, no del repo. Re-medido sobre **ocho rutas de metadatos**,
`dmitry-viskov/pylti1.3` **existe** (y esta KB **ya lo tenía con 138 ★**, de modo que el falso negativo contradecía su
propio archivo); sólo `Eduware-Inc/eduware-oneroster` falla **las ocho**.

🔵 **La práctica que queda, y es generalizable a cualquier barrido:** **correr toda verificación de ausencia junto a un
control positivo conocido.** Si el control falla, falló el método. Y cuando una medición nueva contradice un registro
propio de esta KB, **la contradicción se resuelve antes de publicar** — acá el registro viejo tenía razón. Es la misma
lección de la tendencia 87, que este pase **repitió a pesar de tenerla escrita**: una regla registrada no se aplica
sola.
## 95. Medir el árbol versionado de un API no es medir su superficie HTTP, y la coincidencia de tres fuentes no es cobertura de fuentes (agregado en el pase 32 del 2026-10-02)

El pase 31 midió **tres canales independientes** —los cinco árboles `v0`…`v4` de contentstore, y las 19 tools de
escritura del conector oficial— y los tres coincidieron: *«ninguna versión crea el curso»*. **La medición era correcta y
la conclusión era falsa.** Crear un curso en Open edX **sí es una llamada HTTP**: vive en `course_handler` POST
(`cms/djangoapps/contentstore/views/course.py:342` → `_create_or_rerun_course`, **:1184**), que es la vista **legacy** de
Studio, fuera del árbol `/api/contentstore/` versionado.

**La trampa de método, y es la que hay que conservar:** los tres canales **miraban el mismo lado del proyecto**. En un
proyecto con años encima, la escritura suele haber quedado en el handler viejo mientras el REST nuevo se construyó
prolijo y de lectura. **Tres fuentes que comparten un sesgo de origen son una fuente.** Cuando una medición concluye *«no
se puede»*, hay que preguntarle **a la vista legacy y al `urls.py` raíz** antes de publicarlo — y antes de descontar la
funcionalidad de una cotización.

**Corolario que cambia una cotización:** la pieza que *se llama* `course_rerun` (dos de ellas: la vista REST `v1` y el
handler legacy) es **de sólo lectura y pide `GlobalStaff`**; la que escribe **no se llama rerun y pide
`is_content_creator(user, org)`**. **El nombre del endpoint no predice ni su verbo ni su permiso.**

## 96. «xAPI» es el acrónimo más sobrecargado de este dominio, y el filtro de licencia no protege contra la homonimia (agregado en el pase 32 del 2026-10-02)

Buscar `xapi` en los registros de paquetes devuelve **tres dominios distintos con el mismo nombre exacto**: el xAPI
educativo (Experience API / Tin Can), un *marketplace* de APIs de **cripto/Web3** (`xapi-to`, MIT, `modified`
2026-09-29, que además **se anuncia como *«Agent-friendly CLI for xAPI»* e instala un skill de agente**) y el API del
**bróker de forex XTB** (`xapi-python`, MIT). Son las **colisiones 5 y 6** de esta KB.

**Lo que esto le enseña al barrido, y es lo incómodo:** las dos trampas son **MIT, activas y recientes**. El filtro de
licencia —que es el filtro principal de esta base— **no las descarta**, y la peor de las dos **se presenta como
agéntica**, que es justo el criterio de promoción. Un barrido ordenado por nombre + licencia + frescura **las habría
subido a `agents/top.md`**. El único filtro que las atrapó fue **abrir el README y contar menciones del vocabulario del
dominio** (47.905 caracteres, **cero** menciones de *«Experience API»*, *«Tin Can»* o *«learning record»*).

**Regla operativa:** buscar **`"Experience API"`** o **`"Tin Can"`**, nunca `xapi` a secas. Y en general: **un acrónimo de
cuatro letras o menos no es una consulta de búsqueda, es una invitación a la homonimia.**

## 97. El campo `description` de un paquete no sirve ni para afirmar ni para negar una capacidad (agregado en el pase 32 del 2026-10-02)

`coursecode` (**MIT**) **trae un servidor MCP incorporado** y cubre SCORM 1.2, SCORM 2004, cmi5 y LTI 1.3. **Su
descripción en npm no menciona MCP en ninguna parte.** El barrido por campo `description` —el que esta KB venía
corriendo— **lo habría registrado como ausencia medida**, y la ausencia habría sido falsa.

Es el mismo canal, en el sentido inverso, que atrapó las colisiones de la tendencia 96: **el README afirma lo que la
descripción omite y desmiente lo que el nombre promete.** Las dos mitades de la regla son una sola: **la descripción del
paquete no es evidencia** — ni positiva ni negativa. La tendencia 89 ya decía *«abrir el README»*; este pase mide **cuánto
cuesta no hacerlo**: una puerta MCP entera, en la única capa de estándares donde esta KB tenía puerta.

## 98. Un flag con default seguro convierte un riesgo de arquitectura en una línea de code review (agregado en el pase 32 del 2026-10-02)

El **gap 59** preguntaba qué hace el `sync` de Libraries v2 cuando el bloque *downstream* fue editado por el docente:
¿sobrescribe, rechaza, marca conflicto? **Ninguna de las tres: preserva.**
`SyncFromUpstreamView.post` acepta `override_customizations`, que **vale `False` por omisión**, más
`keep_custom_fields` para blindar campos puntuales cuando sí se pide sobrescribir.

**Por qué es una tendencia y no un detalle de implementación:** el riesgo que esta KB tenía anotado como *«hay que medir
si la propagación es segura para contenido que el docente toca»* —un riesgo de arquitectura, de los que se cotizan como
diseño— **se reduce a vigilar que ningún integrador mande `override_customizations: true` sin `keep_custom_fields`**. Eso
es una regla de *code review*, no un rediseño.

**El corolario general, que vale para evaluar cualquier dependencia:** antes de cotizar la mitigación de un riesgo, **leer
los defaults**. Un proyecto que eligió el default conservador ya pagó ese diseño. Un proyecto que eligió el default
destructivo traslada el costo al integrador — y **el mismo archivo tiene un caso de cada uno**: el `sync` preserva por
omisión, pero si `block_type == "video"` **llama `clear_transcripts` y borra todas las transcripciones antes de copiar
las del upstream**. Default seguro en un camino, destructivo en el otro, **en la misma función**.

## 99. El registro de paquetes es un instrumento **sesgado por el canal de distribución**, y el sesgo ya produjo una ausencia falsa en esta KB (agregado en el pase 35 del 2026-10-02)

Los pases 30, 31 y 32 instalaron un método de descubrimiento que funcionó y rindió hallazgos reales: **consultar el
registro de paquetes del lenguaje de la plataforma** (`registry.npmjs.org`, `pypi.org`, Packagist) en vez de buscar
repos en GitHub. El pase 30 lo formuló así: *«la puerta la publicó el proyecto en PyPI, no en GitHub con nombre
`*-mcp`»*. **Es verdadero y es parcial**, y este pase midió dónde se rompe.

**La medición:**

| Pieza de la capa de telemetría | npm | PyPI | Packagist | Cómo se distribuye de verdad |
|---|---|---|---|---|
| `yetanalytics/lrsql` (el LRS Apache-2.0 vivo) | — | — | — | **Docker Hub + releases de GitHub** (uberjar JVM/Clojure) |
| `DavidLMS/learnmcp-xapi` (la puerta MCP de xAPI) | 🔴 **`total: 0`** | 🔴 **404** | — | **Ninguno: se instala desde el código** |
| `openfun/ralph` (el LRS MIT europeo) | — | ✅ pero **release de 2024-07-11** | — | **`main` de git** para lo actual |

**La regla:** el registro de paquetes de un lenguaje sólo es el instrumento correcto **si la pieza se distribuye como
librería de ese lenguaje**. Una plataforma entregada como **contenedor** o **uberjar** no está en ningún registro de
librerías. Una herramienta que se instala **desde el código** no está en ninguno, punto. Y un proyecto **vivo en `main`
y parado en el registro** se lee como abandonado si sólo se mira el registro.

🔴 **Por qué es una tendencia y no una nota de método: el sesgo ya costó una afirmación falsa publicada.** El **gap 60**
del pase 32 declaró —con la palabra *«medido»*— que **xAPI/LRS no tiene puerta MCP**. La lista de candidatos que abrió
para medir venía del registro; `learnmcp-xapi` no puede estar en esa lista; y la conclusión salió al revés de la
realidad… **que esta misma KB tenía escrita desde el pase 6, en cuatro archivos.** El instrumento se volvió tan
dominante que **se le creyó por encima de la tabla propia**.

**El corolario operativo, y es de dos líneas:**

1. **Antes de declarar una ausencia, consultar esta KB** (`grep` sobre los ocho archivos). Cuesta segundos.
2. **Antes de concluir desde un registro, preguntarse cómo se distribuye la categoría que se está buscando.** LMS y LRS
   se entregan como servicio o contenedor; parsers y SDK se entregan como librería. **Son canales distintos y hace falta
   mirar los dos.**

---

## 100. Para un estándar cuyos implementadores se llaman con palabras comunes, el instrumento es el **nombre de la organización**, no el del paquete (agregado en el pase 35 del 2026-10-02)

El **gap 51** venía abierto desde el pase 28 y pedía desambiguar **CASE** (*Competencies and Academic Standards
Exchange*). El pase 32 descartó por escrito el nombre del **estándar** —`registry.npmjs.org` hace **OR** sobre texto
libre y devolvió **1.696.870** objetos de ruido— y dejó escrita la hipótesis de reemplazo: atacarlo **por el nombre del
proyecto implementador** (`OpenCASE`, `CASS`). **Se hizo, en tres registros, y la hipótesis también falla.**

| Consulta | npm | PyPI | Packagist | Qué devuelve de verdad |
|---|---|---|---|---|
| `opencase` | **7**, 0 del dominio | **404** | **665**, 0 del dominio | Apertura de cajas de skins de videojuego (`opencase`, `skins4go`); en Packagist, *fuzzy match* con **`opencage`** (geocodificador) y **`opencast`** (Apereo) |
| `cass` | ruido | **404** | **26.726** | **Cassandra**, **USPS CASS** (validación de direcciones postales), un *pack* Shimeji, OSU CASS |
| `qti3` | **12** `@longsightgroup/*` ✅ | **404** | — | El stack real |
| `learning_locker` | **1**, exacto ✅ | — | **3**, exactos ✅ | El LRS y su *statement factory* |
| `tincan` | ruido mezclado | ✅ | — | Entre el ruido, **un MCP activo sin relación con educación** |

**El patrón que explica los cinco resultados:** el nombre desambigua cuando es **compuesto y poco común**
(`learning_locker`, `qti3`) y falla cuando es **una palabra común o un acrónimo corto** (`cass`, `opencase`). El filtro
de licencia no ayuda —el ruido también es MIT— y el filtro de actividad tampoco —el ruido también está activo.

🟢 **El instrumento que sí funcionó en los cinco casos es el nombre de la organización:** `LongsightGroup` (QTI 3 en
TypeScript), `oat-sa` (QTI en PHP, 36 paquetes en Packagist), `yetanalytics` (SQL LRS), `openfun` (Ralph),
`LearningLocker`. **La organización es un identificador casi único; el estándar y el producto, no.** **Gap 51 cierra
como no-resoluble por nombre de paquete**, con el método de reemplazo escrito.

---

## 101. Una ausencia declarada se sostiene sólo si está medida por **dos instrumentos distintos** — y el gap 60 es el caso que lo demuestra por las dos caras (agregado en el pase 35 del 2026-10-02)

El **gap 60** del pase 32 afirmó dos ausencias en una sola frase: *«QTI y xAPI/LRS no tienen puerta MCP»*. Este pase
volvió a preguntar por las dos, **con un instrumento distinto del que las midió** (búsqueda abierta en vez de registro),
y el resultado **se partió**:

| Mitad del gap 60 | Instrumento 1 (pase 32: README de candidatos del registro) | Instrumento 2 (pase 33: búsqueda abierta) | Veredicto |
|---|---|---|---|
| **xAPI / LRS** | «no hay puerta» | 🔴 **`learnmcp-xapi`, MIT, 3 tools** — y estaba en esta KB desde el pase 6 | 🔴 **FALSA** |
| **QTI** | «no hay puerta» | ✅ **nada**: ninguna implementación, el ecosistema MCP no nombra QTI | ✅ **CONFIRMADA** |

**Por qué es una tendencia y no la anécdota de un error:** las dos mitades se midieron **igual de bien** y una era falsa.
La diferencia no estuvo en el rigor sino en **si el instrumento podía ver el objeto**. Para xAPI no podía —la pieza no
está en ningún registro— y la ausencia medida fue **el borde del instrumento confundido con el borde del campo**.

**La regla, y es la más barata de todas las que esta KB escribió:** 🔵 **una ausencia se publica con el instrumento
anotado al lado, y se promueve a «no existe» sólo cuando dos instrumentos independientes coinciden.** Hasta entonces se
escribe *«no lo encontré con X»*, que es una frase distinta y defendible. La mitad QTI del gap 60 ya cumple el
requisito; **es la única ausencia de esta base que lo cumple con dos instrumentos y una lectura de SDK.**

---

## 102. El mismo rail de seguridad se está reinventando en dos lugares del protocolo, y **sólo uno frena solo** (agregado en el pase 35 del 2026-10-02)

El pase 30 encontró en `openedx-mcp` el modelo de amenaza escrito en el código —*«a looping agent… a retry storm that
mass-enrols or deletes»*— y su mitigación: **dry run + confirm token atado a una huella del payload** (tendencia 84).
Este pase encontró **la misma primitiva en `coursecode`, resuelta por otro mecanismo**:

| | `openedx-mcp` (AGPL-3.0) | `coursecode` (MIT) |
|---|---|---|
| Dónde vive el freno | **En el servidor**: emite un *confirm token* que el cliente debe devolver | **En el contrato**: `annotations: { readOnlyHint: false, idempotentHint: false, destructiveHint: false }` |
| Ensayo sin efecto | *dry run* | **`dryRun: true`** — *«no API calls, no audio written»* |
| Aprobación | Rechaza la llamada sin token | **Una frase en la descripción**: *«requires explicit user approval before running»* |
| ¿Frena solo? | 🟢 **Sí** — el servidor rechaza | 🔴 **No** — si el cliente MCP ignora las anotaciones, la escritura ocurre |

**La convergencia es la buena noticia:** dos proyectos sin relación, con licencias distintas y en lenguajes distintos,
llegaron a la misma conclusión —*las escrituras de un agente sobre un sistema educativo necesitan ensayo y
confirmación*— y la implementaron sin copiarse. **Eso convierte la primitiva en expectativa de categoría**, no en rasgo
de un producto.

🔴 **La mala noticia es la asimetría, y hay que decirla al componer:** las anotaciones MCP son **declarativas**. Un
cliente que no las lea ejecuta `coursecode_narration` y **gasta crédito de un proveedor TTS pago** sin preguntar. El
*confirm token* no depende del cliente; la anotación sí. **Un stack que compone los dos conectores hereda el freno más
débil de los dos** a menos que el orquestador implemente la confirmación por su cuenta.

**La regla para cotizar:** cuando un conector declara su rail por anotaciones y no por protocolo, **la confirmación es
trabajo del integrador** y entra en la estimación. Es la misma lección que la tendencia 98 (*leer los defaults*) un
nivel más arriba: **leer también quién los hace cumplir.**
## 107. Las estrellas de GitHub y las descargas del registro miden cosas distintas, y en infraestructura educativa se contradicen en los dos sentidos (agregado en el pase 35 del 2026-10-02)

**La tendencia 23 de esta KB —«las estrellas de GitHub esconden la infraestructura educativa que está realmente
desplegada»— se escribió sin instrumento para medir lo que escondían.** El instrumento existe y es público:
`downloads.monthly` de Packagist y el histórico de releases de PyPI y npm. Aplicado a las piezas que esta base ya tenía:

| Pieza | ★ | Descargas total / mes | Último release |
|---|---|---|---|
| `learninglocker/learninglocker` | **583** | 🔴 **2.960 / 0** | 2017-04-04 |
| `RusticiSoftware/TinCanPHP` | 88 | 🔵 **863.777 / 6.178** | 2019-03-05 |
| `oat-sa/qti-sdk` (`qtism/qtism`) | 85 | **218.212 / 3.104** | 2026-07-09 |
| `oat-sa/extension-tao-testqti` | **8** | **117.544 / 950** | 2026-09-30 |
| `php-xapi/client` | 23 | 48.104 / 825 | 2021-03-24 |

**La contradicción va en los dos sentidos y eso es lo que la vuelve una tendencia y no una anécdota.** Hacia abajo:
**583 estrellas con cero descargas mensuales** es atención fosilizada — un proyecto que la comunidad marcó y nadie
instala. Hacia arriba: **8 estrellas con 950 descargas mensuales y 844 versiones etiquetadas** es infraestructura que se
despliega sin que nadie la aplauda, y **88 estrellas con 6.178 descargas mensuales** es una librería que sostiene la
telemetría de aprendizaje de media industria desde una página de GitHub que parece abandonada.

**Por qué pasa en este sector y no en todos:** en educación el que instala **no es** el que estrella. El que estrella es
un desarrollador que mira el panorama; el que instala es un integrador que resuelve un requerimiento de la institución y
no vuelve a GitHub. **El sector tiene una capa de consumo institucional invisible al sistema de reputación del open
source.**

**La regla operativa, y es la que cambia decisiones:** **las estrellas miden interés, las descargas por mes miden
despliegue.** Cuando las dos series se contradicen, la que decide una propuesta es la segunda. Y para promover una pieza
a dependencia de un patrón, **la fecha que importa no es la del primer release, es la del último** — la distancia entre
las dos dice si hay proyecto o hubo publicación.

---

## 108. La capa de conectores MCP de LMS pasó de escasa a saturada en siete pases, y el problema cambió de «encontrar» a «elegir» (agregado en el pase 35 del 2026-10-02)

El pase 26 declaró que Moodle **no tenía** conector MCP permisivo. El 27 encontró dos y agregó la columna. El 30 cerró el
último hueco (Open edX). Este pase cuenta la columna completa: **Canvas tiene cinco puertas —cuatro MIT— y Moodle cuatro
más un cliente envolvible.** **Nueve puertas entre las dos LMS más desplegadas, ocho permisivas, en siete pases.**

**La consecuencia comercial invierte el pitch.** La pregunta de 2026 no es *«¿hay que construir el conector?»* —no hay
que construirlo— sino **«¿cuál, y quién lo mantiene?»**. Lo que se cotiza es **selección, auditoría de licencia,
auditoría de superficie de escritura y mantenimiento**, y eso es un trabajo distinto: es *due diligence* de dependencias,
no desarrollo. **Globant cobra por decidir bien, no por escribir lo que ya está escrito.**

**Y el criterio de selección no es el obvio.** La puerta más grande de esta KB tiene **8 estrellas**
(`bruchris/canvas-lms-mcp`, 165 tools) y la más estrellada tiene **cifra de tools inestable**
(`vishalsachdev/canvas-mcp`, 269 ★, declara 40+/80+/116 según la versión). **El criterio que sirve es: cifra consistente
entre el `description` del paquete y el README, cantidad de versiones publicadas, y fecha del último release.**

---

## 109. La fecha del último release es el único indicador de madurez que ninguna de las puertas de esta KB publicaba, y cambia la cotización de un patrón entero (agregado en el pase 35 del 2026-10-02)

Tres pases consecutivos celebraron la puerta oficial de Open edX: el 30 la descubrió y construyó **P61** encima, el 31
midió sus 35 rutas, el 32 leyó su código. **Ninguno mirό las fechas de publicación.** Leídas:

| Paquete | Releases | Ventana | Silencio | Versión hoy |
|---|---|---|---|---|
| `openedx-mcp` | 5 | **2026-07-24 → 2026-07-25** | **70 días** | **0.1.5** |
| `tutor-contrib-openedxmcp` | 7 | **2026-07-24 → 2026-07-25** | **70 días** | **0.1.7** |

**Doce releases en dos días y nada en los setenta siguientes, todavía en `0.1.x`.** Esa curva —ráfaga inicial, silencio,
versión sub-1.0— es la firma de un **experimento publicado una vez**, no de un producto mantenido.

🔵 **Lo importante es que nada de lo medido se cae.** Las 35 rutas existen, las 19 escrituras existen, y **los cuatro
rails contra «agente en bucle» siguen siendo el artefacto más reutilizable que encontró esta base.** Lo que cambia es el
**modelo de costo**: una propuesta que dependa de esta puerta **presupuesta mantenerla**, y eso es una conversación
honesta que se puede tener en el *discovery*, no una sorpresa en el mes cuatro. **El chequeo cuesta una llamada HTTP al
JSON del registro, y hay que hacerlo cada vez que una pieza se promueve a dependencia de patrón.**

---

## 110. La prueba de accesibilidad de la evaluación existe en permisivo desde este pase, y es la primera obligación vencida de esta KB que tiene con qué cumplirse (agregado en el pase 35 del 2026-10-02)

El pase 8 abrió la capa de accesibilidad y la cerró con un diagnóstico: **la tecnología asistiva madura es toda copyleft,
y lo agéntico y permisivo no pasa de 15 estrellas.** El pase 17 agregó que la obligación europea de accesibilidad es **la
única de esta KB con fecha ya vencida**, y **P17** se escribió sin pieza que la cumpliera.

**La pieza apareció, y apareció donde nadie la buscó: adentro de la pila de evaluación.**
`@longsightgroup/qti3-a11y` (**MIT**, 0.13.1 del **2026-10-01**) publica **`accessibilityProofMatrix`**,
**`a11yContracts`** y **`manualAssistiveTechnologyScripts` para VoiceOver, NVDA y JAWS** — contratos de teclado, foco,
nombre accesible y mensaje de validación **por tipo de interacción**. Y `@longsightgroup/qti3-pnp` (**MIT**, cero
dependencias) resuelve **QTI 3 *Personal Needs and Preferences***.

**Por qué es un cambio de categoría y no una librería más:** lo que estas dos piezas entregan es **metadato de prueba
legible por máquina**, no una característica de accesibilidad. **La diferencia entre «el ítem es accesible» y «acá está
la matriz de prueba, el contrato por interacción y el guion de verificación con tres lectores de pantalla» es
exactamente la diferencia entre una afirmación y un expediente.** Y el expediente es el entregable que EMEA compra.

⚠️ **Lo que no resuelve, y lo declara su propio README:** *«It does not fetch, store, authorize, or transmit PNP records.
LMS identity, consent, institutional policy, persistence, LTI launch handling, and AfA PNP service access belong outside
this package.»* **Identidad, consentimiento, política institucional, persistencia, *launch* LTI y el servicio AfA PNP son
trabajo a cotizar.** Que lo diga el proyecto en vez de dejarlo implícito es lo que vuelve la cotización defendible.

---

## 111. El estándar más desplegado de la capa de evaluación es copyleft, y lo permisivo es lo nuevo — el orden inverso al del resto de esta KB (agregado en el pase 35 del 2026-10-02)

Esta base encontró cinco veces la misma forma (tendencias 18, 19, 22, 27 y la del pase 9): **lo maduro es copyleft, lo
permisivo es chico.** En evaluación eso ahora está **medido con números de despliegue**, y la asimetría es más grande que
en cualquier otra capa:

- 🔴 **Copyleft y desplegado:** `oat-sa/qti-sdk` — **GPL-2.0-only**, **218.212 descargas**, **293 versiones**, release del
  2026-07-09. `oat-sa/extension-tao-testqti` — **GPL-2.0-only**, **117.544 descargas**, **844 versiones**, release del
  **2026-09-30**.
- ✅ **Permisivo y nuevo:** `@longsightgroup/qti3-*` (**MIT**, 12 paquetes, 0.13.1 del **2026-10-01**, `qti3-core` y
  `qti3-pnp` con **cero dependencias de terceros**) e `instructure/qti` (**MIT**, QTI 1.2, 174 commits).

**Lo que esto obliga a hacer distinto en un *discovery*: preguntar si TAO ya está instalado.** Con **117.544 descargas**
y 844 versiones, la probabilidad de que un cliente institucional grande **ya tenga TAO adentro** no es marginal, y eso
cambia el punto de partida del proyecto de «elegir un stack QTI» a «convivir con el que hay».

**Y vuelve a P20 y P48 más valiosos, no menos:** si lo único permisivo es nuevo y chico, **entonces la pila permisiva es
el diferencial**, no el plan B. Lo que no se puede hacer es esconder la madurez detrás de la palabra «MIT». **Se declara
por delante.**

---

## 112. La puerta de agente de un estándar la tiene el servidor, no el SDK — y la frase «X tiene puerta MCP» hay que calificarla por artefacto (agregado en el pase 35 del 2026-10-02)

Esta KB tiene escrito, desde el pase 25, que **CaSS es la primera pieza de estándar educativo con puerta nativa de
agente**, y el 26 midió su cartucho MCP (6 tools, 3 resource templates). **Todo eso es cierto — del servidor.**

Medido en este pase: **`cassproject` 5.0.19 (Apache-2.0, npm, publicado el 2026-08-12, activo) tiene cero menciones de
«MCP» y de «Model Context Protocol» en su README crudo.** El SDK JavaScript del mismo proyecto **no expone la puerta**.

**La consecuencia práctica es inmediata y vale para cualquier estándar:** un integrador que llega a CaSS por npm —que es
el camino natural de un proyecto JavaScript— **no hereda MCP**, hereda una librería. Para tener la puerta hay que
**desplegar el servidor** y, además, sortear la trampa de *loopback* que el pase 27 documentó (si el `fetch` a
`localhost/api/swagger.json` falla, la ruta `/api/mcp` **no se monta y el servidor arranca igual**).

**La regla:** cuando esta base afirme que una pieza «tiene puerta MCP», **tiene que decir en qué artefacto** —servidor,
plugin, SDK, CLI— porque **la puerta no se hereda hacia los paquetes cliente**. Es el mismo error de alcance que el pase
32 cometió con el árbol REST de Open edX, en otra capa.

---

## 113. El control de vocabulario del dominio es asimétrico: sirve para rechazar, nunca para aceptar (agregado en el pase 35 del 2026-10-02)

El pase 32 estableció la tendencia 96 después de encontrar que las dos piezas llamadas «xapi» eran **cripto/Web3** y
**forex**: contar menciones del vocabulario del dominio en el README crudo es el único filtro que las atrapa. **El
control es correcto y este pase lo confirma con una colisión nueva —`censo-escolar` devuelve una billetera Solana—, pero
también le encontró el falso negativo:**

| Pieza | Vocabulario del dominio | ¿Es del dominio? |
|---|---|---|
| `oat-sa/qti-sdk` | 84 | Sí |
| `php-xapi/client` | 15 | Sí |
| `RusticiSoftware/TinCanPHP` | 2 | Sí |
| `cassproject/cass-npm` | 🔴 **0** | 🔴 **Sí** — SDK de *Competency and Skills Service* |
| `RusticiSoftware/TinCanPython` | 🔴 **0** | 🔴 **Sí** |

**Dos piezas que son del dominio puntúan cero, y la causa es de género textual, no de contenido:** su README es un
*quickstart* de SDK —instalar, importar, llamar— sin una línea de prosa sobre el problema que resuelve. **Los SDK buenos
no explican su dominio: lo asumen.**

**Por lo tanto el control se usa en una sola dirección.** Un conteo **alto** no prueba nada por sí solo (un artículo
*sobre* AI en educación puntúa altísimo y no es una pieza de software). Un conteo **bajo** no descarta: dice **«el README
no alcanza para decidir»**, y entonces hay que leer el `package.json`, el archivo `LICENSE` y el árbol. **Lo único que el
control rechaza con confianza es la pieza cuyo README habla con fluidez de OTRO dominio** —cripto, forex,
geocodificación—, que es exactamente el caso que lo originó.

---

## 114. Brasil está construyendo una capa MCP nacional sobre sus datos públicos, y educación es el único dominio grande que falta (agregado en el pase 35 del 2026-10-02)

**Siete pases declararon el barrido regional de LATAM saturado.** Este pase lo atacó por un canal distinto —el registro
de paquetes consultado en portugués y español— y encontró lo contrario de un silencio.

| Dominio de dato público brasileño | Paquete MCP | Licencia | Última versión |
|---|---|---|---|
| Geografía, **censo**, economía, salud | `ibge-br-mcp` | **MIT** ✅ | **2026-09-27** (24 versiones desde 2026-01-18) |
| Banco Central (SGS) | `bcb-br-mcp` | — | **2026-09-28** |
| Salud — **DATASUS SIH/SUS** (internaciones, AIH) | `sih-br-mcp` | — | **2026-10-01** |
| Firma electrónica | `@signdocs-brasil/mcp-server` | — | 2026-09-07 |
| 🔴 **Educación — INEP / Censo Escolar / ENEM** | 🔴 **nada** | — | `inep` → 3 resultados, ninguno MCP; `censo-escolar` → 18, todos colisión; `enem` → 6, el más nuevo de 2024 |

**Lo que importa no es que falte: es que el patrón ya está establecido y educación quedó afuera de él.** Hay cuatro
dominios de dato público brasileño con servidor MCP, uno de ellos **MIT con 24 versiones en nueve meses y con procedencia
de fuente** (`ibge-br-mcp`), y **los tres datasets educativos canónicos de Brasil —INEP, Censo Escolar, ENEM— no tienen
ninguno.**

**Por qué es la mejor oportunidad LATAM que esta base identificó, y no es una opinión:** (a) **existe plantilla**, así que
no se diseña, se replica; (b) **existe demanda medida** —**92 % de estudiantes y 79 % de docentes** de LATAM usan AI, con
**65 % de estudiantes temiendo el aprendizaje superficial**, y un servidor con procedencia de dato público es
exactamente la respuesta a esa objeción; (c) **es contribución *upstream* visible**, del tipo que abre puerta
institucional en una región donde **sólo 8 % de las instituciones tiene presupuesto dedicado**. Ver **P74**.

⚠️ **El límite de este hallazgo, declarado:** se midió la **ausencia en los registros de paquetes** (npm y PyPI). **No se
midió si existe fuera de un registro** —un repo sin publicar, un proyecto de una secretaría de educación— y en este
entorno la búsqueda de código de GitHub está fuera de alcance. **La ausencia está medida en el canal, no en el mundo.**

---

## 103. El registro de servidores falla en **las dos direcciones**, y por eso no se corrige buscando mejor (agregado en el pase 35 del 2026-10-02)

El pase 33 midió el **falso negativo**: `learnmcp-xapi` es MIT, open source y está en esta KB desde el pase 6, y **no
aparece en ningún registro** (PyPI 404, npm `total: 0`). Este pase midió el **falso positivo** y es del mismo tamaño:
`quizlar/mcp-server` aparece como **servidor MCP educativo activo con `LICENSE` MIT**, y **no tiene código**.

| | Falso negativo (pase 33) | Falso positivo (pase 34) |
|---|---|---|
| Caso | `learnmcp-xapi` | `quizlar/mcp-server` |
| El registro dice | **nada** | **MIT, MCP, educación, activo** |
| La realidad | **MIT, 3 tools, en esta KB desde el pase 6** | 🔴 **un manifiesto de 25 líneas; implementación alojada y propietaria** |
| Error producido | se declara ausente lo que existe | **se promueve como open source un servicio de proveedor** |

🔵 **Por qué esto es una tendencia y no una anécdota doble.** Un instrumento con falsos negativos se compensa
**agregando instrumentos** —y es lo que la tendencia 101 ya pide—. Un instrumento con falsos negativos **y** falsos
positivos no se compensa con volumen: **cada resultado que devuelve hay que verificarlo por su cuenta**, porque ni su
silencio ni su afirmación son informativos. **La consecuencia práctica para este barrido es que el registro sirve para
generar candidatos y nunca para aceptarlos ni para descartarlos.**

⚠️ **Y la ironía operativa, que conviene dejar escrita:** `mcp.so` —el registro de servidores MCP, **el instrumento
natural para este objeto de estudio**— está **bloqueado por el proxy de egreso**. Este barrido no puede consultar el
catálogo específico de lo que busca, así que lo encuentra de rebote por búsqueda abierta, que es el canal que el pase 33
demostró insustituible.

---

## 104. Una licencia permisiva puede cubrir **el manifiesto y no la implementación** — y el campo que lo delata es uno (agregado en el pase 35 del 2026-10-02)

Las colisiones 1 a 8 de esta KB son de **término**: `opencase` son cajas de skins, `tincan` es mensajería entre agentes
de código, `xapi` es forex y cripto. **La novena es de clase nueva y es peor, porque el nombre es correcto, el dominio
es correcto y la licencia es real.** Lo que no es lo que parece es **el alcance de esa licencia**.

`quizlar/mcp-server`, leído de primera mano:

| Archivo | Código | Contenido |
|---|---|---|
| `LICENSE` | **200** | *«MIT License — Copyright (c) 2026 Quizlar»* ✅ **real** |
| `server.json` | **200** | 🔴 **manifiesto de registro MCP, nada más** |
| *fuente* | — | 🔴 **no existe** |

```json
"remotes": [{ "type": "streamable-http", "url": "https://mcp.quizlar.app/mcp/",
  "headers": [{ "name": "Authorization", "isRequired": true, "isSecret": true }] }]
```

🔵 **El control es de un campo, y es barato:** **si `server.json` declara `remotes` y no declara paquete ni fuente, lo
licenciado son metadatos.** El `$schema` del registro MCP (**2025-12-11**) hace de esto una categoría y no un caso: con
el esquema nuevo, **una entrada de registro ya no implica código**, y la distinción entre *servidor que se instala* y
*servidor que se consume* vive en un campo que un barrido automático no mira.

🔴 **Y la consecuencia comercial hay que decirla, porque invierte el argumento de esta KB:** una pieza así significa
**cero código reutilizable, dependencia de proveedor, y datos de aprendizaje del alumno saliendo a un tercero bajo API
key** — lo contrario exacto de la privacidad por diseño que esta base construyó sobre el `ACTOR_UUID` de
`learnmcp-xapi`. **En APAC, donde la soberanía define la infraestructura de ~la mitad de las empresas, este patrón
queda descartado de entrada.**

---

## 105. La primitiva anti-bucle tiene **tres** implementaciones y la más barata frena en la **configuración** (agregado en el pase 35 del 2026-10-02)

La tendencia 102 describió dos mecanismos para el mismo riesgo. Este pase encontró el tercero, en una pieza que esta KB
tenía fichada desde el pase 6 **sin registrar este detalle**: `.env.example` de `learnmcp-xapi` declara
`RATE_LIMIT_PER_MINUTE=30` y `MAX_BODY_SIZE=16384`.

| Pieza | Dónde frena | Mecanismo | ¿Frena solo? | Costo de adopción |
|---|---|---|---|---|
| `openedx-mcp` (pase 30) | **servidor** | *confirm token* atado a una huella del payload | 🟢 **Sí** | alto — hay que implementar el ida y vuelta |
| `coursecode` (pase 33) | **contrato** | anotaciones MCP + `dryRun` | 🔴 **No** — el cliente puede ignorarlas | bajo, pero **el freno es trabajo del integrador** |
| **`learnmcp-xapi`** (este pase) | **configuración** | **30 escrituras/minuto, cuerpo de 16 KiB** | 🟢 **Sí** | 🟢 **dos variables de entorno** |

🔵 **La lección es de diseño y es reutilizable más allá de educación: el mecanismo correcto depende de la forma del
daño.** Donde el daño es **irreversible y discreto** —borrar un curso, desmatricular a un alumno— hace falta
**confirmación**, porque un techo de caudal no impide la única llamada que destruye. Donde el daño es **acumulativo y
continuo** —inundar un LRS de statements, quemar crédito de un proveedor pago— **el techo de caudal es suficiente y es
diez veces más barato que un protocolo de confirmación.**

**Para la capa de telemetría, entonces, el freno de configuración es el adecuado y no un sustituto pobre.** Y corrige
por elevación la lectura de la tendencia 102: no es que `coursecode` eligió el mecanismo débil, es que **eligió un
mecanismo declarativo para un daño que además es acumulativo** (gasto de TTS), donde un límite de caudal lo habría
frenado solo. 🔵 **La regla para cotizar: clasificar el daño antes de elegir el rail, y preguntar siempre quién lo hace
cumplir** (tendencia 102) **y si hace falta que alguien lo haga cumplir** (ésta).

---

## 106. Las fuentes primarias multilaterales son inalcanzables **por clase**, y eso define qué puede afirmar esta KB (agregado en el pase 35 del 2026-10-02)

Tres pases consecutivos reportaron un dominio institucional bloqueado como si fuera un incidente: el pase 30
(`openedx.org`), el pase 33 (`eur-lex.europa.eu`, `data.europa.eu`). **Este pase lo midió como clase, probando las dos
poblaciones:**

| Clase | Dominios probados | Alcanzables |
|---|---|---|
| 🔴 **Multilateral / institucional** | `coe.int`, `unu.edu`, `publications.iadb.org`, `www.unesco.org`, `unesdoc.unesco.org`, `iesalc.unesco.org`, `www.oecd.org`, `ec.europa.eu`, `www.worldbank.org`, `eur-lex.europa.eu`, `data.europa.eu` | 🔴 **0 de 11** |
| ✅ **Registro comercial / de código** | `registry.npmjs.org`, `pypi.org`, `packagist.org`, `hub.docker.com`, `raw.githubusercontent.com` | 🟢 **5 de 5** |

🔴 **La consecuencia hay que escribirla en voz alta porque afecta a cada afirmación de `intel/`: toda cifra de mercado y
toda fecha regulatoria de esta base se apoya en fuentes secundarias comerciales POR CONSTRUCCIÓN DEL ENTORNO**, no por
falta de rigor de los pases. No es que no se intentaran las primarias: **se intentaron once y ninguna responde.**

🔵 **Y eso reclasifica el gap 56 de «acción pendiente» a «límite de clase»**, lo cual es más útil que dejarlo abierto:
probar un dominio europeo más es **previsiblemente inútil**, así que **la acción deja de ser técnica y pasa a ser
organizativa** — hace falta **una lectura hecha fuera de esta red**, y así hay que pedirla. Dos pases ya gastaron
intentos en esto; el tercero no debería.

⚠️ **El costo no es sólo regulatorio, y el ejemplo de este pase lo muestra:** el *working paper* de **UNESCO IESALC**
sobre **200 instituciones de educación superior en 19 países** —la mejor evidencia metodológica que LATAM podía
aportarle a esta KB, muy por encima de las encuestas de 29 instituciones que la base cita— **es inalcanzable
(`unu.edu`)**. 🔵 **Pedirlo por fuera vale más que cerrar el gap 56: el texto del AI Act se puede comprar; esa encuesta
regional es pública, gratuita y nadie más la está usando.**

🔵 **La asimetría también aparece en cosas chicas y conviene anotarla:** `api.npmjs.org/downloads/point/...` devolvió
**vacío** para un paquete con *scope*, mientras **Packagist sí entrega descargas**. Por eso la comparación PHP /
TypeScript del **P69** **no es simétrica en la columna de adopción** — y por eso la decisión se tomó por **licencia**,
que sí está medida en los dos lados.

---

## 115. «Descargas por mes» no es un instrumento general: es un instrumento de UN registro, y el sustituto que sí está en los tres es el ***span* de releases** (agregado en el pase 36 del 2026-10-02)

El pase 35 introdujo las descargas del registro como el instrumento que treinta y cuatro pases no habían usado, y la acción 1 pedía aplicarlo a las 52 filas de `agents/top.md`. **Aplicado, el instrumento resultó estar disponible en un canal de tres:**

| Canal | Metadato | Descargas | Estado |
|---|---|---|---|
| Packagist | ✅ 200 | ✅ `downloads.monthly` | completo |
| npm | ✅ 200 (`registry.npmjs.org`, directo por `no_proxy`) | 🔴 `api.npmjs.org` **403 a CONNECT** | sin descargas |
| PyPI | ✅ 200 (`pypi.org`, directo por `no_proxy`) | 🔴 `pypistats.org` **403 a CONNECT** | sin descargas |

**Y todas las cifras de descargas del pase 35 eran de Packagist** (`qtism/qtism`, `TinCanPHP`, `oat-sa/extension-tao-testqti`, `learninglocker` son PHP), **así que el instrumento nunca se había ejercitado fuera de PHP.** La tabla de agentes es casi toda Python y TypeScript.

🔵 **El sustituto resultó mejor que el original para esta tabla, y es el hallazgo: el *span* de releases** —primera publicación, última publicación, cuántas hay en el medio— **está disponible en los tres canales y distingue algo que las descargas NO distinguen: mantenimiento sostenido contra ráfaga de publicación y silencio.** Un paquete abandonado con base instalada **sigue descargándose**: `rusticisoftware/tincan` tiene **6.178 descargas/mes** y su último release es de **2022-11-02**. Las descargas miden **base instalada**; el *span* mide **vida del proyecto**, y para decidir si una pieza entra en una propuesta importa la segunda.

⚠️ **Corrección a una cifra del pase 35:** escribió que la pieza xAPI más desplegada estaba *«congelada desde 2019»*; **medido en el tiempo de versión de Packagist, el último release es 2022-11-02.**

## 116. Un conteo de FILAS no puede detectar una fila repetida, y esta KB publicó un duplicado durante un pase completo (agregado en el pase 36 del 2026-10-02)

El pase 30 estableció una regla para terminar una pelea que esta KB llevaba cinco veces: **contar `agents/top.md` programáticamente**, filas entre el separador y la primera línea que no empieza con `|`. La regla es correcta y resolvió el problema que tenía. **Y tiene un punto ciego exacto: un duplicado es una fila válida.**

🔴 **`SirhanMacx/Claw-ED` estaba en la tabla dos veces** —**59 ★** y **60 ★**, mismo repo— porque el pase 35 lo contó como alta cuando ya había entrado *«en la tercera pasada del 2026-09-30»*, **frase que está escrita en el historial del mismo archivo, a treinta líneas de la fila nueva.** El conteo programático informó «52 filas» y tenía razón: había 52 filas. **Lo que no había era 52 repos.**

🔵 **El control que cierra el punto ciego cuesta una línea y es el que esta KB adopta de acá en adelante: contar *slugs* distintos, no filas.** Medido así, el archivo es **51 filas = 49 repos de GitHub distintos + 2 entradas de PyPI**, y el número se publica **descompuesto** en vez de como un total. **La regla general: un conteo sirve para detectar lo que varía en la dimensión que mide. «Cuántas filas» y «cuántas cosas» son dos preguntas, y esta KB venía respondiendo la primera creyendo que respondía la segunda.**

## 117. La superficie real de un CLI está en el *dispatch*, no en el texto de ayuda — y en el caso medido la diferencia es del 30 % (agregado en el pase 36 del 2026-10-02)

Para escribir el manifiesto MCP de `qti3-cli` (acción 2 del pase 35, ver **P76**) había que enumerar sus comandos. **El `USAGE` del propio CLI y su `switch` de *dispatch* no coinciden:**

- El `switch` tiene **17 comandos de primer nivel**, no los **14** que esta KB tenía anotados.
- **`certification` tiene CUATRO subcomandos** (`import-basic-items`, `import-basic-tests`, `verify-validator`, `check-import-report`), así que la superficie invocable es de **20 tools**.
- 🔴 **El `USAGE` documenta sólo DOS de esos cuatro.** `verify-validator` y `check-import-report` **no aparecen en el texto de ayuda** — y `import-basic-items` acepta **tres flags que el `USAGE` tampoco menciona** (`--validator-package`, `--trusted-report-sha256`, `--require-validator-evidence`).

**Un envoltorio MCP generado desde el `USAGE` —que es lo natural, porque es el texto que el proyecto ofrece como contrato— nace con 6 de 20 tools afuera: el 30 %.** 🔵 **La regla operativa para cualquier CLI que esta KB envuelva: leer el *dispatch*.** Es la misma lección que la tendencia 104 dio para los manifiestos MCP (la licencia cubría el manifiesto y no la implementación) y que el pase 33 dio para `coursecode` (15 tools definidas / 15 en *dispatch*, que ahí **sí** coincidían): **el artefacto manda sobre su descripción, y hay que mirarlo incluso cuando el proyecto parece prolijo** — `qti3-cli` lo es, y aun así su ayuda está incompleta.

## 118. La cuarta variante de primitiva de seguridad no frena al agente: ancla la confianza en un artefacto EXTERNO (agregado en el pase 36 del 2026-10-02)

Esta KB viene registrando la misma necesidad reinventada por mecanismos distintos: **confirm token** del lado servidor (`openedx-mcp`), **anotaciones MCP + `dryRun`** del lado contrato (`coursecode`), **techo de caudal por variable de entorno** del lado configuración (`RATE_LIMIT_PER_MINUTE`). La tendencia 109 concluyó que **el mecanismo correcto depende de la forma del daño**.

🟢 **`qti3-cli` aporta una cuarta variante que no encaja en ese eje, y por eso lo extiende:** `certification verify-validator` toma **`--trusted-report-sha256 <digest>`** y verifica el reporte del validador oficial del consorcio contra un digest de confianza; `import-basic-items` acepta **`--require-validator-evidence`** para **exigirla**.

🔵 **Las tres primeras frenan una ACCIÓN del agente. Ésta no frena nada: valida la PROCEDENCIA de un insumo.** El daño que previene no es «el agente escribió algo que no debía», es **«el expediente se construyó sobre un reporte que no es el que publicó el consorcio»** — y en un entregable de conformidad **ése es el que importa**, porque es exactamente la pregunta que hace un auditor. **La consecuencia de catálogo: el eje de la tendencia 109 (forma del daño) necesita un segundo eje — QUÉ se protege: la acción del agente, o la integridad del insumo.** Las cuatro variantes se reparten 3 a 1, y la cuarta es la única que sirve para firmar algo.

## 119. Un nombre de paquete GENÉRICO en el manifiesto es un predictor de colisión, y hay que sospecharlo ANTES de consultar el registro (agregado en el pase 36 del 2026-10-02)

La medición de las 49 filas (**P76**, `agents/top.md`) resolvió el nombre de paquete leyendo el manifiesto de cada repo y lo verificó contra el *backlink* del registro. **Dos coincidencias que el nombre daba por buenas eran colisiones:**

- 🔴 **Colisión 10 — `tero`:** `marcorojasb/tero` declara `tero` en su `pyproject.toml`; el `tero` de PyPI es *«Configures development machines to cloud resources»*, de `djaodjin/drop`.
- 🔴 **Colisión 11 — `mcp-server`:** `paulocymbaum/ed-tech-system-mcp` declara el nombre **`mcp-server`**, tomado en PyPI por un tercero sin `project_urls`.

**Las once colisiones de esta KB se venían describiendo como un problema del BUSCADOR** —buscar `cass` devuelve Cassandra, buscar `OpenCASE` devuelve OpenCage (tendencias 100 y 113)—. 🔵 **Estas dos son de clase distinta y más peligrosa: no hubo búsqueda.** El nombre vino **del manifiesto del propio repo**, que es la fuente más autoritativa posible, y aun así apuntó a otro software. **La causa es que el autor eligió un nombre genérico y no lo registró, o lo registró otro antes.**

**La regla que esto agrega: la genericidad del nombre declarado es una señal de riesgo evaluable sin red.** `mcp-server`, `tero`, `learn`, `lumen` son sospechosos por construcción; `@longsightgroup/qti3-cli`, `openedu-mcp-server`, `canvas-lms-mcp` no lo son. ✅ **Y el control que resuelve las dos clases es el mismo y ya está probado: el *backlink* del registro al repo.** **Ninguna fila de esta KB debe llevar dato de registro sin él** — y cuando no hay `project_urls` (caso `mentar`), se acepta por coincidencia de descripción y **se marca como confirmación débil**, nunca como medición.

## 120. Un `package.json` en el repo no implica un paquete instalable, y en esta tabla pasa en 7 de 49 (agregado en el pase 36 del 2026-10-02)

El pase 33 midió que `learnmcp-xapi` **no está en ningún registro** y se instala desde el código, y la tendencia 99 concluyó que un barrido que arma su lista de candidatos en npm/PyPI **tiene cero probabilidad de verlo**. **Este pase cuenta cuán común es, mirando desde el otro lado: no «qué no encuentra el registro», sino «qué repos declaran un paquete que el registro no tiene».**

🔵 **Son 7 de 49, y el más grande es el tercero de la tabla:** `Crosstalk-Solutions/project-nomad` (**38,8 k ★**) declara `project-nomad` en npm → **404**; `GarethManning/education-agent-skills` (815 ★) → 404; `Open-TutorAi/open-tutor-ai-CE` (107 ★, declara `open-tutorai`) → 404; más `Alvarmethod`, `gradescope-mcp`, `openedu-mcp` (declara `openedu-mcp-server`) y **la mitad npm de `vishalsachdev/canvas-mcp`** (`canvas-mcp-code-api` → 404, **mientras su mitad PyPI sí está publicada**, 22 releases, 2026-09-28).

⚠️ **Lo operativo, que es lo que va en una propuesta: para estas siete la vía de instalación es `git clone`, no el gestor de paquetes.** Eso cambia el costo de integración (no hay *pinning* de versión, no hay *lockfile*, la actualización es un *pull*) y **hay que decirlo al cotizar**, porque es la diferencia entre una dependencia y un *fork* de hecho.

🔵 **Y la contracara, que evita un error de categoría: 22 de 49 filas no publican NINGÚN manifiesto, y la mayoría pertenece a una clase que no se distribuye como paquete — la *skill* de agente** (`human-skill-tree` 562 ★, `lineage-skill` 448 ★, `universal-examprep-skill` 299 ★, `algo-sensei` 281 ★, `universal-diagnostic-tutor-skill` 235 ★). **Una *skill* se consume clonando el repo o copiando el directorio.** Medir su adopción por registro **no es una ausencia, es una pregunta mal hecha**: para esa clase el instrumento disponible sigue siendo estrellas y *forks*, y conviene escribirlo en la celda en vez de dejarla vacía. **Balance final de las 49: 14 con *backlink* verificado y release real, 6 con cadencia sostenida, 7 que declaran paquete inexistente, 22 sin manifiesto, 2 colisiones descartadas.**

## 121. El calendario del AI Act tiene DOS fechas, y la intuición sobre cuál aplica en educación es la equivocada — el anexo manda sobre la arquitectura de entrega (agregado en el pase 36 del 2026-10-02)

Esta KB viene peleando con el calendario del AI Act desde el pase 22 —seis veces registradas— y el gap 56 lo cerró **a nivel de inciso**: el **Artículo 113** difiere el Capítulo III al **2027-12-02** para los sistemas del Anexo III.

🔴 **El barrido regional de este pase devuelve una segunda fecha que esta base no registraba.** El ***Digital Omnibus on AI***, aprobado por el **Consejo el 2026-06-29**, fija fechas revisadas **en dos tramos**: **2027-12-02 para el alto riesgo *autónomo*** (*stand-alone*) **y 2028-08-02 para el alto riesgo embebido en productos ya regulados.**

🔴 **Y acá esta tendencia documenta su propio error, porque la primera lectura de este pase fue la intuitiva y era falsa.** El razonamiento tentador es: *«un motor de evaluación rara vez se entrega solo, se entrega dentro de un LMS, así que cae en el tramo de 2028 y hay ocho meses más»*. **Es falso, y el control que lo rompe es leer QUÉ CONTIENE CADA ANEXO en vez de qué significan las palabras «autónomo» y «embebido»:**

- **Anexo III** — nombra explícitamente las herramientas de **educación**, junto con contratación, *credit scoring*, *law enforcement* y control de fronteras → **2027-12-02**.
- **Anexo I** — productos con **régimen de conformidad propio**: **dispositivos médicos, maquinaria, vehículos** → **2028-08-02**.

⚠️ **Un LMS no es un producto regulado del Anexo I.** Por lo tanto **un motor de evaluación entregado dentro de un LMS sigue en el 2027-12-02**, y la segunda fecha **no le da prórroga a este sector**. 🔵 **La pregunta correcta de *discovery* no es «¿autónomo o embebido?» —que es la que invita al error— sino «¿el producto que lo contiene tiene conformidad propia del Anexo I?»**, cuya respuesta en educación es **casi siempre no**.

🔵 **La lección de método, que es por la que esta tendencia vale más que la fecha: el error tenía el signo peligroso.** Una fecha equivocada que te hace creer que falta MENOS tiempo se descubre sola; una que te hace creer que falta MÁS se descubre cuando ya es tarde. **Es el mismo tipo de trampa que la advertencia de Taiwán del pase anterior —una fecha correcta sosteniendo una conclusión falsa— y el control es el mismo: verificar que la categoría del instrumento incluya al sujeto, no sólo que la fecha sea correcta.** ✅ **Dato que sí conviene retener del corrimiento real: las fechas originales eran 2026-08-02 (Anexo III) y 2027-08-02 (Anexo I)**, así que el Anexo III **se corrió ~16 meses** —el corrimiento que esta KB ya tenía registrado— **y se detuvo en 2027-12-02.**

⚠️ **Y la advertencia de siempre, sin excepción: es fuente secundaria comercial.** El **gap 65** está cerrado como **límite de clase** —el dominio legal europeo responde **403 a CONNECT**— así que **esta fecha entra concordante y no primaria**, igual que las siete anteriores.

## 122. Las fuentes gubernamentales son inalcanzables por CLASE, y ya son dos dominios nacionales confirmados con control negativo (agregado en el pase 36 del 2026-10-02)

El pase 34 estableció que las primarias multilaterales son inalcanzables por clase (**0 de 11** dominios institucionales contra **5 de 5** registros comerciales y de código), y el pase 35 lo confirmó en el dominio legal europeo. **Este pase lo confirma en un segundo dominio nacional y con el control negativo que el pase 35 pidió explícitamente:**

🔴 **`dados.gov.br`, `servicodados.ibge.gov.br`, `api.dados.gov.br` y `www.gov.br` responden 403 a CONNECT**, y **`WebFetch` sobre `dados.gov.br` devuelve `EGRESS_BLOCKED`** — **dos instrumentos independientes.** ✅ **Control positivo en la misma corrida: `registry.npmjs.org` → 200.** La red funciona.

🟢 **Y el control que esta tendencia aporta como método reutilizable, porque distingue tres estados que se confunden: `getent hosts` separa «bloqueado» de «inexistente».** Medido: `github.com` y `registry.npmjs.org` **resuelven**; **`dados.gov.br` RESUELVE** —así que su 403 es **política del proxy**, no DNS—; **`api.dadosabertosinep.org` NO resuelve**, igual que un dominio inventado de control. 🔵 **Por eso se puede afirmar algo más fuerte que «no pude verificarlo»: la única API de INEP que existe está CAÍDA, no bloqueada.** **La regla: antes de declarar un dominio muerto, resolverlo; y antes de declararlo bloqueado, resolverlo también.** Un 403 sobre un nombre que resuelve y la no-resolución de un nombre son hallazgos distintos, y esta KB venía reportando los dos como «no alcanzable».

## 123. La ausencia de API en la fuente pública no es un detalle de implementación: cambia la ARQUITECTURA y multiplica el plazo por cuatro (agregado en el pase 36 del 2026-10-02)

El gap 69 identificó la mejor oportunidad LATAM de esta base: **Brasil tiene capa MCP nacional de datos públicos y educación es el único dominio grande sin servidor.** El pase 35 pidió, con razón, **verificar si hay API antes de prometer plazo**.

🔴 **No hay.** La distribución oficial del **Censo Escolar** es **ZIP con CSV delimitado por `;`**, **~2-4 GB comprimidos y 10-20 GB descomprimidos por año**, en **cuatro dimensiones** (Escolas, Turmas, Matrículas, Docentes), más ASCII con *input files* de SAS y SPSS. **La única API es de terceros** (`inepdadosabertos/api`, **GPL-2.0**, 45 ★), **cubre sólo IDEB** y **su dominio no resuelve**.

🔵 **El contraste con el IBGE es el hallazgo, y es de arquitectura: `ibge-br-mcp` (MIT, 24 versiones) pudo existir como SERVIDOR FACHADA porque el IBGE publica REST** — el MCP traduce *tool call* → HTTP → JSON **y no almacena nada**. **Sin API, un `inep-mcp` tiene que materializar el dato primero**, y eso **traslada al implementador la responsabilidad de alojar y versionar 10-20 GB por año**, con esquema que cambia entre años y una pregunta de privacidad sobre microdato de matrícula que el fachada nunca tiene que responder.

⚠️ **El número, que es lo que hacía falta: 8-12 semanas de pipeline contra 2-3 de fachada** (ver **P77**). **La lección general para cualquier oportunidad de «datos públicos + MCP»: la pregunta que decide el presupuesto no es si el dato es abierto, es si es CONSULTABLE.** Abierto y consultable no son lo mismo, y la diferencia entre los dos es un proyecto entero.

## 🔵 Estado de gaps al cierre del pase 36 del 2026-10-02

**Este pase ejecutó las TRES acciones que el pase 35 dejó escritas, y las tres rindieron.** Ninguna necesitó un host bloqueado — y la que lo habría necesitado (acción 3) **se respondió por otro canal**, que es el método que el pase 35 pidió.

| Gap | Estado | Resolución |
|---|---|---|
| **70** (envoltorio MCP de QTI) | ✅ **CERRADO — el manifiesto está escrito** | **Acción 2 cumplida: las 20 tools de `qti3-cli@0.13.1` con `inputSchema`, comando y `readOnlyHint` están en P76**, medidas en el `.tgz`. 🔴 **Y el cierre corrigió el enunciado del gap: no son 14 tools sino 20** (17 comandos de primer nivel + `certification` con **4** subcomandos), **el `USAGE` documenta sólo 2 de esos 4** (tendencia **117**), y **hay exactamente 2 rutas de escritura en el paquete**, así que **18 de 20 son de lectura**. El contrato de estado adaptativo es **más estrecho** de lo anotado: sólo `outcomes` y `templateValues`, **cualquier otra clave es error duro**, y `--mode static` + `--state` es error de uso |
| **69** (educación ausente de la capa MCP brasileña) | ⚠️ **RECLASIFICADO de «oportunidad» a «oportunidad con arquitectura y plazo conocidos»** | **Acción 3 cumplida y la respuesta es negativa donde importa: INEP NO publica API.** Censo Escolar = **ZIP/CSV, 10-20 GB descomprimidos, 4 dimensiones**; la única API de terceros es **GPL-2.0, sólo IDEB, y su dominio NO RESUELVE** (caída, no bloqueada — control de DNS corrido). 🔵 **Por eso no es un fachada como `ibge-br-mcp`: es pipeline de ingesta, 8-12 semanas contra 2-3** (**P77**, tendencias **123** y **122**). **La oportunidad sigue siendo real y sigue siendo la mejor de LATAM; lo que cambió es que ya no se puede cotizar como si fuera un servidor fachada** |
| **NUEVO 71** (duplicado en `agents/top.md`) | ✅ **CERRADO en el mismo pase que lo encontró** | **`SirhanMacx/Claw-ED` estaba DOS VECES** (59 ★ y 60 ★): el pase 35 lo contó como alta cuando ya había entrado el 2026-09-30. Fila duplicada **eliminada**; el conteo pasa a **51 filas = 49 repos distintos + 2 entradas de PyPI**. 🔵 **La causa es el instrumento, no el descuido: un conteo de FILAS no puede ver una fila repetida** (tendencia **116**). **Control adoptado: contar *slugs* distintos** |
| **NUEVO 72** (las descargas no son instrumento general) | 🔴 **ABIERTO — límite de entorno, con sustituto ya en uso** | **`api.npmjs.org` y `pypistats.org` responden 403 a CONNECT**, así que **las descargas por mes sólo son medibles en Packagist**, y todas las cifras del pase 35 eran de PHP. **El sustituto está adoptado y es mejor para esta tabla: el *span* de releases**, disponible en los tres canales (tendencia **115**). **Se cierra sólo con un host que este entorno no tiene** — no insistir por esta vía |
| **NUEVO 73** (7 de 49 declaran paquete inexistente) | 🔵 **ABIERTO como dato de catálogo, no como falla** | **Siete repos declaran nombre de paquete y el registro devuelve 404**, el mayor con **38,8 k ★** (`project-nomad`). **Su vía de instalación es `git clone`**, lo que cambia el costo de integración y hay que declararlo al cotizar (tendencia **120**). **Acción: anotar el canal de instalación en la tabla, no la ausencia** |
| **65** (primarias multilaterales / legales) | 🔴 **ABIERTO como límite de CLASE — y este pase lo extiende a un segundo dominio nacional** | **Confirmado en `.gov.br` con dos instrumentos** (403 a CONNECT + `EGRESS_BLOCKED` de `WebFetch`) **y con control positivo** (`registry.npmjs.org` → 200). 🟢 **Lo que este pase agrega es método: `getent hosts` separa «bloqueado» de «inexistente»** — `dados.gov.br` **resuelve** (su 403 es política), `api.dadosabertosinep.org` **no resuelve** (está caída). **Se cierra con una lectura hecha fuera de esta red, no con otro intento** (tendencia **122**) |
| **56** (calendario del Anexo III) | ⚠️ **AMPLIADO a dos fechas, y CONFIRMADO en que la de educación es la primera** | 🔵 **Son DOS fechas: 2027-12-02 (Anexo III, autónomo) y 2028-08-02 (Anexo I, embebido en producto regulado)**, *Digital Omnibus on AI*. 🔴 **Y la corrección que este pase se hizo a sí mismo antes de publicar: EDUCACIÓN ES ANEXO III → 2027-12-02.** El Anexo I son **dispositivos médicos, maquinaria y vehículos**; **un LMS no es Anexo I**, así que *«embebido en un LMS»* **no mueve el plazo** (tendencia **121**). **El Anexo III se corrió ~16 meses desde el 2026-08-02 original y se detuvo ahí. Sigue siendo secundaria y por el gap 65 va a seguir siéndolo** |
| **68** (release de la puerta oficial de Open edX) | 🔴 **ABIERTO, sin avance deliberado este pase** | Las tres acciones del pase 35 tenían prioridad. **Re-chequeo sigue siendo una llamada al JSON de PyPI**, y **P61 se sigue cotizando con presupuesto de mantenimiento** |
| **60** (mitad QTI) / **61** (curso origen vacío) | 🔴 **ABIERTOS, sin avance este pase** | La mitad QTI del 60 queda **subsumida por el cierre del 70**: la puerta no existía y **ahora existe su especificación** (P76); falta que alguien la escriba *upstream*. El 61 sigue abierta para el caso **plantilla institucional con estructura y sin contenido** |

## 🔵 Las tres acciones que el pase 36 deja escritas para el pase 37

**Las tres son de ejecución y ninguna depende de un host bloqueado.**

1. 🟢 **Escribir el envoltorio de P76, no volver a medirlo.** El manifiesto de **20 tools** está completo: nombre, comando, `inputSchema`, `readOnlyHint`, el corte de 18/2 y el contrato de estado. **Lo que falta es el código** — `spawn('qti3', […])` + `JSON.parse`, una dependencia nueva (el SDK de MCP), y **la decisión ya tomada de partir `prepare-delivery` en dos tools** para que el `readOnlyHint` no dependa de un argumento. ⚠️ **Pinnear a `0.13.1` y re-leer el `switch`**, porque el paquete publicó **41 releases desde el 2026-05-21** y el último es del **2026-10-01**: la superficie se mueve. **Es la contribución *upstream* más limpia que esta base tiene identificada y ya no le falta diseño.**
2. 🔵 **Aplicar el control de *slug* distinto y el de *backlink* a los OTROS archivos de la KB, que nunca se auditaron así.** Este pase encontró **un duplicado** y **dos colisiones** en `agents/top.md`; **`repos/foundations.md`, `repos/trending.md` y `verticals/solutions.md` tienen tablas con la misma forma y nunca pasaron por ninguno de los dos controles.** **La acción concreta:** extraer los *slugs* de los tres archivos, **contar distintos contra filas** (detecta duplicados) y, para cada fila que cite dato de registro, **verificar el *backlink*** (detecta colisiones). 🔴 **Hay motivo para esperar hallazgos: `foundations.md` es el archivo con más filas de la base y el que más piezas PHP/Packagist cita**, que es justo donde el dato de registro ya está en uso.
3. ⚠️ **Fechar el resto de la tabla por *span*, y anotar el CANAL DE INSTALACIÓN en vez de la ausencia.** Este pase midió las 49 filas de `agents/top.md` y dejó tres clases sin celda útil: **7 que declaran paquete inexistente** (van con *«instalación: `git clone`»*), **22 sin manifiesto** —de las cuales la mayoría son *skills*, donde el registro es la pregunta equivocada (van con *«clase: skill, se copia el directorio»*)— y **1 confirmación débil** (`mentar`, sin `project_urls`). **La acción es de escritura: convertir esas tres clases en una columna explícita de la tabla.** 🔵 **El valor es comercial y concreto: «cómo se instala» es la primera pregunta del integrador, y hoy esta KB la responde en prosa dispersa o no la responde.**

## 🔵 Estado de gaps al cierre del pase 34 del 2026-10-02

| Gap | Estado | Resolución |
|---|---|---|
| **64** (¿los LRS tienen puerta MCP propia?) | ✅ **CERRADO en negativo, con TRES instrumentos** | **Ninguno de los dos la publica.** Docker Hub de `yetanalytics`: **`count: 6`** (`lrsql`, `xapipe`, `datasim`, `persephone`, `fuseki`, `hello-marathon`) — **ninguna MCP**. `lrsql`: **0 menciones de `mcp`** en `deps.edn` y en `README.md` sobre `main`. `ralph-malph` 5.0.1 en PyPI: **ningún `mcp` en `requires_dist`**, **14 extras y ninguno MCP**, **0 menciones** en la descripción. **`DavidLMS/learnmcp-xapi` (MIT, de un tercero) es la única puerta de la capa de telemetría, y ahora está medido.** 🟢 **Regalo del instrumento: los 14 extras de Ralph son el sitio exacto de un `ralph[mcp]` upstream, sin fork** (**P71**) |
| **63** (fecha del `2.0.0` de `learnmcp-xapi`) | 🟡 **PARTIDO: arquitectura CERRADA, fecha RECLASIFICADA** | **Arquitectura cerrada por evidencia de archivo, que es más fuerte que la prosa del README del pase 33:** `config/plugins/lrsql.yaml`, `ralph.yaml` y `veracity.yaml` dan **200 las tres**, y `.env.example` (**200**) declara `LRS_PLUGIN=lrsql  # Options: lrsql, ralph, veracity`, con `timeout: 30` y `retry_attempts: 3` por backend. 🔴 **La fecha NO está bloqueada: no existe.** Se probaron **8 rutas portadoras de versión** (`pyproject.toml`, `uv.lock`, `CHANGELOG.md`, `VERSION`, `setup.py`, `main.py`, `src/__init__.py`, `app/__init__.py`) y **las 8 dan 404**; sólo hay `requirements.txt`, que no declara versión de proyecto. **El proyecto no se versiona en su árbol, así que ningún canal alcanzable puede fechar ese `2.0.0`.** Se cierra la búsqueda en vez de invitar a repetirla |
| **60** (mitad QTI) | ✅ **CERRADO y COTIZADO** | Confirmada en el pase 33 por dos instrumentos; **este pase decide qué hacer con ella.** Ver **P69** y el gap de decisión de abajo |
| **56** (fecha del Anexo III sin fuente primaria) | 🔄 **RECLASIFICADO: de acción pendiente a LÍMITE DE CLASE** | **No es un dominio que falló: es la clase entera.** **0 de 11** dominios multilaterales alcanzables contra **5 de 5** registros comerciales (tendencia **114**). Van **ocho fuentes secundarias concordantes y cero primarias**: Anexo III → **2027-12-02**, art. 50 → **2026-08-02** vigente. 🔵 **Probar otro dominio europeo es previsiblemente inútil; la acción correcta es organizativa — una lectura del consolidado hecha fuera de esta red.** **No se cita como primaria** |
| **51** (CASE por nombre de paquete) | ✅ **CERRADO** (pase 33), sin cambios | Y su método de reemplazo —**el nombre de la organización**— **rindió dos altas en este pase**: `datasim` y la familia `yetanalytics` completa |
| **65** (nuevo) | 🔴 **ABIERTO — y es organizativo, no técnico** | **Esta KB no puede citar ninguna fuente primaria multilateral.** Lo que hace falta, por orden de valor: **(a)** el *working paper* de **UNESCO IESALC** (200 instituciones, 19 países, cinco dimensiones incluida **gobernanza**) — **mejor evidencia de LATAM que todo lo que esta base cita hoy**; **(b)** el texto consolidado del **AI Act** (gap 56); **(c)** el marco del **BID** para LAC. **Las tres requieren una lectura fuera de este entorno de red** |
| **66** (nuevo) | 🔴 **ABIERTO** | **`yetanalytics/persephone` no se puede fichar.** Docker Hub la describe como *«Clojure CLI and server app for validating xAPI Statements against Profiles»* —**exactamente** la capa que este pase buscaba— pero **10 rutas de licencia dan 404** (`LICENSE`, `.md`, `.txt`, `license`, `COPYING` × `main`/`master`), `project.clj` y `deps.edn` **404**, `README.md` **404** en las dos ramas, y Docker **parado en 2023-10-10 (3 tags)**. **Sin licencia leída no entra a ninguna tabla.** Su árbol puede vivir en una rama con otro nombre, y **eso sólo se contesta con un listado de repositorio** — que es lo que `api.github.com` (**403**) no permite acá |
| **67** (nuevo) | 🔴 **ABIERTO** | **¿Cuántas de las 48 filas de `agents/top.md` son servicios alojados con licencia de metadatos?** La colisión 9 (`quizlar/mcp-server`) se detectó **porque era un candidato nuevo y se le abrió el `server.json`**. 🔴 **Las filas que entraron antes de que existiera el esquema de registro MCP (2025-12-11) nunca pasaron ese control.** El chequeo es de un campo y la población es de 48: **es la auditoría más barata y de mayor rendimiento que le queda a esta base** |
| **62** (`tools/list` de `coursecode` sin ejecutar) | 🔴 **ABIERTO**, sin cambios | Instalar dependencias de terceros sigue **sin permiso de ejecución** en este entorno. No se tocó |
| **61** (origen vacío en `course_rerun_task`) | 🔴 **ABIERTO**, sin cambios | No se tocó en este pase |

## 🔵 Las tres acciones que el pase 34 deja escritas para el pase 35

**Las tres salen del mismo hallazgo —que el registro miente en las dos direcciones— y las tres son de verificación, no
de descubrimiento. Ninguna necesita permiso de ejecución ni un dominio nuevo.**

1. 🔴 **Auditar las 48 filas de `agents/top.md` contra el campo `remotes`** (**gap 69**). **Es la acción de mayor
   rendimiento de las tres y la más barata.** Este pase descartó un candidato por un campo de un archivo; **las filas
   viejas nunca pasaron ese control porque el esquema de registro MCP es del 2025-12-11**, posterior a buena parte de
   ellas. La acción concreta: para cada fila cuyo nombre contenga `mcp` o que esta KB describa como *«servidor MCP»*,
   pedir `server.json` y `package.json` por `raw.githubusercontent.com` y **verificar que exista fuente o paquete, no
   sólo `LICENSE`**. Es el mismo gesto que la acción 1 del pase 33 —auditar lo publicado en vez de buscar más— y ése
   rindió el hallazgo central de dos pases seguidos.
2. **Cerrar el `ralph[mcp]` como propuesta concreta, que es la contribución *upstream* mejor ubicada de esta base**
   (**P71**). Ralph es **MIT**, su `LICENSE` nombra a **France Université Numérique** —el mejor argumento institucional
   para EMEA— y declara **14 extras**, o sea **una convención de plugins ya empaquetada donde un `mcp` encaja sin
   fork**. Concretamente: leer `pyproject.toml` de Ralph por `raw.githubusercontent.com` para ver **cómo se declara un
   extra y cómo se registra el `cli`**, y escribir el alcance de tres tools equivalentes a las de `learnmcp-xapi`
   (1 escribe, 2 leen) **con el techo de caudal del pase 34 como default** (tendencia **109**). ⚠️ **Y verificar antes
   lo que este pase no pudo: Ralph está vivo en `main` y parado en PyPI desde 2024-07-11, así que la propuesta se hace
   contra `main`, no contra el release.**
3. **Fichar `datasim` de verdad, que es el alta de este pase y entró con licencia pero sin superficie medida.** Está
   verificada como **Apache-2.0** y como *«genera xAPI a escala y valida contra xAPI Profile»*, pero **no se midió qué
   expone**: leer `deps.edn` (**200**) y el `README` completo para establecer **(a)** si tiene CLI, servidor HTTP o las
   dos; **(b)** si consume un **xAPI Profile** como entrada —lo que lo volvería la herramienta de conformidad que el
   pase 25 buscó sin encontrar—; y **(c)** si puede apuntar a un LRS externo o sólo genera archivos. 🔵 **De eso
   depende que P71 cotice «probamos la telemetría antes de firmar» como una tarea de horas o de semanas**, y es la
   única pieza de esta KB que contesta con una medición la barrera regional de APAC (**49 % sin infraestructura de
   tiempo real**).

## 🔵 Estado de gaps al cierre del pase 33 del 2026-10-02

| Gap | Estado | Resolución |
|---|---|---|
| **60** (¿QTI y xAPI/LRS sin puerta MCP?) | 🔴 **PARTIDO: mitad FALSA, mitad CONFIRMADA** | **xAPI/LRS: falsa.** `DavidLMS/learnmcp-xapi` (**MIT**, 3 tools: 1 escribe, 2 leen) es la puerta, y **estaba en esta KB desde el pase 6** (`agents/top.md` fila + mapa por estándar con *«desde el pase 6»* escrito, `repos/foundations.md`, 15+ patrones). **QTI: confirmada** por segundo instrumento independiente. Causa de la falla: la lista de candidatos venía del registro de paquetes y `learnmcp-xapi` **no está en ninguno** (PyPI 404, npm 0) — tendencias **99** y **101** |
| **51** (CASE por nombre desambiguado) | ✅ **CERRADO en negativo** | **No es resoluble por nombre de paquete, y ahora está medido en tres registros.** `opencase`: npm 7 / PyPI 404 / Packagist 665, **cero del dominio**. `cass`: Packagist **26.726**. El instrumento de reemplazo es el **nombre de la organización** (`LongsightGroup`, `oat-sa`, `yetanalytics`, `openfun`) — tendencia **100** |
| **56** (calendario del Anexo III) | ⚠️ **ACCIÓN EJECUTADA, resultado negativo — sigue sin fuente primaria** | **Los dos dominios que el pase 32 mandó probar están bloqueados:** `eur-lex.europa.eu` y `data.europa.eu` devuelven **`EGRESS_BLOCKED`**. La fecha suma dos fuentes secundarias más (**siete concordantes, cero primarias**): Anexo III → **2027-12-02**; art. 50 → **2026-08-02**, vigente. 🔴 **No citar como primaria.** Para cerrarlo hace falta **una lectura hecha fuera de este entorno de red** |
| **62** (nuevo) | 🔴 **ABIERTO** | **`tools/list` de `coursecode` no se ejecutó por protocolo.** Instalar dependencias de terceros está **bloqueado en este entorno**. Las cifras **15 definidas / 15 dispatch / 2 escrituras** son **lectura del artefacto publicado**, no respuesta del servidor. La coincidencia 15 = 15 hace improbable el aliasing pero no lo descarta — que es justo la distinción que el pase 30 estableció con `oneroster-ts` |
| **63** (nuevo) | 🔴 **ABIERTO** | **La arquitectura de plugins de `learnmcp-xapi` está leída; su fecha no.** El README documenta `LRS_PLUGIN=lrsql\|ralph\|veracity` + `config/plugins/*.yaml`, lo que **no estaba** en la ficha del pase 6. Fuentes secundarias mencionan un **`2.0.0`** con *«complete redesign with a modular LRS plugin system»* — **sin verificar**: `github.com/releases` da **403** y no hay `pyproject.toml` en la raíz de `main` (404). **Si el `2.0.0` es real, el «no se movió» del pase 25 está vencido** |
| **61** (origen vacío en `course_rerun_task`) | 🔴 **ABIERTO**, sin cambios | No se tocó en este pase |
| **64** (nuevo) | 🔴 **ABIERTO** | **¿`lrsql` o Ralph tienen puerta MCP propia?** Este pase midió que **`learnmcp-xapi` es la puerta de terceros**, pero no preguntó por la del proyecto — que es exactamente el canal donde el pase 30 encontró `openedx-mcp` (oficial, en PyPI, dos meses antes de que esta KB lo notara). **`lrsql` se distribuye por Docker Hub**: la pregunta correcta es si publica una imagen o un módulo con MCP |

## 🔵 Las tres acciones que el pase 33 deja escritas para el pase 34

**Las tres salen del mismo hallazgo —el sesgo del instrumento— y las tres son baratas. Ninguna necesita permiso de
ejecución, que es la restricción que bloqueó media acción de este pase.**

1. 🔴 **Auditar las ausencias declaradas de esta KB contra la propia KB, y después contra un segundo instrumento**
   (**tendencia 101**). Este pase descubrió que el **gap 60** contradecía cuatro archivos de esta base. **No hay razón
   para suponer que es el único.** La acción concreta: listar **todas** las frases de tipo *«no existe»*, *«nada»*,
   *«ausencia medida»* del mapa por estándar de `agents/top.md` —**CASE, CEASN, Open Badges del estándar, Caliper**— y
   para cada una (a) hacer `grep` del término en los ocho archivos, y (b) re-preguntar **por búsqueda abierta**, que es
   el instrumento que destapó la mitad xAPI. **Es la acción de mayor valor de las tres**, porque cada ausencia falsa que
   siga publicada es una pieza que Globant ya podría estar usando y no usa.
2. **Preguntar por la puerta MCP *del proyecto*, no de terceros, en los dos LRS** (**gap 70**). Es el mismo gesto que
   rindió `openedx-mcp` en el pase 30, y nunca se hizo para la capa de telemetría. Concretamente: buscar en
   `hub.docker.com` las imágenes de `yetanalytics`, abrir `raw.githubusercontent.com/yetanalytics/lrsql/main` buscando
   `mcp` en el árbol de módulos, y lo mismo para `openfun/ralph` —que **sí** está en PyPI, así que ahí el registro **es**
   el instrumento correcto—. **Y de paso cerrar el gap 63**: fechar el `2.0.0` de `learnmcp-xapi` por un canal que no sea
   `github.com` (el `uv.lock` o el `__init__.py` del paquete sirven, y `raw.githubusercontent.com` responde 200).
3. **Medir el stack PHP de QTI, que es la mitad del gap 60 que se sostiene y la única capa de evaluación con escala
   real.** Packagist devolvió **36 paquetes** y el ecosistema está dominado por **`qtism/qtism` (OAT QTI-SDK)** y
   **`oat-sa/extension-tao-*`**. La pregunta que decide **P72**: ¿la contribución *upstream* conviene sobre
   `@longsightgroup/qti3-cli` —**MIT, cero dependencias de terceros, un wrapper MCP agrega una sola**— o sobre el stack
   PHP, que tiene **más adopción y más paquetes**? Leer la licencia y la cadencia de `qtism/qtism` por Packagist y
   `raw.githubusercontent.com`, y **decidir con el número de adopción al lado**, no por preferencia de lenguaje.
## 🔵 Estado de gaps al cierre del pase 35 del 2026-10-02

⚠️ **Nota de concurrencia, y conviene que quede asentada:** el **pase 33** se publicó mientras este pase estaba en curso,
así que **las dos corridas midieron en paralelo y sin verse.** Donde coinciden —el bloqueo de `eur-lex` y `data.europa.eu`,
el cierre en negativo del **gap 51**, la imposibilidad de ejecutar `tools/list` en este entorno— **la coincidencia vale como
confirmación independiente**. Donde no, se resuelve acá y se dice cuál gana. 🔴 **Los gaps 62, 63 y 64 de esta tabla son los
del pase 33** (`coursecode` sin `tools/list`, la fecha de `learnmcp-xapi`, y la puerta MCP propia de los LRS);
**los nuevos de este pase son 65, 66, 67 y 68.**

| Gap | Estado | Resolución |
|---|---|---|
| **56** (calendario del Anexo III) | ⚠️ **RESUELTO a nivel de inciso, no de fuente primaria** | 🔵 **Sube de fecha a disposición: el Artículo 113 difiere el Capítulo III, Secciones 1, 2 y 3 —excepto el Artículo 6(5)— al 2027-12-02 para los sistemas del Artículo 6(2) y Anexo III.** Cadena: **Reglamento (UE) 2026/1744**, DOUE **2026-07-24**, en vigor **2026-07-27**, modifica el 2024/1689. El **2026-08-02** es la aplicación general (transparencia, art. 50) y **ya la aplican** el AI Office y las autoridades nacionales. 🔴 **Sigue siendo secundario — y por el gap 65 va a seguir siéndolo** |
| **65** (del pase 34) | 🔴 **ABIERTO — y este pase le agrega la evidencia europea medida** | ⚠️ **No es un gap nuevo: es el mismo del pase 34 («esta KB no puede citar ninguna fuente primaria multilateral»), y esta corrida lo confirma por su cuenta en el caso que más riesgo comercial tiene.** **El dominio de la publicación legal europea es inalcanzable desde este entorno.** Medido en el registro del proxy: `eur-lex.europa.eu` y `data.europa.eu` responden **403 a CONNECT**; también caen `artificialintelligenceact.eu`, `op.europa.eu`, `euaiact.com`, `euai-act.com`, `nicfab.eu`, `cypheron.cz`, `modulos.ai`. 🔴 **Deja de ser una acción pendiente: ningún pase lo va a cerrar por este camino.** Se cierra con el PDF del DOUE traído por una persona |
| **68** (nuevo) | 🔴 **ABIERTO — riesgo de dependencia** | **La puerta oficial de Open edX publicó 12 releases en dos días (2026-07-24/25) y nada en los 70 siguientes, todavía en `0.1.x`.** Nada de lo medido se invalida (35 rutas, 19 escrituras, los cuatro rails); lo que cambia es que **P61 se cotiza con presupuesto de mantenimiento**. Re-chequeo: una llamada al JSON de PyPI |
| **69** (nuevo) | 🔴 **ABIERTO — y es la mejor oportunidad LATAM de esta base** | **Brasil tiene capa MCP nacional de datos públicos —IBGE/censo (MIT, 24 versiones), Banco Central, DATASUS SIH/SUS, firma electrónica— y educación es el único dominio grande sin servidor.** `inep` → 3 resultados sin MCP; `censo-escolar` → 18, todos colisión; `enem` → 6, el más nuevo de 2024. ⚠️ **Ausencia medida en el canal (npm/PyPI), no en el mundo.** Ver **P72** |
| **70** (nuevo, reemplaza la mitad QTI del 60) | 🔴 **ABIERTO y ahora medido** | **`@longsightgroup/qti3-cli` 0.13.1 (MIT): 14 comandos, CERO dependencias de terceros, TODOS emiten JSON** → mapeo comando→tool 1:1, **12 de lectura y 2 de escritura a disco**. ⚠️ **La advertencia de cotización: `prepare-delivery` en modo `server-materialized-adaptive` EXIGE un objeto de estado con `outcomes` — lo adaptativo es un contrato de estado del lado servidor, no un flag.** Ver **P72** |
| **60** (mitad QTI) | 🔴 **La mitad QTI sigue ABIERTA, y este pase la confirma por un segundo instrumento** | ⚠️ **Y se acepta la corrección del pase 33 sobre la otra mitad: la de xAPI era FALSA** — `DavidLMS/learnmcp-xapi` (**MIT**) es la puerta y estaba en esta KB desde el pase 6. **Lo que este pase mide es una afirmación más angosta y compatible: las seis piezas de MAYOR DESPLIEGUE de las dos capas no tienen MCP** —`oat-sa/qti-sdk`, `oat-sa/extension-tao-testqti`, `php-xapi/client`, `TinCanPHP`, `TinCanPython` y `cass-npm`, cero menciones en README crudo—, lo cual **no es lo mismo que «la capa no tiene puerta»**. 🔵 **El dato nuevo que sí es nuevo: el SDK npm de CaSS tampoco expone MCP** — la puerta de CaSS es sólo del servidor (tendencia **112**) |
| **51** (CASE por nombre desambiguado) | ✅ **CERRADO en negativo — y las dos mediciones de hoy coinciden** | ⚠️ **El pase 33 lo cerró y este pase llegó al mismo resultado por su cuenta, que es la mejor confirmación que puede tener un cierre.** El pase 32 descartó el **nombre del estándar**; este pase descartó el **nombre del implementador**: `OpenCASE` falla en los tres registros (🔴 **colisión 7: OpenCage**, geocodificación) y `cass` devuelve **26.726 objetos** de ruido en Packagist (🔴 **colisión 8: Apache Cassandra**). 🔵 **La regla que queda: lo único que desambigua siempre es el *scope* o el prefijo de organización** (`cassproject`, `@longsightgroup/*`), no el nombre del proyecto |
| **61** (curso origen vacío en `course_rerun`) | 🔴 **ABIERTO, sin avance este pase** | Sigue abierta para el caso **plantilla institucional con estructura y sin contenido**. El gap 57 la volvió innecesaria para el *bootstrap* |

## 🔵 Las tres acciones que el pase 35 deja escritas para el pase 36

**Las tres son de ejecución y ninguna necesita un host que este entorno tenga bloqueado.**

1. 🔵 **Aplicar el instrumento nuevo —descargas por mes y fecha del último release— a TODA la tabla de `agents/top.md`,
   no a seis piezas.** Este pase lo aplicó a las que el barrido trajo de la mano y **tres de seis cambiaron de lectura**;
   la tabla tiene **52 filas** y la mayoría nunca se midió por despliegue. **Concretamente:** para cada fila con paquete
   publicado, pedir `packagist.org/packages/<v>/<p>.json` → `downloads.monthly`, o `pypi.org/pypi/<p>/json` y
   `registry.npmjs.org/<p>` → fecha del último release, y **anotar la distancia entre el primer y el último release**.
   **Lo que hay que buscar son las dos puntas:** filas con muchas estrellas y cero tracción (se bajan o se marcan), y
   filas con pocas estrellas y tracción real (se suben). **Es la medición más barata y de mayor rendimiento que tiene
   esta base pendiente**, y ya tiene método probado.
2. **Cerrar el gap 64 escribiendo el envoltorio, no midiéndolo otra vez.** `qti3-cli` tiene **14 comandos que ya emiten
   JSON y cero dependencias**: el envoltorio MCP es **una tabla de 14 entradas** (nombre, `inputSchema`, comando,
   `readOnlyHint`). **La acción concreta es producir ese manifiesto de tools como artefacto de esta KB** —no el código,
   el manifiesto— con el corte de lectura/escritura ya decidido y el contrato de estado de
   `prepare-delivery --mode server-materialized-adaptive` documentado. **Eso convierte P67 de «se puede» en «acá está
   la especificación», que es lo que un cliente compra**, y es además la contribución *upstream* más limpia que esta base
   tiene identificada.
3. 🔵 **Medir el otro extremo del gap 63: ¿los datos existen en la forma que un MCP necesita?** El gap dice que **no hay
   servidor** para INEP, Censo Escolar y ENEM; **no dice si hay API.** `ibge-br-mcp` pudo existir porque el IBGE publica
   API REST. **La acción: verificar si INEP y el portal de dados abertos del gobierno brasileño exponen API o solamente
   descargas de CSV**, porque de eso depende si **P69** es un servidor fachada de semanas o un pipeline de ingesta de
   meses. **Y es la pregunta que decide si la oportunidad es real o es una línea de presupuesto escondida.** ⚠️ Probar
   `dados.gov.br` y `servicodados.ibge.gov.br` **antes** de prometer plazo — y si están bloqueados, declararlo como se
   declaró el gap 65 en vez de dejarlo implícito.

## 🔵 Estado de gaps al cierre del pase 32 del 2026-10-02

| Gap | Estado | Resolución |
|---|---|---|
| **57** (`course_rerun` como bootstrap de P63) | ✅ **CERRADO** | **Y sin objeto: no hace falta plantilla.** `create_new_course` vive en el mismo `POST course_handler`, basta **omitir `source_course_key`**. Devuelve `course_key`/`destination_course_key` **sincrónicamente**; el copiado va a **Celery** (`rerun_course_task.delay`) y se sigue por **`CourseRerunState`** (`FAILED`/`SUCCEEDED`). Permiso: **`is_content_creator(user, org)`**, no `GlobalStaff`. 🔴 Trampa: `rerun_course` lee `fields['display_name']` sin guarda (**:1359**) → **omitirlo en un rerun levanta `KeyError`** |
| **59** (¿el `sync` resuelve conflicto?) | ✅ **CERRADO** | **Preserva por omisión** (`override_customizations` = `False`; `keep_custom_fields` para granularidad). `downstreams/` tiene **cuatro** escrituras: `POST .../sync` (aceptar), `DELETE .../sync` (**rechazar**, `decline_sync` → 204), `PUT` (fijar vínculo), `DELETE` (cortar vínculo). ⚠️ Las cuatro clases están rotuladas **`[ 🛑 UNSTABLE ]`** |
| **56** (calendario del Anexo III) | ✅ **RESUELTO** ⚠️ no primario | Educación es **Anexo III** → **2027-12-02** (movida desde 2026-08-02 por el **Digital Omnibus on AI**, en vigor 2026-07-27). El **2026-08-02** es la **aplicación general** (transparencia, art. 50) y **sigue vigente**. Art. 6(1) embebido → **2028-08-02**. ⚠️ **Cinco fuentes secundarias concordantes; el texto primario quedó bloqueado por el proxy de egreso.** No citar como primario |
| **51** (CASE por nombre desambiguado) | 🔴 **ABIERTO**, con un método descartado | `registry.npmjs.org` hace **OR** sobre texto libre: `"competencies and academic standards exchange"` devuelve **1.696.870** objetos de ruido. **El registro de paquetes no desambigua estándares de nombre multi-palabra.** Atacarlo por el **nombre del proyecto implementador** (`OpenCASE`, `CASS`), no del estándar |
| **60** (nuevo) | 🔴 **ABIERTO** | **QTI y xAPI/LRS no tienen puerta MCP** — medido abriendo los README de los candidatos de las dos capas. La **tendencia 89** valió para OneRoster y Open Badges y **no vale para evaluación ni telemetría**: la única puerta de estándar nueva es la de **empaquetado** (`coursecode`). Es la **oportunidad de contribución *upstream* más limpia** que tiene esta base: `qti3-core` no tiene dependencias y ya expone parser, validación y *scoring* |
| **61** (nuevo) | 🔴 **ABIERTO** | ¿`course_rerun_task` admite un curso **origen vacío**? El gap 57 volvió la pregunta innecesaria para el *bootstrap* (se usa `create_new_course`), pero sigue abierta para el caso **plantilla institucional con estructura y sin contenido**, que es un pedido real en despliegues grandes |

## 🔵 Las tres acciones que el pase 32 deja escritas para el pase 33

1. 🔴 **Cerrar el gap 56 contra el texto primario, y es la única acción no técnica de las tres.** Este pase lo resolvió
   con **cinco fuentes secundarias concordantes** y dejó escrito que **no es verificación primaria**, porque
   `artificialintelligenceact.eu`, `digital-strategy.ec.europa.eu` y el análisis de Gibson Dunn están **bloqueados por el
   proxy de egreso**. **Probar `eur-lex.europa.eu` y `data.europa.eu`**, que no se intentaron, y fechar **cada
   afirmación contra el inciso del Anexo III** que le corresponde. **Sobre esta fecha se construye el pitch de EMEA**: es
   el único número de esta KB que un abogado del cliente va a verificar en la primera reunión.
2. **Levantar `coursecode` y pedirle `tools/list`** — es el mismo gesto que el pase 30 hizo con `oneroster-ts` y el que
   convirtió «35 rutas documentadas» en «132 tools servidas». Hay que responder **cuántas tools expone realmente** su
   servidor MCP y **si alguna escribe** (genera paquete SCORM/cmi5) o si todas leen. **Decide si `coursecode` es la pieza
   de salida de la capa generativa de esta KB** (el rol que hoy ocupa `scorm-mcp-server` con 3 tools) o sólo un CLI con
   fachada MCP. Y de paso: **medir si `qti3-cli` es envolvible como MCP en días**, que es lo que el **gap 60** afirma sin
   haberlo probado.
3. **Repetir la consigna del registro de paquetes, pero por el nombre del proyecto implementador** — que es el método que
   este pase descartó por escrito para el nombre del estándar (**gap 51**). Concretamente: consultar npm, PyPI y
   Packagist por **`OpenCASE`**, **`CASS`**, **`learning_locker`**, **`TinCanPython`** y **`qti3`**, abrir el README de
   cada resultado y buscar «MCP» adentro. **Y aplicarle a cada hallazgo el control de la tendencia 96 antes de
   promoverlo:** contar menciones del vocabulario del dominio, porque este pase demostró que **MIT + activo + «agéntico»
   no garantiza que la pieza sea del dominio educativo.**
## 🔵 Las tres acciones que el pase 31 deja escritas para el pase 32

1. 🔴 **Medir `course_rerun` y cerrar el gap 57**, que es lo único que separa a **P63** de una cotización sin asterisco.
   Concretamente: leer `CourseRerunView` en
   `cms/djangoapps/contentstore/rest_api/v1/views/` por `raw.githubusercontent.com` y responder **tres** cosas:
   (a) ¿acepta como origen un curso **vacío** usado de plantilla, o exige contenido?; (b) ¿qué devuelve —el nuevo
   `course_key` sincrónicamente, o una tarea asíncrona que hay que *pollear*?; (c) ¿qué permisos pide? **Es la acción de
   mayor valor comercial pendiente**, porque decide si el *onboarding* de un curso nuevo en un proyecto Open edX es una
   línea de API o una intervención manual — y Open edX es la huella pública grande de **LATAM e India**.
2. **Cerrar el gap 59 leyendo el mismo árbol: ¿`SyncFromUpstreamView` resuelve conflicto?** Leer
   `v2/views/downstreams.py` y responder qué pasa cuando el bloque *downstream* fue editado localmente y llega un `sync`
   (¿sobrescribe, rechaza, marca conflicto?). **De eso depende si la propagación de la tendencia 91 es segura para
   contenido que el docente toca**, que es el caso real en cualquier despliegue. Y de paso contar si `downstreams/`
   tiene escritura además de `sync`.
3. **Repetir la consigna del registro de paquetes sobre los estándares que quedaron sin segunda vuelta** (tendencia 89).
   El pase 31 probó que **donde hay una puerta MCP suele haber varias**: se hizo OneRoster (apareció una MIT nueva),
   LTI (vacío medido) y Open Badges (apareció OB 3.0 permisivo). **Faltan: QTI** —medido por tres métodos en el pase 28,
   nunca re-preguntado al registro—, **xAPI/LRS**, **CASE por nombre desambiguado**
   (`"Competencies and Academic Standards Exchange"`, **gap 51**, cuarta colisión de término de esta KB, todavía
   abierta) y **SCORM**. Método que funciona: `registry.npmjs.org/-/v1/search?text=<estándar>` y
   `pypi.org/pypi/<pkg>/json`, **abrir el README y buscar «MCP» adentro**, y verificar el repo por
   `raw.githubusercontent.com` **sabiendo que el 404 del repo no invalida el paquete** (tendencia 94).


## 124. La actividad de bot no es mantenimiento, y un barrido que tome el ref más nuevo declara vivos a los proyectos muertos (agregado en el pase 37 del 2026-10-02)

**El instrumento de vitalidad de este pase —`git ls-remote` + `fetch --depth 1` del sha de `HEAD`— tenía una trampa, y se
encontró antes de publicar el número.** `trilogy-group/oneroster-ts` tiene **6 ramas y la más reciente es del 2026-05-11**:
a cuatro meses, parecería tibio. Su rama por defecto está en el **2025-06-27**: **quince meses**. La diferencia son
**cuatro ramas `dependabot/npm_and_yarn/*` y una `speakeasy-sdk-regen-1746144633`, ninguna mergeada.**

El mismo patrón en `satvik314/educhain`: `main` en el **2025-12-03**, y el tip más nuevo del repo (**2026-05-29**) es una
rama **`claude/relaxed-curie-mNW2l`** — generada por un agente, sin mergear.

🔵 **La regla, y vale para cualquier medición de vitalidad de esta base: se fecha el tip de la RAMA POR DEFECTO, nunca el
ref más nuevo.** Dependabot, los regeneradores de SDK y las ramas de agente mantienen vivo el grafo de refs de un proyecto
que nadie atiende. **En `oneroster-ts` lo único que se movió en quince meses lo escribió una máquina y nadie lo revisó.**

⚠️ **Por qué importa comercialmente:** un *due diligence* de dependencias hecho con la pregunta *«¿hay actividad
reciente?»* aprueba estos dos repos. La pregunta correcta es *«¿hay un humano mergeando en la rama principal?»*. Ver el
**gap 72**.

## 125. El registro puede declarar «abandonado» un proyecto activo, y el único canal que no se equivoca es el árbol de git (agregado en el pase 37 del 2026-10-02)

**Esta base ya había visto el caso una vez y lo había escrito como anécdota. Ahora es verificable, y el pase anterior se
equivocó justamente por no tener con qué verificarlo.**

El pase 33 anotó sobre **Ralph** (MIT): *«vivo en `main` y parado en el registro — último release 2024-07-11, `[Unreleased]`
activo → se instala desde git, no desde PyPI»*. El pase 36, midiendo con el único instrumento que tenía —el registro—,
escribió sobre `pykt-team/pykt-toolkit`: *«🔴 2022-10-16. **Cuatro años.** *Backlink* verificado: **es abandono, no
colisión**»*, y lo etiquetó así en las propuestas de *knowledge tracing*.

| Canal | `pykt-toolkit` |
|---|---|
| PyPI | último release **2022-10-16** |
| Tags de git (los 5, fechados) | `v0.0.34-alpha` 2022-06-09 → **`v1.0.0` 2023-02-10** |
| 🟢 **`HEAD` de la rama por defecto** | 🟢 **2026-09-22** — `Merge pull request #305`, `feat: add cgmkt model`, `feat: add cgmkt sweep config` |

🟢 **Está vivo, y con *feature commits*, no con mantenimiento cosmético.** La afirmación «cuatro años de abandono» era
falsa y la pieza entraba a propuestas con esa etiqueta.

🔵 **La regla que esto deja, y es la jerarquía de instrumentos completa de esta base:**

| Instrumento | Qué mide | Dónde falla |
|---|---|---|
| ★ estrellas | interés acumulado | `learninglocker`: 583 ★ / 0 descargas |
| descargas/mes | base instalada | `TinCanPHP`: 6.178/mes, sin publicar desde 2022 |
| *span* de releases | cadencia de publicación | **no existe para las 17 filas con cero tags** |
| 🟢 **commit de `HEAD`** | 🟢 **si alguien escribe código** | el «último tag» por orden de versión (ver **gap 73**) |

**Los cuatro miden cosas distintas y ninguno sustituye a los otros. Para decidir si una dependencia entra en una propuesta,
el que manda es el cuarto.**

## 126. La API de GitHub responde 200 y niega el acceso en el CUERPO: un probe que mire el código HTTP escribe datos vacíos creyendo que funcionó (agregado en el pase 37 del 2026-10-02)

**Esta familia de KBs venía anotando *«github-api-proxy-blocked»*. Medido: es falso, y la verdad es peor.**

- `api.github.com/rate_limit` → **`200`**, con `"limit": 15000, "remaining": 15000`. **Parece plenamente disponible.**
- `api.github.com/repos/<cualquier-repo-no-adjunto>` → **`200` en la capa HTTP**, y en el cuerpo:
  `"message": "GitHub access to this repository is not enabled for this session"`.

🔴 **No es un bloqueo de red: es una compuerta de alcance, y devuelve el error en el cuerpo y no en el código de estado.**
La API sólo contesta por los repositorios adjuntos a la sesión.

⚠️ **El riesgo es de método y es grande, porque todos los probes de esta base miden `%{http_code}`.** Un barrido así sobre
las 49 filas habría registrado «200, funciona» y escrito **49 filas de campos vacíos** —sin estrellas, sin licencia, sin
fecha— con apariencia de medición. 🔵 **La regla: cuando un endpoint devuelve JSON, el control de disponibilidad se hace
sobre un CAMPO ESPERADO del cuerpo, no sobre el código de estado.** Y el reemplazo sin cuota ni autenticación es
`git ls-remote`, que **no tiene compuerta de alcance** y funcionó en las 49. Ver el **gap 74**.

## 127. El registro de paquetes sirve para CONFIRMAR un nombre, no para DESCUBRIRLO — y hay dos límites medidos que lo explican (agregado en el pase 37 del 2026-10-02)

**El pase 35 introdujo el barrido por registro y rindió poco fuera de Packagist. El pase 36 lo atribuyó a que las descargas
sólo existen en Packagist. Hay una segunda causa, y es del buscador.**

- 🔴 **Las consultas de varias palabras se resuelven como OR y se ordenan por descargas.** `xapi mcp` → **110.769**
  resultados, encabezados por `@modelcontextprotocol/sdk`, `@storybook/addon-mcp` y `@upstash/context7-mcp`. **El paquete
  del dominio queda sepultado bajo la infraestructura genérica**, que es la misma dinámica que la tendencia 23 describe
  para las estrellas, aplicada al ranking del registro.
- 🔴 **El calificador `scope:` no está soportado por `/-/v1/search`.** `text=scope:pie-element` → **2.403.867** resultados,
  y la primera página son `locate-path`, `strip-ansi`, `@types/node`. **Hay que pedir el paquete por nombre exacto**
  (`registry.npmjs.org/@pie-element/rubric`), que **sí** funciona y devuelve licencia, versión y fechas.

🔵 **La regla, que consolida la del pase 33 (tendencia 112):** los nombres se descubren por **organización**, por **README
crudo** o por el **árbol de refs**; el registro se consulta **después**, con el nombre ya en la mano, para fechar y para
leer la licencia. **Un barrido que arme candidatos desde el buscador del registro no puede encontrar software de dominio
en una industria cuyo término está capturado** — que es exactamente lo que le pasa a `education` en GitHub desde el pase 23.

## 128. La capa de evaluación permisiva existe y tiene siete años, pero no es conforme al estándar: el trade-off es de tres patas y ninguna domina (agregado en el pase 37 del 2026-10-02)

**El pase 36 cerró P69 con una frase que resultó medio falsa:** *«lo activo y desplegado de la capa de evaluación es
copyleft, y lo permisivo es lo nuevo»*. 🟢 **La segunda mitad se refuta:** `pie-framework/pie-elements` es **ISC**, tiene
**2.226 versiones publicadas desde 2019**, su `HEAD` es del **2026-09-22** y publicó paquetes **el 2026-10-01**. **Siete
años, permisivo y activo.**

⚠️ **Y la refutación trae su propio límite: no implementa QTI** —cero menciones en el README crudo—, tiene su propio modelo
de ítem y su propio contrato de *scoring*. **Por la tendencia 29 de esta base —medida en cinco capas— eso lo pone del lado
que no escala.**

| Opción | Licencia | Madurez | Conforme | Cuándo gana |
|---|---|---|---|---|
| `pie-elements` | 🟢 **ISC** | 🟢 7 años / 2.226 versiones | 🔴 **modelo propio** | Banco propio, sin intercambio con terceros |
| `@longsightgroup/qti3-cli` + `qti3-item-player` | 🟢 **MIT** | ⚠️ nuevo (2026-05-21) | 🟢 **QTI 3** | Hay import/export, o el pliego pide QTI |
| `qtism/qtism` + TAO | 🔴 **GPL-2.0-only** | 🟢 el más desplegado del mundo | 🟢 QTI 2.x | El cliente ya corre TAO |

🔵 **La lectura que hay que llevar a una reunión: en evaluación no hay una recomendación, hay tres, y la que corresponde la
decide el pliego y lo que el cliente ya tiene instalado — no la licencia sola.** Es la primera capa de esta KB donde
**licencia, madurez y conformidad no coinciden en ninguna pieza.**

## 129. El archivo `LICENSE` le gana al MANIFIESTO, y el manifiesto es lo que leen los escáneres automáticos (agregado en el pase 37 del 2026-10-02)

**El pase 10 de esta base estableció: «verificar contra el archivo `LICENSE`, no contra el README». Este pase lo endurece,
porque encontró el caso donde los dos canales formales se contradicen entre sí.**

En `pie-framework/pie-elements`:

| Canal | Qué declara |
|---|---|
| `LICENSE.md` de la rama por defecto | **cuerpo del texto ISC**, `Copyright 2019 CoreSpring Inc` |
| `package.json` de la raíz | 🔴 **`"license": "MIT"`** |
| Paquetes publicados (`rubric`, `graphing`, `math-inline`, `drawing-response`, `extended-text-entry`) | **`ISC`** |
| 🔴 **`@pie-element/multiple-choice` v13.4.4** | 🔴 **no declara licencia** |

🔵 **Tres identificadores, dos respuestas y uno vacío — y el vacío está en la interacción más central de cualquier
evaluación.** Un *due diligence* devuelve **MIT** si entra por la raíz, **ISC** si entra por los paquetes publicados, y
**nada** si entra por `multiple-choice`.

⚠️ **El desenlace de este caso concreto es benigno —ISC y MIT son las dos permisivas y las dos sirven— y por eso sirve como
ejercicio:** la próxima vez la contradicción puede ser entre una permisiva y una copyleft, y entonces decide el proyecto.
**La jerarquía queda: archivo `LICENSE` del repo > manifiesto del paquete publicado > manifiesto de la raíz > README.**

🟢 **ISC entra además como licencia nueva de esta KB** — la tercera «permisiva que los filtros de licencia descartan por
desconocida» después de **ECL-2.0** (tendencia 27) y **0BSD** (pase 28). **Es funcionalmente equivalente a MIT** y hay que
tenerla en la lista blanca. Ver el **gap 76**.

## 130. El bloqueo institucional del gap 65 es del canal de *fetch*, no del canal de información: el buscador devuelve lo que `curl` no alcanza (agregado en el pase 37 del 2026-10-02)

**El gap 65 (pase 34) estableció que las fuentes primarias multilaterales son inalcanzables por clase: 0 de 11 dominios
institucionales responden, contra 5 de 5 registros comerciales. Reverificado en este pase y se confirma:**

`coe.int`, `unesco.org`, `unu.edu`, `publications.iadb.org`, `eur-lex.europa.eu`, `digital-strategy.ec.europa.eu` →
**los 6 devuelven `000`** (falla el CONNECT), con control positivo en la misma corrida: `packagist.org` **200**,
`registry.npmjs.org` **200**, `raw.githubusercontent.com` **200**.

🟢 **Pero hay un matiz que reclasifica el gap a medias, y conviene usarlo:** el barrido regional **sí** devolvió contenido
de `coe.int` en el cuerpo de sus resultados — la **2.ª Working Conference** del Consejo de Europa sobre las dimensiones
regulatorias de la AI en educación, en octubre, con el listado de actores europeos convocados. **También apareció el
*working paper* de UNU sobre implementación de AI en educación superior en América Latina y el Caribe, y el documento del
BID sobre marco regulatorio habilitante.**

🔵 **La distinción, y cambia cómo se cita en `intel/`: está bloqueado el canal de *fetch*, no el canal de información.**
Una afirmación obtenida así es **secundaria en la forma** (no se leyó el PDF) pero **primaria en el origen** (la fuente es
la institución, no una consultora), y **hay que anotarla como tal** en vez de meterla en la misma bolsa que las cifras de
las firmas de *market research*.

⚠️ **Lo que el matiz NO arregla:** no se puede citar un inciso, una fecha exacta ni un número de página, porque no se abre
el documento. **Para el calendario del Anexo III —la afirmación más cara de esta base— sigue valiendo el límite del gap 65**
y la fecha vigente sigue siendo la del pase 11 y 32: **2027-12-02**.

## 131. `curl` sobre `github.com` devuelve 403 para TODO, exista el repo o no: el verificador de URLs prescripto no verifica nada (agregado en el pase 37 del 2026-10-02)

**La consigna de ingesta de esta familia de KBs prescribe «verificar cada URL antes de escribirla (`curl -sI`); un 404 no
es un hallazgo». Medido en este pase: sobre `github.com` ese control es ciego.**

| URL | Existe | `curl` |
|---|---|---|
| `github.com/torvalds/linux` | sí | **403** |
| `github.com/moodle/moodle` | sí | **403** |
| `github.com/pie-framework/pie-elements` | sí | **403** |
| 🔴 `github.com/this-org-does-not-exist-zzz9/nope` | 🔴 **no** | 🔴 **403** |

🔴 **El HTML de `github.com` está bloqueado en bloque por el proxy, así que el código de estado no lleva ninguna
información sobre la existencia del repo.** Las consecuencias son las dos, según cómo se lea el 403: **si se lo toma como
«no 404, entonces existe», se aceptan slugs inventados; si se lo toma como fallo, se descartan repos reales.** En los dos
casos el resultado es ruido presentado como verificación.

🟢 **El discriminador correcto, con control negativo:**

| Canal | Repo real | Repo inexistente |
|---|---|---|
| 🟢 **`git ls-remote`** | **51.410 refs** | 🔴 `fatal: could not read Username for 'https://github.com'` |
| 🟢 `raw.githubusercontent.com/<slug>/<branch>/<archivo>` | **200** | **404** |
| 🟢 Registro de paquetes por nombre exacto | **200** + metadatos | **404** |

🔵 **La regla que reemplaza la de la consigna: la existencia de un repo de GitHub se verifica con `git ls-remote`, y el
contenido con `raw.githubusercontent.com`. Nunca con `curl` sobre `github.com`.** ⚠️ **Y es acumulativa con la tendencia
126:** `api.github.com` devuelve **200 con el error en el cuerpo**, y `github.com` devuelve **403 para todo**. **Los dos
canales «obvios» para verificar un repo están rotos de maneras distintas y los dos fallan en silencio** — razón por la cual
este pase fechó las 49 filas con el protocolo git y no con HTTP. Ver el **gap 77**.

## 132. Un fork con `main` más nuevo NO es un mantenedor, y el caso que lo prueba estaba a punto de entrar a esta base como dato bueno (agregado en el pase 38 del 2026-10-02)

El pase 37 estableció que **la actividad de bot no es mantenimiento** (tendencia 124): Dependabot y los regeneradores de
SDK mantienen vivo el grafo de refs de un proyecto que nadie atiende, y por eso **se fecha el tip de la rama por
defecto, nunca el ref más nuevo**. Este pase encuentra la variante hermana, y es más difícil de detectar porque **esta
vez el dato está en la rama correcta**.

Buscando sucesión para `DavidLMS/learnmcp-xapi` —congelado hace 13,1 meses, **42 menciones en `compose/patterns.md`**—
el primer resultado es **`ashleycribb/learnmcp-xapi`**, que el buscador presenta como *«a more recent fork»*. Y es
cierto en el único sentido medible sin diffear: su `main` está en **2026-09-17**, **trece meses más nuevo que el
upstream**. 🔴 **Si esta base hubiera aceptado el titular, habría escrito que su dependencia más citada tiene sucesor.**

Se midió el grafo en vez del titular:

| Medición | Valor |
|---|---|
| `merge-base` upstream/fork | `fbf6091` — **es el tip del upstream** (2025-08-29) |
| Commits del fork que no están en el upstream | **2** |
| Commits del upstream que no están en el fork | **0** |
| Qué son | `18b2954` *«Add Google Cloud Run deployment configuration and documentation»* + `816d8b8`, su merge |
| Estrellas / tags | **0** / **0** |

🔵 **El fork no mantiene el proyecto: lo despliega.** La lógica xAPI y MCP es la del upstream congelado, sin un cambio.
**La regla:** *fechar un fork sin contar los commits que agrega y leer qué tocan produce la misma clase de dato falso
que fechar un repo por su ref más nuevo.* El barrido estándar de vitalidad de esta base necesita una columna más —
**commits adelante/atrás del upstream**— igual que el pase 37 le agregó la distinción de ramas de bot (**gap 78**).

## 133. Los dos relojes regulatorios que mandan en 2026 ya corren, y los dos piden lo MISMO del software: que la nota la publique una persona (agregado en el pase 38 del 2026-10-02)

Esta base tiene el calendario del AI Act anotado desde el pase 21 (tendencia 121) y el volumen legislativo de North
America desde el 36. Lo que el barrido de este pase agrega es la **convergencia**, y es operativa, no retórica:

| Jurisdicción | Instrumento | Estado medido en este barrido | Qué exige del software |
|---|---|---|---|
| **EMEA** | **AI Act** | **Desde el 2 de agosto de 2026 la AI Office y las autoridades nacionales lo APLICAN.** Educación —acceso, evaluación, scoring de exámenes, trayectoria— es **alto riesgo** | Supervisión humana sobre la decisión |
| **North America** | Leyes estatales | **134 proyectos en 31 estados** (reconfirmado). **Oklahoma y Maryland exigen supervisión humana y prohíben que la AI tome decisiones de alto impacto sobre un alumno** | Lo mismo, por vía estatal |
| **APAC** | 3 leyes marco nuevas | **Corea: AI Basic Act en vigor el 22-01-2026** (19 proyectos consolidados; **segunda jurisdicción del mundo con ley integral después de la UE**). **Vietnam: Ley de AI adoptada en dic-2025, en vigor marzo 2026**, y **nombra educación entre seis sectores de alto riesgo** (evaluación automatizada y monitoreo conductual). **Taiwán: Ley Básica de AI en vigor el 14-01-2026** | Lo mismo, en tres países más |
| **LATAM** | Sin ley integral | Brasil, Chile, Colombia (CONPES) y México a velocidades distintas. **Uruguay fue el primero de la región en firmar el Convenio Marco del Consejo de Europa sobre AI** | Todavía por vía de privacidad y consumidor |

🔵 **La lectura que importa, y es la que convierte una restricción en argumento de venta:** tres regímenes
independientes —europeo, estatal norteamericano y asiático— **convergen en el mismo requisito de arquitectura**: la AI
puede proponer la nota, **la persona la publica**. Eso no es una política que se escribe en un PDF: es una propiedad del
conector. Ver la tendencia **134**.

⚠️ **Lo que este pase NO verificó, y queda declarado:** el **acuerdo Omnibus del AI Act posterga plazos de alto riesgo**
según una de las fuentes del barrido. **No se confirmaron las fechas nuevas contra el texto consolidado**, y esta base
ya tiene abierto el `gap 56` exactamente sobre el calendario del Anexo III. **No citar fechas pospuestas sin cerrar ese
gap**: es el tipo de dato que se dice en una reunión y sale caro.

## 134. Apareció la primera pieza permisiva de esta base cuyo DISEÑO DE SEGURIDAD es argumento de cumplimiento, y no sólo higiene de ingeniería (agregado en el pase 38 del 2026-10-02)

`toshieji/moodle-grading-mcp` (**MIT**, Japón/WACA, `HEAD` **2026-09-07**) reemplaza a la pieza que el pase 37 declaró
*«la única permisiva que pone nota dentro de un LMS»* y estaba fría hace 7,3 meses. Pero lo que lo hace la tendencia no
es que reemplace: es **cómo** escribe. Verificado en su README:

- La nota la **decide el cliente LLM**; el servidor sólo la escribe.
- La escribe en **`workflowstate=readyforreview`** — **graduada y NO publicada**. *Nunca* publica.
- **No dispara notificación al alumno.**
- Exige **`MOODLE_ALLOW_WRITE=1`** y **restringe la escritura a una allowlist de IDs de curso** — lista vacía = no puede escribir nada.
- **Loguea cada intento de escritura en un audit trail JSONL.**
- **Anexa un pie de declaración de asistencia por AI** salvo override explícito.

🟢 **Cada una de esas seis propiedades responde a un requisito de la tendencia 133.** «Human oversight» deja de ser una
cláusula de la propuesta y pasa a ser **el comportamiento por defecto del servidor**: el docente es el único que puede
publicar porque **el software no sabe hacerlo**. La trazabilidad deja de ser una promesa de logging y es un JSONL. La
transparencia hacia el alumno viene en el pie del texto.

🔵 **Por qué es una tendencia y no una ficha de producto:** hasta este pase, el eje de selección de esta base fue
**licencia × vitalidad × superficie de tools**. Esta pieza agrega un cuarto eje —**la forma en que el conector restringe
la escritura**— y es el único de los cuatro que se puede llevar a una conversación de compliance. **Con 0 estrellas.**
Las estrellas no miden esto, y es la segunda vez que esta base encuentra que la fila que más vale es la que menos
tracción tiene.

## 135. Ed-Fi y 1EdTech dejaron de ser dos mundos: apareció el primer repo de esta base con la firma de los DOS consorcios (agregado en el pase 38 del 2026-10-02)

Esta base venía tratando **Ed-Fi** (el dato del distrito, EE. UU.) y **1EdTech** (el estándar de interoperabilidad:
OneRoster, QTI, CLR, Open Badges) como ecosistemas separados, y la separación estaba bien fundada: aparecen en capas
distintas, con repos distintos y gobernanzas distintas.

**`Ed-Fi-Alliance-OSS/edfi-oneroster`** la rompe: vive en la organización de **Ed-Fi**, implementa un estándar de
**1EdTech** (OneRoster 1.2, 14 endpoints GET sobre una base Ed-Fi ODS, Apache-2.0, `HEAD` **2026-10-01**, 86 tags), y su
aviso de copyright dice **«Copyright (c) 2025 1EdTech Consortium, Inc. and contributors»**.

🔵 **Lo que significa para un entregable:** el puente entre *«el distrito tiene sus datos en Ed-Fi»* y *«el proveedor de
EdTech habla OneRoster»* **ya está escrito, es permisivo y está mantenido** — no hay que construir el traductor, que es
exactamente lo que `EASOL/edfi-to-oneroster` intentaba y abandonó **hace 10 años**. ⚠️ **Y el límite, que hay que decir
antes de que lo pregunten:** el repo **no declara certificación 1EdTech**. Implementación de referencia permisiva ≠
implementación certificada, y en una venta a un distrito esa distinción se hace.


## 🔵 Las tres acciones que este pase deja escritas para el siguiente

**Las tres son de medición y las tres son baratas. Dos se hacen en la misma tarde, porque son el mismo gesto —levantar un stack y pedir `tools/list`— sobre dos sistemas distintos.**

1. **Revisar si alguna otra ausencia declarada de esta KB ya fue cerrada por su propio proyecto** (**gap 54**). Este pase descubrió que el gap 48 estaba cerrado **dos meses antes** y el barrido no lo había notado, porque buscaba *«conector de terceros»* y la puerta la publicó el proyecto en **PyPI**, no en GitHub con nombre `*-mcp`. **La acción concreta: para cada ausencia de conector que esta base declara abierta, consultar el registro de paquetes del lenguaje de la plataforma (PyPI, npm, Packagist, RubyGems) con el nombre del proyecto, no del protocolo.** Es el canal que este pase demostró que faltaba.
2. **Pedir `tools/list` a los dos sistemas que quedaron medidos en el papel pero no en ejecución** (**gaps 52 y 55**): `docker-compose up` en **OpenCASE** y pedirle su **OpenAPI 3** al endpoint de descubrimiento —lo que habilita **generar** el conector de **P60** en vez de escribirlo—, y `tutor plugins enable openedxmcp` para ver **cuántas tools expone realmente** el conector oficial de Open edX frente a sus 35 rutas de fachada. **Las dos mediciones convierten cifras de documentación en cifras de protocolo**, que es la distinción que este pase estableció con `oneroster-ts` (aliasing) y CaSS (supresión).
3. 🔴 **Resolver el calendario del Anexo III contra el texto consolidado** (**gap 56**). Es la única de las tres que no es técnica y es la que más riesgo comercial descarga: esta KB tiene **dos fechas incompatibles publicadas en archivos distintos** —2027-12-02 por el pase 11 y «rige desde 2026-08-02» por el pase 28— y **sobre la segunda se construyó argumentación de venta para EMEA**. Hay que fechar cada afirmación con **el inciso del Anexo III** que le corresponde, porque educación es uno entre varios y el calendario no es único para todos.
