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
