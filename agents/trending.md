---
industry: education
region: Global
updated: 2026-10-02
---

# 📈 Agentes trending — education

> **APPEND-ONLY.** Cada corrida agrega una sección fechada arriba y conserva la historia abajo.
> No reescribir secciones anteriores: la serie temporal es el valor de este archivo.

## 2026-10-02 (pase 41) — el pase que **ejecuta las tres acciones del pase 40** y encuentra que **la respuesta comercial que el 40 dejó abierta estaba escrita en un `README.txt` de 174 bytes**: el directorio que hay que subclasear para integrar *proctoring* propio en Open edX **no es AGPL, es Apache-2.0**

**Las tres acciones del pase 40 se ejecutaron y las tres rindieron.** La de mayor valor comercial —la acción 3— se resuelve
con un dato que estaba a un `unzip` de distancia y que **invierte el veredicto del gap 84**. Las otras dos cierran el gap 83,
parten el gap 81 en dos clases y **ponen número a las dos capas que el pase 40 midió vacías de agente.**

### 🟢 El hallazgo que manda: `edx_proctoring/backends/` está *carved-out* en **Apache-2.0** dentro de un repo **AGPL-3.0**

La acción 3 pedía bajar el *wheel* de PyPI y **responder si integrar un *proctoring* propio es implementar una interfaz
existente o escribir la capa desde cero**. La respuesta es **implementar una interfaz** — y la interfaz **no arrastra la AGPL**.

| Medición | Valor |
|---|---|
| Paquete | `edx-proctoring` **5.2.0**, *wheel* `py2.py3-none-any`, **1.315.493 bytes**, 294 entradas |
| Licencia del paquete (nivel superior) | **AGPL-3.0** (`dist-info/LICENSE.txt` → *«GNU AFFERO GENERAL PUBLIC LICENSE Version 3»*) |
| 🟢 **Licencia de `edx_proctoring/backends/`** | 🟢 **Apache-2.0** — `backends/LICENSE.txt`, **11.357 bytes**, contiene *«Apache License / Version 2.0»* y **no contiene la palabra «Affero»** |
| 🟢 La declaración, textual | `backends/README.txt` (**174 bytes**): *«The code in this directory is licensed under a license different from the rest of the edx-proctoring repository. These modules are licensed under Apache 2.0. See LICENSE.txt.»* |
| ✅ Verificado en **dos** canales | En el *wheel* **y** en el árbol (`raw.githubusercontent.com/openedx/edx-proctoring/master/edx_proctoring/backends/{README,LICENSE}.txt` → **200** los dos) |

🔵 **Por qué esto cambia la cotización y no sólo la ficha:** el pase 40 cerró la capa de *proctoring* diciendo *«la única
pieza seria es AGPL-3.0»* y de ahí dedujo que **fuera de Open edX la capa hay que construirla**. **La deducción sigue
siendo correcta para el servidor, y es FALSA para el backend**: el punto de extensión está deliberadamente separado para
que un proveedor escriba su integración **sin tocar la AGPL**. **Es el *upstream* diciendo, en 174 bytes, «escribí tu
backend acá».**

### 🟢 La superficie real de `edx-proctoring`, medida, que es lo que la acción 3 pedía enumerar

| Qué | Cuánto | El dato crudo |
|---|---|---|
| Modelos de estado de examen | **12 clases** (8 entidades + 2 *managers* + 1 *queryset*) | `ProctoredExam`, `ProctoredExamReviewPolicy`(+`History`), `ProctoredExamStudentAttempt`, `ProctoredExamStudentAllowance`(+`History`), `ProctoredExamSoftwareSecureReview`(+`History`), `ProctoredExamSoftwareSecureComment` |
| Rutas REST | **20** | `edx_proctoring/v1/proctored_exam/{exam,attempt,allowance,bulk_allowance,active_exams_for_user,active_attempt,review_policy,settings}`, `v1/user_onboarding/status`, `v1/retire_user/<id>`, `v1/retire_backend_user/<id>`, + 2 *callbacks* (`proctoring_launch_callback/start_exam/<attempt_code>`, `proctoring_review_callback/`) |
| Punto de extensión de proveedor | **`ProctoringBackendProvider`**: **18 métodos + 8 atributos de clase** | `register_exam_attempt`, `start_exam_attempt`, `stop_exam_attempt`, `mark_erroneous_exam_attempt`, `remove_exam_attempt`, `on_review_callback`, `on_exam_saved`, `get_attempt`, `get_exam`, `get_instructor_url`, `retire_user`, `get_onboarding_profile_info`, `get_proctoring_config`, `get_video_review_aes_key`, `should_block_access_to_exam_material`, `get_javascript`, `get_software_download_url` |
| 🔵 **`@abstractmethod` en esa clase** | 🔵 **CERO** | **No es una ABC: es una base concreta con implementaciones por defecto.** Un backend mínimo **sobreescribe sólo lo que usa** — es la diferencia entre «implementar 18 métodos» y «implementar 4» |
| Base REST ya escrita | **`BaseRestProctoringProvider`** (`backends/rest.py`, **14.460 bytes**, 27 métodos) | Trae los constructores de URL (`exam_url`, `create_exam_attempt_url`, `config_url`, `instructor_url`, `onboarding_statuses_url`…) y `_make_attempt_request` |
| Registro del plugin | ***entry point* de Django**, grupo **`[openedx.proctoring]`** | Ya vienen 4: `mock`, `null`, `rpnow4`, `software_secure` (los dos últimos apuntan al mismo proveedor) |
| 🟢 Borrado de datos ya modelado | **2 rutas + 1 método** | `retire_user` / `retire_backend_user` existen en el modelo: **el expediente de supresión no se construye, se cablea** |

🟢 **La respuesta, en una línea para una propuesta:** *«no se escribe la capa: se registra un *entry point* y se
sobreescriben los métodos de ciclo de vida del intento; la máquina de estados, las excepciones (*allowances*), la política
de revisión y las 20 rutas REST ya están, y el directorio donde va tu código es Apache-2.0»*.

### 🟢 Acción 1 — las dos capas sin competencia agéntica ahora tienen anclas medidas, y las dos son usables

**El pase 40 midió que `unitime` y `safe-exam-browser` no devuelven NI UN nombre en los 903.402 de PyPI** y mandó a
medirlas por su repositorio (**gap 85**). Hecho:

| Pieza | Licencia (leída del árbol) | `HEAD` | Tags | Tamaño | Veredicto |
|---|---|---|---|---|---|
| [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** (`LICENSE` + `NOTICE`: *«Copyright 2015, The Apereo Foundation»*) | 🟢 **2026-10-01** (ayer) | **202** | 4.154 archivos, Java | 🟢 **ALTA — y es la mejor noticia de licencia de la capa administrativa** |
| [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | ⚠️ **MPL-2.0** (`LICENSE` en `master`) | ⚠️ `master` **2026-04-01** / 🟢 `dev-3.0` **2026-10-01** | **108** | 1.450 archivos, Java (`ch.ethz.seb`) | 🟢 **ALTA — es la capa de integración de examen que el gap 84 dijo que no existía en permisivo** |
| [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) | ⚠️ **MPL-2.0** (`LICENSE.txt`) | 🟢 **2026-09-25** | **20** | 1.452 archivos, C# | 🟢 **ALTA — el cliente de bloqueo, Windows** |

🟢 **Y la respuesta a la pregunta que la acción 1 hacía — «¿alguno expone una API envolvible como MCP?» — es SÍ en los
dos, y en UniTime es más limpia que en cualquier LMS que esta base haya medido**, porque **el conector ya es la unidad**:

| UniTime: `org.unitime.timetable.api` | Qué es |
|---|---|
| `ApiConnector` (clase abstracta) | `doGet` / `doPut` / `doPost` / `doDelete` + **`getName()`** + `createHelper()` |
| Autenticación | **ya trae token**: `authenticateWithTokenIfNeeded()`, parámetro `?token=`, propiedad `ApiCanUseAPIToken` |
| Serialización | `JsonApiHelper`, `XmlApiHelper`, `BinaryFileApiHelper` |
| 🟢 **Conectores registrados** | 🟢 **15, con nombre propio** |

| Conector | Nombre registrado (`/api/<nombre>`) | Verbos implementados |
|---|---|---|
| `RoomsConnector` | `rooms` | **GET, POST, PUT, DELETE** |
| `BuildingsConntector` *(el typo es del upstream)* | `buildings` | GET, POST, DELETE |
| `EventsConnector` | `events` | GET, POST, DELETE |
| `OnlineStudentSchedulingConnector` | `sectioning` | GET, POST |
| `DataExchangeConnector` | `exchange` | GET, POST |
| 🔴 `ScriptConnector` | 🔴 **`script`** | 🔴 **GET, POST** |
| `VariableTitleCourseConnector` | `var-title-crs` | GET, POST |
| `JsonConnector` | `json` | POST |
| `CurriculaConnector` / `EnrollmentsConnector` / `InstructorsConnector` / `InstructorScheduleConnector` / `RolesConnector` / `StudentGroupsConnector` / `ClassInfoConnector` | `curricula`, `enrollments`, `instructors`, `instructor-schedule`, `roles`, `student-groups`, `class-info` | GET |

🔴 **Y el detalle que hay que leer antes de escribir una línea de *gateway*: existe un conector llamado `script` que acepta
`POST`.** Un envoltorio MCP ingenuo de los 15 conectores **expone ejecución de scripts del servidor como una tool**. **Es
el caso de uso exacto del *gateway* de allowlist que el pase 40 dejó probado (P85), y acá deja de ser higiene para ser
requisito.** Ver **P88**.

### 🟢 SEB Server ya habla con los tres LMS que esta base ya tiene — y eso es lo que lo vuelve componible, no su licencia

**`seb-server` trae 36 controladores REST y 41 constantes de *endpoint***, entre ellos `ExamProctoringController`,
`ExamMonitoringController`, `ClientConnectionController`, `LmsIntegrationController`, `ExamAPI_V1_Controller` y
`ExamAPIDiscoveryController`. 🟢 **Pero el dato que manda es su `enum LmsType`:**

| `LmsType` | *Features* declaradas | ¿Está ya en esta KB? |
|---|---|---|
| **`OPEN_EDX`** | `COURSE_API`, `SEB_RESTRICTION` | 🟢 **sí** (`openedx/edx-platform`) |
| **`MOODLE`** | `COURSE_API`, `COURSE_RECOVERY` *(SEB_RESTRICTION comentada en el fuente)* | 🟢 **sí** (`moodle/moodle`) |
| **`MOODLE_PLUGIN`** | `COURSE_API`, `COURSE_RECOVERY`, `SEB_RESTRICTION`, **`LMS_FULL_INTEGRATION`** | 🟢 **sí** — y es **la única combinación con integración completa** |
| **`OPEN_OLAT`** | `COURSE_API`, `SEB_RESTRICTION` | 🟢 **sí** (`OpenOLAT/OpenOLAT`) |
| `ANS_DELFT` | `COURSE_API`, `SEB_RESTRICTION` | no |
| `MOCKUP` | las tres | — (para pruebas) |

🔵 **O sea: la capa de examen permisiva de este sector ya tiene escrita la unión con tres de las plataformas que esta base
viene listando como fundacionales desde el pase 1.** **El trabajo no es integrar: es `MOODLE_PLUGIN` + una puerta de
agente.** Ver **P89**.

### 🔴 Y un hallazgo de método que obliga a releer cómo esta base fecha proyectos: **la rama por defecto puede ser la rama muerta de un proyecto vivo**

| Rama de `seb-server` | Último commit |
|---|---|
| 🔴 **`master`** (la rama por defecto, la que mide `HEAD`) | 🔴 **2026-04-01** — 6 meses |
| 🟢 **`dev-3.0`** | 🟢 **2026-10-01** — **ayer** |
| 🟢 `development` | 🟢 **2026-09-30** |

🔴 **Medido con el instrumento del pase 37 —`ls-remote --symref HEAD` + fecha del commit— SEB Server se registra como
«FRÍO, 6 meses».** Y es **falso**: el proyecto commiteó ayer, en la rama donde desarrolla, y publica el tag
**`v3.0-latest`**. **El instrumento no está roto; está mal apuntado**: `HEAD` apunta a la rama de *release*, no a la de
trabajo. Ver la tendencia **152**.

### 🟢 La prueba de validez que eso exige, corrida sobre las 10 filas que el pase 37 declaró paradas — y el resultado tiene dos mitades

**Se volvieron a medir las 10, pero contra TODAS las ramas, no sólo la de por defecto.**

| Repo | Ramas | `HEAD` por defecto | Commit más nuevo en cualquier rama | ¿Cambia el veredicto? |
|---|---|---|---|---|
| `Cicatriiz/openedu-mcp` | 5 | 2025-06-03 | 2025-06-03 (`main`) | 🟢 no |
| `DavidLMS/learnmcp-xapi` | 1 | 2025-08-29 | 2025-08-29 (`main`) | 🟢 no |
| `pythpythpython/openstax-mcp-server` | 1 | 2025-11-30 | 2025-11-30 (`main`) | 🟢 no |
| `HugeCatLab/ChatTutor` | 2 | 2026-01-09 | 2026-01-09 (`main`) | 🟢 no |
| `peancor/moodle-mcp-server` | 2 | 2026-02-22 | 2026-02-22 (`main`) | 🟢 no |
| `24kchengYe/human-skill-tree` | 1 | 2026-03-25 | 2026-03-25 (`master`) | 🟢 no |
| ⚠️ `trilogy-group/oneroster-ts` | 6 | 2025-06-27 | **2026-05-11** (`speakeasy-sdk-regen-1746144633`) | ⚠️ **+10,5 meses — pero ver abajo** |
| ⚠️ `plastic-labs/tutor-gpt` | **49** | 2025-11-13 | **2026-02-20** (`vineeth/elysia`) | ⚠️ **+3,2 meses, rama de *feature*** |
| ⚠️ `satvik314/educhain` | 7 | 2025-12-03 | **2026-05-29** (`claude/relaxed-curie-mNW2l`) | ⚠️ **+5,9 meses — pero ver abajo** |
| 🟢 `karanb192/algo-sensei` | 2 | 🟢 **2026-10-02** | 🟢 **2026-10-02** (`main`) | 🔴 **SÍ, y no por la rama: ver abajo** |

🔵 **La segunda mitad es la que salva el veredicto original: hay que leer el AUTOR del commit más nuevo, no sólo su fecha.**

| Caso | Autor del commit más nuevo | Mensaje | Qué es realmente |
|---|---|---|---|
| ⛔ `oneroster-ts` | **`speakeasy-github[bot]`** | *«empty commit to trigger [run-tests] workflow»* | 🔴 **un commit VACÍO de un bot generador de SDK.** No es desarrollo: es el antipatrón de patear el CI |
| ⛔ `educhain` | **`Claude`** | *«Refactor to Educhain 1.0: drop LangChain, build on the OpenAI SDK»* | 🔵 **una rama escrita por un AGENTE, sin mergear desde hace 4 meses** |
| ⚠️ `tutor-gpt` | humano | — | rama de *feature* parada hace 7,5 meses, entre **49** ramas |

🟢 **Conclusión, y es a favor del pase 37: en 10 de 10 el veredicto sobre el desarrollo HUMANO en la rama principal se
sostiene.** Pero el instrumento necesita una línea más: **medir todas las ramas y después leer quién firmó.** **Un commit
vacío de bot y un refactor firmado por un agente no son vida de proyecto** — y los dos habrían entrado como tal. Ver la
tendencia **153**.

🔵 **Y el dato de `educhain` vale por sí mismo, más allá del método:** esta KB lo tiene como alta de los pases 2 y 3.
**La rama que un agente dejó escrita dice hacia dónde iba la 1.0: sacar LangChain y apoyarse en el SDK de OpenAI.**
Está sin mergear. **Es señal de dirección, no de release.**

### 🟢 `algo-sensei` revivió HOY, y el pase 37 tenía razón cuando corrió — las dos cosas a la vez

| Dato | Valor |
|---|---|
| Lo que publicó el pase 37 (corrido **hoy**) | `2025-10-22`, **11,3 meses**, 🔴 **FRÍO** |
| Lo que mide este pase (corrido **hoy**, horas después) | 🟢 **`2026-10-02T15:10:33+05:30`** |
| El commit | *«Offer a star invitation once after confirmed learning (#2)»* — **el commit número 2 del repo**, tras un hueco de **11,4 meses** |
| Commits totales en `main` | **9**, un solo autor |

🔵 **No es una corrección del pase 37: es la demostración de que esta medición caduca en horas.** Y conviene no
sobreleerla: **un repo de 9 commits cuyo primer commit en un año agrega una invitación a poner una estrella es una
reactivación de forma, no de fondo.** Sigue sin ser una dependencia.

### ⚠️ Acción 2 — las tres contradicciones de licencia: una cierra, y las otras dos resultan ser **dos clases distintas**, no una

**(a) `exam-guard` — el gap 83 queda CERRADO, y por la historia del archivo, que es exactamente donde el pase 40 dijo que estaba la respuesta.**

| Evidencia | Valor |
|---|---|
| `LICENSE` en el árbol | **Apache-2.0**, 11.357 bytes |
| 🔴 **Cuándo entró** | 🔴 **en el commit *«Initial commit»*, `1fcf7f6`, 2024-09-10T01:20 — y era el ÚNICO archivo del commit** (201 líneas) |
| `package.json` en el árbol | **`"license": "ISC"`** (versión del árbol: 8.1.0) |
| Cuándo entró `package.json` | el commit siguiente, *«feat: add base code»*, 2024-09-10T15:39 |
| Licencia en el registro | **ISC en 113 de 113 versiones publicadas**, desde 2024-09-12 hasta 2026-01-22 |
| Último toque a `package.json` | **2025-10-09** (el autor lo editó muchas veces) |
| Último toque a `LICENSE` | 🔴 **nunca más desde el *«Initial commit»*** |

🟢 **El veredicto, y es inequívoco:** el `LICENSE` Apache-2.0 es **el artefacto de creación del repo** (la casilla «add a
license» de GitHub: un commit inicial que contiene sólo ese archivo). **La intención expresada y RE-afirmada 113 veces por
el autor es ISC.**

🔵 **Y la parte que importa comercialmente, que el pase 40 no había notado: las dos candidatas son permisivas y OSI, así
que la contradicción NO bloquea el uso.** La diferencia entre Apache-2.0 e ISC **no es permisiva contra copyleft: es la
cláusula de patentes** (Apache-2.0 la concede expresamente; ISC no la menciona). **El gap 83 baja de «bloquea
entregables» a «anotar cuál se asume y por qué».** Ver la tendencia **154**.

⚠️ **Dato lateral, del mismo tipo que la tendencia 147 pero invertido:** `exam-guard` tiene **`HEAD` 2025-10-09 y versión
8.1.0 en el árbol**, contra **10.0.4 publicada el 2026-01-22** en npm. **El registro va ADELANTE del repo**: hay dos
*majors* publicados que no están en la rama. **No se lee el fuente de lo que el cliente instalaría.**

**(b) y (c) — el gap 81 no era una clase: eran dos, y la diferencia de riesgo es grande.** El pase 40 las trataba como
equivalentes (*«licencia declarada sólo en el manifiesto del registro»*). Medidas de primera mano, no se parecen:

| Pieza | Declaraciones de licencia que EXISTEN en el mundo | Medición |
|---|---|---|
| ⚠️ **`Timadey/proctor`** | 🟢 **TRES, y todas en el árbol** | 1) campo `license` del manifiesto npm: **MIT**; 2) **`package.json` del árbol: `"license": "MIT"`**; 3) **`README.md` del árbol: badge *«License: MIT»*** *y* sección *«This project is licensed under the MIT License — see the [LICENSE] file for details»*. 🔴 **Y el archivo `LICENSE` no existe en NINGUNA rama ni en NINGÚN commit de toda la historia** (`git log --all --name-only`, 0 coincidencias con `licen|copying`) |
| 🔴 **`@ink-waffle/sisu-mcp`** | 🔴 **UNA, en todo el mundo** | sólo el campo `license` de npm. **El tarball (44.781 bytes, 17 archivos `dist/*.js`, 1 sola versión 0.1.0 del 2026-09-17) no trae `LICENSE`, y tampoco trae `README`.** Sin `repository`, sin `homepage` |

🟢 **`Timadey/proctor` deja de ser un caso de licencia dudosa y pasa a ser un caso de archivo faltante, y se puede
demostrar:** el propio árbol **apunta** al archivo que falta (*«see the LICENSE file»*). **La intención es inequívoca y
está escrita tres veces; lo único ausente es el texto.** 🔵 **Y se cierra con una contribución de un archivo —el PR más
barato que esta base identificó— que además deja a Globant como contribuyente del upstream.**

🔴 **`sisu-mcp` se queda con la reserva completa, y ahora se sabe que es el caso extremo de la clase:** no hay segunda
declaración posible porque **no hay dónde buscarla**. Sigue siendo **la única puerta de SIS de educación superior de esta
base**, y sigue sin poder proponerse. Ver la tendencia **155**.

⚠️ **Lo que este pase NO hizo, y queda declarado:** la acción 2 del pase 40 proponía **abrir un *issue* o mandar un correo
a los autores** de `@timadey/proctor` y `@ink-waffle/sisu-mcp`. **No se hizo: escribirle a un tercero en su repositorio es
una acción hacia afuera y no la decide esta corrida.** Queda como **acción con destinatario humano** (ver las acciones del
pase 41, abajo). **Lo que sí se hizo es agotar la evidencia disponible sin contactar a nadie** — y para
`@timadey/proctor` eso alcanzó para cambiarle la clase.

### 🔴 Medición de vacío, con el instrumento del pase 40: **nadie envolvió todavía ninguna de las dos capas**

| Instrumento | Términos | Resultado |
|---|---|---|
| npm (`registry.npmjs.org/<nombre>`) | `unitime-mcp`, `mcp-unitime`, `seb-mcp`, `mcp-seb`, `safeexambrowser-mcp`, `sebserver-mcp`, `timetable-mcp`, `timetabling-mcp` | 🔴 **404 en 8 de 8** |
| PyPI (índice `simple` completo, **46.675.078 bytes**) | `unitime`, `seb-server`, `safeexambrowser` | 🔴 **0 nombres** |

🟢 **Conclusión: dos capas con despliegue institucional real, licencia usable (Apache-2.0 y MPL-2.0), API formal
documentada en el fuente — y cero competencia agéntica.** Es el hueco más limpio que esta base midió en varios pases.
Ver el **gap 86** y los patrones **P88** y **P89**.

### ⚠️ Nota de método: el control de `curl` sobre `github.com`, que **re-confirma la tendencia 131** y no descubre nada

Antes de escribir las URLs nuevas se corrió el verificador que la consigna pide (`curl`), **con controles negativos**:

| URL | HTTP |
|---|---|
| `github.com/UniTime/unitime` (**existe**) | **403** |
| `github.com/UniTime/this-repo-does-not-exist-xyz123` (**no existe**) | **403** |
| `github.com/openedx/edx-proctoring` (**existe**) | **403** |
| `github.com/openedx/fake-repo-zzz999` (**no existe**) | **403** |

🔴 **403 en los cuatro: el instrumento no distingue un repo real de uno inventado**, que es la misma forma de falla que el
`200` de PyPI del pase 40 (tendencia **141**). 🟢 **`git ls-remote` acierta en 4 de 4** (devuelve refs en los dos reales,
falla en los dos falsos). **Esto ya estaba escrito como tendencia 131 en el pase 37** y se registra como **re-confirmación
con control negativo**, no como hallazgo: **toda URL de GitHub de este pase se verificó con `git ls-remote` y clonando el
árbol, que es evidencia más fuerte que un `HEAD` de HTTP.**

## 2026-10-02 (pase 40) — el pase que **corre el barrido por registro sobre las cuatro capas de administración académica** y encuentra que **están vacías de agente**, con el instrumento del pase 39 **roto y devolviendo 200**

**La acción 1 del pase 39 pedía barrer las capas que el 39 no barrió: *proctoring*, *timetabling*, analítica por nombre
de herramienta, admisiones, *student success* y accesibilidad** — las dos últimas declaradas por esta base como las
peor abastecidas de toda la KB. Se barrieron **28 términos × 4 registros**. El resultado tiene dos mitades y la
primera es de método.

### 🔴 El hallazgo que manda: el instrumento de PyPI del pase 39 está roto, y falla DEVOLVIENDO 200

