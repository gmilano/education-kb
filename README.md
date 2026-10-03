---
industry: education
region: Global
updated: 2026-10-03
---

# 📚 Education KB

> Knowledge base de la industria **Education** para Globant AI Studios.
> Tutores AI, evaluación automática, personalización del aprendizaje, LMS agents

## Estructura

```
education-kb/
├── agents/        # Agentes AI open source de la industria
├── repos/         # Repos MIT/Apache como punto de partida
├── verticals/     # Plataformas verticales customizables con AI
├── intel/         # Mercado, players, tendencias
├── compose/       # Recetas: cómo componer soluciones
├── ingest/        # Scripts de actualización automática
└── compose/code/  # Código ejecutable y probado, no prosa
```

## `compose/code/` — lo que esta KB puede demostrar corriendo

Cada carpeta trae su propio `README.md`, su suite y el comando que la reproduce. **Las cifras de
aserciones se publican con su invocación**, porque varias dan un número distinto según el argumento
o la variable de entorno (regla de **P107**, pase 47):

| Carpeta | Qué prueba | Invocación | Hoy |
|---|---|---|---|
| `aiact-50-2-pack/` | marca un paquete SCORM ya construido, con un portador por dialecto | `python3 test_pack.py` | **27/27** |
| ídem, conformidad real | ídem + `xmllint` contra los XSD de los **dos** dialectos | `SCORM_SCHEMAS=… SCORM_SCHEMAS12=… python3 test_pack.py --with-xmllint` | **37/37** |
| `aiact-50-2-marking/` | mapea los 9 valores de `lineage-skill` a `synthetic` + etiqueta | `python3 test_marking.py` | **23/23** |
| ídem, conformidad real | ídem + el fragmento de manifiesto | `SCORM_SCHEMAS=… python3 test_marking.py --with-xmllint` | **24/24** |
| `aiact-50-2-spans/` | ¿alguna pieza expuesta emite límites de tramo? | `sh scan_spans.sh` | 🔴 **0 de 33** |
| `aiact-50-2-exposure/` | ¿cuántas filas ponen contenido sintético delante de alguien? | `sh scan_marking.sh` | **32 de 66** |
| `patterns-figure-audit/` | inventario de cifras de `patterns.md` y su instrumento | `python3 extract_figures.py --check` | **383** medidas |
| `sebserver-mcp-gate/` | puerta MCP de SEB Server: sólo lecturas, `-32601` al resto | `python3 test_gate.py` | **37/37** |
| `unitime-mcp-gate/` | puerta MCP de UniTime, con `hard_deny()` como piso | `python3 test_gate.py` | **46** ✅ *(reproducida en el pase 55)* |
| `proctoring-reach-audit/` | alcance de red real de los 14 métodos del SPI | `python3 test_reach.py` | **19/19** |
| ídem, con el árbol upstream | ídem + regeneración byte a byte de las tablas | `python3 test_reach.py /ruta/a/seb-server` | **20/20** |
| `openedx-course-generator/` | genera un curso de Open edX sin levantar la plataforma | `python3 test_plan.py` | **33** ✅ *(reproducida en el pase 55)* |
| `seb-proctoring-validator/` | validador que rechaza ajustes de terceros incompletos | `sh run_test.sh` | **21/21** |
| **`registry-license-remeasure/`** | **el ancla de licencia del tarball: encuentra con cualquier capitalización Y sigue rechazando `node_modules`** | `python3 test_anchor.py` | **24/24** |
| `npm-surface-probe/` | licencia y superficie de un paquete MCP desde el *tarball* del registro | `python3 test_probe.py` | **19/19** |
| `mcp-allowlist-gateway/` | puerta MCP con *allowlist*: lo no listado no llega al upstream | `python3 test_gateway.py` | **ALL PASSED** |
| `trend-backlink-audit/` | cada tendencia citada tiene su sección y su evidencia | `python3 test_trends.py` | **22/22** |

