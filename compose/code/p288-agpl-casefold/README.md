---
industry: education
region: Global
updated: 2026-10-04
---

# `p288-agpl-casefold` — el control COMPARTIDO tenía un hueco de CAJA, sobre el par exacto que existe para proteger

> Nuevo en el **pase 96 del 2026-10-04**. `lib/license_family.sh` es el control compartido que
> **P237** creó para que la corrección GPL-3.0/AGPL-3.0 de **P171** no tuviera que recordarse.
> Este pase encontró un payload real donde ese control devuelve **`GPL-3.0` para una AGPL-3.0**.

| Qué prueba | Invocación | Hoy |
|---|---|---|
| el caso que las 41 aserciones no ejercitaban, + el negativo de `P171` | `sh test_casefold.sh` | 🟢 **9/9** |
| que la suite vieja no se rompe con el arreglo | `sh ../lib/test_license_family.sh` | 🟢 **41/41** *(medido en el pase 96; hoy **50/50** tras `P299`)* |

## 🔬 El canal, declarado antes de cualquier veredicto (`P247`)

Medido hoy: `github.com/<org>/<repo>` → 🔴 **`403` en 3/3** (reproduce el pase 81, 81/81) ·
`github.com/` y `api.github.com/` → 🔴 **`400`** · `raw.githubusercontent.com` → 🟢 **`200` con
payload**. La licencia se **LEE**; el `curl -sI` que el encargo ordena sigue muerto acá.

## 🔴 El defecto, y su mecanismo exacto

El payload es `kuali/kfs` → `HEAD/LICENSE`, **33.755 B**: el Kuali Financial System, el ERP
financiero de dos docenas de universidades. Es una **AGPL-3.0** y el control decía `GPL-3.0`.

| Paso | Qué pasa |
|---|---|
| la rama AGPL es un glob de `case`: `*"GNU AFFERO GENERAL PUBLIC LICENSE"*` | 🔴 **SENSIBLE A LA CAJA** |
| ¿trae el payload esa línea de título en mayúsculas, en sus 40 primeras líneas? | 🔴 **0 veces** — es un AGPL **reflowed** |
| ¿nombra la AGPL en caja mixta? | 🟢 **3 veces** |
| entonces cae a la rama GPL, que usa `grep -qi` — **insensible** | ⚠️ y matchea… |
| …el **PREÁMBULO DE LA PROPIA AGPL**: *«The GNU General Public License permits making a modified version and letting the public access it on a server without ever releasing its source code to the public.»* | 🔴 veredicto **`GPL-3.0`** |

🔵 **Es `P171` reabierto por un eje nuevo.** P171 dice *clasificá por bloque de título, no por el
cuerpo* — y la regla se cumplió. Lo que P171 no previó es que **el bloque de título de la AGPL
nombra la GPL**, porque su preámbulo explica *en qué se diferencia de la GPL*. La asimetría de caja
entre las dos ramas es lo que deja pasar el error.

## 🔴 Y es `P126` punto 2, otra vez, al pie de la letra

Las **41** aserciones de `lib/test_license_family.sh` pasaban — y **ninguna ejercitaba este caso**:
*todas* sus fixtures AGPL (`AGPL3=`, `AGPL_S6=`) empiezan con el título canónico **en mayúsculas**.

> **Un control positivo que pasa no habilita un instrumento si no ejercita el caso donde ese
> instrumento puede fallar.**

Esa regla está escrita en el `README.md` de esta KB desde el pase 56. **El control compartido que
P237 creó para que una corrección no tuviera que recordarse nació sin el caso que lo rompe.**

## 🟢 El arreglo, y por qué es angosto

El ancla es la **definición de la sección 0**, que es mutuamente excluyente entre las dos licencias:

| Licencia | Su sección 0 dice |
|---|---|
| AGPL-3.0 | `"This License"` **refers to** `version 3 of the GNU` **Affero** `General Public License` |
| GPL-3.0 | `"This License"` **refers to** `version 3 of the GNU General Public License` |

🔵 **Y la sección 13 de la GPL-3.0 —la trampa de `P171`— NO es un ancla**, porque dice *«licensed
**UNDER** version 3 of the GNU Affero…»*, no *«refers to»*. Por eso el ancla **lleva `refers to`**:
sin esas dos palabras, el arreglo reabre P171. **El control negativo que lo afirma está en la suite**
(aserciones 5 y 6), medido sobre la fixture GPL-3.0 con su sección 13 incluida.

⚠️ **Lo que NO se hizo, y es deliberado:** no se volvió la rama de título insensible a la caja. Eso
habría hecho que la fixture GPL-3.0 de la suite vieja —cuyo encabezado **incluye** la sección 13—
clasificara como AGPL-3.0. Es exactamente el defecto que P171 registró. **El arreglo correcto era
más angosto que el obvio.**

## 🔴 La consecuente de negocio, que es la que paga el pase

`kuali/kfs` es **AGPL-3.0**, no `GPL-3.0` y no `ECL-2.0`:

| Fuente | Qué dice de Kuali |
|---|---|
| Wikipedia (*Educational Community License*), ayuda de KFS en MSU/WVU/IU, linux.com | «Kuali is licensed pursuant to the **Educational Community License (ECL), Version 2.0**» |
| `kuali/rice` → `HEAD/LICENSE.txt`, payload leído | 🟢 **`ECL-2.0`** — la secundaria acierta **acá** |
| `kuali/kfs` → `HEAD/LICENSE`, payload leído | 🔴 **`AGPL-3.0`** — la secundaria **falla acá** |
| `kuali/kc` → `pom.xml`, declaración leída | 🔴 **`AGPL-3.0`** (ver `p289-maven-manifest/`) |

🔵 **La licencia de Kuali es por REPO, no por organización**, y la diferencia decide una entrega:
**ECL-2.0** es de familia Apache y no pide nada; **AGPL-3.0 §13** obliga a publicar el fuente a los
usuarios de un servidor. Para un ERP universitario entregado como SaaS —que es cómo se entrega—
es la diferencia entre *construir encima* y *publicar el derivado*. 🔴 **Y el `README` de `kuali/kfs`
no declara licencia alguna**, así que la única fuente es el payload.

## 🔴 Alcance del defecto, declarado y NO extrapolado (`P286`)

Lo que se puede decir sin barrer: **141** veredictos `GPL-3.0` viven en **21** archivos de resultado
versionados de esta base, y **94** veredictos ya dicen `AGPL-3.0`.

⚠️ **Y acá se aplica `P286`, que es la lección del pase 95: extrapolar un reparto poblacional desde
UN control positivo no es una estimación, es una corazonada con tabla.** Así que **este README no
predice cuántas de las 141 están mal.** El defecto requiere **dos** condiciones simultáneas —payload
AGPL **y** sin título en mayúsculas— y sólo un barrido lo mide.

🟢 **Lo que sí es falsable sin número, y es la predicción pre-registrada:** el arreglo sólo puede
mover veredictos en **una dirección**, `GPL-3.0` → `AGPL-3.0`. **Si un re-barrido mueve una fila en
el sentido contrario, el arreglo es inseguro y hay que revertirlo.**

## 🔴 Acción pre-registrada para el pase 97

Re-correr `osi_family_of` sobre los payloads de los **141** veredictos `GPL-3.0` y los **94**
`AGPL-3.0` ya publicados, y reportar el reparto **enumerado** (`P293`). La predicción es la de
arriba: **movimiento en un solo sentido, o el arreglo está mal.**
