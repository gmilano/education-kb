# `p114-license-column` — la columna Licencia de `agents/top.md`, medida con P114

**Pase 51 del 2026-10-02.** Ejecuta la **acción 1** que el pase 50 dejó escrita: aplicar las cuatro
preguntas de **P114** a **todos** los `github.com/org/repo` que cita `agents/top.md` y publicar la
salida de **tres valores**.

## Qué corre

| Archivo | Qué hace |
|---|---|
| `repos.input.txt` | los **167** `org/repo` distintos extraídos de `agents/top.md` |
| `scan_license.sh` | P114 pasos 2 y 3: texto en `{main,master}/{LICENSE,LICENSE.md,LICENSE.txt,COPYING}` y, si no hay, **control de alcanzabilidad** |
| `scan_altnames.sh` | **el paso que este pase agrega**: 16 nombres alternos antes de confirmar una ausencia |
| `result.2026-10-02.tsv` | la salida consolidada, 167 filas |

```sh
cat repos.input.txt | xargs -P 8 -I{} ./scan_license.sh {}          # base
./scan_altnames.sh <org/repo>                                       # sobre cada 'sin-licencia'
```

## El denominador, declarado

`agents/top.md` tiene **485** líneas de pipe, de las cuales **60** son separadores `|---|`:
**425 filas de datos y encabezado**. De ellas **176 traen una URL de `github.com`** y dan **167
`org/repo` distintos**. ⚠️ **Las otras 249 filas no traen URL de GitHub y quedan FUERA del alcance
de este instrumento** —son paquetes de registro, especificaciones y plataformas— y **no deben
leerse como «sin medir licencia» sino como «medibles por otro canal»** (registro + tarball).

## El resultado

| Veredicto | Filas | Qué significa |
|---|---|---|
| **licenciado** | **139** | campo **y** texto, con el artefacto exacto anotado |
| **sin licencia** | **23** | ausencia **medida**: **20** nombres de archivo en `main` y `master`, con el repo respondiendo 200 |
| **no público por este canal** | **5** | el canal **está probado contra un hermano de la misma organización** (ver abajo) |

Mezcla de los 139: **MIT 79 · Apache 27 · GPL 9 · AGPL 7 · BSD 4 · CC 3 · LGPL 2** + **4 textos anómalos**.

## Las dos correcciones que este artefacto le hace a P114

**1. La lista de cuatro nombres del paso 2 era incompleta: produjo 4 falsos «sin licencia» de 27
(14,8 %).** Y los dos mecanismos son **convenciones de ECOSISTEMA**, no descuidos:

| Rescatado | Artefacto real | Convención |
|---|---|---|
| **`moodle/moodle`** | `main:COPYING.txt` → *GNU GENERAL PUBLIC LICENSE* | el mundo **GPL/Moodle** usa `COPYING.txt` |
| `jeanlucio/moodle-local_aihub` | `main:COPYING.txt` → ídem | ídem, **plugin de Moodle** |
| `contentauth/c2pa-rs` | `main:LICENSE-MIT` → *MIT License* | **doble licencia** (`LICENSE-MIT` + `LICENSE-APACHE`), mundo Rust |
| `contentauth/c2pa-python` | `main:LICENSE-MIT` → ídem | ídem |

🔴 **El falso más grave es `moodle/moodle`** —la pieza central de `verticals/solutions.md`— que un
probe de cuatro nombres declara sin licencia **siendo GPL**.

**2. «indeterminado» se parte en dos con un control nuevo: el HERMANO.** En vez de concluir «el
canal no llegó», se pregunta si el canal llega a **otro repo de la misma organización**:

| Indeterminado | Hermano probado | Lectura |
|---|---|---|
| `1EdTech/caliper-php`, `IMSGlobal/caliper-python` | **`1EdTech/caliper-spec` → `master:README.md` 200** | el canal llega a la organización: **el repo no es público** |
| `marcusgreen/moodle-tool_aiconnect` | **`marcusgreen/moodle-qtype_gapfill` → 200** | ídem |
| `YL1N/EduGuardBench`, `concentricsky/badgr-server` | — | sin hermano probado: **indeterminado de verdad** |

## Control positivo

Corrido **antes** de publicar, reproduce tres veredictos que esta base ya tenía medidos:
`learningequality/kolibri` → **MIT**, `public-ui/kolibri` → **EUPL-1.2**,
`pie-framework/pie-elements-ng` → **ausencia medida**. Y de forma independiente confirma la
corrección del pase propio sobre `Open-TutorAi/open-tutor-ai-CE`: **BSD-3-Clause** (3 cláusulas
numeradas + *«Neither the name… endorse or promote»*), **no** el Apache-2.0 que un ciclo viejo
había reportado.

## Límite declarado

Mide **texto de licencia**, no **compatibilidad**. Un `LICENSE` que responde 200 con texto real
puede **no ser open source**: ver `dssg/student-early-warning` en el TSV, cuyo texto es una licencia
**académica no comercial** de la Universidad de Chicago que excluye explícitamente *«any service or
part of selling a service»*. **El veredicto `licenciado` significa «hay permiso escrito», nunca
«se puede usar en una entrega».**
