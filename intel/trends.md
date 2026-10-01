---
industry: education
region: Global
updated: 2026-10-01
---

# 📡 Tendencias — education

> Ventana de investigación: septiembre 2026. Verificado 2026-09-30; el pase 11, el 2026-10-01.
> **Pase 26:** se ejecuta la consigna del pase 25 (**cambiar el eje al conector**) y rinde en su primer uso por segunda
> vez consecutiva: **el gap 40 se cierra ejecutando** —el cartucho MCP de CaSS genera **6 tools y 3 resource templates**
> medidos con el generador del propio proyecto, y dos de ellos (`record_evidence`, `get_learner_profile`) son
> **exactamente los dos pasos que P48 tenía inferidos** (tendencia **66**)—; el **lado *platform* de LTI se cierra por
> medición y la respuesta es que no existe permisivo y productivo**, sobre seis candidatos (tendencia **67**, gap **42**);
> y entran **tres verticales nuevas**: biblioteca/ILS **con opción permisiva y grande** (FOLIO, Apache-2.0), y
> **admisiones** y ***student success*** 🔴 **sin ninguna** — la segunda es de **2013–2014** y es la que el regulador
> aprieta más (tendencia **68**, gaps **45**, **46**, **47**).
> **Pase 25:** se ejecuta **entera** la consigna del pase 24 (cuatro artefactos y tres estándares) y el eje rinde por tercera vez:
> **Caliper dejó de ser open source el 2023-06-17** —repos movidos a privado por 1EdTech— así que de los dos estándares de
> analítica de aprendizaje **sólo xAPI se puede construir** (tendencia **63**); la capa de **proctoring** es la única de esta
> KB **sin ninguna opción permisiva y productiva**, y es justo la que el **Annex III** nombra de alto riesgo (tendencia **64**,
> patrón **P49**, gap **39**); y aparece la **primera pieza de estándar educativo con puerta MCP** —CaSS, Apache-2.0— que
> además hace las **aserciones** de competencia que las cuatro piezas CASE de esta KB no hacían (tendencia **65**, patrón **P48**).
> ⚠️ **Y dos no-hallazgos del pase 24 eran falsos negativos:** `LongsightGroup/qti3` existe (y trae el *item bank* que la
> consigna pedía) y `yetanalytics/xapipe` es el repo de *LRSPipe*. Ver la nota de método del pase 25.
> **Pase 24:** se ejecuta la acción del pase 23 **midiendo en vez de leyendo**, y el resultado **corrige** al pase 23:
> el desglose por tabla de un borrado **ya viaja por el cable** y se descarta, así que el **gap 36** no es refactor de SQL
> sino de la capa que recoge el resultado — pero el conteo único disponible es el del **primer** `DELETE` y vale **`0`**
> para el alumno típico (tendencia **61**). Y aparece el **gap 38**, el primero cuyo síntoma es la ausencia del borrado y
> no de su prueba: en MariaDB/MySQL la supresión **falla entera** (error 1064) si una variable de entorno no relacionada
> apaga `allowMultiQueries` (tendencia **62**, patrón **P47**).
> **Pase 23:** se ejecuta la acción que el pase 22 dejó escrita y **el gap 36 queda dimensionado**: los conteos de borrado existen en los tres backends de `lrsql`, pero **la evidencia no es portable entre motores de base de datos** — y eso contradice la razón por la que esta KB lo recomienda por default (tendencia **60**, patrón **P45**).
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

> 🔴 **CORREGIDO EN EL PASE 14 DEL 2026-10-01 — Taiwán no cuenta, y este párrafo lo contaba.** La afirmación de arriba
> lista **tres** regímenes «en vigor» y recomienda construir el expediente «en un despliegue coreano **o taiwanés**».
> **Para Taiwán es incorrecto, y la fecha 2026-01-14 —que es correcta— lo hace parecer exigible.** Verificado: la
> *AI Basic Act* taiwanesa fue aprobada por el Yuan Legislativo el **2025-12-23** y promulgada el **2026-01-14**, pero
> **(a)** son **20 artículos de ley marco sin ninguna disposición sancionatoria**; **(b)** el artículo 5 exige etiquetar
> las aplicaciones de alto riesgo pero **ningún artículo define «alto riesgo»**: la tarea está delegada al **MODA** por
> el artículo 16 y **el marco de clasificación de riesgo todavía no existe** (MODA apuntaba a Q1 2026); **(c)** lo único
> específico de educación es la consideración del interés superior de niños y adolescentes.
>
> **Consecuencia operativa, y es la inversa de lo que el párrafo recomienda:** un despliegue taiwanés **no** produce hoy
> expediente de conformidad reutilizable, porque **no hay contra qué conformar**. **Corea del Sur y Vietnam sí** —el
> coreano con alcance extraterritorial, evaluación de riesgo, supervisión humana y documentación desde enero de 2026;
> el vietnamita con **evaluación automatizada y monitoreo de comportamiento tipificados como alto riesgo**, en vigor
> desde marzo de 2026—. **Los regímenes exigibles de APAC son dos, no tres. Taiwán se sigue, no se vende.**

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

## 33. La capa curricular tenía un estándar de interoperabilidad desde antes que esta KB existiera, y catorce pasadas lo saltearon (agregado 2026-10-01, pase 14)

El gap 19 trataba los esquemas curriculares nacionales como artefactos sueltos a coleccionar país por país. Esa era
la mitad del problema. La otra mitad: **1EdTech publica CASE® (*Competencies and Academic Standards Exchange*), el
estándar que define cómo se publica, versiona e intercambia un marco de competencias o de estándares académicos, y
tiene implementaciones open source certificadas.**

El pase 9 abrió la familia 1EdTech por las **credenciales** (Open Badges, CLR) y no miró los **estándares**, que son
la misma familia de especificaciones. Catorce pasadas después, la capa aparece completa:

| Repo | Licencia | ★ | Conformidad |
|---|---|---|---|
| `opensalt/opensalt` | MIT | **45** | ⚠️ estable 3.2.0 (sept 2023) → **CASE v1.0** |
| `1EdTech/OpenCASE` | Apache-2.0 | **9** | ✅ **certificado CASE Service v1.0 y CASE v1.1 — 2026-02-17** |
| `infosign/compeito` | Apache-2.0 | **3** | ✅ *Provider* CASE v1.1 |
| `conform-ed/conform-ed` | MIT | **2** | ✅ **once estándares a la vez** |

**Y es la tercera vez que esta KB mide el mismo fenómeno: la pieza con más estrellas es la que está más atrás del
estándar.** OpenSALT tiene 45 ★ y su último estable es de septiembre de 2023 contra CASE v1.0; OpenCASE tiene 9 ★ y
está certificado contra v1.1 con fecha de febrero de 2026. El pase 10 lo midió con Sunbird (41 ★ sirviendo 180
millones de alumnos) y el pase 11 con Apereo. **Deja de ser anécdota y pasa a ser regla de método: en capas de
estándar el criterio de selección es la fecha de certificación, no la estrella.**

**La consecuencia de arquitectura, que es lo que importa comercialmente:** los cuatro esquemas curriculares
nacionales verificados se publican cada uno en su formato —RDF el inglés y el coreano, JSON propio el brasileño y el
estadounidense—. Un cliente no quiere cuatro parsers: quiere un endpoint. **CASE es ese endpoint, y hay dos
servidores Apache-2.0 que lo sirven.**

---

## 34. La capa donde el alumno habla no existía en esta KB, y es la que decide si un tutor sirve en primaria (agregado 2026-10-01, pase 14)

Trece pasadas buscaron por el rol del software, por la capa y por el alumno. **Ninguna buscó por el canal**, y todo
lo que esta KB tenía asumía un alumno que **escribe**: el notebook del pase 13, el SRS del pase 12, el LRS del pase 6.

**En alfabetización inicial, la medición que usan los sistemas educativos no es un cuestionario: es que el chico lea
en voz alta y se le midan palabras por minuto y exactitud.** Es la métrica de las evaluaciones de lectura en las
cuatro regiones, y hasta este pase esta KB —31 agentes, catorce capas— no tenía una sola pieza para capturarla.

La capa, medida:

- **`Halleck45/OpenPronounce` (MIT, 85 ★)** es la única pieza permisiva, educativa y utilizable: evaluación fonema a
  fonema con Wav2Vec2, PER/WER, confianza por palabra, DTW y prosodia (F0 y energía), **corriendo local sin API key**.
  Se posiciona explícitamente como la alternativa autoalojada a Azure Pronunciation Assessment.
- **`kaldi-asr/kaldi` (Apache-2.0, 15.5k ★)** es lo maduro, y es ASR genérico: no sabe nada de pedagogía.
- **`jimbozhang/speechocean762` (198 ★)** es el corpus de referencia —5.000 oraciones, **mitad niños**— y **no tiene
  archivo de licencia**.
- El resto de la capa son *papers*.

**Es el patrón base de esta KB otra vez, con un signo que mejora el caso:** lo maduro es genérico y lo educativo es
chico, igual que en accesibilidad (pase 8) y en *skills* (pase 12) — pero acá **la pieza educativa chica es MIT y corre
local**, así que el obstáculo no es la licencia ni la soberanía del dato. Es que nadie la empaquetó para un sistema
educativo.

**Y hay un hueco de mercado que conviene nombrar con número: ~600 millones de hispanohablantes y lusohablantes sin
pieza permisiva de evaluación de fluidez lectora.** El corpus de referencia es inglés con L1 mandarín; lo único de
LATAM (`carrera-lectora`, Chile) no tiene licencia. **Los puntajes publicados sobre `speechocean762` no son
transferibles a un despliegue en español o portugués sin recalibración**, y eso es alcance y presupuesto propios, no
un detalle de implementación.

---

## 35. Lo curricular no es copyleft, y esta KB lo venía asumiendo mal (agregado 2026-10-01, pase 14)

Cuatro pases seguidos (8, 9, 10 y 11) encontraron la misma forma: **lo maduro es copyleft, lo permisivo no tiene
tracción.** Accesibilidad (OptiKey GPL-3.0, Cboard GPL-3.0), interoperabilidad, contenido abierto (donde además
apareció el agravante NonCommercial), analítica institucional. El gap 19 leyó la capa curricular con ese mismo filtro
y sacó una conclusión regional: el coreano es MIT y el español CC BY-SA, *ergo* «el artefacto de APAC es mejor
técnicamente y más barato legalmente», espejo del gap 4.

**Con cuatro artefactos más verificados, el patrón se cae, y en el buen sentido:**

| País | Artefacto | Licencia de datos | Uso comercial |
|---|---|---|---|
| Inglaterra | `oak-curriculum-ontology` | **OGL-3.0** | ✅ con atribución |
| Brasil | `bncc-dados` | **CC BY 4.0** | ✅ con atribución |
| EE. UU. | `commonstandardsproject/api` | **Apache-2.0** | ✅ |
| Corea del Sur | `korean-elementary-learning-map` | **MIT** | ✅ |
| España | `OpenDidactia` | ⚠️ CC BY-SA 4.0 | ⚠️ *share-alike* |

**Hay permisivo apto para uso comercial en las cuatro regiones, y el único *share-alike* es el español.** La
conclusión útil no es «APAC gana»: es que **la capa curricular es, por licencia, la más limpia de toda esta KB**, y
que el filtro mental de los pases 8-11 —«si es educativo y maduro, va a ser copyleft»— **produce falsos negativos
caros** en esta capa.

**La regla nueva que este pase agrega, y vale para toda la KB:** en artefactos de datos, **la licencia del código y
la del dato son dos licencias distintas y casi nunca coinciden.** `bncc-dados` es MIT en código y CC BY 4.0 en datos;
`oak-curriculum-ontology` es MIT en código y OGL-3.0 en ontología. Leer sólo el badge del repo —que muestra la del
código— hace creer que el dato es MIT. **No lo es, y la atribución es una obligación de entregable.**

---

## 36. La pregunta «¿lo escribió una AI?» no tiene respuesta, y la industria educativa está terminando de aceptarlo (agregado 2026-10-01, pase 15)

No es una opinión sobre la tecnología: es el resultado convergente de los propios autores de los detectores, de
sus benchmarks y del comportamiento de las instituciones.

**El número que lo decide, y es el que importa para una empresa global:** siete detectores evaluados sobre
ensayos TOEFL dan **61,3 % de falsos positivos sobre escritura de no nativos de inglés**, contra **~2,9 %** sobre
universitarios estadounidenses nativos. La explicación propuesta —**baja perplejidad** del texto de no nativos por
menor variabilidad léxica— implica que **es estructural**: un detector mejor entrenado sigue midiendo lo mismo.

**Y el resto de los modos de falla están medidos:**

| Medición | Valor | Fuente |
|---|---|---|
| FPR sobre 1.180 abstracts académicos **anteriores a 2018** | **5,85 %**, más 20 % en «incierto» | `Lendarixon/awesome-ai-detection` |
| Texto humano mal marcado por un ensamble de 23 motores | 1 de 66 | README de `sloptotal` |
| Longitud mínima para que el score signifique algo | **~80 palabras**; estabiliza en ~200 | README de `sloptotal` |
| Efecto de la paráfrasis sobre la exactitud | **caídas grandes** | benchmark RAID (ACL 2024) |
| Transferencia a modelos más nuevos | falla | `awesome-ai-detection` |

**`Binoculars` (ICML 2024) lo escribe en su propio README:** *«more proficient in detecting English language text
compared to other languages»*, *«none are perfect and can have multiple failure modes»*, **«for academic purposes
only»**, con supervisión humana requerida.

**El comportamiento institucional ya se movió.** Vanderbilt hizo la cuenta —**1 % de FPR sobre 75.000 trabajos
son ~750 acusaciones injustas por año**— y desactivó el detector de AI de Turnitin. **Más de 50 universidades**
de EE. UU., Reino Unido, Canadá, Australia y Sudáfrica (Johns Hopkins, Yale, Waterloo, Curtin, Australian
Catholic University) lo desactivaron, restringieron o lo abandonaron; **al menos 12 instituciones grandes a marzo
de 2026**. Y el criterio que quedó escrito en las políticas de 2026 es que **un score de detección no es prueba
autónoma de mala conducta**: hace falta un segundo detector, revisión humana y derecho de apelación.

**Qué significa para una propuesta.** No significa que la categoría desaparezca: significa que **cambia de uso**.
Un detector sirve para **priorizar una conversación docente**, nunca para disparar una sanción. Vender detección
como mecanismo disciplinario a un cliente cuyos alumnos escriben inglés como L2 —LATAM, EMEA no anglófona, buena
parte de APAC— es venderle el **61,3 %**. Ver el **gap 25**, la capa en `agents/top.md` y el patrón **P33**.

---

## 37. La integridad se está moviendo de la detección a la procedencia, y la procedencia es Apache-2.0, obligatoria en EMEA y no la usa nadie en educación (agregado 2026-10-01, pase 15)

Es la contracara de la tendencia 36 y es donde está el trabajo vendible.

**La pregunta cambia de forma.** *«¿Esto lo escribió una AI?»* es un juicio probabilístico sobre texto ajeno y no
tiene respuesta confiable. *«¿Esto lo escribió **nuestro** tutor?»* es una **verificación**, y la respuesta es
cierta. Una institución que **provee** el agente puede marcar su salida en el origen; la integridad deja de ser
forense. Es exactamente la forma que describe la **tendencia 29** —lo que se conecta al estándar instalado
escala— aplicada a la autoría.

**Las piezas existen, están maduras y son permisivas:**

| Capa | Pieza | Licencia | Señal de madurez |
|---|---|---|---|
| Watermark de texto | **SynthID-Text**, dentro de `huggingface/transformers` | **Apache-2.0** | En producción en Transformers; copyright HuggingFace + **Google DeepMind** |
| Evaluación del watermark | **MarkLLM** | **Apache-2.0** | **1.100 ★**, 23+ algoritmos, 12 herramientas de evaluación, EMNLP 2024 Demo |
| Procedencia del artefacto | **c2pa-rs** / **c2pa-python** | **MIT *y* Apache-2.0** (dual) | **1.907 commits**; spec C2PA 2.4 con *CAWG identity assertion* |

**Y en EMEA dejó de ser opcional.** El **Artículo 50** está en vigor desde el **2026-08-02**, y los sistemas de
AI generativa **ya en el mercado** antes de esa fecha tienen hasta el **2026-12-02** para cumplir el marcado
legible por máquina del **Artículo 50(2)**: el contenido debe estar marcado de forma *«effective, interoperable,
robust and reliable»*. El **Code of Practice** sobre marcado y etiquetado —voluntario, pero la vía más clara para
demostrar cumplimiento— define un esquema **por capas (metadato + watermarking**, con *fingerprinting* y
*logging* de apoyo) y **adopta las *Content Credentials* de C2PA como estándar técnico de facto** del metadato.

🔴 **Dos cosas que hay que decir con honestidad.** Primero: **esta KB venía recomendando esta oferta desde el
pase 4 sin tener una sola pieza registrada** — `compose/patterns.md:106` anota el deadline del 2026-12-02 desde
entonces, y `watermark` aparecía cinco veces en la KB, **todas en prosa comercial, ninguna apuntando a código**.
Queda corregido. Segundo: **ningún proyecto educativo open source usa nada de esto.** No hay plugin de LMS,
herramienta LTI ni servidor MCP que marque o verifique la salida de un tutor. La infraestructura está lista; **el
puente al aula no está construido**, y es trabajo de días. Ver **P33** y el **gap 25**.

⚠️ **El límite honesto:** el marcado sólo cubre el texto que generó el sistema propio. No resuelve el ensayo
escrito con un modelo externo. Convierte un problema irresoluble en uno **parcial pero cierto**, más un régimen
de **declaración** para el resto — que es, justamente, lo que LATAM ya exige por norma (tendencia 38).

---

## 38. LATAM tiene el régimen regulatorio que el open source puede cumplir hoy, y tiene instalada la herramienta que no lo cumple (agregado 2026-10-01, pase 15)

Las cuatro regiones resolvieron la integridad académica de forma distinta, y **la latinoamericana es la única que
el stack permisivo existente satisface completo**. Es la primera vez en quince pasadas que la lectura regional
sale a favor de LATAM por el lado de la **norma** y no por el del talento.

| Región | Régimen dominante | ¿Lo cumple el open source de hoy? |
|---|---|---|
| **North America** | Vacío federal, parches estatales (Colorado, Texas, Idaho SB 1227). **El abandono de la detección nació acá** | Parcial. No hay obligación que cumplir; hay un hueco que llenar |
| **EMEA** | **Obligación legal con fecha**: Art. 50 en vigor 2026-08-02, marcado legible por máquina 2026-12-02 | **Sí** — y es obligatorio. SynthID-Text + C2PA |
| **APAC** | Fragmentado, sin marco común. Japón cauteloso con marco estatal; China centralizado *top-down*; **Australia: 26 de 35 universidades (73 %) ubican la política de AI dentro de la de integridad académica** | Parcial, caso por caso |
| **LATAM** | **Declaración obligatoria** del uso de AI en **México, Colombia y Chile**, con sanción por uso fraudulento y en algunos casos **entrega de los prompts** | 🟢 **Sí, completo.** Un régimen de divulgación se satisface con procedencia, no con forense |

**El punto es la distancia entre la norma y la herramienta.** La regla latinoamericana **no pide detectar: pide
declarar**. Eso se cumple marcando, firmando y registrando — exactamente lo que SynthID-Text y C2PA producen, con
certeza y sin acusar a nadie. **Y lo que está instalado es detección:** UNAM, Tec de Monterrey, UAM, BUAP y UdeG
usan **Turnitin Originality** como herramienta principal — el mismo tipo de producto que 50 universidades
anglófonas desactivaron, aplicado sobre alumnos que escriben **español**, donde está aún menos validado, y en una
región donde el **61,3 %** de la tendencia 36 pega de lleno.

**Y el contexto institucional lo vuelve urgente:** **más del 80 % de las instituciones de educación superior de
México no tiene marco normativo claro** sobre uso ético y académico de la tecnología. O sea: la norma nacional
existe en tres países, la mayoría de las instituciones no la bajó a reglamento, y la herramienta que compraron no
la sirve. Es una ventana de definición, no sólo de venta. Ver **P33** y `intel/market.md` → LATAM.

⚠️ **Pendiente de verificación, y es la pista más valiosa que deja este pase:** hay un dataset en Zenodo
(`zenodo.org/records/22661179`) con las políticas institucionales de integridad académica y lineamientos de AI
generativa de las **15 universidades latinoamericanas mejor rankeadas en THE 2026** (USP, Unicamp, PUC Chile,
UFRJ, UNESP…). **`zenodo.org` está bloqueado por el proxy de egreso: no se pudo verificar licencia ni contenido.**
Si tiene licencia abierta, es el mapa de la norma institucional de la región servido en bandeja.

## 39. La infraestructura de privacidad es la única capa de esta KB donde lo maduro es permisivo, y la educación no la usa (agregado 2026-10-01, pase 16)

Quince pasadas registraron la misma forma una y otra vez: lo que está desplegado es copyleft o propietario, y lo
permisivo no pasa de unas pocas estrellas. En la capa de privacidad del dato **esa forma se invierte**.

| Pieza | Licencia | ★ |
|---|---|---|
| PySyft (OpenMined) | Apache-2.0 | 10.0k |
| Flower | Apache-2.0 | 7.2k |
| Google DP | Apache-2.0 | 3.4k |
| Opacus (PyTorch/Meta) | Apache-2.0 | 2.0k |
| TensorFlow Privacy | Apache-2.0 | 2.0k |
| diffprivlib (IBM) | MIT | 920 |
| synthcity | Apache-2.0 | 687 |
| OpenDP (Harvard) | MIT | 437 |

**Más de 26.000 estrellas, todas Apache-2.0 o MIT, de Harvard, Google, Meta e IBM.** No hay fricción de licencia,
no hay riesgo de procedencia, no hay que construir nada.

**Y la educación no la toca.** Lo específicamente educativo de esta capa es `PrivGen` (MIT, **3 ★**),
`federated-deep-knowledge-tracing` (**10 ★**, sin licencia), `FedGKT` (**1 ★**, sin licencia) y `SynEdu-HEDL`
(**1 ★**, sin licencia). El techo es **10 estrellas** y **tres de los cuatro no son reutilizables** por no
declarar licencia.

**La lectura, y es la tendencia:** el cuello de botella de esta capa no es tecnológico ni de licencia — es de
**integración**. La distancia entre `Flower` y un modelo de knowledge tracing federado la recorrió un repo de 1
estrella usando piezas que cualquiera tiene disponibles. Es la capa de mejor relación esfuerzo/defensa de toda
esta KB, y es la que nadie recorrió.

## 40. El reloj de privacidad de Norteamérica ya venció, y es el primero de esta KB que se vende como exposición y no como preparación (agregado 2026-10-01, pase 16)

Esta KB viene administrando relojes regulatorios futuros: el Artículo 50 del EU AI Act **vence el 2026-12-02**, el
Anexo III **el 2027-12-02**, Vietnam y Corea con sus propias fechas. Todos se venden igual: *falta tanto, hay
ventana de consultoría*.

**La regla COPPA enmendada de la FTC rompe ese patrón porque ya pasó.**

| Hito | Fecha |
|---|---|
| FTC anuncia las enmiendas finalizadas | enero de 2025 |
| Publicación en el *Federal Register* | 2025-04-22 |
| Entrada en vigor | 2025-06-23 |
| 🔴 **Fecha de cumplimiento general** | **2026-04-22** |

Es la primera actualización sustantiva de COPPA en **doce años**, y lo que agregó es exactamente lo que le pega a
esta KB:

- **Identificadores biométricos** —**voiceprints**, faceprints, huellas dactilares y de palma— pasan a ser
  **información personal**. Eso alcanza a toda la **capa de voz** que el pase 14 abrió, y a cualquier función de
  reconocimiento facial.
- **Consentimiento verificable separado** antes de compartir dato de menores con terceros.
- **Prohibida la retención indefinida**: hace falta **política escrita** de retención y borrado en plazo.

Y debajo, el régimen estatal que ya existía: **SOPIPA** (California) prohíbe vender dato de alumnos y la
publicidad dirigida sin vía de consentimiento que lo habilite; **SOPPA** (Illinois) impone requisitos
contractuales, plazos de notificación de brecha y transparencia pública; **Nueva York** prohíbe el reconocimiento
facial en escuelas; y **BIPA** (Illinois) exige consentimiento escrito para biométricos con daños estatutarios de
**1.000 a 5.000 USD por violación**.

**Por qué cambia el argumento comercial:** con un reloj futuro se vende un plan. Con un reloj vencido se vende
**remediación**, el comprador es otro (jurídico y no innovación), el ciclo es más corto y la objeción «esperemos a
ver cómo queda la norma» no existe. Es, de las cuatro regiones, la única donde esta KB puede decir hoy que el
plazo ya se cumplió.

## 41. El dato de aprendizaje empezó a nombrarse como perfilado dañino, y eso toca la capa predictiva que esta KB declaró desabastecida (agregado 2026-10-01, pase 16)

El pase 11 abrió la capa predictiva —*early warning*, riesgo de deserción— y la registró como **la única capa de
esta KB donde la demanda está madura y la oferta open source es cero** (gap 18). El encuadre era de oferta. Lo que
el pase 16 agrega es que **la demanda de esa capa está empezando a tener techo regulatorio en tres regiones a la
vez**, y por el mismo motivo.

- **APAC (India).** Bajo la **DPDP Act 2023**, toda escuela que procese dato digital de alumnos es *Data
  Fiduciary*, y la **Sección 9** aplica por tratarse de menores: consentimiento parental verificable, sin
  seguimiento conductual ni publicidad dirigida, y nada de tratamiento que pueda causar daño. Sanciones de hasta
  **₹200 crore** por infracción con datos de menores. La lectura de los analistas regionales es explícita: una
  analítica que etiqueta a un alumno como *«de bajo potencial»* o que predice problemas de conducta sin
  salvaguardas **puede tratarse como perfilado dañino**.
- **EMEA.** El Anexo III del EU AI Act ya clasificaba la predicción de deserción como alto riesgo; el GDPR le suma
  el **DPIA obligatorio del Artículo 35** antes del despliegue.
- **LATAM (Brasil).** El **Referencial** del MEC (2026-03-12) advierte sobre la necesidad de transparencia
  algorítmica y sobre el riesgo de **sesgo algorítmico que reproduce y amplifica desigualdades sociales presentes
  en las bases que alimentan estos sistemas** — que es la descripción exacta de un modelo de riesgo de deserción
  entrenado con datos históricos.

**La síntesis que importa para una propuesta:** la capa predictiva no está sólo desabastecida de código — está
quedando **condicionada a una arquitectura**. Un modelo centralizado entrenado con histórico de alumnos y que
emite una etiqueta de riesgo por persona es exactamente el objeto que las tres regiones están nombrando. Lo que
sobrevive a ese encuadre es la versión federada, con DP, con humano en el lazo y con el dato quieto — o sea,
**P25 más P34**.

Y hay un matiz que corrige la lectura del pase 11 sobre esta misma capa. El pase 11 anotó como debilidad que el
repo tope de la capa (`Aliipou/Student-Retention-Prediction`, MIT, 6 ★) **entrena con datos sintéticos**. Visto
desde este pase, entrenar con sintéticos no es la debilidad: **es la decisión correcta**. La debilidad es que lo
hace **sin garantía de privacidad declarada y sin evaluación de utilidad** — que es precisamente lo que
`synthcity` aporta de fábrica con sus métricas de *correctness* y *privacy*.


---

## 42. La máquina para gobernar el dato del alumno ya estaba instalada, lleva años en producción y es toda copyleft (agregado 2026-10-01, pase 17)

Es la tendencia que da vuelta la del pase 16, y las dos juntas describen la capa completa.

**La tendencia 39 dijo**: la infraestructura de privacidad es la única capa de esta KB donde lo maduro es
permisivo, y la educación no la usa. Eso era cierto **de las librerías horizontales** —DP, federado, sintéticos—.

**Lo que faltaba mirar es el LMS**, y ahí la forma es la inversa: **Moodle** (GPL-3.0, 7.5k ★, 123.147 commits)
tiene un **Privacy API en el núcleo que obliga a todos los plugins** a saber exportar y borrar el dato que
guardan; **Open edX** (AGPL-3.0, 8.2k ★) tiene un toolset de retiro de usuario con seis scripts y API REST de
retiro masivo que alcanza LMS, foros, credenciales y las demás IDAs. **No es incipiente: está desplegado en
decenas de miles de instituciones y lleva años en producción.**

**Por qué esto cambia el diagnóstico de la KB y no sólo lo amplía.** Dieciséis pasadas trataron la privacidad
educativa como una capa **faltante**. No falta: **falta operarla.** El `grep` del pase 16 sobre los ocho archivos
—`COPPA` 0, `differential privacy` 0, `federated` 0, `FERPA` 1— medía correctamente la ausencia en la KB, y de
ahí se concluyó ausencia en el sector. **Era ausencia de la KB.**

**Y el copyleft, por única vez en dieciséis pasadas, no es la mala noticia.** No hay que forkear: Moodle se
**extiende** (un `privacy provider` en el plugin propio) y Open edX se **invoca** (scripts y un endpoint). Lo que
se entrega es plugin, configuración, evidencia y operación — no una derivada del LMS. El entregable de esta capa
**casi no es software**, y eso la hace más barata de construir y más difícil de copiar. Ver **P36**.

⚠️ **El límite, y está declarado por el propio proveedor:** *«User retirement is not a compliance guarantee. The
Open edX software makes no claim of satisfying any law or regulation. It is a configurable toolset that site
operators can use to help meet the obligations apply to them specifically.»* El cumplimiento es del **operador
del sitio** — que es precisamente el alcance vendible, y la razón por la que esta capa es servicio y no producto.

## 43. Norteamérica pasó del mandato de política a la prohibición de entrenamiento, y es la primera ley que le toca el modelo de negocio al sector (agregado 2026-10-01, pase 17)

Las tendencias 8 y 40 registraron el reloj regulatorio de Norteamérica como **obligación de tener política
escrita** (COPPA enmendada, 2026-04-22) y como **exposición ya vencida**. Este pase registra el salto siguiente, y
es de otra naturaleza.

**California AB 1159** (Asambleísta **Dawn Addis**) pasó la Legislatura el **2026-08-31** y **el gobernador la
firmó el 2026-09-13**. Lo que hace:

- **Prohíbe** usar información cubierta del alumno —**incluidos identificadores únicos persistentes**— para
  **entrenar sistemas de AI generativa o desarrollar modelos de AI**, *salvo* que el uso sea **estrictamente en
  función de un propósito educativo y en beneficio de la institución educativa correspondiente**.
- **Prohíbe la venta** de datos de alumnos, y pone límites de compartición y retención.
- Crea la **HESIPA** (*Higher Education Student Information Protection Act*), que **entra en vigor el
  2027-07-01** y extiende por primera vez el régimen a **educación superior**: ~**2,9 millones** de estudiantes
  universitarios de California.
- Mejora **KOPIPA** y **ELPIPA**, y protege categorías sensibles: **estatus migratorio, identidad LGBTQ+ y salud
  reproductiva**.

**Por qué esto es distinto de todo el reloj regulatorio que esta KB tiene registrado.** El AI Act europeo, la ley
coreana y la vietnamita regulan **cómo** se usa el sistema: expediente de conformidad, supervisión humana,
transparencia. **AB 1159 prohíbe un insumo.** No pide documentar el entrenamiento sobre dato del alumno: lo
prohíbe, con una excepción acotada.

🔴 **Y le pega a un patrón propio de esta KB.** El **P16** —entrenar el estimador de *mastery*— y el **P1** —tutor
adaptativo con retención real— se apoyan en entrenar modelado del alumno con dato del alumno. **A partir del
2027-07-01 en California eso es ilícito salvo que se pruebe la excepción**, y la excepción no es «es educativo»
en abstracto: es **propósito educativo estricto y beneficio de esa institución**. Entrenar un modelo central con
dato de muchas instituciones para servir a todas **no cae obviamente dentro**, y es la arquitectura por defecto
de la industria.

**La lectura comercial, y es buena noticia para la arquitectura que esta KB ya eligió:** la excepción es
exactamente lo que el **aprendizaje federado** y el **entrenamiento on-premise** permiten defender —el dato no
sale de la institución y el beneficio es de la institución—. El pase 16 abrió esa capa (tendencia 39, **P34**) sin
saber que dieciocho días antes se había firmado la ley que la vuelve obligatoria en el mercado educativo más
grande de los Estados Unidos. Ver **P37** y el **gap 30**.

## 44. El incidente de Canvas movió el presupuesto de privacidad educativa más que cualquier fecha regulatoria (agregado 2026-10-01, pase 17)

Esta KB vende cumplimiento contra fechas. Esta tendencia registra que, en Norteamérica, **lo que abrió el
presupuesto fue un hecho consumado**.

