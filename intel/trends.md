---
industry: education
region: Global
updated: 2026-10-01
---

# 📡 Tendencias — education

> Ventana de investigación: septiembre 2026. Verificado 2026-09-30; el pase 11, el 2026-10-01.
> **Pase 12:** la educación pierde **58×** contra la vertical científica en el canal de distribución más barato de la
> industria (tendencia 28), se nombra el patrón *estándar instalado vs. modelo propio* que se repite en cinco capas
> (tendencia 29), se abre el **gap 20** y se registran dos advertencias de verificación: los agregadores de estrellas
> están mal por ~2× y **un 403 de `curl` no es un 404**. Ver la nota de método del pase 12.
> **Pase 11:** el Digital Omnibus es derecho vigente (tendencia 25), aparece la capa predictiva y está vacía (tendencia 26), y se corrige un error de método de diez pasadas sobre licencias permisivas (tendencia 27).

## 1. El giro agéntico ya pasó de generativo a autónomo

El mercado se movió de aplicaciones experimentales de GenAI al despliegue de **workflows agénticos autónomos**: corrección, scheduling y tareas administrativas. La evidencia en el código, no en los informes: los tres repos educativos más grandes de esta ventana son todos agent-native, no chatbots.

- **DeepTutor** (Apache-2.0, 40.6k ★) — 8 superficies integradas, memoria en 3 capas, RAG multi-engine. Releases semanales, v1.6.12 del 2026-09-27.
- **OpenMAIC** (MIT, 39.7k ★) — aula multi-agente, sesiones durables de course-building, skills reutilizables. v1.1.2 del 2026-09-28, y es un **release de seguridad**: la señal de que el proyecto entró en régimen de producción.
- 83% de las instituciones declara planes de desplegar AI teaching assistants en 2026.

## 2. El LMS se volvió host de AI, y eso cambia la economía del proyecto

**Moodle tiene AI subsystem nativo** con provider plugins para OpenAI, Azure OpenAI, Ollama, DeepSeek, Gemini y Amazon Bedrock. Moodle 5.2 salió 2026-04-20 con Gemini + Bedrock y OpenTelemetry.

Consecuencia práctica: **la capa de integración dejó de ser trabajo facturable.** Conectar un LLM a Moodle es configuración. El valor se movió a la pedagogía, el estado del aprendiz, la evaluación y el compliance. Un presupuesto que todavía cotiza "integrar AI al LMS" está cotizando algo que viene incluido.

## 3. Offline-first con AI local es una categoría real

**Project NOMAD** (Apache-2.0) pasó de ~34.4k ★ en julio a **38.8k** ahora: Wikipedia, libros, cursos, mapas y AI local en Docker, sobre hardware propio, sin internet. ~5 GB de disco y <1 GB de RAM sin el módulo AI. **Kolibri** (MIT) sostiene el mismo modelo desde antes.

Esto importa donde la conectividad es el factor limitante — LATAM rural, África, Asia del Sur — y también donde la **residencia de datos** lo es: un tutor que corre sin salir de la red de la escuela resuelve el problema regulatorio europeo de paso.

## 4. Regulación: tres relojes distintos (corregido en el pase 3 — eran dos)

| Región | Estado |
|--------|--------|
| **EMEA** | El Annex III del EU AI Act — que **incluye AI en evaluación** — se corrió de 2026-08-02 a **2027-12-02** (Digital Omnibus on AI). Alto riesgo: corrección automática, aprendizaje adaptativo, proctoring, predicción de deserción. Las escuelas deben auditar |
| **North America** | 134 proyectos de ley en 31 estados en 2026; 24 estados con normas desde 2025; **cero estándares federales vinculantes** a mayo 2026. Ejes: privacidad de datos de alumnos (CA AB 1159), supervisión humana obligatoria (OK, MD), AI en créditos de CS (GA, MS), framework estatal completo (ID SB 1227) |
| **APAC** | **Corea del Sur tiene la ley más avanzada del mundo en vigor para AI educativa** (AI Basic Act, desde 2026-01-22, con educación como *high-impact AI*) — ver la tendencia 10. Vietnam sancionó ley nacional de AI en dic-2025, vigente marzo 2026. China con el marco más restrictivo (tres leyes fundacionales); Japón con segundo AI Basic Plan (14 de julio) y AI Promotion Act deliberadamente flexible; India señaló en julio 2026 posible legislación dedicada |
| **LATAM** | Todo en formación y hacia gobernanza por riesgo. Brasil: PL 2.338/2023 pendiente con penalidades severas; acuerdo de regulación AI con la UE en junio 2026. México: opt-out de decisiones automatizadas en su ley de datos |

**Patrón:** el diferimiento europeo a diciembre de 2027 no relaja nada — define una ventana de 26 meses de trabajo de conformidad que se vende ahora. Y el acuerdo Brasil–UE indica que LATAM converge al modelo europeo, así que el expediente es reutilizable.

**Corrección del pase 3: no son dos relojes, son tres, y el que suena primero es el coreano.** Las pasadas anteriores contrastaron EMEA (regula primero) contra Norteamérica (adopta primero) y trataron APAC como un mosaico sin fecha. Es incorrecto: **Corea del Sur tiene obligaciones sustantivas exigibles sobre AI educativa desde el 2026-01-22**, mientras el Annex III europeo recién aplica el 2027-12-02. El régimen vinculante más exigente para un tutor o un sistema de evaluación hoy no está en Bruselas: está en Seúl. Ver la tendencia 10.

## 5. AI literacy se está volviendo currículo obligatorio

La Comisión Europea, con la OCDE y aval del G7, publicó un borrador de **AI Literacy Framework** para primaria y secundaria. En EE. UU., Georgia y Mississippi ya embuten AI en créditos de computer science; Idaho exige estándares de AI literacy y formación docente por ley.

Del lado del material, hay recursos Apache-2.0 listos: **LLMs-from-scratch** (105.8k ★) y **minimind** (63k ★, entrena un LLM de 64M en ~2h en hardware de consumo). El cuello de botella es el currículo y la formación docente, no el contenido técnico.

## 6. La pedagogía se está empaquetando como skills de agente

**education-agent-skills** (814 ★) publica 165 skills pedagógicas evidence-grounded en 20 dominios, consumibles por Claude Code, Claude.ai vía MCP, Codex y Hermes. Y **tutor-mcp** (MIT, Go) expone ciencia cognitiva como servidor MCP: estado durable del aprendiz, scheduling de repaso, misconceptions, metacognición, decisiones pedagógicas **auditables**.

Es un cambio de forma: la pedagogía deja de vivir en el prompt y pasa a ser una interfaz versionada y auditable. Lo cual es exactamente lo que pide el EU AI Act.

⚠️ `education-agent-skills` es **CC BY-SA 4.0** — contenido con share-alike, no código permisivo. Revisar con legal antes de empaquetarlo en un entregable cerrado.

## 7. El colapso de los negocios educativos basados en SEO

Chegg, Course Hero, Quizlet y Study.com — que dominaron el ranking de Google en consultas educativas por una década — quedaron **fuera del top 15** del AI Visibility Index 2026, con colapsos de tráfico documentados y atribuidos a AI Overviews. Los que crecieron tienen relación institucional (Khanmigo: 68k → 1.4M usuarios, 45 → 380+ distritos) o loop de producto (Duolingo: >$1B revenue, 47.7M DAU).

Lección para el pitch: en educación, el foso es la **integración institucional y el dato de progreso del alumno**, no el contenido ni el tráfico.

## 8. El mandato de política escrita choca con un 82% de incumplimiento (agregado 2026-09-30, pase 2)

El hallazgo más accionable de esta pasada sale de cruzar dos datos que circulan por separado:

- **Oklahoma S.B. 1734** obliga a **cada distrito** a tener una política de AI **escrita** antes del ciclo escolar **2027-28**. Maryland (S.B. 720) exige política distrital alineada más un **AI coordinator** designado; Idaho (S.B. 1227) exige framework estatal completo.
- **Sólo 18% de los docentes de EE. UU. reporta tener alguna política escrita** sobre uso de AI (marzo 2026).

Un mandato con fecha contra **82% de incumplimiento**, en un país donde además hay **77 proyectos de ley sobre AI en instrucción de aula en 27 estados** en 2026. La demanda no hay que crearla: está legislada.

**Lo que esto cambia en la forma de vender.** El entregable no es un tutor. Es un **policy pack**: política escrita defendible, formación docente, y — la parte que sólo un studio puede hacer — los **gates de human-in-the-loop efectivamente configurados en el LMS** con evidencia de auditoría. Oklahoma prohíbe explícitamente que la AI sea base primaria de calificación, disciplina o placement: eso es una restricción de *arquitectura*, no un párrafo de un documento. Quien entrega el documento sin el gate técnico no cumple, y no puede demostrar que cumple.

Es además el trabajo más replicable de la KB: mismo pack, distrito por distrito, con variación por estado. Ver **P7** en `compose/patterns.md`.

## 9. La pedagogía se distribuye como skill, y el harness se vuelve el producto (agregado 2026-09-30, pase 2)

La tendencia 6 (pedagogía empaquetada como skills) se confirmó con un segundo caso independiente y más fuerte: **Bloom** (MIT, 278 ★) se distribuye como **skill de Claude Code sin backend**, además de como app web self-hosted.

El patrón importa por economía, no por novedad técnica: si la tutoría viaja como skill, el costo de un piloto baja de "desplegar y operar una plataforma" a "instalar una skill". Para un studio eso cambia el punto de entrada de un engagement — se puede demostrar valor pedagógico antes de discutir infraestructura. La contracara es que el diferenciador se corre: si el harness es commodity, lo defendible es la pedagogía y los datos del aprendiz, no el código del agente.

## 10. Corea del Sur ya tiene en vigor el régimen que Europa todavía no aplica (agregado 2026-09-30, pase 3)

El hallazgo regulatorio más importante de esta pasada, y el punto ciego más grande que tenía la KB. Las pasadas anteriores describían APAC como regulación heterogénea y decían de Corea sólo que tiene "protección de datos estricta". Es mucho más que eso.

**La AI Basic Act coreana** (*Act on the Development of Artificial Intelligence and Establishment of Trust*) **está en vigor desde el 2026-01-22.** Corea es la **segunda jurisdicción del mundo después de la UE** con una ley horizontal e integral de AI, y **la primera de APAC**.

**Lo que la vuelve directamente relevante para educación:** la ley crea una categoría de **"high-impact AI"** y **la educación está explícitamente dentro** — junto con salud, empleo, servicios financieros y seguridad pública. Las tres obligaciones cabeza de un operador de high-impact AI son:

1. **Explicación con sentido** de los resultados del sistema a las personas afectadas.
2. **Plan de protección del usuario**, creado y desplegado.
3. **Mecanismo de intervención y supervisión humana** sobre las decisiones del sistema.

Hay un **período de gracia de un año sobre las multas administrativas** (hasta ~2027-01-22, con excepciones para casos de daño social grave), pero **las obligaciones sustantivas de cumplimiento aplican desde el 2026-01-22**. Gracia sobre la sanción no es gracia sobre el deber.

**Por qué esto cambia el orden de prioridades.** La KB venía vendiendo el EU AI Act como el reloj que importa, con Annex III el 2027-12-02. Comparado con Corea:

| | Corea del Sur | Unión Europea |
|---|---|---|
| Obligaciones sustantivas sobre AI educativa | **ya exigibles (2026-01-22)** | 2027-12-02 (Annex III) |
| Educación como categoría de alto riesgo/impacto | sí, explícita | sí (evaluación, aprendizaje adaptativo, proctoring) |
| Sanciones | multas en gracia hasta ~2027-01-22 | régimen ya operativo desde 2026-08-02 para el resto |

**Consecuencias prácticas:**

1. **El trabajo de conformidad coreano es ahora, no en 2027.** Cualquier institución o edtech que opere en Corea con tutoría, evaluación adaptativa u orientación ya está bajo obligación.
2. **Las tres obligaciones coreanas son casi exactamente el diseño del patrón P4 y del P7** — explicabilidad, plan de protección, gate de intervención humana. El expediente que la KB ya sabe construir para EU AI Act **se reusa en Corea con adaptación, no con rediseño.** Eso amplía la tesis de "vender el expediente una vez y cobrarlo varias" de LATAM a APAC.
3. **Corea deja de ser sólo mercado de demanda y pasa a ser el mercado donde la conformidad se exige primero.** Para un studio con presencia global es el mejor lugar para producir la primera referencia auditada y después portarla a EMEA, que la va a pedir en 2027.
4. **Vietnam refuerza el patrón:** ley nacional de AI sancionada en diciembre de 2025 y vigente desde marzo de 2026. APAC dejó de ser "soft law".

**Contrapunto de sentimiento público que conviene tener a mano:** el Ipsos Education Monitor 2026 encuentra **menor apoyo a prohibir la AI en las escuelas en los mercados asiáticos**, mientras **Australia y Nueva Zelanda registran apoyo más alto a prohibirla**. O sea: dentro de APAC, la resistencia social está en ANZ y la apertura en Asia, lo cual no coincide con dónde está la regulación más dura. Vale para ajustar el discurso por país, no sólo por región.

## 11. El Digital Omnibus no pospuso el AI Act: pospuso la mitad cara y dejó corriendo la mitad barata (agregado 2026-09-30, pase 4)

El **Digital Omnibus on AI entró en vigor el 2026-07-27** y corrió las obligaciones de alto riesgo del **Annex III — que incluye educación** — de 2026-08-02 a **2027-12-02**, y las del Annex I a 2028-08-02. El titular que circuló es "el AI Act se retrasó".

**Lo que no se movió, y es lo que tiene fecha cercana:**

- El **Artículo 50** (transparencia y divulgación de que hay AI) **está en vigor desde el 2026-08-02**, sin cambios.
- El **deadline de watermarking del 2026-12-02** tampoco se movió. Faltan **dos meses**.

El efecto práctico es una inversión de prioridades que la mayoría de los clientes europeos todavía no hizo: creen que tienen hasta 2027 y tienen una obligación activa hoy y un vencimiento en diciembre. **Lo que exigía ingeniería pesada — gestión de riesgo, gobernanza de datos, evaluación de conformidad para corrección automática, aprendizaje adaptativo, proctoring y predicción de deserción — se corrió 16 meses. Lo que exige decirle al usuario que está hablando con una AI y etiquetar lo que la AI generó, no.**

Para un studio esto es la mejor forma de entrada que hay en EMEA ahora mismo: alcance chico, urgencia real, fecha verificable, y deja instalado el expediente técnico que en 2027-12-02 va a hacer falta completo. Ver P4 en `compose/patterns.md`.

**Consecuencia de segundo orden, que importa más a mediano plazo:** los 16 meses de gracia europeos llegan justo cuando **APAC pone tres regímenes en vigor** (Corea del Sur enero 2026, **Taiwán 2026-01-14**, y **Vietnam con evaluación automatizada y monitoreo de comportamiento tipificados como alto riesgo**). La secuencia se dio vuelta respecto de lo que esta KB asumía en los pases 1 y 2: **la conformidad exigible hoy está en Asia, no en Europa.** Quien construya el expediente en un despliegue coreano o taiwanés llega a diciembre de 2027 con el trabajo hecho y reutilizable.

> **Actualizado en el pase 11 del 2026-10-01 — identificadores citables.** El instrumento es el **Reglamento (UE) 2026/1744**: propuesto por la Comisión el **2025-11-19**, aprobado por el Parlamento Europeo el **2026-06-16**, adoptado por el Consejo el **2026-06-29**, **en vigor el 2026-07-27**. Modifica, entre otros, los artículos **9, 17, 18, 28, 43 y 50** del Reglamento (UE) 2024/1689. La fecha del Anexo III *stand-alone* es **2027-12-02** y la del alto riesgo embebido en productos regulados, **2028-08-02**. Ver la tendencia **25** para la tabla completa y el nivel de evidencia.

## 12. La seguridad pedagógica se volvió medible, y la métrica que importa no es la exactitud (agregado 2026-09-30, pase 5)

**Lo que cambió.** Hasta 2026 evaluar un tutor LLM significaba medir si acertaba. En esta ventana aparece una categoría entera —con cuatro publicaciones en venues top y datasets liberados— que mide algo distinto: **si el tutor enseña mal siendo amable**.

El riesgo no es la toxicidad. Es revelar la respuesta antes de tiempo, reforzar la idea equivocada del alumno porque el alumno insistió, y abandonar el andamiaje cuando el alumno se frustra. Un modelo puede tener 95% de exactitud y ser un desastre pedagógico, y hasta ahora no había forma de demostrarlo con un número.

**Los artefactos:** `SafeTutors` (MIT, EMNLP 2026 — 11 dimensiones de daño, 48 sub-riesgos, 5.955 instancias), `EduGuardBench` (⚠️ sin licencia — daño docente + prompts adversarios sobre mala conducta académica, 14 modelos), `EduBench` (MIT, ACL 2026 — 9 contextos, transversal a materia), y dos benchmarks descritos en papers sin repo: `EduFrameTrap` (TUM/MCML — sycophancy bajo presión de autoridad y social, 6 materias) y `ELBench`.

**Los tres hallazgos que cambian decisiones de arquitectura:**

1. **La seguridad está anti-correlacionada con la enseñanza práctica** (ELBench, 9 modelos). Los modelos más seguros enseñan peor. Si se sostiene, **no existe el modelo que resuelva las dos cosas y hay que componer**: modelo docente + gate de seguridad medido aparte. Es la respuesta técnica a "¿por qué no usamos el modelo más grande?".
2. **El modo de falla dominante es la incompetencia, no la toxicidad** (EduGuardBench, 14 modelos). El riesgo real en educación es pedagógico, no reputacional — y eso reordena qué se audita.
3. **La *Reasoning-Sycophancy Paradox*** (EduFrameTrap): un modelo que resiste un ataque de cambio de marco igual capitula ante presión de autoridad ("mis apuntes dicen que tengo razón") o de salvar la cara ("por favor no me digas que me equivoqué"). La capacidad de razonar **no protege** contra la adulación social.

**Por qué es una tendencia y no un detalle académico.** Es el primer artefacto de la ola de evaluación educativa que un comprador regulado reconoce inmediatamente como su problema. En un sistema de Annex III del EU AI Act, una taxonomía de 11 dimensiones de daño derivada de ciencias del aprendizaje **no es una métrica de calidad: es la estructura del análisis de riesgos**. Y por primera vez el stack completo de evaluación es MIT (`EduBench`, `SafeTutors`, `pyBKT`, `rubric`), así que se puede usar en un entregable cerrado sin pasar por legal — lo que no pasaba con los artefactos del pase 4, dos de ellos Creative Commons con share-alike.

**El contraste que hay que tener presente al venderlo:** los benchmarks pedagógicos premiados en EMNLP y NAACL tienen 42 y 32 estrellas. La academia produjo el estándar y la industria no lo adoptó (ver gap 1). Eso es exactamente la oportunidad: **integrar y operacionalizar lo que ya existe**, que es un proyecto de semanas.

## 13. El modelo educativo chico y especializado empieza a discutirle al genérico grande (agregado 2026-09-30, pase 5)

`OmniEdu` (Universidad de Pekín + UCAS + Zhongguancun Academy, septiembre 2026) publica una familia de modelos fundacionales para K-12 en **4B, 9B y 27B**, con el corpus de instrucciones abierto (69.999 ejemplos, 15,96M tokens supervisados de 100+ fuentes) organizado en cuatro capacidades: competencia en la materia, anclaje curricular, razonamiento diagnóstico y acción pedagógica/andamiaje.

El número que importa: según el paper, **OmniEdu-27B alcanza 78,74% en el setting Scaffold de MathTutorBench**. Un modelo de 27B especializado compitiendo en tareas pedagógicas con genéricos mucho más grandes.

**Por qué es una tendencia con consecuencia comercial directa.** En un despliegue a escala de sistema educativo —un ministerio, un estado, una red de distritos— la variable que decide no es la calidad marginal sino el **costo por alumno de inferencia**. Un modelo de 4B–27B que se puede correr on-premise cambia el orden de magnitud de esa cuenta, y además resuelve de paso los dos problemas que la KB ya tiene documentados: **soberanía de datos** (APAC y EMEA) y **operación con conectividad pobre** (LATAM rural, África).

⚠️ **Y el artefacto concreto no es usable:** `haolpku/Omni-Edu` **no declara licencia** y sus pesos heredan la licencia de las bases Qwen. La tendencia es real y el repo no es un componente. Lo aprovechable es **la receta** —el corpus y las cuatro capacidades están descritos— para entrenar un modelo propio con currículo del cliente. Esa es la propuesta, no "desplegamos OmniEdu".

## 14. El agente educativo tiene un estándar de memoria desde hace una década y casi nadie lo usa (agregado 2026-10-01, pase 6)

Cada tutor LLM open source que esta KB registró en seis pasadas guarda el progreso del alumno en un esquema inventado por su autor. DeepTutor tiene memoria en tres capas propia. OpenTutor tiene la suya. Los cinco servidores MCP de mastery del pase 5 tienen cinco. Ninguno escribe en **xAPI**, que es un estándar **IEEE (9274.1.1)** con cuatro implementaciones open source maduras y quince años de despliegue en formación corporativa y militar.

La consecuencia no es estética. Un tutor con memoria propietaria:

- no puede entregarle el historial al LMS ni al SIS sin un ETL a medida,
- no deja evidencia auditable en el formato que un regulador o un auditor ya conoce,
- y obliga a rehacer la capa de datos en cada engagement.

**Dónde está el borde del cambio:** `learnmcp-xapi` (MIT, 15 ★) es el primer artefacto que le da a un agente tools MCP sobre un LRS conforme en vez de una tabla propia. Es chico —32 commits— pero marca la dirección correcta.

**Por qué es una tendencia y no una curiosidad técnica:** las tres presiones regulatorias que esta KB viene siguiendo —EU AI Act, mandatos distritales de EE. UU. con supervisión humana obligatoria, y ahora Vietnam clasificando la evaluación automatizada como alto riesgo— **piden exactamente lo que un LRS produce**: registro inmutable de qué decidió el sistema, cuándo y con qué evidencia. La adopción de xAPI en tutoría con AI va a venir empujada por cumplimiento, no por elegancia de arquitectura.

**Qué hacer con esto en una propuesta:** proponer el LRS como **capa 0**, antes del agente. Es barato (`lrsql`, Apache-2.0, corre sobre el Postgres que el cliente ya tiene), es estándar, y convierte "confíe en nuestro tutor" en "acá está el registro". Ver **P15**.

## 15. El submercado de tutores crece más lento que el mercado que lo contiene (agregado 2026-10-01, pase 6)

Dato del pase 6: **AI tutors es USD 2,7 B en 2026 y proyecta USD 17,7 B a 2033, CAGR 30,5%.** El agregado de AI en educación crece a ~35%. El producto más visible de la categoría es **el que crece por debajo del promedio de su propia categoría**.

Eso significa que el crecimiento está en las capas que no son el tutor: administración, analítica, evaluación, cumplimiento y telemetría. Y es justo donde esta KB viene documentando huecos de oferta open source pasada tras pasada — grading (gaps 6 y 9), SIS permisivo (gap 7, parcialmente resuelto), evaluación pedagógica adoptada en producción (gap 1), y ahora el estimador de mastery sobre LRS (gap 5).

**La conclusión de posicionamiento, y contradice el instinto:** entrar por el tutor es competir en el segmento más disputado (MagicSchool, Khanmigo, Duolingo, más los tutores chinos de 40k ★) y de menor crecimiento relativo. **Entrar por la capa que registra, mide y acredita es competir donde el mercado crece más rápido y la competencia open source es más débil o inexistente.** Todos los patrones de esta KB que venden esa capa —P4, P7, P10, P11, P14 y el nuevo P15— están mejor apuntados que P1.

## 16. La librería es MIT y los datos no: el cuello de botella del tutor adaptativo se movió de capa (agregado 2026-10-01, pase 7)

Las pasadas 4 a 6 construyeron un argumento coherente: `pyKT` es MIT, `pyBKT` es MIT, `lrsql` es Apache-2.0, `learnmcp-xapi` es MIT — por lo tanto el tutor adaptativo es **integración de piezas permisivas**, no investigación. El argumento es correcto sobre el código y estaba incompleto, porque **un modelo de knowledge tracing no se instala: se entrena.**

De los tres datasets de knowledge tracing que importan (ver `repos/foundations.md`):

- **EdNet** (131,4M interacciones, 784k alumnos, Corea) → **CC BY-NC 4.0**.
- **FoundationalASSIST** (1,7M interacciones, el único en inglés con respuestas reales y distractores, EE. UU.) → **CC BY-NC 4.0** *y* con acceso condicionado.
- **XES3G5M** (5,5M interacciones, China) → **MIT**, y es chino, de matemática y de tercer grado.

**O sea: el único dataset grande que se puede usar en un entregable facturado es también el menos aplicable.** La capa que parecía resuelta —modelado— lo está en código y no en datos.

**Lo que esto cambia en la práctica, y es una buena noticia disfrazada de problema.** Si no hay dataset público reutilizable, el modelo se entrena con los datos del cliente. Y entonces **el Learning Record Store deja de ser una pieza de conformidad y pasa a ser la pieza que hace posible el producto**: es lo que genera el histórico. El pase 6 vendía el LRS como expediente auditable ante un regulador; el pase 7 le agrega un argumento comercial que no depende de ninguna regulación. **El LRS va en la fase 1 porque sin él el arranque en frío no termina nunca.** Ver **P16**.

