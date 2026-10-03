---
industry: education
region: Global
updated: 2026-10-03
---

# `read-before-write` de `markingworkflow` — el parche de P152, ESCRITO y NO ENVIADO (pase 60, acción 1 del pase 61 preparada)

**Qué es:** la implementación de referencia del patrón **P152**, más su suite. 🔴 **Deja de ser una
recomendación y pasa a ser código porque el pase 60 midió que el dato se puede leer con el token que la
pieza ya tiene.**

## 🔴 Estado de ejecución, declarado antes que cualquier cifra

| Medición | Valor | Cómo se contó |
|---|---|---|
| Sitios de llamada a `check(` | **20** | `grep`, excluyendo la definición |
| Sitios que **no** corren en una pasada exitosa | **2** | los dos `check(False, …)` dentro de `try` |
| Sitios que corren **más de una vez** | **1** (×3) | el `check` dentro del bucle de `test_falla_cerrado` |
| 🟢 **Asertos que correrían en una pasada exitosa** | **20** | 7 + 6 + 3 + 3 + 1, por función |
| 🔴 Asertos **CORRIDOS** | 🔴 **0** | el entorno negó ejecutar código del árbol clonado |

⚠️ **El primer borrador de este README decía «21 asertos escritos», contando sitios de llamada sin
descontar los dos que no corren ni multiplicar el que corre tres veces. Las dos cifras coinciden en 20
por compensación, no por ser la misma medición** — y por eso la tabla dice **cómo** se contó cada una
(regla de **P107**: una cifra sin su instrumento no se puede re-derivar).

⚠️ **Cuarta reproducción consecutiva de la negativa (pases 58, 59, 60), y este pase aporta el dato que
faltaba para pedir bien el permiso: la razón literal del rechazo es `[Code from External]`.** 🔵 **No es
una negativa de red ni de `python3` —este pase corrió `python3` inline sin problema— es específicamente
*ejecutar código que viene del repositorio clonado*.** 🟢 **Eso vuelve el pedido del pase 61 mucho más
angosto y mucho más fácil de conceder: no hace falta egreso ni un intérprete nuevo, hace falta permiso
para correr las suites OFFLINE de este árbol.**

⚠️ **Y lo que este pase NO hizo, para que no se cite mal: no se intentó correr la suite por otra vía.**
Los 20 asertos de arriba son **escritos**, no resultados.

## El hecho medido que lo habilita

`moodle/moodle` @ `main`, `public/mod/assign/externallib.php` (3.146 líneas, `5.3rc2 (Build: 20261002)`),
leído por `raw.githubusercontent.com` en el pase 60:

| Hecho | Línea |
|---|---|
| `$assignment['markingworkflow'] = $module->markingworkflow;` — **sin condicional** | 464 |
| `'markingworkflow' => new external_value(PARAM_INT, 'enable marking workflow')` — **sin `VALUE_OPTIONAL`** | 584 |
| `require_capability('mod/assign:view', $context);` — único gate de lectura | 401 |
| `require_capability('mod/assign:grade', $context);` — gate de escritura de nota | 1033 |

🟢 **`view` es estrictamente más débil que `grade`: toda puerta que pueda calificar puede leer la
precondición.**

## La decisión que implementa

```
markingworkflow == 1  -> escribir con workflowstate="readyforreview"   (borrador REAL)
markingworkflow == 0  -> REHUSAR, con el motivo             (no existe "borrador" en esa plataforma)
dato ausente/ilegible -> REHUSAR, con el motivo             (fallar cerrado)
```

🔴 **La celda contraintuitiva es la segunda: con `markingworkflow = 0` cualquier escritura PUBLICA, así que
la respuesta correcta es rehusar — NO degradar a otro `workflowstate`.** Degradar es publicar con otro
nombre.

## Archivos

| Archivo | Qué es |
|---|---|
| `read_before_write.py` | la implementación de referencia, sin dependencias y sin red |
| `test_read_before_write.py` | 20 asertos, sin red — **escritos, no corridos** |
| `toshieji.patch` | el mismo cambio expresado contra `server.py` de `toshieji/moodle-grading-mcp` |

## ⚠️ Alcance, y los dos límites que hay que decir con el parche

1. ⚠️ **Medido sobre `main` (5.3rc2), no sobre una LTS desplegada.** Un cliente en 4.x necesita la misma
   lectura sobre su rama (**gap 252**).
2. 🔴 **No vale para Canvas.** Canvas no tiene *marking workflow*; la publicación depende de
   `post_manually` / `posting_policy` del *assignment*, y **ninguna** de las puertas de Canvas medidas lo
   consulta. Es otro parche y otra medición.
3. ⚠️ **El PR a `toshieji/moodle-grading-mcp` NO fue abierto.** El parche queda escrito; enviarlo hacia
   afuera es una acción con efecto externo y requiere autorización explícita.
