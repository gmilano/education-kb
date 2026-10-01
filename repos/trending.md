---
industry: education
region: Global
updated: 2026-10-01
---

# 📈 Repos trending — education

> **APPEND-ONLY.** Cada corrida agrega una sección fechada arriba y conserva la historia abajo.

## 2026-10-01 (pase 6) — la capa de datos de aprendizaje, que estaba en un estándar IEEE y no en la KB

Sexta corrida del día. El hallazgo de repos de este pase no es un proyecto nuevo y llamativo: es **una capa entera de infraestructura madura que las cinco pasadas anteriores no registraron**, porque se buscaba por "agente", "tutor" y "benchmark", y esta capa no se llama así. Se llama **Learning Record Store**.

### Por qué no había aparecido antes

Las pasadas 1–5 construyeron el stack de arriba hacia abajo: plataforma (Moodle, Open edX) → agente (DeepTutor, OpenMAIC) → modelado (pyKT, pyBKT) → medición (MathTutorBench, EduBench) → modelo fundacional (OmniEdu). Nunca se preguntó **dónde se escriben los eventos** que alimentan el modelado. La respuesta lleva quince años estandarizada: **xAPI**, hoy **IEEE 9274.1.1**.

Es la misma lección de método del pase 3 con GegoK12, en otra forma: buscar la categoría que uno tiene en la cabeza devuelve lo que uno ya sabe. **Acá el error no fue la consulta sino el mapa** — faltaba una capa en el modelo mental del stack, así que nunca se buscó.

### Los cuatro LRS verificados

Todos verificados de primera mano en GitHub en este pase (licencia, stars y commits leídos del repo):

| Repo | Licencia | Stars | Commits | Lenguaje | Mantenedor | Por qué importa |
|---|---|---|---|---|---|---|
| https://github.com/LearningLocker/learninglocker | **GPL-3.0** ⚠️ | 583 | 3.254 | JavaScript | Learning Pool | El canónico de la categoría, desde 2014. El más adoptado — y copyleft, así que el servicio que lo toque hereda la obligación |
| https://github.com/adlnet/ADL_LRS | **Apache-2.0** ✅ | 331 | 1.885 | Python | **ADL** (EE. UU.), autor del estándar | Implementación **de referencia**, con soporte IEEE 9274.1.1 / xAPI 2.0. ⚠️ El repo declara ser *proof of concept* para pocos usuarios |
| https://github.com/yetanalytics/lrsql | **Apache-2.0** ✅ | 143 | 2.268 | Clojure | Yet Analytics | **El candidato de producción permisivo.** Corre sobre SQLite, PostgreSQL 14–18, MariaDB y MySQL 8–9.5. Copyright © 2021–2026: mantenimiento vivo |
| https://github.com/openfun/ralph | **MIT** ✅ | 50 | 714 | Python | **OpenFun** (France Université Numérique) | El único MIT, y el que **convierte tracking logs de Open edX a xAPI** de fábrica. Mismo origen que Richie, que esta KB ya listaba |

**Tres de los cuatro son permisivos.** Después de cinco pasadas peleando con AGPL en plataformas y CC BY-SA en benchmarks, esta capa se puede adoptar sin pasar por legal — con la salvedad de que el más adoptado (Learning Locker) es justamente el copyleft.

### El dato de arquitectura que cambia una propuesta

`Ralph` viene de **OpenFun**, la misma organización francesa que publica `Richie` (MIT), ya listada en `verticals/solutions.md`. Para un engagement EMEA sobre Open edX eso significa que **la capa pública (Richie), la plataforma (Open edX) y la telemetría (Ralph) tienen integración probada entre sí**, y dos de las tres son MIT. Es la primera vez que esta KB puede ofrecer una cadena vertical coherente y de un mismo origen regional.

### Un repo más, chico, que cierra el circuito

https://github.com/DavidLMS/learnmcp-xapi — **MIT**, **15 ★**, 32 commits, Python. Servidor MCP que expone un LRS a un agente (registrar statement / consultar progreso / gestionar vocabulario), con backends para `lrsql` y `Ralph`, los dos permisivos de la tabla de arriba. Autor: docente del **IES Rafael Alberti** (España). Detalle completo en `agents/trending.md` de este mismo pase.

