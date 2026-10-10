---
industry: education
region: Global
updated: 2026-10-02
---

# Network reachability of SEB Server's proctoring providers — gap 96, closed with code

**Pase 46 del 2026-10-02, acción 2.** Las dos puertas que escribió esta base
(`unitime-mcp-gate`, `sebserver-mcp-gate`) quedaron auditadas con los cinco controles en los
pases 44 y 45. `seb-proctoring-validator` era **la tercera pieza y la única sin medir** —
se escribió en el pase 43, cuando los controles no existían. Esta carpeta la audita, y
**el control (e) corrige una fila de P94 que se venía cotizando.**

Upstream: [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server),
🔴 **MPL-2.0** — *corregido en el pase 98* (`P997`). Este README decía **Apache-2.0**, igual que
`seb-proctoring-validator`, **aunque el pase 44 ya había corregido el valor en `sebserver-mcp-gate`
dos pases antes de que se escribiera este archivo**: una corrección en prosa en un archivo no se
propaga. 🟢 Payload releído en el pase 98: `LICENSE` **16 725 B**, *«Mozilla Public License Version
2.0»*, `master` · `7f45689f797337`, 194 tags. 🔴 **El argumento comercial de esta base (copyleft por
ARCHIVO, §1.10(a)) depende de que sea MPL y no Apache** — y el error iba en la dirección cara, porque
Apache-2.0 es MÁS permisiva.
`HEAD` `7f45689` (2026-04-01, Andreas Hefti) — el mismo commit que ya
citaba el validador, reverificado con `git clone --depth 1 --filter=blob:none --sparse`.

## 🔴 La corrección: Zoom habla con el remoto desde 5 de 14 métodos, no desde 2

P94 publica la fila *«Métodos que hablan con el remoto: Jitsi **1**, Zoom **2**»*. **La cifra
de Jitsi es correcta. La de Zoom no**, y el error es de método: cuenta las primitivas de red
que aparecen **dentro del cuerpo** del método de la interfaz. Esa es la cuenta **directa**, y
para presupuestar importa la **transitiva** — «llamar a este método provoca un viaje HTTP».

| Proveedor | Métodos SPI que **alcanzan** la red | Directos | Profundidad |
|---|---|---|---|
| `JITSI_MEET` | **1 de 14** (`testExamProctoring`) | 1 | 0 |
| `ZOOM` | 🔴 **5 de 14** | 🔴 **0** | **2 a 4** |

**Los cinco de Zoom:** `testExamProctoring` (d=2), `newCollectingRoom` (d=3),
`newBreakOutRoom` (d=3), `disposeBreakOutRoom` (d=3), `disposeServiceRoomsForExam` (d=4).

🔵 **Y el dato que explica por qué la cuenta directa falla tan limpio: en Zoom, CERO métodos
de la interfaz llaman a la red directamente.** Los cinco la alcanzan a través de helpers
privados (`createAdHocMeeting`, `deleteAdHocMeeting`) y de la jerarquía interna
`ZoomRestTemplate`. Un barrido que mire sólo el cuerpo del método puntúa **0**, no 2 ni 5.
**La asimetría real entre la ruta barata y la realista es 1 contra 5, no 1 contra 2.**

### Lo que esto cambia en la cotización

- **`disposeServiceRoomsForExam` está a profundidad 4 y llama a `disposeBreakOutRoom` dentro
  de un `forEach`.** No es un viaje HTTP: es **2 × N**, con N = salas del examen, sin tope en
  el código. Es el método que hay que probar con carga, y P94 lo tenía como local.
- **`newCollectingRoom` y `newBreakOutRoom` cuestan 3 llamadas cada uno, no 1** —
  `createUser` + `applyUserSettings` + `createMeeting` en `createAdHocMeeting` (líneas
  543/554/558). Crear una sala en Zoom **crea un usuario ad-hoc**.
- **Todo el HTTP de Zoom pasa por un único `exchange` privado** (línea 940) envuelto en
  `circuitBreaker.protectedRun`. 🟢 **Para un proveedor propio eso es la buena noticia del
  pase: hay un solo punto donde poner reintentos, *timeouts* y el *circuit breaker*** — y
  conviene copiar esa forma, no inventarla.
- 🔴 **El viaje HTTP menos evidente no está en ninguna llamada a la API: `getZoomRestTemplate`
  valida el template cacheado con `oAuth2RestTemplate.getAccessToken()` (línea 1027), que
  pide el token al endpoint de Zoom.** Validar la caché es tráfico.

## Los cinco controles, con lo que falló