El pase 39 dejó escrito que *«PyPI no tiene API de búsqueda: hay que raspar el HTML de `/search/`»*. **Hoy ese
raspado no devuelve resultados, y no devuelve un error: devuelve `HTTP 200` con una página de desafío anti-bot.**

| Medición | Valor |
|---|---|
| Términos barridos contra `pypi.org/search/?q=` | **28** |
| Respuestas `HTTP 200` | **28 / 28** |
| Respuestas con `<title>Client Challenge</title>` | 🔴 **28 / 28** |
| Paquetes extraídos | **0** |
| Tamaño típico de la respuesta | **3.038 bytes** (una página de resultados real pesa cientos de kB) |
| Control positivo: `pypi.org/pypi/<nombre>/json` | 🟢 **200 con datos reales** (probado en 3 paquetes) |

🔴 **Por qué esto es peor que un bloqueo y hay que dejarlo escrito:** un `403` se nota. **Un `200` con cero resultados
se registra como «ausencia confirmada por segundo canal»**, que es exactamente la frase con la que el pase 39
justificó nueve ausencias. **Un barrido corrido hoy con el procedimiento del 39, sin mirar el `<title>`, habría
publicado 28 ausencias falsas y las habría llamado medición.** Es la forma de error que esta base viene nombrando
desde el principio: *el silencio se parece demasiado a la cobertura*. **Regla nueva y barata: todo raspado de HTML
lleva un control de contenido, no sólo de código de estado.**

### 🟢 Y el reemplazo existe, es mejor que el original y queda documentado: el índice `simple` de PyPI

| Instrumento | Endpoint | Resultado |
|---|---|---|
| 🔴 Búsqueda (roto) | `pypi.org/search/?q=<término>` | 200 + desafío, 0 resultados |
| 🟢 **Descubrimiento (nuevo)** | **`pypi.org/simple/`** | **200, 46.675.078 bytes, 903.402 nombres de paquete** |
| 🟢 Confirmación (sin cambios) | `pypi.org/pypi/<nombre>/json` | 200 con licencia, releases y fechas |

**El índice `simple` entrega el nombre de todos los paquetes de PyPI en una sola respuesta.** No trae descripciones,
así que no reemplaza una búsqueda semántica — **pero la acción del pase 39 era buscar por *nombre de proyecto*, y para
eso es estrictamente mejor que el buscador**: es la lista completa, sin ranking, sin paginación y sin desafío. Se
descarga una vez y se consulta localmente con `grep`.

### 🔴 La segunda mitad: las cuatro capas de administración académica están VACÍAS de agente

**Barridas `proctoring`, `timetabling`, admisiones, *student success* y accesibilidad en npm, PyPI, Packagist y
RubyGems, con el filtro de dominio educativo y descartando homónimos: no existe ni UNA puerta MCP de educación en
ninguna de las cinco capas.** Las piezas reales que aparecen son **librerías de aplicación**, no agentes.

🔵 **Y la única traza de un MCP de *timetabling* que encontró el barrido es su mitad cliente:**
**`ucleeds-mcp-tester`** (**MIT**, npm, **1 release del 2025-04-25**, **sin repositorio**) se describe como *«Test
client for UCLeeds Timetabling MCP integration»*. **El tester se publicó; el servidor que testea, nunca.** Es la
evidencia más limpia que esta base tiene de que alguien construyó la pieza que falta y no la liberó.

### 🔴 Los homónimos, y acá hay un hallazgo de categoría: el mundo de los agentes se quedó con las dos palabras

El pase 39 llevaba la cuenta en **9 colisiones**. Este pase suma **once más**, y no son ruido aleatorio: **dos
términos centrales de esta vertical fueron recolonizados por el vocabulario del propio mundo agéntico.**

**«Proctor» ya no significa vigilar un examen. Significa vigilar al agente.**

| Candidato | Qué es en realidad | Licencia |
|---|---|---|
| ⛔ `proctor-mcp` | *«Human oversight for MCP agents. The human-in-the-loop the MCP spec asks for and does not provide»* | — |
| ⛔ `proctor-skill` | interroga al desarrollador sobre cambios de rama antes de permitir `git push` | — |
| ⛔ `@genramzi/proctor` | *«Audit what coding agents said against what they actually did»* | — |
| ⛔ `proctor-ai` (PyPI) | framework de *prompt engineering* estructurado | MIT |
| ⛔ `agentproctor`, `sqlproctor`, `onion-proctor` | supervisión de agentes / SQL / red | — |
| ⛔ `matthewproctor-postcodes` | **el apellido de una persona** — códigos postales australianos | — |

**«Caliper» tiene seis homónimos y UNA sola pieza educativa.** El estándar de analítica de 1EdTech comparte nombre
con, al menos: `caliper-ai` (**MIT**, costo de AI de *coding agents*), `caliper-py` (**MIT**, *tracker* de
experimentos ML), `caliper-reader` (**BSD**, *profiling* de HPC de **Lawrence Livermore**), `caliper-sdk`
(**GPL-3.0**, observabilidad de LLM), `caliper` (**MPL-2.0**, medición de cambios en paquetes) y `@dendiem/caliper`
(**MCP de revisión de UI**). 🔵 **La única educativa del barrido es `timeback-caliper`**, y hay que leerla con
reserva (ver abajo).

**Dos homónimos más, los dos de dominio adyacente y los dos verosímiles:** ⛔ `sih-br-mcp` — **admisiones
HOSPITALARIAS** de Brasil (DATASUS SIH/SUS), que en un barrido por `admissions` entra como si fuera admisión
universitaria; y ⛔ `timetable-api-node` — **horarios del transporte público de Lviv**, que entra por `timetable`.

### Las altas del pase, con el dato crudo

| Pieza | Capa | Licencia (dónde se leyó) | `HEAD` / release | Veredicto |
|---|---|---|---|---|
| `datakind/student-success-tool` | **student success** | 🟢 **MIT** — `LICENSE.md` del árbol (*«Copyright (c) 2022 DataKind»*) | `HEAD` **2025-09-08** / PyPI **2025-08-05**, 14 releases | 🟢 **ALTA — cierra la capa que esta base declaró peor abastecida.** Ver `repos/foundations.md` |
| `openedx/edx-proctoring` | **proctoring** | **AGPL-3.0** — `LICENSE.txt` en `master` | `HEAD` **2026-05-30** / PyPI **2025-04-28**, 253 releases | 🟢 **ALTA — es el subsistema oficial de Open edX.** Copyleft, y **repo vivo con registro parado hace 17 meses** |
| `Drone9/mereos` | **proctoring** | 🟢 **MIT** — `LICENSE` del árbol **y** campo npm | **2026-08-28** (repo y registro **coinciden**) | 🟢 **ALTA a `agents/top.md`** |
| `@timadey/proctor` | **proctoring** | ⚠️ **MIT sólo en el manifiesto npm** — sin `LICENSE` en el árbol | **2026-08-08** (coinciden) | ⚠️ **ALTA con reserva de evidencia** (clase del gap 81) |
| `odoo14-addon-ssi-school-admission` | **admisiones** | **AGPL-3** | PyPI **2026-05-01**, 6 releases | 🟢 **ALTA a verticales — y es APAC** (Simetri Sinergi, Indonesia) |
| `timeback-caliper` | **analítica** | ⚠️ **MIT** en `license_expression` de PyPI | PyPI **2026-07-18**, **55 releases** | ⚠️ 🔴 **Su repositorio declarado (`superbuilders/timeback-dev-python`) NO es legible por `git ls-remote`** — cuarta instancia de la tendencia 140 |

### 🔴 Lo que el barrido encontró MUERTO, y conviene tenerlo escrito antes de que alguien lo proponga

| Pieza | Licencia | Última señal | Antigüedad |
|---|---|---|---|
| `openfun/xblock-proctor-exam` | AGPL-3.0 | **2021-02-11** | **5,6 años** — y es de **France Université Numérique**, o sea la opción EMEA de la capa |
| `ucsd-ets/caliper-tracking` (`openedx-caliper-tracking`) | AGPL-3.0 | **2020-10-12** | **6 años** |
| `groovetch/grvlms-proctoring` | AGPL-3.0 | **2020-11-09** | **5,9 años** |
| `proctoru-xblock` | 🔴 **sin licencia** | **2016-08-17** | **10,1 años** |

🟢 **Y una confirmación por tercer canal independiente de algo que esta base ya sabía:** `@learninglocker/xapi-agents`
tiene su **última publicación el 2019-07-11**. La tendencia 56 (*«el LRS más instalado del sector tiene cinco años sin
un commit y se presenta como producto vivo»*) **queda confirmada ahora también desde el registro de paquetes**, que es
un canal distinto del repo y del sitio.

## 2026-10-02 (pase 39) — el pase que **deja de preguntarle a GitHub y le pregunta al REGISTRO por el nombre del PROYECTO**, que es la acción 1 del pase 38 — y en una tarde encuentra **seis piezas que treinta y ocho pases de barrido sobre GitHub nunca vieron**

**La hipótesis del pase 38 era que el canal estaba mal, no el filtro, y queda confirmada.** El 38 descubrió que el
gap 48 llevaba dos meses cerrado sin que la KB lo notara, porque el barrido buscaba *«conector de terceros»* en GitHub
con nombre `*-mcp` y la puerta la había publicado el propio proyecto **en PyPI**. La acción que dejó escrita era
concreta: **para cada ausencia de conector que esta base declara abierta, consultar el registro de paquetes del
lenguaje de la plataforma (npm, PyPI, Packagist, RubyGems) con el nombre del PROYECTO, no del protocolo.**

**Ejecutada sobre 23 términos × 4 registros, el canal rinde seis altas y nueve ausencias confirmadas por segundo
instrumento.** Ninguna de las seis estaba en esta KB. Ninguna aparece buscando `mcp` + `education` en GitHub.

🔵 **Nota de método, porque el canal nuevo trae dos modos de falla propios y los dos se cobraron víctimas en este
mismo pase:**

| Modo de falla del canal «registro» | Caso medido en este pase | Control que lo detecta |
|---|---|---|
| **Homonimia** — el nombre del proyecto educativo colisiona con un proyecto ajeno más popular | `folio` → **4 paquetes**, ninguno es el ILS: son *redlining* de `.docx` y reportes de agentes de código. `kolibri` → `@public-ui/mcp`, que es el **design system alemán KoliBri**, no la plataforma de aprendizaje de Learning Equality | Leer la `description` **y** el `repository` antes de contar el hit. El filtro de licencia **no** protege contra esto (tendencia 96) |
| **El `repository` del registro no es un repo legible** | `ed-fi-sdk-mcp` y `frappe-mcp-server` declaran URL de GitHub y **las dos fallan `git ls-remote`**; `@ink-waffle/sisu-mcp` **no declara repo en absoluto** | `git ls-remote` sobre la URL declarada. ⚠️ **`curl` no sirve**: `github.com` devuelve 403 para todo, exista o no (tendencia 131) |

### 🟢 Las seis altas, medidas una por una — licencia leída del archivo, `HEAD` del árbol, tools contadas en el código

| Pieza | Licencia (evidencia) | `HEAD` / release | Tools medidas | Región | Qué rol cubre |
|---|---|---|---|---|---|
| 🟢 **`PabloPC05/mcp-usc`** | **MIT** ✅ (`LICENSE` textual + `pyproject.toml`) | **2026-08-27** (1,2 m) · 30 commits | **91** distintas | **EMEA** (España, U. de Santiago de Compostela) | Moodle del lado alumno **+ fuentes académicas oficiales** (calendario de exámenes, titulaciones) |
| 🟢 **`JOSETRA44/DUTIC-mcp`** | **MIT** ✅ (`LICENSE` textual + manifiesto) | **2026-09-24** (8 d) · 74 commits | **12** | **LATAM** (Perú, U. Nacional de San Agustín de Arequipa) | Moodle institucional + **biblioteca** + encuestas + `pdf_to_markdown` |
| 🟢 **`dasgltd/mcp-brasil`** v0.14.0 | **MIT** ✅ (`LICENSE`, *«(c) 2025-2026 MCP Brasil»*) | **2026-08-18** (1,5 m, commit **humano**) · 246 commits · **23 tags** · PyPI (18 releases) | **97** en total, **13 de educación** | **LATAM** (Brasil) | **INEP: ENEM (6) + Censo Escolar (7)** sobre ingesta de microdatos |
| 🟢 **`maxxeddev/open-badges-mcp`** (`mcp-ob-ts`) | **MIT** ✅ (`LICENSE` + manifiesto + README) | repo **2026-06-10** (3,7 m ⚠️) · npm **0.3.2** / repo **0.4.0** | **16** | **APAC** (zona `+10:00`, Australia) | Open Badges 3.0: spec, **generación, FIRMA Ed25519 y validación** |
| 🟢 **`@ink-waffle/sisu-mcp`** | ⚠️ **MIT** sólo por campo de npm (**sin repo público y sin `LICENSE` en el tarball**) | **2026-09-17** (15 d) · 1 release | **12** (`sisu_*`) | **EMEA** (Finlandia, Sisu de Funidata) | **SIS** de educación superior: *attainments*, *study rights*, matrícula, horarios, planes, catálogo |
| 🟢 **`suren-kk/armenian-national-library-mcp`** | **MIT** ✅ (`LICENSE` + manifiesto) | **2026-08-10** (1,7 m) · 37 commits | **23**, todas de lectura | **EMEA** (Armenia) | **Primera pieza de esta KB sobre DSpace** — descubrimiento, contenido y API cruda del repositorio |

Y dos que entran **con reserva declarada**, porque la evidencia de licencia es más débil que la de las seis anteriores:

| Pieza | Por qué la reserva | Medición |
|---|---|---|
| ⚠️ **`ed-fi-sdk-mcp`** (npm, *maintainer* **`edfi`** — la cuenta del propio consorcio) | **Apache-2.0** ✅ con `LICENSE` **dentro del tarball**, pero el **repo declarado no es legible** y hay **un solo release, del 2025-10-03** (12 meses, *span* 0 días) | **11 tools, y ninguna toca dato de alumno:** `search_endpoints`, `search_schemas`, `get_schema_details`, `get_endpoint_details`, `get_entities_by_domain`, `list_entity_relationships`, `generate_entity_diagram`, `export_diagram_as_text`, `list_available_versions`, `set_data_standard_version`, `set_custom_data_standard_url` |
| ⚠️ **`frappe-mcp-server`** 0.6.0 | **ISC** sólo por campo de npm (**sin `LICENSE` en el tarball**), repo **no legible**, último release **2025-07-30** (14 meses) | **21 tools** de CRUD genérico de DocType — y entre ellas **`call_method`** (ejecución de método arbitrario *whitelisted*) y `delete_document` |

### 🔴 La corrección más importante del pase, y es a una afirmación propia sobre LATAM

Esta base publicó, en el pase 35 y reafirmó en el 36, que **«Brasil está construyendo una capa MCP nacional sobre sus
datos públicos, y educación es el único dominio grande que falta»** (tendencia 114, gap 69), y que por eso el INEP
había que cotizarlo como **pipeline de ingesta de 8-12 semanas** y no como fachada.

**La mitad arquitectónica de esa afirmación era correcta. La mitad de la ausencia era falsa.**

`dasgltd/mcp-brasil` (MIT) tiene **dos de sus quince datasets dedicados a educación**, con **13 tools**:

| Dataset | Tools |
|---|---|
| `inep_enem` | `info_enem`, `refrescar_enem`, `valores_distintos_enem`, `media_notas_uf`, `media_notas_por_grupo`, `top_municipios_por_media` |
| `inep_censo_escolar` | `info_censo_escolar`, `refrescar_censo_escolar`, `valores_distintos_censo`, `buscar_escolas`, `escola_detalhe`, `resumo_uf`, `top_municipios_por_escolas` |

🟢 **Y confirma la predicción de arquitectura del pase 36 ejecutándola:** no consume API del INEP —porque no hay—,
**descarga los ZIP de microdatos** (`download.inep.gov.br/microdados/microdados_enem_*`,
`download.inep.gov.br/dados_abertos/microdados_censo_escolar_*`) y sirve agregados. **Es exactamente el pipeline que
P77 describía. Lo que cambia es que ya está escrito, es MIT, y hay 23 tags y un canario semanal de salud de fuentes en
CI.** La cotización pasa de *«8-12 semanas de construcción»* a *«adopción + extensión»*.

### 🔵 El patrón que aparece al mirar las tres regiones juntas: **tres piezas permisivas, tres estatutos, tres diseños que los encodean**

El pase 38 encontró la primera pieza de esta base cuyo diseño de seguridad es argumento de cumplimiento
(`moodle-grading-mcp`, que deja la nota en `readyforreview` y no la publica). **Este pase encuentra que no es un caso
aislado: es un patrón regional, y ya hay uno por región grande.**

| Pieza | Estatuto que su diseño encodea | Mecanismo medido en el código |
|---|---|---|
| `bruchris/canvas-lms-mcp` (MIT, ya en la tabla) | **FERPA** (North America) | **Modo FERPA**: `CANVAS_PSEUDONYMIZE_STUDENTS=true` seudonimiza alumnos; la **reversión** exige una **segunda** bandera (`CANVAS_PSEUDONYMIZE_REVERSE_LOOKUP=true`) y la tool `resolve_pseudonym` **sólo se registra en transporte stdio**, como tool 166 |
| `toshieji/moodle-grading-mcp` (MIT, pase 38) | **AI Act Anexo III §3** (EMEA) + supervisión humana de Oklahoma/Maryland | `save_grade_draft` → `workflowstate=readyforreview`: **la nota no se publica**; allowlist de cursos, audit trail JSONL, sin notificación al alumno |
| `dasgltd/mcp-brasil` (MIT, alta de este pase) | **LGPD** (LATAM) | `COLUNAS_DISTINCT_PERMITIDAS` en `datasets/inep_enem/constants.py`: *frozenset* de **8 columnas**, todas categorías agregadas (`SG_UF_PROVA`, `SG_UF_ESC`, `TP_SEXO`, `TP_COR_RACA`, `TP_ESCOLA`, `TP_LINGUA`, `TP_FAIXA_ETARIA`, `TP_ST_CONCLUSAO`). `SOURCES.md` documenta el retiro de microdatos del INEP en 2022 por LGPD, la reanudación anonimizada de 2024, clasifica educación como **RISCO ALTO** y remite a **SEDAP** para microdatos no anonimizados; re-identificación **vedada** |

🟢 **Para una propuesta esto es mejor que una cláusula: es código que ya hace lo que el regulador pide, en las tres
regiones donde esta KB vende.** Ver **tendencia 136**.

### 🟢 El sexto mecanismo de confirmación, y es el único que se puede imponer **partiendo el conjunto de tools**

`mcp-usc` tiene **91 tools**, y la mitad de su superficie de escritura está construida como **gemelos `preview_*`**:
`preview_submit_assignment` / `submit_assignment`, `preview_start_quiz` / `start_quiz`,
`preview_save_quiz_answers` / `save_quiz_answers`, `preview_remove_submission` / `remove_submission`,
`preview_replace_submission_files`, `preview_create_personal_calendar_event`, `preview_reply_forum_post`,
`preview_message`, `preview_mark_course_self_completed`, `preview_update_activity_completion_status_manually`… —
**22 tools de previsualización** contra sus escrituras correspondientes.

🔵 **Por qué importa y en qué se diferencia de las cinco variantes que esta base ya catalogó** (`confirm=true`,
*elicitation*, `readOnlyHint`, cuota por ventana, anclaje en artefacto externo): las cinco se cumplen **dentro** de la
tool, así que confiar en ellas es confiar en el servidor. **El gemelo `preview_*` es una tool distinta**, y por lo
tanto se puede **imponer desde afuera**: un cliente al que se le entrega sólo la mitad `preview_*` y las de lectura
**no puede ejecutar la escritura, no porque se porte bien, sino porque la tool no está en su lista**. Es la única
variante aplicable por **partición del conjunto de tools** en vez de por confianza. Ver **tendencia 137** y **P82**.

### ⚫ Lo que el barrido rechazó, fechado, para que ningún pase lo vuelva a buscar

| Candidato | Veredicto | Medición |
|---|---|---|
| ⛔ **`NicolasViruel/moodle-utn-mcp`** (Argentina, UTN) | **No entra: sin licencia en ningún artefacto** | `HEAD` **2026-09-28** (la pieza LATAM más fresca del barrido) y 16 commits, pero **no hay `LICENSE` ni campo de licencia en el manifiesto** → todos los derechos reservados. **Mismo veredicto que `loyaniu/moodle-mcp` en el pase 38** |
| ⛔ `@stll/folio-agents`, `@stll/folio-cli`, `agent-folio`, `@handsong/folio-ui-cli` | **Homonimia**: ninguno es el ILS FOLIO | *redlining* de `.docx`, reportes de agentes de código, UI para agentes |
| ⛔ `@public-ui/mcp` (4.4.0, 136+ componentes) | **Homonimia**: es el *design system* **KoliBri**, no Kolibri de Learning Equality | `repository` → `github.com/public-ui/kolibri` |
| ⛔ `@transcend-io/mcp-server-assessments` | **Homonimia**: *assessments* de privacidad, no de evaluación educativa ni QTI | Apareció en los barridos de `qti assessment` **y** `pronunciation assessment` |
| ⛔ `personaforge`, `confused-ai` | **Homonimia**: frameworks de agentes genéricos, no *knowledge tracing* | Apareció buscando `knowledge tracing` |

### 🟢 Las nueve ausencias que el canal nuevo CONFIRMA por segundo instrumento

**Esto es lo que vuelve útil un barrido que «no encontró nada»:** nueve ausencias que esta base declaraba sobre
evidencia de un solo canal (GitHub) quedan confirmadas por un canal independiente (4 registros de paquetes). **Cero
hits con `mcp`/`agent` en nombre o descripción**, sobre un total de resultados leídos:

| Ausencia declarada | Términos barridos | Resultados leídos | Hits |
|---|---|---|---|
| Koha (ILS) | `koha library` | 35 | **0** |
| Chamilo | `chamilo` | 16 | **0** |
| Sakai | `sakai` | 41 | **0** |
| OpenOLAT | `openolat` | 15 | **0** |
| Oppia | `oppia` | 18 | **0** |
| Opencast | `opencast` | 33 | **0** |
| BigBlueButton | `bigbluebutton` | 40 | **0** |
| Sunbird | `sunbird` | 21 | **0** |
| nbgrader / Caliper / LTI 1.3 / *pronunciation* / *knowledge tracing* | 5 términos | 20 + 21 + 35 + n | **0 reales** |

🔴 **Y la que más vale, porque cierra el residuo del gap 70 por el canal que faltaba:** el envoltorio MCP de **QTI**
sigue sin existir *upstream*. El barrido de `qti assessment` en los cuatro registros devuelve **un solo hit y es
homónimo**. **La especificación de 20 tools que el pase 36 dejó escrita en P76 sigue siendo la contribución más limpia
que esta base tiene identificada, y ahora se sabe que nadie se adelantó.**

### ✅ gap 79 CERRADO — y el instrumento del gap 78 lo resuelve en una medición

El pase 38 dejó abierto cuál de `Ed-Fi-Alliance-OSS/edfi-oneroster` y `CSR2017/edfi-oneroster` es *upstream*.
**Medido con `merge-base` + `rev-list --left-right`:**

| Medición | Valor |
|---|---|
| Primer commit de los dos | **`02cbad5`, idéntico, `2025-08-07T16:03:10-05:00`** |
| `merge-base` | **`937248b` — es el tip exacto de `CSR2017`** |
| Commits que `CSR2017` agrega y la Alliance no tiene | **0** |
| Commits que la Alliance agrega y `CSR2017` no tiene | **3** (los tres de *Vinaya Mayya*) |
| Tags | **86** (Alliance) contra **8** (`CSR2017`) |
| Tip de `CSR2017` | `Bump the minor-patches group…` → **commit de bot**; su último commit humano es **2026-09-22** |

🟢 **Conclusión: `Ed-Fi-Alliance-OSS/edfi-oneroster` es la línea viva y es la que hay que citar.** `CSR2017` **no es
una alternativa: es un espejo estrictamente atrasado**, con 0 commits divergentes.

🔵 **Y deja una sub-regla que el pase 38 no tenía, hermana de la suya:** el 38 aprendió que *un fork con `main` más
nuevo no es un mantenedor*. **El 39 aprende el caso inverso: dos repos con el mismo commit inicial y 0 commits
divergentes no son dos proyectos, son uno y un espejo — y el que hay que citar es el que está adelante, no el que el
buscador lista primero.** Este pase lo vivió **dos veces**: también con `mcp-brasil`, donde el buscador lista primero
a `marcellodesales/mcp-brasil` (**0 adelante, 8 atrás**, `HEAD` 2026-04-26) y la línea viva es `dasgltd/mcp-brasil`
(`HEAD` 2026-08-18). Ver **tendencia 138**.

