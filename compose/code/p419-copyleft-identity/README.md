---
industry: education
region: Global
updated: 2026-10-05
---

# `P419` — la identidad de un copyleft no se lee de las licencias que CITA

Artefactos del **pase 124 (2026-10-05, lectura `21:46Z`)**.

## El defecto, medido 2 de 2 contra payloads vivos

La compuerta del pase 123 (`p411-cession-identity-gate`) clasifica por palabra clave sobre el **cuerpo** del documento. Sobre los dos textos copyleft **prístinos** que midió el pase 124 se equivocó en los dos:

| repo | compuerta del pase 123 | lo que el texto ES | de dónde salió el error |
|---|---|---|---|
| `ahmedEid1/lumen` | 🔴 `AGPL-3.0` | **GPL-3.0** (`Version 3, 29 June 2007`) | GPL-3.0 trae la sección §13 *«Use with the GNU Affero General Public License»* |
| `xiaochong0302/course-tencent-cloud` | 🔴 `LGPL` | **GPL-2.0** (`Version 2, June 1991`) | GPL-2.0 cierra nombrando a la *«Lesser General Public License»* |

No es un defecto de regex: **un texto de licencia prístino NOMBRA a sus parientes**, y un clasificador que busca `affero` o `lesser` en el cuerpo lee la mención como el nombre.

🔴 **Por qué pesa más que un error de etiqueta.** GPL-3.0 y AGPL-3.0 se diferencian **sólo** en el uso **en red**. Una fila que dice AGPL sobre software GPL le prohíbe a un cliente un despliegue hospedado que en realidad tiene permitido; al revés, le habilita uno que no. Es la única columna que decide la entrega, y es la que el error corrompe.

## La regla

La familia se lee del **ENCABEZADO**: título + `Version N`. El cuerpo sirve para **confirmar**, nunca para nombrar. Las menciones que aparecen en el cuerpo y no en el encabezado se publican aparte, como **parentesco**.

## 🔴 Y la primera versión de este instrumento fue refutada por su propia suite

La v1 definía el encabezado como *«las primeras **6** líneas no vacías»*. Su suite la rechazó en 2 de 10 casos: **con una ventana de 6 líneas, la sección §13 de GPL-3.0 entra en la ventana y el instrumento vuelve a cometer exactamente el error de `P419` que vino a arreglar.**

🟢 **La ventana es `n=2`, y el número está MEDIDO, no elegido:** el encabezado de una licencia es título + versión, dos líneas. **Cualquier ventana más ancha que el encabezado admite CUERPO, y el cuerpo nombra parientes.**

🔵 Es el patrón que `P417` dejó escrito el pase 123 —*«una cifra es reproducible sólo contra una referencia FUERA del instrumento que la produjo»*— aplicado a un clasificador: la suite con casos reales fue la referencia externa, y refutó al autor. Si los fixtures hubieran sido *«lo que el instrumento ya hace»*, la v1 habría pasado en verde con el defecto adentro.

## Suite y corrida

- `test_identidad.py` — **10/10 🟢**. 7 casos de identidad (los 2 de `P419`, un AGPL real, Apache centrado con primera línea vacía, MIT, el EULA chino de `P421`, y un GPL **sin versión** que devuelve `GPL-?` y no se infiere, `P286`) + 3 casos de mención cruzada.
- `resultado.2026-10-05.txt` — corrida contra los **10** payloads reales de este pase: **10/10 correctos**, incluidos los 2 que la compuerta del pase 123 erraba.

## `P420` al lado: el tamaño no identifica

`PRISTINOS` guarda los tamaños de referencia, y el campo se llama `tamano_consistente` a propósito: coincidir con el tamaño prístino **no** confirma identidad. Tres AGPL-3.0 de este corpus miden **34.523 B** exactos con digests distintos (`math-question-bank`, `classroomio`, `koakademy`). Y `course-tencent-cloud` mide **18.431 B** contra los 18.046 B del GPL-2.0 prístino ⇒ es un GPL-2.0 **modificado**, lo que el campo informa sin llamarlo otra familia. La identificación sigue siendo el par (ARCHIVO, digest) de `P392`.
