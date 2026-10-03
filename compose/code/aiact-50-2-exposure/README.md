---
industry: education
region: EMEA
updated: 2026-10-02
---

# Exposición al Artículo 50(2) del AI Act de las 66 filas de `agents/top.md`

**Medido en el pase 45 del 2026-10-02 (acción 3, gap 91 CERRADO).** El pase 44 dejó escrito que el resultado esperado
era *«un vacío»* y que **conviene medirlo antes de que lo pregunte un cliente**. Se midió. **El vacío existe y es casi
total — pero no es total, y lo que sobrevive es más útil que el vacío.**

## La pregunta, que es una sola

**¿Esta pieza pone contenido sintético delante de un alumno o de un docente?** Y para las que sí: **¿tiene alguna forma
de marcado** (C2PA, metadatos, marca de agua, o nada)?

## El reparto de las 66 filas

| Veredicto | Filas | Qué significa |
|---|---|---|
| `gen` | **24** | la pieza **genera** el contenido |
| `gen-ind` | **7** | pedagogía empaquetada (una *skill*, un esquema, una superficie MCP de tutor): genera **a través del agente anfitrión** |
| `gen-cond` | **1** | sólo con un módulo opcional activado (`Project NOMAD`, con su módulo de AI local) |
| `pack` | **1** | no genera, pero es **donde el contenido generado se vuelve el curso que el alumno abre** (`scorm-mcp-server`) |
| `no` | **33** | mueve, registra, califica, sincroniza matrícula o supervisa exámenes — **no genera** |

🔵 **33 de 66 filas (50 %) ponen contenido sintético delante de una persona.** Exactamente la mitad de esta tabla, que
es la cifra de encuadre: **el Artículo 50(2) no es un problema de un rincón de esta KB, es un problema de la mitad.**

## 🔴 La medición del marcado: 0 de 33

Medido con `scan_marking.sh`, que **no busca en documentación**: clona el árbol de cada repo expuesto con
`--filter=blob:none` (ningún blob se descarga) y busca artefactos de marcado en **la lista de archivos**, más las
dependencias en **los manifiestos de raíz**.

| Magnitud | Valor |
|---|---|
| Repos barridos (los 32 expuestos + el empaquetador, menos 5 entradas de registro sin repo) | **33** |
| Archivos listados | **24.202** |
| Artefactos de **marcado** (`c2pa`, `watermark`, `synthid`, `content-credentials`, `invisible-watermark`, `imwatermark`) | 🔴 **0** |
| Manifiestos de raíz leídos | **26** |
| **Dependencias** de marcado en esos manifiestos | 🔴 **0** |
| Repos con **0 de todo** | **28 de 33** |
| Artefactos de **procedencia** (que no es lo mismo) | **15, en 5 repos** |

🔴 **Ninguna de las 33 piezas puede marcar su salida como artificialmente generada.** Ninguna se eligió por eso, y la
respuesta a la pregunta del pase 44 es la que el pase 44 predijo. **Lo que el pase 44 no predijo es lo que sigue.**

## 🟢 El hallazgo que cambia la conclusión: una fila SÍ emite una bandera legible por máquina

**`zijinz456/OpenTutor` (MIT, 127 ★) es la única de las 66 filas que emite, hacia el cliente y de forma estructurada,
una afirmación de que el contenido lo generó una AI.** Leído en el código, no en el README:

- `apps/api/services/provenance.py` → `build_provenance(..., generated: bool = True, ...)` arma un payload JSON con
  **`"generated": true`** y una lista **`"source_labels"` que incluye `"generated"`**. El valor por omisión es `True`:
  **falla hacia el lado seguro.**
- `apps/api/services/agent/turn_pipeline.py:144-173` lo llama con `generated=True` y `source_labels=["generated"]`
  **fijos** en el camino del turno del agente, y su docstring dice *«for UI and persistence»*.
- `apps/api/routers/chat.py:214` manda **`"provenance": payload.get("provenance")`** al cliente, y
  `apps/api/schemas/task.py:59` declara `provenance: dict | None` en el esquema de tarea. **O sea: se persiste y se
  sirve, no es telemetría interna.**

🔴 **Y qué le falta para ser Artículo 50(2), que es la parte que se cotiza:**

1. **No es una marca *en* el artefacto, es un campo JSON *al lado*.** Si el texto se copia, se exporta o se reenvía, la
   marca no viaja. El Artículo 50(2) pide que la salida esté marcada y sea **detectable**; esto es detectable sólo
   mientras no se separe del sobre.
2. **Marca el turno, no el tramo.** `generated=True` está fijo en ese camino, así que no distingue una cita textual de
   una fuente de una síntesis del modelo.
3. **No está firmado.** Nada ata la bandera al contenido, así que no es resistente a manipulación — que es justamente a
   lo que apunta *«effective, interoperable, robust and reliable»*.

🔵 **Pero es el punto de injerto más barato que tiene esta KB**: el campo ya existe, ya viaja al cliente y ya está en el
esquema. Marcar de verdad es **llenar un campo que ya está**, no abrir una capa nueva.

## 🟢 La segunda pieza: `lineage-skill` etiqueta la procedencia **por afirmación**

