---
industry: education
region: Global
updated: 2026-10-03
---

# `p172-payload-license-sweep` — ¿la cesión está DENTRO del dato? (pase 65 del 2026-10-03)

Ejecuta la **acción 1 del pase 65**: el pase 64 midió **32 filas** de `agents/top.md` como
`UNLICENSED` preguntando por el **ARCHIVO** (*«¿hay archivo de licencia en alguno de 14
nombres?»*). **P172** —hallado en las ontologías de `FWU-DE`, cuya cesión vive en una anotación
`dct:license` dentro de `src/ontology/*-edit.owl`— dice que esa pregunta puede devolver una
**ausencia falsa**. Este instrumento hace la pregunta del **PAYLOAD** sobre las mismas filas.

## El resultado: «32 sin licencia» era una cifra inflada un 31 %

De las **29** filas no-`FWU-DE`, **7 declaran cesión en el payload**. Sumadas las **3** de
`FWU-DE` que el pase 64 ya había leído, **10 de las 32** no eran ausencias.

| Veredicto | n (de 29) | Qué significa |
|---|---|---|
| `PAYLOAD-LICENSED` | **7** | se LEYÓ una declaración con valor en un archivo de payload |
| `PAYLOAD-SILENT` | **22** | payload alcanzado y **sin** declaración: ausencia medida en dos capas |
| `UNREACHABLE` | **0** | — |

**El denominador del pase 64 queda en 22 ausencias medidas, no 32.**

### Las 7, con el artefacto exacto

| Fila | Archivo | Declaración | Clase |
|---|---|---|---|
| `DMontgomery40/mcp-canvas-lms` | `package.json` | `"license": "MIT"` | identificador |
| `Timadey/proctor` | `package.json` | `"license": "MIT"` | identificador |
| `ink-waffle/moodle-mcp` | `package.json` | `"license": "MIT"` | identificador |
| `tejpalvirk/student` | `package.json` | `"license": "MIT"` | identificador |
| `HKUDS/AI-Researcher` | `setup.cfg` | `license = MIT` | identificador |
| `marcusgreen/moodle-tool_aiconnect` | `version.php` | otorgamiento GPL + `@copyright 2024 Marcus Green` | **cesión** |
| `alvarogregori/moodle-ai-graded-assignment` | `lib.php` | otorgamiento GPL + `@copyright 2026 Alvaro Gregori` | **cesión** |

## Las dos clases no valen lo mismo, y la diferencia decide un engagement

**P179.** Un campo `"license": "MIT"` de manifiesto es un **IDENTIFICADOR**: nombra la licencia
y no transporta **ni titular, ni año, ni una línea del texto**. Es **P168** llevado al límite
—aquel medía que un archivo de 19 bytes es una afirmación y no una cesión; esto son **cero**
bytes de otorgamiento—. El **encabezado de fuente de Moodle**, en cambio, trae la frase de
otorgamiento completa (*«you can redistribute it and/or modify it under the terms of…»*),
**titular con nombre, año y versión** (`@license … GNU GPL v3 or later`): eso sí es una cesión,
y la GPL contempla explícitamente esta forma (*«You should have received a copy…»*).

⚠️ **Operativamente: las 5 filas de identificador se piden como trámite —la intención del autor
está documentada en dos lugares— pero NO se entregan a legales como están.** Las 2 de
encabezado GPL se usan.

### El identificador viaja; el texto no viaja a ninguna parte (medido en 3 canales)

Para las 3 filas publicadas en npm, el identificador se **corroboró por canal independiente**
—el registro declara `MIT` en las tres— y después se bajó el tarball publicado:

| Paquete | repo `package.json` | registro npm | ¿`LICENSE` en el tarball? |
|---|---|---|---|
| `canvas-mcp-server` (`DMontgomery40`) | MIT | **MIT** (v2.2.3) | 🔴 **NO** |
| `@timadey/proctor` | MIT | **MIT** (v1.2.6) | 🔴 **NO** |
| `@ink-waffle/moodle-mcp` | MIT | **MIT** (v0.2.0) | 🔴 **NO** |

🔴 **Y dos de los tres manifiestos PROMETEN el archivo que no existe:** `DMontgomery40` y
`Timadey` listan `"LICENSE"` en su array `files` de npm, y ese archivo no está **ni en el repo**
(404 en 14 nombres, pase 64) **ni en el artefacto publicado** (medido arriba). En `Timadey` la
promesa es más vieja que el repo: el pase 41 midió con `git log --all --name-only` que **no hay
`LICENSE` en ningún commit de toda la historia**.
⚠️ `tejpalvirk/student` **no está publicado en npm** (registro **404**): su cesión depende de un
solo canal, el manifiesto del repo.

## La capa de dato semántico: el caso que más vale del pase

**La acción mandaba empezar por los repos con `.ttl`/`.owl`/`.jsonld`.** El listado se obtuvo por
el canal HTML (`raw` no lista directorios) y el resultado **refuta una reserva publicada**:

🟢 **`dini-ag-kim/school-curriculum-pg` —la capa de currículo alemana POR LAND— SÍ cede, y cede
`CC BY-SA 4.0`, en las 25 serializaciones, los 16 archivos `lp-land-XX-full.owl` incluidos.**
La anotación está sobre el IRI de la ontología, con **titulares identificados por ORCID**, fecha
y IRI versionado — una cesión más completa que la de muchos archivos `LICENSE`:

```turtle
<https://w3id.org/lehrplan/ontology/> rdf:type owl:Ontology ;
    owl:versionIRI <https://w3id.org/lehrplan/ontology/1.0.0-8> ;
    terms:creator <https://orcid.org/0000-0001-6378-2618> , … ;
    terms:license <https://creativecommons.org/licenses/by-sa/4.0/> ;
    terms:title "Curriculum Ontology"@en , "Lehrplan Ontologie"@de .
```

🔴 **La tendencia 457 del pase 63 escribió que «lo que sigue sin licencia es la capa que agrega
el valor específico: la cobertura por Land». Medido: la cobertura por Land está cedida.** La
reserva era correcta en su fecha —la licencia no está en la raíz— y **falsa sobre el hecho**.

## Tres defectos de extracción, cada uno con su control

El instrumento se construyó dos veces porque la pregunta *«¿declara licencia?»* tiene **al menos
tres serializaciones**, y un `grep` que acierta una **reporta ausencia** en las otras. Son de la
familia de **P171** y están fijados en `test_extract.py` (8 asertos, 8 pasan):

| | Defecto | Dónde se midió | Control |
|---|---|---|---|
| **D1** | **predicado como URI**: `<…dc/terms/license> <…by-sa/4.0/>` → tomar el PRIMER URI devuelve el **predicado** y lo publica como licencia | `reasoned.ttl` | `test_D1_predicate_as_uri` |
| **D2** | **nodo en blanco**: `dct:license [ rdf:value <…by/4.0/> ; … ]` → el URI no es adyacente al predicado | `jp-cos/dataset-20250927.ttl` | `test_D2_blank_node` |
| **D3** | **profundidad**: una descripción VOID/DCAT declara en la línea 66, **detrás de 6 KB** de prefijos y literales largos → una ventana de «encabezado» da ausencia falsa | `jp-cos/dataset-20250927.ttl` | `test_D3_depth` |

⚠️ **D1 quedó publicado en una corrida y se conserva fechado como control negativo**:
`result-semantic-predicatebug.2026-10-03.tsv` difiere del autoritativo en **exactamente 1 de 25
filas**, la que lleva el predicado serializado como URI.

## Reservas declaradas, no tapadas

- ⚠️ **La lista de rutas de payload es por CONVENCIÓN, no por listado**: `raw` no lista
  directorios, así que una cesión en un archivo de nombre no convencional se lee como silencio.
  Las 22 `PAYLOAD-SILENT` son *«silencio en los nombres probados»*, no *«silencio probado»*.
- ⚠️ **`codeload.github.com` da 403 por el proxy de esta corrida** (medido), así que no se pudo
  bajar el árbol completo de cada repo y grepearlo entero, que es el instrumento que cerraría
  la reserva anterior. **Canal declarado, no supuesto.**
- ⚠️ Las **249 filas de `agents/top.md` sin URL de GitHub** siguen fuera del denominador.
- 🟢 **Las 23 filas `sin-licencia` del pase 51 están CONTENIDAS en estas 29** (`comm -23` da
  vacío), así que la relectura que la acción pedía quedó hecha en el mismo barrido: **5 de las 23
  declaran en payload → aquella cifra estaba inflada un 22 %.**
- ⚠️ Las 3 filas `indeterminado` del pase 51 que no están en las 29 —`1EdTech/caliper-php`,
  `IMSGlobal/caliper-python`, `concentricsky/badgr-server`— dan **`UNREACHABLE`** por este canal,
  consistente con las lápidas que el pase 64 describió. **Sin afirmación de licencia sobre ellas.**

## Correr

```sh
./sweep_payload.sh <org/repo>                              # manifiesto, citación, header, semántico
xargs -P 6 -n 1 ./sweep_payload.sh < slugs.input.txt       # las 29
./sweep_semantic.sh <org/repo> <archivo.ttl|.owl> [bytes]  # la capa de dato, con D1/D2/D3 corregidos
python3 test_extract.py                                    # los 8 controles
```

## Archivos

- `sweep_payload.sh` — manifiestos, `CITATION.cff`, encabezados de fuente, datos semánticos
- `sweep_semantic.sh` — la capa RDF/OWL, delega la extracción al módulo con controles
- `extract_license.py` · `test_extract.py` — el extractor y **un control por defecto** (D1/D2/D3)
- `result.2026-10-03.tsv` — las 29 filas (**autoritativo**)
- `result-semantic.2026-10-03.tsv` — las 25 serializaciones alemanas (**autoritativo**)
- `result-semantic-predicatebug.2026-10-03.tsv` — **control negativo fechado** de D1
- `result-semantic-jpcos.2026-10-03.tsv` — Japón, los 4 archivos de vocabulario y dataset
- `slugs.input.txt` — el denominador: las 29 de las 32 del pase 64 que no son `FWU-DE`
