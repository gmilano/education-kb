---
industry: education
region: Global
updated: 2026-10-03
---

# 🎯 Agentes AI — education

> Agentes y herramientas AI open source para educación. Foco: MIT / Apache 2.0 / BSD.
> Verificado repo por repo vía WebFetch el 2026-09-30 (stars y licencia leídos de la página del repo).
> **Pase 60 del 2026-10-03:** 🔴 **La acción 1 del pase 59 CIERRA y su hipótesis falsable cae en una TERCERA rama que no había previsto. Los dos pares de fork dan veredictos OPUESTOS sobre la misma pregunta y los dos son correctos: `algorithm0r/canvas-lms-mcp` es byte a byte idéntico a `bruchris/canvas-lms-mcp` en los DIEZ archivos leídos —incluido `src/canvas/submissions.ts`, el del eje—, mientras que `abr-Projects/canvas-mcp` DIVERGE de `vishalsachdev/canvas-mcp` en ocho archivos y en 42 líneas de `bulk_grade_submissions`… y sin embargo es IDÉNTICO en el eje de publicación (1 `posted_grade`, 0 consultas de política en los dos).** 🟢 **Así que el denominador de 9 se SOSTIENE y P146 se confirma —pero sólo para ese eje.** 🔴 **Lo que cae es la lectura cómoda: la divergencia del par B cae entera sobre el eje de seguridad VECINO —la precondición de rúbrica— y el fork está del lado LAXO en las cuatro celdas: pierde la verificación POST-escritura `rubric_grade_is_confirmed` (2 usos → 0), convierte un aborto duro en `if "error" not in assignment_check:` —sigue y califica— y condiciona el segundo aborto a `and not dry_run`. Es un snapshot viejo que perdió el endurecimiento de la madre, no una mejora. « Identificar por commit » NO es una precaución de inventario: es sustantiva, en el eje que uno no estaba mirando** (**P150**). 🔵 **De ahí la regla general del pase: la herencia de un fork es RELATIVA AL EJE, nunca global — « es fork de X » cierra la celda que se comparó y deja abiertas todas las demás** (**P151**). 🟢 **Y la acción 2 CIERRA en su rama BUENA, que es la comercialmente útil: `markingworkflow` viene con el token normal. Leído de primera mano en `moodle/moodle` @ `main` (`public/mod/assign/externallib.php`, 3.146 líneas, 5.3rc2 build 20261002): el campo se asigna SIN condicional (l. 464), está en el contrato de salida y NO es `VALUE_OPTIONAL` (l. 584, contra 10 campos que sí lo son), y la única capacidad exigida es `require_capability('mod/assign:view')` (l. 401). Como escribir nota exige `mod/assign:grade` (l. 1033), el argumento es *a fortiori*: toda puerta que pueda CALIFICAR puede, por construcción, LEER la precondición. El *read-before-write* es código, no una escalada de permisos ni un pedido al cliente — y para `toshieji` es el PR de tres líneas que vuelve INCONDICIONAL su garantía** (**P152**). 🟢 **`gap 250` CERRADO** (el árbol se mudó a `public/`: `200` contra `404`). ⚠️ **Dos correcciones de método: la ruta que el pase 59 prescribió (`src/services/canvas-client.ts` en `algorithm0r`) NO EXISTE —es de `CharlieCardenasToledo/mcp-canvas-server`, colisión de ruta entre dos repos del mismo pase (**gap 251**)—; y el primer extractor de funciones de este pase devolvió 7 líneas para una función de 256 y un `diff` de 0: un «IDÉNTICO» falso que, de haberse publicado, era la conclusión opuesta a la verdadera.** Ver **P150**–**P152** y las tendencias **413**–**425**.
>
> **Pase 59 del 2026-10-03:** 🔴 **la acción 2 del pase 58 CIERRA y su hipótesis falsable cae en la rama de la UNICIDAD: ampliado el barrido de 6 a 9 puertas de escritura de nota leídas en el CÓDIGO, `peancor/moodle-mcp-server` sigue siendo la ÚNICA que AFIRMA la publicación. «Afirma la publicación» NO es una clase de la capa: es UNA fila, y la regla de entrega se confirma — se EXCLUYE, no se configura** (**P142** se sostiene). 🔴 **Y aparece la simetría que reencuadra toda la capa: el eje es BIPOLAR y ESCASO. Sólo 2 de 9 toman posición en el código, y son los dos extremos — `peancor` cablea `workflowstate: 'released'` y `toshieji/moodle-grading-mcp` cablea `"workflowstate": "readyforreview"` con `"released": False` (verificado en `server.py:570` de primera mano en este pase, no en el README). Las otras 6 no dicen nada: heredan. 🔴 **Pero NINGUNO de los dos polos consulta la precondición, así que las dos garantías son CONDICIONALES y en sentidos opuestos: a `peancor` no la salva `markingworkflow=1`, y a `toshieji` la DERROTA `markingworkflow=0`.** El único cumplimiento incondicional sigue siendo `AI-Teaching-Agent`, que no puede publicar (**P145**). 🔴 **Hallazgo estructural NUEVO y cambia cómo se cuenta esta capa: las puertas de Canvas se propagan por FORK. `algorithm0r/canvas-lms-mcp` es fork CONFIRMADO de `bruchris/canvas-lms-mcp` y `abr-Projects/canvas-mcp` es fork CONFIRMADO de `vishalsachdev/canvas-mcp` —ambos MIT, ambos escriben nota— así que heredan el camino de escritura ya medido y un barrido por REPO sobre-cuenta el código. La unicidad se cuenta sobre CÓDIGO DISTINTO, no sobre repos distintos** (**P146**). 🟢 **1 puerta NUEVA y no es fork: `CharlieCardenasToledo/mcp-canvas-server` (MIT, 0 ★, TS) — `posted_grade` crudo y CERO consultas de política de publicación en 60.194 bytes de `canvas-client.ts`; publica por OMISIÓN, así que la configuración correcta la neutraliza.** 🔴 **Y el dato de licencia que hay que decir antes de recomendar nada: el MCP de Moodle más estrellado que apareció en este barrido —`loyaniu/moodle-mcp`, 37 ★— NO TIENE LICENCIA: `LICENSE` ausente en `main` y `master` y sin clave `license` en `pyproject.toml`. Es inusable por Globant, y las que sí tienen licencia tienen 0 ★ — tercera reproducción de la curva invertida de P134/P138** (**P147**). ⚠️ **4 candidatas más SCREENEADAS y descartadas como puertas por ser de SÓLO LECTURA (`loyaniu`, `Jawadh-Salih/moodle-mcp-server` MIT-Go, `dddanielliu/NCCU-Moodle-MCP` sin licencia, `csmediapro/moodle-mcp-server` AGPL-3.0 *«Read-only — never modifies Moodle data»*) más `PabloPC05/mcp-usc`: se registran como ausencias MEDIDAS, no como silencio.** 🔴 **La acción 1 se entrega CON SU FIXTURE REFUTADO: el par que el pase 58 mandó usar de control negativo (acción 3 del pase 57 ↔ tendencia 392) NO EXISTE — el bloque de acciones del pase 57 cita gaps 249/232/100 y no afirma nada sobre fechas; la pregunta de las fechas es el `gap 56`, del pase 32, cerrado en el 39. El defecto que el pase 58 diagnosticó es real, pero su única evidencia era ella misma un error de cruce** (**P148**). ⚠️ **Nota de instrumento, segunda reproducción consecutiva: este entorno negó ejecutar el código clonado INCLUIDAS las suites OFFLINE, así que la suite nueva se publica con 17 asertos ESCRITOS y 0 CORRIDOS, declarado en su README.** Ver **P145**–**P148** y las tendencias **402**–**412**.
> **Pase 58 del 2026-10-03:** 🔴 **la acción 1 del pase 57 CIERRA y su hipótesis falsable cae en la rama que obliga a trabajar: de las SEIS puertas de escritura de nota, leídas en el CÓDIGO y no en el README, **0 consultan la precondición de su plataforma** —`markingworkflow` en Moodle, `posting_policy`/`post_manually` en Canvas—, así que «borrador» es una palabra que esta capa usa sin respaldo y el requisito de Globant pasa a incluir la VERIFICACIÓN DE PLATAFORMA como paso obligado del despliegue.** 🔴 **Y aparece el eje que de verdad decide un despliegue, invisible desde el vocabulario de «borrador»: `peancor/moodle-mcp-server` manda `workflowstate: 'released'` CABLEADO en `src/index.ts`, de modo que es la ÚNICA de las seis que publica incluso con `markingworkflow=1` — 5 de 6 quedan NEUTRALIZADAS por la configuración correcta de la plataforma y 1 de 6 la DERROTA. Es la fila que hay que EXCLUIR, no la que hay que configurar** (**P142**). 🔵 **`NiccoloSalvini/mcp-moodle-staff` está fuera del eje por diseño y no por falta de dato: no llama al web service —*«the CSV import is Moodle's own way in»*—, así que la liberación humana es del PROCESO (una persona aprieta Importar en la UI) y no del servidor; ⚠️ pero el importador del libro de calificaciones tampoco pasa por marking workflow, así que no es «más seguro»** (**P143**). 🟢 **1 ALTA, la primera en DOCE pases, y entra por lo que CONTESTA: `littlecookie0722/AI-Teaching-Agent` (MIT verificado por el texto del `LICENSE`) cumple «borrador + liberación humana» incondicionalmente porque NO PUEDE publicar. El patrón no es una compuerta mejor adentro del camino de escritura: es separar la generación de la publicación** (**P144**). 🔴 **La acción 3 del pase 57 estaba CERRADA antes de escribirse y la cerró el propio pase 57 en su tendencia 392: las «dos fechas incompatibles» son DOS OBLIGACIONES DISTINTAS, no una contradicción — es el defecto del gap 54 aplicado ADENTRO, y el mecanismo es que la lista de acciones y la de tendencias se escriben por separado y nada las cruza.** 🟢 **Las fechas re-verificadas hoy por tres canales concordantes y la tabla del calendario re-anclada al 2026-10-03.** ⚠️ **Nota de instrumento que corrige al pase 52 en la dirección CONTRARIA: este entorno negó ejecutar el código clonado INCLUIDAS las suites OFFLINE, así que la columna «Hoy» del `README.md` NO se re-verificó y este pase no afirma ninguna de esas cifras como medida hoy.** Ver **P142**–**P144** y las tendencias **393**–**401**.
> **Pase 57 del 2026-10-03:** 🔴 **el pase ejecuta las dos acciones del 56 y el hallazgo que manda borra la única celda verde que tenía la tabla de la capa docente: la garantía de borrador de `toshieji` —la ÚNICA pieza T2 y la única conforme al Artículo 50 de las ocho— NO es una propiedad del servidor, es una propiedad de una casilla de configuración POR TAREA que el servidor no mira, no documenta y no posee.** Leído de primera mano en `moodle/moodle` @ `main`, `public/mod/assign/locallib.php:2991-3001`, con el comentario del propio Moodle: *«If marking workflow is enabled, the workflow state is at 'released'»* y su SQL `WHERE (a.markingworkflow = 0 OR (a.markingworkflow = 1 AND uf.workflowstate = :wfreleased))`. 🔴 **Con `markingworkflow = 0` Moodle le manda la nota al alumno sea cual sea el `workflowstate`, y en `locallib.php:7960` el cambio de estado no se registra siquiera. El README de `toshieji` dice «Safety (enforced server-side)» y «No student notification (draft state)», y tiene CERO menciones de `markingworkflow` en sus 8.326 bytes** (**P139**). ⚠️ **Así que el T2 incondicional de la capa es 0 de 8, no 1 de 8.** 🔵 **La hipótesis falsable de la acción 1 cae por SEGUNDO pase consecutivo en el medio que ella misma declaró sin interpretar: la compuerta de arranque sobre la escritura de juicio da 3 de 8 (el 56 pidió ≥ 4 para «es la norma» y ≤ 2 para «hallazgo de riesgo»), así que no decide — pero como en el pase 54 apareció un predictor mejor que un porcentaje.** 🔴 **La escalera G0–G3 del pase 56 suelda DOS EJES INDEPENDIENTES: «impedir listar el tool» no es una propiedad de la granularidad.** `Dymayo` tiene la compuerta más gruesa (un booleano por ROL) y **sí** desregistra (*«Tools behind a disabled flag are not registered at all»*); `toshieji` tiene una más fina (allowlist por RECURSO) y **no** desregistra; y `CANVAS_ROLE` de `bruchris` filtra el listado **sin ser un límite**, dicho por el propio proyecto: *«`CANVAS_ROLE` hides tools from a listing; `block` means the handler is never registered»* (**P137**). 🔴 **Y el eje que de verdad decide un despliegue no está en la escalera: el SENTIDO DEL DEFECTO.** La compuerta más fina de las ocho —`ALLOWED_WRITE_TOOLS`, nacida de un *security release*— es **fail-OPEN en stdio**, que es el despliegue normal de un docente: *«HTTP servers are read-only unless configured … Local stdio servers are unchanged unless you set it»*. **De las 3 piezas con compuerta real sobre la nota, sólo 2 son fail-closed por defecto en local, y las dos tienen 0 ★ mientras la de 272 ★ es la fail-open** (**P138**, misma curva invertida que P134). ⚠️ **`bruchris` desregistra de verdad (`CANVAS_DESTRUCTIVE_TOOLS=block`) pero sobre los SIETE tools de borrado: la nota no está cubierta, así que en este eje es G0 — la compuerta más honesta de la capa apunta al objeto equivocado** (**P140**). 🟢 **Acción 2 cerrada con código versionado: `compose/code/grading-draft-gate/` (37/37, OFFLINE), con los controles negativos que el 56 exigió y tres mutaciones que prueban que la suite tiene dientes (31/37, 36/37, 35/37).** 🟢 **Y una pregunta hacia afuera del pase 56 se contesta MIDIENDO en vez de preguntando: `mcp-moodle-teacher` y `mcp-moodle-staff` sirven el MISMO README byte a byte (sha256 idéntico) y el canónico es `mcp-moodle-staff`, que es el que titula** — con control negativo de tres nombres plausibles del mismo dueño en 404. ⚠️ **La tabla NO crece (80 filas, 0 altas): undécimo pase sin altas.** Ver **P137**–**P141** y las tendencias **370**–**392**.
> **Pase 56 del 2026-10-03:** 🔴 **el pase cierra el agujero de P129 y la hipótesis que el pase 55 escribió de antemano cae en su rama mala: `toshieji` queda SOLO (1 de 8), así que «borrador + liberación humana» NO es la norma emergente de la categoría y el requisito lo tiene que escribir Globant.** 🔴 **Pero el hallazgo que manda degrada una recomendación de esta propia base: el pase 55 llamó al `confirmation_token` de `mcp-usc` «el mejor control de escritura medido en esta KB» y propuso extraerlo a una librería — y la pieza más adoptada de la capa (`vishalsachdev/canvas-mcp`, 272 ★) publicó un *security release* que dice que una confirmación NO PUEDE parar el ataque real de educación:** *«Instructions a student plants in course content can steer an instructor's assistant, and a confirmation token cannot stop that because the assistant can redeem its own token»*. **El que redime el token es el propio asistente: la confirmación no es una segunda autoridad, es la misma autoridad dos veces. Su remedio no es confirmar mejor, es que la herramienta no exista (`ALLOWED_WRITE_TOOLS`)** (**P132**). ⚠️ **El esquema de cuatro clases se rompe igual que el de tres del pase 54: la pluralidad de la capa (4 de 8) confirma pero no divulga, y eso no entra en T3 ni en T4 — se agrega T3′** (**P133**). 🔴 **La divulgación es 1 de 8 con el Artículo 50 vigente hace dos meses, y las curvas van al revés: la más adoptada (272 ★) es T4 y la única conforme tiene 0 ★** (**P134**). 🟢 **Dos regiones ubicadas con evidencia de primera mano (`vishalsachdev` → North America, NUEVA; `toshieji` → APAC, reconfirmada) y las otras 6 declaradas sin región.** ⚠️ **Y dos falsos positivos propios atrapados antes de publicar: un barrido de topónimos que ubicó una pieza en «Italia» por subcadena de `Italicia` (P135), y el resumidor que confundió «pide confirmación» con «escribe borrador» — son ejes independientes.** 🟢 **La tabla NO crece (80 filas, 0 altas): décimo pase sin altas, y el pase se gastó entero en las dos acciones del 55, las dos ejecutadas completas.** Ver **P132**–**P135** y el patrón nuevo **P136** y las tendencias **338**–**369**.
> **Pase 55 del 2026-10-03:** 🔴 **el pase ejecuta las dos acciones del 54 y el hallazgo que manda invierte la intuición de cualquier filtro de componentes: los dos ejes de esta capa están ANTI-correlacionados.** Las **tres** piezas que someten trabajo calificado son las tres de PEOR procedencia de credencial (`@ink-waffle` b4+b3, `mcp-usc` (a)+b2, `moodler-mcp` b4) **y las tres traen salvaguarda de integridad explícita**; la pieza de credencial más limpia —`peancor/moodle-mcp-server`, 🟢 clase (a) con token de administración del **SITIO**— es la **ÚNICA de las seis sin ninguna**: ni confirmación, ni borrador, ni divulgación, ni texto de integridad. 🔴 **Así que un filtro que ordene por higiene de credencial selecciona A FAVOR de la escritura de notas sin guarda** (**P127**). 🟢 **La clase (4) NO existe en las seis, y el pase 54 pidió decirlo: el ecosistema se autolimita donde la licencia no lo obliga** (**P128**) — 🔴 **y el «candidato natural a (4)» que el 54 nombró, `DUTIC-mcp`, resultó el de disciplina MÁS estricta** (*«Todo simula por defecto»*, dos flags obligatorios, *«se niega a completar en vez de inventarse una valoración»*). ⚠️ **El esquema de cuatro clases tiene un agujero que este pase declara en vez de tapar: es estudiante-céntrico y no clasifica la escritura del lado DOCENTE, que es justo donde está la pieza sin guarda** (**P129**, acción 1 del pase 56). 🟢 **Acción 2 cerrada con denominador ENUMERADO: 14 filas del mapa por LMS → 9 clientes de tercero determinables (3 medidas acá por primera vez), 2 no determinables, 1 que no es cliente de un tercero y 2 fuera del eje; y la tasa enumerada (2 de 9, 22,2 %) es MENOR que la oportunista (7 de 18, 38,9 %).** ⚠️ **La tabla NO crece (80 filas, 0 altas): noveno pase sin altas desde el barrido obligatorio.** 🟢 **Una región recuperada con evidencia de primera mano —`toshieji` → APAC, 800 caracteres CJK— y el tamaño del problema medido: 16 de 21 filas sin región declarada.** ⚠️ **Y una corrección que el pase se hace a sí mismo antes de publicar: un `grep` escrito a mano dio dos cifras del README como «vencidas» y era falso positivo** (**P126**). Ver **P126**–**P130** y las tendencias **313**–**336**.
> **Pase 54 del 2026-10-03:** 🔴 **el pase corrige el instrumento que el pase 53 acababa de construir, y lo corrige por donde el pase 53 dijo que había que probarlo: su propio CONTROL NEGATIVO falló.** El pase 53 escribió que `Dymayo/moodler-mcp` *«usa web service token, así que si saliera (b) el instrumento está mal»* — **salió (b)**, y el defecto tiene nombre: **P121 leía el TIPO de la credencial y hay que leer su PROCEDENCIA** (**P123**). 🟢 **La clase nueva, b4, es la que ningún filtro ve: la pieza abre un navegador real, el alumno completa su SSO con passkey y 2FA, y entonces la pieza le pide a Moodle un token de web service de app móvil y lo guarda en disco** — *«requests a mobile-app web service token from Moodle and stores it locally»*. **Artefacto de clase (a), emisor de clase (b).** 🔴 **Y el corolario invierte la intuición de cualquier filtro de componentes: `moodler-mcp` declara UNA variable (`MOODLE_URL`) y NINGUNA credencial, precisamente porque se la consigue sola — un audit de `.env` lo aprueba.** 🔵 **La hipótesis falsable del pase 53 cae en el medio que había declarado sin interpretar (2 de 7 este pase, 28,6 %; acumulado 7 de 18, 38,9 %: ni el ~45 % ni el <15 %), así que no decide — pero apareció un predictor mejor que un porcentaje: el canal correlaciona con el ALCANCE, no con la plataforma. Pieza con nombre de universidad: 3 de 3 en clase (b). Conector genérico de producto: 11 de 13 en (a), y las 2 excepciones son justamente las dos que mintan su propio token.** ⚠️ **La tabla NO crece (80 filas, 0 altas): el pase se gastó en las dos acciones que el 53 dejó escritas, y las dos se ejecutaron completas.** 🔴 **Nota de instrumento que es también una frontera nueva: el barrido que enumera estas filas quedó negado por `[Credential Exploration]` —una TERCERA frontera, distinta de las dos del pase 53— y lo niega tanto sobre el markdown de esta propia KB como sobre READMEs públicos ya descargados; lo que sí corre es WebFetch, que es el canal que la acción 1 del pase 53 prescribía.** ✅ **Control del pase 53 reproducido de primera mano: `curl -sI` da 403 para `github.com/moodle/moodle` Y para un repo inventado — no discrimina; `raw.githubusercontent.com` da 200/404.** Ver **P123**, **P124**, **P125** y las tendencias **295**–**312**.
> **Pase 53 del 2026-10-02:** 🔴 **la tabla NO crece (80 filas, 0 altas) y el pase se gastó en mirar las filas que ya estaban por un eje que nunca se les había aplicado — que es donde estaba el valor.** La acción 1 del pase 52 dejó una hipótesis falsable sobre P118 —*si `canvas-student-mcp` es un caso aislado, el barrido devuelve UNA fila en la clase (b)*— y **devolvió cinco: 12 README leídos, 11 clientes de LMS/SIS clasificables, 5 en clase (b) / 6 en clase (a) / 1 no aplica, con una pieza de clase (b) en CADA una de las cuatro regiones.** 🔵 **Los doce veredictos están escritos EN LA CELDA DEL REPO de cada fila y no en una nota al margen, por la lección del pase 52: quien copia un nombre de una celda se lleva el nombre, no la advertencia.** 🔴 **Y los tres valores de P118 no alcanzaban: la clase (b) son TRES clases —b1 monta la sesión conservando passkey/2FA, b2 pega la cookie de DevTools, b3 guarda usuario y contraseña reutilizables en el `.env`— así que una fila que dijera sólo «(b)» escondería la diferencia entre `jbnu-lms-student` y `DUTIC-mcp`.** ⚠️ **El único candidato nuevo del barrido (`ASEpochs/ai-digital-teacher`, 12 ★, APAC) se RECHAZA por dos motivos independientes y medidos: sin licencia (6 nombres × 2 ramas = 12 sondas en 404 + sidebar sin licencia) y del lado del art. 5(1)(f) del AI Act que hay que defender — razonamiento de conducta sobre alumnos desde cámara.** 🔴 **Nota de instrumento: el verificador `curl -sI` que la consigna prescribe devuelve 403 para TODO `github.com` (4 de 4 URLs verdaderas incluidas), así que todo este pase se verificó por `raw.githubusercontent.com` y WebFetch.** Ver **P121**, **P122** y las tendencias **281**–**293**.
> **Pase 52 del 2026-10-02:** 🟢 **la tabla pasa de 74 a 80 filas (+6) y el hallazgo del pase es que el instrumento de licencia que el pase 51 declaró obligatorio tenía su propio supuesto cultural ADENTRO DE UNA EXPRESIÓN REGULAR.** El ancla del tarball —`^package/(LICEN[CS]E|COPYING)[^/]*$`, obligatoria desde la tendencia 259— **es CASE-SENSITIVE**, y por eso se publicó *«sin licencia en el tarball»* para `@learninglocker/xapi-agents`, que envía **`package/license`** en minúscula con **35.121 bytes de GPL-3.0** adentro. 🔵 **Es el mismo error que la tendencia 252 —una lista de nombres de archivo es un supuesto cultural— sólo que esta vez el supuesto lo había escrito el pase anterior.** Ancla corregida, con control **offline** de 24/24 que demuestra el defecto y conserva el control positivo de la tendencia 259 (144 licencias de `node_modules` → raíz=0). 🟢 **La acción 1 se ejecutó y su hipótesis falsable se CONFIRMA: cambian 3 de los 9 veredictos, y los tres los resuelve el TARBALL, no los 20 nombres** —`@eduware/oneroster` (0BSD), `@osu-cass/sb-components` (MPL-2.0) y `@learninglocker/xapi-agents` (GPL-3.0)—, así que *«indeterminado»* **no era una propiedad de los paquetes sino del canal que se les había aplicado.** 🔴 **Dos direcciones NUEVAS del defecto campo-vs-texto, y en las dos el campo y el texto nombran licencias DISTINTAS:** `@eduware/oneroster` declara `MIT` y envía **0BSD** en un archivo **byte a byte idéntico** (mismo sha256) al de `@superbuilders/oneroster`, **que nombra como titular a un tercero ajeno a las dos organizaciones**; y `@pie-qti/*` declara `MIT` en npm contra **`ISC`** en tres artefactos del repositorio — 🔵 **ahí el lado equivocado es el REGISTRO, así que la dirección del error no es predecible.** ⚠️ **Y una fila entra con una advertencia que NO es de licencia:** `canvas-student-mcp` es **MIT** verificado por dos artefactos **y su argumento de venta es eludir un control institucional** (cookie de sesión para sortear que la universidad deshabilitó los tokens) — **licencia impecable y no entregable sin consentimiento de la institución**, que es el eje nuevo de **P118**. ✅ **Control del gap 71 corrido en el mismo pase que tocó la tabla: 80 filas / 80 claves distintas / 0 duplicados, 60 cabeceras con sus 60 separadores y 0 encabezados usados como dato.** 🟢 **La acción 3 se ejecutó COMPLETA: 27 menciones corregidas en seis archivos y las DOS listas agregadas «MIT / Apache-2.0 ✅» DESARMADAS** —el pase 51 las había marcado al margen y la nota no viaja con el nombre. Código, control offline y TSV en `compose/code/registry-license-remeasure/`. Tendencias **265**–**280**.
> **Pase 50 del 2026-10-02:** 🟢 **el gap 233 queda CERRADO y el 232 baja de bloqueante a opcional: Canvas se entrega hoy sobre MIT.** Las dos puertas permisivas tienen ahora **texto** de licencia verificado por `raw.githubusercontent.com` —`bruchris/canvas-lms-mcp` (*© 2026*, **165** tools, **166** con FERPA en stdio) y `vishalsachdev/canvas-mcp` (*© 2025*, **hasta 103**)— y la mayor **cubre los cuatro dominios del núcleo**. ⚠️ **La resta 227−165 NO se debe escribir: son dos instrumentos distintos** (**P113**). **1 alta, y entra como ADVERTENCIA:** `DMontgomery40/mcp-canvas-lms`, con *badge* de licencia **en el README de un tercero** y `LICENSE` **404 en `main` y `master`** con el repo respondiendo 200. 🔴 **Y una corrección propia: este pase midió dos piezas, las escribió como altas y LAS DOS YA ESTABAN en esta tabla** —se revirtieron antes de publicar (tendencia 246). Tendencias **234**–**246**.
> **Pase 49 del 2026-10-02:** 🟢 **la tabla pasa de 66 a 69 filas, y el séptimo pase sin altas se rompió cambiando
> el CANAL, no insistiendo con la búsqueda.** La acción 3 del pase 48 planteó la hipótesis falsable: *si el vacío de
> origen APAC es del canal, buscar por ORGANIZACIÓN lo rompe; si la organización tampoco devuelve nada, el vacío es
> real.* 🔵 **Resultado: la hipótesis se parte en dos, y las dos mitades son útiles.**
> 🟢 **El canal SÍ era el problema:** una sola consulta a la página de repositorios de **HKUDS** —el laboratorio que
> ya había dado `DeepTutor`— devolvió **tres piezas que esta base no tenía en ninguno de sus ocho archivos**
> (`AI-Researcher` 5.8k, `Paper2Slides` 3.8k, `VideoAgent` 1.9k; **cero** coincidencias previas, medido con `grep -ric`
> sobre los ocho). **Seis pases de `AI education APAC 2026 …` no habían devuelto una sola.**
> 🔴 **Y el vacío EDUCATIVO es real:** **ninguna de las tres menciona educación, enseñanza, alumnos ni cursos.** Son
> capacidad agéntica de un laboratorio APAC, no piezas de aula. **La conclusión honesta no es «APAC no produce», es
> «APAC no produce open source EDUCATIVO-NATIVO, y sí produce la capacidad con la que se construye»** — que para una
> propuesta es una recomendación distinta y mejor: se compone, no se espera. ⚠️ **El barrido obligatorio completo se
> corrió igual** (cuatro globales + cuatro regionales, año **calculado**: 2026) **y por séptima vez no devolvió ninguna
> pieza educativa nueva**; APAC devolvió contenido de *enterprise* y **ni siquiera de educación** (el propio buscador lo
> dijo). 🔴 **La licencia de una de las tres bloquea la entrega:** `AI-Researcher` **no tiene archivo de licencia en
> ninguna rama**, y la ausencia está **medida con control positivo** (el `README.md` del mismo árbol da **200**, así que
> el 404 es del archivo y no del canal). 🟢 **Controles de la tabla, en verde: 69 filas, 64 *slugs* distintos, 0
> duplicados, y 0 filas de encabezado filtradas como dato** (las **5** que lo parecen son encabezados de las cinco
> tablas de este archivo, y **las cinco tienen su `|---|` debajo** — verificado en el pase 49).
> 🟢 **Y el canal de licencias dejó de estar cerrado:** `raw.githubusercontent.com/<org>/<repo>/main/LICENSE` responde
> **200** donde `github.com/<org>/<repo>` responde **403** — ver `compose/code/npm-surface-probe/`.
> **Pase 48 del 2026-10-02:** 🔵 **la tabla sigue en 66 filas — SEXTO pase consecutivo sin altas**, y el barrido
> completo obligatorio (cuatro búsquedas globales + cuatro regionales, con el año **calculado**: 2026) devolvió por
> sexta vez **la capa genérica** (OpenClaw, CrewAI, LangGraph, browser-use, Dify, Flowise, AutoGen, Langflow) y
> **material didáctico *sobre* AI** (catálogos `500-AI-Agents-Projects`, `awesome-ai-agents-2026`, currículos de
> DeepLearning.AI / HuggingFace). 🔴 **Y la señal de saturación más clara hasta acá: el barrido devolvió DOS piezas que
> esta base ya tiene —`lineage-skill` y `SirhanMacx/Claw-ED`— presentadas como novedad.** Cuando una búsqueda de
> descubrimiento empieza a devolver el propio inventario, ha dejado de ser una búsqueda de descubrimiento; se sigue
> corriendo porque es obligatoria y porque un cambio de capa hay que verlo, pero **el rendimiento marginal medido es
> cero.** 🟢 **Controles de integridad de la tabla, corridos y en verde: 66 filas, 61 *slugs* distintos de GitHub y
> ningún duplicado** (el control del gap 71), **y ninguna fila de encabezado filtrada como dato.** 🟢 **El valor del
> pase está afuera de esta tabla: se cerró el gap 103 escribiendo la pieza genérica de P85
> (`compose/code/mcp-allowlist-gateway/`, 34/34), se barrieron las 3.611 cifras de los ocho archivos y se trazó la
> procedencia de `project-nomad` hasta la pantalla (32/32). Ver `repos/trending.md` de este pase.**
> **Pase 47 del 2026-10-02:** 🔵 **la tabla sigue en 66 filas — QUINTO pase consecutivo sin altas**, y el barrido
> completo obligatorio (cuatro búsquedas globales + cuatro regionales, con el año **calculado**) devolvió por quinta vez
> **la capa genérica** (openclaw 385.407 ★, dify 151.639, browser-use 108.128, Mem0 62.735, AutoGen 60.284, Flowise
> 55.226) y **material didáctico *sobre* AI**. Rechazos nuevos registrados para no volver a pagarlos:
> `speedyapply/2026-AI-College-Jobs` (**5.200 ★**, bolsa de trabajo), `karpathy/nn-zero-to-hero`, *Awesome LLM* y
> *Agents Towards Production* (**currículo**, no software que educa). 🔴 **Y el hallazgo del pase es sobre las filas que
> YA están: se leyó el CONTENIDO de las 33 expuestas —24.206 archivos listados, 432 leídos— y CERO emiten un límite
> dentro del texto que generan.** Las tres que un barrido de tokens marcó como candidatas resultaron límites de la
> **entrada** (`chunk_index` de recuperación, una columna de base de datos) y una no es procedencia en absoluto
> (`toc_end_index = min(5, len(images))`, paginado de PDF). **Consecuencia para cualquier fila de esta tabla que se
> proponga con marcado del Artículo 50(2): el marcado del curso entero es entregable, el marcado por afirmación es
> desarrollo nuevo.** Medición en `compose/code/aiact-50-2-spans/`, cotización en **P108**.
> **Pase 25 del 2026-10-01:** **la tabla sigue en 37 filas — séptimo pase consecutivo sin altas**, y el barrido completo
> obligatorio (cuatro búsquedas globales + cuatro regionales, con el año **calculado**) devolvió por tercera vez la capa
> genérica y el material didáctico *sobre* AI. **El hallazgo de agente del pase no es un agente: es una puerta.**
> `cassproject/CASS` (**Apache-2.0**, 62 ★) expone **MCP** entre sus cartuchos — **la primera pieza de estándar educativo
> de esta KB con puerta nativa de agente**, y la que además hace las **aserciones** de competencia que las cuatro piezas
> CASE de esta base no hacían. Ver la tendencia **65**, el patrón **P48** y el **gap 40** (está declarado, no medido).
> **Pase 26 del 2026-10-01:** **la tabla pasa a 38 filas — se corta la racha de siete pases sin altas**, y se corta
> por donde el pase 25 dijo que había que buscar: **el conector, no el agente.** Entra `vishalsachdev/canvas-mcp`
> (**MIT**, 269 ★, 815 commits, **hasta 102–103 tools** + 8 *agent skills*), que es **el conector permisivo de LMS más
> grande que vio esta KB** y el primero que cubre el lado docente además del del alumno. Y el **gap 40 se cierra
> ejecutando**: el cartucho MCP de CaSS **genera 6 tools y 3 resource templates** medidos con el propio generador del
> proyecto — entre ellos `record_evidence` y `get_learner_profile`, que son **exactamente los dos pasos que el patrón
> P48 necesitaba**. Ver la tendencia **66**, el **gap 40 (CERRADO)** y la sección nueva de la capa conector, abajo.
> **Pase 10 del 2026-10-01:** para el contenido, la verificación se hizo contra el archivo `LICENSE`, no contra el README — y por eso apareció la contradicción que documenta la capa de contenido curricular, abajo.
> **Pase 27 del 2026-10-01:** **la tabla pasa de 38 a 41 filas**, y las tres altas son conectores: 🔴 **el pase 26 declaró que Moodle no tenía conector MCP permisivo (gap 43) y es falso** — hay **dos MIT**, y `peancor/moodle-mcp-server` **escribe nota y devolución** (`provide_assignment_feedback`), la primera pieza permisiva que toca el **gap 6** desde el pase 2. Entra también `scorm-mcp-server` (MIT, offline). El hueco real del eje conector **es Open edX**, el único LMS grande sin puerta de agente (**gap 48**). Y la superficie MCP de CaSS queda medida por adaptador: **CASE, CEASN y Open Badges están enteros fuera de MCP**, y el Open Badges de CaSS es **OB 2.0, no 3.0**. Ver la capa de conectores, abajo.

> **Pase 28 del 2026-10-01:** **la tabla pasa de 41 a 43 filas**, y la alta que importa **refuta otra ausencia declarada**: 🔴 **el pase 26 dijo que OneRoster no tenía conector MCP y es falso** — `trilogy-group/oneroster-ts` es **0BSD** (la primera licencia 0BSD de esta KB) y expone **164 métodos como MCP tools, con escritura**, que es **la superficie de herramientas más grande de toda esta base**. Y **la regla del pase 27 no habría alcanzado para encontrarlo**: el repo **no se llama `*-mcp`**, es un **SDK** que agrega MCP en una línea del README. **Cuarta corrección consecutiva por muestreo.** Entra también `paulocymbaum/ed-tech-system-mcp` (MIT, 18 tools, LangGraph, sin LMS). **QTI queda como la única ausencia medida por tres métodos** y **CASE queda sin medir por colisión de término** (cuarta de esta KB: `case` → *case study* / *use case*, **gap 51**). Ver la capa de conectores, abajo.
> **Pase 29 del 2026-10-01:** **la tabla pasa de 43 a 44 filas**, y el valor del pase no está en el alta sino en **dos ausencias que se dan vuelta leyendo el código**. 🔴 **El pase 28 concluyó que el *authoring* de Open edX está «declarado experimental» y que por eso había causa técnica para la ausencia del conector. Es falso, y la causa fue leer un solo archivo.** El aviso *«the Authoring API is still experimental… use the v0 versions»* vive en `v1/urls.py`, **está fechado «(Nov. 23)» y encabeza una sección vacía**; mientras tanto `v0/views/xblock.py` declara **lo contrario** —*«superseded by `XblockViewSet`… use `/api/contentstore/v1/xblock/` going forward»*— y **`v1/urls.py` registra efectivamente ese `XblockViewSet` con CRUD completo** (`create`/`retrieve`/`update`/`partial_update`/`destroy`) bajo un programa de ADRs con nombre (**FC-0118**). **Es una deprecación circular, y la señal nueva gana: la autoría es cotizable.** Ver el **gap 50 (REENCUADRADO)** y **P55**. ✅ **Y el gap 51 queda medido:** CASE **sí** tiene implementación de referencia permisiva —[`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE), **Apache-2.0**, 9 ★, 180 commits, CASE **1.0 y 1.1**— **y sigue sin conector MCP**, ahora por medición y no por colisión. 🔴 **La colisión número cinco de esta KB es de un tipo nuevo: el «MCP» que aparecía en la página de OpenCASE es el menú de GitHub** (*AI CODE CREATION → MCP Registry*), **no el repo** — el README crudo tiene **cero** menciones. **Regla nueva: la presencia de MCP se verifica en el README crudo, nunca en la página renderizada.** Ver las tendencias **78**, **79** y **80**, el **gap 51 (CERRADO)** y el patrón nuevo **P60**.

> **Pase 30 del 2026-10-02:** **la tabla pasa a 47 filas, y la alta más importante cierra la mejor oportunidad que tenía esta KB — en contra.** 🔴 **El gap 48 («Open edX es el único LMS grande sin puerta de agente») lo cerró el propio proyecto:** `openedx-mcp` + `tutor-contrib-openedxmcp`, publicados en PyPI el **2026-07-25**, los dos **AGPL-3.0**. **35 endpoints medidos leyendo el código del sdist** (28 LMS + 7 CMS), **con autoría incluida** —lo que confirma por implementación la refutación del pase 29— y con **cuatro rails contra «agente en bucle»** que son el artefacto más reutilizable que encontró esta base: *dry run* + **confirm token atado a una huella del payload**, rate limit por (key, tool), re-chequeo de autoridad vivo y **auditoría append-only previa a la escritura**. 🔴 **Pero rompe la tesis del pase 27:** esta puerta **corre en proceso** como plugin Django dentro del LMS y del CMS, así que *«las LMS son copyleft pero las puertas son MIT»* **deja de valer para Open edX**. Ver **P55 (reencuadrado)** y **P61**. ✅ **Y la acción 2 del pase 29 queda cumplida ejecutando el servidor:** `tools/list` de `oneroster-ts` devuelve **132 tools** (72 lectura / 60 escritura), y el «164» por fin se explica — **132 operaciones distintas + 32 alias cruzados**, **cero supresión**, el 100 % de lo que el SDK tiene. Entra además `asfai-education` (**Apache-2.0**), la primera pieza con **cinco estándares 1EdTech a la vez**. Ver las tendencias **81**–**87**, los **gaps 52 (CERRADO)**, **53 (medido y corregido)** y **54**–**56**.
> **Pase 35 del 2026-10-02:** **la tabla pasa de 48 a 52 filas, y el pase se gana con un instrumento, no con un repo.**
> Esta base midió adopción con **estrellas** durante treinta y dos pases; el registro de paquetes publica **descargas por
> mes**, y las dos series se contradicen **en los dos sentidos**: `learninglocker` tiene **583 ★ y 0 descargas/mes**,
> mientras `TinCanPHP` tiene **88 ★ y 6.178 descargas/mes** y `oat-sa/extension-tao-testqti` tiene **8 ★, 844 versiones y
> un release de hace dos días**. 🔴 **Y la inversión llega a la fila que más importa:** el conector permisivo de LMS más
> grande de esta KB **ya no es `vishalsachdev/canvas-mcp`** (269 ★, cifra de tools inestable) sino
> **`bruchris/canvas-lms-mcp`** —**MIT, 8 ★, 317 commits, 62 versiones y 165 tools con cifra citable**—, que además trae
> **auditoría de accesibilidad** como categoría de herramientas. Entran también **Claw-ED** (**MIT**, 60 ★, 778 commits,
> el agente docente *local-first* que **P8** describía), **moodle-cli** (**MIT**, cuarta puerta de Moodle y primera del
> lado alumno, **sin token de administrador**) y **jbnu-lms-mcp** (**MIT**, Corea, **25 tools sólo lectura**, la primera
> infraestructura agéntica educativa de **origen APAC** de esta base). ✅ **Acción 2 del pase 32 cumplida y contra la
> expectativa: `coursecode` SÍ es la pieza de salida** — **15 tools** (9 lectura / 6 escritura) y
> **`coursecode_build` acepta `format` como enum `cmi5 | scorm2004 | scorm1.2 | lti`**, así que el empaquetado LMS está
> detrás de MCP. 🔴 **Gap 68 (nuevo):** la puerta oficial de Open edX publicó **12 releases en dos días (2026-07-24/25) y
> nada en los 70 siguientes**, todavía en `0.1.x` — hay que cotizar **mantenerla**, no consumirla. 🔴 **Gap 65 (confirmado, del pase 34):**
> `eur-lex.europa.eu` y `data.europa.eu` están **bloqueados (403 a CONNECT)**, así que el gap 56 **no se cierra desde este
> entorno** — pero la afirmación sube de fecha a **inciso: Artículo 113**. Ver las tendencias **107**–**114** y los
> patrones **P72**–**P75**.

> **Pase 32 del 2026-10-02:** **la tabla pasa a 48 filas, y el alta corta ocho pases sin agentes nuevos.** Entra [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) (**Apache-2.0**, 448 ★), que **destila el material de un docente en Agent Skills con trazabilidad a la fuente** — el eslabón que esta base declaraba vacío entre las skills escritas a mano y los tutores. El resto del pase es de **medición y de corrección**: 🔴 **el gap 57 cierra invirtiendo la conclusión del pase 31 — crear un curso en Open edX *sí* es una llamada HTTP** (`POST course_handler` → `_create_or_rerun_course`), **no vive en el árbol REST versionado** y pide **`is_content_creator(user, org)`, no `GlobalStaff`**; el *bootstrap* con curso plantilla de **P63** era innecesario. ✅ **El gap 59 cierra a favor:** el `sync` de biblioteca **preserva las personalizaciones del docente por omisión** (`override_customizations` = `False`). 🟢 **Aparece la primera puerta MCP de la capa de empaquetado:** `coursecode` (**MIT**, SCORM 1.2/2004 + cmi5 + LTI 1.3, **servidor MCP incorporado**) — y **apareció en el README, no en la descripción del paquete**, que es el canal que el barrido automático se saltea. 🔴 **Colisiones 5 y 6, las dos llamadas «xapi»:** `xapi-to` (cripto/Web3) y `xapi-python` (forex XTB) son **MIT y activas**, así que el filtro de licencia no las descarta. 🔴 **Y el gap 56 resuelve contra la propia argumentación EMEA de esta base:** educación es **Anexo III**, cuya fecha **se movió de 2026-08-02 a 2027-12-02**. Ver las tendencias **95**–**98** y los patrones **P65**–**P66**.
> **Pase 34 del 2026-10-02:** **la tabla se queda en 48 filas, y el candidato que la habría hecho 49 es el hallazgo del pase — por lo que NO es.** 🔴 **`quizlar/mcp-server` es un servidor MCP del dominio educativo, activo, con `LICENSE` MIT real… y sin una línea de código:** su `server.json` declara **`remotes` → `https://mcp.quizlar.app/mcp/`** detrás de una API key `sk-qz-<32>`, así que **la MIT licencia el manifiesto y la implementación es un servicio alojado propietario.** Es la **colisión 9** de esta base y es de **clase nueva** —no colisiona el nombre, colisiona **la superficie de la licencia**— y **completa el hallazgo del pase 33 en la dirección contraria: el registro no sólo tiene falsos negativos (`learnmcp-xapi`, invisible), también tiene falsos positivos (Quizlar, MIT sin código)** (tendencias **103** y **104**). ✅ **Acción 1 del pase 33 ejecutada: las cuatro ausencias del mapa por estándar auditadas con los dos instrumentos. Caliper, CASE y CEASN quedan CONFIRMADAS**; 🟢 **la de Open Badges era MITAD FALSA** — la puerta MCP sigue sin existir, pero **la implementación OB 3.0 que esta KB declaraba inexistente existe**: `Schroedinger-Hat/certo` (⚠️ **AGPL-3.0**, OB 3.0 + W3C VC + DIDs) y el **validador oficial `1EdTech/digital-credentials-public-validator` (Apache-2.0 ✅)**. ✅ **Gap 64 CERRADO en negativo con tres instrumentos: ningún LRS publica puerta MCP propia** — Docker Hub de `yetanalytics` (**6 imágenes, ninguna MCP**), `deps.edn`+README de `lrsql` (**0 menciones**), `ralph-malph` 5.0.1 (**14 extras, ninguno MCP**); **`learnmcp-xapi`, de un tercero, sigue siendo la única puerta.** 🟢 **Gap 63, mitad arquitectura, CIERRA por evidencia de archivo:** los tres `config/plugins/{lrsql,ralph,veracity}.yaml` dan **200** y `.env.example` declara `LRS_PLUGIN`; **la mitad fecha se reclasifica** — se probaron **8 rutas portadoras de versión y las 8 dan 404**, así que **no es el proxy: el proyecto no se versiona en su árbol** y ningún canal alcanzable puede fechar el `2.0.0`. 🟢 **Y aparece la TERCERA variante de la primitiva anti-bucle, la más barata: `learnmcp-xapi` frena en la CONFIGURACIÓN** (`RATE_LIMIT_PER_MINUTE=30`, `MAX_BODY_SIZE=16384`) — **frena solo y sin pedirle cooperación al cliente**, a diferencia de `coursecode` (tendencia **109**). ✅ **P69 DECIDIDO, y lo decide la licencia contra el número: `qtism/qtism` tiene ~10× la adopción (218.212 descargas, 3.104/mes) pero es GPL-2.0-only en LAS 293 RELEASES**, mientras `@longsightgroup/qti3-cli` es **MIT, cero dependencias de terceros y además el que se mueve más rápido** (41 releases desde 2026-05-21, última modificación **2026-10-01**). 🔴 **Y el hallazgo estructural que cambia cómo leer todo `intel/`: las fuentes primarias multilaterales son INALCANZABLES por clase — 0 de 11 dominios institucionales responden (`coe.int`, `unu.edu`, UNESCO, OCDE, BID, Banco Mundial, `ec.europa.eu`…) contra 5 de 5 registros comerciales.** Cada afirmación regulatoria de esta base se apoya en fuentes secundarias comerciales **por construcción del entorno**, y el **gap 56 se reclasifica de acción pendiente a límite de clase** (tendencia **106**, **gap 65**). Ver tendencias **103**–**106**, gaps **65**–**67** y patrones **P70**–**P71**.
> **Pase 33 del 2026-10-02:** **la tabla se queda en 48 filas, y por una vez eso es el hallazgo: la pieza que este pase fue a buscar ya estaba acá.** 🔴 **La mitad xAPI del gap 60 es FALSA, y la refutación estaba en cuatro archivos de esta base:** `DavidLMS/learnmcp-xapi` (**MIT**, 3 tools — **1 escribe, 2 leen**) es la puerta MCP de xAPI, está en esta tabla **desde el pase 6** y el mapa por estándar de abajo lo dice con la frase *«desde el pase 6»* escrita al lado. **El pase 32 declaró ausente algo que esta KB listaba como presente.** ✅ **La mitad QTI, en cambio, se CONFIRMA por un segundo instrumento independiente** — y es la única ausencia de esta base medida por dos instrumentos (tendencia **101**). 🔴 **La causa está medida y es el instrumento, no el rigor:** `learnmcp-xapi` **no está en ningún registro de paquetes** (PyPI **404**, npm **`total: 0`**; se instala desde el código) y `lrsql` se distribuye por **Docker Hub**, así que un barrido que arma candidatos en npm/PyPI/Packagist **no puede verlas** (tendencia **99**). **Regla nueva y barata: antes de declarar una ausencia, `grep` sobre estos ocho archivos.** 🟢 **Lo nuevo del pase es el estado, que es lo que decide si una dependencia entra en una propuesta:** `lrsql` (**Apache-2.0**) publicó **`v0.9.9` el 2026-10-01 — ayer**, con **112 tags** y seis releases en 2026; **Ralph** (**MIT**, *«Copyright (c) 2020-present France Université Numérique»*) está **vivo en `main` y parado en el registro** (último release **2024-07-11**, `[Unreleased]` activo) → **se instala desde git, no desde PyPI**. ✅ **`coursecode` medido en el artefacto publicado: 15 tools definidas / 15 casos de dispatch, sin aliasing ni supresión, y DOS escriben** — `_build`, con **`enum: ['cmi5','scorm2004','scorm1.2','lti']` en el `inputSchema`** (los cuatro estándares dejan de ser prosa del README y pasan a ser **contrato de tool**), y `_narration`, que escribe MP3 llamando a un **TTS pago**. 🟢 **Y trae la primitiva del pase 30 reinventada por otro mecanismo, con una asimetría que hay que cotizar:** `openedx-mcp` frena **en el servidor** (confirm token) y `coursecode` frena **en el contrato** (anotaciones MCP + `dryRun`) — **sólo el primero frena solo** (tendencia **102**). ✅ **Gap 51 CERRADO en negativo, medido en tres registros:** `opencase` da **7 / 404 / 665** con **cero del dominio** (cajas de skins, `opencage`, `opencast`) y `cass` da **26.726** en Packagist; el instrumento que funciona es **el nombre de la organización** (tendencia **100**). ⚠️ **Y una corrección de atribución:** el `LICENSE` de `learnmcp-xapi` dice **`Copyright (c) 2025 David Romero`** —una persona—, no una institución; el argumento de soberanía europea de EMEA conviene apoyarlo en **Ralph**, cuyo titular institucional sí está en el archivo de licencia. Ver las tendencias **99**–**102**, los **gaps 62**–**64** y los patrones **P67**–**P69**.
> **Pase 33 del 2026-10-02:** **la tabla se queda en 48 filas, y por una vez eso es el hallazgo: la pieza que este pase fue a buscar ya estaba acá.** 🔴 **La mitad xAPI del gap 60 es FALSA, y la refutación estaba en cuatro archivos de esta base:** `DavidLMS/learnmcp-xapi` (**MIT**, 3 tools — **1 escribe, 2 leen**) es la puerta MCP de xAPI, está en esta tabla **desde el pase 6** y el mapa por estándar de abajo lo dice con la frase *«desde el pase 6»* escrita al lado. **El pase 32 declaró ausente algo que esta KB listaba como presente.** ✅ **La mitad QTI, en cambio, se CONFIRMA por un segundo instrumento independiente** — y es la única ausencia de esta base medida por dos instrumentos (tendencia **109**). 🔴 **La causa está medida y es el instrumento, no el rigor:** `learnmcp-xapi` **no está en ningún registro de paquetes** (PyPI **404**, npm **`total: 0`**; se instala desde el código) y `lrsql` se distribuye por **Docker Hub**, así que un barrido que arma candidatos en npm/PyPI/Packagist **no puede verlas** (tendencia **107**). **Regla nueva y barata: antes de declarar una ausencia, `grep` sobre estos ocho archivos.** 🟢 **Lo nuevo del pase es el estado, que es lo que decide si una dependencia entra en una propuesta:** `lrsql` (**Apache-2.0**) publicó **`v0.9.9` el 2026-10-01 — ayer**, con **112 tags** y seis releases en 2026; **Ralph** (**MIT**, *«Copyright (c) 2020-present France Université Numérique»*) está **vivo en `main` y parado en el registro** (último release **2024-07-11**, `[Unreleased]` activo) → **se instala desde git, no desde PyPI**. ✅ **`coursecode` medido en el artefacto publicado: 15 tools definidas / 15 casos de dispatch, sin aliasing ni supresión, y DOS escriben** — `_build`, con **`enum: ['cmi5','scorm2004','scorm1.2','lti']` en el `inputSchema`** (los cuatro estándares dejan de ser prosa del README y pasan a ser **contrato de tool**), y `_narration`, que escribe MP3 llamando a un **TTS pago**. 🟢 **Y trae la primitiva del pase 30 reinventada por otro mecanismo, con una asimetría que hay que cotizar:** `openedx-mcp` frena **en el servidor** (confirm token) y `coursecode` frena **en el contrato** (anotaciones MCP + `dryRun`) — **sólo el primero frena solo** (tendencia **114**). ✅ **Gap 51 CERRADO en negativo, medido en tres registros:** `opencase` da **7 / 404 / 665** con **cero del dominio** (cajas de skins, `opencage`, `opencast`) y `cass` da **26.726** en Packagist; el instrumento que funciona es **el nombre de la organización** (tendencia **112**). ⚠️ **Y una corrección de atribución:** el `LICENSE` de `learnmcp-xapi` dice **`Copyright (c) 2025 David Romero`** —una persona—, no una institución; el argumento de soberanía europea de EMEA conviene apoyarlo en **Ralph**, cuyo titular institucional sí está en el archivo de licencia. Ver las tendencias **99**–**102**, los **gaps 62**–**64** y los patrones **P67**–**P69**.

> **Pase 39 del 2026-10-02:** **la tabla pasa de 55 a 63 filas y las ocho altas salen todas del mismo canal, que es el
> que esta KB no estaba usando: el REGISTRO DE PAQUETES consultado por el nombre del PROYECTO.** Es la acción 1 que dejó
> escrita el pase 38, y rinde ocho piezas que **treinta y ocho pases de barrido sobre GitHub nunca vieron**: `mcp-usc`
> (**MIT**, **91 tools**, EMEA), `DUTIC-mcp` (**MIT**, 12, **LATAM/Perú**), `mcp-brasil` (**MIT**, **13 tools de INEP**,
> **LATAM/Brasil**), `open-badges-mcp` (**MIT**, 16, **firma Ed25519**, APAC), `sisu-mcp` (MIT por campo de npm, 12, SIS
> finlandés), `armenian-national-library-mcp` (**MIT**, **23 de lectura**, primera pieza sobre **DSpace**),
> `ed-fi-sdk-mcp` (**Apache-2.0**, 11, **oficial del consorcio**) y `frappe-mcp-server` (ISC, 21). 🔴 **Y la alta más
> importante corrige una afirmación propia: `mcp-brasil` demuestra que educación NO es el dominio que falta en la capa
> MCP brasileña** (tendencia 114 y gap 69, corregidos). 🟢 **El patrón que aparece al mirar las tres regiones juntas:
> ya hay una pieza permisiva por región cuyo diseño encodea su estatuto** — FERPA en `bruchris/canvas-lms-mcp` (modo de
> seudonimización, recién medido), AI Act Anexo III §3 en `moodle-grading-mcp`, **LGPD** en `mcp-brasil` (tendencia
> **136**). Ver también la tendencia **137** (`preview_*` es el primer freno imponible **partiendo el conjunto de
> tools**), la **139** (un *helper* propio esconde las tools de un `grep` del SDK) y el **gap 79 CERRADO**.
> **Control de *slug* distinto corrido: 63 filas = 63 slugs distintos, 0 duplicados.**

> **Pase 37 del 2026-10-02:** **la tabla se queda en 51 filas / 49 repos distintos — sexto pase sin altas de agente — y el
> pase se gana midiendo lo que las 49 filas nunca tuvieron medido: si alguien sigue escribiendo código en ellas.**
> Con `git ls-remote` + `git fetch --depth 1` del sha de `HEAD` (cero cuota de API, cero autenticación) **las 49 quedaron
> fechadas por el commit de su rama por defecto**, y **49 de 49 respondieron: no hay una sola URL muerta en la tabla.**
> 🔴 **El resultado incómodo: 10 de 49 tienen la rama principal parada hace ≥ 6 meses y 3 hace ≥ 12 meses, y tres de esas
> diez son load-bearing en `compose/patterns.md`** — `DavidLMS/learnmcp-xapi` (**MIT**, `HEAD` **2025-08-29**, **13,1
> meses**, **una sola rama**, y es la pieza **más citada de esta base: 42 menciones**, puerta xAPI de **P4/P15/P67/P68/P69**),
> `trilogy-group/oneroster-ts` (**0BSD**, **2025-06-27**, **15,2 meses**, *«la superficie de tools más grande de toda esta
> base»*, **P58/P60/P64**) y `peancor/moodle-mcp-server` (**MIT**, **2026-02-22**, **7,3 meses**, la única pieza permisiva
> que **pone nota dentro de un LMS**, **P54/P55**). ✅ **Y cierra la mitad *fecha* del gap 63, que el pase 34 declaró
> incerrable** tras 8 rutas con 404: los tags estaban en `refs/tags` y el *fetch* los fecha —**`v2.0.0` de `learnmcp-xapi`
> = 2025-06-02**—; **no era un límite del entorno, era el instrumento equivocado.** 🔵 **La distinción que salva al
> instrumento de mentir: la actividad de bot no es mantenimiento** — `oneroster-ts` tiene un ref de hace 4 meses, pero son
> **4 ramas de dependabot + un regenerador de SDK, ninguna mergeada**, y `educhain` tiene su tip más nuevo en una rama
> **`claude/*`** sin mergear: **se fecha el tip de la rama por defecto, nunca el ref más nuevo** (**gap 72**).
> 🔴 **Corrección al pase 36:** `pykt-team/pykt-toolkit` **no está abandonado** — el pase 36 lo etiquetó *«cuatro años, es
> abandono»* leyendo sólo PyPI, y su `HEAD` es del **2026-09-22** con *feature commits* (`feat: add cgmkt model`, PR #305).
> **Está vivo en `main` y congelado en el registro: es la segunda aparición del patrón que esta base nombró con Ralph en el
> pase 33**, y ahora es verificable en vez de anecdótico. 🔴 **Y una corrección de método que evitó llenar esta KB de
> basura:** `api.github.com/rate_limit` da **200**, pero `api.github.com/repos/<cualquiera>` da **200 con un cuerpo que
> dice que el repo no está habilitado para esta sesión** — **compuerta de alcance, no bloqueo de red, y el error viene en
> el cuerpo y no en el código**, así que un probe que mire `%{http_code}` registra «funciona».
> 🔴 **Y el hallazgo de método que descalifica el verificador prescripto: `curl` sobre `github.com` devuelve **403 para
> TODO** —`torvalds/linux`, `moodle/moodle` y un slug inventado dan los tres **403**—, así que *«verificar la URL con
> `curl -sI`»* **no distingue un repo real de uno inexistente.** El discriminador es **`git ls-remote`**, con control
> negativo limpio (`fatal: could not read Username` para lo que no existe). **Las 49 filas de esta tabla quedaron
> verificadas por ese canal en este pase.** Ver las tendencias
> **124**–**131** y los gaps **72**–**77**.


> **Pase 43 del 2026-10-02:** 🔴 **la tabla NO crece, y esta vez el motivo está medido en vez de supuesto.** El barrido
> global obligatorio —cuatro búsquedas, con el año **calculado** (2026)— volvió a devolver **la capa genérica**
> (OpenClaw, OpenHands, opencode, CrewAI, LangGraph) y **material didáctico *sobre* AI**. Los **dos** únicos candidatos
> educativos que apareció, `SirhanMacx/Claw-ED` y `JuneYaooo/lineage-skill`, **ya estaban en esta base** (Claw-ED entró
> en el pase 35). 🔵 **Eso es información, no silencio: el canal «agente» está saturado para esta industria**, y las altas
> de los últimos pases vinieron todas del canal de **conector y de estándar**.
> **El hallazgo de agente del pase existe y se deja FUERA de la tabla a propósito:** `issuebadge/mcp-server`
> (**MIT**, *Copyright (c) 2025-2026 IssueBadge*, TypeScript) es **la primera puerta MCP de emisión de credenciales** que
> ve esta KB — **4 tools** (`validate_key`, `get_all_badges`, `issue_badge`, y `create_badge` sólo en stdio), remoto por
> `streamable-http` con OAuth 2.1 o local por `npx`, además **plugin de Claude Code** con *skill* del flujo
> *listar → confirmar → emitir*, widget **MCP Apps** en `issue_badge`, y servidor remoto **auto-hospedable**.
> 🔴 **Dos razones para no promoverlo, las dos con número o con hecho:** **(1) 0 ★ y 4 commits** — madurez sin evidencia;
> **(2)** la emisión **depende de `app.issuebadge.com` y de una API key del proveedor**, así que **no implementa Open
> Badges 3.0 como estándar** y **no sustituye nada en P84**. Se registra con la cifra a la vista en
> `agents/trending.md` y en la tendencia **165**, para que el próximo pase lo **vuelva a medir** en vez de heredar un
> juicio. 🔵 **Y el barrido por SDK de la capa de estándares dio una sola alta real** —`Simon-Initiative/lti_1p3`
> (**MIT**, Elixir, Carnegie Mellon: **Platform y Tool**, no sólo Tool)— que va a `repos/foundations.md` porque es
> biblioteca, no agente. Ver las tendencias **157**–**165** y los patrones **P93**–**P95**.

> **Pase 44 del 2026-10-02:** **la tabla NO crece, y el barrido lo midió en vez de suponerlo: segundo pase consecutivo
> con cero altas de agente.** Las cuatro búsquedas globales obligatorias, con el año **calculado** (2026), volvieron a
> devolver **la capa genérica** (openclaw 385.407 ★, dify 151.639, browser-use 108.128, AutoGen 60.284, Flowise 55.226)
> y **material didáctico *sobre* AI** — ni un agente educativo nuevo. 🔵 **Eso ya no es una observación, es una
> propiedad medida del canal: las altas de los últimos pases vinieron todas del eje conector y del eje estándar, y el
> eje agente está saturado para esta industria.**
> 🔴 **Y el control de *slugs* distintos del pase 36 encontró un error de aritmética propio: la tabla tiene 66 filas,
> no las 63 que esta base viene publicando** — **61 slugs de GitHub, los 61 distintos, 0 duplicados**, más **5 entradas
> de registro** (`openedx-mcp` y `tutor-contrib-openedxmcp` en PyPI; `@ink-waffle/sisu-mcp`, `ed-fi-sdk-mcp` y
> `frappe-mcp-server` en npm) que no tienen slug de GitHub y se cuentan igual. **El control que importa —ninguna fila
> repetida, ninguna fila de encabezado o de ejemplo entre los datos— pasa limpio; el que fallaba era la suma.**
> **`issuebadge/mcp-server` se re-midió, como el pase 43 pidió, y SIGUE FUERA de esta tabla.** Ahora tiene **v2.1.0,
> 1.106 líneas de TypeScript, 168 casos de test y sólo 2 dependencias**, con `LICENSE` **MIT** real — pero **sigue en
> 4 commits**, **la emisión sigue dependiendo de `app.issuebadge.com` + API key del proveedor**, **no implementa Open
> Badges 3.0** y por lo tanto **no sustituye nada en P84**. 🔴 **Dos hallazgos nuevos del re-medido: no está en npm**
> (`Not found`, aunque declara `bin`), así que es **invisible al barrido por registro** igual que `learnmcp-xapi`; y
> **aporta la quinta variante de primitiva anti-bucle, la más débil de las cinco, porque delega el freno en la API del
> proveedor y su valor por omisión lo anula** — `idempotency_key` se genera por llamada, así que **un reintento sin
> arrastrar la clave emite un segundo certificado**. La primitiva **corregida** se adopta en **P97**; la pieza, no.
> Ver las tendencias **166**–**174** y los patrones **P96**–**P98**.

> **Pase 45 del 2026-10-02:** **la tabla se queda en 66 filas — TERCER pase consecutivo con cero altas de agente, y el
> barrido lo volvió a medir en vez de suponerlo.** Las cuatro búsquedas globales obligatorias, con el año **calculado**
> (2026), devolvieron **la capa genérica** (openclaw 385.407 ★, dify 151.639, browser-use 108.128, Mem0 62.735,
> AutoGen 60.284, Flowise 55.226) y **material didáctico *sobre* AI**. Los cinco candidatos se evaluaron uno por uno y
> **ninguno entra**: **Hermes Agent** (Nous Research, MIT, ~180k ★) es **agente genérico**, no educativo;
> `ai-engineering-from-scratch` (#1 de GitHub Trending en mayo) es **material sobre AI**; **OpenEduCat** ya está en
> `verticals/solutions.md`; y *free-ai-agents-resources*, *Awesome LLM Apps* y **Semantic Kernel** son listas y
> orquestadores genéricos. 🔵 **Tres pases midiendo lo mismo deja de ser observación y pasa a ser propiedad del canal:
> el eje agente está saturado para esta industria, y las altas vienen del eje conector y del eje estándar.**
> 🔴 **El trabajo del pase está en re-auditar lo que esta base ya había publicado, y encontró el defecto donde el pase
> 44 dijo que había que buscarlo.** Corridos sobre `compose/code/unitime-mcp-gate/` los cuatro controles del pase 44
> (**gap 93, CERRADO**): **(a) pasa — las 15 rutas de UniTime son literales de `@Service("/api/x")`**, lo contrario de
> SEB Server donde eran **0 de 30**; **(c) y (d) pasan**; 🔴 **(b) FALLABA, y por un motivo que el pase 42 no podía
> ver: `getName()` NO es la ruta.** `ApiServlet` hace `getBean(servletPath + pathInfo)`, así que **la ruta es el nombre
> del bean de Spring**; `getName()` sólo alimenta `getCacheMode()`. Los 15 coinciden hoy, **así que el dato era
> correcto y el método no** — y el `/api/` del manifiesto era **una f-string de Python**, cuando el `<url-pattern>` es
> `/api/*` y `pom.xml` envía `<warName>UniTime</warName>`: **la URL desplegada es `/UniTime/api/<conector>`.**
> 🔴 **Y apareció un QUINTO control que esta base no tenía, porque es de la abstracción de la puerta y no del
> extractor: el verbo HTTP no es la frontera de escritura.** `ScriptConnector.doGet` despacha por parámetro de query y
> dos ramas escriben — `?script=` **llama `doPost` (un GET ejecuta un script del servidor)** y `?delete=` borra un ítem
> de la cola. **La partición lectura/escritura por verbo, que es el corazón de las DOS puertas de esta KB, no es sólida
> para UniTime**; la política ya negaba `script` por nombre, así que **el resultado era correcto y el motivo
> documentado no lo era**. Desde este pase el rechazo es un **piso y no una política**: se niega con `-32601` **incluso
> si un operador lo nombra en `UNITIME_ALLOW`**. **46 aserciones en verde** (eran 23). Ver las tendencias
> **175**–**177** y el patrón **P100**.
> 🟢 **Y la medición del Artículo 50(2) sobre esta tabla contradice lo que el pase 44 predijo** (**gap 91, CERRADO**).
> **33 de las 66 filas —el 50 %, exactamente la mitad— ponen contenido sintético delante de un alumno o de un docente** (🔴 **cifra corregida en el pase 56: se publicaba «32 / 48 %» porque la composición escrita a mano `24 gen + 7 gen-ind + 1 gen-cond` omitía la fila `pack`; afirmado ahora por `compose/code/aiact-50-2-exposure/test_exposure.py`, 11/11**), y de los **33** repos
> barridos (**24.202 archivos**, **26 manifiestos**) hay 🔴 **0 artefactos de marcado y 0 dependencias de marcado**.
> Pero el pase 44 esperaba *«ninguna»* y **hay una**: 🟢 **`OpenTutor` emite `{"generated": true, "source_labels":
> ["generated"]}` hacia el cliente**, con valor por omisión `True` y declarado en el esquema de la API — **la única
> bandera legible por máquina de contenido generado en toda esta tabla**. 🔴 **Y no alcanza:** es un campo **al lado**
> del contenido, marca **el turno y no el tramo**, y **no está firmado**. La granularidad que le falta está en **otra
> fila** —`lineage-skill`, con un vocabulario cerrado de 9 valores por afirmación, **4 de los 9 «esto lo produjo el
> modelo»**— y **ninguna de las dos sabe de la otra**. Ver la capa nueva al final de este archivo, las tendencias
> **180**–**182** y el patrón **P99**.

## 🔵 Clasificación por canal de credencial (P121/P123) — pase 53, **instrumento corregido en el pase 54**

> 🔴 **El control negativo que el pase 53 declaró FALLA, y por eso el instrumento cambia.** El pase 53
> escribió: *«`toshieji/moodle-grading-mcp` y `Dymayo/moodler-mcp` son el control negativo natural: esta
> base ya documentó que usan web service token, así que si salieran (b) el instrumento está mal.»*
> **`toshieji` salió (a) y `Dymayo/moodler-mcp` salió (b).** El instrumento estaba mal, y el defecto
> tiene nombre: **P121 leía el TIPO de la credencial y hay que leer su PROCEDENCIA.**
>
> 🔵 **La corrección (P123): el canal son DOS campos independientes, no una letra.**
> **Artefacto** = qué guarda la pieza (cookie de sesión · token de web service · credencial primaria ·
> app OAuth registrada). **Emisor** = quién lo emitió (TI de la institución · la propia sesión del
> alumno · el alumno tipeando su contraseña). `moodler-mcp` guarda un **token de web service** —
> artefacto de clase (a)— **que mintió su propia sesión SSO del alumno**: emisor de clase (b).
> ⚠️ **Una fila con una sola letra no puede expresar eso, y la letra que habría puesto es la equivocada.**
>
> 🔴 **Y el corolario que invierte la intuición de cualquier filtro de componentes: la pieza con MENOS
> variables de credencial en su configuración no es la más segura — es la que se consigue la credencial
> sola.** `Dymayo/moodler-mcp` declara **una** variable, `MOODLE_URL`, y **ninguna credencial**,
> precisamente porque abre un navegador y mina el token él mismo. **Un audit de `.env` lo aprueba.**

### Las dos clases nuevas, y por qué no alcanzaban las tres del pase 53

**b4 — token mintado por la sesión del propio alumno.** La pieza abre un navegador real, la persona
completa el SSO con sus factores (passkey/2FA incluidos), y entonces la pieza **pide a Moodle un token
de web service de app móvil** y lo guarda en disco. 🔵 **No evade la emisión de tokens: usa el
endpoint oficial.** ⚠️ **Lo que evade es otra cosa, y casi nadie la administra como control de acceso
de agentes: que el servicio web móvil del sitio esté habilitado.** 🔴 **Y es peor que b1 en
revocación** —b1 guarda una cookie que muere con la sesión; b4 se queda con un **bearer portable y
durable**— **y a la vez invisible donde b2 es visible**, porque en el archivo de configuración no hay
ninguna credencial que mirar.

⚠️ **El nombre canónico del ajuste de Moodle que gobierna b4 NO se pudo verificar en este pase:**
`docs.moodle.org` devuelve **`EGRESS_BLOCKED`** (gap 92, sexto canal). Lo que sí está medido es la cita
de las dos piezas: *«requests a mobile-app web service token from Moodle and stores it locally»*
(`moodler-mcp`) y *«Writes use the site's web-service token, not the browser; file uploads require the
site's mobile web service to permit uploads»* (`@ink-waffle/moodle-mcp`). **Se publica la cita, no el
nombre del ajuste.**

### La tabla, con artefacto y emisor separados

**Lo que se midió este pase (acción 1 del pase 53): 11 piezas leídas por WebFetch, 9 con canal
determinable, 2 no determinables.** Reparto del pase: **5 (a) · 2 (b, las dos b4) · 2 no aplica ·
2 no determinable.**

| Pieza | Clase | Artefacto | Emisor | Región |
|---|---|---|---|---|
| [`Dymayo/moodler-mcp`](https://github.com/Dymayo/moodler-mcp) | 🔴 **b4** — *el control negativo que falló* | token de web service de app móvil, en disco | 🔴 **la sesión SSO del propio alumno** (`login_to_moodle` abre Chrome/Chromium) | sin región declarada |
| [`@ink-waffle/moodle-mcp`](https://github.com/ink-waffle/moodle-mcp) | 🔴 **b4 + b3** | token de web service en `~/.moodle-mcp/config.json` (*«treat as a password file»*) | 🔴 **la sesión del alumno por CDP**, y en sitios sin SSO **la contraseña pasada a `moodle_connect`** | sin región declarada |
| [`mtgibbs/canvas-lms-mcp`](https://github.com/mtgibbs/canvas-lms-mcp) | 🟢 **(a)** | `CANVAS_API_TOKEN` + `CANVAS_BASE_URL` | la institución (*Account → Settings → Approved Integrations → New Access Token*) | sin región declarada |
| [`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp) | 🟢 **(a)** — *control negativo que SÍ se sostiene* | `MOODLE_TOKEN` | la institución (*Site administration → Server → Web services → Manage tokens*) | 🟢 **APAC** (Japón — README bilingüe JA/EN, 800 caracteres CJK medidos por rango Unicode; **ubicada en el pase 55**, la celda decía *«sin región declarada»*) |
| [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🟢 **(a)** | `MOODLE_TOKEN` + `MOODLE_URL` | la institución (*Plugins → Web services → Manage tokens*). ⚠️ **AGPL-3.0** | sin región declarada |
| [`gafapa/moodle-core-cli`](https://github.com/gafapa/moodle-core-cli) | 🟢 **(a)** | `MOODLE_TOKEN` o `--token` | la institución, y 🟢 **recomienda servicio externo dedicado con sólo las funciones necesarias** | sin región declarada |
| [`redbeard-26/asfai-education`](https://github.com/redbeard-26/asfai-education) | 🟢 **(a)** | app OAuth web registrada (`ASFAI_GOOGLE_CLASSROOM_CLIENT_ID`/`_SECRET`) | el administrador del Workspace, que puede negarla | sin región declarada |
| [`Cicatriiz/openedu-mcp`](https://github.com/Cicatriiz/openedu-mcp) | ⚪ **no aplica** | ninguno — OpenLibrary, Wikipedia, Dictionary, arXiv | 🔵 **no es cliente de LMS/SIS: no hay pregunta de credencial** | sin región declarada |
| [`paulocymbaum/ed-tech-system-mcp`](https://github.com/paulocymbaum/ed-tech-system-mcp) | ⚪ **no aplica** | `SUPABASE_URL` + `SUPABASE_SERVICE_ROLE_KEY` de su **propia** base | 🔵 **sistema autónomo; la cookie de la propia app no es la de un tercero** | sin región declarada |
| [`owentaylor/canvas-mcp`](https://github.com/owentaylor/canvas-mcp) (`@owen-x-tech/canvas-mcp`) | ⚫ **no determinable** | — | **repo 404**: 10 sondas (`main`/`master` × 5 nombres de README) en `raw`, reconfirmado este pase | — |
| [`imazhar101/mcp-canvas-server`](https://github.com/imazhar101/mcp-canvas-server) | ⚫ **no determinable** | — | **repo 404**: 10 sondas en `raw`, reconfirmado. Ya excluido por licencia ausente (gap 232) | — |

⚠️ **Nota sobre la lista de la acción 1 del pase 53: nombraba `@ink-waffle/moodle-mcp` como «fila de
`agents/top.md`» y no lo es** — el alcance `@ink-waffle` sólo tiene fila por `sisu-mcp`. Se clasificó
igual, porque es un cliente de LMS real y medido, y porque es la segunda de las dos piezas b4.

### 🔴 La hipótesis falsable del pase 53 cae en el medio declarado, y el predictor bueno es OTRO

El pase 53 escribió: *«si la proporción 5/11 se sostiene en el resto, la clase (b) es ~45 % del
ecosistema; si cae por debajo de ~15 %, lo que este pase midió fue un sesgo de selección.»**
**Medido: 2 de 7 en este pase (28,6 %); acumulado 7 de 18 (38,9 %).** 🔵 **Ni se sostiene el 45 % ni
cae del 15 %: cae exactamente en la banda que el pase 53 no interpretó, así que la hipótesis no decide
nada — y el pase 53 tenía razón a medias sobre su propio sesgo.**

🟢 **Lo que sí se midió, y es un predictor accionable en vez de un porcentaje:** **el canal correlaciona
con el ALCANCE de la pieza, no con la plataforma.**

| Tipo de pieza | (a) | (b) | Lectura |
|---|---|---|---|
| **Nombrada por una institución** (`DUTIC-mcp`/UNSA, `jbnu-lms-student`/JBNU, `mcp-usc`/USC) | 0 | **3 de 3** | 🔴 **Si el repo lleva el nombre de una universidad, asumí (b) hasta probar lo contrario** |
| **Conector genérico de producto** (nombra Canvas o Moodle, no una escuela) | **11 de 13** | 2 de 13 | 🟢 Y **las 2 excepciones son exactamente las dos que mintan su propio token** (b4) |

🔵 **Por qué el mecanismo lo explica:** una pieza de una sola institución no puede pedirle a esa
institución que le emita nada —no tiene interlocutor— así que toma el camino de la sesión. Un conector
de producto se distribuye a quien sí puede pedir un token. **La elusión sigue siendo el camino de menor
resistencia, no mala fe** (pase 53), y ahora se sabe **dónde** hay menos resistencia.

### Las cinco clases, en orden de lo que cuesta defenderlas

**(a)** credencial emitida por la institución, que puede negarla · **b1** monta la sesión conservando
los factores (cookie + `sesskey` en el llavero del SO, sólo lectura) · **b4** 🔴 **token oficial mintado
por la sesión del alumno — artefacto (a), emisor (b), invisible en un audit de configuración** ·
**b2** pegado de cookie desde DevTools · **b3** 🔴 usuario y contraseña reutilizables en texto plano.

⚠️ **Falso positivo a evitar, medido en el pase 53 y reconfirmado acá con dos piezas:** la cookie de
sesión de la **propia** aplicación no es la de un LMS ajeno — P121 pregunta por el control de un
**TERCERO** (`paulocymbaum/ed-tech-system-mcp` y `Cicatriiz/openedu-mcp` quedan afuera por eso).

### 🔵 Un eje distinto que apareció solo, y no es de credencial: la declaración de integridad

`@ink-waffle/moodle-mcp` somete trabajo calificado (`moodle_assignment_submit`, `moodle_quiz_*`) y
**se niega explícitamente a falsificar la declaración de integridad académica**: *«no-draft assignments
requiring [a submission statement] must be completed in Moodle's UI because the save API cannot record
acceptance»*, y advierte que *«starting/finishing a quiz or lesson may consume a graded attempt»*.
🟢 **Es la postura correcta y hay que saber reconocerla**, porque es independiente del canal de
credencial: la misma pieza es **b4+b3** en credencial y **ejemplar** en integridad. ⚠️ **Dos ejes, dos
veredictos — y el pase 55 debería clasificar la tabla por el segundo.**

### Las filas que el pase 53 ya había clasificado (esquema de tres valores, se conservan)

| Pieza | Clase | Credencial que decide | Región |
|---|---|---|---|
| [`JOSETRA44/DUTIC-mcp`](https://github.com/JOSETRA44/DUTIC-mcp) | 🔴 **b3** | `DUTIC_SISACAD_USER` + `DUTIC_SISACAD_PASSWORD` + `DUTIC_ENCUESTA_*`, y un sistema *«sin CAPTCHA»* | **LATAM** (Perú — UNSA) |
| [`bunizao/moodle-cli`](https://github.com/bunizao/moodle-cli) | 🔴 **b2** | `MOODLE_TOKEN` = valor de la cookie `MoodleSession` | sin región declarada |
| [`xmike04/canvas-student-mcp`](https://github.com/xmike04/canvas-student-mcp) | 🔴 **b2** | `CANVAS_COOKIE` extraída de DevTools | **North America** |
| [`PabloPC05/mcp-usc`](https://github.com/PabloPC05/mcp-usc) | ⚠️ **(a) + b2** | `USC_MOODLE_TOKEN` **o** `MoodleSession` vía Entra+MFA | **EMEA** (España — USC) |
| [`moon0825/jbnu-lms-student`](https://github.com/moon0825/jbnu-lms-student) | ⚠️ **b1** | `MoodleSession` + `sesskey` en DPAPI/Keychain, **sin contraseña ni passkey** | **APAC** (Corea — JBNU) |
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | 🟢 **(a)** | `CANVAS_API_TOKEN`, o `oauth_brokered` con client id/secret registrados | sin región declarada |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **(a)** | `CANVAS_API_TOKEN` + `CANVAS_API_URL` | **North America** |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | 🟢 **(a)** | `CANVAS_API_TOKEN` + `CANVAS_DOMAIN` | sin región declarada |
| [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) | 🟢 **(a)** | `MOODLE_WS_TOKEN` — *«No cookie auth, no web scraping, no direct DB access»* | sin región declarada |
| [`NiccoloSalvini/mcp-moodle-teacher`](https://github.com/NiccoloSalvini/mcp-moodle-teacher) | 🟢 **(a)** | `MOODLE_TOKEN` del web service móvil | sin región declarada |
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🟢 **(a)** | `MOODLE_API_TOKEN` de administración del sitio | sin región declarada |
| [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | ⚪ **no aplica** | OAuth del usuario a su **propia** cuenta de Google | sin región declarada |

⚠️ **Denominador acumulado y honesto (P107):** **18 clientes de LMS/SIS con canal determinable** en dos
pases (11 del pase 53 + 7 del 54), **7 en clase (b)**, **2 no determinables por repo 404**, **3 fuera
del eje por no ser clientes de un tercero**. 🔴 **Las filas de este archivo que todavía no se miraron
por este eje están en la acción 1 del pase 55**, y el barrido que las enumeraba quedó **negado por
`[Credential Exploration]`** (ver `intel/trends.md`).

### 🔵 El SEGUNDO eje, clasificado — la declaración de integridad académica (acción 1 del pase 54, pase 55)

**El pase 54 encontró este eje de costado y pidió clasificar la tabla por él. Se clasificaron las seis
piezas que ESCRIBEN en un LMS, leyendo cada README de primera mano por `raw.githubusercontent.com`.**
🔴 **El resultado invierte la intuición de cualquier filtro de componentes y es el hallazgo del pase.**

**Las cuatro clases** (del enunciado del pase 54): **(1)** no escribe · **(2)** escribe con confirmación
previa · **(3)** escribe trabajo calificado y respeta la declaración · **(4)** escribe trabajo calificado
y la elude.

| Pieza | Clase de integridad | Qué escribe | Cita verbatim que lo decide | Clase de credencial (P123) |
|---|---|---|---|---|
| [`@ink-waffle/moodle-mcp`](https://www.npmjs.com/package/@ink-waffle/moodle-mcp) | 🟢 **(3)** — rehúsa, mecánico | `moodle_assignment_submit`, `moodle_quiz_*` | *«no-draft assignments requiring [a submission statement] must be completed in Moodle's UI because the save API cannot record acceptance»* | 🔴 **b4+b3** |
| [`PabloPC05/mcp-usc`](https://github.com/PabloPC05/mcp-usc) | 🟢 **(3)** — delega, normativo | 20 operaciones con efecto, incluidas `submit_assignment`, `start_quiz`, `save_quiz_answers`, `finish_quiz` | *«`submit_assignment` puede cerrar la edición del borrador y **debe respetar la declaración de entrega** que muestre Moodle»* + *«Toda escritura sigue dos llamadas»* | ⚠️ **(a) + b2** |
| [`Dymayo/moodler-mcp`](https://github.com/Dymayo/moodler-mcp) | 🟢 **(3)** — prohibición explícita | `submit_assignment` y 5 escrituras de alumno; `save_assignment_grade` y `grant_extension` del lado docente | *«This includes using an LLM to generate answers for quizzes, assignments, or exams accessed through this tool, submitting AI-generated work as your own, or any activity that violates your institution's academic integrity policy»* | 🔴 **b4** |
| [`JOSETRA44/DUTIC-mcp`](https://github.com/JOSETRA44/DUTIC-mcp) | 🟢 **(2)** — y la más estricta del conjunto | `dutic_encuesta_fill_all`, `dutic_encuesta_submit` — **encuesta de evaluación DOCENTE, no trabajo calificado** | *«Todo simula por defecto; enviar exige `--enviar` **y** `--si-es-irreversible`»* · *«sin política configurada, la herramienta se niega a completar en vez de inventarse una valoración»* · *«Nunca se reenvía algo ya llenado»* | 🔴 **b3** |
| [`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp) | 🟢 **(2)** — lado docente, con divulgación | `save_grade_draft`, *«the only writer»* | *«Grades are written as `workflowstate=readyforreview` (graded but **UNRELEASED**). This server **never releases**»* · *«An AI-assistance disclosure footer is appended if missing»* | 🟢 **(a)** |
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🔴 **sin guarda** — y no cae en ninguna de las cuatro | `provide_assignment_feedback`, `provide_quiz_feedback` — **escribe la nota autoritativa** | **No hay cita: el README no trae confirmación, ni borrador, ni divulgación, ni texto de integridad** | 🟢 **(a)** — token de administración del **SITIO** |

#### 🔴 Lo que hay que leer de esta tabla antes de proponer cualquier fila

🟢 **La clase (4) NO existe en las seis, y el pase 54 pidió decirlo si pasaba: el ecosistema se
autolimita donde la licencia no lo obliga.** 🔴 **Pero el hallazgo que manda es la ANTI-correlación: las
tres piezas que someten trabajo calificado son las tres de peor procedencia de credencial, y las tres
traen salvaguarda. La pieza de credencial más limpia es la única sin ninguna.** ⚠️ **Consecuencia
operativa, y es la que cambia un *checklist* de componentes: un filtro que ordene por higiene de
credencial —el filtro natural, el que cualquiera escribiría— selecciona A FAVOR de la escritura de notas
sin guarda.** Ver **P127**.

⚠️ **Y el esquema de cuatro clases tiene un agujero que este pase declara en vez de tapar: es
estudiante-céntrico.** `peancor` no somete trabajo del alumno, escribe **el juicio sobre** él, y por eso
no entra en ninguna clase. 🔵 **El esquema del lado docente es la acción 1 del pase 56** (**P129**).

🔵 **La diferencia entre las dos posturas de clase (3) no es de grado y conviene saber nombrarla:
`@ink-waffle` REHÚSA por mecanismo** (la API no puede registrar la aceptación, así que no escribe)
**y `mcp-usc` DELEGA por norma** (*«debe respetar»*). **Un verbo normativo no es un control.**

🟢 **El activo reusable del pase, y vale más allá de educación: el protocolo de dos llamadas de
`mcp-usc`.** Los `preview_*` **no escriben** — validan y devuelven `confirmation_token`; *«Los tokens
viven solo en memoria, caducan a los cinco minutos y son de un solo uso»* y *«Cambiar texto,
destinatario, archivos, respuestas, intento o cualquier otra entrada invalida la confirmación»*. **Es el
mejor control de escritura medido en esta KB y hoy está atado a una universidad.**

🔴 **CORRECCIÓN DEL PASE 56 a este mismo párrafo, y es la que manda en el pase:** *«el mejor control de
escritura medido en esta KB»* **sigue siendo cierto como ingeniería y queda DEGRADADO como recomendación**,
porque el modelo de amenaza de educación lo atraviesa. **La pieza más adoptada de esta capa
—`vishalsachdev/canvas-mcp`, 272 ★— publicó un *security release* que lo dice en primera persona:**
*«Instructions a student plants in course content can steer an instructor's assistant, and a confirmation
token cannot stop that because the assistant can redeem its own token»*. 🔵 **El atacante no es el
docente distraído: es el alumno, escribiendo en el contenido del curso que el asistente del docente va a
leer. Y el que redime el token es el propio asistente, así que la confirmación no es una segunda
autoridad — es la misma autoridad dos veces.** ⚠️ **Su remedio no es confirmar mejor, es que la
herramienta de escritura NO EXISTA:** `ALLOWED_WRITE_TOOLS` *«removes every write tool the operator has
not allowed at startup, so it cannot be listed or called»*. Ver **P132**.

## 🧑‍🏫 Capa de escritura del lado DOCENTE — el agujero de P129, cerrado, y la hipótesis del pase 55 cae en su rama mala (acción 1 del pase 56)

**El esquema de credencial de los pases 53–55 es estudiante-céntrico: clasifica quién SOMETE trabajo.
Esta capa clasifica quién escribe EL JUICIO sobre el alumno**, que es donde el pase 55 encontró la única
pieza sin guarda. **Ocho piezas de esta base escriben nota, devolución o estado académico. Las ocho
leídas por `raw.githubusercontent.com` en este pase, una por una, y clasificadas por el esquema que el
pase 55 prescribió.**

### 🔴 La hipótesis falsable del pase 55 cae, y cae en la rama que obliga a trabajar

**El pase 55 escribió la prueba de antemano:** *«si ≥ 3 de las 8 escriben borrador no liberado,
"borrador + liberación humana" ES la norma emergente de la categoría; si `toshieji` queda solo, la
categoría no tiene norma y el requisito hay que escribirlo nosotros»*.

🔴 **`toshieji` queda solo: 1 de 8.** **No hay norma emergente.** 🔵 **Consecuencia comercial directa, y
es la más vendible del pase: el requisito «la nota la libera un humano» no se puede tercerizar al
ecosistema porque el ecosistema no lo tiene. Lo escribe Globant, y eso lo vuelve un diferencial
redactable en una propuesta en vez de un supuesto.**

### Las ocho piezas, con la cita que decide cada celda

| Pieza | Licencia | ★ | Región | Qué escribe | Clase | Guarda medida | Divulgación AI |
|---|---|---|---|---|---|---|---|
| [`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp) | **MIT** | 0 | 🟢 **APAC** (800 car. CJK) | `save_grade_draft` — *«the only writer»* | 🟢 **T2** | *«Grades are written as `workflowstate=readyforreview` (graded but UNRELEASED). This server never releases»* + *«No student notification»* + allowlist de cursos y `MOODLE_ALLOW_WRITE=1` | ✅ **sí** — *«An AI-assistance disclosure footer is appended if missing»* |
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** | 43 | ⚠️ no declarada | `provide_assignment_feedback`, `provide_quiz_feedback` | 🔴 **T4** | 🔴 **ninguna** — cero menciones de confirmación, borrador o liberación | 🔴 **ninguna** |
| [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) | **MIT** | 1 | ⚠️ no declarada | `calificar_manualmente` | 🔴 **T4** | 🔴 **ninguna sobre la nota** — el `publicar_preview`→`confirmar_preview` existe, pero es del grupo de **contenido**, no del *gradebook* | 🔴 **ninguna** |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | **272** | 🟢 **North America** (*University of Illinois Urbana*) | `bulk_grade_submissions`, `grade_submission_with_rubric` | 🔴 **T4** | ⚠️ `ALLOWED_WRITE_TOOLS` en **arranque** (control del operador), **sin confirmación por llamada en la nota**; el `confirmation_token` es de los **siete tools de borrado**, no del *grading* | 🔴 **ninguna** |
| [`Dymayo/moodler-mcp`](https://github.com/Dymayo/moodler-mcp) | **MIT** | 0 | ⚠️ no declarada | `save_assignment_grade`, `grant_extension` | ⚠️ **T3′** | *«Tools behind a disabled flag are not registered at all»* + *«Destructive writes ask for confirmation … otherwise an explicit `confirm=true`»* | 🔴 **ninguna como mecanismo** — tiene política de integridad en prosa, que no es lo mismo |
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | **MIT** | 8 | ⚠️ no declarada | `grade_submission`, `comment_on_submission` | ⚠️ **T3′** | `destructiveHint: true` → prompt del host; 🟢 **y la honestidad más citable de la capa:** *«`confirm` is reserved but not implemented. Setting it is a startup error naming it as such, so it can never be mistaken for protection you do not have»* | 🔴 **ninguna** |
| [`NiccoloSalvini/mcp-moodle-teacher`](https://github.com/NiccoloSalvini/mcp-moodle-teacher) | **MIT** | 0 | ⚠️ no declarada | `grade_submission` (*«mark and written feedback»*), `mark_attendance` | ⚠️ **T3′** | *«every tool that changes Moodle says so and asks for confirmation»* | 🔴 **ninguna** |
| [`openedx-mcp`](https://pypi.org/project/openedx-mcp/) (oficial) | 🔴 **AGPL-3.0** | — (PyPI 0.1.5) | Global | certificados (generar/regenerar/**invalidar**), `students/reset-attempts` | ⚠️ **T3′** | 🟢 **la más fuerte de las ocho: dry-run + confirm token atado a HUELLA DEL PAYLOAD, rate limit por (key, tool), re-chequeo de autoridad vivo y auditoría append-only previa a la escritura** | 🔴 **ninguna** |

### 🔴 El reparto, y el esquema de cuatro clases se rompe igual que el de tres del pase 54

| Clase | Definición del pase 55 | Cuántas |
|---|---|---|
| **T1** | no escribe juicio | **0 de 8** |
| **T2** | escribe borrador que un humano libera | 🟢 **1** (`toshieji`) |
| **T3** | escribe en firme **con** divulgación de asistencia AI | 🔴 **0 de 8** |
| **T4** | escribe en firme, **sin** divulgación y **sin** confirmación | 🔴 **3** (`peancor`, `MarcosNahuel`, `vishalsachdev`) |
| ⚠️ **T3′** | **la clase que el esquema no nombra:** en firme, **con** confirmación, **sin** divulgación | ⚠️ **4** — *la pluralidad* |

⚠️ **El esquema de cuatro clases del pase 55 tiene su propio agujero, y es simétrico al de P129 que vino
a tapar: T3 exige divulgación y T4 exige ausencia de confirmación, así que la combinación más común de
la capa —confirmar sí, divulgar no— no entra en ninguna de las cuatro.** 🔵 **Se agrega **T3′** y se
dice de dónde salió, en vez de forzar cuatro casilleros sobre ocho piezas** (**P133**). 🟢 **Tercer pase
consecutivo en que un esquema de clasificación de esta base resulta insuficiente al primer contacto con
los datos (3→5 en el 54, 4→5 acá): el patrón ya es predecible y conviene escribir los esquemas con una
clase abierta desde el principio.**


### 🔴 La compuerta de ARRANQUE sobre la escritura de juicio (acción 1 del pase 56)

**Denominador: las mismas 8 piezas de la capa docente.** **Canal: `raw.githubusercontent.com`, rama
`main`, 9 de 9 en 200** (las 8 más `PabloPC05/mcp-usc`). ⚠️ **La pregunta NO es «¿tiene una
bandera?» sino «¿hay una compuerta de arranque sobre el tool que escribe el JUICIO?»** — porque el
pase 56 estableció (338–340) que la confirmación por llamada no protege contra el alumno que planta
instrucciones.

| Pieza | Variable de la compuerta | Granularidad | ¿Desregistra? | Defecto | ¿Cubre la nota? | G |
|---|---|---|---|---|---|---|
| [`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp) | `MOODLE_ALLOW_WRITE` + `MOODLE_WRITE_COURSE_ALLOWLIST` | bandera global **+ por RECURSO** | 🔴 **no** — rechaza en la llamada, el tool se lista igual | 🟢 **fail-closed** (`0` / vacía) | ✅ **sí** | 🟢 **G2** |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | `ALLOWED_WRITE_TOOLS` | 🟢 **por TOOL** | 🟢 **sí** — *«so it cannot be listed or called»* | 🔴 **fail-closed en HTTP, fail-OPEN en stdio** | ✅ **sí** | 🟢 **G3** ⚠️ |
| [`Dymayo/moodler-mcp`](https://github.com/Dymayo/moodler-mcp) | `MOODLER_ALLOW_TEACHER_GRADING` | bandera **por ROL** | 🟢 **sí** — *«Tools behind a disabled flag are not registered at all»* | 🟢 **fail-closed** (`off`) | ✅ **sí** | 🟢 **G2′** |
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | `CANVAS_DESTRUCTIVE_TOOLS=block` (y `CANVAS_ROLE`) | por CONJUNTO de tools | 🟢 **sí** — *«`block` means the handler is never registered»* | ⚠️ `allow` por defecto | 🔴 **NO** — sólo los **7** tools de borrado | 🔴 **G0** |
| [`NiccoloSalvini/mcp-moodle-staff`](https://github.com/NiccoloSalvini/mcp-moodle-staff) | `MOODLE_STAFF_TOOLS` (*«sees 17 tools instead of 22»*) | por GRUPO | ⚠️ no determinado | 🔴 **fail-OPEN** — *«on by default»* | ⚠️ **no determinado** (**gap 249**) | ⚠️ **G1?** |
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🔴 **ninguna** — 3 variables y las 3 son de conexión | — | — | — | 🔴 **no** | 🔴 **G0** |
| [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) | 🔴 **ninguna** — `MOODLE_ALLOW_INSECURE` es **TLS**, no escritura | — | — | — | 🔴 **no** | 🔴 **G0** |
| [`openedx-mcp`](https://pypi.org/project/openedx-mcp/) | 🔴 **ninguna de arranque** — autoriza con `is_staff` / `is_superuser` de Django y protege en la LLAMADA | — | — | — | 🔴 **no** | 🔴 **G0** |

**El reparto: 3 de 8 tienen compuerta de arranque de G2 o mejor sobre la escritura de juicio**
(`toshieji`, `vishalsachdev`, `Dymayo`). 🔵 **La hipótesis del pase 56 pedía ≥ 4 para declarar norma de
categoría y ≤ 2 para declarar hallazgo de riesgo: 3 cae en el medio y NO decide.** ⚠️ **Es el segundo
pase consecutivo en que un umbral pre-registrado de 3-contra-4 aterriza exactamente en el hueco; la
lección es de diseño de hipótesis, no de datos: un umbral sobre n = 8 tiene que partir en 4-contra-4.**

#### 🔴 Lo que sí decide: la escalera no es ordinal (P137)

**«Impedir listar el tool» NO es una propiedad de la granularidad**, y las tres piezas con compuerta lo
demuestran en tres direcciones distintas:

| | granularidad | ¿desregistra? |
|---|---|---|
| `Dymayo` | la más **gruesa** (un booleano por rol) | 🟢 **sí** |
| `toshieji` | más **fina** (allowlist por recurso) | 🔴 **no** |
| `bruchris` / `CANVAS_ROLE` | por rol | 🔴 **no, y el proyecto lo dice**: *«hides tools from a listing»* |

🔵 **Son dos ejes ortogonales y el pase 56 los soldó en una escalera. Cuarto pase consecutivo en que un
esquema de esta base resulta insuficiente al primer contacto con los datos** (3→5 en el 54, 4→5 en el
56, y acá una escalera que no es ordinal). **La lección que el pase 56 dejó escrita —escribir los
esquemas con una clase abierta— se aplicó, y no alcanzó: lo que hacía falta era escribirlo con DOS
COLUMNAS.**

#### 🔴 El eje que decide el despliegue no estaba en la escalera: el sentido del defecto (P138)

**`ALLOWED_WRITE_TOOLS` es la compuerta más fina de las ocho y nació del *security release* que el pase
56 citó.** Su defecto depende del TRANSPORTE:

> *«HTTP servers are read-only unless configured → set `ALLOWED_WRITE_TOOLS` to the write tools your
> deployment needs, or `all` … **Local stdio servers are unchanged unless you set it**»*

🔴 **El despliegue normal de un docente es stdio, y en stdio la compuerta está apagada salvo que el
operador la encienda.** De las 3 piezas con compuerta real sobre la nota, **sólo 2 son fail-closed en el
despliegue local por defecto** (`toshieji`, `Dymayo`) — **y las dos tienen 0 ★, mientras la de 272 ★ es
la fail-open.** 🔵 **Misma curva invertida que P134: la adopción y la guarda van al revés.**

#### ⚠️ La compuerta más honesta de la capa apunta al objeto equivocado (P140)

`bruchris/canvas-lms-mcp` es la única pieza que **distingue explícitamente un filtro de un límite** y la
única que **se niega a fingir una guarda que no tiene** (*«`confirm` is reserved but not implemented»*).
🔴 **Y su desregistro real cubre los SIETE tools de borrado, no `grade_submission`.** ⚠️ **Para una
auditoría de compras esto es la trampa del eje: una planilla que cuente «filtrado por rol» o «política
de tools destructivos» como control de escritura de notas cuenta un filtro de UX y un alcance
equivocado como si fueran compuertas.** 🟢 **Y `CANVAS_PROVENANCE_FENCING` (encendido por defecto) es
el único control de la capa que ataca el modelo de amenaza de P132 por donde entra —marca la
procedencia del texto del alumno— con su límite dicho por el propio proyecto:** *«Fencing marks
provenance; it does not enforce obedience … a precondition for a model treating it as data — not a
guarantee that it will»*.

### 🔴 La divulgación es 1 de 8, y la obligación está VIGENTE hace dos meses

🔴 **Una sola de las ocho emite divulgación de asistencia AI, y es la de 0 ★.** ⚠️ **El Artículo 50 de
transparencia rige desde el 2026-08-02 —hace dos meses— y el deber es del PROVEEDOR**, que es
exactamente el rol de Globant cuando construye y entrega. 🔴 **La pieza más adoptada de la capa (272 ★)
es T4, y la única conforme tiene cero adopción: la curva de adopción y la curva de cumplimiento de esta
capa apuntan en direcciones opuestas** (**P134**).

### 🔵 Los dos ejes vuelven a estar ANTI-correlacionados, y ahora se entiende el mecanismo

**El pase 55 encontró la anti-correlación entre higiene de credencial y salvaguarda. Acá reaparece entre
confirmación y divulgación: las 4 piezas con confirmación tienen 0 divulgaciones, y la única con
divulgación no necesita confirmación.** 🟢 **Y el mecanismo no es casualidad: `toshieji` no confirma
porque NUNCA LIBERA — el borrador hace innecesaria la confirmación, mientras las otras siete confirman
porque el efecto es inmediato e irreversible.** 🔵 **Dicho como regla de diseño, que es lo que se lleva
un *engagement*: confirmar es el control que se elige cuando la escritura es definitiva; si la escritura
puede ser un borrador, el borrador domina a la confirmación — y P132 explica por qué, porque la
confirmación no sobrevive al modelo de amenaza y el borrador sí.**

### ⚠️ La región, medida en vez de inferida — y un falso positivo propio

🟢 **2 de 8 quedan ubicadas con evidencia de primera mano:** `toshieji` → **APAC** (800 caracteres CJK,
reconfirmando el pase 55) y `vishalsachdev` → **North America** (*«University of Illinois Urbana»* en su
propio README; **ubicación NUEVA**). ⚠️ **Las otras 6 no declaran región y se dice así**, en vez de
inferirla del nombre del autor.

🔴 **Y el falso positivo que este pase se encontró a sí mismo antes de publicarlo:** un barrido de países
dio *«Italia»* en `MarcosNahuel/moodle-mcp` y **era subcadena de `Italicia`, el titular del copyright**
— una organización, no un país. **Un barrido de topónimos sin límite de palabra ubica piezas en países
donde nadie trabaja** (**P135**). 🔵 **Es el mismo defecto de clase que P126: instrumento casero, control
que no ejercita el caso de falla.**

### 🟢 La pieza que hay que dejar de recomendar, y la que hay que empezar a recomendar

🔴 **`peancor/moodle-mcp-server` es la combinación peor de la capa y esta base la recomienda en
`compose/patterns.md`:** 🟢 clase (a) de credencial —**token de administración del SITIO**, el privilegio
más alto medido— con **T4**, la guarda más baja. **Máximo privilegio, mínima guarda, y 43 ★ que le dan
apariencia de opción por defecto.**

🟢 **`toshieji/moodle-grading-mcp` es la única de las ocho entregable tal cual en un *engagement* con
escritura de notas**, y su desventaja es de tracción, no de ingeniería: **0 ★, MIT, y es la única que
llega conforme al Artículo 50.** 🔵 **Recomendación concreta: se adopta su patrón —`readyforreview` +
nunca liberar + pie de divulgación— aun cuando el conector sea otro.**

### 🟢 Denominador ENUMERADO de la capa de conectores por LMS (acción 2 del pase 54, pase 55)

**Método, que es lo que faltaba:** se recorrió fila por fila la tabla *«El mapa, por LMS»* —acotada y ya
escrita— leyendo cada pieza por `raw.githubusercontent.com`, **sin barrido por vocabulario** (el barrido
sigue negado por `[Credential Exploration]`).

| Reparto de las 14 filas | n | Filas |
|---|---|---|
| Cliente de un tercero, **canal determinable y determinado** | **9** | `bruchris`, `vishalsachdev`, **`mtgibbs`**, `peancor`, `MarcosNahuel`, **`csmediapro`**, `bunizao`, **`gafapa`**, `moon0825` |
| Cliente de un tercero, **no determinable** | **2** | `@owen-x-tech/canvas-mcp` (repo 404 en 12 sondas) · `@imazhar101/mcp-canvas-server` (sin licencia declarada) |
| **No** es cliente de un tercero | **1** | `openedx-mcp` — plugin **oficial del propio proyecto**, corre en proceso |
| Fuera del eje: no pide credencial de LMS | **2** | `giacomomaria81/scorm-mcp-server` · `course-code-framework/coursecode` |

**Las tres medidas por primera vez en este pase:**

| Pieza | Clase | Credencial | Escritura | Cita |
|---|---|---|---|---|
| [`mtgibbs/canvas-lms-mcp`](https://github.com/mtgibbs/canvas-lms-mcp) | 🟢 **(a)** | `CANVAS_API_TOKEN` + `CANVAS_BASE_URL`, emitido en *Account → Settings → New Access Token* | 🟢 **ninguna** | *«This server only reads data; it cannot modify assignments or grades»* |
| [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🟢 **(a)** | `MOODLE_URL` + `MOODLE_TOKEN` de *Site administration → Plugins → Web services → Manage tokens* | 🟢 **ninguna** | *«never modifies Moodle data, safe for production»* |
| [`gafapa/moodle-core-cli`](https://github.com/gafapa/moodle-core-cli) | 🟢 **(a)** | `MOODLE_BASE_URL` + `MOODLE_TOKEN`, o `--url` / `--token` | ⚠️ **sí, ya compuertada** | *«The CLI runs in read-only mode by default. Write operations require `--allow-write`, and destructive operations additionally require `--yes`»* |

🟢 **El dato que abarata la recomendación que esta base viene haciendo desde el pase 35:** `gafapa` era
*«el candidato más barato a envolver»* por no tener MCP (reconfirmado: **cero** menciones), **y ahora se
sabe que la compuerta de escritura ya existe debajo** — el envoltorio hereda `--allow-write` / `--yes`
en vez de tener que inventarlos.

🔵 **Y el denominador enumerado corrige una tasa:** **2 de 9 (22,2 %)** en clase (b) acá, contra el
**7 de 18 (38,9 %)** acumulado de los pases 53 y 54 — **consistente con que la muestra anterior se
eligió por lo interesante.** 🔴 **El «73 de 80» del pase 53 sigue sin instrumento publicado: este pase
cierra la tabla de 14, no esa población.** Ver tendencias **327** y **328**.

### ⚠️ La capa mejor medida de esta KB es la que más región le falta — 16 de 21 (pase 55)

**Medido, no estimado: de las 21 filas de las dos tablas de credencial, 16 dicen «sin región declarada»
y 5 traen región.** 🟢 **Una se recuperó en este pase con evidencia de primera mano:
`toshieji/moodle-grading-mcp` → **APAC**, por **330** han + **216** hiragana + **254** katakana en un
README bilingüe JA/EN.** 🔴 **Y eso corrige parcialmente al pase 49: *«APAC no produce open source
educativo-nativo»* se escribió con una pieza educativa-nativa, MIT, APAC y de la mejor postura de
integridad de la capa ya en esta tabla, con la región en blanco** (tendencia **323**).

🔴 **Pero el instrumento resuelve 1 de 5 y hay que decirlo:** las otras cuatro probadas publican **sólo
en inglés** (0 CJK, dominancia inglesa medida), **y el inglés no lleva señal regional en este
ecosistema.** ⚠️ **Dos instrumentos de este mismo pase dieron falsos positivos y se descartaron con
control** — un `grep` CJK orientado a bytes dio 8–23 coincidencias en 4 de 4 archivos que tienen cero, y
una lista de palabras-marca de italiano dio 12–15 en 5 de 5 por compartir `per`/`con`/`file` con el
inglés. **Ninguno se publicó como dato.** Ver **P130** y la tendencia **326**.

## 🧬 La HERENCIA del fork, medida archivo por archivo — y la hipótesis del pase 59 cae en una TERCERA rama que no había previsto (acción 1 del pase 59, cerrada en el pase 60)

**Canal:** `raw.githubusercontent.com`, rama `main`, archivo por archivo. **Controles negativos corridos
ANTES de leer nada** (regla de **P126**): rama inexistente → `404`, archivo inexistente → `404`, repo
inexistente → `404`. 🟢 **El canal discrimina, así que un `200` significa algo.** ⚠️ **`codeload.github.com`
y `api.github.com` siguen en `403`: cuarta reproducción consecutiva.**

### 🔴 La corrección de método que va antes de la tabla: la ruta que el pase 59 prescribió NO EXISTE

El pase 59 mandó leer **`src/services/canvas-client.ts` en `algorithm0r/canvas-lms-mcp`**. 🔴 **Ese archivo
no existe en ese repo** (`404`). **La ruta pertenece a `CharlieCardenasToledo/mcp-canvas-server`**, que es
la pieza que el propio pase 59 dio de alta tres párrafos antes. 🔵 **Es una colisión de ruta entre dos
repos del mismo pase, y se corrige sola si la acción cita `repo + ruta` en vez de ruta suelta** (**gap 251**).
**La ruta real del eje en `canvas-lms-mcp` es `src/canvas/submissions.ts`.**

### El par A — `bruchris` → `algorithm0r`: IDÉNTICO, byte a byte, en los nueve archivos

| Archivo | Madre (bytes) | Fork (bytes) | Veredicto |
|---|---|---|---|
| `README.md` | 43.022 | 43.022 | 🟢 idéntico |
| `package.json` | 2.883 | 2.883 | 🟢 idéntico |
| `src/tools/index.ts` | 8.159 | 8.159 | 🟢 idéntico |
| `src/canvas/index.ts` | 4.739 | 4.739 | 🟢 idéntico |
| `src/canvas/client.ts` | 5.357 | 5.357 | 🟢 idéntico |
| **`src/canvas/submissions.ts`** | **6.258** | **6.258** | 🟢 **idéntico — es el archivo del eje** |
| `src/tools/catalog.ts` | 7.898 | 7.898 | 🟢 idéntico |
| `src/tools/submissions.ts` | 7.004 | 7.004 | 🟢 idéntico |
| `src/tools/assignments.ts` | 13.070 | 13.070 | 🟢 idéntico |
| `src/tools/destructive-policy.ts` | 6.659 | 6.659 | 🟢 idéntico |

**El literal del eje, verbatim en las dos copias** (`src/canvas/submissions.ts`, método `grade`):

```ts
body: JSON.stringify({ submission: { posted_grade: grade } }),
```

🟢 **Cero menciones de `post_manually`, `posting_policy`, `postPolicy`, `hide_grade` o `unpost` en los diez
archivos de CUALQUIERA de las dos copias.** ⚠️ **El fork ni siquiera cambió los *badges* de CI del README:
siguen apuntando a `bruchris/canvas-lms-mcp`.**

### 🔴 El par B — `vishalsachdev` → `abr-Projects`: DIVERGE, y ahí está el hallazgo

| Archivo | Madre (bytes) | Fork (bytes) | Veredicto |
|---|---|---|---|
| `pyproject.toml` | 4.056 | 4.065 | 🔴 difiere |
| `README.md` | 39.479 | 37.048 | 🔴 difiere |
| `src/canvas_mcp/server.py` | 35.587 | 34.521 | 🔴 difiere |
| `src/canvas_mcp/core/client.py` | 36.263 | 34.711 | 🔴 difiere |
| **`src/canvas_mcp/tools/assignments.py`** | **60.153** | **53.290** | 🔴 **difiere — es el archivo del eje** |
| `src/canvas_mcp/tools/rubrics.py` | 83.623 | 59.436 | 🔴 difiere (−29 %) |
| `src/canvas_mcp/tools/student_write.py` | 43.997 | 46.665 | 🔴 difiere |
| `src/canvas_mcp/tools/peer_reviews.py` | 10.695 | 10.345 | 🔴 difiere |

⚠️ **Y una diferencia de SUPERFICIE, no sólo de bytes: el fork no registra `register_educator_course_tools`.**
La madre importa 26 registradores; el fork, 25.

### 🔴 El resultado que ninguna de las dos ramas de la hipótesis describía (P150)

El pase 59 escribió dos ramas: **«si el fork es idéntico en el eje, identificar por commit es una precaución
de inventario»** o **«si DIVERGE, el fork es una fila propia y el denominador de 9 está mal contado»**.
🔴 **El par B cae en una TERCERA: diverge en 42 líneas de `bulk_grade_submissions` —256 líneas en la madre,
245 en el fork— y sin embargo es IDÉNTICO en el eje de publicación.**

| Medición sobre `bulk_grade_submissions` | Madre | Fork |
|---|---|---|
| Líneas de la función | 256 | 245 |
| Líneas de `diff` | — | **42** |
| `submission[posted_grade]` | **1** | **1** |
| Consultas de `post_manually` / `posting_policy` | **0** | **0** |

🟢 **Así que el denominador de 9 SE SOSTIENE en el eje de publicación y P146 se confirma — pero sólo para
ese eje.** 🔴 **Lo que NO se sostiene es la lectura cómoda de la primera rama: la divergencia del par B cae
entera sobre un eje de seguridad VECINO —la precondición de rúbrica— y el fork está del lado LAXO en las
cuatro celdas.**

| Celda | Madre `vishalsachdev` | Fork `abr-Projects` | Dirección |
|---|---|---|---|
| Verificación POST-escritura `rubric_grade_is_confirmed` | **presente (2 usos)** | 🔴 **ausente (0 usos)** | fork más laxo |
| Constante `RUBRIC_GRADE_UNCONFIRMED` | presente (2) | 🔴 ausente (0) | fork más laxo |
| Si falla leer la config de rúbrica | 🟢 **aborta**: *«Could not verify rubric grading settings; no assessments were submitted.»* | 🔴 `if "error" not in assignment_check:` — **sigue y califica** | fork más laxo |
| Si `use_rubric_for_grading` es falso | 🟢 **aborta siempre** | ⚠️ `if not use_rubric_for_grading and not dry_run:` | fork más laxo |
| `include[]` al pedir la config | `["rubric", "rubric_settings"]` | `["rubric_settings"]` | fork pide menos |

🔴 **La conclusión que cambia la recomendación, y es la de este pase: «identificar por commit» NO es una
precaución de inventario. Es sustantiva — pero en el eje que uno no estaba mirando.** El fork es un
**snapshot viejo que perdió el endurecimiento posterior de la madre**, no una modificación deliberada:
pierde una verificación POST-escritura que existe para atrapar la nota que Canvas acepta y no guarda
(**P150**).

### 🔵 La regla general que deja este pase, y es la que hay que aplicar a las próximas 61 filas (P151)

🔵 **La herencia de un fork es RELATIVA AL EJE, no global.** Un fork puede ser idéntico en el eje medido y
divergente —y peor— en el de al lado. 🔴 **Por lo tanto «es fork de X» NUNCA cierra una celda por sí solo:
cierra la celda del eje que se comparó, y deja abiertas todas las demás.** ⚠️ **El par A y el par B dan
veredictos opuestos sobre la MISMA pregunta («¿hereda?»), y los dos son correctos: uno heredó todo y el
otro heredó sólo el eje que medimos** (**P151**).

### ⚠️ El defecto de instrumento que este pase se encontró a sí mismo, y es el de siempre

🔴 **El primer extractor de funciones devolvió 7 líneas para una función de 256 y, en consecuencia, un
`diff` de 0 líneas: un «IDÉNTICO» falso.** Rompía en la firma multilínea (`async def ...(` seguido de
parámetros a la izquierda del margen). **Lo atrapó el control de plausibilidad —una función de grado masivo
no tiene 7 líneas—, no el `diff`.** 🔵 **Tercera reproducción de la forma: un extractor con pérdida no falla
ruidosamente; devuelve un número más chico y más confiado** (P107, pase 47, pase 49). ⚠️ **Si este pase
hubiera confiado en la primera corrida, habría publicado «el fork B es idéntico» — la conclusión
exactamente opuesta a la verdadera.**

## 🔑 La PRECONDICIÓN se puede LEER con el token que la puerta YA tiene — medido en el código de Moodle (acción 2 del pase 59, cerrada en el pase 60)

**Pregunta del pase 59, textual:** *«¿alguna de las nueve puertas puede verificar `markingworkflow` con el
token que ya tiene?»* 🟢 **Respuesta: SÍ, las nueve, y sin pedir nada al cliente.**

**Fuente, de primera mano:** `moodle/moodle` @ `main`, `public/mod/assign/externallib.php`, **3.146 líneas**,
leído por `raw.githubusercontent.com` en este pase. 🟢 **`gap 250` CERRADO: el árbol efectivamente se mudó
—`public/mod/assign/externallib.php` responde `200` y `mod/assign/externallib.php` responde `404`—.**
**Versión del árbol leído:** `$release = '5.3rc2 (Build: 20261002)'`, `$version = 2026100200.00`.

| Qué | Dónde, con número de línea | Qué dice |
|---|---|---|
| El campo se **selecciona** en SQL | `externallib.php:371` | `'m.markingworkflow, '` |
| El campo se **asigna sin condicional** | `externallib.php:464` | `$assignment['markingworkflow'] = $module->markingworkflow;` |
| El campo está en el **contrato de salida** | `externallib.php:584` | `'markingworkflow' => new external_value(PARAM_INT, 'enable marking workflow'),` |
| La **única** capacidad exigida | `externallib.php:401` | `require_capability('mod/assign:view', $context);` |
| La capacidad para **escribir** nota | `externallib.php:1033` | `require_capability('mod/assign:grade', $context);` |

### 🟢 El argumento que cierra la pregunta, y es *a fortiori*

🔴 **`mod/assign:view` es estrictamente MÁS DÉBIL que `mod/assign:grade`.** Toda puerta que pueda **escribir**
una nota tiene, por construcción, la capacidad necesaria para **leer** `markingworkflow`. 🟢 **No hay un
escenario en el que una de las nueve pueda calificar y no pueda consultar la precondición.** 🔵 **Por la
rama que el propio pase 59 escribió: «si el dato viene con el token normal, entonces la verificación de
plataforma es un PR de tres líneas y esta KB puede ofrecerlo hacia afuera».** **Es esa rama.**

⚠️ **Tres precisiones que evitan que esto se cite mal:**

1. 🟢 **El campo NO es `VALUE_OPTIONAL`.** En la misma estructura hay **10** campos que sí lo son
   —`optionalmarkercount` y `preventsubmissionnotingroup` entre ellos—; `markingworkflow` **no**. **El
   contrato garantiza que viene siempre**, no «si está configurado».
2. ⚠️ **El parámetro `capabilities` de `get_assignments` (`externallib.php:333`, `has_all_capabilities`) es un
   FILTRO DE CURSOS, no una compuerta de campos.** Pasarlo vacío —que es lo que hacen las nueve— no recorta
   la estructura devuelta.
3. ⚠️ **Esto se midió sobre `main` (5.3rc2), no sobre una LTS desplegada.** La celda vale para el árbol
   leído; un cliente en 4.x necesita la misma lectura sobre su rama (**gap 252**).

### 🟢 Lo que esto habilita, concretamente, y es trabajo cotizable

🔵 **El parche es el mismo para las seis puertas silenciosas y para los dos polos: un *read-before-write*.**
Llamar `mod_assign_get_assignments`, leer `markingworkflow`, y **rehusar escribir** si la casilla no sostiene
la garantía que la pieza promete. 🔴 **No es una escalada de permisos ni un pedido al cliente: es código, y
entra en el repo de la pieza.** 🟢 **Para `toshieji/moodle-grading-mcp` —la única que AFIRMA no publicar— es
exactamente el PR de tres líneas que convierte su garantía CONDICIONAL en INCONDICIONAL, y es la
contribución *upstream* más barata y más defendible que esta KB identificó hasta ahora** (**P152**).

## 🔬 La UNICIDAD de `peancor`, medida sobre NUEVE puertas (acción 2 del pase 58, cerrada en el pase 59)

**Pase 58 midió seis puertas y encontró una sola que derrota la configuración correcta del cliente.**
La acción 2 pedía **ampliar el barrido más allá de las seis** y buscar **en el CÓDIGO** —no en el
README, que es donde el pase 58 demostró que no aparece— el literal `'released'` y cualquier
`workflowstate` constante. 🔵 **La hipótesis falsable estaba escrita de antemano y las dos ramas
servían:** *«si `peancor` es único, es una fila para excluir y se nombra; si hay más, "afirma la
publicación" es una clase de la capa y hay que contarla.»*

🔴 **`peancor` es único: 1 de 9.** **No es una clase: es una fila.** 🟢 **La regla de entrega de
P142 se sostiene con el denominador ampliado en un 50 %.**

### Las nueve puertas, con el literal que decide cada celda

**Canal:** `raw.githubusercontent.com`, rama `main`. **Regla del pase 58, mantenida:** la celda se
decide por el archivo que hace la llamada, no por el README.

| Puerta | Licencia | ★ | Qué manda, verbatim | Posición en el eje |
|---|---|---|---|---|
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** | 43 | `workflowstate: 'released'` **cableado** en `src/index.ts` | 🔴 **AFIRMA publicar** |
| [`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp) | **MIT** | 0 | `"workflowstate": "readyforreview"` + `"released": False` **cableado** en `server.py:570`, con el comentario propio *«★未公開ドラフト。releasedにしない»* | 🟢 **AFIRMA NO publicar** |
| [`Dymayo/moodler-mcp`](https://github.com/Dymayo/moodler-mcp) | **MIT** | 0 | `workflowstate=""` en `tools/writes_teacher.py` | ⚠️ omisión |
| [`NiccoloSalvini/mcp-moodle-teacher`](https://github.com/NiccoloSalvini/mcp-moodle-teacher) | **MIT** | 0 | 🔵 **medido en ESTE pase:** `workflowstate: ""` en `src/index.ts:375`, con `attemptnumber`, `addattempt` y `applytoall: false`, antes de `moodle().call("mod_assign_save_grade", payload)` | ⚠️ omisión |
| [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) | **MIT** | 1 | `if (args.workflow_state) { params.workflowstate = args.workflow_state; }` | ⚠️ hereda |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | **272** | `submission[posted_grade]`, sin leer la política | ⚠️ omisión |
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | **MIT** | 8 | `canvas.submissions.grade(...)`, sin condicional previo | ⚠️ omisión |
| [`CharlieCardenasToledo/mcp-canvas-server`](https://github.com/CharlieCardenasToledo/mcp-canvas-server) | **MIT** | 0 | 🟢 **ALTA de este pase, y NO es fork:** `data = { submission: { posted_grade: grade } }` en `src/services/canvas-client.ts:494-507`; **0 menciones de `post_manually` / `posting_policy` / `postPolicy` en los 60.194 bytes del cliente** | ⚠️ omisión |
| [`NiccoloSalvini/mcp-moodle-staff`](https://github.com/NiccoloSalvini/mcp-moodle-staff) | **MIT** | 0 | ninguna llamada a `mod_assign_save_grade`: CSV + importador nativo | ⚫ fuera del eje (**P143**) |

### 🔴 El eje es BIPOLAR y ESCASO, y eso es el hallazgo nuevo (P145)

| Posición | Cuántas | Mecanismo |
|---|---|---|
| 🔴 **AFIRMA la publicación** | **1 de 9** (`peancor`) | constante `'released'` en el código |
| 🟢 **AFIRMA la NO publicación** | **1 de 9** (`toshieji`) | constante `'readyforreview'` en el código |
| ⚠️ **no dice nada: hereda u omite** | **6 de 9** | `""`, condicional, o `posted_grade` crudo |
| ⚫ **fuera del eje** | **1 de 9** (`mcp-moodle-staff`) | no pasa por el web service |

🔵 **Sólo 2 de 9 toman posición, y son los dos extremos.** 🔴 **Y la simetría que ningún pase anterior
vio: NINGUNO DE LOS DOS POLOS consulta la precondición, así que las dos garantías son condicionales y
en sentidos OPUESTOS.**

| Pieza | Lo que cablea | Con `markingworkflow = 1` | Con `markingworkflow = 0` |
|---|---|---|---|
| `peancor` | `'released'` | 🔴 **publica igual — derrota la salvaguarda** | 🔴 publica |
| `toshieji` | `'readyforreview'` | 🟢 **retiene: la garantía funciona** | 🔴 **publica igual — la garantía se DERROTA** |

⚠️ **O sea que la mejor pieza de la capa y la peor dependen de la MISMA casilla, en sentidos
inversos.** 🔵 **Consecuencia de entrega, y es más fuerte que la del pase 58: la verificación de
plataforma no es un paso que proteja de las puertas malas — es el paso del que depende que la puerta
BUENA sea buena.** 🟢 **El único cumplimiento incondicional sigue siendo `AI-Teaching-Agent`, que no
puede publicar** (**P144**, y por eso **P145** lo confirma en vez de reemplazarlo).

### 🔴 Las puertas de Canvas se propagan por FORK, y un barrido por repo sobre-cuenta (P146)

**Medido en la propia página de cada repo, que declara el padre:**

| Fork | Padre declarado | Licencia | ★ | ¿Escribe nota? |
|---|---|---|---|---|
| [`algorithm0r/canvas-lms-mcp`](https://github.com/algorithm0r/canvas-lms-mcp) | 🔴 *«forked from `bruchris/canvas-lms-mcp`»* | **MIT** | 0 | 🔴 **sí** — `grade_submission`, `comment_on_submission`; *«48 tools perform Canvas write operations»* |
| [`abr-Projects/canvas-mcp`](https://github.com/abr-Projects/canvas-mcp) | 🔴 *«forked from `vishalsachdev/canvas-mcp`»* | **MIT** | 0 | 🔴 **sí** — `bulk_grade_submissions` |

🔵 **Las dos puertas de Canvas que esta base ya había medido tienen cada una al menos un fork que
HEREDA su camino de escritura**, y los dos aparecen en el mismo barrido que las madres, con
descripciones casi idénticas. 🔴 **Consecuencia de método, y toca cómo esta KB cuenta: «1 de 9» es una
afirmación sobre CÓDIGO DISTINTO. Contado por repos, el mismo defecto de `bruchris` y de
`vishalsachdev` aparecería dos veces cada uno y el denominador se infla sin que entre un solo
mecanismo nuevo.** ⚠️ **Y el riesgo de despliegue es real y al revés de lo que parece: un cliente
puede adoptar el fork sin que el barrido lo nombre nunca, porque el fork tiene 0 ★ y la madre es la
que se busca.** 🔵 **Es la misma forma del hallazgo del pase 57 —`mcp-moodle-teacher` y
`mcp-moodle-staff` sirviendo el MISMO README byte a byte— ahora con el padre declarado por GitHub en
vez de inferido por `sha256`.**

### ⚠️ Las cinco candidatas SCREENEADAS que no son puertas, registradas como ausencia MEDIDA

**Por la regla de los pases 51–52: una ausencia medida es un dato; el silencio parece cobertura.**

| Candidata | Licencia (de primera mano) | ★ | Por qué NO es puerta |
|---|---|---|---|
| [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) | 🔴 **NINGUNA** — `LICENSE` ausente en `main` **y** `master`, y **sin clave `license` en `pyproject.toml`** (`moodle-mcp` v0.2.1) | **37** | sólo lectura de notas (`get_grades`, `get_assignment_status`, `analyze_assignment`) |
| [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | ⚠️ **AGPL-3.0** | 0 | *«Read-only — never modifies Moodle data, safe for production»* |
| [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | **MIT** ✅ (texto del `LICENSE` leído) | 0 | sólo lectura, lado ALUMNO; Go |
| [`dddanielliu/NCCU-Moodle-MCP`](https://github.com/dddanielliu/NCCU-Moodle-MCP) | 🔴 **NINGUNA** — `LICENSE` ausente en `main` y `master` | 0 | una sola escritura, `submit_assignment`, y es del ALUMNO: *«Saves only — never the irreversible submit-for-grading»* |
| [`PabloPC05/mcp-usc`](https://github.com/PabloPC05/mcp-usc) | **MIT** | 0 | sólo lectura: *«does not … act as teaching staff or administration»* |

### 🔴 El dato de licencia que va antes de cualquier recomendación (P147)

🔴 **El MCP de Moodle más estrellado que apareció en este barrido no tiene licencia.**
`loyaniu/moodle-mcp` acumula **37 ★** —el segundo más estrellado de toda esta capa después de los
272 de `vishalsachdev`— y **no se puede usar**: sin `LICENSE` en ninguna de las dos ramas y sin
declaración en el empaquetado, el defecto es de permiso, no de calidad.

🔵 **Tercera reproducción de la curva invertida de P134/P138, y esta vez sobre la licencia en vez de
sobre la compuerta:** la pieza con más adopción de las que aparecieron es la inusable, y las usables
—`Jawadh-Salih`, `CharlieCardenasToledo`, `toshieji`— tienen **0 ★**. ⚠️ **Para una propuesta esto es
accionable y barato: el filtro de licencia se aplica ANTES del filtro de popularidad, porque el orden
inverso selecciona justamente lo que no se puede entregar.**

⚠️ **Denominador declarado, y la resta importa:** **9** puertas de escritura de nota con código leído
+ **2** forks que heredan + **5** candidatas screeneadas y descartadas = **16 repos tocados en este
pase**, de los cuales **9** entran al eje. 🔵 **Las 8 piezas de la capa docente del pase 56 siguen
siendo 8; el eje creció de 6 a 9 porque entraron `toshieji` (medido en código por primera vez),
`mcp-moodle-teacher` y la alta `CharlieCardenasToledo`.**

## 🔬 La PRECONDICIÓN DE PLATAFORMA, medida en las seis puertas (acción 1 del pase 57, cerrada en el pase 58)

El pase 57 estableció la mitad del mecanismo leyendo `moodle/moodle` de primera mano: con **`markingworkflow = 0`**
Moodle le manda la nota al alumno **sea cual sea el `workflowstate`**. La acción 1 pedía la otra mitad, sobre las
puertas que faltaban: **¿alguna consulta la precondición antes de escribir?** 🔴 **La respuesta es 0 de 6, y las seis
celdas salen del CÓDIGO, no del README** —que es exactamente donde el pase 57 dijo que había que mirar.

### Las seis puertas, con la cita que decide cada celda

| Puerta | Licencia | ¿Lee la precondición antes de escribir? | Qué manda, verbatim | Efecto sobre la nota |
|---|---|---|---|---|
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** | 🔴 **NO** — `getAssignments` existe y **no** pide `markingworkflow` | `workflowstate: 'released'` **cableado** en `src/index.ts` (`provideFeedback`), con `attemptnumber: -1`, `addattempt: 0` | 🔴 **PUBLICA, y publica incluso con `markingworkflow = 1`** |
| [`Dymayo/moodler-mcp`](https://github.com/Dymayo/moodler-mcp) | **MIT** | 🔴 **NO** — no llama a `mod_assign_get_assignments` | `workflowstate=""` en `tools/writes_teacher.py` (+ `attemptnumber=-1`, `addattempt=False`, `applytoall=False`) | 🔴 publica por omisión (ya medido en el pase 38) |
| [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) | **MIT** | 🔴 **NO** | `if (args.workflow_state) { params.workflowstate = args.workflow_state; }` en `src/tools/gradebook/calificar_manualmente.ts` | ⚠️ **HEREDA**: la exposición es de la plataforma, no afirmada por la puerta |
| [`NiccoloSalvini/mcp-moodle-staff`](https://github.com/NiccoloSalvini/mcp-moodle-staff) | **MIT** | ⚫ **no aplica** | **ninguna llamada a `mod_assign_save_grade`**: genera CSV y usa el importador nativo — *«the CSV import is Moodle's own way in»*, con `grades_verify` después | ⚫ **fuera del eje** (ver abajo) |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | 🔴 **NO** — el único `GET` previo pide `include[]=rubric,rubric_settings`, **no** la política de publicación | `PUT /courses/{id}/assignments/{id}/submissions/{user}` con `submission[posted_grade]` | 🔴 publica según el `posting_policy` del *assignment*, **sin consultarlo** |
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | **MIT** | 🔴 **NO** | `canvas.submissions.grade(course_id, assignment_id, user_id, grade)`, sin lógica condicional previa | 🔴 ídem |

### 🔴 El eje NUEVO, que es el que decide un despliegue — y el vocabulario de «borrador» no lo muestra

**Las seis no fallan igual.** La pregunta que separa: **con la plataforma BIEN configurada, ¿la puerta publica igual?**

| Clase | Piezas | Con `markingworkflow = 1` (o `post_manually = true`) |
|---|---|---|
| 🔴 **AFIRMA la publicación** | `peancor` — `'released'` cableado | 🔴 **publica igual: DERROTA la salvaguarda del docente** |
| ⚠️ **publica por OMISIÓN** | `Dymayo` (`""`) + las dos de Canvas | 🟢 **la configuración correcta la neutraliza** |
| ⚠️ **HEREDA** | `MarcosNahuel` (condicional) | 🟢 ídem |
| ⚫ **fuera del eje** | `mcp-moodle-staff` (CSV) | ⚫ no pasa por el web service |

🔵 **5 de 6 quedan neutralizadas por la configuración correcta de la plataforma; 1 de 6 la derrota.** ⚠️ **Y la que la
derrota es la que un barrido por README NO distingue de las otras, porque `'released'` no está en su documentación:
está en `src/index.ts`.** 🔴 **Regla de entrega, y es la frase que va al cliente: `peancor` es la única de las seis que
NO se arregla configurando el Moodle del cliente — es la fila que hay que EXCLUIR, no la que hay que configurar**
(**P142**).

### 🔵 `mcp-moodle-staff` está fuera del eje por DISEÑO, y no es lo mismo que estar a salvo

No llama al web service: arma el CSV y lo pasa por el importador nativo del libro de calificaciones. ⚠️ **No es más
seguro por eso —el importador también escribe la nota y tampoco pasa por marking workflow—.** 🔵 **Lo que cambia es
QUIÉN aprieta el botón: el import lo ejecuta una persona en la UI de Moodle, así que la liberación humana es una
propiedad del PROCESO y no del servidor.** 🔴 **Consecuencia de método: es una garantía real pero NO auditable en el
código de la puerta**, así que no entra en la misma columna que una compuerta — es la distinción de **P143**.

### 🟢 Lo que esta medición le exige al requisito de Globant

1. 🔴 **La verificación de plataforma es un paso OBLIGADO del despliegue, no un supuesto:** `markingworkflow = 1`
   por tarea en Moodle, `post_manually = true` en Canvas. **Ninguna de las seis lo va a hacer por nosotros**, y
   cinco de las seis quedan correctas si alguien lo hace.
2. 🔴 **`peancor` queda EXCLUIDA de la capa de escritura de nota** mientras `'released'` siga cableado. Es un
   cambio de una línea y es un PR hacia afuera; hasta entonces es la única cuyo defecto no se configura.
3. ⚠️ **«Borrador» deja de aceptarse como propiedad declarada por un README.** Se acepta leída en el código, o
   como propiedad del proceso (el caso CSV), y se dice de cuál de las dos se trata.
4. 🟢 **El patrón de referencia es `AI-Teaching-Agent`** (**P144**): generación y publicación separadas, de modo que
   la liberación humana no dependa de que una compuerta funcione.

⚠️ **Denominador declarado:** son **6** puertas, no las 8 de la capa docente del pase 56 — las dos que faltan
(`toshieji` y la octava) ya quedaron medidas por el pase 57 sobre este mismo eje, y `toshieji` es precisamente el caso
que **motivó** la acción (su «borrador» resultó ser una casilla de Moodle que el servidor no mira). 🔵 **Sumando los
dos pases, el eje está medido en 8 de 8 y el resultado no cambia de signo: ninguna pieza de la capa consulta la
precondición de su plataforma.**

## Agentes y herramientas destacadas

**🟢 Pase 51 del 2026-10-02 — la tabla pasa a 74 filas (+4, las primeras altas en NUEVE pases) y la COLUMNA LICENCIA de este archivo deja de ser una afirmación: está medida repo por repo.** Se ejecutó la **acción 1** del pase 50 aplicando **P114** a **los 167 `org/repo` distintos** que cita el archivo, con **20 nombres de archivo de licencia × `main` y `master`** y el control de alcanzabilidad: **139 licenciado · 23 sin licencia (ausencia MEDIDA) · 5 no público por este canal**, mezcla **MIT 79 · Apache 27 · GPL 9 · AGPL 7 · BSD 4 · CC 3 · LGPL 2 + 4 textos anómalos**. ⚠️ **Denominador declarado: 429 filas de pipe menos 60 separadores; 176 traen URL de GitHub, 249 NO —esas no son «sin medir», son medibles por registro + tarball.** 🔴 **Tres filas de este archivo cambian por la medición: `SafeTutors` y `AITutor-EvalKit` decían «MIT ✅» y no tienen UNA línea de texto de licencia** (eran *badge* + prosa; el badge de `SafeTutors` **todavía enlaza `your-username`**, o sea plantilla sin editar), **y `dssg/student-early-warning` pasa de ⚠️ «Other (NOASSERTION)» a 🔴 licencia académica NO COMERCIAL de la Universidad de Chicago que excluye *«any service or part of selling a service»*** — un bloqueo duro para una consultora, no un pendiente administrativo. 🔵 **Y el instrumento se corrigió a sí mismo: la lista de 4 nombres que esta base venía usando produjo 4 falsos «sin licencia» de 27 (14,8 %), entre ellos `moodle/moodle`** (GPL vía `COPYING.txt`) — las dos causas son **convenciones de ecosistema** (`COPYING.txt` en el mundo GNU/Moodle; `LICENSE-MIT`+`LICENSE-APACHE` en doble licencia estilo Rust). 🟢 **Las 4 altas entraron por un canal que esta base nunca había usado —el `?text=` de BÚSQUEDA del registro npm, no la consulta por nombre exacto— y dos de ellas tienen el texto de licencia medido en el TARBALL** porque su repo no es público o no se declara. ⚠️ **La acción 2 sigue SIN EJECUTAR: el entorno niega correr el código versionado de `compose/code/` (`[Code from External]`), igual que en el pase 50; no se reimplementó el probe ni se buscó otro intérprete.** ✅ **Control del gap 71 corrido en el mismo pase que tocó la tabla: 74 filas / 74 slugs distintos / 0 duplicados, y las 22 cabeceras del archivo con su `|---|` debajo (0 encabezados usados como dato).** Código, control positivo y TSV de 167 filas en `compose/code/p114-license-column/`.

**🔵 Pase 40 del 2026-10-02 — el conteo se re-mide con la regla del pase 36 y hay que corregirlo: son 65 filas, no 52.** Aplicada la regla que el pase 36 estableció —**contar *slugs* distintos** entre el separador y la primera línea que no empieza con `|`— el archivo tiene **65 filas de datos y 65 slugs distintos: cero duplicados**. 🔴 **El encabezado declaraba «52 filas», y la diferencia no es de este pase: los pases 37 a 39 agregaron filas sin actualizar el número** (este pase agrega **2**: `mereos` y `@timadey/proctor`, las dos de *proctoring*). 🔵 **Es la séptima vez que esta KB se pelea con este número, y la lección ya no es sobre el instrumento —que funciona— sino sobre el hábito: la regla del pase 36 es correcta y nadie la estuvo corriendo.** La medición es programática y cuesta un comando; **conviene correrla en cada pase que toque la tabla, no cada cinco.** ✅ **Verificado en este pase: 65 filas / 65 slugs / 0 duplicados.**

**🔵 Pase 42 del 2026-10-02 — la tabla se queda en 66 filas: OCTAVO pase consecutivo sin altas de agente, y el pase no se gastó buscándolas.** Se corrieron **las cuatro búsquedas globales y las cuatro regionales con el año calculado** (`date -u +%Y` → **2026**) y 🔴 **devolvieron por octava vez la capa genérica** (openclaw 385.407 ★, dify 151.639 ★, browser-use 108.128 ★, Mem0 62.735 ★, AutoGen 60.284 ★) **y material didáctico *sobre* AI**, que no es un agente de educación. ⚠️ **Dos tercios de los resultados de la primera búsqueda vinieron de agregadores SEO sin repo verificable (`toolradar`, `fungies.io`, `ayautomate`, `oosmetrics`): se descartaron sin medirlos, y se declara.** 🟢 **El valor del pase está en las tres acciones del 41, las tres ejecutadas:** la **puerta MCP de UniTime escrita y PROBADA** (26 tools → 13 expuestos, **23 aserciones en verde, 0 de 9 llamadas retenidas llegaron al upstream**, ver **P92**), las **61 filas de GitHub re-fechadas por sus 472 ramas** (capa de vitalidad corregida, abajo) y la **superficie de `seb-server` enumerada** (**P91**). 🔴 **Y el hallazgo que corrige al pase 41: la ruta MPL-2.0 que ese pase dejó como preferible cuesta MÁS código que la AGPL** — `RemoteProctoringService` es una **interfaz desnuda con 12 métodos obligatorios**, mientras `ProctoringBackendProvider` es una **clase concreta con 0 obligatorios**. 🟢 **Lo que sí la vuelve cotizable: su obligación de publicar es UN valor de enum.** 🔵 **Hallazgo lateral: la familia `Kuali` entra como registro histórico —4 repos, los cuatro muertos (6 a 9 años), middleware ECL-2.0 y aplicaciones AGPL-3.0— y esta KB tenía 0 menciones en 41 pases.** ✅ **Conteo corrido con la regla del pase 36 en el mismo pase que tocó el archivo: 66 filas / 66 identificadores distintos / 0 duplicados.**

**🔵 Pase 41 del 2026-10-02 — la tabla pasa a 66 filas, y el pase no se gastó en buscar agentes nuevos: se gastó en ejecutar las tres acciones que el pase 40 dejó escritas, que era donde estaba el valor.** El alta es **una** (`exam-guard`), y entra porque **se le resolvió la licencia, no porque se la haya encontrado**: el **gap 83 queda CERRADO** leyendo la *historia* de dos archivos, y el resultado es que **la contradicción ISC/Apache-2.0 no bloquea nada** (las dos son permisivas OSI; difieren en la cláusula de patentes). 🔵 **Y dos filas que ya estaban cambian de clase sin cambiar de licencia, que es el resultado más útil del pase:** el **gap 81 no era una clase, eran dos.** `@timadey/proctor` **declara MIT tres veces en el árbol** y apunta a un `LICENSE` que nunca se commiteó —es **archivo faltante**, y se cierra con un PR de un archivo—, mientras `@ink-waffle/sisu-mcp` tiene **una sola declaración en todo el mundo** y ni README en el tarball. **Misma etiqueta antes, riesgo muy distinto.** ✅ **Verificado en este pase con la regla del pase 36, y corrido en el mismo pase que tocó la tabla, como el pase 40 pidió: 66 filas / 66 slugs / 0 duplicados.** 🔴 **Nota de alcance: los tres hallazgos de base de este pase —`UniTime/unitime` (Apache-2.0), `SafeExamBrowser/seb-server` y `seb-win-refactoring` (MPL-2.0)— NO entran en esta tabla porque no son agentes: son plataformas con API, y están en `repos/foundations.md` y `verticals/solutions.md`. Lo que esta tabla registra de ellas es que **su puerta de agente no existe todavía en ningún registro** (gap 86).**

**🔴 Pase 36 del 2026-10-02 — el conteo baja de 52 a 51, y la causa es un defecto que el conteo programático NO PODÍA ver: `Claw-ED` estaba DOS VECES.** Las dos filas apuntaban al mismo repo (`SirhanMacx/Claw-ED`) con **59 ★ y 60 ★**, una del 2026-09-30 y otra agregada como «alta» en el pase 35 — y la línea de historial de este mismo archivo dice *«Claw-ED se agregó en la tercera pasada del 2026-09-30»*, al lado. ⚠️ **La lección es sobre el instrumento, no sobre el descuido: la regla del pase 30 cuenta FILAS entre el separador y la primera línea que no empieza con `|`, y un duplicado es una fila válida.** Un conteo de filas no puede detectar una fila repetida. **El control que sí lo detecta es contar *slugs* distintos**, y medido así el archivo tiene **51 filas = 49 repos de GitHub distintos + 2 entradas que son de PyPI y no de GitHub** (`openedx-mcp` y `tutor-contrib-openedxmcp`, las dos AGPL-3.0, con URL verificable de PyPI). 🔵 **Es la sexta vez que esta KB se pelea con este número y la primera en que el número se descompone en vez de declararse:** 51 filas / 49 repos / 0 duplicados, y de acá en adelante **el conteo que vale es el de slugs distintos**.

**52 filas contadas en el archivo** (**48 → 52 en el pase 35**: entran `Claw-ED`, `bruchris/canvas-lms-mcp`, `bunizao/moodle-cli` y `moon0825/jbnu-lms-mcp` — **las cuatro MIT**, y tres de las cuatro son conectores). **El conteo sigue siendo programático sobre el archivo** (filas entre el separador y la primera línea que no empieza con `|`), que es la regla que el pase 30 estableció después de que esta KB se peleara cinco veces con este número. (**47 → 48 en el pase 32**: entra `lineage-skill` — Apache-2.0.) (**44 → 47 en el pase 30**: entran `openedx-mcp` y `tutor-contrib-openedxmcp` —los dos **AGPL-3.0**— y `asfai-education` —**Apache-2.0**). ⚠️ **Y se deja asentada la diferencia en vez de heredarla:** el encabezado anterior declaraba «43 filas» cuando el archivo tenía **44 filas de datos**. El conteo de este pase es **programático sobre el archivo** (filas entre el separador y la primera línea que no empieza con `|`), así que **47 es el número verificable**; «43» era el conteo a mano del pase 19. **Es la quinta vez que esta KB se pelea con este número y la primera en que se mide en vez de contarse.** (**41 → 43 en el pase 28**: entran `trilogy-group/oneroster-ts` — **0BSD** — y `paulocymbaum/ed-tech-system-mcp` — MIT.) (37 → 38 en el pase 26: entra `canvas-mcp`; **38 → 41 en el pase 27**: entran `peancor/moodle-mcp-server`, `MarcosNahuel/moodle-mcp` y `scorm-mcp-server` — las tres son **conectores MCP**, y las tres son **MIT**.) Ordenados por stars. El conteo se hizo a mano en el pase 19 y
se explica abajo, porque es la cuarta vez que esta KB se pelea con este número.

> *Pase 25 del 2026-10-01:* **séptimo pase sin altas, y el eje de búsqueda que el pase 23 diagnosticó sigue siendo el que
> rinde — pero rinde infraestructura, no agentes.** Se ejecutaron los siete ítems de la consigna del pase 24 (`item bank`,
> `proctoring`, `timetable`, `competency framework`/CASE, y los estándares Caliper, CASE y xAPI Profiles, más
> `LTI platform`): **18 repos verificados de primera mano, 17 nuevos para esta KB, y ninguno es un agente.** Van a `repos/foundations.md` y
> `verticals/solutions.md`. **La lectura, a esta altura, es estructural y conviene no repetirla como queja:** en educación
> el open source produce **capas de interoperabilidad, evaluación y administración**, y los **agentes** que se usan son los
> genéricos de la industria, customizados. Esta tabla de 37 filas es el inventario de lo que sí existe; el crecimiento de
> esta KB está en **cómo se componen**, no en cuántos hay. Ver **P48** y **P49**.

> *Pase 23 del 2026-10-01:* **la tabla sigue en 37 filas — quinto pase consecutivo sin altas, y este identificó la causa
> estructural en vez de volver a declarar el agotamiento.** Se corrió el barrido completo obligatorio (cuatro búsquedas
> globales + cuatro regionales, con el año **calculado**). Los dos repos nuevos del pase **no son agentes**:
> `frappe/education` (GPL-3.0, 657 ★) es plataforma y va a `verticals/solutions.md`, y `aureuserp` (MIT, 12k ★) **no tiene
> módulo educativo** y queda como no-hallazgo declarado en `repos/trending.md`.
> 🔴 **La causa, medida:** en GitHub el término **`education` está capturado por el material didáctico *sobre* AI**
> (`AI Agents for Beginners` y `AutoGen`, 56k ★ cada uno; cursos de DeepLearning.AI) **y no por software que educa**. Los dos
> sentidos comparten la palabra y el primero tiene **dos órdenes de magnitud más de estrellas**, así que sepulta al segundo en
> cualquier ranking. **La consigna para el próximo pase corrige la del 22:** no alcanza cambiar el sustantivo — hay que
> **evitar la palabra `education`** y buscar por el **artefacto del dominio** (`gradebook`, `rubric`, `item bank`,
> `enrolment`, `attendance`, `IEP`, `transcript`) o por el **estándar instalado** (QTI, OneRoster, xAPI, LTI), que es cómo
> aparecieron las capas de los pases 6, 9, 11 y 22. **Nota de método: no se agregó ninguna fila de relleno.** 37 filas reales
> siguen siendo mejores que 40 con tres dudosas.
> **El hallazgo del pase está en la capa de evidencia, no acá:** se ejecutó la acción que el pase 22 dejó escrita y el
> **gap 36 quedó dimensionado** — los conteos de borrado **existen** en los tres backends de `lrsql`, pero la evidencia
> **no es portable entre motores de base de datos**, lo que contradice la razón por la que esta KB recomienda `lrsql` por
> default. Ver la tendencia **60** y el patrón **P46**.

> *Pase 22 del 2026-10-01:* **la tabla sigue en 37 filas, y es el cuarto pase consecutivo sin altas — el primero que
> mide el agotamiento en vez de declararlo.** Se corrió el barrido completo (cuatro búsquedas globales + cuatro
> regionales) y **los dos únicos candidatos que trajo ya estaban acá, con más precisión que la fuente**: `OpenMAIC`
> (la web lo da como «v1.0.0, MIT» y omite que **se relicenció de AGPL-3.0 a MIT en v0.3.0 del 2026-06-28**) y
> `AITutor-EvalKit` (que esta KB ya corrigió en el pase 4: el repo canónico del mismo autor es
> `UnifyingAITutorEvaluation`, 32 ★). El detalle candidato por candidato está en `agents/trending.md`.
> **El hallazgo del pase está en la capa de infraestructura, no acá:** el stack de analítica **oficial** de Open edX
> (**Aspects**, Apache-2.0, 2.269 commits) instala **Ralph sobre ClickHouse** —la configuración que el pase 21 declaró
> imborrable, que resulta ser el **default de la plataforma** y no una elección del cliente— y a la vez **trae el
> disparador de supresión LMS → telemetría que el pase 19 probó inexistente en Moodle** (`UserRetirementSink`,
> escuchando la señal Django `USER_RETIRE_LMS_MISC`). Corrige una advertencia de **P44**, cambia el estado de **P40**
> y abre el **gap 37**. Además se **reconfirmó el gap 36 por lectura independiente del código de `lrsql`**, con el
> sitio exacto del parche (`interceptors/lrs_management.clj:23–33`) y con una sub-pregunta que quedó **sin contestar
> y declarada**, no inferida.

> *Pase 21 del 2026-10-01:* **la tabla principal sigue en 37 filas, y es el tercer pase consecutivo que no agrega
> agentes a propósito.** Este pase ejecutó la acción que el pase 19 dejó escrita como «la pregunta de mayor rendimiento»
> y que el pase 20 no tomó: **confirmar el borrado en la capa de telemetría (gap 33)**. Se ejecutó **clonando los tres
> LRS y leyendo el código fuente**, y 🔴 **el gap 33 se cierra refutado**: `lrsql` (**Apache-2.0**), el almacén que esta
> KB recomienda como default para **P1**, **P10**, **P14** y **P15**, expone `DELETE /admin/agents` —borrado **por
> `actor-ifi`**, en cascada sobre 7 tablas, transaccional— y **viene apagado de fábrica**. Durante catorce pasadas esta
> KB afirmó lo contrario **leyendo documentación en vez de código**, y tenía la nota de límite escrita al pie que lo
> advertía. Lo que queda abierto es la **evidencia** (**gap 36**, el más chico y upstreameable de esta KB) y el
> **disparador LMS→LRS** (**P40**), no la capacidad. Entra **ILIAS** a `verticals/solutions.md`, cuyo Feature Wiki
> documenta ese mismo agujero por escrito. Se reverificó **DeepTutor** de primera mano (**40.6k ★**, Apache-2.0,
> **v1.6.12** del 2026-09-27), coincidente con el pase 20. Ver las tendencias **54**, **55** y **56**, el **gap 36** y
> el patrón **P44**.

> *Pase 20 del 2026-10-01:* **no se agregó ninguna fila a la tabla principal — la tabla sigue teniendo 37 filas**, y
> eso es deliberado. Este pase no buscó tutores: buscó **la máquina que prueba que un tutor cumple**, que es lo que
> esta KB viene prometiendo en `P4`, `P10`, `P11`, `P17` y `P39` desde el pase 4 **sin tener registrada una sola
> herramienta de testing**. La máquina existe, es **Apache-2.0**, la publica **un regulador nacional** (IMDA de
> Singapur, vía la AI Verify Foundation) y trae *benchmarking* + *red-teaming* con un **Starter Kit v1.0 de enero de
> 2026** detrás. Y el hallazgo es lo que **no** tiene: su propio catálogo de evaluaciones cubre **derecho, medicina y
> finanzas — educación no está**. Se abre la **capa de testing de conformidad** al final de este archivo, se abre el
> **gap 35**, y entra **Singapur** a esta KB, que en diecinueve pasadas la nombró una sola vez y de pasada. Ver las
> tendencias **51**, **52** y **53** y los patrones **P42** y **P43**.

> *Conteo del pase 19, con la regla del pase 17 aplicada de forma consistente:* la tabla tiene **37 filas**. Dos no son
> agentes sino **bibliotecas de skills** — `education-agent-skills` (165 skills en 20 dominios) y **`human-skill-tree`**
> (33 skills, nuevo en este pase) —: son catálogos de pedagogía empaquetada, no un tutor. Las otras tres piezas nuevas
> entregadas como skill (**universal-examprep-skill**, **universal-diagnostic-tutor-skill**, **algo-sensei**) **sí** cuentan
> como agentes, por el mismo criterio con el que esta KB ya contaba a `Alvarmethod` y `Gnos`: cada una es **un** tutor
> coherente con su propio loop pedagógico, no un catálogo. **37 = 35 + 2.**
> *Pase 11 del 2026-10-01:* +3 en la tabla principal (**learn**, **Gnos**, **Alvarmethod**) y una **capa predictiva / early warning** nueva al final del archivo, que es la capa peor abastecida de esta KB y la que el Anexo III del EU AI Act nombra de forma explícita.
> *Pase 12 del 2026-10-01:* +1 en la tabla principal (**Study-Mate**), +1 en la capa MCP (**anki-mcp-server**, que
> multiplica por 499 el techo de esa capa) y +1 en evaluación (**ArguLens**). Se abre la **capa de distribución por
> skills de agente** al final del archivo: es la primera capa de esta KB que se mide contra otra vertical, y la
> educación pierde 58× contra la científica en el mismo canal. El conteo de 29 de la tabla principal se verificó a
> mano en este pase y **estaba bien**.
> *Pase 19 del 2026-10-01:* **+5 en la tabla principal** (**human-skill-tree**, **universal-examprep-skill**,
> **algo-sensei**, **universal-diagnostic-tutor-skill**, **lumen**) y **una región cerrada** (lumen → Alemania).
> Pero el trabajo principal de este pase es **corregir al pase 18, y en tres cosas distintas**, porque su hallazgo
> central se apoyaba en una causa falsa. Verificado con `git ls-remote` y con un clon *sparse* del árbol real:
>
> 1. 🔴 **`moodle/moodle` SÍ tiene rama `main`.** El pase 18 escribió textualmente que *«no tiene rama `main` ni rama
>    `master`»* y con eso explicó los cuatro 404 del pase 17. **Es falso:** `refs/heads/main` existe y apunta a
>    `85af0b5` = **Moodle 5.3rc1**. La causa real de los 404 es otra y es más útil: **Moodle movió su *webroot* al
>    subdirectorio `public/` en la serie 5.x.** La ruta no es `ai/provider/ollama/...` sino
>    `public/ai/provider/ollama/...`. Los 404 midieron **la ruta**, no la rama.
> 2. 🔴 **No son tres `privacy provider` de AI: son siete**, más uno del subsistema y dos de *placement* = **10
>    archivos**. Los siete son `anthropic`, `awsbedrock`, `azureai`, `deepseek`, `gemini`, `ollama` y `openai`.
> 3. 🔴 **Y los siete no sirven de plantilla de borrado, porque no borran nada.** Auditados uno por uno: 70–78 líneas
>    cada uno, **cero** llamadas a `delete_records`/`DELETE FROM`/`add_database_table`, y **exactamente un**
>    `add_external_location_link`. Todos sus métodos de borrado tienen **el cuerpo vacío** y están marcados
>    `@codeCoverageIgnore`. La plantilla real existe pero es **otra**: `public/ai/classes/privacy/provider.php`
>    (`core_ai`), ~800 líneas, **6 tablas** —incluidas `prompt` y `generatedcontent`— con `delete_records_list` de
>    verdad. El pase 18 nombró a los shims y no a la plantilla.
>
> **Lo que esto significa, y es el hallazgo del pase:** los siete shims no son un descuido, son una **declaración**.
> Lo único que hacen es declarar que el *prompt* del alumno y el modelo **salen hacia un tercero**. El núcleo de
> Moodle documenta así, en siete lugares, el punto donde su propia maquinaria de supresión **se queda sin nada que
> suprimir**. Ver las tendencias **48**, **49** y **50**, los patrones **P40** y **P41**, y el **gap 32**, que este
> pase **cierra refutándolo**.
> *Pase 18 del 2026-10-01:* se cierra el **gap 29** y **no lo cierra un tercero: lo cierra el núcleo de Moodle**, que
> trae **tres** `privacy provider` de referencia para plugins de AI (`openai`, `azureai`, `ollama`). Se corrige por qué
> el pase 17 no los vio —**`moodle/moodle` no tiene rama `main` ni `master`**, y sus cuatro 404 midieron el nombre de
> la rama, no una ausencia— y con eso el Privacy API pasa de *documentado por snippet* a **verificado de primera
> mano**. Se abre además la **capa de *unlearning***, que ejecuta la segunda acción escrita del pase 17 y confirma su
> predicción: la oferta existe, es grande y es **toda MIT/Apache**, al revés que la capa de borrado del LMS. La pieza
> más completa de `privacy provider` de toda la capa es **brasileña** (`local_aihub`), lo que mueve el **gap 2** otra
> vez. Se abren el **gap 31** y el **gap 32**. Ver las tendencias **45**, **46** y **47**, y los patrones **P38** y **P39**.
> *Pase 17 del 2026-10-01:* **no se agregó ninguna fila a la tabla principal.** Se contó a mano y **la tabla tiene
> 32 filas, no 31** — pero el encabezado es defendible y conviene registrar por qué, porque es la tercera vez que
> esta KB se pelea con este conteo: **una de las 32 filas no es un agente.** `education-agent-skills` es una
> biblioteca de Markdown/YAML y está además listada en la capa de distribución por *skills* de este mismo archivo.
> **32 filas = 31 agentes + 1 paquete de skills duplicado de otra capa.** Se deja la fila donde está (sirve de
> puntero) y se deja anotado que no cuenta como agente. Se **cierra el gap 20**: ya existe skill educativa con *eval* publicada, es **Apache-2.0** y son
> dos repos co-desarrollados (`anthropics/k12-teacher-skills` **541 ★**, nuevo en esta KB, y
> `learning-commons-org/agent-skills` **35 ★**, que **ya estaba** en la enumeración del gap 20 y sí tiene
> `evals/` — el gap lo había dado por carente). Los dos con carpeta `evals/` verificada. Entran en la **capa de distribución por skills** al final del archivo,
> que sube su techo permisivo de **299 a 541 ★**. Se reverificó **DeepTutor**: **40.6k ★**, v1.6.12 del
> **2026-09-27** — la fila ya estaba correcta. Y se refina el encuadre COPPA del pase 16: ver la corrección abajo.
> Se abren el **gap 29** y el **gap 30**. Ver las tendencias **42**, **43** y **44**, y los patrones **P36** y **P37**.
> *Pase 16 del 2026-10-01:* **no se agregó ninguna fila a la tabla principal; el conteo de 31 se mantiene.**
> Se abre la **capa de privacidad del dato del alumno** en `repos/foundations.md` —DP, federado y datos
> sintéticos—, y **no entra acá a propósito: no son agentes, son librerías horizontales**, y ése es parte del
> hallazgo. Lo que sí es de esta tabla: **ninguno de los 31 agentes declara qué hace con el dato del alumno**, y
> desde el **2026-04-22** la **voz de un menor es dato biométrico regulado** bajo la regla COPPA enmendada, lo que
> le pone encuadre legal a la capa de voz que abrió el pase 14. Se abren el **gap 27** y el **gap 28**. Ver las
> tendencias **39**, **40** y **41**, y los patrones **P34** y **P35**.
> *Pase 15 del 2026-10-01:* **no se agregó ninguna fila a la tabla principal; el conteo de 31 se mantiene.**
> Se abre la **capa de autoría y procedencia** al final del archivo —la mitad que le faltaba a la capa de
> integridad académica del pase 8, que era sólo *proctoring*—. **El hallazgo es un error propio:** desde el pase 4
> esta KB le vende a EMEA el deadline de *watermarking* del **2026-12-02** y **nunca registró una implementación**.
> Existe, es **Apache-2.0** y viaja dentro de Hugging Face Transformers (**SynthID-Text**). Se abren el **gap 25**
> (la detección no se puede usar para acusar: **61,3 %** de falsos positivos sobre no nativos de inglés) y el
> **gap 26**. Ver las tendencias **36**, **37** y **38**, y el patrón **P33**.
> *Pase 14 del 2026-10-01:* **no se agregó ninguna fila a la tabla principal; el conteo de 31 se mantiene.**
> Este pase abre dos capas nuevas al final del archivo —**lectura oral y pronunciación** (la primera capa de voz
> de esta KB) y **puente agente↔currículo nacional** (que mueve el gap 15)— y cierra el **gap 19** con cuatro
> esquemas curriculares nacionales verificados, que viven en `repos/foundations.md`.
> *Corrección de conteo del pase 10:* el encabezado decía **24** y la tabla tenía **25** filas antes de este pase. El desfasaje venía de pasadas anteriores que agregaron filas sin actualizar el total. Contado a mano: **26** con la fila que agrega el pase 10.
> Bloom y OpenTutorAI-CE se agregaron en la segunda pasada del 2026-09-30.
> **Claw-ED** se agregó en la tercera pasada del 2026-09-30 — es el primer agente *teacher-facing* open source de la KB.
> **Cuarta pasada del 2026-09-30:** +5 agentes (pyKT, FreeLingo, TutorIA, OpenDidactia, mentar) y **2 regiones cerradas** (OpenTutorAI-CE → Marruecos; Claw-ED → EE. UU.). La capa de evaluación se movió a su propia sección y se corrigió: el repo canónico es `UnifyingAITutorEvaluation` (32 ★), no `AITutor-EvalKit` (3 ★).
> **Sexta pasada del 2026-09-30:** +1 en la tabla principal (**learnmcp-xapi**, el puente MCP hacia la capa de telemetría xAPI) y +1 en evaluación (**L2-Bench**, de Oxford University Press, que cierra el sub-gap de *lengua* — ⚠️ **no verificado de primera mano**, ver la advertencia en su fila). La capa de almacenamiento (los LRS) vive en `repos/foundations.md`, no acá: no son agentes.
> **Quinta pasada del 2026-09-30:** +2 en la tabla principal (**Aila**, de Oak National Academy, y **pyBKT**), +3 en evaluación (**SafeTutors**, **EduBench**, **EduGuardBench**) y una sección nueva de servidores MCP de mastery. **El gap 8 se corrige:** la capa teacher-facing open source no era un solo repo de 59 ★.

> **Séptima pasada del 2026-10-01:** +3 en la tabla principal (**llamatutor**, **ChatTutor**, **tutor-gpt**) y +1 en evaluación (**ProHist-Bench**). Los tres nuevos entraron por un cambio de consulta, no por ser nuevos: las seis pasadas anteriores buscaron `agent`, `benchmark` y `tutoring system`, **nunca `tutor`**, que es la palabra que usa el mercado. Suman 4.3k estrellas y **ninguno se puede empaquetar en un entregable cerrado** — ver las advertencias de licencia. Se registra además una **colisión de nombres** con `Bloom` y la **capa de datos de entrenamiento** (ver `repos/foundations.md`), que es la que decide si `pyKT`/`pyBKT` sirven de verdad.

> **Octava pasada del 2026-10-01:** se abre una **capa que la KB no tenía en siete pasadas — accesibilidad y educación especial** (sección nueva abajo, 11 repos verificados). El hallazgo no es un repo: es la forma del segmento. **Lo maduro es copyleft** (OptiKey 4.4k ★ GPL-3.0, Cboard 759 ★ GPL-3.0) y **lo que es agéntico y permisivo no pasa de 15 estrellas**. Entra además **`tero`** (MIT, Chile) en la tabla principal, que es la primera pieza de esta KB que cierra tres gaps a la vez (2, 8 y 12). Ver el **gap 12** y el **trend 18** en `intel/trends.md`, y los patrones **P17** y **P18**.

> **Novena pasada del 2026-10-01:** se abre la **capa de credenciales verificables e interoperabilidad** (sección nueva abajo). Es la capa que acredita el aprendizaje cuando termina — Open Badges 3.0, W3C Verifiable Credentials, QTI, OneRoster, Caliper — y ocho pasadas no la buscaron porque no se llama «agente» ni «tutor». **El hallazgo no es un repo: es que tres implementaciones de referencia de estos estándares ya no están** (`badgr-server` 404, `caliper-php` puesto en privado por 1EdTech según el banner del fork de la U. de Michigan, `caliper-python` 404) mientras los estándares siguen siendo obligatorios. Lo que queda vivo y permisivo es de **terceros certificados y consorcios universitarios**. Ver el **trend 19**, los **gaps 13 y 14** y los patrones **P19**, **P20** y **P21**.

> **Décima pasada del 2026-10-01:** se abre la **capa de contenido curricular** — de qué lee el tutor. Nueve pasadas construyeron el agente, el modelado, la evaluación, la seguridad, la telemetría, los datos, la accesibilidad y la credencial, y **ninguna preguntó de dónde sale el material que el agente enseña**: la palabra «OER» no aparecía ni una vez en esta KB. **El hallazgo es una trampa de licencia que pega sobre el patrón P1 de esta KB**, y está verificada contra el archivo `LICENSE` de los repos: los bundles de contenido de **OpenStax publicados en GitHub dicen CC BY-NC-SA** en los tres títulos revisados, mientras el único puente agente↔contenido que existe (`openstax-mcp-server`) **anuncia en su README que el contenido es CC BY 4.0**. Entra ese puente en la tabla principal. Ver el **trend 22**, los **gaps 15 y 16** y los patrones **P22**, **P23** y **P24**.

> **Pase 13 del 2026-10-01:** +2 en la tabla principal (**jupyter-ai** y **Shiksha Copilot**) y +1 en evaluación
> (**pedagogy-benchmark**). Se abre en `repos/foundations.md` la **capa de práctica y corrección desplegada (Jupyter)**:
> doce pasadas preguntaron qué hace el agente y ninguna preguntó **dónde hace el alumno el trabajo**. La respuesta son
> cinco repos **BSD-3-Clause**, 14.334 ★, desplegados en universidades desde 2014, con runtime de agente y MCP ya
> incluido — y **corrige el gap 6**, que en once pasadas afirmó que la corrección open source no existía. Los otros dos
> hallazgos del pase son de encuadre: **pedagogy-benchmark** es MIT y está construido sobre **exámenes de habilitación
> docente del Ministerio de Educación de Chile**, y **Shiksha Copilot** documenta **1.043 docentes** con **9 estrellas**.
> Ver los **trends 30, 31 y 32**, los **gaps 21 y 22** y los patrones **P29** y **P30**.

> **Pase 46 del 2026-10-02:** **la tabla se queda en 66 filas, y es el CUARTO pase consecutivo con cero altas de
> agente — ya no es una observación, es una propiedad medida del canal.** Las cuatro búsquedas globales obligatorias
> (año **calculado**: 2026) devolvieron otra vez la **capa genérica** y **material didáctico *sobre* AI**; el único
> nombre nuevo del barrido vertical, **CK-ERP** (32 módulos, incl. `Teacher`/`Student`/`Registrar`), **no entra**:
> su rastro vivo más reciente es de **2010**. **El valor del pase está en las tres acciones del 45, y dos corrigen
> afirmaciones de esta base.** 🔴 **La corrección que más cuentas cambia cae sobre la cotización de *proctoring*:
> P94 publicaba *«métodos que hablan con el remoto: Jitsi 1, Zoom 2»* y la medición transitiva sobre `HEAD 7f45689`
> da **Zoom 5 de 14 — y 0 directos**.** Los cinco llegan al socket por helpers privados, `disposeServiceRoomsForExam`
> a **profundidad 4 y dentro de un `forEach`** (`2 × N` peticiones, sin tope), y **crear una sala cuesta 3 llamadas**
> porque `createAdHocMeeting` crea un usuario ad-hoc. 🟢 **A favor: todo el HTTP de Zoom sale por un único `exchange`
> con *circuit breaker*** — un solo punto donde poner reintentos. 🟢 **Y el gap 95 cierra con código:** el componente
> transversal del **Artículo 50(2)** existe (`compose/code/aiact-50-2-marking/`, **24/24**), mapea los **9 valores**
> de `lineage-skill` a `synthetic` **conservando la etiqueta**, y **la decisión que nadie había tomado son CINCO
> valores, no cuatro** — `unsupported` se marca, porque si ninguna fuente sustenta la afirmación ninguna fuente la
> escribió tampoco. ⚠️ **Y el error simétrico queda escrito: las cuatro categorías humanas devuelven `false` a
> propósito** — marcar como AI un tramo del alumno es dato incorrecto, no cautela. 🟢 **Gap 97 decidido a favor:
> marcar en el empaquetado SCORM NO rompe la conformidad** (`xmllint` contra `imscp_v1p1.xsd`: con *namespace*
> propio **valida**, en el *namespace* por omisión **falla**), así que el marcado se inyecta **una vez** y no 32.
> Ver las tendencias **184**–**196**, los **gaps 95, 96 y 97 (los tres CERRADOS)**, **98**–**101**, y los patrones
> **P102**–**P105**.

| Nombre | Repo | Licencia | Stars | Lenguaje | Descripción | Origen (región) |
|--------|------|----------|-------|----------|-------------|-----------------|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 40.6k | Python | Tutoría personalizada "lifelong"; workspace agent-native con 8 superficies (Chat, Partners, Co-Writer, Book, Knowledge, Space, Memory), memoria en 3 capas y RAG multi-engine. v1.6.12 del 2026-09-27, releases semanales | APAC (HKU Data Intelligence Lab, Hong Kong) |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 39.7k | TypeScript | Open Multi-Agent Interactive Classroom: convierte un tema o documento en una clase interactiva multi-agente. Agent workbench, sesiones durables de course-building, skills reutilizables, persistencia pluggable. v1.1.2 del 2026-09-28. ⚠️ **Relicenciado de AGPL-3.0 a MIT en v0.3.0 (2026-06-28)**: la licencia permisiva tiene ~3 meses, no es el historial completo del proyecto | APAC (Tsinghua / THU-MAIC, China) |
| Project NOMAD | https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | 38.8k | JavaScript | Servidor de conocimiento y educación offline-first: Wikipedia, libros, cursos, mapas y AI local opcional, todo en Docker sobre hardware propio, sin internet. ~5 GB disco, <1 GB RAM sin el módulo AI | North America (Crosstalk Solutions, EE. UU.) |
| AI-Researcher | https://github.com/HKUDS/AI-Researcher | 🔴 **sin licencia** (no hay `LICENSE` ni `LICENSE.md` ni `LICENSE.txt` en `main` ni en `master`, medido por `raw.githubusercontent.com`; el `README.md` del mismo árbol da **200**, así que la ausencia está medida y no es del canal) | 5.8k | Python | ⚠️ **Automatización del ciclo de investigación de punta a punta** (idea → experimento → paper), *Spotlight* en NeurIPS 2025, arXiv:2505.18705. 🔴 **No es educativo: no menciona enseñanza, alumnos ni cursos.** Entra como **capacidad de laboratorio APAC**, no como pieza de aula, y **sin licencia no se puede entregar**: el default legal es «todos los derechos reservados» | 🔵 **APAC** (HKUDS, Universidad de Hong Kong) |
| AIMLInterviews (MCP tutor) | https://github.com/alirezadir/AIMLInterviews | **MIT** ✅ (`main:LICENSE` → *«MIT License»*, `raw`, pase 51) | 9.8k | Python/Markdown | ⚠️ **La fila mide el PAQUETE npm `aimlinterviews-mcp` 0.1.2, no el repo.** El repo es un **currículo** de entrevistas de ML/AI —la clase que los pases 46–48 rechazan como *material didáctico sobre AI*—, pero el servidor MCP publicado desde él **sí es un tutor**: convierte un asistente en examinador «a prueba de spoilers» sobre ese currículo, con la política pedagógica implementada en el servidor. 🔵 **Entró clasificando el ARTEFACTO y no el repositorio** (ver `agents/trending.md`, pase 51) | North America |
| jupyter-ai | https://github.com/jupyterlab/jupyter-ai | **BSD-3-Clause** ✅ | 4.4k | Python/TypeScript | **El runtime de agente del entorno donde el alumno efectivamente trabaja**, y la pieza que doce pasadas de esta KB no vieron. «Connects AI agents to computational notebooks in JupyterLab»: habla **Agent Client Protocol (ACP)** y **servidores MCP propios**, y autodetecta los agentes instalados (Claude, Codex, GitHub Copilot, Gemini, Goose, Kiro, Mistral Vibe, OpenCode). No es un tutor: es el lugar donde el tutor se enchufa al cuaderno del alumno. Su pila de corrección y despliegue —JupyterHub, nbgrader, otter-grader, ltiauthenticator— está en `repos/foundations.md` y es **toda BSD-3-Clause**. *Agregado en el pase 13* | Global (proyecto Jupyter / NumFOCUS) |
| Paper2Slides | https://github.com/HKUDS/Paper2Slides | **MIT** ✅ (`LICENSE` leído por `raw.githubusercontent.com`, **200**) | 3.8k | Python | 🟢 **Paper → presentación o póster en un paso**, con agentes LLM y generación de láminas en paralelo. ⚠️ **No se presenta como educativo** —no nombra clase, docente ni currículo— **pero es la pieza más cercana a material de cátedra que esta base tiene**: convierte un documento en láminas, que es el 80 % del trabajo de armar una clase a partir de un paper. Declara tres vecinos de la misma org: `LightRAG`, `RAG-Anything` y `VideoRAG` | 🔵 **APAC** (HKUDS, Universidad de Hong Kong) |
| learn | https://github.com/amosblomqvist/learn | 🚫 **sin licencia** | 2.9k | TypeScript/Markdown | "My AI learning system": no es software, es una **configuración `.pi`** —una skill con la filosofía de enseñanza, unas extensiones chicas y definiciones de subagentes (researcher, generadores de SVG y Mermaid)— que entrega lecciones, verifica datos, hace preguntas de quiz con feedback y loguea el progreso en Markdown. **El artefacto educativo más estrellado creado en esta ventana, y tiene 2 commits.** 🚫 No reutilizable: sin archivo de licencia el default legal es todos los derechos reservados. *Agregado en el pase 11* | Sin región declarada |
| llamatutor | https://github.com/Nutlope/llamatutor | 🚫 **sin licencia** | 2.1k | TypeScript | Tutor personal sobre **Llama 3 70B + Together.ai**: Next.js + Tailwind, Exa.js para búsqueda web y Helicone para observabilidad. Es una aplicación de producción, no una librería. 132 commits. 🚫 **No reutilizable:** se pidió `/blob/main/LICENSE` y devuelve **404** — sin archivo de licencia el default legal es todos los derechos reservados, con 2.1k estrellas o con ninguna. *Agregado en el pase 7* | Sin región declarada |
| VideoAgent | https://github.com/HKUDS/VideoAgent | **MIT** ✅ (`LICENSE` leído por `raw.githubusercontent.com`, **200**) | 1.9k | Python | ⚠️ **Marco agéntico único para entender, editar y rehacer video** (EMNLP 2026). 🔴 **No menciona educación.** Relevancia para esta base: la **clase grabada** es el activo de video más grande de cualquier institución, y esta es la única pieza permisiva de la KB que la toma como entrada editable. ⚠️ **No confundir con su vecino `VideoRAG`, que es MIT sólo en la arquitectura y NO comercial tal como se embarca** (tendencia 223) | 🔵 **APAC** (HKUDS, Universidad de Hong Kong) |
| ChatTutor | https://github.com/HugeCatLab/ChatTutor | **AGPL-3.0** ⚠️ | 1.3k | TypeScript | Tutor **visual e interactivo**: canvas de matemática para ecuaciones y diagramas y mapas mentales para visualizar conocimiento, **expuestos al LLM como herramientas que usa mientras explica** — es el único agente de esta KB que le da al modelo instrumentos de pizarrón en vez de sólo texto. Desplegado en `chattutor.app` con API key del usuario. README bilingüe inglés/中文. *Agregado en el pase 7* | Sin país declarado (documentación EN/中文) |
| tutor-gpt | https://github.com/plastic-labs/tutor-gpt | **GPL-3.0** ⚠️ | 931 | TypeScript | Compañero de aprendizaje con **razonamiento de teoría de la mente**: modela el estado mental del alumno —qué entiende, qué cree mal, con qué intención pregunta— y **reescribe sus propios prompts** en función de eso. Es un eje **complementario** al knowledge tracing de `pyKT`/`pyBKT`, no un sustituto: aquél modela qué conceptos domina, éste qué está pensando. Next.js + Supabase, inferencia vía OpenRouter, personalización delegada a **`Honcho`** (ver `repos/foundations.md`). 356 commits. ⚠️ Su versión hospedada se llama **"Bloom"** — **no es el `Bloom` de esta tabla**, ver la advertencia abajo. *Agregado en el pase 7* | **North America (EE. UU.)** — el perfil de la organización declara `United States of America` y `plasticlabs.ai` |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 ⚠️ | 815 | Markdown/YAML | 165 skills pedagógicas evidence-grounded en 20 dominios (pedagogía, learning science, currículo, evaluación) para orquestar agentes. Corre en Claude Code, Claude.ai vía MCP, Codex y Hermes | EMEA (autor UK) |
| py-fsrs | https://github.com/open-spaced-repetition/py-fsrs | MIT | 499 | Python | Free Spaced Repetition Scheduler: modelo DSR (Difficulty, Stability, Retrievability) con 21 parámetros optimizables. La pieza de scheduling que le falta a casi todo tutor LLM | Global (org open-spaced-repetition) |
| Educhain | https://github.com/satvik314/educhain | MIT | 389 | Python | Genera contenido educativo con GenAI: MCQs, lesson plans con 8 enfoques pedagógicos, flashcards. Ingesta desde YouTube, imágenes, URLs y PDFs | APAC (Build Fast with AI, India) |
| pyKT | https://github.com/pykt-team/pykt-toolkit | MIT | 441 | Python | Librería de **knowledge tracing** sobre PyTorch: preprocesamiento estandarizado de 7+ datasets, 5 escenarios de predicción y 10+ modelos DLKT comparables entre sí. 811 commits. **No es un agente: es la pieza que le falta a los agentes** — el modelo de estado del alumno que ningún tutor LLM tiene | APAC (Jinan University / Guangdong Institute of Smart Education, China) |
| Gnos | https://github.com/madhvantyagi/Gnos | MIT ✅ | 304 | Python | *Teaching harness* hecho de skills, scripts y herramientas visuales: toma un objetivo de aprendizaje con preferencias de profundidad y tiempo, arma el curso con subagentes que después revisa, y genera gráficos con **JSXGraph**, búsqueda en Khan Academy, PDFs y video. **La decisión de diseño que lo hace citable:** su registro de evidencia distingue *vio la explicación* / *resolvió con ayuda* / *resolvió solo* — es la distinción que casi ningún tutor LLM instrumenta, y es la que hace falta para cualquier medición de mastery. Guía docente en archivos `SOUL.md`. 344 commits. Corre en Codex, Claude Code, OpenCode y Antigravity. *Agregado en el pase 11* | Sin región declarada |
| FreeLingo | https://github.com/artcc/freelingo | **AGPL-3.0** ⚠️ | 150 | Python | Plataforma self-hosted de aprendizaje de idiomas con AI: evalúa nivel CEFR con un LLM local (Ollama) o cloud, genera plan de estudio personalizado, tutor conversacional por voz, flashcards y repetición espaciada. FastAPI + Next.js + Postgres + Redis, todo en Docker Compose | Sin región verificada (el repo no declara ubicación) |
| Bloom | https://github.com/Li-Evan/Bloom | MIT | 278 | Python | Tutor personal que genera un syllabus, entrega una lección a la vez, lee anotaciones y feedback y ajusta la siguiente lección al nivel real de comprensión. Dos modos: CLI como skill de Claude Code (sin backend) y web self-hosted (React + FastAPI, cualquier LLM OpenAI-compatible) | Sin región verificada |
| pyBKT | https://github.com/CAHLR/pyBKT | MIT | 281 | Python | **Bayesian Knowledge Tracing en Python**, del mismo laboratorio que OATutor. Estima mastery cognitivo desde secuencias de resolución de problemas, con variantes que individualizan parámetros por alumno y tasas de aprendizaje por ítem. 379 commits, publicado en **EDM 2021** (Badrinath, Wang & Pardos). Tampoco es un agente: es la alternativa **de procedencia estadounidense** a pyKT en la capa de modelado — más interpretable, menos potente (BKT clásico vs. deep learning). *Agregado en el pase 5* | North America (CAHLR, UC Berkeley) |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 265 | JavaScript | Intelligent Tutoring System con Bayesian Knowledge Tracing para estimar mastery. Deploy en dos clicks a GitHub Pages, A/B testing incorporado, 3 libros de contenido curado (OpenStax) en JSON | North America (CAHLR, UC Berkeley) |
| Alvarmethod | https://github.com/vasanthsreeram/Alvarmethod | MIT ✅ | 160 | Shell/Markdown | **Pedagogía empaquetada como skill portable**, instalable con `npx skills add vasanthsreeram/Alvarmethod -g --all` en Claude Code, Codex, Grok, Pi, OpenCode y Cursor a la vez. Implementa un loop explícito de cuatro pasos: *probe* (MCQ calificado para ubicar el hueco), *plan* (DAG en Mermaid armado para ese alumno), *teach* (un solo paso de razonamiento por vez, con visuales opcionales) y *lock-in quiz* con remediación. **Sólo 4 commits:** es una especificación pedagógica, no un producto — y eso es justamente lo que la hace reusable. Ver la tendencia 9 en `intel/trends.md`. *Agregado en el pase 11* | Sin región declarada |
| OpenTutor | https://github.com/zijinz456/OpenTutor | MIT | 127 | Python | Workspace de aprendizaje adaptativo block-based que corre local: subís material → notas, quizzes, flashcards y tutor adaptativo. FSRS + detección de carga cognitiva, 10+ providers LLM | Sin región verificada |
| OpenTutorAI-CE | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 107 | Python | Plataforma de tutoría personalizada: multi-model, RAG local, interacción por voz y video, control de acceso por roles. PWA multilingüe (árabe, francés, inglés). Community Edition que sirve de base a una Enterprise Edition | **EMEA (Marruecos)** — el perfil de la organización declara `Morocco` y `opentutorai.com`. *Región cerrada en el pase 4* |
| Aila (Oak AI Lesson Assistant) | https://github.com/oaknational/oak-ai-lesson-assistant | MIT | 35 | TypeScript | Asistente de **planificación de clases para docentes** de **Oak National Academy** (nonprofit educativa británica respaldada por el gobierno). Monorepo Turborepo: Next.js + Prisma/PostgreSQL con **pgvector**, entornos de producción y staging, versionado semántico. **1.188 commits** — es el único artefacto teacher-facing de esta KB que corre en producción real y publica su código. ⚠️ El repo declara que está *"intended primarily for internal use by Oak National Academy"*: úsese como **referencia de arquitectura**, no como base de producto (sin API estable ni soporte para terceros). *Agregado en el pase 5* | EMEA (Oak National Academy, Reino Unido) |
| LinguaMCP | https://github.com/Marsmanleo/LinguaMCP | **Apache-2.0** ✅ (`main:LICENSE` → *«Apache License»*, `raw`, pase 51) | 1 | TypeScript | Protocolo de **currículo abierto para tutores de idiomas**: define el currículo como dato y deja que cualquier herramienta de AI lo conduzca, con práctica diaria en vez de lecciones cerradas. npm `lingua-mcp` **0.3.0**. ⚠️ **1 ★ y 0 forks: es una apuesta de diseño, no una pieza probada en producción** | n/d (sin señal de origen) |
| mcp-geralearn | ⚠️ `geraservicesuk/mcp-geralearn` → 🔴 **404 por DOS canales** (`raw` en 6 ramas y `github.com`) · npm [`@gera-services/mcp-geralearn`](https://registry.npmjs.org/@gera-services/mcp-geralearn/latest) ⚠️ *(se enlaza el REGISTRO, que responde 200; `npmjs.com` da 403 por curl y por WebFetch y no se puede verificar)* | **MIT** ✅ 🔵 **texto medido en el TARBALL** (`package/LICENSE` → *«MIT License»*), porque el repo declarado no existe | n/d | TypeScript | Servidor MCP de la plataforma educativa **GeraLearn**: navegar cursos, matricularse en formaciones, seguir progreso y encontrar tutores en **50+ países**. 🔵 **Clase inversa a `@timadey/proctor`: el repositorio no responde y la licencia SÍ viaja en el artefacto que se instala** | EMEA (Reino Unido, por el titular `geraservicesuk`) |
| @schoolexl/mentor | ⚠️ **no declara repositorio** · npm [`@schoolexl/mentor`](https://registry.npmjs.org/@schoolexl/mentor/latest) ⚠️ *(se enlaza el REGISTRO, que responde 200; `npmjs.com` da 403 por los dos canales)* | **MIT** ✅ 🔵 **texto medido en el TARBALL** (`package/LICENSE` → *«MIT License»*) | n/d | TypeScript/React | UI React *drop-in* para **tutores AI en tiempo real**: chat, voz en vivo y **avatar con labios sincronizados** sobre **LiveKit**, temizable, con cliente tipado y hook de React. 🔵 **Es la primera pieza de esta tabla que resuelve la CAPA DE PRESENTACIÓN del tutor en vez del razonamiento** | n/d (sin señal de origen) |
| Shiksha Copilot | https://github.com/microsoft/Shiksha-Copilot | **MIT** ✅ | 9 | Python/TypeScript | **El despliegue docente más grande documentado en esta KB, y tiene 9 estrellas.** De **Microsoft Research India** (iniciativa VELLM): genera planes de clase alineados al currículo, ejemplos, analogías, actividades y evaluaciones formativas y sumativas. Pipeline de ingesta curricular (MinerU, SmolDocLing, OlmOCR), datastores vectorial + grafo + documental, frontend React y backend FastAPI. Investigación publicada sobre **1.043 docentes de Karnataka (India)** trabajando en **inglés y kannada**. 149 commits. ⚠️ **El propio repo declara que es un prototipo de investigación, «not extensively tested for production use», con supervisión humana obligatoria y no apto para despliegue comercial sin validación extensa** — citarlo como evidencia de que la categoría funciona a escala, no cotizarlo como componente. *Agregado en el pase 13* | APAC (India — Microsoft Research India, despliegue en Karnataka) |
| tutor-mcp | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 42 | Go | Servidor MCP que convierte cualquier LLM en un ITS: estado durable del aprendiz, scheduling de repaso, memoria de sesión, misconceptions, metacognición y decisiones pedagógicas auditables | Sin región verificada |
| learnmcp-xapi | https://github.com/DavidLMS/learnmcp-xapi | MIT | 15 | Python | Servidor MCP que le da a un agente memoria de aprendizaje **conforme al estándar**: tres tools sobre un Learning Record Store xAPI — registrar un statement, consultar el historial de progreso y gestionar el vocabulario de verbos/actividades. Backends: `lrsql`, `Ralph`, Veracity Learning, más arquitectura de plugins. Captura el aprendizaje de forma explícita ("practiqué bucles") o **inferida de la conversación**, y después consulta ese historial para adaptar la respuesta. **Es el único artefacto de esta KB que conecta un agente con IEEE 9274.1.1 (xAPI 2.0)** en vez de inventar su propio esquema. ⚠️ 32 commits: referencia de integración o base a forkear, no dependencia de producción. 🟢 **Pase 33 — lo que la ficha no registraba, leído del README (293 líneas):** la selección de LRS es **por variable de entorno** (`LRS_PLUGIN=lrsql \| ralph \| veracity`) con configuración por backend en `config/plugins/<backend>.yaml` (endpoint, credenciales, `retry_attempts`), Basic Auth y **OIDC** según lo que pida el LRS, y **privacidad por diseño**: un `ACTOR_UUID` por alumno con la afirmación *«No personal information is stored — only learning activities and progress indicators»*. 🔴 **Y una medición que cambia cómo se la busca: no está publicada en ningún registro de paquetes** — PyPI **404**, npm **`total: 0`** — así que se instala **desde el código** (*from source*, `venv` o `uv`). **Por eso el barrido del gap 60 no la encontró** (tendencia **107**). ⚠️ **Gap 63:** fuentes secundarias mencionan un **`2.0.0`** con *«complete redesign with a modular LRS plugin system»*, que dejaría vencido el *«no se movió»* del pase 25; **sin verificar** (`github.com/releases` da 403 y no hay `pyproject.toml` en la raíz de `main`). *Agregado en el pase 6; medido de nuevo en el pase 33* | ⚠️ **EMEA (España), con el matiz del pase 33.** El autor declara pertenecer al **IES Rafael Alberti**, instituto público de secundaria — lo escribió un docente en ejercicio, no un laboratorio. **Pero el `LICENSE` del repo dice textualmente `Copyright (c) 2025 David Romero`: el titular verificable es una persona, no la institución.** Las dos cosas son compatibles; para el argumento de soberanía europea en licitación conviene **Ralph** (France Université Numérique), cuyo titular institucional sí está en el archivo de licencia |
| openstax-mcp-server | https://github.com/pythpythpython/openstax-mcp-server | MIT (código) ✅ | 1 | TypeScript | Servidor MCP que le da a un agente acceso a **40+ libros de texto de OpenStax**: búsqueda semántica con embeddings de Cloudflare AI, generación automática de notebooks `.ipynb` por módulo y creación de problemas de práctica. Corre en Cloudflare Workers con Workers KV para cachear el XML parseado. **Es el único puente agente↔contenido curricular que encontró esta KB** — el equivalente, en la capa de contenido, de lo que `learnmcp-xapi` es en la capa de telemetría. 🔴 **Y hay que leerlo con la advertencia puesta: su README declara que el contenido servido es «Creative Commons Attribution 4.0 International (CC BY 4.0)», y el archivo `LICENSE` de los bundles de OpenStax en GitHub dice CC BY-NC-SA** en los tres títulos que este pase verificó. El código es MIT y es reutilizable; **la afirmación de licencia del contenido no se puede usar como base de un entregable facturado sin verificar título por título.** 7 commits. *Agregado en el pase 10* | Sin región verificada |
| gradescope-mcp | https://github.com/Yuanpeng-Li/gradescope-mcp | MIT | 8 | Python | Servidor MCP para Gradescope: 34 tools de gestión de cursos, batch grading, CRUD de rúbricas y regrade review. Escrituras detrás de confirmación explícita | Sin región verificada |
| TutorIA | https://github.com/LabSirius/TutorIA | MIT | 0 | Python | Tutor conversacional autónomo para **educación superior rural**, integrado dentro de Open edX y con la API de Claude como motor. Chat en lenguaje natural, respuestas en audio (TTS), avatar animado, dashboard de estadísticas para el docente y persistencia de contexto entre sesiones. Materias iniciales: Programación I (Python) e Introducción a la Matemática | **LATAM (Pereira, Colombia)** — Grupo Sirius, Universidad Tecnológica de Pereira (`sirius.utp.edu.co`) |
| OpenDidactia | https://github.com/nmarafo/OpenDidactia | CC BY-SA 4.0 ⚠️ | 0 | Markdown/YAML | Esquemas curriculares estructurados (estándar OKF) para que un agente genere **Programaciones Didácticas y Situaciones de Aprendizaje** conformes a la ley educativa española LOMLOE. Cubre las 17 comunidades autónomas y 2 ciudades autónomas, de Infantil a Bachillerato, FP y enseñanzas de régimen especial, con DUA y rúbricas analíticas. No es código: es el *esquema de salida* que hace auditable a un agente docente | EMEA (España) |
| mentar | https://github.com/avps82/mentar | **AGPL-3.0-only** ⚠️ | 1 | Python | Tutor local-first para chicos: corre entero en la máquina del hogar, sin cuentas ni datos que salgan del dispositivo. 934 nodos de concepto en 157 plantillas curriculares (Australia ACARA v9, India, Singapur, EE. UU.). **El detalle de diseño que importa:** el LLM sólo explica y un *checker determinístico* corrige cada respuesta, así que el modelo no puede darle por buena una respuesta incorrecta a un chico. Último commit 2026-08-26 | Sin región verificada (currículo AU primero, pero el repo no declara ubicación) |
| tero | https://github.com/marcorojasb/tero | **MIT** ✅ | 0 | Python | Agente docente de aula para K-12 **chileno**, de terminal y **offline-first**, sobre AWS Bedrock + Strands Agents SDK. Prepara material pedagógico y **adapta contenido para alumnos con necesidades especiales**. La decisión de diseño que lo hace citable: *«el agente propone, el docente decide»* — **el modelo no escribe archivos sin aprobación humana**. Anclado a instrumentos nacionales: MINEDUC, **Decreto 83** (educación especial) y **Ley 21.719** (protección de datos). 111 commits. **0 ★: referencia de arquitectura y contraparte local, no dependencia de producto.** *Agregado en el pase 8* | LATAM (Chile) |
| Study-Mate | https://github.com/Miaotofu01/Study-Mate | **MIT** ✅ | 482 | Python | Compañero de estudio con planificación curricular, instrucción y aprendizaje por proyectos en matemática y CS. *Workflow* integrado + motor de cursos HTML; corre sobre DeepSeek Harness, Google Antigravity y plugins de ChatGPT. 298 commits | APAC |
| human-skill-tree | https://github.com/24kchengYe/human-skill-tree | **AGPL-3.0** ⚠️ (dir. `skills/` en doble licencia MIT/AGPL-3.0) | 562 | TypeScript/Markdown | 33 skills de agente que convierten ChatGPT, Claude, Gemini y compatibles en acompañantes de aprendizaje estructurado, de K-12 a desarrollo profesional. Repetición espaciada y *active recall* explícitos, simulación de aula multi-agente, tutores socráticos y quizzes adaptativos. Declara cobertura de **15 sistemas educativos nacionales y 800+ materias** — es la pieza de mayor alcance curricular declarado de esta tabla. 36 commits. ⚠️ **La licencia es el dato que decide el uso:** el repo es AGPL-3.0 y sólo el directorio `skills/` está en doble licencia MIT/AGPL-3.0. Para un entregable cerrado **sólo es utilizable el subárbol de skills**, y conviene verificarlo archivo por archivo antes de facturar. *Agregado en el pase 19* | Sin región declarada (documentación bilingüe EN/中文) |
| universal-examprep-skill | https://github.com/ZeKaiNie/universal-examprep-skill | **MIT** ✅ | 299 | Python | Skill de preparación de exámenes que ingiere slides, apuntes, tareas y exámenes viejos (PDF, PPTX, DOCX, Markdown) y enseña **citando `archivo p.N` en cada concepto**, extrae figuras, examina con las preguntas reales de la materia, registra errores y arma guías de estudio. Memoria entre sesiones. Instalable con `npx skills add ZeKaiNie/universal-examprep-skill` en Claude Code, Cursor, Windsurf, Codex, Antigravity, Gemini CLI y 40+ agentes. 181 commits. **La propiedad que lo hace citable, y no es pedagógica sino regulatoria:** declara **citación obligatoria con número de página y 100 % de abstención fuera de alcance**, que es exactamente lo que pide el inciso (a) de la Decisión 33 de Vietnam —contenido de autoaprendizaje con *fuentes de datos no controladas* es alto riesgo—. Ver el patrón **P41**. *Agregado en el pase 19* | Sin región declarada |
| algo-sensei | https://github.com/karanb192/algo-sensei | **MIT** ✅ | 281 | Markdown (multi-lenguaje: Python, Java, C++, JS, Go) | Mentor de estructuras de datos y algoritmos que **se niega a dar la solución**: sistema de pistas de **cinco niveles** escalonados —desde la observación más suave hasta el esqueleto en pseudocódigo—, entrenamiento en reconocimiento dinámico de patrones (no plantillas memorizadas), método socrático declarado (*«learn through questions, not lectures»*) y cinco modos (Tutor, Hint, Review, Interview, Pattern Mapper). Su filosofía escrita es *«productive struggle with guidance»*. Corre en Claude Code y Claude.ai. **Sólo 8 commits:** es una especificación pedagógica, no un producto — el mismo perfil que `Alvarmethod`, y el andamiaje graduado es la contraparte operativa de lo que `Gnos` instrumenta como evidencia. *Agregado en el pase 19* | Sin región declarada |
| universal-diagnostic-tutor-skill | https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill | **MIT** ✅ | 235 | Markdown | Tutor *diagnosis-first* para STEM, matemática, programación y AI/CS: antes de enseñar **determina dónde está trabado el alumno**, con un ciclo de clarificar objetivo → localizar el hueco en cuatro niveles (materia → sistema de conocimiento → subtema → conceptos núcleo) → instrucción mínima dirigida → verificación → decisión de avance por mastery demostrada. Continuidad entre conversaciones mediante **«Learning State Cards» visibles** —el estado del alumno es inspeccionable por el alumno, no sólo por el sistema—, enrutamiento en lenguaje natural sin menús de modo y análisis cualitativo de error. v2.0.0 reduce ~41 % el contexto respecto de v1.9.2. Skill oficial de DeepSeek Harness, con variante *Lite Prompt* para chat estándar. 57 commits. *Agregado en el pase 19* | Sin región declarada |
| lumen | https://github.com/ahmedEid1/lumen | **GPL-3.0** ⚠️ | 88 | Python/TypeScript | Plataforma donde el alumno describe su objetivo y un orquestador multi-agente propio (**sin LangChain**) le construye el curso. **Modelo *learner-owned* declarado:** *«every signed-in user runs the whole loop themselves; `admin` only moderates and configures»* — el alumno define, construye, aprende, comparte y remezcla en un catálogo moderado. RAG **con alcance por curso y citación, detrás de un único autorizador**, con aislamiento explícito para que cursos privados y clonados no filtren datos. BYOK con credenciales cifradas, servidor MCP con 9 tools, PostgreSQL 17 + pgvector, decisiones del agente auditables en una tabla `llm_calls`. 828 commits, 1.421 tests de backend y 468 de frontend. **La decisión que lo hace citable:** su *eval harness* **publica también los puntajes malos** — es el único artefacto de esta KB que documenta sus propias debilidades medidas. ⚠️ GPL-3.0: referencia de arquitectura y despliegue propio, no base de un entregable cerrado. *Agregado en el pase 19* | **EMEA (Essen, Alemania)** — el perfil del autor (Ahmed Hobeishy) declara `Essen, Germany`. *Región cerrada en el pase 19* |
| canvas-mcp | https://github.com/vishalsachdev/canvas-mcp — 🟢 **P121 clase (a) (pase 53): `CANVAS_API_TOKEN`, y documenta el formulario de pedido a IT cuando la universidad cierra el self-service** | **MIT** ✅ 🟢 **texto verificado en el pase 50**: `main:LICENSE` → **200**, *«MIT License / Copyright (c) 2025 Vishal Sachdev»* | ⚠️ 269 — **no re-verificable acá, y un directorio de terceros dice 120: se reportan las dos sin elegir** | ⚠️ **TypeScript según esta fila; la tabla comparativa de `bruchris/canvas-lms-mcp` lo declara Python** — discrepancia registrada en el pase 50, sin resolver a favor de ninguno (no se midió el árbol) | **El conector permisivo de LMS más grande de esta KB.** Servidor MCP sobre la API de Canvas con **hasta 102–103 tools** (el README dice «up to 102» en el encabezado y «up to 103» en el resumen: se transcribe la ambigüedad del propio repo) y **8 *agent skills***. Es el primero de esta base que cubre **las dos puntas**: lado alumno (entregas, notas, TODO, *peer review*) y **lado docente** (gestión de tareas, corrección, analítica de alumnos, mensajería), más módulos, páginas, archivos, y un *Learning Designer* que incluye **escaneo de accesibilidad y chequeo WCAG** — la capa del pase 8 llega al conector. Trae `search_canvas_tools` para **descubrimiento de tools**, que es la respuesta a tener 100+: el agente busca la herramienta en vez de recibir las cien. 815 commits, 92 forks. ⚠️ Es *tool-side* sobre la API de Canvas: **no reemplaza el lado LMS** (ver el cierre del lado *platform*, abajo). *Agregado en el pase 26* | Sin región verificada |
| moodle-mcp-server (peancor) | https://github.com/peancor/moodle-mcp-server — 🟢 **P121 clase (a) (pase 53): `MOODLE_API_TOKEN` emitido desde la administración del sitio** | **MIT** ✅ | 43 | TypeScript | **La primera pieza permisiva de esta KB que escribe nota y devolución dentro de un LMS de producción**, y por eso la primera que toca el **gap 6** (corrección, abierto desde el pase 2) del lado del verbo correcto. **8 tools, cuatro de escritura:** `get_courses`, `list_students`, `get_assignments`, `get_student_submissions`, **`provide_assignment_feedback`** (pone nota y comentario en la tarea), `get_quizzes`, `get_quiz_attempts`, **`provide_quiz_feedback`**. Habla **Moodle Web Services** por token: **no se modifica el LMS**. 13 forks, 10 commits. ⚠️ **10 commits no son una base de producción** — es el punto de partida del último tramo, no el sistema de corrección. 🔴 Desmiente el **gap 43** del pase 26, que lo declaraba inexistente. *Agregado en el pase 27* | Sin región verificada |
| moodle-mcp (MarcosNahuel) | https://github.com/MarcosNahuel/moodle-mcp — 🟢 **P121 clase (a) (pase 53), la declaración más limpia de las once: «No cookie auth, no web scraping, no direct DB access»** | **MIT** ✅ | 1 | TypeScript | **El conector MCP de Moodle más completo que existe, y tiene 1 estrella** — el caso más puro del **gap 49** (los directorios rankean por promoción, no por capacidad). **40 tools** en 10 dominios: Curso (crear, actualizar, duplicar, archivar), Secciones, Contenido (publicar material, generar video), Evaluación (configurar quiz, importar GIFT), Alumnos (matrícula, grupos, roles), Gradebook, Comunicación (mensajería, anuncios de foro), Calendario, Badges — **más `ws_raw`, un escape hatch a Web Services crudo** que es la decisión de diseño que conviene portar. v0.5.2 (wrapper) + v0.5.0 (plugin); el README declara **«~80 % operable desde un agente LLM»** y deja salvedades abiertas en subida de archivos y creación de secciones. 59 commits, 1 fork. ⚠️ **Pre-producción declarada por el propio autor.** *Agregado en el pase 27* | Sin región verificada |
| scorm-mcp-server | https://github.com/giacomomaria81/scorm-mcp-server | **MIT** ✅ | 6 | TypeScript | **El puente al LMS que el cliente ya tiene instalado, en el formato que ese LMS ya sabe importar.** Convierte HTML (o *bundles* de diseño) en paquetes **SCORM 2004 4.ª edición y SCORM 1.2**, versión elegible por parámetro. **3 tools:** `scorm_package`, `scorm_validate` (conformidad de un paquete existente), `scorm_selftest`. **Inlinea cada asset —CSS, fuentes, JS, imágenes— como data URI, así que el paquete corre 100 % offline**, e inyecta el *runtime* que reporta *completion*, progreso, tiempo y **resume entre sesiones**. Autohospedable; la demo online es opcional. 0 forks, 11 commits. **Es la pieza de salida que a la capa generativa de esta KB (OpenMAIC, Educhain) le faltaba para aterrizar en un LMS sin integrarse con él.** Ver **P56**. *Agregado en el pase 27* | Sin región verificada |
| oneroster-ts | https://github.com/trilogy-group/oneroster-ts | **0BSD** ✅ | 10 | TypeScript | 🔴 **Refuta el «OneRoster vacío» del pase 26, y es la superficie de tools más grande de esta KB: 🔵 132 tools SERVIDAS, medidas ejecutando `tools/list` en el pase 30** (72 de lectura y 60 de escritura, en 19 grupos). **El «164 métodos» del pase 28 era el conteo del SDK y ya está explicado: son 132 operaciones distintas + 32 alias listados bajo dos grupos a la vez, así que no hay nada oculto —el 100 % de las operaciones se sirve—, al revés de CaSS (6 de 61).** 164 métodos documentados** sobre 21 recursos OneRoster (`academicSessions`, `classes`, `courses`, `enrollments`, `results`/`lineItems`, `orgs`, `schools`, `users`, `demographics`, `scoreScales`…), **expuestos como MCP tools con lectura y escritura** (`createUser`, `updateClass`, `deleteEnrollment`, `postAcademicSession`). OneRoster **v1p2**, paginación por offset y `filter` de 1EdTech. **0BSD es la licencia más permisiva que vio esta KB** — dominio público de hecho, sin obligación de atribución. 🔵 **Y el pase 30 mejora el veredicto legal del pase 29:** `package.json` **omite el campo `license`** (de ahí el `license: None` del registro), **pero el tarball publicado SÍ trae un `LICENSE` completo con el texto 0BSD** (*Copyright (c) 2025 Bjorn Pagen*, que es uno de los *maintainers* de npm, así que la procedencia cierra): **el defecto es de metadatos, no de licencia.** 🔴 **En cambio la antigüedad era peor de lo registrado:** el pase 29 leyó `time.modified` (mutación de metadatos) y escribió «2026-05-04»; la última **versión** publicada es `0.7.0` del **2025-06-27**, o sea **quince meses**, con 9 de las 10 versiones en una ráfaga de tres días. **Fijar un fork sigue siendo el requisito, ahora por abandono y no por licencia.** 🔴 Riesgo nuevo: el README usa como token de ejemplo el IdP Cognito de **un operador concreto** (`alpha-auth-production-idp…`), así que el SDK se generó contra **un despliegue**: hay que sobreescribir `--server-url`/`--token-url`. 🔵 A favor: **cero dependencias de runtime** y un flag **`--tool`** que permite servir un subconjunto de las 132, que es el control de ventana de contexto que hace falta. ⚠️ **No se llama `*-mcp`: es un SDK que expone MCP en una línea del README**, y por eso tres pases no lo encontraron (**gap 49 / gap 50**). 3 forks, 39 commits. *Agregado en el pase 28* | Sin región verificada |
| ed-tech-system-mcp | https://github.com/paulocymbaum/ed-tech-system-mcp — ⚪ **P123 no aplica (pase 54): sistema autónomo con su propia base (`SUPABASE_URL` + `SUPABASE_SERVICE_ROLE_KEY`); la credencial de la propia app no es el control de un tercero** | **MIT** ✅ | 0 | Python | Servidor MCP *domain-driven* para flujos de ed-tech, con **18 tools respaldadas por agentes LangGraph**: `content_generation`, `author_lesson_pipeline`, `validate_lesson`/`validate_quiz`/`validate_project`, `search_graph_nodes` (grafo de currícula), `generate_mock_test_structure`, **`socratic_tutor`**, `collect_project_review_context` + `project_review`, `search_youtube`. Arquitectura limpia + DDD declaradas. ⚠️ **Early-stage declarado por el autor** (backlog «23 done, 6 deferred») y 🔴 **sin integración a ningún LMS**: persiste en backend propio sobre Supabase, así que **no sustituye a un conector de Moodle/Canvas, se compone con uno**. **0 ★ con 132 commits — otro caso puro del gap 49.** *Agregado en el pase 28* | Sin región verificada |
| openedu-mcp | https://github.com/Cicatriiz/openedu-mcp — ⚪ **P123 no aplica (pase 54): no es cliente de LMS/SIS — OpenLibrary, Wikipedia, Dictionary y arXiv, sin credencial institucional** | **MIT** ✅ | 13 | Python | **La capa de descubrimiento de recursos abiertos, que es la que esta KB no tenía en formato de agente.** Servidor MCP sobre **OpenLibrary + Wikipedia + arXiv** con filtrado educativo y adecuación por nivel de grado. **21 nombres de tool leídos del README crudo, de los cuales 20 son de dominio y 1 es transporte** (`handle_stdio_input` no es una herramienta: es el loop de stdio que se filtró a la lista). Los cuatro bloques: libros (`search_educational_books`, `get_book_details_by_isbn`, `search_books_by_subject`, `get_book_recommendations`), artículos (`search_educational_articles`, `get_article_summary`, `get_article_content`, `get_featured_article`, `get_articles_by_subject`), vocabulario (`get_word_definition`, `get_vocabulary_analysis`, `get_word_examples`, `get_pronunciation_guide`, `get_related_vocabulary`) e investigación (`search_academic_papers`, `get_paper_summary`, `get_recent_research`, `get_research_by_level`, `analyze_research_trends`). ⚠️ **No toca ningún LMS ni ningún estándar**: es contenido, no sistema institucional — **no reemplaza un conector**. 21 commits y **10 forks sobre 13 ★**, una relación fork/estrella alta que es señal de uso temprano, no de madurez. Licencia verificada en el archivo `LICENSE` (*MIT, Copyright (c) 2025 OpenEdu MCP Team*), no en el README | Sin determinar — el `owner` no declara ubicación y no se inventa |
| openedx-mcp | https://pypi.org/project/openedx-mcp/ | 🔴 **AGPL-3.0** | — (PyPI, 5 releases) | Python/Django | 🔴 **La puerta oficial de Open edX, y la que cierra el gap 48 que esta KB tenía como su mejor oportunidad.** *«Open edX admin operations exposed as an MCP facade for staff/superusers (Ulmo)»*. **35 endpoints medidos leyendo el sdist 0.1.5: 28 en el LMS + 7 en el CMS (autoría).** Escritura real: `enroll`/`unenroll`/`bulk-enroll`, `users/create`, `roles/set`, `access/instructor`, `students/reset-attempts`, certificados (generar, regenerar, invalidar), reportes asíncronos y **`retirement/request`**; autoría en el CMS con `blocks/create`, 🔵 **`blocks/create-tree`** (árbol entero en una llamada), `update`, `publish`, `delete`. **9 scopes** (`read`, `write:enrollment`, `write:users`, `write:roles`, `grant:admin`, `write:certificates`, `write:reports`, `write:courses`, `destructive`) y **18 tools de escritura con rate limit por tool**. 🔵 **Cuatro rails contra «agente en bucle»: re-chequeo de autoridad vivo, rate limit, confirm token con dry-run atado a huella del payload, y auditoría append-only previa a la escritura.** 🔴 **Corre EN PROCESO como plugin Django dentro del LMS y del CMS, y es AGPL-3.0: no hay escotilla de «proceso separado», así que rompe la tesis de composición del pase 27.** ⚠️ `0.1.5`, apunta a Open edX **Ulmo**; `tools/list` **no observado** (no se levantó instancia). Verificado en **PyPI JSON + código del sdist**; `openedx.org` está bloqueado por el proxy. *Agregado en el pase 30* | Global (proyecto Open edX) |
| tutor-contrib-openedxmcp | https://pypi.org/project/tutor-contrib-openedxmcp/ | 🔴 **AGPL-3.0** | — (PyPI, 7 releases) | Python | **La mitad de despliegue del par anterior:** *«Tutor plugin: MCP server + openedx-mcp Django app for staff/superuser admin (Ulmo)»*. Instala el app Django y **corre el servidor MCP**; soporta **Tutor local y Kubernetes**. `0.1.7`, publicado el **2026-07-25**. **Sin este paquete, `openedx-mcp` es sólo la fachada REST interna: el servidor MCP vive acá.** *Agregado en el pase 30* | Global (proyecto Open edX) |
| asfai-education | https://github.com/redbeard-26/asfai-education — 🟢 **P123 clase (a) (pase 54): app OAuth web registrada (`ASFAI_GOOGLE_CLASSROOM_CLIENT_ID`/`_SECRET`) que el administrador del Workspace puede negar; diseño «accountless», el estado del alumno vive en almacenamiento propio del alumno** | **Apache-2.0** ✅ | 2 | TypeScript | **La primera pieza de esta KB que declara cinco estándares 1EdTech a la vez**, y la única que presenta una arquitectura de evidencia y maestría completa en permisivo: *«Open, standards-based architecture and reference implementation for AI-mediated learning, evidence, and mastery»*. **9 gateways MCP:** `asfai_capability` (descubre capacidades y entrega guía de workflow), `asfai_graph` (grafo de aprendizaje: vecinos, fronteras, caminos), `asfai_run` (trabajo versionado con contratos de revisión), `asfai_session` (diálogo reanudable + quizzes formativos), `asfai_lesson` (autoría→validación→revisión→publicación), `asfai_evidence` (evaluaciones y observaciones justificadas), `asfai_resource`, `asfai_storage`, `asfai_classroom` (conecta proveedores de aula). Estándares nombrados: **QTI** (ítems y resultados portables), **xAPI / IEEE 9274.1.1**, **CASE** (competencias K–12), **LTI + OneRoster** y **CLR + Open Badges**. ⚠️ **2 ★ y 42 commits: es un mapa de capas, no una dependencia** — no va a un entregable de cliente como pieza instalada. ⚠️ **No refuta la ausencia de QTI**: declara QTI como formato, no es un conector MCP de QTI. MCP y licencia verificados en el **README crudo** y el archivo `LICENSE`. *Agregado en el pase 30* | Sin región verificada |
| lineage-skill | https://github.com/JuneYaooo/lineage-skill | **Apache-2.0** ✅ | 448 | Python | 🟢 **El primer alta de agente en ocho pases, y entra por el eslabón que esta KB declaraba vacío: convertir el material de un docente en la metodología ejecutable de un agente.** Destila **videos, PDFs, transcripciones y apuntes** en *Agent Skills* docentes **con trazabilidad a la fuente**: extrae activos de capacidad —diagnósticos, flujos de trabajo, **rúbricas**, plantillas, reglas de transferencia y **modos de falla**—, emite paquetes de conocimiento compatibles con **OKF**, y **fusiona varios cursos preservando campos de habilidad**. Corre sobre Codex, Claude Code, OpenClaw y Hermes. **Por qué importa y no es otra skill de estudio:** las piezas que esta tabla ya tenía o son skills *escritas a mano* (`education-agent-skills`, `human-skill-tree`) o son tutores que consumen material; esta **produce la skill desde el material del docente**, que es el paso que faltaba entre uno y otro. La trazabilidad a la fuente es además la contraparte técnica del hallazgo regional de LATAM (**65 % de los estudiantes teme que la AI vuelva superficial el aprendizaje**): una metodología citable es la respuesta a esa objeción. *Agregado en el pase 32* | Sin región verificada (documentación bilingüe EN/中文) |
| Claw-ED | https://github.com/SirhanMacx/Claw-ED — ⚪ **P121 no aplica (pase 53): OAuth del usuario a su PROPIA cuenta de Google; no hay control institucional de LMS en juego** | **MIT** ✅ | 60 | Python | 🟢 **El agente docente *local-first*, y el eslabón que P8 describía sin tener pieza.** *«Local-first AI teaching assistant for editable lesson drafts, student materials, and slides. Uses your curriculum and chosen model. Teacher-reviewed beta.»* El flujo tiene cuatro pasos y los cuatro importan: **(1)** importa una carpeta de **PDF, DOCX, PPTX, TXT o Markdown** del propio docente, extrae texto, indexa para *retrieval* y **construye un perfil de estilo de enseñanza**; **(2)** recibe una tarea concreta —tema, curso, objetivo de aprendizaje, materiales—; **(3)** emite borradores que el docente **revisa y edita en DOCX y PPTX con sus herramientas de siempre**, con controles de exactitud de fuente, claves de respuesta, ritmo, accesibilidad y maquetado; **(4)** el docente elige qué entregar. **El modelo lo elige el usuario.** 🔵 **Por qué no es otro generador de lecciones:** el artefacto que sale es **editable y revisable**, no un chat — y la revisión docente está en el diseño, no en el descargo de responsabilidad. **778 commits, 13 forks**; PyPI `clawed` con **240 releases** y versión **9.18.2026.1**. ⚠️ **Beta declarada** y **Python 3.11+**. Licencia verificada en el archivo `LICENSE` (*MIT, Copyright (c) 2026 EDUagent Contributors*) y en el clasificador OSI de PyPI. *Agregado en el pase 35* | Sin región verificada |
| canvas-lms-mcp (bruchris) | https://github.com/bruchris/canvas-lms-mcp — 🟢 **P121 clase (a) (pase 53): `CANVAS_API_TOKEN` y además modo `oauth_brokered` con client id/secret que la institución registra y REVOCA — el argumento más fuerte ante seguridad** | **MIT** ✅ 🟢 **texto verificado en el pase 50**: `main:LICENSE` → **200**, *«MIT License / Copyright (c) 2026 Christian Bru»* (la regla del pase 49 exige TEXTO y no sólo campo; esta fila ya la cumple) | ⚠️ 8 — **no re-verificable acá** | TypeScript | 🔵 **El conector permisivo de LMS más grande de esta KB — y tiene 8 estrellas, que es el hallazgo.** *«The TypeScript MCP server for Canvas LMS. Read courses, assignments, submissions, rubrics, quizzes; grade, comment, manage course content, and handle Canvas admin workflows from any AI agent.»* 🟢 **Re-medido en el código en el pase 39, no en el README: 120 `readOnlyHint: true` + 48 `destructiveHint: true`** (el README declara 117 de lectura y 48 de escritura; la diferencia son las condicionales). 🟢 **Y lo que no estaba anotado y es argumento de cumplimiento para North America: tiene MODO FERPA.** `CANVAS_PSEUDONYMIZE_STUDENTS=true` seudonimiza a los alumnos; **la reversión exige una SEGUNDA bandera** (`CANVAS_PSEUDONYMIZE_REVERSE_LOOKUP=true`) y la tool `resolve_pseudonym` **sólo se registra en transporte stdio**, como tool **166**. Es la primera pieza de esta base cuyo diseño encodea **FERPA** (tendencia 136). **165 tools** sobre: *courses, assignments, assignment overrides, submissions, rubrics, quizzes, **New Quizzes (LTI)**, files, **gradebook history**, grade explanations, grading policy, grade projection, grading standards, users, groups, enrollments, discussions, modules, pages, calendar, conversations, peer reviews, accounts, analytics, outcomes, content exports, course setup, link audits, **accessibility audits**, appointment groups, student workflows, student search, dashboard, instructor attention workflows*. **Escribe**: califica, comenta, crea y actualiza *assignments*, publica en foros, administra contenido y flujos de administración. 🔵 **Resuelve la advertencia de cifra del pase 27 en lugar de heredarla:** el **165** coincide entre el campo `description` del paquete y el README sobre **62 versiones** publicadas, así que **es una cifra citable** —a diferencia de la de `vishalsachdev/canvas-mcp`, que varía entre 40+, 80+ y 116 según la versión. Declara **MCP 1.x** (versión de protocolo, no «compatible con MCP»). **317 commits**, 4 forks, última versión npm **2026-09-20**. ⚠️ **`tools/list` no observado**: el 165 es declarado, no servido (misma distinción que el pase 30 estableció con `oneroster-ts`). *Agregado en el pase 35* | Sin región verificada |
| mcp-canvas-lms (DMontgomery40) | https://github.com/DMontgomery40/mcp-canvas-lms — 🟢 **P121 clase (a) (pase 53): `CANVAS_API_TOKEN` + `CANVAS_DOMAIN`, sin cookies ni contraseñas** | 🔴 **SIN TEXTO DE LICENCIA** — `LICENSE` da 404 en `main` y en `master`, y ⚠️ **el repositorio SÍ responde** (`README.md` y `package.json`, **200** en las dos ramas), así que la ausencia está medida y no es del canal. 🔴 **Lo único que afirma una licencia es un *badge* en el README de un TERCERO** (la tabla comparativa de `bruchris/canvas-lms-mcp`) | ⚠️ **no re-verificable acá** | TypeScript | ⚠️ **Tercera alternativa MCP de Canvas, y entra a esta tabla como ADVERTENCIA, no como opción.** **54 tools** según la tabla comparativa de un competidor —**instrumento de tercero, sin fecha ni perfil**. 🔴 **Es el defecto inverso al de `@timadey/proctor`: ahí el manifiesto PROMETÍA un `LICENSE` que no existe; acá es un tercero el que afirma la licencia de un repo ajeno.** Un filtro que lea *badges* la aprueba; el default legal sigue siendo «todos los derechos reservados». **No proponible hasta que el upstream publique el archivo** | North America (D. Montgomery) |
| moodle-cli | https://github.com/bunizao/moodle-cli — 🔴 **P121 clase b2 (pase 53): `MOODLE_TOKEN` NO es un token de web service, es el valor de la cookie `MoodleSession` extraída de DevTools** | **MIT** ✅ | — | TypeScript | **La cuarta puerta de Moodle, y la primera del lado del alumno.** *«Moodle for terminals and AI agents: deadlines, grades, files, feedback and quiz reviews from your browser session»*. 🔵 **El detalle de arquitectura que la vuelve proponible donde las otras tres no entran:** trabaja **desde la sesión del navegador del propio usuario**, así que **no necesita token de administrador ni habilitación de Web Services por parte de la institución** — que es exactamente el bloqueo de *discovery* que frena a `peancor/moodle-mcp-server` y a `MarcosNahuel/moodle-mcp` en un cliente que no quiere tocar su Moodle. **20 versiones** entre 2026-07-09 y **2026-09-27**, con **16 menciones de MCP** en el README. ⚠️ **Lado alumno**: no califica ni devuelve nota, así que **no sustituye** al conector docente, se compone con él. *Agregado en el pase 35* | Sin región verificada |
| jbnu-lms-mcp | https://github.com/moon0825/jbnu-lms-student — ⚠️ **P121 clase b1 (pase 53): monta la sesión del alumno (`MoodleSession`+`sesskey` en DPAPI/Keychain) pero CONSERVA los factores — nunca recibe contraseña ni passkey, y es sólo lectura** | **MIT** ✅ | — | Node.js | 🔵 **Categoría nueva para esta KB: la puerta de agente del LMS de UNA institución, no de un producto.** *«전북대 LMS 학업비서»* — asistente académico del LMS de la **Universidad Nacional de Jeonbuk** (전북대학교, `lms.jbnu.ac.kr`, *JBNU LXP*), **MCP STDIO local** para Claude Desktop o Codex. **25 tools** (**25개 도구**) sobre avisos, vencimientos de trabajos, estado de entrega y material de clase, con una interfaz orientada a *«qué tengo que hacer hoy»* —devuelve **hasta 3 pendientes con su fundamento**— y **devolución con aprobación del usuario**. 🔵 **Dos decisiones de diseño que importan más que el repo:** es **sólo lectura en todas las funciones de LMS** (`조회 전용`), y **el login lo completa la persona en su navegador, con passkey y segundo factor incluidos** — el servidor nunca ve la credencial. **Es la postura exacta que premia el régimen coreano vigente** (*AI Basic Act*, 2026-01-22). ⚠️ **Es una herramienta estudiantil NO oficial por declaración propia** (*«비공식 학생 도구»*): el repo advierte que el nombre y los activos de UI son de la universidad y que hay que revisar su guía oficial antes de distribuir. **No se propone a un cliente como pieza instalada; se propone como arquitectura de referencia.** Windows + macOS, v0.8.0 del **2026-09-08**. 🔵 **Y refuta una ausencia declarada de esta KB:** es **la primera infraestructura agéntica educativa de origen APAC** que entra por el registro de paquetes. *Agregado en el pase 35* | **APAC** (Corea del Sur — 전북대학교 / JBNU) |
| moodle-grading-mcp | https://github.com/toshieji/moodle-grading-mcp — 🟢 **P123 clase (a) (pase 54), control negativo que SÍ se sostiene: `MOODLE_TOKEN` de *Site administration → Server → Web services → Manage tokens*. Y la escritura va DOBLE-cerrada: `MOODLE_ALLOW_WRITE=1` + `MOODLE_WRITE_COURSE_ALLOWLIST`, y la nota queda en borrador sin publicar** | **MIT** ✅ | 0 | Python | 🟢 **La pieza que reemplaza a `peancor` y lo hace mejor, y el alta más importante del pase 38.** **9 tools** de corrección sobre Moodle Web Services: `verify`, `find_courses`, `course_contents`, `list_assignments`, `list_pending`, `get_submission`, `read_submission_file`, `read_submission_images` y **`save_grade_draft`**. 🔵 **La nota la decide el cliente LLM; el servidor sólo la escribe — y la escribe en `workflowstate=readyforreview`, o sea GRADUADA Y NO PUBLICADA.** Nunca publica, **no notifica al alumno**, exige `MOODLE_ALLOW_WRITE=1`, **restringe la escritura a una allowlist de IDs de curso** (lista vacía = no escribe), **loguea cada intento en un audit trail JSONL** y **anexa un pie de declaración de asistencia por AI** salvo override. Requiere 8 funciones de Moodle WS, entre ellas `mod_assign_save_grade`. 🟢 **Su diseño de seguridad es argumento de cumplimiento ante el régimen de alto riesgo del AI Act y las reglas de supervisión humana de Oklahoma y Maryland.** `HEAD` 2026-09-07. *Agregado en el pase 38* | APAC (Web Analytics Consultants Association — WACA, Japón) |
| mcp-moodle-teacher | https://github.com/NiccoloSalvini/mcp-moodle-teacher — 🟢 **P121 clase (a) (pase 53): `MOODLE_TOKEN` del web service móvil, `.env` en modo 600** | **MIT** ✅ | 0 | TypeScript | 🟢 **La mitad docente de Moodle, y la superficie más grande de esta capa: 22 tools** — 15 de lectura (`whoami`, `list_functions`, `my_courses`, `students`, `course_contents`, `assignments`, `submissions`, `submission_status`, `missing`, `gradebook`, `announcements`, `attendance_sessions`, `attendance_report`, `timetable`, **`late_registers`**), **3 de escritura** (`grade_submission` con devolución escrita, `announce`, `mark_attendance`) y 4 de utilidad (`grades_check`, `grades_csv`, `grades_verify`, **`students_at_risk`**). *Read-first* por diseño: **toda tool que modifica Moodle lo declara y pide confirmación**. `late_registers` detecta registros de asistencia no tomados en 24 h — es la única pieza permisiva de esta base que toca asistencia. ⚠️ **En proceso de renombre a `mcp-moodle-staff`**: el commit de cabeza ya lo dice, así que la URL puede moverse. v0.4.0, `HEAD` 2026-09-25. *Agregado en el pase 38* | EMEA (Italia) |
| moodler-mcp | https://github.com/Dymayo/moodler-mcp — 🔴 **P123 clase b4 (pase 54), y es el CONTROL NEGATIVO del pase 53 que FALLÓ: declara una sola variable (`MOODLE_URL`) y ninguna credencial porque `login_to_moodle` abre Chrome, el alumno hace su SSO y la pieza MINTA un token de web service de app móvil y lo guarda en disco. Artefacto (a), emisor (b) — invisible en un audit de configuración. Escrituras tras `MOODLER_ALLOW_STUDENT_WRITES` / `MOODLER_ALLOW_TEACHER_GRADING`** | **MIT** ✅ | — (75 commits, **0 tags**) | 🔴 **Python** (corregido en el pase 39; la fila decía TypeScript) | **Tercera opción permisiva y viva de Moodle MCP** — *«talk to your Moodle in plain English»*. Release **1.1.2** por *conventional commits* con *release-please* (PR #44), `HEAD` 2026-09-19. ⚠️ **Entró a esta tabla por licencia verificada y fecha medida: sus tools NO se enumeraron en el pase 38.** ✅ **Enumeradas en el pase 39: 38 tools = 30 de lectura + 6 de escritura de alumno + 2 de escritura docente**, partidas por rol en `writes_student.py` (`submit_assignment`, `post_forum_reply`, `reply_to_conversation`, `mark_notifications_read`, `mark_activity_complete`, `create_calendar_event`) y `writes_teacher.py` (**`save_assignment_grade`**, `grant_extension`). 🟢 **Triple freno en la escritura:** bandera de entorno **separada por rol** (`MOODLER_ALLOW_TEACHER_GRADING`, `MOODLER_ALLOW_STUDENT_WRITES`), `confirm=true` explícito y **resolución de aprobación del SDK** (`Resolve(approval(...))`), más `ToolAnnotations(read_only_hint=False, destructive_hint=True, idempotent_hint=False)`. 🔴 **Pero el contraste con `moodle-grading-mcp` manda para alto riesgo: `save_assignment_grade` llama a `mod_assign_save_grade` con `workflowstate=""` — PUBLICA la nota**, mientras la pieza de 9 tools la deja en `readyforreview`. ⚠️ **Huella de despliegue, la más grande de las cuatro puertas de Moodle:** depende de `playwright` + `pymupdf` + `python-pptx` + `openpyxl` + `pypandoc-binary`, porque además **baja y parsea material del curso** (`download_resource`, `read_downloaded_file`, `get_module_content`) — es la única de las cuatro que ingiere contenido. Requiere **Python ≥ 3.14** y `mcp>=2.2,<3`. *Agregado en el pase 38* | Sin región declarada (copyright: Ghaith AlHallak, 2026) |
| learnmcp-xapi (fork `ashleycribb`) | https://github.com/ashleycribb/learnmcp-xapi | **MIT** ✅ (heredada: *«(c) 2025 David Romero»*) | 0 | Python | ⚠️ **NO es el sucesor del upstream congelado, y entra a esta tabla justamente para que no se lo cite como tal.** Su `main` está en **2026-09-17**, trece meses más nuevo que `DavidLMS/learnmcp-xapi`, y un buscador lo presenta como *«a more recent fork»*. Medido el grafo: **`merge-base` = tip del upstream**, **2 commits adelante**, **0 atrás**, y los dos commits son `18b2954` *«Add Google Cloud Run deployment configuration and documentation»* y su merge. 🔵 **La lógica xAPI y MCP es la del upstream, sin un cambio.** Valor real: **es una receta de despliegue en GCP Cloud Run** para la puerta xAPI. 0 estrellas, 0 tags. *Agregado en el pase 38* | Sin región declarada |
| mcp-usc | https://github.com/PabloPC05/mcp-usc — ⚠️ **P121 clase (a)+b2 (pase 53): ofrece token institucional `USC_MOODLE_TOKEN` Y sesión por Entra+MFA; entregable configurando SÓLO la primera** | **MIT** ✅ (`LICENSE` textual + `pyproject.toml`) | — (30 commits) | Python | 🟢 **La segunda superficie permisiva más grande de esta KB: 91 tools**, y el diseño de escritura más defendible que vio esta base. *«Servidor MCP local y HTTP-first para el Campus Virtual Moodle y la información académica oficial de la USC»*. Cubre Moodle del lado alumno (entregas, quizzes, foros, mensajería, calendario, badges, grupos, completitud) **y fuentes académicas oficiales** (`list_official_exam_degrees`, `get_my_official_exam_schedule`, `list_usc_degrees`, `locate_usc_subject_codes`). 🟢 **El hallazgo de arquitectura: cada escritura tiene su gemelo `preview_*`** — 22 tools de previsualización (`preview_submit_assignment`, `preview_start_quiz`, `preview_save_quiz_answers`, `preview_remove_submission`…). **Es el único mecanismo de confirmación de esta base que se puede imponer partiendo el conjunto de tools en vez de confiando en el servidor** (tendencia 137, **P82**). 🟢 **Medido en el pase 40 — la fracción portable es del 88 %: 80 de 91 tools son Moodle Web Services genéricas y sólo 11 son de la USC**, y el candado institucional vive en **dos archivos** (`settings.py`, donde el host **ya es `os.getenv`**, y `security.py`, dos `frozenset` de hosts permitidos). 🟢 **Y el activo que no estaba contado: `student_capabilities.py` lleva un catálogo de 306 funciones de Moodle WS** clasificadas por acceso (`read`/`action`), con redacción de secretos y cotas de tamaño de argumento — la pieza más cara de construir en cualquier puerta de Moodle, y es MIT. 🔵 **Reparto exacto de anotaciones, re-medido: 49 `READ_ONLY` + 21 `PREVIEW` + 20 `WRITE` + 1 `STATEFUL_READ`** — el «22 previsualizaciones» del pase 39 eran **21 `PREVIEW` más `inspect_submission_status`**, que está anotada aparte porque **es una lectura que cambia estado**. *Agregado en el pase 39 del 2026-10-02; portabilidad medida en el pase 40* | **EMEA** (España, U. de Santiago de Compostela) |
| DUTIC-mcp | https://github.com/JOSETRA44/DUTIC-mcp — 🔴 **P121 clase b3 (pase 53), la peor de las once: guarda usuario y CONTRASEÑA reutilizables del alumno en `DUTIC_SISACAD_USER`/`DUTIC_SISACAD_PASSWORD`, y un sistema se describe «sin CAPTCHA»** | **MIT** ✅ (`LICENSE` textual + manifiesto) | — (74 commits) | TypeScript | 🟢 **La primera puerta de LMS LATAM con licencia verificada de esta KB.** *«Servidor MCP + CLI para el aula virtual DUTIC (Moodle) de la UNSA»* — Universidad Nacional de San Agustín de Arequipa, Perú. **12 tools**: `dutic_semester_*` (4), `dutic_encuesta_*` (5), `dutic_library_search`, `dutic_library_record`, `dutic_pdf_to_markdown`. 🔵 **Su razón de existir es un defecto real del LMS y vale como caso de venta:** expone las **tareas ocultas que el calendario de Moodle no muestra** (*«24 tareas · 10 SIN ENTREGAR · 18 ocultas»*). Trae además **búsqueda y registro de biblioteca** y conversión de PDF a Markdown. ⚠️ **Antes de proponerla hay que mirar `dutic_encuesta_fill_all` + `dutic_encuesta_submit`:** completa y envía encuestas institucionales en nombre del alumno, que es una escritura que muchas instituciones van a rechazar por integridad, no por seguridad. 🔴 **Medido en el pase 40 y la proporción es la inversa de `mcp-usc`: sólo 1 de 12 tools es portable tal cual** (`dutic_pdf_to_markdown`), **2 más con configuración** (las de biblioteca, que **corren sobre Koha** — primera pieza agéntica sobre Koha de esta KB) y **9 son institucionales**; las 5 de `encuesta` **no son Moodle**, apuntan a la extranet de la UNSA. **El motivo es una línea: `export const HOST = "aulavirtual.unsa.edu.pe"` es constante de compilación** (`src/core/config.ts:11`), no variable de entorno. 🔴 **Y ninguna de las 12 declara `readOnlyHint`**, así que el cliente no puede distinguir lectura de escritura por metadatos: **delante de esta pieza el *gateway* de P85 es obligatorio**. 🔵 **Lo que la compensa, y es el mejor dato de LATAM en varios pases: su telemetría está escrita contra la Ley 29733** — dos niveles de consentimiento, identidad en `unasked` por *default*, honra `DO_NOT_TRACK=1`, estado en chmod 600 y **nunca envía argumentos ni resultados de tools**. ⚠️ Pero la telemetría técnica **viene encendida** y su destino por *default* es un Supabase del autor. `HEAD` 2026-09-24. *Agregado en el pase 39 del 2026-10-02; portabilidad medida en el pase 40* | **LATAM** (Perú, UNSA) |
| mcp-brasil | https://github.com/dasgltd/mcp-brasil | **MIT** ✅ (`LICENSE`, *«(c) 2025-2026 MCP Brasil»*) | — (246 commits, **23 tags**, PyPI 18 releases) | Python ≥3.10 | 🔴 **La alta que corrige una afirmación propia de esta KB: educación NO es el dominio que falta en la capa MCP brasileña.** **2 de sus 15 datasets son del INEP**, con **13 tools de educación** sobre **97** totales: `inep_enem` (`info_enem`, `refrescar_enem`, `valores_distintos_enem`, `media_notas_uf`, `media_notas_por_grupo`, `top_municipios_por_media`) e `inep_censo_escolar` (`info_censo_escolar`, `refrescar_censo_escolar`, `valores_distintos_censo`, `buscar_escolas`, `escola_detalhe`, `resumo_uf`, `top_municipios_por_escolas`). 🟢 **Y confirma la predicción de arquitectura del pase 36 ejecutándola:** no consume API del INEP —no existe—, **descarga los ZIP de microdatos** y sirve agregados. 🟢 **Diseño LGPD medido en el código:** `COLUNAS_DISTINCT_PERMITIDAS` = *frozenset* de 8 columnas, todas categorías agregadas (`SG_UF_PROVA`, `SG_UF_ESC`, `TP_SEXO`, `TP_COR_RACA`, `TP_ESCOLA`, `TP_LINGUA`, `TP_FAIXA_ETARIA`, `TP_ST_CONCLUSAO`); `SOURCES.md` clasifica educación como **RISCO ALTO**, documenta el retiro de microdatos de 2022 por LGPD y la reanudación anonimizada de 2024, y remite a **SEDAP** para microdatos no anonimizados. CI con **canario semanal de salud de fuentes**. ⚠️ Citar `dasgltd`, no `marcellodesales` (**0 adelante, 8 atrás**). *Agregado en el pase 39 del 2026-10-02* | **LATAM** (Brasil) |
| open-badges-mcp (`mcp-ob-ts`) | https://github.com/maxxeddev/open-badges-mcp | **MIT** ✅ (`LICENSE` + manifiesto + README) | — (28 commits, 5 tags) | TypeScript | 🟢 **Cierra la ausencia más vieja de la capa de credenciales: es la primera puerta MCP permisiva de Open Badges 3.0 de esta KB** (el pase 20 había dejado anotado que **Certo no tiene puerta MCP**, reconfirmado dos veces). **16 tools** en tres grupos: **spec** (`search_spec`, `get_section`, `list_sections`, `get_class`, `list_classes`, `get_property`, `list_properties`, `get_context`, `get_examples`, `resolve_term`, `cross_reference`, `find_conformance_requirements`), **emisión** (`generate_credential`, `create_achievement_credential`) y **validación** (`validate_credential`), más `ping`. 🟢 **Y firma de verdad, no sólo serializa:** `src/crypto/data-integrity.ts` con **Ed25519**, `DataIntegrityProof` y `did:key` (`eddsa`), cargando los contextos oficiales de 1EdTech (`purl.imsglobal.org/spec/ob/v3p0/context-3.0.3.json`) y el *schema* `ob_v3p0_achievementcredential`. ⚠️ `HEAD` **2026-06-10** (3,7 meses, franja tibia) y el repo está **adelante del registro**: `package.json` 0.4.0 contra npm 0.3.2. *Agregado en el pase 39 del 2026-10-02* | **APAC** (zona `+10:00`, Australia) |
| sisu-mcp | https://www.npmjs.com/package/@ink-waffle/sisu-mcp | 🔴 **MIT declarada en UNA sola parte del mundo: el campo de npm.** Medido de primera mano en el pase 41: el tarball (**44.781 b, 17 archivos `dist/*.js`, 1 sola versión**) **no trae `LICENSE` y tampoco trae README**, y no declara `repository` ni `homepage` — 🔴 **no hay segunda declaración posible porque no hay dónde buscarla. Es el caso extremo de la clase 81** | — (1 release, 2026-09-17) | JavaScript | 🟢 **La única puerta de SIS de educación superior de esta KB.** *«MCP server for any Sisu (Funidata) student information system: attainments, study rights, enrolments, timetables, plans, and the course catalogue»*. **12 tools**: `sisu_connect`, `sisu_disconnect`, `sisu_status`, `sisu_endpoints`, `sisu_search`, `sisu_call`, `sisu_studies`, `sisu_attainments`, `sisu_enrolments`, `sisu_plan`, `sisu_course`, `sisu_calendar`. 🔵 **Sisu es el SIS de las universidades finlandesas** (Funidata es propiedad de un consorcio universitario), así que la pieza cubre **matrícula, derechos de estudio y expediente** — la capa administrativa que ninguna de las puertas de LMS de esta tabla toca. 🔴 **La reserva es de evidencia, no de función: sin repo no hay auditoría del fuente, ni *issues*, ni vía de PR.** Pedirle el `LICENSE` al autor es una línea de correo y cambia la clase de evidencia. *Agregado en el pase 39 del 2026-10-02* | **EMEA** (Finlandia) |
| armenian-national-library-mcp | https://github.com/suren-kk/armenian-national-library-mcp | **MIT** ✅ (`LICENSE` + manifiesto) | — (37 commits) | TypeScript | 🟢 **La primera pieza agéntica de esta KB sobre DSpace**, que es la plataforma de repositorio que `verticals/solutions.md` lista hace 30 pases sin una sola puerta. *«Independent, unofficial research MCP integration for the National Library of Armenia public DSpace repository»*. **23 tools y las 23 de lectura** —el *helper* `registerEnvelopeTool` fija `annotations: READ_ONLY` para todas—, en cuatro grupos: **descubrimiento** (10: `search_catalog`, `get_search_facets`, `browse_catalog`, `list_communities`, `get_community`, `list_subcommunities`, `list_community_collections`, `list_collections`, `get_collection`, `list_collection_items`), **contenido** (10: `get_item`, `get_item_access_status`, `list_item_files`, `get_item_text`, `get_bitstream`, `get_file_download`, `get_item_relationships`, `get_item_version`, `get_item_identifiers`, `resolve_identifier`), **API cruda** (2: `get_api_capabilities`, `nla_api_get`) y `get_repository_info`. 🔵 **Es una puerta de DSpace de sólo lectura por construcción, no por configuración** — no hay bandera que la vuelva de escritura, lo que la hace la pieza más fácil de aprobar de este pase. ⚠️ **Y una nota de método que este pase se hizo a sí mismo antes de publicar:** la primera medición dio *«8 tools»* con nombres inventados, porque el proyecto **envuelve `server.registerTool` en su propio *helper*** y un `grep` de la llamada del SDK lo subcuenta. El instrumento correcto es buscar **el *helper* del proyecto**, no la API del SDK (tendencia 139). 🔴 **No es un conector genérico de DSpace: está apuntado a UNA instancia.** La ausencia de *«conector MCP de biblioteca reusable»* **sigue abierta**; lo que existe ahora es **una implementación de referencia para generalizar**, que es distinto y es mejor que nada. `HEAD` 2026-08-10. *Agregado en el pase 39 del 2026-10-02* | **EMEA** (Armenia) |
| ed-fi-sdk-mcp | https://www.npmjs.com/package/ed-fi-sdk-mcp | **Apache-2.0** ✅ (`LICENSE` leído **dentro del tarball**) | — (1 release, 2025-10-03) | TypeScript | ⚠️ **La puerta MCP OFICIAL del consorcio Ed-Fi — publicada por la cuenta `edfi` de npm — y hay que leer la columna siguiente antes de celebrarla.** **11 tools y ninguna toca dato de alumno**: `search_endpoints`, `search_schemas`, `get_schema_details`, `get_endpoint_details`, `get_entities_by_domain`, `list_entity_relationships`, `generate_entity_diagram`, `export_diagram_as_text`, `list_available_versions`, `set_data_standard_version`, `set_custom_data_standard_url`. 🔵 **Es un explorador del *Data Standard*, no una puerta al ODS:** sirve para que un agente **escriba la integración**, no para que **consulte los datos de un distrito**. Decir *«Ed-Fi ya tiene MCP»* sin esta distinción es afirmar algo falso en una reunión (tendencia 112). 🔴 **Dos reservas duras: un solo release hace 12 meses** (*span* 0 días) **y el repo declarado no es legible** (`git ls-remote` falla), así que el único canal de auditoría es el tarball. Dependencias: `@modelcontextprotocol/sdk` + `axios`. *Agregado en el pase 39 del 2026-10-02* | **North America** (Ed-Fi Alliance) |
| frappe-mcp-server | https://www.npmjs.com/package/frappe-mcp-server | ⚠️ **ISC** declarada **sólo en el campo de npm** (sin `LICENSE` en el tarball) — **primera pieza ISC de esta KB** | — (32 releases, último 2025-07-30) | TypeScript | ⚠️ **Llega a educación por el framework, no por el dominio:** es una puerta de **DocType de Frappe**, y Frappe es la base de **ERPNext**, **Frappe Education** y **Frappe LMS**, las tres en `verticals/solutions.md`. **21 tools**: `create_document`, `get_document`, `update_document`, `delete_document`, `list_documents`, `get_document_count`, `check_document_exists`, `get_doctype_schema`, `check_doctype_exists`, `find_doctypes`, `get_doctypes_in_module`, `get_module_list`, `get_field_options`, `get_required_fields`, `get_naming_info`, `get_api_instructions`, `get_frappe_usage_info`, `reconcile_bank_transaction_with_vouchers`, `call_method`, `ping`. 🔴 **La advertencia de arquitectura, y es la más fuerte de este pase: `call_method` ejecuta métodos arbitrarios *whitelisted* del servidor y `delete_document` borra.** Sobre un ERP académico eso es superficie de escritura total, sin la partición por rol que tienen las puertas de Moodle de esta tabla. **No proponerlo sin un *gateway* que recorte la lista de tools.** 🔴 **14 meses sin release y repo no legible.** *Agregado en el pase 39 del 2026-10-02* | Sin región determinada |
| mereos | https://github.com/Drone9/mereos | **MIT** ✅ (`LICENSE` en el árbol **y** campo npm, *«Copyright (c) 2024 Drone9»*) | — (19 releases npm) | JavaScript | 🟢 **La pieza de *proctoring* más viva y con licencia más limpia que encontró el barrido del pase 40 — y es la primera de esta capa en toda la KB.** *«This is an ai-empowered proctoring solution for online assessments.»* **Capa de integridad del lado cliente**: detección de presencia por webcam, verificación de pantalla compartida, seguimiento de foco de pestaña y registro de actividad, embebible en la aplicación de evaluación. `HEAD` **2026-08-28**, última versión npm **1.1.9 del 2026-08-28** — la fecha del repo y la del registro **coinciden**, que es lo que las nueve filas de este archivo medidas en el pase 37 casi nunca cumplen. ⚠️ **Y la advertencia es regulatoria, no técnica, y hay que decirla antes de proponerla:** el *proctoring* por webcam es **exactamente el inciso de educación del Anexo III del AI Act** —*«monitoreo durante exámenes»*, punto 3— así que en EMEA esta pieza entra con expediente de alto riesgo y plazo **2027-12-02**, no como un componente más. En North America cae bajo las leyes estatales de privacidad del alumno ya registradas. **Es proponible; no es proponible sin el expediente.** *Agregado en el pase 40 del 2026-10-02* | Sin región determinada (zona `+05:00` del commit — instrumento débil, declarado) |
| @timadey/proctor | https://github.com/Timadey/proctor | ⚠️ **MIT** — 🔴 **no hay `LICENSE` en NINGUNA rama ni en NINGÚN commit de toda la historia** (medido en el pase 41 con `git log --all --name-only`: 0 coincidencias con `licen|copying`), 🟢 **pero el árbol declara MIT TRES veces**: `package.json`, badge *«License: MIT»* del README y la sección *«licensed under the MIT License — see the [LICENSE] file for details»*. 🟢 **El pase 41 le cambia la clase: no es licencia dudosa, es archivo faltante, y el propio árbol apunta al archivo que falta.** Se cierra con un PR de un archivo | — (7 releases npm) | JavaScript | **Segunda pieza de *proctoring* del barrido, y la más específica técnicamente:** *«AI-powered exam proctoring with MediaPipe»*. Declara **detección de rostro y seguimiento de mirada** (`face-detection`, `gaze-tracking`) sobre **MediaPipe** y **WebRTC**, como librería *vanilla-js* sin framework. `HEAD` **2026-08-08**, release **1.2.6 del 2026-08-08** (coinciden). 🔴 **Entra con reserva de evidencia, no de función — es la clase del gap 81:** la licencia vive en el manifiesto del registro y no en el árbol, así que **no hay texto de licencia que mostrarle a legal**. Se cierra con un *issue* o un correo al autor, igual que `@ink-waffle/sisu-mcp`. ⚠️ **Y le aplica la MISMA advertencia de Anexo III que a `mereos`, agravada:** el seguimiento de mirada es inferencia biométrica de comportamiento, que es el extremo caro del expediente. *Agregado en el pase 40 del 2026-10-02* | **EMEA** (zona `+01:00` del commit — instrumento débil, declarado) |
| exam-guard | https://github.com/aswanth9495/exam-guard | ⚠️ **ISC** en el manifiesto npm (**113 de 113 versiones**) **y en el `package.json` del árbol**, contra **Apache-2.0** en el `LICENSE` — 🟢 **gap 83 CERRADO en el pase 41 por la historia del archivo: el `LICENSE` entró en el commit *«Initial commit»* como único archivo (la casilla de GitHub) y nunca se tocó; el `package.json` se editó hasta 2025-10-09 declarando ISC. La intención del autor es ISC.** 🔵 **Y las dos candidatas son permisivas OSI, así que la contradicción NO bloquea el uso: la diferencia es la cláusula de patentes** (Apache-2.0 la concede; ISC no la menciona) | — (**113 releases** npm, última **2026-01-22**) | JavaScript | **Tercera pieza de *proctoring* del lado navegador de esta tabla**, declarada *«AI proctoring tool»*. Del mismo subgrupo que `mereos` y `@timadey/proctor`: **resuelve la detección en el cliente, no la integración con estados de examen** (para eso están `edx-proctoring` y `seb-server`, en `repos/foundations.md`). ⚠️ **Y trae el defecto inverso de la tendencia 147: el registro va DOS *majors* adelante del repo** — árbol en **8.1.0** con `HEAD` del **2025-10-09**, npm en **10.0.4** del **2026-01-22**: **no se puede leer el fuente de lo que el cliente instalaría.** ⚠️ Le aplica la advertencia de Anexo III punto 3 igual que a las otras dos. *Agregado en el pase 41 del 2026-10-02* | **APAC** (India, `+05:30` del commit — instrumento débil, declarado) |
| canvas-student-mcp | https://github.com/xmike04/canvas-student-mcp — 🔴 **P121 clase b2 (pase 53): instruye extraer la cookie `CANVAS_COOKIE` de DevTools; acepta `CANVAS_API_TOKEN` y el token gana si están los dos** | **MIT** ✅ (`main:LICENSE` → *«MIT License»* **y** `package/LICENSE` en el tarball: **dos artefactos independientes**, pase 52) | 2 | TypeScript | **30 tools read-only sobre Canvas LMS**, y la fila entra con una ADVERTENCIA que no es de licencia. 🔴 **Su argumento de venta es eludir un control institucional:** *«works even when your school disables API tokens»*, resuelto pidiéndole al alumno que extraiga la **cookie de sesión** desde las DevTools del navegador. ⚠️ **Muchas universidades deshabilitan la emisión de tokens a propósito; esta pieza trata esa decisión como un obstáculo técnico.** 🔵 **Licencia impecable y NO entregable sin consentimiento de la institución** — ver **P118** | n/d (sin señal de origen) |
| @mtgibbs/canvas-lms-mcp | https://github.com/mtgibbs/canvas-lms-mcp — 🟢 **P123 clase (a) (pase 54): `CANVAS_API_TOKEN` + `CANVAS_BASE_URL`, emitido por la institución vía *Account → Settings → Approved Integrations*; read-only declarado** | **MIT** ✅ (`main:LICENSE` **y** `package/LICENSE`, pase 52) | 0 (1 fork) | TypeScript | **10 tools sobre Canvas, read-only por diseño declarado** (*«only reads data; it cannot modify assignments or grades»*): `get_courses`, `get_missing_assignments`, `get_unsubmitted_past_due`, `get_recent_grades`, `get_due_this_week`, `get_todo` y 4 más, con CLI aparte. 🔵 **Contraste útil con la fila de arriba: misma superficie LMS, misma licencia, y SIN eludir el control de acceso — usa el token que la institución emite.** npm `0.2.18` | n/d (sin señal de origen) |
| @citolab/qti-convert-cli | https://github.com/Citolab/qti-convert | 🔴 **GPL-3.0-only** — ⚠️ **y es la única pieza de esta tabla con la licencia consistente en TRES artefactos**: campo del registro, `main:LICENSE` y `package/LICENSE` del tarball, los tres GPL-3.0 (pase 52) | 6 (1 fork) | JavaScript | Conversión de paquetes **QTI 2.x → QTI 3**, con API de conversión, herramientas de línea de comandos, utilidades de importación en navegador y export a Word y PDF. 🔴 **GPL-3.0 sobre una herramienta de pipeline de evaluación: contamina lo que se enlace, así que entra como paso de build aislado y nunca como librería embebida.** Confirma y extiende el hallazgo del pase 50 sobre `@citolab/qti-convert-local-ai` | n/d (sin señal de origen verificada) |
| @pie-qti/assessment-player | https://github.com/pie-framework/pie-qti | 🔴 **DISCREPA, y el lado equivocado es el REGISTRO** (pase 52): el campo npm de **las dos** piezas dice **`MIT`** y el repositorio dice **`ISC`** en TRES lugares —*sidebar*, `master:LICENSE` (*«ISC License»*) y el pie del README (*«ISC License — see LICENSE»*)—, con **raíz=0** en el tarball. ⚠️ **Las dos son permisivas, así que el riesgo comercial es bajo y el del INVENTARIO no: un filtro que lea el campo archiva la licencia equivocada** | 4 (1 fork) | TypeScript | *Players* **QTI 2.1, 2.2 y 3.0** para renderizar y puntuar evaluación en el navegador, más un marco de transformación bidireccional **QTI XML ↔ PIE JSON**. La familia publica también `@pie-qti/item-player`, `assessment-toolkit`, `qti-common`, `player-elements` y `web-component-loaders`, todas en `0.1.25`. 🔵 **Misma organización que `pie-framework/pie-elements-ng`, que NO tiene licencia: una org con un repo ISC y otro sin nada** | n/d (sin señal de origen) |
| opencode-sit | ⚠️ **no declara repositorio** · npm [`opencode-sit`](https://registry.npmjs.org/opencode-sit/latest) | **MIT** ✅ **medida en el TARBALL** (`package/LICENSE` → *«MIT License»*; el repo no se declara, así que el tarball es el único canal — tendencia 258) | n/d (sin repo público) | TypeScript | **Socratic Intelligent Tutor como *plugin* de OpenCode** `0.1.2`: no es un tutor nuevo, es una **política pedagógica socrática montada sobre un agente de código que ya existe**. 🔵 **La clase que los pases 46–48 aceptan: no enseña *sobre* AI, usa AI para enseñar** — y es el camino más corto de esta KB para convertir un agente de ingeniería en tutor sin construir el agente | n/d (sin señal de origen) |
| aicourse-mcp-server | ⚠️ **no declara repositorio** · npm [`aicourse-mcp-server`](https://registry.npmjs.org/aicourse-mcp-server/latest) | ⚠️ **campo `MIT` en el registro Y en el manifiesto del tarball, y CERO texto de licencia** (`raíz=0 recursivo=0`; sin repo que probar) — 🔴 **el patrón del pase 49, confirmado ahora por los dos únicos canales disponibles** | n/d (sin repo público) | JavaScript | **Servidor MCP que envuelve el agente tutor de conocimiento de curso de Aliyun Bailian** (API de *app completion* de **DashScope**) `0.1.0`. 🟢 **Es CÓDIGO educativo de origen APAC, que es lo que el canal genérico no devolvió en diez pases** — y llega por el `?text=` del registro, no por el buscador web. ⚠️ **Con `MIT` sin texto no entra en una entrega sin gestión** | **APAC** (Alibaba Cloud / Aliyun Bailian, China) |
| AI-Teaching-Agent | https://github.com/littlecookie0722/AI-Teaching-Agent | **MIT** ✅ (texto del `LICENSE` leído de primera mano, *«MIT License / Copyright (c) 2026 littlecookie»*) | **0** | Python (30 commits) | 🟢 **La respuesta ARQUITECTÓNICA al 0 de 8 del pase 57 y al 0 de 6 del pase 58, y la ÚNICA pieza de esta KB que cumple «borrador + liberación humana» de forma INCONDICIONAL — porque no tiene la capacidad de publicar.** Convierte una fuente docente en Markdown en paquetes de laboratorio, examen y los artefactos de corrección, con DSL estructurados, `WAITING_REVIEW` y aprobación/rechazo humano registrado **por página** antes de aprobar el entregable. 🔵 **La cita que decide la celda:** *«The export does not call platform import, grading execution, or publishing paths»* y *«The default Review Center stops at approved local PPTX download and does not offer platform import or publishing»*. ⚠️ **Lo que NO es, y hay que decirlo antes de proponerla: no escribe en el LMS, así que no reemplaza a ninguna de las seis puertas de `mod_assign_save_grade`/`posted_grade` — no hace su trabajo.** Lo que aporta es el patrón de referencia contra el que se las mide (**P144**), y por eso entra en esta tabla y no en `verticals/`. ⚠️ **MCP declarado en la descripción pero CONGELADO en el MVP por el propio proyecto** (*«MCP/Agent expansion … remain frozen»*), así que **no se cotiza como puerta MCP**. ⚠️ **0 ★ y 30 commits: pieza joven, y se declara** — es la misma curva invertida de **P134**/**P138** (la conforme no es la adoptada). *Agregada en el pase 58 del 2026-10-03* | 🔴 **Sin región determinada.** Único indicio: contenido bilingüe inglés/chino en el README — **indicio débil, NO se infiere región** (regla de **P135**, el falso positivo de «Italia» por subcadena) |
| mcp-canvas-server | https://github.com/CharlieCardenasToledo/mcp-canvas-server | **MIT** ✅ (declarada en la página del repo) | **0** | TypeScript | 🟢 **Alta del pase 59, y entra porque AMPLÍA el denominador del eje de publicación sin ser un fork.** Servidor MCP para Canvas LMS, **51 tools para docentes**, con `grade_submission`, `grade_multiple_submissions` y `submit_assignment`. 🔵 **La celda que decide su clase está en el código, no en el README** (regla del pase 58): `src/services/canvas-client.ts:494-507` manda `data = { submission: { posted_grade: grade } }` y **tiene CERO menciones de `post_manually`, `posting_policy` o `postPolicy` en los 60.194 bytes del cliente**, así que **publica por OMISIÓN** y la configuración correcta del *assignment* (`post_manually = true`) la NEUTRALIZA. ⚠️ **No tiene confirmación por llamada ni borrador sobre la nota**, y su propia documentación la describe en modo directo: *«Grade John's submission for 'Essay 1' with a 90 based on the rubric, and add feedback»*. 🔵 **Verificado NO FORK** en la página del repo, que es lo que la distingue de `algorithm0r/canvas-lms-mcp` y `abr-Projects/canvas-mcp` (ver **P146**). ⚠️ **0 ★: pieza joven, y se declara** — curva invertida de **P134**/**P138**. *Agregada en el pase 59 del 2026-10-03* | 🔴 **Sin región determinada.** No declara afiliación ni institución; el nombre del dueño es el único indicio y **NO se infiere región de un antropónimo** (regla de **P135**) |




## ⚖️ Capa de exposición al Artículo 50(2) del AI Act — las 66 filas clasificadas por UNA pregunta (pase 45 del 2026-10-02)

**Ejecuta la acción 3 del pase 44 y cierra el gap 91.** La pregunta es una sola: **¿esta pieza pone contenido sintético
delante de un alumno o de un docente?** Y para las que sí: **¿tiene alguna forma de marcado?**

🔵 **Por qué estaba en la lista de acciones y no en el *backlog*:** es la única de las tres que no es técnica y es la de
más valor comercial, porque **el plazo está dentro del trimestre y esta base no lo tenía clasificado fila por fila.**

### El reparto, que es el dato de encuadre

| Veredicto | Filas | Qué significa |
|---|---|---|
| `gen` | **24** | la pieza **genera** el contenido |
| `gen-ind` | **7** | pedagogía empaquetada (*skill*, esquema, superficie MCP de tutor): genera **a través del agente anfitrión** |
| `gen-cond` | **1** | sólo con un módulo opcional activado (**Project NOMAD**, módulo de AI local) |
| `pack` | **1** | no genera, pero es **donde el contenido generado se vuelve el curso que el alumno abre** (**scorm-mcp-server**) |
| `no` | **33** | mueve, registra, califica, sincroniza matrícula o supervisa exámenes — **no genera** |

🔵 **33 de 66 filas (50 %) ponen contenido sintético delante de una persona. Exactamente la mitad de esta tabla:** el
Artículo 50(2) no es un problema de un rincón de esta KB, **es un problema de la mitad.**

### 🔴 La medición del marcado: 0 de 33, y el método importa

Barrido con `compose/code/aiact-50-2-exposure/scan_marking.sh`, que **no busca en documentación**: clona cada repo
expuesto con `--filter=blob:none` (**ningún blob se descarga**) y busca artefactos en **la lista de archivos**, más
dependencias en **los manifiestos de raíz**.

| Magnitud | Valor |
|---|---|
| Repos barridos (32 expuestos + el empaquetador − 5 entradas de registro sin repo de GitHub) | **33** |
| Archivos listados | **24.202** |
| Artefactos de **marcado** (`c2pa`, `watermark`, `synthid`, `content-credentials`, `invisible-watermark`, `imwatermark`) | 🔴 **0** |
| Manifiestos de raíz leídos | **26** |
| **Dependencias** de marcado en esos manifiestos | 🔴 **0** |
| Repos con **0 de todo** | **28 de 33** |
| Artefactos de **procedencia** | **15, en 5 repos** |

🔴 **Ninguna de las 33 piezas puede marcar su salida como artificialmente generada, y ninguna se eligió por eso.**

### 🟢 Las DOS filas que sobreviven, y son mitades complementarias del mismo componente

**El pase 44 predijo que la respuesta sería «ninguna». Hay una, y hay una segunda que aporta lo que a la primera le
falta.**

| Fila | Licencia | Qué tiene | Qué le falta |
|---|---|---|---|
| 🟢 **`zijinz456/OpenTutor`** | **MIT**, 127 ★ | **La única bandera legible por máquina de toda la tabla.** `services/provenance.py` → `build_provenance(..., generated: bool = True, ...)` emite **`"generated": true`** + `source_labels` con `"generated"`; `turn_pipeline.py:144-173` lo fija en el camino del turno (*«for UI and persistence»*); **`routers/chat.py:214` lo manda al cliente** y `schemas/task.py:59` lo declara en el esquema. **Se persiste y se sirve: no es telemetría interna.** Y el default es `True` — **falla hacia el lado seguro** | 🔴 Es un campo JSON **al lado**, no una marca **dentro**: si el texto se copia o exporta, **la marca no viaja**. Marca **el turno, no el tramo**. **No está firmado**, así que no resiste manipulación — que es a lo que apunta *«effective, interoperable, robust and reliable»* |
| 🟢 **`JuneYaooo/lineage-skill`** | **Apache-2.0**, 448 ★ | `references/provenance-policy.md`: **vocabulario cerrado de 9 valores**, obligatorio *«para toda afirmación consecuente, respuesta de tarea, regla de rúbrica, juicio de feedback y regla de Personal Skill»*. 🔵 **Cuatro de los nueve son literalmente «esto lo produjo el modelo»**: `source_grounded_synthesis`, `cross_source_synthesis`, `mentor_inference`, `external_general_knowledge`. Y ya dice *«High-impact inference needs a visible label and human review when evidence is thin»* | 🔴 **No es legible por máquina:** es **prosa dirigida al modelo**, no un campo emitido junto al artefacto |

🔵 **La lectura que esto habilita, y es la oportunidad:** `OpenTutor` tiene **el campo y el transporte**;
`lineage-skill` tiene **la granularidad correcta** (por afirmación, no por turno). **Ninguna de las dos sabe de la
otra.** Marcar de verdad no es abrir una capa nueva: es **llenar un campo que ya existe, con una etiqueta que ya está
especificada**, y firmarlo con la capa forense que esta KB ya tiene permisiva (`MarkLLM`, SynthID-Text Apache-2.0,
**P33**). Ver **P99**.

### ⚠️ La distinción que hay que hacer en voz alta

Los **15** hits de «procedencia» invitan al error. **13 de los 15** —`DeepTutor` 3, `universal-examprep-skill` 8,
`lumen` 2— son **procedencia de FUENTE**: de qué documento salió una afirmación, o de qué clon salió una fila de base de
datos. **No son procedencia SINTÉTICA.** Saber de dónde viene el material **no dice que el material lo escribió una
máquina**. Son dos problemas y comparten una palabra, y confundirlos sobreestima el cumplimiento de esta tabla por un
factor de 13.

### 🔴 El calendario, con la corrección de encuadre que hay que decir aunque la fecha esté bien

Confirmado en este pase por un **tercer canal independiente**, concordante con lo que esta base ya tenía:

| Obligación | Fecha | Estado al **2026-10-03** (re-verificado en el pase 58) |
|---|---|---|
| Art. 50 transparencia (declarar que se interactúa con AI) | **2026-08-02** | 🔴 **vigente, vencida hace 2 meses** |
| **Art. 50(2) marcado legible por máquina** — sistemas puestos en el mercado **desde** el 2026-08-02 | **2026-08-02** | 🔴 **YA VIGENTE** |
| **Art. 50(2)** — *backstop* para sistemas **ya en el mercado antes** del 2026-08-02 | **2026-12-02** | ⏳ **60 días** |

🟢 **Re-verificación del pase 58 (2026-10-03), por tres canales concordantes:** el *AI Omnibus* corrió el **Anexo III**
*stand-alone* de **2026-08-02 a 2027-12-02** (aprobación final del Consejo **2026-06-29**, **DOUE 2026-07-24**, **en vigor**
**2026-07-27**) y **el Artículo 50 NO fue tocado** — *«Transparency obligations (Article 50) apply from 2 August 2026 and are
not touched by the Omnibus»*. 🔵 **Las tres filas de arriba se sostienen palabra por palabra**, y el motivo declarado del
diferimiento es que no estaban listas las **normas técnicas armonizadas**, no un cambio de criterio sobre el riesgo: ⚠️ **el
expediente de alto riesgo no desapareció, se corrió, y el cliente EMEA lo sigue necesitando para 2027-12-02.**

⚠️ **Y la fila del *backstop* es la razón por la que esta tabla lleva su fecha de lectura EN EL ENCABEZADO: el pase 57 la
publicó como «61 días» y hoy son 60.** 🔵 **Una cuenta regresiva sin su fecha de ancla no se puede re-derivar —es el mismo
defecto que una cifra de aserciones sin su invocación (**P107**)—, y esta tabla ya lo tenía bien resuelto: por eso la
corrección de hoy cuesta una celda y no un pase.**

⚠️ **Lo que NO se pudo hacer de primera mano, y se declara:** `eur-lex.europa.eu` y `artificialintelligenceact.eu` quedaron
**`EGRESS_BLOCKED`** en este pase, así que estas fechas vienen de **canales secundarios concordantes** y no del texto
consolidado (**gap 92**, quinto canal reconfirmado).

🔵 **El 2026-12-02 NO es «cuándo empieza el Artículo 50(2)»: es el plazo de gracia de lo que ya estaba desplegado.**
Para **cualquier sistema nuevo** —que es exactamente lo que es un *engagement* que entrega un tutor construido sobre
estas piezas— **la obligación rige desde el 2026-08-02 y ya está vencida al momento de entregar.** Decir «faltan 61
días» sobre un desarrollo nuevo es **tranquilizar con la fecha equivocada.**

🟢 **Y el dato de responsabilidad que esta KB NO tenía, y decide quién paga:** el deber del Artículo 50(2) recae en el
**proveedor** —quien desarrolla el sistema generativo y lo pone en el mercado, incluidos los proveedores de GPAI— **no
en el *deployer* ni en el usuario final.** Si Globant **construye y entrega**, el deber está del lado del entregable; si
el cliente sólo **despliega** algo de un tercero, está aguas arriba. **Es una pregunta de *discovery*, y hoy no está en
ningún checklist de esta base.**

⚠️ **Límite de fuente, que se repite cada vez que se citen estas fechas:** **gap 92 ampliado a cuatro dominios** —
`eur-lex.europa.eu`, `artificialintelligenceact.eu`, `data.europa.eu` y ahora **`digital-strategy.ec.europa.eu`** (la
página oficial del *Code of Practice on Transparency of AI-generated Content*), probado por **los dos canales**. Las
fechas están confirmadas por **tres canales secundarios independientes**, **no** por texto consolidado.

## 🧭 Capa de vitalidad CORREGIDA — las 61 filas de GitHub re-fechadas por todas sus ramas (pase 42 del 2026-10-02)

**Esta capa REEMPLAZA el instrumento del pase 37 y conserva su tabla abajo como historia.** El pase 41 probó que la rama
por defecto puede ser la rama **muerta** de un proyecto vivo (`seb-server`: 6 meses en `master`, commit de ayer en
`dev-3.0`) y dejó el **gap 89**: *«el número publicado puede estar mal en la dirección peligrosa»*. **Este pase lo midió.**

**Instrumento:** `git ls-remote --heads` sobre las 61 filas de GitHub → **472 ramas** → `git fetch --depth 1` de cada tip
→ **máximo de fecha, y después lectura de autor y mensaje**. Cobertura **61/61, cero `404`**.

### 🔵 La regla que hace funcionar el instrumento, y se encontró rompiéndolo

🔴 **La primera versión aplicaba los filtros a todas las ramas, incluida la de defecto, y el resultado fue silenciosamente
peor que el original:** `jupyterlab/jupyter-ai` perdía 3 meses (el tip de su `main` lo firma un `[bot]`) y
**`zijinz456/OpenTutor` y `microsoft/Shiksha-Copilot` quedaban SIN fecha de vida.**

🟢 **La regla correcta:** **el tip de la rama por defecto cuenta SIEMPRE como vida —es historia mergeada—; los filtros
deciden sólo si una rama NO-defecto agrega vida por encima de ella.**

### 🔴 Las seis clases que NO son vida de proyecto (el pase 41 había nombrado tres)

| Clase | Qué es | Repos / ramas |
|---|---|---|
| 🔴 **`bot-deps`** | rama de `dependabot`/`renovate` con un *bump* de dependencia | **4 / 18** |
| `agent-branch` | rama `claude/`, `codex/`, `triage/` sin mergear | 4 |
| `bot-other` | autor `[bot]` en una rama no-defecto | 2 |
| `sdk-regen` | regeneración automática de SDK | 1 |
| `empty-commit` | *«empty commit to trigger …workflow»* | 1 |
| 🔵 **`auto-content`** | *pipeline* de contenido, no de código | 1 |

🔵 **`bot-deps` es la clase nueva que más cambia cuentas y el pase 41 no la nombró:**
`suren-kk/armenian-national-library-mcp` tiene **10 ramas `dependabot`** y parece 7 semanas más fresco de lo que es.
**25 observaciones de rama retenidas en 7 repos.**

### El reparto corregido, que es el dato de encuadre

| Franja (máximo entre ramas, filtrado) | Filas | % | Pase 37 (rama defecto, 49 filas) |
|---|---|---|---|
| 🟢 Activo — menos de 3 meses | **48** | **78,7 %** | 34 (69,4 %) |
| ⚠️ Tibio — 3 a 6 meses | 3 | 4,9 % | 5 (10,2 %) |
| 🔴 Frío — 6 a 12 meses | 7 | 11,5 % | 7 (14,3 %) |
| 🔴 **Congelado — más de 12 meses** | **3** | 4,9 % | 3 (6,1 %) |

🟢 **La tabla está más viva de lo que esta base venía diciendo**, y eso respalda las propuestas que se apoyan en ella.

### 🔴 Los cuatro veredictos que cambian, y los dos que el filtro SOSTIENE

| Repo | Pase 37 | **Pase 42** | Causa |
|---|---|---|---|
| 🟢 `karanb192/algo-sensei` | 🔴 FRÍO 11,3 m | 🟢 **ACTIVO (hoy)** | **Commiteó hoy en `main`.** 🔵 El pase 37 no se equivocó: **el proyecto revivió después de medirlo.** Sale del conjunto de «no recomendar» |
| 🟢 `Yuanpeng-Li/gradescope-mcp` | ⚠️ tibio | 🟢 **ACTIVO** | `upgrade-mcp-v2`, autor humano |
| 🟢 `LabSirius/TutorIA` | ⚠️ tibio | 🟢 **ACTIVO** | 🔵 `feature/openedx-integration` — repo **LATAM** integrando Open edX |
| 🟢 `maxxeddev/open-badges-mcp` | ⚠️ tibio | 🟢 **ACTIVO** | `chore/release-0.4.0-and-deps` |
| 🔴 `trilogy-group/oneroster-ts` | 🔴 CONGELADO 15,2 m | 🔴 **CONGELADO — SE SOSTIENE** | 🟢 **El filtro se gana el sueldo:** el máximo ingenuo lo promovería a 4,8 m con un **commit vacío de bot** en rama de SDK. Sostiene **P58/P60/P64** y 132 tools |
| 🔴 `satvik314/educhain` | 🔴 FRÍO 10,0 m | 🔴 **FRÍO 8,3 m** | La rama `claude/*` se retiene; una rama humana real (`new-version`, merge del PR #140) sí cuenta. **Número corregido, veredicto intacto** |
| 🔴 `DavidLMS/learnmcp-xapi` | 🔴 CONGELADO 13,1 m | 🔴 **CONGELADO 13,1 m** | **1 sola rama: no hay vida escondida.** Sigue sosteniendo **42 menciones** y el gap 64 |
| ⚠️ `aswanth9495/exam-guard` | *(no estaba en las 49)* | ⚠️ **FRÍO 7,9 m** | `scaler/dcp-revamp`, autor humano. **Entra al conjunto de «no recomendar»** |

**Las 10 filas de ≥ 6 meses siguen siendo 10**, con cambio de composición: **sale `algo-sensei`, entra `exam-guard`**.
**La tabla completa de las 61, fila por fila, está en `repos/trending.md` (pase 42).**

## 📐 Capa de portabilidad medida — qué fracción de las dos puertas institucionales se REUSA y qué fracción se DESARROLLA (pase 40 del 2026-10-02)

El pase 39 admitió `mcp-usc` (91 tools) y `DUTIC-mcp` (12) y dejó escrito que **no sabía la proporción**: las dos
mezclan tools genéricas de Moodle Web Services con tools atadas a una fuente institucional, y de esa fracción depende
si una pieza **se reusa** o **sólo se lee**. Este pase la mide leyendo el árbol, no el README.

🔴 **El resultado es el opuesto en las dos piezas, y por una razón de una línea de código.**

| | `mcp-usc` (USC, España) | `DUTIC-mcp` (UNSA, Perú) |
|---|---|---|
| Tools totales | **91** | **12** |
| **Genéricas (reuso)** | 🟢 **80 de 91 — 88 %** | 🔴 **1 de 12 — 8 %** (+2 con configuración) |
| **Institucionales (desarrollo)** | **11 de 91 — 12 %** | **9 de 12 — 75 %** |
| Host de la institución | 🟢 **variable de entorno**: `os.getenv("USC_MOODLE_URL", "https://cv.usc.es")` | 🔴 **constante de compilación**: `export const HOST = "aulavirtual.unsa.edu.pe"` (`src/core/config.ts:11`) |
| Dónde vive el candado | **2 archivos**: `settings.py` y `security.py` | **repartido por el árbol** |
| Anotaciones de tool | 🟢 **49 `READ_ONLY` + 21 `PREVIEW` + 20 `WRITE` + 1 `STATEFUL_READ`** | 🔴 **ninguna de las 12 declara `readOnlyHint`** |

### 🟢 `mcp-usc`: el candado institucional es configuración, no arquitectura

**El dato que decide la cotización:** los nombres de host de la USC aparecen en **exactamente dos archivos de todo el
árbol**:

- `settings.py` → `moodle_url=os.getenv("USC_MOODLE_URL", "https://cv.usc.es")` — **ya es overridable**, la USC es el
  *default*, no el destino.
- `security.py` → `ALLOWED_PUBLIC_HOSTS = frozenset({"usc.gal", "usc.es"})` y
  `ALLOWED_CAMPUS_HOSTS = frozenset({"cv.usc.es"})`.

**Portar la mitad Moodle es editar dos `frozenset`.** No hay que refactorizar: el proyecto ya separó la política de
destinos del resto del código, en un módulo que además valida `https`, puerto 443, ausencia de credenciales en la URL
y **rechaza la URL si trae `token`, `wstoken`, `sesskey`, `password` o `access_token` en el *query string***.

**Las 11 tools institucionales, nombradas para que nadie las cotice como reuso:** `list_exam_sources`,
`search_exam_dates`, `list_usc_degrees`, `list_degree_timetables`, `get_degree_class_timetable`,
`get_my_class_timetable`, `locate_usc_subject_codes`, `list_official_exam_degrees`, `list_official_exam_subjects`,
`get_official_exam_dates` y `get_my_official_exam_schedule`. **Dos de ellas son híbridas** y conviene saberlo:
`get_my_class_timetable` y `get_my_official_exam_schedule` cruzan **la matrícula leída de Moodle** (genérico) con **el
calendario raspado del sitio de la USC** (institucional). Portadas a otra universidad, la mitad Moodle sirve y la otra
mitad hay que reescribirla contra la fuente local.

### 🟢 El activo reusable que nadie había contado, y es el más caro de construir

**`student_capabilities.py` lleva un catálogo de 306 funciones de Moodle Web Services** clasificadas por categoría y
por tipo de acceso (`read` / `action`), y el árbol completo referencia **327 nombres distintos** de funciones WS. Eso
es **la pieza que más tiempo cuesta en cualquier puerta de Moodle** —saber qué función existe, qué hace y si es
lectura o escritura— y está **MIT**.

🔵 **Y viene con los límites puestos, que es la parte que un *gateway* casero olvida:** `MAX_ARGUMENT_NODES = 1_000`,
`MAX_ARGUMENT_DEPTH = 8`, `MAX_ARGUMENT_STRING = 100_000`, `MAX_ARGUMENT_BYTES = 1_000_000`,
`MAX_RESULT_BYTES = 2_000_000`, más un `frozenset` de claves secretas que se redactan (`moodlesession`, `sesskey`,
`wstoken`, `enrolmentkey`, `guestpassword`, `authorization`, `cookie`…).

**La lectura comercial:** `mcp-usc` no se propone como «la puerta de la USC». Se propone como **la puerta de Moodle con
el catálogo de capacidades y los límites ya escritos**, a la que se le cambia el destino. El 12 % institucional se
descarta o se reescribe contra la fuente del cliente.

### 🔴 `DUTIC-mcp`: la proporción se invierte, y el motivo es `export const HOST`

**`src/core/config.ts:11` declara el host como constante de compilación, no como variable de entorno.** Eso solo ya
mueve la pieza de «configurable» a «fork», y el reparto de las 12 tools lo confirma:

- **`dutic_pdf_to_markdown` (1)** — 🟢 **genérica de verdad**: convierte PDF a Markdown, no sabe de UNSA ni de Moodle.
- **`dutic_library_search` + `dutic_library_record` (2)** — 🟢 **genéricas con configuración, y el hallazgo está acá:
  corren sobre Koha**, que es el ILS open source que `verticals/solutions.md` lista hace pases. El *gateway* vive en
  `src/biblioteca/infrastructure/koha/` y su base es overridable (`DUTIC_LIBRARY_URL`, *default* `KOHA_BASE_URL`).
  **Es la primera pieza agéntica sobre Koha de esta KB** — hermana de lo que el pase 39 encontró para DSpace con la
  biblioteca armenia. ⚠️ **Pero el catálogo se resuelve contra una instancia de Supabase del autor**
  (`SAAS_SUPABASE_URL`, `src/core/saasClient.ts:14`; overridable con `DUTIC_LIBRARY_SUPABASE_URL`).
- **`dutic_semester_*` (4)** — `list`, `current`, `use`, `discover`: codifican **la convención de rutas por período de
  la UNSA** (`/2025B`, `/2026A`, `/2026B`). Es Moodle debajo, pero el patrón de URL es institucional.
- **`dutic_encuesta_*` (5)** — 🔴 **no son Moodle en absoluto**: apuntan a la **extranet** de la UNSA
  (`extranet.unsa.edu.pe/sisacad/...`), y el propio CLI las describe como *«Encuesta de desempeño docente (extranet
  UNSA). Simula por defecto; enviar es irreversible.»* **Sistema distinto, cero reuso.**

🔴 **Y una corrección a la ficha del pase 39: ninguna de las 12 tools declara `readOnlyHint` ni `destructiveHint`.**
La pieza no trae anotaciones, así que **un cliente MCP no puede distinguir lectura de escritura por metadatos** — y
dos de sus tools (`dutic_encuesta_fill_all`, `dutic_encuesta_submit`) envían una encuesta institucional en nombre del
alumno. **Delante de esta pieza el *gateway* de P85 no es recomendable: es obligatorio.**

### 🔵 El hallazgo que invierte la lectura fácil: la telemetría de `DUTIC-mcp` está escrita contra la ley peruana

Un host cableado y un Supabase del autor **parecen** descuido. Leído el módulo de telemetría, no lo es — y es el dato
más vendible que LATAM aportó a esta KB en varios pases. `src/telemetry/consent.ts` documenta **dos niveles de
consentimiento con reglas distintas, citando la Ley 29733** (protección de datos personales del Perú):

| Nivel | Qué manda | Default | Cómo se apaga |
|---|---|---|---|
| **TÉCNICA** | errores, tiempos, versión, SO — **seudónima** | ⚠️ **activa**, con aviso en la primera ejecución | `dutic telemetry off`, `DUTIC_TELEMETRY=0` o **`DO_NOT_TRACK=1`** |
| **IDENTIDAD** | nombre, correo, id de Moodle | 🟢 **`unasked`** — nunca sin un sí explícito | no aplica: no se envía sin consentimiento |

Y `src/telemetry/scrub.ts` declara por escrito la regla que casi nadie implementa: **los argumentos y resultados de
las herramientas NO se envían nunca** (*«NUNCA pasan por aquí argumentos ni resultados de herramientas — esos no se
envían en absoluto»*), con redacción incondicional de secretos (`sesskey`, `MoodleSession`, JWT, credenciales de
instalación, y la ruta del directorio personal porque **en Windows lleva el nombre del usuario**), estado en
`~/.dutic/telemetry.json` con **chmod 600**, y un interruptor maestro `PERSONAL_POLICY_READY` que **no registra ni
envía** mientras la política no esté implementada y probada.

🔵 **Es la cuarta pieza de esta KB cuyo diseño encodea el estatuto de su región** (tendencia 136: FERPA en
`bruchris/canvas-lms-mcp`, LGPD en `dasgltd/mcp-brasil`, el `readyforreview` de `moodle-grading-mcp` contra la
supervisión humana estatal de North America) — **y es la primera que nombra la ley en el comentario del código.**
⚠️ **Lo que sí hay que decirle a una institución antes de desplegarla:** la telemetría técnica **viene encendida** y
su destino por *default* es **infraestructura de un tercero**. Se apaga con una variable de entorno, pero hay que
saberlo, y en una institución pública eso se decide antes de instalar, no después.

## 🔁 Capa de sucesión de las tres piezas congeladas — qué reemplaza a qué (pase 38 del 2026-10-02)

El pase 37 fechó las 49 filas y encontró **tres dependencias load-bearing con la rama principal parada**. Diagnosticar
no es reemplazar: este pase fue a buscar, para cada una, **una pieza del mismo rol, permisiva y viva**, midiendo con
`git ls-remote` + `git fetch --depth 1 <rama>` y leyendo el archivo de licencia por `raw.githubusercontent.com`.
**El resultado es asimétrico y conviene decirlo así en una propuesta, no promediado.**

| Pieza congelada | Rol | Sucesión | Qué usar desde hoy |
|---|---|---|---|
| 🔴 `peancor/moodle-mcp-server` (MIT, 7,3 m) | nota y devolución dentro del LMS — **gap 6**, **P54**, **P55** | 🟢 **CERRADA y sobre-ofertada: tres MIT vivos** | **`toshieji/moodle-grading-mcp`** si lo que importa es corregir con garantías (nota en borrador, allowlist, auditoría). **`NiccoloSalvini/mcp-moodle-teacher`** si hace falta superficie amplia (22 tools, asistencia, alumnos en riesgo). `Dymayo/moodler-mcp` como tercera opción, pendiente de enumerar |
| 🔴 `trilogy-group/oneroster-ts` (0BSD, 15,2 m) | OneRoster, 132 tools — **P58**, **P60**, **P64** | 🟢 **CERRADA del lado servidor y del lado cliente, con un residuo** | **`Ed-Fi-Alliance-OSS/edfi-oneroster`** (Apache-2.0) para **servir** OneRoster 1.2 desde Ed-Fi ODS. **`TCI/OneRoster`** (MIT, Ruby) para **consumir**. 🔴 **No hay cliente OneRoster permisivo y vivo en TypeScript** |
| 🔴 `DavidLMS/learnmcp-xapi` (MIT, 13,1 m) | puerta MCP de xAPI — **P4**, **P15**, **P67**, **P68**, **P69** | 🔴 **ABIERTA en la capa de puerta — pero contenida** | Seguir usándola **a sabiendas**, por **P78**, y apoyarse en que el LRS de abajo está vivo: `yetanalytics/lrsql` (Apache-2.0, `HEAD` **2026-10-01**) u `openfun/ralph` (MIT, **v5.0.1**, `HEAD` 2026-09-07), intercambiables **por configuración** gracias al sistema de plugins de su v2.0.0 |

### 🔵 Por qué la tercera fila no es una emergencia, y cómo se dice

**`learnmcp-xapi` son ~32 commits de adaptador delgado sobre dos LRS que no mantiene nadie de su equipo.** El riesgo
real de una dependencia congelada es que se congele **con el dato adentro**; acá el dato vive en el LRS, y los dos LRS
permisivos de esta base fueron re-fechados hoy con commits de **ayer** (`lrsql`) y de **hace 24 días** (`ralph`), de
organizaciones distintas y en regiones distintas. 🟢 **Eso convierte a `learnmcp-xapi` en el caso medido de `P78`**
—adoptar una dependencia congelada a propósito, con fork mínimo y contrato de mantenimiento— **en vez de un riesgo sin
dimensionar.** Lo que **no** hay que hacer es citar el fork de `ashleycribb` como sucesor: son 2 commits de Cloud Run.

### ⚠️ Las dos piezas de esta capa que NO entran, y por qué

| Repo | `HEAD` | Motivo |
|---|---|---|
| ⛔ `csmediapro/moodle-mcp-server` | **2026-10-01** | **AGPL-3.0** (leído en `main`) y sólo lectura. **Es el más activo de toda la capa**, y por eso el que más tienta: la fecha es excelente y la licencia lo descarta para producto |
| ⛔ `loyaniu/moodle-mcp` | 2026-06-28 | **Sin archivo de licencia**: probados `LICENSE`, `LICENSE.md`, `LICENSE.txt` y `COPYING` en `main` y `master` — **404 en los 8** |

### 🔵 La regla de método que deja este pase, y es hermana de la del pase 37

El pase 37 estableció que **la actividad de bot no es mantenimiento**. Este agrega la variante que casi entró como dato
bueno: **un fork con `main` más nuevo no es un mantenedor.** Hay que contar los commits que agrega y leer qué tocan.
`ashleycribb/learnmcp-xapi` está 13 meses «adelante» en fecha y **2 commits de configuración de despliegue** adelante en
contenido. **Fechar un fork sin diffear su aporte produce exactamente la clase de dato que esta base viene corrigiendo
desde el pase 33** (**gap 78**).


## 🧭 Capa de vitalidad medida — las 49 filas fechadas por su rama principal (pase 37 del 2026-10-02)

**Esta base midió sus filas con estrellas (33 pases), con descargas del registro (pase 35) y con el *span* de releases
(pase 36). Ninguno de los tres puede contestar la única pregunta que decide si una dependencia entra en una propuesta:
¿alguien sigue escribiendo código acá?** Las estrellas miden interés acumulado; las descargas miden base instalada
—`TinCanPHP` tiene 6.178/mes y no publica desde 2022—; y el *span* de releases **no existe para las 17 filas de esta tabla
que tienen cero tags**.

**El instrumento que sí contesta, y es el más barato de los cuatro:**

```
git ls-remote https://github.com/<slug>                 # refs, sin cuota de API
git fetch --depth 1 https://github.com/<slug> <sha-HEAD> # un solo commit
git log -1 --format=%cI FETCH_HEAD                       # fecha ISO del tip
```

**Cobertura: 49 de 49 filas, cero 404.** 🟢 **Es además el primer control de integridad completo de esta tabla: ninguna de
las 49 URLs está muerta.**

### El reparto, que es el dato de encuadre

| Franja (último commit en la rama por defecto) | Filas | % |
|---|---|---|
| 🟢 Activo — menos de 3 meses | **34** | 69,4 % |
| ⚠️ Tibio — 3 a 6 meses | 5 | 10,2 % |
| 🔴 Frío — 6 a 12 meses | 7 | 14,3 % |
| 🔴 **Congelado — más de 12 meses** | **3** | 6,1 % |

🟢 **Lo que hay que leer primero es el 69,4 %: la tabla está mayoritariamente viva**, y eso vale como respaldo de las
propuestas que se apoyan en ella. 🔴 **Lo que hay que corregir es el 20,4 % de ≥ 6 meses**, porque esta KB lo venía citando
sin distinguir.

### 🔴 Las 10 filas de ≥ 6 meses, con lo que cada una sostiene

| Repo | Licencia | `HEAD` | Antigüedad | Qué sostiene en esta KB | Qué hacer |
|---|---|---|---|---|---|
| 🔴 `Cicatriiz/openedu-mcp` | MIT | 2025-06-03 | **16,0 m** | nada en `patterns.md` | **Marcar.** Dato histórico, no dependencia |
| 🔴 `trilogy-group/oneroster-ts` | **0BSD** | 2025-06-27 | **15,2 m** | **P58**, **P60**, **P64** — *«la superficie de tools más grande de toda esta base»* (132 tools) | 🔴 **Cotizar fork o reemplazo.** Las 5 ramas nuevas son de bot, sin mergear |
| 🔴 `DavidLMS/learnmcp-xapi` | **MIT** | 2025-08-29 | **13,1 m** | 🔴 **42 menciones** — puerta xAPI de **P4**, **P15**, **P67**, **P68**, **P69**; el gap 64 la llamó *«la única puerta»* | 🔴 **Asumir mantenimiento en la propuesta.** 1 sola rama: no hay desarrollo escondido |
| 🔴 `karanb192/algo-sensei` | MIT | 2025-10-22 | **11,3 m** | — | Marcar |
| 🔴 `plastic-labs/tutor-gpt` | — | 2025-11-13 | **10,7 m** | — | Marcar |
| 🔴 `pythpythpython/openstax-mcp-server` | MIT | 2025-11-30 | **10,1 m** | 4 menciones en `patterns.md` | Revisar antes de citar |
| 🔴 `satvik314/educhain` | MIT | 2025-12-03 | **10,0 m** | citada como pieza viva **desde el ciclo 2** | 🔴 **Degradar.** Su tip más nuevo es una rama `claude/*` sin mergear |
| 🔴 `HugeCatLab/ChatTutor` | AGPL-3.0 | 2026-01-09 | **8,8 m** | — | Marcar |
| 🔴 `peancor/moodle-mcp-server` | **MIT** | 2026-02-22 | **7,3 m** | **P54**, **P55** — **la única pieza permisiva de esta KB que pone nota y devolución dentro de un LMS** (gap 6) | 🔴 **Revisar con el cliente.** Es el tramo final del gap 6 |
| 🔴 `24kchengYe/human-skill-tree` | — | 2026-03-25 | **6,3 m** | — | Marcar |

**La tabla completa de las 49, fila por fila, está en `repos/trending.md` (pase 37).**

### ✅ Lo que el instrumento cerró y lo que corrigió

- ✅ **Gap 63, mitad *fecha*, CERRADO.** El pase 34 lo declaró incerrable tras *«8 rutas portadoras de versión, las 8 con
  404»*. **Los tags viven en `refs/tags`, no en rutas de archivos:** `learnmcp-xapi` **`v1.0.0` = 2025-05-25**,
  **`v2.0.0` = 2025-06-02**. 🔵 **No era un límite del entorno: era el instrumento equivocado.**
- 🔴 **Corrección al pase 36 — `pykt-team/pykt-toolkit` NO está abandonado.** Los 5 tags llegan hasta `v1.0.0`
  (**2023-02-10**) y PyPI hasta **2022-10-16**, pero `HEAD` es del **2026-09-22** con *feature commits* reales
  (`feat: add cgmkt model`, `Merge pull request #305`). **Vivo en `main`, congelado en el registro** — el patrón «Ralph»
  del pase 33, segunda aparición.
- ⚠️ **Límite declarado: el «último tag» por orden de versión no es confiable.** `jupyter-ai` tiene 279 tags y el «mayor»
  es de 2023 con `HEAD` en 2026-10-01; `LabSirius/TutorIA` tiene un tag **posterior** a su propio `HEAD`. **Las fechas de
  `HEAD` son medidas; las de «último tag» son orientativas y no se citan a un cliente** (**gap 73**).
- 🔴 **`api.github.com` no sirve para esta tabla, y falla de la peor manera.** `/rate_limit` da **200** con
  `limit: 15000`; `/repos/<slug>` da **200 en HTTP** y en el cuerpo *«GitHub access to this repository is not enabled for
  this session»*. **Compuerta de alcance, no bloqueo de red** — y como el error viaja en el cuerpo, **un probe que mire
  sólo el código HTTP escribe campos vacíos creyendo que funcionó** (**gap 74**).


## 📦 Capa de despliegue medida — las 49 filas pasadas por el registro (pase 36 del 2026-10-02)

> **Acción 1 del pase 35, ejecutada sobre la tabla completa en vez de seis piezas.** Para cada repo se leyó el manifiesto
> publicado (`package.json`, `pyproject.toml`, `setup.py`, `composer.json`) desde `raw.githubusercontent.com`, se extrajo
> el **nombre de paquete declarado** y se consultó el registro correspondiente. **Cada coincidencia se verificó contra el
> *backlink* del registro al repo** — la regla anti-colisión de las tendencias 100 y 113 — y **dos de las coincidencias
> resultaron ser colisiones**, abajo.

### 🔴 La corrección de método que hay que leer antes de la tabla: en este entorno «descargas por mes» NO es un instrumento general

**El pase 35 introdujo las descargas del registro como el instrumento que treinta y cuatro pases no usaron. Medido el canal, el instrumento está disponible para UN registro de tres:**

| Canal | Metadato (versión, fecha) | Descargas | Veredicto |
|---|---|---|---|
| **Packagist** (`packagist.org/packages/<v>/<p>.json`) | ✅ 200 | ✅ `downloads.monthly` | **El único con descargas** |
| **npm** (`registry.npmjs.org/<p>`) | ✅ 200 (directo, está en `no_proxy`) | 🔴 `api.npmjs.org` → **403 a CONNECT** | Sólo cadencia |
| **PyPI** (`pypi.org/pypi/<p>/json`) | ✅ 200 (directo, está en `no_proxy`) | 🔴 `pypistats.org` → **403 a CONNECT** | Sólo cadencia |

🔵 **Por eso este pase mide lo que sí se puede medir en los tres canales, y resulta ser mejor instrumento que las descargas para esta tabla: el *span* de releases — primera publicación, última publicación y cuántas hay en el medio.** El *span* separa **mantenimiento sostenido** de **ráfaga de publicación y silencio**, y esa distinción es la que decide si una pieza se puede poner en una propuesta. **Las descargas no la muestran**: un paquete abandonado con base instalada sigue descargándose (ver `rusticisoftware/tincan`, abajo).

### Lo que la medición da vuelta — las dos puntas que el pase 35 pidió buscar

**🟢 Punta 1 — pocas estrellas, tracción real (se suben):**

| Repo | ★ | Paquete | Releases | Primera → última | Lectura |
|---|---|---|---|---|---|
| `SirhanMacx/Claw-ED` | **60** | `clawed` (PyPI) | 🟢 **240** | → **2026-09-19** | 🔴 **240 releases con 60 ★.** *Backlink* verificado (`project_urls` → `/SirhanMacx/Claw-ED/issues`). **La cadencia más alta de toda la tabla, y la fila tenía el conteo de estrellas más bajo de su vecindario.** Es el caso más fuerte del archivo contra medir adopción por estrellas |
| `bruchris/canvas-lms-mcp` | **8** | `canvas-lms-mcp` (npm) | **62** | 2026-04-13 → **2026-09-20** | ✅ **Confirma la promoción del pase 35 por un segundo instrumento:** `v1.30.0`, **MIT leído en el registro** (no en el badge), 62 releases en 5 meses de *span* sostenido |
| `bunizao/moodle-cli` | — | `moodle-cli` (npm) | **20** | 2026-07-09 → **2026-09-27** | `v0.9.6`, MIT en registro, 20 releases en < 3 meses: **vivo** |
| `Miaotofu01/Study-Mate` | 482 | `@yunmiao/studymate` (npm) | 8 | **2026-09-22 → 2026-09-30** | **8 releases en 8 días.** Es nuevo, no maduro: *span* de 8 días no sostiene una propuesta todavía, pero la cadencia es real |

**🔴 Punta 2 — estrellas sin tracción, o tracción que no es lo que parece (se marcan):**

| Repo | ★ | Paquete | Releases | Última | Lectura |
|---|---|---|---|---|---|
| `pykt-team/pykt-toolkit` | **441** | `pykt-toolkit` (PyPI) | 11 | 🔴 **2022-10-16** | **Cuatro años sin publicar.** *Backlink* verificado, así que no es colisión: es abandono. **441 ★ y la fila entra en propuestas de *knowledge tracing* de esta KB** — se marca |
| `satvik314/educhain` | 389 | `educhain` (PyPI) | 35 | ⚠️ **2025-12-03** | **~10 meses sin publicar.** Esta KB viene citando Educhain desde el ciclo 2 (*«v0.4 YouTube→course»*) **como pieza viva**; medido, está parado |
| `MarcosNahuel/moodle-mcp` | 1 | `@nahuelalbornoz/moodle-mcp` | 8 | ⚠️ **2026-04-23** | **8 releases en 4 días (2026-04-19 → 04-23) y nada en 5 meses.** 🔵 **El patrón «ráfaga y silencio» que el *span* delata y las descargas no** |
| `moon0825/jbnu-lms-student` | — | `jbnu-lms-mcp` (npm) | 2 | 2026-09-08 | **2 releases el mismo día**, nada en 24 días. Alta del pase 35: **no maduro** |
| `rusticisoftware/tincan` (TinCanPHP) | 88 | Packagist | 21 | 🔴 **2022-11-02** | **6.178 descargas/mes y el último release hace casi 4 años.** ⚠️ **Y una corrección a la cifra del pase 35**, que escribió *«congelada desde 2019»*: **medido en el tiempo de versión de Packagist es 2022-11-02.** Es el ejemplo que prueba que **las descargas miden base instalada, no vida del proyecto** |
| `learninglocker/learninglocker` | 583 | Packagist | 58 | 🔴 **2017-04-04** | **0 descargas/mes, 2.960 totales, último release 2017.** ✅ Confirma el pase 35 **y lo fecha** |

### 🔴 Las dos colisiones nuevas — y las dos habrían entrado como dato bueno

**La regla anti-colisión de esta KB (tendencias 100 y 113) rechazó dos coincidencias que el nombre declarado en el manifiesto daba por buenas:**

- 🔴 **Colisión 10 — `tero`.** `marcorojasb/tero` declara en su `pyproject.toml` el nombre `tero`, y **`tero` existe en PyPI con 2 releases**. ⚠️ **No es el mismo proyecto: el `tero` de PyPI es *«Configures development machines to cloud resources»*, de `djaodjin/drop`.** Sin el control de *backlink*, esta fila se habría publicado con fecha y conteo de releases **de otro software**.
- 🔴 **Colisión 11 — `mcp-server`.** `paulocymbaum/ed-tech-system-mcp` declara el nombre **`mcp-server`**, que es **genérico y está tomado en PyPI por un tercero** (*«A custom MCP server that provides useful tools and resources for AI as…»*, sin `project_urls`). **Los 5 releases de 2025-04-11 no son de este repo.** 🔵 **La regla que esto agrega a las dos anteriores: un nombre de paquete GENÉRICO en el manifiesto es un predictor de colisión, y hay que tratarlo como sospechoso antes de consultar el registro, no después.**
- ⚠️ **Un caso intermedio, declarado como tal: `avps82/mentar` → `mentar` (PyPI, 1 release, 2026-06-17) NO tiene `project_urls`**, así que no hay *backlink* que verificar; **se acepta por coincidencia de descripción** (*«OSS-first, local-first AI tutor for children»*, que es exactamente el repo) **y queda marcado como confirmación débil**.

### 🔵 Siete filas declaran un paquete que NO está publicado — y es una clase, no un descuido

**Siete repos tienen manifiesto con nombre de paquete y el registro devuelve 404:** `Crosstalk-Solutions/project-nomad` (**38,8 k ★**, declara `project-nomad` en npm), `GarethManning/education-agent-skills` (815 ★), `vasanthsreeram/Alvarmethod`, `Open-TutorAi/open-tutor-ai-CE` (107 ★, declara `open-tutorai`), `Yuanpeng-Li/gradescope-mcp`, `Cicatriiz/openedu-mcp` (declara `openedu-mcp-server`) y `vishalsachdev/canvas-mcp` **en su mitad npm** (`canvas-mcp-code-api` → 404, mientras **su mitad PyPI sí está publicada**, 22 releases, 2026-09-28).

⚠️ **Lo que esto significa para una propuesta, y es operativo: un `package.json` en el repo NO implica que exista un paquete instalable.** Para estas siete, la vía de instalación es **el código fuente** (`git clone`), no el gestor de paquetes — exactamente la causa que el pase 33 midió en `learnmcp-xapi` (tendencia 99), **ahora contada: 7 de 49**.

### Y 22 de 49 filas no tienen manifiesto de paquete — pero eso es coherente, no un defecto

**Veintidós repos no publican ningún manifiesto**, y la mayoría pertenece a **una clase que no se distribuye como paquete: la *skill* de agente** — `24kchengYe/human-skill-tree` (562 ★), `JuneYaooo/lineage-skill` (448 ★), `ZeKaiNie/universal-examprep-skill` (299 ★), `karanb192/algo-sensei` (281 ★), `SenmuuuuW/universal-diagnostic-tutor-skill` (235 ★), `GarethManning/education-agent-skills` (815 ★). 🔵 **La lectura: una *skill* se consume clonando el repo o copiando el directorio, así que medir su adopción por registro es una categoría equivocada** — para esta clase el instrumento sigue siendo las estrellas y los *forks*, y conviene decirlo en vez de dejar la celda vacía. **Las piezas con *backlink* verificado y release reciente son 14 de 49**; **las vivas con cadencia sostenida, 6**.

## Capa de conectores MCP por LMS y por estándar — agregada en el pase 27 del 2026-10-01

**Lo que este pase corrige antes de agregar nada.** El pase 26 cerró afirmando que **Moodle no tenía conector MCP
permisivo** (gap 43) y construyó el patrón **P51** sobre eso. **Es falso**, y lo desmintió una búsqueda. La tabla de
arriba suma las tres piezas nuevas; acá queda el mapa completo, que es lo que se lleva a una conversación con cliente.

### El mapa, por LMS

| LMS | Licencia del LMS | Conector MCP | Licencia | Escribe | Madurez |
|---|---|---|---|---|---|
| 🟢 **Canvas** | AGPL-3.0 | **`bruchris/canvas-lms-mcp`** | **MIT** ✅ | **Sí** — califica, comenta, CRUD de assignments, admin workflows | 🔵 **El más grande y el de cifra citable: 165 tools, 317 commits, 62 versiones, MCP 1.x.** Trae `accessibility audits`. **8 ★** *(pase 35)* |
| **Canvas** | AGPL-3.0 | `vishalsachdev/canvas-mcp` | **MIT** ✅ | Sí | 269 ★ y 815 commits, pero **la cifra de tools es inestable** (40+/80+/116). Ver la advertencia, abajo |
| **Canvas** | AGPL-3.0 | `mtgibbs/canvas-lms-mcp` | **MIT** ✅ | No (consulta) | Notas, entregas y datos académicos. 15 versiones, última 2026-02-13 *(pase 35)* |
| ⚠️ **Canvas** | AGPL-3.0 | `@owen-x-tech/canvas-mcp` | **MIT** (declarada en el paquete) | — | ⚠️ **El paquete existe (2 versiones, 2026-02-23) pero el repo que declara NO resuelve:** `owentaylor/canvas-mcp` da **404 en las doce rutas probadas** (`main`/`master`/`dev` × README/LICENSE/package.json/index.js). **Por la tendencia 94 el 404 del repo no invalida el paquete, pero sin código legible no se propone.** Se registra para no volver a encontrarlo *(pase 35)* |
| **Canvas** | AGPL-3.0 | `@imazhar101/mcp-canvas-server` | 🔴 **ninguna declarada** | — | **Se excluye por licencia ausente**, aunque esté activo (13 versiones, última 2026-10-01) *(pase 35)* |
| **Moodle** | GPL-3.0+ | `peancor/moodle-mcp-server` | **MIT** ✅ | **Sí — nota y devolución** | 43 ★, 13 forks, **10 commits** |
| **Moodle** | GPL-3.0+ | `MarcosNahuel/moodle-mcp` | **MIT** ✅ | Sí, 40 tools | 59 commits, **1 ★**, pre-producción declarada |
| **Moodle** | GPL-3.0+ | `csmediapro/moodle-mcp-server` | ⚠️ **AGPL-3.0** | No (lectura) | Capas útiles = **plugins premium de pago**. ⚠️ **Re-fechado en el pase 35: está vivo** — se distribuye en npm como `moodle-mcp-server-aql`, **8 versiones** entre 2026-08-18 y **2026-10-01** |
| 🟢 **Moodle** | GPL-3.0+ | **`bunizao/moodle-cli`** | **MIT** ✅ | No — **lado alumno** | 🔵 **La única puerta que no pide token de administrador**: trabaja desde la **sesión del navegador del usuario**. Vencimientos, notas, archivos, devoluciones, revisión de quizzes. **20 versiones**, última 2026-09-27 *(pase 35)* |
| ⚪ **Moodle** | GPL-3.0+ | `gafapa/moodle-core-cli` — **sin MCP** | **MIT** ✅ | — (cliente) | **Cliente de *core web services* de Moodle 4.5+, cero menciones de MCP: el candidato más barato a envolver.** 11 versiones, última 2026-09-24 *(pase 35)* |
| 🔵 **LMS institucional** (no producto) | — | **`moon0825/jbnu-lms-student`** | **MIT** ✅ | 🔴 **No — sólo lectura por diseño** | **Categoría nueva.** LMS de la Univ. Nac. de Jeonbuk (Corea), **25 tools**, STDIO local, login por el navegador del usuario con **passkey y 2FA**. **No oficial por declaración propia**: arquitectura de referencia, no pieza instalable *(pase 35)* |
| 🟡 **Open edX** | **AGPL-3.0** | **`openedx-mcp` + `tutor-contrib-openedxmcp`** (oficial del proyecto, PyPI) | ⚠️ **AGPL-3.0** — corre **en proceso** como plugin Django | **Sí — 19 escrituras en 6 scopes** | **La fila cambia de «hueco» a «existe y es copyleft» (pase 30), y el pase 31 la mide desde el wheel publicado:** **35 rutas** (28 LMS + 7 CMS), **19 herramientas de escritura**, **11 con *confirm token* y 8 sin él**. AGPL-3.0 **leída del `LICENSE` del artefacto**, no de la metadata. 🔴 **Ninguna de las 19 crea un curso** — y tampoco lo hace ninguna de las **cinco** versiones REST (`v0`–`v4`): el `v0` de authoring está **deprecado en favor del `v1`** con `DeprecationWarning` en runtime, y el único primitivo de nivel curso es **`course_rerun`** (clona). Ver **gap 50 (cerrado)**, **gap 55 (medido)**, **gap 57** y **P63** | Gap 48 y **gap 50** cerrados · gap 55 medido · **gap 57** · P55 · **P63** |
| **SCORM** (formato) | — | `giacomomaria81/scorm-mcp-server` | **MIT** ✅ | Genera paquetes | 3 tools, offline. **P56** |
| 🟢 **Empaquetado LMS** (SCORM 1.2 + 2004 + cmi5 + LTI 1.3) | — | **`course-code-framework/coursecode`** | **MIT** ✅ | 🟢 **Sí — `coursecode_build` toma `format` como enum `cmi5 \| scorm2004 \| scorm1.2 \| lti`** | **15 tools medidas en el código: 9 de lectura, 6 de escritura, 1 destructiva (`coursecode_reset`).** Superconjunto estricto de `scorm-mcp-server`. ⚠️ El CLI tiene 33 comandos y **la capa de despliegue alojada (login/deploy/promote/CDN) NO está en MCP** *(pase 35, acción 2 del pase 32)* |

⚠️ **Advertencia de cifra sobre `canvas-mcp`, y vale como regla.** La fila de la tabla principal registra **269 ★,
815 commits y «102–103 tools»**, verificado de primera mano en el pase 26. Este pase **no reconfirmó esas cifras** y
encontró que **el conteo de tools varía según la versión** que se consulte: se declaran **40+**, **80+** y **116** en
distintos puntos. 🔴 **El número de tools de este repo no es citable como cifra fija en un entregable** — se cita la
capacidad («más de cuarenta herramientas, lado alumno y lado docente»), no el número.

### El mapa, por estándar educativo — y acá la medición es de primera mano sobre el código

Cruzando `MCP server` con cada estándar que esta KB inventarió. **Lo nuevo de este pase es la columna de la derecha:
qué decidió exponer, y qué decidió ocultar, el proyecto de referencia de cada estándar.**

| Estándar | Conector MCP de terceros | En `cassproject/CASS` (medido por anotación) |
|---|---|---|
| **xAPI** | ✅ `learnmcp-xapi` (desde el pase 6) — 🔴 **y el pase 33 tuvo que reconfirmarlo porque el gap 60 del pase 32 declaró esta celda vacía.** Está acá desde el pase 6 y sigue siendo **MIT, 3 tools (1 escribe, 2 leen)**. **La lección está en la tendencia 101: una ausencia no se declara sin hacer `grep` sobre esta KB** | **1 expuesta** (`record_evidence`) / 4 ocultas — **un statement por llamada** |
| **Competencias / perfil** | — | **1 expuesta** (`get_learner_profile`) / 0 ocultas |
| 🔴 **CASE** | **nada** (y el término está capturado, gap 44). ✅ **Reconfirmado en el pase 34 por un segundo instrumento independiente** (búsqueda abierta) **y por `grep` sobre los ocho archivos de esta KB, sin contradicción**: la ausencia cumple el requisito de la tendencia **101** | **0 expuestas / 13 ocultas** — autoría de marcos **cerrada a MCP** |
| 🔴 **CEASN** | **nada**. ✅ **Reconfirmado en el pase 34 con los dos instrumentos**, y con un dato que vuelve la ausencia **más** robusta en vez de menos: 🔵 **la búsqueda abierta no reconoce la sigla** —la expande como *«Credential Engine Adoption Support Network»*, que **no** es lo que CEASN significa (*Competency and Academic Standards Exchange*)—. **Una ausencia que el instrumento no puede ni nombrar no es un fallo de consulta** | **0 expuestas / 6 ocultas** |
| 🟡 **Open Badges** | **nada del estándar** — lo que aparece es SaaS comercial (`IssueBadge`) y generadores de *badges* de README (**tercera colisión de término**). ⚠️ **El pase 34 auditó esta celda y era MITAD FALSA:** la **puerta MCP** sigue sin existir (confirmado por segundo instrumento), 🟢 **pero la implementación OB 3.0 que esta KB declaraba inexistente existe** — [`Schroedinger-Hat/certo`](https://github.com/schroedinger-hat/certo) (⚠️ **AGPL-3.0**, OB 3.0 + W3C VC + DIDs, emisión masiva por CSV, verificación pública) y el validador oficial [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) (**Apache-2.0** ✅, Open Badges **y** CLR). **La ausencia correcta es «sin puerta de agente», no «sin implementación».** Ver **P72** | **0 expuestas / 5 ocultas**, y **ancladas a `w3id.org/openbadges/v2` → OB 2.0, no 3.0** |
| 🔴 **Caliper** | **nada**, consistente con que dejó de ser open source el **2023-06-17**. **La ausencia está escrita, no inferida** — ✅ **y reconfirmada en el pase 34 con los dos instrumentos** (`grep` sobre los 8 archivos, sin contradicción; búsqueda abierta, sin implementación) | — |
| **xAPI** | ✅ `learnmcp-xapi` (desde el pase 6) — y 🔴 **nada más: medido en el pase 35 sobre los clientes más desplegados.** `RusticiSoftware/TinCanPHP` (**Apache-2.0**, 🔵 **863.777 descargas / 6.178 por mes**, último tag **2019-03-05**), `TinCanPython` (**Apache-2.0**, último release **2020-09-03**) y la familia `php-xapi/*` (**MIT**, último tag 2021-03-24) tienen **cero menciones de MCP**. 🔵 **La buena noticia escondida: del lado CLIENTE la capa xAPI es permisiva** —esta KB la tenía catalogada sólo por sus servidores—, lo que abarata **P15**. 🔴 **La mala: las cuatro piezas están congeladas**, la más fresca hace cinco años → se proponen *forkeables*, no mantenidas | **1 expuesta** (`record_evidence`) / 4 ocultas — **un statement por llamada** |
| **Competencias / perfil** | — · 🔴 **y el pase 35 agrega una frase prohibida: el SDK JavaScript de CaSS NO expone MCP.** `cassproject` 5.0.19 (**Apache-2.0**, npm, **2026-08-12**, activo) tiene **cero menciones de MCP** en su README crudo. *«CaSS tiene puerta MCP»* es cierto del **servidor** (`cassproject/CASS`) y **falso del SDK**: quien integre por npm **no hereda la puerta** | **1 expuesta** (`get_learner_profile`) / 0 ocultas |
| 🔴 **CASE** | **nada** (y el término está capturado, gap 44) | **0 expuestas / 13 ocultas** — autoría de marcos **cerrada a MCP** |
| 🔴 **CEASN** | **nada** | **0 expuestas / 6 ocultas** |
| 🔴 **Open Badges** | **nada del estándar** — lo que aparece es SaaS comercial (`IssueBadge`) y generadores de *badges* de README (**tercera colisión de término**) | **0 expuestas / 5 ocultas**, y **ancladas a `w3id.org/openbadges/v2` → OB 2.0, no 3.0** |
| 🔴 **Caliper** | **nada**, consistente con que dejó de ser open source el **2023-06-17**. **La ausencia está escrita, no inferida** | — |
| ✅ **OneRoster** | 🔴 **La ausencia del pase 26 era falsa.** `trilogy-group/oneroster-ts` (**0BSD**, 10 ★) expone **164 métodos como MCP tools, con escritura**, sobre OneRoster **v1p2**. **No está en ningún directorio de MCP y no se llama `*-mcp`** | — |
| 🔴 **QTI** | **La ausencia pasa a estar medida por CUATRO métodos, y el cuarto es el registro por nombre de implementador (pase 33).** Antes: directorio, patrón de nombre y apertura del SDK permisivo (`examplary/qti`). Ahora además: **los doce paquetes `@longsightgroup/qti3-*` (MIT, 0.13.1 del 2026-10-01) tienen cero menciones de MCP**, y **`oat-sa/qti-sdk` tampoco** (README crudo, 0 de 10.497 caracteres). 🔴 **Y el dato que cambia la cotización: el QTI que el mundo despliega es copyleft** — `qtism/qtism` es **GPL-2.0-only con 218.212 descargas, 293 versiones y release del 2026-07-09**, y `oat-sa/extension-tao-testqti` es **GPL-2.0-only con 117.544 descargas y 844 versiones**. Lo permisivo (`qti3-*`, `instructure/qti`) es **lo único permisivo y lo más nuevo**. 🔵 **La oportunidad quedó medida en vez de afirmada: `@longsightgroup/qti3-cli` (MIT) tiene 14 comandos, CERO dependencias de terceros y TODOS emiten JSON** — el mapeo comando→tool es 1:1 y doce de los catorce son de lectura. Ver **gap 64**, **P59** y **P67** | — |
| ✅⁄🔴 **CASE** (medido en el pase 29) | ✅ **La plataforma existe y es permisiva; el conector sigue sin existir — y ahora las dos mitades están medidas.** [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) (**Apache-2.0**, 9 ★, 3 forks, 180 commits) implementa **CASE 1.0 y 1.1** con la **CASE Provider API oficial**, CRUD de escritura sobre `CFDocuments`/`CFItems`/`CFAssociations`/`CFPackages` en **v1p0 y v1p1**, Keycloak (OIDC) **más API keys**, RBAC de cuatro niveles y multi-tenencia. 🔴 **MCP: cero menciones en el README crudo** — la ausencia pasa de *«sin medir por colisión»* (gap 51) a **medida**. 🔵 **Y es la ausencia más barata de cerrar de esta KB, porque el servidor publica su propio OpenAPI 3** (`GET /ims/case/v1p1/discovery/imscasev1p1_openapi3_v1p0.json`): **el conector se genera, no se escribe** — el mismo camino por el que `oneroster-ts` llegó a 164 métodos. Ver **P60** | **0 expuestas / 13 ocultas** en `cassproject/CASS` — la autoría de marcos sigue **cerrada a MCP** del lado de CaSS, que es justo lo que OpenCASE abre por REST |

**Las dos frases que esto habilita, y las dos que prohíbe.** Habilita: *«la evidencia de aprendizaje entra por MCP, de
a un statement»* y *«el perfil de competencia se lee por MCP»*. 🔴 Prohíbe: *«emitimos insignias por MCP»* y
*«autoramos el marco de competencias por MCP»* — **las dos están excluidas a propósito** por el proyecto de
referencia, y van por REST **fuera** de la superficie de agente. Y si el cliente pide credenciales **OB 3.0 / W3C VC**,
**CaSS no es la pieza que las emite**.

### 🔴 El candidato que NO entra a esta tabla, y por qué queda escrito acá — pase 34 del 2026-10-02

**La tabla se queda en 48 filas y la fila 49 es el hallazgo del pase, por lo que no es.** `quizlar/mcp-server` pasa
**todos** los filtros que este barrido aplica: es **MCP**, es **del dominio educativo** (*«voice-led, FSRS-scheduled
flashcards from YouTube, PDFs, web, or text»* — y **FSRS** es el mismo planificador que usa `OpenTutor`, fila de esta
tabla), está **activo**, y su `LICENSE` dice textualmente *«MIT License — Copyright (c) 2026 Quizlar»*. **Verificado de
primera mano, el repo no tiene código:**

| Archivo | Código HTTP | Qué es |
|---|---|---|
| `LICENSE` | **200** | MIT ✅ — **la licencia es real** |
| `server.json` | **200** | 🔴 **un manifiesto de registro MCP, y nada más** |
| `README.md` | **200** | superficie de descubrimiento |
| *fuente* | — | 🔴 **no existe** |

**El campo que lo delata** es `remotes`: `{"type": "streamable-http", "url": "https://mcp.quizlar.app/mcp/"}`, con
`Authorization` declarado `isRequired` e `isSecret` y una clave `sk-qz-<32 chars>` que se emite en
`quizlar.app/settings/api-keys`. El `$schema` es el de registro MCP del **2025-12-11**.

🔵 **La regla que esto deja, y es de un campo:** **si `server.json` declara `remotes` y no declara paquete ni fuente, la
licencia del repositorio cubre metadatos, no implementación.** Para una propuesta eso significa **cero código
reutilizable, dependencia de proveedor, y datos de aprendizaje del alumno saliendo a un tercero bajo API key** — lo
contrario exacto del argumento de privacidad por diseño que esta base construyó sobre el `ACTOR_UUID` de
`learnmcp-xapi`. **Como producto es legítimo; como pieza componible no existe.** Ver tendencias **103** y **104**.

### La trampa de despliegue que decide si hay superficie MCP o no

Leído de primera mano en `src/main/server/cartridge/adapter/mcp.js`: el adaptador **no lee el spec del disco**, lo pide
**por loopback** — `fetch(CASS_LOOPBACK + '/swagger.json')`, default **`http://localhost/api/`**, puerto **80**. Si ese
`fetch` falla o no devuelve `ok`, el adaptador **loguea y hace `return`**: 🔴 **la ruta `/api/mcp` no se monta, y el
servidor arranca normalmente.** Con proxy, puerto no estándar o HTTPS mal resuelto, **la superficie de agente
desaparece en silencio**. Se apaga además con `DISABLED_ADAPTERS=mcp`. **Es lo primero que hay que mirar si un cliente
reporta que no ve herramientas.**
## ⚠️ Colisión de nombres: hay dos "Bloom" y son proyectos distintos (pase 7)

| Cuál | Repo / marca | Licencia | Stars | Qué es |
|---|---|---|---|---|
| **El `Bloom` de esta tabla** | https://github.com/Li-Evan/Bloom | **MIT** ✅ | 278 | Tutor que genera un syllabus y entrega una lección por vez, ajustando al nivel real de comprensión |
| **El otro "Bloom"** | marca de la versión hospedada de **`tutor-gpt`** (Plastic Labs) | **GPL-3.0** ⚠️ | 931 | Compañero de aprendizaje con razonamiento de teoría de la mente |

Las dos aluden a Benjamin Bloom, así que la colisión va a seguir apareciendo en búsquedas y en prensa.

**La trampa concreta:** buscar "Bloom AI tutor" devuelve material de los dos indistintamente, y es fácil citar **la arquitectura de uno con la licencia del otro** — y las licencias son MIT y GPL-3.0, que es la diferencia entre empaquetable y no empaquetable.

**Convención de esta KB:** `Bloom` sin más es siempre **`Li-Evan/Bloom` (MIT, 278 ★)**. Al otro se lo nombra **`tutor-gpt`**, nunca por su marca.

## Investigación / evaluación

**Reescrita en el pase 4 del 2026-09-30.** Las tres pasadas anteriores registraron un solo evaluador pedagógico (`AITutor-EvalKit`, 3 ★) y concluyeron que "no existe el LegalBench de educación". Buscando por *benchmark* en vez de por *repo de agente* aparecen tres artefactos más, y uno de ellos es diez veces más grande que el que la KB tenía anotado.

| Nombre | Repo | Licencia | Stars | Qué evalúa |
|--------|------|----------|-------|-----------|
| **pyKT** | https://github.com/pykt-team/pykt-toolkit | MIT ✅ | 441 | *(también en la tabla principal)* Benchmark de **knowledge tracing**, no de calidad conversacional: 10+ modelos DLKT sobre 7+ datasets con preprocesamiento estandarizado. Es el más maduro de esta capa por un orden de magnitud |
| **pedagogy-benchmark** | https://github.com/AI-for-Education/pedagogy-benchmark | **MIT** ✅ | 12 | **Conocimiento pedagógico del modelo, medido con exámenes reales de habilitación docente — y los exámenes son chilenos.** 1.143 preguntas en dos componentes: **CDPK** (920, conocimiento pedagógico general transversal a materias, grupos de edad y subdominios pedagógicos) y **SEND** (223, *Special Educational Needs and Disabilities*). El repo acredita las preguntas a la **Agencia de la Calidad de la Educación** y al **CPEIP del Ministerio de Educación de Chile**. Paper: arXiv 2506.18710. De la organización **AI-for-Education** («Empowering Education in LMICs with AI»). Python, 5 commits. **Es la primera pieza de la capa de evaluación de esta KB construida sobre un instrumento estatal latinoamericano, y la primera con componente de educación especial con licencia permisiva.** *Agregado en el pase 13* |
| **MathTutorBench** | https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | 42 | Capacidades pedagógicas *abiertas* de un tutor LLM en matemática: 3 habilidades docentes de alto nivel y 7 tareas concretas, con reward models entrenados para medir calidad de enseñanza y leaderboard publicado. **EMNLP 2025 (Oral)** |
| **ArguLens** | https://github.com/wwrwbs/AI_AWE | Apache-2.0 ✅ | 2 | **Scoring automático de ensayo argumentativo + feedback *label-aware***, descompuesto en tres piezas auditables: clasificador de *discourse moves* (Qwen2.5-7B con LoRA), scorer LightGBM sobre 31 features lingüísticas y generador de feedback (Qwen2.5-14B). UI Gradio con scoring por lote y desglose descargable. Respaldo: arXiv 2608.17356. ⚠️ **2 ★ y 2 commits — grado investigación, no producción**; su valor es la arquitectura separada scorer/feedback, no el repo |
| **UnifyingAITutorEvaluation** | https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | 32 | Taxonomía de 8 dimensiones pedagógicas para respuestas de tutor ante el error de un alumno. Publica **MRBench** en tres versiones: V1 (192 diálogos × 8 dim.), V2 (200 × 8), V3 (300 × 4). **NAACL 2025, Senior Area Chair Award** |
| **EduBench** | https://github.com/ybai-nlp/EduBench | MIT ✅ | 29 | **El primer benchmark pedagógico de esta KB que no es de matemática y no tiene fricción de licencia.** 9 contextos educativos y 4.000+ situaciones, evaluadas en 12 dimensiones agrupadas en adaptabilidad al escenario, exactitud factual/razonamiento y aplicación pedagógica. Cinco escenarios de alumno (QA, corrección de error, provisión de ideas, apoyo personalizado, apoyo emocional) y **cuatro de docente**, entre ellos generación de preguntas y **Automatic Grading**. Publica modelo (`DirectionAI/EDU-Qwen2.5-7B`) y dataset. **ACL 2026**. *Agregado en el pase 5* |
| **SafeTutors** | https://github.com/RadiantCrystal/SafeTutors | 🚫 **sin licencia (ausencia MEDIDA, pase 51)** — 🔴 **esta fila decía «MIT ✅» y no hay UNA línea de texto de licencia:** 20 nombres de archivo × `main` y `master` dan **404** con `README.md` en **200**. La afirmación salía de un *badge* de shields.io más la prosa *«licensed under the MIT License — see the LICENSE file»*, 🔴 **y el enlace del badge sigue apuntando a `github.com/your-username/SafeTutors/blob/main/LICENSE`: es un marcador de PLANTILLA sin editar, prueba de que la sección nunca se llenó** | 0 | **Seguridad pedagógica**, categoría nueva: no mide si el tutor acierta, mide si enseña mal siendo amable. Taxonomía de **11 dimensiones de daño y 48 sub-riesgos** derivada de ciencias del aprendizaje, sobre **5.955 instancias** (3.135 single-turn + 2.820 diálogos multi-turn) en matemática, física y química. 11 modelos evaluados (10 open-weight, 1 cerrado), de 3.8B a 72B. **EMNLP 2026**. *Agregado en el pase 5* |
| **EduGuardBench** | https://github.com/YL1N/EduGuardBench | ⚠️ **sin licencia declarada** | 4 | Daño docente y seguridad adversaria del LLM *como docente simulado* — transversal a materia. Dos datasets: preguntas *Select All That Apply* para diagnosticar déficits de enseñanza, y prompts adversarios con jailbreak basado en personas centrados en **mala conducta académica**. 14 modelos. Reporta un *Educational Transformation Effect* (los modelos más seguros convierten el pedido dañino en momento de enseñanza) y que el modo de falla dominante es la **incompetencia**, no la toxicidad. ⚠️ Sin LICENSE no es reutilizable. *Agregado en el pase 5* |
| **L2-Bench** 🔴 | arXiv 2607.08842 · dataset en HuggingFace bajo `OUP/` · sitio `benchmarks.elt.edu.oup.com` | **código MIT ✅ / dataset y rúbricas CC BY-SA 4.0** ⚠️ | n/d | **Cierra el sub-gap de *lengua*: es el primer benchmark pedagógico de esta KB para enseñanza de segunda lengua.** De **Oxford University Press** con la Universidad de Oxford. Según las fuentes: **1.000+ tareas docentes auténticas**, marco de **12 competencias con 31 sub-habilidades**, rúbricas con descriptores expertos y validación de **200+ educadores de 45+ países**. Paper metodológico compañero: arXiv 2603.20088. 🔴 **NO VERIFICADO DE PRIMERA MANO** — el proxy de egreso de la sesión bloquea `arxiv.org`, `huggingface.co` y `oup.com`, que son los tres lugares donde vive. Licencia y contenido vienen de resultados de búsqueda. **Abrirlo y confirmar antes de cualquier entregable.** *Agregado en el pase 6* |
| **ProHist-Bench** (en `ABench`) | https://github.com/inclusionAI/ABench | **Apache-2.0** ✅ | 30 *(de ABench)* | **Investigación histórica, NO enseñanza de la historia** — y la distinción es el punto. **400 preguntas** núcleo en 4 tipos de tarea con **10.891 rúbricas redactadas por historiadores** sobre **9 dimensiones de capacidad** (versión extendida: 504 preguntas), sobre materiales del **examen imperial chino**. Vive dentro de `ABench`, suite multi-dominio con seis datasets (Física 500 problemas, Actuaría, Lógica, Psicología, Derecho y éste). Paper: arXiv 2604.24690. **No cierra el sub-gap de ciencias sociales**, que es pedagógico: esto mide si el modelo *sabe hacer* historia, no si *sabe enseñarla*. Sí aporta la pieza más cara de construir —10.891 rúbricas de expertos, Apache-2.0— como **capa de exactitud factual** debajo de una capa pedagógica que hay que traer aparte. ⚠️ Procedencia: `inclusionAI` es la organización open source de **Ant Group** (verificado en el perfil: `inclusion-ai.org`, 68 repos) → **APAC/China**, lo que extiende el gap 4. *Agregado en el pase 7* |
| AITutor-EvalKit | https://github.com/kaushal0494/AITutor-EvalKit | 🚫 **sin licencia (ausencia MEDIDA, pase 51)** — 🔴 **esta fila decía «MIT ✅»:** 20 nombres × 2 ramas en **404**, `README.md` en **200**. La afirmación salía de un *badge* `license-MIT` y de una sección *«## License / This project is licensed under the MIT License.»* **que enlaza un `LICENSE` inexistente** | 3 | Implementación LoMTL (LoRA multi-task) sobre las 4 dimensiones del subconjunto MRBench. Demo en EACL 2026 (Rabat). Origen: MBZUAI, Abu Dhabi → EMEA |
| AI-Teaching-Agent | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT ✅ | 0 | Convierte fuentes en Markdown en artefactos **Lab, Exam y Grading** como DSL validado, más slides opcionales. Human review obligatorio, evaluación sandboxeada, servidor **MCP stdio**, y previews de examen "candidate-safe" que excluyen respuestas y referencias internas de corrección. *Agregado en la tercera pasada* |

### Seguridad pedagógica — la categoría que el pase 5 agregó

El pase 4 dejó escrito que el sub-gap pendiente era **"un benchmark pedagógico fuera de matemática"**. Se cae: `EduBench` es transversal a materia por diseño (organiza por *escenario educativo*, no por dominio) y `EduGuardBench` evalúa al modelo como docente simulado, lo que es independiente de la materia. Hay además dos benchmarks descritos en papers sin repo localizable — **EduFrameTrap** (arXiv 2605.14604, TUM/MCML, seis materias incluyendo economía y biología, con los subtipos de sycophancy CS-SYC / AUTH-SYC / FACE-SYC / DIR-SYC) y **ELBench** (arXiv 2608.09548, cuatro módulos bajo protocolo común).

**Lo que hace vendible a esta categoría** es que nombra un riesgo que el cliente reconoce y que los benchmarks de exactitud no capturan: el tutor que revela la respuesta antes de tiempo, que le da la razón al alumno porque el alumno insistió, o que abandona el andamiaje. En un cliente regulado eso no es una métrica de calidad, es el expediente de conformidad.

**El dato de arquitectura, de ELBench:** entre los modelos evaluados, el módulo de *safety* aparece **anti-correlacionado con el de enseñanza práctica** — los más seguros enseñan peor. Si se sostiene, no hay un modelo que resuelva las dos cosas y hay que componer: modelo docente + gate de seguridad medido aparte. Ver el patrón **P11**.

⚠️ **Lo que sigue faltando:** benchmark pedagógico de **lengua, ciencias sociales o formación profesional**. Ninguno de los cinco los cubre.

### Corrección: el repo canónico de MRBench no es el que la KB tenía

`AITutor-EvalKit` (3 ★) y `UnifyingAITutorEvaluation` (32 ★) son **del mismo autor** (Kaushal Kumar Maurya). El pase 1 registró el chico y no el grande. El grande es el que publica la taxonomía completa de 8 dimensiones y las tres versiones de MRBench; el chico es la implementación LoMTL sobre un subconjunto de 4 dimensiones. **Para evaluar un tutor, el punto de partida es `UnifyingAITutorEvaluation`.**

### Leer la licencia antes de usar estos benchmarks en un entregable

Tres de los cinco **no son licencias de código**:

- **MathTutorBench es CC BY 4.0** — atribución, sin share-alike. El más limpio de los tres no-código: se puede usar en un entregable cerrado citando la fuente.
- **UnifyingAITutorEvaluation es CC BY-SA 4.0** — *share-alike*. Un dataset derivado hereda la obligación. Usable para medir internamente; **revisar con legal antes de redistribuir un derivado**.
- ⚠️ **pyKT es MIT con texto verificado; `AITutor-EvalKit` NO** — el pase 51 midió la ausencia (20 nombres × 2 ramas en 404, repo respondiendo): su «MIT» era *badge* y prosa. **La frase original de este bloque decía «los dos son MIT, sin fricción» y era falsa para el segundo.**

La distinción importa porque el uso típico de un benchmark en un engagement es *derivar* uno propio con los datos del cliente, y ahí es exactamente donde muerde el share-alike.

### Por qué `AI-Teaching-Agent` vale seguirlo con 0 estrellas

El gap 6 de esta KB dice que no existe grading open source y que el camino realista es orquestar al incumbente propietario (`gradescope-mcp` sobre Gradescope). Este repo es el primer intento que vemos de la otra estrategia: **generar el artefacto de corrección como DSL auditable** en vez de llamar a un grader externo. El diseño es el correcto para EU AI Act y para los estatutos de EE. UU. que prohíben grading automático — DSL validado, revisión humana en el medio, preview sin respuestas. **No usarlo todavía:** 0 estrellas y 30 commits es un proyecto de una persona sin garantía de continuidad. Registrarlo como la señal de que la categoría empezó a moverse, y re-verificarlo el próximo ciclo.

⚠️ **Varios de esta sección son pre-tracción** (3, 0 y 0 stars). Se incluyen porque son los únicos artefactos open source que encontramos para evaluación pedagógica y grading estructurado, no porque tengan adopción. Ver los gaps 1, 6 y 9 en `intel/trends.md`.

### El hallazgo de encuadre del pase 13: el aporte de LATAM a esta capa no es el repo, es el instrumento de medición

`pedagogy-benchmark` (**MIT**, 12 ★) obliga a releer dos gaps de esta KB a la vez.

**Contra el gap 4.** Desde el pase 7 esta KB viene anotando que **las piezas de evaluación con licencia limpia son todas
chinas**: `XES3G5M` (MIT, el único dataset de knowledge tracing permisivo), `ProHist-Bench` dentro de `ABench`
(Apache-2.0, de `inclusionAI` = Ant Group), `EduBench` (MIT). El pase 12 cerró con la concentración APAC «sin moverse».
**Se mueve acá, y no por donde se la buscaba.** El benchmark es de una organización enfocada en **LMICs**, su código es
MIT, y **sus 1.143 preguntas salen de los exámenes de habilitación docente del Estado chileno** — el repo acredita
explícitamente a la **Agencia de la Calidad de la Educación** y al **CPEIP del Ministerio de Educación de Chile**.

**Contra el gap 2.** Ocho pasadas midieron la oferta LATAM contando *repos* y el resultado fue siempre el mismo: techo
de 0–3 estrellas, proyectos que mueren en el día 90. La conclusión del pase 6 —«no falta talento ni diseño, falta
continuidad»— sigue siendo verdadera, **pero estaba midiendo la cosa equivocada.**

El activo educativo exportable de LATAM que esta KB encontró con tracción real **no es software**. Es un **instrumento
de medición pedagógica producido por el Estado**: estandarizado, validado, con décadas de aplicación, y lo
suficientemente bueno como para que un laboratorio enfocado en países de renta baja y media lo use como vara para medir
el conocimiento pedagógico de los LLM del mundo. Chile no puso el repo. **Puso la pregunta con la que se evalúa al
modelo**, que es la pieza más cara y la más difícil de replicar de cualquier benchmark — el pase 7 ya lo había dicho de
las 10.891 rúbricas de `ProHist-Bench`.

**Y abre un sub-gap que no estaba.** `SEND` (223 preguntas de *Special Educational Needs and Disabilities*) es, con
licencia MIT, **la primera pieza de evaluación de educación especial de esta KB**. El pase 8 había dejado escrito que en
accesibilidad y educación especial «lo maduro es copyleft y lo agéntico y permisivo no pasa de 15 estrellas», y que la
capa no tenía forma de **medirse**. Ahora tiene una, es permisiva, y nadie la está usando: 12 estrellas. Ver el **gap 22**
y el patrón **P30**.

⚠️ **Dos límites, y hay que decirlos.** (a) **12 estrellas y 5 commits**: es un artefacto de investigación, no una
dependencia de producto — se usa como vara de medición en un entregable, no se empaqueta. (b) Mide **conocimiento
pedagógico declarativo** del modelo —responder un examen de habilitación docente— que **no es lo mismo que calidad de
enseñanza en diálogo**, que es lo que miden `MathTutorBench` y `UnifyingAITutorEvaluation`. Son complementarios, y
presentarlo como sustituto sería el mismo error que el pase 7 marcó con `ProHist-Bench`. 🔴 El paper (arXiv 2506.18710)
**no se pudo abrir en este pase**: `arxiv.org` sigue bloqueado por el proxy de egreso. Licencia, conteos, composición y
la atribución a Chile **sí** están verificados de primera mano en la página del repo.

## Capa MCP de mastery — cinco reinvenciones del mismo patrón (pase 5)

El pase 4 cerró el gap 5 diciendo: *"El hueco exacto es `pyKT` detrás de MCP, y no existe."* Buscando por la pieza técnica aparecen **cinco servidores MCP independientes** que exponen estado de mastery a un agente. Ninguno tiene tracción y **ninguno usa una librería de knowledge tracing entrenable** — todos implementan su propia heurística.

| Repo | Licencia | Stars | Commits | Qué implementa |
|------|----------|-------|---------|----------------|
| https://github.com/zcsabbagh/knowledge-graph-mcp | MIT ✅ | 1 | 8 | FastMCP + SQLite. Grafo de conceptos con prerequisitos, **SM-2** para repaso, mastery multidimensional con fórmula fija `0.3×recall + 0.4×application + 0.3×explanation`, detección de misconceptions |
| https://github.com/woodstocksoftware/student-progress-tracker | MIT ✅ | 1 | 9 | Perfiles, inscripciones, resultados de evaluación, mastery por tema, detección de learning gaps, recomendación de foco. Telemetría a nivel de pregunta |
| https://github.com/tejpalvirk/student | MIT ✅ | 1 | 6 | Grafo de conocimiento académico (cursos, trabajos, exámenes, conceptos) con persistencia entre sesiones |
| https://github.com/znecho9/knowledge-forest-mcp | Apache-2.0 ✅ | 0 | 3 | Árboles de prerequisitos + **mastery con evidencia obligatoria**: exige desempeño novedoso, sin asistencia y a libro cerrado antes de declarar dominio |
| https://github.com/radhepa/Teacher-MCP | MIT ✅ | 0 | 2 | MCP-first con memoria SQLite persistente, personas docentes y andamiaje en tres niveles. Incluye un Claude Skill que corre solo o contra el server |
| https://github.com/ankimcp/anki-mcp-server | **MIT** ✅ | **499** | 254 | Puente MCP hacia **Anki**, el SRS de facto: crear, leer y revisar mazos en lenguaje natural. TypeScript, v0.22.0, en beta declarada. **No es un servidor de mastery: es el único de esta capa con tracción real** |

> **Agregado en el pase 12 del 2026-10-01 — el techo de esta capa no era 1 ★, y la diferencia es de qué lado está el estándar.** Las cinco reinvenciones de mastery no pasan de 1 ★; `anki-mcp-server` tiene **499 ★ y 254 commits**. La diferencia no es calidad de código: es que los cinco **inventan** su modelo de dominio (grafo propio, SM-2 propio, esquema propio) mientras Anki **ya es el estándar instalado** de repetición espaciada y el MCP sólo lo expone. Leído junto con `py-fsrs` (MIT, en la tabla principal, que es el algoritmo moderno que reemplaza a SM-2), la lectura para un studio se invierte: **no construir el motor de mastery, conectarse al que el alumno ya usa.** Ver el patrón **P28**.

**Cómo leerlo.** Cinco autores sin relación llegaron al mismo patrón en la misma ventana: eso es **validación de mercado**, no ruido. Y el hueco de ingeniería queda mejor documentado que antes: los tres más grandes suman **3 estrellas y 23 commits**, y se verificó de primera mano en este pase que **`pyKT` sigue sin mencionar MCP ni interfaz de serving** (441 ★, 811 commits).

El gap 5 pasa entonces de *"nadie lo intentó"* a **"cinco lo intentaron y ninguno conectó la librería buena"**. Con `pyBKT` (MIT, 281 ★, publicado) en la mesa, hacerlo bien es integración, no investigación. Ver **P12**.

### Lo que el pase 6 le agrega a esta sección: los cinco reinventaron dos cosas, no una

El diagnóstico del pase 5 fue que ninguno de los cinco servidores MCP de mastery usa una librería de knowledge tracing entrenable. Es cierto, y está incompleto. **Los cinco también inventaron su propio almacén de eventos de aprendizaje**, cuando existe un estándar IEEE con cuatro implementaciones maduras (ver la capa LRS/xAPI en `repos/foundations.md`).

`learnmcp-xapi` —agregado a la tabla principal en este pase— es el primero que no comete ese segundo error: no guarda el progreso en un esquema propio, lo escribe como statements xAPI en un LRS conforme. Sigue **sin** estimar mastery, así que no reemplaza a ninguno de los cinco en lo que a ellos les falta; pero resuelve la mitad que los cinco resolvieron mal.

**Para una propuesta, la lectura es:** el componente a construir es un estimador (`pyBKT` o `pyKT`) detrás de un LRS que ya existe, expuesto por un MCP que ya existe. No es una plataforma. Ver **P15** en `compose/patterns.md`.

## Advertencias de licencia

**Actualizado en el pase 4:** la tabla principal ya **no** es "todo MIT o Apache-2.0". Al agregar agentes nuevos entraron dos AGPL y dos Creative Commons, y eso cambia qué se puede empaquetar en un entregable cerrado.

| Licencia | Repos | Qué implica para un entregable de cliente |
|----------|-------|-------------------------------------------|
| MIT / Apache-2.0 / BSD-3 ✅ **(lista DESARMADA en el pase 52: las dos piezas sin licencia ya NO figuran acá)** | DeepTutor, OpenMAIC, Project NOMAD, py-fsrs, Educhain, pyKT, **pyBKT**, Bloom, OATutor, OpenTutor, OpenTutorAI-CE, Claw-ED, **Aila**, tutor-mcp, gradescope-mcp, TutorIA, **EduBench**, y los 5 servidores MCP de mastery | Sin fricción. Construible y redistribuible cerrado |
| 🚫 **Sin licencia — ausencia MEDIDA** | **`SafeTutors`**, **`AITutor-EvalKit`**. 🔴 **Estaban en la fila de arriba hasta el pase 52.** El pase 51 midió la ausencia; el 52 **sacó los nombres de la clase permisiva en vez de sólo anotarlo al lado**, porque una lista agregada se lee de un vistazo y la nota al margen no viaja con el nombre | No entran sin gestión. Ver **P116** |
| **AGPL-3.0** ⚠️ | **FreeLingo**, **mentar**, **ChatTutor**, y **`Honcho`** (la dependencia de memoria de `tutor-gpt`) | Copyleft **de red**: si se modifica y se sirve por SaaS, hay obligación de publicar el fuente modificado. No forkear para un producto cerrado; usar como referencia de arquitectura o desplegar sin modificar |
| **CC BY-SA 4.0** ⚠️ | **education-agent-skills**, **OpenDidactia**, **UnifyingAITutorEvaluation** | Contenido con *share-alike*: los derivados heredan la obligación. Usable como referencia pedagógica o para medir internamente; **revisar con legal antes de empaquetarlo en un entregable cerrado** |
| **CC BY 4.0** | **MathTutorBench** | Sólo atribución, sin share-alike. El más limpio de los no-código |
| **GPL-3.0** ⚠️ | **tutor-gpt** *(pase 7)* | Copyleft fuerte, pero **no de red**: a diferencia de AGPL, servirlo por SaaS sin modificarlo no dispara la obligación. Modificarlo y **distribuir el binario o el código** sí. Para un entregable cerrado, no; como referencia de arquitectura de teoría de la mente, sí |
| **GPL-2.0** ⚠️ | **TAO** (`oat-sa/tao-core`) *(pase 9)* | Copyleft fuerte, sin cláusula de red. La plataforma de evaluación QTI más madura que encontró esta KB (22.533 commits) **no se puede forkear para un producto cerrado**. Se despliega tal cual y la inteligencia va al lado — la misma receta que Moodle y Open edX |
| **LGPLv3 / LGPL-3.0** ⚠️ | **openbadgeslib** (librería), **caliper-php-public** (U. de Michigan) *(pase 9)* | Copyleft **débil**: enlazar desde un producto cerrado es admisible si el usuario puede reemplazar la librería; **modificarla y distribuirla, no**. Muerde justo donde uno querría tocar, porque los perfiles de badge son específicos de cada cliente. ⚠️ `openbadgeslib` tiene **licencia partida**: LGPLv3 la librería, BSD-2-Clause el CLI |
| **EUPL-1.2** ⚠️ | **european-digital-credentials**, **European-Learning-Model** *(pase 9)* | Licencia pública de la Unión Europea, copyleft con cláusula de compatibilidad. Los dos repos están **archivados** (feb-2024) y el código vivo se mudó a `code.europa.eu`, que **esta sesión no puede alcanzar** (ver gap 14). No cotizar sobre lo archivado |
| **Sin licencia declarada** 🚫 | **EduGuardBench**, **OmniEdu** (`haolpku/Omni-Edu`), **awesome-ai-llm4education**, y **llamatutor** *(pase 7, el caso más caro: 2.1k ★)* | *Agregado en el pase 5, ampliado en el pase 7.* Sin archivo LICENSE el default legal es **todos los derechos reservados**, por mucho que el título diga "open". **Los cuatro** se pueden leer y citar; **ninguno se puede empaquetar**. Se verificó que `/blob/main/LICENSE` devuelve **404** tanto en `awesome-ai-llm4education` (pase 5) como en `llamatutor` (pase 7) |
| **Licencia de investigación custom** 🚫 | **llmgrader** (`sdrangan/llmgrader`) | *Agregado en el pase 5.* "PySilicon Research License", © 2026 Sundeep Rangan — **leída en el archivo**. No es OSI. Es el grading agéntico más maduro que encontró esta KB (240 commits, en producción en NYU, con MCP e integración a Gradescope) y **no se puede usar en un entregable**. Ver `repos/trending.md`, pase 5 |

**La trampa concreta:** `FreeLingo` aparece como MIT en artículos de prensa y agregadores. **La página del repo dice AGPL-3.0.** Se verificó en el pase 4 y se registra acá porque es el modo de falla típico — citar la licencia del listicle en vez de la del repo.

**La trampa del pase 7, que es la inversa y más cara:** `llamatutor` tiene **2.1k estrellas** y **ningún archivo de licencia**. Se verificó pidiendo `/blob/main/LICENSE` y devuelve **404**. Un repo popular, con README cuidado y demo desplegada, se lee como open source y legalmente **no lo es**: sin LICENSE el default es todos los derechos reservados. **Las estrellas no son una licencia**, y es el único indicador que un listicle reporta.

**Y la advertencia que este pase agrega sobre toda la tabla:** las tres entradas nuevas son 🚫 / AGPL-3.0 / GPL-3.0. Al día de hoy, **las únicas bases de tutor open source permisivas y de escala siguen siendo las dos de APAC** — `DeepTutor` (Apache-2.0, 40.6k ★) y `OpenMAIC` (MIT, 39.7k ★). Eso ya no es una suposición por falta de búsqueda: está medido contra las alternativas.

## Corrección sobre ciclos anteriores

### Corrección del pase 17 — la voz del menor sí está regulada, pero no por la vía que el pase 16 escribió

El **pase 16** anotó, acá arriba y en el **gap 28**, que *«desde el 2026-04-22 la voz de un menor es dato
biométrico regulado bajo la regla COPPA enmendada»*. **La conclusión práctica es correcta y la vía no.** La
distinción cambia qué se escribe en un expediente de cumplimiento, así que se corrige en vez de dejarla pasar:

- **Lo que sí hizo la regla enmendada:** agregó a la definición de información personal *«a biometric identifier
  that can be used for the automated or semi-automated recognition of an individual»*, y la enumeración **incluye
  `voiceprints`** junto con huellas, patrones de retina e iris, datos genéticos, marcha, plantillas faciales y
  *faceprints*. Exigible en pleno desde el **2026-04-22**.
- **Lo que la FTC explícitamente NO incluyó:** los datos **derivados** de voz, de rostro y de marcha
  (*voice-derived, facial-derived, gait-derived data*). Estaban propuestos en el NPRM de 2024 y **se quitaron de
  la regla final** tras los comentarios por amplitud excesiva.
- **Y el dato que vuelve más vieja la exposición, no más nueva:** un **archivo de audio con la voz de un chico ya
  estaba cubierto** como categoría propia de información personal bajo **16 CFR 312.2 antes de las enmiendas**.

**Las dos consecuencias operativas:**

1. **`voiceprint` ≠ grabación de voz.** Un *voiceprint* es una plantilla para reconocer a la persona. Un tutor de
   lectura oral que transcribe y puntúa pronunciación **sin construir ni almacenar plantilla de identificación**
   no entra por la puerta biométrica — entra por la de audio del menor, que es la que ya existía.
2. **La fecha a citar no es el 2026-04-22 para todo.** Para la grabación de voz la obligación **precede** a las
   enmiendas; lo que el 2026-04-22 agrega es la **política escrita de retención**, la **prohibición de retención
   indefinida** y el borrado una vez cumplido el propósito. Vender «esto es nuevo desde abril» es vender mal: en
   la mitad que más importa, el cliente **ya estaba incumpliendo antes**.

⚠️ **Lo que no cambia:** si el despliegue construye plantillas de identificación por voz, o toca **Illinois**
(**BIPA**, consentimiento escrito, daños estatutarios de 1.000–5.000 USD por violación), el encuadre del pase 16
aplica entero. El **gap 28** se mantiene abierto con esta precisión incorporada.


Los star counts registrados en ciclos previos de esta KB estaban **inflados por el pipeline**, no medidos. Valores reales verificados hoy contra los que se habían registrado antes:

| Repo | Registrado antes | Real 2026-09-30 |
|------|------------------|-----------------|
| Educhain | ~12k ★ | **389 ★** |
| OATutor | ~1.5k ★ | **265 ★** |
| OpenTutor | ~900 ★ | **127 ★** |
| DeepTutor | ~24k ★ | **40.6k ★** (subestimado) |
| OpenTutorAI-CE | ~600 ★ y Apache-2.0 | **107 ★ y BSD-3-Clause** (stars y licencia, las dos mal) |

Los tres primeros estaban sobreestimados entre 7x y 30x, y en OpenTutorAI-CE el pipeline además reportó la licencia equivocada. Tratar cualquier cifra de ciclos anteriores no re-verificada como no confiable — y verificar la licencia junto con las stars, porque el error no se limitó a los números.

## Capa de accesibilidad y educación especial — agregada en el pase 8 del 2026-10-01

Siete pasadas construyeron el stack por capas —agente, modelado, evaluación, seguridad, telemetría, datos— y **ninguna miró al alumno con discapacidad**. Es el hueco de cobertura más grande que tenía esta KB, y no es un nicho: en la UE la accesibilidad de una plataforma de aprendizaje dejó de ser una característica y pasó a ser **condición de acceso al mercado** (European Accessibility Act, en vigor desde el **2025-06-28**). Ver el **trend 18**.

**El hallazgo no es un repo, es la forma del segmento.** Se parte limpio en dos mitades y ninguna sirve sola:

### Mitad 1 — la tecnología asistiva madura, y es toda copyleft

| Repo | Licencia | Stars | Lenguaje | Qué es |
|------|----------|-------|----------|--------|
| https://github.com/OptiKey/OptiKey | **GPL-3.0** ⚠️ | **4.4k** | C# | Teclado en pantalla y control total de Windows **con la mirada**, para ELA / enfermedad de motoneurona. Es la pieza de tecnología asistiva más adoptada que encontró esta KB en cualquier capa |
| https://github.com/cboard-org/cboard | **GPL-3.0** ⚠️ | **759** | JavaScript | Sistema **AAC** (comunicación aumentativa y alternativa) con texto-a-voz, PWA, para parálisis cerebral y autismo. 5.531 commits. © Assistive Technology LLC; respaldado por la iniciativa **«For every child, a voice» de UNICEF** |

⚠️ **Las dos son GPL-3.0, y eso decide la arquitectura entera de un engagement de accesibilidad.** No se forkean para meterles un agente adentro. Se despliegan tal cual y la inteligencia propia va al lado — exactamente la misma receta que esta KB ya aplica a Moodle y Open edX.

### Mitad 2 — lo agéntico y permisivo, y no pasa de 15 estrellas

| Repo | Licencia | Stars | Commits | Qué implementa | Origen |
|------|----------|-------|---------|----------------|--------|
| https://github.com/AyushBinjola1/Swar-Setu | **MIT** ✅ | 15 | 4 | Detección temprana y apoyo multilingüe de **dislexia, disgrafia y discalculia**: evaluaciones interactivas, soporte por voz, dashboards por rol (padre / docente) | APAC (India — *«Built with ❤️ for India»*) |
| https://github.com/open-behavior-analysis/aba-clinical-agent | **AGPL-3.0** ⚠️ | 7 | 7 | **29 Claude Code Skills** + base Obsidian para supervisión clínica **ABA** de punta a punta (de-identificación, intake, análisis funcional de conducta, plan de tratamiento, supervisión de staff, reporte de hitos). Es la mejor ilustración del **trend 9** — la pedagogía empaquetada como skills — fuera del aula ordinaria | Sin región declarada (© Jiamei Zhang, BCBA) |
| https://github.com/ronda-ai/Ronda-App | **GPL-3.0** ⚠️ | 3 | 17 | Asistente pedagógico generativo para aula inclusiva: participación, coaching docente, gestión de seguridad. **Soberanía de datos por diseño** (self-hosting + cifrado en reposo). Anclado al **Marco para la Buena Enseñanza (MBE)** chileno | LATAM (Chile) |
| https://github.com/Noggin-Labs/noggimigo | **MIT** ✅ | 1 | 19 | Motor de tutoría **socrática local** para necesidades educativas especiales, con diagnóstico de misconceptions y seguimiento de latencia de respuesta — la latencia como señal de carga cognitiva es un diseño que no aparece en ningún otro repo de la KB | Sin región declarada (Noggin Labs) |
| https://github.com/100205ivan/EyeEP | 🚫 **sin licencia** | 1 | 12 | Gestión de **IEP** (programa educativo individualizado) asistida por AI para docentes de educación especial. Sin LICENSE no es reutilizable | APAC (Taiwán — *inferido del README en chino tradicional, no declarado*) |
| https://github.com/SabioTechTeam/Teacher-Hub | **MIT** ⚠️ *(ver advertencia)* | 0 | 156 | Proyecto **«UnStuck»**: sistema adaptativo de matemática K-6 con test adaptativo computarizado (CAT), modelo vivo del alumno, verificación determinística de dominio y **parsing de acomodaciones IEP / 504** | Sin región declarada |
| https://github.com/Autism-Technology-Research-Syndicate/SEALApplication | **GPL-3.0** ⚠️ | 10 | 321 | Currículo de educación especial personalizado para autismo analizando respuesta del alumno con visión por computadora. 🚫 **El repo está marcado como deprecado** | North America (AUTRS, EE. UU.) |
| https://github.com/classifiedstudentkabir/Sign-Language-Interpreter | 🚫 **sin licencia** | 60 | 8 | *SignLens* — reconocimiento de **lengua de señas** a texto en el navegador con MediaPipe. Es el repo con más estrellas del topic `inclusive-education` y **no tiene licencia**: el default legal es todos los derechos reservados | Sin región declarada (hackathon HackNova) |

⚠️ **Trampa de licencia verificada en `Teacher-Hub`, y vale como advertencia general.** El README dice literalmente *«MIT License — free for educational and non-commercial use»*. **Las dos mitades de esa frase se contradicen:** la MIT permite uso comercial sin restricción. No se sabe si el autor quiso MIT o quiso una no-comercial, y esa ambigüedad **es** el riesgo. Antes de cualquier entregable hay que leer el archivo `LICENSE` y, si sigue sin cerrar, pedirle al autor que lo aclare por escrito. Anotado porque es la segunda vez que esta KB encuentra una declaración de licencia que el texto no sostiene (la primera fue OpenTutorAI-CE, donde el pipeline reportó Apache-2.0 y era BSD-3).

### La pieza transversal, y es la única con tracción y licencia limpia

| Repo | Licencia | Stars | Commits | Qué implementa |
|------|----------|-------|---------|----------------|
| https://github.com/Community-Access/accessibility-agents | **MIT** ✅ | **419** | 374 | Agentes de revisión de accesibilidad que **corren dentro del harness de codificación**: Claude Code, GitHub Copilot, Claude Desktop, Codex, Gemini CLI. Seis skills de entrada que rutean a especialistas sobre ARIA, teclado, foco, formularios, contraste, modales, live regions, encabezados, tablas, carga cognitiva, i18n, móvil, email y visualización de datos. Cubre también documentos (Word, Excel, PowerPoint, PDF, ePub) y add-ons de NVDA. **Propósito declarado: que las herramientas de AI dejen de generar código inaccesible** |
| https://github.com/sololabstr/uisight | **MIT** ✅ | 128 | n/d | Medición de contraste, área táctil y *theme drift* en sesiones en vivo, expuesta como **servidor MCP** |
| https://github.com/weAAAre/a11y-agents-kit | **MIT** ✅ | 34 | n/d | Kit de skills de accesibilidad para harnesses de codificación con AI, de **weAAAre** (escuela de accesibilidad digital) |

**Por qué `accessibility-agents` es el hallazgo comercial del pase 8 y no los tutores.** Es MIT, tiene 419 ★ y 374 commits — más tracción que **cualquier** pieza de educación especial de este pase y que la mayoría de la capa de evaluación — y ataca la obligación que **ya está vigente** (EAA, WCAG 2.2 AA) en vez de la que está prohibida (redacción de IEP, ver abajo). **No es un repo educativo**, y por eso ninguna búsqueda de los siete pases anteriores lo iba a encontrar. Ver el patrón **P17**.

### El dato que da vuelta la lectura comercial del segmento en North America

El open source de educación especial que apareció en este pase apunta mayoritariamente a **redactar o gestionar el IEP** (`EyeEP`, el parsing de IEP/504 de `Teacher-Hub`). Y esa es, específicamente, **la tarea que las jurisdicciones de EE. UU. están prohibiendo**: la guía de **Delaware** prohíbe usar AI para objetivos de IEP, evaluación docente y calificación subjetiva, y el marco de **Nueva York** prohíbe usar AI para el desarrollo de planes **IEP o 504**.

**La oferta open source está apuntando al único paso del flujo que no se puede automatizar.** Lo vendible es el resto del flujo — preparar material, diferenciar contenido, adaptar lectura, documentar evidencia — con el docente como autor de la decisión. El diseño de referencia para eso ya está en esta KB y es **`tero`**: *el agente propone, el docente decide*, sin escritura de archivos sin aprobación humana. Ver el patrón **P18** y el **gap 12**.

## Capa de credenciales verificables e interoperabilidad — agregada en el pase 9 del 2026-10-01

Ocho pasadas construyeron el stack del alumno —agente, modelado, evaluación, seguridad, telemetría, datos, accesibilidad— y **ninguna miró qué pasa cuando el aprendizaje termina y hay que acreditarlo.** Es la capa de la *credencial*: quién emite el certificado, con qué formato, cómo se verifica sin llamar a la institución emisora, y cómo viajan la matrícula y el ítem de examen entre sistemas.

Existe, es un estándar con certificación de conformidad, y **esta KB nunca la buscó porque no se llama «agente» ni «tutor»** — se llama Open Badges 3.0, W3C Verifiable Credentials, QTI, OneRoster y Caliper. Es la cuarta vez que se aplica la regla del pase 6: *cuando falta una capa, preguntarse si tiene un nombre que uno no está usando.*

**El hallazgo del pase no son los repos nuevos: es que las implementaciones de referencia de estos estándares se están apagando mientras los estándares siguen siendo obligatorios.** Ver el **trend 19** y el **gap 14**.

### Lo que está vivo, verificado y es permisivo

| Nombre | Repo | Licencia | Stars | Commits | Lenguaje | Descripción | Origen (región) |
|--------|------|----------|-------|---------|----------|-------------|-----------------|
| learner-credential-wallet | https://github.com/digitalcredentials/learner-credential-wallet | **MIT** ✅ | 88 | 1.309 | TypeScript | Billetera móvil (React Native + Expo) para que el **alumno** reciba, guarde y presente credenciales verificables de formación y empleo. Implementa la *Learner Credential Wallet specification* del Digital Credentials Consortium sobre W3C VC. v2.2.10 (junio 2026). **Es la pieza de esta capa con más commits y la única pensada desde el lado del alumno y no del emisor.** ⚠️ Ver el cambio de gobernanza abajo | **North America (EE. UU.)** — el consorcio declara sede en el **MIT**; contacto `lcw-support@mit.edu`, financiamiento inicial del **U.S. Department of Education** |
| verifier-plus | https://github.com/digitalcredentials/verifier-plus | **MIT** ✅ | 18 | 395 | TypeScript | App Next.js que **verifica y muestra** credenciales verificables, con almacenamiento y links públicos compartibles. Acepta la credencial por copiar/pegar, subida de archivo, URL o **QR**. Es el lado «¿esto es auténtico?» del circuito, que es el que pregunta el empleador | North America (EE. UU., Digital Credentials Commons) |
| issuer-coordinator | https://github.com/digitalcredentials/issuer-coordinator | **MIT** ✅ | 12 | 55 | JavaScript | App Express que **emite** credenciales verificables firmadas criptográficamente y después las puede **revocar o suspender**. Orquesta un servicio de firma y un servicio de estado vía Docker Compose. Implementa **W3C VC API** (endpoints de emisión y de actualización de estado) y soporta el formato **Open Badges 3.0** por integración de contexto. v1.0.0 | North America (EE. UU., Digital Credentials Commons) |
| qti3-item-player | https://github.com/amp-up-io/qti3-item-player | **MIT** ✅ | 30 | 596 | JavaScript (Vue 2.6) | Reproductor de ítems de evaluación **QTI 3**: carga QTI XML, maneja la sesión del ítem, procesa respuestas y ejecuta el *response processing* con scoring completo, ítems adaptativos y *template processing*. **Tiene certificación de conformidad QTI 3 Basic y QTI 3 Advanced «Delivery» de 1EdTech** — es el único artefacto de toda esta KB con certificación de conformidad de un organismo de estándares. Licencia leída en el archivo: `Copyright (c) 2022-2024 Amp-up.io, LLC` | Sin región declarada (Amp-up.io, LLC) |
| esco-skill-extractor | https://github.com/KonstantinosPetrakis/esco-skill-extractor | **MIT** ✅ | 32 | 29 | Python | Extrae **competencias y ocupaciones** de texto libre (avisos de trabajo, CV, descripciones de curso) y las mapea a la taxonomía europea **ESCO** y a ocupaciones **ISCO**, con *sentence transformers* y similitud cosena. **Es la única pieza que encontró esta KB que traduce lenguaje natural a un vocabulario de competencias normalizado** — el paso que convierte «el alumno terminó el módulo» en «el alumno acredita esta competencia». ⚠️ No declara versión de ESCO | Sin región declarada (autor Konstantinos Petrakis) |
| oneroster (TypeScript) | https://github.com/LongsightGroup/oneroster | **MIT** ✅ | 0 | 33 | TypeScript | Parsea, valida y escribe **paquetes CSV de OneRoster** y habla la **REST API** en las versiones **1.1 y 1.2**. Corre en Node, Deno y navegador; incluye cliente REST de lectura de roster y de notas del *gradebook*, y un *provider router* neutral al framework para construir servicios OneRoster. Declara validación contra las especificaciones oficiales y las suites de certificación. **0 ★: referencia de integración, no dependencia de producción** | Sin región declarada (Longsight Group) |
| lti-1-3-php-library | https://github.com/1EdTech/lti-1-3-php-library | **Apache-2.0** ✅ | 124 | 110 | PHP | Librería oficial de 1EdTech para construir *tool providers* **LTI 1.3**: flujo de login OIDC, validación de mensajes, respuestas de *deep linking* e integración con los servicios de la plataforma (envío de notas, lectura del roster de miembros). **Es la pieza de esta capa con más estrellas que sigue pública y permisiva**, y es la que hace que un agente se pueda montar dentro de cualquier LMS conforme | Global (1EdTech, `1edtech.org`) |
| openbadges-specification | https://github.com/1EdTech/openbadges-specification | ⚠️ **no declarada en la página** | 205 | 2.266 | HTML | La **especificación** de Open Badges, no una implementación: versiones **3.0, 2.1 y 2.0** en directorios separados (`ob_v3p0`, `ob_v2p1`, `ob_v2p0`), más **Comprehensive Learner Record (CLR) 2.0**. Ramas `main` (estable) y `develop`. Es el documento normativo al que hay que programar; **para el código hay que ir a terceros**, que es exactamente el problema de esta capa | Global (1EdTech) |

### Lo maduro y lo copyleft — la misma forma que el pase 8 encontró en accesibilidad

| Repo | Licencia | Stars | Commits | Lenguaje | Qué es |
|------|----------|-------|---------|----------|--------|
| https://github.com/oat-sa/tao-core | **GPL-2.0** ⚠️ | 64 | **22.533** | PHP | Extensión fundacional de **TAO**, plataforma de evaluación basada en QTI y LTI: integración por webhooks, control de acceso por roles, *feature flags*, colas de tareas, middleware y manejo de CSRF. **22.533 commits** — es, por volumen de trabajo acumulado, la pieza más madura de toda esta KB en cualquier capa. Creada en la **Universidad de Luxemburgo**, mantenida por Open Assessment Technologies. ⚠️ **GPL-2.0: no se forkea para un producto cerrado.** Se despliega tal cual y la inteligencia va al lado |
| https://github.com/luisgf/openbadgeslib | **LGPLv3** (librería) **/ BSD-2-Clause** (CLI) ⚠️ | 1 | 404 | Python | Librería y CLI para el ciclo completo de **emisor Open Badges 3.0**: emite W3C VC como **JWT-VC** o Data Integrity (LDP), las *hornea* dentro de SVG/PNG, las verifica, y **revoca o suspende** con **W3C Bitstring Status Lists** y `did:web`. Claves RSA-2048 (RS256), ECC P-256 (ES256) y Ed25519 (EdDSA). Soporta además OB 2.0 estricto y OB 1.0 legacy. v4.0.0 del **2026-07-22**. Autores: Luis González Fernández y Jesús Cea Avión. **404 commits y 1 estrella: el código más completo de emisión OB 3.0 que encontró esta KB, y nadie lo usa** |
| https://github.com/tl-its-umich-edu/caliper-php-public | **LGPL-3.0** ⚠️ | 3 | 365 | PHP | Fork de la **Universidad de Michigan** del cliente PHP de **Caliper Analytics** (la API de sensores de telemetría de 1EdTech), con `Options::setHttpHeaders()` agregado para uso propio. **Es hoy la implementación PHP de Caliper que sigue accesible** — ver abajo por qué |

⚠️ **`openbadgeslib` tiene licencia partida y hay que leerla antes de cotizar.** La **librería es LGPLv3** y las **herramientas CLI son BSD-2-Clause**. Enlazar la librería desde un producto cerrado es admisible bajo LGPL si se respeta la posibilidad de reemplazarla; **modificarla** y distribuirla, no. La distinción importa porque es la pieza que uno querría tocar (los perfiles de badge son específicos de cada cliente). Ninguna fuente secundaria que describe este proyecto menciona su licencia.

### 🔴 El hallazgo del pase: tres implementaciones de referencia que ya no están

Esto es lo que vale de esta pasada, y no es un repo nuevo. Los estándares de esta capa siguen vigentes y obligatorios; **su código de referencia se está retirando.**

| Qué era | URL canónica que todavía citan los listicles | Estado verificado 2026-10-01 |
|---|---|---|
| **Badgr** — la implementación de referencia de Open Badges que cita toda la documentación del sector | `https://github.com/concentricsky/badgr-server` | 🔴 **404.** Y la búsqueda de repositorios de la organización `concentricsky` con el término `badgr` devuelve literalmente **«No repositories matched your search»**. La organización hoy **verifica el dominio `instructure.com`** (Eugene, Oregón). Badgr pasó a ser **Canvas Credentials** de Instructure y después se plegó en **Parchment Digital Badges** |
| **caliper-php** — cliente PHP oficial de Caliper Analytics | `https://github.com/1EdTech/caliper-php` | 🔴 **404.** El fork de la Universidad de Michigan declara el motivo en su propio banner, **citado textual**: *«This had been archived, but has been unarchived following 1EdTech making its caliper-php private.»* Es decir: **el propio organismo de estándares puso en privado su implementación de referencia**, y una universidad tuvo que desarchivar su fork para no quedarse sin cliente |
| **caliper-python** — implementación de referencia de la Sensor API en Python | `https://github.com/IMSGlobal/caliper-python` | 🔴 **404** |

**Cómo leerlo con rigor.** Un 404 en GitHub no distingue entre *borrado*, *renombrado* y *puesto en privado*: desde afuera son indistinguibles. Lo que está verificado de primera mano es que **las tres URL canónicas no resuelven** y que, en el caso de `caliper-php`, **el mantenedor del fork nombra la causa** (1EdTech lo hizo privado). Para `badgr-server` hay además una segunda señal independiente: la búsqueda dentro de la organización no devuelve nada.

**Por qué importa comercialmente, y es más que una molestia de ingeniería.** La obligación de interoperar no desapareció con el código: un cliente que compra «credenciales digitales» o «analítica de aprendizaje conforme» sigue necesitando OB 3.0, Caliper o QTI. Lo que cambió es **de dónde sale el código**: ya no del organismo ni del vendor de referencia, sino de **terceros certificados** (`qti3-item-player`, MIT, con certificación de conformidad), **consorcios universitarios** (`digitalcredentials/*`, MIT) y **forks de universidad** (`caliper-php-public`, LGPL-3.0). Eso es a la vez el riesgo y la oportunidad: el riesgo es construir sobre una URL que mañana no está; la oportunidad es que **el integrador que sabe cuál de estas piezas sigue viva vale más que el que sabe el estándar.** Ver el patrón **P21**.

### El cambio de gobernanza de la billetera, que hay que saber antes de proponerla

`learner-credential-wallet` es MIT, tiene 1.309 commits y es la pieza más trabajada de esta capa — y **acaba de cambiar de manos.** La página del repo declara, sobre la v2.2.10 de junio de 2026, que *es el último release como Digital Credentials Consortium at MIT*, y que el proyecto pasa a alojarse bajo **OpenWallet Foundation Labs**.

Hay una segunda señal del mismo movimiento: la organización de GitHub ya no se presenta como «Digital Credentials Consortium» sino como **Digital Credentials Commons** (`dccommons.org`, EE. UU., **124 repositorios públicos**).

**Qué significa para una propuesta.** No es un abandono — un traspaso a una fundación neutral es, en general, señal de madurez y de continuidad (es lo mismo que esta KB registró para `goose` al pasar a la Linux Foundation). Pero **sí significa que la cadena de custodia cambió en los últimos cuatro meses**, y que la documentación, los issues y la hoja de ruta van a mudar de lugar. Al proponer esta pieza hay que **fijar la versión y confirmar dónde vive el mantenimiento activo**, no citar el repo del MIT como si nada hubiera pasado.

### La vía de entrada deja de ser sólo PHP, y el lado LMS sigue vacío — agregado en el pase 24 del 2026-10-01

**Sexto pase sin agentes nuevos** (la tabla principal sigue en 37 filas reales, sin relleno), pero el barrido por
**estándar instalado** —la consigna que dejó el pase 23— destapó un sesgo de esta KB que afectaba a tres patrones:
**toda la capacidad LTI registrada era PHP**, porque la KB sólo había encontrado `1EdTech/lti-1-3-php-library`.

| Nombre | Repo | Licencia | ★ | Forks | Lenguaje | Qué es | Región |
|---|---|---|---|---|---|---|---|
| java-lti-1.3 | https://github.com/UOC/java-lti-1.3 | **MIT** ✅ | 21 | 14 | Java | Librería **LTI Advantage** completa, v**1.0.0**. La de más tracción de la familia UOC | EMEA (Universitat Oberta de Catalunya, Barcelona) |
| spring-boot-lti-advantage | https://github.com/UOC/spring-boot-lti-advantage | **MIT** ✅ | 16 | 17 | Java | LTI Advantage para **Spring Boot**: Spring Security valida los *launches* y trae `RestTemplate` de **AGS** (Line Item, Result, Score), **NRPS** y *Deep Linking* por el *launch* OIDC | EMEA (UOC) |
| java-lti-1.3-platform | https://github.com/UOC/java-lti-1.3-platform | ⚠️ **sin licencia declarada** | 0 | 1 | Java | *«Library that **will** implement a full LTI Advantage platform»* — **el lado LMS**. El tiempo futuro del README es el dato: es intención | EMEA (UOC) |
| lti-1-3-php-library (Packback) | https://github.com/packbackbooks/lti-1-3-php-library | **Apache-2.0** ✅ | 53 | 25 | PHP | Segundo *tool provider* LTI 1.3 en PHP, **1.038 commits**. **Independiente** del de 1EdTech, no un fork | North America (Packback, Chicago) |
| OpenAssessmentsClient | https://github.com/gnowledge/OpenAssessmentsClient | **Apache-2.0** ✅ | 0 | 3 | JavaScript (React) | Cliente **QTI 1.x y 2.x**. **No es QTI 3**: para QTI 3 sigue siendo `amp-up-io/qti3-item-player`, el único artefacto certificado por 1EdTech de esta KB | APAC (gnowledge) |

🔴 **El asterisco, y es el que hay que levantar en el *discovery*.** De los 14 repos LTI de la UOC, **13 son *tool-side***
—construyen la herramienta que entra al LMS— y **el único *platform-side* no declara licencia y dice que «implementará»**.
Lo mismo vale para todo lo que esta KB registró en nueve pases: es capacidad de **entrar** a un LMS, no de **ser** uno.
**Si el engagement pide el lado plataforma, esta KB no tiene con qué y hay que decirlo antes de la propuesta, no después.**

**Por qué entran con 21 y 16 estrellas.** Es código que una universidad pública europea usa en su propio campus — el mismo
criterio por el que el pase 22 aceptó `tutor-contrib-aspects` con 14 ★. Para un cliente de educación superior europea con
stack Java/Spring, **la alternativa era meterle PHP al diagrama por una limitación de esta base de conocimiento.**

⚠️ **Corrección de procedencia verificada en este pase.** La hipótesis natural —que la librería de 1EdTech fuera una
donación de Packback y que esta KB apuntara al *fork*— **es falsa**: el README de 1EdTech dice que *«This library was
initially created by @MartinLenord from **Turnitin**»*. Son dos librerías PHP independientes, las dos Apache-2.0. La fila
de la KB está bien apuntada; lo que faltaba era saber que hay una segunda, que importa para decidir dónde abrir un *issue*.


### Lo que esta capa **no** tiene, y es el gap que abre el pase 9

Se buscó explícitamente un agente que **emita o consuma** credenciales verificables, y no existe. Ninguno de los 25+ agentes de la tabla principal escribe un Open Badge, y ninguna de las piezas de credenciales tiene interfaz de agente ni servidor MCP.

**El stack del alumno y el stack de la credencial no se tocan en ningún punto** — y la pieza que los conectaría es justamente la que ya está documentada en esta KB desde el pase 6: el Learning Record Store. El LRS registra la evidencia (xAPI), el estimador de mastery decide si hay dominio (`pyBKT`/`pyKT`, gap 5), y **nadie convierte esa decisión en una credencial verificable**, que es el artefacto que el alumno puede llevarse y el empleador puede verificar. Ver el **gap 13** y el patrón **P19**.

## Capa de contenido curricular — agregada en el pase 10 del 2026-10-01

Nueve pasadas preguntaron *qué hace el agente* y nunca *de qué lee*. Esta sección es la respuesta, y el hallazgo no es un
repo: es que **la licencia del contenido no es la licencia del código, y en esta capa casi nunca coincide**.

### 🔴 El hallazgo del pase: dos fuentes de primera mano que se contradicen, y las dos están en la KB

| Fuente verificada | Qué dice, textual | Dónde vive la afirmación |
|---|---|---|
| `openstax/osbooks-calculus-bundle` | *«Calculus Volume 1, Calculus Volume 2, and Calculus Volume 3 are available under the Creative Commons Attribution-NonCommercial-ShareAlike License»* | archivo **`LICENSE`** |
| `openstax/osbooks-biology-bundle` | *«Creative Commons Attribution-NonCommercial-ShareAlike License»* (Biology 2e, Concepts of Biology, Biology for AP®) | archivo **`LICENSE`** |
| `openstax/osbooks-college-physics-bundle` | *«College Physics 2e and College Physics for AP® Courses 2e are available under the Creative Commons Attribution-NonCommercial-ShareAlike License»* | archivo **`LICENSE`** |
| `CAHLR/OATutor` | *«All content in this repository is made available under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. Attribution is given within each json file, indicating the authoring organization and license for each hint, scaffold, and problem»* | **README** |
| `pythpythpython/openstax-mcp-server` | el contenido servido está *«licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)»* | **README** |

**Las tres primeras filas son `LICENSE`; las dos últimas son README.** Y OATutor declara curar problemas de
**Calculus Volume 1**, que es exactamente uno de los títulos cuyo `LICENSE` dice **NonCommercial-ShareAlike**.

**Lo que este pase afirma, y nada más:** las cinco citas están verificadas de primera mano, y **no son compatibles entre
sí para material derivado** — ShareAlike obliga a licenciar la derivación igual, y NonCommercial prohíbe exactamente el uso
que tiene un entregable facturado. Lo que este pase **no** afirma es cuál de las dos es la correcta. `openstax.org`, donde
vive el catálogo con la licencia por título, está **bloqueado por el proxy de egreso de esta sesión** (ver el gap 17), así
que la discrepancia se registra sin resolver.

### La regla operativa, y es barata de aplicar

El propio README de OATutor dice dónde está la respuesta: **la licencia está declarada por ítem, dentro de cada JSON**
(*«indicating the authoring organization and license for each hint, scaffold, and problem»*). Entonces:

1. **No usar la licencia declarada a nivel de repo** para contenido. Ni la del README, ni la del badge.
2. **Leer el campo de licencia del ítem** que se va a ingestar, y guardarlo junto al ítem. Ese manifiesto es el entregable
   (ver **P22**).
3. **Un corpus mezclado es del color del ítem más restrictivo**, no del promedio.

⚠️ **Esto pega directamente sobre el patrón P1 de esta KB**, que recomienda *«la lógica de BKT de OATutor + su contenido
curado de OpenStax en JSON»*. **El código MIT de OATutor no está en discusión; el contenido sí.** P1 queda corregido en
`compose/patterns.md`.

### Los dos corpus grandes con licencia apta para uso comercial

| Corpus | Licencia | Estado de verificación | Por qué importa |
|---|---|---|---|
| **Oak National Academy** (currículo completo, Reino Unido) | **Open Government Licence v3.0** — permite uso comercial explícitamente | ⚠️ **parcial**: `support.thenational.academy` está **bloqueado por el proxy**. La licencia y el permiso comercial vienen de prensa educativa británica (*Schools Week*), no del documento de licencia | **Es el único caso de esta KB donde el código y el contenido son los dos utilizables**: `Aila` es MIT y ya está en la tabla principal desde el pase 5, y el currículo que Aila sirve es OGL. ⚠️ Hay indicios de **restricción geográfica al Reino Unido** en la cobertura de prensa: verificar antes de proponerlo fuera de UK |
| **OpenStax** (40+ títulos) | 🔴 **en disputa** — ver el cuadro de arriba | ⚠️ verificado en GitHub (**NC-SA** en 3 de 3), no verificado en el catálogo oficial | Es el corpus que todo el mundo asume CC BY. **Asumirlo es el riesgo.** |

### Lo que esta capa no tiene, y es el gap que abre el pase 10

Un puente agente↔contenido con tracción. Hay **uno** (`openstax-mcp-server`, 1 ★, 7 commits) y **declara mal la licencia
de lo que sirve**. El segundo candidato, `moarshy/mcp-tutor` (**0 ★**, 26 commits, 🚫 **sin licencia** — el repo sólo dice
*«This project is experimental and intended for educational and research purposes»*), convierte **repositorios de
documentación** en cursos con DSPy y los expone por MCP: es un tutor de documentación técnica, no de currículo escolar.
Ver el **gap 15**.

---

---
*Verificado manualmente vía WebFetch, no por el pipeline automático. Última verificación: 2026-10-01 (pase 10).*
*Nota de método del pase 5: `curl -sI` contra github.com devuelve **403** a través del proxy de egreso, así que toda verificación se hizo con WebFetch contra la página del repo. Están bloqueados `arxiv.org`, `openreview.net`, `aclanthology.org`, `huggingface.co` y `ojs.aaai.org`, por lo que **los venues, conteos de ítems y hallazgos de los papers no pudieron verificarse en la fuente primaria** — sólo lo alojado en github.com está verificado de primera mano.*

## Capa predictiva / early warning — agregada en el pase 11 del 2026-10-01

Diez pasadas preguntaron qué hace el agente, de qué lee, dónde escribe, cómo se lo mide y cómo se acredita al alumno.
Ninguna preguntó por la capa que **decide sobre el alumno**: el scoring de riesgo de abandono, el *early alert*, el
*student success* que toda universidad compra. Es la capa con más presupuesto asignado del sector y la más regulada
—el Anexo III del EU AI Act la nombra literalmente— y es **la peor abastecida de open source de toda esta KB.**

### 🔴 El hallazgo del pase, y es una medición, no una impresión

Dos consultas acotan la oferta entera:

| Consulta (GitHub, 2026-10-01) | Resultados | Máximo de estrellas |
|---|---|---|
| `topic:learning-analytics stars:>50` | **2 repos en todo GitHub** | 169 ★ — y es `AkihikoWatanabe/paper_notes`, un blog de notas de papers, no un sistema |
| `dropout prediction student license:mit pushed:>2026-01-01` | **110 repos** | **6 ★** |

Es decir: **el único repo real con más de 50 estrellas en el topic de learning analytics es `OpenLRW`** (62 ★, ver
`repos/foundations.md`), que es un almacén de datos, no un predictor. Y la capa predictiva propiamente dicha son
110 repos MIT activos en 2026 cuyo techo es **6 estrellas**.

### El repo que está arriba de esos 110, y por qué el dato importa

| Repo | Licencia | Stars | Qué es, y la advertencia |
|---|---|---|---|
| https://github.com/Aliipou/Student-Retention-Prediction | MIT ✅ | 6 | El tope de la capa. Predice riesgo de abandono con señales de engagement disponibles **a la semana 4** (logins al LMS, asistencia, entrega de trabajos), con **SHAP** para que el tutor entienda por qué se marcó a un alumno. Declara 137 tests y 100% de cobertura. 22 commits, actividad hasta 2026-09-15. ⚠️ **Y entrena con datos sintéticos generados por el propio repo** (`python -m src.train_pipeline`): no hay dataset real detrás, y no hay auditoría de fairness. Como *andamio de ingeniería* sirve; como modelo, no predice nada todavía |
| https://github.com/dssg/student-early-warning | 🔴 **NO ES OPEN SOURCE — licencia académica NO COMERCIAL de la Universidad de Chicago** (texto leído en `master:LICENSE`, pase 51). Permite uso *«for academic research or other not-for-profit scholarly purposes … at a non-profit or government institution»* y 🔴 **excluye explícitamente *«any service or part of selling a service that uses the Program»***. Licencia comercial: Polsky Center, `polsky@uchicago.edu`. ⚠️ **Estaba archivada como *«Other (NOASSERTION)»*, que suena a pendiente administrativo y es un BLOQUEO DURO para una consultora que vende servicios** | 70 | El más estrellado de la capa en términos absolutos, de **Data Science for Social Good** (Universidad de Chicago): early warning de abandono en secundaria, en R. **Último push 2018-08-22.** Sin licencia SPDX reconocible, así que legal no lo va a aprobar sin revisión manual. Valor real: su *metodología* y su feature engineering, no su código |
| https://github.com/novatrix-2030/SIH-2026 | 🚫 **sin licencia** | 0 | "DropGuard": plataforma de early warning explicable para instituciones de la India. Stack serio —Next.js 14 / React 19, FastAPI, LightGBM + XGBoost, **SHAP**, Groq con Llama-3.3-70B, Postgres, Docker—. Es una entrega del **Smart India Hackathon 2026** (PS Code `SIH-2026-13-002`, categoría *Smart Education*), 17 commits. 🚫 Sin licencia. **Es el patrón del gap 2 (LATAM) repetido en APAC:** buen problema, buen diseño, cero continuidad |

### Lo que sí es utilizable de esta capa, y no son predictores

| Repo | Licencia | Stars | Para qué sirve en un engagement |
|---|---|---|---|
| https://github.com/terracotta-education/terracotta | **Apache-2.0** ✅ | 21 | Plug-in de LMS para correr **ensayos controlados aleatorizados dentro del aula**: diferencia el contenido de una tarea en variantes de tratamiento, asigna alumnos al azar, y trae consentimiento informado oculto al docente, filtrado de no-consintientes en los reportes y eliminación de identificadores en las exportaciones. 2.572 commits, actividad al 2026-09-30. **Es la única pieza permisiva de esta KB que permite demostrar que una intervención funcionó** en vez de afirmarlo — y la privacidad ya viene resuelta, que es la mitad cara de un comité de ética |
| https://github.com/GoogleCloudPlatform/aira | **Apache-2.0** ✅ | 24 | Evaluación automática de **fluidez lectora**: clasifica al alumno en Pre-reader / Reader / Advanced y puntúa la performance, sobre la plataforma AI de Google Cloud. Escrito por *Education Engineers* de Google Cloud. ⚠️ **Y hay que leer su propia advertencia antes de proponerlo:** el repo declara que es "an experiment (proof-of-concept only)", **no un producto soportado de Google**, que no se usen datos personales ni sensibles, y que **no debe usarlo un menor de 13 años** — en una herramienta cuyo caso de uso es la alfabetización inicial. Como referencia de arquitectura es buena; como base de un entregable con alumnos reales, no |

### La corrección de encuadre que este pase le hace a la KB

La KB viene sosteniendo, desde el pase 7, que el cuello de botella del modelado del alumno **es el dato**: los
datasets de knowledge tracing son NonCommercial (gap 11). **En esta capa es exactamente al revés, y conviene no
exportar la conclusión de una capa a la otra.** Ver `repos/foundations.md`, capa de datos de deserción: los dos
corpus canónicos de predicción de abandono son **CC BY 4.0**, con uso comercial permitido. Acá no falta el dato:
**falta el software, y falta quien lo mantenga.**

## Capa de distribución por *skills* de agente — agregada en el pase 12 del 2026-10-01

Las pasadas 7 y 8 anotaron dos veces, al pasar, que había pedagogía distribuida **como skill de agente** en vez de
como producto (`education-agent-skills` primero, `Bloom` en modo CLI después), y las dos veces lo trataron como la
anécdota de un repo. **Este pase la trata como una capa y la mide.** El resultado es un número, no una impresión.

### 🔴 El hallazgo del pase: la vertical científica construyó en este canal una biblioteca de 47.2k ★ con MIT; la educativa tiene 815 ★ y es *share-alike*

Mismo estándar (**Agent Skills**), mismos harnesses (Claude Code, Codex, Cursor, Antigravity, Gemini CLI), misma
mecánica de distribución —un repo de Markdown, sin backend, sin despliegue, sin dependencias que auditar—. Verificado
de primera mano contra la página de cada repo el 2026-10-01:

| Biblioteca | Vertical | Licencia | Stars | Contenido |
|---|---|---|---|---|
| https://github.com/K-Dense-AI/scientific-agent-skills | Ciencia | **MIT** ✅ | **47.2k** | 181 skills + 100+ bases de datos científicas + 70+ workflows de paquetes Python. Declara 160.000+ científicos usuarios |
| https://github.com/virgiliojr94/book-to-skill | Genérico (libro → skill) | **MIT** ✅ | **33.2k** | Convierte PDF/EPUB/DOCX en skill estructurada con carga por capítulo y cheatsheet |
| https://github.com/GarethManning/education-agent-skills | **Educación** | **CC BY-SA 4.0** ⚠️ | **815** | 165 skills pedagógicas evidence-grounded en 20 dominios |
| https://github.com/ZeKaiNie/universal-examprep-skill | **Educación** | **MIT** ✅ | **299** | Tutor de examen que enseña desde las diapositivas de la cátedra, con cita de página |
| https://github.com/anthropics/k12-teacher-skills | **Educación** | **Apache-2.0** ✅ | **541** | 4 skills K-12 **+ carpeta `evals/`**. «Skills and eval rubrics for K-12 teachers, co-developed with Learning Commons». *Agregado en el pase 17 — nuevo techo permisivo del canal educativo* |
| https://github.com/learning-commons-org/agent-skills | **Educación** | **Apache-2.0** ✅ | 35 | Las mismas 4 skills del lado del consorcio, con `evals/` de rúbricas de pedagogía, rigor, formato y andamiaje. *Agregado en el pase 17* |

**Los dos números del pase son 58× y 158×.** La biblioteca de skills de la vertical científica tiene **58 veces** las
estrellas de la educativa, y **158 veces** las del mejor artefacto educativo con licencia permisiva. No es que el
canal no funcione para educación: es que **la educación no lo ocupó.**

**Y el techo educativo es justamente el que no se puede empaquetar.** `education-agent-skills` —815 ★, 165 skills, el
activo más grande de esta capa— es **CC BY-SA 4.0**: *share-alike*, los derivados heredan la obligación. Esta KB ya lo
tenía marcado en «Advertencias de licencia», pero no había registrado la consecuencia estructural: **el mejor activo
de la capa de distribución más barata de la industria es el que no entra en un entregable cerrado**, y el mejor
permisivo es un orden de magnitud más chico.

### Los paquetes educativos verificados, y seis de los siete son nuevos en esta KB

Todos verificados vía WebFetch contra la página del repo el 2026-10-01 (licencia, stars y descripción leídas de
primera mano):

| Nombre | Repo | Licencia | Stars | Lenguaje | Qué hace | Origen (región) |
|---|---|---|---|---|---|---|
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 ⚠️ | 815 | Markdown/YAML | 165 skills pedagógicas en 20 dominios. El dominio 20 es *student-facing*, el resto apunta a docentes y diseñadores | EMEA (autor UK) — *ya estaba en la KB* |
| human-skill-tree | https://github.com/24kchengYe/human-skill-tree | **AGPL-3.0** ⚠️ | 562 | TypeScript | 33 skills de K-12 a carrera e inteligencia social, sobre ciencia cognitiva. Híbrido: skills **+** app web (aula multi-agente, repetición espaciada). v2.0 del 2026-03-18 | APAC |
| universal-examprep-skill | https://github.com/ZeKaiNie/universal-examprep-skill | **MIT** ✅ | 299 | Markdown | Enseña desde las diapositivas de la cátedra **citando página**, recorta figuras, evalúa con la práctica real y mantiene memoria entre sesiones. Optimizado para modelos chicos y baratos | Global (bilingüe EN/zh; material de MIT 6.006 y Yale PSYC 110) |
| algo-sensei | https://github.com/karanb192/algo-sensei | **MIT** ✅ | 281 | Markdown | Mentor de algoritmos y DSA: pistas progresivas y reconocimiento de patrones en vez de la solución. Mock interviews, code review, 5 lenguajes | Global |
| universal-diagnostic-tutor-skill | https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill | **MIT** ✅ | 234 | Markdown | Tutor *diagnosis-first* para STEM y CS: decide el próximo paso útil, verifica comprensión y construye dominio. Sin menú de modos ni comandos | Global |
| kaogong-skill | https://github.com/KeWang0622/kaogong-skill | **MIT** ✅ | 147 | Markdown | Tutor para el **examen de servicio civil chino**: aptitud, redacción, entrevista, actualidad. Declara compatibilidad con 40+ clientes de agente | APAC (China) |
| agent-skills (Learning Commons) | https://github.com/learning-commons-org/agent-skills | **Apache-2.0** ✅ | 35 | — | Skills para que un asistente produzca material docente **alineado a estándares K-12**. Cada skill empaqueta instrucciones, referencias y *guardrails* de un workflow docente | North America (foco estándares K-12 de EE. UU.) |

**Cinco de los siete son MIT o Apache-2.0 y suman 996 ★.** Son empaquetables. El problema no es la licencia del
conjunto: es que **el único que tiene cobertura curricular ancha (165 skills) es el que tiene *share-alike*.**

### La forma del segmento, y repite el patrón de los pases 8 y 9 con el signo invertido

Los pases 8 (accesibilidad) y 9 (credenciales) encontraron la misma figura: *lo maduro es copyleft, lo permisivo es
diminuto*. Esta capa la repite —`education-agent-skills` (815 ★, CC BY-SA) y `human-skill-tree` (562 ★, AGPL-3.0)
arriba; MIT abajo—, **pero con una diferencia que la vuelve la capa más accionable de la KB:** acá el costo de
construir el activo permisivo que falta no es una plataforma ni un dataset. Es **Markdown**. La biblioteca científica
de 47.2k ★ es texto estructurado, y su estructura es pública y MIT: se puede copiar la arquitectura sin copiar el
contenido.

### La nota de método del pase, y hay que dejarla escrita porque va a volver a pasar

Dos advertencias de verificación, las dos verificadas contra la fuente:

1. **Los agregadores de estrellas van atrasados, y en esta categoría el atraso es de ~2×.** Para los dos repos
   baseline, la búsqueda web devolvió cifras de terceros (ossinsight, sourcepulse) de **26.5k** y **13.7k**, mientras
   la página del repo —leída el mismo día— dice **47.2k** y **33.2k**. En una categoría que crece a +6.3k ★/mes,
   **la cifra del agregador no es una cifra vieja: es una cifra equivocada.** Regla: en esta capa, sólo vale la página
   del repo.
2. **`curl` no sirve para verificar URLs en este entorno, y un 403 no es un 404.** Se corrieron las **164 URLs de
   GitHub de toda esta KB** por `curl -sL`: **las 164 devolvieron 403**, uniformemente — es el proxy del entorno
   bloqueando `curl` hacia github.com, no *link rot*. **No hay ninguna evidencia de que esas 164 URLs estén caídas, y
   tampoco se las revalidó en este pase.** La verificación de primera mano en esta KB se hace con **WebFetch**, que
   sí resuelve. Un pase futuro que vea 403 masivos no debe interpretarlos como enlaces muertos.

### Lo que esta capa no tiene, y es el gap que abre el pase 12

**No hay una sola skill educativa con *eval* publicada.** Los siete paquetes son texto de prompt sin versionado
semántico, sin suite de regresión y sin medición de efecto pedagógico. La capa de evaluación que esta KB mapeó en el
pase 4 (MathTutorBench, UnifyingAITutorEvaluation, EduBench, EduGuardBench) **nunca se aplicó a una skill**: evalúa
tutores con backend. Es decir: la capa más barata de distribuir es también la única sin control de calidad, y las
herramientas para medirla ya existen en esta misma KB y no están conectadas. Ver el patrón **P27**.

---

## Capa de lectura oral y pronunciación — agregada en el pase 14 del 2026-10-01

Trece pasadas construyeron agente, modelado, evaluación, seguridad, telemetría, datos, accesibilidad, credenciales,
contenido, predicción, *skills* y práctica. **Todas asumieron que el alumno escribe.** En alfabetización inicial —y en
enseñanza de idiomas, que es el otro gran mercado de esta vertical— lo que se evalúa es que el alumno **hable**.

| Pieza | Repo | Licencia | ★ | Qué mide |
|---|---|---|---|---|
| **OpenPronounce** | [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | **MIT** ✅ | **85** | Fonema a fonema contra el texto esperado: puntaje 0-100, *phoneme error rate*, *word error rate*, confianza por palabra (0-1), distancia acústica por DTW, prosodia (F0 y energía). Wav2Vec2 + XLSR por idioma. **Local, sin API key ni nube** |
| **speechocean762** | [`jimbozhang/speechocean762`](https://github.com/jimbozhang/speechocean762) | ⚠️ **sin `LICENSE`** | **198** | Corpus de referencia: 5.000 oraciones, **mitad de hablantes son niños**, L1 mandarín. Exactitud, completitud, **fluidez** y prosodia en tres niveles |
| **Kaldi** | [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | **Apache-2.0** ✅ | **15.5k** | ASR genérico de grado industrial. Base de los tutores de lectura de la literatura. **No es educativo** |
| **Carrera Lectora** | [`vilcaaguilerandrea-oss/carrera-lectora`](https://github.com/vilcaaguilerandrea-oss/carrera-lectora) | 🔴 **SIN LICENCIA** | **0** | PWA chilena, 1.º-4.º básico: **PPM y exactitud** sobre 40 textos graduados, pedagogía intercultural, Web Speech API en dispositivo, sin telemetría. **No reutilizable** |

### Por qué OpenPronounce es la pieza vendible y no el corpus ni Kaldi

Tiene **85 ★** —no es tracción— pero es la única de la capa que cumple las cuatro condiciones a la vez: **licencia
permisiva** (MIT), **métrica que un docente entiende** (fonema mal pronunciado, con transcripción IPA), **ejecución
local** —que es lo que vuelve proponible un despliegue con menores de edad bajo Anexo III del EU AI Act y bajo los
estatutos de privacidad estudiantil de EE. UU.— y **cobertura multilingüe** por XLSR.

**El posicionamiento comercial es explícito en el propio repo: es la alternativa autoalojada a Azure Pronunciation
Assessment.** Eso es exactamente el tipo de sustitución que esta vertical sabe vender: el incumbente es un servicio
de nube por uso, y el reemplazo es un componente MIT que corre en la infraestructura del cliente.

### 🔴 Lo que esta capa no tiene, y es el gap que abre el pase 14

**Ningún agente de los 31 de la tabla principal tiene entrada ni salida de voz.** Se verificó contra la tabla: ni
DeepTutor, ni Educhain, ni OpenTutor, ni OpenTutorAI-CE, ni Bloom. **La capa de habla y la capa de agente no se
tocan** — y tampoco hay ningún servidor MCP que exponga evaluación de pronunciación, aunque el patrón MCP ya está
probado en esta KB (ver `bncc-mcp`, abajo, del mismo pase). Es el gap 24.

**Y para español y portugués no hay nada utilizable.** `carrera-lectora` es pedagógicamente lo más fino de la región
—y no tiene licencia—; el corpus de referencia es inglés con L1 mandarín. **~600 millones de hablantes sin pieza
permisiva de evaluación de fluidez.**

---

## Capa de puente agente↔currículo nacional — agregada en el pase 14 del 2026-10-01

El gap 15 (pase 10) decía que *«ningún puente agente↔contenido curricular tiene tracción, y el único que existe
declara mal la licencia de lo que sirve»*. **Este pase encuentra el puente que faltaba, es MIT, y es de LATAM.**

| Pieza | Repo | Licencia | ★ | Qué expone |
|---|---|---|---|---|
| **bncc-mcp** | [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) | **MIT** ✅ | **14** | Servidor **MCP** de la BNCC brasileña, cinco herramientas: `bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_mapa_de_foco`, `bncc_estatisticas`. **1.717 habilidades** (1.408 Fundamental, 104 Infantil, 205 Médio), 141 de Computação por ejes, y **396 habilidades priorizadas por el Mapa de Foco del Instituto Reúna** con capa pedagógica |
| **curriculum-bncc** | [`aprincar/curriculum-bncc`](https://github.com/aprincar/curriculum-bncc) | ⚠️ **AGPL-3.0** | **0** | *Crosswalk* de IDs propios a referencias BNCC con cuatro relaciones: `direct`, `partial`, `supports`, `prerequisite`, validado contra catálogos versionados |

**Lo que hace valioso a `bncc-mcp` no es el currículo: es el Mapa de Foco.** Exponer 1.717 habilidades por MCP es
un trabajo de ingeniería; exponer **cuáles 396 son prioritarias y con qué capa pedagógica** es un **juicio curricular
de una institución** (Instituto Reúna). Eso es la clase de activo que un cliente no puede generar solo y que ningún
modelo puede inventar sin alucinar. **Con 14 ★ no es tracción — es la pieza que faltaba, y está en la región de origen
de Globant.**

⚠️ **`curriculum-bncc` es AGPL-3.0 y tiene 0 ★:** sirve como referencia de **cómo modelar** un *crosswalk* (los cuatro
tipos de relación son el diseño correcto), **no como dependencia** de un producto comercial.

---

## Capa de autoría y procedencia — agregada en el pase 15 del 2026-10-01

La KB tenía media capa de integridad académica desde el pase 8: **proctoring, y registrado como roadmap**. Esta es
la otra mitad —**cómo se prueba quién escribió el trabajo**— y es la pregunta que todo cliente hace primero.
Son tres familias de herramienta. **Las tres son permisivas. Sólo dos sirven.**

### Familia 1 — marcado en el origen (*watermarking*): es lo que cumple el Artículo 50, y la KB lo vendía sin tenerlo

| Pieza | Repo | Licencia | ★ | Qué hace |
|---|---|---|---|---|
| **SynthID-Text** | `huggingface/transformers` → `src/transformers/generation/watermarking.py` | **Apache-2.0** ✅ | viaja en Transformers | Marcado **y** detección en el mismo paquete. Clases verificadas en el archivo: `SynthIDTextWatermarkLogitsProcessor`, `SynthIDTextWatermarkDetector`, `BayesianDetectorModel`, `BayesianDetectorConfig`, `BayesianDetectorWatermarkedLikelihood`. Copyright **HuggingFace + Google DeepMind** |
| **MarkLLM** | [`THU-BPM/MarkLLM`](https://github.com/THU-BPM/MarkLLM) | **Apache-2.0** ✅ | **1.100** | **23+ algoritmos** de watermarking y **12 herramientas de evaluación** (detectabilidad, robustez, impacto en calidad del texto). EMNLP 2024 Demo. 95 forks, 185 commits |

**Cuál usar y por qué.** **SynthID-Text** es el de producción: no agrega un proveedor, agrega un
`WatermarkingConfig` a la llamada de generación que el proyecto ya hace. **MarkLLM** es la herramienta de
**evaluación y comparación** — es con lo que se demuestra, en un expediente de conformidad, que el marcado
elegido es *«effective, interoperable, robust and reliable»* como pide el Artículo 50(2). Se usan los dos:
uno marca, el otro prueba que el marcado aguanta.

### Familia 2 — procedencia del artefacto (C2PA): el estándar que el Code of Practice europeo canonizó

| Pieza | Repo | Licencia | ★ | Commits | Qué hace |
|---|---|---|---|---|---|
| **c2pa-rs** | [`contentauth/c2pa-rs`](https://github.com/contentauth/c2pa-rs) | **MIT *y* Apache-2.0** (dual) ✅ | **424** | **1.907** | SDK Rust del core C2PA: crear, firmar, validar e incrustar manifiestos de procedencia. Claims **C2PA v2**, spec **2.4**, *CAWG identity assertion*, API en C |
| **c2pa-python** | [`contentauth/c2pa-python`](https://github.com/contentauth/c2pa-python) | **Apache-2.0 *y* MIT** (dual) ✅ | 105 | 344 | Binding Python, **3.10+**. Es la vía realista para un pipeline educativo que ya es Python |

**Por qué esto no es opcional en EMEA.** El **Code of Practice** europeo sobre marcado y etiquetado de contenido
generado por AI —voluntario, pero la vía más clara para demostrar cumplimiento del Artículo 50— **adopta las
*Content Credentials* de C2PA como estándar técnico de facto** del metadato incrustado, en un esquema **por
capas: metadato + watermarking**, con *fingerprinting* y *logging* como medidas de apoyo. Las familias 1 y 2 **no
son alternativas: son las dos capas del mismo esquema.**

### Familia 3 — detección forense: real, permisiva, publicada en ICLR/ICML/ACL, y no se puede usar para acusar

| Repo | Licencia | ★ | Qué es |
|---|---|---|---|
| [`baoguangsheng/fast-detect-gpt`](https://github.com/baoguangsheng/fast-detect-gpt) | **MIT** ✅ | **434** | **ICLR 2024**. Zero-shot por curvatura de probabilidad condicional, **340× más rápido que DetectGPT**. AUROC **0,9887** (5 modelos) / **0,9338** (ChatGPT/GPT-4) |
| [`ahans30/Binoculars`](https://github.com/ahans30/Binoculars) | **BSD-3-Clause** ✅ | **420** | **ICML 2024**. Zero-shot sin datos de entrenamiento; dos modelos de pesos abiertos en inferencia |
| [`liamdugan/raid`](https://github.com/liamdugan/raid) | **MIT** ✅ | **216** | **ACL 2024**. El benchmark: **10M+ documentos**, 11 LLMs, 11 dominios, 4 decodificaciones, **12 ataques adversarios**. Leaderboard `raid-bench.xyz` |
| [`NLP2CT/LLM-generated-Text-Detection`](https://github.com/NLP2CT/LLM-generated-Text-Detection) | **MIT** ✅ | **252** | Survey vivo, ~100+ papers y 17+ datasets. *Computational Linguistics* **51(1), 2025** |
| [`pablocaeg/sloptotal`](https://github.com/pablocaeg/sloptotal) | **MIT** ✅ | 39 | Ensamble de **23 motores** auto-hospedado que **corre en CPU** (incluye Fast-DetectGPT y Binoculars). Acepta texto, PDF, DOCX y URLs |
| [`Lendarixon/awesome-ai-detection`](https://github.com/Lendarixon/awesome-ai-detection) | **CC0-1.0** ✅ | 0 | Catálogo con los **modos de falla medidos** |
| [`yonatanlop/detectoria`](https://github.com/yonatanlop/detectoria) | 🚫 **Sin licencia** | 0 | El único detector pensado para **español**: estilometría + perplejidad con `mrm8488/spanish-gpt2` + rank/entropía estilo GLTR + traducción `Helsinki-NLP/opus-mt-es-en` con `roberta-base-openai-detector`. **No proponerlo** |

### 🔴 Antes de poner cualquier cosa de la familia 3 en un entregable

| Medición | Valor |
|---|---|
| FPR sobre escritura de **no nativos de inglés** (TOEFL, 7 detectores) | **61,3 %** |
| FPR sobre universitarios **nativos**, mismos detectores | ~2,9 % |
| FPR sobre 1.180 abstracts académicos **anteriores a 2018** | **5,85 %** + 20 % «incierto» |
| Umbral de longitud por debajo del cual el score no sirve | **~80 palabras**; estabiliza en ~200 |
| Efecto de la paráfrasis | **caídas grandes de exactitud** (RAID) |

**Binoculars lo dice en su propio README:** *«more proficient in detecting English language text compared to other
languages»*, *«for academic purposes only»*, con **supervisión humana** requerida.

**La regla, y vale para toda la KB:** un score de detección es **evidencia, no prueba**. Sirve para **priorizar una
conversación docente**; nunca para disparar una sanción automática. Sobre alumnos que escriben inglés como segunda
lengua —el alumno modal de LATAM, de EMEA no anglófona y de buena parte de APAC— el **61,3 %** convierte la
herramienta en **pasivo legal antes que en producto**. Vanderbilt lo resolvió con una cuenta: 1 % de FPR sobre
75.000 trabajos son **~750 acusaciones injustas por año**, y desactivó el detector. **Más de 50 universidades**
de EE. UU., Reino Unido, Canadá, Australia y Sudáfrica hicieron lo mismo. Ver el **gap 25**.

### La pieza que cambia la arquitectura, y es una pregunta distinta

*«¿Esto lo escribió una AI?»* no tiene respuesta confiable y no la va a tener. *«¿Esto lo escribió **nuestro**
tutor?»* **sí la tiene**, y es una verificación criptográfica, no una estimación. **La institución que provee el
agente puede marcar su salida en el origen.** Eso saca la integridad del terreno forense y la mete en el terreno
de la procedencia, donde el stack es Apache-2.0 y está maduro. Es el patrón **P33**, y es la misma forma que la
tendencia 29 describe para otras cinco capas de esta KB.

⚠️ **Y el límite honesto del marcado:** sólo cubre texto que generó **tu propio sistema**. No resuelve el ensayo
escrito con un modelo de fuera de la institución. Lo que hace es convertir un problema sin solución —detección
universal— en uno con solución parcial pero **cierta**, más un régimen de **declaración** para el resto. En LATAM
ese régimen **ya es la norma legal** (ver `intel/market.md`), y por eso ahí el stack alcanza hoy.

### El puente que no existe, y es el gap barato de este pase

**Ninguna de las nueve piezas de arriba tiene integración educativa.** No hay plugin de LMS, herramienta LTI ni
servidor MCP que marque o verifique la salida de un tutor. Lo que existe en el directorio de Moodle son
**envoltorios de servicios propietarios**: Compilatio (plugin **GPL-3.0**, 821 instalaciones, release 2026-06-25),
Originality.ai (Moodle 3.9–5.0, release 2026-07-02) y Copyleaks — plugin libre, **detector pago**. El puente es
trabajo de días sobre infraestructura Apache-2.0. Ver **P33** y el **gap 25**.


## Postura de privacidad de los agentes — agregada en el pase 16 del 2026-10-01

Se revisó la tabla principal agente por agente buscando una declaración de **qué hace con el dato del alumno**:
dónde lo guarda, si lo usa para entrenar, si se puede desplegar sin que el dato salga de la institución.

**Ninguno de los 31 la tiene.** No es que declaren una política mala — no declaran ninguna. Lo más cercano es la
capa de memoria (DeepTutor tiene memoria en tres capas, `learnmcp-xapi` persiste contra un LRS), que describe
**dónde** queda el dato pero nunca **bajo qué base legal** ni con qué retención.

**Por qué importa ahora y no antes:**

| Régimen | Qué exige | Estado |
|---|---|---|
| **COPPA enmendada** (North America) | Biométricos —**voiceprints**, faceprints, huellas— son información personal; consentimiento parental verificable; política escrita de retención y borrado; prohibida la retención indefinida | 🔴 **Cumplimiento exigible desde 2026-04-22** |
| **FERPA** (North America) | El dato cedido al proveedor sólo sirve para el fin cedido; **entrenar modelos comerciales generales con él es violación** | Vigente |
| **GDPR Art. 35** (EMEA) | **DPIA obligatorio** antes de usar la herramienta; EDPB pide *balancing test* documentado | Vigente |
| **DPDP Act § 9** (APAC, India) | Consentimiento parental verificable; sin seguimiento conductual; hasta **₹200 crore** por infracción con datos de menores | Vigente |
| **LGPD Art. 14 + ECA Digital** (LATAM, Brasil) | Consentimiento específico y destacado de un responsable; informes semestrales de impacto a la ANPD para plataformas con +1M de usuarios menores | Vigente |

**La consecuencia práctica, y es un criterio de selección nuevo para esta KB:** cuando un agente de la tabla se
proponga para menores, la postura de privacidad **hay que construirla en el proyecto** — no viene con el repo. El
presupuesto de un despliegue educativo con datos reales incluye esa capa, y hasta este pase esta KB la daba por
gratis. Las piezas están en `repos/foundations.md` y el wiring en **P34** y **P35**.

## Capa de borrado efectivo — agregada en el pase 18 del 2026-10-01

El **gap 29** (pase 17) pedía una pieza concreta: *«ningún `privacy provider` de referencia para un plugin de AI,
que es justamente lo que el núcleo de Moodle exige de cualquier plugin que guarde dato del alumno»*. **Existe, y no
la escribió un tercero: la escribió Moodle.** El núcleo trae **tres** implementaciones de referencia, una por cada
proveedor de AI que embute. El gap se cierra, y se cierra con la pieza más defendible posible ante un cliente: la
del propio vendor.

### 🔴 El hallazgo del pase: la referencia estaba en el núcleo, y el pase 17 no la vio por una razón mecánica

El pase 17 dejó escrito que intentó el árbol de `admin/tool/dataprivacy` dentro de `moodle/moodle` *«por cuatro
rutas (`main` y `master`, árbol y archivo) y las cuatro dieron 404»*, y por eso registró el Privacy API como
**documentado por snippet, no verificado de primera mano**. La causa es trivial y conviene dejarla escrita porque
afecta a cualquier pase futuro:

> 🔴 **[FALSO — refutado en el pase 19, ver abajo]** **`moodle/moodle` no tiene rama `main` ni rama `master`.** Sus ramas son `MOODLE_XXX_STABLE`. Cualquier fetch
> contra `main` o `master` da 404 **con independencia de que el archivo exista**. Los cuatro 404 del pase 17 no
> midieron ausencia: midieron el nombre de la rama.

Verificado en este pase por código HTTP contra `raw.githubusercontent.com`, rama por rama:

| Ruta en `moodle/moodle` | `main` | `master` | `MOODLE_405_STABLE` | `MOODLE_500_STABLE` |
|---|---|---|---|---|
| `ai/provider/openai/version.php` | 404 | 404 | **200** | **200** |
| `ai/provider/openai/classes/privacy/provider.php` | 404 | 404 | **200** | **200** |
| `admin/tool/dataprivacy/version.php` | — | — | — | **200** |
| `admin/tool/policy/version.php` | — | — | — | **200** |

**Entonces se corrige el registro de evidencia del pase 17:** el Privacy API, `tool_dataprivacy` y `tool_policy`
pasan de *«documentados por snippet»* a **verificados de primera mano en el núcleo**.


### 🔴 CORRECCIÓN DEL PASE 19 (2026-10-01) — la rama existe, y la causa real es mejor que la que se escribió

**Lo de arriba es falso en su premisa y hay que leerlo con esta corrección puesta.** Verificado con `git ls-remote`
—que lista refs, no adivina— y después con un clon *sparse* del árbol real:

```
$ git ls-remote --heads https://github.com/moodle/moodle | grep -v 'MOODLE_[0-9]*_STABLE$'
85af0b5dc354bf03c73db60079c232f004e01433    refs/heads/main
```

> **`moodle/moodle` SÍ tiene rama `main`,** y apunta a `85af0b5` = **Moodle 5.3rc1**. Lo que no tiene es `master`.

**Y la causa real de los 404 es más útil que la falsa, porque se repite:** **Moodle movió su *webroot* al
subdirectorio `public/` en la serie 5.x.** En `main` no existe `ai/` en la raíz; existe `public/ai/`. Por eso
`ai/provider/openai/version.php` da 404 en `main` **y** 200 en `MOODLE_405_STABLE` y `MOODLE_500_STABLE`: en esas
ramas `ai/` todavía estaba en la raíz. **La tabla de evidencia del pase 18 es correcta; su explicación no.** Los 404
midieron **la ruta**, no el nombre de la rama — y cualquier referencia a rutas de Moodle que esta KB escriba tiene
que decir contra qué serie se resolvió, porque la 5.x las movió todas.

**Lo que hay que corregir del conteo y de la lista:**

| Lo que escribió el pase 18 | Lo verificado en el pase 19 (clon sparse de `main` = 5.3rc1) |
|---|---|
| «El núcleo trae **tres** implementaciones» | **Siete** proveedores con `privacy/provider.php`, más **1** del subsistema (`core_ai`) y **2** de *placement* = **10 archivos** |
| `ai/provider/bedrock` → «404, no está en el núcleo» | **Sí está**, y el nombre es `awsbedrock`, no `bedrock`. El 404 midió el nombre |
| `ai/provider/anthropic` → «404, no está en el núcleo» | **Sí está**: `public/ai/provider/anthropic/classes/privacy/provider.php` |

Los siete, auditados uno por uno sobre el fuente:

| Proveedor (`public/ai/provider/…`) | Líneas | `delete_records` / `DELETE FROM` / `add_database_table` | `add_external_location_link` |
|---|---|---|---|
| `anthropic` | 78 | **0** | 1 |
| `awsbedrock` | 76 | **0** | 1 |
| `azureai` | 77 | **0** | 1 |
| `deepseek` | 70 | **0** | 1 |
| `gemini` | 77 | **0** | 1 |
| `ollama` | 74 | **0** | 1 |
| `openai` | 76 | **0** | 1 |

**Lo que el pase 18 sí acertó, y conviene no perderlo en la corrección:** su lectura de que los métodos vacíos son
*«vacíos a propósito»* y que ésa es la forma correcta para un plugin que sólo transmite **es exacta**, y la
verificación de este pase la confirma (los siete, idénticos, con `@codeCoverageIgnore`). Lo que estaba mal es el
titular: **siete shims de declaración no son «implementaciones de referencia» de un `privacy provider`**, porque lo
que un plugin que guarda dato necesita copiar es precisamente lo que ellos no tienen.

### ✅ La plantilla real, que el pase 18 no nombró: `core_ai`

`public/ai/classes/privacy/provider.php` — **~800 líneas**, y es el artefacto que el **gap 29** pedía:

- **6 tablas declaradas** en `get_metadata()`: `ai_policy_register`, `ai_action_register`,
  `ai_action_generate_image`, `ai_action_generate_text`, `ai_action_summarise_text`, `ai_action_explain_text`.
  Entre sus campos están **`prompt`**, **`generatedcontent`**, `responseid`, `fingerprint`, `prompttokens`,
  `completiontokens`, `model` y `courseid`.
- `get_contexts_for_userid()` con **SQL real** (5 consultas, una por tipo de acción), no un `contextlist` vacío.
- `export_user_data()` que escribe de verdad vía `writer::with_context()`.
- **Borrado real** en las tres variantes: `delete_data_for_user()` (:496), `delete_data_for_users()` (:695) y
  `delete_data_for_all_users_in_context()` (:378), con `delete_records_list()`.

**Eso es lo que hay que copiar en un plugin de AI que guarde dato del alumno** (ver **P39**, que mejora con esto), y
lo que hay que citar ante un cliente cuando pregunte si Moodle sabe borrar lo que su AI generó. Los dos *placement*
(`courseassist`, `editor`) son `null_provider`: declaran explícitamente que no guardan nada.

**El hallazgo de encuadre, que es el que viaja a `intel/trends.md`:** la línea divisoria dentro del propio núcleo de
Moodle no es técnica, es de **arquitectura de dato**. `core_ai` guarda el prompt y la respuesta y por eso sabe
borrarlos. Los siete proveedores **no guardan: transmiten** — y lo único que pueden hacer es declararlo. El núcleo
documenta así, en siete archivos idénticos, **el punto exacto donde su maquinaria de supresión se queda sin nada que
suprimir**, porque el dato ya está en OpenAI, Anthropic, Google, AWS, Azure, DeepSeek o en el Ollama de alguien. Ver
la tendencia **48**.

### ~~Las tres referencias del núcleo~~ — ⚠️ SUPERADA POR EL PASE 19: son siete, y ninguna de las siete es la plantilla (se conserva por la cadena de idioma de `ollama`, que sigue siendo válida y citable)

Verificadas leyendo el archivo fuente, no la página del repo. Las tres implementan las mismas tres interfaces
—`metadata\provider`, `request\core_userlist_provider`, `request\plugin\provider`— con `#[\Override]`, copyright
**2024 Matt Porritt (moodle.com)**, licencia **GPL-3.0-or-later**:

| Proveedor en el núcleo | ¿Trae `privacy/provider.php`? | Qué declara `get_metadata()` |
|---|---|---|
| `ai/provider/openai` | ✅ **200** | `add_external_location_link` con `prompttext`, `model`, `numberimages`, `responseformat` |
| `ai/provider/azureai` | ✅ **200** | ídem patrón |
| `ai/provider/ollama` | ✅ **200** | `add_external_location_link` con `prompttext`, `model` |
| `ai/provider/bedrock` | 🚫 **404** — no está en el núcleo | — |
| `ai/provider/anthropic` | 🚫 **404** — no está en el núcleo | — |

**El patrón canónico, y es contraintuitivo:** los seis métodos de export y borrado están **vacíos a propósito**, y
`get_contexts_for_userid()` devuelve un `contextlist` vacío. No es código sin terminar. Es la forma correcta para un
plugin que **no guarda nada localmente y sólo transmite**: lo único que tiene que declarar es el envío externo. Un
plugin de AI que *sí* guarde —un log de uso, una nota, una conversación— **no puede copiar esta forma**: tiene que
implementar los seis.

### 🔴 La línea que hay que leer antes de poner cualquiera de las tres en un expediente de privacidad

`aiprovider_ollama` es el caso que importa, porque es el que un cliente elige **justamente** para que el dato no
salga. Y aun así el núcleo le declara un envío externo. La cadena de idioma, citada literal:

> `privacy:metadata` → «The Ollama API provider plugin does not store any personal data.»
>
> `privacy:metadata:aiprovider_ollama:externalpurpose` → «This information is sent to the Ollama API in order for a
> response to be generated. Your Ollama account settings may change how Ollama stores and retains this data. **No
> user data is explicitly sent** to Ollama or stored in Moodle LMS by this plugin.»

**La palabra que carga el peso es «explicitly».** El plugin no adjunta identidad —no manda `userid`, ni nombre, ni
email— y en ese sentido la frase es verdadera. Pero `prompttext` **sí** se declara como lo que viaja, y el prompt
lleva lo que el alumno escribió, que puede ser cualquier cosa. **La declaración del núcleo es exacta sobre la
identidad y silenciosa sobre el contenido.** En un expediente de privacidad (ver **P35**) esa distinción se escribe
en una línea y evita la discusión entera: *«el plugin no envía identificadores; el cuerpo del prompt no está
acotado por el plugin y su contenido es responsabilidad de la actividad que lo construye»*.

### Lo que la comunidad construyó arriba, y sólo tres piezas de seis tienen `privacy/provider.php`

Verificado abriendo `classes/privacy/` en cada repo. Ordenado por completitud de la implementación, no por estrellas.

| Pieza | Repo | Licencia | ★ | Interfaces en `privacy/provider.php` | Región del autor | Nota |
|---|---|---|---|---|---|---|
| **local_aihub** | https://github.com/jeanlucio/moodle-local_aihub | **GPL-3.0** ⚠️ | 0 (1 fork, 60 commits) | **Cuatro** — `metadata\provider`, `core_userlist_provider`, `plugin\provider` y **`user_preference_provider`** | **LATAM** — Jean Lúcio, **Instituto Federal do Sertão Pernambucano, Brasil** | **La implementación más completa de la capa, y es la única que declara las tres cosas a la vez:** tabla de base (`local_aihub_log`, 9 columnas), **6 preferencias de usuario** y **4 enlaces externos** (`deepseek`, `google_gemini`, `groq`, `openai_compatible`). Broker BYOK con *SSRF guard*, escalera de proveedores y *key store*; «the hub never contacts a provider on its own»; la API key es opcional y el plugin instala y funciona sin ninguna. Trae `.github/workflows/`, `tests/` y `docs/` |
| **aiprovider_gemini** | https://github.com/Universita-di-Ferrara/moodle-aiprovider_gemini | **GPL-3.0** ⚠️ | 3 (3 forks, 12 commits) | Tres — las mismas del núcleo | **EMEA** — Andrea Bertelli, **Università di Ferrara, Italia** | Moodle **4.5+**; v2.2.0 agrega Gemini 3 e imagen nativa. **Es una adaptación casi literal del `provider.php` del núcleo**: mismos cuatro campos (`prompttext`, `model`, `numberimages`, `responseformat`), misma estructura, y el docblock **todavía dice «Privacy provider implementation for OpenAI provider»**. No es una crítica: es la prueba de que el patrón del núcleo es el que la comunidad copia, y de que copiarlo funciona |
| **mod_aigradedassign** | https://github.com/alvarogregori/moodle-ai-graded-assignment | 🚫 **sin archivo `LICENSE`** — el header del fuente dice GPL-3.0-or-later | 0 (0 forks, 14 commits) | Tres — `metadata\provider`, `plugin\provider`, `core_userlist_provider` (`final class`) | No declarada en el perfil | Actividad de entrega en texto plano con feedback automático (Mistral, OpenAI, Anthropic, endpoints compatibles, y un *mock* determinista local). **Es el único de la capa que corre sobre dato de alumno de verdad** y lo declara: con proveedor remoto salen «the student submission, activity instructions, private rubric, and private evaluated examples». Gate de validación docente: el resultado de la AI **no afecta nota ni compleción hasta que un tutor aprueba o edita** — el diseño de **P18**. ⚠️ **Tercer caso de licencia de esta KB:** no está en el sidebar ni en el README, sólo en el header del archivo. Ver la advertencia de método abajo |
| **ai-moodle-security** | https://github.com/sngdtechnologies/ai-moodle-security | **BSD-2-Clause** ✅ | 0 (0 forks, 103 commits) | 🚫 **No tiene `classes/privacy/`** | No declarada (autor: SOB NGHAMI Gilles Descartes; prototipo de tesis de maestría) | **La única licencia permisiva de la capa, y la única pieza sin privacy provider.** No es un plugin: es una **arquitectura de despliegue** — Phi-3-mini vía Ollama 100% on-site, 7 contenedores, 5 redes Docker, sólo el proxy expuesto (443), Moodle y Ollama en redes internas **sin egreso a internet**, Caddy + WAF Coraza (OWASP CRS). Vale por el diagrama de red, no por el código |
| **tool_aiconnect** | https://github.com/marcusgreen/moodle-tool_aiconnect | 🚫 licencia no mostrada | 10 (4 forks, 37 commits) | 🚫 No se vio directorio `privacy/` | **EMEA** — nota de consultoría a **Catalyst EU** (Moodle Partner) | Fork de `local_ai_connector` para múltiples proveedores LLM incluido Ollama; quita generación de imagen; se integra con `moodle-qtype_aitext` |
| **tool_dataprivacy** (el repo) | https://github.com/moodlehq/moodle-tool_dataprivacy | **GPL-3.0** ⚠️ | 8 (11 forks, 199 commits) | — (es la máquina, no un plugin de AI) | EMEA — `moodlehq` | 🔴 **ARCHIVADO el 2020-09-24, read-only.** No está muerto: **se mudó al núcleo**. Moodle 3.3.8 / 3.4.5 / 3.5 y posteriores ya lo traen de fábrica, y por eso `admin/tool/dataprivacy/version.php` da 200 en `MOODLE_500_STABLE`. **No proponer este repo como dependencia** — proponer la versión del núcleo |

### ⚠️ Advertencia de método — el tercer lugar donde puede estar la licencia

Esta KB ya aprendió dos veces que la licencia no se lee donde parece. El pase 10 pasó del README al archivo
`LICENSE`; el pase 16 encontró dos casos (`diffprivlib`, `SDV`) donde el sidebar de GitHub no alcanzaba.
`mod_aigradedassign` agrega el tercero: **no hay `LICENSE`, no hay licencia en el sidebar, no hay nota en el
README — y el header de cada archivo `.php` declara GPL-3.0-or-later.** Para un plugin de Moodle eso es lo
esperable (el núcleo lo exige), pero **un header de archivo no es una concesión de licencia del repositorio**.
Regla operativa: **si no hay `LICENSE`, se trata como sin licencia a efectos de cotización**, y lo que corresponde
es abrir un *issue* pidiendo el archivo. Es el mismo movimiento de dos líneas que el pase 13 recomendó para el
gap 20.

### ⚠️ Y la nota de diseño sobre `local_aihub`, porque es la pieza que esta KB va a recomendar

El provider declara **6 preferencias de usuario** que incluyen las claves BYOK (`local_aihub_deepseek_key`,
`local_aihub_gemini_key`, `local_aihub_groq_key`, `local_aihub_openai_key`) vía `add_user_preference`. Declararlas
es **lo correcto** —son dato personal del usuario y el Privacy API las tiene que conocer—, pero tiene una
consecuencia que conviene prever: **un pedido de exportación de datos devuelve al usuario sus propias claves de
API en el export**. No es una vulnerabilidad y el diseño es honesto; es una consideración de manejo del artefacto
de export, que en un despliegue institucional circula por correo o por descarga. Se anota, no se descuenta.

---

## Capa de *unlearning* — agregada en el pase 18 del 2026-10-01

El **gap 30** (pase 17) dejó una acción textual: *«buscar procedencia de dato de entrenamiento por los términos del
dominio de ML, no de educación… **`machine unlearning` es el término que este pase no buscó** y es el que podría
tener oferta madura»*. Se buscó. **La predicción era correcta: la oferta existe, es madura y es toda permisiva.**

Y produce el contraste más limpio de esta KB. El pase 17 midió que la máquina para **borrar el registro** del
alumno está instalada en el LMS y es **toda copyleft**. Esta capa borra la otra mitad —**la influencia del dato
sobre el modelo**— y es **toda MIT o Apache-2.0**. Las dos mitades del derecho al olvido tienen licencias
opuestas, y la permisiva es la que la educación no usa.

### Lo horizontal: real, permisivo, publicado y con tracción

| Pieza | Repo | Licencia | ★ | Qué es |
|---|---|---|---|---|
| **awesome-machine-unlearning** | https://github.com/tamlhp/awesome-machine-unlearning | **MIT** ✅ | 970 (79 forks) | El mapa de la capa: artículos, metodologías y **datasets**. Respalda la survey *«A Survey of Machine Unlearning»*, **ACM TIST 2025**, DOI `10.1145/3749987` (arXiv 2209.02299). Es el punto de entrada |
| **machine_unlearning** | https://github.com/jjbrophy47/machine_unlearning | 🚫 **sin licencia declarada** | 965 (117 forks) | Literatura existente sobre *unlearning*, de pre-2017 a 2025 (AAAI, ACL, CVPR, NeurIPS). Segundo agregador por tamaño. **No muestra licencia** → bibliografía sí, dependencia no |
| **awesome-llm-unlearning** | https://github.com/chrisliu298/awesome-llm-unlearning | **Apache-2.0** ✅ | 627 (33 forks) | 616 papers, 18 surveys, 3 frameworks. Es el recorte de LLM |
| **open-unlearning** | https://github.com/locuslab/open-unlearning | **MIT** ✅ | **607** (164 forks, 90 commits, Python) | **El framework ejecutable de la capa.** Benchmarks **TOFU, MUSE, WMDP**; métodos `GradAscent`, `GradDiff`, `NPO`, `SimNPO`, `DPO`, `RMU`, `UNDIAL`, `AltPO`, `SatImp`, `WGA`, `CE-U`, `PDU`; 5+ datasets, 10+ métricas, 7+ arquitecturas. Reporte técnico arXiv **2506.12618** |
| **Unlearn-Saliency (SalUn)** | https://github.com/OPTML-Group/Unlearn-Saliency | **MIT** ✅ | 154 (29 forks) | *Weight saliency* por gradiente para *unlearning*, en clasificación **y** generación (difusión, Stable Diffusion). **ICLR 2024 Spotlight**, arXiv 2310.12508. Es el método con mejor relación resultado/costo publicado |
| **torchunlearn** | https://github.com/Harry24k/machine-unlearning-pytorch | **MIT** ✅ | 12 (2 forks, 51 commits) | *«A PyTorch library for efficient machine unlearning — make your models forget, on demand.»* Interfaz unificada estilo PyTorch sobre algoritmos del estado del arte. **NeurIPS 2025**, *«Unlearning-Aware Minimization»* (Kim et al.). **Es la pieza de esta tabla que alcanza a un modelo de *knowledge tracing*** — ver abajo |
| **model-provenance-kit** | https://github.com/cisco-ai-defense/model-provenance-kit | **Apache-2.0** ✅ | 104 (22 forks) | **Cisco AI Defense.** Toolkit y CLI en Python que determina si dos modelos comparten origen: metadatos de arquitectura, estructura del tokenizer y *fingerprints* a nivel de pesos, **8 señales agregadas en un score**. Modos `compare` (par a par) y `scan` contra una base de ~**150 modelos base de 45+ familias**. *Streaming* para modelos de +20 GB |
| **Data-Provenance-Collection** | https://github.com/Data-Provenance-Initiative/Data-Provenance-Collection | **Apache-2.0** ✅ | 281 (48 forks) | Auditoría de **44 colecciones / 1800+ datasets** de *finetuning* con metadatos de fuente, licencia y creador; genera **fichas de procedencia legibles**. arXiv 2310.16787 |

🔴 **Y una trampa de verificación que este pase casi escribe mal.** La primera búsqueda devolvió
`aflah02/open-unlearning` como el repo de la librería. **Es un fork con 0 ★ y 0 forks**; el canónico es
`locuslab/open-unlearning` con **607 ★**. Un buscador devuelve el fork y el fork se ve idéntico al original: mismo
README, misma licencia, misma lista de métodos. **Lo único que lo delata es el campo «forked from» y el contador
de estrellas en cero.** Es la misma clase de error que el pase 7 cometió con MRBench y el pase 12 con la
distribución por *skills*. Regla: **ningún repo entra a una tabla de esta KB sin mirar si es fork.**

### 🔴 El hallazgo del pase: el algoritmo que la educación necesita existe, es exactamente de su capa de *mastery*, y no publica código

Buscando *unlearning* contra educación aparece **PrivacyCD** — *«PrivacyCD: Hierarchical Unlearning for Protecting
Student Privacy in Cognitive Diagnosis»*, **arXiv 2511.03966**. Y no es un paper tangencial:

- Se declara **el primer estudio sistemático del problema de *data unlearning* para modelos de *cognitive
  diagnosis***, y los modelos de CD son **la misma capa de estimación de dominio** que esta KB viene documentando
  desde el pase 4 con `pyBKT` y `pyKT`.
- El argumento de partida es exactamente el que esta KB necesitaba verificar: *«aplicar directamente algoritmos de
  *unlearning* de propósito general es subóptimo, porque no logran balancear completitud del olvido, utilidad del
  modelo y eficiencia frente a la estructura heterogénea de los modelos de CD»*.
- Aporta **HIF** (*hierarchical importance-guided forgetting*): la importancia de los parámetros en modelos de CD
  tiene características **por capa**, y un mecanismo de suavizado combina importancia individual y de capa para
  distinguir mejor los parámetros asociados al dato a olvidar. Evaluado en **tres datasets reales**.
- Autores: Mingliang Hou, Yinuo Wang, Teng Guo, Zitao Liu, Wenzhou Dou, Jiaqi Zheng, Renqiang Luo, Mi Tian,
  Weiqi Luo.

**No se ubicó repositorio público.** Se buscó explícitamente por el nombre del método y del paper. Es el patrón
que esta KB ya nombró en la capa predictiva (pase 11) y en la de contenido (pase 10): **la pieza más específica y
más valiosa es la que no publica código.**

Hay más literatura en la misma dirección, y conviene registrarla como señal de que la categoría se está formando:
*«Making AI Forget You: Removing Educational Data from Intelligent Education Models»* (capítulo Springer, DOI
`10.1007/978-981-95-1525-7_8`), *«Exploring Fairness in Educational Data Mining in the Context of the Right to be
Forgotten»* (arXiv 2405.16798), *«Trustworthy Intelligent Education: A Systematic Perspective»* (arXiv 2601.21837)
y *«Lifting Data-Tracing Machine Unlearning to Knowledge»* (OpenReview `ScvUCNMdYN`).

⚠️ **Nivel de evidencia:** `arxiv.org` está **bloqueado por el proxy de egreso de esta sesión** (mismo bloqueo que
el gap 17; también cayeron `blogs.cisco.com` y `helpnetsecurity.com`). Los metadatos de estos papers vienen de
**snippets de búsqueda concordantes, no de la fuente primaria**. Los repos de la tabla de arriba **sí** se
verificaron de primera mano, incluida la condición de fork y la ausencia de licencia donde se declara.
No citar un número de paper en material de cliente sin abrir el PDF.

### La conclusión de ingeniería, y es la que decide qué se puede prometer

Esta KB tiene dos estimadores de *mastery* en su tabla de fundacionales, y **el *unlearning* los alcanza de forma
distinta**:

- **`pyKT` (MIT) es PyTorch.** Entonces `torchunlearn` y `SalUn` son **aplicables en principio**: hay una interfaz
  y un conjunto de pesos sobre los cuales operar. Es integración con riesgo técnico, no investigación.
- **`pyBKT` (MIT) no es un modelo PyTorch** — es BKT ajustado por EM. **Ninguna librería de esta tabla lo
  alcanza**, y la respuesta honesta para `pyBKT` **no es *unlearning*: es reajustar desde cero sin el alumno**.
  Para BKT eso es barato —pocos parámetros, EM sobre la secuencia— y además es *exact unlearning*, que es la
  garantía más fuerte que existe. **Es mejor resultado legal por menos trabajo.**

**La regla operativa, en una línea:** *si el modelo de dominio es BKT, el derecho al olvido se cumple
reentrenando y se puede probar; si es deep knowledge tracing, hay que hacer unlearning aproximado y el entregable
incluye la métrica de verificación, no sólo el borrado.*

### Lo que esta capa no tiene, por región, y es un gap informado

El barrido regional de esta capa da un resultado desparejo que conviene escribir en vez de dejar en silencio:

- **North America** — es donde vive la oferta: `locuslab` (CMU), `OPTML-Group` (Michigan State),
  `cisco-ai-defense`, `Data-Provenance-Initiative` (MIT Media Lab).
- **APAC** — la segunda concentración, y es la que tiene **lo específicamente educativo**: `torchunlearn` (Corea),
  `tamlhp` (Australia) y los autores de **PrivacyCD**. Extiende el patrón que el gap 4 viene anotando desde el
  pase 7.
- **EMEA** — 🚫 **no se encontró ninguna pieza de *unlearning*** en este barrido. Se declara **no encontrada, no
  inexistente**. Es llamativo porque EMEA es la región donde el **derecho de supresión (GDPR art. 17)** es
  directamente exigible: el régimen más fuerte del mundo y cero oferta propia de la tecnología que lo cumple.
- **LATAM** — 🚫 **no se encontró ninguna pieza de *unlearning***. Pero LATAM **sí** aporta a la otra mitad de este
  pase, y es la pieza más completa de toda la capa de `privacy provider`: **`local_aihub`, de un instituto federal
  brasileño**. Ver el **gap 2**, que este pase vuelve a mover.

Ver los **gaps 31 y 32**, las tendencias **45**, **46** y **47**, y los patrones **P38** y **P39**.


## Capa de testing de conformidad regulatoria — agregada en el pase 20 del 2026-10-01

Esta es la capa que esta KB **debía tener desde el pase 4** y no tenía. Desde entonces se vende un *expediente de
conformidad* (**P4** para el Anexo III europeo, **P10** para probar que el tutor enseña, **P11** para el gate de
seguridad pedagógica, **P17** para accesibilidad, **P39** para privacidad) y en ningún pase se registró **con qué
herramienta se corre la prueba**. La respuesta es que la herramienta existe, está madura, es permisiva, y la publican
reguladores.

**Verificado repo por repo vía WebFetch el 2026-10-01.** Nueve repos, todos reales, licencia leída en la página del
repo:

| Repo | Licencia | ★ | Forks | Qué es, y qué prueba |
|---|---|---|---|---|
| https://github.com/UKGovernmentBEIS/inspect_ai | **MIT** ✅ | 2.900 | 763 | **Lo más grande y más limpio de la capa.** Framework de evaluación de LLMs del **UK AI Security Institute** (organismo del gobierno británico). Trae **200+ evaluaciones** pre-construidas, *prompt engineering*, uso de herramientas, diálogo multi-turno y *model-graded evals*. Python |
| https://github.com/aiverify-foundation/moonshot | **Apache-2.0** ✅ | 353 | 70 | **La pieza central para un agente educativo.** *Benchmarking* **y** *red-teaming* en una sola herramienta, de la **AI Verify Foundation** (Singapur). Implementa el **Starter Kit de IMDA** como *cookbooks* pre-armados. Web UI + CLI. Python, v0.7.6 (**beta**), 2.153 commits |
| https://github.com/compl-ai/compl-ai | **Apache-2.0** ✅ | 211 | 37 | **La contraparte EMEA, y la única mapeada al AI Act.** Framework de evaluación organizado sobre **6 principios núcleo del EU AI Act** y sus requisitos técnicos, con **29 benchmarks** (y creciendo). De **ETH Zürich + INSAIT + LatticeFlow AI**, construido sobre Inspect. Python, 333 commits |
| https://github.com/aiverify-foundation/aiverify | **Apache-2.0** ✅ | 97 | 31 | La plataforma de *governance testing* de AI Verify: tests estandarizados contra principios reconocidos internacionalmente. ⚠️ **Lee con cuidado el alcance: evalúa modelos de aprendizaje supervisado sobre datos tabulares e imágenes**, no agentes LLM. v2.0 modular, 3.035 commits |
| https://github.com/aiverify-foundation/moonshot-data | **Apache-2.0** ✅ | 45 | 41 | Los *assets* de Moonshot: conectores (OpenAI, Anthropic, Together, HuggingFace), *datasets* (BigBench, CyberSecEval de PurpleLlama, benchmarks de tamil, **Medical LLM**, **AILuminate v1.0 DEMO** vía MLCommons), métricas, *attack modules*, *cookbooks* y plantillas de prompt |
| https://github.com/aiverify-foundation/LLM-Evals-Catalogue | ⚠️ **sin licencia declarada** | 23 | — | **El repo que contiene el hallazgo del pase.** Catálogo colaborativo de frameworks, benchmarks y papers de evaluación de LLMs en 7 categorías, con una de ellas *domain-specific*: **derecho, medicina y finanzas**. **Educación no figura** |
| https://github.com/aiverify-foundation/moonshot-cicd | **Apache-2.0** ✅ | 14 | 4 | La versión GA de Moonshot **para pipeline**: corre dentro de CI/CD, con Docker y soporte S3 nativo y guía de despliegue en AWS CodeBuild. Prueba cuatro categorías de riesgo: **alucinación, contenido indeseable, divulgación de datos y vulnerabilidad adversaria**. Python 3.12 |
| https://github.com/aiverify-foundation/moonshot-ui | **Apache-2.0** ✅ | 12 | 7 | La interfaz web de Moonshot (Next.js). Importa para un entregable: el informe sale en **HTML con gráficos interactivos** y export JSON, que es lo que un comité de ética o una inspección educativa puede leer sin consola |
| https://github.com/aiverify-foundation/aiverify-developer-tools | **Apache-2.0** ✅ | 9 | 6 | **La pieza que vuelve construible el gap 35:** plantillas para escribir **plugins de test y algoritmos propios** compatibles con el toolkit (v2.x). Es el punto de extensión por donde entraría una prueba pedagógica |

### 🔴 El hallazgo del pase, y son tres catálogos independientes diciendo lo mismo

No es una impresión de búsqueda: tres artefactos distintos, de tres jurisdicciones distintas, declaran su cobertura
por dominio y **ninguno incluye educación**.

1. **`LLM-Evals-Catalogue`** (AI Verify Foundation, Singapur) — categoría *domain-specific*: **derecho, medicina,
   finanzas**. Educación ausente.
2. **`compl-ai`** (ETH Zürich / INSAIT / LatticeFlow) — 29 benchmarks mapeados a los 6 principios del AI Act. **Sin
   mención de educación**, aunque el Anexo III del propio AI Act nombra la educación como alto riesgo de forma
   explícita.
3. **`morganrcu/awesome-eu-ai-act`** (**CC0**, 21 ★) — lista curada de herramientas de conformidad al AI Act:
   Giskard (5.700 ★), DeepEval, PyRIT, Inspect AI (MIT), Holistic AI (Apache-2.0), AI Act Companion (MIT), Regula
   (Apache-2.0 / EUPL-1.2), VerifyWise, AIR Blackbox, Venturalitica SDK, Inkog. **Ninguna herramienta específica del
   sector educativo.**

**Y del otro lado, esta KB tiene desde el pase 4 justo lo que falta ahí:** `EduBench` (**MIT**), `SafeTutors`
(🚫 **sin licencia — medida en el pase 51; su «MIT» era un *badge***), `MathTutorBench` (CC BY 4.0),
`UnifyingAITutorEvaluation` (CC BY-SA 4.0), `EduGuardBench` (sin licencia),
`AITutor-EvalKit` (🚫 **sin licencia, ídem**). Benchmarks pedagógicos premiados en EMNLP, NAACL y ACL — **y ninguno está mapeado a un
requisito regulatorio ni empaquetado como *recipe* de ninguna de estas herramientas.**

**Ése es el gap 35, y es el más construible que tiene esta KB**, por una razón de licencia: las dos puntas son
permisivas. `EduBench` es MIT; ⚠️ **`SafeTutors` NO —el pase 51 midió la ausencia de texto, su «MIT» era un *badge*—**; Moonshot, `moonshot-data` y `aiverify-developer-tools` son Apache-2.0;
Inspect es MIT; COMPL-AI es Apache-2.0. **No hay fricción legal en el ensamblado.** Lo que falta es el ensamblado.
Ver **P42**.

### Lo que esta capa NO es, y conviene no sobrevenderlo

- **Ninguna de estas herramientas certifica nada.** `aiverify` lo dice por escrito: *no define estándares éticos de
  AI y no garantiza que ningún sistema evaluado esté libre de riesgos o sesgos, ni que sea completamente seguro*. Es
  **evidencia**, no conformidad.
- **El marco de Singapur es voluntario.** El **Model AI Governance Framework for Agentic AI** no tiene cláusula de
  penalidad, ni registro obligatorio, ni mecanismo de *enforcement*. El europeo sí. Mezclar los dos en una propuesta
  es un error de encuadre: Moonshot sirve como **herramienta** en Europa, no como **cumplimiento** europeo.
- **No hay crosswalk directo de AI Verify al EU AI Act.** Lo que hay verificado son dos mapeos: a **NIST AI RMF**
  (octubre 2023 — el único ejercicio gobierno-a-gobierno del mundo) y a **ISO/IEC 42001:2023** (junio 2024). La vía
  hacia el AI Act es **indirecta, por ISO 42001**. Para un expediente europeo la pieza mapeada es **COMPL-AI**, no
  Moonshot.
- **`aiverify` no evalúa agentes.** Evalúa modelos supervisados tabulares y de imagen. Para un tutor LLM la pieza es
  **Moonshot**, **Inspect** o **COMPL-AI**. Proponer "AI Verify" a secas para un agente educativo es prometer la
  herramienta equivocada.

### El *unlearning* educativo, que llegó por la puerta de al lado

| Repo | Licencia | ★ | Commits | Qué es |
|---|---|---|---|---|
| https://github.com/GEMLab-HKU/Unlearn_and_Relearn | **MIT** ✅ | 4 | 22 | **El primer repo de esta KB que aplica *machine unlearning* a un modelo de alumno, con código publicado.** De GEMLab, **Universidad de Hong Kong** (Jiajia Song, Zhihan Guo, Jionghao Lin). Tres etapas: *unlearning* por destilación con intervención, *relearning* (fine-tuning o enseñanza interactiva guiada por LLM) y un loop de tres partes **Coach / Teachable Agent / Judge**. Olvido progresivo configurable del **10 al 50%**. Python |

🔴 **Y la distinción es el hallazgo, porque decide si mueve el gap 34 o no: no mueve.** Este repo **no usa
*unlearning* para privacidad**. Lo usa **al revés y a propósito**: para volver *tonto* a un modelo que sabe
demasiado, de modo que pueda hacer de **alumno novato creíble** en una dinámica de *learning-by-teaching* — el
problema real que ataca es que un LLM al que se le pide "actuá como principiante" se escapa igual hacia
explicaciones de experto y arruina el ejercicio. Mide si el agente **recupera** el conocimiento borrado cuando el
alumno humano se lo enseña.

**Entonces:** el **gap 34** (*unlearning* evaluado sobre modelos de alumno **por supresión de dato personal**) sigue
abierto, y ahora con un matiz que vale escribir — **la técnica que el gap 34 pide ya está en educación, con código y
licencia MIT; lo que no está es el uso de privacidad.** Es la misma maquinaria con el objetivo invertido. Para quien
construya el *harness* del gap 34, esto es la mejor noticia posible: hay un precedente educativo funcionando del que
salen las dos mitades difíciles (cómo se borra un concepto de un modelo y cómo se mide que se borró), y lo único que
hay que cambiar es qué se borra y para qué. Ver **P43**, que lo usa por su lado pedagógico, que es el que está listo.

⚠️ **4 estrellas y 0 forks.** Es un repo de laboratorio, no una dependencia. Vale como **arquitectura de
referencia**, igual que `tero` en el pase 8.

### La nota de método del pase, y explica dos pasadas de búsquedas fallidas

Los pases 18 y 19 buscaron *unlearning* sobre *knowledge tracing* y no encontraron código. **Hay una colisión de
terminología que lo explica, y conviene dejarla escrita porque va a volver a pasar.** La frase «*knowledge tracing*»
tiene **dos significados incompatibles** en la literatura que devuelve esa búsqueda:

- el de esta KB y de `pyKT`: **modelar el estado de conocimiento del alumno** a lo largo del tiempo;
- el de la literatura de *unlearning* (p. ej. *Lifting Data-Tracing Machine Unlearning to Knowledge-Tracing for
  Foundation Models*): **rastrear qué conocimiento de un modelo fundacional vino de qué dato de entrenamiento**.

Buscar «unlearning + knowledge tracing» devuelve el segundo sentido y **entierra el primero**. La búsqueda que sí
funcionó fue por **escenario educativo** (*novice student simulation*), no por técnica — que es exactamente la regla
que el pase 5 ya había aprendido para los benchmarks y que esta KB vuelve a redescubrir en otra capa.

### Lo que esta capa tiene por región

- **APAC** — **es donde vive la oferta, y por primera vez con un regulador adentro**: toda la pila AI Verify /
  Moonshot es de **Singapur** (IMDA + AI Verify Foundation), y el único *unlearning* educativo con código es de
  **Hong Kong**. Extiende el **gap 4** a una capa más, y con un signo distinto a las anteriores: acá lo APAC no es
  un prototipo sin licencia, es **infraestructura de un Estado con Apache-2.0**.
- **EMEA** — **la única pieza mapeada al régimen que sí es exigible**: `compl-ai` (ETH Zürich + INSAIT +
  LatticeFlow, Apache-2.0, 211 ★) e `inspect_ai` (UK AISI, **MIT**, 2.900 ★). Es el patrón que el **gap 3** viene
  anotando desde el pase 4 —EMEA produce la capa que mide, no el tutor— y acá se cumple de forma casi caricaturesca.
- **North America** — aporta **el puente de interoperabilidad**, no la herramienta: el **NIST AI RMF** es el marco
  contra el que AI Verify se mapeó en 2023. La oferta de herramienta propia en esta capa es privada (LatticeFlow es
  suiza; Giskard, francesa).
- **LATAM** — 🚫 **no se encontró ninguna herramienta de testing de conformidad de origen LATAM** en este barrido.
  Se declara **no encontrada, no inexistente**. Y duele más que en otras capas, porque **Brasil, Chile y México
  tienen los tres obligaciones de auditoría algorítmica escritas o en trámite** (ver `intel/market.md`): la región
  está legislando la auditoría y no está construyendo la herramienta que la ejecuta.

Ver el **gap 35**, las tendencias **51**, **52** y **53**, y los patrones **P42** y **P43**.

## 🔌 La capa conector — agregada en el pase 26 del 2026-10-01

Veinticinco pasadas buscaron **agentes**. Esta buscó **la puerta por la que el agente entra al sistema instalado**, que
es lo que el pase 25 dejó escrito como eje (*«cambiar el eje de búsqueda al conector»*). Es la primera vez que esta KB
mide una capa en vez de inventariarla: **el cartucho MCP de CaSS se ejecutó**, y el resultado cierra el gap 40.

### El cartucho MCP de CaSS, medido — el gap 40 se cierra

El pase 25 registró que CaSS *declara* MCP entre sus cartuchos y marcó el **gap 40** porque nadie había levantado el
servidor ni listado una sola herramienta. **Este pase las listó.** No levantando el servidor —que necesita Elasticsearch
y en este entorno **no hay demonio de Docker**— sino por el camino que la propia arquitectura del proyecto permite:
el adaptador genera las tools con `generateTools(spec)` sobre el OpenAPI que `swagger-jsdoc` construye desde los
comentarios del código, **y eso corre sin base de datos**. Se reprodujeron las opciones exactas de `src/main/server.js`,
se generó el spec, se validó con el mismo `openapi-schema-validator` que el servidor usa al arrancar, y se ejecutó el
generador real del repo.

**Resultado medido:** spec de **51 paths**, **0 errores de validación**, y **6 tools + 3 resource templates**.

| Tool | Método y path | Parámetros | Requeridos | `readOnlyHint` |
|------|---------------|------------|------------|----------------|
| `server_status` | `GET /api/ping` | `fields` | — | ✅ true |
| `search_data` | `GET /api/data/` | `q`, `start`, `size`, `index_hint` | — | ✅ true |
| `get_object` | `GET /api/data/{uid}` | `uid`, `history` | `uid` | ✅ true |
| `save_object` | `POST /api/data/{uid}` | `uid` | `uid` | ❌ false |
| `record_evidence` | `POST /api/xapi/statement` | *(body)* | `body` | ❌ false |
| `get_learner_profile` | `GET /api/profile/latest` | `frameworkId`, `subject`, `flushCache`, `cache`, `targetDateTime` | — | ✅ true |

Resource templates: `CaSS JSON-LD Object`, `CaSS JSON-LD Object (Versioned)`, `CaSS Object by UID`.

**Por qué esto cambia el patrón P48 y no sólo cierra un gap.** Las dos tools que importan son `record_evidence`
(`POST /api/xapi/statement`) y `get_learner_profile` (`GET /api/profile/latest`): **entrar evidencia xAPI y sacar
perfil de competencia, por MCP, bajo Apache-2.0.** Ésos son exactamente los dos pasos que el paso 4 de **P48** tenía
inferidos desde una línea de README. La descripción que el propio repo le pone a `get_learner_profile` —*«use this tool
to answer the question "what does this person know?"»*— es la operación que esta KB viene describiendo desde el pase 14
sin tener con qué ejecutarla. Ver la tendencia **66** y el patrón **P50**.

**Y hay un hallazgo de diseño que corrige una suposición razonable.** De los **51 paths** del spec, el cartucho expone
**6**. No es una limitación: son **45 paths marcados `x-mcp-ignore: true`** uno por uno en el código, con anotaciones
`x-mcp-tool-name` y `x-mcp-description` escritas a mano en los 6 que sí salen. **La superficie MCP de CaSS está curada,
no volcada.** Lo que queda deliberadamente afuera incluye `POST /api/xapi/statements` (el *bulk* del LRS),
`GET /api/xapi/endpoint`, el `multiPut`/`multiDelete`/`multiGet` de skyRepo y todo `skyId`. **Consecuencia práctica:**
por MCP se escribe **un statement por llamada**, no lotes — quien cotice ingestión masiva de telemetría por esta puerta
está cotizando mal. Ver el **gap 41**.

⚠️ **Lo que esta medición NO es.** No se levantó el servidor HTTP ni se hizo *handshake* MCP con un cliente real: se
midió la **generación** de las tools, que es determinista y pura sobre el spec, no su **invocación**, que necesita
Elasticsearch. Las 13 aserciones de `5.mcp.json-schema-to-zod.test.js` pasan (13/13); `5.mcp.openapi-to-tools.test.js`
**no se pudo correr tal cual** porque su `before` hace `fetch` a `localhost:80/api/swagger.json`. El conteo de 6 coincide
con lo que ese test afirma (*«generates exactly 6 tools from the current spec»*) y con las **6** anotaciones
`x-mcp-tool-name` del árbol. **Tres fuentes independientes dan 6.** Queda como acción del pase 27 el *handshake* real.

### El lado *platform* (LMS) se cierra por medición, y la respuesta es que no existe permisivo

El pase 25 dejó como acción *«levantar `LtiAdvantagePlatform` (MIT) contra `ltijs` y medir si el launch OIDC cierra»*.
**La ejecución está bloqueada por el entorno y hay que decirlo:** `LtiAdvantagePlatform` es **ASP.NET Core 10**, en esta
sesión **no hay `dotnet`**, y no se puede instalar — `https://dot.net/v1/dotnet-install.sh` responde
**`CONNECT tunnel failed, 403`** por el proxy de egreso. El *launch* de punta a punta sigue sin medirse.

**Pero la pregunta de fondo sí se pudo contestar, y por primera vez con evidencia de primera mano en los seis
candidatos.** Se instaló `ltijs` desde npm (**5.9.9, Apache-2.0**) y se inspeccionaron sus exports:

```
top-level exports: [ 'Provider' ]
```

**Un solo export, `Provider`.** No hay clase de *consumer*/*platform*. Y su propio `package.json` dice
*«Easily turn your web application into a LTI 1.3 **Learning Tool**»*. **`ltijs` es tool-side y nada más**, medido, no
leído de la documentación.

| Pieza | Licencia | ★ | Lado | Estado real |
|------|----------|---|------|-------------|
| `ltijs` | **Apache-2.0** ✅ | 373 | *tool* | Producción. **Sólo exporta `Provider`** (medido en el pase 26) |
| `oat-sa/lib-lti1p3-core` | ⚠️ **GPL-2.0** | 37 | *platform* **y** *tool* | **El único completo y certificado 1EdTech** — y copyleft |
| `macewan-cs/lti` | **MIT** ✅ | 8 | *tool* | Go. *«partially implements»*, **tool-side** — no es el lado LMS |
| `LtiLibrary/LtiAdvantagePlatform` | **MIT** ✅ | — | *platform* | Se describe **«Sample»**. ⛔ No ejecutable acá: sin `dotnet`, dot.net bloqueado |
| `Citolab/lti-1p3-platform-example` | ⚠️ **GPL-3.0+** | — | *platform* | *«example»* en el nombre. .NET + React |
| `UOC/java-lti-1.3-platform` | ⚠️ **sin licencia** | 0 | *platform* | *«**will** implement»* (pase 24) |

🔴 **La conclusión, dicha sin suavizar: no hay implementación *platform-side* de LTI 1.3 que sea permisiva **y**
productiva.** Las dos permisivas se autodenominan *«Sample»* y *«example»*; la única completa y certificada por 1EdTech
es **GPL-2.0**; la única que prometía serlo en Java no declara licencia y habla en futuro. **Esta KB no puede proponer
el lado LMS con licencia permisiva**, y ahora eso está **medido sobre seis candidatos**, no supuesto. Para un
*engagement* que necesite el lado plataforma la salida honesta es una de tres: aceptar **GPL-2.0** (TAO, certificada),
integrarse como *tool* contra un LMS que el cliente ya tiene (que es donde esta KB sí es fuerte: `ltijs` + `canvas-mcp`),
o presupuestar el lado plataforma como **desarrollo**, no como integración. Ver el **gap 42** y la tendencia **67**.

### Los conectores de LMS que trajo el eje, y la corrección de licencia que hay que leer antes de proponer

| Pieza | Licencia | ★ | Forks | Commits | Tools | Lectura |
|------|----------|---|-------|---------|-------|---------|
| `vishalsachdev/canvas-mcp` | **MIT** ✅ | 269 | 92 | 815 | **hasta 102–103** + 8 skills | **Entra en la tabla principal.** Las dos puntas (alumno y docente), descubrimiento de tools, escaneo WCAG |
| `csmediapro/moodle-mcp-server` | 🔴 **AGPL-3.0** | **0** | **0** | 57 | **10**, sólo lectura | ⛔ **No proponer.** Ver la corrección abajo |
| `DavidLMS/learnmcp-xapi` | **MIT** ✅ | 15 | 4 | 32 | 3 | Ya estaba (pase 6). **Re-verificado: idénticos 15 ★ y 32 commits** → el proyecto no se movió |

🔴 **La corrección de licencia del pase, y es sobre el único conector de Moodle que existe.** El resumen de búsqueda
presentaba `moodle-mcp-server` como *«open-source MCP server, plugin-extensible, LLM-agnostic»* e invitaba a instalarlo
con `npx`. **La página del repo dice otra cosa en dos frentes:** la licencia es **AGPL-3.0** —no permisiva, y la AGPL es
la que más molesta en un entregable SaaS— y el modelo es **open-core**: los diez tools abiertos son **sólo de lectura**
(`list_courses`, `get_course`, `list_course_users`, `list_assignments`, `list_categories`, `get_site_info`, `get_user`,
`list_user_courses`, `search_users`, `search_courses_by_name`) y las capas que un cliente pediría —*Advanced Reporting*,
*User Analytics*, *User Directory*, *Compliance Pack*— son **plugins premium que se venden aparte**. Súmese **0 ★ y 0
forks**: no hay adopción que respalde el riesgo. **Moodle es el LMS más instalado del mundo y su único conector MCP es
AGPL con las partes útiles cerradas.** Ése es el hueco, y es un hueco de oportunidad: ver el **gap 43** y el patrón **P51**.

⚠️ **Nota de método sobre la verificación de URLs en este pase.** La consigna pide `curl -sI` por URL. **En esta sesión
`curl -sI` contra `github.com` devuelve `403` para *todas* las URLs** —incluidas las que existen y están en esta KB desde
el pase 1— porque el proxy de egreso corta el `HEAD`. Verificar con `curl` acá produciría **404s falsos sobre repos
reales**, que es el error que la consigna quiere evitar. Por eso **toda verificación de este pase se hizo con WebFetch
sobre la página del repo** (licencia, ★, forks, commits leídos de la página), y el único 404 que se reporta —
`Cerebro-Tech/FlightPath` — es un 404 **de WebFetch**, no de `curl`.

## Capa de conectores de *rostering* y estándares — medida en el registro de paquetes, pase 31 del 2026-10-02

Treinta pases buscaron conectores **por nombre de protocolo** (`*-mcp`, `mcp-*`). El pase 30 demostró que eso deja
ausencias mal medidas y dejó la consigna de **preguntarle al registro de paquetes por el nombre del proyecto o del
estándar, y abrir el README a buscar «MCP» adentro**. Este pase la ejecutó contra `registry.npmjs.org` y `pypi.org`.
**Rinde: aparece una segunda puerta MCP de OneRoster y es MIT.**

| Agente / conector | Paquete verificado | Versión | Licencia | Sirve MCP | Qué escribe |
|---|---|---|---|---|---|
| **`@eduware/oneroster`** | [registry.npmjs.org](https://registry.npmjs.org/@eduware%2Foneroster) | 1.2.11 | **MIT** ✅ | ✅ **sí — ejecutable `mcp` empaquetado** | OneRoster **1.1 y 1.2** completo + perfil `ClassLink` de sólo lectura |
| `@superbuilders/oneroster` (= `trilogy-group/oneroster-ts`) | [github.com/trilogy-group/oneroster-ts](https://github.com/trilogy-group/oneroster-ts) | 0.7.0 | 0BSD ✅ | ✅ sí (ya registrado, 132 tools medidas en el pase 30) | OneRoster con escritura |
| `openedx-mcp` (oficial Open edX) | [pypi.org/project/openedx-mcp](https://pypi.org/project/openedx-mcp/) | 0.1.5 | ⚠️ **AGPL-3.0** | ✅ sí (35 rutas) | matrícula, usuarios, roles, certificados, reportes, **authoring de bloques** |

**Lo que dice el README de `@eduware/oneroster`, textual:** *«the included MCP server for tool-based integrations»* y
*«The package includes an MCP server that exposes SDK operations as tools»*. 13 versiones publicadas, creado
**2026-01-23**, última modificación **2026-07-10**.

⚠️ **Y la advertencia que va con el alta:** su repo declarado, `Eduware-Inc/eduware-oneroster`, **devuelve 404** por
`raw.githubusercontent.com`. **El paquete es verificable en el registro; el repo es una afirmación que no se puede
comprobar.** Se cita por registro a propósito. Es el **gap 58**, y da una regla nueva para esta KB: **el paquete
publicado y el repo público son dos verificaciones distintas, y la que importa para construir es la del paquete.**

### Lo que se midió y salió vacío — ausencias informadas, no silencios

| Candidato | Qué se midió | Resultado |
|---|---|---|
| **`ltijs`** v7.0.6 (Apache-2.0, repo verificado, modificado **2026-09-18**) | README completo leído, grep de `MCP` / `Model Context Protocol` | **0 menciones.** El SDK LTI 1.3 de referencia está vivo y mantenido **y no tiene puerta de agente**. El **gap 42 sigue cerrado**, ahora por medición y no por etiqueta |
| **`pylti1p3`** v2.0.0 (MIT) | PyPI: 29 releases, **última publicación `2022-11-20`** | Sin MCP, y 🔴 **casi cuatro años sin release**. ✅ El repo (`dmitry-viskov/pylti1.3`) **sí existe** —`README.rst`, `setup.py` y `LICENSE` responden 200— y esta KB ya lo tenía registrado con 138 ★: el abandono es **de publicación en PyPI**, no del repo |
| **`@timeback/caliper`** v0.3.3 | registro: licencia y repo | 🔴 **No declara licencia.** Código **de 2026-09-25** y jurídicamente inusable. Ver advertencias de licencia |
| **`openbadges`** en npm | familia `openbadges-validator*`, `openbadges-bakery*` | Herramientas de validación y *baking*, **OB 2.0**, sin MCP |

### 🟢 Una pieza que faltaba y entra permisiva: OpenBadges **3.0**

| Pieza | Paquete | Versión | Licencia | Qué aporta |
|---|---|---|---|---|
| **`@ajna-inc/openbadges`** | [registry.npmjs.org](https://registry.npmjs.org/@ajna-inc%2Fopenbadges) | 0.6.3 | **Apache-2.0** ✅ | *«OpenBadges v3.0 module for Credo-TS with OAuth 2.0 provider support»*, modificado 2026-05-19 |

Esta KB tenía registrado que **CaSS implementa OB 2.0 y no 3.0**, y no tenía **ninguna** pieza de OB 3.0. Ya la tiene, y
es permisiva. ⚠️ No declara repo, así que se cita por registro (mismo criterio que `@eduware`).

