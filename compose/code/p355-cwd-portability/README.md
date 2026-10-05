---
industry: education
region: Global
updated: 2026-10-05
---

# `P355` — portabilidad de `cwd` del tablero, y la forma del fallo

Artefactos y suite del **pase 112 (2026-10-05)**. Corre la **accion A** pre-registrada por el
pase 111 y reparte su resultado por **causa** y por **forma del fallo**, que es lo que la
prediccion sumo en una sola cifra.

## Que mide

| pregunta | instrumento |
|---|---|
| ¿cuantas suites fallan desde un `cwd` ajeno? | `portability.py` corre cada suite **dos veces**: desde su propio directorio y desde uno ajeno, con la suite referida por ruta absoluta |
| ¿la causa fue una ruta EFIMERA o un `cwd` ASUMIDO? | `ephemeral_refs()` busca `/tmp/`, `$TMPDIR`, `/var/tmp` en el fuente de la suite |
| ¿COMO se ve el fallo? | `shape()` → `CRASH` · `TOTAL-DEGRADADO` · `SILENCIOSO` |

## Invocacion

```sh
python3 portability.py [raiz-del-kb]     # el barrido completo (corre las 69 suites x2)
python3 test_p355.py                     # la suite: 16/16, desde el artefacto versionado
```

`resultado.2026-10-05.tsv` es el barrido del pase 112, versionado para que la suite reproduzca sin
re-correr el tablero.

## El resultado del pase 112

| clausula pre-registrada | pedia | medido | veredicto |
|---|---|---|---|
| suites que fallan o se saltan desde otro `cwd` | **≥3** | 🟢 **4** | **CONFIRMADA** |

🔴 **Y el reparto por causa desarma la cifra que la confirma:**

| causa | suites |
|---|---|
| ruta **EFIMERA** (la clase de `P352`) | 🟢 **0** |
| **`cwd` ASUMIDO** | 🔴 **4** |

| suite | propio | ajeno | forma | que pierde |
|---|---|---|---|---|
| `p183-nongithub-denominator/test_denominator.py` | 15/15 | 🔴 14/15 | `TOTAL-DEGRADADO` | **su control negativo** |
| `p184-holder-mismatch/test_holder.py` | 15/15 | 🔴 11/15 | `TOTAL-DEGRADADO` | 4 fixtures reales |
| `p251-cohort-lineage/test_lineage.py` | 26/26 | 🔴 crash | `CRASH` | `rows.tsv` |
| `sebserver-mcp-gate/test_gate.py` | 37/37 | 🔴 crash | `CRASH` | `operations.tsv` |

🔵 **`P352` queda como ESPECIMEN, no clase:** `p345` nombra `/tmp` y **pasa** desde los dos `cwd`
—el pase 111 lo arreglo con un *skip* declarado—, asi que la clase que motivaba la accion aporta
cero.

🔴 **La severidad va al REVES de la cantidad:** las 4 del `cwd` fallan **ruidosamente** (codigo 1);
la unica de la clase efimera fallaba en **silencio**, publicando «21/21» en verde sin medir nada.

## Los controles negativos, y por que estos

- **Un `CRASH` que ademas imprime un `N/M` no se lee como `TOTAL-DEGRADADO`.** Si `shape()` mirara
  primero el total, el traceback de `p251` —que imprime `26/26` cuando corre bien— caeria en
  `TOTAL-DEGRADADO` y **el reparto 2-2 se volveria 0-4**. El orden de las ramas **es** el hallazgo.
- **`tempfile.mkdtemp()` NO se marca** como ruta efimera: es el **arreglo** de `P352`, no el
  defecto. Un detector que lo marcara reportaria como rota justo la suite que se corrigio.
- **`SILENCIOSO` existe como etiqueta aunque este pase no encontro ninguna**, que es lo que permite
  afirmar el cero en vez de no haberlo buscado.
- **Ninguna suite se cuenta dos veces** (`P126`: el conteo del pase 111 recorrio `lib/` dos veces).

## Una dependencia INVERSA, anotada porque el barrido de suites no la ve

`pattern-citation-audit/audit_patterns.py` —el **instrumento**, no su suite— **falla desde su
propio directorio** (`no existe ./compose/patterns.md`) y solo corre desde la **raiz** del repo.
⚠️ **«`cwd` asumido» no es «asume el suyo»: son dos contratos opuestos conviviendo en el arbol.**
