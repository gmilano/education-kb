# `P637` — compuerta de acuerdo entre instrumentos

**Pase 53, 2026-10-08.** `9/9` verdes, offline, corrida desde este directorio.

## Qué mide

Esta KB tiene **tres** implementaciones de la pregunta *"¿qué familia de licencia es este
payload?"*. Hasta el pase 53 nadie las había corrido **una contra otra**: cada una pasaba sus
propias fixtures, y por eso `Gap 256` sobrevivió **tres pases** declarado.

Medido sobre `openeducat/openeducat_erp` (`master/LICENSE`, 8 241 B), la única plataforma LGPL
del estante de `verticals/solutions.md`, cuyo texto dice *"GNU LESSER GENERAL PUBLIC LICENSE,
**Version 3 (LGPLv3)**"*:

| Instrumento | Antes del pase 53 | Después |
|---|---|---|
| `lib/license_family.sh::osi_family_of` (**el compartido**) | 🔴 `LGPL` | 🟢 `LGPL-3.0` |
| `p419-copyleft-identity::familia` | 🟢 `LGPL-3.0` *(desde el pase 123)* | 🟢 `LGPL-3.0` |
| `licence-grant-gate/grant_gate.py::family_of` | 🟡 `LGPL` | 🟡 `LGPL` **(grueso por contrato)** |
| **el estante, leído de primera mano** | 🟢 `LGPL-3.0` | 🟢 `LGPL-3.0` |

🔴 **La mayoría decía `LGPL` y estaba equivocada.** Por eso esta compuerta **no vota**.

## Las tres clases que distingue

- **`ACUERDO`** — todos coinciden.
- **`DEFECTO`** — dos instrumentos que *pretenden* la misma granularidad y difieren.
- **`CONTRATO`** — uno es deliberadamente más grueso (`grant_gate` contesta
  concesión-vs-mención, donde la versión no es portante). 🟡 **`Gap 259`**: declarado, no alineado.
- **`CONTRADICCION`** — familias distintas, no versiones distintas → `INDECIDIBLE` sin estante.

El desempate es **`respuesta_del_estante`**, la lectura de primera mano. Nunca el conteo.

## Correr

```sh
cd compose/code/p637-cross-instrument-licence-agreement
python3 test_agreement.py          # NUNCA con python3 -I (P621)
```

## Por qué importa fuera de esta KB

`LGPL-2.1` y `LGPL-3.0` difieren en la cláusula de patentes y en la de anti-tivoización, y la
pregunta de **enlace** que un cliente hace sobre `openeducat` se decide exactamente ahí. Un
artefacto de conformidad Anexo III (UE, **2027-12-02**) necesita una línea de licencia por
componente que un auditor pueda re-derivar: esta compuerta muestra que la columna fue derivada
**dos veces de forma independiente** y que coincidieron — o, cuando no, cómo se adjudicó.
