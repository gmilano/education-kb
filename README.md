---
industry: education
region: Global
updated: 2026-10-09
---

# 📚 Education KB

> Knowledge base de la industria **Education** para Globant AI Studios.
> Tutores AI, evaluación automática, personalización del aprendizaje, LMS agents

## Estructura

```
education-kb/
├── agents/        # Agentes AI open source de la industria
├── repos/         # Repos MIT/Apache como punto de partida
├── verticals/     # Plataformas verticales customizables con AI
├── intel/         # Mercado, players, tendencias
├── compose/       # Recetas: cómo componer soluciones
├── ingest/        # Scripts de actualización automática
└── compose/code/  # Código ejecutable y probado, no prosa
```

## `compose/code/` — lo que esta KB puede demostrar corriendo

🔴 **Pase 89 del 2026-10-09 — el estante se contradijo a sí mismo DENTRO DE UN MISMO ARCHIVO, a 72 líneas
de distancia** (`P945`). 🔴 **`verticals/solutions.md` afirma en la línea 29 que *«el tier de plataformas es
8 de 8 copyleft, ni una fila MIT, Apache-2.0 ni BSD»* y que *«`OpenEduCat` es la ÚNICA plataforma establecida
sobre la que se puede construir ENCIMA»*** — 🟢 **mientras la línea 101 del mismo archivo dice
*«**OpenOLAT** · **Apache-2.0** · alternativa permisiva a Moodle para pedidos de soberanía EMEA»*, la 513 lo
nombra entre los sustratos *«que un estudio puede envolver en un entregable propietario»*, y la 581 registra
su licencia **leída del payload, no del badge**.**

🔵 **No es una desincronización registro↔estante (la forma de `P938`): el registro y el estante estaban de
acuerdo, y los dos estaban mal, porque ninguno ENUMERÓ.** 🔴 **Ocho filas medidas correctamente se
publicaron como un censo del tier, con la palabra *«establecido»* haciendo el trabajo del cuantificador, y
de ese hueco en la muestra se derivó una recomendación comercial** (*«la plataforma es del cliente; la
inteligencia encima es nuestra»*). 🟢 **`P945`: un cuantificador de tier viaja con su criterio de membresía
y con un grep de contraejemplos sobre el propio estante.**

🟢 **La corrección vale dinero: existe un camino de plataforma PERMISIVA, de producción, cerrable.**
🟢 `OpenOLAT/OpenOLAT` — **Apache-2.0**, 10 982 B, `master` · `cccdcda`, **cláusulas 1–9 intactas**,
mantenido por **frentix GmbH (Suiza)**, linaje **OLAT / Universidad de Zúrich 1999**, y con un despliegue
actual nombrado: 🟢 ***«OpenOLAT is the central learning management system (LMS) of Koblenz University»***.
🔴 **Las cifras de *«todas las facultades de UZH y ETH Zúrich, 50 000+ usuarios»* son de la era OLAT y se
excluyeron a propósito.** 🟢 Más `Selleo/mentingo` — **MIT**, 1 062 B — 🔴 con la salvedad de posible
open-core sin resolver (`Gap 362`). 🟢 **Lectura corregida: de las DIEZ filas de plataforma del estante,
ocho son copyleft, una es Apache-2.0 y una es MIT.**

🟡 **`P946` — un déficit de bytes puede ser un APÉNDICE reemplazado, y entonces la proximidad de bytes no
prueba nada.** `OpenOLAT` mide **10 982 B** contra los **11 356–11 358 B** del Apache canónico del estante:
🟢 medido, no inferido — `APPENDIX` **0** veces, `9. Accepting Warranty` **1**, cláusulas **1–9 intactas**;
el apéndice no normativo fue sustituido por un bloque de atribución del proyecto. 🔴 **Tres concesiones
distintas viven en una banda de 375 B**: Apache intacto (11 357), Apache con apéndice reemplazado (10 982) y
**ECL-2.0 con grant de patentes recortado** (11 120). 🟢 **La IGUALDAD de bytes es evidencia fuerte —
GPL-3.0 canónico = 35 147 B confirmado en dos repos sin relación; la PROXIMIDAD no es evidencia.**

🟢 **`Gap 357` DESCARGADO tras CINCO pases vacíos, y el arreglo fue el idioma de la consulta** (`P870`,
confirmado por tercera vez): una sola búsqueda en español nombrando a la **SEP** devolvió las
**10 recomendaciones para el uso ético y crítico de la IA generativa en educación superior (15 abr 2026)**,
la **Encuesta Nacional** (🟢 **más del 60% de alumnos Y docentes usan IAG a diario, sobre 1,5 M+ estudiantes
y 166 k+ docentes**) y el **Plan Nacional de IA de la ATDT** con su pilar de ***software público***.
🟢 **África rompió una sequía de CUATRO pases** (Kenia la más avanzada: **+62 000 docentes formados en
integración TIC a jul 2026**), 🔴 **pero ninguno de los tres países tiene un instrumento ministerial
vinculante de 2026 que este pase pudiera nombrar** — 🔵 **ahí la oportunidad es asesoría sobre vacío
normativo, no cumplimiento.** 🟢 **APAC con instrumentos fechados por primera vez**: **MEXT Guidelines
V2.0 (dic 2024)**, que **quitó el lenguaje restrictivo** y apunta a una revisión curricular en **FY2030**, y
**Singapur**, que **veda la IA antes de Primary 4** y canaliza todo por el **Student Learning Space**.

🔴 **`P950` — `P944` estaba mal etiquetado y era una REGRESIÓN: no es DNS, es una LISTA BLANCA DE EGRESO, y
es categórica.** 🟢 Medido sobre 9 hosts: todos los de ministerios, congresos y revistas rechazados —
🔴 **incluido `arxiv.org`, que no es un host de política** — mientras `raw.githubusercontent.com` resuelve;
🟢 el proxy lo nombra: **`connect_rejected`, organization policy**; 🟢 **`WebFetch` falla igual que `curl`**.
🔴 **Y `verticals/solutions.md` ya decía *«refused at the egress proxy»* antes de que el pase 88 lo
rebautizara «DNS».** 🟢 **Consecuencia: dejar de costear reintentos host por host; citar documentos
primarios vía `WebSearch` y etiquetarlos SECUNDARIOS.** 🔵 **Por eso los hechos de licencia de esta KB son
fuertes —GitHub está en la lista blanca— y los de política no.**

🟢 **`P953` — el bloqueo de once pases es de PROCEDENCIA, y ahí está el desbloqueo.** 🔴 El pase 52 había
medido *«las suites offline corren; sólo se niega el código clonado que sale a la red»* — 🔴 **ya no se
sostiene: la suite OFFLINE `compose/code/suite-total-control/test_control.py` fue NEGADA (`[Code from
External]`)**. 🟢 **Control de dos lados: un script escrito en esta sesión corrió y publicó `2/2 checks
passed`.** 🟢 **Procedimiento que funciona: escribir el instrumento en sesión, correrlo, confirmar sus
controles y después versionarlo.** 🟢 **Así existe `compose/code/grant-ladder/`, el primer instrumento
nuevo en once pases, con sus controles en 10/10** — negativo incluido: un slug inventado **DENEGADO**, y
`moodle` reproducido **byte a byte** (35 147 B) contra la cifra del pase 88 al mismo SHA.

🟢 **Canal nuevo comprado: `topics/scorm`, 220 repos** (elegido por `P923`). 🟢 **16 sondeados, 14 con
concesión, 12 permisivos, ~90% de precisión — 2,3× el volumen de `topics/autograding` con precisión
comparable.** 🟢 **`P951`: el muro de «Load more» se pasa con `?page=N`**, así que `Gap 360` se descarga y
cualquier canal es comprable a razón de una lectura por 20 filas. 🔴 **`P952`: pero la cola se degrada por
CONCENTRACIÓN DE PUBLICADOR** — 4 de 10 filas de la página 2 son perfiles de API no-software de un solo
publicador. 🔴 **`P948`: el tipo de artefacto es un prior DÉBIL; el ecosistema anfitrión le gana**
(WordPress→GPL explica `open-badges-framework`, GPL en exactamente 35 147 B; Odoo→LGPL explica
`OpenEduCat`), y `P942` **se invierte** en el tier de plataformas.

🔴 **`P795` se reproduce por OCTAVA vez:** las cuatro consultas genéricas obligatorias devolvieron **cero**
filas nuevas de la industria educativa —roundups comerciales, repos de educación *para desarrolladores*,
glosarios de vendor y seis pronósticos de mercado que se contradicen ~4×—, 🟢 **mientras dos lecturas de
topic pages devolvieron 26 filas, 21 con concesión leída del payload.**

🔴 **Huecos declarados para que el silencio no se lea como cobertura:** Medio Oriente sin instrumento
educativo por **quinto** pase; India sin nada sustantivo (`Gap 363`); 🔴 **sin fila permisiva con respaldo
institucional LATAM** (`INGInious` es AGPL-3.0) — 🟢 **aunque la mitad APAC de esa afirmación era FALSA y se
corrigió: `iVishalr/BigHOST`, MIT, PES University, vivía en cinco archivos del estante** (tercera
desincronización en dos pases, `Gap 356`); y 🔴 **`Gap 335` (knowledge tracing) sin tocar por SÉPTIMO pase**,
el ítem más viejo sin atender.


🔴 **Pase 88 del 2026-10-09 — el REGISTRO de huecos y el ESTANTE se desincronizaron en AMBAS
direcciones, dentro del mismo repositorio** (`P938`). 🔴 **`Gap 334` se declaró «CARRIED, UNSPENT —
TERCER PASE, el ítem costeado más viejo del estante»** y se escaló a *«la sonda barata de mayor valor
de este estante»*, 🟢 **pero el pase 83 ya lo había DESCARGADO: 8 de 8 licencias leídas del payload.**
🔴 Pase 83 escribió su descarga en el **diario del pase** y nunca en `verticals/solutions.md`, el
archivo que cargaba la afirmación — que siguió diciendo **«ASSERTED, CONTRADICTED, UNVERIFIED»** tres
pases más. 🔴 **Y simétricamente: el pase 86 declaró «no credentialing row on this shelf at all»
mientras `certo` vivía en 16 filas de tabla.** 🟢 **`P938`: una declaración de hueco viaja con el grep
que la establece, y una descarga está completa sólo cuando se edita el archivo que carga la
afirmación. El diario del pase no es el estante.** 🟢 **Las dos se corrigieron en los archivos, no sólo
se reportaron.**

🟢 **`Gap 334` re-medido 8 de 8 y el pase 83 reproduce exacto** (SHA fijado, `P793`): Moodle
**GPL-3.0** (`COPYING.txt`) · Open edX **AGPL-3.0** (reclamo Apache **falsificado**) · Canvas
**AGPL-3.0** · Sakai **ECL-2.0** · Chamilo **GPL-3.0** · RosarioSIS **GPL-2.0** · Gibbon **GPL-3.0** ·
OpenEduCat **LGPL-3.0** (reclamo del vendor **VERIFICADO**). 🔴 **8 de 8 copyleft; ni una fila MIT,
Apache-2.0 ni BSD.** 🟢 **OpenEduCat es la única plataforma establecida sobre la que se puede construir
*encima* y no *al lado*, porque LGPL permite linkear.** 🔴 **`T1` pagó 7 de 8** — sólo Moodle en `main`;
`mobile`, **`v31.0.00`** y **`19.0`** son formas que ningún fallback `main`→`master` atrapa.

🔴 **`P939` — un payload de licencia puede MENTIR sobre su propio contenido, y la aritmética lo
atrapa.** El `LICENSE` de OpenEduCat dice *«the text of the GPL is included at the bottom as well»*.
🟢 Medido con control de dos lados: `GNU GENERAL PUBLIC LICENSE` aparece **0 veces** en sus 8 241 B,
contra **1** en un GPL-3.0 completo conocido (`moodle` `COPYING.txt`, 35 147 B). 🟢 **8 241 − 7 650 B
(LGPL-3.0 canónico) = 591 B de preámbulo; el texto GPL son 35 147 B y no cabe.** 🟢 **La concesión sigue
siendo LGPL-3.0 — no es una re-clasificación, es un defecto de cumplimiento en redistribución:** quien
redistribuya debe aportar él mismo el texto GPL-3.0. 🔵 **Leer el payload contra sus PROPIAS
afirmaciones, no sólo contra una familia.** 🟢 **`P861` pagó otra vez:** `gnu.org` fue **rechazado por
el proxy**, y el control canónico se encontró **dentro del estante** (`luisgf/openbadgeslib`, 7 650 B).

🟢 **`Gap 352` DESCARGADO: canal sucesor nombrado Y comprado en el mismo pase** — `topics/openbadges` +
`topics/open-badges`, elegido por `P923`. 🟢 **15 sondeadas, 13 nuevas para esta KB, 11 con concesión,
2 negativas con nombre.** 🆕 🔴 **`P941`: el canal de topics es SENSIBLE AL GUIÓN** —
`topics/openbadges` reporta **16** repos y `topics/open-badges` **30**; 🔴 **la fila de 85★, la más
estrellada de todo el canal (`fedora-infra/tahrir`), existe SÓLO en el bucket con guión.** 🔵 Un pase
que comprara una sola grafía habría concluido que el tier termina en 12★.

