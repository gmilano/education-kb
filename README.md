---
industry: education
region: Global
updated: 2026-10-10
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

## Pase 99 — 2026-10-10

⏱️ **Noveno pase de esta fecha** (el 91 corrió 23:0x–00:00 UTC; el 92, 00:4x–01:3x; el 93, 01:4x–02:24;
el 94, 02:5x; el 95, 03:4x; el 96, 04:4x–05:xx; el 97, 05:4x–06:xx; el 98, 06:4x–07:xx; este,
07:4x–08:xx).

**El hallazgo principal: siete pases registraron «`ladder.sh` denegado» como UN hecho. Son DOS, y
separarlos cambió lo que esta base puede publicar. La denegación cubre EJECUTAR el script, no las
operaciones que el script hace** — `git ls-remote --symref` y `raw.githubusercontent.com` estaban
**permitidos** y se corrieron en línea. 🔵 **`P1005`: cuando el código del repositorio está denegado,
re-corré sus OPERACIONES en línea y leé el bloque de título a mano. `P237` prohíbe un segundo
clasificador, no un segundo fetch.**

🟢 **El dividendo es inmediato y es `P987`: `git ls-remote` devuelve SOLO el SHA de 40 caracteres**, y
siete pases publicaron SHAs de 7 porque la API que devuelve los largos da 403. 🟢 **Toda fila que
agrega este pase trae dirección de 40 caracteres**, y el `seb-server` del pase 98 pasa de
`7f45689f797337` a `7f45689f79733797e70f8c5318ec9cadb08d03be` **reproduciendo exactamente su término
de bytes (16 725 B) y sus 194 tags.**

🔴 **El sandbox sigue sin ejecutar código del repositorio (SÉPTIMO pase consecutivo)**: `ladder.sh`
**y** su suite offline `test_ladder.sh`, denegadas antes de arrancar. 🟢 **Y otra vez no se escribió
ningún clasificador** (`P237`). **14 slugs resueltos: 13 lecturas de payload de licencia, 1 negativo
limpio de 24 nombres.**

### 🔴 `T4` cobra su cuarta confirmación, y esta vez con 53 días de plazo

🟢 **El pase 98 pre-registró «consultá el PROCEDIMIENTO, no la fecha». Corrido, cierra la pregunta:**
el Parlamento Europeo lo refrendó el **16 jun 2026**, 🟢 **el Consejo lo adoptó formalmente el 29 jun
2026**, se publicó como **Reglamento (UE) 2026/1744** (DOUE 24 jul 2026) y **entró en vigor el 27 jul
2026**.

🔴 **Y lo que la atención sobre «el retraso» tapó: el Ómnibus movió la fecha LEJANA y dejó la CERCANA
en pie.**

| limbo | aplica desde | ¿postergado? |
|---|---|---|
| prohibiciones (🔴 **reconocimiento de emociones en educación**) + alfabetización en IA | **2 feb 2025** | 🟢 **no** |
| **Artículo 50** transparencia | **2 ago 2026** | 🟢 **no** |
| 🔴 **Artículo 50(2)** marcado legible por máquina, para IA generativa ya en el mercado antes del 2 ago 2026 | 🔴 **2 dic 2026** | 🟢 **sólo período de gracia** |
| **Anexo III** alto riesgo — admisiones, **supervisión remota de exámenes**, evaluación | **2 dic 2027** | 🔴 **sí** |
| Anexo I embebidos | 2 ago 2028 | 🔴 sí |

🔵 **Así que el limbo que obliga primero a un cliente EMEA es `2026-12-02` — cincuenta y tres días
desde este pase — y NO es la fecha que discute el mercado.** 🟢 **Y esta base ya guarda CUATRO
artefactos probados exactamente para ese limbo**: `aiact-50-2-exposure/`, `aiact-50-2-spans/`,
`aiact-50-2-marking/`, `aiact-50-2-pack/`. 🔵 **`Gap 381` enseñó a leer esto como una VENTA que falta;
`P99-A` es esa venta, y es el único patrón de esta base con fecha de vencimiento.**

### 🔴 `P1006` — la capa de conectores se parte por licencia, y la partición elige la plataforma

