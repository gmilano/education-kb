---
industry: education
region: Global
updated: 2026-10-01
---

# 📈 Agentes trending — education

> **APPEND-ONLY.** Cada corrida agrega una sección fechada arriba y conserva la historia abajo.
> No reescribir secciones anteriores: la serie temporal es el valor de este archivo.

## 2026-10-01 (pase 6) — el agente por fin tiene dónde escribir: aparece la capa de telemetría, y su puente MCP

Sexta corrida del día. El pase 5 cerró con el gap 5 reformulado así: **"cinco lo intentaron y ninguno conectó la librería buena"** — cinco servidores MCP de mastery, todos con heurística propia, ninguno sobre `pyKT` o `pyBKT`. Este pase encuentra que el problema estaba mal partido.

Los cinco servidores MCP del pase 5 no fallaron sólo por no usar una librería de knowledge tracing. Fallaron porque **cada uno inventó también su propio almacén de eventos de aprendizaje**. Y ese almacén no hay que inventarlo: es un estándar IEEE con implementaciones maduras que esta KB no tenía registradas en ninguna de las cinco pasadas anteriores.

### La capa que faltaba: Learning Record Store (xAPI)

Un **LRS** es la base de datos de eventos de aprendizaje: cada "el alumno intentó X y le salió Y" se guarda como un *statement* xAPI. Es el sustrato que consume cualquier modelo de knowledge tracing. La KB tenía plataformas, agentes, modelado, medición, modelos fundacionales, SIS y autograding — y **ningún lugar donde el agente deje registro de lo que observó**.

| Repo | Licencia | Stars | Commits | Lenguaje | Qué es |
|---|---|---|---|---|---|
| **Learning Locker** — https://github.com/LearningLocker/learninglocker | **GPL-3.0** ⚠️ | 583 | 3.254 | JavaScript | El LRS open source canónico, desde 2014. Mantenido por Learning Pool. El más adoptado de la categoría — y el único copyleft de los cuatro |
| **ADL_LRS** — https://github.com/adlnet/ADL_LRS | **Apache-2.0** ✅ | 331 | 1.885 | Python | La implementación de referencia de **ADL** (Advanced Distributed Learning, EE. UU.), que es quien define el estándar. Soporta **IEEE 9274.1.1 (xAPI 2.0)** |
| **SQL LRS (`lrsql`)** — https://github.com/yetanalytics/lrsql | **Apache-2.0** ✅ | 143 | 2.268 | Clojure | LRS sobre SQL corriente: SQLite, **PostgreSQL 14–18**, MariaDB, MySQL 8–9.5. Copyright © 2021–**2026** de Yet Analytics: es el permisivo más vivo de la capa |
| **Ralph** — https://github.com/openfun/ralph | **MIT** ✅ | 50 | 714 | Python | LRS + CLI de pipelines + librería, con conversión nativa de **tracking logs de Open edX** a xAPI. FastAPI, Elasticsearch, Docker/K8s |

⚠️ **La condición que hay que leer antes de proponer ADL_LRS.** El propio repo advierte que *"This version is stable, but only intended to support a small amount of users as a proof of concept"*. Es la implementación **de referencia del estándar**, no un producto de producción. Sirve para validar conformidad, no para aguantar un distrito. Para producción permisiva el candidato es **`lrsql`**; para integración con Open edX, **Ralph**.

### Y el puente que conecta la capa nueva con los agentes

| Repo | Licencia | Stars | Commits | Qué hace |
|---|---|---|---|---|
| **learnmcp-xapi** — https://github.com/DavidLMS/learnmcp-xapi | **MIT** ✅ | 15 | 32 | Servidor **MCP** que le da a un agente tres tools sobre un LRS xAPI: **registrar** un statement, **consultar** el historial de progreso y **gestionar el vocabulario** de verbos/actividades. Backends soportados: **`lrsql`**, **Ralph**, Veracity Learning, y arquitectura de plugins para otros |

El detalle de diseño que lo hace interesante para un tutor: captura el aprendizaje de **dos** maneras — explícita (*"practiqué bucles en Python"*) o **inferida de la conversación**, detectando conocimiento demostrado o vacíos, y después consulta ese historial para adaptar la respuesta siguiente.

**Y el dato de procedencia importa:** el autor declara pertenecer al **IES Rafael Alberti** — un instituto público español de secundaria. Es decir, el puente entre agentes y el estándar de telemetría educativa lo escribió **un docente en ejercicio**, no un laboratorio. Región: **EMEA (España)**.

### Cómo cambia el gap 5, con precisión

El gap 5 decía que el hueco exacto era **`pyKT` detrás de MCP**. Sigue sin existir — verificado otra vez en este pase. Pero el trabajo que implica es **más chico de lo que la KB venía estimando**, porque dos de las tres piezas ya están resueltas y con licencia permisiva:

| Pieza | Estado antes del pase 6 | Estado real |
|---|---|---|
| Almacén de eventos de aprendizaje | "cada servidor MCP se lo inventa" | **Resuelto.** `lrsql` (Apache-2.0) o Ralph (MIT), sobre un estándar IEEE |
| Transporte MCP hacia ese almacén | "no registrado" | **Resuelto.** `learnmcp-xapi` (MIT), que ya habla con los dos anteriores |
| Modelo de knowledge tracing entrenable detrás | "no existe" | **Sigue sin existir.** `learnmcp-xapi` registra y recupera; **no infiere mastery** |

**La formulación correcta del hueco, sexta versión:** no es "construir un servidor MCP de mastery" (eso lo hicieron cinco veces) ni "construir el almacén" (es un estándar con cuatro implementaciones). Es **enchufar `pyBKT` o `pyKT` como estimador detrás de un LRS que ya existe, exponiéndolo por un MCP que ya existe**. Eso es un componente, no una plataforma. Ver el patrón nuevo **P15**.

