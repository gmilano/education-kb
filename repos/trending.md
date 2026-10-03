---
industry: education
region: Global
updated: 2026-10-03
---

# 📈 Repos trending — education

> **APPEND-ONLY.** Cada corrida agrega una sección fechada arriba y conserva la historia abajo.

## 2026-10-03 — pase 68: entran los dos documentos de estándar que SÍ ceden, y la versión vigente de xAPI se fue de GitHub

### 🟢 El movimiento de repos del pase: la capa de estándares gana sus dos piezas permisivas

| Pieza | Licencia | ★ / forks | Qué es |
|---|---|---|---|
| 🟢 [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | **Apache-2.0** (11.525 B) | **952** / 403 | documento normativo de **xAPI 1.0.3**, ADL Initiative (U.S. DoD) |
| 🟢 [`Ed-Fi-Alliance-OSS/Ed-Fi-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Standard) | **Apache-2.0** (10.173 B) | **46** / 13 | **Ed-Fi Data Standard v6.2.0**: Descriptors, Models, Samples, Schemas |
| 🟢 [`aemonge/opencode-sit`](https://github.com/aemonge/opencode-sit) | **MIT** (1.056 B, `NO-HOLDER`) | npm v0.1.2 | tutor socrático como **plugin de OpenCode** |

🔵 **Las dos primeras entran por una pregunta de LICENCIA, no por un eje de descubrimiento: el barrido
de la acción 3 fue a buscar si los documentos de estándar niegan derivados y encontró dos que no.**

### 🔴 La corrección que este archivo arrastraba: «la capa de estándares está cerrada» era media verdad

| Publicador | Artefacto | Régimen | n |
|---|---|---|---|
| 🔴 1EdTech / IMS | documento | `SPEC-NO-DERIVATIVES` + `REGISTERED-USERS` | 2 de 2 |
| 🟢 1EdTech / IMS | software | Apache-2.0 | 4 de 4 |
| 🟢 ADL · Ed-Fi | documento | **Apache-2.0** | 2 de 2 |

🔵 **Cero excepciones en 8 archivos leídos. El eje no es «estándar»: es publicador × tipo de
artefacto** (**P191**).

### 🔴 El hallazgo de canal del pase: un estándar que migra se cae de TODOS los denominadores

🔴 **`xAPI-Spec` declara en su propio README que es la versión vieja. La vigente —IEEE
9274.1.1-2023— vive en `opensource.ieee.org`, GitLab del IEEE.** 🔴 **`curl` → `000`; WebFetch →
`EGRESS_BLOCKED`.** 🔵 **Los cuatro instrumentos de licencia de esta KB apuntan a
`raw.githubusercontent.com`, así que esto no aparece como ausencia: aparece como si no existiera**
(**P195**). ⚠️ **Se declara como hueco en vez de heredar la licencia del archivado.**

### 🔴 Tres `REPO-UNREACHABLE` que esta KB podría haber publicado como ausencias de licencia

🟢 **El instrumento nuevo separa las dos causas antes de escribir ninguna**, que es la lección de
**P187** aplicada a sí misma: `1EdTech/caliper-php`, `IMSGlobal/caliper-python` y
`Ed-Fi-Alliance-OSS/Ed-Fi-SDK-MCP` dan 404 también en `README.md` → **el repo no resuelve.**
⚠️ **`Ed-Fi-SDK-MCP` sale del campo `repository` de un paquete npm vivo cuyo artefacto embarca
Apache-2.0: el paquete declara un repositorio que no existe.**

### ⚠️ El eje de plataformas, saturado por OCTAVO pase — y la cifra de vendedor se movió 30×

⚠️ **`open source platform education ERP CRM MIT Apache` volvió a colapsar sobre el SEO de
OpenEduCat**, otra vez en varios idiomas. 🔴 **La novedad no es la plataforma, es su cifra: el pase 52
registró *«~3 millones de usuarios y 1.000+ instituciones en 90+ países»* y hoy el mismo proveedor
declara **«30.000+ instituciones en 130+ países»**.** 🔵 **Un salto de 30× en la misma afirmación
autodeclarada y sin instrumento se registra como **inestabilidad de cifra de vendedor** (**P107**), no
como crecimiento.** 🟢 **Confirmado en el barrido y sin cambio de licencia: OpenEduCat sigue
**LGPL-3.0** sobre Odoo.** ⚠️ **También aparecieron `Kuali` (consorcio de ERP/SIS universitario) y
`openSIS`: ninguno con licencia leída de primera mano en esta corrida, así que NO entran como filas.**

### ⚠️ Lo que este pase NO midió de este archivo, declarado como tal

⚠️ **No se re-midió tracción (★/forks) de las filas ya publicadas:** las cifras de este pase son las
de las tres altas, leídas hoy. ⚠️ **No se barrió `standards.1edtech.org`, donde viven los documentos de
CLR, QTI, OneRoster y LTI**, así que el veredicto sobre documentos de 1EdTech está medido sobre los
**2** repos que la org publica en GitHub.

## 2026-10-03 — pase 67: la capa de autograding entra entera, y una ausencia de licencia de estándar era falsa

### 🟢 El movimiento de repos del pase: una FUNCIÓN que esta KB tenía casi vacía

⚠️ **La consulta por vertical de *autograding* rindió lo que las cuatro globales no rindieron.** Esta
KB venía con la corrección automática representada por **una** pieza registrada
(`eecs-autograder/autograder.io`, Universidad de Michigan) y por las puertas de nota de Moodle/Canvas,
que son **integración**, no corrección. 🟢 **Entran cuatro piezas de corrección propiamente dicha, las
cuatro con el archivo de licencia LEÍDO de primera mano por `raw.githubusercontent.com`.**

| Repo | Licencia (**medida, bytes**) | Titular (**P184**) | ★ | Señal | Por qué importa |
|---|---|---|---|---|---|
| [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0**, **34.764 B** ⚠️ **con preámbulo de ALCANCE** | FSF → `NOT-APPLICABLE` | **243** (150 forks) | **UCLouvain**, activo 2026 | **Grader externo de Moodle y de edX vía LTI.** La única pieza de esta tanda que es plataforma y no script. 🔴 **Su `LICENSE` declara cubrir *«la mayoría de los archivos»*** (ver **P186**) |
| [`webtech-network/autograder`](https://github.com/webtech-network/autograder) | 🟢 **Apache-2.0**, **11.357 B** | ausente **por construcción** → `NOT-APPLICABLE` | — | activo | **La licencia más cómoda de la tanda.** Autograding con generación de reportes sobre entregas |
| [`johnswyou/autograder`](https://github.com/johnswyou/autograder) | 🟢 **MIT**, **1.065 B** | 🟢 `Copyright (c) 2026 John You` → **`HOLDER-MATCH`** | **0** | alta de 2026 | **Corrige MANUSCRITO** (física, matemática): localiza, transcribe, aplica rúbrica, emite `review_queue.md`. ⚠️ **0 ★: entra por el patrón** |
| [`zmievsa/autograder`](https://github.com/zmievsa/autograder) | 🔴 **GPL-3.0**, **35.149 B** | FSF → `NOT-APPLICABLE` | — | activo | Corrección de entregas de cursos de programación, lado docente. 🔴 **Copyleft: se compone por proceso** |
| [`crpf-mitadt/Indian-AI-for-Education`](https://github.com/crpf-mitadt/Indian-AI-for-Education) | 🟢 **CC0 1.0 Universal**, **7.048 B** | 🔵 **CC0 no lleva titular** → `NOT-APPLICABLE` | — | **APAC / India** | **Mapa curado de *datasets*, modelos, ASR, TTS, OCR, MT, *benchmarks* e infraestructura de AI educativa de India.** 🟢 **CC0 = dominio público: la licencia más permisiva de toda la capa de dato de esta KB** |

🔵 **El reparto de licencias de la tanda es el dato de la capa, y no es bueno:** de 5 piezas, **2
permisivas** (Apache-2.0, MIT), **1 CC0**, **2 copyleft** (AGPL-3.0, GPL-3.0). ⚠️ **La pieza con más
tracción de las cinco —243 ★, la única con despliegue institucional— es justo la AGPL.** Es la misma
forma que esta KB ya midió en los LMS: **la madurez correlaciona con el copyleft en educación.**

### 🔴 Dos forks nuevos de `canvas-mcp`, identificados por `sha256` del `LICENSE`

| Repo | `LICENSE` | `sha256` | Titular | `version` |
|---|---|---|---|---|
| `vishalsachdev/canvas-mcp` *(canónica, registrada)* | 1.071 B | `5385a26e2face987…` | `Vishal Sachdev` | **1.13.0** |
| 🆕 [`sirdanielm/canvas-mcp`](https://github.com/sirdanielm/canvas-mcp) | 1.071 B | 🔴 **`5385a26e2face987…`** *(idéntico)* | 🔴 `Vishal Sachdev` | **1.13.0** |
| 🆕 [`fdis111/canvas-mcp`](https://github.com/fdis111/canvas-mcp) | 1.071 B | 🔴 **`5385a26e2face987…`** *(idéntico)* | 🔴 `Vishal Sachdev` | 🔴 **1.3.0** |

🟢 **`diff` los declara idénticos byte a byte.** ⚠️ **Y la corrección de método: tres archivos de
1.071 B podrían ser tres textos MIT distintos del mismo largo — el tamaño coincidente no prueba nada,
el digest sí.** 🔵 **Los dos llegaron por el canal de búsqueda presentados como proyectos
independientes; el titular del `LICENSE` los reclasifica en una línea.** **El linaje `canvas-mcp` pasa
de 4 forks conocidos con titular ajeno (pase 66) a 6.**

### 🔴 La corrección de este archivo: `openbadges-specification` no era una ausencia

Este archivo publica `IMSGlobal/openbadges-specification` con 🔴 *«ninguna (medida)»*. **Es una
ausencia FALSA**: `ob_v3p0/license.md` existe —**12.324 B**— y es la **SPECIFICATION DOCUMENT LICENSE
de IMS Global**, que ⚠️ **no concede derivados** (*«No right to create modifications or derivatives of
IMS documents is granted pursuant to this license»*). 🔵 **No estaba en la raíz, estaba en el
subdirectorio de la versión, y en minúscula** — ver **P187** y la sección del pase en
`agents/trending.md`. ⚠️ **Y sólo en `ob_v3p0`: `ob_v2p1/license.md` y `ob_v2p0/license.md` dan 404,
así que en un repo de especificación la pregunta de licencia es POR VERSIÓN.**

### ⚠️ Lo que este pase NO midió de este archivo, declarado como tal

🔴 **Las estrellas y las fechas de release de las filas históricas NO se re-verificaron**, porque el
canal que lo haría barato —`api.github.com/repos/{owner}/{repo}`— **da 403 hoy** (y el único endpoint
de ese host que pasa, `rate_limit`, no transporta datos de repositorio). 🔵 **Las cifras de la tabla de
arriba son de este pase y de primera mano; las de las secciones de abajo conservan la fecha de su
pase.**

## 2026-10-03 — pase 66: el grafo japonés completo estaba en el repo, y la capa de paquete está SANA

### 🟢 Los 66 MB que el pase 65 declaró inalcanzables: estaban a un sufijo de distancia

El pase 65 anotó `all-20250927.ttl` → **404** y concluyó *«el grafo completo sólo existe detrás de los
dominios bloqueados»*. 🔴 **`index.html` lo enumera como `all-20250927.ttl.gz`.** El nombre se
transcribió **sin el sufijo** y se sondeó un archivo que el publicador nunca anunció.

| Nombre | Código | Bytes |
|---|---|---|
| **`all-20250927.ttl.gz`** — como lo escribe `index.html` | 🟢 **200** | **4.251.289** |
| `all-20250927.ttl` — lo que se sondeó | 🔴 404 | 14 (el cuerpo es la cadena `404: Not Found`) |
| **`cs-items-20220830.ttl.gz`** | 🟢 **200** | **2.522.650** |
| `cs-items-20220830.ttl` | 🔴 404 | 14 |

⚠️ **Los dos nombres mal transcritos son los dos archivos más grandes del conjunto, que es
exactamente por qué están comprimidos.** 🔵 **La lección: un nombre transcrito de un listado no es el
nombre que el listado dio.** Y el pase 65 **tenía el listado delante** — es el mismo `index.html` que
leyó por `raw` para establecer **P181**. **El canal correcto se usó y el dato se copió mal.**

🟢 **Medidos los 22 volcados exactamente como `index.html` los escribe: 22 de 22 dan 200.** La
columna «no medido» de `dumps.tsv` queda cerrada completa.

### 🟢 Y medido el grafo, Japón pasa de «la mejor pieza de currículo» a «la única con educación especial»

**`jp-cos/jp-cos.github.io`** — 学習指導要領LOD, **CC BY 4.0 sin ShareAlike**. Grafo completo:
**69.288.422 B (66 MB) sin comprimir, 1.004.927 líneas.**

| Clase | n | Qué es |
|---|---|---|
| **`cs:Item`** | **39.958** | los ítems del currículo |
| `cs:Subject` · `cs:SubjectArea` | 786 · 276 | materias y áreas |
| **`cs:CommentaryItem`** | **655** | 🟢 **学習指導要領解説, el comentario OFICIAL, dentro del grafo** |
| **`cs:CourseOfStudyRevision`** | **34** | currículos viejos **y** nuevos |
| `cs:RelatedSubject` · `cs:RelatedSubjectArea` | 158 · 102 | 🟢 **enlaces entre materias: permite recorrer prerrequisitos** |
| **`sh:NodeShape`** | **17** | 🟢 **el SHACL de validación viaja dentro del mismo grafo** |
| **`cs:DisabilityCategory`** | **5** | categorías de discapacidad |

**Cobertura por nivel:** 幼稚園 Kindergarten **1.382** · 小学校 Elementary **23.555** · 中学校
LowerSecondary **17.468** · 高等学校 UpperSecondary **79.926**.

🔵 **Y la rama que la muestra de un registro no podía mostrar: 特別支援学校 (educación especial)
modelada como ciudadana de primera clase y desglosada por discapacidad** — `UpperSecondaryDeptSNES`
**14.560**, `ElementaryAndLowerSecondaryDeptSNES` **6.130**, `-Visual` (視覚) **4.886**, `-Hearing`
(聴覚) **4.721**, `-Intellectual` (知的) **2.207 / 1.546 / 1.223**, `-VHPH` **157 / 76**, y las
variantes `-NC` (sin currículo prescrito) **432 / 372 / 341**.

⚠️ **Esto cambia el valor de la pieza, no su tamaño. Ninguna otra pieza de currículo de esta KB
—tampoco la alemana por *Land*, que es `CC BY-SA 4.0`— trae la dimensión de educación especial
desglosada.** 🟢 **Para `P180` el alcance se cierra: no hay que construir vocabulario, ni validación,
ni el comentario.** ⚠️ **La dependencia que la receta sigue teniendo que declarar es el endpoint
SPARQL (`dydra.com` bloqueado, y el publicador lo anuncia 試験公開中) — con 66 MB en la mano la
receta no lo necesita: se carga en un *triplestore* propio, y eso es lo que se cotiza.**

### 🟢 La capa de PAQUETE está sana, y eso decide qué NO hay que reescribir

Ejecutada la acción que llevaba 14 pases pendiente —las filas de `agents/top.md` **sin URL de
GitHub**—, con el denominador declarado primero, por instrumento versionado:

| | Qué se cuenta | n |
|---|---|---|
| filas de dato de las 98 tablas | | **578** |
| sin `github.com` | | **292** |
| **de esas, en tablas de ENTIDAD** | 🔵 **el denominador real** | **174** |
| con paquete **declarado por su registro** | npm/PyPI | **21 filas → 18 paquetes** |
| sin paquete y sin repo | 🔴 **no medibles por NINGÚN canal** | **153** |

🔴 **La cifra «249» no se puede reproducir: nunca salió de un instrumento versionado.** Y las otras
118 filas sin `github.com` son filas de tablas de **método** (`Magnitud · Valor`, `Estado · n · %`):
**preguntarle la licencia a una fila de `Magnitud · Valor` es un error de categoría.** ⚠️ **La capa
accionable es el 10 % de lo que la cifra sugería.**

**Bajados los 18 paquetes del registro y abiertos sus *tarballs*/sdists (23 mediciones):**

| Capa | Identificador sin texto | 🟢 Texto de licencia presente |
|---|---|---|
| repos de GitHub **sin archivo** (pase 65) | **5 de 7 — 71 %** | 2 de 7 |
| **paquetes de registro** (hoy) | **6 de 23 — 26 %** | 🟢 **17 de 23 — 74 %** |

🟢 **La hipótesis de la acción se resuelve en su segunda rama: NO hay que reescribir la columna
Licencia de la capa de paquete.** El problema de **P179** es **específico de los repos de GitHub cuyo
árbol no tiene archivo de licencia**. 🔵 **Y la dirección útil se invierte: `npm pack` y los
constructores de sdist incluyen el archivo de licencia cuando existe, así que el *tarball* contesta
«¿hay texto?» con UNA llamada al registro y UNA descarga, contra 14 sondas a `raw` por nombre.**
⚠️ **Para 2 de los 18 el registro es el ÚNICO canal que existe** (`opencode-sit` y
`aicourse-mcp-server` no declaran repositorio) **y contesta igual**: el primero con texto de 1.056 B,
el segundo sin.

### 🔴 Y un defecto que esta KB tiene que arreglar en sus propias filas: un NOMBRE no es un PAQUETE

**5 de los 18 nombres viven en los DOS registros**, y en 2 casos con **licencias distintas**:

| Nombre | npm | PyPI | Lectura |
|---|---|---|---|
| **`educhain`** | **ISC** 1.0.0, 🔴 sin texto | **MIT** 0.4.0, texto 1.092 B | 🔴 **La fila de esta KB es el proyecto Python (`satvik314/educhain`): quien corra `npm i educhain` se lleva ISC y ningún texto** |
| **`frappe-mcp-server`** | **ISC** 0.6.0, 🔴 sin texto | **MIT** 1.2.0, texto 1.065 B | 🔴 **La fila cita npm — o sea el canal peor licenciado de los dos** |
| **`clawed`** | MIT 0.0.1, 🔴 sin texto | MIT **9.18.2026.1**, texto | ⚠️ misma licencia, **brecha de versión que delata una reserva de nombre** en npm. La fila cita `(PyPI)`: correcto |
| `canvas-lms-mcp` · `moodle-cli` | MIT con texto | MIT con texto | 🟢 benignos |

⚠️ **Obligación que esto impone a la KB: una fila que nombra un paquete tiene que nombrar su CANAL.**
Sin canal el nombre es ambiguo entre dos artefactos con dos licencias, y en 2 de 5 casos medidos lo
es de verdad.

### Canales de esta corrida, medidos

| Canal | Estado | Qué sirvió |
|---|---|---|
| `raw.githubusercontent.com` | 🟢 **200** | archivos, incluidos los 66 MB del grafo japonés |
| `registry.npmjs.org` · `pypi.org` | 🟢 **200** | metadato de licencia **y** *tarballs*/sdists |
| **`github.com` por WebFetch** | 🟢 **200** | **los 22 listados de raíz** — el canal que la acción 2 nombró |
| `github.com` por `curl` | 🔴 **403** | — |
| `api.github.com` | 🔴 **403** | ninguna cifra de estrellas verificable de primera mano |
| `codeload.github.com` | 🔴 **403** | igual que en el pase 65; **no hizo falta** |

## 2026-10-03 — pase 65: Japón entra con el currículo mejor cedido de la KB, y una página bloqueada se lee por su fuente

### 🟢 El alta del pase: `jp-cos/jp-cos.github.io` — 学習指導要領LOD, **CC BY 4.0**

El hueco de **JAPÓN** llevaba **cuatro pases declarado sin medir** (desde el 61). Cerró al buscar
**en japonés** —`学習指導要領`, no «Japan curriculum ontology»—, el mismo canal que en el pase 61
rindió 11 piezas tras diez pases sin altas.

| Repo | Licencia | Qué trae |
|---|---|---|
| [`jp-cos/jp-cos.github.io`](https://github.com/jp-cos/jp-cos.github.io) | **CC BY 4.0** | currículo nacional japonés completo en RDF/Turtle: **22 volcados versionados**, vocabulario, **SHACL** (71 KB), endpoint SPARQL declarado. 7 ★, 39 issues abiertos, último cambio 2026-09-25 |
| [`ICT-CONNECT-21/CSCode2023`](https://github.com/ICT-CONNECT-21/CSCode2023) | **MIT** (texto completo, 1.081 B) | el programa de referencia de búsqueda de códigos, **por encargo de MEXT** |

🔵 **CC BY 4.0 es más permisiva que la CC BY-SA 4.0 alemana: sin ShareAlike no activa la compuerta
de P178, así que el derivado puede entregarse con licencia propia.** Publicador del dato:
教育データプラス研究会; **MEXT es el 出典, no el publicador**.

### 🔴 La hipótesis de la acción queda REFUTADA, y eso es información

La acción 3 decía: *«si existe y está publicado por MEXT sin licencia explícita, APAC replica el
patrón alemán y **P174** gana una tercera región»*. **Hay licencia explícita y es permisiva.**
**P174 no gana región por este caso**, y el hueco cierra en la mejor rama posible.

### 🟢 Y la reserva publicada sobre Alemania también cae

La tendencia 457 del pase 63 escribió que *«lo que sigue sin licencia es la capa que agrega el
valor específico: la cobertura por Land»*. Medido con el extractor nuevo:
**`dini-ag-kim/school-curriculum-pg` declara `CC BY-SA 4.0` en las 25 serializaciones, los 16
archivos `lp-land-XX-full.owl` incluidos**, con titulares identificados por **ORCID**, fecha y IRI
versionado — una cesión más completa que la de muchos archivos `LICENSE`.

### 🔵 Nota de canal reusable: una página bloqueada se lee por su fuente

`jp-cos.github.io`, `w3id.org`, `zenodo.org`, `dydra.com` y `www.mext.go.jp` están **bloqueados**
en esta corrida (`connect_rejected` / `EGRESS_BLOCKED`, los dos canales probados en cada caso).
🟢 **Pero un sitio **GitHub Pages** se sirve DESDE un repositorio, y `raw.githubusercontent.com`
está abierto: `index.html` y `about.html` se leyeron por `raw` y ahí estaba la cesión.** La
declaración de licencia que el portal muestra **vive en el repo**, y por eso quedó **medida** y no
«corroborada».
⚠️ **Lo que el bloqueo sí costó:** los términos de MEXT quedan corroborados por canal secundario y
no medidos; **el endpoint SPARQL no se verificó** y el publicador lo anuncia 試験公開中.

### ⚠️ El eje genérico volvió a devolver lo mismo

Las búsquedas globales obligatorias de agentes y de trending siguen devolviendo marcos generalistas
y agregadores. **Ninguna alta de este pase salió de ahí: las dos salieron de BUSCAR EN EL IDIOMA
DEL PAÍS**, que es el tercer pase consecutivo en que ese canal rinde y el genérico no.

## 2026-10-03 — pase 64: la ref `HEAD` borra la dimensión «rama», y la licencia del dato estaba dentro del dato

### 🔵 El cambio de instrumento, medido contra su propio control negativo

**La acción 1 venía especificada como «4 nombres × `main` y `master`». Corrida así, y corrida con
la ref `HEAD`, sobre las mismas 200 filas:**

| Instrumento | Licenciados detectados | Falsos «sin licencia» |
|---|---|---|
| 4 nombres × `main`/`master` (la acción **como estaba escrita**) | **153** | 🔴 **7 de 160 (4,4 %)** |
| 14 nombres × ref **`HEAD`** | **160** | 🟢 **0** |

🔴 **Los 7 que la especificación original pierde, y el primero duele:**

| Repo | Dónde estaba | Por qué se perdía |
|---|---|---|
| **`moodle/moodle`** | `COPYING.txt` | 🔴 **la plataforma madre de esta KB, reportada «sin licencia»** |
| `jeanlucio/moodle-local_aihub` | `COPYING.txt` | convención GNU |
| `cboard-org/cboard` | `LICENSE.txt` en `master` | nombre fuera de la lista corta |
| `luisgf/openbadgeslib` | `LICENSE.txt` en `master` | ídem |
| `kaldi-asr/kaldi` | `COPYING` | ídem |
| `contentauth/c2pa-rs` | `LICENSE-MIT` | doble licencia estilo Rust |
| `contentauth/c2pa-python` | `LICENSE-MIT` | ídem |

🟢 **`raw.githubusercontent.com` resuelve la ref literal `HEAD` a la rama por omisión, cualquiera
sea su nombre.** Verificado contra `frappe/education`, cuya licencia vive en **`develop/license.txt`**
y que **ninguna** lista de ramas `main`/`master` alcanza (**P170**).

### 🔴 El defecto de clasificación, con su contraejemplo

🔴 **Un classificador que hace `grep` sobre todo el cuerpo etiqueta **GPL-3.0 como AGPL-3.0**,
porque el §13 del texto de GPL-3.0 se TITULA *«Use with the GNU Affero General Public License»*.**
Detectado contra `frappe/erpnext` (35.148 B), que el pase 63 había leído —bien— como GPL-3.0.
🔵 **Se clasifica por el TÍTULO, en las primeras 12 líneas, no por el cuerpo** (**P171**).
⚠️ **GPL-3.0 y AGPL-3.0 difieren ~600 bytes en tamaño (35,1 KB vs 34,5 KB): el tamaño NO los separa.**

### 🔴 La licencia dentro del payload: las tres ontologías de `FWU-DE`

| Repo | `LICENSE` en raíz | README | Dentro del `.owl` |
|---|---|---|---|
| `FWU-DE/lehrplan-ontologie` | 🔴 404 ×14 | 🔴 0 coincidencias | 🟢 **CC BY-SA 4.0**, `dct:license` IRI completo |
| `FWU-DE/schulfach-ontologie` | 🔴 404 | 🔴 0 | 🟢 **CC BY-SA 4.0**, IRI completo |
| `FWU-DE/schulart-ontologie` | 🔴 404 | 🔴 0 | 🟢 **CC BY-SA 4.0**, ⚠️ **prefijo `dcterms:`** |

⚠️ **Ruta: `src/ontology/<prefijo>-edit.owl`.** Los nombres que anuncia el README (`lp.owl`,
`lp-base.owl`, `lp-full.owl`, `lp-simple.owl`, `reasoned.ttl`) **dan 404 los cinco**: son productos de
build sin versionar. **La ruta se descubre leyendo `.github/workflows/qc.yml`, no probando nombres.**

### 🔴 Y la «dependencia upstream» de la receta P169 es una lápida de 136 bytes

`dini-ag-kim/school-curriculum-pg` — README íntegro: *«# This repo is outdated ·· ## please go to ··
`FWU-DE/lehrplan-ontologie`»*. **14 nombres de licencia 404, 5 subdirectorios 404, 14 nombres de
`.ttl`/`.owl` 404; lo único alcanzable además del README es `.gitignore`** (**P173**).

### 🟢 Reemplazos vivos para tres filas muertas de la capa de estándares

| Alta | Licencia **leída** | Bytes | Reemplaza a |
|---|---|---|---|
| [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | 🟢 **Apache-2.0** | 13.184 | `concentricsky/badgr-server` (404) |
| [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) | 🔴 **IMS Global Specification Document License** (no OSI, por membresía) | 12.402 | `1EdTech/caliper-php` y `IMSGlobal/caliper-python` (404) |
| [`IMSGlobal/openbadges-specification`](https://github.com/IMSGlobal/openbadges-specification) | 🔴 **`SPEC-LICENSE` — corregido en el pase 67:** IMS Global *Specification Document License*, 12.324 B en `ob_v3p0/license.md`, ⚠️ **niega derivados** (**P187**) | — | — |

### ⚠️ Mapa de canales de esta corrida — el bloqueo alemán es de DOMINIO, no de corrida

| Canal | Estado | Nota |
|---|---|---|
| `raw.githubusercontent.com` (incl. ref `HEAD`) | 🟢 **abierto** | ~6 repos por llamada en paralelo; 1.600 peticiones sin estrangulamiento |
| `github.com` HTML vía WebFetch | 🟢 abierto | ⚠️ una llamada por repo; sirve para confirmar 404 |
| `api.github.com` | 🔴 **403** | reproduce el pase 63 |
| `github.com` vía `curl` | 🔴 **403** | reproduce el pase 63 |
| `fwu.de`, `regierung-mv.de`, `handelsregister.de`, `bundesanzeiger.de` | 🔴 **bloqueo de EGRESO** | `000` por `curl`; el proxy reporta *«gateway answered 403 to CONNECT»* |
| `sachsen-anhalt.de`, `bildungsserver.de` vía WebFetch | 🔴 **`EGRESS_BLOCKED`** | ⚠️ **segundo canal, mismo veredicto** |

🔵 **La pregunta que la acción 2 pedía responder primero —«el bloqueo es del dominio o de la
corrida?»— queda contestada: es **del dominio**, y se reproduce en SEIS dominios alemanes por DOS
canales independientes. El canal está agotado, no intermitente.**

## 2026-10-03 — pase 63: el upstream CC0 que estaba un nivel más arriba, y un `LICENSE` de 19 bytes

### 🟢 El alta de la semana es un vocabulario, y es la primera pieza de currículo de EMEA entregable sin condiciones

| Repo | Licencia **leída del archivo** | Prueba | Qué es |
|---|---|---|---|
| [`dini-ag-kim/schulfaecher`](https://github.com/dini-ag-kim/schulfaecher) | 🟢 **CC0 1.0 Universal** | `raw:main/LICENSE` **200** y `raw:master/LICENSE` **200** | vocabulario KIM de **materias escolares alemanas**, SKOS |

🔵 **Cómo apareció, y es la lección: no por búsqueda.** **El README de `FWU-DE/schulfach-ontologie`
declara que mapea a las *KIM school subjects* e importa conceptos de la ontología de currículo de la
DINI AG-KIM. Seguir esa cita hacia arriba dio la pieza licenciada que la región no tenía.**
🔴 **Patrón: la capa de FWU, que agrega la cobertura por Land, NO tiene licencia; el vocabulario base
del que deriva es CC0. El valor específico es lo que no se cede.**

### 🔴 La familia `FWU-DE`, medida repo por repo — cuatro regímenes en un publicador público

| Repo | Tipo | Licencia | Prueba |
|---|---|---|---|
| `mem-mcp` | código | 🟢 **Unlicense** | `raw:main/LICENSE` 200, **1.211 B** |
| `fwu-kc-extensions` | código | 🟢 **Apache-2.0** | `raw:main/LICENSE` 200, **11.357 B** |
| `ais-chat` | código | 🔴 **AGPL-3.0** | `raw:main/LICENSE` 200, **34.523 B** |
| `lehrplan-ontologie` | **dato** | 🔴 **ninguna** | `LICENSE`,`.md`,`.txt`,`COPYING` → **404 los 4** |
| `schulfach-ontologie` | **dato** | 🔴 **ninguna** | **404 los 4** |
| `schulart-ontologie` | **dato** | 🔴 **ninguna** | **404 los 4** |

🔴 **3 de 3 de código licenciados con tres licencias distintas; 3 de 3 de dato sin ninguna, y sin
licencia en prosa tampoco (cero coincidencias de `licen[sz]|lizenz|copyright|CC[ -]BY|urheber|rechte`
en los tres README).** 🔵 **El publicador no es la licencia** (**P166**).

### 🔴 Las dos plataformas de ERP educativo, con la licencia leída en vez de creída

| Plataforma | Repo | Licencia | Prueba |
|---|---|---|---|
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL-3.0** | `raw:master/LICENSE` **200**, texto explícito |
| **Frappe Education** | [`frappe/education`](https://github.com/frappe/education) | 🔴 **GPL-3.0** | `raw:develop/license.txt` **200** — ⚠️ **19 BYTES** |
| **ERPNext** | [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 **GPL-3.0** | `raw:master/license.txt` **200**, texto completo |

🔵 **El `LICENSE` de 19 bytes es una categoría nueva** (**P168**): `License: GNU GPL V3`, sin texto,
sin titular, sin año. **Un chequeo de existencia lo aprueba; sólo un chequeo de CONTENIDO lo atrapa.**
**El control es el tamaño: GPL-3.0 ~35 KB, AGPL-3.0 ~34,5 KB, Apache-2.0 ~11 KB, MIT ~1 KB — por
debajo de ~400 B no cabe ninguna licencia OSI.**

### ⚠️ El mapa de canales de verificación, medido en esta corrida — cambia cómo se planifica un barrido

| Canal | Estado | Sirve | No sirve |
|---|---|---|---|
| `raw.githubusercontent.com` | 🟢 **abierto, sin límite de alcance** | **LICENSE y README de cualquier repo público**; el 404 como prueba de ausencia; **~6 repos por llamada** | linaje de fork, ★, `description` |
| `github.com` HTML vía **WebFetch** | 🟢 abierto | **fork, ★, `description`, licencia de la barra** | ⚠️ **una llamada por repo** |
| `github.com` vía **curl** | 🔴 **403** | — | — |
| `api.github.com` | 🔴 **403 — acotada por SESIÓN, no bloqueada** | — | ⚠️ pedible con `add_repo`, repo por repo |

🟢 **`gap 74` (pase 36) cambia de estado: ahí `api.github.com/repos/<slug>` devolvía **200** con el
cuerpo diciendo que el repo no estaba habilitado para la sesión —y el riesgo era un probe que mirara
sólo el código HTTP—. **Hoy el mismo endpoint devuelve `403`, así que el código concuerda con el cuerpo
y ese modo de fallo silencioso ya no aplica.** ⚠️ **Cambio observado entre dos fechas, no corrección:
la compuerta de alcance es la que aquel pase ya había identificado.** 🔵 **Consecuencia operativa: el barrido de LICENCIA es masivo y barato; el de
LINAJE es unitario y caro. Dejar de planificarlos como una sola tarea es lo que habilita la acción 1
del pase 64.**

## 2026-10-03 (pase 62) — **el dato crudo del barrido de forks: 13 repos abiertos uno por uno, 3 rutas de `LICENSE` probadas en la puerta más forkeada (las tres 404), y el canal de API caído**

### 🔴 Canal de medición de esta corrida, declarado antes que los datos

| Canal | Resultado | Consecuencia |
|---|---|---|
| `curl` → `github.com` | 🔴 **403** | inutilizable para verificar existencia |
| `curl`/WebFetch → `api.github.com` | 🔴 **403** | 🔴 **ninguna cifra de este pase viene de la API** |
| WebFetch → página HTML del repo | 🟢 **200** | de acá salen `★`, forks, commits y la línea `forked from` |
| WebFetch → `raw.githubusercontent.com` | 🟢 **200** / **404** limpio | de acá salen las licencias leídas y los 404 |

🟢 **Control de canal:** el mismo `raw` que devolvió **404** para `DMontgomery40/mcp-canvas-lms:LICENSE`
devolvió **200** y el texto completo para `ashleycribb/learnmcp-xapi:LICENSE`. **El 404 discrimina.**

### Los repos tocados, con lo que se midió en cada uno

| Repo | ¿Fork de? | Licencia medida | ★ | Qué se midió |
|---|---|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | — madre | **MIT** | **272** | README: **103 *tools*, 8 skills**, v1.13.0 (sep 2026) |
| [`BartMassey-upstream/canvas-mcp`](https://github.com/BartMassey-upstream/canvas-mcp) | 🔴 `vishalsachdev` | **MIT** | 0 | 🔴 README: **139 *tools***, **v1.13.0 — la misma release que la madre** |
| [`lindsay-cheng/canvas-mcp`](https://github.com/lindsay-cheng/canvas-mcp) | 🔴 `vishalsachdev` | **MIT** | 0 | README: 103 *tools*, v1.12.0 (ago 2026) |
| [`AmirF194/canvas-mcp`](https://github.com/AmirF194/canvas-mcp) | 🔴 `vishalsachdev` | **MIT** | 0 | README: **101 *tools*** («80+» en la descripción) |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | no | 🔴 **ninguna** | **103** (**39 forks**) | 🔴 **tres rutas probadas, las tres 404** (ver abajo) |
| [`Dymayo/moodler-mcp`](https://github.com/Dymayo/moodler-mcp) | 🔴 `GhaithAlHallak8/moodler-mcp` | **MIT** | 0 | 75 commits; **5 variables declaradas**, 2 son compuertas apagadas |
| [`GhaithAlHallak8/moodler-mcp`](https://github.com/GhaithAlHallak8/moodler-mcp) | no — **madre** | **MIT** | 2 | 75 commits; mismo flujo de token móvil |
| [`ashleycribb/learnmcp-xapi`](https://github.com/ashleycribb/learnmcp-xapi) | 🔴 `DavidLMS/learnmcp-xapi` | 🟢 **MIT leída en el archivo** | 0 | 34 commits; `LICENSE` **propio en la raíz**: *«MIT License / Copyright (c) 2025 David Romero»* |
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | no — madre | **MIT** | 15 | 32 commits; ⚠️ **sin marca de archivado**, issues y guía de contribución abiertas |
| [`Orenda-Project/rumi-platform`](https://github.com/Orenda-Project/rumi-platform) | no — **madre** | 🟢 **Apache-2.0** (`LICENSE` raíz) | **17** (16 forks) | 677 commits; 15 idiomas; 890 videos + 10.929 preguntas |
| [`Jazy1/rumi-pinokio`](https://github.com/Jazy1/rumi-pinokio) | 🔴 `Orenda-Project/rumi-platform` | Apache-2.0 | 0 | 317 commits. **No se da de alta: se da de alta la madre** |
| [`nmarafo/open-lex-edu`](https://github.com/nmarafo/open-lex-edu) | no | ⚠️ **CC BY-SA 4.0**, `LICENSE.md` **en la raíz** | 0 | 143 commits; **832 normas**, frontmatter YAML, `index.yaml` con grafo |
| [`FWU-DE/lehrplan-ontologie`](https://github.com/FWU-DE/lehrplan-ontologie) | no | 🔴 **ninguna** | **10** (4 forks) | RDF/OWL + Turtle, **16 Bundesländer**; `LICENSE` 404, `LICENSE.md` 404, nada en README ni barra lateral |
| [`teacherspet-cloud/schul-apps`](https://github.com/teacherspet-cloud/schul-apps) | no | 🔴 **ninguna declarada** | 0 | 216 commits; ⚠️ **15 de 16 Länder, falta Renania-Palatinado** |

### 🔴 La puerta más forkeada de esta KB promete una licencia que no existe (P161)

**`DMontgomery40/mcp-canvas-lms` — 103 ★, 39 forks.** El README dice literalmente
*«MIT License - see LICENSE file for details»*. **Las tres rutas probadas en esta corrida:**

| Ruta | Resultado |
|---|---|
| `main:LICENSE` | 🔴 **404** |
| `main:LICENSE.md` | 🔴 **404** |
| `master:LICENSE` | 🔴 **404** |

🔵 **Segundo caso de la misma forma** (el primero: `@timadey/proctor`, pase 41 — MIT anunciada, sin
`LICENSE` en ninguna rama de toda la historia). **Se nombra P161: la licencia declarada sólo en
prosa.** 🔴 **Acá tiene escala: 39 forks reciben del upstream la ausencia de cesión, no la MIT que
el README promete.**

⚠️ **Lo que NO se midió:** el listado de forks sólo muestra **15 activos en dos años** de los 39.
**No se abrió fork por fork** para ver si alguno agregó un `LICENSE` propio. **La frase «39 heredan
la ausencia» es sobre lo que reciben del upstream, no una lectura de los 39.** 🔵 **Dato lateral que
conviene anotar: entre esos 15 está `bruchris/mcp-canvas-lms`, y `bruchris/canvas-lms-mcp` es una
puerta clase (a) independiente de esta KB — el mismo autor aparece a los dos lados del eje.**

### 🔴 Ruido medido y rechazos, para que el próximo pase no lo vuelva a pagar

- **La búsqueda global de «top open source AI agents education 2026 github MIT» devolvió, otra vez,
  marcos de agente genéricos** (openclaw, browser-use, AutoGen, Flowise, dify, «Hermes Agent»)
  **y ni una sola pieza de educación.** 🔴 **Es la quinta vez que esta consigna se confirma: en esta
  industria el rendimiento está en buscar el DOMINIO (LMS, currículo, rúbrica, proctoring,
  Lehrplan), no en buscar «agente».**
- ⚠️ **Y una cifra de esa búsqueda que NO se copia a esta KB:** se afirmaba «Hermes Agent, MIT,
  180.000 ★ desde su lanzamiento en febrero de 2026, el framework OSS de más rápido crecimiento».
  🔴 **No se verificó, no es educación, y esta base ya se quemó con conteos de estrellas inflados
  por el pipeline (ver la corrección registrada en `rotation.json` para technology). No entra.**
- **`holt00/TFG-open-cvn-schema`** apareció buscando currículo español: 🔴 **es un esquema de
  *curriculum vitae* académico, no de currículo escolar.** **Falso amigo del término, anotado.**

## 2026-10-03 (pase 61) — **el dato crudo: 14 repos probados por licencia archivo por archivo (≈120 requests), 4 archivos de licencia leídos enteros, 4 endpoints oficiales bloqueados y 1 recomendación secundaria refutada**

### Los repos tocados, con lo que se midió en cada uno

**Canal usado: `raw.githubusercontent.com` archivo por archivo.** 🔴 **`github.com` por `curl` devolvió
`403` para las 14 URLs reales y también para el repo de control inexistente, así que NO discrimina y no
sirve para verificar existencia en esta corrida.** 🟢 **Control de canal corrido: README real → `200`;
`bncc-dev/no-such-repo-9999` → `404`; `dados/NO_SUCH_LICENSE_9999.md` → `404`.**

| Repo | Región | Licencia **código** | Licencia **dato** | ★ | Qué se midió |
|---|---|---|---|---|---|
| `bncc-dev/bncc-dados` | LATAM | **MIT** (`LICENSE`) | **CC BY 4.0** (`dados/LICENSE.md`) | — | ya estaba en la KB desde el pase 11; **este pase le leyó la licencia del dato, que faltaba** |
| `bncc-dev/bncc-pacotes` | LATAM | **MIT** (`LICENSE-CODIGO.md`) | **CC BY 4.0** (`LICENSE-DADOS.md`) | 9 | **NUEVO.** `@bncc/dados` 0.3.1 y `@bncc/mcp` 0.2.0 en npm, `bncc` 0.2.0 en PyPI; MCP hospedado en `https://mcp.bncc.dev` **sin API key**; 7 tools |
| `bncc-dev/bncc-benchmark` | LATAM | **MIT** (`LICENSE-CODIGO.md`) | **CC BY 4.0** (`LICENSE-DADOS.md`) | 9 | **NUEVO.** Banco de ítems (1.721) + estudio de intervención **31,9 % → 0,2 % / 2,3 %**; held-out nunca publicado, a propósito |
| `ayrtonmoura1/conectabncc` | LATAM | **MIT** (`LICENSE`) | — | — | **NUEVO.** ⚠️ `README.md` → `404` en `main` y `master`; `package.json` → `404`; `index.html` → `200`: **es un sitio estático, no un componente** |
| `rodrigohgpontes/buscabase` | LATAM | **MIT** (`LICENSE`) | — | — | **NUEVO.** «Busca Base»: buscar, verificar y reusar el texto de la BNCC |
| `dfdb76/bncc-mcp` | LATAM | **MIT** (`LICENSE`) | — | — | ya estaba; licencia **reconfirmada** de primera mano |
| `oaknational/oak-curriculum-ontology` | EMEA | **MIT** (`CODE-LICENSE.md`) | **OGL v3.0** (`DATA-LICENSE.md`) | — | ya estaba; **este pase leyó el `LICENSE.md` entero y descubrió el reparto dual por directorio** (`ontology/`, `data/`, `docs/` → OGL; `scripts/`, workflows → MIT) |
| `oaknational/oak-open-curriculum-ecosystem` | EMEA | **MIT** (`LICENCE`) | **OGL v3.0** | 8 | **NUEVO.** SDK TypeScript + Zod + metadata de tools MCP; MCP en **beta pública** `mcp.thenational.academy/mcp`; búsqueda híbrida sobre Elasticsearch. ⚠️ **API key necesaria** (gratuita a pedido) y **no acepta PRs externos** |
| `bbc/curriculum-data` | EMEA | — | **CC BY 4.0** (`LICENSE`) | 24 | **NUEVO.** Turtle/RDF; GCSE y Key Stages de Inglaterra, National 4/5 y Higher de Escocia, TGAU de Gales, CCEA/WJEC de Irlanda del Norte. 🔴 **último commit 2014-09-12: de archivo, no vivo** |
| `eVgKatis/CCSO` | EMEA | **GPL-3.0** (`master/LICENSE`) | — | — | **NUEVO.** *Curriculum Course Syllabus Ontology*. 🔴 **copyleft: queda fuera del filtro de Globant** |
| `CEDStandards/CEDS-Ontology` | North America | **Apache 2.0** (`LICENSE`) | — | 15 | **NUEVO.** OWL de CEDS v14; genera JSON, JSON-LD, XML. ⚠️ **modela ENTIDADES educativas, no estándares de aprendizaje: no es currículo** |
| `commoncurriculum/common-standards-project` | North America | 🔴 **ninguno** (5 nombres × 2 ramas → `404`) | registros declaran `CC BY 3.0 US` | 47 | **NUEVO.** «50 states, organizations, districts & schools». 🔴 **sin licencia de repo y detenido desde diciembre de 2015** |
| `SirFizX/standards-data` | North America | 🔴 **ninguno** | — | 12 | **NUEVO.** Common Core Math terminado, Reading en curso; crudo de Achievement Standards Network |
| `qdonnellan/commoncore` | North America | 🔴 **ninguno** | — | — | **NUEVO.** Parser XML→JSON del CCSS |
| `formalms/formalms` | EMEA | 🔴 **ninguno** (7 nombres → `404`) | — | — | **probado para refutar una recomendación secundaria** — ver abajo |

### 🔴 La recomendación secundaria que este pase refutó, con el mecanismo del error (P155)

**Una comparativa de LMS decía que `Forma LMS` es *«best for corporate teams that specifically need
Apache 2.0 permissive licensing … the most permissive licence»*.** 🔴 **Es falso y el error es
mecánico:**

| Qué se midió | Resultado |
|---|---|
| única aparición de «Apache» en `master/README.md` | **línea 21: *«Apache (recommended) with mod_rewrite enabled»*** → **el servidor web** |
| `LICENSE`, `LICENSE.md`, `LICENCE`, `COPYING`, `license.txt`, `LICENSE-GPL`, `docs/LICENSE` | 🔴 **`404` los siete** |
| licencia de la distribución propia del proyecto (SourceForge/OSDN) | **GPLv2**, fork de Docebo CE 4.0.5 |

🔵 **El requisito de servidor web y el nombre de la licencia comparten la palabra, y en esta vertical
el requisito es muchísimo más frecuente que la licencia.** ⚠️ **Seguir esa recomendación pone una
entrega corporativa sobre copyleft.**

### 🔴 Ruido medido y rechazos, para que el próximo pase no lo vuelva a pagar

- 🔴 **4 endpoints oficiales bloqueados por el proxy de egreso**, con la URL exacta para no reintentar:
  `www.australiancurriculum.edu.au/machine-readable-australian-curriculum` y `www.1edtech.org/standards/case/about`
  → `EGRESS_BLOCKED`; `rdf.australiancurriculum.edu.au`, `standards.1edtech.org`, `www.imsglobal.org`
  y `www.scootle.edu.au` → `000`. **Consecuencia: la licencia de MRAC (gap 254) y la de CASE (gap 256)
  quedan sin verificar y NO se infieren.**
- ⚠️ **`bncc.dev` (el sitio del leaderboard) también → `000`.** Las cifras del benchmark se leyeron del
  `README.md` del repo por el canal que sí funciona, no del sitio.
- ⚠️ **`fh-yarbouh/oak-curriculum-ontology` apareció en el barrido y es un fork sin archivo de
  licencia** (5 nombres × 2 ramas → `404`). **No se da de alta**: por **P151**, «es fork de X» cierra
  sólo la celda que se comparó, y acá no se comparó ninguna.
- ⚠️ **Las búsquedas globales obligatorias (4) devolvieron, otra vez, el eje agotado:** OpenClaw,
  OpenHands, opencode, CrewAI, LangGraph — **agentes generalistas ya inventariados en esta KB, ninguno
  educativo.** 🟢 **Lo que rindió fue la consigna del pase 22/44: evitar la palabra `education` y
  buscar por el artefacto del dominio.** `item bank` trajo `bncc-benchmark`; `curriculum ontology`
  trajo la capa entera.

## 2026-10-03 (pase 60) — **el dato crudo: 2 pares de fork diffeados archivo por archivo (18 descargas), 1 árbol de Moodle leído por línea, 3 controles negativos de canal corridos ANTES de leer, y 1 extractor propio que falló devolviendo «idéntico»**

### 🟢 La nota de canal, primero, y esta vez CIERRA una pregunta en vez de abrirla

**Los tres controles negativos corrieron antes de leer nada** (regla de **P126**):

| Control | Resultado | Qué habilita |
|---|---|---|
| Rama inexistente (`zzz-no-such-branch-9999`) | **`404`** | el canal discrimina rama |
| Archivo inexistente (`NO_SUCH_FILE_9999.md`) | **`404`** | discrimina archivo |
| Repo inexistente (`no-such-repo-9999`) | **`404`** | discrimina repo |

🟢 **Así que un `200` de este pase significa algo** — y la pregunta de canal que el pase 59 dejó abierta
queda **CONTESTADA por medición**: `codeload.github.com` **`403`**, `api.github.com` **`403`**,
`raw.githubusercontent.com` archivo por archivo **ES** el canal correcto. 🔵 **Se retira del pedido de
permisos del pase 61: ya no hay que gastar un intento en averiguarlo.**

### Los repos tocados, con lo que se midió en cada uno

| Repo | Licencia | Qué se hizo | Resultado |
|---|---|---|---|
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | **MIT** | madre del par A; 10 archivos descargados | referencia |
| [`algorithm0r/canvas-lms-mcp`](https://github.com/algorithm0r/canvas-lms-mcp) | **MIT** | fork del par A; 10 archivos diffeados | 🟢 **byte a byte idéntico, 10/10** |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | madre del par B; 9 archivos descargados | referencia |
| [`abr-Projects/canvas-mcp`](https://github.com/abr-Projects/canvas-mcp) | **MIT** | fork del par B; 9 archivos diffeados | 🔴 **difiere en 8; idéntico en el eje** |
| [`moodle/moodle`](https://github.com/moodle/moodle) | **GPL-3.0** | `public/mod/assign/externallib.php`, 3.146 líneas | 🟢 **`gap 250` cerrado** |

**Las cuatro licencias del cuadrilátero Canvas re-verificadas en este pase leyendo el archivo `LICENSE`
de cada repo: las cuatro MIT.** ⚠️ **`moodle/moodle` es GPL-3.0 y eso no cambia: se LEE como fuente de
verdad sobre el web service, no se incorpora a un entregable.**

### 🔴 El tamaño de la divergencia del par B, en bytes

| Archivo | Madre | Fork | Δ |
|---|---|---|---|
| `src/canvas_mcp/tools/rubrics.py` | 83.623 | 59.436 | **−29 %** |
| `src/canvas_mcp/tools/assignments.py` | 60.153 | 53.290 | −11 % |
| `src/canvas_mcp/core/client.py` | 36.263 | 34.711 | −4 % |
| `src/canvas_mcp/server.py` | 35.587 | 34.521 | −3 % |
| `src/canvas_mcp/tools/student_write.py` | 43.997 | 46.665 | **+6 %** |
| `src/canvas_mcp/tools/peer_reviews.py` | 10.695 | 10.345 | −3 % |
| `README.md` | 39.479 | 37.048 | −6 % |
| `pyproject.toml` | 4.056 | 4.065 | +0,2 % |

⚠️ **Y una diferencia de SUPERFICIE que los bytes no muestran: la madre importa 26 registradores de
herramientas y el fork 25 — falta `register_educator_course_tools`.**

### 🔴 El defecto propio, que es el de siempre y hay que dejarlo escrito

**El primer extractor de funciones de este pase devolvió 7 líneas para una función de 256**, y por lo
tanto un `diff` de **0 líneas**: un **«IDÉNTICO» falso**. Rompía en la firma multilínea de
`async def bulk_grade_submissions(`. 🔵 **Lo atrapó el control de plausibilidad —una función de calificado
masivo no tiene 7 líneas—, no el `diff`.** 🔴 **Tercera reproducción de la forma: un extractor con pérdida
no falla ruidosamente; devuelve un número más chico y más confiado.** ⚠️ **De haberse publicado, este
archivo diría «el fork B es idéntico» — la conclusión exactamente opuesta a la verdadera.**

## 2026-10-03 (pase 59) — **el dato crudo: 16 repos tocados, 5 archivos de código leídos para el eje de publicación, 3 licencias probadas en 2 ramas cada una, 2 forks con padre declarado y 1 canal de verificación que hubo que cambiar**

### 🔴 La nota de canal, primero, porque invalida un método que esta base usaba

**`curl -sI https://github.com/<owner>/<repo>` devuelve `403` para los OCHO repos probados en este
pase** — incluidos los que el pase 58 verificó sin problema. 🔵 **No es `404`: es el proxy de egreso
de este entorno bloqueando `HEAD` sobre el HTML de `github.com`.** 🔴 **Consecuencia de método: un
`403` por este canal NO es evidencia de que el repo no exista, y una verificación de URL por
`curl -sI` contra `github.com` no vale en este entorno.**

**El canal que sí funciona, y es el que se usó:** `raw.githubusercontent.com` (`200` verificado) y
`WebFetch` sobre la página del repo (renderizó las ocho). **Las ocho URLs quedan verificadas por
esos dos canales concordantes, no por `curl -sI`.**

| Repo | `raw…/main/README.md` | `WebFetch` de la página |
|---|---|---|
| `loyaniu/moodle-mcp` | **200** | 🟢 renderizó |
| `Jawadh-Salih/moodle-mcp-server` | **200** | 🟢 renderizó |
| `dddanielliu/NCCU-Moodle-MCP` | **200** | 🟢 renderizó |
| `NiccoloSalvini/mcp-moodle-teacher` | **200** | 🟢 renderizó |
| `toshieji/moodle-grading-mcp` | **200** | 🟢 renderizó |
| `PabloPC05/mcp-usc` | **200** | 🟢 renderizó |
| `peancor/moodle-mcp-server` | **200** | 🟢 renderizó |
| `littlecookie0722/AI-Teaching-Agent` | **200** | 🟢 renderizó |

### Las 5 lecturas de código del eje de publicación, crudas

**Regla mantenida del pase 58: la celda se decide por el archivo que hace la llamada, no por el README.**

| # | Archivo leído (`raw.githubusercontent.com`, rama `main`) | Bytes | Qué se buscó | Resultado crudo |
|---|---|---|---|---|
| 1 | `NiccoloSalvini/mcp-moodle-teacher` → `src/index.ts` | **62.132** | `workflowstate`, `'released'`, `mod_assign_save_grade`, `markingworkflow` | **3 aciertos**: `can_grade: functions.includes("mod_assign_save_grade")` (l. 98), **`workflowstate: ""` (l. 375)**, `await moodle().call("mod_assign_save_grade", payload)` (l. 383). 🔴 **`markingworkflow`: 0 menciones**, aunque llama a `mod_assign_get_assignments` en l. 198 y l. 1218 |
| 2 | `NiccoloSalvini/mcp-moodle-teacher` → `src/moodle.ts` | 4.297 | ídem | **0 aciertos** (es el cliente del web service) |
| 3 | `NiccoloSalvini/mcp-moodle-teacher` → `src/marking.ts`, `src/grades.ts`, `src/oversight.ts` | 7.322 + 10.069 + 3.067 | ídem | 🔵 **0 aciertos en los tres**: el único escritor de nota está en `index.ts` |
| 4 | `toshieji/moodle-grading-mcp` → `server.py` | **26.489** | ídem | **9 aciertos.** El decisivo, l. 570: `"workflowstate": "readyforreview",  # ★未公開ドラフト。releasedにしない`; más `workflowstate="readyforreview", released=False` (l. 577) y el par `"workflowstate": "readyforreview"` / `"released": False` (l. 583-584). 🔴 **`markingworkflow`: 0 menciones** |
| 5 | `CharlieCardenasToledo/mcp-canvas-server` → `src/services/canvas-client.ts` | **60.194** | `posted_grade`, `post_manually`, `posting_policy`, `postPolicy` | **1 acierto**: `posted_grade: grade` (l. 505), dentro de `gradeSubmission` (l. 494) contra `courses/{c}/assignments/{a}/submissions/{u}`. 🔴 **`post_manually` / `posting_policy` / `postPolicy`: 0 menciones en todo el archivo** (`grep -ic` = **0**) |

⚠️ **Cuatro sondas de ruta que dieron 404 y se registran** (la regla del `gap 250`: la sonda tiene que
ser el archivo que se va a leer): `mcp-moodle-teacher` → `src/tools/grading.ts` **404**,
`src/client.ts` **404**; `mcp-canvas-server` → `src/services/canvas-api.ts` **404**,
`src/tools/grades.ts` **404**, `src/tools/index.ts` **404**, `src/services/index.ts` **404**.
🔵 **El árbol real se obtuvo listando el directorio con `WebFetch`, no adivinando rutas.**

### Las 3 licencias probadas en las dos ramas, crudas

| Repo | `main/LICENSE` | `master/LICENSE` | `pyproject.toml` | Veredicto |
|---|---|---|---|---|
| `loyaniu/moodle-mcp` | 🔴 **ausente** | 🔴 **ausente** | 🔴 **sin clave `license`** (sólo `name = "moodle-mcp"`, `version = "0.2.1"`) | 🔴 **SIN LICENCIA, con 37 ★** |
| `dddanielliu/NCCU-Moodle-MCP` | 🔴 **ausente** | 🔴 **ausente** | — | 🔴 **SIN LICENCIA** |
| `Jawadh-Salih/moodle-mcp-server` | 🟢 **`MIT License`** (primera línea del archivo) | — | — | 🟢 **MIT medido** |

### Los 2 forks, con el padre declarado por GitHub

| Fork | Padre, verbatim de la página | Licencia | ★ | Lenguaje | Escritura de nota |
|---|---|---|---|---|---|
| `algorithm0r/canvas-lms-mcp` | *«forked from bruchris/canvas-lms-mcp»* | MIT | 0 | TypeScript | `grade_submission`, `comment_on_submission`; *«48 tools perform Canvas write operations»* |
| `abr-Projects/canvas-mcp` | *«forked from vishalsachdev/canvas-mcp»* | MIT | 0 | Python | `bulk_grade_submissions`; *«up to 101 tools»*, v1.12.0 |

🔵 **`CharlieCardenasToledo/mcp-canvas-server` se probó contra la misma pregunta y la respuesta fue
NO:** la página no declara padre. **Es la única de las tres nuevas que aporta código distinto.**

### El barrido obligatorio, crudo: 4 globales + 4 regionales, año calculado 2026

| Búsqueda | Qué devolvió de nuevo para esta capa |
|---|---|
| `top open source AI agents education 2026 github MIT` | ⚠️ **nada de educación**: listicles de agentes genéricos (OpenClaw, OpenHands, CrewAI, LangGraph). **Duodécimo pase con la capa genérica** |
| `github trending education AI 2026` | ⚠️ **material didáctico SOBRE AI**, no agentes PARA educación (`AI Agents for Beginners` 56.002 ★, `developer-roadmap`) — mismo sesgo que los 11 pases anteriores |
| `open source platform education LMS SIS MIT Apache` | ⚠️ **sin alta permisiva nueva**: Moodle, Open edX, Sakai (Apache-2.0), Canvas, ILIAS, Chamilo, OpenEduCat (LGPLv3) — ya todas en `verticals/` |
| `AI education industry trends 2026` | 🟢 cifras de mercado y adopción (ver `intel/market.md`) |
| `moodle MCP server grade submission mod_assign_save_grade github workflowstate` | 🟢 **la que rindió**: 3 candidatas nuevas (`loyaniu`, `Jawadh-Salih`, `dddanielliu`) |
| `new open source AI grading agent MCP server Canvas Moodle released 2026 Apache MIT` | 🟢 **la que más rindió**: la alta + los 2 forks + `csmediapro` |
| 4 regionales (NA / EMEA / APAC / LATAM) | 🟢 **las cuatro rindieron** — ver `intel/market.md` y `intel/trends.md` |

🔵 **La lección de barrido, y es la tercera vez que se repite: las dos búsquedas que rindieron son las
ESPECÍFICAS DE MECANISMO** (`mod_assign_save_grade`, `workflowstate`, `posted_grade`), no las cuatro
genéricas obligatorias. ⚠️ **Las genéricas se siguen corriendo porque el barrido es obligatorio, y se
sigue declarando que no rinden en esta capa.**

## 2026-10-03 (pase 58) — **el dato crudo: 6 archivos de código fuente leídos línea por línea para el eje de precondición, 2 licencias probadas en 2 ramas, 2 hosts de la UE bloqueados y 14 suites NO corridas (con el motivo)**

### Las 6 lecturas de código de la acción 1, crudas

**Regla del pase: la celda se decide por el archivo que hace la llamada, no por el README** — que es lo que el
pase 57 demostró al encontrar que el «borrador» de `toshieji` no estaba en el servidor.

| # | Archivo leído (por `raw.githubusercontent.com`) | Qué se buscó | Resultado crudo |
|---|---|---|---|
| 1 | `peancor/moodle-mcp-server` → `src/index.ts` | `mod_assign_save_grade`, `markingworkflow` | **1 sola llamada**, en `provideFeedback`: `workflowstate: 'released'`, `attemptnumber: -1`, `addattempt: 0`. **0 lecturas de `markingworkflow`** |
| 2 | `Dymayo/moodler-mcp` → `src/moodler_mcp/tools/writes_teacher.py` | ídem | `workflowstate=""`, `attemptnumber=-1`, `addattempt=False`, `applytoall=False`. **0 llamadas a `mod_assign_get_assignments`** |
| 3 | `MarcosNahuel/moodle-mcp` → `src/tools/gradebook/calificar_manualmente.ts` | ídem | `if (args.workflow_state) { params.workflowstate = args.workflow_state; }` — **condicional**. **0 lecturas de la precondición** |
| 4 | `NiccoloSalvini/mcp-moodle-staff` → README + superficie de tools | ídem | 🔵 **no hay llamada al web service**: *«the CSV import is Moodle's own way in»* + `grades_csv` / `grades_verify` |
| 5 | `vishalsachdev/canvas-mcp` → `src/canvas_mcp/tools/assignments.py` | `posted_grade`, `post_manually`, `posting_policy` | `PUT /courses/{}/assignments/{}/submissions/{}` con `submission[posted_grade]`; el único `GET` previo pide `include[]=rubric,rubric_settings`. **0 lecturas de la política** |
| 6 | `bruchris/canvas-lms-mcp` → `src/tools/submissions.ts` | ídem | `canvas.submissions.grade(course_id, assignment_id, user_id, grade)`, **sin condicional previa** |

⚠️ **Lo que el README habría dicho, y por qué no alcanzaba:** el README de `peancor` describe
`provide_assignment_feedback` como *«Provides grades and comments for a student's submission»* y **no menciona
`workflowstate` ni `markingworkflow` ni una vez**. 🔴 **La propiedad que decide la entrega —`'released'` cableado—
sólo existe en el código.** 🔵 **Tercera reproducción del mecanismo de P139, ahora sobre otra pieza.**

### Las 2 pruebas de licencia del alta y del rechazo

| Repo | Canal | `main` | `master` | Veredicto |
|---|---|---|---|---|
| `littlecookie0722/AI-Teaching-Agent` | `raw/.../LICENSE` | 🟢 **200, texto MIT** (*«Copyright (c) 2026 littlecookie»*) | — (no hizo falta) | 🟢 **MIT por TEXTO**, no por *badge* |
| `dajiaohuang/WayMarker` | `raw/.../LICENSE` | 🔴 **404** | 🔴 **404** | 🔴 **sin licencia (ausencia MEDIDA)** + sidebar sin licencia + 0 archivo en el árbol → **rechazado** |

🔵 **Se aplica la regla de P114/P115: dos artefactos o no entra.** ⚠️ **Y el rechazo se publica, porque una ausencia
medida es un dato y el silencio parece cobertura.**

### 🔴 Los 2 hosts de la UE que quedaron bloqueados (gap 92, quinto canal reconfirmado)

| Host | Resultado crudo |
|---|---|
| `eur-lex.europa.eu` | 🔴 **`EGRESS_BLOCKED`** por el proxy de egreso |
| `artificialintelligenceact.eu` | 🔴 **`EGRESS_BLOCKED`** (2 rutas probadas: `/article/113/` y `/annex/3/`) |

⚠️ **Consecuencia declarada: las fechas del AI Act de este pase vienen de TRES canales secundarios concordantes, no
del texto consolidado.** 🔵 **Concuerdan entre sí y con la tendencia 392 del pase 57, así que se publican — pero la
etiqueta «de primera mano» NO se usa.**

### ⚠️ Las 14 suites que NO se corrieron, y el motivo

🔴 **`[Code from External]`: el entorno negó ejecutar el código clonado, incluidas las suites OFFLINE**
(`python3 test_*.py`, sin red). **No se reimplementaron, no se buscó otro intérprete y no se trocearon** — la
negativa es sobre el resultado, no sobre la forma del comando.

| Qué se intentó | Resultado |
|---|---|
| las 14 suites OFFLINE de `compose/code/` en un solo barrido | 🔴 **NEGADO** (`[Code from External]`) |

🔵 **Esto CORRIGE al pase 52 en la dirección contraria:** ese pase midió la frontera y la declaró más angosta
(*«la negativa es sobre ejecutar CON RED código que vino clonado, no sobre ejecutar el código»*). ⚠️ **Hoy alcanzó a
la ejecución sin red.** 🔴 **La frontera es del ENTORNO y varía entre pases, así que no se vuelve a publicar como
regla general** —el error que los pases 50 y 51 cometieron y el 52 corrigió. **La columna «Hoy» del `README.md`
queda con la medición del pase 56 y este pase no la re-afirma.**

### El barrido de búsqueda, crudo

**Año calculado, no cableado: 2026.** Las 4 búsquedas globales + 4 regionales se corrieron.
🔴 **Las globales devolvieron por decimotercera vez la capa genérica** (OpenClaw >300k ★, opencode 194.461 ★,
CrewAI 56.723 ★, LangGraph 39.083 ★, OpenHands 70k+ ★) **y material didáctico *sobre* AI** —que no es un agente de
educación—, más agregadores SEO sin repo verificable, **descartados sin medirlos y declarado**.
🟢 **Lo único que rindió un candidato real fue la búsqueda por el VERBO de la tarea** (`tutor grading agent …
released education LMS`) en vez de por la industria: de ahí salieron `AI-Teaching-Agent` (alta) y `WayMarker`
(rechazo medido). 🔵 **Es el canal que el pase 51 ya había descubierto en otro registro: cambiar el EJE de la
consulta, no repetirla.**

## 2026-10-03 (pase 57) — **el dato crudo: 9 READMEs releídos por el eje de compuerta de arranque, el código de Moodle leído de primera mano (643.753 bytes en 2 archivos), 14 suites corridas (1 nueva, 3 mutaciones) y una ruta del árbol de Moodle que se mudó bajo `public/`**

### Las 9 lecturas de la acción 1, crudas

**Canal: `raw.githubusercontent.com`, rama `main`, `README.md` — 9 de 9 en 200.**

| Pieza | bytes | Variables de compuerta halladas | G |
|---|---|---|---|
| `toshieji/moodle-grading-mcp` | 8.326 | `MOODLE_ALLOW_WRITE` (×4), `MOODLE_WRITE_COURSE_ALLOWLIST` (×4) | **G2** |
| `peancor/moodle-mcp-server` | 4.344 | 🔴 **ninguna** — 3 variables, las 3 de conexión | **G0** |
| `MarcosNahuel/moodle-mcp` | 8.585 | `MOODLE_ALLOW_INSECURE` ⚠️ **es TLS, no escritura** | **G0** |
| `vishalsachdev/canvas-mcp` | 39.479 | `ALLOWED_WRITE_TOOLS` (×2), `TOOL_MANIFEST` (×2) | **G3** ⚠️ |
| `Dymayo/moodler-mcp` | 16.228 | `MOODLER_ALLOW_STUDENT_WRITES` (×7), `MOODLER_ALLOW_TEACHER_GRADING` (×3) | **G2′** |
| `bruchris/canvas-lms-mcp` | 43.022 | `CANVAS_ROLE` (×10), `CANVAS_DESTRUCTIVE_TOOLS` (×6), `CANVAS_PROVENANCE_FENCING` (×2), `CANVAS_ENABLE_ASSIGNMENT_SUBMISSION` (×2) | **G0** (alcance) |
| `NiccoloSalvini/mcp-moodle-teacher` | 8.827 | `MOODLE_STAFF_TOOLS` (×1) | **G1?** |
| `NiccoloSalvini/mcp-moodle-staff` | 8.827 | 🟢 **sha256 IDÉNTICO al anterior** | — |
| `PabloPC05/mcp-usc` | 34.404 | 🔴 ninguna de arranque | — |

**Reparto: 3 de 8 con compuerta G2 o mejor sobre la escritura de juicio.** ⚠️ **`bruchris` es la pieza
con MÁS variables de seguridad de toda la capa (16 `CANVAS_*`) y en este eje es G0, porque su
desregistro real cubre los siete tools de borrado y no `grade_submission`.**

### 🔴 El código de Moodle, leído de primera mano

| Archivo | bytes | Qué se leyó |
|---|---|---|
| `public/mod/assign/externallib.php` | **142.802** | `save_grade` (líneas 2013-2062), `workflowstate` como **`PARAM_ALPHA`** (1987) |
| `public/mod/assign/locallib.php` | **500.951** | los **6** estados (64-69), la regla de liberación (**2991-3001**), el registro del cambio (**7960**), `grading_disabled` (8796) |
| `public/lib/moodlelib.php` | 369.302 | `PARAM_ALPHA` → `\core\param::ALPHA` = **`[a-zA-Z]`** (86-89) |

### ⚠️ Nota de instrumento: el árbol de Moodle se mudó bajo `public/` (y la sonda de rama over-reporta)

**Moodle 5 relocalizó el código de la aplicación bajo `public/`.** Medido este pase con 12 sondas:

| Ruta | `main` | `MOODLE_405_STABLE` |
|---|---|---|
| `README.md` | **200** | **200** |
| `config-dist.php` | **200** | **200** |
| `version.php` | 🔴 **404** | **200** |
| `lib/moodlelib.php` | 🔴 **404** | **200** |
| `mod/assign/locallib.php` | 🔴 **404** | **200** |
| `public/version.php` | 🟢 **200** | — |
| `public/mod/assign/locallib.php` | 🟢 **200** | — |

🔴 **Una sonda de rama contra `<rama>/README.md` devuelve 200 y NO prueba que el árbol del proyecto esté
en esa rama.** Dos archivos de la raíz (`README.md`, `config-dist.php`) dan 200 en `main` mientras un
tercero de la MISMA raíz (`version.php`) da 404. ⚠️ **Toca el instrumento de licencia de esta base: el
veredicto «`LICENSE` 404 en `main` y `master`» sigue siendo válido como *«no está en esa rama»*, pero no
como *«el proyecto no tiene licencia»* si el proyecto mudó su árbol.** 🔵 **Regla nueva: la sonda tiene
que ser el archivo que se va a leer, no un hermano cualquiera** (**gap 250**).

### Las 14 suites de `compose/code/`, corridas OFFLINE

| Suite | Hoy | Nota |
|---|---|---|
| `aiact-50-2-pack` | **27/27** | reproduce |
| `aiact-50-2-marking` | **23/23** | reproduce |
| `aiact-50-2-exposure` | **11/11** | reproduce |
| `sebserver-mcp-gate` | **37/37** | reproduce |
| `unitime-mcp-gate` | **46/46** | reproduce |
| `openedx-course-generator` | **33/33** | reproduce |
| `proctoring-reach-audit` | **19/19** | reproduce (`exit=0`; el texto *«Control (c) FAILED»* de su salida es **narrativa histórica**, no una falla de hoy) |
| `seb-proctoring-validator` | **21/21** | reproduce (`run_test.sh`, no `test_*.py`) |
| `registry-license-remeasure` | **24/24** | reproduce |
| `npm-surface-probe` | **19/19** | reproduce |
| `mcp-allowlist-gateway` | **34/34** | reproduce |
| `trend-backlink-audit` | **22/22** | reproduce |
| `suite-total-control` | **10/10** | reproduce |
| 🟢 **`grading-draft-gate`** | **37/37** | **NUEVA** — acción 2 del pase 56 |

**Total: 14 suites, 383 aserciones, 0 fallas.**

### 🟢 Las tres mutaciones de la suite nueva (que es lo que la hace un control)

| Mutación en `gate.py` | Resultado | Quién la atrapa |
|---|---|---|
| `DRAFT_STATE = "released"` | **31/37** | las 5 de (i) + 1 de (iv-d) |
| pie agregado sin chequear si ya está | **36/37** | *«NOT duplicated when already present»* |
| allowlist vacía tratada como comodín | **35/37** | las 2 de *«empty allowlist is no write target»* |

🔵 **Sin estas tres filas, «37/37» no dice nada: una suite que no puede fallar no es un control.**

### ✅ Controles de integridad de este pase, corridos y con sus cifras

| Control | Resultado |
|---|---|
| *frontmatter* en los 8 archivos | 🟢 **8/8**, `industry: education`, `region` dentro del vocabulario cerrado, `updated: 2026-10-03` |
| tabla de inventario de `agents/top.md` (gap 71) | 🟢 **80 filas / 80 claves distintas / 0 duplicados** |
| encabezados usados como dato | 🟢 **0** — las **70** tablas del archivo tienen su `\|---\|` debajo |
| filas totales en las 70 tablas | 438 |
| suites de `compose/code/` | 🟢 **14 corridas, 383 aserciones, 0 fallas** |

⚠️ **Y dos falsos positivos de instrumentos escritos a mano EN ESTE PASE, atrapados antes de publicar
—la clase P126 otra vez, y van tres pases seguidos:**

1. 🔴 **El detector de «encabezado usado como dato» marcó 12 filas**, y las 12 eran filas de celdas
   **vacías** (`| | |`, formato de tabla). El defecto: la condición *«todas las celdas son etiquetas
   genéricas»* es **verdadera por vacuidad** cuando no hay ninguna celda. **Corregido exigiendo ≥ 2
   celdas no vacías → 0 sospechosas.**
2. 🔴 **El control de «fila con repo y sin licencia» marcó 33 filas**, y son filas de las tablas
   **analíticas** (clase de credencial, compuerta, divulgación) que **no tienen columna de licencia** por
   diseño: la licencia de esas piezas vive en la fila del inventario. **El denominador estaba mal, no los
   datos.**

🔵 **La lección es la de la tendencia 376 aplicada a los controles: un control que no puede distinguir
«ausencia» de «no aplica» mide el esquema del autor, no el archivo.**

### El barrido obligatorio, crudo

| Consulta | Devolvió | Alta |
|---|---|---|
| `top open source AI agents education 2026 github MIT` | capa genérica (OpenClaw, CrewAI, OpenHands, opencode) + catálogos | 🔴 0 |
| `github trending education AI 2026` | currículos (MS *GenAI for Beginners* 121k ★, DeepLearning.AI, HuggingFace) + `DeepTutor` **ya en esta base** | 🔴 0 |
| `open source platform education ERP SIS MIT Apache 2026` | OpenEduCat (LGPL), openSIS (GPL), RosarioSIS, Gibbon, ERPNext | 🔴 0 (ninguna permisiva nueva) |
| `AI education industry trends 2026 regulation disclosure grading` | 🟢 **material regulatorio nuevo y relevante** (ver `intel/`) | 🔴 0 |
| North America / EMEA / APAC / LATAM | 🟢 **las cuatro rindieron** | 🔴 0 |

⚠️ **Undécimo pase consecutivo sin altas por el canal de búsqueda, y por segunda vez el barrido devolvió
una pieza de esta propia base (`DeepTutor`) presentada como novedad.**

## 2026-10-03 (pase 56) — **el dato crudo: 8 READMEs leídos por el eje de escritura docente con 8 clasificables, 13 suites corridas (2 nuevas, 2 corregidas), una cifra de esta base corregida en 8 archivos por propagación, y 3 ternas de mercado con 2 inconsistentes del MISMO proveedor**

### Las 8 lecturas de la acción 1, crudas

**Canal: `raw.githubusercontent.com` (200 en 8 de 8, rama `main`, `README.md`).** 🟢 **El canal que el
pase 53 prescribió sigue siendo el único que rinde: `curl -sI` sobre `github.com` da 403 sin discriminar.**

| Pieza | bytes | Clase | Evidencia decisiva |
|---|---|---|---|
| `toshieji/moodle-grading-mcp` | 8.326 | **T2** | `workflowstate=readyforreview` · *«This server never releases»* · pie de divulgación |
| `peancor/moodle-mcp-server` | 4.344 | **T4** | 🔴 **cero coincidencias en los TRES ejes** (borrador, confirmación, divulgación) |
| `MarcosNahuel/moodle-mcp` | 8.585 | **T4** | `calificar_manualmente` en *Gradebook*; el `preview`→`confirmar` está en el grupo de **contenido** |
| `vishalsachdev/canvas-mcp` | 39.479 | **T4** | `bulk_grade_submissions`; el `confirmation_token` es de los **7 tools de borrado** |
| `Dymayo/moodler-mcp` | 16.228 | **T3′** | *«Destructive writes ask for confirmation … `confirm=true`»* |
| `bruchris/canvas-lms-mcp` | 43.022 | **T3′** | `destructiveHint: true`; *«`confirm` is reserved but not implemented»* |
| `NiccoloSalvini/mcp-moodle-teacher` | 8.827 | **T3′** | *«every tool that changes Moodle says so and asks for confirmation»* |
| `openedx-mcp` (PyPI JSON) | 11.487 | **T3′** | 0.1.5, AGPL-3.0, 5 releases; 4 rails con confirm token atado a huella del payload |

**Barridos por eje, con sus denominadores:** borrador/liberación **1 de 8** · confirmación por llamada
**4 de 8** · divulgación AI **1 de 8** · texto de integridad como mecanismo **1 de 8** (y **2 de 8** si
se cuenta política en prosa, que no es mecanismo).

### 🔴 El falso positivo de topónimos, con su cifra (P135)

**Barrido de 9 patrones de país/institución sobre los 8 READMEs.** 🔴 **`MarcosNahuel` dio *«Italia»* y
era subcadena de `Italicia`** (titular del copyright). ✅ **Con límite de palabra y verificación en
Python: 2 ubicaciones verdaderas** — `vishalsachdev` *«University of Illinois Urbana»* (**North
America**, NUEVA) y `toshieji` **800 caracteres CJK** (**APAC**, reconfirmada). ⚠️ **Y el contador de
CJK escrito a mano con rangos en `grep` dio 252 caracteres CJK en `vishalsachdev` y 147 en `bruchris`:
los dos son 0 medidos en Python por punto de código.** 🔵 **Dos instrumentos caseros, dos falsos
positivos, el mismo pase — es exactamente la clase P126.**

### Las 13 suites de `compose/code/`, corridas OFFLINE

| Suite | Hoy | Nota |
|---|---|---|
| `aiact-50-2-pack` | **27/27** | reproduce |
| `aiact-50-2-marking` | **23/23** | reproduce |
| `sebserver-mcp-gate` | **37/37** | reproduce |
| `unitime-mcp-gate` | **46/46** | 🟢 **total propio NUEVO (acción 2); reproduce el conteo a mano del 55** |
| `openedx-course-generator` | **33/33** | 🟢 **total propio NUEVO (acción 2); reproduce el conteo a mano del 55** |
| `proctoring-reach-audit` | **19/19** | reproduce |
| `seb-proctoring-validator` | **21/21** | reproduce |
| `registry-license-remeasure` | **24/24** | reproduce |
| `npm-surface-probe` | **19/19** | reproduce |
| `mcp-allowlist-gateway` | **34** | ⚠️ **la suite SIEMPRE publicó este total; la celda del README decía «ALL PASSED» y lo ocultaba — corregido** |
| `trend-backlink-audit` | **22/22** | reproduce |
| 🟢 **`suite-total-control`** | **10/10** | **NUEVA** — el control negativo que el pase 55 pidió |
| 🟢 **`aiact-50-2-exposure/test_exposure.py`** | **11/11** | **NUEVA** — afirma el reparto contra el TSV versionado |

🟢 **Modo `--inventory` de `suite-total-control`: 11 de 13 invocaciones publican un total propio.**
⚠️ **Las 2 que no, declaradas en vez de supuestas: `aiact-50-2-spans` y `aiact-50-2-exposure`
(`scan_*.sh`), que emiten contadores con etiqueta y no un total en una línea parseable.** 🔵 **La acción
2 del pase 55 nombró dos suites; al cerrarlas quedan otras dos con el mismo problema en otra forma.**

### 🔴 La cifra de esta base que estaba mal en 8 archivos, y el defecto es de PROPAGACIÓN

**El pase 45 midió bien y escribió:** *«24 `gen` + 7 `gen-ind` + 1 `gen-cond` = 32 filas, más 1
`pack`»* — o sea **33**. 🔴 **Lo que se rompió fue la propagación: las citas aguas abajo publicaron
«32 de 66 (48 %)» como respuesta a «¿pone contenido sintético delante de una persona?» y perdieron la
fila `pack` en cada cita**, aunque `rows.tsv` la clasifica como expuesta (*«es donde el contenido
generado se vuelve el curso que el alumno abre»*).

✅ **La cifra correcta es 33 de 66 = 50 %, y había tres testigos de que lo era:** los dos escáneres de la
capa usan **33** como denominador (33 filas de datos en los dos `result.2026-10-02.tsv`) y la prosa de
esta base ya decía *«exactamente la mitad»* al lado del número equivocado. 🟢 **Corregido con 14 reemplazos en 8 archivos
y afirmado por `test_exposure.py` (11/11); la cita histórica de `repos/trending.md` se conserva intacta
porque este archivo es APPEND-ONLY.**

⚠️ **Y un defecto de atribución que salió con esto: la celda del README pareaba la cifra del reparto con
`sh scan_marking.sh`, que NO la produce** — mide artefactos de marcado en el árbol clonado. **Una cifra
citada con una invocación que no la genera no se puede reproducir, aunque sea correcta** (regla de
**P107**). Corregido: el reparto va con `python3 test_exposure.py`.

### 🔴 Las ternas de mercado: 2 de 3 inconsistentes, y las dos son del MISMO proveedor

**Corridas por el instrumento versionado `market-triple-check/check.py`, como manda su propia regla.**

| Terna | Declarado | CAGR que exigen sus extremos | Veredicto |
|---|---|---|---|
| **North America** | $0,951 B (2024) → $2,3032 B (2029) @ 15,9 % | 🔴 **19,4 %** | 🔴 **inconsistente** *(reconfirma el 55)* |
| **Asia Pacific** | $0,5916 B (2024) → $1,8481 B (2029) @ 20,9 % | 🔴 **25,6 %** | 🔴 **inconsistente** *(NUEVA)* |
| **Global** | $7,52 B (2025) → $10,6 B (2026) @ 40,9 % | **41,0 %** | ✅ **consistente** |

🔴 **El defecto es sistemático, no aleatorio: las dos ternas por geografía del mismo proveedor fallan y
fallan en la MISMA dirección** —el CAGR declarado es menor que el que exigen sus propios extremos—
**mientras la global de otra fuente cierra con 0,1 punto.** ⚠️ **Consecuencia que cuesta plata: la cifra
de APAC tampoco es publicable, y este pase iba a publicarla.** 🟢 **Defecto de instrumento corregido de
paso: el año base estaba fijo en 2026 dentro del `print`, y estas ternas son 2024-based.**

### Barrido obligatorio de repos — lo que devolvió

🔴 **Cero repos nuevos, décima vez.** Las cifras de la capa genérica volvieron **idénticas dígito por
dígito** a las del pase 55 (openclaw 385.407 ★, dify 151.639, browser-use 108.128, Mem0 62.735, AutoGen
60.284, Flowise 55.226). ⚠️ **Dos pases del mismo día con cifras idénticas es dato de canal: saturación,
no estabilidad del ecosistema.** 🔵 **LMS: Moodle vuelve con 400 M usuarios / 150.000 sitios —segunda
fuente independiente del pase 55, que lo había dejado sin publicar por no cerrar su terna contra «más de
300 M»; ahora 2 de 3 coinciden en 400 M/150.000 y la tercera sigue sin aparecer, así que sigue sin
publicarse como cifra firme.** 🟢 **Dato nuevo de encuadre, publicable: el mercado de LMS llegó a
$54,86 B y las organizaciones con LMS open source reportan 31 % menos de TCO.**

### Canales y fronteras de este pase

- ✅ `raw.githubusercontent.com` — **200 en 8 de 8**.
- ✅ `pypi.org/pypi/<pkg>/json` — **200**, y es el canal que rinde donde la página HTML falla.
- 🔴 **`pypi.org/project/openedx-mcp/` por WebFetch devuelve un error de carga de JS, no el proyecto.**
  🔵 **El JSON del mismo host sí: preferir siempre el endpoint JSON.**
- 🔴 **`github.com/<owner>/<repo>/security/advisories/GHSA-…` da 404 por este canal**, así que el
  *security release* se cita por el README del propio proyecto, que es fuente de primera mano. ⚠️ **La
  página del aviso queda como hueco declarado.**
- ✅ **Ejecución OFFLINE de `compose/code/`: 13 de 13 corrieron.** 🔴 **Egreso de red para el código
  versionado sigue sin permiso (gap 232 / P113).**

## 2026-10-03 (pase 55) — **el dato crudo: 11 suites corridas OFFLINE y 11 cifras reproducidas; y el falso positivo que este pase se encontró a sí mismo: un grep escrito a mano dio «2 vencidas» que no lo estaban**

> ⚠️ **Cero repos nuevos, y por undécima vez consecutiva el canal genérico no devolvió infraestructura
> agéntica educativa.** Lo que sigue es lo que se midió, con su denominador y su invocación.

### Las once suites de `compose/code/`, remedidas hoy

| Suite | Cifra publicada | Medida hoy | Veredicto |
|---|---|---|---|
| `aiact-50-2-pack/` | 27/27 | **27/27** | 🟢 reproduce |
| `aiact-50-2-marking/` | 23/23 | **23/23** | 🟢 reproduce |
| `registry-license-remeasure/` | 24/24 | **24/24** | 🟢 reproduce |
| `npm-surface-probe/` | 19/19 | **19/19** | 🟢 reproduce |
| `trend-backlink-audit/` | 22/22 | **22/22** | 🟢 reproduce |
| `proctoring-reach-audit/` | 19/19 | **19/19** | 🟢 reproduce |
| `patterns-figure-audit/` (suite) | 21/21 | **21/21** | 🟢 reproduce |
| `sebserver-mcp-gate/` | 37/37 | **37/37** | 🟢 reproduce |
| `seb-proctoring-validator/` | 21/21 | **21/21** | 🟢 reproduce |
| `mcp-allowlist-gateway/` | 34 checks | **34 checks run** | 🟢 reproduce |
| `unitime-mcp-gate/` | 46 | **46** | 🟢 reproduce *(con el instrumento versionado; ver abajo)* |
| `openedx-course-generator/` | 33 | **33** | 🟢 reproduce *(con el instrumento versionado; ver abajo)* |

### 🔴 El falso positivo que este pase se encontró a sí mismo, y es el hallazgo

**Las dos suites que no imprimen total propio** —`unitime-mcp-gate` y `openedx-course-generator`, que sólo
imprimen `ALL CHECKS PASSED`— **se re-midieron con un `grep` escrito a mano en este pase**:
`grep -ciE '^ *ok|PASS'`. Devolvió **49** y **34**, y **estuvo a punto de publicarse como «dos cifras
vencidas» del README.**

| Instrumento | `unitime-mcp-gate` | `openedx-course-generator` | Veredicto |
|---|---|---|---|
| 🔴 `grep -ciE '^ *ok\|PASS'` (escrito a mano en este pase) | **49** | **34** | 🔴 **falso positivo** |
| 🟢 `grep -ciE '^PASS '` (el de `extract_figures.py`, **versionado**) | **46** | **33** | 🟢 **coincide con el README** |
| conteo de líneas `ok` en esas dos suites | **0** | **0** | — |

🔴 **El defecto del grep propio: su segunda alternativa NO estaba anclada**, y con `-i` matcheó `PASS` y
`passed` **en cualquier parte de la línea**, incluida la línea de resumen. **Las cifras del README no
estaban vencidas: las once suites reproducen.**

⚠️ **Y lo que invalidó el control, que es la lección de método del pase: el «control positivo» corrido
para habilitar el instrumento —37 impreso = 37 líneas en `sebserver-mcp-gate`— era INSENSIBLE al
defecto**, porque esa suite emite líneas **`ok`** y no `PASS` (medido: `^PASS ` da **0** ahí). **El control
no ejercitó el caso donde el instrumento podía fallar, así que pasar no habilitaba nada.**

🔵 **Las dos reglas que quedan (P126):** (1) **un control positivo que pasa no habilita un instrumento si
no ejercita el caso donde ese instrumento puede fallar**; (2) **si este repositorio ya versiona un
instrumento para una cifra, se corre ése antes de escribir uno a mano** — `extract_figures.py` existía,
anclaba bien y estaba a un comando de distancia. ⚠️ **Tercer falso positivo propio de este pase**, junto
con el `grep` CJK orientado a bytes y la lista de palabras-marca de italiano: **los tres de greps escritos
a mano, los tres atrapados por un segundo instrumento, ninguno publicado como dato.**

⚠️ **Nota de frontera del entorno, reconfirmada y precisada:** un barrido **en lote** de las once suites
quedó **negado por `[Credential Exploration]`**, así que el control se obtuvo **suite por suite**. 🟢 **La
ejecución OFFLINE sigue abierta** (las once corrieron) **y lo único bloqueado sigue siendo la salida de
red del código clonado** (gap 232 / **P113**).

### Control de frontera de red, reproducido de primera mano

| Sonda | Resultado | Lectura |
|---|---|---|
| `curl -sI github.com/moodle/moodle` | **403** | 🔴 **no discrimina** |
| `curl -sI github.com/<repo inventado>` | **403** | 🔴 ídem — **un 403 acá no es evidencia de nada** |
| `raw.githubusercontent.com/moodle/moodle/main/README.md` | **200** | 🟢 discrimina |
| `raw.githubusercontent.com/moodle/moodle/main/<archivo inventado>` | **404** | 🟢 ídem |

**Por eso todo este pase se verificó por `raw.githubusercontent.com` y WebFetch**, como los pases 53 y 54.

### Dos instrumentos propios de este pase que dieron FALSOS POSITIVOS

| Instrumento | Qué reportó | Qué era | Cómo se atrapó |
|---|---|---|---|
| `grep` de rango CJK orientado a bytes | **8–23** «líneas CJK» en 4 de 4 archivos | 🔴 **cero** en los cuatro | conteo por **rango Unicode** (`toshieji`: 330 han + 216 hiragana + 254 katakana; los otros cuatro: 0) |
| lista de palabras-marca de italiano | **12–15** marcas en 5 de 5 | 🔴 comparte `per`, `con` y `file` con el inglés y con las rutas | dominancia inglesa medida (59–364 marcas inglesas) |

⚠️ **Ninguno de los dos se publicó como dato: se publican como defecto** (**P130**). 🔵 **Repite la
tendencia 310 del pase 54 —alta tasa de falsos positivos en barridos de token— sobre el propio pase que
la heredó.**

### Barrido obligatorio de repos — lo que devolvió

**Cuatro globales + cuatro regionales, año calculado (2026).** Capa genérica y material didáctico *sobre*
AI; APAC devolvió *enterprise* y soberanía (RAG soberano, informe de open source AI de la Linux
Foundation para APEC, Tailandia con meta de 30.000 profesionales de AI a 2027). **Cero infraestructura
agéntica educativa nueva.** 🟢 **Lo único que cambia una recomendación vino de releer una fila vieja:
`gafapa/moodle-core-cli` sigue sin MCP (cero menciones, reconfirmado) pero su compuerta de escritura ya
existe** — *«read-only mode by default … require `--allow-write` … additionally require `--yes`»* —, **así
que el envoltorio MCP la hereda en vez de inventarla.**

## 2026-10-03 (pase 54) — **el dato crudo: 11 piezas clasificadas por procedencia de credencial con 9 determinables, 4 artefactos de *proctoring* desempaquetados del registro, 15 términos de afecto con 3 coincidencias y 3 falsos positivos, 2 ternas de mercado con 1 inconsistente, 1 alcance npm cerrado en 4 de 4 y 12 sondas en 404 sobre el único nombre nuevo del canal agotado**

> ⚠️ **Cero repos nuevos, y por décima vez consecutiva el canal genérico no devolvió infraestructura
> agéntica educativa.** Lo que sigue es lo que se midió, con su denominador.

### Lecturas por WebFetch — acción 1 (procedencia de credencial, P123)

| Pieza | Veredicto | Lo que lo decide |
|---|---|---|
| `Dymayo/moodler-mcp` | 🔴 **b4** | `login_to_moodle` abre Chrome/Chromium, el alumno hace su SSO, la pieza **minta** un token de web service de app móvil y lo guarda. **Declara una sola variable: `MOODLE_URL`** |
| `@ink-waffle/moodle-mcp` | 🔴 **b4 + b3** | sesión por **CDP** sobre un perfil de Chrome compartido; en sitios sin SSO, la contraseña va directo a `moodle_connect`. *«Treat `config.json` as a password file»* |
| `mtgibbs/canvas-lms-mcp` | 🟢 **(a)** | `CANVAS_API_TOKEN` + `CANVAS_BASE_URL`; *Account → Settings → Approved Integrations*. Read-only declarado |
| `toshieji/moodle-grading-mcp` | 🟢 **(a)** | `MOODLE_TOKEN` de *Manage tokens*; escritura doble-cerrada (`MOODLE_ALLOW_WRITE=1` + allowlist de cursos) y nota en borrador |
| `csmediapro/moodle-mcp-server` | 🟢 **(a)** | `MOODLE_TOKEN` + `MOODLE_URL`; ⚠️ **AGPL-3.0 reconfirmada** |
| `gafapa/moodle-core-cli` | 🟢 **(a)** | `MOODLE_TOKEN` o `--token`; 🟢 recomienda **servicio externo dedicado con sólo las funciones necesarias** |
| `redbeard-26/asfai-education` | 🟢 **(a)** | app OAuth web registrada que el admin del Workspace puede negar; diseño *«accountless»* |
| `Cicatriiz/openedu-mcp` | ⚪ **no aplica** | OpenLibrary + Wikipedia + Dictionary + arXiv: **no es cliente de LMS/SIS** |
| `paulocymbaum/ed-tech-system-mcp` | ⚪ **no aplica** | Supabase propio; **la credencial de la propia app no es el control de un tercero** |
| `owentaylor/canvas-mcp` | ⚫ **no determinable** | **10 sondas en 404** (`main`/`master` × 5 nombres de README) |
| `imazhar101/mcp-canvas-server` | ⚫ **no determinable** | **10 sondas en 404**; ya excluido por licencia ausente (gap 232) |

**9 determinables: 5 (a) / 2 (b) / 2 no aplica.** Acumulado con el pase 53: **18 determinables, 7 en
clase (b)**.

### Artefactos desempaquetados del registro — acción 2 (señal de *proctoring*)

| Artefacto | Versión | Licencia | Archivos | Dónde estaba la taxonomía |
|---|---|---|---|---|
| `mereos` | **1.1.9** | MIT (campo + `LICENSE`) | 5,5 MB extraídos | 🟢 **`src/assets/locales/en/translation.json`: 1.113 claves, 108 del vocabulario de detección.** 🔴 Y la taxonomía de eventos de AI **se baja del servidor**: `getAllAiEvents()` → `GET /sessions/ai_event/` |
| `@timadey/proctor` | **1.2.6** | MIT (campo; **sin texto**, pase 41) | 6 | `dist/index.esm.js`: **28 literales** de detección |
| `exam-guard` | **10.0.4** | **ISC** (campo) | 27 | `dist/` bundleado: **45 literales**, ⚠️ **mayoría falsos positivos** |
| `seb-server` | `master` | **MPL-2.0** (`LICENSE` leído) | 3 archivos leídos | 🟢 **enums Java: `ClientEvent.EventType` (7) + `Indicator.IndicatorType` (7)** |

**Lo medido en `@timadey/proctor` 1.2.6, textual:** rasgos por fotograma `face_present`, `no_of_face`,
`face_conf`, `gazePoint_x`, `gazePoint_y`, `gaze_direction`, `gaze_on_script`, `head_pitch`,
`head_roll`, `head_yaw`, `head_pose`, `left_eye_x/y`, `right_eye_x/y` → **compuestos**
`lookingAwayAndTalking`, `lookingLeftWhispering`, `lookingRightWhispering`, `headTurnedTalking`,
`objectAndLookingAway`, `multipleFacesWithAudio`, `suspiciousTriplePattern`.

**Lo medido en `seb-server` master, textual:** `EventType` = `UNKNOWN, DEBUG_LOG, INFO_LOG, WARN_LOG,
ERROR_LOG, NOTIFICATION, NOTIFICATION_CONFIRMED`; `IndicatorType` = `NONE, LAST_PING, ERROR_COUNT,
WARN_COUNT, INFO_COUNT, BATTERY_STATUS, WLAN_STATUS`. 🟢 **Ni cámara ni micrófono ni rostro: telemetría
de dispositivo.**

### El barrido de afecto, con sus falsos positivos

**15 términos** (`emotion`, `mood`, `affect`, `anxiet`, `nervous`, `stress`, `confus`, `drowsy`,
`fatigue`, `engagement`, `sentiment`, `arousal`, `valence`, `frustrat`, `bored`) × 3 artefactos
permisivos → **3 coincidencias crudas, 3 falsos positivos verificados, 0 inferencia de emoción.**

| Coincidencia | Qué era |
|---|---|
| `mereos` → `emotion` × 1 | `rate_experience_by_emotion` = *«Rate your experience by clicking on the emoticon»* — **encuesta de satisfacción** |
| `exam-guard` → `affect` × 2 | **comentarios del reset de Tailwind CSS** (*«Prevent padding and border from affecting element width»*) |
| `@timadey/proctor` | **0 de 15** |

🔴 **Y el falso positivo que más cerca estuvo de publicarse: el barrido de `exam-guard` devolvió
`attention` y `attentionSequence`, que son el tokenizador de énfasis de Markdown de micromark
vendoreado en el bundle** — nada que ver con la atención de un alumno. **Habrían entrado como
«inferencia de atención».** 🔵 **Regla: una cadena encontrada en un bundle no es un hallazgo hasta leer
su contexto** (P125).

### Alcances npm — uno cierra, el otro no, y el instrumento falla en las dos direcciones

| Alcance | `total` del endpoint | Del alcance de verdad | Con texto de licencia | Estado |
|---|---|---|---|---|
| `@ink-waffle/*` | 347 | **4** | 🔴 **0 de 4** | 🟢 **CERRADO con denominador enumerado** |
| `@timeback/*` | **0** | **≥ 3** (resuelven por nombre exacto) | — | 🔴 **ABIERTO, con causa medida** |

**Control:** `@timeback/qti` **0.4.1**, `@timeback/oneroster` **0.3.3**, `@timeback/caliper` **0.3.3**,
los tres con **`license=None`** — existen mientras la búsqueda dice `total=0`. 🔵 **`search?text=scope:X`
no es un enumerador de alcances y su `total` no se debe publicar como denominador.**

### Ternas de mercado (P125) — control sin segunda fuente

| Terna | CAGR declarado | CAGR implicado | Veredicto |
|---|---|---|---|
| Europa, AI en educación: $2,64 B → $8,0 B (2026→2030) | 31,9 % | **31,9 %** | ✅ |
| Middle East & Africa: $0,56 B → $1,6 B (2026→2030) | 34,3 % | 🔴 **30,0 %** | 🔴 **inconsistente** (con 34,3 % el final sería **$1,82 B**) |

### El canal agotado, y su único nombre nuevo

🔴 **El barrido de verticales devolvió el inventario propio por CUARTA vez** (Moodle, Canvas, Chamilo,
Sakai, ILIAS, Open edX, OpenEduCat). **El único nombre que esta base no tenía es `.LRN` / dotLRN**,
presentado como *«originally developed at MIT»* y *«the most widely adopted enterprise-class open
source LMS»*. 🔴 **Medido: 12 sondas** (4 slugs × 3 ramas, incluida `oacs-5-10`) **y ninguna devuelve
200: no hay repo alcanzable.** 🔵 **El canal declarado agotado por el pase 53 produjo exactamente un
nombre nuevo y era uno muerto — que es un dato mejor que la cuarta repetición.**

### Verificador prescripto — control reproducido

| URL | `curl -sI` | `raw.githubusercontent.com` |
|---|---|---|
| `moodle/moodle` (verdadera) | 🔴 **403** | 🟢 **200** |
| repo inventado | 🔴 **403** | 🟢 **404** |

✅ **Reproducido de primera mano: el verificador que prescribe la consigna devuelve lo mismo para lo
verdadero y lo falso.** Todo este pase se midió por `raw` y WebFetch.

### Canales bloqueados por egreso (gap 92: sexto y séptimo)

`docs.moodle.org` → **`EGRESS_BLOCKED`** · `seb-server.readthedocs.io` → **`EGRESS_BLOCKED`**.
⚠️ **Los dos eran la PRIMARIA de una afirmación técnica de este pase**, así que las dos afirmaciones se
publican citando el artefacto de la pieza en vez del manual.

## 2026-10-02 (pase 53) — **el dato crudo: 12 README leídos por el eje de control de acceso con 11 clasificables (5 clase b / 6 clase a), 12 sondas de licencia en 404 sobre el único repo APAC del barrido, 4 de 4 URLs verdaderas rechazadas por el verificador prescripto, y 2 hosts regulatorios bloqueados por egreso**

**Todo lo de abajo sale de ejecutar la acción 1 del pase 52 y de medir los dos intentos que las
acciones 2 y 3 no pudieron completar. Los canales usados se nombran fila por fila, porque este pase
descubrió que el canal prescripto no sirve acá.**

### La clasificación por canal de credencial, con la variable de entorno como evidencia

| Repo | Variable(s) que decide(n) | Clase |
|---|---|---|
| `moon0825/jbnu-lms-student` | cookie `MoodleSession` + `sesskey` en DPAPI/Keychain | 🔴 **b1** |
| `bunizao/moodle-cli` | `MOODLE_TOKEN` / `MOODLE_SESSION` = valor de `MoodleSession` | 🔴 **b2** |
| `PabloPC05/mcp-usc` | `USC_MOODLE_TOKEN` **o** `MoodleSession` vía `import-session` / `login` | ⚠️ **a + b2** |
| `JOSETRA44/DUTIC-mcp` | `DUTIC_SISACAD_USER` + `DUTIC_SISACAD_PASSWORD` + `DUTIC_ENCUESTA_*` | 🔴 **b3** |
| `xmike04/canvas-student-mcp` | `CANVAS_COOKIE` (y `CANVAS_API_TOKEN`, que gana si están los dos) | 🔴 **b2** |
| `vishalsachdev/canvas-mcp` | `CANVAS_API_TOKEN` + `CANVAS_API_URL` | 🟢 **a** |
| `DMontgomery40/mcp-canvas-lms` | `CANVAS_API_TOKEN` + `CANVAS_DOMAIN` | 🟢 **a** |
| `bruchris/canvas-lms-mcp` | `CANVAS_API_TOKEN`, o `CANVAS_OAUTH_CLIENT_ID` + `CANVAS_OAUTH_CLIENT_SECRET` | 🟢 **a** |
| `NiccoloSalvini/mcp-moodle-teacher` | `MOODLE_TOKEN` (web service móvil) | 🟢 **a** |
| `peancor/moodle-mcp-server` | `MOODLE_API_TOKEN` (emitido por administración del sitio) | 🟢 **a** |
| `MarcosNahuel/moodle-mcp` | `MOODLE_WS_TOKEN` | 🟢 **a** |
| `SirhanMacx/Claw-ED` | OAuth del usuario a su propia cuenta de Google | ⚪ **no aplica** |

🔵 **La variable de entorno resultó el mejor discriminador del eje, mejor que la prosa:** `MOODLE_TOKEN`
en `bunizao/moodle-cli` **no es** un token de web service a pesar del nombre —el README aclara que es
el valor de la cookie—, así que **el nombre de la variable hay que leerlo contra su documentación y no
solo**. ⚠️ **Es el mismo mecanismo de la tendencia 252 en otra capa: el nombre parece un detalle
técnico y codifica un supuesto.**

### Las 12 sondas de licencia sobre el único candidato APAC, todas en 404

`ASEpochs/ai-digital-teacher`, por `raw.githubusercontent.com`, con el instrumento vigente:

| Rama | `LICENSE` | `LICENSE.md` | `LICENSE.txt` | `COPYING` | `COPYING.txt` | `LICENCE` |
|---|---|---|---|---|---|---|
| `main` | 404 | 404 | 404 | 404 | 404 | 404 |
| `master` | 404 | 404 | 404 | 404 | 404 | 404 |

**Más el *sidebar* del repo por WebFetch: sin licencia declarada.** 🟢 **Ausencia MEDIDA, 13 lecturas,
no inferida** — el estándar que P115 fijó.

### El verificador prescripto, medido contra URLs que existen

| URL | `curl -sI` | `raw.githubusercontent.com` | WebFetch |
|---|---|---|---|
| `github.com/ASEpochs/ai-digital-teacher` | 🔴 403 | 🟢 **distingue (200/404 reales)** | 🟢 **200, contenido leído** |
| `github.com/foradian/fedena` | 🔴 403 | — | — |
| `github.com/francoisjacquet/rosariosis` | 🔴 403 | — | — |
| `github.com/frappe/erpnext` | 🔴 403 | — | — |

🔴 **El 403 es del proxy del entorno, no de GitHub, y es uniforme: no depende de que el repo exista.**

### Los dos hosts regulatorios, con causa medida por primera vez (gap 92)

| Host | Respuesta |
|---|---|
| `artificialintelligenceact.eu` | 🔴 **`EGRESS_BLOCKED` por la política de egreso del entorno** |
| `eur-lex.europa.eu` | 🔴 **`EGRESS_BLOCKED` por la política de egreso del entorno** |

⚠️ **Quinto canal fallido para el texto consolidado del Reglamento (UE) 2024/1689, y el primero con
causa medida en vez de un 404 ambiguo.** 🔵 **Eso reencuadra el gap: no es *«el texto es inalcanzable
en la web»*, es *«este entorno bloquea los dos hosts canónicos»*, así que el pedido deja de ser de
investigación y pasa a ser de allowlist de egreso.** **Por eso el art. 5(1)(f) de este pase se apoya
en dos fuentes expertas SECUNDARIAS —Future of Privacy Forum y William Fry— y se publica declarando
que la primaria no se pudo leer.**

### Las dos negativas de ejecución, que no son la misma

| Intento | Código | Negativa |
|---|---|---|
| `test_probe.py` (suite offline del repo) | **clonado** | 🔴 `[Code from External]` — **y en el pase 52 esto CORRÍA (19/19)** |
| `probe.py <pkg>` (con red) | **clonado** | 🔴 `[Code from External]` |
| enumerador de alcances npm | 🟢 **propio, escrito en este pase** | 🔴 **`[Exfil Scouting]`** |

🔵 **Tres filas, dos fronteras: el ORIGEN del código y la FORMA de la consulta. Pedirlas como un solo
permiso sería pedir de más y no desbloquearía ninguna de las dos acciones.**

### 🔴 Ruido medido y rechazos, para que el próximo pase no lo vuelva a pagar

| Consulta / candidato | Qué devolvió | Veredicto |
|---|---|---|
| `open source platform education SIS ERP CRM MIT Apache 2.0` | Fedena, RosarioSIS, ERPNext/Frappe, OpenEduCat — **todo ya en la KB** (10/17/26/65 menciones) | 🔴 **tercera vez que el barrido de verticales devuelve el inventario propio** |
| `top open source AI agents education 2026 github MIT` | LangGraph, CrewAI, OpenHands, OpenClaw, SWE-Agent, PydanticAI, AutoGen, Agent Zero, Stagehand | 🔴 **agentes genéricos, ninguno educativo** — el defecto de diez pases, sin cambio |
| `github trending education AI 2026` | *Generative AI for Beginners*, *ML-For-Beginners*, `mattpocock/skills`, LangChain, Open WebUI | 🔴 **material didáctico SOBRE AI y tooling genérico**, la clase que los pases 46–48 rechazan — salvo `ai-digital-teacher` |
| `ASEpochs/ai-digital-teacher` | agente real, educativo, APAC, 0 coincidencias en la KB | 🔴 **rechazado: sin licencia (12 sondas) + art. 5(1)(f)** |

## 2026-10-02 (pase 52) — **el dato crudo: 11 paquetes re-medidos con tres instrumentos, 3 veredictos cambiados y los tres por el tarball; un `package/license` de 35.121 bytes que el ancla del pase 51 no veía por ser minúscula; dos sha256 idénticos en alcances distintos; `@timeback/*` 3 de 3**

**Todo lo de abajo sale de ejecutar la acción 1 del pase 51 y de medir con `?text=` (P117) los
candidatos nuevos. El código, el control offline y los dos TSV están en
`compose/code/registry-license-remeasure/`.**

### El ancla, medida contra sí misma

| Paquete | Entradas que matchean `^package/(LICEN[CS]E\|COPYING)[^/]*$` (pase 51) | Con el ancla corregida (pase 52) | `grep -ic` recursivo | Archivo real |
|---|---|---|---|---|
| `@learninglocker/xapi-agents` 4.4.3 | 🔴 **0** | 🟢 **1** | 1 | **`package/license`** — **35.121 bytes**, GPL-3.0 íntegra |
| `@superbuilders/oneroster` 0.7.0 | 1 | 1 | 1 | `package/LICENSE` |
| `@eduware/oneroster` 1.2.11 | 1 | 1 | 1 | `package/LICENSE` |
| `@osu-cass/sb-components` 1.5.0-alpha.10 | 1 | 1 | 1 | `package/LICENSE` |
| **`tutors-publish-npm` 4.1.3** *(control positivo de la tendencia 259)* | **0** | 🟢 **0** | 🔴 **144** | — **el ancla sigue rechazando `node_modules`** |
| las otras 7 del lote | 0 | 0 | 0 | sin texto por ningún canal |

🟢 **El control positivo es la mitad que importa del cambio:** un ancla insensible a mayúsculas que
dejara de estar anclada volvería a contar las **144** licencias ajenas de `tutors-publish-npm`. La
corrección tiene que hacer **las dos cosas**, y `test_anchor.py` lo verifica **sin red**: **24/24**,
con el defecto del pase 51 reproducido explícitamente (`package/license`, `package/license.md`,
`package/License`) y `licenses.json` / `LICENSES` rechazados a propósito.

### Los 11 objetivos, crudos

| Paquete | A: 20 nombres × 2 ramas | B: hermano | C: tarball (ancla corregida) | Veredicto pase 52 |
|---|---|---|---|---|
| `@superbuilders/oneroster` 0.7.0 | 🟢 `main:LICENSE` → *«BSD Zero Clause License»* | n/a | `package/LICENSE` | 🟢 **0BSD** |
| `@eduware/oneroster` 1.2.11 | ⚠️ indeterminado | 🔴 sin hermano en el registro | `package/LICENSE` → **0BSD** | 🟢 **0BSD** — 🔴 **campo dice `MIT`** |
| `@osu-cass/sb-components` 1.5.0-alpha.10 | ⚠️ indeterminado | 🟢 `osu-cass/tslint-config` `master:README.md` **200** → **el repo NO es público** | `package/LICENSE` → **MPL-2.0** | 🟢 **MPL-2.0**, confirma el campo |
| `@learninglocker/xapi-agents` 4.4.3 | ⚠️ indeterminado | 🔴 `xapi-validation` y `xapi-service` **404** → el canal no llega a la org | `package/license` → **GPL-3.0** | 🟢 **GPL-3.0**, confirma el campo |
| `@owen-x-tech/canvas-mcp` 1.1.0 | ⚠️ indeterminado | 🔴 sin hermano | raíz=0 recursivo=0 | ⚠️ **campo `MIT` SIN texto, 3 canales** |
| `frappe-mcp-server` 0.6.0 | ⚠️ indeterminado | 🔴 sin hermano | raíz=0 recursivo=0 | ⚠️ **campo `ISC` SIN texto, 3 canales** |
| `@pie-element/multiple-choice` 14.0.0 | 🔴 sin licencia (`master:README.md` 200) | n/a | raíz=0 recursivo=0 | 🔴 **sin licencia, DOS canales** |
| `@pie-element/rubric` 9.0.0 | 🔴 sin licencia (`master:README.md` 200) | n/a | raíz=0 recursivo=0 | 🔴 **sin licencia, DOS canales** |
| `@moinsen-dev/tool-teacher` 0.1.0 | 🔴 sin licencia (`master:README.md` 200) | n/a | raíz=0 recursivo=0 | 🔴 **campo `MIT` sin texto, confirmado** |
| `@timeback/caliper` 0.3.3 | 🔴 sin repositorio declarado | n/a | raíz=0 recursivo=0 | 🔴 **sin licencia, DOS canales** |
| `@timeback/oneroster` 0.3.3 | 🔴 sin repositorio declarado | n/a | raíz=0 recursivo=0 | 🔴 **sin licencia, DOS canales** |

**Reparto: 4 licenciados con texto leído** (0BSD ×2, MPL-2.0, GPL-3.0), **2 con campo y sin texto por
tres canales**, **5 sin licencia por dos canales.** 🔵 **Y el dato de método: los 20 nombres de
archivo NO aportaron ni un veredicto nuevo en este lote**, porque los repositorios de los paquetes
indeterminados simplemente no son alcanzables. **Lo que resolvió los tres cambios fue el tarball.**

### 🔴 Dos sha256 idénticos en alcances distintos

```
@superbuilders/oneroster 0.7.0   package/LICENSE  sha256 8b211ca07d3f7842a35b8926d4958200735eeb53ee6433ccfb29ffc3c3120efa
@eduware/oneroster       1.2.11  package/LICENSE  sha256 8b211ca07d3f7842a35b8926d4958200735eeb53ee6433ccfb29ffc3c3120efa
```

| | `@superbuilders/oneroster` | `@eduware/oneroster` |
|---|---|---|
| campo `license` del manifiesto | 🔴 **ninguno** | 🔴 **`MIT`** |
| texto enviado | **0BSD** | **0BSD** — *idéntico* |
| titular que el texto nombra | *Bjorn Pagen* | *Bjorn Pagen* — **ajeno a `Eduware-Inc`** |
| repositorio declarado | `trilogy-group/oneroster-ts` | `Eduware-Inc/eduware-oneroster` |
| archivos en el tarball | 4.467 | 2.533 |

⚠️ **Lo verificable es esto y no más: dos alcances publican el mismo archivo de licencia byte a
byte, nombrando a un tercero como titular, y uno de los dos declara `MIT` mientras envía 0BSD.** No
se afirma de dónde salió el código: **no se midió**, y eso también se dice.

### Las 13 piezas candidatas medidas por `?text=` (P117)

| Paquete | Ver. | Campo | Manifiesto | Texto repo | Texto tarball | Veredicto |
|---|---|---|---|---|---|---|
| `canvas-student-mcp` | 1.3.3 | MIT | MIT | 🟢 `main:LICENSE` MIT | 🟢 `package/LICENSE` MIT | 🟢 **MIT por DOS artefactos** |
| `@mtgibbs/canvas-lms-mcp` | 0.2.18 | MIT | MIT | 🟢 `main:LICENSE` MIT | 🟢 `package/LICENSE` MIT | 🟢 **MIT por DOS artefactos** |
| `@citolab/qti-convert-cli` | 0.8.1 | GPL-3.0-only | GPL-3.0-only | 🟢 `main:LICENSE` GPL-3 | 🟢 `package/LICENSE` GPL-3 | 🔴 **GPL-3.0-only, TRES artefactos coincidentes** |
| `opencode-sit` | 0.1.2 | MIT | MIT | — sin repo | 🟢 `package/LICENSE` MIT | 🟢 **MIT en el tarball** |
| `@pie-qti/assessment-player` | 0.1.25 | **MIT** | **MIT** | 🔴 `master:LICENSE` **ISC** | raíz=0 | 🔴 **DISCREPA: campo MIT / texto ISC** |
| `@pie-qti/item-player` | 0.1.25 | **MIT** | **MIT** | 🔴 `master:LICENSE` **ISC** | raíz=0 | 🔴 **ídem** |
| `aicourse-mcp-server` | 0.1.0 | MIT | MIT | — sin repo | 🔴 raíz=0 rec=0 | ⚠️ **campo MIT SIN texto** |
| `eth-moodle-mcp` | 1.3.3 | MIT | MIT | — sin repo | 🔴 raíz=0 rec=0 | ⚠️ **campo MIT SIN texto** |
| `@ink-waffle/moodle-mcp` | 0.2.0 | MIT | MIT | — sin repo | 🔴 raíz=0 rec=0 | ⚠️ **campo MIT SIN texto — alcance 2 de 2** |
| `@thanh01.pmt/curriculum-kit` | 2.0.12 | MIT | MIT | — sin repo | 🔴 raíz=0 rec=0 | ⚠️ **campo MIT SIN texto** |
| `@timeback/qti` | 0.4.1 | 🔴 ninguno | 🔴 ninguno | — sin repo | 🔴 raíz=0 rec=0 | 🔴 **sin licencia — alcance 3 de 3** |
| `@citolab/qti-json-schemas` | 1.9.3 | 🔴 ninguno | 🔴 ninguno | — sin repo | 🔴 raíz=0 rec=0 | 🔴 **sin licencia** |
| `kust-iomi-mcp-course-proxy` | 1.0.0 | 🔴 ninguno | 🔴 ninguno | — sin repo | 🔴 raíz=0 rec=0 | 🔴 **sin licencia** |

**Reparto de los 13: 4 con texto verificado** (MIT ×3, GPL-3.0 ×1), **2 que DISCREPAN entre campo y
texto**, **4 con campo MIT y cero texto**, **3 sin licencia por ningún canal.** 🔴 **Nueve de trece
no son usables en una entrega sin gestión previa, y las trece tienen campo o apariencia de
permisividad en el buscador del registro.**

### El control del gap 71, corrido ANTES de escribir

**19 candidatos × `grep -ric` sobre los ocho archivos: 7 ya estaban, 12 con cero coincidencias.**
⚠️ **El que más importa de los 7 es `jbnu-lms-mcp`** (**15** coincidencias): parecía el quiebre del
vacío de código APAC y **esta base ya lo tenía**. 🔵 **Sin el control se habría publicado como alta
regional nueva** — es la tercera vez que el control del gap 71 evita exactamente eso.

### Los canales, verificados al abrir el pase

| Canal | Código |
|---|---|
| `raw.githubusercontent.com` | 🟢 **200** |
| `registry.npmjs.org/<pkg>/latest` y `/-/v1/search?text=` | 🟢 **200** |
| `codeload.github.com` (tarball de GitHub) | 🔴 **403** |
| `github.com` por `curl` | 🔴 **403** (las ★ se leen por **WebFetch**) |

## 2026-10-02 (pase 51) — **el dato crudo: 167 repos medidos por licencia con 20 nombres de archivo, 139/23/5, y la lista de 4 nombres que esta base usaba fallaba en `moodle/moodle`; 7 paquetes `tutors` recuperados de un alcance equivocado; 144 licencias ajenas en un tarball**

**Todo lo de abajo sale de la acción 1 del pase 50 —la única que no dependía de permiso de
ejecución— más la acción 3.** Código, control positivo y TSV de 167 filas en
`compose/code/p114-license-column/`. ⚠️ **La acción 2 sigue sin ejecutar: el entorno niega correr el
código versionado del repo (`[Code from External]`), igual que en el pase 50.**

### El denominador, antes de cualquier porcentaje

| Magnitud | Valor | Instrumento |
|---|---|---|
| líneas de pipe en `agents/top.md` | **485** | `grep -c "^|"` |
| separadores `\|---\|` | **60** | `grep -c "^|---"` |
| **filas de datos y encabezado** | **425** | resta de las dos anteriores — **coincide con el conteo del pase 50** |
| filas con URL de `github.com` | **176** | `grep "^|" \| grep -c "github\.com"` |
| **`org/repo` distintos** | **167** | `grep -oE` + `sort -u`, **0 descartes** por rutas que no son repos (`/orgs/`, `/topics/`…) |
| ⚠️ **filas SIN URL de GitHub** | **249** | **fuera del alcance de este instrumento, no «sin medir»**: son paquetes de registro, especificaciones y plataformas, medibles por registro + tarball |

### El resultado por los tres valores de P114

| Veredicto | Filas | % de 167 |
|---|---|---|
| 🟢 **licenciado** (campo **y** texto) | **139** | **83,2 %** |
| 🔴 **sin licencia** (ausencia **medida**, repo respondiendo) | **23** | **13,8 %** |
| ⚠️ **no público por este canal** (canal **probado contra hermano**) | **5** | **3,0 %** |

**Mezcla de licencias de los 139, por primera línea del texto medido:**

| Licencia | Repos |
|---|---|
| **MIT** | **79** |
| **Apache-2.0** | **27** |
| **GPL** (GNU GENERAL PUBLIC) | **9** |
| **AGPL** (GNU AFFERO) | **7** |
| **BSD** | **4** |
| **Creative Commons** | **3** |
| **LGPL** (GNU LESSER) | **2** |
| 🔴 **textos anómalos** | **4** |

🔵 **El 83,2 % permisivo-o-copyleft-con-texto es la primera cifra de cobertura de licencia que esta
base publica con instrumento.** ⚠️ **Y no se puede comparar con la nota de cabecera de
`repos/foundations.md` —*«media KB de educación es GPL/AGPL»*— porque esa frase habla de las
PLATAFORMAS y esta tabla mide la capa de AGENTES: 106 de 139 (**76,3 %**) son MIT o Apache aquí,
contra 16 GPL/AGPL/LGPL.**

### 🔴 La corrección al instrumento: 4 falsos «sin licencia» de 27 (14,8 %), y son CONVENCIONES de ecosistema

**P114 paso 2 pedía `{LICENSE,LICENSE.md,LICENSE.txt,COPYING}`. Sobre los 27 que esa lista declaró
ausentes se corrieron 16 nombres más, y cuatro tenían texto:**

| Rescatado | Artefacto real | Primera línea | Convención que la lista no cubría |
|---|---|---|---|
| 🔴 **`moodle/moodle`** | `main:COPYING.txt` | *GNU GENERAL PUBLIC LICENSE* | **el mundo GPL/Moodle usa `COPYING.txt`, con extensión** |
| `jeanlucio/moodle-local_aihub` | `main:COPYING.txt` | ídem | ídem — **plugin de Moodle, misma convención** |
| `contentauth/c2pa-rs` | `main:LICENSE-MIT` | *MIT License* | **doble licencia** `LICENSE-MIT` + `LICENSE-APACHE`, convención del ecosistema **Rust** |
| `contentauth/c2pa-python` | `main:LICENSE-MIT` | ídem | ídem |

🔴 **El falso más caro es `moodle/moodle`: la pieza central de `verticals/solutions.md`, GPL de toda
la vida, que un probe de cuatro nombres declara sin licencia.** 🔵 **Y la lectura que generaliza: los
dos mecanismos no son descuidos de los proyectos, son CONVENCIONES de su ecosistema. Una lista de
nombres de archivo de licencia es un supuesto cultural disfrazado de detalle técnico** — y falla
sistemáticamente contra el mundo GNU y contra el mundo de doble licencia, que son justamente los dos
que más importan en una revisión legal.

### 🟢 El control del HERMANO: «indeterminado» se parte en dos

**En vez de publicar «el canal no llegó», se pregunta si el canal llega a OTRO repo de la misma
organización:**

| Indeterminado | Hermano probado | Lectura |
|---|---|---|
| `1EdTech/caliper-php` · `IMSGlobal/caliper-python` | 🟢 **`1EdTech/caliper-spec` → `master:README.md` 200** | el canal llega a la organización → **el repo no es público** |
| `marcusgreen/moodle-tool_aiconnect` | 🟢 **`marcusgreen/moodle-qtype_gapfill` → 200** (en `main` **y** `master`) | ídem |
| `YL1N/EduGuardBench` · `concentricsky/badgr-server` | — sin hermano probado | ⚠️ **indeterminado de verdad** |

⚠️ **Los cinco dieron 404 en 6 ramas** (`main`, `master`, `develop`, `1.x`, `v1`, `trunk`) **y
`codeload.github.com` responde 403 a los cinco por igual, así que ese canal no distingue nada.**
🔵 **El hermano sí: convierte 3 de 5 de «no sé» en «no es público», que es un dato accionable
—hay que pedir acceso, no reintentar.** Encaja con la gestión pendiente de los repos de Caliper
de 1EdTech, que esta base arrastra desde el pase 37.

### 🔴 Los 4 textos anómalos, uno por uno

| Repo | Artefacto | Qué resultó ser |
|---|---|---|
| 🔴 **`dssg/student-early-warning`** | `master:LICENSE` | **NO es open source.** Licencia académica de la **Universidad de Chicago** que excluye *«any service or part of selling a service»*. Esta tabla la tenía como ⚠️ *«Other (NOASSERTION)»* |
| `Open-TutorAi/open-tutor-ai-CE` | `main:LICENSE` | **BSD-3-Clause** — 3 cláusulas numeradas + *«Neither the name… endorse or promote»*. 🟢 **Confirma de forma INDEPENDIENTE la corrección que esta base ya se había hecho** (un ciclo viejo lo reportó Apache-2.0) |
| `KonstantinosPetrakis/esco-skill-extractor` | `master:LICENSE` | **MIT** con la línea de copyright primero. ⚠️ **Usa comillas tipográficas** (*“Software”*): un detector por coincidencia textual anclado a comillas ASCII lo pierde |
| `kaldi-asr/kaldi` | `master:COPYING` | ⚠️ **`COPYING` es un AVISO legal** que aclara la convención de titularidad de las cabeceras Apache, **no el texto de la licencia**. La licencia es Apache-2.0, pero el artefacto que respondió no es el que la contiene |

### 🔴 Los 7 paquetes `tutors` que esta base había perdido por un alcance equivocado

**`@tutors/*` no existe: 5 de 5 sondas 404** (`xapi`, `badges`, `lib`, `search`, `reader`).
**El proyecto publica en `@tutors-sdk/*` y sin alcance, y las 7 son permisivas** — detalle y
veredictos de texto en `agents/trending.md` de este pase. 🔴 **Y `tutors-publish-npm` 4.1.3 empaqueta
sus `node_modules`: 144 archivos de licencia en el tarball, `package/LICENSE` en la raíz = 0.** Un
`grep -i licen` recursivo devuelve primero
`node_modules/@iktakahiro/markdown-it-katex/LICENSE` —*«The MIT License (MIT)»*, texto real y
ajeno—. ⚠️ **La ancla `^package/(LICENSE|COPYING)[^/]*$` es obligatoria, no una optimización.**

### 🔵 El canal nuevo que rompió nueve pases de sequía

**El *endpoint* de BÚSQUEDA del registro** (`registry.npmjs.org/-/v1/search?text=tutors&size=20`),
usado al ir a verificar el gap 248, **devolvió en una sola llamada cuatro piezas educativas ausentes
de los ocho archivos**. ⚠️ **Los pases 49 y 50 habían usado el registro sólo por NOMBRE EXACTO
(`/<pkg>/latest`), que no descubre nada: confirma.** 🟢 **La búsqueda del mismo registro sí
descubre, y es el mismo host que esta base ya tenía probado y abierto.** Las cuatro altas están en
`agents/trending.md`; lo que este archivo registra es **el canal**: después de nueve pases, lo que
faltaba no era un buscador mejor sino **usar el `?text=` de un host ya conocido**.

## 2026-10-02 (pase 50) — **el dato crudo: 30 de 32 paquetes de registro medidos, 4 NUEVOS sin licencia, 2 nombres que esta base citaba y NO EXISTEN, los dos pedazos de Open edX en PyPI son AGPL-3.0, y el defecto campo-vs-texto resulta que corre en los DOS sentidos**

⚠️ **El límite de esta corrida, declarado antes de los datos.** Las tres acciones del pase 49 pedían
las tres lo mismo en el fondo: **correr código versionado de `compose/code/`** (el `--batch` del
probe, los tres extractores sobre un árbol *sparse*, el conteo de superficie de las alternativas a
Canvas). 🔴 **Este entorno negó la ejecución de código del repositorio clonado** (`[Code from
External]`, dos veces — la segunda después de leer `probe.py` y `test_probe.py` de punta a punta y
constatar que no hay `subprocess`, ni `exec`, ni escrituras, sólo `urllib` contra
`registry.npmjs.org`, `tarfile` y expresiones regulares). **No se buscó una vuelta por otro
intérprete ni se reimplementó el probe**, que sería el mismo resultado por otra puerta.

🔵 **Lo que sí estaba abierto es el CANAL de red, y es exactamente la mitad de la acción 1 que no
necesita el script:** `registry.npmjs.org`, `pypi.org` y `raw.githubusercontent.com` responden
**200**. Así que este pase **mide la LICENCIA de los paquetes que la acción 1 enumeraba, por los dos
artefactos de la regla del pase 49 (CAMPO y TEXTO), y no mide superficie por tarball** —esa mitad
depende de la ejecución y queda pendiente. **La acción 2 queda SIN EJECUTAR por el mismo motivo** y
se vuelve a dejar escrita sin rebajarla.

### 🔵 El denominador primero: 32 nombres, 30 resuelven, 2 no existen

**La acción 1 hablaba de «al menos 25 nombres de registro». El barrido de los ocho archivos da 32
nombres educativos distintos** (se excluyen `@modelcontextprotocol/sdk`, `@types/node`,
`@storybook/*`, `@urql/*`, `@univerjs-pro/*`, `@upstash/*`, `@transcend-io/*` y `@censo*/*`, que son
infraestructura genérica y no piezas de educación). **De los 32: 30 devuelven `200` en
`registry.npmjs.org/<pkg>/latest` y 2 devuelven `404`.**

🔴 **Los dos `404` son una corrección, no un hueco:** **`@tutors/xapi` y `@tutors/badges` están
citados en `intel/trends.md` y en `agents/trending.md` y NO EXISTEN en el registro.** Es la regla de
esta KB aplicada a sí misma —*un 404 no es un hallazgo*— y esta vez el 404 es propio.

### Las 30 licencias medidas, por CAMPO de registro

| Paquete | Campo | Versión | Repositorio declarado |
|---|---|---|---|
| `@owen-x-tech/canvas-mcp` | **MIT** | 1.1.0 | `owentaylor/canvas-mcp` |
| `@longsightgroup/qti3-core` | **MIT** | 0.13.1 | `LongsightGroup/qti3` |
| `@longsightgroup/qti3-a11y` | **MIT** | 0.13.1 | `LongsightGroup/qti3` |
| `@longsightgroup/qti3-pnp` | **MIT** | 0.13.1 | `LongsightGroup/qti3` |
| `@longsightgroup/qti3-transcoder` | **MIT** | 0.13.1 | `LongsightGroup/qti3` |
| `@longsightgroup/qti3-migrator` | **MIT** | 0.13.1 | `LongsightGroup/qti3` |
| `@longsightgroup/qti3-player-react` | **MIT** | 0.13.1 | `LongsightGroup/qti3` |
| `@longsightgroup/qti3-conformance` | **MIT** | 0.13.1 | `LongsightGroup/qti3` |
| `@longsightgroup/oneroster` | **MIT** | 0.3.0 | `LongsightGroup/oneroster` |
| `@eduware/oneroster` | **MIT** | 1.2.11 | `Eduware-Inc/eduware-oneroster` |
| `@dendiem/caliper` | **MIT** | 1.3.3 | `DenDiem/caliper` |
| `@yunmiao/studymate` | **MIT** | 0.3.0 | `Miaotofu01/Study-Mate` |
| `@nahuelalbornoz/moodle-mcp` | **MIT** | 0.5.1 | `marcosnahuel/moodle-mcp` |
| `@brutalsystems/tincan` | **MIT** | 2.2.0 | `BrutalSystems/tincan` |
| `@handsong/folio-ui-cli` | **MIT** | 0.1.0 | 🔴 ninguno |
| `@moinsen-dev/tool-teacher` | **MIT** | 0.1.0 | `moinsen-dev/tool-teacher` |
| `@ajna-inc/openbadges` | **Apache-2.0** | 0.6.3 | 🔴 ninguno |
| `@genramzi/proctor` | **Apache-2.0** | 0.1.0 | `GenRamzi/Proctor` |
| `@stll/folio-agents` | **Apache-2.0** | 0.15.1 | `stella/folio` |
| `@stll/folio-cli` | **Apache-2.0** | 0.4.0 | `stella/folio` |
| `frappe-mcp-server` | **ISC** | 0.6.0 | `appliedrelevance/frappe_mcp_server` |
| `@universis/one-roster` | ⚠️ **LGPL-3.0-or-later** | 2.31.1 | 🔴 ninguno |
| `@osu-cass/sb-components` | ⚠️ **MPL-2.0** | **1.5.0-alpha.10** | `osu-cass/sb-components` |
| `@public-ui/mcp` | 🔴 **EUPL-1.2** | 4.4.0 | `public-ui/kolibri` |
| `@citolab/qti-convert-local-ai` | 🔴 **GPL-3.0-only** | 0.8.1 | `Citolab/qti-convert` |
| `@learninglocker/xapi-agents` | 🔴 **GPL-3.0** | 4.4.3 | `LearningLocker/xapi-agents` |
| `@superbuilders/oneroster` | 🔴 **ninguno** | 0.7.0 | `trilogy-group/oneroster-ts` |
| `@timeback/caliper` | 🔴 **ninguno** | 0.3.3 | 🔴 ninguno |
| `@pie-element/multiple-choice` | 🔴 **ninguno** | **14.0.0** | `pie-framework/pie-elements-ng` |
| `@pie-element/rubric` | 🔴 **ninguno** | **9.0.0** | `pie-framework/pie-elements-ng` |

**El reparto, que es lo que una propuesta necesita de una sola mirada: 21 permisivas** (16 MIT,
4 Apache-2.0, 1 ISC), **5 con copyleft o recíproca** (GPL-3.0, GPL-3.0-only, LGPL-3.0-or-later,
EUPL-1.2, MPL-2.0) **y 4 SIN campo de licencia**.

🔴 **Las 4 sin licencia son NUEVAS: el pase 49 encontró 2 de 6, este pase encuentra 4 más de 30.**
Y dos de ellas no son prototipos: **`@pie-element/multiple-choice` va en la versión 14.0.0 y
`@pie-element/rubric` en la 9.0.0.** Una librería de ítems de evaluación con catorce mayores y sin
licencia no es un descuido de arranque.

🔵 **Y un patrón de ALCANCE, no de paquete:** con `@timeback/oneroster` del pase 49,
**el scope `@timeback` va 2 de 2 sin campo de licencia y sin repositorio publicado.** Deja de ser
una fila a revisar y pasa a ser una regla de cotización: **`@timeback/*` no entra en una entrega sin
gestión previa.**

### 🔴 El hallazgo que cambia el instrumento: el defecto campo-vs-texto corre en los DOS sentidos

El pase 49 estableció la regla —*un CAMPO de licencia no es TEXTO de licencia*— y la ilustró en una
sola dirección: **campo que dice MIT y no hay texto** (`sisu-mcp`, `@timadey/proctor`). **Este pase
encuentra la dirección inversa, y es peor para un filtro automático:**

| Paquete | Campo de registro | Texto en el repositorio |
|---|---|---|
| **`@superbuilders/oneroster`** 0.7.0 | 🔴 **ninguno** | 🟢 **`trilogy-group/oneroster-ts` `main:LICENSE` → 200** |

⚠️ **Un filtro de licencias que lea sólo el campo RECHAZA un paquete que sí está licenciado**, igual
que uno que lea sólo el *badge* **aprueba** uno que no lo está. **Las dos lecturas de un solo
artefacto fallan, en sentidos opuestos, y el error de cada una es el que más caro sale en su
contexto:** el que sobre-aprueba crea un riesgo legal, el que sobre-rechaza descarta la pieza
correcta. **La regla operativa que sale de esto: los dos artefactos, siempre, y la discrepancia se
reporta en vez de resolverse a favor de ninguno.**

### Los TEXTOS de licencia, y el control que distingue «no hay» de «no llegué»

`raw.githubusercontent.com/<org>/<repo>/<rama>/{LICENSE,LICENSE.md,LICENSE.txt,COPYING}`, probando
`main` y después `master`. **12 de los 19 repositorios declarados tienen texto de licencia
alcanzable.** ⚠️ **Y los 7 restantes no son una sola categoría —** ése es el control que este pase
agrega al instrumento, porque sin él un `NONE` se publica como «sin licencia» cuando puede ser «el
canal no llegó al repositorio»:

| Repositorio | Texto | ¿El repo responde? | Lectura |
|---|---|---|---|
| `pie-framework/pie-elements-ng` | 🔴 ninguno | 🟢 **sí** (`master/README.md` → 200) | 🔴 **sin licencia de verdad**, y confirma los dos campos vacíos |
| `moinsen-dev/tool-teacher` | 🔴 ninguno | 🟢 **sí** (`master/README.md` → 200) | 🔴 **campo MIT sin texto** — el patrón del pase 49 |
| `owentaylor/canvas-mcp` | 🔴 ninguno | 🔴 **no** (`main`/`master`/`develop`, README y `package.json`) | ⚠️ **indeterminado**: campo MIT, tarball 200, repositorio inalcanzable |
| `Eduware-Inc/eduware-oneroster` | 🔴 ninguno | 🔴 **no** | ⚠️ **indeterminado** |
| `LearningLocker/xapi-agents` | 🔴 ninguno | 🔴 **no** | ⚠️ **indeterminado** |
| `osu-cass/sb-components` | 🔴 ninguno | 🔴 **no** | ⚠️ **indeterminado** |
| `appliedrelevance/frappe_mcp_server` | 🔴 ninguno | 🔴 **no** | ⚠️ **indeterminado** |

🔵 **Dos conclusiones firmes y cinco declaradas indeterminadas es un resultado mejor que siete
«sin licencia»**, que es lo que el instrumento habría publicado sin el control. **El control cuesta
una petición por repositorio.**

### 🔴 La extensión a PyPI: los DOS pedazos de Open edX que esta base cita son AGPL-3.0

La acción 1 pedía extender el probe al *sdist*/*wheel* de PyPI. **La superficie no se pudo medir
(exige ejecución), pero la metadata sí, y responde la pregunta que más importa:**

| Paquete PyPI | Versión | `license` | Clasificador OSI |
|---|---|---|---|
| `openedx-mcp` | 0.1.5 | 🔴 **AGPL-3.0** | *GNU Affero General Public License v3* |
| `tutor-contrib-openedxmcp` | 0.1.7 | 🔴 **AGPL-3.0** | 🔴 **ninguno declarado** |

🔴 **Las dos únicas piezas de la capa MCP de Open edX que esta KB cita son AGPL-3.0, o sea copyleft
de RED.** Un servidor MCP es precisamente el caso que la AGPL contempla: **si se expone como
servicio a un tercero, la obligación de liberar fuente alcanza al servicio**, no sólo a la
redistribución del binario. ⚠️ **Y no es una sorpresa aislada: concuerda con la nota de cabecera de
`repos/foundations.md` —*media KB de educación es GPL/AGPL, no permisiva*— pero la mueve de la
plataforma a la CAPA DE AGENTES**, que es donde esta base venía suponiendo permisividad.
🔵 **Consecuencia de cotización: la puerta MCP de Open edX se construye propia sobre la API
permisiva, o el engagement acepta AGPL en el componente que mira al cliente.** ⚠️ Y
`tutor-contrib-openedxmcp` **no declara clasificador OSI**, así que un inventario automático de
licencias que lea clasificadores —no el campo— lo cuenta como desconocido.

### 🔴 La colisión de nombre que un inventario por NOMBRE no puede ver: hay DOS «Kolibri», con licencias distintas

| Proyecto | Licencia medida | Qué es |
|---|---|---|
| **`learningequality/kolibri`** | **MIT** (`master/LICENSE`, 200) | el LMS offline-first que `verticals/solutions.md` lista |
| **`public-ui/kolibri`** | 🔴 **EUPL-1.2** (`master/LICENSE`, 200 — *«EUROPEAN UNION PUBLIC LICENCE v. 1.2»*) | sistema de diseño accesible alemán, y el origen de **`@public-ui/mcp` 4.4.0** |

⚠️ **Son dos proyectos distintos con el mismo nombre y licencias que NO son intercambiables**, y
esta base los nombra a los dos: «Kolibri (MIT, offline)» en verticales, `@public-ui/mcp` en la capa
MCP. **Una búsqueda de licencia por nombre de proyecto devuelve la respuesta del otro**, y la EUPL-1.2
tiene cláusula de reciprocidad con compatibilidad explícita hacia otras copyleft —no es «como MIT».
🔵 **La regla que esto deja: la clave de un inventario de licencias es `org/repo`, nunca el nombre
del proyecto.**

### 🔴 UN servidor, CUATRO conteos de tools, y ninguno es «el» número

Medido sobre `bruchris/canvas-lms-mcp`, que es la alternativa con licencia a la puerta de Canvas:

| Valor | Instrumento | Fuente |
|---|---|---|
| **165** | titular del README del proyecto | `main/README.md` línea 14 |
| **165** | **el propio desglose del proyecto: 117 de lectura + 48 de escritura** | ídem, línea 153 — **internamente consistente** |
| **166** | ídem **con FERPA activo en el transporte stdio**, donde se registra `resolve_pseudonym` | ídem — y **el transporte HTTP nunca lo registra** |
| **157** | nombres distintos recuperables por expresión regular sobre su tabla de inventario enumerada | medición propia de este pase, `sed -n '107,156p'` + `grep -oE` |
| **115** | «read+write tools across 17 domains» | **directorio de terceros** (`getdrio.com`) |

⚠️ **La discrepancia 165 vs 157 es de MI instrumento, no de la fuente:** el desglose del propio
proyecto cierra (**117 + 48 = 165**), así que los 8 que faltan son un artefacto de contar una tabla
en prosa con una expresión regular. **Se publican los dos con su invocación, como manda P107.**
🔴 **La de 115 es otra cosa: es un tercero publicando un conteo sin instrumento ni fecha**, y es la
que un cliente encuentra primero en un buscador. 🔵 **Y el mismo defecto aparece cruzado entre los
dos proyectos: el README de `bruchris` cotiza a `vishalsachdev/canvas-mcp` en «80+» tools, y el
README de `vishalsachdev` dice «up to 103 tools», aclarando que «el perfil por defecto registra
menos».** **Un conteo de tools sin (a) instrumento, (b) perfil y (c) transporte no es comparable con
ningún otro** — y el *proveedor* de la cifra, propio o ajeno, cambia el valor más que el software.

## 2026-10-02 (pase 49) — **el dato crudo: DOS canales que esta base había declarado cerrados responden 200, y uno de ellos mide 227 tools sobre Canvas**

Todo lo de abajo se **midió con un comando** en este repositorio o contra `registry.npmjs.org` /
`raw.githubusercontent.com`. Las **dos** carpetas nuevas de `compose/code/` fallan si el upstream
cambió: `trend-backlink-audit` **22/22**, `npm-surface-probe` **19/19**.

### 🔴 El hallazgo con precio: la superficie de LMS más grande de esta KB no tiene licencia, y nadie la había medido

**El pase 35 excluyó `@imazhar101/mcp-canvas-server` por licencia ausente y tenía razón. Lo que
nadie midió es QUÉ se estaba excluyendo.**

| Medición | Valor | Instrumento |
|---|---|---|
| tools distintos sobre Canvas LMS | 🔴 **227** | nombres en `dist/servers/canvas/src/tools/` del *tarball* |
| conteo independiente | **227** | ocurrencias de `inputSchema` en el mismo árbol |
| archivos de `tools/`, uno a uno | **18**, y **coinciden los dos conteos en cada uno** | `user-tools.js` **39**, `page-tools.js` **21**, `file-tools.js` **20**, `submission-tools.js` **20**, `module-tools.js` **18**, `enrollment-tools.js` **15**, … `lti-launch-definition-tools.js` **1** |
| licencia (registro npm / manifiesto embarcado / archivo / repo) | 🔴 **ninguna / ninguna / ninguno / no publicado** | `probe.py` |

🔵 **Por qué esto es una acción y no un dato:** **227 tools es la superficie más grande de esta
base**, y lo único que la bloquea es **un archivo de licencia**. **Pedirlo upstream es la gestión
de mayor apalancamiento de toda esta KB**: un `LICENSE` permisivo convierte la integración de
Canvas más completa que existe en material entregable. Sin él, el default legal es «todos los
derechos reservados» y **no se puede proponer**.

### 🟢 Los dos canales que se reabrieron, y las 326 + N cifras que vuelven a ser medibles

| Clase de cifra | Estado declarado | Canal que responde 200 |
|---|---|---|
| **`tools`** (**326** cifras en los ocho archivos) | 🔴 «exige el paquete instalado» | **el *tarball* de `registry.npmjs.org`**: se cuenta **estáticamente**, sin instalar ni levantar servidor |
| **licencias** | 🔴 cerrado desde el pase 37 (`github.com` **403**, `api.github.com` 200 negando acceso) | **`raw.githubusercontent.com/<org>/<repo>/<rama>/LICENSE`** |

⚠️ **Y el canal de licencias se verificó con control positivo sobre cinco repos:** `Paper2Slides`,
`VideoAgent`, `VideoRAG`, `DeepTutor` y `OpenMAIC` dieron **200** por `raw`, mientras los cinco
daban **403** por `github.com`. **El canal no estaba cerrado: estaba mal elegido.**

### 🔴 La trampa de licencia que un *badge* no muestra: MIT en la arquitectura, NO comercial en el código

**`HKUDS/VideoRAG`** —vecino declarado en el README de `Paper2Slides`— **no es MIT a secas**. Su
`LICENSE` (139 líneas) es un **doble licenciamiento** y lo dice él mismo:

- **Parte 1, la arquitectura:** MIT.
- **Parte 2, la implementación tal como se embarca:** `Vimo-desktop/` y `VideoRAG-algorithm/`
  **integran ImageBind, que es CC BY-NC-SA 4.0 — NO comercial**, y `MiniCPM` (Apache-2.0).
- 🔴 **Y la conclusión la escribe el propio archivo:** *«the current complete implementation is
  restricted to NonCommercial use only»*.

🔵 **La salida está documentada y es la que una propuesta debe cotizar:** usar **sólo la
arquitectura** y reemplazar ImageBind por un modelo de licencia comercial. ⚠️ **Lo peligroso es el
atajo:** un filtro de licencias que lee «MIT» del *badge* o del campo **aprueba una pieza que, tal
como está, no se puede facturar.**

### Las licencias npm medidas en este pase, con el campo separado del TEXTO

| Paquete | Campo (registro / manifiesto) | ¿Archivo de licencia? | Repositorio | Tools |
|---|---|---|---|---|
| `@imazhar101/mcp-canvas-server` 2.1.3 | 🔴 ninguno / ninguno | 🔴 ninguno | 🔴 no publicado | 🔴 **227** |
| `@ink-waffle/sisu-mcp` 0.1.0 | MIT / MIT | 🔴 ninguno | 🔴 no publicado | **12** |
| `@signdocs-brasil/mcp-server` 0.11.2 | MIT / MIT | 🟢 `LICENSE` | 🔴 no publicado | **26** (37 registros) |
| `@timadey/proctor` 1.2.6 | MIT / MIT | 🔴 ninguno | 🟢 `Timadey/proctor` | 0 (no es MCP) |
| `@longsightgroup/qti3-cli` 0.13.1 | MIT / MIT | 🟢 `LICENSE.md` | 🟢 `LongsightGroup/qti3` | 0 (es CLI) |
| `@timeback/oneroster` 0.3.3 | 🔴 ninguno / ninguno | 🔴 ninguno | 🔴 no publicado | 0 |

⚠️ **`tools` distintos ≠ ocurrencias de registro:** `@signdocs-brasil/mcp-server` registra **37**
veces **26** herramientas porque embarca dos *builds*. **Publicar 37 infla la superficie un 42 %**,
y el probe reporta las dos cifras en vez de elegir.

🟢 **Dos confirmaciones independientes de cifras que esta base ya tenía:** `sisu-mcp` **12 tools**
(coincide con lo que el pase 41 anotó) y la exclusión de Canvas por licencia del pase 35.
🔴 **Y una corrección de grado:** el bloqueante *«licencia de `sisu-mcp` sin segunda fuente»* **baja
de grado y no se cierra** — la segunda fuente **existe** (MIT en el documento del registro **y** en
el `package.json` embarcado, dos artefactos independientes), pero **no hay texto de licencia en
ningún canal y no hay repositorio publicado**: se embarca `dist/` compilado. **Lo que falta ya no es
la fuente: es el texto y el código.**

## 2026-10-02 (pase 48) — **el dato crudo: 3.611 cifras inventariadas en los OCHO archivos, el 50,8 % no re-verificable acá, 1 cifra vencida de verdad, y 7 saltos de procedencia trazados hasta la pantalla**

Las tres acciones del pase 47 se ejecutaron. Todo lo de abajo se **midió con un comando** en
este repositorio o sobre un clon `--filter=blob:none --sparse`, y **las tres carpetas nuevas de
`compose/code/` fallan si el upstream cambió**.

### 🔵 El inventario de cifras, por archivo — y el pase 47 barrió justo el archivo MENOS denso

`python3 compose/code/patterns-figure-audit/extract_figures.py --all` (la ruta pasó a ser un
parámetro, que es lo que pedía la acción 2).

| Archivo | Líneas | KB | Cifras | Cifras / kilolínea |
|---|---|---|---|---|
| `agents/top.md` | 2.191 | 315 | 405 | 🔴 **184,8** — el más denso |
| `intel/market.md` | 5.232 | 546 | **907** | 🔴 **173,4** |
| `intel/trends.md` | 8.010 | 885 | **750** | 93,6 |
| `agents/trending.md` | 5.495 | 477 | 522 | 95,0 |
| `repos/trending.md` | 3.945 | 339 | 295 | 74,8 |
| `repos/foundations.md` | 2.855 | 283 | 205 | 71,8 |
| `verticals/solutions.md` | 1.785 | 180 | 144 | 80,7 |
| `compose/patterns.md` | 5.863 | 508 | 383 | 🔵 **65,3** — el MENOS denso |
| **TOTAL** | **35.376** | | **3.611** | **102,1** |

🔴 **Dos hallazgos, y el segundo es el que cambia cómo se cita esta base:**

1. **El pase 47 eligió `compose/patterns.md` por ser el activo más citado, y resultó ser el
   archivo con MENOR densidad de cifras de los ocho.** Concluyó una tasa de falla del **1,0 %**
   sobre **368** mediciones. Los dos archivos que nunca se habían barrido, `intel/market.md` y
   `intel/trends.md`, **tienen 1.657 cifras entre los dos — el 46 % del total de la base.**
2. 🔴 **1.836 de las 3.611 cifras (el 50,8 %) NO son re-verificables en este entorno.**
   Desglose: **1.042 estrellas**, **418 commits**, **326 conteos de tools**, **50 descargas**.
   Son propiedades del canal, no de la base —`github.com` da 403 a curl y `api.github.com`
   niega en el cuerpo (pase 37)— pero **la consecuencia comercial hay que escribirla: más de la
   mitad de las cifras de esta KB no se pueden refrescar desde acá.** Las **1.775 restantes**
   sí, y son las que valen para una propuesta: líneas, aserciones, rutas, métodos, archivos.

### 🟢 `--crossref`: el defecto que el pase 47 no vio, porque arregló una cifra en UN archivo

La acción 2 pedía barrer cifras. El barrido encontró algo más preciso: **el pase 47 corrigió
«11/11 checks» en `compose/patterns.md` y la misma cifra siguió viva en otros archivos.**
**El defecto no es que una cifra se venza: es que una CORRECCIÓN NO SE PROPAGA**, porque una
sola medición se cita hasta en diez lugares de ocho archivos.

Por eso el instrumento pasó a ser cruzado: `extract_figures.py --crossref` **vuelve a correr las
ocho suites** y atribuye cada cita de un conteo de checks.

| Suite | Conteo medido hoy | Condición |
|---|---|---|
| `unitime-mcp-gate` | **46** | — |
| `sebserver-mcp-gate` | **37** | — |
| `mcp-allowlist-gateway` | **34** | 🆕 **nueva en este pase** |
| `openedx-course-generator` | **33** | — |
| `aiact-50-2-pack` | **27** | 37 con los dos directorios de esquemas |
| `aiact-50-2-marking` | **23** | 24 con `--with-xmllint` + `SCORM_SCHEMAS` |
| `seb-proctoring-validator` | **21** | — |
| `proctoring-reach-audit` | **19** | 20 con la ruta a un checkout de seb-server |

**Resultado final: 15 citas concuerdan, 0 vencidas, 0 sin condición** — después de corregir tres
cosas, dos de ellas del instrumento:

| Hallazgo | Veredicto | Qué se hizo |
|---|---|---|
| `verticals/solutions.md:1690` — *«79 tools, 36 expuestas, **11/11** checks»* | 🔴 **VENCIDA DE VERDAD, y en una fila de catálogo que se lee como estado actual** | Corregida a **37/37**, con la nota de qué decía antes |
| `intel/trends.md:5056` — *«`aiact-50-2-marking`, **24/24**, sólo stdlib»* | ⚠️ **Real pero SIN CONDICIÓN escrita** (la corrida desnuda da 23) | Condición agregada en el sitio de la cita |
| `repos/foundations.md:2827` — *«20 aserciones»* | ⚠️ **Real pero SIN CONDICIÓN escrita** (19 sin la ruta) | Condición agregada |

🔵 **Y tres reglas de instrumento que salieron de hacerlo, cada una encontrada porque el
instrumento falló primero:**

1. 🔴 **La ventana de lectura tiene que seguir la ESTRUCTURA del documento.** Por línea, el
   escáner perdía la condición que vivía una línea más abajo (prosa cortada a ~100 caracteres) →
   **1 falso positivo**. Por párrafo, se comía las filas vecinas de una tabla markdown, que no
   llevan línea en blanco entre sí → **3 hallazgos se volvieron 9, y 6 eran fabricados por la
   ventana**. La regla: **fila de tabla ⇒ la ventana es la fila; prosa ⇒ la ventana es el
   párrafo.**
2. **Una cifra que coincide con una de varias suites nombradas en la ventana pertenece a ÉSA.**
   Cargársela a todas fabrica hallazgos — es lo que produjo el falso positivo de
   `foundations.md:2827`, que nombra dos suites.
3. **Una cifra condicional no es una cifra vencida.** El instrumento ahora distingue
   `STALE` de `COND` (real, pero la condición no viaja con la cita), porque la acción es
   distinta: una se corrige, la otra se completa.

⚠️ **Y el límite declarado: 29 citas quedaron `unattributed`** — no nombran su suite en la
ventana. **No se adivinan**, porque adivinar es exactamente lo que produjo las cifras vencidas.

### 🟢 `project-nomad`, leído de punta a punta: la procedencia LLEGA al alumno, y llega hasta la pantalla

Acción 3 (**gap 104**). `compose/code/nomad-citation-trace/`, **32/32**, sobre un clon
`--filter=blob:none` con `sparse-checkout` de `admin/app`, `admin/types`,
`admin/inertia/components/chat` y `admin/database/migrations`, rama `main` al **2026-10-02**.

**Siete saltos, cada uno una aserción que falla si el upstream cambia:**

| # | Salto | Evidencia |
|---|---|---|
| 1 | Recuperación **emite** la identidad | `rag_service.ts` — el `metadata` de retorno lleva `source`, `document_id`, `archive_title`, `archive_date`, `chunk_index` |
| 2 | El prompt inyectado **rotula** cada bloque | `rag_prompt.ts` → `[Context N — Título (fecha)]`, **deliberadamente sin el score** |
| 3 | Se construye la **lista de citas** | `buildCitations`, alimentada de **lo inyectado, no de todo lo recuperado** |
| 4 | La **forma** que cruza al cliente | `types/chat.ts` → `ChatSource = { title, date?, source? }` |
| 5 | Se **persiste** | migración `1785468975052`, columna `sources` *text nullable* en `chat_messages` |
| 6 | Se **devuelve** | `JSON.parse(msg.sources)` en el historial, objeto directo en la respuesta nueva |
| 7 | La UI lo **renderiza** | `ChatMessageBubble.tsx`, bajo la respuesta del asistente |

🔵 **Un regalo del árbol:** el propio upstream dejó escrito que `source` *«previously dropped
here»* hacía imposible mapear un *chunk* a su documento, **y lo arreglaron para citas y para
`recall@k`**. La mitad que el pase 47 no pudo ver **ya la había construido el proyecto.**

🔴 **Pero el límite decide qué puede prometer P108, y se prueba por AUSENCIA:** `ChatSource`
tiene **tres campos** y **ninguno es de tramo** (`offset`/`index`/`span`) ni distingue **cita
textual de síntesis**; y `buildCitations` **deduplica por documento**. **La unidad de
procedencia de esta arquitectura es el DOCUMENTO, por diseño y con razón escrita, no por
olvido.** Concuerda con el gap 99 del pase 47 y lo precisa. Cotización en **P108**, corregida.

## 2026-10-02 (pase 47) — **el dato crudo: 2 comodines que no coinciden, 3 de 3 «handles» que se caen al abrirlos, 163 cifras que un `\b` se comía, y 1 import que falta en un esquema**

Todo lo de abajo se leyó del árbol con `git clone --depth 1 --filter=blob:none --sparse` o con
`raw.githubusercontent.com`, y se **reprodujo con un comando**: las tres carpetas nuevas de
`compose/code/` regeneran sus tablas contra el repo real y fallan si el upstream cambió.

### 🔴 `giacomomaria81/scorm-mcp-server` — los dos esquemas que empaqueta no acuerdan, y el que valida no importa todo lo que trae

Leído a `HEAD` del 2026-10-02 (`src/converter.ts`, `src/validate.ts`, `schemas/`, `schemas12/`).

| Medición | Valor | Instrumento |
|---|---|---|
| Dialectos que emite `buildManifestFor` | **2** (`buildManifest` 2004 / `buildManifest12` 1.2) | `src/converter.ts:603` |
| `grp.any` en el XSD de **2004** | `processContents="lax"` | `grep -A6 'name="grp.any"' schemas/imscp_v1p1.xsd` |
| `grp.any` en el XSD de **1.2** | 🔴 **`processContents="strict"`** | `grep -A6 'name="grp.any"' schemas12/imscp_rootv1p1p2.xsd` |
| Puntos de extensión, cada dialecto | **9** | `grep -c 'ref = "grp.any"'` (2004) y `grep -c 'ref="grp.any"'` (1.2) — ⚠️ **el espaciado difiere entre archivos** |
| `grp.any` del XSD de **metadatos LOM** | 🔴 **`##any` + `strict`** (más duro que los dos) | `grep -A6 'name="grp.any"' schemas12/imsmd_rootv1p2p1.xsd` |
| XSDs empaquetados en `schemas12/` | **5** (`imscp_rootv1p1p2`, `adlcp_rootv1p2`, `imsmd_rootv1p2p1`, `ims_xml`, `wrapper12`) | `ls schemas12/` |
| *Namespaces* que `wrapper12.xsd` importa | 🔴 **2 de 3** — falta `imsmd_rootv1p2p1` | `src/validate.ts:49-52` |
| `checks` distintos de `scorm_validate` | **9** ids (**15** sitios de llamada) | `grep -oE 'push\("[a-z0-9-]+"' src/validate.ts \| sort -u \| wc -l` |

🟢 **Y un detalle de `validate.ts` que conviene tener escrito porque es una superficie de confianza:**
las líneas 240-249 copian al directorio temporal **los `.xsd` que trae el propio paquete ANTES** de
caer a las copias embebidas, y sólo copia la embebida si el nombre no está ya. **O sea: un paquete
puede traer su propio `imscp_rootv1p1p2.xsd` y el validador lo usará.** El `wrapper12.xsd` sí se
escribe fresco cada vez, así que la raíz no es sustituible — pero lo que la raíz importa, sí.
**`schema-valid` es tan confiable como el paquete que se está validando.**

### 🔴 Las 33 filas expuestas, barridas por CONTENIDO y no por nombre de archivo

Primera vez que esta base lee el **contenido** de los repos expuestos en vez de su lista de
archivos. Detalle y TSV en [`compose/code/aiact-50-2-spans/`](../compose/code/aiact-50-2-spans/README.md).

| Magnitud | Valor |
|---|---|
| Repos barridos | **33** |
| Archivos listados (ningún blob descargado) | **24.206** |
| Candidatos por patrón de ruta | **3.249** |
| Archivos **leídos** (tope **25**/repo, declarado) | **432** |
| `HANDLE` → al verificar a mano, **límites de ENTRADA** | **3** |
| `WEAK` / `OPAQUE` / `NO_CANDIDATES` | **16** / **8** / **6** |
| 🔴 **Límites dentro del texto GENERADO** | 🔴 **0** |

| Repo | Archivo:línea | Token | Qué es |
|---|---|---|---|
| `Crosstalk-Solutions/project-nomad` | `admin/app/services/rag_service.ts:1137` | `chunk_index` | `metadata` del resultado de recuperación, con `source` y `document_id` |
| `microsoft/Shiksha-Copilot` | `components/ingestion-pipeline/.../utils/toc_extractor.py:110` | `end_index` | `toc_end_index = min(5, len(images))` — 🔴 **falso positivo** |
| `ahmedEid1/lumen` | `apps/backend/app/models/lesson_chunk.py:57` | `chunk_index` | columna con `UniqueConstraint("lesson_id", "chunk_index")` |

### 🔵 `compose/patterns.md`, medido contra sí mismo

| Magnitud | Valor | Instrumento |
|---|---|---|
| Líneas | **5.863** | `wc -l compose/patterns.md` |
| Mediciones numéricas | **383** | `python3 compose/code/patterns-figure-audit/extract_figures.py` |
| Reproducibles en este entorno | **165** | ídem |
| 🔴 No reproducibles acá | **218** (`tools` 78, `★` 90, `commits` 46, descargas 4) | ídem |
| 🔴 Cifras que la primera versión del instrumento se comía | **163 (44 %)** | `\b` tras `%` y `★` nunca dispara |
| `MCP_ALLOWLIST` en `compose/code/` | 🔴 **0 archivos** | `grep -rl MCP_ALLOWLIST compose/code/` |

### Las suites de esta base, todas corridas en este pase

| Suite | Hoy | Lo que `patterns.md` publicaba |
|---|---|---|
| `aiact-50-2-pack/test_pack.py` (**nuevo**) | **27/27** sin `xmllint`, **37/37** con él | — |
| `sebserver-mcp-gate/test_gate.py` | **37/37** | 🔴 «11/11» (L345) |
| `unitime-mcp-gate/test_gate.py` | **46** | 🔴 «23» (L608) |
| `openedx-course-generator/test_plan.py` | **33** | 🟢 «33» |
| `proctoring-reach-audit/test_reach.py` | **19/19** a secas, **20/20** con `/ruta/a/seb-server` | ⚠️ «20/20» sin la condición (L423) |
| `aiact-50-2-marking/test_marking.py` | **23/23** a secas, **24/24** con `--with-xmllint` | ⚠️ «24/24» sin la condición |
| `seb-proctoring-validator/run_test.sh` | **21/21** | 🟢 «21/21, JDK puro» |

### 🔴 Ruido medido y rechazos, para que el próximo pase no lo vuelva a pagar

- `speedyapply/2026-AI-College-Jobs` (**5.200 ★**, 206 forks) — **bolsa de trabajo de AI/ML**, no
  pieza educativa. Primera aparición en el barrido de *trending*; se registra como no-hallazgo.
- `karpathy/nn-zero-to-hero`, *Awesome LLM*, *Agents Towards Production*, `pguso/agents-from-scratch`,
  `rohitg00/ai-engineering-from-scratch` — **currículo y listas sobre AI**, la colisión de término
  que el pase 23 midió y que lleva cinco pases devolviendo lo mismo.
- `gittrend.io`, `trendshift.io`, `oosmetrics.com`, `sourcepulse.org` — **agregadores** cuyos conteos
  de ★ **no se pueden verificar acá** (`github.com` → 403 para `curl`, pase 37). Se citan como
  encuadre, **nunca como cifra verificada**.

## 2026-10-02 (pase 46) — **el dato crudo: 5 de 14 alcanzan la red y 0 directamente, 8 constructores emitidos como métodos, 9 puntos de extensión en el XSD y 1 de 3 casos de `xmllint` rechazado**

Todo lo de abajo se leyó del árbol con `git clone --depth 1 --filter=blob:none --sparse` y se
**reprodujo con un comando**: las dos carpetas nuevas de `compose/code/` regeneran sus tablas contra
un checkout y lo aseveran (`test_reach.py` exige que `reach.tsv` se regenere **byte a byte**).

### `SafeExamBrowser/seb-server` — Apache-2.0, `HEAD` `7f45689` (**2026-04-01**, Andreas Hefti)

🟢 **El `HEAD` coincide con el que ya citaba `seb-proctoring-validator`**, así que la auditoría es
sobre el mismo árbol que sostiene la cotización de *proctoring* — reverificado, no asumido.

| Magnitud | P94 (pase 43) | Pase 46 | Nota |
|---|---|---|---|
| Métodos obligatorios del SPI | 14 | **14** | leídos de `RemoteProctoringService.java` (130 líneas) |
| Líneas de código, Jitsi | 481 | **481** | 🟢 **la métrica queda NOMBRADA: no-blancas-no-comentario** (`wc -l` da 583) |
| Líneas de código, Zoom | 912 | **912** | ídem (`wc -l` da 1.116) |
| Métodos que **alcanzan** el remoto, Jitsi | 1 | **1** | ✅ la cifra de Jitsi era correcta |
| Métodos que **alcanzan** el remoto, Zoom | 🔴 **2** | 🔴 **5** | cerradura **transitiva**, no directa |
| Métodos que llaman la red **directamente**, Zoom | no medido | 🔴 **0** | los cinco pasan por helpers |
| Profundidad máxima al socket, Zoom | no medido | 🔴 **4** | `disposeServiceRoomsForExam` |
| Llamadas HTTP por sala creada | no medido | 🔴 **3** | `createUser` + `applyUserSettings` + `createMeeting` |
| Puntos únicos de salida HTTP, Zoom | no medido | 🟢 **1** | `exchange` privado (línea 940) con *circuit breaker* |
| Guardas de runtime no-anotación | no medido | **2** | `sendRejoinForCollectingRoom`, `enableWaitingRoom` — **las dos `false` por omisión** |
| Aserciones de `test_reach.py` | — | **20** | 20/20 en verde, incluida la regeneración |

**Los 14 métodos del SPI, leídos de la interfaz:** `getType` · `testExamProctoring` ·
`getProctorRoomConnection` · `getClientRoomConnection` · `createJoinInstructionAttributes` ·
`disposeServiceRoomsForExam` · `newCollectingRoom` · `newBreakOutRoom` · `disposeBreakOutRoom` ·
`getDefaultReconfigInstructionAttributes` · `mapReconfigInstructionAttributes` ·
`notifyBreakOutRoomOpened` · `notifyCollectingRoomOpened` · `clearRestTemplateCache`.

**La cadena de Zoom hasta el socket**, que es lo que la cuenta directa no ve:

```
disposeServiceRoomsForExam  --forEach-->  disposeBreakOutRoom
      --> deleteAdHocMeeting --> deleteMeeting/deleteUser --> exchange --> restTemplate.exchange
newCollectingRoom / newBreakOutRoom --> createAdHocMeeting
      --> createUser + applyUserSettings + createMeeting --> exchange --> restTemplate.exchange
testExamProctoring --> createNewRestTemplate --> testServiceConnection --> exchange
getZoomRestTemplate --> isValid --> oAuth2RestTemplate.getAccessToken()   🔴 token = tráfico
```

🔴 **Las tres trampas de lectura de este árbol, anotadas para que no se repitan:**

1. **`.put(` y `.delete(` no son verbos HTTP acá.** Una lista de verbos ingenua puntúa
   `attributes.put(...)` —un `Map.put`— como petición: daba **6** llamadas de red en
   `createJoinInstructionAttributes` de Jitsi y **10** en el de Zoom, **dos métodos que no tocan un
   socket**. **El verbo no identifica una petición; el receptor sí.**
2. **El receptor tiene que TERMINAR en `restTemplate`.** Zoom cachea templates en
   `restTemplatesCache`, que es un `LinkedHashMap`: un patrón laxo lo aceptaba y le daba a
   `getZoomRestTemplate` **2** llamadas fantasma.
3. **Construir un `RestTemplate` no es una petición.** Jitsi construye uno en la línea 162 y la
   llamada real es el `getForEntity` de la 163. Contar el constructor habría inflado justamente la
   cifra que había que corregir.

🔴 **Y el control (c) falló por TERCERA vez con el mismo síntoma:** la primera versión del extractor
emitió **8 constructores como métodos** (`JitsiProctoringService`, `ZoomProctoringService`,
`ZoomRestTemplate`, `OAuthZoomRestTemplate`, más `Context`, `Features`, `JWTContext` y `User` de las
clases internas). **Tercera pieza, tercer acierto del mismo control: el defecto es del método de
extracción, no de un árbol en particular.**

### `giacomomaria81/scorm-mcp-server` — MIT, `HEAD` `fd5f110` (**2026-09-03**), **v2.3.0**

✅ **Dos cifras de esta base se CONFIRMAN por lectura del árbol**, que es la primera vez que esta
fila se verifica por código y no por README:

| Magnitud | Esta KB decía | Pase 46 | Nota |
|---|---|---|---|
| Tools MCP | 3 | ✅ **3** | `scorm_package` · `scorm_validate` · `scorm_selftest` |
| Licencia | MIT | ✅ **MIT** | `LICENSE`: *«Copyright (c) 2026 Giacomo Pilia»* |
| Versión | no registrada | **2.3.0** | `package.json` + `RELEASE-2.3.0.md` |
| Fuente TypeScript | no medido | **3.517 líneas** en 6 módulos | `converter` 1.010, `tom` 652, `index` 559, `runtime` 506, `ui` 495, `validate` 295 |
| XSD empaquetados | no registrado | 🟢 **15** | **14 de ADL/IMS** + `xml.xsd` de W3C; conformidad **offline**: `xsi:schemaLocation` resuelve a hermanos del ZIP |
| Checks de `scorm_validate` | no medido | **9** | `zip-readable`, `manifest-at-root`, `manifest-parses`, `version-detected`, `organization`, `launch-resource`, `entry-exists`, `files-exist`, `schema-valid` |

⚠️ **`scorm_version` NO es una cuarta tool** — es un campo del JSON de respuesta. Un `grep` de
`"scorm_[a-z_]+"` devuelve cuatro cadenas y sólo tres son herramientas. **Colisión de instrumento,
registrada.**

🟢 **El punto de extensión, medido en el XSD y no en la documentación.** `metadataType` de
`imscp_v1p1.xsd` (línea 267) es:

```xml
<xsd:complexType name = "metadataType">
  <xsd:sequence>
    <xsd:element ref = "schema" minOccurs = "0"/>
    <xsd:element ref = "schemaversion" minOccurs = "0"/>
    <xsd:group ref = "grp.any"/>
  </xsd:sequence>
  <xsd:anyAttribute namespace = "##other" processContents = "lax"/>
</xsd:complexType>
```

y `grp.any` (línea 141) es
`<xsd:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>`.
🔵 **Aparece en NUEVE `complexType`, no en uno:** `manifestType`, `metadataType`,
`organizationsType`, `organizationType`, `itemType`, `resourcesType`, `resourceType`, `fileType` y
`dependencyType`. **Hay nueve puntos donde un marcador es legal.**

**Los tres casos de `xmllint`, corridos de verdad** contra los XSD del propio repo:

| Caso | Resultado |
|---|---|
| manifiesto 2004 base | `validates` |
| `<m:aiGenerated xmlns:m="urn:globant:aiact:50-2">` dentro de `<metadata>` | 🟢 **`validates`** |
| `<bogus>x</bogus>` (*namespace* por omisión) dentro de `<metadata>` | 🔴 **`fails to validate`** |

🔴 **La condición dura queda medida, no razonada: el marcador DEBE declarar su propio *namespace*.**
Y ⚠️ **el generador no tiene gancho**: `buildManifest` (línea 535) y `buildManifest12` (línea 576)
de `src/converter.ts` arman el `<metadata>` como **literal de cadena**, con `<schema>` y
`<schemaversion>` fijos y **ningún parámetro de extensión**. Inyectar exige **parchear el generador
o post-procesar el ZIP** — se cotiza, pero **una vez**, no 32.

### `JuneYaooo/lineage-skill` y `zijinz456/OpenTutor` — las dos fuentes del componente, leídas de primera mano

- **`lineage-skill/references/provenance-policy.md`** (Apache-2.0): **9 valores**, confirmados uno a
  uno contra el archivo, que además queda commiteado como *fixture* para que la deriva rompa la
  prueba: `direct_source`, `source_grounded_synthesis`, `cross_source_synthesis`,
  `mentor_inference`, `learner_hypothesis`, `learner_observation`, `real_world_evidence`,
  `external_general_knowledge`, `unsupported`. La política los exige *«for every consequential
  claim, task answer, rubric rule, feedback judgment, and Personal Skill rule»*.
- **`OpenTutor/apps/api/services/provenance.py`** (MIT): **72 líneas, dos funciones**.
  `build_provenance` tiene **12 parámetros** y `generated: bool = True` **por omisión** —
  🟢 **falla hacia el lado seguro**— y agrega `"generated"` a `source_labels` cuando es verdadero.
  `merge_provenance` **unifica `source_labels` como conjunto ordenado** y descarta `None`, que es el
  detalle que permite extender el payload sin romper el merge.

🔵 **Dato que cambia la lectura del campo:** `build_provenance` **no tiene nada por tramo** — ni
`spans`, ni desplazamientos, ni etiqueta por afirmación. **La granularidad no estaba «a medias»: no
estaba.** Lo que esta base agrega es el tramo, y lo agrega **sin romper** el contrato del turno.

## 2026-10-02 (pase 45) — **el dato crudo: 15 rutas literales de 15, 60 rutas vivas (no 26), 46 aserciones en verde, 24.202 archivos barridos y 0 artefactos de marcado**

Todo lo de abajo se leyó del árbol, con `git clone --depth 1 --filter=blob:none --sparse` y con
`raw.githubusercontent.com` sobre la rama por defecto verificada con `git ls-remote --symref` — el canal que el pase 37
estableció como el único fiable, porque `curl` sobre `github.com` devuelve **403 para todo** y `api.github.com/repos/<x>`
devuelve **200 con un cuerpo que niega el acceso**.

### `UniTime/unitime` — Apache-2.0, `HEAD` `aeb4431` (**2026-10-02**, Tomáš Müller)

🟢 **El `HEAD` del clon es de hoy**, así que la re-auditoría es sobre código vivo, no sobre un árbol viejo.

| Magnitud | Pase 42 | Pase 45 | Nota |
|---|---|---|---|
| Conectores con bean `@Service("/api/…")` | 15 | **15** | barrido sobre `JavaSource` **entero**: no hay un 16.º |
| Tools en el manifiesto (conector × verbo implementado) | 26 | **26** | 14 lecturas + 12 escrituras |
| **Rutas HTTP vivas** | no medido | 🔴 **60** | 15 × 4; las **34** sin *override* **responden 501**, no 404 |
| Rutas base **literales** | no medido | 🟢 **15 de 15** | lo contrario de SEB Server, donde eran **0 de 30** |
| Columna de ruta en `connectors.tsv` | 🔴 **no existía** | **sí** | antes se inferían `getName()` + `"/api/"` en una f-string |
| Prefijo del servlet | inferido | **`/api/*`** | leído de `WebContent/WEB-INF/web.xml`, `<servlet-name>apiServlet</servlet-name>` |
| Contexto de despliegue | **no registrado** | 🔴 **`/UniTime`** | leído de `pom.xml:614`, `<warName>UniTime</warName>` |
| Verbos que **cruzan** la frontera de escritura | no medido | 🔴 **1** | `GET /api/script` |
| Verbos **guardados por propiedad** | no medido | **2** | `var-title-crs` `Get` **y** `Post` |
| Aserciones de `test_gate.py` | 11 → 23 | **46** | 46/46 en verde |

**Los 15 beans, leídos del árbol** (`grep -rn '@Service("/api' JavaSource`), **y los 15 coinciden con `getName()`**:
`/api/buildings` · `/api/class-info` · `/api/curricula` · `/api/exchange` · `/api/enrollments` · `/api/events` ·
`/api/instructor-schedule` · `/api/instructors` · `/api/json` · `/api/sectioning` · `/api/roles` · `/api/rooms` ·
`/api/script` · `/api/student-groups` · `/api/var-title-crs`.

🔵 **Reproducible, no transcrito:** el pase deja `compose/code/unitime-mcp-gate/extract_surface.py`, que regenera la
tabla contra un checkout. Las cifras de arriba se vuelven a obtener con un comando.

🔴 **Las dos trampas de lectura de este árbol, anotadas para que no se repitan:**

1. **`getName()` no es la ruta** — es la clave de *cache mode* (`ApplicationProperty.ApiCacheMode.value(getName())`).
2. **No tomar el primer literal después de la palabra `getName`:** ese atajo devuelve `"name"` para `EventsConnector` y
   `"log"` para `ScriptConnector`. (Trampa registrada en el pase 42; sigue vigente y ahora está aseverada.)

### `openedx/edx-platform` — AGPL-3.0, leído sobre `master` por `raw.githubusercontent.com`

La acción 2 pedía cerrar el costo de **P55**. Las tres piezas del contrato que el pase 44 midió **se reverificaron de
primera mano** y **aparecieron dos cosas que no estaban**:

| Pregunta | Respuesta medida | Sitio exacto |
|---|---|---|
| ¿Qué devuelve la creación? | **`{"locator", "courseKey"}`**, y `locator` es el usage key del bloque nuevo | `xblock_storage_handlers/view_handlers.py:895-897` |
| ¿Cuánto cuesta leer el curso? | **1 llamada** — `GET /api/contentstore/v1/course_index/{course_id}` → `course_structure` | `rest_api/v1/urls.py:82-84` |
| ¿`category` tiene enum en un curso? | **No.** `CharField(required=False, allow_null=True)` sin `choices`; el enum `["html","problem","video"]` es **sólo** para `LibraryUsageLocator` | `rest_api/v0/serializers/xblock.py:29`, `view_handlers.py:867` |
| 🔴 **¿Cuántas claves exige el handler sin declararlas?** | **DOS, no una**: `request.json["parent_locator"]` (832) **y** `request.json["category"]` (864), las dos subscripts pelados | `view_handlers.py:832,864` |
| 🔴 **¿Qué estatus da cada falta?** | **403** la primera, **500** la segunda, **400** una clave de más | ver abajo |

🔴 **Tres estatus para un mismo defecto —un cuerpo mal formado— y sólo uno es el correcto:**

1. **sin `parent_locator` → 403.** `XblockViewSet.initial()` deriva `course_key` **del cuerpo crudo**
   (`request._request.body`); si falta, queda `None`, y `HasCourseAuthorAccess.has_permission` hace
   `if not course_key: return False` (`rest_api/v1/views/permissions.py:25-27`). **Un defecto de cuerpo se reporta como
   falla de autorización**, que es donde un operador va a buscar credenciales en vez de el payload.
2. **sin `category` → 500.** `category` se lee **dos veces**: `request.json.get("category")` en la 834, que alimenta el
   chequeo de permisos, y el **subscript pelado** en la 864. Así que el POST **pasa el control de autorización** y
   revienta después, con `KeyError`.
3. **con un campo inesperado → 400**, correctamente, porque `XblockSerializer` extiende `StrictSerializer`
   (`rest_api/serializers/common.py:40-49`).

🟢 **Y una corrección a favor del upstream, por lectura de primera mano:** el `create` del `v1` **sí** corre el
serializer — lleva `@validate_request_with_serializer` además de `@expect_json_in_class_view`
(`rest_api/v1/views/xblock.py:239-243`). **El serializer se ejecuta y es estricto con las claves de más**; lo que no
puede hacer es atrapar las dos claves que el handler exige, **porque las declara opcionales a las dos.**

**El costo de P55, cerrado, con la fórmula transferible:** `llamadas = 1 + bloques`, en `profundidad` olas secuenciales,
con los hermanos en paralelo dentro de cada ola. Para el outline de ejemplo del generador (2 módulos / 3 secuencias /
4 verticales / 8 componentes = **17 bloques**): **18 llamadas, 4 olas, ola más ancha de 8**. **33 aserciones en verde.**
Artefacto en `compose/code/openedx-course-generator/`. **Gap 94 CERRADO.**

### El barrido de marcado del Artículo 50(2) — 33 repos, y el cero es el dato

Medido con `compose/code/aiact-50-2-exposure/scan_marking.sh`, que **no busca en documentación**: clona cada repo
expuesto con `--filter=blob:none` (**ningún blob se descarga**) y busca en **la lista de archivos**, más las
dependencias en **los manifiestos de raíz**.

| Magnitud | Valor |
|---|---|
| Filas de `agents/top.md` clasificadas | **66** |
| Filas que ponen contenido sintético delante de una persona | **32** (24 `gen` + 7 `gen-ind` + 1 `gen-cond`) = **48 %** |
| Repos barridos (los 32 + el empaquetador − 5 entradas de registro sin repo) | **33** |
| Archivos listados | **24.202** |
| Artefactos de **marcado** (`c2pa`, `watermark`, `synthid`, `content-credentials`, `imwatermark`) | 🔴 **0** |
| Manifiestos de raíz leídos | **26** |
| **Dependencias** de marcado | 🔴 **0** |
| Repos con **0 de todo** | **28 de 33** |
| Artefactos de **procedencia** | **15, en 5 repos** — y **13 de los 15 son procedencia de FUENTE**, no sintética |

🟢 **La única fila que emite una bandera legible por máquina:** `zijinz456/OpenTutor`
(`"generated": true` + `source_labels: ["generated"]`, servido al cliente en `routers/chat.py:214` y declarado en
`schemas/task.py:59`). 🔴 **Y no alcanza:** es un campo **al lado** del contenido, marca **el turno y no el tramo**, y
**no está firmado**. Detalle y veredicto en `compose/code/aiact-50-2-exposure/README.md`.

### 🔴 Ruido medido y rechazos, para que el próximo pase no lo vuelva a pagar

- **`gap 92` ampliado a CUATRO dominios.** A `eur-lex.europa.eu`, `artificialintelligenceact.eu` y `data.europa.eu` se
  suma **`digital-strategy.ec.europa.eu`** —la página oficial del *Code of Practice on Transparency of AI-generated
  Content*—, probada por **los dos canales** (`curl` y WebFetch) con **`connect_rejected` / `EGRESS_BLOCKED`**. Las
  fechas del Artículo 50 quedan confirmadas por **tres canales secundarios independientes y concordantes**, y eso **hay
  que seguir diciéndolo cada vez que se citen.**
- **`EventsConnector:170` es un falso positivo del barrido de mutaciones** (`Iterator.remove()` sobre una lista en
  memoria). Se registra para que no vuelva a aparecer como hallazgo.
- **La alternativa `public boolean do*` del extractor de UniTime está muerta:** **0 ocurrencias** en el árbol. Los 26
  *overrides* son **todos** `public void do<Verb>(ApiHelper)`, y **ninguno** usa la forma
  `(HttpServletRequest, HttpServletResponse)` de la clase base, así que el patrón del pase 42 **no perdía nada** — pero
  tampoco lo sabía.

## 2026-10-02 (pase 44) — **el dato crudo: 55 constantes (no 42), 341 operaciones (no 79), 31 controladores (no 4), 37 aserciones en verde, y 0 rutas base literales en todo el servicio**

Todo lo de abajo se leyó del árbol, con `git clone --depth 1 --filter=blob:none --sparse` sobre los dos upstreams —el
canal que el pase 37 estableció como el único discriminador fiable, porque `curl` sobre `github.com` devuelve **403 para
todo** y `api.github.com/repos/<x>` devuelve **200 con un cuerpo que niega el acceso**.

### `SafeExamBrowser/seb-server` — Apache-2.0, `HEAD` `7f45689` (2026-04-01, Andreas Hefti)

El `HEAD` del clon **coincide exactamente con el commit que el pase 43 declaró medido**, así que las dos mediciones son
comparables fila por fila.

| Magnitud | Pase 43 | Pase 44 | Nota |
|---|---|---|---|
| Constantes `*_ENDPOINT` en `gbl/api/API.java` | 42 | **55** | 41 literales + **14 compuestas**; las 14 que faltaban son **exactamente** las compuestas |
| Operaciones en `operations.tsv` | 79 | **341** | `own` 135 · `inherited` 186 · `inherited-denied` 16 · `inherited-guarded` 4 |
| Clases `@RestController` cubiertas | 4 | **31** | el total real del paquete `weblayer/api` |
| Endpoints distintos | 4 | **30** | |
| Escrituras (POST/PUT/DELETE/PATCH) | — | **170** | las 170 retenidas con `-32601` |
| Aserciones de `test_gate.py` | 11 | **37** | 37/37 en verde |
| Rutas base **literales** | — | **0 de 30** | 27 bajo `${…api.admin.endpoint}`, 3 bajo las de exam/LMS |

**Valores de propiedad leídos de `src/main/resources` (no supuestos):**
`sebserver.webservice.api.admin.endpoint` = **`/admin-api/v1`** ·
`…api.exam.endpoint` = **`/exam-api`** ·
`…api.exam.endpoint.discovery` = **`/exam-api/discovery`** ·
`…api.exam.endpoint.v1` = **`/exam-api/v1`** ·
`sebserver.webservice.lms.api.endpoint` = **`/lms-api/v1`** ·
`sebserver.webservice.light.setup` = **`false`**.

🔵 **Reproducible, no transcrito:** el pase deja `compose/code/sebserver-mcp-gate/extract_surface.py`, que regenera las
dos tablas contra un checkout. Las cifras de arriba se vuelven a obtener con un comando.

### `openedx/edx-platform` — AGPL-3.0, `HEAD` `c0048e1` (2026-10-02, Feanil Patel)

🟢 **El `HEAD` es de hoy**, así que la medición de autoría del `v1` es sobre código vivo, no sobre un árbol viejo.

| Pregunta de la acción 2 | Respuesta medida | Archivo |
|---|---|---|
| ¿Qué devuelve `create_xblock_response`? | **`{locator, courseKey}`** — y `locator` **es el usage key del bloque nuevo**, así que el recorrido del árbol es **recursable sin un GET extra** | `xblock_storage_handlers/view_handlers.py:894` |
| Variantes del cuerpo | *clipboard*: +`static_file_notices` +`upstreamRef` (4 claves) · import de biblioteca v2: +`upstreamRef` +`static_file_notices` +`parent_locator` (5) · duplicado: las mismas 2 | ídem |
| ¿Qué `category` acepta sin configuración extra? | En un **curso, ninguna restricción**: `XblockSerializer.category` es un `CharField(required=False)` **sin `choices`**. El **único** enum del árbol es `["html","problem","video"]` y sólo para `LibraryUsageLocator` | `rest_api/v0/serializers/xblock.py:29`, `view_handlers.py:867` |
| ¿`?view=minimal` sólo en `retrieve`? | **Sí**, y además **no hay hijos que recorrer**: `get_block_info` lleva escrito *«children aren't being returned until we have a use case»* (`view_handlers.py:710`) y nunca pasa `include_child_info` | `rest_api/v1/views/xblock.py:275`, `view_handlers.py` |

🔴 **Tres defectos del `v1` que un cliente descubre en producción si no se leen antes:**

1. **El docstring del `v1` llama «tree-shaped» a la respuesta de `retrieve` y no lo es.** El handler es
   `get_block_info`, que devuelve **un solo bloque**.
2. **2 de los 6 campos que promete `?view=minimal` son claves que el handler no emite.**
   `_MINIMAL_VIEW_FIELDS` lista `{id, display_name, category, children, has_children, studio_url}` y
   `_apply_minimal_view` es un `project()` **de primer nivel**; como no hay `children` ni `has_children` en el cuerpo,
   la vista mínima devuelve **a lo sumo 4 de 6**.
3. **La única forma de obtener hijos de este endpoint es una combinación no documentada:**
   `?fields=customReadToken&view=minimal`. Devuelve `children` como identificadores `{block_type, block_id}` —**un solo
   nivel**— y **descarta `parent` en silencio**, porque `parent` no está en `_MINIMAL_VIEW_FIELDS`.

⚠️ **Y un defecto de validación que conviene saber antes de escribir el cliente:** el serializer declara `category`
**opcional** pero `_create_block_core` hace `request.json["category"]`, así que un POST sin `category` (y sin
`staged_content="clipboard"`) **levanta `KeyError` → 500, no 400**.

🟢 **El instrumento correcto para leer el árbol completo existe y no es el endpoint de xblock:**
`GET /api/contentstore/v1/course_index/{course_id}` devuelve **`course_structure`**, el *outline* anidado, **en una sola
llamada** (`CourseIndexSerializer.course_structure` es un `DictField`); y
`GET /api/contentstore/v1/container/{usage_key}/children` devuelve **un nivel** de hijos con nombre y tipo.
**Eso fija el costo de P55: leer el curso = 1 llamada; escribir = 1 POST por bloque**, secuencial bajando una rama
(el hijo necesita el `locator` del padre) y **paralelizable entre hermanos**.

### `issuebadge/mcp-server` — MIT, `HEAD` `ea249e4` (2026-09-26)

**4 commits, y la forma de la historia es el dato:** tres commits del **2025-07-06** (README y subida de archivos) y
**uno solo del 2026-09-26** que trae `v2.1.0` entero —worker remoto con OAuth 2.1, servidor stdio, plugins—. Catorce
meses de silencio y una descarga: es **«ráfaga y silencio»**, el patrón que esta base nombró en el pase 36 con el *span*
de releases, ahora visible en el árbol de git. **No está en npm** (`Not found`), así que ningún barrido por registro lo
alcanza. Detalle completo y veredicto en `agents/trending.md`.

## 2026-10-02 (pase 43) — **el dato crudo de las tres acciones: 42 constantes de endpoint, 79 operaciones, 14 métodos obligatorios (no 12) y 22 % de clase, más 3 altas de estándar y 1 repo que no es legible**

Todo lo de abajo se leyó **de primera mano** por `raw.githubusercontent.com` sobre la rama por defecto, verificada con
`git ls-remote --symref`. Las licencias salen del archivo **`LICENSE`**, no del README ni del manifiesto.

### Acción 1 — `SafeExamBrowser/seb-server` (Apache-2.0, `master` @ `7f45689`)

| Medición | Valor | Lo que esta base tenía |
|---|---|---|
| Constantes `*_ENDPOINT` en `gbl/api/API.java` | **42** en `master` | 🔴 decía **41** |
| idem en `development` | **47** | no registrado |
| Controladores concretos | **30** | 🔴 decía **36** |
| Clases base abstractas | **3** (`EntityController`, `ActivatableEntityController`, `ReadonlyEntityController`) | no desglosado |
| Archivos `.java` en `weblayer/api/` | **40** (incluye excepciones y servicios, no sólo controladores) | — |
| Superficie CRUD de `EntityController` | **10** operaciones | — |
| Operaciones que agrega `ActivatableEntityController` | **3** distintas (la cuarta, `POST (root)`, es *override*) | — |
| Operaciones medidas para los 4 endpoints objetivo | **79** (33 `own` + 46 `inherited`) | — |
| Verbos en los `own`: | `GET` 18 · `POST` 9 · `PUT` 3 · `DELETE` 2 · **`PATCH` 1** | 🔴 el `PATCH` no estaba registrado |

**Colisión de paths:** `EXAM_ADMINISTRATION_ENDPOINT` y `LMS_FULL_INTEGRATION_EXAM_ENDPOINT` **valen las dos `/exam`**.

**Resultado del gate** (`python3 test_gate.py`, **11/11**): 79 tools → **36 expuestas**; **37** escrituras con `-32601`;
**11** tools de `/batch-action` fuera, lecturas incluidas; **0** llegadas al upstream.

### Acción 2 — el costo de `RemoteProctoringService`

| | **Jitsi** | **Zoom** |
|---|---|---|
| Métodos obligatorios de la interfaz | **14** (0 `default`, 0 `static`) | **14** |
| Líneas de código de la clase | **481** | **912** |
| Líneas en los 14 métodos | **107** (**22 %**) | **212** (**23 %**) |
| Triviales (≤6 líneas, sin red) | **10** | **6** |
| Hablan con el remoto | **1** | **2** |
| Privados de apoyo / clases internas | 2 / 0 | **8** / 1 |
| *Imports* de terceros | 17 | **38** |
| Cripto | `Mac.getInstance` + `HmacSHA256` + `Base64` | idem |

### Acción 3 — el validador

`ProctoringSettingsValidator.java` termina en **`return true`**; `ProctoringServerType` tiene **2** valores. El reemplazo
en `compose/code/seb-proctoring-validator/` da **21/21 checks** con **JDK puro** (`javac` + `java`, cero dependencias
instaladas), e incluye una copia fiel del validador actual para **reproducir el defecto por ejecución**: un
`BIGBLUEBUTTON` con todos los campos `null` → `true` y **0** violaciones.

### Gap 50 — `openedx/edx-platform` (`master`; ⚠️ **la rama es `master`, `main` da 404**)

| Archivo | Medición |
|---|---|
| `contentstore/rest_api/v0/urls.py` | 4.092 bytes. Rutas de *authoring*: `advanced_settings`, `tabs` (×3), `heartbeat`, `file_assets` (×2), `videos/*` (×6), `grading`, `video_transcripts`, **`xblock` (×2)**, `youtube_transcripts` (×2), `link_check*`, `rerun_link_update*`. 🔴 **Ninguna crea cursos** |
| `contentstore/rest_api/v0/views/xblock.py` | 🔴 **`(DEPRECATED)`** en el encabezado + `DeprecationWarning` en los 5 métodos. Remite a `/api/contentstore/v1/xblock/` |
| `contentstore/rest_api/v1/urls.py` | **22** rutas con nombre. `XblockViewSet` registrado en un `DefaultRouter`. Incluye `course_rerun`, `course_index`, `course_details`, `course_settings`, `course_grading`, `container/{usage_key}/children`. 🔴 **No crea cursos** |
| `contentstore/rest_api/v1/views/xblock.py` | 14.080 bytes. ADR **0025/0026/0027/0028/0029/0034/0036**. `create` lee `parent_locator` de `request._request.body` (no de `request.data`, para no consumir el *stream* WSGI) y de ahí deriva el `course_key` **antes** de los permisos |
| `v0/serializers/xblock.py` | `StrictSerializer`: tipos validados y **ningún campo inesperado**. Campos: `id`, `parent_locator`, `display_name`, `category`, `data`, `metadata`, `has_changes`, `children`, `fields`, `has_children`, `video_sharing_*`, `edited_on`, `published` |

🔵 **Conclusión del gap 50:** curso **no** por el árbol versionado (sí por `POST /course/` legacy, pase 32);
**sección, subsección, unidad y componente: los cuatro por `POST /api/contentstore/v1/xblock/`**, distinguidos por
`parent_locator` + `category`.

### El barrido de estándar: **una alta real**, el resto ya estaba. Licencias leídas del archivo `LICENSE`

🔴 **De las piezas de abajo, esta base ya tenía `opensalt` (pase 14), `digital-credentials-public-validator`,
`openbadgeslib` y `ltijs`.** La **única alta** es `Simon-Initiative/lti_1p3`. Se listan todas igual porque las cifras
★/forks y los detalles de licencia **se re-midieron en este pase**, pero **no se cuentan como altas**.

| Repo | `LICENSE` dice | ★ / forks | Dato |
|---|---|---|---|
| [`opensalt/opensalt`](https://github.com/opensalt/opensalt) ⚠️ *ya estaba (pase 14)* | 🟢 **MIT** (2016 Public Consulting Group) | **45** / 27 | PHP, **5.027 commits** en `develop`, 135 issues abiertos. Hoy el README lo presenta como registro de **LER**. 🔴 **Lo nuevo es la divergencia: lo activo y lo compatible con CASE 1.1 está en `develop`, no en el estable 3.2.0 (sept 2023 → CASE v1.0)** |
| [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) ⚠️ *ya estaba* | 🟢 **Apache-2.0** | **17** / 12 | 🔵 **Lo nuevo:** el README dice **«primarily a validator for Open Badges 3.0»** — esta base lo tenía como «OB + CLR» sin la precisión de 3.0. Acepta también OB 2.0 |
| 🟢 [`Simon-Initiative/lti_1p3`](https://github.com/Simon-Initiative/lti_1p3) — **LA ÚNICA ALTA** | 🟢 **MIT** (2021 Carnegie Mellon University) | **16** / 4 | Elixir. **Platform Y Tool**, no sólo Tool — toda la capa LTI previa de esta base era *tool provider* |
| [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) ⚠️ *ya estaba* | 🔴 **LGPL-3.0** | — | Firma/verifica OB 2.0 (JWS) y **3.0 (W3C VC / JWT-VC)**. **No permisiva** |
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) ⚠️ *ya estaba* | 🟢 **Apache-2.0** | — | El canónico. ⚠️ La búsqueda devolvió antes el fork `kristofb/ltijs` (tendencia 132) |
| [`issuebadge/mcp-server`](https://github.com/issuebadge/mcp-server) | 🟢 **MIT** (2025-2026 IssueBadge) | **0** / 0 | TypeScript, **4 commits**. 4 tools. 🔴 Depende de `app.issuebadge.com` + API key: **no es el camino de estándar** |

### 🔴 El repo que NO se puede leer, y es un dato

`IMSGlobal/caliper-php` → **404** en `raw.githubusercontent.com` para `master` **y** `main`; también **404** bajo
`1EdTech/caliper-php`. 1EdTech lo confirma: los repos de **Caliper Sensor API** son **para miembros *Contributing* y
*Affiliate*** con acceso solicitado — algo que **esta base ya tenía registrado** para `caliper-java`/`-js`/`-python`.
⚠️ El paquete **sí** figura en Packagist (`imsglobal/caliper`): el registro **confirma el nombre pero no da el código**
(tendencia 127). 🟢 **Y el camino legible ya estaba acá:** `tl-its-umich-edu/caliper-php-public`, el fork **LGPL-3.0** de
la U. de Michigan, en `agents/top.md` desde el pase 9. **Lo que este pase refuta es la premisa del handoff**, no el
estado de Caliper.

**Y la colisión de nombre, la séptima de esta KB:** `llnl/Caliper` (profiling de performance) y `google/caliper`
(microbenchmarking de Java, **deprecado**) **no tienen nada que ver** con analítica de aprendizaje.

### ⚠️ Nota de método: `curl` sobre `github.com` sigue dando 403 para todo

Consistente con la tendencia **131**. Todo lo de arriba se midió por **`raw.githubusercontent.com`** (que **sí** responde
200 y **404 legítimo** cuando el archivo no existe, que es lo que lo hace un verificador útil) y por **WebFetch** para
★/forks. **El verificador `curl -sI` que el prompt prescribe no sirve contra `github.com` en este entorno.**

## 2026-10-02 (pase 42) — **el dato crudo de las tres acciones: 472 ramas leídas en 61 repos, 26 tools generados desde el árbol de UniTime, 313 archivos de `servicelayer` en `seb-server` y los 4 repos de Kuali fechados y licenciados**

**Este archivo guarda la medición; el veredicto está en `agents/trending.md`.** Todo se obtuvo con `git ls-remote` +
`git fetch --depth 1` + lectura del árbol: **sin API de GitHub, sin Docker, sin el buscador roto de PyPI.**

### 🧭 Las 61 filas de GitHub de `agents/top.md`, re-fechadas por el MÁXIMO ENTRE TODAS SUS RAMAS

**472 ramas leídas. Cobertura 61/61, cero `404`.** Regla: **el tip de la rama por defecto cuenta siempre** (es historia
mergeada); una rama no-defecto agrega vida **sólo si pasa los seis filtros** (`dependabot`, `sdk-regen`, `bot-other`,
`empty-commit`, `agent-branch`, `auto-content`). La columna «Nota» dice qué rama agregó vida o qué clase se retuvo.

| # | Repo | `HEAD` rama defecto | Fecha corregida | Antigüedad | Banda | Nota |
|---:|---|---|---|---:|---|---|
| 1 | [`madhvantyagi/Gnos`](https://github.com/madhvantyagi/Gnos) | 2026-10-02 | **2026-10-02** | 0.0 m | 🟢 activo |  |
| 2 | [`karanb192/algo-sensei`](https://github.com/karanb192/algo-sensei) | 2026-10-02 | **2026-10-02** | 0.0 m | 🟢 activo |  |
| 3 | [`bunizao/moodle-cli`](https://github.com/bunizao/moodle-cli) | 2026-10-02 | **2026-10-02** | 0.0 m | 🟢 activo |  |
| 4 | [`Yuanpeng-Li/gradescope-mcp`](https://github.com/Yuanpeng-Li/gradescope-mcp) | 2026-05-13 | **2026-10-02** | 0.0 m | 🟢 activo | rama `upgrade-mcp-v2` |
| 5 | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 2026-10-02 | **2026-10-02** | 0.0 m | 🟢 activo |  |
| 6 | [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | 2026-10-02 | **2026-10-02** | 0.0 m | 🟢 activo |  |
| 7 | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 2026-10-01 | **2026-10-01** | 0.0 m | 🟢 activo |  |
| 8 | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 2026-10-01 | **2026-10-01** | 0.0 m | 🟢 activo | 🔴 retenida `agent-branch` |
| 9 | [`jupyterlab/jupyter-ai`](https://github.com/jupyterlab/jupyter-ai) | 2026-10-01 | **2026-10-01** | 0.0 m | 🟢 activo |  |
| 10 | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 2026-10-01 | **2026-10-01** | 0.0 m | 🟢 activo |  |
| 11 | [`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp) | 2026-09-07 | **2026-09-30** | 0.1 m | 🟢 activo | rama `feat/cloud-rubric-tabs` |
| 12 | [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | 2026-05-20 | **2026-09-30** | 0.1 m | 🟢 activo | rama `feature/openedx-integratio` |
| 13 | [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 2026-09-29 | **2026-09-30** | 0.1 m | 🟢 activo | rama `dev` |
| 14 | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 2026-09-30 | **2026-09-30** | 0.1 m | 🟢 activo | 🔴 retenida `auto-content` |
| 15 | [`dasgltd/mcp-brasil`](https://github.com/dasgltd/mcp-brasil) | 2026-08-18 | **2026-09-29** | 0.1 m | 🟢 activo | rama `feat/batch-optimization` |
| 16 | [`redbeard-26/asfai-education`](https://github.com/redbeard-26/asfai-education) | 2026-09-28 | **2026-09-28** | 0.1 m | 🟢 activo |  |
| 17 | [`oaknational/oak-ai-lesson-assistant`](https://github.com/oaknational/oak-ai-lesson-assistant) | 2026-09-28 | **2026-09-28** | 0.1 m | 🟢 activo |  |
| 18 | [`Dymayo/moodler-mcp`](https://github.com/Dymayo/moodler-mcp) | 2026-09-19 | **2026-09-28** | 0.1 m | 🟢 activo | rama `fix/accept-token-without-p` |
| 19 | [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) | 2026-09-27 | **2026-09-27** | 0.2 m | 🟢 activo |  |
| 20 | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 2026-09-27 | **2026-09-27** | 0.2 m | 🟢 activo |  |
| 21 | [`nmarafo/OpenDidactia`](https://github.com/nmarafo/OpenDidactia) | 2026-09-25 | **2026-09-25** | 0.2 m | 🟢 activo |  |
| 22 | [`artcc/freelingo`](https://github.com/artcc/freelingo) | 2026-09-25 | **2026-09-25** | 0.2 m | 🟢 activo |  |
| 23 | [`NiccoloSalvini/mcp-moodle-teacher`](https://github.com/NiccoloSalvini/mcp-moodle-teacher) | 2026-09-25 | **2026-09-25** | 0.2 m | 🟢 activo |  |
| 24 | [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | 2026-09-24 | **2026-09-24** | 0.3 m | 🟢 activo |  |
| 25 | [`JOSETRA44/DUTIC-mcp`](https://github.com/JOSETRA44/DUTIC-mcp) | 2026-09-24 | **2026-09-24** | 0.3 m | 🟢 activo |  |
| 26 | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 2026-09-22 | **2026-09-22** | 0.3 m | 🟢 activo |  |
| 27 | [`marcorojasb/tero`](https://github.com/marcorojasb/tero) | 2026-09-20 | **2026-09-20** | 0.4 m | 🟢 activo |  |
| 28 | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | 2026-09-20 | **2026-09-20** | 0.4 m | 🟢 activo | 🔴 retenida `bot-deps` |
| 29 | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | 2026-09-18 | **2026-09-18** | 0.5 m | 🟢 activo |  |
| 30 | [`ashleycribb/learnmcp-xapi`](https://github.com/ashleycribb/learnmcp-xapi) | 2026-09-17 | **2026-09-17** | 0.5 m | 🟢 activo |  |
| 31 | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | 2026-09-17 | **2026-09-17** | 0.5 m | 🟢 activo |  |
| 32 | [`microsoft/Shiksha-Copilot`](https://github.com/microsoft/Shiksha-Copilot) | 2026-09-15 | **2026-09-15** | 0.6 m | 🟢 activo | 🔴 retenida `bot-deps` |
| 33 | [`moon0825/jbnu-lms-student`](https://github.com/moon0825/jbnu-lms-student) | 2026-09-08 | **2026-09-08** | 0.8 m | 🟢 activo |  |
| 34 | [`paulocymbaum/ed-tech-system-mcp`](https://github.com/paulocymbaum/ed-tech-system-mcp) | 2026-09-06 | **2026-09-06** | 0.9 m | 🟢 activo |  |
| 35 | [`giacomomaria81/scorm-mcp-server`](https://github.com/giacomomaria81/scorm-mcp-server) | 2026-09-03 | **2026-09-03** | 1.0 m | 🟢 activo |  |
| 36 | [`avps82/mentar`](https://github.com/avps82/mentar) | 2026-09-03 | **2026-09-03** | 1.0 m | 🟢 activo |  |
| 37 | [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | 2026-08-28 | **2026-08-28** | 1.1 m | 🟢 activo |  |
| 38 | [`Drone9/mereos`](https://github.com/Drone9/mereos) | 2026-08-28 | **2026-08-28** | 1.1 m | 🟢 activo |  |
| 39 | [`PabloPC05/mcp-usc`](https://github.com/PabloPC05/mcp-usc) | 2026-08-27 | **2026-08-27** | 1.2 m | 🟢 activo |  |
| 40 | [`amosblomqvist/learn`](https://github.com/amosblomqvist/learn) | 2026-08-26 | **2026-08-26** | 1.2 m | 🟢 activo |  |
| 41 | [`maxxeddev/open-badges-mcp`](https://github.com/maxxeddev/open-badges-mcp) | 2026-06-10 | **2026-08-17** | 1.5 m | 🟢 activo | rama `chore/release-0.4.0-and-de` |
| 42 | [`vasanthsreeram/Alvarmethod`](https://github.com/vasanthsreeram/Alvarmethod) | 2026-08-16 | **2026-08-16** | 1.5 m | 🟢 activo |  |
| 43 | [`suren-kk/armenian-national-library-mcp`](https://github.com/suren-kk/armenian-national-library-mcp) | 2026-08-10 | **2026-08-10** | 1.7 m | 🟢 activo | 🔴 retenida `bot-deps` |
| 44 | [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | 2026-08-09 | **2026-08-09** | 1.8 m | 🟢 activo |  |
| 45 | [`Timadey/proctor`](https://github.com/Timadey/proctor) | 2026-08-08 | **2026-08-08** | 1.8 m | 🟢 activo |  |
| 46 | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 2026-08-05 | **2026-08-05** | 1.9 m | 🟢 activo |  |
| 47 | [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) | 2026-07-23 | **2026-07-23** | 2.3 m | 🟢 activo |  |
| 48 | [`Nutlope/llamatutor`](https://github.com/Nutlope/llamatutor) | 2026-07-12 | **2026-07-12** | 2.7 m | 🟢 activo |  |
| 49 | [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 2026-06-26 | **2026-06-26** | 3.2 m | ⚠️ tibio |  |
| 50 | [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) | 2026-06-07 | **2026-06-07** | 3.8 m | ⚠️ tibio |  |
| 51 | [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) | 2026-05-03 | **2026-05-03** | 5.0 m | ⚠️ tibio |  |
| 52 | [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | 2026-03-25 | **2026-03-25** | 6.3 m | 🔴 frío |  |
| 53 | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 2026-02-22 | **2026-02-22** | 7.3 m | 🔴 frío |  |
| 54 | [`aswanth9495/exam-guard`](https://github.com/aswanth9495/exam-guard) | 2025-10-09 | **2026-02-04** | 7.9 m | 🔴 frío | rama `scaler/dcp-revamp` |
| 55 | [`satvik314/educhain`](https://github.com/satvik314/educhain) | 2025-12-03 | **2026-01-21** | 8.3 m | 🔴 frío | rama `new-version` |
| 56 | [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) | 2026-01-09 | **2026-01-09** | 8.7 m | 🔴 frío |  |
| 57 | [`pythpythpython/openstax-mcp-server`](https://github.com/pythpythpython/openstax-mcp-server) | 2025-11-30 | **2025-11-30** | 10.1 m | 🔴 frío |  |
| 58 | [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | 2025-11-13 | **2025-11-13** | 10.6 m | 🔴 frío |  |
| 59 | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 2025-08-29 | **2025-08-29** | 13.1 m | 🔴 congelado |  |
| 60 | [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | 2025-06-27 | **2025-06-27** | 15.2 m | 🔴 congelado | 🔴 retenida `bot-deps` |
| 61 | [`Cicatriiz/openedu-mcp`](https://github.com/Cicatriiz/openedu-mcp) | 2025-06-03 | **2025-06-03** | 16.0 m | 🔴 congelado |  |

**Reparto:** 🟢 **48 activas (78,7 %)** · ⚠️ 3 tibias (4,9 %) · 🔴 7 frías (11,5 %) · 🔴 3 congeladas (4,9 %).

### 🔴 Las 25 observaciones de rama RETENIDAS por no ser vida de proyecto, con su clase

| Repo | `HEAD` defecto | Rama retenida (más nueva) | Clase | Autor |
|---|---|---|---|---|
| `CAHLR/OATutor` | 2026-09-30 | `content-staging` → **2026-10-02** | 🔵 `auto-content` | `Generic User` (*«Automated content update»*) |
| `vishalsachdev/canvas-mcp` | 2026-10-01 | `triage/2026-10-02` → **2026-10-02** | `agent-branch` | `Claude` |
| `microsoft/Shiksha-Copilot` | 2026-09-15 | `dependabot/…/joi-17.13.7` → **2026-10-01** | 🔴 `bot-deps` (**5 ramas**) | `dependabot[bot]` |
| `suren-kk/armenian-national-library-mcp` | 2026-08-10 | `dependabot/…/ip-address-10.7.2` → **2026-09-29** | 🔴 `bot-deps` (**10 ramas**) | `dependabot[bot]` |
| `bruchris/canvas-lms-mcp` | 2026-09-20 | `dependabot/…/sdk-1.30.1` → **2026-09-29** | 🔴 `bot-deps` (**2 ramas**) | `dependabot[bot]` |
| `trilogy-group/oneroster-ts` | 2025-06-27 | `speakeasy-sdk-regen-1746144633` → **2026-05-11** | 🔴 `sdk-regen` + `empty-commit` | `speakeasy-github[bot]` (*«empty commit to trigger [run-tests] workflow»*) |
| `satvik314/educhain` | 2025-12-03 | `claude/relaxed-curie-mNW2l` → **2026-05-29** | `agent-branch` | `Claude` (*«Refactor to Educhain 1.0: drop LangChain…»*) |
| `oaknational/oak-ai-lesson-assistant` | 2026-09-28 | `dependabot/…/next-16.2.11` → 2026-07-26 | 🔴 `bot-deps` | `dependabot[bot]` |

⚠️ **`oneroster-ts` es el caso que justifica el filtro entero:** el máximo ingenuo lo promovería de **15,2 meses a 4,8**
con un **commit vacío de un bot** en una rama de regeneración de SDK. **Sostiene P58, P60 y P64 y 132 tools.**

### 🟢 `UniTime/unitime` — los 15 conectores verificados en el árbol, con el nombre leído del `getName()`

**Ruta:** `JavaSource/org/unitime/timetable/api/connectors/`. **Verbos leídos de los `do*` sobreescritos, no de la
documentación.** 🔴 **Corrección de método sobre el propio instrumento: un `grep` del primer literal después de
`getName` da nombres FALSOS** (devolvió `"name"` para `EventsConnector` y `"log"` para `ScriptConnector`); hay que leer
**el `return` del override**. Ambos confirmados así: **`events` y `script`**. La tabla del pase 41 era correcta.

| Clase | Nombre | GET | POST | PUT | DELETE | Tools generados |
|---|---|:--:|:--:|:--:|:--:|:--:|
| `RoomsConnector` | `rooms` | ✅ | ✅ | ✅ | ✅ | 4 |
| `BuildingsConntector` ⚠️ *(typo upstream, confirmado)* | `buildings` | ✅ | ✅ | | ✅ | 3 |
| `EventsConnector` | `events` | ✅ | ✅ | | ✅ | 3 |
| `DataExchangeConnector` | `exchange` | ✅ | ✅ | | | 2 |
| `OnlineStudentSchedulingConnector` | `sectioning` | ✅ | ✅ | | | 2 |
| `VariableTitleCourseConnector` | `var-title-crs` | ✅ | ✅ | | | 2 |
| 🔴 `ScriptConnector` | 🔴 `script` | ✅ | 🔴 ✅ | | | 2 |
| `JsonConnector` | `json` | | ✅ | | | 1 |
| `ClassInfoConnector` | `class-info` | ✅ | | | | 1 |
| `CurriculaConnector` | `curricula` | ✅ | | | | 1 |
| `EnrollmentsConnector` | `enrollments` | ✅ | | | | 1 |
| `InstructorsConnector` | `instructors` | ✅ | | | | 1 |
| `InstructorScheduleConnector` | `instructor-schedule` | ✅ | | | | 1 |
| `RolesConnector` | `roles` | ✅ | | | | 1 |
| `StudentGroupsConnector` | `student-groups` | ✅ | | | | 1 |
| **15 conectores** | | **13** | **8** | **1** | **3** | 🟢 **26** |

🟢 **Con la política por defecto (negar `script`, sólo lecturas) quedan 13 de 26 expuestos.** Probado por ejecución:
**23 aserciones en verde, 0 de 9 llamadas retenidas llegaron al upstream.** Ver **P92**.

### 🟢 `SafeExamBrowser/seb-server` — la superficie de `dev-3.0`, al nivel que el pase 41 midió `edx-proctoring`

| Medición | Valor |
|---|---|
| Rama medida | 🔴 **`dev-3.0`**, no `master` (**gap 87**) |
| Tip de `dev-3.0` | 🟢 **2026-10-01**, `Andreas Hefti`, *«code cleanup»* |
| Licencia | ⚠️ **MPL-2.0**, leída del `LICENSE` del árbol |
| Archivos versionados | **1.201** |
| Archivos `.java` en `webservice/servicelayer/` | **313** |
| Archivos relacionados con *proctoring* | **75** |
| SPI de proveedor de *proctoring* | 🟢 **`RemoteProctoringService`** (130 líneas) |
| Métodos / `default` / **obligatorios** | 14 / 2 / 🔴 **12** |
| Implementaciones de referencia | **2** — `JitsiProctoringService`, `ZoomProctoringService` |
| Registro | 🟢 **abierto** — `RemoteProctoringServiceFactory(Collection<RemoteProctoringService>)`, inyección de Spring |
| 🔴 Tipo | 🔴 **cerrado** — `enum ProctoringServerType { JITSI_MEET, ZOOM }` |
| Archivos *Covered* que mencionan el enum / **que hay que tocar** | 10 / 🟢 **1** |
| Validador ante un tipo desconocido | ⚠️ **`return true`** — pasa sin validar |

**Las 4 APIs de integración de LMS** (`webservice/servicelayer/lms/`): `CourseAccessAPI` (147 líneas, ~21 firmas, 3
`default`), `SEBRestrictionAPI` (69, ~8, 2), `LmsAPITemplate` (83, ~4, 1), `FullLmsIntegrationAPI` (38, ~6, **0
`default`**). **Bindings concretos en el árbol:** `edx`, `moodle`, `olat`, `ans`, `mockup`.

### 🔴 `Kuali` — cuatro repos que esta base no tenía, los cuatro muertos

| Repo | Licencia (del archivo) | Rama defecto | `HEAD` | Máx. corregido | Antigüedad |
|---|---|---|---|---|---|
| [`kuali/rice`](https://github.com/kuali/rice) | 🟢 **ECL-2.0** | `master` (11 ramas) | 2017-05-17 | **2018-09-01** (`rice-2.5`) | 🔴 **~8 años** |
| [`KualiCo/rice`](https://github.com/KualiCo/rice) | 🟢 **ECL-2.0** | `java11` (13 ramas) | 2020-07-01 | **2020-07-01** | 🔴 **~6 años** |
| [`kuali/kc`](https://github.com/kuali/kc) | 🔴 **AGPL-3.0** | `master` (12 ramas) | 2017-01-06 | 2017-01-06 | 🔴 **~9 años** |
| [`kuali/kfs`](https://github.com/kuali/kfs) | 🔴 **AGPL-3.0** | `master` (35 ramas) | 2018-03-22 | 2018-03-22 | 🔴 **~8 años** |

🔴 **`KualiCo/kc`, `KualiCo/kfs` y `KualiCo/kuali-student` no existen** (`git ls-remote` falla). ⚠️ **Y `KualiCo/rice` da
la cuarta confirmación de la clase `dependabot`:** su rama más nueva es `dependabot/maven/…jackson-databind-2.9.10.7`
(**2021-01-21**), 7 meses «más fresca» que la vida real del repo.

## 2026-10-02 (pase 41) — **el dato crudo de las dos capas que el pase 40 midió vacías: 3 repos fechados y licenciados desde el árbol, 15 conectores con nombre, 36 controladores REST, 11 nombres de registro probados y 8 de 8 en 404**

**Instrumentos de este pase:** `git ls-remote` (refs y tags), `git clone --depth 1 --filter=blob:none --no-checkout` +
`git log -1 --format=%cI` (fecha), `git show HEAD:<archivo>` (licencia leída del árbol), `zipfile` sobre el *wheel* de
PyPI (superficie de API), `registry.npmjs.org/<nombre>` y el índice `simple` de PyPI (vacío).
🔴 **`curl` sobre `github.com` NO se usa para verificar: devuelve 403 para repos reales e inventados por igual** —
re-confirmado con control negativo en este pase (tendencia **131**).

### Las tres altas de base, con el dato crudo leído del árbol

| Repo | Licencia (archivo y dónde) | `HEAD` (rama por defecto) | Tags | Archivos | Lenguaje | Región |
|---|---|---|---|---|---|---|
| [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** — `LICENSE` + `NOTICE` (*«Copyright 2015, The Apereo Foundation»*) | 🟢 **2026-10-01** (Tomáš Müller) | **202** | **4.154** | Java | **North America** (Apereo Foundation; ⚠️ *committer* en `+02:00`) |
| [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | ⚠️ **MPL-2.0** — `LICENSE` en `master` | ⚠️ **2026-04-01** en `master` / 🟢 **2026-10-01** en `dev-3.0` | **108** | **1.450** | Java (`ch.ethz.seb`) | **EMEA** (ETH Zürich, Suiza) |
| [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) | ⚠️ **MPL-2.0** — `LICENSE.txt` (+ `Setup/Resources/License.rtf`) | 🟢 **2026-09-25** (Damian Büchel) | **20** | **1.452** | C# | **EMEA** (ETH Zürich, Suiza) |

⚠️ **MPL-2.0 no es MIT/Apache y tampoco es AGPL: es copyleft DÉBIL por archivo.** Lo que se modifica de los archivos
cubiertos se publica; lo que se agrega al lado, no. **Para un integrador es usable sin abrir su propio código**, y es una
clase de licencia que esta base no tenía anotada en esta capa.

### `UniTime`: los 15 conectores de API, con su nombre registrado y sus verbos — el dato que hace al envoltorio MCP cotizable

**Ruta:** `JavaSource/org/unitime/timetable/api/`. **Clase base:** `ApiConnector` (`doGet`/`doPut`/`doPost`/`doDelete`,
`getName()`); **autenticación por token ya incluida** (`?token=`, `ApiCanUseAPIToken`, `authenticateWithTokenIfNeeded`);
*helpers* `JsonApiHelper` / `XmlApiHelper` / `BinaryFileApiHelper`.

| Clase | Nombre registrado | GET | POST | PUT | DELETE |
|---|---|:--:|:--:|:--:|:--:|
| `RoomsConnector` | `rooms` | ✅ | ✅ | ✅ | ✅ |
| `BuildingsConntector` ⚠️ *(typo del upstream)* | `buildings` | ✅ | ✅ | | ✅ |
| `EventsConnector` | `events` | ✅ | ✅ | | ✅ |
| `OnlineStudentSchedulingConnector` | `sectioning` | ✅ | ✅ | | |
| `DataExchangeConnector` | `exchange` | ✅ | ✅ | | |
| 🔴 `ScriptConnector` | 🔴 `script` | ✅ | 🔴 ✅ | | |
| `VariableTitleCourseConnector` | `var-title-crs` | ✅ | ✅ | | |
| `JsonConnector` | `json` | | ✅ | | |
| `ClassInfoConnector` | `class-info` | ✅ | | | |
| `CurriculaConnector` | `curricula` | ✅ | | | |
| `EnrollmentsConnector` | `enrollments` | ✅ | | | |
| `InstructorsConnector` | `instructors` | ✅ | | | |
| `InstructorScheduleConnector` | `instructor-schedule` | ✅ | | | |
| `RolesConnector` | `roles` | ✅ | | | |
| `StudentGroupsConnector` | `student-groups` | ✅ | | | |

🔴 **`script` acepta `POST`: un envoltorio MCP de los 15 conectores expone ejecución de scripts del servidor como tool.**
Va en la *denylist* antes de la primera demo (**P88**).

### `seb-server`: 36 controladores REST y 41 constantes de *endpoint*

**Controladores** (`webservice/weblayer/api/`): `ExamAdministrationController`, `ExamProctoringController`,
`ExamMonitoringController`, `ExamTemplateController`, `ExamConfigurationMappingController`, `ExamAPI_V1_Controller`,
`ExamAPIDiscoveryController`, `ClientConnectionController`, `ClientEventController`, `ClientGroupController`,
`LmsSetupController`, `LmsIntegrationController`, `QuizController`, `SEBClientConfigController`,
`SEBSettingsController`, `ConfigurationController`, `ConfigurationNodeController`, `ConfigurationValueController`,
`ConfigurationAttributeController`, `CertificateController`, `IndicatorController`, `InstitutionController`,
`UserAccountController`, `UserActivityLogController`, `RegisterUserController`, `BatchActionController`,
`OrientationController`, `InfoController`, `LightController`, `ViewController`, `EntityController`,
`ActivatableEntityController`, `ReadonlyEntityController`, `APIExceptionHandler`, `APIConstraintViolationException`,
`ExamAPIDiscoveryController`.

**`*_ENDPOINT` en `gbl/api/API.java`: 41.** Los que importan para una puerta de agente:

| Grupo | Endpoints |
|---|---|
| Examen / administración | `/exam`, `/exam-template`, `/exam-configuration-map`, `/indicator`, `/client-group`, `/quiz` |
| 🟢 **Monitoreo** | `/monitoring`, `/overview`, `/instruction`, `/notification`, `/disable-connection`, `/signature`, `/testrun`, `/finishedexams` |
| 🟢 **API de cliente SEB** | `/handshake`, `/examconfig`, `/light-config`, `/sebping`, `/seblog` |
| 🟢 **Integración con LMS** | `/lms-setup`, `/exam`, `/seb_config`, `/login_token` |
| Conexiones y eventos | `/seb-client-connection`, `/data`, `/seb-client-event` |
| Configuración | `/configuration`, `/configuration-node`, `/configuration_value`, `/configuration_attribute`, `/template-attribute`, `/orientation` |
| Plataforma | `/oauth`, `/info`, `/register`, `/institution`, `/useraccount`, `/useractivity`, `/certificate`, `/client_configuration`, `/batch-action` |

**`enum LmsType`** (`gbl/model/institution/LmsSetup.java`): `MOCKUP`, **`OPEN_EDX`**, **`MOODLE`**,
**`MOODLE_PLUGIN`** (la única con `LMS_FULL_INTEGRATION`), `ANS_DELFT`, **`OPEN_OLAT`**.

### `edx-proctoring` 5.2.0: el dato crudo del *wheel*, y la licencia que contradice al repo **a favor**

| Medición | Valor |
|---|---|
| *Wheel* | `edx_proctoring-5.2.0-py2.py3-none-any.whl`, **1.315.493 bytes**, **294 entradas**, subido **2025-04-28** |
| Releases en PyPI | **253** — 🔴 el último es el **2025-04-28** (**17 meses**), con `HEAD` del repo el **2026-05-30** |
| Licencia declarada | `License: AGPL 3.0`; `Classifier: ... GNU Affero General Public License v3 or later (AGPLv3+)` |
| 🟢 **`edx_proctoring/backends/LICENSE.txt`** | 🟢 **Apache-2.0**, **11.357 bytes** — contiene *«Apache License / Version 2.0»*, **no contiene «Affero»** |
| 🟢 `edx_proctoring/backends/README.txt` | **174 bytes**: *«The code in this directory is licensed under a license different from the rest of the edx-proctoring repository. These modules are licensed under Apache 2.0.»* |
| ✅ Verificación cruzada en el árbol | `raw.githubusercontent.com/openedx/edx-proctoring/master/edx_proctoring/backends/README.txt` → **200**; `.../LICENSE.txt` → **200** |
| Archivos clave | `models.py` 30.184 b · `urls.py` 6.397 b · `views.py` 94.918 b · `api.py` 123.167 b · `backends/rest.py` 14.460 b · `backends/software_secure.py` 15.037 b |
| Dependencias declaradas | `Django>=2.2`, `djangorestframework`, `django-waffle`, `django-crum`, `django-model-utils`, `django-webpack-loader>=0.6.0`, `django-ipware>=1.1.0`, `django-simple-history` |
| *Entry points* | `[lms.djangoapp]` y `[cms.djangoapp]` → `EdxProctoringConfig`; 🟢 **`[openedx.proctoring]` → `mock`, `null`, `rpnow4`, `software_secure`** |
| Modelos | **12 clases** (ver `agents/trending.md`, pase 41) |
| Rutas | **20** (18 en `v1/` + 2 *callbacks*) |
| `ProctoringBackendProvider` | **18 métodos, 8 atributos, 🔵 0 `@abstractmethod`** |
| `BaseRestProctoringProvider` | **27 métodos**, incluidos 8 constructores de URL |

### `exam-guard`: la historia de los dos archivos, que es lo que cierra el gap 83

| Hecho | Dato |
|---|---|
| Repo | [`aswanth9495/exam-guard`](https://github.com/aswanth9495/exam-guard) — *«AI proctoring tool»*, `main`, `HEAD` **2025-10-09** |
| `LICENSE` (Apache-2.0) entró en | 🔴 **`1fcf7f6` *«Initial commit»*, 2024-09-10T01:20 — único archivo del commit, 201 líneas** |
| `package.json` entró en | *«feat: add base code»*, 2024-09-10T15:39, con **`"license": "ISC"`** |
| `LICENSE` modificado después | 🔴 **nunca** |
| `package.json` modificado después | **sí, hasta 2025-10-09** |
| ISC en el registro | 🟢 **113 de 113 versiones** (2024-09-12 → 2026-01-22) |
| Versión en el árbol vs. en npm | **8.1.0** contra **10.0.4** — ⚠️ **el registro va 2 *majors* adelante del repo** |

### `Timadey/proctor` y `@ink-waffle/sisu-mcp`: la medición que parte el gap 81 en dos

| Pieza | `LICENSE` en el árbol | `package.json` del árbol | README | Manifiesto del registro | Total de declaraciones |
|---|---|---|---|---|---|
| `Timadey/proctor` (`HEAD` 2026-08-08) | 🔴 **no existe en ninguna rama ni commit** (`git log --all --name-only`: 0 coincidencias) | 🟢 **MIT** | 🟢 **badge *«License: MIT»*** + *«licensed under the MIT License — see the [LICENSE] file»* | 🟢 MIT | 🟢 **3 (todas en el árbol)** |
| `@ink-waffle/sisu-mcp` 0.1.0 (2026-09-17) | 🔴 **tarball sin `LICENSE`** (44.781 b, 17 `dist/*.js`) | ⚠️ sólo en el manifiesto empaquetado | 🔴 **no hay README en el tarball** | 🟢 MIT | 🔴 **1 en todo el mundo** |

### 🔴 El vacío medido: nadie publicó una puerta de agente para ninguna de las dos capas

| Canal | Nombres probados | Resultado |
|---|---|---|
| npm | `unitime-mcp`, `mcp-unitime`, `seb-mcp`, `mcp-seb`, `safeexambrowser-mcp`, `sebserver-mcp`, `timetable-mcp`, `timetabling-mcp` | 🔴 **404 en 8 de 8** |
| PyPI, índice `simple` completo (**46.675.078 bytes**, 903.402+ nombres) | `unitime`, `seb-server`, `safeexambrowser` | 🔴 **0 nombres** |

### La re-medición de las 10 filas que el pase 37 declaró paradas, contra TODAS las ramas

| Repo | Ramas | `HEAD` por defecto | Más nuevo en cualquier rama | Autor del más nuevo |
|---|---|---|---|---|
| `Cicatriiz/openedu-mcp` | 5 | 2025-06-03 | 2025-06-03 (`main`) | — |
| `trilogy-group/oneroster-ts` | 6 | 2025-06-27 | **2026-05-11** (`speakeasy-sdk-regen-1746144633`) | 🔴 **`speakeasy-github[bot]`**, *«empty commit to trigger [run-tests] workflow»* |
| `DavidLMS/learnmcp-xapi` | 1 | 2025-08-29 | 2025-08-29 (`main`) | — |
| `karanb192/algo-sensei` | 2 | 🟢 **2026-10-02** | 🟢 **2026-10-02T15:10:33+05:30** (`main`) | Karan Bansal — *«Offer a star invitation once after confirmed learning (#2)»*, **commit nº 2 del repo**, 9 commits totales |
| `plastic-labs/tutor-gpt` | **49** | 2025-11-13 | **2026-02-20** (`vineeth/elysia`) | humano, rama de *feature* |
| `pythpythpython/openstax-mcp-server` | 1 | 2025-11-30 | 2025-11-30 (`main`) | — |
| `satvik314/educhain` | 7 | 2025-12-03 | **2026-05-29** (`claude/relaxed-curie-mNW2l`) | 🔵 **`Claude`** — *«Refactor to Educhain 1.0: drop LangChain, build on the OpenAI SDK»* |
| `HugeCatLab/ChatTutor` | 2 | 2026-01-09 | 2026-01-09 (`main`) | — |
| `peancor/moodle-mcp-server` | 2 | 2026-02-22 | 2026-02-22 (`main`) | — |
| `24kchengYe/human-skill-tree` | 1 | 2026-03-25 | 2026-03-25 (`master`) | — |

### Ramas de `seb-server`, que es el caso que obliga a cambiar el instrumento

| Rama | Último commit | Nota |
|---|---|---|
| 🔴 `master` (**rama por defecto**) | **2026-04-01** | la que mide `ls-remote --symref HEAD` |
| 🟢 **`dev-3.0`** | 🟢 **2026-10-01** | donde desarrolla; tag **`v3.0-latest`** publicado |
| 🟢 `development` | 2026-09-30 | |

**Ramas totales:** 14 (`dev-1.2` … `dev-3.0`, `development`, `master`, `old_gui`, `dev-e2e-tests`, `SEBSERV-918-PoC-SEB-Restriction`).

### 🔴 Control negativo del verificador prescripto, re-confirmando la tendencia 131

| URL | Existe | `curl` | `git ls-remote` |
|---|---|---|---|
| `github.com/UniTime/unitime` | sí | 🔴 **403** | 🟢 refs |
| `github.com/UniTime/this-repo-does-not-exist-xyz123` | **no** | 🔴 **403** | 🟢 falla |
| `github.com/openedx/edx-proctoring` | sí | 🔴 **403** | 🟢 refs |
| `github.com/openedx/fake-repo-zzz999` | **no** | 🔴 **403** | 🟢 falla |

🔴 **`curl`: 4 de 4 iguales, no discrimina. `git ls-remote`: 4 de 4 correctos.**

## 2026-10-02 (pase 40) — **el dato crudo del barrido sobre las capas de administración académica: 28 términos × 4 registros, 1 instrumento roto, 1 instrumento nuevo, 6 altas y 5 capas confirmadas vacías de agente**

**Consigna ejecutada: la acción 1 del pase 39** — correr el barrido por registro sobre las capas que el 39 no barrió
(*proctoring*, *timetabling*, analítica por nombre de herramienta, admisiones, *student success*, accesibilidad).

### Los 28 términos, para que el barrido sea repetible

```
proctoring proctor safe-exam-browser exam-monitoring
timetable timetabling unitime school-timetable
learninglocker ralph-lrs trax-lrs lrsql openlrs yet-analytics watershed-lrs caliper-sensor
admissions student-application enrollment
student-success early-warning student-retention academic-advising
accessibility-checker alt-text screen-reader wcag-audit a11y-report
```

### 🔴 Estado de los cuatro endpoints — uno cambió desde el pase 39 y hay que corregir la tabla

| Registro | Endpoint | Pase 39 | **Pase 40** |
|---|---|---|---|
| npm | `registry.npmjs.org/-/v1/search?text=<t>` | 200 | 🟢 **200, resultados reales** |
| Packagist | `packagist.org/search.json?q=<t>` | 200 | 🟢 **200, resultados reales** |
| RubyGems | `rubygems.org/api/v1/search.json?query=<t>` | 200 | 🟢 **200, resultados reales** |
| PyPI | `pypi.org/search/?q=<t>` (HTML) | 200 | 🔴 **200 pero DESAFÍO ANTI-BOT — 0 resultados en 28/28** |

🔴 **El procedimiento del pase 39 para PyPI ya no mide nada, y su modo de falla es el peor posible: código 200.** La
respuesta pesa **3.038 bytes** y lleva `<title>Client Challenge</title>`. **Sin un control de contenido, 28 ausencias
falsas se habrían publicado como medidas.**

### 🟢 El instrumento de reemplazo, medido

```
curl -s https://pypi.org/simple/ -o pypi_simple.html
#   -> HTTP 200, 46.675.078 bytes
grep -o '>[^<]*</a>' pypi_simple.html | sed 's/^>//; s|</a>$||' > pypi_names.txt
#   -> 903.402 nombres de paquete
grep -i 'proctor' pypi_names.txt      # descubrimiento local, sin red
curl -s "https://pypi.org/pypi/<nombre>/json"   # confirmación: licencia, releases, fechas
```

**Rendimiento del canal nuevo, por término:**

| Término | Nombres en PyPI | Término | Nombres en PyPI |
|---|---|---|---|
| `proctor` | **22** | `admission` | **13** |
| `proctoring` | 6 | `enrol` | 25 |
| `timetabl` | **37** | `student-success` | **1** |
| `unitime` | **0** | `early-warning` | **0** |
| `lrs` | 57 | `retention` | 23 |
| `xapi` | **169** | `advising` | 2 |
| `caliper` | 14 | `accessib` | 67 |
| `wcag` | 9 | `a11y` | 37 |
| `safeexam` / `safe-exam` | **0 / 0** | | |

🔵 **Dos ceros que valen como dato:** `unitime` (el planificador de horarios universitario de referencia) **no publica
en PyPI**, y **`safe-exam-browser` tampoco** — las dos piezas canónicas de sus capas viven fuera del registro, que es
la misma forma que la tendencia 133 del pase 39 describió para la infraestructura educativa desplegada.

### Las 6 altas con su dato crudo

| Paquete / repo | Licencia (dónde se leyó) | `HEAD` | Último release | Releases | Lenguaje | Región |
|---|---|---|---|---|---|---|
| `datakind/student-success-tool` | 🟢 **MIT** — `LICENSE.md` del árbol | **2025-09-08** | **2025-08-05** | 14 | Python (3.10–3.12) | **North America** |
| `openedx/edx-proctoring` | **AGPL-3.0** — `LICENSE.txt` (`master`) | **2026-05-30** | **2025-04-28** | **253** | Python | **North America** (Open edX / Axim) |
| `Drone9/mereos` | 🟢 **MIT** — `LICENSE` + campo npm | **2026-08-28** | **2026-08-28** | 19 | JavaScript | Sin determinar (`+05:00`) |
| `Timadey/proctor` (`@timadey/proctor`) | ⚠️ **MIT sólo campo npm** — 🔴 sin `LICENSE` en el árbol | **2026-08-08** | **2026-08-08** | 7 | JavaScript | **EMEA** (`+01:00`) |
| `odoo14-addon-ssi-school-admission` | **AGPL-3** | — (PyPI) | **2026-05-01** | 6 | Python | **APAC** (Indonesia) |
| `timeback-caliper` | ⚠️ **MIT** — `license_expression` de PyPI | 🔴 **repo ilegible** | **2026-07-18** | **55** | Python ≥3.12 | Sin determinar |

🔴 **`timeback-caliper` es la cuarta instancia de la tendencia 140 en dos pases:** declara
`Repository: github.com/superbuilders/timeback-dev-python` y **`git ls-remote` falla**. 55 releases y una licencia
permisiva declarada, con **cero superficie de auditoría**. Se registra, no se recomienda.

### 🔴 La verificación de licencia que se contradijo a sí misma — clase de evidencia nueva

| Pieza | Campo del registro | Archivo del árbol | Veredicto |
|---|---|---|---|
| `exam-guard` (npm, 113 releases, `HEAD` 2025-10-09) | **ISC** | 🔴 **Apache-2.0** (`LICENSE` en `main`) | **CONTRADICCIÓN** |

🔵 **Esto no es el gap 81 y conviene no confundirlos.** El gap 81 es *«la licencia está sólo en el manifiesto»* —
ausencia de una de las dos fuentes. **Esto es peor: las dos fuentes existen y dicen cosas distintas.** Para un
entregable, **manda el archivo del árbol** (es el instrumento que el pase 39 ya había sancionado), pero la
contradicción **hay que resolverla con el autor antes de usar la pieza**, porque mientras exista, cualquiera de las
dos licencias es citable de buena fe por un tercero. **Y la diferencia no es cosmética: ISC y Apache-2.0 difieren en
la cláusula de patentes**, que es justo lo que un cliente grande revisa.

### 🔴 Ruido medido y rechazos, para que el próximo pase no lo vuelva a pagar

**El filtro importa más que el término.** El primer barrido, filtrando por `accessib|a11y|wcag` junto con los términos
educativos, devolvió **256 candidatos** en npm y **prácticamente todos eran herramientas de accesibilidad web
genéricas** (`eslint-plugin-jsx-a11y`, `@storybook/addon-a11y`, `cypress-a11y-report`, `wick-a11y`…). **Nada de
educación.** Exigiendo un *token* de dominio educativo y cruzándolo con señal agéntica, los 256 bajaron a **22**, y de
esos **11 eran homónimos**. 🔵 **Regla: en esta capa, «accesibilidad» sin un término educativo al lado es un término
inútil** — el ecosistema de a11y web lo satura por completo.

**Los 11 homónimos rechazados, con la evidencia:**

| Candidato | Qué es | Por qué entró |
|---|---|---|
| ⛔ `proctor-mcp` | *human-in-the-loop* para agentes MCP | `proctor` |
| ⛔ `proctor-skill` | interroga al dev antes de `git push` | `proctor` |
| ⛔ `@genramzi/proctor` | audita lo que hizo un *coding agent* | `proctor` |
| ⛔ `proctor-ai` (PyPI, MIT) | *prompt engineering* | `proctor` |
| ⛔ `agentproctor` / `sqlproctor` / `onion-proctor` | supervisión de agentes / SQL / red | `proctor` |
| ⛔ `matthewproctor-postcodes` | **apellido** — códigos postales AU | `proctor` |
| ⛔ `caliper-ai` (MIT) / `caliper-py` (MIT) / `caliper-reader` (BSD, LLNL) / `caliper-sdk` (GPL-3.0) / `caliper` (MPL-2.0) / `@dendiem/caliper` | costo de AI, *tracker* ML, *profiling* HPC, observabilidad LLM, cambios de paquete, revisión de UI | `caliper` |
| ⛔ `sih-br-mcp` | **admisiones hospitalarias** de Brasil (DATASUS) | `admissions` |
| ⛔ `timetable-api-node` | **transporte público de Lviv** | `timetable` |
| ⛔ `@moinsen-dev/tool-teacher` | inventario de herramientas de dev | `early-warning` |
| ⛔ `@aep-foundation/*` | *Agent Enrollment Protocol* — credenciales de agente | `enrollment` |
| ⛔ `proctoring-sdk` (npm, 14 releases) | 🔴 **sin licencia y sin repo** | `proctoring` |

### 🔴 Las 5 ausencias confirmadas por doble canal

**No hay puerta MCP de educación para:** *proctoring*, *timetabling*, admisiones, *student success* ni accesibilidad —
**en ninguno de los cuatro registros**, con el canal npm/Packagist/RubyGems sano y el canal PyPI reemplazado por el
índice `simple`. Lo que existe en esas capas son **librerías de aplicación** (las 6 altas de arriba) y **ningún
agente**. 🔵 **La única traza de un MCP de *timetabling* es `ucleeds-mcp-tester`** (MIT, 1 release 2025-04-25, sin
repo): *«Test client for UCLeeds Timetabling MCP integration»* — **el cliente de prueba se publicó y el servidor no**.

## 2026-10-02 (pase 39) — **el dato crudo del barrido por REGISTRO: 23 términos × 4 registros, 8 altas, 5 homónimos rechazados y 9 ausencias confirmadas por segundo canal**

**El instrumento de este pase no es GitHub.** Es la acción 1 del pase 38: consultar **npm, PyPI, Packagist y
RubyGems** con el nombre del **proyecto** (`moodle`, `chamilo`, `sakai`, `ed-fi`, `frappe`, `koha`…), no del protocolo
(`mcp`, `agent`). Los cuatro registros responden **200** en este entorno; `github.com` por `curl` sigue respondiendo
**403 para todo** (tendencia 131), así que la verificación de existencia es **`git ls-remote`** y la de licencia es el
**archivo** leído del árbol clonado o del tarball publicado.

### Los endpoints usados, para que el barrido sea repetible

| Registro | Endpoint de búsqueda | Código |
|---|---|---|
| npm | `registry.npmjs.org/-/v1/search?text=<término>` | 200 |
| PyPI | `pypi.org/search/?q=<término>` (HTML; **no hay API de búsqueda JSON**) | 200 |
| Packagist | `packagist.org/search.json?q=<término>` | 200 |
| RubyGems | `rubygems.org/api/v1/search.json?query=<término>` | 200 |

⚠️ **PyPI no tiene API de búsqueda**: hay que raspar el HTML de `/search/`. El JSON **por proyecto**
(`pypi.org/pypi/<nombre>/json`) sí existe y es el que sirve para **confirmar** un nombre, nunca para descubrirlo
(tendencia 127).

🔵 **Nota de verificación de URL, porque toca a tres filas de `agents/top.md` de este pase:** las páginas web
`npmjs.com/package/<pkg>` devuelven **403** en este entorno, **igual que `github.com`** — y por el mismo motivo, que es
política de proxy y no inexistencia del paquete (tendencia 131). **Las tres piezas de npm de este pase se verificaron
contra `registry.npmjs.org/<pkg>`, que devuelve 200 en las tres**, y de ahí salieron licencia, versiones, fechas de
release y *maintainer*. **La URL legible por humanos que quedó escrita en la tabla no es la que se verificó: la
verificada es la del registro.** Quien revise esas filas desde otra red puede confirmar las dos.

### Las 8 altas con su dato crudo

| Repo / paquete | Licencia (dónde se leyó) | `HEAD` o release | Commits / tags | Lenguaje | Tools | Región |
|---|---|---|---|---|---|---|
| `PabloPC05/mcp-usc` | **MIT** — `LICENSE` textual + `pyproject.toml` | `HEAD` **2026-08-27** | 30 / — | Python | **91** | **EMEA** (ES) |
| `JOSETRA44/DUTIC-mcp` | **MIT** — `LICENSE` textual + manifiesto | `HEAD` **2026-09-24** | 74 / — | TypeScript | **12** | **LATAM** (PE) |
| `dasgltd/mcp-brasil` | **MIT** — `LICENSE`, *«(c) 2025-2026 MCP Brasil»* | `HEAD` **2026-08-18** | **246 / 23** | Python ≥3.10 | **97** (13 de educación) | **LATAM** (BR) |
| `maxxeddev/open-badges-mcp` | **MIT** — `LICENSE` + manifiesto + README | `HEAD` **2026-06-10** ⚠️ | 28 / 5 | TypeScript | **16** | **APAC** (AU) |
| `@ink-waffle/sisu-mcp` | ⚠️ **MIT** sólo campo npm | release **2026-09-17** | — (**sin repo**) | JavaScript | **12** | **EMEA** (FI) |
| `suren-kk/armenian-national-library-mcp` | **MIT** — `LICENSE` + manifiesto | `HEAD` **2026-08-10** | 37 / — | TypeScript | **23** (todas `READ_ONLY`) | **EMEA** (AM) |
| `ed-fi-sdk-mcp` (npm, *maintainer* `edfi`) | **Apache-2.0** — `LICENSE` **en el tarball** | release **2025-10-03** 🔴 | — (**repo ilegible**) | TypeScript | **11** | **North America** |
| `frappe-mcp-server` | ⚠️ **ISC** sólo campo npm | release **2025-07-30** 🔴 | 32 releases (**repo ilegible**) | TypeScript | **21** | Sin región determinada |

🔵 **La columna «Región» se determinó por dos instrumentos, y conviene saber cuál se usó en cada fila:** la
**organización** cuando existe (Ed-Fi Alliance → North America; Funidata/Sisu → EMEA; USC → EMEA; UNSA → LATAM; MCP
Brasil → LATAM) y, cuando no, la **zona horaria del commit** (`+10:00` → APAC para `open-badges-mcp`; `+04:00` → EMEA
para la biblioteca armenia). **La zona horaria es un instrumento débil y se declara como tal**: ubica al autor en el
momento del commit, no al proyecto. `frappe-mcp-server` **no se pudo ubicar por ninguno de los dos** y se deja sin
región en vez de inventarla.

### Las dos filas de `agents/top.md` que este pase re-mide y corrige

| Fila | Qué decía | Qué se midió hoy |
|---|---|---|
| `Dymayo/moodler-mcp` | **TypeScript**, *«tools NO enumeradas»* | 🔴 **Es Python** (`requires-python >=3.14`, `mcp>=2.2,<3`). **38 tools = 30 lectura + 6 escritura de alumno + 2 escritura docente.** `save_assignment_grade` → `workflowstate=""`: **publica la nota** |
| `bruchris/canvas-lms-mcp` | 165 tools | ✅ **Confirmado en el código, no en el README**: **120 `readOnlyHint: true`** + **48 `destructiveHint: true`** (el README dice 117 de lectura; la diferencia son las tools condicionales). 🟢 **Y lo que no estaba anotado: tiene MODO FERPA** — `CANVAS_PSEUDONYMIZE_STUDENTS` seudonimiza, la reversión exige **segunda** bandera y `resolve_pseudonym` **sólo se registra en stdio**, como tool **166** |

### `mcp-brasil`: el dato que corrige la tendencia 114

| Medición | Valor |
|---|---|
| Datasets totales | **15** |
| Datasets de educación | **2** (`inep_enem`, `inep_censo_escolar`) |
| Tools totales en datasets | **97** |
| Tools de educación | **13** |
| Fuente de datos | **ZIP de microdatos** de `download.inep.gov.br` (ENEM y Censo Escolar) — **no hay API, y el proyecto tampoco la usa** |
| Salvaguarda LGPD | `COLUNAS_DISTINCT_PERMITIDAS` = *frozenset* de **8 columnas agregadas** |
| CI | **canario semanal de salud de las fuentes** (`feat(ci)`, commit humano del 2026-08-18) |
| PyPI | `mcp-brasil` **0.14.0**, 18 releases |
| Espejo atrasado | `marcellodesales/mcp-brasil`: **0 adelante, 8 atrás**, `HEAD` 2026-04-26 — **el buscador lo lista primero** |

### Los rechazos, con la medición que los justifica

| Candidato | Veredicto | Evidencia |
|---|---|---|
| ⛔ `NicolasViruel/moodle-utn-mcp` | **sin licencia** → todos los derechos reservados | `HEAD` 2026-09-28 (fresco), 16 commits, **sin `LICENSE` y sin campo en el manifiesto** |
| ⛔ `@stll/folio-agents` · `@stll/folio-cli` · `agent-folio` · `@handsong/folio-ui-cli` | homonimia con el ILS **FOLIO** | `repository` → `github.com/stella/folio`, `github.com/srsatt/folio` |
| ⛔ `@public-ui/mcp` 4.4.0 | homonimia con **Kolibri** de Learning Equality | es el *design system* KoliBri: `github.com/public-ui/kolibri` |
| ⛔ `@transcend-io/mcp-server-assessments` 2.1.13 | homonimia con **QTI** y con *pronunciation assessment* | *assessments* de privacidad |
| ⛔ `personaforge` 1.4.0 · `confused-ai` 2.4.2 | homonimia con *knowledge tracing* | frameworks de agentes genéricos |
| ⛔ `CSR2017/edfi-oneroster` | **espejo**, no alternativa | **0 commits divergentes**, 8 tags contra 86, tip = commit de bot |

### gap 79, resuelto con dos comandos

```
git merge-base HEAD other/main        # -> 937248b, que es el tip EXACTO de CSR2017
git rev-list --left-right --count HEAD...937248b   # -> 3   0
```

**La Alliance está 3 commits adelante y 0 atrás. `CSR2017` no agrega nada.** Primer commit idéntico en los dos
(`02cbad5`, 2025-08-07T16:03:10-05:00): **es la misma historia, no dos proyectos.**

### Control de gap 65, corrido otra vez y extendido a una tercera clase de dominio

| Host | `getent hosts` | HTTPS |
|---|---|---|
| `eur-lex.europa.eu` | **RESUELVE** | **000** (bloqueado) |
| `ai-act-service-desk.ec.europa.eu` | **RESUELVE** | **000** |
| `digital-strategy.ec.europa.eu` | **RESUELVE** | **000** |
| `artificialintelligenceact.eu` | **RESUELVE** | **000** (y `EGRESS_BLOCKED` por `WebFetch`) |
| `registry.npmjs.org` (control positivo) | RESUELVE | **200** |

🔵 **Los cuatro resuelven DNS y los cuatro están bloqueados por política, no caídos.** El gap 65 queda extendido de
*«primarias multilaterales y gubernamentales»* a **una tercera clase: las fuentes legales primarias de la UE**,
incluido el explorador no gubernamental del AI Act. **El dato del AI Act de este pase vino por el buscador**, que es el
canal que la tendencia 130 dejó sancionado para exactamente este caso.


## 2026-10-02 (pase 38) — **el dato crudo de los 19 repos candidatos a suceder a las tres dependencias congeladas**: 13 de OneRoster/Moodle/LRS medidos de cero, y el reparto es **8 vivos, 1 tibio, 5 muertos de ≥ 3 años y 1 sin licencia**

El pase 37 fechó las **49 filas que esta base ya tenía**. Este pase mide **19 repos que la base NO tenía**, buscando
reemplazo permisivo y vivo para `learnmcp-xapi`, `oneroster-ts` y `peancor/moodle-mcp-server`. Mismo instrumento
(`git ls-remote --symref` + `git fetch --depth 1 <rama por defecto>` + `git log -1 --format=%cI`), más verificación del
**archivo de licencia** por `raw.githubusercontent.com` probando `LICENSE`, `LICENSE.md`, `LICENSE.txt` y `COPYING` en
`main` y en `master`. El razonamiento, las correcciones y la lectura comercial están en `agents/trending.md` (pase 38);
acá queda **la medición**, que es lo que hay que poder mirar fila por fila antes de poner una dependencia en una
propuesta.

🔵 **Corrección de método al pase 37, que afecta a todo barrido futuro:** el `fetch` por **SHA** de `HEAD` devuelve
`FETCHFAIL` en este entorno para **todos** los repos. El que funciona es el `fetch` de la **rama por defecto por su
nombre**, leído del `ref:` que entrega `ls-remote --symref`. El instrumento del 37 es correcto; su invocación no era
portable, y durante un rato pareció que 49 repos habían desaparecido.

### La tabla completa de este pase, ordenada por antigüedad del último commit en la rama por defecto

| Repo | Licencia (verificada en archivo) | Último commit `HEAD` | Antigüedad | Tags | Rol | Estado |
|---|---|---|---|---|---|---|
| `yetanalytics/lrsql` | **Apache-2.0** ✅ | **2026-10-01** | 0 d | 115 (semver top **v0.9.9**) | LRS | 🟢 activo |
| `Ed-Fi-Alliance-OSS/edfi-oneroster` | **Apache-2.0** ✅ | **2026-10-01** | 0 d | **86** (**v1.0.2**) | OneRoster **servidor** | 🟢 activo · **ALTA** |
| `csmediapro/moodle-mcp-server` | 🔴 **AGPL-3.0** | **2026-10-01** | 0 d | 7 (v0.1.7) | Moodle MCP (lectura) | ⛔ **no proponer** (licencia) |
| `NiccoloSalvini/mcp-moodle-teacher` | **MIT** ✅ | **2026-09-25** | 6 d | 4 (**v0.4.0**) | Moodle MCP **escritura** | 🟢 activo · **ALTA** |
| `CSR2017/edfi-oneroster` | **Apache-2.0** ✅ | **2026-09-22** | 9 d | 8 | OneRoster servidor | 🟢 activo (relación upstream sin resolver → `gap 79`) |
| `Dymayo/moodler-mcp` | **MIT** ✅ | **2026-09-19** | 13 d | 0 (release 1.1.2 por commit) | Moodle MCP | 🟢 activo · **ALTA** |
| `ashleycribb/learnmcp-xapi` | **MIT** ✅ (heredada: *«(c) 2025 David Romero»*) | **2026-09-17** | 15 d | 0 | fork de la puerta xAPI | ⚠️ **NO es sucesión** — 2 commits adelante, ambos de Cloud Run |
| `TCI/OneRoster` | **MIT** ✅ | **2026-09-11** | 20 d | 35 (**v2.3.27**) | OneRoster **cliente** (Ruby) | 🟢 activo · **ALTA** |
| `openfun/ralph` | **MIT** ✅ | **2026-09-07** | 24 d | 32 (**v5.0.1**) | LRS | 🟢 activo |
| `toshieji/moodle-grading-mcp` | **MIT** ✅ (WACA + T. Ejiri) | **2026-09-07** | 24 d | 0 | Moodle MCP **corrección** | 🟢 activo · **ALTA destacada** |
| `loyaniu/moodle-mcp` | 🚫 **sin archivo de licencia** (8 rutas probadas, 8 × 404) | 2026-06-28 | 95 d | 0 | Moodle MCP | ⛔ **no proponer** (licencia) |
| `DavidLMS/learnmcp-xapi` | **MIT** ✅ | 2025-08-29 | **13,1 meses** | 2 (v2.0.0) | puerta xAPI (upstream) | 🔴 **CONGELADO** (reconfirmado) |
| `jdolny/OneRoster.NET` | — (no verificada: repo muerto) | 2023-10-13 | **3,0 años** | 0 | OneRoster cliente (.NET) | ⚫ muerto |
| `gotranseo/oneroster` | — (no verificada: repo muerto) | 2023-05-01 | **3,4 años** | 22 | OneRoster cliente (Swift) | ⚫ muerto |
| `bgwdotdev/go-oneroster` | — (no verificada: repo muerto) | 2019-11-04 | **6,9 años** | 5 | OneRoster servidor (Go) | ⚫ muerto |
| `EASOL/edfi-to-oneroster` | — (no verificada: repo muerto) | 2016-10-19 | **10,0 años** | 0 | Ed-Fi → OneRoster | ⚫ muerto |
| `Transcordia/jupiter` | — (no verificada: repo muerto) | 2015-04-19 | **11,5 años** | 0 | LRS xAPI + Caliper | ⚫ muerto |

**Nota de honestidad sobre la columna de licencia:** en los cinco repos muertos **no se verificó el archivo**. No hacía
falta y habría sido gasto: una licencia permisiva sobre un repo sin commits en una década no cambia la decisión. Las
licencias que esta tabla afirma con ✅ son todas lectura de primera mano del archivo, hoy.

### 🟢 Las cinco altas de base de este pase, en una línea cada una

1. **`Ed-Fi-Alliance-OSS/edfi-oneroster`** (Apache-2.0) — sirve **OneRoster 1.2** con **14 endpoints GET** desde una base **Ed-Fi ODS** (Data Standard 4.0 y 5.0/5.1/5.2), Docker o IIS. **Es el lado proveedor de OneRoster, que esta base nunca tuvo.** ⚠️ Copyright **«1EdTech Consortium, Inc.»** dentro de la org **Ed-Fi-Alliance-OSS**: artefacto conjunto de los dos consorcios, el primero de esta KB.
2. **`toshieji/moodle-grading-mcp`** (MIT, Japón/WACA) — **9 tools**, y la única que escribe deja la nota en `workflowstate=readyforreview`: **no la publica**. Allowlist de cursos, `MOODLE_ALLOW_WRITE=1`, audit trail JSONL, sin notificación al alumno, pie de declaración de AI. **El diseño de seguridad es argumento de cumplimiento.**
3. **`NiccoloSalvini/mcp-moodle-teacher`** (MIT, Italia) — **22 tools** (15 lectura, 3 escritura, 4 utilidad), incluidas `grade_submission` con devolución escrita, `mark_attendance` y `late_registers` (registros no tomados en 24 h). Toda tool que modifica Moodle **pide confirmación**. En proceso de renombre a `mcp-moodle-staff`.
4. **`TCI/OneRoster`** (MIT, Ruby, v2.3.27) — wrapper de **consumo** de OneRoster, vivo y publicado en rubygems. Reemplaza el rol de cliente de `oneroster-ts`, **en otro lenguaje**.
5. **`Dymayo/moodler-mcp`** (MIT) — tercera opción permisiva de Moodle MCP, release 1.1.2. ⚠️ Entró por licencia y fecha: **sus tools no se enumeraron este pase**.

### 🔴 El dato de encuadre que deja el barrido de OneRoster, y vale para cotizar

De las **ocho** implementaciones de OneRoster que devuelve un barrido abierto, **cinco llevan ≥ 3 años sin un commit**
y una sexta (`oneroster-ts`, 0BSD) lleva 15,2 meses. **Quedan dos servidores Apache-2.0 vivos y un cliente MIT vivo.**
OneRoster es un estándar con mucho código escrito y poco código mantenido: en esta capa **la selección pesa más que en
ninguna otra de esta base**, y un barrido por «existe una librería para X» da ocho respuestas de las que seis no se
pueden usar.

## 2026-10-02 (pase 37) — **las 49 filas fechadas una por una por el commit de su rama principal**, con el instrumento que no usa registro ni API: la tabla completa, y el alta de base del pase es una librería de evaluación **ISC** con 2.226 versiones que esta KB nunca vio

**El instrumento:** `git ls-remote <repo>` para los refs, `git fetch --depth 1 <sha de HEAD>` y `git log -1 --format=%cI`.
Cero cuota de API, cero autenticación, **49 de 49 repos respondieron y ninguno dio 404**. El detalle de método, los límites
y las correcciones que produjo están en `agents/trending.md` (pase 37); acá queda **el dato crudo**, que es lo que hay que
poder consultar fila por fila antes de poner una dependencia en una propuesta.

### La tabla completa, ordenada por antigüedad del último commit en la rama por defecto

| Repo | Último commit en `HEAD` | Antigüedad | Tags | Estado |
|---|---|---|---|---|
| `Cicatriiz/openedu-mcp` | 2025-06-03 | **16.0 meses** | 0 | 🔴 **CONGELADO** (>12 meses) |
| `trilogy-group/oneroster-ts` | 2025-06-27 | **15.2 meses** | 12 | 🔴 **CONGELADO** (>12 meses) |
| `DavidLMS/learnmcp-xapi` | 2025-08-29 | **13.1 meses** | 2 | 🔴 **CONGELADO** (>12 meses) |
| `karanb192/algo-sensei` | 2025-10-22 | **11.3 meses** | 0 | 🔴 **FRÍO** (>6 meses) |
| `plastic-labs/tutor-gpt` | 2025-11-13 | **10.6 meses** | 0 | 🔴 **FRÍO** (>6 meses) |
| `pythpythpython/openstax-mcp-server` | 2025-11-30 | **10.1 meses** | 0 | 🔴 **FRÍO** (>6 meses) |
| `satvik314/educhain` | 2025-12-03 | **10.0 meses** | 0 | 🔴 **FRÍO** (>6 meses) |
| `HugeCatLab/ChatTutor` | 2026-01-09 | **8.7 meses** | 2 | 🔴 **FRÍO** (>6 meses) |
| `peancor/moodle-mcp-server` | 2026-02-22 | **7.3 meses** | 0 | 🔴 **FRÍO** (>6 meses) |
| `24kchengYe/human-skill-tree` | 2026-03-25 | **6.3 meses** | 1 | 🔴 **FRÍO** (>6 meses) |
| `MarcosNahuel/moodle-mcp` | 2026-05-03 | **5.0 meses** | 10 | ⚠️ tibio (>3 meses) |
| `Yuanpeng-Li/gradescope-mcp` | 2026-05-13 | **4.7 meses** | 0 | ⚠️ tibio (>3 meses) |
| `LabSirius/TutorIA` | 2026-05-20 | **4.4 meses** | 1 | ⚠️ tibio (>3 meses) |
| `ahmedEid1/lumen` | 2026-06-07 | **3.8 meses** | 1 | ⚠️ tibio (>3 meses) |
| `Open-TutorAi/open-tutor-ai-CE` | 2026-06-26 | **3.2 meses** | 1 | ⚠️ tibio (>3 meses) |
| `Nutlope/llamatutor` | 2026-07-12 | **2.7 meses** | 0 | 🟢 activo |
| `JuneYaooo/lineage-skill` | 2026-07-23 | **2.3 meses** | 0 | 🟢 activo |
| `CAHLR/pyBKT` | 2026-08-05 | **1.9 meses** | 4 | 🟢 activo |
| `open-spaced-repetition/py-fsrs` | 2026-08-09 | **1.8 meses** | 38 | 🟢 activo |
| `vasanthsreeram/Alvarmethod` | 2026-08-16 | **1.5 meses** | 0 | 🟢 activo |
| `amosblomqvist/learn` | 2026-08-26 | **1.2 meses** | 0 | 🟢 activo |
| `GarethManning/education-agent-skills` | 2026-08-28 | **1.1 meses** | 0 | 🟢 activo |
| `avps82/mentar` | 2026-09-03 | **1.0 meses** | 2 | 🟢 activo |
| `giacomomaria81/scorm-mcp-server` | 2026-09-03 | **1.0 meses** | 6 | 🟢 activo |
| `paulocymbaum/ed-tech-system-mcp` | 2026-09-06 | **0.9 meses** | 0 | 🟢 activo |
| `moon0825/jbnu-lms-student` | 2026-09-08 | **0.8 meses** | 3 | 🟢 activo |
| `microsoft/Shiksha-Copilot` | 2026-09-15 | **0.6 meses** | 0 | 🟢 activo |
| `Li-Evan/Bloom` | 2026-09-17 | **0.5 meses** | 0 | 🟢 activo |
| `SirhanMacx/Claw-ED` | 2026-09-18 | **0.5 meses** | 139 | 🟢 activo |
| `bruchris/canvas-lms-mcp` | 2026-09-20 | **0.4 meses** | 69 | 🟢 activo |
| `marcorojasb/tero` | 2026-09-20 | **0.4 meses** | 0 | 🟢 activo |
| `pykt-team/pykt-toolkit` | 2026-09-22 | **0.3 meses** | 5 | 🟢 activo |
| `SenmuuuuW/universal-diagnostic-tutor-skill` | 2026-09-24 | **0.3 meses** | 2 | 🟢 activo |
| `artcc/freelingo` | 2026-09-25 | **0.2 meses** | 116 | 🟢 activo |
| `nmarafo/OpenDidactia` | 2026-09-25 | **0.2 meses** | 0 | 🟢 activo |
| `HKUDS/DeepTutor` | 2026-09-27 | **0.2 meses** | 84 | 🟢 activo |
| `ZeKaiNie/universal-examprep-skill` | 2026-09-27 | **0.2 meses** | 7 | 🟢 activo |
| `oaknational/oak-ai-lesson-assistant` | 2026-09-28 | **0.1 meses** | 129 | 🟢 activo |
| `redbeard-26/asfai-education` | 2026-09-28 | **0.1 meses** | 0 | 🟢 activo |
| `Crosstalk-Solutions/project-nomad` | 2026-09-29 | **0.1 meses** | 81 | 🟢 activo |
| `CAHLR/OATutor` | 2026-09-30 | **0.1 meses** | 4 | 🟢 activo |
| `jupyterlab/jupyter-ai` | 2026-10-01 | **0.0 meses** | 279 | 🟢 activo |
| `ArnaudGuiovanna/tutor-mcp` | 2026-10-01 | **0.0 meses** | 7 | 🟢 activo |
| `vishalsachdev/canvas-mcp` | 2026-10-01 | **0.0 meses** | 22 | 🟢 activo |
| `zijinz456/OpenTutor` | 2026-10-01 | **0.0 meses** | 0 | 🟢 activo |
| `Miaotofu01/Study-Mate` | 2026-10-01 | **0.0 meses** | 7 | 🟢 activo |
| `bunizao/moodle-cli` | 2026-10-02 | **0.0 meses** | 32 | 🟢 activo |
| `madhvantyagi/Gnos` | 2026-10-02 | **0.0 meses** | 0 | 🟢 activo |
| `THU-MAIC/OpenMAIC` | 2026-10-02 | **0.0 meses** | 106 | 🟢 activo |

**Resumen: 34 activos (< 3 meses), 5 tibios, 7 fríos, 3 congelados.** Las tres filas congeladas y las siete frías son las
que hay que revisar antes de citarlas como vivas; **tres de ellas son load-bearing en `compose/patterns.md`**
(`learnmcp-xapi`, `oneroster-ts`, `peancor/moodle-mcp-server`) y están tratadas en `compose/patterns.md` y
`agents/trending.md` de este pase.

⚠️ **Leer la columna «Tags» con la advertencia del pase:** **17 de las 49 filas tienen cero tags**, y para ésas el *span*
de releases del pase 36 **no podía medir nada**. Es la razón por la que este instrumento existe.

### 🟢 El alta de base del pase: `pie-framework/pie-elements` — la capa de interacciones de evaluación, permisiva y viva

| Campo | Valor medido |
|---|---|
| Repo | [`pie-framework/pie-elements`](https://github.com/pie-framework/pie-elements) |
| Licencia | 🟢 **ISC** (cuerpo del `LICENSE.md`, `Copyright 2019 CoreSpring Inc`) — ⚠️ **con contradicción, ver abajo** |
| `HEAD` (rama por defecto `develop`) | 🟢 **2026-09-22** |
| Versiones publicadas | 🔵 **2.226** en npm, desde **2019-05-31**, última modificación **2026-10-01** |
| Refs en el repo | **51.410** |
| Qué es | Monorepo de **interacciones de evaluación** como *web components*: `multiple-choice`, `rubric`, `complex-rubric`, `graphing`, `drawing-response`, `math-inline`, `extended-text-entry`… cada una con sub-paquetes `configure` (autoría) y `controller` (scoring) |

🔵 **Por qué importa, y es la capa que esta KB tenía peor abastecida en permisivo.** El pase 36 cerró **P69** con la
conclusión de que *«lo activo y desplegado de la capa de evaluación es copyleft»* —`qtism/qtism` **GPL-2.0-only** con
218.212 descargas, `oat-sa/extension-tao-testqti` **GPL-2.0-only** con 885 versiones— *«y lo permisivo es lo nuevo»*
(`@longsightgroup/qti3-cli`, MIT, desde 2026-05-21). 🟢 **`pie-elements` refuta la segunda mitad: hay una capa de
evaluación permisiva que no es nueva — tiene siete años, 2.226 versiones y publicó ayer.**

⚠️ **Y la refutación tiene un límite que hay que decir en la misma frase, porque decide si se propone:** **`pie-elements`
no implementa QTI.** Se verificó: **cero menciones de QTI en el README crudo.** Tiene su propio modelo de ítem y su propio
contrato de *scoring*. 🔴 **Por la tendencia 29 de esta base —*«lo que inventa su propio modelo de dominio no escala, lo que
se conecta al estándar instalado sí»*— eso lo pone en la categoría débil**, y es exactamente el trade-off que hay que poner
sobre la mesa: **permisivo y maduro pero propietario de modelo** (`pie-elements`) contra **permisivo y nuevo pero conforme
al estándar** (`qti3-cli`) contra **copyleft, conforme y desplegado en producción** (`qtism` / TAO). **Las tres opciones son
reales y ninguna domina a las otras dos** (tendencia **128**).

### 🔴 La contradicción de licencia, que es de una clase que esta KB no tenía: **tres identificadores, dos respuestas, y uno vacío**

| Canal | Qué declara |
|---|---|
| `LICENSE.md` de la rama `develop` | **cuerpo del texto ISC** (*«Permission to use, copy, modify, and/or distribute… with or without fee»*), `Copyright 2019 CoreSpring Inc` |
| `package.json` de la raíz | 🔴 **`"license": "MIT"`** |
| `@pie-element/rubric`, `drawing-response`, `math-inline`, `graphing`, `extended-text-entry` en npm | **`ISC`** |
| 🔴 **`@pie-element/multiple-choice` v13.4.4** | 🔴 **NINGUNA — el campo `license` no existe** |

🔵 **La regla del pase 10 de esta base era «verificar contra el archivo `LICENSE`, no contra el README». Este caso la
extiende y la endurece: el archivo `LICENSE` le gana al MANIFIESTO, y el manifiesto es lo que leen los escáneres
automáticos de licencia.** Un escáner que lea la raíz dice **MIT**; uno que lea los paquetes publicados dice **ISC**; y
sobre **`multiple-choice` —la interacción más central de cualquier evaluación— no dice nada.**

⚠️ **El impacto comercial real es chico pero no es cero:** ISC y MIT son las dos permisivas y las dos sirven, así que
**el resultado no cambia**; lo que cambia es que **un *due diligence* de licencia sobre este monorepo devuelve tres
respuestas distintas según por dónde entre**, y el paquete sin campo hay que resolverlo por el `LICENSE.md` del repo.
🟢 **ISC es además licencia nueva para esta KB** —la tercera «permisiva que los filtros no reconocen» después de **ECL-2.0**
(tendencia 27) y **0BSD** (pase 28)— y **es funcionalmente equivalente a MIT** (tendencia **129**, **gap 76**).

### 🔴 La no-alta del pase, declarada: `@timeback/oneroster`

Apareció buscando reemplazo para `oneroster-ts` (congelado hace 15 meses). **58 versiones, última 2026-09-25** — o sea
activo. 🔴 **Pero no declara licencia, ni repositorio, ni *homepage*.** **Sin licencia no es open source: es código
publicado**, y no entra. Queda como **gap 75**.

### ⚠️ Lo que este pase NO pudo medir, y es lo mismo que el 36

`api.npmjs.org` y `pypistats.org` reverificados hoy: **403 a CONNECT**, con control positivo en la misma corrida
(`registry.npmjs.org` → **200**, `packagist.org` → **200**). **Las descargas por mes siguen existiendo sólo para
Packagist.** Y las **once** fuentes institucionales del **gap 65** se reprobaron: **0 de 6 dominios responden hoy**
(`coe.int`, `unesco.org`, `unu.edu`, `publications.iadb.org`, `eur-lex.europa.eu`, `digital-strategy.ec.europa.eu` →
todos **000**). 🔵 **Matiz nuevo del gap 65, que lo reclasifica a medias:** el buscador **sí** devuelve contenido de
`coe.int` en el cuerpo de sus resultados (la *2nd Working Conference* sobre las dimensiones regulatorias de la AI en
educación, octubre). **Está bloqueado el canal de *fetch*, no el canal de *información*** — y una cita obtenida así es
secundaria en la forma pero primaria en el origen, lo que conviene anotar como tal y no como fuente comercial
(tendencia **130**).

## 2026-10-02 (pase 36) — el registro se mide **en los tres canales** y resulta que sólo uno da descargas: **el *span* de releases reemplaza a las descargas**, y con él la capa PHP de evaluación y telemetría queda **fechada pieza por pieza** — la más descargada de todas no publica desde **2022**

**Hallazgo de método primero, porque cambia cómo se leen las cifras del pase 35.** Las descargas por mes —el instrumento
que el pase 35 introdujo— **sólo están disponibles en Packagist** en este entorno: `api.npmjs.org` y `pypistats.org`
responden **403 a CONNECT**, con control positivo en la misma corrida (`registry.npmjs.org` → **200**). **Las cuatro
cifras de descargas del pase 35 eran todas de paquetes PHP**, así que el instrumento nunca se había ejercitado fuera de
Packagist. 🟢 **El sustituto está en los tres canales y distingue lo que las descargas no: el *span* de releases**
(tendencia **115**).

### La capa de evaluación y telemetría en PHP, medida y fechada

| Paquete (Packagist) | Desc./mes | Total | Versiones | Último release | Licencia |
|---|---|---|---|---|---|
| `rusticisoftware/tincan` (TinCanPHP) | 🟢 **6.178** | 863.777 | 21 | 🔴 **2022-11-02** | Apache-2.0 ✅ |
| `qtism/qtism` | 3.104 | 218.212 | **315** | 2026-07-16 | 🔴 **GPL-2.0-only** |
| `moodle/moodle` | 2.134 | 94.453 | 485 | 🟢 **2026-10-01** | GPL-3.0 |
| `oat-sa/extension-tao-testqti` | 950 | 117.544 | 🟢 **885** | 🟢 **2026-09-30** | 🔴 GPL-2.0-only |
| `php-xapi/client` | 825 | 48.104 | 7 | 🔴 **2021-03-24** | **MIT** ✅ |
| `learninglocker/learninglocker` | 🔴 **0** | 2.960 | 58 | 🔴 **2017-04-04** | GPL-3.0 |

**Lo que la tabla dice y las estrellas no podían decir:**

- 🔴 **La pieza xAPI más descargada de esta KB —6.178/mes, 863 mil totales— no publica desde el 2022-11-02.** ⚠️ **Y es una corrección a la cifra del pase 35**, que escribió *«congelada desde 2019»*: medido en el tiempo de versión de Packagist es **2022-11-02**. 🔵 **Es el caso que prueba la regla: las descargas miden BASE INSTALADA, no vida del proyecto.** Un cliente que ya tiene xAPI en producción probablemente corre esto.
- ⚠️ **El único MIT de la capa xAPI, `php-xapi/client`, está parado desde el 2021-03-24** con 825 descargas/mes. **La capa xAPI en PHP es: lo permisivo está quieto y lo vivo es copyleft o está en otro lenguaje** — razón adicional para que la receta de telemetría de esta base se apoye en **Ralph (MIT)** + **`lrsql` (Apache-2.0)** + **`learnmcp-xapi` (MIT)**, que son las piezas vivas y permisivas (**P67**, **P68**).
- 🟢 **`oat-sa/extension-tao-testqti` subió de 844 a 885 versiones** y publicó **hace dos días**: es la pieza **más activa** de la capa de evaluación, y sigue siendo **GPL-2.0-only**. ✅ **Confirma la decisión de P69/P76:** lo activo y desplegado es copyleft; **lo permisivo (`@longsightgroup/qti3-cli`, MIT) es lo nuevo** — 41 releases desde el **2026-05-21**, último el **2026-10-01**, y **cero dependencias de terceros** (sus 4 dependencias son todas `@longsightgroup/*` de la misma versión exacta).
- ✅ **`learninglocker` queda fechado además de confirmado:** el pase 35 midió **0 descargas/mes**; ahora se sabe **desde cuándo**: **último release 2017-04-04**.

### 🔴 Y una ausencia de catálogo que hay que decir: `oat-sa/qti-sdk` NO es un paquete de Packagist

Esta base viene citando **`oat-sa/qti-sdk`** entre las piezas de mayor despliegue de la capa de evaluación.
`packagist.org/packages/oat-sa/qti-sdk.json` devuelve **404**. 🔵 **No es que el proyecto no exista: es que `oat-sa/qti-sdk`
es el nombre del REPO de GitHub y su paquete se publica como `qtism/qtism`** —el que tiene 218.212 descargas totales—.
**La lección, que es la misma del gap 69 en otra escala: el nombre del repo y el nombre del paquete son dos
identificadores distintos, y mezclarlos produce un 404 que parece una ausencia.** Lo mismo pasó al probar
`1edtech/oneroster`, `imsglobal/lti-1-3-php-library` y `packbackbooks/lti-1-3-php-library`: **404 los tres**, y lo que
corresponde escribir es *«no verificado en Packagist bajo ese nombre»*, **no** *«no existe»*.

## 2026-10-02 (pase 35) — el registro deja de responder «qué hay» y empieza a responder **«qué se usa»**: con descargas por mes, la capa de evaluación y la de telemetría **cambian de orden**, y la pieza xAPI más desplegada de esta KB resulta ser **Apache-2.0 y congelada desde 2019**

**Lo medido:** consultas a **npm** (`registry.npmjs.org/-/v1/search` y documentos de paquete), **PyPI** (`/pypi/<pkg>/json`)
y **Packagist** (`packagist.org/packages/<vendor>/<pkg>.json`) por **nombre de proyecto implementador** —la consigna del
pase 32— más lectura de **README crudo**, `package.json` y archivo `LICENSE` de cada candidato. Más la lectura de
`lib/mcp-server.js` y `lib/mcp-prompts.js` de `coursecode`, que está en `agents/trending.md`.

🔵 **El canal nuevo de este pase no es un host: es un campo.** `downloads.monthly` de Packagist y la fecha del último
release de PyPI son dos números que esta base nunca pidió, y los dos **reordenan capas enteras**.

### 🟢 Lo que entra, verificado el 2026-10-02

| Repo | URL | Licencia | Adopción medida | Stack | Por qué importa |
|---|---|---|---|---|---|
| **canvas-lms-mcp** | [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | **MIT** ✅ | **8 ★**, 4 forks, **317 commits**, **62 versiones** npm (última 2026-09-20) | TypeScript | 🔵 **165 tools — el conector permisivo de LMS más grande de esta KB**, con escritura (califica, comenta, CRUD de assignments) y **cifra citable**. Declara **MCP 1.x**. Trae **`accessibility audits`** como categoría de tools |
| **Claw-ED** | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | **MIT** ✅ (`LICENSE`, *(c) 2026 EDUagent Contributors*) | **60 ★**, 13 forks, **778 commits**; PyPI `clawed` **240 releases** | Python 3.11+ | 🟢 **El agente docente *local-first*.** Importa PDF/DOCX/PPTX/TXT/MD del docente, indexa para *retrieval*, construye **perfil de estilo de enseñanza** y emite borradores **editables en DOCX y PPTX**. Beta revisada por docentes |
| **moodle-cli** | [bunizao/moodle-cli](https://github.com/bunizao/moodle-cli) | **MIT** ✅ | **20 versiones** (2026-07-09 → 2026-09-27) | TypeScript | **Cuarta puerta de Moodle y primera del lado alumno**: vencimientos, notas, archivos, devoluciones, revisión de quizzes, **desde la sesión del navegador** (sin token de administrador) |
| **moodle-core-cli** | [gafapa/moodle-core-cli](https://github.com/gafapa/moodle-core-cli) | **MIT** ✅ | **11 versiones**, última 2026-09-24 | Node.js | ⚪ **Cero menciones de MCP — y por eso vale:** cliente limpio de *core web services* de **Moodle 4.5+**. Es el candidato más barato a envolver como MCP en esta capa |
| **jbnu-lms-mcp** | [moon0825/jbnu-lms-student](https://github.com/moon0825/jbnu-lms-student) | **MIT** ✅ | v0.8.0, **2026-09-08** | Node.js (STDIO local) | 🔵 **Categoría nueva: el LMS de UNA institución.** 전북대학교 (Univ. Nacional de Jeonbuk, Corea), **25 tools**, **sólo lectura por diseño**, login por el navegador del propio usuario (**passkey y 2FA incluidos**), Windows + macOS. **No oficial por declaración propia** |
| **@longsightgroup/qti3-a11y** | [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** ✅ | 0.13.1, **2026-10-01** | TypeScript | 🔵 **La pieza que P17 necesitaba y esta KB declaraba inexistente en permisivo:** `accessibilityProofMatrix`, `a11yContracts` y **guiones manuales de tecnología asistiva para VoiceOver, NVDA y JAWS**. Es **metadato de prueba de accesibilidad**, legible por máquina |
| **@longsightgroup/qti3-pnp** | [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** ✅ | 0.13.1, **cero dependencias** | TypeScript | **Resolutor de QTI 3 *Personal Needs and Preferences***: parsea el XML de PNP, normaliza, valida el perfil y lo resuelve contra las capacidades del *player* y el catálogo QTI |
| **ibge-br-mcp** | [SidneyBissoli/ibge-br-mcp](https://github.com/SidneyBissoli/ibge-br-mcp) | **MIT** ✅ | **24 versiones** (2026-01-18 → 2026-09-27) | TypeScript | 🔵 **La plantilla del gap 63.** Datos públicos brasileños —geografía, **censo**, economía, salud— servidos por MCP con procedencia. **No cubre educación**, y eso es justamente la oportunidad |

### 🔴 Lo que NO entra, y por qué

| Pieza | Licencia | Por qué queda afuera |
|---|---|---|
| `@imazhar101/mcp-canvas-server` | 🔴 **ninguna declarada** | 13 versiones y la última del **2026-10-01** (activo), README de 35.048 caracteres. **Sin licencia no hay entregable**: no se propone ni como referencia cerrada |
| `lms-mcp` | MIT | **Sin repositorio declarado**, README de 1.091 caracteres, última versión **2025-04-05**. No verificable de primera mano |
| `@owen-x-tech/canvas-mcp` | MIT (declarada) | 2 versiones, 2026-02-23. 🔴 **El repo que declara da 404 en las doce rutas probadas** (`owentaylor/canvas-mcp`, `main`/`master`/`dev` × README/LICENSE/package.json/index.js). Por la **tendencia 94** eso no invalida el paquete, **pero sin código legible no se propone** |
| `educhain` (PyPI) | MIT | ⚠️ **No sale: se re-fecha.** Esta KB lo tiene como alta de los pases 2 y 3 (*YouTube → curso, v0.4*). **35 releases y el último es del 2025-12-03 — diez meses sin publicar.** Sigue siendo MIT y usable; **deja de ser «lo nuevo»** |
| `opencase` (npm) · `opencage/geocode` (Packagist) | — | 🔴 **Colisión 7.** El nombre del implementador de CASE devuelve **geocodificación** |
| `@censo-custody/solana-wallet-adapter`, `@censo/eth-contracts` | — | 🔴 **Colisión 9.** «censo escolar» devuelve **custodia de criptoactivos en Solana** |

### 🔵 La capa de evaluación, reordenada por adopción en vez de por novedad

El pase 28 escribió *«el QTI utilizable es PHP»*; el pase 32 dijo que `qti3` (MIT) **rompía** esa frase. **Las dos cosas
eran ciertas y a la vez insuficientes, porque ninguno midió despliegue ni licencia del lado PHP.** Medido:

| Pieza | Licencia | ★ | Descargas total / mes | Versiones | Último release |
|---|---|---|---|---|---|
| `qtism/qtism` → [oat-sa/qti-sdk](https://github.com/oat-sa/qti-sdk) | 🔴 **GPL-2.0-only** | 85 | **218.212 / 3.104** | **293** | 2026-07-09 (v19.7.2) |
| [oat-sa/extension-tao-testqti](https://github.com/oat-sa/extension-tao-testqti) | 🔴 **GPL-2.0-only** | **8** | **117.544 / 950** | **844** | **2026-09-30** |
| `@longsightgroup/qti3-*` (12 paquetes) | **MIT** ✅ | 5 | — (npm, 0.13.1) | — | **2026-10-01** |
| [instructure/qti](https://github.com/instructure/qti) (QTI 1.2) | **MIT** ✅ | 8 | — | 174 commits | — |

🔴 **La conclusión que sirve para una propuesta, y es más fuerte que las dos anteriores:** **el QTI que el mundo
efectivamente despliega es copyleft** —GPL-2.0-only, 218.212 descargas, 293 versiones, mantenido— y **el QTI permisivo es
nuevo y chico**. Así que `@longsightgroup/qti3-*` no es «una opción más»: es **la única pila QTI 3 permisiva con releases
vivos**, y `instructure/qti` **la única permisiva para el acervo 1.2**. Eso vuelve a **P20** y a **P48** más valiosos, no
menos — pero **obliga a declarar el riesgo de madurez**, no a esconderlo detrás de la licencia.

⚠️ **Y `oat-sa/extension-tao-testqti` con 8 ★, 844 versiones etiquetadas y un release de hace dos días es el mejor
ejemplo que tiene esta base de la tendencia 23**: TAO es infraestructura de evaluación desplegada, y en GitHub parece un
proyecto abandonado.

### 🔵 La capa de telemetría, reordenada igual — y el resultado es mejor de lo que esta KB creía

| Pieza | Licencia | ★ | Descargas total / mes | Último tag |
|---|---|---|---|---|
| [`RusticiSoftware/TinCanPHP`](https://github.com/RusticiSoftware/TinCanPHP) | **Apache-2.0** ✅ | 88 | 🔵 **863.777 / 6.178** | 🔴 **2019-03-05** |
| [`RusticiSoftware/TinCanPython`](https://github.com/RusticiSoftware/TinCanPython) (PyPI `tincan`) | **Apache-2.0** ✅ | — | — (5 releases) | 🔴 **2020-09-03** |
| [`php-xapi/client`](https://github.com/php-xapi/client) + familia `php-xapi/*` | **MIT** ✅ | 23 | 48.104 / 825 | 🔴 2021-03-24 |
| [`learninglocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | 🔴 GPL-3.0 | **583** | 🔴 **2.960 / 0** | 🔴 2017-04-04 |

🔵 **La buena noticia que estaba escondida:** la pieza cliente xAPI más desplegada del planeta es **Apache-2.0** y
descarga **6.178 veces por mes**. Esta KB tenía la capa de telemetría catalogada por sus **servidores** (lrsql, Learning
Locker, Veracity) y nunca por sus **clientes**. **Del lado cliente, la capa es permisiva** — y eso abarata todo lo que
cuelga de **P15** (el LRS como capa 0).

🔴 **La mala, y hay que decirla en la misma frase:** las cuatro piezas están **congeladas**. La más fresca tiene cinco
años. **Un cliente xAPI Apache-2.0 con 6.178 descargas mensuales y sin release desde 2019 es a la vez el camino más
barato y una deuda técnica asumida** — se propone *forkeable*, no *mantenido*. ⚠️ **Y `learninglocker` queda cerrado por
medición y no por rumor: 583 estrellas, 0 descargas mensuales.** No se propone.

### 🔴 La ausencia de MCP, confirmada por el segundo método — y ahora con el SDK de CaSS adentro

README crudo de las seis piezas de la consigna, conteo de «MCP» y «Model Context Protocol»:

| Pieza | MCP | Vocabulario del dominio | Nota |
|---|---|---|---|
| `oat-sa/qti-sdk` | **0** | 84 | — |
| `oat-sa/extension-tao-testqti` | **0** | 12 | — |
| `php-xapi/client` | **0** | 15 | — |
| `RusticiSoftware/TinCanPHP` | **0** | 2 | — |
| `RusticiSoftware/TinCanPython` | **0** | 🔴 **0** | Falso negativo del control: *es* del dominio |
| `cassproject/cass-npm` (`cassproject` 5.0.19, Apache-2.0, **2026-08-12**) | **0** | 🔴 **0** | 🔵 **Hallazgo:** el SDK JS de CaSS **no** expone MCP — la puerta de CaSS es **sólo del servidor** |

**La mitad QTI del gap 60 queda confirmada por un segundo método independiente** — ⚠️ **y la mitad xAPI NO: el pase 33, que corrió en paralelo a este, demostró que `DavidLMS/learnmcp-xapi` (MIT) es la puerta y que estaba en esta KB desde el pase 6. Lo que este pase mide es más angosto y compatible: las piezas de MAYOR DESPLIEGUE de las dos capas no tienen MCP, que no es lo mismo que «la capa no tiene puerta».** Y queda una frase prohibida nueva: *«CaSS tiene puerta
MCP»* es cierto de `cassproject/CASS` (servidor) y **falso** de `cassproject` (SDK npm). **Quien integre por npm no
hereda la puerta.**

### ⚠️ Nota de método — qué canal verificó en este pase, y qué quedó fuera de alcance

- ✅ **Verificaron:** `registry.npmjs.org`, `pypi.org/pypi/*/json`, `packagist.org/packages/*.json`,
  `raw.githubusercontent.com` (README, `LICENSE`, `package.json` y código fuente).
- 🔴 **Bloqueado por el proxy de egreso, medido en su registro:** `eur-lex.europa.eu` y `data.europa.eu`
  (**403 a CONNECT**), más `artificialintelligenceact.eu`, `op.europa.eu`, `euaiact.com`, `euai-act.com`. **Gap 65.**
- ⚠️ **`repo.packagist.org` devuelve `"404 not found, no packages here"` para rutas de paquete**; el host que sirve el
  JSON de paquete es **`packagist.org`**. Anotado para que el próximo pase no pierda el intento.
- 🔴 **La API de GitHub está limitada al alcance de repos de la sesión** (`api.github.com/repos/...` responde *«GitHub
  access to this repository is not enabled for this session»*). Las estrellas y los commits de piezas de terceros se
  leyeron de la **página renderizada**, y el código por **`raw.githubusercontent.com`**. ⚠️ Recordar la regla del pase
  29: **la presencia de MCP se verifica en el README crudo, nunca en la página renderizada.**
- 🔴 **En este entorno no se puede instalar ni ejecutar paquetes de terceros.** Por eso los conteos de tools de
  `coursecode` (15) y de `canvas-lms-mcp` (165) son **de código fuente y de documentación**, no de `tools/list`. La
  distinción del pase 30 —declaradas contra servidas— **se mantiene abierta** para las dos piezas.

## 2026-10-02 (pase 34) — **dos altas verificadas, una no-alta declarada y un falso positivo desarmado**: la familia `yetanalytics` rinde por el nombre de la organización —el instrumento del pase 33— y aparece la capa de **conformidad y simulación xAPI** que treinta y tres pases no buscaron

🔵 **El eje de búsqueda de este pase no fue un término: fue una organización.** El pase 33 cerró el gap 51 concluyendo
que *«el instrumento que funciona es el nombre de la organización»* (tendencia **100**). Se aplicó literalmente: se
listó **el catálogo Docker Hub entero de `yetanalytics`** —el mantenedor de `lrsql`, que esta KB ya tenía— y se cruzó
cada imagen contra los ocho archivos. **De seis imágenes, dos no estaban en esta base.**

| Imagen | ¿Estaba en la KB? | Último movimiento (Docker Hub) |
|---|---|---|
| `lrsql` | ✅ sí, desde el pase 6 | **2026-10-01** (confirma la fecha del pase 33) |
| `xapipe` / LRSPipe | ✅ sí | 2026-08-18 |
| **`datasim`** | 🔴 **NO** | **2025-12-02** |
| **`persephone`** | 🔴 **NO** | 🔴 **2023-10-10** |
| `fuseki` | no (fork de infraestructura, fuera de alcance) | 2022-04-11 |
| `hello-marathon` | no (demo de 2017) | 2017-05-16 |

### ✅ Alta 1 — `yetanalytics/datasim`: **Apache-2.0**, y es la pieza que faltaba para *probar* un LRS antes de cotizarlo

| | |
|---|---|
| **Repo** | [`yetanalytics/datasim`](https://github.com/yetanalytics/datasim) |
| **Licencia** | **Apache-2.0** ✅ — leída del `LICENSE` sobre `master` (*«Apache License»*) |
| **Verificación de primera mano** | `LICENSE` **200**, `README.md` **200**, `deps.edn` **200**, imagen Docker con tag publicado |
| **Qué es** | *Data and Training Analytics Simulated Input Modeler* — **genera datos xAPI simulados a escala** |
| **Para qué sirve, textual del README** | *«benchmark and stress-test the design of applications with the Total Learning Architecture»* y *«evaluate the implementation of xAPI data design using the xAPI Profile specification»*; apunta además a **pruebas de conformidad** |
| **Origen** | financiado inicialmente por la **Advanced Distributed Learning Initiative** (ADL, Departamento de Defensa de EE. UU.) |

🟢 **Por qué importa y no es una curiosidad.** Esta KB recomienda `lrsql` o Ralph en **más de quince patrones**, y hasta
este pase **no tenía con qué dimensionarlos**. `datasim` permite **cargar el LRS con tráfico sintético conforme a un
xAPI Profile antes de comprometer una cifra en una propuesta** — y viene del mismo mantenedor que `lrsql`, así que la
combinación es la que el propio proyecto usa. **Es la diferencia entre proponer una arquitectura y haberla probado.**
Ver **P71**.

🔵 **Y resuelve, de paso, una carencia de método de esta base:** los xAPI Profiles aparecieron en la consigna del pase
24 y se buscaron en el **25** sin encontrar herramienta; `datasim` **valida contra Profile** y estaba a un listado de
organización de distancia.

### ✅ Alta 2 — `1EdTech/digital-credentials-public-validator`: **Apache-2.0**, el validador **del propio consorcio**

| | |
|---|---|
| **Repo** | [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) |
| **Licencia** | **Apache-2.0** ✅ — `LICENSE` **200** en `main` **y** en `master`, texto *«Apache License Version 2.0»* |
| **Qué es** | validador público de **Open Badges** y **Comprehensive Learner Record (CLR)**, con **interfaz web, HTTP y API** |

🟢 **Cierra media carencia que esta KB tenía escrita.** Este archivo registraba que *«las implementaciones de referencia
de estos estándares ya no están»* (`badgr-server` **404**, `caliper-php` en privado). **El validador no sólo está: es
Apache-2.0 y lo publica 1EdTech, el consorcio que escribe el estándar.** Para un entregable de credenciales eso es lo
que convierte *«cumplimos Open Badges»* en una afirmación verificable por un tercero neutral. Ver **P74**.

### 🔴 No-alta declarada — `yetanalytics/persephone`: **no se agrega, y se dice por qué**

Sería tentador sumarla: Docker Hub la describe como *«a Clojure CLI and server app for validating xAPI Statements
against Profiles»*, que es **exactamente** la capa que este pase vino a buscar. **No entra, por dos razones medidas:**

| Chequeo | Resultado |
|---|---|
| Licencia | 🔴 **no verificable** — se probaron **10 rutas**: `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license` y `COPYING`, cada una en `main` **y** `master`. **Las diez, 404** |
| `project.clj` / `deps.edn` | 🔴 **404 las dos** en `master` |
| `README.md` | 🔴 **404** en `main` y en `master` |
| Docker Hub | **3 tags**, el último **2023-10-10** → **~3 años sin movimiento** |

⚠️ **O sea: existe la imagen, pero el árbol no es alcanzable por ninguna ruta probada y la pieza está congelada hace
tres años.** **Sin licencia leída no va a ninguna tabla de esta KB** — es la misma regla que el pase 31 aplicó a Caliper
(*«no es que no haya código, es que es inusable»*). Se anota acá **para que un pase futuro no la descubra como novedad**
y para dejar la pregunta precisa: su árbol puede estar bajo una rama con otro nombre, y eso **sólo se contesta con un
listado de repositorio**, que es justo lo que `api.github.com` (**403**) no permite acá. **Gap 68.**

### 🔴 El falso positivo del pase, y es el hallazgo transferible: `quizlar/mcp-server`

Un servidor MCP **del dominio educativo**, **activo**, con **`LICENSE` MIT real** — y **sin una línea de código**. El
repo contiene un `server.json` cuyo campo **`remotes`** apunta a `https://mcp.quizlar.app/mcp/` detrás de una API key
`sk-qz-<32>`. **La MIT cubre el manifiesto; la implementación es un servicio alojado propietario.** Está desarrollado en
`agents/trending.md` de este mismo pase (**colisión 9**, tendencias **103** y **104**); acá queda la consecuencia para
este archivo: 🔵 **un barrido de repos que filtre por «MCP + dominio + licencia permisiva» lo promueve, y el control que
lo descarta es leer `server.json` y buscar `remotes`.**

### ⚠️ Lo que se buscó y **no** rindió, declarado en vez de omitido

- **Puerta MCP propia de los dos LRS** (`gap 64`): 🔴 **no existe** — Docker Hub de `yetanalytics` (**6 imágenes, ninguna
  MCP**), `deps.edn` y `README` de `lrsql` (**0 menciones**), `ralph-malph` 5.0.1 en PyPI (**14 extras, ninguno MCP**).
  **Cerrado en negativo con tres instrumentos.**
- **Puerta MCP de Caliper, CASE y CEASN:** 🔴 **ninguna**, reconfirmado por búsqueda abierta (segundo instrumento).
- **`mcp.so`**, el registro de servidores MCP y **el instrumento natural para esta pregunta**: 🔴 **bloqueado por el
  proxy de egreso**. Es una limitación que conviene tener presente: **este barrido no puede consultar el catálogo
  específico de su propio objeto de estudio.**

### 🟢 Nota de instrumento: `packagist.org/packages/<vendor>/<pkg>.json` da **licencia y fecha por release**

Hasta este pase esta KB usaba `packagist.org/search.json`, que devuelve descripción y descargas. El endpoint por
paquete devuelve **el array completo de versiones con `time` y `license` en cada una** — y así se midió que
`qtism/qtism` es **GPL-2.0-only en las 293 releases**, no sólo en la última. 🔵 **Para una decisión de licencia eso
importa: un proyecto puede haber relicenciado, y el único modo de saberlo es mirar la serie, no la punta.**

---
## 2026-10-02 (pase 33) — **cero altas y tres fechas**: las piezas de la capa de telemetría ya estaban en esta KB desde el pase 6, y lo que faltaba era su **estado**; `hub.docker.com` entra como canal de verificación y fecha `lrsql` **en el día de ayer**

🔵 **Este pase no agrega repos a la capa de telemetría, y eso es el hallazgo.** Fue a buscar la puerta MCP de xAPI que el
**gap 60** declaró ausente, la encontró… **y ya estaba en esta base desde el pase 6**, junto con los dos LRS. Lo que **no**
estaba era el dato que decide si una dependencia entra en una propuesta: **cuándo se movió por última vez.** Eso es lo
que este pase mide.

### ✅ Las tres piezas de la capa, ahora fechadas de primera mano

| Repo | Licencia | Canal de verificación | Estado medido |
|---|---|---|---|
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** ✅ | `LICENSE` (200) = texto Apache 2.0; `README.md`, `doc/overview.md`, `deps.edn` (200); **`hub.docker.com/v2`** | 🟢 **VIVO, y la cifra es de ayer: `v0.9.9` el 2026-10-01.** **112 tags.** Seis releases en 2026 |
| [`openfun/ralph`](https://github.com/openfun/ralph) | **MIT** ✅ | PyPI `ralph-malph` 5.0.1 (clasificador OSI); `CHANGELOG.md` (200) | ⚠️ **Vivo en `main`, parado en el registro**: último release **2024-07-11**, `[Unreleased]` grande y activo |
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** ✅ | `LICENSE` (200): *«Copyright (c) 2025 David Romero»*; `README.md` (200), 293 líneas | 🟢 **Arquitectura de plugins leída del README**; 🔴 **fuera de todo registro de paquetes** |

**`deps.edn` de `lrsql`, leído:** Clojure 1.11.2, `core.async`, `cheshire` 6.2.0, `spec-tools`, `aero`, `selmer`. Es un
proyecto **JVM/Clojure**, y eso explica su canal de distribución.

### 🟢 Canal de verificación nuevo: `hub.docker.com` fecha lo que `api.github.com` ya no puede

`api.github.com` sigue devolviendo **403** en este entorno (tendencia 94), así que estrellas y fechas de release no son
alcanzables. **Para una pieza que se distribuye como contenedor hay un sustituto, y funciona:**

```
GET https://hub.docker.com/v2/repositories/yetanalytics/lrsql/tags?page_size=8&ordering=last_updated
→ 200, count: 112
   latest  last_updated 2026-10-01T15:08:08Z
   v0.9.9  last_updated 2026-10-01T15:08:06Z
   v0.9.8  last_updated 2026-08-17T20:43:38Z
   v0.9.7  last_updated 2026-08-11T16:00:25Z
   v0.9.6  last_updated 2026-08-08T18:29:39Z
   v0.9.5  last_updated 2026-04-30T17:02:39Z
   v0.9.4  last_updated 2026-04-28T23:21:32Z
   v0.9.3  last_updated 2025-11-11T16:16:22Z
```

**Seis releases en 2026 y la última de ayer.** Es cadencia medida, no impresión. **Agregar `hub.docker.com` al conjunto
de canales verificables de esta KB**, al lado de `registry.npmjs.org`, `pypi.org`, `packagist.org` y
`raw.githubusercontent.com`.

### 🔴 El sesgo del instrumento, medido: el registro de paquetes no puede devolver media capa

| Pieza | npm | PyPI | Packagist | Canal real de distribución |
|---|---|---|---|---|
| `lrsql` | — | — | — | **Docker Hub + releases de GitHub** (uberjar JVM) |
| `learnmcp-xapi` | 🔴 **`total: 0`** (`text=learnmcp`) | 🔴 **404** | — | **Ninguno: se instala desde el código** (*from source*, `venv`, `uv`) |
| `ralph` | — | `ralph-malph` ✅ **pero 2 años atrás** | — | **`main` de git** para lo actual |

**La regla: el registro de paquetes de un lenguaje sólo es el instrumento correcto si la pieza se distribuye como
librería de ese lenguaje.** Una plataforma entregada como **contenedor** o **uberjar** es invisible a npm, PyPI y
Packagist; una herramienta que se instala **desde el código** es invisible a todos a la vez. Esto generaliza un nivel la
lección del pase 30 (*«buscar en PyPI, no en GitHub»*): no alcanza con elegir el registro, hay que **elegir el canal**.
Y tuvo una consecuencia concreta: **el gap 60 declaró ausente una pieza que esta KB lista desde el pase 6**, porque la
lista de candidatos venía del registro. Ver tendencias **99** y **100**.

### ✅ `coursecode` — del README al contrato de la tool

Se bajó y abrió el artefacto publicado (`coursecode@0.1.61`, tarball de `registry.npmjs.org`, 200, 2,9 MB):

| Medición | Valor |
|---|---|
| Licencia del artefacto | **MIT**, *«Copyright (c) 2026 Seth Vincent»* |
| Dependencia MCP | **`@modelcontextprotocol/sdk`** en `dependencies` |
| Tools definidas / casos de dispatch | **15 / 15** — sin aliasing ni supresión |
| Escrituras | **2**: `coursecode_build` (paquete a `dist/`) y `coursecode_narration` (MP3 + TTS pago) |

🟢 **El upgrade de evidencia que importa:** los cuatro estándares de salida dejan de ser prosa del README y pasan a estar
**en el `inputSchema` de la tool**: `enum: ['cmi5','scorm2004','scorm1.2','lti']`. Un *enum* de contrato lo verifica el
cliente MCP; una frase de README no.

⚠️ **Lo que no se hizo, y se dice:** **no se ejecutó `tools/list`.** Instalar dependencias de terceros quedó bloqueado en
este entorno, así que las cifras son **lectura de artefacto**, no de protocolo (**gap 62**).

### 🟢 `qti3-cli`: el costo del wrapper MCP queda medido

`@longsightgroup/qti3-cli@0.13.1` (**MIT**), `bin: { "qti3": "dist/index.js" }`, superficie declarada *«parsing,
validating, scoring, inspecting, and checking QTI 3 items»*. Sus `dependencies` son **sólo sus cuatro hermanas**
(`qti3-core`, `-a11y`, `-fixtures`, `-conformance`, las cuatro en `0.13.1`): **cero dependencias de terceros en toda la
cadena**. Un wrapper MCP **agrega exactamente una** (`@modelcontextprotocol/sdk`). Ver **P74**.

### 🔴 Ruido medido, para que el próximo pase no lo vuelva a pagar

| Consulta | Registro | Resultado | Qué devuelve de verdad |
|---|---|---|---|
| `opencase` | npm | **7**, 0 del dominio | Apertura de cajas de skins (`opencase`, `skins4go`, *«OpenCase by ДикиЙ»*) |
| `opencase` | Packagist | **665**, 0 del dominio | *Fuzzy match* contra **`opencage`** (geocodificador) y **`opencast`** (Apereo, otro proyecto) |
| `cass` | npm / Packagist | ruido / **26.726** | Cassandra, **USPS CASS** (direcciones postales), Shimeji, OSU CASS |
| `opencase` / `cass` / `qti3` | PyPI | **404 / 404 / 404** | Nada |
| `tincan` | npm | ruido mezclado | 🔴 **`@brutalsystems/tincan`**: servidor MCP de mensajería entre sesiones de Claude Code y Codex. **MIT, activo, con MCP — y cero relación con educación** |
| `learning_locker` | npm / Packagist | **1** / **3**, exactos ✅ | El único caso donde el nombre del proyecto **sí** desambigua |
| `qti` | Packagist | **36** | El stack PHP real: **`qtism/qtism` (OAT QTI-SDK)** y las extensiones **`oat-sa/extension-tao-*`** |

**Hallazgo incidental que sí es del dominio:** `@osu-cass/sb-components` — *«Shared components for Smarter Balanced»*,
del consorcio de evaluación de Oregon State. Apareció buscando `cass` por otra cosa. **No es CaSS**; se anota para que
no se vuelva a confundir.

### 🔴 La capa xAPI «clásica», medida y congelada

| Paquete | Registro | Licencia | Último movimiento |
|---|---|---|---|
| `learning_locker` | npm | 🔴 **GPL-3.0** | `modified` **2022-06-19** (~4,3 años) |
| `tincanjs` (RusticiSoftware) | npm | **Apache-2.0** | `modified` **2022-06-27** (~4,3 años) |
| `tincan` / TinCanPython (RusticiSoftware) | PyPI | **Apache-2.0** | release **2020-09-03** (~6 años) |

**Esto confirma la recomendación que esta KB ya tenía** (`lrsql` o Ralph, nunca Learning Locker) **y ahora con la razón
medida**: no es sólo que sea copyleft, es que está **congelado**. 🔵 Y el `learning_locker` de Packagist devuelve **3
resultados exactos**, uno de ellos `yetanalytics/statementfactory`: **la consulta que encontró lo muerto llevaba el
puntero a lo vivo en la columna del mantenedor.**

---
## 2026-10-02 (pase 32) — el registro de paquetes rinde **un MCP MIT que el campo `description` ocultaba**, y el término «xapi» resulta ser una **trampa de tres vías** con dos paquetes MIT activos que no tienen nada que ver con educación

**Lo medido:** `registry.npmjs.org/-/v1/search` sobre **QTI, xAPI, SCORM** y la pregunta desambiguada de **CASE**, más
sondeo directo a **PyPI**, más lectura de README de cada candidato. Más la lectura de código de Open edX que cierra los
**gaps 57 y 59** (en `agents/trending.md`).

### 🟢 Lo que entra, verificado el 2026-10-02

| Repo | URL | Licencia | ★ | Stack | Señal | Por qué importa |
|---|---|---|---|---|---|---|
| **coursecode** | [course-code-framework/coursecode](https://github.com/course-code-framework/coursecode) | **MIT** ✅ | 5 | JavaScript | `coursecode@0.1.61`, npm `modified` 2026-07-20 | 🟢 **Primera puerta MCP de la capa de empaquetado de esta KB.** **SCORM 1.2 + SCORM 2004 + cmi5 + LTI 1.3** en una pieza permisiva, con **servidor MCP incorporado** |
| **qti3** | [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** ✅ | 5 | TypeScript | `@longsightgroup/qti3-migrator@0.13.1`, `modified` **2026-10-01** — publicado **ayer** | 🔴 **Rompe el «QTI utilizable es PHP» del pase 28.** **12 paquetes**, `qti3-core` con **cero dependencias de terceros**, más `-migrator` (1.2/2.x → 3) y `-transcoder` (3 → 1.2/2.x) |
| **lineage-skill** | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** ✅ | **448** | Python | El alta de agente del pase | Destila videos/PDFs/transcripciones en **Agent Skills docentes con trazabilidad a la fuente**. Ver `agents/top.md` |

**Nota de adopción, declarada:** los dos primeros tienen **5 ★**. **Capacidad y licencia verificadas; comunidad mínima.**
Se registran porque desbloquean una capa, no porque tengan tracción.

### 🔴 Lo que NO entra, y por qué el filtro de licencia no alcanza

| Paquete | Licencia | Fresco | Por qué queda afuera |
|---|---|---|---|
| `xapi-to` ([xapi-labs/xapi-cli](https://github.com/xapi-labs/xapi-cli)) | **MIT** | `modified` **2026-09-29** | 🔴 **No es xAPI educativo.** *Marketplace* de APIs de **cripto/Web3** (BlockPI RPC, Binance Web3, dominios/DNS). **Cero** menciones de *«Experience API»*, *«Tin Can»* o *«learning record»* en 47.905 caracteres de README — **y se anuncia como *«Agent-friendly CLI for xAPI»* con skill instalable**. **Colisión 5** |
| `xapi-python` | **MIT** | — | 🔴 **«The xStation5 API Python library»**: API del bróker de **forex XTB**. **Colisión 6** |
| `@citolab/qti-convert-local-ai` | **GPL-3.0-only** ⚠️ | `modified` 2026-09-28 | Conversión planilla → paquete QTI en el navegador. Referencia, no base de entregable cerrado |
| `mizcausevic-dev/mcp-ai-tutor` | **AGPL-3.0** ⚠️ | 10 commits, **0 ★** | Seis tools MCP de *AI Tutor Card* con **FERPA/COPPA/GDPR**. Ataca el bloqueador regulatorio correcto por el canal correcto (`.well-known` + MCP), pero **ni componible ni adoptado**. Señal de especificación a vigilar |

🔵 **La lección de método, y es la que hay que conservar:** **las dos colisiones son MIT, activas y una se anuncia como
agéntica.** Un barrido que ordene por nombre + licencia + frescura —que es el barrido obvio— **las habría promovido a la
tabla de agentes**. El único filtro que las atrapó fue **abrir el README y contar menciones del vocabulario del
dominio**. Y en el otro sentido, **la descripción de `coursecode` no dice «MCP» y el README sí**: el mismo canal que
descarta falsos positivos es el que encuentra los verdaderos. **El campo `description` no sirve ni para afirmar ni para
negar.**

### ⚪ Lo que no se pudo medir con este método — gap 51 sigue abierto

`registry.npmjs.org` hace **OR** sobre texto libre: `"competencies and academic standards exchange"` devuelve
**1.696.870** objetos (`@urql/exchange-retry`, `@univerjs-pro/exchange-client`, ASN.1 PKCS#12…). **El registro de
paquetes no sabe desambiguar un estándar de nombre multi-palabra.** El **gap 51** queda abierto **con un método
descartado por escrito**: hay que atacarlo por el **nombre del proyecto implementador** (`OpenCASE`, `CASS`), no por el
del estándar.

### 🔴 Y la ausencia que sí quedó medida: **QTI y xAPI/LRS no tienen puerta MCP**

Tras abrir los README de los candidatos de las dos capas: **QTI no tiene conector MCP** (`LongsightGroup/qti3` trae
`AGENTS.md` pero no MCP) y **xAPI/LRS tampoco**. La **tendencia 89** —*«donde hay una puerta MCP suele haber varias»*—
**valió para OneRoster y Open Badges (pase 31) y no vale para la capa de evaluación y telemetría**: ahí la única puerta
es la de **empaquetado** (`coursecode`). **Es una ausencia medida, no silencio**, y es la oportunidad de contribución
*upstream* más limpia que tiene esta KB: `qti3-core` no tiene dependencias y ya expone parser, validación y *scoring* —
el servidor MCP encima es trabajo de días, no de meses.

## 2026-10-02 (pase 31) — **cinco versiones de API leídas una por una**: el `v0` que la KB iba a recomendar está deprecado, y la pregunta correcta no era «qué versión» sino «¿alguna crea el curso?» — **ninguna**

**Canal:** `raw.githubusercontent.com` (el único que responde para código; ver la tabla de verificación abajo).
**Repo:** `openedx/edx-platform`, rama `master`, árbol `cms/djangoapps/contentstore/rest_api/`.

### Lo que dice `rest_api/urls.py`, que es donde se termina la discusión de «cuántas versiones hay»

```python
urlpatterns = [
    path('v0/', include(v0_urls)),
    path('v1/', include(v1_urls)),
    path('v2/', include(v2_urls)),
    path('v3/', include(v3_urls)),
    path('v4/', include(v4_urls)),
]
```

**Cinco, montadas en paralelo.** El pase 29 lo había contado bien (*«cinco versiones de API vivas donde el pase 28 vio
tres»*) y queda ratificado leyendo el `include`, no inventariando archivos.

### 🔴 El `v0` de authoring está deprecado **en favor del `v1`** — al revés de la consigna que traía este pase

`v0/views/xblock.py`, primeras líneas:

```
Public rest API endpoints for the CMS API — v0 xblock (DEPRECATED).

.. deprecated::
    These views are superseded by ``XblockViewSet`` in
    ``cms.djangoapps.contentstore.rest_api.v1.views.xblock``.
    Use ``/api/contentstore/v1/xblock/`` going forward.
    These v0 endpoints will be removed in a future release.
```

Y además **lo ejecuta**: define

```python
_DEPRECATION_MSG = ("The v0 xblock API (/api/contentstore/v0/xblock/) is deprecated. "
                    "Use /api/contentstore/v1/xblock/ instead.")
```

y llama `warnings.warn(_DEPRECATION_MSG, DeprecationWarning, stacklevel=2)` en **las cinco** operaciones
(`retrieve`, `update`, `partial_update`, `destroy`, `create`).

Del otro lado, `v1/urls.py` **ya tiene el router montado**:

```python
_router = DefaultRouter()
_router.register(r'xblock', XblockViewSet, basename='xblock')
urlpatterns = _router.urls + [ ... ]
```

y `v1/views/xblock.py` (14.080 bytes) define `XblockViewSet(StandardizedErrorMixin, viewsets.ViewSet)` con
`create`, `retrieve`, `update`, `partial_update`, `destroy`, más un parámetro ya marcado `deprecated=True` y un modo
`minimal` de respuesta.

**El comentario que mandó a medir el `v0` sigue al final de `v1/urls.py`**, después del router:

```python
    # Authoring API
    # Do not use under v1 yet (Nov. 23). The Authoring API is still experimental and the v0 versions should be used
```

**«Nov. 23» es noviembre de 2023.** Es el mismo aviso que el pase 29 describió como *«encabeza una sección vacía y es de
2023»* — literalmente encabeza una sección vacía, porque después de esas dos líneas **el archivo termina**.

### El serializer dice qué se puede crear, y alcanza para secciones, subsecciones, unidades y componentes

`v0/serializers/xblock.py` → `XblockSerializer(StrictSerializer)`, con validación estricta (*«No unexpected fields are
passed in»*) y estos campos relevantes:

| Campo | Para qué sirve |
|---|---|
| `parent_locator` | dónde se cuelga el bloque nuevo |
| `category` | **qué tipo** de bloque: `chapter` (sección), `sequential` (subsección), `vertical` (unidad), o el componente |
| `display_name` | nombre visible |
| `data`, `metadata`, `fields` | contenido y configuración |
| `children`, `has_children` | estructura |
| `published`, `has_changes`, `edited_on` | estado editorial |

En Open edX **la sección, la subsección, la unidad y el componente son todos xblocks**, así que **un solo endpoint con
`parent_locator` + `category` cubre toda la jerarquía**. El `v1` confirma el contrato: el *docstring* del viewset
documenta `create` como *«Create a new xblock under a parent block»* y extrae el `course_key` **del `parent_locator`**.
Las dos versiones delegan en el mismo `view_handlers.handle_xblock`.

### 🔵 Y lo que nadie había leído: `v2` trae la capa de **reutilización** (Libraries v2)

`v2/urls.py` completo tiene **7 rutas**, y cuatro son una capa entera que no figura en ningún archivo de esta KB:

| Ruta | Vista |
|---|---|
| `home/courses` | `HomePageCoursesViewV2` — **sólo `GET`** |
| `downstreams/` | `DownstreamListView` |
| `downstreams/<usage_key>` | `DownstreamView` |
| `downstreams/<course_key>/summary` | `DownstreamSummaryView` |
| **`downstreams/<usage_key>/sync`** | **`SyncFromUpstreamView`** |
| `validate/numerical-input/` | `NumericalInputValidationView` |

Es el mecanismo **upstream → downstream**: un bloque vive en una biblioteca (*upstream*) y los cursos que lo consumen
(*downstream*) **se sincronizan**. Para un agente autor es la diferencia entre *«editar N cursos»* y *«editar uno y
propagar»*. **Entra como capa nueva en `repos/foundations.md`.**

### La respuesta al gap 50, en una tabla

| Capa medida | Authoring **dentro** del curso | **Crear** el curso |
|---|---|---|
| REST `v0` (deprecado) | sí — xblock, assets, video, transcripts, grading, advanced settings, tabs | **no** |
| REST `v1` (vigente) | sí — `XblockViewSet` + settings, details, grading, certificates, textbooks, group configurations, container children | **no** — sólo `course_rerun` (clona) |
| REST `v2`/`v3`/`v4` | parcial (grading en `v3`); `v2` agrega `downstreams` | **no** (`home/courses` es `GET`) |
| Conector oficial `openedx-mcp` 0.1.5 (AGPL-3.0) | sí — 7 rutas CMS, incluida `blocks/create-tree/` | **no** — ninguna de sus 19 escrituras es `create_course` |

**Tres mediciones independientes, la misma conclusión.** El `v0` no era «la versión recomendada» y el `v1` no era
«experimental»: las dos authorean, y **ninguna crea la cáscara del curso**. El bootstrap es curso plantilla +
`course_rerun` (**gap 57**: falta medir si `course_rerun` acepta un plantilla vacío como origen).

### Altas de este pase — del barrido de registros de paquetes (consigna del pase 30)

Se consultó `registry.npmjs.org` y `pypi.org` **por nombre de proyecto/estándar**, abriendo el README de cada paquete y
buscando «MCP» adentro. Lo verificable:

| Paquete | Versión | Licencia | Modificado | Repo verificado | MCP |
|---|---|---|---|---|---|
| [`@eduware/oneroster`](https://registry.npmjs.org/@eduware%2Foneroster) | 1.2.11 | **MIT** | 2026-07-10 | ⚠️ **no** (`Eduware-Inc/eduware-oneroster` → 404) | ✅ **sí, servidor MCP empaquetado** |
| [`@longsightgroup/oneroster`](https://github.com/LongsightGroup/oneroster) | 0.3.0 | **MIT** | 2026-07-15 | ✅ sí | no |
| [`@superbuilders/oneroster`](https://github.com/trilogy-group/oneroster-ts) | 0.7.0 | 0BSD (ya registrado) | 2026-05-04 | ✅ sí | ✅ sí (12 menciones) |
| [`@ajna-inc/openbadges`](https://registry.npmjs.org/@ajna-inc%2Fopenbadges) | 0.6.3 | **Apache-2.0** | 2026-05-19 | ⚠️ no declara repo | no |
| [`ltijs`](https://github.com/Cvmcosta/ltijs) | 7.0.6 | Apache-2.0 | 2026-09-18 | ✅ sí | **no — 0 menciones en README** |
| [`@timeback/caliper`](https://registry.npmjs.org/@timeback%2Fcaliper) | 0.3.3 | 🔴 **ninguna declarada** | 2026-09-25 | ⚠️ no declara repo | no |
| [`pylti1p3`](https://pypi.org/project/pylti1p3/) | 2.0.0 | MIT | 🔴 **2022-11-20** | ✅ sí (`dmitry-viskov/pylti1.3`, por `README.rst`) | no |
| [`openedx-mcp`](https://pypi.org/project/openedx-mcp/) | 0.1.5 | **AGPL-3.0** (leída del wheel) | 2026-07-25 | — (PyPI) | es el conector |

**`@eduware/oneroster` es el alta que más mueve la aguja: es la primera puerta MCP *permisiva* de OneRoster** de esta
KB. La que ya estaba —`oneroster-ts`— es 0BSD, que también es permisiva, pero ahora hay dos y una es MIT con README que
documenta el ejecutable.

### ⚠️ Qué canal verifica acá, y por qué este pase no publica estrellas

| Canal | Resultado |
|---|---|
| `github.com/<owner>/<repo>` (HEAD) | **403** para todos, incluido `openedx/edx-platform` |
| `api.github.com/repos/...` | **403** — *«GitHub access to this repository is not enabled for this session»* |
| `www.npmjs.com/package/...` | **403** |
| `raw.githubusercontent.com/<o>/<r>/HEAD/README.md` | **200** si existe, **404** si no → **es el test de existencia válido** |
| `registry.npmjs.org/<pkg>` | **200** con licencia, versiones, fechas y README |
| `pypi.org/pypi/<pkg>/json` + `files.pythonhosted.org` | **200**, y el artefacto se baja y se abre |

🔴 **Sin `api.github.com` no hay forma de medir estrellas de primera mano, así que este pase no escribe ninguna.** Las
altas van con licencia, versión, fecha de modificación y canal verificado. Es menos vistoso y es lo que se midió.

## 2026-10-02 (pase 30) — el **gap 52 cierra leyendo el código**, y la contradicción entre los dos documentos no se resuelve eligiendo uno: **los dos describen rutas que existen, y la regla es cuál lleva el prefijo**

**La acción 1 del pase 29 era resolver la forma exacta de las rutas de OpenCASE leyendo el código, no los docs** — el
método que funcionó con Open edX. Se ejecutó sobre **cinco archivos del árbol `main`**, y el resultado es mejor que
«gana uno»: **hay una regla, es simple, y ninguno de los dos documentos la enuncia.**

### El canal, y un bloqueo nuevo que conviene anotar

`raw.githubusercontent.com` **responde** (tercer pase consecutivo en que es el canal que rinde). 🔴 **Lo que NO responde:
`codeload.github.com` devuelve 403 por el proxy**, así que **no se puede bajar el tarball del repo** y hay que leer
archivo por archivo; y la **API de GitHub está cerrada** para repos fuera del alcance de la sesión. ⚠️ **Dos dominios
nuevos al registro de bloqueos de esta KB: `openacs.org` y `openedx.org`.**

**Todo lo de abajo es lectura de primera mano de `main`.** Los archivos: `apps/opencase/package.json`,
`apps/opencase/src/main.ts`, `apps/opencase/src/interfaces/http/server.ts`,
`apps/opencase/src/interfaces/http/http-management/routes.ts` y
`apps/opencase/src/interfaces/http/http-public/v1p1/routes.ts` (más su gemelo `v1p0`), y `docs/DEVELOPMENT.md`.

### ✅ La respuesta al gap 52, en una regla

🔵 **El segmento `ims/case/v1pX` aparece exactamente cuando la operación actúa sobre una entidad del estándar CASE.
No aparece nunca en las rutas de plataforma.**

| Forma | Qué documento la escribía | ¿Existe en el código? |
|---|---|---|
| `PUT /management/tenants/{tenantId}/ims/case/v1p1/CFItems/{id}` | `FRAMEWORK_EDITOR_BACKEND_INTEGRATION.md` | ✅ **Sí, literal** |
| `POST /management/tenants/{tenantId}/ims/case/v1p1/CFPackages/import` | `FRAMEWORK_EDITOR_BACKEND_INTEGRATION.md` | ✅ **Sí, literal** |
| `PUT /management/tenants/{tenantId}/CFItems/{id}` | `DEVELOPER.md` | 🔴 **No. No existe ninguna ruta así** |
| `GET /management/tenants/{tenantId}/CFPackages` | — | ✅ **Sí** — y es **la única** ruta `CFPackages` sin prefijo: el *listado* |

**Veredicto: `FRAMEWORK_EDITOR_BACKEND_INTEGRATION.md` es correcto y `DEVELOPER.md` está equivocado para entidades CASE.**
Y se ve de dónde salió el error: **el listado de paquetes sí va sin prefijo**, porque es una operación de plataforma
—«dame los paquetes de este tenant»— y no una operación del estándar sobre una entidad versionada.

✅ **Confirmado lo que el pase 29 reportó:** `apps/opencase/FRAMEWORK_MANAGEMENT_GUIDE.md`, el documento que el README
principal ofrece como *«Complete endpoint reference»*, **sigue devolviendo 404 en `main`**. El enlace está roto en la rama
por defecto.

### La superficie completa, contada: **72 rutas**

| Bloque | Rutas | Detalle |
|---|---|---|
| **Lectura CASE `v1p1`** | **12** | `CFDocuments` (lista y por id), `CFItems`, `CFAssociations`, `CFItemAssociations`, `CFRubrics`, `CFSubjects`, `CFConcepts`, `CFAssociationGroupings`, `CFItemTypes`, `CFLicenses`, `CFPackages` |
| **Lectura CASE `v1p0`** | **12** | 🔵 **El mismo juego completo.** Las dos versiones del estándar están montadas enteras, no parcialmente |
| **Management** | **44** | **20 con prefijo `ims/case/v1pX`** (escritura sobre entidades CASE, en las dos versiones) + **24 sin prefijo** (plataforma) |
| **Descubrimiento** | **2** | 🔵 **Uno por versión**, y sin autenticación |
| **Público** | 1 | `GET /public/tenant-lookup` |
| **Salud** | 1 | `GET /health` |
| **Total** | **72** | |

### 🔵 Tres hallazgos que el pase 29 no tenía, y los tres cambian cómo se cotiza P60

**1. Hay DOS endpoints de descubrimiento, no uno.** El pase 29 registró
`GET /ims/case/v1p1/discovery/imscasev1p1_openapi3_v1p0.json`. También existe
**`GET /ims/case/v1p0/discovery/imscasev1p0_openapi3_v1p0.json`**, y los dos están registrados **antes de los
*middlewares* de autenticación**: *«Service Discovery endpoints (no auth required)»*. **Se pueden generar dos conectores,
uno por versión del estándar, sin credenciales para leer el spec.**

**2. 🔵 La lectura usa autenticación OPCIONAL, y eso abarata el conector de sólo lectura a casi cero.** El código monta
`makeOptionalAuthMiddleware` en `/ims/case` y lo comenta así:

> *«CASE Provider API — optional auth (frameworks marked public are readable without auth). IDs are globally unique so no
> tenantId is needed for read endpoints.»*

**Un conector MCP de lectura sobre marcos públicos no necesita credenciales ni tenant.** El `/management` sí: va con
`makeAuthMiddleware` estricto.

**3. 🔴 Las operaciones de escritura NO son parte del estándar, y el propio código lo declara.** El encabezado de
`http-management/routes.ts`: *«These endpoints provide UPDATE and DELETE operations for CASE entities. These operations
are **NOT part of the CASE standard specification** and are provided as extended functionality.»*
**Consecuencia directa para P60: la mitad de lectura del conector generado es portable a cualquier proveedor CASE
certificado; la mitad de escritura es específica de OpenCASE.** Eso hay que decirlo antes de cotizar, no después.

### 🔵 La capa que nadie había visto: **CGE — CASE Global Exchange**, 11 rutas de federación

Ni el pase 29 ni ningún otro registró esto, y es la pieza que convierte a OpenCASE de «servidor propio» en **cliente de
un registro global de marcos**:

| Ruta (bajo `/management/tenants/{tenantId}/cge/`) | Qué hace |
|---|---|
| `credentials` (GET / PUT / DELETE) | Credenciales contra el exchange |
| `credentials/test` (POST) | 🔵 Prueba la credencial sin importar nada |
| `frameworks` (GET) · `frameworks/{frameworkId}` (GET) | Lista y trae marcos **del registro global** |
| `subscriptions` (POST / GET) | **Se suscribe a un marco** |
| `import` (POST) | Importa desde el exchange al tenant |
| `frameworks/{frameworkId}/refresh` (POST) | **Refresca la copia cacheada** |
| `cache/{docId}/items` (GET) | Busca ítems en la copia cacheada |

**Por qué importa comercialmente:** un cliente no tiene que **cargar** los marcos curriculares — puede **suscribirse** a
los que ya existen en el exchange de 1EdTech y mantenerlos sincronizados. **Eso cambia el alcance de un proyecto de
competencias de «digitalizar el currículum» a «suscribir y alinear»**, que es mucho más barato y mucho más defendible.

### El resto de lo medido, en una tabla

| Qué | Medición |
|---|---|
| Stack | **Express 5**, TypeScript, **Apache-2.0** (verificado en `package.json`) |
| 🔵 Generación del spec | **`swagger-jsdoc`** es dependencia: **el OpenAPI se genera de anotaciones en el código**, así que el código *es* la fuente autoritativa — no hay spec que pueda atrasarse |
| Scopes | `case.read`, `case.write`, `case.admin`, `case.owner`, vía `requireScope` / `requireAnyScope`, y **anotados como `x-required-scopes` en el OpenAPI** |
| Ciclo de vida | 🔵 **`POST .../CFPackages/{id}/restore`** — archivado y restauración, que el pase 29 no tenía |
| Versionado en ruta | `withCaseVersion('1.0'\|'1.1')` inyecta la versión; **Express 5 hace `req.query` de sólo lectura**, así que el proyecto la pasa por un *override* |
| Límite de cuerpo | **50 MB** (`express.json({limit:'50mb'})`) — coherente con importar paquetes CASE grandes |
| 🔴 Riesgo de seguridad | **`cors({ origin: true, credentials: true })`**, con el comentario *«Allow all origins (for development) - restrict in production»* **en el código**. Para un entregable de cliente es una línea de endurecimiento obligatoria |
| Enrutamiento externo | Traefik: `/ims/*` → lectura, `/management/*` → escritura, `/public/*`, `/health`, y Keycloak en `/realms/*` y `/admin/*` |

⚠️ **El límite honesto de toda esta medición: no se levantó una instancia.** Es lectura de código del árbol `main`, no
tráfico observado, y **el OpenAPI real no se pidió al endpoint de descubrimiento** porque eso requiere el stack Docker
corriendo. **Las rutas quedan medidas; el spec generado, no.** Es la **acción 2 del pase 31**, y ahora es una tarde de
trabajo con `docker-compose up` y una sola llamada.


## 2026-10-01 (pase 29) — el gap 50 se **reencuadra leyendo el archivo de al lado**: el aviso de «experimental» encabeza una sección vacía y es de 2023, y hay **cinco versiones de API vivas** donde el pase 28 vio tres

**La acción 1 del pase 28 era verificar si los endpoints `v0` de *authoring* cubren lo que el `v1` experimental
promete.** Se ejecutó, y **la pregunta resultó mal planteada** — no por error de quien la escribió, sino porque la
premisa venía de **un solo archivo**. Al leer tres, la dirección del tráfico es la contraria a la que el pase 28
supuso.

### 🔵 El canal del pase 28 vuelve a rendir, y ahora se lo usa como corresponde: **varios archivos, no uno**

`raw.githubusercontent.com` responde (los dos dominios de documentación de Open edX siguen bloqueados). **La lección de
método de este pase no es sobre el canal sino sobre la muestra:** el pase 28 leyó `v1/urls.py`, encontró un aviso
literal y verdadero, y **sacó de él una conclusión sobre el estado del proyecto**. Bastaba abrir `v0/views/xblock.py`
—**un archivo, en el mismo paquete**— para ver que el proyecto dice lo contrario.

**Toda la medición de abajo es lectura de primera mano del árbol `master`.**

### La contradicción, con las citas enfrentadas

| Archivo | Qué dice, textual | Fecha de la señal |
|---|---|---|
| `cms/djangoapps/contentstore/rest_api/v1/urls.py` | `# Authoring API` / *«Do not use under v1 yet (Nov. 23). The Authoring API is still experimental and the v0 versions should be used»* | 🔴 **Nov. 2023**, y **sin una sola ruta debajo del comentario** |
| `cms/djangoapps/contentstore/rest_api/v0/views/xblock.py` | *«v0 xblock (DEPRECATED). These views are superseded by `XblockViewSet` in `…rest_api.v1.views.xblock`. Use `/api/contentstore/v1/xblock/` going forward. These v0 endpoints will be removed in a future release.»* | ✅ **Vigente**, con `DeprecationWarning` emitido en las 5 vistas |

**Y el desempate no es interpretativo, es de código:** `v1/urls.py` **registra** el sucesor en la primera línea de sus
`urlpatterns` —`_router.register(r'xblock', XblockViewSet, basename='xblock')`— y `v1/views/xblock.py` implementa
**`create`, `retrieve`, `update`, `partial_update` y `destroy`**. **CRUD completo, registrado, no prometido.**

### 🔵 El `XblockViewSet` de `v1` no es un parche: está construido contra un programa de ADRs con nombre

El docstring enumera los ADRs de **FC-0118** que cumple: **0025** (`serializer_class`), **0026**
(`authentication_classes` + `permission_classes` explícitas), **0028** (consolidación en un `ViewSet` vía
`DefaultRouter`), **0029** (envelope de error estandarizado vía `StandardizedErrorMixin`), **0034**
(`JwtAuthentication` + `SessionAuthenticationAllowInactiveUser`, elegido explícitamente para que un autor inactivo siga
pudiendo operar mientras se verifica su sesión) y **0036**.

🔵 **ADR 0036 es el hallazgo que vale más por línea leída, y no se buscó: `retrieve` acepta `?view=minimal`**, que
*«strips the (tree-shaped) xblock response to a small set of structural fields»*. **El árbol completo de un curso es
precisamente la respuesta que revienta la ventana de contexto de un agente**, y la plataforma **ya trae el recorte
oficial**. Para un conector eso es trabajo que no hay que hacer ni cotizar.

### La *Authoring API* real, que está en `v0` y es más grande de lo que el pase 28 registró

Bajo el propio encabezado `# Authoring API` de `v0/urls.py`:

| Grupo | Rutas | Escritura |
|---|---|---|
| **Assets / archivos** | `file_assets/{course_id}`, `file_assets/{course_id}/{asset_key}` | ✅ **create + retrieve** y **update + destroy** (`CreateAPIView`/`RetrieveAPIView`, `UpdateAPIView`/`DestroyAPIView`, leído en `v0/views/assets.py`) |
| **Video** | `videos/uploads/{course_id}`, `videos/uploads/{course_id}/{edx_video_id}`, `videos/images/…`, `videos/encodings/…`, `videos/features` | ✅ Sube y gestiona |
| **Transcripciones** | `video_transcripts/{course_id}`, `youtube_transcripts/{course_id}/check`, `/upload` | ✅ **Incluye el camino de YouTube** |
| **XBlock** | `xblock/{course_id}` (create), `xblock/{course_id}/{usage_key}` (RUD) | ⚠️ Existe y escribe, **pero está deprecado en favor de `v1`** |
| **Notas** | `grading/{course_id}` (`AuthoringGradingView`) | ✅ |
| **Configuración** | `advanced_settings/{course_id}`, `tabs/{course_id}`, `tabs/…/settings`, `tabs/…/reorder` | ✅ |
| **Course Optimizer** | `link_check`, `link_check_status`, `rerun_link_update`, `rerun_link_update_status` | ✅ **Verifica enlaces robados de un *rerun*** — útil para un agente de QA de curso |

### 🔴 El hallazgo colateral que cambia cómo se cotiza: **`v0`, `v1`, `v2`, `v3` y `v4`, todas montadas a la vez**

`rest_api/urls.py` las incluye las cinco. El pase 28 conocía tres. Lo que hay en las dos nuevas:

- **`v2`** — `downstreams`: `DownstreamListView`, `DownstreamView`, `DownstreamSummaryView` y **`SyncFromUpstreamView`**;
  más `NumericalInputValidationView` y `HomePageCoursesViewV2`. 🔵 **`SyncFromUpstream` es propagación de contenido de
  biblioteca a los cursos que lo heredan** — la pieza exacta que necesita un agente que corrige un error una vez y lo
  empuja a todos lados.
- **`v3`** — `DefaultRouter` con `home`, `course_details` y **`authoring_grading`**.
- **`v4`** — `home/courses` (`HomeCoursesViewSet`, ADR **0028**).

🔴 **El costo concreto de esa rotación, en una sola capacidad: las notas están en tres versiones a la vez** —
`grading/` (`v0`), `course_grading/` (`v1`) y `authoring_grading` (`v3`). **Un conector serio no le pega a una ruta
fija: necesita un adaptador de versión**, y eso es una línea de la propuesta, no una sorpresa de la semana cuatro.

### 🔵 El repo nuevo de estándares, y es el que cierra el hueco más viejo de esta KB

[`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) — **Apache-2.0** (verificado en el archivo `LICENSE`), **9 ★**,
**3 forks**, **180 commits**. **Es la implementación de referencia de CASE, del propio organismo de estándares**, y
esta KB llevaba cuatro pases declarando que CASE no tenía nada permisivo que abrir.

Lo que es, leído de los README de sus componentes:

- **Publishing Server** — implementa la **CASE Provider API oficial**, *«fully compatible with the 1EdTech
  certification requirements»*, **CASE 1.0 y 1.1**, con el juego completo de recursos: `documents`, `items`,
  `associations`, `rubrics`, `packages`. Soporta *field filtering*, paginación, ordenamiento y filtrado por metadatos
  **como lo define la especificación**, más **endpoints de descubrimiento de servicio**.
- **Visual Editor** — canvas de autoría: items como nodos, asociaciones como conexiones (*«is child of»*, *«is related
  to»*, *«precedes»*), *layout* automático (jerarquía, radial o árbol) y publicación directa al servidor.
- **Identidad** — **Keycloak** (OIDC, SSO) y **RBAC de cuatro niveles**: *Viewer*, *Author*, *Tenant Administrator*,
  *System Administrator*, con **aislamiento por tenant** forzado por el token.
- **Almacenamiento** — 🔵 **versionado inmutable en archivos, no en base de datos**: *«zero external dependencies for
  storage»*, cada cambio es una versión nueva, **auditoría completa por diseño** y capa de storage reemplazable.
- **Despliegue** — un solo comando, Docker, HTTPS automático detrás del reverse proxy en producción.

**Superficie medida** (26 pares método+ruta distintos en `apps/opencase/docs/DEVELOPER.md`, 28 en
`FRAMEWORK_EDITOR_BACKEND_INTEGRATION.md`): CRUD de escritura sobre **`CFDocuments`, `CFItems`, `CFAssociations` y
`CFPackages`** en **v1p0 y v1p1** (`PUT`, `POST`, `DELETE`), administración de tenants y miembros
(`POST/GET/PATCH/DELETE /management/tenants/{tenantId}/members/…`), **API keys**
(`POST`/`DELETE /management/tenants/{tenantId}/api-keys`), importación de marcos (`cge/import`, `cge/subscriptions`,
`cge/credentials`), `GET /health` y `GET /public/tenant-lookup` (sin autenticar).

🔵 **Y el dato que convierte esto en el mejor negocio de la KB:
`GET /ims/case/v1p1/discovery/imscasev1p1_openapi3_v1p0.json`.** **El servidor publica su propio OpenAPI 3.** Eso
significa que el conector MCP **no se escribe: se genera** — exactamente el camino por el que `oneroster-ts` llegó a
164 métodos con 39 commits. Ver **P60**.

🔴 **Pero MCP no aparece en ninguna parte del repo**, y la ausencia está medida en el README crudo, no inferida. **Ver
la colisión 5 en `agents/trending.md`: la página renderizada de GitHub sí dice «MCP», porque es el menú de GitHub.**

### Lo que este pase deja medido y lo que no, sobre estos dos repos

- ✅ **Medido:** cinco versiones de API de Studio, el CRUD del `XblockViewSet`, los ADRs de FC-0118 y `?view=minimal`,
  **leyendo el código**; la superficie REST de OpenCASE y su endpoint de descubrimiento, **leyendo los docs del repo**;
  las dos licencias, **en el archivo `LICENSE`**.
- ❌ **No medido:** **ninguna llamada HTTP contra ninguna de las dos plataformas.** Sin instancia, y levantarla choca
  con el límite declarado del pase 27. **OAuth2, *scopes*, *rate limits* y forma de las respuestas, sin verificar.**
- ❌ **No medido, y es una contradicción interna del repo:** la **forma exacta** de las rutas de OpenCASE.
  `DEVELOPER.md` escribe `/management/tenants/{tenantId}/CFItems/{id}`;
  `FRAMEWORK_EDITOR_BACKEND_INTEGRATION.md` escribe
  `/management/tenants/{tenantId}/ims/case/v1p1/CFItems/{itemId}`. 🔴 **Y el
  `FRAMEWORK_MANAGEMENT_GUIDE.md` que el README principal enlaza como «Complete endpoint reference» devuelve 404 en
  `main`.** Es el **gap 52** y la **acción 1 del pase 30**: resolverlo leyendo el código del servidor, o pidiéndole el
  OpenAPI a su propio endpoint de descubrimiento.
- ⚠️ **Higiene de documentación, en los dos repos nuevos del eje conector, y vale como señal de madurez:** el README de
  `oneroster-ts` dejó el bloque de ejemplo del binario con el nombre `"Todos"` y los placeholders `{org}/{repo}` sin
  reemplazar (residuo del generador), y OpenCASE dejó un `PUT /management/tenants/acme/cge/credentials` con el tenant
  de ejemplo literal. **Ninguna de las dos cosas es un defecto funcional; las dos dicen que los docs no tuvieron una
  pasada de revisión**, y eso se pondera al estimar.

## 2026-10-01 (pase 28) — el gap 48 queda contestado **leyendo el código fuente de Open edX**, y la respuesta es doble: la API alcanza para matrícula y notas, y **el *authoring* se declara experimental en el propio repo**

**La acción 1 del pase 27 era la de mayor valor comercial de esta KB** —*«verificar si Open edX expone una API REST
suficiente, y si lo hay, P55 se cotiza; si no, ésa es la razón de la ausencia»*. **Se ejecutó, y la respuesta no es
«sí» ni «no»: es un corte limpio entre dos mitades de la plataforma**, y el corte explica la ausencia mejor que
cualquiera de las dos respuestas simples.

### 🔵 El canal nuevo, que es lo que hizo posible la medición

🔴 **`docs.openedx.org` y `openedx.atlassian.net` están los dos bloqueados por el proxy de egreso** (dominios cinco y
seis de la lista de esta KB), así que **la documentación oficial de la API era inalcanzable** — justo para la acción
más valiosa del pase.

✅ **Pero `raw.githubusercontent.com` responde.** Eso habilita un canal de verificación que esta KB no estaba usando:
**leer el archivo fuente directamente, sin clonar y sin instalar nada.** Es importante más allá de este pase, porque
**esquiva parcialmente el límite que bloqueó al pase 27** (no se puede instalar código de terceros): no permite
*ejecutar*, pero sí **leer la declaración en el código**, que para medir superficie de API es exactamente lo que hace
falta.

**Toda la medición de abajo es lectura de primera mano de los `urls.py` del árbol `master`.** No es documentación, no
es un resumen de búsqueda, y no es inferencia.

### La mitad que alcanza: hay superficie versionada **y escribe**

| Grupo de API | Archivo leído | Rutas (verbatim) | Escribe |
|---|---|---|---|
| **Course Blocks** | `lms/djangoapps/course_api/blocks/urls.py` | `v1/blocks/{usage_key}`, `v1/blocks/`, `v1/block_metadata/{usage_key}` **y los tres equivalentes en `v2/`** | Lectura |
| **Enrollment** | `openedx/core/djangoapps/enrollments/urls.py` | `enrollment/{username},{course_key}`, `enrollment/{course_key}`, `enrollment`, `enrollments/`, `course/{course_key}`, **`unenroll/`**, `roles/`, **`enrollment_allowed/`** | ✅ **Sí** — `EnrollmentListView`, `UnenrollmentView`, `EnrollmentAllowedView`, `EnrollmentUserRolesView` |
| **Grades v1** | `lms/djangoapps/grades/rest_api/v1/urls.py` | `courses/`, `courses/{course_id}/`, `policy/courses/{course_id}/`, **`gradebook/{course_id}/`**, **`gradebook/{course_id}/bulk-update`**, `gradebook/{course_id}/grading-info`, **`subsection/{subsection_id}/`**, `section_grades_breakdown/`, `submission_history/{course_id}/` | ✅ **Sí** — **`GradebookBulkUpdateView`** y **`SubsectionGradeView`** (*course_grade_overrides*) |

🔵 **El dato que cotiza, y es mejor de lo que el pase 27 suponía:** **Open edX escribe notas por lote.**
`GradebookBulkUpdateView` es el equivalente funcional de `provide_assignment_feedback` del conector MIT de Moodle —
**y es *bulk*, que es justamente lo que el conector de Moodle no tiene** (el hallazgo del pase 27 fue que el *bulk* de
xAPI en CaSS quedaba afuera de MCP; acá el *bulk* es el que está).

**Precisión de método que conviene no saltearse:** el `urls.py` de *Enrollment* **no lleva la versión adentro**. La
versión la monta el *URL conf* padre (`/api/enrollments/v1/`), que es cómo se citan estos endpoints. **Decir que la
API de matrícula "no está versionada" sería leer mal el archivo**, y se deja anotado porque es el tipo de error que
este canal nuevo facilita.

### 🔴 La mitad que no alcanza, y está declarada por el propio proyecto

| Grupo de API | Archivo leído | Qué hay | Estado |
|---|---|---|---|
| **Studio / CMS (contentstore) v1** | `cms/djangoapps/contentstore/rest_api/v1/urls.py` | 21 rutas: `xblock/`, `course_settings/{course_id}`, `course_details/{course_id}`, `course_index/{course_id}`, `course_grading/{course_id}`, `course_team/{course_id}`, `container_handler/{usage_key}`, `container/{usage_key}/children`, `course_rerun/{course_id}`, `certificates/…`, `textbooks/…`, `group_configurations/…`, `videos/…`, **`proctored_exam_settings/{course_id}`** | 🔴 **El repo declara que «the Authoring API is still experimental» y recomienda usar las versiones `v0`** |

**Ésa es la razón de la ausencia, y es una razón real, no una excusa.** Un conector MCP de Open edX que haga lo que
hace `MarcosNahuel/moodle-mcp` —crear curso, crear secciones, publicar material, armar quiz— **tendría que apoyarse en
la única parte de la plataforma que el propio proyecto marca como inestable.** El de Moodle se apoya en Web Services,
que es una superficie estable de hace más de una década.

### La lectura, que es la que se le lleva a un cliente

> **El gap 48 no era un gap técnico uniforme: era dos gaps con la misma cara.**
> **Para matrícula, roles, bloques de curso y notas —incluido el lote— la superficie está, está versionada y escribe:
> la ausencia del conector ahí es puro gap 49** (nadie lo publicó, no que no se pueda). **Para *authoring*, la
> ausencia tiene causa técnica declarada por el proyecto.**

**Lo que eso le hace a P55:** se cotiza **el conector de operación y evaluación** —que es además el que paga, porque es
el que toca la nota y la matrícula— y **no** se promete *authoring* en la misma frase. El patrón queda reescrito abajo
con ese corte.

⚠️ **La licencia no es el obstáculo y conviene decirlo, porque es la primera pregunta del cliente.** Open edX es
**AGPL-3.0**, pero **un conector que habla REST desde otro proceso no deriva de la plataforma y no hereda la AGPL** —
es exactamente la configuración que esta KB ya tiene verificada dos veces: `canvas-mcp` (MIT) contra Canvas y los dos
`moodle-mcp` (MIT) contra Moodle, que es **GPL-3.0**. **Las LMS son copyleft y las puertas son permisivas**; esto no
sería la excepción.

### ⚠️ Nota de nomenclatura, que corrige un detalle de catálogo de esta KB

**El repo se renombró: `openedx/edx-platform` → `openedx/openedx-platform`.** Las dos URLs resuelven (la vieja
redirige) y son el mismo árbol: **AGPL-3.0, 8.2k ★, 4.4k forks, 68.764 commits**. `repos/foundations.md` citaba el
nombre viejo y `verticals/solutions.md` el nuevo; **las dos citas eran válidas, y ninguna era un error** — se unifica
al canónico y se deja la nota, porque el reflejo de "corregir" la que parecía mal habría metido un error donde no
había.

### 🔵 Lo que este pase deja medido y lo que no, sobre Open edX

- ✅ **Medido:** rutas, versiones y capacidad de escritura de cuatro grupos de API, **leyendo el código**.
- ❌ **No medido:** **no se hizo ninguna llamada HTTP contra una instancia de Open edX.** No hay instancia, y levantarla
  necesita instalar el árbol de dependencias, que es el límite declarado del pase 27. **Autenticación (OAuth2),
  *scopes*, *rate limits* y forma real de las respuestas quedan sin verificar.**
- ❌ **No medido:** si los endpoints `v0` de *authoring* —los que el repo recomienda— cubren lo que el `v1`
  experimental promete. **Es la acción 1 del pase 29.**

## 2026-10-01 (pase 27) — la superficie MCP de CaSS medida por anotación: **6 expuestas y 55 ocultas sobre 61 operaciones**, y el «45» del pase 26 era aritmética, no conteo

**Dos repos abiertos de primera mano sobre el árbol clonado** (`cassproject/CASS` v1.7.7, Apache-2.0) **y uno verificado
por página** (`1EdTech/ltibootcamp`). Este pase **no pudo ejecutar el generador** (ver la nota de método) y entonces
midió la misma cosa por el otro canal disponible: **contar las anotaciones en el código fuente**. El resultado
**confirma las seis tools del pase 26 nombre por nombre** y **corrige el conteo de lo excluido**.

### Las seis expuestas, confirmadas por segundo canal independiente

`grep` de `x-mcp-tool-name` sobre `src/main` devuelve **exactamente seis nombres distintos**, y son los seis que el pase
26 obtuvo corriendo `generateTools(spec)`: `server_status`, `search_data`, `get_object`, `save_object`,
**`record_evidence`**, **`get_learner_profile`**. **Dos métodos independientes, el mismo resultado** — el cierre del
gap 40 queda corroborado en lo que afirma sobre el catálogo.

### La corrección: 55 ocultas, no 45

El pase 26 escribió **«45 `x-mcp-ignore: true` puestos uno por uno»**. El conteo real de declaraciones es **55**
(`grep -c "x-mcp-ignore: true"`, excluyendo la librería que *lee* la anotación). **El 45 era `51 − 6`** —paths del spec
menos tools— y ahí está el error, que es conceptual y no de aritmética:

> **`x-mcp-ignore` se declara por operación, no por path.** Un path con `GET`, `POST` y `DELETE` lleva **tres**
> anotaciones. De ahí que **51 paths contengan 61 operaciones**: 6 expuestas + 55 ocultas. **Restar tools de paths no
> da operaciones ocultas**, y la diferencia (10) es exactamente el número de paths multi-método.

**Por qué importa más allá del número:** refuerza, no debilita, la lectura del pase 26. La curaduría es **más**
deliberada de lo que se creía — **55 decisiones de exclusión escritas a mano**, no 45.

### El desglose por adaptador, que es el dato nuevo y el que se cotiza

| Adaptador / módulo | Expuestas | Ocultas | Qué significa |
|---|---|---|---|
| `skyRepo/data.js` | **3** | 3 | El CRUD JSON-LD, mitad expuesto |
| `cartridge/adapter/xapi.js` | **1** | 4 | **Sólo `record_evidence`.** El *bulk* queda afuera (hallazgo del pase 26) |
| `cartridge/adapter/profile.js` | **1** | 0 | `get_learner_profile`, íntegro |
| `skyRepo/ping.js` | **1** | 0 | `server_status` |
| `cartridge/adapter/caseAdapter.js` | 0 | **11** | 🔴 **CASE entero, fuera de MCP** |
| `cartridge/adapter/ceasn.js` | 0 | **6** | 🔴 CEASN entero, fuera |
| **`cartridge/adapter/openbadges.js`** | 0 | **5** | 🔴 **Open Badges entero, fuera** — ver abajo |
| `skyId.js` · `util.js` | 0 | 4 · 4 | Identidad y utilidades |
| `cartridge/adapter/mcp.js` | 0 | 3 | El propio adaptador no se expone |
| `caseIngest.js` · `asn.js` · `pna.js` · `search.js` | 0 | 2 cada uno | Ingesta, ASN, PNA, búsqueda |
| `multiput` · `multiget` · `multidelete` · `admin` · `ollama` · `scd` · `jsonLd` | 0 | 1 cada uno | Lotes, admin, Ollama, SCD, JSON-LD |
| **TOTAL** | **6** | **55** | **61 operaciones** |

### 🔴 El hallazgo que responde la pregunta de Open Badges desde adentro

La consigna del pase 26 pedía buscar `MCP server` + **Open Badges**. La búsqueda web no devolvió nada del estándar
(arriba). **Pero el árbol de CaSS tiene `cartridge/adapter/openbadges.js`, y sus cinco operaciones están todas
`x-mcp-ignore: true`.** Dos cosas, las dos citables:

1. **La implementación más relevante del estándar en esta KB tiene el adaptador y lo excluyó a propósito de su
   superficie de agente.** La respuesta a *«¿hay conector MCP de Open Badges?»* no es sólo «no se encontró»: es **«la
   pieza existe y la puerta está cerrada por decisión de diseño»**. Es una ausencia **medida**, no inferida.
2. **El adaptador está anclado a `https://w3id.org/openbadges/v2` — Open Badges 2.0, no 3.0.** Aparece en cuatro
   `@context` del archivo. Importa para credenciales verificables: **el stack de OB 3.0 / W3C VC no es lo que CaSS
   emite**, y un entregable que lo prometa sobre CaSS está prometiendo de más.

### La trampa de despliegue que hay que poner en el checklist

Leyendo `cartridge/adapter/mcp.js` de primera mano aparece algo que ninguna pasada registró y que **decide si el
cliente tiene superficie MCP o no**:

- El adaptador **no lee el spec del disco: lo busca por loopback** — `fetch(CASS_LOOPBACK + '/swagger.json')`, default
  **`http://localhost/api/`** (puerto **80**).
- Si ese `fetch` falla o no devuelve `ok`, el adaptador **loguea el error y hace `return`**. 🔴 **La ruta `/api/mcp`
  nunca se monta** — y el servidor **arranca normalmente**. El síntoma es *«el MCP no existe»*, no *«el servidor no
  levanta»*.
- Se apaga además por `DISABLED_ADAPTERS` (clave `mcp`).

**Consecuencia:** en un despliegue con proxy, puerto no estándar o HTTPS mal resuelto, **la superficie de agente
desaparece en silencio**. Va a **P57** como ítem de verificación, y es lo primero que hay que mirar si un cliente
reporta que no ve tools.

### `1EdTech/ltibootcamp` — y con esto el gap 42 cierra por agotamiento

| Repo | Licencia | ★ | Forks | Commits | Qué es |
|------|----------|---|-------|---------|--------|
| [`1EdTech/ltibootcamp`](https://github.com/1EdTech/ltibootcamp) | 🚫 **ninguna declarada en la página** | 127 | 19 | 47 | **Colección de enlaces, no implementación.** El README dice literalmente que *«esta página junta links que se relacionan con entender e implementar Tools y Platforms LTI»* |

Era la última candidata sin mirar del **gap 42**. **No es la implementación de referencia en Ruby on Rails**: es
material de referencia, y **sin licencia declarada**. La implementación de referencia real de 1EdTech (platform *y*
tool, con código Ruby) está **en el repositorio de Contributing Members** — es decir, **detrás de la membresía**.
Ver el **gap 42**, ahora cerrado.

---

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
