---
industry: education
region: Global
updated: 2026-10-05
---

# `p385-binding-interval` — un conteo cosechado de PROSA es un intervalo, no un número

**Pase 118 del 2026-10-05.** Nace de correr la acción B pre-registrada por el pase 117
(«deduplicar por el par (`sha256`, titular) todas las filas que ya traen `sha256`») y descubrir que
**el primer resultado estaba mal por una razón que importa más que el resultado.**

## Qué mide

El mismo estante, con dos extractores:

| Extractor | Fingerprints | Racimos (≥2 repos) | Dirección del sesgo |
|---|---|---|---|
| **Anclado a URL** (`github.com/owner/repo` en la línea) | 54 | **3** | 🔴 **SUBCUENTA** → es un **PISO** |
| **Permisivo** (además `` `owner/repo` `` y handles pelados) | 54 | **22** | 🔴 **SOBRECUENTA** → es un **TECHO** |
| 🔬 **Vetado a mano, fila por fila** | 54 | 🟢 **4** | — |

## El hallazgo

🔴 **El extractor anclado a URL se pierde el racimo MÁS GRANDE de esta base.** La familia de forks
de `vishalsachdev/canvas-mcp` comparte `sha256:5385a26e2face987` (MIT, 1.071 B, titular
`Copyright (c) 2025 Vishal Sachdev`) entre **8 miembros** — pero esas filas los nombran como
**handles pelados** (`` `sirdanielm` ``, `` `fdis111` ``, `` `BartMassey-upstream` ``,
`` `abr-Projects` ``, `` `lindsay-cheng` ``, `` `AmirF194` ``), **no** como URLs. Un extractor
anclado a URL las cuenta como **cero**.

🔴 **Y el permisivo falla al revés: liga todo repo nombrado en la MISMA LÍNEA.** En
`de8107bf9312` metió `VedShh/Tutor-AI` y `pupilfirst/pupilfirst`, que sólo comparten el párrafo
resumen del pase 117 — no el archivo de licencia.

**Regla de una línea:** un binding `fingerprint → repo` leído de prosa está acotado por la
**convención de escritura** por un lado y por la **co-ocurrencia de línea** por el otro. Las dos
puntas son sesgo, en direcciones opuestas. **El número honesto es el par (piso, techo); un conteo
publicado como número único esconde cuál de los dos sesgos lo produjo.**

## Consecuencia práctica

Un deduplicador construido sobre el extractor anclado **no deduplicaría justo la familia de 8 que
más lo necesita.** ⇒ El binding tiene que leerse de un **campo estructurado (celda de tabla)**, no
de una línea.

## Uso

```
python3 binding_interval.py agents/top.md repos/foundations.md ...   # TSV con el intervalo
python3 test_binding_interval.py                                     # 9/9
```

## Estado

🟢 **Implementado y corrido sobre los 8 archivos este pase: intervalo `[3, 22]`, veredicto
DIVERGEN por 19.** Suite de 9 casos, cada uno nombrando el sesgo que demuestra (incluido el control
de que los dos extractores **convergen** cuando la convención es uniforme).
