---
industry: education
region: Global
updated: 2026-10-03
---

# `p190-holder-package-layer` — el TITULAR en la capa que el cliente instala (acción 2 del pase 67, pase 68 del 2026-10-03)

Ejecuta la **acción 2 del pase 67** —*«el barrido de TITULAR (**P184**) con el denominador
ampliado»*—, que venía **debida por tercera vez**: los pases 66 y 67 no la pudieron correr porque
exige código de este repositorio y el entorno lo negaba (`[Code from External]`). 🟢 **Este pase sí
pudo: `sweep_holder.sh` corrió, y lo primero que hizo fue REPRODUCIR la cifra del pase 66.**

## Lo primero: la cifra del pase 66 queda VERIFICADA, no corregida

🟢 **Re-corrido `sweep_holder.sh` de cero sobre las 160 filas `LICENSED` de `p170`, la salida es
idéntica a la guardada: 68 `HOLDER-MATCH` · 31 `HOLDER-UNRELATED` · 61 `NOT-APPLICABLE`.** Ningún
*slug* cambió de veredicto, ninguno desapareció y ninguno entró (`comm -23` y `comm -13` dan vacío).
⚠️ **La acción advertía *«no publicar un reparto que se lea como el del pase 66 (68/31/61)»* por si la
cifra estaba inflada. No lo estaba: 68/31/61 es reproducible dos pases después.**

### 🔴 Un defecto de MEDICIÓN propio, declarado porque es barato de repetir

🔴 **La primera lectura de esta corrida publicó 66/30/60 sobre 156 filas, y era un artefacto de mi
instrumento de lectura, no del barrido.** `sweep_holder.sh` escribe desde **6 trabajos en paralelo**;
leí el archivo en la misma cadena de comandos y conté **156 de 160 líneas**, porque las últimas
escrituras todavía no habían llegado al disco. 🔵 **La regla que deja: la salida de un barrido
paralelo se cuenta en una invocación SEPARADA de la que lo lanza, y el conteo se valida contra el
número de entradas antes de publicarse.** ⚠️ **Si esa lectura se hubiera publicado, esta KB habría
«corregido» una cifra correcta.**

## La ampliación del denominador: la capa de PAQUETE

**P184** leyó el titular de los 160 archivos que **P170** midió **en un árbol de GitHub**. 🔴 **Las
filas que esta KB cita por REGISTRO no estaban en ese denominador, y son la capa que el cliente
INSTALA.** Este instrumento no reimplementa ninguna de las dos mitades (**regla 1 de P126**): compone
el alcance probado por `p183-nongithub-denominator` con el extractor de `p184-holder-mismatch`,
importado **sin modificar**.

**Denominador declarado antes de empezar: las 17 filas `TARBALL-TEXT` de
`p183/result.2026-10-03.tsv`** —las únicas con texto de licencia DENTRO del artefacto, que es lo único
que un área legal puede leer—. ⚠️ **n = 17. Es una muestra chica y el reparto se publica como
tal: la dirección es clara, la magnitud no está establecida.**

### La adaptación, y no es cosmética

🔵 **`extract_holder.py` clasifica un titular contra un *slug* `owner/repo`. Un paquete no tiene
*slug*.** Su identidad es el **repositorio DECLARADO** cuando declara uno, y si no, el *maintainer*
(npm) o el *author* (PyPI). El instrumento pasa lo que haya y **emite contra QUÉ comparó**
(`DECLARED-REPO` · `MAINTAINER` · `AUTHOR`), porque un `HOLDER-MATCH` contra un *handle* de
*maintainer* es una afirmación más débil que uno contra un repositorio declarado, y la salida tiene
que decir cuál está haciendo.

### El reparto, con el de P184 al lado

| Veredicto | Capa ÁRBOL (**P184**, n=160) | Capa PAQUETE (**P190**, n=17) |
|---|---|---|
| `HOLDER-MATCH` | **68** (42,5 %) | **6** (35,3 %) |
| `HOLDER-UNRELATED` | **31** (19,4 %) | 🔴 **6** (35,3 %) |
| `NOT-APPLICABLE` | **61** (38,1 %) | **4** (23,5 %) |
| `NO-HOLDER` | **0** | 🔴 **1** (5,9 %) |

🔴 **`HOLDER-UNRELATED` casi DUPLICA su proporción en la capa donde el cliente instala** (19,4 % →
35,3 %), **y la clase `NO-HOLDER` —que en 160 archivos de árbol no apareció nunca— aparece acá.**
⚠️ **Con n=17 esto no establece una tasa; establece que la capa de paquete no es mejor que la de
árbol, y que el supuesto de que lo publicado en un registro está más prolijo no se sostiene.**

## D8 — la línea de copyright SIN RELLENAR

🔴 **`opencode-sit` embarca `MIT License` con `Copyright (c) 2026` y NINGÚN NOMBRE.** El camino
permisivo de `extract_holder.py` tomó entonces la línea siguiente —*«Permission is hereby granted,
free of charge, to any person obtaining a copy»*— **como titular.**

