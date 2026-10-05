---
industry: education
region: Global
updated: 2026-10-05
---

# `P411`/`P412`/`P414` — compuerta de IDENTIDAD de cesión

Artefactos del **pase 123 (2026-10-05, lectura `20:45Z`)**. Decide si un payload de licencia **cede** lo que este estante necesita, leyendo el archivo y no la etiqueta.

## Por qué existe

Tres piezas de alta tracción de este pase habrían entrado a la tabla por un clasificador de palabra clave, y ninguna se puede entregar:

| repo | ★ | lo que el clasificador decía | lo que es |
|---|---|---|---|
| `CaviraOSS/PageLM` | 2.000 ★ | `MIT` | **«PageLM Community License»**: no comercial + **reparto de ingresos** |
| `canyongbs/advisingapp` | 338 ★ | `UNCLASSIFIED` | **Elastic License 2.0**: prohíbe el servicio gestionado |
| `leemonade/leemons` | 292 ★ | `UNCLASSIFIED` | **«Fair code License»**: núcleo no OSI |

## Las tres patologías

- 🆕 **`P411` — la frase de concesión no es la identidad.** `PageLM` abre con la concesión **MIT literal** y sigue con un documento que prohíbe el uso comercial. El delator es el **tamaño**: 8.563 B contra el piso de ~1.070 B de un MIT real.
- 🆕 **`P412` — `UNCLASSIFIED` no es ausencia: es señal.** Las dos únicas filas sin familia reconocible del pase son licencias *source-available* NO-OSI. Se trata como NO-OSI hasta leerla.
- 🆕 **`P414` — hay tres sub-clases bajo el piso de tamaño**, no una: **0 B** (no cede nada, `P404`) · **~3 B** (campo `license` de metadata de paquete) · **~19 B** (**nombra** una licencia sin otorgarla). *Nombrar una licencia no es otorgarla.*

## Cómo decide

Tres señales, **en este orden**. Nunca la frase de concesión sola.

1. **TAMAÑO** — piso de 200 B, con las tres sub-clases de `P414` separadas por nombre.
2. **TÍTULO** — manda sobre cualquier frase del cuerpo: `community license`, `elastic license`, `fair code`, `business source`, `commons clause`, `proprietary`, `all rights reserved`, …
3. **LIMITACIONES** — `non-commercial`, `revenue sharing`, *«hosted or managed service»*, *«prior written consent»*. Una concesión permisiva no las tiene.

Además marca `P403`: si el titular leído es el **placeholder** del apéndice (`<name of author>`, `[name of copyright owner]`), no es un titular.

## Verificación

```
python3 test_gate.py        # 7/7 🟢 — un caso por patologia MEDIDA, no inventada
./barrido_pase123.sh        # los 12 payloads vivos del pase
```

`test_gate.py`: **7/7 🟢** (MIT real, `P411`, Elastic, Fair code, nombramiento de 19 B, metadata de 3 B, 0 B).
`barrido_pase123.sh`: los 3 NO-OSI salen `usable=NO`, los 5 permisivos `usable=SI`.

## ⚠️ `P417` — lo que esta suite aprendió de su propio error

La primera versión del barrido hacía `payload=$(curl …)` y `printf '%s' "$payload"`. **Las dos formas comen los saltos de línea finales**, así que los tamaños salían 1–2 B cortos y los `sha256` equivocados. 🔴 **Y el verificador independiente del mismo pase tenía el mismo idioma, así que coincidía dígito por dígito: dos instrumentos de acuerdo, los dos mal.**

El error se destapó contra una referencia **externa** que estaba en el propio corpus: el digest crudo de `laramint` (`3972dc9744f6`) ya estaba publicado por un pase anterior. **El corpus mide crudo y siempre lo midió.** El barrido ahora baja el payload a archivo temporal (`curl -o`) y lo pasa por `stdin`.

🔵 **Regla que queda:** una cifra es reproducible sólo contra una referencia **fuera** del instrumento que la produjo. Dos verificadores en el mismo lenguaje no son dos canales.