### L2-Bench — el sub-gap de "benchmark pedagógico fuera de matemática" se cierra en lengua, con una advertencia de verificación

El pase 5 dejó el sub-gap así: *"benchmark pedagógico específico de **lengua**, ciencias sociales o formación profesional"*. Para **lengua** aparece un artefacto, y no es académico de nicho:

**L2-Bench** — *An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education* (arXiv 2607.08842), de **Oxford University Press** con la Universidad de Oxford. Según las fuentes localizadas: **1.000+ tareas docentes auténticas**, un marco de **12 competencias docentes con 31 sub-habilidades**, rúbricas con descriptores expertos, y validación de **200+ educadores de 45+ países**. Licencia declarada: **dataset y rúbricas CC BY-SA 4.0 ⚠️, código de evaluación MIT ✅**. Hay un paper metodológico compañero (arXiv 2603.20088).

🔴 **Advertencia de verificación, y es importante:** a diferencia de todo lo demás en este pase, **L2-Bench no se pudo verificar de primera mano**. El proxy de egreso de esta sesión bloquea `arxiv.org`, `huggingface.co` y `oup.com` — los tres lugares donde vive. Todo lo anterior viene de resultados de búsqueda, no de leer el dataset ni el archivo de licencia. **Antes de usarlo en un entregable hay que abrirlo y confirmar licencia y contenido.** Se registra porque un benchmark de segunda lengua de OUP con 200+ validadores es exactamente lo que el gap pedía, y omitirlo sería peor; pero se registra marcado.

Si se confirma, refuerza el gap 3 una vez más: **EMEA vuelve a producir la medición, no el tutor.** Cuatro de los artefactos de evaluación de esta KB son ya europeos o de MBZUAI.

### Lo que se buscó y no está — formación profesional sigue siendo un desierto, ahora con números

El otro tercio del sub-gap del pase 5 es **formación profesional**, y acá no hay hallazgo: hay una medición del vacío. Búsqueda directa en GitHub por `vocational education AI`: **24 repos en total**, el más grande con **2 estrellas**. Casi todos son trabajos de curso o portfolios personales. Los dos únicos con forma de producto:

- `edufeedai/edufeedai` (Java, **0 ★**) — feedback automatizado sobre entregas de FP. 9 issues abiertos, sin tracción.
- `straussbastian/ai_flashcards_for_school` (Python, **1 ★**) — flashcards generadas por un agente vía **MCP** para *Berufsschule* alemana; el docente arma el bundle, la clase entra con un link de tres palabras, sin login ni resultados almacenados. Diseño de privacidad interesante, tamaño irrelevante.

**Conclusión, que es un dato y no una ausencia:** la formación profesional —el segmento con más presión de reskilling en las cuatro regiones— **no tiene nada open source con tracción**. 24 repos y 2 estrellas de techo no es un ecosistema incipiente: es un hueco. Para un engagement de FP hay que presupuestar construcción, no integración.

## 2026-09-30 (pase 5) — aparece una categoría entera que la KB no tenía: seguridad pedagógica

Quinta corrida del día. Se volvió a aplicar la lección de método del pase 3 (buscar la *pieza técnica*, no la categoría) y esta vez el resultado no es un repo: es **una categoría de evaluación con cuatro publicaciones en venues top y datasets liberados, que ninguna de las cuatro pasadas anteriores registró**.

El pase 4 cerró diciendo que el estándar pedagógico "existe, está publicado y nadie lo usa", y que **lo que seguía faltando era un benchmark fuera de matemática**. Ese sub-gap se cae en este pase, y se cae por partida doble.

### La categoría nueva: *pedagogical safety* / sycophancy

No se trata de toxicidad ni de jailbreak genérico. Se trata de una falla propia de la educación: **el tutor que enseña mal siendo amable**. Revelar la respuesta antes de tiempo, reforzar la idea equivocada del alumno porque el alumno insistió, abandonar el andamiaje. Es medible, y desde 2026 hay con qué medirlo.

| Artefacto | Repo / fuente | Licencia | Stars | Qué mide | Alcance |
|---|---|---|---|---|---|
| **SafeTutors** | https://github.com/RadiantCrystal/SafeTutors | MIT ✅ | 0 | Taxonomía de **11 dimensiones de daño y 48 sub-riesgos** derivadas de literatura de ciencias del aprendizaje. **5.955 instancias** (3.135 escenarios single-turn + 2.820 diálogos multi-turn). 11 modelos evaluados (10 open-weight, 1 cerrado), de 3.8B a 72B | Matemática, física, **química** |
| **EduGuardBench** | https://github.com/YL1N/EduGuardBench | ⚠️ **sin licencia declarada** | 4 | Daño docente vía preguntas *Select All That Apply* + set de prompts adversarios con jailbreak basado en personas, enfocado en **mala conducta académica**. 14 modelos | Simulación de docente, transversal a materia |
| **EduBench** | https://github.com/ybai-nlp/EduBench | MIT ✅ | 29 | **9 contextos educativos** y 4.000+ situaciones sobre **12 dimensiones** en 3 categorías (adaptabilidad al escenario, exactitud factual/razonamiento, aplicación pedagógica). Cubre 5 escenarios de alumno y **4 de docente, entre ellos Automatic Grading** | Transversal — **no es de matemática** |
| **EduFrameTrap** | arXiv 2605.14604 (2026-05-14) — no se localizó repo público | n/d | — | Sycophancy bajo presión social: subtipos **CS-SYC** (cambio de marco), **AUTH-SYC** (deferencia ante autoridad), **FACE-SYC** (salvar la cara), **DIR-SYC** (endoso directo). Formula la *Reasoning-Sycophancy Paradox*: un modelo que resiste el ataque de marco igual capitula ante presión de autoridad | Matemática, física, **economía, química, biología, ciencias de la computación** |
| **ELBench** | arXiv 2608.09548 (ago 2026) — no se localizó repo público | n/d | — | 4 módulos bajo un protocolo común: General Capability, Safety & Trustworthiness, Basic Education, High-Level Cultivation. 9 modelos | Transversal |