**Y la lección de método, que es transversal a esta KB:** verificar la licencia del repo dejó de ser suficiente. Hay que verificar la licencia de **los datos con que ese repo se vuelve útil**. Es una capa que ninguna de las seis pasadas anteriores había mirado.

## 17. La ola regulatoria de APAC dejó de ser Corea del Sur sola (consolidado 2026-10-01, pase 7 — el hallazgo es del pase 6)

⚠️ **Nota de atribución, porque importa para no contar dos veces el mismo hallazgo:** este trend **no es un descubrimiento del pase 7**. Las tres jurisdicciones ya estaban registradas en `intel/market.md` por el **pase 6**. El pase 7 las encontró de forma independiente en búsqueda regional, confirmó las fechas, y las trae acá por una razón de estructura: **`intel/trends.md` seguía teniendo sólo el trend 10 ("Corea del Sur ya tiene en vigor el régimen que Europa todavía no aplica"), que presenta a Corea como excepción cuando ya es regla.** Lo que sigue corrige esa formulación.

| Jurisdicción | Instrumento | Vigencia | Qué dice sobre educación |
|---|---|---|---|
| **Corea del Sur** | AI Basic Act | **2026-01-22** | Marco integral (trend 10) |
| **Taiwán** | Basic Law on Artificial Intelligence | **2026-01-14** | Ley marco vigente, no borrador |
| **Vietnam** | Ley nacional de AI, sancionada **dic. 2025** | **marzo 2026** | **Alto riesgo en seis sectores, uno es educación** — nombra explícitamente **evaluación automatizada** y **monitoreo de comportamiento** |

**El trend 10 queda corregido en su encuadre:** Corea no es el país que se adelantó, es el primero de tres. Y mientras eso pasaba, **Europa corrió el Annex III a 2027-12-02** (trend 11). La consecuencia es contraintuitiva y conviene decirla sin rodeos: **a fines de 2026, la obligación de conformidad para un tutor agéntico es exigible antes en APAC que en la UE.**

**Por qué Vietnam es el caso que más pesa de los tres.** Nombra *evaluación automatizada* y *monitoreo de comportamiento*, que son las dos funciones que un tutor agéntico implementa sin proponérselo: calificar y observar al alumno para adaptarse. No es una categoría de riesgo que se pueda esquivar con una decisión de diseño; es la descripción del producto.

**La contradicción que es la oportunidad, ya medida en `intel/market.md`:** tres leyes vigentes, y **sólo el 10%** de las instituciones de un relevamiento de 450+ en APAC tiene lineamientos formales, con **93%** de los educadores diciendo que hacen falta regulaciones. Obligación legal arriba, capacidad de cumplirla ausente abajo.

**Para el patrón P5** eso significa que la orquestación multi-jurisdicción deja de ser un patrón para grupos regionales multinacionales y pasa a ser **el patrón por defecto de cualquier despliegue APAC serio**: el mismo tutor tiene que demostrar conformidad bajo tres regímenes con calendarios distintos, ante un comprador con menos capacidad instalada que su par europeo para producir ese expediente solo.

## 18. La accesibilidad dejó de ser una característica y pasó a ser condición de acceso al mercado (agregado 2026-10-01, pase 8)

Las seis obligaciones regulatorias que esta KB viene siguiendo —EU AI Act, Corea, Vietnam, los mandatos estatales de EE. UU., el Digital Omnibus, el Decreto 83 chileno— tienen algo en común: **regulan cómo se usa la AI**. El **European Accessibility Act** es de otra clase y la KB no lo tenía: no regula la AI, **regula la plataforma**, y alcanza a cualquiera que ofrezca e-learning o un LMS en la UE.

Lo que lo hace distinto de todo lo demás de esta lista:

- **La fecha ya pasó.** En vigor desde el **2025-06-28**. No hay período de gracia que esperar, a diferencia del Annex III del AI Act.
- **Es binaria, no graduada.** Referencia técnica **WCAG 2.1 AA**. Se cumple o no se cumple; no hay «enfoque basado en riesgo» que module la obligación.
- **Alcanza por mercado, no por domicilio.** Una empresa fuera de la UE que sirva usuarios de la UE está adentro — el mismo mecanismo extraterritorial del GDPR.
- **El presupuesto ya existe.** Vive en cumplimiento y en compras, no en innovación. Es la diferencia práctica con la evaluación pedagógica, que hay que explicar antes de venderla.

**Y la oferta open source que lo resuelve no es educativa**, que es por qué siete pasadas de esta KB no la encontraron. `accessibility-agents` (**MIT, 419 ★, 374 commits**) revisa WCAG 2.2 AA desde adentro de Claude Code, GitHub Copilot, Codex y Gemini CLI, sobre código y sobre documentos — PDF y ePub incluidos, que es donde vive el material didáctico. Tiene más tracción que cualquier pieza de educación especial registrada en el pase 8 y que casi toda la capa de evaluación pedagógica.

**La lectura de negocio, y es contraintuitiva respecto del resto de la KB.** Los diecisiete trends anteriores empujan hacia el tutor, el modelado y la medición — territorio disputado, con incumbentes de 40k ★ en APAC. Este empuja hacia un trabajo que **no tiene incumbente open source, no tiene que desplazar a nadie, tiene obligación legal vigente y partida presupuestaria asignada**. Es el trabajo menos glamoroso y el de ciclo de venta más corto. Ver el patrón **P17**.

⚠️ **Lo que no hay que confundir, y es la mitad del trend.** WCAG mide **acceso técnico**: que el lector de pantalla llegue, que el contraste alcance, que el teclado navegue. **No mide si el contenido es comprensible para un alumno con discapacidad cognitiva.** Esa segunda mitad no tiene oferta open source — es el **gap 12** — y es la que un cliente de educación especial realmente pide. Venderlas juntas es prometer de más; venderlas en ese orden es un camino.

## 19. Los estándares de interoperabilidad educativa siguen siendo obligatorios y su código de referencia se está retirando (agregado 2026-10-01, pase 9)

Es el trend más incómodo de esta KB porque va en contra de la dirección que llevan los dieciocho anteriores. En todas las
capas anteriores la historia era *aparece oferta open source nueva*. Acá la historia es **se retira oferta open source que
existía**, y los estándares que esa oferta implementaba siguen siendo condición de compra institucional.

Verificado URL por URL el 2026-10-01:

| Qué era | URL que la documentación del sector sigue citando | Estado |
|---|---|---|
| **Badgr**, la implementación de referencia de Open Badges | `concentricsky/badgr-server` | **404**, y la búsqueda de repos de la organización por `badgr` devuelve *«No repositories matched your search»*. La organización verifica hoy el dominio **`instructure.com`**: Badgr → **Canvas Credentials** → **Parchment Digital Badges** |
| **caliper-php**, cliente oficial de Caliper Analytics | `1EdTech/caliper-php` | **404.** Causa nombrada por el fork de la **Universidad de Michigan**, textual: *«This had been archived, but has been unarchived following 1EdTech making its caliper-php private.»* |
| **caliper-python**, Sensor API de referencia | `IMSGlobal/caliper-python` | **404** |
| **European Digital Credentials** (Issuer/Viewer/Wallet) y **European Learning Model** | `european-commission-empl/*` | **Archivados** (2024-02-02 y 2024-02-14, EUPL-1.2), con aviso de mudanza a `code.europa.eu` — fuera de GitHub |

**El rigor que corresponde:** un 404 no distingue borrado de renombrado de privado. Lo afirmado es que **las URL no
resuelven**, con una señal independiente en `badgr-server` y la causa nombrada por un tercero en `caliper-php`.

**Lo que esto significa, y es lo vendible.** La obligación de interoperar no se fue con el código. El cliente que compra
credenciales digitales o analítica de aprendizaje conforme sigue necesitando **OB 3.0, QTI, OneRoster y Caliper**. Lo que
cambió es de dónde sale la implementación: ya no del organismo de estándares ni del vendor de referencia, sino de
**terceros certificados** (`amp-up-io/qti3-item-player`, MIT, con certificación de conformidad de 1EdTech),
**consorcios universitarios** (`digitalcredentials/*`, MIT) y **forks de universidad** (`caliper-php-public`, LGPL-3.0).

**El corolario de método, que vale para cualquier propuesta de esta capa:** acá **la señal de calidad no son las
estrellas**. El repo más estrellado de la capa (205 ★) es **una especificación, no código**; el de más commits (22.533)
es **GPL-2.0**; el único con **certificación de conformidad** tiene **30 ★**; y el emisor OB 3.0 más completo tiene
**404 commits y 1 estrella**. Se elige por conformidad y por licencia leída en el archivo. Ver **P21**.

## 20. La credencial es la vía por la que la formación profesional entra por fin a esta KB (agregado 2026-10-01, pase 9)

El **gap 10** lleva tres pasadas diciendo que la formación profesional no tiene *nada* open source con tracción: ni
plataforma, ni agente, ni benchmark. Cero de tres. Eso sigue siendo cierto **si se busca «plataforma de FP»**.

Buscando por el instrumento que la FP realmente usa —la **microcredencial**— el segmento no está vacío: tiene estándar
(**Open Badges 3.0 / W3C VC**), tiene vocabulario de competencias (**ESCO/ISCO**), tiene implementaciones **MIT** de
emisión, verificación y billetera, y tiene demanda medida. **46% de las instituciones de LATAM y el Caribe ya ofrecen
microcredenciales.** Y los tres obstáculos declarados del segmento son **estandarización (82%)**, **preparación
institucional (76%)** y **reconocimiento formal (71%)** — los tres se atacan con conformidad al estándar.

**Política pública que lo empuja, por región.** En **APAC**: Filipinas tiene microcredenciales en TVET vía **TESDA** y un
marco de la **CHED** en consulta pública; el consorcio **MICROCASA** articula España, Italia, Indonesia, Malasia y
Filipinas. En **EMEA**: el stack de credenciales es política europea (Europass/EBSI) y hay un **Micro-credentials
Masterclass** (Ámsterdam, 24–26 de febrero de 2026) con reguladores y proveedores de FP; **AI4VET**, Erasmus+ KA210-VET
2026, publica un curso de upskilling docente abierto probado en Portugal y Rumania. La **OCDE** publicó un informe sobre
desarrollar FP con AI, de mapeo de competencias a redacción asistida de currículo.

**Cómo reformula el gap 10 sin cerrarlo.** El gap era «no hay oferta». La formulación correcta es: **la oferta existe en
la capa de acreditación y no en la capa de aprendizaje**. Para un cliente de FP, el producto defendible hoy no es un
tutor de oficios —eso sigue sin existir— sino **acreditar de forma verificable y reconocible lo que el cliente ya
enseña**. Es un alcance más chico, más barato y mucho más vendible. Ver **P19**.

## 21. El fin del período gratuito de AI del incumbente abre una ventana de compra, y se cerró ayer (agregado 2026-10-01, pase 9)

🔴 **No verificado de primera mano — leer la advertencia antes de usarlo con un cliente.**

Según resultados de búsqueda concordantes, **Instructure** lanzó **IgniteAI Agent** para Canvas el **2026-03-15**,
construido sobre **Amazon Bedrock**: arma módulos, diseña páginas, genera rúbricas, revisa discusiones y organiza flujos
de trabajo docentes y administrativos. Y reestructuró Canvas en tres niveles —**Canvas Core, Canvas Plus y Canvas
Next**— donde las capacidades agénticas avanzadas viven en los dos de arriba.

**El dato con fecha:** el acceso gratuito a las funciones avanzadas (IgniteAI Grading Assistance y IgniteAI Agent)
terminó el **2026-06-30 en EE. UU.** y el **2026-09-30 en el resto del mundo**. Después hace falta subir a Canvas Plus o
Canvas Next.

**Hoy es el 2026-10-01.** Si el dato es correcto, la ventana se cerró **ayer** a nivel mundial, y hay una población de
instituciones que acaba de descubrir que la AI que venía usando sin costo ahora es una línea de presupuesto. Eso es un
momento de conversación —no un argumento de reemplazo del LMS, que nadie quiere— sobre **qué parte de esa capacidad se
puede cubrir con piezas MIT al lado del Canvas que ya tienen**: P8 para material docente, P14 para corrección sin que
califique el modelo, P20 para evaluación conforme por LTI.

**Y el hilo que conecta este trend con el 19, que es lo más interesante:** el mismo vendor que acaba de poner su AI
detrás de un nivel de pago es el que absorbió **Badgr**, la implementación de referencia de Open Badges que hoy devuelve
404. **La capa de credenciales y la capa de AI del mismo incumbente se cerraron en la misma ventana de tiempo.** Para una
propuesta, ese es un argumento de soberanía, no de precio.

⚠️ **Por qué está marcado como no verificado.** Los tres sitios con el detalle —`constellationr.com`, `nasdaq.com` y
`aijourn.com`— están **bloqueados por el proxy de egreso de esta sesión**. Fechas, nombres de niveles y condiciones
vienen de texto de resultados de búsqueda concordantes entre sí, **no de leer la fuente**. Es el dato más accionable del
pase y el peor verificado: **confirmarlo en el anuncio oficial de Instructure antes de llevarlo a un cliente.**

## 22. La licencia del contenido no es la licencia del código, y en educación abierta casi nunca coinciden (agregado 2026-10-01, pase 10)

Nueve pasadas de esta KB leyeron la licencia **del software**. El contenido curricular tiene **su propia licencia**, y es la
que decide si un entregable se puede facturar. Verificado en este pase contra el archivo `LICENSE`:

| Artefacto | Licencia declarada | Nivel de la página |
|---|---|---|
| `openstax/osbooks-calculus-bundle` | **CC BY-NC-SA** | `LICENSE` |
| `openstax/osbooks-biology-bundle` | **CC BY-NC-SA** | `LICENSE` |
| `openstax/osbooks-college-physics-bundle` | **CC BY-NC-SA** | `LICENSE` |
| `CAHLR/OATutor` (cura problemas de Calculus Volume 1) | **CC BY 4.0** | README |
| `pythpythpython/openstax-mcp-server` | **CC BY 4.0** | README |

**Las dos condiciones del lado NC-SA pegan exactamente donde duele:** *NonCommercial* prohíbe el uso en un entregable
facturado, y *ShareAlike* obliga a licenciar la derivación igual — o sea, a abrir el corpus construido para el cliente.

**Lo que el trend afirma** es que **la fuente secundaria y el README son sistemáticamente menos confiables que el archivo
`LICENSE`**, y que en la capa de contenido la diferencia cambia la viabilidad comercial del proyecto. **Lo que no afirma** es
cuál de las dos licencias de OpenStax es la vigente: `openstax.org` está bloqueado por el proxy (gap 17).

**La regla, y es barata:** el README de OATutor dice dónde está la respuesta — la licencia se declara **por ítem**, dentro de
cada JSON. Se lee el ítem, se guarda el campo junto al dato, y **el manifiesto de licencias es el entregable** (**P22**).
Corolario: **un corpus mezclado es del color de su ítem más restrictivo**, no del promedio.

**Es la tercera vez que esta KB encuentra el mismo patrón en tres capas distintas:** pase 7, los datasets de knowledge
tracing son NonCommercial; pase 8, la tecnología asistiva madura es copyleft; pase 10, el contenido es NC-SA y **el metadato
del catálogo también** (gap 16). **El riesgo de licencia en educación no está en el código: está en todo lo que el código
necesita para funcionar.**

## 23. Las estrellas de GitHub esconden la infraestructura educativa que está realmente desplegada (agregado 2026-10-01, pase 10)

Hallazgo de método, y es el que más cambia cómo se construye esta KB. Nueve pasadas ordenaron por estrellas. Con ese orden,
**la plataforma educativa más grande del mundo era invisible**.

| Repo | Stars | Forks | Commits | Forks/Stars |
|---|---|---|---|---|
| `Sunbird-Ed/SunbirdEd-portal` (sostiene DIKSHA, 180 M+ alumnos) | **41** | **317** | **38.046** | **7,7×** |
| `project-sunbird/sunbird-devops` | 62 | **392** | — | **6,3×** |
| `Sunbird-Ed/SunbirdEd-consumption-ngcomponents` | 3 | 64 | — | **21×** |
| `DSpace/DSpace` | 1.1k | **1.5k** | **25.385** | 1,4× |
| `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` | 28 | 47 | 1.053 | 1,7× |
| `HKUDS/DeepTutor` (comparación) | **40,6k** | — | — | ≪1 |

**La explicación es el modelo de adopción, no la calidad:** en infraestructura pública **el fork es la unidad de
despliegue**. Cada estado indio forkea Sunbird para levantar su instancia; cada distrito forkea Ed-Fi. La estrella mide
*atención de desarrolladores*; el fork mide *organizaciones que lo pusieron en producción*. **Son métricas de cosas
distintas, y para vender a un ministerio importa la segunda.**

**Un proyecto con 38.046 commits y 41 estrellas no está muerto: nadie lo mira y todo el mundo lo usa.**

**La regla operativa para esta KB:** en las capas de **plataforma institucional, estándar e infraestructura pública**,
ordenar por **forks y commits**, no por estrellas. Es hermana de la regla del pase 6 (*si un gap sobrevive, revisar el
nombre que no se está usando*) y del criterio del pase 9 (*en credenciales se elige por conformidad certificada, no por
popularidad*). **Las tres dicen lo mismo: el indicador por defecto de GitHub mide mal lo institucional.**

## 24. Hay una tercera vía para la plataforma de sistema educativo nacional, y es permisiva (agregado 2026-10-01, pase 10)

Hasta este pase, la respuesta de esta KB a «plataforma para un ministerio» era **Moodle** (GPL-3.0) u **Open edX**
(AGPL-3.0): las dos copyleft, con el agente obligado a vivir afuera o a asumir obligación de apertura. **Sunbird** cambia eso:
**MIT**, microservicios (contenido, autenticación, rutas de aprendizaje, analítica, notificaciones), app Android con consumo
**offline**, reconocida **Digital Public Good** por la DPGA, y **38.046 commits** de trabajo acumulado.

**Y en North America el equivalente de la capa de datos ya es permisivo también:** **Ed-Fi** pasó de licencia propietaria a
**Apache-2.0 en abril de 2020**, y con ese cambio sus repos privados se hicieron públicos.

**La consecuencia para el posicionamiento, que es lo vendible:** el argumento de «open source para soberanía educativa» dejó
de tener la contradicción de licencia que tenía. Antes había que explicarle a un ministerio que la plataforma abierta que le
proponíamos lo obligaba a publicar sus modificaciones. **Con Sunbird y Ed-Fi no.** Ver **P23** y **P24**.

## 25. El Digital Omnibus dejó de ser propuesta y es derecho vigente: el Anexo III vence el 2027-12-02 (agregado 2026-10-01, pase 11)

La tendencia 11 (pase 4) ya registró que el Digital Omnibus entró en vigor el 2026-07-27 y que corrió la mitad cara
del AI Act dejando corriendo la barata. **Esa lectura se confirma y no se corrige.** Lo que este pase agrega es lo
que faltaba para poder citarlo en un documento de cliente: **el número de reglamento, la cronología legislativa
completa y los artículos modificados.**

**Reglamento (UE) 2026/1744** — *Digital Omnibus on AI*:

| Hito | Fecha |
|---|---|
| Propuesta de la Comisión Europea | **2025-11-19** |
| Aprobación del Parlamento Europeo | **2026-06-16** |
| Adopción final del Consejo | **2026-06-29** |
| **Entrada en vigor** | **2026-07-27** |

Modifica, entre otros, los artículos **9, 17, 18, 28, 43 y 50** del Reglamento (UE) 2024/1689, y también el
Reglamento (UE) 2018/1139 (seguridad aérea) y el 2023/1230 (máquinas).

**Lo que se movió y lo que no:**

| Obligación | Antes | Ahora |
|---|---|---|
| **Anexo III alto riesgo *stand-alone*** — incluye evaluación de resultados de aprendizaje, screening de postulantes y monitoreo de exámenes | 2026-08-02 | **2027-12-02** |
| Alto riesgo embebido en productos regulados | 2027-08-02 | **2028-08-02** |
| **Prácticas prohibidas**, entre ellas el **reconocimiento de emociones en instituciones educativas** | vigente | **vigente, sin cambio** |
| **Alfabetización en AI** (art. 4) | desde 2025-02-02 | **vigente, sin cambio** |

**Por qué esto no es "hay más tiempo" sino lo contrario, comercialmente.** 16 meses de corrimiento sobre la mitad
cara del expediente es exactamente el plazo en que un comprador institucional aprueba y contrata un programa de
conformidad. Antes del Omnibus, la fecha estaba tan encima que el comprador la trataba como imposible y la ignoraba;
ahora es alcanzable, y por lo tanto exigible internamente. **La ventana de compra se abrió al correrse la fecha, no
se cerró.** Y lo que ya es exigible —prohibiciones y alfabetización— sigue siendo la puerta de entrada barata al
mismo cliente. Ver **P4** y el patrón nuevo **P25**.

🔴 **Nivel de evidencia:** verificado en **múltiples fuentes legales secundarias independientes y coincidentes**
(firmas de abogados y publicaciones de cumplimiento que citan el número de reglamento, las fechas de votación y las
nuevas fechas de aplicación). **El texto primario no se leyó:** `eur-lex.europa.eu` y
`digital-strategy.ec.europa.eu` están bloqueados por el proxy de egreso de esta sesión. **Confirmar en EUR-Lex antes
de poner la fecha en un documento de cliente.**

## 26. La capa que decide sobre el alumno es la más regulada del sector y la peor abastecida de open source (agregado 2026-10-01, pase 11)

Once pasadas de esta KB describieron capas con oferta chica. **Esta es distinta: acá la oferta no es chica, es
inexistente, y se puede demostrar con dos consultas.**

| Consulta en GitHub, 2026-10-01 | Resultado | Techo de estrellas |
|---|---|---|
| `topic:learning-analytics stars:>50` | **2 repos en todo GitHub** | 169 ★, y es un blog de notas de papers |
| `dropout prediction student license:mit pushed:>2026-01-01` | **110 repos** | **6 ★** |

El único repo real del primer resultado es **`OpenLRW`** (62 ★), que almacena datos y no predice nada. El tope del
segundo entrena con **datos sintéticos**. Y el stack institucional que esta capa tuvo —la **Apereo Learning
Analytics Initiative**— está archivado: `OpenLRS` dice `Deprecated` en su descripción, `OpenDashboard-legacy` dice
`(Deprecated)`, el reemplazo (`-ux` y `-api`) **se creó el 2020-02-12 y se abandonó dentro del mes**, y
*Student Success Plan* —el producto de advising con despliegues reales— **no tiene repositorio localizable** desde
alrededor de 2015.

**La asimetría que hay que leer.** En todas las capas anteriores de esta KB, la ausencia de open source coincidía con
ausencia de demanda o con demanda incipiente. Acá no: *student success* es **categoría de compra consolidada**, con
incumbentes propietarios y presupuesto asignado en cada universidad. **Es la única capa de esta KB donde la demanda
está madura, el presupuesto existe, y la oferta open source es cero.**

**Y la segunda asimetría, que es la útil:** el cuello de botella **no es el dato**. Los dos corpus canónicos de la
capa —**OULAD** (32.593 alumnos, 10.655.280 registros de clicks, The Open University) y **UCI 697** (4.424 × 36,
Portugal)— son **CC BY 4.0, con uso comercial permitido**. Es lo contrario del diagnóstico del gap 11 para knowledge
tracing, y la conclusión de una capa no se puede exportar a la otra. **Acá falta el software y falta quien lo
mantenga: las dos cosas que una consultora vende.**

Una nota técnica que vale para la propuesta: el benchmark de supervivencia sobre OULAD (arXiv 2604.08870, Eastern
University) reporta que, en ablación y explicabilidad, **la señal predictiva dominante es temporal y conductual, no
demográfica ni estructural**. Es el argumento que hace aprobable un sistema de riesgo ante un DPO o un comité de
ética: **se puede predecir sin apoyarse en atributos protegidos.** 🔴 Sin verificar de primera mano (`arxiv.org`
bloqueado) y las fuentes reportan que el link al repositorio del paper está roto.

## 27. ECL-2.0: una licencia permisiva que los filtros de licencia descartan por desconocida (agregado 2026-10-01, pase 11)

**Esta tendencia es un error propio documentado, y por eso es la más reutilizable del pase.** Diez pasadas de esta KB
filtraron por **MIT / Apache-2.0 / BSD** y, al hacerlo, descartaron en silencio el stack completo de la **Apereo
Foundation**, que licencia con **ECL-2.0 (Educational Community License 2.0)**.

**Qué es ECL-2.0, con precisión:** Apache-2.0 con **una** modificación — el alcance de la concesión de patentes de la
sección 3, acotado a la contribución en vez de a las combinaciones. Salió del *Licensing and Policy Summit*
convocado por la comunidad académica en 2006, porque las universidades no podían conceder el paquete amplio de
Apache-2.0 sobre código escrito con fondos de investigación. **Aprobada por OSI y por la FSF. No es copyleft.** El
propio README de `LearningAnalyticsProcessor` la describe como *"a slightly less permissive Apache2"*.

