---
industry: education
region: Global
updated: 2026-10-02
---

# 📈 Agentes trending — education

> **APPEND-ONLY.** Cada corrida agrega una sección fechada arriba y conserva la historia abajo.
> No reescribir secciones anteriores: la serie temporal es el valor de este archivo.

## 2026-10-02 (pase 30) — la ausencia más valiosa de esta KB **la cerró el propio proyecto**: Open edX tiene conector MCP oficial, y es **AGPL-3.0 y en proceso**, así que lo que se rompe no es el gap sino **la tesis de composición del pase 27**

**6 artefactos verificados de primera mano (4 leyendo código fuente, 1 ejecutando el servidor, 1 en el registro de
paquetes), 3 altas, 1 tesis propia refutada, 1 conclusión propia corregida, 2 nombres cerrados.**
Este pase ejecutó **las tres acciones** que dejó escritas el pase 29 y las tres rindieron. Pero el hallazgo que manda no
salió de ninguna de las tres: salió de volver a preguntar por el **gap 48**, que esta KB tenía como su mejor oportunidad
comercial. **Ya no lo es.**

| Artefacto | Licencia | Versión / ★ | Canal de verificación | Qué quedó medido | Estado |
|---|---|---|---|---|---|
| [`openedx-mcp`](https://pypi.org/project/openedx-mcp/) | 🔴 **AGPL-3.0** | **0.1.5**, 5 releases, **2026-07-25** | **PyPI JSON + código del sdist** (`openedx.org` bloqueado) | **28 endpoints LMS**, **9 scopes**, **18 tools de escritura** con *rate limit* por tool, **4 rails de seguridad** | 🔴 **Cierra el gap 48 y mata la premisa de P55.** **Nuevo** |
| [`tutor-contrib-openedxmcp`](https://pypi.org/project/tutor-contrib-openedxmcp/) | 🔴 **AGPL-3.0** | **0.1.7**, 7 releases, **2026-07-25** | PyPI JSON | Plugin Tutor que instala el app Django y **corre el servidor MCP**; Tutor local y Kubernetes | **Nuevo.** Es la mitad de despliegue del par |
| [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) | **Apache-2.0** ✅ | 9 ★ | **Código fuente, 5 archivos** vía `raw.githubusercontent.com` | 🔵 **72 rutas contadas**, la regla exacta del prefijo, **2 endpoints de descubrimiento** y una **capa CGE** que nadie había visto | ✅ **Acción 1 cumplida. Gap 52 CERRADO** |
| [`@superbuilders/oneroster`](https://www.npmjs.com/package/@superbuilders/oneroster) | **0BSD** ✅ (en el tarball) | 0.7.0 | 🔵 **Ejecutando el servidor**: `initialize` + `tools/list` | 🔵 **132 tools servidas**, y el «164» explicado: **132 operaciones + 32 alias** | ✅ **Acción 2 cumplida.** 🔴 **Y corrige dos cosas del pase 29** |
| [`redbeard-26/asfai-education`](https://github.com/redbeard-26/asfai-education) | **Apache-2.0** ✅ | 2 ★, 0 forks, 42 commits | README **crudo** (regla del pase 29) | **9 gateways MCP** y **cinco estándares 1EdTech a la vez** | **Nuevo para esta KB.** ⚠️ Muy temprano |
| [`instructure/qti`](https://github.com/instructure/qti) | **MIT** ✅ | 8 ★, 10 forks, 174 commits | README **crudo** | QTI **1.2 y 2.1**, *import/parse*, Ruby. **0 menciones de MCP** | **Nuevo para esta KB.** Es la pata **legada** que `examplary/qti` no cubre |

---

### 🔴 El hallazgo del pase: **el gap 48 lo cerró Open edX, no un tercero — y la licencia de la puerta invierte la conclusión del pase 27**

Esta KB sostuvo durante tres pases que **Open edX era el único LMS grande sin puerta de agente** (gap 48), y los pases
28 y 29 gastaron su esfuerzo principal en medir la superficie REST para cotizar el conector que faltaba (**P55**).
**El conector existe, es oficial del proyecto, y se publicó el 2026-07-25** — dos meses antes de este pase.

Son **dos paquetes**, los dos en PyPI y los dos **AGPL-3.0** (clasificador OSI leído en el JSON del registro, no en
prosa):

- **`openedx-mcp` 0.1.5** — *«Open edX admin operations exposed as an MCP facade for staff/superusers (Ulmo)»*.
- **`tutor-contrib-openedxmcp` 0.1.7** — *«Tutor plugin: MCP server + openedx-mcp Django app»*, Tutor local y Kubernetes.

🔴 **Por qué esto rompe una tesis propia y no sólo cierra un gap.** El pase 27 escribió la frase que organizó tres pases
de trabajo: *«las LMS son copyleft pero las puertas son MIT, y por eso se pueden componer»*. Esa frase descansaba en una
propiedad **arquitectónica**, no legal: las puertas de Moodle y Canvas son **procesos aparte que hablan REST**, así que
llevan su propia licencia. **Esta puerta no.** Leído del propio paquete:

> *«Installs into BOTH the LMS and the CMS process via the standard Open edX djangoapp plugin entry points, because
> course-authoring operations must run in the CMS (they touch the modulestore) while people/access/analytics run in the
> LMS.»*

**Es un plugin Django que corre adentro de los procesos del LMS y del CMS, y es AGPL-3.0.** No hay escotilla de «proceso
separado»: no queda el patrón de composición que esta KB documentó para Moodle y Canvas. **La conclusión comercial, dicha
de frente:** para un cliente que corre Open edX, la puerta oficial es gratis y es mejor que lo que esta KB iba a cotizar,
pero **entra con AGPL en el núcleo de su plataforma**. Lo que queda para vender no es el conector: es **el criterio y la
operación** (ver el reencuadre de P55 y el patrón nuevo **P61**).

### 🔵 Y lo que sí es un regalo: **el proyecto resolvió el riesgo que el pase 29 había dejado anotado como el costo real**

El pase 29 midió **cinco versiones de API montadas a la vez** (`v0`–`v4`), con las notas en tres de ellas y
assets/video/transcripciones sólo en `v0`, y concluyó —bien— que eso era **riesgo de adaptador, cotizable por separado**.
**La puerta oficial no paga ese costo, porque no usa la API REST.** Del propio paquete:

> *«Pure Open edX: every operation is implemented against native openedx-platform **Python APIs**. No third-party stack
> (no Hasura, no external identity, no org multi-tenancy).»*

🔵 **Corre en proceso contra las APIs Python nativas y el modulestore.** Esa decisión **evita entera** la rotación de
versiones que el pase 29 identificó. Es la respuesta de diseño al **gap 50**, y la da el proyecto: *no integres por
REST; corré adentro.* ⚠️ **Y es exactamente la decisión que obliga al AGPL.** Las dos caras son la misma.

### ✅ La autoría de Open edX: el pase 29 tenía razón, y ahora está confirmado por implementación

El pase 29 refutó al 28 mostrando que *«the Authoring API is still experimental»* encabezaba una sección vacía y de 2023,
y que la autoría **era cotizable**. **Queda confirmado por la vía más fuerte posible: el proyecto la implementó.** Las
**7 rutas del CMS**, leídas de `cms_urls.py`:

| Ruta (CMS, bajo `^api/mcp/cms/`) | Qué hace |
|---|---|
| `courses/{course_id}/outline/` | Árbol del curso |
| `courses/settings/` | Ajustes del curso |
| `blocks/create/` | Crea un bloque |
| 🔵 `blocks/create-tree/` | **Crea un árbol entero de bloques en una llamada** |
| `blocks/update/` | Edita |
| `blocks/publish/` | Publica |
| `blocks/delete/` | Borra |

🔵 **`blocks/create-tree/` es la primitiva que un agente necesita y que ningún conector de esta KB tenía:** armar
sección → subsección → unidad en **una** operación, en vez de N llamadas encadenadas que un agente puede dejar a medias.

### 🔵 El artefacto más reutilizable que encontró esta KB: **los cuatro rails de escritura**, con el modelo de amenaza escrito en el código

`guards.py` documenta el diseño en primera persona, y **nombra la amenaza**: no es un humano equivocándose, es **un
agente en bucle**.

> *«An MCP key is driven by an autonomous agent, not a human clicking a button. The failure mode designed against is a
> *looping* agent — a retry storm that mass-enrols or deletes.»*

Los cuatro rails, aplicados por el decorador `audited_write`:

1. **Re-chequeo de autoridad vivo** en cada request.
2. **Rate limit por (key, tool)**, ventana fija — *«turns a runaway loop into ~N calls»*.
3. 🔵 **Confirm token = *dry run* + token de un solo uso atado a una huella del payload exacto.** Una escritura sin token
   **no escribe**: devuelve un *preview*. Se reenvía con el token para aplicar, y **cambiar el payload invalida el token**.
4. **Auditoría *append-only*: la intención se registra ANTES de la escritura, y la escritura se rechaza si el registro no
   se puede persistir.**

**El rail 3 es, en una línea, la compuerta humana que los patrones P53 y P54 de esta KB venían describiendo en prosa.**
Acá está como primitiva de protocolo, con semántica definida. ⚠️ **El patrón se puede reimplementar (un diseño no es
código); el código es AGPL.**

**Y el modelo de credenciales es mejor de lo que decía el resumen de prensa** (*«Django's own is_staff/is_superuser»* es
cierto pero incompleto). Leído de `auth.py`: claves `X-MCP-Key` acuñadas desde el admin, **revocables, con vencimiento y
telemetría de último uso**, y —lo que importa— *«the authorization rule is re-checked **LIVE** on every request… A key
does not cache privilege — demote the user and every key they hold dies on the next call. `scopes` on a key only narrow,
never widen.»*

**Los 9 scopes**, leídos de `models.py`: `read`, `write:enrollment`, `write:users`, `write:roles`, **`grant:admin`**,
`write:certificates`, `write:reports`, `write:courses` y **`destructive`** (aditivo). **18 tools de escritura** con
límite por tool; las tres más restringidas son `bulk_enroll` (**5 cada 300 s**), `regenerate_certificates` (**5 cada
600 s**) y `request_retirement` (**5 cada 600 s**), y la más holgada es `create_xblock`/`update_xblock` (**200 cada 60 s**),
que es coherente con autoría asistida.

🔴 **El requisito de despliegue que está en el código y no en la documentación, y que es cotizable:**

> *«The confirm-token store and rate-limit counter use the ambient Django cache. In production that must be a shared
> backend (Redis/memcached); under LocMemCache (dev) both are per-process.»*

**Un despliegue multi-worker con la caché por defecto degrada los rails 2 y 3 en silencio** — el rate limit cuenta por
proceso y el confirm token puede no encontrarse. Es una línea de infraestructura obligatoria, y es el tipo de hallazgo
que esta KB existe para llevar a una propuesta.

🔵 **Y un puente con el hilo de privacidad de esta base:** hay `retirement/status/{username}/` y `retirement/request/`.
Open edX expone el **retiro de cuenta como operación soportada y documentada** a través de la puerta de agente — justo lo
que los gaps 29/31/32 y **P38** registraron que **ningún LRS ofrece**.

⚠️ **Lo que NO se verificó, dicho explícito:** no se levantó una instancia, así que **no hay `tools/list` observado** de
este servidor. Las 35 rutas (**28 LMS + 7 CMS**) son lectura de `urls.py` y `cms_urls.py` del sdist 0.1.5, y el servidor
MCP vive en el plugin Tutor, que no se corrió. **Es `0.1.x` y apunta a Open edX Ulmo.** Es la **acción 1 del pase 31**.
⚠️ `openedx.org` quedó **bloqueado por el proxy** (nuevo dominio para el registro de bloqueos de esta KB, junto con
`openacs.org`), así que **el blog oficial no se leyó**: todo lo de arriba sale de PyPI y del código.

---

### ✅ Acción 2 cumplida: **132 tools servidas**, y el «164» del pase 28 tiene por fin una explicación que no es supresión

Se bajó el tarball de npm, se corrió `bin/mcp-server.js start --transport stdio` y se hizo el *handshake* real. El
servidor se identifica como **`OneRoster 0.7.0`** y `tools/list` devuelve **132 tools** — **72 de lectura y 60 de
escritura**, en **19 grupos de recurso**.

🔵 **Y la brecha 164 → 132 no es pérdida: es *aliasing*, y está probado por conteo.** El SDK documenta **164 métodos**
(confirmado: 186 encabezados `##` menos 22 «Overview»), pero sólo **132 nombres distintos**: hay **exactamente 32
operaciones listadas bajo dos grupos a la vez**. Ejemplos: `getStudentsForClass` aparece en `classesmanagement` **y** en
`studentsmanagement`; los cinco métodos de *course components* aparecen en `coursecomponentsmanagement` **y** en
`coursesmanagement`. **32 alias, 32 entradas de más, y el servidor registra cada operación una sola vez.**

| Medición | CaSS (pase 27) | `oneroster-ts` (este pase) |
|---|---|---|
| Operaciones del adaptador | 61 | **132 distintas** (164 con alias) |
| Expuestas como tools | **6** | 🔵 **132 — el 100 %** |
| Mecanismo de supresión | `x-mcp-ignore` en 55 | 🔵 **ninguno** |

**La frase citable se corrige en la dirección favorable: «132 tools MCP servidas, el 100 % de las operaciones distintas
del SDK».** No «164 tools», y tampoco la cautela del pase 29 de que podía haber supresión: **no hay nada oculto.** Sigue
siendo **la superficie de tools más grande de esta KB** (132 contra las 102–103 de `canvas-mcp`).

### 🔴 Dos correcciones al pase 29 sobre este mismo paquete, y una es un error de método nuevo

**1. La fecha estaba mal, y el campo leído era el equivocado.** El pase 29 escribió que *«el último publicado es del
2026-05-04, casi cinco meses antes de este pase»*. Ese valor es **`time.modified`** del registro de npm, que es
**mutación de metadatos**, no publicación. La última **versión** publicada es **`0.7.0`, del 2025-06-27**: **quince
meses** antes de este pase, no cinco.

> **Regla nueva de método:** en npm la antigüedad se lee en **`time[version]`**, nunca en `time.modified`. `modified`
> cambia por un *dist-tag*, un cambio de dueño o una deprecación, sin que se publique una línea de código.

**Y el patrón de publicación, que es el dato que importa para «fijar un fork»:** **9 de las 10 versiones salieron en una
ráfaga de tres días** (2025-04-29 → 2025-05-01), después `0.7.0` el 2025-06-27, y **nada en quince meses**.

**2. 🔵 La licencia está mejor de lo que concluyó el pase 29, y la mitigación sigue siendo la correcta por otra razón.**
El pase 29 registró `license: None` en el registro y de ahí sacó que *«el artefacto que se instala no respalda la
recomendación»*. Medido dentro del tarball: **`package.json` no trae el campo `license` en absoluto** (de ahí el `None`
del registro), **pero el paquete publicado SÍ incluye un archivo `LICENSE` completo con el texto de la BSD Zero Clause
License**, *«Copyright (c) 2025 Bjorn Pagen»*. **El defecto es de metadatos, no de licencia: el artefacto sí viaja con su
0BSD.** ✅ **Y cierra la duda de procedencia del pase 29:** `bjornpagen` es **uno de los *maintainers* de npm** que ese
pase anotó como «no son la organización del repositorio» — es el titular del copyright en el LICENSE del tarball, así que
la cadena cierra.

🔴 **Pero aparece un riesgo de portabilidad que no estaba medido.** El README del paquete trae como URL de token de
ejemplo `https://alpha-auth-production-idp.auth.us-west-2.amazoncognito.com/oauth2/token` — **el IdP de producción de un
operador concreto**. El SDK se generó contra **un despliegue**, no contra la especificación en abstracto: hay que
sobreescribir `--server-url` y `--token-url`, y conviene no suponer que cubre a cualquier proveedor OneRoster.
⚠️ Dato menor en la misma dirección: `RUNTIMES.md` declara Node LTS **18 y 20** (se corrió sin problema en **22**).

🔵 **Dos datos operativos a favor, medidos:** **cero dependencias de runtime** (`dependencies: {}` — el servidor MCP es un
*bundle* de 3 MB que no arrastra ni el SDK de MCP), y el flag **`--tool`** permite **servir un subconjunto** de las 132,
que es el control de ventana de contexto que un agente sobre 132 tools necesita.

---

### ✅ Acción 3 cumplida, y el pronóstico del pase 29 era el equivocado: **`.LRN` no está muerto — está vivo, es GPL-2.0 y vive en CVS**

El pase 29 anotó el nombre con la hipótesis de que *«la señal disponible sugiere un proyecto de los 2000»* y pidió
declararlo muerto para no volver a encontrarlo. **La medición dice lo contrario, y el cierre es mejor que «muerto».**

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

⚠️ **`openacs.org` devuelve 403 por el proxy de egreso** (dominio nuevo del registro de bloqueos), así que **nada de lo de
arriba sale de su web: todo sale del árbol git**, que resultó el canal más confiable de los dos.

✅ **Y el nombre que apareció en el barrido vertical de este pase se cierra sin ambigüedad: `CK-ERP` está muerto.** Última
release **v0.31.1, abril de 2012** — catorce años —, alojado en SourceForge, con conector para **Drupal 7.12**. Tenía
módulos educativos reales (*Teacher, Counsellor, Student, Applicant, Family, Registrar, Edu Administration*), y por eso
conviene dejarlo anotado como muerto: **es el tipo de nombre que un barrido de «education ERP open source» va a devolver
otra vez.**

---

### Las dos altas de este pase, verificadas por README crudo

🔵 **`redbeard-26/asfai-education` (Apache-2.0, 2 ★, 0 forks, 42 commits, TypeScript)** — **la primera pieza de esta KB
que declara los cinco estándares 1EdTech a la vez**, y con **9 gateways MCP** (12 menciones de MCP en el README crudo):

| Gateway | Qué hace |
|---|---|
| `asfai_capability` | Descubre capacidades y entrega guía de *workflow* |
| `asfai_graph` | Busca en el grafo de aprendizaje; vecinos, fronteras y caminos |
| `asfai_run` | Prepara trabajo versionado con validación y contratos de revisión |
| `asfai_session` | Diálogo de aprendiz reanudable y *quizzes* formativos |
| `asfai_lesson` | Autoría, validación, revisión, publicación y facilitación de lecciones |
| `asfai_evidence` | Prepara evaluaciones y registra observaciones justificadas |
| `asfai_resource` | Recursos del docente, aulas, *quizzes*, artefactos |
| `asfai_storage` | Almacenamiento privado con verificación de lectura posterior |
| `asfai_classroom` | Conecta proveedores de aula y gestiona asignaciones |

Los estándares que nombra: **1EdTech QTI** (ítems y resultados portables), **xAPI / IEEE 9274.1.1** (eventos de actividad
y evidencia), **1EdTech CASE** (marcos de competencia K–12), **LTI y OneRoster** (lanzamiento y contexto institucional) y
**CLR + Open Badges** (logros portables). ⚠️ **Es una arquitectura de referencia, no una dependencia: 2 ★ y 42 commits.**
Se propone como **mapa de capas**, no como pieza a instalar en un entregable de cliente.

⚠️ **Y matiza —no refuta— la ausencia de QTI.** El **gap** de QTI decía que no hay conector MCP de QTI, medido por tres
métodos. **Sigue siendo cierto en lo que afirma**: esto no es un conector de QTI, es un servidor MCP de aprendizaje que
**declara QTI como su formato** de ítems. La ausencia de una puerta MCP *dedicada* a QTI se mantiene.

🔵 **`instructure/qti` (MIT, 8 ★, 10 forks, 174 commits, Ruby)** — y la razón de que entre es que **cubre la pata que
`examplary/qti` no cubre**. `examplary/qti` es QTI **3.0 y 2.1**; esta gema es QTI **1.2 y 2.1**, o sea **el formato
legado**, que es exactamente el acervo que **P48** parte de migrar. ⚠️ **Con la precisión que corresponde: P48 ya nombraba
`LongsightGroup/qti3` (MIT, 667 commits) para esa pata, y además migra 1.2/2.x a QTI 3 — así que esta gema es una
alternativa de lectura en Ruby o un segundo parser de validación, no una pieza que faltaba.** ⚠️ **Dos límites medidos, y acotan el uso:** sólo
**importa y parsea** (no genera), y los tipos de interacción soportados son **True/False, Multiple Choice y Multiple
Answer**. **0 menciones de MCP** en el README crudo, lo que la vuelve otro control negativo para la ausencia de QTI.

### ⚠️ Un falso positivo evitado, y se escribe porque la trampa es nueva: **la señal estaba en un *pull request*, no en el producto**

El barrido devolvió `tutors-sdk/tutors-mono-repo` (**MIT**, 4 ★, 5 forks, **813 commits**, TypeScript/Svelte 5) con
xAPI y **Open Badges 3.0**. **Verificado en el README crudo: 0 menciones de xAPI, 0 de Open Badges, 0 de MCP.** Todo eso
vive en el **PR #341, que está ABIERTO** (última actualización **2026-09-30**), y es donde aparecen `@tutors/xapi`,
`@tutors/badges` (credenciales **OB 3.0** desde un `badges.yaml`) y un `compose.yaml` que levanta **Yet Analytics SQL LRS
(Apache-2.0)** y el **DCC signing service (MIT)**.

> **Regla nueva, hermana de la del pase 29 sobre el README renderizado:** cuando el buscador devuelve un *pull request*
> como evidencia de una capacidad, **la capacidad no está en el producto**. Se anota como **vigilancia**, no como alta.

**`tutors-mono-repo` entra entonces como lo que sí es —un *course reader* / LMS MIT con 813 commits— y el trabajo de
estándares queda en vigilancia** para el pase que lo encuentre mergeado.


## 2026-10-01 (pase 29) — las **dos ausencias declaradas se dan vuelta**, y las dos por el mismo error de método: **se había leído un archivo donde hacían falta dos**

**4 repos verificados de primera mano, 2 nuevos para esta KB, 1 conclusión propia refutada, 1 colisión de tipo nuevo.**
Este pase ejecutó **las tres acciones** que dejó escritas el pase 28. Las tres rindieron, y **la 1 refutó la conclusión
del pase que la pidió** — es la **quinta vez consecutiva** que el error estaba en el muestreo y no en la fuente, y la
**primera** en que la fuente mal muestreada era **un archivo de un repo que ya teníamos abierto**.

| Repo | Licencia | ★ | Forks | Commits | Lenguaje | Qué expone | Estado |
|------|----------|---|-------|---------|----------|------------|--------|
| [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) | **Apache-2.0** ✅ | 9 | 3 | 180 | — (monorepo `apps/`) | **CASE 1.0 y 1.1** por la **CASE Provider API oficial**, *«ready for 1EdTech certification»*. CRUD de escritura sobre `CFDocuments`, `CFItems`, `CFAssociations`, `CFPackages` en **v1p0 y v1p1**; editor visual de marcos; Keycloak (OIDC) **+ API keys**; RBAC de 4 niveles; multi-tenencia; versionado **inmutable en archivos, sin base de datos externa**; **endpoint de descubrimiento OpenAPI 3** | 🔵 **Cierra el gap 51 y abre P60.** **Nuevo para esta KB** — y es la pieza que faltaba del lado de los estándares |
| [`Cicatriiz/openedu-mcp`](https://github.com/Cicatriiz/openedu-mcp) | **MIT** ✅ | 13 | **10** | 21 | Python | **21 nombres de tool leídos del README crudo: 20 de dominio + 1 de transporte.** Libros (OpenLibrary), artículos (Wikipedia), vocabulario e investigación (arXiv), con filtrado educativo y adecuación por nivel de grado | **Nuevo para esta KB.** ⚠️ **No toca LMS ni estándar** — es la capa de **contenido abierto**, no un conector institucional |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 8.2k | 4.4k | 68.764 | Python/Django | **Medido leyendo cinco `urls.py` y dos `views/`**, no la documentación. 🔴 **Refuta la conclusión del pase 28** | 🔵 **La autoría NO está bloqueada.** Ver abajo |
| [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | **0BSD** ✅ (en el repo) | 10 | 3 | 39 | TypeScript | **164 métodos CONTADOS uno por uno** sobre **21 grupos de recurso**, no «declarados» | ✅ **Acción 3 cumplida.** 🔴 **Pero aparecieron dos riesgos nuevos que no estaban medidos** — ver abajo |

### 🔴 La refutación del pase: **la autoría de Open edX no está bloqueada, y el aviso que lo decía está vacío y es de 2023**

El pase 28 cerró el **gap 48** y abrió el **gap 50** con esta frase: *«el repo avisa que "the Authoring API is still
experimental" y recomienda usar las versiones `v0`»*. **La cita es literal y está bien transcripta. La conclusión que
se sacó de ella es falsa**, y alcanzó **leer el archivo de al lado** para verlo.

**Las tres lecturas, en orden, porque el orden es el argumento:**

1. **`v1/urls.py`** — el aviso existe, y está **al final del archivo**, así:
   `# Authoring API` / `# Do not use under v1 yet (Nov. 23). The Authoring API is still experimental and the v0 versions should be used`.
   🔴 **Esa sección no tiene ni una ruta debajo: es un comentario encabezando el vacío**, y está fechado
   **noviembre de 2023** — casi tres años antes de este pase.
2. **`v0/urls.py`** — acá sí está la *Authoring API* real, bajo su propio `# Authoring API`: `heartbeat`,
   `file_assets/{course_id}` (**create/retrieve**) y `file_assets/{course_id}/{asset_key}` (**update/destroy**),
   `videos/encodings`, `videos/features`, `videos/images`, `videos/uploads` (**create** y por `edx_video_id`),
   `video_transcripts`, `youtube_transcripts/check` y `/upload`, `grading/{course_id}`, **`xblock/{course_id}`
   (create) y `xblock/{course_id}/{usage_key}`**, más `advanced_settings`, `tabs` (**list/settings/reorder**) y el
   *Course Optimizer* (`link_check`, `link_check_status`, `rerun_link_update`, `rerun_link_update_status`).
3. **`v0/views/xblock.py`** — y acá se cierra la pinza. El docstring dice **lo contrario** del comentario de `v1`:
   *«Public rest API endpoints for the CMS API — v0 xblock (DEPRECATED). These views are superseded by `XblockViewSet`
   in `cms.djangoapps.contentstore.rest_api.v1.views.xblock`. Use `/api/contentstore/v1/xblock/` going forward. These
   v0 endpoints will be removed in a future release.»* Las cinco vistas emiten `DeprecationWarning` en runtime.

🔵 **Y el sucesor existe de verdad, no es una promesa.** `v1/urls.py` **registra `XblockViewSet` en su primera línea de
`urlpatterns`** (`_router.register(r'xblock', XblockViewSet, basename='xblock')`), y `v1/views/xblock.py` tiene
**CRUD completo**: `create`, `retrieve`, `update`, `partial_update`, `destroy`. **No es código experimental abandonado:
está construido contra un programa de ADRs con nombre y número** — **FC-0118**, ADRs **0025** (`serializer_class`),
**0026** (`authentication_classes`/`permission_classes` explícitas), **0028** (consolidación vía `DefaultRouter`),
**0029** (envelope de error estandarizado), **0034** (`JwtAuthentication` +
`SessionAuthenticationAllowInactiveUser`) y **0036**.

🔵 **El detalle de ADR 0036 es el que más vale para un agente, y no se encontró buscando: estaba en el docstring.**
`retrieve` acepta **`?view=minimal`**, que *«strips the (tree-shaped) xblock response to a small set of structural
fields»*. **Un árbol de curso completo es exactamente la respuesta que hace explotar la ventana de contexto de un
agente**, y la plataforma ya trae el recorte. **Eso no hay que construirlo: hay que pasar un query param.**

**La conclusión, entonces, es una deprecación circular:** `v1` dice *«usá v0»* (2023) y `v0` dice *«usá v1»* (vigente,
con `DeprecationWarning` en el código). **Cuando dos avisos del mismo repo se contradicen, gana el que está respaldado
por rutas registradas y por un programa de ADRs activo** — y ése es `v1`. **El gap 50 no se cierra: se reencuadra.** Lo
que queda no es *«la autoría es inestable»* sino *«la autoría está a mitad de una migración de versiones»*, que es un
riesgo de **adaptador**, no de **viabilidad**.

### 🔵 El hallazgo colateral, y es el que cambia la forma de la propuesta: **hay cinco versiones de API vivas al mismo tiempo**

`rest_api/urls.py` monta **`v0/`, `v1/`, `v2/`, `v3/` y `v4/`**. El pase 28 conocía tres. Las dos nuevas:

- **`v2`** — `downstreams` (`DownstreamListView`, `DownstreamView`, `DownstreamSummaryView`, **`SyncFromUpstreamView`**),
  más `NumericalInputValidationView` y `HomePageCoursesViewV2`. 🔵 **`SyncFromUpstream` es reutilización de contenido de
  biblioteca**: es la pieza que un agente necesita para propagar una corrección a todos los cursos que la heredan.
- **`v3`** — ViewSets de `home`, `course_details` y **`authoring_grading`**.
- **`v4`** — `home/courses` (`HomeCoursesViewSet`, ADR **0028**).

🔴 **Y el costo de esa rotación se ve en una sola capacidad: las notas viven en tres lugares a la vez** — `grading/` en
`v0`, `course_grading/` en `v1` y `authoring_grading` en `v3`. **Eso es lo que un conector tiene que absorber**, y es
un argumento concreto para cobrar un adaptador de versión en vez de pegarle a una ruta fija.

### ✅ La acción 3, cumplida — y **«declara 164» pasa a «164 contados»**, con dos riesgos nuevos de regalo

El pase 28 escribió *«los 164 métodos son los que declara el README»* y lo dejó como cautela. **Ahora está contado por
dos canales independientes dentro del propio repo:**

1. **Conteo directo del índice de métodos generado**: **exactamente 164** entradas, repartidas en **21 grupos de
   recurso** (`academicSessionsManagement`, `assessmentLineItemsManagement`, `assessmentResultsManagement`,
   `categoriesManagement`, `classesManagement`, `courseComponentResourcesManagement`, `courseComponentsManagement`,
   `coursesManagement`, `demographicsManagement`, `enrollmentsManagement`, `gradingPeriodsManagement`,
   `lineItemsManagement`, `organizationsManagement`, `resourcesManagement`, `resultsManagement`, `schoolsManagement`,
   `scoreScalesManagement`, `studentsManagement`, `teachersManagement`, `termsManagement`, `usersManagement`).
   **Los 21 recursos que el pase 28 citó quedan confirmados por conteo.**
2. **Corroboración por la tabla de errores generada**, que es independiente del índice: *«Applicable to **131 of 164
   methods**»*, repetido para `400`, `401` y `403`.

⚠️ **Lo que sigue sin medirse, y la distinción importa porque esta KB ya se quemó con ella.** 164 es el conteo de
**métodos del SDK**, no de **tools MCP observadas en `tools/list`**. **CaSS enseñó exactamente esta diferencia**: 61
operaciones, **6 expuestas y 55 con `x-mcp-ignore: true`**. 🔵 **A favor de `oneroster-ts`: no aparece ninguna
anotación de supresión ni ningún `scope` de tool en el repo** — no hay indicio de ocultamiento, que es una postura
distinta de la de CaSS, que **documentaba** sus exclusiones. **Pero la frase citable sigue siendo «164 métodos de SDK
contados», no «164 tools MCP».**

🔴 **Riesgo nuevo 1, y es el más serio para un entregable: el paquete que se instala no declara licencia.** El repo es
**0BSD**; el artefacto publicado es **`@superbuilders/oneroster`** y el registro de npm devuelve **`license: None`**,
tanto en la raíz como en la versión `0.7.0`. **El repo auditado y el paquete instalado no dicen lo mismo sobre el
derecho de uso.** Para un cliente eso no es un detalle de metadatos: es lo que mira su área legal. **Refuerza la
recomendación que ya estaba escrita —fijar un fork— y le agrega el motivo real.**

🔴 **Riesgo nuevo 2: el publicador no es la organización del repo.** El repo vive en **`trilogy-group`**; los
*maintainers* de npm son **`abhi-superbuilders`, `hbauer`, `bjornpagen`, `supersterling`, `ameeralns`**. ✅ **La
procedencia es rastreable** —el `repository.url` del paquete apunta de vuelta a `git+https://github.com/trilogy-group/oneroster-ts.git`—
**pero no es la misma organización**, y eso se declara en la propuesta en vez de que lo descubra el cliente.

⚠️ **Y dos datos de frescura que antes no estaban: `0.7.0`, 10 versiones, publicado por última vez el 2026-05-04.**
Eso son **casi cinco meses** a la fecha de este pase, y una versión **pre-1.0**. **El riesgo de mantenimiento del
gap 49 deja de ser cualitativo y pasa a tener fecha.**

### 🔴 La colisión número cinco, y es de un tipo que esta KB no tenía: **la que mete el propio GitHub**

La **acción 2** pedía medir CASE por el nombre completo del estándar. **Funcionó** —apareció `1EdTech/OpenCASE`, que
ninguna búsqueda por sigla había devuelto— **y después casi produjo un falso positivo de los caros.**

La página renderizada de GitHub de OpenCASE **contiene la palabra «MCP»**: en el menú de navegación, bajo *AI CODE
CREATION*, como *«MCP Registry—Integrate external tools»*. 🔴 **Eso es chrome de la interfaz de GitHub, no contenido
del repositorio.** La lectura del **README crudo** por `raw.githubusercontent.com` devuelve **cero** menciones de
`MCP` o `Model Context Protocol`.

**El registro de colisiones de esta KB, ahora con un tipo nuevo:**

| # | Colisión | Tipo | Pase |
|---|---|---|---|
| 1 | `Bloom` → dos proyectos homónimos | Nombre de proyecto | 7 |
| 2 | `education` → material didáctico *sobre* AI | Término de dominio | 23 |
| 3 | `MCP` + *badges* → generadores de *badges* de README | Término técnico | 27 |
| 4 | `case` → *case study* / *use case* | Término técnico | 28 |
| 5 | **`MCP` en una página de GitHub → menú de GitHub** | 🔴 **Chrome de plataforma** | **29** |

**Las cuatro primeras son ambigüedades de la consulta. La quinta es una contaminación de la fuente**, y por eso la
regla es distinta y más fuerte: **la presencia o ausencia de MCP se verifica en el README crudo, nunca en la página
renderizada.** Vale para toda medición de esta KB hacia adelante, y **vale retroactivamente como advertencia sobre
cualquier presencia de MCP que se haya afirmado leyendo una página de GitHub**.

### El barrido obligatorio, y lo que devolvió por quinta vez consecutiva

Cuatro búsquedas globales y cuatro regionales, con el año **calculado** (2026):

- 🔴 **`top open source AI agents education 2026 github MIT`** y **`github trending education AI 2026`** devolvieron
  **otra vez la capa genérica** (OpenClaw ~362k ★, `opencode` **194.461 ★**, OpenHands 70k+, CrewAI **56.723 ★**,
  LangGraph **39.083 ★**, AutoGen **56.730 ★**) **y material didáctico *sobre* AI** (*AI Agents for Beginners* de
  Microsoft, **56.002 ★**, 12 lecciones). **Quinta confirmación de la colisión 2.** Ninguno es un agente educativo y
  ninguno entra a la tabla.
- ⚠️ **`open source platform education ERP CRM MIT Apache`** devolvió **únicamente plataformas que esta KB ya tiene**
  (OpenEduCat, ERPNext/Frappe, Moodle, RosarioSIS, Sakai, Chamilo, Kolibri, openSIS, Fedena, Open edX, OpenOLAT).
  **Cero altas de vertical, y se escribe porque el silencio se lee igual que la cobertura.** Un solo nombre no estaba:
  **`.LRN`/dotLRN** (LMS nacido en el MIT sobre OpenACS) — **no se verificó en este pase y no se cita hasta verificarlo**.
- Las cuatro regionales se registran en `intel/market.md` y `intel/trends.md`.

### Lo que este pase deja medido y lo que no

- ✅ **Medido:** las cinco versiones de API de Studio y el CRUD de `XblockViewSet`, **leyendo el código**; los 164
  métodos de `oneroster-ts`, **contados**; la licencia de los dos repos nuevos, **leída del archivo `LICENSE`**; la
  ausencia de MCP en OpenCASE, **leída del README crudo**.
- ❌ **No medido:** **ninguna llamada HTTP contra una instancia de Open edX ni de OpenCASE.** Sigue en pie el límite
  del pase 27 (no se instala código de terceros). **OAuth2, *scopes*, *rate limits* y forma de las respuestas siguen
  sin verificar en las dos plataformas.**
- ❌ **No medido:** el `tools/list` real de `oneroster-ts`. **164 es conteo de métodos de SDK, no de tools servidas.**
- ❌ **No medido:** la forma exacta de las rutas de OpenCASE. **Los dos documentos del repo se contradicen** (uno
  muestra `/management/tenants/{tenantId}/CFItems/{id}`, el otro `/management/tenants/{tenantId}/ims/case/v1p1/CFItems/{itemId}`),
  y **el `FRAMEWORK_MANAGEMENT_GUIDE.md` que el README enlaza como referencia de endpoints devuelve 404 en `main`**.
  Es el **gap 52** y la **acción 1 del pase 30**.

### Las tres acciones que este pase deja escritas para el 30

1. **Resolver la contradicción de rutas de OpenCASE leyendo el código, no los docs** — el método que funcionó con Open
   edX. **Y si se levanta la instancia, pedirle el OpenAPI 3 a su propio endpoint de descubrimiento**, que es la
   medición definitiva y la que habilita **generar** el conector de **P60**.
2. **Medir el `tools/list` de `oneroster-ts`**, que es lo único que convierte «164 métodos» en «N tools». Es el último
   tramo abierto de la cadena que empezó en el pase 26 con CaSS.
3. **Verificar `.LRN`/dotLRN**: si está vivo, es una vertical que esta KB no tiene; si está muerto, se declara muerto y
   se cierra el nombre para no volver a encontrarlo cada barrido.

## 2026-10-01 (pase 28) — el eje conector rinde por **cuarta vez**, y la corrección es de método: **la puerta MCP se esconde adentro de un SDK**, no detrás de un nombre `*-mcp`

**5 repos verificados de primera mano, 3 nuevos para esta KB, 1 control negativo, 1 cifra de agregador refutada en la
dirección contraria a la esperada.** Este pase ejecutó las **acciones 1 y 2** del pase 27. Las dos rindieron, y la 2
**volvió a corregir la premisa de un pase anterior** — es la **cuarta vez consecutiva** que el error estuvo en el
muestreo y no en la fuente.

| Repo | Licencia | ★ | Forks | Commits | Lenguaje | Qué expone | Estado |
|------|----------|---|-------|---------|----------|------------|--------|
| [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | **0BSD** ✅ | 10 | 3 | 39 | TypeScript | **164 métodos** sobre 21 recursos OneRoster (`academicSessions`, `classes`, `courses`, `enrollments`, `grades`/`results`, `lineItems`, `orgs`, `schools`, `users`, `demographics`…) **expuestos como MCP tools**. **Lectura y escritura**: `createUser`, `updateClass`, `deleteEnrollment`, `postAcademicSession`. OneRoster **v1p2**, paginación por offset y `filter` de 1EdTech | 🔴 **Refuta el «OneRoster vacío» del pase 26.** **La superficie de tools más grande de esta KB** |
| [`paulocymbaum/ed-tech-system-mcp`](https://github.com/paulocymbaum/ed-tech-system-mcp) | **MIT** ✅ | 0 | 0 | 132 | Python | **18 tools** sobre agentes LangGraph: `content_generation`, `author_lesson_pipeline`, `validate_lesson`/`_quiz`/`_project`, `search_graph_nodes`, `generate_mock_test_structure`, **`socratic_tutor`**, `project_review`, `search_youtube` | **Early-stage declarado** (0 ★ con 132 commits). **Sin integración a LMS**: backend propio en Supabase. Otro caso puro del **gap 49** |
| [`examplary/qti`](https://github.com/examplary/qti) | **MIT** ✅ | 1 | 0 | 32 | TypeScript | QTI **3.0 (default) y 2.1**, generación y parseo de paquetes | **Control negativo del pase.** 🔴 **MCP no se menciona en ningún lugar del repo.** Ver abajo: es lo que convierte la ausencia de QTI en **medida** |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 8.2k | 4.4k | 68.764 | Python/Django | Medido **leyendo el código**, no la documentación. Ver la sección del gap 48 | ⚠️ **Nota de nomenclatura:** el repo **se renombró** — `openedx/edx-platform` es el nombre viejo y **redirige**. Las dos URLs resuelven y apuntan al mismo árbol |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent) | **MIT** ✅ | **250,6k** | 53,6k | — | — | Agente genérico auto-mejorable, sucesor de OpenClaw | **No es educativo** y no entra a la tabla de agentes. Se verificó **porque el pase 27 dejó la instrucción de verificarlo si volvía a aparecer** — y volvió |

### 🔴 La corrección, y esta vez la regla del pase anterior tampoco habría alcanzado

El pase 26 declaró **OneRoster vacío** consultando un directorio. El pase 27 diagnosticó la causa (**gap 49**: los
directorios rankean por promoción) y dejó escrita la regla: *«no preguntarle a un directorio de MCP, preguntarle al
host del repositorio por patrón de nombre»* — `*-mcp`, `mcp-*`, `mcp-server` + el nombre del estándar.

**Esa regla encuentra el repo, pero no por el patrón que proponía.** `trilogy-group/oneroster-ts` **no se llama
`oneroster-mcp` ni `mcp-oneroster`**, y no aparece en ningún directorio de MCP. Se llama `-ts` porque **es un SDK**, y
el servidor MCP es **una característica del SDK**, declarada en una sola línea del README:

> *«This SDK is also an installable MCP server where the various SDK methods are exposed as tools that can be invoked
> by AI applications.»*

**La regla que sale de acá, y es la cuarta iteración de la misma lección:**

> **La puerta de agente ya no se publica como producto propio: se le agrega a la biblioteca que ya hablaba el
> estándar.** Buscar `*-mcp` encuentra a los que *quisieron* ser conectores. Para encontrar a los que *son* conectores
> hay que buscar **el estándar + `SDK`/`client`/`library`** y **leer el README por dentro**. Un nombre no es un índice
> de capacidad, igual que un directorio no es un índice de licencia.

**Por qué importa más que el repo:** las ausencias que esta KB declaró consultando nombres y directorios —y hay
varias— **están todas mal medidas por construcción**. La única ausencia que sobrevive a los tres métodos en este pase
es la de QTI, y sobrevive porque **se abrió el SDK y se miró adentro**.

### QTI: la ausencia pasa de muestreada a **medida**

Es el único no-hallazgo de este pase que se puede firmar, y conviene decir por qué vale distinto:

| Método | Resultado |
|---|---|
| Consulta a directorio MCP (pase 26) | vacío — **no concluyente**, es el error del gap 49 |
| Patrón de nombre `qti-mcp` / `mcp-qti` (regla del pase 27) | vacío |
| **Apertura del SDK permisivo** (`examplary/qti`, MIT, QTI 3.0 + 2.1) | 🔴 **MCP no aparece en el repo** |

**Tres métodos independientes, el mismo resultado.** La otra pieza de la capa, `oat-sa/qti-sdk`, es **PHP** — y el
ecosistema MCP de PHP es marginal, lo que **explica** la ausencia en vez de sólo registrarla. **Conclusión citable: el
estándar de evaluación de 1EdTech es el único de los tres revisados que de verdad no tiene puerta de agente**, y la
pieza sobre la que construirla es MIT y TypeScript. Ver **P59**.

### CASE: cuarta colisión de término de esta KB, y la ausencia queda **sin medir**

`"case-mcp"` / `"mcp-case"` devuelve **`09-CaseStudy` de `microsoft/mcp-for-beginners`**, **`Casys-AI/mcp-server`** y
**`mcp-usecase`**. La palabra `case` está capturada por ***case study*** y ***use case***, que son dos de los términos
más frecuentes de la documentación de MCP.

Es la **cuarta colisión** registrada, y el patrón ya es un activo de método de esta KB:

| # | Término | Capturado por | Pase |
|---|---|---|---|
| 1 | `education` | material didáctico **sobre** AI | 23 |
| 2 | `MCP` + *badges* | generadores de *badges* de README | 27 |
| 3 | `Bloom` | dos proyectos distintos homónimos | 7 |
| 4 | **`case`** | ***case study*** · ***use case*** | **28** |

🔵 **Se declara explícitamente: la ausencia de conector CASE NO está medida en este pase.** La colisión es demasiado
fuerte para que el canal de búsqueda sirva, y el método que funcionó con OneRoster —abrir el SDK— **no se pudo aplicar
porque CASE no tiene un SDK permisivo y traccionado que abrir**. Lo que sí está medido, de los pases 26 y 27, es que
**CaSS tiene los 11 métodos de su adaptador CASE con `x-mcp-ignore: true`**, es decir **excluidos a propósito**. Queda
como **gap 51**.

### La cifra de agregador, refutada **en la dirección contraria** a la que esta KB esperaba

El pase 27 registró un *«Hermes Agent, MIT, 180.000+ ★»* y **se negó a escribirlo** por venir de un agregador sin
verificación, dejando la instrucción de verificarlo si reaparecía. **Reapareció en el barrido global de este pase, y
con tres cifras distintas en tres fuentes: 180.000, 212.000 y 230.000.** La página del repo dice **250,6k ★ y 53,6k
forks**.

> **Las tres estaban mal, y las tres estaban mal *por debajo*.** El pase 22 y el pase 4 del `technology`-KB habían
> encontrado agregadores **inflando** estrellas, y esta KB venía escribiendo la regla como *«los agregadores inflan»*.
> **Es más preciso decir que los agregadores están viejos**: en un repo que crece rápido el error cae del lado bajo, y
> en uno estancado del lado alto. **La regla correcta no es sobre la dirección del error sino sobre la fuente: la
> cifra se lee de la página del repo o no se escribe.**

**Hermes Agent no entra a la tabla de agentes de esta KB:** es un agente de propósito general, no educativo. Se
registra acá por el método, y como nota de sucesión de OpenClaw.

## 2026-10-01 (pase 27) — el eje conector rinde por tercera vez, y lo que devuelve es una corrección: el conector MCP de Moodle **sí existe, es MIT y escribe notas**, y el hueco real se corre a Open edX

**5 repos verificados de primera mano, 4 nuevos para esta KB, 1 inexistente.** Este pase no agrega una capa: **corrige
la premisa del pase anterior.** El **gap 43** y el patrón **P51** del pase 26 se construyeron sobre la afirmación *«el
único conector MCP de Moodle es `csmediapro/moodle-mcp-server`, AGPL-3.0, 0 ★, 10 tools sólo de lectura»*. **Es falsa.**
Hay al menos **dos conectores MIT** que el pase 26 no vio, y uno de ellos **escribe notas y devoluciones**.

| Repo | Licencia | ★ | Forks | Commits | Lenguaje | Qué expone | Estado |
|------|----------|---|-------|---------|----------|------------|--------|
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** ✅ | 43 | 13 | 10 | TypeScript | **8 tools, y cuatro son de escritura**: `get_courses`, `list_students`, `get_assignments`, `get_student_submissions`, **`provide_assignment_feedback`**, `get_quizzes`, `get_quiz_attempts`, **`provide_quiz_feedback`** | **El más traccionado de la capa.** Es el primer artefacto permisivo de esta KB que **pone nota y devolución dentro de un LMS de producción** |
| [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) | **MIT** ✅ | 1 | 1 | 59 | TypeScript | **40 tools** en 10 dominios (Curso, Secciones, Contenido, Evaluación, Alumnos, Gradebook, Comunicación, Calendario, Badges) **+ `ws_raw`**, escape hatch a Web Services crudo | v0.5.2; el README declara **«~80 % operable desde un agente LLM»** y deja salvedades en subida de archivos y creación de secciones. **Pre-producción, no MVP** |
| [`giacomomaria81/scorm-mcp-server`](https://github.com/giacomomaria81/scorm-mcp-server) | **MIT** ✅ | 6 | 0 | 11 | TypeScript | **3 tools**: `scorm_package`, `scorm_validate`, `scorm_selftest`. SCORM **2004 4.ª ed. y 1.2**, versión elegible por parámetro | Empaqueta HTML a SCORM **inlineando cada asset como data URI → 100 % offline**. Es el puente al LMS que ya está instalado |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** ✅ | — | — | — | Python | Re-verificado. ⚠️ **El conteo de tools no es citable como cifra fija**: según versión se declaran **40+**, **80+** y **116** (una implementación TypeScript) | Ver la corrección de abajo: el pase 26 escribió «102–103 tools» |
| `Snaw80/mcp-moodle` | — | — | — | — | — | — | 🔴 **No existe. HTTP 404.** Apareció en el resumen de búsqueda con licencia MIT y lista de tools. **Falso positivo del canal de búsqueda** |

### 🔴 La corrección, dicha con precisión

El pase 26 no inventó el dato: **leyó bien el repo que encontró**. `csmediapro/moodle-mcp-server` es efectivamente
AGPL-3.0 con plugins premium. **El error fue el cuantificador** — *«el único»* — y tiene una causa de método que vale
más que el hallazgo:

> **Los directorios de MCP rankean por promoción, no por licencia ni por capacidad.** El conector que se vende a sí
> mismo (dominio propio, paquete npm con nombre de producto, *premium plugins*) aparece primero. Los dos MIT tienen
> **1 ★ y 43 ★ y ningún material de marketing**, y por eso no salieron. **Regla: cuando una búsqueda de directorio
> devuelve un solo candidato y además es el único con sitio comercial, la capa no está medida — está mal muestreada.**

Es hermana de la regla del pase 26 (*verificar que el término no esté capturado por otro mercado*) y de la del pase 6
(*si un gap sobrevive, revisar el método antes que la conclusión*). **Tres pases consecutivos en que el error estuvo en
el muestreo y no en la fuente.**

### Lo que esto le hace al inventario

- **El gap 6 (grading), abierto desde el pase 2, cambia de estado por primera vez.** El gap decía que la demanda de
  corrección y devolución está probada y la oferta open source es nula. **`provide_assignment_feedback` y
  `provide_quiz_feedback` son esa oferta, son MIT, y escriben contra Moodle sin modificar el LMS.** No cierra el gap
  —8 tools no son un sistema de corrección— pero **deja de poder decirse que no hay nada permisivo del lado de la
  escritura.** Ver **P54**.
- **El hueco real se corre a Open edX.** Búsqueda extendida: **no hay conector MCP para Open edX.** Y es la ausencia
  que más importa, porque Open edX es el LMS de los despliegues públicos grandes de LATAM e India. Ver el **gap 48** y
  **P55**.
- **Open Badges y Caliper siguen vacíos, y de Open Badges ahora hay medición de primera mano** (abajo, en la nota de
  CaSS).

### Lo que se buscó y salió vacío, escrito como tal

| Estándar | Consulta | Resultado |
|---|---|---|
| **Open Badges** | `"MCP server" Open Badges Open Badges 3.0 github open source connector` | 🔴 **Nada del estándar.** Lo que aparece es `IssueBadge` (SaaS comercial de insignias) y `MCP Badges` (genera *badges* de README — **tercera colisión de término** de esta KB) |
| **Caliper** | `"MCP server" Caliper Analytics IMS learning analytics open source` | 🔴 **Nada.** Consistente con que Caliper dejó de ser open source el **2023-06-17**. La ausencia está **escrita**, no inferida |
| **Open edX** | `"Open edX" MCP server github repository connector tools Studio API` (modo extendido) | 🔴 **Nada.** Ver **gap 48** |

---

## 2026-10-01 (pase 26) — se corta la racha de siete pases sin altas, y se corta en el conector: el gap 40 se cierra ejecutando y el lado LMS se cierra midiendo que no existe

**La tabla principal pasa de 37 a 38 filas.** Entra `vishalsachdev/canvas-mcp` (**MIT**, 269 ★, 92 forks, 815 commits,
**hasta 102–103 tools** y 8 *agent skills*). Es **el conector permisivo de LMS más grande que registró esta KB** y el
primero que cubre **el lado docente** además del del alumno: corrección, analítica de alumnos, mensajería, gestión de
módulos y páginas, y un *Learning Designer* con **escaneo de accesibilidad y chequeo WCAG** — la capa que el pase 8
abrió, llegando por fin al conector. Trae `search_canvas_tools`, que es la respuesta de diseño a tener cien
herramientas: **el agente descubre la tool en vez de recibir las cien en el contexto.**

**Y entró por donde el pase 25 dijo que había que buscar.** La consigna era literal: *«cambiar el eje de búsqueda al
conector, que es donde este pase mostró tracción: `MCP server` + cada estándar que esta KB ya inventarió»*. **La
consigna rindió en su primer uso, por segunda vez consecutiva** (el pase 24 ya había validado el eje
artefacto/estándar). El barrido obligatorio —cuatro globales y cuatro regionales, con el año **calculado** (2026)—
volvió a dar **cero agentes nuevos por octava vez**: la capa genérica (openclaw 385k ★, browser-use, Mem0, AutoGen) y
material didáctico *sobre* AI. **Ocho pases confirman la medición del pase 23: en GitHub `education` es «cursos sobre
AI», no «software que educa». El canal de descubrimiento por esa palabra está agotado y conviene dejar de pagarlo.**

### El gap 40 se cierra ejecutando, y no hacía falta la base de datos

El pase 25 dejó el **gap 40** abierto porque CaSS *declaraba* MCP en el README y nadie había listado una tool. Este pase
listó las seis. **No levantando el servidor** —necesita Elasticsearch y en este entorno **no hay demonio de Docker**
(el CLI está, `/var/run/docker.sock` no existe)— sino por donde la arquitectura del propio proyecto lo permite: las
tools se generan con `generateTools(spec)` sobre el OpenAPI que `swagger-jsdoc` arma desde los comentarios del código,
**y eso es puro y corre sin base de datos.** Se replicaron las opciones exactas de `src/main/server.js`, se validó el
spec con el mismo `openapi-schema-validator` que el servidor usa al arrancar, y se corrió el generador real.

**51 paths, 0 errores de validación, 6 tools, 3 resource templates.** Las dos que importan:
**`record_evidence`** (`POST /api/xapi/statement`) y **`get_learner_profile`** (`GET /api/profile/latest`) — *entrar
evidencia xAPI, sacar perfil de competencia, por MCP, Apache-2.0*. Son **exactamente los dos pasos que el paso 4 de
P48 tenía inferidos de una línea de README**. La tendencia **65** deja de ser promesa y pasa a capacidad medida
(tendencia **66**). Tabla completa en `agents/top.md`.

**El hallazgo de diseño, que corrige una suposición razonable:** de los 51 paths, el cartucho expone **6**. Hay **45
`x-mcp-ignore: true`** puestos uno por uno en el código. **La superficie MCP de CaSS está curada, no volcada** — y lo
que queda afuera incluye `POST /api/xapi/statements`, el *bulk* del LRS. **Por MCP se escribe un statement por llamada,
no lotes.** Quien cotice ingestión masiva por esta puerta cotiza mal (**gap 41**).

### El lado LMS: la acción del pase 25 quedó bloqueada por el entorno, y la pregunta de fondo igual se contestó

La acción 1 era *«levantar `LtiAdvantagePlatform` (MIT) contra `ltijs` y medir si el launch OIDC cierra»*. **Bloqueada,
y se dice por qué:** es **ASP.NET Core 10**, acá **no hay `dotnet`**, y no se puede instalar porque
`https://dot.net/v1/dotnet-install.sh` devuelve **`CONNECT tunnel failed, 403`** por el proxy. El *launch* de punta a
punta **sigue sin medirse** y queda como acción.

**Lo que sí se midió es la pregunta que estaba debajo.** Se instaló `ltijs` (**5.9.9, Apache-2.0**) y se inspeccionaron
sus exports: **`[ 'Provider' ]`**, uno solo, sin clase de *platform*; y su `package.json` dice *«turn your web
application into a LTI 1.3 **Learning Tool**»*. **`ltijs` es tool-side y nada más, medido.** Con eso, y verificando dos
candidatos nuevos, el mapa del lado plataforma queda completo sobre **seis** piezas — y la respuesta es **que no existe
permisivo y productivo**: las dos permisivas se autodenominan *«Sample»* y *«example»*, la única completa y **certificada
1EdTech** es **GPL-2.0** (`oat-sa`), y `macewan-cs/lti` (**MIT**, 8 ★) resultó ser **tool-side**, no el lado LMS que el
resumen de búsqueda sugería. **Esta KB no puede proponer el lado LMS con licencia permisiva, y ahora está medido sobre
seis candidatos en vez de supuesto sobre dos** (gap **42**, tendencia **67**).

### La corrección de licencia del pase, sobre el único conector MCP de Moodle que existe

El resumen de búsqueda vendía `csmediapro/moodle-mcp-server` como *«open-source, plugin-extensible, LLM-agnostic»* con
instalación por `npx`. **La página del repo dice dos cosas peores:** es **AGPL-3.0** —la licencia que más molesta en un
entregable SaaS— y es **open-core**: los diez tools abiertos son **sólo de lectura**, y *Advanced Reporting*, *User
Analytics*, *User Directory* y *Compliance Pack* son **plugins premium que se venden aparte**. Con **0 ★ y 0 forks**.
**Moodle es el LMS más instalado del planeta y su único conector MCP es AGPL con lo útil cerrado** (gap **43**, patrón
**P51**).

### Re-verificación que vale como señal de vida: `learnmcp-xapi` no se movió

Se re-verificó el puente xAPI que esta KB tiene desde el pase 6: **MIT, 15 ★, 4 forks, 32 commits, 3 tools**, backends
`lrsql`/Ralph/Veracity. **Idénticos a los registrados.** La ficha de la KB era correcta — y el hecho de que no haya
movido ni una estrella ni un commit es el dato: **sigue siendo referencia de integración, no dependencia de producción**,
tal como la fila lo advierte.

### Lo que este pase NO hizo, declarado como tal

- **No hizo *handshake* MCP real** con el cartucho de CaSS: se midió la **generación** de las tools (determinista y pura
  sobre el spec), no su **invocación**, que necesita Elasticsearch y por lo tanto Docker. Queda como acción.
- **No midió el launch LTI de punta a punta**: sin `dotnet` y con dot.net bloqueado por el proxy.
- **No encontró nada en dos de los cinco estándares del eje conector**, y se declara: `MCP server` + **OneRoster** y
  `MCP server` + **CASE** no devolvieron ningún repo verificable. Peor: **`CASE` colisiona como término** —la búsqueda
  se llena de *certificaciones* de MCP (MCPA del Linux Foundation, certs de Claude), igual que `education` colisiona con
  *cursos sobre AI*. **Es la segunda colisión de término medida por esta KB.** Para QTI apareció un *Question Bank MCP
  Server* listado en Glama **sin repo de GitHub localizable: no se registra como hallazgo** (gap **44**).
- **No verificó fecha de último commit** de ninguno de los repos nuevos: la página no la expone de forma legible vía
  WebFetch en esta sesión. Las señales de vida son commits totales, forks y ★.

## 🔵 Las tres acciones que este pase deja escritas para el siguiente

1. **Hacer el *handshake* MCP real contra el cartucho de CaSS.** Es lo que falta para que el cierre del gap 40 sea de
   punta a punta. Necesita Elasticsearch: o un entorno con demonio de Docker, o un ES embebido/stub que satisfaga a
   `SkyrepMigrate` (el log se queda en *«Waiting for Elasticsearch to appear at http://localhost:9200»*, así que el
   punto exacto a destrabar está localizado). Con el servidor arriba, `POST /api/mcp` e `initialize` → `tools/list`
   y comparar contra las **6** medidas acá. **Si coinciden, P48 y P50 se pueden cotizar sin asterisco.**
2. **Seguir el eje conector en los tres estándares que quedaron sin barrer**: `MCP server` + **Open Badges**,
   + **SCORM**, + **Caliper** (sabiendo que Caliper dejó de ser open source el 2023-06-17, así que ahí el hallazgo
   esperable es la **ausencia**, y hay que escribirla). Y **buscar `canvas-mcp` como patrón, no como repo**: si existe
   un conector MIT de 102 tools para Canvas, preguntar explícitamente por el equivalente de **Moodle** y de
   **Open edX** — el gap 43 dice que para Moodle no existe, y Open edX **no se buscó**.
3. **Cerrar el lado *platform* por el único camino que queda abierto:** leer la licencia y el estado real de la
   **implementación de referencia de 1EdTech en Ruby on Rails** (platform + tool), que apareció en el barrido de este
   pase y **no se verificó**. Es la última candidata no mirada; si también es copyleft o *sample*, el gap 42 pasa de
   «medido sobre seis» a **cerrado por agotamiento**, y eso habilita decirle a un cliente *«el lado LMS se presupuesta
   como desarrollo»* con la evidencia puesta.

## 2026-10-01 (pase 25) — séptimo pase sin altas de agentes, y el pase que encontró la puerta de agente donde no la buscaba: un estándar educativo con cartucho MCP

**La tabla principal sigue en 37 filas.** Se corrió el barrido completo obligatorio —las cuatro búsquedas globales y las
cuatro regionales, con el año **calculado** (2026)— y **no apareció ni un agente educativo que esta KB no tuviera.** Es la
séptima pasada consecutiva sin altas, y a esta altura **el dato ya no es la ausencia: es que la ausencia se explica y la
explicación se confirmó por tercer pase seguido.** Candidato por candidato:

| Candidato que trajo la búsqueda | Qué es | Por qué no entra en `agents/top.md` |
|---|---|---|
| **openclaw** (385.407 ★), **dify** (151.639 ★), **browser-use** (108.128 ★), **Mem0** (62.735 ★), **AutoGen** (60.284 ★), **Flowise** (55.226 ★) | Agentes y orquestadores de propósito general | **Ya en la KB o fuera de dominio.** El barrido global de *«open source AI agents»* devuelve la capa genérica por **séptima** vez, con las mismas cifras que el pase 24 |
| **`rohitg00/ai-engineering-from-scratch`** (#1 en GitHub Trending el 2026-05-24), **Awesome LLM Apps** (133k ★), **Prompt Engineering Guide** (77,6k ★), **`free-ai-agents-resources`**, **`speedyapply/2026-AI-College-Jobs`** (5,2k ★) | Cursos, listas y bolsas de trabajo **sobre** AI | **No es software que educa: es material didáctico sobre AI.** Tercera confirmación consecutiva del fenómeno que midió el pase 23 |
| **Hermes Agent** (Nous Research), **Aider**, **Cline**, **CrewAI**, **LangGraph** | Agentes de código y frameworks multi-agente | Fuera de dominio |
| **LearnUpon** (nueva sede APAC en Sídney + autoría de cursos con AI), **NIIT MTS**, **TCS + Pearson**, **Cisco / IBM / BT / Rolls-Royce** (socios del AI Adoption Summit del Reino Unido) | Plataformas y alianzas **comerciales** de formación | **No son open source.** Van a `intel/market.md` como *players* |
| **OpenEduCat**, **CK-ERP** | ERP educativo sobre Odoo y ERP/CRM educativo de 32 módulos | **No son agentes: son plataformas.** Van a `verticals/solutions.md` |

### 🔴 El hallazgo de agente del pase, y vino por la puerta de los estándares: `cassproject/CASS` expone **MCP**

**Es la primera vez que esta KB encuentra una pieza de estándar educativo con puerta nativa de agente.** CaSS
(Apache-2.0, 62 ★, 29 forks, 2.123 commits — verificado de primera mano) hospeda marcos de competencias, **registra
aserciones de logro individual y computa perfiles del aprendiz**, y entre sus cartuchos de interoperabilidad
—**IMS CASE, xAPI, CTDL-ASN, ASN, Open Badges 2.0**— hay uno de **MCP**.

**Por qué importa más que una fila más en la tabla.** Siete pases buscaron *agentes educativos* y encontraron agentes
genéricos. Este pase no encontró un agente nuevo: **encontró el enchufe por el que los agentes que la KB ya tiene se
conectan al expediente de competencias del alumno.** La diferencia operativa es grande: un tutor que lee competencias por
MCP desde CaSS **no necesita que nadie le escriba un adaptador**, y lo que devuelve queda como *aserción* en un servidor
de estándares, no como texto en un chat. Es la pieza que faltaba entre la capa de estándares y la capa de agentes de esta
misma KB. Ver el patrón **P48** y la tendencia **65**.

### La consigna del pase 24 se ejecutó entera, y conviene registrar que rindió por segunda vez consecutiva

La instrucción era precisa: barrer los artefactos **`item bank`**, **`proctoring`**, **`timetable`** y
**`competency framework`/CASE**, y los estándares **Caliper**, **CASE** y **xAPI Profiles**, más *«buscar `LTI platform`
explícitamente»*. **Se hizo los siete, y el rendimiento fue el más alto del eje hasta ahora: 18 repos verificados de
primera mano, 17 nuevos para esta KB** (ver `repos/trending.md`), más **dos correcciones a conclusiones del propio pase 24** y **una decisión de
estándar con fecha** (Caliper, tendencia **63**).

🔵 **Dos de los tres resultados más valiosos del pase no son repos: son límites medidos.** Que no exista *item bank* QTI 3
certificado en open source, y que **toda** la capa de proctoring sea copyleft o de pesos no comerciales, son hallazgos de
decisión: ahorran una propuesta mal armada. **Un pase sin altas que mide dos límites rinde más que un pase con tres filas
de relleno** — y van siete pases en que esta KB elige eso.

**La consigna para el pase 26, y cambia de eje porque el artefacto ya rindió dos veces y queda poco sin barrer:**
1. **Cerrar los artefactos que faltan**, que son los menos: **`admissions`/matrícula**, **`library`/OPAC** (ILS: Koha, Evergreen) y **`alumni`/*student success*** (predicción de deserción, que es Annex III).
2. **Cambiar el eje de nuevo, y hacia donde este pase mostró tracción: el `pluggable cartridge`.** CaSS resultó valiosa por sus cartuchos, no por su core. **Buscar por el conector, no por el sistema:** `MCP server` + los estándares que esta KB ya tiene inventariados (**OneRoster, CASE, xAPI, QTI, LTI**). Si hay un servidor MCP por estándar educativo, es la capa de integración entera de esta KB convertida en herramientas de agente.
3. **Una verificación que este pase dejó pendiente y es barata:** `LtiLibrary/LtiAdvantagePlatform` dice **ASP.NET Core 10** y es **MIT con AGS+NRPS+Deep Linking** — **levantarla contra un *tool* real** (`ltijs`, Apache-2.0, 373 ★) y medir si el *launch* cierra de punta a punta. Si cierra, esta KB puede proponer **el lado LMS** con licencia permisiva, que es lo que no podía hacer hasta el pase 24. Si no cierra, hay que escribirlo: *«sample»* está en su propia descripción.

## 2026-10-01 (pase 24) — sexto pase sin altas de agentes, pero el pase que dejó de leer código y lo ejecutó: la medición corrigió una conclusión que la KB había escrito con confianza

**La tabla principal sigue en 37 filas.** Se corrió el barrido completo obligatorio —las cuatro búsquedas globales y las
cuatro regionales, con el año **calculado** (2026)— y **no apareció ni un agente educativo que esta KB no tuviera.** Es la
sexta pasada consecutiva sin altas. Candidato por candidato:

| Candidato que trajo la búsqueda | Qué es | Por qué no entra en `agents/top.md` |
|---|---|---|
| **openclaw** (385.407 ★), **browser-use** (108.128 ★), **Mem0** (62.735 ★), **AutoGen** (60.284 ★), **Flowise**, **dify** (151.639 ★) | Agentes y orquestadores de propósito general | **Ya en la KB o fuera de dominio.** El barrido global de *«open source AI agents»* devuelve la capa genérica por sexta vez |
| **`rohitg00/ai-engineering-from-scratch`** (#1 en GitHub Trending el 2026-05-24), **`free-ai-agents-resources`**, **Awesome LLM Apps** (133k ★), **Prompt Engineering Guide** (77,6k ★) | Cursos y colecciones **sobre** AI | **No es software que educa: es material didáctico sobre AI.** Es exactamente el fenómeno que el pase 23 midió, y este pase lo vuelve a confirmar sin excepción |
| **Hermes Agent** (Nous Research), **Aider**, **Cline**, **CrewAI**, **LangGraph** | Agentes de código y frameworks multi-agente | Fuera de dominio |
| **LearnUpon**, **NIIT MTS**, **TCS + Pearson**, **Alteryx Academy** (del barrido APAC) | Plataformas y alianzas **comerciales** de formación corporativa | **No son open source.** Van a `intel/market.md` como *players*, no acá |
| **Ednova** (Chile), **Kredi**, **MindHealth LATAM** (del barrido LATAM) | Startups de edtech/fintech/healthtech | **No son open source.** Ednova queda registrada en `intel/market.md` como edtech LATAM nombrada en la fuente |

🔴 **Y la consigna del pase 23 rindió en su primer uso, lo cual es el dato de método del pase.** La instrucción era:
*«no alcanza con cambiar el sustantivo — hay que evitar la palabra `education` y buscar por el artefacto del dominio o por
el estándar instalado»*. Se hizo: cuatro búsquedas por `gradebook`+OneRoster+LTI, por QTI 3 *item bank*, por IEP y por
SIS/matrícula/asistencia/legajo. **Trajeron seis repos verificados de primera mano, cinco nuevos** — y el hallazgo de
encuadre del pase: **la capa LTI de esta KB era íntegramente PHP** y existe una **familia Java/Spring MIT** publicada por
la Universitat Oberta de Catalunya. Ver `repos/trending.md` y la sección nueva de esta misma tabla.

**La consigna para el pase 25 es una continuación, no un cambio de eje** —porque el eje no se agotó, rindió—: quedan sin
barrer los artefactos **`item bank`**, **`proctoring`**, **`timetable`** y **`competency framework`/CASE**, y los
estándares **Caliper**, **CASE** y **xAPI Profiles**. Y una consigna específica: **buscar `LTI platform` explícitamente**,
porque todo lo que esta KB registró en seis pases es *tool-side* (el lado de la herramienta) y las dos únicas piezas
*platform-side* aparecieron en este pase — **una de ellas sin licencia declarada**. Un stack que sólo sabe ser herramienta
no puede proponer el lado LMS.

### El pase no vino a buscar agentes: vino a ejecutar la acción del pase 23, y la ejecución corrigió al pase 23

El pase 23 dejó escrita una acción precisa: *«levantar `lrsql` sobre PostgreSQL, borrar un actor con datos en las siete
tablas y leer el valor»*. **Se hizo —PostgreSQL 16.14 y MariaDB 10.11.14 levantados, esquema creado con el DDL propio de
lrsql, el SQL literal de `delete.sql`— y el resultado invierte la conclusión arquitectónica del pase 23.**

| | Lo que el pase 23 dedujo leyendo | Lo que el pase 24 midió ejecutando |
|---|---|---|
| **¿Se puede obtener el desglose por tabla?** | «No, sin **partir el SQL** en siete queries con nombre» | 🔴 **Sí, y sin tocar el SQL.** El driver parte él mismo la cadena y entrega los siete conteos en orden: `[7, 2, 3, 8, 5, 6, 1]` por el bucle `getMoreResults()`, que es JDBC estándar |
| **¿Cuál de los siete números se ve hoy?** | «Un solo valor; cuál de los siete **no se midió y no se infiere**» | **El del PRIMER `DELETE`** (`statement_to_statement`). `executeUpdate()` devuelve el mismo |
| **Tamaño del parche del gap 36** | «4 archivos de 3 backends más el interceptor; refactor de SQL en dos» | **Más chico:** sólo la capa que recoge el resultado. El SQL queda igual y los tres backends simétricos |

🔴 **Y el número que hoy se ve vale `0` para el alumno típico.** El primer `DELETE` de la secuencia es el de
`statement_to_statement`, tabla que sólo tiene filas si las sentencias tienen anidamiento o *voiding*. Medido con el mismo
actor sin esas filas: **25 filas borradas y el único testigo disponible dice `0`**. Eso cambia el consejo: **cablear el
conteo «porque ya está» produce un expediente que afirma algo falso**, y un `0` falso es peor que el `200` vacío del pase
21, porque el `200` no afirma nada. Ver la tendencia **61** y el patrón **P47**.

### El hallazgo que no se buscó, y es el más accionable del pase: en MariaDB el borrado no es inexacto, no ocurre

Armando el fixture sobre MariaDB apareció el **gap 38**. Con `allowMultiQueries` en el default del driver (`false`),
`delete-actor-and-dependents!` **falla entera**: error **1064 / SQLState 42000** en el segundo de los siete `DELETE`.
lrsql trae el parámetro, pero como *fallback* de aero —
`:db-properties #or [#env LRSQL_DB_PROPERTIES "allowMultiQueries=true"]`— así que **cualquier** uso de
`LRSQL_DB_PROPERTIES`, o de `LRSQL_DB_JDBC_URL`, **lo reemplaza y lo apaga en silencio**. Y `doc/env_vars.md` la describe
como *«Optional **additional** DB properties»* con default *«Not set»*: **inexacto en los dos campos** para MariaDB y MySQL.

**Por qué importa más que todo lo anterior de esta cadena:** es el primer hueco de esta KB cuyo síntoma es **la ausencia
del borrado** y no la ausencia de su prueba. El despliegue ingiere, consulta y pasa el *health check* con normalidad,
porque el borrado de actor es la única operación del producto que manda varias sentencias en un paquete. **El fallo
aparece la primera vez que alguien ejerce el derecho al olvido** — el día en que hay expediente abierto y plazo corriendo.
Ver la tendencia **62** y el **paso 0** de **P47**.


## 2026-10-01 (pase 23) — quinto pase sin altas de agentes, y el barrido confirmó el diagnóstico del pase 22: lo que aparece ya no es agente, es plataforma administrativa

**La tabla principal sigue en 37 filas.** Se corrió el barrido completo obligatorio —las cuatro búsquedas globales y las
cuatro regionales, con el año calculado (2026), no fijado— y **no apareció ni un agente educativo que esta KB no tuviera**.
Es la quinta pasada consecutiva sin altas. Lo que trajo el barrido, candidato por candidato:

| Candidato que trajo la búsqueda | Qué es | Por qué no entra en `agents/top.md` |
|---|---|---|
| **Frappe Education** · https://github.com/frappe/education | Gestión académica sobre Frappe Framework. **GPL-3.0** (en `license.txt`), **657 ★**, 1.091 commits — verificado de primera mano | **No es un agente: es plataforma.** Entra en `verticals/solutions.md` (capa SIS) y en `repos/foundations.md`. Su valor es que **cierra la pregunta abierta del pase 21** sobre ERPNext |
| **AureusERP** · https://github.com/aureuserp/aureuserp | ERP genérico. **MIT** ✅, **12k ★**, 3.794 commits, Laravel 13 + FilamentPHP 5 | **No es agente y tampoco es educativo:** no tiene ningún módulo académico. Registrado como **no-hallazgo con su razón** en `repos/trending.md` |
| **AutoGen / AI Agents for Beginners** (Microsoft, 56k ★ cada uno) | Framework multi-agente y curso de 12 lecciones | **Ya en la KB**, y el segundo es material de formación, no un agente educativo. Aparecen en toda búsqueda de *«education AI github»* porque el sustantivo *education* en GitHub significa, mayoritariamente, **cursos sobre AI** y no **AI para educar** |
| **OpenClaw, LangGraph, CrewAI, OpenHands, Codex** | Agentes y orquestadores de propósito general | **Ya en la KB** o fuera de dominio. El barrido global de *«open source AI agents»* devuelve la capa genérica, no la vertical |

🔴 **El hallazgo de método de este pase, y es el que explica los cinco pases secos.** El pase 22 escribió que *«el
rendimiento está en cambiar el sustantivo de la búsqueda, no la región»*. Este pase lo hizo —buscó por **plataforma** y por
**ERP**, no por *agente*— y **volvió a rendir: los dos únicos repos nuevos del pase salieron de ahí.** Pero además dejó
medido *por qué* el eje *«agente educativo»* está agotado: **en GitHub, `education` como término de búsqueda está capturado
por el material didáctico sobre AI** (`AI Agents for Beginners`, `ai-engineering-from-scratch`, cursos de DeepLearning.AI)
**y no por software que educa.** Los dos sentidos comparten la palabra y el primero tiene dos órdenes de magnitud más de
estrellas, así que sepulta al segundo en cualquier ranking.

**La consigna para el próximo pase, que es una corrección de la del pase 22, no una repetición:** no alcanza con cambiar el
sustantivo — hay que **evitar la palabra `education`** y buscar por el **artefacto del dominio** (`gradebook`, `rubric`,
`item bank`, `enrolment`, `attendance`, `IEP`, `transcript`) o por el **estándar instalado** (QTI, OneRoster, xAPI, LTI),
que es cómo esta KB encontró las capas de los pases 6, 9, 11 y 22. Donde la palabra *education* no discrimina, el nombre de
la cosa sí.

### La acción que el pase 22 dejó escrita, ejecutada: el gap 36 queda dimensionado, y la respuesta no es ninguna de las dos que se esperaban

El pase 22 dejó una sub-pregunta concreta y declaró que **no la pudo contestar** porque el clasificador de seguridad del
entorno bloqueó la traza del árbol clonado: *«¿`-delete-actor` ya devuelve los conteos de filas afectadas, o hay que
plomearlos desde la capa SQL? Si ya los devuelve, el parche es una línea; si no, hay que propagarlos.»*

**Se contestó en este pase, clonando `yetanalytics/lrsql` y leyendo los tres backends.** La respuesta es **ninguna de las
dos**, y el detalle está en `intel/trends.md` (tendencia 57) y en el patrón **P45**. En una línea: **los conteos ya existen
en los tres backends** —toda sentencia de borrado declara `-- :result :affected`— **pero el parche es distinto en cada
backend y en ninguno es de una línea**, porque SQLite expone siete conteos y descarta seis, mientras Postgres y MariaDB
tienen un solo nombre HugSQL con siete `DELETE` adentro y por lo tanto **no pueden dar el desglose sin partir el SQL**.

## 2026-10-01 (pase 22) — cuarto pase consecutivo sin agregar agentes, y el barrido obligatorio se agotó por cuarta vez: los dos candidatos que trajo ya estaban en la KB, medidos con más precisión que la web

**La tabla principal sigue en 37 filas.** Este pase corrió el barrido completo —las cuatro búsquedas globales y las
cuatro regionales— y **no encontró un solo agente que esta KB no tuviera**. Vale escribir cuáles trajo, porque un
barrido agotado y documentado es información, mientras que el silencio se lee igual que la cobertura:

| Candidato que trajo la búsqueda | Qué dijo la web | Qué tenía ya esta KB |
|---|---|---|
| **OpenMAIC** | «MIT, v1.0.0 del 2026-08-27, construido con LangGraph» | Registrado con **39,7k ★**, v**1.1.2** del 2026-09-28, 653 commits — y con **la advertencia que la web no da: relicenciado de AGPL-3.0 a MIT en v0.3.0 (2026-06-28)**, así que la licencia permisiva tiene ~3 meses y no cubre el historial |
| **AITutor-EvalKit** | «el primer modelo open source de evaluación de calidad pedagógica, MIT» | Registrado desde el pase 1 con **3 ★**, y **corregido en el pase 4**: el repo canónico del mismo autor (Kaushal Kumar Maurya, MBZUAI) es `UnifyingAITutorEvaluation` (**32 ★**), que publica la taxonomía de 8 dimensiones y MRBench V1/V2/V3 completo |

**Las dos veces la KB estaba más precisa que la fuente, y las dos veces la diferencia era material** —una licencia con
tres meses de antigüedad y un repo canónico equivocado son exactamente los errores que hunden una propuesta—. Es la
cuarta pasada sin altas y **la primera en la que el agotamiento está medido candidato por candidato** en vez de
declarado: las búsquedas que el barrido prescribe ya no alcanzan material nuevo para esta vertical.

**Qué habría que cambiar para que el barrido vuelva a rendir.** Los tres pases que sí movieron la tabla lo hicieron
cambiando el **eje de búsqueda**, no insistiendo con el mismo: el pase 4 buscó *benchmark* en vez de *repo de agente*,
el pase 17 buscó `SKILL.md` + dominio educativo, y **este pase encontró lo que encontró buscando la plataforma
(`LMS open source`) y no el agente**. La consigna operativa para el próximo pase es la misma: **el rendimiento está en
cambiar el sustantivo de la búsqueda, no la región.**

### El pase no vino a buscar agentes: vino a reconfirmar el gap 36, y lo reconfirmó de primera mano

El pase 21 cerró el **gap 33** por refutación leyendo el código de `lrsql`, y dejó el **gap 36** declarado como *«el
más chico y más upstreameable de esta KB»*. Este pase **volvió a clonar `lrsql` y leyó el interceptor por su cuenta**,
porque un hallazgo que invierte el argumento de tres patrones merece una segunda lectura independiente. **Se confirma,
y ahora con el sitio exacto del parche:**

| | |
|---|---|
| **Ruta** | `DELETE /admin/agents`, en `src/main/lrsql/admin/routes.clj:331` — registrada **sólo si** el flag está encendido (`routes.clj:407`), así que apagada el síntoma es **404 y no 403** |
| **Protocolo** | `-delete-actor`, declarado en `src/main/lrsql/admin/protocol.clj:58` |
| 🔴 **El sitio del parche** | `src/main/lrsql/admin/interceptors/lrs_management.clj:23–33`. El cuerpo del interceptor es `(adp/-delete-actor lrs params)` **como expresión suelta, cuyo valor de retorno se descarta**, y la respuesta es `{:status 200 :body params}` |
| **Qué significa `params`** | es el `::data` que dejó el interceptor de validación anterior — o sea **el `actor-ifi` que mandó el cliente**. La respuesta es un eco de la entrada |

**Entonces el gap 36 queda confirmado por lectura independiente y con coordenadas:** no hay registro de auditoría, no
hay evento, y el único testigo del borrado es un `200` que repite lo que uno mandó. Para un expediente del art. 17 o de
**AB 1159** (operativa el **2027-07-01**) eso no es prueba de nada.

⚠️ **Lo que este pase NO pudo verificar, y hay que declararlo porque cambia el tamaño del parche.** Queda abierta una
sub-pregunta concreta: **¿`-delete-actor` ya devuelve los conteos de filas afectadas, o hay que plomearlos desde la
capa SQL?** Si ya los devuelve, el parche es **una línea** —cambiar `:body params` por el valor de retorno—; si no,
hay que propagarlos por la implementación del protocolo. **La traza de la implementación quedó bloqueada por el
clasificador de seguridad del entorno en este pase** (dos denegaciones al explorar el árbol clonado de terceros), así
que la pregunta no se pudo contestar y **no se contestó por inferencia**. Es lo primero que tiene que hacer el próximo
pase sobre este gap, y es una sola lectura: la implementación de `-delete-actor` y su `:result` en la capa SQL.

### Dónde está el hallazgo grande de este pase

No está en esta capa. Está en **`repos/trending.md`**: el stack de analítica **oficial** de Open edX (**Aspects**,
Apache-2.0) instala **Ralph sobre ClickHouse** —la configuración que el pase 21 declaró imposible de borrar, que
resulta no ser una elección del cliente sino el default de la plataforma— y al mismo tiempo **trae el disparador de
supresión LMS → telemetría que el pase 19 probó que no existe en Moodle**, como listener Apache-2.0 de una señal
Django. Eso corrige una advertencia de **P44**, cambia el estado de **P40**, y abre el **gap 37**.

## 2026-10-01 (pase 21) — tercer pase consecutivo sin agregar agentes a la tabla, y el primero que corrige una afirmación que esta KB venía vendiendo al revés: el almacén permisivo que recomienda sí sabe borrar al alumno

**La tabla principal sigue en 37 filas.** Este pase no buscó agentes: fue a **ejecutar la acción 1 del pase 19** —
confirmar la API de borrado de la capa de telemetría (**gap 33**)—, declarada ahí como la pregunta de mayor rendimiento
y salteada por el pase 20. Se ejecutó **clonando los tres LRS y leyendo el código fuente**. El resultado invierte el
argumento de **P38**, **P40** y de la lectura de EMEA/LATAM en `intel/market.md`.

### 🔴 El hallazgo: `lrsql` (Apache-2.0) tiene el mejor primitivo de borrado de la capa, y esta KB decía que no tenía ninguno

El artefacto que esta KB recomienda como **almacén por default** para el agente educativo —`lrsql`, Apache-2.0, en la
KB desde el pase 6 y base de **P15**, **P1**, **P10** y **P14**— expone un endpoint hecho exactamente para el
art. 17 del GDPR:

| | |
|---|---|
| **Endpoint** | `DELETE /admin/agents` (`src/main/lrsql/admin/routes.clj:331`) |
| **Parámetro** | **uno solo: `actor-ifi`** — el identificador xAPI del alumno (`spec/admin.clj:191`) |
| **Qué borra** | cascada sobre **7 tablas** en **una transacción**: `statement_to_statement`, `statement_to_activity`, `attachment`, `xapi_statement`, `agent_profile_document`, `state_document`, `actor` |
| **La 8.ª tabla** | `statement_to_actor` se borra por **`ON DELETE CASCADE`**, agregado por una migración con guarda y comentario explícito del mantenedor |
| ⚠️ **Estado de fábrica** | **apagado**: `LRSQL_ENABLE_ADMIN_DELETE_ACTOR` default **`false`** en la config de producción. La ruta no se registra si el flag está apagado |

**No es un desarrollo: es una variable de entorno.** Y como el borrado es **por actor**, es el único de los tres que
responde un pedido de supresión sin pasos intermedios.

### El gap 36, que es lo que queda del gap 33 después de leerlo bien

`lrsql` **borra de forma completa y atómica, y no deja evidencia de haberlo hecho.** El interceptor responde
`{:status 200 :body params}` — o sea **devuelve el `actor-ifi` que le mandaste**. Y el SQL está declarado
`-- :result :affected`, así que **el número de filas afectadas se calcula y se descarta**. No hay registro de
auditoría, no hay evento, no hay conteo.

Para un expediente del art. 17 —o de **AB 1159** en California, operativa el **2027-07-01**— eso significa que el
borrado ocurre y **lo único que queda como prueba es un `200` con tu propio input adentro**. El gap 36 es, por lejos,
**el más chico y más upstreameable que tuvo esta KB**: el dato ya está calculado en la capa SQL, falta devolverlo y
registrarlo, sobre un repo **Apache-2.0**. Ver **P44** y la tendencia **54**.

### Lo que esto le hace a los patrones que ya estaban vendidos

- **P40** (propagar la supresión del LMS a la telemetría y al modelo) **mejora y se abarata**: el extremo del LRS
  **deja de ser desarrollo** y pasa a ser una llamada HTTP con un flag encendido. Lo que sigue sin existir es **el
  disparador**, igual que el pase 19 encontró en Moodle: `lrsql` no tiene evento de borrado y Learning Locker tampoco
  —expone `total`/`deleteCount`/`processing`/`done` para **sondear**, no para notificar.
- **P38** (derecho al olvido que alcanza al modelo) **cambia de forma**: la mitad «registro» está resuelta en el LRS
  permisivo; la mitad «modelo» sigue siendo el **gap 34**.
- **El argumento de EMEA pierde una pata y gana otra.** `intel/market.md` dice que bajo el art. 17 *«el LRS permisivo
  que esta KB recomienda no sabe borrar»*. **Es falso y hay que corregirlo.** Lo que sí se sostiene, y es más vendible,
  es que **viene apagado** y **no deja evidencia**: eso es una revisión de configuración y un parche chico, no un
  proyecto.

### Ralph y Learning Locker, en una línea cada uno (el detalle está en `repos/trending.md`)

- **Ralph** (MIT, HEAD 2026-09-07, **activo**): **no hay `@router.delete` en ningún router** — sólo GET/PUT/POST. El
  borrado existe en el *data backend*, **por ID de statement**, así que hay que consultar primero. Y
  🔴 **el backend ClickHouse declara `DELETE` como no soportado**: el backend que se elige para analítica a escala es
  el que no puede borrar.
- **Learning Locker** (GPL-3.0): la API de borrado **existe y está confirmada** (`POST /api/v2/batchdelete/initialise`,
  por filtro), después de dos pasadas atribuyéndola a fuente secundaria. Pero **el código no se mueve desde el
  2021-11-16** (`HEAD` = tag v7.1.1) aunque el repo **no está archivado** y su README habla de oferta comercial.
  **«No archivado» no es «mantenido».**

### Lo que este pase NO hizo, dicho explícitamente

- **No agregó agentes.** La búsqueda de agentes educativos nuevos no devolvió ninguno con licencia permisiva y
  tracción que no estuviera ya en la tabla. Se reverificó **DeepTutor** de primera mano por tercera vez
  (**40.6k ★**, Apache-2.0, **2.386 commits**, **v1.6.12 del 2026-09-27**), que **coincide** con lo que registró el
  pase 20 — dos verificaciones independientes concordantes.
- **No cerró los gaps 31, 34 ni 35.** Ninguno se tocó en este pase.
- **No verificó ILIAS de primera mano en su Feature Wiki.** Ver la nota de método del pase 21 en `intel/trends.md`.

## 2026-10-01 (pase 20) — diecinueve pasadas vendieron un expediente de conformidad sin registrar una sola herramienta de testing: existe, es Apache-2.0, la publica un regulador, y su catálogo cubre derecho, medicina y finanzas

**Este pase no agregó agentes a la tabla principal, y es el segundo que termina así a propósito** (el pase 17 fue el
otro). Lo que buscó es la capa que a esta KB le faltaba en el medio: **con qué se corre la prueba**.

### 🔴 El hallazgo: la máquina existe, y educación no está en su catálogo

Desde el pase 4 esta KB vende expedientes de conformidad —**P4** (Anexo III), **P10** (probar que el tutor enseña),
**P11** (gate de seguridad pedagógica), **P17** (accesibilidad), **P39** (privacidad)— y en diecinueve pasadas **no
registró una sola herramienta de testing con la que ejecutarlos**. Existe, y es mejor de lo esperable:

| Pieza | Licencia | ★ | Quién la publica |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | **MIT** ✅ | 2.900 | **UK AI Security Institute** (gobierno británico), 200+ evals pre-construidas |
| `aiverify-foundation/moonshot` | **Apache-2.0** ✅ | 353 | **AI Verify Foundation** (Singapur), *benchmarking* + *red-teaming*, v0.7.6 beta |
| `compl-ai/compl-ai` | **Apache-2.0** ✅ | 211 | **ETH Zürich + INSAIT + LatticeFlow AI**, 29 benchmarks mapeados al EU AI Act |
| `aiverify-foundation/aiverify` | **Apache-2.0** ✅ | 97 | AI Verify Foundation — ⚠️ tabular/imagen supervisado, **no agentes** |
| `aiverify-foundation/moonshot-data` | **Apache-2.0** ✅ | 45 | Conectores, datasets, métricas y *attack modules* de Moonshot |
| `aiverify-foundation/LLM-Evals-Catalogue` | ⚠️ sin licencia | 23 | **El repo con el hallazgo adentro** |
| `aiverify-foundation/moonshot-cicd` | **Apache-2.0** ✅ | 14 | Moonshot GA para pipeline CI/CD (Docker, S3) |
| `aiverify-foundation/moonshot-ui` | **Apache-2.0** ✅ | 12 | Informe HTML con gráficos, export JSON |
| `aiverify-foundation/aiverify-developer-tools` | **Apache-2.0** ✅ | 9 | Plantillas para **plugins de test propios** |

**Y el hallazgo es lo que falta, confirmado por tres catálogos independientes de tres jurisdicciones:**

- **`LLM-Evals-Catalogue`** declara su categoría *domain-specific*: **derecho, medicina, finanzas**. Educación no.
- **`compl-ai`** mapea 29 benchmarks a los 6 principios del AI Act **sin una mención de educación** — y el Anexo III
  del AI Act nombra la educación como alto riesgo de forma textual.
- **`awesome-eu-ai-act`** (**CC0**, 21 ★) lista once herramientas de conformidad open source (Giskard 5.700 ★,
  DeepEval, PyRIT, Inspect, Holistic AI, AI Act Companion, Regula, VerifyWise, AIR Blackbox, Venturalitica SDK,
  Inkog) y **ninguna del sector educativo**.

**La otra punta ya está en esta KB desde el pase 4, y es la parte cara de construir:** `EduBench` (**MIT**, ACL 2026,
9 contextos educativos), `SafeTutors` (**MIT**), `MathTutorBench` (CC BY 4.0, EMNLP 2025 Oral),
`UnifyingAITutorEvaluation` (CC BY-SA 4.0, NAACL 2025). **Ninguno está mapeado a un requisito regulatorio ni
empaquetado como *recipe* de ninguna herramienta.** Ése es el **gap 35**, y las dos puntas son permisivas: MIT de un
lado, Apache-2.0 del otro. **No hay fricción legal en el ensamblado — falta el ensamblado.** Ver **P42**.

### Lo que hay que no prometer, y son cuatro cosas

1. **Ninguna de estas herramientas certifica.** `aiverify` lo declara por escrito: no define estándares éticos y **no
   garantiza** que el sistema evaluado esté libre de riesgos o sesgos. Produce **evidencia**, no conformidad.
2. **El régimen de Singapur es voluntario**: el *Model AI Governance Framework for Agentic AI* no tiene penalidad, ni
   registro, ni *enforcement*. El europeo sí. Moonshot es **herramienta** en Europa, nunca **cumplimiento** europeo.
3. **No hay crosswalk directo de AI Verify al EU AI Act.** Verificados hay dos: a **NIST AI RMF** (oct-2023, el único
   mapeo gobierno-a-gobierno del mundo) y a **ISO/IEC 42001:2023** (jun-2024). Al AI Act se llega **indirecto por ISO
   42001**. Para expediente europeo la pieza es **COMPL-AI**.
4. **`aiverify` no evalúa agentes** — tabular e imagen supervisados. Para un tutor LLM: Moonshot, Inspect o COMPL-AI.

### El segundo hallazgo: el *unlearning* llegó a educación, y entró por la puerta pedagógica

| Repo | Licencia | ★ | Commits | Qué hace |
|---|---|---|---|---|
| `GEMLab-HKU/Unlearn_and_Relearn` | **MIT** ✅ | 4 | 22 | *Unlearning* + *relearning* sobre un modelo de alumno. GEMLab, **Universidad de Hong Kong**. Coach / Teachable Agent / Judge, olvido progresivo 10–50% |

🔴 **No mueve el gap 34, y la razón es interesante: usa la técnica al revés.** No borra para proteger al alumno —
**borra para fabricar un alumno**. Vuelve novato a un modelo que sabe demasiado, porque un LLM al que se le pide
"actuá como principiante" se escapa igual hacia explicaciones de experto y arruina el *learning-by-teaching*. Después
mide cuánto **recupera** cuando el alumno humano le enseña.

**El gap 34 sigue abierto** (*unlearning* evaluado sobre modelos de alumno **por supresión de dato personal**), pero
cambia de forma: **la técnica ya está en educación, con código y MIT. Lo que falta es el uso de privacidad, no la
maquinaria.** Ver **P43**, que lo aprovecha por el lado que sí está listo.

### 🔴 Y una nota de método que explica dos pasadas de búsquedas fallidas

Los pases 18 y 19 buscaron *unlearning* sobre *knowledge tracing* y no encontraron código. **Hay una colisión de
terminología:** «knowledge tracing» significa **dos cosas incompatibles** según la literatura. En esta KB y en `pyKT`
es *modelar el estado de conocimiento del alumno*; en la literatura de *unlearning* es *rastrear qué conocimiento de
un modelo fundacional vino de qué dato* (p. ej. *Lifting Data-Tracing Machine Unlearning to Knowledge-Tracing for
Foundation Models*). Buscar por la técnica devuelve el segundo sentido y **entierra el primero**. Lo que funcionó fue
buscar por **escenario educativo** — la misma regla que el pase 5 aprendió para benchmarks, redescubierta en otra capa.

### Lo que esta pasada buscó y no encontró

- 🚫 **Ninguna herramienta de testing de conformidad de origen LATAM.** No encontrada, **no inexistente**. Y es un
  desajuste fuerte: Brasil (PL 2338/2023, evaluación de impacto algorítmico y auditorías periódicas), Chile (Ley
  21.719 + proyecto de cuatro niveles de riesgo con auditoría) y México (auditoría **al menos anual** para alto
  riesgo) **legislan la auditoría y no construyen la herramienta**.
- 🚫 **Ninguna *recipe* ni plugin educativo** en `moonshot-data`, `aiverify-developer-tools` ni `compl-ai`. Se revisó
  el contenido declarado de los tres. Es el gap 35 medido, no supuesto.
- 🚫 **Ningún caso de uso educativo documentado** de AI Verify o Moonshot. La búsqueda devuelve casos de EdTech
  genéricos (IU International, el tutor por WhatsApp de Ghana) sin relación con estas herramientas.
- ⚠️ **`moe.gov.sg` y `learning.moe.edu.sg` están bloqueados por el proxy de egreso de esta sesión**, así que todo lo
  de la plataforma SLS de Singapur de este pase viene de **fuentes secundarias concordantes**, no de leer al MOE.

## 2026-10-01 (pase 19) — cinco agentes nuevos, y el hallazgo es que el pase anterior explicó bien un dato con una causa falsa

Dos cosas en este pase. La chica: **+5 en la tabla principal** y **una región cerrada**. La grande: **el pase 18 se
apoyó en una afirmación falsa sobre `moodle/moodle`**, y corregirla deja ver lo que su hallazgo realmente era.

### Los cinco nuevos, verificados uno por uno

Entraron por una consulta que dieciocho pasadas no habían hecho: **el *topic* `ai-tutor` de GitHub**, que es donde el
ecosistema se autoclasifica. Las pasadas anteriores buscaron por `agent`, `benchmark`, `tutoring system` y `tutor`;
ninguna por la etiqueta que usan los propios autores.

| Repo | Licencia | ★ | Commits | Qué aporta que la KB no tenía |
|---|---|---|---|---|
| **human-skill-tree** | **AGPL-3.0** ⚠️ (sólo `skills/` en doble MIT/AGPL) | 562 | 36 | 33 skills, **15 sistemas educativos nacionales y 800+ materias** declarados. El mayor alcance curricular de la tabla |
| **universal-examprep-skill** | **MIT** ✅ | 299 | 181 | **Citación obligatoria `archivo p.N` + 100 % de abstención fuera de alcance.** Es una propiedad regulatoria, no pedagógica |
| **algo-sensei** | **MIT** ✅ | 281 | 8 | **Pistas en 5 niveles y negativa explícita a dar la solución.** *«Productive struggle with guidance»* |
| **universal-diagnostic-tutor-skill** | **MIT** ✅ | 235 | 57 | *Diagnosis-first*: localiza el hueco en 4 niveles antes de enseñar. **«Learning State Cards» visibles al alumno** |
| **lumen** | **GPL-3.0** ⚠️ | 88 | 828 | RAG con alcance por curso y citación detrás de un autorizador único; MCP con 9 tools; **publica sus propios puntajes malos** |

**Tres observaciones de forma, que valen más que las cinco filas:**

1. **Cuatro de los cinco se entregan como *skill* instalable**, no como aplicación. La capa de distribución que abrió
   el pase 12 ya no es una curiosidad: es **cómo se publica la pedagogía en esta ventana**.
2. **La licencia y la tracción están desacopladas al revés de lo esperado.** Lo más estrellado del lote
   (`human-skill-tree`, 562 ★) es **AGPL-3.0** y sólo reutilizable en su subdirectorio `skills/`; lo más reutilizable
   es MIT y tiene **8 commits** (`algo-sensei`). Se repite el patrón del pase 7.
3. **`lumen` cierra región: Alemania (EMEA)** — el autor declara `Essen, Germany`. Y es el único artefacto de toda
   esta KB que **publica los resultados en los que su propio *eval* sale mal**. Eso es citable ante un cliente como
   estándar de honestidad de medición, independientemente de si el repo se usa.

### 🔴 La corrección: `moodle/moodle` sí tiene rama `main`, y los 404 medían otra cosa

El pase 18 escribió, en este mismo archivo, que *«`moodle/moodle` no tiene rama `main` ni rama `master`»* y con eso
explicó los cuatro 404 del pase 17. **Es falso.** Verificado con `git ls-remote`, que lista refs en vez de inferirlas:

```
$ git ls-remote --heads https://github.com/moodle/moodle | grep -v 'MOODLE_[0-9]*_STABLE$'
85af0b5dc354bf03c73db60079c232f004e01433    refs/heads/main
```

`main` existe y es **Moodle 5.3rc1**. Lo que no existe es `master`. **Y la causa real de los 404 es mejor, porque es
reutilizable:** **Moodle movió su *webroot* a `public/` en la serie 5.x.** En `main` la ruta no es
`ai/provider/ollama/...` sino **`public/ai/provider/ollama/...`**. Eso explica, sin contradicción, la tabla de
evidencia del pase 18: 404 en `main` (ruta movida) y 200 en `MOODLE_405_STABLE` y `MOODLE_500_STABLE` (donde `ai/`
todavía estaba en la raíz). **Los 404 midieron la ruta, no la rama.**

> **Lección de método, y es la tercera vez que esta KB tropieza con lo mismo:** un 404 nunca dice *«no existe»*, dice
> *«no está donde preguntaste»*. El pase 17 lo leyó como ausencia, el pase 18 como nombre de rama, y era una
> reestructuración del árbol. `git ls-remote` cuesta un segundo y responde la pregunta de la rama **sin inferir**;
> para la ruta, lo único que sirve es mirar el árbol.

### Y con la ruta correcta, el hallazgo del pase 18 cambia de tamaño y de signo

No son tres proveedores de AI con `privacy provider`: son **siete** (`anthropic`, `awsbedrock`, `azureai`,
`deepseek`, `gemini`, `ollama`, `openai`), más el del subsistema y dos de *placement* = **10 archivos**. El pase 18
dio por ausentes a `anthropic` y `bedrock`; los dos están, y el segundo se llama **`awsbedrock`** — ese 404 también
midió un nombre.

Auditados uno por uno sobre el fuente, los siete son **idénticos**: 70–78 líneas, **cero** llamadas a
`delete_records` / `DELETE FROM` / `add_database_table`, y **exactamente un** `add_external_location_link`. Todos sus
métodos de borrado tienen el cuerpo vacío, con `@codeCoverageIgnore`.

**El pase 18 acertó en que eso es deliberado** —y conviene no perder ese acierto en la corrección—. Lo que estaba mal
es el titular: **siete shims de declaración no son «implementaciones de referencia» de un `privacy provider`**,
porque lo que necesita copiar un plugin que *sí* guarda dato es exactamente lo que ellos no tienen. La plantilla real
existe y el pase 18 no la nombró: **`public/ai/classes/privacy/provider.php`** (`core_ai`), ~800 líneas, **6 tablas**
—con `prompt` y `generatedcontent` entre sus campos— y `delete_records_list()` de verdad en las tres variantes de
borrado.

**Y leído así, el hallazgo es más fuerte que como lo escribió el pase 18:** los siete shims no son un descuido, son
una **declaración**. Lo único que hacen es declarar que el *prompt* del alumno sale hacia un tercero. El núcleo de
Moodle documenta, en siete archivos idénticos, **el punto exacto donde su propia maquinaria de supresión se queda sin
nada que suprimir** — porque el dato ya está en OpenAI, Anthropic, Google, AWS, Azure, DeepSeek o en el Ollama de
alguien. Ver las tendencias **48**, **49** y **50**.

## 2026-10-01 (pase 18) — el gap 29 se cerró con la pieza del propio vendor, y las dos mitades del derecho al olvido tienen licencias opuestas

El **gap 29** del pase 17 pedía *«un `privacy provider` de referencia para un plugin de AI»* y lo declaraba
inexistente después de buscarlo. **Existe desde Moodle 4.5 y está en el núcleo**: `ai/provider/openai`,
`ai/provider/azureai` y `ai/provider/ollama` traen cada uno su `classes/privacy/provider.php`. El gap era
**verdadero cuando se escribió sobre terceros y falso sobre el núcleo**, y la diferencia la explica un detalle
mecánico que vale más que el hallazgo.

### 🔴 Por qué el pase 17 no lo encontró, y es una lección de método reutilizable

El pase 17 escribió, con honestidad, que intentó el árbol de Moodle *«por cuatro rutas (`main` y `master`, árbol y
archivo) y las cuatro dieron 404»*. La causa:

> **`moodle/moodle` no tiene rama `main` ni rama `master`.** Las ramas son `MOODLE_405_STABLE`,
> `MOODLE_500_STABLE`, etc. Un fetch contra `main` da 404 aunque el archivo exista.

Medido en este pase por código HTTP: `ai/provider/openai/classes/privacy/provider.php` da **404 en `main`**, **404
en `master`** y **200 en `MOODLE_405_STABLE` y `MOODLE_500_STABLE`**. Lo mismo
`admin/tool/dataprivacy/version.php` y `admin/tool/policy/version.php`, que pasan a **verificados de primera
mano**.

**La generalización, porque va a volver a pasar:** cuando un 404 contra un repo grande y vivo contradice la
documentación del vendor, **el 404 es sobre la rama, no sobre el archivo**. Antes de declarar una ausencia en un
repo con releases versionadas, probar la rama de release.

### Lo que se midió de la capa de la comunidad, y el reparto es el dato

Seis piezas abiertas una por una mirando `classes/privacy/`. **Tres tienen `provider.php` y tres no.** Y el
ranking de completitud no sigue el de estrellas ni el del PIB:

| Pieza | Interfaces implementadas | Licencia | ★ | Región del autor |
|---|---|---|---|---|
| `jeanlucio/moodle-local_aihub` | **4** (incluye `user_preference_provider`) | GPL-3.0 | 0 | **LATAM — Instituto Federal do Sertão Pernambucano, Brasil** |
| `Universita-di-Ferrara/moodle-aiprovider_gemini` | 3 | GPL-3.0 | 3 | EMEA — Università di Ferrara, Italia |
| `alvarogregori/moodle-ai-graded-assignment` | 3 | 🚫 sin `LICENSE` | 0 | no declarada |
| `sngdtechnologies/ai-moodle-security` | 🚫 ninguna | **BSD-2-Clause** | 0 | no declarada |
| `marcusgreen/moodle-tool_aiconnect` | 🚫 no vista | 🚫 no mostrada | 10 | EMEA — Catalyst EU |
| `moodlehq/moodle-tool_dataprivacy` | — (es la máquina) | GPL-3.0 | 8 | EMEA — archivado 2020-09-24, **se mudó al núcleo** |

**La más completa de la capa es la brasileña**, y por un margen real: declara tabla de base, **6 preferencias de
usuario** y **4 enlaces externos**, con CI, tests y docs en el repo. El **gap 2** de esta KB dice desde el pase 2
que *«LATAM produce agentes educativos, pero ninguno sale de la fase cero»*. Esta pieza tiene 0 estrellas —fase
cero en adopción— y **disciplina de ingeniería por encima de todo el resto de la capa**. El pase 13 ya había
reencuadrado el gap 2 diciendo que el aporte de LATAM no era el repo sino el instrumento. Acá es otra cosa: **es
el repo, y es el mejor de su capa.** Lo que le falta no es calidad: es visibilidad.

### 🔴 La línea de `aiprovider_ollama` que hay que leer antes de vender «el dato no sale»

El proveedor Ollama del núcleo es el que un cliente elige para que nada salga. Y el núcleo **le declara un envío
externo igual**. La cadena literal: *«No user data is **explicitly** sent to Ollama or stored in Moodle LMS by this
plugin.»*

**«Explicitly» es la palabra.** El plugin no manda identidad; `prompttext` sí viaja, y el prompt lleva lo que el
alumno escribió. **La declaración es exacta sobre la identidad y silenciosa sobre el contenido.** Es una línea en
el expediente de **P35** y ahorra la discusión entera.

### La capa nueva: *unlearning*, y confirma la predicción del pase 17 palabra por palabra

El pase 17 dejó escrito: *«`machine unlearning` es el término que este pase no buscó y es el que podría tener
oferta madura: si existe una librería permisiva de *unlearning* aplicable a modelos de knowledge tracing, el gap 30
cambia de forma»*. Se buscó. **Existe y es grande:** `tamlhp/awesome-machine-unlearning` **MIT 970 ★**,
`jjbrophy47/machine_unlearning` 965 ★, `chrisliu298/awesome-llm-unlearning` **Apache-2.0 627 ★**,
`locuslab/open-unlearning` **MIT 607 ★**, `OPTML-Group/Unlearn-Saliency` **MIT 154 ★** (ICLR 2024 Spotlight),
`Harry24k/machine-unlearning-pytorch` **MIT 12 ★** (NeurIPS 2025), `cisco-ai-defense/model-provenance-kit`
**Apache-2.0 104 ★**, `Data-Provenance-Initiative/Data-Provenance-Collection` **Apache-2.0 281 ★**.

**El contraste con el pase 17 es el hallazgo, y es exacto:**

| Mitad del derecho al olvido | Dónde vive | Licencia | ¿La usa la educación? |
|---|---|---|---|
| Borrar **el registro** del alumno | Instalado en el LMS (Privacy API, `tool_dataprivacy`, retiro de Open edX) | **Toda copyleft** (GPL-3.0 / AGPL-3.0) | Sí, viene de fábrica |
| Borrar **la influencia sobre el modelo** | Librerías horizontales de ML | **Toda MIT / Apache-2.0** | **No. Cero.** |

Los dos agregadores más grandes de la capa —970 ★ y 627 ★— **no mencionan educación, dato de alumno ni knowledge
tracing en ninguna parte**. Verificado buscando los términos.

### Y el paper que sí es de esta industria no publica código

**PrivacyCD** (arXiv **2511.03966**) se declara *el primer estudio sistemático de data unlearning para modelos de
cognitive diagnosis* —la **misma capa** de `pyBKT` y `pyKT`— y aporta **HIF**, con el argumento de que los métodos
genéricos son subóptimos frente a la estructura heterogénea de los modelos de CD. **No se ubicó repositorio
público.** Tercera capa de esta KB donde la pieza más específica es la que no publica (pases 10, 11 y ahora 18).

### La conclusión de ingeniería del pase, y decide qué se promete

- **`pyKT` es PyTorch** → `torchunlearn` y `SalUn` son aplicables. Integración, no investigación.
- **`pyBKT` no es PyTorch** (BKT por EM) → ninguna librería lo alcanza, y la respuesta correcta **no es
  unlearning: es reajustar sin el alumno**. Para BKT es barato y además es ***exact unlearning***, la garantía más
  fuerte que existe. **Mejor resultado legal por menos trabajo.**

### ⚠️ Dos notas de verificación de este pase

1. **La primera búsqueda de `open-unlearning` devolvió un fork con 0 ★** (`aflah02/open-unlearning`) en lugar del
   canónico `locuslab` con 607 ★. README idéntico, licencia idéntica, lista de métodos idéntica. Lo único que lo
   delata es «forked from» y el contador en cero. **Ningún repo entra a esta KB sin mirar si es fork.**
2. **La lectura de la página rendida se contradijo con el fuente, y el fuente ganó.** El resumen de la página de
   `aiprovider_gemini` afirmaba que el provider tenía *todos* los métodos vacíos y por tanto no declaraba el envío
   externo. **Leyendo el `.php` crudo, declara `add_external_location_link` con cuatro campos.** La conclusión
   contraria se iba a escribir como hallazgo del pase. **Para una afirmación de cumplimiento, leer el fuente, no
   el resumen.**

Ver los **gaps 31 y 32**, las tendencias **45**, **46** y **47**, y los patrones **P38** y **P39**.

---

## 2026-10-01 (pase 17) — el gap 20 se cerró: ya existe skill educativa con eval publicada, es Apache-2.0, y el techo permisivo del canal subió de 299 a 541 estrellas

El **gap 26** del pase 15 dejó una acción textual: *«medir el canal otra vez, pero buscando por `SKILL.md` +
dominio educativo en vez de por repos educativos — que es el error de método que el pase 12 ya documentó».* **Este
pase la ejecutó y encontró lo que doce y quince no vieron**, por el mismo motivo que el pase 14: la consulta
estaba mal, no el canal.

**La tabla principal de `agents/top.md` no cambió y el conteo sigue en 31.** Lo nuevo son paquetes de *skills*,
no agentes, y van a la capa de distribución por *skills* al final de ese archivo. Decirlo importa porque el pase
12 abrió esa capa y el pase 17 la cierra en su mitad peor: la de la licencia y la de la evidencia.

### 🔴 El hallazgo del pase: el gap 20 era verdadero cuando se escribió y es falso ahora

El **gap 20** del pase 12 decía: *«Ninguna skill educativa del mundo tiene eval publicada, y esta KB tiene las
herramientas para medirlas sin usarlas.»* Se verificó contra los siete paquetes de entonces y era correcto.

**Ya no lo es** — y hay que decir con precisión qué parte es hallazgo nuevo y qué parte es error de medición
propio, porque **uno de los dos repos ya estaba en la KB**. El gap 20 enumeraba siete paquetes e incluía
`learning-commons-org/agent-skills` (35 ★), concluyendo que todos eran *«texto de prompt sin versionado
semántico, sin suite de regresión y sin medición de efecto pedagógico»*. **Ese repo tiene una carpeta `evals/`
con rúbricas, verificada de primera mano en este pase.** Lo que no se puede afirmar es *desde cuándo*: este pase
no pudo datar la carpeta, así que **no se sabe si el pase 12 la pasó por alto o si es posterior**. Se registra la
duda en vez de resolverla a favor propio.

Lo que sí es inequívocamente nuevo en esta KB es el otro repo, y es el grande:

| Repo | Licencia | Stars | Skills | Eval publicada |
|---|---|---|---|---|
| https://github.com/anthropics/k12-teacher-skills | **Apache-2.0** ✅ | **541** | 4 | **Sí** — carpeta `evals/` con el framework de evaluación y cómo adaptarlo |
| https://github.com/learning-commons-org/agent-skills | **Apache-2.0** ✅ | 35 | 4 | **Sí** — `evals/` con rúbricas de **pedagogía, rigor, formato y andamiaje del modelo** |

Las cuatro skills son las mismas en los dos repos y están **co-desarrolladas**: `k12-lesson-plan-creation`
(plan de clase alineado a estándar), `k12-lesson-differentiation` (versiones por nivel de competencia y por
necesidad del alumno), `k12-lesson-prep` (socio de preparación sobre una clase existente) y
`k12-check-for-understanding` (chequeos formativos de 1 a 3 ítems para estándares de matemática, **con
distractores y guía docente**). El repo de Learning Commons declara que el conjunto inicial de skills y de
rúbricas evaluadoras se co-desarrolló con Anthropic; el de Anthropic lo declara al revés, «co-developed with
Learning Commons».

### Los dos números que cambian, y conviene no sobrevenderlos

**El techo permisivo del canal educativo subió 1,8×: de 299 ★ a 541 ★.** Hasta este pase, el mejor activo
educativo con licencia permisiva del canal era `universal-examprep-skill` (MIT, 299 ★). Ahora es
`k12-teacher-skills` (Apache-2.0, 541 ★).

**Lo que NO cambia: el activo educativo más grande del canal sigue siendo el que no se puede empaquetar.**
`education-agent-skills` sigue en **815 ★** y sigue siendo **CC BY-SA 4.0** —se reverificó en este pase y además
creció de 152 a **165 skills en 20 dominios**—. Y la comparación con la vertical científica sigue perdida:
`scientific-agent-skills` tiene **47.2k ★ con MIT**, que son **87×** el nuevo techo permisivo educativo. El pase
12 midió 58× contra el activo *share-alike*; medido contra el mejor permisivo, la brecha es peor, no mejor.

**Entonces el gap 20 se cierra y el 26 no.** Son dos afirmaciones distintas y el pase 12 las había mezclado:
- *«no hay eval publicada»* → **falso desde este pase.** Hay dos repos Apache-2.0 con `evals/`.
- *«la educación no ocupó el canal»* → **sigue siendo cierto.** 541 ★ contra 47.200 ★ no es ocupar un canal.

### Por qué esto cambia una propuesta, y no es un detalle de licencia

Esta KB tiene desde el pase 4 una capa de evaluación pedagógica premiada y sin adoptar (`MathTutorBench` 42 ★,
`UnifyingAITutorEvaluation` 32 ★ — gap 1), y desde el pase 12 una capa de distribución sin evidencia (gap 20).
**Los dos repos de este pase son el primer caso del sector en que el artefacto distribuible y su rúbrica de
evaluación viajan en el mismo paquete, con licencia permisiva.** Para un entregable de Studios eso es la
diferencia entre «le entregamos 4 skills» y «le entregamos 4 skills y el instrumento con que se verifica que
hacen lo que dicen» — que es exactamente el argumento de **P10** y de **P30**, y hasta hoy había que construirlo
a mano.

⚠️ **Y el límite, que hay que decir antes de que lo pregunte el cliente:** son **cuatro** skills, de **K-12**, y
el chequeo formativo está acotado a **matemática**. Comparado con los 165 dominios de `education-agent-skills`,
es un conjunto chico. El valor de este pase es la **licencia y la eval**, no la cobertura.

### Lo que esta pasada buscó y no encontró

- **Una skill educativa con eval publicada que no venga de este par de repos:** ninguna. Los siete paquetes del
  pase 12 se revisaron de nuevo y siguen sin `evals/`.
- **Una eval de skill atada a un estándar curricular nacional** (la unión natural con la capa CASE del pase 14):
  no existe. Las rúbricas nuevas evalúan calidad pedagógica, no alineación verificable a un marco.
- **Un agente de la tabla principal que consuma estas skills:** ninguno de los 31 las referencia. Es la misma
  desconexión que el gap 24 anotó para la voz y el gap 13 para las credenciales.

## 2026-10-01 (pase 16) — ninguno de los 31 agentes de esta KB declara qué hace con el dato del alumno, y desde abril la voz de un chico es dato biométrico regulado en EE. UU.

El pase 15 abrió la capa que prueba **quién escribió** el trabajo. Este pase abre la que decide **con qué derecho
el sistema lee al alumno**. Las dos son de cumplimiento, pero esta es anterior: sin ella, las otras quince capas
de esta KB no se pueden desplegar sobre datos reales.

**La tabla principal de `agents/top.md` no cambió en este pase y el conteo sigue en 31.** Lo que se encontró no
son agentes: son librerías de infraestructura, y viven en `repos/foundations.md`. Decirlo es parte del hallazgo —
**la capa de privacidad del dato educativo no tiene agentes, tiene librerías horizontales**.

### 🔴 El hallazgo del pase: la KB abrió la capa de voz hace dos pasadas y no registró que la voz ya está regulada

El **pase 14** abrió la capa de lectura oral y pronunciación —la primera capa de voz de esta KB— y dejó el
**gap 24** anotando que ninguno de los 31 agentes tiene voz. El encuadre era de producto. **Le faltaba el
encuadre regulatorio, y es el que decide si esa capa se puede vender en Norteamérica.**

La **regla COPPA enmendada de la FTC** agregó los **identificadores biométricos a la definición de información
personal**, y la enumeración incluye explícitamente **voiceprints**, faceprints, huellas y huellas de palma.

| Hito | Fecha verificada |
|---|---|
| La FTC anuncia las enmiendas finalizadas | **enero de 2025** |
| Publicación en el *Federal Register* | **2025-04-22** |
| Entrada en vigor | **2025-06-23** |
| 🔴 **Fecha de cumplimiento general** | **2026-04-22** |

**Esa fecha ya pasó: hace más de cinco meses.** Y es la diferencia de postura con todo lo que esta KB viene
escribiendo sobre EMEA: el reloj europeo del Artículo 50 **vence en diciembre** y se vende como urgencia futura;
**el reloj norteamericano ya venció y se vende como exposición presente.**

Lo que eso le hace a la capa de voz del pase 14, en concreto: un agente que escucha a un chico leer en voz alta
para evaluar su fluidez **captura un voiceprint**, y en Norteamérica eso ahora exige consentimiento parental
verificable bajo COPPA. Si además el despliegue toca Illinois, **BIPA** exige consentimiento escrito con daños
estatutarios de **1.000 a 5.000 USD por violación** — por alumno, en un producto cuyo caso de uso es un aula
entera.

### Las otras tres reglas que la KB no tenía y que pegan sobre patrones ya escritos

**1. FERPA prohíbe exactamente el atajo de datos que esta KB venía necesitando.** Bajo la *school official
exception*, el dato que una institución le entrega a un proveedor **sólo puede usarse para el fin por el que se
entregó** — prestar el servicio educativo. Usar dato de alumnos para **entrenar modelos con fines comerciales
generales** es, típicamente, una violación de FERPA.

Eso cae directo sobre el **gap 11** de esta KB, que desde el pase 7 viene diciendo que los datasets de knowledge
tracing son NonCommercial y que, para un cliente con restricción de procedencia, **«entrenar con los datos propios
pasa a ser la única opción»**. Sigue siendo cierto, y ahora tiene una condición que la KB no había escrito:
*los datos propios son los del cliente, y el contrato FERPA no deja llevárselos al modelo general*. La salida no
es legal, es técnica, y es la capa que abre este pase: **DP, federado o sintético**.

**2. El dato de aprendizaje puede ser *perfilado dañino*, y en APAC está nombrado así.** Bajo la **DPDP Act 2023**
de India, toda escuela que procese dato digital de alumnos es *Data Fiduciary*, y como los alumnos son menores
aplica la **Sección 9**: consentimiento parental verificable, sin seguimiento conductual ni publicidad dirigida.
Las sanciones por infracciones con datos de menores llegan a **₹200 crore**. Y la lectura que circula entre los
analistas regionales es la que importa para esta KB: **una analítica que etiqueta a un alumno como «de bajo
potencial» o que predice problemas de conducta sin salvaguardas puede tratarse como perfilado dañino.**

Eso es, literalmente, la **capa predictiva** que el pase 11 abrió (gap 18) y el patrón **P25**.

**3. GDPR convierte el despliegue en un entregable documental.** Antes de que una escuela use una herramienta de
AI que procese dato de alumnos, el **DPIA es obligación legal bajo el Artículo 35**, y el EDPB recomienda
documentar formalmente el *balancing test* de interés legítimo por cada actividad de tratamiento. Para un studio
eso no es fricción: **es un entregable con nombre, alcance acotado y comprador claro**, y se vende antes del
sistema, no después.

### Lo que esto cambia en la postura comercial de la KB

Quince pasadas vendieron **capacidad** (el tutor enseña, el evaluador mide, el detector marca). Este pase agrega
la pregunta que un CISO o un DPO hace primero y que ninguna de las quince respondía: **¿dónde está el dato del
chico y quién puede verlo?** La buena noticia del pase es que la respuesta técnica ya existe, es permisiva y no
hay que construirla —`PySyft`, `Flower`, `OpenDP`, `Opacus`, `synthcity`—; la mala es que **nadie la conectó al
dato educativo**: el mejor puente que se encontró, `FedGKT`, tiene **1 estrella y no declara licencia**.

Ver los **trends 39, 40 y 41**, los **gaps 27 y 28**, y los patrones **P34** y **P35**.

## 2026-10-01 (pase 15) — la KB le vende a EMEA un deadline de *watermarking* desde el pase 4 y nunca registró una sola implementación: existe, es Apache-2.0 y viaja dentro de Hugging Face Transformers

Catorce pasadas construyeron la capa que **enseña** y la capa que **evalúa**. Ninguna construyó la capa que
**prueba quién escribió el trabajo**. La KB tenía media capa de integridad académica —la del pase 8, que es
**proctoring y nada más**, y que ella misma registró como *roadmap, no componente*. La otra mitad, la de autoría,
no estaba. Y es la mitad que todo cliente pregunta primero, porque el 92 % de los alumnos ya usa AI.

Este pase la abre, y encuentra adentro un error de la propia KB.

### 🔴 El hallazgo del pase: la KB vende una obligación que no sabe cumplir

Desde el **pase 4**, `compose/patterns.md` y `intel/market.md` recomiendan la misma entrada comercial para EMEA:
*vender el Artículo 50 antes que el Anexo III*. El argumento está bien construido y la fecha está bien puesta —
`compose/patterns.md:106` anota **«Watermarking de contenido generado → 2026-12-02»** y `intel/trends.md:126`
remata **«Faltan dos meses»**.

**Once pasadas después, esta KB no tiene una sola pieza de watermarking registrada.** Ni un repo, ni una
librería, ni un nombre. Se buscó `watermark` en los ocho archivos: aparece **cinco veces, todas en prosa
comercial**, ninguna apuntando a código. La oferta de entrada a EMEA —la que la KB describe como *«alcance chico,
urgencia real»*— no tenía implementación detrás.

**La tiene, y es mejor de lo que el gap sugería:**

| Pieza | Repo | Licencia | ★ | Qué resuelve exactamente |
|---|---|---|---|---|
| **SynthID-Text** | `huggingface/transformers` → `src/transformers/generation/watermarking.py` | **Apache-2.0** ✅ | — (viaja en Transformers) | Marcado **e**  detección. Clases verificadas en el archivo: `SynthIDTextWatermarkLogitsProcessor` (marca en generación), `SynthIDTextWatermarkDetector`, `BayesianDetectorModel`, `BayesianDetectorConfig`, `BayesianDetectorWatermarkedLikelihood`. Cabecera de copyright: **«The HuggingFace Inc. team and Google DeepMind»** |
| **MarkLLM** | https://github.com/THU-BPM/MarkLLM | **Apache-2.0** ✅ | **1.1k** (95 forks, 185 commits) | **23+ algoritmos** de watermarking (KGW, Unigram, SWEET, SIR, DiPmark, SemStamp, **SynthID-Text**…) más **12 herramientas de evaluación** en tres ejes: detectabilidad, robustez e impacto en calidad del texto. EMNLP 2024 Demo |
| **c2pa-rs** | https://github.com/contentauth/c2pa-rs | **MIT *y* Apache-2.0** (dual) ✅ | **424** (192 forks, **1.907 commits**) | SDK Rust del estándar **C2PA**: crear, firmar, validar e incrustar manifiestos de procedencia. Claims **C2PA v2**, spec **2.4**, más la *CAWG identity assertion*. API en C para otros lenguajes |
| **c2pa-python** | https://github.com/contentauth/c2pa-python | **Apache-2.0 *y* MIT** (dual) ✅ | **105** (35 forks, 344 commits) | El *binding* Python del anterior. Python 3.10+. Es la vía realista para meter procedencia en un pipeline educativo que ya es Python |

**Por qué `SynthID-Text` es el hallazgo y no `MarkLLM`.** MarkLLM tiene más algoritmos y es la herramienta de
**investigación**; SynthID-Text es el que **ya está dentro de la dependencia que el proyecto va a tener igual**.
Un tutor construido sobre Transformers no agrega un proveedor: agrega un `WatermarkingConfig` a la llamada de
generación y un detector del mismo paquete. Eso convierte la obligación del Artículo 50 de *proyecto* en
*parámetro*, y es exactamente el tamaño de entrada que el patrón del pase 4 prometía sin poder respaldar.

⚠️ **Y C2PA dejó de ser opcional en la práctica.** El **Code of Practice** europeo sobre marcado y etiquetado de
contenido generado por AI —voluntario, pero la vía más clara para demostrar cumplimiento— **adopta las
*Content Credentials* de C2PA como estándar técnico de facto** para el metadato incrustado, en un esquema por
capas: **metadato + watermarking**, con *fingerprinting* y *logging* como medidas de apoyo. O sea: las cuatro
piezas de la tabla no son alternativas entre sí, son **las dos capas del mismo esquema**. Ver el patrón **P33**.

🔴 **Discrepancia de fecha que hay que resolver antes de usarla con un cliente.** Dos fuentes secundarias dan dos
fechas de publicación del Code of Practice: **10 de junio de 2026** (IPTC) y **20 de julio de 2026** (otra).
`digital-strategy.ec.europa.eu`, `artificialintelligenceact.eu` e `iptc.org` están **bloqueados por el proxy de
egreso**, así que no se pudo ir a la fuente. **Lo que sí está consistente en todas las fuentes y es lo que
sostiene la propuesta:** Artículo 50 **en vigor desde 2026-08-02**, y los sistemas **ya en el mercado** antes de
esa fecha tienen hasta el **2026-12-02** para cumplir el marcado legible por máquina del Artículo 50(2). Esa es
la fecha que la KB ya tenía bien.

### La otra mitad del hallazgo: la detección existe, es permisiva, y no se puede usar para acusar

La capa forense está mejor abastecida de lo que la KB suponía, y **toda con licencia apta**:

| Repo | Licencia | ★ | Forks | Commits | Qué es |
|---|---|---|---|---|---|
| https://github.com/baoguangsheng/fast-detect-gpt | **MIT** ✅ | **434** | 85 | 76 | **ICLR 2024**. Detección *zero-shot* por curvatura de probabilidad condicional. **340× más rápido que DetectGPT** sin perder exactitud. AUROC declarado **0,9887** sobre generaciones de 5 modelos y **0,9338** sobre ChatGPT/GPT-4 |
| https://github.com/ahans30/Binoculars | **BSD-3-Clause** ✅ | **420** | 67 | 54 | **ICML 2024**. *Zero-shot* sin datos de entrenamiento; necesita dos modelos de pesos abiertos en inferencia |
| https://github.com/liamdugan/raid | **MIT** ✅ | **216** | 98 | **378** | **ACL 2024**. El *benchmark* compartido: **10M+ documentos**, 11 modelos, 11 dominios, 4 estrategias de decodificación y **12 ataques adversarios** (homoglifos, paráfrasis, sinónimos, erratas). Leaderboard en `raid-bench.xyz` |
| https://github.com/NLP2CT/LLM-generated-Text-Detection | **MIT** ✅ | **252** | 16 | 40 | Survey vivo: ~100+ papers, 17+ datasets, métodos estadísticos/neuronales/watermarking y la sección de **ataques adversarios**. Paper en *Computational Linguistics* **51(1), 2025** |
| https://github.com/pablocaeg/sloptotal | **MIT** ✅ | 39 | 8 | 58 | *«VirusTotal para texto AI»*: **23 motores** (8 clasificadores neuronales, 6 estadísticos —incluidos Fast-DetectGPT y Binoculars— y 7 heurísticas lingüísticas), auto-hospedado, **corre en CPU**, score de ensamble calibrado |
| https://github.com/Lendarixon/awesome-ai-detection | **CC0-1.0** ✅ | 0 | 0 | 4 | Catálogo chiquito pero honesto: lo que vale son los **modos de falla con número** |

### 🔴 El segundo hallazgo, y es el que decide la arquitectura: la detección falla **exactamente** sobre el alumno de Globant

Los números no vienen del marketing de los detectores, vienen de sus propios autores y benchmarks:

- **61,3 % de falsos positivos sobre escritura de no nativos de inglés.** Liang et al. compararon siete
  detectores sobre ensayos TOEFL: **61,3 % de FPR promedio en no nativos contra ~2,9 % en universitarios
  estadounidenses nativos.** La explicación propuesta es la baja perplejidad del texto de no nativos, por menor
  variabilidad léxica — o sea, **es estructural, no un bug que se arregle con otra versión**.
- **Binoculars lo dice en su propio README:** *«more proficient in detecting English language text compared to
  other languages»*, *«none are perfect and can have multiple failure modes»*, **«for academic purposes only»**
  y exige **supervisión humana**.
- **SlopTotal lo dice en el suyo:** *«Short text is unreliable below roughly 80 words and settles from about
  200»* — con AUC global 0,974 y **1 de 66 textos humanos marcado mal**.
- **5,85 % de FPR** sobre escritura académica genuina **anterior a 2018** (1.180 abstracts, o sea texto que no
  pudo ser generado por un LLM), con **20 % adicional cayendo en «incierto»**.
- **RAID muestra caídas grandes de exactitud por paráfrasis.** Un alumno que pasa el texto por un reescritor
  rompe la detección; el detector sigue acusando al que no lo hizo.

**La aritmética que cerró la discusión en North America, y conviene llevarla escrita:** Vanderbilt calculó que
**1 % de falsos positivos sobre 75.000 trabajos son ~750 acusaciones injustas por año**, y **desactivó el
detector de AI de Turnitin**. **Más de 50 universidades** de EE. UU., Reino Unido, Canadá, Australia y Sudáfrica
lo desactivaron, restringieron o lo abandonaron —Johns Hopkins, Yale, Vanderbilt, Waterloo, Curtin, Australian
Catholic University entre ellas—; **al menos 12 instituciones grandes a marzo de 2026**.

**La conclusión operativa, y es una regla de propuesta, no una opinión:** un score de detección es **evidencia,
no prueba**. Ningún entregable de Globant debería producir una decisión disciplinaria automática a partir de uno.
Y para un cliente **LATAM o EMEA no anglófono**, el 61,3 % convierte la herramienta en **pasivo legal**, no en
producto. Ver el **gap 25** y el patrón **P33**.

### El tercer hallazgo, y conecta con el pase 12: el lado adversario **sí** usa el canal de distribución que la educación perdió

El pase 12 midió que la vertical científica se quedó con el canal de *skills* de agente (47,2k ★ MIT) y que la
educativa tiene 815 ★ *share-alike*. Este pase encontró **quién sí lo está usando en el dominio educativo**:

**`ervin-mo/humanizar-es`** (https://github.com/ervin-mo/humanizar-es, **MIT** ✅, 0 ★, 6 commits) reescribe texto
en **español** generado por AI para que los detectores dejen de marcarlo, sin cambiar lo que dice. Corre
**Binoculars y Fast-DetectGPT localmente sobre Qwen2.5-0.5B** para guiar la reescritura. Y está empaquetado como
**`SKILL.md` para Claude Code, Codex, OpenCode, Antigravity, DeepSeek Harness y Gemini CLI**.

Resultado declarado por el propio autor: un párrafo pasó de **«100 % AI» en Grammarly a «0 % AI / 99 % humano»**
en CleverHumanizer; el ensayo completo procesado de una sola vez quedó en **39 %**. El autor acota la evidencia
(*un solo ensayo*) y aclara que **no está pensado para entregar trabajo calificado**.

**Por qué importa más que sus 0 estrellas.** No es el repo: es la **asimetría de canal**. La evasión se
distribuye como *skill* de agente —instalable en seis harnesses, en español, con los detectores de la KB
adentro— y la integridad se distribuye como **plugin propietario de LMS**. El pase 12 preguntó por qué la
educación no usa ese canal; la respuesta parcial es que **sí lo usa, del lado equivocado del problema**. Es el
**gap 26**.

### La lectura por región, y por una vez LATAM sale favorecida

| Región | Régimen dominante | Qué implica para esta capa |
|---|---|---|
| **North America** | Vacío regulatorio federal + parches estatales (Colorado, Texas, Idaho SB 1227). **El movimiento de abandono de la detección nació acá** | La conversación ya está ganada del lado del cliente: no hay que convencerlo de no comprar detección, hay que **ofrecerle el reemplazo**. Mercado: **951 M USD (2024) → 2.303,2 M (2029), 15,9 % CAGR**, 36 % del global |
| **EMEA** | **Artículo 50 en vigor (2026-08-02); marcado legible por máquina para sistemas ya en mercado: 2026-12-02.** Code of Practice voluntario que canoniza C2PA | Es la **única región donde esta capa es obligación legal con fecha**. Y es donde el 61,3 % pega más fuerte, porque la mayoría de los universitarios escribe inglés como L2. **Marcar, no detectar** |
| **APAC** | Fragmentado y sin marco común. Japón cauteloso con marco estatal; China centralizado *top-down*; **Australia: 26 de 35 universidades (73 %) ubican su política de AI dentro de la política de integridad académica** | Australia es el punto de entrada: la política ya existe y ya está en el lugar correcto del organigrama. Mercado: **591,6 M (2024) → 1.848,1 M (2029), 20,9 % CAGR**, el de crecimiento más rápido |
| **LATAM** | **Declaración obligatoria del uso de AI** en México, Colombia y Chile, con sanción por uso fraudulento y **en algunos casos entrega de los *prompts*** como documentación | 🟢 **El único régimen de los cuatro que el stack open source puede satisfacer hoy.** No pide detección: pide **divulgación y procedencia**, que es justo lo que SynthID-Text + C2PA producen. Ver abajo |

### 🔴 El cuarto hallazgo: LATAM tiene el régimen correcto y la peor herramienta posible instalada

Las dos cosas son ciertas a la vez y juntas son la propuesta:

1. **La regla latinoamericana no pide detectar, pide declarar.** México, Colombia y Chile exigen que el alumno
   **declare** que usó AI y para qué, y en algunos casos que **adjunte los prompts**. Un régimen de divulgación
   se satisface con **procedencia** —marca en el origen, manifiesto firmado, log— y **no requiere acertar un
   juicio forense sobre el texto**. Es el único de los cuatro regímenes donde la tecnología permisiva que existe
   hoy **alcanza**.
2. **Y sin embargo lo que está instalado es detección.** UNAM, Tec de Monterrey, UAM, BUAP y UdeG usan
   **Turnitin Originality** como herramienta principal — el mismo tipo de producto que 50 universidades
   anglófonas desactivaron, aplicado sobre alumnos que escriben **español**, donde los detectores están aún
   menos validados. Y **más del 80 % de las instituciones de educación superior de México no tiene marco
   normativo claro** sobre uso ético y académico de la tecnología.

**Eso es una brecha vendible y con fecha propia:** el instrumento normativo (declaración) ya existe, la
herramienta instalada no lo sirve, y el reemplazo es Apache-2.0. Ver **P33** y la sección LATAM de
`intel/market.md`.

**Lo español de esta capa, verificado, y vuelve el patrón de siempre:** **`yonatanlop/detectoria`**
(https://github.com/yonatanlop/detectoria, 🚫 **sin licencia**, 0 ★, 7 commits) es el único detector
específicamente diseñado para español que encontró este pase — cuatro métodos (estilometría, perplejidad/
*burstiness* con `mrm8488/spanish-gpt2`, rank/entropía estilo GLTR, y traducción con `Helsinki-NLP/opus-mt-es-en`
+ `roberta-base-openai-detector`), pensado para correr en el *Always Free* de Oracle Cloud. **Y van cuatro
pasadas seguidas en que la pieza hispanohablante correcta aparece sin licencia.** No proponerlo; sí registrarlo,
y sí considerar pedirle al autor una licencia, que es lo más barato de esta KB.

### Lo que esta pasada buscó y no encontró

- **Watermarking aplicado a educación.** No existe. SynthID-Text y MarkLLM son infraestructura genérica; **ningún
  proyecto educativo open source los usa**, y no hay plugin de LMS, servidor MCP ni integración LTI que marque o
  verifique la salida de un tutor. El puente hay que construirlo — es chico, y es **P33**.
- **Integridad académica open source dentro de Moodle.** Los plugins que existen en el directorio son
  **envoltorios de servicios propietarios**: Originality.ai (Moodle 3.9–5.0, release 2026-07-02), Compilatio
  (GPL-3.0 **el plugin**, 821 instalaciones, release 2026-06-25), Copyleaks. El código del plugin es libre; **el
  detector detrás es un servicio pago**. No cambia el diagnóstico del pase 8: la categoría sigue siendo
  propietaria, ahora medida también del lado de la autoría y no sólo del proctoring.
- **Evidencia de proceso (keystroke / historial de versiones) en abierto.** Todo lo que hay es propietario —
  GPTZero Authorship, Grammarly Authorship, Turnitin Clarity, Draftback. 🔴 **Y hay literatura de 2026 que sostiene
  que la señal no sirve**: un análisis de *timing-forgery* argumenta que el registro de pulsaciones **no distingue
  a quien compone de quien transcribe un borrador de ChatGPT**. **No verificable desde esta sesión —
  `arxiv.org` está bloqueado por el proxy** (arXiv 2601.17280 y 2608.26710 quedaron sin abrir). Anotado como
  pista, no como hallazgo.
- ⚠️ **Y la colisión con el pase 8 que hay que registrar antes de que cueste algo:** el reemplazo que las
  universidades están adoptando —*«mostrá el historial de versiones»*— **no lo puede producir un alumno que
  escribe hablando**. Choca de frente con la capa de accesibilidad del pase 8 y con la de habla del pase 14. Un
  entregable que exija evidencia de proceso **necesita una vía alternativa documentada**, o es un problema de
  accesibilidad con forma de política de integridad.
- **Datos LATAM de primera mano.** Hay un dataset en Zenodo (`zenodo.org/records/22661179`) con las políticas
  institucionales de integridad académica y lineamientos de AI generativa de las **15 universidades
  latinoamericanas mejor rankeadas en THE 2026** (USP, Unicamp, PUC Chile, UFRJ, UNESP…). 🔴 **`zenodo.org` está
  bloqueado por el proxy: no se pudo verificar licencia ni contenido.** Es la pista más valiosa que deja este
  pase sin cerrar.

### Sin movimiento en los dos grandes, y van seis pases

`DeepTutor` (Apache-2.0, 40,6k ★) y `OpenMAIC` (MIT, 39,7k ★) siguen planos. Seis pasadas consecutivas sin
movimiento en la cima ya no es ruido: **es la forma del mercado open source educativo.** La acción está en las
capas, no en los dos grandes.

---

## 2026-10-01 (pase 14) — trece pasadas trataron el aprendizaje como texto: aparece la capa donde el alumno **habla**, y es la que decide si un tutor sirve en primaria

Las trece pasadas anteriores buscaron por el rol del software (agente, tutor, evaluador, predictor), por la capa
(contenido, telemetría, credencial, práctica) y por el alumno (educación especial). **Ninguna buscó por el canal.**
Todo lo que esta KB tiene asume que el alumno **escribe**: el notebook del pase 13, el SRS del pase 12, el LRS del
pase 6, los *skills* pedagógicos del pase 12. Buscado directamente, aparece una capa entera y tiene consecuencias.

### 🔴 El hallazgo del pase: la habilidad que más se evalúa en primaria en el mundo es la lectura oral, y esta KB no tenía una sola pieza para medirla

En los primeros años de escolaridad la medición que usan los sistemas educativos **no es un cuestionario: es que el
chico lea en voz alta y se le midan palabras por minuto y exactitud.** Es la métrica de las evaluaciones de
alfabetización inicial en las cuatro regiones. Hasta este pase, esta KB —con 31 agentes y catorce capas— **no tenía
ninguna forma de capturar, puntuar ni devolver *feedback* sobre voz.**

| Pieza | Licencia | ★ | Qué hace | Utilizable |
|---|---|---|---|---|
| [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | **MIT** ✅ | **85** | Evaluación de pronunciación **a nivel de fonema** contra el texto esperado. Wav2Vec2 (`facebook/wav2vec2-lv-60-espeak-cv-ft` para fonemas, `wav2vec2-large-960h` para palabras, XLSR por idioma). Devuelve **puntaje 0-100, *phoneme error rate*, *word error rate*, confianza por palabra, distancia acústica por DTW y prosodia (F0 y energía)**. Corre **local, sin API key ni nube** | ✅ **Sí. Es la pieza vendible de la capa** |
| [`jimbozhang/speechocean762`](https://github.com/jimbozhang/speechocean762) | ⚠️ **sin archivo LICENSE** (ver abajo) | **198** | Corpus de inglés no nativo para *pronunciation scoring*: **5.000 oraciones, la mitad de los hablantes son niños**, L1 mandarín. Puntajes de exactitud, completitud, fluidez y prosodia a nivel fonema, palabra y oración | ⚠️ **Con cautela.** Es el dataset de referencia de la tarea |
| [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | **Apache-2.0** ✅ | **15.5k** | *Toolkit* de ASR de grado industrial, C++/CUDA. Es la base sobre la que la literatura académica construye los tutores de lectura (holandés, bambara) | ✅ Sí, pero **es infraestructura genérica, no educativa** |
| [`vilcaaguilerandrea-oss/carrera-lectora`](https://github.com/vilcaaguilerandrea-oss/carrera-lectora) | 🔴 **SIN LICENCIA** | **0** | PWA chilena de fluidez lectora para **1.º a 4.º básico**: 40 textos diferenciados (10 por nivel), mide **PPM y exactitud**, pedagogía intercultural, Web Speech API en el dispositivo, sin registro ni telemetría | 🔴 **No. No es reutilizable** |

### La forma de la capa, y es el patrón base de esta KB otra vez

**Lo maduro es genérico y lo educativo es chico.** Kaldi tiene **15.500 ★** y no sabe nada de pedagogía;
OpenPronounce tiene **85 ★** y es lo único permisivo que mide lo que un docente necesita; el resto de la capa son
*papers*. Es exactamente la forma que el pase 8 encontró en accesibilidad y el pase 12 en *skills*, con una
diferencia que mejora el caso: **acá la pieza educativa chica es MIT y corre local**, así que el obstáculo no es la
licencia ni la soberanía del dato — es que nadie la empaquetó para un sistema educativo.

### ⚠️ La trampa de licencia del pase, y es la del pase 10 repetida en otra capa

`speechocean762` tiene **198 ★** y su README dice que el corpus está *«available for free download for both
commercial and non-commercial purposes»*. **No hay archivo `LICENSE` en el repositorio.** El pase 10 documentó
exactamente esta forma —la licencia declarada en el README no es la licencia del repositorio— y dejó una regla
operativa. **Se aplica igual acá: una afirmación en prosa del README no es un instrumento de licencia que un
cliente pueda auditar.** Antes de meter este corpus en un entregable hay que conseguir los términos del titular
(SpeechOcean) por escrito. **Con 198 ★ y sin `LICENSE`, es la pieza con mejor relación tracción/riesgo mal medido de
toda esta capa.**

### 🔴 El segundo hallazgo: LATAM vuelve a producir la pieza correcta sin licencia, y van tres

El gap 2 dice, desde el pase 2, que *«LATAM produce agentes educativos, pero ninguno sale de la fase cero… no falta
interés de constructores, falta masa crítica y gobernanza de proyecto (empezando por poner una licencia)»*. Las dos
evidencias eran `H1bertto/professor-agent` (MIT, 0 ★) y `ANTONIOALGMAR/StudyAgent` (sin licencia, 2 ★).

**`carrera-lectora` es la tercera, y es la más dolorosa de las tres.** Es pedagógicamente la más fina que vimos de la
región: 40 textos graduados por nivel, pedagogía intercultural explícita, procesamiento **en el dispositivo** sin
telemetría —que es la arquitectura que el Anexo III del EU AI Act y los estatutos de privacidad de EE. UU. piden— y
mide la métrica que el sistema escolar chileno efectivamente usa. **Y no se puede usar, porque no tiene licencia.**

El dato que lo vuelve accionable y no una lamentación: **es el vacío más barato de cerrar de esta KB después del
gap 20.** No hay que construir nada — hay que abrir un *issue* pidiendo una licencia.

### Lo que esta pasada buscó y no encontró

- **Ningún agente de los 31 de `agents/top.md` tiene entrada ni salida de voz.** Se verificó contra la tabla. Ni
  DeepTutor, ni Educhain, ni OpenTutor. **La capa de habla y la capa de agente no se tocan** — gap 24 de este pase.
- **Ningún servidor MCP de evaluación de pronunciación.** Existe el patrón (`bncc-mcp` del mismo pase lo hace para
  currículo), pero nadie expuso OpenPronounce ni equivalente por MCP.
- **Nada en portugués ni en español con licencia utilizable.** `carrera-lectora` (sin licencia) es lo único de LATAM.
  Para evaluación de fluidez en español y portugués **no hay pieza permisiva**, y son ~600 millones de hablantes.
- **Ninguna evaluación de fluidez en lenguas indígenas o africanas con repo verificable.** La literatura registra un
  caso en bambara (`arXiv 2606.31508`, 55 horas de lectura de 60 niños, con *benchmark* público declarado) pero
  **`arxiv.org` está bloqueado por el proxy de esta sesión** y no se pudo abrir el paper ni localizar el repo. Se
  declara como pista, no como hallazgo.
- **Sin movimiento en los dos grandes, y van seis pases.** DeepTutor y Educhain no registran cambio de versión ni
  salto de estrellas en esta ventana.

## 2026-10-01 (pase 13) — doce pasadas preguntaron qué hace el agente; ninguna preguntó dónde hace el alumno el trabajo, y la respuesta corrige el gap 6

Decimotercera corrida. Las doce anteriores recorrieron el tutor, el modelado del conocimiento, la evaluación pedagógica,
la seguridad, la telemetría, los datos de entrenamiento, la accesibilidad, la credencial, el contenido curricular, la
predicción de abandono y el empaquetado en *skills*. **Ninguna documentó el entorno donde el alumno escribe la respuesta
y donde esa respuesta se corrige.** Este pase lo busca y encuentra una capa entera que la KB no tenía — y que da vuelta
una conclusión que sobrevivió once pasadas.

### 🔴 El hallazgo del pase: la capa más desplegada y la de licencia más limpia de esta KB se llama «notebooks»

Verificado repo por repo vía WebFetch el 2026-10-01.

| Repo | Licencia | Stars | Rol en la capa |
|---|---|---|---|
| https://github.com/jupyterhub/jupyterhub | **BSD-3-Clause** ✅ | **8.300** | Entorno de cómputo aislado por alumno, en el navegador, para una cohorte entera |
| https://github.com/jupyterlab/jupyter-ai | **BSD-3-Clause** ✅ | **4.400** | **Runtime de agente con ACP + MCP.** Autodetecta Claude, Codex, Copilot, Gemini, Goose, Kiro, Mistral Vibe, OpenCode |
| https://github.com/jupyter/nbgrader | **BSD-3-Clause** ✅ | **1.400** | Autocorrección + corrección manual + **tests ocultos** en un flujo. **v0.9.6 del 2026-09-30** |
| https://github.com/ucbds-infra/otter-grader | **BSD-3-Clause** ✅ | 161 | Autograder modular del **DSEP de UC Berkeley**, sin acoplarse a JupyterHub |
| https://github.com/jupyterhub/ltiauthenticator | **BSD-3-Clause** ✅ | 73 | **LTI 1.3 / 1.1** probado contra **Open edX, Canvas y Moodle** — las tres plataformas que esta KB ya documentaba |

**Cinco repos, 14.334 ★, una sola familia de licencia, y la release más reciente es del día anterior a este pase.**

### Por qué no apareció en doce pasadas

Porque **la consulta estaba mal formulada**, que es la quinta vez que esta KB registra lo mismo (ver la nota de método del
pase 7). Buscar «agente educativo», «tutor», «LMS» o «grading» no devuelve Jupyter: Jupyter no se presenta como producto
educativo. Se presenta como herramienta de cómputo científico, **y resulta ser la infraestructura docente de educación
superior en STEM desde 2014** — nbgrader está implementado en **UC Berkeley, Cal Poly, Universidad de Edimburgo** y
**Aalto**, que publica su propia guía de autograding para instructores.

### Lo que corrige, con precisión y sin exagerar

El **gap 6** dice desde el pase 2, sin cambios: *«no hay agente de grading open source con tracción; la capa sigue siendo
propietaria —Gradescope (Turnitin), Codio, Kangaroos AI—; no prometer reemplazar Gradescope, prometer orquestarlo»*.

**La afirmación era más amplia que la evidencia que la sostenía** (`gradescope-mcp` 8 ★, `classmoji` 83 ★ AGPL, `rubric`
0 ★). Queda partida en dos, y las dos mitades son verdaderas:

- **Trabajo computacional** —código, notebooks, datos, cálculo numérico—: **la corrección open source existe, es
  BSD-3-Clause y está desplegada a escala de cohorte desde 2014.** No hay que construirla ni orquestar a un propietario.
- **Prosa** —ensayo, respuesta abierta—: **el gap 6 sigue intacto**, y es exactamente donde vive el incumbente.

Para un cliente de STEM, ciencia de datos o formación técnica, la recomendación anterior de esta KB era **falsa y además
más cara que la alternativa**. Para uno de humanidades, sigue valiendo tal cual. Ver el patrón **P29**.

### Los otros dos hallazgos del pase, y los dos son de encuadre

**1. El aporte de LATAM a la capa de evaluación no es un repo: es un examen del Estado.**

| Repo | Licencia | Stars | Qué es |
|---|---|---|---|
| https://github.com/AI-for-Education/pedagogy-benchmark | **MIT** ✅ | 12 | **1.143 preguntas de exámenes de habilitación docente**: CDPK (920, pedagogía general transversal a materias y edades) + **SEND (223, educación especial)**. El repo acredita a la **Agencia de la Calidad de la Educación** y al **CPEIP del Ministerio de Educación de Chile**. arXiv 2506.18710 |

Ocho pasadas midieron LATAM contando repos y encontraron siempre el mismo techo de 0–3 ★. **Estaban midiendo la cosa
equivocada.** El activo educativo exportable de la región que esta KB encontró con uso real no es software: es un
**instrumento de medición pedagógica producido por el Estado**, lo bastante sólido para que un laboratorio enfocado en
LMICs lo use de vara para medir a los LLM del mundo. Y de paso mueve el **gap 4** —la concentración china de la capa de
evaluación limpia— por primera vez en seis pasadas. Ver el **gap 22**.

**2. El despliegue docente más grande de esta KB tiene nueve estrellas.**

| Repo | Licencia | Stars | Qué es |
|---|---|---|---|
| https://github.com/microsoft/Shiksha-Copilot | **MIT** ✅ | **9** | **Microsoft Research India** (iniciativa VELLM). Planes de clase alineados al currículo, actividades y evaluaciones. Ingesta curricular con MinerU/SmolDocLing/OlmOCR, datastores vectorial+grafo+documental, React + FastAPI. Investigación publicada sobre **1.043 docentes de Karnataka** en **inglés y kannada**. 149 commits |

Es la confirmación más nítida del **trend 23** («las estrellas de GitHub esconden la infraestructura educativa realmente
desplegada»): **9 estrellas, 1.043 docentes.** El pase 10 lo había mostrado con Sunbird (41 ★, 180 M de alumnos); acá el
cociente es aún más extremo y encima la licencia es MIT.

⚠️ **Y el límite es del propio repo, no nuestro:** declara ser *«a research prototype… not extensively tested for
production use»*, con supervisión humana obligatoria y no apto para despliegue comercial sin validación extensa. **Se
cita como evidencia de que la categoría funciona a escala docente real; no se cotiza como componente.**

### Lo que esta pasada buscó y no encontró

- **Corrección open source de prosa con licencia permisiva y tracción.** Sigue sin existir: es la mitad del gap 6 que
  este pase **no** cierra. Lo nuevo es que ahora el gap está acotado al tipo de trabajo correcto.
- **Una capa de práctica equivalente fuera de STEM.** JupyterHub + nbgrader sirven donde el trabajo del alumno es
  ejecutable. **Para un alumno de derecho, historia o lengua no hay análogo**: no existe el «notebook» de la prosa, con
  entorno aislado, entrega, autocorrección parcial y LTI. Es el **gap 21**, nuevo.
- **Formación profesional en esta capa.** El **gap 10** sigue abierto: nbgrader vive en educación superior, no en FP.
- **Un benchmark pedagógico de ciencias sociales.** Cuarta acotación del gap 1 sin cerrar; `pedagogy-benchmark` es
  transversal a materias pero mide conocimiento **declarativo**, no enseñanza en diálogo.
- **Movimiento LATAM en la capa de práctica.** Ninguno. La región aparece en este pase **como fuente del instrumento de
  evaluación**, no como productora de la capa.

### Nota de verificación del pase, y contradice una fuente secundaria

Una fuente secundaria de este pase (una guía comercial sobre el EU AI Act en educación) afirma que la fecha de
aplicación general del AI Act fue el **2026-08-02**. **Esta KB no lo adopta.** El **trend 25** tiene documentado, con
fuentes primarias, que el **Digital Omnibus on AI entró en vigor el 2026-07-27** y corrió el **Anexo III —que es el que
cubre educación— a 2027-12-02**. Se registra la discrepancia para que una pasada futura no haga regresar el dato: **la
fecha del Anexo III sigue siendo 2027-12-02.** `arxiv.org`, `huggingface.co` y `www.iesalc.unesco.org` siguen bloqueados
por el proxy de egreso; lo que vino de ahí está marcado 🔴 donde corresponde.

## 2026-10-01 (pase 12) — once pasadas midieron la educación contra sí misma: medida contra la vertical científica, pierde 58× en el canal más barato

Duodécima corrida. Las once anteriores compararon repos educativos **entre sí** —el mejor tutor, el mejor benchmark, el
mejor LMS— y de ahí salieron todos los "techos" de esta KB. Este pase cambia el denominador: **compara la vertical
educativa contra otra vertical en el mismo canal de distribución**, y el resultado es el peor número que registró esta KB.

### 🔴 El hallazgo del pase, y es una división

Canal: **Agent Skills**, el estándar de paquetes de instrucciones que cargan Claude Code, Codex, Cursor, Antigravity y
Gemini CLI. Sin backend, sin despliegue, sin infraestructura: un repo de Markdown. Verificado contra la página de cada
repo el 2026-10-01.

| Biblioteca de skills | Vertical | Licencia | Stars |
|---|---|---|---|
| https://github.com/K-Dense-AI/scientific-agent-skills | Ciencia | **MIT** ✅ | **47.200** |
| https://github.com/virgiliojr94/book-to-skill | Genérico | **MIT** ✅ | **33.200** |
| https://github.com/GarethManning/education-agent-skills | **Educación** | CC BY-SA 4.0 ⚠️ | **815** |
| https://github.com/ZeKaiNie/universal-examprep-skill | **Educación** | **MIT** ✅ | **299** |

**58× contra el activo educativo más grande. 158× contra el mejor educativo que se puede empaquetar.**

La vertical científica construyó en este canal una biblioteca de **181 skills + 100 bases de datos** con licencia MIT
que declara 160.000 científicos usuarios. La vertical educativa, con un mercado más grande y una base de usuarios
incomparablemente mayor, puso **165 skills con *share-alike*** y nada más de tamaño comparable.

### Por qué esto no es una curiosidad de estrellas

Las once pasadas anteriores vinieron documentando que lo bueno en educación es **caro de desplegar** (plataformas),
**copyleft** (accesibilidad, pase 8), **archivado** (analítica institucional, pase 11) o **de licencia trampa**
(contenido OER, pase 10). El canal de skills no tiene ninguno de esos problemas: es texto, es permisivo en su mayoría,
no se despliega y **la arquitectura de referencia es pública y MIT**. Es decir: **la capa donde la educación está más
atrasada es justo la que tiene la barrera de entrada más baja de toda esta KB.**

Para un studio eso invierte la pregunta. No es *"¿qué plataforma adaptamos?"* sino *"¿por qué el activo pedagógico
permisivo de referencia no existe todavía, si cuesta Markdown?"*

### Los seis paquetes educativos nuevos, verificados uno por uno

| Repo | Licencia | Stars | Qué agrega que la KB no tenía | Región |
|---|---|---|---|---|
| https://github.com/24kchengYe/human-skill-tree | **AGPL-3.0** ⚠️ | 562 | Híbrido skills + app: 33 competencias de K-12 a carrera, con repetición espaciada y aula multi-agente. v2.0 del 2026-03-18 | APAC |
| https://github.com/ZeKaiNie/universal-examprep-skill | **MIT** ✅ | 299 | **Cita de página sobre la diapositiva de la cátedra** — el único de la capa con atribución a la fuente como mecanismo anti-alucinación. Memoria entre sesiones | Global (bilingüe EN/zh) |
| https://github.com/karanb192/algo-sensei | **MIT** ✅ | 281 | Pistas progresivas en vez de solución + mock interview. Es *empleabilidad*, no currículo | Global |
| https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill | **MIT** ✅ | 234 | **Diagnóstico antes de instrucción**, sin menú de modos: el agente decide el próximo paso útil | Global |
| https://github.com/KeWang0622/kaogong-skill | **MIT** ✅ | 147 | Examen de servicio civil chino: 3,7 M de postulantes/año contra cursos de 10–30 k CNY. **Caso claro de skill como sustituto de un mercado de preparación pago** | APAC (China) |
| https://github.com/learning-commons-org/agent-skills | **Apache-2.0** ✅ | 35 | Material docente **alineado a estándares K-12** con *guardrails* por workflow. El único de la capa pensado para cumplimiento curricular | North America |

Cinco de seis son MIT o Apache-2.0. Suman **996 ★** y ninguno tiene backend.

### El segundo hallazgo, y corrige una conclusión del pase 5

El pase 5 cerró la **capa MCP de mastery** diciendo que eran "cinco reinvenciones del mismo patrón" con techo de **1 ★**.
Eso sigue siendo cierto para los cinco, y es incompleto: existe
**[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) — MIT, 499 ★, 254 commits, v0.22.0**, puente MCP hacia
**Anki**.

La diferencia no es calidad: **los cinco inventan su modelo de dominio y Anki ya es el estándar instalado.** Leído con
`py-fsrs` (MIT, el algoritmo que reemplaza a SM-2, ya en la KB), la conclusión operativa cambia de signo: **no construir
el motor de repetición espaciada; conectarse al que el alumno ya tiene abierto.** Ver **P28**.

### Lo que este pase deja abierto

**Ninguna de las siete skills educativas tiene *eval* publicada.** Son prompts sin versionado semántico, sin suite de
regresión y sin medición de efecto. Y esta KB **ya tiene** la capa de evaluación para medirlas (MathTutorBench,
UnifyingAITutorEvaluation, EduBench, EduGuardBench, del pase 4) — construida para tutores con backend y **nunca aplicada
a una skill**. Las dos piezas están en el mismo repositorio de conocimiento y no se tocan. Ese es el gap 20.

### Nota de método, para que un pase futuro no se equivoque

- **El agregador de estrellas miente en esta categoría.** Los dos repos baseline dieron **26.5k** y **13.7k** vía
  agregadores de terceros, y **47.2k** y **33.2k** en la página del repo el mismo día. Con `book-to-skill` sumando
  +6.3k ★/mes, el dato de tercero no está viejo: **está mal**. Sólo vale la página del repo.
- **Un 403 de `curl` no es un 404.** Se pasaron las **164 URLs de GitHub de toda esta KB** por `curl -sL` y
  **las 164 dieron 403**: es el proxy del entorno, no *link rot*. **Esas 164 URLs no quedaron revalidadas en este pase**
  — no hay evidencia de que estén caídas ni de que estén vivas. La verificación de primera mano se hace con **WebFetch**.

## 2026-10-01 (pase 11) — diez pasadas preguntaron qué hace el agente y ninguna qué decide: aparece la capa predictiva, y es la peor abastecida de la KB

Undécima corrida. Las diez anteriores cubrieron el agente, su contenido, su telemetría, su evaluación, su seguridad
pedagógica, su accesibilidad y su credencial. **Faltaba la capa que toma decisiones sobre el alumno** —riesgo de
abandono, *early alert*, *student success*—, que es la que la universidad ya tiene presupuestada y la que el
**Anexo III del EU AI Act nombra de forma explícita.** Está vacía, y este pase la mide en vez de describirla.

### 🔴 El hallazgo del pase, y son dos números

| Consulta en GitHub, 2026-10-01 | Resultado | Techo de estrellas |
|---|---|---|
| `topic:learning-analytics stars:>50` | **2 repos en todo GitHub** | 169 ★ — y es un blog de notas de papers (`AkihikoWatanabe/paper_notes`), no un sistema |
| `dropout prediction student license:mit pushed:>2026-01-01` | **110 repos** | **6 ★** |

**El techo de la capa predictiva open source permisiva es un repo de 6 estrellas que entrena con datos sintéticos.**
Es `Aliipou/Student-Retention-Prediction` (MIT, señales de engagement a la semana 4, SHAP, 137 tests declarados) y
su pipeline genera su propio dataset: no hay datos reales detrás y no hay auditoría de fairness. Ver `agents/top.md`.

Para comparar con lo que esta KB ya sabía: la capa de **evaluación pedagógica** (gap 1) también es chica, pero sus
artefactos están premiados en EMNLP y NAACL. Acá no hay ni eso. **Es la primera capa de esta KB donde el techo no es
académico ni institucional, sino un proyecto de portafolio.**

### Lo que estaba y se murió, y es el dato que una propuesta tiene que saber

La capa *sí* tuvo un stack institucional: la **Apereo Learning Analytics Initiative**, 21 repos. Verificado uno por
uno (ver `repos/foundations.md`):

- `OpenLRS` → **archivado, y su descripción es la palabra `Deprecated`**
- `OpenDashboard-legacy` → **`(Deprecated)`** declarado
- `OpenDashboard-ux` + `OpenDashboard-api` → el reemplazo. **Creados el 2020-02-12, abandonados dentro del mes.** 1 ★ y 0 ★
- `LearningAnalyticsProcessor` → el orquestador del pipeline. 23 ★, **último push 2023-01-19**
- `OpenLRW` → **la única pieza viva: 62 ★, ECL-2.0, push del 2026-08-04**, y habla xAPI + Caliper + OneRoster a la vez
- *Student Success Plan* (SSP), el producto de advising con despliegues reales → **sin repositorio localizable; el rastro público se corta en 2014-2015**

**La capa no se desinfló: se intentó reescribir una vez, en febrero de 2020, y el intento duró tres semanas.**

### La trampa de método que este pase encontró, y es la más cara de todas

**Esta KB venía filtrando por MIT / Apache-2.0 / BSD, y ese filtro excluía en silencio a todo Apereo.** Apereo
licencia con **ECL-2.0**: Apache-2.0 con el alcance de la concesión de patentes de la sección 3 acotado para
universidades, **aprobada por OSI y por la FSF**, no copyleft. Lo que el filtro dejaba afuera:

| Repo | Licencia | Stars | Último push |
|---|---|---|---|
| https://github.com/sakaiproject/sakai | **ECL-2.0** | **1.234** | 2026-09-30 |
| https://github.com/opencast/opencast | **ECL-2.0** | 505 | 2026-09-30 |
| https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW | **ECL-2.0** | 62 | 2026-08-04 |
| https://github.com/uPortal-Project/uPortal | Apache-2.0 | 286 | 2026-09-22 |

**Sakai es el LMS que faltaba después de diez pasadas, y faltaba por una línea de licencia mal leída, no por falta
de búsqueda.** Y `opencast` cubre la capa de video de clase, que ningún otro repo de esta KB toca.

### Lo nuevo y utilizable de la ventana, verificado

| Repo | Licencia | Stars | Por qué entra |
|---|---|---|---|
| https://github.com/madhvantyagi/Gnos | **MIT** ✅ | 304 | *Teaching harness* que arma el curso con subagentes y después los revisa. **Lo citable es su registro de evidencia: distingue "vio la explicación" / "resolvió con ayuda" / "resolvió solo"** — la distinción sin la cual ninguna medición de mastery significa nada, y que los tutores LLM de esta KB no instrumentan. 344 commits |
| https://github.com/vasanthsreeram/Alvarmethod | **MIT** ✅ | 160 | Pedagogía como **skill portable** instalable en seis harnesses con un comando. Loop explícito *probe → plan (DAG Mermaid) → teach (un paso por vez) → lock-in quiz*. **4 commits:** es una especificación, no un producto, y por eso sirve |
| https://github.com/DECK6/korean-elementary-learning-map | **MIT** ✅ | 117 | Ontología del **currículo primario coreano 2022**: 620 anclas de estándares, 1.956 temas, **2.293 relaciones de prerrequisito**, JSON + RDF/Turtle con SPARQL y SHACL. **Es el contrapunto permisivo de `OpenDidactia`** (España, CC BY-SA): mismo artefacto, mejor licencia, y con el grafo de prerrequisitos que al español le falta |
| https://github.com/terracotta-education/terracotta | **Apache-2.0** ✅ | 21 | Plug-in de LMS para correr **RCTs dentro del aula**, con consentimiento informado oculto al docente y anonimización en las exportaciones ya resueltos. 2.572 commits. **La única pieza permisiva de esta KB con la que se puede *demostrar* que una intervención funcionó** |
| https://github.com/ai-builders-foundation/ai-builders-curriculum | **MIT** ✅ | 1.4k | Currículum full-stack de AI vendor-neutral de una **501(c)(3)**, con 3 starter kits ejecutables. Creado el 2026-07-05. Capa de *capability building*, que en educación corporativa es la mitad de la demanda |

### Lo que apareció grande y no se puede usar, y es una tendencia en sí

| Repo | Stars | Problema |
|---|---|---|
| https://github.com/amosblomqvist/learn | **2.9k** | 🚫 **Sin licencia.** Y no es software: es una **configuración `.pi`** —una skill con la filosofía de enseñanza más definiciones de subagentes— con **2 commits**. **El artefacto educativo más estrellado creado en esta ventana es un archivo de configuración sin licencia** |
| https://github.com/jude-miller-dev/Milky-institute-online | 374 | 🚫 **Sin licencia.** Plataforma de **formación profesional para adultos** sobre SpringCloud Alibaba + **Spring AI**, con agente de recomendación de cursos y módulo LangChain en desarrollo. Bilingüe zh/en, 15 commits. **Es el artefacto de formación profesional más grande que encontró esta KB en once pasadas** — y el gap 10 sigue abierto por licencia, no por ausencia |
| https://github.com/novatrix-2030/SIH-2026 | 0 | 🚫 **Sin licencia.** "DropGuard", early warning explicable para instituciones de la India: Next.js 14 + FastAPI + LightGBM/XGBoost + SHAP + Groq. Entrega del **Smart India Hackathon 2026** (`SIH-2026-13-002`, *Smart Education*). **El patrón del gap 2 se repite fuera de LATAM** |
| https://github.com/classmoji/classmoji | 83 | ⚠️ **AGPL-3.0.** Toolkit Git-native para enseñar programación: autograding con GitHub Actions, gradebook y **generación de quizzes con Claude**. 2.074 commits, actividad al 2026-10-01. **Es lo más vivo que encontró esta KB en la capa de grading (gaps 6 y 9) y vuelve a ser copyleft** — van cinco pasadas con la misma asimetría |

### El reloj regulatorio se movió, y hay que corregir lo que esta KB afirmaba

**El Anexo III del EU AI Act ya no vence el 2026-08-02: vence el 2027-12-02.** Lo cambió el **Digital Omnibus on AI,
Reglamento (UE) 2026/1744**, en vigor desde el **2026-07-27**. Afecta directamente a esta capa, porque el Anexo III
nombra la evaluación de resultados de aprendizaje, el screening de postulantes y el monitoreo de exámenes. Ver la
tendencia 25 y el patrón **P25** en `compose/patterns.md`. 🔴 Verificado en fuentes legales secundarias
coincidentes; `eur-lex.europa.eu` y `digital-strategy.ec.europa.eu` están bloqueados por el proxy de esta sesión.

### Lo que esta pasada buscó y no encontró

- **Un sistema de early warning open source mantenido, de cualquier región.** No existe. 110 repos MIT con techo de 6 ★, un stack institucional archivado, y un producto de advising (SSP) sin repo. Es el gap 18, nuevo.
- **Un predictor de deserción con auditoría de fairness publicada.** Varios repos declaran SHAP (explicabilidad) y uno declara *fairness audit* en la descripción, pero ninguno de los verificados publica el resultado de la auditoría. Para un sistema Anexo III, explicabilidad sin equidad medida no alcanza.
- **Movimiento en LATAM en esta capa.** Las búsquedas en portugués y español devuelven **investigación académica, no software**: revisión sistemática de 11 estudios 2022-2026 sobre riesgo de evasión en primaria (UFPE), tesis y papers de institutos federales con Random Forest y XGBoost. **La región produce el paper y no el repo** — que es el espejo exacto del gap 2, donde produce el repo y no la comunidad.
- **Sakai con AI.** El LMS está activo y mantiene dos ramas, pero no se localizó un subsistema de AI comparable al de Moodle 4.5+. Si el engagement necesita AI sobre Sakai, hoy se construye; sobre Moodle, se configura.

### Sin movimiento en los dos grandes, y van cinco pases

`DeepTutor` (40.590 ★) y `OpenMAIC` (39.693 ★) siguen en el mismo orden de magnitud que el pase 10, los dos con
actividad del 2026-10-01. La concentración APAC del gap 4 no se mueve.

## 2026-10-01 (pase 10) — nueve pasadas preguntaron qué hace el agente y ninguna de qué lee: aparece la capa de contenido, y con una trampa de licencia adentro

Décima corrida. Los pases 4–9 construyeron el stack del alumno por capas: modelado, evaluación, seguridad, telemetría,
datos de entrenamiento, accesibilidad, credencial. **Ninguna preguntó de dónde sale el material que el agente enseña.**
La palabra «OER» no aparecía ni una vez en esta KB antes de este pase.

Es la **quinta** aplicación de la regla del pase 6: *cuando un gap sobrevive varias pasadas, revisar si la pieza que falta
tiene un nombre que uno no está usando.* Acá el nombre era **OER / Open Educational Resources**, y el contenido no se
llama ni «agente» ni «tutor» ni «dataset».

### 🔴 El hallazgo del pase, y pega sobre el patrón base de esta KB

Dos fuentes de primera mano, verificadas las dos en este pase, dicen cosas incompatibles sobre el mismo contenido:

| Artefacto | Dice | Nivel de la página |
|---|---|---|
| `openstax/osbooks-calculus-bundle` | *«Calculus Volume 1, Calculus Volume 2, and Calculus Volume 3 are available under the Creative Commons Attribution-**NonCommercial-ShareAlike** License»* | archivo **`LICENSE`** |
| `openstax/osbooks-biology-bundle` | **CC BY-NC-SA** (Biology 2e, Concepts of Biology, Biology for AP®) | archivo **`LICENSE`** |
| `openstax/osbooks-college-physics-bundle` | **CC BY-NC-SA** (College Physics 2e y la edición AP®) | archivo **`LICENSE`** |
| `CAHLR/OATutor` | *«All content in this repository is made available under the Creative Commons Attribution 4.0 International (**CC BY 4.0**) license»* — y cura problemas de **Calculus Volume 1** | **README** |
| `pythpythpython/openstax-mcp-server` | el contenido servido es *«**CC BY 4.0**»* | **README** |

**Por qué importa y no es una discusión de abogados.** **NonCommercial prohíbe exactamente el uso que tiene un entregable
facturado**, y **ShareAlike obliga a licenciar la derivación con la misma licencia** — es decir, a abrir el corpus que se
construyó para el cliente. Las dos condiciones pegan sobre el caso de uso central de un engagement.

**Y pega sobre P1, el patrón base de esta KB**, que recomienda textualmente *«la lógica de BKT de OATutor + su contenido
curado de OpenStax en JSON»*. El código MIT de OATutor no está en discusión. **El contenido sí.** P1 queda corregido.

**Lo que este pase NO afirma:** cuál de las dos licencias es la correcta. `openstax.org` —donde vive el catálogo con la
licencia por título— está **bloqueado por el proxy de egreso** (gap 17). Se registra la contradicción sin resolverla,
porque resolverla a favor de cualquiera de los dos lados sería inventar el dato que falta.

**La regla operativa, que el propio README de OATutor regala:** la licencia está declarada **por ítem**, dentro de cada
JSON (*«indicating the authoring organization and license for each hint, scaffold, and problem»*). Entonces se lee el ítem,
no el badge del repo — y el manifiesto de licencias por ítem **es el entregable** (ver **P22**).

### El puente agente↔contenido existe, y es uno solo

| Repo | Licencia | Stars | Commits | Qué hace |
|---|---|---|---|---|
| https://github.com/pythpythpython/openstax-mcp-server | **MIT** (código) ✅ | **1** | 7 | Servidor MCP sobre **40+ libros de OpenStax**: búsqueda semántica (embeddings de Cloudflare AI), generación de notebooks `.ipynb` por módulo, creación de problemas de práctica. Cloudflare Workers + Workers KV |
| https://github.com/moarshy/mcp-tutor | 🚫 **sin licencia** | **0** | 26 | Convierte **repositorios de documentación** en cursos con DSPy y los expone por MCP. Es tutoría de documentación técnica, **no de currículo escolar**. El repo sólo declara: *«This project is experimental and intended for educational and research purposes»* |

**Es exactamente la misma forma que el pase 6 encontró en telemetría y el pase 9 en credenciales:** la capa existe, el
estándar existe, y el puente hacia el agente es **un repo de una estrella**. Ver el **gap 15**.

### Lo que sí está limpio, y es el caso que conviene conocer

**Oak National Academy** publica su currículo bajo **Open Government Licence v3.0**, que **permite uso comercial de forma
explícita**. Y `Aila`, su asistente de planificación de clases, ya está en esta KB desde el pase 5 con licencia **MIT**.
**Es el único caso de esta KB donde el código y el contenido son los dos utilizables en un entregable facturado.**

⚠️ **Dos reservas, las dos honestas:** `support.thenational.academy` está **bloqueado por el proxy**, así que la licencia
viene de prensa educativa británica (*Schools Week*) y no del documento; y en esa misma cobertura hay indicios de
**restricción geográfica al Reino Unido**, que hay que confirmar antes de proponer el corpus fuera de UK.

### Lo que esta pasada buscó y no encontró

- **Un agente que genere contenido con la licencia puesta.** Ninguno de los 26 agentes de la tabla principal emite el
  metadato de licencia del material que produce o deriva. Es el mismo hueco que el pase 9 encontró con las credenciales:
  el artefacto se genera sin la pieza que lo hace usable ante un tercero.
- **Un recomendador curricular open source sobre catálogo abierto.** No se puede construir comercialmente: el **metadato**
  de OER Commons (ISKME) es **NonCommercial**. Ver el **gap 16**.
- **Contenido abierto de formación profesional con licencia apta.** `LibreTexts` declara tener materia de *workforce
  development*, pero su plataforma es **GPL-3.0** y no se pudo verificar la licencia del contenido por título. El **gap 10**
  no se cierra.

### Sin movimiento en los dos grandes, y van cuatro pases

`DeepTutor` y `OpenMAIC` siguen planos en el orden de magnitud que la KB ya registró. Lo que cambió en este pase no es el
ranking de agentes: es **el indicador**. Ver `repos/trending.md` — en la capa de infraestructura pública desplegada, el
cociente **forks/stars** encuentra lo que las estrellas esconden (Sunbird: **41 ★ / 317 forks / 38.046 commits**).

---

## 2026-10-01 (pase 9) — la capa que acredita: aparece el stack de credenciales verificables, y tres de sus implementaciones de referencia ya no están

Novena corrida. El pase 8 encontró un segmento entero buscando por **población de alumnos** en vez de por capa técnica.
Este pase cambia el eje otra vez y mira **el final del recorrido**: qué pasa cuando el aprendizaje termina y hay que
acreditarlo de forma que un tercero lo verifique sin llamar a la institución emisora.

Esa capa existe, tiene estándares con certificación de conformidad y una década de recorrido —**Open Badges 3.0**,
**W3C Verifiable Credentials**, **QTI**, **OneRoster**, **Caliper**— y **las ocho pasadas anteriores no la tenían.**
Es la cuarta aplicación de la regla del pase 6: cuando falta una capa, preguntarse si tiene un nombre que uno no usa.

### 🔴 El hallazgo del pase, y no es un repo nuevo

**Las implementaciones de referencia de estos estándares se están apagando mientras los estándares siguen siendo obligatorios.**

| Qué era | URL que los listicles siguen citando | Verificado 2026-10-01 |
|---|---|---|
| **Badgr**, implementación de referencia de Open Badges | `concentricsky/badgr-server` | 🔴 **404**, y la búsqueda de repos de la organización por `badgr` devuelve *«No repositories matched your search»*. La organización **verifica hoy el dominio `instructure.com`** (Eugene, Oregón): Badgr → Canvas Credentials → Parchment Digital Badges |
| **caliper-php**, cliente PHP oficial de Caliper | `1EdTech/caliper-php` | 🔴 **404.** El fork de la **Universidad de Michigan** nombra la causa en su banner, textual: *«This had been archived, but has been unarchived following 1EdTech making its caliper-php private.»* |
| **caliper-python**, Sensor API de referencia | `IMSGlobal/caliper-python` | 🔴 **404** |

**El rigor que corresponde:** un 404 no distingue borrado de renombrado de privado — desde afuera son indistinguibles.
Verificado de primera mano está que **las tres URL no resuelven**, que en `badgr-server` hay una segunda señal
independiente (la búsqueda interna de la organización no devuelve nada) y que en `caliper-php` **el mantenedor del fork
nombra al responsable**. No se afirma más que eso.

**Y el mismo patrón en Europa, por otra vía:** los dos repos del stack de credenciales de la Comisión Europea
—`european-digital-credentials` (EUPL-1.2, 6 ★) y `European-Learning-Model` (EUPL-1.2, 54 ★)— están **archivados**
(2024-02-02 y 2024-02-14) con el aviso de que el código vivo se mudó a `code.europa.eu`, **que el proxy de egreso de
esta sesión bloquea**. El stack europeo de credenciales salió de GitHub, y por eso ninguna búsqueda en GitHub lo ve.

### Lo que sí está vivo, y de dónde sale

Ocho piezas verificadas repo por repo. Lo relevante es **quién las sostiene**: ya no el organismo de estándares ni el
vendor de referencia, sino **terceros certificados, consorcios universitarios y forks de universidad**.

- **`amp-up-io/qti3-item-player`** (**MIT**, 30 ★, 596 commits) — runtime de ítems **QTI 3** con scoring completo y
  **certificación de conformidad QTI 3 Basic y Advanced «Delivery» de 1EdTech**. Es el **único artefacto de toda esta KB,
  en cualquier capa, con certificación de conformidad de un organismo de estándares.** Licencia leída en el archivo:
  `Copyright (c) 2022-2024 Amp-up.io, LLC`.
- **`digitalcredentials/learner-credential-wallet`** (**MIT**, 88 ★, **1.309 commits**) — la billetera del alumno, y la
  pieza más trabajada de la capa. ⚠️ Ver el cambio de gobernanza abajo.
- **`digitalcredentials/verifier-plus`** (**MIT**, 18 ★, 395 commits) — verificación y visualización, incluido QR.
- **`digitalcredentials/issuer-coordinator`** (**MIT**, 12 ★, 55 commits) — emisión, revocación y suspensión por
  **W3C VC API**, con soporte de formato **Open Badges 3.0**.
- **`1EdTech/lti-1-3-php-library`** (**Apache-2.0**, 124 ★, 110 commits) — **LTI 1.3**: lo que monta un agente *dentro*
  de cualquier LMS conforme. Es la pieza con más estrellas de la capa que sigue pública y permisiva.
- **`KonstantinosPetrakis/esco-skill-extractor`** (**MIT**, 32 ★, 29 commits) — texto libre → competencias **ESCO** y
  ocupaciones **ISCO**. El puente entre «terminó el módulo» y «acredita esta competencia».
- **`LongsightGroup/oneroster`** (**MIT**, 0 ★, 33 commits) — **OneRoster 1.1/1.2**, CSV y REST, Node/Deno/navegador.
- **`luisgf/openbadgeslib`** (**LGPLv3** librería / **BSD-2-Clause** CLI, **1 ★**, **404 commits**, v4.0.0 del
  2026-07-22) — el ciclo completo de emisor OB 3.0: JWT-VC, `did:web`, **Bitstring Status Lists** para revocar.
  **El código de emisión más completo que encontró esta KB, con una estrella.**

### El cambio de gobernanza que hay que saber antes de proponer la billetera

La página de `learner-credential-wallet` declara que la **v2.2.10 (junio 2026) es el último release como *Digital
Credentials Consortium at MIT***, y que el proyecto pasa a **OpenWallet Foundation Labs**. Señal independiente del mismo
movimiento: la organización de GitHub ya no se presenta como «Digital Credentials Consortium» sino como **Digital
Credentials Commons** (`dccommons.org`, EE. UU., 124 repos públicos).

**No es abandono** — un traspaso a una fundación neutral suele ser madurez, como ya registró esta KB con `goose` hacia la
Linux Foundation. **Pero la cadena de custodia cambió hace cuatro meses:** al proponerla hay que **fijar la versión y
confirmar dónde vive el mantenimiento activo**, no citar el repo del MIT como si nada hubiera pasado.

### La asimetría de licencias, otra vez, y van tres pases seguidos

El pase 8 encontró que en accesibilidad **lo maduro es copyleft y lo permisivo no tiene tracción**. Esta capa repite la
forma con precisión incómoda: lo más maduro es **`oat-sa/tao-core`** (**GPL-2.0**, **22.533 commits** — por volumen de
trabajo, la pieza más madura de toda esta KB en cualquier capa) y lo más completo en emisión es **`openbadgeslib`**
(**LGPLv3**, 404 commits, **1 estrella**). Lo permisivo y vivo son piezas de 12 a 124 estrellas.

Entran además **tres familias de licencia nuevas** para esta KB —**GPL-2.0**, **LGPLv3/LGPL-3.0** y **EUPL-1.2**— y la
LGPL tiene un matiz que la GPL no tiene: enlazar desde un producto cerrado es admisible, **modificar y distribuir no**.
Muerde exactamente donde uno querría tocar, porque los perfiles de badge son específicos de cada cliente. Ver la tabla
de advertencias en `agents/top.md`.

### Lo que esta pasada buscó y no encontró

**Ningún agente open source emite ni consume credenciales verificables.** Se buscó explícitamente: ninguno de los 25+
agentes de la tabla principal escribe un Open Badge, y ninguna pieza de credenciales tiene interfaz de agente ni servidor
MCP. **El stack del alumno y el stack de la credencial no se tocan en ningún punto.** Es el **gap 13**, nuevo, y la pieza
que los uniría ya está en esta KB desde el pase 6: el LRS registra la evidencia, el estimador de mastery decide si hay
dominio, y nadie convierte esa decisión en una credencial verificable. Ver **P19**.

**Tampoco apareció** un agente educativo nuevo de escala en la ventana. Se verificó `Seechange-edu/act-ai-tutor-backend`
—que aparece en búsquedas por sus releases del 2026-09-15 y 2026-09-30— y es **0 ★, 24 commits y sin archivo de
licencia**: no es un hallazgo, es un repo de trabajo de alguien. Se registra para que la próxima pasada no lo persiga.

## 2026-10-01 (pase 8) — la KB buscó siete veces por lo que hace el software y nunca por quién es el alumno: aparece un segmento entero

Octava corrida del día. El pase 7 dejó escrita la lección de que la consulta importa más que el mercado — se había buscado `agent` y `benchmark` y nunca `tutor`. Este pase comete el mismo tipo de hallazgo un nivel más arriba y es el más grande de la serie: **las ocho pasadas buscaron por capa técnica o por categoría de producto, y ninguna buscó por *población de alumnos*.** Buscando por el alumno con discapacidad aparece un segmento completo que la KB no tenía.

### Lo que apareció, y la forma que tiene

**Doce repos verificados de primera mano.** El hallazgo no es ninguno de ellos: es que el segmento **se parte en dos mitades y ninguna sirve sola**.

**Mitad madura — toda copyleft:**

| Repo | Licencia | Stars | Qué es |
|---|---|---|---|
| https://github.com/OptiKey/OptiKey | **GPL-3.0** ⚠️ | **4.4k** | Control total de computadora y habla **con la mirada** (ELA / motoneurona) |
| https://github.com/cboard-org/cboard | **GPL-3.0** ⚠️ | 759 | **AAC** con texto-a-voz en navegador. 5.531 commits. Respaldo de **UNICEF** |

**Mitad agéntica y permisiva — techo de 15 estrellas:**

| Repo | Licencia | Stars | Commits | Origen |
|---|---|---|---|---|
| https://github.com/AyushBinjola1/Swar-Setu | **MIT** ✅ | 15 | 4 | APAC (India) — dislexia, disgrafia, discalculia |
| https://github.com/open-behavior-analysis/aba-clinical-agent | AGPL-3.0 ⚠️ | 7 | 7 | 29 Claude Code Skills para supervisión clínica ABA |
| https://github.com/ronda-ai/Ronda-App | GPL-3.0 ⚠️ | 3 | 17 | **LATAM (Chile)** — aula inclusiva, anclado al MBE |
| https://github.com/Noggin-Labs/noggimigo | **MIT** ✅ | 1 | 19 | Tutor socrático local; **latencia como señal de carga cognitiva** |
| https://github.com/100205ivan/EyeEP | 🚫 sin licencia | 1 | 12 | APAC (Taiwán, inferido) — gestión de IEP |
| https://github.com/marcorojasb/tero | **MIT** ✅ | **0** | **111** | **LATAM (Chile)** — MINEDUC, Decreto 83, Ley 21.719 |
| https://github.com/SabioTechTeam/Teacher-Hub | MIT ⚠️ | 0 | 156 | *UnStuck* — CAT + parsing de acomodaciones IEP/504 |

### El repo del pase, y no es un repo educativo

**`accessibility-agents`** — https://github.com/Community-Access/accessibility-agents — **MIT, 419 ★, 374 commits.** Agentes de revisión **WCAG 2.2 AA** que corren dentro de Claude Code, GitHub Copilot, Claude Desktop, Codex y Gemini CLI, sobre código, documentos (Word, Excel, PowerPoint, **PDF y ePub**) y markdown.

**Tiene más tracción que cualquier pieza de educación especial de este pase y que casi toda la capa de evaluación pedagógica de la KB** — y ninguna búsqueda educativa lo iba a encontrar nunca. Ataca la obligación que **ya está vigente** (European Accessibility Act, **2025-06-28**) en vez de la que está prohibida.

### Las dos cosas que cambian una propuesta

**1. En EE. UU., el open source apunta justo al paso prohibido.** Lo poco que hay de educación especial agéntica apunta a **redactar o gestionar el IEP**. **Delaware** prohíbe usar AI para objetivos de IEP, evaluación docente y calificación subjetiva; **Nueva York** prohíbe usarla para desarrollar planes IEP o 504. Un producto que redacta IEPs es invendible en los distritos más grandes del país. Lo vendible es el resto del flujo — **P18**.

**2. Un repo chileno de 0 estrellas tiene la arquitectura correcta.** `tero` implementa *«el agente propone, el docente decide»* con gate humano obligatorio, por **Decreto 83** chileno — o sea que llegó por restricción local a la misma arquitectura que la regulación estadounidense está imponiendo. Con **dos repos chilenos** en este pase (`tero`, `Ronda`), más Latam-GPT y el Observatorio UNESCO en la CEPAL, **Chile se está volviendo el nodo técnico de LATAM**. El gap 2 **no se cierra** — 0 y 3 estrellas — pero cambia dónde buscar contraparte.

### Trampas registradas en este pase

- **Colisión de siglas:** el topic `aac` de GitHub tiene 600+ repos y casi todos son **Advanced Audio Coding**, no *Augmentative and Alternative Communication*. Usar `assistive-technology`, `special-education`, `inclusive-education`.
- **Licencia internamente contradictoria:** `Teacher-Hub` declara *«MIT License — free for educational and non-commercial use»*. Las dos mitades se contradicen. Segunda vez que la KB encuentra esto (la primera fue OpenTutorAI-CE).
- **Techos medidos:** topic `special-education` → 20 repos, techo 10 ★ (y está deprecado); `inclusive-education` → 30 repos, techo 60 ★ (y sin licencia); búsqueda `IEP ... AI` → **1 repo en todo GitHub**.

⚠️ **Verificación:** los doce repos se abrieron vía WebFetch contra su página de GitHub. `uisight` (128 ★) y `a11y-agents-kit` (34 ★) se abrieron después para cerrar la licencia: **las dos son MIT**. Lo regulatorio (EAA, Delaware, Nueva York) viene de resultados de búsqueda, **no del texto normativo**.

---

## 2026-10-01 (pase 7) — la KB estuvo buscando "agente" y el mercado dice "tutor": tres repos grandes que faltaban, y ninguno se puede empaquetar

Séptima corrida del día. Los seis pases anteriores construyeron el stack por capas —agente, modelado, evaluación, seguridad, telemetría— y la lección de método que se venía repitiendo era **"buscá la pieza técnica, no la categoría"**. Este pase encuentra el error complementario, y es más barato de cometer: **se buscó siempre por `agent`, `benchmark` y `tutoring system`, y nunca por la palabra que usa el mercado — `tutor`.**

Tres repos con más estrellas que casi todo lo que la KB tenía anotado estaban afuera por eso.

### Los tres que faltaban

| Repo | Licencia | Stars | Commits | Qué es | Región |
|---|---|---|---|---|---|
| **llamatutor** — https://github.com/Nutlope/llamatutor | 🚫 **sin licencia** (verificado: `/blob/main/LICENSE` → **404**) | **2.1k** | 132 | Tutor personal sobre Llama 3 70B + Together.ai. Next.js + Tailwind, Exa.js para búsqueda, Helicone para observabilidad. Es una aplicación de producción, no una librería | Sin región declarada |
| **ChatTutor** — https://github.com/HugeCatLab/ChatTutor | **AGPL-3.0** ⚠️ | **1.3k** | n/d | Tutor **visual e interactivo**: canvas de matemática para ecuaciones y diagramas, y mapas mentales para visualizar conocimiento, **expuestos al LLM como herramientas que usa durante la explicación**. Desplegado en `chattutor.app`, API key del usuario. README bilingüe inglés/chino | Sin país declarado (documentación EN/中文) |
| **tutor-gpt** — https://github.com/plastic-labs/tutor-gpt | **GPL-3.0** ⚠️ | **931** | 356 | Compañero de aprendizaje con **razonamiento de teoría de la mente**: modela el estado mental del alumno y **reescribe sus propios prompts** en función de eso. Next.js + Supabase, inferencia vía OpenRouter, y la personalización delegada a **Honcho**, la librería de memoria del mismo laboratorio | **North America (EE. UU.)** — el perfil de la organización declara `United States of America` y `plasticlabs.ai` |

**El dato que ordena la tabla no son las estrellas, es la columna de licencia.** Los tres juntos suman **4.3k estrellas y cero posibilidad de empaquetado cerrado**: uno sin licencia (todos los derechos reservados por default), uno AGPL-3.0 (copyleft de red, el peor caso para SaaS) y uno GPL-3.0. Comparado con la tabla principal de la KB —donde DeepTutor es Apache-2.0 y OpenMAIC es MIT, con 40.6k y 39.7k— **la conclusión práctica no cambia: los dos grandes de APAC siguen siendo las únicas bases permisivas de escala.** Lo que cambia es que ahora está medido contra la alternativa, en vez de supuesto.

### `tutor-gpt` es el hallazgo que vale, y no por el tamaño

Es el único de los tres con una idea arquitectónica que la KB no tenía registrada en ningún agente: **no mantiene un modelo de mastery, mantiene un modelo del estado mental del alumno, y lo usa para reescribir su propio prompt.** Las seis pasadas anteriores trataron el problema del estado del alumno como *knowledge tracing* —qué conceptos domina, con `pyKT` o `pyBKT`— y esto es un eje distinto y complementario: qué está entendiendo, qué cree erróneamente, con qué intención pregunta.

Y la pieza reutilizable no es el tutor, es su dependencia: **`Honcho`** (https://github.com/plastic-labs/honcho, **AGPL-3.0** ⚠️, **7.4k ★**, Python, 760 commits) — memoria para agentes con estado, de propósito general, con enfoque *reasoning-first*: "extrae conclusiones de las conversaciones y los eventos, no sólo hace match de chunks". Modela a cada participante —humano o agente— como peer de primera clase.

**Cómo se lee junto con el pase 6.** El pase 6 agregó la capa de telemetría de aprendizaje (xAPI / IEEE 9274.1.1 + `learnmcp-xapi`) y concluyó que los cinco servidores MCP de mastery habían inventado su propio almacén de eventos cuando existía un estándar. `Honcho` es la **otra** respuesta al mismo problema, y es importante no confundirlas:

| | xAPI / LRS (pase 6) | Honcho (pase 7) |
|---|---|---|
| Qué guarda | **Hechos de aprendizaje** conformes a un estándar IEEE: "practicó bucles", "aprobó el módulo 3" | **Conclusiones inferidas** sobre la persona: preferencias, creencias, estado mental |
| Para qué sirve | Expediente auditable, portabilidad, conformidad | Personalización y continuidad de la relación |
| Ante un regulador | Es evidencia: esquema estándar, verbos acordados | **No es evidencia**: son inferencias de un modelo sobre un alumno, 7.4k ★ y AGPL-3.0 |

**No son sustitutos y conviene decirlo en una propuesta:** un tutor serio quiere las dos, y la que va al expediente de conformidad es la primera. Usar Honcho como capa de registro de aprendizaje sería exactamente el error que el pase 6 documentó, con una licencia peor.

### ⚠️ Colisión de nombres que hay que registrar antes de que cueste algo

La KB lista en la tabla principal **`Bloom`** (https://github.com/Li-Evan/Bloom, **MIT**, 278 ★) — tutor que genera un syllabus y entrega una lección por vez.

**La versión hospedada de `tutor-gpt` también se llama "Bloom"**, y es un proyecto distinto, de otra organización, con otra licencia (GPL-3.0) y otra arquitectura. Las dos aluden a Benjamin Bloom, así que la colisión va a seguir apareciendo.

**La trampa concreta:** buscar "Bloom AI tutor" devuelve material de los dos indistintamente, y es fácil citar la arquitectura de uno con la licencia del otro. Cuando esta KB diga `Bloom` sin más, es **`Li-Evan/Bloom` (MIT, 278 ★)**; al otro se lo nombra siempre **`tutor-gpt`**, nunca por su marca.

### Lo que esta pasada buscó y no encontró

- **Formación profesional (gap 10): sigue vacío, y la búsqueda en inglés se contaminó.** Buscar `vocational OR berufsschule OR apprenticeship AI tutor` devuelve 24.481 resultados que son casi todos `tutorial` —GitHub no respeta límites de palabra en `in:name`— y entre los que sí son de FP no apareció nada nuevo con tracción por encima de lo que el pase 6 ya había anotado (`edufeedai`, 0 ★; `straussbastian/ai_flashcards_for_school`, 1 ★). **El gap 10 se mantiene sin cambios y sin matices nuevos.** Lo único que se agrega es una pista no verificable desde esta sesión: **AIVET** (`aivet-training.eu`), proyecto europeo de AI para proveedores de FP con siete módulos de formación de acceso abierto — 🔴 **el proxy de egreso bloquea el dominio**, así que no se pudo confirmar financiamiento, socios ni licencia de los materiales. Anotado como pista, no como hallazgo.
- **LATAM (gap 2): medido otra vez, y da lo mismo.** Búsqueda en GitHub por `tutor IA educativo español`: **197 resultados, y el techo entre los que realmente son tutores es de 3 estrellas.** Lo nuevo respecto del pase 6, todo en fase cero: `Javi111003/OlivIA-RAG` (tutor RAG para ingreso universitario en matemática, **1 ★, sin licencia**, último movimiento 2025-07) y `jrobador/finetuned-llama3.2-3B_mat-IA` (**3 ★**, segundo puesto del *Llama Impact Pan-LATAM Hackathon*, **sin actividad desde 2024-11**). El segundo es la ilustración exacta del diagnóstico del pase 6: **el problema de LATAM no es que no haya quien construya, es que nadie sostiene el proyecto después del primer release** — un finalista de hackathon regional, abandonado a los dos meses.
- **Ciencias sociales (sub-gap del gap 1): no se cierra, y ahora se sabe qué hay al lado.** Ver `repos/trending.md` de este pase: `ProHist-Bench` existe, es Apache-2.0, y **mide investigación histórica, no enseñanza de la historia**. Son cosas distintas y el sub-gap pedagógico sigue abierto.

### Dos benchmarks de seguridad más, los dos sin repo

La categoría que el pase 5 abrió (seguridad pedagógica, trend 12) sigue produciendo, y sigue produciendo papers sin código:

- **EduZone** (arXiv 2608.02024, 2026-08-03) — framework de seguridad LLM para K-12 que cubre **alumno y docente**, con **6 categorías de riesgo y 28 subcategorías** entre daños convencionales y específicos de educación, y un dataset liberado de **2.600 prompts adversarios single-turn + 2.600 multi-turn estáticos**. Autores de **KAIST** (Junyeong Park, Jieun Han, Haneul Yoo, So-Yeon Ahn, Jinsung Yoon, Alice Oh) → **APAC**. El hallazgo reportado: mayor vulnerabilidad en los riesgos *específicos de educación* y en multi-turn dinámico, y **los guardrails existentes no los cubren**.
- **AIriskEval-edu** (arXiv 2607.01934) — dataset de evaluación de riesgo en explicaciones educativas mediadas por AI, K-12.

🔴 **Los dos están sin verificar de primera mano: `arxiv.org` sigue bloqueado por el proxy de egreso en este pase** (se reintentó). Tamaños, autorías y hallazgos vienen de resultados de búsqueda. **No usar sus cifras en un entregable sin abrir el paper.**

**Por qué igual se anotan:** EduZone es el primero de esta capa que cubre explícitamente el lado **docente** además del alumno, y el único que mide multi-turn *dinámico*. Si se confirma, refuerza el argumento de **P11** — el gate de seguridad hay que medirlo aparte del modelo docente, y medirlo en conversación, no en prompts aislados.

### Sin movimiento: los dos grandes están planos, y eso ya es una serie

Re-verificados de primera mano en este pase, y conviene leer la serie completa porque es la tercera medición consecutiva:

| Repo | Pase 5 | Pase 6 | **Pase 7** | Estado |
|---|---|---|---|---|
| DeepTutor (Apache-2.0) | 40.6k ★ | 40.6k ★ | **40.582 ★** (v1.6.12, push 2026-09-27) | Plano, pero con releases semanales |
| OpenMAIC (MIT) | 39.7k ★ | 39.7k ★ | **39.7k ★** (652 commits, v1.1.2 del 2026-09-28) | Plano. La v1.1.2 es **de seguridad**: cierra validación en conexiones de provider y descarga de media |

**Dos cosas valen de esto.** Primero: las cifras de la KB para los dos grandes están **confirmadas por tercera vez**, así que se pueden usar sin la advertencia que arrastran los números de los ciclos 1–3. Segundo: que OpenMAIC dedique una release a cerrar validación de providers y descargas es la señal de madurez que importa en una due diligence —**el proyecto ya tiene superficie de ataque y la está tratando**— y es un argumento a favor que no estaba escrito.

## 2026-10-01 (pase 6) — el agente por fin tiene dónde escribir: aparece la capa de telemetría, y su puente MCP

Sexta corrida del día. El pase 5 cerró con el gap 5 reformulado así: **"cinco lo intentaron y ninguno conectó la librería buena"** — cinco servidores MCP de mastery, todos con heurística propia, ninguno sobre `pyKT` o `pyBKT`. Este pase encuentra que el problema estaba mal partido.

Los cinco servidores MCP del pase 5 no fallaron sólo por no usar una librería de knowledge tracing. Fallaron porque **cada uno inventó también su propio almacén de eventos de aprendizaje**. Y ese almacén no hay que inventarlo: es un estándar IEEE con implementaciones maduras que esta KB no tenía registradas en ninguna de las cinco pasadas anteriores.

### La capa que faltaba: Learning Record Store (xAPI)

Un **LRS** es la base de datos de eventos de aprendizaje: cada "el alumno intentó X y le salió Y" se guarda como un *statement* xAPI. Es el sustrato que consume cualquier modelo de knowledge tracing. La KB tenía plataformas, agentes, modelado, medición, modelos fundacionales, SIS y autograding — y **ningún lugar donde el agente deje registro de lo que observó**.

| Repo | Licencia | Stars | Commits | Lenguaje | Qué es |
|---|---|---|---|---|---|
| **Learning Locker** — https://github.com/LearningLocker/learninglocker | **GPL-3.0** ⚠️ | 583 | 3.254 | JavaScript | El LRS open source canónico, desde 2014. Mantenido por Learning Pool. El más adoptado de la categoría — y el único copyleft de los cuatro |
| **ADL_LRS** — https://github.com/adlnet/ADL_LRS | **Apache-2.0** ✅ | 331 | 1.885 | Python | La implementación de referencia de **ADL** (Advanced Distributed Learning, EE. UU.), que es quien define el estándar. Soporta **IEEE 9274.1.1 (xAPI 2.0)** |
| **SQL LRS (`lrsql`)** — https://github.com/yetanalytics/lrsql | **Apache-2.0** ✅ | 143 | 2.268 | Clojure | LRS sobre SQL corriente: SQLite, **PostgreSQL 14–18**, MariaDB, MySQL 8–9.5. Copyright © 2021–**2026** de Yet Analytics: es el permisivo más vivo de la capa |
| **Ralph** — https://github.com/openfun/ralph | **MIT** ✅ | 50 | 714 | Python | LRS + CLI de pipelines + librería, con conversión nativa de **tracking logs de Open edX** a xAPI. FastAPI, Elasticsearch, Docker/K8s |

⚠️ **La condición que hay que leer antes de proponer ADL_LRS.** El propio repo advierte que *"This version is stable, but only intended to support a small amount of users as a proof of concept"*. Es la implementación **de referencia del estándar**, no un producto de producción. Sirve para validar conformidad, no para aguantar un distrito. Para producción permisiva el candidato es **`lrsql`**; para integración con Open edX, **Ralph**.

### Y el puente que conecta la capa nueva con los agentes

| Repo | Licencia | Stars | Commits | Qué hace |
|---|---|---|---|---|
| **learnmcp-xapi** — https://github.com/DavidLMS/learnmcp-xapi | **MIT** ✅ | 15 | 32 | Servidor **MCP** que le da a un agente tres tools sobre un LRS xAPI: **registrar** un statement, **consultar** el historial de progreso y **gestionar el vocabulario** de verbos/actividades. Backends soportados: **`lrsql`**, **Ralph**, Veracity Learning, y arquitectura de plugins para otros |

El detalle de diseño que lo hace interesante para un tutor: captura el aprendizaje de **dos** maneras — explícita (*"practiqué bucles en Python"*) o **inferida de la conversación**, detectando conocimiento demostrado o vacíos, y después consulta ese historial para adaptar la respuesta siguiente.

**Y el dato de procedencia importa:** el autor declara pertenecer al **IES Rafael Alberti** — un instituto público español de secundaria. Es decir, el puente entre agentes y el estándar de telemetría educativa lo escribió **un docente en ejercicio**, no un laboratorio. Región: **EMEA (España)**.

### Cómo cambia el gap 5, con precisión

El gap 5 decía que el hueco exacto era **`pyKT` detrás de MCP**. Sigue sin existir — verificado otra vez en este pase. Pero el trabajo que implica es **más chico de lo que la KB venía estimando**, porque dos de las tres piezas ya están resueltas y con licencia permisiva:

| Pieza | Estado antes del pase 6 | Estado real |
|---|---|---|
| Almacén de eventos de aprendizaje | "cada servidor MCP se lo inventa" | **Resuelto.** `lrsql` (Apache-2.0) o Ralph (MIT), sobre un estándar IEEE |
| Transporte MCP hacia ese almacén | "no registrado" | **Resuelto.** `learnmcp-xapi` (MIT), que ya habla con los dos anteriores |
| Modelo de knowledge tracing entrenable detrás | "no existe" | **Sigue sin existir.** `learnmcp-xapi` registra y recupera; **no infiere mastery** |

**La formulación correcta del hueco, sexta versión:** no es "construir un servidor MCP de mastery" (eso lo hicieron cinco veces) ni "construir el almacén" (es un estándar con cuatro implementaciones). Es **enchufar `pyBKT` o `pyKT` como estimador detrás de un LRS que ya existe, exponiéndolo por un MCP que ya existe**. Eso es un componente, no una plataforma. Ver el patrón nuevo **P15**.

### L2-Bench — el sub-gap de "benchmark pedagógico fuera de matemática" se cierra en lengua, con una advertencia de verificación

El pase 5 dejó el sub-gap así: *"benchmark pedagógico específico de **lengua**, ciencias sociales o formación profesional"*. Para **lengua** aparece un artefacto, y no es académico de nicho:

**L2-Bench** — *An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education* (arXiv 2607.08842), de **Oxford University Press** con la Universidad de Oxford. Según las fuentes localizadas: **1.000+ tareas docentes auténticas**, un marco de **12 competencias docentes con 31 sub-habilidades**, rúbricas con descriptores expertos, y validación de **200+ educadores de 45+ países**. Licencia declarada: **dataset y rúbricas CC BY-SA 4.0 ⚠️, código de evaluación MIT ✅**. Hay un paper metodológico compañero (arXiv 2603.20088).

🔴 **Advertencia de verificación, y es importante:** a diferencia de todo lo demás en este pase, **L2-Bench no se pudo verificar de primera mano**. El proxy de egreso de esta sesión bloquea `arxiv.org`, `huggingface.co` y `oup.com` — los tres lugares donde vive. Todo lo anterior viene de resultados de búsqueda, no de leer el dataset ni el archivo de licencia. **Antes de usarlo en un entregable hay que abrirlo y confirmar licencia y contenido.** Se registra porque un benchmark de segunda lengua de OUP con 200+ validadores es exactamente lo que el gap pedía, y omitirlo sería peor; pero se registra marcado.

Si se confirma, refuerza el gap 3 una vez más: **EMEA vuelve a producir la medición, no el tutor.** Cuatro de los artefactos de evaluación de esta KB son ya europeos o de MBZUAI.

### Lo que se buscó y no está — formación profesional sigue siendo un desierto, ahora con números

El otro tercio del sub-gap del pase 5 es **formación profesional**, y acá no hay hallazgo: hay una medición del vacío. Búsqueda directa en GitHub por `vocational education AI`: **24 repos en total**, el más grande con **2 estrellas**. Casi todos son trabajos de curso o portfolios personales. Los dos únicos con forma de producto:

- `edufeedai/edufeedai` (Java, **0 ★**) — feedback automatizado sobre entregas de FP. 9 issues abiertos, sin tracción.
- `straussbastian/ai_flashcards_for_school` (Python, **1 ★**) — flashcards generadas por un agente vía **MCP** para *Berufsschule* alemana; el docente arma el bundle, la clase entra con un link de tres palabras, sin login ni resultados almacenados. Diseño de privacidad interesante, tamaño irrelevante.

**Conclusión, que es un dato y no una ausencia:** la formación profesional —el segmento con más presión de reskilling en las cuatro regiones— **no tiene nada open source con tracción**. 24 repos y 2 estrellas de techo no es un ecosistema incipiente: es un hueco. Para un engagement de FP hay que presupuestar construcción, no integración.

## 2026-09-30 (pase 5) — aparece una categoría entera que la KB no tenía: seguridad pedagógica

Quinta corrida del día. Se volvió a aplicar la lección de método del pase 3 (buscar la *pieza técnica*, no la categoría) y esta vez el resultado no es un repo: es **una categoría de evaluación con cuatro publicaciones en venues top y datasets liberados, que ninguna de las cuatro pasadas anteriores registró**.

El pase 4 cerró diciendo que el estándar pedagógico "existe, está publicado y nadie lo usa", y que **lo que seguía faltando era un benchmark fuera de matemática**. Ese sub-gap se cae en este pase, y se cae por partida doble.

### La categoría nueva: *pedagogical safety* / sycophancy

No se trata de toxicidad ni de jailbreak genérico. Se trata de una falla propia de la educación: **el tutor que enseña mal siendo amable**. Revelar la respuesta antes de tiempo, reforzar la idea equivocada del alumno porque el alumno insistió, abandonar el andamiaje. Es medible, y desde 2026 hay con qué medirlo.

| Artefacto | Repo / fuente | Licencia | Stars | Qué mide | Alcance |
|---|---|---|---|---|---|
| **SafeTutors** | https://github.com/RadiantCrystal/SafeTutors | MIT ✅ | 0 | Taxonomía de **11 dimensiones de daño y 48 sub-riesgos** derivadas de literatura de ciencias del aprendizaje. **5.955 instancias** (3.135 escenarios single-turn + 2.820 diálogos multi-turn). 11 modelos evaluados (10 open-weight, 1 cerrado), de 3.8B a 72B | Matemática, física, **química** |
| **EduGuardBench** | https://github.com/YL1N/EduGuardBench | ⚠️ **sin licencia declarada** | 4 | Daño docente vía preguntas *Select All That Apply* + set de prompts adversarios con jailbreak basado en personas, enfocado en **mala conducta académica**. 14 modelos | Simulación de docente, transversal a materia |
| **EduBench** | https://github.com/ybai-nlp/EduBench | MIT ✅ | 29 | **9 contextos educativos** y 4.000+ situaciones sobre **12 dimensiones** en 3 categorías (adaptabilidad al escenario, exactitud factual/razonamiento, aplicación pedagógica). Cubre 5 escenarios de alumno y **4 de docente, entre ellos Automatic Grading** | Transversal — **no es de matemática** |
| **EduFrameTrap** | arXiv 2605.14604 (2026-05-14) — no se localizó repo público | n/d | — | Sycophancy bajo presión social: subtipos **CS-SYC** (cambio de marco), **AUTH-SYC** (deferencia ante autoridad), **FACE-SYC** (salvar la cara), **DIR-SYC** (endoso directo). Formula la *Reasoning-Sycophancy Paradox*: un modelo que resiste el ataque de marco igual capitula ante presión de autoridad | Matemática, física, **economía, química, biología, ciencias de la computación** |
| **ELBench** | arXiv 2608.09548 (ago 2026) — no se localizó repo público | n/d | — | 4 módulos bajo un protocolo común: General Capability, Safety & Trustworthiness, Basic Education, High-Level Cultivation. 9 modelos | Transversal |

### El sub-gap "no hay benchmark fuera de matemática" se cae

El pase 4 lo dejó escrito: *"Lo que sigue sin existir: un benchmark pedagógico fuera de matemática. Los tres son de matemática (…). Para lengua, ciencias sociales o formación profesional no hay nada."*

Corrección:

- **EduBench (MIT, ACL 2026)** es explícitamente **transversal a materia** y organiza la evaluación por *escenario educativo*, no por dominio. Incluye cuatro escenarios docentes, uno de ellos corrección automática.
- **EduFrameTrap** cubre **seis materias**, entre ellas economía y biología.
- **EduGuardBench** evalúa al modelo *como docente simulado*, lo que es independiente de la materia.

Lo que **sí se mantiene** del gap: no hay benchmark pedagógico para **lengua, ciencias sociales ni formación profesional** específicamente. Ninguno de los cinco los cubre. Pero la afirmación "todo es matemática" dejó de ser cierta, y `EduBench` es MIT, lo que lo vuelve el primer artefacto de evaluación pedagógica de esta KB **sin fricción de licencia** — los dos que el pase 4 celebró (MathTutorBench CC BY, UnifyingAITutorEvaluation CC BY-SA) sí la tienen.

### El hallazgo más vendible: la seguridad está *anti-correlacionada* con la enseñanza práctica

De ELBench, y es el dato que conviene llevar a una conversación de cliente regulado: **entre los modelos evaluados, el módulo de safety está anti-correlacionado con el de enseñanza práctica.** Los modelos más seguros enseñan peor y los que mejor enseñan son menos seguros.

Si se sostiene, tiene una consecuencia directa de arquitectura: **no existe el modelo que resuelva las dos cosas eligiéndolo bien.** Hay que componer — modelo docente + gate de seguridad medido aparte — que es exactamente lo que el patrón nuevo **P11** propone. Es también el mejor argumento contra la pregunta "¿y por qué no usamos el modelo más grande y listo?".

EduGuardBench aporta el matiz opuesto y también sirve: identificó un *Educational Transformation Effect* — los modelos más seguros no se limitan a rechazar el pedido dañino, lo **convierten en momento de enseñanza** (*Educational Refusal*). Y que el modo de falla dominante no sea la toxicidad sino la **incompetencia** confirma que el riesgo real en educación es pedagógico, no reputacional.

### Teacher-facing: el gap 8 se corrige — no es un solo repo de 59 estrellas

El pase 3 declaró que toda la capa docente es propietaria "con una sola excepción open source", Claw-ED (MIT, 59 ★). **Es incorrecto y se corrige:** hay un asistente de planificación docente **MIT, en producción, con 1.188 commits y respaldo institucional público**.

| Repo | Licencia | Stars | Commits | Qué es |
|---|---|---|---|---|
| **Aila** — https://github.com/oaknational/oak-ai-lesson-assistant | MIT ✅ | 35 | **1.188** | *AI Lesson Planning Assistant* de **Oak National Academy** (Reino Unido, nonprofit educativa respaldada por el gobierno británico). Monorepo Turborepo: Next.js + Prisma/PostgreSQL con **pgvector**. Entornos de producción y staging, versionado semántico, estrategia de ramas |
| **ai-lesson-planner** — https://github.com/saniales/ai-lesson-planner | GPL-3.0 ⚠️ | 20 | 2 | Toolkit chat-first con workflow multi-agente (course-planner → discussion-moderator → lesson-planner → slides-maker) y salida a slides **MARP** |

⚠️ **La condición de Aila hay que leerla antes de proponerlo.** El propio repo aclara que *"this project is intended primarily for internal use by Oak National Academy"*. Es **código abierto de un producto en producción, no un producto empaquetado para terceros**: no hay compromiso de API estable, ni de soporte, ni de que el monorepo se pueda desplegar fuera del contexto de Oak. La lectura correcta es **"la mejor referencia de arquitectura teacher-facing que existe en abierto, con licencia que permite copiar piezas"**, no "la base sobre la que montamos el producto del cliente". Con 1.188 commits de un equipo real resolviendo el problema en producción, como referencia vale más que los otros dos juntos.

**Lo que no cambia:** el segmento sigue dominado por propietarios (MagicSchool, Brisk, Diffit, Curipod, Eduaide.AI, SchoolAI). Lo que cambia es que ya no es cierto que en abierto sólo haya un repo de autor individual.

### Knowledge tracing detrás de MCP: existe cinco veces, y ninguna sirve todavía

El pase 4 cerró el gap 5 con una formulación muy precisa: *"El hueco exacto es `pyKT` detrás de MCP, y no existe."* **La primera mitad se confirma; la segunda hay que matizarla de una forma que es más interesante que si fuera falsa.**

Buscando por la pieza técnica aparecen **cinco servidores MCP independientes** que exponen mastery/knowledge tracing a un agente:

| Repo | Licencia | Stars | Commits | Qué implementa |
|---|---|---|---|---|
| https://github.com/zcsabbagh/knowledge-graph-mcp | MIT ✅ | 1 | 8 | FastMCP + SQLite. Grafo de conceptos con prerequisitos, **SM-2** para repaso y mastery multidimensional con fórmula fija: `0.3×recall + 0.4×application + 0.3×explanation`. Detección de misconceptions |
| https://github.com/woodstocksoftware/student-progress-tracker | MIT ✅ | 1 | 9 | Perfiles, inscripciones, resultados de evaluación, cálculo de mastery por tema, detección de learning gaps y recomendación de foco. Telemetría a nivel de pregunta |
| https://github.com/tejpalvirk/student | MIT ✅ | 1 | 6 | Grafo de conocimiento académico (cursos, trabajos, exámenes, conceptos) con persistencia entre sesiones |
| https://github.com/znecho9/knowledge-forest-mcp | Apache-2.0 ✅ | 0 | 3 | Árboles de prerequisitos + **mastery con evidencia obligatoria**: exige desempeño novedoso, sin asistencia y a libro cerrado antes de declarar dominio |
| https://github.com/radhepa/Teacher-MCP | MIT ✅ | 0 | 2 | MCP-first con memoria persistente SQLite, personas docentes y andamiaje en tres niveles. Trae además un Claude Skill que funciona solo o contra el server |

**La lectura correcta, que es una señal de mercado y no un hallazgo técnico:** cinco autores sin relación entre sí llegaron a la misma idea en la misma ventana. El patrón *"el agente consulta el estado de mastery antes de decidir qué preguntar"* **se está reinventando en paralelo**, lo cual valida que el problema es real y sentido por muchos.

**Y el hueco de ingeniería sigue intacto, ahora con mejor evidencia.** Ninguno de los cinco usa una librería de knowledge tracing entrenable: todos **implementan su propia heurística** (SM-2, fórmulas de pesos fijos, reglas de evidencia). Los tres con más tracción suman **3 estrellas y 23 commits**. Verificado de primera mano en este pase: **`pyKT` sigue en 441 ★ / 811 commits y su documentación no menciona MCP ni interfaz de serving.**

Dicho de otro modo: el gap 5 pasa de *"nadie lo intentó"* a **"cinco lo intentaron y ninguno conectó la librería buena"**. Es una propuesta mejor, no peor: el trabajo dejó de ser inventar el patrón (ya está validado cinco veces) y pasó a ser **hacerlo bien una vez** — ver **P12**.

### La pieza que faltaba para hacerlo bien, y es de North America

| Repo | Licencia | Stars | Commits | Por qué importa |
|---|---|---|---|---|
| **pyBKT** — https://github.com/CAHLR/pyBKT | MIT ✅ | **281** | 379 | Bayesian Knowledge Tracing y variantes en Python: estima mastery cognitivo desde secuencias de resolución, con parámetros individualizados por alumno y tasas de aprendizaje por ítem. Publicado en **EDM 2021** (Badrinath, Wang & Pardos) |

Viene de **CAHLR (UC Berkeley)**, **el mismo laboratorio de Zachary Pardos que produjo OATutor**, que esta KB ya tenía listado sin haber mirado el resto del laboratorio.

**Por qué cambia la propuesta y no sólo el inventario:** el gap 4 de esta KB dice que la oferta está concentrada en APAC, y el pase 4 agravó el diagnóstico al descubrir que también la capa de modelado era china (pyKT, Jinan University). **pyBKT es MIT, tiene 281 estrellas, está publicado y es de una universidad estadounidense.** Para un cliente con restricciones de procedencia de software —el riesgo que el gap 4 manda declarar temprano— ahora hay una alternativa en la capa de modelado que no obliga a elegir entre cumplir la restricción y tener knowledge tracing.

El trade-off técnico hay que decirlo igual: pyBKT es **BKT bayesiano clásico**, pyKT es **deep learning (10+ modelos DLKT)**. pyKT es más potente y pyBKT es más interpretable y mucho más fácil de defender ante un regulador que pregunta por qué el sistema decidió lo que decidió. Para un primer engagement regulado, la interpretabilidad suele ganar.

### Correcciones de esta corrida

1. **`SirhanMacx/eduagent` no es un repo nuevo: redirige a `SirhanMacx/Claw-ED`.** Aparece en búsquedas como "EduAgent, CLI agent con 48+ tools" y parece un segundo proyecto del mismo autor. Es el mismo repo renombrado. Verificado: la URL `/SirhanMacx/eduagent` resuelve a `SirhanMacx/Claw-ED`. **No agregarlo como entidad separada** — se deja anotado acá justamente para que una pasada futura no lo duplique.
2. **Claw-ED sigue en 59 ★ pero creció en código:** **778 commits**, release **v9.18.2026.1**. Soporta Anthropic, OpenAI, Gemini, Ollama y OpenRouter. Las estrellas están planas y el desarrollo no: es un proyecto activo con poca visibilidad, no uno abandonado.
3. **`GeminiLight/awesome-ai-llm4education` (220 ★, catálogo de 334 papers 2001–2026) NO TIENE ARCHIVO LICENSE.** Verificado: `/blob/main/LICENSE` devuelve 404. Es un índice bibliográfico excelente para orientarse, y **no es reutilizable en un entregable** — sin licencia, el default legal es "todos los derechos reservados". Usarlo para leer, no para copiar.

### Lo que esta pasada buscó y no encontró

- **Repo público de EduFrameTrap y de ELBench.** Los dos papers describen benchmarks con rúbricas y subtipos concretos; no se localizó código ni dataset publicado para ninguno de los dos. Son las dos únicas filas de la tabla de arriba sin artefacto verificable.
- **Agente educativo de origen LATAM con tracción.** Se volvió a buscar en español y portugués. Nada nuevo por encima de lo del pase 4 (TutorIA, MIT, 0 ★). **El gap 2 se mantiene sin cambios.**
- **Benchmark pedagógico de lengua, ciencias sociales o formación profesional.** Sigue sin existir, ver arriba.

### Nota de método — el proxy de egreso bloquea la mayoría de las fuentes académicas

Dato operativo para las próximas pasadas, porque cambia qué se puede afirmar como verificado:

- **`curl -sI` contra github.com devuelve 403** a través del proxy. Confirma lo que anotó el pase 4: **no sirve para verificar URLs en este entorno**. El método que funciona es WebFetch contra la página del repo.
- **Bloqueados por el proxy de egreso:** `arxiv.org`, `openreview.net`, `aclanthology.org`, `huggingface.co`, `ojs.aaai.org`, `mcml.ai`, `unu.edu`, `coe.int`, `digitaleducationcouncil.com`, `mcpservers.org`.
- **Consecuencia que hay que respetar al leer este pase:** todo lo de **github.com está verificado de primera mano** (licencia, stars, commits leídos de la página del repo). Todo lo que sale de **papers, datasets de HuggingFace y cifras de mercado está tomado de resúmenes de búsqueda y NO pudo verificarse contra la fuente primaria** — incluidos los conteos de ítems de SafeTutors, los subtipos de EduFrameTrap, el hallazgo de anti-correlación de ELBench y el venue de cada publicación. Están registrados porque son útiles y consistentes entre fuentes independientes, no porque se hayan visto en el original. **No citarlos en material de cliente sin abrir el paper.**

## 2026-09-30 (pase 4) — la capa de evaluación y de knowledge tracing existía; la KB la estaba buscando mal

Cuarta corrida del día. No se buscaron "agentes educativos": las tres pasadas anteriores ya agotaron esa consulta. Se aplicó la **lección de método que el propio pase 3 dejó escrita** — cuando un gap dice "no existe X", re-buscar por la *pieza técnica* y no por la categoría. Resultado: **dos gaps declarados se caen y un tercero se refina**, y el mayor hallazgo tiene 441 estrellas y llevaba cuatro años publicado.

### Nuevos agentes y piezas verificadas

Todo verificado vía WebFetch contra la página del repo.

| Repo | URL | Licencia | Stars | Lenguaje | Qué es | Región |
|------|-----|----------|-------|----------|--------|--------|
| **pyKT** | https://github.com/pykt-team/pykt-toolkit | MIT ✅ | **441** | Python | Librería de **knowledge tracing** sobre PyTorch: 10+ modelos DLKT, 7+ datasets, preprocesamiento estandarizado. 811 commits | APAC (Jinan University, China) |
| **FreeLingo** | https://github.com/artcc/freelingo | **AGPL-3.0** ⚠️ | 150 | Python | Duolingo self-hosted: nivel CEFR evaluado por LLM local (Ollama), plan de estudio, tutor por voz, flashcards, repetición espaciada | Sin verificar |
| **MathTutorBench** | https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | 42 | Python | Benchmark de capacidad **pedagógica** de tutores LLM: 3 habilidades docentes, 7 tareas, reward models y leaderboard. EMNLP 2025 Oral | EMEA (org `eth-lre`) |
| **UnifyingAITutorEvaluation** | https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | 32 | — | Taxonomía de 8 dimensiones pedagógicas + **MRBench** V1/V2/V3. NAACL 2025, Senior Area Chair Award | EMEA (MBZUAI) |
| **TutorIA** | https://github.com/LabSirius/TutorIA | MIT ✅ | **0** | Python | Tutor autónomo dentro de Open edX para **educación superior rural**, con TTS, avatar y dashboard docente | **LATAM (Pereira, Colombia)** |
| **OpenDidactia** | https://github.com/nmarafo/OpenDidactia | CC BY-SA 4.0 ⚠️ | 0 | Markdown | Esquemas curriculares OKF para generar Programaciones Didácticas **LOMLOE** con agentes. 17 comunidades autónomas | EMEA (España) |
| **mentar** | https://github.com/avps82/mentar | **AGPL-3.0** ⚠️ | 1 | Python | Tutor local-first para chicos, 934 nodos de concepto en 157 plantillas (AU/IN/SG/US). El LLM explica, un checker determinístico corrige | Sin verificar |

### Lo que se cae: el gap "no hay evaluador pedagógico open source"

El gap 1 decía que el único evaluador era `AITutor-EvalKit` con **3 estrellas** y que "no existe el LegalBench de educación". Las dos mitades estaban mal medidas:

- **`UnifyingAITutorEvaluation` (32 ★) es del mismo autor y es el repo canónico.** La KB había registrado el repo chico — la implementación LoMTL sobre 4 dimensiones — y no el grande, que publica la taxonomía de 8 dimensiones y las tres versiones de MRBench. Premio de Senior Area Chair en NAACL 2025.
- **`MathTutorBench` (42 ★, EMNLP 2025 Oral) no estaba en la KB en absoluto.** Tiene reward models entrenados y leaderboard público.

El gap no desaparece del todo — 42 y 32 estrellas siguen siendo poca tracción — pero pasa de "no existe" a "**existe, está publicado en EMNLP y NAACL, y nadie lo está usando en producción**". Es una afirmación muy distinta frente a un cliente que tiene que demostrar calidad pedagógica bajo EU AI Act.

### Lo que se cae: LATAM deja de ser fase cero *institucional*

El gap 2 decía que LATAM produce agentes pero "ninguno sale de la fase cero", con ejemplos de 0 y 2 estrellas y uno sin licencia. **TutorIA** sigue teniendo 0 estrellas — pero es cualitativamente otra cosa:

- Tiene **licencia MIT** (el problema del gap 2 era justamente que los proyectos LATAM no la ponían).
- Tiene **respaldo institucional verificado**: Grupo Sirius, Universidad Tecnológica de Pereira (`sirius.utp.edu.co`, perfil de la organización declara Pereira, Colombia).
- Tiene **un caso de uso específico y no genérico**: educación superior **rural** en Risaralda, integrado dentro de Open edX, con TTS y avatar porque el contexto lo pide.

Que un laboratorio universitario colombiano publique MIT e integre contra Open edX es exactamente el tipo de contraparte que un engagement LATAM necesita. **Las estrellas no son la métrica acá; la gobernanza del proyecto sí, y esta vez está.**

### Lo que se refina: EMEA sí produce artefactos agénticos, pero son *benchmarks y esquemas*, no tutores

El gap 3 decía que "EMEA no produce agentes, produce plataformas". Con lo de este pase, la formulación correcta es más útil: **EMEA produce la capa de evaluación y de conformidad.** MathTutorBench (Suiza), UnifyingAITutorEvaluation y AITutor-EvalKit (Abu Dhabi), OpenDidactia (España), education-agent-skills (UK), y ahora **OpenTutorAI-CE confirmado en Marruecos**. Ninguno es un tutor de producto; todos son *cómo se mide o cómo se acredita* un tutor. Encaja con que EMEA es donde la regulación muerde.

### Dos regiones cerradas en agentes que ya estaban en la KB

- **OpenTutorAI-CE → EMEA (Marruecos).** El perfil de la organización `Open-TutorAi` declara `Morocco` y `opentutorai.com`. Explica el soporte multilingüe árabe/francés/inglés que la KB ya había registrado sin conectarlo.
- **Claw-ED → North America (Nueva York, EE. UU.)**, con la confianza declarada: el perfil **no** publica ubicación, pero los repos hermanos del mismo autor son un portal del *NYS Seal of Civic Readiness* "built for Great Neck Public Schools" y un juego de repaso de **Regents** y AP. Se registra como inferido de artefactos, no como declarado.

Quedan tres sin cerrar tras buscarlo explícitamente: **Bloom**, **OpenTutor** y **tutor-mcp** no declaran ubicación en el perfil ni en el repo, y no hay artefacto que lo evidencie. Se deja como gap, no como silencio.

### Sin movimiento: los dos grandes están planos

**DeepTutor 40.6k ★ y OpenMAIC 39.7k ★ — exactamente los mismos números que el pase 3**, horas antes. Es lo esperable dentro del mismo día y se registra para que la serie no tenga un hueco: la ventana de esta corrida no midió crecimiento, midió cobertura. DeepTutor sigue en v1.6.12 (2026-09-27) y OpenMAIC en v1.1.2 (2026-09-28).

### Corrección de licencia que vale registrar

**FreeLingo se publica como MIT en prensa y agregadores; la página del repo dice AGPL-3.0.** Se tomó la del repo. Es el modo de falla que esta KB ya se impuso evitar: la licencia se lee en el repo, no en el listicle.

---

## 2026-09-30 (pase 3) — teacher-facing y grading: dos categorías que se abrieron

Tercera corrida del día. Objetivo declarado: buscar agentes net-new en las capas que las dos pasadas anteriores habían marcado como vacías. Se encontraron dos, y una de ellas mueve un gap. Todo verificado vía WebFetch contra la página del repo.

### Nuevos agentes verificados

| Agente | Repo | Licencia | Stars (2026-09-30) | Lenguaje | Qué es |
|--------|------|----------|--------------------|----------|--------|
| **Claw-ED** | https://github.com/SirhanMacx/Claw-ED | MIT | **59** | Python | Agente CLI **local-first para docentes**. Se apunta a una carpeta de lecciones viejas, infiere el estilo de enseñanza del docente y emite el bundle completo: plan, handouts, versiones diferenciadas, juegos, evaluaciones, como DOCX de docente + DOCX de alumno + PPTX de slides en una corrida. 48+ tools, alineación a estándares estatales, cualquier provider LLM, bot de Telegram con la misma memoria. v9.18.2026.1 (Beta), 778 commits. `pip install clawed` |
| **AI-Teaching-Agent** | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT | **0** | Python | Markdown → artefactos **Lab / Exam / Grading como DSL validado**, más slides opcionales. Human review obligatorio, evaluación sandboxeada, servidor **MCP stdio** con adaptadores de tools, previews de examen *candidate-safe* que excluyen respuestas y referencias internas de corrección. 30 commits |

### Por qué Claw-ED importa más que sus 59 estrellas

**Es el primer agente teacher-facing open source de esta KB, y llega a la capa donde el mercado cerrado no tiene competencia.** `intel/market.md` ya venía diciendo que las herramientas *para docentes* son "el ángulo menos disputado" y que MagicSchool lidera ahí con poco foso. Esta pasada buscó el equivalente abierto y confirmó que **el segmento entero es propietario**: MagicSchool, Brisk, Diffit, Curipod, Eduaide.AI, SchoolAI, Taskade. Claw-ED es la única entrada open source que apareció.

Tres cosas lo vuelven propuesta y no curiosidad:

1. **Ataca el rechazo docente en su causa real.** La objeción no es "la AI genera material malo", es "genera material que no suena a mí". Un agente cuyo insumo son *las lecciones anteriores del propio docente* invierte esa objeción en un argumento de venta.
2. **Local-first, y eso resuelve dos problemas de una.** El corpus histórico del docente —su propiedad intelectual— no sale de la máquina. Sirve igual para el pudor profesional y para residencia de datos en EMEA.
3. **No toca al alumno.** Produce borradores que un docente aprueba. Queda fuera del alcance de las restricciones de decisión automatizada de Oklahoma, Maryland, el Annex III europeo y la AI Basic Act coreana. **Es el patrón con menos superficie regulatoria de toda la KB** — ver **P8** en `compose/patterns.md`.

⚠️ **59 ★ y un solo autor.** Verificar continuidad antes de un contrato largo y presupuestar el costo de mantenerlo forkeado.

### AI-Teaching-Agent: 0 estrellas, pero es la primera señal en la categoría de grading

El gap 6 (pase 2) concluyó que no existe grading open source con tracción y que el camino realista es **orquestar al incumbente propietario** vía `gradescope-mcp`. **Eso no cambia.** Lo que cambia es que apareció el primer intento de la estrategia opuesta: en vez de llamar a un grader externo, **generar el artefacto de corrección como DSL auditable**, con revisión humana en el medio y preview de examen sin respuestas.

El diseño es exactamente el que piden el EU AI Act y los estatutos de EE. UU. que prohíben grading automático. Pero **0 estrellas y 30 commits es un proyecto de una persona**: se registra, no se usa. Re-verificar el próximo ciclo. Si en tres meses sigue en 0, es un experimento abandonado; si pasa a 200, es la semilla de la categoría.

### Corrección de procedencia — OpenMAIC fue AGPL-3.0 hasta hace tres meses

La KB registra OpenMAIC como MIT, y lo es. Lo que faltaba: **fue relicenciado de AGPL-3.0 a MIT en v0.3.0, el 2026-06-28.** La licencia permisiva tiene ~3 meses, no la vida del proyecto.

No cambia la recomendación —MIT es MIT— pero sí lo que hay que decir en una due diligence: si el cliente audita procedencia de software, **declarar que el historial previo a junio de 2026 es AGPL-3.0**. Combinado con el gap 4 (concentración de la oferta en instituciones chinas: OpenMAIC es de Tsinghua), es el tipo de dato que conviene poner sobre la mesa temprano y no descubrir en revisión legal.

Releases recientes, para contexto de madurez: v1.1.0 trajo chat de aula sobre un agent loop con referencias a elementos de slide y pizarra durante playback; **v1.1.1 y v1.1.2 son los dos de seguridad** — política de direcciones públicas en uploads a MinerU Cloud, validación de redirects, y validación de base URLs provistas por el caller en parsing de PDF y rutas de provider para prevenir SSRF. Un proyecto que endurece contra SSRF está recibiendo reportes de seguridad reales.

### Lo que esta pasada buscó y no encontró

- **Agente educativo net-new con tracción alta (>1k ★).** No apareció ninguno que la KB no tuviera ya. Los tres líderes siguen siendo DeepTutor, OpenMAIC y NOMAD, y el resto del campo está por debajo de 1k. La distribución del sector es extremadamente bimodal: tres repos de ~40k y una cola larga de menos de 1k, sin nada en el medio.
- **Agente de origen LATAM con tracción.** Sin cambios respecto del pase 2: el gap 2 sigue abierto.
- **DeepTutor v1.6.12 sigue siendo la última release** (2026-09-27), con 40.6k ★ sin cambio medible en la ventana. Agrega Kiwix, reubicación de knowledge base del workspace, render de figuras de fuente, Task Board de progreso, interfaz en alemán y recuperación de chat.

## 2026-09-30 (pase 2) — segunda pasada de verificación

Segunda corrida del día. Objetivo: resolver las pistas que la pasada anterior dejó abiertas y buscar agentes net-new. Todo verificado vía WebFetch contra la página del repo (`curl` a github.com devuelve 403 a través del proxy de esta sesión, incluso para repos que existen — no sirve como verificador).

### Nuevo agente verificado

| Agente | Repo | Licencia | Stars (2026-09-30) | Qué es |
|--------|------|----------|--------------------|--------|
| Bloom | https://github.com/Li-Evan/Bloom | MIT | 278 | Tutor personal que genera un syllabus estructurado, entrega una lección a la vez, lee las anotaciones y el feedback del alumno y ajusta la siguiente lección al nivel real de comprensión. Dos modos: CLI como **skill de Claude Code** (sin backend) y web self-hosted (React + FastAPI, cualquier LLM OpenAI-compatible). Se apoya explícitamente en el "2 sigma" de Benjamin Bloom |

**Por qué importa más que sus 278 estrellas.** Es el segundo caso en dos pasadas de *pedagogía distribuida como skill de agente* en vez de como producto (el primero fue `education-agent-skills`). El modo CLI no tiene backend: el harness del agente **es** el producto. Para un studio esto baja el costo de un piloto de tutoría de "desplegar una plataforma" a "instalar una skill".

### Corrección de licencia y stars — OpenTutorAI-CE

El ciclo 3 lo registró como `Apache-2.0, ~600 ★`. Verificado hoy: **BSD-3-Clause, 107 ★**. Las dos cosas estaban mal. BSD-3 sigue siendo permisiva, así que el repo es usable; el dato de tracción estaba inflado ~6x.

### Agentes educativos de origen LATAM — el gap se confirma, con mejor evidencia

La pasada anterior declaró que no había agentes educativos open source de origen latinoamericano con tracción medible. Esta pasada buscó explícitamente en español y portugués. **Resultado: sí existen, y todos están pre-tracción.**

| Repo | Origen | Licencia | Stars | Estado |
|------|--------|----------|-------|--------|
| https://github.com/H1bertto/professor-agent | Brasil | MIT | 0 | Tutor local con avatar 2D/3D superpuesto al escritorio, por voz, con provider propio. TypeScript |
| https://github.com/ANTONIOALGMAR/StudyAgent | Brasil | **sin licencia** ⚠️ | 2 | Tutor multimodal 100% local sobre Ollama: voz bidireccional, visión de pantalla/cámara, PDFs, corrección automática, flashcards con repetición espaciada, gamificación |

`studyield/studyield` apareció en los resultados de búsqueda como plataforma self-hosted en 12 idiomas: **la URL da 404.** No es un finding.

**El gap declarado cambia de forma, no de conclusión.** Antes era "no encontramos ninguno". Ahora es más preciso y más útil: **hay iniciativas reales en Brasil, pero ninguna pasa de 2 estrellas y al menos una no tiene licencia** — sin licencia no hay permiso de uso, así que no es reutilizable ni siquiera si el código sirviera. El espacio sigue abierto y ahora sabemos que la demanda de constructores existe: no falta interés, falta masa crítica y gobernanza de proyecto.

### Gap confirmado: no hay agente de grading open source con tracción

Se buscó específicamente grading/assessment automatizado open source con licencia permisiva. La capa de corrección sigue siendo **propietaria**: Gradescope (Turnitin), Codio, Kangaroos AI. Lo que hay en abierto son *papers* (arXiv 2601.00730, 2607.02432, 2506.07955), no repos con adopción.

Esto explica por qué `gradescope-mcp` (8 ★) vale seguirlo pese a su tamaño: **el camino realista hacia grading agéntico hoy es un MCP contra el incumbente propietario, no un reemplazo open source.** Consecuencia para propuestas: no prometer sustituir Gradescope; prometer orquestarlo.

## 2026-09-30 — verificado a mano (WebFetch, repo por repo)

Lo nuevo y lo que se movió en esta ventana:

| Agente | Repo | Licencia | Stars (2026-09-30) | Qué cambió |
|--------|------|----------|--------------------|------------|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 40.6k | v1.6.12 el 2026-09-27. Cadencia de release semanal, 2.386 commits. Pasó de ~20k ★ (abr-2026, 111 días desde el lanzamiento) a 40.6k: duplicó en ~5 meses |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 39.7k | v1.1.2 el 2026-09-28, release de **seguridad** (validación en provider routing y descarga de media). Señal de madurez: ya recibe reportes de seguridad, no sólo features |
| Project NOMAD | https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | 38.8k | ~34.4k ★ en jul-2026 → 38.8k ahora (+4.4k en ~2 meses). Educación offline-first con AI local es una categoría en crecimiento real, no un nicho |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 ⚠️ | 814 | 165 skills pedagógicas consumibles por Claude Code / MCP / Codex / Hermes. Primer caso que vemos de *pedagogía empaquetada como skills de agente* en lugar de como prompt |
| gradescope-mcp | https://github.com/Yuanpeng-Li/gradescope-mcp | MIT | 8 | Nuevo y minúsculo, pero es el primer MCP que vemos sobre un sistema de grading de producción real (Gradescope, 34 tools). Vale seguirlo, no usarlo todavía |

**Los tres líderes (DeepTutor, OpenMAIC, NOMAD) están los tres entre 38k y 41k ★ y ninguno existía con esa masa hace un año.** La tutoría open source dejó de ser terreno académico de bajo star-count.

### Corrección importante de esta corrida

Los star counts de ciclos anteriores estaban inflados por el pipeline, no medidos. Educhain se había registrado con ~12k ★ y tiene **389**; OATutor con ~1.5k y tiene **265**; OpenTutor con ~900 y tiene **127**. Ver la tabla de corrección en `agents/top.md`.

## 2026-07-02 — pipeline automático (histórico, sin verificar)

⚠️ Salida cruda del pipeline. Conservada como historia. Varias filas son repos de 0–2 estrellas y al menos una (`claude-war-room`, `aulalibre`) no es de educación. No usar como recomendación.

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