### El sub-gap "no hay benchmark fuera de matemática" se cae

El pase 4 lo dejó escrito: *"Lo que sigue sin existir: un benchmark pedagógico fuera de matemática. Los tres son de matemática (…). Para lengua, ciencias sociales o formación profesional no hay nada."*

Corrección:

- **EduBench (MIT, ACL 2026)** es explícitamente **transversal a materia** y organiza la evaluación por *escenario educativo*, no por dominio. Incluye cuatro escenarios docentes, uno de ellos corrección automática.
- **EduFrameTrap** cubre **seis materias**, entre ellas economía y biología.
- **EduGuardBench** evalúa al modelo *como docente simulado*, lo que es independiente de la materia.

Lo que **sí se mantiene** del gap: no hay benchmark pedagógico para **lengua, ciencias sociales ni formación profesional** específicamente. Ninguno de los cinco los cubre. Pero la afirmación "todo es matemática" dejó de ser cierta, y `EduBench` es MIT, lo que lo vuelve el primer artefacto de evaluación pedagógica de esta KB **sin fricción de licencia** — los dos que el pase 4 celebró (MathTutorBench CC BY, UnifyingAITutorEvaluation CC BY-SA) sí la tienen.

### El hallazgo más vendible: la seguridad está *anti-correlacionada* con la enseñanza práctica

De ELBench, y es el dato que conviene llevar a una conversación de cliente regulado: **entre los modelos evaluados, el módulo de safety está anti-correlacionado con el de enseñanza práctica.** Los modelos más seguros enseñan peor y los que mejor enseñan son menos seguros.

Si se sostiene, tiene una consecuencia directa de arquitectura: **no existe el modelo que resuelva las dos cosas eligiéndolo bien.** Hay que componer — modelo docente + gate de seguridad medido aparte — que es exactamente lo que el patrón nuevo **P11** propone. Es también el mejor argumento contra la pregunta "¿y por qué no usamos el modelo más grande y listo?".

EduGuardBench aporta el matiz opuesto y también sirve: identificó un *Educational Transformation Effect* — los modelos más seguros no se limitan a rechazar el pedido dañino, lo **convierten en momento de enseñanza** (*Educational Refusal*). Y que el modo de falla dominante no sea la toxicidad sino la **incompetencia** confirma que el riesgo real en educación es pedagógico, no reputacional.

### Teacher-facing: el gap 8 se corrige — no es un solo repo de 59 estrellas

El pase 3 declaró que toda la capa docente es propietaria "con una sola excepción open source", Claw-ED (MIT, 59 ★). **Es incorrecto y se corrige:** hay un asistente de planificación docente **MIT, en producción, con 1.188 commits y respaldo institucional público**.

| Repo | Licencia | Stars | Commits | Qué es |
|---|---|---|---|---|
| **Aila** — https://github.com/oaknational/oak-ai-lesson-assistant | MIT ✅ | 35 | **1.188** | *AI Lesson Planning Assistant* de **Oak National Academy** (Reino Unido, nonprofit educativa respaldada por el gobierno británico). Monorepo Turborepo: Next.js + Prisma/PostgreSQL con **pgvector**. Entornos de producción y staging, versionado semántico, estrategia de ramas |
| **ai-lesson-planner** — https://github.com/saniales/ai-lesson-planner | GPL-3.0 ⚠️ | 20 | 2 | Toolkit chat-first con workflow multi-agente (course-planner → discussion-moderator → lesson-planner → slides-maker) y salida a slides **MARP** |

⚠️ **La condición de Aila hay que leerla antes de proponerlo.** El propio repo aclara que *"this project is intended primarily for internal use by Oak National Academy"*. Es **código abierto de un producto en producción, no un producto empaquetado para terceros**: no hay compromiso de API estable, ni de soporte, ni de que el monorepo se pueda desplegar fuera del contexto de Oak. La lectura correcta es **"la mejor referencia de arquitectura teacher-facing que existe en abierto, con licencia que permite copiar piezas"**, no "la base sobre la que montamos el producto del cliente". Con 1.188 commits de un equipo real resolviendo el problema en producción, como referencia vale más que los otros dos juntos.

**Lo que no cambia:** el segmento sigue dominado por propietarios (MagicSchool, Brisk, Diffit, Curipod, Eduaide.AI, SchoolAI). Lo que cambia es que ya no es cierto que en abierto sólo haya un repo de autor individual.

### Knowledge tracing detrás de MCP: existe cinco veces, y ninguna sirve todavía

El pase 4 cerró el gap 5 con una formulación muy precisa: *"El hueco exacto es `pyKT` detrás de MCP, y no existe."* **La primera mitad se confirma; la segunda hay que matizarla de una forma que es más interesante que si fuera falsa.**

Buscando por la pieza técnica aparecen **cinco servidores MCP independientes** que exponen mastery/knowledge tracing a un agente:

| Repo | Licencia | Stars | Commits | Qué implementa |
|---|---|---|---|---|
| https://github.com/zcsabbagh/knowledge-graph-mcp | MIT ✅ | 1 | 8 | FastMCP + SQLite. Grafo de conceptos con prerequisitos, **SM-2** para repaso y mastery multidimensional con fórmula fija: `0.3×recall + 0.4×application + 0.3×explanation`. Detección de misconceptions |
| https://github.com/woodstocksoftware/student-progress-tracker | MIT ✅ | 1 | 9 | Perfiles, inscripciones, resultados de evaluación, cálculo de mastery por tema, detección de learning gaps y recomendación de foco. Telemetría a nivel de pregunta |
| https://github.com/tejpalvirk/student | MIT ✅ | 1 | 6 | Grafo de conocimiento académico (cursos, trabajos, exámenes, conceptos) con persistencia entre sesiones |
| https://github.com/znecho9/knowledge-forest-mcp | Apache-2.0 ✅ | 0 | 3 | Árboles de prerequisitos + **mastery con evidencia obligatoria**: exige desempeño novedoso, sin asistencia y a libro cerrado antes de declarar dominio |
| https://github.com/radhepa/Teacher-MCP | MIT ✅ | 0 | 2 | MCP-first con memoria persistente SQLite, personas docentes y andamiaje en tres niveles. Trae además un Claude Skill que funciona solo o contra el server |

**La lectura correcta, que es una señal de mercado y no un hallazgo técnico:** cinco autores sin relación entre sí llegaron a la misma idea en la misma ventana. El patrón *"el agente consulta el estado de mastery antes de decidir qué preguntar"* **se está reinventando en paralelo**, lo cual valida que el problema es real y sentido por muchos.

**Y el hueco de ingeniería sigue intacto, ahora con mejor evidencia.** Ninguno de los cinco usa una librería de knowledge tracing entrenable: todos **implementan su propia heurística** (SM-2, fórmulas de pesos fijos, reglas de evidencia). Los tres con más tracción suman **3 estrellas y 23 commits**. Verificado de primera mano en este pase: **`pyKT` sigue en 441 ★ / 811 commits y su documentación no menciona MCP ni interfaz de serving.**

Dicho de otro modo: el gap 5 pasa de *"nadie lo intentó"* a **"cinco lo intentaron y ninguno conectó la librería buena"**. Es una propuesta mejor, no peor: el trabajo dejó de ser inventar el patrón (ya está validado cinco veces) y pasó a ser **hacerlo bien una vez** — ver **P12**.

### La pieza que faltaba para hacerlo bien, y es de North America

| Repo | Licencia | Stars | Commits | Por qué importa |
|---|---|---|---|---|
| **pyBKT** — https://github.com/CAHLR/pyBKT | MIT ✅ | **281** | 379 | Bayesian Knowledge Tracing y variantes en Python: estima mastery cognitivo desde secuencias de resolución, con parámetros individualizados por alumno y tasas de aprendizaje por ítem. Publicado en **EDM 2021** (Badrinath, Wang & Pardos) |

Viene de **CAHLR (UC Berkeley)**, **el mismo laboratorio de Zachary Pardos que produjo OATutor**, que esta KB ya tenía listado sin haber mirado el resto del laboratorio.

**Por qué cambia la propuesta y no sólo el inventario:** el gap 4 de esta KB dice que la oferta está concentrada en APAC, y el pase 4 agravó el diagnóstico al descubrir que también la capa de modelado era china (pyKT, Jinan University). **pyBKT es MIT, tiene 281 estrellas, está publicado y es de una universidad estadounidense.** Para un cliente con restricciones de procedencia de software —el riesgo que el gap 4 manda declarar temprano— ahora hay una alternativa en la capa de modelado que no obliga a elegir entre cumplir la restricción y tener knowledge tracing.

El trade-off técnico hay que decirlo igual: pyBKT es **BKT bayesiano clásico**, pyKT es **deep learning (10+ modelos DLKT)**. pyKT es más potente y pyBKT es más interpretable y mucho más fácil de defender ante un regulador que pregunta por qué el sistema decidió lo que decidió. Para un primer engagement regulado, la interpretabilidad suele ganar.

### Correcciones de esta corrida

1. **`SirhanMacx/eduagent` no es un repo nuevo: redirige a `SirhanMacx/Claw-ED`.** Aparece en búsquedas como "EduAgent, CLI agent con 48+ tools" y parece un segundo proyecto del mismo autor. Es el mismo repo renombrado. Verificado: la URL `/SirhanMacx/eduagent` resuelve a `SirhanMacx/Claw-ED`. **No agregarlo como entidad separada** — se deja anotado acá justamente para que una pasada futura no lo duplique.
2. **Claw-ED sigue en 59 ★ pero creció en código:** **778 commits**, release **v9.18.2026.1**. Soporta Anthropic, OpenAI, Gemini, Ollama y OpenRouter. Las estrellas están planas y el desarrollo no: es un proyecto activo con poca visibilidad, no uno abandonado.
3. **`GeminiLight/awesome-ai-llm4education` (220 ★, catálogo de 334 papers 2001–2026) NO TIENE ARCHIVO LICENSE.** Verificado: `/blob/main/LICENSE` devuelve 404. Es un índice bibliográfico excelente para orientarse, y **no es reutilizable en un entregable** — sin licencia, el default legal es "todos los derechos reservados". Usarlo para leer, no para copiar.

### Lo que esta pasada buscó y no encontró

- **Repo público de EduFrameTrap y de ELBench.** Los dos papers describen benchmarks con rúbricas y subtipos concretos; no se localizó código ni dataset publicado para ninguno de los dos. Son las dos únicas filas de la tabla de arriba sin artefacto verificable.
- **Agente educativo de origen LATAM con tracción.** Se volvió a buscar en español y portugués. Nada nuevo por encima de lo del pase 4 (TutorIA, MIT, 0 ★). **El gap 2 se mantiene sin cambios.**
- **Benchmark pedagógico de lengua, ciencias sociales o formación profesional.** Sigue sin existir, ver arriba.