| Control | Resultado |
|---|---|
| **(a)** ninguna ruta con `${` | **N/A declarado** — esta pieza clasifica métodos, no publica rutas |
| **(b)** toda ruta absoluta y con contexto | **N/A declarado** — el SPI es una interfaz Java, no un espacio de URLs |
| **(c)** ninguna fila de una declaración de clase | 🔴 **FALLÓ en la primera corrida** — ver abajo |
| **(d)** todo guarda registrado, incluido el de runtime | 🟢 pasa, y **encuentra dos** |
| **(e)** ningún verbo de lectura que escriba (generalizado) | 🔴 **FALLÓ contra P94** — es el hallazgo |

⚠️ **(a) y (b) se declaran N/A en voz alta y no se omiten.** Un control salteado se lee
exactamente igual que un control aprobado, y esa confusión es la que esta base viene
corrigiendo pase a pase.

🔴 **(c) falló igual que en las dos puertas, y por el mismo motivo.** La primera versión del
extractor emitía **8 constructores como métodos** (`JitsiProctoringService`,
`ZoomProctoringService`, `ZoomRestTemplate`, `OAuthZoomRestTemplate`, más `Context`,
`Features`, `JWTContext` y `User` de las clases internas). Ahora llevan `kind=ctor` y quedan
fuera de la cuenta. **Tercera pieza, tercera vez que el control (c) atrapa lo mismo: el
defecto es del método de extracción, no de un árbol en particular.**

🟢 **(d) encuentra dos guardas de runtime que no son anotaciones**, y una tiene consecuencia
comercial directa: `notifyCollectingRoomOpened` **no hace nada** si
`sendRejoinForCollectingRoom` es `false`, **y `false` es el valor por omisión**
(`@Value("${sebserver.webservice.proctoring.sendRejoinForCollectingRoom:false}")`). Hay un
segundo corte en el mismo método si el *town-hall* del examen está abierto. **Un proveedor
de terceros que implemente ese método copiando la referencia está copiando un no-op.**
El otro flag es `enableWaitingRoom`, también `false` por omisión, que viaja hasta
`createMeeting`.

## 🔴 Las dos trampas del instrumento, anotadas para que no se repitan

Las dos son falsos positivos de **la misma clase** —el verbo no identifica una petición, el
receptor sí— y las dos se encontraron porque la cifra no cerraba con la lectura a mano:

1. **`.put(` y `.delete(` no son verbos HTTP en este árbol.** Una lista de verbos ingenua
   puntúa `attributes.put(...)` —un `Map.put`— como petición: daba **6** llamadas de red en
   `createJoinInstructionAttributes` de Jitsi y **10** en el de Zoom, dos métodos que no
   tocan un socket.
2. **El receptor tiene que TERMINAR en `restTemplate`.** Zoom cachea sus templates en un
   campo llamado `restTemplatesCache`, que es un `LinkedHashMap`: un patrón laxo
   (`\w*restTemplate\w*`) lo aceptaba y le daba a `getZoomRestTemplate` **2** llamadas
   fantasma.

🔵 **Y una decisión explícita en la dirección contraria: construir un `RestTemplate` no es una
petición.** Jitsi construye uno en la línea 162 y la llamada real es el `getForEntity` de la
163. Contar el constructor habría inflado justamente la cifra que este script existe para
corregir.

## Correr la prueba

```sh
python3 extract_reach.py /ruta/a/seb-server > reach.tsv   # regenera la tabla
python3 test_reach.py    /ruta/a/seb-server               # 20/20, incluida la regeneración
```

Sólo biblioteca estándar: **no se instala ninguna dependencia de terceros** y no se modifica
el checkout. Sin argumento, `test_reach.py` valida el `reach.tsv` ya commiteado; con el
checkout, **exige además que la tabla se regenere byte a byte** — una tabla que nadie puede
reproducir es una transcripción, que es exactamente lo que esta base se viene detectando.

Resultado sobre Python 3.11 y `HEAD` `7f45689`:

```
20/20 checks passed
```

## Lo que esto NO cubre

**Alcance, no volumen bajo carga.** `reach.tsv` dice que `disposeServiceRoomsForExam` provoca
`2 × N` peticiones; **no** dice cuánto tarda ni qué hace el *circuit breaker* cuando Zoom
devuelve 429 — eso necesita el servicio levantado, y esta carpeta no levanta nada. Tampoco
cubre el grafo **entre** clases: la cerradura transitiva es intra-archivo, que alcanza porque
las dos implementaciones son autocontenidas (asegurado por la cobertura 14/14 de ambas).