🟢 **Pase 55 del 2026-10-03: la columna «Hoy» se re-verificó COMPLETA y las once suites reprodujeron su
cifra publicada.** Las once corren OFFLINE en este entorno.

🔴 **Y la corrección que este pase tiene que hacerse a sí mismo, porque casi publicó lo contrario.** Las
dos suites que **no imprimen total propio** (`unitime-mcp-gate` y `openedx-course-generator`, que sólo
imprimen `ALL CHECKS PASSED`) se re-midieron con un `grep` **escrito a mano en el pase**, que devolvió
**49** y **34** — y estuvo a punto de publicarse como *«dos cifras vencidas»*. ⚠️ **Era un falso
positivo:** el instrumento **versionado** de esta KB (`compose/code/patterns-figure-audit/extract_figures.py`,
que ancla `^PASS `) devuelve **46** y **33**, exactamente lo que esta tabla publica. **El defecto del grep
propio: su segunda alternativa no estaba anclada y con `-i` matcheó `PASS`/`passed` en cualquier parte de
la línea, incluida la línea de resumen.**

🔴 **Lo que invalidó el control, y es la lección de método que deja el pase: el «control positivo» que se
corrió para habilitar el instrumento (37 = 37 en `sebserver-mcp-gate`) era INSENSIBLE al defecto**, porque
esa suite emite líneas `ok` y no `PASS` — **el control no ejercitó el caso donde el instrumento podía
fallar.** 🔵 **Un control positivo que pasa no habilita un instrumento si no ejercita ese caso. Y antes de
escribir un instrumento a mano hay que correr el que este repositorio ya versiona.** Ver **P126** y la
tendencia **313**.

🟢 **Corrección del pase 52 del 2026-10-02: la columna «Hoy» SÍ se re-verificó, y estaba estancada desde el pase 49
por una conclusión demasiado amplia.** Los pases 50 y 51 escribieron que *«el entorno niega la ejecución de código de
este repositorio»* (`[Code from External]`) y dejaron de intentarlo. **Este pase midió la frontera exacta de esa
negativa y es más angosta:**

| Qué se corre | Resultado en este entorno |
|---|---|
| las suites **OFFLINE** (`test_*.py`, `run_test.sh`) | 🟢 **corren todas, y los doce valores de arriba se reprodujeron hoy** |
| un script del repositorio que **sale a la red** (`probe.py`) | 🔴 **NEGADO (`[Code from External]`)** |

🔵 **O sea que la negativa es sobre EJECUTAR CON RED código que vino clonado, no sobre ejecutar el código.** ⚠️ **La
consecuencia de método, que es la que vale: una negativa puntual se midió por su caso más amplio y se publicó como
regla general, y eso costó DOS pases de cifras sin re-verificar** — exactamente el error que **P107** existe para
evitar, cometido sobre el propio instrumento. 🔴 **Lo único que sigue bloqueado es la acción 2** (hacer comparables las
superficies de Canvas, **227** vs **165**), **porque exige `probe.py` con red**, y por eso el permiso que hay que
pedir es **salida de red para ese script**, no permiso de ejecución. Ver **P119** y la tendencia **280**.

⚠️ **Las dos filas «ídem» no son adorno: son el caso que el pase 47 encontró citado sin su
condición.** Una cifra de aserciones sin la invocación que la produce no se puede reproducir, aunque
sea correcta.

## Uso

1. **Nuevo engagement**: leer `intel/market.md` + `repos/foundations.md`
2. **Proponer solución AI**: `agents/top.md` + `compose/patterns.md`
3. **Mantenerse al día**: correr `ingest/update.sh` semanalmente
4. **Verificar antes de citar**: `compose/code/patterns-figure-audit/extract_figures.py --check`
   remide las cifras de `compose/patterns.md` que salen de suites propias. **Una cifra de una suite
   se vence cuando la suite crece**, y el pase 47 encontró dos vencidas

---
*Red de KBs Globant AI Studios → [globant-kb](../globant-kb/)*
