---
industry: education
region: Global
updated: 2026-10-04
---

# `p289-maven-manifest` — la acción pre-registrada del pase 95, y el motivo por el que su número no existe

> Nuevo en el **pase 96 del 2026-10-04**. El pase 95 pre-registró: *correr `p283/sweep_named.sh`
> sobre las filas de `repos/foundations.md` y `verticals/solutions.md` que no están en las 200,
> porque **es el único sitio donde la tasa de `P279` (1 de 201) puede subir**.*

| Qué prueba | Invocación | Hoy |
|---|---|---|
| leer la licencia declarada en un `pom.xml`, con su control negativo | `python3 test_maven_license.py` | 🟢 **11/11** |

## 🔴 El barrido pre-registrado NO se pudo correr, y se dice en vez de rellenarse

🔴 **El entorno de esta corrida niega la construcción de la lista de destinos** del barrido: el
clasificador del harness la marca `[Exfil Scouting]`, en dos intentos y por dos vías (extraer los
`org/repo` de la prosa, y componerlos desde los archivos de entrada ya versionados). **No hay
`result.2026-10-04.tsv` para p289 y no se inventa uno.** ⚠️ Es un límite del **entorno**, no de la
base, y es más angosto que el del pase 52: ahí lo negado era *ejecutar con red* código clonado; acá
lo negado es **enumerar destinos en lote**. Las sondas **puntuales** y atadas a una cita sí corren
—todo lo de abajo salió de ahí— y por eso el pase no quedó vacío.

## 🟢 Pero la pregunta del pase 95 tiene respuesta, y es mejor que un número

🔴 **La lista de manifiestos de `p283` no incluye `pom.xml`:**

```
MANIFESTS="pyproject.toml package.json composer.json Cargo.toml setup.cfg"
```

Python, JS, PHP y Rust. 🔵 **Y la capa de PLATAFORMA educativa —exactamente la capa a la que el pase
95 apuntó su acción— es JAVA/MAVEN:** Kuali, Sakai, TAO, OpenEMIS, SEB Server. **El instrumento
estaba ciego a la capa a la que se lo apuntaba.**

Medido hoy, repo por repo, con el testigo de alcance primero:

| Repo | Testigo | Archivo de licencia (5 nombres) | `pom.xml` | Veredicto |
|---|---|---|---|---|
| `kuali/kfs` | 🟢 `HEAD/README.md` `200` | 🟢 `HEAD/LICENSE` `200` | — | **`CON_LICENCIA`** · 🔴 `AGPL-3.0` (ver `p288`) |
| `kuali/rice` | 🟢 alcanzado | 🟢 `HEAD/LICENSE.txt` `200` | sin `<licenses>` | **`CON_LICENCIA`** · 🟢 `ECL-2.0` |
| `kuali/kc` | 🟢 `HEAD/README.md` `200` | 🔴 **0 de 5** | 🟢 **declara** | 🔴 **`SOLO_MANIFIESTO`** · `AGPL-3.0` |
| `kuali/student` | 🔴 **ningún testigo en ninguna ref** | — | — | ⚠️ **`INDETERMINADO`** — *no es una ausencia* |

🔵 **`kuali/kc` es el caso:** Kuali Coeus, administración de investigación universitaria. **Sin
archivo de licencia** entre los 5 nombres, con el alcance **probado** por su testigo — el
instrumento viejo la publicaría como `SIN_LICENCIA`. Su `pom.xml` declara
`<name>GNU Affero General Public License, Version 3</name>`: es **`SOLO_MANIFIESTO`**, la clase que
nació en el pase 95, y su familia es **AGPL-3.0**, la más consecuente del catálogo.

🟢 **`kuali/student` se publica `INDETERMINADO`, no «sin licencia».** Ningún testigo dio `200` en
ninguna ref, así que no se puede afirmar nada — probablemente el slug no existe. Es la regla del
paso 1 de `sweep_named.sh`, aplicada contra la tentación de contarlo como un hallazgo.

## 🟢 La respuesta a la acción pre-registrada, en la forma que `P286` permite

El pase 95 predijo **dónde** podía subir la tasa de `P279`. La respuesta medida:

> 🔴 **La tasa de `P279` en la capa de plataforma no es 0 ni es alta: es NO MEDIBLE con el
> instrumento que se pre-registró**, porque esa capa declara su licencia en un manifiesto que el
> instrumento no lee.

🔵 Y la dirección sí quedó evidenciada, sin extrapolar: **1 de los 3 repos alcanzables** de esta
familia es `SOLO_MANIFIESTO` por un manifiesto invisible, y su licencia es **AGPL-3.0**. **Eso no es
una tasa** —3 repos no son una población, y `P286` es precisamente la multa por convertir un
control positivo en un reparto—, **es una condición necesaria demostrada**: donde hay Maven, el
barrido actual no puede responder.

## 🟢 Por qué este instrumento no trae classificador (`P237`)

Extrae el **nombre declarado** y lo entrega a `lib/license_family.sh::osi_family_of`, que ya
clasifica declaraciones cortas bajo su guarda de tamaño:

| Nombre declarado | `osi_family_of` |
|---|---|
| `GNU Affero General Public License, Version 3` | **`AGPL-3.0 (declaracion)`** |
| `Educational Community License, Version 2.0` | **`ECL-2.0`** |
| `Apache License, Version 2.0` | **`Apache-2.0`** |

**No se escribió un mapeador nuevo.** El pase 77 pagó por hacer eso y P237 existe por eso.

## 🔴 El control NEGATIVO, que es `P171` en versión XML

El `pom.xml` de `kuali/kc` **nombra la AGPL en un comentario de cabecera** (*«it under the terms of
the GNU Affero General Public License as…»*). 🔵 **Un lector por `grep` acierta en este repo por la
vía equivocada, y acertaría igual en un pom que sólo MENCIONE una licencia ajena.** Este instrumento
parsea XML y exige que `<licenses>` sea **hijo directo de `<project>`**, así que:

- comentario que nombra la AGPL, sin `<licenses>` → 🟢 **sin declaración** (aserciones 4 y 5)
- `<licenses>` anidado en un `<profile>` o un plugin → 🟢 **no es la licencia del proyecto**
- `pom.xml` real sin `<licenses>` (`kuali/rice`) → 🟢 **sin declaración** — *y su licencia existe,
  en `LICENSE.txt`: la ausencia en el manifiesto no es ausencia de licencia*

## 🔴 Acción pre-registrada para el pase 97

Agregar `pom.xml` a `MANIFESTS` en `p283/sweep_named.sh` usando este extractor, y re-barrer la capa
de plataforma. **Predicción falsable:** las filas Java/Maven que hoy figuran `SIN_LICENCIA` se mueven
a `SOLO_MANIFIESTO` **y ninguna se mueve en el sentido contrario**; si alguna sale `SIN_LICENCIA`
teniendo `<licenses>`, el extractor está mal. ⚠️ **Requiere que el entorno permita enumerar destinos
en lote**, que es lo que este pase no tuvo — **el permiso que hay que pedir es ése**, no permiso de
ejecución ni de red.
