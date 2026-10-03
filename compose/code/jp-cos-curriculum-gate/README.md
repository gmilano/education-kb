---
industry: education
region: APAC
updated: 2026-10-03
---

# `jp-cos-curriculum-gate` — el currículo japonés, medido (pase 65 del 2026-10-03)

Ejecuta la **acción 3 del pase 65**. El hueco de **JAPÓN** venía declarado **sin medir desde el
pase 61** —cuatro veces— y se cierra buscando **en japonés**, `学習指導要領` (*gakushū shidō
yōryō*), que es el canal que el pase 61 ya había demostrado productivo.

## El resultado: el hueco cierra en la mejor rama, y REFUTA la hipótesis de la acción

La acción escribió: *«si existe y está publicado por MEXT sin licencia explícita, APAC replica el
patrón alemán y **P174** gana una tercera región»*. **Medido: el artefacto existe Y tiene licencia
explícita. P174 NO gana una tercera región por este caso.**

🟢 **`jp-cos/jp-cos.github.io` — 学習指導要領LOD / Japanese Course of Study LOD — `CC BY 4.0`.**

| | |
|---|---|
| Qué es | el currículo nacional japonés completo como **Linked Open Data**, RDF/Turtle + HTML |
| Alcance | *«todos los tipos de escuela, currículos nuevos y viejos»*, jardín → secundaria superior |
| Licencia | **CC BY 4.0** — **medida**, ver abajo |
| Publicador | **教育データプラス研究会** (Education Data Plus Research Group), © 2021-2026 |
| Fuente (出典) | 文部科学省 **MEXT**, «学習指導要領コードのコード表（全体版）» |
| IRI canónico | `https://w3id.org/jp-cos/` |
| Volcados | **22 TTL versionados**, el más reciente `all-20250927.ttl` — ver `dumps.tsv` |
| Vocabulario | `schema-class` + `schema-property`, y **SHACL `shapes-20250817.ttl`** (71 KB) |
| SPARQL | `https://dydra.com/masao/jp-cos/sparql` (試験公開中 — publicación de prueba) |
| Actividad | **39 issues abiertos**, último cambio **2026-09-25**: vivo |
| Software compañero | `ICT-CONNECT-21/CSCode2023` — **MIT**, texto completo (1.081 B), encargo de MEXT |

### La cesión, medida en DOS lugares del repositorio

El archivo `LICENSE` **no existe** (14 nombres × ref `HEAD` → 404), y por eso el instrumento de
la capa de archivo clasifica este repo como `UNLICENSED`. **La cesión está en el repo, dos veces:**

**1. En el HTML publicado** (`index.html`, en la rama por omisión):

```html
<p class="license">
  <a href="https://creativecommons.org/licenses/by/4.0/"><img src="…/by/4.0/88x31.png"></a>
  このデータセットは<a href="https://creativecommons.org/licenses/by/4.0/">クリエイティブ・コモンズ
  ライセンス 表示 4.0</a>として自由に利用できます。
</p>
```

**2. En el PAYLOAD RDF** (`dataset-20250927.ttl`, descripción VOID/DCAT, línea 66):

```turtle
dct:license [ rdf:value <https://creativecommons.org/licenses/by/4.0/> ;
              rdfs:label "Creative Commons license Attribution 4.0"@en ] ;
```

🔴 **Las DOS ubicaciones eran invisibles a los instrumentos de esta KB antes de este pase**: la
primera porque `index.html` no es un nombre de licencia ni de payload convencional; la segunda por
**D2** (nodo en blanco) y **D3** (profundidad) — ver `../p172-payload-license-sweep/`.

## Por qué Japón es ahora la mejor pieza de currículo de la KB

🔵 **`CC BY 4.0` es más permisiva que la alemana `CC BY-SA 4.0`**: sin ShareAlike, **no activa la
compuerta de P178**, así que un currículo derivado puede entregarse con licencia propia. Y viene
con **volcados versionados, vocabulario, SHACL y endpoint SPARQL** — nada que construir.

| Región | Pieza de currículo | Licencia | ShareAlike |
|---|---|---|---|
| **APAC — Japón** | `jp-cos` 学習指導要領LOD | **CC BY 4.0** | 🟢 no |
| APAC — Corea | (pieza MIT registrada en pases previos) | MIT | 🟢 no |
| **EMEA — Alemania** | `dini-ag-kim/school-curriculum-pg` (16 Länder) | **CC BY-SA 4.0** | 🔴 sí |
| EMEA — Alemania | `dini-ag-kim/schulfaecher` (materias) | CC0 1.0 | 🟢 no |
| LATAM — Chile | `curriculumnacional.cl` — sin artefacto, sólo PDF/HTML | ⚠️ sin leer | — |
| NA — Common Core | 3 renderizaciones JSON | 🔴 sin licencia | — |

## Canales declarados, no supuestos

