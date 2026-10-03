# description-drift-audit — el instrumento de P165 (pase 63, 2026-10-03)

**Qué mide.** Dentro de **un mismo repo**, separa dos cifras que la base venía leyendo como una:

- `description_tools` — la cifra de *tools* que anuncia el campo `description` de GitHub;
- `readme_tools` — la que declara el README;
- `drift` — `readme_tools − description_tools`, o **`None` si falta cualquiera de las dos**;
- `searchable` — `False` si el repo **no tiene descripción**, y por lo tanto un barrido por
  búsqueda **no lo encuentra**.

**Por qué existe, y por qué no alcanzaba el instrumento del pase 62.** El pase 62 midió la
divergencia descripción/README en la familia de forks de `vishalsachdev/canvas-mcp` y la explicó
como **herencia**: la `description` se hereda entera y la superficie no (**P160**). Este pase
midió la misma divergencia en repos **ORIGINALES, sin fork de por medio, y aparece igual**. 🔵 **El
fork no es la causa: es una de las maneras en que la `description` se queda vieja. La otra, más
común, es que el autor la escribió una vez y no la volvió a tocar** (**P165**).

🔴 **Y hay una diferencia de diseño que obliga a un archivo aparte:** en `fork-lineage-audit`,
`surface()` toma el **máximo sobre todo el texto capturado**, así que **mezcla los dos ejes en una
sola cifra** — justo lo que hay que separar para medir la deriva. No es un defecto de aquel
instrumento: medía otra cosa.

## La medición del pase 63, con su invocación al lado (P107)

```
python3 audit_drift.py fixtures/*.txt
```

| Repo | ¿fork? | `description` | README | deriva | ¿buscable? |
|---|---|---|---|---|---|
| `AmirF194/canvas-mcp` | 🔴 sí | **80** | **101** | **+21** | sí |
| `lindsay-cheng/canvas-mcp` | 🔴 sí | **102** | **103** | **+1** | sí |
| `xmike04/canvas-student-mcp` | 🟢 **no** | **19** | **29** | **+10** | sí |
| `mtgibbs/canvas-lms-mcp` | 🟢 no | — | — | **None** | sí |
| `peancor/moodle-mcp-server` | 🟢 no | — | — | **None** | 🔴 **NO** |

🔴 **De las cinco filas, las TRES que declaran una cifra en los dos lugares DISCREPAN —ninguna
coincide—, y una de las tres no es un fork.** ⚠️ **Sumando la familia del pase 62
(`abr-Projects/canvas-mcp`: 102 → 139, **+37**) y a la madre (`vishalsachdev`: 102 → 103, **+1**),
el conteo es **5 de 5 discrepan, 0 coinciden**.**

## El control, que es lo que hace que la salida valga (P126)

`test_audit.py` **falla si el instrumento no discrimina**. Hay tres controles y el segundo es el
que justifica el archivo:

| Control | Qué exige | Por qué |
|---|---|---|
| 1 — `peancor` | `description_tools is None` **y** `searchable is False` | Un repo **sin descripción** es invisible a un barrido por búsqueda. **43 ★ y la base lo encontró por repo, no por búsqueda.** |
| 2 — falta una cifra | `drift is None`, **y NO `0`** | 🔴 **Un `0` se lee como «coinciden».** Es la forma de error de **P151**: una salida implausible que entra a un `diff` sin que nadie la mire. |
| 3 — coincidencia real | `drift(42, 42) == 0` | El `0` existe, pero **no es el valor por defecto**. ⚠️ **Es el único control SINTÉTICO del archivo, y se declara: el barrido del pase 63 no encontró ningún repo con las dos cifras iguales.** |

```
python3 test_audit.py     # 14 aserciones
```

**Estado: 14/14 pasan.**

## Lo que este instrumento NO hace

- ⚠️ **No hace red.** Recibe texto ya capturado, igual que el instrumento del pase 62. **La
  captura es WebFetch y sigue siendo el único paso manual** — y es el cuello de botella real: el
  linaje de fork y la descripción **sólo** están en la página HTML.
- ⚠️ **No cuenta las *tools* reales**: lee las **declaradas**. Que el README diga 101 no prueba
  que el servidor registre 101.
- ⚠️ **No reemplaza el conteo por perfil.** Toma el **techo** declarado, que es la cifra que un
  integrador compara, no la que arranca por defecto.
