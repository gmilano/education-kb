---
industry: education
region: North America
updated: 2026-10-02
---

# ¿La procedencia llega al alumno? — gap 104, cerrado, y la respuesta es **SÍ hasta el documento y NO hasta la afirmación**

**Pase 48 del 2026-10-02, acción 3.** El pase 47 dejó **P108** apoyado en **una sola
lectura**: `rag_service.ts` mete `chunk_index` + `source` + `document_id` en el `metadata`
del resultado de recuperación. Eso es **la punta de recuperación**. La acción pedía la otra
punta, con una pregunta sola: **¿el cliente recibe la identidad de la fuente, o se consume
adentro para *ranking* y se descarta?**

```sh
python3 trace_citations.py /ruta/a/project-nomad     # 32/32
```

## 🟢 La respuesta, en una línea

**Llega, y llega hasta la pantalla.** La cadena está completa, medida en **siete saltos** del
árbol real de [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
(Apache-2.0), y cada salto es una aserción que falla si el upstream cambia.

| # | Salto | Archivo | Qué quedó medido |
|---|---|---|---|
| 1 | Recuperación **emite** la identidad | `admin/app/services/rag_service.ts` | El `metadata` de retorno de `searchSimilar` lleva `source`, `document_id`, `archive_title`, `archive_date`, `chunk_index`. 🔵 **Y el propio upstream deja escrito que `source` *«previously dropped here»*, lo que hacía imposible mapear un *chunk* a su documento — lo arreglaron para citas y para *recall@k*** |
| 2 | El prompt **inyectado** rotula cada bloque | `admin/app/utils/rag_prompt.ts` | `buildContextBlock` → `[Context N — Título (fecha)]`. ⚠️ **Deliberadamente SIN el score**: *«surfacing e.g. "42%" primes the model to distrust correct context»* |
| 3 | Se construye la lista de citas | `admin/app/utils/rag_prompt.ts` | `buildCitations`, y **se alimenta de lo INYECTADO, no de todo lo recuperado**: un *chunk* que el planificador de presupuesto descartó nunca llegó al modelo, así que citarlo acreditaría la respuesta a un documento que no la sostiene |
| 4 | La forma que cruza al cliente | `admin/types/chat.ts` | 🔴 **`ChatSource` tiene TRES campos: `title`, `date`, `source`.** Nada más |
| 5 | Se **persiste** en el mensaje | `chat_service.ts`, `models/chat_message.ts`, migración `1785468975052` | `JSON.stringify(sources)` → columna `sources` **text nullable** en `chat_messages` |
| 6 | Se **devuelve** al cliente | `chat_service.ts` | `JSON.parse(msg.sources)` en el historial, y el objeto directo en la respuesta nueva |
| 7 | La UI lo **renderiza** | `admin/inertia/components/chat/ChatMessageBubble.tsx` | Bajo la respuesta del asistente, sólo para `role === 'assistant'` |

## 🔴 Y el límite, que es lo que decide qué puede prometer P108

**P108 promete *«`synthetic` por turno, separando `direct_source` del resto»*. La primera
mitad se sostiene; la segunda no, y el instrumento lo prueba por ausencia:**

- **`ChatSource` no tiene ningún campo de tramo** — ni `offset`, ni `index`, ni `span`.
- **Ningún campo distingue una cita textual de una síntesis.** No hay `kind`, `label`,
  `direct_source`, `synthetic` ni `verbatim`.
- **`buildCitations` deduplica por documento**: *«a dozen chunks out of one archive collapse
  to one entry»*. La granularidad que cruza al cliente **es el documento, no la afirmación**.

**Consecuencia, y hay que escribirla antes de que alguien cotice P108:**

| Tramo de P108 | Veredicto | Por qué |
|---|---|---|
| Marcado **a nivel de turno/mensaje**, nombrando los documentos que lo sostienen | 🟢 **COTIZABLE como integración** | Los siete saltos ya existen, están persistidos y renderizados. Se consume `message.sources`; no hay que construir la procedencia |
| Separar **`direct_source` de `synthetic`** por afirmación | 🔴 **NO cotizable como integración — es desarrollo nuevo** | El dato no cruza al cliente y **no existe en el árbol**: habría que clasificar el texto generado contra los *chunks* inyectados |

🔵 **Esto concuerda con el gap 99 del pase 47** (*«0 de 33 repos emiten un límite dentro del
texto que generan»*) **y lo precisa con una pieza leída de punta a punta**: no es que falte el
límite del tramo en la salida — es que **la unidad de procedencia de esta arquitectura es el
documento**, por diseño y por una razón escrita (la deduplicación), no por olvido.

## Límites del instrumento, declarados

- **Es un trazado estático del árbol**, no una ejecución: no se levantó NOMAD ni se hizo una
  consulta real. Lo que está probado es que **el valor tiene camino** por los siete saltos,
  no que un despliegue concreto lo muestre siempre (`sources` es *nullable*, y un turno sin
  recuperación no lleva ninguna).
- **Un salto se verifica por subcadena** del archivo fuente. Si el upstream renombra, la
  aserción **falla** —que es lo que se quiere— pero puede fallar por el renombre y no por una
  pérdida de la procedencia. El veredicto hay que releerlo, no asumirlo.
- `HEAD` del clon leído: **rama `main`, el 2026-10-02**, con `--filter=blob:none` y
  `sparse-checkout` sobre `admin/app`, `admin/types`,
  `admin/inertia/components/chat` y `admin/database/migrations`.
