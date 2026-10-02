---
industry: education
region: EMEA
updated: 2026-10-02
---

# El componente transversal de marcado del Artículo 50(2) — gap 95, cerrado con código

**Pase 46 del 2026-10-02, acción 1.** El pase 45 midió el hueco
([`../aiact-50-2-exposure/`](../aiact-50-2-exposure/README.md)): **32 de las 66 filas** de
`agents/top.md` ponen contenido sintético delante de un alumno o un docente, y **0 de 33
repos** pueden marcarlo. También encontró que **las tres piezas ya estaban en esta base y
sólo había que unirlas**. Esta carpeta es esa unión, y **convierte «esta KB no cumple el
Artículo 50(2)» en «esta KB tiene el componente»**.

| Pieza | De dónde sale | Qué aportaba | Qué le faltaba |
|---|---|---|---|
| **El campo y el transporte** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) (**MIT**) | `build_provenance` → `{"generated": true, "source_labels": [… "generated"]}`, servido en `routers/chat.py:214` | marca **el turno**, no el tramo |
| **La etiqueta y la granularidad** | [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) (**Apache-2.0**) | vocabulario **cerrado de 9 valores** por afirmación | **no tiene booleano ni transporte** |
| **La firma** | `MarkLLM` / SynthID-Text (**Apache-2.0**, **P33**) | marca **dentro** del artefacto | 🔴 **no implementada acá** — ver `sign_hook` |

## 🔵 La decisión de diseño que nadie había tomado — y son CINCO, no cuatro

El pase 45 contó *«cuatro valores son literalmente ‘esto lo produjo el modelo’»*:
`source_grounded_synthesis`, `cross_source_synthesis`, `mentor_inference` y
`external_general_knowledge`. **Este componente marca cinco.** El quinto es `unsupported`, y
el criterio es explícito: **`synthetic` es verdadero cuando el MODELO escribió las palabras**
— no cuando la afirmación es falsa, ni cuando está mal fundada. Son ejes distintos y
confundirlos es cómo este campo se llena mal.

| Valor de `lineage-skill` | `synthetic` | Por qué |
|---|---|---|
| `direct_source` | **false** | lo escribió la fuente del docente; el modelo cita |
| `source_grounded_synthesis` | **true** | síntesis acotada **sigue siendo** síntesis: las oraciones son del modelo |
| `cross_source_synthesis` | **true** | ídem, cruzando fuentes |
| `mentor_inference` | **true** | *«runtime interpretation not stated by the teacher»* — el true más claro del vocabulario |
| `learner_hypothesis` | **false** | lo escribió **el alumno**, una persona |
| `learner_observation` | **false** | ídem |
| `real_world_evidence` | **false** | un hecho del mundo transportado, no generado |
| `external_general_knowledge` | **true** | salió de los pesos del modelo; nada más pudo aportarlo |
| 🔵 `unsupported` | **true** | **la decisión** — ver abajo |

🔵 **Por qué `unsupported` se marca, en contra de cómo se lee.** *«No adequate evidence is
available»* habla de **evidencia**, no de autoría, así que parece una quinta categoría y no un
quinto `true`. Se marca igual **porque la alternativa es peor**: si ninguna fuente sustenta la
afirmación, ninguna fuente **la escribió** tampoco, y el único autor que queda es el modelo.
Marcarlo `false` produciría exactamente el caso que el Artículo 50(2) existe para evitar:
**prosa del modelo sin fuente llegando a un alumno con `synthetic: false` adosado.**

⚠️ **Y el error simétrico, que importa igual:** marcar como generado por AI un tramo que
escribió **el alumno** le estaría diciendo a un estudiante que su propia oración la escribió
una máquina. Las cuatro categorías humanas se devuelven `false` a propósito; *«por las dudas
marco todo»* no es cautela, es dato incorrecto.

**Falla cerrado:** una etiqueta que no está en el vocabulario se marca `synthetic: true` **y
se señala** con `flags: ["unknown_provenance"]`, así que es visible además de segura. Si
`lineage-skill` agrega un décimo valor, esta base lo marca y lo muestra en vez de dejarlo
pasar — y `test_marking.py` **asevera el vocabulario contra el archivo de política upstream**,
de modo que la deriva rompe la prueba en vez de aparecer en producción.

## Lo que agrega sobre OpenTutor, y en qué es más ESTRICTO