### ✅ El residuo explícito del pase 38, cerrado: `moodler-mcp` enumerado — y trae una corrección y un contraste

El pase 38 lo admitió por licencia y fecha y dejó dicho que **sus tools no se habían enumerado**. Enumeradas:

🔴 **Primero la corrección: `moodler-mcp` NO es TypeScript. Es Python** (`pyproject.toml`, `src/moodler_mcp/**.py`,
`requires-python >= 3.14`, `mcp>=2.2,<3`). La fila de `agents/top.md` decía TypeScript y queda corregida.

**38 tools en 10 módulos: 30 de lectura + 8 de escritura**, y la escritura está partida por **rol**:

| Módulo | Tools | Rol |
|---|---|---|
| `assignments` (8) · `courses` (5) · `calendar` (3) · `forums` (3) · `grades` (3) · `messaging` (3) · `quizzes` (3) · `students` (2) | **30** | lectura |
| `writes_student` (6): `submit_assignment`, `post_forum_reply`, `reply_to_conversation`, `mark_notifications_read`, `mark_activity_complete`, `create_calendar_event` | **6** | escritura de alumno |
| `writes_teacher` (2): **`save_assignment_grade`**, `grant_extension` | **2** | escritura docente |

🟢 **Lo bueno, y es lo más fino de esta capa:** la escritura pide **tres** cosas a la vez — bandera de entorno
**separada por rol** (`MOODLER_ALLOW_TEACHER_GRADING` y `MOODLER_ALLOW_STUDENT_WRITES`, que es más granular que el
`ALLOW_WRITE=1` único de las otras), `confirm=true` explícito, y una **resolución de aprobación del SDK de MCP**
(`Resolve(approval("Save this grade for the student?"))`), además de `ToolAnnotations(read_only_hint=False,
destructive_hint=True, idempotent_hint=False)`.

🔴 **Y lo que hay que decir antes de proponerla para corrección, porque es el contraste exacto con la estrella del
pase 38:** `save_assignment_grade` llama a `mod_assign_save_grade` con **`workflowstate=""`**. **Publica la nota.**
`moodle-grading-mcp` la deja en `readyforreview` a propósito. **Para el régimen de alto riesgo del AI Act y para las
reglas de supervisión humana de North America, la pieza de 9 tools le gana a la de 38.** Superficie y conformidad no
apuntan al mismo lado, y la elección depende de cuál de las dos cosas pesa en el engagement.

⚠️ **Un detalle de arquitectura que la distingue de las otras tres puertas de Moodle y hay que saberlo antes de
cotizar:** depende de **`playwright`**, más `pymupdf`, `python-pptx`, `openpyxl` y `pypandoc-binary`. **No es sólo un
cliente de Web Services: baja y parsea material del curso** (`download_resource`, `read_downloaded_file`,
`get_module_content`). Es la única de las cuatro que ingiere contenido, y también la de huella de despliegue más
grande. **0 tags en el remoto** pese a usar *release-please*: su canal de versión es el changelog, no el tag.

### Lo que este pase deja abierto

- 🔴 **`gap 80`** — **el *daemon* de Docker no corre en este entorno** (`/var/run/docker.sock` ausente), así que la acción 2 del pase 38 (`docker-compose up` en OpenCASE y `tutor plugins enable openedxmcp` para pedir `tools/list` real) **no se pudo ejecutar**. Los **gaps 52 y 55 siguen medidos en papel y en código fuente, no en protocolo.** Es límite de entorno, como el 65 y el 72: **no insistir por esta vía**.
- ⚠️ **`@ink-waffle/sisu-mcp` y `frappe-mcp-server` tienen licencia declarada sólo en el campo de npm**, sin texto en el tarball ni repo legible. Entran con reserva. **Para `sisu-mcp`, que es la única puerta de SIS de educación superior de esta base, vale pedirle el `LICENSE` al autor: es una línea de correo y cambia la clase de evidencia.**
- 🔴 **El `tools/list` real de `ed-fi-sdk-mcp` no se observó** — sus 11 tools se leyeron del tarball publicado. Es la misma distinción que el 30 estableció: superficie de código, no de protocolo.
- ⚠️ **`mcp-usc` y `DUTIC-mcp` son de UNA institución** (USC y UNSA). La mitad Moodle es genérica y la mitad de fuentes oficiales no lo es. **Falta medir qué fracción de cada una es portable**, que es la pregunta que decide si se reusan o se leen como referencia.


## 2026-10-02 (pase 38) — el pase que va a buscar **sucesión** para las tres dependencias congeladas que dejó el 37, y el resultado es asimétrico: **dos de las tres quedan cerradas con piezas permisivas vivas**, la tercera no — y el fork que parecía salvarla está **exactamente 2 commits adelante, y los dos son configuración de Cloud Run**

**La pregunta del pase es la que el 37 dejó abierta y no contestó.** El 37 fechó las 49 filas por el commit de su rama
por defecto y encontró **10 filas paradas hace ≥ 6 meses**, de las cuales **tres son load-bearing**: `learnmcp-xapi`
(42 menciones en `compose/patterns.md`), `oneroster-ts` (la superficie de tools más grande de la base) y
`moodle-mcp-server` de `peancor` (la única pieza permisiva que ponía nota dentro de un LMS). **Diagnosticar no es
reemplazar.** Este pase busca, para cada una, una pieza **permisiva, viva y del mismo rol**, con el mismo instrumento
del 37 (`git ls-remote` + `git fetch --depth 1 <rama>` + `git log -1 --format=%cI`) y verificando el archivo de
licencia por `raw.githubusercontent.com` antes de escribir una sola fila.

🔵 **Nota de método, porque corrige al pase 37 en un detalle que importa para todo barrido futuro:** el `fetch` por
**SHA** de `HEAD` que el 37 describe **falla en este entorno** (`FETCHFAIL` en las 49). El que funciona es el `fetch`
de la **rama por defecto por nombre**, tomando el nombre del `ref:` que devuelve `ls-remote --symref`. Mismo dato,
misma precisión, una llamada menos. El instrumento del 37 es correcto; su invocación no era portable.

### El resultado, fila por fila — y conviene leer la tercera columna antes que la cuarta

| Pieza congelada (pase 37) | Rol que sostiene | Sucesión encontrada en este pase | Estado |
|---|---|---|---|
| 🔴 `DavidLMS/learnmcp-xapi` · MIT · `HEAD` **2025-08-29** (13,1 m) | puerta MCP de xAPI (**P4, P15, P67, P68, P69**) | ❌ **Ninguna en la capa de puerta.** El único fork con `main` más nuevo está 2 commits adelante y no toca el protocolo | 🔴 **Abierto — pero CONTENIDO** (ver abajo) |
| 🔴 `trilogy-group/oneroster-ts` · 0BSD · `HEAD` **2025-06-27** (15,2 m) | OneRoster, 132 tools (**P58, P60, P64**) | ✅ **Lado servidor:** `Ed-Fi-Alliance-OSS/edfi-oneroster` (Apache-2.0, `HEAD` **2026-10-01**). ✅ **Lado cliente:** `TCI/OneRoster` (MIT, Ruby, `HEAD` **2026-09-11**) | 🟢 **Cerrado**, salvo el cliente TypeScript |
| 🔴 `peancor/moodle-mcp-server` · MIT · `HEAD` **2026-02-22** (7,3 m) | nota y devolución dentro del LMS (**P54, P55**, gap 6) | ✅ **Tres** reemplazos MIT vivos, y **dos con mejor diseño que el original** | 🟢 **Cerrado y sobre-ofertado** |

### 🔴 El hallazgo que hay que decir primero, porque es una corrección a una fuente, no a esta base

La búsqueda de sucesión para `learnmcp-xapi` devuelve, en el primer resultado, **`ashleycribb/learnmcp-xapi`**,
descrito por el buscador como *«a more recent fork»*. Y es literalmente cierto: su `main` está en **2026-09-17**,
trece meses más nuevo que el upstream. **Si esta base lo hubiera tomado por el titular, habría escrito que la
dependencia más citada de la KB tiene sucesor.** No lo tiene. Se midió el grafo, no el titular:

| Medición | Valor |
|---|---|
| `merge-base` upstream/fork | `fbf6091` — **es el tip del upstream** (2025-08-29) |
| Commits del fork **que no están** en el upstream | **2** |
| Commits del upstream **que no están** en el fork | **0** |
| Qué son esos 2 commits | `18b2954` *«Add Google Cloud Run deployment configuration and documentation»* + `816d8b8`, su merge de PR #1 |
| Estrellas / tags del fork | **0** / **0** |

🔵 **O sea: el fork no mantiene el proyecto, lo despliega.** La lógica xAPI y MCP es **byte por byte la del upstream
congelado**. Es una receta de despliegue en GCP, y como tal tiene valor — pero **no es sucesión y no debe citarse como
tal**. 🔵 **La regla que deja, y es hermana de la del pase 37 sobre ramas de bot:** *un fork con `main` más nuevo no
es un mantenedor hasta que se cuentan los commits que agrega y se lee qué tocan.* Dependabot infla el grafo de refs;
un fork de despliegue infla la fecha de `main` (**tendencia 132**, **gap 78**).

### 🔵 Por qué «abierto» no es «urgente»: la capa que está DEBAJO de la puerta congelada está viva y es permisiva

Esta es la parte que cambia la lectura de riesgo, y se apoya en algo que la base ya tenía anotado sin conectarlo:
**`learnmcp-xapi` v2.0.0 trae un sistema de plugins de LRS** (SQLite, **Ralph**, **Veracity**), o sea que el LRS se
cambia **por variable de entorno, no por fork**. Y los dos LRS permisivos que esta base recomienda hace 33 pases
fueron re-fechados hoy:

| LRS | Licencia | `HEAD` medido hoy | Último semver | Motores | Región |
|---|---|---|---|---|---|
| 🟢 `yetanalytics/lrsql` (SQL LRS) | **Apache-2.0** ✅ | **2026-10-01** (ayer) | **v0.9.9** | SQLite 3.42 · Postgres 14–18 · MariaDB 10.6–11.8 · MySQL 8.0.44–9.5.0 | North America (Yet Analytics) |
| 🟢 `openfun/ralph` | **MIT** ✅ | **2026-09-07** | **v5.0.1** | Elasticsearch + los 14 extras de `ralph-malph` ya inventariados en `repos/foundations.md` | EMEA (France Université Numérique) |

🔵 **La conclusión de riesgo, y es la que va a una propuesta:** lo congelado no es la telemetría del cliente, es **un
adaptador delgado de ~32 commits** montado sobre dos LRS vivos, permisivos y mantenidos por organizaciones distintas
en dos regiones distintas. **El costo de adoptar la pieza congelada es acotado y medible**, que es exactamente la
condición que **P78** (adoptar una dependencia congelada a propósito) pedía poder verificar antes de recomendarlo.
**P78 deja de ser una receta teórica: `learnmcp-xapi` es su caso medido.**

### 🟢 Las tres altas MIT que cierran el gap 6 — y la mejor de las tres está diseñada como lo pide un regulador

El pase 37 escribió que `peancor` era *«la única pieza permisiva de esta KB que pone nota y devolución dentro de un
LMS»*. **Hoy hay tres, todas MIT, todas con `main` de menos de un mes**, y ninguna estaba en esta base:

| Repo | Licencia (verificada) | `HEAD` | Tools | Qué escribe | Región |
|---|---|---|---|---|---|
| 🟢 **`toshieji/moodle-grading-mcp`** | **MIT** ✅ (WACA + Toshiaki Ejiri, 2026) | **2026-09-07** (24 d) | **9** | `save_grade_draft` → `workflowstate=readyforreview`: **nota NO publicada** | **APAC** (Japón, Web Analytics Consultants Association) |
| 🟢 **`NiccoloSalvini/mcp-moodle-teacher`** | **MIT** ✅ (2026) | **2026-09-25** (6 d) | **22** (15 lectura · 3 escritura · 4 utilidad) | `grade_submission`, `announce`, `mark_attendance`, con confirmación explícita | **EMEA** (Italia) |
| 🟢 **`Dymayo/moodler-mcp`** | **MIT** ✅ (2026) | **2026-09-19** (13 d) | — (no enumeradas este pase) | release 1.1.2, *conventional commits* | Sin región declarada |

🔵 **Y el hallazgo comercial del pase está en la columna «qué escribe» de la primera fila.** `moodle-grading-mcp` no
publica notas: las deja en `readyforreview`. Además, **verificado en su README**: la escritura exige
`MOODLE_ALLOW_WRITE=1`, está **restringida a una allowlist de IDs de curso** (lista vacía = no puede escribir nada),
**loguea cada intento de escritura en un audit trail JSONL**, **no dispara notificación al alumno** y **anexa un pie
de declaración de asistencia por AI** salvo override. 🟢 **Eso no es prolijidad: es exactamente la forma que exige el
régimen de alto riesgo del AI Act para evaluación de alumnos — el humano sigue siendo quien publica** — y es también
lo que piden las reglas de supervisión humana de Oklahoma y Maryland en North America (ver `intel/trends.md`,
**tendencia 133**). **Es la primera vez que esta base encuentra una pieza permisiva cuyo diseño de seguridad es
argumento de cumplimiento y no sólo higiene de ingeniería** (**tendencia 134**).

### ⚠️ Las dos trampas de esta capa, medidas, para que nadie las repita

| Repo | Por qué NO entra | Medición |
|---|---|---|
| ⛔ `csmediapro/moodle-mcp-server` | **AGPL-3.0** y sólo lectura — **es el más activo de todos** (`HEAD` **2026-10-01**, v0.1.7) y por eso es el que más tienta | `LICENSE` en `main` = AGPL-3.0 textual. Confirma el veredicto que la base ya tenía en `agents/top.md` |
| ⛔ `loyaniu/moodle-mcp` | **Sin archivo de licencia** → por defecto, todos los derechos reservados | Probados `LICENSE`, `LICENSE.md`, `LICENSE.txt` y `COPYING` en `main` **y** `master`: **404 en los 8**. `HEAD` 2026-06-28 |

### 🟢 OneRoster: aparece el lado PROVEEDOR, que esta base nunca tuvo — y trae una rareza de gobernanza

`Ed-Fi-Alliance-OSS/edfi-oneroster` — **Apache-2.0**, Node.js, 6 ★, **86 tags**, último **v1.0.2**, `HEAD`
**2026-10-01**. **Sirve una API OneRoster 1.2 desde una base Ed-Fi ODS**: **14 endpoints GET** (`academicSessions`,
`classes`, `courses`, `demographics`, `enrollments`, `orgs`, `users`, `schools`, `students`, `teachers`,
`gradingPeriods`, `terms`, más recuperación por id), con `limit`/`offset`, `sort`/`orderBy`, `filter` y `fields`.
Compatible con **Ed-Fi Data Standard 4.0 y 5.0/5.1/5.2**. Despliegue por **Docker** o IIS/Windows.

⚠️ **La rareza, y hay que saberla antes de nombrar al proyecto en una reunión:** el repo vive en la organización
**Ed-Fi-Alliance-OSS**, pero su aviso de copyright dice **«Copyright (c) 2025 1EdTech Consortium, Inc. and
contributors»**. **Es un artefacto conjunto de los dos consorcios que esta base venía tratando como mundos separados**
— Ed-Fi del lado del dato del distrito, 1EdTech del lado del estándar de interoperabilidad. **Es el primero de esta
KB con esa doble firma** (**tendencia 135**). No declara certificación 1EdTech en el repo: no afirmar que está
certificado.

Acompaña `CSR2017/edfi-oneroster` (**Apache-2.0**, `HEAD` **2026-09-22**, 8 tags), con la misma descripción. 🔴 **La
relación entre los dos —cuál es upstream— NO se determinó este pase: queda como `gap 79`**, y hasta resolverlo hay que
citar el de la Alliance, que es el que tiene 86 tags y commit de ayer.

Y del lado cliente, **`TCI/OneRoster`** — **MIT**, Ruby, **v2.3.27**, `HEAD` **2026-09-11**, 35 tags, 4 ★: wrapper de
consumo (no servidor) para `students`, `teachers`, `classes`, `classrooms`, `courses`, `enrollments`, con filtrado por
`sourcedId`, publicado en rubygems. **Es el reemplazo funcional de `oneroster-ts` para el rol de cliente — pero en
Ruby.** 🔴 **El cliente OneRoster permisivo y vivo en TypeScript no existe**: `oneroster-ts` (0BSD) está congelado y
`@timeback/oneroster` ya fue declarado no-alta en `repos/foundations.md`. **Ese es el residuo honesto del gap, y
conviene decirlo así en una propuesta en vez de prometer paridad de lenguaje.**

### ⚫ Los callejones sin salida, fechados — para que ningún pase los vuelva a buscar

Cinco candidatos de OneRoster y LRS que el barrido devolvió y que **están muertos**, medidos hoy:

| Repo | `HEAD` | Antigüedad |
|---|---|---|
| ⚫ `Transcordia/jupiter` (LRS xAPI + Caliper) | 2015-04-19 | **11,5 años** |
| ⚫ `EASOL/edfi-to-oneroster` | 2016-10-19 | **10,0 años** |
| ⚫ `bgwdotdev/go-oneroster` | 2019-11-04 | **6,9 años** |
| ⚫ `gotranseo/oneroster` (Swift) | 2023-05-01 | **3,4 años** |
| ⚫ `jdolny/OneRoster.NET` | 2023-10-13 | **3,0 años** |

🔵 **El dato de encuadre que dejan juntos:** de las **ocho** implementaciones de OneRoster que devuelve un barrido
abierto, **cinco llevan ≥ 3 años sin un commit**. OneRoster tiene mucho código escrito y poco código mantenido:
**la selección importa más acá que en cualquier otra capa de esta base.**

### Lo que este pase deja abierto

- 🔴 **`gap 78`** — un fork con `main` más nuevo no es sucesión: falta incorporar el conteo de commits adelante/atrás al barrido estándar de vitalidad, como el pase 37 incorporó la distinción de ramas de bot.
- 🔴 **`gap 79`** — cuál de `Ed-Fi-Alliance-OSS/edfi-oneroster` y `CSR2017/edfi-oneroster` es upstream.
- 🔴 **El cliente OneRoster permisivo en TypeScript sigue sin existir.** Es candidato a contribución *upstream* propia, no a búsqueda.
- ⚠️ `Dymayo/moodler-mcp` entró por licencia y fecha; **sus tools no se enumeraron**. Falta pasarlo por el mismo detalle que las otras dos.

## 2026-10-02 (pase 37) — el pase que deja de preguntarle al registro y le pregunta **al árbol de git**: con `git ls-remote` + un *fetch* de profundidad 1, las **49 filas quedan fechadas por su commit de `HEAD`**, y el resultado es que **10 de 49 tienen la rama principal parada hace más de seis meses — tres hace más de un año**, entre ellas **la dependencia más citada de esta KB**

**El instrumento del pase, y es el primero de esta base que no depende de ningún registro ni de ninguna API.** El pase 35
midió adopción con descargas; el 36 encontró que **las descargas sólo existen en Packagist** (`api.npmjs.org` y
`pypistats.org` siguen dando **403 a CONNECT**, reverificado hoy) y las sustituyó por el *span* de releases. 🔴 **Pero el
*span* de releases sólo mide los proyectos que etiquetan releases, y 17 de las 49 filas tienen CERO tags.** Para esas, esta
base no tenía **ningún** instrumento de vitalidad.

🔵 **El que funciona es `git ls-remote` sobre el repo público, más un `git fetch --depth 1` del sha de `HEAD` y
`git log -1 --format=%cI`.** No usa cuota de API, no necesita autenticación, funciona en **las 49 filas** y mide lo único
que ni las estrellas, ni las descargas, ni el *span* de releases pueden medir: **si alguien sigue escribiendo código en la
rama principal.** Verificado: **49 de 49 repos respondieron, cero 404.** 🟢 **Es además el primer control de integridad
completo de esta tabla: no hay una sola URL muerta entre las 49.**

### 🔴 El resultado, y no es cómodo: el 20 % de la tabla tiene la rama principal parada

| Franja | Filas | % |
|---|---|---|
| 🟢 Activo (< 3 meses) | **34** | 69,4 % |
| ⚠️ Tibio (3–6 meses) | 5 | 10,2 % |
| 🔴 Frío (6–12 meses) | 7 | 14,3 % |
| 🔴 **Congelado (> 12 meses)** | **3** | 6,1 % |

**La franja que decide una propuesta son las 10 filas de ≥ 6 meses**, porque esta KB las cita como piezas vivas en
`compose/patterns.md`. Y **tres de esas diez son load-bearing**:

### 🔴 Lo más grave del pase: la dependencia más citada de esta base está congelada hace 13 meses

| Pieza | Licencia | `HEAD` | Antigüedad | Ramas | Dónde pesa |
|---|---|---|---|---|---|
| 🔴 **`DavidLMS/learnmcp-xapi`** | **MIT** | **2025-08-29** | **13,1 meses** | **1 sola** | 🔴 **42 menciones en `compose/patterns.md`** — es la puerta MCP de xAPI de **P4**, **P15**, **P67**, **P68** y **P69**, y el **gap 64** la declaró *«la única puerta»* |
| 🔴 **`trilogy-group/oneroster-ts`** | **0BSD** | **2025-06-27** | **15,2 meses** | 6 (5 de bot) | **P58**, **P60**, **P64**. Es *«la superficie de tools más grande de toda esta base»* (**132 tools**, pase 30) |
| 🔴 **`peancor/moodle-mcp-server`** | **MIT** | **2026-02-22** | **7,3 meses** | 2 | **P54**, **P55**. Es **la única pieza permisiva de esta KB que pone nota y devolución dentro de un LMS** (gap 6) |

**Sobre `learnmcp-xapi` conviene ser exacto, porque es la fila que más cuesta:** se verificó que **tiene una sola rama**
(`main`), así que **no hay desarrollo escondido en otra parte**: el 2025-08-29 es final. ✅ **Y de paso cierra la mitad
*fecha* del gap 63, que el pase 34 declaró incerrable** tras probar *«8 rutas portadoras de versión, las 8 con 404»*:
`ls-remote` entrega los tags y el *fetch* los fecha — **`v1.0.0` = 2025-05-25** y **`v2.0.0` = 2025-06-02**. 🔵 **El gap 63
no era un límite del entorno: era el instrumento equivocado.** Se buscó el número de versión en rutas de archivos cuando
estaba en `refs/tags`.

### 🔵 La distinción nueva, y es la que salva al instrumento de mentir: **la actividad de bot no es mantenimiento**

`oneroster-ts` tiene **6 ramas y la más reciente es del 2026-05-11** — a cuatro meses, no a quince. **Un instrumento que
tomara el ref más nuevo lo habría declarado vivo.** Pero las ramas son: cuatro `dependabot/npm_and_yarn/*` y una
`speakeasy-sdk-regen-1746144633`, **ninguna mergeada**. Lo mismo en `satvik314/educhain`: `main` está en **2025-12-03** y
el tip más nuevo (**2026-05-29**) es una rama **`claude/relaxed-curie-mNW2l`**, o sea generada por un agente y sin mergear.

🔵 **La regla que esto deja, y aplica a todo barrido futuro de esta base: se fecha el *tip de la rama por defecto*, nunca
el ref más nuevo.** Dependabot, los regeneradores de SDK y las ramas de agente mantienen vivo el grafo de refs de un
proyecto que nadie atiende. **En `oneroster-ts` lo único que se movió en quince meses lo escribió una máquina, y nadie lo
mergeó** (tendencia **124**, **gap 72**).

### 🔴 Corrección al pase 36: `pykt-toolkit` NO está abandonado, y el error es exactamente el que esta KB ya tenía escrito

El pase 36 escribió sobre `pykt-team/pykt-toolkit`: *«🔴 **2022-10-16** — **Cuatro años.** *Backlink* verificado: **es
abandono, no colisión**»*, y lo metió en las propuestas de *knowledge tracing* con esa etiqueta. **Es falso.**

| Canal | Qué dice |
|---|---|
| PyPI (pase 36) | último release **2022-10-16** |
| Tags de git (los 5, fechados hoy) | `v0.0.34-alpha` 2022-06-09 … **`v1.0.0` 2023-02-10** |
| 🟢 **`HEAD` de la rama por defecto** | 🟢 **2026-09-22** — `Merge pull request #305`, `feat: add cgmkt model`, `feat: add cgmkt sweep config` |

