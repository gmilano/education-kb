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

## Uso

1. **Nuevo engagement**: leer `intel/market.md` + `repos/foundations.md`
2. **Proponer solución AI**: `agents/top.md` + `compose/patterns.md`
3. **Mantenerse al día**: correr `ingest/update.sh` semanalmente
4. **Verificar antes de citar**: `compose/code/patterns-figure-audit/extract_figures.py --check`
   remide las cifras de `compose/patterns.md` que salen de suites propias. **Una cifra de una suite
   se vence cuando la suite crece**, y el pase 47 encontró dos vencidas

---
*Red de KBs Globant AI Studios → [globant-kb](../globant-kb/)*