### Nota de método — el proxy de egreso bloquea la mayoría de las fuentes académicas

Dato operativo para las próximas pasadas, porque cambia qué se puede afirmar como verificado:

- **`curl -sI` contra github.com devuelve 403** a través del proxy. Confirma lo que anotó el pase 4: **no sirve para verificar URLs en este entorno**. El método que funciona es WebFetch contra la página del repo.
- **Bloqueados por el proxy de egreso:** `arxiv.org`, `openreview.net`, `aclanthology.org`, `huggingface.co`, `ojs.aaai.org`, `mcml.ai`, `unu.edu`, `coe.int`, `digitaleducationcouncil.com`, `mcpservers.org`.
- **Consecuencia que hay que respetar al leer este pase:** todo lo de **github.com está verificado de primera mano** (licencia, stars, commits leídos de la página del repo). Todo lo que sale de **papers, datasets de HuggingFace y cifras de mercado está tomado de resúmenes de búsqueda y NO pudo verificarse contra la fuente primaria** — incluidos los conteos de ítems de SafeTutors, los subtipos de EduFrameTrap, el hallazgo de anti-correlación de ELBench y el venue de cada publicación. Están registrados porque son útiles y consistentes entre fuentes independientes, no porque se hayan visto en el original. **No citarlos en material de cliente sin abrir el paper.**

## 2026-09-30 (pase 4) — la capa de evaluación y de knowledge tracing existía; la KB la estaba buscando mal

Cuarta corrida del día. No se buscaron "agentes educativos": las tres pasadas anteriores ya agotaron esa consulta. Se aplicó la **lección de método que el propio pase 3 dejó escrita** — cuando un gap dice "no existe X", re-buscar por la *pieza técnica* y no por la categoría. Resultado: **dos gaps declarados se caen y un tercero se refina**, y el mayor hallazgo tiene 441 estrellas y llevaba cuatro años publicado.

### Nuevos agentes y piezas verificadas

Todo verificado vía WebFetch contra la página del repo.

| Repo | URL | Licencia | Stars | Lenguaje | Qué es | Región |
|------|-----|----------|-------|----------|--------|--------|
| **pyKT** | https://github.com/pykt-team/pykt-toolkit | MIT ✅ | **441** | Python | Librería de **knowledge tracing** sobre PyTorch: 10+ modelos DLKT, 7+ datasets, preprocesamiento estandarizado. 811 commits | APAC (Jinan University, China) |
| **FreeLingo** | https://github.com/artcc/freelingo | **AGPL-3.0** ⚠️ | 150 | Python | Duolingo self-hosted: nivel CEFR evaluado por LLM local (Ollama), plan de estudio, tutor por voz, flashcards, repetición espaciada | Sin verificar |
| **MathTutorBench** | https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | 42 | Python | Benchmark de capacidad **pedagógica** de tutores LLM: 3 habilidades docentes, 7 tareas, reward models y leaderboard. EMNLP 2025 Oral | EMEA (org `eth-lre`) |
| **UnifyingAITutorEvaluation** | https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | 32 | — | Taxonomía de 8 dimensiones pedagógicas + **MRBench** V1/V2/V3. NAACL 2025, Senior Area Chair Award | EMEA (MBZUAI) |
| **TutorIA** | https://github.com/LabSirius/TutorIA | MIT ✅ | **0** | Python | Tutor autónomo dentro de Open edX para **educación superior rural**, con TTS, avatar y dashboard docente | **LATAM (Pereira, Colombia)** |
| **OpenDidactia** | https://github.com/nmarafo/OpenDidactia | CC BY-SA 4.0 ⚠️ | 0 | Markdown | Esquemas curriculares OKF para generar Programaciones Didácticas **LOMLOE** con agentes. 17 comunidades autónomas | EMEA (España) |
| **mentar** | https://github.com/avps82/mentar | **AGPL-3.0** ⚠️ | 1 | Python | Tutor local-first para chicos, 934 nodos de concepto en 157 plantillas (AU/IN/SG/US). El LLM explica, un checker determinístico corrige | Sin verificar |

### Lo que se cae: el gap "no hay evaluador pedagógico open source"

El gap 1 decía que el único evaluador era `AITutor-EvalKit` con **3 estrellas** y que "no existe el LegalBench de educación". Las dos mitades estaban mal medidas:

- **`UnifyingAITutorEvaluation` (32 ★) es del mismo autor y es el repo canónico.** La KB había registrado el repo chico — la implementación LoMTL sobre 4 dimensiones — y no el grande, que publica la taxonomía de 8 dimensiones y las tres versiones de MRBench. Premio de Senior Area Chair en NAACL 2025.
- **`MathTutorBench` (42 ★, EMNLP 2025 Oral) no estaba en la KB en absoluto.** Tiene reward models entrenados y leaderboard público.

El gap no desaparece del todo — 42 y 32 estrellas siguen siendo poca tracción — pero pasa de "no existe" a "**existe, está publicado en EMNLP y NAACL, y nadie lo está usando en producción**". Es una afirmación muy distinta frente a un cliente que tiene que demostrar calidad pedagógica bajo EU AI Act.

### Lo que se cae: LATAM deja de ser fase cero *institucional*

El gap 2 decía que LATAM produce agentes pero "ninguno sale de la fase cero", con ejemplos de 0 y 2 estrellas y uno sin licencia. **TutorIA** sigue teniendo 0 estrellas — pero es cualitativamente otra cosa:

- Tiene **licencia MIT** (el problema del gap 2 era justamente que los proyectos LATAM no la ponían).
- Tiene **respaldo institucional verificado**: Grupo Sirius, Universidad Tecnológica de Pereira (`sirius.utp.edu.co`, perfil de la organización declara Pereira, Colombia).
- Tiene **un caso de uso específico y no genérico**: educación superior **rural** en Risaralda, integrado dentro de Open edX, con TTS y avatar porque el contexto lo pide.

Que un laboratorio universitario colombiano publique MIT e integre contra Open edX es exactamente el tipo de contraparte que un engagement LATAM necesita. **Las estrellas no son la métrica acá; la gobernanza del proyecto sí, y esta vez está.**

### Lo que se refina: EMEA sí produce artefactos agénticos, pero son *benchmarks y esquemas*, no tutores

El gap 3 decía que "EMEA no produce agentes, produce plataformas". Con lo de este pase, la formulación correcta es más útil: **EMEA produce la capa de evaluación y de conformidad.** MathTutorBench (Suiza), UnifyingAITutorEvaluation y AITutor-EvalKit (Abu Dhabi), OpenDidactia (España), education-agent-skills (UK), y ahora **OpenTutorAI-CE confirmado en Marruecos**. Ninguno es un tutor de producto; todos son *cómo se mide o cómo se acredita* un tutor. Encaja con que EMEA es donde la regulación muerde.

### Dos regiones cerradas en agentes que ya estaban en la KB

- **OpenTutorAI-CE → EMEA (Marruecos).** El perfil de la organización `Open-TutorAi` declara `Morocco` y `opentutorai.com`. Explica el soporte multilingüe árabe/francés/inglés que la KB ya había registrado sin conectarlo.
- **Claw-ED → North America (Nueva York, EE. UU.)**, con la confianza declarada: el perfil **no** publica ubicación, pero los repos hermanos del mismo autor son un portal del *NYS Seal of Civic Readiness* "built for Great Neck Public Schools" y un juego de repaso de **Regents** y AP. Se registra como inferido de artefactos, no como declarado.

Quedan tres sin cerrar tras buscarlo explícitamente: **Bloom**, **OpenTutor** y **tutor-mcp** no declaran ubicación en el perfil ni en el repo, y no hay artefacto que lo evidencie. Se deja como gap, no como silencio.

### Sin movimiento: los dos grandes están planos

**DeepTutor 40.6k ★ y OpenMAIC 39.7k ★ — exactamente los mismos números que el pase 3**, horas antes. Es lo esperable dentro del mismo día y se registra para que la serie no tenga un hueco: la ventana de esta corrida no midió crecimiento, midió cobertura. DeepTutor sigue en v1.6.12 (2026-09-27) y OpenMAIC en v1.1.2 (2026-09-28).

### Corrección de licencia que vale registrar

**FreeLingo se publica como MIT en prensa y agregadores; la página del repo dice AGPL-3.0.** Se tomó la del repo. Es el modo de falla que esta KB ya se impuso evitar: la licencia se lee en el repo, no en el listicle.

---

## 2026-09-30 (pase 3) — teacher-facing y grading: dos categorías que se abrieron

Tercera corrida del día. Objetivo declarado: buscar agentes net-new en las capas que las dos pasadas anteriores habían marcado como vacías. Se encontraron dos, y una de ellas mueve un gap. Todo verificado vía WebFetch contra la página del repo.

### Nuevos agentes verificados

| Agente | Repo | Licencia | Stars (2026-09-30) | Lenguaje | Qué es |
|--------|------|----------|--------------------|----------|--------|
| **Claw-ED** | https://github.com/SirhanMacx/Claw-ED | MIT | **59** | Python | Agente CLI **local-first para docentes**. Se apunta a una carpeta de lecciones viejas, infiere el estilo de enseñanza del docente y emite el bundle completo: plan, handouts, versiones diferenciadas, juegos, evaluaciones, como DOCX de docente + DOCX de alumno + PPTX de slides en una corrida. 48+ tools, alineación a estándares estatales, cualquier provider LLM, bot de Telegram con la misma memoria. v9.18.2026.1 (Beta), 778 commits. `pip install clawed` |
| **AI-Teaching-Agent** | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT | **0** | Python | Markdown → artefactos **Lab / Exam / Grading como DSL validado**, más slides opcionales. Human review obligatorio, evaluación sandboxeada, servidor **MCP stdio** con adaptadores de tools, previews de examen *candidate-safe* que excluyen respuestas y referencias internas de corrección. 30 commits |

### Por qué Claw-ED importa más que sus 59 estrellas

**Es el primer agente teacher-facing open source de esta KB, y llega a la capa donde el mercado cerrado no tiene competencia.** `intel/market.md` ya venía diciendo que las herramientas *para docentes* son "el ángulo menos disputado" y que MagicSchool lidera ahí con poco foso. Esta pasada buscó el equivalente abierto y confirmó que **el segmento entero es propietario**: MagicSchool, Brisk, Diffit, Curipod, Eduaide.AI, SchoolAI, Taskade. Claw-ED es la única entrada open source que apareció.

Tres cosas lo vuelven propuesta y no curiosidad:

1. **Ataca el rechazo docente en su causa real.** La objeción no es "la AI genera material malo", es "genera material que no suena a mí". Un agente cuyo insumo son *las lecciones anteriores del propio docente* invierte esa objeción en un argumento de venta.
2. **Local-first, y eso resuelve dos problemas de una.** El corpus histórico del docente —su propiedad intelectual— no sale de la máquina. Sirve igual para el pudor profesional y para residencia de datos en EMEA.
3. **No toca al alumno.** Produce borradores que un docente aprueba. Queda fuera del alcance de las restricciones de decisión automatizada de Oklahoma, Maryland, el Annex III europeo y la AI Basic Act coreana. **Es el patrón con menos superficie regulatoria de toda la KB** — ver **P8** en `compose/patterns.md`.