Es chico y hay que decirlo: **15 estrellas y 32 commits no es una dependencia de producción**. Pero a diferencia de los cinco servidores MCP de mastery del pase 5 —que sumaban 3 estrellas y 23 commits **entre los tres más grandes** e implementaban cada uno su propia heurística— este no reinventa el almacén: se apoya en el estándar. Como referencia de integración vale; como base a forkear, también, porque es MIT y son 32 commits que se leen en una tarde.

### Lo que se buscó y no apareció en este pase

- **`pyKT` o `pyBKT` expuestos detrás de MCP o de un LRS**: siguen sin existir. El gap 5 se mantiene abierto, pero más chico (ver `intel/trends.md`).
- **Un LRS con estimación de mastery incorporada**: ninguno de los cuatro la tiene. Son almacenes conformes al estándar, no motores de inferencia. La separación es correcta desde el diseño, pero significa que el estimador **siempre** es trabajo propio.
- **Repos de FP (formación profesional) con tracción**: 24 repos en total, techo de 2 ★. Detalle en `agents/trending.md`.
- **Repos educativos LATAM con tracción**: se volvió a medir, en español. 20 repos, **ninguno pasa de 1 estrella**. Detalle en `intel/trends.md`, gap 2.

## 2026-09-30 (pase 5) — un modelo fundacional educativo abierto, y la capa de grading deja de ser un hueco vacío

Quinta corrida del día. Dos hallazgos de repo que no son incrementales: **aparece una familia de modelos fundacionales open para K-12** (capa que la KB no tenía en absoluto: tenía plataformas, agentes, modelado y medición, pero ningún modelo entrenado para educación), y **la capa de grading deja de ser un gap puramente vacío** — aunque lo que aparece obliga a leer licencias con más cuidado que en cualquier pasada anterior.

### OmniEdu — modelos fundacionales abiertos para K-12, y sin licencia declarada

| Repo | Licencia | Stars | Commits | Qué es |
|---|---|---|---|---|
| https://github.com/haolpku/Omni-Edu | ⚠️ **sin licencia declarada** | 48 | 2 | Familia de modelos fundacionales para enseñanza y aprendizaje K-12. **Tres checkpoints: 4B, 9B y 27B** |

Lo verificado de primera mano en el repo:

- Los checkpoints se construyen sobre **Qwen3.5-4B-Base, Qwen3.5-9B-Base y Qwen3.8-27B**, y los pesos están alojados en HuggingFace bajo `lhpku20010120/`.
- La mezcla de instrucciones es **pública**: 69.999 ejemplos y 15,96M tokens de respuesta supervisada, de 100+ fuentes (60.951 específicos de educación + 9.048 de propósito general).
- La supervisión se organiza en cuatro capacidades: competencia en la materia, anclaje curricular, razonamiento diagnóstico y acción pedagógica/andamiaje.
- Origen: **Universidad de Pekín, University of the Chinese Academy of Sciences y Zhongguancun Academy** (Hao Liang, Qihan Lin et al.).

Dato de conexión con la KB: según el paper, **OmniEdu-27B alcanza 78,74% en el setting Scaffold de MathTutorBench** — el benchmark que el pase 4 agregó a `repos/foundations.md`. Es la primera vez que un artefacto de esta KB se evalúa contra otro artefacto de esta KB.

⚠️ **Dos problemas de licencia, no uno, y los dos son bloqueantes hasta que se resuelvan:**

1. **El repo no declara licencia.** Sin archivo LICENSE, el default legal es "todos los derechos reservados", por mucho que el título diga *Open Foundation Models*. "Abierto" acá significa *los pesos se pueden descargar*, no *se pueden usar comercialmente*.
2. **Los pesos heredan la licencia del modelo base.** Están construidos sobre bases Qwen, cuyas licencias no son uniformes entre tamaños y no son todas Apache-2.0. Aun si el repo declarara MIT mañana, eso no levantaría la restricción del base model.