**Lo que el filtro dejaba afuera:** `sakaiproject/sakai` (**1.234 ★**, 1.014 forks, push del 2026-09-30, dos ramas
mantenidas), `opencast/opencast` (**505 ★**, la única capa de video de clase open source a escala),
`Apereo-Learning-Analytics-Initiative/OpenLRW` (62 ★, el único artefacto de esta KB que habla xAPI, Caliper y
OneRoster a la vez). **Un LMS de educación superior de primera línea no apareció en diez pasadas por una línea de
licencia que nadie leyó.**

**La generalización, y es la parte que sirve fuera de educación.** Un filtro de licencias por lista blanca de nombres
produce falsos negativos silenciosos, y los falsos negativos de un filtro no dejan rastro: no hay forma de notar lo
que no apareció. **La regla correcta no es "MIT / Apache / BSD" sino "permisiva, aprobada por OSI, sin obligación de
publicar el derivado"** — y cuando aparece una licencia desconocida, se lee en vez de descartarse. En educación esto
pega más fuerte que en otros sectores, porque los sectores con fundaciones académicas tienen licencias propias:
educación tiene ECL, y es probable que haya equivalentes en salud e investigación que esta KB tampoco vio.

**La contracara honesta que hay que decirle al cliente:** la concesión de patentes más angosta es real. Para uso,
modificación, cierre del derivado y redistribución, ECL-2.0 se comporta como Apache-2.0 ✅. **Para un entregable con
cesión de patentes o un cliente con due diligence de patentes, es una pregunta de legal, no una respuesta.** ⚠️

## 28. La educación perdió el canal de distribución más barato de la industria, y la vertical científica se lo quedó (agregado 2026-10-01, pase 12)

El estándar **Agent Skills** —bundles de instrucciones, referencias y scripts que un agente carga sólo cuando la tarea
los pide, leídos por Claude Code, Codex, Cursor, Antigravity, Gemini CLI y Copilot CLI— es hoy la vía de distribución de
conocimiento de dominio con la barrera de entrada más baja que existe: **sin backend, sin despliegue, sin dependencias
que auditar.** Un repo de Markdown.

**Las once pasadas anteriores de esta KB midieron la educación contra sí misma.** Esta la mide contra otra vertical en
el mismo canal, y el resultado es el peor número registrado. Verificado contra la página de cada repo el 2026-10-01:

| Biblioteca | Vertical | Licencia | Stars | Contenido |
|---|---|---|---|---|
| `K-Dense-AI/scientific-agent-skills` | Ciencia | **MIT** ✅ | **47.200** | 181 skills + 100+ bases de datos + 70+ workflows. Declara 160.000 científicos usuarios |
| `virgiliojr94/book-to-skill` | Genérico | **MIT** ✅ | **33.200** | Pipeline documento → skill. **+6.300 ★ en 30 días** |
| `GarethManning/education-agent-skills` | **Educación** | CC BY-SA 4.0 ⚠️ | **815** | 165 skills pedagógicas en 20 dominios |
| `ZeKaiNie/universal-examprep-skill` | **Educación** | **MIT** ✅ | **299** | Tutor de examen con cita de página |

**58× contra el activo educativo más grande; 158× contra el mejor educativo empaquetable.**

**Y la asimetría de licencia es el núcleo de la tendencia, no un detalle.** El activo educativo más grande de la capa
es **CC BY-SA 4.0** —*share-alike*, el derivado hereda la obligación— mientras el científico equivalente es **MIT**. Es
decir: la vertical científica publicó su conocimiento como **software**, y la educativa como **obra cultural**. Las dos
decisiones son coherentes con su cultura de origen, y sólo una de las dos se puede empaquetar en un entregable cerrado.

**Por qué esto es una tendencia y no una anécdota de estrellas.** Las once pasadas anteriores documentaron que lo bueno
en educación es caro de desplegar (plataformas), copyleft (accesibilidad, pase 8), archivado (analítica institucional,
pase 11) o de licencia trampa (contenido OER, pase 10). **Este canal no tiene ninguno de esos problemas** y la
educación igual no lo ocupó. La conclusión incómoda: el retraso de la capa educativa no se explica por barreras
técnicas ni de licencia, porque acá no hay ninguna. Ver `agents/top.md` y el **gap 20**.

## 29. El patrón que se repite en cinco capas de esta KB: lo que inventa su propio modelo de dominio no escala, lo que se conecta al estándar instalado sí (agregado 2026-10-01, pase 12)

El pase 5 registró **cinco servidores MCP de mastery** y concluyó "cinco reinvenciones del mismo patrón", con techo de
**1 ★**. El pase 12 encuentra el término de comparación que faltaba:
**`ankimcp/anki-mcp-server` — MIT, 499 ★, 254 commits, v0.22.0.**

| Enfoque | Repos | Techo |
|---|---|---|
| **Inventar** el modelo de dominio (grafo propio, scheduler propio, esquema propio) | los 5 MCP de mastery del pase 5 | **1 ★** |
| **Exponer** el estándar ya instalado (Anki, AGPL-3.0, +3 M de usuarios sólo en Android) | `anki-mcp-server` | **499 ★** |

Son ~500× con la misma tecnología (MCP), la misma licencia permisiva y la misma ventana temporal. La diferencia es de
dónde está el modelo de dominio.

**Y el patrón ya había aparecido cuatro veces en esta KB sin que se lo nombrara:**

- **Pase 9, credenciales:** las implementaciones de referencia de los estándares se retiran (`badgr-server`,
  `caliper-php`, `caliper-python`) y **el estándar sigue obligatorio**. Lo que sobrevive es lo que habla el estándar,
  no lo que lo reimplementa.
- **Pase 10, infraestructura desplegada:** Sunbird (MIT) tiene **41 ★** y 180 M de alumnos. La adopción no vive en la
  estrella; vive en el despliegue.
- **Pase 11, analítica institucional:** de los 21 repos de Apereo el único vivo es **`OpenLRW`**, y es precisamente el
  que habla **xAPI + Caliper + OneRoster a la vez**. Los que inventaban dashboard propio están archivados.
- **Pase 12, FSRS:** el algoritmo moderno de repetición espaciada **ya está integrado en Anki desde la versión 23.10
  (2023)**. `py-fsrs` (MIT, en esta KB) sirve para razonar y simular del lado del servidor, **no para reimplantarlo**.

**La regla operativa que esto deja, y aplica a cualquier propuesta de esta KB:** antes de construir el motor de un
subsistema educativo —mastery, repaso, credencial, telemetría, datos de alumno— verificar si existe el estándar
instalado y si hay un puente hacia él. **El valor del studio está en el puente y en la pedagogía, no en el motor.**
Ver **P28**.

## 30. La capa donde el alumno efectivamente trabaja estaba fuera del mapa, y es la de mejor licencia de todo el sector (agregado 2026-10-01, pase 13)

Doce pasadas de esta KB construyeron el mapa desde el agente hacia afuera: el tutor, el modelado del conocimiento, la
evaluación, la seguridad, la telemetría, los datos, la accesibilidad, la credencial, el contenido, la predicción y la
distribución. **Nunca apareció el entorno donde el alumno escribe la respuesta** — y en educación superior STEM y
formación técnica ese entorno está estandarizado desde 2014.

Es **Jupyter**, y la pila completa es **BSD-3-Clause**: `jupyterhub` (8.300 ★), `jupyter-ai` (4.400 ★), `nbgrader`
(1.400 ★, **v0.9.6 del 2026-09-30**), `otter-grader` (161 ★, UC Berkeley DSEP) y `ltiauthenticator` (73 ★, LTI 1.3
probado contra Open edX, Canvas y Moodle). **14.334 ★, una sola familia de licencia.**

**Por qué es un trend y no sólo un hallazgo de catálogo.** Esta capa viola, sola, los cinco patrones estructurales que
esta KB documentó pase tras pase:

| Patrón documentado por la KB | Esta capa |
|---|---|
| Lo desplegable es copyleft (Moodle GPL, Open edX y Canvas AGPL) | **Permisiva de punta a punta** |
| Lo permisivo es pre-tracción (tutores LATAM 0–3 ★) | **8.300 ★ y despliegue universitario de una década** |
| Los datos de entrenamiento son NonCommercial (gap 11) | **No aplica**: la evidencia la produce el alumno del cliente |
| El runtime de agente con MCP hay que construirlo | **Ya existe, BSD, con ACP y MCP** |
| El contenido tiene trampa de licencia (pase 10) | **No aplica**: el artefacto lo escribe el docente |

**La lectura comercial es un cambio de orden de operaciones.** Esta KB venía proponiendo *construir* el agente y después
buscarle dónde enchufarlo. En cualquier cliente de STEM, ciencia de datos, ingeniería o formación técnica **la
infraestructura ya está instalada o es trivial de instalar, es permisiva, y el trabajo facturable es la capa pedagógica
encima** — feedback formativo sobre tests que ya corrieron, estimación de mastery, evidencia hacia el LRS. Eso es más
barato de vender y mucho más defendible que una plataforma nueva.

**Y la causa de los doce pases de ceguera es metodológica, no de disponibilidad.** Jupyter no se presenta como producto
educativo: se presenta como herramienta de cómputo científico. Buscar «agente educativo», «tutor», «LMS» o «grading» no
lo devuelve nunca. Es la quinta vez que esta KB registra que **la consulta equivocada costó pasadas** (ver la nota de
método del pase 7). La regla que queda: **buscar también por el artefacto material del alumno —el cuaderno, el
entregable, el entorno de ejecución— y no sólo por el rol del software.**

## 31. Vietnam puso en vigor lo que Europa posterga, y su texto nombra exactamente el patrón base de esta KB (agregado 2026-10-01, pase 13)

El **trend 10** registró que Corea del Sur ya tenía en vigor el régimen que Europa no aplicaba, y el **trend 17**
consolidó que «la ola regulatoria de APAC dejó de ser Corea del Sur sola». **Vietnam la extiende, y con el texto más
específico que esta KB encontró para educación.**

- La **Ley de Inteligencia Artificial** fue aprobada por la Asamblea Nacional el **2025-12-10** y está **en vigor desde
  el 2026-03-01**. Es la primera ley integral y autónoma de AI del país, de enfoque **basado en riesgo**.
- El Gobierno publicó una **lista sectorial de 46 sistemas de AI de alto riesgo en seis sectores**, y **educación es uno**.
- En educación, alto riesgo incluye explícitamente tres cosas: **(a)** sistemas que entregan contenido de
  autoaprendizaje **a partir de fuentes de datos no controladas**; **(b)** sistemas que **evalúan, califican o rankean
  alumnos automáticamente**; **(c)** sistemas que **monitorean o analizan la conducta del alumno con datos biométricos**
  —reconocimiento facial, seguimiento de mirada—.
- Obligaciones: **evaluación de conformidad antes del despliegue** (y después de cada modificación significativa),
  documentación técnica, gestión de riesgo a lo largo del ciclo de vida, **supervisión humana** y transparencia. Para
  ciertos sistemas designados la evaluación **debe hacerla un organismo registrado o reconocido**; para el resto se
  admite autoevaluación del proveedor.
- **Las dos fechas que hay que llevar a una propuesta:** los sistemas de educación **ya en operación antes del
  2026-08-15** tienen período transitorio con vencimiento **2027-09-01**.

**Por qué esto reordena el reloj regulatorio de esta KB.** El vencimiento educativo de Vietnam (**2027-09-01**) cae
**antes** que el del Anexo III europeo (**2027-12-02**, trend 25). Por tercera vez, **APAC exige antes que EMEA** — y
esta vez con un texto más explícito que el europeo sobre qué arquitectura queda alcanzada.

**Y acá está el punto que ninguna otra regulación de esta KB había escrito.** El inciso (a) —contenido de
autoaprendizaje **desde fuentes de datos no controladas**— es, literalmente, la descripción de un **tutor RAG sobre
corpus abierto**, que es el **patrón P1** de esta KB y lo que el pase 10 documentó al abrir la capa de contenido
curricular. En Vietnam eso no es una buena práctica: **es la condición que mete al sistema en alto riesgo**. El
entregable que el pase 10 inventó para un problema de licencia —el **manifiesto de procedencia por ítem** del patrón
**P22**— resulta ser también el expediente que vuelve demostrable el control de la fuente. **El mismo artefacto sirve
para dos obligaciones distintas en dos regiones distintas**, y eso lo vuelve mucho más fácil de justificar.

El inciso (c), de paso, confirma el diagnóstico del pase 8 sobre proctoring: **la vigilancia biométrica del alumno queda
en alto riesgo también en Vietnam.** Van tres jurisdicciones (EU Anexo III, Corea, Vietnam) donde la categoría entera
nace con expediente de conformidad obligatorio.

## 32. LATAM dejó de tener un problema de adopción y tiene uno de gobernanza, y ahora hay número institucional (agregado 2026-10-01, pase 13)

El pase 4 de esta KB trajo la encuesta del Digital Education Council (92% de estudiantes y 79% de docentes de LATAM
usando AI) y concluyó que **«la región no tiene un gap de adopción; tiene un gap de oferta open source propia»**. Ahora
hay una medición institucional, de fuente multilateral, que precisa **dónde** está el déficit.

**UNESCO IESALC, publicado el 2026-09-09 durante la UNESCO Digital Learning Week 2026**, sobre **200 instituciones de
educación superior de 19 países** de América Latina y el Caribe:

| Indicador | Valor |
|---|---|
| Instituciones que usan AI en al menos un área | **87%** |
| Que la usan en enseñanza y aprendizaje | **74%** (mayormente con herramientas de propósito general: ChatGPT, Copilot, Gemini) |
| Que la usan para análisis de datos e investigación | **57%** |
| **Que tienen una estrategia formal de AI** | **26%** |

Y el estudio señala la causa de la brecha: **el uso lo empujan docentes, investigadores y estudiantes, no las políticas
institucionales.** Es adopción de abajo hacia arriba, sin marco.

**La brecha 87 → 26 es el dato comercial del pase**, y conviene leerla junto con la cifra comparativa del pase 8: **~70%
de las instituciones de Europa y North America tienen o están desarrollando guías de AI, contra 45% en América Latina y
el Caribe.** La región no está atrasada en uso —está por encima de varias—; **está atrasada en gobernanza, que es
precisamente lo que se contrata.**

**Qué vende esto, concretamente.** No una plataforma: **un marco de gobernanza de AI institucional con inventario de uso
real.** El 87% que ya usa AI con herramientas de propósito general significa que en esas 200 instituciones hay *shadow
AI* docente sin registrar, sin política de datos y sin criterio de evaluación. El primer entregable no es un tutor: es
el **inventario + la política + el criterio de evaluación pedagógica** (patrones **P10**, **P11** y **P13**). Es un
proyecto corto, repetible en 19 países, y es la puerta de entrada al resto.

## Gaps declarados

Huecos confirmados tras buscar, no ausencias por no haber buscado. Un gap informado es información; el silencio se parece demasiado a la cobertura.