`JuneYaooo/lineage-skill` (**Apache-2.0**, 448 ★) trae `references/provenance-policy.md`: un **vocabulario cerrado de 9
valores** que el agente debe asignar *«para toda afirmación consecuente, respuesta de tarea, regla de rúbrica, juicio de
feedback y regla de Personal Skill»*.

🔵 **Cuatro de los nueve valores son, literalmente, «esto lo produjo el modelo»:**
`source_grounded_synthesis`, `cross_source_synthesis`, `mentor_inference` y `external_general_knowledge` (más
`unsupported`, que es el caso sin evidencia). Los otros cuatro anclan a fuente humana o a evidencia observable.
Y la política ya dice: *«High-impact inference needs a visible label and human review when evidence is thin»*.

🔴 **Lo que no es:** una marca legible por máquina. Es **prosa dirigida al modelo**, no un campo emitido junto al
artefacto. **Pero es la granularidad correcta** —por afirmación, no por turno— que es exactamente lo que le falta a
OpenTutor. 🔵 **Las dos piezas son mitades complementarias del mismo componente, y ninguna de las dos lo sabe.**

⚠️ **Y la distinción que hay que hacer en voz alta, porque los 15 hits de «procedencia» invitan al error:** los 13 hits
restantes (`DeepTutor` 3, `universal-examprep-skill` 8, `lumen` 2) son **procedencia de fuente** —de qué documento salió
una afirmación, o de qué clon salió una fila de base de datos—, **no procedencia sintética**. Saber de dónde viene el
material no dice que el material lo escribió una máquina. **Son dos problemas y comparten una palabra.**

## 🔴 El dato de calendario, con la corrección de encuadre que hay que decir

Confirmado en este pase por un **tercer canal independiente** (los dos primeros son de los pases 43 y 44), y
**coincide con lo que esta base ya tenía bien**:

| Obligación | Fecha | Estado al 2026-10-02 |
|---|---|---|
| Art. 50 transparencia (declarar que se interactúa con AI) | **2026-08-02** | 🔴 **ya vigente, vencida hace 2 meses** |
| **Art. 50(2) marcado legible por máquina** — sistemas **puestos en el mercado desde** el 2026-08-02 | **2026-08-02** | 🔴 **YA VIGENTE** |
| **Art. 50(2)** — *backstop* para sistemas **ya en el mercado antes** del 2026-08-02 | **2026-12-02** | ⏳ **61 días** |

🔵 **El encuadre que hay que corregir al usarlo con un cliente, aunque la fecha esté bien:** el 2026-12-02 **no es
«cuándo empieza el Artículo 50(2)»** — es **el plazo de gracia de lo que ya estaba desplegado**. Para **cualquier
sistema nuevo** —que es exactamente lo que es un *engagement* de Globant que entrega un tutor construido sobre estas
piezas— **la obligación rige desde el 2026-08-02 y ya está vencida al momento de entregar.** Decir «faltan 61 días»
sobre un desarrollo nuevo es **tranquilizar con la fecha equivocada.**

🟢 **Y el dato de responsabilidad, que esta KB NO tenía y decide quién paga:** el deber del Artículo 50(2) recae en el
**proveedor** —quien desarrolla el sistema generativo y lo pone en el mercado, incluidos los proveedores de GPAI— **no
en el *deployer* ni en el usuario final.** Para un *engagement*: si Globant **construye y entrega** el sistema, el deber
está del lado del entregable; si el cliente sólo **despliega** algo de un tercero, el deber está aguas arriba. **Es una
pregunta de *discovery*, y hoy no está en ningún checklist de esta base.**

⚠️ **Límite de fuente, que se repite cada vez que se citen estas fechas:** **cuatro** canales primarios o
cuasi-primarios siguen bloqueados por el proxy de egreso —`eur-lex.europa.eu`, `artificialintelligenceact.eu`,
`data.europa.eu` y ahora también **`digital-strategy.ec.europa.eu`**, la página oficial del *Code of Practice on
Transparency of AI-generated Content*—. **Gap 92 reconfirmado y ampliado a cuatro dominios.** Las fechas están
confirmadas por **tres canales secundarios independientes y concordantes**, no por texto consolidado.

## Qué hay

| Archivo | Qué es |
|---|---|
| `rows.tsv` | Las **66 filas** con su veredicto. El comentario de cabecera define los cinco valores. |
| `scan_marking.sh` | El barrido. **Reproducible**: clona con `--filter=blob:none`, lista archivos, lee manifiestos de raíz. Sólo `git`, `curl`, `awk`. |
| `result.2026-10-02.tsv` | La salida de este pase, versionada, para que el próximo **compare** en vez de volver a medir desde cero. |

```
sh scan_marking.sh [workdir]      # imprime los totales y deja el detalle por repo
```

## La oportunidad, que es la razón de haber medido esto

🟢 **Un componente transversal de marcado, y el hueco está medido:** 32 filas lo necesitan, **1** tiene el campo pero no
la marca, **1** tiene la granularidad pero no el campo, **0** tienen la marca. La capa forense **ya existe en esta KB y
es permisiva** —`MarkLLM` y la familia de detectores de `repos/foundations.md`, más SynthID-Text (Apache-2.0) en
**P33**—, así que **el componente no hay que inventarlo: hay que conectarlo**. Ver el patrón **P99**.
