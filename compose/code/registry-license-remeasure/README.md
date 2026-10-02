---
industry: education
region: Global
updated: 2026-10-02
---

# `registry-license-remeasure` — la acción 1 del pase 51, ejecutada, y el ancla del tarball corregida

**Pase 52 del 2026-10-02.** El pase 51 dejó escrito: *re-medir con los 20 nombres de archivo los 30
paquetes de registro del pase 50, porque su veredicto salió con la lista de 4 que este pase probó
incompleta*, con una hipótesis **falsable**: si la causa de los falsos es la misma convención de
ecosistema, **al menos uno de los 9 cambia de veredicto**; si ninguno cambia, el defecto era
específico de la capa de GitHub.

🟢 **Resultado: la hipótesis se confirma, y por un mecanismo que NO era el previsto.** Cambian
**tres** veredictos, y los tres los resuelve el **tarball**, no los 20 nombres sobre el repositorio.

## Qué corre

| Archivo | Qué hace | Red |
|---|---|---|
| `targets.txt` | los **11** objetivos: los 4 «sin campo» y los 5 «indeterminados» del pase 50, más `@moinsen-dev/tool-teacher` y `@timeback/oneroster` | — |
| `remeasure.sh` | los tres instrumentos por objetivo: (a) 20 nombres × `{main,master}`, (b) alcanzabilidad, (c) tarball anclado | sí |
| `measure_candidate.sh` | el mismo instrumento sobre un paquete nuevo, para altas | sí |
| `test_anchor.py` | **control OFFLINE del ancla**, con el defecto que corrige demostrado y el control positivo de la tendencia 259 | **no** |
| `result.2026-10-02.tsv` | los 11 objetivos con veredicto del pase 50 y del 52, y la columna `cambia` | — |
| `candidates.2026-10-02.tsv` | las 13 piezas nuevas medidas por el canal `?text=` (**P117**) | — |

```sh
./remeasure.sh < targets.txt          # los 11 objetivos
./measure_candidate.sh <paquete> ...  # una o varias altas
python3 test_anchor.py                # 24/24, sin red
```

## El denominador, declarado

**11 paquetes re-medidos. De ellos 9 declaran un `org/repo` utilizable y 2 no** (`@timeback/caliper`
y `@timeback/oneroster`, que no declaran repositorio en absoluto). ⚠️ **Los 30 del pase 50 no se
re-midieron enteros: sólo los 9 cuyo veredicto era «sin licencia» o «indeterminado»**, que son los
únicos que la lista de 4 nombres podía haber dañado. Los 21 con campo permisivo y texto ya leído no
cambian de clase por agregar nombres de archivo.

## 🔴 El defecto que este pase le encuentra al instrumento del pase 51

El pase 51 declaró **obligatoria** el ancla `^package/(LICEN[CS]E|COPYING)[^/]*$` para no contar las
licencias de `node_modules` (**tendencia 259**: 144 archivos ajenos en `tutors-publish-npm`). El
ancla cumple eso **y es CASE-SENSITIVE**:

| Paquete | Archivo real | Ancla del pase 51 | Ancla corregida |
|---|---|---|---|
| `@learninglocker/xapi-agents` 4.4.3 | **`package/license`** (minúscula, sin extensión), **35.121 bytes de GPL-3.0** | 🔴 **raíz=0** → se publicaba «sin licencia en el tarball» | 🟢 **raíz=1 → GPL-3.0** |

🔵 **Es el mismo error que la tendencia 252**, que encontró que una lista de nombres de archivo es un
supuesto cultural —`COPYING.txt` en el mundo GNU— **sólo que esta vez el supuesto estaba adentro de
una expresión regular y lo había escrito el pase anterior.** El ancla corregida es
`^package/(licen[cs]e|copying)([._-][A-Za-z0-9]+)?$` **insensible a mayúsculas**, y tiene que cumplir
**dos** cosas a la vez, que es lo que `test_anchor.py` verifica: encontrar el texto con cualquier
capitalización **y seguir rechazando todo lo que no esté en la raíz de `package/`**, que es la única
razón por la que el ancla existe. ⚠️ **`licenses.json` y `LICENSES` quedan fuera a propósito: un
inventario de licencias no es un texto de licencia.**

## Los tres veredictos que cambian, y los dos que se precisan

