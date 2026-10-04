---
industry: education
region: Global
updated: 2026-10-04
---

# `p268-capability-surface/` — un conteo de capacidades tiene SUPERFICIE, y las superficies del mismo repo se contradicen

**Pase 89 del 2026-10-04.** Esta base cita conteos de herramientas desde el pase 10, y dejó abierta
una comparación —**227 vs 165** de Canvas— esperando salida de red. 🔴 **Este pase midió que esa
comparación no era comparable ni en principio**, porque los dos números pueden venir de superficies
distintas del mismo repositorio.

## Lo medido

**5 lecturas de superficie sobre 3 repos** del cohorte `canvas-mcp`, por WebFetch el **2026-10-04**
(el proxy de egreso devuelve **403** a `curl` y a `api.github.com`, así que la lectura es de la página
del repo):

| Repo | Rol | `DESCRIPTION` | `README-BODY` | Release | Licencia | ★ |
|---|---|---|---|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | UPSTREAM | **102** herramientas / 8 skills | **103** herramientas | v1.13.0 (sep-2026) | MIT | 274 |
| [`harrywang/canvas-mcp`](https://github.com/harrywang/canvas-mcp) | FORK | **80+** / 5 skills | — | v1.12.0 (ago-2026) | MIT | 0 |
| [`jsrodr/canvas-mcp`](https://github.com/jsrodr/canvas-mcp) | FORK | **80+** / 5 skills | **99** herramientas | v1.10.0 (ago-2026) | MIT | 0 |

```
python3 surface.py          # la tabla por repo
python3 surface.py --tsv    # result.2026-10-04.tsv
python3 test_surface.py     # 25/25
```

| Cifra | Qué dice |
|---|---|
| **2** repos donde DOS superficies del MISMO repo se contradicen | el upstream **102 vs 103**; `jsrodr` **80 vs 99** |
| **2** forks cuya `DESCRIPTION` repite un claim que el upstream ya no publica | los dos dicen `80+ / 5` contra `102–103 / 8` |
| **0** repos cuyo conteo es CITABLE sin nombrar la superficie | de los tres medidos, ninguno |

## 🔴 El hallazgo

**El upstream se contradice consigo mismo, el mismo día y en la misma lectura:** su campo
`description` dice *«up to 102 tools and 8 agent skills»* y el cuerpo de su README dice **103**. No es
un fork desactualizado ni una fuente secundaria mal citada: **son dos superficies del repositorio
canónico.**

🔵 **Y el fork no sólo congela el claim viejo: hereda la contradicción y la agranda.** `jsrodr`
publica `80+` en la descripción y **99** en su README — dos números que no coinciden ni entre sí ni
con ninguna superficie del upstream.

🟢 **La regla que sale: un conteo de capacidades se cita con su superficie, o no se cita.** Y la
acción abierta desde el pase 10 (`227` vs `165`) queda **reencuadrada, no desbloqueada**: aunque
llegara el permiso de red, comparar dos números sin saber de qué superficie salió cada uno no produce
una comparación.

## 🔴 `EastArctica/canvas-mcp` da 404 y no se escribe como fila

El canal de búsqueda lo devolvió como repo vivo, con la misma descripción que los demás. **WebFetch
da 404.** No entra a `rows.tsv`: un 404 no es un hallazgo. Las otras dos altas del cohorte
(`harrywang`, `jsrodr`) se verificaron una por una antes de escribirlas.

## 🔵 El tri-estado, que la primera versión no tenía

`harrywang` tiene **una sola** superficie medida. La primera versión de `citable()` lo devolvía
`CITABLE`, como si sus superficies estuvieran de acuerdo. **No lo están: no se midieron.** Ahora el
veredicto es tri-estado y ese caso sale `COTA-DE-INSTRUMENTO` — la misma distinción que **P119** dejó
registrada cuando una negativa puntual se publicó como regla general.

Por lo mismo, `NO-CLAIM` **no es cero**: un conteo ausente no entra a la comparación como un conteo
bajo, porque eso inventaría un conflicto que no se midió.

## Los controles que habilitan el instrumento

Por la regla de **P126** —un control positivo sólo habilita si ejercita el caso donde el instrumento
puede fallar—, `test_surface.py` (**25/25**) trae:

| Control | Qué ejercita | Por qué hace falta |
|---|---|---|
| **NEGATIVO del conflicto** | dos superficies que dicen **lo mismo** → `False` | las dos filas reales conflictúan, así que un instrumento que grite «conflicto» siempre saca 100 % sin este caso |
| **NEGATIVO de la citabilidad** | esas dos de acuerdo → `CITABLE` | el veredicto bueno tiene que ser alcanzable, o el tri-estado es decorativo |
| **del tri-estado** | una sola superficie → `COTA-DE-INSTRUMENTO` | la primera versión lo daba por acuerdo |
| **de `NO-CLAIM`** | ausencia + claim → no conflictúa, y queda `COTA` | que un ausente no se cuente como cero |
| **del slug sin medir** | `no/existe` → `(False, "sin medición")` | que no se afirme nada de lo que no se leyó |

## Archivos

| Archivo | Qué es |
|---|---|
| `rows.tsv` | las 5 lecturas, con fecha e instrumento de lectura en el encabezado |
| `surface.py` | el clasificador: conflicto intra-repo, claim congelado, citabilidad tri-estado |
| `test_surface.py` | **25/25** |
| `result.2026-10-04.tsv` | el veredicto por repo |

**Entorno:** `Python 3.11.15`.
