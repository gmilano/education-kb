---
industry: education
region: Global
updated: 2026-10-02
---

# `unitime-mcp-gate` — la puerta MCP de UniTime, con su prueba

**Escrita y verificada en el pase 42 del 2026-10-02.** Implementa el patrón **P92** de `compose/patterns.md`.

## Por qué este directorio existe

🔴 **El pase 40 escribió y probó el *gateway* de allowlist (**P85**) y NO guardó el código.** El pase 42, al ejecutar la
acción 1, tuvo que reconstruirlo. 🔵 **Una pieza «probada» que no está versionada no es un activo de la KB: es un
recuerdo.** Desde este pase, el código que esta base declara probado se guarda acá.

## Qué hay

| Archivo | Qué es |
|---|---|
| `gate.py` | El generador de manifiesto + el *gateway* de allowlist. **Sólo stdlib.** |
| `connectors.tsv` | Los 15 conectores de UniTime leídos del árbol: `clase`, `nombre registrado`, `verbos`. |
| `test_gate.py` | **23 aserciones.** Verifica por ejecución, con un *upstream* que registra cada llamada recibida. |

## Cómo se corre

```
python3 test_gate.py        # 23 aserciones; sale 0 si todas pasan
python3 gate.py             # servidor MCP por stdio (JSON-RPC por línea)
```

**Variables de entorno:** `UNITIME_ALLOW` (lista de tools separada por comas; si no está, se aplica la política por
defecto: negar `script`, exponer sólo lecturas) y `UNITIME_CONNECTORS` (ruta al TSV).

## Qué prueba, y qué NO

🟢 **Prueba:** que `tools/list` se construye **desde la allowlist**; que un tool retenido se responde `-32601`
**sin llegar al upstream** (`0 de 9`); que una *allowlist* vacía expone **0 tools**; y el camino completo por **stdio
real** en un subproceso.

⚠️ **NO prueba:** el mapeo de parámetros de cada conector contra una instancia real de UniTime. **El *upstream* es un
*stub***, igual que en la prueba de P85. **Lo medido es la partición de tools**, que es la parte que decide si la puerta
se puede proponer.

## De dónde salen los datos

`connectors.tsv` se regenera desde un clon de [`UniTime/unitime`](https://github.com/UniTime/unitime) (**Apache-2.0**):

```
for f in JavaSource/org/unitime/timetable/api/connectors/*.java; do
  name=$(awk '/protected String getName\(\)/{f=1} f&&/return "/{gsub(/.*return "|".*/,"");print;exit}' "$f")
  verbs=$(grep -oE 'public (void|boolean) do(Get|Post|Put|Delete)' "$f" | sed 's/.*do//' | sort -u | tr '\n' ' ')
  printf '%s\t%s\t%s\n' "$(basename "$f" .java)" "$name" "$verbs"
done
```

🔴 **Hay que leer el `return` del override de `getName()`, no el primer literal que aparezca después de la palabra
`getName`:** ese atajo devuelve `"name"` para `EventsConnector` y `"log"` para `ScriptConnector` — **dos nombres falsos,
y uno es el del conector que ejecuta scripts del servidor.**