⚠️ **59 ★ y un solo autor.** Verificar continuidad antes de un contrato largo y presupuestar el costo de mantenerlo forkeado.

### AI-Teaching-Agent: 0 estrellas, pero es la primera señal en la categoría de grading

El gap 6 (pase 2) concluyó que no existe grading open source con tracción y que el camino realista es **orquestar al incumbente propietario** vía `gradescope-mcp`. **Eso no cambia.** Lo que cambia es que apareció el primer intento de la estrategia opuesta: en vez de llamar a un grader externo, **generar el artefacto de corrección como DSL auditable**, con revisión humana en el medio y preview de examen sin respuestas.

El diseño es exactamente el que piden el EU AI Act y los estatutos de EE. UU. que prohíben grading automático. Pero **0 estrellas y 30 commits es un proyecto de una persona**: se registra, no se usa. Re-verificar el próximo ciclo. Si en tres meses sigue en 0, es un experimento abandonado; si pasa a 200, es la semilla de la categoría.

### Corrección de procedencia — OpenMAIC fue AGPL-3.0 hasta hace tres meses

La KB registra OpenMAIC como MIT, y lo es. Lo que faltaba: **fue relicenciado de AGPL-3.0 a MIT en v0.3.0, el 2026-06-28.** La licencia permisiva tiene ~3 meses, no la vida del proyecto.

No cambia la recomendación —MIT es MIT— pero sí lo que hay que decir en una due diligence: si el cliente audita procedencia de software, **declarar que el historial previo a junio de 2026 es AGPL-3.0**. Combinado con el gap 4 (concentración de la oferta en instituciones chinas: OpenMAIC es de Tsinghua), es el tipo de dato que conviene poner sobre la mesa temprano y no descubrir en revisión legal.

Releases recientes, para contexto de madurez: v1.1.0 trajo chat de aula sobre un agent loop con referencias a elementos de slide y pizarra durante playback; **v1.1.1 y v1.1.2 son los dos de seguridad** — política de direcciones públicas en uploads a MinerU Cloud, validación de redirects, y validación de base URLs provistas por el caller en parsing de PDF y rutas de provider para prevenir SSRF. Un proyecto que endurece contra SSRF está recibiendo reportes de seguridad reales.

### Lo que esta pasada buscó y no encontró

- **Agente educativo net-new con tracción alta (>1k ★).** No apareció ninguno que la KB no tuviera ya. Los tres líderes siguen siendo DeepTutor, OpenMAIC y NOMAD, y el resto del campo está por debajo de 1k. La distribución del sector es extremadamente bimodal: tres repos de ~40k y una cola larga de menos de 1k, sin nada en el medio.
- **Agente de origen LATAM con tracción.** Sin cambios respecto del pase 2: el gap 2 sigue abierto.
- **DeepTutor v1.6.12 sigue siendo la última release** (2026-09-27), con 40.6k ★ sin cambio medible en la ventana. Agrega Kiwix, reubicación de knowledge base del workspace, render de figuras de fuente, Task Board de progreso, interfaz en alemán y recuperación de chat.

## 2026-09-30 (pase 2) — segunda pasada de verificación

Segunda corrida del día. Objetivo: resolver las pistas que la pasada anterior dejó abiertas y buscar agentes net-new. Todo verificado vía WebFetch contra la página del repo (`curl` a github.com devuelve 403 a través del proxy de esta sesión, incluso para repos que existen — no sirve como verificador).

### Nuevo agente verificado

| Agente | Repo | Licencia | Stars (2026-09-30) | Qué es |
|--------|------|----------|--------------------|--------|
| Bloom | https://github.com/Li-Evan/Bloom | MIT | 278 | Tutor personal que genera un syllabus estructurado, entrega una lección a la vez, lee las anotaciones y el feedback del alumno y ajusta la siguiente lección al nivel real de comprensión. Dos modos: CLI como **skill de Claude Code** (sin backend) y web self-hosted (React + FastAPI, cualquier LLM OpenAI-compatible). Se apoya explícitamente en el "2 sigma" de Benjamin Bloom |

**Por qué importa más que sus 278 estrellas.** Es el segundo caso en dos pasadas de *pedagogía distribuida como skill de agente* en vez de como producto (el primero fue `education-agent-skills`). El modo CLI no tiene backend: el harness del agente **es** el producto. Para un studio esto baja el costo de un piloto de tutoría de "desplegar una plataforma" a "instalar una skill".

### Corrección de licencia y stars — OpenTutorAI-CE

El ciclo 3 lo registró como `Apache-2.0, ~600 ★`. Verificado hoy: **BSD-3-Clause, 107 ★**. Las dos cosas estaban mal. BSD-3 sigue siendo permisiva, así que el repo es usable; el dato de tracción estaba inflado ~6x.

### Agentes educativos de origen LATAM — el gap se confirma, con mejor evidencia

La pasada anterior declaró que no había agentes educativos open source de origen latinoamericano con tracción medible. Esta pasada buscó explícitamente en español y portugués. **Resultado: sí existen, y todos están pre-tracción.**

| Repo | Origen | Licencia | Stars | Estado |
|------|--------|----------|-------|--------|
| https://github.com/H1bertto/professor-agent | Brasil | MIT | 0 | Tutor local con avatar 2D/3D superpuesto al escritorio, por voz, con provider propio. TypeScript |
| https://github.com/ANTONIOALGMAR/StudyAgent | Brasil | **sin licencia** ⚠️ | 2 | Tutor multimodal 100% local sobre Ollama: voz bidireccional, visión de pantalla/cámara, PDFs, corrección automática, flashcards con repetición espaciada, gamificación |