El payload conserva `generated` y `source_labels` con el mismo significado que
`routers/chat.py:214` ya sirve y `schemas/task.py:59` ya persiste — **un consumidor que sólo
entiende el nivel de turno sigue funcionando**. Lo nuevo es `spans`, `synthetic_span_count` y
`synthetic_char_count`.

🟢 **Y la diferencia que no es sólo granularidad:** `turn_pipeline.py` de OpenTutor fija
`generated=True` en el camino del agente, así que **no puede representar un turno que sólo
cita**. Acá `generated` es el **OR sobre los tramos**, medido: el turno de ejemplo de la
prueba —una cita del material, una inferencia del tutor y una observación del alumno— reporta
**1 de 3 tramos sintéticos, 81 de 170 caracteres**, y un turno que sólo cita y relata reporta
`generated: false` **porque se midió, no porque se asumió**.

## 🔴 El límite, dicho en voz alta: esto NO es una marca de agua

`sign_hook()` es **una costura declarada y vacía**, y devuelve el artefacto sin tocarlo. La
firma dentro del artefacto (`MarkLLM` / SynthID-Text, **P33**) es un *watermark* sobre los
**tokens** generados y necesita el decodificador; este módulo corre **después** de decodificar,
así que no puede producirla y no finge hacerlo.

🟢 **Lo que sí mejora respecto del límite que midió el pase 45:** la marca ya no vive sólo en
el sobre. `detach_artifact()` emite **el artefacto solo** —texto + tramos, sin envoltorio— y la
prueba asevera que **los desplazamientos sobreviven un `json.dumps` → `json.loads`** y siguen
seleccionando exactamente la oración generada (rango `(50, 131)` en el caso de prueba). Copiar
el texto **y sus tramos** conserva la marca; copiar sólo el texto, no. **Es una mejora
medible, no una marca de agua, y llamarla así sería el tipo de dato incorrecto que esta base
viene corrigiendo.**

## 🟢 El punto de inyección: UNA vez en el empaquetado, no 32 veces

**La acción 3 de este mismo pase lo decidió, y a favor** (ver
[`gap 97`](../../intel/trends.md)). `manifest_metadata_fragment()` emite el XML para splicear
en `<metadata>` de `imsmanifest.xml`, **con una condición dura y medida**:

🔴 **El marcador DEBE declarar su propio *namespace*.** Verificado con `xmllint` contra el
`imscp_v1p1.xsd` que empaqueta `scorm-mcp-server`:

| Caso | Resultado |
|---|---|
| manifiesto base | `validates` |
| `<m:aiGenerated xmlns:m="urn:globant:aiact:50-2">` dentro de `<metadata>` | 🟢 **`validates`** |
| un elemento en el *namespace* por omisión dentro de `<metadata>` | 🔴 **`fails to validate`** |

Porque `metadataType` termina en `<xsd:group ref="grp.any"/>`, que es
`<xsd:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>`:
**cualquier cantidad de elementos de cualquier otro *namespace*, validados laxamente.**
`test_marking.py --with-xmllint` corre esa validación de verdad.

## Correr las pruebas

```sh
python3 test_marking.py                   # 23 checks, sólo stdlib
SCORM_SCHEMAS=/ruta/a/scorm-mcp-server/schemas \
  python3 test_marking.py --with-xmllint  # 24: agrega la conformidad real del manifiesto
```

Resultado sobre Python 3.11 y `xmllint` 2.9:

```
24/24 checks passed
```

Las **tres aserciones que pidió la acción 1** son los tres bloques del medio: un tramo citado
textualmente **no** se marca; un tramo `mentor_inference` **sí**; y la marca **sobrevive** al
`json.dumps` → `json.loads` del artefacto separado del sobre, con los desplazamientos intactos.

## Lo que esto NO resuelve

- **No es asesoramiento legal, y el texto primario sigue inalcanzable** (**gap 92**: cuatro
  canales `connect_rejected` / `EGRESS_BLOCKED`). Produce el marcado legible por máquina; que
  eso **baste** no es algo que pueda aseverar un test. Y para educación la fecha que esta base
  tiene confirmada **por tres canales secundarios concordantes, no por primaria**, es
  **Anexo III → 2027-12-02**.
- **No clasifica.** Alguien tiene que **asignar** la etiqueta de `lineage-skill` a cada tramo;
  este módulo mapea, transporta y asevera. El clasificador es el trabajo de integración y se
  cotiza aparte.
- **No modifica los 32 generadores.** Define el contrato que tendrían que emitir, y por la
  acción 3 el punto barato es el empaquetado.
