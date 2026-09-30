---
industry: education
region: Global
updated: 2026-09-30
---

# 📡 Tendencias — education

> Ventana de investigación: septiembre 2026. Verificado 2026-09-30.

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

## Gaps declarados

Huecos confirmados tras buscar, no ausencias por no haber buscado. Un gap informado es información; el silencio se parece demasiado a la cobertura.

1. ~~**No hay evaluador pedagógico open source con tracción.**~~ → **GAP REFORMULADO en el pase 4 del 2026-09-30.** Los pases 1–3 registraron un solo evaluador, `AITutor-EvalKit` (MIT, MBZUAI, **3 ★**), y concluyeron que "no existe el LegalBench de educación". **La medición estaba mal hecha y la conclusión era más fuerte de lo que los datos permitían.**

   Lo que hay, verificado en el pase 4:

   - **`UnifyingAITutorEvaluation`** (https://github.com/kaushal0494/UnifyingAITutorEvaluation, CC BY-SA 4.0, **32 ★**) — **del mismo autor que `AITutor-EvalKit`**. Es el repo canónico: taxonomía de **8 dimensiones** pedagógicas y el dataset **MRBench** en tres versiones (V1 192 diálogos × 8 dim., V2 200 × 8, V3 300 × 4). **NAACL 2025, Senior Area Chair Award.** La KB había registrado el repo chico del mismo trabajo.
   - **`MathTutorBench`** (https://github.com/eth-lre/mathtutorbench, CC BY 4.0, **42 ★**) — no estaba en la KB. 3 habilidades docentes de alto nivel, 7 tareas, **reward models entrenados** para medir calidad de enseñanza y **leaderboard público**. **EMNLP 2025 (Oral).**
   - **`pyKT`** (MIT, **441 ★**) mide la otra mitad del problema: el estado de conocimiento del alumno, no la calidad de la respuesta del tutor.

   **La formulación correcta del gap:** el estándar **existe, está publicado en los dos venues principales de NLP, y nadie lo está usando en producción.** 42 y 32 estrellas para benchmarks premiados en EMNLP y NAACL es señal de que la academia los produjo y la industria no los adoptó. Eso sigue siendo una oportunidad — pero es "integrar y operacionalizar lo que ya existe", no "construir lo que falta", y son propuestas muy distintas. Ver el patrón **P10**.

   ⚠️ **Y hay que leer la licencia:** MathTutorBench es CC BY 4.0 y UnifyingAITutorEvaluation es **CC BY-SA 4.0** (*share-alike*). El uso típico en un engagement — derivar un benchmark propio con datos del cliente — es exactamente lo que dispara la obligación del share-alike.

   **Lo que sigue sin existir:** un benchmark pedagógico **fuera de matemática**. Los tres son de matemática (o de matemática, física y química en el caso de `EduFair-Bench`, que es un paper de arXiv sin repo localizable). Para lengua, ciencias sociales o formación profesional no hay nada.
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
3. **EMEA no produce tutores: produce la capa que los mide y los acredita** *(reformulado en el pase 4; antes decía "produce plataformas")*. La formulación anterior era correcta pero pobre — agrupaba todo lo no-agéntico como "plataformas". Con lo del pase 4 el patrón es más nítido y más útil:

   - **Plataformas:** OpenOLAT (Suiza), Chamilo (Bélgica/España), Richie (Francia), H5P (Noruega).
   - **Evaluación:** **MathTutorBench** (org `eth-lre`, CC BY 4.0, 42 ★, EMNLP 2025 Oral) y **UnifyingAITutorEvaluation** + AITutor-EvalKit (MBZUAI, Abu Dhabi, NAACL 2025).
   - **Esquemas de conformidad curricular:** **OpenDidactia** (España, CC BY-SA 4.0, 0 ★) — esquemas OKF para generar Programaciones Didácticas conformes a **LOMLOE** en las 17 comunidades autónomas. No es un agente: es el *formato de salida auditable* que un agente docente necesita para ser aceptable ante una inspección educativa.
   - **Skills pedagógicas:** education-agent-skills (UK, CC BY-SA 4.0, 814 ★).
   - **Tutores, la excepción:** **OpenTutorAI-CE** (BSD-3-Clause, 107 ★) — **región cerrada en el pase 4: Marruecos**, lo que explica su soporte multilingüe árabe/francés/inglés.

   **Que EMEA produzca medición y conformidad mientras APAC produce tutores no es casualidad: es el reflejo de dónde muerde la regulación.** Para una propuesta europea eso es favorable — el artefacto local disponible es justamente el que pide el EU AI Act. Lo que EMEA no tiene es un tutor open source de escala, y hay que ir a buscarlo a APAC con el riesgo de procedencia que eso implica (gap 4).
4. **La oferta de agentes está concentrada en APAC.** DeepTutor (HKU) y OpenMAIC (Tsinghua) son ~80k ★ combinadas y las dos vienen de instituciones chinas. Para un cliente con restricciones de procedencia de software, esto es un riesgo a declarar temprano, no a descubrir en due diligence.
5. **No hay integración madura entre knowledge tracing y agentes LLM** *(el gap se mantiene; el inventario estaba incompleto — corregido en el pase 4)*. La conclusión —**nadie los cosió bien**— sigue siendo correcta y es el hueco técnico concreto del patrón P1. Lo que estaba mal era el inventario de piezas disponibles: los pases 1–3 listaban sólo `py-fsrs` (MIT, 499 ★, scheduling) y OATutor (BKT embebido en un ITS completo).

   Falta agregar la pieza central: **`pyKT`** (https://github.com/pykt-team/pykt-toolkit, **MIT**, **441 ★**, 811 commits) — librería de *knowledge tracing* profundo sobre PyTorch con **10+ modelos DLKT** comparables, **7+ datasets** con preprocesamiento estandarizado y 5 escenarios de predicción. Publicada en **NeurIPS 2022** y mantenida. Origen: **Jinan University / Guangdong Institute of Smart Education, China → APAC** (refuerza el gap 4, ahora también en la capa de modelado).

   **Por qué la corrección importa aunque el gap no se cierre:** con el inventario viejo, coser tracing a un agente parecía "implementar BKT a mano o extraerlo de OATutor". Con `pyKT` en la mesa, el trabajo es **integración de una librería MIT madura**, no investigación. Eso cambia la estimación de un proyecto de meses a semanas, y cambia lo que se puede prometer: un modelo DLKT publicado y reproducible es evidencia defendible de eficacia adaptativa ante un regulador; "el LLM decidió" no lo es. Ver el patrón nuevo **P10**.

   **Lo que sigue faltando literalmente:** un repo que exponga un modelo de knowledge tracing **como tool o servidor MCP** para que el agente consulte el estado de mastery antes de decidir qué preguntar. `tutor-mcp` (MIT, 42 ★, Go) es lo más cercano — implementa BKT y repetición espaciada detrás de MCP — pero usa su propio BKT, no una librería DLKT entrenable. **El hueco exacto es `pyKT` detrás de MCP**, y no existe.

6. **No hay agente de grading open source con tracción** *(agregado en el pase 2)*. Se buscó específicamente corrección y assessment automatizado con licencia permisiva. La capa de grading sigue siendo **propietaria**: Gradescope (Turnitin), Codio, Kangaroos AI. En abierto hay *papers* (arXiv 2601.00730, 2607.02432, 2506.07955), no repos con adopción. Consecuencia directa para propuestas: **no prometer reemplazar Gradescope; prometer orquestarlo** — por eso `gradescope-mcp` (MIT, 8 ★) vale seguirlo pese a su tamaño. Es el camino realista hacia grading agéntico hoy.

7. ~~**No hay SIS open source permisivo y vivo**~~ → **GAP RETIRADO en el pase 3 del 2026-09-30.** El pase 2 declaró que toda la capa SIS open source era PHP y copyleft, que la única opción permisiva (**Fedena**, Apache-2.0, 547 ★) estaba **muerta desde el 2016-07-20**, y concluyó que en el lado administrativo el agente **siempre** tiene que ir afuera. **La conclusión era incorrecta y se corrige.**

   **GegoK12** (https://github.com/Gego-K12/gegok12) es **MIT** — verificado en el archivo `LICENSE` del repo, `SPDX-License-Identifier: MIT`, © 2025 GegoSoft Technologies — con **54 ★, 97 forks, 123 commits y último commit el 2026-09-23**. Está vivo, es PHP 8.4 + Laravel 12, API-first, y **tiene sistema de plugins** (`Plugin-Hello-Teacher`). O sea: en el lado administrativo el agente **sí puede vivir adentro**, como plugin, sin contaminar IP, porque MIT no impone share-alike.

   **Lo que sigue siendo cierto:** todo el SIS open source es PHP, Fedena sigue muerta y no hay que proponerla, y para RosarioSIS / openSIS / OpenEduCat (los tres copyleft, y los tres con más instalaciones reales) el agente sigue yendo afuera. **Lo que cambia:** dejó de ser "la única opción limpia" y pasó a ser "el patrón por defecto, con una alternativa".

   **La condición que hay que leer:** GegoK12 es **open-core**. De 38 módulos, 26 están en el core MIT (alumnos, admisiones, asistencia, tareas, biblioteca, staff, avisos, comunicación con padres) y **12 son Pro pagos, USD 100–250 cada uno** — entre ellos **examinación y gestión de fees**, que son justo los dos procesos que un agente querría automatizar primero. Licencia Pro lifetime por dominio con fuente incluido, no suscripción por alumno. Detalle completo en `verticals/solutions.md`.

   **Por qué este gap se sostuvo dos pasadas.** Las dos anteriores buscaron "SIS open source" y encontraron los listicles, que repiten Fedena/RosarioSIS/openSIS y no incluyen a GegoK12 porque es reciente. La lección de método: **un gap de la forma "no existe X permisivo" hay que re-buscar con la consulta invertida** — por licencia y stack ("school ERP MIT Laravel"), no por categoría. Buscar la categoría devuelve el consenso de los listicles; buscar la licencia devuelve los proyectos nuevos.


8. **La capa teacher-facing es propietaria, con una sola excepción open source** *(agregado en el pase 3)*. `intel/market.md` ya observaba que las herramientas *para docentes* son "el ángulo menos disputado" y que MagicSchool lidera ahí. Buscando el equivalente open source aparece que el segmento entero es cerrado: **MagicSchool, Brisk, Diffit, Curipod, Eduaide.AI, SchoolAI, Taskade**. La única entrada open source que encontramos es **Claw-ED** (MIT, **59 ★**). Es decir: donde la demanda docente es más clara y la competencia menos feroz, la oferta abierta es un solo repo de 59 estrellas. Ver el patrón **P8**.

9. **Sigue sin haber grading open source con tracción, pero la categoría se movió** *(actualizado en el pase 3)*. El gap 6 se mantiene: Gradescope (Turnitin), Codio y Kangaroos AI siguen siendo propietarios y no apareció ningún reemplazo con adopción. Lo nuevo es **AI-Teaching-Agent** (MIT, **0 ★**, 30 commits): genera artefactos **Lab / Exam / Grading como DSL validado**, con revisión humana obligatoria, evaluación sandboxeada, servidor MCP y previews de examen sin respuestas. Es la primera vez que vemos la estrategia de *generar el artefacto de corrección auditable* en vez de orquestar al incumbente — y el diseño es exactamente el que piden el EU AI Act y los estatutos de EE. UU. que prohíben grading automático. **Con 0 estrellas no se usa: se sigue.** La recomendación operativa del gap 6 no cambia (orquestar Gradescope vía `gradescope-mcp`).

## Fuentes

Mercado y players: [Grand View Research](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-education-market-report) · [Research and Markets](https://www.researchandmarkets.com/reports/5896034/ai-in-education-market-report) · [AI Tutors Market](https://www.grandviewresearch.com/industry-analysis/ai-tutors-market-report) · [5WPR EdTech AI Visibility Index 2026](https://www.5wpr.com/research/edtech-ai-visibility-index-2026/) · [Khan Academy / Duolingo agents](https://callsphere.ai/blog/ai-agents-education-khan-academy-duolingo-autonomous-tutoring)

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
