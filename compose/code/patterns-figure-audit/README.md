---
industry: education
region: Global
updated: 2026-10-02
---

# Las cifras de `compose/patterns.md` y su instrumento — gap 101, cerrado con un barrido repetible

**Pase 47 del 2026-10-02, acción 2.** El pase 46 dejó el aviso: **«481 / 912 líneas» era
correcto y su métrica no estaba escrita**, así que durante tres pases nadie podía reproducirla
—`wc -l` da 583 / 1.116— y una propuesta que la citara habría defendido un número que no cerraba.
La acción pedía listar toda cifra de `patterns.md` que sea una **medición** y escribirle **con
qué comando se obtiene**. Hecho, y como **script** en vez de lista, porque una lista se vuelve a
vencer el pase que viene.

```sh
python3 extract_figures.py            # el inventario por unidad, con su instrumento
python3 extract_figures.py --check    # + vuelve a correr los instrumentos locales
python3 extract_figures.py --tsv      # una fila por cifra, legible por máquina
```

## 🟢 Pase 48: el barrido pasa de UN archivo a los OCHO, y el defecto real resulta otro

```sh
python3 extract_figures.py --all        # inventario por archivo, los ocho
python3 extract_figures.py --crossref   # re-corre las 8 suites y atribuye cada cita
python3 extract_figures.py <ruta>       # cualquier archivo suelto
```

**El inventario completo: 3.611 mediciones en 35.376 líneas.**

| Archivo | Líneas | Cifras | Cifras / kilolínea |
|---|---|---|---|
| `agents/top.md` | 2.191 | 405 | 🔴 **184,8** |
| `intel/market.md` | 5.232 | **907** | 🔴 **173,4** |
| `agents/trending.md` | 5.495 | 522 | 95,0 |
| `intel/trends.md` | 8.010 | **750** | 93,6 |
| `verticals/solutions.md` | 1.785 | 144 | 80,7 |
| `repos/trending.md` | 3.945 | 295 | 74,8 |
| `repos/foundations.md` | 2.855 | 205 | 71,8 |
| `compose/patterns.md` | 5.863 | 383 | 🔵 **65,3** |
| **TOTAL** | **35.376** | **3.611** | **102,1** |

🔴 **Dos hallazgos de escala:**

1. **El pase 47 barrió `compose/patterns.md` por ser el activo más citado, y es el archivo con MENOR densidad de
   cifras de los ocho.** Los dos que nunca se barrieron, `intel/market.md` e `intel/trends.md`, suman **1.657 cifras —
   el 46 % de la base.**
2. 🔴 **1.836 de 3.611 (el 50,8 %) NO son re-verificables en este entorno:** **1.042** `★`, **418** `commits`,
   **326** conteos de `tools`, **50** descargas. Las **1.775** restantes sí lo son, y son las únicas que una propuesta
   puede defender hoy.

## 🔴 Pase 49: las 7 cifras «vencidas» del `--crossref` eran falsas, y la causa era la VENTANA

**El pase 48 cerró en «15 concuerdan / 0 vencidas». El pase 49 corrió el mismo comando y obtuvo
7 VENCIDAS.** Ninguna era real, y el motivo tardó dos lecturas en aparecer — por eso hay un
`test_crossref.py` con **21/21** controles:

1. **Primera lectura:** la prosa *«ya dice el número correcto y cita el viejo como historia»*.
   Es cierto de **una** línea (`repos/foundations.md:30`: *«11/11 checks» (hoy 37/37), «23
   aserciones» (hoy 46)*), y produjo una regla de corrección.
2. 🔴 **Después se corrió el control, y la regla resultaba satisfecha por COINCIDENCIA:** la ventana
   que el instrumento le pasaba medía **5.635 caracteres** en `repos/foundations.md` y **9.914** en
   `verticals/solutions.md`.

**La causa, medida:** la regla del pase 48 era *«fila de tabla ⇒ la fila; prosa ⇒ el párrafo»*, y el
código hacía crecer la ventana mientras las líneas no fueran blancas ni filas de tabla.
🔴 **Los ocho archivos de esta base abren con un `>` *blockquote* largo y sin una sola línea en
blanco**, así que «el párrafo» se tragaba el encabezado entero del archivo — y **una suite nombrada
4.000 caracteres más lejos se leía como la dueña de la cifra**.