- 🔴 **`www.mext.go.jp` BLOQUEADO por dos canales independientes** (`curl` → `connect_rejected`;
  WebFetch → `EGRESS_BLOCKED`), **igual que los seis dominios alemanes del pase 64.** Así que los
  términos de MEXT **no se leyeron de primera mano**. Por canal secundario: el sitio de MEXT
  declara **公共データ利用規約（第1.0版）** —libre reproducción, transmisión pública, traducción y
  adaptación—. ⚠️ **Esto queda «corroborado por canal secundario», NO medido**, con el mismo
  rótulo que el pase 64 aplicó a FWU.
- 🔴 **`jp-cos.github.io` (el sitio Pages) y `w3id.org` BLOQUEADOS** → `connect_rejected`.
  🟢 **La vuelta que SÍ funciona, y es reusable:** un sitio Pages se sirve DESDE un repo, y
  `raw.githubusercontent.com` está abierto, así que `index.html` y `about.html` se leyeron por
  `raw`. **La página bloqueada se leyó igual, por su fuente.**
- 🔴 **`zenodo.org` BLOQUEADO por dos canales** → el registro DOI (badge `392285422`) no se pudo
  leer. **Para un dataset de investigación el depósito DOI es un lugar canónico de licencia**, así
  que esta reserva queda abierta con el canal nombrado.
- 🔴 **`dydra.com` (el endpoint SPARQL) BLOQUEADO** → **no se verificó que responda.** El endpoint
  se cita como *declarado por el publicador*, no como probado, y además él mismo se anuncia
  試験公開中 (*publicación de prueba*): **una receta no debe depender de él sin verificarlo.**
- ⚠️ **Se midió un único registro de ítem** (`710/0000000000000.ttl`, leído entero, 1.102 B:
  Kindergarten/2008 第1章 総則, con `qb:order`, `schema:hasPart`, `cs:school`). **No se recorrieron
  los 104 directorios de código**, así que la riqueza del grafo está medida por muestra.
- 🟢 **Una sola rama** (`main`, por omisión): verificado contra `/branches/all`, así que la ref
  `HEAD` de **P170** cubre este repo entero. **La hipótesis de que la licencia pudiera vivir en una
  rama `gh-pages` quedó REFUTADA**, y eso refuerza P170 en vez de limitarlo.

## Archivos

- `dumps.tsv` — los 22 volcados TTL, con qué trae cada uno y qué se midió por `raw`
- `result-semantic-jpcos.2026-10-03.tsv` — los 4 archivos de vocabulario/dataset barridos

---

# Pase 66 del 2026-10-03 — el GRAFO medido, y la corrección que este pase le hace al 65

Ejecuta la **acción 3 del pase 65**: *«medir el GRAFO japonés, que este pase midió por MUESTRA de un
solo registro»*, con la advertencia que la acción añadía — *«y medir de una vez `all-20250927.ttl`,
que dio 404 en la raíz del repo y es el único volcado que el publicador enumera y este pase no pudo
alcanzar: si no está en el repo, el grafo completo sólo existe detrás de los dominios bloqueados»*.

## 🔴 El grafo completo SÍ está en el repo. El 404 era un nombre mal transcrito

**`index.html` lo enumera como `all-20250927.ttl.gz`, con sufijo `.gz`.** El pase 65 anotó el nombre
en `dumps.tsv` **sin el sufijo** y sondeó un archivo que el publicador nunca anunció.

| Nombre | Código | Bytes |
|---|---|---|
| **`all-20250927.ttl.gz`** — como lo escribe `index.html` | 🟢 **200** | **4.251.289** |
| `all-20250927.ttl` — lo que el pase 65 sondeó | 🔴 404 | 14 (el cuerpo es la cadena `404: Not Found`) |
| **`cs-items-20220830.ttl.gz`** | 🟢 **200** | **2.522.650** |
| `cs-items-20220830.ttl` — ídem | 🔴 404 | 14 |

⚠️ **Los DOS nombres mal transcritos son los dos archivos más grandes del conjunto, que es
exactamente el motivo por el que están comprimidos.** 🔵 **La lección de método: un nombre
transcrito de un listado no es el nombre que el listado dio.** El 404 era real y la conclusión que se
sacó de él —*«el grafo completo sólo existe detrás de los dominios bloqueados»*— era falsa. Y el
pase 65 **tenía el listado delante**: es el mismo `index.html` que leyó por `raw` para establecer
**P181**. 🔴 **El canal correcto se usó y el dato se copió mal; ningún canal nuevo hacía falta.**

🟢 **Medidos los 22 volcados exactamente como `index.html` los escribe: 22 de 22 dan 200.** La
reserva «no medido» de `dumps.tsv` queda cerrada completa — ver `dumps.2026-10-03.tsv`, generado por
`measure_dumps.sh`, que pide **cada nombre tal cual** y además el nombre sin `.gz` para que la
corrección se vea en vez de suponerse.

| Magnitud | Valor |
|---|---|
| volcados enumerados por `index.html` | **22** (20 `.ttl` + 2 `.ttl.gz`) |
| alcanzables por `raw` | 🟢 **22 de 22** |
| el grafo completo, comprimido | **4.251.289 B** |
| el grafo completo, sin comprimir | **69.288.422 B** (66 MB), **1.004.927 líneas** |
| el volcado plano más grande | `section-hierarchy-20240704.ttl`, **13.689.658 B** |