**Cómo tratarlo en una propuesta:** como la mejor evidencia disponible de que **un modelo chico y especializado puede competir con uno grande y genérico en tareas pedagógicas** —que es un argumento de costo muy fuerte para un ministerio o un distrito— y **no** como un componente desplegable. Si el cliente necesita un modelo educativo propio, esto es la receta a replicar (el corpus y las cuatro capacidades están descritos), no el artefacto a instalar. Refuerza además el **gap 4**: la concentración APAC ya no es sólo de agentes y de modelado, ahora también de modelos fundacionales.

### La capa de grading: tres repos nuevos y ninguno limpio

El gap 6 (y su actualización, el gap 9) viene diciendo desde el pase 2 que **no hay grading open source con tracción** y que la recomendación operativa es *orquestar Gradescope, no reemplazarlo*. Esta pasada buscó por licencia y stack en vez de por categoría. Lo que apareció **no cierra el gap, pero lo vuelve mucho más preciso**:

| Repo | Licencia | Stars | Commits | Estado real |
|---|---|---|---|---|
| https://github.com/paper-instruments/rubric | **MIT** ✅ | **75** | 64 | Librería de evaluación con **rúbricas ponderadas**: scoring criterio por criterio, single-pass y juicio holístico, validación con Pydantic, cualquier proveedor LLM. **No es educativa** — es genérica de LLM-as-judge. Es la pieza permisiva más útil de la tabla |
| https://github.com/sdrangan/llmgrader | ⚠️ **PySilicon Research License** (custom, no OSI) | 2 | **240** | Autograder para cursos de ingeniería: derivaciones multi-paso, trade-offs de diseño, justificación abierta. Problemas y rúbricas como **XML estructurado**, trazas de corrección transparentes, **servidor MCP** para autoría asistida e **integración con Gradescope**. De Sundeep Rangan (NYU), **desplegado en un curso de maestría real** |
| https://github.com/Dmoayad/essay-grader-llm | GPL-3.0 ⚠️ | 1 | 12 | Corrección de ensayos con rúbrica + RAG comparando contra material de referencia, FastAPI/Gradio/LangChain. Incluye detección de plagio |

**El hallazgo incómodo es `llmgrader`.** Es, de largo, el grading agéntico más maduro que esta KB encontró en cinco pasadas: 240 commits, en producción en un curso de NYU, con MCP y con la integración a Gradescope que el gap 6 recomienda construir. Y su licencia es una **"PySilicon Research License" propia, © 2026 Sundeep Rangan** — verificado leyendo el archivo LICENSE. **No es OSI, no es MIT/Apache/BSD, y no se puede usar en un entregable de cliente.**

Que el proyecto más avanzado de la categoría tenga licencia de investigación custom **explica por qué el gap 6 se sostuvo cuatro pasadas**: no es que nadie construyera grading agéntico, es que quien lo construyó bien no lo liberó de forma reutilizable. Es una corrección de diagnóstico que vale tanto como un repo nuevo.

**La recomendación operativa cambia poco pero se vuelve más concreta:** seguir orquestando Gradescope (vía `gradescope-mcp`, MIT, 8 ★), y cuando haya que construir la capa de juicio, **construirla sobre `paper-instruments/rubric` (MIT, 75 ★)** en vez de desde cero. Es genérica, así que la pedagogía hay que aportarla — y para eso ahora están EduBench y SafeTutors (ver `agents/trending.md`, pase 5).

### Contexto: la infraestructura de autograding clásica ya existe y no es AI

Verificado en esta pasada porque conviene no confundir capas en una propuesta:

| Repo | Licencia | Stars | Commits | Qué es |
|---|---|---|---|---|
| https://github.com/eecs-autograder/autograder.io | ⚠️ no declarada en este repo (es el repo de documentación e issues) | **79** | 61 | Sistema de autograding **basado en casos de test, no en LLM**. Sandboxing con Docker, feedback configurable, entregas en grupo, hand-grading. Mantenido por el departamento de CS de la **Universidad de Michigan**, que lo usa para **~5.000 alumnos por semestre en una docena de cursos** |