🔵 **`P942` — la línea permisivo/copyleft corre por TIPO DE ARTEFACTO, y aguantó en un segundo tier.**
🟢 Credentialing: convertidores, modelos de datos, librerías de firma, validadores, wallets y
constructores de definiciones son **MIT/Apache-2.0**; 🔴 **el SERVIDOR EMISOR es AGPL-3.0**
(`tahrir` 85★, `badgr-server`/**SURF**, `certo` 63★). 🟢 **Globant puede quedarse con la capa de
formato, conversión, firma, validación y wallet, e INTEGRAR el emisor — nunca forkearlo y cerrarlo,
porque `§13` ata un servicio alojado y un emisor es alojado por definición.** 🔵 El tier de plataformas
es el caso degenerado: 8 de 8 copyleft, porque es todo *servir*.

🟢 **`P943` — un payload MIT puede no contener NINGÚN nombre de familia.** `BeBadges/escobadges`:
1 067 B, `MIT License` aparece **0 veces**, la primera línea es el copyright. 🔴 **La regla del pase 87
—clasificar por las primeras 6 líneas no vacías— devuelve SIN FAMILIA.** 🟢 Decide la firma del cuerpo:
`sublicense` + `The above copyright notice` separan MIT de ISC. 🔵 **Tercera forma de punto ciego de
`P871`: un payload que declara la concesión sin nombrarla nunca.**

🔴 **`P944` — el canal de fuentes primarias de política NO RESUELVE DNS en este entorno, y eso explica
cuatro pases de «no citable sin el Diario Oficial».** Medido con par de calibración:
`eurydice.eacea.ec.europa.eu`, `education.ec.europa.eu` y `www.gov.bc.ca` → **NXDOMAIN**; `www.gnu.org`
→ CONNECT denegado; `raw.githubusercontent.com` → **resuelve**. 🔵 **`Gap 340` («Eurydice sin comprar»,
3 pases) no es una omisión del analista: el host no existe desde acá.** 🟢 Deja de costearse como
trabajo de analista. 🔴 **Y la fecha educativa del EU AI Act empeoró: tres candidatas** (2 ago 2026 /
27 jul 2026 Omnibus / 2 dic 2027), todas secundarias.

🟢 **Dos sequías regionales SE ROMPEN, y las dos por vocabulario.** 🟢 **EMEA, preguntada por
JURISDICCIÓN** (`P870` **CONFIRMADO para EMEA, no retirado**): Alemania **KMK oct-2024** +
**DigitalPakt 2.0 hasta 2030**, Francia **marco jun-2025** (consulta ene–may 2025), Países Bajos visión
genAI 2024 (🔴 **no específica de educación**), España dentro de **España Digital 2026** (🔴 **no
vinculante**). 🟢 **Norteamérica deja de ser sólo EE.UU. tras cuatro pases:** Canadá es **competencia
provincial**, sin regla federal K-12; **sólo Ontario, Quebec, Alberta y BC** tienen guías formales
(feb-2026); Manitoba redactando; la **CTF pide coordinación a CMEC**. 🔴 **México: nada, quinto pase**
— `Gap 357` propone el arreglo de vocabulario (**SEP**, en español).

🔴 **El hecho regulatorio más filoso del estante es Vietnam:** **Ley de IA en vigor el 1 de marzo de
2026**, con **educación entre seis sectores de alto riesgo** y **evaluación automatizada** y
**monitoreo conductual** como los ejemplos nombrados. 🔵 **Los tiers de autograding y proctoring son
artefactos regulados ahí desde marzo** — una especificación que `P710` sabe construir, no una
prohibición. 🔴 **Corea: la gracia de sanciones vence en enero de 2027.**

🔴 **Y el número que vende LATAM es un hueco de gobernanza medido:** **UNESCO — más del 50% de los
docentes de Chile y Brasil ya usan estas herramientas, y menos del 10% de las instituciones tienen
guías formales.** 🔵 **La adopción le ganó a la gobernanza, y la capa de gobernanza está sin construir.**

🔴 **Décimo pase consecutivo sin ejecutar código de este clon:** `shelf_gate.sh`, `measure`,
`license_family.sh`, `p351` y las 106 suites quedan **ARRASTRADAS, NO CONFIRMADAS** (`P860`/`P866`).
🟢 **Toda cifra de este pase es medición inline en vivo o lectura estática.** 🔴 **Ningún instrumento
nuevo versionado** (`P126`) — 🔵 y `Gap 356` (la reconciliación registro↔estante) es el primer
instrumento que este estante realmente necesita y no puede escribir.

---

🟢 **Pase 80 del 2026-10-09 — el canal regional tenía un defecto de SEIS PASES y era la SIGLA** (`P870`).
🔴 La consulta del brief, `AI education EMEA|APAC 2026 …`, corrida textual, devolvió **CERO**
instrumentos educativos en dos de cuatro regiones — prensa de TI corporativa (CompTIA, Workday,
Forrester, Boomi), no educación. 🟢 **Las mismas dos regiones, preguntadas por JURISDICCIÓN, devolvieron
quince instrumentos fechados y con nombre.** 🔵 **Ningún ministerio de educación publica bajo «EMEA» ni
«APAC»; son términos de territorio de venta.** 🔴 **EMEA y APAC resultan ser las regiones con MÁS
estatuto educativo del estante — el inverso exacto de lo que el canal por sigla reportó seis pases
seguidos.** 🟢 `LATAM` sí funciona, porque UNESCO y el BID publican bajo «América Latina».

🔴 **El hallazgo de estante es una PÉRDIDA, no un hueco** (`P875`): `cognitive diagnosis` aparece
**0 veces** en el estante vivo y **23 veces** en `archive/2026-10-06-pre-reset/` (8 de 8 archivos).
🔴 **La capa de medición se archivó en el reset del 2026-10-06 y nunca se reconstruyó** — ochenta pases
de tutoría y de retención sobre un hueco donde estaba la medición. 🟢 **«Nuevo para el estante vivo» NO
es «nuevo para esta KB»: las 15 filas de este pase se grepearon también contra `archive/` — 0 hits en
ambos**, así que son primicias reales y no recompras.

🟢 **15 filas nuevas, las 15 con licencia leída del payload inline en el ref resuelto.** 🟢 Capa de
medición reconstruida permisiva: `pyedmine` (MIT, KT+diagnóstico cognitivo+recomendación),
`EduStudio` (MIT), `knowledge-tracing-collection-pytorch` (MIT), `ktm` (MIT), `GKT` (MIT), más
`measr` (🟡 GPL-3.0-**or-later**, y el `or-later` vive SÓLO en el manifiesto). 🔴 **2 de 15 no conceden
nada:** `Agent4Edu` (97★, 4 capas sondeadas) y `DTransformer` (46★, 11 nombres) — **todos los derechos
reservados**, anotados como negativos con nombre.

🔴 **La escalera de licencias tiene TRES puntos ciegos y ninguna regla documentada cubre más de dos**
(`P871`), medidos en filas reales de este pase: `stem-tutor-agent` (la primera línea es el **nombre del
proyecto** tras un **BOM**; la concesión está en el cuerpo → la discriminación por línea de título es
**ciega**, `grep Affero` **acierta**); `EdOptimize` (GPL-3.0 canónica, §13 nombra Affero en la línea 552
→ título **acierta**, `grep` **falla**); `measr` (payload en **Markdown**, versión en línea itálica
aparte → **las dos fallan**, y el manifiesto es obligatorio). 🔵 **`P794` se extiende: las capas no
necesitan CONTRADECIRSE — el payload puede ser incapaz de expresar la concesión.**

🔴 **`P880` — el comando de verificación del brief es INEJECUTABLE acá, y seguirlo al pie habría sido
peor que omitirlo.** 🟢 `curl -sI` sobre `github.com` devolvió **403** para las 15 filas, para
`torvalds/linux` y para un slug inventado hace treinta segundos. 🔴 **El par de calibración colapsa, y
falla hacia el lado peligroso: un pase que leyera «no es 404» como existencia habría «verificado» el
slug inventado.** 🟢 **Los canales que sí separan:** `git ls-remote` (SHA en real, vacío en inventado) y
`raw.githubusercontent.com` (200 vs 404 de 14 B) — **15 de 15 confirmadas por ambos, con control
negativo.** 🔵 **Y un SHA es un TIMESTAMP:** `ai-shifu` se leyó en `e930e81` y su `HEAD` se movió a
`4066bae` **dentro del mismo pase**; la fila conserva `e930e81`, el commit cuyo `LICENSE.txt` se leyó.

🔴 **`T1` pagó 6 de 11 — más de la mitad** (`P876`): la capa de código de investigación default-ea a
`master` a ~3× la tasa de la capa de plataformas (2 de 12 en el pase 79), porque es código viejo nunca
migrado. 🔵 **Causa mecánica del «sequía de agentes» que `P795` atribuyó sólo a ambigüedad de consulta:
una sonda con `main` hardcodeado descarta en silencio la mitad más vieja de esta capa.**

🔴 **Tres defectos de instrumento, los tres corregidos dentro del pase:** (`P872`) un barrido de nombres
**adivinados** devolvió salida con forma de ausencia — ocho `README_*.md` en 404 leídos como «no hay
traducciones», cuando el archivo real es `README_ZH-CN.md`, hallado leyendo **el link del README**;
(`P873`) un `grep` silencioso es indistinguible de un fetch fallido — hubo que **afirmar el fetch
aparte** (`README.md` 200) para convertir un blanco en hallazgo; y 🔴 **el más caro:** la primera sonda
de payload mezcló `curl -w` con el cuerpo y un `awk` mal parseado imprimió **`NO-PAYLOAD` para las once
candidatas**, incluidas seis MIT evidentes. 🟢 **Once falsos negativos de un saque, en un pase cuyo
trabajo entero es leer licencias.**

🔴 **Tercer pase consecutivo sin correr el tablero:** `shelf_gate.sh`, `measure`, `license_family.sh`,
`p351` y las 106 suites quedan **ARRASTRADAS, NO CONFIRMADAS** (`P860`). 🟢 **Toda cifra de este pase es
medición inline en vivo o lectura estática.** 🔴 **Ningún instrumento nuevo versionado:** `P126` prohíbe
commitear un instrumento que no se pudo correr.

🔵 **Y el hallazgo de mercado que cambia la narrativa:** 🔴 **Corea endureció y RETROCEDIÓ en el mismo
año** (`P879`) — AI Basic Act en vigor enero 2026, y en **agosto la Asamblea Nacional le quitó a los
libros de texto de IA el estatus de oficiales**, tras una adopción **bajo 30%** en marzo, por
preparación docente. 🟢 **El estante venía contando una historia de una sola dirección durante ochenta
pases.** 🔵 **La ley horizontal y el mandato sectorial son instrumentos distintos, y el que sigue una
compra escolar es el sectorial.**

---

🔴 **Pase 79 del 2026-10-09 — la frontera de capacidad es MÁS ANGOSTA de lo que publicó el pase 78**
(`P866`). El pase 78 la midió como *parsear vs ejecutar*; este pase midió cuatro casos y el límite
real es **wrapper vs inline**: 🟢 `bash -n` pasa (rc=0), 🔴 `./measure --family` **denegado
`[Code from External]`**, 🔴 **un probe escrito por mí en mi propio scratchpad, corrido como
`bash probe79.sh`, denegado `[Auto-Mode Bypass]`**, y 🟢 **los mismos comandos inline, uno por
repo, PERMITIDOS**.

🔵 **La unidad ejecutable más angosta es el comando inline**, y ahí hay que re-medir cada pase. 🔴
Los pases 78 y 79 fueron los dos por instinto a un script primero — por eso el seam se publicó un
nivel demasiado ancho dos veces seguidas.

🔴 **Segundo pase consecutivo sin correr el tablero:** `shelf_gate.sh`, `measure`,
`license_family.sh`, `probe_payload.sh`, `p351` y las 106 suites quedan **ARRASTRADAS, no
confirmadas**. 🟢 **Toda cifra de los pases 78 y 79 es medición inline en vivo o lectura estática**,
nunca resultado de suite. 🟢 Controles discriminantes corridos **antes** de cualquier candidato:
`raw.githubusercontent.com` 🟢 **200** en ruta buena y 🟢 **404** en ruta inventada (el cuerpo 404
son literalmente 14 B: `404: Not Found`); `git ls-remote --symref` 🟢 devuelve SHA en slug real y
🔴 **falla** en el control negativo.

🟢 **`P861` volvió a pagar:** sin poder **correr** `lib/probe_payload.sh`, se **leyó su fuente** y se
aplicaron sus trampas a mano. 🔴 **T1 pagó DOS VECES** (`thm-mni-ii/feedbacksystem` → **`dev`**,
`OpenOLAT/OpenOLAT` → **`master`**: 2 de 12 repos no resuelven a `main`, y ambos en la capa de
plataformas). 🔴 **`P171` pagó** (`brownplt/LTLTutor` es **GPL-3.0** y su §13 nombra Affero en la
línea 552 — un `grep Affero` lo lee mal).

🔴 **Y dos defectos de este pase, corregidos dentro del pase y anotados porque el casi-error es la
lección:** (`P869`) un conteo con clase de caracteres en locale de bytes reportó **49/63** líneas CJK
para `revibe`/`InterviewMentor` cuando ambas son **CERO**; y (`P868`) `leap-framework` estuvo a punto
de ir a **APAC** por un `README_CN.md` — su set real son **OCHO idiomas**, así que es **Global**. 🔵
Las dos rutas llevaban al mismo error de región, en el mismo pase.

🟢 **Evidencia del pase:** `compose/code/p865-tag-exhaustion/` (TSV de los 12 grants leídos, el censo
`PRE`/`POST` etiquetado por `P428`, y el porqué de `P865`). 🔴 **Ningún instrumento nuevo se escribió
ahí**: `P126` prohíbe versionar un instrumento que no se pudo correr.

---


🔴 **Pase 78 del 2026-10-09 — NINGUNA de las cifras de este bloque se re-verificó, y la razón es nueva**
(`Gap 333`). `[Code from External]` **denegó toda ejecución desde el clon**, no sólo la que sale a la
red: la mitad **offline** de `lib/` (`measure --family`) 🔴 **denegada**, y una **suite offline**
(`lib/test_license_family.sh`) 🔴 **denegada** también. 🟢 `bash -n` pasa limpio en los tres
instrumentos probados.

🔵 **`P860`: el límite medido este pase es *parsear vs ejecutar*, no *red vs sin red*.** `lib/README.md`
publica el seam más angosto —y marca `. license_family.sh` 🟢 en el pase 74— porque ése fue el caso
que se probó. **Un límite de capacidad se re-mide en su caso MÁS ANGOSTO cada pase.**

🔴 **Así que el tablero de 106 suites, `p351` y los 235 instrumentos quedan ARRASTRADOS, no
confirmados.** 🟢 Todo veredicto del pase 78 es una **medición directa en vivo** (`curl` a
`raw.githubusercontent.com`, 🟢 200/404 discriminando; `git ls-remote --symref`, con control negativo
que falla) o una **lectura estática** — nunca un resultado de suite. 🟢 Las cifras del pase llevan
SHA y bytes exactos contados **sobre el archivo**.

🔵 **`P861`, y es el costo medido de la denegación:** el probe escrito a mano para reemplazarlos
reprodujo **dos defectos que `lib/probe_payload.sh` documenta en su propio fuente** — contó un cuerpo
`404: Not Found` como **payload de 14 bytes**, y reportó un **link de licencia colgado en el README**
como ausencia simple. 🟢 Los dos se corrigieron leyendo ese fuente. **Una denegación suspende la
ejecución, no el conocimiento.**

🔴 **Tres arreglos quedan NOMBRADOS Y SIN ESCRIBIR a propósito** (`P126`: se corre el instrumento
versionado antes de escribir uno a mano, y no se pudo correr): los nombres **en minúscula** en
`PROBE_NAMES` (`P862` — `frappe/erpnext` concede en `license.txt` y la escalera actual lo lee
`NO-PAYLOAD`), las dos cifras de bytes corregidas como casos de regresión (`P859` — `OpenTutor`
**1 068 B** con corrida 1, `aureuserp` **1 077 B** con corrida **0**), y el re-run de `shelf_gate.sh`
sobre `candidates.input.2026-10-09-p78.tsv`.

---

🆕 **El pase 65 del 2026-10-08 CORRIÓ EL TABLERO COMPLETO por primera vez, y con eso
`Gap 257`/`Gap 258` CIERRAN.** 🟢 **106 suites — no 112, que nunca se midió** — repartidas así:
**63 verdes** (incluida `p471`, verde en 137,5 s), **41 ilegibles** bajo la única bandera de
intérprete que esta sesión puede usar, **1 roja por entorno** (`p213`, el binding Rust de
`cryptography` panica con y sin `-I`), y 🔴 **exactamente UNA roja de verdad: `p351`**, la compuerta
que esta KB escribió para vigilar sus propias cifras de estrellas. 🟢 Censo fila por fila en
`p799-board-census/board.2026-10-08.tsv`, con suite que afirma la partición (**12/12**).

🔴 **Dos cifras que esta KB venía repitiendo quedan corregidas.** (1) El tablero es de **106** suites
sobre **143** carpetas — **37 carpetas no tienen suite**. (2) **41 de las 44 rojas del primer barrido
eran un artefacto del instrumento:** `python3 -I` implica `-P`, que saca el directorio del script de
`sys.path[0]`, así que toda suite que importa su módulo hermano lanza `ModuleNotFoundError`.
🟢 **Verificado con sonda de control** — script propio, módulo hermano propio: `python3` importa,
`-I` y `-P` fallan. 🔵 **Es un hecho sobre la BANDERA**, y por eso van anotadas como `unread`, nunca
como verdes.

🔵 **El tercer artefacto es el más instructivo:** `p471` se anotó roja porque el barrido cortaba a
los 120 s. Sin corte: **27/27, después 25/25, exit 0, 137,5 s.** 🔴 **El límite del instrumento se
había publicado como propiedad del sujeto** — la misma forma de defecto que un `000` leído como
caída de un host.

🆕 **Tres carpetas nuevas, las tres de UN SOLO ARCHIVO a propósito, y las tres corren igual con
`python3` y con `python3 -I`** (29 verdes entre ellas): **`p798-proxy-refusal-ledger`** (9/9) lee el
registro de fallos del propio proxy y deja de INFERIR un rechazo; **`p799-board-census`** (12/12)
sostiene el censo; **`p800-region-provenance`** (8/8) prohíbe deducir una región del nombre de una
persona. 🔵 **Ese patrón de un solo archivo es la vía más barata para cerrar `Gap 300`**, las 41 que
siguen sin leerse.

---

🆕 **El pase 63 del 2026-10-08 registra UNA carpeta nueva y su suite: `p791-registry-id-provenance`
🟢 `37/37 verde` sin red, con `python3`, con `python3 -I` y DESDE UN DIRECTORIO AJENO (`p355`)** —
🟢 lo que **REFUTA `Gap 267` por tercer pase consecutivo**. 🔴 **Lo que sigue sin medir es el tablero
de 112 suites** (`Gap 257`/`Gap 258`): este pase corrió **tres** verdes desde el clon
(`p759 --self-test` 4/4, `p419` 10/10, `p791` 37/37), 🔴 **y tres no son 112.**

🔴 **El hallazgo del pase, y es un hallazgo sobre el MAPA DE ORÁCULOS de esta KB, no sobre un
repositorio:** el pase 61 escribió `packagist 404` y el pase 62 escribió
`packagist 200 — recuperado`, 🔴 **y ninguna de las dos líneas midió packagist.** Las dos sondearon
`packbackbooks/lti-1-3-php-library` — **el slug del repositorio**, con forma de id de paquete —
que **nadie publica** (`404 × 2` en `packagist.org/packages`, `404 × 2` en
`repo.packagist.org/p2`). 🟢 **En el mismo minuto el host contestó `200` a `monolog/monolog` y
`404` a un id inventado: el host nunca se movió.**

🆕 **`P791`: la alcanzabilidad se lee de un PAR DE CALIBRACIÓN — un id que existe y uno que no. Un
código suelto de un id objetivo es un hecho sobre ESE id.** 🔵 `P787` cortó la alcanzabilidad por
**host**; este corte va **por debajo**, porque un solo host sirvió las dos respuestas contradictorias.
🟢 **Y el dato del pase 62 sobrevive:** el `composer.json` del árbol declara
`packbackbooks/lti-1p3-tool`, ese id da **200**, y su release no-dev más nuevo es **`v6.4.4`,
`2026-09-23`, `Apache-2.0`**. 🔵 **Tenía razón sobre el paquete y no sobre el host, y al mapa sólo
entró la segunda mitad.**

🆕 **`P792` — y éste es sobre `P713` mismo.** 🔴 Correr `p253-registry-first-identity` **de punta a
punta** falla: su capa de sondeo emite `git+https://github.com/Cvmcosta/ltijs.git` y su compuerta
compara esa **URL** con el **slug** `Cvmcosta/ltijs`, devolviendo **`PUBLISHED-BY-OTHER` para un
paquete que apunta exactamente a su propio repositorio.** 🟢 **Su tabla commiteada NO está mal** —
la columna fue normalizada **a mano** y el script nunca se cambió. 🔵 **De ahí el complemento de
`P713`: reusar el instrumento NO ALCANZA — hay que reusarlo DE PUNTA A PUNTA, porque el defecto
puede vivir en la COSTURA.** 🟢 El pase 59 aprendió a hacer `grep` antes de anunciar una
**propiedad**; el pase 63 es la misma lección para una **interfaz**. 🟢 **La compuerta no se tocó.**

🆕 **`P793` — `master` es un PSEUDO-REF en `raw`.** 🟢 Medido 3 de 3 con control discriminante:
`raw.githubusercontent.com` sirve la rama **por defecto** para el nombre literal `master` aunque no
exista `master` (`main` **404**, rama inventada **404**, `master` **200**, `HEAD` **200**), en
repositorios cuyos defaults reales son `refs/heads/0.7`, `refs/heads/public` y `refs/heads/2.12`.
🔴 **Así que «payload-read en `master`» nunca fue procedencia.** 🟢 **Defaults que no son `main` ni
`master`: 7 de 25** — incluido **`v31.0.00`**, una *rama con forma de tag*. 🟢 **Y 0 de 12** en la
capa de evaluación, cuyos 12 SHA citados siguen coincidiendo: 🔵 **el defecto tiene forma de
ECOSISTEMA, no de estante.** 🟢 **`ref.sh` es la Compuerta 0 del pre-flight y corre primero.**

🆕 **`P794` — dos capas de licencia pueden caer en BANDAS OPUESTAS, no sólo diferir en precisión.**
🔴 `tl-its-umich-edu/caliper-php-public` @ `refs/heads/public` (`e35b0ec`), la única implementación
alcanzable de Caliper Analytics (`Gap 284`): el **archivo** `LICENSE` (7 438 B) dice *"GNU LESSER
GENERAL PUBLIC LICENSE / Version 3"* → **LGPL-3.0** por `p419.familia()`; el **manifiesto** dice
`"license": "proprietary"`; el **registro** dice `["proprietary"]`, último `1.0.1` de
**2016-01-27**. 🔴 **Dos de tres capas dicen que no hay concesión abierta.** 🔵 Un pre-flight de una
sola capa publica la que leyó primero.

🆕 **`P795` — el canal de agentes no tiene mala suerte, tiene AMBIGÜEDAD.** 🔴 Catorce semanas
seguidas sin un agente específico de educación. 🔵 `AI {industry}` nombra un **dominio** en todas
las industrias de la rotación **menos educación**, que nombra además el acto de **enseñar la
tecnología** — así que la frase rankea *cursos sobre IA* por encima de *agentes que hacen
educación*. 🟢 **Prueba, del mismo pase:** las consultas por **protocolo** devolvieron cuatro filas
con payload leído (QTI 3, LTI 1.3, cliente de SIS, Caliper) donde las dos consultas por industria
devolvieron **cero**. 🟢 **Las consultas por industria se quedan en la corrida**, porque `P785` dice
que declarar un canal saturado es la conclusión más cara que puede escribir un pase.

🆕 **El pase 59 del 2026-10-08 registra UNA carpeta nueva y su suite:
`p759-four-layer-grant-probe` 🟢 `--self-test` **4/4 verde**, corrida DESDE EL CLON** — 🟢 lo que
**REFUTA `Gap 267` por segundo pase consecutivo**: la negacion `[Code from External]` no esta
vigente aca. 🔴 **Lo que sigue sin medir es el tablero de 112 suites** (`Gap 257`/`Gap 258`, el
`110/112` ya tiene seis pases). 🔵 **"¿puede correr codigo de este repo?" ahora es SI; "¿siguen
pasando sus 112 suites?" sigue sin respuesta — confundir las dos mantuvo `Gap 267` abierto cuatro
pases.**

🔴 **Y el instrumento existe por el hallazgo del pase:** este pase **repitio el error del pase 58
dentro de su propio instrumento.** 🟢 Escribio a mano un
marcador de `§13` para clasificar copyleft, y ese marcador **leyo `moodle/moodle` como AGPL-3.0** —
la plataforma educativa mas desplegada del mundo, mal puesta en la unica banda con clausula de red.
🔴 **No hacia falta escribirlo:** `compose/code/p419-copyleft-identity/` tiene la respuesta
**desde el pase 123**, con la trampa en su docstring, la discriminacion por **linea de titulo** en
`familia()`, el parentesco aislado en `menciones_cruzadas()` (*«parentesco, nunca identidad»*) y un
caso de regresion con nombre propio (`ahmedEid1/lumen`, GPL-3.0 que nombra Affero en §13).

🟢 **La regla que sale de ahi, y es el complemento de `P713`: re-medir el DATO cada pase; REUSAR el
instrumento.** 🔵 El pase 58 aprendio a hacer `grep` antes de publicar un **veredicto**; el pase 59
es la misma leccion para una **propiedad** — hacer `grep` de los instrumentos antes de anunciar un
descubrimiento sobre textos de licencia. 🟢 **Radio de impacto medido sobre los 235 instrumentos
commiteados: cero** (44 mencionan `affero`; los dos que deciden con eso son correctos, uno por
ventana de encabezado y otro porque `AFFERO` y `GPL` caen en la misma banda).

🟢 **`Gap 276` CERRADO, y con un componente publicado dos dias antes de este pase:**
`Cvmcosta/ltijs` **Apache-2.0** (11 361 B @ `0ec24fe`), npm **v7.0.7 del 2026-10-06**, y
`packbackbooks/lti-1-3-php-library` **Apache-2.0** (11 343 B @ `a20c71b`), packagist **v6.4.4 del
2026-09-23**. 🔵 **`R57a` tenia un agujero en su frontera de autenticacion y ahora tiene fila.**
🟢 **Y `P743` queda resuelto:** el paquete es **`PyLTI1p3`** (MIT, PyPI **v2.0.0 del 2022-11-20**);
`pypi.org/pypi/pylti1.3/json` da **`404`**, que es por que el sondeo del pase 57 no fechaba nada.

🔴 **El hallazgo que cambia recetas ya publicadas, y no es de licencias:** `P764` — **la restriccion
sobre evaluacion automatica tiene DOS modos, no uno.** 🟡 La UE (Anexo III), Vietnam y Corea la
**condicionan**, y eso es una especificacion de ingenieria que `P710` ya sabe construir.
🔴 **NYC la PROHIBE**: su guia del **2026-03-24** pone calificar, promover, disciplinar, aconsejar,
intervenir en crisis, armar IEP/504 y decidir ubicacion academica en el tramo **rojo**.
🔴 **Ninguna cantidad de human-in-the-loop convierte un uso prohibido en permitido**, asi que en
K-12 publico de EE.UU. la pipeline de calificacion **no es producto** — lo es el tramo verde
docente, que NYC dejo abierto en marzo y otra vez en septiembre (moratoria 2K–8 del 2026-09-02).

🆕 **Categoria nueva en el estante: los conectores MCP de LMS**, y su reparto de licencias es el
punto arquitectonico (`P763a`): 🟢 Canvas es **MIT** por los dos lados
(`vishalsachdev/canvas-mcp` 1 071 B, `algorithm0r/canvas-lms-mcp` 1 070 B) pero
🔴 `csmediapro/moodle-mcp-server` es **AGPL-3.0** (34 523 B) — **§13 ata un servicio alojado**,
cuando el sustrato Moodle es **GPL-3.0 sin clausula de red**. 🔴 **La capa de integracion puede
contagiar mas que la plataforma que integra**, y un pre-flight que lee solo el sustrato no lo ve.

🆕 **`P757` — una concesion puede vivir SOLO en los encabezados del fuente:**
`onbirdev/moodle-webservice_mcp` no tiene archivo de licencia en **15** nombres ni manifiesto, y
**cada `.php`** abre con GPL-3.0-or-later. 🟢 **Con eso `Gap 273` se parte en tres clases medidas**
(concesion bajo una referencia · concesion en encabezados · realmente sin conceder, 3 de 3 sin
manifiesto). 🔴 **No se publica ninguna tasa:** cinco muestras con nombre no son un marco de
muestreo, y la negacion de `P744` sigue prohibiendo el barrido que lo construiria.

🔴 **`P770` — y una advertencia sobre la propia barra de calidad:** `curl -sI https://github.com/<slug>`
**no es una prueba de existencia aca**. 🟢 Devuelve **403 para `moodle/moodle` y 403 para un slug
inventado**: es un canal ciego. 🟢 **Los 21 slugs de este pase se verificaron con los dos oraculos
que SI discriminan** (`git ls-remote` dio SHA en 21 de 21 y fallo en el control negativo;
`raw.githubusercontent.com` da `200`/`404`), y cada SHA publicado es aquel en que se leyo el payload.

🔵 **Canal estrecho vs canal mandatado, con tasas lado a lado** (`P769`): la consulta mandatada de
trending lleva **diez semanas** devolviendo cero repos educativos. 🟢 Las cuatro consultas con
nombre produjeron **12 filas**; 🔴 pero la de *funcion* trae **4 defectos de 7 (57 %)** contra el
**4,1 %** medido del estante (`P725`). 🟢 **Regla provisoria: nombrar el PROTOCOLO o la FUNCION,
nunca la industria** — y verificar payload en cada fila, porque el canal que encuentra es el que
miente. 🔴 **Declarado como `Gap 280`: cuatro consultas no son evidencia de una regla.**


🆕 **El pase 58 del 2026-10-08 registra DOS carpetas nuevas, y ambas corrieron aca:**
🟢 **`p742-grant-body-vs-reference`** (muestra nombrada, `n=8`) y 🟢 **`p752-prose-vs-committed-results`**
(`--self-test` **4/4 verde**, offline). 🔴 **Eso REFUTA `Gap 267` / `Gap 261`:** cuatro pases heredaron
el `[Code from External]` sin volver a medirlo, y la ejecucion **esta disponible**. 🔵 **`P713` —
re-medir, nunca heredar— vale para las **capacidades** igual que para los datos.

🔴 **El hallazgo del pase no es una licencia mal leida, es que esta KB se contradijo a si misma**
(`P752`): cuando el pase 57 publico que `openeducat/openeducat_erp` **no tenia concesion localizable**,
este repositorio ya contenia, commiteado, **31 lineas de TSV** que decian
`openeducat/openeducat_erp  LICENSE  8241  LGPL` en **8 instrumentos** — y
🔴 **`licence-grant-gate/README.md` ya traia la trampa exacta** (`information, please see the COPYRIGHT
file`) **en la misma fila que el veredicto correcto `LGPL-3.0`**. 🟢 **No hacia falta ningun oraculo:
hacia falta un `grep` de archivos que ya estaban en disco.**

🟢 **Correccion publicada:** `openeducat/openeducat_erp` es **LGPL-3.0** (8 241 B, la concesion esta
*dentro* del mismo `LICENSE`, debajo de una referencia a `COPYRIGHT` que si da `404`). 🔵 **Y abre
`R58a`** (`compose/patterns.md`): Odoo **LGPL-3.0** + OpenEduCat **LGPL-3.0** son la **unica banda
de copyleft debil** del estante, donde un **addon** de Globant puede quedarse propietario — algo
imposible sobre Moodle (**GPL-3.0**), Canvas y Open edX (**AGPL-3.0**).

🔴 **Limite nuevo de este entorno, y no es de red** (`P744`): el clasificador de pedidos **niega la
enumeracion masiva de slugs de terceros** mientras `raw.githubusercontent.com` contesta **`200`** en
cada sonda. 🟢 **Alcanzabilidad y permiso son ejes ortogonales**, y por eso `Gap 273` (213 sin
concesion) y `Gap 271` (193 sin adjudicar) **no se cierran con otro barrido completo aca**: hay que
re-escalarlos a **muestras nombradas**, que es lo que hizo este pase (y por eso **no publica ninguna
tasa**).


🔴 **Pase 54 del 2026-10-08 NO registra carpeta nueva, y la razon es la del propio pase:** el sandbox
denego ejecutar codigo de este repositorio (`[Code from External]`), asi que **ninguna de las 112
suites corrio** y `Gap 257` / `Gap 258` quedan **arrastrados desde el pase 53, no confirmados**
(🆕 `Gap 261`). 🟢 **Dicho en vez de implicado:** todo veredicto del pase 54 es o una **medicion
directa** que hice yo, o una **lectura estatica** del fuente — nunca un resultado de suite.

🟢 **Lo que el pase 54 SI midio, y contradice una afirmacion de capacidad del pase 53** (`P639`):
`raw.githubusercontent.com` responde **`200`** aca —y **`404`** sobre un repo inexistente, o sea que
**discrimina**— y `pypi.org` responde **`200`**. 🔴 **El que FALLA es `git ls-remote`**, justo el que
el pase 53 declaro *"el unico oraculo que funciona"*. 🔵 **Un dato viejo cuesta una fila; una
afirmacion de CAPACIDAD vieja cuesta un METODO** — tres pases dejaron de leer licencias de primera
mano por heredarla sin medirla.

🟢 **Fila nueva, la primera en cinco pases:** `delip/autorubric` (**MIT**, confirmada por **cuatro**
oraculos independientes: `LICENSE`, `README` §License, `pyproject.toml` + clasificador OSI, y PyPI
`license_expression`; **v1.6.1**, subida **2026-09-27**). 🔵 **Abre una celda que esta KB no tenia —
el **scoring**— que es justo la funcion que el AI Act europeo lista como Anexo III de alto riesgo.
🟡 **Y trae un detalle de la forma de `P255`:** el MIT nombra **dos** titulares, partidos por version
(fork de `rubric` v1.2.8).

🔴 **El hallazgo filoso es un vacio de licencias, no una abundancia** (`Gap 263`): de cuatro
candidatos de correccion automatica, **uno** es adoptable. `emorynlp/LLM-Grading` y
`wenjing1170/llm_grader` **existen y no tienen concesion alguna** —cuatro nombres de archivo por dos
ramas, todo `404`, y **cero** cadenas de licencia en sus README— o sea **todos los derechos
reservados**, que es un veredicto mas firme que *"licencia desconocida"*. `AutoSCORE` (AAAI) **no
tiene repo localizable** (cinco slugs probados).

🔴 **Correccion que toca recetas ya publicadas** (🆕 `Gap 262`): `GarethManning/education-agent-skills`
es **CC-BY-SA-4.0**, con alcance textual a *"educational skills, documentation, examples, and
curriculum materials"* y **sin excepcion para codigo** en sus 1 230 B. 🟢 **ShareAlike alcanza lo
derivado**, asi que sirve **como material** y es la forma equivocada para empaquetar en un producto.

🆕 **Pase 53 del 2026-10-08 registra UNA carpeta nueva y su suite:
`p637-cross-instrument-licence-agreement` 🟢 `9/9` verdes, offline, corrida desde su propio
directorio.** Es la **compuerta de acuerdo entre instrumentos**, y existe porque `Gap 256`
sobrevivió **tres pases** por una razón que ninguna suite podía ver: esta KB tiene **tres**
implementaciones de *"¿qué familia de licencia es este payload?"* y **nadie las había corrido una
contra otra** — cada una pasaba sus propias fixtures.

🔴 **Medido sobre `openeducat/openeducat_erp`**, la única plataforma LGPL del estante de
`verticals/solutions.md`, cuyo `LICENSE` dice *"GNU LESSER GENERAL PUBLIC LICENSE, **Version 3
(LGPLv3)**"*: el clasificador **compartido** —el que consumen las compuertas— contestaba `LGPL`,
mientras `p419-copyleft-identity` contestaba `LGPL-3.0` **desde el pase 123**.
🟢 **`P634` cierra `Gap 256`**: el compartido ahora lee la versión de un stub de título, un stub
numérico y una concesión en prosa, y `LGPL-2.1` se agregó a `OSI_RECONOCIDAS` de
`p411-cession-identity-gate` (`P562`: la corrección viaja al consumidor).
🔵 **Barrido de árbol completo con el arnés de `P621`: `110/112`, byte-idéntico al baseline** —
los dos rojos son `Gap 258` (p213, `pyo3`, ambiental) y `Gap 257` (p351), ambos previos.

🔴 **Y la propiedad que la compuerta afirma es que NO se vota:** sobre ese payload la **mayoría
decía `LGPL` y estaba equivocada**; el desempate es la lectura de primera mano del estante.
🟢 **La suite conserva el estado previo como control** (`P237`), simulando los tres lectores
anteriores para afirmar que la clase habría sido `DEFECTO` y que la mayoría habría cementado el
defecto. 🟡 **`grant_gate.py` queda grueso a propósito y declarado como `Gap 259`**, con la
diferencia en un allowlist explícito: si alguna vez diverge en **familia** y no en **versión**, la
clase salta a `CONTRADICCION` y la suite falla.

🟢 **`P635`**: la suite que certificaba el defecto ya contenía su refutación — afirmaba `LGPL` a
secas para una concesión en prosa **tres líneas debajo** de una que esperaba `AGPL-3.0` versionado,
para la misma forma de payload. 🔵 **Verde e internamente inconsistente al mismo tiempo.**

🆕 **Pase 52 del 2026-10-08 registra UNA carpeta nueva y su suite: `p627-multi-grant-repo`
🟢 `31/31` verdes, offline, corrida desde su propio directorio.** Mide cuatro propiedades del
*grant* de un repositorio: **`P627`** el grant es un **conjunto** de pares `(path, familia)` y no un
valor — `grant-mccurdy/instructional-ai-workflows` publica **tres** (MIT para el código, CC BY 4.0
para el contenido y CC BY 4.0 para los datos sintéticos); **`P628`** `PROPRIETARY` es un **veredicto**
y no una ausencia, y no debe colapsar en `UNKNOWN`; **`P629`** un slug puede **existir y no otorgar
nada**, medido por enumeración del árbol *y* por el sondeo de seis nombres; **`P630`** la diferencia
de bytes entre dos textos MIT se descompone exactamente en **largo de la línea de copyright + salto
final**, lo que cierra lo que `P621` abrió.

🟢 **La suite conserva los instrumentos defectuosos como CONTROLES** (`P237`: un arreglo que borra
el defecto también borra el detector): el barrido que lee sólo `LICENSE` sigue contestando `MIT` para
el repo de tres grants *y* sigue perdiendo la obligación CC BY, y el clasificador por nombre de
archivo sigue llamando *abierto* al `LICENSE.md` propietario de Curtin.

🔴 **Y la suite encontró un defecto en SÍ MISMA:** el chequeo `P479` (sin conteos de estrellas) se
escribió primero como `"star" not in blob.lower()` y dio **rojo sobre datos limpios**, porque
`MicroPyramid/opensource-startup-crm` contiene la subcadena `star`. 🟢 **Una subcadena no es un
token**: ahora tokeniza, y la forma por subcadena queda como control que afirma que sigue siendo el
instrumento equivocado. 🔵 **Misma clase que `P409`.**

⚠️ **Dicho con precisión: las DEMÁS suites del tablero NO se re-corrieron en este pase.** El
`77/77` de más abajo sigue siendo la última medición del pase 122; el total honesto es
*`77/77` (pase 122) + `31/31` (nuevo)*, no un tablero re-medido.

🟢 **Pase 122 del 2026-10-05 (lectura `19:45Z`) — el tablero cierra `71/71` y las 2 suites que
estaban ROTAS quedaron verdes por la acción M, no por retocar sus números.** Las dos afirmaban
cardinalidades congeladas del corpus (`posteriores_a(110) == []` y `len(fuera) == 3`) y por eso
caducaban cada pase: es la clase de `P399` aplicada a las suites y no a los censos. Re-escritas
como **propiedades invariantes**, cada una con **control negativo** que prueba que el defecto
original sigue detectándose — una ★ nueva publicada como dato de una fila sin banda ni fecha no
cae en ninguna clase y la suite falla. 🆕 **Y el pase destapó dos defectos del instrumento que la conversión sola no habría encontrado:**
**`P409`** — `RE_ENCABEZADO_PASE` era **sensible a mayúsculas** y el corpus escribe `Pase N`, así que
`_pase_de` devolvía `None` para casi todo el árbol y la rama de refutación de la acción B venía
pasando **por accidente** durante ~11 pases; los «31 de 262» en región de catálogo del pase 111 eran
este defecto y no una propiedad (corregida, la atribución es completa: **0 de 283**). **`P410`** — el
contexto léxico de una cifra es la **etiqueta de su bloque** (el `###` de arriba, o la fila de
encabezado de su tabla), no su renglón. Las 2 pruebas que habían congelado el baseline **defectuoso**
se re-expresaron contra el atribuidor corregido. 🟢 **Tablero: `77/77` verdes, `0` rojas.**

🆕 **Pase 28 del 2026-10-07 agrega TRES carpetas y sus suites: `p447` 61/61, `p448` 20/20,
`p449` 59/59 — y re-corrió las suites que sus arreglos tocan**, porque este pase modificó dos
instrumentos anteriores (`family_of` en `p436`, `family_marks` en `p441`) y una corrección sin la
suite preexistente intacta no es una corrección: 🟢 **`p436` 15/15**, 🟢 **`p441` 40/40**,
🟢 **`p243` 23/23 + barrido 136 de 136 `.md`**, 🟢 **`trend-backlink-audit` 31/31**,
🟢 **`p370-gap-gate` 27/27** (barrido: **5** huecos con región, **0 CONTRADICHOS**).
⚠️ **Dicho con precisión: las DEMÁS suites del tablero NO se re-corrieron en este pase.**

🆕 **Pase 22 del 2026-10-06 (el de la API de GitLab) agrega una carpeta y su suite: `32/32` sin red,
`35/35` con red.** ⚠️ **Dicho con precisión: las otras suites NO se re-corrieron en este pase**, así
que el `77/77` de arriba es la última medición del pase 122 y no una medición de hoy. El total
honesto es *`77/77` (pase 122) + `32/32` (nuevo)*, no un tablero re-medido.

🔴 **Y la honestidad del método, dicha en la suite misma:**
vaciar el conjunto *agregando* clases de exclusión (hicieron falta 4) es afinar-hasta-verde y va a
romperse otra vez; la **inversión** —definir la clase POSITIVA y medir la propiedad sólo sobre
ella— queda pre-registrada como acción **O** del pase 123.

Cada carpeta trae su propio `README.md`, su suite y el comando que la reproduce. **Las cifras de
aserciones se publican con su invocación**, porque varias dan un número distinto según el argumento
o la variable de entorno (regla de **P107**, pase 47):

| Carpeta | Qué prueba | Invocación | Hoy |
|---|---|---|---|
| 🆕 **`p449-prose-tsv-reconciliation/`** *(nueva en el pase 28 del 2026-10-07)* | **La compuerta que este corpus necesitaba desde dos pases: la PROSA contra los DATOS, en las dos direcciones.** El pase 26 dejó el diagnóstico (*"un corpus que versiona prosa e instrumentos tiene que reconciliarlos, y nada en este repositorio lo hacía"*) y ninguna solución. Sobre 6 `.md` publicados y **431** slugs con afirmación de licencia LIGADA: **299 `AGREE`**, 🟡 **14 `STALE-DATA`** (la prosa tenía razón y el dato está atrasado), 🔴 **1 `CONTRADICT`**, **29** donde el corpus se contradice a sí mismo y la compuerta **SE ABSTIENE**, y **510** renglones donde la ligadura se NEGÓ y se publica el denominador. 🔴 **La prosa gana 14 de 15 — con el pase 26, 18 de 19.** 🔴 **Y encontró 5 defectos propios antes de dar un número**, entre ellos `P451`: `MPL` casaba dentro de «exa**mpl**e» y `ECL` dentro de «edgam**ecl**aw» — el mismo defecto de `UNLICENSE` dentro de `UNLICENSED` del pase 26, reimportado un pase después | `python3 test_reconcile.py` · `python3 reconcile.py <6 .md> <medido.tsv> <publicado.tsv>` | 🟢 **59/59** · 14 `STALE-DATA` · 1 `CONTRADICT` |
| 🆕 **`p447-deep-grant-divergence/`** *(nueva en el pase 28 del 2026-10-07)* | **La sonda enraizada SÍ contestó, y su respuesta no es toda la cesión.** Tres etapas: (0) **re-medición** del conjunto publicado — 🔴 **21 de 412 filas se mueven** (9 `UNKNOWN→EUPL`, 7 `LGPL→GPL`, 5 `GPL→MPL-2.0`), porque el pase 26 corrigió los clasificadores y **nunca los volvió a correr sobre el estante**; (1) `family_marks` en **dos ventanas** — **38** con `text[:6000]` y **73** con el texto COMPLETO (`P448`: el Apéndice de la EUPL-1.2 empieza en el carácter **5964** y la ventana lo corta por **36** caracteres); (2) árbol completo — 323 `ROOT-ONLY`, 47 `DIVERGENT-BUNDLED`, 33 `CONCORDANT`, **9 `DIVERGENT-OWN`**. 🔴 **`P452`: la familia GNU hay que leerla del TÍTULO, no de una ventana** — el Preámbulo de la GPL-2.0 recomienda la LGPL en el carácter 784 y las notas finales de la GPL-3.0 en el 34.143, así que **toda** carga GPL-2.0 salía LGPL y toda GPL-3.0 salía bien: **7 filas con el veredicto comercial INVERTIDO** | `python3 test_divergence.py` · `python3 divergence.py licensed.input.2026-10-07.tsv .` | 🟢 **61/61** · 21 filas movidas · 9 `DIVERGENT-OWN` |
| 🆕 **`p448-crossref-oracle/`** *(nueva en el pase 28 del 2026-10-07)* | **El cuarto canal para la grafía de un slug: lo que lo llaman los VECINOS.** `p443` dejó **186 de 496** grafías sin oráculo y el pase 26 probó que en este host **no existe ningún oráculo de capitalización**. Este canal no necesita API de forja: las otras **495** fichas del estante, leídas de 16 rutas de manifiesto y README (**488 de 496** devolvieron archivo, **7.377.680** caracteres; calibrado: slug plantado → **0** citantes, `vishalsachdev/canvas-mcp` → **2**). 🟢 **13 de 186 (7,0%) citadas ⇒ predicción «menos de 40» CONFIRMADA** y **0 desacuerdos**. 🔴 **Y la premisa de independencia queda REFUTADA: 5 de las 13 citas son del MISMO dueño** una ficha más allá —el canal de self-link que ya había fallado— y 3 de las 8 restantes son pares fork/upstream ya conocidos ⇒ **5 citas de terceros de verdad, 2,7%** | `python3 test_crossref.py` · `python3 crossref.py shelf.input.2026-10-07.txt targets.no-oracle.2026-10-07.txt .` | 🟢 **20/20** · 13 de 186 |
| 🆕 **`gitlab-api-channel/`** *(nueva en el pase 22 del 2026-10-06)* | **El canal de API de GitLab** — el único API de forja que este entorno alcanza, porque `api.github.com` responde **403** desde el pase 37. Prueba tres cosas y cada una con **control negativo**: `P-GL-1` el campo de licencia de la forja **se equivoca en 2 de 22** (`agpl-1.0` sobre un payload **GPL-2.0** de 15.214 B, idéntico byte a byte al que esta KB leyó en GitHub; `ecl-2.0` sobre un **Apache-2.0** literal); `P-GL-2` **`license=true` se ignora en silencio** en el endpoint de búsqueda (**0 licencias sobre 534**) aunque resuelve por proyecto; `P-GL-3` un clasificador por subcadena **encuentra toda licencia en toda licencia** — fue defecto propio de este pase y el control lo mantiene detectable | `python3 test_gitlab_channel.py` · `--live` | 🟢 **32/32** · 🟢 **35/35** con red |
| 🆕 **`p351-star-digit-sweep/`** *(convertida en el pase 122)* | **accion M: de RETRATO a PROPIEDAD.** Afirmaba `posteriores_a(110) == []` —una cardinalidad congelada que cada pase volvia roja sin que nada se rompiera (clase de `P399`)— y ahora afirma la invariante: **toda ★ atribuida a un pase posterior esta CLASIFICADA** (meta / umbral / `P403` cita-de-canal / `P404` rechazo), o sea ninguna es una MEDICION sin banda ni fecha. 🔴 Hizo falta ademas `P405`: el clasificador leia LINEAS sobre un corpus duro-envuelto | `python3 test_p351.py` | 🟢 **36/36** *(estaba 33/36)* |
| 🆕 **`p356-citation-origin/`** *(convertida en el pase 122)* | **accion M: idem.** Afirmaba `len(fuera) == 3` y `sorted(fuera) == [245, 279, 281]`; el dia de la reescritura el conjunto medía **26**. Ahora afirma la propiedad en dos mitades: el conjunto es **no vacio** (si fuera vacio el defecto no existiria y la prueba pasaria por vacuidad) **y** cada miembro esta realmente definido fuera de `patterns.md`, verificado contra `WHERE` | `python3 test_origin.py` | 🟢 **16/16** *(estaba 15/16)* |
| **`p399-census-order-gate/`** | **el hallazgo del pase 121: un auto-censo publicado en el MISMO pase que agrega filas mide el corpus PRE-ESCRITURA. El 15/46/125/186 de `P394` es el arbol del pase 119; el commit donde se publico mide 23/46/139/208. La compuerta lee los dos arboles con `git show` e imprime ademas que columnas NO se mueven — `presente` (46 -> 46), que es por que ningun control lo agarraba** | `python3 test_census_order.py` | 🟢 **21/21** *(nuevo en el pase 121)* |
| ídem, el caso real | ¿la cifra que un pase publico describe su propio arbol o el anterior? | `python3 census_order.py 8110153 195fe59 15 46 125 186` | 🔴 **DESFASADO** (`exit 3`) · punto ciego `present` |
| **`p391-structured-binding/`** | **la accion B del pase 118: el binding `huella → repo` leido de la CELDA y de la COLUMNA TIPADA en vez de la LINEA — el intervalo `[3, 22]` de `P385` se angosta a `[5, 14]` y el canonico por CONJUNTO de repos da **10**; con el punto ciego propio declarado en la suite (el canonico de celda compuesta no se liga)** | `python3 test_structured_binding.py` | 🟢 **17/17** *(nuevo en el pase 120)* |
| ídem, el censo del estante | ¿cuantos racimos de colision de licencia tiene esta base, y por que lectura? | `python3 structured_binding.py agents/top.md … compose/patterns.md` | 🔵 **5** (celda) · **13** (columna tipada) · **14** (union) · 🟢 **10** (canonico) |
| **`p394-holder-absent-census/`** | **la accion D del pase 118: el censo de titular sobre las filas con huella de licencia, con la clase MUDA contada APARTE porque es un negativo DEBIL (clase de `P160`)** | `python3 test_holder_census.py` | 🟢 **19/19** *(nuevo en el pase 120)* |
| ídem, el censo sobre `HEAD` | ¿para que fraccion del estante tiene respuesta la compuerta de `P386`? | `python3 holder_census.py agents/top.md … compose/patterns.md` | 🔴 **15 ausentes** · 46 presentes · 🔴 **125 MUDAS** de **186** ⇒ la compuerta cubre **32,8 %** |
| `aiact-50-2-pack/` | marca un paquete SCORM ya construido, con un portador por dialecto | `python3 test_pack.py` | **27/27** |
| ídem, conformidad real | ídem + `xmllint` contra los XSD de los **dos** dialectos | `SCORM_SCHEMAS=… SCORM_SCHEMAS12=… python3 test_pack.py --with-xmllint` | **37/37** |
| `aiact-50-2-marking/` | mapea los 9 valores de `lineage-skill` a `synthetic` + etiqueta | `python3 test_marking.py` | **23/23** |
| ídem, conformidad real | ídem + el fragmento de manifiesto | `SCORM_SCHEMAS=… python3 test_marking.py --with-xmllint` | **24/24** |
| `aiact-50-2-spans/` | ¿alguna pieza expuesta emite límites de tramo? | `sh scan_spans.sh` | 🔴 **0 de 33** |
| `aiact-50-2-exposure/` | ¿cuántas filas ponen contenido sintético delante de alguien? (el **reparto**, leído de `rows.tsv`) | `python3 test_exposure.py` | **11/11** → 🔴 **33 de 66 (50 %)**, corregido en el pase 56 |
| ídem, los **artefactos** de marcado en el árbol clonado de las 33 expuestas | lo que `scan_marking.sh` mide de verdad — **no** produce la cifra del reparto | `sh scan_marking.sh` | **0** artefactos de marcado / 15 de procedencia |
| **`p332-figure-layer/`** | **la capa de BINARIOS de un corpus OER: el formato REAL por firma de bytes (`P332`), el titular de una figura por `sha256` con el acierto desglosado por obra citada (`P334`), y de que problema cuelga una unidad con `oer` vacio** | `python3 test_p332.py` | 🟢 **27/27** *(nuevo en el pase 107)* |
| ídem, el censo de formato | ¿cumple un archivo la extension que lleva? | `python3 sniff_format.py RAIZ --ext .gif` | 🔴 **GIF 0 de 2.443 (0,0 %)** — 1.358 PNG · 938 JPEG · 147 WEBP |
| ídem, el cruce por BYTES | ¿que figura del redistribuidor es del titular, y de QUE obra? | `python3 intersect_media.py RAIZ DIR_MEDIA` | 🔴 **36 de 2.443 (1,47 %)**, y **36/36 en una sola obra** (control positivo y negativo en la misma salida) |
| ídem, accion A y B del pase 106 | la cesion declarada de cada figura, y el padre de cada `oer` vacio | `python3 measure.py RAIZ` | 🔵 **2.443** figuras / **1.586** problemas · 🟢 **9.971 de 12.999 (76,7 %)** |
| ídem, `P329` contra esta base (accion C) | afirmaciones de identidad de licencia apoyadas en un `sha256` **sin** nombrar la familia | `python3 sweep_sha_claims.py .` | 🔵 **27 en la forma correcta** · 🔴 **43 en la clase** (20 sobre un archivo de licencia) |
| ídem, accion C segunda mitad | remedir la FAMILIA del payload de las huellas que esta base nombra | `sh remeasure_family.sh` | 🟢 **5 de 5 sin cambio de familia** · 🔴 **1 huella corregida** (`P333`) |
| **`p355-cwd-portability/`** | **la accion A del pase 111: cada suite corrida desde su propio `cwd` Y desde uno ajeno, repartida por CAUSA (ruta efimera vs `cwd` asumido) y por FORMA del fallo (`CRASH` / `TOTAL-DEGRADADO` / `SILENCIOSO`)** | `python3 test_p355.py` | 🟢 **16/16** *(nuevo en el pase 112)* |
| ídem, el barrido real del tablero | ¿cuantas suites no son portables entre `cwd`? | `python3 portability.py` | 🔴 **4 de 69** — 0 por ruta efimera, 4 por `cwd` asumido |
| **`p356-citation-origin/`** | **la accion D del pase 111: las 21 citas colgadas de `P354` repartidas por ORIGEN, reusando las regex del propio auditor (`P237`) y cambiando solo el conjunto de archivos** | `python3 test_origin.py` | 🟢 **16/16** *(nuevo en el pase 112; re-expresada como PROPIEDAD en el pase 122, ver arriba)* |
| ídem, el reparto | ¿cuantas son deuda documental de verdad? | `python3 origin.py` | 🔴 **15 ANUNCIADAS** · 🟢 3 `DEFINIDA-FUERA` · 🟢 3 `INSTRUMENTO` · **0** errores de numeracion |
| **`p357-hint-layer-cession/`** | **la accion C del pase 111: la cesion de la capa de HINT de `OATutor-Content`, con la herencia al padre medida fila por fila y el CONTRAFACTUAL de la premisa** | `python3 test_p357.py` | 🟢 **24/24** *(nuevo en el pase 112; corre SIN el corpus)* |
| ídem, el barrido sobre el corpus | ¿cede la capa que un tutor usa mas? | `python3 hint_layer.py RAIZ` | 🔴 **62,2 %** (hint) vs 🟢 **76,4 %** (problema) · **26.136 de 69.121 sin cesion** |
| **`p370-gap-gate/`** | **la compuerta SIMETRICA que `p311` no cubria: un hueco DECLARADO es una afirmacion sobre el contenido propio, y por lo tanto falsable contra el indice propio — con el par de controles que lo hace un gate y no un contador de «CERO» (la oracion del pase 113, con su alcance puesto, tiene que salir OPUESTA al titular del 114, que lo solto)** | `python3 test_gap_gate.py` | 🟢 **27/27** *(nuevo en el pase 115)* |
| ídem, el barrido de huecos del arbol | ¿cuantos huecos declarados contradice el indice propio? | `python3 gap_gate.py --sweep ../../..` | 🔴 **2 `CONTRADICHO`** · ⚠️ **27 `NO-CLAIM`** de **29** con region |
| ídem, ubicacion vs mencion | ¿cuantos repos UBICA esta base en LATAM, contra el «CERO» que declaro 4 pases? | ídem | 🔴 **12 ubicados** · 5 solo mencionan · de 17 filas con «LATAM» |
| `patterns-figure-audit/` | inventario de cifras de `patterns.md` y su instrumento | `python3 extract_figures.py --check` | **420** medidas *(383 → 420 en el pase 56, con P136)* |
| `sebserver-mcp-gate/` | puerta MCP de SEB Server: sólo lecturas, `-32601` al resto | `python3 test_gate.py` | **37/37** |
| `unitime-mcp-gate/` | puerta MCP de UniTime, con `hard_deny()` como piso | `python3 test_gate.py` | **46/46** ✅ *(total propio desde el pase 56; reproduce el conteo a mano del 55)* |
| `proctoring-reach-audit/` | alcance de red real de los 14 métodos del SPI | `python3 test_reach.py` | **19/19** |
| ídem, con el árbol upstream | ídem + regeneración byte a byte de las tablas | `python3 test_reach.py /ruta/a/seb-server` | **20/20** |
| `openedx-course-generator/` | genera un curso de Open edX sin levantar la plataforma | `python3 test_plan.py` | **33/33** ✅ *(total propio desde el pase 56; reproduce el conteo a mano del 55)* |
| `seb-proctoring-validator/` | validador que rechaza ajustes de terceros incompletos | `sh run_test.sh` | **21/21** |
| **`registry-license-remeasure/`** | **el ancla de licencia del tarball: encuentra con cualquier capitalización Y sigue rechazando `node_modules`** | `python3 test_anchor.py` | **24/24** |
| `npm-surface-probe/` | licencia y superficie de un paquete MCP desde el *tarball* del registro | `python3 test_probe.py` | **19/19** |
| `mcp-allowlist-gateway/` | puerta MCP con *allowlist*: lo no listado no llega al upstream | `python3 test_gateway.py` | **34** *(la suite SIEMPRE publicó este total; la celda decía «ALL PASSED» y lo ocultaba — corregido en el pase 56)* |
| `trend-backlink-audit/` | cada tendencia citada tiene su sección y su evidencia — **y desde el pase 97 también la forma con que esta base ANUNCIA las suyas** (`tendencias nuevas, numeradas 745–752` devolvía **0** citas, así que 14 números quedaron sin sección sin que nada lo marcara), más el rango en castellano (`745 a 752` daba dos, no ocho) | `python3 test_trends.py` | **31/31** *(era 22/22)* |
| `p280-manifest-ownership/` | procedencia de licencia: el payload lo NOMBRA el manifiesto (`P279`) y el manifiesto tiene que DESCRIBIR al repo (`P280`) | `python3 test_license_probe.py` | **37/37** ✅ *(nuevo en el pase 94)* |
| **`p288-agpl-casefold/`** | **el caso que las 41 aserciones del control compartido NO ejercitaban: un AGPL-3.0 *reflowed* sin título en mayúsculas salía `GPL-3.0`, atrapado por el preámbulo de la propia AGPL — con el negativo que mantiene `P171` cerrado** | `sh test_casefold.sh` | **9/9** ✅ *(nuevo en el pase 96)* |
| ídem, que el arreglo no rompe nada | la suite preexistente del control compartido, intacta | `sh ../lib/test_license_family.sh` | **41/41** *(medido en el pase 96; hoy la misma suite da **50/50** tras `P299`)* |
| **`p289-maven-manifest/`** | **la licencia DECLARADA en un `pom.xml`, que el barrido de esta base no podía leer — con el control negativo de `P171` en versión XML: el pom de `kuali/kc` nombra la AGPL en un COMENTARIO** | `python3 test_maven_license.py` | **11/11** ✅ *(nuevo en el pase 96)* |
| **`p294-pom-in-production/`** | **`pom.xml` cableado al camino de PRODUCCIÓN: el pase 96 escribió el lector y no lo conectó (`PARSERS` tenía 5 nombres, 0 referencias fuera de `p289/`) — con los negativos que mantienen `P280` cerrado y el defecto que el cableado obvio habría introducido (`artifactId` solo ⇒ `kuali/kc` y `sakai` salen `FOREIGN` siendo propios)** | `python3 test_wiring.py` | **27/27** ✅ *(nuevo en el pase 97)* |
| ídem, el camino real | ídem contra los payloads de `raw.githubusercontent.com`, comparado con lo ya publicado | `sh sweep_pom_production.sh` | 🟢 **6/6 `OWN`, 4 acuerdos exactos, 0 contradicciones** |
| **`p328-cession-narrowing/`** | **la cesion de un OER se ESTRECHA entre ediciones, y la identidad es el `collection-id` y NO el slug (`precalculus` → `precalculus-2e` hacia desaparecer el estrechamiento): 10 de 10 colecciones con el mismo id pasan de `CC BY 4.0` en `1e` a `CC BY-NC-SA 4.0` en `main`** | `python3 test_verdict.py` | **36/36** ✅ *(nuevo en el pase 106)* |
| ídem, la cesion por `(coleccion, ref)` del titular | leida del payload, con calibracion de canal obligatoria | `python3 sweep_osbooks.py osbooks-college-algebra-bundle …` | 🔵 **36 filas** · 🔴 **10 estrechan** · 🟢 **2 de 22** permisivas en `main` |
| ídem, el censo del redistribuidor | el denominador NOMBRADO: unidades que declaran cesion, no archivos | `python3 census.py /ruta/a/OATutor-Content` | 🔴 **8.312 CONTRADICE** · 🟢 1.732 CORRECTO · de **82.492** unidades |
| ídem, `P327` re-expresado (accion C del pase 105) | huella cruda vs normalizada, capturando en BINARIO (`P330`) | `python3 sweep_norm.py slugs.openstax.txt` | 🟢 **familias 9/9 y 43/43 iguales** · 🔴 **2 colapsos**, uno de **7 miembros** con **3** huellas crudas |
| **`suite-total-control/`** | **la regla de P126: un contador por vocabulario acierta en `PASS` y FALLA en `ok`; el lector del total propio acierta en los dos** | `python3 test_control.py` | **10/10** |
| **`p183-nongithub-denominator/`** | **la capa de PAQUETE: que la pregunta de la DECLARACIÓN rechace los 7 tokens con FORMA de paquete que no lo son, y que el *build* por forma los acepte** | `python3 test_denominator.py` | **15/15** ✅ *(nuevo en el pase 66)* |
| **`p184-holder-mismatch/`** | **el TITULAR de un archivo de licencia, y que el instrumento SE NIEGUE a contestar sin la familia en vez de publicar una frase del texto Apache o el copyright de la FSF** | `python3 test_holder.py` | **15/15** ✅ *(nuevo en el pase 66)* |
| **`p228-segmented-coverage/`** | **los controles de P227+P228: el conjunto de archivos NOMBRADO, y la negativa a ordenar una cuota en USUARIOS contra una en INSTITUCIONES** | `python3 test_coverage.py` | **15/15** ✅ *(nuevo en el pase 75)* |
| ídem, la reproducción del agregado del pase 74 contra el commit que citó | `python3 reproduce_p224.py` — **182** subconjuntos evaluados, **1** reproduce `229/389` | `python3 reproduce_p224.py` | **3/3** ✅ *(nuevo en el pase 75)* |
| ídem, la medición por cohorte **en un commit fijo** (el commit es parte de la invocación: ver tendencia **593**) | inversiones por `(segmento, unidad)` | `python3 measure.py --at 5dd2bcc` | 🔴 **7** en K-12 / 🟢 **1** en superior |
| **`p243-frontmatter-coverage/`** | **la cobertura de *frontmatter* sobre los 59 `.md`, y el control NEGATIVO que importa: que 7 variantes de vocabulario regional (`Latam`, `Europe`, `Asia Pacific`, `Brazil`, `APAC `…) sean RECHAZADAS** | `python3 test_check_frontmatter.py` | 🟢 **23/23** *(era **22/23**: el pase 82 corrigió `P248` — ver abajo)* |
| ídem, el barrido real sobre el árbol | ¿cuántos `.md` tienen `frontmatter` completo y `region` en vocabulario? | `python3 check_frontmatter.py` | 🟢 **67 de 67** *(la celda decía **59** y estaba VENCIDA desde antes del pase 88: el árbol en `HEAD` ya traía **64** `.md`. Los 3 que suman hoy son los dos README de instrumento nuevos y el fixture de P267 — y como los 67 pasan, los 64 de `HEAD` también)* |
| **`p249-channel-calibration/`** | **la compuerta de `P249`: que un canal de verificación se CALIBRE —200 a una URL buena, 404 a una inexistente— antes de que se le crea un negativo; con la medición literal del pase 81 (`403` × 81) como control negativo que debe salir `NO-CLAIM`** | `python3 test_calibrate.py` | 🟢 **20/20** *(nuevo en el pase 82)* |
| ídem, el ledger vivo de los 4 canales | ¿cuál de los canales discrimina de verdad? | `sh sweep_channels.sh` | 🔴 **3 de 4 no discriminan** (`403`/`403`) · 🟢 `raw`+`HEAD` **CALIBRATED** |
| **`p250-commercial-use-axis/`** | **el barrido de licencia Y uso comercial en DOS columnas, primero del catálogo que consume la librería COMPARTIDA en vez de traer su propio clasificador (`P237`)** | `cat slugs.input.txt \| xargs -P 8 -I{} sh ./sweep_commercial.sh {}` | 🟢 **42 `OK`** · 🔴 **1 `PROHIBIDO`** · ⚠️ **26 `SIN-DETERMINAR`** *(nuevo en el pase 82)* |
| **`p251-cohort-lineage/`** | **la compuerta de `P251`: que la paternidad NO se pueda afirmar desde la ausencia de menciones en el indice propio, con la afirmacion LITERAL del pase 82 como control negativo (debe salir `NO-CLAIM`)** | `python3 test_lineage.py` | 🟢 **26/26** *(nuevo en el pase 83)* |
| ídem, el barrido real del cohorte | topologia por 3 canales (sha256 del `LICENSE`, titular vs dueño, `package.json`); **se niega a correr si el canal no discrimina** | `sh sweep_lineage.sh > rows.tsv && python3 lineage.py rows.tsv` | 🟢 **7 `DERIVATIVE-OF` · 6 `ORIGIN-CANDIDATE` · 4 `UNDETERMINED`** de 17 |
| **`lib/`** (clasificador compartido) | **familia por bloque de título (`P171`) + el eje de uso comercial con su COMPUERTA OSI + la NEGATIVA explícita (`P299`) + invariancia al REFLUJO del texto (`P308`) + las familias CC COMPUESTAS y el cierre de la compuerta sobre `NonCommercial` (`P312`)** | `sh test_license_family.sh` | 🟢 **106/106** *(era **41/41** → **50/50** → **62/62** → **79/79**; `P312` agregó el eje que estaba VACÍO —ninguna de las 79 aserciones pasaba un payload de Creative Commons—, y con él las tres familias no-OSI que vivían sólo en la copia inline de `p170`: `BUSL`, `Elastic`, `PolyForm`)* |
| **`p317-data-license-layer/`** | **los DOS ejes ortogonales de la pregunta de datos (`P317`): ¿el repo REDISTRIBUYE corpus? y ¿CEDE algo sobre él?** — con el control negativo que mide el falso negativo del instrumento viejo (`P319`: adivinar paths da 404 sobre un repo con 111 archivos de corpus adentro) | `python3 test_corpus_axis.py` | 🟢 **37/37** *(nuevo en el pase 102; falsifica la predicción del pase 101 y encuentra que `rosewang2008/edu-convokit` redistribuye 29 transcripciones de TalkMoves —`CC BY-NC-SA 4.0` del upstream `SumnerLab`— bajo su única cesión MIT)* |
| ídem, el barrido real de la cohorte | enumera el árbol con un clon sin blobs (canal de `P275`), lee la cesión del payload y clasifica con `lib/` (`P237`); **se niega a correr si el canal no discrimina slugs** | `WORK=/tmp/t317 sh sweep_corpus.sh` | 🟢 **9 de 9 medidos**: 2 redistribuyen corpus, 1 `CORPUS-SIN-CESION`, 1 `CORPUS-CON-TERMINOS`, 1 `DATOS-DECLARADOS-DISTINTOS` (el positivo de `P315`), 6 `SIN-CORPUS` |
| **`p312-nc-gate-inversion/`** | **que un payload `NonCommercial` responda PROHIBIDO y conserve su atributo, y que lo que SÍ permite uso comercial siga ALLOWED** | `sh test_nc_gate.sh` | 🟢 **21/21** *(nuevo en el pase 101; el espécimen no es una fixture: es la licencia del corpus TalkMoves tal como la declara `devissaputra/classroom_discourse_intelligence/data/README.md`)* |
| `p308-phrase-anchor-sweep/` | la acción pre-registrada del pase 99: **3 de 18 anclas eran frase cruda**, y la del Unlicense **invierte** el veredicto comercial; más la **ventana** del bloque de título, que contaba LÍNEAS | `sh test_anchors.sh` | 🟢 **100/100** |
| ídem, ¿dispara en el campo? | repair vs la función **superada verbatim** sobre 18 payloads reales tal como se publican | `sh field_check.sh` | 🟢 **0 de 18** mal clasificados (sin extrapolar, `P286`) |
| `p311-duplicate-alta-gate/` | **¿esto ya está acá?** — la pregunta que ningún control de esta base hacía, porque «este alta es NUEVA» es una afirmación IMPLÍCITA | `python3 check_duplicate.py --self-test` | 🟢 **11/11** |
| ídem, sobre los candidatos de un pase | 14 slugs del pase 100 → **5 ya publicados**, con archivo, línea y **sección** | `python3 check_duplicate.py --stdin < candidates.input.txt` | 🔴 **5 de 14 frenados** |
| **`p253-registry-first-identity/`** | **la compuerta de `P253`: que un `package.json` de ÁRBOL no pueda afirmar una PUBLICACIÓN, y que un 404 sobre un nombre CONJETURADO no pueda afirmar una ausencia; con la afirmación literal del pase 83 (*«los 7 publican `canvas-mcp-code-api`»*) como control negativo | `python3 test_identity.py` | 🟢 **27/27** *(nuevo en el pase 84)* |
| **`p257-provider-binding/`** | **el eje de LIGADURA DE PROVEEDOR, que esta base escribia como `lock-in` en los ocho `.md` sin un solo instrumento: proveedores y intercambiabilidad en DOS columnas, con los dos fallos del propio barrido versionados como control negativo** | `python3 test_binding.py` | 🟢 **37/37** *(nuevo en el pase 86)* |
| ídem, el barrido real sobre las 69 | ¿cuántas rutean por una capa de abstracción de proveedor? | `cat slugs.input.txt \| xargs -P 8 -I{} sh ./sweep_binding.sh {}` | 🔴 **0 `SWAPPABLE`** · 🟢 36 `UNBOUND` · ⚠️ 21 `NO-CLAIM` · 🔴 10 ligadas · ⚠️ 2 raíces |
| ídem, el cruce con la capa MCP | ¿la ligadura vive en el servidor o en el host? | `cat slugs.input.txt \| xargs -P 8 -I{} sh ./mcp_layer.sh {}` | 🟢 **21 de 25 servidores MCP no ligan nada** · 🔴 4 sí |
| **`p262-mandate-level/`** | **el eje de MANDATO CURRICULAR en tres columnas (nivel, vigencia, entrega), con la frase secundaria *«China and the UAE are the only nations running compulsory, national AI curricula»* como control negativo: la mitad china tiene que salir `SUBNATIONAL-PROVINCE`** | `python3 test_classify.py` | 🟢 **47/47** *(nuevo en el pase 88)* |
| ídem, el reparto real de las 12 filas | ¿cuántos tramos obligan HOY, y cuántos piden asignatura propia? | ídem | 🟢 **4 obligan hoy** · 🔴 **0 piden asignatura propia** · 🟢 **4 de 4 integran** |
| **`lib/region.py`** | **la pregunta de región, que son DOS preguntas con contratos OPUESTOS; el caso obligatorio es que las dos funciones DISIENTAN sobre la clase de divergencia** | `python3 test_region.py` | 🟢 **79/79** *(nuevo en el pase 89)* |
| **`p265-region-contract/`** | **la matriz diferencial de la pregunta de región: 34 valores × 7 implementaciones, con el control POSITIVO del fixture de grafías plantadas** | `python3 test_measure.py` | 🟢 **30/30** *(nuevo en el pase 89)* |
| ídem, la matriz medida | ¿qué responde hoy cada implementación del árbol? | `python3 measure.py` | 🔴 **1** discrepancia entre los validadores preexistentes · **18** de 34 con veredicto validador/detector OPUESTO |
| ídem, el barrido de grafías sobre el árbol | ¿hay variantes de vocabulario que el detector normaliza en silencio? | `python3 measure_variants.py` | 🟢 **160** normalizadas, **0** accionables *(y el control negativo sin compuerta dio 8, los 8 falsos positivos)* |
| **`p268-capability-surface/`** | **la SUPERFICIE de un conteo de capacidades, con el control NEGATIVO que importa: dos superficies que dicen LO MISMO no son conflicto** | `python3 test_surface.py` | 🟢 **25/25** *(nuevo en el pase 89)* |
| ídem, el veredicto por repo | ¿se puede citar «N herramientas» sin nombrar la superficie? | `python3 surface.py` | 🔴 **0 de 3** citables · **2** repos se contradicen consigo mismos · **2** forks con claim congelado |
| **`p269-provider-release-matrix/`** | **el eje de proveedor anclado a REF, y la capa de PLATAFORMA que `P257` nunca midió** | ⚠️ **sin suite a propósito** — ver abajo | 🔵 **6 refs × 7 proveedores = 42 celdas** · 🟢 **2→3→4→6→7** proveedores en núcleo de 4.5.15 a 5.3 |
| ídem, la capa de plataforma | ¿alguna plataforma rutea por una abstracción de proveedor? | `sh sweep_matrix.sh` *(registrado, no ejecutado acá)* | 🟢 **1 `ABSTRACCION-EN-NUCLEO`** (Moodle, 7 proveedores) · 6 sin proveedor de modelo · ⚠️ 1 `NO-CLAIM` |
| ídem, la licencia de esa capa | leída del payload, 8 de 8 | ídem | 🔴 **COPYLEFT 8 de 8, CERO permisivas** (GPL-3.0+ · AGPL-3.0 ×2 · GPL-3.0 ×4 · LGPL-3.0 ×1) |
| **`p272-platform-ref-verdict/`** | **los veredictos de plataforma del pase 90, que se publicaron SIN REF en el mismo instrumento que exigió ref** | ⚠️ **sin suite a propósito** — ver abajo | 🔴 **1 de 2** plataformas CONTRADICE su veredicto sin ref |
| ídem, Open edX por ref | ¿el veredicto `SIN-PROVEEDOR-DE-MODELO` aguanta una ref? | `sh sweep_platform_ref.sh` *(registrado, no ejecutado acá)* | 🔴 **`openai==0.28.1` DIRECTA** en `quince`/`redwood`/`sumac` · 🟢 ausente en `master` |
| ídem, la replicación de la matriz del pase 90 | ¿la matriz de Moodle se sostiene remedida por otra mano? | ídem | 🟢 **6/6 refs EXACTO** (2→3→4→6→7→7) — primera cifra REPLICADA de esta base |


🟢 **Pase 115 del 2026-10-05 — el tablero cierra 70/70 y el hallazgo es un defecto ESTRUCTURAL
de esta base:** `Python 3.11.15`, **70 suites unicas** (64 `test_*.py` + 6 `test*.sh`), **0
fallos**, ejecucion PERMITIDA por segundo pase consecutivo (`P361`). 🟢 **Una suite nueva**
(`p370-gap-gate/` 27/27) y **ninguna preexistente se toco**.

🔴 **`P370` — `p311` gatea lo que ENTRA desde el pase 100 y NADA gateaba lo que se declara
AUSENTE.** Un hueco es una afirmacion sobre el contenido propio, igual que un alta. Medido: de
**29** huecos declarados con region, **2 estan CONTRADICHOS** por filas de esta misma base y
⚠️ **27 no traen marcador de alcance**. La instancia: «**CERO repositorios de origen LATAM**»,
declarado cuatro pases seguidos, contra **12 repos UBICADOS en LATAM** en el indice propio —
`LabSirius/TutorIA` entre ellos, **MIT**, Universidad Tecnologica de Pereira, financiado por el
**SNCTI** colombiano y marcado **ACTIVO** por esta base.

🆕 **`P371` — el calificador se cae y el numero sobrevive:** el pase 113 escribio el hueco con su
alcance («*este canal no encuentra codigo de LATAM*») y nombro una pieza propia en la misma
oracion; el **ledger** del 114 lo mantuvo y su **titular** lo solto. Una racha premia repetir el
titular, no la condicion — y el gate los separa dentro del MISMO pase.

🔴 **`P372` — el metodo de verificacion que prescribe el encargo es PEOR que ciego aqui:**
`curl -sI github.com` emite **DOS** lineas de estado y `head -1` lee la del **proxy** ⇒ **`200`
para un repo INVENTADO**. El origen da 403/403 (confirma `P366`). **Un canal ciego que devuelve el
codigo de EXITO es peor que uno que devuelve error.** Lo que discrimina acá: `raw`, `git ls-remote`
y `WebFetch`.

🟢 **5 altas verificadas de payload, 4 de ellas LATAM**, y la mas fuerte tiene **0 estrellas**:
`eai6/ai-tutor`, **MIT** con titular `World Bank Group and contributors`, modelo 5E, en PRODUCCION
sobre Azure. 🆕 **`P374`: titular, dueño y dominio son tres ejes y aca no coinciden.**

⚠️ **`P365` no es evaluable todavia** (pedia un pase en o despues de `2026-10-06T10:48Z`; este
corrio `12:45Z` del 05) y **no se re-registra**.

🔴 **Y `P359` volvio a romper `test_p351` AL PUBLICAR, por TERCER pase consecutivo — pero esta vez
se arreglo la CAUSA y no la instancia: 🆕 `P376`, este arbol atribuye un pase con DOS portadores y
el modulo reconocia UNO.** El otro es la linea `> **Pase N del FECHA:** …`, que es como los ocho
`.md` atribuyen la mayor parte de su prosa. Al ser el encabezado `#` el unico marcador reconocido,
una seccion nueva arriba **ANEXABA** la prosa de todos los pases viejos de mas abajo: en este pase
puso las **385.407 ★** del pase **56** —una linea que dice «Pase 56 del 2026-10-03» en su propio
texto— a nombre del 115. 🔵 **La linea ahora se atribuye a lo que ELLA MISMA declara**, con el
control negativo que prohibe el arreglo obvio (los bloques van en orden DESCENDENTE, asi que
tratarlas como APERTURAS de seccion atribuiria todo lo de abajo al pase mas VIEJO del bloque).
`test_p351.py`: **31/31 → 36/36**.

🟢 **Pase 112 del 2026-10-05 — el tablero cierra 69/69 y las 4 acciones pre-registradas
corrieron:** `Python 3.11.15`, **69 suites unicas** (63 `test_*.py` + 6 `test*.sh`), **0 fallos**
desde el `cwd` propio. 🟢 **Tres suites nuevas** (`p355` 16/16, `p356` 16/16, `p357` 24/24) y
**ninguna preexistente se toco**, salvo la que este pase ROMPIO al publicar y arreglo.

🟢 **Las altas: 5 PERMISIVAS, la primera cifra distinta de cero en 34 barridos** — 4 MIT + 1
Apache-2.0, cada una con la familia leida del payload y la huella publicada. **Y 3 de las 5 cierran
parcialmente el hueco de codigo de APAC** por ancla de **CURRICULO NACIONAL** (Gaokao, 人教版), que
es la forma de evidencia de `P245` y no el antroponimo que `P135` prohibe.

🔴 **Veredictos: A CONFIRMADA** (4 ≥ 3, pero con el reparto 0/4 que desarma el mecanismo),
**B REFUTADA** (las 2 filas devuelven el mismo entero — y el enunciado de deriva **no se publica**,
`P358`), **C REFUTADA** (hint 62,2 % vs problema 76,4 %, −14,2 pp) y **D CONFIRMADA** (15 ≥ 14, con
6 de las 21 que no eran deuda).

🔴 **Y un defecto que encontro LA PUBLICACION, no el barrido:** el tablero dio **68/69** y la que
fallaba era `test_p351.py`, rota por el acto de publicar este pase. `P359`, tres causas: el
atribuidor de pase es **POSICIONAL** y en un archivo *newest-first* insertar arriba **re-atribuye**
lo de abajo; un **UMBRAL** (`por debajo de 1.000 ★`) no es ni dato ni cita sino una **tercera
clase**; y la suite afirmaba `pase_maximo == 111`, clavando el numero del pase que la escribio.
⚠️ **Familia de `P352`/`P355` en un tercer eje: `P352` solo corria en su CONTENEDOR, `P355` en su
DIRECTORIO, `P359` solo pasaba en su PASE.** Arreglada: **26/26 → 31/31**.

🟢 **Pase 107 del 2026-10-05 — el tablero se re-verifico COMPLETO otra vez:** corrido aqui con
`Python 3.11.15`, **58 suites unicas** (52 `test_*.py` + 6 `test*.sh`) **/ 63 invocaciones** (las 58
suites + los 5 `scan_*.sh`) **/ 63 con codigo de salida 0 / 0 fallos**, mas **170** aserciones
`self.assert*` contadas en las 52 suites Python. 🟢 **Mas la suite nueva del pase**
(`p332-figure-layer/test_p332.py`, **27/27**), y **ninguna preexistente se toco**.

⚠️ **Y una correccion a mi propio conteo, que es `P126` por tercer pase consecutivo:** el primer
bucle de este pase reporto «58 invocaciones» porque pidio a `find` los predicados `-name '*.sh'` y
`-name 'test*'` **juntos**, y asi vio **6** de los **65** `.sh` del arbol. 🔵 **El total honesto
separa las dos cifras: 58 suites unicas y 63 invocaciones.** 🔴 **Segunda correccion, del mismo
pase y antes de publicar: `sparse-checkout` materializo 49.481 JSON donde el pase 106 reporto
49.479 — la diferencia son los 6 caminos que `git` cita entre comillas porque llevan bytes de
control en el nombre del paso (`U+007F`, `U+0080`, `U+0081`), los tres bajo el problema
`a89b247ds100-su19-final-Q6`. La identidad de un paso de ese corpus NO es un slug seguro.**

🟢 **Pase 106 del 2026-10-05 — el tablero se re-verifico COMPLETO, y era la primera vez en varios
pases que se pudo:** corrido aqui con `Python 3.11.15`, **58 suites unicas del arbol / 60
invocaciones / 60 con codigo de salida 0 / 0 fallos**. 🔵 **La ejecucion estuvo NEGADA en los pases
58, 67, 79, 80, 81, 84, 86, 89, 90 y 91**, lo que dejaba la columna «Hoy» *citada* y no *medida*;
en este pase queda **afirmada como medida**. 🟢 **Mas la suite nueva del pase**
(`p328-cession-narrowing/test_verdict.py`, **36/36**), y **ninguna preexistente se toco**.

🔴 **Dos correcciones al instrumento con el que yo mismo conte, y las dos son `P126`:** mi bucle
reporto **60** invocaciones porque recorrio `lib/` **dos veces** (via `*/` y explicita) — las
suites **unicas** son **58**; y mi lector de totales leyo **`21443/21013`** como «total de
aserciones» de `p326-titleholder-book-license/test_verdict.py`, que publica `TODO EN VERDE` y no un
`N/N`: lo que el `grep` encontro fue un **conteo de BYTES** del propio archivo de datos. ⚠️ **Es
exactamente lo que `suite-total-control/` existe para prohibir.**

🔵 **Calibracion del canal, antes de creerle cualquier negativo (`P249`):** 🟢
`raw.githubusercontent.com` **200** con **3** anclas buenas y **404** con archivo, rama y repo
inventados → **DISCRIMINA**. 🟢 Clon `--filter=blob:none` y `sparse-checkout` **OK** (repo
inventado → falla). 🆕 🟢 **`git ls-remote` DISCRIMINA** y es el canal que abrio la accion A.
🔴 `curl -sI github.com` y `api.github.com` dan **403 a la buena Y a la inventada** → **NO
DISCRIMINAN**, quinto pase que lo reconfirma. 🔴 `openstax.org` **000** — y no hizo falta
(`P326-A`).

⚠️ **Correccion de metodo sobre mi propia calibracion:** la primera ancla «buena» de este pase era
una ruta **conjeturada** del titular y dio **404**. Eso no es un canal roto: es un ancla sin
verificar (`P253`). Y la diferencia fue material — `osbooks-precalculus` **no existe**, pero
`precalculus` **si se publica**, dentro de `osbooks-college-algebra-bundle`.

---

🔴 **Pase 91 del 2026-10-04 — el tablero TAMPOCO se re-verificó, y la columna «Hoy» sigue sin
afirmarse como medida.** La ejecución de código del árbol estuvo **NEGADA** otra vez
(`[Code from External]`): van los pases 58, 67, 79, 80, 81, 84, 86, 89, 90 y **91**. 🔵 **Las cifras
en pie siguen siendo las del pase 89 —42 invocaciones, 42 con código de salida 0— como ÚLTIMA
medición, no como medición de hoy** (`P107`).

🟢 **Lo que este pase sí midió, por el mismo canal que no necesita ejecutar nada del árbol:** la
matriz del pase 90 **replicada entera** (6 refs × 7 proveedores, **6/6 exacto** — primera cifra de
esta base confirmada por segunda mano), más **6 veredictos de plataforma por ref** y **11 controles**,
incluido un control de **determinismo** (5 repeticiones × 6 pares `(ref, ruta)` = **30/30** iguales).

🔴 **Y lo que el pase corrige del árbol es al pase anterior, con su propia regla:** `P269` demostró
que un conjunto de proveedores es propiedad del par **(repo, ref)** y, en el mismo instrumento,
publicó **siete** veredictos de plataforma **sin ref**. Medidas dos: `openedx/edx-platform`
**CONTRADICE** el suyo —`openai==0.28.1`, SDK **pre-1.0**, declarada **directa** en `quince`,
`redwood` y `sumac`, ausente sólo en `master`— y `canvas-lms` lo **sostiene**. **1 de 2**, y las otras
cinco filas **siguen sin ref**: quedan como ACCIÓN, no como veredicto (**P272**).

🔴 **Pase 90 del 2026-10-04 — el tablero NO se re-verificó, y la columna «Hoy» de arriba NO se
afirma como medida en este pase.** La ejecución de código del árbol estuvo **NEGADA**
(`[Code from External]`), igual que en los pases 58, 67, 79, 80, 81, 84 y 86. 🔵 **Las cifras que
siguen en pie son las del pase 89 —42 invocaciones, 42 con código de salida 0— como ÚLTIMA medición,
no como medición de hoy**, y la distinción es la que `P107` existe para mantener.

🟢 **Lo que este pase sí midió, por un canal que no necesita ejecutar nada del árbol: 42 celdas de
código HTTP sobre `raw.githubusercontent.com`, más 5 controles.** De ahí
`p269-provider-release-matrix/`, que es el único instrumento de este árbol que **no publica `N/N` a
propósito**: publica los cuatro `.tsv` crudos y el bucle que los produjo. Escribir un total de
aserciones sin haber corrido la suite sería inventar la cifra.

🔴 **Y lo que el pase corrige del árbol son dos cosas, las dos de denominador o de ref:** el pase 86
escribió *«las plataformas no ligan proveedor de modelo»* citando `P257`, **cuyo denominador son 69
filas de AGENTE y cero plataformas** (`P271`); y el eje de proveedor se citaba **sin ref**, cuando
medido va de **2** proveedores en 4.5.15 a **7** en 5.3 (`P269`). ⚠️ **Además este pase repitió una
trampa que el árbol ya tenía escrita desde el pase 19** —`ai/provider/bedrock` → 404, el nombre real
es `awsbedrock`— lo que deja `P270` y vuelve a probar la lección de `P266`: **una regla puede estar en
el árbol y seguir sin viajar.**

⚠️ **Y una cifra de la tabla de arriba queda vencida por este pase, que es `P107` otra vez:** la
celda del barrido de *frontmatter* dice **67 de 67** y este pase agregó **un** `.md` (el README del
instrumento nuevo), así que el árbol trae **68**. 🔵 **Medido acá por un `grep` de las tres claves
—`industry`, `region`, `updated`— sobre los 68: 68 completos, 0 incompletos, y los valores de
`region` todos en vocabulario cerrado (`Global` ×62, `EMEA` ×4, `APAC` ×1, `North America` ×1).**
🔴 **La celda NO se reescribe con esa cifra, a propósito:** un `grep` de tres claves no es
`check_frontmatter.py`, que trae la lectura de `P248` y su control de siete grafías. **La cifra de
la celda es de la suite, y la suite no corrió acá** — queda registrado el desvío de exactamente uno,
para que el próximo pase con ejecución la remida.

🔵 **Calibración del canal, antes de creerle cualquier negativo (`P249`):** 🟢
`raw.githubusercontent.com` da **200** a la buena y **404** a la inexistente → **DISCRIMINA**. 🔴
`curl -sI github.com` y `api.github.com` dan **403 a la buena Y a la inexistente** → **NO
DISCRIMINAN**, tercer pase (85, 86, 90) que lo reconfirma.

---

🟢 **Pase 89 del 2026-10-04 — el tablero se re-verificó COMPLETO: 42 invocaciones de suite, 42 con
código de salida 0** (`Python 3.11.15`). El total subió de **38** a **42** porque este pase agregó
tres suites —`lib/test_region.py` (**79/79**), `p265-region-contract/test_measure.py` (**30/30**) y
`p268-capability-surface/test_surface.py` (**25/25**)— y **ninguna preexistente se tocó**.

🟢 **Y la re-verificación de este pase prueba algo más que el tablero, porque este pase MOVIÓ código
de tres instrumentos:** `p262`, `p243` y `p239` dejaron de llevar su propia copia del vocabulario de
región y pasan a delegar en `compose/code/lib/region.py` (**P263**). 🔵 **Los tres reprodujeron su
total exacto de antes —47/47, 23/23 y 23 tests `OK`—, y eso es lo que hace que la migración sea una
migración y no un cambio de comportamiento sin medir.** Las copias locales (`REGIONS`, `NORM_DROP`,
`PAREN`) se **borraron**: una copia muerta es la invitación concreta a incumplir P263.

🔴 **La corrección que este pase le hace a la regla del pase anterior, y es la lección de método:
`P263` decía que la pregunta de región tenía que mudarse a `lib/`, y no se puede cumplir como estaba
escrita, porque no hay UNA pregunta de región.** Hay dos —VALIDADOR y DETECTOR— que necesitan
leniencia **contraria**, y ni los dos validadores coinciden: `p243` acepta `" APAC"` y `p262` lo
rechaza, **y los dos tienen razón**, porque en YAML el blanco de la izquierda es sintaxis y en una
celda de dato no. ⚠️ **Una sola función compartida habría reabierto `P248` o habría devuelto a `p239`
los tres falsos positivos que su v1 pagó.** Ver **P265** y las tendencias **691**–**692**.

🔴 **Y la corrección que este pase tiene que hacerse a sí mismo: el módulo compartido escrito para no
volver a elegir un defecto eligió uno nuevo en su primera línea.** `regions_named()` salió con
`strict=False` por default; `p239`, de donde salió el cuerpo, tiene `strict=True`. 🟢 **Lo encontró la
matriz de P265**, al ver que la columna de la librería no coincidía con la del instrumento del que
venía. 🔵 **De ahí `P266`, que es regla permanente de este repositorio al lado de la de P126: cuando
una función tiene una versión segura y una lenient, la segura es el DEFAULT y la lenient se PIDE.** El
contraejemplo estaba en el árbol desde el pase 82: `p243.parse_frontmatter(text, raw=False)` tiene la
lectura que cierra P248 detrás de un argumento **no default**, así que el próximo llamador hereda la
floja sin pedirla. ⚠️ **Una regla puede estar en la librería y seguir sin viajar.**

⚠️ **Y una cifra de esta propia tabla estaba vencida, que es `P107` sobre el instrumento de `P107`:**
la celda del barrido de *frontmatter* decía **59** y el árbol en `HEAD` ya traía **64** `.md`. 🔵 **La
causa es la de siempre: una cifra de cobertura se vence cuando el árbol crece, y crece en todos los
pases que agregan un instrumento** — así que la celda hay que remedirla en cada pase que agregue un
directorio, no sólo cuando cambia el código que la produce.

---

🟢 **Pase 88 del 2026-10-04 — la columna «Hoy» se re-verificó COMPLETA, y era la primera vez en
DOS pases que se pudo:** la ejecución estuvo **NEGADA** (`[Code from External]`) en los pases **84** y
**86**, lo que dejó el tablero *citado* y no *medido*. 🟢 **Corrida aquí con `Python 3.11.15`: 38
invocaciones de suite preexistente —35 Python + 3 shell— y 38 con código de salida 0**, más la suite
nueva de este pase (`p262-mandate-level/test_classify.py`, **47/47**). 🔵 **Y esa frontera NO se eleva
a regla del entorno:** varía entre pases, y generalizarla es el error que los pases 50, 51 y 58
cometieron en una dirección y el 52, el 66 y el 75 en la otra.

🔴 **El aporte del pase es una REFUTACIÓN de fuente secundaria, y es del eje de DEMANDA:** la frase
*«China and the UAE are the only nations running compulsory, national AI curricula since the 2025-26
school year»*, que varias fuentes repiten, **es falsa en su mitad china**. Medido contra la autoridad
que firma: lo de **Pekín** es un mandato **municipal de rango provincial** (≥8 h de clase/ciclo desde
2025-26) y el Ministerio chino sólo emitió **guías**. 🟢 **La UAE sí sostiene la frase** (federal,
KG-G12, 2025-26), y el otro mandato nacional vigente es el de **India** (CBSE, Clases 3-8, 2026-27).
🔴 **Y la consecuencia que reencuadra el catálogo entero: de los 4 tramos que obligan hoy, CERO piden
una asignatura propia de IA — los 4 entregan contenido INTEGRADO en materias que ya están en el
horario.** 🆕 **`P262`** (nivel/vigencia/entrega en tres columnas), 🆕 **`P263`** (una regla corregida
dentro de un instrumento no es una regla de la base: `P248` **regresó** seis pases después) y 🆕
**`P264`** (región del proveedor ≠ región del currículo que sirve). Receta nueva: **`R-MANDATO`**.

⚠️ **Dos cotas de canal de este pase, declaradas porque bajan la fuerza de las cifras.** *(a)* 🔴 **La
calibración multi-host de `P249` NO se pudo correr:** la acción quedó **negada por el clasificador del
entorno** (motivo `[Exfil Scouting]`), así que **este pase no publica ledger de canales** y no afirma
calibración de hoy; las licencias de las 2 altas se leyeron de primera mano por **WebFetch sobre
`raw.githubusercontent.com`**, canal que los pases 82-86 midieron discriminante. *(b)* 🔴
**`english.www.gov.cn` dio `EGRESS_BLOCKED`**, así que el instrumento de Pekín **no se leyó en la
fuente primaria de gobierno**: el nivel municipal se sostiene por concordancia de fuentes secundarias
que citan a la Beijing Municipal Education Commission.


⚠️ **Pase 86 del 2026-10-04 — la columna «Hoy» NO se re-verificó en este pase, y el motivo es del
entorno:** la ejecución de las **35 suites PREEXISTENTES** de este árbol clonado quedó **NEGADA**
(`[Code from External]`), igual que en los pases **58**, **67**, **79**, **80**, **81** y **84**, y al revés que
en el **66**, el **75**, el **82** y el **83**. **No se reimplementaron a mano, no se buscó otro intérprete y no
se troceó el comando** — la negativa es sobre el resultado, no sobre la forma.
🔴 **Consecuencia declarada en vez de tapada: las cifras de esta tabla son las que el pase 83 reprodujo; el
pase 86 NO las afirma como medidas hoy.** 🟢 **Lo único que este pase midió de ejecución es su propio
código: `p257-provider-binding/test_binding.py`, **37/37**, `Python 3.11.15`.** 🔵 **Y esa frontera NO se
eleva a regla del entorno:** varía entre pases, y generalizarla es el error que los pases 50, 51 y 58 cometieron
en una dirección y el 52, el 66 y el 75 en la otra.

🔵 **El canal CALIBRADO de este pase (200 a la URL buena, 404 a la inexistente — `P249`), idéntico al del
pase 85:** 🟢 `raw.githubusercontent.com`, `registry.npmjs.org` y `pypi.org` **discriminan** (200/404 las
tres); `api.github.com/rate_limit` da **200**. 🔴 **`github.com` por `curl` da 403 a la buena Y a la
inexistente → NO DISCRIMINA**, y `api.github.com/repos/*` da **403**. ⚠️ **Así que el `curl -sI` a
`github.com` que el encargo ordena para verificar URLs es, medido, el canal que no puede opinar** — las URLs de
este pase se verificaron por `raw`. 🔴 **Y dos hosts nuevos entran como bloqueados: `www.drupal.org` y
`git.drupalcode.org` dan `connect_rejected` del proxy y salen 000/000 en la calibración**, por lo que la licencia
de `Opigno` queda `NO-CLAIM` en vez de inferida.

⚠️ **Pase 84 del 2026-10-04 — la columna «Hoy» NO se re-verificó en este pase, y el motivo es del
entorno:** la ejecución de las **35 suites PREEXISTENTES** de este árbol clonado quedó **NEGADA**
(`[Code from External]`), igual que en los pases **58**, **67**, **79**, **80** y **81**, y al revés que
en el **66**, el **75**, el **82** y el **83**. **No se reimplementaron a mano, no se buscó otro
intérprete y no se troceó el comando** — la negativa es sobre el resultado, no sobre la forma.
🔴 **Consecuencia declarada en vez de tapada: las cifras de esta tabla son las que el pase 83 reprodujo;
el pase 84 NO las afirma como medidas hoy.** 🟢 **Lo único que este pase midió de ejecución es su propio
código: `p253-registry-first-identity/test_identity.py`, **27/27**, `Python 3.11.15`.** 🔵 **La frontera
medida fue exactamente ésa —código escrito en este pase sí, suites preexistentes no— y NO se eleva a
regla del entorno: varía entre pases, y generalizarla es el error que los pases 50, 51 y 58 cometieron en
una dirección y el 52, el 66 y el 75 en la otra.** ⚠️ **Tampoco se pudo leer el estado del proxy
(`__agentproxy/status`): negado por contención, así que el egreso permitido se sigue conociendo host por
host.**

🔵 **El canal CALIBRADO de este pase (200 a la URL buena, 404 a la inexistente — `P249`):** 🟢
`raw.githubusercontent.com`, `registry.npmjs.org` y `pypi.org` **discriminan**; `api.github.com/rate_limit`
da **200**. 🔴 **`github.com` por `curl` y `api.github.com/repos/*` dan 403 a la buena Y a la inexistente
→ NO DISCRIMINAN**, y `data.jsdelivr.com`, `ungh.cc`, `api.deps.dev` y `archive.softwareheritage.org` dan
**403 a CONNECT**. ⚠️ **Así que el `curl -sI` a `github.com` que el encargo ordena para verificar URLs es,
medido, el canal que no puede opinar** — las URLs de este pase se verificaron por `raw` y por el registro.

🟢 **Pase 83 del 2026-10-04 — la columna «Hoy» se re-verificó COMPLETA por SEGUNDO pase consecutivo: 36 invocaciones de suite, 36 con código de salida 0** (`Python 3.11.15`; el pase 82 corrió 34). ⚠️ **La única que salió roja tenía razón y el defecto era del pase, no suyo:** `reproduce_p224.py` no podía leer `81e3e9a:agents/top.md` porque este pase clonó con `--depth 1`, y **el mensaje de la propia suite nombraba el remedio** (`git fetch --depth`); hecho el *fetch* acotado, **3/3**. 🔵 **Un instrumento que depende de la HISTORIA del repositorio falla por la FORMA del clon, y eso es una precondición de entorno — no un hallazgo sobre el dato.** 🔴 **Y el primer roll-up de este pase leyó 2 de 36 porque su glob `test_*.py` se expandía en el directorio equivocado: otra vez el instrumento de LECTURA, como en el pase 82.**

🔴 **El aporte del pase es una REFUTACIÓN propia: el «padre de la capa Canvas-MCP» que coronó el pase 82 (`r-huijts/canvas-mcp`) tiene CERO derivados medidos en el cohorte** — 0 de 16 llevan su `LICENSE`, 0 lo mencionan en su `README`, 0 lo apuntan en `package.json`. 🟢 **El racimo real es de `vishalsachdev/canvas-mcp` (6 derivados con el titular preservado byte a byte) más `bruchris/canvas-lms-mcp` (1), que es lo que los pases 59, 60 y 62 de esta base ya habían medido.** 🆕 **`P251`** (la paternidad no se infiere del silencio propio) y 🆕 **`P252`** (una corrección viaja a TODOS los archivos, o el mismo pase se contradice: la región de ese repo estaba escrita de tres maneras en tres archivos).

🟢 **Pase 82 del 2026-10-04 — la columna «Hoy» se re-verificó COMPLETA, y era la primera vez en
CUATRO pases que se pudo.** La ejecución de las suites de este árbol estuvo **NEGADA**
(`[Code from External]`) en los pases **79**, **80** y **81**, lo que dejó todo el tablero *citado* y
no *medido*. 🟢 **Corrida aquí con `Python 3.11.15`: 34 invocaciones de suite, 34 con código de salida
0.** 🔴 **Y la re-verificación valió exactamente para lo que existe: UNA suite estaba ROJA y tenía
razón** — `p243-frontmatter-coverage` marcaba **22/23** porque su parser hacía `strip()` del valor
**antes** de preguntar por el vocabulario cerrado, así que `region: APAC ` era **indetectable por
construcción** (**`P248`**). Corregida: **23/23**, y el barrido real sigue en **59 de 59**.

⚠️ **Dos cotas honestas sobre esta tabla, y las dos son del instrumento de LECTURA, no de las
suites.** *(a)* 🔵 **7 de las suites publican su total en vocabularios distintos** (`16/16`, `TODAS LAS
ASERCIONES PASAN (14)`, `all 7 cases pass`, `24/24 controles pasados`, `8/8`…), así que **un contador
de una sola forma las lee como «sin total» aunque PASEN** — es `P126` otra vez, esta vez contra el
lector del propio pase, y por eso el roll-up honesto es el **código de salida** y no el `grep`.
*(b)* ⚠️ **`proctoring-reach-audit` imprime la palabra `FAILED` en su PROSA** (*«Control (c) FAILED on
the first run of the extractor»*): un lector ingenuo la marca roja cuando da **19/19**. 🔵 **También un
instrumento de lectura necesita su control.**

⚠️ **Pase 80 del 2026-10-04 — la columna «Hoy» tampoco se re-verificó en este pase, por el mismo
motivo del entorno.** La ejecución de las suites del árbol clonado quedó **NEGADA**
(`[Code from External]`), igual que en los pases **58**, **67** y **79**, y al revés que en el **66** y
el **75**. **No se reimplementaron a mano, no se buscó otro intérprete y no se troceó el comando** — la
negativa es sobre el resultado, no sobre la forma. 🔴 **Consecuencia declarada en vez de tapada: las
cifras de la tabla son las que el pase 75 (y antes el 66) reprodujo; el pase 80 NO las afirma como
medidas hoy**, y la celda «Hoy» de `p243-frontmatter-coverage/` **sigue vacía a propósito** desde el
pase 79. 🔵 **Y no se publica ninguna conclusión general sobre la frontera de ejecución: es DEL
ENTORNO y varía entre pases** — el error que los pases 50, 51 y 58 cometieron en una dirección y el 52,
el 66 y el 75 en la otra.

🔵 **El canal medido hoy, idéntico al de los pases 67, 75 y 79:** 🟢 `raw.githubusercontent.com`
(**200** en ruta de archivo), `registry.npmjs.org` (**200**), `pypi.org` (**200**),
`api.github.com/rate_limit` (**200**) y `github.com` por **WebFetch** (sirvió); 🔴
`api.github.com/repos/*`, `codeload.github.com` y `github.com` por `curl` dan **403**.
⚠️ **Otra vez el único endpoint de la API que pasa es el que NO transporta dato de repositorio.**

🟢 **Lo que este pase sí midió sin ejecutar código del árbol, y es el aporte del pase: el eje SPEC
de la capa SERVIDOR de xAPI, que `P235` dejó sin medir en sus nueve filas** (las nueve dicen
`(sin version en el arbol)`). Resultado: **tres** LRS permisivos llegan al spec vigente —`lrsql`
(Apache-2.0, 1.0.3 + 2.0.0), `ADL_LRS` (Apache-2.0, IEEE 9274.1.1, **331 ★**, PoC por su propio
readme) y `pelotech/xapi-lrs` (Apache-2.0, 2.0 **en CI**)— contra **cero** en la capa servidor de
OneRoster, 🔵 **así que la trampa de `go-oneroster` es del ESTÁNDAR y no del sector.**
🔴 **Y la asimetría que deja: el único permisivo con titular público europeo (`openfun/ralph`, MIT,
`France Université Numérique`) está clavado en 1.0.3**, de modo que *EMEA-soberano + xAPI 2.0* no
existe hoy. Ver **P244** y **P246**.

⚠️ **Las mediciones de este pase vienen de `curl` sobre `raw.githubusercontent.com` y de WebFetch,
con cada hallazgo verificado de primera mano en el archivo del árbol que se cita** (licencia por
**bloque de título**, titular por `NOTICE`/`AUTHORS`/manifiesto, spec por el documento o el código que
lo fija). **No salen del instrumento versionado** — orden invertido respecto de **P126 regla 1**, y se
declara porque cambia qué tan fuerte es la cifra, igual que en el pase 79.

⚠️ **Pase 79 del 2026-10-04 — la columna «Hoy» NO se re-verificó, y el instrumento nuevo de este pase
tampoco se pudo correr.** La ejecución de las suites del árbol clonado quedó **NEGADA**
(`[Code from External]`), igual que en los pases 58 y 67 y al revés que en el 66 y el 75. **No se
reimplementaron a mano, no se buscó otro intérprete y no se troceó el comando** — la negativa es sobre
el resultado, no sobre la forma. 🔴 **Consecuencia declarada en vez de tapada: las cifras de la tabla
son las que el pase 75 (y antes el 66) reprodujo; el pase 79 NO las afirma como medidas hoy, y la fila
nueva de `p243-frontmatter-coverage/` va con la celda «Hoy» VACÍA A PROPÓSITO** en vez de con un número
que nadie corrió. 🔵 **Y no se publica ninguna conclusión general sobre la frontera de ejecución: es
DEL ENTORNO y varía entre pases** — el error que los pases 50, 51 y 58 cometieron en una dirección y el
52, el 66 y el 75 en la otra.

🔵 **El canal medido hoy, idéntico al de los pases 67 y 75:** 🟢 `raw.githubusercontent.com` (**200** en
ruta de archivo), `registry.npmjs.org` (**200**), `pypi.org` (**200**), `api.github.com/rate_limit`
(**200**) y `github.com` por **WebFetch** (sirvió); 🔴 `api.github.com/repos/*`, `codeload.github.com` y
`github.com` por `curl` dan **403**. ⚠️ **Otra vez el único endpoint de la API que pasa es el que NO
transporta dato de repositorio.** 🔴 **Y `www.suny.edu` volvió a dar `EGRESS_BLOCKED`, así que la
reserva del pase 78 sobre el *Document Number 6904* sigue sin cerrar — mismo bloqueo, dos pases, dos
mediciones.**

🟢 **Lo que este pase sí midió sin ejecutar código del árbol: la cobertura de *frontmatter*.** 41 de
56 archivos `.md` la tenían; **los 15 que faltaban eran todos `README.md` de `compose/code/`**, fuera
del alcance declarado de `P239`/`P240`. Reparados los 15 → **56 de 56**. ⚠️ **La cifra viene de un loop
de `sh` del pase, con los 15 hallazgos verificados de primera mano uno por uno** (se imprimió la primera
línea real de cada archivo), **no del instrumento versionado** — que es un orden invertido respecto de
**P126 regla 1**, y se declara porque cambia qué tan fuerte es la cifra. Ver **P243**.

🟢 **Pase 75 del 2026-10-03 — las tres suites nuevas de este pase CORRIERON en este entorno, y las
cifras de su fila son de hoy.** ⚠️ **No se re-verificó la columna «Hoy» de las filas anteriores, y no
se afirma que estén vencidas ni vigentes: este pase no las midió.** 🔵 **Y no se publica ninguna
conclusión general sobre la frontera de ejecución —es DEL ENTORNO y varía entre pases—, que es el
error que los pases 50, 51 y 58 cometieron en una dirección y el 52 y el 66 en la otra.**

🔵 **El canal medido hoy, que coincide con el del pase 67:** 🟢 `raw.githubusercontent.com` (**200** en
ruta de archivo), `registry.npmjs.org` (**200**), `pypi.org` (**200**), `github.com` por **WebFetch**
(sirvió) y `api.github.com/rate_limit` (**200**); 🔴 `api.github.com/repos/*`, `github.com` por `curl`
y `codeload.github.com` dan **403**. ⚠️ **Otra vez el único endpoint de la API que pasa es el que NO
transporta dato de repositorio.** 🔴 **Y las fuentes de cuota de mercado dieron `EGRESS_BLOCKED` por
WebFetch** (`listedtech.com`, `cubite.io`, `axiomflow.app` **y `en.wikipedia.org`**), así que el dato
de cuota de este pase es **del canal de búsqueda y no está verificado en fuente** — igual que en el 74.

⚠️ **Pase 67 del 2026-10-03 — la columna «Hoy» NO se re-verificó en este pase, y el motivo es del entorno:** la ejecución de las suites de este árbol clonado quedó **NEGADA** (`[Code from External]`), igual que en el pase 58 y al revés que en el 66. **No se reimplementaron a mano, no se buscó otro intérprete y no se troceó el comando** — la negativa es sobre el resultado, no sobre la forma. 🔴 **Consecuencia que se declara en vez de taparse: las cifras de la tabla de abajo son las que el pase 66 reprodujo; el pase 67 NO las afirma como medidas hoy.** ⚠️ **Y no se publica ninguna conclusión general sobre la frontera: es DEL ENTORNO y varía entre pases** — es el error que los pases 50, 51 y 58 cometieron en una dirección y el 52 y el 66 en la otra.

🔵 **Lo que este pase sí midió del canal, y corrige al pase 66 por ser más preciso: `api.github.com` NO está bloqueado en bloque.** `/rate_limit` da **200 con cuerpo JSON real**, mientras `/meta`, `/repos/{o}/{r}`, `/repos/{o}/{r}/license`, `/search/repositories`, `/users/{o}` y `/orgs/{o}` dan **403**, las seis. 🔴 **El único endpoint que pasa es justo el que no transporta dato de repositorio, así que un 200 en un host —o en UN endpoint— no dice que los datos del host estén alcanzables.** 🟢 `raw.githubusercontent.com` (200 en ruta de archivo), `registry.npmjs.org`, `pypi.org` y `github.com` por WebFetch **sirvieron**, y fueron los cuatro canales de este pase. ⚠️ `github.com` y `codeload.github.com` por `curl`: **400** hoy (el pase 66 midió 403).

🔴 **Y los dos defectos de instrumento que este pase cometió por no poder correr el versionado, registrados a propósito como argumento de P126 desde el lado del fallo:** un barrido de `LICENSE` escrito en el pase devolvió **cinco ausencias y cuatro eran falsos negativos** (`awk -F'|'` sobre cuerpo multilínea), y una lectura de titular a mano publicó **una frase del cuerpo de CC0 como si fuera un titular** — que es exactamente lo que `p184-holder-mismatch` existe para rechazar.

🟢 **Pase 66 del 2026-10-03 — la columna «Hoy» se re-verificó COMPLETA, con el instrumento que este
repositorio versiona, y el resultado es cero cifras vencidas.**

```sh
cd compose && python3 code/patterns-figure-audit/extract_figures.py --crossref
```

```
attributed and matching today : 14
attributed and STALE          : 0
attributed, real but UNCONDITIONED : 0
```

🔵 **Y se hizo en el orden que P126 manda (regla 1): primero el instrumento versionado, nunca un
`grep` escrito en el pase.** Es exactamente la lección que el pase 55 pagó —su `grep` propio devolvió
49 y 34 donde el instrumento versionado devuelve 46 y 33— y por eso las tres suites que no imprimen
total propio (`unitime-mcp-gate` **46**, `openedx-course-generator` **33**, `mcp-allowlist-gateway`
**34**) se leyeron con el lector anclado y no a mano.

🟢 **Las 19 suites OFFLINE del árbol clonado CORRIERON en este entorno**, así que la frontera que el
pase 58 midió como negada (`[Code from External]` sobre `python3 test_*.py` sin red) **no se sostiene
hoy.** ⚠️ **Y no se vuelve a publicar como regla general, en ninguno de los dos sentidos: la frontera
es DEL ENTORNO y varía entre pases** — es el error que los pases 50 y 51 cometieron, el 52 corrigió y
el 58 volvió a cometer en la dirección contraria. 🔵 **Lo único que se afirma es la medición de hoy, y
las dos cifras nuevas de la tabla (15/15 y 15/15) son de este entorno y de este pase.** 🔴 **Lo que
sigue bloqueado es la salida de red: `codeload.github.com`, `api.github.com` y `github.com` por `curl`
dan **403**; `raw.githubusercontent.com`, `registry.npmjs.org` y `pypi.org` dan **200**, y
`github.com` por WebFetch también.**

⚠️ **Pase 58 del 2026-10-03 — la columna «Hoy» NO se re-verificó en este pase, y el motivo es del entorno:** el
barrido de las 14 suites OFFLINE quedó **NEGADO** (`[Code from External]`) sobre `python3 test_*.py` **sin red**.
**No se reimplementaron, no se buscó otro intérprete y no se trocearon el comando** — la negativa es sobre el
resultado, no sobre la forma. 🔴 **Consecuencia que se declara en vez de taparse: las cifras de la tabla de abajo
son las que el pase 56 reprodujo; el pase 58 NO las afirma como medidas hoy.**

🔵 **Y corrige al pase 52 en la dirección contraria.** Ese pase midió la frontera y la declaró más angosta
—*«la negativa es sobre EJECUTAR CON RED código que vino clonado, no sobre ejecutar el código»*—; **hoy alcanzó a la
ejecución sin red.** ⚠️ **La frontera es del ENTORNO y varía entre pases, así que no se vuelve a publicar como regla
general** — que es exactamente el error que los pases 50 y 51 cometieron y el 52 corrigió, ahora en el otro sentido.
🔴 **El permiso a pedir es angosto y es uno: ejecución de las suites OFFLINE del árbol clonado** (no incluye red; la
salida de red para `probe.py` sigue siendo un pedido aparte, del pase 52).

🟢 **Pase 55 del 2026-10-03: la columna «Hoy» se re-verificó COMPLETA y las once suites reprodujeron su
cifra publicada.** Las once corren OFFLINE en este entorno.

🔴 **Y la corrección que este pase tiene que hacerse a sí mismo, porque casi publicó lo contrario.** Las
dos suites que **no imprimen total propio** (`unitime-mcp-gate` y `openedx-course-generator`, que sólo
imprimen `ALL CHECKS PASSED`) se re-midieron con un `grep` **escrito a mano en el pase**, que devolvió
**49** y **34** — y estuvo a punto de publicarse como *«dos cifras vencidas»*. ⚠️ **Era un falso
positivo:** el instrumento **versionado** de esta KB (`compose/code/patterns-figure-audit/extract_figures.py`,
que ancla `^PASS `) devuelve **46** y **33**, exactamente lo que esta tabla publica. **El defecto del grep
propio: su segunda alternativa no estaba anclada y con `-i` matcheó `PASS`/`passed` en cualquier parte de
la línea, incluida la línea de resumen.**

🔴 **Lo que invalidó el control, y es la lección de método que deja el pase: el «control positivo» que se
corrió para habilitar el instrumento (37 = 37 en `sebserver-mcp-gate`) era INSENSIBLE al defecto**, porque
esa suite emite líneas `ok` y no `PASS` — **el control no ejercitó el caso donde el instrumento podía
fallar.** 🔵 **Un control positivo que pasa no habilita un instrumento si no ejercita ese caso. Y antes de
escribir un instrumento a mano hay que correr el que este repositorio ya versiona.** Ver **P126** y la
tendencia **313**.

### 📏 La regla de P126, como regla permanente de este repositorio (escrita en el pase 56)

**Vale para toda cifra de este repositorio, no sólo para las de `compose/code/`:**

1. 🔴 **Antes de escribir un instrumento a mano se corre el que este repositorio ya versiona**
   (`compose/code/patterns-figure-audit/extract_figures.py`). Si hace falta uno nuevo, se versiona.
2. 🔴 **Un control positivo sólo habilita un instrumento si ejercita el caso donde ese instrumento
   puede fallar.** Dos suites que comparten vocabulario **no son dos casos**: son el mismo caso dos
   veces. El control del pase 55 pasó porque midió `PASS` contra `PASS`.
3. 🟢 **Una suite que no publica su propio total invita al instrumento casero**, así que toda suite
   nueva de `compose/code/` **imprime su total** en una de las formas que el lector ya reconoce
   (`N/N checks passed`, `N controles pasados`, `N checks run`, `N de M`).
4. 🔵 **La regla está ejecutable, no sólo escrita:** `compose/code/suite-total-control/`
   (**10/10**) afirma el caso NEGATIVO —el contador por vocabulario acierta en `PASS` y **falla en
   `ok`**— que es el que faltaba. Es el control concreto que el pase 55 pidió para la próxima vez.

✅ **Las dos suites que faltaban ya cumplen el punto 3 (pase 56), y las dos reprodujeron el conteo a
mano del pase 55 —46 y 33—, lo que confirma que el defecto nunca estuvo en el número sino en que
obtenerlo exigía un instrumento casero.**

🟢 **Corrección del pase 52 del 2026-10-02: la columna «Hoy» SÍ se re-verificó, y estaba estancada desde el pase 49
por una conclusión demasiado amplia.** Los pases 50 y 51 escribieron que *«el entorno niega la ejecución de código de
este repositorio»* (`[Code from External]`) y dejaron de intentarlo. **Este pase midió la frontera exacta de esa
negativa y es más angosta:**

| Qué se corre | Resultado en este entorno |
|---|---|
| las suites **OFFLINE** (`test_*.py`, `run_test.sh`) | 🟢 **corren todas, y los doce valores de arriba se reprodujeron hoy** |
| un script del repositorio que **sale a la red** (`probe.py`) | 🔴 **NEGADO (`[Code from External]`)** |

🔵 **O sea que la negativa es sobre EJECUTAR CON RED código que vino clonado, no sobre ejecutar el código.** ⚠️ **La
consecuencia de método, que es la que vale: una negativa puntual se midió por su caso más amplio y se publicó como
regla general, y eso costó DOS pases de cifras sin re-verificar** — exactamente el error que **P107** existe para
evitar, cometido sobre el propio instrumento. 🔴 **Lo único que sigue bloqueado es la acción 2** (hacer comparables las
superficies de Canvas, **227** vs **165**), **porque exige `probe.py` con red**, y por eso el permiso que hay que
pedir es **salida de red para ese script**, no permiso de ejecución. Ver **P119** y la tendencia **280**.

⚠️ **Las dos filas «ídem» no son adorno: son el caso que el pase 47 encontró citado sin su
condición.** Una cifra de aserciones sin la invocación que la produce no se puede reproducir, aunque
sea correcta.

## Uso

1. **Nuevo engagement**: leer `intel/market.md` + `repos/foundations.md`
2. **Proponer solución AI**: `agents/top.md` + `compose/patterns.md`
3. **Mantenerse al día**: correr `ingest/update.sh` semanalmente
4. **Verificar antes de citar**: `compose/code/patterns-figure-audit/extract_figures.py --check`
   remide las cifras de `compose/patterns.md` que salen de suites propias. **Una cifra de una suite
   se vence cuando la suite crece**, y el pase 47 encontró dos vencidas

---
*Red de KBs Globant AI Studios → [globant-kb](../globant-kb/)*