## La hipótesis de la acción se resuelve en su PRIMERA rama: P180 se puede cotizar con alcance cerrado

La acción escribió: *«si los volcados cubren todos los niveles escolares y el comentario oficial
(学習指導要領解説), la receta **P180** se puede cotizar con alcance cerrado; si cubren sólo parte, la
estimación de 6-8 semanas está mal y hay que publicar qué falta.»*

🟢 **Medido sobre el grafo entero: cubre todos los niveles Y el comentario oficial.**

| Clase | n | Qué es |
|---|---|---|
| **`cs:Item`** | **39.958** | 🔵 **los ítems del currículo — el dato que un tutor necesita** |
| `cs:Subject` | **786** | materias |
| `cs:SubjectArea` | **276** | áreas de materia |
| **`cs:CommentaryItem`** | **655** | 🟢 **学習指導要領解説, el comentario OFICIAL, dentro del grafo** |
| `cs:CosCommentary` | 2 | los dos cuerpos de comentario |
| `cs:CourseOfStudyRevision` | **34** | 🔵 **revisiones: los currículos viejos Y los nuevos, como el publicador declara** |
| `cs:CourseOfStudy` | 20 | currículos |
| `cs:RelatedSubject` + `cs:RelatedSubjectArea` | **158 + 102** | 🟢 **enlaces entre materias — lo que permite recorrer prerrequisitos** |
| `sh:NodeShape` | **17** | 🟢 **el SHACL de validación viaja DENTRO del mismo grafo** |
| `cs:School` · `cs:Stage` · `cs:Period` | 9 · 7 · 9 | tipos de escuela, etapas, vigencias |
| **`cs:DisabilityCategory`** | **5** | categorías de discapacidad |
| `cs:Number` (literales tipados) | 46.277 | |

Ver `graph-classes.2026-10-03.tsv` para el inventario completo.

### 🟢 La cobertura por nivel, y el diferenciador que nadie había visto: educación especial

| Nivel (segmento de IRI) | Apariciones |
|---|---|
| 幼稚園 **Kindergarten** | **1.382** |
| 小学校 **Elementary** | **23.555** |
| 中学校 **LowerSecondary** | **17.468** |
| 高等学校 **UpperSecondary** | **79.926** |

🔵 **Y una rama entera que la muestra de un registro no podía mostrar: 特別支援学校 (SNES, educación
especial) está modelada como ciudadana de primera clase, desglosada por categoría de discapacidad.**

| Rama SNES | Apariciones |
|---|---|
| `UpperSecondaryDeptSNES` | **14.560** |
| `ElementaryAndLowerSecondaryDeptSNES` | **6.130** |
| `UpperSecondaryDeptSNES-Visual` (視覚) | **4.886** |
| `UpperSecondaryDeptSNES-Hearing` (聴覚) | **4.721** |
| `UpperSecondaryDeptSNES-Intellectual` (知的) | **2.207** |
| `LowerSecondaryDeptSNES-Intellectual` | **1.546** |
| `ElementaryDeptSNES-Intellectual` | **1.223** |
| `KindergartenDeptSNES` | **515** |
| `UpperSecondaryDeptSNES-VHPH` · `ElementaryDeptSNES-VHPH` | **157 · 76** |
| variantes `-NC` (教育課程なし / sin currículo prescrito) | **432 + 372 + 341** |

⚠️ **Esto cambia el valor de la pieza, no sólo su tamaño.** El currículo nacional japonés en LOD
**viene con el currículo de educación especial desglosado por discapacidad**, bajo **`CC BY 4.0` sin
ShareAlike**. Ninguna otra pieza de currículo de esta KB —tampoco la alemana por *Land*, que es
`CC BY-SA 4.0`— trae esa dimensión. Ver `graph-coverage.2026-10-03.tsv`.

🔵 **Consecuencia para P180: la estimación se sostiene y el alcance se cierra.** No hay que construir
vocabulario, ni validación, ni el comentario: los tres vienen en el artefacto. ⚠️ **Y la dependencia
que la receta TIENE que declarar sigue siendo el endpoint SPARQL**, no el grafo: `dydra.com` está
bloqueado en esta corrida y el publicador lo anuncia 試験公開中. **Con el grafo de 66 MB en la mano,
la receta no necesita el endpoint** — se carga en un *triplestore* propio, y eso es lo que hay que
cotizar.

## Archivos del pase 66

- `measure_dumps.sh` — pide **cada nombre tal cual lo escribe `index.html`**, más el nombre sin `.gz`
- `dumps.2026-10-03.tsv` — los 22 volcados, los 22 con código y bytes (**autoritativo**; `dumps.tsv`
  queda como el estado del pase 65, con sus dos nombres mal transcritos a la vista)
- `graph-classes.2026-10-03.tsv` — el inventario de clases del grafo completo
- `graph-coverage.2026-10-03.tsv` — la cobertura por nivel escolar y por rama SNES