No es un competidor de Gradescope con AI: es la plomería determinista sobre la que una capa AI podría montarse. Es relevante porque tiene **volumen real verificable** —el dato de 5.000 alumnos/semestre es el único número de escala de producción de toda la capa de grading de esta KB— y porque para código, el autograding determinista sigue siendo mejor que un LLM. El ángulo AI correcto acá es **feedback y explicación sobre tests que ya pasaron o fallaron**, no reemplazar los tests.

### Nota de método

- **`curl -sI` contra github.com devuelve 403** a través del proxy de egreso (confirmado otra vez en este pase, ya lo había anotado el pase 4). Verificación por WebFetch contra la página del repo.
- **Dominios bloqueados por el proxy en esta corrida:** `arxiv.org`, `openreview.net`, `aclanthology.org`, `huggingface.co`, `ojs.aaai.org`, `mcml.ai`, `unu.edu`, `coe.int`, `digitaleducationcouncil.com`, `mcpservers.org`. Todo lo de esta sección que sale de github.com está verificado; los números de papers y los pesos en HuggingFace no pudieron abrirse en la fuente primaria.
- **Licencias leídas en el archivo, no inferidas del badge**, en los dos casos donde importaba: `llmgrader` (PySilicon Research License) y `awesome-ai-llm4education` (404, no existe LICENSE). En los dos, el badge o la apariencia del repo sugería algo distinto de lo que dice el archivo. **Leer el LICENSE sigue siendo la única verificación válida.**

## 2026-09-30 (pase 4) — aparece la capa de medición, y tenía cuatro años de antigüedad

Cuarta corrida del día. El hallazgo principal de esta ventana **no es un repo nuevo**: es un repo maduro que la KB nunca había mirado porque buscaba en la categoría equivocada.

### pyKT — 441 ★, MIT, y el gap 5 lo estaba pidiendo desde el pase 1

https://github.com/pykt-team/pykt-toolkit · **MIT** · **441 ★** · Python · 811 commits

El gap 5 de `intel/trends.md` viene diciendo desde la primera pasada: *"No hay integración madura entre knowledge tracing y agentes LLM. `py-fsrs` y OATutor resuelven retención y mastery; los agentes grandes resuelven conversación. Nadie los cosió bien."*

La segunda mitad sigue siendo cierta — **nadie los cosió**. La primera mitad estaba mal planteada: la KB tenía como única pieza de mastery a **OATutor** (265 ★, un ITS completo con BKT adentro) y a **py-fsrs** (499 ★, scheduling). Faltaba la librería de *knowledge tracing* propiamente dicha, y existe desde 2022:

- **10+ modelos DLKT** comparables entre sí (DKT, SAKT, AKT, simpleKT y demás), no un solo algoritmo embebido en un producto.
- **7+ datasets** con preprocesamiento estandarizado y **5 escenarios de predicción** — o sea, resultados reproducibles, que es lo que hace falta para defender una afirmación de eficacia ante un cliente.
- Publicado en **NeurIPS 2022** (Liu, Liu, Chen, Huang, Tang, Luo) y mantenido: 811 commits.
- **MIT**, sin fricción de licencia.

**Origen: Jinan University, Guangdong Institute of Smart Education (China) → APAC.** Zitao Liu es Profesor y Decano de ese instituto; el trabajo tuvo apoyo del Key Laboratory of Smart Education of Guangdong. Refuerza el gap 4 (concentración APAC de la oferta), ahora también en la capa de modelado y no sólo en tutores.

**Por qué importa más que sus 441 estrellas.** Es la diferencia entre un tutor que *parece* adaptativo y uno que puede demostrar que lo es. Bajo EU AI Act, un sistema de educación en Anexo III tiene que documentar cómo decide; "el LLM decidió" no es documentación, y una curva de mastery de un modelo DLKT publicado sí lo es. Ver el nuevo patrón **P10**.

