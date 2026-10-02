---
industry: education
region: Global
updated: 2026-10-02
---

# 🧩 Patrones de composición — Education

> Recetas concretas: repos nombrados, licencias verificadas, wiring explícito y estimación.
> Todos los repos citados fueron verificados vía WebFetch el 2026-09-30; los del pase 11, el 2026-10-01 (ver `agents/top.md`).
> **Pase 36 del 2026-10-02:** +2 patrones, y **los dos cierran una acción que el pase 35 dejó escrita.** **P76** — *el
> manifiesto MCP de QTI 3, escrito en vez de estimado*: las **20 tools** de `qti3-cli@0.13.1` con su `inputSchema` y su
> `readOnlyHint`, medidas en el `.tgz` y no en el README. 🔴 **Y la medición corrige tres cosas que esta KB traía: no son
> 14 comandos sino 17, no son 14 tools sino 20 —`certification` tiene CUATRO subcomandos— y el `USAGE` del propio CLI
> documenta sólo 2 de esos 4**, así que un envoltorio generado desde el texto de ayuda nace con **30 % de la superficie
> afuera**. **Hay exactamente 2 rutas de escritura en el paquete entero**, así que **18 de 20 tools son de lectura**, y el
> contrato de estado del modo adaptativo resulta **más estrecho de lo anotado**: sólo admite `outcomes` y
> `templateValues`, **cualquier otra clave es error duro**. **P77** — *datos educativos públicos de Brasil*: 🔴 **la
> respuesta a la acción 3 es que INEP NO publica API** —Censo Escolar es ZIP/CSV de **10-20 GB descomprimidos**— y la
> única API de terceros es **GPL-2.0, sólo IDEB y con el dominio sin resolver**. **Por eso el patrón se cotiza en 8-12
> semanas de pipeline y no en 2-3 de fachada**, que es la diferencia entre una propuesta honesta y una sorpresa.
> **Pase 34 del 2026-10-02:** +2 patrones, y **P69 pasa de abierto a decidido.** **P70** — *credenciales
> verificables con el expediente cerrado por el propio consorcio*: la capa que esta base declaraba vacía existe
> (`Schroedinger-Hat/certo`, ⚠️ **AGPL-3.0**, **OB 3.0 + W3C VC + DIDs**) y 🟢 **el validador oficial de 1EdTech es
> Apache-2.0**, así que la pieza copyleft queda **aislada en el borde** y el expediente lo cierra un tercero neutral —
> **North America primero, porque es la región donde no hay certificador y el comprador debe fabricarse la evidencia.**
> **P71** — *probar la telemetría antes de firmarla*: entra **`yetanalytics/datasim` (Apache-2.0)**, que permite
> **cargar el LRS con tráfico xAPI sintético antes de comprometer una cifra** —la única pieza de esta KB que contesta
> con una medición la barrera de APAC (**49 % sin infraestructura de tiempo real**)— y deja identificado el
> ***upstream* mejor ubicado de esta base: un `ralph[mcp]`**, que encaja en los **14 extras** que Ralph ya empaqueta
> **sin fork** (**gap 64**, cerrado en negativo con tres instrumentos). ✅ **Y P69 queda decidido por licencia y no por
> adopción: el stack PHP tiene ~10× las descargas pero es GPL-2.0-only en las 293 releases.**
> **Pase 33 del 2026-10-02:** +3 patrones, los tres sobre la capa de telemetría y la de evaluación. **P67** — *evidencia
> de aprendizaje auditable sobre el LMS que el cliente ya tiene*, que resuelve **dos mandatos de North America con
> piezas que ya existen** (`ACTOR_UUID` sin dato personal contra **California AB 1159**; rail de escritura con
> confirmación contra la **supervisión humana** de Oklahoma y Maryland) y la **brecha de uso superficial de LATAM**
> (79 % usa AI, 88 % con compromiso mínimo-a-moderado). **P68** — *telemetría soberana europea*, que existe porque este
> pase midió que **las piezas no soportan el argumento de soberanía con la misma fuerza**: el `LICENSE` de **Ralph**
> nombra a **France Université Numérique** y el de `learnmcp-xapi` dice **`Copyright (c) 2025 David Romero`**, así que
> **la soberanía se apoya en Ralph y la privacidad por diseño en `learnmcp-xapi`**. **P69** — *la puerta MCP de QTI*,
> que es **contribución *upstream*, no integración**: la mitad QTI del gap 60 es la **única ausencia de esta base medida
> por dos instrumentos independientes**, y envolver `@longsightgroup/qti3-cli` (**MIT**) cuesta **exactamente una
> dependencia externa** porque su cadena no tiene ninguna de terceros. ⚠️ **Y una advertencia transversal que atraviesa
> los tres: `coursecode` pone su rail de seguridad en las *anotaciones MCP* y no en el servidor, así que — a diferencia
> del *confirm token* de `openedx-mcp` — no frena solo.** Donde el pliego exija supervisión humana demostrable, **la
> confirmación es trabajo del integrador y entra en la estimación** (tendencia **114**).
> **Pase 26:** +4 patrones — **P50** (el perfil de competencia por MCP, con las 6 tools de CaSS **medidas** en vez de
> inferidas), **P51** (el conector MCP de Moodle que no existe, construido sobre el patrón del que sí existe para
> Canvas), **P52** (la capa agéntica de biblioteca sobre el bus de Kafka de FOLIO, Apache-2.0) y **P53** (*early warning*
> con humano decidiendo, que es el único envoltorio facturable de la capa predictiva en las cuatro regiones).
> **Pase 25:** +2 patrones — **P48** (del acervo QTI viejo a la aserción de competencia: migración → banco de ítems →
> entrega **certificada** → evidencia xAPI filtrada → competencia en CaSS, **todo MIT/Apache-2.0**) y **P49** (integridad
> de examen **sin** AI de vigilancia, que saca el entregable del **Annex III** en vez de buscar la pieza de proctoring que
> no existe en open source permisivo).
> **Pase 11:** +2 patrones — **P25** (riesgo de abandono conforme al Anexo III, la capa con presupuesto ya asignado y sin oferta open source) y **P26** (agente docente sobre la ontología curricular nacional ya publicada).
> **Pase 27:** **+4 patrones y una corrección.** 🔴 **P51 queda con premisa falsa** —el conector MCP de Moodle **sí existe y es MIT**— y lo reemplazan **P54** (corrección y devolución sobre Moodle con **compuerta humana**, el último tramo del gap 6, con piezas que ya escriben), **P55** (el conector de **Open edX**, que es el único que de verdad no existe), **P56** (**SCORM** como formato de salida de la capa generativa: cero integración, offline) y **P57** (evidencia por MCP cotizada sobre lo que CaSS **realmente** expone — 6 de 61 operaciones, con insignias y autoría de marcos **fuera**).

> **Pase 35 del 2026-10-02:** **+4 patrones, y tres de ellos existen porque aparecieron las piezas, no porque se haya inventado una receta.** 🟢 **P72** — *expediente de accesibilidad de la evaluación*: la obligación europea vencida que **P17** describía sin pieza por fin la tiene, y es **MIT y está adentro de la pila de evaluación** (`qti3-a11y` con `accessibilityProofMatrix` y guiones **VoiceOver/NVDA/JAWS**, `qti3-pnp` para *Personal Needs and Preferences*, `qti3-cli a11y-proof`, más **`accessibility audits`** del lado LMS en `bruchris/canvas-lms-mcp`). 🟢 **P73** — *el bucle cerrado docente*: **material propio → lección revisable → aula → nota**, con trazabilidad de punta a punta (`Claw-ED` MIT + `lineage-skill` Apache-2.0 + `coursecode` MIT + `canvas-lms-mcp` MIT); es el patrón que **P8** describía sin piezas, y **la rúbrica que califica sale del material del docente, no del modelo**. 🔵 **P74** — *el servidor MCP del dato educativo nacional*: Brasil tiene capa MCP de datos públicos (**IBGE/censo, BCB, DATASUS, firma**) y **educación es el único dominio grande que falta**; ⚠️ **se publica con la incógnita adelante —API o CSV— porque de eso depende si son 6 semanas o 4 meses, y esa medición es la acción 3 del pase 36.** 🔵 **P75** — *piloto sobre el LMS sin pedirle nada a sistemas*: `bunizao/moodle-cli` y `moon0825/jbnu-lms-student` trabajan **desde la sesión del navegador del usuario, con passkey y 2FA, sin token de administrador**, así que el valor se demuestra **antes** de la primera reunión con TI — 🔴 al costo de ser **sólo lectura**, que es un límite que se pone adelante. ⚠️ **Y P61 cambia de costo sin cambiar de contenido: la puerta oficial de Open edX publicó 12 releases en dos días y nada en los 70 siguientes (gap 70), así que se cotiza con presupuesto de mantenimiento.** ✅ **P56 gana su superconjunto:** `coursecode` expone **15 tools** y su `build` toma `format` como enum (`cmi5`/`scorm2004`/`scorm1.2`/`lti`), contra las 3 tools de `scorm-mcp-server`, que queda como la opción mínima *offline*. ⚠️ **P20 y P48 quedan más valiosos y más honestos: el QTI que el mundo despliega es GPL-2.0-only** (`oat-sa/qti-sdk`, 218.212 descargas, 293 versiones), **así que la pila permisiva es el diferencial — y hay que preguntar en el *discovery* si TAO ya está instalado.**

> **Pase 30 del 2026-10-02:** **+2 patrones y una muerte.** 🔴 **P55 queda con premisa muerta** —el conector MCP de Open edX **existe**, es oficial y es **AGPL-3.0 corriendo en proceso**—, y lo que queda de él es el mapa REST para quien necesite una puerta permisiva *fuera* de proceso. Entran **P61** (el **rail de escritura de agente** reimplementado en permisivo: *dry run* + **confirm token atado a una huella del payload**, rate limit por tool, autoridad viva y auditoría previa — la primitiva que P53 y P54 venían describiendo en prosa, ahora medida sobre una implementación real) y **P62** (el **expediente de competencia** para el requisito de graduación de *AI fluency*, con el marco **suscripto** vía la capa **CGE** de OpenCASE en vez de redactado). ✅ **Y P58 gana precisión sin reescribirse:** pasa de «164 métodos de SDK» a **«132 tools servidas, el 100 % de las operaciones distintas»**, medido ejecutando el servidor. ⚠️ **Corrección de este pase sobre sí mismo:** se iba a escribir que **P48** *«gana por fin una herramienta nombrada para la pata legada»* con `instructure/qti`, **y es falso** — P48 ya nombraba `LongsightGroup/qti3` (**MIT**, 667 commits), que además **migra** QTI 1.2/2.x a QTI 3, mientras la gema de Instructure **sólo importa y parsea**. **`instructure/qti` entra como alternativa de lectura en Ruby, no como pieza que faltaba.**

> **Pase 37 del 2026-10-02:** 🔴 **este pase no agrega recetas: audita las que hay.** Las **49 dependencias** de
> `agents/top.md` quedaron fechadas por el commit de su rama por defecto (`git ls-remote` + `fetch --depth 1`, **49 de 49
> respondieron, cero 404**), y **10 están paradas hace ≥ 6 meses — 3 hace ≥ 12**. 🔴 **Tres de esas diez son load-bearing
> en este archivo:** `DavidLMS/learnmcp-xapi` (**MIT**, `HEAD` **2025-08-29**, **13,1 meses**, **42 menciones acá**, puerta
> xAPI de **P4/P15/P67/P68/P69**), `trilogy-group/oneroster-ts` (**0BSD**, **2025-06-27**, **15,2 meses**, **132 tools**,
> **P58/P60/P64**) y `peancor/moodle-mcp-server` (**MIT**, **2026-02-22**, **7,3 meses**, **P54/P55**, la única pieza
> permisiva que pone nota dentro de un LMS). ⚠️ **Ninguno de los tres se retira** —los tres siguen siendo lo mejor
> disponible y los tres son permisivos— **pero los tres pasan de supuesto a línea de presupuesto**, y eso se escribe en la
> propuesta, no se descubre en la semana 6. Ver la sección de auditoría abajo y **P78**. 🟢 **Lo que sí está sano:** `lrsql`
> (Apache-2.0, **v0.9.9 del 2026-10-01**), Ralph (MIT, vivo en `main`), las cuatro puertas de Canvas y Moodle-alumno
> (commits de las últimas dos semanas) y `qti3-cli` (MIT). **El resto de las recetas no cambia.**

## P96 — Generar un curso de Open edX entero, con el **número de llamadas** cerrado (reencuadra **P95**: el árbol no se lee del endpoint de xblock) (agregado en el pase 44 del 2026-10-02)

**P95 quedó escrito con una premisa que este pase midió y es falsa:** que el recorrido del árbol se hace con el endpoint
de xblock del `v1`. **No se puede** — `get_block_info` lleva escrito *«children aren't being returned until we have a use
case»* y la respuesta de `retrieve` es **un bloque**, no un árbol (tendencia **172**). P96 reemplaza esa mitad y deja el
costo con número.

**Piezas** — todas en `openedx/edx-platform` (**AGPL-3.0**, `HEAD` `c0048e1` del 2026-10-02), API
`/api/contentstore/v1/`:

| Operación | Llamada | Qué devuelve | Costo |
|---|---|---|---|
| Leer el outline completo | `GET course_index/{course_id}` | `course_structure` (dict anidado) | **1 llamada, todo el árbol** |
| Leer un nivel de hijos | `GET container/{usage_key}/children` | hijos con `name`, `block_id`, `block_type` | 1 por contenedor |
| Crear un bloque | `POST xblock/` con `{parent_locator, category, display_name}` | **`{locator, courseKey}`** | **1 por bloque** |
| Crear el curso | `POST course_handler` + `course_rerun` | — | fuera del árbol REST versionado (**gap 57**) |

**Wiring, y es la parte que vuelve cotizable el patrón:**

```
POST /api/contentstore/v1/xblock/  {parent_locator: <curso>,    category: "chapter",    display_name: …}
   └─> {"locator": "block-v1:…+type@chapter+block@<uuid>"}        ← ESTE string es el parent_locator del hijo
       POST …/xblock/              {parent_locator: <ese locator>, category: "sequential", …}
           └─> POST …/xblock/      {parent_locator: <ese>,         category: "vertical", …}
               └─> POST …/xblock/  {parent_locator: <ese>,         category: "html" | "problem" | "video", …}
```

**Costo: exactamente N POSTs para N bloques, y cero lecturas intermedias.** La dependencia es sólo vertical —un hijo
necesita el `locator` de su padre— así que **los hermanos se emiten en paralelo**. Para un curso de 4 capítulos × 3
secuencias × 4 verticales × 3 bloques = **4 + 12 + 48 + 144 = 208 POSTs**, con un camino crítico de **4** llamadas.
Eso es lo que se escribe en la propuesta, en vez de «se recorre el árbol».

⚠️ **Tres cosas que hay que poner en el cliente, no descubrir en UAT:**

1. **`category` no se valida en el servidor.** `XblockSerializer.category` es un `CharField(required=False)` sin
   `choices`; se resuelve en runtime contra los XBlock instalados. **Validar la lista en el cliente**, contra los
   `category` que el `course_structure` ya muestra en ese despliegue.
2. **Omitir `category` da 500, no 400** (`request.json["category"]` → `KeyError`). **Requerirlo en el cliente.**
3. **En una biblioteca v1 el enum existe y son tres:** `["html", "problem", "video"]`. Un generador que meta `vertical`
   en una biblioteca recibe **400 con texto plano**, no JSON.

🔵 **Y si hace falta bajar el payload de las lecturas:** `?view=minimal` sirve, pero devuelve **4 de los 6 campos que
documenta** y sólo en `retrieve`; para hijos, la única combinación que los trae es
`?fields=customReadToken&view=minimal`, **un nivel y sin `parent`**. Para recorrer, `course_index` es estrictamente
mejor.

**Estimación:** 2–3 semanas para el generador con reintentos y validación de `category` en cliente, sobre un despliegue
existente. **No** incluye crear el curso (curso plantilla + `course_rerun`, **P63**).

## P97 — Idempotencia **derivada del contenido** para toda operación que crea algo irreversible hacia afuera (agregado en el pase 44 del 2026-10-02)

**El problema, medido en una pieza real.** Emitir un credencial, mandar un mail a un alumno, publicar una nota: son
operaciones que un agente en bucle puede repetir y que **no se pueden deshacer desde el agente**. `issuebadge/mcp-server`
(**MIT**) es la primera pieza de esta base que intenta frenarlo con **idempotencia** —la forma correcta— y las dos
decisiones que toma son las dos equivocadas (tendencia **174**):

| Lo que hace | Por qué falla | Qué hacer en su lugar |
|---|---|---|
| `idempotency_key` **opcional**, y si falta la genera: `input.idempotency_key \|\| "mcp-" + crypto.randomUUID()` **por llamada** | Un reintento sin arrastrar la clave **emite un segundo certificado**: el valor por omisión **anula** la primitiva | **Derivarla del contenido**, nunca de un UUID: `sha256(badge_id + recipient_email + achievement_id)`. Dos intentos del mismo hecho dan la misma clave **sin que nadie recuerde nada** |
| El cumplimiento vive **en la API del proveedor** (*«a reused key is rejected by the API»*) | El README ofrece auto-hospedar el worker: un despliegue propio **hereda la forma sin la protección** | Hacerla cumplir **del lado que uno controla**: tabla `(idempotency_key → issue_id)` en el *gateway*, y responder el `issue_id` guardado en vez de reenviar |

**La receta, componible con el *gateway* de P85 / P93 que esta base ya tiene escrito y probado:**

```
agente ──tools/call issue_badge──▶ gateway
                                    │ 1. key = sha256(badge_id|email|achievement)   ← derivada, no recibida
                                    │ 2. ¿key en la tabla?  sí ─▶ devolver el issue_id guardado (no se llama al upstream)
                                    │ 3. no ─▶ POST upstream ─▶ guardar (key → issue_id) ANTES de responder
                                    ▼
                              emisor (issuebadge / certo / cualquiera)
```

**Por qué el orden importa:** guardar **antes** de responder convierte una caída entre el POST y la respuesta en una
lectura de tabla en el reintento, no en una segunda emisión. Es la misma disciplina que `openedx-mcp` aplica con su
**auditoría append-only previa a la escritura** (tendencia 84) — y aquí la primitiva es más fuerte, porque no le pide
cooperación al cliente.

🔵 **Dónde cae en el catálogo de esta base.** Las cinco variantes de freno, ordenadas por quién tiene que cooperar:

1. **Nadie** — `learnmcp-xapi`: rate limit en la configuración; frena solo.
2. **Nadie** — **esta receta**: la clave se deriva, el estado es del gateway.
3. **El servidor** — `openedx-mcp`: *confirm token* atado a una huella del payload.
4. **El cliente** — `coursecode`: anotaciones MCP + `dryRun`; y `qti3-cli`, que ancla procedencia.
5. **El proveedor remoto** — `issuebadge` tal como está: la más débil, y se cae al auto-hospedar.

**Licencia:** la receta es propia; el emisor es sustituible. Para el camino de **estándar** (Open Badges 3.0 firmado) el
emisor sigue siendo el de **P84** —`1EdTech/digital-credentials-public-validator` (**Apache-2.0**) y
`@ajna-inc/openbadges` (**Apache-2.0**)—, no `issuebadge`, que **no implementa OB 3.0**.

**Estimación:** 1 semana sobre un *gateway* ya desplegado (la tabla y el hash son el trabajo; el resto ya está).

## P98 — Antes de proponer la superficie REST de un servicio Spring: los **cuatro controles** que el pase 44 tuvo que inventar (agregado en el pase 44 del 2026-10-02)

**Esto no es un patrón de producto, es el control de calidad de todos los patrones de esta base que envuelven un
servicio** — P60, P85, P92, P93. El pase 44 descubrió que la tabla de SEB Server, medida con cuidado dos pases antes,
tenía **cuatro defectos** y **ninguno** era del upstream: los cuatro eran del extractor (tendencias **166**–**170**).
Cualquiera se repite en el próximo servicio si no se asevera.

| # | Control | Cómo se verifica | Qué atrapa |
|---|---|---|---|
| 1 | **Ninguna ruta contiene `${`, y toda ruta empieza con `/`** | aserción sobre la tabla | El mapeo de clase que es una **propiedad** y no una ruta. En SEB Server **27 de 30** controladores. Sin esto, la puerta da **404 en el 100 %** de las llamadas |
| 2 | **Las constantes compuestas están resueltas** | contar `X = "literal"` contra `X = OTRO + "/sufijo"` y comparar con el total | En SEB Server, **14 de 55** eran compuestas y se perdían todas — incluida **la superficie de autenticación completa** |
| 3 | **Ninguna fila viene de una declaración de clase** | el patrón exige `(public\|protected) <tipo> <nombre>(` | La **fila fantasma** por controlador. Un `public class Foo` no tiene tipo de retorno; una operación sí |
| 4 | **Las clases con `@ConditionalOn*` están marcadas y excluidas** | columna `condition` + aserción | La ruta que **existe en el árbol y no en el despliegue**. `LightController` con `light.setup=false` |

**Y dos controles de método que vienen de pases anteriores y siguen valiendo:**

* **La herencia aporta rutas, y la subclase «sólo lectura» no las borra.** `ReadonlyEntityController` conserva los
  `@RequestMapping` y lanza en el cuerpo, así que **la ruta de escritura se sigue anunciando**. Hay que negar **por
  nombre**, nunca por descubrimiento — y hay que contar bien: en SEB Server niega **4 de 5**, y la quinta
  (`DELETE /{id}/force`) se frena **una capa más abajo** (tendencia **169**).
* **Control de regresión contra la medición anterior, aunque la anterior sea la que se corrige.** Las cuatro filas
  viejas y las nuevas tenían que coincidir **salvo por los defectos explicados**; fue así como se detectó que el patrón
  nuevo, en su primera versión, perdía 6 métodos con tipo de retorno cualificado. **Una corrección sin control de
  regresión es una segunda medición sin verificar.**

🔵 **El artefacto está escrito y es reutilizable:** `compose/code/sebserver-mcp-gate/extract_surface.py` (stdlib, sin
dependencias) toma un checkout y emite las dos tablas con las columnas que estos controles necesitan; y
`test_gate.py` aseverá los cuatro, con **37/37 en verde**. Para el próximo servicio Spring se cambian los tres
diccionarios de arriba del archivo.

**Costo de aplicarlo: horas.** Costo de no aplicarlo: una puerta que se demuestra en una reunión y da 404 en la primera
llamada real.

## P93 — La puerta MCP de SEB Server: supervisión de examen con la escritura fuera de la lista, y **la capa de examen por fin completa** (agregado en el pase 43 del 2026-10-02)

**Qué resuelve.** Cierra la mitad abierta del **gap 86**. De las dos capas institucionales de examen de esta KB, UniTime
(horarios) ya tenía puerta de agente (**P85**/**P92**) y **SEB Server** (supervisión) no. Con las dos escritas, se puede
proponer **la capa de examen completa —horario y supervisión— con licencia permisiva y sin competencia agéntica**.

### Las piezas, verificadas el 2026-10-02

| Pieza | Licencia | Dato medido |
|---|---|---|
| [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | 🟢 **Apache-2.0** | Rama por defecto **`master`** (`git ls-remote --symref`), commit `7f45689`. **42** constantes `*_ENDPOINT` en `gbl/api/API.java`; **30** controladores concretos + **3** bases abstractas |
| `compose/code/sebserver-mcp-gate/` | el de esta KB | **79** operaciones → **79** tools, **36** expuestas. **11/11 checks** por ejecución |

### El wiring

1. **Los datos salen del árbol, no de la documentación.** `endpoints.tsv` son las 42 constantes `*_ENDPOINT` de
   `gbl/api/API.java`; `operations.tsv` son las operaciones por controlador, separadas en **`own`** (el
   `@RequestMapping` propio del controlador) e **`inherited`** (la superficie CRUD medida sobre `EntityController`, que
   declara **10** operaciones, y `ActivatableEntityController`, que agrega **3** distintas).
2. **El manifiesto se indexa por constante y controlador, nunca por path.** `EXAM_ADMINISTRATION_ENDPOINT` y
   `LMS_FULL_INTEGRATION_EXAM_ENDPOINT` **valen las dos `/exam`**: indexar por path los colapsa.
3. **La allowlist se construye por NOMBRE.** Dos políticas: *read-only* (todo `POST`/`PUT`/`DELETE`/**`PATCH`** queda
   fuera) y **deny nombrado** para `/batch-action`, **lecturas incluidas** — es un ejecutor de acciones masivas, una
   llamada se abre en muchas entidades, que es la misma razón por la que P85 retiene el conector `script` de UniTime.
4. **`tools/list` se arma DESDE la allowlist**, así que una tool retenida **no se anuncia**. La retenida que se llama
   igual recibe **`-32601`** y **no llega al upstream**.

### 🔴 Por qué la allowlist NO se puede derivar descubriendo rutas

Es lo que convierte este patrón en argumento y no en preferencia. `ReadonlyEntityController` **conserva** las
anotaciones `@RequestMapping` de `PUT`/`POST`/`DELETE` heredadas y lanza `AccessDeniedException` **en el cuerpo**:

```java
@Override
@RequestMapping(method = RequestMethod.PUT, ...)
public T savePut(@Valid @RequestBody final T modifyData) {
    throw new AccessDeniedException(ONLY_READ_ACCESS);
}
```

La ruta **existe y se anuncia**. Un generador que lea anotaciones **emite tools de escritura legítimas en apariencia**
sobre entidades de sólo lectura. Y `ExamAdministrationController` declara un **`PATCH`**, verbo ausente de la base: un
manifiesto armado con las 10 operaciones de `EntityController` **se lo pierde**. Ver la tendencia **159**.

### La prueba, por ejecución y sin levantar SEB Server

```sh
cd compose/code/sebserver-mcp-gate && python3 test_gate.py
```

* **37** tools de escritura en `/exam`, `/lms-setup`, `/useraccount`, `/batch-action` → **todas `-32601`**
* **11** tools de `/batch-action` → **todas** fuera de la allowlist, **incluidas las lecturas**
* **0** llamadas retenidas llegaron al upstream — afirmado sobre **el contador del propio stub**, no sobre el mensaje
* **36** lecturas **sí** se despachan: el gate no es vacuamente restrictivo
* una tool inventada recibe el mismo `-32601`, sin filtrar la diferencia entre «no existe» y «no está permitida»

### Cómo se cotiza, por región

| Región | Encuadre |
|---|---|
| **EMEA** | 🔵 **El más fuerte.** SEB Server es suizo (ETH Zürich) y la supervisión de exámenes es **alto riesgo** bajo el AI Act, con plazo a **2 de diciembre de 2027**: el *gateway* es evidencia de **supervisión humana** y de que el agente **no escribe** |
| **North America** | Oklahoma y Maryland **prohíben** decisiones de alto impacto automatizadas: la partición lectura/escritura es exactamente ese control, documentado |
| **LATAM** | Entra por **integridad académica**, que es el cuello de botella real de la región (**61 %** de alumnos preocupados por el mal uso de sus pares), no por habilitación de AI |
| **APAC** | Se cita el **marco de AI agéntica de la IMDA de Singapur** (22 de enero de 2026), el primer texto de regulador que trata a los agentes como categoría propia |

### ⚠️ Alcance, declarado y no implícito

`operations.tsv` cubre **los cuatro endpoints** que el handoff nombró para verificación. Los **26** controladores
concretos restantes **no** están medidos, y la tendencia 159 es la razón por la que **no se adivinan**. Extenderlo es
mecánico —un `curl` por controlador, leer el `extends`— y es **la acción 1 del pase 44**.

## P94 — Cotizar un **tercer** proveedor de proctoring en SEB Server con el costo real, no con la cantidad de métodos (agregado en el pase 43 del 2026-10-02)

**Qué resuelve.** **P91** decía «12 métodos obligatorios», y con eso no se arma un presupuesto: ni la cifra era correcta
ni la cantidad de métodos es la magnitud que manda. Este patrón reemplaza esa línea por una tabla medida, **y agrega la
pieza de validación que faltaba**.

### 🔴 Las dos correcciones, primero

1. `RemoteProctoringService` tiene **14 métodos obligatorios, no 12** — los 14 abstractos, **sin ningún `default`** y
   **sin ningún `static`**.
2. **Los 14 métodos son el 22-23 % de la clase.** El resto —*helpers*, DTOs, caché de `RestTemplate`, construcción de
   tokens— es el **77 %** que nadie presupuesta.

| Magnitud que se cotiza | **Jitsi** (la barata) | **Zoom** (la realista) |
|---|---|---|
| Líneas de código de la clase | **481** | **912** |
| Líneas en los 14 métodos | 107 (**22 %**) | 212 (**23 %**) |
| Líneas **fuera** de la interfaz | **374** | **700** |
| Métodos triviales (≤6 líneas, sin red) | 10 de 14 | 6 de 14 |
| Métodos que hablan con el remoto | **1** (`testExamProctoring`) | **2** |
| Métodos privados de apoyo / clases internas | 2 / 0 | **8** / 1 |
| *Imports* de terceros | 17 | **38** |
| Criptografía | 🔴 **HmacSHA256 + Base64 + `Mac.getInstance`** | 🔴 **idem** |

### El wiring, en tres piezas y en este orden

1. **La implementación.** Una clase que implemente los **14** métodos. Presupuestar el rango **481–912 líneas**, no 107:
   el piso es Jitsi porque delega casi todo, el techo es Zoom porque administra el ciclo de vida de salas de verdad.
   Partir de **`JitsiProctoringService`** si el proveedor expone salas por URL firmada; de **`ZoomProctoringService`** si
   hay *breakout rooms* y reconfiguración.
2. 🔴 **La validación, que SEB Server NO aplica a un proveedor de terceros.** Antes de escribir la implementación, poner
   el validador: `compose/code/seb-proctoring-validator/` —**21/21 checks, JDK puro**— porque el validador de upstream
   termina en `return true` y **acepta el proveedor nuevo con todos los campos vacíos**. Sin esto, el síntoma aparece en
   la primera sesión de examen como fallo de autenticación, no al guardar como error de formulario. Ver la tendencia
   **161**.
3. **El enum y la anotación.** Un valor nuevo en `ProctoringServerType` y apuntar `@ValidProctoringSettings` a la clase
   que valida de verdad.

### 🔴 Lo que sube el nivel de revisión y hay que decirlo en la propuesta

**Las dos implementaciones de referencia firman tokens con HMAC-SHA256 a mano.** La criptografía **no es opcional** en
este puerto: es el contrato de los dos proveedores. Un error ahí no es un bug funcional, así que la revisión de
seguridad **se presupuesta aparte** — y eso no estaba en P91.

**Y que sólo 1 de 14 métodos hable con la red no abarata:** significa que el resto es **lógica de dominio del
proveedor** (ciclo de vida de salas, instrucciones de reconfiguración, mapeo de atributos), que es precisamente lo que
**no** se copia de la otra implementación.

## P95 — Generar un curso de Open edX **entero** por HTTP: una llamada legacy y **un** endpoint recorrido en árbol (agregado en el pase 43 del 2026-10-02)

**Qué resuelve.** Reencuadra **P55** y **P63**. Esta base tenía el *authoring* partido en dos dudas: si se podía crear el
curso (resuelto en el pase 32) y si el árbol versionado alcanzaba para la estructura (el **gap 50**). Con el gap 50
cerrado, **el recorrido completo son dos endpoints, no cinco**, y 🔴 **sobre `v1`, no sobre `v0`**.

### 🔴 La corrección de versión, primero, porque invierte lo que esta base recomendaba

`v0` de *authoring* está **deprecado**: su propio encabezado dice *«superseded by `XblockViewSet` … Use
`/api/contentstore/v1/xblock/` going forward. These v0 endpoints will be removed in a future release»*, y cada método
emite `DeprecationWarning`. **El `v1` no es el experimental: es el canónico**, y trae sobre de error estandarizado
(ADR 0029), autenticación explícita (ADR 0026/0034), **`?view=minimal`** (ADR 0036) y el tag OpenAPI
**`openedx-platform-sdk`** para generar clientes. Ver la tendencia **157**.

### El wiring

| Paso | Llamada | Nota |
|---|---|---|
| 1. Crear el curso | `POST /course/` con `Accept: application/json` (vista **legacy**) | **Sin** `source_course_key` crea de cero. Permiso: **`is_content_creator(user, org)`**, no `GlobalStaff` → el alta **se delega por organización**. ⚠️ Al **clonar**, omitir `display_name` levanta `KeyError` |
| 2. Secciones, subsecciones, unidades **y** componentes | `POST /api/contentstore/v1/xblock/` | 🔵 **El mismo endpoint para los cuatro niveles.** `parent_locator` dice de quién cuelga; `category` dice qué es (`chapter`, `sequential`, `vertical`, o el tipo de bloque) |
| 3. Leer/modificar un bloque | `GET`/`PUT`/`PATCH`/`DELETE /api/contentstore/v1/xblock/{usage_key}/` | El mismo `ViewSet`, cinco verbos |
| 4. Recorrer el árbol barato | `GET …/{usage_key}/?view=minimal` | Devuelve sólo `id`, `display_name`, `category`, `children`, `has_children`, `studio_url` — **sin** `data`, `metadata`, `student_view_data` ni OLX |

🔵 **Por qué esto cambia la estimación:** no hay un cliente por nivel de jerarquía. En Open edX **la sección, la
subsección y la unidad SON XBlocks**, igual que un componente, así que el generador es **una función recursiva sobre un
endpoint**. El serializer es **estricto** (`StrictSerializer`: tipos validados, **ningún campo inesperado**), así que el
contrato se valida del lado del servidor y los campos disponibles están enumerados: `parent_locator`, `display_name`,
`category`, `data`, `metadata`, `children`, `fields`.

### ⚠️ Las dos trampas que van escritas en la propuesta

1. **`?fields=` no es ADR 0036.** Es un *pass-through* **legacy** que selecciona *tipo de respuesta*
   (`?fields=graderType`, `ancestorInfo`, `customReadToken`), no un subconjunto de claves. Para subconjunto, **`?view=minimal`**.
2. **El clon es medio asincrónico.** La clave vuelve en la respuesta, pero el copiado va a **Celery**
   (`rerun_course_task.delay`) y se sigue por **`CourseRerunState`**: hay que **pollear antes de escribir** en el curso
   nuevo. Y el clon **resetea** `advertised_start`, `enrollment_start`, `enrollment_end` y `video_upload_pipeline`.

### Cómo se cotiza, por región

**Open edX es la huella pública grande de LATAM e India**, así que este patrón se cotiza primero ahí — con la salvedad de
licencia que esta base ya tiene escrita: **Open edX es AGPL-3.0**, y la regla *«las puertas de agente son MIT»* **no
vale** para esta pieza. El cliente propio que se escribe contra estos endpoints **sí** puede ser permisivo; el servidor
que se despliega, no.

## P88 — La puerta MCP de UniTime: horarios, aulas y exámenes académicos, con el conector `script` fuera de la lista (agregado en el pase 41 del 2026-10-02)

**La capa que el pase 40 midió vacía de agente tiene una base Apache-2.0 viva, y su API es la más fácil de envolver que
esta base haya medido — porque el conector ya ES la unidad.**

**Piezas**

| Pieza | Licencia | Rol |
|---|---|---|
| [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** (Apereo) | el sistema de horarios: cursos, aulas, exámenes, *student scheduling*. `HEAD` **2026-10-01**, 202 tags |
| *Gateway* de allowlist del pase 40 (**P85**) | propio | **175 líneas de stdlib**, ya probado: recorta `tools/list` y bloquea con `-32601` sin llegar al upstream |

**Wiring**

1. **La unidad de mapeo es `conector × verbo`.** UniTime despacha en `/api/<nombre>` y el nombre lo da `getName()`.
   La autenticación **ya existe**: `?token=`, habilitada con la propiedad `ApiCanUseAPIToken`.
2. **Las tools de LECTURA, que son las que se exponen primero** (9 conectores, sólo `GET`):
   `class-info`, `curricula`, `enrollments`, `instructors`, `instructor-schedule`, `roles`, `student-groups`, más la
   lectura de `rooms` y `events`. 🔵 **Con eso solo ya se contesta la pregunta que un agente de operación académica
   necesita**: *«¿qué aulas están libres el martes a las 10?»*, *«¿cuál es el horario de este docente?»*,
   *«¿quién está inscripto en esta clase?»*.
3. 🔴 **La *denylist*, que va en la primera versión y no en la segunda:**

| Tool candidata | Por qué queda fuera |
|---|---|
| 🔴 **`script` (GET y POST)** | 🔴 **ejecuta scripts del servidor.** Exponerlo como tool es dar ejecución remota al modelo. **Nunca** |
| `rooms` POST/PUT/**DELETE** | borra y modifica el inventario de aulas de la institución |
| `buildings` POST/**DELETE** | ídem, edificios |
| `events` POST/**DELETE** | borra reservas de espacio |
| `exchange` POST | `DataExchangeConnector`: importación masiva de datos |
| `sectioning` POST | **inscribe y desinscribe alumnos** |

4. **El `tools/list` se construye desde la allowlist, no desde el catálogo.** Es exactamente el caso que P85 probó: con
   allowlist vacía expone **0 tools**, y lo que no está en la lista **se rechaza con `-32601` sin llegar al upstream**.
5. **La escritura, cuando se habilite, pasa por confirmación humana** — el mismo principio que `readyforreview` de
   `moodle-grading-mcp` (tendencia 136): el agente propone el cambio de horario; **lo confirma una persona.**

**Estimación.** La parte de descubrimiento **ya está hecha y publicada en esta KB** (los 15 nombres y sus verbos, en
`repos/trending.md`, pase 41). Lo que queda es el manifiesto de tools y el cableado sobre un *gateway* que ya existe y
está probado. ⚠️ **Se prueba contra un *stub* que imite `/api/<nombre>`, sin levantar UniTime** — es el método que el
pase 40 usó para validar P85.

🟢 **Por qué este patrón vale más que los otros conectores de LMS de esta base: es la única capa donde la medición dice
que no hay competencia.** **404 en 8 de 8 nombres de npm y 0 en los 46,6 MB del índice de PyPI** (**gap 86**).
🔵 **Y el dato de venta: `rooms` acepta los cuatro verbos, o sea que la institución que ya usa UniTime tiene la gestión
de espacios lista para automatizar — pero eso es la fase 2, y la fase 1 ya es útil sin ningún riesgo de escritura.**

## P89 — *Proctoring* y examen seguro SIN AGPL: SEB Server sobre el LMS que el cliente ya tiene (agregado en el pase 41 del 2026-10-02)

**Hasta el pase 40 esta base sostenía que fuera de Open edX la capa de integración de examen había que construirla. Es
falso: existe, es MPL-2.0, es de ETH Zürich y ya habla con tres de los LMS de este archivo.**

**Piezas**

| Pieza | Licencia | Rol |
|---|---|---|
| [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | ⚠️ **MPL-2.0** (copleft **débil**, por archivo) | administración, configuración, **monitoreo** y *proctoring* de exámenes. **36 controladores REST / 41 endpoints** |
| [`seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) | ⚠️ **MPL-2.0** | el cliente de bloqueo de escritorio (Windows) |
| `moodle/moodle` **o** `openedx/edx-platform` **o** `OpenOLAT/OpenOLAT` | GPL-3.0 / AGPL-3.0 / Apache-2.0 | el LMS que el cliente **ya tiene** |
| *Gateway* de allowlist (**P85**) | propio | la puerta de agente, que **no existe todavía** (gap 86) |

**Wiring**

1. **Se elige el binding por el `enum LmsType` de SEB Server, que ya está escrito:** 🟢 **`MOODLE_PLUGIN` es la única
   combinación con `LMS_FULL_INTEGRATION`** (además de `COURSE_API`, `COURSE_RECOVERY` y `SEB_RESTRICTION`). `OPEN_EDX` y
   `OPEN_OLAT` traen `COURSE_API` + `SEB_RESTRICTION`. ⚠️ **`MOODLE` «pelado» NO trae `SEB_RESTRICTION`** — está
   comentada en el fuente. **Si el cliente es Moodle, el plugin de integración no es opcional.**
2. **El LMS sigue siendo la fuente de verdad del curso y del examen**; SEB Server aporta la configuración del cliente
   (`/examconfig`, `/light-config`), el *handshake* (`/handshake`) y la telemetría de la sesión (`/sebping`, `/seblog`).
3. 🟢 **La capa agéntica se engancha en los endpoints de monitoreo, que es donde un agente agrega valor sin decidir nada
   sobre el alumno:** `/monitoring`, `/overview`, `/notification`, `/instruction`, `/finishedexams`.
   🔵 **El agente resume y prioriza incidentes para el supervisor humano; no expulsa a nadie.**
4. 🔴 **Lo que NO se expone como tool, por la misma razón que en P88:** `/disable-connection` (corta la conexión de un
   alumno **en medio de un examen**) y todo lo que escriba sobre `/exam` o `/client_configuration`.

**La decisión de licencia, que es el punto del patrón**

| Ruta | Licencia del punto de integración | Cuándo conviene |
|---|---|---|
| **Open edX nativo** (`edx-proctoring`) | 🟢 `backends/` **Apache-2.0** dentro de un paquete AGPL-3.0 | el cliente **ya es Open edX**: la AGPL del LMS ya está aceptada y el backend se registra con un *entry point* (**P90**) |
| **SEB Server** | ⚠️ **MPL-2.0**: se publica lo que se modifica de los archivos cubiertos; **lo que se construye al lado, no** | el cliente **no es Open edX**, o quiere **un producto propio al lado** sin discusión de obra derivada |

⚠️ **Antes de proponerlo, dos advertencias medidas en este pase:** (1) **la rama por defecto de `seb-server` tiene 6 meses
y la de desarrollo commiteó ayer** — hay que decidir si el entregable se para en el tag `v3.0-latest` o en `dev-3.0`
(**gap 87**); (2) esta base tiene **los nombres** de los 36 controladores pero **no** sus modelos de estado ni su contrato
de extensión de proveedor: **la ruta Open edX se puede cotizar con números y ésta todavía con adjetivos** (es la acción 3
del pase 42).

🔴 **Y el expediente va primero, no después:** el *«monitoreo durante exámenes»* está **nombrado en el Anexo III punto 3
del AI Act** (**2027-12-02**) y **Vietnam nombra la *monitorización del comportamiento* en evaluación** entre sus seis
sectores de alto riesgo (**2027-03-01**, nueve meses antes). **Para un cliente con operación en los dos lados, la fecha
que manda es marzo de 2027** (tendencia **156**).

## P92 — La puerta MCP de UniTime: 26 tools generados del árbol, 13 expuestos, y el `script` retenido antes del upstream (agregado en el pase 42 del 2026-10-02)

**Este patrón no se describe: está escrito y probado.** La acción 1 del pase 41 pedía escribir la puerta de la única capa
que esta base midió con **cero competencia agéntica, licencia Apache-2.0 y despliegue institucional real**. Hecho, y
verificado por ejecución: **23 aserciones, 23 en verde.**

**Piezas**

| Pieza | Licencia | Rol |
|---|---|---|
| [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** (Apereo) | El *upstream*: 15 conectores con nombre registrado, verbos y `?token=` |
| *Gateway* de allowlist (**P85**) | propio | **175 líneas de stdlib** del pase 40, ya probadas |
| Generador de manifiesto (**este patrón**) | propio | **~115 líneas de stdlib**: lee los conectores del árbol y emite 26 tools. 🟢 **Código y prueba versionados en [`compose/code/unitime-mcp-gate/`](code/unitime-mcp-gate/)** |
| Un agente cualquiera de `agents/top.md` | — | El consumidor MCP |

**Cómo se arma**

1. **El manifiesto se genera del ÁRBOL, no de documentación.** Se recorre
   `JavaSource/org/unitime/timetable/api/connectors/*.java` y por cada clase se leen dos cosas: **el literal que devuelve
   el override de `getName()`** y **los `do{Get,Post,Put,Delete}` efectivamente sobreescritos**. Sale un tool por
   `(conector, verbo)`: **26 para los 15 conectores.** 🔴 **Y hay que leer el `return` del override, no el primer literal
   después de `getName`:** ese atajo devuelve `"name"` para `EventsConnector` y `"log"` para `ScriptConnector` — **dos
   nombres falsos, uno de ellos el del conector peligroso.**
2. **La política por defecto es dos reglas, no una lista a mano:** *negar los conectores de la denylist* (`script`) y
   *exponer sólo verbos de lectura*. Sobre 26 tools deja **13**.
3. **El `tools/list` se construye DESDE la allowlist**, así que un tool retenido no existe para el agente: no lo ve y no
   puede pedirlo por nombre.
4. **Un `tools/call` a un tool retenido se responde `-32601` y NO se reenvía.** Es lo que el *gateway* del pase 40 probó y
   lo que este pase volvió a probar con un *stub* que **registra cada llamada que recibe**.

**Lo que la prueba verifica, y es lo que se le muestra a un cliente**

| Aserción | Resultado |
|---|---|
| Conectores leídos del árbol / tools generados | **15** / **26** |
| Tools expuestos / verbos de escritura expuestos / tools de `script` | 🟢 **13** / 🟢 **0** / 🟢 **0** |
| `script.{get,post}` → `-32601` | 🟢 ✅ |
| `rooms.{post,put,delete}`, `buildings.{post,delete}`, `events.{post,delete}` → `-32601` | 🟢 ✅ |
| 🔴 **Llamadas retenidas que llegaron al upstream** | 🟢 **0 de 9** |
| `rooms.get` permitido llega al upstream | 🟢 ✅ **1 y sólo 1** |
| Allowlist vacía → 0 tools, y hasta una lectura da `-32601` | 🟢 ✅ |
| Extremo a extremo por stdio real (subproceso, 3 peticiones) | 🟢 **3 de 3** |

🔴 **Por qué esta puerta no se demuestra nunca sin allowlist:** `ScriptConnector` acepta `POST` y arma un
`ExecuteScriptRpcRequest` — **ejecuta un script del servidor**. Un envoltorio ingenuo de los 15 conectores **publica
ejecución remota como tool de un agente**. 🟢 **El *gateway* lo retiene antes del upstream; no después, y no con un
*prompt*.**

⚠️ **Lo que este patrón NO prueba, declarado:** no se levantó UniTime. El *upstream* es un *stub* que imita la API de
conectores, **igual que el pase 40 probó su *gateway***. **Lo medido es la partición de tools, que es la parte que decide
si la puerta se puede proponer; lo que falta es el mapeo de parámetros de cada conector contra una instancia real.**

## P91 — Elegir ruta de *proctoring* por TRABAJO y por LMS, no por licencia (agregado en el pase 42 del 2026-10-02)

**Este patrón corrige a P90 y al pase 41.** Ese pase dejó la ruta MPL-2.0 como preferible *«porque no arrastra AGPL»*.
Enumeradas las dos superficies, **la ruta MPL cuesta más código** — y **el LMS del cliente manda más que la licencia**.

**La medición que decide**

| | Open edX (`edx-proctoring`) | SEB Server (`seb-server`, `dev-3.0`) |
|---|---|---|
| Pieza | `ProctoringBackendProvider` (clase concreta) | `RemoteProctoringService` (interfaz desnuda) |
| 🔴 **Métodos obligatorios** | 🟢 **0 de 18** | 🔴 **12 de 14** |

> 🔴 **Corrección del pase 43 (2026-10-02): la celda de arriba dice «12 de 14» y son «14 de 14».** No hay clase base
> intermedia (las dos referencias hacen `implements`, no `extends`), la interfaz no tiene ningún `default` ni `static`, y
> `JitsiProctoringService` tiene **exactamente 14 `@Override`**. 🔵 **Y la cantidad de métodos no es la magnitud que se
> cotiza:** son el **22-23 %** de cada clase de referencia. **Para presupuestar, usar P94, no esta tabla.**

| Punto de integración | 🟢 Apache-2.0 (*carve-out*) | ⚠️ MPL-2.0 |
| Registro | *entry point* | 🟢 inyección de Spring, **sin tocar la fábrica** |
| 🟢 **Divulgación obligatoria** | 🟢 ninguna | 🟢 **un valor de enum** (1 archivo *Covered*) |
| Tu código | propietario | 🟢 propietario (archivo nuevo) |

**El árbol de decisión, en orden**

1. 🟢 **Cliente ya en Open edX** → **ruta Open edX.** AGPL ya aceptada, `backends/` Apache-2.0, **0 métodos
   obligatorios**. Es la ruta barata y es la que se cotiza primero.
2. 🟢 **Cliente en Moodle + plugin de SEB Server** → **ruta SEB**: es la **única** combinación del `enum` con
   **`LMS_FULL_INTEGRATION`**.
3. ⚠️ **Cliente en Open edX que quiere producto propio al lado** → **ruta SEB**, pagando los 12 métodos, y 🔴 **avisando
   que con `OPEN_EDX` no hay integración plena**: `COURSE_API` + `SEB_RESTRICTION` y nada más.
4. 🔴 **Cliente en Moodle sin plugin** → **`SEB_RESTRICTION` está comentada en el fuente**. No prometer restricción SEB
   por esta vía.

**Los dos detalles que se escriben en la propuesta y no se descubren en UAT**

- ⚠️ **El validador de SEB cae a `return true`** ante un `ProctoringServerType` desconocido: tu proveedor **pasa sin
  validación de campos**. Hay que escribirla; **es trabajo, no es un bloqueo**.
- 🔴 **`master` de `seb-server` tiene 6 meses y `dev-3.0` commiteó el 2026-10-01** (**gap 87**). Si el entregable se para
  en `v3.0-latest`, **toda esta tabla se re-verifica en ese tag**.

🔴 **Y el expediente va primero, igual que en P90:** el *«monitoreo durante exámenes»* está en el **Anexo III punto 3 del
AI Act** (**2027-12-02**) y Vietnam nombra la *monitorización del comportamiento* en evaluación (**2027-03-01**). **Para
un cliente con operación en los dos lados manda marzo de 2027** (tendencia **156**).

## P90 — *Proctoring* propio dentro de Open edX: un *entry point*, cuatro métodos y el código propio en Apache-2.0 (agregado en el pase 41 del 2026-10-02)

**Este patrón existe porque la acción 3 del pase 40 midió la superficie y el resultado invierte el presupuesto: no se
construye la capa, se implementa una interfaz — y la interfaz está deliberadamente carved-out en permisiva.**

**Piezas**

| Pieza | Licencia | Rol |
|---|---|---|
| [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) **5.2.0** | **AGPL-3.0** el paquete / 🟢 **Apache-2.0 `edx_proctoring/backends/`** | la máquina de estados de examen, las excepciones, la política de revisión y **20 rutas REST** |
| `mereos` (MIT) · `@timadey/proctor` (MIT) · `exam-guard` (ISC) | permisivas | la mitad **cliente**: detección de rostro y mirada en el navegador (ver `agents/top.md`) |
| El backend propio | 🟢 **lo escribe Globant** | el pegamento entre los dos |

**Wiring, con los nombres exactos**

1. **Subclasear `BaseRestProctoringProvider`** (`edx_proctoring/backends/rest.py`, 27 métodos, 8 constructores de URL) —
   **no** `ProctoringBackendProvider` directamente, salvo que el proveedor no sea REST.
2. **Sobreescribir sólo el ciclo de vida del intento.** 🔵 **Y acá está el dato que cambia la estimación: la clase base
   tiene 18 métodos y CERO `@abstractmethod`** — es una base **concreta** con *defaults*, así que un backend mínimo
   implementa lo que usa, típicamente: `register_exam_attempt`, `start_exam_attempt`, `stop_exam_attempt`,
   `on_review_callback`, y `retire_user` si hay obligación de supresión.
3. **Registrar UN *entry point*** en el grupo **`[openedx.proctoring]`** (el paquete ya trae `mock`, `null`, `rpnow4` y
   `software_secure` como ejemplos de referencia). **Es una línea de `setup.py`.**
4. **Lo que NO hay que escribir, porque ya existe:** los **12 modelos** de estado (`ProctoredExam`,
   `ProctoredExamStudentAttempt`, `ProctoredExamStudentAllowance`, `ProctoredExamReviewPolicy` y sus `History`), las
   **20 rutas REST**, y 🟢 **las dos rutas de supresión de datos** (`v1/retire_user/<id>`, `v1/retire_backend_user/<id>`)
   — **el expediente de borrado se cablea, no se construye.**
5. **La mitad cliente se cubre con una de las tres piezas permisivas** de `agents/top.md`, que resuelven visión por
   computadora en el navegador y **no** la integración con estados de examen.

**La nota de licencia, dicha con precisión y sin exagerar**

| Hecho medido | Consecuencia |
|---|---|
| 🟢 `backends/LICENSE.txt` es **Apache-2.0** (11.357 b, sin la palabra «Affero») y `backends/README.txt` lo declara en 174 b | **el directorio donde va el código propio es permisivo**, por decisión explícita del upstream |
| 🔴 El directorio **no es autocontenido**: `rest.py` importa `edx_proctoring.exceptions` y `edx_proctoring.statuses`, que son AGPL | **el backend propio importa módulos AGPL en ejecución** |
| 🟢 Pero esos módulos son **vocabulario, no lógica**: `exceptions.py` = 24 clases / 0 funciones; `statuses.py` = 5 clases / 0 funciones; `constants.py` = 0 clases / 0 funciones / 18 asignaciones | lo que se cruza son **nombres de excepción y valores de estado** |
| ⚠️ Los dos módulos con lógica real (`utils.py`, 26 funciones; `callbacks.py`) los importan **sólo los backends de referencia** | **el backend propio no los necesita** |

⚠️ **Lo que esta KB no puede decidir: si eso hace al backend obra derivada.** Es una pregunta legal. **La tabla de arriba
es el insumo de la consulta, no su respuesta** — y el plugin corre **dentro** de un proceso Open edX que es AGPL completo
de todos modos. 🔵 **Para un cliente que ya es Open edX, la discusión es casi vacía; para uno que quiera vender el backend
como producto separado, la ruta honesta es P89 (MPL-2.0).**

⚠️ **Y el riesgo de mantenimiento, que no cambia con la licencia:** el último release de `edx-proctoring` en PyPI es del
**2025-04-28** — **17 meses** — con `HEAD` del repo en **2026-05-30**. **`HEAD` mide al proyecto, el release mide lo que el
cliente instala** (tendencia 147).

## Patrón base

```
[Plataforma vertical open source: Moodle / Open edX / Kolibri / OpenOLAT]
          ↓  (punto de extensión: AI subsystem plugin · XBlock · LTI 1.3 — NUNCA fork del core)
[Servicio agéntico separado: proceso propio, licencia propia]
          ↓  (MCP / REST)
[Estado del aprendiz + scheduling de retención: tutor-mcp + py-fsrs]
          ↓
[Capa de auditoría: decisiones pedagógicas logueadas + AITutor-EvalKit]
          ↓
[UI conversacional encima de los flujos existentes, no en lugar de ellos]
```

**La regla que no se negocia:** el core copyleft (Moodle GPL-3.0, Open edX / Canvas / Frappe AGPL-3.0) no se modifica. La lógica propietaria vive en un servicio aparte. Esto mantiene el IP del cliente fuera del alcance de GPL/AGPL.

---

## P1 — Tutor adaptativo con retención real (el patrón de base)

**Problema.** Los tutores LLM explican bien y no hacen aprender: no hay modelo de mastery ni scheduling de repaso. Es el gap técnico #5 de `intel/trends.md`.

- **Punto de partida:** [DeepTutor](https://github.com/HKUDS/DeepTutor) (Apache-2.0, 40.6k ★) como workspace de tutoría
- **Estado del aprendiz:** [tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT, Go) — estado durable, misconceptions, metacognición, decisiones auditables
- **Retención:** [py-fsrs](https://github.com/open-spaced-repetition/py-fsrs) (MIT, 499 ★) — scheduling DSR con 21 parámetros optimizables
- **Mastery:** lógica de Bayesian Knowledge Tracing de [OATutor](https://github.com/CAHLR/OATutor) (MIT) + su contenido curado de OpenStax en JSON
  - 🔴 **Corregido en el pase 10:** el **código** de OATutor es MIT y no está en discusión; **el contenido sí**. OATutor declara en su README que su contenido es **CC BY 4.0**, y el archivo `LICENSE` de los bundles de OpenStax en GitHub dice **CC BY-NC-SA** — incluido **Calculus Volume 1**, que OATutor declara curar (verificado 3 de 3 bundles: Calculus, Biology, College Physics). **NonCommercial prohíbe el uso en un entregable facturado y ShareAlike obliga a abrir la derivación.** Antes de usar este contenido en un proyecto pago hay que leer **el campo de licencia de cada ítem JSON** —que es donde OATutor dice que está la licencia real— y producir el manifiesto de **P22**. Ver el **trend 22** y el **gap 17**
- **Evaluación:** [AITutor-EvalKit](https://github.com/kaushal0494/AITutor-EvalKit) (MIT) — mide Mistake Identification, Mistake Location, Providing Guidance, Actionability

**Wiring.** DeepTutor conversa. `tutor-mcp` se monta como servidor MCP y es la **única** fuente de verdad del estado del aprendiz — DeepTutor no guarda mastery en su memoria, la consulta. Cada intento del alumno actualiza BKT (mastery) y alimenta `py-fsrs` (cuándo repasar). `py-fsrs` emite la cola de repaso que DeepTutor usa para abrir la sesión siguiente. Todas las decisiones pedagógicas se loguean con timestamp y razón. `AITutor-EvalKit` corre en CI contra MRBench como gate de regresión pedagógica.

**Tiempo estimado:** 8–10 semanas. **Licencias:** todo MIT/Apache-2.0 → sin fricción.

---

## P2 — Aula multi-agente sobre LMS existente

**Problema.** El cliente ya tiene Moodle con años de contenido y no lo va a reemplazar; quiere experiencia de clase interactiva encima.

- **Base:** Moodle (GPL-3.0) — **AI subsystem nativo**, no hay que construir la integración
- **Experiencia de aula:** [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (MIT, 39.7k ★) — convierte tema o documento en clase multi-agente
- **Pedagogía:** [education-agent-skills](https://github.com/GarethManning/education-agent-skills) (CC BY-SA 4.0 ⚠️) — 165 skills en 20 dominios
- **Contenido interactivo de salida:** [H5P](https://github.com/h5p/h5p-php-library) (GPL-3.0), ya embebible en Moodle

**Wiring.** Un plugin del AI subsystem de Moodle (provider plugin, no fork) expone el curso a OpenMAIC por API. OpenMAIC toma el material del curso y genera la sesión multi-agente; las skills de `education-agent-skills` se cargan como guía pedagógica de los agentes. La salida se materializa como actividades H5P dentro del curso Moodle, así que **persiste en la plataforma que el cliente ya administra** y sobrevive si se apaga el agente. Progreso y engagement vuelven por la API de Moodle.

⚠️ `education-agent-skills` es CC BY-SA 4.0: share-alike. Usar como referencia pedagógica; **revisar con legal antes de empaquetar derivados en un entregable cerrado.**

**Tiempo estimado:** 6–8 semanas. **Nota de procedencia:** OpenMAIC es de Tsinghua — declarar origen temprano si el cliente tiene restricciones de procedencia de software (ver gap #4).

---

## P3 — Tutoría offline-first (LATAM rural, África, Asia del Sur)

**Problema.** Conectividad no confiable, o prohibición de que datos de menores salgan de la red de la escuela. Un tutor que depende de una API remota no sirve.

- **Servidor de conocimiento:** [Project NOMAD](https://github.com/Crosstalk-Solutions/project-nomad) (Apache-2.0, 38.8k ★) — Wikipedia, libros, cursos, mapas en Docker. ~5 GB disco, <1 GB RAM sin AI
- **LMS offline:** [Kolibri](https://github.com/learningequality/kolibri) (MIT, 1.1k ★) — offline-first, licencia permisiva
- **Modelo local:** Ollama como provider; en LATAM, **Latam-GPT** (`latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0`) por contexto cultural en español/portugués — gratuito para instituciones públicas
- **Retención:** `py-fsrs` (MIT) — funciona offline por diseño, no necesita red

**Wiring.** NOMAD y Kolibri corren en un mini-PC en la escuela. Ollama sirve el modelo local en la misma máquina (acá está el techo de RAM: dimensionar por el modelo, no por NOMAD). Kolibri aporta currículo y tracking de progreso; NOMAD el corpus de referencia para RAG. `py-fsrs` mantiene la cola de repaso en SQLite local. **Cero tráfico saliente:** resuelve conectividad y residencia de datos con la misma arquitectura. Sincronización oportunista cuando hay red, no como requisito.

**Tiempo estimado:** 6–8 semanas para el primer sitio, 1–2 semanas por sitio adicional una vez fijada la imagen.

---

## P4 — Evaluación auditable bajo EU AI Act (EMEA)

**Problema.** La corrección automática y la predicción de deserción caen en el **Annex III** del EU AI Act; aplicable **2027-12-02**. La institución debe poder auditar. El entregable no es el modelo: es el expediente de conformidad.

- **Base:** [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (**Apache-2.0**, 444 ★, Suiza) — assessment serio + licencia permisiva + credibilidad DACH. La mejor base de esta KB para el caso
- **Decisiones auditables:** `tutor-mcp` (MIT) — decisiones pedagógicas con traza
- **Gate humano:** patrón de [gradescope-mcp](https://github.com/Yuanpeng-Li/gradescope-mcp) (MIT) — escrituras detrás de confirmación explícita
- **Evidencia de calidad:** **[UnifyingAITutorEvaluation](https://github.com/kaushal0494/UnifyingAITutorEvaluation)** (CC BY-SA 4.0, 32 ★) — taxonomía de **8 dimensiones** + dataset MRBench, NAACL 2025. *Corregido en el pase 4: este es el repo canónico; `AITutor-EvalKit` (MIT, 3 ★) es la implementación LoMTL sobre 4 de esas dimensiones y sirve como el ejecutable.* Para matemática, sumar **[MathTutorBench](https://github.com/eth-lre/mathtutorbench)** (CC BY 4.0, 42 ★, EMNLP 2025 Oral), que trae reward models y leaderboard
- **Evidencia de eficacia adaptativa:** **[pyKT](https://github.com/pykt-team/pykt-toolkit)** (MIT, 441 ★) — curva de mastery de un modelo DLKT publicado y reproducible. *Agregado en el pase 4:* es la diferencia entre documentar cómo decide el sistema y decir "lo decidió el LLM", que no es documentación
- **Modelo:** Ollama on-premise → sin transferencia de datos de menores a terceros

**Wiring.** OpenOLAT conserva la autoridad sobre la nota; el agente **propone** y nunca escribe la calificación final — el gate humano de `gradescope-mcp` es la arquitectura, no una feature opcional. Cada sugerencia se persiste con: input, versión del modelo, prompt, razón, revisor humano y timestamp. `AITutor-EvalKit` corre periódicamente y su salida es el anexo de calidad pedagógica del expediente. El modelo local elimina la transferencia internacional de datos.

**Entregable real:** el expediente de conformidad, no el tutor. Es lo que se factura y lo que el cliente no puede hacer solo.

**Tiempo estimado:** 10–12 semanas. **Ventana comercial:** 14 meses hasta 2027-12-02. Reutilizable para el PL 2.338 de Brasil por el acuerdo Brasil–UE de junio 2026.

> **Corregido en el pase 4 del 2026-09-30 — la ventana decía 26 meses y son 14.** El número anterior se calculó desde una fecha que no corresponde: entre hoy (2026-09-30) y el 2027-12-02 hay **14 meses**, no 26. Con un proyecto de 10–12 semanas eso sigue siendo holgado, pero no es lo que el número sugería.

### Variante de plazos — vender el Artículo 50 antes que el Annex III (agregado en el pase 4)

El **Digital Omnibus on AI** (en vigor 2026-07-27) corrió el Annex III a 2027-12-02, y el titular que le llegó al cliente es "el AI Act se pospuso". **Dos obligaciones no se movieron, y una vence en dos meses:**

| Obligación | Fecha | ¿Se movió con el Omnibus? |
|---|---|---|
| **Artículo 50** — transparencia / divulgar que hay AI | **en vigor desde 2026-08-02** | **No** |
| **Watermarking** de contenido generado | **2026-12-02** | **No** |
| Annex III alto riesgo (evaluación, adaptativo, proctoring, deserción) | 2027-12-02 | Sí, +16 meses |
| Annex I (AI embebida en producto regulado) | 2028-08-02 | Sí |

**Cómo se vende, y el orden importa.** Un cliente europeo con un tutor en producción hoy tiene una obligación **activa** de transparencia y una fecha de diciembre encima, mientras cree que tiene hasta 2027. La entrada es un proyecto chico — **divulgación en la UI, etiquetado de contenido generado, watermarking, y el registro de qué modelo produjo qué** — de 3 a 4 semanas, con urgencia verificable.

**Y no es trabajo desechable:** el registro de procedencia que exige el Artículo 50 (input, modelo, versión, timestamp por cada salida generada) **es el mismo log que el expediente del Annex III va a pedir completo en 2027-12-02**. Se entrega valor en un mes y queda instalada la mitad del proyecto grande. Ése es el argumento, no el miedo a la multa.

---

### Variante Corea del Sur — el mismo expediente, pero exigible ya (agregado en el pase 3)

La **AI Basic Act coreana está en vigor desde el 2026-01-22** y lista la **educación como "high-impact AI"**. Sus tres obligaciones cabeza mapean casi uno a uno contra lo que este patrón ya construye:

| Obligación coreana | Pieza de este patrón que la cumple |
|--------------------|-----------------------------------|
| Explicación con sentido de los resultados a los afectados | El log de decisiones pedagógicas de `tutor-mcp` (razón + timestamp + modelo), expuesto al alumno y al docente |
| Plan de protección del usuario | El archivo de policy del P7 más el expediente de conformidad de este patrón |
| Mecanismo de intervención y supervisión humana | El gate de confirmación explícita antes de cualquier escritura de nota, disciplina o placement |

**Consecuencia operativa:** el expediente que este patrón produce para EU AI Act **se adapta a Corea, no se rediseña**. Y como Corea exige ahora lo que Europa exige en 2027-12-02, conviene invertir el orden: **producir la primera referencia auditada en Corea y portarla a EMEA**, en vez de esperar el deadline europeo. Hay un año de gracia sobre las multas administrativas (hasta ~2027-01-22), pero las obligaciones sustantivas ya aplican.

---

## P5 — Orquestación multi-jurisdicción (APAC, grupos regionales)

**Problema.** Un grupo educativo que opera en China + Japón + India + Singapur enfrenta cuatro regímenes incompatibles. Una política hardcodeada por país no escala.

- **Orquestación:** LangGraph (MIT) con **nodos de política por jurisdicción**
- **Tutoría:** DeepTutor (Apache-2.0) o OpenMAIC (MIT) como ejecutor
- **Estado:** `tutor-mcp` (MIT), particionado por jurisdicción
- **Modelo:** provider intercambiable por región (Ollama on-premise donde la residencia de datos lo exige)

**Wiring.** El grafo resuelve la jurisdicción del alumno **antes** de cualquier llamada al modelo. Cada nodo de política decide: qué provider se puede usar, si se permite decisión automática, qué se puede loguear y dónde se almacena. El ejecutor de tutoría es el mismo en todas las regiones — **la política es datos, no código**, así que agregar un país es una entrada de configuración y un test, no un fork. Almacenamiento particionado por jurisdicción desde el día uno; retrofitearlo después es una migración dolorosa.

**Tiempo estimado:** 12–14 semanas.

---

## P6 — AI literacy a escala de sistema educativo (LATAM, programa de ministerio)

**Problema.** 13 de los 19 países de LAC no enseñan adopción temprana de AI en escuelas, con cuello de botella declarado en formación avanzada. No es un problema de producto: es un programa nacional. Comprador: ministerio. Financiador habitual: BID.

- **Material técnico:** [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) (Apache-2.0, 105.8k ★) y [minimind](https://github.com/jingyaogong/minimind) (Apache-2.0, 63k ★ — LLM de 64M entrenado en ~2h en hardware de consumo)
- **Generación de currículo localizado:** [Educhain](https://github.com/satvik314/educhain) (MIT, 389 ★) — MCQs, lesson plans con 8 enfoques pedagógicos, flashcards, desde PDF/YouTube/URL
- **Entrega:** Kolibri (MIT) para escuelas con conectividad intermitente, Chamilo (GPL-3.0) para las que tienen red — el más liviano de self-hostear, y con adopción real en LATAM
- **Modelo:** Latam-GPT para español/portugués con contexto cultural regional
- **Marco de referencia:** borrador de AI Literacy Framework de la Comisión Europea + OCDE (aval del G7) — alinearse a un estándar existente en lugar de inventar uno

**Wiring.** `minimind` da el laboratorio ("entrená tu propio modelo en dos horas") que convierte AI de abstracción en ejercicio. `Educhain` + Latam-GPT generan las variantes localizadas de currículo y evaluación por país e idioma — es el paso que hace viable cubrir 13 países sin escribir 13 currículos. Kolibri/Chamilo entregan y trackean. La formación docente es un track paralelo y **es el que decide si el programa funciona**: sin docentes formados, la plataforma queda sin uso.

**Tiempo estimado:** 14–16 semanas para el primer país (currículo + formación + plataforma), 4–6 semanas por país adicional usando el pipeline de localización.

**Por qué es defendible:** Latam-GPT es gratuito, regional y entrenado en contexto propio. Ningún competidor global puede ofrecer soberanía de modelo en español/portugués rápido. Y no hay incumbente open source educativo en LATAM (gap #2).

### Variante APAC — India, currículo obligatorio desde Class 3, ciclo 2026-27

*Agregada en la segunda pasada del 2026-09-30.* El mismo patrón, con el deadline más grande y más cercano de la KB: **India hizo AI y pensamiento computacional obligatorios desde 3.º grado a partir del ciclo 2026-27**, y es —con China— uno de los dos únicos países del mundo con currículo nacional de AI obligatorio.

Tres cambios respecto de la versión LATAM:

1. **El material sube de nivel.** Para docentes y secundaria, [ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) (MIT, 62.1k ★) aporta las 20 fases ya secuenciadas; `minimind` sigue siendo el laboratorio de primaria/secundaria baja. ⚠️ **No usar `tiny-llm` acá**: es Apache-2.0 y excelente, pero corre sobre MLX (macOS ARM64) y ningún sistema escolar indio va a tener hardware Apple.
2. **El stack de entrega es nativo.** `Educhain` es MIT y **de India** (Build Fast with AI) para generación multilingüe, sobre [Frappe LMS](https://github.com/frappe/lms) (AGPL-3.0) u [OpenEduCat](https://github.com/openeducat/openeducat_erp) (LGPL-3.0) — los dos de stack indio, con el agente afuera por las razones de licencia de siempre.
3. **El multiplicador es el idioma, no el país.** En LATAM se localiza a 13 países en dos idiomas; en India a un país en decenas de idiomas. El pipeline de localización de `Educhain` es la pieza crítica y hay que dimensionarla desde el día uno, no al final.

**Tiempo estimado:** 16–20 semanas para el primer estado indio (el volumen de localización manda), 4–6 semanas por estado adicional. **Comprador:** gobierno estatal o grupo educativo de escala, no una escuela.

---

## P7 — Policy pack de cumplimiento distrital (North America; Ohio y Virginia ya vencieron, Oklahoma vence 2027-28)

*Agregado en la segunda pasada del 2026-09-30. Ataca la tendencia 8 de `intel/trends.md`.*

**Problema.** Oklahoma S.B. 1734 obliga a **cada distrito** a tener política de AI **escrita** antes del ciclo escolar **2027-28**, prohíbe que la AI sea base primaria de calificación, disciplina o placement, y exige uso human-in-the-loop dirigido por el docente. Maryland S.B. 720 exige además un **AI coordinator** por distrito. Y **sólo 18% de los docentes de EE. UU. tiene hoy alguna política escrita**. El distrito no necesita un tutor: necesita demostrar cumplimiento, y no tiene cómo.

Lo que hace este patrón distinto de una consultoría de políticas: la ley restringe **arquitectura**, no redacción. Un documento que dice "hay supervisión humana" sin el gate técnico que la fuerza no es cumplimiento, es una declaración. Esto entrega las dos mitades.

- **Host / sistema de registro:** [Moodle](https://github.com/moodle/moodle) (GPL-3.0) vía plugin del **AI subsystem** — no tocar el core. Si el distrito usa Canvas, [Canvas LMS](https://github.com/instructure/canvas-lms) (AGPL-3.0) por **LTI 1.3**, nunca fork
- **Gate de decisiones auditables:** [tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT, Go) — estado durable del aprendiz y **decisiones pedagógicas auditables con razón y timestamp**. Es la pieza que convierte "hay human-in-the-loop" en un registro consultable
- **Gate de escritura en grading:** [gradescope-mcp](https://github.com/Yuanpeng-Li/gradescope-mcp) (MIT) — 34 tools sobre Gradescope con **escrituras detrás de confirmación explícita**. Ver el gap 6: el grading open source no existe, así que se orquesta el incumbente
- **Evidencia de calidad pedagógica:** [AITutor-EvalKit](https://github.com/kaushal0494/AITutor-EvalKit) (MIT) — 4 dimensiones sobre MRBench, corriendo en CI
- **Formación docente (lo que Maryland paga):** [ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) (MIT, 62.1k ★, 523 lecciones en 20 fases) como cantera de currículum, recortado a un track docente corto
- **Currículo AI para créditos de CS (GA, MS):** [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) (Apache-2.0) y [minimind](https://github.com/jingyaogong/minimind) (Apache-2.0)

**Wiring.** La política escrita se compila a **configuración, no a PDF**: un archivo de policy por estado (qué decisiones no puede tomar la AI, qué requiere confirmación docente, qué se retiene y por cuánto) que el plugin del AI subsystem lee en cada invocación. Toda llamada del alumno o del docente pasa por `tutor-mcp`, que registra decisión, razón, modelo y timestamp. Ninguna escritura sobre nota, disciplina o placement sale sin confirmación humana explícita: `gradescope-mcp` ya está diseñado así, y en Moodle el placement queda detrás del mismo gate. `AITutor-EvalKit` corre en CI y su salida es un anexo del expediente. El entregable final son cuatro piezas: **política escrita + configuración que la fuerza + registro de auditoría + evidencia de evaluación**.

**Actualizado en el pase 3 del 2026-09-30 — el primer deadline ya venció, así que el patrón cambia de tiempo verbal.** Este patrón se escribió contra un plazo futuro (Oklahoma, ciclo 2027-28). Resulta que **ya venció uno y hay dinero asignado en otro**:

- **Ohio** fue el primer estado en obligar a *todos* sus distritos a adoptar política de AI, con plazo **2026-07-01 — hace tres meses**. El Ohio DEW publicó un modelo de política (dic-2025) que los distritos podían adoptar o reemplazar por una propia alineada.
- **Virginia** (SB 394 / HB 1186, vigentes **2026-07-01**): el VDOE desarrolla guía estatal y los school boards locales deben adoptar políticas consistentes, con acuerdos de privacidad y salvaguardas contra sesgo. Y trae el **AIS Innovation in Education Pilot Program con USD 2 millones en el presupuesto FY 2027–2028**, priorizando formación docente, privacidad y equidad.
- **35+ estados** ya tienen guía oficial de AI de su Department of Education (junio 2026).

**Cómo entrar ahora, que es distinto de cómo se entraba antes.** Contra un deadline futuro se vende "te ayudo a cumplir". Contra uno vencido se vende algo más fuerte: **ya adoptaron un documento, y casi con certeza no adoptaron el gate técnico que el documento declara** — a nivel nacional sólo 18% de los docentes reporta tener política escrita, y el camino de menor esfuerzo para un distrito apurado fue copiar el modelo estatal. Entonces la conversación de apertura no es un pitch, es una **auditoría de brecha**: tomar la política que el distrito ya adoptó, y mostrar cuáles de sus cláusulas no están forzadas por ninguna configuración. Cada cláusula sin gate es una línea de alcance.

Ohio es además el **mercado de referencia** de este patrón: es el único estado donde se puede preguntar qué pasó después del deadline, y el pilot program de Virginia es una de las pocas partidas de dinero público con monto que la KB tiene identificada.

**Por qué escala.** El mismo pack se reimplanta distrito por distrito cambiando un archivo de policy por estado. California AB 1159 (prohíbe entrenar modelos con datos de alumnos) se expresa como una bandera de retención; Oklahoma y Maryland como gates de decisión; Idaho S.B. 1227 agrega los requisitos de AI literacy y formación, que ya están cubiertos por el track docente. Es el trabajo más replicable de la KB, con un mandato legal con fecha detrás.

**Tiempo estimado:** 6–8 semanas el primer distrito; 2–3 semanas cada distrito siguiente del mismo estado. **Licencias:** el agente y los gates son MIT; Moodle queda intacto detrás de su punto de extensión.

---

## P8 — Fábrica de lecciones en la voz del docente (teacher-facing, el ángulo menos disputado)

*Agregado en la tercera pasada del 2026-09-30. Ataca el gap 8 de `intel/trends.md`.*

**Problema.** Todo el mercado construye tutores para *alumnos*. El comprador que menos resistencia opone es el **docente**, porque el dolor es medible: quien usa AI semanalmente ahorra **5,9 horas por semana** (Gallup). Pero la capa teacher-facing es propietaria entera — MagicSchool, Brisk, Diffit, Curipod, Eduaide.AI, SchoolAI — y un distrito que quiere esas capacidades sin SaaS por alumno no tiene de dónde partir. Y el rechazo docente no es a la AI: es a que genere material que no suena a ellos.

- **Motor:** [Claw-ED](https://github.com/SirhanMacx/Claw-ED) (MIT, 59 ★, Python) — se apunta a una carpeta de lecciones viejas del docente, **infiere su estilo**, y emite el bundle completo: DOCX de docente, DOCX de alumno y PPTX de slides, más versiones diferenciadas, juegos y evaluaciones. 48+ tools, alineación a estándares estatales, cualquier provider LLM. Interfaz CLI + bot de Telegram con la misma memoria
- **Pedagogía como guía:** [education-agent-skills](https://github.com/GarethManning/education-agent-skills) (CC BY-SA 4.0 ⚠️) — 165 skills evidence-grounded en 20 dominios
- **Destino del material:** [Moodle](https://github.com/moodle/moodle) (GPL-3.0) vía plugin del AI subsystem, materializando salida como actividades [H5P](https://github.com/h5p/h5p-php-library) cuando conviene que viva en el curso
- **Evaluación y corrección:** [gradescope-mcp](https://github.com/Yuanpeng-Li/gradescope-mcp) (MIT) si el cliente ya usa Gradescope; si no, ver el gap 9 y **no prometer grading automático**
- **Gate de política:** [tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT, Go) para registrar qué se generó, con qué modelo y quién lo aprobó

**Wiring.** Claw-ED corre **local-first**, que es la mitad del argumento: el material histórico del docente —su propiedad intelectual— no sale de la máquina ni de la red de la escuela. Se lo apunta a un corpus de lecciones por docente (o por departamento, si se quiere una voz institucional). Las skills de `education-agent-skills` se cargan como guía pedagógica para que el bundle no sea sólo estilísticamente fiel sino didácticamente defendible. La salida va a un directorio de revisión: **nada se publica al alumno sin aprobación explícita del docente**, y esa aprobación se registra vía `tutor-mcp` con timestamp y autor. Recién aprobado, un plugin del AI subsystem de Moodle sube el material al curso (H5P para lo interactivo, DOCX/PPTX como recurso). El bot de Telegram es el canal de baja fricción: el docente pide algo desde el celular y recibe los archivos en el chat.

**Por qué este patrón se vende distinto.** No hay que convencer a nadie de que un agente enseñe. El agente **no toca al alumno**: produce borradores para un docente que decide. Eso lo saca del alcance de las restricciones de alto impacto de Oklahoma, Maryland, del Annex III europeo y de la AI Basic Act coreana, porque no hay decisión automatizada sobre el estudiante. Es el patrón con **menos superficie regulatoria y el ROI más fácil de medir** (horas docentes) de toda la KB — el lugar natural para un primer piloto que después habilita los patrones de tutoría.

⚠️ **Riesgos a declarar.** Claw-ED tiene **59 ★ y es de un solo autor**: verificar continuidad antes de comprometerlo en un contrato largo, y prever el costo de mantenerlo forkeado. `education-agent-skills` es **CC BY-SA 4.0** (share-alike): usable como guía, revisar con legal antes de empaquetar derivados en un entregable cerrado.

**Tiempo estimado:** 3–5 semanas — el más corto de la KB, porque no hay plataforma que desplegar. **Licencias:** Claw-ED MIT; la advertencia está en las skills, no en el motor.

---

## P9 — Agente adentro del SIS, sin fricción de licencia (lado administrativo)

*Agregado en la tercera pasada del 2026-09-30. Es el patrón que el gap 7 declaraba imposible hasta hoy.*

**Problema.** Los datos que más valen para un agente —matrícula, asistencia, legajos, comunicación con familias— viven en el SIS, y hasta esta pasada la KB sostenía que el agente **siempre** tenía que quedar afuera, porque todo SIS open source era copyleft. Con [GegoK12](https://github.com/Gego-K12/gegok12) (**MIT**, 54 ★, 97 forks, último commit 2026-09-23, PHP 8.4 + Laravel 12, **con sistema de plugins**) eso dejó de ser cierto.

- **Base:** GegoK12 (MIT) — core de 26 módulos: alumnos, admisiones, asistencia, tareas, biblioteca, staff, avisos, comunicación con padres. API-first, instalador visual o Docker
- **Punto de extensión:** su propio sistema de plugins — referencia: [`Plugin-Hello-Teacher`](https://github.com/Gego-K12/Plugin-Hello-Teacher)
- **Gate de decisiones auditables:** [tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT, Go) — decisiones con razón y timestamp
- **Capa de conformidad:** el mismo archivo de policy por jurisdicción del **P7**
- **Si el alcance incluye tutoría:** [DeepTutor](https://github.com/HKUDS/DeepTutor) (Apache-2.0) contra el estado del alumno que el SIS ya tiene

**Wiring.** El agente se empaqueta como **plugin de GegoK12**, corriendo en el mismo proceso Laravel y leyendo el modelo de datos directo, sin capa de sincronización, sin ETL y sin un segundo sistema de identidad. Eso es lo que la arquitectura de sidecar obligaba a construir y mantener. Como el core es MIT, **el plugin puede ser propietario del cliente sin contaminar nada** — MIT no impone share-alike. Los casos de uso de arranque son los administrativos aburridos y de ROI inmediato: triage de admisiones, seguimiento de ausentismo con alerta temprana, borradores de comunicación a familias en su idioma. Toda escritura sobre un registro de alumno pasa por `tutor-mcp` y queda auditada; las decisiones de alto impacto quedan detrás de confirmación humana, igual que en P7.

**Cuándo NO usar este patrón — leer antes de proponerlo.** Tres condiciones lo descartan:

1. **El cliente ya tiene un SIS.** Nadie migra de SIS por poder meter un agente adentro: el SIS es el sistema de registro de la institución y la migración es un proyecto en sí mismo. Esto sirve para **implementaciones nuevas** o instituciones que ya iban a cambiar.
2. **El alcance necesita exámenes o cobranzas.** Son **módulos Pro pagos** (USD 100–250 cada uno). Se pueden comprar —licencia lifetime por dominio con fuente incluido— pero hay que **cotizarlo de entrada**. Descubrirlo a mitad del proyecto es el modo de falla obvio.
3. **El cliente exige madurez de proyecto.** 54 ★ y un solo vendor (GegoSoft) es riesgo de continuidad. Para una institución grande, OpenEduCat (LGPL-3.0, más adoptado) con el agente afuera sigue siendo la opción conservadora, y está bien elegirla.

**Tiempo estimado:** 5–7 semanas para el primer caso administrativo sobre una instalación nueva. **Licencias:** core MIT + plugin propietario del cliente = la combinación más limpia que la KB puede ofrecer en el lado administrativo. Contrastar con el resto de la capa SIS (RosarioSIS GPL-2.0, openSIS GPL, OpenEduCat LGPL-3.0), donde el agente va afuera.

---

## P10 — Probar que el tutor enseña, no que responde (agregado en el pase 4, transversal a todas las regiones)

**Problema.** Todos los patrones anteriores construyen un tutor. **Ninguno mide si enseña.** Es el hueco que aparece en cuanto el comprador es institucional: un rector, un ministerio o un inspector no compra "el alumno conversó con la AI", compra evidencia de aprendizaje. Y ahora hay tres compradores distintos pidiendo lo mismo por razones distintas:

- **EMEA:** el expediente del Annex III (2027-12-02) exige documentar cómo decide el sistema.
- **North America:** los estatutos de Oklahoma, Maryland e Idaho prohíben que la AI sea base primaria de decisiones de alto impacto — hay que mostrar en qué se basó.
- **LATAM:** **65% de los estudiantes teme que la AI vuelva el aprendizaje superficial** (DEC LATAM 2026, 30.000+ respuestas). Acá el comprador de la evidencia es la propia comunidad educativa.

Hasta este pase la KB no tenía con qué responder. Ahora sí, y las piezas son MIT o CC.

**Las tres preguntas son distintas y cada una tiene su repo:**

| Pregunta | Pieza | Licencia | Stars |
|----------|-------|----------|-------|
| ¿Qué sabe el alumno ahora? | **[pyKT](https://github.com/pykt-team/pykt-toolkit)** — 10+ modelos DLKT sobre 7+ datasets | MIT ✅ | 441 |
| ¿Cuándo hay que volver a preguntárselo? | **[py-fsrs](https://github.com/open-spaced-repetition/py-fsrs)** — scheduler DSR, 21 parámetros | MIT ✅ | 499 |
| ¿El agente respondió *pedagógicamente bien*? | **[MathTutorBench](https://github.com/eth-lre/mathtutorbench)** (reward models + leaderboard) y **[UnifyingAITutorEvaluation](https://github.com/kaushal0494/UnifyingAITutorEvaluation)** (8 dimensiones + MRBench) | CC BY 4.0 / CC BY-SA 4.0 ⚠️ | 42 / 32 |

**Wiring concreto.**

1. **Instrumentar el tutor existente** — el de P1, P2 o P3, da igual cuál. Cada turno emite un evento `(alumno, skill, ítem, correcto/incorrecto, timestamp)`. Sin esto no hay nada que medir, y es el 80% del trabajo real.
2. **`pyKT` como servicio de estado, offline primero.** Entrenar un modelo DLKT (empezar por `simpleKT` o `AKT`, que son las baselines fuertes del propio toolkit) sobre el histórico del cliente. Exponerlo como un servicio con un endpoint `mastery(alumno, skill) → probabilidad`. **Correrlo en batch antes que en línea:** la primera versión no necesita estar en el loop del agente, necesita producir la curva de mastery del cohort.
3. **El agente consulta antes de decidir qué preguntar.** Acá está el hueco que el gap 5 declara abierto: **no existe `pyKT` detrás de MCP**, así que esta pieza se construye. Es un servidor MCP fino con una tool `get_mastery` y una tool `record_attempt`, siguiendo el diseño de `tutor-mcp` (MIT, 42 ★, Go) pero con un modelo DLKT entrenable atrás en vez de su BKT propio. **Es la pieza de IP del patrón** — chica, y la única que no está hecha.
4. **`py-fsrs` programa el repaso** con la probabilidad de mastery de `pyKT` como señal de dificultad inicial, en vez del default.
5. **El benchmark corre en CI, no una vez.** Los diálogos del tutor se puntúan contra las 8 dimensiones de MRBench (y contra MathTutorBench si el dominio es matemática) **en cada cambio de prompt o de modelo**. Un cambio de prompt que sube la satisfacción y baja la calidad pedagógica es exactamente el fallo que este paso atrapa, y es invisible sin él.
6. **La salida es un reporte, y es el entregable.** Curva de mastery por skill y por cohorte, retención a 30/60/90 días, y puntaje pedagógico por dimensión con su evolución. Eso es lo que se le muestra al rector, al ministerio y al inspector.

**Lo que hay que construir vs. lo que se toma hecho.** Se toman hechos `pyKT`, `py-fsrs` y los dos benchmarks. Se construye el servidor MCP del paso 3 y el reporte del paso 6. **Esa proporción es el argumento comercial:** el cliente paga integración y evidencia, no investigación.

⚠️ **La trampa de licencia, y es la que muerde en este patrón justamente.** `pyKT` y `py-fsrs` son MIT, sin problema. Pero **MRBench es CC BY-SA 4.0**, y el uso natural acá es *derivar un benchmark propio con los diálogos del cliente* — que es exactamente lo que dispara el share-alike. **MathTutorBench es CC BY 4.0** (sólo atribución) y no tiene ese problema. Decidirlo antes de empezar: o el benchmark derivado se publica bajo la misma licencia, o se construye sobre MathTutorBench, o se escribe una taxonomía propia inspirada en las 8 dimensiones sin reusar el dataset. Las tres son defendibles; descubrirlo al final no.

**Tiempo estimado:** 6–8 semanas sobre un tutor ya desplegado (la instrumentación del paso 1 domina). **Dónde venderlo primero:** EMEA como anexo de calidad del expediente de P4; LATAM como respuesta directa al 65%; North America como la evidencia que los estatutos de decisiones de alto impacto obligan a tener.

**Por qué es el patrón con menos competencia de esta KB:** los benchmarks están premiados en EMNLP 2025 y NAACL 2025 y tienen 42 y 32 estrellas. **La academia los produjo y la industria no los adoptó.** Operacionalizar lo que ya está publicado y validado es un trabajo mucho más barato y más defendible que construir un evaluador propio, y hoy no lo está haciendo casi nadie.

---

## P11 — Gate de seguridad pedagógica (agregado en el pase 5; transversal, se vende primero en EMEA y North America)

**Problema.** P10 mide si el tutor *enseña bien*. Este mide si **enseña mal siendo amable**, que es un modo de falla distinto y el que un docente reconoce al instante: el tutor revela la respuesta antes de tiempo, le da la razón al alumno que insiste con una idea equivocada, o abandona el andamiaje cuando el alumno se frustra. Un tutor con 95% de exactitud puede fallar en todas esas y **los benchmarks de exactitud no lo ven**.

**El dato que justifica la arquitectura, y es lo que lo hace vendible.** Según ELBench (9 modelos), el módulo de *safety* está **anti-correlacionado con el de enseñanza práctica**: los modelos más seguros enseñan peor. Si se sostiene, **no existe el modelo que resuelva las dos cosas eligiéndolo bien** — hay que componer. Eso convierte "poné un gate de seguridad" de preferencia de arquitecto en requisito justificado por evidencia. Y de EduGuardBench (14 modelos): el modo de falla dominante es la **incompetencia**, no la toxicidad — o sea que el guardrail genérico de contenido que el cliente ya tiene **no cubre este riesgo**.

**Las piezas, todas verificadas y las dos centrales MIT:**

| Rol | Pieza | Licencia | Stars |
|-----|-------|----------|-------|
| Taxonomía de daño pedagógico + dataset de evaluación | **[SafeTutors](https://github.com/RadiantCrystal/SafeTutors)** — 11 dimensiones, 48 sub-riesgos, 5.955 instancias (3.135 single-turn + 2.820 multi-turn), matemática/física/química | MIT ✅ | 0 |
| Fidelidad pedagógica transversal a materia | **[EduBench](https://github.com/ybai-nlp/EduBench)** — 9 contextos, 4.000+ situaciones, 12 dimensiones, incluye 4 escenarios docentes | MIT ✅ | 29 |
| Seguridad adversaria del modelo como docente | **[EduGuardBench](https://github.com/YL1N/EduGuardBench)** — SATA + prompts adversarios de mala conducta académica | ⚠️ sin licencia | 4 |
| Motor de scoring por rúbrica ponderada | **[rubric](https://github.com/paper-instruments/rubric)** — criterio por criterio, single-pass u holístico, Pydantic | MIT ✅ | 75 |

**Wiring concreto.**

1. **Mapear las 11 dimensiones de daño de SafeTutors al contexto del cliente.** No se usan las 11 en producción: se eligen las que aplican al nivel y la materia, y se escribe para cada una qué cuenta como falla *en este despliegue*. Es una hora de trabajo con el equipo pedagógico del cliente y es el paso que hace que el resto signifique algo.
2. **Cargar el dataset como suite de regresión.** Los 3.135 escenarios single-turn corren rápido; los 2.820 multi-turn son los que atrapan el abandono de andamiaje, que por definición no aparece en un solo turno. Correr los dos.
3. **Scoring con `rubric` (MIT)** y no con un prompt de juicio ad hoc: rúbricas ponderadas explícitas, salida validada con Pydantic, reproducible. Que el criterio esté versionado en el repo es lo que lo vuelve auditable.
4. **`EduBench` para lo que SafeTutors no cubre** — es transversal a materia y trae los cuatro escenarios docentes, así que cubre el caso teacher-facing (P8) que SafeTutors no mira.
5. **El gate en el pipeline, con umbral que bloquea.** Corre en CI en cada cambio de prompt, de modelo o de temperatura. **Un cambio que sube la satisfacción del alumno y baja el puntaje de sycophancy es el fallo exacto que este gate atrapa** — y es el más probable, porque optimizar satisfacción es optimizar adulación.
6. **En runtime, el gate va aparte del modelo docente.** Por la anti-correlación: el modelo que enseña bien no es el que hay que usar para juzgar si se pasó de amable. Modelo docente + evaluador separado, y el evaluador puede ser más chico y más barato.
7. **La salida es el anexo de riesgos.** Puntaje por dimensión de daño, evolución entre releases, y los casos que fallaron con su transcripción. **En un expediente de Annex III eso no es QA: es el análisis de riesgos.**

**Lo que se toma hecho vs. lo que se construye.** Se toman SafeTutors, EduBench y `rubric`. Se construye el mapeo del paso 1, la integración en CI del paso 5 y el reporte del paso 7. **Proporción deliberadamente parecida a P10:** el cliente paga integración y evidencia.

⚠️ **Licencias.** `SafeTutors`, `EduBench` y `rubric` son **MIT** — es la primera vez en esta KB que un patrón de evaluación no arrastra fricción de Creative Commons. **`EduGuardBench` no declara licencia**: usarlo para leer y diseñar, **no** incorporar sus datasets a un entregable. Si hace falta el ángulo adversario dentro del entregable, escribir prompts propios siguiendo su estructura.

⚠️ **Y lo que hay que verificar antes de ponerlo en una slide:** los hallazgos de anti-correlación (ELBench) y de incompetencia dominante (EduGuardBench) **no pudieron verificarse en la fuente primaria** — `arxiv.org` y `ojs.aaai.org` están bloqueados en el entorno donde se investigó. Son el argumento central del patrón: abrir los papers antes de presentarlos.

**Tiempo estimado:** 3–4 semanas sobre un tutor ya desplegado e instrumentado; 5–6 si hay que instrumentarlo. **Dónde venderlo primero:** **EMEA**, como el anexo de riesgos del expediente Annex III de P4 (llegar con la taxonomía de 11 dimensiones ya mapeada gana contra un integrador que llega con "medimos accuracy"); **North America**, como la auditoría que los estatutos de decisiones de alto impacto obligan a tener; **LATAM**, ver P13.

---

## P12 — `pyBKT` detrás de MCP: la pieza que cinco proyectos intentaron y ninguno terminó (agregado en el pase 5)

**Problema.** El gap 5 de esta KB lleva cinco pasadas diciendo que nadie cosió bien knowledge tracing con agentes LLM. El pase 5 encontró que **cinco servidores MCP independientes** exponen mastery a un agente —`knowledge-graph-mcp`, `student-progress-tracker`, `tejpalvirk/student`, `knowledge-forest-mcp`, `Teacher-MCP`— y que **ninguno usa una librería de knowledge tracing entrenable**: todos implementan su propia heurística (SM-2, fórmulas de pesos fijas, reglas de evidencia). Los tres más grandes suman **3 estrellas y 23 commits**.

**Por qué eso es una oportunidad y no una categoría saturada.** Cinco autores sin relación llegaron al mismo patrón en la misma ventana: el problema está validado sin que haya que evangelizarlo. Y el trabajo dejó de ser inventar el patrón — pasó a ser **hacerlo bien una vez**, con una librería publicada atrás en vez de una heurística.

**La pieza central, y es la novedad del pase 5:**

| Rol | Pieza | Licencia | Stars | Nota |
|-----|-------|----------|-------|------|
| Modelo de mastery **interpretable** | **[pyBKT](https://github.com/CAHLR/pyBKT)** — BKT y variantes, parámetros por alumno y por ítem. EDM 2021, CAHLR/UC Berkeley | MIT ✅ | **281** | **Procedencia estadounidense** — la respuesta al gap 4 |
| Modelo de mastery **potente** | **[pyKT](https://github.com/pykt-team/pykt-toolkit)** — 10+ modelos DLKT sobre PyTorch | MIT ✅ | 441 | APAC (Jinan University) |
| Scheduling de repaso | **[py-fsrs](https://github.com/open-spaced-repetition/py-fsrs)** | MIT ✅ | 499 | — |
| Referencia de diseño MCP | **[tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp)** — BKT propio detrás de MCP, en Go | MIT ✅ | 42 | Copiar la forma de las tools, no el modelo |

**Wiring concreto.**

1. **Elegir el modelo según el cliente, y decirlo explícito.** **`pyBKT` si hay regulador o licitación**: BKT bayesiano es menos potente que DLKT y **mucho más fácil de defender** cuando preguntan por qué el sistema decidió lo que decidió — los parámetros tienen significado (prior, learn, guess, slip) y se pueden mostrar en una tabla. **`pyKT` si el cliente tiene volumen de datos y quiere el techo más alto.** Para un primer engagement regulado, pyBKT.
2. **Entrenar offline sobre el histórico del cliente.** pyBKT necesita secuencias `(alumno, skill, correcto/incorrecto)`; casi cualquier LMS las tiene en la tabla de intentos. Empezar con el modelo base, después las variantes que individualizan por alumno o por ítem.
3. **Servidor MCP fino, y es la IP del patrón.** Dos tools y nada más al principio: `get_mastery(alumno, skill) → probabilidad` y `record_attempt(alumno, skill, resultado)`. Seguir la forma de `tutor-mcp` (que ya resolvió el diseño de las tools) con **pyBKT atrás en vez de un BKT propio**. FastMCP en Python es el camino corto porque pyBKT es Python.
4. **El agente consulta antes de decidir qué preguntar, no después.** Esto es todo el punto: el tutor deja de elegir el próximo ítem por heurística de prompt y lo elige por probabilidad de mastery. Es la diferencia entre un chatbot con memoria y un sistema adaptativo.
5. **`py-fsrs` toma la probabilidad de pyBKT como dificultad inicial** en vez del default, y programa el repaso.
6. **Cerrar el loop con P11 o P10.** El mastery es la métrica de resultado; el gate pedagógico es la métrica de proceso. Juntas son el reporte que compra una institución.

**Lo que se construye:** el servidor MCP del paso 3, y es chico — dos tools sobre una librería que ya funciona. **Lo que se toma hecho:** el modelo (pyBKT/pyKT), el scheduler (py-fsrs) y el diseño de las tools (tutor-mcp). **Eso es el argumento de estimación: semanas, no trimestres, y ninguna investigación.**

⚠️ **Verificado de primera mano en el pase 5:** `pyKT` sigue sin mencionar MCP ni interfaz de serving en su documentación (441 ★, 811 commits). El hueco sigue abierto — pero conviene re-verificarlo cada ciclo, porque con cinco proyectos empujando en esa dirección es el gap con más probabilidad de cerrarse solo.

**Tiempo estimado:** 4–6 semanas (paso 2 y paso 3 dominan; el paso 2 depende de cuán limpia esté la tabla de intentos del cliente). **Dónde venderlo:** como el motor adaptativo de P1, y como el sustrato de evidencia de P10. **Para un cliente con restricción de procedencia de software, `pyBKT` es la única ruta** — ver gap 4.

---

## P13 — Cerrar la tijera de LATAM: 73,5% enseña con AI, 9% puede medirla (agregado en el pase 5, LATAM)

**Problema, con fuente.** UNESCO IESALC encuestó **200 instituciones de educación superior en 19 países** de América Latina y el Caribe (campo agosto–octubre 2025). **73,5% implementa AI en enseñanza y aprendizaje. 9,0% tiene un mecanismo formal de evaluación. 18,5% tiene política institucional transversal. 26,0% tiene estrategia formal.**

**64 puntos entre enseñar con AI y poder medirla** — la tijera más ancha que esta KB documentó en cualquier región.

**Por qué este patrón y no "construyamos un tutor LATAM".** El gap 2 dice que LATAM no produce tutores con tracción, y la conclusión tentadora es construir uno. Es la peor opción: competir contra DeepTutor (40.6k ★) y OpenMAIC (39.7k ★) con un producto nuevo. **Cerrar el gap de medición, en cambio, es integrar cuatro librerías MIT que ya existen** — y el comprador ya declaró que le falta.

**Las piezas:** `EduBench` (MIT, transversal a materia — importa porque las instituciones LATAM no son sólo STEM), `SafeTutors` (MIT, 11 dimensiones de daño), `pyBKT` (MIT, mastery interpretable **y de procedencia no-china**, que en licitación pública de la región importa), `rubric` (MIT, scoring). Todo el stack es MIT: **no hay conversación de legal que frene el proyecto.**

**Wiring concreto.**

1. **Entrar por el presupuesto que ya existe.** ⚠️ **Sólo 8,0% de las instituciones tiene presupuesto asignado a AI.** Este proyecto **no se vende como línea nueva de gasto y va a fracasar si se intenta.** Se vende contra **acreditación, aseguramiento de la calidad, cumplimiento o reporte a ministerio** — rubros donde "mecanismo formal de evaluación" ya tiene partida y ya tiene un dueño con incentivo.
2. **Empezar por el inventario, no por el software.** Qué herramientas AI se están usando ya en la institución, en qué cursos, con qué autorización. En una institución del 73,5% que no está en el 18,5% con política, **nadie tiene esa lista** — y producirla es un entregable valioso en sí mismo, cobrable, y de dos semanas.
3. **Instrumentar un piloto, no la institución entera.** Dos o tres cursos con volumen de intentos en el LMS (Moodle o Chamilo, que son los que dominan la región). Emitir eventos `(alumno, skill, ítem, resultado)`.
4. **`pyBKT` sobre el histórico de esos cursos** → curva de mastery por cohorte. Primera evidencia cuantitativa que la institución tiene de que la AI ayuda o no.
5. **`EduBench` + `SafeTutors` sobre el tutor en uso** — incluso si es una herramienta de tercero. Medir lo que ya se usa, en vez de proponer reemplazarlo, es lo que hace que el proyecto entre sin pelear contra nadie internamente.
6. **El entregable es el mecanismo, no el reporte.** Política institucional (cubre el 18,5%), proceso de evaluación con umbrales (cubre el 9,0%), y el reporte periódico que el proceso produce. Es exactamente lo que la encuesta dice que falta, dicho en el vocabulario de la encuesta.

**A quién golpear primero, con dato:** adopción por tipo de institución — **privadas sin fines de lucro 84%, públicas 68%, privadas con fines de lucro 52%**. Las privadas sin fines de lucro son el segmento más maduro y el de ciclo de compra más corto: empezar ahí y usar el caso para entrar al sector público, que es el volumen y el ciclo largo.

**El argumento de cierre con la comunidad educativa:** la KB ya documentó que **65% de los estudiantes LATAM teme que la AI vuelva superficial el aprendizaje** (DEC, 30.000+ respuestas). Este patrón es la única respuesta que no es retórica: medición publicada. Sirve igual para el consejo académico que para el gremio docente.

**Tiempo estimado:** 6–8 semanas para el piloto completo (pasos 2–6), de los cuales el inventario del paso 2 es facturable por separado y sirve de puerta de entrada. **Composición:** es P11 + P12 empaquetados en el lenguaje institucional de la región, no patrones nuevos.

---

## P14 — Calificar sin que califique el modelo (agregado en el pase 5; North America primero, aplica donde haya prohibición de grading automático)

**Problema.** Los estatutos de EE. UU. que esta KB documenta (Ohio, Virginia, Oklahoma, Maryland, Idaho) y el Annex III del EU AI Act **no prohíben la AI en evaluación: prohíben que la decisión de calificación sea automática.** Es una distinción implementable, y casi nadie la está vendiendo bien — se vende "AI para corregir" y se choca con el regulador, o no se vende nada.

**Y el gap 6 de esta KB explica por qué hay poco con qué construir:** el grading agéntico open source más maduro que existe, `llmgrader` (NYU, 240 commits, en producción en un curso de maestría, con MCP e integración a Gradescope), tiene **licencia de investigación custom — "PySilicon Research License", no OSI — y no se puede usar en un entregable.** El gap no era que nadie lo construyera; era que quien lo construyó bien no lo liberó.

**La arquitectura que cumple sin perder el beneficio: la nota la pone un componente determinista y el LLM sólo explica.**

| Rol | Pieza | Licencia | Nota |
|-----|-------|----------|------|
| **La nota** (código) | **[Autograder.io](https://github.com/eecs-autograder/autograder.io)** — casos de test, sandbox Docker | ⚠️ verificar por componente | U. de Michigan, **~5.000 alumnos/semestre**. El único dato de escala de producción de toda esta capa |
| **La nota** (no-código) | **[rubric](https://github.com/paper-instruments/rubric)** — rúbricas ponderadas, salida validada | MIT ✅ | 75 ★ |
| El incumbente que no se va a cambiar | **[gradescope-mcp](https://github.com/Yuanpeng-Li/gradescope-mcp)** — 34 tools, escrituras tras confirmación | MIT ✅ | 8 ★ |
| Artefacto de corrección auditable | **[AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent)** — Lab/Exam/Grading como DSL validado, review humano obligatorio | MIT ✅ | 0 ★ — seguir, no usar |
| Que el gate no sea adulador | **P11** (`SafeTutors`, `EduBench`) | MIT ✅ | — |

**Wiring concreto.**

1. **Separar explícitamente dos decisiones que el cliente tiene mezcladas:** *cuánto vale esta respuesta* (determinista, auditable, apelable) y *por qué* (generado, útil, no vinculante). Escribirlo en el diseño antes de tocar código, porque es lo que se le muestra al abogado del distrito.
2. **La nota sale de un test o de una rúbrica, nunca de un modelo.** Código → Autograder.io u otro runner de tests. Respuesta abierta → `rubric` con criterios ponderados versionados en el repo. **Lo determinista no es sólo cumplimiento: es reproducible y sobrevive una apelación de nota**, que es el riesgo operativo real de un distrito.
3. **El LLM explica el resultado que ya existe.** Recibe la respuesta del alumno, el resultado de los tests o del criterio, y produce feedback formativo: qué concepto falta, qué caso falló y por qué. **Nunca recibe la pregunta "¿qué nota merece?".** Esa separación en el prompt es el control técnico que se audita.
4. **Revisión humana en el medio, con el artefacto correcto.** El diseño de `AI-Teaching-Agent` es el modelo a copiar: DSL validado, review obligatorio, previews de examen sin respuestas ni referencias de corrección. Con 0 ★ **no se usa como dependencia** — se copia el diseño.
5. **Si el cliente ya tiene Gradescope, orquestarlo y no reemplazarlo** (`gradescope-mcp`, MIT). Sigue siendo la recomendación del gap 6 y esta pasada no encontró nada que la cambie.
6. **Medir el explicador con P11.** Un feedback formativo que revela la respuesta completa o que le da la razón al alumno para no desmotivarlo **es exactamente la falla que SafeTutors mide**. Sin este paso, el paso 3 introduce el riesgo que el paso 1 quiso evitar.
7. **El entregable de cumplimiento:** diagrama de flujo de decisión mostrando que la nota nunca pasa por el modelo, el registro de revisión humana, y los criterios versionados con su historial. Eso responde el estatuto.

⚠️ **Lo que no hay que hacer, y es la tentación:** usar `llmgrader` porque es el más maduro. Su licencia no lo permite. Sirve como **referencia de diseño** —sus rúbricas en XML y sus trazas de corrección son buenas ideas— y nada más.

⚠️ **`eecs-autograder/autograder.io` es el repo de documentación e issues y no declara licencia**; el código vive en otros repos de la organización. Verificar la licencia del componente concreto antes de cotizar.

**Tiempo estimado:** 5–7 semanas para código (Autograder.io hace el trabajo pesado); 8–10 para respuesta abierta (la rúbrica es donde se va el tiempo, y es trabajo pedagógico con el cliente, no de ingeniería). **Dónde venderlo primero:** **North America**, distritos y universidades con estatuto vigente — es el patrón que convierte una prohibición en una especificación, y llegar con la arquitectura ya resuelta gana contra quien llega a pedir una excepción.

---

## P15 — Memoria de aprendizaje conforme al estándar: el LRS como capa 0 (agregado en el pase 6; transversal, y es la base de P1, P10 y P14)

**El problema que resuelve.** Todo tutor con AI llega a la misma pregunta del director académico: *"¿esto dónde queda guardado, y cómo sé lo que el sistema decidió?"*. La respuesta habitual —"en nuestra base de datos"— no sirve ante un auditor, no se integra con el LMS ni con el SIS, y hay que rehacerla en cada engagement. Existe una respuesta estándar desde hace una década y esta KB no la tenía registrada hasta el pase 6: **xAPI / IEEE 9274.1.1**, implementado por un **Learning Record Store**.

**Por qué se propone antes que el tutor.** Es barato, es infraestructura que el cliente entiende, y convierte cada patrón posterior en auditable sin trabajo extra. Los mandatos de supervisión humana de EE. UU. (gap regulatorio de `intel/market.md`), el EU AI Act y la clasificación de Vietnam de la evaluación automatizada como alto riesgo piden todos lo mismo: **registro de qué decidió el sistema, cuándo y con qué evidencia.** Eso es literalmente lo que un LRS almacena.

### Las piezas, todas verificadas en el pase 6

| Capa | Pieza | Licencia | Por qué esta |
|---|---|---|---|
| Almacén | **`lrsql`** — https://github.com/yetanalytics/lrsql | Apache-2.0 ✅ | Corre sobre el PostgreSQL (14–18) que el cliente ya opera. No agrega infraestructura nueva al diagrama |
| Almacén (alternativa Open edX) | **`Ralph`** — https://github.com/openfun/ralph | MIT ✅ | Convierte tracking logs de Open edX a xAPI de fábrica. Mismo origen que Richie (OpenFun, Francia) |
| Puente al agente | **`learnmcp-xapi`** — https://github.com/DavidLMS/learnmcp-xapi | MIT ✅ | Tres tools MCP: registrar statement, consultar progreso, gestionar vocabulario. Ya soporta `lrsql` y Ralph |
| Estimador de mastery | **`pyBKT`** — https://github.com/CAHLR/pyBKT | MIT ✅ | **Esta es la pieza que hay que construir/integrar** — no viene hecha. BKT bayesiano, interpretable, UC Berkeley. Alternativa: `pyKT` (MIT, DLKT, más potente y menos defendible) |
| Scheduling de repaso | **`py-fsrs`** — https://github.com/open-spaced-repetition/py-fsrs | MIT ✅ | Decide *cuándo* volver sobre un concepto, una vez que el LRS sabe cómo le fue |
| Agente | El que corresponda al engagement | — | El tutor deja de tener memoria propia: escribe y lee del LRS |

**Las seis piezas son permisivas.** Es el primer patrón de esta KB que se arma completo sin una sola licencia con fricción.

### El wiring

1. **Levantar el LRS.** `lrsql` contra el Postgres existente (o `Ralph` si el cliente está sobre Open edX). Definir el perfil xAPI del proyecto: qué verbos se usan (`attempted`, `answered`, `mastered`, `asked-for-hint`) y sobre qué objetos.
2. **Instrumentar el origen de eventos.** Si hay LMS, sus eventos ya salen (Ralph los convierte desde Open edX; Moodle y Canvas salen por sus propios plugins/LTI). Si el tutor es la única superficie, lo instrumenta el paso 3.
3. **Conectar `learnmcp-xapi` al LRS** y dárselo al agente como servidor MCP. Desde acá el tutor ya **registra** cada interacción como statement y **consulta** el historial antes de responder. Esto solo ya entrega el argumento de auditabilidad — sin ningún modelo de mastery todavía.
4. **La pieza propia: el estimador.** Un servicio que lee los statements del LRS, los mapea a secuencias `(alumno, skill, correcto/incorrecto)`, entrena `pyBKT` y expone `P(mastery | skill, alumno)`. Se publica como **tool MCP adicional** junto a las tres de `learnmcp-xapi`. Es el componente que el pase 5 buscó en cinco repos y no encontró bien hecho en ninguno.
5. **Cerrar el lazo con scheduling.** `py-fsrs` toma la estimación de mastery y decide el próximo repaso. El agente pregunta al MCP qué toca antes de elegir el ejercicio.
6. **Evaluar que efectivamente enseña.** `MathTutorBench` o `EduBench` sobre las respuestas del tutor, y `SafeTutors` como gate de seguridad pedagógica (ver **P10** y **P11**). El LRS da la trazabilidad; estos dan la calidad.

### Plazo y alcance

**6–8 semanas** para los pasos 1–3 (LRS + instrumentación + MCP, auditable end-to-end). **+4–6 semanas** para los pasos 4–5 (estimador de mastery y scheduling). El corte entre ambos es limpio y conviene venderlo así: **la primera mitad entrega cumplimiento y no depende de que el modelo de mastery funcione**, lo que la vuelve mucho más fácil de aprobar.

### Dónde se vende primero

- **North America** — donde hay mandato distrital con **supervisión humana obligatoria** (Idaho, Maryland, Oklahoma, Virginia): el LRS *es* la evidencia de supervisión. Combina con **P7** y **P14**.
- **EMEA** — expediente del EU AI Act (**P4**), con el argumento extra de que `Ralph` y `learnmcp-xapi` son artefactos europeos y MIT (soberanía tecnológica, que puntúa en licitación).
- **LATAM** — es la respuesta directa a la tijera de la región: 50%+ de docentes usando AI y <10% de instituciones con lineamientos. El LRS es el instrumento más barato para pasar de "se usa" a "se puede medir y gobernar". Combina con **P13**.
- **APAC** — obligatorio donde la evaluación automatizada es alto riesgo (**Vietnam**) y bajo el AI Basic Act coreano. Combina con **P5**.

⚠️ **Lo que NO hay que prometer.** Ningún LRS estima mastery: son almacenes conformes al estándar. La inferencia es siempre desarrollo propio (paso 4). Y `learnmcp-xapi` tiene **32 commits** — sirve como referencia de integración o base a forkear (es MIT), **no como dependencia de producción sin revisarlo**. Si el cliente ya tiene un LRS, lo más probable es que sea **Learning Locker**, que es **GPL-3.0**: en ese caso el servicio propio va afuera y se habla por la API estándar, sin tocar el core.

## P16 — Entrenar el estimador de mastery sin un dataset que se pueda usar (agregado en el pase 7; transversal, y es la condición de posibilidad de P1, P12 y P15)

**El problema que resuelve, y es el que P15 dejó abierto sin decirlo.** P15 termina en el paso 4 —"la pieza propia: el estimador"— y lo presenta como integración de `pyBKT`, que es MIT. Lo es. Pero un modelo de knowledge tracing **no se instala: se entrena**, y cuando se va a buscar con qué, la licencia se da vuelta (ver `repos/foundations.md`, capa de datos de entrenamiento):

| Dataset | Volumen | Licencia | ¿Sirve en un entregable facturado? |
|---|---|---|---|
| **EdNet** | 131,4M interacciones, 784k alumnos | ⚠️ **CC BY-NC 4.0** | **No** |
| **FoundationalASSIST** | 1,7M, el único en inglés con respuestas reales y distractores | ⚠️ **CC BY-NC 4.0** + gated | **No** |
| **XES3G5M** | 5,5M interacciones, 18k alumnos, 7.652 preguntas, 865 KC | **MIT** ✅ | **Sí**, y es **chino, matemática, tercer grado** |

**La consecuencia no es legal, es de arquitectura y de cronograma:** si el dataset de producción tiene que ser el del cliente, entonces **el LRS no es la fase de conformidad, es la fase que fabrica el activo**. Y el proyecto tiene un arranque en frío que hay que presupuestar en vez de descubrirlo en la semana 10.

### El wiring, en tres fases con un corte comercial limpio

**Fase A — Validar la arquitectura con `XES3G5M` (2–3 semanas).** Entrenar `pyBKT` (y opcionalmente un DLKT de `pyKT`) sobre `XES3G5M`, que es **MIT** y por lo tanto el único que se puede tocar sin pasar por legal. El entregable no es un modelo: es el **pipeline probado** —ingesta, mapeo a secuencias `(alumno, skill, correcto)`, entrenamiento, métricas de AUC/accuracy, serving detrás de MCP— y la evidencia de que funciona end-to-end.

⚠️ **El error que hay que evitar acá, y es fácil de cometer:** presentar el modelo entrenado sobre `XES3G5M` como el modelo del cliente. Es matemática de tercer grado en chino. Sirve para demostrar que el pipeline entrena y mide; **no transfiere** a la materia, el nivel ni el idioma del cliente. En la propuesta va escrito como *validación de arquitectura*, con esas palabras.

**Fase B — Arranque en frío, con el LRS produciendo el dataset (6–10 semanas, solapada con el uso real).** Es P15 en su totalidad —`lrsql` (Apache-2.0) o `Ralph` (MIT) instrumentado desde el día 1, statements xAPI con el perfil de verbos del proyecto— y mientras el histórico se acumula, el tutor **no miente sobre lo que sabe**:

1. **Arrancar con `py-fsrs`** (MIT) como única política de secuenciación. FSRS no necesita histórico de la población: funciona por alumno desde la primera interacción, con parámetros por defecto. Es la respuesta correcta al día 1.
2. **Prerequisitos declarados a mano**, no aprendidos: un grafo de conceptos del currículo del cliente, que es trabajo de experto de dominio y no de ML. Da adaptación defendible sin ningún modelo entrenado.
3. **Medir la cobertura del dataset propio** como KPI visible del proyecto: interacciones por skill y por alumno. `pyBKT` empieza a dar estimaciones útiles cuando hay volumen por skill, y conviene que el cliente vea crecer ese número en vez de esperar un hito opaco.

**Fase C — Reentrenar con los datos del cliente y recién ahí prometer mastery (4–6 semanas, cuando la fase B dio volumen).** El mismo pipeline de la fase A, ahora sobre los statements del LRS. Acá el modelo sí es del cliente, los datos no tienen fricción de licencia porque son suyos, y la estimación es defendible ante un regulador porque es interpretable (`pyBKT` es BKT bayesiano) y porque el expediente de cómo se llegó a ella está en el LRS.

### Las piezas

| Rol | Pieza | Licencia | Nota |
|---|---|---|---|
| Dataset de validación | **`XES3G5M`** — https://github.com/ai4ed/XES3G5M | **MIT** ✅ | El único grande reutilizable. Chino, matemática, 3.er grado |
| Estimador | **`pyBKT`** — https://github.com/CAHLR/pyBKT | MIT ✅ | Interpretable, UC Berkeley. Preferible a DLKT ante un regulador |
| Estimador (alternativa potente) | **`pyKT`** — https://github.com/pykt-team/pykt-toolkit | MIT ✅ | 10+ modelos DLKT. Más potente, menos explicable. Origen China (gap 4) |
| Scheduling día 1 | **`py-fsrs`** — https://github.com/open-spaced-repetition/py-fsrs | MIT ✅ | **La pieza que hace viable el arranque en frío** |
| Almacén / fábrica de dataset | **`lrsql`** o **`Ralph`** | Apache-2.0 / MIT ✅ | Ver **P15** |
| Transporte al agente | **`learnmcp-xapi`** | MIT ✅ | 32 commits: base a forkear, no dependencia |

**Todas las piezas son permisivas.** La fricción de este patrón **no está en el código: está en los datos**, y es exactamente lo que P1, P12 y P15 no decían.

### Plazo y alcance

**12–19 semanas** de punta a punta, con un corte comercial limpio: la **fase A** (2–3 semanas) es un PoC vendible por separado que demuestra capacidad técnica sin comprometer plazos de producto; las **fases B+C** son el proyecto real. Vender A y B juntas y C como opción condicionada al volumen de datos es más honesto y se cotiza mejor que prometer "tutor adaptativo" en un solo bloque.

### Dónde se vende primero

- **Cliente con restricción de procedencia de software (cualquier región).** Acá el patrón **deja de ser opcional**. La ruta alternativa occidental que el pase 5 armó (`pyBKT` + `Aila` + `MathTutorBench` + `SafeTutors`) se sostiene en código y se rompe en datos: el único dataset permisivo es chino. Entrenar con datos propios es la **única** salida, y este patrón es cómo se hace sin que el cronograma explote. Ver gap 4.
- **North America** — combina con **P7** y **P14**. Y hay un argumento regulatorio que cae justo: **California AB 1159 prohíbe usar datos de estudiantes para entrenar modelos**, así que la fase C necesita base legal explícita y acotada al cliente. Un patrón que ya separa validación (datos de terceros) de producción (datos propios, con consentimiento) es el que se puede defender; uno que entrena sobre todo lo que encuentra, no.
- **EMEA** — el expediente del EU AI Act (**P4**) pide trazabilidad de los datos de entrenamiento, no sólo del modelo. Este patrón la produce como subproducto.
- **LATAM** — es la forma de atacar la tijera de la región (**P13**) sin depender de datasets que no existen en español: el histórico se fabrica. Encaja con la institucionalidad nueva del Observatorio de UNESCO/CEPAL, que necesita precisamente referencias metodológicas.

⚠️ **Lo que NO hay que prometer.** (1) Un modelo de mastery funcionando el día 1: no existe sin histórico, y decirlo temprano es más barato que corregirlo en la semana 10. (2) Que el modelo de la fase A transfiere al dominio del cliente: no transfiere. (3) Usar `EdNet` o `FoundationalASSIST` en el entregable: son **CC BY-NC** y un engagement es comercial — valen para investigación interna o un paper, nada más.

## P17 — Conformidad de accesibilidad como entregable auditable (agregado en el pase 8; **EMEA primero**, y es la única obligación de esta KB con fecha ya cumplida)

**El problema que resuelve.** Toda plataforma de e-learning y todo LMS que se ofrezca en la UE está alcanzado por el **European Accessibility Act**, en vigor desde el **2025-06-28**, con **WCAG 2.1 AA** como referencia técnica. A diferencia del AI Act —cuyo Annex III todavía se está escalonando— **esta fecha ya pasó**. Y a diferencia de la evaluación pedagógica, que hay que explicarle al cliente por qué la necesita, acá el cliente ya sabe que la necesita y suele no saber cómo demostrarla.

**Por qué es el patrón más fácil de vender de los dieciocho.** No compite con nada: no hay incumbente open source, no hay que desplazar a un proveedor, y el presupuesto **ya existe** — vive en cumplimiento y en compras públicas, no en innovación. En licitación pública europea la accesibilidad no es un diferencial, es un criterio de admisibilidad.

### Las piezas, todas verificadas en el pase 8

| Pieza | Licencia | Rol |
|---|---|---|
| **accessibility-agents** (419 ★, 374 commits) | **MIT** ✅ | El motor. Corre dentro de Claude Code / Copilot / Codex / Gemini CLI y revisa WCAG 2.2 AA sobre código, documentos (incluye PDF y ePub, que es donde vive el material didáctico) y markdown |
| **uisight** (128 ★) / **a11y-agents-kit** (34 ★) | **MIT** ✅ | Medición de contraste, área táctil y *theme drift*; `uisight` expone **servidor MCP**, así que el agente la consulta sin pegamento propio. **Las tres piezas de este patrón son MIT** |
| **LRS** (`lrsql` Apache-2.0 / `Ralph` MIT) | ✅ | Donde queda el registro fechado de cada verificación. Es lo que convierte un reporte en expediente |
| La plataforma del cliente | según caso | Moodle, Open edX, Canvas — sin forkear, como siempre |

### El wiring

1. **Auditoría base** con `accessibility-agents` sobre el tema del LMS, los componentes propios y el material (PDF y ePub incluidos). Sale un inventario de hallazgos WCAG 2.2 AA con severidad.
2. **Remediación** por punto de extensión — tema y plugin, nunca el core copyleft.
3. **Gate en CI:** los agentes corren en cada pull request, así que el código nuevo no puede volver a romper la conformidad. **Este paso es el producto**; la auditoría sola la hace cualquiera y caduca en un sprint.
4. **Expediente:** cada corrida escribe un *statement* al LRS. Lo que se entrega no es un PDF de auditoría, es **la serie temporal que demuestra conformidad sostenida** — que es lo que un regulador pide y lo que una auditoría puntual no puede dar.
5. **Autoría humana sobre las excepciones.** Donde la remediación automática no aplica, la decisión queda documentada y firmada por una persona.

### Plazo y alcance
**4–6 semanas** para auditoría + gate en CI + expediente sobre una plataforma. La remediación del material histórico se cotiza aparte y por volumen: es la parte grande y la que el cliente subestima siempre.

### Dónde se vende primero
**EMEA**, por el EAA, y en particular en licitación pública. **North America** entra por la vía de Section 508 y de las obligaciones de IDEA sobre materiales accesibles. **LATAM** entra más tarde y por otra puerta — la de inclusión educativa, no la de cumplimiento.

⚠️ **Lo que no promete este patrón:** que la plataforma sea *pedagógicamente* accesible para un alumno con discapacidad cognitiva. WCAG mide acceso técnico. La adaptación del contenido es **P18**, es otro trabajo, y mezclarlos en una sola propuesta es prometer de más.

## P18 — Asistente de educación especial donde redactar el IEP está prohibido (agregado en el pase 8; **North America primero**)

**El problema que resuelve, y es un problema de encuadre antes que técnico.** El docente de educación especial es el más sobrecargado del sistema y el primero que pide ayuda de AI. Pero el open source que apareció en el pase 8 apunta casi todo a **redactar y gestionar el IEP**, y esa es precisamente la tarea que las jurisdicciones de EE. UU. están cerrando: **Delaware** prohíbe usar AI para objetivos de IEP, evaluación docente y calificación subjetiva, y el marco de **Nueva York** prohíbe usar AI para el desarrollo de planes **IEP o 504**.

**La consecuencia comercial es directa: un producto que redacta IEP es invendible en los distritos más grandes del país.** Lo vendible es todo el resto del flujo, con el docente como autor de la decisión.

### La arquitectura de referencia ya existe y es `tero`

`tero` (MIT, 111 commits, Chile) implementa exactamente la postura que esta restricción obliga: ***el agente propone, el docente decide*** — **el modelo no escribe ningún archivo sin aprobación humana explícita**, y está anclado a instrumentos normativos nacionales (MINEDUC, Decreto 83, Ley 21.719) en vez de a un currículo genérico. Con **0 ★ no es una dependencia de producto**; es la referencia de diseño, y es reutilizable porque es MIT.

### Las piezas

| Pieza | Licencia | Rol |
|---|---|---|
| **`tero`** (0 ★, 111 commits) | **MIT** ✅ | Referencia de arquitectura del gate humano y de la vinculación a norma. Reutilizable |
| **`Aila`** (35 ★, 1.188 commits, Oak National Academy) | **MIT** ✅ ⚠️ *"internal use"* | Referencia teacher-facing **en producción**, la única de la KB con escala real |
| **`accessibility-agents`** (419 ★) | **MIT** ✅ | Garantiza que el material que el agente produce sea **él mismo accesible** — si el entregable para un alumno con discapacidad no cumple WCAG, el proyecto se contradice |
| **`EduBench`** + **`SafeTutors`** | **MIT** ✅ | El expediente de calidad y de seguridad pedagógica. Ver **P10** y **P11** |
| **LRS** (`lrsql` / `Ralph`) | Apache-2.0 / MIT ✅ | Registro de qué propuso el agente, qué aprobó el docente y qué rechazó. **Bajo IDEA, la trazabilidad de la decisión es la defensa del distrito** |
| **`noggimigo`** (1 ★) | **MIT** ✅ | Idea reutilizable, no dependencia: **latencia de respuesta como señal de carga cognitiva** |

### El wiring, con el límite adelante

1. **Entrada:** la acomodación **ya decidida y ya firmada** por el equipo de IEP se carga como configuración. **El sistema nunca la genera ni la sugiere.** Este límite es la primera línea de la propuesta, no una nota al pie.
2. **Adaptación de material** contra esa acomodación: nivel de lectura, segmentación, apoyo visual, texto-a-voz, andamiaje.
3. **Gate humano obligatorio** al estilo `tero`: el docente aprueba, edita o rechaza antes de que algo llegue al alumno.
4. **Verificación de accesibilidad** del artefacto producido con `accessibility-agents` (P17).
5. **Evidencia al LRS:** propuesta, decisión docente, versión entregada, resultado.
6. **Medición pedagógica** con `EduBench` y `SafeTutors` antes de entregar.

### Plazo y alcance
**8–10 semanas** para un piloto de una materia en un distrito. El trabajo caro no es el agente: es **mapear el vocabulario de acomodaciones del distrito** a transformaciones concretas de material, y eso es trabajo con los docentes, no con el modelo.

### Dónde se vende primero
**North America**, donde IDEA crea la obligación y la prohibición de IEP automatizado crea el encuadre. **EMEA** entra combinado con **P17** (EAA). **LATAM** entra por Chile, donde el Decreto 83 cumple el papel de IDEA y donde `tero` y `Ronda` dan contraparte técnica local — ver el **gap 2**.

⚠️ **Las dos frases que no se pueden decir en esta venta:** que el sistema «escribe IEPs» y que «decide acomodaciones». Las dos están prohibidas en jurisdicciones concretas y las dos son innecesarias — el valor está en las horas de preparación de material, que es donde el docente efectivamente se consume.

## P72 — Expediente de accesibilidad de la evaluación, generado y no declarado (agregado en el pase 35; **EMEA primero**, y es la segunda obligación vencida de esta KB que por fin tiene piezas)

**El problema que resuelve.** La obligación europea de accesibilidad es **la única de esta KB con fecha ya cumplida**
(pase 17), y **P17** se escribió sin una pieza permisiva que la cumpliera: el pase 8 midió que la tecnología asistiva
madura es toda copyleft y que lo permisivo no pasaba de 15 estrellas. Mientras tanto, lo que un cliente institucional
necesita entregar no es una afirmación —*«nuestros ítems son accesibles»*— sino **evidencia reproducible por ítem**.

🟢 **Lo que cambió en el pase 33:** las piezas existen, son **MIT**, y están **adentro de la pila de evaluación**, que es
donde nadie las buscó.

### Las piezas, todas verificadas en el pase 35

| Pieza | Licencia | Rol |
|---|---|---|
| `@longsightgroup/qti3-core` | **MIT** ✅ (cero deps) | Parseo, validación, *response processing* y **scoring** del ítem QTI 3 |
| `@longsightgroup/qti3-a11y` | **MIT** ✅ | 🔵 **La prueba:** `accessibilityProofMatrix`, `a11yContracts` (teclado, foco, nombre accesible, mensaje de validación **por tipo de interacción**) y **`manualAssistiveTechnologyScripts` para VoiceOver, NVDA y JAWS** |
| `@longsightgroup/qti3-pnp` | **MIT** ✅ (cero deps) | Resuelve **Personal Needs and Preferences** contra las capacidades del *player* y el catálogo QTI, con diagnósticos de perfil |
| `@longsightgroup/qti3-cli` | **MIT** ✅ | **`a11y-proof`**, `validate`, `inspect-package`, `validate-package`, `support-matrix` — **todos emiten JSON** |
| `@longsightgroup/qti3-conformance` + `-fixtures` | **MIT** ✅ | Corredor de *fixtures* y casos sintéticos con resultados esperados: es el **control de regresión** del expediente |
| `bruchris/canvas-lms-mcp` | **MIT** ✅ | 🔵 **El lado LMS, y es nuevo: trae `accessibility audits` como categoría de tools** entre sus 165 |
| `lrsql` (LRS) | Apache-2.0 | Registra el resultado de cada corrida como *statements* xAPI → el expediente queda **fechado y consultable** |

### El wiring

1. **Entrada:** el banco de ítems QTI 3 del cliente (o el convertido con `qti3-migrator` desde 1.2 / 2.x).
2. **Por ítem:** `qti3-cli validate` → `qti3-cli a11y-proof` → se emite el par **`accessibilityProofMatrix` + contrato de
   interacción**, en JSON.
3. **Por perfil de alumno:** `qti3-pnp` resuelve el PNP declarado contra las capacidades del *player* y **emite
   `diagnostics` y `catalogRequests`** — es decir, deja escrito **qué pidió el alumno y qué pudo entregar el sistema**.
   🔵 **Ese par es el corazón del expediente**, porque documenta la brecha en vez de afirmar su ausencia.
4. **Verificación manual, acotada:** `manualAssistiveTechnologyScripts` da el guion para **VoiceOver, NVDA y JAWS**. Se
   corre sobre una **muestra estratificada por tipo de interacción**, no sobre el banco entero: el contrato es por tipo,
   así que la muestra cubre la clase.
5. **Regresión:** `qti3-conformance` + `-fixtures` en CI → **el expediente no caduca con el próximo release del player**.
6. **Trazabilidad:** cada corrida emite *statements* a `lrsql`, y el lado LMS se audita con las tools de
   `accessibility audits` de `bruchris/canvas-lms-mcp`.
7. **Salida al cliente:** un paquete con la matriz por ítem, los diagnósticos de PNP, los guiones ejecutados con fecha y
   operador, y el resultado de CI. **Eso es un expediente, no un informe.**

### Plazo y alcance

**6–8 semanas** para un banco de hasta ~500 ítems con 6–8 tipos de interacción, incluyendo la conversión desde QTI 1.2 /
2.x si hace falta. **El costo no está en la accesibilidad: está en la integración de PNP.**

⚠️ **Y el límite hay que poner adelante, porque el propio proyecto lo escribe:** *«It does not fetch, store, authorize,
or transmit PNP records. LMS identity, consent, institutional policy, persistence, LTI launch handling, and AfA PNP
service access belong outside this package.»* 🔴 **Identidad, consentimiento, política institucional, persistencia,
*launch* LTI y el servicio AfA PNP son el trabajo de integración y se cotizan aparte.** Que lo declare la librería en vez
de dejarlo implícito es lo que vuelve la cotización defendible.

⚠️ **Riesgo de madurez, declarado:** la pila es **0.13.1 del 2026-10-01** y tiene **5 ★**. **Capacidad y licencia
verificadas; comunidad mínima.** Se propone con *fork* interno y CI propio, no como dependencia transparente.

### Dónde se vende primero

**EMEA**, por la obligación vencida y porque es la única región donde esta KB midió que la ventaja comprable es el
expediente y no la adopción (**UE 19,95 % contra OCDE 20,2 %**). **Segundo North America**, donde cuatro estados obligan
a política distrital y **Oklahoma y Maryland prohíben la decisión de alto impacto automatizada** — el expediente de
accesibilidad es el mismo artefacto con otra carátula.

---

## P73 — El bucle cerrado docente: material propio → lección revisable → aula → nota, todo permisivo (agregado en el pase 35; **transversal, y es el patrón que P8 describía sin tener piezas**)

**El problema que resuelve.** **P8** («Fábrica de lecciones en la voz del docente») era el ángulo menos disputado de esta
KB y el peor abastecido: había generadores de contenido genérico y había conectores de LMS, **y nada que uniera el
material propio del docente con la calificación**. Y es justo el circuito donde la objeción de LATAM pega más fuerte:
**65 % de los estudiantes teme que la AI vuelva superficial el aprendizaje.**

🟢 **El pase 33 cierra el circuito con tres piezas MIT y una Apache-2.0.**

### Las piezas, todas verificadas en el pase 35

| Pieza | Licencia | Rol |
|---|---|---|
| **`SirhanMacx/Claw-ED`** | **MIT** ✅ (60 ★, 778 commits) | **Entrada y autoría.** Importa PDF/DOCX/PPTX/TXT/MD del docente, indexa para *retrieval*, **construye perfil de estilo de enseñanza** y emite borradores **editables en DOCX y PPTX**. El modelo lo elige el usuario; **corre local** |
| **`JuneYaooo/lineage-skill`** | **Apache-2.0** ✅ (448 ★) | **Destilación con procedencia.** Convierte el material en *Agent Skills* con **trazabilidad a la fuente**: diagnósticos, flujos, **rúbricas**, plantillas y **modos de falla** |
| **`course-code-framework/coursecode`** | **MIT** ✅ | **Salida empaquetada.** **15 tools**; `coursecode_build` con `format` = `cmi5` \| `scorm2004` \| `scorm1.2` \| `lti`; `coursecode_lint` y `coursecode_screenshot` para verificar antes de publicar |
| **`bruchris/canvas-lms-mcp`** | **MIT** ✅ | **Aula y nota.** **165 tools**: *assignments*, *submissions*, **rubrics**, *gradebook history*, califica y comenta |
| `peancor/moodle-mcp-server` | **MIT** ✅ | Alternativa del lado Moodle: **escribe nota y devolución** |
| `lrsql` | Apache-2.0 | *Statements* xAPI de cada paso → evidencia de que el circuito ocurrió |

### El wiring, y el orden importa

1. **`Claw-ED` toma el material del docente y construye el perfil de estilo.** No se parte de un prompt: se parte del
   acervo real de la cátedra.
2. **`lineage-skill` destila ese acervo en skills con trazabilidad y extrae la rúbrica**, que es la pieza que después
   califica. 🔵 **La rúbrica sale del material del docente, no del modelo** — y eso es lo que hace defendible la nota.
3. **`Claw-ED` emite la lección, los materiales del alumno y las diapositivas en DOCX y PPTX. El docente edita en sus
   herramientas de siempre y aprueba.** El paso de revisión está en el diseño, no en el descargo de responsabilidad.
4. **`coursecode` empaqueta**: `coursecode_lint` → `coursecode_screenshot` para verificar maquetado →
   `coursecode_build(format)` según lo que coma el LMS del cliente.
5. **`canvas-lms-mcp` publica el *assignment* con su rúbrica** y, cuando llegan las entregas, **califica y comenta
   citando la rúbrica destilada en el paso 2**.
6. **`lrsql` registra cada paso**, así que al final hay **una cadena auditable desde el material original hasta la nota**.

🔵 **Por qué este patrón vale más que la suma de sus piezas:** es el único de esta KB donde **la trazabilidad va de punta
a punta** — la nota se puede justificar hasta el documento que el docente trajo. **Es la respuesta técnica literal al
65 % de desconfianza estudiantil de LATAM**, y es también el argumento de cumplimiento en EMEA, donde el Anexo III nombra
la **evaluación de resultados de aprendizaje**.

### Plazo y alcance

**8–10 semanas** para una cátedra con acervo existente y un LMS ya desplegado. Hitos: (1) perfil + destilación, 2–3
semanas; (2) primeras lecciones revisadas y aceptadas por el docente, 2 semanas; (3) empaquetado y publicación, 2
semanas; (4) circuito de calificación con rúbrica, 2–3 semanas.

⚠️ **Riesgos declarados.** `Claw-ED` está en **beta declarada** (Python 3.11+) y **no es oficial de ninguna institución**.
El **165** de `canvas-lms-mcp` es **declarado, no servido** (`tools/list` no observado): la primera semana del proyecto
se gasta en **medirlo**. Y 🔴 **la capa de despliegue alojada de `coursecode` (login/deploy/promote/CDN) NO está detrás de
MCP y es un servicio de terceros**: el patrón usa **sólo el build local**.

### Dónde se vende primero

**LATAM**, porque la objeción de compra ya está medida y este patrón es su respuesta. **Después North America**, donde
el ahorro docente es la métrica que decide retención (**5 a 10 horas por semana** es el umbral medido) y donde el
**STUDENTS FIRST Act of 2026** pide exactamente esta clase de trazabilidad.

---

## P74 — El servidor MCP del dato educativo nacional, replicando una plantilla que ya existe (agregado en el pase 35; **LATAM / Brasil primero**, y es contribución *upstream* antes que proyecto)

**El problema que resuelve.** **Brasil tiene una capa MCP nacional de datos públicos y educación es el único dominio
grande que falta** (gap 63, tendencia 106). Cuatro dominios ya tienen servidor —**IBGE/censo** (`ibge-br-mcp`, **MIT**,
24 versiones desde enero de 2026, con procedencia de fuente), **Banco Central** (`bcb-br-mcp`), **DATASUS SIH/SUS**
(`sih-br-mcp`) y **firma electrónica**—, y los tres datasets educativos canónicos —**INEP**, **Censo Escolar**,
**ENEM**— **no tienen ninguno**: `inep` devuelve 3 resultados sin MCP, `censo-escolar` 18 y todos colisión
(🔴 **Censo Custody, billetera Solana**), `enem` 6 y el más nuevo es de 2024.

### Las piezas

| Pieza | Licencia | Rol |
|---|---|---|
| **`SidneyBissoli/ibge-br-mcp`** | **MIT** ✅ | 🔵 **La plantilla, no una dependencia.** Ya resolvió el problema difícil: **servir dato público por MCP con procedencia**. Se replica su forma, no su código |
| `@modelcontextprotocol/sdk` | **MIT** ✅ | Servidor MCP |
| `qdrant` o `pgvector` | Apache-2.0 / PostgreSQL | Índice semántico sobre metadatos y diccionarios de variables (los datasets del INEP tienen cientos) |
| `lrsql` | Apache-2.0 | Opcional: registra qué consultó cada agente — útil para la rendición de cuentas de un ministerio |
| `temporal` | MIT | Sólo si el dato llega por CSV y hay que ingestarlo: orquesta la actualización periódica |

### El wiring, en dos variantes y **la elección no se puede hacer todavía**

- **Variante A — fachada (semanas).** Si INEP y el portal de datos abiertos exponen **API REST**, el servidor es una
  fachada: tools de consulta por escuela, municipio, red y año, con **cita de fuente y versión del dataset** en cada
  respuesta, igual que `ibge-br-mcp`. **4–6 semanas.**
- **Variante B — ingesta (meses).** Si sólo hay **descargas de CSV**, hace falta pipeline: descarga versionada →
  normalización → carga → índice → fachada, con `temporal` orquestando la actualización anual del Censo Escolar.
  **12–16 semanas.**

🔴 **Cuál de las dos es se decide con una medición que este pase NO hizo, y está escrita como acción 3 del pase 34:**
probar `dados.gov.br` y las APIs del INEP. ⚠️ **No cotizar este patrón antes de esa medición** — es la diferencia entre
seis semanas y cuatro meses, y prometer la primera y entregar la segunda es la forma más rápida de perder una cuenta
pública.

### Por qué se propone igual, con esa incógnita adelante

**Porque el valor no está sólo en el entregable.** (a) **Es contribución *upstream* visible** en una región donde
**sólo 8 % de las instituciones tiene presupuesto dedicado** a AI: abre puerta institucional por reputación, no por
licitación. (b) **Hay demanda medida**: **92 % de estudiantes y 79 % de docentes** de LATAM usan AI, y **65 % de los
estudiantes desconfía de la superficialidad** — un servidor que responde **con dato público y procedencia** es la
respuesta directa a esa objeción. (c) **El patrón es replicable por país**: la misma forma sirve para el **SIMCE**
chileno, las pruebas **Saber** colombianas y la **ENLACE/PLANEA** mexicana, y **CONPES 4144** en Colombia tiene programa
nacional con presupuesto hasta 2030.

### Dónde se vende primero

**LATAM / Brasil.** Y el camino de entrada no es una propuesta comercial: es **publicar el servidor como open source
MIT** y dejar que la conversación institucional venga después.

---

## P75 — Piloto de agente sobre el LMS sin pedirle nada al área de sistemas (agregado en el pase 35; **transversal, y desbloquea el piloto que esta KB no podía arrancar**)

**El problema que resuelve, y es el que frenaba todo lo demás.** Todos los patrones de esta KB que tocan un LMS piden lo
mismo: **token de administrador y Web Services habilitados.** Eso convierte un piloto de dos semanas en una conversación
de tres meses con el área de sistemas, seguridad y compras de la institución — y **es la causa por la que un
*discovery* se muere antes de demostrar valor.**

🔵 **El pase 33 encontró dos piezas que resuelven esto por arquitectura, no por negociación: trabajan desde la sesión
del navegador del propio usuario.**

### Las piezas

| Pieza | Licencia | Qué hace | Credencial |
|---|---|---|---|
| **`bunizao/moodle-cli`** | **MIT** ✅ | Vencimientos, notas, archivos, devoluciones y **revisión de quizzes** de Moodle, para terminal y para agentes. **20 versiones** (jul→sep 2026) | 🔵 **La sesión del navegador del usuario. Sin token de administrador** |
| **`moon0825/jbnu-lms-student`** | **MIT** ✅ | **La arquitectura de referencia.** **25 tools**, MCP STDIO local, orientado a *«qué tengo que hacer hoy»*: devuelve **hasta 3 pendientes con su fundamento** | 🔵 **Login en el navegador de la persona, con passkey y segundo factor. El servidor nunca ve la credencial** |
| `gafapa/moodle-core-cli` | **MIT** ✅ | Cliente de *core web services* de **Moodle 4.5+**, **sin MCP** | Token, cuando la institución sí lo da |
| `lrsql` | Apache-2.0 | Registra el uso del piloto → **la evidencia con la que se pide el presupuesto de la fase 2** |

### El wiring

1. **Fase 0 — piloto (2 semanas, sin TI).** `moodle-cli` o un servidor con la forma de `jbnu-lms-student` corriendo
   **local en la máquina del docente o del alumno**, con **STDIO**, hablándole al LMS por la sesión del navegador. **Sólo
   lectura.** Entregable: el agente contesta *«qué tengo que hacer hoy»* **con fundamento citado**.
2. **Fase 0.5 — evidencia.** `lrsql` registra qué se consultó y con qué frecuencia. 🔵 **Eso es el argumento del paso
   siguiente: no «creemos que sirve», sino «se usó N veces en dos semanas».**
3. **Fase 1 — institucionalización.** Con la evidencia en la mano se pide lo que al principio no se podía pedir: token,
   Web Services, y **el conector que escribe** (`peancor/moodle-mcp-server` para nota y devolución, o
   `bruchris/canvas-lms-mcp` con sus 165 tools del lado Canvas).
4. **Fase 2 — el resto de la KB.** Recién acá entran **P1**, **P10**, **P15** y **P73**, que son los que cierran circuito.

### Plazo y alcance

**2 semanas la fase 0**, y es el punto: **el valor se demuestra antes de la primera reunión con sistemas.**
Institucionalización, 4–6 semanas más según la burocracia del cliente.

⚠️ **Los límites, y son duros — se ponen adelante o el patrón se usa mal.**
🔴 **Las dos piezas son de SÓLO LECTURA y del lado del usuario: no califican, no devuelven nota, no escriben nada.** Un
piloto que prometa calificación con estas piezas **no se puede cumplir.**
🔴 **`jbnu-lms-student` es una herramienta estudiantil NO oficial por declaración propia** —el repo advierte que el
nombre y los activos de UI son de la universidad y que hay que revisar su guía oficial antes de distribuir—: **se usa
como arquitectura de referencia, nunca se instala en un cliente.**
⚠️ **Y la pregunta de gobernanza hay que hacerla el primer día, no el último:** operar sobre la sesión del usuario es
legítimo y es lo que hace barato el piloto, pero **la institución tiene que saberlo**. Un piloto que el cliente descubre
después es un problema de confianza, no de arquitectura.

### Dónde se vende primero

**APAC**, donde la pieza nació y donde el régimen coreano vigente (*AI Basic Act*, **2026-01-22**) premia exactamente
esta postura: **sólo lectura y credencial que nunca sale del navegador del usuario.** **Y LATAM en segundo lugar**,
donde **73,5 % ya enseña con AI y sólo 8 % tiene presupuesto dedicado**: un piloto que no necesita presupuesto ni
habilitación institucional es la única forma de entrar.

---

## Nota de licencias para todos los patrones

⚠️ **Agregado en el pase 7 del 2026-10-01 — esta tabla cubre repos, y para los patrones que entrenan un modelo (P1, P10, P12, P15, P16) eso no alcanza.** La licencia del **dataset** es una dimensión aparte y es donde vive el riesgo con más frecuencia:

| Dataset de knowledge tracing | Licencia | En un entregable facturado |
|---|---|---|
| **XES3G5M** | **MIT** ✅ | **Usable** — chino, matemática, 3.er grado: sirve para validar arquitectura, no para producción |
| **EdNet** | ⚠️ CC BY-NC 4.0 | **No usable** — sólo investigación interna |
| **FoundationalASSIST** | ⚠️ CC BY-NC 4.0 + gated | **No usable** — sólo investigación interna |

**La regla práctica:** todo patrón que entrene algo entrena **con los datos del cliente**, y por eso el LRS de **P15** es dependencia de fase 1. Ver **P16**.

| Licencia | Repos en estos patrones | Implicancia |
|----------|-------------------------|-------------|
| **MIT / Apache-2.0** ✅ | DeepTutor, OpenMAIC, NOMAD, OATutor, Educhain, tutor-mcp, py-fsrs, gradescope-mcp, AITutor-EvalKit, Kolibri, OpenOLAT, Richie, Oppia, XBlock, LLMs-from-scratch, minimind, **Bloom**, **ai-engineering-from-scratch**, **learn-claude-code**, **tiny-llm**, **Claw-ED**, **AI-Teaching-Agent**, y del pase 5: **pyBKT**, **EduBench**, **SafeTutors**, **rubric**, **Aila**, y los 5 servidores MCP de mastery | Sin fricción. Base de todo lo que Globant construye |
| **MIT con open-core** ⚠️ | **GegoK12** | El core (26 de 38 módulos) es MIT de verdad y admite plugin propietario. Pero **12 módulos son Pro pagos, USD 100–250 cada uno — entre ellos exámenes y fees**. La licencia no es el problema; el alcance sí. Cotizar los módulos Pro de entrada |
| **MIT reciente** ⚠️ | **OpenMAIC** | Relicenciado de **AGPL-3.0 a MIT en v0.3.0 (2026-06-28)**. Es permisivo hoy, pero la licencia tiene ~3 meses: si el cliente audita procedencia, declarar que el historial previo es AGPL |
| **BSD-3-Clause** ✅ | OpenTutorAI-CE | Permisiva. Sólo exige atribución y no usar el nombre del proyecto para endosar derivados |
| **GPL-2.0** ⚠️ | RosarioSIS, openSIS | Copyleft, **no** de red. El agente va afuera leyendo por API; no modificar el SIS |
| **GPL-3.0** ⚠️ | Moodle, Chamilo, H5P | No modificar el core. Integrar por plugin del AI subsystem |
| **AGPL-3.0** ⚠️ | Open edX, Canvas, Frappe LMS | Copyleft de red: modificar el core y servirlo por SaaS obliga a publicar el fuente. Integrar por XBlock (Apache-2.0) o LTI 1.3 |
| **CC BY-SA 4.0** ⚠️ | education-agent-skills, **UnifyingAITutorEvaluation / MRBench** | Contenido share-alike, no código. Revisar con legal antes de derivados cerrados. **Es la licencia que muerde en P10**, porque derivar un benchmark con datos del cliente dispara el share-alike |
| **Sin licencia declarada** 🚫 | **EduGuardBench**, **OmniEdu**, `awesome-ai-llm4education` | *Pase 5.* Sin LICENSE el default es todos los derechos reservados. Leer y citar sí; **empaquetar no**. En P11, EduGuardBench se usa para diseñar, no se incorpora |
| **Licencia de investigación custom** 🚫 | **llmgrader** (NYU) | *Pase 5.* "PySilicon Research License", © 2026 Sundeep Rangan, leída en el archivo. No es OSI. Es el grading agéntico más maduro que existe y **no se puede usar** — referencia de diseño en P14, nada más |

## P19 — De la evidencia de aprendizaje a la credencial verificable (agregado en el pase 9; **transversal, se vende primero en EMEA y APAC**)

**El problema que resuelve.** El cliente puede demostrar que el alumno estudió y no puede demostrar que el alumno
**sabe** de una forma que un tercero verifique sin llamarlo por teléfono. Es el tramo que cierra todo lo que esta KB
viene construyendo: el LRS registra la evidencia (P15), el estimador de mastery decide si hay dominio (P16), y hasta este
pase **nadie convertía esa decisión en un artefacto portable y verificable**. Ese hueco es el **gap 13**.

**Por qué es vendible ahora y no antes.** Las piezas de emisión y verificación son **MIT** y existen; lo que no existe es
el pegamento. Y la demanda está medida: **46% de las instituciones de LATAM y el Caribe ya ofrecen microcredenciales**, y
los tres obstáculos declarados del segmento son **estandarización (82%)**, **preparación institucional (76%)** y
**reconocimiento formal (71%)** — los tres se atacan con conformidad al estándar, que es exactamente lo que este patrón entrega.

### Las piezas, todas verificadas en el pase 9

| Capa | Pieza | Licencia | Por qué esta |
|------|-------|----------|--------------|
| Evidencia | `lrsql` o `Ralph` (LRS xAPI) | Apache-2.0 ✅ | Ya es la capa 0 de P15. **Es la que fabrica el dato**, no un anexo de conformidad |
| Dominio | `pyBKT` (MIT, 281 ★) o `pyKT` (MIT, 441 ★) | MIT ✅ | La decisión «domina / no domina» tiene que salir de un modelo publicado y reproducible, no de un LLM. ⚠️ Entrenar con datos del cliente — ver **gap 11** y **P16** |
| Competencia | `esco-skill-extractor` | **MIT** ✅ | Traduce el objetivo de aprendizaje del cliente al vocabulario **ESCO/ISCO**. **Es la pieza que hace reconocible la credencial fuera de la institución** |
| Emisión | `digitalcredentials/issuer-coordinator` | **MIT** ✅ | **W3C VC API** + formato **Open Badges 3.0**, con revocación y suspensión desde el día uno |
| Verificación | `digitalcredentials/verifier-plus` | **MIT** ✅ | El lado del empleador: copiar/pegar, archivo, URL o **QR** |
| Billetera | `digitalcredentials/learner-credential-wallet` | **MIT** ✅ | El lado del alumno. ⚠️ **Fijar versión**: la gobernanza pasó a OpenWallet Foundation Labs tras la v2.2.10 |
| Entrada al LMS | `1EdTech/lti-1-3-php-library` | Apache-2.0 ✅ | El agente entra como herramienta LTI 1.3 conforme, sin forkear el LMS |

### El wiring

1. **El LRS es la fuente de verdad.** Toda interacción se escribe como statement xAPI (P15). Sin esto el resto no tiene insumo.
2. **El estimador decide, no el modelo de lenguaje.** `pyBKT` consume las secuencias del LRS y emite una probabilidad de
   dominio por concepto. El LLM explica y acompaña; **no firma el juicio**.
3. **El mapa a ESCO se hace una vez, en diseño.** `esco-skill-extractor` corre sobre los objetivos de aprendizaje del
   cliente —no sobre cada alumno— y produce la tabla «concepto interno → competencia ESCO». Esa tabla es un entregable
   revisable por el cliente y es lo que hace la credencial legible para un empleador.
4. **El umbral es una decisión humana documentada.** «Dominio ≥ 0,85 sostenido en dos evaluaciones separadas» se define
   con el cliente y se versiona. Es el corazón del expediente de conformidad.
5. **`issuer-coordinator` emite la credencial** cuando se cruza el umbral: OB 3.0 firmado, con la competencia ESCO adentro.
6. **Revocación desde el primer día.** Se configura el servicio de estado antes de emitir la primera credencial — un
   esquema de credenciales sin revocación es inauditable, y reconstruirlo después obliga a reemitir todo.
7. **Billetera y verificador** cierran el circuito hacia alumno y empleador.

### Plazo y alcance

**8–10 semanas** para un piloto con un programa y un conjunto acotado de competencias, suponiendo LRS ya desplegado
(si no, sumar las 3–4 semanas de P15). El trabajo real no es criptográfico —eso lo resuelven las piezas MIT— sino
**el mapa a ESCO y la definición del umbral**, que son conversaciones con el cliente.

### Dónde se vende primero

**EMEA**, porque ESCO es el vocabulario europeo y porque el marco de credenciales está en política pública (⚠️ el stack
de la Comisión está archivado en GitHub y vive en `code.europa.eu`, bloqueado para esta sesión — **abrirlo antes de
cotizar**, gap 14). Después **APAC**, donde Filipinas tiene microcredenciales en TVET vía **TESDA** y un marco de la
**CHED** en consulta pública, y donde el consorcio **MICROCASA** articula España, Italia, Indonesia, Malasia y Filipinas.
**LATAM** tiene el 46% de instituciones ya ofreciendo microcredenciales y fragmentación de reconocimiento: el argumento
ahí es conformidad al estándar como atajo al reconocimiento transfronterizo.

---

## P20 — Evaluación conforme a QTI 3 con autoría asistida (agregado en el pase 9; **transversal, y es el camino de entrada al cliente institucional grande**)

**El problema que resuelve.** El cliente quiere generar evaluaciones con AI y necesita que los ítems **vivan en su
plataforma de examen y sobrevivan a un cambio de proveedor**. Generar preguntas con un LLM a un formato propio es un
callejón: no entra en el LMS, no se audita y no migra. QTI 3 es el formato que sí.

**La decisión de arquitectura que define el patrón.** La plataforma QTI madura es **TAO** (`oat-sa/tao-core`,
**22.533 commits**) y es **GPL-2.0**. Hay dos caminos y conviene elegirlo explícito:

- **Camino A — TAO desplegada tal cual.** Cuando el cliente quiere plataforma completa (autoría, entrega, scoring,
  roles). **No se forkea**: se despliega y la AI va al lado, entregando QTI XML por webhook/LTI. Misma receta que Moodle.
- **Camino B — componente embebido, sin fricción de licencia.** Cuando el entregable es producto del cliente,
  **`amp-up-io/qti3-item-player`** (**MIT**, **certificación de conformidad QTI 3 Basic y Advanced «Delivery» de
  1EdTech**) es el runtime de entrega y la autoría se construye arriba. **Es la única pieza certificada de toda esta KB**,
  y es el argumento más fuerte que existe para decir «conforme» sin que sea una afirmación propia.

### Las piezas

| Función | Pieza | Licencia |
|---------|-------|----------|
| Generación de ítems | `Educhain` (MCQs, lesson plans, flashcards desde PDF/URL/YouTube) | MIT ✅ |
| Entrega y scoring | `amp-up-io/qti3-item-player` (camino B) o **TAO** (camino A) | MIT ✅ / GPL-2.0 ⚠️ |
| Gate de calidad pedagógica | `EduBench` (transversal a materia, incluye **Automatic Grading** y generación de preguntas) | MIT ✅ |
| Gate de seguridad pedagógica | `SafeTutors` (11 dimensiones de daño, 48 sub-riesgos) | MIT ✅ |
| Matrícula y devolución de notas | `LongsightGroup/oneroster` (OneRoster 1.1/1.2) | MIT ✅ |
| Montaje en el LMS del cliente | `1EdTech/lti-1-3-php-library` | Apache-2.0 ✅ |

### El wiring

1. `Educhain` genera ítems candidatos desde el material del cliente.
2. **Se serializan a QTI 3 XML** — no a un JSON propio. Este paso es el que hace portable todo lo demás.
3. `EduBench` y `SafeTutors` corren como **gate automático** sobre el lote: el ítem que no pasa no llega al revisor.
4. **Revisión humana obligatoria** del lote que pasó el gate. El docente aprueba; el modelo propone (la postura de `tero`).
5. El ítem aprobado se carga en el runtime QTI y **el response processing lo ejecuta la plataforma**, no el LLM — lo que
   mantiene la nota fuera del modelo, que es lo que exigen las jurisdicciones con prohibición de grading automático (P14).
6. `oneroster` devuelve las notas al SIS; LTI 1.3 monta la experiencia dentro del LMS.

### Plazo y alcance

**6–8 semanas** por el camino B con un banco de ítems de una materia. El camino A depende del despliegue de TAO y suma
2–3 semanas. Lo que no hay que subestimar es la **serialización a QTI 3**: el estándar es grande y conviene acotar los
tipos de interacción soportados en el alcance (elección múltiple, respuesta corta y emparejamiento cubren la mayoría).

### Dónde se vende primero

Donde ya hay plataforma de examen y obligación de auditoría: **EMEA** (expediente EU AI Act, P4) y **North America**
(distritos y estados con prohibición de calificación automática, P7 y P14). Es además el patrón que mejor convive con un
incumbente: no reemplaza el LMS, se le enchufa por LTI.

---

## P21 — Due diligence de interoperabilidad: el entregable que el pase 9 convirtió en vendible (agregado en el pase 9; transversal)

**El problema que resuelve, y es real porque esta KB se lo encontró de frente.** La documentación del sector sigue
citando como «la implementación open source» de estos estándares a repos que **ya no existen**. Verificado el 2026-10-01:
`concentricsky/badgr-server` → **404**; `1EdTech/caliper-php` → **404** (puesto en privado por 1EdTech, según el banner
del fork de la Universidad de Michigan); `IMSGlobal/caliper-python` → **404**; los dos repos de credenciales de la
Comisión Europea → **archivados** y mudados a un dominio distinto.

Un equipo que arranca un proyecto de credenciales o de analítica conforme leyendo listicles **va a construir sobre una
URL muerta**, y lo va a descubrir después de haber cotizado.

**El entregable.** Un informe corto y fechado, por estándar (OB 3.0 / W3C VC, QTI, OneRoster, Caliper, LTI, xAPI), con:

1. **Qué URL resuelve hoy** y qué devuelve la que todo el mundo cita. Verificado, no inferido.
2. **La licencia leída en el archivo `LICENSE`**, no la del README ni la del listicle. Esta KB lleva registradas tres
   trampas de este tipo: `FreeLingo` (prensa dice MIT, el repo dice AGPL-3.0), `Teacher-Hub` (*«MIT — free for
   non-commercial use»*, que se contradice), y `openbadgeslib` (**licencia partida**: LGPLv3 la librería, BSD-2-Clause el CLI).
   **Cuarta trampa, agregada en el pase 10 y es la peor de las cuatro:** los bundles de OpenStax en GitHub dicen
   **CC BY-NC-SA** en su `LICENSE` mientras `OATutor` y `openstax-mcp-server` declaran **CC BY 4.0** en su README, sobre el
   mismo contenido. **Y acá el `LICENSE` del repo tampoco alcanza:** OATutor declara que la licencia está **por ítem**, dentro
   de cada JSON. La regla se endurece — **la licencia del contenido no es la licencia del código, y se lee en el ítem**.
3. **La conformidad certificada**, donde exista. En esta capa vale más que las estrellas: `qti3-item-player` tiene
   **30 ★** y certificación de 1EdTech; el repo de 205 ★ de la capa **es una especificación, no código**.
4. **La cadena de custodia.** Quién mantiene hoy. `learner-credential-wallet` pasó del **DCC at MIT** a **OpenWallet
   Foundation Labs** tras la v2.2.10 (jun-2026), y la organización se renombró a **Digital Credentials Commons**.
5. **La recomendación de pinneo**: versión fijada y, donde el riesgo lo justifique, **fork propio en el repositorio del
   cliente** — que es precisamente lo que tuvo que hacer la Universidad de Michigan con Caliper.

**Plazo:** 1–2 semanas. **Cuándo venderlo:** como fase 0 de P19 o P20, o suelto ante un cliente que ya tiene un proyecto
de credenciales en marcha y no sabe sobre qué está construido.

**Por qué es defendible cobrarlo.** No es una búsqueda en GitHub: es **verificación de primera mano de la URL, del archivo
de licencia y del estado de mantenimiento**, en una capa donde las tres cosas cambiaron en los últimos dos años y donde
la fuente secundaria está desactualizada de forma sistemática. Y el costo de no hacerlo se paga entero en implementación.


## P22 — Corpus curricular con licencia auditable: el manifiesto por ítem como entregable (agregado en el pase 10; **transversal, y es condición de posibilidad de P1, P8 y P10**)

**El problema que resuelve.** Todo patrón de esta KB que enseñe algo asume que hay contenido. Diez pasadas no preguntaron de
dónde sale ni con qué licencia. Cuando se pregunta, aparece esto: los bundles de OpenStax en GitHub dicen **CC BY-NC-SA** en
su archivo `LICENSE` (3 de 3 verificados), el ITS que los curó y el servidor MCP que los sirve dicen **CC BY 4.0** en su
README, y el **metadato** del catálogo de referencia del sector (OER Commons / ISKME) es **NonCommercial**.
**NonCommercial prohíbe exactamente el uso de un entregable facturado; ShareAlike obliga a abrir la derivación hecha para el
cliente.** Es el riesgo de licencia más caro de esta KB porque **se descubre después de haber ingestado el corpus**.

**Las piezas, todas verificadas en el pase 10**

| Pieza | Licencia | Rol |
|---|---|---|
| [DSpace](https://github.com/DSpace/DSpace) | **BSD-3-Clause** ✅ | El repositorio donde vive el corpus **con su metadato de licencia por ítem**. 25.385 commits: es la pieza madura y permisiva de la capa |
| [LibreTexts/shapeshift](https://github.com/LibreTexts/shapeshift) | **MIT** ✅ | Extracción y transformación de contenido a formatos de exportación. Es el paso de ingesta, y es permisivo aunque la plataforma LibreTexts sea GPL-3.0 |
| [openstax-mcp-server](https://github.com/pythpythpython/openstax-mcp-server) | **MIT** (código) ✅ | El puente MCP hacia el agente. **Se forkea y se le corrige la declaración de licencia**, que es incorrecta en su README |
| Currículo de **Oak National Academy** | **OGL v3.0** (uso comercial permitido) ⚠️ verificar | El corpus de arranque limpio. Y `Aila` (MIT) es el asistente que ya lo usa |
| [learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) + LRS | **MIT** ✅ | Registrar qué ítem se usó con qué alumno, que es también la evidencia de atribución |

**El wiring, y el orden importa**

1. **Fase 0 — inventario de licencias, antes de ingestar nada.** Por cada fuente candidata: abrir el **archivo `LICENSE`**
   (no el README, no el badge, no el listicle) y, cuando la fuente declare licencia **por ítem**, leer el campo del ítem.
   Clasificar en tres baldes: **apta para uso comercial** (CC BY, OGL, dominio público), **ShareAlike** (usable, contamina la
   derivación) y **NonCommercial** (inutilizable en entregable pago).
2. **Fase 1 — ingesta con el metadato pegado al dato.** `shapeshift` extrae; cada ítem entra a `DSpace` **con su campo de
   licencia, su atribución y su fuente**. Un ítem sin licencia conocida no entra: se registra en la lista de excluidos.
3. **Fase 2 — el corpus del cliente se arma sólo con el balde apto.** Regla dura: **un corpus mezclado es del color de su
   ítem más restrictivo.** Si entra un ítem NC, el corpus entero es NC.
4. **Fase 3 — el agente consulta vía MCP** (fork de `openstax-mcp-server` o adaptador propio contra `DSpace`), y **cada
   respuesta puede citar la atribución del ítem que usó**, que es lo que CC BY exige y casi nadie implementa.
5. **Fase 4 — el manifiesto es el entregable.** Un documento fechado: qué ítems, qué licencia cada uno, qué quedó afuera y
   por qué, y qué obligaciones de atribución quedan vivas en producción.

**Plazo y alcance.** Fase 0 sola: **1–2 semanas**, y se vende suelta como due diligence de contenido (es hermana de **P21**,
que hace lo mismo con los estándares). Fases 0–4 sobre un dominio acotado: **6–8 semanas**.

**Dónde se vende primero.** **EMEA**, por dos razones que se refuerzan: el expediente auditable es lo que pide el EU AI Act,
y el único corpus con licencia explícitamente apta para uso comercial que encontró esta KB —Oak National Academy, OGL v3.0—
es británico. Después **North America**, donde el dinero público nuevo de Q1 2026 está etiquetado **«AI responsable»**.

**Por qué es defendible cobrarlo.** Porque el costo de no hacerlo es rehacer el corpus entero después de la auditoría legal
del cliente, y porque el hallazgo que lo motiva está verificado: **dos fuentes de primera mano declaran licencias
incompatibles sobre el mismo contenido**, y la que la industria repite es la equivocada en al menos tres títulos.

## P23 — Forkear Sunbird para un sistema educativo nacional (agregado en el pase 10; **APAC, LATAM y África**)

**El problema que resuelve.** Hasta el pase 9, la respuesta de esta KB a «plataforma para un ministerio» era Moodle
(GPL-3.0) u Open edX (AGPL-3.0). Las dos obligan a explicarle al cliente que la plataforma abierta que le proponemos lo
compromete a publicar sus modificaciones — y con AGPL, también si la sirve por red. **Sunbird elimina esa conversación.**

**Por qué Sunbird y no otra cosa**

- **MIT** ✅ — el agente vive **adentro**, no al lado.
- **38.046 commits** en el portal. Es la plataforma con más trabajo acumulado de toda esta KB después de TAO, y a diferencia
  de TAO es permisiva.
- **El fork es el modelo de adopción, no un accidente:** **317 forks contra 41 estrellas**, porque cada estado indio levanta
  su instancia. Eso es el precedente de venta: no hay que explicar que *se puede* forkear por jurisdicción — ya se hizo
  decenas de veces.
- **Escala demostrada:** sostiene **DIKSHA**, **180 M+ alumnos**, **290.000+ contenidos**, **36 idiomas**, **4.950 M+
  sesiones**. ⚠️ Cifras de fuente secundaria; lo verificado de primera mano es el repo.
- **Digital Public Good** reconocido por la DPGA — que ante un ministerio o un organismo multilateral es un argumento
  de compra, no un detalle.

**Las piezas**

| Pieza | Licencia | Rol |
|---|---|---|
| [SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** ✅ | El portal web. Se forkea al repositorio del cliente y se fija la versión por tag |
| [sunbird-devops](https://github.com/project-sunbird/sunbird-devops) | **MIT** ✅ | El despliegue. 392 forks: es lo que ejecuta la jurisdicción |
| [SunbirdEd-mobile-app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) | **MIT** ✅ | Android con **consumo offline**. Es lo que hace viable el patrón en ruralidad (converge con **P3**) |
| [sunbird-telemetry-sdk](https://github.com/project-sunbird/sunbird-telemetry-sdk) | **MIT** ✅ | Telemetría nativa, que se puentea a la capa **LRS/xAPI** del pase 6 (**P15**) |
| [Kolibri](https://github.com/learningequality/kolibri) | **MIT** ✅ | Alternativa/complemento offline donde no haya infraestructura para Sunbird completo |
| Agente pedagógico | según el caso | El tutor o el asistente docente, adentro de la plataforma, no como SaaS externo |

**El wiring, en tres fases con corte comercial limpio**

1. **Fase 1 — instancia soberana.** Fork de `SunbirdEd-portal` al repositorio del ministerio, despliegue con
   `sunbird-devops`, versión fijada por tag. Entregable: plataforma corriendo con contenido del cliente y **sin obligación de
   apertura de las modificaciones**.
2. **Fase 2 — telemetría y medición.** `sunbird-telemetry-sdk` puenteado a un LRS xAPI (**P15**), que es la base para
   cualquier medición posterior y para entrenar el estimador de mastery con datos propios (**P16**, que existe justamente
   porque los datasets públicos son NonCommercial).
3. **Fase 3 — el agente adentro.** Tutor o asistente docente sobre el contenido de la plataforma, con el corpus auditado por
   **P22** y el gate de seguridad pedagógica de **P11** antes de abrirlo a alumnos.

**Plazo y alcance.** Fase 1: **6–10 semanas** según integración de identidad y datos existentes. Las tres: **5–7 meses**.

**Dónde se vende primero.** **APAC** —el precedente es local y verificable, y en Singapur el requisito de que la AI viva
dentro de la plataforma estatal (Student Learning Space) empuja exactamente a esta arquitectura— y después **LATAM** y
**África**, donde el patrón de compra es **ministerio + organismo multilateral** y el sello de Digital Public Good pesa.
Para LATAM es además más corto que forkear Moodle, y encaja con la línea de base ya medida por UNESCO/UNU en 19 países.

**La objeción que va a aparecer, y cómo se contesta.** *«41 estrellas, ¿está vivo?»* — 38.046 commits, 317 forks y la
plataforma escolar de India corriendo encima. Ver el **trend 23**: en infraestructura pública **la estrella mide atención de
desarrolladores y el fork mide organizaciones en producción**.

## P24 — Ed-Fi como columna de datos antes del agente (agregado en el pase 10; **North America, K-12**)

**El problema que resuelve.** El pase 9 cubrió los estándares que **mueven** datos educativos —OneRoster (matrícula y notas),
Caliper (eventos), QTI (ítems), Open Badges (credencial)— y dejó afuera el que los **guarda**: el expediente longitudinal del
alumno. En K-12 de EE. UU. eso es **Ed-Fi**, está adoptado a nivel estatal, y **es Apache-2.0**. Un proyecto que mete un
agente en un distrito sin pasar por ahí termina construyendo un silo que el estado no puede leer.

**Las piezas**

| Pieza | Licencia | Rol |
|---|---|---|
| [Ed-Fi-ODS](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | **Apache-2.0** ✅ | Operational Data Store + API. **Se despliega y se consume por API; no se forkea el ODS** |
| [Ed-Fi-Data-Standard](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | **Apache-2.0** ✅ | El modelo de datos. Es el contrato al que hay que programar |
| [LTI 1.3](https://github.com/1EdTech/lti-1-3-php-library) | **Apache-2.0** ✅ | Cómo entra el agente al LMS del distrito sin forkearlo (**P20**) |
| LRS xAPI (`lrsql` / `Ralph`) + [learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | **MIT/Apache** ✅ | La evidencia granular de aprendizaje, que es de otra granularidad que el expediente (**P15**) |
| [tero](https://github.com/marcorojasb/tero) | **MIT** ✅ | La postura de diseño obligatoria en EE. UU.: *el agente propone, el docente decide* (**P18**) |

**El wiring**

1. **Leer, no escribir, al principio.** El agente consume el expediente por la **Ed-Fi ODS API** para contextualizar
   (historia del alumno, cursos, secciones) y **no escribe nada** en el ODS en la fase 1. Es lo que hace aceptable el
   proyecto ante el área de datos del distrito.
2. **La evidencia nueva va al LRS, no al ODS.** xAPI para el detalle de interacción (**P15**); el ODS guarda el expediente
   oficial. Mezclarlos es el error que hace que el distrito pierda la trazabilidad.
3. **La decisión pedagógica queda del lado humano.** Donde haya calificación, componente determinista + explicación del
   modelo (**P14**), porque varios estados prohíben el grading automático.
4. **La credencial, al final** (**P19**), con Open Badges 3.0 cuando corresponda.

**Plazo y alcance.** Integración de lectura contra una instancia Ed-Fi existente: **4–6 semanas**. Con despliegue del ODS:
**3–4 meses**.

**Dónde se vende primero.** **North America**, y el momento es bueno: **41,7%** del crecimiento global del mercado 2026-2030
es de la región y el dinero público nuevo de Q1 2026 (**USD 169 M**) está etiquetado **«AI responsable»** — que es
precisamente lo que describe esta arquitectura. Es también el contra-argumento concreto al programa a nivel país del
incumbente: **soberanía del dato del alumno, sobre un estándar que el estado ya adoptó.**

---
*Ver `intel/market.md` para la oportunidad por región y `intel/trends.md` para los gaps que estos patrones atacan.*

## P25 — Riesgo de abandono conforme al Anexo III, con el humano en el lazo (agregado en el pase 11; **EMEA y North America primero**, y es la capa con presupuesto ya asignado)

**El problema que resuelve, y es el único de esta KB donde el cliente ya tiene la partida abierta.** Toda institución
de educación superior compra *student success* / *early alert*. El open source de esa capa **no existe** (gap 18:
110 repos MIT con techo de 6 ★, el tope entrenado con datos sintéticos, el stack de Apereo archivado). Y la
regulación lo nombra: el **Anexo III del EU AI Act** cubre la evaluación de resultados de aprendizaje, el screening
de postulantes y el monitoreo de exámenes, con fecha **2027-12-02** (Reglamento (UE) 2026/1744). En EE. UU.,
**Oklahoma y Maryland exigen supervisión humana y prohíben que la AI tome decisiones de alto impacto sobre un
alumno**, y **California AB 1159 prohíbe usar datos de alumnos para entrenar modelos**.

**La consecuencia de diseño, y hay que ponerla adelante: el entregable no es el modelo, es el expediente.** Un
modelo de riesgo sin expediente de conformidad es invendible en las dos regiones donde está el dinero.

### Las piezas, todas verificadas en el pase 11

| Capa | Pieza | Licencia | Por qué esta |
|---|---|---|---|
| Motor predictivo | **Analytics API del core de Moodle** | GPL-3.0 (es el core) | Define modelos como *indicadores + target*, los evalúa y entrena internamente, con el target de alumno en riesgo incluido. **Es la base más sólida que existe hoy**, y se extiende por los puntos de extensión del core sin forkear |
| Alternativa / almacén | **OpenLRW** · https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW | **ECL-2.0** ✅ | Si el cliente no es Moodle: *learning record warehouse* que habla **xAPI + IMS Caliper + IMS OneRoster** a la vez — los tres formatos que una universidad realmente tiene. 62 ★, push del 2026-08-04 |
| Telemetría de origen | `yetanalytics/lrsql` o `openfun/ralph` *(capa del pase 6)* | Apache-2.0 ✅ | Donde el agente y el LMS escriben los statements que alimentan el modelo. Ver **P15** |
| Estado del alumno | **pyBKT** (MIT) o **pyKT** (MIT) *(capa del pase 5)* | MIT ✅ | El riesgo de abandono y el mastery son ejes distintos y se venden juntos: un alumno que no domina el prerrequisito es la explicación del riesgo, no un dato aparte. ⚠️ Pero leer el gap 11: **los datasets de knowledge tracing son NonCommercial**, y el entrenamiento se hace con datos del cliente |
| Explicabilidad | **SHAP** por caso | Apache-2.0/MIT ✅ | No opcional: es lo que convierte "el sistema marcó a este alumno" en algo que un tutor puede discutir y un auditor puede revisar |
| **Evidencia de que la intervención sirve** | **Terracotta** · https://github.com/terracotta-education/terracotta | **Apache-2.0** ✅ | RCT dentro del LMS con **consentimiento informado oculto al docente**, filtrado de no-consintientes y remoción de identificadores en las exportaciones. 2.572 commits, push del 2026-09-30 |
| Datos de arranque | **OULAD** (CC BY 4.0) y **UCI 697** (CC BY 4.0 ⚠️ confirmar) | CC BY 4.0 ✅ | Para calibrar el pipeline antes de tocar datos del cliente. ⚠️ **No son el modelo final:** UCI 697 son 4.424 alumnos portugueses de hace una década |
| Expediente | **P4** / **P17** de esta KB | — | La forma del entregable de conformidad ya está resuelta en esta KB para evaluación auditable y accesibilidad. Acá se reusa |

### El wiring

1. **Capa 0 — telemetría antes que modelo.** LRS o OpenLRW recibiendo eventos del LMS y del agente. Sin esto no hay features temporales, y las features temporales son las que predicen (ver abajo).
2. **Features conductuales y temporales, explícitamente sin atributos protegidos.** Logins, asistencia, entrega de trabajos, latencia de entrega, racha de inactividad. **El benchmark de supervivencia sobre OULAD reporta que la señal dominante es temporal y conductual, no demográfica ni estructural** (arXiv 2604.08870 🔴 sin verificar de primera mano). Eso no es una restricción ética que cueste performance: **es el hallazgo que permite no usar los atributos protegidos sin perder exactitud**, y es el argumento que aprueba el sistema ante un DPO.
3. **Modelo en la Analytics API de Moodle** (indicadores + target) o pipeline propio sobre OpenLRW. **Entrenado con datos del cliente, nunca con los del alumno en jurisdicciones donde eso está prohibido** — en California, AB 1159 lo prohíbe de frente.
4. **Salida a persona, no a sistema.** El score va a la bandeja de un tutor con su explicación SHAP y una acción sugerida. **El sistema nunca ejecuta la consecuencia** — ni baja al alumno de categoría, ni cambia su inscripción, ni le manda la notificación automática. Esto es simultáneamente el requisito de supervisión humana del Anexo III y la prohibición de Oklahoma y Maryland: **una sola decisión de arquitectura cubre las dos regulaciones.**
5. **Auditoría de equidad como artefacto publicado, no como párrafo.** Métricas por subgrupo, con el resultado en el expediente. **Ninguno de los repos verificados en el pase 11 publica esto**, y es la diferencia entre un entregable y un notebook.
6. **Terracotta para medir la intervención.** Grupo de tratamiento y control sobre la misma tarea, con el consentimiento ya resuelto. Al final del ciclo se puede decir cuánto bajó el abandono **y con qué intervalo de confianza**, en vez de mostrar la curva del modelo.

### Plazo y alcance

- **Fase 1 — telemetría + expediente (6-8 semanas).** LRS/OpenLRW desplegado, inventario de features, evaluación de impacto y diseño de supervisión humana firmados. **Esta fase se puede vender sola y es la que el cliente aprueba sin discutir**, porque es lo que ya le exige su propio comité.
- **Fase 2 — modelo + explicabilidad + auditoría de equidad (8-10 semanas).**
- **Fase 3 — RCT con Terracotta y medición del efecto (un ciclo académico).** Es la fase que produce el caso de referencia.

### Dónde se vende primero

- **EMEA:** la fecha es el driver. **2027-12-02** son ~14 meses, exactamente el plazo de un programa de conformidad institucional. Y los dos datasets de referencia son europeos y CC BY.
- **North America:** el driver no es una fecha sino una prohibición vigente que deja al cliente con presupuesto y sin forma legal de gastarlo como pensaba. **La fase 1 y el punto 4 del wiring son literalmente el producto.** 38% del mercado global.
- **LATAM:** el método ya existe y es local —papers brasileños con features validadas sobre datos reales de institutos federales, ausentismo como predictor dominante— y el dato está en el SIS. Lo que falta es la ingeniería. Ver `intel/market.md`.
- **APAC:** Vietnam ya nombró la **evaluación automatizada y el monitoreo del comportamiento** como alto riesgo en educación; se vende como P5 multi-jurisdicción con este patrón adentro.

### ⚠️ Lo que no hay que prometer en este patrón

- **No proponer ningún repo de la capa predictiva de GitHub como base de producto.** Techo de 6 ★, datos sintéticos, licencias ausentes o `NOASSERTION`. Sirven para leer feature engineering, nada más.
- **No proponer Apereo SSP, OpenDashboard ni LearningAnalyticsProcessor.** Verificado en el pase 11: el primero no tiene repo localizable, el segundo está declarado *(Deprecated)* y su reemplazo se abandonó en 2020, el tercero no tiene push desde enero de 2023.
- **No presentar métricas de los papers como métricas esperables.** Los accuracy de 0,87 y los AUC de 0,96 que circulan en esta capa están medidos sobre 4.424 registros de una institución europea. Con los datos del cliente, el número se mide; no se promete.

## P26 — Agente docente conforme al currículo nacional, con la ontología ya publicada (agregado en el pase 11; **APAC primero, EMEA segundo**)

**El problema que resuelve.** El patrón **P8** (fábrica de lecciones en la voz del docente) y el **P6** (AI literacy a
escala de sistema educativo) chocan siempre con la misma pieza: **el currículo nacional estructurado.** Es el artefacto
más caro de construir de un agente docente —hay que leer el currículo oficial, modelarlo, validarlo y mantenerlo— y es
el que ningún ministerio quiere pagar dos veces. **El pase 11 encontró que, para dos países, ya está publicado.**

### Las piezas

| Pieza | Licencia | Región | Qué aporta |
|---|---|---|---|
| **korean-elementary-learning-map** · https://github.com/DECK6/korean-elementary-learning-map | **MIT** ✅ | APAC (Corea del Sur, currículo revisado 2022) | **620 anclas de estándares de logro, 1.956 temas, 2.293 relaciones de prerrequisito, 152 clusters**, 11 materias, grados 1-6. **JSON y RDF/Turtle**, con *competency questions* en **SPARQL** y restricciones **SHACL**. ⚠️ Construcción independiente, **no producto oficial del Ministerio** |
| **OpenDidactia** · https://github.com/nmarafo/OpenDidactia | CC BY-SA 4.0 ⚠️ | EMEA (España, LOMLOE) | Esquemas de Programación Didáctica y Situación de Aprendizaje para 17 comunidades + 2 ciudades autónomas, con DUA y rúbricas. ⚠️ **Share-alike:** derivar el esquema para el cliente dispara la obligación de publicar |
| **mentar** · https://github.com/avps82/mentar | AGPL-3.0-only ⚠️ | — | Referencia de cómo se consume: **934 nodos de concepto en 157 plantillas curriculares** (ACARA v9 de Australia, India, Singapur, EE. UU.) con **checker determinístico** en vez de dejar que el modelo valide |
| **Gnos** · https://github.com/madhvantyagi/Gnos | **MIT** ✅ | — | *Teaching harness* cuyo registro de evidencia distingue **"vio la explicación" / "resolvió con ayuda" / "resolvió solo"** — la granularidad que el grafo de prerrequisitos necesita para decidir el siguiente nodo |
| **Alvarmethod** · https://github.com/vasanthsreeram/Alvarmethod | **MIT** ✅ | — | El loop pedagógico como skill portable: *probe → plan (DAG) → teach → lock-in*. **El `plan` es exactamente un recorrido sobre el grafo de prerrequisitos**, así que las dos piezas encajan sin adaptador |
| **pyBKT** / **pyKT** | MIT ✅ | — | Estimación de mastery por nodo del grafo |

### El wiring

1. **El grafo de prerrequisitos es la fuente de verdad, no el prompt.** Se carga la ontología (JSON para la aplicación, RDF/Turtle si el cliente ya tiene triple store) y se validan las restricciones **SHACL** en CI: si el ministerio cambia el currículo, el build falla antes que el agente alucine.
2. **`Alvarmethod` para el loop, con el `plan` recorriendo el grafo** en vez de pidiéndole al LLM que invente la secuencia. La diferencia es auditable: el plan de estudio queda trazado contra anclas de estándares oficiales.
3. **`pyBKT` estima mastery por nodo**, y las *competency questions* SPARQL de la ontología se reusan como consultas de cobertura: "¿qué estándares de 4.º grado cubrió este alumno?" es una consulta, no un reporte a mano.
4. **`Gnos` para la captura de evidencia** con la distinción de los tres niveles de ayuda. Sin eso, el mastery se estima sobre "respondió bien" y vale poco.
5. **El checker determinístico de `mentar` como patrón** —no como dependencia, que es AGPL—: **el LLM explica, un verificador no-LLM corrige.** Es la única forma de que el agente no le dé por bueno un error a un chico.
6. **Telemetría a LRS** (P15) para que la cobertura curricular sea un dato consultable por el ministerio y no una captura de pantalla.

### Plazo y alcance

- **6-8 semanas** para un piloto de una materia y un grado sobre un currículo **que ya tiene ontología publicada** (Corea del Sur hoy; España con la advertencia de licencia).
- **12-16 semanas** si hay que **construir la ontología** del país. Esa es la fase cara, y el gap 19 dice que conviene mirar primero si alguien ya la publicó: Brasil (BNCC), Reino Unido, Australia (ACARA, que `mentar` ya consume) y los estándares estatales de EE. UU. son candidatos sin verificar.

### Dónde se vende primero

- **APAC:** es la única región con la pieza **MIT**, completa y formalmente validada. Un engagement de currículo nacional empieza con el artefacto más caro ya resuelto y sin fricción de licencia.
- **EMEA:** España tiene el esquema, pero es **CC BY-SA**. Se puede usar como referencia y **hay que decidir adelante** si el esquema derivado se publica o se construye uno propio — es una decisión comercial, no técnica, y tomarla tarde cuesta.
- **LATAM:** la BNCC de Brasil es el equivalente obvio y **nadie verificó si está publicada en formato estructurado.** Si no lo está, construirla con autoría local es exactamente el tipo de aporte que el gap 2 recomienda, y es reusable en todo el país.

## P27 — Biblioteca de skills pedagógicas permisiva y con *eval* desde el día uno (agregado en el pase 12; **LATAM primero por autoría, North America y EMEA por demanda regulada**)

**El problema que resuelve.** Todos los patrones anteriores de esta KB arrancan desplegando algo: Moodle con plugin
(P1), OpenMAIC (P1), Sunbird forkeado (P23), Ed-Fi como columna de datos (P24). Eso pone el primer entregable a
semanas de distancia y mete al cliente en costo de infraestructura antes de que haya visto valor pedagógico. **El
estándar Agent Skills permite entregar pedagogía sin desplegar nada** —el artefacto es Markdown y corre en el harness
que el cliente ya paga— y el pase 12 midió que **la vertical educativa no ocupó ese canal: pierde 58× contra la
científica.** El hueco no es técnico ni de licencia: está vacío.

**Y el diferencial del patrón no es publicar la biblioteca: es publicarla medida.** Ninguno de los siete paquetes
pedagógicos que existen en el mundo tiene *eval* (gap 20). Una biblioteca que nazca con suite de evaluación no es la
octava de la lista: es la primera medible.

### Las piezas

| Pieza | Licencia | Qué aporta |
|---|---|---|
| **scientific-agent-skills** · https://github.com/K-Dense-AI/scientific-agent-skills | **MIT** ✅ | **La arquitectura de referencia**, y es copiable: 181 skills + 100+ bases de datos + 70+ workflows, con 47.2k ★ de validación. **Se copia la estructura, no el contenido** |
| **learning-commons-org/agent-skills** · https://github.com/learning-commons-org/agent-skills | **Apache-2.0** ✅ | El patrón de *guardrails* por workflow docente y alineación a estándares K-12. Es el único de la capa pensado para cumplimiento curricular, y es empaquetable |
| **book-to-skill** · https://github.com/virgiliojr94/book-to-skill | **MIT** ✅ | Pipeline contenido → skill: `SKILL.md` con modelos mentales (~4k tokens), un archivo por capítulo on-demand, glosario, patrones, cheatsheet. **Procesa local** |
| **UnifyingAITutorEvaluation** · https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | Taxonomía de evaluación de tutor. **Usar para medir internamente, no empaquetar** |
| **MathTutorBench** · https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | Capacidades pedagógicas abiertas en matemática. Atribución, sin *share-alike* |
| **EduGuardBench** · https://github.com/YL1N/EduGuardBench · **EduBench** · https://github.com/ybai-nlp/EduBench | ver sus filas en `agents/top.md` | Seguridad pedagógica y cobertura de escenarios educativos |
| **universal-examprep-skill** · https://github.com/ZeKaiNie/universal-examprep-skill | **MIT** ✅ | Referencia de **cita de página sobre la fuente** como mecanismo anti-alucinación. Es el patrón a copiar, y es permisivo |
| ⚠️ **education-agent-skills** · https://github.com/GarethManning/education-agent-skills | **CC BY-SA 4.0** ⚠️ | 165 skills en 20 dominios. **Referencia de cobertura de dominios — NO derivar de acá si el entregable es cerrado** |

### El wiring

1. **Fijar la taxonomía de dominios antes de escribir una skill.** Se lee `education-agent-skills` (20 dominios) y
   `scientific-agent-skills` (181 skills) **como mapa de cobertura**, y se decide el subconjunto propio. ⚠️ Leer no es
   derivar: el texto se escribe de cero con autoría propia, porque CC BY-SA contamina el derivado.
2. **Estructura por skill, copiada de la arquitectura MIT:** `SKILL.md` con el modelo mental y el índice (~4k tokens),
   un archivo por sub-tema cargado on-demand, glosario, patrones y cheatsheet de decisión. Es lo que hace que una
   biblioteca de 100+ skills no reviente el contexto.
3. **Los *guardrails* van en la skill, no en el prompt del usuario**, con el patrón de `learning-commons-org/agent-skills`
   (Apache-2.0, derivable): qué verificar primero, qué ignorar, qué formato de salida, contra qué estándar se alineó.
4. **Atribución obligatoria a la fuente**, con el patrón de `universal-examprep-skill`: toda afirmación curricular cita
   el material de origen con página. Es lo que convierte la skill en artefacto auditable y no en opinión del modelo.
5. **Contenido:** `book-to-skill` convierte el corpus del cliente —o un OER con licencia apta— en skill estructurada.
   ⚠️ **La advertencia del pase 10 es acá donde más pega:** la licencia de la fuente se verifica **antes** de convertir,
   porque el Markdown de salida **no arrastra el archivo `LICENSE`** y después no se ve. Los bundles de OpenStax en
   GitHub dicen **CC BY-NC-SA** en los tres títulos revisados.
6. **La suite de eval es parte del repo, no un anexo.** Cada release corre MathTutorBench (capacidad pedagógica),
   EduGuardBench (seguridad) y la taxonomía de UnifyingAITutorEvaluation (calidad de feedback) **contra las skills**,
   y publica el resultado versionado. Esto no existe hoy en ninguna de las siete bibliotecas del mundo.
7. **Versionado semántico y changelog pedagógico.** Una skill es un artefacto de comportamiento: si cambia, cambia la
   enseñanza. Sin SemVer no hay forma de que una escuela declare qué versión usó en el ciclo.

### Plazo y alcance

- **2-3 semanas** para una biblioteca vertical de 10-15 skills de una materia y un nivel, con eval corriendo en CI.
  **No hay infraestructura que desplegar**, y ése es el punto: es el entregable más rápido de toda esta KB.
- **8-10 semanas** para cobertura de 60-80 skills multi-materia con suite de eval completa y changelog pedagógico.
- **Costo de infraestructura: cero.** Corre en Claude Code, Codex, Cursor, Antigravity, Gemini CLI o Copilot CLI — los
  seis leen el mismo `SKILL.md`, así que el artefacto es portable y no genera *lock-in* de harness.

⚠️ **Lo que este patrón NO entrega, y hay que decirlo antes de cotizar.** Una skill no produce evidencia de
aprendizaje: no hay telemetría, no hay credencial y no hay registro institucional. Si el cliente necesita acreditar,
este patrón es la **capa pedagógica** y hay que combinarlo con P15 (telemetría a LRS) y P19-P21 (credenciales). Un
piloto de skills es barato de empezar y **no es acreditable tal como viene.**

### Dónde se vende primero

- **LATAM:** es el vacío medido del pase 12 —**cero** bibliotecas de skills educativas de origen LATAM o en español,
  contra 1 de EMEA, 4 de APAC y 1 de North America— y es la región de origen de Globant, donde el contenido pedagógico
  en español ya está. Es el gap más barato de cerrar de los veinte declarados y el único donde la autoría regional es
  en sí misma el diferencial. `tero` (MIT, Chile) ya demostró que un artefacto chico y permisivo de origen chileno
  entra en esta KB por mérito propio.
- **North America:** es donde está la **demanda regulada**. Cuatro estados (MD, ID, OK, VA) exigen política distrital
  de AI con supervisión humana, y una skill con *guardrails* y atribución **deja rastro en texto revisable** — la forma
  de evidencia que ese mandato pide. La oferta open source en esa capa es un repo de 35 ★.
- **EMEA:** el Anexo III exige trazabilidad de **cómo** se tomó la decisión pedagógica, y una skill es texto auditable
  —se lee, se versiona, se diferencia—, mucho más fácil de documentar frente a un auditor que un modelo fine-tuneado.
  Pero el activo europeo de referencia es **CC BY-SA**, así que el entregable defendible es una biblioteca permisiva
  propia, no un derivado del británico.
- **APAC:** es la región que **ya está produciendo** esta capa (4 de 7 paquetes). Entrar acá es competir, no llenar un
  hueco. El ángulo distinto es el eval: ninguno de los cuatro lo tiene.

## P28 — Retención del alumno sobre el SRS que ya está instalado, en vez de construir el motor (agregado en el pase 12; **transversal a las cuatro regiones**)

**El problema que resuelve.** El pase 5 encontró **cinco servidores MCP de mastery** —grafo de prerrequisitos,
scheduler, esquema de progreso— construidos por cinco autores sin relación, **ninguno arriba de 1 ★**. La lectura de
entonces fue "validación de mercado". El pase 12 agrega el término de comparación que faltaba y da vuelta la
conclusión: **`anki-mcp-server` tiene 499 ★ con la misma tecnología y la misma licencia**, y la diferencia es que no
inventa el modelo de dominio: expone el que el alumno **ya tiene instalado**.

Dicho de otro modo: el motor de repetición espaciada es un problema resuelto, desplegado en más de 3 millones de
dispositivos sólo en Android, y con el algoritmo moderno (**FSRS**) integrado de fábrica desde la versión 23.10 (2023).
**Construirlo de nuevo es la forma más cara de llegar a peor.**

### Las piezas

| Pieza | Licencia | Qué aporta |
|---|---|---|
| **Anki** · https://github.com/ankitects/anki | **AGPL-3.0-or-later** ⚠️ (porciones de contribuyentes BSD-3; verificado en el archivo `LICENSE`) | El SRS de facto: 31.7k ★, **+3 M de usuarios sólo en Android**, FSRS integrado desde 23.10. **Corre en la máquina del alumno** |
| **anki-mcp-server** · https://github.com/ankimcp/anki-mcp-server | **MIT** ✅ | 499 ★, 254 commits, v0.22.0 (beta declarada). Puente MCP: crear, leer y revisar mazos en lenguaje natural desde el agente |
| **AnkiConnect** (add-on, v25.11.9.0 del 2025-11-02) | — | La API HTTP local sobre `localhost` que es **la frontera de proceso** del patrón |
| **py-fsrs** · https://github.com/open-spaced-repetition/py-fsrs | **MIT** ✅ | FSRS del lado del servidor **para razonar y simular**, no para reimplantar el scheduler |
| **pyBKT** · https://github.com/CAHLR/pyBKT · **pyKT** · https://github.com/pykt-team/pykt-toolkit | **MIT** ✅ | Mastery por concepto, que es la pregunta que el SRS **no** responde (el SRS sabe cuándo repasar una tarjeta, no si el alumno domina el tema) |
| **Gnos** · https://github.com/madhvantyagi/Gnos | **MIT** ✅ | Registro de evidencia con los tres niveles de ayuda ("vio la explicación" / "resolvió con ayuda" / "resolvió solo") |

### 🔴 La condición de licencia, y es la que hace viable el patrón

**Anki es AGPL-3.0-or-later.** En el resto de esta KB eso sería una advertencia fuerte. Acá no lo es, por arquitectura:

- **No se forkea Anki ni se enlaza contra su código.** Se le habla por **AnkiConnect**, una API HTTP sobre `localhost`,
  desde un **proceso separado** (`anki-mcp-server`, MIT).
- Es exactamente la regla 2 que esta KB ya tenía escrita en `repos/foundations.md`: *«la lógica propietaria vive en un
  servicio aparte — el agente es un proceso separado con su propia licencia, hablando por API/MCP»*.
- **Anki corre en el dispositivo del alumno, no en infraestructura del cliente.** No hay distribución de un derivado y
  no hay servicio de red operado por el cliente: los dos disparadores de la AGPL quedan afuera.

⚠️ **Lo que sí hay que revisar con legal:** empaquetar, redistribuir o preinstalar Anki —o un *fork* con marca del
cliente— como parte del entregable. Ahí la AGPL aplica de lleno. Proponerlo como **cliente que el alumno ya tiene**
es otra cosa.

### El wiring

1. **El agente enseña; Anki retiene.** Terminada una sesión de tutoría (cualquiera de los tutores de P1, P7 o P27), el
   agente emite las tarjetas de lo trabajado **vía `anki-mcp-server`** al mazo del alumno. No hay base de datos de
   repaso del lado del cliente.
2. **El scheduler no se toca.** FSRS ya está en Anki. `py-fsrs` se usa del lado servidor **sólo para simular** —"¿cuánta
   carga de repaso genera este plan de estudio en 8 semanas?"— y para dimensionar el currículo, nunca para decidir el
   intervalo. Esa decisión queda en el cliente del alumno.
3. **El mastery es otra pregunta y necesita otra pieza.** `pyBKT` estima dominio **por concepto** a partir de la
   evidencia; el SRS sólo sabe de tarjetas. Las dos señales se combinan: *tarjeta vencida* (Anki) + *concepto no
   dominado* (pyBKT) = el tema vuelve a la sesión de tutoría, no sólo al mazo.
4. **La evidencia se captura con la distinción de `Gnos`**, porque "respondió bien" sin saber si fue con ayuda hace que
   el mastery estimado valga poco.
5. **La telemetría institucional va por LRS (P15), no por Anki.** Anki es del alumno y es local: lo que la institución
   necesita saber —cobertura, progreso, riesgo— se emite como xAPI desde el agente, no leyendo el mazo. **Esto es
   también lo que mantiene el patrón del lado correcto de la privacidad:** el historial de repaso nunca sale del
   dispositivo.

### Plazo y alcance

- **2-3 semanas** para enchufar `anki-mcp-server` a un tutor existente y tener emisión de tarjetas funcionando.
- **5-7 semanas** con mastery (`pyBKT`) y captura de evidencia (`Gnos`) combinados, más la emisión xAPI al LRS.
- ⚠️ **`anki-mcp-server` declara estado beta (v0.22.0).** Es la pieza más joven del patrón y la que hay que fijar por
  versión y cubrir con tests de integración propios antes de ponerla en un entregable.

### Dónde se vende primero

**Es transversal a las cuatro regiones**, y es uno de los pocos patrones de esta KB del que se puede decir eso con
fundamento: Anki no depende de currículo nacional, de estándar de interoperabilidad ni de régimen regulatorio, porque
corre del lado del alumno.

- **Donde más rinde** es en preparación de examen y certificación profesional, que es donde el SRS ya es la herramienta
  que el alumno elige solo. `kaogong-skill` (APAC) y `universal-examprep-skill` son la evidencia de que ese segmento
  está demandando exactamente esto.
- **Y donde conviene decirlo explícitamente en la propuesta** es en EMEA: el historial de repaso **no sale del
  dispositivo**, así que la capa de retención no agrega superficie de alto riesgo bajo el Anexo III ni datos personales
  nuevos que gobernar. Es un argumento de arquitectura, no de cumplimiento, y es más fuerte por eso.

---

## P29 — Capa pedagógica sobre la pila de práctica que ya está instalada (agregado en el pase 13; **North America y EMEA primero**, y es el patrón de menor costo de entrada de toda esta KB)

**El patrón invierte el orden de operaciones de P1.** P1 construye el tutor y después le busca dónde enchufarse. Acá la
infraestructura ya existe, es **BSD-3-Clause**, está desplegada desde 2014 y **ya trae runtime de agente**: lo único que
se construye es la capa pedagógica. Aplica a cualquier cliente donde **el trabajo del alumno sea ejecutable** —ciencia
de datos, ingeniería, programación, estadística, física computacional, formación técnica—.

### Las piezas, todas verificadas vía WebFetch en el pase 13

| Pieza | Licencia | Stars | Rol |
|---|---|---|---|
| https://github.com/jupyterhub/ltiauthenticator | **BSD-3-Clause** ✅ | 73 | **Entrada por LTI 1.3** desde el LMS del cliente. Probado contra **Open edX, Canvas y Moodle** |
| https://github.com/jupyterhub/jupyterhub | **BSD-3-Clause** ✅ | **8.300** | Entorno aislado por alumno, en el navegador |
| https://github.com/jupyter/nbgrader | **BSD-3-Clause** ✅ | **1.400** | Asignación, recolección, autocorrección, **tests ocultos** y tramo de corrección **manual**. v0.9.6 del 2026-09-30 |
| https://github.com/ucbds-infra/otter-grader | **BSD-3-Clause** ✅ | 161 | Alternativa a nbgrader **cuando el cliente no va a operar JupyterHub** |
| https://github.com/jupyterlab/jupyter-ai | **BSD-3-Clause** ✅ | **4.400** | **La capa de agente, y no hay que construirla.** ACP + servidores MCP propios |
| https://github.com/DavidLMS/learnmcp-xapi | MIT ✅ | 15 | Puente MCP → **xAPI**: convierte la actividad en evidencia conforme al estándar |
| https://github.com/yetanalytics/lrsql | Apache-2.0 ✅ | — | **LRS**: el almacén de evidencia (capa 0 del patrón **P15**) |
| https://github.com/CAHLR/pyBKT | MIT ✅ | 281 | Estimación de **mastery** sobre la evidencia (gap 5, patrón **P12**) |

**Cero copyleft en la pila. Cero NonCommercial. Cero fork del core del LMS.**

### El wiring

1. **El alumno entra desde el LMS que ya usa.** `ltiauthenticator` con **LTI 1.3**: el alumno hace clic en la actividad
   dentro de Moodle, Canvas u Open edX y aterriza autenticado en su entorno. **No se forkea el core AGPL/GPL del LMS**,
   que es la regla que `repos/foundations.md` viene recomendando desde la tercera pasada.
2. **El docente escribe el assignment una vez.** En `nbgrader`: celdas autocorregidas, **tests ocultos** que el alumno no
   ve, y tramos marcados para corrección manual. El artefacto es del docente, así que **no hay problema de licencia de
   contenido** (gap 15, pase 10) y **no hay fuente de datos no controlada** —que es exactamente lo que el inciso (a) de
   la ley de Vietnam castiga (trend 31)—.
3. **La corrección determinística corre primero, y el modelo no participa.** `nbgrader` autocorrige contra los tests. La
   nota de esa parte **la produce código, no un LLM**. Esto es lo que vuelve el patrón defendible donde la decisión
   automatizada está prohibida (Oklahoma, Maryland, Anexo III, Vietnam inciso (b)).
4. **Recién acá entra el agente, y sólo para explicar.** `jupyter-ai` dentro del notebook, con un servidor **MCP** propio
   que recibe *(el test que falló, el caso de prueba, el código del alumno)* y devuelve **feedback formativo**: qué
   concepto falta, no cuál es la respuesta. Es el ángulo que el pase 5 ya había identificado como correcto —«explicación
   y feedback sobre tests que ya corrieron»— y ahora tiene dónde vivir.
5. **La evidencia sale al LRS.** `learnmcp-xapi` emite las sentencias xAPI a `lrsql`: qué intentó, cuántas veces, qué
   test falló, qué explicación recibió. Eso es el expediente, y es la pieza que ninguna herramienta propietaria entrega.
6. **El mastery se estima sobre evidencia real del cliente.** `pyBKT` sobre las sentencias del LRS. ⚠️ **En California,
   AB 1159 prohíbe usar datos de estudiantes para *entrenar* modelos**: acá el uso es **estimación/inferencia**, no
   entrenamiento, y esa distinción hay que **escribirla en la propuesta**, no asumirla.
7. **El docente decide.** Ninguna nota sumativa se emite sin revisión humana; el tramo manual de `nbgrader` es el lugar
   donde eso ya está previsto por diseño.

### Plazo y alcance

- **Fase 1 (3–4 semanas):** LTI 1.3 + JupyterHub + nbgrader sobre una materia piloto, con los assignments existentes del
  docente migrados. Entregable: la cohorte corrige automáticamente lo ejecutable.
- **Fase 2 (4–5 semanas):** servidor MCP de feedback formativo + `jupyter-ai` en el notebook. Entregable: explicación por
  test fallado, con el docente revisando una muestra.
- **Fase 3 (4–6 semanas):** `learnmcp-xapi` + `lrsql` + `pyBKT`. Entregable: tablero de mastery por concepto y expediente
  de evidencia por alumno.
- **Total: 11–15 semanas**, y las tres fases tienen corte comercial limpio: la fase 1 ya es valor entregado sin AI.

### Dónde se vende primero

- **North America.** La pila es de autoría local (Jupyter/NumFOCUS; `otter-grader` del **DSEP de UC Berkeley**) y está
  desplegada en **UC Berkeley y Cal Poly**: la infraestructura es familiar y el argumento de no-decisión-automatizada
  encaja con lo que **Oklahoma y Maryland** exigen y con lo que **CA AB 1159** restringe.
- **EMEA, y es la mejor propuesta de la región.** Ya está instalada en la **Universidad de Edimburgo** y en **Aalto**. El
  cliente no necesita migrar nada: necesita **el expediente de conformidad del Anexo III (2027-12-02)** sobre lo que ya
  corre. Es **P4 aplicado a P29**, y se vende como auditoría + remediación, no como plataforma.
- **APAC, con el reloj más corto.** El vencimiento educativo de **Vietnam es 2027-09-01**, antes que el europeo. El
  diseño de los pasos 3 y 4 —corrección determinística, LLM sólo explicando— es la respuesta directa al inciso (b).
- **LATAM.** Aplica igual, y es más barato que cualquier plataforma: dentro del **87% de instituciones que ya usan AI con
  herramientas de propósito general** (trend 32), esto es lo primero que convierte ese uso informal en algo gobernado.

### ⚠️ Dónde NO proponerlo

**Si el trabajo del alumno no se ejecuta, este patrón no aplica.** Para derecho, historia, lengua o ciencias sociales no
hay análogo —es el **gap 21**— y el incumbente de la corrección de prosa sigue siendo propietario (**gap 6**, mitad no
cerrada): ahí el camino sigue siendo orquestar Gradescope (`gradescope-mcp`) y el patrón **P14**. Presentar P29 a una
facultad de humanidades es un error de encaje que se detecta en la primera reunión.

---

## P30 — Acreditar la competencia pedagógica del asistente contra el examen del Estado (agregado en el pase 13; **LATAM primero por autoría, North America segundo por educación especial**)

**El problema que resuelve.** Esta KB tiene desde el pase 4 un stack de evaluación pedagógica que nadie usa (gap 1:
*«el estándar existe, está publicado en los venues principales, y sigue sin adoptarse»*). La razón práctica es que
ninguno de esos benchmarks responde la pregunta que hace el comprador institucional, que no es *«¿qué tan bueno es tu
modelo?»* sino **«¿por qué debería creer que esto sabe enseñar?»**. `pedagogy-benchmark` responde exactamente eso, porque
**la vara no la puso un laboratorio: la puso el Estado**, y es la misma con la que se habilita a un docente humano.

### Las piezas, verificadas en el pase 13 y en pasadas anteriores

| Pieza | Licencia | Stars | Qué acredita |
|---|---|---|---|
| https://github.com/AI-for-Education/pedagogy-benchmark | **MIT** ✅ | 12 | **CDPK (920 preguntas)**: conocimiento pedagógico general, transversal a materias, edades y subdominios. **SEND (223)**: educación especial. Fuente: exámenes de habilitación docente de la **Agencia de la Calidad de la Educación** y el **CPEIP del Ministerio de Educación de Chile**. arXiv 2506.18710 |
| https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | 32 | Taxonomía de **8 dimensiones** pedagógicas ante el error del alumno (MRBench). NAACL 2025 |
| https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | 42 | **Enseñanza en diálogo**: andamiaje, no resolución. EMNLP 2025 (Oral) |
| https://github.com/ybai-nlp/EduBench | **MIT** ✅ | 29 | 9 contextos educativos, transversal a materia, con cuatro escenarios docentes |
| https://github.com/RadiantCrystal/SafeTutors | **MIT** ✅ | 0 | **Daño pedagógico**: si enseña mal siendo amable |

**El reparto de trabajo entre ellas es el punto, y es lo que ninguna sola cubre:** `pedagogy-benchmark` mide
**conocimiento declarativo** (sabe pedagogía), `MathTutorBench` y `UnifyingAITutorEvaluation` miden **conducta en
diálogo** (sabe enseñar), `SafeTutors` mide **daño**. Presentar una sola como «evaluación pedagógica» es el error que el
pase 7 marcó con `ProHist-Bench`.

### El wiring

1. **Correr CDPK contra la configuración concreta del cliente** —el modelo elegido, con su *system prompt*, sus skills y
   su RAG—, no contra el modelo desnudo. Lo que se acredita es **el producto**, no el proveedor del LLM.
2. **Correr `SEND` aparte y reportarlo aparte.** Es la pieza que decide la venta en educación especial y **no conviene
   promediarla** con CDPK: un asistente puede estar bien en pedagogía general y mal en discapacidad, y ese promedio
   esconde exactamente el riesgo que el distrito teme.
3. **Agregar la capa conductual**: `MathTutorBench` + las 8 dimensiones de `UnifyingAITutorEvaluation` sobre diálogos
   reales del piloto. ⚠️ `UnifyingAITutorEvaluation` es **CC BY-SA 4.0**: derivar un benchmark propio con datos del
   cliente **dispara el *share-alike***. Usarlo como vara de medición es limpio; derivarlo y no publicar, no.
4. **Agregar el gate de seguridad**: `SafeTutors` (patrón **P11**) como criterio de bloqueo, no como métrica informativa.
5. **El entregable es un expediente, no un número.** *Dossier de competencia pedagógica*: resultado por subdominio, el
   delta contra el modelo base, los casos fallados con su transcripción, y el criterio de regresión para la próxima
   versión. **Eso es lo que firma un ministerio o un distrito**, y es reusable como artefacto de conformidad bajo el
   Anexo III, la ley de Vietnam y los estatutos estatales de EE. UU.

### Plazo y alcance

- **2 semanas** para el dossier CDPK + SEND sobre una configuración existente. Es un entregable corto y autónomo: se
  puede vender como diagnóstico de entrada antes de cualquier desarrollo.
- **+3 semanas** para la capa conductual y el gate de seguridad sobre diálogos del piloto.
- **Total 5 semanas**, y es el patrón más barato de esta KB después de **P27**.

### Dónde se vende primero

- **LATAM, y el argumento es de autoría.** Ante un ministerio de la región el pitch no es *«les traemos una
  herramienta»*: es **«la vara con la que el mundo está midiendo a estos modelos son los exámenes docentes de Chile, y
  ustedes producen ese mismo activo sin capitalizarlo»**. Los exámenes de habilitación, las pruebas estandarizadas y los
  marcos de competencias de los ministerios son datos de evaluación de altísimo costo de producción. **Extenderlos a más
  países de la región es un entregable de política pública que no compite con ningún proveedor.** Ver el **gap 22**.
- **North America, por educación especial.** El pase 8 documentó que redactar el IEP con AI está prohibido o restringido
  en varios estados, y el patrón **P18** puso el límite adelante (*el agente propone, el docente decide*). Lo que le
  faltaba a P18 era **cómo demostrarle al distrito que el asistente es competente** sin tocar la decisión protegida.
  **`SEND` es ese instrumento**, y es MIT. Con **35+ estados con guía oficial** y **cuatro que obligan a política
  distrital** (Maryland, Idaho, Oklahoma, Virginia), el dossier es material de cumplimiento, no marketing.
- **EMEA y APAC** lo consumen como insumo del expediente de conformidad (**P4**), no como producto propio.

### ⚠️ Los límites, y van en la primera página del dossier

- **12 estrellas y 5 commits.** `pedagogy-benchmark` es un artefacto de investigación: **se usa como vara de medición en
  un entregable, no se empaqueta como dependencia de producto.** Pinear el commit.
- **Mide conocimiento declarativo, no calidad de intervención.** Responder un examen de habilitación no es enseñarle a
  un chico. Por eso los pasos 3 y 4 no son opcionales.
- 🔴 **El paper (arXiv 2506.18710) no se pudo abrir** en el pase 13 —`arxiv.org` bloqueado por el proxy—. Licencia,
  conteos, composición CDPK/SEND y la atribución a Chile **sí** están verificados en la página del repo. **Abrir el paper
  antes de citar metodología en un entregable.**

---

## P31 — Publicar el currículo nacional como marco CASE conforme, y usarlo de eje del agente docente (agregado en el pase 14; **las cuatro regiones, con artefacto distinto en cada una**)

Es el patrón que cierra el gap 19 y abre el 23. Resuelve el problema más caro de cualquier agente docente —el mapa de
qué se enseña, en qué grado, en qué orden y con qué prerrequisitos— **sin construirlo**, y lo deja publicado contra un
estándar auditable en vez de en un JSON propietario del proyecto.

### Las piezas, todas verificadas vía WebFetch el 2026-10-01

**Capa 0 — el esquema curricular, uno por región:**

| Región | Artefacto | Licencia | Qué trae |
|---|---|---|---|
| **EMEA** | [`fh-yarbouh/oak-curriculum-ontology`](https://github.com/fh-yarbouh/oak-curriculum-ontology) (0 ★) | **OGL-3.0** datos + **MIT** código | 50.948 *key learning points*, **11.207 *misconceptions***, 7.432 prerrequisitos, 160 *threads*, 12 materias, 38 *shapes* SHACL |
| **LATAM** | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) (19 ★) | **MIT** código + **CC BY 4.0** datos | 1.721 aprendizagens, JSON/SQLite/CSV, proveniencia por registro |
| **North America** | [`commonstandardsproject/api`](https://github.com/commonstandardsproject/api) (44 ★) | **Apache-2.0** | Estándares de los 50 estados + distritos, API en vivo |
| **APAC** | [`DECK6/korean-elementary-learning-map`](https://github.com/DECK6/korean-elementary-learning-map) | **MIT** | 620 anclas, 1.956 temas, **2.293 prerrequisitos**, SPARQL + SHACL |

**Capa 1 — publicación conforme:** [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) (**Apache-2.0**, 9 ★),
**certificado para CASE Service v1.0 y CASE v1.1 con fecha 2026-02-17**. Alternativa Python:
[`infosign/compeito`](https://github.com/infosign/compeito) (**Apache-2.0**, 3 ★), que además importa CFPackages de
OpenSALT/OpenCASE y CSV compatible OpenSALT.

**Capa 2 — verificación:** [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) (**MIT**, 2 ★), que
valida CASE 1.1 y otros diez estándares en el mismo *pipeline*.

**Capa 3 — puente al agente:** [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) (**MIT**, 14 ★) es la
**implementación de referencia** del puente: cinco herramientas MCP (`bncc_lookup`, `bncc_buscar`, `bncc_listar`,
`bncc_mapa_de_foco`, `bncc_estatisticas`) sobre 1.717 habilidades. Para los otros tres países **hay que escribirlo**, y
este repo es el molde.

**Capa 4 — el agente:** cualquiera de la tabla principal de `agents/top.md`. Para generación de material docente, la
referencia sigue siendo el patrón **P8**.

### El wiring

1. **Ingerir el esquema de la región** en su formato nativo (RDF para Inglaterra y Corea, JSON para Brasil y EE. UU.).
   Pinear el commit o la versión del *dump*: el currículo cambia por acto administrativo y hay que poder decir contra
   qué versión se generó cada material.
2. **Cargar el marco en OpenCASE** y publicarlo por su API CASE v1.1. Acá se gana lo que ningún JSON propio da: el
   currículo queda **direccionable por URI estable, versionado y consumible por cualquier herramienta certificada**.
3. **Pasar `conform-ed`** como *gate* de CI sobre el endpoint publicado. Entregable: reporte de conformidad firmado.
4. **Exponerlo al agente por MCP**, siguiendo el diseño de `bncc-mcp`: *lookup* por código, búsqueda por palabra clave
   con filtros, listado por componente y año, y —la herramienta que de verdad importa— **la capa de priorización**.
5. **Anclar cada artefacto que el agente genere** (lección, ítem de evaluación, *feedback*) **al URI CASE del punto
   curricular**. Eso es lo que convierte «el agente generó una lección» en «la lección cubre el estándar X.Y.Z, y acá
   está la traza».

### Por qué este patrón se vende, en una frase por región

- **EMEA:** las **11.207 *misconceptions*** inglesas son conocimiento de diagnóstico que no se deriva de un documento
  oficial con un *script* — se construye con docentes. Es el insumo que le faltaba a **P8** para dejar de depender de
  prompt y pasar a depender de datos, y está publicado con licencia comercial.
- **North America:** el mandato de política distrital (pase 12, patrón **P7**) exige material **alineado a estándar
  estatal y auditable**. El eje de los 50 estados ya existe en Apache-2.0: deja de ser alcance a cotizar.
- **LATAM:** el **Mapa de Foco del Instituto Reúna** (396 habilidades priorizadas con capa pedagógica) es un juicio
  curricular institucional que ningún modelo puede inventar sin alucinar, y ya está expuesto por MCP con licencia MIT.
- **APAC:** el coreano trae **2.293 relaciones de prerrequisito**, que es lo que un tutor adaptativo necesita para
  secuenciar (ver **P1** y **P26**).

### Plazo y alcance

- **3-4 semanas** donde el esquema ya existe y hay puente MCP (Brasil).
- **5-7 semanas** donde el esquema existe y hay que escribir el puente MCP (Inglaterra, EE. UU., Corea).
- **El gap 23 es el entregable vendible por sí solo:** publicar un currículo nacional como marco CASE conforme es
  trabajo de **días** una vez ingerido el dato, y **nadie lo hizo todavía en ningún país**. Es un activo reutilizable
  en todo el sistema educativo y auditable contra estándar.

### ⚠️ Los límites, y van en la primera página

- **Atribución obligatoria, y no es cosmética.** OGL-3.0 y CC BY 4.0 exigen acreditar a Oak National Academy y al MEC
  **en el producto**. Es una obligación de entregable: hay que diseñarla, no descubrirla en revisión legal.
- **La licencia del código no es la del dato.** Ver advertencia 2 de la nota de método del pase 14.
- 🔴 **Australia queda afuera hasta verificar licencia.** MRAC existe (RDF/XML, JSON, SPARQL, v9.0) pero
  `www.australiancurriculum.edu.au` está **bloqueado por el proxy de esta sesión** y los términos de reuso **no se
  leyeron**. No cotizar MRAC sin abrirlos.
- **España es *share-alike*.** `OpenDidactia` es **CC BY-SA 4.0**: contamina derivados. Para un entregable comercial en
  España, tratarlo como referencia, no como dependencia.
- **0 estrellas no es 0 valor, pero sí es 0 soporte.** `oak-curriculum-ontology` tiene 0 ★: se *forkea* y se pinea, y
  el cliente tiene que saber que el mantenimiento es del proyecto, no de una comunidad.
- **No se eligió OpenSALT, y es a propósito:** tiene 45 ★ —cinco veces más que OpenCASE— pero su último estable
  (3.2.0, septiembre de 2023) apunta a **CASE v1.0**. En capas de estándar el criterio es la fecha de certificación,
  no la estrella (tendencia 33).

---

## P32 — Evaluación de lectura oral que corre en el aula y no sale del dispositivo (agregado en el pase 14; **LATAM y APAC primero por volumen, EMEA y North America por régimen de privacidad**)

Es el primer patrón de esta KB con voz, y ataca la habilidad más evaluada de los primeros años de escolaridad del
mundo: **leer en voz alta, medida en palabras por minuto y exactitud.** Hasta el pase 14 esta KB no tenía ninguna
pieza para eso (ver gap 24).

### Las piezas, verificadas el 2026-10-01

| Rol | Pieza | Licencia | ★ |
|---|---|---|---|
| **Evaluación de pronunciación y fluidez** | [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | **MIT** ✅ | **85** |
| **ASR base / adaptación a voz infantil** | [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | **Apache-2.0** ✅ | **15.5k** |
| **Memoria de aprendizaje conforme a estándar** | LRS xAPI de la capa del pase 6 (ver **P15**) | — | — |
| **Eje curricular** | el artefacto de **P31** de la región | ver P31 | — |
| **Corpus de referencia** | [`jimbozhang/speechocean762`](https://github.com/jimbozhang/speechocean762) | 🔴 **sin `LICENSE`** | 198 |

### El wiring, con el límite adelante

1. **El texto a leer sale del eje curricular de P31**, no de una lista suelta: el nivel de dificultad queda anclado
   al punto curricular y al grado, y eso es lo que vuelve comparable la medición entre aulas y entre años.
2. **La captura y el puntaje corren en el dispositivo**, con `OpenPronounce` autoalojado. Devuelve puntaje 0-100,
   **PER y WER**, confianza por palabra (0-1), distancia acústica por **DTW** y **prosodia (F0 y energía)**. De ahí se
   derivan las dos métricas que el sistema escolar usa: **palabras por minuto y exactitud**.
3. **🔴 El audio del menor no sale del dispositivo. Nunca.** Lo que se envía al LRS es **la métrica**, no la voz: PPM,
   exactitud, puntaje por fonema y el URI curricular. Esto no es una preferencia de arquitectura — es la condición
   que vuelve el despliegue proponible (ver límites).
4. **Persistir en el LRS vía xAPI** (**P15**), de modo que la progresión de fluidez sea una serie temporal auditable y
   no una captura de pantalla de una app.
5. **El docente decide la intervención.** El sistema devuelve *qué fonemas y qué palabras fallan*, con transcripción
   IPA; **no clasifica al alumno, no le asigna nivel y no deriva a educación especial.** Ver límites.
6. **Opcional, y es donde hay trabajo nuevo:** envolver el paso 2 en un **servidor MCP de cinco herramientas**
   siguiendo el molde de `bncc-mcp`, para que un agente de `agents/top.md` pueda pedir la evaluación y razonar sobre
   el resultado. **Eso no existe hoy en ninguna parte — es el gap 24**, y es la pieza que convierte este patrón en un
   tutor de lectura en vez de un instrumento de medición.

### Plazo y alcance

- **4-6 semanas** para el instrumento de medición en inglés (pasos 1-5), que es donde el corpus y los modelos están.
- **+6-10 semanas** para español o portugués, **y la mayor parte es recalibración**, no desarrollo: hay que construir
  un conjunto de validación local con voz infantil. **Es alcance propio y presupuesto propio.**
- **+3-4 semanas** para el servidor MCP del paso 6.

### Dónde se vende primero

- **LATAM y APAC por volumen y por política:** la alfabetización inicial es prioridad declarada de los sistemas
  educativos de las dos regiones, y **la arquitectura en el dispositivo encaja con despliegues de conectividad
  intermitente** — que es el mismo argumento del patrón **P3** (offline-first) y de Kolibri.
- **EMEA y North America por régimen:** procesar voz de menores **sin que el audio salga del dispositivo** es
  exactamente lo que piden el Anexo III del EU AI Act y los estatutos estatales de EE. UU. que prohíben usar datos de
  alumnos para entrenar modelos (**California e Idaho**, pase 14). Un competidor que use un servicio de nube por uso
  tiene que justificar la transferencia; este patrón no tiene que justificar nada porque no transfiere.

### ⚠️ Los límites, y son más duros que en el resto de los patrones

- 🔴 **No hay corpus permisivo en español ni en portugués.** El de referencia (`speechocean762`, 198 ★) es **inglés con
  L1 mandarín y no tiene archivo de licencia** — el README afirma uso comercial permitido, pero eso es prosa, no un
  instrumento auditable. **Conseguir los términos por escrito antes de cotizar, y no prometer cifras de precisión en
  español o portugués basadas en resultados publicados sobre ese corpus.**
- 🔴 **Fluidez no es comprensión, y confundirlas es el error pedagógico clásico de esta capa.** PPM y exactitud miden
  decodificación. Un alumno puede leer rápido y preciso sin entender nada. **El instrumento mide una cosa y hay que
  decir cuál.**
- 🔴 **Esto no diagnostica dislexia ni ninguna condición, y no deriva a educación especial.** La capa del pase 8 dejó
  escrito que el open source de educación especial «apunta a la tarea que se está prohibiendo»: redactar o decidir
  sobre el alumno con discapacidad. **Este patrón produce una métrica para que un humano decida** (ver **P18**), y esa
  frontera va en la primera página de la propuesta, no en un anexo.
- **Sesgo de acento y de variedad dialectal.** Un modelo entrenado con una variedad del español penaliza a hablantes
  de otra, y en LATAM eso se superpone con nivel socioeconómico y con población indígena. **Es riesgo de equidad
  medible y hay que medirlo**, no declararlo resuelto.
- **La pieza más fina de la región no se puede usar:** `carrera-lectora` (Chile, 1.º-4.º básico, 40 textos graduados,
  pedagogía intercultural, en el dispositivo) **no tiene licencia**. No proponerla. Pedir que la pongan es, por costo
  sobre beneficio, una de las mejores acciones disponibles en esta KB.

---

## P33 — Integridad por procedencia en vez de por detección: marcar lo que el tutor genera (agregado en el pase 15; **EMEA primero por obligación legal, LATAM segundo por norma de declaración**)

Es el patrón que cierra el **gap 25** y que le pone código a la oferta que esta KB recomienda desde el pase 4 sin
tenerlo. Y es el único patrón de esta KB cuyo entregable **tiene fecha legal**: **2026-12-02**.

**La idea entera en una línea:** dejar de preguntar *«¿esto lo escribió una AI?»* —que no tiene respuesta
confiable— y empezar a preguntar *«¿esto lo escribió **nuestro** tutor?»*, que se responde con una verificación
criptográfica.

### Por qué no se hace con detectores, y conviene tenerlo escrito antes de la reunión

La capa forense existe, es permisiva y está publicada en ICLR, ICML y ACL. **Y no se puede usar para producir
una consecuencia sobre un alumno:**

| Medición | Valor |
|---|---|
| FPR sobre escritura de **no nativos de inglés** (TOEFL, 7 detectores) | **61,3 %** |
| FPR sobre universitarios nativos | ~2,9 % |
| FPR sobre 1.180 abstracts académicos **pre-2018** | **5,85 %** + 20 % «incierto» |
| Longitud mínima para que el score sirva | **~80 palabras** |
| Efecto de la paráfrasis | **caídas grandes** (RAID) |

**La cuenta de Vanderbilt:** 1 % de FPR sobre 75.000 trabajos = **~750 acusaciones injustas por año**. Desactivaron
el detector; **más de 50 universidades** hicieron lo mismo. Y existe `humanizar-es` (MIT), que **usa Binoculars y
Fast-DetectGPT como función objetivo** para reescribir español hasta que dejen de marcarlo, distribuido como
*skill* para seis harnesses de agente. **Esa carrera no se gana.** La de procedencia sí, porque marcar en el
origen no es un clasificador que se pueda optimizar en contra.

### Las piezas, verificadas repo por repo vía WebFetch el 2026-10-01

| Rol | Pieza | Licencia | Señal |
|---|---|---|---|
| **Marcar el texto en generación** | **SynthID-Text** — `huggingface/transformers` → `src/transformers/generation/watermarking.py` | **Apache-2.0** ✅ | `SynthIDTextWatermarkLogitsProcessor`, `SynthIDTextWatermarkDetector`, `BayesianDetectorModel`. Copyright HuggingFace + Google DeepMind |
| **Probar que el marcado aguanta** | [`THU-BPM/MarkLLM`](https://github.com/THU-BPM/MarkLLM) | **Apache-2.0** ✅ | **1.100 ★**, 23+ algoritmos, **12 herramientas** de detectabilidad/robustez/calidad. EMNLP 2024 Demo |
| **Manifiesto de procedencia firmado** | [`contentauth/c2pa-rs`](https://github.com/contentauth/c2pa-rs) · [`c2pa-python`](https://github.com/contentauth/c2pa-python) | **MIT *y* Apache-2.0** (dual) ✅ | **1.907** / 344 commits. Spec **C2PA 2.4**, *CAWG identity assertion* |
| **Entrada al LMS sin forkearlo** | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) (ver **P21**) | **Apache-2.0** ✅ | Ya en esta KB desde el pase 9 |
| **Registro de la evidencia** | LRS xAPI del pase 6 — `lrsql` / `Ralph` (ver **P15**) | Apache-2.0 / MIT ✅ | Ya en esta KB |
| **Triage, nunca sanción** | [`fast-detect-gpt`](https://github.com/baoguangsheng/fast-detect-gpt) (MIT) o [`sloptotal`](https://github.com/pablocaeg/sloptotal) (MIT, 23 motores, CPU) | MIT ✅ | **Opcional, y con el límite puesto por diseño** |

### El wiring

1. **El tutor marca su propia salida.** Donde el agente llama a `generate()` sobre Transformers, se agrega un
   `WatermarkingConfig` de SynthID-Text. **No es un servicio nuevo ni un proveedor nuevo: es un parámetro.** La
   clave de marcado es del cliente y vive donde viven sus secretos.
2. **Cada salida sale con manifiesto C2PA firmado** (`c2pa-python`): qué modelo, qué versión, qué timestamp, bajo
   qué identidad institucional (*CAWG identity assertion*). Esto es el tramo con ingeniería real —custodia de
   claves y política de firma— y es el entregable que el cliente no puede hacer solo.
3. **El LMS entrega por LTI 1.3** (P21). El alumno entrega su trabajo; el servicio de verificación corre
   `SynthIDTextWatermarkDetector` contra la clave de la institución y valida el manifiesto C2PA si lo hay.
4. **El resultado es una de tres cosas, y ninguna es una acusación:**
   - **Marca válida de nuestro tutor** → uso declarado y verificado. Se registra en el LRS como evento xAPI.
     En LATAM, **esto es el cumplimiento de la norma de declaración**, automatizado.
   - **Sin marca** → no dice nada sobre autoría. Es el estado por defecto de todo texto humano y de todo texto
     generado fuera de la institución.
   - **Marca válida de otra institución o proveedor** → procedencia externa verificada.
5. **MarkLLM produce la evidencia de robustez** —detectabilidad, resistencia a edición y paráfrasis, impacto en
   calidad— que el **Artículo 50(2)** exige al pedir un marcado *«effective, interoperable, robust and reliable»*.
   **Ese informe es un entregable facturable**, no un anexo técnico.
6. **El detector forense, si entra, entra con el límite en el código:** produce **cola de revisión docente**, nunca
   una marca en el expediente, nunca una notificación automática al alumno, y **nunca como insumo único**. El
   umbral se fija con la institución y se documenta. Si el cliente pide sanción automática, **esa es la línea**:
   el **61,3 %** lo convierte en discriminación medible contra el alumnado que escribe inglés como L2.

### Lo que hay que construir, y es chico

**El puente no existe en ninguna forma open source.** No hay plugin de Moodle, XBlock de Open edX, herramienta LTI
ni servidor MCP que marque o verifique. Lo que hay en el directorio de Moodle son **envoltorios de servicios
propietarios** —Compilatio (plugin GPL-3.0, 821 instalaciones), Originality.ai, Copyleaks— que además **detectan**
en vez de marcar. El trabajo es: el servicio de verificación, la política de firma, la herramienta LTI y el
mapeo a xAPI. **Semanas, sobre infraestructura Apache-2.0 madura.**

### Plazos y por qué el orden regional es ése

| Región | Gancho | Urgencia |
|---|---|---|
| **EMEA** | **Obligación legal**: Art. 50 en vigor 2026-08-02; marcado legible por máquina para sistemas ya en mercado **2026-12-02**. Code of Practice adopta **C2PA** como estándar de facto | 🔴 **62 días** |
| **LATAM** | **Norma de declaración** ya vigente en México, Colombia y Chile (a veces con entrega de prompts). El paso 4 **la cumple automáticamente**. Y lo instalado (Turnitin Originality en UNAM, Tec, UAM, BUAP, UdeG) no la cumple | 🟡 Alta: >80 % de las IES mexicanas sin reglamento propio — ventana de definición |
| **North America** | Sin obligación. El gancho es **exposición**: 50+ universidades apagaron la detección y **no compraron reemplazo** | 🟡 Hueco abierto |
| **APAC** | **Australia**: 26 de 35 universidades (73 %) ya tienen la política de AI dentro de integridad académica — *owner* y presupuesto resueltos | 🟢 Entrada por organigrama |

**Estimación:** 6-8 semanas para el tramo EMEA con el informe de robustez de MarkLLM incluido; 4-5 si el cliente
ya tiene el tutor sobre Transformers y sólo falta C2PA + verificación + LTI.

### Lo que este patrón NO resuelve, y hay que decirlo en la primera reunión

- **Sólo cubre el texto que generó el sistema propio.** El ensayo escrito con un modelo externo no lleva marca y
  nunca la va a llevar. El patrón convierte un problema irresoluble en uno **parcial pero cierto**, más un
  **régimen de declaración** para el resto. Vender esto como «detectamos todo» es mentir y se cae en la primera
  prueba.
- **No reemplaza el rediseño de la evaluación.** Las instituciones que apagaron la detección adoptaron escritura
  en clase, defensa oral y consignas que integran AI. El patrón **convive** con eso; no lo sustituye.
- ⚠️ **No pedir evidencia de proceso sin una vía alternativa.** *«Mostrá el historial de versiones»* **no lo puede
  producir un alumno que escribe hablando**. Choca de frente con la capa de accesibilidad del pase 8 y con la de
  habla del pase 14. Si el entregable incluye evidencia de proceso, **el camino alternativo es parte del alcance**,
  no una excepción a gestionar después.
- **La detección de proceso por pulsaciones no es una opción.** Todo lo que existe es propietario (GPTZero
  Authorship, Grammarly Authorship, Turnitin Clarity, Draftback) y hay literatura de 2026 que sostiene que la
  señal **no distingue a quien compone de quien transcribe un borrador** — 🔴 **no verificable desde esta sesión,
  `arxiv.org` bloqueado por el proxy**. Anotado como pista.
- 🔴 **Verificar la fecha del Code of Practice contra la fuente oficial** antes de citarla: dos fuentes secundarias
  dan 10 de junio y 20 de julio de 2026. Las fechas de vigencia (2026-08-02) y de marcado (2026-12-02) sí son
  consistentes.


---

## P34 — Entrenar el modelo de mastery sin que el dato del alumno salga de la institución (agregado en el pase 16; **transversal, y es la salida técnica al gap 11**)

**El problema que resuelve, y lo venía arrastrando esta KB desde el pase 7.** El gap 11 estableció que los
datasets de knowledge tracing son NonCommercial salvo uno (chino), y concluyó que para un cliente con restricción
de procedencia **entrenar con los datos propios es la única opción**. El pase 16 le agrega la condición que
faltaba: bajo la *school official exception* de **FERPA**, el dato que la institución cede al proveedor sólo
puede usarse **para el fin por el que se cedió**, y usarlo para entrenar un modelo comercial general es
típicamente una violación. O sea: «entrenar con los datos propios» no es una licencia para llevarse el dato.

**La salida no es legal, es arquitectónica, y tiene tres variantes según lo que el cliente permita.**

### Las piezas, todas verificadas en el pase 16

| Pieza | Licencia | ★ | Rol |
|---|---|---|---|
| **Flower** | Apache-2.0 ✅ | 7.2k | Orquesta el entrenamiento federado. El modelo viaja, el dato no |
| **PySyft** | Apache-2.0 ✅ | 10.0k | Variante más estricta: el **cómputo** viaja y el dueño del dato lo ejecuta |
| **Opacus** | Apache-2.0 ✅ | 2.0k | DP sobre el entrenamiento PyTorch; contador de presupuesto en vivo |
| **OpenDP** | MIT ✅ | 437 | La garantía **formal** que va en el expediente. Harvard |
| **pyKT** / **pyBKT** | MIT ✅ | 441 / 281 | El modelo de mastery en sí (ya en esta KB desde los pases 4 y 5) |
| **FedGKT** | ⚠️ sin licencia | 1 | **Referencia de arquitectura, no dependencia.** Ya hace exactamente esto sobre Flower |

### El wiring

1. **Capa 0 — el dato se queda donde está.** Cada escuela/campus corre un cliente Flower contra su propio LRS
   (`lrsql` o Ralph, Apache-2.0/MIT, de **P15**). Ninguna interacción cruza el borde institucional.
2. **Capa 1 — el modelo federa.** `pyKT` (o `pyBKT` si hace falta interpretabilidad ante regulador) se entrena por
   rondas FedAvg/FedProx sobre Flower. Lo que viaja son **pesos**, no secuencias de alumno.
3. **Capa 2 — presupuesto de privacidad.** `Opacus` sobre el entrenamiento local, con ε declarado y registrado por
   ronda. Acá es donde el DPIA del Artículo 35 encuentra su evidencia.
4. **Capa 3 — el expediente.** `OpenDP` para las estadísticas agregadas que se publican hacia afuera (dashboards de
   dirección, reportes a ministerio). Es la pieza que un comité de ética reconoce sin discusión.
5. **Capa 4 — el entregable de demostración.** `synthcity` genera el dataset sintético con el que se demuestra el
   sistema, se licita y se hace QA, **sin tocar dato real en ningún momento del ciclo de venta**.

**La arquitectura no es especulativa:** `FedGKT` ya la implementa —grafos de conocimiento personales de 722
conceptos, 1.401 aristas de prerrequisito anotadas por expertos, FedAvg/FedProx sobre Flower, dataset Junyi de 25M
interacciones—. Tiene **1 estrella y no declara licencia**, así que se lee y se reimplementa; no se depende de él.

### Plazo y alcance

**8–10 semanas** para el piloto con dos instituciones federadas, incluyendo el DPIA. El multiplicador está en que
la institución número tres en adelante entra sin renegociar el tratamiento de datos: la arquitectura ya responde
la pregunta.

### Dónde se vende primero

**EMEA** (el DPIA del Artículo 35 es obligación, no argumento) y **North America K-12** (donde FERPA + COPPA
cierran la vía centralizada). En **APAC-India** el argumento es la Sección 9 de la DPDP y las sanciones de hasta
₹200 crore. En **LATAM-Brasil**, el Art. 14 de la LGPD más los informes semestrales a la ANPD.

### ⚠️ Lo que no hay que prometer en este patrón

- **Federado no es anonimato.** Sin DP encima, los pesos filtran. Si se promete privacidad, `Opacus` no es opcional.
- **DP cuesta exactitud.** Hay que medirla con `diffprivlib` antes de comprometer métricas de mastery, no después.
- **No usar `SDV`** para el dataset sintético de demostración, por mucho que sea el nombre conocido: su BUSL 1.1
  excluye explícitamente el uso comercial que este patrón hace. `synthcity`.

---

## P35 — El expediente de privacidad como entregable de entrada (agregado en el pase 16; **EMEA y North America primero**, y es la venta más chica de toda esta KB)

**Por qué existe este patrón.** Los 34 patrones anteriores venden **capacidad**. Éste vende el permiso para
ejercerla, y es el único de la KB cuyo alcance cabe en semanas y cuyo comprador (DPO, CISO, dirección jurídica) no
es el mismo que el de los demás. Sirve como puerta de entrada cuando el cliente todavía no compró el sistema.

### El entregable, que son cuatro artefactos y nada más

1. **DPIA del Artículo 35** (EMEA) o evaluación equivalente. Es **obligación legal** antes de usar una herramienta
   de AI que procese dato de alumnos, y el EDPB pide además el *balancing test* de interés legítimo documentado por
   actividad de tratamiento. La mayoría de las instituciones no lo tiene hecho para sus herramientas de AI ya
   desplegadas.
2. **Inventario de dato biométrico**, que es el que nadie hizo. Desde el **2026-04-22** la regla COPPA enmendada
   cuenta **voiceprints**, faceprints, huellas y huellas de palma como información personal. Cualquier función de
   voz —y la capa de lectura oral del pase 14 es exactamente eso— entra. Si el despliegue toca **Illinois**, BIPA
   exige consentimiento escrito con daños de **1.000 a 5.000 USD por violación**.
3. **Política de retención y borrado por escrito.** La COPPA enmendada **prohíbe la retención indefinida** y exige
   política escrita con borrado en plazo. Es el punto donde más despliegues educativos fallan, porque los logs de
   LMS y LRS se guardan «por las dudas».
4. **Matriz de base legal por flujo de dato**, incluida la frontera FERPA: qué dato se usa para prestar el servicio
   y qué dato **no puede** ir a entrenamiento de modelo general.

### Las piezas técnicas que lo vuelven demostrable

El expediente no es sólo papel. Lo que lo hace defendible es poder mostrar la implementación:

- **`OpenDP`** (MIT, Harvard) para las estadísticas agregadas publicadas — garantía formal, no promesa.
- **`Opacus`** (Apache-2.0) con ε registrado si hay entrenamiento.
- **`synthcity`** (Apache-2.0) para que los ambientes de desarrollo, demo y QA **no contengan dato real**, que es
  la mitigación más barata y la que más impresiona en una auditoría.
- **`Flower`** (Apache-2.0) si hay más de una institución.

### Plazo y alcance

**3–5 semanas.** Es el entregable más chico de esta KB y el único que se puede vender sin que el cliente haya
decidido todavía qué sistema de AI quiere.

### Dónde se vende primero

**EMEA**, porque el DPIA es obligatorio y la institución ya sabe que lo debe. **North America**, porque el reloj
COPPA **ya venció el 2026-04-22** y la conversación no es de preparación sino de exposición: a diferencia del
Artículo 50 europeo, acá no queda plazo que administrar. **LATAM-Brasil** tiene su propia versión con fecha:
plataformas con más de **1 millón de usuarios menores de 18** deben publicar **informes semestrales de impacto** y
presentarlos a la **ANPD**.

### ⚠️ Lo que no hay que prometer en este patrón

- **No es asesoría legal.** El entregable es el expediente técnico y la evidencia de implementación; la firma
  jurídica la pone el cliente o su estudio.
- **No prometer «cumplimiento COPPA» como estado binario.** Se entrega el inventario, la mitigación y la
  trazabilidad; quien declara conformidad es el operador.
- **No proponer este patrón solo en mercados sin obligación.** Donde no hay regla exigible, el argumento es
  exposición legal y no cumplimiento, y se vende distinto.

---

## P36 — El `privacy provider` del LMS como capa 0 del agente (agregado en el pase 17; **transversal, y es condición de posibilidad de P1, P15, P16 y P34**)

**El problema que resuelve, en una línea:** el dato del alumno ya está en el LMS y el LMS ya tiene la máquina para
gobernarlo, pero **ningún agente la usa** (gap 29). Y en Moodle no es opcional: el núcleo **obliga a todo plugin**
que guarde dato del alumno a saber declararlo, exportarlo y borrarlo.

**Por qué es «capa 0» y no un patrón más:** P1, P15, P16 y P34 tocan dato real del alumno. **Ninguno es
desplegable en una institución que tome en serio un pedido de borrado si el plugin que los sostiene no implementa
el contrato de privacidad del LMS.** Esto va antes, no después.

### Las piezas, verificadas en el pase 17

| Pieza | Licencia | Rol |
|---|---|---|
| https://github.com/moodle/moodle | GPL-3.0 ⚠️ | Privacy API en el núcleo (obliga a los plugins) + `tool_dataprivacy` (pedidos, delegado de protección de datos, retención) + `tool_policy` |
| https://github.com/openedx/edx-platform | AGPL-3.0 ⚠️ | `scripts/user_retirement` (6 scripts) + `lms/djangoapps/bulk_user_retirement` (API REST de retiro masivo) |
| https://github.com/openeducat/openeducat_erp | LGPL-3.0 ⚠️ | Variante autohospedada donde **la institución es el responsable del dato**: el argumento FERPA más corto de esta KB |
| `learnmcp-xapi` + el LRS de la capa del pase 6 | ver `repos/foundations.md` | Donde queda la evidencia de aprendizaje, que es **también** dato personal y entra en el mismo expediente |

### El wiring

1. **Inventario de contextos.** Enumerar dónde vive dato del alumno: LMS, LRS (xAPI), memoria del agente, logs de
   inferencia. **La memoria del agente es la que siempre se olvida**, y el gap 27 ya midió que ninguno de los 31
   agentes declara qué hace con ella.
2. **Implementar el `privacy provider` en el plugin propio** (Moodle): declarar metadatos de qué se guarda,
   exportar por contexto y borrar por usuario y por contexto. Para un plugin que **no** persiste nada, el
   `null_provider` es la declaración correcta — y declararlo es trabajo, no es nada.
3. **Conectar el retiro** (Open edX): orquestar los seis scripts y el endpoint REST desde la automatización del
   cliente; definir qué pasa con el dato en sistemas externos.
4. **Política de retención escrita**, con período configurado en `tool_dataprivacy` y borrado al cumplirse el
   propósito. Es lo que COPPA enmendada exige desde el **2026-04-22** y lo que AB 1159 refuerza.
5. **Expediente de evidencia:** por cada pedido, qué se exportó, qué se borró, de qué contextos y cuándo.

### Plazo y alcance

**4 a 6 semanas** para una institución con un LMS y un agente. **Casi no es software**: el `privacy provider` es
la única pieza de código y es chica. El resto es inventario, configuración, política y evidencia — más barato de
construir y más difícil de copiar que un plugin.

### Dónde se vende primero

**North America**, por dos razones concretas y no por madurez de mercado: el incidente de **Instructure/Canvas**
(tendencia 44) dejó a las instituciones sin poder responder qué dato de sus alumnos se expuso, y **sólo el 11 %**
de los distritos tiene evaluación rigurosa de privacidad. Después **LATAM**, donde el **vacío regulatorio juega a
favor** por única vez: este patrón entrega capacidad verificable sin ningún régimen que certificar (ver
`intel/market.md`, `### LATAM`). Y **APAC vía Australia**, el único régimen de la región con **consecuencia
aplicada** (Privacy Act + Notifiable Data Breaches, con resultados publicados por la OAIC).

### ⚠️ Lo que no hay que prometer en este patrón

- **No prometer cumplimiento.** Open edX lo niega por escrito: *«User retirement is not a compliance guarantee.
  The Open edX software makes no claim of satisfying any law or regulation.»* El cumplimiento es del **operador
  del sitio**. (Cita de snippet; `docs.openedx.org` bloqueado en esta sesión — resolver contra la fuente oficial
  antes de citarla.)
- **No forkear el LMS.** Moodle se extiende, Open edX se invoca. Un fork de AGPL-3.0 es el peor resultado posible.
- **No asumir paridad en Canvas.** No se verificó un toolset de retiro equivalente. Es alcance a dimensionar.
- **No prometer borrado de lo que ya salió hacia un modelo.** El Privacy API borra el registro, **no el modelo**.
  Eso es P37.

---

## P37 — Expediente de procedencia del dato de entrenamiento (agregado en el pase 17; **North America primero, y es obligatorio en California desde el 2027-07-01**)

**El problema:** **California AB 1159** (firmada **2026-09-13**) prohíbe usar información cubierta del alumno
—incluidos **identificadores únicos persistentes**— para **entrenar AI generativa o desarrollar modelos**, salvo
uso **estrictamente de propósito educativo y en beneficio de la institución correspondiente**. La **HESIPA**
extiende el régimen a **educación superior** desde el **2027-07-01**.

**Por qué esto es un patrón y no una nota legal:** la excepción es defendible **sólo si se puede probar**, y
**ninguna pieza open source produce esa prueba** (gap 30). Entrenar un modelo central con dato de muchas
instituciones para servir a todas —la arquitectura por defecto de la industria— **no cae obviamente dentro**.

### Las piezas

| Pieza | Licencia | Rol |
|---|---|---|
| `Flower` (capa del pase 16) | Apache-2.0 ✅ | Entrenamiento federado: el dato **no sale** de la institución. Es la mitad arquitectónica de la excepción |
| `Opacus` / `diffprivlib` / Google DP (capa del pase 16) | Apache-2.0 / MIT ✅ | Presupuesto de privacidad medible sobre el entrenamiento |
| `pyKT` / `pyBKT` | MIT ✅ | El modelo de *mastery* que se entrena, y el que AB 1159 toca |
| Privacy API de Moodle / retiro de Open edX (**P36**) | GPL-3.0 / AGPL-3.0 ⚠️ | De dónde sale el inventario de qué dato de qué alumno entró |
| `synthcity` | Apache-2.0 ✅ | Para demo, licitación y desarrollo **sin tocar dato real**: saca de alcance la pregunta entera |

### El wiring

1. **Clasificar el propósito, por institución.** La excepción es *propósito educativo estricto* **y** *beneficio
   de esa institución*. Si el modelo sirve a varias, hay que poder sostener el beneficio de cada una.
2. **Federado por defecto** donde haya dato de alumno de California: el dato no sale, el modelo viaja.
3. **Manifiesto por corrida de entrenamiento:** qué institución, qué contextos, qué rango temporal, qué
   identificadores (y la constancia de que **no** entraron identificadores únicos persistentes fuera de la
   excepción), qué presupuesto de privacidad.
4. **Atar el manifiesto al inventario de P36**, que es la única fuente que sabe qué dato existía.
5. **Ruta de borrado del modelo**, no sólo del registro: qué pasa cuando un alumno pide borrado y su dato entró a
   un entrenamiento.

### Plazo y alcance

**6 a 8 semanas** sobre una arquitectura federada que ya exista; **12 a 14** si hay que migrar de entrenamiento
central a federado.

⚠️ **Lo que este patrón NO puede prometer todavía, y hay que decirlo antes de cotizar:** el paso 5 —deshacer el
entrenamiento— **no tiene solución verificada en esta KB**. El pase 17 **no buscó `machine unlearning`** y lo deja
anotado como la acción del próximo pase (ver la nota de método). Hasta entonces, la respuesta honesta a «¿y si un
alumno pide borrado después de que su dato entrenó el modelo?» es **reentrenar sin ese dato**, con el costo que
eso tenga, y el manifiesto del paso 3 es lo que vuelve ese reentrenamiento acotado en vez de total. **Tampoco se
midió el costo de producir la evidencia** sobre una arquitectura federada real.

### Dónde se vende primero

**California**, por fecha: **2027-07-01** para educación superior, ~2,9 millones de estudiantes. Después el resto
de **North America** como anticipación (**134 proyectos en 31 estados** en 2026). Y **EMEA** como argumento
complementario: no hay prohibición de insumo equivalente, pero el **GDPR ya se aplica directamente** al
procesamiento de dato de alumnos y la base legal del entrenamiento es la misma pregunta con otro nombre.

## P38 — El derecho al olvido que alcanza al modelo, no sólo al registro (agregado en el pase 18; **EMEA primero por GDPR art. 17, North America segundo por AB 1159**)

**El problema, y es una promesa que el sector ya está haciendo sin poder cumplirla.** Una institución con un tutor
adaptativo en producción recibe un pedido de supresión. Ejecuta el flujo del LMS —`tool_dataprivacy` en Moodle, los
scripts de retiro en Open edX— y borra las filas del alumno. **El estimador de *mastery* sigue conteniendo lo que
aprendió de ese alumno.** El pase 17 lo escribió en una línea: *«borra el registro, no el modelo»*. Este patrón es
la parte que faltaba.

**Por qué ahora.** En **EMEA** el derecho de supresión del **GDPR art. 17** es directamente exigible y no distingue
entre la fila y el modelo. En **North America**, **California AB 1159** (firmada 2026-09-13) prohíbe usar
información cubierta del alumno para entrenar AI generativa o desarrollar modelos salvo la excepción de propósito
educativo, con **HESIPA** extendiéndolo a educación superior desde el **2027-07-01**: un modelo ya entrenado con
dato que no debía entrar necesita una vía de remediación, y la remediación es esta.

**El wiring, y bifurca según el modelo de dominio — esto es lo que decide el presupuesto:**

```
                 ┌─ pedido de supresión aprobado ─┐
   Moodle núcleo │  admin/tool/dataprivacy        │  (GPL-3.0, YA INSTALADO)
   (4.5+ / 5.0)  │  classes/privacy/provider.php  │  patrón: ai/provider/openai
                 └────────────┬───────────────────┘
                              │  ⚠️ este disparador NO EXISTE (gap 32) — es el trabajo de integración
                              ▼
                 ┌────────────────────────────────┐
                 │  orquestador de borrado        │  ← lo que se construye
                 └───────┬────────────────┬───────┘
                         │                │
        modelo = BKT ────┘                └──── modelo = deep KT
        pyBKT (MIT)                             pyKT (MIT)
             │                                       │
             ▼                                       ▼
   REAJUSTE sin el alumno                   torchunlearn (MIT) · SalUn (MIT)
   (EM, pocos parámetros, barato)           unlearning aproximado sobre pesos
             │                                       │
             ▼                                       ▼
   ✅ EXACT UNLEARNING                     ⚠️ APROXIMADO → el entregable
   la garantía más fuerte                  incluye la MÉTRICA DE VERIFICACIÓN
```

**Las piezas, todas con licencia verificada:**

| Rol | Pieza | Licencia |
|---|---|---|
| Pedido de borrado y declaración | Moodle núcleo: `admin/tool/dataprivacy`, `admin/tool/policy`, patrón `ai/provider/openai/classes/privacy/provider.php` | GPL-3.0 (ya instalado) |
| Referencia de `privacy provider` más completa de la comunidad | https://github.com/jeanlucio/moodle-local_aihub (4 interfaces) | GPL-3.0 |
| Estimador BKT → reajuste exacto | `pyBKT` | MIT |
| Estimador deep KT → unlearning aproximado | `pyKT` + https://github.com/Harry24k/machine-unlearning-pytorch | MIT + MIT |
| Método de unlearning con mejor costo/resultado | https://github.com/OPTML-Group/Unlearn-Saliency (SalUn, ICLR 2024 Spotlight) | MIT |
| Si el componente es un LLM afinado | https://github.com/locuslab/open-unlearning (12 métodos, TOFU/MUSE/WMDP) | MIT |
| Métricas de verificación del olvido | `open-unlearning` (10+ métricas) + https://github.com/tamlhp/awesome-machine-unlearning | MIT |

**La decisión de arquitectura que este patrón fuerza, y es contraintuitiva:** **elegir BKT en vez de deep knowledge
tracing puede ser la decisión de cumplimiento correcta aun si predice algo peor.** Con BKT el borrado es exacto,
barato y demostrable ante un regulador; con deep KT es aproximado y hay que presupuestar la verificación. Esta KB
venía recomendando `pyBKT` por madurez y licencia (pase 5, **P12**); este pase le agrega el argumento legal.

⚠️ **Lo que este patrón NO promete.** El disparador LMS → modelo **no existe en abierto** (gap 32): es trabajo de
integración de tamaño acotado, no una pieza que se instala. Y para deep KT, *«unlearning aproximado»* significa que
**queda residuo medible**: el entregable es el borrado **más** la métrica, y si el cliente necesita garantía
absoluta sobre un modelo deep, la única respuesta honesta sigue siendo reentrenar. No vender «olvido garantizado»
sobre deep KT.

⚠️ **Y el algoritmo específico de esta industria no está disponible.** **PrivacyCD / HIF** (arXiv 2511.03966) hace
exactamente esto para modelos de *cognitive diagnosis* y argumenta que los métodos genéricos son subóptimos frente
a su estructura heterogénea. **No publica código** (gap 31). Si aparece, este patrón cambia de forma y mejora.

---

## P39 — Plugin de AI para el LMS del cliente con el expediente de privacidad incluido de fábrica (agregado en el pase 18; **transversal, y es la venta más chica que cierra el gap 29**)

**El problema.** El cliente ya tiene Moodle y quiere una capacidad agéntica propia —no la del núcleo— sobre el
dato que ya tiene. El pase 17 estableció que el `privacy provider` no es opcional: el núcleo **lo exige a todo
plugin**. Hasta este pase, esta KB tenía que decir que no había referencia publicada. **Ahora hay cuatro, y tres
están en el núcleo.**

**La receta, y el orden importa porque la capa 0 es la declaración, no la funcionalidad:**

1. **Elegir el proveedor contra lo que el núcleo ya trae.** `openai`, `azureai` y `ollama` **están en el núcleo
   con su `privacy provider`** → no se cotizan. `bedrock` y `anthropic` **no están** (verificado, 404) → el
   proveedor y su `privacy provider` son alcance propio.
2. **Copiar el patrón canónico del núcleo:** `ai/provider/openai/classes/privacy/provider.php`. Tres interfaces
   —`metadata\provider`, `request\core_userlist_provider`, `request\plugin\provider`— y, **si el plugin no guarda
   nada local**, los seis métodos de export/borrado vacíos y sólo `add_external_location_link` poblado. Es
   exactamente lo que hizo Ferrara para Gemini, y funciona.
3. **Si el plugin SÍ guarda, no copiar esa forma.** Hay que implementar los seis de verdad. La referencia completa
   es `jeanlucio/moodle-local_aihub` (GPL-3.0, Brasil), que es la única de la capa con **cuatro** interfaces
   —agrega `user_preference_provider`— y declara tabla de base, 6 preferencias de usuario y 4 enlaces externos.
4. **Poner el gate humano en el camino de escritura**, no después. `mod_aigradedassign` lo tiene resuelto: el
   resultado de la AI **no afecta nota ni compleción hasta que un tutor aprueba o edita** la nota y el texto. Es
   el diseño de **P18** y es lo que exigen Oklahoma S.B. 1734 y Maryland S.B. 720.
5. **Si la promesa es que el dato no sale, usar la arquitectura de red, no una declaración.**
   `sngdtechnologies/ai-moodle-security` (**BSD-2-Clause** — la única licencia permisiva de la capa) es la
   referencia: Ollama on-site, Moodle y el modelo en redes internas **sin egreso**, sólo el proxy expuesto.
6. **Escribir la línea de «explicitly» en el expediente.** Incluso `aiprovider_ollama` declara envío externo, y la
   cadena del núcleo dice *«No user data is explicitly sent»*: no manda identidad, pero `prompttext` viaja.
   **Acotar el contenido del prompt es responsabilidad del entregable**, y decirlo por escrito evita la discusión.

**Por qué es la venta más chica de esta KB y conviene ofrecerla primero.** No requiere modelo propio, ni dato de
entrenamiento, ni infraestructura nueva: es un plugin con su declaración de privacidad bien hecha sobre un LMS que
el cliente ya opera. Es la **capa 0** de **P1**, **P15**, **P16** y **P34** (ver **P36**), y es el único entregable
de esta KB que se puede completar y auditar sin tocar el modelo del alumno.

⚠️ **Advertencia de licencia que decide la cotización.** De las piezas de la comunidad en esta capa, **las dos
usables son GPL-3.0** (`local_aihub`, `aiprovider_gemini`) — lo cual es lo esperable y lo correcto para un plugin
de Moodle, porque el núcleo es GPL-3.0+ y lo exige. `mod_aigradedassign` **no tiene archivo `LICENSE`** (sólo el
header GPL en el fuente) y `tool_aiconnect` **no muestra licencia**: a efectos de cotización se tratan como **sin
licencia**, y lo que corresponde es abrir un *issue* pidiendo el archivo. **Un plugin derivado de Moodle va a ser
GPL-3.0 de todos modos** — eso no es un obstáculo para el engagement, pero sí hay que decirlo antes de firmar.

## P40 — Propagar la supresión del LMS a la telemetría y al modelo, sin evento porque no hay evento (agregado en el pase 19; **EMEA y North America primero por régimen, LATAM con instrumento local**)

**Problema.** Un cliente aprueba un pedido de supresión en Moodle. El LMS borra sus filas. **El LRS sigue teniendo la
historia de aprendizaje del alumno y el modelo de mastery sigue teniendo su influencia en los pesos.** El pase 19
midió los tres eslabones y el del medio no borra ni en la especificación. Este patrón es el eslabón que falta,
construido con lo que hay.

**Lo que hay que saber antes de diseñarlo, y es lo que el pase 19 refutó.** No se puede hacer con un observer:

- `tool_dataprivacy` **no emite ningún evento** — 187 archivos, **cero** `trigger()`.
- `api::update_request_status()` (por donde pasa `approve_data_request()`) es **una escritura de base de datos**: setea
  `status`, `dpo`, `dpocomment` y hace `update()`. Sin evento, sin hook, sin notificación.
- El único observer registrado va **hacia adentro**: `\core\event\user_deleted` → **crear** un pedido.

> 🔴 **ACTUALIZACIÓN DEL PASE 22 — el disparador que este patrón declara inexistente SÍ existe, pero en la otra
> plataforma, y es Apache-2.0.** Todo lo de arriba sigue siendo cierto **para Moodle**. Para **Open edX** no: el plugin
> oficial `openedx/platform-plugin-aspects` (**Apache-2.0**, 528 commits) trae el **`UserRetirementSink`**, que
> **escucha la señal Django `USER_RETIRE_LMS_MISC` y elimina la PII del usuario de ClickHouse** (verificado de primera
> mano en su README). O sea: **en Open edX el disparador es una señal del framework con un listener permisivo ya
> escrito.**
>
> **Lo que esto cambia en la cotización de este patrón:**
> - **Cliente Open edX** → el extremo del disparador **deja de ser desarrollo** y pasa a ser **configuración más
>   verificación**. Lo que hay que auditar es *qué* borra (ver abajo), no *si* dispara.
> - **Cliente Moodle** → sigue siendo el sondeo del mecanismo (a), **pero ya no hay que diseñarlo de cero**: el
>   `UserRetirementSink` es la **implementación de referencia**, permisiva y en producción, del lado que recibe.
> - ⚠️ **Y no hay que sobrevenderlo:** ese sink borra **PII** (tablas de perfil), **no el registro de eventos**, que
>   Aspects conserva con el argumento de que queda *anonimizado*. Eso es el **gap 37** y está sin resolver. Ver **P45**.

**Entonces hay dos mecanismos posibles, y el (a) es el que se cotiza.**

**(a) Reloj de estado sobre `tool_dataprivacy_request` — recomendado.**

1. **Plugin `local_` propio** (GPL-3.0 por derivación del núcleo; es un plugin de Moodle, no se puede evitar) con una
   **tarea programada** (`\core\task\scheduled_task`, cada 5–15 min) que consulta
   `tool_dataprivacy_request` por filas con `type = DATAREQUEST_TYPE_DELETE` y `status` en
   `{APPROVED, COMPLETE, DELETED}` que aún no tengan marca propia de propagación.
2. **Tabla de control propia** (`local_<x>_propagation`) con `requestid`, `userid`, `stage`, `attempts`, `completed`.
   Es lo que suple la ausencia de evento: **el idempotente lo pone el plugin, no Moodle**.
3. **Fan-out en dos ramas**, cada una con su propio reintento:
   - **Telemetría.** `DELETE` de los *statements* del actor en el LRS. ⚠️ **Acá está el trabajo a medida, y hay que
     cotizarlo explícitamente:** xAPI **no define supresión** y `lrsql` (Apache-2.0) y Ralph (MIT) **no la documentan**
     (gap 33). Sobre `lrsql` es `DELETE` en SQL contra el esquema de statements; sobre Ralph, contra el backend
     (Elasticsearch/Mongo). **No es una llamada de API soportada: es intervención en el almacén, y el cliente tiene que
     firmar que lo entiende.** Si el cliente ya tiene **Learning Locker** (GPL-3.0), existe API de borrado — ⚠️ no
     verificada por esta KB, confirmar antes de prometerla.
   - **Modelo.** Si el estimador es **`pyBKT`** (MIT, no PyTorch): **reajustar desde cero sin el alumno** — barato, y da
     ***exact unlearning***, la garantía más fuerte que existe. Si es **`pyKT`** (MIT, PyTorch): *unlearning* aproximado
     con **`torchunlearn`** (MIT) **más la métrica de verificación con las métricas de *membership inference* de
     `OpenUnlearning`** (MIT). **Sin esa métrica el entregable es una promesa; con ella es un número.**
4. **Registro de auditoría** de cada etapa, con fecha y resultado, que es lo que se adjunta al expediente (**P35**).

**(b) Disparar desde afuera, si el cliente ya tiene orquestación.** Exponer el borrado como web-service y llamarlo desde
el sistema que ya coordina identidad. **Antecedente conocido:** `local_gdpr_deleteuserdata` (GPL-3.0, Dorel Manolescu),
que expone el borrado del Privacy API como web-service. ⚠️ **Antecedente de diseño, no dependencia:** es de **2018-07-08**
y declara requerir **Moodle 3.5** cuando el núcleo va por **5.3**; `moodle.org` está bloqueado por el proxy de esta
sesión y **no se localizó repositorio en GitHub**. Leer el patrón, no instalar el plugin.

**Contramedida obligatoria del mismo patrón, por P-MIA (tendencia 50).** Si el proyecto expone un **dashboard de
mastery**, el vector de estado de conocimiento **no se publica crudo**: ruido o cuantización sobre el vector expuesto, o
control de acceso por rol para que el vector completo no salga del lado docente. **Razón:** P-MIA (arXiv 2511.04716)
revierte los vectores de estado **desde las visualizaciones de radar** y con eso infiere pertenencia al entrenamiento.
**La decisión —cuánto ruido, qué rol ve qué— se escribe en el expediente**, porque es exactamente el tipo de
compensación entre explicabilidad (Anexo III) y minimización (GDPR) que un auditor quiere ver justificada.

**Piezas, todas verificadas en el pase 19:** Moodle 5.x (`core_ai` como plantilla de `privacy provider`, **GPL-3.0**) ·
`lrsql` **Apache-2.0** o Ralph **MIT** · `pyBKT` **MIT** / `pyKT` **MIT** · `torchunlearn` **MIT** · `OpenUnlearning`
**MIT** · plugin propio **GPL-3.0**.

**Tiempo estimado:** 6–8 semanas para la rama de telemetría + modelo BKT; **10–12** si el estimador es deep knowledge
tracing (la métrica de verificación es la mitad del trabajo).

**Por qué se vende.** Es la respuesta a *«¿y si un padre pide que borren todo?»*, que ningún cliente puede contestar hoy
y que **tres regímenes ya exigen**: art. 17 del GDPR (EMEA), **AB 1159** + leyes estatales (North America), **Ley 21.719**
chilena y marco brasileño (LATAM). Y es honesto en su alcance: **no promete borrado estándar de la telemetría, porque el
estándar no lo tiene** — cotiza la intervención en el almacén como lo que es.

⚠️ **Límite declarado:** el mecanismo (a) está **verificado en el fuente** (esquema, flujo de `update_request_status()`,
ausencia de eventos con control negativo) pero **no ejecutado contra una instancia de Moodle**. Es diseño leído del
código, no integración probada.

## P41 — Tutor con procedencia obligatoria y abstención fuera de alcance, para el inciso (1) de la Decisión 33 de Vietnam (agregado en el pase 19; **APAC primero por obligación con fecha, transversal por calidad**)

**Problema.** La **Decisión 33** de Vietnam clasifica como **alto riesgo** el *«contenido automatizado para apoyar el
autoaprendizaje del alumno usando **fuentes de datos no controladas**»*. Eso **no describe un modelo peligroso: describe
la arquitectura por defecto de casi todo tutor LLM** — un RAG apuntado a material arbitrario, o un modelo contestando de
memoria. Un tutor que no puede decir **de dónde salió cada afirmación** cae en el inciso.

**Y esta vez la contraparte no es una recomendación: son dos repos verificados en el pase 19.**

1. **Capa de enseñanza con citación obligatoria — `universal-examprep-skill`** (**MIT**, 299 ★, 181 commits). Declara
   **citación `archivo p.N` en cada concepto enseñado** y **100 % de abstención fuera de alcance**. Ingesta PDF/PPTX/DOCX/
   Markdown del material **del curso**, examina con las preguntas reales de la materia y registra errores. Instalable
   como skill en 40+ agentes. **Es el inciso (1) contestado con una propiedad declarada del artefacto**, no con una
   política.
2. **Aislamiento del corpus — `lumen`** (GPL-3.0, 88 ★, 828 commits) como **referencia de arquitectura**: RAG **con
   alcance por curso y citación, detrás de un único autorizador**, con aislamiento explícito para que cursos privados y
   clonados no filtren datos, decisiones del agente auditables en una tabla `llm_calls`. ⚠️ GPL-3.0: se copia el diseño
   (autorizador único + *scoping* por curso + log de decisiones), no el código, si el entregable es cerrado.
3. **Procedencia del material de origen — `openstax-mcp-server`** (MIT el código) con **la advertencia del pase 10
   puesta**: su README declara el contenido CC BY 4.0 y los bundles de OpenStax en GitHub dicen **CC BY-NC-SA** en los
   tres títulos verificados. **«Fuente controlada» implica licencia verificada título por título**, no sólo origen
   conocido. Para currículo nacional, los esquemas del pase 14 y **P31**.
4. **Marcado de lo generado — SynthID-Text** (Apache-2.0, dentro de Hugging Face Transformers, **P33**): cierra el otro
   extremo, porque lo que el tutor **genera** también tiene que ser distinguible de la fuente.
5. **Telemetría de la decisión — `learnmcp-xapi`** (MIT) sobre `lrsql` (Apache-2.0): deja registro de qué se enseñó con
   qué evidencia, que es lo que un régimen de alto riesgo audita. ⚠️ **Con el gap 33 declarado en el contrato:** ese
   almacén **no sabe borrar**; si el proyecto necesita supresión, entra **P40**.

**Alcance regulatorio, con fechas reales.** Vietnam: **2027-03-01** para un sistema nuevo (**5 meses desde hoy**),
**2027-09-01** si ya operaba antes del 2026-08-15 (**11 meses**) — **el sistema nuevo tiene menos plazo**. Y el mismo
entregable sirve, sin rehacerlo, para el **Anexo III** europeo (2027-12-02), para los mandatos de supervisión humana de
**Oklahoma y Maryland**, y para el inciso (2) de Vietnam vía **P5**.

**Tiempo estimado:** 6–8 semanas. **Por qué es la venta de entrada en APAC:** es chica, tiene fecha legal, y el
diferenciador —**citación con número de página y abstención fuera de alcance**— es verificable por el cliente en una
demo de diez minutos, no en una auditoría de seis meses.


## P42 — El expediente de conformidad como corrida reproducible, no como documento (agregado en el pase 20; **transversal, y es el que vuelve ejecutables P4, P10, P11, P17 y P39**)

**El problema que resuelve, y es un problema de esta KB antes que de un cliente.** Cinco patrones de este archivo
prometen un *expediente de conformidad* —**P4** (Anexo III europeo), **P10** (probar que el tutor enseña), **P11**
(gate de seguridad pedagógica), **P17** (accesibilidad), **P39** (privacidad)— y hasta el pase 19 ninguno decía **con
qué herramienta se corre la prueba**. El entregable era un documento. Un documento no se vuelve a correr cuando el
cliente cambia de modelo, y en 2026 el cliente cambia de modelo cada trimestre.

**Lo que cambia:** la máquina existe, es permisiva, y la publican reguladores. El entregable pasa de *informe* a
**pipeline que se vuelve a correr en cada cambio de modelo y emite el mismo informe con datos nuevos**.

### Las piezas, todas verificadas vía WebFetch en el pase 20

| Capa | Pieza | Licencia | Rol |
|---|---|---|---|
| Ejecutor | `aiverify-foundation/moonshot` (353 ★) | **Apache-2.0** | *Benchmarking* + *red-teaming*: alucinación, contenido indeseable, **divulgación de dato del alumno**, vulnerabilidad adversaria |
| Pipeline | `aiverify-foundation/moonshot-cicd` (14 ★) | **Apache-2.0** | La misma corrida dentro de CI/CD, con Docker y S3. **Es la pieza que vuelve el expediente reproducible** |
| Mapeo regulatorio | `compl-ai/compl-ai` (211 ★) | **Apache-2.0** | 29 benchmarks sobre los **6 principios núcleo del EU AI Act**. La pieza del expediente europeo |
| Sustrato de evals | `UKGovernmentBEIS/inspect_ai` (2.900 ★) | **MIT** | Donde se escribe la prueba pedagógica que no existe. 200+ evals pre-construidas, *model-graded* |
| Extensión de datos | `aiverify-foundation/moonshot-data` (45 ★) | **Apache-2.0** | Donde entra el dataset educativo como *recipe* / *cookbook* |
| Extensión de código | `aiverify-foundation/aiverify-developer-tools` (9 ★) | **Apache-2.0** | Donde entra el algoritmo de test propio |
| Informe | `aiverify-foundation/moonshot-ui` (12 ★) | **Apache-2.0** | Salida **HTML con gráficos** + JSON: lo que lee un comité de ética o una inspección |
| Contenido pedagógico | `EduBench` · `SafeTutors` | **MIT** | El qué se mide: 9 contextos educativos, 4.000+ situaciones, 12 dimensiones; y el daño |
| Contenido pedagógico | `MathTutorBench` · `UnifyingAITutorEvaluation` | CC BY 4.0 / **CC BY-SA 4.0** ⚠️ | Taxonomía de 8 dimensiones y *reward models* de calidad de enseñanza. **El share-alike se dispara si se deriva un benchmark propio con dato del cliente** |

### El wiring, y es el trabajo del gap 35

```
   EduBench (MIT) ─┐
  SafeTutors (MIT) ─┼──► empaquetado como *recipe* / cookbook ──► moonshot-data (Apache-2.0)
                    │         ⚠️ ESTE PASO NO EXISTE (gap 35) — es el trabajo de integración
                    │
  prueba pedagógica ┴──► plugin de test ──► aiverify-developer-tools (Apache-2.0)
                                                      │
   agente educativo del cliente ◄───── evalúa ────────┤
                                                      ▼
                                              moonshot-cicd  (corre en cada deploy)
                                                      │
                            ┌─────────────────────────┴────────────────────────┐
                            ▼                                                  ▼
                 moonshot-ui → informe HTML                      compl-ai → mapeo a los 6
                 (comité de ética, inspección)                   principios del EU AI Act
```

**Las tres fases, con corte comercial limpio:**

1. **Fase 1 — la corrida base, sin nada educativo (2–3 semanas).** `moonshot-cicd` sobre el agente del cliente con los
   *cookbooks* del Starter Kit de IMDA ya existentes: alucinación, contenido indeseable, **divulgación de datos**,
   prompts adversarios. **Ya entrega valor** y no depende de cerrar ningún gap. Es la demo de diez minutos.
2. **Fase 2 — la capa pedagógica (4–6 semanas).** Empaquetar `EduBench` y `SafeTutors` (**MIT, sin fricción**) como
   *recipes* y escribir la prueba pedagógica propia sobre `inspect_ai`. **Acá se cierra el gap 35**, y es el
   diferenciador: nadie en el mercado tiene esto, porque los tres catálogos de la capa declaran cobertura de
   **derecho, medicina y finanzas** y no de educación.
3. **Fase 3 — el mapeo regulatorio (3–4 semanas, sólo EMEA).** Mapear las pruebas a los 6 principios de `compl-ai`
   para el expediente del **Anexo III**. Sólo tiene sentido donde el régimen es exigible.

**Plazo y alcance.** Fase 1: **2–3 semanas**. Las tres: **3–4 meses**.

### Dónde se vende primero, y hay un orden

1. **LATAM** — es donde el desajuste es mayor y la competencia, nula: **Brasil** (PL 2338/2023 pide **evaluación de
   impacto algorítmico** y **auditorías periódicas**), **Chile** (Ley 21.719 vigente + proyecto con auditoría para alto
   riesgo) y **México** (**auditoría al menos anual** de alto riesgo) legislan la auditoría y **la región no produce
   una sola herramienta que la ejecute**. Motor de compra normativo + cero oferta local.
2. **EMEA** — es donde el régimen es **vinculante** (aplicación desde el **2026-08-02**, Anexo III el **2027-12-02**) y
   donde la pieza mapeada es local (`compl-ai`, ETH Zürich). Fase 3 obligatoria.
3. **North America** — el argumento de entrada es el **crosswalk a NIST AI RMF**: no es software exótico, está mapeado
   al marco federal que el cliente ya conoce. Y con **134 proyectos de ley en 31 estados**, el comprador ya tiene el
   problema.
4. **APAC** — es donde nació la herramienta, así que el diferenciador no es traerla: es **la capa educativa que le
   falta**.

⚠️ **Lo que este patrón NO promete, y hay que decirlo en la primera reunión.**

- **No certifica.** `aiverify` declara por escrito que no define estándares éticos y **no garantiza** que el sistema
  evaluado esté libre de riesgos o sesgos. Se entrega **evidencia reproducible**, que es lo que una auditoría pide.
- **El marco de Singapur es voluntario** (sin penalidad, sin registro, sin *enforcement*). Moonshot es **herramienta**
  en un proyecto europeo, nunca **cumplimiento** europeo.
- **No hay crosswalk directo de AI Verify al EU AI Act** — sólo a **NIST AI RMF** (oct-2023) y a **ISO/IEC 42001:2023**
  (jun-2024). Al AI Act se llega **indirecto por ISO 42001**.
- **`aiverify` no evalúa agentes** (tabular e imagen supervisados). El tutor se prueba con Moonshot, Inspect o COMPL-AI.
- **`LLM-Evals-Catalogue` no tiene licencia declarada**: se lee para orientarse, **no se incorpora** a un entregable.
- **`MathTutorBench` es CC BY 4.0 y `UnifyingAITutorEvaluation` es CC BY-SA 4.0.** Derivar un benchmark propio con dato
  del cliente **dispara el share-alike** del segundo. Las dos piezas limpias son `EduBench` y `SafeTutors` (MIT).

**El bonus de posicionamiento, y no cuesta nada extra.** Como las dos puntas son MIT y Apache-2.0, la capa educativa se
puede **contribuir hacia arriba**: a `moonshot-data`, a `compl-ai` (ETH Zürich) o al `LLM-Evals-Catalogue` del
regulador singapurense. Un entregable de cliente se convierte en **la referencia pública de evaluación educativa de la
industria**, que es exactamente el hueco que los tres catálogos declaran tener.

## P43 — El alumno simulado que de verdad no sabe, para evaluar al tutor sin poner chicos adelante (agregado en el pase 20; **transversal, y es la pieza que le faltaba a P10**)

**El problema que resuelve.** **P10** promete *probar que el tutor enseña, no que responde*, y el **gap 1** viene
diciendo desde el pase 4 que el estándar de evaluación pedagógica **existe, está premiado en EMNLP, NAACL y ACL, y no
se adopta en producción**. Una de las razones prácticas de esa no-adopción es que **medir enseñanza requiere un alumno
que no sepa**, y las dos opciones conocidas son malas: poner alumnos reales (lento, caro y, con menores, regulado — ver
el pase 16) o pedirle a un LLM que *«actúe como principiante»*, que **no funciona**: el modelo se escapa hacia
explicaciones de experto y el diálogo deja de medir lo que se quería medir.

**La pieza nueva, y es educativa.** `GEMLab-HKU/Unlearn_and_Relearn` (**MIT**, 4 ★, 22 commits, Universidad de Hong
Kong) ataca exactamente eso: aplica **machine unlearning** para volver **genuinamente novato** a un modelo que sabe, de
forma **configurable (10–50% de olvido)**, y después mide cuánto **recupera** cuando se le enseña. Arquitectura de tres
etapas y un loop de tres partes **Coach / Teachable Agent / Judge**.

### Las piezas

| Pieza | Licencia | Rol |
|---|---|---|
| `GEMLab-HKU/Unlearn_and_Relearn` | **MIT** ✅ | **Arquitectura de referencia.** Unlearning por destilación con intervención → relearning → loop Coach/Teachable Agent/Judge |
| `torchunlearn` (`machine-unlearning-pytorch`) | **MIT** ✅ | Los 20 algoritmos de *unlearning* si hay que reimplementar la etapa 1 |
| `UnifyingAITutorEvaluation` | CC BY-SA 4.0 ⚠️ | La taxonomía de **8 dimensiones** contra la que se puntúa al tutor |
| `MathTutorBench` | CC BY 4.0 ⚠️ | *Reward models* entrenados de calidad de enseñanza y leaderboard |
| `EduBench` · `SafeTutors` | **MIT** ✅ | Las piezas limpias: 9 contextos educativos y seguridad pedagógica |
| `moonshot` / `inspect_ai` | **Apache-2.0** / **MIT** ✅ | Donde corre todo esto como prueba repetible (ver **P42**) |

### El wiring

1. **Fabricar el alumno.** Tomar un modelo abierto y aplicarle *unlearning* sobre los **componentes de conocimiento
   específicos** de la materia del engagement, al nivel de olvido que corresponda al curso (el repo parametriza 10–50%).
2. **Enseñarle con el tutor del cliente.** El tutor a evaluar toma el rol de **Coach** contra el *Teachable Agent*.
3. **Medir recuperación, no satisfacción.** La métrica es **cuánto conocimiento recupera el alumno simulado**, puntuado
   con la taxonomía de 8 dimensiones y los *reward models* de `MathTutorBench`. **Es la métrica que P10 siempre quiso y
   no tenía cómo producir:** no mide si la respuesta del tutor es buena, mide si **el alumno aprendió**.
4. **Empaquetarlo como prueba.** Entra como *recipe* en **P42** y se vuelve a correr en cada cambio de modelo.

**Plazo y alcance.** Prueba de concepto sobre una materia: **4–6 semanas**. Como capa de evaluación integrada a P42:
**2–3 meses**.

**Dónde se vende primero.** **EMEA** y **North America**, por la misma razón y es regulatoria: donde hay supervisión
humana obligatoria y prohibición de decisiones de alto impacto (Oklahoma, Maryland) o evaluación de conformidad previa
(Anexo III), **evaluar al tutor sin exponer alumnos reales es un argumento de cumplimiento, no sólo de ingeniería**. Y
en **North America** hay un filo extra: **AB 1159 prohíbe usar dato de alumnos para entrenar modelos** — un alumno
sintético producido por *unlearning* **no es dato de alumno**.

⚠️ **Lo que este patrón NO promete.**

- **4 estrellas y 0 forks.** Es **arquitectura de referencia, no dependencia** — mismo criterio con el que el pase 8
  trató a `tero`. Hay que leer el código antes de comprometerlo en un plan.
- **El paper no se verificó de primera mano:** `arxiv.org` y `link.springer.com` están bloqueados por el proxy de
  egreso de esta sesión. Lo verificado es el **repo** (licencia MIT, 22 commits, autoría GEMLab-HKU).
- **No cierra el gap 34 y no hay que presentarlo como privacidad.** Este *unlearning* es **pedagógico**: borra para
  fabricar un alumno, no para proteger a uno. El derecho al olvido sobre el modelo de *mastery* sigue siendo el **gap
  34**, y su camino es **P38** / **P40**.
- **El alumno simulado no reemplaza la validación con alumnos reales** para un despliegue. Reemplaza la **iteración**:
  permite cien corridas antes de la primera clase, no evitar la primera clase.

## P44 — La supresión del alumno en la telemetría, que resulta que ya estaba implementada: encenderla, evidenciarla y propagarla (agregado en el pase 21; **EMEA primero por art. 17, North America por AB 1159, LATAM con la Ley 21.719 chilena**)

**Problema.** Esta KB vendió durante seis pasadas que el almacén de telemetría del alumno **no sabía borrar**, y que
intervenirlo era alcance a medida. **Es falso**, y el pase 21 lo verificó leyendo el código de los tres LRS (ver la
tendencia **54**). El trabajo real es otro, es mucho más chico, y es el que este patrón empaqueta: **encender una
capacidad que viene apagada, producir la evidencia que la capacidad no produce, y conectar el disparador que
efectivamente no existe.**

**Por qué es el patrón de menor costo de entrada de toda esta KB.** No hay que construir el borrado. Hay que
configurar, instrumentar y conectar.

### Las piezas, todas ya verificadas en esta KB

| Pieza | Licencia | Rol en este patrón |
|---|---|---|
| **`lrsql`** (Yet Analytics) | **Apache-2.0** ✅ | El almacén. **Trae el primitivo**: `DELETE /admin/agents` por `actor-ifi`, cascada sobre 7 tablas, transaccional |
| **Moodle** `tool_dataprivacy` | GPL-3.0 ⚠️ | El lado donde el pedido de supresión **se registra y se aprueba** (pase 19). No forkear: plugin |
| **`learnmcp-xapi`** | **MIT** ✅ | El puente agente ↔ LRS que esta KB ya recomienda. Declara `lrsql` como backend |
| **OpenUnlearning** | **MIT** ✅ | Sólo si el alcance incluye el modelo. Es el **gap 34**, y no hay que prometerlo acá |

### El wiring, en tres pasos, y el tercero es el único que es desarrollo

**Paso 1 — encender el primitivo. Es una variable de entorno, no una historia de usuario.**

```bash
# lrsql, config de producción: viene en false
LRSQL_ENABLE_ADMIN_DELETE_ACTOR=true
```

Con el flag apagado **la ruta no se registra** (`routes.clj:407`), así que el síntoma es un 404 y no un 403 — conviene
saberlo antes de depurarlo. Encendido, la supresión de un alumno es **una llamada**:

```
DELETE /admin/agents        body: { "actor-ifi": "mbox::mailto:alumno@escuela.edu" }
  └─> delete-actor-and-dependents!   (una transacción, 7 tablas)
        statement_to_statement · statement_to_activity · attachment · xapi_statement
        agent_profile_document · state_document · actor
        └─> statement_to_actor se borra por ON DELETE CASCADE
```

**Paso 2 — producir la evidencia, porque el producto no la produce.** Acá se cierra el **gap 36**. `lrsql` responde
`200` con el `actor-ifi` que le mandaste y **descarta el conteo de filas afectadas**, que el SQL ya calcula
(`-- :result :affected`). Dos caminos, y conviene hacer los dos:

- **El entregable del cliente:** envolver la llamada en un servicio propio que, **antes** de borrar, cuente los
  statements del actor (`GET /xapi/statements?agent=…`), **después** vuelva a contar, y registre el par
  *(antes, después, timestamp, operador, id del pedido en `tool_dataprivacy`)* en un registro append-only. **Eso es el
  expediente del art. 17**, y es lo que un régimen de alto riesgo audita.
- **La contribución hacia arriba:** devolver el `:affected` en el body del interceptor. Son pocas líneas sobre un repo
  **Apache-2.0**, el dato ya existe, y convierte un entregable de cliente en posicionamiento público — el mismo
  movimiento que el pase 20 identificó para el gap 35.

**Paso 3 — el disparador, que es el único trabajo real y hay que cotizarlo como integración.**

```
Moodle tool_dataprivacy              ⚠️ ESTE PASO NO EXISTE — es el trabajo de integración
  pedido aprobado  ──────────?──────────▶  DELETE /admin/agents   ──▶  ✅ borra
       │                                                                    │
       │ no hay evento de "borrado completado"                              │ no hay evento
       │ (pase 19, verificado en el árbol de Moodle)                        │ (pase 21)
       ▼                                                                    ▼
  hay que sondear tool_dataprivacy_request.status            hay que registrar el conteo uno mismo
```

Ninguno de los dos extremos emite evento, así que el pegamento es **un sondeo más un registro**, no una suscripción.
**Y la limitación está reconocida por un proveedor, lo que la vuelve defendible en una propuesta:** el Feature Wiki de
**ILIAS** declara por escrito que al borrar un objeto xAPI/cmi5 el dato personal **persiste en el LRS** y que ILIAS
**no tiene forma de borrarlo** (tendencia **55**). No es una carencia que invente esta KB.

### Cómo se cotiza, que es lo que cambió

| | Lo que esta KB cotizaba hasta el pase 20 | Lo que corresponde cotizar |
|---|---|---|
| Borrado en el LRS | **Desarrollo a medida** sobre el almacén, o asumir copyleft | **Configuración.** Una variable de entorno |
| Evidencia | No estaba identificada | **Servicio chico + registro append-only** (gap 36) |
| Disparador LMS→LRS | Desarrollo | **Desarrollo** — sigue siendo esto, y es lo único |

### ⚠️ Lo que este patrón NO promete

- **No alcanza al modelo.** Borra el **registro** (statements, documentos de estado y perfil, el actor). **No borra la
  influencia del dato sobre el estimador de *mastery***: eso es el **gap 34** y el camino es **P38**. Prometer "derecho
  al olvido" sin decir esto es prometer de más.
- **No es conformidad con el estándar, y hay que escribirlo en el contrato.** **xAPI / IEEE 9274.1.1 no define
  supresión** —define *voiding*, que marca sin borrar—. El endpoint de `lrsql` es **extensión propia del producto**: si
  el cliente cambia de LRS, **esto no es portable**.
- 🔴 **Con Ralph sobre ClickHouse este patrón no se puede ejecutar — y CORRECCIÓN DEL PASE 22: eso no es una
  elección del cliente, es el default de Open edX.** El pase 21 escribió esta advertencia como condicional (*«si el
  cliente ya eligió ese backend por analítica»*). **No es condicional.** El plugin de analítica **oficial** de Open
  edX —**Aspects**, `openedx/tutor-contrib-aspects`, Apache-2.0, 2.269 commits— **instala Ralph sobre ClickHouse**,
  junto con Superset, Vector, event-routing-backends y dbt. Un cliente con Open edX y analítica **no eligió** el
  backend difícil de borrar: lo tiene de fábrica. **Hay que levantarlo en el discovery como supuesto por default**,
  no al llegar al expediente de privacidad.
  **Y la razón hay que decirla bien:** ClickHouse no tiene `UPDATE`/`DELETE` de propósito general al estilo OLTP, pero
  **sí** tiene borrado liviano sobre MergeTree detrás de un setting y mutaciones `ALTER TABLE … DELETE`. La
  imposibilidad **práctica** se sostiene —no transaccional, dependiente de versión, y el backend ClickHouse de Ralph
  no lo expone en la API del LRS—, pero *«el motor no puede»* es falso y un arquitecto del cliente lo va a corregir.
  ⚠️ Dependiente de versión, no verificado de primera mano. Ver **P45** y el **gap 37**.
- **Con Learning Locker, cuatro condiciones más:** el flag `ENABLE_STATEMENT_DELETION` (en `false` el worker descarta
  el job **en silencio**), la **ventana UTC** de borrado y la dependencia del proceso *scheduler* que rescata los jobs
  fuera de ventana, el hecho de que **`done:true` no significa borrado** (hay que comparar `deleteCount` contra
  `total`), y que **`terminate` no es rollback**. Más el dato que decide: **el código no se mueve desde el
  2021-11-16** (tendencia **56**).
- **El borrado no es reversible y no hay confirmación previa.** `delete-actor-and-dependents!` corre en una
  transacción y no tiene *dry-run*. El conteo previo del paso 2 cumple además esa función: **es la única oportunidad de
  ver qué se va a borrar antes de borrarlo.**

---

## P45 — El expediente de supresión sobre Open edX + Aspects: la plataforma donde el disparador ya existe y lo que falta es la auditoría de qué se borró de verdad (agregado en el pase 22; **EMEA primero por art. 17, North America por AB 1159, transversal por Anexo III**)

**Problema.** Un cliente sobre **Open edX** con analítica tiene, sin haberlo decidido, el stack oficial **Aspects**:
Ralph sobre ClickHouse, Superset, dbt. Cuando llega un pedido del art. 17, pasan dos cosas al mismo tiempo y las dos
hay que decirlas: **(1)** el disparador existe —el `UserRetirementSink` escucha `USER_RETIRE_LMS_MISC` y borra la PII
de ClickHouse—, y **(2)** lo que queda en la telemetría es el **registro conductual completo**, conservado con el
argumento de que está *anonimizado*. **El entregable de este patrón no es construir el borrado: es auditar y
evidenciar qué se borró, y cerrar por contrato lo que no.**

**Por qué es distinto de P44.** P44 es el patrón para **`lrsql`**: ahí el primitivo de borrado es excelente
(por `actor-ifi`, 7 tablas, transaccional) y **viene apagado**. Acá el primitivo es **parcial** (PII sí, eventos no) y
**viene encendido**. Son dos ventas distintas: P44 enciende y evidencia; **P45 audita, acota y documenta.**

### Las piezas, todas verificadas en esta KB

| Pieza | Licencia | Rol en este patrón |
|---|---|---|
| **`tutor-contrib-aspects`** · `openedx` | **Apache-2.0** ✅ | El stack que el cliente **ya tiene**: ClickHouse + Superset + Ralph + Vector + event-routing-backends + dbt |
| **`platform-plugin-aspects`** · `openedx` | **Apache-2.0** ✅ | Donde vive el **`UserRetirementSink`** y el flag `ASPECTS_ENABLE_PII`. **Es el archivo que hay que leer**, no el que hay que escribir |
| **Open edX** `user_retirement` | AGPL-3.0 ⚠️ | El lado donde el pedido se registra y se aprueba. **No forkear:** el sink entra por señal, es el punto de extensión limpio |
| **`inspect_ai`** (UK AISI) | **MIT** ✅ | Para empaquetar la auditoría como **corrida reproducible** y no como documento. Es **P42** aplicado acá |
| **OpenUnlearning** | **MIT** ✅ | Sólo si el alcance incluye el modelo. Es el **gap 34** y **no hay que prometerlo** |

### El wiring, en cuatro pasos, y el único desarrollo real es el paso 3

**Paso 1 — leer el sink antes de prometer nada. Es el paso que decide si el resto del patrón es vendible.**
Hay que contestar la pregunta del **gap 37** sobre la instancia del cliente: cuando corre el `UserRetirementSink`,
**¿qué le pasa al identificador del actor en las tablas de eventos — se borra, se rota o se deja?**

```
UserRetirementSink  ──escucha──▶  señal Django USER_RETIRE_LMS_MISC
       │
       ├──▶ borra PII en ClickHouse:  user_profile · external_id · auth_user
       │                               (gobernado por ASPECTS_ENABLE_PII)
       │
       └──▶ ❓ tablas de eventos / statements xAPI  ── ¿actor-ifi?
                 • si se BORRA o se ROTA  → la postura de Aspects es defendible, escribirlo así
                 • si se DEJA             → es dato personal pseudonimizado, y hay que decirlo en el contrato
```

**Si se deja, la frase que corresponde en la propuesta no es «cumplimos el art. 17»**, es *«se suprime la
identificación directa y se conserva el registro de actividad pseudonimizado, cuya base legal de retención hay que
declarar»*. Esa frase es defendible; la otra no.

**Paso 2 — verificar que el control de privacidad no esté sorteado.** El **PR #1328** de `tutor-contrib-aspects`
documenta que el *job* manual de *backfill* volcaba `user_profile` / `external_id` a ClickHouse **aun con
`ASPECTS_ENABLE_PII=False`**, *«sorteando exactamente la protección que ese setting existe para dar»*. 🔴 **Está
cerrado sin mergear (2026-09-16).** Entonces: comprobar en la versión del cliente si el *check* de PII está en el
camino manual **además** del automático. **Si no está, el flag no es un control y no se puede escribir como tal en un
expediente.**

**Paso 3 — producir la evidencia, porque el producto no la produce.** Es el mismo trabajo que el paso 2 de **P44** y
es el único desarrollo: envolver la retirada en un servicio propio que **cuente antes y después** —statements del
actor, filas en las tablas de PII— y registre el par *(antes, después, timestamp, operador, id del pedido de
retirement)* en un registro **append-only**. Sobre ClickHouse el conteo se hace con SQL directo contra las tablas de
eventos, que es más fácil que en P44: **la analítica ya está instalada y Superset ya está ahí para mostrarlo.** Ese
registro **es** el expediente del art. 17.

**Paso 4 — empaquetarlo como corrida reproducible (P42), no como PDF.** La auditoría de los pasos 1–3 se escribe como
*eval* sobre **`inspect_ai`** (MIT): dado un usuario de prueba, retirarlo y **afirmar** que las tablas de PII quedaron
vacías y que el identificador de actor hizo lo que el paso 1 determinó. Así el expediente **se vuelve a correr en cada
upgrade de Aspects** en vez de envejecer — y los upgrades de Aspects son frecuentes (2.269 commits).

### Cómo se cotiza

| | Lo que parecía | Lo que corresponde cotizar |
|---|---|---|
| Disparador LMS → telemetría | Desarrollo (como en Moodle) | **Ya existe.** Lectura y verificación del sink |
| Borrado de PII | Desarrollo | **Ya existe y viene encendido.** Verificación |
| Borrado del registro de eventos | Se asumía incluido | 🔴 **NO existe.** Es decisión de retención y **cláusula contractual**, no desarrollo |
| Evidencia | No estaba identificada | **Servicio chico + registro append-only** (igual que P44) |
| Repetibilidad | — | ***Eval* sobre `inspect_ai`** (P42) |

### ⚠️ Lo que este patrón NO promete

- **No borra el registro de aprendizaje, y ésa es la parte que el cliente cree que está comprando.** Aspects conserva
  los eventos. Si el cliente necesita supresión real del registro conductual sobre Open edX, **el stack oficial no la
  da** y hay que discutir arquitectura: migrar la telemetría a **`lrsql`** (Apache-2.0, y entonces es **P44**, que sí
  borra por actor en cascada) o aceptar y declarar la retención. **Esa conversación va al principio del proyecto.**
- **No alcanza al modelo.** Igual que P44: borra registro, no influencia en los pesos. Es el **gap 34**, camino **P38**.
- **No está cerrado el gap 37, y el paso 1 es literalmente ir a cerrarlo.** Esta KB **no verificó de primera mano** qué
  pasa con el identificador del actor: el ADR de PII de Aspects vive en `docs.openedx.org`, bloqueado por el proxy en
  el pase 22. **No presentar la lectura optimista ni la pesimista como hecho verificado** — el paso 1 existe para
  contestarlo sobre la instancia real, que además es la única respuesta que importa.
- **Y la limitación está reconocida por dos proveedores, lo que la vuelve defendible.** El Feature Wiki de **ILIAS**
  declara por escrito que el dato personal **persiste en el LRS** al borrar un objeto xAPI/cmi5 (tendencia **55**), y
  Aspects documenta su retención **en su propia decisión de arquitectura**. **No es una carencia que invente esta KB.**

## P46 — La evidencia de borrado en el LRS, parcheada por backend: el upstream chico que convierte un `200` vacío en un expediente (agregado en el pase 23; **EMEA primero por art. 17, North America por AB 1159, transversal por Anexo III**)

**Qué problema resuelve.** P44 y P45 llegan los dos al mismo muro: se puede *borrar* el dato del alumno en la telemetría,
pero no se puede *probar* qué se borró. `lrsql` responde `{:status 200 :body params}`, que es un eco del `actor-ifi` que
mandó el cliente — **no es prueba de nada** ante un expediente del art. 17 o de **AB 1159** (operativa el **2027-07-01**).
Este patrón es el parche, y el pase 23 lo dimensionó leyendo los tres backends (tendencia **60**).

**Las piezas, todas verificadas de primera mano sobre el árbol clonado (HEAD del 2026-10-01):**

| Pieza | Licencia | Rol |
|---|---|---|
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | **Apache-2.0** ✅ | El LRS a parchear. Apache-2.0 → **el upstream es viable y el fork también** |
| [openfun/ralph](https://github.com/openfun/ralph) | **MIT** ✅ | Alternativa de LRS si el cliente está en Open edX — **pero no tiene `DELETE` en ningún router**, así que acá no aplica: el parche es sobre `lrsql` |
| [openedx/tutor-contrib-aspects](https://github.com/openedx/tutor-contrib-aspects) | **Apache-2.0** ✅ | Quien dispara el borrado aguas arriba (P44/P45) |

**El wiring, y es distinto en cada backend — ésa es la parte que hay que presupuestar:**

1. **Encender la ruta.** `LRSQL_ENABLE_ADMIN_DELETE_ACTOR=true`. Viene en `false`, y apagada el síntoma es **404, no 403**
   (`src/main/lrsql/admin/routes.clj:407`). Sin esto no hay nada que parchear.
2. **SQLite — recoger los siete conteos que ya se calculan.** En
   `src/db/sqlite/lrsql/sqlite/record.clj:169–176` las siete queries se invocan como expresiones sueltas y Clojure
   devuelve sólo la séptima. Envolver en `let`, bindear las siete y devolver un mapa por tabla
   (`{:statement-to-statement n :statement-to-activity n :attachment n :xapi-statement n :agent-profile-document n
   :state-document n :actor n}`). **~8 líneas, el dato ya está: sólo se está tirando.**
3. **PostgreSQL / MariaDB — partir el SQL antes de poder recoger nada.** En los dos,
   `delete-actor-and-dependents!` es **un** nombre HugSQL con **siete `DELETE` adentro**, así que hay un solo número
   disponible. Para obtener el desglose hay que **partirlo en siete queries con nombre**, como SQLite ya las tiene, y
   después aplicar el paso 2. **Es refactor de SQL, no plomería.**
4. **Devolver el conteo en vez del eco.** En `src/main/lrsql/admin/interceptors/lrs_management.clj:23–33`, el cuerpo es
   `(adp/-delete-actor lrs params)` **como expresión suelta cuyo retorno se descarta**, y la respuesta es
   `{:status 200 :body params}`. Bindear ese retorno y devolverlo junto al `actor-ifi`, el timestamp y el admin que
   ejecutó.
5. **Persistir el expediente fuera del LRS.** El conteo en la respuesta HTTP se pierde con la sesión: escribirlo en una
   tabla de auditoría propia (o en el `llm_calls`-style de la aplicación) con `actor-ifi` **hasheado**, timestamp, admin,
   backend y el mapa de conteos. Eso es lo que se adjunta al expediente.

**Estimación:** 2–3 semanas incluyendo el *upstream* de los pasos 2–4 (Apache-2.0, cambio chico, sin dependencias nuevas).
Si el cliente no quiere esperar el *merge*, el fork es legal y el *rebase* es barato porque el cambio toca 4 archivos.

🔴 **Lo que hay que decir en la propuesta, y es incómodo pero es el hallazgo del pase.** La ventaja que esta KB le vende a
`lrsql` —*«corre sobre la base de datos que el cliente ya opera»*— **no se extiende a la evidencia**. Un despliegue sobre
SQLite llega al desglose de siete tablas con ~8 líneas; **el mismo producto sobre PostgreSQL no pasa de un número sin tocar
el SQL.** Cuando el alcance incluya prueba de supresión, **el motor de base de datos es una decisión de cumplimiento, no de
infraestructura**: hay que preguntarlo en el *discovery*.

> 🔴 **SUPERADO POR EL PASE 24 (2026-10-01) — este patrón queda reemplazado por P47, y la advertencia de abajo ya
> está contestada.** Se midió ejecutando: el driver **no** entrega un solo valor por limitación del SQL — entrega
> **los siete conteos en orden** (`[7, 2, 3, 8, 5, 6, 1]`) por el bucle `getMoreResults()` de JDBC estándar, así que
> **no hay que partir el SQL** y el parche del gap 36 es más chico que lo estimado acá. El número que hoy se ve es el
> del **primer** `DELETE`, y vale **`0`** para el alumno sin sub-sentencias. Y apareció el **gap 38**: en MariaDB/MySQL
> el borrado **falla entero** si `allowMultiQueries` quedó apagado. **Usar P47**, que incluye el paso 0 de verificación.
> Se conserva este patrón por su cadena de razonamiento y por las coordenadas del parche, que siguen siendo válidas.

⚠️ **Lo que no está medido, y no se infiere.** Cuál de los siete `DELETE` reporta el driver JDBC en el `:execute`
multi-sentencia de PostgreSQL/MariaDB (el primero, el último o la suma) **no se verificó ejecutando**. La lectura del código
prueba que hay **un solo valor disponible**, que es lo que sostiene el patrón; el valor exacto es la acción que el pase 23
deja escrita: levantar `lrsql` sobre PostgreSQL, borrar un actor con datos en las siete tablas y leerlo.

- **No alcanza al modelo.** Igual que P44 y P45: esto audita el registro, no la influencia en los pesos. Sigue siendo el
  **gap 34**, camino **P38**.

---

## P47 — El expediente de supresión del LRS con el desglose que ya está en el cable, y la verificación de que el borrado puede ocurrir (agregado en el pase 24; **EMEA primero por art. 17, North America por AB 1159, transversal por Anexo III**)

**Este patrón reemplaza la estimación de P46, no la contradice en su objetivo.** P46 se escribió sobre la lectura del pase
23 —que el desglose por tabla exigía partir el SQL— y sobre una incógnita declarada: *cuál* de los siete `DELETE` reporta el
driver. **El pase 24 lo midió y las dos cosas cambian:** el desglose **ya vuelve completo** por JDBC estándar, y el número
que hoy se ve es el del **primer** `DELETE`, que vale **`0`** para el alumno típico. P47 es P46 con la plomería medida, más
una verificación previa que P46 no tenía porque nadie sabía que hacía falta.

### Paso 0 — la verificación que va antes de todo lo demás, y que puede cancelar el resto (gap 38)

🔴 **Antes de prometer un expediente de supresión sobre `lrsql` con MariaDB o MySQL, hay que comprobar que el borrado
puede siquiera ejecutarse.** Medido en el pase 24: con `allowMultiQueries` en el default del driver (`false`),
`delete-actor-and-dependents!` **falla entera** con error **1064 / SQLState 42000**. Y lrsql trae el parámetro sólo como
*fallback* de aero, así que **cualquier** uso de `LRSQL_DB_PROPERTIES` —o de `LRSQL_DB_JDBC_URL`— lo apaga en silencio.

| Qué preguntar en el *discovery* | Por qué | Qué hacer si la respuesta es la mala |
|---|---|---|
| ¿El backend es MariaDB o MySQL? | Si es PostgreSQL o SQLite, el paso 0 no aplica | Seguir al paso 1 |
| ¿Está definida `LRSQL_DB_PROPERTIES`? | Si está, **reemplazó** el default y `allowMultiQueries=true` ya no está | Re-agregarlo **al string del operador**, no en vez de él: `allowMultiQueries=true&<lo-que-ya-tenía>` |
| ¿Está definida `LRSQL_DB_JDBC_URL`? | Override total de las propiedades | Agregar `allowMultiQueries=true` a la query de la URL |
| ¿Hay un test que pruebe un borrado de actor de punta a punta? | **No existe en el proyecto** | Es el primer entregable: el test de regresión que detecta el apagón de configuración |

**Entregable del paso 0, y es media jornada:** un *preflight* que corre contra el despliegue del cliente, borra un actor
sintético con filas en las siete tablas y falla ruidosamente si el resultado no es el esperado. **Eso solo ya vale como
venta chica**, porque convierte un fallo que aparece el día del expediente en un fallo que aparece en CI.

### Paso 1 — recoger el desglose entero, que es la corrección a P46

**No hay que partir el SQL.** Medido sobre PostgreSQL 16.14 + pgjdbc 42.7.4 y MariaDB 10.11.14 + Connector/J 3.4.1, con el
DDL y el SQL propios de lrsql: el driver parte la cadena multi-sentencia y entrega **los siete conteos en el orden de los
siete `DELETE`**.

| | |
|---|---|
| **Lo que hay hoy** | un conteo: el del **primer** `DELETE` (`statement_to_statement`) |
| **Lo que ya está disponible** | `[st2st, st2activ, attachment, xapi_statement, agent_profile, state_document, actor]` — medido: `[7, 2, 3, 8, 5, 6, 1]` |
| **Dónde está el parche** | en la capa que **recoge** el resultado, no en el SQL ni en el driver: hay que drenar `getMoreResults()` en vez de leer un conteo |
| **Qué NO hay que hacer** | cablear el conteo único «porque ya está». **Vale `0` para el alumno sin sub-sentencias** — 25 filas borradas, el expediente diría `0` |

🔴 **La trampa, escrita para que no se repita:** un expediente que afirma «0 filas borradas» sobre una supresión exitosa es
**peor** que el `200` vacío que el pase 21 denunció. El `200` vacío no afirma nada; el `0` afirma algo falso y es
exactamente lo que un auditor usa para decir que el borrado no ocurrió.

### Paso 2 — contar aparte lo que se va en cascada, porque no aparece en ningún conteo

`statement_to_actor` —**la tabla que vincula al alumno con su rastro**— no la borra ninguno de los siete `DELETE`. Se va
sólo por `ON DELETE CASCADE` desde `xapi_statement`, y **las filas en cascada no se cuentan en ningún *update count* de
JDBC**. En el fixture del pase 24 eran **10 filas** y ninguna medición las vio.

| Motor | De dónde sale la cascada | Qué verificar en el despliegue |
|---|---|---|
| **MariaDB** | Nativa en la tabla (`statement_fk_stactor`) | `information_schema.referential_constraints` → `delete_rule = CASCADE` |
| **PostgreSQL** | **Por migración** (`add-statement-to-actor-cascading-delete!`) | `pg_constraint` → que `statement_fk` diga `ON DELETE CASCADE`. **En un despliegue viejo sin migrar no está** |

**Entonces el expediente honesto hace una de dos cosas:** un `SELECT count(*)` sobre `statement_to_actor` **antes** del
borrado y lo declara como línea propia, o dice explícitamente que ese número no se cuenta. Las dos son defendibles; omitirlo
sin decirlo, no.

### El stack, nombrado

| Pieza | Repo | Licencia | Rol |
|---|---|---|---|
| LRS | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** ✅ | El almacén y el sitio de los tres parches |
| Transformación LMS → xAPI | [`openedx/event-routing-backends`](https://github.com/openedx/event-routing-backends) | **Apache-2.0** ✅ | De donde viene el dato (ver **P45**) |
| Disparador del lado LMS | [`openedx/platform-plugin-aspects`](https://github.com/openedx/platform-plugin-aspects) | **Apache-2.0** ✅ | `UserRetirementSink` — el evento que inicia la cadena |
| Orquestación del expediente | [`temporalio/temporal`](https://github.com/temporalio/temporal) | **MIT** ✅ | Durabilidad y reintento del flujo de supresión (ver **P40**) |
| Conformidad como corrida | [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) | **MIT** ✅ | El expediente como corrida reproducible (ver **P42**) |

### Plazo y alcance

| | |
|---|---|
| **Paso 0 (preflight + test de regresión)** | **0,5–1 semana.** Es la venta más chica de esta KB y la más defendible: evita un fallo de cumplimiento, no agrega una capacidad |
| **Paso 1 (drenar los siete conteos)** | **1–2 semanas** incluyendo el *upstream* a Yet Analytics. Baja respecto de P46 porque no hay refactor de SQL |
| **Paso 2 (cascada declarada)** | **0,5 semana** |
| **Expediente completo sobre un despliegue existente** | **4–6 semanas**, encadenado con **P45** si el LMS es Open edX |

### Advertencias

- **No alcanza al modelo.** Igual que P44, P45 y P46: esto audita el registro, no la influencia en los pesos. Sigue siendo
  el **gap 34**, camino **P38**.
- **Un eslabón sigue inferido.** Qué devuelve exactamente `next.jdbc` con `:result :affected` no se midió —`repo.clojars.org`
  responde **403** por el proxy de egreso— así que **dónde** vive el parche del paso 1 (adaptador de HugSQL, `next.jdbc` o el
  interceptor de lrsql) hay que confirmarlo antes de presupuestar el *upstream*. Que el desglose **esté disponible** sí está
  medido, y es lo que sostiene el patrón.
- **El *blast radius* del gap 38 no está enumerado.** Que el borrado de actor sea la única consulta multi-sentencia del
  producto es lo que se desprende de cuatro pases de lectura, pero no se contó. Si hubiera otras, el paso 0 es más urgente,
  no menos.

---

## P48 — Del acervo de ítems viejo a la aserción de competencia, todo permisivo: migración QTI → banco → entrega certificada → evidencia xAPI → competencia en CaSS (agregado en el pase 25; **North America primero por acervo instalado, transversal por licencia**)

**Qué resuelve, en los términos en que el cliente lo pide:** *«tenemos veinte años de ítems en QTI 2.1, queremos práctica
adaptativa y queremos poder decir qué sabe cada alumno»*. Hasta el pase 24 esta KB **no podía armar esta cadena completa**:
le faltaban el banco de ítems, la migración y la pieza de aserción. **Las tres aparecieron este pase, y las tres son
permisivas.**

### Las piezas, todas verificadas de primera mano el 2026-10-01

| Rol en la cadena | Repo | Licencia | ★ | Nota decisiva |
|---|---|---|---|---|
| **Migración + banco + autoría** | https://github.com/LongsightGroup/qti3 | **MIT** ✅ | 5 | 12 paquetes, 667 commits. **Migra QTI 1.2 y QTI 2.x → autoría QTI 3** y escribe **paquete de banco de ítems**. 🚫 **No certificado**, lo dice su README |
| **Entrega al candidato** | https://github.com/amp-up-io/qti3-item-player | **MIT** ✅ | **30** | ✅ **Certificado 1EdTech: QTI 3 Basic *y* Advanced «Delivery»**. Sólo entrega — no autoría, no banco |
| **Entrada al LMS** | https://github.com/Cvmcosta/ltijs | **Apache-2.0** ✅ | **373** | Node/TS. Launches, Deep Linking, **AGS** (devolver notas), NRPS, Dynamic Registration. **La más traccionada de su capa** |
| *(alternativa por stack)* | `UOC/spring-boot-lti-advantage` (MIT, Java) · `dmitry-viskov/pylti1.3` (MIT, 138 ★, Python) · `1EdTech/lti-1-3-php-library` (Apache-2.0, 124 ★, PHP) | ✅ | — | **Elegir por el stack del cliente, no por el de esta KB** (es el sesgo que corrigió el pase 25) |
| **Telemetría** | `yetanalytics/lrsql` *(ya en la KB)* | **Apache-2.0** ✅ | — | LRS xAPI. ⚠️ **Leer antes el paso 0 de P47** si va con MariaDB/MySQL (gap 38) |
| **Minimización de telemetría** | https://github.com/yetanalytics/xapipe | **Apache-2.0** ✅ | 17 | *LRSPipe*. **Filtra por *statement template* y por *pattern* de un xAPI Profile**: decide qué sale y qué no |
| **Perfil xAPI** | https://github.com/adlnet/xapi-profiles | **Apache-2.0** ✅ | 60 | La especificación. Grupo **IEEE p9274.2.1** activo |
| **Aserción de competencia** | https://github.com/cassproject/CASS | **Apache-2.0** ✅ | **62** | Marcos + **aserciones de logro** + perfil del aprendiz. Cartuchos **IMS CASE**, **xAPI**, **Open Badges 2.0** y 🔵 **MCP** |
| **Modelo de qué sabe el alumno** | `pykt-team/pykt-toolkit` *(ya en la KB)* | **MIT** ✅ | 441 | *Knowledge tracing* profundo, para elegir el próximo ítem |

### El wiring, en cinco pasos, y sólo dos son desarrollo

1. **Migrar e inventariar (`LongsightGroup/qti3`).** Correr el paquete de migración sobre el acervo QTI 1.2/2.x y escribir el **paquete de banco de ítems**. Salida: ítems QTI 3 de autoría, con *«typed diagnostics»* — o sea, **el inventario de lo que no migró limpio es parte del entregable**, y eso es lo que se le reporta al cliente por volumen.
2. **Entregar con la pieza certificada (`amp-up-io/qti3-item-player`).** El banco alimenta al *player* certificado. ⚠️ **Esta separación es el núcleo del patrón y va escrita en la propuesta:** el sello de 1EdTech cubre **la entrega**, que es lo que el cliente audita; la autoría y el banco van con la pieza no certificada. Prometer *«todo certificado»* es falso.
3. **Montar como *tool* LTI (`ltijs`).** *Launch* OIDC desde el LMS del cliente, y **las notas vuelven por AGS** al *gradebook* — sin exportaciones manuales. Es configuración más pegamento, no desarrollo de plataforma.
4. **Drenar evidencia de proceso a xAPI, filtrada (`lrsql` + `xapipe`).** Las interacciones con el ítem salen como sentencias xAPI; **`xapipe` filtra por el *statement template* del perfil** antes de que lleguen al LRS de largo plazo. **Esto es minimización por construcción**, no una política escrita: lo que el perfil no contempla, no viaja.
5. **Asertar la competencia (`CaSS`).** El resultado del ítem se convierte en **aserción de logro** contra el marco de competencias por el cartucho **xAPI** o **IMS CASE**, y queda disponible como **Open Badges 2.0**. 🔵 **Y por el cartucho MCP, un tutor de `agents/top.md` lee el marco y escribe la aserción sin adaptador propio** (⚠️ ver la advertencia del gap 40).

**Los dos pasos que son desarrollo real son el 1 y el 5** —la limpieza del acervo migrado y el mapeo ítem→competencia—.
Los pasos 2, 3 y 4 son integración de piezas que ya hacen lo que hace falta.

### Dónde se vende primero

| Región | Gancho |
|---|---|
| **North America** | **El acervo instalado y el costo de salida del proveedor de assessment.** El estándar curricular ya está (`commonstandardsproject/api`, 50 estados; **Ed-Fi**, Apache-2.0). Cotizable **por volumen de ítems**, unidad que el cliente ya cuenta |
| **EMEA** | Como pieza de **P49**: integridad sin proctoring. Y el marco de competencias puede anclarse a la ontología de Oak (`oak-curriculum-ontology`, 50.948 *key learning points*) |
| **LATAM** | Entra por **gobernanza**: el 45 % de las instituciones de LAC con guía formal de AI (vs. 70 % en Europa y North America) necesita **resultado medible**, y la aserción de competencia es exactamente eso |
| **APAC** | ⚠️ **Con cuidado:** evaluación y aprendizaje adaptativo están alcanzados por el **AI Basic Act** coreano (vigente 2026-01-22) y por el **Annex III** europeo. Ir con el expediente de **P42** desde el día uno |

### Plazo y alcance

| | |
|---|---|
| **Piloto (un curso, un marco, sin migración)** | **4–6 semanas** |
| **Migración de acervo** | **depende del volumen**, y se cotiza por ítem: el *diagnostics* tipado del paso 1 da la curva real tras la primera tanda |
| **Cadena completa con aserción y badges** | **10–14 semanas** |

### ⚠️ Lo que este patrón NO promete

- **La certificación no cubre la cadena, cubre la entrega.** Dicho arriba, repetido acá porque es el error fácil.
- **El cartucho MCP está declarado, no medido** (**gap 40**). El paso 5 funciona igual por xAPI o IMS CASE; **lo que no se puede prometer todavía es el *«sin adaptador»***.
- **`LongsightGroup/qti3` tiene 5 ★.** La tracción es baja; lo que sostiene la elección son **667 commits y 12 paquetes publicados**, y que **es el único camino open source desde QTI viejo**. Si el cliente exige respaldo comercial, esto es un riesgo que se declara.
- **No incluye proctoring**, y es deliberado: ver **P49** y la tendencia **64**.

---

## P49 — Integridad de examen sin AI de vigilancia: sacar el entregable del Annex III en vez de buscar la pieza que no existe (agregado en el pase 25; **EMEA primero por Annex III, APAC por el AI Basic Act coreano, transversal por licencia**)

**El patrón empieza con un «no».** Cuando el cliente pide *«proctoring con AI»*, la respuesta correcta no es buscar la
pieza: **este pase barrió la capa entera y no existe ninguna opción open source permisiva y productiva** (tendencia
**64**). Y el *proctoring* es **la única función educativa que el Annex III del EU AI Act nombra explícitamente** como
alto riesgo (aplicable **2027-12-02**); Corea del Sur ya la alcanza como *high-impact AI* desde el **2026-01-22**.

### Lo que hay, y por qué ninguna sirve

| Pieza | Licencia | ★ | Por qué se descarta |
|---|---|---|---|
| `vardanagarwal/Proctoring-AI` | **MIT** ✅ | **635** | 🔴 **Pesos de uso no comercial** (*facial landmarks*), por su propio README. Código permisivo, modelo no. Y es demo de investigación |
| `openedx/edx-proctoring` | ⚠️ AGPL-3.0 | 68 | Copyleft fuerte: inviable para un SaaS multicliente |
| `oat-sa/lib-lti1p3-core` | ⚠️ GPL-2.0 | 37 | **La única certificada en *LTI 1.3 Proctoring Services*** — y copyleft |
| `sudosylabs/Proctor` | ⚠️ AGPL-3.0 | 0 | *«has not published a supported production release»* |
| `kamlendras/OpenProctor` | ⚠️ AGPL-3.0 | 15 | 37 commits, sin releases |

### El wiring de la alternativa, en cuatro pasos

1. **Variabilizar el ítem en vez de vigilar al candidato (`LongsightGroup/qti3`, MIT).** Usar el ***writer* de banco de ítems** para generar **familias de variantes** del mismo ítem y **aleatorizar por candidato**. El fraude por copia entre pares se vuelve ineficaz **sin mirar a nadie por la cámara**.
2. **Entregar con la pieza certificada (`amp-up-io/qti3-item-player`, MIT, certificada «Delivery»),** con límite de tiempo y navegación controlada por la propia especificación QTI 3.
3. **Devolver notas por AGS (`ltijs`, Apache-2.0, 373 ★)** al *gradebook* del LMS: la traza de calificación queda en el sistema de registro del cliente, no en una herramienta aparte.
4. **Evidencia de proceso en xAPI, minimizada (`lrsql` + `yetanalytics/xapipe`, los dos Apache-2.0).** Secuencia de respuestas, tiempos por ítem y revisiones — **filtrado por *statement template* del perfil**, así que **no se recoge biometría ni video**: no hay dato de categoría especial que custodiar, porque no se capturó.

### Por qué es mejor negocio que el proctoring que el cliente pidió

| | Proctoring con AI | P49 |
|---|---|---|
| **Clasificación EU AI Act** | 🔴 **Annex III, alto riesgo** (2027-12-02): expediente, evaluación de impacto, auditoría | ✅ **Fuera del Annex III** — no hay inferencia sobre la persona |
| **Dato tratado** | Rostro, mirada, voz, ambiente — **categoría especial**, y de **menores** en K-12 | Respuestas, tiempos y secuencia: dato académico |
| **Licencia disponible** | AGPL/GPL o pesos no comerciales | **MIT y Apache-2.0 de punta a punta** |
| **Lo que se discute con el cliente** | Falsos positivos, sesgo, reclamos, prensa | Diseño de la evaluación |

🔵 **El argumento de venta, en una línea:** *«no le instalamos vigilancia: le rediseñamos el examen para que la vigilancia
no sea necesaria — y le sacamos el proyecto del Anexo III de paso»*. En EMEA el ahorro es **regulatorio y cuantificable**;
en las otras regiones se vende por **licencia y por costo**.

### Plazo y alcance

| | |
|---|---|
| **Diagnóstico de integridad + diseño de variantes sobre un examen real** | **2–3 semanas** |
| **Implementación completa (banco variabilizado + entrega + AGS + xAPI filtrado)** | **8–10 semanas** |
| **Encadenado con P48** | Comparte los pasos 1-4: si el cliente ya va a P48, **P49 es incremental** |

### ⚠️ Lo que este patrón NO promete

- **No elimina el fraude, cambia su economía.** Un candidato con ayuda externa presencial no es detectado. **Lo que elimina es la copia escalable** — y eso hay que decirlo, porque un cliente que necesite certificación de alto riesgo (habilitaciones profesionales, exámenes de estado) **probablemente siga necesitando proctoring supervisado**, y entonces la respuesta honesta es un proveedor comercial cerrado, no open source.
- **La aleatorización por variantes no está medida en esta KB.** Que `LongsightGroup/qti3` escriba paquetes de banco de ítems está **verificado**; que su *writer* soporte el patrón de familias de variantes que pide el paso 1 **está inferido de la descripción de los paquetes**, no probado. **Es el gap 39.**
- **La equivalencia psicométrica entre variantes es trabajo propio** y no lo cubre ninguna pieza de esta tabla: si las variantes no son de dificultad equivalente, la nota deja de ser comparable. Para un examen de consecuencia alta, eso requiere análisis de ítems que esta cadena no incluye.

## P50 — Perfil de competencia por MCP, con las tools medidas (pase 26)

**Problema que resuelve.** Un cliente con un acervo de cursos quiere responder, por alumno, *«¿qué sabe esta persona?»*
— no *«¿qué cursos aprobó?»*. Es la pregunta que paga un proyecto de competencias, y hasta el pase 25 esta KB la
describía sin tener con qué ejecutarla: la capa CASE hospeda marcos y **no registra logro**.

**Qué cambia respecto de P48.** P48 tenía el paso 4 **inferido de una línea de README**. **Este pase lo midió:** el
cartucho MCP de CaSS genera **6 tools y 3 resource templates** (51 paths en el spec, 0 errores de validación), y dos de
ellas son exactamente los extremos de la cadena. **P50 es P48 con el paso 4 verificado y cotizable.**

**Piezas, todas verificadas y todas permisivas:**

| Pieza | Licencia | Rol |
|------|----------|-----|
| `cassproject/CASS` | **Apache-2.0** ✅ | Marcos de competencia + **aserciones de logro** + cómputo de perfil. **Expone MCP en `/api/mcp`** |
| `DavidLMS/learnmcp-xapi` | **MIT** ✅ | Puente MCP hacia el LRS: registra statements y consulta progreso |
| `yetanalytics/lrsql` | **Apache-2.0** ✅ | El LRS de almacenamiento (xAPI 2.0 / IEEE 9274.1.1) |
| `vishalsachdev/canvas-mcp` | **MIT** ✅ | Si el cliente es Canvas: trae la actividad real (entregas, notas, módulos) |

**Wiring, con los nombres de tool medidos:**

```
Actividad del alumno (Canvas vía canvas-mcp  |  o el LMS del cliente)
        │
        ▼
  [Agente orquestador]  ── record_evidence ──▶  CaSS   POST /api/xapi/statement
        │                  (xAPI statement: actor + verb + competencia)
        │
        ├── learnmcp-xapi ─▶ lrsql        (historial crudo, consulta de progreso)
        │
        ▼
  get_learner_profile ──▶ CaSS   GET /api/profile/latest
        (frameworkId, subject, targetDateTime)  ──▶  perfil de competencia computado
```

**Las dos llamadas que cierran el patrón, con su firma real:**

- `record_evidence` → `POST /api/xapi/statement`, requiere `body`. `readOnlyHint: false`.
- `get_learner_profile` → `GET /api/profile/latest`, parámetros `frameworkId`, `subject`, `flushCache`, `cache`,
  `targetDateTime`. `readOnlyHint: true`, `idempotentHint: true` → **se puede cachear y reintentar sin efectos**.

**`targetDateTime` es el parámetro que hay que vender.** Permite preguntar *«¿qué sabía esta persona en tal fecha?»* —
es decir, **el perfil es histórico, no sólo actual**. Eso habilita el entregable que un área de RRHH o una acreditadora
pide y que casi ningún producto da: *la evolución de la competencia en el tiempo*, con evidencia trazable detrás.

🔴 **Las dos restricciones de cotización, y no son menores:**

1. **Por MCP se escribe un statement por llamada.** `POST /api/xapi/statements` (el *bulk*) está **`x-mcp-ignore`**, como
   otros 44 paths. **No cotizar ingestión masiva de telemetría por esta puerta**: para lotes, API REST por fuera de MCP.
   Ver el **gap 41**.
2. **El *handshake* MCP real no está medido.** Se midió la **generación** de las tools (determinista, y confirmada por
   tres fuentes independientes), no su **invocación**: eso necesita Elasticsearch. **Antes de firmar, hacer
   `initialize` + `tools/list` contra `/api/mcp`** — es la acción 1 del pase 27. Estimación: una tarde con Docker.

**Estimación.** 3–4 semanas para el circuito completo sobre un marco de competencias existente, asumiendo que el LMS ya
expone la actividad. El riesgo no es técnico: es **tener el marco de competencias del cliente en CASE**, que suele ser
el trabajo de verdad.

## P51 — ~~El conector MCP de Moodle que no existe, construido sobre el que sí existe~~ 🔴 **PREMISA FALSA — CORREGIDO EN EL PASE 27** (pase 26)

> 🔴 **Este patrón se construyó sobre una afirmación falsa y queda reemplazado por P54 y P55.** El pase 26 declaró que *«el único conector MCP de Moodle es `csmediapro/moodle-mcp-server`, AGPL-3.0, 10 tools sólo de lectura»*. **Existen al menos tres, y dos son MIT:** `peancor/moodle-mcp-server` (**MIT**, 43 ★, 13 forks, **8 tools, cuatro de escritura**, incluidas `provide_assignment_feedback` y `provide_quiz_feedback`) y `MarcosNahuel/moodle-mcp` (**MIT**, 59 commits, **40 tools** en 10 dominios **+ `ws_raw`**). El error fue de **muestreo** —los directorios de MCP rankean por promoción, **gap 49**—, no de lectura: lo que el pase 26 dijo de `csmediapro` es correcto.
>
> **Qué hacer en su lugar:** para Moodle, **no hay que construir el conector — hay que endurecer y componer los dos que existen**, que es un proyecto mucho más corto: ver **P54** (corrección y devolución con compuerta humana). La ausencia real del eje conector **está en Open edX** (**gap 48**): ver **P55**.
>
> **Lo que de este patrón sigue siendo válido y por eso se conserva entero abajo:** la tabla de decisiones de diseño de `canvas-mcp` —descubrimiento de tools, separación de perfiles, *agent skills*, chequeo WCAG— **es exactamente lo que hay que portar**, y ahora se porta a Open edX en vez de a Moodle. ⚠️ Con una salvedad de cifra: el conteo de tools de `canvas-mcp` **varía por versión** (40+, 80+, 116) y **no es citable como número fijo**; «102–103» era la lectura del README en el pase 26.

**El hueco, medido.** `canvas-mcp` (**MIT**, 269 ★, 815 commits) da **hasta 102–103 tools** sobre Canvas, con lado
alumno y lado docente. **Para Moodle —el LMS más instalado del planeta— el único conector MCP es `csmediapro/moodle-mcp-server`:
AGPL-3.0, 0 ★, 0 forks, 10 tools sólo de lectura, y las capas útiles (*Reporting*, *Analytics*, *Directory*,
*Compliance*) son plugins premium que se venden aparte.** Ver el **gap 43**.

**Por qué es patrón y no sólo oportunidad: `canvas-mcp` ya resolvió los problemas de diseño.** No hay que inventar la
arquitectura, hay que portarla:

| Decisión de diseño de `canvas-mcp` | Por qué importa al portarla a Moodle |
|-----------------------------------|--------------------------------------|
| **`search_canvas_tools`** — descubrimiento de tools | Con 100+ tools **no se puede volcar el catálogo al contexto**. El agente busca la herramienta. Moodle Web Services tiene **cientos** de funciones: sin esto, el conector es inusable |
| **Separación alumno / docente / *learning designer*** | Son tres perfiles con permisos distintos. Moodle tiene *capabilities* por rol: el mapeo es directo |
| **8 *agent skills* además de las tools** | Las tareas compuestas (corregir una tanda, armar un módulo) no son una tool: son un procedimiento |
| ***Learning Designer*** con **chequeo WCAG** | Conecta con la capa de accesibilidad del pase 8 y con el **EAA** (vigente 2025-06-28). Es el diferenciador regulatorio en EMEA |

**Wiring:**

```
[Agente]  ──MCP──▶  moodle-mcp (a construir, licencia a elegir)
                        │
                        ▼
                Moodle Web Services (REST/token)   ◀── sin modificar el LMS
                        │
                        ├── core_course_*, core_enrol_*, mod_assign_*, gradereport_*
                        └── capabilities por rol → perfiles alumno / docente

  Opcional, y es el combo que esta KB recomienda:
  [Agente] ──MCP──▶ learnmcp-xapi ──▶ lrsql     (telemetría conforme al estándar)
  [Agente] ──MCP──▶ CaSS                        (competencia, P50)
```

⚠️ **La decisión de licencia hay que tomarla a conciencia, y es la trampa del patrón.** **El core de Moodle es GPL-3.0**,
pero **un conector que habla con Moodle Web Services por HTTP no es obra derivada de Moodle**: es un cliente de su API.
**Se puede licenciar permisivo.** Lo que **no** se puede es forkear `moodle-mcp-server` (AGPL-3.0) y relicenciar. **El
camino limpio es construir desde cero contra la API documentada**, tomando de `canvas-mcp` (MIT) las decisiones de
diseño —que es legítimo— y no su código si no se respeta el MIT (que es trivial de respetar: atribución).

**Estimación.** 4–6 semanas para un conector de ~30 tools útiles con descubrimiento. **El valor no está en el número de
tools: está en `search_canvas_tools`** — sin descubrimiento, un conector de Moodle es un catálogo que no entra en el
contexto.

## P52 — La capa agéntica de biblioteca sobre el bus de eventos que ya está puesto (pase 26)

**La vertical que esta KB abrió en el pase 26 y que no tiene ni una pieza agéntica.** Y es la más fácil de todas las que
inventarió esta base, por un motivo concreto: **FOLIO ya publica los eventos.**

| Pieza | Licencia | Rol |
|------|----------|-----|
| `folio-org/platform-complete` | **Apache-2.0** ✅ | Ensamblado de la plataforma: fija el conjunto compatible de releases + infra Docker |
| `folio-org/mod-inventory` | **Apache-2.0** ✅ | *Instances* / *holdings* / *items*, **import por Kafka**, **MARC**, *authority linking*, **multi-tenant** |
| `DavidLMS/learnmcp-xapi` + `lrsql` | **MIT** / **Apache-2.0** ✅ | Si se quiere registrar el uso como evidencia de aprendizaje |

**Wiring — y el punto es que no se parchea nada:**

```
FOLIO (Apache-2.0, multi-tenant)
   │
   ├── mod-inventory ──Kafka──▶  [consumidor agéntico]   ◀── NO se parchea el core
   │                                   │
   │                                   ├─ recomendación por curso/competencia
   │                                   ├─ enriquecimiento de catálogo (MARC → lenguaje natural)
   │                                   └─ descubrimiento conversacional sobre el OPAC
   │
   └── API HTTP por tenant ──▶ lectura de holdings/items
                                        │
                     opcional ──────────▼
                        learnmcp-xapi ──▶ lrsql  (el préstamo como statement xAPI)
```

**Por qué el modelo de despliegue de FOLIO es la mitad del valor.** Es **modular y multi-tenant por diseño**: el módulo
agéntico se despliega **al lado**, consume Kafka y expone su propia API, **sin tocar el core y sin bloquear upgrades**.
Es la diferencia con Koha (**GPL-3.0+**, Perl, monolítico), donde la capa AI va necesariamente por fuera contra la
interfaz y hay que leer la GPL antes de tocar algo.

⚠️ **La advertencia de lectura que hay que poner en la propuesta.** `platform-complete` tiene **15 ★** y `mod-inventory`
**4 ★**. **No aplicar el umbral de estrellas:** son 3.096 y 2.402 commits, 27 y 15 forks, y un consorcio de bibliotecas
universitarias detrás. **Para software de consorcio las estrellas miden moda; los commits y las implantaciones miden
vida.** Mismo patrón que Apereo y `UniTime`.

**Regla de decisión.** Cliente **con Koha** → capa AI por fuera, GPL leída. Cliente **eligiendo o migrando** → **FOLIO**,
por la licencia **y** por el bus. **Estimación:** 3 semanas para el consumidor de Kafka + descubrimiento conversacional
sobre un tenant de prueba. Ver el **gap 45**.

## P53 — *Early warning* con humano decidiendo: el único envoltorio facturable de la capa predictiva (pase 26)

**El problema de forma, y es el patrón más importante de este pase.** La capa de *student success* open source es de
**2013–2014**, es **GPL**, y no vive en GitHub (**gap 47**). Y es **la que más presión regulatoria tiene encima**: el
**Annex III** del EU AI Act la clasifica de alto riesgo, **Oklahoma y Maryland prohíben la decisión autónoma sobre el
alumno**, **Delaware y Nueva York** prohíben el IEP automatizado, y **Colorado y Texas** agregaron requisitos. **Seis
estados y un reglamento europeo sobre una capa cuyo software libre tiene doce años.**

🔴 **La trampa que este patrón evita, dicha sin suavizar.** *La misma pieza técnica tiene dos envoltorios, y sólo uno se
puede facturar.* Un modelo que predice riesgo de abandono y **dispara una acción** —baja de curso, reasignación, alerta
automática al tutor con recomendación— **es ilegal en dos estados y de alto riesgo en EMEA**. El mismo modelo que
**ordena una cola de revisión humana** no cae en la prohibición de decisión autónoma. **No es un matiz de redacción: es
la diferencia entre un entregable y un pasivo.**

**Piezas (y hay que decir que la de modelado es permisiva y la de producto no existe):**

| Pieza | Licencia | Rol |
|------|----------|-----|
| `pykt-team/pykt-toolkit` / `pyBKT` | **MIT** ✅ | El modelado del alumno. **Permisivo** — pero ⚠️ **verificar la licencia de los *datasets*** (casi todos **CC BY-NC**, ver gap 11) |
| `lrsql` + `learnmcp-xapi` | **Apache-2.0** / **MIT** ✅ | La telemetría conforme al estándar que alimenta el modelo |
| Capa de producto (*early alert*, cola, expediente) | 🔴 **no existe permisiva** | **FlightPath** es GPLv3+ de 2013 y sin repo en GitHub. **Esto es el desarrollo** |

**Wiring — y el recuadro del medio es el patrón:**

```
LMS / SIS  ──▶  lrsql (xAPI)  ──▶  pyKT / pyBKT   ──▶  score de riesgo
                                                            │
                                   ┌────────────────────────▼─────────────────────────┐
                                   │  COLA DE REVISIÓN HUMANA                         │
                                   │  · ordena por riesgo, NO actúa                   │
                                   │  · muestra los features que pesaron              │
                                   │  · exige decisión de un tutor identificado       │
                                   │  · escribe expediente: quién, cuándo, por qué    │
                                   └────────────────────────┬─────────────────────────┘
                                                            ▼
                                            intervención (humana) + statement xAPI
```

**Las cuatro propiedades que hacen al entregable defendible en las cuatro regiones**, y conviene listarlas así en la
propuesta: **(1)** el sistema **ordena**, no decide; **(2)** la decisión la toma **una persona identificada**;
**(3)** el alumno puede saber **qué features pesaron** (explicabilidad, que es lo que el Annex III pide);
**(4)** queda **expediente** de quién decidió qué y cuándo — que es lo que convierte una inspección en un trámite.

**Y el argumento de venta que viene del usuario final, no del regulador:** el pase 23 midió que **65 % de los alumnos
en LATAM teme el aprendizaje superficial**. Un sistema que explícitamente pone un humano a decidir sobre su caso **es
también el argumento pedagógico**, no sólo el de cumplimiento. **En LATAM esto se vende por pedagogía defendible; en
EMEA y North America, por cumplimiento.** Mismo entregable, dos relatos.

**Estimación.** 6–8 semanas: 2 de modelado sobre datos del cliente (con la licencia de los datasets verificada) y 4–6
de la capa de cola + expediente, **que es la que no existe y es la que se factura**. Ver el **gap 47** y la tendencia **68**.


## P54 — Asistente de corrección sobre Moodle con compuerta humana: el último tramo del gap 6, con piezas MIT que ya escriben (pase 27)

**Por qué este patrón existe recién ahora.** El **gap 6** —corrección y devolución— lleva abierto desde el pase 2 con
el mismo diagnóstico: la demanda está probada (Singapur construyó tres asistentes de devolución, cerrados) y la oferta
open source **analizaba sin escribir**. El resultado del análisis **no volvía al expediente del alumno**, y ese último
tramo se cotizaba como desarrollo. **El pase 27 encontró la pieza que lo cierra**, y es MIT.

**Las piezas, todas verificadas:**

| Pieza | Licencia | Rol |
|---|---|---|
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** ✅ | **El que escribe.** `get_student_submissions` → `provide_assignment_feedback` / `provide_quiz_feedback` |
| [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) | **MIT** ✅ | **El que cubre el resto**: 40 tools (gradebook, grupos, calendario) **+ `ws_raw`** para lo que falte |
| **Moodle** | GPL-3.0+ | El LMS, **sin modificar** — todo entra por Web Services con token |
| `MathTutorBench` / `pedagogy-benchmark` | MIT | **El *eval* pedagógico**, para medir la calidad de la devolución (gap 1, P10) |
| `learnmcp-xapi` + **lrsql** | permisivas | **La evidencia append-only** de cada devolución escrita |

**Wiring, y la compuerta es el punto del patrón:**

```
[Docente] ──── revisa y firma ────┐
                                  │  (nada se escribe sin este paso)
[Agente] ──MCP──▶ moodle-mcp-server ──▶ Moodle Web Services ──▶ nota + comentario
   │                                         (LMS sin modificar)
   ├──MCP──▶ moodle-mcp (40 tools) ──▶ gradebook / grupos / calendario
   ├──▶ eval pedagógico (MathTutorBench) ──▶ puntaje de la devolución, antes de mostrarla
   └──MCP──▶ learnmcp-xapi ──▶ lrsql  ──▶ statement por cada escritura (quién, qué, cuándo)
```

🔴 **La razón regulatoria por la que la compuerta no es opcional ni es un detalle de UX.** **Oklahoma y Maryland
prohíben que la AI tome decisiones de alto impacto sobre un alumno**, y una nota lo es. El patrón **no es «la AI
corrige»**: es **«la AI instruye el expediente y la persona firma»** —exactamente el encuadre que el bloque de North
America viene sosteniendo— y el `provide_*_feedback` es **el punto donde se inserta la firma**. En **North America**
eso lo hace vendible; en **APAC** la compuerta **ya es política pública** (plataforma estatal + supervisión docente), así
que no hay que argumentarla, hay que instrumentarla.

**Estimación: 4–6 semanas.** ⚠️ **Lo que hay que decirle al cliente sin maquillar:** `peancor/moodle-mcp-server` tiene
**10 commits** y 8 tools — **es el punto de partida del último tramo, no un sistema de corrección**. El trabajo real
del proyecto es la compuerta, el *eval* y la evidencia; el conector se endurece, no se adopta tal cual.

## P55 — El conector MCP de Open edX (pase 27) — 🔴 **PREMISA MUERTA EN EL PASE 30: la puerta existe, es oficial y es AGPL-3.0**

> 🔴 **Leer esto antes del patrón.** Este patrón se escribió sobre una ausencia —*«Open edX es el único LMS grande sin conector MCP»*— y esa ausencia **ya no existe**. El **2026-07-25** el propio proyecto publicó **`openedx-mcp`** y **`tutor-contrib-openedxmcp`** en PyPI, los dos **AGPL-3.0**, con **35 endpoints** (28 LMS + 7 CMS, **autoría incluida**) y con **cuatro rails de seguridad de escritura** que ningún conector de esta KB tenía. **Esta KB no lo notó durante dos meses: ver el gap 54.**
>
> **Lo que de este patrón sigue vivo, y es bastante:**
>
> - ✅ **Todo el mapa de la superficie REST versionada** (`v0`–`v4`, notas en tres versiones, assets y transcripciones sólo en `v0`) **sigue siendo válido y sigue siendo el único camino para un conector permisivo**, porque la puerta oficial es AGPL **y corre en proceso**. Si el cliente necesita una puerta **permisiva y fuera de proceso**, este patrón es la receta y el mapa del pase 29 es el plano.
> - ✅ **La refutación del pase 29 quedó confirmada por implementación:** la autoría **no** estaba bloqueada, y el proyecto la implementó (`blocks/create`, 🔵 **`blocks/create-tree`**, `update`, `publish`, `delete`).
> - 🔵 **Y lo que el proyecto enseñó gratis:** corriendo **adentro** del LMS y del CMS **no se paga la rotación de versiones** que este patrón cotizaba como riesgo de adaptador. **Capacidad y copyleft son la misma decisión** (tendencia **82**).
>
> **Lo que reemplaza a este patrón para un cliente que corre Open edX: no vender el conector.** Vender **criterio** (qué scopes se habilitan — `grant:admin` y `destructive` son separables), **endurecimiento** (el backend de caché compartido que los rails necesitan en producción), **operación** y **la capa pedagógica arriba**. Ver **P61**. ⚠️ **Y si el cliente ofrece la plataforma como servicio a terceros con modificaciones propias, el artículo 13 del AGPL alcanza a la obra combinada: el análisis legal es obligatorio, no opcional.**


**Reemplaza a P51**, cuyo premisa era falsa (ver la corrección al final de este archivo). **Acá la ausencia está
medida y es real:** búsqueda en modo extendido, **ningún conector MCP para Open edX** (**gap 48**).

**Por qué es el patrón de mayor valor comercial de esta KB en este momento:**

1. **Es el LMS de la huella pública grande** — los programas nacionales de **LATAM e India** corren sobre Open edX.
2. **Es la región de menor presupuesto.** En LATAM, **8 % de instituciones tiene presupuesto dedicado a AI** y
   **73,5 % ya enseña con AI**: el entregable tiene que correr **sobre lo que ya está pagado**, y eso es Open edX.
3. **La arquitectura está resuelta dos veces** (Canvas y Moodle): no hay que diseñar, hay que portar.
4. **El cliente ya llega con telemetría impuesta:** si corre Open edX con analítica, corre **Aspects → Ralph sobre
   ClickHouse sin haberlo elegido** (pase 22). El conector es la puerta que falta sobre un stack ya decidido.

**La decisión de diseño a portar, que es lo que hace esto barato — de `MarcosNahuel/moodle-mcp`:**

| Decisión | Por qué importa en Open edX |
|---|---|
| **Fachadas de alto nivel, no un tool por endpoint** | 40 tools en 10 dominios en vez de cientos. Un catálogo volcado **no cabe en el contexto** y vuelve el conector inusable |
| **`ws_raw` como escape hatch** | Lo que la fachada no cubra sigue alcanzable **sin esperar una release**. Es la válvula que evita el bloqueo |
| **Descubrimiento de tools** (`search_canvas_tools` en `canvas-mcp`) | Con catálogo grande, el agente **busca** la herramienta |
| **Separación alumno / docente / diseñador** | Open edX tiene roles por curso: el mapeo es directo |

**Wiring:**

```
[Agente] ──MCP──▶ openedx-mcp (A CONSTRUIR — licencia a elegir, MIT recomendada)
                       │
                       ▼
        APIs REST de Open edX  ◀── sin parchear la plataforma
        (Course Blocks · Enrollment · Grades · Studio/CMS)
                       │
                       ▼
        Aspects / Ralph / ClickHouse  ◀── la analítica que el cliente ya tiene
```

### ✅ La medición se hizo en el pase 28, y el patrón queda **partido en dos cotizaciones**

Se leyeron los `urls.py` del árbol `master` por `raw.githubusercontent.com` (la documentación oficial está bloqueada
por el proxy). **La respuesta no fue «sí» ni «no»: fue un corte por la mitad de la plataforma**, y cambia cómo se
vende este patrón.

| Tramo | Superficie medida | Veredicto |
|---|---|---|
| **Operación** (matrícula, roles) | `enrollment`, `enrollment/{username},{course_key}`, `enrollments/`, **`unenroll/`**, `roles/`, **`enrollment_allowed/`** | ✅ **Escribe.** Cotizable |
| **Consumo** (estructura de curso) | `v1/blocks/`, `v1/block_metadata/{usage_key}` **y los tres equivalentes en `v2/`** | ✅ **Versionado en dos versiones.** Cotizable |
| **Evaluación** (notas) | **`gradebook/{course_id}/bulk-update`** (`GradebookBulkUpdateView`), **`subsection/{subsection_id}/`** (*course_grade_overrides*), `gradebook/{course_id}/`, `policy/courses/{course_id}/`, `submission_history/{course_id}/` | ✅ **Escribe, y POR LOTE** |
| 🔴 **Autoría** (crear curso/contenido) | `xblock/`, `container/{usage_key}/children`, `course_settings/…`, `course_rerun/…` (21 rutas, `v1`) | 🔴 **El repo declara «the Authoring API is still experimental» y recomienda `v0`** |

🔵 **El dato que mejora la propuesta respecto de lo que el pase 27 suponía: Open edX escribe notas por lote, y el
conector MIT de Moodle no tiene lote** (`provide_assignment_feedback` es de a una). **En la capacidad que más importa
para el gap 6, la plataforma sin puerta es más capaz que la que ya tiene dos.** Eso vuelve a este conector el camino
más corto a un asistente de corrección a escala — ver **P54**, que es su compuerta humana.

**Cómo se cotiza, entonces:**

- ✅ **Conector de operación y evaluación: 6–8 semanas**, sobre superficie versionada y con escritura verificada en el
  código. **Es el tramo que paga**, porque toca la nota y la matrícula.
- ✅ **Autoría de curso: el pase 29 la desbloquea, y corrige este mismo patrón.** 🔴 **Lo que decía acá —que había que
  apoyarse en «la única parte que el mantenedor marca inestable»— es falso, y el error fue haber leído un archivo
  donde hacían falta dos.** El aviso de «experimental» está en `v1/urls.py`, **fechado «(Nov. 23)», encabezando una
  sección sin ninguna ruta**; `v0/views/xblock.py` declara lo contrario (**`v0` es el deprecado**, *«use
  `/api/contentstore/v1/xblock/` going forward»*, con `DeprecationWarning` en sus 5 vistas), y **`v1/urls.py` registra
  `XblockViewSet`** con **CRUD completo** (`create`/`retrieve`/`update`/`partial_update`/`destroy`) bajo los ADRs de
  **FC-0118**. 🔵 **Y trae un regalo para un agente: `?view=minimal` (ADR 0036)** recorta la respuesta en árbol a
  campos estructurales — el problema de ventana de contexto más caro de este tramo **ya está resuelto por la
  plataforma**. **Cotización: autoría 4–6 semanas adicionales**, sobre `xblock` en `v1` más assets, video y
  transcripciones en `v0`. **El gap 50 queda reencuadrado, no cerrado:** lo que falta no es estabilidad, es
  **adaptador de versión** — ver abajo.

- ⚠️ **La línea nueva de alcance que este pase obliga a cotizar aparte: resolución de versión.** La API de Studio monta
  **cinco versiones a la vez** (`v0`–`v4`), y **las notas viven en tres** (`grading/` en `v0`, `course_grading/` en
  `v1`, `authoring_grading` en `v3`) mientras **assets, video y transcripciones existen sólo en `v0`**. **No hay una
  "API de Studio" contra la que programar: hay cinco superficies solapadas.** Se cotiza **1–2 semanas** de capa de
  resolución de versión, y se dice en la propuesta, porque es la diferencia entre alcance declarado y sorpresa de la
  semana cuatro. 🔵 **Bonus que aparece en `v2` y que conviene ofrecer: `SyncFromUpstreamView`** (`downstreams`)
  propaga una corrección de biblioteca a todos los cursos que la heredan — **es el multiplicador de un agente que
  corrige una vez**. Ver las tendencias **78** y **79**.

⚠️ **La licencia no es el obstáculo, y conviene decirlo primero porque es la primera pregunta del cliente.** Open edX
es **AGPL-3.0**, pero **un conector que habla REST desde otro proceso no deriva de la plataforma y no hereda la
AGPL** — es la configuración ya verificada dos veces en esta KB: `canvas-mcp` (MIT) contra Canvas y los dos
`moodle-mcp` (MIT) contra Moodle, que es **GPL-3.0**.

🔴 **Lo que sigue sin medir, y hay que decirlo en la propuesta:** **no se hizo ninguna llamada HTTP contra una
instancia.** La superficie está **declarada en el código**, no observada. **OAuth2, *scopes*, *rate limits* y forma de
las respuestas no están verificados**, y eso es riesgo de estimación, no de viabilidad.

⚠️ **Nota de nomenclatura:** el repo es **`openedx/openedx-platform`**; `openedx/edx-platform` es el nombre viejo y
**redirige**. Las dos URLs resuelven.

## P56 — SCORM como formato de salida de la capa generativa: aterrizar en el LMS que el cliente ya tiene, sin integrarse con él (pase 27)

**El problema que resuelve, y es el más común de todos.** Esta KB tiene una capa generativa fuerte —**OpenMAIC** (MIT,
tema → clase interactiva multi-agente), **Educhain** (MIT, YouTube → curso)— y un cliente que dice *«muy bien, y cómo
entra esto a mi LMS»*. La respuesta por integración es un conector por plataforma. **La respuesta por formato es un
paquete que cualquier LMS importa desde hace veinte años.**

| Pieza | Licencia | Rol |
|---|---|---|
| **OpenMAIC** / **Educhain** | MIT ✅ | Generan el contenido |
| [`giacomomaria81/scorm-mcp-server`](https://github.com/giacomomaria81/scorm-mcp-server) | **MIT** ✅ | `scorm_package` (HTML → SCORM **2004 4.ª ed.** o **1.2**), `scorm_validate`, `scorm_selftest` |
| **Moodle · Open edX · Canvas · cualquier LMS** | — | **Importan SCORM sin desarrollo** |

**Wiring:**

```
[tema / PDF / video]
      │
      ▼
OpenMAIC · Educhain ──▶ HTML del módulo
      │
      ▼
scorm_package  ──▶  .zip SCORM (assets inlineados como data URI → 100 % offline,
      │               runtime que reporta completion, progreso, tiempo y resume)
      ▼
scorm_validate ──▶  conformidad verificada ANTES de entregar
      │
      ▼
[LMS del cliente]  ◀── importación estándar, cero integración
```

**Las tres razones por las que este patrón gana más seguido de lo que parece:**

1. **Cero integración, cero permisos.** No hay token de API, no hay plugin, no hay revisión de seguridad del LMS. Es el
   camino más corto del laboratorio al aula.
2. 🔴 **El `resume` y el reporte de progreso vienen puestos.** El paquete reporta *completion*, progreso y tiempo — es
   decir **produce la telemetría mínima** sin que haya que montar un LRS en la primera etapa.
3. **Offline de verdad.** Al inlinear cada asset como data URI, el módulo corre sin red. Conecta directo con
   **Project NOMAD** (Apache-2.0, servidor de conocimiento offline) y con los despliegues de baja conectividad — que es
   buena parte de la huella educativa pública de **LATAM** y **APAC**.

**Estimación: 2–3 semanas** para el primer módulo validado de punta a punta. ⚠️ **El límite a declarar:** SCORM
**no lleva la conversación de vuelta** — es contenido empaquetado, no un tutor en vivo. Para interacción con el alumno
hace falta el conector del LMS (**P54**, **P55**) o xAPI. **SCORM es la vía de entrada, no el destino.**

## P57 — Evidencia de competencia por MCP, cotizada sobre la superficie que CaSS realmente expone (pase 27)

**Refina P50** con la medición por adaptador del pase 27, que es lo que separa una propuesta cotizable de una promesa.

**Lo que SÍ entra por MCP en `cassproject/CASS`** (Apache-2.0, medido por anotación, **2 canales**):

| Tool | Operación | Uso |
|---|---|---|
| `get_learner_profile` | `GET /api/profile/latest` | Leer el perfil de competencia computado |
| **`record_evidence`** | `POST /api/xapi/statement` | **Escribir evidencia — un statement por llamada** |
| `search_data` · `get_object` · `save_object` | CRUD JSON-LD | Marcos y objetos |
| `server_status` | `GET /api/ping` | Salud |

🔴 **Lo que NO entra, y hay que decirlo en la propuesta porque está excluido a propósito:**

| Capa | Operaciones ocultas | Consecuencia de cotización |
|---|---|---|
| **CASE** (`caseAdapter` + `caseIngest`) | **13** | **Autoría de marcos de competencia: por REST, fuera de MCP** |
| **CEASN** | 6 | Fuera de MCP |
| **Open Badges** | **5** | 🔴 **Emisión de insignias: fuera de MCP.** Y el adaptador es **OB 2.0** (`w3id.org/openbadges/v2`), **no 3.0** |
| **Bulk xAPI** (`POST /api/xapi/statements`) | — | 🔴 **Ingestión masiva de telemetría NO entra por MCP.** Un statement por llamada |

**Las frases que se pueden decir y las que no.** ✅ *«El perfil de competencia se lee por MCP»*, *«la evidencia se
registra por MCP, de a un statement»*. 🔴 *«Emitimos insignias por MCP»*, *«autoramos el marco por MCP»*, *«ingestamos
la telemetría histórica por MCP»* — **las tres son falsas**. Y si el cliente pide **OB 3.0 / W3C VC**, **CaSS no es la
pieza que las emite.**

**Checklist de despliegue — y el primer ítem es el que hace fallar esto en silencio:**

1. 🔴 **Verificar `CASS_LOOPBACK` antes que nada.** El adaptador pide el spec por loopback
   (`fetch(CASS_LOOPBACK + '/swagger.json')`, default `http://localhost/api/`, **puerto 80**). Si ese `fetch` falla,
   **hace `return` y la ruta `/api/mcp` no se monta — con el servidor arrancando normalmente.** El síntoma es *«no veo
   herramientas»*, no *«no arranca»*. Con proxy, puerto no estándar o HTTPS mal resuelto, **la superficie de agente
   desaparece sin error visible**.
2. Verificar que `DISABLED_ADAPTERS` **no** contenga `mcp`.
3. Elasticsearch en `:9200` — el *probe* sólo pide `GET /` y salud **`yellow`/`green`**.
4. `initialize` + `tools/list` contra **`POST /api/mcp`** y **comparar con las 6 declaradas**.

⚠️ **El asterisco que este patrón todavía lleva, dicho con precisión:** las 6 tools están confirmadas **por
declaración en el código, por dos métodos independientes** (ejecución del generador en el pase 26, conteo estático de
anotaciones en el pase 27) — **no por invocación**. Nadie hizo el `tools/list` real. **Alcanza para cotizar el catálogo
y el alcance; no alcanza para prometer latencia, forma de respuesta ni comportamiento de sesión.** Ver el **gap 40**.

## P58 — Agente de rostering y matrícula sobre OneRoster, con la puerta que ya existe y nadie publicitó (pase 28)

**El patrón que este pase habilita sin construir nada**, y el más barato de arrancar de toda esta KB: la puerta ya
está escrita, es **0BSD**, y cubre el estándar entero.

**La pieza, verificada de primera mano:** [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts)
— **0BSD**, 10 ★, 3 forks, 39 commits, TypeScript. **Declara 164 métodos sobre 21 recursos OneRoster expuestos como
MCP tools**, con **lectura y escritura** (`createUser`, `updateClass`, `deleteEnrollment`, `postAcademicSession`),
sobre **OneRoster v1p2**, con paginación por offset y el `filter` de 1EdTech.

**Por qué vale más que un conector de LMS puntual:** OneRoster **no es una plataforma, es el estándar de intercambio de
listas** —alumnos, docentes, clases, matrículas, resultados— que el SIS le pasa al LMS. **Un agente que habla OneRoster
no está atado al LMS del cliente**: funciona contra cualquier stack que implemente el estándar, que es el caso del
distrito escolar típico de **North America** y de los despliegues que ya pasaron por integración de rostering.

**Wiring:**

```
[Agente]
   │
   ├──MCP──▶ oneroster-ts  (0BSD, 164 métodos, LECTURA Y ESCRITURA)
   │              │
   │              ▼
   │        SIS / LMS que implementa OneRoster v1p2
   │        (users · classes · enrollments · results · lineItems · orgs)
   │
   ├──MCP──▶ moodle-mcp-server (MIT)   ◀── si el LMS es Moodle: la nota y la devolución
   │
   └──MCP──▶ learnmcp-xapi (MIT) ──▶ lrsql  ◀── evidencia de lo que el agente hizo
```

**Los tres entregables que esto cotiza, en orden de menor a mayor riesgo:**

| # | Entregable | Por qué es de bajo riesgo |
|---|---|---|
| 1 | **Auditoría de rostering** (lectura): detectar matrículas huérfanas, clases sin docente, duplicados de usuario | **Sólo lee.** Es el *quick win* de semana uno y no toca datos |
| 2 | **Altas y bajas asistidas con compuerta humana**: el agente propone el lote, una persona confirma | La escritura existe (`createUser`, `deleteEnrollment`) y **la compuerta es el requisito del Annex III** (ver **P49**, **P54**) |
| 3 | **Reconciliación SIS ↔ LMS continua** | Es el que más paga y el que más hay que medir antes |

🔴 **Las tres cautelas, y son serias:**

- ✅ **«Declara 164» pasó a «164 contados» en el pase 29, por dos canales independientes del propio repo:** el conteo
  directo del índice de métodos generado devuelve **exactamente 164 entradas en 21 grupos de recurso** (los 21 que este
  patrón ya citaba, ahora confirmados por conteo), y la tabla de errores generada —independiente del índice— repite
  *«Applicable to **131 of 164 methods**»* para `400`, `401` y `403`. ⚠️ **Pero la distinción que esta KB aprendió con
  CaSS sigue en pie: 164 es el conteo de métodos del SDK, no de tools observadas en `tools/list`** (CaSS: 61
  operaciones, **6 expuestas y 55 con `x-mcp-ignore`**). 🔵 **A favor de `oneroster-ts`: no hay ninguna anotación de
  supresión ni `scope` de tool en el repo**, que es una postura distinta de la de CaSS. ~~**La frase citable es «164
  métodos de SDK contados», no «164 tools MCP».** Medirlo es la **acción 2 del pase 30**.~~
- ✅ **MEDIDO EN EL PASE 30 EJECUTANDO EL SERVIDOR, Y LA CAUTELA SE LEVANTA EN LA DIRECCIÓN FAVORABLE.** `initialize` +
  `tools/list` por stdio contra `bin/mcp-server.js` devuelve **132 tools** —**72 de lectura y 60 de escritura, en 19
  grupos**— y el servidor se identifica como **`OneRoster 0.7.0`**. 🔵 **La brecha 164 → 132 no era supresión: era
  *aliasing*.** El SDK documenta 164 métodos pero sólo **132 nombres distintos**, porque **32 operaciones están listadas
  bajo dos grupos a la vez** (`getStudentsForClass` en `classes` **y** en `students`; los cinco de *course components* en
  `coursecomponents` **y** en `courses`; y así 32 veces). **Cero anotaciones de supresión: se sirve el 100 % de las
  operaciones distintas**, lo contrario de CaSS. **La frase citable definitiva: «132 tools MCP servidas, el 100 % de las
  operaciones del SDK».** 🔵 **Y un dato de diseño que conviene usar: el servidor acepta `--tool`, así que se sirve un
  SUBCONJUNTO.** Darle 132 tools enteras a un agente es ventana de contexto desperdiciada y riesgo de elección errónea:
  **el recorte por caso de uso es decisión de diseño, no limitación.**

- 🔴 **Riesgo de licencia que el pase 29 descubrió y que cambia la recomendación de «forkear» de buena práctica a
  requisito: el paquete que se instala no declara licencia.** El repo es **0BSD**; el artefacto publicado es
  **`@superbuilders/oneroster`** y npm devuelve **`license: None`** en la raíz y en `0.7.0`. Además **los
  *maintainers* de npm no son la organización del repo** (`abhi-superbuilders`, `hbauer`, `bjornpagen`,
  `supersterling`, `ameeralns` contra `trilogy-group`), aunque ✅ la procedencia es rastreable por el `repository.url`
  del paquete. **Y el último publicado es del 2026-05-04**, casi cinco meses, en versión **pre-1.0**. **Entonces el
  entregable no depende del paquete: se fija un fork del repositorio, donde la 0BSD sí está declarada.** Ver el
  **gap 53**.

- **El `--client-id`, `--client-secret` y `--token-url` del arranque dicen la forma de la autenticación: OAuth2
  *client credentials*.** Es lo que espera OneRoster 1.2, y es un dato de integración que se confirma con el cliente
  **antes** de la semana uno, porque las credenciales las emite su SIS.
- **10 ★ y 39 commits.** Es un **caso de gap 49** —capacidad alta, promoción nula— y eso es bueno para el hallazgo y
  **malo para el riesgo de mantenimiento**. **0BSD permite forkear sin ninguna obligación**, y para un entregable de
  cliente **eso es exactamente lo que hay que hacer: fijar el fork**.
- **Escribir matrícula es escribir el dato más sensible del sistema.** Ninguna de las tres fases va sin compuerta
  humana y sin registro de evidencia.

## P59 — El conector MCP de QTI, que es la única ausencia de esta KB medida por tres métodos (pase 28)

**El contraste con P58 es el punto del patrón.** OneRoster parecía vacío y tenía puerta. **QTI parece vacío y está
vacío**, y se puede afirmar porque se midió por **tres métodos independientes**:

| Método | Resultado |
|---|---|
| Consulta a directorio MCP (pase 26) | vacío — **no concluyente** (gap 49) |
| Patrón de nombre `qti-mcp` / `mcp-qti` (pase 27) | vacío |
| **Apertura del SDK permisivo** (pase 28) | 🔴 **`examplary/qti` (MIT, QTI 3.0 + 2.1): MCP no se menciona en el repo** |

**Y hay una explicación, que es mejor que un registro de ausencia:** la otra implementación de la capa,
**`oat-sa/qti-sdk`, es PHP**, y el ecosistema MCP de PHP es marginal. **La ausencia no es casual: el estándar de
evaluación de 1EdTech vive en el lenguaje donde la puerta de agente no se está construyendo.**

**La pieza sobre la que construir, y es la buena noticia:** `examplary/qti` es **MIT**, **TypeScript** y cubre **QTI
3.0 (default) y 2.1** — generación **y** parseo de paquetes. Es exactamente la forma de `oneroster-ts` antes de que
alguien le agregara el *transport*. **El trabajo no es escribir un conector de QTI: es agregarle MCP a un SDK MIT que
ya habla el estándar**, que es el movimiento más barato que identificó la tendencia **73**.

**Wiring propuesto:**

```
[Agente autor de evaluaciones]
        │
        ├──MCP──▶ qti-mcp  (A CONSTRUIR sobre examplary/qti, MIT → MIT)
        │             │  generate_item · parse_package · validate_qti3 · export_package
        │             ▼
        │        Paquete QTI 3.0  ──▶ banco de ítems / LMS que importa QTI
        │
        └──MCP──▶ scorm-mcp-server (MIT)  ◀── la vía alterna de P56 si el LMS no habla QTI
```

**Dónde encaja en lo que esta KB ya tiene:** es la pieza que le falta a **P48** (migración QTI → banco → entrega
certificada → evidencia xAPI → competencia en CaSS), donde el primer tramo se hacía **a mano**. Con esto, el tramo de
autoría y validación de ítems entra a la superficie de agente, y **P48 pasa a ser agéntico de punta a punta salvo la
entrega certificada**.

⚠️ **Y la cautela de encuadre:** `examplary/qti` tiene **1 ★ y 32 commits**. Es una base pequeña. **Para un entregable
de cliente se forkea y se fija** — la MIT lo permite sin obligaciones más allá de la atribución. **Lo que no se debe
hacer es prometer un conector de QTI como si existiera:** no existe, y éste es el patrón para construirlo, no para
comprarlo.

## P60 — El conector MCP de CASE **generado, no escrito**: el patrón más barato de esta KB, y el único donde el sistema publica su propia especificación (pase 29)

**El contraste con P55 y P59 es el punto del patrón.** Open edX hay que integrarlo a mano y con adaptador de versión
(**P55**). QTI hay que construirlo desde cero (**P59**). 🔵 **CASE no: el servidor de referencia sirve su propio
OpenAPI 3, así que el conector se genera.**

### Lo que existe, y está verificado de primera mano

| Pieza | Repo | Licencia | Qué aporta |
|---|---|---|---|
| **Servidor + editor de marcos** | [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) | **Apache-2.0** ✅ (leída del archivo `LICENSE`) | **CASE Provider API oficial**, CASE **1.0 y 1.1**, CRUD de escritura sobre `CFDocuments`/`CFItems`/`CFAssociations`/`CFPackages` en **v1p0 y v1p1**, editor visual, Keycloak (OIDC) **+ API keys**, RBAC de 4 niveles, multi-tenencia, **versionado inmutable en archivos sin base de datos externa**, despliegue de un comando en Docker |
| **Aserción de competencia por MCP** | [`cassproject/CASS`](https://github.com/cassproject/CASS) | **Apache-2.0** ✅ | `record_evidence` y `get_learner_profile`, las dos tools que **P48** y **P57** ya usan |
| **Evidencia xAPI** | `learnmcp-xapi` + `lrsql` | **MIT** ✅ / Apache-2.0 | El registro de lo que el agente hizo |

🔵 **El dato que define el patrón:**
`GET /ims/case/v1p1/discovery/imscasev1p1_openapi3_v1p0.json`. **El sistema al que hay que conectarse publica la
especificación con la que se genera el conector.** No hay que inferirla de la documentación, y **no puede estar
desactualizada respecto del servidor que la sirve**.

### El precedente que prueba que el camino funciona

**No es teoría: ya pasó en esta misma KB.** `trilogy-group/oneroster-ts` llegó a **164 métodos sobre 21 grupos de
recurso con 39 commits** porque **se generó desde la especificación** (Speakeasy) y **el servidor MCP salió como un
modo del SDK**, no como un proyecto aparte. **La proporción método/commit es imposible a mano, y es justamente la
firma de un conector generado.**

### Cómo se arma, concretamente

```
OpenCASE (Apache-2.0, Docker, 1 comando)
   │
   ├── GET /ims/case/v1p1/discovery/imscasev1p1_openapi3_v1p0.json   ← la especificación, servida por el propio sistema
   │        │
   │        └──▶ generador de SDK + servidor MCP  ──▶  conector MCP de CASE
   │                                                      │
   │                              (curaduría: qué se expone y qué no)
   │                                                      │
   ├── API keys por tenant  ◀── auth del agente ───────────┘
   │   (POST /management/tenants/{tenantId}/api-keys)
   │
   └── versionado inmutable por archivo  ──▶  expediente de auditoría, sin construir nada

   agente de autoría ──▶ propone items y asociaciones ──▶ editor visual ──▶ humano aprueba (P54)
                                     │
                                     └──MCP──▶ CaSS `record_evidence` ──▶ learnmcp-xapi ──▶ lrsql
```

### Los tres entregables, de menor a mayor riesgo

| # | Entregable | Por qué es de bajo riesgo |
|---|---|---|
| 1 | **Lectura y consulta de marcos por MCP** (qué competencias existen, cómo se relacionan, qué prerrequisitos tiene una) | **Sólo lee**, y el filtrado por campos, la paginación y el ordenamiento ya los define la especificación. Es el *quick win* |
| 2 | **Alineación de contenido a estándar**: el agente propone a qué competencia corresponde cada recurso, una persona confirma | Es **el caso de uso que el propio 1EdTech pone adelante**, y el versionado inmutable deja cada propuesta auditada **sin trabajo extra** |
| 3 | **Autoría asistida de marcos**: el agente propone items y asociaciones (*is child of*, *is related to*, *precedes*) y el editor visual es la compuerta | La escritura existe en **v1p0 y v1p1**, y 🔵 **es exactamente lo que `cassproject/CASS` tiene cerrado a MCP** (0 expuestas / 13 ocultas): **este patrón abre por REST lo que el otro proyecto decidió no exponer** |

### Por qué este patrón gana en EMEA y en North America

- **EMEA:** el AI Act clasifica la **evaluación** como alto riesgo y exige **gobernanza de datos, supervisión humana y
  trazabilidad**. 🔵 **El versionado inmutable por archivo es el expediente**, y el despliegue de un comando en
  infraestructura propia resuelve **residencia de datos** en la misma jugada.
- **North America:** Oklahoma y Maryland **prohíben la decisión autónoma sobre el alumno**, y cuatro estados obligan a
  política distrital escrita. **Este patrón no decide sobre ningún alumno** —opera sobre el currículo, no sobre la
  persona— y produce el registro que la política exige. **Es el de menor fricción regulatoria de toda esta KB.**

### 🔴 Las tres cautelas, y son honestas

- **Las rutas exactas están en contradicción entre dos documentos del repo** (`DEVELOPER.md` sin prefijo,
  `FRAMEWORK_EDITOR_BACKEND_INTEGRATION.md` con `ims/case/v1p1/`), y **el `FRAMEWORK_MANAGEMENT_GUIDE.md` que el README
  ofrece como referencia completa devuelve 404 en `main`**. **Es el gap 52.** **Hasta resolverlo, este patrón se
  propone con arquitectura y costo relativo, no con rutas literales** — y la forma de resolverlo es pedirle el OpenAPI
  al endpoint de descubrimiento con una instancia levantada.
- **No se hizo ninguna llamada HTTP contra una instancia.** La superficie está **declarada en los docs del repo**, no
  observada. **OAuth2/Keycloak, *scopes*, *rate limits* y forma de las respuestas, sin verificar.**
- ⚠️ **Generar no es exponer, y ésta es la parte que se cobra.** **CaSS genera su catálogo y después oculta 55 de 61
  operaciones a propósito.** La decisión de qué tools se exponen —y cuáles no, sobre todo las de escritura— **es
  trabajo de producto y de riesgo, no de generador**. **9 ★ y 180 commits**: para un entregable de cliente **se fija un
  fork**, que la Apache-2.0 permite.

## P61 — El rail de escritura de agente, reimplementado en permisivo: la pieza que vuelve aprobable un agente con permiso de escritura (pase 30)

**Qué problema resuelve.** Todo patrón de esta KB que escribe en un sistema de producción —P54 (corrección y devolución en
Moodle), P53 (*early warning*), P58 (rostering sobre OneRoster), P60 (CASE)— choca con la misma objeción de un comité de
riesgo: *«¿qué pasa si el agente entra en bucle?»*. Hasta este pase, la respuesta de esta base era **«compuerta humana»**
descripta en prosa. **El pase 30 encontró la respuesta implementada y midió sus cuatro partes**, en `guards.py` de
`openedx-mcp` — que es **AGPL-3.0**, así que **lo que se propone acá es el diseño reimplementado, no el código**.

**El modelo de amenaza, citado del original, porque nombrarlo bien es la mitad del diseño:**

> *«An MCP key is driven by an autonomous agent, not a human clicking a button. The failure mode designed against is a
> *looping* agent — a retry storm that mass-enrols or deletes.»*

**Los cuatro rails, y qué pieza permisiva usa cada uno:**

| Rail | Qué hace | Implementación permisiva |
|---|---|---|
| **1. Autoridad viva** | La credencial **no cachea privilegio**: se re-chequea en cada llamada. Degradás al usuario y **todas sus claves mueren en la llamada siguiente** | El verificador de JWT del propio sistema + una consulta de rol por request. **Los `scopes` de una clave sólo acotan, nunca amplían** |
| **2. Rate limit por (clave, tool)** | Convierte un bucle en ~N llamadas. **El límite codifica el riesgo de cada operación, no un número global** | Redis/memcached **compartido** (ver el riesgo abajo). Referencia medida: masivo **5/300 s**, destructivo **5/600 s**, autoría **200/60 s** |
| 🔵 **3. Confirm token** | Una escritura **sin token no escribe**: hace **dry run**, devuelve *preview* + **token de un solo uso atado a una huella del payload exacto**. Cambiar el payload **invalida el token**. TTL 300 s | Hash del payload canonicalizado + almacén con TTL. **Es el rail que hace el trabajo** |
| **4. Auditoría previa** | La intención se registra **antes** de escribir, y **la escritura se rechaza si el registro no se puede persistir** | Tabla *append-only*. **Nada de «loguear después»**: el log es precondición, no efecto |

🔵 **Por qué el rail 3 es el que importa, dicho en una línea para una propuesta:** el problema de seguridad de un agente
con permiso de escritura es que **«confirmar» y «hacer» son el mismo acto**. Separarlos con un token **atado a la huella del
payload** hace imposible el *bait-and-switch* —el agente no puede hacerse aprobar un *preview* y aplicar otra cosa—
**sin poner un humano en cada llamada**. **Eso es lo que convierte «agente que escribe» en algo aprobable.**

🔴 **El riesgo de despliegue que hay que cotizar, y que está en el código del original y no en su documentación:** el
almacén del confirm token y el contador del rate limit **tienen que ser un backend compartido**. Con caché en memoria por
proceso y varios *workers*, **los rails 2 y 3 se degradan en silencio**: el límite cuenta por proceso y el token puede
caer en un worker que no lo tiene. **Es una línea de infraestructura obligatoria (Redis), no un *nice to have*.**

**Vocabulario de scopes que conviene copiar tal cual**, porque ya está probado contra un dominio educativo real:
`read`, `write:enrollment`, `write:users`, `write:roles`, `write:certificates`, `write:reports`, `write:courses`,
**`grant:admin`** y **`destructive`** (aditivo). 🔵 **Separar `grant:admin` y `destructive` del resto es la decisión que
permite habilitar un agente útil sin habilitar un agente peligroso**, y es exactamente la conversación que un cliente
quiere tener.

**Wiring.** Cualquier conector de esta KB + este rail por delante:

```
[Agente] → [Servidor MCP del conector: moodle-mcp (MIT) / oneroster-ts (0BSD) / el de CASE generado por P60]
              ↓  (cada tool de escritura envuelta en el decorador de rails)
         [Rail 1 autoridad viva] → [Rail 2 rate limit (Redis)] → [Rail 3 confirm token: dry-run + huella]
              ↓
         [Rail 4 auditoría append-only — precondición de la escritura]
              ↓
         [LMS / SIS / servidor de estándares]
```

**Estimación.** **2–3 semanas** para el decorador, el almacén de tokens, el vocabulario de scopes y las pruebas de bucle
(el *test* que importa: simular un agente en reintento y verificar que el rate limit y el token lo contienen). **Se cotiza
una vez y se reutiliza en todos los patrones de escritura de esta KB.**

**Y es vendible como entregable de gobernanza, no sólo como código** — que es justo lo que piden las dos regiones donde
esta base midió gobernanza atrasada: **APAC** (marcos que no siguen el ritmo de la implementación) y **LATAM** (9 % de
instituciones con mecanismos formales de evaluación).

## P62 — El expediente de competencia para un requisito de graduación, con el marco *suscripto* en vez de redactado (pase 30)

**Qué lo dispara, y es nuevo:** **Boston Public Schools convirtió la *AI fluency* en requisito de graduación a partir de
septiembre de 2026**, y hay legislación en seguimiento en **25 estados**. **Un requisito de graduación no se satisface con
un asistente**: necesita declarar la competencia, evaluarla y **dejar evidencia auditable de que el alumno la alcanzó**.
**Es el primer caso de esta KB donde el entregable es un expediente y no una herramienta.**

🔵 **La novedad de este pase que lo abarata, y es la razón de que el patrón sea nuevo y no una variante de P48:** la capa
**CGE — CASE Global Exchange** de OpenCASE (11 rutas, medidas en el pase 30) permite **suscribirse a marcos de competencia
del registro global de 1EdTech y mantenerlos sincronizados** (`subscriptions`, `import`, `frameworks/{id}/refresh`), en vez
de **redactar** el marco. **El alcance cambia de «digitalizar el currículum» a «suscribir y alinear»**, que es más barato y
mucho más defendible ante un consejo escolar: el marco no lo inventó el proveedor.

**La cadena, toda permisiva y toda verificada en esta KB:**

```
[Marco de competencia] 1EdTech/OpenCASE (Apache-2.0)
   ├── CGE: suscribir el marco del registro global  ← NO redactarlo
   └── CASE Provider API v1p1 (lectura con AUTH OPCIONAL si el marco es público)
          ↓
[Ítems de evaluación]
   ├── acervo legado QTI 1.2 → instructure/qti (MIT)      ← alta del pase 30
   └── ítems nuevos QTI 3.0  → examplary/qti (MIT)
          ↓
[Entrega y evidencia] xAPI → Yet Analytics SQL LRS (Apache-2.0)
          ↓
[Aserción de competencia] cassproject/CaSS (Apache-2.0) — record_evidence / get_learner_profile por MCP
          ↓
[Credencial portable] Open Badges / CLR
          ↓
[Rail de escritura] P61 sobre cada paso que escribe
```

⚠️ **Los dos límites que se declaran antes de cotizar, los dos medidos en este pase:** (a) **la escritura de OpenCASE no es
parte del estándar CASE** —lo dice su código—, así que la mitad de escritura del conector es específica de OpenCASE y **no
portable** a otro proveedor certificado; (b) **`instructure/qti` sólo importa y parsea**, y soporta **True/False, Multiple
Choice y Multiple Answer**: un acervo con *matching*, *ordering* o respuesta construida **no entra entero**, y eso es
alcance declarado, no sorpresa.

**Estimación.** **8–10 semanas** para una competencia y un grado, con el marco suscripto, el banco migrado, la entrega
instrumentada y el expediente armado. **La pieza reutilizable entre competencias es el expediente; la que se repite por
competencia es la alineación de ítems.**

**Región.** **North America** es donde el disparador existe hoy con fecha. **LATAM y EMEA** comparten la mitad de
cumplimiento del patrón pero **sin el requisito de graduación**, así que ahí se vende como *marco de gobernanza*, no como
requisito.


## P63 — Agente autor sobre Open edX — 🟢 **ACTUALIZADO EN EL PASE 32: el bootstrap SÍ lo da la API, y el asterisco del gap 57 se cae** (agregado en el pase 31; **LATAM e India primero**, donde está la huella pública grande de Open edX)

**Qué resuelve.** P55 venía cotizándose con asterisco porque no se sabía si el *authoring* de Open edX era alcanzable.
El pase 31 lo midió en tres capas independientes y la respuesta es **sí para todo lo que vive adentro del curso, no para
crear el curso**. Este patrón cotiza eso: agente que construye y mantiene contenido curricular en Open edX, con el
hueco del bootstrap cubierto explícitamente y con el rail de seguridad que el conector **no** trae.

**Piezas, con licencia verificada el 2026-10-02:**

| Pieza | Licencia | Rol en el patrón |
|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | **AGPL-3.0** | la plataforma; API `contentstore` `v0`–`v4` |
| [`openedx-mcp`](https://pypi.org/project/openedx-mcp/) + `tutor-contrib-openedxmcp` | ⚠️ **AGPL-3.0** (leída del `LICENSE` del wheel) | puerta MCP oficial: **35 rutas**, **19 escrituras** |
| `blocks/create-tree/` (ruta CMS del conector) | — | **crea el árbol** sección→subsección→unidad **en una llamada** |
| `downstreams/<usage_key>/sync` (REST `v2`, **fuera del conector**) | AGPL-3.0 | **propaga** el cambio de la biblioteca a los N cursos |
| [`LangGraph`](https://github.com/langchain-ai/langgraph) | MIT | el grafo del agente, con el nodo de confirmación humana |
| [`Temporal`](https://github.com/temporalio/temporal) | MIT | durabilidad de la secuencia de escritura y reintentos **idempotentes** |

### El wiring, en el orden en que hay que construirlo

1. 🟢 **Bootstrap del curso — y en el pase 32 esto dejó de ser trabajo.** El pase 31 concluyó que *«ninguna de las
   cinco versiones REST crea un curso»*, y la medición era correcta pero el alcance no: **el árbol REST versionado no es
   toda la superficie HTTP de Studio.** La creación vive en el handler legacy:

   ```
   POST /course/                      (cms/djangoapps/contentstore/views/course.py:342 → _create_or_rerun_course :1184)
   Accept: application/json
   {"org": "...", "number": "...", "run": "...", "display_name": "..."}        → crea de cero  → {"course_key": "..."}
   {"org": "...", "number": "...", "run": "...", "display_name": "...",
    "source_course_key": "course-v1:..."}                                     → clona         → {"destination_course_key": "..."}
   ```

   **Las tres consecuencias que cambian la cotización:**
   - 🟢 **No hace falta curso plantilla ni alta manual en Studio.** `create_new_course` se activa **omitiendo
     `source_course_key`**. La «tarea manual de una vez» que este patrón cotizaba **se elimina del presupuesto**.
   - 🟢 **El permiso es `is_content_creator(user, org)`, no `GlobalStaff`.** Para multi-tenant esto es decisivo: **el alta
     de cursos se delega por organización**, sin entregar superusuario. (`GlobalStaff` sólo gatea las dos vistas **GET**
     de formulario — `CourseRerunView` del REST `v1` y `course_rerun_handler` —, que **no escriben nada**.)
   - ⚠️ **La clave vuelve sincrónica; el contenido, no.** En el caso de clonado, `rerun_course` (**:1331**) devuelve
     `destination_course_key` de inmediato pero despacha el copiado a **Celery** (`rerun_course_task.delay`, **:1375**).
     **Hay que pollear `CourseRerunState`** (`FAILED`/`SUCCEEDED`, vía `CourseRerunUIStateManager`) antes de escribir en
     el curso nuevo, o el paso 2 corre contra una copia en vuelo. **Este es el nodo de espera que el grafo necesita.**

   🔴 **Y una trampa que rompe en runtime, no con un 400 prolijo:** `rerun_course` lee **`fields['display_name']`** sin
   guarda (**:1359**), pero `_create_or_rerun_course` sólo puebla esa clave `if display_name is not None`. **Omitir
   `display_name` al clonar levanta `KeyError`.** Tratarlo como **obligatorio para clonar**, opcional para crear.
   Además el clonado **resetea** `advertised_start`, `enrollment_start`, `enrollment_end` y `video_upload_pipeline`, y
   hace `add_instructor(destination, user, user)`: **quien clona queda instructor del clon** — hay que preverlo en el
   modelo de permisos del entregable.

2. **Estructura.** `POST blocks/create-tree/` con el árbol completo: `category: chapter` → `sequential` → `vertical`.
   Por REST crudo el equivalente es `POST /api/contentstore/v1/xblock/` con `parent_locator` + `category` **bloque por
   bloque** — razón suficiente para usar el conector acá y no la API cruda.
3. **Contenido.** `blocks/update/` por componente. El `XblockSerializer` es **estricto** (*«No unexpected fields are
   passed in»*): el agente tiene que emitir exactamente `data`, `metadata`, `fields`, `display_name` — **validar el
   payload contra el serializer antes de llamar**, porque un campo extra es un 400 y no un *warning*.
4. **Publicación con humano en el lazo.** `blocks/publish/` **pide *confirm token*** (`require_confirm=True`): es el
   punto natural de la compuerta pedagógica. Nada se publica sin que un docente confirme — y eso no hay que construirlo,
   **el conector ya lo exige**.
5. **Mantenimiento, que es donde está el margen.** El material común vive en una **biblioteca (Libraries v2)** y se
   propaga con `downstreams/<usage_key>/sync`. ⚠️ **Esa capa no está en el conector MCP** (no figura entre sus 7 rutas
   CMS), así que **el agente necesita dos canales: MCP para operar y REST directo para propagar.** Sumar ese cliente REST
   al alcance. ⚠️ **Y antes de prometer propagación sobre contenido que el docente edita, cerrar el gap 59**: no se midió
   qué hace `sync` ante un bloque *downstream* editado localmente.

### 🔴 El rail que hay que agregar, porque el conector no lo tiene

Las **19 escrituras** se reparten en **11 con *confirm token* y 8 sin él**. Entre las 8 sin token está
**`unenroll_user`**. El modelo de amenaza del propio código —*«a looping agent… a retry storm that mass-enrols or
deletes»*— **está implementado contra la operación masiva, no contra la repetida**: `bulk_enroll` pide confirmación,
`unenroll_user` de a uno no. **Un agente en bucle puede desmatricular 500 alumnos en 500 llamadas sin un solo token.**

**Lo que hay que poner afuera del conector, y es alcance de este patrón:**

- **cuota por sujeto y por ventana** (p. ej. *N* operaciones de matrícula por alumno por hora), no sólo por operación —
  es el rail que falta, y es el que protege al alumno;
- **idempotencia por clave de negocio** en Temporal (`(curso, alumno, operación)`), para que un reintento no cuente como
  una segunda escritura;
- **tope de *blast radius* por ejecución**: el agente no puede tocar más de *K* sujetos por corrida sin aprobación
  humana, con `K` configurable y auditado.

### Licencia — decirlo en la primera reunión

⚠️ El conector es **AGPL-3.0 y corre *in-process*** como plugin Django (tendencia 82: *la licencia de un conector la
decide su arquitectura*). **No hay frontera de proceso que aísle la obligación.** Para un cliente que no acepta AGPL en
su árbol, la alternativa es **consumir `contentstore` por REST desde un servicio propio** y escribir un conector MCP
*out-of-process* — más trabajo, y la medición de este pase deja el mapa de rutas hecho para hacerlo.

**Estimación.** 6–8 semanas con el plantilla + `course_rerun` resuelto y sin la capa `downstreams`; **9–12 semanas** con
propagación por biblioteca y los tres rails de cuota. El bootstrap manual del plantilla: horas, una vez.

## P64 — *Rostering* conforme a OneRoster por MCP, ahora con opción **MIT** (agregado en el pase 31; transversal, y es la pieza de entrada de cualquier proyecto con SIS)

**Qué cambia respecto de lo que esta KB venía cotizando.** El pase 28 encontró que OneRoster tenía conector y era
**0BSD** (`trilogy-group/oneroster-ts`, 132 tools medidas en el pase 30). El pase 31 preguntó al registro de npm por el
**estándar** y encontró **una segunda puerta, y es MIT**. Eso saca la conversación de licencia del camino crítico con
clientes cuyo *procurement* no tiene criterio para 0BSD.

| Pieza | Licencia | Verificación | Rol |
|---|---|---|---|
| [`@eduware/oneroster`](https://registry.npmjs.org/@eduware%2Foneroster) v1.2.11 | **MIT** ✅ | ⚠️ paquete sí; repo `Eduware-Inc/eduware-oneroster` **404** (gap 58) | **servidor MCP empaquetado** (ejecutable `mcp`); OneRoster **1.1 + 1.2** + perfil `ClassLink` de lectura |
| [`@superbuilders/oneroster`](https://github.com/trilogy-group/oneroster-ts) v0.7.0 | 0BSD ✅ | ✅ repo verificado | alternativa medida: **132 tools** |
| [`LongsightGroup/oneroster`](https://github.com/LongsightGroup/oneroster) v0.3.0 | **MIT** ✅ | ✅ repo verificado | **sin MCP**, pero cubre **los dos perfiles** del estándar (CSV **y** REST) — la pieza para el lado *batch* |
| [`Temporal`](https://github.com/temporalio/temporal) | MIT | — | sincronización durable, reintentos idempotentes |

### Wiring

1. **Elegir puerta por licencia, no por estrellas** (que este pase no pudo medir y por lo tanto no publica):
   `@eduware/oneroster` si el cliente pide MIT; `oneroster-ts` si quiere el repo público verificable y acepta 0BSD.
   **Declarar la elección y el motivo en la propuesta** — son dos licencias permisivas distintas y la diferencia es de
   *procurement*, no técnica.
2. **Perfil REST para lo incremental, CSV para la carga inicial.** OneRoster tiene **dos perfiles** y casi toda
   implementación cubre uno. `LongsightGroup/oneroster` cubre los dos: usarlo para el *bulk load* del año académico y la
   puerta MCP para el delta diario.
3. **El agente consume el roster como *tools*, no como base de datos.** Clases, docentes, alumnos e inscripciones
   llegan por MCP, lo que deja el modelo de permisos del SIS **del lado del SIS** — es el mismo argumento de P9 (agente
   adentro del SIS sin fricción de licencia) y acá se cumple con licencia permisiva de punta a punta.
4. **Rail obligatorio, por lo que aprendió P63:** el *rostering* escribe sobre personas. Antes de habilitar escritura,
   **contar qué fracción de las tools del SDK elegido pasa por confirmación** y poner **cuota por sujeto** afuera. No
   asumir que el SDK la trae: en el conector de Open edX, 8 de 19 escrituras no la tienen.

⚠️ **Dónde NO sirve este patrón:** si el cliente necesita **Caliper** para la telemetría, no hay pieza usable —
`@timeback/caliper` v0.3.3 es de **2026-09-25** y **no declara licencia**. La ruta de telemetría sigue siendo **xAPI/LRS**
(ver **P15**), no Caliper.

**Estimación.** 3–4 semanas para el delta diario por MCP con un SIS que ya habla OneRoster; +2 semanas si hay que hacer
la carga inicial por CSV; +2 semanas para los rails de cuota e idempotencia.


## P65 — Propagación segura de biblioteca a N cursos, con el default que ya protege al docente (agregado en el pase 32 del 2026-10-02)

**Qué resuelve.** El patrón más pedido en un despliegue grande: una corrección se hace **una vez** en la biblioteca y
baja a los **N** cursos que la usan. P63 ya lo usaba como paso 5, pero con un asterisco abierto (**gap 59**): nadie había
medido qué pasa cuando **el docente ya editó localmente** el bloque que recibe la actualización. **Medido en el pase 32,
y la respuesta habilita el patrón en vez de limitarlo: el `sync` preserva las personalizaciones por omisión.**

**Piezas, con licencia verificada el 2026-10-02:**

| Pieza | Licencia | Rol |
|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) — `contentstore/rest_api/v2/views/downstreams.py` | **AGPL-3.0** | las cuatro operaciones de vínculo *upstream/downstream* |
| [`LangGraph`](https://github.com/langchain-ai/langgraph) | MIT | el grafo: decidir qué cursos sincronizar y en qué orden |
| [`Temporal`](https://github.com/temporalio/temporal) | MIT | durabilidad: N cursos es N llamadas que pueden fallar a la mitad |

### La superficie real, que es de cuatro escrituras y no de una

| Operación | Qué hace | Cuándo usarla en el patrón |
|---|---|---|
| `POST downstreams/{usage_key}/sync` | Acepta la actualización | el camino feliz |
| `DELETE downstreams/{usage_key}/sync` | **Rechaza** la actualización (`decline_sync`) → `204` | **el docente dijo no** — el patrón tiene que ofrecer este botón, no sólo el de aceptar |
| `PUT downstreams/{usage_key}` | Fija o edita el vínculo (`upstream_ref`, con parámetro `sync` `"true"`/`"false"`) | **enganchar** contenido existente a una biblioteca, que es la migración inicial |
| `DELETE downstreams/{usage_key}` | **Corta** el vínculo (`sever_upstream_link` + borra `ComponentLink`/`ContainerLink`) → `204` | el curso se bifurca a propósito y deja de seguir a la biblioteca |

### El wiring

1. **Enganche inicial.** `PUT downstreams/{usage_key}` con `upstream_ref` y **`sync: "false"`** sobre el contenido que ya
   existe en los cursos. Con `sync: "false"` el bloque **no se sobreescribe**, pero la plataforma **igual trae los
   valores personalizables del upstream y los guarda como campos ocultos** — que es lo que después permite al docente
   «restaurar al default». **Hacer este paso con `sync: "true"` es el error que pisa contenido en la migración.**
2. **Propagación.** Por cada *downstream*, `POST .../sync` **sin cuerpo**, o con el cuerpo explícito:
   ```json
   { "override_customizations": false, "keep_custom_fields": [] }
   ```
   🟢 **`override_customizations` vale `False` por omisión:** **un `sync` no pisa lo que el docente personalizó.** El
   patrón es seguro **por defecto**, no por configuración.
3. 🔴 **El único rail que hay que escribir, y es una línea de code review, no un diseño.** El riesgo no es el `sync`: es
   **un integrador que manda `override_customizations: true` sin `keep_custom_fields`**. Prohibirlo en el cliente, y si
   alguna vez hace falta sobrescribir, **exigir `keep_custom_fields` poblado** en la misma llamada.
4. 🔴 **La excepción que hay que tratar aparte: `video`.** Si `block_type == "video"`, el `post` llama
   **`clear_transcripts(downstream)` *antes* de copiar** — «delete all transcripts so we can copy new ones from
   upstream». **Si el upstream no trae transcripciones, se pierden.** Y las transcripciones son **requisito de
   accesibilidad**, no un adorno: en North America caen bajo las obligaciones de supervisión y en EMEA entran al
   expediente del Anexo III. **Rail concreto:** antes de sincronizar un bloque de video, **verificar que el upstream
   tiene transcripciones**; si no, **rechazar con `DELETE .../sync`** y escalar a humano.
5. **Durabilidad.** N cursos son N llamadas HTTP que pueden cortarse a la mitad. Temporal, con el `usage_key` como clave
   de idempotencia.

⚠️ **El caveat que va en la propuesta, no en una nota al pie:** las **cuatro clases** del módulo están rotuladas
**`[ 🛑 UNSTABLE ]`** en su propio *docstring*. Es API usable hoy y **sin contrato de estabilidad**: hay que fijar la
versión de Open edX y **presupuestar una revisión por upgrade**.

## P66 — Evaluación portable: QTI 3 en TypeScript permisivo y salida a SCORM/cmi5 por MCP (agregado en el pase 32 del 2026-10-02)

**Qué resuelve.** La capa de evaluación era el hueco más viejo de esta KB en licencia y en *stack*: el pase 28 midió por
tres métodos que lo utilizable era **PHP** (`oat-sa/qti-sdk`), y la salida al LMS del cliente dependía de una pieza de 3
tools. El pase 32 encontró **las dos mitades en MIT**, y una de ellas **con servidor MCP incorporado**.

**Piezas, con licencia verificada el 2026-10-02:**

| Pieza | Licencia | ★ | Rol en el patrón |
|---|---|---|---|
| [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | **MIT** ✅ | 5 | **12 paquetes**: `qti3-core` (parser + validación + *scoring*, **cero dependencias**), `-player` (web component), `-player-react`/`-preact`, `-writer` (emitir QTI), `-migrator` (1.2/2.x → 3), `-transcoder` (3 → 1.2/2.x), `-conformance`, `-a11y`, `-pnp`, `-fixtures`, `-cli` |
| [`course-code-framework/coursecode`](https://github.com/course-code-framework/coursecode) | **MIT** ✅ | 5 | **Servidor MCP incorporado**; empaqueta a **SCORM 1.2, SCORM 2004, cmi5 y LTI 1.3** |
| [`tincan`](https://pypi.org/project/tincan/) | **Apache-2.0** ✅ | — | telemetría xAPI de los intentos, si el cliente tiene LRS |
| [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** ✅ | 448 | genera **rúbricas y modos de falla** desde el material del docente, que es la entrada del ítem |

### El wiring

1. **Entrada: del material del docente al ítem.** `lineage-skill` destila los PDFs/videos del curso en activos de
   capacidad **con trazabilidad a la fuente**, incluidas **rúbricas** y **modos de falla** — los modos de falla son
   literalmente los distractores de un ítem de opción múltiple bien hecho.
2. **Autoría y validación en QTI 3.** `qti3-writer` emite el XML; **`qti3-core` lo valida y lo puntúa**, y como **no tiene
   dependencias de terceros** entra en un *bundle* de navegador o en un worker sin arrastrar árbol. `qti3-a11y` verifica
   los contratos de accesibilidad y `qti3-pnp` las *Personal Needs and Preferences* — las dos cosas que el expediente
   regulatorio pide y que normalmente se cotizan como desarrollo propio.
3. **Migración del banco que el cliente ya tiene.** `qti3-migrator` sube **QTI 1.2 y 2.x a QTI 3**; `qti3-transcoder`
   hace el camino inverso **cuando el LMS del cliente todavía no lee QTI 3**. Es la pieza que vuelve el patrón vendible
   en una institución con veinte años de ítems guardados.
4. **Reproducción.** `qti3-player` como web component, con adaptadores React o Preact según el front del cliente.
5. 🟢 **Salida al LMS, por MCP.** `coursecode` empaqueta el resultado a **SCORM 1.2/2004, cmi5 o LTI 1.3**, y **expone un
   servidor MCP** que habla con Claude Code, Codex y Cursor: **el agente autor puede pedir el empaquetado como una tool**,
   sin que haya que escribirle un conector. Es el rol que en P56 ocupaba `scorm-mcp-server` (3 tools) **con dos estándares
   más y la misma licencia**.
6. **Telemetría.** Si el cliente tiene LRS, `tincan` (Apache-2.0) para emitir los *statements* de intento. ⚠️ **Buscar
   esta capa por `"Experience API"` o `"Tin Can"`, nunca por `xapi`**: los dos primeros resultados de ese término son un
   *marketplace* de cripto y el API de un bróker de forex, **los dos MIT y activos** (tendencia 96).

⚠️ **La honestidad que va al frente de la propuesta:** `qti3` y `coursecode` tienen **5 ★ cada uno**. Son hallazgos **de
capacidad y de licencia, no de adopción**: resuelven el bloqueo con licencia permisiva y tienen comunidad mínima. **Fijar
versión y prever *fork* mantenido** es parte del presupuesto, igual que esta KB ya escribió para `oneroster-ts`.
🔴 **Y el hueco declarado (gap 60):** **ninguna de las dos capas de QTI ni xAPI tiene puerta MCP** — `qti3` trae
`AGENTS.md` pero no MCP. **La contribución *upstream* más limpia disponible hoy** es envolver `qti3-cli` en un servidor
MCP: el core no tiene dependencias y ya expone parser, validación y *scoring*, así que es trabajo de días. **Medirlo es la
acción 2 del pase 33.**

> 🔴 **CORREGIDO EN EL PASE 33 DEL 2026-10-02 — el párrafo de arriba afirma la mitad falsa del gap 60.** **xAPI SÍ tiene
> puerta MCP:** [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) (**MIT**, 3 tools — 1 escribe, 2
> leen), **y está en esta KB desde el pase 6**, en `agents/top.md` y en `repos/foundations.md`. El gap 60 armó su lista
> de candidatos con el **registro de paquetes**, y `learnmcp-xapi` **no está en ninguno** (PyPI 404, npm `total: 0`): el
> instrumento no podía verla. ✅ **La mitad QTI sí se sostiene**, y ahora confirmada por un segundo instrumento
> independiente — es la única ausencia de esta base que cumple ese requisito. ✅ **Y la acción 2 quedó cumplida: envolver
> `qti3-cli` cuesta UNA dependencia externa**, medido en sus metadatos (`dependencies` = sólo sus cuatro hermanas, cero
> de terceros). Ver **P69**, y las tendencias **99**, **100**, **101** y **102**.

## P67 — Evidencia de aprendizaje auditable sobre el LMS que el cliente ya tiene (agregado en el pase 33 del 2026-10-02; **North America y LATAM primero**, por razones opuestas)

**El problema que resuelve, y es distinto en cada región.** En **North America** hay mandatos que prohíben entrenar con
datos del alumno (**California AB 1159**) y exigen supervisión humana con prohibición de decisión autónoma (**Oklahoma**,
**Maryland**). En **LATAM** el **79 %** de los docentes ya usa AI pero el **88 %** declara compromiso *«mínimo» a
«moderado»*: **el dato de aprendizaje se está generando y se está perdiendo.** Las dos situaciones piden lo mismo:
**convertir la interacción con el agente en evidencia conforme al estándar, sin acumular dato personal y con cada
escritura auditable.**

### Las piezas, todas verificadas de primera mano en el pase 33

| Rol | Pieza | Licencia | Estado medido |
|---|---|---|---|
| Almacén conforme | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** ✅ | 🟢 **`v0.9.9` el 2026-10-01**, 112 tags, seis releases en 2026. Corre sobre SQLite / PostgreSQL / MariaDB / MySQL |
| Almacén alternativo sobre Open edX | [`openfun/ralph`](https://github.com/openfun/ralph) | **MIT** ✅ | ⚠️ **Vivo en `main`, release de 2024-07-11** → instalar desde git. Convierte *tracking logs* de Open edX a xAPI **de fábrica** |
| Puente al agente | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** ✅ | **3 tools: 1 escribe, 2 leen.** `LRS_PLUGIN=lrsql\|ralph\|veracity`. 🔴 **Fuera de todo registro**: se instala desde el código |
| Rail de escritura | el del orquestador propio | — | ⚠️ **Hay que construirlo.** Ver el paso 4 y la tendencia **102** |

### El wiring, en el orden en que hay que construirlo

1. **El LMS se queda donde está y no se toca.** Si es **Open edX** (AGPL-3.0), el agente va **afuera** — y conviene
   **Ralph**, porque la ingesta de *tracking logs* ya existe y no hay que escribirla. Si es cualquier otro, **`lrsql`**
   sobre la base de datos que el cliente ya opera, para no agregar una pieza nueva al diagrama.
2. **`learnmcp-xapi` como servidor MCP del agente**, con `LRS_PLUGIN` apuntando al LRS del paso 1 y el
   `config/plugins/<backend>.yaml` con endpoint, credenciales y `retry_attempts`. Desde acá el tutor **registra** cada
   interacción como *statement* xAPI y **consulta** el historial antes de responder.
3. **La privacidad se configura, no se promete.** Un **`ACTOR_UUID`** por alumno, con la tabla de correspondencia
   **fuera** del LRS y bajo control del cliente. Lo que queda en el almacén es **actividad de aprendizaje**, no identidad
   — que es exactamente lo que **AB 1159** pide y lo que el **Anexo III** premia.
4. 🔴 **El rail que hay que agregar, porque ninguna de las piezas lo trae.** `learnmcp-xapi` tiene **una** tool de
   escritura (el *statement recording*) y **no** publica un *confirm token* como `openedx-mcp` ni anotaciones de
   destructividad como `coursecode`. En un despliegue con mandato de supervisión humana hay que interponer, **en el
   orquestador**:
   - **Ensayo**: construir el *statement* y mostrarlo antes de postearlo.
   - **Confirmación** para escrituras en lote, con huella del payload (el patrón de `openedx-mcp`, tendencia 84).
   - **Auditoría *append-only*** previa a la escritura: quién, qué, cuándo, con qué *prompt*.

   **Esto es desarrollo y se cotiza.** No está heredado de ninguna de las tres piezas.

### Estimación y lo que no hay que prometer

**6–8 semanas** con el LMS ya en producción: 1–2 para el LRS y la configuración de plugin, 2 para el rail del paso 4,
2–3 para el mapeo de vocabulario xAPI del dominio del cliente y el tablero.

⚠️ **Lo que NO hay que prometer, y es la advertencia que esta KB repite porque se la piden igual:** **ningún LRS estima
*mastery*.** Son almacenes conformes al estándar. La inferencia (`pyBKT`, `pyKT`) es **desarrollo propio** y es otro
patrón (**P15**). Y ⚠️ `learnmcp-xapi` tiene **32 commits** registrados: **es base a forkear o referencia de
integración, no dependencia de producción** — ver el **gap 63**, que es el que falta cerrar para saber si el `2.0.0`
cambia esa lectura.

---

## P68 — Telemetría soberana europea, con el argumento apoyado en el archivo de licencia correcto (agregado en el pase 33 del 2026-10-02; **EMEA**)

**Por qué es un patrón y no una variante de P67.** En una licitación pública europea el argumento de **soberanía
tecnológica** puntúa, y se verifica **abriendo el archivo de licencia**. Este pase midió que **las piezas de esta KB no
soportan el mismo argumento con la misma fuerza**, y el patrón consiste en usar cada una para lo que su `LICENSE`
respalda.

| Pieza | Lo que dice su `LICENSE` | Para qué sirve en el pliego |
|---|---|---|
| [`openfun/ralph`](https://github.com/openfun/ralph) | **MIT** — *«Copyright (c) 2020-present **France Université Numérique**»* | 🟢 **Soberanía.** Titular: **institución pública francesa** |
| `Richie` (OpenFun) | **MIT**, mismo origen institucional | 🟢 **Soberanía**, misma cadena de origen |
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** — *«Copyright (c) 2025 **David Romero**»* | ⚠️ **No soberanía** (titular: una persona). 🟢 **Privacidad por diseño**: `ACTOR_UUID`, *«No personal information is stored»* |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0**, Yet Analytics (EE. UU.) | 🟢 **Madurez y cadencia** (`v0.9.9`, 2026-10-01). 🔴 **No** sirve para el argumento de origen europeo |

### El wiring, y la decisión que lo gobierna

1. **Ralph como LRS**, no `lrsql`, **cuando el pliego valora el origen** — aunque `lrsql` tenga mejor cadencia. Es una
   decisión de licitación, no de ingeniería, y conviene escribirla como tal en la propuesta.
2. ⚠️ **Instalar Ralph desde `main` de git.** Último release en PyPI: **2024-07-11** (`ralph-malph` 5.0.1), con un
   `[Unreleased]` grande y activo en el `CHANGELOG.md` (CORS, baja de Python 3.8, correcciones de tipos Pydantic).
   **`pip install ralph-malph` trae código de hace ~2,2 años.** Fijar el *commit* y documentarlo.
3. **`learnmcp-xapi` encima**, con `LRS_PLUGIN=ralph`, y el argumento de **privacidad por diseño** en la sección de
   conformidad del expediente — **no** en la de soberanía.
4. **El expediente del Anexo III**, con el calendario fechado por inciso: **art. 50 (transparencia) rige desde el
   2026-08-02** —o sea, declarar que el alumno habla con una AI **ya es obligatorio**— y **el Anexo III, que es el
   inciso que nombra educación, desde el 2027-12-02**. La evaluación de conformidad (interna o auditoría de tercero) va
   **antes** de poner el sistema en el mercado.

🔴 **La regla de citación que hay que respetar, y es la única de esta KB que un abogado verifica en la primera
reunión.** La fecha del Anexo III está sostenida por **siete fuentes secundarias concordantes y cero primarias**:
`eur-lex.europa.eu` y `data.europa.eu` están **bloqueados** desde el entorno donde se investigó esta base (**gap 56**).
**No citarla como primaria**; pedir la verificación del texto consolidado como primer ítem del expediente.

**Estimación: 8–10 semanas**, de las cuales 3–4 son el expediente de conformidad y no el código.

---

## P69 — La puerta MCP de QTI, que no existe y cuesta una dependencia (agregado en el pase 33 del 2026-10-02; contribución *upstream*, transversal)

**Por qué este patrón es distinto de todos los demás de este archivo: acá Globant no integra, aporta.** La mitad QTI del
**gap 60** es la **única ausencia de esta KB medida por dos instrumentos independientes** —apertura de README de
candidatos (pase 32) y búsqueda abierta (pase 33)— más una lectura de SDK. **QTI, el estándar de interoperabilidad de
evaluación, no tiene puerta MCP.** Y la base sobre la que construirla está medida.

### El costo, medido en vez de estimado

| Medición | Valor | Fuente |
|---|---|---|
| Paquete | `@longsightgroup/qti3-cli@0.13.1` | `registry.npmjs.org` |
| Licencia | **MIT** ✅ | metadatos del paquete |
| Ejecutable | **`bin: { "qti3": "dist/index.js" }`** — ya es un CLI | metadatos del paquete |
| Superficie | *«parsing, validating, scoring, inspecting, and checking QTI 3 items»* | `description` del paquete |
| **`dependencies`** | 🟢 **Sólo sus cuatro hermanas**: `qti3-core`, `-a11y`, `-fixtures`, `-conformance` (las cuatro en `0.13.1`). **Cero dependencias de terceros en toda la cadena** | metadatos del paquete |
| Cadencia del monorepo | `@longsightgroup/qti3-migrator@0.13.1`, npm `modified` **2026-10-01** | `registry.npmjs.org` |

🟢 **La conclusión cotizable: un wrapper MCP sobre `qti3-cli` agrega exactamente UNA dependencia externa**
(`@modelcontextprotocol/sdk`) a un árbol que hoy no tiene ninguna. No hay que escribir parser, ni *scoring*, ni
validación: **ya están y son MIT.**

### El wiring de la contribución

1. **Un paquete nuevo en el monorepo** (`packages/mcp`), que importe `qti3-core` y exponga como tools MCP las
   operaciones que el CLI ya tiene: `parse`, `validate`, `score`, `inspect`, `check`.
2. **Las cuatro primeras son de sólo lectura** → `annotations: { readOnlyHint: true, idempotentHint: true }`.
3. **La de escritura es el *writer* de banco de ítems** (`qti3-writer`, que el pase 32 registró): esa sí necesita
   **`dryRun` + confirmación**, siguiendo el modelo de `coursecode`. ⚠️ **Y con la advertencia de la tendencia 102: la
   anotación MCP no frena sola.** Si la contribución quiere el freno real, va **un chequeo en el servidor**, como
   `openedx-mcp`.
4. **Salida al LMS, que ya está resuelta y es la pieza vecina:** **`coursecode`** (**MIT**) empaqueta a **SCORM 1.2,
   SCORM 2004, cmi5 y LTI 1.3** —los cuatro **en el `enum` del `inputSchema` de `coursecode_build`**, medido en este
   pase, no leído del README— y expone **15 tools** por MCP.

### El pipeline completo que esto cierra

```
[Agente autor] ──MCP──▶ qti3-mcp (a construir, MIT, +1 dependencia)
                            │  parse / validate / score / check  (lectura)
                            └─ writer de banco de ítems          (escritura, con dry run)
                                     │
                            ──MCP──▶ coursecode (MIT, 15 tools)
                                     └─ coursecode_build → cmi5 | scorm2004 | scorm1.2 | lti
                                              │
                                              ▼
                                        [LMS del cliente]
```

### Por qué conviene aportarlo en vez de tenerlo interno

El `LICENSE` es **MIT** y el monorepo está **activo** (`modified` 2026-10-01). Una contribución aceptada convierte a
Globant en **el integrador que escribió la puerta de agente del estándar de evaluación** — que es exactamente el
posicionamiento que la tendencia de esta KB describe: *«el integrador que sabe cuál de estas piezas sigue viva vale más
que el que sabe el estándar»*.

### ✅ La decisión, tomada en el pase 34 del 2026-10-02 — y la toma la licencia, no el número de adopción

El pase 33 dejó esta decisión abierta y pidió resolverla **con el número de adopción al lado**. Se midió en Packagist
(endpoint por paquete, que devuelve `license` y `time` **en cada versión**) y en npm:

| | `qtism/qtism` (OAT QTI-SDK) | `@longsightgroup/qti3-cli` |
|---|---|---|
| **Licencia** | 🔴 **GPL-2.0-only — en las 293 releases** | **MIT** ✅ |
| **Adopción** | 🟢 **218.212 descargas** totales, **3.104/mes**, 85 *favers* | menor y nueva (⚠️ `api.npmjs.org` no devolvió descargas para el paquete con *scope*) |
| **Actividad** | viva: `v19.7.2` el **2026-07-09** | 🟢 **41 releases**, primera **2026-05-21**, última modificación **2026-10-01** |
| **Dependencias de terceros** | stack PHP completo | 🟢 **cero en toda la cadena** |

Y el ecosistema PHP alrededor es real: `oat-sa/extension-tao-item` **130.032** descargas, `extension-tao-itemqti`
**128.201**, `-pci` **89.265**, `-pic` **79.373**, `extension-tao-itemhtml` **37.722**.

🔵 **Se contribuye sobre el lado TypeScript, y el criterio es que el número grande era el equivocado para esta
pregunta.** El stack PHP tiene **~10× la adopción** —el argumento que estaba a su favor— pero **`GPL-2.0-only` cierra
el caso de uso**: Globant no puede envolverlo en un producto propietario ni embeberlo en una entrega de cliente sin
heredar copyleft, y la obligación alcanza al derivado. **Y el lado MIT no sólo es viable: resulta ser el que se mueve
más rápido** —41 releases en cuatro meses y medio, la última de ayer—, que era lo contrario de lo esperable de la
opción con menos adopción. 🔵 **La regla general: cuando una de las dos opciones tiene una licencia que prohíbe el uso
previsto, la comparación de adopción no se empata, se descarta.**

⚠️ **Lo que la medición NO es:** la columna de adopción **no es simétrica** —Packagist da descargas y el endpoint de
npm no las dio para este paquete—, así que **la decisión se apoya en la licencia, que sí está medida de los dos
lados**, y no en una comparación de volumen que esta KB no puede hacer de forma pareja.
⚠️ **La decisión que falta, y es la acción 3 del pase 36.** El ecosistema QTI tiene **dos mitades**: la TypeScript
permisiva de `LongsightGroup` (**cero dependencias**, pero `qti3` tiene **5 ★**) y la PHP de **OAT SA** (**36 paquetes
en Packagist**: `qtism/qtism`, `oat-sa/extension-tao-*`, mucha más adopción). **La contribución más limpia es la
TypeScript; la de más alcance podría ser la PHP.** Hay que medir licencia y cadencia de `qtism/qtism` antes de elegir
—**y decidir con el número de adopción al lado, no por preferencia de lenguaje.**

⚠️ **La honestidad que va al frente de la propuesta:** `qti3` tiene **5 ★**. Es un hallazgo **de arquitectura y de
licencia**, no de tracción — y así hay que presentarlo.

---


## P70 — Credenciales verificables con el expediente cerrado por el propio consorcio (agregado en el pase 34 del 2026-10-02; **transversal, con North America primero**)

**El problema.** El cliente quiere emitir credenciales que valgan afuera —no un PDF con logo— y quiere poder
demostrarle a un tercero (una empresa que contrata, un ministerio, un área de compras) que la credencial es auténtica.
Hasta este pase esta KB **no tenía con qué**: `badgr-server` da **404**, el Open Badges de `cassproject/CASS` está
anclado a `w3id.org/openbadges/v2` —**OB 2.0, no 3.0**— y CaSS deja **Open Badges entero fuera de su superficie MCP**.

**Las piezas, las dos verificadas de primera mano en este pase.**

| Rol | Pieza | Licencia | Nota |
|---|---|---|---|
| **Emisión y gestión** | [`Schroedinger-Hat/certo`](https://github.com/schroedinger-hat/certo) | ⚠️ **AGPL-3.0** | **OB 3.0 + W3C VC + DIDs.** Plantillas de *Achievement* con criterios y habilidades, emisión **individual y masiva por CSV**, panel del receptor, **página pública de verificación**, compartir a LinkedIn. Strapi 5.x + Nuxt 3 |
| **Validación independiente** | [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) | **Apache-2.0** ✅ | Validador **del consorcio que escribe el estándar**, para **Open Badges y CLR**, con web, HTTP y **API** |
| **Evidencia de que la credencial se ganó** | `learnmcp-xapi` + `lrsql` | **MIT** / **Apache-2.0** ✅ | La capa que esta KB ya tenía: `ACTOR_UUID` sin dato personal, **30 escrituras/minuto** de techo |
| **Dimensionamiento previo** | `yetanalytics/datasim` | **Apache-2.0** ✅ | Carga el LRS con tráfico xAPI sintético **antes** de comprometer una cifra |

**El wiring, y el orden importa.**

1. **`lrsql` + `learnmcp-xapi`** registran la evidencia de aprendizaje mientras el alumno cursa — un statement por
   llamada, con `ACTOR_UUID` en lugar de identidad, y el techo de caudal de configuración como freno.
2. **Certo** emite la credencial OB 3.0 al cumplirse el criterio, **firmada criptográficamente** (W3C VC), de modo que
   **la insignia lleva su propia prueba y no depende de que el servidor del emisor siga en pie**.
3. 🟢 **El validador de 1EdTech cierra el expediente**, y es el paso que vuelve la propuesta defendible: el tercero
   verifica la credencial **contra el consorcio**, sin pedirle nada al emisor ni a Globant ni a Certo.

🔴 **La restricción de licencia va al frente de la cotización, no al pie.** **AGPL-3.0 en un servicio de red obliga a
ofrecer la fuente a los usuarios del servicio.** Entonces:

- ✅ **Certo desplegado y operado por el cliente** —el cliente lo customiza y asume la obligación— **es viable, y hoy
  es la única opción OB 3.0 completa que esta KB conoce.**
- 🔴 **Certo embebido en un producto propietario de Globant, no.** La obligación alcanza al derivado.
- 🟢 **Las otras tres piezas son permisivas** (MIT / Apache-2.0), así que **la pieza copyleft queda aislada en el borde
  del sistema** — que es la forma correcta de convivir con ella.

**Por qué North America primero.** El pase 34 midió el encuadre regulatorio de la región: 🔴 **en educación no existe
un equivalente a la FDA**, y la decisión la toma cada escuela, distrito o universidad con supervisión externa mínima.
🔵 **Donde no hay certificador, el comprador tiene que fabricarse su propia evidencia** — y este patrón es exactamente
eso, con **un validador neutral al final** en vez de una declaración del proveedor. Encaja además con lo ya registrado:
**California AB 1159** (sin datos del alumno para entrenar: `ACTOR_UUID` lo cumple por diseño) y la **supervisión
humana** exigida por **Oklahoma y Maryland**.

**Estimación.** 6–8 semanas para emisión + verificación sobre un LMS existente, con el validador integrado como paso de
CI del expediente. ⚠️ **Lo que falta medir y hay que decirlo: Certo no tiene puerta MCP** —reconfirmado por segundo
instrumento en este pase—, así que **la emisión se automatiza por su API, no por un agente**.

---

## P71 — Probar la telemetría antes de firmarla, y dejar la puerta MCP *upstream* donde el proyecto ya la espera (agregado en el pase 34 del 2026-10-02; **APAC y EMEA primero, por razones distintas**)

**El problema, y es el que más caro sale.** Esta KB recomienda `lrsql` o Ralph en **más de quince patrones** y hasta el
pase 34 **no tenía con qué dimensionarlos**. Se proponía una arquitectura de telemetría **sin haberla probado** — y en
APAC eso choca de frente con la barrera que el barrido regional de este pase midió: 🔴 **49 % de las empresas declara
infraestructura insuficiente para procesamiento de datos en tiempo real.** Una capa de telemetría de aprendizaje **es**
ingestión de eventos en tiempo real: es precisamente la objeción que hay que contestar con un número.

**Las piezas, todas verificadas y todas permisivas.**

| Rol | Pieza | Licencia |
|---|---|---|
| LRS | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** ✅ — `v0.9.9` del **2026-10-01**, 112 tags |
| LRS alternativo, soberano | [`openfun/ralph`](https://github.com/openfun/ralph) | **MIT** ✅ — `LICENSE`: *«Copyright (c) 2020-present **France Université Numérique**»* |
| 🟢 **Generador de carga y conformidad** | [`yetanalytics/datasim`](https://github.com/yetanalytics/datasim) | **Apache-2.0** ✅ |
| Puerta MCP | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** ✅ |
| Reenvío / middleware | `yetanalytics/xapipe` (LRSPipe) | ya en esta KB |

**El wiring, en el orden que convierte la propuesta en medición.**

1. **`datasim` genera tráfico xAPI sintético a escala** —*«benchmark and stress-test … with the Total Learning
   Architecture»*— **contra el `lrsql` del cliente, en su infraestructura**, antes de comprometer cualquier cifra.
   🟢 **Mismo mantenedor que `lrsql`, así que es la combinación que el propio proyecto usa.**
2. Se fija el techo de escritura **en la configuración** de `learnmcp-xapi` (`RATE_LIMIT_PER_MINUTE=30`,
   `MAX_BODY_SIZE=16384`): **frena solo, no pide cooperación del cliente MCP y cuesta dos variables de entorno**
   (tendencia **109**). 🔵 **Es el rail adecuado para esta capa porque acá el daño es acumulativo —inundar el LRS— y no
   irreversible y discreto como borrar un curso.**
3. `datasim` **valida además contra un xAPI Profile**, lo que cubre la capa de conformidad que **el pase 25 buscó sin
   encontrar**.
4. `xapipe` reenvía a la analítica del cliente si ya tiene una.

🟢 **Y la contribución *upstream*, con el sitio exacto medido en este pase.** El **gap 64** quedó cerrado en negativo:
**ninguno de los dos LRS publica puerta MCP propia** (Docker Hub de `yetanalytics`: **6 imágenes, ninguna MCP**;
`lrsql`: **0 menciones** en `deps.edn` y `README`; `ralph-malph` 5.0.1: **0 menciones** y **14 extras, ninguno MCP**).
🔵 **Pero el instrumento regaló el encaje:** los **14 extras** de Ralph —`backend-clickhouse`, `-es`, `-ldp`, `-lrs`,
`-mongo`, `-s3`, `-swift`, `-ws`, `backends`, `cli`, `lrs`, `dev`, `ci`, `full`— son **una convención de plugins ya
empaquetada**. Un **`ralph[mcp]`** con tres tools equivalentes a las de `learnmcp-xapi` (**1 escribe, 2 leen**) **entra
por la puerta del proyecto y no requiere fork.**

**Por qué EMEA para la mitad *upstream*.** Ralph es **MIT** y su archivo de licencia nombra a **France Université
Numérique**, una institución pública francesa — **el mejor argumento de soberanía europea que tiene esta base**, y el
que el pase 33 corrigió para que no se apoyara en `learnmcp-xapi` (cuyo `LICENSE` dice `Copyright (c) 2025 David
Romero`, una persona). Una contribución aceptada posiciona a Globant como **el integrador que escribió la puerta de
agente del LRS público europeo**.

**Estimación.** 2–3 semanas para el ensayo de carga con `datasim` sobre un `lrsql` desplegado (es el entregable que
contesta la objeción de APAC con un número). 4–6 semanas adicionales para el `ralph[mcp]` *upstream*.

⚠️ **Las tres cosas que hay que verificar antes de cotizar, y están escritas como acciones del pase 35.**
**(a)** `datasim` entró con **licencia verificada pero sin superficie medida**: no se sabe aún si tiene CLI, servidor o
las dos, ni si apunta a un LRS externo o sólo escribe archivos — **y de eso depende que el punto 1 sea horas o
semanas**. **(b)** **Ralph está vivo en `main` y parado en PyPI desde 2024-07-11**, así que la contribución se hace
**contra `main`** y cualquier dependencia **se instala desde git, no desde el registro**. **(c)** El `2.0.0` de
`learnmcp-xapi` **no se puede fechar por ningún canal alcanzable** (**8 rutas de versión, las 8 en 404**: el proyecto
no se versiona en su árbol), así que **se pinnea por commit, no por versión.**

---

## P76 — 🟢 El manifiesto MCP de QTI 3, ESCRITO: las 20 tools de `qti3-cli` con su corte de lectura/escritura (agregado en el pase 36 del 2026-10-02; **contribución *upstream*, transversal**)

> **Acción 2 del pase 35, ejecutada. Esto cierra el gap 70 y convierte P69 de «se puede» en «acá está la especificación».**
> Todo lo que sigue se midió **leyendo el `.tgz` de `@longsightgroup/qti3-cli@0.13.1` bajado de npm** —`src/index.ts`,
> `src/commands/*.ts`— no el README.

### 🔴 Primero, tres correcciones al conteo que esta KB traía, y las tres cambian el manifiesto

| Lo que la KB decía | Medido en el artefacto | Consecuencia |
|---|---|---|
| «**14 comandos**» | 🔴 **17 comandos de primer nivel** (`switch` de `executeCli`) | Un envoltorio escrito contra «14» **deja 3 comandos afuera** |
| «14 comandos» ⇒ 14 tools | 🔴 **20 tools invocables**: 16 comandos directos + **`certification` tiene 4 subcomandos** | El manifiesto es de **20 entradas**, no 14 |
| El `USAGE` del CLI es la superficie | 🔴 **El `USAGE` documenta 2 de los 4 subcomandos de `certification`** | **`verify-validator` y `check-import-report` no figuran en el `USAGE`.** Un envoltorio generado desde el `USAGE` —que es lo natural— **nace incompleto** |

🔵 **Y la lección general, que vale para cualquier CLI que esta KB envuelva: la superficie real está en el *dispatch*, no en el texto de ayuda.** Acá la diferencia es de **6 tools sobre 20 (30 %)**.

### El corte lectura/escritura, medido por `grep` de efectos de disco en todo `src/`

🟢 **Hay exactamente DOS rutas de escritura en el paquete entero** — `src/commands/items.ts:153,158` (`mkdir` + `writeFile`) y `src/commands/prepare-delivery.ts:56` (`writeFile`). **Todo lo demás sólo lee.** Así que **18 de 20 tools llevan `readOnlyHint: true`**, y es un dato verificado por ausencia de `writeFile`/`mkdir`/`unlink`/`rm` en los otros archivos, no una suposición por el nombre del comando.

| # | Tool MCP | Comando | `inputSchema` (requeridos → opcionales) | `readOnlyHint` |
|---|---|---|---|---|
| 1 | `qti3_parse` | `parse <item.xml>` | `itemFile` | ✅ true |
| 2 | `qti3_parse_dir` | `parse-dir <dir>` | `directory` | ✅ true |
| 3 | `qti3_validate` | `validate <item.xml>` | `itemFile` | ✅ true |
| 4 | `qti3_validate_dir` | `validate-dir <dir>` | `directory` | ✅ true |
| 5 | `qti3_score` | `score <item.xml> --responses <r.json>` | `itemFile`, `responsesFile` | ✅ true |
| 6 | `qti3_score_correct` | `score-correct <item.xml>` | `itemFile` | ✅ true |
| 7 | `qti3_score_correct_dir` | `score-correct-dir <dir>` | `directory` | ✅ true |
| 8 | `qti3_prepare_delivery` | `prepare-delivery …` | `itemFile` → `mode` (**enum** `static`\|`server-materialized-adaptive`), `stateFile`, `outputFile` | 🔴 **false si se pasa `outputFile`; true si no** — ver abajo |
| 9 | `qti3_inspect_package` | `inspect-package <pkg.zip\|dir>` | `packagePath` | ✅ true |
| 10 | `qti3_validate_package` | `validate-package <pkg.zip\|dir>` | `packagePath` | ✅ true |
| 11 | `qti3_basic_item_player_report` | `basic-item-player-report [pkg …]` | — (**variádico**, 0..n rutas) | ✅ true |
| 12 | `qti3_write_fixtures` | `write-fixtures <dir>` | `directory` | 🔴 **false — `mkdir` recursivo + `writeFile`** |
| 13 | `qti3_support_matrix` | `support-matrix` | — (sin argumentos) | ✅ true |
| 14 | `qti3_a11y_proof` | `a11y-proof` | — (sin argumentos) | ✅ true |
| 15 | `qti3_assert_support` | `assert-support` | — (sin argumentos) | ✅ true |
| 16 | `qti3_run_fixtures` | `run-fixtures` | — (sin argumentos) | ✅ true |
| 17 | `qti3_cert_import_basic_items` | `certification import-basic-items` | `qtiRoot` → `validatorReport`, `validatorPackage`, `trustedReportSha256`, `requireValidatorEvidence` (bool) | ✅ true |
| 18 | `qti3_cert_import_basic_tests` | `certification import-basic-tests` | `qtiRoot` | ✅ true |
| 19 | `qti3_cert_verify_validator` | `certification verify-validator` | `validatorReport`, `validatorPackage`, `trustedReportSha256` (**los 3 obligatorios**) | ✅ true |
| 20 | `qti3_cert_check_import_report` | `certification check-import-report` | `qtiRoot`, `savedReport` | ✅ true |

**Las 20 devuelven JSON** (`jsonResult`), así que **el `content` del resultado MCP es el *stdout* sin transformar** y el `isError` se deriva del código de salida. **Cero dependencias de terceros en la cadena** — las 4 dependencias de `qti3-cli@0.13.1` son `@longsightgroup/qti3-{a11y,core,fixtures,conformance}`, **todas de la misma organización y pinneadas a la misma versión exacta** — así que el envoltorio agrega **exactamente una** (el SDK de MCP).

### 🔴 El contrato de estado de `prepare-delivery`, que es lo que hay que documentar o el agente falla

**El pase 35 anotó que el modo adaptativo «exige un objeto de estado con `outcomes`». Medido en `prepareAdaptiveDelivery`, el contrato es más estrecho y rechaza más cosas:**

- El `--state` es un **objeto JSON** que **puede contener SÓLO dos claves: `outcomes` y `templateValues`.** 🔴 **Cualquier otra clave es error duro** — *«may contain only outcomes and templateValues»*. **No es un objeto extensible**, y ahí es donde un agente que agrega metadatos (`sessionId`, `candidate`) se estrella.
- **`outcomes` es obligatorio** y debe ser un objeto de **QTI values** validados uno por uno (`isQtiValue`). `templateValues` es **opcional**, misma validación.
- **Arrays y `null` se rechazan** (`typeof !== object || null || Array.isArray`).
- 🔵 **Y la exclusión mutua que no está en el `USAGE`: `--mode static` junto con `--state` es ERROR de uso.** El estado pertenece sólo al modo adaptativo.
- ⚠️ **La asimetría de respuesta que el envoltorio tiene que reflejar: sin `--out` el resultado JSON INCLUYE `candidateSafeXml`; con `--out` lo OMITE y agrega `outputFile`.** **Son dos formas de respuesta para una sola tool**, y es la razón por la que `readOnlyHint` acá es condicional y no fijo. **La recomendación para el manifiesto: partirla en dos tools** —`qti3_prepare_delivery` (sin `--out`, `readOnlyHint: true`, devuelve el XML en la respuesta) y `qti3_prepare_delivery_to_file` (con `--out`, `readOnlyHint: false`)— porque **una tool cuyo `readOnlyHint` depende de un argumento no se puede gobernar con una política de permisos**, que es justo lo que un cliente de educación va a pedir.

### 🟢 El hallazgo lateral que vale por sí mismo: `certification` trae una primitiva de integridad de cadena de suministro

**`verify-validator` toma `--trusted-report-sha256 <digest>` y verifica el reporte del validador oficial del consorcio contra un digest de confianza**, y `import-basic-items` acepta `--require-validator-evidence` para **exigir** esa evidencia. 🔵 **Es la CUARTA variante de primitiva de seguridad que esta KB encuentra reinventada** (tras el *confirm token* de `openedx-mcp`, las anotaciones + `dryRun` de `coursecode` y el techo de caudal por variable de entorno), **y es de una clase distinta a las tres: las otras tres frenan una ACCIÓN del agente; ésta ancla la CONFIANZA EN UN ARTEFACTO EXTERNO.** Para un expediente de conformidad QTI eso es exactamente lo que un auditor pide: *«¿cómo sé que este reporte de validador es el que publicó el consorcio?»* — y la respuesta es un flag.

### Wiring y estimación

1. **Envoltorio MCP** sobre las 20 entradas de la tabla (21 si se parte `prepare-delivery`), `stdio`, Node 20+. El `dispatch` es `spawn('qti3', [...])` + `JSON.parse` del *stdout*: **las 20 ya emiten JSON**, así que no hay capa de *parsing* que escribir.
2. **Política de permisos**: las 18 de lectura se auto-aprueban; `write-fixtures` y `prepare-delivery_to_file` **requieren confirmación** — y conviene **acotarlas a un directorio de salida configurado**, porque `write-fixtures` hace `mkdir` recursivo sobre la ruta que reciba.
3. **Composición con lo que esta KB ya tiene:** `qti3_validate_package` + `qti3_a11y_proof` producen la **matriz de accesibilidad con guiones VoiceOver/NVDA/JAWS** (el `a11y-proof` devuelve `target` + `interactions` + `manualAssistiveTechnologyScripts`) → **es el insumo del expediente de accesibilidad de P17**; y `coursecode_build` (`enum: cmi5|scorm2004|scorm1.2|lti`) toma la salida para empaquetar al LMS → **P66**.
4. **Estimación: 1-2 semanas** para el envoltorio y su suite de contrato. ⚠️ **El riesgo no es el código, es la versión:** `qti3-cli` publicó **41 releases desde el 2026-05-21** y la última es del **2026-10-01**, así que el manifiesto se pinnea a `0.13.1` y se re-mide el *dispatch* en cada *minor* — **el `switch` es la fuente de verdad, y ya cambió de tamaño respecto de lo que esta KB tenía anotado.**

## P77 — 🔴 Datos educativos públicos de Brasil: la oportunidad es REAL y es un pipeline de ingesta, no un servidor fachada (agregado en el pase 36 del 2026-10-02; **LATAM**)

> **Acción 3 del pase 35, ejecutada — y el resultado cambia la cotización del patrón que el gap 69 insinuaba.**
> **La pregunta era: ¿INEP expone API o sólo descargas?** Respuesta medida: **sólo descargas.**

### Lo que se midió, y con qué control

- 🔴 **`dados.gov.br`, `servicodados.ibge.gov.br`, `api.dados.gov.br` y `www.gov.br` responden 403 a CONNECT** en el registro del proxy, y **`WebFetch` sobre `dados.gov.br` devuelve `EGRESS_BLOCKED`** — **dos instrumentos independientes, mismo resultado.** ✅ **Control negativo corrido, porque el pase 35 pidió declarar el bloqueo en vez de dejarlo implícito:** `registry.npmjs.org` devuelve **200** desde el mismo proceso, así que **la red funciona y el bloqueo es de dominio.** 🔵 **Es la misma clase que el gap 65 (dominio legal europeo), ahora confirmada en el dominio `.gov.br`: las fuentes gubernamentales son inalcanzables por clase desde este entorno.**
- 🟢 **Pero la pregunta se respondió por otro canal, y la respuesta es inequívoca:** la distribución oficial del **Censo Escolar** es **descarga de archivo** — **CSV delimitado por `;` dentro de ZIP, ~2-4 GB comprimidos y 10-20 GB descomprimidos por año**, organizado en **cuatro dimensiones (Escolas, Turmas, Matrículas, Docentes)**, más formato **ASCII con *input files* de SAS y SPSS**. **No hay endpoint REST oficial.**
- 🔴 **La única API de INEP que existe es de terceros, y está muerta:** `inepdadosabertos/api` (**GPL-2.0**, 45 ★, 29 commits) con base `http://api.dadosabertosinep.org/v1`, **cubre sólo IDEB** (censo, SAEB, ENEM figuran como *roadmap* no implementado). ⚠️ **Y su dominio ya no resuelve:** `api.dadosabertosinep.org` → **sin resolución DNS**, *control* corrido en la misma corrida (`github.com` y `registry.npmjs.org` **resuelven**; `dados.gov.br` **resuelve** —su 403 es política, no DNS—; un dominio inventado **no resuelve**, igual que éste). **Está caída, no bloqueada.** 🔴 **Y además es GPL-2.0, así que ni viva serviría como base permisiva.**

### 🔵 Por qué `ibge-br-mcp` pudo existir y un `inep-mcp` no es lo mismo

**El contraste es el hallazgo:** el **IBGE publica API REST** (`servicodados.ibge.gov.br`), y por eso existe `ibge-br-mcp` (**MIT, 24 versiones**) como **servidor fachada**: el MCP traduce *tool call* → HTTP → JSON, sin almacenar nada. **INEP no publica API**, así que **un `inep-mcp` tiene que materializar el dato primero**. ⚠️ **Eso no es una diferencia de esfuerzo, es una diferencia de ARQUITECTURA Y DE RESPONSABILIDAD:** quien lo construye pasa a **alojar y versionar 10-20 GB por año**, con todo lo que eso arrastra (actualización anual, esquema que cambia entre años, y la pregunta de privacidad sobre microdato de matrícula).

### El patrón, y es honesto sobre el plazo

1. **Ingesta** (lo que no se puede evitar): descargar los ZIP anuales del Censo Escolar, normalizar las **cuatro dimensiones**, resolver el **cambio de esquema entre años** —el obstáculo real de los microdatos de INEP— y cargar a un almacén columnar (**DuckDB** o **Postgres**; DuckDB es lo correcto si el entregable es analítico y de una sola máquina).
2. **Capa semántica**: vistas por escola / turma / matrícula / docente, con el **código INEP de escuela** como clave de *join* — que es la clave que ya aparece en portales estaduales (p. ej. el de São Paulo publica *datasets* etiquetados por *Código INEP Escola*, **CC-BY-4.0**), así que **el enriquecimiento estadual es incremental y no requiere renegociar la ingesta**.
3. **Servidor MCP** sobre la capa semántica, **no sobre el CSV**: tools de lectura (`escolas_buscar`, `matriculas_agregar`, `docentes_por_escola`), **todas `readOnlyHint: true`**, con el rail de confirmación de **P61** innecesario porque **no hay escritura**.
4. **Estimación honesta: 8-12 semanas**, de las cuales **la ingesta y el esquema multi-año son 6-8** — contra las **2-3 semanas** que costaría un fachada sobre una API que existiera. 🔵 **Decir esto en el *discovery* es exactamente la «línea de presupuesto escondida» que el pase 35 advirtió, y ahora tiene número.**
5. ⚠️ **Y el pedido que hay que hacer afuera, porque este entorno no puede verificarlo:** confirmar si **`dados.gov.br` expone su API CKAN** (`/api/3/action/package_search`), que es lo habitual en ese portal. **Si la expone, el paso 1 se acorta para los *datasets* que estén publicados ahí** — pero **los microdatos del Censo Escolar se distribuyen igual como archivo**, así que el plazo del pipeline **no cambia**, sólo el descubrimiento.

## 🔴 Auditoría de vitalidad de las dependencias de este archivo (pase 37 del 2026-10-02)

**Treinta y seis pases construyeron recetas citando repos como piezas vivas. Este pase midió si lo son.** Instrumento:
`git ls-remote` + `git fetch --depth 1` del sha de `HEAD` + `git log -1 --format=%cI`, sobre las 49 filas de
`agents/top.md`. **49 de 49 respondieron; ninguna URL está muerta.** Tabla completa en `repos/trending.md` (pase 37).

🔵 **La regla de lectura, antes de los números: una dependencia congelada no es una dependencia inválida.** Lo que cambia
es **quién paga el mantenimiento**, y eso pertenece a la propuesta. Las tres piezas de abajo siguen siendo **lo mejor
disponible en permisivo** para lo que hacen.

### Las tres dependencias load-bearing que están paradas

| Pieza | Licencia | `HEAD` | Patrones afectados | Diagnóstico y qué se escribe en la propuesta |
|---|---|---|---|---|
| 🔴 **`DavidLMS/learnmcp-xapi`** | **MIT** | **2025-08-29** (13,1 m) | **P4**, **P15**, **P67**, **P68**, **P69** — **42 menciones en este archivo** | **Una sola rama**: el 2025-08-29 es final, no hay desarrollo escondido. 🟢 **Mitigante fuerte: son 3 tools (1 escribe, 2 leen) sobre `xAPI 1.0.3`, que es un estándar cerrado de 2013.** La superficie más chica de toda esta KB sobre un contrato que no se mueve. **Se propone, con una línea de mantenimiento explícita** |
| 🔴 **`trilogy-group/oneroster-ts`** | **0BSD** | **2025-06-27** (15,2 m) | **P58**, **P60**, **P64** | **132 tools (72 lectura / 60 escritura)** y **quince meses sin que un humano mergee**. Las 5 ramas nuevas son **4 de dependabot + 1 regenerador de SDK**. 🟢 **Mitigante decisivo: es 0BSD — la licencia más permisiva que existe, se forkea sin ninguna obligación.** 🔴 **Sin reemplazo:** el único candidato activo (`@timeback/oneroster`) **no declara licencia** (**gap 75**). **Se propone con fork propio cotizado** |
| 🔴 **`peancor/moodle-mcp-server`** | **MIT** | **2026-02-22** (7,3 m) | **P54**, **P55** | **8 tools, 4 de escritura**, entre ellas `provide_assignment_feedback` y `provide_quiz_feedback`: **es el único artefacto permisivo de esta base que pone nota y devolución dentro de un LMS de producción** — el tramo final del **gap 6**. ⚠️ **Siete meses es frío, no muerto.** 🟢 **Hay alternativa viva para la parte de lectura:** `bunizao/moodle-cli` (**2026-10-02**) y `MarcosNahuel/moodle-mcp` (2026-05-03). **Se propone; la escritura es el tramo a mantener** |

### 🟢 Lo que la auditoría confirma sano, y es la mayoría

| Receta | Piezas verificadas vivas |
|---|---|
| **P67** / **P68** (telemetría) | 🟢 `lrsql` **Apache-2.0, v0.9.9 del 2026-10-01**; **Ralph** MIT vivo en `main` — **las dos patas de almacenamiento están bien** |
| **P54** / lectura de Moodle | 🟢 `bunizao/moodle-cli` **2026-10-02** (el más activo de la capa), `MarcosNahuel/moodle-mcp` 2026-05-03 |
| Canvas (transversal) | 🟢 `bruchris/canvas-lms-mcp` **2026-09-20** (165 tools), `vishalsachdev/canvas-mcp` **2026-10-01** |
| **P56** (SCORM) | 🟢 `giacomomaria81/scorm-mcp-server` **2026-09-03** |
| **P66** / **P69** / **P76** (QTI) | 🟢 `@longsightgroup/qti3-cli` MIT, última modificación **2026-10-01** |
| **P16** / **P12** (*knowledge tracing*) | 🟢 **`pykt-team/pykt-toolkit` vivo: `HEAD` 2026-09-22** — ⚠️ **el pase 36 lo había declarado abandonado leyendo sólo PyPI; es falso** |
| **P63** (autoría Open edX) | 🔴 `openedx-mcp` AGPL-3.0, **gap 68** sin cambios (12 releases en 2 días, nada en 70) |

### 🔵 La regla de método que esta auditoría deja para todos los pases siguientes

**Antes de citar un repo como pieza viva en una receta, fechar el tip de su rama por defecto.** Y **no** el ref más nuevo:
`oneroster-ts` y `educhain` tienen refs de hace 4 y 5 meses que son **ramas de bot y de agente sin mergear**
(**gap 72**, tendencia **124**). El «último tag» tampoco sirve donde los nombres de tag son heterogéneos
(**gap 73**).

## 🔄 Corrección del pase 38 (2026-10-02) a la auditoría del pase 37 y a la premisa de **P78** — dos de las tres dependencias congeladas SÍ tienen reemplazo vivo

🔴 **La premisa que hay que corregir, porque está escrita en este archivo y es la que decide si se cotiza un fork:** la
auditoría del pase 37 y el enunciado de **P78** afirman que las tres dependencias congeladas *«no tienen reemplazo
vivo»*. **Se fue a buscar, y dos de las tres sí lo tienen.** El pase 37 midió vitalidad pero **no buscó sucesión**:
diagnosticar no es reemplazar, y la diferencia vale dos patrones.

| Pieza congelada | Qué decía el pase 37 | Qué midió el pase 38 | Efecto sobre **P78** |
|---|---|---|---|
| 🟢 `peancor/moodle-mcp-server` | *«único permisivo que escribe nota y devolución en un LMS»* (gap 6) | **FALSO desde hoy: hay tres MIT vivos** — `toshieji/moodle-grading-mcp` (9 tools, nota en borrador), `NiccoloSalvini/mcp-moodle-teacher` (22 tools), `Dymayo/moodler-mcp` | 🔴 **Sale de P78.** No se cotiza fork: **se migra**. Ver **P79** |
| 🟢 `trilogy-group/oneroster-ts` | *«único SDK OneRoster con MCP y escritura»* | **Parcialmente falso: hay servidor Apache-2.0 vivo** (`Ed-Fi-Alliance-OSS/edfi-oneroster`, `HEAD` 2026-10-01) **y cliente MIT vivo** (`TCI/OneRoster`, Ruby). 🔴 **Sigue siendo el único cliente en TypeScript** | ⚠️ **Sale de P78 salvo que el requisito sea TypeScript.** Ver **P80** |
| 🔴 `DavidLMS/learnmcp-xapi` | *«la única puerta»* (gap 64) | **CONFIRMADO: sigue sin sucesor.** El fork `ashleycribb` está **2 commits adelante y los dos son config de Cloud Run** | 🟢 **P78 se mantiene, y ahora tiene su caso medido.** Ver **P81** |

🔵 **Lo que esto le hace a P78 como patrón: lo mejora.** P78 era una receta para tres piezas y resulta que **dos no la
necesitaban**. Queda para **una**, con la premisa verificada en serio —se buscó sucesión y no hay— y con el riesgo
dimensionado: son **~32 commits de adaptador delgado** sobre dos LRS vivos e intercambiables por configuración. **Un
patrón que se aplica a una pieza con la premisa probada vale más que uno que se aplicaba a tres por falta de búsqueda.**

⚠️ **Y la regla de proceso que deja, para esta base:** **toda auditoría de vitalidad tiene que ir seguida de un barrido
de sucesión antes de que sus conclusiones entren a un patrón.** Medir que algo está frío y concluir que no tiene
reemplazo son dos afirmaciones distintas, y la segunda necesita su propia búsqueda (`gap 78`).

## P78 — Adoptar una dependencia congelada a propósito: el fork mínimo con contrato de mantenimiento, para las piezas que no tienen reemplazo (agregado en el pase 37 del 2026-10-02; **transversal, y es el patrón que vuelve proponibles las tres piezas auditadas arriba**)

**El problema que resuelve, y es el que este pase destapó.** Tres de las dependencias más valiosas de esta base están
congeladas: `learnmcp-xapi` (13,1 m), `oneroster-ts` (15,2 m) y `peancor/moodle-mcp-server` (7,3 m). **Las tres son
permisivas, las tres hacen exactamente lo que la receta necesita, y ninguna tiene reemplazo vivo.** La respuesta honesta
no es esconderlo ni descartarlas: es **cotizar la adopción**.

🔵 **Y la condición que lo hace viable está medida: las tres son MIT o 0BSD.** `oneroster-ts` es **0BSD**, que **no exige
ni conservar el aviso de copyright** — el fork no tiene costo legal alguno. Las dos MIT exigen conservar el aviso y nada más.

### Las piezas, con su estado verificado el 2026-10-02

| Pieza | Licencia | `HEAD` | Superficie | Por qué no se reemplaza |
|---|---|---|---|---|
| `DavidLMS/learnmcp-xapi` | **MIT** | 2025-08-29 | **3 tools** (1 escribe / 2 leen) | **Única puerta MCP de xAPI** (gap 64, cerrado en negativo con tres instrumentos: ningún LRS publica puerta propia) |
| `trilogy-group/oneroster-ts` | **0BSD** | 2025-06-27 | **132 tools** (72/60) | Único SDK OneRoster con MCP y escritura. `@timeback/oneroster` **sin licencia** (gap 75) |
| `peancor/moodle-mcp-server` | **MIT** | 2026-02-22 | **8 tools, 4 escriben** | Único permisivo que **escribe nota y devolución** en un LMS (gap 6) |

### El wiring, que es de proceso y no de código

1. **Fork en la organización del cliente, no en la de Globant** — y se dice por qué: **el cliente se queda con la pieza al
   final del proyecto**, que es lo que convierte la dependencia congelada de riesgo en activo. Con 0BSD y MIT no hay
   obligación de republicar.
2. **Fijar la versión por sha, no por tag.** `learnmcp-xapi` tiene 2 tags y el último es de 2025-06-02, **anterior** a su
   propio `HEAD` (2025-08-29): **el tag no es el código que se quiere**. Es el caso concreto del **gap 73**.
3. **Suite de contrato antes de tocar nada:** para cada pieza, un test por tool que fije la forma de entrada y de salida.
   🟢 **En `learnmcp-xapi` esto cuesta casi nada: son 3 tools**, y el contrato de abajo es **xAPI 1.0.3**, un estándar
   cerrado. En `oneroster-ts` son **132 tools**, así que se fija **sólo el subconjunto que la receta usa** — típicamente
   las 20-30 de rostering y matrícula de **P64** — y el resto se deja sin cubrir **declarándolo**.
4. **Reproducir el build y publicar el artefacto al registro privado del cliente**, para no depender de que el upstream
   siga publicando. ⚠️ **En `learnmcp-xapi` esto es obligatorio y no opcional: la pieza no está en ningún registro**
   (PyPI 404, npm `total: 0`) — **se instala desde el código fuente**, que es el hallazgo del pase 33.
5. **Mantener los rails de escritura al adoptar, y si no los tiene, agregarlos:** el patrón de **P61** (dry-run +
   *confirm token* atado a una huella del payload + auditoría *append-only* previa a la escritura). 🔴 **Las tres piezas
   escriben y ninguna de las tres trae los cuatro rails de `openedx-mcp`** — es el tramo que el fork justifica por sí solo.
6. **Ofrecer la contribución *upstream* una vez, y seguir sin esperarla.** Los tres repos tienen *issues* abiertos; un PR
   con la suite de contrato es barato y, si entra, el fork se vuelve innecesario. **Pero el plan no depende de eso**, que es
   la diferencia entre este patrón y «esperamos que el mantenedor vuelva».

### Plazo y alcance

| Pieza | Fork + contrato + publicación | Rails de **P61** si faltan |
|---|---|---|
| `learnmcp-xapi` (3 tools) | 🟢 **1-2 semanas** | +1 semana |
| `peancor/moodle-mcp-server` (8 tools, 4 escriben) | **2-3 semanas** | +1-2 semanas |
| `oneroster-ts` (subconjunto de 20-30 tools) | **3-4 semanas** | +2 semanas |

🔵 **Es la estimación que hay que poner en la propuesta en vez del supuesto «la dependencia existe y se mantiene sola».**
Sobre un proyecto de **P67** de 10-12 semanas, adoptar `learnmcp-xapi` son **1-2 semanas de las diez**: visible, chico y
defendible — **y es exactamente el costo que aparece en la semana 6 si no se escribió antes.**

### Dónde se vende primero

- 🟢 **North America**, donde el estándar contractual de Microsoft/AFT (vigente desde el 1.º de noviembre) obliga a
  supervisión humana y a no usar dato de alumno para entrenar: **un expediente que nombra sus dependencias y quién las
  mantiene es parte del cumplimiento**, no un extra.
- 🟢 **EMEA**, donde el Anexo III (**2027-12-02**) exige trazabilidad y gestión de riesgo del sistema: **una dependencia
  congelada sin plan de mantenimiento es un hallazgo de auditoría**; con **P78** es un control documentado.
- ⚠️ **LATAM y APAC**: se vende igual, pero el argumento es de continuidad operativa y no regulatorio.

## P79 — Corregir dentro de Moodle con la nota en BORRADOR: la receta que convierte el requisito regulatorio en el comportamiento por defecto del servidor (agregado en el pase 38 del 2026-10-02)

**El problema que resuelve.** Un cliente institucional quiere que la AI ayude a corregir, y su regulador —AI Act en EMEA,
reglas estatales en North America, Vietnam y Corea en APAC— exige **supervisión humana** sobre la evaluación del alumno.
La respuesta habitual es una cláusula en la propuesta. **Esta receta la pone en el software**, y reemplaza la pieza que
el pase 37 encontró congelada hace 7,3 meses (`peancor/moodle-mcp-server`, **P54**/**P55**).

### Las piezas, todas verificadas el 2026-10-02

| Rol | Pieza | Licencia | `HEAD` |
|---|---|---|---|
| LMS | **Moodle** (`moodle/moodle`) | GPL-3.0 — es el host, no se linkea | — |
| Puerta de corrección | **`toshieji/moodle-grading-mcp`** | **MIT** ✅ | **2026-09-07** |
| Superficie docente amplia (opcional) | **`NiccoloSalvini/mcp-moodle-teacher`** | **MIT** ✅ | **2026-09-25** |
| Telemetría del proceso (opcional) | `yetanalytics/lrsql` (Apache-2.0) o `openfun/ralph` (MIT) | permisivas ✅ | **2026-10-01** / 2026-09-07 |

### El wiring

1. **Habilitar en Moodle las 8 funciones de Web Services que la puerta requiere**, y sólo esas:
   `core_webservice_get_site_info`, `core_course_get_courses_by_field`, `core_course_get_contents`,
   `mod_assign_get_assignments`, `mod_assign_get_submissions`, `mod_assign_get_grades`,
   `mod_assign_get_submission_status`, `mod_assign_save_grade`. ⚠️ **En Moodle 5.x el *webroot* es `public/`**: ver la
   advertencia del pase 19 en `verticals/solutions.md` antes de escribir una sola ruta.
2. **Crear el token de servicio con el rol más chico que cubra esas ocho** — no un token de admin.
3. **Configurar la puerta en modo lectura primero:** sin `MOODLE_ALLOW_WRITE=1` **no puede escribir nada**. Se demuestra
   el circuito completo de lectura (`list_pending`, `get_submission`, `read_submission_file`, `read_submission_images`)
   **antes** de habilitar escritura.
4. **Habilitar escritura con allowlist explícita de IDs de curso** — empezar por **un** curso piloto. Lista vacía = no
   escribe; esa es la posición segura por defecto, y es la que se deja en los entornos que no son el piloto.
5. **La nota la decide el modelo, la escribe el servidor y queda en `workflowstate=readyforreview`:** graduada y **NO
   publicada**, **sin notificación al alumno**. 🟢 **El docente sigue siendo el único que publica, porque el servidor no
   sabe hacerlo.**
6. **Dejar el pie de declaración de asistencia por AI activado** (viene por defecto) y **conservar el audit trail JSONL**
   como evidencia: es el artefacto que se le entrega al auditor.
7. **Si hace falta más que corregir** —asistencia, anuncios, alumnos en riesgo— se compone `mcp-moodle-teacher` al lado
   (22 tools, con confirmación obligatoria en las 3 de escritura), **no se reemplaza** la puerta de corrección: la que
   tiene las garantías de nota en borrador es la de `toshieji`.
8. **Opcional, y es lo que cierra el expediente:** emitir un statement xAPI por cada corrección asistida hacia `lrsql` o
   `ralph`, para tener la serie temporal de *qué propuso la AI y qué publicó el docente*. Eso es **P4**/**P68** enchufado
   acá, y es la métrica que prueba la supervisión humana en vez de afirmarla.

🔵 **Lo que se escribe en la propuesta:** *«el sistema no puede publicar notas»*. No *«el sistema está configurado para
no publicar notas»*. La diferencia la sostiene el código, y es verificable por el cliente en el README.

⚠️ **Lo que NO entra en esta receta:** `csmediapro/moodle-mcp-server` —**AGPL-3.0**, y es el más activo de la capa, así
que va a aparecer primero en cualquier búsqueda— y `loyaniu/moodle-mcp`, **sin archivo de licencia** (8 rutas probadas,
8 × 404).

## P80 — Rostering OneRoster sin escribir un cliente: servir el estándar desde el Ed-Fi ODS que el distrito ya tiene (agregado en el pase 38 del 2026-10-02)

**El problema que resuelve.** Las recetas **P58**, **P60** y **P64** de esta base consumen OneRoster con
`trilogy-group/oneroster-ts`, que está **congelado hace 15,2 meses** y cuyo único movimiento en ese tiempo fueron cuatro
ramas de Dependabot sin mergear. Y hay un problema anterior: en un distrito norteamericano el dato **no está en
OneRoster**, está en **Ed-Fi ODS**, así que la receta vieja suponía un traductor que nadie escribió — `EASOL/edfi-to-oneroster`
lo intentó y lo abandonó **hace 10 años**.

### Las piezas, verificadas el 2026-10-02

| Rol | Pieza | Licencia | `HEAD` | Nota |
|---|---|---|---|---|
| Fuente | **Ed-Fi ODS** del distrito | — | — | Ya desplegado en el cliente: **no se cotiza** |
| **Proveedor OneRoster** | **`Ed-Fi-Alliance-OSS/edfi-oneroster`** | **Apache-2.0** ✅ | **2026-10-01** | **14 endpoints GET**, OneRoster 1.2, Ed-Fi DS 4.0 y 5.0/5.1/5.2, **86 tags**, v1.0.2 |
| Consumidor (Ruby) | **`TCI/OneRoster`** | **MIT** ✅ | **2026-09-11** | v2.3.27, rubygems |
| Consumidor (TypeScript) | 🔴 `trilogy-group/oneroster-ts` | 0BSD | 🔴 2025-06-27 | **Congelado. No tiene sucesor** → si el requisito es TS, aplica **P78** sólo a esta pieza |
| Competencias / alineación | `cassproject/CASS`, `1EdTech/OpenCASE` | Apache-2.0 | — | Como en **P50**, **P57**, **P60** |

### El wiring

1. **Levantar `edfi-oneroster` con Docker apuntando al ODS del cliente** — hay guía de stack completo en el repo; también
   IIS/Windows si el distrito es Microsoft-shop. **Verificar primero la versión del Data Standard**: soporta **4.0 y
   5.0/5.1/5.2**, y el ODS del cliente puede estar en otra.
2. **Validar los 14 endpoints GET contra el ODS real** antes de prometer superficie: `academicSessions`, `classes`,
   `courses`, `demographics`, `enrollments`, `orgs`, `users`, `schools`, `students`, `teachers`, `gradingPeriods`,
   `terms` y recuperación por id. Usar `fields` y `filter` para no traer de más, y `limit`/`offset` para paginar.
3. 🔴 **Decir en voz alta que es de SÓLO LECTURA.** Son 14 endpoints **GET**. El rol de escritura que `oneroster-ts`
   cubría con sus 60 tools de escritura **no lo cubre esta pieza**: si la receta necesita escribir rostering, eso sigue
   abierto y hay que cotizarlo aparte.
4. **Elegir el consumidor por lenguaje, no por costumbre:** en Ruby, `TCI/OneRoster` y se termina. En TypeScript **no hay
   opción viva**: o se asume `oneroster-ts` con **P78** (fork mínimo, 0BSD, sin obligación ni de conservar el aviso), o se
   consume la API HTTP directamente —que es lo razonable, porque del otro lado ahora hay un servidor estándar y no una
   librería.
5. **Componer con la capa de competencias** (`CASS`/`OpenCASE`) como en **P60**: el rostering da *quién está en qué*, la
   capa de competencias da *qué debería saber*.

⚠️ **Las dos cosas que no hay que prometer.** (1) **Certificación 1EdTech: el repo no la declara.** Es implementación de
referencia permisiva, y ante un distrito esa distinción se hace. (2) **Cuál de `Ed-Fi-Alliance-OSS/edfi-oneroster` y
`CSR2017/edfi-oneroster` es upstream no está resuelto** (`gap 79`): citar el de la Alliance, que tiene 86 tags y commit
de ayer.

🔵 **El cambio de encuadre que esta receta habilita, y es el que se vende:** OneRoster deja de ser *«una librería que hay
que envolver»* y pasa a ser **una plataforma que se despliega** sobre datos que el cliente ya tiene. Lo que se cotiza es
la capa de AI arriba del estándar, no el plomería del estándar.

## P81 — La puerta xAPI congelada, propuesta con el riesgo acotado por medición en vez de por promesa (agregado en el pase 38 del 2026-10-02)

**El problema que resuelve.** `DavidLMS/learnmcp-xapi` tiene **42 menciones en este archivo** —es la puerta xAPI de
**P4**, **P15**, **P67**, **P68** y **P69**— y está **congelada hace 13,1 meses, con una sola rama**. Es la única de las
tres piezas del pase 37 que **sí** confirmó no tener sucesor. Esta receta es **P78 aplicado a ella**, con la diferencia
de que ahora el riesgo está medido y se puede decir en números.

### Las tres mediciones que convierten el riesgo en una cifra

| Medición | Valor | Por qué importa en la propuesta |
|---|---|---|
| Tamaño de lo congelado | **~32 commits**, **3 tools** (1 escribe / 2 leen), 1 sola rama | **Es un adaptador delgado, no un sistema.** Es auditable en una tarde y mantenible por una persona |
| Dónde vive el dato | **En el LRS, no en el adaptador** | Si la puerta se abandona, **el dato del cliente no está atrapado en ella** |
| Vitalidad de la capa de abajo | `yetanalytics/lrsql` **Apache-2.0, `HEAD` 2026-10-01, v0.9.9** · `openfun/ralph` **MIT, v5.0.1, `HEAD` 2026-09-07** | **Dos LRS vivos, permisivos, de organizaciones distintas y regiones distintas** (una pública europea) |

🔵 **Y el dato que cierra el argumento:** la **v2.0.0 de `learnmcp-xapi` trae sistema de plugins de LRS** (SQLite, Ralph,
Veracity). **El LRS se cambia por variable de entorno, no por fork.** Es decir: la pieza congelada es intercambiable por
abajo y chica por dentro.

### El wiring

1. **Fork mínimo en la organización del CLIENTE** (no en la de Globant), como manda **P78**: MIT, basta conservar el aviso.
2. **Fijar el commit** `fbf6091` —el tip real del upstream, 2025-08-29— y partir de ahí. ⚠️ **No partir del fork
   `ashleycribb`**: está 2 commits adelante y los dos son **configuración de Cloud Run**, no mantenimiento. Si el
   despliegue es en GCP, **esos 2 commits sí sirven y se cherry-pickean a sabiendas de qué son**.
3. **Elegir el LRS por región y por argumento, no por costumbre:** en EMEA, `openfun/ralph` —**MIT y de una entidad
   pública francesa**, que es el argumento de soberanía de **P68**—; en North America o cuando el cliente quiere correr
   sobre su base existente, `yetanalytics/lrsql` sobre Postgres/MySQL/MariaDB/SQLite.
4. **Dejar el plugin de LRS configurado por entorno**, no hardcodeado: es lo que hace que cambiar de LRS no toque la
   puerta.
5. **Cotizar el mantenimiento explícito** —ventana de respuesta, quién actualiza dependencias, qué pasa si la spec xAPI
   cambia— y entregarlo **como control documentado**: en EMEA, una dependencia congelada sin plan de mantenimiento es un
   hallazgo de auditoría; **con plan, es un control**.
6. **Vigilar el upstream con el instrumento del pase 38, no con la fecha de `main`:** `git ls-remote` para los refs, y
   **contar commits adelante/atrás** antes de concluir que alguien lo retomó. Un `main` más nuevo puede ser una receta de
   despliegue (`gap 78`).

🟢 **Lo que esto le da a la conversación:** en vez de *«usamos una librería que no se actualiza»*, se dice **«usamos un
adaptador de 32 commits del que somos dueños, sobre un LRS mantenido por una entidad pública europea, intercambiable por
configuración»**. Es la misma dependencia; el riesgo es el mismo; **la diferencia es que está medido**.


## P85 — El *gateway* de allowlist de tools, **escrito y probado**: la pieza que P82 describía en prosa (agregado en el pase 40 del 2026-10-02)

**P82 (pase 39) describió el patrón y dejó la pieza por escribir.** Este pase la escribe y **la prueba**, que es la
diferencia entre un patrón y un entregable. **175 líneas, sólo biblioteca estándar de Python, sin dependencias.**

### El problema, en una frase

Esta base tiene **nueve puertas de LMS** y varias traen escritura sin partición por rol. La peor es
**`frappe-mcp-server`**, que expone **`call_method`** (ejecuta métodos arbitrarios *whitelisted* del servidor) y
**`delete_document`** (borra) sobre un ERP académico. **La tendencia 137 probó, con el patrón `preview_*` de
`mcp-usc`, que un filtro por nombre de tool es un control de cumplimiento real y no cosmético.** Lo que faltaba era
la pieza intermedia.

### Las dos decisiones de diseño que lo vuelven un control y no un adorno

🔴 **1. El filtro se aplica en DOS puntos, no en uno.** Recortar `tools/list` **no es un control**: un cliente que ya
conoce el nombre —de una versión anterior, de la documentación o por adivinanza— puede invocar una tool no listada.
**El segundo punto, `tools/call` rechazado por nombre antes de reenviar, es el que convierte el patrón en control.**

🔴 **2. *Default deny*.** Allowlist vacía ⇒ **cero tools**. Un *gateway* que falla abierto no es un *gateway*.

**Y dos decisiones menores que importan:** la allowlist es **por nombre exacto, sin globs ni prefijos** —así
`preview_submit_assignment` no habilita `submit_assignment` y `delete_*` no entra por accidente—, y **cada rechazo se
escribe como una línea JSON con timestamp**, porque sin registro no hay nada que mostrarle a un auditor y ésa es la
razón de existir de la pieza.

### El código

```python
#!/usr/bin/env python3
"""mcp-allowlist-gateway — proxy MCP stdio que reexporta SOLO las tools de una
allowlist y registra cada llamada bloqueada."""
import json, os, subprocess, sys, threading, time

ALLOW = frozenset(t.strip() for t in os.environ.get("MCP_ALLOWLIST", "").split(",") if t.strip())
AUDIT_LOG = os.environ.get("MCP_AUDIT_LOG", "").strip()
_lock = threading.Lock()

def audit(event, **fields):
    rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "event": event, **fields}
    line = json.dumps(rec, ensure_ascii=False)
    with _lock:
        if AUDIT_LOG:
            try:
                with open(AUDIT_LOG, "a", encoding="utf-8") as fh:
                    fh.write(line + "\n")
                return
            except OSError:
                pass            # si el log falla, el evento no se pierde: cae a stderr
        print(line, file=sys.stderr, flush=True)

def deny(req_id, name):
    # -32601 (Method not found) y no -32602: para el cliente, la tool NO EXISTE
    # en este servidor, que es exactamente lo que el gateway quiere afirmar.
    return {"jsonrpc": "2.0", "id": req_id,
            "error": {"code": -32601,
                      "message": f"Tool '{name}' no expuesta por este gateway",
                      "data": {"allowed": sorted(ALLOW)}}}

def main():
    argv = sys.argv[1:]
    if argv and argv[0] == "--":
        argv = argv[1:]
    if not argv:
        print("uso: gateway.py -- <comando del servidor upstream>", file=sys.stderr)
        return 2
    audit("gateway_start", upstream=argv, allowlist=sorted(ALLOW))
    up = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                          stderr=None, text=True, bufsize=1)
    pending, plock = set(), threading.Lock()

    def c2u():                                   # cliente -> upstream
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
            except json.JSONDecodeError:
                up.stdin.write(line + "\n"); up.stdin.flush(); continue
            m = msg.get("method")
            if m == "tools/list":
                with plock:
                    pending.add(json.dumps(msg.get("id")))
            elif m == "tools/call":
                name = (msg.get("params") or {}).get("name", "")
                if name not in ALLOW:            # PUNTO 2: el control real
                    audit("tool_call_blocked", tool=name, request_id=msg.get("id"))
                    sys.stdout.write(json.dumps(deny(msg.get("id"), name)) + "\n")
                    sys.stdout.flush(); continue
                audit("tool_call_allowed", tool=name, request_id=msg.get("id"))
            up.stdin.write(json.dumps(msg) + "\n"); up.stdin.flush()
        try:
            up.stdin.close()
        except OSError:
            pass

    def u2c():                                   # upstream -> cliente
        for line in up.stdout:
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
            except json.JSONDecodeError:
                sys.stdout.write(line + "\n"); sys.stdout.flush(); continue
            key = json.dumps(msg.get("id"))
            with plock:
                is_list = key in pending
                if is_list:
                    pending.discard(key)
            if is_list and isinstance(msg.get("result"), dict):
                tools = msg["result"].get("tools")
                if isinstance(tools, list):      # PUNTO 1: recorte del listado
                    kept = [t for t in tools if t.get("name") in ALLOW]
                    dropped = [t for t in tools if t.get("name") not in ALLOW]
                    msg["result"]["tools"] = kept
                    audit("tools_list_filtered",
                          exposed=[t.get("name") for t in kept],
                          withheld=[t.get("name") for t in dropped],
                          upstream_total=len(tools))
            sys.stdout.write(json.dumps(msg) + "\n"); sys.stdout.flush()

    threading.Thread(target=c2u, daemon=True).start()
    t2 = threading.Thread(target=u2c, daemon=True); t2.start()
    rc = up.wait(); t2.join(timeout=2)
    audit("gateway_stop", upstream_returncode=rc)
    return rc

if __name__ == "__main__":
    sys.exit(main())
```

### El wiring

```bash
MCP_ALLOWLIST=get_document,list_documents,get_doctype_schema \
MCP_AUDIT_LOG=./mcp-blocked.jsonl \
python3 mcp_allowlist_gateway.py -- npx -y frappe-mcp-server
```

En la configuración del cliente MCP, el servidor pasa a ser **el gateway**, y el upstream real queda detrás.

### 🟢 La verificación, que es lo que distingue esto de P82

**Probado contra un upstream que imita la superficie de `frappe-mcp-server`** (7 tools: `get_document`,
`list_documents`, `get_doctype_schema`, `update_document`, `delete_document`, `call_method`, `create_document`):

| Prueba | Resultado medido |
|---|---|
| `tools/list` con allowlist de 3 | 🟢 **7 → 3 expuestas** (`get_document`, `list_documents`, `get_doctype_schema`) |
| `tools/call` de una tool permitida | 🟢 **llega al upstream y ejecuta** |
| `tools/call` de `delete_document` **sin listarla** | 🟢 **`-32601`, y NO llega al upstream** |
| `tools/call` de `call_method` **sin listarla** | 🟢 **`-32601`, y NO llega al upstream** |
| Ejecuciones totales en el upstream | 🟢 **1** — sólo la permitida |
| Allowlist **vacía** (`MCP_ALLOWLIST=""`) | 🟢 **0 tools expuestas, las 3 llamadas bloqueadas** (*default deny*) |
| `initialize` y el resto del protocolo | 🟢 **pasa sin tocarse** |

**Y el log que queda, que es el entregable para el auditor:**

```json
{"event":"tools_list_filtered","upstream_total":7,
 "exposed":["get_document","list_documents","get_doctype_schema"],
 "withheld":["update_document","delete_document","call_method","create_document"]}
{"event":"tool_call_blocked","tool":"delete_document","request_id":4}
{"event":"tool_call_blocked","tool":"call_method","request_id":5}
```

### Dónde se aplica primero, por orden de urgencia

| Pieza | Por qué | Allowlist sugerida |
|---|---|---|
| 🔴 **`frappe-mcp-server`** | `call_method` + `delete_document`, **sin partición por rol**, sobre ERP académico | sólo las 10 de lectura y esquema |
| 🔴 **`DUTIC-mcp`** | **ninguna de sus 12 tools declara `readOnlyHint`**, y `dutic_encuesta_fill_all` + `_submit` envían una encuesta institucional en nombre del alumno | las 4 de semestre + `dutic_pdf_to_markdown` + las 2 de biblioteca |
| ⚠️ **`bruchris/canvas-lms-mcp`** | **48 tools con `destructiveHint: true`** sobre 165 | las 120 `readOnlyHint` |
| ⚠️ **`moodler-mcp`** | `save_assignment_grade` con `workflowstate=""` **publica la nota** | las 30 de lectura |

⚠️ **Dos límites, declarados.** (1) **Es un control de superficie, no de autorización**: no sustituye los permisos del
LMS ni el rol del token — una tool permitida sigue pudiendo hacer todo lo que el token permita. (2) **Cubre transporte
stdio.** Para un upstream HTTP el mismo filtro aplica en un *reverse proxy*, pero **ese código no está escrito ni
probado en este pase** y no hay que presentarlo como si lo estuviera.

## P86 — *Student success* sin construir el modelo: adoptar el pipeline MIT que ya trae el expediente regulatorio (agregado en el pase 40 del 2026-10-02)

**El patrón que la tendencia 148 vuelve posible, y reemplaza lo que esta base venía diciendo sobre esta capa.** Hasta
el pase 39, la capa predictiva se cotizaba como desarrollo: el **gap 26** la declaraba *«la peor abastecida»* y los
110 repos de *knowledge tracing* no eran productos. **Ya no se construye: se adopta.**

### Las piezas, verificadas el 2026-10-02

| Pieza | Licencia | Rol | Estado medido |
|---|---|---|---|
| [`datakind/student-success-tool`](https://github.com/datakind/student-success-tool) | 🟢 **MIT** (`LICENSE.md` del árbol) | **El pipeline entero**: esquema, ingesta, *features*, EDA, *targets*, AutoML, reporting | `HEAD` **2025-09-08**, PyPI 0.3.10, **181 archivos `.py`** ⚠️ ~13 meses |
| `reporting/model_card/` + `reporting/sections/bias_sections.py` | (dentro de la anterior) | 🟢 **El expediente**: *model card* generada del modelo + análisis de sesgo | En el árbol |
| `ingestion_validation/` + `generation/pdp/` | (dentro de la anterior) | Validación de ingesta + **datos sintéticos** | En el árbol |
| `bruchris/canvas-lms-mcp` **o** una puerta de Moodle de esta base | **MIT** | La fuente de señal del LMS, si el cliente no tiene PDP | `HEAD` 2026-09-20 |
| **P85** (*gateway* de allowlist) | — | Recortar la puerta del LMS a **sólo lectura** para alimentar el modelo | 🟢 **probado en este pase** |

### El wiring

1. **Decidir el esquema, y es la bifurcación que define el presupuesto.** Si el cliente es un *college*
   estadounidense dentro del **Postsecondary Data Partnership**, el esquema base sirve tal cual: `dataio/schemas/pdp/`
   ya modela cohortes, cursos y términos. **Si no**, se usa la ruta **`custom/`** que el repo trae paralela a cada
   `pdp/` (en `dataio/`, `preprocessing/`, `reporting/sections/`, `pipelines/`) y **se escribe el esquema del
   cliente**. 🔵 **La customización está prevista por diseño, no es un fork.**
2. **Alimentar la señal.** Con PDP, el dato ya viene. Sin PDP, la señal de compromiso se lee del LMS con una puerta
   MIT **recortada a lectura con P85** — y eso, además de prudente, es el argumento de privacidad: **el modelo nunca
   recibe una tool que escriba**.
3. **Demostrar sin dato real de alumno.** `generation/pdp/` produce datos sintéticos. 🔵 **Es lo que destraba el
   piloto**: se muestra el pipeline completo, el *model card* y el reporte de sesgo **antes** de firmar el acuerdo de
   tratamiento de datos.
4. **Entrenar y evaluar** con el AutoML configurado por `config.yaml`, en los puntos de control que
   `preprocessing/checkpoints/` define.
5. **Emitir el expediente, que es el entregable.** *Model card* del modelo entrenado + secciones de sesgo, atributos,
   métricas y evaluación. **Esto no es documentación del proyecto: es el artefacto que contesta al regulador.**
6. **Cerrar con el humano en el lazo, y decirlo así.** El README del proyecto lo declara —*«humans in the loop by
   design»*, las intervenciones las ejecuta un asesor— y **eso es exactamente lo que exigen Oklahoma y Maryland**
   (supervisión humana, prohibición de que la AI decida en alto impacto). **En EMEA es la base del expediente del
   Anexo III punto 3, cuyo plazo es el 2027-12-02.**

### Cómo se cotiza, por región

| Región | Qué es | Por qué |
|---|---|---|
| **North America** | 🟢 **casi reuso** | PDP es su estándar y Databricks es común. Se cotiza adaptación + expediente |
| **EMEA** | **adopción del armazón + esquema propio** | No hay PDP. 🔵 **Pero es la región donde el expediente vale más**, porque el Anexo III lo va a pedir |
| **APAC / LATAM** | **adopción del armazón + esquema propio** | 🔵 **En LATAM es la mejor entrada medida de este pase**: administración es la dimensión menos adoptada (**34,1 %**) y la capa **no tiene competencia open source** |

⚠️ **Las tres reservas que van en la propuesta, no en la letra chica:** acoplamiento a **PyPI sin licencia declarada**
(el MIT se lee en el árbol, gap 83 invertido), **~13 meses sin release** (tibia, no archivada), y el resultado del
README —**+32 % en graduación en John Jay College**— es **auto-reportado por el proyecto, no un estudio
independiente**: abre la conversación, no promete el número.

## P87 — *Proctoring*: cuál de las dos rutas se cotiza, y la pregunta que lo decide es una sola (agregado en el pase 40 del 2026-10-02)

El pase 40 cerró la capa de *proctoring* (gap 84) y el mapa es chico y claro: **una pieza seria y copyleft, dos SDK
MIT que resuelven la otra mitad.** El patrón, entonces, no es una receta única: **son dos, y la pregunta que elige
entre ellas es «¿el cliente corre Open edX?».**

| Pieza | Licencia | Qué resuelve | Qué NO resuelve |
|---|---|---|---|
| [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | **AGPL-3.0** | **Integración con el examen**: estados, excepciones, auditoría, proveedores | La detección en sí (la delega al proveedor) |
| [`Drone9/mereos`](https://github.com/Drone9/mereos) | 🟢 **MIT** | **Detección en el navegador**: presencia por webcam, pantalla compartida, foco de pestaña, registro de actividad | Nada del flujo de examen del LMS |
| [`Timadey/proctor`](https://github.com/Timadey/proctor) | ⚠️ MIT (sólo npm) | Detección de rostro y **seguimiento de mirada** con MediaPipe | Ídem |

### Ruta A — el cliente corre Open edX: **adopción**, y la AGPL no agrega fricción

`edx-proctoring` es el subsistema oficial y **el LMS entero ya es AGPL**, así que la licencia **no introduce una
decisión nueva**. Se adopta y se configura el proveedor. ⚠️ **La única advertencia es de versión, y es la tendencia
147: el repo tiene `HEAD` del 2026-05-30 pero el último release de PyPI es del 2025-04-28 — 17 meses.** Lo que llega
por Tutor/pip es ese artefacto. **Hay que fijar la versión a conciencia y presupuestar la diferencia**, no asumir que
«el proyecto está activo» significa «el paquete está al día».

### Ruta B — el cliente NO corre Open edX: **desarrollo de la integración**, con la mitad cliente resuelta

**Los SDK MIT cubren la visión por computadora; el trabajo es el flujo**: estados de examen, excepciones, evidencia,
retención y auditoría. `mereos` es la mejor base por licencia (**`LICENSE` en el árbol y campo npm coincidentes**, y
**repo y registro en la misma fecha**, 2026-08-28, que es lo menos frecuente de este pase).

### 🔴 Y lo que va ANTES de las dos rutas, sin excepción

**El *proctoring* por webcam es el inciso de educación del Anexo III del AI Act**: el punto 3 nombra
**«monitoreo durante exámenes»**. Eso significa:

- **EMEA:** expediente de alto riesgo, plazo **2027-12-02** (y el **Artículo 50** de transparencia **ya rige desde el
  2026-08-02**, independiente del nivel de riesgo). ⚠️ **El seguimiento de mirada de `@timadey/proctor` es inferencia
  biométrica de comportamiento, que es el extremo caro del expediente.**
- **North America:** leyes estatales de privacidad del alumno ya registradas por esta base (**California AB 1159**,
  **Idaho SB 1227**) y el estándar contractual que **Microsoft/AFT** aplica desde el **1.º de noviembre**, que
  **prohíbe el seguimiento del alumno**. 🔴 **Un despliegue de *proctoring* con webcam choca de frente con esa
  cláusula: hay que leerla antes de proponer, no después.**

🔵 **La forma honesta de llevarlo a una reunión:** *«la capa existe, la pieza de referencia es copyleft y está dentro
de Open edX, la detección se resuelve con MIT — y el plazo regulatorio que gobierna esto es diciembre de 2027, así que
el expediente se diseña ahora y no al final»*. 🔴 **Lo que no se puede decir es que hay una opción permisiva completa:
no la hay** (gap 84).

## P82 — El *gateway* de partición de tools: convertir «confiamos en el servidor» en «la escritura no está en la lista» (agregado en el pase 39 del 2026-10-02)

**El problema que resuelve, y es el que bloquea más propuestas de esta base.** Una institución que no acepta que un
agente escriba en su LMS no se convence con `confirm=true` ni con `readOnlyHint`: los dos se cumplen **dentro** del
servidor MCP, así que aceptarlos es aceptar confiar en código de terceros. `PabloPC05/mcp-usc` demostró que hay otra
forma — **22 gemelos `preview_*`**, donde la previsualización es **una tool distinta** de la escritura (tendencia
**137**). **Esta receta generaliza ese hallazgo a las nueve puertas de LMS de esta KB.**

**Las piezas, todas verificadas en esta base:**

| Pieza | Licencia | Rol en la receta |
|---|---|---|
| `@modelcontextprotocol/sdk` | MIT | El *proxy* es un servidor MCP que a su vez es cliente MCP del servidor real |
| Cualquiera de las puertas de LMS de `agents/top.md` | MIT | El servidor *upstream*: `bruchris/canvas-lms-mcp` (165 tools), `PabloPC05/mcp-usc` (91), `Dymayo/moodler-mcp` (38), `NiccoloSalvini/mcp-moodle-teacher` (22), `toshieji/moodle-grading-mcp` (9) |
| `frappe-mcp-server` | ISC | 🔴 **El caso donde el *gateway* no es opcional**: trae `call_method` (ejecución arbitraria) y `delete_document` sin partición por rol |

**Cómo se arma, y son cuatro pasos:**

1. **Levantar el *proxy* como servidor MCP** y, en el arranque, pedirle `tools/list` al *upstream*. **No hardcodear la
   lista:** las superficies se mueven (`qti3-cli` publicó 41 releases en cuatro meses).
2. **Clasificar cada tool por su propia anotación, no por su nombre:** `readOnlyHint: true` → perfil **lectura**;
   `destructiveHint: true` → perfil **escritura**. En `bruchris/canvas-lms-mcp` esto parte las 165 en **120 / 48**
   automáticamente, sin leer el README.
3. **Reexportar sólo el perfil del `role` con el que arranca el *proxy*** (`reader`, `preview`, `grader`, `admin`). Una
   tool que no se reexporta **no existe para el cliente**: no hay ruta de llamada, no hay *prompt injection* que la
   alcance. 🔵 **En `mcp-usc` el perfil `preview` sale gratis: es el conjunto `preview_*` + las de lectura.**
4. **Registrar cada llamada bloqueada** (nombre de tool, perfil, timestamp, hash del argumento) en un JSONL append-only
   —el formato que ya usa `toshieji/moodle-grading-mcp` para su audit trail— **y ese archivo es el entregable de
   auditoría**, no un log de depuración.

🟢 **Por qué esto se vende:** es la única forma de contestar *«¿qué garantiza que no cambie una nota?»* con una
demostración en vez de una promesa — se le muestra al cliente el `tools/list` del *proxy* y la escritura **no está**.
⚠️ **El límite honesto, y hay que decirlo:** el *gateway* protege de **el agente**, no de credenciales filtradas. Si el
token de Moodle con permiso de escritura se escapa, el *proxy* es irrelevante. **Va junto con token por rol, nunca en
lugar de él.**

🔴 **Lo que todavía no se puede afirmar:** esta base **nunca observó un `tools/list` real** (gap **80**: el *daemon* de
Docker no corre en este entorno). Las cifras de 120/48, 91, 38 y 23 **se midieron en código fuente o en el tarball
publicado**. Para el paso 1 eso es suficiente —el *proxy* lee la lista en tiempo de ejecución, no la cifra— **pero no
hay que publicar esas cifras como superficie de protocolo**.

## P83 — Datos educativos de Brasil: ADOPTAR el pipeline del INEP en vez de construirlo, con la salvaguarda LGPD ya escrita (agregado en el pase 39 del 2026-10-02)

🔴 **Esta receta reemplaza la cotización que esta KB venía dando.** El pase 36 dejó escrito que el INEP, por no publicar
API, obligaba a un **pipeline de ingesta de 8-12 semanas** contra las 2-3 de un servidor fachada. **La arquitectura
estaba bien diagnosticada y el pipeline ya está escrito, es MIT y tiene 23 tags.**

**Las piezas:**

| Pieza | Licencia | Qué aporta |
|---|---|---|
| `dasgltd/mcp-brasil` | **MIT** | **13 tools de educación**: `inep_enem` (`info_enem`, `refrescar_enem`, `valores_distintos_enem`, `media_notas_uf`, `media_notas_por_grupo`, `top_municipios_por_media`) e `inep_censo_escolar` (`info_censo_escolar`, `refrescar_censo_escolar`, `valores_distintos_censo`, `buscar_escolas`, `escola_detalhe`, `resumo_uf`, `top_municipios_por_escolas`). PyPI: `mcp-brasil` 0.14.0 |
| Los ZIP del INEP | dato público | `download.inep.gov.br/microdados/microdados_enem_*` y `…/dados_abertos/microdados_censo_escolar_*`. 🔴 **No hay API: la ingesta es parte del diseño, no un workaround** |
| `COLUNAS_DISTINCT_PERMITIDAS` | **MIT**, dentro del repo | *frozenset* de **8 columnas agregadas** que acota qué se puede enumerar: `SG_UF_PROVA`, `SG_UF_ESC`, `TP_SEXO`, `TP_COR_RACA`, `TP_ESCOLA`, `TP_LINGUA`, `TP_FAIXA_ETARIA`, `TP_ST_CONCLUSAO` |

**Cómo se arma:**

1. **Levantar `mcp-brasil` con los dos datasets de educación habilitados** y correr `refrescar_enem` /
   `refrescar_censo_escolar` una vez: ahí se paga el costo real de la receta, que es **descarga y descompresión de
   microdatos** (el Censo Escolar ronda decenas de GB descomprimido).
2. **Dejar el canario de salud de fuentes que el proyecto ya trae en CI** (commit humano del 2026-08-18). 🔵 **Es la
   pieza que esta base no habría escrito y es la que más vale en un pipeline sobre ZIP publicados a mano:** avisa cuando
   el INEP cambia una URL o un layout, que es el modo de falla real de esta arquitectura.
3. **Componer encima**, no adentro: las 13 tools entregan agregados por UF, municipio y grupo. Un agente que compara
   una red escolar con su municipio y su UF se arma con `buscar_escolas` + `escola_detalhe` + `resumo_uf` +
   `top_municipios_por_escolas`, sin escribir una línea de ingesta.
4. **Conservar la salvaguarda y decirlo en la propuesta.** 🟢 **`SOURCES.md` del proyecto clasifica educación como
   RISCO ALTO**, documenta el retiro de microdatos de 2022 por LGPD y la reanudación anonimizada de 2024, **veda la
   re-identificación** y remite a **SEDAP** para investigación con microdatos no anonimizados. **Eso es cumplimiento
   heredado del repo, y conviene citarlo textual.**

⚠️ **Las dos reservas:** `HEAD` del **2026-08-18** (1,5 meses, activo, commit **humano** — no de bot), y **hay que citar
`dasgltd/mcp-brasil`, no `marcellodesales/mcp-brasil`**, que el buscador lista primero y está **0 adelante / 8 atrás**
(tendencia **138**).

## P84 — Cerrar el curso emitiendo un credencial Open Badges 3.0 FIRMADO, no un PDF (agregado en el pase 39 del 2026-10-02)

**La ausencia que cierra.** Esta KB tiene desde el pase 9 la capa de credenciales verificables inventariada —Open
Badges 3.0, W3C VC, CLR— **y ninguna pieza con puerta de agente**: `schroedinger-hat/certo` quedó anotado dos veces
como *«sin puerta MCP»*. Con `maxxeddev/open-badges-mcp` la cadena se completa de punta a punta.

**Las piezas:**

| Pieza | Licencia | Rol |
|---|---|---|
| `maxxeddev/open-badges-mcp` (`mcp-ob-ts`) | **MIT** | **16 tools**: spec (`search_spec`, `get_class`, `resolve_term`, `find_conformance_requirements`, …), **emisión** (`generate_credential`, `create_achievement_credential`) y **validación** (`validate_credential`) |
| `src/crypto/data-integrity.ts` del mismo repo | **MIT** | 🟢 **Firma real: `Ed25519`, `DataIntegrityProof`, `did:key` (`eddsa`)**, contra los contextos oficiales `purl.imsglobal.org/spec/ob/v3p0/context-3.0.3.json` y el *schema* `ob_v3p0_achievementcredential` |
| Una puerta de LMS de esta base | MIT | La señal de logro: `get_completion_status` / `get_course_grades` (`moodler-mcp`), `get_my_completion` (`mcp-usc`) o la capa de *gradebook* de `bruchris/canvas-lms-mcp` |
| `cassproject/CASS` | Apache-2.0 | 🔵 **La pata de competencia, ya en esta base:** `record_evidence` y `get_learner_profile` de su cartucho MCP (6 tools, 3 *resource templates*), para que el credencial apunte a una competencia asertada y no a un nombre de curso |

**Cómo se arma:**

1. **Disparar con la señal del LMS, no con una fecha.** El agente consulta completitud/nota por la puerta del LMS y
   **sólo entonces** llama a la emisión. 🔴 **La decisión de emitir no la toma el agente solo:** se compone con el
   patrón de nota en borrador (**P79**) — **si la nota la publica una persona, el credencial se emite después de eso**,
   y así la cadena entera queda del lado correcto del Anexo III punto 3.
2. **Construir el credencial con `create_achievement_credential`** y **resolver el vocabulario con `resolve_term` y
   `find_conformance_requirements`** en vez de escribir el JSON-LD a mano: es la diferencia entre un badge que valida y
   uno que *parece* válido.
3. **Firmar**, no serializar: `DataIntegrityProof` + `Ed25519` sobre `did:key`. 🟢 **Es lo que hace que el credencial
   sirva fuera de la institución que lo emitió**, que es el único motivo para preferirlo a un PDF.
4. **Validar lo propio antes de entregarlo** con `validate_credential`, y **archivar la evidencia en CaSS**
   (`record_evidence`) para que el perfil del alumno quede consultable por el agente del próximo curso.

⚠️ **Las reservas, dichas antes de cotizar:** `HEAD` **2026-06-10** (**3,7 meses**, franja tibia — no está muerto, pero
no tiene mantenimiento semanal), y el **repo está adelante del registro** (`package.json` 0.4.0 contra npm 0.3.2): hay
que **fijar la versión desde git o esperar el release**. 🔴 **Y el `tools/list` real no se observó** (gap **80**): las 16
tools se contaron en el árbol.

🟢 **Por qué esta receta vale más en APAC y en India en particular:** un mandato curricular nacional desde 3.º grado
(ciclo 2026-27) genera volumen de acreditación que ningún proceso manual absorbe, y el credencial firmado es
**portable entre instituciones** desde el día uno.