🟢 **Está vivo en `main` y congelado en el registro — y son *feature commits*, no mantenimiento cosmético.** ⚠️ **Es la
segunda aparición del patrón que esta base ya había nombrado con Ralph en el pase 33** (*«vivo en `main` y parado en el
registro → se instala desde git, no desde PyPI»*). **El pase 36 tenía la regla escrita y no la aplicó, porque sólo tenía
el instrumento del registro.** 🔵 **Ahora hay instrumento, y la regla pasa a ser verificable en vez de anecdótica:
el registro puede decir «abandonado» de un proyecto activo, y el único canal que no se equivoca es el árbol** (tendencia
**125**).

### ⚠️ Un límite del instrumento, declarado antes de que alguien lo use mal

**El «último tag» por orden de versión NO es confiable, y el commit de `HEAD` sí.** Donde los nombres de tag son
heterogéneos, `sort -V` elige mal: `jupyterlab/jupyter-ai` tiene **279 tags** y el «mayor» es un tag de monorepo de
**2023**, con `HEAD` en **2026-10-01**; `LabSirius/TutorIA` tiene un tag `informe-minciencias-2026-09` **posterior** a su
propio `HEAD`. **Las fechas de `HEAD` de este pase son medidas; las de «último tag» son orientativas y no deben citarse a
un cliente** (**gap 73**).

### 🔴 Y una corrección de método sobre la API de GitHub, porque un probe mal leído habría llenado esta KB de basura

El pase 36 de la KB hermana anotó *«github-api-proxy-blocked»*. **Medido hoy: `api.github.com/rate_limit` devuelve `200`
con `limit: 15000`.** 🔴 **Pero `api.github.com/repos/HKUDS/DeepTutor` devuelve `200` en la capa HTTP y un cuerpo que dice
`"GitHub access to this repository is not enabled for this session"`.** 🔵 **No es un bloqueo de red: es una compuerta de
alcance, y devuelve el error en el cuerpo, no en el código.** Un barrido que midiera `%{http_code}` —como hace el resto de
los probes de esta base— **habría registrado «funciona» y escrito 49 filas de campos vacíos.** La API sólo responde por
los repos adjuntos a la sesión, así que **sigue sin ser un instrumento usable para esta tabla**, y `ls-remote` lo
reemplaza sin cuota (tendencia **126**, **gap 74**).

### 🔴 El hallazgo de método más importante del pase, y descalifica el verificador que esta familia de KBs tiene prescripto

**La consigna de ingesta dice «verificar cada URL antes de escribirla (`curl -sI`)». Medido hoy: ese control no funciona en
este entorno, y falla de la única manera que no se puede detectar — devuelve lo mismo para una URL buena y para una
inexistente.**

| URL probada con `curl` | Código |
|---|---|
| `github.com/torvalds/linux` (existe) | **403** |
| `github.com/moodle/moodle` (existe) | **403** |
| `github.com/pie-framework/pie-elements` (existe) | **403** |
| 🔴 **`github.com/this-org-does-not-exist-zzz9/nope` (NO existe)** | 🔴 **403** |

🔴 **El HTML de `github.com` está bloqueado en bloque: las cuatro dan 403, y la cuarta no existe.** Un barrido que use
`curl -sI` sobre `github.com` **no puede distinguir un repo real de un 404**, así que cualquier «verificación de URL» hecha
por ese canal en esta o en otra KB de esta familia **no verificó nada** — y según cómo se interprete el 403 produce **o
bien filas inventadas aceptadas como válidas, o bien repos reales descartados como muertos.**

🟢 **El discriminador que sí funciona es `git ls-remote`, y lo hace con control negativo limpio:**

- `git ls-remote https://github.com/pie-framework/pie-elements` → **51.410 refs**
- `git ls-remote https://github.com/this-org-does-not-exist-zzz9/nope` → 🔴 **`fatal: could not read Username for 'https://github.com'`** (GitHub pide credenciales para lo que no existe o es privado)

🔵 **La regla, y reemplaza la de la consigna para todo repo de GitHub: la existencia de un repo se verifica con
`git ls-remote`, nunca con `curl` sobre `github.com`.** Los otros dos canales que discriminan son
`raw.githubusercontent.com` (200 por archivo real) y el registro de paquetes. ✅ **Las 49 filas de esta KB quedaron
verificadas por el canal correcto en este pase** (tendencia **131**, **gap 77**).

### Lo que NO se encontró, declarado como tal

**Cero altas de agentes, por quinta vez consecutiva, y el barrido completo lo dice.** Las cuatro búsquedas globales con el
año **calculado** (`2026`) devolvieron otra vez **la capa genérica** —OpenClaw (385.407 ★), browser-use (108.128 ★), Dify
(151.639 ★), Mem0 (62.735 ★), AutoGen (60.284 ★), Flowise (55.226 ★), CrewAI, LangGraph, Aider, Cline— más **material
didáctico *sobre* AI** (`ai-engineering-from-scratch`, #1 en GitHub Trending del 2026-05-24; `agents-from-scratch`;
`free-ai-agents-resources`; cursos de DeepLearning.AI). ✅ **Quinta confirmación directa de la causa que midió el pase 23**:
en GitHub `education` nombra al material que **enseña AI**, no al software que **educa**.

⚠️ **Un nombre nuevo que aparece y NO entra, con la razón:** **Hermes Agent** (Nous Research), que las fuentes dan como
**MIT** y **~180.000 ★ desde su lanzamiento de febrero de 2026**. **No es educativo** — es un agente general *local-first*.
Entra en el encuadre de capa genérica, **no en esta tabla**.

### 🔴 El candidato de registro que no entra, y la razón es que no tiene licencia

`@timeback/oneroster` (**58 versiones**, última **2026-09-25**) apareció buscando reemplazo para `oneroster-ts`.
🔴 **No declara licencia (`license: None`), no declara repositorio y no declara *homepage*.** ⚠️ **Es la cuarta vez que
esta base encuentra una pieza del dominio sin licencia declarada, y la regla no cambia: sin licencia no es open source,
es código publicado.** No entra; queda como ausencia declarada (**gap 75**).

### ⚠️ Dos límites del buscador de npm, medidos, que explican barridos anteriores de esta base

- 🔴 **Las consultas de dos palabras se resuelven como OR y se ordenan por descargas:** `xapi mcp` devuelve
  **110.769** resultados encabezados por `@modelcontextprotocol/sdk` y `@storybook/addon-mcp`. **El paquete del dominio
  queda sepultado.**
- 🔴 **El calificador `scope:` NO está soportado:** `text=scope:pie-element` devuelve **2.403.867** resultados y la
  primera página son `locate-path`, `strip-ansi`, `@types/node`. **Hay que pedir el paquete por nombre exacto.**

🔵 **Juntos explican por qué el barrido por registro del pase 35 rindió poco fuera de Packagist, y la regla es: el registro
sirve para CONFIRMAR un nombre que ya se tiene, no para DESCUBRIR** (tendencia **127**).

### 🔵 Las tres acciones que este pase deja escritas para el 38

**Las tres salen del instrumento nuevo y las tres son baratas, porque `ls-remote` cuesta un *round-trip* por repo y no
consume cuota.**

1. 🔴 **Fechar por rama por defecto los repos que esta KB cita FUERA de `agents/top.md`** — `repos/foundations.md` y
   `verticals/solutions.md` tienen piezas que nunca pasaron por este control: `cassproject/CASS`, `1EdTech/OpenCASE`,
   `instructure/qti`, `yetanalytics/datasim`, `oat-sa/tao-core`, la pila `qti3-*`, Ralph, `lrsql`, los tres LRS y las
   plataformas (Moodle, Open edX, ILIAS, Chamilo, OpenEduCat, Frappe). **Este pase midió 49 filas; la base cita bastante
   más de 49 repos.** La acción concreta: correr el mismo barrido sobre los slugs de esos dos archivos y **publicar las
   frías**, porque son las que sostienen `P15`, `P50`, `P57`, `P60`, `P66`, `P70` y `P71`.
2. 🔵 **Ejecutar `P78` sobre la pieza más chica para convertir la estimación en un número medido: `learnmcp-xapi`, 3 tools.**
   Clonar, correr su suite si tiene, escribir el test de contrato de las 3 tools contra un `lrsql` local —que está vivo,
   `v0.9.9` del 2026-10-01— y **cronometrar**. Esta KB estima **1-2 semanas** para ese fork; **es la única estimación de
   `P78` que se puede verificar en una tarde**, y si el número real se aparta hay que corregir las otras dos.
3. ⚠️ **Resolver si `pie-elements` es proponible de verdad, que es lo que el alta de este pase dejó a medias.** Lo medido
   es licencia, vitalidad y catálogo; **lo que decide una propuesta es el contrato de *scoring***. La acción: leer el
   `controller` de **dos** interacciones (`multiple-choice` y `rubric`) y responder **si el *scoring* es puro y portable o
   si depende del *runtime* de `pie-player`** — porque de eso depende si se puede usar como motor de evaluación detrás de un
   agente, o si sólo sirve como UI. 🔴 **Y de paso resolver la licencia de `@pie-element/multiple-choice`, que no declara
   ninguna** (**gap 76**).

## 2026-10-02 (pase 36) — el pase que **mide las 49 filas en vez de seis**, y encuentra que la tabla tenía **una fila repetida** que ningún conteo anterior podía ver: el agente con **la cadencia más alta del archivo tiene 60 estrellas y 240 releases**, y dos piezas que esta KB cita como vivas no publican desde **2022** y **2025**

**Acción 1 del pase 35, ejecutada sobre la tabla completa.** Para cada repo se leyó el manifiesto publicado desde
`raw.githubusercontent.com`, se extrajo el nombre de paquete **declarado por el propio repo** y se consultó el registro,
**verificando el *backlink* registro → repo en cada coincidencia**. Detalle completo en `agents/top.md`, sección
*Capa de despliegue medida*.

### 🔴 Lo primero, porque es un defecto de esta KB y no del mercado: `Claw-ED` estaba DOS VECES

`SirhanMacx/Claw-ED` figuraba con **59 ★** y con **60 ★** — mismo repo, dos filas. El pase 35 lo contó como alta cuando
ya había entrado *«en la tercera pasada del 2026-09-30»*, **frase escrita en el historial del mismo archivo**. El conteo
programático del pase 30 informó «52 filas» y **tenía razón**: había 52 filas. Lo que no había era 52 repos.
🔵 **Un conteo de FILAS no puede detectar una fila repetida.** Fila eliminada; el número pasa a **51 filas = 49 repos de
GitHub distintos + 2 entradas de PyPI**, y de acá en adelante el conteo que vale es el de **slugs distintos**
(**gap 71**, tendencia **116**).

### 🟢 Pocas estrellas, tracción real — las filas que se suben

| Repo | ★ | Paquete | Releases | Última | Lectura |
|---|---|---|---|---|---|
| `SirhanMacx/Claw-ED` | **60** | `clawed` (PyPI) | 🟢 **240** | 2026-09-19 | **La cadencia más alta de la tabla, con uno de los conteos de estrellas más bajos de su vecindario.** *Backlink* verificado |
| `bruchris/canvas-lms-mcp` | **8** | `canvas-lms-mcp` (npm) | **62** | 2026-09-20 | ✅ **Confirma la promoción del pase 35 por un segundo instrumento.** `v1.30.0`, **MIT leído en el registro**, 62 releases en 5 meses |
| `bunizao/moodle-cli` | — | `moodle-cli` (npm) | **20** | 2026-09-27 | `v0.9.6`, MIT en registro, 20 releases en menos de 3 meses |
| `Miaotofu01/Study-Mate` | 482 | `@yunmiao/studymate` (npm) | 8 | 2026-09-30 | **8 releases en 8 días** — real pero **nuevo**, no maduro |

### 🔴 Estrellas sin tracción — las filas que se marcan

| Repo | ★ | Paquete | Última publicación | Lectura |
|---|---|---|---|---|
| `pykt-team/pykt-toolkit` | **441** | `pykt-toolkit` (PyPI) | 🔴 **2022-10-16** | **Cuatro años.** *Backlink* verificado: es abandono, no colisión. Entra en las propuestas de *knowledge tracing* de esta KB |
| `satvik314/educhain` | 389 | `educhain` (PyPI) | ⚠️ **2025-12-03** | **~10 meses.** Esta base lo cita como pieza viva **desde el ciclo 2** |
| `MarcosNahuel/moodle-mcp` | 1 | `@nahuelalbornoz/moodle-mcp` | ⚠️ **2026-04-23** | **8 releases en 4 días y nada en 5 meses:** el patrón *ráfaga y silencio* |
| `moon0825/jbnu-lms-student` | — | `jbnu-lms-mcp` (npm) | 2026-09-08 | **2 releases el mismo día.** Alta del pase 35, **no maduro** |

### 🔴 Dos colisiones nuevas, y de clase más peligrosa que las nueve anteriores

Las nueve colisiones previas eran del **buscador**. **Estas dos no:** el nombre vino **del manifiesto del propio repo**,
la fuente más autoritativa posible, y apuntaba a otro software.

- **Colisión 10 — `tero`:** `marcorojasb/tero` declara `tero`; el `tero` de PyPI es *«Configures development machines to cloud resources»* (`djaodjin/drop`).
- **Colisión 11 — `mcp-server`:** `paulocymbaum/ed-tech-system-mcp` declara el nombre genérico **`mcp-server`**, tomado por un tercero sin `project_urls`.
- ⚠️ **Confirmación débil declarada:** `avps82/mentar` → `mentar` **sin `project_urls`**; se acepta por coincidencia de descripción y **se marca**.

🔵 **La regla nueva: la genericidad del nombre declarado es un predictor de colisión evaluable sin red** (tendencia **119**).

### Lo que NO se encontró, declarado como tal

**Cero altas de agentes este pase, y es el barrido completo el que lo dice:** las cuatro búsquedas globales con el año
**calculado** (`2026`) devolvieron, por cuarta vez consecutiva, **la capa genérica de la industria** —OpenClaw (~388 k ★),
OpenHands, CrewAI, LangChain, AutoGen— más **material didáctico *sobre* AI** (`500-AI-Agents-Projects`,
`awesome-ai-agents-2026`, cursos de DeepLearning.AI / HuggingFace / Microsoft). ✅ **Es la confirmación directa de la causa
que el pase 23 midió:** en GitHub el término `education` está capturado por el material que **enseña AI**, no por software
que **educa**. Los dos candidatos nuevos que aparecieron por nombre —`HugeCatLab/ChatTutor` y `TovTechOrg/Tov-learn`— **el
primero ya está en esta tabla** (AGPL-3.0, 1,3 k ★) y el segundo es **una skill de Claude Code**, o sea la clase que la
tendencia **120** describe: **no se distribuye como paquete y medir su adopción por registro es la pregunta equivocada**.

## 2026-10-02 (pase 35) — el pase que **mide la adopción con el instrumento que treinta y cuatro pases no usaron**: las descargas del registro. Y el instrumento da vuelta tres filas de esta KB, entre ellas **cuál es el conector de LMS más grande que tiene** (tiene 8 ★) y **si la puerta oficial de Open edX está viva** (no publicó nada en 70 días)

⚠️ **Nota de concurrencia, primero, porque explica la numeración.** Esta corrida arrancó cuando el último pase
publicado era el **32**, y mientras medía se publicaron el **33** y el **34**. **Las tres corridas trabajaron en paralelo y
sin verse**, sobre la misma consigna del pase 32. Este pase **se renumeró a 35 al publicar**, **no reescribió nada de las
otras dos**, y **resolvió los choques diciendo cuál gana**: donde las mediciones coinciden —el bloqueo de `eur-lex` y
`data.europa.eu`, el cierre en negativo del **gap 51**, la imposibilidad de ejecutar `tools/list` en este entorno, y las
**15 tools de `coursecode`** leídas por dos canales distintos— **la coincidencia vale como confirmación independiente**;
donde no —la mitad xAPI del **gap 60**, el conteo de escrituras de `coursecode`— se acepta la corrección ajena o se
publican los dos criterios con su regla. **Los gaps nuevos de este pase son 68, 69 y 70**; el **65** es del pase 34 y acá
sólo se le agrega evidencia.

**Lo que se hizo:** el barrido obligatorio completo —**cuatro búsquedas globales y cuatro regionales**, con el año
**calculado** (2026); las cuatro regiones rindieron— más **las tres acciones que el pase 32 dejó escritas**. Las tres se
ejecutaron. La 2 **se contestó contra la expectativa del pase que la pidió** y cerró a favor; la 3 rindió **cinco altas
y tres colisiones nuevas**; la 1 🔴 **no se pudo cerrar y ahora se sabe que no se va a poder cerrar desde este entorno**,
que es un resultado distinto de «no se intentó».

🔵 **Pero el hallazgo del pase no es ninguna de las tres: es un instrumento.** Esta base midió adopción con **estrellas**
durante treinta y dos pases, y escribió la tendencia 23 (*«las estrellas esconden la infraestructura desplegada»*) sin
tener con qué medir lo que escondían. El registro de paquetes publica **descargas por mes**, y eso **sí** mide
despliegue. Las dos series no se parecen, y no se parecen **en los dos sentidos**.

### 🔵 El instrumento nuevo: ★ contra descargas/mes, medido en las piezas que esta KB ya tenía

| Pieza | ★ | Descargas (total / mes) | Último tag | Lectura |
|---|---|---|---|---|
| `learninglocker/learninglocker` | **583** | **2.960 / 0** | **2017-04-04** | 🔴 **583 estrellas y cero descargas mensuales.** La demostración más limpia de la tendencia 23: la atención persiste, el despliegue es nulo |
| `RusticiSoftware/TinCanPHP` | 88 | **863.777 / 6.178** | **2019-03-05** | 🔵 **Setenta veces más descargas mensuales que estrellas, y sin release en siete años.** Es la librería xAPI más desplegada de esta KB — **y es Apache-2.0** |
| `oat-sa/qti-sdk` (`qtism/qtism`) | 85 | **218.212 / 3.104** | 2026-07-09 | 🔴 **El QTI más desplegado del mundo es GPL-2.0-only.** 293 versiones etiquetadas, activo |
| `oat-sa/extension-tao-testqti` | **8** | **117.544 / 950** | **2026-09-30** | 🔴 8 estrellas, **844 versiones** y un release de hace dos días. TAO es infraestructura, no proyecto |
| `php-xapi/client` | 23 | 48.104 / 825 | 2021-03-24 | **MIT**, modular, congelado hace cinco años pero con tráfico vivo |

**La regla que esto deja, y aplica a toda esta base:** **las estrellas miden interés; las descargas por mes miden
despliegue.** Cuando las dos series se contradicen, la que decide una propuesta es la segunda. Y los dos extremos de
esta tabla son el argumento: **583 ★ / 0 descargas** contra **8 ★ / 950 descargas por mes**.

### 🔴 La misma inversión, en la fila que más le importa a esta KB: el conector de LMS más grande tiene 8 estrellas

El pase 26 declaró a `vishalsachdev/canvas-mcp` (**MIT**, 269 ★, «102–103 tools») **el conector permisivo de LMS más
grande que vio esta KB**, y el pase 27 agregó una *advertencia de cifra* porque el número de tools variaba según la
versión (40+, 80+, 116). **La advertencia era correcta y el título caducó.**

| Conector Canvas | Licencia | ★ | Tools | Escribe | Commits / versiones |
|---|---|---|---|---|---|
| 🟢 **`bruchris/canvas-lms-mcp`** | **MIT** ✅ | **8** | 🔵 **165** | **Sí** — califica, comenta, crea/actualiza assignments, administra contenido y *admin workflows* | **317 commits**, **62 versiones** en npm, última **2026-09-20** |
| `vishalsachdev/canvas-mcp` | **MIT** ✅ | **269** | 102–103 (cifra inestable) | Sí | 815 commits |
| `mtgibbs/canvas-lms-mcp` | **MIT** ✅ | — | — | Consulta notas, entregas, datos académicos | 15 versiones, última 2026-02-13 |
| `owentaylor/canvas-mcp` | **MIT** ✅ | — | — | — | 2 versiones, 2026-02-23 |
| `@imazhar101/mcp-canvas-server` | 🔴 **sin licencia declarada** | — | — | — | 13 versiones, última **2026-10-01** — **se excluye por licencia ausente** |

**Descripción verbatim de la pieza nueva:** *«The TypeScript MCP server for Canvas LMS. Read courses, assignments,
submissions, rubrics, quizzes; grade, comment, manage course content, and handle Canvas admin workflows from any AI
agent.»* Las **165** tools cubren, entre otros: *courses, assignments, assignment overrides, submissions, rubrics,
quizzes, **New Quizzes (LTI)**, files, **gradebook history**, grade explanations, grading policy, grade projection,
grading standards, users, groups, enrollments, discussions, modules, pages, calendar, conversations, peer reviews,
accounts, analytics, outcomes, content exports, course setup, link audits, **accessibility audits**, appointment groups,
student workflows, student search, dashboard* e *instructor attention workflows*.

🔵 **Y resuelve la advertencia de cifra del pase 27 en vez de heredarla:** acá el número **165** aparece igual en el
campo `description` del paquete y en el README, sobre 62 versiones publicadas. **Es una cifra citable**, a diferencia de
la de `canvas-mcp`. 🔵 **Dos detalles que valen para una propuesta:** declara **MCP 1.x** (versión de protocolo, no
«compatible con MCP»), y trae **`accessibility audits`** como categoría propia — el único conector de LMS de esta base
que expone auditoría de accesibilidad como herramienta, que es exactamente lo que **P17** y **P72** necesitaban del lado del LMS.

⚠️ **Lo que no se midió:** `tools/list` **no se observó**. El **165** viene del `description` del paquete y del README,
no del protocolo — la misma distinción que el pase 30 estableció con `oneroster-ts` (132 servidas contra 164
declaradas). **No se cita como «165 servidas».**

### 🔴 Gap 62 (nuevo) — la puerta oficial de Open edX **no publicó nada en 70 días**, y eso no lo midió ninguno de los tres pases que la celebraron

El pase 30 cerró el gap 48 con `openedx-mcp` + `tutor-contrib-openedxmcp` y construyó **P61** encima; el 31 midió sus 35
rutas; el 32 leyó su código. **Ninguno miró las fechas de publicación.** Leídas del JSON de PyPI:

| Paquete | Releases | Ventana de publicación | Silencio hasta hoy | Versión |
|---|---|---|---|---|
| `openedx-mcp` | **5** (0.1.1 → 0.1.5) | **2026-07-24 → 2026-07-25** | 🔴 **70 días** | **0.1.5** |
| `tutor-contrib-openedxmcp` | **7** (0.1.1 → 0.1.7) | **2026-07-24 → 2026-07-25** | 🔴 **70 días** | **0.1.7** |

🔴 **Doce releases en dos días y nada en los setenta siguientes, con la versión todavía en `0.1.x`.** Esa es la forma de
un **experimento publicado una vez**, no de un producto mantenido. **No invalida nada de lo medido** —las 35 rutas, los
19 escritores, los cuatro rails siguen siendo ciertos y los rails siguen siendo el artefacto más reutilizable de esta
base—, pero **cambia cómo se cotiza P61**: una propuesta que dependa de esta puerta tiene que presupuestar
**mantenerla**, no consumirla. **Y es barato de volver a chequear:** es una llamada al JSON del registro.

🔵 **La regla general que esto deja:** cuando esta KB promueve una pieza a dependencia de patrón, la fecha que importa
**no es la del primer release, es la del último** — y la distancia entre las dos es lo que dice si hay proyecto.

### ✅ Acción 2 CUMPLIDA — y contestó **contra** la expectativa: `coursecode` **sí** es la pieza de salida, porque su `build` **emite el paquete**

El pase 32 preguntó si las tools de `coursecode` leen o si alguna escribe, y si eso lo convierte en la pieza de salida
de la capa generativa o lo deja como «un CLI con fachada MCP». **Medido sobre `lib/mcp-server.js` y `lib/mcp-prompts.js`
del árbol `main`: 15 tools declaradas en el array que sirve `ListToolsRequestSchema` — 9 de sólo lectura y 6 que no.**

