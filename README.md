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

## Pase 92 — 2026-10-10

⏱️ **Segundo pase de esta fecha** (el 91 corrió 23:0x–00:00 UTC; este, 00:4x–01:3x UTC).

**El hallazgo principal: el instrumento del pase anterior BIFURCÓ el clasificador de licencias, y al
re-derivar el estante volvió a escribir mal una licencia que esta KB YA HABÍA CORREGIDO. El valor
equivocado llegó hasta una recomendación de engagement.**

🔴 **`grant-ladder-v3` escribió su propio clasificador de 30 líneas en vez de usar el compartido
`compose/code/lib/license_family.sh`. `P237` existe exactamente para prohibir eso**, y la cabecera de
ese archivo ya registra que el pase 77 lo había hecho una vez.

| fila | el pase 91 publicó | el bloque de título del payload dice |
|---|---|---|
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🔴 `LGPL-3.0` · *"LGPL: linkable"* | 🔴 **GNU GENERAL PUBLIC LICENSE, Version 2** → **GPL-2.0** |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 `LGPL-3.0` · *"link, don't absorb"* | 🔴 **Version 2, June 1991** → **GPL-2.0** |

- 🔴 **El mecanismo es `P171` sobre un par que `P171` nunca cubrió.** El **preámbulo** canónico de
  GPL-2.0 dice *"(Some other Free Software Foundation software is covered by the **GNU Lesser General
  Public License** instead.)"* en el **byte 847** (`tao-core`) y **849** (`i-educar`) — dentro de la
  ventana de 4.000 B — y la copia bifurcada probaba `"gnu lesser"` **antes** de `"gnu general public"`.
  **Todo payload GPL-2.0 canónico trae esa frase, así que el defecto era universal.**
- 🟢 **Y el control está en la misma clase de veredicto y la misma corrida:** `rosariosis` también es
  GPL-2.0, pero su texto variante de 15.214 B **no contiene `"gnu lesser"` en absoluto** (offset `-1`),
  así que el mismo clasificador devolvió `GPL` a secas. 🔵 **Un instrumento, un pase, una familia, dos
  veredictos — decididos por si una frase de referencia cruzada estaba presente.**
- 🔴 **El costo NO fue interno.** `verticals/solutions.md` recomendaba por nombre *"para un **SIS público
  brasileño** → `i-educar` (**LGPL-3.0**) — **link, don't absorb**"*, y `compose/patterns.md` construyó
  `P91-E` sobre *"LGPL-3.0 permite exactamente eso, y **esta distinción hace posible el engagement**"*.
  **"Link, don't absorb" es un consejo que sólo existe para LGPL; GPL-2.0 no tiene excepción de
  enlace.** 🟢 Los tres archivos corregidos; `P91-E` re-presupuestado sobre una frontera de servicio,
  con el aumento de costo dicho explícitamente.
- 🔵 **Y esta KB ya sabía las dos respuestas:** `repos/trending.md` publicó *"la fila que decide un
  proyecto: `oat-sa/tao-core` es GPL-2.0"*, derivada —en sus propias palabras— *"por reusar el
  clasificador compartido `lib/license_family.sh` (`P237`) en vez de reescribirlo"*.
  🔴 **Las correcciones existían y un instrumento nuevo las sobrescribió.** `P960` / `P963`.

**Dos huecos descargados, y uno de ellos es el más viejo del estante:**

