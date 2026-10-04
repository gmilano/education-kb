---
industry: education
region: Global
updated: 2026-10-04
---

# P230 — la capa OneRoster no es un callejón de LICENCIAS, es un callejón de CAPA

**Pase 76 del 2026-10-03.** Instrumento: `measure.sh`. Salida ejecutada: `result.2026-10-03.txt`
(**10/10** piezas medidas, 0 sin resolver).

## Qué corrige

El pase 75 (**P229**) concluyó que la capa de *rostering* de K-12 es un **callejón de licencias** y que
pedir **permisivo + vivo + spec vigente** deja 🟢 **una** pieza: `bgwdotdev/go-oneroster` (MIT, v1p1).

🔴 **Esa conclusión se falsifica con datos que ya estaban en el mismo archivo que la publica.**
`repos/foundations.md` dice de la MISMA pieza, a 1.662 líneas de distancia:

| Línea | Qué dice de `bgwdotdev/go-oneroster` |
|---|---|
| `repos/foundations.md:106` | 🟢 **«vivo**, 8 ★, Go» |
| `repos/foundations.md:1768` | ⚫ «2019-11-04 · 6,9 años · **muerto**» |

Y lo mismo, cruzado, en `repos/trending.md:24` (vivo) contra `agents/trending.md:4577` (muerto).
**La misma pieza se publica viva y muerta en el mismo `HEAD`.** La condición «viva» de P229 nunca se
evaluó contra la tabla de frescura que esta KB ya tenía.

Las tres condiciones, evaluadas **por separado** y cada una contra su propia evidencia:

| Condición | `go-oneroster` | Evidencia |
|---|---|---|
| permisiva | 🟢 **sí** | MIT, payload de `master/LICENSE` medido en este pase |
| viva | 🔴 **no** | `HEAD` 2019-11-04 — **6,9 años**, por la tabla de esta KB |
| spec vigente | 🔴 **no** | implementa **v1p1**; **v1.2 superó a 1.1 en 2023** y 1.1 está *sunset* para certificaciones nuevas |

🔵 **El conteo correcto de piezas que cumplen las tres no es 1: es 0.** Y el callejón es más cerrado
que lo que dijo el pase 75, no menos.

## El eje que sí explica la capa: CAPA (servidor / cliente / puente)

Medido, no inferido (`result.2026-10-03.txt`):

| Capa | Permisivo | Copyleft | Sin licencia | ¿Alguno con **v1p2**? |
|---|---|---|---|---|
| **servidor** | `go-oneroster` (MIT, v1p1, muerto) | `libre-oneroster` · `chalk` (AGPL-3.0) | — | 🔴 **ninguno** |
| **cliente** | `OneRoster.NET` (MIT) · `gotranseo` (Apache-2.0) · `TCI/OneRoster` (MIT) · `ex_oneroster` (Apache-2.0) | — | — | 🟢 **uno: `OneRoster.NET`** |
| **puente** | — | — | 🔴 **los dos** (`*-csv-sds`, `*-csv-asm`) | 🔴 ninguno |

🔵 **La frase comercial que sale de la tabla, y es la única que importa en una propuesta:**
**CONSUMIR** OneRoster con spec vigente y licencia permisiva **se puede hoy** (`OneRoster.NET`, MIT,
v1p2). **EXPONERLO** —ser la fuente de *roster*— **no**: no existe servidor permisivo en v1p2, así
que la elección real es **construir** o **tomar AGPL-3.0** y asumir el despliegue del distrito.
**Es una decisión de capa, no de licencia.**

## El error de método que este instrumento hace imposible repetir

`repos/trending.md:3383` registra la licencia de `jdolny/OneRoster.NET` como
**«— (no verificada: repo muerto)»**.

🔴 **«Muerto» no es un motivo para no medir la licencia; es un motivo para medirla.** Un permisivo
muerto **se bifurca**; un AGPL muerto **no**. Para código sin mantenimiento la licencia pesa **más**,
no menos — es lo único que queda cuando no hay quien atienda un *issue*. El costo de la omisión fue
una petición HTTP, y escondió el único dato que P229 necesitaba:

🟢 **`jdolny/OneRoster.NET` es MIT (payload `master/LICENSE`, titular `theopenem`, 2020) e implementa
`v1p1` Y `v1p2`**, con dos modelos de autenticación distintos en la API pública —
`V1p1(baseUrl, consumerKey, consumerSecret)` contra `V1p2(tokenUrl, baseUrl, clientId, clientSecret)` —
o sea OAuth1 de dos patas contra *client credentials* de OAuth2. **La pieza que cubría el hueco de
spec de esta capa estaba en la base desde antes, sin licencia y sin spec en la fila.**

⚠️ **Y sus cotas se declaran, porque sin ellas la fila miente por omisión:** es **cliente**, no
servidor; es **sólo rostering** (*«Grade book has not been implemented»*); y su propio README dice
*«The OneRoster 1.2 specification has not yet been finalized»* — 🔴 **fue escrito contra un BORRADOR
de 1.2**, afirmación que hoy está vencida (1.2 se publicó en **septiembre de 2022**). **Sirve como
punto de partida bifurcable, no como conformidad certificable.**