| Tool | Modo | Anotación | Qué hace |
|---|---|---|---|
| `coursecode_state` | READ | idempotente | Estado del curso + diagnósticos del preview en una llamada |
| `coursecode_errors` | READ | idempotente | Diagnósticos sin el *payload* pesado de estado |
| `coursecode_screenshot` | READ | idempotente | Captura JPEG del preview |
| `coursecode_workflow_status` | READ | idempotente | Detecta la etapa de autoría y devuelve instrucciones de etapa |
| `coursecode_lint` | READ | idempotente | *Linter* estático con resultados estructurados |
| `coursecode_css_catalog` · `_component_catalog` · `_interaction_catalog` · `_icon_catalog` | READ | idempotentes | Catálogos de CSS, componentes, interacciones e iconos |
| `coursecode_navigate` | WRITE | idempotente | Navega a una diapositiva; fija tema claro/oscuro y alto contraste |
| `coursecode_interact` | WRITE | — | Fija **y evalúa** una respuesta de interacción en una llamada |
| `coursecode_reset` | WRITE | 🔴 **destructiva** | Borra el estado del alumno y reinicia el curso |
| `coursecode_viewport` | WRITE | idempotente | Tamaño de viewport del navegador headless (prueba responsive) |
| 🟢 **`coursecode_build`** | **WRITE** | idempotente | 🔵 **`format` es un enum: `cmi5` \| `scorm2004` \| `scorm1.2` \| `lti`** — **el empaquetado LMS está detrás de MCP** |
| `coursecode_narration` | WRITE | — | Genera (o *dry-run*) narración de audio por TTS configurado |

⚠️ **Reconciliación con el pase 33, que midió lo mismo en paralelo y por otro canal — y conviene asentarla porque las dos
lecturas se publican el mismo día.** El pase 33 bajó el **tarball de `coursecode@0.1.61` de `registry.npmjs.org`** y leyó
el artefacto publicado; este pase leyó **`main` por `raw.githubusercontent.com`**. 🔵 **Las dos coinciden en todo lo que
decide:** **15 tools definidas**, **15 casos de dispatch** (o sea **cero *aliasing* y cero supresión** — a diferencia de
`oneroster-ts`), el `enum` de `coursecode_build`, y la conclusión de que **`coursecode` es la pieza de salida y no un CLI
con fachada**. **Dos canales independientes, mismos números: es la verificación más fuerte que puede tener una cifra en
esta base.**

🔴 **Donde difieren es en el conteo de escrituras, y la diferencia es de criterio, no de medición — así que se publican
los dos con su regla:**

| Criterio | Cuenta | Qué incluye |
|---|---|---|
| **Anotación del protocolo** (este pase): tools **sin** `readOnlyHint: true` | **6** | `_navigate`, `_interact`, `_reset`, `_viewport`, `_build`, `_narration` |
| **Efecto persistente** (pase 33): tools que dejan un artefacto en disco | **2** | `_build` (paquete LMS en `dist/`) y `_narration` (**MP3 en `course/assets/audio/`, vía proveedor TTS pago**) |

🔵 **Las dos son correctas y sirven para cosas distintas.** Para **revisar permisos** de un agente, el número que importa
es **6**: `_reset` borra el estado del alumno y `_interact` lo modifica, y aunque nada de eso sobreviva al proceso,
**sí altera lo que el alumno ve**. Para **cotizar riesgo de artefacto y costo**, el número es **2**, y el que cuesta
dinero es `_narration`. ⚠️ **Dato del pase 33 que esta lectura no tenía y que hay que conservar: el `LICENSE` del
artefacto dice *«Copyright (c) 2026 Seth Vincent»*** — la licencia MIT está verificada en el artefacto publicado, no sólo
en el repo.

🟢 **La respuesta, y es un sí:** `coursecode_build` **acepta el formato de LMS como parámetro de entrada**, así que la
generación de **SCORM 1.2, SCORM 2004, cmi5 y LTI** es alcanzable por protocolo, no sólo por CLI. **`coursecode` pasa a
ser la pieza de salida de la capa generativa de esta KB**, y es un **superconjunto estricto** de
`giacomomaria81/scorm-mcp-server` (3 tools, sólo SCORM), que queda como la opción mínima y *offline*.

🔵 **La forma del servidor vale aparte:** normaliza errores a **códigos de dominio con *hint* accionable**
(`preview_not_running`, `invalid_slide_id`, `invalid_arguments`, `unknown_tool`, `tool_failed`) y devuelve
`structuredContent` además del texto. **Es la segunda vez que esta KB encuentra ingeniería de rails reutilizable en una
pieza educativa** —la primera fueron los cuatro rails de `openedx-mcp`— y esta es **MIT**.

⚠️ **Tres límites declarados.** (a) **No se ejecutó**: el conteo es por **lectura de código fuente**, igual que el pase
30 con el sdist de `openedx-mcp`; `tools/list` sigue sin observarse y en este entorno **la instalación de paquetes de
terceros no está disponible**. (b) El CLI tiene **33 comandos** y la superficie MCP expone 15: lo que queda afuera
incluye `convert`, `import`, `export`, `html`, `upgrade` y **toda la capa de despliegue** (`login`, `deploy`, `promote`,
`courses`, `token`, `preview-link`, `delete`) — 🔴 **el paquete MIT trae cliente de un servicio alojado multi-tenant con
CDN; la superficie de agente es local, el CLI no.** (c) El `--no-zip` del CLI **no** está en la tool de build.

### ✅ Acción 2, segunda mitad: `qti3-cli` es envolvible como MCP, y ahora está medido en vez de afirmado

El **gap 60** sostenía que `qti3-core` «no tiene dependencias y ya expone parser, validación y *scoring*», **sin haberlo
abierto**. Abierto: **`@longsightgroup/qti3-cli` 0.13.1 (MIT)**, `bin: { qti3 }`, **cero dependencias de terceros en
runtime**, y **catorce comandos que emiten JSON**:

`parse`, `validate`, `score --responses`, `score-correct`, `prepare-delivery [--mode static|server-materialized-adaptive] [--state] [--out]`,
`inspect-package`, `validate-package`, `certification import-basic-items`, `certification verify-validator`,
`certification check-import-report`, `certification import-basic-tests`, `write-fixtures`, `support-matrix`, `a11y-proof`.

🔵 **Por qué el «en días» se sostiene:** **cada comando ya devuelve JSON** (*«emits the parsed item model as JSON»*,
*«emits validation diagnostics as JSON»*, *«emits the complete scoring result, including diagnostics, state, responses,
outcomes, and score»*), así que el envoltorio **no necesita capa de parseo** — el mapeo es 1:1 comando→tool y el corte
lectura/escritura ya está dado: **doce leen** y sólo `prepare-delivery --out` y `write-fixtures` escriben a disco.
**Sigue siendo la contribución *upstream* más limpia que tiene esta base** (**gap 64**), y ahora con el inventario de
tools ya escrito.

⚠️ **Y una advertencia de cotización que el gap 60 no tenía:** `prepare-delivery` distingue **modo estático** (default,
y **rechaza** un archivo de estado) de **`server-materialized-adaptive`**, que **exige** un objeto de estado con
`outcomes`. **Lo adaptativo no es un flag, es un contrato de estado del lado servidor** — es trabajo de integración, no
de configuración.

### ✅ Acción 3 CUMPLIDA — y el método del pase 32 **funciona a medias, con una regla que lo explica**

El pase 32 descartó por escrito atacar el registro por el **nombre del estándar** (gap 51: `"competencies and academic
standards exchange"` → 1.696.870 objetos de ruido) y mandó atacarlo por el **nombre del proyecto implementador**.
Ejecutado sobre **npm, PyPI y Packagist** con `OpenCASE`, `CASS`, `learning_locker`, `TinCanPython` y `qti3`:

| Nombre consultado | npm | PyPI | Packagist | Veredicto del método |
|---|---|---|---|---|
| `CASS` | ✅ **`cassproject` 5.0.19** (Apache-2.0, 2026-08-12) | — | 🔴 **26.726 objetos de ruido** (Cassandra, cassowary, cassis) | **Funciona en npm, falla en Packagist** |
| `qti3` | ✅ **12 paquetes `@longsightgroup/qti3-*`** (MIT, 0.13.1) | — | — | **Funciona** |
| `TinCanPython` | 🔴 0 resultados | ✅ **`tincan` 1.0.0** (Apache-2.0) | ✅ **`rusticisoftware/tincan`** (Apache-2.0) | **El nombre del repo no es el nombre del paquete** |
| `learning_locker` | ⚠️ `learning_locker` 2.0.7 (**2017**) | — | ⚠️ `learninglocker/learninglocker` (**0 descargas/mes**) | **Funciona, y lo que encuentra está muerto** |
| `OpenCASE` | 🔴 ruido (`opencase` de 2017, sin relación) | 🔴 ausente | 🔴 **`OpenCage` (geocodificación)** | **Falla en los tres** |

🔵 **La regla que explica el patrón, y es nueva:** el nombre del implementador desambigua **sólo cuando el publicador usó
el nombre de la organización del proyecto como nombre de paquete** (`cassproject`, `@longsightgroup/*`) **o el término
del dominio** (`tincan`). Cuando el proyecto se llama como una palabra corta y común (`CASS`, `OpenCASE`), **colisiona
igual que el estándar** — el problema del gap 51 **no era el nivel de nombre, era el largo del nombre.** **Lo que sí
desambigua siempre es el *scope* o el prefijo de organización**, y esa es la consulta que hay que escribir.

### 🔴 Colisiones de término **7, 8 y 9** — y una es cripto otra vez

| Término | Qué devuelve | Dónde |
|---|---|---|
| `opencase` | 🔴 **OpenCage** — geocodificación (`opencage/geocode`, 568.555 descargas) y `opencafe/datium` | Packagist |
| `cass` | 🔴 **Apache Cassandra** y `cassowary` (solver de restricciones) — **26.726 objetos** | Packagist |
| `censo-escolar` | 🔴 **Censo Custody** — **billetera Solana** (`@censo-custody/solana-wallet-adapter`, `@censo/eth-contracts`) | npm |

🔵 **La novena colisión repite el patrón de la quinta y la sexta:** el pase 32 encontró que las dos piezas llamadas
«xapi» eran **cripto/Web3** y **forex**. Acá, el término del censo educativo brasileño devuelve **custodia de
criptoactivos**. **Tres de las nueve colisiones de esta KB son con el vocabulario cripto**, y las tres pasan el filtro de
licencia porque son MIT y están activas. **El único control que las atrapa sigue siendo abrir el README y contar
vocabulario del dominio.**

### ⚠️ Pero el control de la tendencia 96 tiene un falso negativo medido, y hay que acotarlo

Aplicado a las cinco piezas de la acción 3, el conteo de vocabulario del dominio sobre el README crudo dio:

| Pieza | Vocabulario del dominio | ¿Es del dominio? |
|---|---|---|
| `oat-sa/qti-sdk` | **84 apariciones** | Sí |
| `oat-sa/extension-tao-testqti` | 12 | Sí |
| `php-xapi/client` | 15 | Sí |
| `RusticiSoftware/TinCanPHP` | **2** | **Sí** |
| `cassproject/cass-npm` | 🔴 **0** | 🔴 **Sí** — es el SDK de *Competency and Skills Service* |
| `RusticiSoftware/TinCanPython` | 🔴 **0** | 🔴 **Sí** |

🔴 **Dos piezas que son del dominio puntúan cero**, porque su README es un *quickstart* de SDK (instalar, importar,
llamar) sin prosa. **La tendencia 96 es por lo tanto asimétrica y hay que usarla así: sirve para RECHAZAR, nunca para
ACEPTAR.** Un cero no dice «no es del dominio», dice «el README no alcanza para decidir» — y entonces hay que leer el
`package.json`, el `LICENSE` y el árbol, como se hizo acá.

### 🔴 Gap 60 CONFIRMADO por un segundo método independiente: QTI y xAPI siguen sin puerta MCP

Abiertos los **README crudos** de las seis piezas que la acción 3 trajo —`qti-sdk`, `extension-tao-testqti`,
`php-xapi/client`, `TinCanPHP`, `TinCanPython` y `cass-npm`— el conteo de «MCP» y «Model Context Protocol` es **cero en
las seis**. El gap 60 pasa de *medido abriendo los candidatos de dos capas* a **medido además por nombre de implementador
en tres registros**. 🔵 **Y aparece un dato que el gap no tenía:** **el SDK JavaScript de CaSS tampoco expone MCP** —
el cartucho MCP de CaSS vive **sólo del lado servidor** (`cassproject/CASS`), así que *«CaSS tiene puerta MCP»* es
cierto del servidor y **falso del SDK**. Quien integre por npm no hereda la puerta.

### 🟢 Las altas del pase, todas verificadas por archivo `LICENSE` o clasificador OSI

| Pieza | URL | Licencia | ★ | Señal | Por qué entra |
|---|---|---|---|---|---|
| **Claw-ED** | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | **MIT** ✅ (`LICENSE`: *Copyright (c) 2026 EDUagent Contributors*) | **60** (13 forks) | **778 commits**; PyPI `clawed` con **240 releases**, v**9.18.2026.1** | 🟢 **El agente docente *local-first* que P8 describía y esta KB no tenía.** Importa material propio (PDF/DOCX/PPTX/TXT/MD), construye **perfil de estilo de enseñanza** y emite borradores editables |
| **canvas-lms-mcp** | [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | **MIT** ✅ | 8 (4 forks) | **317 commits**, **62 versiones** npm, **165 tools**, MCP 1.x | 🔵 **El conector permisivo de LMS más grande de esta KB**, con cifra citable y **auditoría de accesibilidad** como categoría |
| **moodle-cli** | [bunizao/moodle-cli](https://github.com/bunizao/moodle-cli) | **MIT** ✅ | — | **20 versiones** (2026-07-09 → 2026-09-27), 16 menciones de MCP | **La cuarta puerta de Moodle, y la primera del lado alumno**: vencimientos, notas, archivos, devoluciones y revisión de quizzes **desde la sesión del navegador** |
| **jbnu-lms-mcp** | [moon0825/jbnu-lms-student](https://github.com/moon0825/jbnu-lms-student) | **MIT** ✅ | — | v0.8.0, **2026-09-08**, **25 tools**, passkey, Windows+macOS | 🔵 **Categoría nueva: el LMS de una institución, no un producto.** Universidad Nacional de Jeonbuk (전북대학교). **Sólo lectura por diseño** y **no oficial por declaración propia** |
| **moodle-core-cli** | [gafapa/moodle-core-cli](https://github.com/gafapa/moodle-core-cli) | **MIT** ✅ | — | **11 versiones**, última 2026-09-24, Moodle **4.5+** | ⚪ **Sin MCP (cero menciones) — y por eso entra**: cliente limpio de *core web services*, el candidato más barato a envolver |

🔵 **Lo que esto le hace al mapa de conectores: Canvas tiene al menos cinco puertas MIT y Moodle cuatro más un cliente
envolvible.** La capa de conectores **ya no es escasa** — es la capa mejor abastecida de esta KB, y es toda permisiva
salvo dos piezas. ⚠️ **Y eso erosiona por segunda vez la tesis del pase 27** (*«las LMS son copyleft pero las puertas son
MIT»*): la primera grieta fue Open edX (AGPL y en proceso); la segunda es que **de las puertas de Moodle, una es
AGPL-3.0** (`csmediapro/moodle-mcp-server`, que esta KB ya tenía y que este pase re-fecha: **8 versiones en npm como
`moodle-mcp-server-aql`, la última del 2026-10-01** — está vivo). **La tesis vale por mayoría, no por regla.**

### 🔴 Acción 1 NO CUMPLIDA, y el resultado es estructural — y coincide con el gap 65 del pase 34

El pase 32 mandó probar **`eur-lex.europa.eu`** y **`data.europa.eu`**, «que no se intentaron». **Se intentaron. Los dos
están bloqueados**, y esta vez el bloqueo está medido en el registro del propio proxy de egreso, no inferido de un
timeout:

```
connect_rejected  gateway answered 403 to CONNECT  eur-lex.europa.eu:443
connect_rejected  gateway answered 403 to CONNECT  data.europa.eu:443
```

Probados además y **todos inalcanzables**: `artificialintelligenceact.eu`, `op.europa.eu`, `euaiact.com`,
`euai-act.com`, `nicfab.eu`, `cypheron.cz`, `modulos.ai`. 🔴 **No es un host caído: es el dominio completo de la
publicación legal europea más los analistas que lo citan.** **Gap 65 (planteado por el pase 34 como clase, confirmado acá en el caso europeo):** *el calendario del Anexo III no es verificable
de primera mano desde este entorno, y ningún pase futuro lo va a cerrar por este camino.* Deja de ser una acción
pendiente y pasa a ser una **restricción declarada**: se cierra con un PDF del DOUE traído por una persona, o no se
cierra.

✅ **Lo que sí avanzó, y es lo que descarga el riesgo comercial: la afirmación pasa de fecha a *inciso*.** El pase 32
tenía «2027-12-02» por concordancia de cinco fuentes. Este pase tiene **la disposición**:

> **Artículo 113** difiere la aplicación del **Capítulo III, Secciones 1, 2 y 3 — con la excepción del Artículo 6(5) —
> al 2 de diciembre de 2027** para los sistemas de alto riesgo del **Artículo 6(2) y el Anexo III**.

Y la cadena de publicación: **Reglamento (UE) 2026/1744**, DOUE del **2026-07-24**, **en vigor 2026-07-27**, **modifica**
el Reglamento (UE) 2024/1689 sin reemplazarlo. ⚠️ **Sigue siendo fuente secundaria** —no hay lectura del DOUE— pero
ahora es **citable con artículo y sección**, que es lo que el área legal de un cliente pide. **La frase de venta no
cambia; su respaldo sí.**

### 🔵 El hallazgo regional que convierte el «silencio de LATAM» en una oportunidad con nombre — gap 63 (nuevo)

Siete pases declararon el barrido regional de LATAM **saturado**. Este pase lo atacó por el registro de paquetes en
portugués y español, y **encontró lo contrario de un silencio: encontró una capa entera, activa, MIT — y el hueco exacto
donde debería estar educación.**

| Dominio de dato público brasileño | Paquete MCP | Licencia | Señal |
|---|---|---|---|
| Geografía, **censo**, economía, salud | [`ibge-br-mcp`](https://github.com/SidneyBissoli/ibge-br-mcp) | **MIT** ✅ | **24 versiones**, 2026-01-18 → **2026-09-27** |
| Banco Central (SGS, series) | `bcb-br-mcp` | — | **2026-09-28** |
| Salud — **DATASUS SIH/SUS** (internaciones, AIH) | `sih-br-mcp` | — | **2026-10-01** |
| Firma electrónica | `@signdocs-brasil/mcp-server` | — | 2026-09-07 |
| 🔴 **Educación — INEP / Censo Escolar / ENEM** | 🔴 **nada** | — | **Medido: `inep` → 3 resultados, ninguno MCP; `censo-escolar` → 18, todos colisión; `enem` → 6, el más nuevo de 2024** |

🔴 **Brasil está construyendo una capa nacional de MCP sobre sus datos públicos —estadística, banco central, salud,
firma— y educación es el único dominio grande que falta.** Eso no es un gap de esta KB: es un **hueco en el ecosistema
LATAM**, con un peer ya escrito que sirve de plantilla (`ibge-br-mcp`, MIT, 24 versiones) y con las tres fuentes
canónicas identificadas (**INEP**, **Censo Escolar**, **ENEM**). Ver **P74**.

### 🗺️ Las cuatro regiones rindieron — ninguna quedó en silencio

- **North America** — **confirmación, sin dato nuevo**, y es la cuarta vez seguida: **86 %** de las organizaciones
  educativas con AI generativa adoptada; **134 proyectos de ley en 31 estados** en la sesión 2026; **cuatro estados
  —Idaho, Maryland, Oklahoma, Virginia—** obligan a **política distrital**, no sólo guía estatal; **California AB 1159**
  prohíbe entrenar modelos con datos de alumnos; **Oklahoma** y **Maryland** exigen supervisión humana y **prohíben la
  decisión de alto impacto sobre el alumno**; Georgia y Mississippi suman créditos de CS con AI. Despliegues:
  **Gemini for Education** en **+1.000** instituciones de educación superior, **Khanmigo** en Maryland con **~4.350**
  alumnos. 🔵 **El dato nuevo es de abajo hacia arriba:** estudiantes de **los 50 estados** produjeron un marco nacional
  de AI para K-12 —**STUDENTS FIRST Act of 2026**— presentado por AASA en **agosto de 2026**. Es la primera pieza de
  gobernanza de esta KB **escrita por el usuario final regulado**, y encaja con **P7**.
- **EMEA** — gobernada por el calendario del **gap 56**, ahora con **artículo**: desde el **2026-08-02** el AI Office y
  las autoridades nacionales **ya aplican** el AI Act (transparencia incluida); el Anexo III de educación **vence el
  2027-12-02** por el Artículo 113. 🔵 **Dato nuevo, y es el que explica por qué EMEA compra infraestructura y no
  producto:** la adopción empresarial de AI en la **UE es 19,95 %** contra **20,2 % de la OCDE** — EMEA **no** va
  adelantada en adopción, va adelantada en regulación. Y la señal técnica se repite: **los distritos con exigencia de
  residencia de datos autoalojan pesos abiertos** (Llama 3, Mistral) en vez de consumir API, lo que vuelve el *stack*
  soberano **requisito**, no preferencia. El uso que efectivamente se despliega hoy sigue siendo el de **consecuencia
  liviana** (chatbot de información a familias).
- **APAC** — 🔴 **y acá hay una corrección a esta KB.** El pase 32 escribió *«Japón y Taiwán redactan ley»*. **Taiwán ya
  la tiene en vigor:** *Basic Law on Artificial Intelligence*, **vigente 2026-01-14**, **20 artículos**, ley marco que
  **no impone obligaciones operativas directas al sector privado** — es un *framework*, no un régimen de cumplimiento, y
  conviene no venderlo como tal. **Corea del Sur**: *AI Basic Act* **vigente 2026-01-22**, consolidación de **19**
  proyectos, segunda jurisdicción del mundo con ley integral. **Vietnam**: ley de AI que nombra educación entre **seis**
  sectores de alto riesgo (evaluación automatizada y monitoreo conductual), ⚠️ **con fecha de cumplimiento para los
  sistemas identificados el 2027-03-01** — esta KB tenía «vigente marzo de 2026», que es la entrada en vigor de la ley,
  **no** el plazo de cumplimiento del alto riesgo. **Son dos relojes y había uno.** Mercado dominado por China, India y
  Japón; *players* citados: Google, Microsoft, IBM, Pearson, Byju's. 🔵 **Y el dato de ingeniería del pase viene de acá:**
  `jbnu-lms-mcp` es **la primera pieza de infraestructura agéntica educativa de origen APAC** que entra a esta base por
  el registro de paquetes, y es **sólo lectura por diseño** — que es exactamente la postura que el régimen coreano
  vigente premia.
- **LATAM** — **la adopción sigue por delante del mundo y la regulación por detrás**, confirmado: *AI in Higher Education
  LATAM Survey 2026* (Digital Education Council con el Institute for the Future of Education del **Tec de Monterrey**,
  más **AIGEN** y **RIE360**, **+30.000 respuestas de 29 instituciones**): **92 % de estudiantes** y **79 % de docentes**
  usan AI activamente, **94 % de docentes** espera usarla, y **65 % de los estudiantes teme que la AI vuelva superficial
  el aprendizaje**. Regulación a distintas velocidades: proyecto de ley en **Brasil**, marco en **Chile**,
  **CONPES 4144** en **Colombia** (política nacional con presupuesto hasta 2030; adoptada en **febrero de 2025**),
  reglas sectoriales en **México**. 🔵 **El dato nuevo es de oferta, no de demanda, y es el gap 63:** existe una capa
  MCP brasileña de datos públicos, activa y MIT, **sin educación**. 🔴 **Y la barrera que las encuestas no miden:**
  escasez y costo de ingenieros de ML y arquitectos de plataforma senior, **tensionada por el trabajo remoto** que abre
  el talento LATAM a empleadores de EE. UU. y Europa. Para Globant eso es las dos cosas: competencia por el perfil, y
  el argumento de por qué el cliente terciariza la capa.

## 2026-10-02 (pase 34) — el pase que mide **el error del registro en la dirección contraria**: el pase 33 probó que el registro **no ve** open source real; este pase encuentra que el registro **muestra como MIT lo que no tiene código**

**Lo que se hizo:** el barrido obligatorio completo —**cuatro búsquedas globales y cuatro regionales**, con el año
**calculado** (2026); **las cuatro regiones rindieron y ninguna quedó en silencio**— más **las tres acciones que el pase
33 dejó escritas**. Las tres se ejecutaron y **las tres cerraron**: la acción 1 auditó las ausencias declaradas y
encontró **tres confirmadas y una parcialmente falsa**; la acción 2 **cerró el gap 64 en negativo con tres instrumentos**;
la acción 3 **decidió P69**, y la decidió por licencia y no por lenguaje.

🔴 **El hallazgo que manda completa el del pase 33 y lo invierte.** El pase 33 midió que `learnmcp-xapi` **no está en
ningún registro de paquetes** y concluyó que un barrido basado en registros **tiene falsos negativos**. Este pase
encontró el **falso positivo**, y es del mismo tamaño:

| | Pase 33 (falso negativo) | Pase 34 (falso positivo) |
|---|---|---|
| **El caso** | `learnmcp-xapi` | **`quizlar/mcp-server`** |
| **Lo que el registro dice** | **nada** — PyPI 404, npm `total: 0` | **MIT**, servidor MCP de educación, activo |
| **La realidad** | **MIT, open source, 3 tools, en esta KB desde el pase 6** | 🔴 **No hay código.** El repo es **un manifiesto de 25 líneas** |
| **El error que produce** | se declara ausente lo que existe | **se promueve como open source lo que es un servicio propietario** |

**O sea: el registro de paquetes y el de servidores MCP fallan en las dos direcciones, y la corrección no es «buscar
mejor» en ninguna de las dos. Son instrumentos con sesgo conocido, y a esta altura conviene escribirlo como tal.** Ver
tendencias **103** y **104**.

### 🔴 Colisión 9 — y es de clase nueva: no colisiona el **nombre**, colisiona la **superficie de la licencia**

Las colisiones 1 a 8 de esta KB son de **término** (`opencase` son cajas de skins, `tincan` es mensajería entre agentes
de código, `xapi` es forex). **La novena es distinta y más peligrosa, porque el nombre es correcto, el dominio es
correcto y la licencia es real.** Lo que no es lo que parece es **qué cubre esa licencia.**

Leído de primera mano por `raw.githubusercontent.com` sobre `quizlar/mcp-server@main`:

| Archivo | Código | Qué contiene |
|---|---|---|
| `LICENSE` | **200** | *«MIT License — Copyright (c) 2026 **Quizlar**»* ✅ **la licencia es real** |
| `server.json` | **200** | 🔴 **un manifiesto de registro, y nada más** |
| `README.md` | **200** | la superficie de descubrimiento |
| *cualquier fuente* | — | 🔴 **no hay** |

**Y el manifiesto se delata solo, en un campo:**

```json
"remotes": [{ "type": "streamable-http", "url": "https://mcp.quizlar.app/mcp/",
  "headers": [{ "name": "Authorization", "isRequired": true, "isSecret": true,
    "description": "Mint a Quizlar API key at https://quizlar.app/settings/api-keys (format: sk-qz-<32 chars>)" }] }]