- 🟢 **`Gap 335` (knowledge tracing) DESCARGADO tras OCHO pases sin tocar.**
  [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (**MIT**, 1.066 B, `77c3e90`,
  ~430★) — la librería de referencia de *deep knowledge tracing* (NeurIPS 2022): DKT, DKVMN, SAKT,
  SAINT, AKT, GKT, LPKT sobre 7 datasets. 🟢 **Encontrada con la primera consulta que nombró la
  TÉCNICA en vez de la industria** — `P955` por segundo pase consecutivo. Nuevo **Tier 2b** en
  `repos/foundations.md` y patrón **`P92-A`** en `compose/patterns.md`.
- 🟢 **`Gap 356` DESCARGADO con una compuerta que falla en su primera corrida.**
  `compose/code/p963-shelf-licence-agreement/`: **4 MISMATCH antes de las correcciones de este pase, 0
  después.** 🔵 Se arrastró cuatro pases con la nota *"habría cazado `P953` y `P957`"* — **este pase
  habría cazado `P960`, cuyo costo fue una recomendación equivocada a un cliente.**
  🔴 **Y encontró un defecto en SÍ MISMA:** leyó `frappe/lms` como **MIT** —el reclamo *refutado* en una
  tabla *"lo que se afirma | lo que dice el payload"*— **castigando justo a las filas que habían hecho
  el trabajo.** 🟢 Arreglado con la convención del propio estante: **una celda de veredicto trae bytes,
  una celda que cita a otro no.** `P967`.

**Tres reparaciones llevadas DE VUELTA al clasificador compartido, porque reusar OBLIGA a reparar:**

- 🆕 **`P962` — la rama CC0 de `lib` era INALCANZABLE para su propio texto canónico.** Estaba anidada
  dentro de una compuerta que exige `Creative Commons`/`CC BY` en la ventana de 4.000 B. En el payload
  real: **`CC0` en offset 0**, **`creative commons` en 6.227** (afuera, por 1,6×), **`CC-BY` ausente del
  archivo entero.** 🔵 **Y la única mención es la cláusula que DESLIGA a Creative Commons** — *"Creative
  Commons is not a party to this document"*. **La compuerta estaba condicionada a un descargo de
  responsabilidad, no a una concesión.** 🔴 **Y la suite de `lib` pasaba 199/199 igual, porque su
  fixture de CC0 es una línea escrita a mano que ABRE con el token de la compuerta.**
- 🆕 **`P964` — reusar SOLO habría PERDIDO una familia que la copia bifurcada sí conocía.** `lib` tenía
  BUSL/Elastic/PolyForm pero **no Fair Code ni Sustainable Use**, así que `leemonade/leemons` caía de
  `FAIRCODE-NOT-OSI` a `UNCLASSIFIED` — y `UNCLASSIFIED` cae al token-match comercial, donde el cuerpo
  de la SUL **concede** uso *"for commercial purposes"* antes de restringir la reventa.
  🔵 **Ninguno de los dos clasificadores dominaba al otro. La lección no es «reusar siempre gana»: es
  que reusar OBLIGA a reparar.**
- 🆕 **`P965` — un archivo en un nombre de licencia puede ser un MARCO, no una concesión.** El
  `LICENSE.md` de `learning-commons-org/knowledge-graph` no concede nada: explica licenciamiento por
  dataset y termina en **"Gated content isn't yours to redistribute by default"**. 🔴 **Clasificarlo
  devolvía `CC0-1.0` — la familia más permisiva que el documento MENCIONA — sobre un payload cuyo
  término operativo es el opuesto.** 🟢 **Umbral MEDIDO, no elegido** (toda concesión real nombra 0–2
  familias; el marco nombra 3 de tres linajes) **y posición MEDIDA también** (MPL-2.0 nombra las tres
  marcas GNU en su §1.12, así que un umbral temprano se comería todo payload MPL-2.0).

**Otros resultados del pase:**

- 🔴 **`Gap 367` apuntado y ENDURECIDO.** Una consulta K-5 devolvió **cero repositorios de GitHub**;
  toda la oferta permisiva de currículo es para desarrolladores adultos. 🟢 Alternativa nombrada: **MIT
  Day of AI** (`dayofai.org`, **CC**) + Code.org, sobre las **AI4K12 Five Big Ideas**. 🔴 **Y el repo del
  marco está sin licencia:** [`touretzkyds/ai4k12`](https://github.com/touretzkyds/ai4k12) (AAAI/CSTA) →
  **sin payload / 24**. 🔵 **Es la forma de `Gap 354` otra vez: cuatro jurisdicciones obligan a enseñar
  IA y el marco de referencia no se puede redistribuir en un entregable.**
- 🟢 **APAC cambió de régimen, y es el cambio regulatorio más grande del pase.** **Corea del Sur**
  (AI Basic Act **vigente 22-ene-2026**, con **un año de gracia en sanciones**), **Vietnam** (primera ley
  de IA de Sudeste Asiático: **educación es alto riesgo** junto a finanzas y salud — registro previo en
  la **National AI Database**, supervisión humana obligatoria y **reporte de incidentes en 72 h**, plazo
  **sep-2027**) y **Taiwán** (dic-2025). 🔵 **Mercado distinto al de los mandatos curriculares:
  gobernanza y auditoría, no contenido.** 🔴 **Y la región NO converge** — Japón y Singapur siguen
  voluntarios: *"cumplimiento APAC"* no es un producto. `T8`.
- 🟢 **EMEA: `Jisc` reportó resultados preliminares en mayo-2026 de pilotos de corrección con IA de un
  año en **38 colleges y universidades del Reino Unido***. 🔵 **Es exactamente la actividad que el Anexo
  III clasifica como alto riesgo** (evaluar resultados de aprendizaje, admisiones, proctoring), y lo que
  **sí** vincula hoy es el **Artículo 4** y la **prohibición de reconocimiento de emociones** (ambos
  vigentes desde 2-feb-2025), no el diferimiento a dic-2027. `T9`.
- 🟢 **LATAM: México por fin tiene instrumento, y es SUB-NACIONAL** — el **Estado de México** reformó el
  **Artículo 61** de su Ley de Educación en **abril de 2026**, primer estado en legislar IA en el aula.
  🔵 **`P870` por quinta vez, con la demostración más limpia:** la consulta en inglés devolvió nada
  durante cinco pases; **la consulta en español devolvió una reforma fechada a nivel de artículo en el
  primer intento.** 🟢 Y la referencia regional que faltaba: **`AyudantIA` (PUC de Chile)**, tutores por
  curso que **el profesor configura y ancla en su propia bibliografía** — ~170-194 agentes, ~100 cursos,
  2.300-4.600 estudiantes.
- 🟢 🆕 **Fila LATAM nueva y permisiva de punta a punta:**
  [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (**MIT**, `032b5aa`, Universidad
  Tecnológica de Pereira, **Colombia**) — tutor autónomo para **educación superior rural en Risaralda**,
  **integrado con Open edX**. Región tomada de la línea de copyright del payload, no inferida (`P800`).
- 🔴 **GitHub Trending: CERO repos de la industria educativa, cuarto pase consecutivo.** 🔵 **Cuatro
  negativos idénticos son una propiedad del CANAL, no de la industria** — trending mide velocidad de
  popularidad y los repos de esta industria son chicos, institucionales y lentos. 🟢 **Recomendación
  registrada: dejar de gastar el presupuesto del pase en esa consulta** y usarlo en una página
  `topics/<spec>` o en una consulta en español/portugués — las dos dieron filas este pase.
- 🔴 **`P966`: el archivo de censo del pase 91 era un log, no un censo** — **123 filas, 122 slugs
  únicos**, reclamo publicado de *"120 slugs resueltos"*, y `leemonade/leemons` **dos veces con dos
  veredictos distintos al mismo SHA**. `pass92-results.tsv`: **133 filas, 133 slugs únicos**, afirmado.
- 🟡 **`P961`: el piso de bytes es parte del alcance** — v3 aceptaba sólo `>200 B` publicando *"24
  nombres"*. 🔵 **Efecto medido sobre este corpus: CERO.** Ningún payload del estante está entre 1 y
  200 B. **Se reporta como defecto latente que no costó nada, en vez de inflarlo a corrección.**

## `compose/code/grant-ladder-v4/` — el instrumento

🟢 **v4 no tiene clasificador propio: hace `. ../lib/license_family.sh` (`P237`).** Mantiene lo que v3
hizo bien (SHA fijado, alcance imprimible) y **publica el alcance COMPLETO**:
`--reach` → `names=24 byte-floor=1B classifier=lib/license_family.sh`.
Las reparaciones van **aguas arriba**, a la librería compartida, nunca a una copia.
**Suites: `lib` 199/199, v4 16/16** (7 payloads reales que el pase 91 leyó mal o bien, el marco de
`P965`, la familia de `P964`, y **7 controles negativos** que la nueva ancla CC0 no debe robar).
Control de dos lados: `moodle/moodle` → `COPYING.txt` **35.147 B** (décima reproducción, idéntico byte a
byte) y dos slugs inventados `ABSENT`.

### Mapa de oráculos — medido, y re-confirmado en el pase 92

`curl -sI https://github.com/<slug>` **no discrimina** bajo el proxy de egreso de estas sesiones: devuelve 403
para un slug real y uno inventado por igual, y con `-sI` imprime solo el `200 Connection Established` del
proxy — que pases anteriores tomaron por una página viva. `api.github.com` igual. **Lo que sí discrimina:**
`git ls-remote --symref` (existencia, rama, SHA) y `raw.githubusercontent.com/<slug>/<SHA>/<file>` (licencia).
Control de dos lados en cada corrida. Ver `compose/code/grant-ladder-v4/README.md`. 🆕 **Y un positivo nuevo en el mapa de oráculos: `WebFetch`
renderiza `github.com/topics/<t>` con estrellas y el total del topic, mientras `curl` en la misma URL da 403.**

## Uso

1. **Nuevo engagement**: leer `intel/market.md` + `repos/foundations.md`
2. **Proponer solución AI**: `agents/top.md` + `compose/patterns.md`
3. **Mantenerse al día**: correr `ingest/update.sh` semanalmente
4. **Verificar antes de citar**: `compose/code/patterns-figure-audit/extract_figures.py --check`
   remide las cifras de `compose/patterns.md` que salen de suites propias. **Una cifra de una suite
   se vence cuando la suite crece**, y el pase 47 encontró dos vencidas

---
*Red de KBs Globant AI Studios → [globant-kb](../globant-kb/)*
