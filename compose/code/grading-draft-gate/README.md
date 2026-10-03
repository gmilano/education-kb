---
industry: education
region: Global
updated: 2026-10-03
---

# `grading-draft-gate/` — el único patrón conforme de esta base, vuelto suite

**Hoy: 37/37**, OFFLINE, sólo biblioteca estándar, sin red.

```sh
python3 test_gate.py        # 37/37
```

**Qué prueba:** las **tres** propiedades del patrón de
[`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp) **por separado**,
contra un stub que reproduce el contrato REAL de `mod_assign_save_grade`, **más los controles
negativos** que el pase 56 enseñó a exigir (**P126**, punto 2).

| # | Propiedad | Aserciones |
|---|---|---|
| **(i)** | la nota se escribe `workflowstate=readyforreview` y **nunca** se libera | 7 |
| **(ii)** | el pie de divulgación se **agrega si falta** y **no se duplica** si está | 5 |
| **(iii)** | una escritura fuera de la *allowlist* de cursos se **rechaza** (y `MOODLE_ALLOW_WRITE` y *allowlist vacía* también) | 8 |
| **(iv)** | 🔴 **controles negativos** — las aserciones que fallan si la compuerta se desactiva | 12 |
| — | el stub castiga lo que castiga Moodle (no es un *yes-man*) | 5 |

## 🔴 Por qué la acción 2 encontró más de lo que buscaba

El pase 56 dejó escrito que había que volver entregable *«lo único conforme que esta base
encontró»*. Al escribir el stub contra el código de Moodle apareció que **la propiedad (i) no es una
propiedad del servidor**: es una propiedad de **una casilla de configuración por tarea** que el
servidor **no mira, no documenta y no posee**.

`moodle/moodle` @ `main`, `public/mod/assign/locallib.php:2991-3001`, comentario del propio Moodle y
su SQL:

> *«Submissions are included if all are true: … **If marking workflow is enabled, the workflow state
> is at 'released'.**»*

```sql
WHERE (a.markingworkflow = 0 OR (a.markingworkflow = 1 AND uf.workflowstate = :wfreleased)) AND
```

🔴 **Con `markingworkflow = 0`, Moodle le manda la nota al alumno sea cual sea el `workflowstate`.**
Y en `locallib.php:7960` el cambio de estado **no se registra siquiera**:

```php
$modified->workflowstatechanged = $this->get_instance()->markingworkflow && ...
```

**Consecuencia:** el README de `toshieji` dice *«Safety (enforced server-side)»* y *«No student
notification (draft state)»*. **Las dos afirmaciones son verdaderas sólo si la tarea de destino tiene
el *marking workflow* activado**, y el README **no lo menciona** (0 coincidencias de
`markingworkflow` en sus 8.326 bytes). Una institución que despliega la pieza sobre una tarea sin
*marking workflow* **publica la nota al alumno de inmediato, con el pie de divulgación puesto.**

🔵 **Por eso `gate.py` agrega una cuarta propiedad que el patrón publicado no tiene**
(`require_marking_workflow`, **encendida por defecto**): antes de escribir, consulta
`mod_assign_get_assignments` y **se niega** si la tarea tiene `markingworkflow=0`. Es una llamada de
lectura más por tarea, y es la diferencia entre un borrador y una nota publicada.

## Los controles negativos, que son el punto

| Control | Qué demuestra |
|---|---|
| **(iv-a)** | ensanchar la *allowlist* **sí** deja pasar el curso 6 → el rechazo de (iii) **es la compuerta**, no un accidente |
| 🔴 **(iv-b)** | con `require_marking_workflow=False` el servidor **hace todo bien** (manda `readyforreview`) **y Moodle notifica al alumno igual** |
| **(iv-c)** | con el chequeo encendido, **la misma escritura se rechaza** y el alumno nunca se enteró |
| **(iv-d)** | las dos tareas del stub difieren **sólo** en `markingworkflow` — el control aísla la variable |

## El stub es un contrato, no un *yes-man*

Todo lo que castiga está leído de `moodle/moodle` @ `main` y citado por archivo y línea:

- `public/mod/assign/externallib.php:1987` — `workflowstate` es **`PARAM_ALPHA`**
  (`public/lib/moodlelib.php:86-89`: sólo `[a-zA-Z]`), así que `ready_for_review` **lo rechaza Moodle**.
- `public/mod/assign/locallib.php:64-69` — los **seis** estados legales, verbatim.
- `public/mod/assign/locallib.php:3001` — la regla de liberación de arriba.
- `public/mod/assign/locallib.php:7960` — el estado no se registra sin *marking workflow*.
- una función fuera del token da **`accessexception`**, la clave de error real de Moodle.

## ⚠️ Nota de instrumento: `main` de Moodle mudó el árbol a `public/`

**Moodle 5 relocalizó todo el código bajo `public/`.** Medido este pase:

| Ruta | `main` | `MOODLE_405_STABLE` |
|---|---|---|
| `README.md` | **200** | 200 |
| `mod/assign/locallib.php` | 🔴 **404** | **200** |
| `public/mod/assign/locallib.php` | 🟢 **200** | — |

🔴 **Una sonda de rama contra `<rama>/README.md` da 200 y no prueba que el árbol del proyecto esté
ahí**: `main/README.md` y `main/config-dist.php` dan 200 mientras `main/version.php` da 404. **La
sonda tiene que ser el archivo que se va a leer**, no un hermano cualquiera.

## Mutación: la suite tiene dientes

Tres mutaciones corridas sobre `gate.py`, cada una atrapada por las aserciones que le tocan:

| Mutación | Resultado |
|---|---|
| `DRAFT_STATE = "released"` | **31/37** — caen las 5 de (i) y una de (iv-d) |
| pie agregado sin chequear si ya está | **36/37** — cae *«NOT duplicated when already present»* |
| *allowlist* vacía tratada como comodín | **35/37** — caen las 2 de *«empty allowlist is no write target»* |

## Cómo se cablea en una propuesta

`gate.py` no depende de `toshieji`: es el patrón, no el repo. Se monta sobre cualquiera de las cuatro
puertas MIT de Moodle de esta base reemplazando `MoodleStub` por el cliente real de Web Services. Lo
que **no** se puede tercerizar al ecosistema es el requisito: la tendencia **337** ya estableció que
*«borrador + liberación humana»* es **1 de 8** en la capa, así que el requisito lo escribe Globant —
y ahora llega a la reunión **como suite que corre**, no como prosa.
