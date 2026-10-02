---
industry: education
region: EMEA
updated: 2026-10-02
---

# ¿Hay por dónde agarrar el tramo? — gap 99, cerrado con una medición y la respuesta es NO

**Pase 47 del 2026-10-02, acción 3.** El pase 46 escribió el componente de marcado del
Artículo 50(2) ([`../aiact-50-2-marking/`](../aiact-50-2-marking/README.md)) y lo dejó con un
límite declarado: **mapea, transporta y asevera, pero no clasifica.** Alguien tiene que
**asignar** una de las 9 etiquetas de `lineage-skill` a cada tramo, y el pase 46 no sabía si
algo en esta base lo hacía. La acción 3 pedía una pregunta sola: **¿hay por dónde agarrar el
tramo, o la salida es un bloque de texto opaco?**

## 🔴 La respuesta, en una línea

**Cero de 33 repos emiten un límite dentro del texto que el modelo genera.** Las tres piezas
que el barrido marcó `HANDLE` resultaron, al abrirlas, **límites sobre la ENTRADA** —el *chunk*
recuperado, la página del PDF— y una de las tres **no es procedencia en absoluto**. El
clasificador hay que escribirlo entero, y eso cambia el presupuesto.

## Lo que se midió

| Magnitud | Valor |
|---|---|
| Filas expuestas barridas (las 32 + el empaquetador, menos las entradas de registro sin repo) | **33** |
| Archivos listados (clones `--filter=blob:none`, ningún blob descargado) | **24.206** |
| Archivos candidatos por ruta | **3.249** |
| Archivos **leídos de verdad** (tope de 25 por repo) | **432** |
| `HANDLE` → al verificar a mano, **límites de entrada** | **3** |
| `WEAK` (vocabulario adyacente, ningún límite) | **16** |
| `OPAQUE` (leído, nada) | **8** |
| `NO_CANDIDATES` (ninguna ruta candidata) | **6** |

⚠️ **El límite del instrumento, dicho antes que el resultado:** el barrido lee **25 archivos
por repo**, elegidos por patrón de ruta. Un `OPAQUE` significa *«ningún límite de tramo en los
archivos que este script eligió leer»*, **no** *«ningún límite de tramo en el repo»*. El tope
está en la salida y es la razón por la que esta medición responde *«no encontré»* y no
*«no existe»*.

## 🔴 Las tres `HANDLE`, abiertas una por una — y las tres se caen

Ésta es la parte que hace falta decir, porque el TSV solo diría `HANDLE` tres veces:

| Repo | Token | Qué es realmente | Veredicto |
|---|---|---|---|
| `Crosstalk-Solutions/project-nomad` | `chunk_index` | `admin/app/services/rag_service.ts:1137` lo mete en el `metadata` del **resultado de recuperación**, junto con `source` y `document_id` | ⚠️ **límite de la ENTRADA**: dice de qué documento salió el contexto, no qué parte de la respuesta lo usó |
| `microsoft/Shiksha-Copilot` | `end_index` | `utils/toc_extractor.py:110` — `toc_end_index = min(5, len(images))`, las primeras 5 páginas de un PDF | 🔴 **falso positivo**: no es procedencia, es paginado de ingesta |
| `ahmedEid1/lumen` | `chunk_index` | `app/models/lesson_chunk.py:57` — una **columna de base de datos** con `UniqueConstraint("lesson_id", "chunk_index")` | ⚠️ **límite de la ENTRADA**: indexa el corpus troceado, no la salida |

🔵 **Y el dato de encuadre que explica cómo se equivoca un lector apurado:** el vocabulario de
índices está **en todas partes** —16 repos dieron `WEAK` con `citation`, `chunk`, `grounding`,
`provenance`— así que un barrido de palabras concluye que el gancho existe. **No existe.** Todo
ese vocabulario habla de **de dónde vino el contexto**, y ni una sola pieza habla de **qué parte
de su propia salida escribió el modelo.** Es la misma asimetría que el pase 45 midió con otro
instrumento (*«13 de 15 son procedencia de FUENTE, no sintética»*), ahora confirmada leyendo
código en vez de nombres de archivo.

## 🟢 Y sin embargo hay un piloto — por otra razón que la que la acción esperaba

`project-nomad` es la fila por donde empezar, **no** porque dé el tramo, sino porque lleva
`chunk_index` + `source` + `document_id` **hasta el resultado** que alimenta la generación.
El comentario del propio repo dice para qué: *«needed for citations and for recall@k scoring»*.
Con eso **se puede separar `direct_source` del resto a nivel de turno** —la mitad barata del
vocabulario de `lineage-skill`— sin resolver los límites de tramo. **Es media respuesta
entregable, y conviene cotizarla como media.**

## Qué significa para el presupuesto

1. 🔴 **El clasificador por tramo es desarrollo nuevo, no integración.** No hay nada que
   envolver. El componente del pase 46 queda correcto y **sin alimentador**.
2. ⚠️ **La ruta barata no da tramos, da turnos.** Un `synthetic` por turno se puede derivar hoy
   en las piezas con `grounding`/`citation`; el `spans` del pase 46 **no**.
3. 🟢 **Y el empaquetado sigue siendo el punto de inyección correcto** (gap 100,
   [`../aiact-50-2-pack/`](../aiact-50-2-pack/README.md)): marcar el curso **entero** como
   generado no necesita clasificador. **El marcado grueso es entregable hoy; el fino, no.**

## Correr el barrido

```sh
sh scan_spans.sh [workdir]        # CAP=25 por omisión; CAP=50 sh scan_spans.sh para ampliar
```

Resultado versionado en [`result.2026-10-02.tsv`](result.2026-10-02.tsv). **El TSV guarda los
tokens encontrados por repo**, así que el próximo pase puede contradecir este veredicto sin
volver a barrer: si un token de la columna `tokens` resulta ser un límite de salida, la fila
cambia y la cuenta con ella.