`studyield/studyield` apareció en los resultados de búsqueda como plataforma self-hosted en 12 idiomas: **la URL da 404.** No es un finding.

**El gap declarado cambia de forma, no de conclusión.** Antes era "no encontramos ninguno". Ahora es más preciso y más útil: **hay iniciativas reales en Brasil, pero ninguna pasa de 2 estrellas y al menos una no tiene licencia** — sin licencia no hay permiso de uso, así que no es reutilizable ni siquiera si el código sirviera. El espacio sigue abierto y ahora sabemos que la demanda de constructores existe: no falta interés, falta masa crítica y gobernanza de proyecto.

### Gap confirmado: no hay agente de grading open source con tracción

Se buscó específicamente grading/assessment automatizado open source con licencia permisiva. La capa de corrección sigue siendo **propietaria**: Gradescope (Turnitin), Codio, Kangaroos AI. Lo que hay en abierto son *papers* (arXiv 2601.00730, 2607.02432, 2506.07955), no repos con adopción.

Esto explica por qué `gradescope-mcp` (8 ★) vale seguirlo pese a su tamaño: **el camino realista hacia grading agéntico hoy es un MCP contra el incumbente propietario, no un reemplazo open source.** Consecuencia para propuestas: no prometer sustituir Gradescope; prometer orquestarlo.

## 2026-09-30 — verificado a mano (WebFetch, repo por repo)

Lo nuevo y lo que se movió en esta ventana:

| Agente | Repo | Licencia | Stars (2026-09-30) | Qué cambió |
|--------|------|----------|--------------------|------------|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 40.6k | v1.6.12 el 2026-09-27. Cadencia de release semanal, 2.386 commits. Pasó de ~20k ★ (abr-2026, 111 días desde el lanzamiento) a 40.6k: duplicó en ~5 meses |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 39.7k | v1.1.2 el 2026-09-28, release de **seguridad** (validación en provider routing y descarga de media). Señal de madurez: ya recibe reportes de seguridad, no sólo features |
| Project NOMAD | https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | 38.8k | ~34.4k ★ en jul-2026 → 38.8k ahora (+4.4k en ~2 meses). Educación offline-first con AI local es una categoría en crecimiento real, no un nicho |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 ⚠️ | 814 | 165 skills pedagógicas consumibles por Claude Code / MCP / Codex / Hermes. Primer caso que vemos de *pedagogía empaquetada como skills de agente* en lugar de como prompt |
| gradescope-mcp | https://github.com/Yuanpeng-Li/gradescope-mcp | MIT | 8 | Nuevo y minúsculo, pero es el primer MCP que vemos sobre un sistema de grading de producción real (Gradescope, 34 tools). Vale seguirlo, no usarlo todavía |

**Los tres líderes (DeepTutor, OpenMAIC, NOMAD) están los tres entre 38k y 41k ★ y ninguno existía con esa masa hace un año.** La tutoría open source dejó de ser terreno académico de bajo star-count.

### Corrección importante de esta corrida

Los star counts de ciclos anteriores estaban inflados por el pipeline, no medidos. Educhain se había registrado con ~12k ★ y tiene **389**; OATutor con ~1.5k y tiene **265**; OpenTutor con ~900 y tiene **127**. Ver la tabla de corrección en `agents/top.md`.

## 2026-07-02 — pipeline automático (histórico, sin verificar)

⚠️ Salida cruda del pipeline. Conservada como historia. Varias filas son repos de 0–2 estrellas y al menos una (`claude-war-room`, `aulalibre`) no es de educación. No usar como recomendación.

| Nombre | Licencia | Descripción | Stars |
|--------|----------|-------------|-------|
| [ai4kids](https://github.com/alfredang/ai4kids) | ? | 🤖 AI Kids Academy — a kids' AI learning portal (ages 4–16): gamified AI storyte | 1 |
| [flashcards-open-source-app](https://github.com/kirill-markin/flashcards-open-source-app) | MIT | AI-powered flashcards app built for serious daily study on iOS, Android, and the | 24 |
| [vacademy_platform](https://github.com/Vacademy-io/vacademy_platform) | AGPL-3.0 | Open source comprehensive e-learning platform with a focus on educational conten | 14 |
| [Edyfra](https://github.com/marsley01/Edyfra) | ? | Edyfra is a modern, modular web application built primarily in TypeScript and Ja | 2 |
| [claude-war-room](https://github.com/digestionadiabaticprocess828/claude-war-room) | MIT | Orchestrate six specialized AI agents to analyze code features from multiple ang | 2 |
| [PS-HK19_MindForge_MindForge](https://github.com/iqiipo-dev/PS-HK19_MindForge_MindForge) | ? | Provide context-based, accurate answers to syllabus questions using AI powered b | 2 |
| [unlimited-ai-platform](https://github.com/Ahmed-html/unlimited-ai-platform) | MIT | Build and deploy a Next.js AI chat platform with authentication, role management | 1 |
| [LearnX-Radar](https://github.com/Yusuprozimemet/LearnX-Radar) | MIT | LearnX-Radar is an automated “daily learning radar” for developers that tracks t | 0 |
| [STUTIFY](https://github.com/myxineglutinosameniere4389/STUTIFY) | ? | Convert text into natural speech with this automated stuttering and fluency tool | 0 |
| [aulalibre](https://github.com/loqganesh-hue/aulalibre) | MIT | Access Denmark's Aula with Rust tools, a CLI, and a FUSE mount for messages, fil | 0 |

---
*Historia conservada. Append-only: agregar arriba, nunca sobrescribir.*
