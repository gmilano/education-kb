---
industry: education
region: Global
updated: 2026-10-04
---

# 🏗️ Repos fundacionales — education

> Bases sobre las cuales construir. Verificado repo por repo vía WebFetch el 2026-09-30 (capas del pase 10, el 2026-10-01).
> Leer la columna **Licencia** antes de proponer: media KB de educación es GPL/AGPL, no permisiva.
> **Pase 100 del 2026-10-04:** 🟢 **1 alta fundacional, y es la pieza que COMPLETA una capa que este archivo tenía a medias desde el pase 14: el MODELO de evaluación de pronunciación.** `YuanGongND/gopt` (**BSD-3-Clause**, `LICENSE` 1.517 B, titular `Yuan Gong`, 2022) es GOPT —ICASSP 2022, MIT & PAII—, el primer modelo que puntúa **múltiples aspectos** (exactitud, fluidez, prosodia) en **múltiples granularidades** (fonema, palabra, oración) a la vez, y es **SOTA sobre `speechocean762`**, que es justo el corpus que este archivo ya inventariaba. 🔴 **Pero el hallazgo del pase es contra esta base, y este archivo es la prueba: el pase estuvo a punto de publicar la capa de habla como NUEVA, y la «Capa de habla y lectura oral» está acá desde el pase 14** con `OpenPronounce`, `kaldi` y `speechocean762` — **incluido el hallazgo de que el corpus no trae archivo de licencia**, que el pase iba a anunciar. 🟢 **`P311`: ningún control de esta base preguntaba «¿esto ya está acá?» —todos auditan una afirmación que el pase HACE, y la de que un alta es NUEVA es implícita— así que el gate quedó escrito y corrido antes de publicar** (`p311`, **11/11**; 14 slugs → **5 ya publicados**, con archivo, línea y sección). 🔴 **La cadena permisiva de esta capa queda CERRADA como irresoluble desde acá, y es una corrección de alcance sobre el pase 14:** ese pase dejó *«pedir los términos a SpeechOcean por escrito»*, y este intentó la vía de **registro** con la que `P306` desempató `examplary/qti` vía npm — **`openslr.org` y `huggingface.co` dan los dos `000` por egreso bloqueado**. **Se puede construir el evaluador entero permisivo (`OpenPronounce` MIT + `gopt` BSD-3 + `kaldi` Apache-2.0) y NO se puede verificar la licencia del corpus contra el que todo el campo se mide.** 🔴 **Y `P308`: 3 de 18 anclas del control compartido eran frase cruda; la del Unlicense INVIERTE el veredicto comercial a `NONCOMMERCIAL-NOT-OSI`, y la ventana del bloque de título contaba LÍNEAS, lo que perdía la AGPL de `P288`.** 🟢 **`lib/license_family.sh` 62/62 → 79/79; 51 suites pasan, 0 fallan.** Ver **`P308`**–**`P311`**.
> **Pase 99 del 2026-10-04:** 🟢 **7 altas fundacionales, y son DOS CAPAS que este estante no tenía: el ALMACÉN xAPI y la librería de ÍTEMS QTI.** El barrido obligatorio (`open source platform education ERP CRM MIT Apache`) devolvió por vigesimosexta vez el eje generalista (ERPNext/Frappe, Odoo, OFBiz, Huly, AureusERP) — **cero** piezas fundacionales educativas nuevas. 🟢 **Pero el EJE ROTADO que el pase 98 pre-registró sí rindió: 15 candidatas medidas → 9 licenciadas, 6 sin cesión**, y 7 de las 9 son repo fundacional. 🔵 **Lo que abren no es un tema nuevo sino la OTRA MITAD de dos temas que esta base tenía a medias: tenía el CLIENTE xAPI (`learnmcp-xapi`) y no el ALMACÉN; tenía REPRODUCTORES de ítems QTI (`qti3-item-player`, `pie-qti`) y no las librerías de GENERACIÓN y MIGRACIÓN.** 🔴 **`P304` — el ancla BSD del control compartido estaba escrita como FRASE CONTIGUA y perdía una familia PERMISIVA:** `instructure/QTIMigrationTool` es BSD-3-Clause real (University of Cambridge, 1.392 B) y volvía `UNCLASSIFIED`, porque su oración de concesión inserta *«of this software»* y *«(where applicable)»* dentro de la frase canónica. **Cuarto eje del mismo defecto** (`P171` cuerpo-vs-título, `P288` caja, `P299` palabra-vs-subcadena, `P304` frase-vs-tokens-ordenados). 🟢 **`lib/license_family.sh` 50/50 → 62/62** (3 controles negativos), **51 suites pasan, 0 fallan**. 🔴 **`P305` — `adlnet/xapi-lab` declara DOS familias en DOS payloads del mismo repo:** `LICENSE` dice **MIT** (titular `Tyler Mulligan`, 2015) y el `README` dice **Apache-2.0** (titular `Advanced Distributed Learning`, 2016) — **familia, titular y año discrepan a la vez**, y la obligación de atribución corre hacia una parte distinta según cuál gobierne. 🟢 **`P306` — `examplary/qti` ≡ `examplary-ai/qti`, byte-idénticos en 3 archivos, y el REGISTRO desempata:** `registry.npmjs.org/@examplary/qti` nombra `github.com/examplary/qti` como canónico y confirma `MIT` por un canal independiente del payload. Ver **`P304`**–**`P306`**.

> **Pase 97 del 2026-10-04:** 🔴 **Sin repos fundacionales nuevos — el barrido `github trending education AI 2026` (año CALCULADO) devolvió por vigesimoquinta vez el eje generalista: 6 de infra de agentes, 4 de currículo para formar ingenieros de AI, 0 de la industria educativa, y las seis cifras de estrellas IDÉNTICAS a las de los pases 95 y 96.** 🟢 **Pero este archivo gana algo que no tenía: la capa de plataforma Java/Maven queda leída por un SEGUNDO canal independiente —la declaración del `pom.xml`— y concuerda con lo publicado.** Medido punta a punta sobre payloads reales: `sakaiproject/sakai` declara `Educational Community License, Version 2.0` → 🟢 **`ECL-2.0`, igual que la fila**; `UniTime/unitime` declara `Apache Software License (ASL), Version 2.0` → 🟢 **`Apache-2.0`, igual**; `DSpace/DSpace` declara `DSpace BSD License` → 🔵 **`BSD`, acuerdo de FAMILIA pero menos preciso que el `BSD-3-Clause` publicado, porque de un nombre de fantasía no sale el número de cláusulas**; `kuali/kc` → 🔴 **`AGPL-3.0`, y el pom es la ÚNICA fuente porque no tiene archivo de licencia entre los nombres sondeados**. 🟢 **4 acuerdos exactos, 1 de familia, 0 contradicciones: el manifiesto es canal CORROBORANTE, no reemplazo.** 🔴 **El cableado que lo hizo posible tuvo que esquivar un defecto propio: con `artifactId` como identidad, `sakaiproject/sakai` (artifactId `base`) sale `FOREIGN` siendo su propio pom raíz** (**P294**). ⚠️ **Y un límite declarado: un `pom.xml` NO responde `P279`** —no nombra archivos de licencia—, así que la pregunta del pase 95 sobre las filas de este archivo fuera de las 200 **sigue abierta** por el lado del nombre de archivo; lo que se cerró es el lado de la **declaración**. Ver `compose/code/p294-pom-in-production/` (**27/27**) y la tendencia **757**.

> 🔴 **Acción pre-registrada para el pase 98, falsable en las dos direcciones y con su número escrito ANTES de correrla.** Este pase midió que el canal de **declaración** es menos preciso que el de **payload** en 1 de 5 casos (`DSpace BSD License` → `BSD`, contra `BSD-3-Clause` leído del archivo), y la pregunta que eso deja abierta es si esa pérdida es **estructural** —los poms de esta vertical declaran prosa— o **incidental** —DSpace es el raro—. **Acción:** sondear el `pom.xml` de **seis** repos Java/Maven educativos NO tocados por este pase, nombrados a mano (el entorno niega enumerar destinos en lote), y clasificar cada `<name>` en **PROSA** (`Apache Software License (ASL), Version 2.0`) o **SPDX PRECISO** (`BSD-3-Clause`, `Apache-2.0`). **Predicción pre-registrada: 0 de 6 declararán un identificador SPDX preciso**, o sea que la pérdida de precisión de `P296` es estructural en esta vertical. 🔵 **Qué la refuta:** **una sola** declaración SPDX precisa en los seis — y entonces el canal de declaración puede, a veces, ser **más** preciso que una lista fija de nombres de archivo, y `P296` hay que reescribirlo con esa rama. ⚠️ **Lo que NO puede pasar es que se publique sin número:** si el entorno niega las seis sondas, se dice *no se pudo correr* como hizo el pase 96, y no se rellena.

