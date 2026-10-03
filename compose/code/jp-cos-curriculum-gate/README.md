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
