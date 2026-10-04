---
industry: education
region: Global
updated: 2026-10-04
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

Cada carpeta trae su propio `README.md`, su suite y el comando que la reproduce. **Las cifras de
aserciones se publican con su invocación**, porque varias dan un número distinto según el argumento
o la variable de entorno (regla de **P107**, pase 47):

| Carpeta | Qué prueba | Invocación | Hoy |
|---|---|---|---|
| `aiact-50-2-pack/` | marca un paquete SCORM ya construido, con un portador por dialecto | `python3 test_pack.py` | **27/27** |
| ídem, conformidad real | ídem + `xmllint` contra los XSD de los **dos** dialectos | `SCORM_SCHEMAS=… SCORM_SCHEMAS12=… python3 test_pack.py --with-xmllint` | **37/37** |
| `aiact-50-2-marking/` | mapea los 9 valores de `lineage-skill` a `synthetic` + etiqueta | `python3 test_marking.py` | **23/23** |
| ídem, conformidad real | ídem + el fragmento de manifiesto | `SCORM_SCHEMAS=… python3 test_marking.py --with-xmllint` | **24/24** |
| `aiact-50-2-spans/` | ¿alguna pieza expuesta emite límites de tramo? | `sh scan_spans.sh` | 🔴 **0 de 33** |
| `aiact-50-2-exposure/` | ¿cuántas filas ponen contenido sintético delante de alguien? (el **reparto**, leído de `rows.tsv`) | `python3 test_exposure.py` | **11/11** → 🔴 **33 de 66 (50 %)**, corregido en el pase 56 |
| ídem, los **artefactos** de marcado en el árbol clonado de las 33 expuestas | lo que `scan_marking.sh` mide de verdad — **no** produce la cifra del reparto | `sh scan_marking.sh` | **0** artefactos de marcado / 15 de procedencia |
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
| `trend-backlink-audit/` | cada tendencia citada tiene su sección y su evidencia | `python3 test_trends.py` | **22/22** |
| **`suite-total-control/`** | **la regla de P126: un contador por vocabulario acierta en `PASS` y FALLA en `ok`; el lector del total propio acierta en los dos** | `python3 test_control.py` | **10/10** |
| **`p183-nongithub-denominator/`** | **la capa de PAQUETE: que la pregunta de la DECLARACIÓN rechace los 7 tokens con FORMA de paquete que no lo son, y que el *build* por forma los acepte** | `python3 test_denominator.py` | **15/15** ✅ *(nuevo en el pase 66)* |
| **`p184-holder-mismatch/`** | **el TITULAR de un archivo de licencia, y que el instrumento SE NIEGUE a contestar sin la familia en vez de publicar una frase del texto Apache o el copyright de la FSF** | `python3 test_holder.py` | **15/15** ✅ *(nuevo en el pase 66)* |
| **`p228-segmented-coverage/`** | **los controles de P227+P228: el conjunto de archivos NOMBRADO, y la negativa a ordenar una cuota en USUARIOS contra una en INSTITUCIONES** | `python3 test_coverage.py` | **15/15** ✅ *(nuevo en el pase 75)* |
| ídem, la reproducción del agregado del pase 74 contra el commit que citó | `python3 reproduce_p224.py` — **182** subconjuntos evaluados, **1** reproduce `229/389` | `python3 reproduce_p224.py` | **3/3** ✅ *(nuevo en el pase 75)* |
| ídem, la medición por cohorte **en un commit fijo** (el commit es parte de la invocación: ver tendencia **593**) | inversiones por `(segmento, unidad)` | `python3 measure.py --at 5dd2bcc` | 🔴 **7** en K-12 / 🟢 **1** en superior |
| **`p243-frontmatter-coverage/`** | **la cobertura de *frontmatter* sobre los 56 `.md`, y el control NEGATIVO que importa: que 7 variantes de vocabulario regional (`Latam`, `Europe`, `Asia Pacific`, `Brazil`…) sean RECHAZADAS** | `python3 test_check_frontmatter.py` | ⚠️ **sin medir — ver abajo** *(nuevo en el pase 79)* |


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