🔵 **Es exactamente el fallo **D6** que **P184** ya había aprendido, en una familia que su filtro no
cubre:** D6 estableció que un texto de licencia son kilobytes de prosa **SOBRE** el copyright, así que
cualquier línea del cuerpo puede hacerse pasar por titular. 🟢 **Y **P184** ya tiene la clase correcta
para esto —`NO-HOLDER`, escrita para el apéndice de Apache sin rellenar—, así que la corrección es una
RECLASIFICACIÓN a una clase existente, no un veredicto nuevo.**

**La guarda:** una línea de copyright cuyo resto después del año está vacío significa que la cesión
**no nombra a nadie**. Cubierta por `test_pkg_holder.py` (**7 casos, los 7 corriendo y pasando**),
incluidos los dos que NO deben disparar: el titular de tercero del caso `tldraw` de **P184** y el
*placeholder* del apéndice de Apache, que es otra clase.

🟢 **Control negativo fechado al lado, como manda el punto 3 de P126:**
`preguard.NEGATIVE-CONTROL-2026-10-03.tsv` es la corrida **sin** la guarda. `diff` contra la corrida
con guarda devuelve **exactamente una línea** —`opencode-sit`, `HOLDER-UNRELATED` → `NO-HOLDER`— y
ninguna otra fila se movió. **La guarda es quirúrgica y está demostrado que lo es.**

## Lo que el barrido encontró, caso por caso

| Caso | Qué dice el registro | Qué dice el PAYLOAD | Lectura |
|---|---|---|---|
| 🔴 **`@eduware/oneroster`** (v1.2.11) | npm: **MIT**, *maintainer* `ian-eduware` | **BSD Zero Clause License** (0BSD), 711 B, `Copyright (c) 2025 Bjorn Pagen <…@users.noreply.github.com>` | **CUATRO desajustes en una fila:** familia equivocada en el identificador · titular de un tercero · *maintainer* distinto del titular · 🔴 **y el repo declarado `Eduware-Inc/eduware-oneroster` (también como `homepage`) da 404 en README y LICENSE, probadas 4 variantes.** 🟢 0BSD es más permisiva que MIT, así que el error de familia cae del lado seguro |
| 🔴 **`frappe-mcp-server`** (PyPI) | PyPI: **MIT**, **sin repo y sin author** | `LICENSE` 1.065 B, titular **`muthanii`** | **tres canales, tres respuestas, ninguna de primera parte:** npm dice ISC con repo `appliedrelevance/frappe_mcp_server`, ese repo **no tiene `LICENSE` en la raíz** (404 en 3 nombres), y el artefacto de PyPI cede bajo un titular que no es ninguno de los dos |
| 🔴 **`opencode-sit`** | npm: **MIT** | `Copyright (c) 2026` **sin nombre** | `NO-HOLDER` (D8) |
| 🔴 **`clawed`** (PyPI) | PyPI, repo `SirhanMacx/Claw-ED` | titular **`EDUagent Contributors`** | titular de un **nombre anterior del proyecto** → señal de renombre, no de herencia |
| ⚠️ **`canvas-lms-mcp`** (npm) | repo `bruchris/canvas-lms-mcp` | titular `Christian Bru` | `HOLDER-UNRELATED` por *token*, pero es **casi-coincidencia** (`Bru` ↔ `bruchris`). **P184** ya dice que esta clase es una **lista de lectura**, no un hallazgo: este caso lo confirma |
| ⚠️ **`@yunmiao/studymate`** | repo `Miaotofu01/Study-Mate` | titular `Cattofu` | ídem: comparten el *token* `tofu`, probablemente la misma persona |
| 🟢 **`moodle-cli`** (npm **y** PyPI) | los dos: repo `bunizao/moodle-cli` | los dos: `bunizao`, 1.064 B | **el único de los 5 nombres de doble registro que es UN proyecto en dos canales**, y el titular lo confirma en los dos |

## Reproducir

```bash
cd compose/code/p190-holder-package-layer
python3 test_pkg_holder.py          # 7/7
bash sweep_pkg_holder.sh targets.tsv > out.tsv
diff <(cut -f1,2,5 preguard.NEGATIVE-CONTROL-2026-10-03.tsv) <(cut -f1,2,5 out.tsv)
```

## Lo que este instrumento NO contesta, declarado

⚠️ **No mide las 153 filas que `p183` declaró no medibles por ningún canal** (sin repo y sin
paquete). ⚠️ **No cubre la clase `REG-ID-ONLY`** (identificador en el registro, sin texto en el
artefacto): ahí no hay titular que leer, que es justamente lo que **P179** dice de un identificador.
⚠️ **Y no contesta la pregunta de **P186** —qué archivos de un árbol NO cubre el `LICENSE`—, que sigue
siendo el hueco de instrumento declarado desde el pase 67.**