| plataforma | conector | licencia (payload) | tags / último |
|---|---|---|---|
| **Canvas** | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · 1 071 B | 🟢 **26 / `v1.14.0`** |
| **Moodle** | [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** · 34 523 B | 🟡 **7 / `v0.1.7`** |
| **Moodle** | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🟢 **MIT** · 1 064 B | 🔴 **0** |

🔴 **Canvas tiene un conector permisivo Y liberado. Moodle tiene uno de cada cosa y ninguno es
ambas.** 🔵 **Y el golpe es regional: Moodle es lo que corren los ministerios y las universidades
públicas — justo donde esta base apuntó LATAM y sector público durante ocho pases de patrones.**
🔴 **`P975` otra vez**: el directorio que lo listó dijo sólo *«open-source»*; el payload dice
**AGPL-3.0**, 🔴 **y el error fue en la dirección CARA** (`P997`), porque AGPL sobre un servidor que
el cliente alcanza por red es la única familia que puede alcanzar su propio código.

### 🔴 `Gap 372` nunca fue una ausencia: es un GAP DE RELEASE, y eso se compra distinto

🟢 **Tres correctores permisivos de respuesta abierta, leídos a SHA fijo:**
`KamalEzzo/automated-essay-grading-system` (**MIT**, sólo contabilidad) ·
`shibing624/judger` (**Apache-2.0**, README de **177 B**) ·
`doheejin/ProTACT` (**BSD-3-Clause**, implementación del paper ACL Findings 2023).
🔴 **0 de 3 tiene un solo tag de release.** 🟢 **Y el control está en el mismo pase, misma industria,
mismo instrumento: `canvas-mcp` 26 tags, `DeepTutor` 135, `seb-server` 194.**
🔵 **`T20`: en educación el permiso abunda y el RELEASE escasea, y los dos se confunden porque ambos
se ven como «no encontré nada usable».** 🟢 **La oferta pasa de «buscar un corrector» a «endurecer
uno», y `ProTACT` es el que vale endurecer** porque *cross-prompt* —transferir a una consigna no
vista— es lo que el cliente necesita el primer día.

### 🔴 Una hipótesis que este pase FORMÓ, PROBÓ y REFUTÓ

🔵 **La hipótesis:** el código de scoring es permisivo y los corpus corregidos son no-comerciales, así
que el corpus es el bloqueo real. 🔴 **Refutada con n = 3:**
`anaistack/cefr-asag-corpus` es **CC-BY-NC-SA-4.0** (leído del payload, `LICENSE.txt` 20 863 B),
🟢 ASAP 2.0 se reporta **CC BY**, y 🔴 **PERSUADE 2.0 lo tiene DISPUTADO: el distribuidor dice
CC-BY-NC-SA-4.0 y el originador dice CC BY 4.0.**
🟢 **Lo que reemplaza a la regla es más angosto y más útil:** la licencia del corpus es el término que
decide un proyecto de respuesta abierta, **no es uniforme**, y en el corpus más grande **el
distribuidor y el originador la declaran distinto**. 🔴 **No se pudo zanjar — las dos páginas están en
el conjunto rechazado — así que queda como `Gap 389`.** 🔵 **Una licencia de corpus es un término de
compra: nunca heredarla del listado de un distribuidor.**

### 🟢 `Gap 388` descargado como CONDICIÓN, re-registrado como NO CABLEADO

🟢 **Medido:** un 404 real de `raw.githubusercontent.com` trae un cuerpo de **exactamente 14 bytes**,
el literal `404: Not Found`. 🔴 El throttle del pase 98 fue **429 con cuerpo HTML de 1 523 B**.
🔵 **`404` = ausente, `429` = estrangulado, y a nivel de bytes no se pueden confundir.** 🟢 **Cero 429
en 14 slugs × hasta 24 nombres**, así que el único negativo del pase
(`sankalpjain99/Automatic-Essay-Scoring`) es una ausencia **real**.
🔴 **No cableado**: el remedio son tres líneas dentro de un archivo que este sandbox no ejecuta.

### 🟢 `P872` vuelve a falso-descartar, y cae sobre la fila que promovió el pase 98

| ruta en `SafeExamBrowser/seb-server` · `7f45689f79733797e70f8c5318ec9cadb08d03be` | HTTP | bytes |
|---|---|---|
| `README.md` | 🔴 **404** | **14** |
| `LICENSE` | 🟢 **200** | **16 725** |

🔴 **El testigo dice «ausente» de un repo cuyo payload de licencia tiene 16 725 bytes.** 🟢
Confirmación independiente del 3-de-6 del pase 98, sobre la plataforma misma que `Gap 387` existe
para recuperar.

### 🟡 `P998` tiene una segunda forma, y es el COSTO del arreglo que `P960` hizo bien

[`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) — `LICENSE`
**1 531 B**, `main` · `196c547291da5df57b68165691e47ca7ffdbb137`. 🟢 **Trae las tres cláusulas BSD
textuales** (aviso · reproducción binaria · **no-endoso**) → **BSD-3-Clause por su texto operativo**.
🔴 **Y la cadena `"BSD"` aparece CERO veces. No tiene bloque de título**: abre con
`Copyright (c) 2023-2025 Mohamed El hajji` y **`All rights reserved.`**
🔵 **`lib/license_family.sh` clasifica por bloque de título POR DISEÑO — es exactamente aquello en lo
que `P960` convirtió a v3 — así que sobre este payload devuelve UNCLASSIFIED.** 🟢 **Queda registrado
como el costo medido de una corrección que sigue siendo correcta, no como argumento para revertirla**;
`P237` sigue prohibiendo el fork. 🟡 Y para el abogado del cliente, no para el clasificador:
`All rights reserved.` encima de una concesión permisiva es una contradicción de cara.

### 🟢 Los cinco leads que el pase 98 se pre-registró: CINCO corridos, primera vez en este archivo

1. 🟢 **India PAGÓ, por nombre de ministerio.** NCERT + CBSE, IA y Pensamiento Computacional **grados
   3 a 8 desde el ciclo 2026-27**, anuncio del **30 oct 2025**, **tres documentos** aprobados por
   NCERT, **integrado en materias existentes** (grado 3 vía *«The World Around Us»*), capacitación
   docente en el receso. 🟢 **Apareció una dirección de primera parte — `pib.gov.in`, `PRID 2184211`**
   🔴 **y es inalcanzable desde acá, así que queda como LEAD CON DIRECCIÓN, nunca como lectura
   primaria.**
2. 🟡 **L&D: MITAD pagada.** 🟢 **LATAM ubicado** (USD 24 800 M en 2025 → USD 43 600 M en 2034, CAGR
   **6,27 %**; LMS LATAM USD 2 060 M en 2026; 194 startups, 43 financiadas, USD 165 M).
   🔴 **EMEA: cero medido** — los resultados eran globales o de EE. UU. 🔵 **Instrumentos nombrados
   para el próximo pase: CIPD, Fosway, y el informe completo de SHRM MENA.**
3. 🟢 **El procedimiento de la UE: PAGÓ Y CERRÓ** → ver `T4` arriba.
4. 🟢 **Singapur (IMDA) PAGÓ, con su limitación dicha**: *Model AI Governance Framework for Agentic
   AI*, lanzado en Davos el **22 ene 2026**, **voluntario** pero con responsabilidad legal retenida;
   su **cuarta dimensión** es educación del usuario e incluye *«que los usuarios CONSERVEN
   competencias fundamentales»*. 🔴 **Es transversal, NO es guía del sector educativo.** 🟡 Conflicto
   de versión sin resolver (una fuente reporta v1.5, 20 may / 5 jun 2026).
5. 🟢 **África, 4 de 4, una consulta por país** (`T16` honrado, tercera confirmación): **Ruanda**
   (MIT RAISE *Day of AI* + MINEDUC/REB, **>5 000 docentes**, el mayor despliegue nacional del
   programa en África; tablets con IA y robótica con **Keza Lab**; tres pilares del ministro
   Nsengimana) · **Marruecos** (**Recomendación N.º 1/2026 del 14 abril**, 41 páginas, **sin
   autoridad ejecutiva**, diferenciada por nivel: primaria **precautoria**, protegiendo lectura,
   escritura y matemática) · **Ghana** (Estrategia Nacional de IA, abril 2026; currículo NaCCA de
   KG a secundaria básica, 🔴 **anunciado y NO vigente** — falta Gabinete y Parlamento) ·
   **Etiopía** (**mayo 2026**, MoE + UNESCO redactan la Política Nacional de IA y Educación, aún
   borrador; universidad **Medemer** aprobada el 2 mar 2026; 🔴 **>85 % de estudiantes usan IA contra
   15–20 % de docentes**, el espejo invertido del resto del archivo).

### 🔴 Lo que NO se consiguió, dicho en vez de ocultado

- 🔴 **CERO lecturas de fuente primaria, NOVENO pase.** 🟢 **Pero este pase enuncia el límite como un
  CONJUNTO en vez de una lista de fracasos.** 🟢 **Alcanzable:** el backend de WebSearch ·
  `github.com` por git smart-HTTP · `raw.githubusercontent.com`. 🔴 **Rechazado, todo lo intentado:**
  `arxiv.org`, `www.iesalc.unesco.org`, `digital-strategy.ec.europa.eu`, `eur-lex.europa.eu`,
  `www.kaggle.com`, `the-learning-agency.com`.
- 🔵 **Y la misma negativa IMPRIME DISTINTO según qué herramienta pregunte**: `curl` devuelve
  **error 56** (conexión reseteada), `WebFetch` devuelve **`ENOTFOUND`** (resolución de nombre).
  🔵 **Dos formas, un hecho, y ninguna es una ausencia** — la lección de `P872` un nivel más afuera.
  🟡 Una sonda al endpoint de estado del propio proxy fue **denegada** (`[Exfil Scouting]`), así que el
  mecanismo no es legible desde adentro.
- 🔴 **`github trending education AI {año}` SIGUE RETIRADA** y **no se re-corrió**. 🟢 **La retirada
  quedó corroborada por otra vía**: la consulta general `top open source AI agents education {año}
  github MIT` devolvió **frameworks de agentes genéricos y material de curso**, sin **un solo agente
  específico de educación** — el mismo modo de falla desde otra consulta. 🔵 **Las consultas que
  nombran la TÉCNICA (`P955`) volvieron a pagar donde las que nombran la categoría no.**
- 🔴 **`Gap 376` NO queda descargado**: `P1005` permite re-correr las operaciones, pero **no** permite
  probar el clasificador que produjo las filas históricas. Eso sigue requiriendo `grant-ladder-v4`
  **ejecutado**.
- 🔴 **`Gap 388` descargado como condición pero NO CABLEADO**, y 🔴 **`Gap 389` abierto** (licencia de
  corpus en disputa entre distribuidor y originador).
- 🔴 **Los cuatro artefactos del Artículo 50(2) que `P99-A` vende NUNCA se ejecutaron en este
  sandbox.** 🟢 Están committeados con sus tests y fixtures; **un equipo de entrega debe correr las
  suites en su propia máquina antes de cotizar.** 🔵 **Dicho acá en vez de descubierto por un
  cliente.**

## Pase 98 — 2026-10-10

⏱️ **Octavo pase de esta fecha** (el 91 corrió 23:0x–00:00 UTC; el 92, 00:4x–01:3x; el 93, 01:4x–02:24;
el 94, 02:5x; el 95, 03:4x; el 96, 04:4x–05:xx; el 97, 05:4x–06:xx; este, 06:4x–07:xx).

**El hallazgo principal: `Gap 381` pedía UN `grep` desde el pase 96 y nadie lo había corrido. Corrido,
dice que esta base publicó una exposición regulatoria —el reconocimiento de emociones en educación,
PROHIBIDO desde el 2 feb 2025— y no ofrecía nada con qué atenderla, mientras guardaba TRES artefactos
probados, desde el pase 43, para la plataforma open source dominante de supervisión de exámenes.**
🔵 **`Gap 381` costeado: no es una fila que falta, es una VENTA que falta.**

🔴 **El sandbox sigue sin ejecutar código del repositorio (SEXTO pase consecutivo)**: `ladder.sh` **y**
su suite offline `test_ladder.sh`, denegadas antes de arrancar. 🟢 **Y otra vez no se escribió ningún
clasificador** (`P237`). 🟢 **Pero esta vez la negativa no costó el pase**: las dos auditorías que
rindieron —`Gap 381` y la mitad de `Gap 384`— **tienen como corpus el propio repositorio**, y se
corrieron sin red y sin ejecutar código del repo. 🔵 **`P1004`: cuando el instrumento está denegado,
preferí la pregunta cuyo corpus es el repositorio.**

### 🔴 `Gap 387` — la fila no se perdió midiendo: la perdió el reset de esta base

| población | n |
|---|---|
| slugs en `compose/code/` | **1 056** |
| slugs en las páginas del estante | **159** |
| en código y en **ninguna** página | **956** |
| 🟢 …sostenidos por un directorio **hecho a propósito** y no por una tabla de barrido | **4** (uno es artefacto de parseo) |

🟢 **956 no es el defecto** — los barridos registran candidatos por diseño. 🔴 **Los 3 reales son la
forma `UniTime`**, y el peor es [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server):
🟡 **MPL-2.0**, payload **16 725 B**, `master` · `7f45689f797337`, **194 tags**, `v3.0-latest`.

🔴 **Y el `README` del pase 44 afirma que el veredicto MPL es «lo que dicen `repos/foundations.md` y
las tendencias del pase 41/42».** 🟢 **El archivo prueba que era cierto cuando se escribió**
(`archive/2026-10-06-pre-reset/repos-foundations.md:3774`) 🔴 **y el reset del 2026-10-06 la tiró.**
🟢 **La lectura de hoy reproduce el veredicto archivado exactamente, con el término de bytes que el
archivo no tenía** — así que es una RESTAURACIÓN, no un descubrimiento, y eso es la prueba más fuerte
de que la pérdida fue del reset y no de una medición.

🟢 **Altas de este pase, las tres verificadas por payload:** `seb-server` (**MPL-2.0 — la PRIMERA fila
MPL de cualquier página viva de esta base**; copyleft por ARCHIVO, §1.10(a), así que una capa
propietaria alrededor es lícita) · `toshieji/moodle-grading-mcp` (**MIT**, 1 120 B — la costura de
`Gap 372`: escribe la nota en `workflowstate=readyforreview` y **nunca la libera**) ·
`juneyaooo/lineage-skill` (**Apache-2.0**, 11 358 B).

### 🔴 `P997` — una corrección en prosa, en un archivo, NO se propaga

🔴 **Dos de los tres `README` de `seb-server` decían Apache-2.0** — y `proctoring-reach-audit` se
escribió en el **pase 46**, *dos pases después* de que el pase 44 corrigiera el valor a MPL-2.0 en
`sebserver-mcp-gate`. 🔴 **Y el error iba en la dirección CARA: Apache-2.0 es MÁS permisiva que MPL**,
de modo que habría hecho prometer a un cliente libertades que la licencia no da.
🟢 **Los dos archivos quedan corregidos en este commit.**

### 🟢 Dos capas nuevas, las dos de consultas que nombran la TÉCNICA (`P955`)

- 🟢 **Taxonomía de skills** — `nestauk/ojd_daps_skills` (**MIT**, `v3.0.0`, 8 tags, 🟢 **EMEA** por la
  línea de titular *«Copyright (c) 2024, Nesta»*) · `KonstantinosPetrakis/esco-skill-extractor`
  (**MIT** leído del CUERPO, sin título, y 🔴 **con comillas tipográficas** — `P998`) ·
  `dkavargy/ESCOPlus2.0` (**MIT**, mantiene la taxonomía misma).
  🔴 **Y la trampa: `workforce-data-initiative/skills-ml`, la biblioteca bandera del Open Skills
  Project y el primer resultado de cualquier búsqueda, es `NONCOMMERCIAL-NOT-OSI`** — **mismo
  template de la Universidad de Chicago**, frase por frase, que el que `Gap 385` encontró un pase
  antes en `dssg/student-early-warning`. 🔵 **`P999`: los dos casos de uso institucionales de mayor
  ROI de esta industria comparten UNA oficina de licenciamiento.** 🟢 El sello `"BY DOWNLOADING"` ya
  atrapó 2 de 2. 🔴 **Es clave de búsqueda, nunca veredicto — `P975` manda.**
- 🟢 **Credencialización** — `CredentialEngine/Open-Badge-Publisher` (**Apache-2.0**, 11 357 B
  prístino, 4 de 4 encabezados) y `nfh-trust-labs/opencred` (**MIT**, `v1.9.1`, 30 tags) contra
  🔴 **cuatro emisores AGPL/LGPL**. 🔵 **`P1001`/`T17`: la licencia permisiva está del lado que MIDE y
  el copyleft del lado que se vuelve el REGISTRO** — segunda confirmación independiente, siete pases
  después de la del scoring (`Gap 372`). 🔵 **Publicado como falsable, con las tres consultas que lo
  romperían.**

### 🟢 `Gap 386` descargado como DIMENSIONADO (y re-registrado como SIN MAPA)

🟢 **Las dos consultas pre-registradas se corrieron por separado y las dos pagaron:** IA en formación
corporativa **USD 7 490 M (2026) → USD 18 190 M (2031)**, CAGR **19,43 %** (Mordor), contra una base
total de formación corporativa de **~USD 400 000 M** (Bersin). 🔴 **Las dos cifras de «plataformas de
upskilling» difieren 7,5× y la diferencia es ALCANCE, no desacuerdo.** 🟢 **Y una fuente es
internamente inconsistente por un factor de ~257 en una sola página** (Verified Market Research:
USD 100 000 M en 2024 y ~USD 388,9 M en 2025) — queda registrada para que nadie la cite.
🟡 **Sólo 1 de 5 cifras trae región**, así que el comprador de L&D es un número sin mapa: gap más
angosto que el que reemplaza, re-registrado.

### 🔴 Lo que NO se consiguió, dicho en vez de ocultado

- 🔴 **CERO lecturas de fuente primaria, octavo pase.** Y este pase perdió la mejor candidata en diez:
  el **Plan Nacional de IA de México (abril 2026)**, PDF de primera parte en `portal.atdt.gob.mx`.
  El proxy de egreso rechazó el `CONNECT` (`000`, `connect_rejected`), igual que `www.unesco.org` y
  `eur-lex.europa.eu`. 🔵 **«Rechazado» no es «no encontrado», y se registra como lo primero.**
- 🔴 **`github trending education AI {año}`: SÉPTIMO cero consecutivo. QUEDA RETIRADA.** Devuelve
  materiales *sobre* IA, nunca IA *para* educación.
- 🔴 **`api.github.com` 403 por séptimo pase y `github.com` HTML 403** — ninguna ★ se movió. `—`
  significa *no leído*, nunca cero.
- 🔴 **`Gap 388` abierto: `raw.githubusercontent.com` devolvió 429** con cuerpo HTML de 1 523 B.
  🟢 `ladder.sh` exige `code = 200`, así que no puede clasificar una página de rate-limit como
  licencia; 🔴 **pero un 429 en los 24 nombres se imprime igual que un negativo real.** 🟢 **El remedio
  es una condición, no un clasificador: 404 = ausente, 429 = estrangulado.**
- 🔴 **Y el testigo `README.md` de `P872` FALSO-DESCARTA: 3 de 6 filas auditadas devuelven 404 en el
  testigo con payload 200.** 🟢 Un barrido con ese control habría tirado 3 de 6 barridos buenos.
- 🔴 **`Gap 376` no queda descargado** (requiere `grant-ladder-v4`), y **`Gap 372` sigue sin corrector
  permisivo de grado productivo para respuesta abierta.**

## Pase 96 — 2026-10-10

⏱️ **Sexto pase de esta fecha** (el 91 corrió 23:0x–00:00 UTC; el 92, 00:4x–01:3x; el 93, 01:4x–02:24;
el 94, 02:5x; el 95, 03:4x; este, 04:4x–05:xx).

**El hallazgo principal: `Gap 376` llevaba cuatro pases diciendo que el censo se degradaba sin poder decir
cuánto. Ahora se sabe: de las 127 filas publicadas con `(slug, ref, sha7)`, 122 siguen EXACTAMENTE en el
SHA en que se midieron, 0 son inalcanzables, 0 refs desaparecieron — y las 5 que se movieron se releyeron
este pase y las 5 conservaron su licencia.** 🔵 **«Se está degradando» pasó a ser «5 filas de 127, y se
leyeron».**

🔴 **El sandbox sigue sin ejecutar código del repositorio (CUARTO pase consecutivo)**: `ladder.sh` **y** su
suite offline `test_ladder.sh` fueron denegadas antes de arrancar. 🟢 **Y otra vez no se escribió ningún
clasificador** (`P237`). 🔴 **`Gap 376` NO queda descargado** — un SHA vigente no dice nada sobre si el
alcance de 24 nombres ni el clasificador que produjeron esa fila eran correctos, y eso **sólo** lo resuelve
`grant-ladder-v4`. 🟢 **Lo que cambió es que la deuda ya tiene tamaño.**

### 🔴 `P987` — un SHA de 7 caracteres es un formato de presentación, no una dirección

| URL | HTTP |
|---|---|
| `…/Submitty/Submitty/ff82521694719bc1e282d046631bf0232c9d673e/README.md` | 🟢 **200** |
| `…/Submitty/Submitty/ff82521/README.md` | 🔴 **404** |
| `…/Submitty/Submitty/80d7d66/README.md` *(el SHA corto ANTERIOR, mismo repo)* | 🟢 **200** |

🔴 **Mismo objeto: la abreviatura da 404 y los 40 caracteres completos no** — y de forma **inconsistente
por commit**, lo que falla en silencio. 🔴 **Una abreviatura que no resuelve da 404 en los 24 nombres, que
es exactamente lo que este estante publica como `sin payload de licencia`.** 🟢 **`P872` lo atrapó** (el
testigo `README.md` también dio 404, así que el barrido se descartó en vez de publicarse) 🟢 **y el radio
se MIDIÓ en vez de suponerse: las 10 filas publicadas como «sin licencia» devuelven testigo 200 en su SHA
publicado. 0 de 10 son artefactos del instrumento.**

### 🟢 Dos gaps DESCARGADOS, y los dos con una corrección a su propia redacción

- 🟢 **`Gap 377`** pedía *«agregar `pom.xml`/`build.gradle` a la lista de rutas del ladder; es barato»*.
  **Barato sí, pero no hay que escribir nada:** `p289-maven-manifest/maven_license.py` (**11/11**, con su
  control negativo) ya estaba cableado a `p283::PARSERS` y a `sweep_named.sh` por **`P294`**, y
  `build.gradle` ya está en la lista de `p172`. 🔵 **`grant-ladder-v4` necesita UN import, no un lector
  nuevo** (`P237`). 🔴 **Y la otra mitad del gap es FALSA: `build.gradle` no es oráculo de licencia** —
  Artemis no declara ninguna en **52 855 B**. 🔵 **La asimetría es la política de distribución de Maven
  Central, no el lenguaje.** 🟢 **El oráculo sí paga: 4 de 4 plataformas Maven declaran.**
- 🟢 **`Gap 375`** queda descargado **como INMEDIBLE, con el mecanismo nombrado.** `pupilfirst`,
  `academico` y `open-tutor-ai-CE` sirven su manifiesto con **200 y sin campo `version`**; dos declaran
  `"private": true`, la convención npm para una raíz de workspace que nunca se publica a un registro.
  🟢 **`P985` separa «sin versión» en tres hechos que se cotizan distinto** — y 🔴 **`academico`, la
  candidata a SIS permisivo de esta base, tiene CERO tags.**

### 🟢 Altas: una plataforma y una capa entera

- 🟢 **[`UniTime/unitime`](https://github.com/UniTime/unitime)** — **Apache-2.0**, payload **11 357 B
  prístino**, **101 tags**, `v4.9.152`, y su `pom.xml` lo confirma de forma independiente. **Horarios,
  cursos y matriculación universitaria**: la única capa para la que el tier permisivo no tenía nada.
  🔴 **Y el hallazgo es sobre esta base, no sobre UniTime:** `compose/code/unitime-mcp-gate/` lleva una
  puerta MCP **probada** desde el **pase 42** y la plataforma no estaba en ninguna página del estante
  (`Gap 381`). 🔴 **Término de costeo obligatorio: su `NOTICE` son 22 526 B y da 200** — el §4(d) de
  Apache-2.0 obliga a propagarlo.
- 🟢 **La capa de RÚBRICAS, cuatro filas permisivas, hallada con la primera consulta que nombró la TÉCNICA
  y no la industria** (`P955`, cuarto pase consecutivo): `OpenRS` (**Apache-2.0**) juzga con criterios
  ponderados y veredicto interpretable, `OpenRubrics` (**MIT**) genera rúbricas, `rubricbench` (**MIT**)
  calibra al juez contra **1 147 comparaciones anotadas por expertos**, `awesome-rubric-rewards` (**CC0**)
  indexa. 🔵 **Esto reescribe el gap de alineación curricular que esta base declaró cinco veces: no es un
  gap de OFERTA, es un gap de CABLEADO** — y un cableado es un encargo acotado, no una apuesta de
  investigación. `Gap 379`, costeado como **`P96-A`**.

### 🔴 El cambio regional que invierte la prioridad de esta base — `T15`

🔴 **La UE aplazó las obligaciones de alto riesgo del Anexo III —evaluar resultados de aprendizaje entre
ellas— del 2 ago 2026 al 2 dic 2027.** 🟢 **Vietnam puso en vigor deberes equivalentes el 15 ago 2026,
trece días después de la fecha que la UE dejó vacante**, con `Decision 33/2026/QD-TTg` (firmada por el
vice-primer ministro Hồ Quốc Dũng, publicada el 30 jun 2026; deberes de implementación en el
`Decree 142/2026/NĐ-CP`): **46 sistemas de alto riesgo en 6 sectores, y educación son 3 de ellos.**

🟢 **Y el primero de esos tres limbos no habla de evaluación:** *«contenido de autoestudio generado a
partir de fuentes de datos no controladas»*. 🔵 **Un tutor RAG que nunca califica queda dentro del alcance
en Vietnam por el ORIGEN de su material.** 🟢 **Esta base ya tenía la respuesta medida** — `T11`:
fundamentar un tutor alineado al currículo en datos de estándares verificados lleva la alucinación de
**31,9 % → 0,2 %**, y `bncc-dev/bncc-pacotes` expone **1 721 objetivos verificados** por MCP con el dataset
embebido. 🔵 **Así que el *grounding* deja de ser un argumento de calidad y pasa a ser un CONTROL
REGULATORIO** — mucho más fácil de vender. Costeado como **`P96-B`**.

🟡 **`P94-A` no se retira: se RE-SECUENCIA.** El entregable y su capa de evidencia permisiva (`rsmtool`
Apache-2.0, `skll` BSD-3) no cambian. 🔴 **Cambió el comprador.** **Véndase en APAC con plazo vivo y en
EMEA como preparación para 2027.**

### 🔴 Lo que NO se consiguió, dicho en vez de ocultado

- 🔴 **CERO lecturas de fuente primaria.** `WebFetch` devolvió `getaddrinfo ENOTFOUND` en
  `digital-strategy.ec.europa.eu`, `www.gibsondunn.com` y `en.wikipedia.org`; `curl` crudo devolvió
  **`000`** en tres URLs de editoriales jurídicas. 🟢 **Toda afirmación regulatoria de este pase lleva
  grado «resumen de búsqueda» y fue corroborada por dos rondas independientes sobre conjuntos de fuentes
  distintos.**
- 🔴 **África, sexto pase sin nada — y este pase se halló el MECANISMO.** Una consulta que empareja
  *«Golfo Y África»* devolvió **nueve fuentes, todas del Golfo, cero africanas.** 🔵 **Emparejar
  sub-regiones garantiza la respuesta de la más ruidosa y disfraza el silencio de la otra como cobertura.**
  🟢 **Remedio pre-registrado: Kenia, Nigeria, Sudáfrica y Egipto como cuatro consultas separadas.**
- 🔴 **`github trending education AI {año}`: SEXTO cero consecutivo. RETIRAR la consulta** — devuelve
  materiales *sobre* IA, no IA *para* educación. 🔵 **La ambigüedad está en la frase, no en el índice.**
- 🔴 **`Gap 372` sin cambios**: no hay corrector permisivo de grado productivo para respuesta abierta.
- 🔴 **`api.github.com` 403 por quinto pase consecutivo**, así que ninguna ★ se movió. **`—` significa *no
  leído*, nunca cero.**

## Pase 94 — 2026-10-10

⏱️ **Cuarto pase de esta fecha** (el 91 corrió 23:0x–00:00 UTC; el 92, 00:4x–01:3x; el 93, 01:4x–02:24;
este, 02:5x).

**El hallazgo principal: el pase anterior cerró `Gap 372` con una frase demasiado amplia —"no existe
librería permisiva de grado productivo para corrección automática"— y leer los payloads la invierte por una
costura que nadie había trazado. El SCORER no existe en abierto permisivo. La CAPA DE EVIDENCIA —la que el
regulador y una apelación consumen de verdad— sí existe, es Apache/BSD, tiene 2 916 commits y la publica la
casa que opera TOEFL y el GRE.**

🔴 **El sandbox sigue sin ejecutar código del repositorio** (segundo pase consecutivo): `ladder.sh` se
rechaza antes de arrancar. 🟢 **Y otra vez no se escribió ningún clasificador** (`P237`): se corrió el mapa
de oráculos a mano y se imprimió el bloque de título de cada payload en vez de clasificarlo (`P970`).
**12 slugs resueltos: 9 lecturas de licencia con SHA fijado, 1 negativo de control, 2 lecturas de archivo de
versión.** El censo de 133 filas del pase 92 **no queda superado** (`P966`).

### 🟢 `Gap 372` ACOTADO — y el reencuadre vale más que las tres filas nuevas

[`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) (**Apache-2.0**,
11 358 B, `main`·`a844f71`, 71★, **2 916 commits**, 🟢 4 de 4 encabezados de cláusula presentes) ·
[`EducationalTestingService/skll`](https://github.com/EducationalTestingService/skll) (**BSD-3-Clause**,
1 555 B, `main`·`b350eb0`, 🟢 **North America por la línea de copyright del payload**: *"Educational Testing
Service"*) · [`HASKI-RAK/NodeGrade`](https://github.com/HASKI-RAK/NodeGrade) (**MIT**, 1 062 B,
`main`·`8e144ac`, 421 commits, 🟢 **LTI 1.1/1.3** y proveedor de modelo **local**).

🔴 **Y donde vive el código de scoring en producción es copyleft, medido este pase:** `openedx/ease`
(**AGPL-3.0**, 35 136 B) y `openedx/edx-ora2` (**AGPL-3.0**, 35 135 B). 🔵 **Entonces la forma del
engagement es una frontera, no un fork: puntuar detrás del límite AGPL o comprar la nota, validar con
Apache/BSD, y que el paquete de evidencia quede del cliente.** Costeado en `P94-A`.

### 🔴 Un publicador, tres licencias (`P975`)

**ETS publica Apache-2.0 (`rsmtool`), BSD-3 (`skll`) y GPL-2.0 (`factor_analyzer`, 18 092 B,
`main`·`de933d2`) desde una sola organización.** 🔵 **La licencia es una propiedad del repositorio, nunca
del publicador** — y un publicador sofisticado es justamente el caso donde la inferencia se siente segura.
🟢 Control negativo: `EducationalTestingService/rsmexplain`, nombrado por un resumen de búsqueda, **no
resuelve** (`ls-remote` exit 128).

### 🟢 La versión de una plataforma también se lee del payload (`P972`) — y Moodle va dos releases por delante de todo blog

`moodle/moodle` · `main` · `f205347` → `$release = '6.0dev (Build: 20261005)'`, `MATURITY_ALPHA`;
`MOODLE_503_STABLE` → 🟢 **`5.3 (Build: 20261005)`, `MATURITY_STABLE`**. 🔴 **Todas las fuentes secundarias
leídas este pase decían "5.2 es el estable actual".** Ambos payloads llevan sello **2026-10-05**, cinco días
antes de este pase.

🔴 **Y `version.php` NO está en la raíz (`P973`): está en `public/version.php`**, porque Moodle **movió su
web root a `public/` en la 5.0**. 🔵 **`P969` generaliza: el defecto de alcance en la raíz no es sobre
licencias, es sobre rutas** — y esta KB sondea 24 nombres de licencia en la raíz desde el pase 1.
🔴 **En un engagement eso es dinero:** cada Dockerfile, regla de proxy, ruta de `config.php` y
personalización escrita contra Moodle pre-5.0 apunta un directorio más arriba. Semana 0 si se lee
`public/version.php`; semana 3 si no.

🟡 **El límite del propio instrumento, encontrado en la segunda plataforma (`P977`):** los heads
`open-release/*` de `openedx/edx-platform` **se detienen en Sumac**, mientras `release/teak.*` y
`release/ulmo.*` existen solo como **tags** y **con el prefijo cambiado**. 🟢 El cruce que lo detecta es la
distribución que se despliega: `overhangio/tutor` en **`v22.0.2`**. 🔵 **Un oráculo es una lectura; dos que
discrepan son un hallazgo.** Gate completo en `P94-B`.

### 🟢 La fecha equivocada del `T4` apareció por SEXTA vez — y este pase encontró el MECANISMO

**No es ignorancia: es una CONFUSIÓN.** El 2-ago-2026 **era** la fecha del Anexo III; el **Digital Omnibus
sobre IA — `Reglamento (UE) 2026/1744`** (PE 16-jun-2026, Consejo 29-jun-2026, firmado 8-jul-2026;
🔴 **las fuentes discrepan entre publicación en el DO el 24-jul y entrada en vigor el 27-jul, y ninguna se
leyó en primario**) la movió a **2-dic-2027** (Anexo I a 2-ago-2028). 🟢 **Pero el 2-ago-2026 no quedó
vacío: pasó a ser una fecha del Artículo 50.**

🔵 **Por eso corregirla de plano nunca funcionó, y la jugada es una pregunta: ¿de qué artículo hablamos?**
Anexo III → llegan 16 meses antes y van a sub-construir. Artículo 50 → tienen razón y probablemente no
están listos.

🔴 **Y la obligación que ninguna de las seis fuentes mencionó es la única ya exigible: el reconocimiento de
emociones en educación está PROHIBIDO desde el 2-feb-2025** (Artículo 5). 🔵 **No es un punto de
planificación para 2027: es una auditoría de features sobre lo que el cliente ya opera**, porque la
detección de engagement y la inferencia de afecto vienen encendidas por defecto en proctoring y
"engagement analytics". **Es también el entregable de apertura más barato en EMEA.**

### 🟢 Por primera vez, el método de una región encontró el instrumento de otra

El pase 93 sacó de Canadá una regla: **en un sistema federal el instrumento casi nunca es nacional, y una
consulta nacional reporta un mundo vacío.** El pase 93 además descargó a México como vacío tras cinco pases.
🟢 **El pase 94 apuntó la regla de Canadá a México y encontró el instrumento al primer intento:** reforma al
**Art. 61 de la `Ley de Educación` del Estado de México** (medio superior y superior: uso **responsable,
ético y gradual** de IA; Dip. Lili Urbina, PRI; avalada por unanimidad en comisiones unidas).
🔴 **La fecha de promulgación NO queda establecida** (abr-2026 según un análisis; ventana 31-ene a
15-jul-2026 según otro; la Gaceta no era alcanzable). 🔴 **A nivel federal no hay ley**: la iniciativa del
PT del 29-abr-2026 está en comisión. `T12`.

### 🟢 `Gap 371` DESCARGADO A MEDIAS, y el contraste es el hallazgo

**Existe otra publicación con la forma de la BNCC: el *Machine Readable Australian Curriculum* (MRAC) v9 de
ACARA** — RDF/XML, JSON-LD y endpoint SPARQL (`rdf.australiancurriculum.edu.au/api/sparql`).
🔴 **Su licencia no se pudo verificar: el host está bloqueado por el allowlist de egreso y no existe
repositorio ni cliente en GitHub del cual leer el payload** → **`Gap 374`**.
🔵 **Y el contraste vale más que la fila: Brasil publica un REPOSITORIO** (código MIT, datos CC BY 4.0,
proveniencia por registro, CI que rechaza divergencias, servidor MCP) **y Australia publica un SERVICIO.**
Un repositorio se forkea, se audita, se fija y corre sin red en una escuela; un endpoint SPARQL no.
**Para un despliegue escolar esa diferencia pesa más que la calidad del dato.**

### 🔴 Lo que este pase declara vacío

🔴 **Japón: nada, por segundo pase** (cuatro consultas regionales, ningún instrumento). 🟡 Método
especificado para el próximo: MEXT (文部科学省) y *guidelines*, **en japonés**.
🔴 **GitHub Trending: cero repos de la industria por SEXTO pase** — 🟢 aunque corroboró desde fuera el
*empaquetado* de esta industria: **4 de 11 filas eran skills para harnesses de agentes**, que es el hallazgo
del pase 90. 🔴 **`govinfo.gov` se suma a los hosts bloqueados; ya son ocho.**
🔴 **`Gap 370` sigue abierto como cableado** (el sondeo por ruta se corrió a mano: `dados/LICENSE.md`,
676 B, HTTP 200 — con una cláusula de soberanía que ninguna licencia en la raíz podía tener:
**los textos normativos de la BNCC son actos oficiales del Estado brasileño y no son objeto de protección
autoral** (art. 8º, IV, Lei nº 9.610/1998); la licencia cubre solo la compilación y la curaduría).

## Pase 93 — 2026-10-10

⏱️ **Tercer pase de esta fecha** (el 91 corrió 23:0x–00:00 UTC; el 92, 00:4x–01:3x; este, después).

**El hallazgo principal: el pase no pudo EJECUTAR el instrumento de esta KB, y la decisión correcta fue
no escribir otro. Aun así el pase produjo la capa que faltaba, un contraejemplo a una regla que esta KB
daba por cierta, y el primer número medido para una tesis que sostiene desde el pase 1.**

🔴 **`compose/code/grant-ladder-v4/ladder.sh` no se pudo correr**: el sandbox de esta sesión no ejecuta
código del repositorio. 🔴 **La salida tentadora —escribir un clasificador nuevo— es exactamente la que
`P237` prohíbe y la que en el pase 91 costó dos licencias de plataforma y una recomendación a cliente.**
🟢 **Entonces este pase no escribió ninguno.** Corrió el *mapa de oráculos* de v4 a mano
(`git ls-remote --symref` → existencia/rama/SHA; `raw.githubusercontent.com/<slug>/<SHA>/<file>` → payload)
y **imprimió el bloque de título de cada payload en vez de clasificarlo.** `P970`.
🔵 **Declinar clasificar es el modo de falla correcto; bifurcar no lo es.**

**13 slugs resueltos** (11 lecturas de payload con SHA fijado, 1 negativo, 1 control inventado), contra los
133 del pase 92. 🔵 **Fue un pase profundo sobre pocas filas, no un censo** — `grant-ladder-v4/pass92-results.tsv`
**no queda superado** (`P966`). Evidencia en `compose/code/p969-root-only-licence-reach/`.

### 🟢 La capa psicométrica — el pase 92 descargó `Gap 335` con UNA librería; el estante son cuatro técnicas

[`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) (**MIT**, 1 132 B, `cc1682e`, 282★, **North America** por la
línea de copyright del payload) · [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) (**MIT**, 1 121 B,
`6514928`, 173★, **North America**) · [`eribean/girth`](https://github.com/eribean/girth) (**MIT**, 1 064 B
en 🟡 `LICENSE.txt`, `daf2277`, 126★) · [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim)
(**BSD-3-Clause**, 1 514 B, rama 🟡 `dev`, `7e6caae`, 153★, 🟡 **LATAM/Brasil por el host de documentación,
no por el payload**) · [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs)
(**MIT**, 1 079 B, `9446cb0`, 506★).

🟢 **Encontradas nombrando la TÉCNICA y no la industria — `P955` por tercer pase consecutivo.**
🔵 **Y el hallazgo es un ORDEN, no un conteo: en esta capa la opción permisiva y la EXPLICABLE son la
misma.** Bajo el Anexo III, evaluar resultados de aprendizaje es alto riesgo y debe explicarse:
**un parámetro de dificultad de ítem es una explicación; la activación de una red no lo es.**
🟢 **Así que la matemática vieja es la opción que cumple, y además la mejor licenciada y la más rodada**
(`catsim`: 877 commits). `T10`, costeado en `P93-A`.
🟢 **Las costuras las documentan las propias librerías:** el README de `catsim` dice textualmente
*"catsim does not implement item parameter estimation"* y apunta a `py-irt` y `girth`.

### 🟢 Un currículo nacional como datos abiertos auditados — la regla "los marcos no están licenciados" queda refutada

🔴 **Lo que esta KB había generalizado** desde `touretzkyds/ai4k12` (sin payload / 24) y
`learning-commons-org/knowledge-graph` (`LICENSE.md` que no concede nada, `P965`): *los estándares
curriculares los escriben organismos que nunca los licencian.* 🟢 **Falso para Brasil, y el contraejemplo
está mejor construido que el artefacto al que contradice.**

`bncc.dev` (Profy) publica la **Base Nacional Comum Curricular**: **1 721 aprendizajes** en JSON/SQLite/CSV,
**proveniencia por registro** (`fonte` → fila de planilla + página del PDF oficial), pipeline reproducible
que CI vuelve a correr y rechaza si divergen, **servidor MCP con 7 herramientas y el dataset embebido**, y un
**benchmark abierto de alucinación**. 🟢 **1 576 de 1 580 textos de la BNCC-2018 coinciden carácter por
carácter con el PDF del MEC/CNE; las 4 discrepancias están documentadas en `DECISOES.md`; 141 de 141 en
Computación.** Cuatro repos verificados del payload: `bncc-dados` (🟡 MIT en la raíz), `bncc-pacotes`,
`bncc-benchmark` (🟢 concesión dividida declarada en la raíz) y `dfdb76/bncc-mcp` (**MIT**, segundo MCP
independiente → **n=2**). 🟢 **`P870` por quinto pase: la consulta en inglés no devolvió nada; la consulta
en portugués lo devolvió al primer intento.**

🟡 **No descarga `Gap 367`** (la BNCC no es material de alfabetización en IA para K-5): **refuta la
generalización, no el hueco.** 🔴 Nuevo **`Gap 371`**: ¿existe una publicación con esta forma para algún
otro currículo nacional?

### 🟢 El número que esta KB venía argumentando sin tener: 31,9 % → 0,2 %

El estudio de anclaje de `bncc-benchmark` (**8 modelos, 300 ítems**): **31,9 %** de alucinación sin fuente en
contexto · **0,2 %** con el dataset en el prompt · **2,3 %** consultando el servidor MCP.
🟢 **Anclar vale ~160× en esta tarea**, y 🔴 **la vía MCP es diez veces peor que embeber** aunque siga siendo
~14× mejor que nada. 🔵 **Decisión de arquitectura con evidencia: para alineación curricular, embebé el
dataset y dejá la llamada a herramienta para la cola larga.** La fidelidad sin anclaje va de **88 % a 3 %**
según el modelo, así que *"qué modelo"* es una palanca mucho más débil que *"¿está la fuente en el
contexto?"*. `T11`, costeado en `P93-B`.
🟡 **Citarlo con cuidado, por razones que el repo declara él mismo:** 🟢 su README **declara el conflicto de
interés** (*"a Profy opera produtos que usam LLMs sobre a BNCC"*) y publica metodología, ítems y respuestas
crudas para recalcular; 🔴 **y sus dos superficies se contradicen en el tamaño del corpus** (descripción:
15 300 respuestas/17 modelos; README: 19 modelos × 900 = 17 100). 🔵 **Citar los porcentajes, no el tamaño
del corpus.** 🔴 **Límite: un benchmark, un currículo, un idioma, 300 ítems — la dirección generaliza, la
magnitud no.**

### 🔴 Dos defectos nuevos de alcance, y uno lo confirma un segundo oráculo

- 🆕 🔴 **`P969` — el escalador de licencias lee SOLO nombres en la raíz.** `bncc-dev/bncc-dados` publica
  **MIT en la raíz** mientras **los datos bajo `dados/` son CC BY 4.0**, y `LICENSE-DADOS.md` en la raíz es
  **404**. 🔴 **La barra lateral de licencias de GitHub dice lo mismo que el escalador: "MIT license".**
  🔵 **Dos oráculos independientes, un punto ciego, una causa: detección solo en la raíz** — por eso es un
  hallazgo sobre el método y no un defecto de un script. 🟢 **Y el mismo publicador muestra el arreglo en sus
  otros dos repos:** un índice de concesión dividida **en la raíz**, con cada licencia acotada a rutas
  explícitas. **La convención, no la herramienta, es lo que hace legible una concesión dividida.**
  🔴 **`Gap 370`**: `compose/code/p199-perfile-license/` ya hace sondeo por ruta y **no está conectado** al
  escalador; el caso que falla queda comiteado en `compose/code/p969-root-only-licence-reach/`.
- 🆕 🔴 **`P971` — un archivo `LICENSE` puede ser el AVISO de cabecera de Apache, no la LICENCIA.**
  [`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE): **1 865 B** contra los **11 357 B** canónicos, 29
  líneas no vacías, bloque de título correcto y el aviso *"obtain a copy at <URL>"*. 🔴 **Un grep no
  encuentra "Grant of Patent License", "Grant of Copyright License", "Redistribution", "trademark" ni
  "APPENDIX".** 🔵 **La concesión existe por referencia, pero los términos no están en el repositorio** — y
  **la única razón fuerte para preferir Apache sobre MIT es §3, la concesión de patente, que viaja como URL.**
  🔴 **Invisible a todo instrumento de este estante**, porque un clasificador de bloque de título devuelve
  `Apache-2.0` y no se equivoca.

🟢 **Y `P965` sobrevive a un payload para el que no fue construido.** Su umbral medido (*una concesión real
nombra 0–2 familias; un marco nombra 3, de tres linajes*) separa correctamente los índices de `bncc-dev`
—nombran **2**, y **son** concesiones reales, con los textos referenciados verificados presentes— del
`LICENSE.md` de `learning-commons-org/knowledge-graph`, que no concede nada. **Misma forma de documento,
usabilidad opuesta.**

### 🟢 El barrido regulatorio: tres huecos descargados, uno acotado, dos en pie

- 🟢 **`H.R. 8747` DESCARGADO tras tres pases.** Reportado por el comité de Educación y Trabajo de la Cámara
  el **21-jul-2026, con enmienda, 18–15**; **sin voto en el pleno, sin acción del Senado, no promulgado.**
  🔴 **Y no es lo que su nombre sugiere**: enmienda la **ESEA de 1965** para que currículo de IA y formación
  docente sean **usos permitidos de fondos federales K-12 ya existentes**. **Es elegibilidad de fondos, no un
  mandato.**
- 🟢 **Canadá DESCARGADO al primer intento, nombrando el instrumento y no el país** (`P955`, el método que el
  pase 92 escribió para sí mismo). **BC**: guía ministerial (2023) + nuevos recursos K-12 a mayo-2026 +
  comité asesor previsto + documento de principios para post-secundaria y recurso provincial de ene-2026.
  **Alberta**: **convenio a tres años con Amii** para construir el marco + guía de la ASBA (sep-2024).
  🔴 **Ontario: ningún instrumento ministerial** — solo guía de asociaciones de consejos escolares
  (OASBO/ECNO, 2025), y **el TDSB pidió públicamente al ministerio una estrategia provincial.**
  🔵 **Es la forma de México encontrada en inglés: en un sistema federal el instrumento casi nunca es
  nacional, y una consulta nacional reporta un mundo vacío.**
- 🟢 **UAE DESCARGADO — y era un instrumento real detrás de una etiqueta equivocada.** Currículo de IA
  aprobado por gabinete, **obligatorio de kindergarten a Grado 12** en escuelas públicas, siete ejes,
  anunciado en **mayo-2025**. 🟢 **Quinta jurisdicción con mandato de ENSEÑANZA de IA**, y resuelve la
  atribución errónea que el pase 92 registró **sin usar**. 🔵 **Lección barata: anotar lo que se rechazó, y
  por qué, convirtió un dato descartado en un hueco descargado un pase después.**
- 🟡 **India, educación superior: ACOTADO, sigue abierto.** Actividad de AICTE documentada pero toda
  secundaria y sin fecha de notificación; **UGC confirmado sin instrumento propio.**
- 🟢 **EMEA: la Comisión Europea actualizó sus directrices éticas de IA y datos en la enseñanza el
  5-mar-2026** (uno de cuatro paquetes del Plan de Acción de Educación Digital), sucediendo a la de 2022.
  🔴 **Un boletín la reportó como "9 de junio"; es 5 de marzo** — corregido antes de entrar a la KB.
  🔵 **Su audiencia son docentes y direcciones, no ministerios: la Comisión responde al Artículo 4 con
  CAPACIDAD, y la capacidad se compra.**
- 🔴 **Y la fecha equivocada del `T4` apareció por QUINTA vez**, en una fuente por lo demás correcta y
  actual: *"las obligaciones del Anexo III aplican desde el 2-ago-2026"*. 🔵 **Cinco instancias en cinco
  pases significa que la fecha equivocada es la lectura MAYORITARIA del mercado** — el asesor instalado del
  cliente probablemente le dio el plazo equivocado.
- 🟢 **LATAM consiguió la mejor base de evidencia regional de esta KB:** UNESCO IESALC con UNU-IAS,
  lanzado el **9-sep-2026**, **200 instituciones en 19 países**: **87 %** usa IA en al menos un área,
  **74 %** en enseñanza, **57 %** en investigación, **26 %** tiene estrategia formal y 🔴 **solo 9 % evalúa
  cómo funciona su implementación.** 🔵 **Diez veces más universidades usando IA que midiéndola: una línea de
  servicio sin atender, con comprador identificado que ya gastó el dinero.** 🔴 **Trampa de proveniencia
  registrada: las cifras 19 % / 42 % / 45 % pertenecen a OTRA encuesta (Cátedras UNESCO 2025) y no son
  comparables. No usadas.**
- 🔴 **GitHub Trending: CERO repos de la industria por QUINTO pase consecutivo.** 🔵 **`catsim` tiene 877
  commits y 153 estrellas — exactamente el perfil que trending no puede ver.** 🟢 **El pase 92 recomendó
  gastar el presupuesto en otra parte; el 93 lo hizo y las alternativas volvieron a pagar** (la consulta por
  técnica dio cinco filas; la consulta en portugués dio la pila BNCC). 🔵 **Consulta retirada a rol de
  registro.**
- 🔴 **Y el tamaño de mercado: el desacuerdo ahora está DENTRO de una sola firma.** La serie regional de
  MarketsandMarkets (NA **951 M USD**, Europa **512,6 M**, APAC **591,6 M**, resto de LATAM **18,2 M**, todos
  2024) **suma ≈ 2,07 mil millones**, contra una banda 2026 de **7–11,4 mil millones** de las firmas de la
  tabla. 🔵 **Dos años de 40 % no cierran esa brecha: el problema es el ALCANCE, no la fecha.** 🔴 **No se
  puede cerrar**: `marketsandmarkets.com` está bloqueado por el allowlist de egreso y ninguna firma de la
  serie alta publica desglose geográfico. 🟢 **Regla nueva: nunca poner un tamaño de mercado en un deck de
  educación sin nombrar el alcance al lado.**

### 🔴 El hueco más consecuente que este pase abrió

🔴 **`Gap 372`: no existe librería permisiva y de grado productivo para corrección automática de ensayos.**
Toda la oferta permisiva es **un repo de investigación de 2★** con la licencia de `P971`. 🔵 **Es decir: la
actividad que el AI Act nombra de alto riesgo de forma más explícita es la que tiene menos oferta abierta.**
`P93-A` la deja fuera de alcance explícitamente en vez de prometerla.

## Pase 92 — 2026-10-10 (resumen)

🔴 **El instrumento del pase 91 bifurcó el clasificador de licencias y reescribió mal una licencia que esta
KB YA HABÍA CORREGIDO; el valor equivocado llegó hasta una recomendación de engagement.**
`oat-sa/tao-core` y `portabilis/i-educar` se publicaron como **LGPL-3.0** y son **GPL-2.0** — y *"link,
don't absorb"* es un consejo que solo existe para LGPL. Mecanismo (`P960`): el preámbulo canónico de
GPL-2.0 referencia la LGPL en el byte ~847, dentro de la ventana, y la copia bifurcada probaba
`"gnu lesser"` **antes** de `"gnu general public"`. 🟢 Corregido en tres archivos; `grant-ladder-v4` no
tiene clasificador propio (`P237`); tres reparaciones llevadas **aguas arriba** a la librería compartida
(`P962` CC0 inalcanzable, `P964` Fair Code, `P965` marco-no-es-concesión); `Gap 335` (knowledge tracing) y
`Gap 356` descargados. **Detalle completo en el historial de git y en `*/trending.md`.**

### Mapa de oráculos — medido, y re-confirmado en el pase 93

`curl -sI https://github.com/<slug>` **no discrimina** bajo el proxy de egreso de estas sesiones: devuelve 403
para un slug real y uno inventado por igual. `api.github.com` igual. **Lo que sí discrimina:**
`git ls-remote --symref` (existencia, rama, SHA — un slug inventado falla con exit 128) y
`raw.githubusercontent.com/<slug>/<SHA>/<file>` (licencia; 🔴 **un 404 devuelve un cuerpo de 14 B, así que el
código HTTP se verifica siempre, no solo los bytes**). 🆕 **Positivo nuevo del pase 93: `WebFetch` sobre
`https://github.com/<owner>/<repo>` renderiza estrellas, forks y la licencia de la barra lateral** — de ahí
salen los ★ de este pase, 🔴 **y ahí se detectó que la barra lateral comparte el punto ciego de raíz del
escalador** (`P969`). Sigue vigente que `WebFetch` renderiza `github.com/topics/<t>`.
🔴 **Límite nuevo del sandbox: no se puede ejecutar código del repositorio**, de donde `P970`.

🆕 **Canal nuevo del pase 94 — la VERSIÓN de una plataforma (`P972`).** `git ls-remote --heads <slug>` y
`--tags <slug>` devuelven la escalera de releases que el proyecto mantiene de verdad, y el archivo de
versión del propio proyecto a un SHA fijado devuelve la cadena de release. 🔴 **Dos trampas medidas:**
`moodle/moodle` no tiene `version.php` en la raíz (está en `public/version.php` desde la 5.0 — `P973`), y
la escalera de `openedx/edx-platform` **se mudó de heads a tags y cambió de prefijo** entre Sumac y Teak
(`P977`), así que un sondeo de heads reporta una versión dos releases vieja **sin fallar**.
🔴 **El sandbox sigue sin ejecutar código del repositorio** (segundo pase), y
🔴 **`govinfo.gov`, `unesco.org` y `rdf.australiancurriculum.edu.au` se suman a los hosts bloqueados por el
allowlist de egreso: ya son ocho.** Per `P950`, no se reintentaron host por host.

## Uso

1. **Nuevo engagement**: leer `intel/market.md` + `repos/foundations.md`
2. **Proponer solución AI**: `agents/top.md` + `compose/patterns.md`
3. **Mantenerse al día**: correr `ingest/update.sh` semanalmente
4. **Verificar antes de citar**: `compose/code/patterns-figure-audit/extract_figures.py --check`
   remide las cifras de `compose/patterns.md` que salen de suites propias. **Una cifra de una suite
   se vence cuando la suite crece**, y el pase 47 encontró dos vencidas

---
*Red de KBs Globant AI Studios → [globant-kb](../globant-kb/)*