### Los dos benchmarks pedagógicos que faltaban

| Repo | URL | Licencia | Stars | Venue |
|------|-----|----------|-------|-------|
| **MathTutorBench** | https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | 42 | EMNLP 2025 (Oral) |
| **UnifyingAITutorEvaluation** | https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | 32 | NAACL 2025 (Senior Area Chair Award) |

El segundo es **del mismo autor que `AITutor-EvalKit`**, el repo de 3 ★ que la KB venía citando como "el único evaluador pedagógico que existe". Era el repo chico del mismo trabajo. Corregido en `agents/top.md`.

### Lo demás de la ventana

- **FreeLingo** (https://github.com/artcc/freelingo, **AGPL-3.0**, 150 ★): Duolingo self-hosted con Ollama, CEFR, voz y repetición espaciada. Stack moderno (FastAPI + Next.js + Postgres + Redis en Docker Compose). **AGPL**, así que sirve como referencia de arquitectura, no como base de producto cerrado.
- **mentar** (https://github.com/avps82/mentar, AGPL-3.0, 1 ★, último commit 2026-08-26): 934 nodos de concepto en 157 plantillas curriculares (Australia ACARA v9, India, Singapur, EE. UU.). Idea de diseño que vale robar aunque el repo no se use: **el LLM sólo explica y un checker determinístico corrige**, de modo que el modelo no puede validar una respuesta incorrecta. Es la respuesta más simple que vimos al riesgo de alucinación en corrección.
- **TutorIA** (https://github.com/LabSirius/TutorIA, MIT, 0 ★) y **OpenDidactia** (https://github.com/nmarafo/OpenDidactia, CC BY-SA 4.0, 0 ★): cubiertos en `agents/trending.md` — mueven los gaps 2 (LATAM) y 3 (EMEA).
- **Sin movimiento en los grandes:** DeepTutor sigue en 40.6k ★ y OpenMAIC en 39.7k ★, idénticos al pase 3 de hoy. Se registra el dato plano para no dejar hueco en la serie.

### Nota de método — `curl -sI` no sirve para verificar en este entorno

El procedimiento estándar de esta KB es verificar cada URL con `curl -sI` antes de escribirla. **En esta corrida devuelve `403` para *todas* las URLs de github.com**, incluidas las de repos que sabemos vivos (DeepTutor, OpenMAIC, el propio `gegok12` verificado en el pase 3). O sea: el proxy de salida bloquea el `HEAD`, y un 403 uniforme **no distingue un repo real de uno inexistente** — usarlo como verificación daría falsos negativos en todo.

La verificación de este pase se hizo con **WebFetch contra la página del repo**, y se comprobó que el canal sí discrimina: una URL deliberadamente inexistente devolvió `HTTP 404 Not Found`, mientras que las 13 URLs reales devolvieron la página. **`api.github.com` también está fuera de alcance** (responde que el repo no está habilitado para la sesión), así que stars y licencia se leen de la página renderizada, no de la API.

---

## 2026-09-30 (pase 3) — un gap declarado se cae: aparece un SIS permisivo y vivo

Tercera corrida del día. El hallazgo principal no es un repo trending: es que **el gap 7 de `intel/trends.md` estaba mal** y hay que retirarlo.

### GegoK12 — el SIS open source permisivo que las dos pasadas anteriores dijeron que no existía

| Repo | URL | Licencia | Stars | Forks | Último commit | Stack |
|------|-----|----------|-------|-------|---------------|-------|
| **GegoK12** | https://github.com/Gego-K12/gegok12 | **MIT** ✅ | 54 | 97 | **2026-09-23** | PHP 8.4 + Laravel 12 |

Verificación: el archivo `LICENSE` del repo dice `MIT License`, con `SPDX-License-Identifier: MIT`, © 2025 GegoSoft Technologies and GegoK12 Contributors. 123 commits, 11 issues abiertos. School management / ERP completo, API-first, mobile-apps-ready, instalador visual en `/public/installer` o Docker. La organización mantiene además `gegok12-documentation` y **`Plugin-Hello-Teacher`** — o sea, **tiene sistema de plugins**, actualizado el 2026-09-23.

**Lo que esto retira.** El pase 2 declaró el gap 7 así: *"No hay SIS open source permisivo y vivo… en el lado administrativo el agente **siempre** va afuera, leyendo por API. No es preferencia de diseño, es la única opción limpia."* La conclusión era incorrecta. Con un core MIT y un punto de extensión por plugins, **el agente puede vivir adentro del SIS**, y como MIT no impone share-alike, ese plugin puede ser propiedad del cliente. Es la primera vez que la KB puede ofrecer eso en el lado administrativo. Patrón nuevo: **P9** en `compose/patterns.md`.

⚠️ **Y la condición que hay que leer antes de proponerlo: es open-core.** De 38 módulos, **26 están en el core MIT** (alumnos, admisiones, asistencia, tareas, biblioteca, staff, avisos, comunicación con padres) y **12 son add-ons Pro pagos, USD 100–250 cada uno** (USD 1.650 los doce): **examinación, gestión de fees**, timetable, media files, chat room, certificados, transporte, inventario, stock, video room, alumni y generador de exámenes. La licencia Pro es lifetime por dominio, con fuente incluido y 5 años de updates — no suscripción por alumno, que es razonable, pero **exámenes y cobranzas son justo los dos procesos que un agente querría automatizar primero**. Cotizarlos de entrada.

**Tracción, sin maquillaje:** 54 ★ con 97 forks. La proporción ~2:1 de forks sobre stars dice que se despliega más de lo que se estrella, lo cual es esperable en un ERP administrativo cuyo usuario es una escuela y no un desarrollador. Pero es un proyecto chico de un solo vendor (GegoSoft): riesgo de continuidad a declarar. **OpenEduCat (LGPL-3.0), más adoptado y con el agente afuera, sigue siendo la opción conservadora** y está bien elegirla.

### Por qué el gap se sostuvo dos pasadas — nota de método

Las dos pasadas anteriores buscaron la categoría ("SIS open source", "open source school ERP") y recibieron el consenso de los listicles, que repiten Fedena / RosarioSIS / openSIS y no incluyen GegoK12 porque es reciente. **Lo que lo encontró fue buscar por licencia y stack** — "school ERP MIT Laravel self-hosted" — no por categoría.

Regla que conviene aplicar al resto de la KB: **un gap de la forma "no existe X con licencia permisiva" hay que re-buscarlo con la consulta invertida.** Buscar la categoría devuelve el consenso establecido; buscar la licencia y el stack devuelve los proyectos nuevos, que son exactamente los que un gap de este tipo puede estar tapando. Candidatos a re-buscar así el próximo ciclo: el gap 1 (evaluador pedagógico) y el gap 6 (grading).

### Lo demás de la ventana: sin movimiento medible

Los cinco repos de la sección del pase 1 de hoy siguen en los mismos valores (LLMs-from-scratch 105.8k ★, minimind 63k, DeepTutor 40.6k, OpenMAIC 39.7k, NOMAD 38.8k) y los tres del pase 2 también (learn-claude-code 77.8k, ai-engineering-from-scratch 62.1k, tiny-llm 4.7k). Tres pasadas en un día no mueven star counts: la cadencia útil de este archivo es semanal, no horaria. **La próxima corrida conviene que priorice categorías sin cubrir antes que re-medir los mismos repos.**

Adyacente que apareció y **no** pasa a `foundations.md` por no ser de educación: `microsoft/mcp-for-beginners` — currículum open source de MCP con ejemplos en .NET, Java, TypeScript, JavaScript, Rust y Python. Es material de AI literacy técnica genuinamente útil para un track de formación, pero es de protocolo, no de educación, y no verificamos licencia ni stars de primera mano. Pista para la próxima corrida.

## 2026-09-30 (pase 2) — pistas pendientes, resueltas

La pasada anterior dejó tres repos anotados como "pista para la próxima corrida" porque no había podido verificar licencia y stars de primera mano. **Los tres son reales, permisivos y grandes.** Verificados vía WebFetch contra la página del repo.

| Repo | URL | Licencia | Stars (2026-09-30) | Lenguaje | Qué es |
|------|-----|----------|--------------------|----------|--------|
| learn-claude-code | https://github.com/shareAI-lab/learn-claude-code | MIT | **77.8k** | Python | Tutorial progresivo de 17 capítulos sobre cómo se construye un *harness* de agente: tools, gestión de conocimiento, sistema de tareas, coordinación de equipos. Tesis explícita del repo: "agency comes from model training, not external orchestration" |
| ai-engineering-from-scratch | https://github.com/rohitg00/ai-engineering-from-scratch | MIT | **62.1k** | Python | Curriculum de AI engineering: **523 lecciones en 20 fases**, de fundamentos matemáticos a agent engineering. Exige implementar los algoritmos a mano antes de usar frameworks de producción; cada lección deja un artefacto reusable (prompts, skills, agents, MCP servers) |
| tiny-llm | https://github.com/skyzh/tiny-llm | Apache-2.0 | 4.7k | Python | Curso de **serving** de LLMs para ingenieros de sistemas: KV cache, continuous batching, flash attention, paged attention, sobre APIs de arrays MLX y sin capas de red neuronal de alto nivel. Construye una vLLM en miniatura con Qwen3 |

**Lo que estos tres cambian para la KB.** La sección de AI literacy de `repos/foundations.md` tenía dos entradas (`LLMs-from-scratch`, `minimind`), las dos sobre *entrenar* un modelo. Estos tres cubren las capas que faltaban y que son las que un cliente corporativo realmente necesita:

- **`ai-engineering-from-scratch`** → el currículum completo, ya secuenciado en 20 fases. Es lo más cercano a un programa de capability building listo para usar que hay en abierto con licencia MIT.
- **`learn-claude-code`** → cómo se construye la infraestructura de agentes. 77.8k ★ lo vuelve el material de referencia de facto del tema.
- **`tiny-llm`** → operar e inferir eficientemente, que es donde se va el costo en producción. Nota: usa **MLX (macOS ARM64)**, así que como material de aula obliga a hardware Apple — verificar antes de comprometerlo en un programa.

Los tres son MIT o Apache-2.0: curricularizables sin fricción legal.

## 2026-09-30 — GitHub trending, ventana de septiembre 2026

Verificado vía WebFetch más agregadores de trending (`agents-radar`, `gittok`) para la ventana 2026-09-22 → 2026-09-30.

| Repo | URL | Licencia | Stars | Por qué aparece |
|------|-----|----------|-------|-----------------|
| LLMs-from-scratch | https://github.com/rasbt/LLMs-from-scratch | Apache-2.0 | 105.8k | El recurso de referencia para entender arquitectura transformer. Base de cualquier programa de AI literacy serio |
| minimind | https://github.com/jingyaogong/minimind | Apache-2.0 | 63k | LLM de 64M params entrenado desde cero en ~2h en hardware de consumo. Convierte "entrenar un modelo" en un ejercicio de aula |
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 40.6k | Trending sostenido; v1.6.12 del 2026-09-27 |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 39.7k | v1.1.2 del 2026-09-28 |
| Project NOMAD | https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | 38.8k | Servidor educativo offline-first con AI embebida; ~38.1k–38.8k en los conteos de esta semana |

Adyacentes que aparecieron en trending de educación AI sin que pudiéramos verificar licencia/stars de primera mano, y que por lo tanto **no pasan a `top.md`**: `shareAI-lab/learn-claude-code` (~77.8k ★ reportado), `rohitg00/ai-engineering-from-scratch`, `tiny-llm`. Registrados acá como pista para la próxima corrida.

## 2026-07-02 — pipeline automático (histórico, sin verificar)

⚠️ Salida cruda del pipeline. Conservada como historia. Idéntica a la de `agents/trending.md` de esa fecha — el pipeline escribía el mismo contenido en ambos archivos. Mayoría de repos con 0–24 estrellas. No usar como recomendación.

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
