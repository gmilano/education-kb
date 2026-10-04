---
industry: education
region: Global
updated: 2026-10-04
---

# `p312-nc-gate-inversion/` — la compuerta se abría sobre las familias que existe para atrapar

**Qué prueba:** que un payload con restricción **NonCommercial** responda `PROHIBIDO` en el eje de
uso comercial y conserve el atributo `NC` en su familia, **y** que las familias que sí permiten uso
comercial sigan respondiendo `ALLOWED`.

**Invocación:** `sh test_nc_gate.sh` — **hoy 21/21**, corre OFFLINE.
La suite compartida pasó de **79/79** a **106/106** con los mismos controles.

## El especimen, que no es una fixture

`devissaputra/classroom_discourse_intelligence` (alta de este pase) es **MIT en el código** y
**CC BY-NC-SA 4.0 en los datos**. Su `data/README.md`, leído el 2026-10-04 por
`raw.githubusercontent.com`, dice:

> `CC BY-NC-SA 4.0.` **Non-commercial** `and ShareAlike restrictions apply. This repository does not`
> `redistribute the source corpus.`

Medir ese payload contra el control compartido es lo que destapó **dos** defectos.

## D1 — el orden de dos ramas decidía la respuesta entre atributos ORTOGONALES

La rama CC se escribió en el pase 82 como una cadena de `elif`, y `ShareAlike` iba **antes** de
`NonCommercial`. Las cláusulas de Creative Commons **se combinan** (BY, NC, SA, ND), así que la
primera que matcheaba retornaba y las demás no se leían:

| payload | antes | después |
|---|---|---|
| CC BY-NC-SA 4.0 | 🔴 `CC-BY-SA-4.0` — **el `NC` se perdía** | 🟢 `CC-BY-NC-SA-4.0` |
| CC BY-NC-ND 4.0 | 🔴 `CC-BY-NC-4.0` — el `ND` se perdía | 🟢 `CC-BY-NC-ND-4.0` |
| CC BY-SA 4.0 | 🟢 `CC-BY-SA-4.0` | 🟢 `CC-BY-SA-4.0` (positivo) |

🔵 **El arreglo no es reordenar dos líneas.** Una cadena de `elif` sobre atributos **combinables**
es el defecto, no el orden de sus ramas: la identidad ahora se **compone** (`CC-BY` + `-NC` + `-SA`
+ `-ND`). Reordenar habría arreglado el especimen y dejado `CC BY-NC-ND` roto.

## D2 — y éste es el grave: la compuerta de `P250` abría sobre `CC-BY-NC-4.0`

La premisa de la compuerta está escrita en la librería desde el pase 82 y **es correcta**: *«una
familia OSI identificada permite uso comercial POR DEFINICIÓN, y por eso nunca se le hace
token-match»*. El problema es que el **mismo pase** que la escribió puso **detrás** de ella cuatro
familias que **no son OSI**: la rama CC.

🔴 **Resultado medido:** `CC-BY-NC-4.0` —una familia cuyo **nombre dice NonCommercial**— volvía
**uso comercial PERMITIDO**, porque la compuerta cortocircuitaba el token-match antes de que
alguien leyera la palabra `NonCommercial` del payload.

| | `family_of` | `commercial_use_ok` antes | después |
|---|---|---|---|
| CC BY-NC-SA 4.0 | `CC-BY-NC-SA-4.0` | 🔴 **ALLOWED** | 🟢 PROHIBITED |
| CC BY-NC 4.0 | `CC-BY-NC-4.0` | 🔴 **ALLOWED** | 🟢 PROHIBITED |
| CC BY-NC-ND 4.0 | `CC-BY-NC-ND-4.0` | 🔴 **ALLOWED** | 🟢 PROHIBITED |
| CC BY-SA 4.0 | `CC-BY-SA-4.0` | 🟢 ALLOWED | 🟢 ALLOWED |
| MIT / Apache-2.0 / AGPL-3.0 | — | 🟢 ALLOWED | 🟢 ALLOWED |

⚠️ **La dirección del daño es la peor de las dos posibles, y conviene decirlo contra `P308`.** El
defecto del pase 100 **perdía** permiso sobre un texto permisivo: se sobre-restringe, y eso cuesta
una oportunidad. Éste **inventa** permiso sobre un texto que lo prohíbe **en su propio nombre**: se
sub-restringe, y eso cuesta el entregable. 🔵 **Es la inversión que `P250` existe para evitar,
cometida dentro del control que `P250` creó.**

El arreglo **nombra el conjunto** en vez de confiar en «identificada»: una familia no-OSI con
restricción no comercial responde `PROHIBIDO` sin consultar el payload, y toda otra familia no-OSI
(`CC-BY`, `CC-BY-SA`, `CC0`, `BUSL`, `Elastic`, `PolyForm`) **cae al token-match** en vez de pasar
por la compuerta — que es exactamente lo que la premisa permite.

