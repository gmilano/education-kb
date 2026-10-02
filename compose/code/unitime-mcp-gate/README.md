---
industry: education
region: Global
updated: 2026-10-02
---

# `unitime-mcp-gate` — la puerta MCP de UniTime, con su prueba

**Escrita en el pase 42 del 2026-10-02. Re-auditada en el pase 45** con los cuatro controles que el pase 44 tuvo que
inventar para la puerta de SEB Server (**gap 93, CERRADO**). Implementa el patrón **P92** de `compose/patterns.md`.

## Por qué este directorio existe

🔴 **El pase 40 escribió y probó el *gateway* de allowlist (**P85**) y NO guardó el código.** El pase 42, al ejecutar la
acción 1, tuvo que reconstruirlo. 🔵 **Una pieza «probada» que no está versionada no es un activo de la KB: es un
recuerdo.** Desde este pase, el código que esta base declara probado se guarda acá.

## 🔴 Qué encontró la re-auditoría del pase 45, y por qué importa

El defecto del pase 44 **no era del upstream: era del extractor**, y esta puerta se había construido con el mismo método
antes de que existieran los controles. Corridos los cuatro sobre UniTime:

| Control | UniTime | Qué pasó |
|---|---|---|
| **(a)** ninguna ruta contiene `${` | 🟢 **PASA, 15/15** | las rutas son literales de `@Service("/api/x")`. El defecto que invalidó las 30 rutas de SEB Server **no se reproduce acá** |
| **(b)** toda ruta empieza con `/` | 🔴 **FALLABA como dato** | `connectors.tsv` **no tenía columna de ruta**: llevaba `getName()`, y `gate.py` pegaba `"/api/"` en una f-string de Python. La ruta estaba **inferida dos veces y leída cero** |
| **(c)** ninguna fila viene de una declaración de clase | 🟢 **PASA** | el extractor casa `public void do<Verb>(ApiHelper)`; ninguna declaración de clase puede casar. **0 `public boolean do*` en el árbol**, así que esa alternativa del patrón estaba muerta |
| **(d)** toda clase condicionada está excluida | 🟢 **PASA (no hay ninguna)** | **ningún conector lleva `@ConditionalOn*`**. Pero el análogo existe y es *runtime*: ver abajo |

### 🔴 (b) El hallazgo central: `getName()` NO es la ruta

`ApiServlet.getConnector()` hace
`applicationContext.getBean(request.getServletPath() + request.getPathInfo())`. **La ruta es el nombre del bean de
Spring**, o sea el valor de `@Service("/api/rooms")`. `ApiConnector.getName()` **no participa del enrutado**: su único
uso es `getCacheMode()`, que lo pasa a `ApplicationProperty.ApiCacheMode.value(getName())`.

🔵 **Los 15 coinciden hoy** (`@Service` vale exactamente `/api/` + `getName()` en 15 de 15), así que **el dato publicado
era correcto y el método no**. Una puerta construida sobre `getName()` acierta por coincidencia y se rompe en silencio el
día que un conector registre un bean con otro nombre. Desde este pase la ruta es **dato leído**, y `load_connectors()`
**levanta `StaleTable`** si le dan la tabla de 3 columnas del pase 42 en vez de volver a inferir.

### 🔴 (b) Y la ruta absoluta no es la URL desplegada

`getServletPath()` es relativo al contexto del *webapp*. El `<url-pattern>` de `apiServlet` en
`WebContent/WEB-INF/web.xml` es **`/api/*`**, y `pom.xml` envía **`<warName>UniTime</warName>`**, así que la URL real
por omisión es **`/UniTime/api/<conector>`**, no `/api/<conector>`. La puerta ahora publica `<contexto>+ruta` y lleva
`UNITIME_CONTEXT`.

### 🔴 (d) El análogo de `LightController`: una ruta viva que no funciona sin configurar

UniTime no condiciona el *bean*; condiciona el **handler**. `VariableTitleCourseConnector.validateRequest()` lanza
`IllegalArgumentException` si `VariableTitleConfigName`, `VariableTitleDefaultLimit` o `VariableTitleInstructionalType`
no están seteadas, **y lo llaman `doGet` y `doPost` las dos**. 🔵 **Por eso la columna `guarded` marca la LECTURA
también:** `GET /UniTime/api/var-title-crs` devuelve **400 en un despliegue por omisión**. Marcar no es ocultar — el
tool sigue expuesto, con la condición a la vista.

### 🔴 (e) El control que SÓLO necesita UniTime: el verbo no es la frontera de escritura

Ésta es la quinta clase de defecto y es de la **abstracción de la puerta**, no del extractor. `ScriptConnector.doGet`
despacha por parámetro de query, y dos de sus ramas escriben:

- `?script=…` → **llama `doPost(helper)`**, o sea **un GET ejecuta un script del servidor**;
- `?delete=…` → `getQueueProcessor().remove(…)`, o sea **un GET borra un ítem de la cola**.

