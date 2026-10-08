---
industry: education
region: Global
updated: 2026-10-08
---

# `p571-cession-family-delegation/` — la compuerta de cesión dejó de clasificar familias

**Pase 47 del 2026-10-08.** Cierra un pendiente que el pase 46 declaró abierto con estas
palabras: *«`p411-cession-identity-gate` todavía inlinea un clasificador de licencias y todavía
carga `P561`»*.

## Qué se midió

La escalera inlineada de `p411/gate_cesion.py` contra `lib/license_family.sh::family_of`, sobre
los **29 payloads de cesión reales** del árbol. No fixtures: los `LICENSE` y `COPYING` que esta
base ya tenía guardados.

**Divergían 18 de 29.** Reproducible: `python3 medir.py --check` reconstruye la compuerta
anterior y falla si el antes deja de dar 18.

| Código | Payload real | La escalera decía | Es |
|---|---|---|---|
| 🔴 `P571` | `COPYING` de **Moodle**, y `gpl-3.0-lmscloud` | `AGPL-3.0` | `GPL-3.0` |
| 🔴 `P572` | `OpenEMIS/core` | `LGPL` | `GPL-2.0` |
| 🔴 `P573` | `mozilla/rhino` | `AGPL-3.0` | `MPL-2.0` |
| 🔴 `P574` | `hcengineering/platform` (Huly), `eclipse-ee4j/jersey` | `GPL` | `EPL-2.0` |
| 🔴 `P575` | texto canónico **MPL-1.1** de SPDX | `MPL-2.0` | `MPL-1.1` |
| 🔴 `P578` | `h2database` (dual MPL-2.0 **o** EPL-1.0) | `AGPL-3.0` | `MPL-2.0` (`Gap 249`) |
| 🔴 `P576` | **Sakai** (Educational Community License) | `NO-OSI` | `ECL-2.0`, **usable** |
| 🔴 `P577` | `YuanGongND/gopt` | `NO-OSI` | `BSD`, **usable** |
| 🔴 `P579` | `FWU-DE/mem-mcp` (**Unlicense**) | `usable=NO` | **usable** |

### Las tres causas, que no son la misma

1. **El cuerpo de una licencia nombra otras licencias.** La sección 13 de GPL-3.0 se titula *«Use
   with the GNU Affero General Public License»*; el párrafo de cierre de GPL-2.0 recomienda *«use
   the GNU Lesser General Public License instead»*; la sección 1.12 de MPL-2.0 y la cláusula
   *Secondary Licenses* de EPL-2.0 **definen** su compatibilidad nombrando GPL. Una sonda sobre el
   **cuerpo** lee el nombre citado, no el otorgado. Es `P171` y `P454`, ya pagados en `lib/`,
   re-importados por un instrumento que escribió su propia escalera (`P571`–`P575`, `P578`).
2. **Un disparador NO-OSI que aparece como subcadena de un nombre OSI.** `'community license'`
   existe por `PageLM`, pero la **Educational** Community License lo contiene; `'all rights
   reserved'` es, en BSD y MIT, parte del encabezado de copyright **convencional** (`P576`, `P577`).
3. **Una limitación que aparece para CONCEDERSE.** El Unlicense dice *«for any purpose, commercial
   or non-commercial»*: la subcadena `'non-commercial'` no distingue la concesión de la prohibición
   (`P579`).

🔴 **Las tres últimas son FALSOS RECHAZOS: la compuerta descartaba software que esta base existe
para habilitar.** `P576` rechazaba Sakai —un LMS del canal vertical— por el nombre de su licencia,
y `P579` rechazaba la licencia más permisiva que existe.

## Por qué sobrevivió un pase entero debajo de un verde

🔵 **El corpus de `p411/test_gate.py` no tenía ni un payload copyleft, ni uno OSI que no fuera
MIT.** Siete casos, todos sintéticos, todos verdes. **Una suite verde porque nunca preguntó.** Por
eso el arreglo durable no fue un assert más: fue agregarle corpus real a esa suite (7 → **11
casos**), además de este instrumento.

## La arquitectura: composición, no reemplazo

`family_of` contesta **qué texto de concesión es éste**. La compuerta contesta **si el documento
cede de verdad esos derechos**. Son dos preguntas con contratos opuestos, como las dos de región
en `P265`.

🟢 **La prueba de que no se puede delegar ciego: el clasificador compartido lee `PageLM` como
`MIT`** — exactamente el payload que `P411` existe para atrapar. Así que la familia se delega y la
compuerta de título se conserva, **estrechada**: un disparador NO-OSI ya no invalida un texto que
el clasificador endurecido reconoce, salvo que el documento traiga limitaciones fatales. `PageLM`
sigue siendo `NO-OSI` por esa segunda condición, y Sakai ya no.

Y si el clasificador compartido no está, `familia_compartida()` **levanta `SinClasificador`**. No
degrada a una escalera inlineada: eso es `P197`, y es el defecto que este pase acaba de pagar.

## Qué corre

| Archivo | Qué hace |
|---|---|
| `test_delegacion.py` | **33/33**. 13 payloads reales + 6 controles negativos de escalera + 3 de disparador + **6 mutantes** + `P197` + `P542` + vocabulario |
| `medir.py` | el barrido antes/después. `--check` exige que el antes reproduzca **18** y el después no pase de **4** |
| `result-before.2026-10-08.tsv` / `result-after.2026-10-08.tsv` | las 29 filas, antes y después |

**Los 6 mutantes** rompen el arreglo a propósito y la suite debe verlos: 3 quitan la delegación
(Moodle vuelve a `AGPL-3.0`, rhino a `AGPL-3.0`, Huly a `GPL`), uno quita la exención de `P576`
(Sakai vuelve a `NO-OSI`), uno la guarda de `P577` (BSD vuelve a `NO-OSI`) y uno el descuento de
`P579` (el Unlicense vuelve a `FATAL`).

🔵 **Las 4 filas que todavía divergen no son defecto: son el juicio de la compuerta.** Son los
cuatro payloads **Creative Commons** del árbol, que `family_of` nombra (`CC-BY-SA-4.0`,
`CC-BY-NC-4.0`, …) y la compuerta además califica `NO-OSI` — porque ninguna licencia CC es una
licencia de software aprobada por la OSI. Las dos respuestas son correctas; contestan preguntas
distintas.

## Lo que queda abierto

- 🟡 **`Gap 249`** — una licencia **dual** se reporta por un solo brazo. `h2database` ofrece
  MPL-2.0 **o** EPL-1.0 y la respuesta es `MPL-2.0`: el brazo EPL-1.0 se pierde. Declarado por el
  pase 46, sigue abierto, y ahora con un payload real en el corpus de dos suites.
- 🟡 **`p419-copyleft-identity` inlinea un TERCER clasificador**, por encabezado. Clasificar por
  encabezado es el método correcto (`P171`), así que no carga los defectos de `P571`–`P575`, pero
  tampoco hereda nada de `lib/`. Medido, no arreglado: no se toca un instrumento cuyo contrato no
  se midió primero (`P562`).