🔵 **La medición que lo prueba, y que es contraintuitiva:** acotar la ventana subió
`unattributed` de **31 a 36**. **Cinco atribuciones las fabricaba el tamaño de la ventana.** Un
instrumento de citas que atribuye de más no es optimista: es falso, y en la dirección peligrosa,
porque **un pase siguiente habría «corregido» prosa que estaba bien**.

| Estado | Pase 48 | Pase 49, ventana sin acotar | Pase 49, ventana acotada |
|---|---|---|---|
| concuerdan | 15 | 17 | **12** |
| 🔴 **VENCIDAS** | 0 | 🔴 **7** | 🟢 **0** |
| sin condición | 0 | 0 | **0** |
| citadas **como ya corregidas** (historia) | — | 7 | **3** |
| 🆕 **AMBIGUAS** (no coinciden con ninguna de varias suites nombradas) | — | 0 | **1** |
| sin atribuir (**no se adivinan**) | 29 | 31 | ⚠️ **36** |

**La ventana correcta es la que el propio comentario del código describía:** la prosa va cortada a
~100 caracteres, así que una condición puede vivir **una línea más abajo**. **Una línea más abajo es
la ventana** — acotada, no un corrido. `figure_window()` queda como función pura y con controles.

### 🔴 Y dos defectos más de atribución, que inflaban la cuenta

1. **Una cifra que no coincide con NINGUNA de varias suites nombradas se cargaba a TODAS.**
   El comentario lo decía explícito (*«si no coincide con ninguna, se reporta contra todas»*), y eso
   convierte **una** cifra en **N** hallazgos: las 7 vencidas eran **3 cifras**. Ahora es
   **`AMBIG`: se reporta una vez y no se le asigna dueño**, que es la regla que esta carpeta ya tenía
   escrita para los *slugs* y no estaba aplicada acá.
2. **`named = owners` se hacía DENTRO del bucle por cifra**, así que la primera cifra de una línea
   **angostaba permanentemente** la lista de suites para todas las siguientes de la misma línea.
   La resolución es por cifra ahora, y hay un control de no-mutación.

### Las cifras de código verificadas a mano en este pase

**El denominador declarado primero**, porque es la mitad del resultado: de las **1.672** mediciones
de `intel/market.md` (**912**) e `intel/trends.md` (**760**), sólo **195 (11,7 %)** son de las
unidades reproducibles acá (`lines`, `assertions`, `routes`, `methods`, `files`, `rows`, `classes`,
`modules`, `tables`, `fields`). ⚠️ **Las 1.477 restantes NO se tocaron y se declara por qué:**
**916** `percent` (derivadas: hay que nombrar numerador y denominador, no el porcentaje), **389**
`★`, **83** `commits`, **83** `tools`, **10** `downloads`. 🟢 **Y de esas clases, `tools` y las
licencias dejaron de estar cerradas en este pase** — ver `../npm-surface-probe/`.

| Cifra publicada | Instrumento | Hoy | Veredicto |
|---|---|---|---|
| «**66 filas**, **61** *slugs* distintos, **0** duplicados» (el control de cada pase) | tabla principal de `agents/top.md`, líneas 398–465 | **68** líneas de pipe = 1 encabezado + 1 separador + **66 filas**; **61** *slugs* distintos; **0** duplicados | 🟢 **reproduce exacto** |
| «**233** crudas / **196** no-blancas / **184** no-blancas-no-comentario» (`mcp-allowlist-gateway`) | `wc -l` + `grep -cvE` sobre `gateway.py` + `policy.py` | **128+105 = 233** / **113+83 = 196** / **108+76 = 184** | 🟢 **reproduce exacto** |
| «**162** y **146** no-blancas; **145/145** no-blancas-no-comentario» (las dos puertas) | ídem sobre los dos `gate.py` | seb **189/162/145**, UniTime **171/146/145** | 🟢 **reproduce exacto** — la corrección del pase 48 se sostiene |
| «**186** crudas / **152** no-blancas» (`extract_surface.py`, en este README) | ídem | **186** crudas, **157** no-blancas, **152** no-blancas-no-comentario | 🔴 **el valor es correcto y la MÉTRICA está mal etiquetada**: 152 es no-blancas-**no-comentario**; no-blancas son **157** |
| las **5** filas que parecen encabezado en `agents/top.md` (L398, 605, 746, 794, 851) | ¿tienen un `\|---\|` debajo? | **las cinco lo tienen** | 🟢 **son encabezados legítimos, no datos filtrados** |