🔵 **La partición lectura/escritura por verbo —que es el corazón de las dos puertas de esta KB— no es sólida para
UniTime.** La política por defecto ya negaba `script` **por nombre**, así que el resultado era correcto; el motivo
documentado no lo era. Desde este pase `hard_deny()` es un **piso, no una política**: `unitime.script.get` se niega con
`-32601` **incluso si un operador lo nombra en `UNITIME_ALLOW`**, y la decisión se registra como `floor` y no como
`withheld`.

⚠️ **Barrido completo, para no dejarlo como impresión:** se revisaron los 15 `doGet` buscando mutaciones. El único
cruce real es `ScriptConnector`. `EventsConnector:170` casa el patrón y **es un falso positivo**: es `Iterator.remove()`
sobre una lista en memoria, no estado persistido.

## Qué hay

| Archivo | Qué es |
|---|---|
| `extract_surface.py` | **Nuevo en el pase 45.** Regenera `connectors.tsv` contra un *checkout*: lee el bean de `@Service`, el `<url-pattern>` de `web.xml`, el `<warName>` de `pom.xml`, los *overrides* de verbo, los cruces de verbo y los guardas por propiedad. **Sólo stdlib.** |
| `gate.py` | El generador de manifiesto + el *gateway* de allowlist, con el piso `hard_deny()`. **Sólo stdlib.** |
| `connectors.tsv` | Los 15 conectores leídos del árbol: `clase`, **`ruta`**, `nombre`, `verbos`, `crossing`, `guarded`. |
| `test_gate.py` | **46 aserciones** (eran 23). Los cuatro controles del pase 44 + el quinto + la prueba de partición del pase 42, verificada por ejecución con un *upstream* que registra cada llamada. |

## Las cifras, medidas

| Magnitud | Pase 42 | Pase 45 | Nota |
|---|---|---|---|
| Conectores con bean `@Service("/api/…")` | 15 | **15** | barrido sobre `JavaSource` entero: **no hay un 16.º** |
| Tools en el manifiesto (conector × verbo implementado) | 26 | **26** | 14 lecturas + 12 escrituras |
| **Rutas HTTP vivas** | — | **60** | 15 × 4. Las **34** sin *override* **no dan 404: `ApiConnector` responde 501 NOT_IMPLEMENTED** |
| Rutas base **literales** | no medido | **15 de 15** | lo contrario de SEB Server, donde eran **0 de 30** |
| Tools expuestos por la política por omisión | 13 | **13** | 14 lecturas − `script.get` |
| Piso (`hard_deny`) | — | **1** | `unitime.script.get` |
| Verbos guardados por propiedad | — | **2** | `var-title-crs` `Get` y `Post` |
| Aserciones en verde | 23 | **46** | |

## Cómo se corre

```
python3 test_gate.py        # 46 aserciones; sale 0 si todas pasan
python3 gate.py             # servidor MCP por stdio (JSON-RPC por línea)
```

**Variables de entorno:** `UNITIME_ALLOW` (lista de tools separada por comas; si no está, se aplica la política por
defecto: negar `script`, exponer sólo lecturas — y el **piso** se aplica siempre), `UNITIME_CONNECTORS` (ruta al TSV) y
`UNITIME_CONTEXT` (contexto del *webapp*, por omisión `/UniTime`).

## De dónde salen los datos

`connectors.tsv` se **regenera**, no se transcribe, desde un clon de
[`UniTime/unitime`](https://github.com/UniTime/unitime) (**Apache-2.0**, `HEAD` `aeb4431` del **2026-10-02**, Tomáš
Müller — el árbol es de hoy, así que la medición es sobre código vivo):

```
git clone --depth 1 --filter=blob:none --sparse https://github.com/UniTime/unitime ut
cd ut && git sparse-checkout set JavaSource WebContent/WEB-INF
python3 extract_surface.py ./ut
```

🔴 **Las dos trampas de lectura, anotadas para que no se repitan:**

1. **No leer `getName()` como ruta** — es la clave de *cache mode*. La ruta es el bean de `@Service`.
2. **No tomar el primer literal que aparece después de la palabra `getName`:** ese atajo devuelve `"name"` para
   `EventsConnector` y `"log"` para `ScriptConnector` — **dos nombres falsos, y uno es el del conector que ejecuta
   scripts del servidor.** (Trampa registrada en el pase 42; sigue vigente.)

## Qué prueba, y qué NO

🟢 **Prueba:** que `tools/list` se construye **desde la allowlist**; que un tool retenido se responde `-32601`
**sin llegar al upstream**; que una *allowlist* vacía expone **0 tools**; que el **piso** resiste una allowlist
explícita; que una tabla de 3 columnas **se rechaza** en vez de inferir; y el camino completo por **stdio real** en un
subproceso.

⚠️ **NO prueba:** el mapeo de parámetros de cada conector contra una instancia real de UniTime. **El *upstream* es un
*stub***, igual que en la prueba de P85. **Lo medido es la partición de tools**, que es la parte que decide si la puerta
se puede proponer.