| Paquete | Pase 50 | Pase 52 | Lo que lo resolvió |
|---|---|---|---|
| `@eduware/oneroster` 1.2.11 | ⚠️ indeterminado | 🟢 **licenciado 0BSD** — 🔴 **y el campo dice `MIT`** | el tarball |
| `@osu-cass/sb-components` 1.5.0-alpha.10 | ⚠️ indeterminado | 🟢 **licenciado MPL-2.0**, y el repo **NO ES PÚBLICO** (control del hermano) | el tarball + el hermano |
| `@learninglocker/xapi-agents` 4.4.3 | ⚠️ indeterminado | 🟢 **licenciado GPL-3.0** | el tarball, **sólo con el ancla corregida** |
| `@owen-x-tech/canvas-mcp` 1.1.0 | ⚠️ indeterminado | ⚠️ **campo MIT SIN TEXTO, medido por TRES canales** | los tres, en negativo |
| `frappe-mcp-server` 0.6.0 | ⚠️ indeterminado | ⚠️ **campo ISC SIN TEXTO, medido por TRES canales** | ídem |

🔵 **El patrón que esto deja: de los 5 «indeterminados» del pase 50, el tarball resuelve 3 y precisa
los otros 2.** La categoría «indeterminado» del pase 50 **no era una propiedad de los paquetes: era
una propiedad del canal que se les había aplicado.**

## 🔴 Y el control del HERMANO queda degradado a tercer lugar

El pase 51 presentó el control del hermano (**tendencia 255**) como la forma de partir
«indeterminado» en dos. Este pase le encuentra **dos límites que no estaban escritos**:

| Límite | Evidencia |
|---|---|
| **Tiene una precondición que nadie declaró: la organización tiene que publicar MÁS DE UN paquete.** No aplica a `Eduware-Inc`, `owentaylor` ni `appliedrelevance`, que publican uno solo | búsqueda en el registro por organización: un solo paquete cada una |
| **Es SUBORDINADO al tarball.** En `LearningLocker` **todos** los hermanos dan 404 —`xapi-validation`, `xapi-service`—, así que el control concluye *«el canal no llega a la organización»* y **el tarball resolvió la licencia igual** | `LearningLocker/*` → 404; `package/license` → GPL-3.0 |

🔵 **El orden correcto de los tres instrumentos es: 20 nombres → TARBALL → hermano.** El hermano no
responde *«qué licencia tiene»*: responde *«por qué no pude verlo»*, que es una pregunta de gestión y
no de licencia. **Ponerlo segundo cuesta un veredicto.**

## 🔴 El hallazgo que no se buscaba: dos paquetes de alcances distintos con el MISMO archivo de licencia

| Paquete | Campo | `package/LICENSE` | sha256 |
|---|---|---|---|
| `@superbuilders/oneroster` 0.7.0 | 🔴 ninguno | **0BSD**, *«Copyright (c) 2025 Bjorn Pagen»* | `8b211ca0…20efa` |
| `@eduware/oneroster` 1.2.11 | 🔴 **`MIT`** | **0BSD**, *«Copyright (c) 2025 Bjorn Pagen»* | 🔴 **`8b211ca0…20efa` — idéntico** |

🔴 **Dos alcances distintos (`@superbuilders`, `@eduware`), dos repositorios declarados distintos
(`trilogy-group/oneroster-ts`, `Eduware-Inc/eduware-oneroster`) y el MISMO archivo de licencia byte
a byte, que nombra a un tercero como titular.** ⚠️ **Y el segundo declara `MIT` en su manifiesto
mientras envía texto 0BSD.** Para una cotización los dos son permisivos y el riesgo comercial es
bajo; **para un inventario, el campo registra la licencia equivocada**, y el titular del permiso no
es ninguna de las dos organizaciones que publican.

🔵 **Es la séptima dirección del defecto campo-vs-texto** y la primera en que **campo y texto nombran
licencias DISTINTAS** —no «falta una de las dos»—; la octava apareció el mismo pase, en
`@pie-qti/*` (campo `MIT`, texto `ISC`), y ahí el lado equivocado es el **registro**, con el
repositorio consistente en tres artefactos. ⚠️ **La dirección del error no es predecible, y eso es
exactamente por qué los dos artefactos se leen siempre.**