🔵 **La cuarta fila es el gap 101 en su forma más barata y más terca:** la encontró el propio
archivo que existe para evitarla, **tres pases después de escribir la regla**. La regla —*«decir
crudas o no-blancas-no-comentario»*— **no alcanza cuando hay TRES métricas y no dos.**

## 🟢 `--crossref`: el defecto NO era que una cifra se venza

**El pase 47 corrigió «11/11 checks» en `compose/patterns.md`. La misma cifra siguió viva en otros archivos.**
**Una corrección no se propaga**, porque una sola medición se cita hasta en diez lugares de ocho archivos. Por eso el
instrumento ahora **vuelve a correr las ocho suites** y atribuye cada cita de un conteo de *checks*.

| Suite | Hoy | Condición |
|---|---|---|
| `unitime-mcp-gate` | **46** | — |
| `sebserver-mcp-gate` | **37** | — |
| `mcp-allowlist-gateway` | **34** | nueva en el pase 48 |
| `openedx-course-generator` | **33** | — |
| `aiact-50-2-pack` | **27** | **37** con los dos directorios de esquemas |
| `aiact-50-2-marking` | **23** | **24** con `--with-xmllint` + `SCORM_SCHEMAS` |
| `seb-proctoring-validator` | **21** | — |
| `proctoring-reach-audit` | **19** | **20** con la ruta a un checkout de seb-server |

**Estado al cierre del pase 48: 15 citas concuerdan, 0 vencidas, 0 sin condición.** Se corrigieron **1 cifra vencida
real** (`verticals/solutions.md:1690`, «11/11» → **37/37**, en una fila de catálogo que se lee como estado actual) y
**2 condiciones sin escribir** (`repos/foundations.md`, `intel/trends.md`).

### 🔴 Y tres reglas de instrumento, cada una encontrada porque el instrumento falló primero

1. **La ventana de lectura sigue la ESTRUCTURA del documento.** Por **línea** se perdía la condición que vivía una
   línea más abajo (la prosa va cortada a ~100 caracteres) → **1 falso positivo**. Por **párrafo** se comía las filas
   vecinas de una tabla markdown, que no llevan línea en blanco entre sí → **3 hallazgos se volvieron 9, y 6 los
   fabricó la ventana**. **Regla: fila de tabla ⇒ la ventana es la fila; prosa ⇒ el párrafo.**
2. **Una cifra que coincide con una de varias suites nombradas en la ventana pertenece a ÉSA.** Cargársela a todas
   fabrica hallazgos.
3. **Condicional ≠ vencida.** `STALE` se corrige; `COND` se completa. Son acciones distintas.

⚠️ **Límite declarado: 29 citas quedan `unattributed`** —no nombran su suite en la ventana— **y no se adivinan**,
porque adivinar es lo que produjo las cifras vencidas. ⚠️ **Y una cifra CONTADA no es una cifra VERIFICADA:** el
inventario localiza, la verificación es por cifra y sólo las que apuntan a código de esta base son reproducibles acá.

## 🔴 Lo primero que encontró el barrido fue un error del barrido

La primera versión reportó **205 mediciones** sobre el archivo tal como estaba al empezar el pase. La real era
**368**. Faltaban **163 — el 44 %**.
**Motivo:** el patrón cerraba con `\b`, y `\b` después de un carácter que no es de palabra
**nunca dispara**, así que **todas** las cifras cuyo unidad era `%` (82) o `★` (81) se caían en
silencio. Se detectó cruzando el total contra un `grep` más flojo.