**2026-04-29** y **2026-05-07**: dos incidentes en **Instructure**, con cambios no autorizados en páginas de
Canvas en el segundo. Interrumpió clases y exámenes finales en EE. UU., incluidas varias **HBCU**.
**ShinyHunters** reclamó ~**275 millones de registros** de alumnos, docentes y personal: nombres, correos,
**números de identificación de alumno** y **mensajes privados**. Sin indicio de SSN, fechas de nacimiento ni
contraseñas. **2026-05-11**: Instructure informó un **acuerdo con los atacantes** para devolución y destrucción
del dato, con *«shred logs»* como prueba de borrado.

**Canvas sostiene ~41 % de la educación superior del continente y miles de distritos K-12.** Por alcance, es el
incidente más consecuente que haya tocado al sector.

**Lo que esto cambia en una conversación de venta, y conviene no usarlo mal.** El argumento no es «su proveedor
es inseguro». Es que **el incidente dejó una pregunta sin respuesta que la institución no puede contestar sola**:
un acuerdo con el atacante y un log de borrado **no son verificables por la institución**, que sigue siendo la
responsable del dato y no tiene forma propia de saber qué se exfiltró de *sus* alumnos. La capacidad que faltaba
el 2026-04-29 —saber qué dato de qué alumno vive en qué sistema, exportarlo y borrarlo con evidencia— es
exactamente el Privacy API de Moodle y el retiro de Open edX, **operados**.

**Y el contexto que lo vuelve estructural, no anecdótico:** sólo el **11 %** de los distritos de EE. UU. aplica
medidas rigurosas de evaluación de privacidad antes de adoptar una herramienta de AI, y la violación de FERPA más
común de 2026 es **docentes pegando dato de alumnos en herramientas de AI de propósito general** sin acuerdo de
tratamiento — que no ocurre por imprudencia, sino porque **no hay herramienta conforme disponible en el
distrito**. El incidente de Canvas puso presupuesto donde ya había exposición.

## 45. Las dos mitades del derecho al olvido tienen licencias opuestas, y la permisiva es la que la educación no usa (agregado 2026-10-01, pase 18)

El pase 17 midió que la máquina para **borrar el registro** del alumno está instalada en el LMS y es **toda
copyleft**. Este pase midió la otra mitad —**borrar la influencia del dato sobre el modelo**— y es **toda
permisiva**. El contraste es exacto y es la tendencia:

| Mitad del derecho al olvido | Dónde vive | Licencia | ¿La usa la educación? |
|---|---|---|---|
| Borrar **el registro** | Instalado en el LMS: Privacy API de Moodle, `tool_dataprivacy`, `tool_policy`, retiro de Open edX | **Toda GPL-3.0 / AGPL-3.0** | Sí, viene de fábrica |
| Borrar **la influencia sobre el modelo** | Librerías horizontales de ML: `awesome-machine-unlearning` (MIT, 970 ★), `open-unlearning` (MIT, 607 ★), `awesome-llm-unlearning` (Apache-2.0, 627 ★), `SalUn` (MIT, 154 ★), `torchunlearn` (MIT, 12 ★), `model-provenance-kit` (Apache-2.0, 104 ★), `Data-Provenance-Collection` (Apache-2.0, 281 ★) | **Toda MIT / Apache-2.0** | **No. Cero.** |

**2.700+ estrellas combinadas, licencias que Globant puede usar para construir, y cero menciones de educación.**
Verificado buscando «education», «student» y «knowledge tracing» en los dos agregadores grandes (970 ★ y 627 ★):
ninguna aparición.

**Por qué esto es una tendencia y no un dato aislado:** es la **segunda** capa de esta KB donde lo maduro es
permisivo —la primera fue la privacidad horizontal del pase 16, con 26.000+ ★— y en las otras once lo maduro es
copyleft. Las dos capas permisivas son, las dos, **de cumplimiento**, **horizontales** y **sin adaptador
educativo**. Eso ya no describe una casualidad: describe dónde está el trabajo disponible. La industria de ML
resolvió el cumplimiento de forma reutilizable y **nadie lo trajo al aula**.

## 46. La ausencia que se registró por un nombre de rama, y cuesta una pasada entera (agregado 2026-10-01, pase 18)

El pase 17 declaró el **gap 29** —*«ningún `privacy provider` de referencia para un plugin de AI»*— después de
buscarlo y de registrar honestamente cuatro 404 contra `moodle/moodle`. **La referencia existía, estaba en el
núcleo y eran tres.** La causa del error no fue de criterio:

> **`moodle/moodle` no tiene rama `main` ni rama `master`.** Sus ramas son `MOODLE_XXX_STABLE`. Cualquier fetch
> contra `main` o `master` devuelve **404 con independencia de que el archivo exista**.

Medido por código HTTP en este pase: `ai/provider/openai/classes/privacy/provider.php` da **404 en `main`**, **404
en `master`**, **200 en `MOODLE_405_STABLE`** y **200 en `MOODLE_500_STABLE`**.

**Por qué merece ser una tendencia de la KB y no sólo una nota al pie:** esta KB mide ausencias y las vende como
información —*«un gap informado es información; el silencio se parece demasiado a la cobertura»*—. Entonces **el
método de medir ausencias es parte del producto**, y acá falló de una forma que se repite: un 404 contra un repo
grande, vivo y con releases versionadas es, con alta probabilidad, **un 404 sobre la rama**. La regla queda
escrita: **antes de declarar que algo no existe en un repo con releases, probar la rama de release.** El pase 17
tenía razón sobre terceros y se equivocó sobre el núcleo, y el costo fue una pasada entera de un gap mal abierto.

**Y el saldo positivo:** con las rutas correctas, `admin/tool/dataprivacy/version.php` y
`admin/tool/policy/version.php` dan **200**, con lo que el pase 17 deja de depender de snippets y la máquina de
privacidad del LMS queda **verificada de primera mano**.

## 47. LATAM produjo la mejor implementación de su capa y tiene cero estrellas, y esta vez el gap 2 no explica por qué (agregado 2026-10-01, pase 18)

El **gap 2** dice desde el pase 2 que *«LATAM produce agentes educativos, pero ninguno sale de la fase cero»*, y el
pase 13 lo reencuadró diciendo que el aporte real de LATAM no era el repo sino el instrumento de medición. **Este
pase encuentra el caso que no entra en ninguna de las dos lecturas.**

`jeanlucio/moodle-local_aihub` —Jean Lúcio, **Instituto Federal do Sertão Pernambucano, Brasil**— es, de las seis
piezas de la capa de `privacy provider` de la comunidad, **la más completa, y por margen**:

- **Cuatro** interfaces del Privacy API, incluida `user_preference_provider`, que ninguna otra implementa (las
  tres referencias del núcleo de Moodle implementan tres).
- Declara **las tres cosas a la vez**: tabla de base (`local_aihub_log`, 9 columnas), **6 preferencias de usuario**
  y **4 enlaces de ubicación externa** (`deepseek`, `google_gemini`, `groq`, `openai_compatible`).
- Diseño defendible: broker **BYOK** con *SSRF guard*, escalera de proveedores y *key store*; la API key es
  opcional y el plugin funciona sin ninguna; *«the hub never contacts a provider on its own»*.
- Disciplina de ingeniería que el resto de la capa no tiene: `.github/workflows/`, `tests/`, `docs/`, 60 commits.

**Tiene 0 estrellas y 1 fork.** Frente a: Ferrara (Italia) 3 ★ con tres interfaces, `tool_aiconnect` (Catalyst EU)
10 ★ sin provider visible, y una pieza de 0 ★ sin archivo `LICENSE`.

**Por qué el gap 2 no lo explica.** El gap 2 describe proyectos que no salen de la fase cero *por falta de
continuidad y de disciplina* —«buen problema, buen diseño, cero continuidad», como lo formuló el pase 11 para el
caso de la India—. **Acá la continuidad y la disciplina están**, y lo que falta es **visibilidad**: un repo con CI,
tests, docs y la implementación más completa de su categoría, invisible. La formulación correcta para este caso es
distinta y hay que escribirla aparte: **LATAM no sólo produce prototipos sin continuidad; también produce trabajo
mejor que el del promedio de su capa y no lo distribuye.** La acción no es construir: es **señalar**. Para esta KB
es la recomendación más barata que puede hacer —`local_aihub` es la referencia que **P39** usa cuando el plugin
guarda dato—, y para el autor, dos líneas en el directorio de plugins de Moodle.

**La lectura comercial, por región.** Un cliente de **EMEA** o **North America** que pida un plugin de AI con
expediente de privacidad va a recibir como referencia técnica una pieza **brasileña**, mantenida por un instituto
federal público. Eso es exactamente el argumento de *nearshore* de Studios con evidencia en vez de con
presentación.

## 48. El núcleo de Moodle documenta, en siete archivos idénticos, el punto donde su propia maquinaria de borrado se queda sin nada que borrar (agregado 2026-10-01, pase 19)

**El dato.** Moodle 5.3rc1 trae **siete** proveedores de AI en el núcleo (`anthropic`, `awsbedrock`, `azureai`,
`deepseek`, `gemini`, `ollama`, `openai`), y los siete traen `classes/privacy/provider.php`. Auditados sobre el
fuente, los siete son **idénticos en forma**: 70–78 líneas, **cero** llamadas a `delete_records`, `DELETE FROM` o
`add_database_table`, y **exactamente un** `add_external_location_link`. Todos sus métodos de borrado y export tienen
**el cuerpo vacío**, marcados `@codeCoverageIgnore`.

**La lectura correcta, que no es «están sin terminar».** Es la forma canónica para un plugin que **no guarda nada
localmente y sólo transmite**: lo único que tiene que declarar es el envío externo. Y por eso mismo **no sirven de
plantilla** para un plugin que sí guarde — ésa es otra, y está en el mismo árbol:
`public/ai/classes/privacy/provider.php` (`core_ai`), ~800 líneas, 6 tablas con `prompt` y `generatedcontent` entre
sus campos, y `delete_records_list()` real en las tres variantes de borrado.

**La tendencia, y es la que importa para una propuesta.** La línea divisoria dentro del propio núcleo de Moodle **no
es técnica, es de arquitectura de dato**: `core_ai` guarda el prompt y la respuesta, y por eso sabe borrarlos. Los
siete proveedores **no guardan: transmiten** — y lo único que pueden hacer es declararlo. Es decir: **el LMS más
desplegado del mundo documenta, siete veces, el punto exacto donde el derecho de supresión deja de ser ejecutable**,
porque el dato ya está en OpenAI, Anthropic, Google, AWS, Azure, DeepSeek o en el Ollama de un tercero.

**Por qué esto se vende y no sólo se anota.** Cualquier institución que active la AI de Moodle hereda esa frontera sin
decidirla. Un cliente que tiene que responder un pedido de supresión necesita saber **qué parte de la cadena alcanza
su Privacy API y qué parte no**, y la respuesta está escrita en el núcleo con nombre de archivo. Eso es un expediente
(**P35**) y un plugin (**P39**), no una discusión de principios.

> ⚠️ **Y la frase del propio núcleo que hay que leer antes de citar esto como tranquilizador** (se conserva del pase
> 18 porque sigue siendo exacta): `aiprovider_ollama` —el proveedor que un cliente elige **justamente** para que el
> dato no salga— declara «*No user data is **explicitly** sent*». El plugin no adjunta identidad; `prompttext` **sí**
> viaja, y el prompt lleva lo que el alumno escribió. **La declaración es exacta sobre la identidad y silenciosa
> sobre el contenido.**

## 49. La cadena de supresión tiene el agujero en la telemetría, y el estándar es el que lo abre (agregado 2026-10-01, pase 19)

**El dato, de arriba hacia abajo.** Esta KB venía construyendo una cadena de borrado de tres eslabones. Medidos los
tres en este pase:

| Eslabón | ¿Sabe borrar? | Con qué |
|---|---|---|
| **LMS** (el registro) | ✅ Sí | Privacy API de Moodle, `core_ai` con `delete_records_list()` — **GPL-3.0** |
| **Telemetría** (la historia del aprendizaje) | 🔴 **No** | **El estándar xAPI no define supresión.** Define *voiding*: marca sin borrar |
| **Modelo** (la influencia del dato) | ✅ Sí | OpenUnlearning (**MIT**, 607 ★), `torchunlearn` (MIT) — pero **no para modelos del alumno**: ver gap 34 |

**El eslabón del medio es el que falla, y falla en la especificación, no en las implementaciones.** xAPI —hoy IEEE
9274.1.1— no tiene operación de borrado de *statements*. Tiene ***voiding***: un statement nuevo con verbo `voided`
que declara obsoleto al anterior **dejándolo donde está**. Eso es exactamente lo contrario del art. 17 del GDPR, de
la Ley 21.719 chilena y del derecho de supresión que Vietnam, Corea y Brasil reconocen.

**Y abajo del estándar, el reparto de licencias repite por tercera vez el patrón de la tendencia 45:**

| LRS | Licencia | ★ | ¿Borra? |
|---|---|---|---|
| `lrsql` | **Apache-2.0** ✅ | 144 | 🚫 No documentado |
| Ralph | **MIT** ✅ | 51 | 🚫 No documentado |
| Learning Locker | **GPL-3.0** ⚠️ | 584 | ✅ Sí (API especial) |

**Lo permisivo no borra; lo que borra es copyleft.** Tres capas, tres veces el mismo reparto.

**Y hay que decirlo en primera persona, porque pega sobre el stack que esta KB recomienda.** `learnmcp-xapi` (MIT, en
la tabla principal) es el único artefacto de esta KB que conecta un agente con IEEE 9274.1.1, y declara como backends
**`lrsql`, Ralph y Veracity**: los permisivos. Un tutor armado con el stack recomendado por esta KB escribe la
historia del alumno en un almacén **del que no hay forma estándar de sacarla**. Eso no invalida el patrón: lo
convierte en un patrón con una obligación de diseño explícita (**P40**), y en una línea que hay que escribir en el
expediente antes de firmar.

**Consecuencia comercial, que es la parte útil.** La pregunta *«¿y si un padre pide que borren todo?»* no se contesta
con el LMS. Se contesta con **tres sistemas, tres licencias y un eslabón que hay que construir a medida** — y eso es
alcance facturable, no un riesgo que se esconde.

## 50. El dashboard que el regulador pide es la superficie de ataque que el regulador prohíbe (agregado 2026-10-01, pase 19)

**El dato.** **P-MIA** (arXiv 2511.04716) es el primer trabajo sistemático de inferencia de pertenencia contra
**modelos de *cognitive diagnosis***. Su modelo de amenaza es ***grey-box* y explota las funciones de explicabilidad
de la plataforma**: los vectores internos de estado de conocimiento **se exponen al usuario en visualizaciones —el
paper nombra los gráficos de radar— y se pueden revertir con precisión a partir de ellas**. Con probabilidades de
predicción + vectores reconstruidos, **supera con claridad** a los baselines *black-box* sobre tres datasets reales
contra CDMs mainstream. Mismo grupo que **PrivacyCD/HIF**; **ninguno de los dos publica código**.

**La tensión, dicha sin adornos.** El Anexo III del EU AI Act clasifica la evaluación automatizada como alto riesgo y
exige **transparencia y explicabilidad**. El GDPR exige **minimización**. P-MIA mide el costo de la primera en
términos de la segunda: **cuanto mejor le explicás el modelo al docente, más fácil es extraer de él quién estuvo en el
entrenamiento.** Las dos obligaciones aplican al mismo sistema y empujan en direcciones opuestas.

**Por qué le pega a esta KB y no es un riesgo genérico.** El dashboard de mastery **es algo que esta KB viene
recomendando**: es la salida natural de `pyKT` y `pyBKT`, es lo que `Gnos` instrumenta con su distinción
*vio / resolvió con ayuda / resolvió solo*, y es lo que la capa predictiva del pase 11 le muestra al docente. La
tendencia no es «hay un ataque nuevo»: es que **el artefacto que esta KB propone como entregable tiene un vector de
ataque publicado**.

**Lo que se hace al respecto, y es concreto:** ruido o cuantización en el vector de estado que se expone, o control de
acceso por rol de forma que el vector completo no salga nunca del lado docente — **y la decisión escrita en el
expediente de privacidad**, porque la elección entre explicabilidad y minimización es exactamente el tipo de decisión
que el Anexo III quiere ver justificada. Ver **P40**.

**Y el contrapeso, que es la buena noticia del pase:** la misma ventana trajo **OpenUnlearning** (MIT, 607 ★, CMU),
cuyas métricas **incluyen ataques de inferencia de pertenencia**. Es decir: **ya existe, con licencia permisiva, la
herramienta para medir si una defensa aguanta.** Lo que no existe es su aplicación a modelos del alumno — ése es el
**gap 34**, y es ensamblado, no investigación.

## 51. La industria construyó la máquina que prueba que una AI cumple, la publicó permisiva, y su catálogo de dominios cubre derecho, medicina y finanzas — educación no está (agregado 2026-10-01, pase 20)

Esta KB vende *expedientes de conformidad* desde el pase 4 —**P4** para el Anexo III europeo, **P10** para probar que
el tutor enseña, **P11** para el gate de seguridad pedagógica, **P17** para accesibilidad, **P39** para privacidad— y
en **diecinueve pasadas no registró una sola herramienta con la que ejecutarlos**. El pase 20 fue a buscarla y existe,
madura, permisiva, y publicada por organismos de gobierno:

- **`inspect_ai`** — **MIT**, **2.900 ★**, 763 forks, del **UK AI Security Institute**. 200+ evals pre-construidas.
- **`moonshot`** — **Apache-2.0**, 353 ★, de la **AI Verify Foundation** (Singapur, con IMDA). *Benchmarking* **y**
  *red-teaming*, con el **Starter Kit de IMDA v1.0 (enero 2026)** implementado como *cookbooks*.
- **`compl-ai`** — **Apache-2.0**, 211 ★, de **ETH Zürich + INSAIT + LatticeFlow AI**. **29 benchmarks mapeados a los
  6 principios núcleo del EU AI Act.**

**Y el hallazgo es la ausencia, declarada por los propios catálogos y no inferida de una búsqueda.** Tres artefactos de
tres jurisdicciones distintas publican su cobertura por dominio:

| Catálogo | Dominios que cubre | Educación |
|---|---|---|
| `LLM-Evals-Catalogue` (AI Verify Foundation) | **derecho, medicina, finanzas** | **ausente** |
| `compl-ai` (ETH Zürich / INSAIT / LatticeFlow) | 29 benchmarks sobre 6 principios del AI Act | **sin mención** |
| `awesome-eu-ai-act` (**CC0**) | 11 herramientas de conformidad open source | **ninguna educativa** |

**El contraste con lo que esta KB ya tiene es lo que convierte esto en oportunidad y no en queja.** Desde el pase 4
están registrados `EduBench` (**MIT**, ACL 2026, 9 contextos educativos), `SafeTutors` (**MIT**), `MathTutorBench`
(CC BY 4.0, EMNLP 2025 Oral) y `UnifyingAITutorEvaluation` (CC BY-SA 4.0, NAACL 2025): **benchmarks pedagógicos
premiados en los venues principales, y ninguno mapeado a un requisito regulatorio ni empaquetado como *recipe* de
ninguna herramienta.**

**Las dos mitades existen, están maduras, y son licencia-compatibles — MIT de un lado, Apache-2.0 del otro.** Lo que no
existe es el puente. Ése es el **gap 35**, y es distinto de todos los gaps técnicos de esta KB en un punto que decide
su valor: los gaps 31 y 34 esperan que alguien publique código; **el 35 se cierra con trabajo de integración sobre
repos que ya están verificados en esta KB.** No es investigación: es empaquetado. Y es el gap de mayor valor comercial
de esta KB, porque el expediente que habilita es el que ya se vende en cinco patrones. Ver **P42**.

⚠️ **Lo que este trend no dice, y es importante para no sobrevenderlo.** Ninguna de estas herramientas **certifica**:
`aiverify` declara por escrito que no define estándares éticos y **no garantiza** que el sistema evaluado esté libre de
riesgos o sesgos. El marco de Singapur es **voluntario** (sin penalidad, sin registro, sin *enforcement*), el europeo
no. No hay **crosswalk directo de AI Verify al EU AI Act** —sólo a **NIST AI RMF** (oct-2023) y a **ISO/IEC 42001:2023**
(jun-2024), y al AI Act se llega indirecto por ISO 42001—. Y `aiverify` evalúa **modelos supervisados tabulares y de
imagen, no agentes**: para un tutor LLM la pieza es Moonshot, Inspect o COMPL-AI.

## 52. Singapur tiene el despliegue educativo de AI más instrumentado del mundo y esta KB lo nombró una vez en diecinueve pasadas (agregado 2026-10-01, pase 20)

La KB registró de Singapur una sola línea: *«el agente tiene que vivir adentro del Student Learning Space»*. Es poco
para lo que hay. El **SLS** del MOE corre **ocho funciones de AI en producción nacional, seis de ellas usadas
directamente por el alumno**: **ALS** (Adaptive Learning System, matemática de primaria superior y secundaria inferior
+ geografía de secundaria superior), **LEA** (Learning Assistant), **FA-Math** (Feedback Assistant–Mathematics),
**AFA** (Annotated Feedback Assistant), **SAFA** (Short Answer Feedback Assistant) y **SET** (**Speech Evaluation
Tool**). Todas curadas, alineadas al currículo y supervisadas por docente, desarrolladas por **MOE + GovTech**.

**Y pega sobre tres cosas que esta KB tenía escritas:**

1. **La capa de lectura oral del pase 14, que se declaró desabastecida.** Ese pase escribió que la habilidad más
   evaluada en primaria en el mundo es la lectura oral y que **la KB no tenía una sola pieza para medirla**. Singapur
   la tiene desplegada a escala nacional (**SET**). **No cierra la capa** —es software estatal cerrado, no open
   source— pero cambia el argumento de venta: deja de ser una apuesta y pasa a ser **una función que un sistema
   educativo nacional ya considera indispensable**.
2. **El gap 6 (grading), intacto desde el pase 2.** Tres de las seis funciones del alumno son **asistentes de
   devolución** (FA-Math, AFA, SAFA). Singapur **confirma la demanda y no aporta oferta open source**: lo construyó el
   Estado, cerrado. **El gap 6 no se mueve** — pero deja de poder decirse que la demanda no está probada.
3. **La voz del menor del pase 16.** Un *Speech Evaluation Tool* usado por chicos es exactamente el caso que el pase 16
   levantó como regulado. Singapur lo resuelve con **plataforma estatal + supervisión docente** en vez de con
   consentimiento individual: **es una tercera vía de arquitectura que esta KB no tenía registrada.**

**La consecuencia arquitectónica, que ya estaba en la KB y ahora se entiende por qué.** El requisito de que el agente
viva **dentro** del SLS no es preferencia de compra: se corresponde con una política por nivel — según las fuentes
localizadas, **los alumnos de primaria inferior no usan AI directamente**, y **desde 4.º grado** el uso es
*estructurado, limitado, en clase y bajo supervisión docente*. Para un proyecto: **el SaaS suelto está descartado de
entrada**, y el entregable es un componente integrado con **control de nivel y traza de supervisión**.

⚠️ **Nivel de evidencia: secundario.** `moe.gov.sg` y `learning.moe.edu.sg` están **bloqueados por el proxy de egreso**
de esta sesión. Los nombres de las seis funciones y el alcance de ALS vienen de varias fuentes concordantes; **las otras
dos de las ocho no quedaron nombradas**. Hay que abrir la fuente del MOE antes de usar esto con un cliente.

## 53. El *machine unlearning* llegó a la educación, y entró por la puerta pedagógica en vez de por la de privacidad (agregado 2026-10-01, pase 20)

Los pases 18 y 19 abrieron la capa de *unlearning* buscando **la forma de cumplir el derecho al olvido sobre el modelo
del alumno** —borrar la influencia del dato, no sólo el registro— y dejaron el **gap 34**: *unlearning* evaluado sobre
modelos de alumno, con la nota de que `OpenUnlearning` (MIT, 607 ★) resuelve la técnica para LLMs pero **ninguno de sus
tres benchmarks evalúa un modelo de knowledge tracing o de cognitive diagnosis**.

El pase 20 encuentra el **primer repo educativo de *unlearning* con código publicado** —**`GEMLab-HKU/Unlearn_and_Relearn`**,
**MIT**, 4 ★, 22 commits, Universidad de Hong Kong— y **no cierra el gap 34, porque usa la técnica con el objetivo
invertido.**

**No borra para proteger a un alumno: borra para fabricar uno.** El problema que ataca es real y específico: un LLM al
que se le pide *«actuá como principiante»* se escapa igual hacia explicaciones de experto, y eso arruina las dinámicas
de *learning-by-teaching*, donde el alumno humano aprende enseñándole a un agente que **de verdad** no sabe. Entonces
aplica *unlearning* por destilación con intervención para volverlo novato de forma **configurable (10–50% de olvido)**,
y después mide cuánto **recupera** cuando el humano le enseña, con un loop de tres partes **Coach / Teachable Agent /
Judge**.

**Lo que esto cambia, y es más de lo que parece:**

- **El gap 34 sigue abierto** —falta el uso de **privacidad**— pero cambia de diagnóstico: **la maquinaria difícil ya
  existe en un contexto educativo y es MIT.** Borrar un concepto del modelo de un alumno y medir que se borró está
  implementado y funcionando. Lo que falta es **apuntarlo al objetivo de supresión**, no inventarlo.
- **Aparece una capacidad pedagógica que esta KB no tenía:** el **alumno simulado creíble**, que es la pieza que faltaba
  para evaluar un tutor sin poner chicos reales adelante — y eso conecta directo con **P10** y con el **gap 1** (el
  estándar de evaluación existe y no se adopta). Ver **P43**.
- ⚠️ **4 ★ y 0 forks: arquitectura de referencia, no dependencia.** Mismo criterio con el que el pase 8 trató a `tero`.

**🔴 Y la lección de método, que ya costó tres pasadas.** Los pases 18 y 19 buscaron este código y no lo encontraron por
una **colisión de terminología**: «knowledge tracing» significa dos cosas incompatibles. En esta KB y en `pyKT` es
*modelar el estado de conocimiento del alumno*; en la literatura de *unlearning* es *rastrear qué conocimiento de un
modelo fundacional vino de qué dato de entrenamiento* (p. ej. *Lifting Data-Tracing Machine Unlearning to
Knowledge-Tracing for Foundation Models*). **Buscar por la técnica devuelve el segundo sentido y entierra el primero.**
Lo que funcionó fue buscar por **escenario educativo** (*novice student simulation*) — exactamente la regla que el pase
5 aprendió para los benchmarks. **Tercera vez que esta KB paga el mismo peaje: cuando una búsqueda técnica no devuelve
nada en educación, hay que rehacerla por escenario antes de declarar el vacío.**

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
19. ~~**Los esquemas curriculares nacionales existen, son la pieza más cara de construir, y esta KB encontró dos de casualidad en dos pasadas distintas**~~ → **GAP CERRADO EN EL PASE 14 DEL 2026-10-01.** Se ejecutó la acción que este gap pedía (buscar por país, en el idioma del país). **De las cinco candidatas, cuatro existen y están verificadas** —Brasil (`bncc-dados`, MIT+CC BY 4.0), Inglaterra (`oak-curriculum-ontology`, MIT+OGL-3.0, con **11.207 *misconceptions***), EE. UU. (`commonstandardsproject/api`, Apache-2.0, los 50 estados) y Corea del Sur (ya registrada)—; **Australia (MRAC/ACARA) existe pero su licencia no se pudo verificar** (dominio bloqueado por el proxy) y **Singapur no apareció**. Además aparecieron dos cosas que el gap no anticipaba: **el estándar CASE con implementaciones certificadas** (tendencia 33) y **que esta capa no es copyleft** (tendencia 35, que corrige la lectura regional de abajo). El inventario completo está en `repos/foundations.md`. **Lo que queda abierto pasa al gap 23.** El texto original se conserva: **Los esquemas curriculares nacionales existen, son la pieza más cara de construir, y esta KB encontró dos de casualidad en dos pasadas distintas** *(agregado en el pase 11 del 2026-10-01)*. No es un gap de oferta: es un **gap de búsqueda**, y se declara para que la próxima pasada lo cierre a propósito.

    Lo que hay, sin haberlo buscado sistemáticamente:

    | Artefacto | Región | Licencia | Contenido |
    |---|---|---|---|
    | `nmarafo/OpenDidactia` *(pase 3)* | EMEA (España, LOMLOE) | **CC BY-SA 4.0** ⚠️ *share-alike* | Esquemas de Programación Didáctica y Situación de Aprendizaje para 17 comunidades + 2 ciudades autónomas, de Infantil a Bachillerato, FP y régimen especial |
    | `DECK6/korean-elementary-learning-map` *(pase 11)* | APAC (Corea del Sur, currículo revisado 2022) | **MIT** ✅ | **620 anclas de estándares de logro, 1.956 temas, 2.293 relaciones de prerrequisito, 152 clusters**, 11 materias, grados 1-6, en JSON y RDF/Turtle con *competency questions* SPARQL y restricciones SHACL |

    **Dos pasadas separadas por ocho ciclos encontraron el mismo tipo de artefacto en dos regiones distintas, y ninguna lo estaba buscando.** Eso es evidencia de que el resto probablemente exista: el *Common Core* y los estándares estatales de EE. UU., el *National Curriculum* británico, la BNCC de Brasil, los currículos de ACARA (Australia, que `mentar` ya consume en 157 plantillas) y de Singapur. **Si están publicados en formato estructurado, cada uno vale lo mismo que estos dos: es la pieza más cara de cualquier agente docente y la que ningún cliente quiere pagar dos veces.**

    **Y la comparación entre los dos que hay es la lección de método:** el coreano es **MIT** y trae el grafo de prerrequisitos y la validación formal; el español es **CC BY-SA** y no trae ninguna de las dos. **El artefacto de APAC es mejor técnicamente y más barato legalmente**, lo cual es el espejo del gap 4 — pero acá, por una vez, la concentración en APAC juega a favor del cliente y no en contra.

    **La acción para el próximo pase:** buscar explícitamente `curriculum ontology`, `achievement standards`, `learning map` y `prerequisite graph` por país, en el idioma del país, en vez de esperar que aparezcan buscando agentes.


