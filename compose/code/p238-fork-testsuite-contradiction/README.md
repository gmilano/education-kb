# P238 — cuando el FUENTE de un fork es idéntico byte a byte, lo que se bifurcó es el SUITE DE PRUEBAS

**Pase 77 del 2026-10-03.** Instrumento: `check_contract.py` · test: `test_check_contract.py` (**8/8**)
· salida: `result.2026-10-03.txt`.

## Lo que esta base publicaba

El pase 38 clasificó `ashleycribb/learnmcp-xapi` como **«⚠️ NO es sucesión — 2 commits adelante,
ambos de Cloud Run»**, leyendo **los asuntos de los commits**. Sobre esa base, esta KB viene
recomendando `DavidLMS/learnmcp-xapi` como la puerta xAPI canónica desde el pase 6.

## Lo medido

Comparación a nivel de archivo de los dos árboles:

- 🟢 **14 de 14 archivos de FUENTE son idénticos byte a byte** (`config.py`, `main.py`, `mcp/core.py`,
  `mcp/validator.py`, los cinco *plugins*, `verbs.py`, `run_server.py`…).
- 🆕 **Sólo el fork agrega** `Dockerfile`, `.dockerignore`, `docs/GCP_DEPLOYMENT.md`.
- 🔴 **Y difieren CINCO archivos de TEST.** **La configuración de despliegue no toca los tests**, así
  que los tests son el hallazgo.

Los dos suites corren contra fuentes idénticas, así que **como máximo uno describe el código que está
ahí**. Para cada afirmación divergente, ¿existe el símbolo en el fuente compartido?

| Afirmación | El `upstream` afirma | El fork afirma | Qué dice el fuente COMPARTIDO |
|---|---|---|---|
| atributo de cache del token OIDC | `self._oidc_token` | `self._token_cache` | 🔴 **asigna `_token_cache`, nunca `_oidc_token`** |
| *casing* de la ruta de statements | `/xapi/statements/` | `/xAPI/statements/` | 🔴 **`/xAPI/statements/`**, y el código trae el comentario *«note the capital X»* |
| contrato de validación de config | `"LRS_ENDPOINT is required"` | `"LRS_KEY and LRS_SECRET are required"` | 🔴 **la segunda**, con la rama `CONFIG_PATH` *legacy* |

**Afirmaciones que el código compartido sostiene: `upstream` 0/3 · fork 3/3.**

🔴 **O sea: la puerta xAPI que esta KB recomienda desde el pase 6 publica un suite de pruebas que
contradice a su propio fuente, y el fork que el pase 38 descartó es el único árbol
auto-consistente.** El commit del fork que repara los tests **dice «Cloud Run deployment» y no
menciona los tests.**

🔵 **El error del pase 38 fue de CANAL, y es la lección transferible: clasificó una relación de fork
leyendo los ASUNTOS de los commits.** Un asunto de commit es prosa del autor. 🔴 **Un fork cuyo
fuente es idéntico y cuyos tests no lo son no es «sólo empaquetado»: es un árbol que cambió el
contrato de prueba**, y eso se ve únicamente comparando archivos.

## Cota declarada, y es importante

⚠️ **Esto es una prueba ESTÁTICA de contradicción, no una corrida de tests.** Instalar las
dependencias de terceros del suite (`pytest`, `respx`, `httpx`) no está disponible en este entorno,
así que lo medido es *«esta afirmación nombra un símbolo ausente del fuente»*, **no** *«pytest
reporta un fallo»*. Las dos cosas no son lo mismo y acá se afirma la más débil. **Correr los dos
suites queda como acción pre-registrada para un pase con ese presupuesto.**

## El defecto que este instrumento pagó en su propia construcción

🔴 **La primera versión probó la cadena pelada `_oidc_token` y la reportó PRESENTE** en el `ralph.py`
compartido. Lo que está presente es el **método** `_get_oidc_token`, que **contiene** ese nombre; el
test afirma un **acceso a atributo** (`plugin._oidc_token == …`), y ese atributo no existe.
🔵 **Una sonda por subcadena sobre un nombre de atributo pega en el *getter* que lo envuelve, y
convierte una contradicción en un acuerdo** — habría publicado `upstream 1/3` en vez de `0/3`. Las
sondas son regex ancladas en la forma del acceso (`self\.`), y el test de regresión pin­ea el caso.

## ⚠️ Y un segundo defecto, de la misma familia que P237: el test dependía del `cwd`

🔴 **`test_check_contract.py` pasaba 8/8 desde su propio directorio y reportaba 4/8 FAIL desde
`compose/code/` o desde la raíz del repo**, porque invocaba el instrumento como
`"check_contract.py"` —ruta relativa al llamador—, no lo encontraba, recibía `stdout` vacío y las
aserciones lo leían como **tres defectos reales del código medido**.

🔵 **Es P237 otra vez, en versión pequeña: un control que sólo funciona bajo UNA invocación no es un
control.** Y el modo de falla es el peor de los dos posibles — **no explota, miente**: un barrido de
todos los suites de este árbol habría visto rojo y atribuido el rojo al hallazgo.

Reparado en dos movimientos, los dos verificados desde tres directorios distintos (**8/8** en los
tres): la ruta del instrumento se resuelve contra `__file__` y **nunca** contra el `cwd`, y un
`returncode` distinto de cero o un `stdout` vacío salen como **`ERROR` con código 2**, no como
aserción fallida. **Un fallo del arnés y un fallo del código medido no son la misma cosa, y un test
que los confunde es inservible exactamente cuando más se lo necesita.**

## Cómo correrlo

```sh
git clone --depth 50 https://github.com/DavidLMS/learnmcp-xapi.git     /tmp/ll-up
git clone --depth 50 https://github.com/ashleycribb/learnmcp-xapi.git  /tmp/ll-fork
python3 check_contract.py /tmp/ll-up /tmp/ll-fork
python3 test_check_contract.py      # 8/8
```