🔵 **Y conviene decirlo así y no disculparse:** la acción 2 existe porque una cifra sin
instrumento no se puede auditar. **El primer instrumento que esta base escribió para auditar sus
cifras tenía exactamente ese defecto, y se vio porque había dos mediciones del mismo objeto.**
Es el argumento de la acción, demostrado sobre sí misma.

## El inventario: 383 mediciones, 165 reproducibles acá

⚠️ **Dos cifras y las dos son correctas, que es justo el punto de este archivo: 368** sobre
`compose/patterns.md` **tal como estaba al empezar el pase 47**, y **383** al cerrarlo, porque el
mismo pase le agregó **P106**, **P107** y **P108**. 🔵 **Quince cifras de deriva en un pase, sobre el
archivo que esta carpeta audita, es la demostración más corta de por qué una cifra necesita decir
CUÁNDO se midió además de CON QUÉ.** El inventario de abajo es el del cierre.

| Unidad | Cifras | ¿Reproducible en este entorno? | Instrumento |
|---|---|---|---|
| `tools` | **78** | 🔴 **No** | `tools/list` por stdio contra el servidor — exige el paquete instalado |
| `★` | **81 → 90** | 🔴 **No** | `github.com` responde **403** a `curl` acá y `api.github.com` responde 200 con un cuerpo que niega acceso (pase 37) |
| `%` | **82 → 85** | 🟡 **Derivada** | **nombrar numerador y denominador**, no el porcentaje |
| `commits` | **46** | 🔴 **No** | `git rev-list --count HEAD` sobre un clon completo; los clones de esta base son `--depth 1` |
| `métodos` | 18 | 🟢 Sí | `grep -cE` de la firma, o contar `@abstractmethod` en la interfaz |
| `rutas`/`endpoints` | 15 | 🟢 Sí | `grep -oE '@(Get\|Post\|…)Mapping\|@Service("/'`, o el `<url-pattern>` del servlet |
| `líneas` | 13 | 🟢 Sí | 🔴 **`wc -l` y «no-blanca-no-comentario» NO coinciden: hay que decir cuál** |
| `filas` | 9 | 🟢 Sí | `grep -vc '^#'` sobre el TSV medido |
| `aserciones`/`checks` | 9 | 🟢 Sí | correr la suite y leer el `N/N checks passed` del final |
| `archivos`, `módulos`, `clases`, `tablas`, `campos` | 16 | 🟢 Sí | `git ls-tree`, `ls`, `grep -cE '^class '`, la migración, el serializador |
| `descargas` | 4 | 🔴 No | la API del registro (`pypi.org` / `npmjs`), caso por caso |

🔵 **El reparto es el dato de encuadre:** **218 de 383 cifras (57 %) no se pueden reproducir en
este entorno**, y **casi todas son de la misma clase**: popularidad (`★`, `commits`, descargas) y
superficie MCP (`tools`). **No es que estén mal: es que su canal está cerrado acá.** Las cifras
de **código** —métodos, rutas, líneas, clases, tablas— **sí** se reproducen, y son las que
sostienen una cotización.

## Las once cifras verificadas a mano, y las cuatro que no cierran