> **Pase 96 del 2026-10-04:** 🔴 **Sin repos fundacionales nuevos — el barrido `github trending education AI 2026` (año CALCULADO) devolvió por vigesimoquinta vez el eje generalista, con las SEIS cifras de estrellas idénticas a las del pase 95: 6 de infra de agentes, 4 de currículo para enseñar AI a ingenieros, 0 de la industria educativa (`P281`, con fuentes distintas).** 🔴 **Pero el pase encuentra un defecto en el CONTROL COMPARTIDO que clasifica la columna «Licencia» de este archivo: `lib/license_family.sh` devolvía `GPL-3.0` para una AGPL-3.0 real.** El mecanismo: su rama AGPL es un glob de `case` —**sensible a la caja**— así que un payload AGPL *reflowed* sin el título canónico en mayúsculas cae por ahí, y lo atrapa la rama GPL, que usa `grep -qi` y matchea **el preámbulo de la propia AGPL** («*The GNU General Public License permits … access it on a server*»). 🔵 **Es `P171` reabierto por el eje de la CAJA, sobre el par exacto que P171 existe para proteger — y es `P126` punto 2 literal: las 41 aserciones pasaban y NINGUNA ejercitaba el caso, porque todas las fixtures AGPL de la suite traen el título en mayúsculas.** 🟢 **Arreglado con el ancla de la sección 0 (`refers to version 3 of the GNU Affero…`, que la §13 de la GPL-3.0 NO contiene: dice «*under*») y con su control negativo versionado — `compose/code/p288-agpl-casefold/` **9/9**, suite vieja intacta **41/41**.** ⚠️ **Alcance declarado y NO extrapolado (`P286`, la lección del pase 95): 141 veredictos `GPL-3.0` viven en 21 archivos de resultado versionados y 94 ya dicen `AGPL-3.0`, pero este pase NO predice cuántos están mal — el defecto exige DOS condiciones simultáneas (payload AGPL *y* sin título en mayúsculas) y sólo un barrido lo mide. Lo falsable sin número: el arreglo sólo puede mover veredictos en UN sentido, `GPL-3.0` → `AGPL-3.0`; si un re-barrido mueve una fila al revés, el arreglo es inseguro.** 🔴 **Y la acción pre-registrada del pase 96 NO se pudo correr: el entorno niega construir la lista de destinos en lote (`[Exfil Scouting]`, 2 intentos, 2 vías), así que no hay TSV y no se inventa uno.** 🟢 **Su pregunta igual quedó respondida, y mejor que con un número: la lista de manifiestos de `p283` (`pyproject.toml package.json composer.json Cargo.toml setup.cfg`) NO incluye `pom.xml`, y la capa de plataforma de este archivo es JAVA/MAVEN — el instrumento estaba CIEGO a la capa a la que se lo apuntó. La tasa de `P279` ahí no es 0 ni alta: es NO MEDIBLE con el instrumento pre-registrado** (`compose/code/p289-maven-manifest/`, **11/11**, con el negativo que importa: el `pom.xml` de `kuali/kc` nombra la AGPL en un COMENTARIO, así que un lector por `grep` acierta por la vía equivocada). 🔴 **Acción pre-registrada para el pase 97: agregar `pom.xml` a `MANIFESTS` con el extractor de `p289` y re-barrer la capa de plataforma; predicción falsable — las filas Java/Maven hoy `SIN_LICENCIA` se mueven a `SOLO_MANIFIESTO` y NINGUNA al revés. Requiere que el entorno permita enumerar destinos en lote: ese es el permiso que hay que pedir, no permiso de ejecución ni de red.**
> **Pase 95 del 2026-10-04:** 🔴 **Sin repos fundacionales nuevos (el barrido `github trending education AI 2026`, año CALCULADO, devolvió por vigesimocuarta vez el eje generalista: 6 de infra de agentes, 4 de currículo para enseñar AI a ingenieros, 0 de la industria educativa — `P281`).** 🟢 **Pero el pase cierra el hueco que el 94 dejó ABIERTO sobre este archivo: `openedx/XBlock` estaba publicado como Apache-2.0 y el barrido no lo podía confirmar (33 sondas, 0 hits); hoy el payload se LEE —`master/LICENSE.TXT`, 200, abre con `Apache License`— porque el nombre se toma del manifiesto (`license-files = ["LICENSE.TXT"]`) en vez de adivinarse. La fila era CORRECTA y ahora está confirmada por payload.** 🔵 **Y queda medido que `P279` es real pero RARO: 1 de 201 sobre todo lo barrido, 0 de 200 en las filas de agentes (`P286` — la predicción de ~28 del pase 94 falló por un factor de ~28).** 🟢 **Cuatro repos de este archivo ganan familia de licencia leída del payload por reusar `lib/license_family.sh` (`P237`): `kaldi-asr/kaldi` Apache-2.0 (desde `UNKNOWN`), `trilogy-group/oneroster-ts` 0BSD, `nmarafo/OpenDidactia` CC-BY-SA-4.0, y `dssg/student-early-warning` queda `UNCLASSIFIED` porque su licencia académica NO comercial no tiene familia OSI — sigue fuera de lo que Globant puede construir encima.** 🔴 **Acción pre-registrada para el pase 96: correr `p283/sweep_named.sh` sobre las filas de ESTE archivo y de `verticals/solutions.md` que no están en las 200, que es el único sitio donde la tasa de `P279` puede subir.**
> **Pase 94 del 2026-10-04:** 🔴 **Sin repos fundacionales nuevos, y el barrido global devolvio por NOVENA vez el eje generalista — pero el cero se publica con denominador ENUMERADO: `kouweizhu/agents-radar` #328, fechado el mismo 2026-10-04, lista 47 repos y 0 son de la industria educativa** (**P281**: su etiqueta `[EDUCATION]` marca curriculos para enseñar AI a ingenieros —`rasbt/LLMs-from-scratch`, `rohitg00/ai-engineering-from-scratch`, las dos YA en esta base— y no software que sirva a una institucion). 🔴 **El aporte del pase cae sobre una fila de ESTE archivo y es un defecto del INSTRUMENTO: `openedx/XBlock` se publica como Apache-2.0 —y es CORRECTO— pero el barrido de licencia no lo podia confirmar: 11 variantes de nombre × 3 ramas = 33 sondas, 0 hits, con el testigo de alcance en verde (`master/README.rst`, 200).** 🟢 **El payload es `master/LICENSE.TXT`, con la EXTENSION en mayuscula, y abre con `Apache License`. El nombre no hay que adivinarlo: `pyproject.toml` lo NOMBRA —`license = "Apache-2.0"`, `license-files = ["LICENSE.TXT"]`** (**P279**). 🔴 **Consecuencia directa para este archivo: si `P279` se reparte como en el control positivo (1 de 7), hay ~28 de las ~200 filas `org/repo` que los pases 62/64 barrieron cuyo veredicto de licencia es un hueco de nombre y no un dato. Queda PRE-REGISTRADO como accion 1 del pase 95.** 🔵 **Y la rama por defecto de XBlock es `master`, no `main`: caso de `P278` en el eje del nombre del payload.**
> **Pase 93 del 2026-10-04:** 🔴 **Cero altas fundacionales, SEXTO pase consecutivo, y se declara.** El barrido (`open source platform education ERP CRM MIT Apache`) devolvio por **decimonovena** vez el catalogo ya verificado de este estante, y volvio a nombrar la *Kuali Foundation* en PRESENTE —medida en el pase 42: cuatro repos, los cuatro muertos hace 6–9 años. 🟢 **Lo que si cambia: este estante recupera la capacidad de sostener una AUSENCIA, que `P274` le habia retirado sin reemplazo.** Un clon `--filter=blob:none --no-checkout --depth 1` + `git ls-tree -d -r` enumera el arbol **completo** (< 1 s en ILIAS; 10.923 directorios en Moodle) sin truncar y sin `api.github.com`, que este arbol registra en **403** desde el pase 89 (**P275**). 🟢 **Cuatro filas pasan de *sostenidas por manifiesto + arbol truncable* a *sostenidas por arbol COMPLETO*, las cuatro con CERO capa de AI en el nucleo:** `frappe/erpnext` (39 modulos), `frappe/education` (11), `openeducat/openeducat_erp` (15, en la **raiz**) e `ILIAS` (180 en `release_11`). Para un *engagement*: la capa agentica sobre estas piezas es **desarrollo completo**, no integracion — y ahora es medido. 🔴 **`P278`: la ruta que contiene los modulos es propiedad de la (repo, ref)** —`components/ILIAS/` da 180 en `release_11` y **CERO** en `release_9`, donde viven en `Modules/`(54)+`Services/`(126)— **asi que todo conteo anclado a una ruta fija tiene fecha de vencimiento.** ⚠️ **Cota: mide el arbol publicado en esa ref, nada dice de plugins de terceros** (donde vive la AI de ILIAS y la del ecosistema Frappe). Instrumento: [`compose/code/p275-tree-enumeration/`](../compose/code/p275-tree-enumeration/).
> **Pase 92 del 2026-10-04:** 🔴 **Cero altas fundacionales, QUINTO pase consecutivo, y se declara.** El barrido de plataformas (`open source platform education ERP CRM MIT Apache`) devolvió por **decimoctava** vez lo que este estante ya tiene (`OpenEduCat` sobre Odoo, `CK-ERP`, `ERPNext`/`frappe/education`, Moodle, Open edX, Chamilo, ILIAS). 🟢 **Lo que sí cambia, y afecta a CÓMO se lee este estante entero: dos de sus plataformas tienen una capa de proveedores de modelo EN EL NÚCLEO, y el manifiesto no la muestra.** Medido por ref (**P273**): `chamilo/chamilo-lms` liga **0 → 5 → 6** proveedores según versión en `src/CoreBundle/AiProvider/`, con `composer.json` en **cero tokens en las ocho refs**. 🔵 **Consecuencia para este estante: antes de clonar hay que preguntar la VERSIÓN, no sólo el repo** — el mismo repo da tres respuestas distintas a «¿qué proveedor tengo sin código de terceros?». 🟢 **Y las otras tres filas de este estante SOSTIENEN su veredicto medidas por ref:** `ILIAS` (sin componente de AI en el tramo **A–L**; **M–Z no listado**, se declara), `frappe/education` y `frappe/erpnext` (árbol completo, cero módulos de AI; la capacidad es de **apps de marketplace** de terceros). 🟢 **`openeducat/openeducat_erp` pasa de NO-CLAIM a MEDIDO y es `P270` otra vez:** el pase 90 probó `requirements.txt` → 404 y correctamente no afirmó ausencia; el manifiesto **real** es `openeducat_core/__manifest__.py` (200 en `16.0`, `17.0`, `18.0`), con `'depends': ['board','hr','web','website']` y cero proveedores. ⚠️ **Licencias de la capa, novena y décima lectura de payload: Chamilo `GPL-3.0`, OpenEduCat `LGPL-3.0` — sigue CERO permisivas en capa de plataforma** (tendencia **701**).
> **Pase 91 del 2026-10-04:** 🔴 **Cero altas fundacionales, CUARTO pase consecutivo, y se declara.** El barrido de plataformas (`open source platform education ERP CRM MIT Apache`) devolvió por **decimoséptima** vez lo que este estante ya tiene (`OpenEduCat` sobre Odoo, `CK-ERP`, `ERPNext`/`frappe/education`, Moodle, Open edX, Chamilo, ILIAS). ⚠️ **`CK-ERP` venía como posible alta y NO entra: `grep` contra el árbol lo encuentra ya archivado en 6 archivos**, y su rastro público es de 2010 — es cobertura, no hallazgo. 🟢 **El aporte es una columna que este estante nunca midió: el MANIFIESTO DE RUNTIME de la capa de plataforma, leído POR REF y no en la rama por defecto.** Medido así, `openedx/edx-platform` trae **`openai==0.28.1` declarada DIRECTA** (`via -r requirements/edx/kernel.in`) en las tres releases nombradas que resuelven —`quince` (l. 767), `redwood` (l. 767), `sumac` (l. 809)— y **no** la trae en `master`. 🔴 **Consecuencia de entrega: `0.28.1` es la última release PRE-1.0 del SDK de Python de OpenAI**, cuya API no es la de `openai>=1.0` (`openai.OpenAI()`), así que un engagement que caiga en un Open edX Quince/Redwood/Sumac se choca con un **major antiguo en el core**, no en su propio código. Instrumento y datos crudos: [`compose/code/p272-platform-ref-verdict/`](../compose/code/p272-platform-ref-verdict/) (**P272**).
> **Pase 90 del 2026-10-04:** 🔴 **Cero altas fundacionales, tercer pase consecutivo, y se declara.** El barrido de plataformas (`open source platform education ERP CRM MIT Apache`) devolvió por decimosexta vez lo que este estante ya tiene (`OpenEduCat`, `ERPNext`/`frappe/education`, `Moodle`, `Open edX`, `Chamilo`, `ILIAS`) — es una medición de la COBERTURA de este archivo, no un hallazgo. 🟢 **El aporte es una columna que este estante nunca midió del payload: la LICENCIA de la capa de plataforma, leída archivo por archivo.** 8 de 8 verificadas de primera mano (no por política de proyecto, no por la página del repo): `moodle/moodle` **GPL-3.0-or-later** · `openedx/edx-platform` **AGPL-3.0** · `instructure/canvas-lms` **AGPL-3.0** · `chamilo/chamilo-lms` **GPL-3.0** · `ILIAS-eLearning/ILIAS` **GPL-3.0** · `frappe/erpnext` **GPL-3.0** · `frappe/education` **GPL-3.0** · `openeducat/openeducat_erp` **LGPL-3.0**. 🔴 **8 de 8 son COPYLEFT y CERO son permisivas**, así que el foco MIT/Apache/BSD que el encargo pide se cumple en la capa de AGENTE y **en la capa de PLATAFORMA no hay ninguna permisiva que elegir**: la restricción no es de selección, es de entrega. 🔵 **La única fila cuya familia cambia una cotización es `openeducat_erp` (LGPL-3.0)**, y las dos plataformas más grandes son **AGPL-3.0**, que alcanza el uso **en red** — que es exactamente la forma en que se entrega un LMS. ⚠️ **`openeducat/openeducat_erp` queda `NO-CLAIM` en el eje de proveedor**: su `requirements.txt` da 404 en esa ruta y no se afirma ausencia desde una ruta que falla. Instrumento y datos crudos: [`compose/code/p269-provider-release-matrix/`](../compose/code/p269-provider-release-matrix/).
> **Pase 89 del 2026-10-04:** 🔴 **Cero altas fundacionales por segundo pase consecutivo, y se declara en vez de rellenar.** El barrido obligatorio (`open source platform education ERP CRM student information system MIT Apache 2026`) devolvió `OpenEduCat` —con cifras nuevas de producto: **300 módulos, 65 idiomas, 45 localizaciones**, sobre Odoo— y las otras siete que esta base ya archiva (`ERPNext`/`frappe/education`, `Apache OFBiz`, `OpenSIS`, `Moodle`, `Open edX`, `Kolibri`, `INGInious`), **verificado por `grep` contra el árbol antes de escribir esta línea.** 🟢 **Lo único verificado de primera mano son dos forks nuevos de `canvas-mcp`, y NO entran acá: son forks de un repo ya listado.** ⚠️ **Un tercero que el canal dio por vivo, `EastArctica/canvas-mcp`, da 404.**
> 🔵 **Lo que este pase sí le deja a este estante es una regla de lectura antes de proponer, al lado de la columna **Licencia**: `P268` midió que un conteo de capacidades depende de la SUPERFICIE donde se lee, y que el repo canónico de Canvas publica **102** en su `description` y **103** en su README.** 🔴 **Así que «N herramientas» no es criterio de selección hasta que se nombre la superficie — y de 3 repos medidos, CERO es citable sin nombrarla.** La receta de pre-adopción que sale de ahí es [`R-SUPERFICIE`](../compose/patterns.md), con instrumento y suite ([`compose/code/p268-capability-surface/`](../compose/code/p268-capability-surface/), **25/25**).
> **Pase 88 del 2026-10-04:** 🔴 **Cero altas fundacionales, y se declara en vez de rellenar.** El barrido obligatorio de plataformas (`open source platform education ERP CRM student information system MIT Apache 2026`) devolvió **todo lo que esta base ya tiene**: `OpenEduCat` (73+ módulos), `ERPNext` + `frappe/education`, `Apache OFBiz` (Apache-2.0), `OpenSIS`, `Moodle`, `Open edX`, `Kolibri`, `INGInious` — **verificado por `grep` contra el árbol antes de escribir esta línea**. ⚠️ **La única que el canal trajo y este árbol casi no tiene es `Dolibarr` (1 archivo) y NO entra: es ERP generalista, sin módulo educativo propio, y entraría sólo para llenar la cuota de 5.**
> 🟢 **Lo que sí cambia, y es del lado de la DEMANDA: `P262` midió los mandatos curriculares de IA por NIVEL de la autoridad que firma, y de los 4 tramos que obligan hoy (UAE nacional, Pekín provincial, India Clases 3-8 nacional, CABA ciudad) CERO piden una asignatura propia — los 4 piden contenido INTEGRADO en materias que ya están en el horario.** 🔵 **Consecuencia para este estante: el repo fundacional que el mandato vigente pide no es otro framework de agentes, es CAPA DE CONTENIDO CURRICULAR alineada a un currículo nombrado.** 🟢 **Y ahí este archivo está mejor parado de lo que creía: los cuatro esquemas curriculares nacionales del pase 10 y la capa `Edu*` de BigData Lab @USTC del pase 87 son exactamente eso — y hasta hoy ninguna de las dos se había justificado por el lado de la demanda.** Instrumento: [`compose/code/p262-mandate-level/`](../compose/code/p262-mandate-level/), **47/47**.
> 🟢 **Y el tablero entero de `compose/code/` se re-verificó en este pase: 38 invocaciones de suite preexistente (35 Python + 3 shell), 38 con código de salida 0, `Python 3.11.15`** — al revés que los pases 84 y 86.
> **Pase 87 del 2026-10-04:** 🟢 **7 altas fundacionales de una sola vez, y es la primera vez en este estante: no son siete piezas sueltas sino UNA CAPA DE MEDICIÓN EDUCATIVA completa —trazado de conocimiento, diagnóstico cognitivo, testing adaptativo, datasets, NLP de ítems y simulación— de un laboratorio con nombre y dirección: BigData Lab @USTC (`中国科学技术大学大数据实验室`), `bigdata.ustc.edu.cn`, Hefei.** 🟢 **7 de 8 son permisivas (4 Apache-2.0 + 3 MIT, leídas del payload) y 6 de 8 están publicadas en PyPI.** 🔴 **Y la cota que decide si se cotiza o no: el estante está PUBLICADO pero VIEJO. `EduSim` 0.0.2 es de 2019-11-29, `EduData` 0.0.18 de 2021-08-20, `EduKTM` 0.0.10 de 2022-05-18, `EduNLP` 0.0.9 de 2022-11-14; sólo `EduCDM` 1.0.1 (2024-10-25) está vigente. «Hay paquete» NO es «hay mantenimiento» (**P260**).** 🔴 **El titular NO es uniforme dentro del mismo `org`: `EduData` y `EduCDM` dicen `Copyright [2020] [bigdata-ustc]`, pero `EduCAT` dice `Copyright (c) 2019 tswsxk` —un INDIVIDUO— y `EduSim` es fork de `tswsxk/EduSim`. Dos de las ocho no las tiene la institución, y eso cambia a quién se le pide cesión en un contrato.** 🔴 **`EduX` queda AFUERA: es el paraguas del conjunto y es la única SIN LICENCIA.** 🟢 **Y el hueco de APAC, abierto quince pases, cierra acá y por método correcto: la región sale de la bio, el sitio y la ubicación declaradas del `org`, no de un antropónimo (**P261**).**
> **Pase 86 del 2026-10-04:** 🟢 **Cero altas de repo, y una columna nueva para TODA la tabla: la LIGADURA DE PROVEEDOR, medida del manifiesto de runtime.** Hasta este pase, «¿lo podemos usar de base?» se contestaba sólo con la licencia; ahora se contesta además con «¿a qué proveedor de modelo ata al cliente?». 🔴 **El resultado sobre las 69 filas recomendables: `SWAPPABLE` = 0.** Ninguna rutea por `litellm`, `langchain` ni `@ai-sdk/*`, así que **las 10 que ligan son 10 cambios A MANO** si un cliente manda su proveedor. 🟢 **Y la buena noticia es más grande que la mala: 36 son `UNBOUND` y 21 de los 25 servidores MCP no ligan NADA** — la elección de modelo vive en el host, así que construir sobre ellos no compromete al cliente. ⚠️ **21 quedan `NO-CLAIM` (sin manifiesto alcanzable por este canal): no se afirma que no liguen, se afirma que no se pudo leer.** 🔵 **La columna de licencia de esta tabla NO cambia y no se re-litiga** — es otro eje, y `P257` existe justamente para no volver a mezclarlos. Ver `compose/code/p257-provider-binding/` (**37/37**) y las tendencias **667**–**674**.
> **Pase 77 del 2026-10-03:** 🟢 **La tabla de «repo muerto ⇒ licencia no verificada» cierra, y era un patrón y no una excepción: 5 de 5 permisivas** (3 MIT + 2 Apache-2.0) — `compose/code/p234-dead-license-closeout/`, cinco peticiones HTTP. 🆕 **Dos piezas ganan licencia tras 76 pases:** [`EASOL/edfi-to-oneroster`](https://github.com/EASOL/edfi-to-oneroster) (**Apache-2.0**) y [`Transcordia/jupiter`](https://github.com/Transcordia/jupiter) (**MIT**, titular `Transcordia`). 🧾 **Y las dos cotas de titular son Apache-2.0 y son la NORMA, no una anomalía: `EASOL` no trae ninguna línea de copyright y `gotranseo` trae el apéndice sin llenar** (`Copyright [yyyy] [name of copyright owner]`) — el archivo responde el titular **sólo** para MIT/BSD/ISC (**P184**). 🪜 **La capa xAPI medida por CAPA invierte el signo de P230** (**P235**): servidor 🟢 **dos permisivos VIVOS** (`lrsql` Apache-2.0 **2 d** · `ralph` MIT **26 d**) · cliente ⚠️ **permisivos pero TODOS congelados** (`php-xapi/model` MIT **1,7 a** · `TinCanPHP` Apache-2.0 **3,9 a** · `TinCanPython` Apache-2.0 **6,1 a**) · puente 🟡 MIT con el *upstream* congelado **1,1 a**. **8 de 9 permisivas, y la única copyleft (`LearningLocker`, GPL-3.0) es la que está muerta.** 🔵 **Para esta capa la frase comercial es la INVERSA de la de OneRoster: EXPONER xAPI se puede hoy, permisivo y con mantenimiento de esta semana; CONSUMIRLO obliga a bifurcar un cliente congelado.** ⚠️ **Corrección de fecha a esta base: la familia `php-xapi/*` se databa en «último tag 2021-03-24» y el `HEAD` de `php-xapi/model` es 2025-01-20.** ✅ **`gap 79` estaba CERRADO desde el pase 39 y tres archivos de esta KB seguían diciendo «sin resolver» cuatro pases después — reparado acá, en `repos/trending.md` y en `verticals/solutions.md`.** 🔴 **Y la advertencia de instrumento que vale para todo barrido futuro de este archivo: un clasificador de licencias que `grep`-ea el CUERPO marca a `moodle/moodle` como AGPL-3.0**, porque GPL-3.0 §13 se titula *«Use with the GNU Affero General Public License»*. El clasificador pasa a vivir en **`compose/code/lib/license_family.sh`** con test (**12/12**): **no se inlinea uno** (**P237**).
> **Pase 76 del 2026-10-03:** 🔴 **La conclusión de P229 se cae con datos de su propio archivo: `bgwdotdev/go-oneroster` se publicaba 🟢 «vivo» en la tabla de licencias y ⚫ «muerto hace 6,9 años» en la tabla de frescura, a 1.662 líneas de distancia y en el mismo `HEAD`.** Medidas por separado, las tres condiciones (permisiva + viva + spec vigente) las cumplen 🔴 **CERO** piezas, no una. 🟢 **Y el permisivo con el spec VIGENTE que P229 declaró inexistente ya estaba en esta base, sin licencia: [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) — MIT (titular `theopenem`) con `v1p1` + `v1p2`** — porque el pase 75 registró su licencia como *«no verificada: repo muerto»*. 🧪 **«Muerto» no exime de medir la licencia: la hace más importante — un permisivo muerto se BIFURCA, un AGPL muerto no.** 🪜 **El eje nuevo es CAPA: CONSUMIR OneRoster con spec vigente y licencia permisiva se puede hoy; EXPONERLO no** (ningún servidor permisivo en v1p2). 🔴 **Corrección de spec que afecta a toda la capa: v1p1 NO es el spec vigente** — 1.2 se publicó en septiembre de 2022, superó a 1.1 en 2023 (7→14→22 CSV, 38→61→81 endpoints). **5 altas + 1 duplicado registrado; EMEA recupera 2 piezas, las dos sin archivo de licencia.** Instrumento y corrida en `compose/code/p230-rostering-layer-axis/`.
> **Pase 73 del 2026-10-03:** 🟢 **La «tercera vía permisiva» de la plataforma de sistema educativo nacional (tendencia **24**) deja de ser hipótesis y tiene repositorio:** [`motiolabs-space/open-academic`](https://github.com/motiolabs-space/open-academic) — **MIT** medido (1.087 B, titular `PT Motiolabs Digital Indonesia`, persona jurídica), SIAKAD completo de admisión a graduación **con el reporte obligatorio al Estado ya construido** (PDDIKTI/Neo Feeder idempotente con *ledger* y diff, SISTER, KIP Kuliah, LKPS, IKU). 🔵 **0 ★ y 75 commits: el caso de libro de la tendencia **23** —las estrellas esconden la infraestructura desplegada—.** 🟢 **Y rompe la anti-correlación de **P209**: permisiva Y específica a la vez, desde APAC.**
> **Pase 72 del 2026-10-03:** 🟢 **La capa de SIS gana su primera pieza LATAM y trae el único patrón de CREDENCIAL del inventario:** [`iDavi/usp-mcp`](https://github.com/iDavi/usp-mcp) + [`iDavi/heidy_backend`](https://github.com/iDavi/heidy_backend) (**GPL-3.0**, 35.148 B cada uno, Brasil) **sellan la Senha Única de la USP contra la clave pública del backend antes del login — ninguna otra pieza de esta base evita la contraseña en claro.** 🔴 **Y las dos cotas están medidas con test ejecutable y control negativo** (**P213**, 13 checks): los metadatos del sobre **no** están autenticados (el AAD es una constante) y el *key schedule* **no** es RFC 9180, así que el sobre interopera con UN backend. ⚠️ **Tercer corte institucional consecutivo ganado por copyleft** — para esta vertical, «permisivo» ya es la excepción, no el caso base.
> **Pase 68 del 2026-10-03:** 🟢 **Entran los DOS documentos de estándar que ceden de verdad, y son la corrección más útil que este archivo recibió sobre la capa: [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) (**Apache-2.0**, 11.525 B, 952 ★, 403 forks) y [`Ed-Fi-Alliance-OSS/Ed-Fi-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Standard) (**Apache-2.0**, 10.173 B, 46 ★, v6.2.0) publican el DOCUMENTO normativo bajo licencia permisiva, así que un perfil derivado se puede entregar con atribución y sin trámite.** 🔴 **Eso REFUTA lo que este archivo publicó en el pase 67 —*«la capa de estándares es la PEOR cedida de todas»*—: el régimen no se parte por «ser un estándar», se parte por **PUBLICADOR × TIPO DE ARTEFACTO**, sin una sola excepción en 8 archivos leídos** (**P191**). 🔴 **1EdTech cede su SOFTWARE bajo Apache-2.0 (4 de 4: OpenCASE, los dos validadores, la librería LTI 1.3) y sus DOCUMENTOS bajo la licencia que NIEGA derivados (2 de 2).** ⚠️ **Hueco nuevo y de los que importan: la versión VIGENTE de xAPI (IEEE 9274.1.1-2023) ya no está en GitHub —vive en `opensource.ieee.org`, que este entorno tiene EGRESS-BLOQUEADO—, así que los cuatro instrumentos de licencia de esta KB, todos apuntados a `raw.githubusercontent.com`, son ciegos a un estándar que migra** (**P195**). 🟢 **Y una pieza de agente: [`aemonge/opencode-sit`](https://github.com/aemonge/opencode-sit) (MIT, tutor socrático como plugin de OpenCode), con la identidad probada por `sha256` porque el paquete no declara repositorio** (**P193**). Ver `compose/code/p191-spec-license-sweep/`.
> **Pase 67 del 2026-10-03:** 🟢 **Entra la capa de CORRECCIÓN automática, que esta base tenía representada por UNA pieza: `INGInious` (AGPL-3.0, 243 ★, 150 forks, **UCLouvain** → EMEA) como *grader* externo de Moodle y edX vía LTI, más `webtech-network/autograder` (Apache-2.0), `johnswyou/autograder` (MIT, corrige MANUSCRITO con rúbrica y cola de revisión humana) y `zmievsa/autograder` (GPL-3.0) — las cuatro con el archivo de licencia LEÍDO.** 🟢 **Y APAC gana un índice regional con la cesión más limpia de toda la capa de dato de esta KB: `crpf-mitadt/Indian-AI-for-Education`, **CC0 1.0** (dominio público: ni atribución ni ShareAlike).** 🔴 **La corrección que este archivo tiene que hacerse: `IMSGlobal/openbadges-specification` figuraba como *«ninguna (ausencia MEDIDA) … alcanzable y sin cesión»* y es una ausencia FALSA — `ob_v3p0/license.md` trae 12.324 B de la *Specification Document License* de IMS Global, que ⚠️ **NIEGA los derivados**, o sea una cesión PEOR que el silencio para un entregable** (**P187**). 🔵 **El detalle de la fila vieja era correcto —los 14 nombres dan 404 en la RAÍZ— y el error fue leer «no hay licencia en la raíz» como «no hay cesión».** ⚠️ **Nuevo patrón de alcance: el `LICENSE` de `INGInious` declara cubrir *«la mayoría de los archivos»* y delega las excepciones a los encabezados por archivo, y esta base no tiene instrumento para un barrido POR ARCHIVO** (**P186**, gap declarado).
> **Pase 65 del 2026-10-03:** 🟢 **JAPÓN entra a la capa de currículo, y entra como la MEJOR pieza que tiene la KB: `jp-cos/jp-cos.github.io` —学習指導要領LOD— publica el currículo nacional japonés completo en RDF/Turtle bajo **CC BY 4.0**, con 22 volcados versionados, vocabulario, SHACL y endpoint SPARQL declarado.** 🔵 **CC BY 4.0 es MÁS permisiva que la alemana CC BY-SA 4.0: sin ShareAlike, no activa la compuerta de **P178**, así que el currículo derivado puede entregarse con licencia propia.** 🔴 **Y la acción 3 queda REFUTADA en su hipótesis: decía «si está publicado por MEXT sin licencia explícita, APAC replica el patrón alemán y **P174** gana una tercera región» — hay licencia explícita, así que P174 NO gana región por este caso.** 🟢 **La reserva de la tendencia 457 también cae: `dini-ag-kim/school-curriculum-pg` —la cobertura por LAND, que el pase 63 escribió como «la capa que agrega el valor específico y sigue sin licencia»— declara **CC BY-SA 4.0** en las 25 serializaciones, los 16 `lp-land-XX-full.owl` incluidos, con titulares por ORCID.** 🔴 **Las dos cesiones eran invisibles a los instrumentos de esta KB: ninguna está en un archivo `LICENSE` y las dos aparecieron sólo al abrir el dato** (**P172**, **P179**). Ver `compose/code/jp-cos-curriculum-gate/`.
> **Pase 64 del 2026-10-03:** 🔴 **La acción 3 del pase 63 CIERRA y REFUTA el titular del pase 63 sobre Alemania: las TRES ontologías de `FWU-DE` SÍ declaran licencia —**CC BY-SA 4.0**, como anotación `dct:license` DENTRO del `.owl`— mientras no tienen archivo `LICENSE` ni la palabra «licencia» en el README. El pase 63 grepeó el README y concluyó «3 de 3 sin ninguna licencia»: la cesión existía, un nivel más abajo, en el PAYLOAD** (**P172**, y es el caso más fuerte de **P153**). 🔴 **Y la dependencia de la receta **P169** estaba al revés: `dini-ag-kim/school-curriculum-pg` no es el upstream que FWU importa — es una **lápida de 136 bytes** cuyo README entero dice *«This repo is outdated, please go to FWU-DE/lehrplan-ontologie»*, o sea apunta HACIA la pieza sin archivo de licencia** (**P173**). 🔵 **Consecuencia de instrumento: un verificador de licencias que mira raíz + README es ciego a toda la capa de DATO semántico; hay que grepear dentro del RDF/OWL/TTL, y en las DOS serializaciones (`<http://purl.org/dc/terms/license>` e `dcterms:license`).** 🟢 **Alta permisiva verificada: `1EdTech/openbadges-validator-core` (Apache-2.0, 13.184 B), que reemplaza al muerto `concentricsky/badgr-server`.**
> **Pase 62 del 2026-10-03:** 🟢 **+3 repos fundacionales y la capa de currículo extendida a ALEMANIA (`FWU-DE/lehrplan-ontologie`: los 16 Bundesländer en RDF/OWL) y a ESPAÑA (`nmarafo/open-lex-edu`: 832 normas con frontmatter YAML e `index.yaml` de referencias cruzadas).** 🔴 **Y el dato que decide: de SIETE artefactos de currículo medidos en cuatro regiones, exactamente UNO es permisivo y legible (Corea, MIT) — dos son *share-alike*, uno CC BY, DOS NO TIENEN LICENCIA y uno es ilegible. La capa más cara de reconstruir es la peor licenciada, y la región con más presupuesto (NA) y la de mayor cobertura técnica (Alemania) son justo las dos sin cesión.** 🔴 **El `gap 255` del pase 61 se auto-refuta en España: declaraba «sin artefacto» un país que esta base cubre desde el pase 3 en siete archivos — una declaración de hueco tiene que correr contra el índice propio antes de salir a buscar** (**P162**). 🟢 **Y `open-lex-edu` es el control negativo que a P153 le faltaba y lo pasa: su licencia de DATO sí está en la raíz.**
> **Pase 61 del 2026-10-03:** 🟢 **+12 filas fundacionales y las cuatro regiones tocadas, tras varios pases sin altas — porque este pase ejecutó la acción pre-registrada que llevaba ciclos pendiente: buscar `curriculum ontology`, `achievement standards`, `learning map` e `item bank` POR PAÍS, en vez de buscar «agentes educativos».** 🔴 **Leer las DOS columnas de licencia: la capa es dual (código permisivo / dato con atribución) y el archivo del DATO no está en la raíz en dos de tres casos —`dados/LICENSE.md` adentro del directorio de datos, `LICENSE-DADOS.md`, `DATA-LICENSE.md`—, así que el probe de raíz de P114/P115 reporta «MIT» para toda la capa y MIT cubre la parte sin valor** (**P153**). 🟢 **Lo licenciable es la COMPILACIÓN, no el currículo: los textos normativos son actos de Estado no protegidos (art. 8º IV de la Lei 9.610/98; OGL v3.0 como *public sector information*)** (**P154**). 🔴 **Y la asimetría regional invierte el gap 4: LATAM tiene CC BY 4.0 con procedencia por registro, EMEA tiene OGL v3.0 con permiso comercial explícito, APAC tiene publicación oficial del Estado — y North America, el 38 % del mercado, reparte sus estándares entre 50 estados y sus tres renderizaciones JSON en GitHub NO tienen archivo de licencia** (**P159**).
> **Pase 59 del 2026-10-03:** ⚠️ **cero plataformas nuevas y el barrido obligatorio completo (cuatro globales + cuatro regionales, año calculado: 2026) volvió por DUODÉCIMA vez con la capa genérica y material didáctico *sobre* AI.** 🔴 **El hallazgo del pase es de LICENCIA y cambia el ORDEN de los filtros: el MCP de Moodle más estrellado que apareció —`loyaniu/moodle-mcp`, 37 ★, el segundo de toda esta capa tras los 272 de `vishalsachdev`— NO TIENE LICENCIA: `LICENSE` ausente en `main` y en `master` y sin clave `license` en `pyproject.toml`. Es inusable por Globant, y las tres permisivas del mismo barrido tienen 0 ★** (**P147**, tercera reproducción de la curva invertida de P134/P138, ahora sobre la licencia). 🔵 **Regla que queda escrita: el filtro de licencia se aplica ANTES del de popularidad, porque el orden inverso selecciona lo que no se puede entregar.** ⚠️ **Corrección de CANAL, y toca al verificador de licencias de esta base: `curl -sI` contra `github.com` devolvió `403` en los OCHO repos probados —el proxy de egreso bloquea `HEAD` sobre el HTML, no es un 404—, así que la verificación se hizo por `raw.githubusercontent.com` (200) y `WebFetch`, dos canales concordantes. Los veredictos de licencia de este pase siguen valiendo porque sus sondas fueron contra `raw`, que responde.** ⚠️ **Nota de instrumento: segunda reproducción consecutiva de la negativa a ejecutar el código clonado, incluidas las suites OFFLINE, así que ninguna cifra de `compose/code/` se re-verificó en este pase.** Ver **P145**–**P148** y las tendencias **402**–**412**.
> **Pase 57 del 2026-10-03:** ⚠️ **cero repos nuevos y el barrido obligatorio completo (cuatro globales + cuatro regionales, año calculado: 2026) volvió por UNDÉCIMA vez con la capa genérica y material didáctico *sobre* AI** — y por segunda vez devolvió una pieza de esta propia base (`DeepTutor`) presentada como novedad. 🔴 **El hallazgo del pase es sobre un repo que esta base ya tenía y cuyo ÁRBOL SE MUDÓ: `moodle/moodle` relocalizó todo el código de la aplicación bajo `public/` en Moodle 5.** Medido con 12 sondas: `main/mod/assign/locallib.php` da **404** mientras `main/public/mod/assign/locallib.php` da **200** y `MOODLE_405_STABLE/mod/assign/locallib.php` da **200**. ⚠️ **Y la nota de instrumento que sale de ahí toca el verificador de licencias de esta base: `main/README.md` y `main/config-dist.php` dan 200 mientras `main/version.php` —de la MISMA raíz— da 404, así que una sonda de rama contra `README.md` NO prueba que el árbol esté en esa rama.** 🔵 **El veredicto «`LICENSE` 404 en `main` y `master`» sigue valiendo como *«no está en esa rama»*, pero no como *«el proyecto no tiene licencia»* cuando el proyecto mudó su árbol. Regla nueva: la sonda tiene que ser el archivo que se va a leer, no un hermano cualquiera** (**gap 250**). 🟢 **El valor del pase está en el instrumento, otra vez: 14 suites corridas OFFLINE con 383 aserciones y 0 fallas, una NUEVA (`grading-draft-gate` 37/37, la acción 2 del pase 56) y con TRES MUTACIONES que prueban que la suite nueva puede fallar (31/37, 36/37, 35/37).** 🔴 **Y una corrección que esta base se hace sobre su propia recomendación fundacional: nueve pases citaron el `readyforreview` de `toshieji/moodle-grading-mcp` como el patrón de cumplimiento a copiar, y la lectura del código de Moodle (`public/mod/assign/locallib.php:3001`) muestra que la garantía depende de `markingworkflow=1` en la TAREA — con `markingworkflow=0` Moodle publica la nota igual** (**P139**). ⚠️ **Dato de licencia que no cambia: la pieza de escritura docente mejor guardada de la capa sigue siendo MIT con 0 ★, y la puerta oficial de Open edX sigue siendo AGPL-3.0.** Ver **P137**–**P141** y las tendencias **370**–**392**.
> **Pase 56 del 2026-10-03:** ⚠️ **cero repos nuevos y el barrido obligatorio completo (cuatro globales + cuatro regionales, año calculado: 2026) volvió por DÉCIMA vez con la capa genérica — y esta vez con las cifras idénticas dígito por dígito a las del pase 55** (openclaw **385.407 ★**, dify **151.639**, browser-use **108.128**, Mem0 **62.735**, AutoGen **60.284**, Flowise **55.226**). 🔵 **Dos pases del mismo día con cifras que no se mueven ni un dígito es dato de CANAL, no de ecosistema: el barrido genérico está saturado, y decirlo es más útil que repetirlo.** 🟢 **El valor del pase está otra vez en el instrumento de este repositorio: las 13 suites de `compose/code/` corrieron OFFLINE, dos son NUEVAS (`suite-total-control` 10/10 y `aiact-50-2-exposure/test_exposure.py` 11/11) y dos pasaron a publicar su total propio (`unitime-mcp-gate` **46/46**, `openedx-course-generator` **33/33**), cerrando la acción 2 del pase 55.** 🔴 **Y una cifra de esta base quedó corregida: el conjunto expuesto al Artículo 50(2) es **33 de 66 (50 %)**, no 32/48 % — el pase 45 lo había medido bien (*«32 … más 1 `pack`»*) y la propagación perdió la fila `pack` en cada cita aguas abajo, mientras los dos escáneres de la capa seguían usando 33 como denominador.** ⚠️ **Dato de licencia que no cambia pero conviene repetir antes de cotizar: la única pieza de escritura docente conforme al Artículo 50 es MIT con 0 ★, y la puerta oficial de Open edX sigue siendo AGPL-3.0.** Ver **P132**–**P135** y el patrón nuevo **P136** y las tendencias **338**–**369**.
> **Pase 55 del 2026-10-03:** ⚠️ **cero repos nuevos y el barrido obligatorio completo (cuatro globales + cuatro regionales, año calculado: 2026) volvió por novena vez con la capa genérica y material didáctico *sobre* AI** — openclaw **385.407 ★**, dify **151.639**, browser-use **108.128**, Mem0 **62.735**, AutoGen **60.284**, Flowise **55.226**. 🔵 **Un nombre nuevo que NO entra y queda registrado para no volver a pagarlo: *«Hermes Agent»*, que una secundaria declara MIT con 180.000+ ★ desde feb-2026 — agente general, no educativo, y sin terna.** 🔴 **El valor del pase está en el instrumento de este repositorio, no afuera: las once suites de
`compose/code/` corrieron OFFLINE y las ONCE reprodujeron su cifra publicada.** ⚠️ **Y el pase se corrige a
sí mismo antes de publicar: un `grep` escrito a mano (`^ *ok|PASS`, sin anclar la segunda alternativa) dio
**49** y **34** para las dos suites que no imprimen total propio, y estuvo a punto de publicarse como «dos
cifras vencidas» — el instrumento **versionado** de esta KB (`extract_figures.py`, que ancla `^PASS `) da
**46** y **33**, que es lo que el README ya publicaba.** 🔴 **Lo que invalidó el control: el «control
positivo» (37 = 37 en `sebserver-mcp-gate`) era insensible al defecto, porque esa suite emite líneas `ok` y
no `PASS`.** 🔵 **Dos reglas que quedan (P126): un control positivo que pasa no habilita un instrumento si
no ejercita el caso donde puede fallar, y si el repositorio ya versiona un instrumento para una cifra se
corre ése antes de escribir uno a mano** (tendencia **313**). 🟢 **Y el `gafapa/moodle-core-cli` que esta base viene señalando como «el candidato más barato a envolver» se abarata más: la compuerta de escritura ya existe debajo** (*«read-only mode by default … require `--allow-write` … additionally require `--yes`»*).
> **Pase 54 del 2026-10-03:** ⚠️ **ninguna base nueva, y el pase resuelve la pregunta que el pase 53 dejó abierta sobre la capa de integridad de examen de este archivo — resulta que era el caso FÁCIL.** 🟢 **`SafeExamBrowser/seb-server` queda clasificado leyendo tres archivos de su propio código, y el veredicto es el mejor posible para una entrega europea: `ClientEvent.EventType` son siete valores (`UNKNOWN`, `DEBUG_LOG`, `INFO_LOG`, `WARN_LOG`, `ERROR_LOG`, `NOTIFICATION`, `NOTIFICATION_CONFIRMED`) y `Indicator.IndicatorType` son otros siete (`NONE`, `LAST_PING`, `ERROR_COUNT`, `WARN_COUNT`, `INFO_COUNT`, `BATTERY_STATUS`, `WLAN_STATUS`).** 🔵 **Ni cámara, ni micrófono, ni rostro en el modelo de indicadores: es TELEMETRÍA DE DISPOSITIVO, no observación del alumno — así que no es un sistema biométrico y la pregunta del art. 5(1)(f) no le aplica.** 🟢 **La lectura de arquitectura, que es la más vendible del pase: todo el riesgo de AI Act de un despliegue de SEB Server es IMPORTADO del servicio de sala que se le enchufe en `/admin-api/v1/monitoring/proctoring`** — **el cumplimiento pasa a ser una decisión de proveedor, negociable, en vez de una propiedad del producto.** **Licencia reconfirmada de primera mano: MPL-2.0, leída del `LICENSE` de `master`.** 🔴 **Y la línea que este archivo tenía que leer antes de proponer una base de integridad de examen CAMBIA, porque el pase 53 la clavó al artículo equivocado: no es «¿emite eventos de presencia y foco o infiere estado interno?» sino «¿emite eventos o infiere CONDUCTA?».** Medido sobre los artefactos publicados de las tres piezas permisivas de la capa: **15 términos de afecto, 3 coincidencias crudas, 3 falsos positivos verificados, 0 inferencia de emoción** — así que **el art. 5(1)(f) no parte esta capa**, y lo que hay es **Anexo III con plazo 2027-12-02 más art. 22 GDPR** (ver **P124**). ✅ **Control del pase 53 reproducido de primera mano: `curl -sI` devuelve 403 tanto para `github.com/moodle/moodle` como para un repo inventado — no discrimina; `raw.githubusercontent.com` devuelve 200/404.** ⚠️ **Y el gap 92 suma dos canales, los dos `EGRESS_BLOCKED` y los dos primarios de una afirmación técnica de este pase: `docs.moodle.org` (sexto) y `seb-server.readthedocs.io` (séptimo)** — por eso el ajuste de Moodle que gobierna el canal b4 de **P123** se publica como cita de las piezas y no como nombre de ajuste. Ver **P123**, **P124** y las tendencias **295**–**312**.
> **Pase 53 del 2026-10-02:** ⚠️ **ninguna base nueva, y los dos hallazgos del pase son sobre INSTRUMENTOS de este archivo, no sobre repos.** 🔴 **Primero: el verificador de URLs que la consigna de esta corrida prescribe (`curl -sI`) devuelve 403 para TODO `github.com`, incluidas 4 de 4 URLs verdaderas (`ASEpochs/ai-digital-teacher`, `foradian/fedena`, `francoisjacquet/rosariosis`, `frappe/erpnext`) — un verificador que falla igual para lo verdadero y lo falso no verifica, y aplicado como está escrito habría borrado los cuatro hallazgos.** 🟢 **Los dos canales que sí distinguen en este entorno son `raw.githubusercontent.com` (200/404 reales) y WebFetch sobre `github.com`, y con esos se midió todo el pase.** 🔴 **Segundo, y toca la capa de *proctoring* de este archivo: el art. 5(1)(f) del AI Act PROHÍBE inferir emociones en instituciones educativas desde datos biométricos desde el 2025-02-02, no la difiere a 2027-12-02 — así que la línea a leer antes de proponer una base de integridad de examen es «¿emite eventos de presencia y foco, o infiere estado interno?».** `SafeExamBrowser/seb-server` y su endpoint `/admin-api/v1/monitoring/proctoring` quedan **sin clasificar por este eje** y la acción 2 del pase 54 lo pide explícitamente. ⚠️ **Y el gap 92 suma un quinto canal fallido, por primera vez con causa medida: `eur-lex.europa.eu` y `artificialintelligenceact.eu` devuelven `EGRESS_BLOCKED` por la política de egreso del entorno, así que lo que falta es una allowlist, no más búsqueda.** Ver **P122** y las tendencias **286**–**292**.
> **Pase 52 del 2026-10-02:** 🔴 **la capa de licencia de esta base se midió contra sí misma otra vez y el defecto estaba en el instrumento que el pase 51 acababa de declarar obligatorio: el ancla del tarball era CASE-SENSITIVE.** `@learninglocker/xapi-agents` envía **`package/license`** en minúscula con **35.121 bytes de GPL-3.0** adentro, y el ancla del pase 51 publicaba **raíz=0** sobre eso. 🔵 **Es el mecanismo de la tendencia 252 —un supuesto cultural disfrazado de detalle técnico— una capa más adentro: ya no en una lista de nombres, sino en una expresión regular escrita por el pase anterior.** Corregida e **instrumentada offline**: `compose/code/registry-license-remeasure/test_anchor.py` → **24/24 sin red**, con el defecto reproducido y el control positivo de la tendencia 259 conservado (**144** licencias de `node_modules` → raíz=0). 🟢 **La acción 1 se ejecutó: 11 paquetes re-medidos, 3 veredictos cambian y los tres los resuelve el TARBALL** —`@eduware/oneroster` 0BSD, `@osu-cass/sb-components` MPL-2.0, `@learninglocker/xapi-agents` GPL-3.0—, **mientras los 20 nombres de archivo no aportaron ni un veredicto nuevo en este lote.** 🔵 **La lectura de encuadre: «indeterminado» no era una propiedad de los paquetes, era del canal que se les había aplicado.** ⚠️ **Y el control del HERMANO queda en tercer lugar, con dos límites que nadie había escrito: exige que la organización publique más de un paquete** (no aplica a `Eduware-Inc`, `owentaylor` ni `appliedrelevance`) **y es subordinado al tarball** (en `LearningLocker` todos los hermanos dan 404 y el tarball resolvió la licencia igual). **El orden correcto es 20 nombres → tarball → hermano.** 🔴 **Dos reglas de ALCANCE quedan firmes y son de cotización, no de revisión: `@timeback/*` va 3 de 3 sin licencia** (`qti` 0.4.1 se suma a `oneroster` y `caliper`: sin campo, sin repo, sin texto y sin descripción) **y `@ink-waffle/*` va 2 de 2 con campo MIT y cero texto.**
> **Pase 51 del 2026-10-02:** 🟢 **la nota de arriba —*media KB de educación es GPL/AGPL*— ahora tiene su contraparte MEDIDA en la capa de agentes, y el reparto se invierte: de los 139 repos de `agents/top.md` con texto de licencia verificado, 106 (76,3 %) son MIT o Apache-2.0 contra 16 GPL/AGPL/LGPL.** ⚠️ **Las dos frases no se contradicen: la nota habla de PLATAFORMAS —Moodle, Open edX, Sakai, Chamilo, ILIAS— y el 76,3 % es de la capa de AGENTES. Son dos poblaciones distintas y hay que decir cuál se está citando.** 🔴 **Y el instrumento de licencia de esta base se corrigió a sí mismo: la lista de 4 nombres de archivo producía 4 falsos «sin licencia» de 27 (14,8 %), y el falso más grave era `moodle/moodle` —GPL vía `COPYING.txt`, la pieza central de `verticals/solutions.md`.** Las dos causas son **convenciones de ecosistema**, no descuidos: `COPYING.txt` en el mundo GNU/Moodle y `LICENSE-MIT`+`LICENSE-APACHE` en doble licencia estilo Rust (`contentauth/c2pa-rs`, `c2pa-python`). 🟢 **El gap 248 se recasta y mejora: `@tutors/xapi` y `@tutors/badges` siguen dando 404, pero NO eran citas inventadas —son nombres del PR #341, que está ABIERTO, y un paquete nombrado en un PR sin mergear no está en un registro por definición. El defecto es una cita SIN ETIQUETA DE ESTADO.** 🔵 **Y el alcance estaba mal, lo que había costado SIETE paquetes reales: el proyecto publica en `@tutors-sdk/*` y sin alcance, y las siete son permisivas (MIT ×6, ISC ×1).** Ver **P114** y `compose/code/p114-license-column/`.
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

## 🟢 La capa de habla gana su MODELO — y el pase descubre que casi publica la capa entera de nuevo (pase 100 del 2026-10-04)

### 🟢 El alta, con la familia leída del payload por el control compartido

| Repo | Familia (payload) | Bytes | Titular | Capa | Región |
|---|---|---|---|---|---|
| [`YuanGongND/gopt`](https://github.com/YuanGongND/gopt) | 🟢 **BSD-3-Clause** | 1.517 | `Copyright (c) 2022, Yuan Gong` | **modelo** de *pronunciation assessment* multi-aspecto y multi-granularidad | North America |

🔵 **Por qué completa la capa y no la repite.** Este archivo tenía, desde el pase 14:

| Pieza | Qué es | Qué le faltaba a la capa |
|---|---|---|
| `Halleck45/OpenPronounce` (MIT) | el **motor** listo para usar: fonema a fonema, PER/WER, DTW, prosodia, local | — |
| `kaldi-asr/kaldi` (Apache-2.0) | la **infraestructura** ASR genérica | — |
| `jimbozhang/speechocean762` (⚠️ sin licencia) | el **corpus** de referencia | 🔴 **el MODELO entrenable y comparable** |

🔵 **`gopt` es ese modelo, y trae su número:** `0,612` de PCC a nivel **fonema**, `0,549` a nivel
**palabra** y `0,742` a nivel **oración** sobre `speechocean762` — las tres, las mejores publicadas
sobre ese corpus. Trae **pesos preentrenados** y un notebook de Colab, y el `README` declara que
sus salidas intermedias de Kaldi están publicadas **para poder reproducir sin Kaldi**.

⚠️ **Límite declarado, y es del repo, no de la lectura:** el propio `README` anota que el tutorial
de inferencia sobre datos propios **tiene un bug reportado y abierto** (issue #15) que *«needs to be
addressed before use»*. **La cesión es BSD-3 y es limpia; el camino de inferencia sobre audio nuevo
no está liso.** Se cotiza como *modelo a integrar*, no como *servicio a desplegar*.

### 🔴 La corrección de alcance sobre el pase 14, y decide una cotización

El pase 14 cerró el hueco del corpus con una acción: *«pedir los términos a SpeechOcean por escrito
antes de cotizar»*. Este pase intentó resolverlo por el camino que esta base ya tenía probado —**el
REGISTRO**, con el que `P306` desempató `examplary/qti` leyendo npm— y **las dos distribuciones
canónicas están cerradas por egreso**:

| Canal | Código | Qué habría resuelto |
|---|---|---|
| `raw.githubusercontent.com/jimbozhang/speechocean762/HEAD/LICENSE` | 🔴 **404** en 6 nombres | la cesión en el repo |
| `openslr.org/101/` | 🔴 **000 `EGRESS_BLOCKED`** | los términos de la distribución canónica |
| `huggingface.co/api/datasets/mispeech/speechocean762` | 🔴 **000 `connect_rejected`** | el campo `license` de la tarjeta del dataset |

🔴 **El hueco pasa de «pendiente de una gestión» a «no verificable por ningún canal disponible», y
eso cambia la forma de la propuesta:** la cadena **técnica** es permisiva de punta a punta, y el
**benchmark** con el que se demuestra que funciona no lo es. 🔵 **La salida de ingeniería está a la
vista y es cotizable: `gopt` compara contra `speechocean762`, pero `OpenPronounce` NO necesita ese
corpus para OPERAR** — lo necesita para *comparar*. **Una entrega puede usar la cadena permisiva en
producción y dejar el corpus fuera del entregable**, con la medición hecha sobre datos del cliente.

### 🔵 La región, y de dónde sale cada placa (`P135`)

| Pieza | Región | Indicio, de primera mano |
|---|---|---|
| `YuanGongND/gopt` | **North America** | el `README` nombra la filiación de los autores: **MIT & PAII** |
| `jimbozhang/speechocean762` | **APAC** | el `README`: *«All the speakers are non-native, and their mother tongue is **Mandarin**»* |
| `Halleck45/OpenPronounce` | 🔸 **sin región** | el titular es un antropónimo con blog propio; **de un antropónimo no se infiere región** (`P135`) y no se eleva el indicio a dato |

### 🔴 `P311` — el control que esta base no tenía, y este archivo es el espécimen

Todos los controles de esta base auditan una afirmación que el pase **hace**: la familia de
licencia, el titular, el uso comercial, el vocabulario de región, la cita de una tendencia, la
propiedad de un manifiesto. 🔴 **La afirmación de que un alta es NUEVA es implícita, y lo implícito
no lo audita nada** — así que un pase 100 pases y ~250 slugs adentro puede republicar su propia
capa sin que nada objete.

🟢 El gate vive en `compose/code/p311-duplicate-alta-gate/` (**11/11**) y reporta **archivo, línea y
sección**, que es lo que vuelve la respuesta accionable: no *«ya está»* sino *«ya está, en la capa
de habla agregada en el pase 14»*. Tiene control negativo para **las dos** direcciones de error — el
falso `NEW`, que es el defecto, y el falso `ALREADY`, que **suprimiría** un alta real
(`AmirF194/canvas-mcp` y `BartMassey-upstream/canvas-mcp` son filas distintas y legítimas de esta
base, igual que `examplary/qti` y `instructure/qti`).

---

## 🟢 Altas fundacionales: 7 — y son DOS CAPAS, no siete piezas sueltas: el ALMACÉN xAPI y la librería de ÍTEMS QTI (pase 99 del 2026-10-04)

### 🔬 El canal, declarado antes de cualquier veredicto (`P247`)

| Canal | Código | Consecuencia |
|---|---|---|
| `github.com/<org>/<repo>` | 🔴 **403** | el `curl -sI` del encargo está **muerto acá** |
| `api.github.com/repos/<org>/<repo>` | 🔴 **403** | sin estrellas, sin licencia declarada, sin fecha de *commit* |
| `codeload.github.com` | 🔴 **403** | sin clon por tarball |
| `raw.githubusercontent.com/<slug>/HEAD/<path>` | 🟢 **200 con payload** | **el canal de primera mano**, y por él se midió todo lo de abajo |
| `registry.npmjs.org` | 🟢 **200** | segundo canal independiente, y este pase lo USÓ (`P306`) |
| `pypi.org` | 🟢 **200** | disponible, no necesario este pase |

🔴 **Ninguna fila nueva lleva estrellas, y es decisión y no olvido:** el canal que las sirve da
**403**, y una cifra leída del buscador puesta en una columna que el resto del archivo llena con
medición de primera mano es **dato falso con forma de dato bueno**.

### 🔴 El cero del barrido del encargo, con el denominador enumerado

`open source platform education ERP CRM MIT Apache` (año **calculado**, `date -u +%Y` → **2026**)
devolvió, por vigesimosexta vez, el eje generalista de ERP:

| Lo que devolvió | Veredicto |
|---|---|
| ERPNext / Frappe Education | 🔵 ya inventariado (y su `license.txt` de 19 B es el espécimen que originó la rama de DECLARACIÓN del control compartido) |
| OpenEduCat | 🔵 ya inventariado (LGPL-3.0) |
| Odoo, Apache OFBiz, Huly Platform | 🔴 ERP **genérico**, sin modelo de dominio educativo |
| `aureuserp/aureuserp` | 🟢 **MIT medida** — pero ERP **genérico**: va a `verticals/`, no a este estante |

### 🟢 Las 7 altas, con la familia leída del PAYLOAD y clasificada por el control compartido

| Repo | Familia (payload) | Bytes / `sha256` | Capa | Región |
|---|---|---|---|---|
| `pelotech/xapi-lrs` | 🟢 **Apache-2.0** | `LICENSE` 11.357 B · `c71d239df91726fc…` | 🟢 **ALTA DE CAPA: el ALMACÉN xAPI, conformante 1.0.3 **y** 2.0** — Hono + PostgreSQL, o **PGlite** embebido sin dependencias | 🔴 sin indicio |
| `KI-Campus/LRS` (`openLRS`) | 🟢 **MIT** | `LICENSE` 1.122 B · `d0ad2ec8573230da…` | LRS para H5P/LTI con **plugin Moodle** (`KI-Campus/LRS-Moodle`); Express + React | 🟢 **EMEA** |
| `adlnet/xapi-lab` | ⚠️ **MIT en `LICENSE`, Apache-2.0 en `README`** (`P305`) | `LICENSE` 1.082 B · `7625cb30bac8c76b…` | constructor y **validador** de *statements* xAPI, sobre `XAPIWrapper` | 🔴 sin indicio que resuelva |
| `instructure/qti` | 🟢 **MIT** | `LICENSE` 1.084 B · `e5edc6e4b0be1559…` | 🟢 **ALTA DE CAPA: importador QTI 1.2/2.1 del fabricante de Canvas** (gema Ruby) | 🔴 sin indicio |
| `examplary/qti` | 🟢 **MIT** (payload **+ npm**) | `LICENSE` 1.069 B · `38164d198cfe2ea7…` | 🟢 **generación QTI 3.0** tipada en TypeScript, con parseo y detección de versión | 🔴 sin indicio |
| `instructure/QTIMigrationTool` | 🟢 **BSD-3-Clause** — 🔴 **la medía `UNCLASSIFIED` hasta este pase** (`P304`) | `LICENSE.txt` 1.392 B · `26f8e53396b60ac4…` | migración QTI 1.x → 2.0 | 🟢 **EMEA** |
| `OpenOLAT/qtiworks` | 🟢 **BSD-3-Clause** (*«3-clause BSD»* textual en el payload) | `LICENSE.txt` 2.058 B · `a5c692f120907d58…` | motor de **ENTREGA** QTI 2.1 + `JQTI+` (librería Java) + extensiones **MathAssess** | 🟢 **EMEA** |

🔵 **Por qué valen más que su cuenta.** Esta base ya tenía `DavidLMS/learnmcp-xapi` —el lado
**agente** del xAPI— y no tenía dónde **guardar** los *statements*; y tenía `amp-up-io/qti3-item-player`
y `pie-framework/pie-qti` —**reproductores**— y no tenía con qué **generar** ni **migrar** los ítems.
⚠️ **Un eje con filas no es un eje cubierto: la pregunta que rinde no es «¿barrí este tema?» sino
«¿de qué LADO de este tema tengo filas?».**

🟢 **Y las tres de QTI se componen entre sí, que es lo que las hace una capa:** `examplary/qti`
**genera** QTI 3.0, `instructure/QTIMigrationTool` **migra** lo heredado de 1.x, `instructure/qti`
**importa** a Canvas y `OpenOLAT/qtiworks` lo **entrega y puntúa**. **Las cuatro son permisivas**
(3 MIT + 2 BSD-3-Clause), que es raro en esta vertical: la mitad de este estante es GPL/AGPL.

### 🔴 Los 6 descartes, enumerados — y el más caro es de la capa SIS

| Candidata | Veredicto medido | Canal |
|---|---|---|
| `chatt-state/banner-mcp-server` | 🔴 **SIN CESIÓN** — alcanzable por `package.json`, **0 de 14 nombres** de archivo de licencia | `raw` |
| `tunapanda/wp-xapi-lrs` | 🔴 SIN CESIÓN (alcanzable por `README.md`) | `raw` |
| `dmccreary/learning-record-store` | 🔴 SIN CESIÓN (alcanzable por `README.md`) | `raw` |
| `api-evangelist/powerschool` | 🔴 SIN CESIÓN — y es un **perfil de API**, no software | `raw` |
| `pawalshriram06-ops/mcp-student-management-system` | 🔴 SIN CESIÓN | `raw` |
| `mihir-webmavens/student-management-system` | 🔴 SIN CESIÓN — su `README` dice *«learning mcp server»* | `raw` |

🔴 **`chatt-state/banner-mcp-server` es el descarte que decide un presupuesto.** Es el **único** MCP
sobre **Ellucian Banner** que el barrido encontró, Banner es uno de los SIS de educación superior
más instalados del mundo, el repo está **vivo y alcanzable**, y **no cede nada**. 🔵 **Consecuencia
para una pre-venta de educación superior: la capa MCP sobre el SIS no tiene punto de partida
construible y se presupuesta como desarrollo propio** — al contrario de K-12, donde
`443pablo/mcp-powerschool` sí está en esta base. ⚠️ **Y `ishandutta2007/Awesome-University-Management`
es MIT medida (1.069 B) y tampoco es fila: es un ÍNDICE, no un sistema.** Entra al denominador.

### 🔴 `P304` — el ancla BSD era una FRASE CONTIGUA, y perdía una familia PERMISIVA

El payload de `instructure/QTIMigrationTool` dice:

> *«Redistribution and use **of this software** in source and binary forms **(where applicable)**,
> with or without modification, are permitted provided that the following conditions are met»*

🔴 **Dos inserciones dentro de la misma oración** —un complemento y un parentético— **y el `grep` de
frase fija no matchea.** Veredicto: `UNCLASSIFIED` sobre un BSD-3-Clause de libro, con sus tres
cláusulas y su *«Neither the name of the University of Cambridge…»*.

🔵 **Es el CUARTO eje del mismo defecto, y la serie es la lección:**

| Patrón | Eje del defecto | Qué se midió mal |
|---|---|---|
| `P171` | cuerpo **vs** título | la sección 13 de la GPL-3.0 nombra la AGPL |
| `P288` | **caja** | un AGPL *reflowed* sin título en mayúsculas caía a la rama GPL |
| `P299` | palabra **vs** subcadena | `mit` es subcadena de `permit`, `submit`, `limit` |
| 🟢 `P304` | **frase contigua vs tokens ordenados** | una inserción dentro de la oración de concesión |

⚠️ **La dirección es la CONTRARIA a la de `P299`, y por eso casi no se arregla:** `P299` convertía
una negativa en un permiso MIT —falla de **cumplimiento**—, mientras `P304` **pierde** una fila
permisiva —falla de **estante**—. 🔴 **Lo que obliga el arreglo es el segundo efecto: con la familia
en `UNCLASSIFIED`, la compuerta de `P250` NO corta, así que el veredicto de uso comercial de un
payload PERMISIVO lo producía el token-match sobre el CUERPO — justo la vía que `P171` declara
insegura. La respuesta era `allowed`, que es la correcta, obtenida por la vía equivocada.**

| Eje | Antes de `P304` | Después |
|---|---|---|
| familia | 🔴 `UNCLASSIFIED` | 🟢 `BSD` |
| uso comercial | ⚠️ `allowed` **por token-match sobre el cuerpo** | 🟢 `allowed` **por la compuerta** |
| titular | ⚠️ acertado por la rama `UNCLASSIFIED` | 🟢 por la rama BSD, que lo carga por construcción |

🔴 **Y por qué 50/50 pasaba con el defecto puesto, que es `P126` punto 2 otra vez:** la fixture BSD
de la suite era la oración **CANÓNICA**, o sea **el único caso donde el ancla de frase no puede
fallar**. **Una fixture canónica valida la rama feliz y certifica un clasificador roto.**

🟢 **`lib/license_family.sh` — 50/50 → 62/62**, con **tres controles negativos** que es lo que
`P126` exige: (1) el hueco **no cruza una oración** (`[^.]`), (2) la **cota de 40 caracteres** se
declara y se afirma como límite conocido, (3) la relajación **no se come** a GPL-3.0, Apache-2.0,
MIT, ISC ni 0BSD.

⚠️ **`p230-rostering-layer-axis/measure.sh` cambió de FORMA, no sólo de ancla:** la rama BSD **salió
del `case`**, porque un glob no puede expresar un hueco acotado con clase negada — y el glob de dos
estrellas que sí lo "resuelve" es **ilimitado y cruza oraciones**, justo lo que el control negativo
1 prohíbe.

🔴 **`P237` queda ABIERTO y declarado para cuatro instrumentos.** `p170`, `p206`, `p211` y `p230`
llevan **copia propia** del ancla y ninguno hace `source` del control compartido. Este pase parchó
las cuatro **para no dejar instrumentos rotos a sabiendas**, pero **parchar cuatro copias ES el
antipatrón que `P237` existe para nombrar.** El rewiring queda pre-registrado **con su bloqueo
dicho: el control compartido todavía no es superconjunto de las copias** —`p170` clasifica `BUSL`,
`Elastic` y `PolyForm`, que el control no tiene—, **y adoptarlo sin eso PERDERÍA familias**, que es
la advertencia que `lib/README.md` ya traía escrita desde el pase 77.

### 🔴 `P305` — dos payloads del MISMO repo declaran familias, titulares y años distintos

| Fuente en `adlnet/xapi-lab` | Familia | Titular | Año |
|---|---|---|---|
| `LICENSE` (1.082 B) | 🟢 **MIT** | `Tyler Mulligan` — **persona física** | 2015 |
| `README.md`, sección *License* | ⚠️ **Apache-2.0** | `Advanced Distributed Learning` — **organización** | 2016 |

🔵 **Las dos son permisivas, así que el riesgo comercial es bajo — y no es ahí donde duele.**
🔴 **Difiere el TITULAR, y la obligación de atribución corre hacia una parte distinta según cuál
gobierne:** una persona bajo MIT, o la **ADL Initiative** (iniciativa del Departamento de Defensa de
EE. UU.) bajo Apache-2.0. **Un aviso de atribución en un entregable nombra a uno y se equivoca con
el otro.** ⚠️ **Esta base NO resuelve el conflicto —la pregunta es legal, no de medición— y la fila
lo lleva declarado en vez de elegir en silencio.** 🔵 **El eje es nuevo acá: `P184` y `P280` miden
licencia-vs-**manifiesto**; este es archivo-de-licencia-vs-**README**.**

### 🟢 `P306` — identidad por REGISTRO, que es lo que al `sha256` le faltaba

`examplary/qti` y `examplary-ai/qti`, byte-idénticos en los **tres** archivos probados
(`README.md` `e04864bfc0706da0…`, `LICENSE` `38164d198cfe2ea7…`, `package.json` `e30cc496a3bfaa57…`).

🔴 **El `sha256` dice «son el mismo artefacto» y NO dice cuál es el canónico.** El pase 98 quedó
exactamente ahí con `iriseye395`/`itsnone-liu`/`zijinz456`: el canónico se eligió porque **ya estaba
en la tabla**, no porque un canal lo afirmara. 🟢 **El registro contesta eso:**
`registry.npmjs.org/@examplary/qti` (🟢 `200`) declara `repository.url` =
`git+https://github.com/examplary/qti.git` y `license` = `MIT`. **Canónico `examplary/qti`, espejo
`examplary-ai/qti`, y la familia confirmada por DOS canales independientes que concuerdan.**

⚠️ **Cota declarada: sirve sólo para piezas PUBLICADAS en un registro.** De las 9 licenciadas de
este pase **una** tenía paquete en npm, y `pelotech/xapi-lrs` trae `package.json` **sin campo
`license`** — su cesión vive sólo en el `LICENSE` y el registro no la respalda.

### 🟢 Regiones: dos ganadas por indicio de primera mano, y cuatro huecos declarados

| Repo | Región | Indicio, y es del PAYLOAD |
|---|---|---|
| `instructure/QTIMigrationTool` | 🟢 **EMEA** | `README` fija `qtitools.caret.cam.ac.uk` y el contacto `swl10@cam.ac.uk`; el `LICENSE.txt` nombra la **University of Cambridge** |
| `OpenOLAT/qtiworks` | 🟢 **EMEA** | `README` fija `webapps.ph.ed.ac.uk/qtiworks/` — **University of Edinburgh** |
| `KI-Campus/LRS` | 🟢 **EMEA** | 🔵 **clase de indicio NUEVA: la FORMA JURÍDICA.** Titular *«Hasso Plattner Institute for Digital Engineering **gGmbH**»*, y `gGmbH` es una figura del derecho societario **alemán** |
| `pelotech/xapi-lrs` | 🔴 **ninguna** | sólo el nombre del titular |
| `adlnet/xapi-lab` | 🔴 **ninguna** | los dos indicios son nombres de titular **y además se contradicen** (`P305`) |
| `instructure/qti` · `examplary/qti` | 🔴 **ninguna** | sólo nombres de titular |

🔵 **`gGmbH` merece el subrayado porque amplía `P135` sin romperlo:** `P135` prohíbe inferir región
del **nombre** del titular, y una **forma de constitución** no es el nombre — es la jurisdicción
bajo la cual la entidad existe. 🔴 **Y los cuatro huecos se dicen en vez de rellenarse: elevar
«North America» desde «Instructure es de Utah» sería inventar dato con forma de dato medido.**

### 🟢 Suites y canales

- `lib/test_license_family.sh` — 🟢 **62/62** (era **50/50**; 12 aserciones nuevas, 3 negativas).
- Barrido total — 🟢 **51 suites pasan, 0 fallan**, con su invocación, que es la regla de `P107`:
  `find compose/code -name 'test_*.py' -o -name 'test_*.sh' -o -name 'run_test.sh'`.
- `p170-headref-license-sweep/sweep_headref.sh instructure/QTIMigrationTool` → 🟢 `LICENSED LICENSE.txt 1393 BSD` (era `UNKNOWN`).
- Canal: todo por `raw.githubusercontent.com` + `registry.npmjs.org`; `github.com`, `api.github.com`
  y `codeload.github.com` → **403**.


## 🔴 Altas fundacionales: 0 — pero las SIETE plataformas de esta capa quedan re-medidas por payload, y NINGUNA es permisiva (pase 98 del 2026-10-04)

🔬 **Canal (`P247`):** `github.com/<org>/<repo>` y `api.github.com` → 🔴 **403**;
`raw.githubusercontent.com` → 🟢 **200 con payload**. Todo lo de abajo se leyó por `raw`.

### 🔴 El cero, con el denominador enumerado

El barrido `open source platform education LMS SIS MIT Apache` devolvió **7 plataformas
nombradas** —Moodle, Open edX, Canvas LMS, ILIAS, Sakai, Chamilo, OpenEduCat— y 🔴 **las 7 ya
estaban en esta base.** No hay alta fundacional porque **no había nada nuevo que dar de alta**, no
porque no se buscara.

### 🟢 El aporte del pase: las 7 licencias, medidas en el PAYLOAD de una sola barrida

| Plataforma | Repo | Licencia **leída del payload** | Bytes | Ruta que la tenía |
|---|---|---|---|---|
| Moodle | `moodle/moodle` | **GPL-3.0** (`affero_lines=3` → **no** es AGPL, `P171` discriminando bien) | 35.147 | 🔵 **`main/COPYING.txt`** |
| Open edX | `openedx/edx-platform` | 🔴 **AGPL-3.0** (`affero_lines=15`, `sha256:106a1b4b8b71324a…`) | 35.135 | `master/LICENSE` |
| Canvas LMS | `instructure/canvas-lms` | 🔴 **AGPL-3.0** | 34.520 | `master/LICENSE` |
| Chamilo | `chamilo/chamilo-lms` | **GPL-3.0** | 35.147 | `master/LICENSE` |
| ILIAS | `ILIAS-eLearning/ILIAS` | **GPL-3.0** | 35.147 | `master/LICENSE` |
| Sakai | `sakaiproject/sakai` | 🟢 **ECL-2.0** | 11.120 | `master/LICENSE` |
| OpenEduCat | `openeducat/openeducat_erp` | **LGPL** | 8.241 | `master/LICENSE` |

🔴 **El resultado que manda para una venta: CERO de las siete es MIT/Apache/BSD.** 🟢 **La única
permisiva es Sakai, por ECL-2.0** —la *Educational Community License*, derivada de Apache-2.0 y
aprobada por la OSI—, y eso la vuelve **la única de las siete sobre la que se puede construir un
entregable cerrado sin pedir permiso.**

⚠️ **Y las DOS de copyleft de red son justo las dos de despliegue público grande:** Open edX y
Canvas son **AGPL-3.0**, cuya sección 13 alcanza al uso **por red** — o sea que un SaaS montado
encima **dispara la obligación de fuente**. 🔵 **Es el hecho de licencia más caro de toda esta capa
y es el que hay que decir en la primera reunión, no en la due diligence.**

### 🔴 El canal de búsqueda afirmó Apache-2.0 sobre Open edX, y esta base ya lo tenía bien

El barrido de hoy devolvió textualmente *«Open edX uses the Apache License 2.0»*. 🔴 **Falso, y en
la dirección CARA:** el payload de `openedx/edx-platform` es el título **`GNU AFFERO GENERAL PUBLIC
LICENSE Version 3`** con **15 líneas nombrando la AGPL** (un cuerpo GPL-3.0 la nombra en 3 — el
discriminador de `P171`).

🟢 **Y el valor del pase está acá: esta base YA registraba `AGPL-3.0 ⚠️` para ese repo, así que la
disciplina de payload-primero la defendió de una afirmación externa equivocada sin que nadie
tuviera que acordarse de nada.** 🔵 **La confusión del canal tiene explicación y conviene anotarla:
hay COMPONENTES de Open edX que sí son Apache-2.0 —`openedx/XBlock`, que el pase 95 confirmó por
payload, y `Aspects`— así que «Open edX es Apache-2.0» es un component-vs-plataforma mal
generalizado.** La pregunta correcta no es «¿qué licencia tiene Open edX?» sino **«¿qué licencia
tiene el artefacto que voy a desplegar?»**.

### ⚠️ Nota de instrumento, para el próximo barrido que se escriba

🔴 **Un sondeo que pruebe sólo `LICENSE` devuelve «sin licencia» para `moodle/moodle`** —el LMS más
desplegado del mundo— **porque su texto vive en `COPYING.txt`.** El primer sondeo de este pase cayó
justo ahí. 🔵 **No se eleva a defecto de esta base: los instrumentos del árbol ya prueban `COPYING`
y `COPYING.txt` entre los nombres.** Queda como cautela para instrumentos NUEVOS, que es donde esta
base viene fallando sus primeras pruebas honestas.

### 🟢 Suites

- `lib/test_license_family.sh` — 🟢 **50/50** (era 41/41; `P299`, ver `agents/top.md`).
- Barrido total del árbol — 🟢 **50 suites pasan, 0 fallan.**

## 🟢 El hueco que el pase 94 dejó abierto sobre este archivo queda CERRADO: `openedx/XBlock`, confirmado por payload (pase 95 del 2026-10-04)

El pase 94 descubrió que la fila de **`openedx/XBlock`** —publicada aquí como **Apache-2.0**— era
**correcta** pero que **el barrido no la podía confirmar**: 11 variantes de nombre × 3 ramas = **33
sondas, 0 hits**, con testigo de alcance en `200`. La diferencia era la **CAJA de la extensión**: se
probaba `LICENSE.txt`, el archivo es `LICENSE.TXT`.

🟢 **Hoy se LEE, y no por adivinar un nombre más sino por tomarlo del manifiesto:**

| Sonda | Resultado |
|---|---|
| `master/pyproject.toml` → `license-files` | 🟢 **`["LICENSE.TXT"]`** (y `license = "Apache-2.0"`) |
| `master/LICENSE.TXT` (el nombre NOMBRADO, con su caja) | 🟢 **`200`**, abre con `Apache License` |
| propiedad del manifiesto (`P280`): `name = "XBlock"` vs repo `openedx/XBlock` | 🟢 **`OWN`** → atribuible |
| sondas necesarias | **10** (contra 33 que no alcanzaban) |

🔵 **La fila no cambia: cambia su EVIDENCIA.** Pasa de *«correcta según el badge»* a *«correcta según
el payload»*, que es la diferencia que `P114` le costó a esta base aprender.

### 🔵 Y queda medido que `P279` es real pero RARO

El pase 94 pre-registró que si el hueco de caja se repartía como en su control positivo (1 de 7),
**~28 de 200** filas tendrían un veredicto de licencia que es un hueco y no un dato. Medido sobre las
200 filas de agentes: 🔴 **0**.

| | valor |
|---|---|
| huecos de `P279` en las 200 filas de agentes | 🔴 **0** |
| casos de `P279` conocidos en TODA la base | **1** (`openedx/XBlock`, de este archivo) |
| tasa real | **1 de 201** |

🔴 **`P286`**: *extrapolar un reparto poblacional desde UN control positivo no es una estimación, es
una corazonada con tabla.* 🟢 **Y el dato útil para este archivo es el contrario del alarmante:** el
único `P279` conocido vive **acá**, en la capa de **plataforma/empaquetado** —repos con manifiesto de
distribución y ramas `master` viejas—, no en la capa de agentes.

### 🟢 Cuatro filas de este archivo ganan familia de licencia LEÍDA DEL PAYLOAD

Por reusar el classificador compartido `lib/license_family.sh` (`P237`), que classifica por **bloque
de título** y no por el cuerpo (`P171`):

| Repo | Antes | Hoy | Payload | Qué cambia para Globant |
|---|---|---|---|---|
| [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | `UNKNOWN` | **Apache-2.0** | `COPYING` | 🟢 permisiva: utilizable como base de ASR |
| [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | `UNKNOWN` | 🟢 **0BSD** | `LICENSE` | 🟢 la **más permisiva** del inventario de *rostering*: ni atribución |
| [`nmarafo/OpenDidactia`](https://github.com/nmarafo/OpenDidactia) | `UNKNOWN` | ⚠️ **CC-BY-SA-4.0** | `LICENSE.md` | ⚠️ *share-alike* **sobre el contenido**: el material derivado hereda |
| [`dssg/student-early-warning`](https://github.com/dssg/student-early-warning) | `UNKNOWN` | **UNCLASSIFIED** | `LICENSE` | 🔴 licencia académica **NO comercial** (U. de Chicago): **fuera** de lo construible |

🟢 **`UNCLASSIFIED` es el classificador portándose BIEN**, no fallando: negarse a asignar familia OSI a
una licencia académica no comercial es el comportamiento correcto, y la fila ya estaba marcada como no
open source.

⚠️ **Límite declarado, sobre `kaldi`:** el veredicto **Apache-2.0 es correcto** —el `COPYING` concede
Apache 2.0 en su línea 51 y repite el *grant* estándar en la 145— **pero la evidencia que lo disparó es
PROSA del bloque de título**: el `COPYING` de Kaldi es un *legal notice* de 364 líneas, no el texto de
la licencia. **Es un acierto por una vía débil**, y esta fila ya estaba marcada como *texto anómalo*
desde el pase 36.

### 🔴 Acción pre-registrada para el pase 96, con su razón

Correr `compose/code/p283-manifest-named-license/sweep_named.sh` sobre las filas `org/repo` de **este
archivo** y de **`verticals/solutions.md`** que **no** están en las 200 ya barridas. 🔵 **La razón, y es
falsable:** el único `P279` conocido vive acá, en la capa de plataforma, así que **es el único sitio
donde la tasa de 1 de 201 puede subir**. Si sube, `P279` es un patrón **de los repos de plataforma**;
si no sube, es un **caso único** y hay que decirlo así en vez de seguir tratándolo como una clase.

## 🔴 Sin altas fundacionales — y una fila de este archivo revela que el barrido de licencia tiene un hueco de NOMBRE

### 🔬 Canal declarado primero (`P247`)

`curl -sI` sobre `github.com/` → 🔴 **`403` en 3/3** (reproduce el pase 81, 81/81). 🟢 Lo que
rinde es `raw.githubusercontent.com`, que **entrega el payload**: la licencia se LEE.

### 🔴 El denominador del cero

[`kouweizhu/agents-radar` #328](https://github.com/kouweizhu/agents-radar/issues/328),
fechado **2026-10-04**: **47 repos, 0 de la industria educativa**; las 2 etiquetadas
`[EDUCATION]` son curriculos de AI para ingenieros y **las 2 ya estan en este archivo**
(`rasbt/LLMs-from-scratch`, `rohitg00/ai-engineering-from-scratch`). Ver **`P281`**.

### 🔴 `P279` — `openedx/XBlock` es Apache-2.0, la fila es correcta, y el barrido no lo podia probar

| Sonda | Resultado |
|---|---|
| 11 variantes de nombre × 3 ramas = **33 sondas** | 🔴 **0 hits** |
| testigo de alcance: `master/README.rst` | 🟢 `200` — se alcanzaba |
| `master/LICENSE.TXT` | 🟢 `200`, abre con `Apache License` |
| `master/pyproject.toml` | 🟢 `license = "Apache-2.0"` · `license-files = ["LICENSE.TXT"]` |

Se probo `LICENSE.txt`; el archivo es **`LICENSE.TXT`**. **El canal distingue mayusculas,
tambien en la extension.**

**P279**: *una lista fija de nombres de archivo de licencia siempre tiene un hueco, porque el
espacio de nombres es libre y el canal es sensible a la caja. El nombre autoritativo esta en
el manifiesto del paquete (`license-files`): hay que LEERLO de ahi y sondear ESE nombre.*
🔵 Y la ref importa: la rama por defecto de XBlock es **`master`**, no `main` —caso de
**`P278`** en el eje del nombre del payload.

### 🔴 Cuanto de este archivo puede estar afectado, y la accion queda pre-registrada

Control positivo del instrumento: **7** repos de licencia conocida, **6 hallados** en la
primera pasada, **1 (`XBlock`) solo por manifiesto**.

🔴 **Si ese reparto (1 de 7) se mantiene, de las ~200 filas `org/repo` que los pases 62/64
barrieron con el instrumento viejo hay ~28 cuyo veredicto de licencia es un hueco de nombre y
no un dato.** Es la accion de mayor valor pendiente de esta base y se **pre-registra como
accion 1 del pase 95** para que no se pueda eludir:
`sh compose/code/p280-manifest-ownership/sweep.sh <org/repo>`.

### 🟢 Lo que si quedo cerrado: las 8 filas `SIN LICENCIA`, 8/8

264 sondas (33 por fila), 6 manifiestos por fila, y **testigo de alcance antes del veredicto**
—porque sin alcance la «ausencia» mide el canal, no el repo: 🟢 **8/8 alcanzadas, 8/8 AUSENCIA
CONFIRMADA**. Enumeradas en `compose/code/p280-manifest-ownership/README.md`.

🔴 **La unica de las 8 que devolvio licencia de manifiesto la devolvio AJENA** (**`P280`**):
`alfredang/ai-mms` aloja en su raiz el `composer.json` de `openmage/magento-lts`
(`["OSL-3.0","AFL-3.0"]`), sin modificar. Y la medicion del arbol (`app/Mage.php` → `200`;
upstream con `LICENSE.txt` **y** `LICENSE_AFL.txt`) muestra que **hereda OSL-3.0**: copyleft
fuerte con gatillo de **despliegue externo**. 🔵 **Para esta capa: una base que parte de un
repo DERIVADO hereda la cesion del upstream, no la del repo —y hay que medirlo antes de
elegirlo como fundacion.** Suite: `python3 test_license_probe.py` → 🟢 **37/37**.


## 🧾 Altas fundacionales: 0 — SEXTO pase consecutivo, y el estante gana el instrumento que le faltaba para sostener una AUSENCIA (pase 93 del 2026-10-04)

### 🔴 El barrido, declarado

🔴 **Cero altas.** El barrido fundacional obligatorio
(`open source platform education ERP CRM MIT Apache`, año **CALCULADO**: 2026) devolvió por
**decimonovena** vez el catálogo que este estante ya tiene verificado repo por repo: `OpenEduCat`
(**LGPL-3.0**), `ERPNext` / `frappe/education` (**GPL-3.0**), Moodle, Open edX, Chamilo, ILIAS,
`openSIS`. Es una medición de la **cobertura** de este estante, no un hallazgo.

⚠️ **Y nombró una vez más la *Kuali Foundation* descrita en PRESENTE** (*«consorcio de más de dos
docenas de universidades»*). Este estante la midió en el **pase 42** y el veredicto no cambió:
`kuali/rice` y `KualiCo/rice` (**ECL-2.0**), `kuali/kc` y `kuali/kfs` (**AGPL-3.0**), los cuatro
**sin commits desde hace 6–9 años**; `KualiCo/kc`, `KualiCo/kfs` y `KualiCo/kuali-student` **no
existen**. 🔵 **Haberla medido una vez es lo que impide ofrecerla hoy como opción viva.**

### 🟢 Lo que sí cambia para quien va a partir de una de estas piezas: la ausencia pasa a ser MEDIBLE

El pase 85 retiró un instrumento de este estante (sobre un árbol copyleft el `sha256` del `LICENSE`
no identifica nada) y el pase 92 retiró otra clase de negativo con **`P274`** (en el canal `raw` un
path de **directorio** da 404 **siempre**, exista o no) **sin dejar reemplazo**. Desde entonces este
estante no podía sostener *«esta pieza no trae X»* más que con el tramo declarado.

🟢 **Reemplazo, y es de este pase (`P275`):**

```sh
git clone --filter=blob:none --no-checkout --depth 1 -b "$REF" "https://github.com/$REPO" "$DIR"
git -C "$DIR" ls-tree -d --name-only -r HEAD
```

Baja commit y árboles **sin ningún blob** y enumera el árbol **completo**: sin truncar, sin paginar y
**sin `api.github.com`**, que este árbol registra en **403** desde el pase 89. Medido: el clon de
ILIAS tarda **< 1 s**; sobre Moodle enumera **10.923** directorios de una vez.

🔵 **Para este estante eso cambia una clase de pregunta entera.** *«¿Esta pieza trae su propia capa de
AI o hay que ponerla?»* dejó de contestarse con un sondeo de nombres —que mide la lista sondeada— y
se contesta enumerando. Las tres filas de ERP/SIS de este estante quedan re-medidas sobre el árbol
completo:

| pieza | ref | layout resuelto | módulos | árbol (dirs) | ¿capa de AI en el núcleo? |
|---|---|---|---|---|---|
| `frappe/erpnext` | `develop` | `erpnext` | 39 | 1.427 | 🟢 **no** — ausencia CERRADA |
| `frappe/education` | `develop` | `education` | 11 | 159 | 🟢 **no** — ausencia CERRADA |
| `openeducat/openeducat_erp` | `18.0` | **raíz del repo** | 15 | 173 | 🟢 **no** — ausencia CERRADA |
| `ILIAS-eLearning/ILIAS` | `release_11` | `components/ILIAS` | 180 | 4.266 | 🟢 **no** — ausencia CERRADA |

🟢 **Pasan de *sostenidas por manifiesto + árbol truncable* a *sostenidas por árbol COMPLETO*.** Para
un *engagement* eso significa que la capa agéntica sobre estas cuatro piezas es **desarrollo
completo**, no integración con algo que ya viene — y ahora es una afirmación medida y no una
inferencia.

### 🔴 `P278` — la ruta que contiene los módulos es propiedad de la (repo, ref), y este estante iba a tropezar con eso

🔴 **`components/ILIAS/` da 180 directorios en `release_11` y CERO en `release_9`**, donde el mismo
árbol los tiene en `Modules/` (54) + `Services/` (126) = **180**: el layout se movió en la 10.
Publicar ese cero sería *«ILIAS 9 no tiene componentes»*, que es dato incorrecto.

🔵 Es `P270` subido una capa: de negativos sobre un **nombre** a negativos sobre un **layout**. Por
eso el barrido de este estante se escribe como **compuerta** —recibe las rutas candidatas, elige la
poblada en esa ref, y devuelve `NO-CLAIM` si ninguna lo está— y no como contador.
⚠️ **Y es una advertencia para las piezas de este estante que esta base fechó en ramas antiguas:**
cualquier conteo de módulos tomado de una ruta fija tiene **fecha de vencimiento** cuando el proyecto
reorganiza su árbol.

### ⚠️ Lo que este pase NO midió de estas filas, declarado

- ⚠️ **Mide el árbol PUBLICADO en esa ref.** Nada dice de **plugins de terceros**, que es exactamente
  donde vive la capacidad de AI de ILIAS (*AI Chat plugin*, *ILIAS Assistant*) y la del ecosistema
  Frappe (`noviz_ai`, `nextai`, `ChatNext`, apps de marketplace).
- ⚠️ **`--depth 1` mide una ref por clon.** El costo crece con el número de refs, no con el tamaño del
  repo; ninguna de estas cuatro filas está medida en todas sus ramas de soporte.
- 🔴 **Licencias sin cambio y sin permisiva nueva:** la capa de plataforma de esta vertical sigue
  **copyleft 8 de 8** (tendencia **701**, cuarto pase sostenida). El foco MIT/Apache/BSD del encargo
  se cumple en la capa de agente; acá la restricción es de **entrega**, no de selección.

Instrumento, datos crudos y controles:
[`compose/code/p275-tree-enumeration/`](../compose/code/p275-tree-enumeration/).

## 🟢 7 altas fundacionales de un golpe, y es una CAPA entera que este estante no tenía: la psicometría computacional del aprendizaje, de un laboratorio con nombre y dirección (pase 87 del 2026-10-04)

### 🔴 El hueco que este estante tenía, y era el más caro de todos

Este estante sabía inventariar **plataformas** (LMS, SIS, ERP educativo), **conectores** (*rostering*, xAPI,
OneRoster, Ed-Fi) y **servidores MCP**. Lo que no tenía —en 86 pases— era la capa que está **debajo de
cualquier promesa de «aprendizaje personalizado»**:

- **¿Cómo se estima qué sabe un alumno?** → *knowledge tracing*
- **¿Cómo se diagnostica en qué concepto falla?** → *cognitive diagnosis* (IRT, MIRT, DINA)
- **¿Cómo se elige el próximo ítem para medir con menos preguntas?** → *computerized adaptive testing*
- **¿Con qué datos se entrena y evalúa todo eso?** → datasets educativos normalizados

Sin esa capa, «tutor adaptativo» es una promesa de prosa. **Ningún LMS de este árbol la trae**: Moodle,
Canvas, Open edX y OpenEduCat gestionan cursos, no estiman rasgos latentes. Este pase la pone, y la pone
completa, de **un solo origen institucional**.

### 🟢 La procedencia, medida de primera mano (y es lo que cierra el hueco de APAC)

`P135` de esta base prohíbe inferir región de un antropónimo, y este pase **no la infiere**. La declara con
**tres lecturas de primera mano de la propia organización**:

| Señal | Valor leído |
|---|---|
| Nombre del `org` | **BigData Lab @USTC** · `中科大大数据实验室` |
| Bio del `org` | `中国科学技术大学大数据实验室` — Laboratorio de Big Data de la **Universidad de Ciencia y Tecnología de China** |
| Sitio declarado | `http://bigdata.ustc.edu.cn/index.html` |
| Ubicación declarada | **`Hefei 合肥`** (Anhui, China) |
| Tamaño | 73 repositorios públicos · 354 seguidores |

⇒ **Región: APAC**, declarada desde la institución y su dominio `.ustc.edu.cn`, **no desde un nombre propio**
(**P261**). Es el **decimoquinto** pase que este árbol declaraba «APAC sin código educativo propio en el
inventario». **Cierra.**

### 🟢 Las 8 filas, con licencia leída del PAYLOAD y release leída de la API de PyPI

| Repo | Licencia (payload) | Titular (payload, verbatim) | ★ / forks | PyPI | Última release | Veredicto |
|---|---|---|---|---|---|---|
| [`bigdata-ustc/EduData`](https://github.com/bigdata-ustc/EduData) | 🟢 **Apache-2.0** | `Copyright [2020] [bigdata-ustc]` | 310 ★ / *no medido* | 🟢 `EduData` 0.0.18 (18 versiones) | 🔴 **2021-08-20** | 🟢 Permisivo · 🔴 estante viejo. Datasets educativos + interfaz de descarga y preproceso. **Es la puerta de entrada del resto.** |
| [`bigdata-ustc/EduKTM`](https://github.com/bigdata-ustc/EduKTM) | 🟢 **Apache-2.0** | 🔴 *sin línea de titular en el árbol leído* | 265 ★ / 70 forks | 🟢 `EduKTM` 0.0.10 (10 versiones) | 🔴 **2022-05-18** | 🟢 *Model Zoo* de **trazado de conocimiento**. Cita «A Survey of Knowledge Tracing» (Liu et al., 2021, `arXiv:2105.15106`). |
| [`bigdata-ustc/EduCDM`](https://github.com/bigdata-ustc/EduCDM) | 🟢 **Apache-2.0** | `Copyright [2020] [bigdata-ustc]` | 197 ★ / *no medido* | 🟢 `EduCDM` 1.0.1 (13 versiones) | 🟢 **2024-10-25** | 🟢🟢 **La más vigente del conjunto y la única con release de 2024 en serie larga.** *Model Zoo* de **diagnóstico cognitivo**: IRT, MIRT, DINA y variantes neuronales. |
| [`bigdata-ustc/EduCAT`](https://github.com/bigdata-ustc/EduCAT) | 🟢 **MIT** | ⚠️ `Copyright (c) 2019 tswsxk` — **INDIVIDUO, no la institución** | 76 ★ / 32 forks | 🟢 `EduCAT` 0.0.1 (**1 sola versión**) | 2024-01-24 | 🟢 **Testing adaptativo computarizado** (CAT). Cita «Survey of Computerized Adaptive Testing» (`arXiv:2404.00712`). ⚠️ Una sola release publicada. |
| [`bigdata-ustc/EduNLP`](https://github.com/bigdata-ustc/EduNLP) | 🟢 **Apache-2.0** | README se declara *«commercial open-source software, released under the Apache-2.0 license»* | 64 ★ / 20 forks | 🟢 `EduNLP` 0.0.9 (9 versiones) | 🔴 **2022-11-14** | 🟢 NLP sobre **ítems educativos multimodales** (enunciados con fórmula, figura y texto). `pip install EduNLP[full]`. |
| [`bigdata-ustc/EduSim`](https://github.com/bigdata-ustc/EduSim) | 🟢 **MIT** | ⚠️ **fork de `tswsxk/EduSim`** — el árbol upstream es de un individuo | 29 ★ / 13 forks | 🟢 `EduSim` 0.0.2 (2 versiones) | 🔴 **2019-11-29** | ⚠️ Simulador de entornos para **recomendadores educativos**, con interacción secuencial con el alumno. **Release de 2019: se usa como referencia, no como dependencia.** |
| [`bigdata-ustc/EduRec`](https://github.com/bigdata-ustc/EduRec) | 🟢 **MIT** | 🔴 *no medido* | 4 ★ / 2 forks | 🔴 **NO publicado** (`404` calibrado) | — | ⚠️ Recomendación educativa. Tiene estructura real (`setup.py`, `pytest.ini`, `Makefile`, `examples/`), pero **4 ★ y sin paquete**: es semilla. |
| [`bigdata-ustc/EduX`](https://github.com/bigdata-ustc/EduX) | 🔴 **SIN LICENCIA** | — | 11 ★ / 5 forks | 🔴 **NO publicado** (`404` calibrado) | — | 🔴 **AFUERA.** Es el **paraguas** que indexa a los demás y es justamente el único sin cesión. Se cita como mapa, **no se construye encima**. |

**Recuento, para que no haya que contarlo:** **8 repos medidos · 7 con licencia permisiva (4 Apache-2.0 +
3 MIT) · 1 sin licencia · 6 publicados en PyPI · 2 ausentes de PyPI con negativo calibrado · 1 sola con
release de 2024.**

### 🔴 El defecto de cotización que esta capa trae encima, y hay que decirlo ANTES de proponerla

**«Hay paquete publicado» y «hay paquete mantenido» son dos preguntas distintas, y este estante sólo venía
haciendo la primera** (el pase 84 inventarió 9 paquetes instalables sin mirarles la fecha). Medida la fecha,
el resultado es incómodo:

- **5 de 6** paquetes publicados tienen su última release **entre 2019 y 2022**.
- **1 de 6** (`EduCDM`) está vigente, con 13 versiones y release de **2024-10-25**.
- La mediana de antigüedad del estante publicado es de **~4 años**.

⇒ **La recomendación no es «instalar la familia»**, es: **`EduCDM` como dependencia; el resto, VENDORIZADO**
(copia del algoritmo dentro del proyecto, con su aviso Apache/MIT) y con los tests propios encima. Apache-2.0
y MIT lo permiten sin fricción. Lo que **no** conviene es pinnear `EduData==0.0.18` en un proyecto de cliente
y descubrir en integración que el loader de datasets apunta a URLs de 2021 (**P260**).

### 🔴 Y el hallazgo de TITULAR, que es el que aparece en la mesa de contrato

Dentro de **un mismo `org` institucional**, el titular del copyright **no es uniforme**:

- `EduData`, `EduCDM` → `Copyright [2020] [bigdata-ustc]` (la **organización**)
- `EduCAT` → `Copyright (c) 2019 tswsxk` (un **individuo**)
- `EduSim` → **fork** de `tswsxk/EduSim` (el árbol original es del **individuo**)

⇒ **2 de las 8 piezas no las tiene la institución.** Para un *engagement* con cesión explícita o auditoría de
procedencia, **a quién se le pide la cesión cambia según la pieza**, y el `org` no lo dice: hay que leer el
`LICENSE` de cada árbol. Esta base ya había pagado esta lección en el pase 85 (**P255**, el titular leído del
payload y no de una insignia); acá se repite **dentro de un solo propietario aparente**.

### ⚠️ Lo que este pase NO midió de estas filas, declarado en vez de rellenado

- **Forks de `EduData` y `EduCDM`**: no medidos. Se dejan como *no medido* y no se estiman.
- **Fecha del último commit**: ninguna de las 8 la expuso por el canal usado. **La vigencia de este pase se
  afirma sobre la fecha de RELEASE de PyPI, que sí es de primera mano, no sobre actividad de repo.**
- **Titular de `EduKTM`, `EduNLP`, `EduRec`**: sin línea de copyright localizada en la lectura hecha. La
  licencia sí está medida; el titular **no**.
- **`EduX` no se re-midió por un segundo canal**: su ausencia de licencia viene de una sola lectura.

## 🧾 Altas fundacionales: 0 — y el estante pierde un INSTRUMENTO que creía tener: sobre un árbol copyleft, el `sha256` del `LICENSE` no identifica NADA (pase 85 del 2026-10-04)

### 🔴 El método que este estante venía usando, y la mitad del catálogo donde está VOID

Desde el pase 68 este estante corona el origen de una familia de forks con `sha256(LICENSE)`:
**`P193`** («el hash que separa forks también UNE un paquete a su árbol») y **`P251`** (elegir punto
de partida sin coronar al padre equivocado). 🟢 **Sobre el racimo Canvas-MCP funcionó, y funcionó
bien: separó seis orígenes de once derivados.**

🔴 **Y funcionó por una razón que nadie había escrito: porque esos árboles son MIT, y un texto MIT
lleva el titular DENTRO.** El hash distingue porque el contenido distingue.

🔴 **Sobre un árbol copyleft el contenido NO distingue.** GPL-2.0, GPL-3.0, AGPL-3.0, LGPL,
Apache-2.0 y MPL-2.0 **no tienen ranura de titular**: el texto es idéntico, byte a byte, para todo
proyecto del planeta que lo embarque sin modificar. **Medido este pase, no razonado:**

| Árbol | `sha256` del archivo de licencia | |
|---|---|---|
| `OpenEMIS/core` (GPL-2.0, 15.518 B) | **`b6f03c6715ee7b0f`** | |
| `caravanadestrucs/coreemis` (GPL-2.0, 15.518 B) | **`b6f03c6715ee7b0f`** | 🔴 **idéntico** |
| `gibbonedu/core` (GPL-3.0, 35.121 B) | `93178a43d6d3` | |
| `macsnoeren/genai-open-assessment` (GPL-3.0, 35.149 B) | `3972dc9744f6` | ⚠️ difiere sólo por 28 B de empaquetado |

🔵 **Es exactamente lo que `P198` midió en el pase 69 —un *boilerplate* prístino carga CERO
identidad y su hash colisiona por diseño— y lo que este pase agrega es la CONSECUENCIA PARA ESTE
ESTANTE: la pregunta «¿de qué árbol parto?» no se puede responder por licencia sobre ninguna pieza
copyleft, y copyleft es la familia de Moodle, Gibbon, ClassroomIO, OpenEduCat, INGInious,
`frappe/education` y el alta de hoy.**

### 🟢 Con qué se responde entonces, y está medido

**Por el ÁRBOL, no por la cesión.** Sobre el par `OpenEMIS/core` ↔ `caravanadestrucs/coreemis`:

| Canal | `OpenEMIS/core` | `caravanadestrucs/coreemis` | Veredicto |
|---|---|---|---|
| `sha256(LICENSE)` | `b6f03c6715ee` | `b6f03c6715ee` | 🔴 **idéntico y NO concluyente** |
| `sha256(composer.json)` | `7865d398fc14` | `7865d398fc14` | 🟢 **idéntico — y SÍ concluyente** |
| `sha256(README.md)` | `e3dc70736884` | `e3dc70736884` | 🟢 **idéntico — y SÍ concluyente** |

→ **copia VERBATIM, establecida por el manifiesto y el *readme*.** 🔵 **La regla operativa para
este estante: en MIT basta la licencia; en copyleft hay que pedir el MANIFIESTO (`composer.json`,
`package.json`, `Cargo.toml`, `pyproject.toml`), que es el archivo que sí lleva identidad.**

### 🟢 Lo que sí cambia para quien va a partir de una de estas piezas

⚠️ **Y la cota, dicha antes de que alguien la use de atajo: dos manifiestos idénticos prueban COPIA,
no prueban DIRECCIÓN.** Que `coreemis` sea copia de `OpenEMIS/core` y no al revés se sostiene en la
adopción (**24 ★ / 18 forks** contra **0 / 0**) y en que el `README` copiado apunta al sitio de
OpenEMIS, **no** en el hash. **La dirección sigue siendo una inferencia, y se declara como tal.**

### 🔴 Y el barrido fundacional del pase, declarado

`open source platform {industria} ERP CRM MIT Apache` devolvió, por **decimocuarta vez**,
`openeducat`, `erpnext`/`frappe` y Odoo — **las tres ya en este estante**, confirmado por `grep`
antes de buscar. 🟢 **Lo único no inventariado del canal fue el eje EMIS, y su pieza es
plataforma, así que va a `verticals/solutions.md` y no acá** (misma regla con la que
`frappe/education` salió de este estante en el pase 41).


## 🧾 Altas fundacionales: 0 — y el estante gana la pregunta que va ANTES de clonar: ¿de qué ÁRBOL se parte? (pase 84 del 2026-10-04)

🔴 **Ninguna pieza fundacional nueva.** La búsqueda de plataformas del encargo
(`open source platform education ERP CRM MIT Apache`) devolvió `OpenEduCat` y `Moodle`, **las dos ya
inventariadas**, y las búsquedas de agentes devolvieron la capa genérica por decimotercera vez.

### 🟢 Lo que sí cambia para quien va a partir de una de estas piezas

**El pase 84 midió que, para una pieza con paquete publicado, el árbol del ORIGEN puede NO reproducir
el artefacto que el cliente instala.** Caso medido: los 5 archivos del *tarball* de `canvas-mcp@1.1.0`
dan **404 en `vishalsachdev/canvas-mcp`** —el repo al que el propio paquete apunta con
`repository.directory: "cli"`— y **200 en el fork `fdis111/canvas-mcp`**, con **4 de 5 byte a byte
idénticos**. ✅ **Control positivo: la raíz del origen (`package.json`, `README.md`, `LICENSE`) da 200,
así que `HEAD` resuelve y los 404 son reales.**

🔵 **La regla operativa para este estante, que es `P254`:**

1. **Bajar el *tarball* del registro** — es la única copia **inmutable** de lo que el cliente instala.
2. **Comparar por `sha256` archivo por archivo** contra el árbol del origen **y contra los forks**.
3. 🟢 **Partir del árbol que REPRODUCE el *tarball*, no del que lleva el nombre del autor.**
4. ⚠️ **Declararlo en la propuesta:** el titular del `LICENSE` sigue siendo del origen (**`P184`**) y el
   código de partida puede no serlo.

### ⚠️ Y la cota que hay que leer antes de cotizar «hay paquete, hay producto»

🔴 **El paquete publicado del origen del racimo más forkeado de esta base son 5 archivos y 2.704 B de
*setup wizard*: `bin/cli.js`, `lib/wizard.js`, `lib/clients.js`, `lib/config-writer.js`.** **No trae
servidor MCP ni UNA herramienta** — el servidor existe sólo en el árbol, bajo un nombre
(`canvas-mcp-code-api`) que **no está publicado**. 🔵 **Así que «publicado» e «instalable como
producto» son cosas distintas, y el estante lo dice ahora explícitamente.** Ver **`P253`** y
`compose/code/p253-registry-first-identity/` (**27/27**).


## 🧾 Altas fundacionales: 0 — y el estante gana una COTA de reutilización: 7 de sus piezas Canvas son el mismo árbol con siete dueños (pase 83 del 2026-10-04)

🔴 **El dato que cambia cómo se cuenta este estante: de los 17 `org/repo` Canvas que esta base cita, 7
comparten el `LICENSE` byte a byte (`sha256:5385a26e2face987`, titular `Copyright (c) 2025 Vishal
Sachdev`) y son UN origen más 6 derivados.** 🔵 **Un estante que los cuenta como 7 puntos de partida
distintos sobre-cuenta el código disponible por un factor de 7** — es **`P146`** («la unicidad se cuenta
sobre CÓDIGO DISTINTO, no sobre repos distintos») medido ahora sobre el cohorte completo y no sobre
pares.

| Lo que el estante tiene | Lo que el estante OFRECE |
|---|---|
| **17** `org/repo` Canvas citados | 🔴 **6 orígenes** (`vishalsachdev`, `bruchris`, `r-huijts`, `CharlieCardenasToledo`, `mtgibbs`, `xmike04`) |
| de ésos, **14** con licencia legible | 🟢 **6 de 6 orígenes permisivos** — MIT en los seis, medida por bloque de título |
| **7** derivados medidos | ⚠️ **heredan el árbol del origen: no son puntos de partida independientes** |
| **4** indeterminados | 🔴 **3 sin archivo de licencia** (`DMontgomery40` **existe** y no lo tiene: `P161`) **+ 1 con titular colectivo** (`ahnopologetic`) |

🟢 **Para elegir punto de partida sobre Canvas el estante real tiene SEIS candidatos, no diecisiete, y
los seis son MIT.** 🔵 **Y el que concentra la adopción y la dirección técnica es `vishalsachdev/canvas-mcp`,
el único con región verificada de primera mano (North America, pase 56).**

⚠️ **Cota de reutilización que no se ve en la licencia: los 7 del racimo publican el MISMO nombre de
paquete (`canvas-mcp-code-api`) y ninguno declara `repository`**, así que **fijar una dependencia por
nombre de paquete en esta familia no es ambiguo — es indecidible** (`P190` a escala de cohorte). 🟢 **La
forma correcta de fijarla es por `org/repo` + commit**, que es lo que **`P150`** ya pedía por otra razón.

🔴 **Y una medida que NO se puede tomar con el instrumento del pase 82: `docs/TOOLS.md` existe en 1 de
los 17 repos**, así que la superficie comparada entre candidatos de este estante **no está medida** y se
declara como hueco en vez de estimarse de la prosa.

Instrumento, compuerta y controles en `compose/code/p251-cohort-lineage/` — **26/26**.

## 🧾 Altas fundacionales: 0 — y el estante entero pasa a tener una columna que no tenia: si Globant puede VENDER sobre cada pieza (pase 82 del 2026-10-04)

🔴 **Sin altas de repo fundacional en este pase.** 🟢 **Lo que cambia es el criterio con el que se
mira el estante, y cambia para las 69 filas `org/repo` del catalogo a la vez.**

### 🔴 El defecto que este estante tenia y no se veia

Un repo fundacional entra aqui porque su licencia permite construir encima. 🔴 **Pero el instrumento
que medía la licencia devolvía `UNKNOWN` cuando no reconocía el texto, y `UNKNOWN` es indistinguible
de *«el uso comercial esta PROHIBIDO»*** — que es justamente la respuesta que descalifica una pieza de
este estante. 🟢 **Desde este pase son dos columnas separadas** (`P250`):

| Familia de licencia | Uso comercial | Lectura para el estante |
|---|---|---|
| 🟢 MIT · Apache-2.0 · BSD · **0BSD** · **Unlicense** · CC0-1.0 | 🟢 `OK` | **Apto sin condiciones** — 38 de 43 licenciadas (**88,4 %**) |
| ⚠️ AGPL-3.0 · GPL-3.0 | 🟢 `OK` | **Apto con decision de ARQUITECTURA**: el copyleft no prohibe vender, obliga sobre la distribucion |
| ⚠️ **CC-BY-SA-4.0** | 🟢 `OK` | **ShareAlike de CONTENIDO**: viaja al entregable del cliente |
| 🔴 **NONCOMMERCIAL-NOT-OSI** | 🔴 `PROHIBIDO` | **Fuera del estante.** 1 de 43 |
| ⚠️ sin archivo de licencia / inalcanzable | ⚠️ `SIN-DETERMINAR` | **26 de 69** — pregunta abierta, **no** «permisivo por omision» |

### 🟢 Tres familias que este estante no sabia nombrar, y una de ellas MEJORA la cotizacion

| Pieza | Antes | 🟢 Ahora | Por que importa aqui |
|---|---|---|---|
| `trilogy-group/oneroster-ts` | `UNKNOWN` | 🟢 **0BSD**, 710 B | **Mas permisiva que MIT**: sin obligacion de atribucion. Es la licencia mas comoda de todo el estante |
| `FWU-DE/mem-mcp` | `UNCLASSIFIED` | 🟢 **Unlicense**, 1.210 B | **Dominio publico, con titular institucional PUBLICO aleman** — el perfil ideal para un pliego de EMEA |
| `nmarafo/OpenDidactia` | `UNKNOWN` | ⚠️ **CC-BY-SA-4.0**, 2.122 B | ShareAlike sobre esquemas curriculares: **condicion que hay que poner sobre la mesa antes de la propuesta** |
| `kaldi-asr/kaldi` | `UNKNOWN` en `p170` | 🟢 **Apache-2.0**, 17.263 B | Su `COPYING` abre con un aviso legal y el bloque de titulo queda abajo: **el classificador compartido lo resuelve y el de `p170` no** |

⚠️ **Honestidad sobre el hallazgo: ninguna de las cuatro es un descubrimiento. Las cuatro estaban
resueltas EN PROSA desde los pases 51 y 64.** 🔵 **Es `P237` otra vez —la correccion nunca llego al
codigo— y por eso se arreglo en `lib/license_family.sh`, el control compartido (18/18 → **41/41**), y
no en el barrido de turno.**

### 🟢 Y el barrido confirma que el estante esta VIVO

🔴 **El pase 81 escribio que el canal de verificacion marcaba muerto el 100 % del catalogo.**
🟢 **Re-medido por un canal CALIBRADO (200 a una URL buena, 404 a una inexistente): 43 `LICENSED` ·
23 `UNLICENSED` con ausencia MEDIDA · 3 `UNREACHABLE` → **66 de 69 alcanzables (95,7 %)**, y CERO
deriva en los 58 slugs que comparte con el resultado del pase 64.** 🔵 **Ningun repo de este estante
se cae por el pase 81.**

## 🧭 P244 — el eje SPEC sobre la capa SERVIDOR de xAPI, que **P235** midió sin medirlo: la trampa de OneRoster NO se reproduce, y el permisivo con respaldo EMEA es el único que se queda afuera (pase 80 del 2026-10-04)

**P235** (pase 77) midió la capa xAPI por **CAPA** y concluyó que *«EXPONER xAPI —ser el LRS— se puede
hoy, con licencia permisiva y mantenimiento de esta semana»*. 🔴 **Lo que su `result.tsv` NO registró
en ninguna de las nueve filas fue la VERSIÓN DE SPEC: las nueve dicen `(sin version en el arbol)`.**

Y esa es exactamente la columna que decidió la capa OneRoster: `go-oneroster` es **MIT, permisivo y
vivo de licencia**, y resulta **inusable** porque implementa **v1p1**, un spec **superado en 2023**.
🔵 **Este pase le hace a xAPI la pregunta que esa lección obliga: ¿hay un LRS permisivo en el spec
VIGENTE —xAPI 2.0 / IEEE 9274.1.1— o sólo en 1.0.3?**

### 🟢 Resultado: hay TRES PERMISIVOS sobre CUATRO conformantes medidos, y la trampa de OneRoster no se reproduce

| Servidor | Licencia (**bloque de título**) | Titular (**P184**) | xAPI 2.0 / IEEE 9274.1.1 | ★ | Evidencia **en el árbol** |
|---|---|---|---|---|---|
| 🟢 **`yetanalytics/lrsql`** | **Apache-2.0** | 🟢 `Yet Analytics, Inc.` → **`HOLDER-MATCH`** (persona jurídica) | 🟢 **SÍ — 1.0.3 + 2.0.0**, negociado **por request** con `X-Experience-API-Version` | — | `doc/xapi_versioning.md` |
| 🟢 **`adlnet/ADL_LRS`** | **Apache-2.0** | 🟢 `Advanced Distributed Learning` (`readme.md:23`) | 🟢 **SÍ — IEEE 9274.1.1 por su propio readme** | **331** | `readme.md:3` · ⚠️ y `:5` se autodeclara **PoC**: *«only intended to support a small amount of users»* |
| ⚠️ **`pelotech/xapi-lrs`** | **Apache-2.0** | 🔴 **AUSENTE — medido** (ver abajo) | 🟢 **SÍ — 1.0.3 + 2.0.0, y es el único con conformidad EN CI** | 🔴 **0** | `package.json` · `.github/workflows/ci.yml` |
| 🔴 **`raif-s-naffah/xapi-rs`** | 🔴 **`GPL-3.0-or-later`** (**payload**: `Cargo.toml`) | 🔴 `Raif S. Naffah <raif@mailbox.org>` — persona fisica, correo generico → **sin region** (**P135**) | 🟢 **SI — v2.0.0 conformante** (*«HTTP Server implementation of IEEE Standard … version 2.0.0 LRS»*) | 🔴 **0** (0 forks) | `Cargo.toml` (`license`, `authors`, `edition = "2024"`) · **pase 81** |
| 🔴 **`openfun/ralph`** | **MIT** (`LICENSE.md`) | 🟢 `France Université Numérique` → **`HOLDER-MATCH`** · 📍 **EMEA** | 🔴 **NO — clavado en 1.0.3** | — | `docs/index.md:63` *(«we're following the xAPI specification **1.0.3**»)* **+** `src/ralph/api/routers/statements.py`, que fija sus 4 referencias al tag `1.0.3` del spec |

🆕 **Pase 81: la cuarta fila cierra el denominador, y el conteo permisivo no se mueve.**
`raif-s-naffah/xapi-rs` es **conformante con v2.0.0** y **`GPL-3.0-or-later` leido del payload**, con
**0 ★ / 0 forks**. 🟢 **Asi que *permisivo + spec vigente* sigue dando TRES, pero ahora sobre 4 de 4
conformantes MEDIDOS en vez de 3 encontrados** — el unico que faltaba resulto copyleft, lo que vuelve
la afirmacion del pase 80 mas fuerte y no mas debil. 🔴 **Y la asimetria regional de la tendencia 624
se sostiene por una segunda razon independiente: el candidato nuevo no declara afiliacion (**P135**) y
encima es copyleft, asi que *EMEA-soberano + xAPI 2.0* sigue sin existir.** ⚠️ **Colision de nombre
registrada: `pawelkn/xapi-rs` —nombre EXACTAMENTE igual— es una libreria de trading xStation5, sin
relacion con educacion** (**P188**).

🔵 **Por lo tanto el eje SPEC separa a los dos estándares por segunda vez y en el MISMO sentido que el
eje CAPA de P235:** en OneRoster, pedir *permisivo + vivo + spec vigente* en la capa servidor deja
**cero** piezas; en xAPI deja **tres**. **La trampa de `go-oneroster` es una propiedad de OneRoster,
no del sector** — y generalizarla a xAPI habría descartado una capa que está sana.

### 🔴 La consecuencia que cuesta dinero, y es regional

**El único de los cuatro con respaldo institucional EMEA es el único que NO llega a 2.0.** `ralph` es
**MIT** y su titular es **France Université Numérique** —una persona jurídica pública francesa—, que
es precisamente el perfil que el patrón de **soberanía EMEA** (**P63**) venía recomendando. 🔴 **En
xAPI 2.0 ese perfil no está disponible:** la combinación *EMEA-soberano + spec vigente* obliga hoy a
elegir entre `lrsql` (Apache-2.0, titular estadounidense) o una pieza **sin titular**. ⚠️ **Es un
dato de arquitectura para un pliego público europeo, no una preferencia.**

### 🔴 `pelotech/xapi-lrs` — permisivo y **sin titular en ninguna parte del árbol**, ausencia MEDIDA

| Dónde debería estar el titular | Resultado medido |
|---|---|
| `LICENSE`, líneas con `Copyright` | **12 coincidencias, y las 11 primeras son el CUERPO de la Apache-2.0** |
| `LICENSE:189` — la única candidata | 🔴 **`Copyright [yyyy] [name of copyright owner]`** — el **apéndice SIN RELLENAR** |
| `NOTICE` | 🔴 **404** |
| `AUTHORS` | 🔴 **404** |
| `package.json` → `author` | 🔴 **ausente** |
| `package.json` → `license` | 🔴 **ausente** (la licencia sólo está en el archivo y en la prosa del README) |

🔵 **Veredicto `HOLDER-ABSENT`, y es justo el caso que `p184-holder-mismatch` existe para no errar:**
el instrumento **debe NEGARSE** a publicar la línea del apéndice como titular, igual que debe negarse
a publicar una frase del cuerpo de Apache o el *copyright* de la FSF. ⚠️ **Consecuencia para una
consultora:** la **Apache-2.0 §4(c)** obliga a **conservar los avisos de copyright** de la obra — **y
no hay aviso que conservar**; el otorgante de la cesión no está identificado. El nombre de la
organización en GitHub (`pelotech`) es un **nombre de CUENTA**, no una persona jurídica declarada.
🔵 **Es una bandera de diligencia, no un bloqueo:** el texto de la licencia es permisivo y completo.

### 🟢 El hallazgo OPERATIVO, que vale más que la fila de catálogo: toma de posesión de una base `lrsql` VIVA

`xapi-lrs` declara **paridad de catálogo con la forma Postgres de `lrsql` v0.9.5**, y que por eso
**puede apuntarse a una base `lrsql` viva y tomarla en el lugar** — *«no dump/restore needed»*, con
*statements*, actores, documentos y **credenciales** pasando sin modificación. **Y no es sólo prosa
del README: está en la matriz de CI.**

```
driver: [pg, pglite] × xapi-version: ['1.0.3', '2.0.0'] × schema-source: [migration, lrsql]
```

🟢 **8 trabajos de conformidad por *commit***, con `SCHEMA_SOURCE=lrsql` como una de las dos fuentes de
esquema — o sea que **la toma de posesión se ejercita en CI contra las DOS versiones de spec y los DOS
drivers**, no se afirma de palabra.

⚠️ **Y la auto-corrección del pase, que importa porque casi calificó de menos el dato más fuerte de la
tabla:** un título de *commit* de ese repo habla de *«ADL conformance **fork** bumps need
inspection»*, lo que invitaba a publicar *«su conformidad 2.0 descansa sobre un fork de la suite»*.
🔴 **Es falso.** `package.json:62` fija la suite **OFICIAL** y **por SHA**:

```
"adl-lrs-conformance-tests": "github:adlnet/lrs-conformance-test-suite#5bc232d349c60faded8240da698f195106091638"
```

🔵 **Suite oficial de ADL, anclada por SHA, que es la forma MÁS fuerte posible —reproducible— y no la
más débil.** (El `pool: 'forks'` de `vitest.config.ts` es el pool de procesos de vitest y no tiene
relación.) **Se comprobó antes de escribir; de no haberse comprobado, este pase habría publicado una
calificación falsa sobre la única pieza con conformidad en CI.**

### ⚠️ La cota de `xapi-lrs`, por delante de cualquier recomendación

🔴 **0 ★ / 0 forks** · `HEAD` **2026-08-08** · **v0.9.6, pre-1.0** · y un **cambio incompatible
declarado**: las bases anteriores a **v0.6.0** *no son actualizables* —la sonda de arranque detecta el
esquema desajustado y **se niega a arrancar** en vez de servir contra él (lo cual, en sí, es buen
comportamiento). 🔵 **Por eso NO entra como recomendación de estante: entra como la ÚNICA ruta medida
de «xAPI 2.0 + toma de posesión de `lrsql`», con su cota escrita.** La recomendación de capa sigue
siendo **`lrsql`** (Apache-2.0, titular jurídico, 1.0.3 + 2.0.0) y, si el cliente necesita el
*blessing* del organismo, **`ADL_LRS`** con su cota de PoC declarada por su propio readme.

### 🟡 La trampa de interoperabilidad que `lrsql` documenta y conviene no descubrir en producción

De `doc/xapi_versioning.md`, literal: **por omisión, una petición con
`X-Experience-API-Version: 1.0.3` puede recibir *statements* en formato `2.0.0`.** Para que los
`2.0.0` se **degraden** a `1.0.3` hay que encender `LRSQL_ENABLE_STRICT_VERSION`
(`enableStrictVersion`). ⚠️ **Un cliente 1.0.3 legado recibe cargas 2.0.0 en silencio si nadie puso
esa variable** — y el *default* es el permisivo. 🔵 **Y las *reactions* generan `1.0.3` por omisión
(`LRSQL_REACTION_VERSION`): crearlas en `2.0.0` y después restringir el LRS a `1.0.3` rompe el
front-end del Admin UI**, con un procedimiento de recuperación declarado (reactivar 2.0.0, borrar las
incompatibles, volver). **Es configuración de un renglón que decide si una migración de spec es
transparente o un incidente.**

---

## 🧪 Altas fundacionales: 0 — y la mejor candidata del pase se autodescalifica de este estante, por escrito (pase 79 del 2026-10-04)

El canal devolvió **seis repos que esta KB no tenía** (verificado por `grep` sobre los *slugs* ya
catalogados antes de medir) y 🔴 **ninguno es fundacional.** Se dice en vez de promover una pieza a
este estante para que no quede vacío.

🔵 **La candidata que más cerca estuvo, y el motivo exacto por el que no entra acá.**
`MysterionRise/adaptive-knowledge-graph` (🟢 **MIT**, `LICENSE` 1.520 B, **17 ★**, 137 commits) es la
referencia de **arquitectura** más completa que esta KB tiene de **KG-RAG + BKT/IRT con inferencia
local** —Neo4j con aristas de prerrequisito, BM25 + vectorial en OpenSearch con *reranking*, Ollama
local, citas con fragmento, y un arnés de **50+ casos dorados de OpenStax**—. ⚠️ **Y su propio README
la descalifica de este estante por escrito:** *«controlled client-demo and AI engineering portfolio
prototype»*, *«not as a production certification platform»*, **sin LMS/LTI, sin modelo de
inquilinos, sin certificación de cumplimiento, sin IRT calibrado** y **perfiles de alumno
sintéticos**.

🟢 **Entró a `agents/top.md` como referencia de arquitectura y NO acá como base de producción.** Es
la regla de **P234** aplicada en su dirección útil: la fila hereda la **capacidad** del código, no la
**ambición** del README — con la diferencia, poco común, de que acá el README fue el honesto y lo que
había que respetar era su propia cota.

⚠️ **Y el barrido de plataformas sólo devolvió confirmación:** **OpenOLAT** (Apache-2.0, 20.3.4 de
junio de 2026), el SDK de **OpenProct**, **OpenEduCat**, **ERPNext/`frappe/education`** y
**`frappe/lms`** 🔵 **ya estaban todos en esta base.** El estante no crece este pase, y la razón no es
que no se buscó.

## 🧪 Cero altas de repo fundacional, y el barrido de plataformas devolvió sólo confirmación (pase 78 del 2026-10-03)

🔴 **Cero altas, con lo buscado escrito.** La consulta obligatoria de plataformas verticales se corrió
(`open source education ERP SIS student information system MIT Apache self-hosted 2026`) y **todo lo
devuelto ya estaba en esta base**, verificado por `grep` antes de escribirlo:

| Pieza devuelta | Estado en esta KB |
|---|---|
| **OpenEduCat** (ERP educativo, 70+ módulos) | 🔵 ya registrada (159 menciones) |
| **GegoK12** (MIT, PHP 8.4 + Laravel 12, v1.1 de marzo 2026) | 🔵 ya registrada (47 menciones) |
| **RosarioSIS** (SIS, PHP + PostgreSQL) | 🔵 ya registrada (31 menciones) |
| **openSIS** / **OS4ED** | 🔵 ya registrada (37 / 12 menciones) |
| **ERPNext** (módulo Education) | 🔵 ya registrada (81 menciones) |

🟢 **La única pieza del barrido que esta base NO tenía, y por qué igual no entra:** **eduTrac SIS**
(0 menciones) — ⚠️ el canal lo ofrece desde **SourceForge**, no desde un repo con licencia y `HEAD`
verificables por los instrumentos de esta KB (**P170** / **P172** miden por `raw.githubusercontent`
con `ref HEAD`). 🔴 **Sin medición de licencia por payload no entra como fundacional**, y se registra
como **candidata pendiente de canal**, no como hallazgo.

🔵 **Lectura del agotamiento, que es el dato y no el fracaso:** es el enésimo barrido consecutivo en
que la capa de plataformas verticales **no mueve**. Esa capa está **cubierta**; el margen de esta KB
dejó de estar en descubrir plataformas y está en **medir lo que ya tiene** — que es exactamente donde
este pase gastó su presupuesto (ver `agents/top.md` y `compose/code/p239-table-integrity/`).

## 🪪 La capa de ROSTERING de K-12, medida ENTERA por licencia: pedir «permisivo + vivo + spec vigente» deja UNA pieza en pie (pase 75 del 2026-10-03)

🔵 **Continúa el pase 74 por el lado que dejó abierto.** Ese pase estableció que en K-12 la fundación
no es el LMS sino **la capa de integración**, y agregó el puente Ed-Fi → OneRoster → Clever. **Este
pase midió la capa completa por LICENCIA, y el resultado reordena la recomendación.**

### 🔬 El canal de verificación de este pase, dicho antes de las filas

| Canal | Resultado | Para qué sirvió |
|---|---|---|
| `raw.githubusercontent.com/{o}/{r}/{main,master}/LICENSE` | 🟢 **200** | **el texto** de licencia, leído del archivo |
| `github.com/{o}/{r}` por WebFetch | 🟢 sirvió | descripción, ★, lenguaje, **estado de archivado** |
| `api.github.com/repos/{o}/{r}` | 🔴 **403** | — |
| `api.github.com/rate_limit` | 🟢 200 | ⚠️ el único endpoint que pasa es el que **no** transporta dato de repo |
| `github.com` / `codeload.github.com` por `curl` | 🔴 **403** | — |

### 🧾 Las filas, con la licencia leída del ARCHIVO y no de una insignia

| Repo | Licencia (del archivo) | Estado medido | Spec | Qué cubre |
|---|---|---|---|---|
| ⚠️ **`bgwdotdev/go-oneroster`** | **MIT** (`master/LICENSE`, titular **`fffnite`** 2019) | 🔴 **`HEAD` 2019-11-04 — 6,9 años** · 8 ★, Go | 🔴 **v1p1 — spec SUPERADO** (1.2 desde 2022; 1.1 *sunset*) | servidor REST + MongoDB, y **extiende el spec con ESCRITURA** (PUT/POST en todos los endpoints). 🔴 **Corregido en el pase 76: esta celda decía «vivo» y la tabla de frescura de ESTE MISMO archivo (más abajo) la data muerta hace 6,9 años.** 🔁 **Y es un duplicado byte a byte de [`fffnite/go-oneroster`](https://github.com/fffnite/go-oneroster), que es el upstream** |
| 🔴 **`usechalk/chalk`** | **AGPL-3.0** (`main/LICENSE`) | vivo, 2 ★, Rust, **298** commits | OneRoster 1.1 + CSV | 🟢 **la única pieza que cubre las cinco propietarias**: PowerSchool, Infinite Campus, Skyward, **Clever** y **ClassLink** (importadores de migración + compat OAuth), más Google Workspace, AD/LDAP y Entra ID — **en un binario** |
| 🔴 `bgwdotdev/libre-oneroster` | **AGPL** (`master/LICENSE`) | vivo, Rust | OneRoster 1.1 | servidor + librería + CLI |
| 🔴 `lepo-project/roster-hub` | **AGPL** (`main/LICENSE`) | vivo | OneRoster v1.1 | gestión de *roster*, conversor CSV → REST |
| ⚠️ `ridencww/uniroster-server` | **MIT** (`master/LICENSE`) | 🔴 **ARCHIVADO 2024-09-26**, 6 ★, Node | 🔴 **v1.0 solamente** | v1.1 y Ed-Fi figuran como **planeados**, no construidos |
| 🔴 **`Tools4ever-NIM/*`** (familia) | 🔴 **NO HAY ARCHIVO DE LICENCIA** en `main` ni `master` | viva | OneRoster v1.1 y **v1.2** | los **únicos** conectores de **Skyward** (v1.1, v1.2) e **Infinite Campus** (v1.2) fuera de `chalk` |
| 🟢 **`jdolny/OneRoster.NET`** | **MIT** (`master/LICENSE`, titular **`theopenem`** 2020) | ⚫ `HEAD` 2023-10-13 — 3,0 años | 🟢 **v1p1 + v1p2** | 🆕 **alta del pase 76, y es el ÚNICO permisivo de la capa con el spec VIGENTE.** Capa **cliente** (no servidor) y **sólo rostering** (*«Grade book has not been implemented»*). Dos flujos de credencial en la API pública: `V1p1(baseUrl, consumerKey, consumerSecret)` vs `V1p2(tokenUrl, baseUrl, clientId, clientSecret)`. ⚠️ **Su README dice haberse escrito contra un BORRADOR de 1.2** |
| 🟢 `gotranseo/oneroster` | **Apache-2.0** (`main/LICENSE.txt`) | ⚫ `HEAD` 2023-05-01 — 3,4 años | v1p1 | alta del pase 76. Librería **Swift/Vapor**, capa cliente. **La licencia faltaba en la fila que esta base ya tenía** |
| ⚫ `jrissler/ex_oneroster` | **Apache-2.0** (`master/LICENSE`) | 🔴 **sólo-lectura por decisión del autor** | v1p1 | alta del pase 76. Elixir/Phoenix. 🔵 **Donado *upstream* al organismo del estándar**: el README redirige a `IMSGlobal/ex-OR-code` (*«Now supporting this through IMS»*) |
| 🔴 `the-glasgow-academy/oneroster-api-to-csv-sds` | 🔴 **SIN ARCHIVO DE LICENCIA** — ausencia **MEDIDA**: 10 nombres × `main` y `master` en 404, `README.md` en 200 | viva | v1p1 | alta del pase 76. **El único puente abierto a Microsoft School Data Sync**, al *«UK standard CSV»*. PowerShell Core. 📍 **EMEA** |
| 🔴 `the-glasgow-academy/oneroster-api-to-csv-asm` | 🔴 **SIN ARCHIVO DE LICENCIA** (ídem, ausencia MEDIDA) | viva | v1p1 | alta del pase 76. **El único puente abierto a Apple School Manager**. PowerShell Core. 📍 **EMEA** |

### 🔴 El hallazgo que manda, CORREGIDO en el pase 76: el callejón es de CAPA, y las piezas que cumplen las tres condiciones son CERO

⚠️ **Lo que esta sección decía hasta el pase 75** —«las tres condiciones se cumplen juntas en
**exactamente una** pieza: `go-oneroster`»— 🔴 **se falsifica con datos de este mismo archivo.** Las
tres condiciones, evaluadas **por separado** y cada una contra su propia evidencia
(`compose/code/p230-rostering-layer-axis/`, **10/10** piezas medidas):

| Condición | `go-oneroster` | Evidencia |
|---|---|---|
| permisiva | 🟢 **sí** | MIT, payload de `master/LICENSE` |
| viva | 🔴 **no** | `HEAD` **2019-11-04 — 6,9 años**, por la tabla de frescura de ESTE archivo |
| spec vigente | 🔴 **no** | **v1p1**; **1.2 se publicó en 2022, superó a 1.1 en 2023** y 1.1 quedó *sunset* |

🔴 **El conteo correcto es 0, no 1 — y el callejón es más cerrado que lo que se publicó, no menos.**
La celda «vivo» de la tabla de arriba contradecía a la tabla de frescura de más abajo **en el mismo
`HEAD`**; P229 le preguntó la vitalidad a la prosa de su propia fila y no a la tabla que esta KB ya
tenía.

🪜 **Y el eje que SÍ explica la capa es CAPA, no licencia:**

| Capa | Permisivo | Copyleft | Sin licencia | ¿Alguno con **v1p2**? |
|---|---|---|---|---|
| **servidor** | `go-oneroster` (MIT, v1p1, muerto) | `libre-oneroster` · `chalk` · `roster-hub` (AGPL-3.0) | — | 🔴 **ninguno** |
| **cliente** | `OneRoster.NET` (MIT) · `gotranseo` (Apache-2.0) · `TCI/OneRoster` (MIT, 🟢 vivo) · `ex_oneroster` (Apache-2.0) | — | — | 🟢 **uno: `OneRoster.NET`** |
| **puente** (SDS / Apple School Manager) | — | — | 🔴 **los dos de Glasgow** | 🔴 ninguno |
| **conector SIS** | — | `chalk` (AGPL-3.0) | 🔴 `Tools4ever-NIM/*` | ⚠️ sí, **pero sin licencia** |

🔵 **La frase que cotiza: CONSUMIR OneRoster con spec vigente y licencia permisiva se puede hoy
(`OneRoster.NET`, MIT, v1p2); EXPONERLO no.** No existe servidor permisivo en v1p2, así que ser la
**fuente** de *roster* obliga a **construir** o a tomar **AGPL-3.0** y asumir el despliegue del
distrito. **Es una decisión de CAPA, no de licencia.**

🧪 **Y el error de método que lo escondió, porque es el aporte más transferible del pase 76:**
`repos/trending.md:3383` registraba la licencia de `OneRoster.NET` como **«— (no verificada: repo
muerto)»**. 🔴 **«Muerto» no exime de medir la licencia: la hace más importante.** Un permisivo muerto
**se bifurca**; un AGPL muerto **no**. El costo de la omisión fue **una petición HTTP**, y escondió el
único dato que P229 declaró inexistente.

Sobre el resto de la tabla, cada pieza cae por un motivo distinto:

- **AGPL** (`chalk`, `libre-oneroster`, `roster-hub`) → sirve para un despliegue **del distrito**, no
  para embeber en producto propietario;
- **archivada y v1.0** (`uniroster-server`) → MIT no alcanza si el spec quedó dos versiones atrás;
- 🔴 **sin licencia** (`Tools4ever-NIM`) → *all rights reserved* por defecto. **Y es la única vía a
  Skyward e Infinite Campus que no sea AGPL**, así que el hueco de esas dos plataformas **no es de
  investigación: es de derechos.**

⚠️ **Un caso de deriva de descripción (P165) medido en este pase:** el canal de búsqueda presentó
`uniroster-server` como *«multiple protocols (e.g., OneRoster, Ed-Fi, etc.)»*. **El árbol dice v1.0
soportado, v1.1 y Ed-Fi planeados, y archivado desde septiembre de 2024.** La capacidad estaba en el
*snippet*. 🔵 **Por eso el estado de archivado se agregó a la tabla como columna propia: una licencia
permisiva sobre un árbol archivado es una trampa que la columna de licencia sola no muestra.**

### 🟢 La distribución de la capa, con denominador propio

De los **18** repos del *topic* `oneroster` de GitHub: **1** supera 10 ★
(`Apereo-Learning-Analytics-Initiative/OpenLRW`, **62 ★**, *Educational Community License*, ya en
esta base), **2** están entre 2 y 8 ★, y 🔴 **15 tienen ≤ 1 ★.** Esto confirma la tendencia **584**
con un denominador externo en vez de una muestra: **la capa está atomizada, y no hay un incumbente
open source al que sumarse.**

🔵 **La consecuencia práctica para un engagement de K-12, y es la recomendación que reemplaza a la
del pase 74:** la elección **A (`go-oneroster`, MIT) vs B (`chalk`, AGPL-3.0)** se resuelve por
**modelo de entrega antes que por técnica**, porque el *delta* entre las dos no es un módulo: **son
cinco integraciones propietarias.** La receta completa, con la regla de decisión, en **P229**.

---

## 🔌 La capa de ROSTERING gana el eslabón que le faltaba, y el pase reencuadra cuál es la plataforma fundacional de K-12 (pase 74 del 2026-10-03)

### 🔴 Primero el reencuadre, porque cambia qué cuenta como «fundacional»

Este repositorio eligió sus fundaciones de K-12 por **presencia en la base de código abierto**
(Moodle desde el pase 1; Canvas en **229 líneas / 389 ocurrencias** de los cuatro archivos de
contenido). El canal de mercado de este pase dice que la
**base instalada** ordena distinto:

| Plataforma | Cuota de LMS (canal de este pase) | Estado en esta KB antes del pase 74 |
|---|---|---|
| **Google Classroom** | 🟢 **~39 % — primera** | 🔴 **0 menciones en 73 pases** |
| Canvas | ~19 % (41 % en superior de NA) | **229 líneas / 389 ocurrencias** (4 archivos) |
| Moodle | ~14 %, **19 % (2017) → 7 % (2026)** | fundacional desde el pase 1 |
| Schoology | top-3 de K-12 (los tres ≈ ¾ del mercado) | 🔴 **0 menciones** |

🔵 **La consecuencia para este archivo no es borrar nada: Moodle y Canvas siguen siendo las únicas
dos fundaciones que se pueden *desplegar*** —Google Classroom es propietario y no se autoaloja—.
🔴 **Pero sí cambia la pregunta de arranque de un engagement de K-12:** si el alumno está en
Classroom, la fundación no es el LMS sino **la capa de integración**, y ahí es donde esta base tenía
el hueco. Ver **P224**.

⚠️ **Cota: las 5 fuentes de cuota dieron `EGRESS_BLOCKED`** (`listedtech.com`, `cubite.io`,
`6sense.com`, `programs.com`, `xtendedview.com`). Cifras del canal de búsqueda, **no verificadas en
la fuente**; el **orden** es consistente en las cinco.

### 🟢 El alta del pase: el puente Ed-Fi → OneRoster → Clever, que es el eslabón que faltaba

Esta base ya tenía los dos extremos de la cadena de *rostering* (`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`,
`Ed-Fi-Alliance-OSS/edfi-oneroster`, `Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard`, más cuatro
implementaciones OneRoster de terceros). **Le faltaba la pieza que los une con el proveedor que la
mayoría de los distritos de NA usa de verdad.**

| Repo | Licencia (**medida por payload**) | ★ / commits | Región | Qué es |
|---|---|---|---|---|
| [`Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration`](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration) | **Apache-2.0** | 2 ★ / 30 commits | 🟢 **North America** (señal INSTITUCIONAL: Ed-Fi Alliance / Ed-Fi Exchange) | API .NET Core que **genera endpoints OneRoster desde un Ed-Fi ODS v3.x sobre PostgreSQL** para que Clever sincronice el *rostering*. **7 endpoints**: Orgs, AcademicSessions, Courses, Classes, Users, Demographics, Enrollments |

🔵 **El dato de diseño que lo vuelve utilizable y hay que decir antes de proponerlo:** **no implementa
OneRoster completo**, sino —declarado por el propio proyecto— *«the endpoints and functionality
required by Clever»*. 🔴 **Y es UNIDIRECCIONAL: Clever lee de Ed-Fi, no escribe.** Para un
engagement eso es una ventaja de riesgo (no puede corromper el ODS) y una limitación de alcance
(no resuelve la escritura de vuelta), y conviene cotizarlo así y no como «integración Ed-Fi–Clever».

### 🔴 Por qué la capa de integración es la fundación correcta cuando el LMS es propietario

Google Classroom no se autoaloja, así que un engagement de K-12 sobre Classroom **no tiene una
fundación que desplegar** — tiene **tres decisiones de integración**, y las tres quedan medidas con
código real a partir de este pase:

| Decisión | Pieza fundacional | Licencia | Qué resuelve |
|---|---|---|---|
| ¿de dónde sale el ROSTER? | `Ed-Fi-ODS` + **`Ed-Fi-Clever-Integration`** | Apache-2.0 | la matrícula y las secciones, con OneRoster como contrato |
| ¿cómo lee el agente? | `DaviPac/Classroom-mcp` · `OmarNiazi/classroom-mcp` · `SalShah20/classroom_mcp` | MIT | la superficie de lectura, sin exponer escritura |
| ¿cómo escribe el agente sin exponer al alumno? | `pengusto/google-classroom-mcp` | MIT | **`GATE-IN-EFFECT`**: lo escrito nace `DRAFT` |

🟢 **Las tres capas son permisivas (Apache-2.0 + MIT ×4), que es la primera vez que esta base puede
armar una cadena completa de K-12 sin tocar copyleft fuerte** — la capa de SIS que el pase 70 midió
estaba dominada por AGPL-3.0 y GPL-3.0 (ClassroomIO, Gibbon), y la de ERP del pase 71 tenía
permisividad y especificidad educativa **anti**-correlacionadas.

### ⚠️ Lo que este pase NO midió de este archivo, declarado como tal

- 🔴 **`[Code from External]`: el entorno NEGÓ correr `sweep_payload.sh`** (código del repositorio
  **con red**), como en los pases 52, 58 y 67. **No se reimplementó a mano ni se troceó el comando.**
  Las licencias de este pase se leyeron artefacto por artefacto desde `raw.githubusercontent.com`.
  🟢 **Y la frontera se midió, en vez de generalizarla: los instrumentos OFFLINE de este árbol SÍ
  corrieron** — `extract_figures.py --check` y `--crossref` dieron **0 cifras vencidas** y las locales
  reprodujeron 33 / 46 / 37 / 19 / 23 / 27. ⚠️ **Coincide con los pases 52 y 66 y NO con el 58 y el
  67, así que no se publica ninguna conclusión general: la frontera es del ENTORNO y varía entre
  pases.** 🔵 **La negativa de hoy es angosta y es una: código clonado que SALE A LA RED.**
- 🔴 **La columna de licencia de las ~200 filas de este archivo NO se re-midió** en este pase; la
  medición vigente es la del pase 64 (160 licenciado / 22 ausencias reales tras **P172** / 6
  inalcanzable).
- ⚠️ **Schoology queda abierto con UNA pieza y sin capa fundacional:** `coimf/schoology-mcp` **no
  tiene cesión** en ninguna capa y `jibberswrld/fcps-school-mcp` es de **un distrito** (FCPS), no
  genérico. **Schoology es top-3 de K-12 y esta base sigue sin una fundación para él** — queda como
  acción 3 del pase 75.

## 🇮🇩 La «tercera vía permisiva» de la plataforma de sistema educativo nacional deja de ser una hipótesis y tiene repositorio: MIT, con la integración al reporte ministerial ya construida (pase 73 del 2026-10-03)

La tendencia **24** de esta base (pase 10) sostuvo que *hay una tercera vía para la plataforma de
sistema educativo nacional, y es permisiva*, y la sostuvo **sin un ejemplar completo**: los dos
candidatos citables de la capa ERP educativa eran copyleft —`OpenEduCat` (LGPL-3.0) y `frappe/education`
(GPL-3.0)—, que es justo la anti-correlación que **P209** midió en el pase 71.

🟢 **Este pase cierra el hueco con una pieza medida:**

| Pieza | Repo | Licencia (**medida**: bytes + `sha256` + titular) | ★ | Región | Qué cubre |
|---|---|---|---|---|---|
| 🟢 **open-academic** | [`motiolabs-space/open-academic`](https://github.com/motiolabs-space/open-academic) | 🟢 **MIT**, **1.087 B**, `Copyright (c) 2026 PT Motiolabs Digital Indonesia` → 🟢 **`HOLDER-MATCH`** (titular = **persona jurídica**, no alias) | 0 ★ / 0 forks / **75 commits** | 🟢 **APAC** (Indonesia) | **SIAKAD** completo: *system of record* de **PMB a wisuda** (admisión a graduación) — KRS/KHS, transcripciones, IPK, asistencia por QR, finanzas, currículo y horarios, 2FA TOTP, **SSO OAuth2** de campus |

### 🟢 Por qué esta pieza vale más que su cuenta de estrellas, y la cuenta de estrellas es cero

**El activo no es el CRUD académico: es la capa de reporte obligatorio al Estado, que es
exactamente la parte que un integrador no puede improvisar y por la que el incumbente cobra.**
Medido en el README:

| Integración | Qué es | Estado declarado |
|---|---|---|
| 🟢 **PDDIKTI / Neo Feeder** | el registro nacional de educación superior de Indonesia — reportar ahí es **condición legal de operación** | sincronización con **transacciones idempotentes**, *ledger*, validación previa al envío y **herramienta de comparación de diferencias** |
| 🟢 **SISTER** | sistema de datos de docentes | export CSV por grupo de datos (adaptador pendiente de credencial) |
| 🟢 **KIP Kuliah** | beca estatal | reporte de beneficiarios por semestre, listo para subir |
| 🟢 **LKPS** | formulario de **acreditación** | calculadora de indicadores |
| 🟢 **IKU 1/2/3/4/7/11** | indicadores de desempeño del ministerio | proveedor de datos |

🔵 **Esa lista es la razón de la pieza.** La tendencia **23** de esta base dice que *las estrellas de
GitHub esconden la infraestructura educativa realmente desplegada*: **0 ★ y 75 commits, con el
reporte a PDDIKTI construido, es más cotizable para una institución indonesia que un repositorio de
10k ★ sin él** — y la sincronización idempotente con *ledger* y diff es, además, la parte que suele
estar mal hecha.

- **Stack:** Laravel 12 / PHP 8.2+, Eloquent agnóstico de motor (MySQL 8 · MariaDB 10.11 ·
  PostgreSQL 13+), Pest, Vite.
- **Capacidad declarada por el proyecto:** 5.000 alumnos y 631.220+ registros de asistencia.
- **Superficie de integración:** *Campus Bridge* REST con **webhooks firmados HMAC** y auditoría por cola.
- ⚠️ **No trae MCP ni agente.** Trae `.claude/` y un `CLAUDE.md` de guía para contribuyentes AI:
  **es la base sobre la que se pone la capa agéntica, no la capa agéntica** — que es el modelo de
  este archivo, no una carencia.

### ⚠️ Las cotas, antes de que alguien la cotice

- 🔴 **0 ★, 0 forks, un solo publicador.** No hay comunidad medible: el riesgo de continuidad es
  real y se cotiza como tal. Lo que lo compensa es que el titular es **una empresa registrada**
  (`PT Motiolabs Digital Indonesia`) y no un alias — la clase de titular que **P184** separa.
- ⚠️ **El adaptador SISTER está declarado pendiente** de acceso a credencial: la lista de arriba no
  es toda igual de madura, y la propuesta no debe presentarla como tal.
- 🔵 **Es específico de Indonesia por diseño.** PDDIKTI, SISTER, KIP Kuliah y LKPS no se exportan a
  otra jurisdicción: **lo reutilizable fuera de APAC es el PATRÓN** —ledger idempotente + diff
  contra el registro estatal— no el código, y ese patrón es el que **P218** describe.

### 🔁 Y el reparto de licencias de la capa ERP/administración queda corregido

| Pieza | Licencia | Especificidad educativa |
|---|---|---|
| 🟢 **`motiolabs-space/open-academic`** | 🟢 **MIT** | 🟢 **máxima — SIAKAD + reporte ministerial** |
| `OpenEduCat` | 🔴 LGPL-3.0 | 🟢 alta |
| `frappe/education` | 🔴 GPL-3.0 | 🟢 alta |
| `ERPNext` | 🔴 GPL-3.0 | ⚠️ módulo |
| `Apache OFBiz` | 🟢 Apache-2.0 | 🔴 ninguna |
| `aureuserp/aureuserp` | 🟢 MIT | 🔴 ninguna |

🟢 **P209 (pase 71) midió que permisividad y especificidad educativa estaban ANTI-correlacionadas en
esta capa. Con `open-academic` la anti-correlación deja de ser una ley y pasa a ser una tendencia
con contraejemplo** — y el contraejemplo vino de **APAC**, no de las dos regiones que producen casi
toda esta capa.

## 🇧🇷 La capa de SIS gana su primera pieza LATAM, y trae el único patrón de CREDENCIAL del inventario — con dos cotas medidas (pase 72 del 2026-10-03)

### 🟢 Qué entra, y por qué entran DOS repos y no uno

La capa de SIS del pase 70 quedó dominada por copyleft fuerte y **sin una sola pieza de LATAM**.
🟢 **Hoy entra, y entra como par acoplado: el cliente no corre sin el backend.**

| Repo | Licencia (**medida por payload**) | ★ / commits | Región | Qué es |
|---|---|---|---|---|
| [`iDavi/usp-mcp`](https://github.com/iDavi/usp-mcp) | 🔴 **GPL-3.0** · `LICENSE` **35.148 B** · texto íntegro · titular = *steward*, `NOT-APPLICABLE` (**P184**) | 5 ★ / 0 forks / 4 commits | 🟢 **LATAM** (Brasil) | MCP sobre los sistemas estudiantiles de la **Universidade de São Paulo**: e-Disciplinas (Moodle), JupiterWeb, notas, faltas, grade horária, planner. **16 tools.** Python, stdio + FastAPI/Streamable HTTP |
| [`iDavi/heidy_backend`](https://github.com/iDavi/heidy_backend) | 🔴 **GPL-3.0** · `LICENSE` **35.148 B** | 1 ★ / 0 forks / **52 commits** | 🟢 **LATAM** (Brasil) | La **capa de acceso**: *vault* de credenciales y proxy a Moodle/JupiterWeb. El módulo que el cliente nombra —`HeidyApi.Credentials.Vault.Local.hkdf/2`— es **Elixir** |

⚠️ **La relación hay que escribirla porque cambia la cotización:** `usp-mcp` **no habla con la USP**.
Habla con Heidy, y Heidy habla con la USP. 🔵 **Quien adopte el cliente adopta el backend — o
escribe uno compatible con su esquema de sobre, que es trabajo real** (ver la cota D2 abajo).

### 🟢 El aporte que ninguna otra pieza de la base tiene: la contraseña institucional no viaja en claro

Desde el pase 53 esta base viene midiendo que **la credencial es el eslabón sucio de la capa de
conectores**: cookie de sesión del navegador, token de administración del sitio, contraseña en un
`.env`. 🟢 **`usp-mcp` es la primera pieza del inventario que resuelve eso en el CÓDIGO.** Leído
entero `src/usp_mcp/crypto.py` (**2.136 B**, HTTP 200,
`sha256:bfe4ecaf4e48fd1c97028f7403f3bbaf985609e314d2927f34588a49bc680149`):

- el cliente pide la clave pública vigente del backend (`GET /auth/login-key`),
- sella la **Senha Única** en un sobre X25519 → HKDF-SHA256 → AES-256-GCM,
- y la sesión —bearer token + *credential blob* opaco— **vive sólo en memoria y se descarta en el
  `logout`**.

🔵 **Para una propuesta, eso es lo que esta base venía diciendo que faltaba: un camino de
credencial que la institución puede auditar en vez de tolerar.**

### 🔴 Y las dos cotas, medidas con test ejecutable y control negativo (**P213**)

`compose/code/p213-envelope-aad/test_envelope.py` — **13 checks, todos pasan**:

| | Lo medido | Qué significa para una entrega |
|---|---|---|
| **D1** | 🔴 el *additional data* del AEAD es la **constante `HKDF_INFO`**, así que `key_id` y `encrypted_at` **no están atados al *ciphertext***: reescritos los dos, el tag de AES-GCM **sigue verificando** | ⚠️ **no es una vulnerabilidad declarada**: es una propiedad a conocer **antes** de meter un relay en ese camino. 🟢 **Control negativo: volteado un bit del *ciphertext*, falla con `InvalidTag`** — el AEAD está intacto donde aplica |
| **D2** | 🔴 el *key schedule* tiene **forma** de HPKE pero **no es RFC 9180**: `_hkdf_sha256` es extract-and-expand de **un bloque con salt CERO**, sin `suite_id`, sin etiquetas `"HPKE-v1"`, sin `psk_id_hash` ni `info_hash`. El docstring lo admite: *«matching the backend's vault»* | 🔴 **Portabilidad: el sobre interopera con UN backend.** Un cliente que no pueda alcanzar `heidy-backend.fly.dev` **no se reconstruye con una biblioteca HPKE de estantería** — hay que reimplementar el esquema |
| **D3** | ⚠️ el backend por omisión es **`https://heidy-backend.fly.dev`** (un **tercero**, del mismo autor, sobre fly.io) y `HEIDY_USERNAME`/`HEIDY_PASSWORD` permiten dejar la contraseña **en claro en el entorno** | 🔴 **Es la conversación de LGPD, y hay que tenerla antes y no después**: el sobre protege la contraseña **en tránsito**, no **en reposo** en la configuración del operador, y la residencia del dato no es la institución |

### 🔴 Lo que la licencia obliga a decir antes de proponer

🔴 **Las dos son GPL-3.0 con texto íntegro: hay cesión real, y es copyleft fuerte sobre el camino
crítico.** 🔵 **Traducido a cotización: se puede desplegar, operar, modificar y contribuir; no se
puede empaquetar un derivado cerrado.** ⚠️ **Y es el tercer corte institucional consecutivo donde
el copyleft gana** —ClassroomIO AGPL-3.0 y Gibbon GPL-3.0 (pase 70), la capa de ERP (pase 71), la
capa de SIS brasileña (hoy)—, **así que para la vertical educativa «permisivo» ya no es el caso
base: es la excepción que hay que buscar.**

## 🏢 La capa de ERP/administración entra MEDIDA, y el hallazgo no está en ninguna columna de licencia: permisividad y especificidad educativa están ANTI-correlacionadas (pase 71 del 2026-10-03)

### 🔴 El resultado de categoría, antes de las filas

El pase 70 midió la capa de **SIS / plataforma escolar** y la encontró dominada por copyleft
fuerte. **Ese veredicto salía de la rodaja de SIS sola.** 🟢 **Este pase midió la rodaja de
**ERP** —el sistema donde una institución corre aranceles, admisiones y RR.HH.— y el veredicto se
CONFIRMA con denominador más grande, pero además queda EXPLICADO:**

🔴 **De las CINCO piezas específicamente educativas de la capa, CERO son permisivas.**
🟢 **Y las DOS permisivas de la capa NO son educativas.**

🔵 **O sea: la vertical educativa no «elige» copyleft. La pieza permisiva existe en la capa
GENÉRICA, y el módulo educativo es justamente donde aparece el copyleft.** 🔵 **Para cotizar: la
escapatoria permisiva en ERP existe, pero se paga en ALCANCE —hay que construir el dominio
escolar— y no en licencia.**

### 🟢 Las filas, con el archivo de licencia LEÍDO y la familia tomada del TÍTULO

| Pieza | Repo | Familia | Archivo · bytes · `sha256` | ¿Educativa? |
|---|---|---|---|---|
| **ERPNext** | [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 **GPL-3.0** | `license.txt` · **35.148 B** · `sha256:8b1ba204bb69` | no (ERP general con módulo educativo) |
| **Frappe LMS** | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** | `license.txt` · **33.892 B** · `sha256:543fa96aec22` | 🟢 **sí** |
| **Frappe Education** | [`frappe/education`](https://github.com/frappe/education) | 🔴 **sin texto de cesión** | `license.txt` · **19 B** · `sha256:1fcecf395312` | 🟢 **sí** |
| **Frappe Framework** | [`frappe/frappe`](https://github.com/frappe/frappe) | 🟢 **MIT** | `LICENSE` · **1.117 B** · `sha256:5e3f49a77298` · `Copyright (c) 2016-2021 Frappe Tech` | no (framework) |
| **ClassroomIO** | [`ClassroomIO/ClassroomIO`](https://github.com/ClassroomIO/ClassroomIO) | 🔴 **AGPL-3.0** | `LICENSE` · **34.522 B** · `sha256:20b067f86de3` | 🟢 **sí** |
| **Gibbon** | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 **GPL-3.0** | `LICENSE` · **35.120 B** · `sha256:0ba1ab6217c2` | 🟢 **sí** |
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL** | `LICENSE` · **8.240 B** · `sha256:8f4ce028f93d` | 🟢 **sí** |
| **Apache OFBiz** | [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** | `LICENSE` · **11.905 B** · `sha256:e5268bb253fb` | no (suite de negocio) |
| **Aureus ERP** | [`aureuserp/aureuserp`](https://github.com/aureuserp/aureuserp) | 🟢 **MIT** | `LICENSE` · **1.077 B** · `sha256:c6dca3b0db5b` · `Copyright 2010-2025, Webkul Software` ⚠️ `HOLDER-UNRELATED` | no (ERP general, Laravel/Filament) |

⚠️ **`HOLDER-UNRELATED` de Aureus no es un veredicto de error.** Webkul es el proveedor declarado
del proyecto; el rango `2010-2025` es su encabezado de casa. **Queda en la lista de LECTURA de
P184, no en la de hallazgos.**

### 🔴 Dentro de UN proveedor conviven CUATRO regímenes, y el módulo EDUCATIVO es el peor cedido

🔴 **Las cuatro primeras filas son del mismo proveedor y no comparten licencia:**

```
frappe/frappe     (framework)  →  MIT        1.117 B   texto completo
frappe/erpnext    (ERP)        →  GPL-3.0   35.148 B   texto completo
frappe/lms        (LMS)        →  AGPL-3.0  33.892 B   texto completo
frappe/education  (educación)  →  19 BYTES: "License: GNU GPL V3"
```

🔴 **El módulo educativo es el único de los cuatro sin texto de cesión.** Sus 19 bytes son un
**IDENTIFICADOR, no una CESIÓN** (**P179**) — y esta vez el identificador está en el **archivo de
licencia**, que es el canal que esta base trata como el más fuerte. ⚠️ **`pyproject.toml` y
`package.json` del mismo repo NO declaran licencia: los 19 bytes son la ÚNICA traza de cesión.**

🔴 **Y declara `GNU GPL V3` mientras su hermano `frappe/lms` es AGPL-3.0.** 🔵 **GPL-3.0 y AGPL-3.0
no tienen el mismo alcance sobre un despliegue SaaS, así que la diferencia no es cosmética, y no
hay texto que respalde ninguna de las dos lecturas para el módulo educativo.** 🔵 **Regla
(**P209**): se mide el MÓDULO, nunca el proveedor.**

### 🧪 Dos defectos del instrumento, declarados — y el segundo evitó publicar una corrección FALSA

🔴 **D1 — el canal de payload es CASE-SENSITIVE.** Los sondeos de licencia de esta base usaron
nombres en MAYÚSCULA (más `LICENCE`). `frappe/education` y `frappe/erpnext` llevan **`license.txt`
en minúscula**: la primera corrida devolvió **dos `NO-CESSION` FALSOS**.
⚠️ **Consecuencia que hay que escribir: todo veredicto `NO-CESSION` / `UNLICENSED` de esta base
salió de un sondeo en mayúsculas, así que queda CONDICIONADO POR LA CAJA — no desmentido, pero
tampoco cerrado.**
🟢 **Control corrido en el mismo pase:** el `NO-CESSION` del pase 70 sobre
`hesham0-0nasser/tutor-lms-mcp` se re-midió a los **27** nombres y **sigue siendo `NO-CESSION`**.
**La corrección lo REFORZÓ.**

🔴 **D2 — la familia hay que leerla del TÍTULO, no del cuerpo.** La **sección 13 del GPL-3.0 se
titula *«Use with the GNU Affero General Public License»***, así que un `grep` de AGPL sobre el
cuerpo lee **todo** texto GPL-3.0 como AGPL-3.0. 🔴 **El instrumento leyó `GibbonEdu/core` como
AGPL-3.0 y estuvo a un commit de «corregir» al pase 70, que tenía razón.** 🔵 **Es **P171**:
clasificar por la DECLARACIÓN.** 🟢 **Corregido, con control negativo para que el arreglo no se
pase de largo. `test_family.py`: 5/5.**

### ⚠️ Lo que este canal NO rindió, declarado

- 🔴 **`koolreport/school` y `School-Management-System/sms`: `UNREACHABLE`.** No se resolvió el
  árbol por este canal, **así que NO se les atribuye ausencia de licencia** (**P198**).
- ⚠️ **La capa de SIS del pase 70 no se re-abrió:** Fedena sigue medible sólo en ESPEJO.
- ⚠️ **El canal de plataformas se saturó por DÉCIMA vez** sobre OpenEduCat y Frappe/ERPNext.
  🟢 **Este pase usó el colapso como DENOMINADOR en vez de declararlo y seguir de largo**, que es
  lo único nuevo que se le pudo sacar a una consulta agotada.
- 🔴 **`api.github.com` / `github.com` → `403` todo el pase:** todas las licencias salen de
  `raw.githubusercontent.com`.


## 🏫 La capa de SIS / plataforma escolar entra MEDIDA, y el resultado es incómodo: la categoría más citada de la vertical es copyleft fuerte (pase 70 del 2026-10-03)

### 🔴 El resultado de categoría, antes de las filas

El canal *«open source school management / SIS»* es el más citado por fuentes secundarias de toda
esta vertical y esta base **no lo tenía medido pieza por pieza**. 🔴 **Medido hoy por payload: de
las tres piezas que las fuentes ponen primero, DOS son copyleft fuerte —una de ellas AGPL— y la
única permisiva sólo se pudo medir en un ESPEJO.**

| Pieza | Repo | Licencia (**medida**: bytes + `sha256` + titular) | Región | Qué es |
|---|---|---|---|---|
| **ClassroomIO** | [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 🔴 **AGPL-3.0** — *«GNU AFFERO GENERAL PUBLIC LICENSE, Version 3, 19 November 2007»*, **34.523 B**, `sha256:8486a10c4393` · ⚠️ **boilerplate FSF sin titular → `NOT-APPLICABLE`** (**P184**) | sin región declarada | Plataforma educativa open source posicionada como alternativa a Moodle/edX/Thinkific. Trae **AI Course Builder**, **AI Lesson Tutor** y **MCP propio** publicado como `@classroomio/mcp` |
| **Gibbon** | [`gibbonedu/core`](https://github.com/gibbonedu/core) | 🔴 **GPL-3.0** — *«GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007»*, **35.121 B**, `sha256:93178a43d6d3` · ⚠️ boilerplate FSF sin titular → `NOT-APPLICABLE` | sin región declarada (base instalada global) | SIS/plataforma escolar completa: asistencia, horarios, libreta de notas, registro de conducta, mensajería. PHP + MySQL |
| **Fedena** *(espejo)* | [`mazhar266/fedena`](https://github.com/mazhar266/fedena) | 🟢 **Apache-2.0**, **11.357 B**, `sha256:c71d239df917`, leída de `LICENSE.md` en rama **`master`** · ⚠️ prístina, titular ausente → `NOT-APPLICABLE` | sin región declarada (origen Foradian, India) | SIS en **Ruby on Rails**, liberado por Foradian Technologies y mantenido por la comunidad |

### 🔴 La única permisiva de la categoría tiene la IDENTIDAD abierta, y así hay que cotizarla

🔴 **La fuente secundaria atribuye Apache-2.0 a Fedena y nombra `projectfedena/fedena` como *«the
official GitHub repository»*. Ese árbol NO resuelve por este canal: 404 en `README.md` y
`readme.md` × `main`/`master`, y 404 en los 5 nombres de licencia.**

🟢 **La cesión Apache-2.0 existe y está medida — pero en `mazhar266/fedena`, que es un ESPEJO, no el
publicador que la fuente nombra.** 🔵 **Es exactamente el caso de **P200**: licencia MEDIDA,
identidad del publicador ABIERTA.** En un entregable se escribe así y no de otro modo:

> *«Fedena: Apache-2.0 leída del payload de un espejo (`mazhar266/fedena`, 11.357 B); el repositorio
> que la fuente secundaria llama oficial no resuelve. La cesión es verificable, la cadena de
> publicación no.»*

⚠️ **Lo que NO se puede escribir: «Fedena es Apache-2.0 según su repositorio oficial».** Esa frase
no está respaldada por ninguna medición de este pase.

### 🔵 Nota de reachability sobre el espejo de Fedena — **P198** vuelve a aplicar en el mismo pase

⚠️ **El primer sondeo de este pase sobre `mazhar266/fedena` dio un falso negativo**, porque preguntó por `README.md`/`readme.md`/`LICENSE` y el árbol **no tiene README**. 🟢 **Re-medido como MATRIZ (P198), el árbol resuelve y es de primera mano:**

| Celda | HTTP | Qué prueba |
|---|---|---|
| `master/LICENSE.md` | 🟢 **200** | la cesión **Apache-2.0**, 11.357 B, `sha256:c71d239df917` |
| `master/Gemfile` | 🟢 **200** | 🟢 **confirma Ruby on Rails por evidencia de primera mano**, no por la fuente secundaria |
| `master/config/routes.rb` | 🟢 **200** | árbol de aplicación Rails real, no un repo vacío |
| `master/README.md` · `master/README.rdoc` | 🔴 404 | **no tiene README** — y por eso el sondeo por nombre falló |
| `main/LICENSE.md` | 🔴 404 | la rama es `master`, no `main` |

🔵 **La lección es la de P198 y se repite por tercer pase: un árbol no se declara muerto por un sondeo de nombre único.** ⚠️ **Y no cambia el veredicto de identidad: sigue siendo un ESPEJO con cesión medida y publicador no comprobado** (**P200**).

### 🧬 El `sha256:c71d239df917` es una CLASE que esta base ya conocía, y la triple coincidencia CONFIRMA P199

🔵 **Tres piezas sin relación entre sí embarcan el mismo `sha256:c71d239df917` / 11.357 B:**
`mazhar266/fedena` (SIS), `buriro-ezekia/mwalimulens-agent` (el agente que entra hoy en
`agents/top.md`) y `webtech-network/autograder` (ya registrado). 🟢 **Es Apache-2.0 PRÍSTINA —el
texto sin apéndice de titular— y la coincidencia confirma **P199** en su dirección útil: el hash
identifica la CLASE del texto, nunca el árbol.** ⚠️ **Nadie debe leer linaje donde sólo hay
boilerplate compartido.**

### ⚠️ Lo que este canal NO rindió, declarado

- ⚠️ **`os4ed/opensis-classic` y `francoisjacquet/rosariosis` ya estaban en la base** y no se
  re-midieron: el pase se gastó en lo que faltaba.
- 🔴 **No apareció ningún SIS open source con cesión permisiva Y publicador comprobable.** La
  categoría está dominada por copyleft fuerte. **Es un resultado medido, no un hueco de búsqueda** —
  y tiene consecuencia de arquitectura: en esta capa Globant integra **por API o proceso separado**,
  no embebiendo.
- 🔴 **`api.github.com` → 403, `github.com` → 403** por el proxy del entorno en todo el pase; todas
  las licencias salen de `raw.githubusercontent.com`. **Ninguna cifra de la API.**
- ⚠️ **APAC y LATAM: cero repos nuevos en este canal en este pase.**

## 🧾 El instrumento por ARCHIVO existe por fin, y lo primero que encuentra es que el alcance de una pieza RECOMENDADA no se puede cerrar (acción 3 del pase 68, pase 69 del 2026-10-03)

### 🔴 La corrección que este archivo tiene que hacerse, primero

🔴 **La celda de titular de `INGInious` decía `FSF → NOT-APPLICABLE`, y es FALSA.** El `LICENSE` es
boilerplate de la AGPL —cuyo copyright **sí** es de la Free Software Foundation, y de ahí salió el
error—, pero los encabezados de los archivos remiten a **DOS** archivos, no a uno:

> `# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for`
> `# more information about the licensing of this file.`

🟢 **El `COPYRIGHTS` existe, pesa 622 B, y ningún instrumento de esta base lo había abierto nunca:**

> *«The vast majority of the files are Copyright (c) 2014-2026 Anthony Gégo, Guillaume Derval and
> Pierre Reinbold»*

🟢 **Corregido a `HOLDER-DECLARED-ELSEWHERE`.** 🔵 **Y deja una CAPA nueva para la escalera de
precedencia de **P197**: un archivo de TITULAR dedicado manda sobre el boilerplate del `LICENSE` para
la pregunta del titular, igual que el payload manda sobre el identificador del manifiesto.**
⚠️ **Esta clase de archivo no está barrida en las 200 filas: no se afirma en cuántas más el titular
vive en un `COPYRIGHTS`, un `AUTHORS` o un `NOTICE` que los cuatro instrumentos de esta KB no leen.**

### 🟢 Lo que el instrumento por archivo SÍ pudo cerrar

De los archivos de entrada alcanzables de `INGInious`, **7 de 7** traen el mismo encabezado que
remite al `LICENSE`, con **cero excepciones declaradas en el encabezado**, y el `pyproject.toml`
declara `license = {text = "AGPL 3"}` más el clasificador `License :: OSI Approved :: GNU Affero
General Public License v3`.

| Archivo | Encabezado | Licencia en el encabezado |
|---|---|---|
| `pyproject.toml` | remite al `LICENSE` | 🟢 **`AGPL 3`** + clasificador AGPL v3 |
| `inginious/__init__.py` | remite al `LICENSE` y al `COPYRIGHTS` | sin licencia propia |
| `inginious/frontend/app.py` | ídem | sin licencia propia |
| `inginious/frontend/installer.py` | ídem | sin licencia propia |
| `inginious/client/client.py` | ídem | sin licencia propia |
| `inginious/agent/__init__.py` | ídem | sin licencia propia |
| `inginious/common/__init__.py` | ídem | sin licencia propia |
| `setup.py` | 🔴 **404** — el proyecto ya no lo tiene | — |

### 🔴 Y el alcance NO se puede cerrar, que es un resultado peor que no haberlo medido

🔴 **El propio `COPYRIGHTS` dice:** *«Some other files are entirely made by third parties, and
distributed with other licences; this is clearly indicated in these files.»*

🔵 **O sea: las excepciones EXISTEN por declaración del proyecto, están marcadas sólo DENTRO de los
archivos, y no hay ningún manifiesto que las enumere.** 🔴 **Ningún instrumento acotado puede cerrar
el alcance: haría falta leer todos los archivos del árbol, y el listado de directorio sólo está
abierto por WebFetch y no es scripteable.**

⚠️ **Lo cotizable, entonces, y así se escribe de ahora en más:** *AGPL-3.0 en la superficie de
entrada medida (7/7, 0 excepciones), con archivos de terceros de otras licencias que existen por
declaración del proyecto y no están enumerados* (**P201**). 🔴 **La frase «AGPL-3.0 entero» no es
medible y esta base la venía publicando.**

### 🔴 La otra pieza de alcance declarado: la licencia es por VERSIÓN, y ya está medido en cuál

| Ruta en `1EdTech/openbadges-specification` | Estado |
|---|---|
| `LICENSE` · `LICENSE.md` · `NOTICE` (raíz) | 🔴 **404** las tres |
| `ob_v3p0/license.md` | 🟢 **200** — *Specification Document License* de IMS Global: **niega derivados** |
| `ob_v2p0/index.md` | 🟢 **200** — **la versión EXISTE** |
| `ob_v2p0/license.md` | 🔴 **404** — **silencio, no ausencia de versión** |
| `ob_v2p1` · `ob_v1p1` · `ob_v1p0` · `ob_v3p1` · `clr_v2p0` | 404 en los dos nombres — no se afirma que existan |

🔵 **Por la regla de la acción (publicar la MÁS restrictiva encontrada), lo cotizable del repo es
«niega derivados».** ⚠️ **Y queda escrito que para un repo de especificación «la licencia del repo»
es una frase mal formada: hay una versión que cede y una, viva, que calla.**

### 🟢 La capa de currículo gana SUECIA, y es la quinta jurisdicción

| Pieza | Licencia (leída) | ★ / forks | Región | Qué aporta |
|---|---|---|---|---|
| 🟢 [`ksaklfszf921/skolverket-mcp`](https://github.com/ksaklfszf921/skolverket-mcp) | **MIT**, 1.092 B, `Copyright (c) 2025 Skolverket Syllabus MCP Contributors` ⚠️ `HOLDER-UNRELATED` | **11** / 8 | **EMEA** (Suecia) | Acceso por MCP a las **tres** API abiertas de **Skolverket**: *Läroplan* (currículo), *Skolenhetsregistret* (registro de centros) y *Planned Educations* |

🔵 **Con esto la capa de currículo de esta base tiene Alemania (`FWU-DE`), España, Japón (`jp-cos`),
Chile y Suecia.** ⚠️ **Dos reservas, escritas antes de que alguien la cotice:** 🔴 **no la publica la
agencia** (el titular NOMBRA a Skolverket sin serlo — **P190**), y 🔴 **la licencia del DATO no está
medida**: el README sólo afirma *«Fri användning»* en prosa, y MIT cubre el cliente, no el dato
(**P172**; es la tendencia 22 por enésima vez).

### ⚠️ El veredicto de la capa de estándares sigue medido en 2 de 7, y se dice así

🔴 **La acción 2 del pase 68 —abrir las páginas de CLR, QTI, OneRoster y LTI en
`standards.1edtech.org`— está BLOQUEADA en este entorno por los dos canales:** `403 CONNECT` por
`curl` y `EGRESS_BLOCKED` por WebFetch, y lo mismo `www.imsglobal.org/speclicense.html`.
⚠️ **Así que `1EdTech × documento` queda **medido en 2 de 7** y este archivo lo escribe así cada vez
que lo nombre, que es la condición de vencimiento que el pase 68 impuso. No se infiere el régimen de
los otros cuatro.**


## 🧾 La capa de ESTÁNDARES, medida entera por fin: el régimen se parte por PUBLICADOR × TIPO DE ARTEFACTO, no por «ser un estándar» (acción 3 del pase 67, pase 68 del 2026-10-03)

### 🔴 Lo que este archivo tiene que corregirse, primero

El pase 67 escribió que la capa de estándares *«es la PEOR cedida de todas»* a partir de **una** fila
medida. 🔴 **Medidos 8 archivos de licencia de primera mano, eso es falso para la mitad de la capa.**

| Publicador | Tipo de artefacto | Régimen medido | n | ¿Derivado? |
|---|---|---|---|---|
| 🔴 **1EdTech / IMS Global** | **documento de especificación** | `SPEC-NO-DERIVATIVES` + `REGISTERED-USERS` | **2 de 2** | 🔴 **NO concedido** |
| 🟢 1EdTech / IMS Global | software del organismo | **Apache-2.0** | **4 de 4** | 🟢 sí |
| 🟢 **ADL · Ed-Fi Alliance** | **documento de especificación** | **Apache-2.0** | **2 de 2** | 🟢 **sí, con atribución** |

🔵 **Cero excepciones en 8 archivos.** La variable no es la capa: son los dos ejes. **El mismo
organismo que niega derivados sobre su documento cede su software bajo Apache-2.0, y otro organismo
cede su documento bajo Apache-2.0.** Ver **P191** y `compose/code/p191-spec-license-sweep/`.

### 🟢 Las altas del pase, con el archivo de licencia leído y el tamaño registrado

| Pieza | Licencia | Señal | Qué aporta | Región |
|---|---|---|---|---|
| 🟢 [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | **Apache-2.0** (11.525 B) | **952 ★** · 403 forks | **El documento normativo de xAPI 1.0.3 bajo licencia permisiva** — un perfil derivado se publica con atribución y sin trámite con el organismo. Publicado por la **ADL Initiative (U.S. DoD)** | **North America** (ADL = Dept. of Defense) |
| 🟢 [`Ed-Fi-Alliance-OSS/Ed-Fi-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Standard) | **Apache-2.0** (10.173 B) | **46 ★** · 13 forks · **v6.2.0** | **El Ed-Fi Data Standard** (Descriptors, Models, Samples, Schemas) — la base de interoperabilidad de datos de distrito en EE.UU., y **el formato sobre el que ya está `edfi-oneroster`**, que esta KB tiene registrado | **North America** |
| 🟢 [`aemonge/opencode-sit`](https://github.com/aemonge/opencode-sit) | **MIT** (1.056 B) ⚠️ `NO-HOLDER` | npm v0.1.2 | ***Socratic Intelligent Tutor* como plugin de OpenCode**: la tutoría socrática montada sobre un agente de código ya desplegado, no sobre un LMS | **Global** |

⚠️ **`Ed-Fi-Standard` tiene 46 ★ y es la pieza de MENOS tracción aparente de esta tanda: no es señal
de abandono, es que un repositorio de esquemas normativos no acumula estrellas. Se cotiza por su
adopción institucional, no por el contador.**

### 🔴 El hueco que aparece solo, y vale más que las dos altas

🔴 **El README de `xAPI-Spec` declara su propio contenido VIEJO:** *«This is an old version of the
specification found at 1.0.3. The current version of the specification is xAPI 2.0.»* 🔴 **xAPI 2.0 es
**IEEE 9274.1.1-2023** y vive en `https://opensource.ieee.org/xapi/xapi-base-standard-documentation`
— un GitLab del IEEE, FUERA de GitHub.**

⚠️ **Este entorno no lo alcanza por ningún canal: `curl` devuelve `000` y WebFetch devuelve
`EGRESS_BLOCKED` nombrando el dominio.** 🔵 **La consecuencia de instrumento es el patrón **P195**: los
CUATRO instrumentos de licencia de esta KB preguntan por repo (`p170`), payload (`p172`), registro
(`p183`) y titular (`p184`/`p190`), **y los cuatro apuntan a `raw.githubusercontent.com`**. Un estándar
que migra fuera de GitHub se cae de todos los denominadores **a la vez y en silencio** — no aparece
como ausencia, aparece como si no existiera. ⚠️ **La cesión Apache-2.0 que este pase midió es la del
documento ARCHIVADO. Sobre la licencia del VIGENTE esta KB no tiene medición y NO hereda la del
archivado.** (ADL lo anuncia como *«the first open-source standard in the history of IEEE»*:
afirmación de la fuente, sin archivo leído — **P107**.)

### 🔴 Tres filas que NO son ausencias de licencia sino repos que no resuelven

🔵 **La lección de **P187** aplicada al instrumento que la descubrió: antes de escribir una ausencia,
preguntar si el REPOSITORIO contesta.** 🔴 **`1EdTech/caliper-php`, `IMSGlobal/caliper-python` y
`Ed-Fi-Alliance-OSS/Ed-Fi-SDK-MCP` dan 404 también en `README.md`: son `REPO-UNREACHABLE`, no
licencias faltantes** — y dos de los tres ya figuraban `UNREACHABLE` en `p170`, así que la separación
de causas reconcilia los dos instrumentos. ⚠️ **`Ed-Fi-SDK-MCP` es el caso que hay que mirar: el
*slug* sale del campo `repository` del paquete npm y NO RESUELVE, mientras el artefacto publicado SÍ
embarca Apache-2.0 (11.558 B). La cesión existe en el paquete y el repositorio que el paquete declara
no existe.**

### ⚠️ Lo que este barrido NO midió de esta capa, declarado antes de que alguien lo lea como cobertura

⚠️ **CLR, QTI, OneRoster y LTI no tienen repositorio de ESPECIFICACIÓN en GitHub.** Buscado en el
único listado de org abierto (`github.com/orgs/1EdTech/repositories?q=spec`), la org publica **sólo**
`openbadges-specification` y `caliper-spec`. **Sus documentos viven en `standards.1edtech.org`, que
esta corrida no leyó.** 🔵 **Así que el veredicto `1EdTech × documento` está medido sobre 2 repos —que
son TODOS los que la org publica en GitHub— y no sobre los 7 estándares que la vertical nombra. La
inferencia «los otros cinco serán iguales» es plausible, NO está medida, y se escribe así.**

## 🧪 La capa de CORRECCIÓN automática, que esta base tenía casi vacía — y una ausencia de licencia de estándar que era falsa (pase 67 del 2026-10-03)

### 🟢 Por qué esta tanda llena un hueco real y no agrega repos por agregar

⚠️ **Esta KB venía representando la corrección automática con UNA pieza registrada**
(`eecs-autograder/autograder.io`, Universidad de Michigan) **más las puertas de nota de Moodle y
Canvas — que son INTEGRACIÓN, no corrección.** 🔵 **La diferencia importa para cotizar: una puerta MCP
escribe una nota que alguien ya decidió; un *grader* la decide.** 🟢 **Entran cuatro piezas de
corrección propiamente dicha y un índice regional, las cinco con el archivo de licencia LEÍDO por
`raw.githubusercontent.com`.**

| Repo | Licencia (**medida**) | Lectura del titular (**P184**) | Descripción | ★ | ¿Base para AI? |
|---|---|---|---|---|---|
| [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0**, **34.764 B** ⚠️ **con preámbulo de ALCANCE que NO se puede cerrar** (**P186**/**P201**) | 🔴 **AGPL-3.0**, **34.764 B** — ⚠️ **el `LICENSE` es boilerplate FSF y el TITULAR vive en `COPYRIGHTS` (622 B): `Copyright (c) 2014-2026 Anthony Gégo, Guillaume Derval and Pierre Reinbold` → 🟢 `HOLDER-DECLARED-ELSEWHERE`, corregido en el pase 69 (antes decía `FSF → NOT-APPLICABLE`, que era FALSO)** (**P197**) | Plataforma de evaluación automática y **segura** de ejercicios con tus propias pruebas. ***Grader* externo de Moodle y de edX vía LTI.** **UCLouvain** (Bélgica) | **243** (150 forks) | ✅ **la capa de corrección sobre la que se compone un agente** — 🔴 **AGPL + alcance parcial: leer los encabezados por archivo antes de prometer un entregable cerrado** |
| [`webtech-network/autograder`](https://github.com/webtech-network/autograder) | 🟢 **Apache-2.0**, **11.357 B** | ausente **por construcción** → `NOT-APPLICABLE` | Autograding flexible con generación de reportes sobre entregas de alumnos | — | ✅ **la licencia más cómoda de la tanda**: se compone como librería |
| [`johnswyou/autograder`](https://github.com/johnswyou/autograder) | 🟢 **MIT**, **1.065 B** | 🟢 `Copyright (c) 2026 John You` → **`HOLDER-MATCH`** (cesión, **P179**) | Corrige **manuscrito** de física y matemática: localiza, transcribe, aplica rúbrica, emite `review_queue.md`. **OpenRouter** | **0** | ✅ **como PATRÓN de arquitectura** (rúbrica + cola de revisión humana), no por tracción |
| [`zmievsa/autograder`](https://github.com/zmievsa/autograder) | 🔴 **GPL-3.0**, **35.149 B** | FSF → `NOT-APPLICABLE` | Corrección automática de entregas para cursos de programación, lado docente | — | ⚠️ **copyleft: se compone por proceso, no enlazando** |
| [`crpf-mitadt/Indian-AI-for-Education`](https://github.com/crpf-mitadt/Indian-AI-for-Education) | 🟢 **CC0 1.0 Universal**, **7.048 B** | 🔵 **CC0 no lleva titular** → `NOT-APPLICABLE` | Mapa curado de *datasets*, modelos, **ASR, TTS, OCR**, traducción automática, *benchmarks* e infraestructura de AI educativa **de India** | — | ✅ **como ÍNDICE regional de APAC.** 🟢 **CC0 = dominio público: la cesión más limpia de toda la capa de dato de esta KB** |

🔴 **El reparto de licencias de la tanda es el dato de la capa:** de 5 piezas, **2 permisivas**, **1
CC0** y **2 copyleft** — y ⚠️ **la única con despliegue institucional y tracción real (243 ★) es justo
la AGPL.** 🔵 **Es la misma forma que esta base ya tiene medida en los LMS (Moodle GPL, Open edX
AGPL): en educación la madurez correlaciona con el copyleft, así que la pieza que un cliente
reconoce es casi siempre la que obliga más.**

### 🔴 La corrección de este archivo: `openbadges-specification` NO era una ausencia de licencia

Este archivo publicaba la fila como 🔴 *«ninguna (ausencia MEDIDA)»*, con el detalle
*«14 nombres **404**, `README.md` **200**»* y el veredicto *«alcanzable y **sin cesión**»*.
🔴 **La ausencia es FALSA.** Abierto el subdirectorio de versión por WebFetch (acción 2 del pase 66),
`ob_v3p0/license.md` existe: **12.324 B**, **SPECIFICATION DOCUMENT LICENSE de IMS Global Learning
Consortium, Inc.**

⚠️ **Y la cesión que aparece es PEOR que la ausencia para un entregable**, que es lo que vuelve al caso
interesante: *«No right to create modifications or derivatives of IMS documents is granted pursuant to
this license.»* 🔵 **Un silencio se pregunta; una negativa explícita de derivados hay que tramitarla
con el organismo.** Ver **P187**.

🟢 **El detalle de la fila vieja era CORRECTO y es lo que salva la medición:** los 14 nombres **sí**
dan 404 **en la raíz**, y el `README.md` **sí** da 200. 🔵 **La pregunta estaba bien hecha y la
respuesta era verdadera — lo que estaba mal era leer «no hay licencia en la raíz» como «no hay
cesión».** ⚠️ **El archivo vive en el subdirectorio de la VERSIÓN y en minúscula, y sólo en una de las
tres versiones: `ob_v2p1/license.md` y `ob_v2p0/license.md` dan 404.**

### 🔵 La consigna de instrumento que esto deja para esta capa

🔴 **Esta base tiene 15 filas de estándares** (1EdTech/IMS, QTI, xAPI, Caliper, Open Badges, CLR,
OneRoster, Ed-Fi…). **La pregunta de licencia sobre un repo de especificación no es la misma que sobre
un repo de código:**

1. 🔵 **Enumerar los subdirectorios de versión** y pedir `license.md` **en minúscula** en cada uno.
2. ⚠️ **No asumir que el repo tiene UNA licencia:** puede tener una por versión, y dos versiones en
   silencio.
3. 🔴 **Y si aparece una licencia de especificación, distinguir las dos cosas que un cliente mezcla:**
   **implementar** contra el estándar no requiere permiso; **derivar un perfil** del documento sí.

## 🇯🇵 La capa de currículo gana JAPÓN, y es la pieza mejor cedida de toda la capa (acción 3 del pase 65, pase 65 del 2026-10-03)

El hueco de Japón venía **declarado sin medir desde el pase 61** —cuatro veces—. Cerró al buscar
**en el idioma del país**: `学習指導要領` (*gakushū shidō yōryō*), no «Japan curriculum ontology».
Es el mismo canal que en el pase 61 rindió 11 piezas tras diez pases sin altas.

| Repo | Licencia | Qué es | Región |
|---|---|---|---|
| [`jp-cos/jp-cos.github.io`](https://github.com/jp-cos/jp-cos.github.io) | **CC BY 4.0** 🟢 *medida en el payload y en el HTML del repo* | **学習指導要領LOD** — el currículo nacional japonés completo como Linked Open Data: RDF/Turtle + HTML, todos los tipos de escuela, currículos nuevos y viejos. **22 volcados TTL versionados** (`all-20250927.ttl` el mayor), vocabulario (`schema-class`, `schema-property`), **SHACL `shapes-20250817.ttl`** (71 KB) y endpoint SPARQL declarado. 7 ★, **39 issues abiertos**, último cambio **2026-09-25** | **APAC** (Japón) |
| [`ICT-CONNECT-21/CSCode2023`](https://github.com/ICT-CONNECT-21/CSCode2023) | **MIT** 🟢 *texto completo, 1.081 B* | El programa de referencia de búsqueda sobre los códigos del currículo, **por encargo de MEXT**. Es el lado SOFTWARE de la misma capa | **APAC** (Japón) |

**Publicador del dato:** 教育データプラス研究会 (*Education Data Plus Research Group*), © 2021-2026 —
**no es MEXT**. MEXT es el **出典** (la fuente): «学習指導要領コードのコード表（全体版）».
**IRI canónico:** `https://w3id.org/jp-cos/`.

### La cesión, y por qué los instrumentos de esta KB no la veían

`LICENSE` **no existe** en los 14 nombres × ref `HEAD`, así que la capa de archivo clasifica este
repo `UNLICENSED`. **Está declarada dos veces, las dos dentro del repositorio:**

1. **En el HTML publicado** (`index.html`, rama por omisión):
   `このデータセットは…クリエイティブ・コモンズライセンス 表示 4.0…として自由に利用できます。`
   con el URI canónico `creativecommons.org/licenses/by/4.0/`.
2. **En el PAYLOAD RDF** (`dataset-20250927.ttl`, descripción VOID/DCAT):
   `dct:license [ rdf:value <https://creativecommons.org/licenses/by/4.0/> ; rdfs:label "Creative Commons license Attribution 4.0"@en ]`

🔵 **La segunda forma —nodo en blanco, y en la línea 66, detrás de 6 KB de prefijos y literales
largos— es la que define los defectos D2 y D3 del extractor** de
`compose/code/p172-payload-license-sweep/`, cada uno con su control.

### Por qué esto ordena la capa entera, con la licencia como clave

| Región | Pieza | Licencia | ShareAlike | Entregable |
|---|---|---|---|---|
| **APAC — Japón** | `jp-cos` 学習指導要領LOD | **CC BY 4.0** | 🟢 no | 🟢 **sí, con atribución** |
| APAC — Corea | pieza MIT de pases previos | MIT | 🟢 no | 🟢 sí |
| **EMEA — Alemania** | `dini-ag-kim/school-curriculum-pg` (16 Länder) | **CC BY-SA 4.0** | 🔴 **sí** | ⚠️ derivado debe ir CC BY-SA (**P178**) |
| EMEA — Alemania | `dini-ag-kim/schulfaecher` (materias) | CC0 1.0 | 🟢 no | 🟢 sí |
| LATAM — Chile | `curriculumnacional.cl` | ⚠️ términos **no leídos** (dominio bloqueado) | — | 🔴 hay dato, no hay artefacto: se extrae |
| NA — Common Core | 3 renderizaciones JSON | 🔴 **sin licencia** | — | 🔴 no |

🔴 **El orden comercial se invierte respecto de lo que esta base venía diciendo: la región con el
38 % del mercado (NA) sigue siendo la PEOR cedida, y la mejor es Japón**, que hasta este pase
figuraba como hueco.

### Canales declarados

- 🔴 **`www.mext.go.jp` bloqueado por DOS canales independientes** (`curl` → `connect_rejected`;
  WebFetch → `EGRESS_BLOCKED`), igual que los seis dominios alemanes del pase 64. Los términos de
  MEXT —公共データ利用規約（第1.0版）, que permite reproducir, transmitir, traducir y adaptar—
  quedan **corroborados por canal secundario, NO medidos**.
- 🔴 **`jp-cos.github.io`, `w3id.org`, `zenodo.org` y `dydra.com` bloqueados.** 🟢 **La vuelta que
  funcionó, y es reusable: un sitio Pages se sirve DESDE un repo, y `raw.githubusercontent.com`
  está abierto** — `index.html` y `about.html` se leyeron por `raw`.
- ⚠️ **El endpoint SPARQL no se verificó** (dominio bloqueado) y el publicador lo anuncia
  **試験公開中** (*publicación de prueba*): **ninguna receta debe depender de él sin verificarlo.**
- ⚠️ **El grafo está medido por MUESTRA**: se leyó entero un registro de ítem
  (`710/0000000000000.ttl`, 1.102 B) y no se recorrieron los 104 directorios de código.

---

## 🧬 La licencia del DATO vive DENTRO del dato: las tres ontologías de `FWU-DE` declaran CC BY-SA 4.0 en el `.owl`, y eso refuta el titular del pase 63 (acción 3 del pase 63, pase 64 del 2026-10-03)

**El pase 63 cerró la capa de currículo con una afirmación fuerte y un patrón elegante: *«3 de 3
de código licenciados con tres licencias distintas; 3 de 3 de dato sin ninguna, y sin licencia en prosa
tampoco»*, con *«el publicador no es la licencia»* (**P166**) como lección. La acción 3 pedía
buscar la licencia FUERA de la raíz —en subdirectorios, en GitHub Pages y en las cabeceras del
RDF/OWL— sobre `dini-ag-kim/school-curriculum-pg`. Al correrla, la mitad «sin ninguna licencia» del
titular se cae.**

### 🔴 Las tres ontologías SÍ ceden, y la cesión estaba en el payload

| Repo | Archivo `LICENSE` en raíz | «Licencia» en el README | **Dentro del `.owl`** |
|---|---|---|---|
| [`FWU-DE/lehrplan-ontologie`](https://github.com/FWU-DE/lehrplan-ontologie) | 🔴 **404** los 14 nombres | 🔴 **0 coincidencias** en 4.297 B | 🟢 **`Annotation(<http://purl.org/dc/terms/license> <https://creativecommons.org/licenses/by-sa/4.0/>)`** en `src/ontology/lp-edit.owl` |
| [`FWU-DE/schulfach-ontologie`](https://github.com/FWU-DE/schulfach-ontologie) | 🔴 **404** | 🔴 **0** | 🟢 **misma anotación, IRI completo**, en `src/ontology/sf-edit.owl` |
| [`FWU-DE/schulart-ontologie`](https://github.com/FWU-DE/schulart-ontologie) | 🔴 **404** | 🔴 **0** | 🟢 **`Annotation(dcterms:license <https://creativecommons.org/licenses/by-sa/4.0/>)`** — ⚠️ **serialización PREFIJADA**, en `src/ontology/sa-edit.owl` |

🔴 **La conclusión del pase 63 era correcta sobre el canal que miró y falsa sobre el mundo: no
hay archivo de licencia y no hay licencia en prosa — pero **sí hay cesión**, y es la misma en las
tres.** 🔵 **Esto es **P153** ganando su caso más fuerte: la licencia del dato no está donde el
filtro la busca, está DENTRO del dato** (**P172**).

⚠️ **Y el detalle que rompe un grep ingenuo: las dos serializaciones no coinciden.** Dos repos
escriben el IRI completo `<http://purl.org/dc/terms/license>` y el tercero el prefijo
`dcterms:license`. **Un instrumento que busque una sola de las dos formas reporta 2 de 3 y vuelve a
publicar una ausencia falsa.** 🔵 **El patrón a buscar es `licen[sc]e` sobre el payload,
case-insensitive, no una cadena exacta.**

### 🔴 La ruta tampoco es adivinable, y por eso el pase 63 no la encontró

Los artefactos no están en la raíz ni con el nombre del repo: viven en **`src/ontology/<prefijo>-edit.owl`**,
y los nombres que el README anuncia —`lp.owl`, `lp-base.owl`, `lp-full.owl`, `lp-simple.owl`,
`reasoned.ttl`— **dan 404 los cinco**, porque son *productos de build* que el repo no versiona.
🔵 **El único archivo presente es el de EDICIóN, y es el que lleva la anotación. La ruta se
descubre leyendo el workflow de CI (`.github/workflows/qc.yml` → `cd src/ontology && make test`), no
probando nombres.**

### 🔴 `school-curriculum-pg` no es un upstream: es una lápida, y la receta P169 apuntaba al revés

**La acción 3 partía de un supuesto escrito en el pase 63: que `dini-ag-kim/school-curriculum-pg` era
*«la pieza que FWU importa y de la que depende la salida CC0 de la receta P169»*. Es falso.**

| Prueba | Resultado |
|---|---|
| `raw:HEAD/README.md` | 🟢 **200 — 136 bytes en total** |
| Contenido ÍNTEGRO del README | 🔴 *«# This repo is outdated ·· ## please go to ·· https://github.com/FWU-DE/lehrplan-ontologie»* |
| 14 nombres de licencia en raíz | 🔴 **404 los 14** |
| 5 subdirectorios (`ontology/`, `docs/`, `src/`, `data/`, `.github/`) | 🔴 **404** |
| 14 nombres de `.ttl`/`.owl`/GitHub Pages | 🔴 **404 los 14** |
| Lo único alcanzable además del README | ⚠️ **`.gitignore`** |

🔴 **El repo está vaciado y REDIRIGE a `FWU-DE/lehrplan-ontologie` — que es justamente la pieza
sin archivo de licencia.** 🔵 **La dirección de la dependencia era la inversa de la que la receta
suponía: no es «FWU importa de DINI, así que hay una salida CC0 arriba»; es «DINI apunta a FWU».**

🔵 **La hipótesis falsable de la acción 3 tenía dos ramas —declara en cabecera RDF, o no
declara en ningún lado— y el resultado no cae en ninguna: el repo no tiene cabeceras RDF porque no
tiene RDF.** ⚠️ **Una lápida con README no es «sin licencia» ni «con licencia»: es un
artefacto que ya no existe como dato, y medirle la cesión es una pregunta mal planteada** (**P173**).

### 🟢 La salida CC0 de la receta P169 sigue en pie, pero por otra pieza

🟢 **`dini-ag-kim/schulfaecher` —CC0 1.0, `raw:HEAD/LICENSE` 200, 7.047 B, re-verificado este
pase— NO es `school-curriculum-pg`.** Es el **vocabulario SKOS de materias escolares**, no la
ontología de currículo. 🔵 **Así que la receta P169 no se cae, pero hay que decir qué cubre:
la capa de MATERIAS está en dominio público; la capa de CURRÍCULO por Land está en CC BY-SA 4.0.**

### 🔴 El reparto de licencias de la capa de currículo, corregido por tercera vez

| Pieza | Región | Pase 63 decía | Pase 64 mide |
|---|---|---|---|
| `dini-ag-kim/schulfaecher` | EMEA (DE) | 🟢 CC0 1.0 | 🟢 **CC0 1.0** (sin cambio) |
| `FWU-DE/lehrplan-ontologie` | EMEA (DE) | 🔴 ninguna | 🔴 **CC BY-SA 4.0** (en el `.owl`) |
| `FWU-DE/schulfach-ontologie` | EMEA (DE) | 🔴 ninguna | 🔴 **CC BY-SA 4.0** (en el `.owl`) |
| `FWU-DE/schulart-ontologie` | EMEA (DE) | 🔴 ninguna | 🔴 **CC BY-SA 4.0** (en el `.owl`) |
| `nmarafo/OpenDidactia` | EMEA (ES) | ⚠️ texto anómalo | 🔴 **CC BY-SA 4.0** (`LICENSE.md`) |
| `dini-ag-kim/school-curriculum-pg` | EMEA (DE) | ⚠️ dependencia de P169 | 🔴 **lápida de 136 B** |

🔵 **El dato comercial que sale de la corrección, y es mejor Y peor que el del pase 63:**
**mejor**, porque Alemania **sí tiene cesión** y no hay que pedirle nada a FWU para usar el dato;
**peor**, porque **CC BY-SA 4.0 es ShareAlike** — el currículo derivado hereda la obligación de
compartirse igual. 🔴 **Para un engagement eso NO es «entregable sin condiciones»: es
entregable con una condición que se propaga al entregable del cliente.**
🔵 **Y aparece un patrón regional: las DOS piezas de currículo de EMEA con cesión leída
—Alemania y España— convergen en la MISMA licencia, CC BY-SA 4.0, publicadas por organizaciones
sin relación. El dato curricular converge en ShareAlike** (**P174**).

### 🟢 Las altas de este pase, con la licencia leída del archivo

| Repo | Licencia **leída** | Prueba | Qué es / por qué entra |
|---|---|---|---|
| [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | 🟢 **Apache-2.0** | `raw:HEAD/LICENSE` **200**, **13.184 B** | validador de Open Badges del organismo de estándares. 🟢 **Es el reemplazo PERMISIVO del muerto `concentricsky/badgr-server`: la capa de credenciales vuelve a tener una pieza viva y cedida** |
| [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) | 🔴 **IMS Global Specification Document License** (NO OSI) | `raw:HEAD/LICENSE.md` **200**, **12.402 B** | la spec de Caliper Analytics, **viva**, donde los clientes `caliper-php` y `caliper-python` dieron 404. ⚠️ **Ver la clase de licencia nueva abajo** |
| [`IMSGlobal/openbadges-specification`](https://github.com/IMSGlobal/openbadges-specification) | 🔴 **`SPEC-LICENSE` — ausencia FALSA, corregida en el pase 67**: IMS Global *Specification Document License*, **12.324 B** en `ob_v3p0/license.md` | 14 nombres **404 en la RAÍZ** (correcto), `README.md` **200** — ⚠️ **la cesión vive en el subdirectorio de la VERSIÓN y en minúscula**, y **sólo en `ob_v3p0`** | 🔴 **no es «sin cesión»: es una cesión que NIEGA los derivados** (*«No right to create modifications or derivatives of IMS documents is granted»*) — más dura que ShareAlike (**P187**) |

### 🔴 Una clase de licencia que la taxonomía de esta KB no tenía: la del ORGANISMO DE ESTÁNDARES

**`1EdTech/caliper-spec` no es permisiva, no es copyleft y no es ausencia. Es un régimen propio, y
conviene citarlo textual antes de que alguien lo cotice como «tiene LICENSE.md, listo»:**

> *«IMS specifications are published solely for the purpose of enabling interoperability … and are
> made available under license to **Registered Users** solely to further that purpose.»*

🔴 **Es una licencia de DOCUMENTO condicionada a membresía, con política de IPR y registro de
usuarios — no una cesión de software.** 🔵 **Para el filtro de esta KB
(MIT/Apache/BSD) el efecto práctico es: **la spec se lee, no se redistribuye como parte de un
entregable**, y la implementación propia es el camino. **Un escaneo que sólo pregunta «existe
LICENSE?» la aprueba** — el mismo modo de fallo de **P168**, por otra vía: ahí el archivo era
demasiado chico para ser una cesión, acá es lo bastante grande y **tampoco lo es** (**P175**).

## 🧾 La capa de currículo, cerrada por el lado de la LICENCIA: el publicador no es la licencia, y el upstream CC0 es la salida (pase 63 del 2026-10-03)

**El pase 62 dejó una acción explícita en este archivo —línea 135: *«Queda como acción del pase 63»*—:
establecer qué es FWU, porque de eso dependía si la ausencia de licencia en la mejor ontología de
currículo de Europa era un trámite o una decisión. Ejecutada, cambia el reparto de esta capa.**

### 🟢 FWU es público: una gGmbH de los 16 Länder

**FWU = «Institut für Film und Bild in Wissenschaft und Unterricht», gGmbH, sede en Grünwald (Baviera),
que se presenta como «das Medieninstitut der Länder».** La estructura societaria —**los 16 Bundesländer
al 6,25 % cada uno**— está declarada en el portal de participaciones del **Ministerio de Finanzas de
Mecklemburgo-Pomerania Occidental**, que es la fuente primaria correcta: un Land declarando su tenencia.

🔴 **Reserva de método, y es fuerte: este pase NO abrió ninguna de esas páginas.** `regierung-mv.de`,
`fwu.de`, `bildungsserver.de` y `de.wikipedia.org` están **los cuatro bloqueados por el proxy de egreso
de esta corrida.** **Lo que hay es el resultado de búsqueda sobre fuentes primarias identificadas, no su
lectura.** 🔵 **Se publica así a propósito: la fuente queda nombrada y localizable para que el próximo
pase —o un humano sin este proxy— la confirme en un minuto.**

### 🔴 Y la hipótesis cae en una TERCERA rama: es público Y la ausencia es deliberada

**La hipótesis del pase 62 era binaria —público ⇒ trámite pedible; privado ⇒ decisión—. Medido repo por
repo con `raw.githubusercontent.com`, el mismo publicador usa CUATRO regímenes a la vez:**

| Repo de `FWU-DE` | Tipo | Licencia **leída del archivo** | Prueba |
|---|---|---|---|
| [`mem-mcp`](https://github.com/FWU-DE/mem-mcp) | **código** (MCP) | 🟢 **Unlicense** | `raw:main/LICENSE` **200**, 1.211 B |
| [`fwu-kc-extensions`](https://github.com/FWU-DE/fwu-kc-extensions) | **código** (Java/Keycloak) | 🟢 **Apache-2.0** | `raw:main/LICENSE` **200**, 11.357 B |
| [`ais-chat`](https://github.com/FWU-DE/ais-chat) | **código** (chatbot escolar) | 🔴 **AGPL-3.0** | `raw:main/LICENSE` **200**, 34.523 B |
| [`lehrplan-ontologie`](https://github.com/FWU-DE/lehrplan-ontologie) | **dato** (16 Länder, RDF/OWL) | 🔴 **ninguna** | `LICENSE`,`.md`,`.txt`,`COPYING` → **404 los 4** |
| [`schulfach-ontologie`](https://github.com/FWU-DE/schulfach-ontologie) | **dato** (materias + SKOS por Land) | 🔴 **ninguna** | **404 los 4** |
| [`schulart-ontologie`](https://github.com/FWU-DE/schulart-ontologie) | **dato** (tipos de escuela, niveles) | 🔴 **ninguna** | **404 los 4** |

🔴 **El corte es exacto: 3 de 3 repos de CÓDIGO tienen licencia, con tres licencias distintas elegidas
una por una; 3 de 3 repos de ONTOLOGÍA no tienen ninguna.** ⚠️ **Y no hay licencia en prosa tampoco: se
buscó `licen[sz]|lizenz|copyright|CC[ -]BY|urheber|rechte|terms of use|nutzungsbedingung` en los tres
README y da **cero coincidencias en los tres**.** 🔵 **Es más limpio que el caso de P161 —ahí el README
prometía un `LICENSE` que no existía—: acá no se promete nada. Es silencio, no promesa incumplida.**

🔵 **La consecuencia, y es el patrón P166: un publicador que eligió Unlicense, Apache-2.0 y AGPL-3.0
para tres piezas distintas sabe adjuntar una licencia. La ausencia en las ontologías deja de ser
descuido y pasa a ser política.** **Para un engagement: se puede pedir, pero se entra a una negociación,
no a un trámite — y conviene pedirlo invocando que el dueño son los 16 Länder.**

### 🟢 La salida que SÍ está licenciada, y estaba un nivel más arriba: el upstream es CC0

**`schulfach-ontologie` declara en su README que mapea a las *KIM school subjects* e importa conceptos
de la ontología de currículo de la DINI AG-KIM. Medidas las dos fuentes:**

| Repo upstream | Licencia **leída del archivo** | Prueba |
|---|---|---|
| [`dini-ag-kim/schulfaecher`](https://github.com/dini-ag-kim/schulfaecher) | 🟢 **CC0 1.0 Universal** | `raw:main/LICENSE` **200** y `raw:master/LICENSE` **200** |
| [`dini-ag-kim/school-curriculum-pg`](https://github.com/dini-ag-kim/school-curriculum-pg) | 🔴 **ninguna en la raíz** | `LICENSE`,`.md`,`.txt` → **404** en `main` **y** `master` |

🟢 **El vocabulario base de materias escolares alemanas es CC0 —dedicación al dominio público, el techo
de permisividad— y es la primera pieza de currículo de EMEA que esta KB puede poner en un entregable
comercial sin ninguna condición.** 🔴 **Lo que no tiene cesión es, otra vez, la capa que agrega el valor
específico: la cobertura por Land que pone FWU encima.**

⚠️ **Lo que NO se midió, y por P153 no se infiere:** si `school-curriculum-pg` declara licencia en un
subdirectorio o en su GitHub Pages. **La ausencia en la raíz no prueba la ausencia.**

### 🧾 El reparto de licencias de TODA la capa de currículo, actualizado con el pase 63

| Región | Artefacto | Licencia | ¿Usable en entregable comercial? |
|---|---|---|---|
| **North America** | las tres renderizaciones JSON de Common Core en GitHub | 🔴 **sin archivo de licencia** (pase 61) | 🔴 **no** |
| **EMEA** (Alemania) | 🟢 **`dini-ag-kim/schulfaecher` — vocabulario KIM de materias** | 🟢 **CC0 1.0** (**alta del pase 63**) | 🟢 **sí, sin condiciones** |
| **EMEA** (Alemania) | `FWU-DE/lehrplan-ontologie` — 16 Länder, RDF/OWL | 🔴 **ninguna** (4 comprobaciones) | 🔴 **no** |
| **EMEA** (Alemania) | 🆕 `FWU-DE/schulfach-ontologie`, `schulart-ontologie` | 🔴 **ninguna** (**medidas en el pase 63**) | 🔴 **no** |
| **EMEA** (España) | `OpenDidactia` + `open-lex-edu` — LOMLOE, 17 CCAA, 832 normas | ⚠️ **CC BY-SA 4.0** | ⚠️ **sí, con *share-alike* en el contrato** |
| **EMEA** (Inglaterra) | `bbc/curriculum-data` | — | ⚠️ **último commit 2014** |
| **LATAM** (Brasil) | `bncc-dev/bncc-dados` y familia — BNCC | 🟢 **CC BY 4.0** | 🟢 **sí, con atribución** |
| **LATAM** (Chile) | 🆕 `curriculumnacional.cl` — OA por curso y asignatura | ⚠️ **PDF/HTML, sin artefacto estructurado** (**pase 63**) | ⚠️ **extracción, no reutilización** |
| **APAC** (Corea) | `DECK6/korean-elementary-learning-map` — 620 anclas, 2.293 prerrequisitos | 🟢 **MIT** | 🟢 **sí** |
| **APAC** (Australia) | MRAC / ACARA | 🔴 **ilegible** — `gap 254` | ⚠️ **indeterminado** |

🔵 **El dato que cambia respecto del pase 62: la capa pasa de UN artefacto permisivo y legible (Corea,
MIT) a DOS (Corea MIT + vocabulario KIM CC0), y el segundo está en EMEA, que era la región donde la
mejor cobertura técnica coincidía con la peor cesión.** 🔴 **Sigue valiendo el titular: de los
artefactos de currículo medidos, la mayoría no es entregable sin condiciones, y la ontología de mayor
cobertura poblacional de Europa continúa sin licencia.**

### 🔑 Y la capa gana superficie de agente: `mem-mcp`, dominio público, sobre dato sin licencia

🟢 **`FWU-DE/mem-mcp` (Unlicense, 6 ★) es un servidor MCP con 9 *tools* sobre un *triple store* del
currículo alemán** —`sparql_query`, `list_bundeslaender`, `list_schulfaecher`, `list_schularten`,
`find_lehrplaene`, `get_lehrplan_tree`, `get_children`, `get_kompetenzen`, `search`—, **MCP Streamable
HTTP con `Authorization: Bearer`.** **Esta KB venía declarando que Alemania tenía la mejor cobertura de
currículo de EMEA y ninguna puerta de agente encima. La tiene, es oficial y es dominio público.**

🔴 **Y deja el riesgo del engagement en su forma más nítida: la PUERTA es de dominio público y el DATO
que sirve no tiene licencia** (**P167**). **Se toma el mecanismo; el contenido se negocia.** 🔵 **Lo que
sí se puede hacer hoy sin pedir nada: apuntar `mem-mcp` a un *triple store* cargado con el vocabulario
CC0 de la KIM, y usar la ontología de FWU sólo como referencia de modelado.**

## 🌍 La capa de currículo, ampliada a ALEMANIA y a ESPAÑA — y el reparto de licencias de toda la capa, que es el dato que decide (pase 62 del 2026-10-03)

> **El pase 61 cerró declarando `gap 255`:** *«Para Alemania, Francia, España, Italia, Nórdicos,
> África, México, Colombia, Argentina, Chile y Perú este pase no encontró artefacto de currículo
> estructurado: es hueco medido, no cobertura.»* **Este pase lo trabajó país por país, buscando en el
> idioma del país. 🔴 El primer resultado es que el gap estaba mal declarado.**

### 🔴 `gap 255` se auto-refuta en España: la KB ya cubría el país desde el pase 3

**España figura en el `gap 255` como país sin artefacto de currículo estructurado.** 🔴 **Esta base
tiene [`nmarafo/OpenDidactia`](https://github.com/nmarafo/OpenDidactia) —LOMLOE, 17 comunidades
autónomas + 2 ciudades, de Infantil a FP— registrado desde el pase 3 y citado en SIETE archivos**
(`agents/top.md`, `agents/trending.md`, `repos/foundations.md`, `repos/trending.md`,
`compose/patterns.md`, `intel/market.md`, `intel/trends.md`), **con la región escrita como
«EMEA (España)»**.

🔵 **El gap no se declaró contra el mercado: se declaró sin leer la propia base.** ⚠️ **Es un defecto
del mismo tipo que los 114 *backlinks* colgados del pase 60 —la KB afirmando sobre sí misma sin
medirse— y por eso se anota como regla: una declaración de hueco por país tiene que correr contra el
índice de la base ANTES de salir a buscar** (**P162**).

### 🟢 Lo que SÍ es nuevo en España, y es la pieza grande: `open-lex-edu`

**`OpenDidactia` apuntaba a un repositorio de CONTENIDO que esta base nunca había registrado.**

| Repo | Región | Licencia | Dónde está el archivo | Qué trae |
|---|---|---|---|---|
| [`nmarafo/open-lex-edu`](https://github.com/nmarafo/open-lex-edu) | **EMEA** (España) | ⚠️ **CC BY-SA 4.0** | 🟢 **`LICENSE.md` en la RAÍZ** | 🟢 **832 normas estructuradas** en 9 categorías canónicas: Markdown con **frontmatter YAML** por documento (jurisdicción, fechas, estado, relaciones) y un **`index.yaml` global con grafo de referencias cruzadas**. Currículos mínimos del Estado (**RD 95/2022, 157/2022, 217/2022, 243/2022**) + los decretos LOMLOE de las **17 comunidades + 2 ciudades**, Infantil a Bachillerato. Declara cobertura completa al **2026-09-15**. 143 commits, 0 ★ |

🟢 **Y es el CONTROL NEGATIVO que a P153 le faltaba, y lo pasa:** P153 (pase 61) dice que en la capa
de currículo *«el archivo que declara la licencia del DATO no está en la raíz»* y que por eso el
probe de nombres de raíz devuelve la licencia de la parte sin valor. **Acá el dato declara su
licencia en `LICENSE.md` de la raíz, y el probe lo encontraría.** 🔵 **P153 describe un defecto
FRECUENTE, no universal — y ahora tiene su contraejemplo medido** (regla de P126).

⚠️ **Pero la licencia es `CC BY-SA`, igual que `OpenDidactia`: *share-alike* en las dos piezas
españolas.** 🔴 **España entera, en esta capa, es copyleft de contenido: derivar el esquema con los
datos del cliente arrastra la obligación. No es un bloqueo, es una partida del contrato.**

### 🟢 Alemania se cubre — y se cubre SIN licencia, que es el hallazgo

| Repo | Región | Licencia | Cobertura | Medición |
|---|---|---|---|---|
| [`FWU-DE/lehrplan-ontologie`](https://github.com/FWU-DE/lehrplan-ontologie) | **EMEA** (Alemania) | 🔴 **NINGUNA** | **los 16 Bundesländer** (`lp-land-XX-full.owl`: BB, BE, BW, BY, HB, HE, HH, MV, NI, NW, RP, SH, SL, SN, ST, TH) | **10 ★**, 4 forks. **RDF/OWL + Turtle** en cuatro variantes (`lp.owl`, `lp-full`, `lp-base`, `lp-simple`). Modela competencias, contenidos, materias, cursos, tipos de escuela, itinerarios y niveles de titulación, **conservando la terminología de cada Land**. ⚠️ Fuera de alcance declarado: FP y educación especial |
| [`teacherspet-cloud/schul-apps`](https://github.com/teacherspet-cloud/schul-apps) | **EMEA** (Alemania) | 🔴 **ninguna declarada** | ⚠️ **15 de los 16 Länder — falta Renania-Palatinado** | 0 ★, 216 commits. Temas de Lehrplan como dato estructurado + `resources/cefr/levels.json`. ⚠️ El propio README avisa que donde el documento oficial no decía nada *«bleibt das Feld leer»* |

🔴 **`FWU-DE/lehrplan-ontologie` es la pieza de currículo con la mayor cobertura poblacional de toda
esta capa —los 16 estados alemanes, en RDF/OWL— y NO TIENE LICENCIA.** Comprobado por tres caminos
en esta corrida: **`main:LICENSE` → 404**, **`main:LICENSE.md` → 404**, **ninguna declaración de
licencia en el README ni en la barra lateral del repo.**

⚠️ **Lo que este pase NO verificó de primera mano: qué es «FWU».** La organización en GitHub se llama
`FWU-DE` y el repo tiene forma de obra institucional, **pero la expansión de la sigla y su carácter
público no se leyeron en ninguna fuente primaria en esta corrida: no se afirma.** 🔵 **Importa, porque
si es un organismo público la ausencia de licencia es una gestión pendiente y se puede pedir; si no,
es una decisión.** **Queda como acción del pase 63.**

### 🔴 El reparto de licencias de TODA la capa de currículo, que es el dato que decide un engagement

**Juntando lo del pase 61 con lo de éste, la capa completa que esta KB tiene medida:**

| Región | Artefacto | Licencia | ¿Usable en entregable comercial? |
|---|---|---|---|
| **North America** | las tres renderizaciones JSON de Common Core en GitHub | 🔴 **sin archivo de licencia** (pase 61) | 🔴 **no** |
| **EMEA** (Alemania) | `FWU-DE/lehrplan-ontologie` — **16 Länder, RDF/OWL** | 🔴 **ninguna** (3 comprobaciones, este pase) | 🔴 **no** |
| **EMEA** (España) | `OpenDidactia` + `open-lex-edu` — LOMLOE, 17 CCAA, 832 normas | ⚠️ **CC BY-SA 4.0** | ⚠️ **sí, con *share-alike* como partida del contrato** |
| **EMEA** (Inglaterra) | `bbc/curriculum-data` | — | ⚠️ **último commit 2014** |
| **LATAM** (Brasil) | `bncc-dev/bncc-dados` y familia — BNCC | 🟢 **CC BY 4.0** (`dados/LICENSE.md`) | 🟢 **sí, con atribución** |
| **APAC** (Corea) | `DECK6/korean-elementary-learning-map` — 620 anclas, 2.293 prerrequisitos | 🟢 **MIT** | 🟢 **sí** |
| **APAC** (Australia) | MRAC / ACARA | 🔴 **ilegible** — `gap 254`, reconfirmado | ⚠️ **indeterminado** |

🔴 **El dato que vende, y es el resumen de dos pases: de SIETE artefactos de currículo medidos en
cuatro regiones, exactamente UNO es permisivo y legible —Corea, MIT—. Dos son *share-alike*, uno es
CC BY, dos no tienen licencia y uno es ilegible.** 🔵 **La capa más cara de reconstruir en cualquier
engagement educativo es también la peor licenciada, y el extremo permisivo es la EXCEPCIÓN.**

⚠️ **Y la asimetría regional se invierte respecto de lo que uno esperaría:** la región con más
presupuesto (**North America**) y la de mayor cobertura técnica (**Alemania**) son las dos que **no
tienen cesión**, mientras las dos utilizables vienen de **Brasil y Corea**.

### ⚠️ Lo que queda abierto de `gap 255`, medido y no inferido

🔴 **Francia, Italia, Nórdicos y África: este pase no los buscó** (se gastó el presupuesto de
búsqueda en Alemania y en el hispanohablante). **Siguen abiertos y NO se leen como cobertura.**

🔴 **LATAM hispanohablante sigue sin artefacto, y ahora con la búsqueda documentada.** Buscado en
español para México, Colombia, Argentina, Chile y Perú. **Lo que existe es dato ESTADÍSTICO, no
currículo estructurado y versionado:**

- **Argentina** — bases de la Evaluación Nacional **Aprender** y del **Relevamiento Anual**
  (`argentina.gob.ar/educacion/evaluacion-e-informacion-educativa/datos-abiertos`), con escritorio
  virtual y salida a R/Excel/PSPP. **Desempeño y variables del sistema, no el currículo.**
- **Colombia** — conjunto de datos abiertos del **Ministerio de Educación Nacional**. Ídem.
- **Chile** — **Datos Abiertos del Centro de Estudios del Mineduc** (establecimientos, estudiantes,
  docentes) y el portal **`curriculumnacional.cl`**, que publica objetivos de aprendizaje por curso y
  asignatura. ⚠️ **Es un PORTAL de consulta, no un artefacto versionado en un repositorio: es el
  candidato más cercano de la región y la pieza a atacar primero.**
- **México** — PLANEA usada para definir currículo y materiales; **sin artefacto estructurado hallado.**

🔵 **Conclusión honesta de la región: Brasil sigue siendo el ÚNICO país de LATAM con la capa de
currículo en un repositorio con licencia legible.** **No es que LATAM no tenga dato abierto: tiene
mucho, y es del eje equivocado.**

## 🌍 Capa fundacional de CURRÍCULO nacional estructurado — las cuatro regiones, con la licencia del DATO medida (pase 61)

> **Es la pieza más cara de cualquier agente docente y la que ningún cliente quiere pagar dos veces
> (gap 4).** Un pase anterior encontró dos artefactos de este tipo por accidente —uno coreano (MIT,
> con grafo de prerrequisitos) y uno español (CC BY-SA)— y dejó escrita la acción de buscarlos
> explícitamente por país. **Este pase la ejecutó.**
>
> 🔴 **Leer las DOS columnas de licencia.** La capa entera es dual, y el archivo que declara la del
> dato **no está en la raíz** en dos de los tres casos medidos (**P153**).

| Repo / artefacto | Región | Licencia **código** | Licencia **dato** | Formato | Estado |
|---|---|---|---|---|---|
| `bncc-dev/bncc-dados` | **LATAM** | **MIT** | **CC BY 4.0** | JSON, SQLite, CSV | 🟢 **vivo**, 1.721 aprendizajes, **procedencia por registro** (documento oficial y página), pipeline de extracción reproducible verificado en cada commit |
| `bncc-dev/bncc-pacotes` | **LATAM** | **MIT** | **CC BY 4.0** | npm, PyPI, MCP | 🟢 vivo, 97 commits en `main`; `@bncc/dados` 0.3.1, `@bncc/mcp` 0.2.0, `bncc` 0.2.0 |
| `bncc-dev/bncc-benchmark` | **LATAM** | **MIT** | **CC BY 4.0** | banco de ítems + resultados | 🟢 vivo; **1.721 ítems** en `itens/`, 17.100 respuestas crudas, held-out deliberadamente **no** publicado |
| `oaknational/oak-curriculum-ontology` | **EMEA** | **MIT** | **OGL v3.0** | OWL, SKOS, SHACL, RDF | 🟢 vivo; **31 clases**, alineado al National Curriculum for England (2014), 12 materias |
| `oaknational/oak-open-curriculum-ecosystem` | **EMEA** | **MIT** | **OGL v3.0** | SDK TS + MCP + Elasticsearch | 🟢 vivo; lecciones, unidades, *threads*, secuencias, quizzes y transcripciones. ⚠️ API key gratuita a pedido; **no acepta PRs externos** |
| `bbc/curriculum-data` | **EMEA** | — | **CC BY 4.0** | Turtle / RDF | 🔴 **de archivo: último commit 2014-09-12.** Cubre GCSE y Key Stages (Inglaterra), National 4/5 y Higher (Escocia), TGAU (Gales), CCEA/WJEC (Irlanda del Norte) |
| `eVgKatis/CCSO` | **EMEA** | **GPL-3.0** | — | ontología (OWL) | ⚠️ vivo pero **copyleft**: fuera del filtro permisivo de Globant |
| **MRAC** — Machine Readable Australian Curriculum V9 (ACARA) | **APAC** | oficial del Estado | ⚠️ **NO verificada este pase** | RDF/XML, JSON-LD, **SPARQL** | 🟢 publicación oficial; endpoint `rdf.australiancurriculum.edu.au/api/sparql`. ⚠️ **gap 254** |
| `CEDStandards/CEDS-Ontology` | **North America** | **Apache 2.0** | — | OWL → JSON, JSON-LD, XML | 🟢 vivo, CEDS v14, *«actively maintained production release»*. ⚠️ **modela ENTIDADES educativas (escuelas K12, postsecundaria, primera infancia), NO estándares de aprendizaje** |
| `commoncurriculum/common-standards-project` | **North America** | 🔴 **ninguna** | registros: `CC BY 3.0 US` | JSON | 🔴 **detenido desde diciembre de 2015**; 47 ★; «50 states, organizations, districts & schools» |
| `SirFizX/standards-data` | **North America** | 🔴 **ninguna** | — | JSON | ⚠️ 12 ★; Common Core Math terminado, Reading en curso; crudo de Achievement Standards Network |
| `qdonnellan/commoncore` | **North America** | 🔴 **ninguna** | — | XML → JSON | ⚠️ parser del CCSS |

**Son 12 filas y 12 son reales:** cada URL se verificó por `raw.githubusercontent.com`
(`200` en `main` o `master`) con control negativo en el mismo canal (repo inexistente → `404`);
cada licencia se leyó del archivo, no del README ni de la barra lateral. 🔴 **Las tres filas sin
licencia NO son usables en una entrega** (**P116**): «no hay archivo» no significa «permisivo por
defecto», significa que no hay permiso escrito.

### 🟢 Lo que esta capa vale, con número en vez de argumento (P156)

**Sin currículo aterrizado, el agente docente inventa el currículo del país del cliente, y está
medido:** en la ronda `oficial-seca-2026-09` de `bncc-dev/bncc-benchmark` (19 modelos × 900
respuestas) la fidelidad al texto oficial de la BNCC **va de 88 % a 3 %** y **la mayoría de los
modelos queda por debajo del 25 %**. 🟢 **Con la fuente: 31,9 % → 0,2 % de alucinación con el dato en
el prompt, 2,3 % vía MCP** (8 modelos, 300 ítems, tres condiciones pareadas, pre-registro cerrado
antes de la batería, media de caída 30,6 puntos, IC 95 % por bootstrap por ítem). ⚠️ **Ressalva que el
propio repo declara y que va junto con la cifra siempre:** la fuente de grounding y el gabarito son el
mismo dataset del mismo proyecto, así que **no es un ranking** — es el efecto del acceso al dato, y la
condición de control (el dato pegado en el prompt, sin herramienta) existe justamente para separar el
mérito del dato del mérito del instrumento.

### 🟢 Lo legal, que cambia la negociación y no sólo el inventario (P154)

**Leído textual en `bncc-dev/bncc-dados` @ `dados/LICENSE.md`:** *«os textos normativos da BNCC são
atos oficiais do Estado brasileiro e não são objeto de proteção autoral (art. 8º, IV, da Lei nº
9.610/1998). Esta licença cobre a compilação, a estruturação, os identificadores, as relações e a
curadoria produzidas por este projeto.»* 🔵 **El Reino Unido llega al mismo lugar por otra vía:** la
OGL v3.0 es la licencia de *public sector information*, con permiso **explícito** de explotación
comercial y una frase de atribución obligatoria y fija. 🟢 **Así que lo licenciable es la
COMPILACIÓN, no el currículo: a un cliente no se le puede cobrar el currículo de su propio país, y a
Globant no se le puede cobrar por usarlo.** ⚠️ **Y el reverso sirve de *due diligence*: un proveedor
que cobre por el texto normativo está cobrando por dominio público.**

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

## 🧱 `moodle/moodle` como FUENTE DE VERDAD del contrato de web service, no como dependencia (pase 60 del 2026-10-03)

🔵 **El pase 60 usó `moodle/moodle` de una forma que esta sección no tenía registrada y que conviene
dejar escrita como práctica: leerlo para resolver una pregunta de CONTRATO que ninguna de las piezas
derivadas contesta.**

| Dato | Valor |
|---|---|
| Repo | [`moodle/moodle`](https://github.com/moodle/moodle) |
| Licencia | ⚠️ **GPL-3.0** |
| Archivo leído | `public/mod/assign/externallib.php`, **3.146 líneas** |
| Versión del árbol | `$release = '5.3rc2 (Build: 20261002)'`, `$version = 2026100200.00` |
| Canal | `raw.githubusercontent.com` (`codeload` y `api.github.com` en `403`) |

🟢 **Lo que resolvió, y no estaba en ningún README de las nueve puertas:** que `markingworkflow` se
devuelve con el token normal —asignado sin condicional (l. 464), en el contrato y **no** `VALUE_OPTIONAL`
(l. 584), con `require_capability('mod/assign:view')` como único gate (l. 401) contra el
`mod/assign:grade` que exige escribir (l. 1033)—. 🔵 **Es un hecho del contrato de la plataforma, y por eso
vale para las nueve piezas a la vez en vez de haber que medirlo una por una.**

🔴 **La regla de uso, y es de licencia:** **GPL-3.0 se LEE como fuente de verdad, no se INCORPORA a un
entregable.** Lo que sale de esta lectura es **conocimiento del contrato** —qué campo viene, con qué
capacidad— y eso no es código derivado. ⚠️ **Lo que sí sería derivado es copiar su código a un
entregable propietario: no se hizo y no se propone.**

🟢 **`gap 250` cerrado por esta lectura:** el árbol de Moodle 5 se mudó a `public/` —
`public/mod/assign/externallib.php` responde `200` y `mod/assign/externallib.php` responde `404`—, así
que cualquier ruta de Moodle que esta KB citara con el prefijo viejo está desactualizada.
⚠️ **`gap 252` abierto en su lugar:** esto es `main` (5.3rc2), **no** una LTS desplegada; un cliente en
4.x necesita la misma lectura sobre su rama.

## 🧾 La LICENCIA se mide ANTES de la popularidad, y este pase tiene el contraejemplo más caro (pase 59 del 2026-10-03)

**Cero plataformas nuevas: duodécimo pase con el barrido genérico devolviendo la capa de siempre**
(Moodle, Open edX, Sakai, Canvas, ILIAS, Chamilo, OpenEduCat) **y material didáctico *sobre* AI en vez
de repos *para* educación.** 🔵 **El valor del pase está en una medición de licencia que cambia el
ORDEN de los filtros con que esta base recomienda.**

### 🔴 El MCP de Moodle más estrellado del barrido no tiene licencia (P147)

| Repo | ★ | `main/LICENSE` | `master/LICENSE` | Metadatos del paquete | Veredicto |
|---|---|---|---|---|---|
| [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) | **37** | 🔴 ausente | 🔴 ausente | 🔴 **sin clave `license` en `pyproject.toml`** (`moodle-mcp` v0.2.1) | 🔴 **SIN LICENCIA — inusable** |
| [`dddanielliu/NCCU-Moodle-MCP`](https://github.com/dddanielliu/NCCU-Moodle-MCP) | 0 | 🔴 ausente | 🔴 ausente | — | 🔴 **SIN LICENCIA** |
| [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | 0 | 🟢 **`MIT License`** | — | — | 🟢 **MIT medido de primera mano** |
| [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 0 | ⚠️ **AGPL-3.0** | — | — | ⚠️ **copyleft fuerte: no es base** |
| [`CharlieCardenasToledo/mcp-canvas-server`](https://github.com/CharlieCardenasToledo/mcp-canvas-server) | 0 | 🟢 **MIT** | — | — | 🟢 **permisiva** |

🔴 **`loyaniu/moodle-mcp` acumula 37 ★ —el segundo de toda la capa MCP de esta base, después de los
272 de `vishalsachdev/canvas-mcp`— y no se puede entregar.** El defecto es de **permiso**, no de
calidad: sin `LICENSE` en ninguna de las dos ramas y sin declaración en el empaquetado, no hay
concesión de derechos y el *default* del derecho de autor es «todos reservados».

🔵 **Regla de orden, y es lo que este pase aporta a este archivo:** **el filtro de licencia se aplica
ANTES del de popularidad.** ⚠️ **El orden inverso selecciona justamente lo que no se puede entregar**:
de las cinco medidas arriba, la más adoptada es la inusable y las tres permisivas tienen **0 ★**.
🔵 **Tercera reproducción de la curva invertida de P134/P138 —la pieza conforme no es la adoptada—,
ahora sobre la licencia en vez de sobre la compuerta de seguridad.**

### ⚠️ Y una corrección de CANAL que toca al verificador de licencias de esta base

🔴 **`curl -sI https://github.com/<owner>/<repo>` devolvió `403` para los ocho repos probados en este
pase**, incluidos los que el pase 58 verificó sin problema. **Es el proxy de egreso bloqueando `HEAD`
sobre el HTML de `github.com`, no un `404`.** 🔵 **Así que en este entorno la verificación de
existencia se hace por `raw.githubusercontent.com` (200) y por `WebFetch` de la página, dos canales
concordantes** — y **un `403` por `curl -sI` no es evidencia de nada sobre el repo.** ⚠️ **Se declara
porque el veredicto «`LICENSE` 404 en `main` y `master`» de este pase SÍ es válido: esas sondas fueron
contra `raw.githubusercontent.com`, que responde, y no contra el HTML bloqueado.**

## 🧱 La base que este pase agrega no es una plataforma: es el patrón de separación generación/publicación (pase 58 del 2026-10-03)

🔵 **El pase 58 no encontró plataforma nueva, y lo dice en vez de rellenar.** Las cuatro búsquedas globales
devolvieron por decimotercera vez la capa genérica de agentes (OpenClaw, opencode, CrewAI, LangGraph, OpenHands) y
material didáctico *sobre* AI, **que no es una base de la industria**. 🟢 **Lo que sí entró como punto de partida es
un repo chico con una propiedad arquitectónica que esta base necesitaba:**

| Repo | Licencia | Qué aporta como PUNTO DE PARTIDA |
|---|---|---|
| [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | **MIT** ✅ (texto del `LICENSE` leído: *«Copyright (c) 2026 littlecookie»*) | 🟢 **la implementación de referencia de P144**: genera laboratorio, examen y artefactos de corrección con DSL estructurados, `WAITING_REVIEW` y aprobación humana por página, **y no tiene camino de publicación** — *«The export does not call platform import, grading execution, or publishing paths»*. **30 commits, 0 ★, Python** |

⚠️ **Por qué se lista acá además de en `agents/top.md`:** como agente es joven y chico; **como punto de partida vale
por su forma** — el proceso que genera **no tiene credencial de escritura al LMS**, que es la única propiedad de las
medidas en los pases 56–58 que no se puede desconfigurar. 🔴 **Y lo que NO hay que esperar de él: no escribe en
ningún LMS**, así que un *engagement* que deba entregar notas necesita además una de las puertas de **P142** (y
entonces la verificación de plataforma es obligatoria) o el camino del importador CSV de **P143**.

⚠️ **Rechazo medido en el mismo barrido, para que el registro no parezca cobertura:**
[`dajiaohuang/WayMarker`](https://github.com/dajiaohuang/WayMarker) (tutor adaptativo con RAG y modelo de alumno
persistente) **queda afuera por licencia ausente MEDIDA** — `LICENSE` **404 en `main` y en `master`**, sin licencia
en el *sidebar*, 1 commit, 0 ★.

## 🧾 Capa de licencia de la capa de AGENTES — los 167 repos de `agents/top.md`, medidos con 20 nombres de archivo (agregada en el pase 51 del 2026-10-02)

**El pase 50 midió la licencia de los 32 paquetes de REGISTRO (sección de abajo). Este pase mide la
otra mitad: los repositorios de GitHub.** Código, control positivo y TSV en
`compose/code/p114-license-column/`.

| Veredicto | Repos | % |
|---|---|---|
| 🟢 **licenciado** (campo **y** texto, artefacto anotado) | **139** | **83,2 %** |
| 🔴 **sin licencia** (ausencia **medida**: 20 nombres × 2 ramas, repo respondiendo 200) | **23** | **13,8 %** |
| ⚠️ **no público por este canal** (canal **probado contra hermano de la misma organización**) | **5** | **3,0 %** |

**Mezcla de los 139:** MIT **79** · Apache-2.0 **27** · GPL **9** · AGPL **7** · BSD **4** ·
Creative Commons **3** · LGPL **2** · 🔴 **textos anómalos 4**.

🔵 **El dato de encuadre que esta sección agrega, y hay que decirlo con cuidado:** **106 de 139
(76,3 %) son MIT o Apache-2.0**. ⚠️ **Eso NO refuta la nota de cabecera de este archivo** —*media KB
de educación es GPL/AGPL*— **porque esa frase es sobre las PLATAFORMAS y esta tabla es sobre los
AGENTES.** 🔵 **La regla de cotización que sale: la capa agéntica se compone permisiva y la capa de
plataforma hay que negociarla. Una propuesta que promedie las dos poblaciones en un solo número de
«licencia» miente en las dos direcciones.**

### 🔴 Las 4 licencias que esta base no veía, y las dos causas son convenciones de ecosistema

| Repo | Artefacto real | Convención que la lista de 4 nombres no cubría |
|---|---|---|
| 🔴 **`moodle/moodle`** | `main:COPYING.txt` → *GNU GENERAL PUBLIC LICENSE* | **el mundo GNU/Moodle usa `COPYING.txt`, con extensión** |
| `jeanlucio/moodle-local_aihub` | `main:COPYING.txt` → ídem | ídem, plugin de Moodle |
| `contentauth/c2pa-rs` | `main:LICENSE-MIT` → *MIT License* | **doble licencia** (`LICENSE-MIT` + `LICENSE-APACHE`), mundo Rust |
| `contentauth/c2pa-python` | `main:LICENSE-MIT` → ídem | ídem |

⚠️ **Los dos `c2pa` importan más de lo que su nombre sugiere en una KB de educación: son la
implementación de referencia de C2PA, que es la pieza con la que se marca contenido generado — el
mismo requisito del Artículo 50(2) del AI Act que esta base cotiza en `compose/patterns.md`.**
**Estaban archivados como «sin licencia» y son MIT.**

### 🔴 Los 23 sin licencia confirmados incluyen piezas que esta base venía citando como permisivas

**Dos filas de `agents/top.md` decían «MIT ✅» sobre *badge* y prosa, sin una línea de texto:**
`RadiantCrystal/SafeTutors` y `kaushal0494/AITutor-EvalKit`. 🔴 **En `SafeTutors` el badge todavía
enlaza `github.com/your-username/SafeTutors/blob/main/LICENSE`: es andamiaje de plantilla sin
editar.** Y **`dssg/student-early-warning`**, archivado como *«Other (NOASSERTION)»*, resultó ser
una **licencia académica NO COMERCIAL de la Universidad de Chicago** que excluye *«any service or
part of selling a service»*. ⚠️ **Las tres habrían entrado a una propuesta por un filtro de badge.**

### 🟢 El control del hermano, que convierte «no sé» en «pedir acceso»

**Los 5 no resueltos dieron 404 en 6 ramas y `codeload` 403 por igual, así que ese canal no
distingue. El hermano sí:** `1EdTech/caliper-spec` responde **200** y `marcusgreen/moodle-qtype_gapfill`
también, **así que el canal llega a esas organizaciones y el repo específico no es público** —
`1EdTech/caliper-php`, `IMSGlobal/caliper-python`, `marcusgreen/moodle-tool_aiconnect`. ⚠️ **Quedan
indeterminados de verdad sólo 2** (`YL1N/EduGuardBench`, `concentricsky/badgr-server`).
🔵 **Encaja con la gestión de acceso a los repos de Caliper de 1EdTech que esta base arrastra: la
acción no es reintentar, es pedir membresía.**

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
| 🔴 **Sin campo de licencia** | **4** | `@superbuilders/oneroster` 0.7.0 → 🟢 **el pase 52 le leyó el TEXTO: `package/LICENSE` es 0BSD**, así que tiene permiso escrito y no campo; `@timeback/caliper` 0.3.3 → 🔴 **sin licencia confirmado por DOS canales**; `@pie-element/multiple-choice` **14.0.0** y `@pie-element/rubric` **9.0.0** → 🔴 **sin licencia confirmado por DOS canales** (20 nombres × 2 ramas + tarball anclado) |

**Y los 2 que no resuelven son una corrección propia, CORREGIDA a su vez en el pase 51 y etiquetada
en el pase 52:** ⚠️ **`@tutors/xapi` y `@tutors/badges` devuelven 404 en el registro, y NO eran citas
inventadas: son nombres del PR #341 de `tutors-sdk/tutors-mono-repo`, que está ABIERTO** (última
actualización 2026-09-30). 🔵 **Un paquete nombrado en un PR sin mergear no está en un registro por
definición, así que el defecto real es una cita SIN ETIQUETA DE ESTADO, no una cita falsa**
(tendencia 262). **Etiqueta que corresponde: `propuesto en PR abierto #341`, no `publicado`.**
🔴 **Y el alcance estaba equivocado, lo que costó SIETE paquetes permisivos reales:** el proyecto
publica en `@tutors-sdk/*` y sin alcance (MIT ×6 + ISC ×1), no en `@tutors/*`.

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
| 🟢 [`CSR2017/edfi-oneroster`](https://github.com/CSR2017/edfi-oneroster) | **Apache-2.0** ✅ (`LICENSE` **200** en `main`) | `HEAD` **2026-09-22** · 8 tags · 13 ramas | Misma descripción y mismo propósito. ✅ **`gap 79` CERRADO (pase 39, `merge-base` + `rev-list --left-right`): `Ed-Fi-Alliance-OSS` es upstream —3 commits adelante, 0 atrás— y el `merge-base` es el tip EXACTO de `CSR2017`, así que CSR2017 no agrega nada. Citar el de la Alliance.** ⚠️ *Esta celda decía «NO se resolvió → gap 79» cuatro pases después del cierre; corregido en el pase 77* |
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
| `jdolny/OneRoster.NET` | 2023-10-13 | 3,0 años | ⚫ muerto — 🟢 **pero MIT y v1p1+v1p2 (medido en el pase 76): muerto y BIFURCABLE** |
| `gotranseo/oneroster` | 2023-05-01 | 3,4 años | ⚫ muerto |
| `bgwdotdev/go-oneroster` (= `fffnite/go-oneroster`, 🔁 **duplicado byte a byte**) | 2019-11-04 | 6,9 años | ⚫ muerto |
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
| **SafeTutors** | https://github.com/RadiantCrystal/SafeTutors | 🚫 **sin licencia (medida en el pase 51; decía MIT ✅ sobre un *badge*)** | 0 | *(pase 5)* **Seguridad pedagógica**: 11 dimensiones de daño y 48 sub-riesgos sobre 5.955 instancias (matemática, física, química). EMNLP 2026 |
| **rubric** | https://github.com/paper-instruments/rubric | MIT ✅ | 75 | *(pase 5)* Motor genérico de **rúbricas ponderadas** para LLM-as-judge: criterio por criterio, single-pass u holístico, validación Pydantic. No es educativo — es la plomería permisiva sobre la que construir la capa de juicio |

**Cómo se usan juntas, que es el punto:** `pyKT` o `pyBKT` estiman qué domina el alumno, `py-fsrs` decide cuándo volver a preguntárselo, y `MathTutorBench` / `MRBench` / `EduBench` miden si la forma en que el agente responde es pedagógicamente buena y no sólo correcta. Las tres preguntas son distintas y hasta el pase 4 la KB sólo tenía la segunda. Ver el patrón **P10** en `compose/patterns.md`.

**Lo que agrega el pase 5 a esta capa son dos preguntas más, y las dos se venden solas en un cliente regulado:**

- **"¿enseña mal siendo amable?"** → `SafeTutors` (11 dimensiones de daño, 48 sub-riesgos). Mide revelación prematura de la respuesta, refuerzo de la idea equivocada del alumno y abandono del andamiaje. Ninguno de los benchmarks anteriores captura esto, y es el modo de falla que un docente reconoce al instante.
- **"¿esto funciona fuera de matemática?"** → `EduBench`. Los tres artefactos del pase 4 eran todos de matemática; este organiza por *escenario educativo* y cubre también los escenarios del docente.

**Y un cambio de licencia que importa:** el pase 4 tuvo que advertir que dos de sus cuatro piezas de medición eran Creative Commons con fricción (CC BY-SA en `UnifyingAITutorEvaluation`). `EduBench`, `pyBKT` y `rubric` son **MIT**; ⚠️ **`SafeTutors` NO —el pase 51 midió la ausencia de texto (20 nombres × 2 ramas en 404), así que esta frase decía «todas MIT» y era falsa para una de las cuatro.** El stack de evaluación pedagógica se arma permisivo **sin** `SafeTutors`, o con gestión previa de su `LICENSE`.

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

**Y la pieza complementaria ya está en esta KB desde el pase 4:** `EduBench` (**MIT**), `SafeTutors` (🚫 **sin licencia, pase 51**),
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

---

## 🇯🇵 El grafo japonés, MEDIDO — y la pieza pasa de «la mejor cedida» a «la única con educación especial» (acción 3 del pase 65, pase 66 del 2026-10-03)

El pase 65 midió este artefacto **por muestra de un solo registro** (`710/0000000000000.ttl`, 1.102 B)
y lo declaró *«la mejor pieza de currículo de la KB»* sobre esa muestra. 🔵 **Medido el grafo entero,
la afirmación se sostiene y se vuelve más fuerte por un motivo que la muestra no podía mostrar.**

### 🔴 Primero, la corrección: los 66 MB que el pase 65 declaró inalcanzables estaban en el repo

| Nombre | Código | Bytes |
|---|---|---|
| **`all-20250927.ttl.gz`** — como lo escribe `index.html` | 🟢 **200** | **4.251.289** |
| `all-20250927.ttl` — lo que el pase 65 sondeó | 🔴 404 | 14 (el cuerpo es la cadena `404: Not Found`) |
| **`cs-items-20220830.ttl.gz`** | 🟢 **200** | **2.522.650** |
| `cs-items-20220830.ttl` | 🔴 404 | 14 |

⚠️ **El nombre se transcribió sin el sufijo `.gz`, y los dos nombres mal transcritos son los dos
archivos más grandes del conjunto — que es exactamente por qué están comprimidos.** El pase 65
concluyó de ese 404 que *«el grafo completo sólo existe detrás de los dominios bloqueados»*: 🔴 **el
404 era real y la conclusión era falsa.** 🔵 **Y el listado estaba delante: es el mismo `index.html`
que ese pase leyó por `raw` para establecer **P181**. El canal correcto se usó y el dato se copió
mal; ningún canal nuevo hacía falta.**

🟢 **Medidos los 22 volcados exactamente como `index.html` los escribe: 22 de 22 dan 200.** La columna
«no medido» de `dumps.tsv` queda cerrada completa (`dumps.2026-10-03.tsv`).

### El grafo: 69.288.422 B (66 MB), 1.004.927 líneas

| Clase | n | Qué es |
|---|---|---|
| **`cs:Item`** | **39.958** | 🔵 **los ítems del currículo: el dato que un tutor necesita** |
| `cs:Subject` · `cs:SubjectArea` | **786 · 276** | materias y áreas |
| **`cs:CommentaryItem`** · `cs:CosCommentary` | **655 · 2** | 🟢 **学習指導要領解説, el comentario OFICIAL, dentro del mismo grafo** |
| **`cs:CourseOfStudyRevision`** · `cs:CourseOfStudy` | **34 · 20** | 🔵 **currículos viejos Y nuevos, como el publicador declara** |
| **`cs:RelatedSubject`** · `cs:RelatedSubjectArea` | **158 · 102** | 🟢 **enlaces entre materias: es lo que permite recorrer prerrequisitos** |
| **`sh:NodeShape`** | **17** | 🟢 **el SHACL de validación viaja DENTRO del grafo** |
| `cs:School` · `cs:Stage` · `cs:Period` | 9 · 7 · 9 | tipos de escuela, etapas, vigencias |
| **`cs:DisabilityCategory`** | **5** | categorías de discapacidad |
| `cs:Number` (literales tipados) | 46.277 | |

### 🟢 La cobertura, y el diferenciador: 特別支援学校 desglosado por discapacidad

| Nivel | Apariciones |
|---|---|
| 幼稚園 **Kindergarten** | **1.382** |
| 小学校 **Elementary** | **23.555** |
| 中学校 **LowerSecondary** | **17.468** |
| 高等学校 **UpperSecondary** | **79.926** |

| Rama de educación especial (SNES) | Apariciones |
|---|---|
| `UpperSecondaryDeptSNES` | **14.560** |
| `ElementaryAndLowerSecondaryDeptSNES` | **6.130** |
| `-Visual` (視覚) · `-Hearing` (聴覚) | **4.886 · 4.721** |
| `-Intellectual` (知的), tres niveles | **2.207 · 1.546 · 1.223** |
| `KindergartenDeptSNES` | **515** |
| `-VHPH` (視覚・聴覚・肢体・病弱) | **157 · 76** |
| variantes `-NC` (教育課程なし) | **432 · 372 · 341** |

⚠️ **Esto cambia el VALOR de la pieza, no su tamaño: el currículo nacional japonés en LOD viene con el
currículo de educación especial desglosado por categoría de discapacidad, bajo `CC BY 4.0` sin
ShareAlike.** 🔵 **Ninguna otra pieza de currículo de esta KB trae esa dimensión — tampoco la alemana
por *Land*, que además es `CC BY-SA 4.0`.** Y es el eje que decide un derivado:

| Región | Pieza de currículo | Licencia | ShareAlike | Educación especial desglosada |
|---|---|---|---|---|
| **APAC — Japón** | `jp-cos` 学習指導要領LOD | **CC BY 4.0** | 🟢 **no** | 🟢 **sí, por discapacidad** |
| **EMEA — Alemania** (base) | `dini-ag-kim/schulfaecher` | **CC0 1.0** | 🟢 no | 🔴 no |
| **EMEA — Alemania** (por *Land*) | `dini-ag-kim/school-curriculum-pg` | **CC BY-SA 4.0** *(corregido en el pase 66)* | 🔴 **sí** | 🔴 no |

🟢 **Para `P180` el alcance se cierra: no hay que construir vocabulario, ni validación, ni el
comentario — los tres vienen en el artefacto.** ⚠️ **La dependencia que la receta SÍ tiene que
declarar es el endpoint SPARQL**: `dydra.com` sigue bloqueado en esta corrida y el publicador lo
anuncia 試験公開中 (*publicación de prueba*). 🔵 **Con los 66 MB en la mano la receta no lo necesita:
se carga en un *triplestore* propio, y eso es exactamente lo que se cotiza.**

Medición reproducible en `compose/code/jp-cos-curriculum-gate/`:
`measure_dumps.sh`, `dumps.2026-10-03.tsv`, `graph-classes.2026-10-03.tsv`,
`graph-coverage.2026-10-03.tsv`.
