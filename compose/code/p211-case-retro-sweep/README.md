# P211 — The retroactive case re-measure (pass 72 del 2026-10-03)

**Qué cierra.** El pase 71 descubrió que `raw.githubusercontent.com` es **case-sensitive**,
corrigió dos `NO-CESSION` falsos (`frappe/education`, `frappe/erpnext`) y escribió una
advertencia general: *«todo veredicto `NO-CESSION` / `UNLICENSED` que esta base publicó salió de
un sondeo en mayúsculas, así que cada uno queda CONDICIONADO POR LA CAJA»*.

Este instrumento cierra esa condición sobre la población más grande que existe: las **32 filas**
que **P170** devolvió como `UNLICENSED`.

**Hipótesis falsable, escrita antes de correr.** Si el defecto de caja es **general**, al menos
una de las 32 vuelve `LICENSED`. Si era **específico** del corte de ERP que midió el pase 71, las
32 se sostienen y la condición cierra en su rama **benigna** — que es, en sí mismo, el hallazgo.

**Resultado (2026-10-03, `result.2026-10-03.tsv`): 32 de 32 se sostienen. 0 flips.**

Y la medición corrige a quien la pidió: **la generalización del pase 71 era demasiado amplia.**
P170 sondeaba 14 nombres y **tres de ellos ya eran minúscula** (`license`, `license.md`,
`license.txt`), más `LICENCE`/`LICENCE.md`. Nunca fue un sondeo «en mayúsculas». El que lo era —y
por eso fabricó las dos lápidas— fue la **primera corrida de P206**, no P170.

**Control positivo** (`control-positive.2026-10-03.tsv`): los cuatro casos que debían resolver
resuelven, y los cuatro resuelven **con nombres que ya estaban en la lista de P170** — que es la
prueba de la corrección anterior:

| slug | archivo | bytes | familia |
|---|---|---|---|
| `frappe/education` | `license.txt` | **19** | `UNCLASSIFIED` (los 19 bytes son `License: GNU GPL V3` — **P168**) |
| `frappe/erpnext` | `license.txt` | 35.148 | GPL-3.0 |
| `moodle/moodle` | `COPYING.txt` | 35.146 | GPL-3.0 |
| `buriro-ezekia/mwalimulens-agent` | `LICENSE` | 11.356 | Apache-2.0 |

**Qué agrega igual la re-medición.** 28 nombres contra 14, y por primera vez las **tres cajas**
(UPPER / lower / Title) para cada raíz, más `copying`/`Copying` y `COPYRIGHT`. Los 32 veredictos
pasan de *condicionados* a **cerrados**.

**Correcciones que lleva adentro:** P170 (ref `HEAD`), P172 (canal de payload; `api.github.com` y
`github.com` dan 403 en este entorno), P171 (la familia se lee del **bloque de título**, no del
cuerpo: la sección 13 del GPL-3.0 se titula *«Use with the GNU Affero General Public License»*),
P198 (*reachable and silent* ≠ *unreachable*, con control positivo en el mismo árbol).

```
./sweep_retro.sh                 # las 32 filas de slugs.input.txt
./sweep_retro.sh org/repo        # una sola
```