20. ~~**Ninguna skill educativa del mundo tiene *eval* publicada, y esta KB tiene las herramientas para medirlas sin usarlas**~~ → **GAP CERRADO EN EL PASE 17 DEL 2026-10-01**, ejecutando la acción que el **gap 26** había dejado escrita (*buscar por `SKILL.md` + dominio educativo, no por repos educativos*). Ya existe skill educativa con *eval* publicada y es **Apache-2.0**:

    - **`anthropics/k12-teacher-skills`** (https://github.com/anthropics/k12-teacher-skills, **Apache-2.0**, **541 ★**) — *«Skills and eval rubrics for K-12 teachers, co-developed with Learning Commons»*. Cuatro skills y una carpeta **`evals/`** con el framework de evaluación y cómo adaptarlo. **Nuevo en esta KB, y es el nuevo techo permisivo del canal educativo: 541 ★ contra los 299 ★ de `universal-examprep-skill`.**
    - **`learning-commons-org/agent-skills`** (https://github.com/learning-commons-org/agent-skills, **Apache-2.0**, **35 ★**) — las mismas cuatro skills del lado del consorcio, con `evals/` de rúbricas de **pedagogía, rigor, formato y andamiaje del modelo**.

    Las cuatro skills: `k12-lesson-plan-creation`, `k12-lesson-differentiation`, `k12-lesson-prep` y `k12-check-for-understanding` (chequeos formativos de 1–3 ítems para estándares de matemática, con distractores y guía docente).

    ⚠️ **Y el gap se cierra con una corrección propia incorporada, no limpiamente.** Este gap **ya enumeraba** `learning-commons-org/agent-skills` entre sus siete paquetes y lo declaraba *«texto de prompt sin versionado semántico, sin suite de regresión y sin medición de efecto pedagógico»*. **Ese repo tiene `evals/`.** El pase 17 no pudo datar la carpeta, así que **no se sabe si el pase 12 la pasó por alto o si es posterior al pase 12** — se registra la duda en vez de resolverla a favor propio. Lo inequívocamente nuevo es el repo de 541 ★.

    **Lo que el cierre de este gap NO cierra:** el **gap 26** sigue abierto. *«No hay eval publicada»* es falso desde este pase; *«la educación no ocupó el canal»* sigue siendo cierto — **541 ★ contra las 47.200 ★ de `scientific-agent-skills` (MIT) son 87×**, peor que el 58× que midió el pase 12 contra el activo *share-alike*. Y el conjunto nuevo es chico: **cuatro** skills, **K-12**, con el chequeo formativo acotado a **matemática**. El valor es la **licencia y la eval**, no la cobertura.

    *Texto original del gap, conservado:* Los **siete** paquetes pedagógicos verificados en el pase 12 —`education-agent-skills` (815 ★), `human-skill-tree` (562 ★), `universal-examprep-skill` (299 ★), `algo-sensei` (281 ★), `universal-diagnostic-tutor-skill` (234 ★), `kaogong-skill` (147 ★), `learning-commons-org/agent-skills` (35 ★)— Los **siete** paquetes pedagógicos verificados en este pase —`education-agent-skills` (815 ★), `human-skill-tree` (562 ★), `universal-examprep-skill` (299 ★), `algo-sensei` (281 ★), `universal-diagnostic-tutor-skill` (234 ★), `kaogong-skill` (147 ★), `learning-commons-org/agent-skills` (35 ★)— son **texto de prompt sin versionado semántico, sin suite de regresión y sin medición de efecto pedagógico.**

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


23. **Ningún ministerio publica su currículo nacional *como* marco CASE, y es el último tramo que falta de la capa que el pase 14 cerró** *(agregado en el pase 14 del 2026-10-01)*. Es el gap que abre el cierre del gap 19, y es chico, concreto y caro de ignorar.

    Los cuatro esquemas curriculares nacionales verificados se publican **cada uno en su propio formato**: RDF/Turtle el inglés y el coreano, JSON propio el brasileño, JSON para proveedores K-12 el estadounidense. Las implementaciones de **CASE** que existen (`OpenCASE` Apache-2.0 certificado v1.1, `compeito` Apache-2.0, `opensalt` MIT) son **herramientas de publicación sin marcos nacionales publicados en ellas**.

    **Nadie cerró el círculo.** El estándar existe, los datos existen, las dos cosas no se tocan — y es exactamente la misma forma del gap 13 (*«ningún agente open source emite ni consume credenciales verificables: el stack del alumno y el stack de la credencial no se tocan»*). **Dos capas distintas, el mismo diagnóstico: la KB tiene las piezas y nadie las conectó.**

    **Por qué es una oportunidad y no una queja:** publicar la BNCC o los estándares de un estado de EE. UU. como marco CASE conforme es trabajo de **días**, no de meses — los datos están en JSON con proveniencia y el servidor es Apache-2.0 con certificación de febrero de 2026. El resultado es un activo reutilizable en todo el país y auditable contra un estándar. Es el patrón **P31**.

24. **La capa de habla y la capa de agente no se tocan: ninguno de los 31 agentes de esta KB tiene voz** *(agregado en el pase 14 del 2026-10-01)*. Se verificó contra la tabla principal de `agents/top.md`, agente por agente: **ni DeepTutor, ni Educhain, ni OpenTutor, ni OpenTutorAI-CE, ni Bloom, ni ninguno de los demás tiene entrada ni salida de voz.**

    Y tampoco existe el puente: **no hay ningún servidor MCP que exponga evaluación de pronunciación o de fluidez lectora**, aunque el patrón está probado en esta misma KB y en este mismo pase (`bncc-mcp`, MIT, expone un currículo nacional completo por MCP).

    **Las dos mitades existen y son permisivas:** `OpenPronounce` (MIT, 85 ★) mide fonema a fonema con prosodia y corre local; los agentes de la tabla saben conversar, planificar y recordar. **Lo que no existe es el servidor MCP de cinco herramientas que los une** — y es, por tamaño de trabajo, comparable al que `bncc-mcp` ya resolvió para currículo con 14 ★.

    **Es, después del gap 20 y del pedido de licencia a `carrera-lectora`, el tercer vacío más barato de cerrar de los veinticuatro declarados**, y el único que habilita una vertical entera que esta KB no puede atender hoy: **alfabetización inicial y enseñanza de idiomas.** Sin voz, un tutor no sirve en los primeros años de escolaridad, que es donde los sistemas educativos de las cuatro regiones ponen la mayor parte del presupuesto de evaluación.

25. **Nada en el ecosistema educativo open source marca ni verifica la procedencia de lo que genera, y en EMEA eso es obligatorio en 62 días** *(agregado en el pase 15 del 2026-10-01)*. Es el gap con **fecha legal más cercana** de los veinticinco declarados, y el único que esta KB venía **vendiendo sin tener implementación**.

    **Lo que falta no es la tecnología.** La infraestructura está lista y es permisiva: **SynthID-Text** (Apache-2.0, dentro de `huggingface/transformers`, con `SynthIDTextWatermarkLogitsProcessor` y `SynthIDTextWatermarkDetector`), **MarkLLM** (Apache-2.0, 1.100 ★, 23+ algoritmos y 12 herramientas de evaluación), **c2pa-rs** y **c2pa-python** (MIT + Apache-2.0 dual, 1.907 y 344 commits).

    **Lo que falta es el puente al aula, y no existe en ninguna forma:** ni plugin de LMS, ni herramienta LTI, ni servidor MCP, ni XBlock que marque la salida de un tutor o verifique un manifiesto C2PA en una entrega. Se buscó explícitamente. Lo único que hay en el directorio de Moodle son **envoltorios de servicios propietarios** —Compilatio (plugin GPL-3.0, 821 instalaciones), Originality.ai, Copyleaks—, que además hacen lo contrario: **detectan** en vez de marcar.

    **Y la mitad forense del problema no se puede usar para cerrarlo.** La capa de detección existe, es permisiva y está publicada en ICLR, ICML y ACL (`fast-detect-gpt` MIT 434 ★, `Binoculars` BSD-3 420 ★, `RAID` MIT 216 ★, `sloptotal` MIT 39 ★) — y tiene **61,3 % de falsos positivos sobre escritura de no nativos de inglés**, **5,85 %** sobre abstracts académicos anteriores a 2018, y se rompe con paráfrasis. **Un score es evidencia, no prueba.** Ver la tendencia 36.

    **Por qué es el gap más barato con fecha más dura.** El **Artículo 50** está en vigor desde el **2026-08-02** y los sistemas ya en mercado tienen hasta el **2026-12-02** para el marcado legible por máquina del 50(2). Para un tutor construido sobre Transformers —casi cualquiera de esta KB— el lado del texto es **un `WatermarkingConfig` en la llamada de generación**. El trabajo real está en C2PA (identidad de firma, custodia de claves, validación) y en el puente al LMS. Es un proyecto de semanas, no de meses, con obligación legal detrás.

    ⚠️ **Y la deuda propia que hay que registrar:** desde el pase 4 esta KB recomienda *«vender el Artículo 50 antes que el Anexo III»* con el deadline bien puesto. **Once pasadas con la oferta escrita y cero implementación detrás.** El gap se declara con la corrección incluida para que no vuelva a pasar: **cuando la KB recomiende cumplir una obligación, tiene que nombrar el código que la cumple.**

    🔴 **Sin resolver en este pase:** la fecha de publicación del **Code of Practice** europeo sobre marcado y etiquetado aparece como **10 de junio de 2026** en una fuente y **20 de julio de 2026** en otra. `digital-strategy.ec.europa.eu`, `artificialintelligenceact.eu` e `iptc.org` están **bloqueados por el proxy de egreso**. Resolver contra la fuente oficial antes de citarla a un cliente. Lo consistente en todas las fuentes: vigencia 2026-08-02, marcado 2026-12-02, C2PA como estándar de facto del metadato en un esquema por capas.

26. **La educación no usa el canal de distribución de *skills* de agente, pero la evasión de detectores sí — en español y con licencia MIT** *(agregado en el pase 15 del 2026-10-01)*. Es la continuación medida del gap que abrió el pase 12, y le da la vuelta desagradable.

    El pase 12 midió que la vertical científica construyó en el canal de *skills* de agente una biblioteca de **47,2k ★ con MIT** mientras la educativa tiene **815 ★ y es *share-alike*** — 58× de diferencia en el canal de distribución más barato de la industria. La conclusión fue que la educación **no estaba usando el canal**.

    **Lo está usando. Del lado adversario.** **`ervin-mo/humanizar-es`** (https://github.com/ervin-mo/humanizar-es, **MIT**, 0 ★, 6 commits) reescribe texto en **español** generado por AI para que los detectores dejen de marcarlo sin cambiar lo que dice, usando **Binoculars y Fast-DetectGPT sobre Qwen2.5-0.5B** como guía local — y está empaquetado como **`SKILL.md` para Claude Code, Codex, OpenCode, Antigravity, DeepSeek Harness y Gemini CLI**. El autor declara un párrafo pasando de **100 % a 0 % de «AI»**, acota que la evidencia es **un solo ensayo** y aclara que **no está pensado para entregar trabajo calificado**.

    **No es el repo —tiene 0 estrellas— es la asimetría.** La evasión se distribuye como *skill* instalable en **seis harnesses**, en español, gratis, con los detectores de esta KB adentro. La integridad se distribuye como **plugin propietario de LMS con servicio pago detrás**. Un lado tiene costo marginal cero y alcance global; el otro tiene ciclo de compra institucional.

    **Por qué esto cierra el argumento de la tendencia 36 en vez de abrir uno nuevo:** cualquier estrategia de integridad basada en detección compite contra una herramienta de evasión que **usa el mismo detector como función objetivo** y que se instala en un comando. Esa carrera no se gana. La que sí se puede ganar es la de **procedencia**, porque marcar en el origen no es un clasificador que se pueda optimizar en contra. Ver el **gap 25** y **P33**.

    **La acción para la próxima pasada:** medir el canal otra vez, pero buscando por **`SKILL.md` + dominio educativo** en vez de por repos educativos — que es el error de método que el pase 12 ya documentó y que este pase confirma desde el otro lado. Si la evasión llegó al canal, la pedagogía puede.


27. **Ningún agente educativo open source declara una postura de privacidad, y ninguna pieza de privacidad habla educación** *(agregado en el pase 16 del 2026-10-01)*. Es un gap de doble filo y las dos mitades se midieron en este pase.

    *Mitad A — los agentes.* Se revisaron los **31** de la tabla principal de `agents/top.md` buscando una declaración de qué hacen con el dato del alumno: dónde queda, si se usa para entrenar, si se puede desplegar sin que salga de la institución. **Ninguno la tiene.** No declaran una política mala: no declaran ninguna. Lo más cercano es la capa de memoria —DeepTutor con memoria en tres capas, `learnmcp-xapi` persistiendo contra un LRS— que describe **dónde** queda el dato pero nunca bajo **qué base legal** ni con qué retención. Eso importa porque desde el **2026-04-22** la regla COPPA enmendada exige política **escrita** de retención y prohíbe la retención indefinida.

    *Mitad B — las piezas de privacidad.* Las ocho librerías maduras de la capa (26.000+ ★ combinadas, todas Apache-2.0 o MIT) son **horizontales**: ninguna trae un adaptador educativo, ni plugin de LMS, ni servidor MCP, ni ejemplo con datos de knowledge tracing. Lo específicamente educativo son cuatro repos con techo de **10 ★**, y **tres no declaran licencia**.

    **Por qué este gap es distinto a los otros 26:** no es falta de oferta ni trampa de licencia. La oferta existe, es enorme y es permisiva. **Lo que falta es un puente de integración de tamaño conocido**, y hay prueba de que es factible: `FedGKT` ya corre knowledge tracing federado sobre Flower con grafos de prerrequisitos anotados por expertos. Lo hizo **un repo de 1 estrella sin licencia**. Es el gap más barato de cerrar de esta KB y el que mejor se defiende ante un regulador. Ver **P34**.

28. **La capa de voz que el pase 14 abrió es dato biométrico regulado en Norteamérica, y esta KB la registró sin ese encuadre** *(agregado en el pase 16 del 2026-10-01)*. Es un gap de **método propio**, como el 11 y el 25, y se declara en vez de corregirlo en silencio.

    El **pase 14** abrió la capa de lectura oral y pronunciación —la primera capa de voz de esta KB— y dejó el **gap 24** anotando que ninguno de los 31 agentes tiene voz. El análisis fue íntegramente de producto: qué repos hay, qué licencia tienen, qué resuelven en primaria. **No registró que la voz de un menor ya es información personal regulada.**

    Lo que faltaba: la regla COPPA enmendada agregó los **identificadores biométricos** a la definición de información personal, y la enumeración incluye **voiceprints** junto con faceprints, huellas dactilares y de palma. **Cumplimiento exigible desde el 2026-04-22.** Si el despliegue toca **Illinois**, **BIPA** suma consentimiento escrito con daños estatutarios de **1.000 a 5.000 USD por violación** — por alumno, en un producto cuyo caso de uso natural es un aula entera.

    **Lo que no cambia:** la capa de voz sigue siendo una buena oportunidad y los repos del pase 14 siguen siendo los que son. **Lo que cambia es el presupuesto y el orden:** un piloto de lectura oral en Norteamérica necesita el consentimiento parental verificable y la política de retención **antes** del piloto, no después, y eso es alcance que el pase 14 no contabilizó. Ver **P35**, que lo empaqueta como entregable propio.

    ⚠️ **Y la generalización que conviene hacer, porque va a volver a pasar:** esta KB abre capas por *capacidad* —qué sabe hacer el software— y recién después, si alguien pregunta, por *régimen*. Pasó con el watermarking en el pase 15 (la KB vendía un deadline sin implementación) y pasó acá al revés (la KB registró una implementación sin su deadline). **Toda capa nueva que toque a un menor necesita las dos lecturas en la misma pasada.**


29. **La máquina de privacidad del LMS no habla con ningún agente, y es la tercera capa consecutiva con ese mismo diagnóstico** *(agregado en el pase 17 del 2026-10-01)*. No es un gap de oferta ni de licencia: es un **gap de puente**, del tamaño conocido, y es el tercero idéntico seguido.

    Lo que existe y está maduro: el **Privacy API** de Moodle en el núcleo, que **obliga a todos los plugins** —incluidos los de terceros— a declarar qué dato guardan y a saber exportarlo y borrarlo, más `tool_dataprivacy` (flujo de pedidos, delegado de protección de datos, retención) y `tool_policy`. Y el **user retirement** de Open edX: seis scripts verificados por nombre más `lms/djangoapps/bulk_user_retirement` (API REST de retiro masivo), que alcanza LMS, foros, credenciales y las demás IDAs.

    **Lo que no existe, buscado explícitamente en este pase:** ningún servidor MCP, ninguna herramienta LTI, ningún plugin publicado que conecte un agente al Privacy API de Moodle o al retiro de Open edX. Y —la pieza más chica y más vendible— **ningún `privacy provider` de referencia para un plugin de AI**, que es justamente lo que el núcleo de Moodle exige de cualquier plugin que guarde dato del alumno.

    **Por qué es la tercera vez:** el pase 15 encontró la misma forma en procedencia (SynthID-Text y C2PA existen y son permisivos; el puente al aula no existe) y el pase 16 en privacidad horizontal (ocho librerías maduras, 26.000+ ★, ningún adaptador educativo). **Tres capas seguidas donde la infraestructura está resuelta y lo que falta es integración de tamaño acotado.** Eso ya no es una coincidencia de tres capas: es la descripción del mercado en el que Studios entra. Ver **P36**.

    ⚠️ **Y la mitad que este pase no pudo cerrar:** no se ubicó en abierto un toolset de retiro equivalente para **Canvas** (AGPL-3.0, 6.9k ★). Se declara **no encontrado, no inexistente** — no se auditó el árbol completo del repo en este pase.

30. **Ninguna pieza open source puede probar con qué dato se entrenó un modelo educativo, y California acaba de convertir eso en el requisito que decide si el modelo es legal** *(agregado en el pase 17 del 2026-10-01)*. Es el gap con la **consecuencia arquitectónica más directa** sobre los patrones propios de esta KB, y el primero que nace de una ley ya firmada en lugar de una fecha futura.

    **El requisito.** **California AB 1159**, firmada el **2026-09-13**, prohíbe usar información cubierta del alumno —incluidos **identificadores únicos persistentes**— para **entrenar AI generativa o desarrollar modelos**, *salvo* que el uso sea **estrictamente en función de un propósito educativo y en beneficio de la institución educativa correspondiente**. La **HESIPA** extiende el régimen a **educación superior** desde el **2027-07-01** (~2,9 millones de estudiantes).

    **Lo que falta, y se buscó:** no hay en abierto ninguna pieza que produzca **procedencia del dato de entrenamiento a nivel de alumno y de institución** — ni *manifest* por corrida de entrenamiento, ni atestación de qué registros entraron, ni forma de demostrar que un modelo entrenado se benefició *de esa* institución y no de un agregado multi-institución. El **Privacy API del LMS no alcanza**: borra el registro, **no el modelo**.

    🔴 **Y le pega a dos patrones propios.** **P1** (tutor adaptativo con retención real) y **P16** (entrenar el estimador de *mastery*) se apoyan en entrenar modelado del alumno con dato del alumno. La arquitectura por defecto de la industria —un modelo central entrenado con dato de muchas instituciones para servir a todas— **no cae obviamente dentro de la excepción**. Esta KB tiene que dejar de ofrecer P1 y P16 en California sin la cláusula de procedencia adelante.

    **La buena noticia, y es que la arquitectura ya estaba elegida antes de conocerse la ley.** La excepción es exactamente lo que el **aprendizaje federado** y el **entrenamiento on-premise** permiten defender: el dato no sale de la institución y el beneficio es de la institución. El pase 16 abrió esa capa (**P34**) **dieciocho días después** de que se firmara la ley que la vuelve obligatoria en el mercado educativo más grande de EE. UU., y sin registrarla. Lo que falta no es la arquitectura: es **la evidencia**. Ver **P37** y la tendencia **43**.


31. **La capa que borra la influencia del dato sobre el modelo es grande, madura y permisiva, y no menciona educación en ninguna parte** *(agregado en el pase 18 del 2026-10-01)*. Este gap **reemplaza la formulación del gap 30 por el lado del modelo** y nace de ejecutar la acción que el pase 17 dejó escrita.

    **Lo que se encontró, y la predicción del pase 17 era correcta.** Buscando por `machine unlearning` —el término que el pase 17 anotó como no buscado— aparece una capa de **2.700+ estrellas combinadas** y **toda permisiva**: `tamlhp/awesome-machine-unlearning` (**MIT, 970 ★**), `jjbrophy47/machine_unlearning` (965 ★, **sin licencia declarada**), `chrisliu298/awesome-llm-unlearning` (**Apache-2.0, 627 ★**), `locuslab/open-unlearning` (**MIT, 607 ★**, 12 métodos, TOFU/MUSE/WMDP), `Data-Provenance-Initiative/Data-Provenance-Collection` (**Apache-2.0, 281 ★**), `OPTML-Group/Unlearn-Saliency` (**MIT, 154 ★**, ICLR 2024 Spotlight), `cisco-ai-defense/model-provenance-kit` (**Apache-2.0, 104 ★**) y `Harry24k/machine-unlearning-pytorch` (**MIT, 12 ★**, NeurIPS 2025).

    **Lo que falta.** **Ninguna menciona educación, dato de alumno ni knowledge tracing.** Verificado buscando los términos en los dos agregadores grandes: cero apariciones. Y el único trabajo específico de la industria —**PrivacyCD**, arXiv **2511.03966**, que se declara *el primer estudio sistemático de data unlearning para modelos de cognitive diagnosis* y aporta el algoritmo **HIF**— **no publica código**. Es la tercera capa de esta KB donde la pieza más específica es la que no publica, después de contenido curricular (pase 10) y predictiva (pase 11).

    **Por qué este gap es más barato de lo que parece, y es una conclusión de ingeniería.** Los dos estimadores de *mastery* de esta KB se comportan distinto: **`pyKT` es PyTorch** → `torchunlearn` y `SalUn` son aplicables en principio, y es integración con riesgo técnico; **`pyBKT` no es PyTorch** (BKT por EM) → ninguna librería lo alcanza, y la respuesta correcta **no es unlearning sino reajustar sin el alumno**, que para BKT es barato y además es ***exact unlearning*** — la garantía más fuerte que existe. **Mejor resultado legal por menos trabajo.** Ver **P38**.

    🚫 **El barrido regional de esta capa, declarado en vez de omitido:** **North America** concentra la oferta (`locuslab`/CMU, `OPTML-Group`/Michigan State, `cisco-ai-defense`, `Data-Provenance-Initiative`/MIT Media Lab); **APAC** es segunda y tiene lo único educativo (`torchunlearn` Corea, `tamlhp` Australia, autores de PrivacyCD); **EMEA** y **LATAM**: **ninguna pieza encontrada**, declarado como *no encontrado, no inexistente*. El caso de EMEA es el llamativo: es la región donde el **derecho de supresión del GDPR art. 17** es directamente exigible, y no tiene oferta propia de la tecnología que lo cumple.

    ⚠️ **Nivel de evidencia:** los repos se verificaron de primera mano. Los metadatos de los papers vienen de **snippets concordantes**, no de la fuente primaria: `arxiv.org` está bloqueado por el proxy de esta sesión (igual que `blogs.cisco.com` y `helpnetsecurity.com`). Ver el gap 17.

32. ~~**Nada conecta el pedido de borrado del LMS con el borrado en el modelo**~~ → ✅ **CERRADO EN EL PASE 19 DEL 2026-10-01, REFUTANDO LA HIPÓTESIS DEL PASE 18** *(agregado en el pase 18 del 2026-10-01)*.

    **El pase 18 dejó escrita «la hipótesis más barata que esta KB tiene abierta»:** que el Privacy API **emite un evento al aprobar un pedido** y que, si ese evento es observable, el puente sería un `db/events.php` de diez líneas. **Se midió sobre el árbol real de `moodle/moodle` (`main` = 5.3rc1) y la hipótesis es falsa en su dirección:**

    - `public/admin/tool/dataprivacy/db/events.php` registra **exactamente un** observer, y va **hacia adentro**: escucha `\core\event\user_deleted` para **crear** un pedido de borrado (`user_deleted_observer::create_delete_data_request`, gated por la config `automaticdeletionrequests`). **Es el sentido contrario al que hacía falta.**
    - **`tool_dataprivacy` no emite ningún evento.** Recorridos los **187 archivos** del subárbol: **cero** llamadas a `trigger()`.
    - `api::update_request_status()` —por donde pasa `approve_data_request()`— es **una escritura de base de datos y nada más**. Sin evento, sin hook, sin notificación.
    - *Control negativo:* el mismo `api.php` tiene **1.678 líneas** y `approve_data_request()` está en la línea **642**. El archivo existía y el grep era válido: **la ausencia es real.**

    **Lo que el gap deja como resultado utilizable, y es más valioso que un «sigue abierto»:** el puente **no puede ser un observer**, y por lo tanto hay exactamente dos formas de construirlo (ver **P40**) — **(a)** sondear `tool_dataprivacy_request.status`, la única superficie observable que existe, o **(b)** disparar desde afuera vía web-service. **Eso convierte el gap en alcance cotizable con mecanismo conocido**, que es justo lo que un gap debería producir. Lo que queda de investigación abierta se reformuló como **gap 34**.

    ⚠️ **Y lo que este gap no promete** (se conserva del pase 18, sigue vigente): para deep knowledge tracing el *unlearning* es **aproximado** y queda residuo medible. El entregable es el borrado **más la métrica de verificación** — que desde el pase 19 tiene herramienta permisiva: las métricas de *membership inference* de **OpenUnlearning** (MIT). No vender «olvido garantizado» sobre un modelo deep.


    **Las dos puntas existen y están verificadas.** Del lado del LMS: el **Privacy API** de Moodle, `admin/tool/dataprivacy` y `admin/tool/policy` **en el núcleo** (verificado por código HTTP en `MOODLE_500_STABLE`), más los `privacy provider` de AI del núcleo (⚠️ **el pase 19 corrigió esto: son siete, no tres, y ninguno de los siete borra nada — la plantilla real es `core_ai`; ver la tendencia 48**) y el retiro de usuario de Open edX. Del lado del modelo: la capa permisiva de *unlearning* del gap 31.

    **Lo que no existe, y se buscó:** ningún *hook*, plugin, herramienta LTI ni servidor MCP que, a partir de un pedido de supresión **aprobado** en el LMS, dispare el reajuste o el *unlearning* del estimador de *mastery*. El flujo del LMS termina en el borrado de filas. **El modelo no se enteró.**

    **Por qué es la quinta vez, y a esta altura es la descripción del mercado.** Pase 15: procedencia (SynthID-Text y C2PA existen y son permisivos; el puente al aula no). Pase 16: privacidad horizontal (ocho librerías, 26.000+ ★, ningún adaptador educativo). Pase 17: privacidad del LMS (la máquina instalada, ningún agente que la use). Pase 18, dos veces: la capa de *unlearning* sin educación (gap 31) y **este disparador ausente**. **Cinco capas seguidas donde la infraestructura está resuelta y lo que falta es integración de tamaño acotado.** Esa es la forma del trabajo que Studios puede vender en esta industria, y conviene dejar de tratarla como un hallazgo por pase.

    ⚠️ **Y lo que este gap no promete.** Para deep knowledge tracing el *unlearning* es **aproximado**: queda residuo medible. El entregable es el borrado **más la métrica de verificación**. No vender «olvido garantizado» sobre un modelo deep; si el cliente necesita garantía absoluta, la respuesta honesta es reentrenar — o elegir BKT desde el principio, que es la recomendación de **P38**.

33. ~~**Ningún LRS permisivo implementa el borrado, y el estándar xAPI tampoco lo contempla**~~ 🔴 **CERRADO POR REFUTACIÓN EN EL PASE 21** *(abierto en el pase 19 del 2026-10-01, cerrado el 2026-10-01)*.

    🔴 **La primera mitad era falsa, y se detectó leyendo el código en vez de la documentación.** **`lrsql` (Apache-2.0) implementa `DELETE /admin/agents`**: borrado **por `actor-ifi`** —la identidad xAPI del alumno— en cascada sobre **7 tablas** y dentro de **una transacción**, más una migración `ON DELETE CASCADE` puesta a propósito para que no quede residuo en `statement_to_actor`. ⚠️ **Viene apagado**: `LRSQL_ENABLE_ADMIN_DELETE_ACTOR=false` por default en producción. **Learning Locker** también borra (por filtro), confirmado. **Ralph** no en la API del LRS, pero sí en su *data backend* por ID de statement — y 🔴 **con backend ClickHouse es imposible**.

    **La segunda mitad se sostiene, y es lo único que queda del gap:** **xAPI / IEEE 9274.1.1 no define supresión** (define *voiding*), así que todo borrado acá es **extensión propia de cada implementación y no es portable entre LRS**. Lo que queda abierto es la **evidencia** (**gap 36**) y el **disparador LMS→LRS** (**P40**, ahora con la limitación declarada por escrito por ILIAS — ver tendencia **55**), **no la capacidad**. Ver las tendencias **54**, **55** y **56**, el patrón **P44**, y la corrección completa en `repos/foundations.md`.

    **El registro original del pase 19 se conserva abajo, porque el error de método es el hallazgo:** un gap declarado sobre documentación no es un gap, es una lectura pendiente.

    **Formulación original (pase 19):** Es el **eslabón del medio** de la cadena de supresión que esta KB venía construyendo, y el único que falla.

    **Empieza arriba de los repos, en la especificación.** **xAPI —hoy IEEE 9274.1.1— no define una operación de supresión de *statements*.** Define ***voiding***: un statement nuevo con verbo `voided` que declara obsoleto al anterior **dejándolo donde está**. Eso es lo contrario del art. 17 del GDPR, de la Ley 21.719 chilena y del derecho de supresión que reconocen Vietnam, Corea y Brasil.

    **Y abajo, el reparto de licencias repite por tercera vez el patrón de la tendencia 45:** `lrsql` (**Apache-2.0**, 144 ★) 🚫 no documenta borrado; Ralph (**MIT**, 51 ★) 🚫 tampoco; **Learning Locker (GPL-3.0, 584 ★)** ✅ es el único al que se le atribuye API de borrado. **Lo permisivo no borra; lo que borra es copyleft.**

    **Por qué este gap es de esta KB y no del mercado:** `learnmcp-xapi` (MIT) está en la tabla principal como el único puente agente↔IEEE 9274.1.1, y declara como backends **`lrsql`, Ralph y Veracity** — los permisivos. **El stack que esta KB recomienda escribe la historia del alumno en un almacén del que no hay forma estándar de sacarla.** No invalida el patrón: le agrega una obligación de diseño explícita (**P40**) y una línea en el expediente.

    ⚠️ **Límite de la afirmación.** El «no» es **ausencia en la documentación publicada**, no imposibilidad: las dos son bases SQL/Elasticsearch y un `DELETE` a mano siempre es posible. La afirmación exacta: **ninguno ofrece el borrado como operación soportada y documentada**, y por eso ninguno puede figurar en un expediente como el componente que cumple el art. 17 — el `DELETE` a mano es trabajo a medida y se cotiza como tal. El «sí» de Learning Locker es de fuente secundaria y **sigue sin verificarse contra su API**: es la acción 1 que este pase deja escrita.

34. ***Unlearning* evaluado sobre modelos del alumno** *(agregado en el pase 19 del 2026-10-01)*. Es lo que queda del gap 32 después de medirlo, y es **el hueco más construible que tiene esta KB**.

    **La asimetría, en una tabla de dos filas.** Para el **tutor LLM** la capa está resuelta y es permisiva: **OpenUnlearning** (MIT, **607 ★**, Locus Lab / CMU) trae TOFU, MUSE y WMDP, 12+ métodos y **10+ métricas que incluyen ataques de inferencia de pertenencia**. Para el **estimador de mastery** —que en educación es el modelo que contiene el dato sensible— **no hay nada**: ninguno de los tres benchmarks evalúa *knowledge tracing* ni *cognitive diagnosis*, y el único trabajo específico (**PrivacyCD/HIF**, arXiv 2511.03966) **no libera código**, igual que su contraparte de ataque (**P-MIA**, arXiv 2511.04716).

    **Por qué es construible y no investigación de frontera:** las tres piezas existen y las tres son permisivas. `pyKT` es **MIT** y es PyTorch; `torchunlearn` es **MIT** y trae 20 algoritmos; las métricas de ataque de OpenUnlearning son **MIT**. **Falta el ensamblado y la medición, no el método.** El entregable es exactamente el número que hoy **P38** no puede prometer, y convierte «olvido aproximado» en «olvido aproximado con residuo medido». Es la acción 2 que este pase deja escrita.

    ⚠️ **Y la razón por la que vale la pena construirlo ahora, que es nueva en este pase:** **P-MIA** mide que el **dashboard de mastery** —el artefacto que esta KB propone como entregable— **es la superficie de ataque**, porque los vectores de estado de conocimiento se pueden revertir desde las visualizaciones de radar. Ver la tendencia **50**. Sin métrica de verificación, un *unlearning* sobre `pyKT` es una promesa; con las métricas de OpenUnlearning, es un número.


35. **Ningún benchmark pedagógico está empaquetado como prueba de conformidad, y ninguna herramienta de conformidad tiene cobertura educativa** *(agregado en el pase 20 del 2026-10-01)*. **Es el gap más construible y de mayor valor comercial de esta KB**, y es de naturaleza distinta a todos los demás: no espera que nadie publique nada.

    **Las dos mitades existen, están maduras, y son licencia-compatibles.** Del lado de la **herramienta**: `inspect_ai` (**MIT**, 2.900 ★, UK AI Security Institute), `moonshot` (**Apache-2.0**, 353 ★, AI Verify Foundation / IMDA Singapur), `compl-ai` (**Apache-2.0**, 211 ★, ETH Zürich + INSAIT + LatticeFlow, **29 benchmarks mapeados a los 6 principios del EU AI Act**), más los puntos de extensión: `moonshot-data` (**Apache-2.0**, datasets y *cookbooks*) y `aiverify-developer-tools` (**Apache-2.0**, plugins de test propios). Del lado del **benchmark pedagógico**, ya en esta KB desde el pase 4: `EduBench` (**MIT**, ACL 2026), `SafeTutors` (**MIT**), `MathTutorBench` (CC BY 4.0, EMNLP 2025 Oral), `UnifyingAITutorEvaluation` (CC BY-SA 4.0, NAACL 2025), `AITutor-EvalKit` (**MIT**).

    **La ausencia está declarada por los propios catálogos, no inferida de una búsqueda** — y eso es lo que la vuelve citable: `LLM-Evals-Catalogue` (AI Verify Foundation, 23 ★, ⚠️ sin licencia declarada) publica su categoría *domain-specific* con **derecho, medicina y finanzas** y **educación no figura**; `compl-ai` mapea 29 benchmarks al AI Act **sin una mención de educación**, aunque el **Anexo III del propio AI Act nombra la educación como alto riesgo de forma textual**; y `awesome-eu-ai-act` (**CC0**, 21 ★) lista once herramientas de conformidad open source y **ninguna del sector educativo**.

    **Por qué es distinto de los gaps 31 y 34:** ésos esperan que un grupo de investigación libere código. **Éste se cierra con trabajo de integración sobre repos que ya están verificados en esta KB** — empaquetar `EduBench` y `SafeTutors` como *recipe* de Moonshot y como benchmark mapeado de `compl-ai`. **No es investigación: es empaquetado.** Y habilita exactamente el expediente que esta KB ya vende en cinco patrones (**P4**, **P10**, **P11**, **P17**, **P39**). Ver **P42**.

    **La acción escrita, para el pase que la ejecute:** las dos puntas son MIT y Apache-2.0, así que la contribución puede ir **hacia arriba** —a repos de un regulador nacional y de ETH Zürich—, lo que convierte un entregable de cliente en posicionamiento público. ⚠️ **Y los cuatro límites que no hay que cruzar:** ninguna de estas herramientas **certifica** (`aiverify` declara por escrito que no garantiza ausencia de riesgo o sesgo); el marco de Singapur es **voluntario** y el europeo no; **no hay crosswalk directo de AI Verify al EU AI Act** (sólo a **NIST AI RMF**, oct-2023, y a **ISO/IEC 42001:2023**, jun-2024 — al AI Act se llega indirecto por ISO 42001); y `aiverify` evalúa **modelos supervisados tabulares y de imagen, no agentes**.


40. ~~**El cartucho MCP de CaSS está declarado, no medido.**~~ → 🟢 **GAP CERRADO EN EL PASE 26 DEL 2026-10-01, y cerrado ejecutando.** El pase 25 lo abrió porque toda la tendencia 65 y el paso 4 de **P48** descansaban en una línea del README de CaSS entre sus *pluggable cartridges*. **Este pase corrió el generador.** No se levantó el servidor —necesita Elasticsearch y en este entorno **no hay demonio de Docker**: el CLI está, `/var/run/docker.sock` no existe— sino por donde la arquitectura del proyecto lo permite: las tools se generan con `generateTools(spec)` sobre el OpenAPI que `swagger-jsdoc` arma desde los comentarios del código, **y eso es puro y corre sin base de datos**. Se replicaron las opciones exactas de `src/main/server.js`, se validó el spec con el mismo `openapi-schema-validator` del arranque y se ejecutó el generador real del repo.

    **Medido: 51 paths, 0 errores de validación, 6 tools, 3 resource templates.** `server_status` (`GET /api/ping`), `search_data` (`GET /api/data/`), `get_object` (`GET /api/data/{uid}`), `save_object` (`POST /api/data/{uid}`), **`record_evidence`** (`POST /api/xapi/statement`) y **`get_learner_profile`** (`GET /api/profile/latest`). Resource templates: `CaSS JSON-LD Object`, `… (Versioned)`, `… by UID`. Tabla completa con parámetros y `annotations` en `agents/top.md`.

    **Las dos últimas son las que importan: entrar evidencia xAPI y sacar perfil de competencia, por MCP, bajo Apache-2.0** — los dos pasos exactos que **P48** tenía inferidos. Ver la tendencia **66** y el patrón **P50**.

    ⚠️ **Lo que esta medición no es, dicho con precisión:** se midió la **generación** de las tools, determinista y pura sobre el spec, **no su invocación**, que necesita Elasticsearch. Las 13 aserciones de `5.mcp.json-schema-to-zod.test.js` pasan **13/13**; `5.mcp.openapi-to-tools.test.js` **no corre tal cual** porque su `before` hace `fetch` a `localhost:80/api/swagger.json`. El conteo de **6** coincide con lo que ese test afirma literalmente (*«generates exactly 6 tools from the current spec»*) y con las **6** anotaciones `x-mcp-tool-name` del árbol: **tres fuentes independientes dan 6.** El *handshake* MCP real queda como acción del pase 27.

41. **Por MCP, CaSS escribe un statement por llamada: la superficie está curada y el *bulk* queda afuera a propósito** *(agregado en el pase 26 del 2026-10-01)*. De los **51 paths** del spec el cartucho expone **6**, y no por inmadurez: hay **45 `x-mcp-ignore: true`** puestos **uno por uno** en el código, con `x-mcp-tool-name` y `x-mcp-description` escritos a mano en los seis que salen. Lo excluido incluye **`POST /api/xapi/statements`** (el *bulk* del LRS), `GET /api/xapi/endpoint`, el `multiPut`/`multiGet`/`multiDelete` de skyRepo y **todo `skyId`**. **Consecuencia de cotización, y es la que importa:** quien presupueste **ingestión masiva de telemetría por la puerta MCP** está cotizando mal — por ahí entra **un statement por llamada**. Para lotes hay que ir a la API REST por fuera de MCP. **No es un defecto: es una decisión de diseño que conviene citar como tal**, porque muestra que el proyecto pensó la superficie de agente en vez de volcar su API.

42. **No existe implementación *platform-side* (lado LMS) de LTI 1.3 que sea permisiva *y* productiva** *(agregado en el pase 26 del 2026-10-01, medido sobre seis candidatos)*. El pase 24 lo sospechó con dos piezas; este pase lo midió con seis. **`ltijs` (Apache-2.0, 5.9.9) exporta `[ 'Provider' ]` y nada más** —sin clase de *platform*— y su `package.json` dice *«turn your web application into a LTI 1.3 **Learning Tool**»*: **tool-side, medido, no leído**. `macewan-cs/lti` (**MIT**, 8 ★) resultó **tool-side** también, contra lo que sugería el resumen de búsqueda. Las dos permisivas del lado plataforma se autodenominan **«Sample»** (`LtiLibrary/LtiAdvantagePlatform`, MIT) y **«example»** (`Citolab/lti-1p3-platform-example`, **GPL-3.0+**). La única **completa y certificada por 1EdTech** es `oat-sa/lib-lti1p3-core`, **GPL-2.0**. Y `UOC/java-lti-1.3-platform` **no declara licencia** y habla en futuro.

    **La salida para un engagement, y son tres, ninguna gratis:** aceptar **GPL-2.0** (TAO, certificada); integrarse **como *tool*** contra el LMS que el cliente ya tiene —donde esta KB sí es fuerte: `ltijs` + `canvas-mcp`—; o presupuestar el lado plataforma **como desarrollo, no como integración**. ⛔ **La verificación del *launch* OIDC de punta a punta sigue pendiente y está bloqueada por el entorno:** `LtiAdvantagePlatform` es **ASP.NET Core 10**, acá **no hay `dotnet`** y no se puede instalar — `https://dot.net/v1/dotnet-install.sh` responde **`CONNECT tunnel failed, 403`** por el proxy.

43. **Moodle es el LMS más instalado del planeta y su único conector MCP es AGPL-3.0 con las partes útiles cerradas** *(agregado en el pase 26 del 2026-10-01)*. `csmediapro/moodle-mcp-server` es **AGPL-3.0**, **0 ★, 0 forks**, 57 commits. Sus **10 tools abiertos son sólo de lectura** (`list_courses`, `get_course`, `list_course_users`, `list_assignments`, `list_categories`, `get_site_info`, `get_user`, `list_user_courses`, `search_users`, `search_courses_by_name`) y las capas que un cliente pediría —*Advanced Reporting*, *User Analytics*, *User Directory*, *Compliance Pack*— son **plugins premium que se venden aparte**. 🔴 **El resumen de búsqueda lo presentaba como «open-source, plugin-extensible, LLM-agnostic» con instalación por `npx`:** la licencia y el modelo comercial sólo aparecen leyendo la página. **Es hueco de oportunidad, no sólo de inventario** — existe `canvas-mcp` (MIT, 269 ★, 102+ tools) para Canvas y **nada equivalente para Moodle**. Ver el patrón **P51**.

44. **El eje conector tiene dos estándares vacíos y uno con colisión de término** *(agregado en el pase 26 del 2026-10-01)*. Cruzando `MCP server` con cada estándar inventariado: **xAPI** ✅ (`learnmcp-xapi`, ya estaba), **LTI** ✅ (vía conectores de LMS), **OneRoster** 🔴 **nada**, **QTI** 🔴 nada verificable —apareció un *Question Bank MCP Server* listado en Glama **sin repo de GitHub localizable, y no se registra como hallazgo**—, **CASE** 🔴 nada **y con el término capturado**: la búsqueda se llena de *certificaciones* de MCP (MCPA de Linux Foundation, certs de Claude). **Es la segunda colisión de término que mide esta KB**, después de `education` = «cursos sobre AI» (pase 23). **Regla de método que deja: antes de concluir que una capa está vacía, verificar que la palabra no esté capturada por otro mercado.** Con `education` costó siete pases descubrirlo.

45. **La vertical biblioteca no tiene ninguna pieza agéntica, y es la que tiene el bus de eventos servido** *(agregado en el pase 26 del 2026-10-01)*. Se abrió la capa biblioteca/ILS y **tiene opción permisiva y grande** —**FOLIO**, Apache-2.0, 3.096 commits en `platform-complete`, **multi-tenant, modular y con Kafka** en `mod-inventory`— pero **no existe conector MCP ni agente** ni para FOLIO ni para Koha (GPL-3.0+). **FOLIO es el candidato más obvio de toda esta KB para construir uno**, porque ya publica eventos en Kafka: el agente se engancha como consumidor **sin parchear el core**. Ver el patrón **P52**.

46. **No hay plataforma de admisiones open source permisiva y productiva** *(agregado en el pase 26 del 2026-10-01)*. Lo que sirve es copyleft y ya estaba en esta KB: **OpenEduCat** (**LGPL-3.0**, pipeline completo de consulta → solicitud → verificación documental → entrevista → oferta → alta en SIS, sin fee por postulante) y `OS4ED/openSIS-Classic` (**GPL**). Lo único permisivo verificado es `CollinsTatang/admissionSystem` (**MIT**, **4 commits**, 6 ★, 0 forks, PHP/MySQL): no es base de producción, y el conteo de commits lo dice solo. ⚠️ **Y un no-hallazgo declarado:** el barrido ofreció `WalaEddine01/OrgSchool-portfolio-project` como *«Open Source Software about student Management System»* y **verificado da 404** — **no se registra**, porque un 404 no es un hallazgo. **La salida practicable es LGPL-3.0 sobre OpenEduCat**, y para un módulo Odoo es manejable porque **la LGPL admite el módulo propietario al lado**; la alternativa es desarrollo.

47. **La capa de *student success* open source es de 2013–2014, es GPL, no vive en GitHub — y es la que el regulador aprieta más** *(agregado en el pase 26 del 2026-10-01)*. **FlightPath Academics** (asesoría académica, *degree audit*, ***early alerts***, *Academic Priority*) es **PHP, GPLv3+**, liberada el **2013-03-13** por la University of Louisiana at Monroe, y **no tiene repositorio en GitHub** (el 404 de `Cerebro-Tech/FlightPath` es de WebFetch). **Student Success Plan** (Unicon) y el *dashboard* de **Marist College** tienen referencias verificables sólo de **2013–2014**. 🔴 **Es la capa más vieja y peor abastecida de las veintiséis pasadas** — y simultáneamente la que concentra más presión regulatoria, porque *predecir qué alumno va a fracasar* es exactamente la decisión automatizada sobre el alumno que el **Annex III** clasifica de alto riesgo y que **Oklahoma y Maryland** prohíben tomar de forma autónoma. **Hueco de mercado grande y riesgo alto en la misma celda.** Ver la tendencia **68** y el patrón **P53**.

## 54. El almacén permisivo que esta KB recomienda sabe borrar al alumno desde antes de que esta KB existiera, y seis pasadas vendieron lo contrario por leer documentación en vez de código (agregado 2026-10-01, pase 21)

**Ésta no es una tendencia del mercado: es una corrección de esta KB, y se registra como tendencia porque cambia el
argumento de venta de tres patrones y de dos regiones.**

Desde el pase 6, esta KB sostiene que la cadena de supresión del dato del alumno **se rompe en la telemetría**. Sobre
esa afirmación construyó la tendencia **49**, el **gap 33**, el patrón **P40**, media argumentación de EMEA y la
contraparte LATAM en `intel/market.md`. El pase 19 la midió del lado de Moodle y dejó escrita la acción:
*«Confirmar la API de borrado de Learning Locker (gap 33). Es la pregunta de mayor rendimiento del pase.»* El pase 20
no la tomó. **El pase 21 la ejecutó, y la afirmación es falsa.**

**Lo que hay, leído en el código fuente de los tres LRS:**

| LRS | ¿Borra? | Granularidad | Dónde está |
|---|---|---|---|
| **`lrsql`** (**Apache-2.0**) | ✅ **Sí, y es el mejor primitivo de la capa** | **por `actor-ifi`** — la identidad xAPI del alumno | `DELETE /admin/agents` → `delete-actor-and-dependents!` |
| **Learning Locker** (GPL-3.0) | ✅ Sí | por **filtro** de statements | `POST /api/v2/batchdelete/initialise` + worker paginado |
| **Ralph** (MIT) | ⚠️ No en la API del LRS | por **ID de statement** | `write(operation_type=DELETE)` en el *data backend* |

**El primitivo de `lrsql` es exactamente la forma del art. 17.** Recibe **un solo parámetro** y borra en cascada,
dentro de una transacción, de **siete tablas** —`statement_to_statement`, `statement_to_activity`, `attachment`,
`xapi_statement`, `agent_profile_document`, `state_document`, `actor`—. Y la octava, `statement_to_actor`, que es la
que **contiene el IFI del alumno junto a cada statement**, se borra por una **`ON DELETE CASCADE`** que una migración
con guarda agrega a propósito, con el comentario del mantenedor explicando para qué. **Alguien pensó este caso y lo
cerró**, años antes de que esta KB declarara que no existía.

⚠️ **Y viene apagado de fábrica:** `LRSQL_ENABLE_ADMIN_DELETE_ACTOR` es **`false`** por default en la configuración de
producción, y la ruta **no se registra** con el flag apagado. **Eso no es un desarrollo: es una variable de entorno.**

**Por qué esto es una tendencia y no una errata.** El error no estuvo en la búsqueda: estuvo en **confundir el silencio
de la documentación con la ausencia de la capacidad** — y esta KB lo tenía anotado. La nota de límite al pie de la
tabla del gap 33 decía, textual, que el «no» era *«ausencia en la documentación publicada, no una prueba de que la
operación sea imposible»*. **La nota tenía razón y nadie la ejecutó durante catorce pasadas.** El costo no fue un repo
que faltaba en una tabla: fue **venderle a un cliente la ausencia de una capacidad que el producto recomendado ya
tenía**, y cobrarle como alcance propio una intervención de almacén que son dos líneas de configuración.

**La regla que queda, y es la quinta de la serie de método de esta KB:** pase 5 — buscar la pieza, no la categoría;
pase 7 — la palabra del mercado, no la del paper; pase 8 — por quién es el alumno; pase 9 — el final del recorrido;
**pase 21 — leer el código, no la documentación. Un gap declarado sobre documentación no es un gap: es una tarea de
lectura pendiente, y hay que marcarla como tal para que no se cotice como ausencia.**

**Lo que esto no arregla, y es lo que queda vendible.** El borrado existe; **la evidencia y el disparador no.** Ningún
LRS de los tres emite evento de finalización, y `lrsql` **no devuelve ni el conteo de lo borrado** (**gap 36**). Y
arriba de los tres, **xAPI / IEEE 9274.1.1 sigue sin definir supresión**: todo esto es extensión propia de cada
implementación, **no portable**. Ver **P44**, y la corrección completa en `repos/foundations.md`.


## 55. El agujero de la cadena de borrado no está en el almacén: está en el enlace LMS → LRS, y lo documenta por escrito un LMS europeo de primera mano (agregado 2026-10-01, pase 21)

Con la tendencia 54, el diagnóstico de la cadena de supresión se reordena entero, y **el hueco se corre un eslabón**:

```
LMS (Moodle, Open edX, ILIAS)     LRS (lrsql, Learning Locker)     Modelo (pyKT / mastery)
   ✅ aprueba y ejecuta      ──?──▶   ✅ sabe borrar por actor    ──?──▶   🚫 gap 34
   el borrado del registro          (pase 21: existe y funciona)         (unlearning sin
   (pase 19: Privacy API)                                                 benchmark educativo)
                                 ▲
                      🔴 ACÁ está el agujero: no hay disparador,
                         no hay evento, y no es un problema de
                         capacidad sino de integración
```

**Lo nuevo de este pase es que el eslabón faltante está documentado por una de las partes.** El Feature Wiki de
**ILIAS** —LMS GPL-3.0 de referencia en DACH, 506 ★, 426 forks, rama `release_11` con **76.385 commits**— dice que al
borrar un objeto xAPI/cmi5 **el dato personal de los *statements* persiste en el LRS**, que una vez comunicado el dato
al LRS **ILIAS no tiene control sobre su borrado**, y que **no hay forma de borrar datos del LRS desde ILIAS**.

**Por qué vale más que un hallazgo de repo.** Hasta ahora el gap de propagación era **inferencia de esta KB**: el pase
19 lo midió en el árbol de Moodle y no encontró evento. Ahora hay **un segundo LMS, independiente, que lo declara por
escrito en su propia documentación de producto**. Dos implementaciones distintas, misma conclusión, y una de las dos
la publica como limitación conocida. **Eso convierte P40 de hipótesis técnica en limitación reconocida por el
proveedor** — que es exactamente lo que se necesita para ponerlo en el alcance de una propuesta sin que suene a
invento.

**Y hay una segunda mitad, puramente técnica, que decide arquitecturas antes de escribirlas.** En **Ralph** el borrado
no depende del LRS sino **del backend de datos elegido**: Mongo y Elasticsearch lo soportan, y
🔴 **ClickHouse lo declara explícitamente no soportado**, junto con `APPEND` y `UPDATE`. ClickHouse es el backend que
se elige **para analítica de aprendizaje a escala**. O sea: **el backend que se elige por performance es el que vuelve
imposible el art. 17**, y la decisión se toma al principio del proyecto, cuando nadie está mirando el GDPR.

⚠️ **Límite de verificación:** `docu.ilias.de` **está bloqueado por el proxy de egreso** de esta sesión. Lo de ILIAS
viene de **resultados de búsqueda sobre su Feature Wiki**, no de la página abierta; el repo sí se verificó de primera
mano vía WebFetch. **Antes de citar la limitación de ILIAS ante un cliente hay que abrir el wiki.** Lo de Ralph,
Learning Locker y `lrsql` está leído en el código y no tiene esa marca.


## 56. «No archivado» no es «mantenido»: el LRS más instalado del sector tiene cinco años sin un commit y se presenta como producto vivo (agregado 2026-10-01, pase 21)

**Learning Locker** es, según esta KB desde el pase 6, *«el LRS más adoptado de la categoría»*. Su repositorio
**no está archivado**, no tiene aviso de fin de vida, su README describe *«The Open Source Learning Record Store.
Started in 2014»* y remite a la oferta **comunitaria y comercial de Learning Pool** (585 ★, 294 forks, GPL-3.0,
verificado vía WebFetch el 2026-10-01).

**Y `git log` dice que el código no se mueve desde el 2021-11-16.** `HEAD` coincide exactamente con el tag **v7.1.1**,
el último publicado. Son **casi cinco años** — y en esos cinco años pasaron el art. 17 aplicado a EdTech, la COPPA
enmendada, el EU AI Act, AB 1159 y el incidente de Canvas.

**Las dos cosas son verdad al mismo tiempo y hay que decirlas juntas:** la API de borrado de Learning Locker
**existe, es correcta y este pase la verificó línea por línea**; y el software que la implementa **no recibe
mantenimiento**. Un cliente que ya lo tiene instalado —que es el caso más probable, por eso está en esta KB— tiene la
capacidad de cumplir el art. 17 y **no tiene a quién reportarle un bug de seguridad**.

**La regla, que es la contracara de la del pase 8.** Ahí la lección fue *leer el archivo `LICENSE`, no el badge*,
porque el badge mentía. **Acá es: leer el `git log`, no el banner de archivado.** GitHub marca «archivado» sólo cuando
el mantenedor decide marcarlo, y **el abandono silencioso no tiene insignia**. Para toda pieza que esta KB proponga
como **infraestructura instalada** —no como librería que se copia— la fecha del último commit es un dato de
elegibilidad, no un detalle de color. Es el mismo problema que el pase 12 encontró con `Continue` archivado y el pase
9 con las tres implementaciones de referencia de credenciales retiradas, pero **invertido**: ahí el proyecto avisó;
acá no.

36. **El borrado del LRS permisivo no deja evidencia de haber ocurrido** *(agregado en el pase 21 del 2026-10-01)*. Es lo que queda del gap 33 después de refutarlo, y es **el gap más chico, más concreto y más upstreameable que tuvo esta KB en veintiún pasadas.**

    **El hallazgo, leído en el código.** `lrsql` borra de forma completa y atómica — y **no devuelve ni registra nada sobre lo que borró**. El SQL `delete-actor-and-dependents!` está declarado `-- :result :affected`, así que **el conteo de filas afectadas se calcula y se descarta**; el interceptor responde `{:status 200 :body params}`, que es **el `actor-ifi` que mandó el cliente**. No hay registro de auditoría, no hay evento, no hay conteo. Learning Locker está un escalón mejor —expone `total`, `deleteCount`, `processing` y `done` para **sondear**— pero tampoco notifica, y 🔴 **su `done:true` no significa «borrado»**: tres caminos de error marcan el job terminado con `deleteCount` en `null`.

    **Por qué importa comercialmente, y es la parte que no es técnica.** El art. 17 del GDPR, **AB 1159** (California, operativa el **2027-07-01**) y la Ley 21.719 chilena no piden borrar: piden **poder demostrar que se borró**. Con `lrsql` tal como viene, la única prueba de una supresión es **un `200` con el input del propio pedido adentro**. Eso no es un expediente: es un recibo que el cliente se escribió a sí mismo.

    **Por qué es distinto de los gaps 31, 34 y 35.** Los gaps 31 y 34 esperan que un grupo de investigación libere código; el 35 es empaquetado de dos mitades que existen. **Éste es un parche de pocas líneas sobre un repo Apache-2.0**: el dato ya está calculado en la capa SQL y se tira. **No requiere investigación, no requiere ensamblado, y se contribuye hacia arriba** — a Yet Analytics, con lo que un entregable de cliente se convierte en posicionamiento público, igual que el camino que el pase 20 identificó para el gap 35. Ver **P44**.

    ⚠️ **Y los dos límites de alcance, para no venderlo más grande de lo que es.** Primero: devolver el conteo **no** resuelve el disparador LMS→LRS, que sigue siendo integración (**P40**). Segundo: el conteo de filas afectadas **no es** una prueba criptográfica de borrado — es telemetría de la operación. Para un régimen de alto riesgo hay que combinarlo con el registro del pedido en el LMS (`tool_dataprivacy`, pase 19) y con el expediente de **P35**.

## 57. La capa de analítica del LMS open source más desplegado es permisiva mientras su núcleo es AGPL — y trae el LRS puesto, así que la «elección de arquitectura» que esta KB suponía no existe (agregado 2026-10-01, pase 22)

**El dato.** **Aspects** (`openedx/tutor-contrib-aspects`, **Apache-2.0**, 14 ★, 32 forks, **2.269 commits**) es el
plugin de analítica y reporting **oficial** de Open edX, e instala vía Tutor un stack entero: **ClickHouse** +
**Apache Superset** + **Ralph** (el LRS) + **Vector** + **event-routing-backends** (xAPI) + **dbt**. Su complemento del
lado LMS/Studio, `openedx/platform-plugin-aspects` (**Apache-2.0**, 528 commits), empuja el dato a ClickHouse y
**embebe dashboards de Superset dentro de la interfaz del docente**.

**Por qué es tendencia y no una ficha de repo.** Dos cosas, y las dos cambian decisiones:

1. **El arbitraje de licencia se repite por tercera vez en esta KB.** Open edX es **AGPL-3.0** —el peor caso para
   SaaS—, pero **la capa que un estudio efectivamente customiza es Apache-2.0**. Es la misma forma que el pase 14
   encontró en la capa curricular y el pase 20 en la de conformidad: **lo que se toca es permisivo, lo copyleft es el
   sustrato que no se forkea.** Ya no es una casualidad: es el patrón de cómo se gobierna el open source educativo
   maduro —núcleo protegido, periferia abierta— y es a favor de quien construye.
2. **Para Open edX, el LRS no es una decisión.** Hasta el pase 21 esta KB razonaba el almacén como elección de
   arquitectura (`lrsql` para producción permisiva, Ralph para Open edX). **Si hay analítica oficial y trae el LRS
   puesto, el cliente no eligió: hereda.** Y hereda, específicamente, la configuración que el pase 21 declaró
   imposible de borrar. **El discovery tiene que preguntar qué stack de analítica corre, no qué LRS eligieron.**

⚠️ **Las estrellas de esta capa no miden nada** (14 y 6) y no hay que leerlas como tracción: es infraestructura de
plataforma, no un proyecto que compite por atención. La señal son los commits y la organización que publica.

## 58. Los dos LMS open source grandes divergen en la plomería del art. 17: en Moodle el disparador de supresión no existe, en Open edX es una señal del framework con listener permisivo (agregado 2026-10-01, pase 22)

**El dato, medido en los dos lados y en dos pases distintos:**

| | Moodle | Open edX |
|---|---|---|
| ¿Emite evento al aprobar/ejecutar una supresión? | 🚫 **No.** Pase 19: **187 archivos** de `tool_dataprivacy`, **cero** `trigger()`. `api::update_request_status()` es una escritura de base y nada más | ✅ **Sí.** Señal Django **`USER_RETIRE_LMS_MISC`** |
| ¿Hay listener que propague a la telemetría? | 🚫 No en el núcleo. El único antecedente (`local_gdpr_deleteuserdata`, GPL-3.0) **es de 2018 y pide Moodle 3.5** contra un núcleo en 5.3 | ✅ **`UserRetirementSink`** en `platform-plugin-aspects`, **Apache-2.0**, que borra la PII del usuario de ClickHouse |
| Cómo se construye el puente | **Sondeo** de `tool_dataprivacy_request.status` — la única superficie observable | **Ya construido.** Configuración y verificación |

**Por qué importa más que como detalle técnico.** Esta KB venía diciendo, desde el pase 19 y en **P40**, que el
disparador LMS → telemetría **no existe**. Dicho así es falso: **no existe en Moodle.** En Open edX existe, está en el
núcleo del ecosistema oficial y es permisivo. Consecuencias comerciales directas:

- **La elección de LMS del cliente ahora tiene una consecuencia de cumplimiento medible**, y es un argumento que se
  puede poner sobre la mesa en una evaluación de plataforma. No es preferencia: es cuánto cuesta el expediente del
  art. 17 sobre cada una.
- **Para un proyecto Moodle, el diseño ya no hay que inventarlo:** el `UserRetirementSink` es la implementación de
  referencia, permisiva y en producción, del extremo que recibe.

⚠️ **Y la simetría no es completa, así que no hay que venderla como tal:** el sink de Open edX borra **PII**, no el
registro de eventos. Ver la tendencia 59.

## 59. «Anonimizado» se está volviendo el argumento de retención por default: borrar el nombre y conservar la conducta, y ya son dos plataformas que lo documentan por escrito (agregado 2026-10-01, pase 22)

**El dato.** Ante un pedido de supresión, el stack oficial de Open edX borra las tablas de **PII**
(`user_profile`, `external_id`, `auth_user`, gobernadas por el flag `ASPECTS_ENABLE_PII`) y **conserva el dato de
eventos del usuario retirado**, con el argumento de que **queda anonimizado**. Y el pase 21 registró que el Feature
Wiki de **ILIAS** declara por escrito que al borrar un objeto xAPI/cmi5 el dato personal **persiste en el LRS** y que
ILIAS no tiene forma de borrarlo (tendencia **55**).

**Por qué es tendencia.** Son **dos proveedores europeos/globales de LMS que documentan el mismo límite en su propia
documentación de arquitectura**, en vez de ocultarlo. Eso tiene dos lecturas y las dos se usan:

- **A favor de una propuesta:** la carencia **no la inventa esta KB** — está escrita por el proveedor. Un argumento de
  cumplimiento que cita la decisión de arquitectura del propio producto es defendible ante un comité.
- **Como riesgo que hay que acotar:** un *statement* xAPI está indexado por un identificador de actor estable
  (`actor-ifi`). Un registro **pseudonimizado no es anónimo**, y bajo GDPR sigue siendo dato personal. **Si el
  identificador sobrevive a la retirada, «anonimizado» está haciendo un trabajo legal que puede no sostener** — y lo
  que queda retenido es el expediente conductual completo de alguien que ejerció el art. 17. Ése es el **gap 37**.

**ACTUALIZACIÓN DEL GAP 36 EN EL PASE 24 DEL 2026-10-01 — queda contestado con número, y el tamaño baja por segunda vez.**
El pase 23 lo dejó dimensionado *por lectura* y estimó *«un cambio en 4 archivos de 3 backends más el interceptor»*, porque
concluyó que en PostgreSQL y MariaDB el desglose por tabla exigía **partir el SQL**. **Se midió ejecutando, y no hace falta
partir nada:** pgjdbc y MariaDB Connector/J **parten ellos mismos** la cadena multi-sentencia y entregan **los siete
conteos, uno por tabla, en orden** (`[7, 2, 3, 8, 5, 6, 1]`) por el bucle `getMoreResults()` de JDBC estándar. El SQL no se
toca y los tres backends quedan simétricos: **lo único que hay que cambiar es la capa que recoge el resultado**, que lee un
conteo y nunca pide el siguiente.

Y aparece una trampa que el gap no tenía anotada: **el conteo único que hoy está disponible es el del PRIMER `DELETE`**, que
es el de `statement_to_statement` — **vale `0` para cualquier alumno sin sub-sentencias, que es el caso normal**. Medido: 25
filas borradas, el número disponible dice `0`. **Cablear ese conteo "porque ya está" produce un expediente que afirma algo
falso**, y eso es peor que el `200` vacío del pase 21. El gap 36 ya no es *«falta el número»*: es **«está el desglose, hay
que recogerlo entero y no confundirlo con el primero»**. Ver la tendencia **61** y el patrón **P47**.

38. **La supresión del alumno en MariaDB/MySQL cuelga de un parámetro de driver que una variable de entorno documentada apaga en silencio** *(agregado en el pase 24 del 2026-10-01)*. **Medido en este pase:** con `allowMultiQueries` en su default (`false`), `delete-actor-and-dependents!` **no se degrada, falla entera** — error **1064 / SQLState 42000** en el segundo de los siete `DELETE`. lrsql trae el parámetro, pero como *fallback* de **aero**: `:db-properties #or [#env LRSQL_DB_PROPERTIES "allowMultiQueries=true"]`, así que **cualquier** uso de `LRSQL_DB_PROPERTIES` —y `doc/postgres.md` enseña a usarla para `currentSchema`— **lo reemplaza entero y lo apaga**; `LRSQL_DB_JDBC_URL` hace lo mismo. Y `doc/env_vars.md` la describe como *«Optional **additional** DB properties»* con default *«Not set»*: **inexacto en los dos campos** para estos backends.

    **Por qué es el gap más accionable de esta KB sobre este repo, y el más barato de los siete pases que lleva mirándolo.** No hay que tocar SQL ni lógica, y no requiere investigación ni ensamblado: son **dos líneas de documentación mal escritas**, una advertencia ausente en `doc/mariadb.md`, y una decisión de diseño de configuración —**fusionar** en vez de reemplazar, o, más barato todavía y sin cambiar semántica de aero, **fallar al arrancar** cuando el backend es MariaDB/MySQL y `allowMultiQueries` no quedó activo—. Es *upstream* puro a Yet Analytics, igual que el gap 36, y se contribuye con un test de regresión que hoy no existe.

    **Y es el único gap de esta KB cuyo síntoma es la ausencia de un borrado en vez de la ausencia de su prueba.** Los gaps 36 y 37 son sobre **evidencia**; éste es sobre **capacidad**: el despliegue ingiere, consulta y pasa el *health check* con normalidad, porque el borrado de actor es la única operación del producto que manda varias sentencias en un paquete. **El fallo se manifiesta la primera vez que alguien ejerce el art. 17** — el día en que hay expediente abierto y plazo corriendo. Ver la tendencia **62** y el patrón **P47**.

    ⚠️ **Lo declarado y no verificado:** que ésa sea la *única* consulta multi-sentencia del producto no se enumeró — el clasificador de seguridad del entorno bloqueó el recorrido masivo del árbol clonado. Si una migración de arranque también lo fuera, el síntoma sería **más** visible y por lo tanto menos peligroso que lo descrito.

**La consecuencia práctica, que es de redacción de propuesta.** Sobre Open edX + Aspects la frase correcta **no es**
*«cumplimos el derecho al olvido»*; es *«se suprime la identificación directa y se conserva el registro de actividad
pseudonimizado, cuya base legal de retención se declara»*. La primera no se sostiene en una inspección; la segunda sí.
Ver **P45**.

⚠️ **Verificación declarada:** el `UserRetirementSink`, la señal y las tablas de PII están **verificados de primera
mano** (README de `platform-plugin-aspects`). La afirmación de que *el dato de eventos se conserva porque queda
anonimizado* viene de **snippets concordantes de búsqueda, no de lectura directa**: el ADR que la contiene está en
`docs.openedx.org`, **bloqueado por el proxy de egreso** en este pase, y los dos caminos alternativos probados
devolvieron 404. URL anotada para el próximo pase:
`https://docs.openedx.org/projects/openedx-aspects/en/latest/technical_documentation/decisions/0009_pii.html`.

## 60. La capacidad de probar un borrado no es portable entre bases de datos, y eso contradice la razón por la que esta KB recomienda su LRS por default (agregado 2026-10-01, pase 23)

**El pase 22 dejó escrita una sub-pregunta y declaró que no la pudo contestar** (el clasificador de seguridad del entorno
bloqueó la traza del árbol clonado): *«¿`-delete-actor` ya devuelve los conteos de filas afectadas, o hay que plomearlos
desde la capa SQL? Si ya los devuelve, el parche es una línea; si no, hay que propagarlos.»* Este pase clonó
`yetanalytics/lrsql` y leyó **los tres backends**. **La respuesta es ninguna de las dos opciones, y la diferencia es
arquitectónica, no de tamaño.**

Los conteos **ya existen en los tres backends**: toda sentencia de borrado de actor está declarada `-- :result :affected`.
Lo que no existe es **una sola forma de recogerlos**:

| Backend | Cómo está escrito el borrado | Cuántos conteos hay disponibles | Qué devuelve hoy |
|---|---|---|---|
| **SQLite** · `src/db/sqlite/lrsql/sqlite/record.clj:169–176` | **Siete queries HugSQL con nombre propio** (`delete-actor-st2st`, `-st2activ`, `-attachments`, `-statements`, `-agent-profile`, `-state-document`, `-actor`), cada una con `:result :affected` | **Siete, uno por tabla** | **Uno solo.** El cuerpo las invoca como siete expresiones sueltas en secuencia, así que Clojure **devuelve el valor de la séptima** (`delete-actor-actor`) y **descarta las otras seis** — y la séptima es la menos informativa de todas: el borrado de la fila del propio actor, que es 0 o 1 |
| **PostgreSQL** · `postgres/record.clj:135–136` | **Un único nombre HugSQL** (`delete-actor-and-dependents!`) cuyo cuerpo son **siete `DELETE` separados por `;`** bajo un solo `:command :execute` / `:result :affected` | **Uno** | Ese uno, que el interceptor igual descarta |
| **MariaDB** · `mariadb/record.clj:116–117` | Idéntico a PostgreSQL: un nombre, siete `DELETE` adentro | **Uno** | Ídem |

🔴 **Las dos consecuencias, y la segunda es la que importa comercialmente.**

**1. El parche del gap 36 no es de una línea en ningún backend, y no es el mismo parche en ninguno.** En **SQLite** es
mecánico pero no trivial: hay que envolver las siete llamadas en un `let` y devolver un mapa por tabla (~8 líneas) — el dato
ya está, sólo se está tirando. En **PostgreSQL y MariaDB** *no se puede obtener el desglose por tabla sin partir el SQL* en
siete queries con nombre, como SQLite ya las tiene: deja de ser plomería y pasa a ser **refactor del SQL**. Con eso, la
estimación honesta del gap 36 sube de *«una línea»* a **un cambio en 4 archivos de 3 backends más el interceptor**, y sigue
siendo chico y upstreameable, pero hay que presupuestarlo como tal.

**2. Y acá está el hallazgo que da vuelta un argumento de esta KB.** La fila de `lrsql` en `verticals/solutions.md` lo
recomienda como **«el default»** con esta razón textual: *«corre sobre la base de datos que el cliente ya opera, así que no
agrega una pieza de infraestructura nueva al diagrama»*. Eso sigue siendo cierto para **almacenar**. **Para *probar* un
borrado no lo es:** la evidencia disponible depende del motor que el cliente eligió por motivos que no tienen nada que ver
con privacidad. **Un despliegue sobre SQLite puede dar hoy un desglose de siete tablas con ~8 líneas; el mismo producto
sobre PostgreSQL no puede dar más de un número sin tocar el SQL.** Para un expediente del **art. 17** o de **AB 1159**
(operativa el **2027-07-01**), donde lo que se audita es la *prueba*, eso significa que **la portabilidad de base de datos
—la ventaja que vendemos— es también una asimetría de cumplimiento que hay que declarar en la propuesta.**

**La regla operativa que deja este pase:** cuando el alcance incluya evidencia de supresión, **el motor de base de datos
deja de ser una decisión de infraestructura del cliente y pasa a ser una decisión de cumplimiento del proyecto.** Hay que
preguntarlo en el *discovery*, no descubrirlo en la auditoría. Ver **P45**.

⚠️ **Verificación declarada.** Los tres `record.clj`, los tres `delete.sql`, `ops/command/statement.clj`,
`system/lrs.clj:459–463`, `admin/protocol.clj:58` y `admin/interceptors/lrs_management.clj:23–33` están **leídos de primera
mano sobre el árbol clonado** (`git clone --depth 1`, HEAD del 2026-10-01). **Lo que NO se verificó ejecutando:** qué número
devuelve exactamente el driver JDBC para un `:execute` multi-sentencia en PostgreSQL y MariaDB — si el del primer `DELETE`,
el del último o la suma. La lectura del código prueba que **hay un solo valor disponible**, que es lo que sostiene el
argumento; **cuál de los siete es ese valor no se midió y no se infiere.** Es la acción que este pase deja escrita: levantar
`lrsql` sobre PostgreSQL, borrar un actor con datos en las siete tablas y leer el valor. Es una tarde de trabajo y cierra el
gap 36 con número en vez de con lectura.

## 61. El desglose de un borrado no hay que construirlo: ya viene en el cable y se descarta — y el número que la aplicación sí puede leer es `0` para el alumno típico (agregado 2026-10-01, pase 24)

**El pase 23 dejó escrita una acción concreta y acotada:** *«levantar `lrsql` sobre PostgreSQL, borrar un actor con datos en
las siete tablas y leer el valor. Es una tarde de trabajo y cierra el gap 36 con número en vez de con lectura.»*
**Se ejecutó en este pase, y el resultado corrige la conclusión arquitectónica del pase 23, no la confirma.**

### Cómo se midió (y por qué el fixture está armado así)

| | |
|---|---|
| **Árbol** | `yetanalytics/lrsql` clonado, HEAD `cb794e4` |
| **Esquema** | Las tablas creadas **con el DDL propio de lrsql**, extraído de `src/db/postgres/lrsql/postgres/sql/ddl.sql` — no un esquema equivalente escrito a mano |
| **Migración aplicada** | `add-statement-to-actor-cascading-delete!`, así que el fixture es un despliegue **migrado**, como el de producción. Verificado en `pg_constraint`: `statement_fk … REFERENCES xapi_statement(statement_id) ON DELETE CASCADE` |
| **SQL bajo prueba** | El cuerpo literal de `delete-actor-and-dependents!` de `delete.sql`, con `:actor-ifi` sustituido por `?` — **las 8 ocurrencias**, que es lo que emite HugSQL |
| **Motor y driver** | PostgreSQL **16.14** + **pgjdbc 42.7.4**; y MariaDB **10.11.14** + **Connector/J 3.4.1** |
| **El truco del fixture** | Se sembró un conteo **distinto por tabla** (7, 2, 3, 8, 5, 6, 1) para que el número que vuelve sea **identificable**: primero=7, último=1, suma=32, máximo=8, todos distintos entre sí |

### Lo que devolvió, medido

```
MODE=prepared  execute()->hasResultSet=false
  getUpdateCount() INMEDIATAMENTE DESPUÉS de execute()  = 7
  TODOS los conteos vía el bucle getMoreResults()        = [7, 2, 3, 8, 5, 6, 1]
  first=7  last=1  sum=32  max=8
MODE=executeUpdate  returned = 7
```

🔴 **Hallazgo 1 — y corrige al pase 23.** El pase 23 escribió que en PostgreSQL y MariaDB *«no se puede obtener el desglose
por tabla sin partir el SQL»*, y que por eso el gap 36 *«deja de ser plomería y pasa a ser refactor del SQL»*.
**Es falso, y se mide arriba:** pgjdbc **parte él mismo** la cadena multi-sentencia y expone **los siete conteos, uno por
tabla, en el orden de los siete `DELETE`**, a través del bucle `getMoreResults()` que es JDBC estándar desde 1997.
**El desglose por tabla ya viaja por el cable.** Lo mismo, idéntico, en MariaDB con `allowMultiQueries=true`:
`[7, 2, 3, 8, 5, 6, 1]`.

**Entonces el gap 36 vuelve a bajar de tamaño, y por segunda vez.** No es un refactor del SQL ni hay que partir
`delete-actor-and-dependents!` en siete queries con nombre: lo que hay que cambiar es **la capa que recoge el resultado**,
que lee un conteo y nunca pide el siguiente. El SQL no se toca y los tres backends quedan simétricos.

🔴 **Hallazgo 2, y es el que hay que llevar a la reunión.** El único número que hoy queda disponible —el que
`getUpdateCount()` devuelve, y el mismo que devuelve `executeUpdate()`— **es el del PRIMER `DELETE`**, no el del último
ni la suma. Y el primer `DELETE` de la secuencia es el de **`statement_to_statement`**: la tabla de aristas entre
sentencias, que **sólo tiene filas si las sentencias del alumno tienen anidamiento o *voiding***.

**Para el alumno corriente, que no tiene sub-sentencias, ese número es `0`.** Medido, borrando el mismo actor con el
fixture sin filas en `statement_to_statement`:

```
  getUpdateCount() INMEDIATAMENTE DESPUÉS de execute()  = 0
  TODOS los conteos vía el bucle getMoreResults()        = [0, 2, 3, 8, 5, 6, 1]
  first=0  last=1  sum=25  max=8
```

**Veinticinco filas borradas, y el único testigo disponible dice `0`.** Esto cambia el consejo del pase 23 en un punto
que importa: **el parche del gap 36 hecho de la manera obvia —cablear el conteo que ya está— produce un expediente que
afirma «0 filas borradas» sobre una supresión exitosa.** Un oficial de privacidad que lea eso concluye, con razón, que
no se borró nada. **Un número incorrecto es peor que el `200` vacío que el pase 21 denunció**, porque el `200` vacío no
afirma nada y el `0` afirma algo falso. El parche correcto es el bucle completo, no el conteo único.

### Hallazgo 3 — la tabla que une a la persona con su rastro no se borra nunca de forma explícita, y por eso no aparece en ningún conteo

Los siete `DELETE` **no incluyen `statement_to_actor`**, que es justamente la tabla que vincula al alumno con sus
sentencias. Las cuatro primeras sentencias **la leen** en subconsultas, pero nadie la borra. Sus filas desaparecen
**sólo por `ON DELETE CASCADE`** desde `xapi_statement`, y **las filas borradas en cascada no se cuentan en ningún
*update count* de JDBC**. En el fixture eran **10 filas** (8 del alumno y 2 del docente que aparecía en las mismas
sentencias) y **ninguna de las dos mediciones las ve**.

Y el camino por el que existe esa cascada **no es el mismo en los dos motores**, lo que importa para auditar un
despliegue ajeno:

| Motor | Cómo llega la cascada | Consecuencia operativa |
|---|---|---|
| **MariaDB** | **Nativa en la definición de la tabla** (`statement_fk_stactor`, verificado `CASCADE` en `information_schema.referential_constraints`) | Está desde la creación del esquema |
| **PostgreSQL** | **Por migración**: `add-statement-to-actor-cascading-delete!`, condicionada por `check-statement-to-actor-cascading-delete` | **Depende de que `-update-all!` haya corrido.** En un despliegue viejo sin migrar, la cascada no está |

**La regla operativa:** incluso con el bucle completo de siete conteos, **el expediente sigue subdeclarando el borrado**,
porque la tabla de vínculo se va en silencio. Un expediente honesto tiene que contar las filas en cascada aparte —con un
`SELECT` previo— o decir explícitamente que no las cuenta. Ver **P47**.

⚠️ **Verificación declarada.** Todo lo de arriba está **ejecutado en este pase**, no leído: PostgreSQL 16.14 y MariaDB
10.11.14 levantados localmente, esquema creado con el DDL de lrsql, los conteos impresos por un arnés JDBC propio sobre
los drivers oficiales. **Lo que NO se midió:** (1) el valor que entrega `next.jdbc` con `:result :affected` *dentro* de
lrsql —el repositorio de artefactos Clojure (`repo.clojars.org`) responde **403** a través del proxy de egreso de esta
sesión, así que no se pudo resolver `next.jdbc` ni el adaptador de HugSQL y **la cadena se midió a la altura del driver,
que es donde estaba la pregunta abierta**; la lectura del pase 23 sobre el interceptor que descarta el valor sigue en
pie y no se repitió. (2) **Cuántas otras consultas multi-sentencia tiene lrsql**: el clasificador de seguridad del
entorno bloqueó el recorrido masivo del árbol clonado, así que el *blast radius* de la tendencia **62** queda sin
enumerar y se declara como tal.


## 62. La supresión del alumno en el LRS que esta KB recomienda depende de un parámetro de driver que una variable de entorno no relacionada apaga en silencio (agregado 2026-10-01, pase 24)

Esta tendencia **no se buscó**: salió de armar el fixture de la tendencia **61** sobre MariaDB. Es el hallazgo más
accionable del pase y el único que puede dejar una supresión del **art. 17** sin ejecutar.

### El síntoma, medido

Con el **driver en su configuración por default** —`allowMultiQueries` sin tocar, que en MariaDB Connector/J es
`false`— la consulta `delete-actor-and-dependents!` **no se degrada: falla entera**:

```
driver: MariaDB Connector/J 3.4.1   db: MariaDB 10.11.14
  SQLException: java.sql.SQLSyntaxErrorException
  message: You have an error in your SQL syntax; ... near
           'DELETE FROM statement_to_activity WHERE statement_id IN ( SELECT statement_...' at line 11
  SQLState: 42000   vendorCode: 1064
```

El servidor corta en el **segundo** `DELETE` de los siete. Con `allowMultiQueries=true` en la URL, la misma consulta
sobre el mismo esquema y los mismos datos funciona y devuelve `[7, 2, 3, 8, 5, 6, 1]`. **El parámetro es la diferencia
entre borrar y no borrar.**

### Por qué eso no es un bug de lrsql, y es peor que un bug

🔴 **lrsql sí trae el parámetro puesto — pero como *fallback*, no como base.** En
`resources/lrsql/config/prod/mariadb/database.edn:5` (y el equivalente de `mysql`), leído de primera mano:

```clojure
:db-properties #or [#env LRSQL_DB_PROPERTIES "allowMultiQueries=true"]
```

El `#or` de **aero** devuelve **el primer valor no nulo**. O sea: **si el operador define `LRSQL_DB_PROPERTIES` por
cualquier motivo, su string REEMPLAZA al default completo** y `allowMultiQueries=true` **desaparece**. No se fusiona.
No avisa. Y hay un segundo camino con el mismo efecto: `LRSQL_DB_JDBC_URL`, que —según `doc/env_vars.md`— *«overrides
the above properties if set»*, así que una URL JDBC entregada a mano también se lleva el parámetro puesto.

**Y la documentación empuja al operador exactamente hacia ahí.** `doc/env_vars.md` describe `LRSQL_DB_PROPERTIES` como
*«Optional **additional** DB properties»* con default *«Not set»*. **Las dos cosas son inexactas para MariaDB y MySQL:**
no es *additional* —es reemplazo— y el default **no** es *not set*, es `allowMultiQueries=true`. Peor: el propio
`doc/postgres.md` le enseña al lector a usar `LRSQL_DB_PROPERTIES` para fijar `currentSchema`, y `doc/mariadb.md`
**no menciona el tema en ninguna línea**. Un operador de MariaDB que quiera fijar un timeout, un `sessionVariables` o
TLS hace lo que la documentación le enseñó y **apaga la supresión del alumno sin enterarse**.

### Por qué no se nota hasta el peor momento posible

La consulta del borrado de actor es **la única operación del producto que depende de enviar varias sentencias en un
paquete**. Todo lo demás —ingesta de sentencias, consultas, documentos de estado, credenciales— es de una sentencia por
viaje y **sigue funcionando perfecto**. Así que el despliegue se ve sano: ingiere, consulta, responde, pasa el
*health check*. **El fallo aparece la primera vez que alguien ejerce el derecho al olvido**, que es, por definición, el
día en que hay un expediente abierto y un plazo corriendo.

⚠️ **El alcance exacto queda declarado, no afirmado.** Que el borrado de actor sea la *única* consulta multi-sentencia
de lrsql es lo que se desprende de las lecturas de los pases 21 a 23 y de este, **pero no se enumeró**: el clasificador
de seguridad del entorno bloqueó el recorrido masivo del árbol clonado. Si alguna migración de arranque también fuera
multi-sentencia, el síntoma sería más visible (fallaría al levantar) y por lo tanto **menos** peligroso que lo descrito.
Lo que sí está medido es que **con el default del driver, el borrado falla**, y que **lrsql no lo documenta**.

### Lo que esto cambia en la postura comercial

| | |
|---|---|
| **Lo que esta KB venía diciendo** | `lrsql` es el LRS por default porque corre sobre la base que el cliente ya opera (ver `verticals/solutions.md`) |
| **Lo que agrega el pase 23** | La *evidencia* de un borrado no es portable entre motores (tendencia **60**) |
| 🔴 **Lo que agrega este pase** | En MariaDB y MySQL, **la capacidad misma de borrar** cuelga de un parámetro de driver que una variable de entorno documentada y no relacionada apaga en silencio |

**Es, además, el *upstream* más chico y más defendible que encontró esta KB en siete pases sobre este repo:** no requiere
tocar SQL ni lógica. Son tres cosas —corregir dos líneas de `doc/env_vars.md`, advertirlo en `doc/mariadb.md`, y
**fusionar** `LRSQL_DB_PROPERTIES` con el default en vez de reemplazarlo (o, más barato y sin cambiar semántica,
**fallar al arrancar** si el backend es MariaDB/MySQL y `allowMultiQueries` no quedó activo)—. Ese es el **gap 38**.
Ver **P47**.


## Fuentes

### Pase 24 (2026-10-01) — medición propia y fuentes del barrido

**Medición de primera mano (ejecutada en este pase, no leída).** `yetanalytics/lrsql` HEAD `cb794e4`; esquema creado con el
DDL propio del proyecto (`src/db/{postgres,mariadb}/lrsql/*/sql/ddl.sql`); SQL bajo prueba: el cuerpo literal de
`delete-actor-and-dependents!` de `delete.sql` con las 8 ocurrencias de `:actor-ifi` como `?`. Motores: **PostgreSQL 16.14**
(pgjdbc **42.7.4**) y **MariaDB 10.11.14** (Connector/J **3.4.1**). Configuración leída en
`resources/lrsql/config/prod/mariadb/database.edn`, `resources/lrsql/config/prod/postgres/database.edn`,
`src/main/lrsql/system/util.clj` (`make-jdbc-url`), `doc/env_vars.md`, `doc/postgres.md`, `doc/mariadb.md`.

**Repos verificados vía WebFetch** (y no por `curl`: el proxy de egreso de esta sesión devuelve **403 a todo github.com**,
que es la advertencia del pase 12 —*un 403 de `curl` no es un 404*— y por eso la verificación de URL se hace con WebFetch,
que distingue contenido real de un 404 real): [UOC/java-lti-1.3](https://github.com/UOC/java-lti-1.3) ·
[UOC/spring-boot-lti-advantage](https://github.com/UOC/spring-boot-lti-advantage) ·
[UOC/java-lti-1.3-platform](https://github.com/UOC/java-lti-1.3-platform) ·
[UOC/java-lti-1.3-provider-example](https://github.com/UOC/java-lti-1.3-provider-example) ·
[packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) ·
[1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) (atribución a Turnitin) ·
[gnowledge/OpenAssessmentsClient](https://github.com/gnowledge/OpenAssessmentsClient) ·
[OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic). **404 confirmados:** `UOC/java-lti-1.3-provider`,
`LongsightGroup/qti3-core`.

**Barrido de mercado.** MarketsandMarkets (North America AI in education) · Technavio · azumo (compilación de estadísticas) ·
[Consejo de Europa — 2.ª conferencia de trabajo sobre regulación de AI en educación](https://coe.int/web/education) ·
QS (2026 Europe EdTech 200+) · [itnews.asia — AI sovereignty in Asia Pacific 2026](https://www.itnews.asia/news/ai-sovereignty-will-set-the-pace-for-asia-pacific-in-2026-623233) ·
[UNU/UNESCO — AI implementation in higher education in LAC](https://unu.edu/publication/ai-implementation-higher-education-latin-america-and-caribbean) ·
[BID/IADB — An Enabling Regulatory Framework for AI in LAC](https://publications.iadb.org/publications/english/document/An-Enabling-Regulatory-Framework-for-Artificial-Intelligence-in-Latin-America-and-the-Caribbean.pdf).


### Verificación del pase 23 (2026-10-01)

🟢 **Verificado de primera mano leyendo el código fuente**, con `git clone --depth 1` sobre el árbol real (no vía WebFetch,
no vía documentación): [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) — **Apache-2.0**. Leídos en este pase:
**`src/db/sqlite/lrsql/sqlite/record.clj:169–176`** (las siete llamadas secuenciales y el retorno de la séptima),
**`src/db/postgres/lrsql/postgres/record.clj:135–136`** y **`src/db/mariadb/lrsql/mariadb/record.clj:116–117`** (el nombre
único `delete-actor-and-dependents!`), los tres **`sql/delete.sql`** (siete `DELETE` en cada backend; `:result :affected`
declarado en **todas** las sentencias, y en SQLite **siete nombres HugSQL separados** frente a **uno** en Postgres/MariaDB),
`src/main/lrsql/ops/command/statement.clj:74–76` (`delete-actor!` es *pass-through* a `bp/-delete-actor!`),
`src/main/lrsql/system/lrs.clj:459–463`, `src/main/lrsql/admin/protocol.clj:58` (`-delete-actor` pertenece a
`AdminLRSManager`), `src/main/lrsql/backend/protocol.clj:42` y
`src/main/lrsql/admin/interceptors/lrs_management.clj:23–33`. **Esto contesta la sub-pregunta que el pase 22 dejó abierta y
no pudo responder** (ver tendencia **60** y **P46**).

🟢 **Verificado vía WebFetch** (licencia, estrellas, commits y lenguaje leídos en la página del repo el 2026-10-01):
[frappe/education](https://github.com/frappe/education) — **657 ★, 1.091 commits, Python, rama `develop`**; la licencia **no
aparece en la página** y se leyó en **`license.txt` (HTTP 200): «GNU GPL V3»**, aplicando la regla de método del pase 10
(verificar contra el archivo de licencia, no contra el README) · [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp)
— **MIT, 12k ★, 3.794 commits, PHP (Laravel 13 + FilamentPHP 5)**, y **sin ningún módulo educativo** entre sus plugins.

⚠️ **Nota de método, que reconfirma la del pase 12 y conviene no volver a olvidar.** `curl -sI` contra `github.com` devolvió
**HTTP 403** para los tres repos de este pase. **Un 403 del proxy de egreso no es un 404 y no invalida un repo**: los tres se
verificaron por vías más fuertes —`lrsql` **clonado**, los otros dos **leídos en la página vía WebFetch**— y
`raw.githubusercontent.com` sí responde **200**. **La regla operativa: cuando `curl` da 403, cambiar de herramienta, no
descartar el hallazgo.**

🔴 **No verificado, y declarado como tal:** cuál de los siete `DELETE` reporta el driver JDBC en el `:execute`
multi-sentencia de PostgreSQL y MariaDB (el primero, el último o la suma). **No se midió ejecutando y no se infiere.** La
lectura del código prueba que hay **un solo valor disponible**, que es lo que sostiene la tendencia 60; el valor exacto es la
acción escrita que este pase deja para el próximo. **Todo lo regulatorio de este pase viene de resultados de búsqueda** —los
134 proyectos en 31 estados, Idaho SB 1227, Oregon S.B. 1546, Washington H.B. 2225, el AI Basic Act coreano (2026-01-22), la
Decisión 33/2026/QD-TTg de Vietnam y CONPES 4144—: **hay que abrir el texto normativo antes de usarlos con un cliente.**

Cadena de borrado en la capa de telemetría — **pase 21 (2026-10-01)**. 🟢 **Verificado de primera mano leyendo el
código fuente**, clonando cada repo con `git clone --depth 1 --filter=blob:none` y leyendo los archivos citados (no vía
WebFetch, no vía documentación):

- [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) — **Apache-2.0**, HEAD `2d24f2d` del **2026-09-04**.
  Leídos: `src/main/lrsql/admin/routes.clj` (ruta `["/admin/agents" :delete …]`, línea 331, y el registro condicional
  de la línea 407), `src/main/lrsql/admin/interceptors/lrs_management.clj` (la respuesta
  `{:status 200 :body params}`), `src/main/lrsql/spec/admin.clj` (`delete-actor-spec`, un solo campo `actor-ifi`),
  `src/main/lrsql/system/lrs.clj` (`-delete-actor`, dentro de `jdbc/with-transaction`),
  `src/main/lrsql/ops/command/statement.clj` (`delete-actor!`),
  **`src/db/postgres/lrsql/postgres/sql/delete.sql`** (`delete-actor-and-dependents!`, las 7 sentencias `DELETE` y la
  declaración `-- :result :affected`), `src/db/postgres/lrsql/postgres/sql/ddl.sql` (DDL de `statement_to_actor` y la
  migración `check-statement-to-actor-cascading-delete` / `add-statement-to-actor-cascading-delete!`),
  `resources/lrsql/config/prod/default/webserver.edn` (**`LRSQL_ENABLE_ADMIN_DELETE_ACTOR` default `false`**) y
  `LICENSE`.
- [LearningLocker/learninglocker](https://github.com/LearningLocker/learninglocker) — **GPL-3.0**, HEAD `5fec948`,
  que **coincide con el tag `v7.1.1`**, del **2021-11-16** (verificado con `git log -1` y `git ls-remote --tags`).
  Leídos: `api/src/routes/HttpRoutes.js`, `lib/constants/routes.js` (las rutas
  `/batchdelete/initialise|terminate/:id|terminate/all`), `api/src/controllers/BatchDeleteController.js`,
  `worker/src/handlers/batchStatementDeletion/batchStatementDeletion.js` (`Statement.deleteMany`, el `markDone` de los
  tres caminos de error, el re-encolado por páginas), `lib/models/batchDelete.js` (`total`, `deleteCount`,
  `processing`, `done`, `pageSize` 1000, y las funciones de ventana), `lib/models/siteSettings.js` (los tres campos
  `batchDeleteWindow*`) y `cli/src/scheduler/batchDelete.js` (el rescate de los jobs fuera de ventana).
- [openfun/ralph](https://github.com/openfun/ralph) — **MIT** (`LICENSE.md`, France Université Numérique), HEAD
  `53cc58c` del **2026-09-07**. Leídos: `src/ralph/api/routers/statements.py` (**sólo `@router.get`, `@router.put` y
  `@router.post`; no existe `@router.delete` en ningún router**), `src/ralph/backends/data/base.py`
  (`BaseOperationType`), `src/ralph/backends/data/mongo.py` (`_bulk_delete`, `unsupported_operation_types`),
  `src/ralph/backends/data/es.py` y **`src/ralph/backends/data/clickhouse.py`** (`DELETE` dentro de
  `unsupported_operation_types` y el docstring que lo declara).

Verificado vía **WebFetch** el 2026-10-01 (estrellas, forks, licencia y estado del repo leídos en la página):
[learninglocker](https://github.com/LearningLocker/learninglocker) (585 ★, 294 forks, GPL-3.0, **no archivado y sin
aviso de fin de vida** — ver tendencia 56) · [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS)
(506 ★, 426 forks, **GPL-3.0**, PHP, rama `release_11`, 76.385 commits) ·
[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (reverificación independiente: **40.6k ★**, Apache-2.0,
**2.386 commits**, **v1.6.12 del 2026-09-27** — coincide con el pase 20).

🔴 **No verificado de primera mano en el pase 21:** la limitación de **ILIAS** sobre xAPI/cmi5 y el LRS
(*«el dato personal de los statements persiste en el LRS»*, *«no hay forma de borrar datos en el LRS desde ILIAS»*)
viene del **Feature Wiki de ILIAS vía resultados de búsqueda**: **`docu.ilias.de` está bloqueado por el proxy de
egreso** (`EGRESS_BLOCKED`, reintentado en este pase). Es la afirmación que sostiene la mitad documental de la
tendencia **55** y **hay que abrir el wiki antes de citarla ante un cliente**. Contexto adicional sobre xAPI y GDPR
tomado de fuentes secundarias concordantes: [Learning Pool — cómo xAPI ayuda con
GDPR](https://learningpool.com/how-xapi-helps-solve-for-gdpr-requirements) · [Watershed — GDPR, xAPI y
herramientas](https://www.watershedlrs.com/blog/product/news/what-is-gdpr/) · [Rustici — GDPR en SCORM
Cloud](https://rusticisoftware.com/products/gdpr/).

Barrido regional del pase 21 (🔴 **ninguna fuente abierta de primera mano; todo de resultados de búsqueda**):
[MarketsandMarkets — North America AI in Education](https://www.marketsandmarkets.com/Market-Reports/geography/ai-in-education-market/North-America) ·
[Technavio — AI en el sector educativo](https://technavio.com/report/artificial-intelligence-market-in-the-education-sector-industry-analysis) ·
[CompTIA — tendencias EMEA 2026](https://www.comptia.org/en/blog/five-tech-trends-shaping-emeas-it-strategy-in-2026/) ·
[Consejo de Europa — dimensiones regulatorias de la AI en educación](https://coe.int/web/education/-/key-stakeholders-across-europe-will-explore-the-regulatory-dimensions-of-ai-in-education-at-the-2nd-working-conference-in-october) ·
[QS — Europe EdTech 200 y London EdTech Week 2026](https://newsletters.qs.com/announcing-the-2026-europe-edtech-200-plus-london-edtech-week-ai-skills-and-policy-moves/) ·
[IntelligentCIO APAC — brechas de gobernanza de AI en directorios APAC 2026](https://www.intelligentcio.com/apac/2025/12/09/ai-governance-gaps-widen-as-apac-boards-prioritise-innovation-for-2026/) ·
[UNU/UNESCO — AI en educación superior en LAC](https://unu.edu/publication/ai-implementation-higher-education-latin-america-and-caribbean) ·
[BID — marco regulatorio habilitante para AI en LAC](https://publications.iadb.org/publications/english/document/An-Enabling-Regulatory-Framework-for-Artificial-Intelligence-in-Latin-America-and-the-Caribbean.pdf) ·
[Barchart — adopción de AI en LATAM, expectativas 2026](https://www.barchart.com/story/news/36012717/industry-demand-is-driving-ai-adoption-from-the-ground-up-in-latin-america-heres-what-to-expect-in-2026)

## 63. De los dos estándares de analítica de aprendizaje, uno dejó de ser open source — con fecha, y hace tres años (agregado 2026-10-01, pase 25)

**El hallazgo:** 1EdTech **movió los repositorios de Caliper Analytics a privado el 2023-06-17**, y el acceso quedó para
*Contributing Members* y *Affiliates*. No es una inferencia: **la descripción del repo `1EdTech/caliper-java` es
literalmente el aviso** — *«NOTICE: 1EdTech will be moving Caliper to private repositories on June 17, 2023. Access to
the repositories will be available for 1EdTech Contributing Members and Affiliates.»*

Medido contra el otro estándar de la misma función:

| | **xAPI** (ADL → IEEE) | **Caliper Analytics** (1EdTech) |
|---|---|---|
| Especificación pública | `adlnet/xapi-profiles` — **Apache-2.0** ✅, 60 ★, 33 forks, 153 commits, viva | `1EdTech/caliper-spec` — 22 ★, **IMS Specification Document License** ⚠️ **no OSI** |
| Implementación de referencia | **Pública y permisiva:** `yetanalytics/lrsql` + **`yetanalytics/xapipe`** (Apache-2.0, 17 ★) | 🔴 **Privada.** `caliper-java`, `caliper-js`, `caliper-python`: **404** |
| Lo que queda público | — | `caliper-js-example` (**LGPL-3.0**, 8 ★, **©2018**) y `caliper-ontology`, **archivado** en 2019 |
| Trabajo normativo | **IEEE p9274.2.1 activo** tras xAPI 2.0 | Caliper 1.2, con implementaciones cerradas |

**Por qué es una tendencia y no un dato de catálogo.** Es la instancia más nítida del patrón *«estándar instalado vs.
modelo propio»* que esta KB nombró en la **tendencia 29**, y con una vuelta nueva: acá **el estándar sigue instalado
—los LMS siguen emitiendo Caliper— pero su implementación dejó de ser construible.** Eso **traslada costo al integrador**:
el cliente tiene un LMS que habla Caliper y un proveedor que, si no es miembro del consorcio, **tiene que escribir el
adaptador**. Y explica hacia atrás por qué toda la capa de telemetría que esta KB levantó en diez pases es xAPI: **no fue
una preferencia de esta base, fue el único lado del que había código.**

🔵 **La regla operativa, desde el pase 25:** se propone **xAPI**. Cuando el cliente pida Caliper, se le dice que **la
especificación es legible pero las implementaciones no son open source desde junio de 2023** y se cotiza el adaptador
como trabajo, no como configuración. Y `yetanalytics/xapipe` (*LRSPipe*) es la pieza que faltaba en el medio: **filtra
telemetría por *statement template* y por *pattern* de un xAPI Profile**, que es el control de minimización que piden
P40, P44, P45, P46 y P47.

## 64. La única capa de esta KB sin ninguna opción permisiva y productiva es, exactamente, la que el regulador nombró de alto riesgo (agregado 2026-10-01, pase 25)

Se barrió la capa de *proctoring* completa —era consigna del pase 24— y el resultado es simétrico y vale como advertencia
de propuesta: **las cinco piezas que existen fallan el mismo filtro, por dos caminos distintos.**

- **Camino copyleft:** `openedx/edx-proctoring` (**AGPL-3.0**, 68 ★), `oat-sa/lib-lti1p3-core` (**GPL-2.0**, 37 ★ — y es **la única certificada en *LTI 1.3 Proctoring Services*** de toda la base), `sudosylabs/Proctor` (**AGPL-3.0**, pre-release declarado), `kamlendras/OpenProctor` (**AGPL-3.0**, 37 commits).
- **Camino de los pesos:** `vardanagarwal/Proctoring-AI` es **MIT y tiene 635 ★ / 352 forks** —la pieza más traccionada de la capa— **pero su modelo de *facial landmarks* está entrenado con datasets de uso no comercial**, por su propio README, y el proyecto se declara de investigación.

🔴 **Y acá está la tendencia, que es la coincidencia:** el *proctoring* es **la única función educativa que el Annex III
del EU AI Act nombra de forma explícita** entre las de alto riesgo (aplicable **2027-12-02**), y Corea del Sur ya la
alcanza como *high-impact AI* desde el **2026-01-22**. O sea: **la capa con más exigencia regulatoria del sector es la
que tiene cero opciones permisivas y productivas en open source.** Las dos cosas no son independientes — el riesgo
regulatorio y de reputación es justamente lo que mantiene a los proveedores serios en modelo cerrado y deja el open
source en manos de demos y de copyleft institucional.

**La consecuencia comercial, y conviene decirla al revés de como la pide el cliente:** cuando un cliente pide
*«proctoring con AI»*, la respuesta rentable **no es buscar la pieza**: es **sacar el entregable del Annex III**. Se
entrega integridad de examen con **banco de ítems variabilizado y aleatorización** (`LongsightGroup/qti3` → ver
corrección en **P49**), **entrega certificada**, **notas por AGS** y **evidencia de proceso en xAPI**. Menos riesgo
regulatorio, licencias permisivas y un expediente defendible. Ver **P49** y el **gap 39**.

## 65. Apareció la primera pieza de estándar educativo con puerta nativa de agente, y la capa de competencias de esta KB no sabía hacer aserciones (agregado 2026-10-01, pase 25)

**Dos hallazgos que van juntos, los dos en `cassproject/CASS`** (Apache-2.0, 62 ★, 29 forks, 2.123 commits, verificado de
primera mano):

**(1) La capa de competencias de esta KB estaba incompleta y no lo sabía.** El pase 14 y el pase 20 levantaron la capa
CASE —`opensalt` (MIT, 45 ★), `1EdTech/OpenCASE` (Apache-2.0, 9 ★), `compeito` (Apache-2.0, 3 ★), `conform-ed` (MIT,
2 ★)— y las cuatro piezas **hospedan y validan marcos de competencias**. Ninguna **registra si un alumno alcanzó una
competencia**. CaSS hace las dos: autoría de marcos **y aserciones de logro individual con cómputo de perfil del
aprendiz**. Con 62 ★ es, además, **la más traccionada de toda la capa**. La pregunta que paga un proyecto de competencias
no es *«¿existe este marco?»* sino *«¿qué sabe este alumno?»*, y esta KB no tenía con qué responderla.

**(2) Y trae cartucho MCP.** Entre sus *«pluggable cartridges»* —**IMS CASE**, **xAPI**, CTDL-ASN, ASN, **Open Badges
2.0**— hay uno de **MCP**. 🔵 **Es la primera vez en 25 pases que esta KB encuentra una pieza de estándar educativo que
expone puerta nativa de agente.** La diferencia es de arquitectura, no de comodidad: un tutor de `agents/top.md` **lee el
marco y escribe la aserción sin adaptador escrito a mano**, y lo que devuelve **queda como aserción en un servidor de
estándares, no como texto en un chat** — o sea, queda auditable, exportable a Open Badges y comparable entre cohortes.

**Por qué es tendencia:** siete pases buscando *«agentes educativos»* devolvieron agentes genéricos (ver
`agents/trending.md`). Este pase encontró el valor en el lado opuesto del cable: **no un agente nuevo, sino el enchufe
estandarizado por donde entran los que ya hay.** Si el patrón se repite —estándares educativos publicando servidores MCP—
la capa de integración entera de esta KB se vuelve herramientas de agente, y eso es la consigna de búsqueda del pase 26.

## 66. El estándar de competencias con puerta de agente pasó de promesa a capacidad medida, y las dos tools que expone son exactamente los dos pasos que esta KB tenía inferidos (agregado 2026-10-01, pase 26)

La tendencia **65** (pase 25) registró que `cassproject/CASS` **declaraba** MCP entre sus cartuchos. Era una línea de
README, y el pase 25 fue honesto al marcarla como **gap 40**: *«está declarado, no medido»*. **Este pase la midió, y el
resultado es mejor que la promesa.**

**6 tools y 3 resource templates**, generados sobre un spec de **51 paths** que valida con **0 errores**. Y las dos que
deciden si esta capa sirve:

- **`record_evidence`** → `POST /api/xapi/statement`. *«Record evidence that a person has demonstrated (or failed to
  demonstrate) a competency»*, en palabras del propio repo. **Entra evidencia xAPI.**
- **`get_learner_profile`** → `GET /api/profile/latest`, con `frameworkId`, `subject`, `flushCache`, `cache` y
  `targetDateTime`. Su descripción es literalmente *«use this tool to answer the question "what does this person
  know?"»*. **Sale perfil de competencia computado.**

**Por qué esto es una tendencia y no un hallazgo de repo.** Desde el pase 14 esta KB sostiene que la pregunta que paga
un proyecto de competencias no es *«¿existe este marco?»* sino *«¿qué sabe este alumno?»*, y durante doce pasadas no
tuvo con qué responderla: la capa CASE (`opensalt`, `OpenCASE`, `compeito`, `conform-ed`) **hospeda y valida marcos y no
registra logro**. Ahora existe la pieza que lo registra **y la expone por MCP, bajo Apache-2.0** — es decir, **un agente
puede escribir evidencia y leer mastery sin que nadie escriba un *adapter***. El paso 4 de **P48** deja de ser inferido.

**Y hay una lectura de segundo orden que vale para toda esta KB.** CaSS no expone su API: **expone una superficie
curada** — 6 de 51 paths, con 45 `x-mcp-ignore` puestos a mano y descripciones escritas para que las lea un modelo
(*«Hints:»* incluidos). **La tendencia real es ésa: los estándares educativos están empezando a publicar superficie de
agente diseñada, no pasarelas automáticas sobre REST.** Es la diferencia entre un proyecto que agregó MCP y uno que
pensó qué debe poder hacer un agente. Para elegir sobre qué estándar construir, **la calidad de la superficie MCP ya es
un criterio de selección** — y conviene mirarla antes que las estrellas. Ver el **gap 40 (cerrado)**, el **gap 41** y
el patrón **P50**.

## 67. Esta KB puede proponer la herramienta y no el aula: el lado LMS de LTI no tiene implementación permisiva y productiva, y ahora está medido sobre seis candidatos (agregado 2026-10-01, pase 26)

El pase 24 encontró las dos primeras piezas *platform-side* de LTI y sospechó el problema. El pase 25 dejó escrita la
acción de medirlo. **Este pase lo cerró, con un resultado negativo que vale más que un repo nuevo:**

| Pieza | Licencia | Lado | Estado real |
|------|----------|------|-------------|
| `ltijs` | **Apache-2.0** ✅ | *tool* | **Exporta `[ 'Provider' ]` y nada más** (medido). *«Learning Tool»* en su propio `package.json` |
| `oat-sa/lib-lti1p3-core` | ⚠️ **GPL-2.0** | *platform* **y** *tool* | **La única completa y certificada 1EdTech.** Copyleft |
| `macewan-cs/lti` | **MIT** ✅ | *tool* | **Refutado como lado LMS.** *«partially implements»* |
| `LtiLibrary/LtiAdvantagePlatform` | **MIT** ✅ | *platform* | **«Sample»** en su propia descripción. ⛔ Sin `dotnet` acá |
| `Citolab/lti-1p3-platform-example` | ⚠️ **GPL-3.0+** | *platform* | **«example»** en el nombre |
| `UOC/java-lti-1.3-platform` | ⚠️ **sin licencia** | *platform* | *«**will** implement»* |

**La asimetría es estructural y conviene nombrarla así.** El ecosistema open source de LTI está construido para que
**mucha gente haga herramientas que entren a pocos LMS**. Por eso el lado *tool* es abundante, permisivo y maduro, y el
lado *platform* es escaso, copyleft o ejemplar: **los LMS grandes no necesitaban publicar el suyo**, y quien lo publicó
lo hizo como material de referencia. **No es una laguna del open source: es la forma del mercado.**

**Qué significa comercialmente, dicho sin adorno.** Esta KB es fuerte proponiendo **la herramienta que entra al LMS del
cliente** (`ltijs` Apache-2.0 + `canvas-mcp` MIT, y con el pase 26 el lado docente también). **No puede proponer el aula
misma con licencia permisiva.** Si un *engagement* pide el lado plataforma, las opciones son **GPL-2.0 certificada**,
integración como *tool*, o **desarrollo presupuestado** — y la peor de las cuatro es prometerlo como integración y
descubrirlo después. Ver el **gap 42** y el patrón **P51**.

## 68. La capa que el regulador aprieta más es la más vieja y peor abastecida del inventario, y la distancia es de doce años (agregado 2026-10-01, pase 26)

El pase 25 registró en la tendencia **64** que *proctoring* era la única capa sin opción permisiva y productiva, y que
era justo la que el **Annex III** nombra de alto riesgo. **Este pase encuentra una peor, y por un margen amplio.**

***Student success* / *early warning*.** Lo que existe open source: **FlightPath Academics** (GPLv3+, PHP, liberada el
**2013-03-13**, con *early alerts* y *Academic Priority* para alumnos en riesgo) **sin repositorio en GitHub**;
**Student Success Plan** de Unicon y el *dashboard* de **Marist College**, los dos con referencias verificables de
**2013–2014**. **Doce años sin renovación en la capa que predice el fracaso del alumno.**

**Y es exactamente la capa que la regulación acotó mientras el open source se quedaba quieto.** El **Annex III** del EU
AI Act la clasifica de alto riesgo; **Oklahoma y Maryland prohíben la decisión autónoma sobre el alumno** (pase 23);
**Delaware y Nueva York** prohíben el IEP automatizado (pase 3); **Colorado y Texas** agregaron requisitos *piecemeal*
(pase 26). **Seis estados y un reglamento europeo sobre una capa cuyo software libre es de 2013.**

**La inferencia que esta tendencia habilita, y es la más valiosa del pase para una propuesta.** Cuando el software
disponible es viejo y la regulación es nueva, **el entregable defendible no es el modelo predictivo: es el flujo con
humano decidiendo.** Un *early warning* que **ordena una cola de revisión humana** y deja expediente de por qué el
alumno entró en ella es vendible en las cuatro regiones y **no cae en la prohibición de decisión autónoma**; el mismo
modelo conectado a una acción automática es ilegal en dos estados y de alto riesgo en EMEA. **Es la misma pieza técnica
con dos envoltorios, y sólo uno se puede facturar.** Ver el **gap 47** y el patrón **P53**.

**Y el contraste que ordena el inventario de verticales de esta KB, ahora que son varias:** la biblioteca —abierta en
este pase— **tiene** opción permisiva, grande y moderna (**FOLIO**, Apache-2.0, 3.096 commits, Kafka) **y no tiene
presión regulatoria**; *student success* **no tiene** opción y **tiene toda la presión**. **La regla que se puede sacar:
en esta industria, el abastecimiento open source y el riesgo regulatorio están inversamente correlacionados** — lo que
el regulador nombró de alto riesgo es, sistemáticamente, lo que el open source no construyó. Vale para *proctoring*
(tendencia 64), para la capa predictiva (ésta) y para el modelado del alumno (gap 5). **Donde hay más riesgo hay menos
pieza, y por eso hay más proyecto.**

## Nota de método del pase 26 (2026-10-01) — el pase que ejecutó sin poder levantar el servidor, y el que midió un «no existe» sobre seis candidatos en vez de sospecharlo sobre dos

**Dos resultados de método, y el segundo vale más que el primero.**

**1. Cuando la ejecución está bloqueada, hay que buscar el eslabón puro y ejecutar ése.** El **gap 40** pedía levantar
el cartucho MCP de CaSS. El camino obvio —arrancar el servidor— está cerrado: necesita Elasticsearch y en este entorno
**no hay demonio de Docker** (el CLI está instalado, `/var/run/docker.sock` no existe). El pase 25 habría escrito
*«bloqueado»* y habría tenido razón. **Pero la generación de tools no depende del servidor:** `generateTools(spec)` es
una función pura sobre el OpenAPI, y el OpenAPI lo arma `swagger-jsdoc` leyendo los comentarios del código, **sin base
de datos**. Replicando las opciones exactas de `src/main/server.js` y validando con el mismo
`openapi-schema-validator` del arranque, el generador real corrió y devolvió **6 tools y 3 resource templates**.

**La regla que deja, y es la contracara de la regla del pase 24:** el pase 24 estableció que *cuando una conclusión
depende del comportamiento de una pieza de terceros, la inferencia no alcanza y hay que ejecutar*. Este pase agrega la
otra mitad: **cuando ejecutar el todo está bloqueado, hay que preguntarse qué parte del todo es pura — y ejecutar esa.**
Casi siempre existe un eslabón determinista (un generador, un parser, un validador) que no necesita la infraestructura
que falta. **No es una medición de segunda: las tres fuentes independientes —el generador ejecutado, la aserción del
test del propio repo (*«exactly 6 tools»*) y las 6 anotaciones `x-mcp-tool-name` del árbol— dan el mismo número.** Lo
que no se midió se dice: el *handshake* MCP real, que sí necesita Elasticsearch.

**2. Un «no existe» sólo vale si se midió el espacio completo, y hay que decir cuántos candidatos.** El pase 24 vio dos
piezas *platform-side* de LTI y escribió, con razón, que la capa estaba sesgada a *tool-side*. Este pase verificó
**seis** candidatos uno por uno —incluyendo instalar `ltijs` desde npm y **leer sus exports** en vez de su
documentación— y pudo pasar de *«parece que no hay»* a **«no hay, sobre seis, y éstas son las razones de cada uno»**.
**La diferencia es comercial, no académica:** lo primero no se puede decir en una reunión; lo segundo es un argumento
con evidencia que justifica presupuestar desarrollo. **Un gap sin denominador es una impresión. Con denominador es un
hallazgo.** Y de paso corrigió un falso positivo del resumen de búsqueda: `macewan-cs/lti` es **MIT** pero es
**tool-side**, no el lado LMS que el resumen sugería.

### Lo que trajo el barrido obligatorio, y es la octava pasada seca para la tabla de agentes

Cuatro búsquedas globales y cuatro regionales, con el año **calculado** (2026). **Cero agentes nuevos por octava vez
consecutiva.** Lo global devolvió la capa genérica (openclaw 385k ★, browser-use, Mem0, AutoGen, dify) y **material
didáctico *sobre* AI** (`ai-engineering-from-scratch`, `free-ai-agents-resources`, listas de repos para «aprender AI
en 2026»). **Ocho pases confirman la medición del pase 23 y conviene sacar la conclusión operativa: el canal de
descubrimiento por la palabra `education` está agotado y seguir pagándolo es desperdicio.** Las altas de las últimas
tres pasadas vinieron, todas, de ejes que no usan esa palabra: **artefacto** (pase 24), **estándar** (pase 25) y
**conector** (pase 26).

⚠️ **Y una cifra del barrido que NO se registró, con el motivo.** El barrido global devolvió un *«Hermes Agent, MIT,
180.000+ ★ desde su lanzamiento en febrero de 2026, el framework OSS de más rápido crecimiento de 2026»*. **No se
registra:** no es educativo, viene de un agregador sin verificación de primera mano, y **esta KB ya se quemó con
conteos de estrellas inflados por el canal** (la corrección del pase 4 del `technology`-KB y la del pase 22 acá). Si
aparece otra vez, se verifica contra la página del repo antes de escribirlo.

### La advertencia de método sobre la verificación de URLs, que contradice la consigna y hay que decir por qué

**La consigna pide verificar cada URL con `curl -sI`. En esta sesión eso produce datos falsos y no se usó.**
`curl -sI` contra `github.com` devuelve **`403` para todas las URLs** —se probó contra cinco, incluidas
`cassproject/CASS` y `DavidLMS/learnmcp-xapi`, que existen y están en esta KB desde los pases 25 y 6— porque el proxy
de egreso corta el `HEAD`. **Verificar con `curl` acá habría marcado como 404 a repos reales**, que es exactamente el
error que la consigna quiere prevenir. **Toda la verificación de este pase se hizo con WebFetch sobre la página del
repo**, leyendo licencia, ★, forks y commits de la página. El único 404 reportado —`Cerebro-Tech/FlightPath`— es un 404
**de WebFetch** sobre una URL que este pase **conjeturó** (FlightPath no publica en GitHub), no la refutación de una
URL citada por una fuente.

### Los dominios bloqueados, que ya son cuatro y sostienen afirmaciones regionales

`unu.edu` (**`EGRESS_BLOCKED`**), **`publications.iadb.org`** (**`EGRESS_BLOCKED`**, nuevo en este pase),
`coe.int` (**HTTP 000**) y `www.iesalc.unesco.org`. 🔴 **Van dos pases con la base de evidencia primaria de LATAM
inalcanzable**, y el dominio que se agregó dolía: el barrido ubicó *«An Enabling Regulatory Framework for Artificial
Intelligence in Latin America and the Caribbean»* (**BID**), que es **la fuente primaria regulatoria regional que esta
KB no tiene**. **Es un límite del entorno, no una laguna de investigación** — y hay que levantarlo desde una red sin
este proxy antes de usar esas cifras con un cliente.

### Lo que este pase NO hizo, declarado como tal

- **No hizo *handshake* MCP** contra el cartucho de CaSS (necesita Elasticsearch → Docker). Se midió generación, no
  invocación.
- **No midió el *launch* LTI de punta a punta**: sin `dotnet`, y `dot.net` bloqueado por el proxy (`CONNECT … 403`).
- **No verificó fecha de último commit** de ninguno de los repos nuevos: la página no la expone de forma legible vía
  WebFetch en esta sesión. Señales de vida usadas: commits totales, forks y ★.
- **No buscó conector MCP para Open edX**, que es el hueco simétrico del **gap 43**. Queda como consigna.
- **No verificó la implementación de referencia de 1EdTech en Ruby on Rails** (platform + tool), que apareció en el
  barrido. Es la última candidata no mirada del **gap 42**.
- **No cerró los gaps 36 y 38** (la cadena de `lrsql`): siguen necesitando `next.jdbc` resuelto, y
  `repo.clojars.org` sigue respondiendo **403** por el proxy, igual que en el pase 25.

## 🔵 Las tres acciones que este pase deja escritas para el siguiente

1. **Hacer el *handshake* MCP real contra el cartucho de CaSS**, que es lo único que falta para que el cierre del gap 40
   sea de punta a punta. **El punto exacto a destrabar está localizado:** el log se detiene en
   *«SkyrepMigrate Waiting for Elasticsearch to appear at http://localhost:9200»* — todos los endpoints ya se bindean
   antes de eso, así que **sólo falta satisfacer ese *probe***. Con un entorno con demonio de Docker
   (`docker compose up -d elasticsearch-cass`, que el repo ya trae) o un ES embebido, levantar el server, hacer
   `initialize` + `tools/list` contra **`POST /api/mcp`** y comparar con las **6** medidas acá. **Si coinciden, P48 y
   P50 se cotizan sin asterisco.**
2. **Seguir el eje conector, que rindió dos veces seguidas, en lo que quedó sin barrer:** `MCP server` +
   **Open Badges**, + **SCORM**, + **Caliper** (acá el hallazgo esperable es la **ausencia**, porque Caliper dejó de ser
   open source el 2023-06-17 — y hay que **escribir la ausencia**). Y **buscar `canvas-mcp` como patrón, no como repo:**
   si existe un conector MIT de 102 tools para Canvas, preguntar explícitamente por el equivalente de **Open edX** (que
   **no se buscó**) — para Moodle ya se sabe que no existe (gap 43).
3. **Cerrar el gap 42 por agotamiento** verificando la **implementación de referencia de 1EdTech en Ruby on Rails**
   (platform **y** tool), que es la última candidata no mirada. Si también es copyleft o material de referencia, el
   *«no existe permisivo y productivo del lado LMS»* pasa de **medido sobre seis** a **cerrado**, y eso habilita decirle
   a un cliente *«el lado plataforma se presupuesta como desarrollo»* con la evidencia completa puesta sobre la mesa.

## Nota de método del pase 25 (2026-10-01) — el pase que ejecutó la consigna entera y volvió con dos falsos negativos propios: el eje artefacto rinde, y lo que más rinde es declarar límites

**Lo que se hizo:** el barrido obligatorio completo —**cuatro búsquedas globales y cuatro regionales**, con el año
**calculado** (2026), no fijado— **más los siete ítems de la consigna del pase 24**: los artefactos `item bank`,
`proctoring`, `timetable` y `competency framework`/CASE, los estándares **Caliper**, **CASE** y **xAPI Profiles**, y la
instrucción específica de *«buscar `LTI platform` explícitamente»*. **Se ejecutaron los siete.**

**Resultado: 18 repos verificados de primera mano, 17 nuevos para esta KB**, 3 tendencias nuevas (**63, 64, 65**), 2 patrones nuevos
(**P48, P49**), 2 gaps nuevos (**39, 40**) y **dos correcciones a conclusiones del pase 24**.

### 🔴 Los dos falsos negativos del pase 24, y los dos tienen la misma causa

| Lo que el pase 24 escribió | Lo que el pase 25 midió | La causa |
|---|---|---|
| *«`LongsightGroup/qti3-core` → **404** […] el repo GitHub con ese nombre no existe»* | ✅ **`LongsightGroup/qti3` existe** — MIT, 667 commits, 12 paquetes, **con *writer* de banco de ítems y migración QTI 1.2/2.x→3** | Se buscó **el nombre del paquete npm** (`@longsightgroup/qti3-core`), no el del repo. El monorepo no lleva sufijo |
| *«`yetanalytics/lrspipe`»* (citado como la pieza de *forwarding*) | **404.** El repo real es **`yetanalytics/xapipe`** (Apache-2.0, 17 ★) | Se buscó **el nombre del producto** (*LRSPipe*), no el del repo |

🔵 **La regla que este pase agrega, y vale para toda la KB:** **el nombre del producto y el nombre del paquete no son el
nombre del repo.** Antes de escribir un 404 como no-hallazgo hay que probar **el nombre corto de la organización** —sin
sufijos (`-core`, `-platform`) y sin el nombre comercial—. Dos de los cuatro no-hallazgos que el pase 24 declaró eran
repos reales, y uno de ellos tenía justamente lo que la consigna del pase 25 estaba buscando. Un no-hallazgo mal medido
**es peor que no buscar**, porque cierra la pregunta.

### ⚠️ Advertencia 1 — dos dominios institucionales bloqueados, y los dos sostienen cifras regionales

`unu.edu`, `coe.int` y `www.iesalc.unesco.org` están **bloqueados por el proxy de egreso** de esta sesión. Eso afecta
directamente a dos datos que van a `intel/market.md`:

- Las cifras del estudio **UNESCO IESALC / UNU-IAS** sobre AI en educación superior en LAC (**87 %**, **74 %**, **45 % vs. 70 %**) vienen de **resúmenes de buscador concordantes**, **no** de la lectura de la fuente primaria. Están etiquetadas como tales en `market.md`.
- La **2.ª conferencia de trabajo del Consejo de Europa** sobre las dimensiones regulatorias de la AI en educación **no se pudo verificar**: queda registrada como **señal sin verificar**, con el dominio bloqueado dicho por su nombre.

### ⚠️ Advertencia 2 — una tensión de fechas en la fuente LATAM que no hay que copiar mal

El mismo estudio aparece con **dos fechas** según el canal: el **trabajo de campo** se declara entre **agosto y octubre de
2025**, y el **lanzamiento** fue durante la **Digital Learning Week 2026** en la sede de UNESCO en París. **Las dos son
correctas y no son la misma cosa.** Una propuesta que cite *«datos 2026»* para una encuesta de campo de **2025** está
sobredatando la evidencia en un año, que en adopción de AI es mucho. Escribir: *«encuesta de 2025, publicada en 2026»*.

### ⚠️ Advertencia 3 — la coincidencia de cifras LATAM es aparente, y mezcla dos poblaciones

El barrido LATAM devolvió **87 %** (instituciones de educación superior con AI en al menos un área, IESALC) junto a
**«100 % de las empresas usará AI en al menos una actividad»** y **«85 % de las empresas la integra nativamente»**. **No
son la misma medición ni la misma población:** una es de **universidades**, las otras de **empresas**. Promediarlas o
usarlas de refuerzo mutuo en una propuesta es un error de lectura. La cifra que sirve para un *engagement* educativo es
la de **instituciones**.

### Lo que este pase NO hizo, declarado como tal

- **No levantó `LtiLibrary/LtiAdvantagePlatform` contra un *tool* real.** Es **MIT, con AGS v2 + NRPS v2 + Deep Linking 2.0 y ASP.NET Core 10**, pero **se describe a sí misma como *«Sample»***. Que el *launch* cierre de punta a punta **está leído, no medido** — y es la acción barata que el pase 26 tiene que ejecutar antes de que esta KB prometa el lado LMS.
- **No verificó la fecha del último commit** de ninguno de los 12 repos: la página de GitHub no la expuso de forma legible vía WebFetch en esta sesión. Las señales de vida usadas son **commits totales, releases y forks**, que son más débiles.
- **No midió si el cartucho MCP de CaSS funciona.** Está **declarado en el README** entre los *pluggable cartridges*; no se levantó el servidor ni se listó una sola herramienta. Toda la tendencia **65** y el paso 4 de **P48** descansan en una declaración del propio proyecto. **Es el gap 40.**
- **No buscó** los artefactos `admissions`, `library`/OPAC ni `alumni`/*student success*: quedan como consigna del pase 26.

### 🔵 Las tres acciones que este pase deja escritas para el siguiente

1. **Levantar `LtiAdvantagePlatform` (MIT) contra `ltijs` (Apache-2.0, 373 ★) y medir si el *launch* OIDC cierra**, con AGS devolviendo una nota. Si cierra, esta KB puede proponer **el lado LMS con licencia permisiva** — capacidad que no tuvo en 24 pases. Si no cierra, escribirlo: *«Sample»* está en su propia descripción.
2. **Levantar el cartucho MCP de CaSS y listar sus herramientas** (gap 40). Es la verificación que convierte la tendencia 65 de promesa en capacidad, y la que decide si **P48** se puede cotizar.
3. **Cambiar el eje de búsqueda al conector**, que es donde este pase mostró tracción: `MCP server` + cada estándar que esta KB ya inventarió (**OneRoster, CASE, xAPI, QTI, LTI**). CaSS valió por sus cartuchos, no por su núcleo.

## Nota de método del pase 24 (2026-10-01) — el pase que dejó de leer código y lo ejecutó, y por eso pudo corregir al pase anterior

**Los pases 21, 22 y 23 leyeron `lrsql`. Este lo corrió.** Es la primera vez en veinticuatro pasadas que esta KB levanta
un motor de base de datos, crea el esquema con el DDL del proyecto y mide lo que devuelve un driver. **Y el resultado
invirtió una conclusión que la KB había escrito con confianza**: el pase 23 dedujo, de la forma del SQL, que el desglose
por tabla era inalcanzable sin partir las consultas; la medición muestra que los siete conteos ya vuelven por el bucle
estándar de JDBC. **La lectura del código era correcta y la inferencia sobre el driver no**, y sólo ejecutar podía
distinguir una cosa de la otra.

**La regla de método que deja, y vale más que el hallazgo:** cuando una conclusión de esta KB dependa del
**comportamiento de una pieza de terceros** —un driver, un runtime, un planificador— y no del código que se está
leyendo, **la inferencia no alcanza y hay que marcarla como pendiente de ejecución.** El pase 23 hizo lo correcto al
declarar explícitamente *«lo que NO se verificó ejecutando»* y dejar la acción escrita; sin esa declaración este pase
no habría sabido qué medir. **La cadena funcionó: declarar la ignorancia con precisión es lo que la vuelve resoluble.**

### Lo que trajo el barrido obligatorio, y es la sexta pasada seca para la tabla de agentes

Se corrieron las cuatro búsquedas globales y las cuatro regionales con el año **calculado** (2026). **Cero agentes nuevos
por sexta vez consecutiva.** Lo global devolvió, otra vez, la capa genérica (openclaw 385k ★, AutoGen, browser-use,
Mem0) y **material didáctico sobre AI** (`ai-engineering-from-scratch`, `free-ai-agents-resources`) — confirmando la
medición del pase 23: en GitHub el término `education` está capturado por *cursos sobre AI*, no por *software que educa*.

**Pero la consigna del pase 23 sí rindió, y rindió donde dijo que iba a rendir.** La instrucción era **evitar la palabra
`education`** y buscar por el **artefacto del dominio** o por el **estándar instalado**. Las cuatro búsquedas de
artefacto/estándar (`gradebook`+OneRoster+LTI, QTI 3 *item bank*, IEP, SIS/matrícula/asistencia/legajo) trajeron **seis
repos verificados de primera mano, cinco nuevos para esta KB**, y el hallazgo de encuadre del pase: **la capa LTI de esta
KB era íntegramente PHP, y existe una familia Java/Spring completa** publicada por una universidad europea. Ver
`repos/trending.md` y la sección nueva de `agents/top.md`.

**La consigna para el pase 25, y es una continuación, no un cambio de eje:** el eje artefacto/estándar **no está agotado**
— rindió en su primer uso. Quedan sin barrer los artefactos **`item bank`/banco de ítems**, **`proctoring`**,
**`timetable`/horario** y **`competency framework`/CASE**, y los estándares **Caliper**, **CASE** y **xAPI Profiles**.
Y queda una pregunta de método abierta: las dos únicas piezas *platform-side* (lado LMS) que vio esta KB aparecieron en
este pase y **una no declara licencia**; conviene buscar explícitamente `LTI platform`, porque toda la capa registrada
hasta ahora es *tool-side* y eso sesga lo que se puede proponer.

### La acción que este pase deja escrita

Dos, y las dos son chicas y de primera mano:

1. **Medir qué devuelve `next.jdbc` con `:result :affected`** sobre una consulta multi-sentencia, que es el único eslabón
   de la cadena del gap 36 que sigue inferido. **Este pase no pudo:** `repo.clojars.org` responde **403** por el proxy de
   egreso, así que no se pudo resolver `next.jdbc` ni `hugsql-adapter-next-jdbc`. Se puede hacer con el jar bajado por
   fuera o con `clojure-tools` oficial instalado. **Lo que hay que mirar** es si `execute!` llama `getMoreResults()`: si
   no lo llama —y la medición del driver sugiere que no, porque lrsql ve un solo número— el parche del gap 36 vive en el
   adaptador o en el interceptor, y no en lrsql.
2. **Enumerar las consultas multi-sentencia de lrsql** para dimensionar el *blast radius* del gap 38. Este pase lo
   intentó y **el clasificador de seguridad del entorno bloqueó el recorrido masivo del árbol clonado** — el mismo límite
   que frenó al pase 22. Con el árbol a mano fuera de este entorno es una tarde.


## Nota de método del pase 22 (2026-10-01) — el pase que midió su propio agotamiento, y encontró el hallazgo en la búsqueda que no era sobre agentes

**Qué se ejecutó.** El barrido obligatorio completo —cuatro búsquedas globales y cuatro regionales (North America,
EMEA, APAC, LATAM)— más la reconfirmación independiente del **gap 36** leyendo el código de `lrsql`.

**Resultado del barrido: agotado por cuarta vez consecutiva, y por primera vez medido candidato por candidato.**

- **Cero agentes nuevos.** Los dos únicos candidatos que trajo la búsqueda ya estaban en la KB **y la KB los tenía más
  precisos que la fuente**: `OpenMAIC` (la web lo da como «v1.0.0, MIT» y omite el **relicenciamiento de AGPL-3.0 a MIT
  en v0.3.0 del 2026-06-28**, que es exactamente el dato que hunde una propuesta) y `AITutor-EvalKit` (ya corregido en
  el pase 4: el repo canónico del mismo autor es `UnifyingAITutorEvaluation`, 32 ★).
- **Cero cifras de mercado nuevas.** Las ocho que devolvió el barrido regional —global $7,52B→$10,6B al 40,9% y los
  $79,6B a 2034; North America $951M→$2.303,2M al 15,9%; APAC $591,6M→$1.848,1M al 20,9%; la encuesta LATAM 2026 del
  Digital Education Council con 92%/79% y la grilla de gobernanza 26,0/18,5/9,0; el programa educativo de OpenAI con 8
  socios y los USD 169 M— **ya estaban todas en `intel/market.md`, con fuente y con las discrepancias metodológicas
  declaradas**. Se reconfirman, no se agregan.
- **Y una donde la KB le gana en precisión a la web, que conviene saber porque el cliente leyó la web:** las fuentes
  generalistas dicen que el EU AI Act *«entra plenamente en vigor en agosto de 2026»* clasificando educación como alto
  riesgo. **El calendario real que esta KB tiene es más fino** —en vigor 2026-07-27, aplicación por el AI Office desde
  2026-08-02, **Anexo III (educación) el 2027-12-02**— y la diferencia es de **16 meses de margen** sobre la obligación
  que al cliente más le preocupa. Hay que llevar el calendario, no la nota de prensa.

**Lo que esto dice sobre el método, y es la conclusión operativa del pase.** Los tres pases que movieron la tabla lo
hicieron **cambiando el sustantivo de la búsqueda**, no la región: el pase 4 buscó *benchmark* en vez de *repo de
agente*, el pase 17 buscó `SKILL.md` + dominio educativo, y **este pase encontró lo que encontró buscando
`plataforma / LMS open source` — no buscando agentes**. El barrido regional lleva cuatro pasadas dando confirmación.
**El rendimiento está en cambiar el eje, no en insistir con el mismo y rotar el país.**

**Qué se verificó de primera mano.** `tutor-contrib-aspects` y `platform-plugin-aspects` (licencia, estrellas, forks,
commits, lenguaje, y el `UserRetirementSink` leído en el README); el **PR #1328** (título, autor, estado **cerrado sin
mergear** el 2026-09-16, y la descripción del bypass del flag de PII); y el interceptor de `lrsql`
(`interceptors/lrs_management.clj:23–33`, `routes.clj:331` y `:407`, `protocol.clj:58`) por lectura directa del árbol
clonado.

**Qué NO se pudo verificar, y queda declarado en vez de inferido.** Dos cosas, las dos con su causa:

1. **El ADR de PII de Aspects** —la fuente de la afirmación *«el dato de eventos no se elimina porque queda
   anonimizado»*— vive en `docs.openedx.org`, **bloqueado por el proxy de egreso**, igual que `arxiv.org` en los pases
   6, 7, 14, 16–19 y `moodle.org` en el 19. Los dos caminos alternativos (el `.rst` crudo y el listado del directorio
   de decisiones en GitHub) dieron **404**. La afirmación se registra por snippets concordantes, con la URL anotada.
2. **Si `-delete-actor` ya devuelve los conteos de filas afectadas** —la sub-pregunta que decide si el parche del
   **gap 36** es de una línea o necesita plomería—. **La traza de la implementación quedó bloqueada por el clasificador
   de seguridad del entorno** (dos denegaciones al explorar el árbol clonado de terceros). **No se contestó por
   inferencia**, que era la tentación obvia teniendo el resto del archivo a la vista.

**La regla que este pase agrega a las de los pases 5 y 12.** El pase 5 escribió que *«el proxy de egreso decide qué se
puede afirmar»*. Este pase agrega la otra mitad: **el entorno también decide qué se puede investigar, y cuando bloquea
una lectura la respuesta correcta es declarar la pregunta abierta con su coordenada exacta, no completarla con lo que
probablemente diga el código.** Las dos veces que esta KB se equivocó en grande —el gap 33 y las estrellas de los
ciclos 1–3— fue por afirmar sin leer.

## Nota de método del pase 21 (2026-10-01) — el pase que ejecutó la acción escrita hace dos pasadas, y encontró que la KB se había equivocado a su propio favor comercial

**Lo que se hizo distinto, y es la razón por la que funcionó.** Veinte pasadas verificaron repos **abriendo su página en
GitHub**: licencia, estrellas, forks, commits, descripción. Eso alcanza para saber **qué es** un repo y **no alcanza
para saber qué hace**. Este pase **clonó tres repositorios y leyó el código fuente**, que es lo que el pase 19 había
hecho una sola vez —sobre el árbol de Moodle— y que resultó, las dos veces, el método más productivo de esta KB.

**El resultado incómodo, dicho sin suavizar.** El **gap 33** —vigente desde el pase 19, citado en la tendencia 49, en
**P38**, en **P40**, en `verticals/solutions.md`, en `repos/foundations.md` y en los argumentos de EMEA y LATAM de
`intel/market.md`— **era falso en su mitad principal**. El LRS permisivo que esta KB recomienda como default
(`lrsql`, Apache-2.0) tiene el mejor primitivo de borrado de toda la capa, y lo tenía desde antes de que esta KB
existiera. **Y la propia KB tenía escrita la nota que lo advertía**, al pie de la tabla: *«el "no" es ausencia en la
documentación publicada, no una prueba de que la operación sea imposible»*. **La nota tenía razón y sobrevivió catorce
pasadas sin que nadie la ejecutara.**

**Por qué el error fue en esta dirección y no en otra, que es lo que conviene no repetir.** Un gap declarado es
**vendible**: justifica alcance, justifica horas, justifica un patrón. Una capacidad que ya existe en el producto
recomendado **no factura nada**. No hubo mala fe —hubo una tabla construida sobre documentación y una nota al pie que
nadie convirtió en tarea— pero el sesgo es estructural: **los gaps se revisan menos que los hallazgos, porque nadie
tiene incentivo para cerrar uno.** La contramedida concreta, para los pases que vienen: **todo gap cuya evidencia sea
"no está documentado" se marca como lectura pendiente, no como ausencia**, y no entra a un entregable de cliente hasta
que alguien haya leído el código.

**Qué está verificado y con qué fuerza, en tres niveles distintos.**

1. 🟢 **Leído en el código fuente** (la evidencia más fuerte que produce esta KB): todo lo que afirman las tendencias
   **54** y **56**, la mitad técnica de la **55**, el **gap 36**, la matriz corregida de `verticals/solutions.md`, la
   tabla corregida de `repos/foundations.md` y el patrón **P44**. Incluye las rutas, los nombres de archivo y los
   números de línea, para que el próximo pase pueda contradecirlo sin volver a buscar.
2. 🟡 **Leído en la página del repo vía WebFetch**: estrellas, forks, licencias y el hecho de que Learning Locker
   **no** está archivado. La reverificación de **DeepTutor** coincide con la del pase 20 — dos lecturas independientes
   concordantes, que es lo más cerca de "confirmado" que llega esta KB sin la API.
3. 🔴 **Resultados de búsqueda, sin fuente primaria**: la limitación de **ILIAS** (`docu.ilias.de` bloqueado) y
   **todo el barrido regional**. No usar en material de cliente sin abrir la fuente.

**El barrido regional dio el mismo resultado que en los pases 19 y 20, y por tercera vez consecutiva se registra como
gap informado y no como silencio.** Las cuatro búsquedas regionales (`AI {industry} {region} 2026 adoption regulation
players`) devolvieron **AI empresarial, no educativa**: prioridades de CIO, gobernanza de directorios, soberanía de
infraestructura, inversión en *reskilling* corporativo. **La consulta regional genérica está agotada para esta
vertical** — y la regla del pase 20 sigue siendo la salida: *si la región no devuelve nada, el nombre que falta es el
de un país*. Lo poco aprovechable apareció así: Reino Unido con **£200M+** comprometidos en adopción de AI (del cual
£100M a Bridge AI y £53M a iniciativas regionales), el **Europe EdTech 200** y la London EdTech Week como mapa de
*players* de EMEA, y la constatación de que **APAC y LATAM no tienen cifra de mercado educativo propia en esta
ventana**. Se detalla por región en `intel/market.md`.

**Una limitación de entorno que cambió, y conviene registrarla.** Veinte pasadas anotaron que `curl -sI` devuelve 403
contra `github.com` y que la API de GitHub está fuera de alcance. **Las dos siguen siendo verdad, y las dos dejaron de
importar para lo que decide este archivo:** `git clone --depth 1 --filter=blob:none` **funciona a través del proxy**,
y leer un archivo del árbol clonado es evidencia más fuerte que cualquier cosa que devuelva la API. **La verificación
de capacidad se hace clonando, no consultando.** Es la recomendación de método más reutilizable de este pase.

Testing de conformidad y evaluación regulatoria — **pase 20 (2026-10-01)**. Repos verificados de primera mano vía WebFetch (licencia, estrellas, forks, alcance declarado): [inspect_ai (UK AISI)](https://github.com/UKGovernmentBEIS/inspect_ai) · [moonshot](https://github.com/aiverify-foundation/moonshot) · [compl-ai](https://github.com/compl-ai/compl-ai) · [aiverify](https://github.com/aiverify-foundation/aiverify) · [moonshot-data](https://github.com/aiverify-foundation/moonshot-data) · [LLM-Evals-Catalogue](https://github.com/aiverify-foundation/LLM-Evals-Catalogue) · [awesome-eu-ai-act](https://github.com/morganrcu/awesome-eu-ai-act) · [moonshot-cicd](https://github.com/aiverify-foundation/moonshot-cicd) · [moonshot-ui](https://github.com/aiverify-foundation/moonshot-ui) · [aiverify-developer-tools](https://github.com/aiverify-foundation/aiverify-developer-tools) · [organización aiverify-foundation](https://github.com/aiverify-foundation)

*Unlearning* educativo — **pase 20**, verificado vía WebFetch: [GEMLab-HKU/Unlearn_and_Relearn](https://github.com/GEMLab-HKU/Unlearn_and_Relearn) (MIT, 4 ★, 22 commits; GEMLab, Universidad de Hong Kong — Jiajia Song, Zhihan Guo, Jionghao Lin). Paper: Springer `10.1007/978-3-032-29744-0_42`, preprint `arXiv 2603.26142` (🔴 **arxiv.org y link.springer.com no se abrieron: bloqueados / no verificados de primera mano**). Colisión de terminología documentada contra *Lifting Data-Tracing Machine Unlearning to Knowledge-Tracing for Foundation Models* (`arXiv 2506.11253`, 🔴 sin verificar).

Marco regulatorio y plataforma estatal de Singapur — **pase 20**. 🔴 **Todo de fuentes secundarias concordantes: `imda.gov.sg`, `moe.gov.sg` y `learning.moe.edu.sg` están bloqueados por el proxy de egreso de esta sesión.** *Model AI Governance Framework for Agentic AI* v1.5 (anunciado 2026-01-22 en el WEF; actualizado 2026-05-20 y 2026-06-05), *Starter Kit for Testing LLM-Based Applications for Safety and Reliability* v1.0 (enero 2026), crosswalks a NIST AI RMF (oct-2023) y a ISO/IEC 42001:2023 (jun-2024), y las ocho funciones de AI del Student Learning Space (seis nombradas: ALS, LEA, FA-Math, AFA, SAFA, SET). **Antes de usar cualquiera de estos datos con un cliente: abrir la fuente del MOE y de IMDA.**

Regulación regional — **pase 20**, fuentes secundarias concordantes: North America (**134 proyectos de ley en 31 estados**, California AB 1159, Idaho SB 1227, Oklahoma y Maryland, Georgia y Mississippi; RAND 25%→53% en planificación docente) · EMEA (AI Act en vigor 2026-07-27, aplicación desde 2026-08-02, Anexo III 2027-12-02, Anexo I 2028-08-02) · LATAM (Brasil **PL 2338/2023**, Chile **Ley 21.719** + proyecto de cuatro niveles, México **85 iniciativas** y auditoría anual de alto riesgo; auditorías técnicas de detectores en el sector educativo mexicano con tasas de error altas).

Borrado, telemetría y *unlearning* — **pase 19 (2026-10-01)**. Verificado de primera mano sobre el árbol de Moodle (clon `--depth 1 --filter=blob:none --sparse`, `main` = **5.3rc1**, commit `85af0b5`): [moodle/moodle](https://github.com/moodle/moodle) — `public/ai/classes/privacy/provider.php`, los siete `public/ai/provider/*/classes/privacy/provider.php`, `public/admin/tool/dataprivacy/db/events.php`, `public/admin/tool/dataprivacy/classes/event/user_deleted_observer.php` y `public/admin/tool/dataprivacy/classes/api.php`. Rama verificada con `git ls-remote --heads`. Repos verificados vía WebFetch: [open-unlearning](https://github.com/locuslab/open-unlearning) · [machine-unlearning-pytorch (`torchunlearn`)](https://github.com/Harry24k/machine-unlearning-pytorch) · [OngWinKent/MachineUnlearning](https://github.com/OngWinKent/MachineUnlearning) · [jjbrophy47/machine_unlearning](https://github.com/jjbrophy47/machine_unlearning) · [lrsql](https://github.com/yetanalytics/lrsql) · [ralph](https://github.com/openfun/ralph) · [learninglocker](https://github.com/LearningLocker/learninglocker) · [topic `ai-tutor`](https://github.com/topics/ai-tutor)

Agentes nuevos — pase 19, verificados vía WebFetch: [human-skill-tree](https://github.com/24kchengYe/human-skill-tree) · [universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) · [algo-sensei](https://github.com/karanb192/algo-sensei) · [universal-diagnostic-tutor-skill](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) · [lumen](https://github.com/ahmedEid1/lumen)

Regulación — pase 19: **Vietnam, Ley de IA N.º 134/2025/QH15 y Decisión 33** (46 sistemas de alto riesgo en 6 sectores, 3 en educación; [Allen & Gledhill](https://www.allenandgledhill.com/vn/publication/articles/33374/identifies-high-risk-ai-systems-across-six-sectors), [Vietnam Briefing](https://www.vietnam-briefing.com/news/46-high-risk-ai-systems-to-face-enhanced-regulatory-oversight-in-vietnam.html), [Tilleke & Gibbins](https://www.tilleke.com/insights/vietnam-introduces-sectoral-list-of-high-risk-ai-systems/2/)) · **Digital Omnibus / Reglamento (UE) 2026/1744 y la confirmación de que el Art. 50 no se movió** ([Usercentrics](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/), [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/), [Jones Walker](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon)) · **California AB 1159 / HESIPA**, firma **2026-09-10**, operativa **2027-07-01** ([F3 Law](https://www.f3law.com/insights/new-california-law-limits-technology-companies-use-of-student-data-in-ai-systems-102o16i/), [Privacy Rights Clearinghouse](https://privacyrights.org/resources-tools/articles/governor-signs-prc-sponsored-ab-1159-law-strengthening-privacy-protections)) · **gobernanza docente en EE. UU.** ([MultiState](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session), [AI for Education: guía estatal](https://www.aiforeducation.io/ai-resources/state-ai-guidance)) · **adopción LATAM** ([Digital Education Council, encuesta LATAM 2026](https://www.digitaleducationcouncil.com/dec-insights/92-of-students-and-79-of-faculty-actively-engaging-with-ai-findings-from-ai-in-higher-education-latam-survey-2026)) · **borrado en xAPI** ([Learning Pool: xAPI y GDPR](https://learningpool.com/how-xapi-helps-solve-for-gdpr-requirements))

⚠️ *Del pase 19: **`arxiv.org` sigue bloqueado por el proxy de egreso**, igual que en los pases 6, 7, 14, 16, 17 y 18 — **PrivacyCD (arXiv 2511.03966)** y **P-MIA (arXiv 2511.04716)** se registran por **snippets concordantes**, con su número anotado para que el próximo pase los abra, **no para citarlos ante un cliente**. **`moodle.org` también sigue bloqueado**: `local_gdpr_deleteuserdata` (GPL-3.0, 2018-07-08, Moodle 3.5) **no se verificó de primera mano y no se localizó repositorio en GitHub** — se registra como antecedente de diseño, no como dependencia. La **API de borrado de Learning Locker** viene de fuente secundaria y **no se verificó contra su API**: es la acción 1 que este pase deja escrita.*


Privacidad del dato en el LMS instalado y canal de *skills* — pase 17 (2026-10-01), repos verificados vía WebFetch: [edx-platform](https://github.com/openedx/edx-platform) y su [scripts/user_retirement](https://github.com/openedx/edx-platform/tree/master/scripts/user_retirement) y [lms/djangoapps/bulk_user_retirement](https://github.com/openedx/edx-platform/tree/master/lms/djangoapps/bulk_user_retirement) · [moodle](https://github.com/moodle/moodle) · [canvas-lms](https://github.com/instructure/canvas-lms) · [openeducat_erp](https://github.com/openeducat/openeducat_erp) · [k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) · [learning-commons-org/agent-skills](https://github.com/learning-commons-org/agent-skills) · [DeepTutor](https://github.com/HKUDS/DeepTutor) · [education-agent-skills](https://github.com/GarethManning/education-agent-skills)

Regulación y incidentes — pase 17: **California AB 1159 / HESIPA** (firmada 2026-09-13; [comunicado de la oficina de la asambleísta Addis](https://addis.asmdc.org/press-releases/20260910-addis-bill-bolstering-student-data-protection-signed-law), [análisis del comité APCP](https://apcp.assembly.ca.gov/system/files/2026-01/ab-1159-addis-apcp-analysis.pdf), [Golden Data](https://medium.com/golden-data/ab-1159-extending-student-data-privacy-protections-to-higher-education-8676161660e1), [Captain Compliance](https://captaincompliance.com/education/california-ab-1159-a-landmark-student-privacy-bill-that-fixes-the-past-while-struggling-to-catch-the-present/)) · **COPPA enmendada, precisión del pase 17** ([Finnegan](https://www.finnegan.com/en/insights/articles/the-ftcs-updated-coppa-rule-redefining-childrens-digital-privacy-protection.html), [National Law Review](https://natlawreview.com/article/ftc-publishes-final-coppa-rule-amendments), [promise.legal](https://blog.promise.legal/coppa-april-2026-amendments-edtech/)) · **incidente Instructure/Canvas** abril–mayo 2026 ([TechRepublic](https://www.techrepublic.com/fr/article/news-canvas-breach-hackers-deal-275m-records-stolen/), [JD Supra](https://www.jdsupra.com/legalnews/client-alert-instructure-data-breach-7807251/), [Nasdaq](https://www.nasdaq.com/articles/canvas-parent-instructure-hit-cyberattack)) · **Anexo III del AI Act diferido al 2027-12-02** ([Reed Smith](https://www.reedsmith.com/our-insights/blogs/technology-law-dispatch/102nfi5/eu-ai-act-next-level-applies-as-of-2-august-2026/), [sota.io para EdTech](https://sota.io/blog/eu-ai-act-edtech-educational-software-developer-compliance-2026)) · **gobernanza de AI en educación en EE. UU.** ([informe Kiteworks 2026](https://www.kiteworks.com/sites/default/files/resources/kiteworks-report-education-ai-governance-data-security-compliance-2026-report.pdf), [MultiState: cómo los estados regulan la AI en educación](https://multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session)) · **adopción LATAM** ([Digital Education Council, encuesta LATAM 2026](https://www.digitaleducationcouncil.com/post/92-of-students-and-79-of-faculty-actively-engaging-with-ai-findings-from-ai-in-higher-education-latam-survey-2026)) · **directrices éticas de la Comisión Europea para docentes** ([BABL AI](https://babl.ai/european-commission-updates-ai-ethics-guidelines-to-help-teachers-navigate-ai-and-data-use-in-schools/))

⚠️ *Del pase 17: **`moodle.org`, `docs.moodle.org`, `docs.openedx.org`, `privacyrights.org`, `calmatters.org` y `leginfo.legislature.ca.gov` están bloqueados por el proxy de egreso.** En consecuencia: (a) la cita «User retirement is not a compliance guarantee…» viene de **snippet de búsqueda**, no de fetch de primera mano, y el `README` del directorio en GitHub no la contiene; (b) el **Privacy API de Moodle**, `tool_dataprivacy` y `tool_policy` están **documentados por Moodle vía snippet**, no verificados de primera mano —el árbol de `admin/tool/dataprivacy` dio 404 por cuatro rutas distintas—; (c) **AB 1159** no se leyó en la fuente legislativa oficial: fechas, autoría y texto de la prohibición provienen de múltiples fuentes concordantes. **`curl -sI` devolvió 403 incluso para un repo deliberadamente inexistente**, así que no verifica nada en esta sesión; ver la nota de método del pase 17.*

Privacidad y datos del alumno — pase 16 (2026-10-01), repos verificados vía WebFetch: [PySyft](https://github.com/OpenMined/PySyft) · [Flower](https://github.com/adap/flower) · [OpenFL (deprecado)](https://github.com/securefederatedai/openfl) · [Google DP](https://github.com/google/differential-privacy) · [Opacus](https://github.com/pytorch/opacus) · [TensorFlow Privacy](https://github.com/tensorflow/privacy) · [diffprivlib](https://github.com/IBM/differential-privacy-library) · [OpenDP](https://github.com/opendp/opendp) · [synthcity](https://github.com/vanderschaarlab/synthcity) · [ydata-synthetic](https://github.com/ydataai/ydata-synthetic) · [SDV](https://github.com/sdv-dev/SDV) y su [LICENSE (BUSL 1.1)](https://github.com/sdv-dev/SDV/blob/main/LICENSE) · [PrivGen](https://github.com/Akulen/PrivGen) · [FedGKT](https://github.com/TarunRaina/FedGNN-for-Personalized-Knowledge-Tracing) · [federated-deep-knowledge-tracing](https://github.com/hxwujinze/federated-deep-knowledge-tracing) · [SynEdu-HEDL](https://github.com/drsanjayagal/SynEdu-HEDL)

Regulación de privacidad educativa — pase 16: COPPA enmendada ([White & Case](https://www.whitecase.com/insight-alert/unpacking-ftcs-coppa-amendments-what-you-need-know), [Privacy & Data Security Insight](https://www.privacyanddatasecurityinsight.com/2026/04/enforcement-begins-soon-for-significant-coppa-rule-amendments/)) · FERPA y AI ([AFS Law](https://www.afslaw.com/perspectives/ai-law-blog/the-development-ai-and-protecting-student-data-privacy)) · DPDP Act India ([ORF](https://www.orfonline.org/research/governing-learner-data-risks-in-india-the-dpdp-act-and-the-case-for-edtech-specific-regulation), [medianama](https://www.medianama.com/2026/09/223-microsoft-student-data-ai-training-schools-india/)) · Brasil: Referencial do MEC ([O Tempo](https://www.otempo.com.br/educacao/2026/3/13/mec-recomenda-veto-de-ia-na-educacao-infantil-e-desaconselha-reconhecimento-facial-nas-escolas), [Jeduca](https://jeduca.org.br/noticia/ia-na-educacao-entenda-o-novo-referencial-do-mec-e-pontos-de-atencao)), ANPD y biometría en Paraná ([Data Privacy Brasil](https://www.dataprivacybr.org/anpd-suspende-o-uso-de-reconhecimento-facial-em-escolas-publicas-do-parana/), [Convergência Digital](https://convergenciadigital.com.br/governo/anpd-exige-suspensao-imediata-do-tratamento-de-dados-biometricos-na-frequencia-escolar-no-parana/)), LGPD na educação ([Confidata](https://confidata.com.br/blog/lgpd-educacao-2026-impacto-eca-digital))

⚠️ *Del pase 16: se abrieron de primera mano sólo los enlaces a `github.com`. **`nature.com` y `arxiv.org` están bloqueados por el proxy de egreso**, así que el paper de `SynEdu-HEDL` (Scientific Reports `s41598-026-44990-8`) y el de síntesis por cópulas (`arXiv 2604.04195`) **no se verificaron de primera mano**. El `Referencial` del MEC se leyó vía cobertura periodística, no desde el PDF oficial. `curl -sI` devolvió **403 en los catorce repos consultados** — ninguno era un 404; ver la nota de método del pase 16.*


Nuevo en el pase 15 — capa de marcado y procedencia (verificado vía WebFetch el 2026-10-01): [SynthID-Text en transformers](https://github.com/huggingface/transformers/blob/main/src/transformers/generation/watermarking.py) · [MarkLLM](https://github.com/THU-BPM/MarkLLM) · [c2pa-rs](https://github.com/contentauth/c2pa-rs) · [c2pa-python](https://github.com/contentauth/c2pa-python)

Nuevo en el pase 15 — capa de detección forense (verificado vía WebFetch el 2026-10-01): [fast-detect-gpt](https://github.com/baoguangsheng/fast-detect-gpt) · [Binoculars](https://github.com/ahans30/Binoculars) · [RAID](https://github.com/liamdugan/raid) · [LLM-generated-Text-Detection (survey)](https://github.com/NLP2CT/LLM-generated-Text-Detection) · [sloptotal](https://github.com/pablocaeg/sloptotal) · [awesome-ai-detection](https://github.com/Lendarixon/awesome-ai-detection) · [detectoria (sin licencia)](https://github.com/yonatanlop/detectoria) · [humanizar-es (evasión, skill de agente)](https://github.com/ervin-mo/humanizar-es)

Nuevo en el pase 15 — Artículo 50 y Code of Practice de marcado (⚠️ **todo de fuentes secundarias: los dominios oficiales están bloqueados por el proxy**, y las dos primeras discrepan en la fecha de publicación del Code of Practice —10 de junio vs. 20 de julio de 2026—): [IPTC — European AI Office releases Code of Practice on Transparency of AI-Generated Content](https://iptc.org/news/eu-ai-transparency-code-of-practice-june-2026/) · [Lewis Silkin — the EU's new AI labelling rules](https://www.lewissilkin.com/insights/2026/07/24/the-eus-new-ai-labelling-rules-what-every-organisation-needs-to-know-102ne35) · [Paul Weiss — EU finalises transparency rules for AI-generated content](https://www.paulweiss.com/insights/client-memos/eu-finalises-transparency-rules-for-ai-generated-content) · [artificialintelligenceact.eu — guía del Artículo 50 (🔴 bloqueado, no abierto)](https://artificialintelligenceact.eu/transparency-rules-article-50/)

Nuevo en el pase 15 — abandono institucional de la detección: [Más de 50 universidades desactivaron la detección de AI de Turnitin](https://www.aiplagguides.com/blog/universities-disabling-turnitin-ai-detection) · [Diplo — universidades dejan de usar detectores](https://www.diplomacy.edu/updates/universities-stop-using-ai-detection-tool-such-as-turnitin/) · [GPT detectors are biased against non-native English writers (🔴 arxiv bloqueado, citado vía resultados de búsqueda)](https://arxiv.org/html/2304.02819)

Nuevo en el pase 15 — integridad académica en LATAM: [Infobae — México, Colombia y Chile: declaración obligatoria del uso de AI](https://www.infobae.com/educacion/2025/08/26/las-claves-de-mexico-colombia-y-chile-para-incorporar-a-la-inteligencia-artificial-en-la-universidad/) · [Educación y Tecnología — IA en la educación en México 2026](https://educacionytecnologia.com/inteligencia-artificial-educacion-mexico-estudio-2026/) · [UNESCO ESS — autoría e integridad académica ante la IA generativa](https://ess.iesalc.unesco.org/index.php/ess3/article/view/1174) · [Zenodo — políticas de integridad de las 15 universidades LATAM mejor rankeadas en THE 2026 (🔴 bloqueado, licencia sin verificar)](https://zenodo.org/records/22661179)

Nuevo en el pase 15 — plugins de integridad en Moodle (envoltorios de servicios propietarios; ⚠️ **`moodle.org` está bloqueado por el proxy: licencia, instalaciones y fechas de release provienen de resultados de búsqueda, no de la página del directorio**): [Compilatio (plugin GPL-3.0)](https://moodle.org/plugins/plagiarism_compilatio) · [Copyleaks](https://moodle.org/plugins/plagiarism_copyleaks) · [Originality.ai](https://marketplace.moodle.com/plugins/plagiarism_origai)

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

## Nota de método del pase 19 (2026-10-01) — el pase que ejecutó las dos acciones escritas, y las dos dieron "no" (que es un resultado)

Tres pases consecutivos ejecutaron acciones escritas por el anterior. Éste también, y es **el primero en el que las
dos devuelven negativo** — una refutada y una no encontrada. Las dos se registran como hallazgo, porque un negativo
medido con control es información y el silencio se parece demasiado a la cobertura.

### Acción 1 — «buscar si PrivacyCD publicó código (gap 31)» → **NO. Gap 31 sigue abierto, con la búsqueda documentada**

Se buscó por los términos que el pase 18 dejó escritos. **Lo que confirmó:** la autoría completa (Mingliang Hou,
Yinuo Wang, Teng Guo, Zitao Liu, Wenzhou Dou, Jiaqi Zheng, Renqiang Luo, Mi Tian, Weiqi Luo — los tres nombres que el
pase 18 anticipó están en la lista) y el algoritmo **HIF** (*hierarchical importance-guided forgetting*: explota que
la importancia de parámetros en un CDM tiene estructura por capas, con suavizado que combina importancia individual y
de capa; experimentos sobre tres datasets reales). **Lo que no apareció: código.** Ni repo localizable ni enlace en
los resultados.

**Y la búsqueda devolvió algo que no se buscaba, que es el verdadero aporte de esta acción:** **P-MIA** (arXiv
2511.04716), del mismo grupo — el **ataque** correspondiente al **defensa** de PrivacyCD. Los dos lados del mismo
problema, publicados por el mismo entorno, **y ninguno de los dos libera implementación**. Ver la tendencia **50**.

### Acción 2 — «medir el disparador del gap 32 por el lado del evento» → **REFUTADA. La hipótesis era al revés, y el gap 32 se cierra**

El pase 18 llamó a esto *«la hipótesis más barata que esta KB tiene abierta»*: que el Privacy API **emite un evento al
aprobar un pedido** y que, si es observable, el puente es un `db/events.php` de diez líneas. **Se midió sobre el árbol
real y es falso.** Verificado con clon *sparse* de `moodle/moodle` en `main` (= 5.3rc1):

- `public/admin/tool/dataprivacy/db/events.php` registra **exactamente un** observer, y va **hacia adentro**: escucha
  `\core\event\user_deleted` para **crear** un pedido de borrado
  (`user_deleted_observer::create_delete_data_request`, y sólo si la config `automaticdeletionrequests` está activa).
  **Es el sentido contrario al que hacía falta.**
- **`tool_dataprivacy` no emite ningún evento.** Recorridos los **187 archivos** del subárbol: **cero** llamadas a
  `trigger()`.
- `api::update_request_status()` —por donde pasa `approve_data_request()`— es **una escritura de base de datos y nada
  más**: setea `status`, opcionalmente `dpo` y `dpocomment`, y llama a `$datarequest->update()`. **Sin evento, sin
  hook, sin notificación.**

**Control negativo, porque la conclusión es una ausencia:** el mismo `api.php` tiene **1.678 líneas** y
`approve_data_request()` está en la **línea 642**. El archivo existía y el grep era válido; **la ausencia es real, no
un error de ruta** — que es precisamente el error que este pase tuvo que corregirle al anterior.

**El gap 32 se cierra refutado, y deja dos caminos** (ver **P40**): **(a)** sondear `tool_dataprivacy_request.status`,
la única superficie observable que existe, o **(b)** disparar desde afuera, como hace el único antecedente conocido,
**`local_gdpr_deleteuserdata`** (GPL-3.0, expone el borrado del Privacy API como web-service). ⚠️ Antecedente, **no
dependencia**: es de **2018-07-08**, declara requerir **Moodle 3.5** —el núcleo va por 5.3—, `moodle.org` está
bloqueado por el proxy y **no se localizó repositorio en GitHub**.

### Lo que se verificó de primera mano, y con qué herramienta

Este pase cambió de instrumento, y conviene dejar escrito por qué: **WebFetch infiere, `git` lista.** Preguntado por
la rama por defecto de `moodle/moodle`, WebFetch contestó «main» leyendo la página renderizada — y acertó por
casualidad, porque la misma consulta sobre rutas devolvió dos 404 que no significaban ausencia.

- ✅ **`git ls-remote --heads`** sobre `moodle/moodle`: `refs/heads/main` → `85af0b5`. **Lista refs, no infiere.** Es
  la herramienta correcta para la pregunta de la rama y cuesta un segundo.
- ✅ **Clon `--depth 1 --filter=blob:none --sparse`** de `moodle/moodle`: el árbol real, `main` = **Moodle 5.3rc1**.
  Sobre él se auditaron los 10 archivos de privacidad, los 7 shims (línea por línea), `core_ai` (~800 líneas),
  `db/events.php`, `api.php` y los 187 archivos de `tool_dataprivacy`.
- ✅ **WebFetch** sobre los repos de GitHub: licencia, estrellas, commits y descripción de los 5 agentes nuevos,
  OpenUnlearning, `MachineUnlearning`, `torchunlearn`, `jjbrophy47/machine_unlearning`, Ralph, `lrsql` y Learning
  Locker.

### ⚠️ Advertencia 1 — un 404 nunca dice «no existe»; dice «no está donde preguntaste». Tercera vez.

El pase 17 leyó sus 404 como **ausencia de la pieza**. El pase 18 los leyó como **nombre de rama** y escribió una
afirmación falsa (*«`moodle/moodle` no tiene rama `main` ni `master`»*). La causa real era una **tercera**: Moodle
movió su *webroot* a **`public/`** en la serie 5.x, así que en `main` la ruta es `public/ai/...` y no `ai/...`. Los
mismos 404 del pase 18 son consistentes con esto: 404 en `main` (ruta movida) y 200 en `MOODLE_405_STABLE` y
`MOODLE_500_STABLE`, donde `ai/` todavía estaba en la raíz. **Su tabla de evidencia era correcta; su explicación no.**

**Dos consecuencias operativas, para no repetirlo:**

1. **Toda ruta de Moodle que esta KB escriba tiene que decir contra qué serie se resolvió.** La 5.x las movió todas.
2. **Dos de los tres «404 = no está en el núcleo» del pase 18 medían un nombre, no una ausencia:** `anthropic` **sí**
   está, y `bedrock` se llama **`awsbedrock`**.

### ⚠️ Advertencia 2 — «la oferta es grande» se midió con los repos equivocados, y el error es de tamaño, no de signo

El pase 18 cerró la capa de *unlearning* con *«la oferta existe, es grande y es toda MIT/Apache»*. La conclusión es
correcta; la medición no. **Sus dos piezas ejecutables tienen 12 ★ cada una**, y lo que tenía cientos de estrellas
(`jjbrophy47/machine_unlearning`, 965 ★, reverificado: **sigue sin licencia**) es una **bibliografía**. La pieza seria
de la capa —**OpenUnlearning**, MIT, **607 ★**, CMU, con TOFU/MUSE/WMDP y métricas de *membership inference*— **no
estaba registrada en esta KB**. Lección: **contar estrellas sin separar código de bibliografía produce una conclusión
correcta por accidente**, y la próxima vez puede producir una incorrecta.

### ⚠️ Advertencia 3 — el barrido regional sigue saturado, y esta vez hay un dato nuevo igual

El pase 12 declaró saturación del barrido regional y el pase 17 la confirmó. Este pase la confirma otra vez: las
cuatro consultas regionales devolvieron **cifras que la KB ya tenía** (134 proyectos en 31 estados, 92 %/79 % del
Digital Education Council, Reglamento (UE) 2026/1744 con el Anexo III en 2027-12-02, AB 1159). **Se registra como
confirmación, no como hallazgo.** Lo único genuinamente nuevo es **APAC**, y es preciso: la **Ley de IA de Vietnam
N.º 134/2025/QH15** y su **Decisión 33** (ver `intel/market.md`). La KB tenía la clasificación de Vietnam en términos
generales desde el pase 5; no tenía **el instrumento, los tres incisos ni las dos fechas de cumplimiento**.

### Lo que este pase NO hizo, declarado como tal

- **No se leyó ningún paper en fuente primaria.** `arxiv.org` sigue bloqueado por el proxy, igual que en los pases 6,
  7, 14, 16, 17 y 18. **P-MIA (2511.04716) y PrivacyCD (2511.03966) vienen de snippets concordantes** y se anotan con
  su número **para que el próximo pase los abra**, no para citarlos ante un cliente.
- **No se verificó la API de borrado de Learning Locker.** El «sí» viene de una fuente secundaria (Learning Pool). Es
  el único «sí» de la tabla del gap 33 y **es el que más conviene confirmar**, porque es el que decide si la única
  salida de la capa de telemetría es copyleft.
- **No se probó el sondeo de `tool_dataprivacy_request`.** P40 describe el mecanismo leyendo el esquema y el flujo de
  `update_request_status()`; **no se ejecutó contra una instancia de Moodle**. Es diseño verificado en el fuente, no
  integración probada.
- **No se verificó `local_gdpr_deleteuserdata` de primera mano** ni se localizó su repositorio. `moodle.org` sigue
  bloqueado y el directorio oficial de plugins sigue sin auditarse — es la cuarta pasada consecutiva con esta misma
  limitación.
- **No se auditó el árbol de `canvas-lms`.** Cuarta pasada que lo declara **no buscado, no inexistente**.
- **No se verificó archivo por archivo la doble licencia de `human-skill-tree`.** El repo declara AGPL-3.0 con el
  directorio `skills/` en doble MIT/AGPL; **eso se tomó del README**, y antes de facturar hay que leer los encabezados
  del subárbol.

### 🔵 Las tres acciones que este pase deja escritas para el siguiente

1. **Confirmar la API de borrado de Learning Locker** (gap 33). Es la pregunta de mayor rendimiento del pase: si el
   «sí» se confirma, la única forma estándar de borrar telemetría de aprendizaje es **GPL-3.0**, y eso es una
   restricción de arquitectura que hay que decirle al cliente **antes** de elegir LRS. Buscar por
   `learninglocker statement delete API`, por su documentación de administración y por el repo de `xapi-service`.
2. **Construir el *harness* del gap 34**, que es lo más construible que tiene esta KB y no requiere investigación:
   tomar `pyKT` (MIT, PyTorch), aplicarle un método de `torchunlearn` (MIT) y **medirlo con las métricas de
   *membership inference* de OpenUnlearning** (MIT). Las tres piezas son permisivas y ya existen. El entregable es el
   número que hoy **P38** no puede prometer.
3. **Abrir P-MIA (2511.04716) y PrivacyCD (2511.03966) en fuente primaria** si algún pase consigue `arxiv.org`, o
   buscar sus versiones en otro alojamiento. La tendencia 50 sostiene una recomendación de diseño —ruido o
   cuantización en el vector de estado expuesto— sobre **snippets**, y esa recomendación va a llegar a una propuesta.
## Nota de método del pase 18 (2026-10-01) — el tercer pase que ejecuta acciones escritas, y el primero que descubre que una ausencia de la KB era un error de rama

Este pase ejecutó **las dos acciones** que el pase 17 dejó escritas, y las dos dieron resultado. Conviene registrar
que es el tercer pase consecutivo donde una acción escrita por el pase anterior se convierte en hallazgo verificado
(pases 14, 17 y 18): **el mecanismo de dejar acciones textuales está funcionando** y vale protegerlo.

### Acción 1 — «construir y medir el `privacy provider` de referencia para un plugin de AI de Moodle (gap 29)»

No hubo que construirlo. **Existe, y son tres, y están en el núcleo de Moodle.** Lo que este pase sí tuvo que hacer
fue entender **por qué el pase 17 no los encontró**, y la respuesta es mecánica y reutilizable: **`moodle/moodle` no
tiene rama `main` ni `master`**. Los cuatro 404 que el pase 17 registró con honestidad midieron el nombre de la
rama, no una ausencia.

### Acción 2 — «buscar procedencia por los términos del dominio de ML; `machine unlearning` es el término que este pase no buscó»

Se buscó y **la predicción del pase 17 se cumplió literalmente**: hay una capa de 2.700+ ★, toda MIT/Apache-2.0, y
contiene librerías aplicables a *knowledge tracing*. El gap 30 cambia de forma, como el pase 17 anticipó, y se
reformula en los **gaps 31 y 32**.

### Lo que se verificó de primera mano

1. **Siete rutas de `moodle/moodle` probadas por código HTTP** contra `raw.githubusercontent.com` en cuatro ramas
   (`main`, `master`, `MOODLE_405_STABLE`, `MOODLE_500_STABLE`). De ahí sale la corrección del pase 17 y el cierre
   del gap 29.
2. **Tres `privacy provider` leídos en el archivo fuente crudo**, no en la página rendida: el del núcleo
   (`aiprovider_openai`), el de Ferrara (`aiprovider_gemini`) y el brasileño (`local_aihub`). Se leyeron las
   declaraciones de clase, las interfaces, los nombres de método y el contenido de `get_metadata()`.
3. **Las cadenas de idioma de privacidad de `aiprovider_openai` y `aiprovider_ollama`**, citadas literal. De ahí
   sale la lectura de la palabra «explicitly», que es el aporte más accionable del pase para un expediente de
   cliente.
4. **`classes/privacy/` abierto en seis repos de la comunidad** para contar cuántos tienen `provider.php`: tres sí,
   tres no.
5. **Nueve repos de la capa de *unlearning* y procedencia** abiertos uno por uno para licencia, estrellas, forks y
   condición de fork.

### ⚠️ Advertencia 1 — la página rendida contradijo al fuente, y el fuente ganó

El resumen de la página de `Universita-di-Ferrara/moodle-aiprovider_gemini` afirmaba que **todos** los métodos del
provider estaban vacíos y que por tanto el plugin **no declaraba** el envío externo a Google. **Eso iba a escribirse
como el hallazgo del pase**: un defecto de cumplimiento en una pieza universitaria europea. **Leyendo el `.php`
crudo, el plugin declara `add_external_location_link` con cuatro campos** (`prompttext`, `model`, `numberimages`,
`responseformat`) y un propósito. La afirmación habría sido **falsa y acusatoria**.

**La regla que queda:** para una afirmación de **cumplimiento** —positiva o negativa— se lee el fuente, no el
resumen de la página. Es la tercera variante del mismo problema de método en esta KB (pase 10: README vs `LICENSE`;
pase 16: sidebar vs archivo de licencia; ahora: página rendida vs fuente).

### ⚠️ Advertencia 2 — el primer resultado de búsqueda fue un fork con 0 estrellas

Buscando `open-unlearning` el primer resultado fue **`aflah02/open-unlearning`**: README idéntico, licencia
idéntica, misma lista de métodos, **0 ★ y 0 forks**. El canónico es **`locuslab/open-unlearning`, 607 ★ y 164
forks**. Lo único que distingue a uno del otro es el campo «forked from» y el contador. **Ningún repo entra a una
tabla de esta KB sin mirar si es fork** — es el mismo error que el pase 7 cometió con MRBench.

### ⚠️ Advertencia 3 — el tercer lugar donde puede estar la licencia

`alvarogregori/moodle-ai-graded-assignment` **no tiene archivo `LICENSE`, no muestra licencia en el sidebar y no la
menciona en el README** — y el header de cada `.php` declara GPL-3.0-or-later. Para un plugin de Moodle es lo
esperable, pero **un header de archivo no es una concesión de licencia del repositorio**. Regla operativa: **sin
`LICENSE`, se trata como sin licencia a efectos de cotización.**

### Lo que este pase NO hizo, declarado como tal

- **No se auditó el árbol de `canvas-lms`.** Igual que el pase 17, la ausencia de un toolset de retiro comparable
  se declara **no encontrada, no inexistente**.
- **`jjbrophy47/machine_unlearning` (965 ★) y `Awesome-Diffusion-Model-Unlearning` (67 ★) no muestran licencia.**
  Se abrieron y se confirmó que existen y que **ninguno declara licencia** — están en las tablas como *sin licencia
  declarada*, usables como bibliografía y no como dependencia. Lo que corresponde es un *issue* pidiendo el archivo.
- **No se leyó ningún paper en la fuente primaria.** `arxiv.org` está bloqueado por el proxy. Todo lo que se afirma
  de PrivacyCD, SalUn, torchunlearn y la survey de ACM TIST viene de **snippets concordantes**. Los números de
  arXiv se registran para que el próximo pase los abra, no para citarlos ante un cliente.
- **No se probó `torchunlearn` sobre `pyKT`.** La afirmación de que es «aplicable en principio» se basa en que
  ambos son PyTorch, **no en una integración ejecutada**. P38 lo dice en su advertencia en vez de prometer que
  funciona.
- **No se buscó jurisprudencia ni sanciones aplicadas** sobre el derecho de supresión aplicado a modelos. Se
  registró qué exige cada régimen, no cómo se está aplicando.
- **No se revisó el directorio de plugins de Moodle**: `moodle.org` sigue bloqueado. El conteo de seis piezas de la
  comunidad es de lo encontrado en GitHub, no del directorio oficial.

### 🔵 Las dos acciones que este pase deja escritas para el siguiente

1. **Buscar si PrivacyCD publicó código** (gap 31). Buscar por `HIF unlearning cognitive diagnosis`, por los
   nombres de los autores (**Zitao Liu**, **Weiqi Luo**, **Teng Guo** — el mismo grupo publica herramienta open
   source con frecuencia) y por la organización de `pyKT`, que es del mismo entorno. **Si aparece, P38 mejora y el
   gap 31 se cierra.** Si no aparece, verificar las licencias pendientes de `jjbrophy47/machine_unlearning` y
   abrir *issues* de licencia en `mod_aigradedassign` y `tool_aiconnect`.
2. **Medir el disparador del gap 32 por el lado del evento, no del borrado.** Este pase buscó «quién borra el
   modelo» y no encontró puente. La próxima consulta tiene que ser por el **mecanismo de evento de Moodle**:
   `moodle event observer privacy delete`, `core_privacy delete_data_for_user hook external`, y por el lado del
   LRS, `xAPI delete statements forget`. El Privacy API **emite un evento al aprobar un pedido**, y si ese evento
   es observable, el gap 32 deja de ser investigación y pasa a ser un `db/events.php` de diez líneas. **Esa es la
   hipótesis más barata que esta KB tiene abierta.**

## Nota de método del pase 17 (2026-10-01) — el segundo pase que ejecuta una acción escrita por un gap anterior, y van dos de dos

El pase 14 dejó registrado que **no tuvo que inventar la pregunta**: el gap 19 se la había dejado escrita, y
cerrarla funcionó. Este pase repitió el método **con dos acciones escritas a la vez**, y las dos pagaron:

1. **La del gap 26 (pase 15):** *«medir el canal otra vez, pero buscando por `SKILL.md` + dominio educativo en
   vez de por repos educativos».* Resultado: **el gap 20 se cerró** y el techo permisivo del canal educativo pasó
   de 299 a 541 ★.
2. **La del cierre del pase 16:** *«No se revisó la capa de privacidad de los LMS ya instalados (Moodle, Open
   edX, Canvas). Es el paso siguiente obvio: el dato del alumno ya está ahí, no en el agente.»* Resultado: una
   **capa nueva** y dos gaps nuevos (29 y 30).

**La conclusión de método, y ya tiene tres pasadas de evidencia (14, 17 y el fracaso relativo de las que
inventaron la pregunta):** cuando un gap deja escrita una acción concreta, ejecutarla rinde más que abrir una capa
nueva por intuición. **Conviene que cada pase cierre dejando una acción textual**, y este pase deja dos, abajo.

### Lo que se verificó de primera mano

Vía **WebFetch contra la página del repo** el 2026-10-01: `openedx/edx-platform` (AGPL-3.0, 8.2k ★, 4.4k forks) y
su árbol `scripts/user_retirement` (seis scripts leídos por nombre) y `lms/djangoapps/bulk_user_retirement` ·
`moodle/moodle` (GPL-3.0, 7.5k ★, 123.147 commits) · `instructure/canvas-lms` (AGPL-3.0, 6.9k ★) ·
`openeducat/openeducat_erp` (LGPL-3.0, 881 ★) · `anthropics/k12-teacher-skills` (Apache-2.0, 541 ★, `evals/`) ·
`learning-commons-org/agent-skills` (Apache-2.0, 35 ★, `evals/`) · `HKUDS/DeepTutor` (Apache-2.0, **40.6k ★**,
v1.6.12 del **2026-09-27** — **la fila de la KB ya estaba correcta**).

### ⚠️ Advertencia 1 — `curl -sI` no verifica nada en esta sesión, y ahora está probado con control negativo

El pase 16 anotó que `curl -sI` devolvió 403 en catorce repos y que ninguno era un 404. **Este pase lo probó
bien:** se consultaron tres repos reales (`instructure/canvas-lms`, `openedx/edx-platform`, `moodle/moodle`) y
**uno deliberadamente inexistente** (`github.com/this-definitely-does-not-exist-xyz123/nope`). **Los cuatro
devolvieron 403.** El proxy responde antes de llegar a GitHub, así que **un 403 no distingue un repo vivo de uno
que no existe** y `curl` no puede usarse para cumplir la regla de «verificar toda URL». La verificación válida en
esta sesión es **WebFetch contra la página del repo**. Dejar de intentar `curl` ahorra tiempo en cada pase.

### ⚠️ Advertencia 2 — seis dominios bloqueados, y dos afectan a citas que van a una propuesta

Bloqueados por el proxy de egreso en este pase: **`moodle.org`**, **`docs.moodle.org`**, **`docs.openedx.org`**,
**`privacyrights.org`**, **`calmatters.org`** y **`leginfo.legislature.ca.gov`**.

Las dos consecuencias que importan:

- **La cita de Open edX** (*«User retirement is not a compliance guarantee…»*) se leyó en el **snippet de
  búsqueda** de `docs.openedx.org`, **no en un fetch de primera mano**, y el `README` del directorio en GitHub
  —que sí se verificó— **no la contiene**. Se usa en tres archivos de esta KB: resolver contra la fuente oficial
  antes de ponerla en un documento para un cliente.
- **El Privacy API de Moodle, `tool_dataprivacy` y `tool_policy`** quedan registrados como **documentados por
  Moodle vía snippet**, no verificados de primera mano. Se intentó el árbol de `admin/tool/dataprivacy` por
  **cuatro rutas** (`main` y `master`, árbol y archivo) y **las cuatro dieron 404 vía WebFetch**. Del repo se
  verificó licencia, estrellas y commits.
- **AB 1159** no se pudo leer en `leginfo.legislature.ca.gov` ni en las dos fuentes de la organización
  patrocinante. Fechas, autoría, el texto de la prohibición y la vigencia de HESIPA provienen de **búsqueda
  extendida con múltiples fuentes concordantes** (incluido el comunicado de la oficina de la asambleísta), no de
  la fuente legislativa oficial. **Antes de citar la ley en un contrato, leer el texto chaptered.**

### ⚠️ Advertencia 3 — dos correcciones de este pase son sobre la propia KB, no sobre el mercado

- **El conteo de `agents/top.md`.** El encabezado dice 31 y la tabla tiene **32 filas**. No es un error nuevo: es
  la tercera vez que esta KB se pelea con este conteo (ver la corrección del pase 10). **La reconciliación es que
  una fila no es un agente:** `education-agent-skills` es una biblioteca de Markdown/YAML y está además en la capa
  de distribución por *skills* del mismo archivo. **32 filas = 31 agentes + 1 duplicado de otra capa.**
- **El encuadre COPPA del pase 16.** *«La voz de un menor es dato biométrico regulado desde el 2026-04-22»* tiene
  la conclusión correcta y la vía equivocada: la FTC **excluyó explícitamente** de la regla final los datos
  *derivados* de voz, rostro y marcha (estaban en el NPRM de 2024 y se quitaron por amplitud excesiva), mientras
  **`voiceprints` sí está en la enumeración**. Y un **archivo de audio con la voz de un chico ya estaba cubierto
  bajo 16 CFR 312.2 antes de las enmiendas** — la exposición es **más vieja**, no más nueva. Ver la corrección
  completa en `agents/top.md`.

### Lo que este pase NO hizo, declarado como tal

- **No se auditó el árbol de `canvas-lms`.** La ausencia de un toolset de retiro comparable al de Open edX se
  declara como **no encontrada**, no como inexistente.
- **No se verificó si `learning-commons-org/agent-skills` tenía `evals/` al momento del pase 12.** No se pudo
  datar la carpeta. Por eso el cierre del gap 20 registra la duda en vez de culpar al pase 12 o absolverlo.
- **No se midió el costo de cumplir AB 1159 sobre una arquitectura federada.** Se sabe que la excepción de la ley
  y el federado encajan conceptualmente; **cuánto cuesta producir la evidencia nadie lo midió acá**, y P37 lo dice
  en su advertencia en vez de prometer números.
- **No se buscó jurisprudencia ni sanciones aplicadas** — igual que el pase 16, se registró qué exige cada régimen
  y desde cuándo, no cómo se está aplicando.
- **No se revisó el directorio completo de plugins de Moodle.** `moodle.org` está bloqueado; lo que se afirma del
  ecosistema de plugins viene de snippets.

### 🔵 Las dos acciones que este pase deja escritas para el siguiente

1. **Construir y medir el `privacy provider` de referencia** para un plugin de AI de Moodle (gap 29). Es la pieza
   más chica de la capa, el núcleo la **exige** a todos los plugins, y no existe publicada. Buscar primero
   `moodle privacy provider ai plugin` y `moodle local plugin privacy provider example` antes de darla por
   inexistente.
2. **Buscar procedencia de dato de entrenamiento** (gap 30) por los términos del dominio de ML, no de educación:
   `training data provenance`, `dataset attestation`, `model card training data lineage`, `machine unlearning`.
   **`machine unlearning` es el término que este pase no buscó** y es el que podría tener oferta madura: si existe
   una librería permisiva de *unlearning* aplicable a modelos de knowledge tracing, el gap 30 cambia de forma.

## Nota de método del pase 16 (2026-10-01) — dieciséis pasadas preguntando qué sabe hacer el software, y la pregunta que faltaba era con qué derecho toca al alumno

Este pase no buscó una tecnología: buscó un **régimen**. El disparador fue medir el vocabulario de la propia KB
antes de investigar nada, sobre los ocho archivos:

| Término buscado | Apariciones antes del pase 16 |
|---|---|
| `COPPA` | **0** |
| `differential privacy` / `privacidad diferencial` | **0** |
| `federated` / `federado` | **0** |
| `FERPA` | **1**, de pasada, dentro de la descripción de un repo de otra capa |
| `sintétic` | 10, **todas como crítica** a un repo de la capa predictiva, ninguna como capacidad |

Quince pasadas y cinco de los seis términos que definen el tratamiento legal del dato de un menor no aparecían.
Ese conteo es el hallazgo del pase tanto como los repos.

### Lo que se verificó de primera mano

1. **Quince repos abiertos uno por uno vía WebFetch** para licencia, estrellas, forks, commits y lenguaje. Dos
   licencias **no estaban en el sidebar de GitHub y hubo que abrir el archivo**: `diffprivlib` (`LICENSE.md` →
   «MIT License», IBM Corporation 2018) y `SDV` (`LICENSE` → «Business Source License 1.1», licenciante DataCebo,
   Inc.). **En los dos casos la conclusión habría sido distinta leyendo sólo la página del repo.**
2. **El texto de la BUSL de SDV leído campo por campo** —*Change Date*, *Change License*, *Additional Use Grant*,
   la exclusión de *Synthetic Data Service*— porque de ahí sale la recomendación de no usarlo, y una recomendación
   negativa necesita la cita, no el resumen.
3. **La deprecación de OpenFL citada literal** desde su propia página, incluida la recomendación de migrar a
   Flower.
4. **Las cuatro fechas de la regla COPPA enmendada** (anuncio enero 2025, publicación 2025-04-22, vigencia
   2025-06-23, cumplimiento **2026-04-22**) cruzadas entre varias fuentes secundarias coincidentes.

### ⚠️ Advertencia 1 — `curl -sI` dio 403 en los catorce repos, y ninguno era un 404

El pase 12 ya había dejado escrito que **un 403 del proxy no es un 404**. Volvió a pasar, esta vez en el 100 % de
los casos: `curl -sI` contra `github.com` devolvió **403 en los catorce** URLs candidatas que se le pasaron, incluidas las de
10.000 y 7.200 estrellas. **Verificar con `curl` desde esta sesión produce una tasa de falsos negativos del 100 %
sobre GitHub.** La verificación válida es WebFetch sobre la página del repo. Queda anotado por tercera vez porque
es el error que más barato sale cometer y más caro sale publicar.

### ⚠️ Advertencia 2 — el badge de licencia no alcanza, y acá cambió dos conclusiones

Relacionado con lo anterior pero distinto: en `SDV` el README dice *«publicly available under the Business Source
License»* y el proyecto se presenta con origen en el **MIT Data to AI Lab**, lo que invita a leerlo como permisivo.
**No lo es.** En `diffprivlib` pasa lo contrario: GitHub no muestra licencia en el sidebar y el archivo dice MIT.
**Para cualquier pieza de la que dependa una recomendación, abrir el archivo de licencia.**

### ⚠️ Advertencia 3 — dos dominios bloqueados, y los dos afectan a la metodología, no a los datos

`nature.com` (el paper de `SynEdu-HEDL` en *Scientific Reports*, `s41598-026-44990-8`) y `arxiv.org`
(`2604.04195`, síntesis por cópulas con marginales empíricas) están **bloqueados por el proxy de egreso**. Los
números de los repos salen de GitHub y están verificados; **la metodología publicada detrás de esos dos
artefactos, no**. Importa poco para la recomendación —ninguno de los dos se propone como dependencia— y se declara
igual.

### Lo que este pase NO hizo, declarado como tal

- **No se agregó ningún agente a `agents/top.md`.** El conteo sigue en **31** y se verificó que la tabla no cambió.
  Lo encontrado son librerías, no agentes.
- **No se buscó jurisprudencia ni sanciones aplicadas.** Se registró qué exige cada régimen y desde cuándo, no cómo
  se está aplicando. Para una propuesta real eso hay que mirarlo.
- **No se evaluó el costo de utilidad de DP sobre modelos de knowledge tracing.** Se sabe que DP cuesta exactitud y
  que `diffprivlib` sirve para medirlo; **cuánto cuesta sobre `pyKT` o `pyBKT` nadie lo midió en este pase**, y
  P34 lo dice en su advertencia en vez de prometer números.
- **No se revisó la capa de privacidad de los LMS ya instalados** (Moodle, Open edX, Canvas). Es el paso siguiente
  obvio: el dato del alumno ya está ahí, no en el agente.

## Nota de método del pase 14 (2026-10-01) — el primer pase que ejecutó la acción que un gap anterior le dejó escrita, y funcionó

Los pases 8 a 13 abrieron una capa nueva cada uno preguntándose qué no se había preguntado todavía. **Este pase no
tuvo que inventar la pregunta: el gap 19 la había dejado escrita en el pase 11**, con la acción textual *«buscar
explícitamente `curriculum ontology`, `achievement standards`, `learning map` y `prerequisite graph` por país, en el
idioma del país, en vez de esperar que aparezcan buscando agentes»*.

**Se ejecutó literalmente, y el rendimiento fue el más alto por búsqueda de los catorce pases:** cuatro de cinco
candidatas confirmadas, más un estándar de interoperabilidad con cuatro implementaciones que nadie había visto, más
una corrección de encuadre que afecta a cómo se leyeron cuatro pases anteriores. **La lección de método es que un gap
bien escrito es más productivo que una pregunta nueva**, y conviene que los próximos pases revisen la lista de gaps
antes de buscar un ángulo inédito: los gaps **20** (medir las *skills* educativas con los benchmarks que esta KB ya
tiene), **23** y **24** están escritos con el mismo nivel de detalle y siguen abiertos.

### Lo que este pase buscó por canal y no por rol, y por eso encontró la capa de voz

El segundo hallazgo (capa de habla y lectura oral, tendencia 34) salió de una pregunta distinta y vale registrarla:
**no «qué hace el software» ni «quién es el alumno», sino «por qué canal entra y sale el trabajo del alumno».**
Trece pasadas asumieron texto. Preguntado por el canal, aparece que la habilidad más evaluada en los primeros años
de escolaridad del mundo —leer en voz alta, medida en palabras por minuto y exactitud— **no tenía una sola pieza en
esta KB.**

### ⚠️ Advertencia 1 — una fecha correcta puede sostener una conclusión falsa, y pasó con Taiwán

El pase 13 escribió que *«la conformidad exigible hoy está en Asia»* y recomendó construir el expediente en un
despliegue **«coreano o taiwanés»**, listando Taiwán con la fecha **2026-01-14**. **La fecha es correcta: la ley se
promulgó ese día.** La conclusión no, porque la ley **no tiene sanciones y no define «alto riesgo»** — delega la
clasificación al MODA y ese marco todavía no existe.

**La trampa es específica y va a volver a pasar:** en seguimiento regulatorio, *promulgada* no es *exigible*, y una
fecha de promulgación verificada le da a una afirmación una solidez que el contenido de la ley no respalda. **Regla
para los próximos pases: junto a cada fecha regulatoria hay que registrar (a) si hay régimen sancionatorio y (b) si
las definiciones operativas están publicadas o delegadas.** Con esos dos campos, Taiwán se habría registrado bien en
el pase 13. Corregido en la tendencia 11 y en `intel/market.md` → `### APAC`.

### ⚠️ Advertencia 2 — el badge de licencia del repo es la licencia del código, no la del dato

En artefactos de datos las dos licencias son distintas y casi nunca coinciden: `bncc-dados` es **MIT en código y
CC BY 4.0 en datos**; `oak-curriculum-ontology` es **MIT en código y OGL-3.0 en la ontología**. **Leer sólo el badge
hace creer que el dato es MIT.** Las dos combinaciones permiten uso comercial, pero **con atribución**, y eso es una
obligación que viaja al entregable. Es la continuación directa de la trampa que el pase 10 documentó para OER, y
ahora se declara como regla general de la KB (tendencia 35).

### ⚠️ Advertencia 3 — dos dominios bloqueados por el proxy, y los dos afectan a entregables

- **`www.australiancurriculum.edu.au` bloqueado:** existencia, formatos (RDF/XML, JSON, SPARQL) y versión (9.0) del
  MRAC están confirmados por fuentes secundarias coincidentes; **la licencia de reuso no se pudo leer**. No cotizar
  MRAC sin abrir antes los términos de ACARA.
- **`arxiv.org` bloqueado, igual que en el pase 13:** la literatura de ASR infantil —incluido el caso en bambara
  (`arXiv 2606.31508`, 55 horas de lectura de 60 niños con *benchmark* público declarado)— **no se pudo verificar en
  origen** y queda como pista, no como hallazgo. Es la única vía que vimos hacia evaluación de fluidez en lenguas
  africanas, así que conviene que un pase futuro con otro proxy la abra.
- **`curl` contra `github.com` devuelve 403 por el proxy, no 404.** La verificación de los catorce repos de este pase
  se hizo íntegramente vía WebFetch, leyendo estrellas y licencia de la página del repo. **El pase 12 ya dejó escrita
  esta advertencia y sigue vigente: un 403 no es un repo inexistente.**

### Lo que este pase NO hizo, declarado como tal

- **No agregó ninguna fila a la tabla principal de `agents/top.md`.** El conteo de **31** se mantiene y se verificó.
  Las piezas nuevas entran como capas al final del archivo, porque no son agentes: son componentes y datos.
- **No verificó Singapur como ausencia definitiva.** Se buscó y no apareció esquema curricular estructurado y
  publicado abiertamente; eso es «no encontrado», no «no existe».
- **No abrió los términos de uso de ACARA** (dominio bloqueado), así que MRAC queda registrado sin licencia verificada.
- **No midió el efecto pedagógico de ninguna pieza de la capa de voz.** `OpenPronounce` devuelve métricas acústicas
  (PER, WER, prosodia); **que esas métricas mejoren el aprendizaje de lectura es una hipótesis, no un dato de este
  pase.** El gap 20 y los benchmarks del pase 4 siguen siendo el camino para medirlo.
- **No replicó el pipeline de `bncc-dados` para ningún otro país de LATAM.** Se verificó que ninguno lo tiene; que sea
  replicable es una lectura razonada del pipeline publicado, no una prueba de ejecución.

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