## Dos hallazgos de identidad que el barrido trajo de arriba

🔁 **`fffnite/go-oneroster` es el MISMO proyecto que `bgwdotdev/go-oneroster`**, y esta base nunca lo
registró: `README.md` **byte a byte idéntico** (3.978 B los dos) y `LICENSE` idéntico. El titular del
MIT es **`fffnite`**, 🔴 **cadena con 0 apariciones en 75 pases**. El README se delata solo: la imagen
publicada es `docker.pkg.github.com/**fffnite**/go-oneroster/goors:0.3.1` y los proyectos
acompañantes viven en `fffnite/*`. **Un dedupe por *slug* cuenta dos piezas donde hay una.**

🧾 **El desacople titular ≠ dueño es la NORMA en los permisivos de esta capa, no la excepción: 2 de 2.**
`go-oneroster` (dueño `bgwdotdev`, titular `fffnite`) y `OneRoster.NET` (dueño `jdolny`, titular
`theopenem`). 🔵 **Consecuencia práctica para `p184`/`p190`: en esta capa, preguntarle la licencia al
dueño del repo da el titular equivocado la mitad de las veces.** Hay que leer el payload.

## La fila «puente» de P230: el lado de la EXPORTACIÓN también está cerrado, y por una vía distinta

Los **únicos** puentes abiertos de OneRoster hacia las dos consolas donde un colegio realmente
aprovisiona cuentas son `the-glasgow-academy/oneroster-api-to-csv-sds` (**Microsoft School Data
Sync**) y `oneroster-api-to-csv-asm` (**Apple School Manager**). 🔴 **Los dos: sin archivo de
licencia** — 10 nombres × `main` y `master` en 404 con `README.md` en **200** (ausencia **medida**,
no supuesta). Los dos en PowerShell Core y los dos clavados a **v1p1**
(`GOORS_URL=…/ims/oneroster/v1p1`); `GOORS` es el binario de `go-oneroster`, así que son el **anillo
acompañante** de la pieza muerta.

📍 **Región: EMEA, por configuración y no por antropónimo** (regla **P135**): el README del de
Microsoft dice construir *«the **UK** standard CSV required by Microsoft School Data Sync»*, y el
dueño es un colegio de Glasgow — **afiliación institucional, no nombre propio**. 🔵 **Los pases 74 y
75 declararon EMEA = 0 piezas; esta capa le devuelve dos, y las dos son no entregables por licencia.**

## Cota de canal, medida en este pase y no heredada

| Canal | Hoy | Nota |
|---|---|---|
| `raw.githubusercontent.com` | 🟢 **200** | el único que sirve **payload**; es el canal de este instrumento |
| `pypi.org/pypi/*/json` | 🟢 **200** | |
| `api.github.com/rate_limit` | 🟢 **200** | ⚠️ el único endpoint que pasa es el que **no** transporta dato de repo |
| `api.github.com/repos/*`, `api.github.com/search/*` | 🔴 **403** | por eso no hay ★ ni fecha de `HEAD` medidas en este pase |
| `en.wikipedia.org`, `listedtech.com`, `cubite.io` | 🔴 **bloqueado** | ver abajo |

🔴 **`SOURCE-VERIFIED` para cuota de mercado deja de ser un pendiente y pasa a ser INALCANZABLE por
este entorno, y se mide con dos canales independientes en el mismo pase:**
`curl` devuelve **403 al CONNECT** y el propio proxy lo registra en su bitácora
(`recentRelayFailures`: `{"kind":"connect_rejected","detail":"gateway answered 403 to CONNECT (policy
denial or upstream failure)","host":"en.wikipedia.org:443"}`), y **WebFetch** devuelve
`{"error_type":"EGRESS_BLOCKED"}` para el mismo host. **No es una rareza de WebFetch: es política de
red del entorno.** La lista de excepciones del proxy son **registros de paquetes y hosts de código**
(`registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org`, `index.crates.io`, `proxy.golang.org`,
`jsr.io`) — 🔵 **ni un solo host de investigación de mercado.** La conclusión estructural:
**esta KB puede verificar CÓDIGO y LICENCIAS en la fuente, y no puede verificar CUOTA en la fuente.
Los pases futuros no deberían gastar presupuesto en intentarlo** — lo que sí se puede es lo que hizo
el pase 75: declarar el canal y publicar el **orden** sin el porcentaje.

## Reproducir

```bash
cd compose/code/p230-rostering-layer-axis
./measure.sh                      # la tabla completa (10 piezas)
./measure.sh jdolny/OneRoster.NET # una sola: "MIT|2020 theopenem|master/LICENSE"
```

Control positivo esperado: `usechalk/chalk` → `AGPL-3.0`, `TCI/OneRoster` → `MIT`.
Control negativo esperado: los dos `the-glasgow-academy/*` → `SIN-ARCHIVO-DE-LICENCIA`.