```

🔴 **`remotes` significa que el servidor corre en el host del proveedor.** El `$schema` es
`static.modelcontextprotocol.io/schemas/**2025-12-11**/server.schema.json`, o sea el esquema nuevo de registro de MCP.
**Lo que está licenciado MIT es el manifiesto; la implementación es un endpoint alojado detrás de una clave
`sk-qz-<32>`.** No hay nada que auto-hospedar, forkear, auditar ni extender.

🔵 **El control es de un campo y hay que incorporarlo al barrido:** si `server.json` declara **`remotes`** y no declara
paquete ni fuente, **la licencia del repo cubre metadatos**. Para una propuesta de Globant eso significa **cero código
reutilizable, una dependencia de proveedor, y datos de aprendizaje del alumno saliendo a un tercero bajo API key** —
que es exactamente lo contrario del argumento de privacidad por diseño que esta base construyó sobre `ACTOR_UUID`.

⚠️ **Y conviene decir qué sí es Quizlar, sin despreciarlo:** *«voice-led, FSRS-scheduled flashcards from YouTube, PDFs,
web, or text»*. Como **producto** es del dominio y usa **FSRS**, el mismo planificador que `OpenTutor` (fila de esta
tabla). Como **pieza componible, no existe.** No entra a la tabla, y se anota acá para que ningún pase lo promueva.

### ✅ Acción 1 ejecutada — las ausencias del mapa por estándar, auditadas una por una

El pase 33 ordenó auditar **todas** las frases de tipo *«no existe»* contra (a) un `grep` sobre estos ocho archivos y
(b) una **búsqueda abierta**, que es el instrumento que destapó la mitad xAPI. Se hizo para las cuatro:

| Ausencia declarada | (a) `grep` sobre la KB | (b) búsqueda abierta | Veredicto |
|---|---|---|---|
| **Caliper** sin puerta MCP | presente en los 8 archivos, **sin contradicción** | 🔴 ninguna implementación MCP | ✅ **CONFIRMADA, dos instrumentos** |
| **CASE** sin puerta MCP | presente, **sin contradicción** | 🔴 nada del dominio | ✅ **CONFIRMADA, dos instrumentos** |
| **CEASN** sin puerta MCP | presente en 4 archivos, **sin contradicción** | 🔴 nada — y el buscador **expande mal la sigla** | ✅ **CONFIRMADA, dos instrumentos** |
| **Open Badges** sin puerta MCP | presente en los 8 archivos | 🔴 ninguna puerta MCP… **pero sí una plataforma OB 3.0 que esta KB no tenía** | ⚠️ **la mitad MCP se sostiene; la de implementación era falsa** |

🔵 **Dato de método sobre CEASN, y es tranquilizador al revés:** la búsqueda abierta ni reconoce la sigla —la expande
como *«Credential Engine Adoption Support Network»*, que **no es** lo que CEASN significa (*Competency and Academic
Standards Exchange*)—. **Una ausencia que el instrumento no puede ni nombrar es una ausencia robusta**, no un fallo de
consulta.

🟢 **Y la mitad que era falsa paga el pase entero.** Esta KB registraba que *«las implementaciones de referencia de
estos estándares ya no están»* (`badgr-server` **404**) y que el Open Badges de CaSS es **OB 2.0, no 3.0**. Existe una
implementación **OB 3.0 completa**, y no estaba en ninguno de los ocho archivos:

| Pieza | Licencia (leída del archivo) | Qué es |
|---|---|---|
| [`Schroedinger-Hat/certo`](https://github.com/schroedinger-hat/certo) | ⚠️ **AGPL-3.0** (`LICENSE` 200: *«GNU AFFERO GENERAL PUBLIC LICENSE Version 3»*) | **Open Badges 3.0 + W3C Verifiable Credentials + DIDs**, emisión individual y **masiva por CSV**, página pública de verificación, compartir a LinkedIn. Strapi 5.x + Nuxt 3 |
| [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) | **Apache-2.0** ✅ (`LICENSE` 200 en `main` **y** `master`) | El **validador oficial del consorcio** para Open Badges **y Comprehensive Learner Record**, con HTTP y API |

⚠️ **La licencia de Certo decide cómo se propone:** AGPL-3.0 **en un servicio de red** obliga a ofrecer la fuente a los
usuarios. Como **plataforma desplegada para el cliente** sirve; como **componente embebido en un producto de Globant**,
no. 🟢 **El validador de 1EdTech, en cambio, es Apache-2.0 y es el que cierra el expediente**: permite verificar la
credencial emitida **contra el consorcio que publica el estándar**, sin pedirle permiso a nadie. Ver **P74**.

### ✅ Acción 2 — gap 64 CERRADO en negativo, y medido con **tres** instrumentos independientes

La pregunta era si los LRS publican **su propia** puerta MCP, que es el canal donde el pase 30 encontró `openedx-mcp`
(oficial, dos meses antes de que esta KB lo notara). **La respuesta es no, y por tres caminos que no se apoyan entre sí:**

| Instrumento | Consulta | Resultado |
|---|---|---|
| **Docker Hub** (el canal que el pase 33 incorporó) | `hub.docker.com/v2/repositories/yetanalytics/` | **`count: 6`** — `lrsql`, `xapipe`, `datasim`, `persephone`, `fuseki`, `hello-marathon`. 🔴 **ninguna MCP** |
| **Árbol de `lrsql`** | `deps.edn` + `README.md` sobre `main` | 🔴 **cero menciones de `mcp`** en las dos |
| **PyPI de Ralph** | `ralph-malph` 5.0.1, `requires_dist` + `provides_extra` | 🔴 **ningún `mcp`** en dependencias; **14 extras** y ninguno MCP; **0 menciones** en la descripción |

**Entonces `DavidLMS/learnmcp-xapi` (MIT, de un tercero) sigue siendo la única puerta MCP de la capa de telemetría**, y
ahora eso está medido en vez de supuesto. 🔵 **Y el instrumento regaló el sitio exacto de la contribución *upstream*:**
los **14 extras** de Ralph (`backend-clickhouse`, `-es`, `-ldp`, `-lrs`, `-mongo`, `-s3`, `-swift`, `-ws`, `backends`,
`cli`, `lrs`, `dev`, `ci`, `full`) son una **superficie de plugins ya instalada y empaquetada**. Un `ralph[mcp]` es la
contribución que encaja en la convención del proyecto, no un fork. Ver **P71**.

### 🟢 Gap 63 — la mitad de arquitectura CIERRA con evidencia de archivo; la de fecha queda abierta **con mejor razón**

El pase 33 leyó la arquitectura de plugins de `learnmcp-xapi` **del README** y lo dejó anotado como no fechado. Este
pase la confirma **por existencia de archivos**, que es evidencia más fuerte que la prosa:

| Ruta | Código |
|---|---|
| `config/plugins/lrsql.yaml` | **200** ✅ |
| `config/plugins/ralph.yaml` | **200** ✅ |
| `config/plugins/veracity.yaml` | **200** ✅ |
| `.env.example` | **200** — declara `LRS_PLUGIN=lrsql  # Options: lrsql, ralph, veracity` |

**Los tres backends del README existen como archivos de configuración.** El `lrsql.yaml` trae
`endpoint: ${LRSQL_ENDPOINT:-http://localhost:8080}`, `key`/`secret` por variable, `timeout: 30` y `retry_attempts: 3`.

🔴 **Pero la fecha del `2.0.0` no es que esté bloqueada: es que no existe en el árbol.** Se probaron **ocho** rutas
portadoras de versión y **las ocho dan 404**: `pyproject.toml`, `uv.lock`, `CHANGELOG.md`, `VERSION`, `setup.py`,
`main.py`, `src/__init__.py`, `app/__init__.py`. Lo único que hay es `requirements.txt` (**200**), que **no declara
versión de proyecto**. **El gap 63 se reclasifica:** no es una limitación del proxy —como se escribió en el pase 33—,
es que **el proyecto no se versiona dentro de su propio árbol**, así que **ningún canal alcanzable puede fechar ese
`2.0.0`**. Eso es una conclusión más útil que «bloqueado»: cierra la búsqueda en vez de invitar a repetirla.

### 🟢 Y aparece la **tercera** variante de la misma primitiva de seguridad — ésta frena en la **configuración**

`.env.example` de `learnmcp-xapi` declara dos límites que la ficha de esta KB no registraba:

```
RATE_LIMIT_PER_MINUTE=30
MAX_BODY_SIZE=16384
```

**La serie queda completa y conviene cotizarla junta,** porque son tres mecanismos para el mismo riesgo —el agente en
bucle— con tres propiedades de falla distintas:

| Pieza | Dónde frena | ¿Frena solo? |
|---|---|---|
| `openedx-mcp` (pase 30) | **en el servidor** — *confirm token* atado a una huella del payload | 🟢 **Sí** |
| `coursecode` (pase 33) | **en el contrato** — anotaciones MCP + `dryRun` | 🔴 **No** — si el cliente ignora las anotaciones, gasta |
| **`learnmcp-xapi` (este pase)** | **en la configuración** — 30 escrituras/minuto y cuerpo de 16 KiB | 🟢 **Sí**, y sin pedirle nada al cliente |

🔵 **El de configuración es el más barato de los tres y el único que no requiere cooperación de nadie:** es un techo de
caudal, no una decisión. **Para la capa de telemetría —donde el riesgo es inundar el LRS de statements, no borrar un
curso— es exactamente el freno adecuado.** `learnmcp-xapi` además corre sobre **`fastmcp>=0.3.2`** (no el SDK crudo),
con **8 dependencias de runtime**: `fastmcp`, `fastapi`, `uvicorn[standard]`, `httpx[http2]`, `jsonschema`, `pydantic`,
`pyyaml`, `orjson`. Ver tendencia **105**.

### ✅ Acción 3 — P69 DECIDIDO, y lo decide la licencia, no el lenguaje

El pase 33 pidió decidir **con el número de adopción al lado** si la contribución *upstream* de QTI conviene sobre el
stack PHP o sobre el TypeScript. **Los números se midieron en Packagist y npm, y el número de adopción perdió:**

| | `qtism/qtism` (OAT QTI-SDK) | `@longsightgroup/qti3-cli` |
|---|---|---|
| **Licencia** | 🔴 **GPL-2.0-only** — en **las 293 releases** | **MIT** ✅ |
| **Adopción** | 🟢 **218.212 descargas** totales, **3.104/mes**, 85 *favers* | menor y nueva |
| **Actividad** | viva: `v19.7.2` el **2026-07-09** | 🟢 **41 releases**, primera **2026-05-21**, última modificación **2026-10-01** |
| **Dependencias de terceros** | stack PHP completo | 🟢 **cero en toda la cadena** |

Y el ecosistema PHP alrededor es real: `oat-sa/extension-tao-item` **130.032** descargas,
`extension-tao-itemqti` **128.201**, `-pci` **89.265**, `-pic` **79.373**, `extension-tao-itemhtml` **37.722**.

🔵 **La decisión, y el criterio por el que se toma:** **se contribuye sobre el lado TypeScript.** El stack PHP tiene
**~10× la adopción** y eso era el argumento a favor, pero **`GPL-2.0-only` cierra el caso de uso**: Globant no puede
envolverlo en un producto propietario ni embeberlo en una entrega de cliente sin heredar copyleft, y la obligación
alcanza al derivado. **El lado MIT no sólo es viable: resulta ser el que se mueve más rápido** —41 releases en cuatro
meses y medio, la última de ayer—, lo que era lo contrario de lo que cabía esperar de la opción con menos adopción.
**El número grande era el equivocado para esta pregunta.** **P69** queda cerrado y cotizado.

### 🔴 El hallazgo estructural del pase, y es de método: **el entorno sesga esta KB hacia fuentes comerciales**

El pase 33 cerró el gap 56 reportando que `eur-lex.europa.eu` y `data.europa.eu` están bloqueados. Este pase fue a
buscar **dos fuentes primarias regionales nuevas** —el Consejo de Europa (EMEA) y el *working paper* de **UNESCO
IESALC** sobre **200 instituciones en 19 países** (LATAM)— y **las dos están bloqueadas**. Así que se midió el patrón
en vez de seguir encontrándolo de a uno:

| Clase de dominio | Probados | Alcanzables |
|---|---|---|
| 🔴 **Multilaterales e institucionales** | `coe.int`, `unu.edu`, `publications.iadb.org`, `www.unesco.org`, `unesdoc.unesco.org`, `iesalc.unesco.org`, `www.oecd.org`, `ec.europa.eu`, `www.worldbank.org` (+ `eur-lex.europa.eu` y `data.europa.eu` del pase 33) | 🔴 **0 de 11** |
| ✅ **Registros comerciales y de código** | `registry.npmjs.org`, `pypi.org`, `packagist.org`, `hub.docker.com`, `raw.githubusercontent.com` | 🟢 **5 de 5** |

🔴 **Esto cambia cómo hay que leer todo `intel/` de esta base, y hay que decirlo en voz alta: cada afirmación
regulatoria y de tamaño de mercado de esta KB se apoya en fuentes secundarias comerciales *por construcción del
entorno*, no por falta de rigor del pase.** No es que las primarias no se hayan intentado —se intentaron **once**—: es
que **ninguna es alcanzable desde esta red**.

🔵 **Y eso reclasifica el gap 56 de «acción pendiente» a «límite de clase».** Probar un dominio europeo más es
previsiblemente inútil. **La petición correcta no es técnica, es organizativa: una lectura del texto consolidado hecha
fuera de esta red**, y así hay que pedirla. Ver tendencia **106** y **gap 65**.

### 🔵 Dominios y canales que este pase agrega al mapa del entorno

- 🔴 **Bloqueados por el proxy de egreso (nuevos):** `mcp.so` (el registro de servidores MCP — **el instrumento natural
  para este barrido, y no se puede consultar**), `coe.int`, `unu.edu`, `publications.iadb.org`, `www.unesco.org`,
  `unesdoc.unesco.org`, `iesalc.unesco.org`, `www.oecd.org`, `ec.europa.eu`, `www.worldbank.org`.
- ✅ **Responden:** `registry.npmjs.org`, `pypi.org`, `packagist.org` (`/packages/<vendor>/<pkg>.json` da licencia y
  fecha **por release**, que es mejor que `/search.json`), `hub.docker.com`, `raw.githubusercontent.com`.
- ⚠️ **`api.npmjs.org/downloads/point/...` devolvió vacío** para un paquete con *scope*; la adopción de npm de este pase
  se reporta por **conteo y fechas de releases**, no por descargas. **La asimetría hay que decirla:** Packagist **sí**
  da descargas, así que la comparación PHP/TypeScript de arriba **no es simétrica en esa columna** — y por eso la
  decisión se tomó por licencia, que sí está medida en las dos.

---
## 2026-10-02 (pase 33) — el pase que descubre que **el gap 60 se contradecía con la propia tabla de esta KB**, y mide **por qué**: la lista de candidatos venía del registro de paquetes, y la pieza que lo refuta **no está en ningún registro**

**Lo que se hizo:** el barrido obligatorio completo —**cuatro búsquedas globales y cuatro regionales**, con el año
**calculado** (2026); las cuatro regiones rindieron y ninguna quedó en silencio— más **las tres acciones que el pase 32
dejó escritas**. Las tres se ejecutaron: una cerró con **resultado negativo y definitivo** (gap 56), otra cerró **a
medias por falta de permiso de ejecución** (gap 62, nuevo) y **la tercera dio vuelta la conclusión del pase anterior**.

🔴 **El hallazgo que manda es de consistencia interna, y es incómodo.** El pase 32 declaró —con la palabra *«medido»*—
que **xAPI/LRS no tiene puerta MCP** (**gap 60**). **Es falso, y la refutación ya estaba adentro de esta misma KB:**

| Dónde | Desde cuándo | Qué dice |
|---|---|---|
| `agents/top.md`, tabla principal (fila `learnmcp-xapi`) | **pase 6** | *«Servidor MCP que le da a un agente memoria de aprendizaje conforme al estándar: tres tools sobre un Learning Record Store xAPI»* |
| `agents/top.md`, mapa por estándar | **pase 27** | **`| xAPI | ✅ learnmcp-xapi (desde el pase 6) |`** |
| `repos/foundations.md`, capa de telemetría | **pase 6** | `learnmcp-xapi` **MIT**, con `lrsql` (Apache-2.0) y `Ralph` (MIT) |
| `compose/patterns.md` | varios | **más de quince patrones** ya componen `learnmcp-xapi` + `lrsql` |

**O sea: el pase 32 declaró ausente una pieza que esta base lista como presente en cuatro archivos, uno de ellos con la
frase «desde el pase 6» escrita al lado.** No es un error de búsqueda: es un error de **no consultarse a sí misma**.

### 🔴 Por qué pasó, y esto sí es una medición nueva

El pase 32 midió *«abriendo los README de los candidatos de las dos capas»*. **La lista de candidatos la produjo el
barrido del registro de paquetes** —el método que los pases 30, 31 y 32 instalaron como canal de descubrimiento. Y se
midió, en este pase, que ese canal **no puede contener a `learnmcp-xapi`**:

| Consulta | Resultado |
|---|---|
| `pypi.org/pypi/learnmcp-xapi/json` | 🔴 **404** |
| `registry.npmjs.org/-/v1/search?text=learnmcp` | 🔴 **`total: 0`** |
| Instalación que el README documenta | *from source*, `venv` o `uv` — **las tres desde el código** |

🔴 **`learnmcp-xapi` no está publicada en ningún registro de paquetes.** Un barrido que arma su lista de candidatos
consultando npm, PyPI y Packagist **tiene cero probabilidad** de devolverla, por bien formulada que esté la consulta.
La *«ausencia medida»* del gap 60 era **un artefacto del instrumento** — y el instrumento era tan dominante que **se le
creyó por encima de la tabla propia**. Ver tendencias **99** y **100**.

**La regla que esto deja, y es barata:** 🔵 **antes de declarar una ausencia, consultar esta KB.** Un `grep` sobre los
ocho archivos cuesta segundos y habría evitado el gap 60 entero. **Ninguna ausencia se declara sin ese paso.**

### ✅ Lo que sí es nuevo del pase sobre la capa de telemetría: las tres piezas quedan **fechadas**

La KB tenía las tres piezas y su licencia; **lo que no tenía era su estado actual**. Eso se midió:

| Pieza | Licencia | Verificación de primera mano | Estado medido en este pase |
|---|---|---|---|
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** ✅ (`LICENSE` 200 = texto Apache 2.0) | **`hub.docker.com/v2`**: `count: 112` tags | 🟢 **VIVO y la cifra es de ayer: `v0.9.9` el 2026-10-01.** Seis releases en 2026 (v0.9.4 abr, v0.9.5 abr, v0.9.6 ago, v0.9.7 ago, v0.9.8 ago, v0.9.9 oct) |
| [`openfun/ralph`](https://github.com/openfun/ralph) | **MIT** ✅ (clasificador OSI en PyPI) | PyPI `ralph-malph` **5.0.1**, *upload* **2024-07-11**; `CHANGELOG.md` (200) | ⚠️ **Vivo en `main`, parado en el registro.** El `[Unreleased]` es grande y activo (CORS, baja de Python 3.8, correcciones de tipos Pydantic, mantenimiento de CI) pero **no hay release desde hace ~2,2 años** |
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** ✅ | `LICENSE` (200): *«MIT License — Copyright (c) 2025 **David Romero**»*; `README.md` (200), **293 líneas** | 🟢 **Arquitectura de plugins documentada de primera mano** (ver abajo). 🔴 **Fuera de todo registro** |

🔵 **La distinción de Ralph hay que decirla en la primera reunión:** vivo en `main` **no** es lo mismo que publicado. Un
proyecto que lo use **instala desde git, no desde PyPI**, y eso cambia la cotización del *onboarding* y del pipeline de
dependencias. No está abandonado —el `[Unreleased]` lo prueba— pero **no se cotiza como dependencia estable**.

### 🟢 `learnmcp-xapi`: lo que la ficha de la KB no tenía, leído del README

La ficha del pase 6 decía *«tres tools sobre un LRS»* y el pase 25 la re-verificó como *«no se movió»* (15 ★, 32
commits). **Las tres tools siguen siendo tres** —*«statement recording, progress retrieval, and activity vocabulary
management»*, o sea **1 escribe y 2 leen**— pero el README documenta hoy una **arquitectura que la ficha no registraba**:

- **Selección de LRS por variable de entorno:** `LRS_PLUGIN=lrsql | ralph | veracity`, con un bloque de configuración
  propio por backend y archivos `config/plugins/<backend>.yaml` (`retry_attempts`, endpoint, credenciales).
- **Plugin system declarado como extensible:** *«designed for easy addition of new LRS implementations without
  modifying core code»*.
- **Privacidad por diseño:** un `ACTOR_UUID` por alumno, con el README afirmando *«No personal information is stored —
  only learning activities and progress indicators»*.
- **Autenticación:** Basic Auth y **OIDC**, según lo que pida el LRS.

⚠️ **Lo que no se pudo fechar, y se dice:** fuentes secundarias mencionan un **`2.0.0`** con *«complete redesign with a
modular LRS plugin system»*, que sería **movimiento posterior** al *«no se movió»* del pase 25. **No se verificó de
primera mano:** la página de *releases* vive en `github.com`, que devuelve **403** en este entorno, y el repo **no tiene
`pyproject.toml` en la raíz de `main`** (404). Queda como **gap 63**: la arquitectura de plugins está leída, su fecha no.

⚠️ **Y una corrección de atribución que hay que anotar sin inventar.** `intel/market.md` atribuye `learnmcp-xapi` a
*«IES Rafael Alberti, España»*. **El `LICENSE` del repo dice textualmente `Copyright (c) 2025 David Romero`** — una
persona, no una institución. Las dos cosas pueden ser compatibles (autor individual con filiación docente), pero **el
dato verificable es el del `LICENSE`**, y el argumento de soberanía europea de EMEA conviene apoyarlo en **Ralph
(France Université Numérique)**, cuyo titular institucional **sí** está en el archivo de licencia.

### ✅ Gap 60, mitad QTI: CONFIRMADA, y ahora por dos instrumentos independientes

Lo que el pase 32 midió abriendo README, este pase lo volvió a preguntar **por búsqueda abierta** —el instrumento que
acabó de demostrar que el registro no sustituye— y el resultado **coincide**: **QTI no tiene puerta MCP.** La búsqueda
explícita de MCP + QTI no devuelve ninguna implementación y el ecosistema MCP no nombra QTI.

🔵 **O sea: el gap 60 no era falso, era *mitad* falso** — y las dos mitades fallaban por motivos opuestos. La mitad xAPI
falló por **exceso de confianza en el instrumento** (la pieza existía y la KB la tenía). La mitad QTI **se sostiene y
ahora está doblemente medida**. Es la diferencia entre *«no lo encontré»* y *«no está»*.

**Y la envolvibilidad que el gap 60 afirmaba sin probar queda medida.** `@longsightgroup/qti3-cli@0.13.1` (**MIT**):

- **`bin`**: `{ "qti3": "dist/index.js" }` — ya es un ejecutable.
- **Superficie declarada**: *«parsing, validating, scoring, inspecting, and checking QTI 3 items»*.
- 🟢 **`dependencies` completas**: `@longsightgroup/qti3-core`, `-a11y`, `-fixtures`, `-conformance`, **las cuatro en
  `0.13.1` y las cuatro hermanas. Cero dependencias de terceros en toda la cadena.**

**La conclusión cotizable:** un wrapper MCP sobre `qti3-cli` **agrega exactamente una dependencia externa**
(`@modelcontextprotocol/sdk`) a un árbol que hoy no tiene ninguna. Es la contribución *upstream* más limpia de esta
base, y ahora con el costo **medido** en vez de estimado. Ver **P74**.

### ✅ `coursecode` medido en el artefacto publicado — 15 tools, y **dos escriben**

Se bajó el tarball de `coursecode@0.1.61` de `registry.npmjs.org` (200, 2,9 MB) y se leyó el código publicado:

| Medición | Valor | Fuente |
|---|---|---|
| Licencia | **MIT**, *«Copyright (c) 2026 Seth Vincent»* | `LICENSE` del artefacto |
| Dependencia MCP | **`@modelcontextprotocol/sdk`** en `dependencies` | `package.json` del artefacto |
| Tools definidas | **15** | `lib/mcp-prompts.js` |
| Casos de dispatch | **15** | `lib/mcp-server.js` |
| **Aliasing / supresión** | 🟢 **Ninguno** — 15 definidas, 15 servidas | las dos lecturas coinciden |

**Las 15:** `coursecode_state`, `_errors`, `_navigate`, `_interact`, `_reset`, `_screenshot`, `_viewport`,
`_workflow_status`, `_build`, `_css_catalog`, `_component_catalog`, `_interaction_catalog`, `_lint`, `_narration`,
`_icon_catalog`.

🟢 **Sí escribe, y eso responde la pregunta de la acción 2: `coursecode` es la pieza de salida de la capa generativa**,
no un CLI con fachada. Reemplaza con ventaja a `scorm-mcp-server` (3 tools) en ese rol:

- **`coursecode_build`** — `inputSchema` con **`enum: ['cmi5','scorm2004','scorm1.2','lti']`**. 🔴 **Esto es evidencia más
  fuerte que la que la KB tenía:** los cuatro estándares de salida dejan de estar afirmados en prosa del README y pasan
  a estar **en el contrato de la tool**. Corre `vite build` con `LMS_FORMAT` y devuelve `outputDir` (`dist/`).
  `annotations: { idempotentHint: true }`.
- **`coursecode_narration`** — escribe **MP3 en `course/assets/audio/`** llamando a un **proveedor TTS pago**. Cachea por
  hash de texto+voz en `.narration-cache.json`.

⚠️ **Lo que este pase NO pudo hacer, y se registra en vez de maquillarse:** **no se ejecutó `tools/list` por protocolo.**
Instalar dependencias de terceros quedó **bloqueado en este entorno**, así que las cifras de arriba son **lectura del
artefacto publicado**, no medición de protocolo — justo la distinción que el pase 30 estableció con `oneroster-ts`. La
coincidencia 15 = 15 entre definiciones y dispatch hace **improbable** el aliasing, pero no lo descarta como lo haría una
respuesta del servidor. **Gap 62.**

### 🟢 El regalo del hallazgo: la misma primitiva de seguridad, reinventada por otro mecanismo

El pase 30 encontró en `openedx-mcp` el rail *dry run + confirm token atado a una huella del payload* (**tendencia 84**).
`coursecode_narration` resuelve **el mismo problema con otro mecanismo**, en tres capas:

1. **`dryRun: true`** — *«no API calls, no audio written»*.
2. **Una cláusula de aprobación escrita en la descripción de la tool**: *«Real generation … **requires explicit user
   approval before running**»*.
3. 🟢 **Anotaciones MCP declaradas**: `readOnlyHint: false`, `idempotentHint: false`, `destructiveHint: false`.

**Por qué importa para componer:** `openedx-mcp` pone el freno **en el servidor** (un token que el cliente debe
devolver); `coursecode` lo pone **en el contrato** (anotaciones que el cliente MCP lee para decidir si pide
confirmación). Son dos mitades del mismo control y **sólo una frena sola**: si el cliente MCP ignora las anotaciones,
`coursecode_narration` gasta crédito de TTS sin preguntar. Ver tendencia **102**.

### 🔴 Gap 51 CERRADO — y cierra en negativo: el registro **no desambigua** CASE, ni por estándar ni por proyecto

El pase 32 descartó por escrito el nombre del **estándar** y dejó escrito que había que atacarlo **por el nombre del
proyecto implementador**. Se hizo, en **tres registros**:

| Consulta | npm | PyPI | Packagist |
|---|---|---|---|
| `opencase` | **7 resultados, 0 del dominio** | **404** | **665 resultados, 0 del dominio** |
| `cass` | ruido puro | **404** | **26.726 resultados** |
| `qti3` | 12 paquetes `@longsightgroup/*` ✅ | **404** | — |
| `learning_locker` | **1 resultado**, exacto ✅ | — | **3 resultados**, exactos ✅ |
| `tincan` | ruido mezclado | `tincan` ✅ | — |

🔴 **Lo que devuelve `opencase` en npm es apertura de cajas de skins de videojuego** (`opencase` y `skins4go`, los dos con
la misma descripción *«OpenCase by ДикиЙ»*). En Packagist, `opencase` hace *fuzzy match* contra **`opencage`** (un
geocodificador) y **`opencast`** (la captura de clase de Apereo — del dominio educativo, pero otro proyecto). `cass`
colisiona con **Cassandra**, con **USPS CASS** (validación de direcciones postales) y con un *pack* de personaje Shimeji.

**Veredicto, y es metodológico:** **el registro de paquetes no es el instrumento para un estándar cuyos implementadores
se llaman con palabras comunes.** El instrumento que sí funcionó en los cinco casos de arriba es **el nombre de la
organización**: `LongsightGroup`, `oat-sa`, `yetanalytics`, `openfun`, `LearningLocker`. **Gap 51 cierra como
no-resoluble por nombre de paquete**, con el método de reemplazo escrito. Ver tendencia **100**.

### 🔴 Colisiones 7 y 8 — y la 8 es el caso de libro de la tendencia 96

| # | Término | El paquete que aparece | ¿Del dominio? |
|---|---|---|---|
| **7** | `opencase` | `opencase` / `skins4go` — *«OpenCase by ДикиЙ»*, apertura de cajas de skins | 🔴 **No** |
| **8** | `tincan` | **`@brutalsystems/tincan` v2.2.0** — *«Peer messaging between a live Claude Code session and a live Codex session… One MCP server, run inside each»* | 🔴 **No** |

🔴 **La colisión 8 es la que hay que recordar:** es **un servidor MCP**, **activo**, **con el nombre del estándar de
telemetría educativa en el paquete**… y es mensajería entre sesiones de agentes de código. **Cero relación con
educación.** Un barrido que busque «MCP + nombre de estándar + activo» la promueve sin dudar. Es exactamente el control
que la tendencia 96 pide: **contar el vocabulario del dominio antes de promover.**

**Hallazgo incidental que sí es del dominio:** `@osu-cass/sb-components` — *«Shared components for Smarter Balanced»*,
del consorcio de evaluación de Oregon State. Apareció buscando `cass` por otra cosa. **No es CaSS**; se anota para que
no se vuelva a confundir.

### 🔴 La capa xAPI «clásica» está congelada, y una mitad es copyleft

Tres mediciones de registro, no impresiones:

| Pieza | Registro | Licencia | Último movimiento |
|---|---|---|---|
| `learning_locker` | npm | 🔴 **GPL-3.0** | `modified` **2022-06-19** (~4,3 años) |
| `tincanjs` (RusticiSoftware) | npm | **Apache-2.0** | `modified` **2022-06-27** (~4,3 años) |
| `tincan` / TinCanPython (RusticiSoftware) | PyPI | **Apache-2.0** | release **2020-09-03** (~6 años) |

**Esto confirma, no corrige, la recomendación que esta KB ya tenía:** el stack vivo es `lrsql` (o Ralph) +
`learnmcp-xapi`, y **Learning Locker no es alternativa** — es copyleft **y** está congelado. 🔵 **Dato de puente:** el
`learning_locker` de Packagist devuelve **3 resultados exactos**, y uno es `yetanalytics/statementfactory`. **La consulta
que encontró lo muerto llevaba el puntero a lo vivo en la columna del mantenedor.**

### ⚠️ Gap 56: la acción se ejecutó y el resultado es negativo y definitivo para este entorno

El pase 32 mandó **probar `eur-lex.europa.eu` y `data.europa.eu`**, que no se habían intentado. Se intentaron:

| Dominio | Resultado |
|---|---|
| `eur-lex.europa.eu` | 🔴 **`EGRESS_BLOCKED` por el proxy** |
| `data.europa.eu` | 🔴 **`EGRESS_BLOCKED` por el proxy** |

**La fecha no cambia y suma concordancia secundaria.** El barrido regional de EMEA devuelve, otra vez y de fuentes
distintas: **Anexo III (educación) → 2027-12-02**, diferido desde el 2026-08-02; **art. 50 (transparencia) en aplicación
desde el 2026-08-02**; evaluación de conformidad —interna o auditoría de tercero— **antes de poner el sistema en el
mercado**. Con esto van **siete fuentes secundarias concordantes y cero primarias**.

🔴 **La regla se mantiene: esta fecha no se cita como primaria.** Es el único número de esta KB que un abogado del
cliente verifica en la primera reunión, y el texto consolidado **no es alcanzable desde este entorno**. La acción se
cierra como **ejecutada con resultado negativo** —no como pendiente—: para cerrarla hace falta **una lectura hecha fuera
de este entorno de red**, y así hay que pedirla.

### 🔵 Dominios y permisos que este pase agrega al mapa del entorno

- 🔴 **Bloqueados por el proxy de egreso (nuevos):** `eur-lex.europa.eu`, `data.europa.eu`.
- ✅ **Responden 200:** `registry.npmjs.org`, `pypi.org`, `raw.githubusercontent.com`, `packagist.org`
  (`/search.json`), `hub.docker.com` (`/v2/repositories/…/tags`).
- 🟢 **`hub.docker.com` es un canal de verificación nuevo para esta KB**, y es el que fechó `lrsql`: la API de tags
  devuelve `last_updated` por versión. **Para una pieza que se distribuye como contenedor es el sustituto de
  `api.github.com`** —que sigue dando 403— y de la fecha de release. **Agregarlo al conjunto de canales verificables.**
- ⚠️ **Sin permiso de ejecución en este entorno:** instalar dependencias de terceros. Por eso `tools/list` de
  `coursecode` quedó sin ejecutar (**gap 62**), y por eso toda medición de este pase es **lectura de artefacto o de
  registro**, nunca de proceso.

---
## 2026-10-02 (pase 32) — el pase que **cierra el gap 57 invirtiendo la conclusión del 31, y esta vez a favor**: crear un curso en Open edX **sí es una llamada HTTP**, sólo que no vive en el árbol REST versionado — y el permiso que pide **no es GlobalStaff**

**Lo que se hizo:** el barrido obligatorio completo —**cuatro búsquedas globales y cuatro regionales**, con el año
**calculado** (2026); las cuatro regiones rindieron y ninguna quedó en silencio— más **las tres acciones que el pase 31
dejó escritas**. Las tres se ejecutaron. Dos cerraron (**gaps 57 y 59**), la tercera rindió un hallazgo **MIT con MCP** y
**dos colisiones de término nuevas**. Y de regalo, el barrido regional de EMEA entregó lo que hacía falta para cerrar el
**gap 56**, que era el de mayor riesgo comercial de la base.

### 🔴 Gap 57 CERRADO — y la conclusión del pase 31 era verdadera en su medición y falsa en su alcance

El pase 31 midió tres capas por separado (los cinco árboles `v0`…`v4`, y las 19 tools de escritura del conector oficial)
y concluyó: *«crear la cáscara del curso no es alcanzable por REST»*. **La medición era correcta. La conclusión, no**, y
el error es de alcance: **el árbol REST versionado no es toda la superficie HTTP de Studio.**

Leído de primera mano por `raw.githubusercontent.com` sobre `master`:

| Pieza | Coordenada | Métodos | Permiso | ¿Crea o clona? |
|---|---|---|---|---|
| `CourseRerunView` | `contentstore/rest_api/v1/views/course_rerun.py` | **sólo `get`** | **`GlobalStaff`** explícito | **No** — devuelve el *contexto del formulario* |
| `course_rerun_handler` | `contentstore/views/course.py:365` | **sólo `GET`** (`@require_http_methods(["GET"])`) | **`GlobalStaff`** explícito | **No** — renderiza `course-create-rerun.html` |
| **`course_handler` POST** | `contentstore/views/course.py:342` → `_create_or_rerun_course` (**:1184**) | **`POST`** JSON | **`is_content_creator(user, org)`** | **Sí, las dos cosas** |

**El hallazgo:** las dos piezas que *se llaman* `course_rerun` son de lectura y piden el permiso más caro de la
plataforma; **la que escribe no se llama rerun y pide el permiso de creador de contenido.** `_create_or_rerun_course`
lee del JSON `org`, `number`/`course`, `display_name`, `start`, `end`, `run` y, **opcionalmente, `source_course_key`**:

- **con `source_course_key`** → `rerun_course(...)` → `{"url": …, "destination_course_key": "<key>"}` (clona)
- **sin `source_course_key`** → `create_new_course(...)` → `{"url": …, "course_key": "<key>"}` (**crea de cero**)

### 🔵 Las tres respuestas que el gap 57 pedía

**(a) ¿Acepta un curso vacío de plantilla como origen?** **La pregunta quedó sin objeto, y eso es la buena noticia:**
no hace falta plantilla ninguna, porque **`create_new_course` vive en el mismo endpoint** y se activa simplemente
*omitiendo* `source_course_key`. El *bootstrap* con curso plantilla que **P63** iba a cotizar **no es necesario**.

**(b) ¿Qué devuelve —el `course_key` sincrónico o una tarea a pollear?** **Las dos cosas, y conviene no confundirlas.**
`rerun_course` (**:1331**) calcula `destination_course_key` con `store.make_course_key` bajo `default_store('split')` y
**lo devuelve sincrónicamente**; el copiado de contenido se despacha a **Celery** (`rerun_course_task.delay(*args)`,
**:1375**) y su progreso se sigue por **`CourseRerunState` / `CourseRerunUIStateManager`** (estados `FAILED` /
`SUCCEEDED`). O sea: **la clave existe en la respuesta, el contenido todavía no.** Cualquier automatización que escriba
en el curso recién clonado inmediatamente después del POST corre contra una copia en vuelo.

**(c) ¿Qué permisos pide?** **`is_content_creator(user, org)`** para el POST que crea o clona —**no `GlobalStaff`**—, más
`has_studio_write_access` sobre el curso **origen** dentro de `rerun_course`, y también sobre el **destino** si cambian
`org` o `course`. `GlobalStaff` sólo gatea las dos vistas GET de formulario. **Para un despliegue multi-tenant esto
cambia la cotización**: el alta de cursos se delega por organización, no por superusuario.

🔴 **Y una trampa operativa que hay que escribir porque rompe en runtime:** `rerun_course` lee
**`fields['display_name']`** sin guarda (**:1359**), pero `_create_or_rerun_course` sólo puebla esa clave
**`if display_name is not None`**. **Omitir `display_name` en un rerun levanta `KeyError`**, no un 400 prolijo. En la
práctica `display_name` es **obligatorio para clonar** y opcional para crear. Además `rerun_course` **resetea**
`advertised_start`, `enrollment_start`, `enrollment_end` y `video_upload_pipeline`, y hace
`add_instructor(destination_course_key, user, user)`: el que clona queda instructor del clon.

🔵 **La regla de método que deja este pase (tendencia 95):** **medir el árbol versionado de un API no es medir su
superficie HTTP.** Un proyecto con años encima suele tener la escritura en el handler viejo y la lectura prolija en el
REST nuevo. Cuando una medición concluye *«no se puede»*, hay que preguntarle **a la vista legacy y al `urls.py` raíz**
antes de publicarlo. El pase 31 midió tres canales independientes y los tres coincidieron —y aun así la conclusión
salió mal, porque **los tres miraban el mismo lado del proyecto**. Coincidencia de fuentes no es cobertura de fuentes.

### 🔵 Gap 59 CERRADO — y la propagación **es segura por omisión**, que era justo lo que había que saber

`SyncFromUpstreamView.post` (`contentstore/rest_api/v2/views/downstreams.py:510`) acepta JSON opcional:

```json
{ "override_customizations": false, "keep_custom_fields": [] }
```

**La respuesta a «¿sobrescribe, rechaza o marca conflicto?» es ninguna de las tres: preserva.**
`override_customizations` **vale `False` por omisión**, de modo que **un `sync` no pisa los campos que el docente
personalizó localmente** a menos que el llamador lo pida explícitamente. Y cuando lo pide, `keep_custom_fields` da
granularidad **campo por campo** para blindar algunos de todas formas.

**Entonces la propagación de la tendencia 91 es segura para contenido que el docente toca**, y el riesgo queda
**invertido**: el peligro no es el `sync` por defecto, es **un integrador que manda `override_customizations: true` sin
`keep_custom_fields`**. Eso es una línea de *code review*, no un rediseño.

Dos cosas más que el mismo archivo contesta:

1. 🔴 **El caso `video` destruye transcripciones antes de copiar.** Si `block_type == "video"`, el `post` llama
   **`clear_transcripts(downstream)`** *antes* de `sync_library_content` — «delete all transcripts so we can copy new
   ones from upstream». Si el *upstream* no las trae, **se pierden**. Para accesibilidad esto es material: las
   transcripciones son requisito, no adorno.
2. **`downstreams/` sí tiene escritura además de `sync`** — son **cuatro** operaciones, no una:

| Operación | Qué hace |
|---|---|
| `POST downstreams/{usage_key}/sync` | Acepta la actualización (con los dos flags de arriba) |
| `DELETE downstreams/{usage_key}/sync` | **Rechaza** la actualización (`decline_sync`) → `204`. El docente puede decir no. |
| `PUT downstreams/{usage_key}` | Fija o edita el vínculo *upstream* (`upstream_ref`, con parámetro `sync` `"true"`/`"false"`) |
| `DELETE downstreams/{usage_key}` | **Corta** el vínculo (`sever_upstream_link`) y borra el `ComponentLink`/`ContainerLink` → `204` |

⚠️ **Caveat que hay que repetir en material de cliente:** las cuatro clases del módulo están rotuladas
**`[ 🛑 UNSTABLE ]`** en el propio *docstring*. Es API de biblioteca-a-curso usable hoy y **sin contrato de
estabilidad**.

### 🟢 Acción 3 — el registro de paquetes rindió **un MCP MIT**, y lo rindió **en el README, no en la descripción**

Se corrió `registry.npmjs.org/-/v1/search` sobre **QTI, xAPI, SCORM** y la pregunta desambiguada de **CASE**, más sondeo
directo a **PyPI**. Resultado por estándar:

| Estándar | ¿MCP? | Lo que hay, verificado |
|---|---|---|
| **SCORM / cmi5 / LTI 1.3** | 🟢 **SÍ** | **`coursecode`** — **MIT** — [course-code-framework/coursecode](https://github.com/course-code-framework/coursecode) — **servidor MCP incorporado** |
| **QTI** | 🔴 No | **`LongsightGroup/qti3`** — **MIT**, TypeScript, **12 paquetes** publicados. Tiene `AGENTS.md`, no MCP |
| **xAPI / LRS** | 🔴 No | `tincan` (PyPI, **Apache-2.0**, `RusticiSoftware/TinCanPython`), `learning_locker` (npm). **Dos colisiones nuevas, abajo** |
| **CASE** (gap 51) | ⚪ **Método falló** | npm devuelve **1.696.870** objetos de ruido. **Gap 51 sigue abierto** |

🟢 **El hallazgo del pase, y es de capa, no de repo:** **`coursecode`** (**MIT**, `coursecode@0.1.61`) es un framework de
*authoring* multi-formato por CLI que cubre **SCORM 1.2, SCORM 2004, cmi5 y LTI 1.3** en una sola pieza permisiva, y
**trae un servidor MCP incorporado** que habla con Claude Code, Codex y Cursor. Es **la primera puerta MCP de la capa de
empaquetado** de esta KB.

🔵 **Y el método importa más que el hallazgo:** **la descripción del paquete en npm no dice «MCP» en ninguna parte.** El
barrido por campo `description` —que es el que esta KB venía corriendo— **lo habría declarado ausente**. Apareció al
**abrir el README**, que es exactamente lo que la tendencia 89 manda hacer y lo que el barrido automático se saltea.
**Donde la tendencia 89 dice «abrir el README», no es una formalidad: es el único canal donde esto era visible.**

🟢 **El segundo hallazgo rompe un registro propio:** el pase 28 midió por tres métodos que la capa QTI utilizable era
**PHP** (`oat-sa/qti-sdk`). **Ya no.** [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) es **MIT**,
**TypeScript**, y publica **12 paquetes** —`qti3-core` (parser/validación/scoring, **cero dependencias de terceros**),
`-player` (web component), `-player-react`, `-player-preact`, `-conformance`, `-a11y`, `-fixtures`, `-pnp`, `-writer`,
`-migrator` (QTI 1.2/2.x → QTI 3), `-transcoder` (QTI 3 → 1.2/2.x), `-cli`—. `@longsightgroup/qti3-migrator@0.13.1`
registra `modified` **2026-10-01**: se publicó **ayer**. Y `LongsightGroup` **ya estaba en esta base por OneRoster**, de
modo que es el mismo actor cubriendo un segundo estándar.

⚠️ **Honestidad de adopción, que esta KB se debe después de la corrección de estrellas del pase 31:** los dos hallazgos
headline tienen **5 ★ cada uno**. Son hallazgos **de capacidad y de licencia, no de adopción**. Se registran porque
resuelven un bloqueo técnico con licencia permisiva, y hay que presentarlos así: **capacidad verificada, comunidad
mínima.** `@citolab/qti-convert-local-ai` existe y es relevante, pero es **GPL-3.0-only** — queda fuera de lo que
Globant puede componer sin contagio.

### 🔴 Colisiones de término **5 y 6** — y las dos se llaman «xapi»

Esta KB venía con cuatro colisiones registradas. **Van seis, y las dos nuevas son el mismo término:**

- **`xapi-to`** (npm, **MIT**, [xapi-labs/xapi-cli](https://github.com/xapi-labs/xapi-cli), `modified` 2026-09-29) se
  presenta como *«Agent-friendly CLI for xAPI — discover and call capabilities and APIs»* e **instala un skill de
  agente** (`npx skills add xapi-labs/xapi-cli`). Parece **exactamente** la puerta agéntica del xAPI educativo. **No lo
  es.** Su README —47.905 caracteres— tiene **cero** menciones de *«Experience API»*, *«Tin Can»* o *«learning
  record»*, y en cambio habla de **BlockPI RPC, Binance Web3, cripto, dominios/DNS**. Es un *marketplace* de APIs
  comerciales que se llama xAPI.
- **`xapi-python`** (PyPI, **MIT**) es **«The xStation5 API Python library»**: el API del **bróker de forex XTB**.

🔵 **La regla que queda (tendencia 96):** **«xAPI» es el acrónimo más sobrecargado de este dominio**, y las tres cosas
que devuelve —aprendizaje, cripto, forex— **comparten nombre exacto**. Para esta capa hay que buscar
**`"Experience API"` o `"Tin Can"`**, nunca `xapi` a secas; y como las dos trampas son **MIT y activas**, el filtro de
licencia **no** las descarta. Un barrido que sólo mire nombre y licencia las habría promovido a la tabla.

⚪ **Y la cuarta sub-acción no se pudo hacer con este método, lo cual también es dato:** `registry.npmjs.org` hace **OR**
sobre texto libre, así que `"competencies and academic standards exchange"` devuelve **1.696.870** resultados
(`@urql/exchange-retry`, `@univerjs-pro/exchange-client`, ASN.1…). **El registro de paquetes no sabe desambiguar un
estándar de nombre multi-palabra.** El **gap 51** sigue abierto y ahora con un método descartado por escrito: hay que
atacarlo por el **nombre del proyecto implementador**, no por el del estándar.

### 🟢 Un agente nuevo de verdad, el primero en ocho pases

[JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) — **Apache-2.0**, **448 ★**, Python. Destila
**videos, PDFs, transcripciones y apuntes en Agent Skills docentes con trazabilidad a la fuente**: extrae diagnósticos,
flujos de trabajo, rúbricas, plantillas, reglas de transferencia y modos de falla; emite paquetes de conocimiento
compatibles con **OKF**; fusiona varios cursos preservando campos de habilidad; corre sobre Codex, Claude Code, OpenClaw
y Hermes. **Por qué entra a `agents/top.md` y los últimos siete pases no tuvieron altas:** no es material didáctico
*sobre* AI ni un wrapper genérico — es **la pieza que convierte el material de un docente en la metodología ejecutable
de un agente**, que es el eslabón que esta base venía declarando vacío entre `education-agent-skills` (skills escritas a
mano) y los tutores.

⚠️ **Señal temprana, con el caveat por delante:**
[mizcausevic-dev/mcp-ai-tutor](https://github.com/mizcausevic-dev/mcp-ai-tutor) — **AGPL-3.0**, **0 ★**, TypeScript, **10
commits** — expone **seis** tools MCP para revisar *AI Tutor Cards* en compra institucional:
`tutor_card_well_known_url`, `_fetch`, `_validate`, `_inspect`, `_subject_check` y `_coppa_check`, con banderas de
**FERPA / COPPA / GDPR** y una regla condicional (edad mínima < 13 exige bandera de cumplimiento). **Ataca el bloqueador
regulatorio número uno de las cuatro regiones** y lo hace por el canal correcto —`.well-known` + MCP—, pero con
**AGPL-3.0 y cero estrellas no es componible ni adoptado**. Se registra como **idea de especificación a vigilar**, no
como fila de `agents/top.md`. Lo que vale es la forma: **una ficha pública y verificable por tool del tutor**.

### 🔴 Gap 56 RESUELTO — y la argumentación EMEA que esta KB tenía escrita **estaba mal aplicada**

El barrido regional de EMEA entregó el calendario que faltaba. **Las dos fechas incompatibles que esta base publicaba
eran las dos correctas, sobre obligaciones distintas** — y la que se usó para vender era la que no correspondía:

| Clase de obligación | Fecha | Aplica a educación |
|---|---|---|
| **Aplicación general** del AI Act (incl. **transparencia**, art. 50) | **2026-08-02** — **vigente hoy** | Sí, las de transparencia |
| **Anexo III, alto riesgo *stand-alone*** | **2026-08-02 → 2027-12-02** (postergada) | **Sí — acá vive educación** |
| Art. 6(1), alto riesgo **embebido** en producto regulado | **2028-08-02** | Sólo si va embebido |

Educación es **uno de los ocho supuestos del Anexo III** y entra por **evaluación de resultados de aprendizaje,
selección de postulantes y monitoreo durante exámenes**. El **Digital Omnibus on AI** movió esa fecha: acuerdo político
**2026-05-07**, aval del Parlamento **2026-06-16**, adopción del Consejo **2026-06-29**, publicación en el DOUE
**2026-07-24**, **en vigor 2026-07-27**.

🔵 **La corrección comercial, que es lo que descarga riesgo:** el pase 28 escribió *«rige desde 2026-08-02»* para el alto
riesgo educativo y **sobre eso se construyó el pitch de EMEA**. **Post-Omnibus eso es falso.** El pitch correcto es de
dos tiempos y es **más vendible, no menos**: *«las obligaciones de transparencia ya rigen —desde agosto de 2026—; la
evaluación de conformidad del Anexo III vence el 2 de diciembre de 2027, y eso es el tiempo que tienen para hacerla
bien»*. Vender una fecha vencida que no venció quema credibilidad en la primera consulta al área legal del cliente.

⚠️ **Confianza de esta resolución, declarada:** **cinco fuentes legales secundarias independientes concuerdan** en
`2027-12-02` y en la cronología del Omnibus. **El texto primario no se pudo abrir**: `artificialintelligenceact.eu`,
`digital-strategy.ec.europa.eu` y el análisis de Gibson Dunn están **bloqueados por el proxy de egreso** de este
entorno. **No es verificación primaria** y no debe citarse como tal en material de cliente sin abrir el DOUE. Queda
como acción para el pase siguiente.

### 🗺️ Las cuatro regiones rindieron — ninguna quedó en silencio

- **North America** — **86 %** de las organizaciones educativas ya adoptaron AI generativa. **134 proyectos de ley en 31
  estados** en la sesión 2026: **California AB 1159** prohíbe usar datos de alumnos para entrenar modelos; **Idaho SB
  1227** exige protecciones de privacidad; **Oklahoma** y **Maryland** exigen supervisión humana y **prohíben decisiones
  de alto impacto sobre alumnos tomadas por AI**; Georgia y Mississippi suman créditos de CS con AI. **Cuatro estados
  —Idaho, Maryland, Oklahoma, Virginia— obligan a política distrital de AI**, no sólo guía estatal. Despliegues:
  **Gemini for Education** en **+1.000** instituciones de educación superior; piloto de tutoría **Khanmigo** en Maryland
  con **~4.350** alumnos en dos condados.
- **EMEA** — gobernada por el calendario de arriba (**gap 56**). La mayoría de las instituciones está en modo
  **piloto y pre-cumplimiento**, no en enforcement. Señal técnica de peso para Globant: **los distritos con exigencia de
  residencia de datos autoalojan modelos de pesos abiertos** (Llama 3, Mistral) en lugar de consumir API. Eso convierte
  el *stack* soberano —Ollama/vLLM + LMS open source— en requisito, no en preferencia.
- **APAC** — es la región que **legisló más rápido**. **Corea del Sur**: *AI Basic Act* **vigente 2026-01-22**, que
  consolidó **19 proyectos** y la vuelve la **segunda jurisdicción del mundo** con ley integral después de la UE.
  **Vietnam**: ley nacional de AI adoptada en **diciembre de 2025**, vigente **marzo de 2026**, y **nombra educación
  como sector de alto riesgo** —evaluación automatizada y monitoreo de conducta—. **Japón** y **Taiwán** redactan ley y
  montan institutos de *testing*; **Singapur** apuesta a marcos y toolkits (**AI Verify**, que esta base ya tiene
  catalogado). Mercado dominado por China, India y Japón; *players* citados: Google, Microsoft, IBM, Pearson, Byju's.
- **LATAM** — **la adopción va por delante del mundo y la regulación por detrás.** *AI in Higher Education LATAM Survey
  2026* (Digital Education Council, con el Institute for the Future of Education del **Tec de Monterrey**, más **AIGEN**
  y **RIE360**): **92 % de estudiantes** y **79 % de docentes** usan AI activamente —por encima del promedio global—, y
  **94 % de docentes** espera usarla a futuro. Pero **65 % de los estudiantes teme que la AI vuelva superficial el
  aprendizaje**. Regulación fragmentada y a distintas velocidades: proyecto de ley en **Brasil**, marco en **Chile**,
  **CONPES 4144** en **Colombia** (política nacional con presupuesto hasta 2030), reglas sectoriales en **México**.
  🔵 **La lectura comercial:** en LATAM no hay que vender adopción —ya ocurrió, sin gobernanza—. Hay que vender
  **gobernanza retroactiva y evidencia de aprendizaje**: el 65 % de desconfianza estudiantil es el *driver* de compra,
  y es el mismo problema que `lineage-skill` (trazabilidad a la fuente) y las *AI Tutor Cards* atacan.

## 2026-10-02 (pase 31) — el pase que **da vuelta la consigna que traía**: los endpoints `v0` que el pase 29 mandó a medir *como los recomendados* están **deprecados en favor de `v1`**, y el bloqueo real no es la versión, es que **ninguna de las cinco versiones crea el curso**

**Lo que se hizo:** el barrido obligatorio completo —**cuatro búsquedas globales y cuatro regionales**, con el año
**calculado** (2026)— más las **tres acciones** del pase 30 y la **acción 1 pendiente del pase 29** (el gap 50, que el
pase 30 no ejecutó). **Las cuatro rindieron**, y la de más valor comercial rindió *contra* la premisa con la que estaba
escrita.

### 🔴 Gap 50 CERRADO leyendo el código, y cierra invirtiendo la consigna

El pase 29 dejó escrito: *«medir los endpoints `v0` de authoring de Open edX, **que son los que el propio repo
recomienda** sobre el `v1` experimental»*. Se midió. **La premisa es falsa en `master`:**

- `cms/djangoapps/contentstore/rest_api/v0/views/xblock.py` encabeza con una directiva
  **`.. deprecated::`** explícita: *«These views are superseded by `XblockViewSet` in
  `…rest_api.v1.views.xblock`. Use `/api/contentstore/v1/xblock/` going forward. These v0 endpoints will be removed in
  a future release.»* Y no es sólo prosa: define `_DEPRECATION_MSG` y **emite `DeprecationWarning` en runtime en las
  cinco operaciones** (`retrieve`, `update`, `partial_update`, `destroy`, `create`).
- `v1/urls.py` **ya registra el xblock por router**: `_router.register(r'xblock', XblockViewSet, basename='xblock')`,
  con `create / retrieve / update / partial_update / destroy`.
- El comentario que originó la consigna sigue ahí, **al final** de `v1/urls.py`: *«Do not use under v1 yet (Nov. 23).
  The Authoring API is still experimental and the v0 versions should be used»*. Es de **noviembre de 2023**, y está
  escrito **después** del `register` que ya montó el xblock en `v1`.

🔵 **La regla de método que deja este pase (tendencia 88):** cuando dos señales del mismo repo se contradicen, **gana la
que el runtime ejecuta**, no la que el comentario afirma. Un `DeprecationWarning` que se emite es un hecho; un
comentario fechado es una opinión vieja. El pase 29 ya había aprendido la mitad de esto —anotó que el aviso de
«experimental» *«encabeza una sección vacía y es de 2023»*— y **el pase 30 lo volvió a tomar como recomendación
vigente**. La KB se contradijo a sí misma en dos pases consecutivos.

### 🔵 Y el bloqueo real estaba una capa más arriba: **no hay creación de curso en ninguna versión**

Se leyeron **las cinco versiones** del API de contentstore (`rest_api/urls.py` monta `v0`…`v4`):

| Versión | Qué expone | ¿Crea curso? |
|---|---|---|
| `v0` | authoring **deprecado**: xblock, `file_assets`, videos/transcripts, `grading`, `advanced_settings`, `tabs`, Course Optimizer (`link_check`, `rerun_link_update`) | No |
| `v1` | `XblockViewSet` (router), `course_settings`, `course_details`, `course_index`, `course_team`, `course_grading`, `certificates`, `textbooks`, `group_configurations`, `container_children`, `course_rerun`, `proctored_exam_settings` | No — sólo **`course_rerun`** (clona) |
| `v2` | `home/courses` (**sólo `GET`**: `HomePageCoursesViewV2` define `get` y nada más), **`downstreams/*`** (ver abajo), `validate/numerical-input` | No |
| `v3` | ViewSets `home`, `course_details`, `authoring_grading` | No |
| `v4` | ViewSet `home/courses` | No |

**Y la tercera confirmación, independiente de las dos anteriores:** el conector oficial del propio proyecto tiene
**19 herramientas de escritura y ninguna se llama `create_course`** (medición abajo). Tres capas medidas por separado
dicen lo mismo: **el authoring de todo lo que vive *adentro* del curso está resuelto y es alcanzable por REST; crear la
cáscara del curso no lo es.** El único primitivo de nivel curso alcanzable es **`course_rerun`**, que **clona** un curso
existente (**gap 57**: queda sin medir si `course_rerun` acepta un curso plantilla vacío como origen, que es lo que
decide si el bootstrap es de una línea o de una intervención manual).

Eso **no parte P55: lo cotiza entero con un bootstrap declarado** — curso plantilla + `course_rerun`, y de ahí en
adelante todo por API. Ver **P63**.

### ✅ Gap 55 MEDIDO sin Docker: 35 rutas, 19 escrituras, 6 *scopes*, y **8 escriben sin confirmación**

El pase 30 pedía `tutor plugins enable openedxmcp` para contar herramientas reales contra las 35 rutas de fachada. **No
hay demonio de Docker en este entorno** (límite ya registrado), así que se midió por el canal que sí existe: **se bajó
el wheel publicado de PyPI y se leyó** (`openedx_mcp-0.1.5-py3-none-any.whl`, 46.685 bytes, 2026-07-25).

- **Licencia confirmada en el artefacto**, no en la metadata: `dist-info/licenses/LICENSE` es
  **GNU AFFERO GENERAL PUBLIC LICENSE v3**. **AGPL-3.0 queda ratificado.**
- **35 rutas exactas** — **28 en LMS** (`api/mcp/urls.py`) + **7 en CMS** (`cms_urls.py`). El «35» del pase 30 era
  correcto.
- **19 herramientas de escritura**, todas detrás del decorador `@audited_write`, repartidas en **6 scopes**:
  `WRITE_COURSES` 6, `WRITE_USERS` 4, `WRITE_ENROLLMENT` 3, `WRITE_CERTIFICATES` 3, `WRITE_ROLES` 2, `WRITE_REPORTS` 1.
- **Las 7 rutas CMS son la superficie de authoring del agente:** `outline` (lectura), `courses/settings/`,
  `blocks/create/`, **`blocks/create-tree/`**, `blocks/update/`, `blocks/publish/`, `blocks/delete/`.
  🔵 **`create-block-tree` es el hallazgo útil:** crea **un árbol** de bloques en una llamada —secciones, subsecciones y
  unidades juntas—, que es exactamente lo que un agente autor necesita y lo que el endpoint REST crudo obliga a hacer
  bloque por bloque.

🔴 **Y la medición encontró algo que la documentación no dice: 11 de las 19 escrituras exigen *confirm token* y 8 no.**

| Sin confirmación (8) | Con confirmación (11) |
|---|---|
| `create_xblock` (×2 vistas), `update_xblock`, `update_course_settings`, `enroll_user`, **`unenroll_user`**, `generate_certificate`, `submit_report` | `bulk_enroll`, `create_user`, `deactivate_user`, `delete_xblock`, `instructor_access`, `invalidate_certificate`, `publish_xblock`, `regenerate_certificates`, `request_retirement`, `reset_attempts`, `set_role` |

El modelo de amenaza que el pase 30 citó del propio código —*«a looping agent… a retry storm that mass-enrols or
deletes»*— **está implementado contra la operación masiva, no contra la repetida**: `bulk_enroll` pide confirmación,
pero **`unenroll_user` de a uno no**. Un agente en bucle no puede desmatricular a un curso entero de una llamada, y
**sí puede desmatricular a 500 alumnos en 500 llamadas sin un solo token**. Es un hallazgo de arquitectura, no un bug
de la librería —la asimetría es deliberada y está en el decorador— y **es una condición de despliegue que un
*engagement* tiene que cubrir afuera del conector** (ver **P63**, rail de cuota por sujeto).

### ✅ Gap 54: la acción del pase 30 rinde, y aparece **una segunda puerta OneRoster — y es MIT**

El pase 30 dejó la consigna de **preguntarle al registro de paquetes por el nombre del proyecto, no del protocolo**. Se
ejecutó contra `registry.npmjs.org` y `pypi.org`, leyendo el README de cada paquete y buscando «MCP» adentro:

- 🟢 **`@eduware/oneroster` v1.2.11 — MIT — trae servidor MCP propio.** README literal: *«the included MCP server for
  tool-based integrations»*, *«The package includes an MCP server that exposes SDK operations as tools»*, con un
  ejecutable `mcp` empaquetado. **13 versiones, creado 2026-01-23, última modificación 2026-07-10.** OneRoster **1.1 y
  1.2**, más un perfil `ClassLink` de sólo lectura. **Es la primera puerta OneRoster permisiva de esta KB** — la que ya
  estaba registrada, `trilogy-group/oneroster-ts`, es **0BSD** y aparece en npm como `@superbuilders/oneroster` v0.7.0
  (12 menciones de MCP en el README; mismo repo, confirmado por el campo `repository`).
- ⚠️ **Pero su repo declarado no es verificable:** `github.com/Eduware-Inc/eduware-oneroster` devuelve **404** por
  `raw.githubusercontent.com`. **El paquete es real y verificable en el registro; el repo es una afirmación que no se
  puede comprobar.** Se registra con la URL del registro, no con la del repo (**gap 58**).
- 🟢 **`@longsightgroup/oneroster` v0.3.0 — MIT — repo verificado** (`LongsightGroup/oneroster`, README y
  `package.json` responden 200). *«Faithful OneRoster 1.2 for TypeScript — CSV and portable REST contracts.»* Sin MCP.
- Hay además `@universis/one-roster` v2.30.2 y `@timeback/oneroster` v0.3.3. **La capa OneRoster no es «un SDK con
  MCP»: son al menos seis implementaciones y dos de ellas sirven MCP** (tendencia 89).

### ⚠️ Caliper: código nuevo, licencia ausente

`@timeback/caliper` v0.3.3, **modificado 2026-09-25** —el paquete más fresco de todo este pase— es un *«Caliper
Analytics client SDK»* y **no declara licencia** (`license: null` en el registro, sin repo declarado). Esto **afina** lo
que esta KB venía diciendo: no es que Caliper se quedó sin código desde que dejó de ser open source en 2023, es que
**hay código nuevo de 2026 y no se puede usar**, que es peor y más accionable. No entra como fundación; entra como
advertencia de licencia.

### ✅ OpenBadges 3.0 entra a la KB, y es Apache-2.0

`@ajna-inc/openbadges` v0.6.3 — **Apache-2.0** — *«OpenBadges v3.0 module for Credo-TS with OAuth 2.0 provider
support»*, modificado 2026-05-19. Esta KB tenía registrado que **CaSS implementa OB 2.0 y no 3.0** y no tenía ninguna
pieza de **OB 3.0**. Ya la tiene, y es permisiva. ⚠️ Mismo límite que `@eduware`: **no declara repo**, así que se cita
por registro.

### ✅ Gap 42 (LTI con MCP) sigue cerrado, pero ahora **medido en los dos lenguajes**, no por etiqueta

- **`ltijs` v7.0.6 — Apache-2.0 — repo verificado** (`Cvmcosta/ltijs`), modificado **2026-09-18**: se leyó el README
  completo y tiene **0 menciones de MCP**. Vivo, mantenido, sin puerta de agente.
- **`pylti1p3` v2.0.0 — MIT — última publicación `2022-11-20`**, 29 releases. 🔴 **El lado Python de LTI 1.3 lleva casi
  cuatro años sin release**. ✅ Su repo (`dmitry-viskov/pylti1.3`) **sí existe** — ver la autocorrección de este pase
  más abajo, que es el hallazgo de método que más vale de los dos.
  **La asimetría es el hallazgo (tendencia 90):** el mismo estándar obligatorio tiene un SDK JS mantenido este mes y un
  SDK Python congelado en 2022. Para un *engagement* en Python sobre LTI, eso es riesgo de dependencia, no una nota al
  pie.

### 🔵 Una capa que treinta pases no vieron: el *upstream/downstream* de Open edX

Leyendo `v2/urls.py` apareció algo que no está en ningún archivo de esta KB: **`downstreams/`**, con cuatro vistas —
`DownstreamListView`, `DownstreamView`, `DownstreamSummaryView` y **`SyncFromUpstreamView`** (`downstreams/<usage_key>/sync`).
Es la API de **reutilización de contenido de Libraries v2**: un bloque se edita **una vez** en la biblioteca y se
**sincroniza** a los N cursos que lo consumen. Para un agente autor eso cambia la economía del patrón: no es «editar N
cursos», es «editar uno y propagar». **Es el primitivo de propagación que P55 y P63 necesitaban y que se estaba
cotizando como trabajo manual** (tendencia 91).

### ⚠️ Nota de método: qué canal verifica en este entorno

Se intentó cumplir el *«verificá cada URL con `curl -sI`»* y **el canal obvio no sirve acá**:

| Canal | Resultado |
|---|---|
| `github.com/...` (HEAD) | **403** — el proxy lo rechaza para todo repo, incluso `openedx/edx-platform` |
| `www.npmjs.com/package/...` | **403** |
| `api.github.com` | **403** — *«GitHub access to this repository is not enabled for this session»* (scoping de sesión) |
| `raw.githubusercontent.com/<owner>/<repo>/HEAD/README.md` | **200** — y **404 real** cuando el repo no existe |
| `registry.npmjs.org/<pkg>` | **200**, con licencia, fechas y README completo |
| `pypi.org/pypi/<pkg>/json` y `files.pythonhosted.org` | **200**, y el wheel se puede bajar y leer |

🔵 **Por eso este pase no publica ni una estrella de GitHub:** sin `api.github.com` no hay forma de medirlas de primera
mano, y **la regla de esta KB es no escribir cifras que no se midieron**. Las altas de este pase se publican con
**licencia, versión, fecha de modificación y canal verificado**, que es lo que sí se pudo comprobar.

### 🔴 Autocorrección del propio pase, y es el hallazgo de método que más vale de este barrido

**Este pase casi publicó un falso negativo, y lo salvó por accidente.** La primera pasada de verificación usó
`raw.githubusercontent.com/<owner>/<repo>/HEAD/README.md` como test de existencia y declaró **404** —es decir, *«repo no
verificable»*— para **dos** repos. Al correr el mismo test sobre `openedx/edx-platform` —un repo que este pase **ya había
leído entero**, archivo por archivo— **también dio 404**. Eso delató el método, no el repo: `edx-platform` publica
**`README.rst`**, no `README.md`.

Re-medido contra **ocho rutas de metadatos** (`README.rst`, `README.md`, `readme.md`, `package.json`,
`pyproject.toml`, `setup.py`, `LICENSE`, `.gitignore`):

| Repo | Resultado real |
|---|---|
| `openedx/edx-platform` | ✅ **existe** — `README.rst`, `package.json`, `pyproject.toml`, `LICENSE` en 200 |
| `dmitry-viskov/pylti1.3` | ✅ **existe** — `README.rst`, `setup.py`, `LICENSE` en 200. **Y esta KB ya lo tenía registrado con 138 ★ desde un pase anterior**, así que el falso negativo contradecía su propio archivo |
| `Eduware-Inc/eduware-oneroster` | 🔴 **no existe públicamente** — **las ocho rutas en 404**. Ésta sí se sostiene |

**La tendencia 87 del pase 30 ya decía exactamente esto** (*«"No hay README" no es "no hay repo": cada ecosistema tiene
su archivo de metadatos»*) **y este pase la repitió de todos modos.** Dos conclusiones, y la segunda es la importante:

1. **Un test de existencia de un solo archivo no es un test de existencia.** Son **ocho rutas**, o como mínimo
   `README.rst` + el manifiesto del ecosistema (`package.json` / `pyproject.toml` / `setup.py` / `composer.json`).
2. 🔵 **El control que lo atrapó hay que convertirlo en rutina: correr el test de verificación sobre un caso que ya se
   sabe positivo.** `edx-platform` funcionó como **control negativo del método**. Cuando un barrido declara una ausencia,
   **tiene que declararla junto al resultado del control** — si el control también falla, lo que falló es el
   instrumento. Es la versión barata de lo que el pase 24 aprendió ejecutando en vez de leer.

**Y queda una regla de prioridad entre fuentes:** cuando una medición nueva contradice un registro propio de esta KB
—138 ★ para un repo que el test dice que no existe—, **la contradicción se resuelve antes de publicar**, no después. El
registro viejo fue el que tenía razón.

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