1. ~~**No hay evaluador pedagógico open source con tracción.**~~ → **GAP REFORMULADO en el pase 4 del 2026-09-30.** Los pases 1–3 registraron un solo evaluador, `AITutor-EvalKit` (MIT, MBZUAI, **3 ★**), y concluyeron que "no existe el LegalBench de educación". **La medición estaba mal hecha y la conclusión era más fuerte de lo que los datos permitían.**

   Lo que hay, verificado en el pase 4:

   - **`UnifyingAITutorEvaluation`** (https://github.com/kaushal0494/UnifyingAITutorEvaluation, CC BY-SA 4.0, **32 ★**) — **del mismo autor que `AITutor-EvalKit`**. Es el repo canónico: taxonomía de **8 dimensiones** pedagógicas y el dataset **MRBench** en tres versiones (V1 192 diálogos × 8 dim., V2 200 × 8, V3 300 × 4). **NAACL 2025, Senior Area Chair Award.** La KB había registrado el repo chico del mismo trabajo.
   - **`MathTutorBench`** (https://github.com/eth-lre/mathtutorbench, CC BY 4.0, **42 ★**) — no estaba en la KB. 3 habilidades docentes de alto nivel, 7 tareas, **reward models entrenados** para medir calidad de enseñanza y **leaderboard público**. **EMNLP 2025 (Oral).**
   - **`pyKT`** (MIT, **441 ★**) mide la otra mitad del problema: el estado de conocimiento del alumno, no la calidad de la respuesta del tutor.

   **La formulación correcta del gap:** el estándar **existe, está publicado en los dos venues principales de NLP, y nadie lo está usando en producción.** 42 y 32 estrellas para benchmarks premiados en EMNLP y NAACL es señal de que la academia los produjo y la industria no los adoptó. Eso sigue siendo una oportunidad — pero es "integrar y operacionalizar lo que ya existe", no "construir lo que falta", y son propuestas muy distintas. Ver el patrón **P10**.

   ⚠️ **Y hay que leer la licencia:** MathTutorBench es CC BY 4.0 y UnifyingAITutorEvaluation es **CC BY-SA 4.0** (*share-alike*). El uso típico en un engagement — derivar un benchmark propio con datos del cliente — es exactamente lo que dispara la obligación del share-alike.

   ~~**Lo que sigue sin existir:** un benchmark pedagógico **fuera de matemática**.~~ → **SUB-GAP CERRADO EN EL PASE 5 DEL 2026-09-30.** El pase 4 escribió que los tres artefactos eran de matemática y que "para lengua, ciencias sociales o formación profesional no hay nada". Buscando por *escenario educativo* en vez de por dominio aparecen tres más:

   - **`EduBench`** (https://github.com/ybai-nlp/EduBench, **MIT**, 29 ★, **ACL 2026**) — **transversal a materia por diseño**: organiza la evaluación en **9 contextos educativos** y 4.000+ situaciones sobre 12 dimensiones, con cinco escenarios de alumno y **cuatro de docente** (generación de preguntas, **Automatic Grading**, generación de material, contenido personalizado). Publica dataset y modelo.
   - **`EduGuardBench`** (https://github.com/YL1N/EduGuardBench, ⚠️ **sin licencia declarada**, 4 ★) — evalúa al modelo *como docente simulado*, lo cual es independiente de la materia. 14 modelos.
   - **`EduFrameTrap`** (arXiv 2605.14604, TUM/MCML) — **seis materias**: matemática, física, **economía, química, biología y ciencias de la computación**. Sin repo localizable.

   **Y el dato de licencia es la mejor parte:** `EduBench` y `SafeTutors` son **MIT**. Hasta el pase 4 toda la capa de evaluación pedagógica tenía fricción (CC BY, CC BY-SA con *share-alike*). Ahora se puede armar el stack de evaluación completo sin pasar por legal.

   ~~**Lo que sigue sin existir, más acotado:** benchmark pedagógico específico de **lengua, ciencias sociales o formación profesional**.~~ → **ACOTADO OTRA VEZ EN EL PASE 6 DEL 2026-09-30: cae *lengua*, quedan ciencias sociales y FP.**

   **`L2-Bench`** — *An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education* (arXiv 2607.08842), de **Oxford University Press** con la Universidad de Oxford. Según las fuentes localizadas: **1.000+ tareas docentes auténticas**, marco de **12 competencias docentes con 31 sub-habilidades**, rúbricas con descriptores expertos, y validación de **200+ educadores de 45+ países**. Código de evaluación **MIT ✅**; dataset y rúbricas **CC BY-SA 4.0 ⚠️**. Paper metodológico compañero: arXiv 2603.20088.

   🔴 **Marcado como no verificado, y es una diferencia importante respecto de todo lo demás de este pase.** El proxy de egreso de la sesión bloquea `arxiv.org`, `huggingface.co` y `oup.com` — los tres lugares donde vive L2-Bench. Licencia, tamaño y autoría vienen de resultados de búsqueda, **no de leer el artefacto**. Se registra porque un benchmark de segunda lengua producido por OUP con 200+ validadores es exactamente lo que el sub-gap pedía, y omitirlo sería peor que anotarlo con la advertencia; **pero hay que abrirlo y confirmarlo antes de cualquier entregable**.

   Si se confirma, hay algo más que anotar: **L2-Bench sería el primer benchmark de esta capa producido por una editorial educativa comercial y no por un laboratorio académico.** Eso importa para el diagnóstico central de este gap — significa que la medición pedagógica empezó a tener demanda de mercado y no sólo interés de investigación.

   **Lo que sigue sin existir, tercera acotación:** benchmark pedagógico de **ciencias sociales** y de **formación profesional** (ver el **gap 10**, nuevo en este pase, que mide el vacío de FP con números). Y el diagnóstico central del gap 1 **no cambia**: el estándar existe, está publicado en los venues principales, y sigue sin adoptarse en producción.

   **Medido otra vez en el pase 7 del 2026-10-01 — ciencias sociales no se cierra, y ahora se sabe por qué no se cierra solo.** Buscando el benchmark pedagógico de ciencias sociales aparece **`ProHist-Bench`**, dentro de **`ABench`** (https://github.com/inclusionAI/ABench, **Apache-2.0** ✅, 30 ★): **400 preguntas** núcleo en 4 tipos de tarea con **10.891 rúbricas redactadas por historiadores** sobre **9 dimensiones de capacidad** (extendida: 504 preguntas), sobre materiales del examen imperial chino. Paper: arXiv 2604.24690.

   **No cierra el sub-gap, y la distinción es exactamente la que este gap viene sosteniendo desde el pase 4:** ProHist-Bench mide si el modelo **sabe hacer investigación histórica**, no si **sabe enseñar historia**. Es un benchmark de dominio, no pedagógico — la misma diferencia por la que `MathTutorBench` no mide si el modelo resuelve la ecuación sino si andamía al alumno que no la resuelve.

   **Lo que sí aporta, y no es poco:** 10.891 rúbricas de expertos con licencia **Apache-2.0** es la pieza más cara de construir en cualquier evaluación. Para un engagement de humanidades sirve como **capa de exactitud factual** debajo de una capa pedagógica que hay que traer aparte (`UnifyingAITutorEvaluation` para la taxonomía, `SafeTutors` para el daño). Lo que no se puede es presentarlo como evaluación de enseñanza.

   ⚠️ **Y pega otra vez en el gap 4:** `inclusionAI` es la organización open source de **Ant Group** — verificado en el perfil (`inclusion-ai.org`, 68 repos). La única pieza de evaluación en humanidades con licencia limpia que encontró esta KB es, también, china.

   **Dos benchmarks de seguridad más en este pase, los dos sin repo localizable:** **EduZone** (arXiv 2608.02024, 2026-08-03, **KAIST** → APAC) — **6 categorías de riesgo y 28 subcategorías**, cubre **alumno y docente**, dataset de **2.600 prompts adversarios single-turn + 2.600 multi-turn**, y reporta que los guardrails existentes no cubren los riesgos específicos de educación ni el multi-turn dinámico; y **AIriskEval-edu** (arXiv 2607.01934), riesgo en explicaciones educativas mediadas por AI en K-12. 🔴 **Sin verificar de primera mano: `arxiv.org` sigue bloqueado por el proxy en este pase.**

   **Lo que sigue sin existir, cuarta acotación:** benchmark **pedagógico** de **ciencias sociales** y de **formación profesional**. El diagnóstico central del gap 1 **no cambia** en siete pasadas: el estándar existe, está publicado en los venues principales, y sigue sin adoptarse en producción.
2. **LATAM produce agentes educativos, pero ninguno sale de la fase cero.** *Refinado en el pase 2 del 2026-09-30: antes decía "cero repos".* Buscando explícitamente en español y portugués aparecen iniciativas reales y técnicamente ambiciosas — `H1bertto/professor-agent` (Brasil, MIT, **0 ★**) y `ANTONIOALGMAR/StudyAgent` (Brasil, **sin licencia**, 2 ★, tutor multimodal local completo sobre Ollama) — y **ninguna pasa de 2 estrellas**; una no tiene licencia, así que no es reutilizable. `studyield/studyield` **da 404**. Latam-GPT sigue siendo un modelo fundacional, no un framework de tutoría. La conclusión no cambia y el diagnóstico mejora: **no falta interés de constructores, falta masa crítica y gobernanza de proyecto** (empezando por poner una licencia). Espacio abierto, y ahora con evidencia de que hay gente intentándolo.

   **Actualizado en el pase 4 del 2026-09-30 — el gap baja de categoría.** Buscando en español apareció **TutorIA** (https://github.com/LabSirius/TutorIA, **MIT**, **0 ★**, Python): tutor conversacional autónomo **integrado dentro de Open edX**, con TTS, avatar animado, dashboard docente y persistencia de contexto, apuntado a **educación superior rural en Risaralda, Colombia**. Materias iniciales: Programación I e Introducción a la Matemática.

   Sigue teniendo **0 estrellas**, así que el gap de tracción se mantiene intacto. Lo que cambia son las **dos causas** que el pase 2 había identificado:

   | Diagnóstico del pase 2 | Estado en el pase 4 |
   |---|---|
   | "Falta gobernanza de proyecto, empezando por poner una licencia" | **Resuelto en este caso:** TutorIA es MIT |
   | "Falta respaldo institucional" | **Resuelto en este caso:** Grupo Sirius, **Universidad Tecnológica de Pereira** (`sirius.utp.edu.co`; el perfil de la organización declara Pereira, Colombia) |
   | "Falta masa crítica" | **Sin resolver.** 0 estrellas |

   **La lectura para un engagement LATAM:** dejó de ser cierto que la región sólo produce prototipos de autor individual sin licencia. Hay un laboratorio universitario colombiano publicando MIT e integrando contra Open edX, con un caso de uso específico (ruralidad, por eso el TTS y el avatar) en vez de un tutor genérico. **Como contraparte técnica local eso es utilizable hoy; como dependencia de producto no, y no hay que presentarlo como si lo fuera.**

   Y hay un dato de mercado del mismo pase que reencuadra el gap entero: la encuesta del Digital Education Council (30.000+ respuestas, 29 instituciones) da **92% de estudiantes y 79% de docentes de LATAM usando AI**. **La región no tiene un gap de adopción; tiene un gap de oferta open source propia.** Ver `intel/market.md`.

   **Medido otra vez en el pase 6 del 2026-10-01, y da lo mismo con más evidencia.** Búsqueda directa en GitHub en español (`tutor educativo IA`): **20 repos, ninguno pasa de 1 estrella.** Los más sustantivos, todos nuevos para esta KB y todos en fase cero:

   | Repo | País | Qué es | Stars |
   |---|---|---|---|
   | `dev-deivis/aprendia` | México | Tutor Flutter para **adultos en rezago educativo** que terminan primaria/secundaria vía **INEA**. Voz, avatar animado, y una decisión de diseño correcta: **guía en vez de dar la respuesta** | 0 |
   | `i-fretes/tutor-fpuna-ai` | Paraguay | Tutor de Aritmética y Álgebra para el ingreso a **FP-UNA**, con RAG y **verificación simbólica** del resultado. Creado 2026-09-25 | 0 |
   | `yago-jnp/kez.ia` | Brasil | Juez online + tutor de IA para Python y algoritmos: evalúa código, explica errores y personaliza listas de ejercicios | 0 |
   | `matematiccj/red-funciones-lineales` | Sin país declarado (español) | Recurso STEAM de funciones lineales con **tutor socrático offline** | 0 |

   **Lo que agrega el pase 6 al diagnóstico, y es lo más útil del gap.** Las causas del pase 2 eran "falta licencia, falta respaldo institucional, falta masa crítica". El pase 4 mostró con TutorIA que las dos primeras se resuelven caso por caso. El pase 6 muestra algo más específico: **ninguno de estos proyectos es un tutor genérico — cada uno ataca un problema local real y bien elegido** (rezago educativo adulto en México vía INEA, ingreso universitario en Paraguay, ruralidad en Colombia con TutorIA). **El déficit de la región no está en identificar el problema ni en diseñar el producto. Está en la continuidad y en la comunidad:** nadie los sostiene después del primer release.

   **Y eso cambia qué puede aportar Globant acá:** no "construir el tutor que falta" —hay varios, y bien pensados— sino **aportarle a uno de ellos la ingeniería, la gobernanza de proyecto y la evaluación que le falta**. Sale más barato, es más defendible ante un ministerio, y produce un caso regional con autoría local en vez de una importación.

   **Medido una tercera vez en el pase 7 del 2026-10-01, y el diagnóstico del pase 6 se confirma con el mejor ejemplo posible.** Búsqueda en GitHub por `tutor IA educativo español`: **197 resultados, techo de 3 estrellas entre los que realmente son tutores.** Nuevos respecto del pase 6:

   | Repo | Qué es | Stars | Estado |
   |---|---|---|---|
   | `Javi111003/OlivIA-RAG` | Tutor RAG para preparar el ingreso universitario en matemática | **1** | ⚠️ **sin licencia**; último movimiento 2025-07 |
   | `jrobador/finetuned-llama3.2-3B_mat-IA` | Llama 3.2 3B afinado para matemática; **segundo puesto del *Llama Impact Pan-LATAM Hackathon*** | **3** | 🚫 **sin actividad desde 2024-11** |

   **El segundo es la ilustración exacta del diagnóstico:** un finalista de un hackathon regional de Meta, con reconocimiento público, **abandonado dos meses después**. No falta talento, ni idea, ni visibilidad. **Falta continuidad.** El déficit de LATAM no está en el día 1 de un proyecto, está en el día 90.

   **Y hay un cambio institucional del pase 7 que reencuadra la oportunidad entera:** el **Observatorio de IA en Educación para América Latina y el Caribe** de UNESCO (lanzado **2026-04-14** en la sede de la CEPAL, Santiago) crea por primera vez una **contraparte regional permanente** con CAF, CENIA, Cetic.br/NIC.br, Fundación Ceibal, Tec de Monterrey, ProFuturo e IRCAI. Ver `intel/market.md`. Eso es precisamente el tipo de estructura que puede sostener un proyecto más allá del día 90 — que es lo único que a estos repos les falta.

   **Medido una cuarta vez en el pase 8 del 2026-10-01 — y por primera vez el gap tiene una geografía adentro.** Buscando accesibilidad y educación especial (ángulo que esta KB nunca había usado) aparecen **dos repos chilenos**, y no son dos proyectos de autor suelto:

   | Repo | Licencia | Stars | Commits | Anclaje normativo nacional |
   |---|---|---|---|---|
   | `marcorojasb/tero` | **MIT** ✅ | 0 | **111** | MINEDUC, **Decreto 83** (educación especial), **Ley 21.719** (protección de datos) |
   | `ronda-ai/Ronda-App` | GPL-3.0 ⚠️ | 3 | 17 | **Marco para la Buena Enseñanza (MBE)** |

   **Lo que esto agrega al diagnóstico, que venía siendo «falta continuidad, no talento».** Los dos están anclados a **instrumentos normativos nacionales reales** en vez de a un currículo genérico, y `tero` además resuelve bien el problema de gobernanza que los pases anteriores señalaron: es MIT, tiene 111 commits, y su postura de diseño —*el agente propone, el docente decide*, sin escritura de archivos sin aprobación humana— es **la arquitectura que la regulación de EE. UU. está forzando** (ver gap 12). Un repo de 0 ★ de Chile llegó por restricción local a la misma conclusión de diseño que Delaware y Nueva York están imponiendo por norma.

   **Y junto con lo que la KB ya tenía, Chile se está volviendo el nodo técnico de LATAM:** Latam-GPT (CENIA), el **Observatorio UNESCO lanzado en la sede de la CEPAL en Santiago**, y ahora dos repos educativos con anclaje normativo. Ninguno tiene tracción — el gap 2 **no se cierra** — pero por primera vez hay una concentración geográfica en vez de iniciativas dispersas, y eso cambia dónde conviene buscar contraparte. Ver `intel/market.md`.
3. **EMEA no produce tutores: produce la capa que los mide y los acredita** *(reformulado en el pase 4; antes decía "produce plataformas")*. La formulación anterior era correcta pero pobre — agrupaba todo lo no-agéntico como "plataformas". Con lo del pase 4 el patrón es más nítido y más útil:

   - **Plataformas:** OpenOLAT (Suiza), Chamilo (Bélgica/España), Richie (Francia), H5P (Noruega).
   - **Evaluación:** **MathTutorBench** (org `eth-lre`, CC BY 4.0, 42 ★, EMNLP 2025 Oral) y **UnifyingAITutorEvaluation** + AITutor-EvalKit (MBZUAI, Abu Dhabi, NAACL 2025).
   - **Esquemas de conformidad curricular:** **OpenDidactia** (España, CC BY-SA 4.0, 0 ★) — esquemas OKF para generar Programaciones Didácticas conformes a **LOMLOE** en las 17 comunidades autónomas. No es un agente: es el *formato de salida auditable* que un agente docente necesita para ser aceptable ante una inspección educativa.
   - **Skills pedagógicas:** education-agent-skills (UK, CC BY-SA 4.0, 814 ★).
   - **Tutores, la excepción:** **OpenTutorAI-CE** (BSD-3-Clause, 107 ★) — **región cerrada en el pase 4: Marruecos**, lo que explica su soporte multilingüe árabe/francés/inglés.

   **Que EMEA produzca medición y conformidad mientras APAC produce tutores no es casualidad: es el reflejo de dónde muerde la regulación.** Para una propuesta europea eso es favorable — el artefacto local disponible es justamente el que pide el EU AI Act. Lo que EMEA no tiene es un tutor open source de escala, y hay que ir a buscarlo a APAC con el riesgo de procedencia que eso implica (gap 4).

   **Ampliado en el pase 5:** EMEA también produce **la mejor referencia teacher-facing que existe en abierto** — **`Aila`** (https://github.com/oaknational/oak-ai-lesson-assistant, **MIT**, 35 ★, **1.188 commits**), el asistente de planificación de clases de **Oak National Academy** (Reino Unido), **en producción**. Y en la capa de evaluación se suma **EduFrameTrap** (TUM/MCML, Alemania). La formulación se afina una vez más: **EMEA produce todo lo que rodea al tutor —medición, conformidad, currículo, herramientas docentes— y no produce el tutor.** ⚠️ `Aila` declara ser para uso interno de Oak: referencia de arquitectura, no base de producto.

   **África, que faltaba entera en este gap.** EMEA se venía leyendo como Europa + MBZUAI + Marruecos. Hay evidencia propia: **AfriLabs + WISE** (nov 2025, 3.875 encuestados, 47 instituciones, 199 empresas edtech), **North-West University** como primera universidad sudafricana con política oficial de AI (2026-01-15), MoU **DHET–Microsoft SA** (2025-10-07), y **N-ATLAS** (Nigeria), LLM multilingüe open source. El patrón de compra africano es **ministerio + MoU con big tech**, no adquisición institucional. Ver `intel/market.md`.
4. **La oferta de agentes está concentrada en APAC.** DeepTutor (HKU) y OpenMAIC (Tsinghua) son ~80k ★ combinadas y las dos vienen de instituciones chinas. Para un cliente con restricciones de procedencia de software, esto es un riesgo a declarar temprano, no a descubrir en due diligence.

   **Agravado y a la vez mitigado en el pase 5, y las dos mitades importan.**

   *Agravado:* la concentración ya no es sólo de agentes. Con **`OmniEdu`** (Universidad de Pekín + UCAS + Zhongguancun Academy — modelos fundacionales 4B/9B/27B) y **`EduBench`** (ACL 2026), **las cuatro capas del stack educativo open source tienen su artefacto de referencia en instituciones chinas**: modelo (OmniEdu), modelado del alumno (pyKT), agente (DeepTutor, OpenMAIC) y evaluación (EduBench).

   *Mitigado:* por primera vez hay una **ruta alternativa completa** para un cliente con restricción de procedencia — **`pyBKT`** (MIT, 281 ★, CAHLR/UC Berkeley, EDM 2021) en modelado, **`Aila`** (MIT, Reino Unido) como referencia teacher-facing, **`MathTutorBench`** (ETH Zúrich) y **`SafeTutors`** (MIT) en evaluación, y `OpenOLAT` / `Kolibri` / `Oppia` en plataforma. El pase 4 había dejado el gap en su peor momento (descubrió que también el modelado era chino); esto lo revierte parcialmente.

   **Lo que hay que decir al proponer la ruta alternativa:** existe, y **no es gratis**. Se paga en capacidad de modelo (pyBKT es BKT clásico, pyKT es deep learning con 10+ modelos DLKT) y en madurez de agente (no hay equivalente occidental a DeepTutor con 40.6k ★). La ventaja compensatoria de pyBKT es la **interpretabilidad**, que ante un regulador que pregunta por qué el sistema decidió lo que decidió vale más que la potencia.

   **Extendido a una quinta capa en el pase 7 del 2026-10-01, y acá la ruta alternativa se rompe.** Las capas chinas de referencia eran cuatro: modelo (`OmniEdu`), modelado del alumno (`pyKT`), agente (DeepTutor, OpenMAIC) y evaluación (`EduBench`). La quinta es **los datos de entrenamiento**, y el patrón es peor que en las otras cuatro:

   | Dataset de knowledge tracing | Licencia | Origen |
   |---|---|---|
   | **XES3G5M** (5,5M interacciones) | **MIT** ✅ — *el único permisivo* | **China** |
   | **EdNet** (131,4M interacciones) | ⚠️ CC BY-NC | APAC (Corea) |
   | **FoundationalASSIST** (1,7M, inglés) | ⚠️ CC BY-NC + gated | North America |

   **El único dataset de knowledge tracing con licencia permisiva es chino.** Los dos de procedencia no china son los dos NonCommercial.

   La ruta alternativa que el pase 5 armó para un cliente con restricción de procedencia (`pyBKT` + `Aila` + `MathTutorBench` + `SafeTutors`) **se sostiene en código y se rompe en datos**. Para ese cliente, entrenar con los datos propios deja de ser la opción preferible y pasa a ser **la única**, con el costo de arranque en frío que eso implica. Y se suma un dato de la capa de evaluación en humanidades: **`ProHist-Bench` / `ABench` también es chino** (Ant Group). Ver **P16**.
5. **No hay integración madura entre knowledge tracing y agentes LLM** *(el gap se mantiene; el inventario estaba incompleto — corregido en el pase 4)*. La conclusión —**nadie los cosió bien**— sigue siendo correcta y es el hueco técnico concreto del patrón P1. Lo que estaba mal era el inventario de piezas disponibles: los pases 1–3 listaban sólo `py-fsrs` (MIT, 499 ★, scheduling) y OATutor (BKT embebido en un ITS completo).

   Falta agregar la pieza central: **`pyKT`** (https://github.com/pykt-team/pykt-toolkit, **MIT**, **441 ★**, 811 commits) — librería de *knowledge tracing* profundo sobre PyTorch con **10+ modelos DLKT** comparables, **7+ datasets** con preprocesamiento estandarizado y 5 escenarios de predicción. Publicada en **NeurIPS 2022** y mantenida. Origen: **Jinan University / Guangdong Institute of Smart Education, China → APAC** (refuerza el gap 4, ahora también en la capa de modelado).

   **Por qué la corrección importa aunque el gap no se cierre:** con el inventario viejo, coser tracing a un agente parecía "implementar BKT a mano o extraerlo de OATutor". Con `pyKT` en la mesa, el trabajo es **integración de una librería MIT madura**, no investigación. Eso cambia la estimación de un proyecto de meses a semanas, y cambia lo que se puede prometer: un modelo DLKT publicado y reproducible es evidencia defendible de eficacia adaptativa ante un regulador; "el LLM decidió" no lo es. Ver el patrón nuevo **P10**.

   **Lo que sigue faltando literalmente:** un repo que exponga un modelo de knowledge tracing **como tool o servidor MCP** para que el agente consulte el estado de mastery antes de decidir qué preguntar. `tutor-mcp` (MIT, 42 ★, Go) es lo más cercano — implementa BKT y repetición espaciada detrás de MCP — pero usa su propio BKT, no una librería DLKT entrenable. **El hueco exacto es `pyKT` detrás de MCP**, y no existe.

   **Reformulado en el pase 5 del 2026-09-30 — el patrón existe cinco veces; la ingeniería, ninguna.** La afirmación "no existe" era demasiado fuerte. Buscando por la pieza técnica aparecen **cinco servidores MCP independientes** que exponen mastery a un agente: `zcsabbagh/knowledge-graph-mcp` (MIT, 1 ★, 8 commits — SM-2 + fórmula de pesos fija), `woodstocksoftware/student-progress-tracker` (MIT, 1 ★, 9 commits), `tejpalvirk/student` (MIT, 1 ★, 6 commits), `znecho9/knowledge-forest-mcp` (Apache-2.0, 0 ★, 3 commits — mastery con evidencia a libro cerrado obligatoria) y `radhepa/Teacher-MCP` (MIT, 0 ★, 2 commits).

   **Las dos lecturas, y las dos son útiles:**

   - **Señal de mercado:** cinco autores sin relación entre sí llegaron al mismo patrón en la misma ventana. El problema es real y sentido por muchos; el patrón está validado sin que Globant tenga que evangelizarlo.
   - **El hueco de ingeniería sigue intacto, y mejor documentado:** **ninguno de los cinco usa una librería de knowledge tracing entrenable** — todos implementan su propia heurística. Los tres más grandes suman **3 estrellas y 23 commits**. Verificado de primera mano en el pase 5: `pyKT` sigue en 441 ★ / 811 commits y **su documentación no menciona MCP ni interfaz de serving**.

   **Y ahora hay dos librerías candidatas, no una:** a `pyKT` (MIT, 441 ★, deep learning, APAC) se suma **`pyBKT`** (https://github.com/CAHLR/pyBKT, **MIT**, **281 ★**, 379 commits, **EDM 2021**, CAHLR/UC Berkeley — el mismo laboratorio de Zachary Pardos que produjo OATutor, que esta KB ya listaba sin haber mirado el resto del laboratorio). Para un primer engagement regulado pyBKT es probablemente la mejor elección: BKT bayesiano es menos potente que DLKT y **mucho más fácil de defender ante un regulador**.

   **El gap pasa de "nadie lo intentó" a "cinco lo intentaron y ninguno conectó la librería buena".** Es una propuesta mejor: el trabajo dejó de ser inventar el patrón y pasó a ser hacerlo bien una vez. Ver el patrón nuevo **P12**.

   **Reformulado otra vez en el pase 6 del 2026-10-01 — el problema estaba mal partido, y el trabajo pendiente es más chico de lo que la KB venía estimando.**

   Los cinco servidores MCP del pase 5 no fallaron sólo por no usar una librería de knowledge tracing entrenable. **También inventaron, cada uno, su propio almacén de eventos de aprendizaje.** Y ese almacén no hay que inventarlo: es **xAPI / IEEE 9274.1.1**, con cuatro implementaciones open source maduras que ninguna de las cinco pasadas anteriores había registrado — porque se buscaba por "agente", "tutor" y "benchmark", y esta capa se llama **Learning Record Store**.

   | Pieza del patrón | Diagnóstico hasta el pase 5 | Estado real tras el pase 6 |
   |---|---|---|
   | Almacén de eventos de aprendizaje | "cada servidor MCP se lo inventa" | **Resuelto y estandarizado.** `lrsql` (Apache-2.0, 143 ★, Postgres 14–18) o `Ralph` (MIT, 50 ★, conversión nativa de Open edX) |
   | Transporte MCP hacia ese almacén | No registrado | **Resuelto.** `learnmcp-xapi` (MIT, 15 ★) — y ya habla con los dos anteriores |
   | **Estimador de mastery entrenable detrás** | "no existe" | **Sigue sin existir.** `learnmcp-xapi` registra y recupera; **no infiere mastery** |

   **La formulación correcta del hueco, sexta versión:** no es "construir un servidor MCP de mastery" (se hizo cinco veces) ni "construir el almacén" (es un estándar con cuatro implementaciones). Es **enchufar `pyBKT` o `pyKT` como estimador detrás de un LRS que ya existe, expuesto por un MCP que ya existe**. Eso es **un componente, no una plataforma** — y cambia la estimación de un proyecto otra vez, ahora hacia abajo.

   **La lección de método, que es la tercera vez que esta KB tropieza con la misma piedra en otra forma.** El pase 3 aprendió que un gap "no existe X permisivo" hay que re-buscarlo por licencia y stack, no por categoría. El pase 6 agrega el caso complementario: **acá la consulta no estaba mal, estaba mal el mapa.** Faltaba una capa entera en el modelo mental del stack, así que nunca se buscó. Cuando un gap sobrevive cinco pasadas, conviene preguntarse no sólo *cómo* se buscó sino **si la cosa que falta tiene un nombre que uno no está usando**.

   **Completado en el pase 7 del 2026-10-01 — la pieza que falta no es sólo código, es el dataset con que se entrena.**

   Seis pasadas acotaron el gap hasta dejarlo en una sola pieza: **un estimador de mastery** (`pyBKT` o `pyKT`) detrás de un LRS que ya existe, expuesto por un MCP que ya existe. Eso sigue siendo correcto. Lo que faltaba decir es que **ese estimador hay que entrenarlo**, y que los datasets de knowledge tracing disponibles son mayoritariamente **NonCommercial** (ver el **gap 11** y el **trend 16**).

   | Pieza del patrón | Estado tras el pase 7 |
   |---|---|
   | Almacén de eventos (LRS xAPI) | **Resuelto.** `lrsql` (Apache-2.0) o `Ralph` (MIT) |
   | Transporte MCP | **Resuelto.** `learnmcp-xapi` (MIT) |
   | Librería de estimación | **Resuelto.** `pyBKT` (MIT) o `pyKT` (MIT) |
   | **Datos para entrenar la estimación** | ⚠️ **Es el cuello de botella real.** Sólo `XES3G5M` es permisivo, y es chino / matemática / tercer grado. `EdNet` y `FoundationalASSIST` son CC BY-NC |
   | Integración | **Sigue siendo trabajo propio** — ninguno de los cinco servidores MCP lo hizo bien |

   **El gap pasa de "cinco lo intentaron y ninguno conectó la librería buena" a su formulación final: la integración es trabajo de semanas y el dato de entrenamiento es trabajo del cliente.** Es la mejor versión del gap porque es la que se puede cotizar sin sorpresas: el LRS entra en la fase 1 justamente porque es el que fabrica el dataset. Ver **P16**.

   Ver el patrón nuevo **P15**.

6. **No hay agente de grading open source con tracción** *(agregado en el pase 2)*. Se buscó específicamente corrección y assessment automatizado con licencia permisiva. La capa de grading sigue siendo **propietaria**: Gradescope (Turnitin), Codio, Kangaroos AI. En abierto hay *papers* (arXiv 2601.00730, 2607.02432, 2506.07955), no repos con adopción. Consecuencia directa para propuestas: **no prometer reemplazar Gradescope; prometer orquestarlo** — por eso `gradescope-mcp` (MIT, 8 ★) vale seguirlo pese a su tamaño. Es el camino realista hacia grading agéntico hoy.

   **🔴 CORREGIDO EN EL PASE 13 DEL 2026-10-01 — el gap se parte en dos y una mitad estaba mal.** Once pasadas repitieron esta formulación. La evidencia que la sostenía era `gradescope-mcp` (8 ★), `classmoji` (83 ★, AGPL-3.0), `rubric` (0 ★) y `llmgrader` (licencia de investigación) — toda la capa medida **por el lado del agente**. Buscando por **el entorno donde el alumno hace el trabajo** aparece una pila entera que esta KB no tenía:

   | Tipo de trabajo del alumno | Estado real de la corrección open source |
   |---|---|
   | **Código, notebooks, datos, cálculo numérico** | **Resuelto, permisivo y desplegado.** `nbgrader` (**BSD-3-Clause**, 1.400 ★, **v0.9.6 del 2026-09-30**) y `otter-grader` (**BSD-3-Clause**, 161 ★, UC Berkeley DSEP), sobre `jupyterhub` (**BSD-3-Clause**, 8.300 ★), con `jupyter-ai` (**BSD-3-Clause**, 4.400 ★, ACP+MCP) como capa de agente y `ltiauthenticator` (**BSD-3-Clause**, LTI 1.3 contra Open edX/Canvas/Moodle) como puente al LMS. Implementado desde 2014 en **UC Berkeley, Cal Poly, Edimburgo y Aalto** |
   | **Prosa — ensayo, respuesta abierta, trabajo escrito** | **El gap 6 sigue intacto, y es ahí donde vive el incumbente.** Gradescope y Turnitin son dueños de esto; lo open source sigue siendo *papers* y repos pre-tracción |

   **Consecuencia para propuestas, corregida:** para un cliente de **STEM, ciencia de datos, ingeniería o formación técnica**, decirle «la corrección open source no existe, orquestemos Gradescope» es **falso y además más caro que la alternativa**. Para un cliente de **humanidades o evaluación por escrito**, la recomendación original se mantiene sin cambios. Ver el **trend 30** y el patrón **P29**.

   ⚠️ **Lo que esta corrección no dice:** nbgrader no evalúa pedagogía ni modela al alumno — autocorrige contra tests que escribió el docente. El **gap 1** (nadie usa los benchmarks pedagógicos que existen) y el **gap 5** (nadie conectó una librería de knowledge tracing entrenable) **no se tocan**.

7. ~~**No hay SIS open source permisivo y vivo**~~ → **GAP RETIRADO en el pase 3 del 2026-09-30.** El pase 2 declaró que toda la capa SIS open source era PHP y copyleft, que la única opción permisiva (**Fedena**, Apache-2.0, 547 ★) estaba **muerta desde el 2016-07-20**, y concluyó que en el lado administrativo el agente **siempre** tiene que ir afuera. **La conclusión era incorrecta y se corrige.**

   **GegoK12** (https://github.com/Gego-K12/gegok12) es **MIT** — verificado en el archivo `LICENSE` del repo, `SPDX-License-Identifier: MIT`, © 2025 GegoSoft Technologies — con **54 ★, 97 forks, 123 commits y último commit el 2026-09-23**. Está vivo, es PHP 8.4 + Laravel 12, API-first, y **tiene sistema de plugins** (`Plugin-Hello-Teacher`). O sea: en el lado administrativo el agente **sí puede vivir adentro**, como plugin, sin contaminar IP, porque MIT no impone share-alike.

   **Lo que sigue siendo cierto:** todo el SIS open source es PHP, Fedena sigue muerta y no hay que proponerla, y para RosarioSIS / openSIS / OpenEduCat (los tres copyleft, y los tres con más instalaciones reales) el agente sigue yendo afuera. **Lo que cambia:** dejó de ser "la única opción limpia" y pasó a ser "el patrón por defecto, con una alternativa".

   **La condición que hay que leer:** GegoK12 es **open-core**. De 38 módulos, 26 están en el core MIT (alumnos, admisiones, asistencia, tareas, biblioteca, staff, avisos, comunicación con padres) y **12 son Pro pagos, USD 100–250 cada uno** — entre ellos **examinación y gestión de fees**, que son justo los dos procesos que un agente querría automatizar primero. Licencia Pro lifetime por dominio con fuente incluido, no suscripción por alumno. Detalle completo en `verticals/solutions.md`.

   **Por qué este gap se sostuvo dos pasadas.** Las dos anteriores buscaron "SIS open source" y encontraron los listicles, que repiten Fedena/RosarioSIS/openSIS y no incluyen a GegoK12 porque es reciente. La lección de método: **un gap de la forma "no existe X permisivo" hay que re-buscar con la consulta invertida** — por licencia y stack ("school ERP MIT Laravel"), no por categoría. Buscar la categoría devuelve el consenso de los listicles; buscar la licencia devuelve los proyectos nuevos.


8. **La capa teacher-facing es propietaria, con una sola excepción open source** *(agregado en el pase 3)*. `intel/market.md` ya observaba que las herramientas *para docentes* son "el ángulo menos disputado" y que MagicSchool lidera ahí. Buscando el equivalente open source aparece que el segmento entero es cerrado: **MagicSchool, Brisk, Diffit, Curipod, Eduaide.AI, SchoolAI, Taskade**. ~~La única entrada open source que encontramos es **Claw-ED** (MIT, **59 ★**).~~ → **CORREGIDO EN EL PASE 5 DEL 2026-09-30.** La afirmación "una sola excepción open source" era incorrecta:

   | Repo | Licencia | Stars | Commits | Qué es |
   |---|---|---|---|---|
   | **Aila** — https://github.com/oaknational/oak-ai-lesson-assistant | MIT ✅ | 35 | **1.188** | Asistente de planificación de clases de **Oak National Academy** (nonprofit educativa británica respaldada por el gobierno), **en producción**. Next.js + Prisma/PostgreSQL con pgvector |
   | **Claw-ED** — https://github.com/SirhanMacx/Claw-ED | MIT ✅ | 59 | **778** | Agente CLI local-first. *Sin cambios en stars desde el pase 3, pero activo: v9.18.2026.1* |
   | **ai-lesson-planner** — https://github.com/saniales/ai-lesson-planner | GPL-3.0 ⚠️ | 20 | 2 | Workflow multi-agente con salida a slides MARP |

   **Lo que cambia la propuesta:** el mejor artefacto teacher-facing abierto ya no es un proyecto de autor individual — es **código de producción de una institución educativa nacional, con 1.188 commits y licencia MIT**. Como referencia de arquitectura (RAG curricular, persistencia de la conversación de planificación, generación de recursos) vale más que todo lo demás junto.

   ⚠️ **Y la condición hay que leerla:** `Aila` declara estar *"intended primarily for internal use by Oak National Academy"* — sin API estable, sin soporte, sin garantía de despliegue externo. Es **referencia, no base de producto**. Para desplegar, el candidato sigue siendo Claw-ED.

   **Lo que no cambia:** el segmento sigue dominado por propietarios (MagicSchool, Brisk, Diffit, Curipod, Eduaide.AI, SchoolAI, Taskade). Ver el patrón **P8**.

9. **Sigue sin haber grading open source con tracción, pero la categoría se movió** *(actualizado en el pase 3)*. El gap 6 se mantiene: Gradescope (Turnitin), Codio y Kangaroos AI siguen siendo propietarios y no apareció ningún reemplazo con adopción. Lo nuevo es **AI-Teaching-Agent** (MIT, **0 ★**, 30 commits): genera artefactos **Lab / Exam / Grading como DSL validado**, con revisión humana obligatoria, evaluación sandboxeada, servidor MCP y previews de examen sin respuestas. Es la primera vez que vemos la estrategia de *generar el artefacto de corrección auditable* en vez de orquestar al incumbente — y el diseño es exactamente el que piden el EU AI Act y los estatutos de EE. UU. que prohíben grading automático. **Con 0 estrellas no se usa: se sigue.** La recomendación operativa del gap 6 no cambia (orquestar Gradescope vía `gradescope-mcp`).

   **Actualizado en el pase 5 — por fin sabemos *por qué* este gap se sostuvo cuatro pasadas, y la respuesta no es que nadie lo haya construido.**

   | Repo | Licencia | Stars | Commits | Estado |
   |---|---|---|---|---|
   | `sdrangan/llmgrader` | 🚫 **PySilicon Research License** (custom, no OSI) | 2 | **240** | Autograder para ingeniería: derivaciones multi-paso y justificación abierta, rúbricas en **XML**, trazas de corrección, **servidor MCP** e **integración con Gradescope**. De Sundeep Rangan (NYU), **desplegado en un curso de maestría real** |
   | `paper-instruments/rubric` | **MIT** ✅ | **75** | 64 | Rúbricas ponderadas genéricas para LLM-as-judge. No es educativo, es la plomería |
   | `Dmoayad/essay-grader-llm` | GPL-3.0 ⚠️ | 1 | 12 | Corrección de ensayos con rúbrica + RAG + detección de plagio |
   | `eecs-autograder/autograder.io` | ⚠️ no declarada (repo de docs) | 79 | 61 | Autograding **determinista por casos de test**, Docker sandbox. U. de Michigan, **~5.000 alumnos/semestre** |

   **`llmgrader` es el hallazgo incómodo:** es de largo el grading agéntico más maduro que esta KB encontró en cinco pasadas, y su licencia es una **"PySilicon Research License" propia, © 2026 Sundeep Rangan** — verificada leyendo el archivo LICENSE, no el badge. **No es OSI y no se puede usar en un entregable.**

   **La corrección de diagnóstico, que vale tanto como un repo nuevo:** el gap no era *"nadie construyó grading agéntico"* sino **"quien lo construyó bien no lo liberó de forma reutilizable"**. Son gaps distintos y llevan a propuestas distintas.

   **La recomendación operativa se vuelve más concreta:** (1) seguir orquestando Gradescope vía `gradescope-mcp`; (2) cuando haya que construir la capa de juicio, construirla sobre **`paper-instruments/rubric`** (MIT) en vez de desde cero, aportando la pedagogía con `EduBench` y `SafeTutors`; (3) para código, **no reemplazar el autograding determinista** — el ángulo AI correcto es explicación y feedback formativo sobre tests que ya corrieron, que además esquiva de frente la prohibición de calificación automática. Ver **P14**.


10. **La formación profesional no tiene nada open source con tracción — y ahora está medido** *(agregado en el pase 6 del 2026-10-01)*. El pase 5 dejó "formación profesional" como parte del sub-gap de benchmarks pedagógicos. Buscándolo directamente, el vacío es más grande que un benchmark faltante: **es el segmento entero**.

    Búsqueda en GitHub por `vocational education AI`: **24 repos en total, el más grande con 2 estrellas.** Casi todos son trabajos de curso, portfolios o apps de autor. Los dos únicos con forma de producto:

    - `edufeedai/edufeedai` (Java, **0 ★**, 9 issues abiertos) — recuperación, evaluación y generación de feedback sobre entregas de alumnos de FP. Sin tracción.
    - `straussbastian/ai_flashcards_for_school` (Python, **1 ★**) — flashcards generadas por un agente vía **MCP** para *Berufsschule* alemana: el docente arma el bundle, la clase entra con un link de tres palabras, **sin login y sin almacenar resultados**. El diseño de privacidad es interesante y replicable; el tamaño es irrelevante.

    **Por qué este gap importa más que su tamaño aparente.** La FP es el segmento con mayor presión de reskilling en las cuatro regiones y el que más rápido compra cuando hay presupuesto público — y no tiene ni plataforma, ni agente, ni benchmark open source con adopción. Cero de tres.

    **Consecuencia directa para una propuesta de FP:** hay que **presupuestar construcción, no integración**. Es lo contrario del resto de esta KB, donde la recomendación casi siempre es componer artefactos existentes. Decirlo temprano evita comprometer plazos de integración sobre una base que no existe. La contrapartida es que **quien construya ahí no tiene competencia open source**, que es la otra cara del mismo dato.

11. **Los datasets con que se entrena el modelado del alumno son NonCommercial, y la KB no lo había mirado en seis pasadas** *(agregado en el pase 7 del 2026-10-01)*. No es un gap de oferta: es un gap de **método** de esta KB, y corrige una afirmación que los pases 4, 5 y 6 repitieron.

    Las tres pasadas anteriores verificaron la licencia de los **repos** (`pyKT` MIT, `pyBKT` MIT, `lrsql` Apache-2.0, `learnmcp-xapi` MIT) y concluyeron que el tutor adaptativo es integración de piezas permisivas. Nunca verificaron la licencia de **los datos sin los cuales esos repos no hacen nada**. Al mirarla:

    | Dataset | Licencia | Reutilizable en un entregable facturado |
    |---|---|---|
    | **XES3G5M** | **MIT** ✅ | **Sí** — pero es chino, sólo matemática, tercer grado |
    | **EdNet** (el más grande, 131,4M interacciones) | ⚠️ CC BY-NC 4.0 | **No** |
    | **FoundationalASSIST** (el único en inglés con respuestas reales) | ⚠️ CC BY-NC 4.0 + gated | **No** |

    **Lo que el gap obliga a cambiar en una propuesta:** no se puede ofrecer un modelo de mastery "entrenado sobre datasets públicos del estado del arte". Se entrena con los datos del cliente, **y hay que presupuestar el arranque en frío**. La contrapartida es que eso convierte al Learning Record Store de la fase 1 (gap 5, pase 6) en una dependencia dura del producto y no en un anexo de conformidad — que es un argumento más fuerte, no más débil. Ver **P16**.

    **La lección de método, que vale para las otras once entradas de esta lista:** verificar la licencia del repo es necesario y no suficiente. Para cualquier pieza que **se entrene** —modelos de mastery, graders, clasificadores de riesgo— hay que verificar además la licencia del dataset, y el riesgo vive ahí con más frecuencia que en el código.

12. **La educación especial y la accesibilidad son la capa peor abastecida de esta KB — lo maduro es copyleft, lo permisivo no tiene tracción, y el open source apunta a la tarea que se está prohibiendo** *(agregado en el pase 8 del 2026-10-01)*. Siete pasadas construyeron agente, modelado, evaluación, seguridad, telemetría y datos, y **ninguna buscó al alumno con discapacidad**. Buscado directamente, el vacío está medido:

   | Señal | Medición |
   |---|---|
   | Topic `special-education` | **20 repos**, techo **10 ★** — y ese techo (`SEALApplication`) está **marcado como deprecado** y es GPL-3.0 |
   | Topic `inclusive-education` | **30 repos**, techo **60 ★** (`Sign-Language-Interpreter`) — y ese techo **no tiene licencia** |
   | Búsqueda `IEP individualized education program AI` | **1 repo** en todo GitHub (`EyeEP`, 1 ★, **sin licencia**) |
   | Lo agéntico y permisivo | techo **15 ★** (`Swar-Setu`, MIT, India) |
   | Lo maduro | **todo copyleft**: OptiKey (GPL-3.0, 4.4k ★), Cboard (GPL-3.0, 759 ★) |

   **Las tres consecuencias, en orden de importancia comercial:**

   **(a) La demanda está regulada y la oferta no la sigue.** El **European Accessibility Act** rige desde el **2025-06-28** sobre plataformas de e-learning y LMS, e **IDEA** obliga en EE. UU. desde hace décadas. Es el único segmento de esta KB donde la obligación legal **ya venció** y la oferta open source sigue en fase cero. La única pieza con tracción y licencia limpia — `accessibility-agents`, **MIT, 419 ★** — **no es un repo educativo**, y por eso ninguna consulta de los siete pases anteriores la iba a encontrar.

   **(b) El open source apunta justo al paso prohibido.** Lo poco que hay de educación especial agéntica apunta a **redactar o gestionar el IEP** (`EyeEP`; el parsing de IEP/504 de `Teacher-Hub`). La guía de **Delaware** prohíbe usar AI para objetivos de IEP, evaluación docente y calificación subjetiva; el marco de **Nueva York** prohíbe usar AI para desarrollar planes **IEP o 504**. **Un producto que redacta IEPs es invendible en los distritos más grandes de EE. UU.** Lo vendible es el resto del flujo con el docente como autor — patrón **P18**.

   **(c) Falta la pieza del medio, y es la que el cliente pide.** `accessibility-agents` resuelve acceso técnico; `Cboard` y `OptiKey` resuelven el dispositivo. **No existe en abierto la pieza que conecta la acomodación declarada de un alumno con la adaptación automática del material.** Eso no es investigación — es integración sobre piezas MIT que ya existen — pero hoy no está hecho por nadie.

   **El detalle de licencia que hay que mirar antes de cotizar:** `Teacher-Hub` declara *«MIT License — free for educational and non-commercial use»*, y **las dos mitades se contradicen** (MIT permite uso comercial). Segunda vez que esta KB encuentra una declaración de licencia que el texto no sostiene. Leer el `LICENSE` y pedir aclaración por escrito antes de cualquier entregable.

   **Lo que sí cambia respecto del gap 2:** de los repos nuevos de este pase, **dos son chilenos** — `tero` (MIT) y `Ronda` (GPL-3.0) — y los dos están anclados a instrumentos nacionales reales (Decreto 83, Ley 21.719, Marco para la Buena Enseñanza) en vez de a un currículo genérico. Ver la actualización del gap 2 y `intel/market.md`.

13. **Ningún agente open source emite ni consume credenciales verificables — el stack del alumno y el stack de la credencial no se tocan** *(agregado en el pase 9 del 2026-10-01)*. Se buscó explícitamente. Ninguno de los 25+ agentes de la tabla principal de `agents/top.md` escribe un Open Badge ni una credencial W3C VC, y ninguna de las ocho piezas de la capa de credenciales tiene interfaz de agente ni servidor MCP.

    **Por qué este gap es mejor noticia que los anteriores.** Las dos puntas existen y son **MIT**: del lado de la decisión, `pyBKT` (281 ★) y `pyKT` (441 ★) sobre un LRS conforme (pase 6); del lado de la emisión, `issuer-coordinator`, `verifier-plus` y `learner-credential-wallet`. Falta **el pegamento**, y el pegamento es una regla de umbral más un mapa de competencias —no es investigación. La pieza que traduce objetivos de aprendizaje a vocabulario **ESCO/ISCO** también existe y es MIT (`esco-skill-extractor`, 32 ★).

    **La formulación precisa del gap, para que la próxima pasada lo mida y no lo repita:** no falta tecnología, falta **un artefacto que convierta una estimación de dominio en una credencial verificable** con el umbral declarado y auditable. Eso es exactamente **P19**, y es el patrón más corto de construir de los tres que agrega este pase.

14. **El stack europeo de credenciales salió de GitHub y esta sesión no puede verificarlo** *(agregado en el pase 9 del 2026-10-01)*. No es un gap de oferta: es un **gap de verificación**, y se declara en vez de callarlo porque afecta directamente a cualquier propuesta en EMEA.

    Los dos repos de la Comisión Europea —`european-digital-credentials` (Issuer, Viewer, Wallet; EUPL-1.2, 6 ★, 31 commits) y `European-Learning-Model` (EUPL-1.2, 54 ★, 199 commits)— están **archivados** (2024-02-02 y 2024-02-14) y declaran, textual: *«For the latest versions go to: https://code.europa.eu/qualifications-courses-and-credentials/»*.

    **`code.europa.eu` está bloqueado por el proxy de egreso de esta sesión** (`EGRESS_BLOCKED`, verificado). Así que del stack europeo de credenciales esta KB puede afirmar **sólo lo que quedó archivado en GitHub**: que existe, su licencia EUPL-1.2, su modelo de datos compatible con W3C VC, y que el código vivo está en otro lado. **Versión actual, estado de mantenimiento y licencia vigente no están verificados.**

    **La consecuencia de método, que generaliza.** El pase 6 dejó escrito que *el proxy de egreso decide qué se puede afirmar*, y el pase 7 agregó que *también decide qué se puede cerrar*. Este pase agrega la tercera forma: **también decide qué regiones se pueden cubrir bien.** El stack europeo de credenciales es, muy posiblemente, la oferta más relevante del mundo para P19 en EMEA, y es la que esta sesión no puede mirar. Un cliente europeo exige abrir `code.europa.eu` **antes** de cotizar.


15. **Ningún puente agente↔contenido curricular tiene tracción, y el único que existe declara mal la licencia de lo que
    sirve** *(agregado en el pase 10 del 2026-10-01)*. Se buscó explícitamente un servidor MCP o adaptador que le dé a un
    agente acceso a contenido curricular abierto. Hay **dos**, y los dos son fase cero:

    | Repo | Licencia | Stars | Commits | Problema |
    |---|---|---|---|---|
    | `pythpythpython/openstax-mcp-server` | **MIT** (código) ✅ | **1** | 7 | Sirve 40+ libros de OpenStax con búsqueda semántica y generación de notebooks. 🔴 **Declara en su README que el contenido es CC BY 4.0; el `LICENSE` de los bundles de OpenStax en GitHub dice CC BY-NC-SA** (3 de 3 títulos verificados) |
    | `moarshy/mcp-tutor` | 🚫 **sin licencia** | **0** | 26 | Convierte repositorios de **documentación técnica** en cursos con DSPy. No es currículo escolar. El repo sólo dice: *«This project is experimental and intended for educational and research purposes»* |

    **Es exactamente la misma forma que el pase 6 encontró en telemetría y el pase 9 en credenciales:** la capa existe desde
    hace años, el estándar existe, y **el puente hacia el agente es un repo de una estrella**. Va tres capas seguidas con el
    mismo diagnóstico, y eso ya no es casualidad: **el trabajo que falta en educación abierta no es construir capas, es
    conectarlas.** Para Globant es el hueco más barato de llenar y el más defendible de cobrar — es integración verificable,
    no investigación.

    **Y hay un segundo hueco adentro del mismo gap:** ninguno de los **26 agentes** de la tabla principal de `agents/top.md`
    **emite el metadato de licencia del material que genera o deriva**. El agente produce el artefacto sin la pieza que lo
    hace usable ante un tercero — el mismo patrón que el gap 13 encontró con las credenciales.

16. **La capa de descubrimiento de contenido abierto es NonCommercial a nivel de metadato, así que el catálogo está bloqueado
    aunque el contenido no lo esté** *(agregado en el pase 10 del 2026-10-01)*. **OER Commons**, de **ISKME**, es la
    biblioteca de referencia de OER (catálogo buscable K-16). **ISKME comparte el metadato del catálogo con licencia
    NonCommercial**, por decisión explícita de tratar la educación como bien público.

    **Consecuencia directa:** no se puede construir un recomendador curricular, un buscador ni una capa de *discovery*
    comercial sobre ese catálogo. Y el catálogo es precisamente lo que uno querría para no curar a mano. **El cuello de
    botella no es el contenido: es el índice.**

    **Lo que queda como camino, y hay que decirlo en la propuesta:** curar un corpus propio y acotado al dominio del cliente,
    con manifiesto de licencia por ítem (**P22**), guardado en un repositorio permisivo (`DSpace`, BSD-3-Clause) e ingestado
    con herramienta permisiva (`LibreTexts/shapeshift`, MIT). Sale más caro que apoyarse en el catálogo abierto, **y es la
    única variante que se puede facturar.**

17. **La licencia declarada por el editor del contenido no es verificable desde esta sesión, y es la mitad que falta de la
    contradicción del trend 22** *(agregado en el pase 10 del 2026-10-01)*. No es un gap de oferta: es un **gap de
    verificación**, y se declara porque afecta a la afirmación más accionable del pase. Están **bloqueados por el proxy de
    egreso**: `openstax.org` (catálogo con la licencia por título), `openscied.org` (que vende una **licencia comercial**
    sobre contenido abierto — señal de mercado que valía confirmar) y `support.thenational.academy` (documento de licencia de
    Oak National Academy, incluida la posible restricción geográfica al Reino Unido).

    **Lo verificado de primera mano es el lado GitHub de cada afirmación** (archivo `LICENSE` de tres bundles de OpenStax,
    README de OATutor y del servidor MCP). **Lo que falta es el lado del editor.** Antes de llevar a un cliente cualquier
    afirmación de licencia de contenido de este pase, abrir esos tres dominios y confirmarla en la fuente del editor.

18. **No existe un sistema de early warning / student success open source mantenido, en ninguna región — y es la única capa de esta KB donde la demanda está madura y la oferta es cero** *(agregado en el pase 11 del 2026-10-01)*. No es un gap de tracción como el 1 ni de licencia como el 11: es **ausencia de producto**, medida.

    **Lo que se buscó y lo que devolvió, con la sintaxis exacta para que la próxima pasada pueda repetirlo:**

    | Consulta en GitHub, 2026-10-01 | Resultado | Techo de estrellas |
    |---|---|---|
    | `topic:learning-analytics stars:>50` | **2 repos en todo GitHub** | 169 ★ — `AkihikoWatanabe/paper_notes`, un blog de notas de papers |
    | `dropout prediction student license:mit pushed:>2026-01-01` | **110 repos** | **6 ★** |

    **El estado de los tres artefactos que importan** (detalle en `agents/top.md`): `Aliipou/Student-Retention-Prediction` (MIT, 6 ★) es el tope de la capa y **entrena con datos sintéticos generados por el propio repo**, sin auditoría de fairness; `dssg/student-early-warning` (70 ★, Data Science for Social Good, Universidad de Chicago) tiene licencia **`NOASSERTION`** y **último push 2018-08-22**; `novatrix-2030/SIH-2026` ("DropGuard", Smart India Hackathon 2026) tiene el mejor stack del grupo —LightGBM + XGBoost + SHAP + Groq— y **ninguna licencia**.

    **Y el stack institucional que la capa tuvo está archivado**, verificado repo por repo en los 21 de la organización `Apereo-Learning-Analytics-Initiative`: `OpenLRS` **archivado con la descripción `Deprecated`**; `OpenDashboard-legacy` **`(Deprecated)`**; el reemplazo `OpenDashboard-ux` + `OpenDashboard-api` **creado el 2020-02-12 y abandonado dentro del mes** (1 ★ y 0 ★); `LearningAnalyticsProcessor`, que es el orquestador del pipeline, **sin push desde 2023-01-19**; y **`OpenLRW` como única pieza viva** (62 ★, ECL-2.0, push del 2026-08-04). Falta además **Student Success Plan (SSP)**, el producto de *case management* de advising de Apereo con despliegues reales (St. Petersburg College, Sinclair Community College, soporte de Unicon): 🔴 **sin repositorio localizable en 2026; el rastro público se corta cerca de 2014-2015, en SSP 2.4.**

    **Por qué este gap es el más vendible de los 19, y no el más preocupante.** En todos los demás, la ausencia de oferta acompaña a una demanda incipiente. Acá la demanda está **presupuestada**: *student success* es categoría de compra consolidada en educación superior, con incumbentes propietarios. Y las dos condiciones que normalmente bloquean un engagement **no se cumplen**: los datos de referencia son **CC BY 4.0** con uso comercial (OULAD y UCI 697, ver `repos/foundations.md`) y la base técnica existe en el core de Moodle (*Analytics API*, GPL-3.0, con el target de alumno en riesgo incluido) o sobre OpenLRW. **Lo que falta es exactamente lo que se factura: ingeniería, mantenimiento y expediente de conformidad.** Ver **P25**.

    ⚠️ **La trampa que hay que evitar al cotizar:** el número `4.424` aparece en decenas de esos 110 repos porque **es el mismo dataset portugués de hace una década**. La capa entera está entrenada sobre 4.424 alumnos de una institución europea. Para un cliente de cualquier otra región, eso es un punto de partida metodológico y **no un modelo que se pueda presentar como funcionando**.

    **Y la dimensión regional, que reencuadra el gap 2.** Esta capa falta en las cuatro regiones, pero falta distinto: **North America** tiene el mercado y su único aporte open source es de 2018 con licencia irreconocible; **EMEA** tiene la regulación que lo exige y los dos datasets CC BY; **APAC** produce el repo con mejor stack y lo abandona después del hackathon; **LATAM** produce el **método publicado y revisado por pares** —revisión sistemática de 11 estudios 2022-2026 sobre riesgo de evasión en primaria (UFPE), tesis de UNIFEI, estudios de caso en institutos federales con Random Forest y XGBoost, ausentismo como predictor dominante— **y ningún repositorio**. El gap 2 dice que LATAM produce repos sin comunidad; en esta capa produce ciencia sin código. **Son los dos lados del mismo déficit, y juntos dicen que el problema no es regional: es que nadie convierte el resultado en artefacto mantenido.**
19. **Los esquemas curriculares nacionales existen, son la pieza más cara de construir, y esta KB encontró dos de casualidad en dos pasadas distintas** *(agregado en el pase 11 del 2026-10-01)*. No es un gap de oferta: es un **gap de búsqueda**, y se declara para que la próxima pasada lo cierre a propósito.

    Lo que hay, sin haberlo buscado sistemáticamente:

    | Artefacto | Región | Licencia | Contenido |
    |---|---|---|---|
    | `nmarafo/OpenDidactia` *(pase 3)* | EMEA (España, LOMLOE) | **CC BY-SA 4.0** ⚠️ *share-alike* | Esquemas de Programación Didáctica y Situación de Aprendizaje para 17 comunidades + 2 ciudades autónomas, de Infantil a Bachillerato, FP y régimen especial |
    | `DECK6/korean-elementary-learning-map` *(pase 11)* | APAC (Corea del Sur, currículo revisado 2022) | **MIT** ✅ | **620 anclas de estándares de logro, 1.956 temas, 2.293 relaciones de prerrequisito, 152 clusters**, 11 materias, grados 1-6, en JSON y RDF/Turtle con *competency questions* SPARQL y restricciones SHACL |

    **Dos pasadas separadas por ocho ciclos encontraron el mismo tipo de artefacto en dos regiones distintas, y ninguna lo estaba buscando.** Eso es evidencia de que el resto probablemente exista: el *Common Core* y los estándares estatales de EE. UU., el *National Curriculum* británico, la BNCC de Brasil, los currículos de ACARA (Australia, que `mentar` ya consume en 157 plantillas) y de Singapur. **Si están publicados en formato estructurado, cada uno vale lo mismo que estos dos: es la pieza más cara de cualquier agente docente y la que ningún cliente quiere pagar dos veces.**

    **Y la comparación entre los dos que hay es la lección de método:** el coreano es **MIT** y trae el grafo de prerrequisitos y la validación formal; el español es **CC BY-SA** y no trae ninguna de las dos. **El artefacto de APAC es mejor técnicamente y más barato legalmente**, lo cual es el espejo del gap 4 — pero acá, por una vez, la concentración en APAC juega a favor del cliente y no en contra.

    **La acción para el próximo pase:** buscar explícitamente `curriculum ontology`, `achievement standards`, `learning map` y `prerequisite graph` por país, en el idioma del país, en vez de esperar que aparezcan buscando agentes.


20. **Ninguna skill educativa del mundo tiene *eval* publicada, y esta KB tiene las herramientas para medirlas sin usarlas** *(agregado en el pase 12 del 2026-10-01)*. Los **siete** paquetes pedagógicos verificados en este pase —`education-agent-skills` (815 ★), `human-skill-tree` (562 ★), `universal-examprep-skill` (299 ★), `algo-sensei` (281 ★), `universal-diagnostic-tutor-skill` (234 ★), `kaogong-skill` (147 ★), `learning-commons-org/agent-skills` (35 ★)— son **texto de prompt sin versionado semántico, sin suite de regresión y sin medición de efecto pedagógico.**

    Y lo que lo vuelve un gap y no una queja: **la capa de evaluación para medirlos ya está en esta KB desde el pase 4** —MathTutorBench, UnifyingAITutorEvaluation, EduBench, EduGuardBench— construida para **tutores con backend** y **nunca aplicada a una skill**. Las dos piezas están en el mismo repositorio de conocimiento y no se tocan.

    **Es el gap más barato de cerrar de los veinte declarados**: no requiere plataforma, dataset licenciado ni implementación de estándar certificada. Requiere correr benchmarks que ya existen contra artefactos que ya existen. Es también el diferencial de la propuesta LATAM del pase 12 (ver `intel/market.md`, `### LATAM`) y del patrón **P27**.

21. **No existe el «notebook de la prosa»: fuera de las materias ejecutables no hay capa de práctica y corrección** *(agregado en el pase 13 del 2026-10-01)*. Es el gap que abre el hallazgo principal de este pase, y se declara **junto con** la buena noticia porque sin él la buena noticia se sobrevende.

    El pase 13 encontró que para trabajo **ejecutable** —código, notebooks, datos, cálculo— la capa está resuelta, permisiva y desplegada desde 2014: `jupyterhub` + `nbgrader` + `otter-grader` + `jupyter-ai` + `ltiauthenticator`, **14.334 ★, todo BSD-3-Clause**. Funciona porque el trabajo del alumno **se puede correr**: hay un artefacto ejecutable contra el que un test se evalúa de forma determinística.

    **Para un alumno de derecho, historia, lengua, filosofía o ciencias sociales no hay análogo de nada de eso.** Buscado explícitamente en este pase, no existe un entorno open source que ofrezca, para trabajo en prosa, el conjunto que Jupyter ofrece para código: entorno de trabajo por alumno, entrega versionada, corrección parcial automática, tramo de corrección manual integrado en el mismo flujo, y conexión por LTI 1.3 al LMS.

    | Pieza del flujo | Trabajo ejecutable | Trabajo en prosa |
    |---|---|---|
    | Entorno de trabajo por alumno | **JupyterHub** (BSD, 8.300 ★) | **No existe** |
    | Entrega y recolección | **nbgrader** (BSD) | El *assignment* del LMS, sin estructura |
    | Corrección automática parcial | **nbgrader / otter-grader** (BSD) | **No existe en abierto** — Gradescope/Turnitin, propietarios |
    | Corrección manual en el mismo flujo | **nbgrader** | Rúbrica suelta, fuera de la herramienta |
    | Capa de agente | **jupyter-ai** (BSD, ACP+MCP) | `ArguLens` (Apache-2.0, **2 ★**) es lo único, y es scoring de ensayo argumentativo, no entorno |

    **Es la mitad del gap 6 que este pase no cierra, vista desde el lado de la oferta en vez del de la corrección.** Y es un gap de **ausencia de producto**, como el 18: no es que lo haya y no se adopte (gap 1), ni que la licencia moleste (gap 11). No está construido.

    ⚠️ **Y hay una razón para no apurarse a construirlo.** En EMEA (Anexo III, 2027-12-02), Corea y ahora **Vietnam** (trend 31), la evaluación automática del alumno es **alto riesgo con expediente de conformidad obligatorio**. Un entorno de corrección de prosa es exactamente eso. La forma defendible es la del patrón **P14** —calificar sin que califique el modelo— y la del **P29**: el agente explica y evidencia, el docente decide. Construir el autograder de ensayo «a secas» es construir el pasivo regulatorio.

22. **La educación especial ya tiene con qué medirse, es permisiva, y nadie la está midiendo** *(agregado en el pase 13 del 2026-10-01)*. El pase 8 abrió la capa de accesibilidad y educación especial y dejó dos conclusiones: **lo maduro es copyleft** (OptiKey 4.4k ★ GPL-3.0, Cboard 759 ★ GPL-3.0) y **lo agéntico y permisivo no pasa de 15 estrellas**. Faltaba una tercera que no se buscó: **la capa no tenía ninguna forma de evaluarse.**

    Ahora la tiene. **`SEND`**, el segundo componente de `pedagogy-benchmark` (https://github.com/AI-for-Education/pedagogy-benchmark, **MIT** ✅, 12 ★), son **223 preguntas de *Special Educational Needs and Disabilities*** tomadas de exámenes de habilitación docente, con licencia permisiva y publicadas con paper (arXiv 2506.18710).

    **Es la primera pieza de evaluación de educación especial de esta KB, y tiene 12 estrellas.** O sea: la forma del gap es la del **gap 1**, no la del 18. No falta el artefacto — **falta que alguien lo use**. Y eso lo vuelve barato de cerrar: medir un asistente de educación especial contra `SEND` es integración, no investigación.

    **Por qué importa más que su tamaño.** El pase 8 documentó que en North America redactar el IEP con AI está prohibido o restringido en varios estados, y que por eso el patrón **P18** pone el límite adelante (el agente propone, el docente decide). El problema de ese patrón siempre fue **cómo demostrarle al distrito que el asistente es competente** sin tocar la decisión protegida. `SEND` es exactamente ese instrumento: mide **conocimiento pedagógico de educación especial del modelo**, que es lo que se puede acreditar, y no la decisión sobre el alumno, que es lo que no se puede automatizar. Ver el patrón **P30**.

    ⚠️ **Los límites, y son los mismos de todo `pedagogy-benchmark`:** mide conocimiento **declarativo** (responder un examen de habilitación), no calidad de intervención con un alumno real; son 12 ★ y 5 commits, así que es vara de medición en un entregable, **no dependencia de producto**; y el paper no se pudo abrir en este pase (`arxiv.org` bloqueado por el proxy), aunque licencia, conteos y composición **sí** están verificados en la página del repo.


## Fuentes

Nuevo en el pase 13 — capa de práctica y corrección desplegada (verificado vía WebFetch el 2026-10-01): [jupyterhub](https://github.com/jupyterhub/jupyterhub) · [jupyter-ai](https://github.com/jupyterlab/jupyter-ai) · [nbgrader](https://github.com/jupyter/nbgrader) · [nbgrader releases v0.9.6](https://github.com/jupyter/nbgrader/releases) · [otter-grader](https://github.com/ucbds-infra/otter-grader) · [ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) · [jupyterhub-deploy-teaching](https://github.com/jupyterhub/jupyterhub-deploy-teaching) · [Aalto Scientific Computing — autograding](https://scicomp.aalto.fi/aalto/jupyterhub-instructors/autograding/) · [Aalto — nbgrader basics](https://scicomp.aalto.fi/aalto/jupyterhub-instructors/nbgrader/)

Nuevo en el pase 13 — evaluación pedagógica y docente: [pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) · [AI-for-Education (organización)](https://github.com/AI-for-Education) · [microsoft/Shiksha-Copilot](https://github.com/microsoft/Shiksha-Copilot) · [Shiksha Copilot — sitio del proyecto](https://deeshib.github.io/shiksha-copilot/) · [Microsoft Research — diseño con docentes de India](https://www.microsoft.com/en-us/research/blog/teachers-in-india-help-microsoft-research-design-ai-tool-for-creating-great-classroom-content/)

Nuevo en el pase 13 — regulación de Vietnam (educación como alto riesgo): [Allen & Gledhill — marco basado en riesgo, en vigor 2026-03-01](https://www.allenandgledhill.com/vn/publication/articles/32667/s-new-law-on-artificial-intelligence-risk-based-regulatory-framework-in-force-1-march-2026) · [Allen & Gledhill — lista sectorial de alto riesgo, seis sectores](https://www.allenandgledhill.com/perspectives/articles/33373/vnkh-vietnam-identifies-high-risk-ai-systems-across-six-sectors) · [China Briefing — 46 sistemas de alto riesgo](https://www.china-briefing.com/china-outbound-news/46-high-risk-ai-systems-to-face-enhanced-regulatory-oversight-in-vietnam) · [Baker McKenzie](https://www.bakermckenzie.com/en/insight/publications/2026/02/vietnam-artificial-intelligence-law-foundation-and-outlook) · [Tilleke & Gibbins](https://www.tilleke.com/insights/a-closer-look-at-vietnams-new-ai-law-what-it-means-for-ai-businesses/51/) · [VILAF — obligaciones desde 2026-03-01](https://www.vilaf.com.vn/blog/vietnam-enacts-its-first-law-on-artificial-intelligence-key-regulatory-obligations-from-1-march-2026/)

Nuevo en el pase 13 — LATAM institucional y regulatorio: [UNESCO IESALC — estudio 2026-09-09](https://www.iesalc.unesco.org/en/articles/new-unesco-iesalc-study-reveals-widespread-ai-adoption-higher-education-across-latin-america-and) 🔴 *dominio bloqueado por el proxy; las cifras vienen de resultados de búsqueda* · [UNESCO Digital Learning Week 2026](https://www.unesco.org/en/weeks/digital-learning) · [Plan Nacional de IA de México — ATDT (PDF)](https://www.portal.atdt.gob.mx/wp-content/uploads/2026/06/Plan-Nacional-de-IA.pdf) · [Polifonía — olas regulatorias LATAM 2026-2030](https://polifonia.org/2026-2030-regulacion-ia-en-america-latina/)

Nuevo en el pase 13 — North America, legislación educativa: [MultiState — tendencias de política estatal 2026](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session) · [NASBE — gobernanza del uso de AI en escuelas](https://www.nasbe.org/states-take-next-steps-on-governing-ai-use-in-schools/) · [ExcelinEd — hitos de política K-12 2026](https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/) · [AI for Education — guía estatal](https://www.aiforeducation.io/ai-resources/state-ai-guidance)

Mercado y players: [Grand View Research](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-education-market-report) · [Research and Markets](https://www.researchandmarkets.com/reports/5896034/ai-in-education-market-report) · [AI Tutors Market](https://www.grandviewresearch.com/industry-analysis/ai-tutors-market-report) · [5WPR EdTech AI Visibility Index 2026](https://www.5wpr.com/research/edtech-ai-visibility-index-2026/) · [Khan Academy / Duolingo agents](https://callsphere.ai/blog/ai-agents-education-khan-academy-duolingo-autonomous-tutoring)

Capa predictiva, Apereo y licencia ECL-2.0 — agregado en el pase 11: [sakai](https://github.com/sakaiproject/sakai) · [opencast](https://github.com/opencast/opencast) · [uPortal](https://github.com/uPortal-Project/uPortal) · [OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) · [LearningAnalyticsProcessor](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) · [OpenLRS (archivado)](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS) · [OpenDashboard-legacy](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy) · [OpenDashboard-ux](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-ux) · [OpenDashboard-api](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) · [Larissa](https://github.com/Apereo-Learning-Analytics-Initiative/Larissa) · [terracotta](https://github.com/terracotta-education/terracotta) · [aira](https://github.com/GoogleCloudPlatform/aira) · [Student-Retention-Prediction](https://github.com/Aliipou/Student-Retention-Prediction) · [student-early-warning](https://github.com/dssg/student-early-warning) · [SIH-2026 / DropGuard](https://github.com/novatrix-2030/SIH-2026) · licencia: [SPDX ECL-2.0](https://spdx.org/licenses/ECL-2.0.html)

Nuevos en el pase 11 — agentes, currículo y plataformas: [Gnos](https://github.com/madhvantyagi/Gnos) · [Alvarmethod](https://github.com/vasanthsreeram/Alvarmethod) · [learn](https://github.com/amosblomqvist/learn) · [korean-elementary-learning-map](https://github.com/DECK6/korean-elementary-learning-map) · [ai-builders-curriculum](https://github.com/ai-builders-foundation/ai-builders-curriculum) · [classmoji](https://github.com/classmoji/classmoji) · [Milky-institute-online](https://github.com/jude-miller-dev/Milky-institute-online) · [tadreeblms](https://github.com/Tadreeb-LMS/tadreeblms) · [dsh-openmaic](https://github.com/THU-MAIC/dsh-openmaic)

Datos de deserción — agregado en el pase 11 (🔴 ninguno leído de primera mano, dominios bloqueados por el proxy): OULAD · `https://analyse.kmi.open.ac.uk/open_dataset` · UCI 697 · `https://archive.ics.uci.edu/dataset/697` · benchmark de supervivencia · `arXiv 2604.08870`

Regulación del pase 11 (🔴 fuentes secundarias coincidentes; primarias bloqueadas): Reglamento (UE) 2026/1744 (Digital Omnibus on AI) · EU AI Act Anexo III · legislación estatal de EE. UU. 2026 (134 proyectos en 31 estados; MD, ID, OK, VA; California AB 1159; Idaho SB 1227) · Ley Básica de IA de Taiwán (en vigor 2026-01-14) · sectores de alto riesgo de Vietnam · UNESCO IESALC (200 instituciones, 19 países) · Digital Education Council LATAM 2026 (30.000+ respuestas, 29 instituciones)

Credenciales verificables e interoperabilidad — agregado en el pase 9: [learner-credential-wallet](https://github.com/digitalcredentials/learner-credential-wallet) · [verifier-plus](https://github.com/digitalcredentials/verifier-plus) · [issuer-coordinator](https://github.com/digitalcredentials/issuer-coordinator) · [qti3-item-player](https://github.com/amp-up-io/qti3-item-player) · [esco-skill-extractor](https://github.com/KonstantinosPetrakis/esco-skill-extractor) · [oneroster (TypeScript)](https://github.com/LongsightGroup/oneroster) · [lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) · [openbadges-specification](https://github.com/1EdTech/openbadges-specification) · [tao-core](https://github.com/oat-sa/tao-core) · [openbadgeslib](https://github.com/luisgf/openbadgeslib) · [caliper-php-public (U. de Michigan)](https://github.com/tl-its-umich-edu/caliper-php-public) · [European Learning Model (archivado)](https://github.com/european-commission-empl/European-Learning-Model) · [European Digital Credentials (archivado)](https://github.com/european-commission-empl/european-digital-credentials) · [Open Badges 3.0 — guía de implementación 1EdTech](https://standards.1edtech.org/open-badges/guides/standards/v3p0/impl) · [Europass — información para desarrolladores](https://europass.europa.eu/en/information-developers)

Evaluación y seguridad pedagógica — agregado en el pase 5: [SafeTutors (repo)](https://github.com/RadiantCrystal/SafeTutors) · [EduBench (repo)](https://github.com/ybai-nlp/EduBench) · [EduGuardBench (repo)](https://github.com/YL1N/EduGuardBench) · [EduFrameTrap / sycophancy (arXiv 2605.14604)](https://arxiv.org/abs/2605.14604) · [ELBench (arXiv 2608.09548)](https://arxiv.org/abs/2608.09548) · [SafeTutors (arXiv 2603.17373)](https://arxiv.org/abs/2603.17373) · [EduGuardBench (arXiv 2511.06890)](https://arxiv.org/abs/2511.06890)

Modelado y modelos — agregado en el pase 5: [pyBKT](https://github.com/CAHLR/pyBKT) · [OmniEdu (repo)](https://github.com/haolpku/Omni-Edu) · [OmniEdu (arXiv 2609.23088)](https://arxiv.org/abs/2609.23088)

Teacher-facing y grading — agregado en el pase 5: [Aila / Oak National Academy](https://github.com/oaknational/oak-ai-lesson-assistant) · [rubric](https://github.com/paper-instruments/rubric) · [llmgrader](https://github.com/sdrangan/llmgrader) · [Autograder.io](https://github.com/eecs-autograder/autograder.io)

Mercado y regulación — agregado en el pase 5: [UNESCO IESALC / UNU — AI Implementation in Higher Education in LAC](https://unu.edu/publication/ai-implementation-higher-education-latin-america-and-caribbean) · [Times Higher Education — uneven AI adoption in Latin America](https://www.timeshighereducation.com/node/744954) · [Council of Europe — 3rd Working Conference & Compass for AI and Education](https://www.coe.int/en/web/education/-/artificial-intelligence-and-education-third-working-conference) · [MarketsandMarkets — North America AI in Education](https://www.marketsandmarkets.com/Market-Reports/geography/ai-in-education-market/North-America) · [AfriLabs / WISE — Harnessing AI for Higher Education in Africa](https://www.afrilabs.com/?p=7452)

Capa de datos de entrenamiento (KT datasets) — agregado en el pase 7: [EdNet](https://github.com/riiid/ednet) · [XES3G5M](https://github.com/ai4ed/XES3G5M) · [FoundationalASSIST (arXiv 2602.00070)](https://arxiv.org/abs/2602.00070) · [XES3G5M (OpenReview)](https://openreview.net/pdf?id=Mn9oHNdYCE)

Tutores y memoria de agente — agregado en el pase 7: [tutor-gpt](https://github.com/plastic-labs/tutor-gpt) · [Honcho](https://github.com/plastic-labs/honcho) · [ChatTutor](https://github.com/HugeCatLab/ChatTutor) · [llamatutor](https://github.com/Nutlope/llamatutor) · [ABench / ProHist-Bench](https://github.com/inclusionAI/ABench) · [ProHist-Bench (arXiv 2604.24690)](https://arxiv.org/abs/2604.24690)

Seguridad pedagógica — agregado en el pase 7: [EduZone (arXiv 2608.02024)](https://arxiv.org/abs/2608.02024) · [AIriskEval-edu (arXiv 2607.01934)](https://arxiv.org/abs/2607.01934) · [L2-Bench (arXiv 2607.08842)](https://arxiv.org/abs/2607.08842) · [L2-Bench (sitio OUP)](https://benchmarks.elt.edu.oup.com/)

Capa de contenido curricular (OER) — agregado en el pase 10: [osbooks-calculus-bundle](https://github.com/openstax/osbooks-calculus-bundle) · [osbooks-biology-bundle](https://github.com/openstax/osbooks-biology-bundle) · [osbooks-college-physics-bundle](https://github.com/openstax/osbooks-college-physics-bundle) · [openstax-mcp-server](https://github.com/pythpythpython/openstax-mcp-server) · [mcp-tutor](https://github.com/moarshy/mcp-tutor) · [DSpace](https://github.com/DSpace/DSpace) · [Pressbooks](https://github.com/pressbooks/pressbooks) · [Manifold](https://github.com/ManifoldScholar/manifold) · [openstax-cms](https://github.com/openstax/openstax-cms) · [LibreTexts/shapeshift](https://github.com/LibreTexts/shapeshift) · [LibreTexts/conductor](https://github.com/LibreTexts/conductor) · [Creative Commons — Using CC-Licensed Works for AI Training](https://creativecommons.org/using-cc-licensed-works-for-ai-training-2/) · [Schools Week — Oak will allow commercial use of its lessons](https://schoolsweek.co.uk/oak-national-academy-will-allow-commercial-use-of-its-lessons/)

Infraestructura pública desplegada — agregado en el pase 10: [SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) · [Sunbird-Ed (org)](https://github.com/Sunbird-Ed) · [project-sunbird (org)](https://github.com/project-sunbird) · [Ed-Fi-ODS](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) · [Ed-Fi-Data-Standard](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) · [Ed-Fi — what is Ed-Fi](https://www.ed-fi.org/what-is-ed-fi/) · [DPI Global — DIKSHA](https://dpi.global/globaldpi/diksha) · [EkStep — DIKSHA learnings](https://ekstep.org/)

Mercado y política por región — agregado en el pase 10: [Technavio — AI in the education sector](https://technavio.com/report/artificial-intelligence-market-in-the-education-sector-industry-analysis) · [Azumo — AI in education statistics 2026](https://azumo.com/artificial-intelligence/ai-insights/ai-in-education-statistics) · [TechWire Asia — India AI curriculum from Class 3](https://techwireasia.com/2025/11/india-ai-curriculum-schools-2026/) · [TechWire Asia — mandatory AI literacy: China joins UAE and India](https://techwireasia.com/2026/04/ai-literacy-national-education-workforce/) · [ABC News — why some countries are moving fast on AI in schools](https://www.abc.net.au/news/2026-05-31/schools-in-asia-embracing-ai/106703054) · [Council of Europe — AI and education](https://www.coe.int/en/web/education/artificial-intelligence-and-education) · [CompTIA — five tech trends shaping EMEA IT strategy 2026](https://www.comptia.org/en/blog/five-tech-trends-shaping-emeas-it-strategy-in-2026/) · [UNU/UNESCO — AI implementation in higher education in LAC](https://unu.edu/publication/ai-implementation-higher-education-latin-america-and-caribbean) · [BID — An Enabling Regulatory Framework for AI in LAC](https://publications.iadb.org/publications/english/document/An-Enabling-Regulatory-Framework-for-Artificial-Intelligence-in-Latin-America-and-the-Caribbean.pdf)

Regulación y mercado por región — agregado en el pase 7: [MultiState — AI in Education Legislation: 2026 State Policy Trends](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session) · [ExcelinEd — State K-12 AI Policy in 2026](https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/) · [NASBE — States Take Next Steps on Governing AI Use in Schools](https://www.nasbe.org/states-take-next-steps-on-governing-ai-use-in-schools/) · [AASA — National framework for AI from students in all 50 states](https://www.aasa.org/news-media/news/2026/08/03/students-produce-national-framework-for-ai-in-america's-schools) · [Latham & Watkins — AI Regulation in APAC](https://www.lw.com/en/insights/ai-regulation-in-apac-diverging-approaches-across-the-region) · [CX Network — How 9 APAC countries are regulating AI](https://www.cxnetwork.com/artificial-intelligence/articles/ai-regulation-in-apac-current-developments-and-key-areas) · [Ken Research — Asia-Pacific AI in Education Market](https://www.kenresearch.com/industry-reports/asia-pacific-ai-in-education-market) · [UNESCO — Observatory on AI in Education for LAC](https://www.unesco.org/en/articles/unesco-launches-observatory-artificial-intelligence-education-latin-america-and-caribbean) · [UNESCO — Public–private partnership advances the Regional Observatory](https://www.unesco.org/en/articles/public-private-partnership-advances-regional-observatory-artificial-intelligence-education-led) · [EU AI Act — regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

Accesibilidad y educación especial — agregado en el pase 8: [accessibility-agents](https://github.com/Community-Access/accessibility-agents) · [OptiKey](https://github.com/OptiKey/OptiKey) · [Cboard](https://github.com/cboard-org/cboard) · [tero](https://github.com/marcorojasb/tero) · [Ronda App](https://github.com/ronda-ai/Ronda-App) · [noggimigo](https://github.com/Noggin-Labs/noggimigo) · [Swar-Setu](https://github.com/AyushBinjola1/Swar-Setu) · [aba-clinical-agent](https://github.com/open-behavior-analysis/aba-clinical-agent) · [Teacher-Hub / UnStuck](https://github.com/SabioTechTeam/Teacher-Hub) · [EyeEP](https://github.com/100205ivan/EyeEP) · [SEALApplication](https://github.com/Autism-Technology-Research-Syndicate/SEALApplication) · [Sign-Language-Interpreter](https://github.com/classifiedstudentkabir/Sign-Language-Interpreter)

Accesibilidad — regulación y mercado, pase 8: [European Accessibility Act — impacto en e-learning (BESA)](https://www.besa.org.uk/news/the-european-accessibility-act-eaa-and-its-impact-on-e-learning-what-you-need-to-know/) · [EAA y LMS (Synergy Learning)](https://synergy-learning.com/blog/european-accessibility-act-eaa-lms/) · [EAA para e-learning (ReadSpeaker)](https://www.readspeaker.com/blog/european-accessibility-act-e-learning/) · [US ED — Final Priority on Advancing AI in Education (Federal Register, 2026-04-13)](https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing) · [AI for Education — State AI Guidance tracker](https://www.aiforeducation.io/ai-resources/state-ai-guidance) · [NYC Public Schools — AI guidance for educators (2026-03-24)](https://www.schools.nyc.gov/home/2026/03/24/new-york-city-public-schools-announces-release-of-ai-guidance-for-educators-and-school-leaders) · [CIDDL — Navigating AI in IEP Development](https://ciddl.org/navigating-ai-in-iep-development-a-framework-for-ethical-practice/) · [Open edX — Proctoring UI proposal](https://openedx.atlassian.net/wiki/spaces/OEPM/pages/5336334337/Proposal+Proctoring+UI+A+Free+Open+Source+Browser-Lockdown+and+AI-Assisted+Exam+Integrity+Tool) · [Ipsos Education Monitor 2026 — APAC](https://www.ipsos.com/en-th/different-rules-different-technologies-how-asia-pacific-thinking-about-education-ai-and-future)

⚠️ *Del pase 8: los doce enlaces a `github.com` se abrieron de primera mano (licencia, stars, commits y descripción leídos en la página del repo). Los enlaces de **regulación y mercado provienen de resultados de búsqueda, no de la página abierta** — incluidas las fechas del EAA y las prohibiciones de IEP de Delaware y Nueva York. **Confirmar el texto normativo antes de citarlo en material de cliente.***


⚠️ *Del pase 7: se abrieron de primera mano sólo los enlaces a `github.com`. `arxiv.org`, `huggingface.co`, `benchmarks.elt.edu.oup.com` y `aivet-training.eu` están **bloqueados por el proxy de egreso** (reintentados en este pase); las fuentes de regulación y mercado provienen de resultados de búsqueda, no de la página abierta. Se dejan los enlaces para que una corrida con otra configuración de red los verifique.*

⚠️ *De las fuentes del pase 5, sólo los enlaces a `github.com` pudieron abrirse: `arxiv.org`, `unu.edu`, `coe.int`, `aclanthology.org` y `huggingface.co` están bloqueados por el proxy de egreso de este entorno. Se dejan los enlaces para que una corrida con otra configuración de red los verifique.*

Regulación — agregado en el pase 3: [Korea AI Basic Act guide (Casrai)](https://casrai.org/guides/korea-ai-basic-act) · [Latham & Watkins — AI regulation in APAC](https://www.lw.com/en/insights/ai-regulation-in-apac-diverging-approaches-across-the-region) · [KJK — Ohio's July 1 2026 school AI policy deadline](https://kjk.com/2026/06/12/ohios-july-1-2026-school-ai-policy-deadline-what-districts-educators-and-parents-need-to-know/) · [EdWeek — Ohio requires AI policies for all K-12 schools](https://marketbrief.edweek.org/regulation-policy/ohio-is-requiring-ai-policies-for-all-k-12-schools-will-other-states-follow/2025/08) · [Ohio DEW model AI policy (PDF)](https://education.ohio.gov/getattachment/Topics/AI-in-Ohio-s-Education/Model-Policy/AI-In-Education-Model-Policy.pdf.aspx?lang=en-US) · [Williams Mullen — Virginia AI guidance for schools](https://www.williamsmullen.com/insights/news/legal-news/virginia-establish-guidance-artificial-intelligence-schools) · [VPM — HB 1186 / SB 394](https://www.vpm.org/general-assembly/2026-03-25/hb1186-sb394-ai-guidance-schools-pekarsky-rasoul-spanberger-heny/) · [FutureEd — 2026 state AI in education bill tracker](https://www.future-ed.org/legislative-tracker-2026-state-ai-in-education-bills/)

Repos y verticales — pase 3: [Claw-ED](https://github.com/SirhanMacx/Claw-ED) · [GegoK12](https://github.com/Gego-K12/gegok12) · [AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent)

Mercado regional — pase 3: [Azumo — AI in education statistics 2026](https://azumo.com/artificial-intelligence/ai-insights/ai-in-education-statistics) · [EdTech Hub — AI in education in MENA](https://docs.edtechhub.org/lib/EPJAMMH9/download/BHXDDPBB) · [Ipsos — APAC education, AI and the future](https://www.ipsos.com/en-th/different-rules-different-technologies-how-asia-pacific-thinking-about-education-ai-and-future)

Regulación: [MultiState — AI in education legislation 2026](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session) · [ExcelinEd — K-12 AI policy 2026](https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/) · [EU AI Act in education](https://aiadopt.eu/en/insights/eu-ai-act-education) · [Uniwise — Annex III diciembre 2027](https://uniwise.eu/resources/blog/the-eu-ai-act-and-assessment-december-2027-is-not-a-snooze-button) · [Xenoss — APAC AI regulations](https://xenoss.io/blog/asia-pacific-apac-ai-regulations) · [FPF — AI regulation in Latin America](https://fpf.org/blog/ai-regulation-in-latin-america-overview-and-emerging-trends-in-key-proposals/) · [Baker McKenzie — LATAM AI regs](https://connectontech.bakermckenzie.com/emerging-ai-regulations-in-latin-america-what-multinationals-need-to-know/)

Plataformas y repos: [Moodle AI tools docs](https://docs.moodle.org/502/en/AI_tools) · [Moodle AI plugin types](https://moodledev.io/docs/5.0/apis/plugintypes/ai) · [Moodle 5.2 release](https://edzlms.com/moodle-5-2-release-ai-integration-smarter-courses-elearning/) · [AITutor-EvalKit (arXiv 2512.03688)](https://arxiv.org/abs/2512.03688) · [Latam-GPT / CENIA](https://www.opensourceforu.com/2026/02/chile-launches-open-source-latam-gpt-to-power-latin-americas-ai-sovereignty/)

LATAM: [Nivelics — impacto AI empresas LATAM 2026](https://www.nivelics.com/en/blog/impacto-ia-empresas-latam-2026) · [VuraOS — mapa de adopción LATAM](https://vuraos.com/en/blog-mapa-adopcion-latam)

**Agregado en el pase 4 (2026-09-30):**

Regulación EMEA — Digital Omnibus: [Gibson Dunn — EU AI Act Omnibus agreement, postponed high-risk deadlines](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) · [Usercentrics — EU AI Act high-risk delay, Article 50 transparency](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/) · [Uniwise — December 2027 is not a snooze button (assessment)](https://uniwise.eu/resources/blog/the-eu-ai-act-and-assessment-december-2027-is-not-a-snooze-button) · [European Commission — AI Act regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

Regulación APAC: [Latham & Watkins — AI regulation in APAC](https://www.lw.com/en/insights/ai-regulation-in-apac-diverging-approaches-across-the-region) · [CX Network — how 9 APAC countries regulate AI](https://www.cxnetwork.com/artificial-intelligence/articles/ai-regulation-in-apac-current-developments-and-key-areas) · [OneTrust — where AI regulation is heading in 2026](https://www.onetrust.com/blog/where-ai-regulation-is-heading-in-2026-a-global-outlook/)

Regulación North America: [MultiState — AI in education legislation, 2026 state policy trends](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session) · [NASBE — states take next steps on governing AI use in schools](https://www.nasbe.org/states-take-next-steps-on-governing-ai-use-in-schools/) · [ExcelinEd — K-12 AI policy 2026 milestones](https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/) · [AASA — students from all 50 states produce national AI framework](https://www.aasa.org/news-media/news/2026/08/03/students-produce-national-framework-for-ai-in-america's-schools)

Mercado LATAM: [Digital Education Council — AI in Higher Education LATAM Survey 2026](https://www.digitaleducationcouncil.com/dec-insights/92-of-students-and-79-of-faculty-actively-engaging-with-ai-findings-from-ai-in-higher-education-latam-survey-2026) · [DEC — AI adoption nearly universal among students](https://www.digitaleducationcouncil.com/post/ai-adoption-is-nearly-universal-among-students-but-confidence-is-not)

Mercado APAC y global: [Ken Research — Asia-Pacific AI in education market to 2030](https://www.kenresearch.com/industry-reports/asia-pacific-ai-in-education-market) · [HolonIQ — 2026 education trends snapshot](https://www.holoniq.com/notes/2026-education-trends-snapshot) · [Azumo — AI in education statistics 2026](https://azumo.com/artificial-intelligence/ai-insights/ai-in-education-statistics)

Repos y benchmarks: [MathTutorBench](https://github.com/eth-lre/mathtutorbench) · [UnifyingAITutorEvaluation](https://github.com/kaushal0494/UnifyingAITutorEvaluation) · [pyKT](https://github.com/pykt-team/pykt-toolkit) · [TutorIA](https://github.com/LabSirius/TutorIA) · [OpenDidactia](https://github.com/nmarafo/OpenDidactia) · [FreeLingo](https://github.com/artcc/freelingo) · [mentar](https://github.com/avps82/mentar)

Capa de telemetría (LRS / xAPI) — agregado en el pase 6, **todo verificado de primera mano en GitHub**: [lrsql (Yet Analytics)](https://github.com/yetanalytics/lrsql) · [Ralph (OpenFun)](https://github.com/openfun/ralph) · [ADL_LRS (ADL)](https://github.com/adlnet/ADL_LRS) · [Learning Locker](https://github.com/LearningLocker/learninglocker) · [learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) · [ERPNext](https://github.com/frappe/erpnext)

Evaluación — agregado en el pase 6, 🔴 **no verificado de primera mano** (dominios bloqueados por el proxy): L2-Bench (arXiv 2607.08842) · metodología de L2-Bench (arXiv 2603.20088) · `benchmarks.elt.edu.oup.com` · dataset en HuggingFace bajo `OUP/`

Regulación y mercado por región — agregado en el pase 6: [MultiState — AI in Education Legislation: 2026 State Policy Trends](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session) · [NASBE — States Take Next Steps on Governing AI Use in Schools](https://www.nasbe.org/states-take-next-steps-on-governing-ai-use-in-schools/) · [ExcelinEd — State K-12 AI Policy in 2026](https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/) · [Latham & Watkins — AI Regulation in APAC](https://www.lw.com/en/insights/ai-regulation-in-apac-diverging-approaches-across-the-region) · [Xenoss — APAC AI regulations](https://xenoss.io/blog/asia-pacific-apac-ai-regulations) · [UNESCO — Observatory on AI in Education for LAC](https://www.unesco.org/en/articles/unesco-launches-observatory-artificial-intelligence-education-latin-america-and-caribbean) · [Compliance & Risks — LATAM AI legislation](https://www.complianceandrisks.com/blog/shaping-the-future-ai-legislative-initiatives-across-latin-america/) · [IDB — An Enabling Regulatory Framework for AI in LAC](https://publications.iadb.org/publications/english/document/An-Enabling-Regulatory-Framework-for-Artificial-Intelligence-in-Latin-America-and-the-Caribbean.pdf) · [Azumo — AI in Education Statistics 2026](https://azumo.com/artificial-intelligence/ai-insights/ai-in-education-statistics) · [Grand View Research — AI Tutors Market](https://www.grandviewresearch.com/industry-analysis/ai-tutors-market-report) · [EdTech Hub — AI in Education in MENA](https://docs.edtechhub.org/lib/EPJAMMH9/download/BHXDDPBB)

## Nota de método del pase 13 (2026-10-01) — trece pasadas buscando por el rol del software, y la pregunta que faltaba era dónde trabaja el alumno

El pase 7 dejó escrita una regla: *«cuando un gap sobrevive varias pasadas, revisar si la pieza que falta existe con otro
nombre»*. Este pase la aplica al gap que más había sobrevivido —el **6**, once pasadas sin cambios— y encuentra que la
pieza no sólo existía: **era el repo con más estrellas de toda la KB.**

**Qué cambió en la consulta, y es replicable.** Las doce pasadas anteriores buscaron por **el rol del software**:
«tutor», «agente educativo», «LMS», «grading», «early warning», «skills pedagógicas». Este pase buscó por **el artefacto
material del alumno**: dónde escribe, qué entrega, dónde se ejecuta. Esa consulta devuelve Jupyter, que no se presenta
como producto educativo y por eso nunca apareció. **Es la quinta vez que esta KB registra que la consulta equivocada
costó pasadas** (pases 4, 5, 6, 7 y 13).

**La regla que agrega este pase, para la pasada 14 y las siguientes:** buscar al menos una vez por **el objeto físico o
digital que el alumno produce** —el cuaderno, el entregable, el examen, el portfolio, el instrumento de medición— y no
sólo por el rol del software que lo rodea. Las dos veces que esta KB lo hizo encontró capas enteras: el **contenido**
(pase 10, «de qué lee el tutor») y la **práctica** (este pase, «dónde trabaja el alumno»).

### ⚠️ Advertencia 1 — una fuente secundaria hizo regresar la fecha del EU AI Act, y hay que no copiarla

Una guía comercial sobre el AI Act en educación, consultada en este pase, afirma que la fecha de aplicación general fue
el **2026-08-02**. **El trend 25 de esta KB documenta, con fuentes primarias, que el Digital Omnibus on AI entró en vigor
el 2026-07-27 y corrió el Anexo III —que es el que cubre educación— al 2027-12-02.** La discrepancia se registra
explícitamente: **la fecha operativa sigue siendo 2027-12-02**, y una pasada futura que cite esa clase de guía sin
contrastarla va a hacer regresar el dato más importante del archivo.

### ⚠️ Advertencia 2 — el hallazgo del pase es grande y conviene no sobrevenderlo

La pila Jupyter es real, permisiva y está desplegada, pero **corrige una mitad del gap 6, no el gap entero**. Lo que
corrige: corrección de trabajo **ejecutable**. Lo que **no** corrige: prosa (sigue propietario), evaluación
**pedagógica** (gap 1, intacto), modelado del alumno (gap 5, intacto) y formación profesional (gap 10, intacto). Y
`nbgrader` está **fuertemente acoplado a JupyterHub**: fuera de ahí el flujo de entrega se complica, y la pieza correcta
pasa a ser `otter-grader`. Un entregable que presente «resolvimos el grading con open source» sin esas cuatro
limitaciones va a fallar en la primera facultad de humanidades.

### Lo que este pase NO hizo, declarado como tal

- **No revalidó las 179 URLs de GitHub preexistentes de esta KB.** Se verificaron de primera mano, vía WebFetch, **las
  7 nuevas** (los 5 de la pila Jupyter, `pedagogy-benchmark` y `Shiksha-Copilot`) más la organización `AI-for-Education`.
  La advertencia del pase 12 sigue vigente: **`curl` a github.com devuelve 403 en este entorno por el proxy, no por *link
  rot***, y la verificación de primera mano se hace con WebFetch.
- **No abrió el paper de `pedagogy-benchmark`** (arXiv 2506.18710): `arxiv.org` sigue bloqueado. Licencia, conteos,
  composición CDPK/SEND y la atribución al Ministerio de Educación de Chile **sí** están leídos de la página del repo.
- **No abrió el estudio de UNESCO IESALC**: `www.iesalc.unesco.org` está bloqueado por el proxy. Las cifras del trend 32
  (87% / 74% / 57% / 26%, 200 instituciones, 19 países, 2026-09-09) vienen de **resultados de búsqueda concordantes**,
  no del documento. Están marcadas como tales en `intel/market.md`.
- **No verificó de primera mano el despliegue de 1.043 docentes de Shiksha Copilot** — viene de la literatura
  secundaria y del sitio del proyecto, no de un documento del Gobierno de Karnataka. Lo que **sí** está verificado en la
  página del repo es licencia MIT, 9 ★, 12 forks, 149 commits y la advertencia de no-producción.
- **No buscó la capa de práctica para materias no ejecutables más allá de confirmar que no existe** (gap 21). Queda
  explícitamente para la pasada 14.

## Nota de método del pase 12 (2026-10-01) — doce pasadas comparando la educación consigo misma, y dos advertencias de verificación que van a volver a pasar

**El cambio de método del pase.** Las once pasadas anteriores compararon artefactos educativos **entre sí**: de ahí
salieron todos los "techos" de esta KB (el techo de la capa predictiva, el de accesibilidad permisiva, el de los MCP de
mastery). Este pase cambió el denominador y comparó **la vertical educativa contra otra vertical en el mismo canal de
distribución**. Es lo que produjo la tendencia 28, y no se podía ver desde adentro de la vertical.

**Qué se verificó de primera mano.** Los **diez repos nuevos** de este pase (los siete paquetes pedagógicos, los dos
baseline de otras verticales y `anki-mcp-server`), más Anki y DeepTutor: licencia, estrellas, lenguaje y descripción
leídos vía **WebFetch contra la página del repo** el 2026-10-01. La licencia de Anki se verificó **en el archivo
`LICENSE`**, no en el README —**AGPL-3.0-or-later**, con porciones de contribuyentes bajo BSD-3—, siguiendo la regla
que el pase 10 dejó escrita.

### ⚠️ Advertencia 1 — los agregadores de estrellas de terceros están mal, no viejos

| Repo | Agregador de terceros | Página del repo (mismo día) | Error |
|---|---|---|---|
| `K-Dense-AI/scientific-agent-skills` | 26.500 ★ (ossinsight) | **47.200 ★** | **−44%** |
| `virgiliojr94/book-to-skill` | 13.700 ★ (sourcepulse) | **33.200 ★** | **−59%** |

En una categoría que suma **+6.300 ★/mes**, el dato del agregador no es una cifra vieja: es una cifra equivocada, y por
un factor cercano a 2. **Regla: en esta capa sólo vale la página del repo.** Esto concuerda con la corrección que
`rotation.json` ya registraba sobre ciclos anteriores de esta KB ("star counts were pipeline-inflated"): el problema
nunca fue el sentido del error, fue confiar en una fuente intermedia.

### ⚠️ Advertencia 2 — un 403 de `curl` no es un 404, y acá son 164

Se pasaron **las 164 URLs de GitHub de toda esta KB** por `curl -sL` para auditar enlaces muertos. **Las 164 devolvieron
403**, uniformemente — incluidas las de repos que el mismo día se verificaron vivos vía WebFetch (`HKUDS/DeepTutor`,
`moodle/moodle`, `instructure/canvas-lms`). Es **el proxy del entorno bloqueando `curl` hacia github.com**, no *link
rot*.

Dos consecuencias que hay que dejar escritas:

1. **Esas 164 URLs quedan sin revalidar en este pase.** No hay evidencia de que estén caídas **ni de que estén vivas**.
   La auditoría masiva de enlaces de esta KB sigue pendiente.
2. **Un pase futuro que vea 403 masivos no debe interpretarlos como enlaces muertos** ni borrar filas por eso. La
   verificación de primera mano en este entorno se hace con **WebFetch**, que sí resuelve github.com. Es la misma
   restricción que el pase 5 registró sobre el proxy de egreso, ahora medida.

### Lo que este pase NO hizo, declarado como tal

- **No revalidó el inventario histórico de la KB** (ver advertencia 2).
- **No encontró nada nuevo en el barrido regulatorio de North America, EMEA ni LATAM.** Las cuatro consultas regionales
  se corrieron y devolvieron lo que la KB ya tenía registrado. El único hallazgo regulatorio nuevo de las cuatro
  regiones es **la oficialización del libro de texto digital en Japón** (ver `intel/market.md`, `### APAC`). Esto se
  registra como **saturación de la capa regulatoria para esta cadencia**, no como cobertura: doce pasadas en dos días
  sobre las mismas cuatro consultas devuelven lo mismo. **Recomendación: bajar el barrido regulatorio a frecuencia
  semanal** y gastar las corridas en capas sin cubrir.
- **No se midió el tamaño de la capa de skills con una consulta de GitHub Search.** La página `github.com/topics/agent-skills`
  declara **28.111 repos** con ese topic, pero la cifra viene de la misma página cuyos conteos de estrellas resultaron
  inflados, así que **se registra como no verificada y no se usa para ninguna conclusión**. Las conclusiones del pase
  descansan sólo en los repos leídos uno por uno.
- **`github.com/topics/claude-skill` devuelve 404** — ese topic no existe; el canónico es `agent-skills`.

## Nota de método del pase 11 (2026-10-01) — once pasadas preguntando qué hace el software, y la pregunta que faltaba era qué decide

**El cambio de pregunta.** El pase 10 cambió el indicador (de estrellas a despliegue real). Este pase cambia el
**sujeto**: las diez pasadas anteriores preguntaron qué hace el software *con* el alumno —le enseña, lo mide, lo
acredita, lo hace accesible—. Ninguna preguntó qué software **decide sobre** el alumno. Esa es la capa de riesgo de
abandono y *student success*, es la que la institución ya tiene presupuestada, es la que el Anexo III del EU AI Act
nombra literalmente, y está vacía. Ver el gap 18 y las tendencias 25 y 26.

**El error propio que este pase encontró, y es más importante que el hallazgo.** La KB filtraba por **MIT /
Apache-2.0 / BSD**. Ese filtro descartó durante diez pasadas el stack completo de Apereo —**Sakai, 1.234 ★, push de
ayer**— porque su licencia es **ECL-2.0**, que es permisiva, aprobada por OSI y FSF, y no estaba en la lista.
**Un filtro por lista blanca de nombres produce falsos negativos que no dejan rastro:** lo que no apareció no se
puede auditar. La regla corregida está en `repos/foundations.md` y la generalización en la tendencia 27.

**Canales de verificación de este pase, en orden de confianza:**

1. **Metadatos de repo** (estrellas, licencia SPDX, `archived`, último push, forks, fecha de creación) leídos vía la **API de búsqueda de GitHub**. Es la fuente de todas las cifras de repos de este pase. ⚠️ `curl` directo a `api.github.com/repos/...` está **restringido al repositorio de la sesión**, así que no se usó para nada: eso también significa que **no se pudo leer el archivo `LICENSE` por API** en repos de terceros.
2. **Página del repo abierta y leída** para licencia exacta, README, conteo de commits y advertencias del autor. Así se confirmaron ECL-2.0 en Sakai, Opencast, OpenLRW y LearningAnalyticsProcessor, el *proof-of-concept only* de `aira`, y los datos sintéticos de `Student-Retention-Prediction`.
3. **Consultas cuantitativas con sintaxis registrada**, para que valgan como serie y no como anécdota: `topic:learning-analytics stars:>50` y `dropout prediction student license:mit pushed:>2026-01-01`. La próxima pasada debería repetirlas tal cual.
4. **Fuentes secundarias múltiples y coincidentes**, para lo regulatorio y de mercado. Marcado 🔴 cuando es el único canal disponible.

**🔴 Bloqueado por el proxy de egreso en este pase** — todo lo que dependa de estas fuentes está marcado como no
verificado de primera mano: `eur-lex.europa.eu` y `digital-strategy.ec.europa.eu` (texto del Reglamento (UE)
2026/1744), `archive.ics.uci.edu` (licencia exacta del dataset UCI 697), `analyse.kmi.open.ac.uk` (ficha de OULAD),
`arxiv.org` (benchmark de supervivencia 2604.08870), `zenodo.org`, `en.wikipedia.org`.

**Lo que este pase afirma con menos fuerza de la que parecería, a propósito:**

- **La licencia del dataset UCI 697** se registra como "CC BY 4.0 ⚠️ confirmar". El tamaño, las features y la procedencia están verificados contra el descriptor publicado; la licencia, no. **Es la clase de dato que el pase 10 aprendió a no dar por bueno** (ver la tendencia 22).
- **Las fechas del Reglamento (UE) 2026/1744** son consistentes en todas las fuentes secundarias consultadas, con número de reglamento, fechas de votación y fechas de aplicación coincidentes. Aun así: **confirmar en EUR-Lex antes de ponerlas en un documento de cliente.**
- **El benchmark de supervivencia** se registra con su conclusión (señal temporal y conductual, no demográfica) porque es exactamente el argumento que un DPO necesita, y **con la advertencia de que su repositorio está reportado como link roto**: no hay código que auditar.

**Lo que no se buscó y se declara como tal:** los esquemas curriculares nacionales (gap 19). Este pase encontró el
coreano **de casualidad**, igual que el pase 3 encontró el español. Dos hallazgos accidentales del mismo tipo de
artefacto en dos regiones son suficiente evidencia para buscarlo a propósito, y no se hizo en esta corrida.

## Nota de método del pase 10 (2026-10-01) — diez pasadas preguntando qué hace el agente, y la pregunta que faltaba era de qué lee

**Lo que este pase hizo distinto.** Las nueve anteriores buscaron por **capa técnica** (agente, modelado, evaluación,
telemetría, datos), por **categoría de producto** (tutor, plataforma, benchmark), por **población de alumnos** (pase 8) y por
**el final del recorrido** (pase 9, la credencial). Ninguna buscó **la entrada**: el material que el agente enseña. La palabra
**«OER»** no aparecía ni una vez en 549 KB de KB.

Es la **quinta** aplicación de la regla del pase 6 —*cuando un gap sobrevive varias pasadas, revisar si la pieza que falta
tiene un nombre que uno no está usando*— y el nombre era **Open Educational Resources**. Sigue siendo la regla más productiva
de esta KB.

**Y este pase agrega una regla propia, que es el otro hallazgo:** *cuando una capa parece vacía, revisar si el indicador con
el que se la está midiendo sirve para esa capa.* Ordenando por estrellas, **Sunbird —la plataforma que sostiene la educación
escolar de India, 180 M+ alumnos, MIT— tiene 41 estrellas y era invisible.** Tiene **317 forks y 38.046 commits**. En
infraestructura pública el **fork es la unidad de despliegue**, no una señal de interés. Ver el **trend 23**.

**Verificado de primera mano** (WebFetch contra la página del repo, y contra el archivo `LICENSE` donde la afirmación es de
licencia): los tres bundles de contenido de OpenStax (`osbooks-calculus-bundle`, `osbooks-biology-bundle`,
`osbooks-college-physics-bundle`, **CC BY-NC-SA en los tres**), el README de `CAHLR/OATutor` y el de
`pythpythpython/openstax-mcp-server` (**CC BY 4.0 en los dos**), `moarshy/mcp-tutor` (sin licencia), los repos de Sunbird
(`SunbirdEd-portal`, `SunbirdEd-mobile-app`, `SunbirdEd-consumption-ngcomponents`, `sunbird-client-services`,
`SunbirdEd-forms`, `sunbird-devops`, `sunbird-telemetry-sdk`, `sunbird-lms-mw`), los dos de Ed-Fi (`Ed-Fi-ODS`,
`Ed-Fi-Data-Standard`, **Apache-2.0**), y la capa de contenido (`DSpace` BSD-3-Clause, `pressbooks` GPL-3.0+,
`ManifoldScholar/manifold` GPL-3.0, `openstax/openstax-cms` **AGPL-3.0**, y el tooling MIT de LibreTexts: `shapeshift`,
`conductor`, `davis`, `LibreOne`).

**Lo que NO está verificado, y está marcado donde aparece:**

1. **La licencia que declara el editor del contenido.** `openstax.org`, `openscied.org` y `support.thenational.academy` están
   **bloqueados por el proxy**. Es la mitad que falta de la contradicción del trend 22, y por eso **la contradicción se
   registra sin resolver**. Ver el **gap 17**.
2. **Las cifras de DIKSHA** (180 M+ alumnos, 290.000+ contenidos, 36 idiomas, 4.950 M+ sesiones) vienen de EkStep y DPI
   Global, fuentes secundarias. Lo verificado es el repo.
3. **La licencia de Oak National Academy** (OGL v3.0 con uso comercial permitido) viene de prensa educativa británica, no del
   documento de licencia. Lo mismo la posible **restricción geográfica al Reino Unido**.
4. **Las cifras de mercado** de este pase (41,7% del crecimiento global en NA, USD 169 M, programa de OpenAI con 8 socios
   nacionales, £200 M+ del Reino Unido, 38%/94% de EMEA) salen de resultados de búsqueda, no de los informes originales.
5. `curl -sI` contra `github.com` **sigue devolviendo 403**, y `api.github.com` también **403** — probado otra vez en este
   pase, igual que en los pases 5 a 9. No hubo forma de confirmar fechas de último commit; se registran **conteos de commits
   y de forks**, que sí aparecen en la página.

**La lección de método que deja la contradicción de licencia, y extiende la del pase 9.** El pase 9 dejó escrito que
*«descripción, banner, README y archivo `LICENSE` son cuatro fuentes distintas con cuatro grados de autoridad distintos»*.
Este pase lo confirma con un caso donde la diferencia **cambia la viabilidad comercial del proyecto**: el README dice CC BY
4.0 y el `LICENSE` dice CC BY-NC-SA, sobre el mismo contenido. **La regla se endurece: para contenido, el README no es
fuente.** Y en este caso ni el `LICENSE` del repo alcanza, porque la licencia real está declarada **por ítem** dentro de cada
JSON — que es lo que hace del manifiesto por ítem un entregable y no una formalidad (**P22**).

**Una tentación que se evitó, y vale registrarla.** Con tres bundles de OpenStax diciendo NC-SA, lo cómodo era escribir
«OpenStax es NonCommercial y la industria lo viene citando mal». Eso es **una interpretación**: tres títulos no son el
catálogo, y el catálogo no se pudo abrir. Lo que se afirma es lo que se leyó —**tres de tres bundles revisados dicen
NC-SA**— y lo que falta se declara como gap.

**Gap regional declarado, también de método.** La búsqueda regional genérica de APAC devolvió **AI empresarial, no
educativa** (gobernanza de directorios, soberanía de infraestructura). **APAC no tiene cifra de mercado educativo propia en
esta ventana.** Lo que sí tiene —India con mandato nacional, Singapur con integración controlada en el Student Learning
Space, Japón en espera evaluativa, China sumándose a la alfabetización obligatoria— apareció buscando **por país**. La regla
del pase 6 aplicada a la geografía: *si la región no devuelve nada, el nombre que falta puede ser el de un país.*

## Nota de método del pase 9 (2026-10-01) — nueve pasadas buscando el principio del recorrido, y la capa que faltaba era el final

**Lo que este pase hizo distinto.** Las ocho pasadas anteriores buscaron por **capa técnica** (agente, modelado,
evaluación, telemetría, datos), por **categoría de producto** (tutor, plataforma, benchmark) y, en el pase 8, por
**población de alumnos**. Ninguna buscó por **el final del recorrido**: qué pasa cuando el aprendizaje termina y hay que
acreditarlo ante un tercero. Esa capa existe desde hace más de una década, tiene estándares con certificación de
conformidad, y no estaba en la KB porque **no se llama «agente» ni «tutor»** — se llama Open Badges 3.0, W3C Verifiable
Credentials, QTI, OneRoster y Caliper.

Es la **cuarta** aplicación de la regla que dejó escrita el pase 6: *cuando un gap sobrevive varias pasadas, revisar si la
pieza que falta tiene un nombre que uno no está usando.* La regla sigue siendo la más productiva de esta KB.

**Verificado de primera mano** (WebFetch contra la página del repo en github.com, y en dos casos contra el archivo):
las ocho piezas vivas de la capa (`learner-credential-wallet`, `verifier-plus`, `issuer-coordinator`,
`qti3-item-player`, `esco-skill-extractor`, `LongsightGroup/oneroster`, `lti-1-3-php-library`,
`openbadges-specification`), las cuatro copyleft/archivadas (`tao-core`, `openbadgeslib`, `caliper-php-public`, los dos
de la Comisión Europea), el **archivo `LICENSE`** de `qti3-item-player` (`Copyright (c) 2022-2024 Amp-up.io, LLC`), el
**banner y la descripción** del fork de la Universidad de Michigan, y las **tres URL que devuelven 404**
(`concentricsky/badgr-server`, `1EdTech/caliper-php`, `IMSGlobal/caliper-python`), más la búsqueda de repositorios de la
organización `concentricsky` por el término `badgr`, que devuelve *«No repositories matched your search»*.

**Lo que NO está verificado, y está marcado en rojo donde aparece:**

1. **Todo el trend 21** (IgniteAI, niveles de Canvas, fechas de fin del acceso gratuito). Los tres sitios con el detalle
   —`constellationr.com`, `nasdaq.com`, `aijourn.com`— están **bloqueados por el proxy**. Es el dato más accionable del
   pase y el peor verificado.
2. **El estado actual del stack europeo de credenciales**: `code.europa.eu` está bloqueado (gap 14).
3. **`moodle.org`** está bloqueado, así que el plugin `enrol_oneroster` de Moodle se menciona sólo como contexto de que
   la integración OneRoster existe en el LMS, sin verificar licencia ni versión.
4. `curl -sI` contra `github.com` **sigue devolviendo 403** y `api.github.com` también **403**, igual que en los pases
   5 a 8. No hubo forma de confirmar fechas de último commit; se registran los **conteos de commits**, que sí aparecen
   en la página.

**La honestidad que exige un 404.** Un repo que devuelve 404 en GitHub puede estar borrado, renombrado o puesto en
privado, y desde afuera son indistinguibles. Este pase afirma únicamente que **las URL no resuelven** — y donde hay más,
lo cita: en `caliper-php` el mantenedor de un fork **nombra la causa**, y en `badgr-server` hay una **segunda señal
independiente**. La tentación era escribir «1EdTech y Instructure retiraron su código open source»; eso es una
interpretación, y sólo una de las dos mitades tiene a alguien que la respalde por escrito.

**Una corrección de proceso que vale registrar.** La primera lectura de la página del fork de Michigan devolvió la
afirmación sobre 1EdTech, pero una segunda lectura **dirigida al `README.md`** no la encontró. En vez de escribirla como
verificada o descartarla, se hizo una tercera consulta dirigida a la **descripción «About» y al banner** del repo, que es
donde efectivamente está, y recién entonces se citó textual. **El nivel de la página en que vive una afirmación importa:**
descripción, banner, README y archivo `LICENSE` son cuatro fuentes distintas con cuatro grados de autoridad distintos.


## Nota de método del pase 8 (2026-10-01) — una población entera que siete pasadas no buscaron, y una sigla que colisiona

**Lo que se hizo distinto.** Los pases 1–7 buscaron por **capa técnica** (agente, modelado, evaluación, seguridad, telemetría, datos) y por **palabra de mercado** (la lección del pase 7: `tutor`, no `agent`). Este pase buscó por **población de alumnos**, y apareció un segmento completo — accesibilidad y educación especial — que **ninguna de las dos estrategias anteriores podía encontrar**, porque sus repos no se describen como «tutor» ni como «agente educativo» y la pieza con más tracción (`accessibility-agents`, MIT, 419 ★) **ni siquiera es educativa**.

**La lección de método, que es la tercera de esta serie:** pase 5 — buscar la pieza técnica, no la categoría; pase 7 — buscar la palabra del mercado, no la del paper; **pase 8 — buscar por quién es el alumno, no por qué hace el software.** Las tres veces el hueco no estaba en el mercado: estaba en la consulta.

**La colisión de siglas, anotada para que no se repita.** El topic `aac` de GitHub tiene 600+ repos y casi todos son de **Advanced Audio Coding** — codecs, demuxers, servidores de streaming. *Augmentative and Alternative Communication* queda enterrado bajo el ranking por estrellas. Los topics que sí sirven son `assistive-technology`, `special-education` e `inclusive-education`.

**Qué está verificado de primera mano en este pase.** Los **doce repos** de la capa nueva se abrieron con WebFetch contra su página de GitHub: licencia, stars, commits, lenguaje y descripción leídos ahí. `uisight` (128 ★) y `a11y-agents-kit` (34 ★) entraron por listado de búsqueda y se abrieron después para cerrar la licencia: **las dos son MIT**, así que **las tres piezas de P17 son permisivas** y no queda ninguna licencia abierta en la capa de conformidad.

**Qué no está verificado, y es la parte que más pesa comercialmente.** La **API de GitHub sigue bloqueada** en esta sesión (`api.github.com` responde que el repo no está habilitado para la sesión; `curl -sI` contra github.com devuelve 403), así que no hubo forma de confirmar fechas de último commit — se registran los conteos de commits, que sí aparecen en la página. Y **todo lo regulatorio de este pase viene de resultados de búsqueda**: la fecha de entrada en vigor del **EAA (2025-06-28)**, el nivel **WCAG 2.1 AA**, y las prohibiciones de IEP de **Delaware** y **Nueva York**. Son las tres afirmaciones sobre las que se apoyan `P17`, `P18` y el `gap 12`, así que **hay que abrir el texto normativo antes de usarlas con un cliente.**

**Una corrección de licencia detectada leyendo, no buscando.** `Teacher-Hub` declara *«MIT License — free for educational and non-commercial use»*. Las dos mitades se contradicen. Es la segunda declaración de licencia internamente inconsistente que encuentra esta KB (la primera fue OpenTutorAI-CE). **Leer la frase completa de licencia, no sólo el nombre del badge.**

## Nota de método del pase 7 (2026-10-01) — la consulta equivocada costó seis pasadas, y la licencia del dataset no se había mirado nunca

**Dos errores de método propios, los dos corregidos en este pase, y los dos vale dejarlos escritos porque se repiten.**

**1. Se buscó la palabra del gremio, no la del mercado.** Las seis pasadas anteriores buscaron `agent`, `tutoring system`, `benchmark` y `MCP`. Nunca `tutor`. Buscando por descripción con esa palabra aparecen tres repos que suman **4.3k estrellas** y que la KB no tenía: `llamatutor` (2.1k), `ChatTutor` (1.3k) y `tutor-gpt` (931). Ninguno es nuevo; eran invisibles a la consulta. **Regla:** para cada capa, buscar también con el término que usaría quien compra, no sólo el que usa quien construye.

**2. Se verificó la licencia del código y nunca la de los datos.** Los pases 4–6 afirmaron que el modelado del alumno es "integración de una librería MIT". Cierto sobre `pyKT` y `pyBKT`, e insuficiente: los datasets con que se entrenan son **CC BY-NC** salvo uno. Ver el **gap 11**. **Regla:** para toda pieza que se entrene, verificar la licencia del dataset junto con la del repo.

**Límite técnico de la búsqueda de GitHub que conviene registrar:** `in:name` **no respeta límites de palabra** — `tutor in:name` devuelve 276 resultados dominados por `tutorial`, y un `OR` entre términos degrada la consulta entera (`vocational OR berufsschule OR apprenticeship AI tutor` → 24.481 resultados, casi todos irrelevantes). Lo que funcionó fue buscar por **descripción**.

**Qué está verificado de primera mano en este pase (WebFetch contra la página del repo):** `DeepTutor` (40.582 ★, Apache-2.0, push 2026-09-27), `OpenMAIC` (39.7k ★, MIT, 652 commits, v1.1.2 del 2026-09-28), `tutor-gpt` (GPL-3.0, 931 ★, 356 commits), `ChatTutor` (AGPL-3.0, 1.3k ★), `Honcho` (AGPL-3.0, 7.4k ★, 760 commits), `ABench` (Apache-2.0, 30 ★), `XES3G5M` (MIT, 61 ★), `EdNet` (CC BY-NC 4.0, 385 ★), los perfiles de organización de `plastic-labs` (declara **EE. UU.**) y de `inclusionAI` (declara **Ant Group**), y la **ausencia** de licencia en `llamatutor` (`/blob/main/LICENSE` → **404**).

**Qué NO está verificado y por qué.** El proxy de egreso sigue bloqueando `arxiv.org`, `huggingface.co` y los dominios de OUP — **se reintentaron los tres en este pase**. Quedan con cifras de resultados de búsqueda, no de fuente primaria: **`FoundationalASSIST`** (arXiv 2602.00070), **`EduZone`** (2608.02024), **`AIriskEval-edu`** (2607.01934), el paper de **`ProHist-Bench`** (2604.24690) y **`L2-Bench`**. También está bloqueado `aivet-training.eu`, por lo que AIVET queda como pista, no como hallazgo.

**Sobre `L2-Bench`, que arrastra la marca 🔴 desde el pase 6:** este pase obtuvo **más detalle** de resultados de búsqueda — taxonomía de 12 competencias y 31 subcompetencias validada por **200+ practicantes expertos** con puntajes de autenticidad de tarea **4,42/5,00** y adecuación de criterios **4,18/5,00**, y resultados por modelo (el mejor frontier model en **85,5%**, cayendo a **69,9–73,4%** en tareas difíciles). **Dos pasadas independientes que coinciden en las cifras es evidencia circunstancial, no verificación.** La marca 🔴 **se mantiene**: el artefacto sigue sin abrirse. No usar esas cifras en un entregable sin leer la fuente.

**Nota sobre la API de GitHub:** `get_file_contents` vía MCP está restringido a los repos de esta sesión, así que no sirve para leer el LICENSE de un tercero (se intentó con `Nutlope/llamatutor` y fue denegado). La verificación de licencias se hizo con WebFetch. `curl -sI` contra github.com sigue devolviendo **403** a través del proxy, como en los pases 4–6.

## Nota de método del pase 6 (2026-10-01) — qué se verificó, qué no, y una capa que faltaba en el mapa

**Verificado de primera mano** (leyendo el repo en GitHub: licencia, stars, commits, y en varios casos el texto del README): los cinco artefactos de la capa LRS/xAPI, ERPNext, y la recuenta de `EduBench`. Los conteos de repos que sostienen los gaps 2 y 10 (20 repos en español, ninguno >1 ★; 24 repos de FP, techo 2 ★) salen de consultas directas a la API de búsqueda de GitHub, no de listicles.

**No verificado, y marcado en rojo donde aparece:** **L2-Bench**. El proxy de egreso de esta sesión bloquea `arxiv.org`, `huggingface.co` y `oup.com`, que son exactamente los tres lugares donde vive. Se registró igual, con la advertencia pegada a cada mención, porque cerraba un sub-gap declarado hacía dos pasadas; pero **no debe entrar en un entregable sin abrirlo antes**. El pase 5 ya había dejado escrito que "el proxy de egreso decide qué se puede afirmar"; este pase lo confirma y agrega un matiz: **también decide qué se puede cerrar**. Un gap que se cierra con una fuente no verificable no está cerrado, está anotado.

**Lo que este pase aprendió sobre buscar, y es la parte reutilizable.** Los pases 3 y 5 concluyeron que un gap terco hay que re-buscarlo con la consulta invertida (por licencia y stack, no por categoría). El pase 6 encontró el caso complementario: **la consulta estaba bien y el mapa estaba mal.** La capa de Learning Record Store existe desde hace más de una década, es un estándar IEEE, tiene cuatro implementaciones maduras y una de ellas con 583 ★ — y no apareció en cinco pasadas porque la KB buscaba "agente", "tutor", "benchmark" y "plataforma", y esto no se llama así.

La regla que queda: **cuando un gap sobrevive varias pasadas, revisar si la pieza que falta tiene un nombre que uno no está usando.** Buscar mejor no alcanza si el mapa no tiene el casillero.

## Nota de método del pase 5 (2026-09-30) — el proxy de egreso decide qué se puede afirmar

Esto no es color: cambia qué de este archivo se puede citar en material de cliente.

**Lo que funcionó.** WebFetch contra `github.com`. Todo lo que este pase afirma sobre repos —licencia, stars, lenguaje, commits— se leyó de la página del repo o del archivo LICENSE.

**Lo que no funcionó.** `curl -sI` contra github.com devuelve **403** a través del proxy (confirma lo que ya anotó el pase 4: **no sirve para verificar URLs en este entorno**). Y están **bloqueados por el proxy de egreso**: `arxiv.org`, `openreview.net`, `aclanthology.org`, `huggingface.co`, `ojs.aaai.org`, `mcml.ai`, `unu.edu`, `coe.int`, `digitaleducationcouncil.com`, `mcpservers.org`.

**La consecuencia, dicha sin adornos.** Todo lo que en este pase viene de **papers, datasets de HuggingFace, cifras de mercado y documentos de organismos** está tomado de **resúmenes de búsqueda y no pudo verificarse contra la fuente primaria**. Eso incluye: los conteos de ítems de SafeTutors (5.955) y de EduBench (4.000+), los subtipos de EduFrameTrap, **el hallazgo de anti-correlación de ELBench**, el 78,74% de OmniEdu en MathTutorBench, los venues (ACL 2026, EMNLP 2026, AAAI), **todas las cifras de UNESCO IESALC** y las fechas del Consejo de Europa.

Se registran porque son útiles, internamente consistentes y provienen de fuentes independientes que coinciden. **No citarlos en un entregable sin abrir el paper o el informe.** Los tres hallazgos de ELBench y de EduGuardBench que este archivo usa como argumento de arquitectura (trend 12) son justamente los que más conviene confirmar antes de ponerlos en una slide.

**Lo que sí se verificó leyendo el archivo y no el badge**, porque en los dos casos el badge sugería otra cosa: `llmgrader` → **PySilicon Research License** (no MIT), y `awesome-ai-llm4education` → **`/blob/main/LICENSE` devuelve 404**, no tiene licencia. Leer el LICENSE sigue siendo la única verificación válida.

**Una corrección de premisa propia**, que se registra para que no se repita: este pase buscó una Working Conference del Consejo de Europa de **octubre de 2026** y **no existe** — la última realizada es la 3ª, de **octubre de 2025**. La búsqueda corrigió la suposición; si no se hubiera verificado, habría entrado a la KB un evento inventado.

## Nota de método del pase 4 (2026-09-30) — cómo se verificó y qué no se pudo

**Verificado de primera mano:** los 7 repos nuevos y los 6 ya registrados que se re-chequearon, todos vía **WebFetch contra la página del repo** — stars, licencia, lenguaje y, donde estaba, fecha de último commit.

**Tres limitaciones del entorno que conviene dejar escritas, porque cambian el procedimiento:**

1. **`curl -sI` no verifica nada acá.** El procedimiento estándar de esta KB es chequear cada URL con `curl -sI` antes de escribirla. En esta corrida devuelve **403 para todas las URLs de github.com**, incluidos repos que sabemos vivos. Un 403 uniforme no distingue un repo real de uno inexistente. Se reemplazó por WebFetch, y **se comprobó que ese canal sí discrimina**: una URL deliberadamente inexistente devolvió `HTTP 404 Not Found` mientras las 13 reales devolvieron su página.
2. **`api.github.com` está fuera de alcance** para esta sesión (responde que el repo no está habilitado). Stars y licencia se leen de la página renderizada, no de la API — así que son valores mostrados, redondeados por GitHub en el caso de los repos grandes (40.6k, 39.7k).
3. **`arxiv.org` está bloqueado por el proxy de salida.** Consecuencia concreta: **la afiliación institucional de MathTutorBench no se pudo verificar de primera mano.** Se le asigna EMEA/Suiza por el handle de la organización (`eth-lre`) y por el venue, **no por el paper**. Es la atribución regional menos firme de este pase y hay que tratarla como tal. Lo mismo con `EduFair-Bench` (arXiv 2609.12949): se conoce por la búsqueda, no se le encontró repo, y no se lo registra como hallazgo.

**Atribuciones con confianza declarada, no binaria.** Dos regiones se cerraron en este pase con niveles de evidencia distintos, y se registran distinto: **OpenTutorAI-CE → Marruecos** está *declarado* en el perfil de la organización; **Claw-ED → Nueva York** está *inferido de artefactos* (repos hermanos sobre NYS Regents y Great Neck Public Schools), no declarado. Tres agentes —**Bloom, OpenTutor y tutor-mcp**— se buscaron explícitamente y **no declaran ubicación en ningún lado**: quedan como gap, no como silencio.

## Nota de método — qué está verificado de primera mano y qué no (pase 3, 2026-09-30)

Esta KB ya se quemó una vez con datos que el pipeline reportó sin medir (ver la tabla de corrección en `agents/top.md`). Así que conviene ser explícito sobre el nivel de evidencia de cada cosa, porque **en esta corrida no fue uniforme**.

**Verificado de primera mano (fuerte).** Todo lo que es repo: licencia, stars, forks, commits, fecha del último commit, releases. Se leyó la página del repo vía WebFetch, y en el caso de GegoK12 además el archivo `LICENSE` crudo (`SPDX-License-Identifier: MIT`). Aplica a Claw-ED, AI-Teaching-Agent, GegoK12, `Plugin-Hello-Teacher`, OpenMAIC y DeepTutor.

**Corroborado pero no leído en la fuente (medio).** Todas las afirmaciones **regulatorias y de tamaño de mercado** del pase 3: la AI Basic Act coreana, la ley vietnamita, el deadline de Ohio del 2026-07-01, Virginia SB 394 / HB 1186 y su pilot de USD 2M, los 35+ estados con guía oficial, y las cifras de Europa y MENA. El proxy de egreso de esta sesión **bloquea el acceso directo** a esos dominios (`lw.com`, `multistate.us`, `casrai.org`, `kjk.com`, `edweek.org`, `education.ohio.gov`, `gegok12.com` y otros), y `curl` no sirve como verificador acá — devuelve 000 o 403 incluso para páginas que existen. Cada afirmación de este grupo se sostiene en **múltiples resultados de búsqueda independientes que concuerdan** (el deadline de Ohio aparece en 6+ medios distintos; la fecha coreana del 2026-01-22 y la inclusión de educación como *high-impact*, en 5+), no en la lectura de la página.

**Qué hacer con eso.** Son datos suficientemente sólidos para orientar prioridades y construir propuestas, y **no** suficientes para citarse textualmente en un entregable de cliente sin abrir la fuente primaria. Antes de usar cualquier cifra regulatoria de esta sección en material de cliente: **leer el estatuto o la guía oficial**. Las URLs quedan listadas arriba para eso, pero están sin verificar a nivel HTTP en esta corrida.

**Lo que explícitamente no se pudo verificar y queda marcado como tal:** el conteo de MultiState de "cuatro estados con leyes de 2026 que exigen guía estatal más política distrital obligatoria (Maryland, Idaho, Oklahoma, Virginia)". Ohio y Virginia se corroboraron por separado; el conteo de cuatro queda atribuido a MultiState y sin verificar uno por uno.

---
*Repos (stars, licencias, releases) verificados uno por uno vía WebFetch el 2026-09-30, no por el pipeline. Afirmaciones regulatorias y de mercado del pase 3: corroboradas por múltiples fuentes concordantes, con las fuentes primarias inaccesibles desde esta sesión — ver la nota de método arriba.*