| Dónde | Cifra publicada | Instrumento | Hoy | Veredicto |
|---|---|---|---|---|
| L23, L203 | «33 aserciones» | `python3 code/openedx-course-generator/test_plan.py` | **33** | 🟢 reproduce |
| L450 | «21/21 checks, JDK puro» | `sh code/seb-proctoring-validator/run_test.sh` | **21/21** | 🟢 reproduce |
| L5681 | «9 checks de `scorm_validate`» | `grep -oE 'push\("[a-z0-9-]+"' src/validate.ts \| sort -u \| wc -l` | **9** ids distintos (**15** sitios de llamada) | 🟢 reproduce — **y el instrumento importa: el id distinto es la cifra correcta** |
| L445 | «481–912 líneas» | `grep -cvE '^[[:space:]]*(#.*)?$'` | **481 / 912**; `wc -l` da **583 / 1.116** | 🟢 correcta, **métrica ahora escrita** |
| L5584 | «20/20, exige regeneración byte a byte» | `python3 test_reach.py /ruta/a/seb-server` | **20/20** | 🟢 reproduce — **esta línea sí declara la condición** |
| L423 | «(20/20)» | ídem | **20/20 con la ruta, 19/19 sin ella** | ⚠️ **correcta y condicional**: esta línea **no** declara la condición |
| — (README y `trends`) | «24/24» del componente de marcado | `SCORM_SCHEMAS=<dir> python3 test_marking.py --with-xmllint` | **24/24**; a secas da **23/23** | ⚠️ **correcta y condicional**, citada sin la condición |
| **L608** | «23 aserciones, 23 en verde» (UniTime) | `python3 code/unitime-mcp-gate/test_gate.py` | 🔴 **46** | 🔴 **VENCIDA**: el pase 45 la subió a 46 y `patterns.md` no se actualizó |
| **L345** | «11/11 checks» (SEB Server) | `python3 code/sebserver-mcp-gate/test_gate.py` | 🔴 **37/37** | 🔴 **VENCIDA**: el pase 44 la subió |
| **L616** | «~115 líneas de stdlib» | `wc -l code/unitime-mcp-gate/extract_surface.py` | 🔴 **186** crudas / **152** no-blancas | 🔴 **no coincide con ninguna de las dos** |
| **L521, L615, L5174** | «**175 líneas** de stdlib» (**P85**) | — | 🔴 **ningún archivo de este repositorio la implementa** | 🔴 **NO REPRODUCIBLE: el artefacto no está** |

## 🔴 El hallazgo que vale el pase: P85 se cita como entregable y su código no está acá

**P85** se titula *«El *gateway* de allowlist de tools, **escrito y probado***» y su propio texto
dice **«la diferencia entre un patrón y un entregable»**. Pero:

- `MCP_ALLOWLIST` —la variable que P85 documenta, con su matriz de casos— **aparece únicamente en
  `compose/patterns.md`**. `grep -rl MCP_ALLOWLIST compose/code/` no devuelve nada.
- Las dos puertas que **sí** están versionadas usan **`SEB_ALLOW`** y **`UNITIME_ALLOW`**, y
  miden **189** y **171** líneas crudas (**145** y **145** no-blancas-no-comentario). **Ninguna
  da 175 por ninguno de los dos instrumentos.**
- La sección de P85 es la única de las que citan código que **no enlaza a `compose/code/`**.

⚠️ **Por qué esto importa más que un número flojo:** **P85 se cita como dependencia ya resuelta
en dos tablas de solución** —L521 (*«ya probado»*) y L615 (*«ya probadas»*)— **y P60, P92 y P93 se
apoyan en él.** Esas dos filas le prometen a un cliente una pieza que este repositorio no puede
entregar. **La corrección no es borrar la cifra: es decir dónde está el código, o escribirlo.**
🔵 **Y el mitigante honesto:** las dos puertas que sí existen **hacen** lo que P85 describe
(allowlist, `-32601`, `tools/list` recortado) y están probadas —**37/37** y **46**—, así que el
patrón es real; lo que falta es **la pieza genérica que P85 dice tener escrita**.

## La regla que queda escrita

🔵 **Toda cifra nueva en `patterns.md` nombra su instrumento en la misma línea o en la tabla que
la contiene.** Dos casos lo exigen explícitamente:

1. **Líneas**: decir *«crudas»* o *«no-blancas-no-comentario»*. Para la clase de SEB la
   diferencia es **481 vs 583** y **912 vs 1.116** — entre 17 % y 22 % del presupuesto.
2. **Aserciones**: decir **qué invocación** las produce. Dos suites de esta base dan un número
   distinto según el argumento o la variable de entorno (**19/19 vs 20/20**, **23/23 vs 24/24**),
   y las dos se citan en algún lado sin la condición.

Y un tercero, que no es de instrumento sino de ciclo: **una cifra de una suite propia se vence
cuando la suite crece.** Dos de las cuatro que no cierran son eso. `--check` las vuelve a medir
en un comando, así que el próximo pase no tiene excusa.