## Y la sigla, que es por dónde el especimen real se escapaba

La puerta de entrada a la rama pedía el nombre `Creative Commons` o el dominio, y el `data/README.md`
del especimen **no trae ninguno de los dos**: trae la sigla. Caía a `UNCLASSIFIED`, y por ese camino
el token-match **sí** corre y acierta el permiso.

🔴 **O sea que el especimen real daba la respuesta correcta por la razón equivocada, mientras el
texto canónico de la misma licencia daba la incorrecta.** Un control que sólo hubiera medido el
especimen habría pasado. La sigla entra ahora como puerta, **después** de los anclas de
MIT/Apache/GPL, con dos controles negativos que lo acotan: un MIT y un Apache-2.0 que **mencionan**
`CC BY` en su texto siguen siendo MIT y Apache-2.0.

## Por qué la suite llegó a 79/79 con esto roto

La regla de **`P126` punto 2** de este repositorio, otra vez y sobre la librería compartida:
**ninguna de las 79 aserciones le pasaba un payload de Creative Commons.** El control estaba
completo en el eje que le importaba (GPL/AGPL, reflujo, familias OSI) y **vacío** en el eje donde
podía fallar. Un control positivo que pasa no habilita un instrumento si no ejercita el caso.

## `P313` — el rewiring que esto habilitó, y el control que rompió

`P237` quedaba **ABIERTO** para `p170`, `p206`, `p211` y `p230`: las cuatro llevaban **copia propia**
del clasificador. La razón declarada en el pase 100 para no rewirearlas era concreta y **correcta** —
*«el control compartido todavía no es un superconjunto de las copias»*: `BUSL`, `Elastic` y
`PolyForm` vivían **sólo** en `p170`, y adoptar la librería habría **perdido tres familias**.

Este pase hizo las dos cosas **en ese orden**: primero las tres familias entraron a la librería con
sus controles negativos, después se rewirearon las cuatro copias. **`P237` queda CERRADO.**

🟢 **El vocabulario publicado de cada instrumento se conserva a propósito** (`GPL` agrupado en
`p170` y `p230`, `CC-BY`, `UNKNOWN`, `OTRO`, `VACIO`), para que los TSV ya escritos sigan siendo
comparables. La traducción **agrupa y nunca inventa**, y la suite lo afirma con cuatro aserciones.

🔴 **Y `p230` arrastraba un defecto YA PAGADO por esta base.** Sus ramas eran globs de `case`, que
son **sensibles a la caja** — `P288`, el defecto que clasificaba una AGPL-3.0 *reflowed* como
GPL-3.0. Medido sobre la copia vieja antes de tocarla:

```
copia vieja de p230, "mit license" en minúsculas  ->  OTRO     🔴
copia vieja de p230, "MIT License" canónico       ->  MIT
copia rewireada, los dos casos                    ->  MIT      🟢
```

🔴 **El rewiring rompió el control que guardaba a `p206`, y el defecto no es del rewiring.**
`p206/test_family.py` extraía el cuerpo de `family_of` **del propio `sweep_erp.sh`** con
`sed -n "/^family_of() {/,/^}/p"`: estaba acoplado al **texto** del archivo y no a su
**comportamiento**. Al mudarse la función, el `sed` no encontró nada y las tres aserciones de `D2`
—**las que guardan `P171`, el par GPL/AGPL**— devolvieron cadena **vacía** y fallaron. 🔵 **Un
control escrito contra el layout de un archivo se rompe con la consolidación que `P237` pide, justo
cuando más falta hace que siga midiendo.** Ahora apunta a la librería: **5/5**, y las fixtures no se
tocaron.

## Control de comportamiento del rewiring, contra payloads reales

`p170` rewireada, corrida contra seis repos medidos este pase por un camino independiente
(`curl` directo): **6 de 6 coinciden**, incluido el par que decide el hallazgo de procedencia de
este pase.

```
THU-MAIC/OpenMAIC                        LICENSED  LICENSE   1066   MIT
wwyw4842-dot/OpenMAIC                    LICENSED  LICENSE  34524   AGPL-3.0
rosewang2008/edu-convokit                LICENSED  LICENSE   1069   MIT
EduNLP/EduCoder                          LICENSED  LICENSE   1068   MIT
joaopdmol/Automated_Classroom_Attendance LICENSED  LICENSE   1069   MIT
yptheangel/attention-monitor             LICENSED  LICENSE  11358   Apache-2.0
```

⚠️ **Y una cota de entorno que cambió respecto del pase 52, declarada en vez de heredada:** ese pase
registró que *«un script del repositorio que sale a la red → NEGADO (`[Code from External]`)»*. Este
pase **corrió `p170/sweep_headref.sh` con red y funcionó** — las seis filas de arriba son su salida.
La negativa del pase 52 **no se reproduce hoy**, y se re-mide en vez de citarse.
