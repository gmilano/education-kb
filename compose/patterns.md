---
industry: education
region: Global
updated: 2026-10-01
---

# 🧩 Patrones de composición — Education

> Recetas concretas: repos nombrados, licencias verificadas, wiring explícito y estimación.
> Todos los repos citados fueron verificados vía WebFetch el 2026-09-30 (ver `agents/top.md`).

## Patrón base

```
[Plataforma vertical open source: Moodle / Open edX / Kolibri / OpenOLAT]
          ↓  (punto de extensión: AI subsystem plugin · XBlock · LTI 1.3 — NUNCA fork del core)
[Servicio agéntico separado: proceso propio, licencia propia]
          ↓  (MCP / REST)
[Estado del aprendiz + scheduling de retención: tutor-mcp + py-fsrs]
          ↓
[Capa de auditoría: decisiones pedagógicas logueadas + AITutor-EvalKit]
          ↓
[UI conversacional encima de los flujos existentes, no en lugar de ellos]
```

**La regla que no se negocia:** el core copyleft (Moodle GPL-3.0, Open edX / Canvas / Frappe AGPL-3.0) no se modifica. La lógica propietaria vive en un servicio aparte. Esto mantiene el IP del cliente fuera del alcance de GPL/AGPL.

---

## P1 — Tutor adaptativo con retención real (el patrón de base)

**Problema.** Los tutores LLM explican bien y no hacen aprender: no hay modelo de mastery ni scheduling de repaso. Es el gap técnico #5 de `intel/trends.md`.

- **Punto de partida:** [DeepTutor](https://github.com/HKUDS/DeepTutor) (Apache-2.0, 40.6k ★) como workspace de tutoría
- **Estado del aprendiz:** [tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT, Go) — estado durable, misconceptions, metacognición, decisiones auditables
- **Retención:** [py-fsrs](https://github.com/open-spaced-repetition/py-fsrs) (MIT, 499 ★) — scheduling DSR con 21 parámetros optimizables
- **Mastery:** lógica de Bayesian Knowledge Tracing de [OATutor](https://github.com/CAHLR/OATutor) (MIT) + su contenido curado de OpenStax en JSON
- **Evaluación:** [AITutor-EvalKit](https://github.com/kaushal0494/AITutor-EvalKit) (MIT) — mide Mistake Identification, Mistake Location, Providing Guidance, Actionability

**Wiring.** DeepTutor conversa. `tutor-mcp` se monta como servidor MCP y es la **única** fuente de verdad del estado del aprendiz — DeepTutor no guarda mastery en su memoria, la consulta. Cada intento del alumno actualiza BKT (mastery) y alimenta `py-fsrs` (cuándo repasar). `py-fsrs` emite la cola de repaso que DeepTutor usa para abrir la sesión siguiente. Todas las decisiones pedagógicas se loguean con timestamp y razón. `AITutor-EvalKit` corre en CI contra MRBench como gate de regresión pedagógica.

**Tiempo estimado:** 8–10 semanas. **Licencias:** todo MIT/Apache-2.0 → sin fricción.

---

## P2 — Aula multi-agente sobre LMS existente

**Problema.** El cliente ya tiene Moodle con años de contenido y no lo va a reemplazar; quiere experiencia de clase interactiva encima.

- **Base:** Moodle (GPL-3.0) — **AI subsystem nativo**, no hay que construir la integración
- **Experiencia de aula:** [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (MIT, 39.7k ★) — convierte tema o documento en clase multi-agente
- **Pedagogía:** [education-agent-skills](https://github.com/GarethManning/education-agent-skills) (CC BY-SA 4.0 ⚠️) — 165 skills en 20 dominios
- **Contenido interactivo de salida:** [H5P](https://github.com/h5p/h5p-php-library) (GPL-3.0), ya embebible en Moodle

**Wiring.** Un plugin del AI subsystem de Moodle (provider plugin, no fork) expone el curso a OpenMAIC por API. OpenMAIC toma el material del curso y genera la sesión multi-agente; las skills de `education-agent-skills` se cargan como guía pedagógica de los agentes. La salida se materializa como actividades H5P dentro del curso Moodle, así que **persiste en la plataforma que el cliente ya administra** y sobrevive si se apaga el agente. Progreso y engagement vuelven por la API de Moodle.

⚠️ `education-agent-skills` es CC BY-SA 4.0: share-alike. Usar como referencia pedagógica; **revisar con legal antes de empaquetar derivados en un entregable cerrado.**

**Tiempo estimado:** 6–8 semanas. **Nota de procedencia:** OpenMAIC es de Tsinghua — declarar origen temprano si el cliente tiene restricciones de procedencia de software (ver gap #4).

---

## P3 — Tutoría offline-first (LATAM rural, África, Asia del Sur)

**Problema.** Conectividad no confiable, o prohibición de que datos de menores salgan de la red de la escuela. Un tutor que depende de una API remota no sirve.

- **Servidor de conocimiento:** [Project NOMAD](https://github.com/Crosstalk-Solutions/project-nomad) (Apache-2.0, 38.8k ★) — Wikipedia, libros, cursos, mapas en Docker. ~5 GB disco, <1 GB RAM sin AI
- **LMS offline:** [Kolibri](https://github.com/learningequality/kolibri) (MIT, 1.1k ★) — offline-first, licencia permisiva
- **Modelo local:** Ollama como provider; en LATAM, **Latam-GPT** (`latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0`) por contexto cultural en español/portugués — gratuito para instituciones públicas
- **Retención:** `py-fsrs` (MIT) — funciona offline por diseño, no necesita red

**Wiring.** NOMAD y Kolibri corren en un mini-PC en la escuela. Ollama sirve el modelo local en la misma máquina (acá está el techo de RAM: dimensionar por el modelo, no por NOMAD). Kolibri aporta currículo y tracking de progreso; NOMAD el corpus de referencia para RAG. `py-fsrs` mantiene la cola de repaso en SQLite local. **Cero tráfico saliente:** resuelve conectividad y residencia de datos con la misma arquitectura. Sincronización oportunista cuando hay red, no como requisito.

**Tiempo estimado:** 6–8 semanas para el primer sitio, 1–2 semanas por sitio adicional una vez fijada la imagen.

---

## P4 — Evaluación auditable bajo EU AI Act (EMEA)

**Problema.** La corrección automática y la predicción de deserción caen en el **Annex III** del EU AI Act; aplicable **2027-12-02**. La institución debe poder auditar. El entregable no es el modelo: es el expediente de conformidad.

- **Base:** [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (**Apache-2.0**, 444 ★, Suiza) — assessment serio + licencia permisiva + credibilidad DACH. La mejor base de esta KB para el caso
- **Decisiones auditables:** `tutor-mcp` (MIT) — decisiones pedagógicas con traza
- **Gate humano:** patrón de [gradescope-mcp](https://github.com/Yuanpeng-Li/gradescope-mcp) (MIT) — escrituras detrás de confirmación explícita
- **Evidencia de calidad:** **[UnifyingAITutorEvaluation](https://github.com/kaushal0494/UnifyingAITutorEvaluation)** (CC BY-SA 4.0, 32 ★) — taxonomía de **8 dimensiones** + dataset MRBench, NAACL 2025. *Corregido en el pase 4: este es el repo canónico; `AITutor-EvalKit` (MIT, 3 ★) es la implementación LoMTL sobre 4 de esas dimensiones y sirve como el ejecutable.* Para matemática, sumar **[MathTutorBench](https://github.com/eth-lre/mathtutorbench)** (CC BY 4.0, 42 ★, EMNLP 2025 Oral), que trae reward models y leaderboard
- **Evidencia de eficacia adaptativa:** **[pyKT](https://github.com/pykt-team/pykt-toolkit)** (MIT, 441 ★) — curva de mastery de un modelo DLKT publicado y reproducible. *Agregado en el pase 4:* es la diferencia entre documentar cómo decide el sistema y decir "lo decidió el LLM", que no es documentación
- **Modelo:** Ollama on-premise → sin transferencia de datos de menores a terceros

**Wiring.** OpenOLAT conserva la autoridad sobre la nota; el agente **propone** y nunca escribe la calificación final — el gate humano de `gradescope-mcp` es la arquitectura, no una feature opcional. Cada sugerencia se persiste con: input, versión del modelo, prompt, razón, revisor humano y timestamp. `AITutor-EvalKit` corre periódicamente y su salida es el anexo de calidad pedagógica del expediente. El modelo local elimina la transferencia internacional de datos.

**Entregable real:** el expediente de conformidad, no el tutor. Es lo que se factura y lo que el cliente no puede hacer solo.

**Tiempo estimado:** 10–12 semanas. **Ventana comercial:** 14 meses hasta 2027-12-02. Reutilizable para el PL 2.338 de Brasil por el acuerdo Brasil–UE de junio 2026.

> **Corregido en el pase 4 del 2026-09-30 — la ventana decía 26 meses y son 14.** El número anterior se calculó desde una fecha que no corresponde: entre hoy (2026-09-30) y el 2027-12-02 hay **14 meses**, no 26. Con un proyecto de 10–12 semanas eso sigue siendo holgado, pero no es lo que el número sugería.

### Variante de plazos — vender el Artículo 50 antes que el Annex III (agregado en el pase 4)

El **Digital Omnibus on AI** (en vigor 2026-07-27) corrió el Annex III a 2027-12-02, y el titular que le llegó al cliente es "el AI Act se pospuso". **Dos obligaciones no se movieron, y una vence en dos meses:**

| Obligación | Fecha | ¿Se movió con el Omnibus? |
|---|---|---|
| **Artículo 50** — transparencia / divulgar que hay AI | **en vigor desde 2026-08-02** | **No** |
| **Watermarking** de contenido generado | **2026-12-02** | **No** |
| Annex III alto riesgo (evaluación, adaptativo, proctoring, deserción) | 2027-12-02 | Sí, +16 meses |
| Annex I (AI embebida en producto regulado) | 2028-08-02 | Sí |

**Cómo se vende, y el orden importa.** Un cliente europeo con un tutor en producción hoy tiene una obligación **activa** de transparencia y una fecha de diciembre encima, mientras cree que tiene hasta 2027. La entrada es un proyecto chico — **divulgación en la UI, etiquetado de contenido generado, watermarking, y el registro de qué modelo produjo qué** — de 3 a 4 semanas, con urgencia verificable.

**Y no es trabajo desechable:** el registro de procedencia que exige el Artículo 50 (input, modelo, versión, timestamp por cada salida generada) **es el mismo log que el expediente del Annex III va a pedir completo en 2027-12-02**. Se entrega valor en un mes y queda instalada la mitad del proyecto grande. Ése es el argumento, no el miedo a la multa.

---

### Variante Corea del Sur — el mismo expediente, pero exigible ya (agregado en el pase 3)

La **AI Basic Act coreana está en vigor desde el 2026-01-22** y lista la **educación como "high-impact AI"**. Sus tres obligaciones cabeza mapean casi uno a uno contra lo que este patrón ya construye:

| Obligación coreana | Pieza de este patrón que la cumple |
|--------------------|-----------------------------------|
| Explicación con sentido de los resultados a los afectados | El log de decisiones pedagógicas de `tutor-mcp` (razón + timestamp + modelo), expuesto al alumno y al docente |
| Plan de protección del usuario | El archivo de policy del P7 más el expediente de conformidad de este patrón |
| Mecanismo de intervención y supervisión humana | El gate de confirmación explícita antes de cualquier escritura de nota, disciplina o placement |

**Consecuencia operativa:** el expediente que este patrón produce para EU AI Act **se adapta a Corea, no se rediseña**. Y como Corea exige ahora lo que Europa exige en 2027-12-02, conviene invertir el orden: **producir la primera referencia auditada en Corea y portarla a EMEA**, en vez de esperar el deadline europeo. Hay un año de gracia sobre las multas administrativas (hasta ~2027-01-22), pero las obligaciones sustantivas ya aplican.

---

## P5 — Orquestación multi-jurisdicción (APAC, grupos regionales)

**Problema.** Un grupo educativo que opera en China + Japón + India + Singapur enfrenta cuatro regímenes incompatibles. Una política hardcodeada por país no escala.

- **Orquestación:** LangGraph (MIT) con **nodos de política por jurisdicción**
- **Tutoría:** DeepTutor (Apache-2.0) o OpenMAIC (MIT) como ejecutor
- **Estado:** `tutor-mcp` (MIT), particionado por jurisdicción
- **Modelo:** provider intercambiable por región (Ollama on-premise donde la residencia de datos lo exige)

**Wiring.** El grafo resuelve la jurisdicción del alumno **antes** de cualquier llamada al modelo. Cada nodo de política decide: qué provider se puede usar, si se permite decisión automática, qué se puede loguear y dónde se almacena. El ejecutor de tutoría es el mismo en todas las regiones — **la política es datos, no código**, así que agregar un país es una entrada de configuración y un test, no un fork. Almacenamiento particionado por jurisdicción desde el día uno; retrofitearlo después es una migración dolorosa.

**Tiempo estimado:** 12–14 semanas.

---

## P6 — AI literacy a escala de sistema educativo (LATAM, programa de ministerio)

**Problema.** 13 de los 19 países de LAC no enseñan adopción temprana de AI en escuelas, con cuello de botella declarado en formación avanzada. No es un problema de producto: es un programa nacional. Comprador: ministerio. Financiador habitual: BID.

- **Material técnico:** [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) (Apache-2.0, 105.8k ★) y [minimind](https://github.com/jingyaogong/minimind) (Apache-2.0, 63k ★ — LLM de 64M entrenado en ~2h en hardware de consumo)
- **Generación de currículo localizado:** [Educhain](https://github.com/satvik314/educhain) (MIT, 389 ★) — MCQs, lesson plans con 8 enfoques pedagógicos, flashcards, desde PDF/YouTube/URL
- **Entrega:** Kolibri (MIT) para escuelas con conectividad intermitente, Chamilo (GPL-3.0) para las que tienen red — el más liviano de self-hostear, y con adopción real en LATAM
- **Modelo:** Latam-GPT para español/portugués con contexto cultural regional
- **Marco de referencia:** borrador de AI Literacy Framework de la Comisión Europea + OCDE (aval del G7) — alinearse a un estándar existente en lugar de inventar uno

**Wiring.** `minimind` da el laboratorio ("entrená tu propio modelo en dos horas") que convierte AI de abstracción en ejercicio. `Educhain` + Latam-GPT generan las variantes localizadas de currículo y evaluación por país e idioma — es el paso que hace viable cubrir 13 países sin escribir 13 currículos. Kolibri/Chamilo entregan y trackean. La formación docente es un track paralelo y **es el que decide si el programa funciona**: sin docentes formados, la plataforma queda sin uso.

**Tiempo estimado:** 14–16 semanas para el primer país (currículo + formación + plataforma), 4–6 semanas por país adicional usando el pipeline de localización.

**Por qué es defendible:** Latam-GPT es gratuito, regional y entrenado en contexto propio. Ningún competidor global puede ofrecer soberanía de modelo en español/portugués rápido. Y no hay incumbente open source educativo en LATAM (gap #2).

### Variante APAC — India, currículo obligatorio desde Class 3, ciclo 2026-27

*Agregada en la segunda pasada del 2026-09-30.* El mismo patrón, con el deadline más grande y más cercano de la KB: **India hizo AI y pensamiento computacional obligatorios desde 3.º grado a partir del ciclo 2026-27**, y es —con China— uno de los dos únicos países del mundo con currículo nacional de AI obligatorio.

Tres cambios respecto de la versión LATAM:

1. **El material sube de nivel.** Para docentes y secundaria, [ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) (MIT, 62.1k ★) aporta las 20 fases ya secuenciadas; `minimind` sigue siendo el laboratorio de primaria/secundaria baja. ⚠️ **No usar `tiny-llm` acá**: es Apache-2.0 y excelente, pero corre sobre MLX (macOS ARM64) y ningún sistema escolar indio va a tener hardware Apple.
2. **El stack de entrega es nativo.** `Educhain` es MIT y **de India** (Build Fast with AI) para generación multilingüe, sobre [Frappe LMS](https://github.com/frappe/lms) (AGPL-3.0) u [OpenEduCat](https://github.com/openeducat/openeducat_erp) (LGPL-3.0) — los dos de stack indio, con el agente afuera por las razones de licencia de siempre.
3. **El multiplicador es el idioma, no el país.** En LATAM se localiza a 13 países en dos idiomas; en India a un país en decenas de idiomas. El pipeline de localización de `Educhain` es la pieza crítica y hay que dimensionarla desde el día uno, no al final.

**Tiempo estimado:** 16–20 semanas para el primer estado indio (el volumen de localización manda), 4–6 semanas por estado adicional. **Comprador:** gobierno estatal o grupo educativo de escala, no una escuela.

---

## P7 — Policy pack de cumplimiento distrital (North America; Ohio y Virginia ya vencieron, Oklahoma vence 2027-28)

*Agregado en la segunda pasada del 2026-09-30. Ataca la tendencia 8 de `intel/trends.md`.*

**Problema.** Oklahoma S.B. 1734 obliga a **cada distrito** a tener política de AI **escrita** antes del ciclo escolar **2027-28**, prohíbe que la AI sea base primaria de calificación, disciplina o placement, y exige uso human-in-the-loop dirigido por el docente. Maryland S.B. 720 exige además un **AI coordinator** por distrito. Y **sólo 18% de los docentes de EE. UU. tiene hoy alguna política escrita**. El distrito no necesita un tutor: necesita demostrar cumplimiento, y no tiene cómo.

Lo que hace este patrón distinto de una consultoría de políticas: la ley restringe **arquitectura**, no redacción. Un documento que dice "hay supervisión humana" sin el gate técnico que la fuerza no es cumplimiento, es una declaración. Esto entrega las dos mitades.

- **Host / sistema de registro:** [Moodle](https://github.com/moodle/moodle) (GPL-3.0) vía plugin del **AI subsystem** — no tocar el core. Si el distrito usa Canvas, [Canvas LMS](https://github.com/instructure/canvas-lms) (AGPL-3.0) por **LTI 1.3**, nunca fork
- **Gate de decisiones auditables:** [tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT, Go) — estado durable del aprendiz y **decisiones pedagógicas auditables con razón y timestamp**. Es la pieza que convierte "hay human-in-the-loop" en un registro consultable
- **Gate de escritura en grading:** [gradescope-mcp](https://github.com/Yuanpeng-Li/gradescope-mcp) (MIT) — 34 tools sobre Gradescope con **escrituras detrás de confirmación explícita**. Ver el gap 6: el grading open source no existe, así que se orquesta el incumbente
- **Evidencia de calidad pedagógica:** [AITutor-EvalKit](https://github.com/kaushal0494/AITutor-EvalKit) (MIT) — 4 dimensiones sobre MRBench, corriendo en CI
- **Formación docente (lo que Maryland paga):** [ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) (MIT, 62.1k ★, 523 lecciones en 20 fases) como cantera de currículum, recortado a un track docente corto
- **Currículo AI para créditos de CS (GA, MS):** [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) (Apache-2.0) y [minimind](https://github.com/jingyaogong/minimind) (Apache-2.0)

**Wiring.** La política escrita se compila a **configuración, no a PDF**: un archivo de policy por estado (qué decisiones no puede tomar la AI, qué requiere confirmación docente, qué se retiene y por cuánto) que el plugin del AI subsystem lee en cada invocación. Toda llamada del alumno o del docente pasa por `tutor-mcp`, que registra decisión, razón, modelo y timestamp. Ninguna escritura sobre nota, disciplina o placement sale sin confirmación humana explícita: `gradescope-mcp` ya está diseñado así, y en Moodle el placement queda detrás del mismo gate. `AITutor-EvalKit` corre en CI y su salida es un anexo del expediente. El entregable final son cuatro piezas: **política escrita + configuración que la fuerza + registro de auditoría + evidencia de evaluación**.

**Actualizado en el pase 3 del 2026-09-30 — el primer deadline ya venció, así que el patrón cambia de tiempo verbal.** Este patrón se escribió contra un plazo futuro (Oklahoma, ciclo 2027-28). Resulta que **ya venció uno y hay dinero asignado en otro**:

- **Ohio** fue el primer estado en obligar a *todos* sus distritos a adoptar política de AI, con plazo **2026-07-01 — hace tres meses**. El Ohio DEW publicó un modelo de política (dic-2025) que los distritos podían adoptar o reemplazar por una propia alineada.
- **Virginia** (SB 394 / HB 1186, vigentes **2026-07-01**): el VDOE desarrolla guía estatal y los school boards locales deben adoptar políticas consistentes, con acuerdos de privacidad y salvaguardas contra sesgo. Y trae el **AIS Innovation in Education Pilot Program con USD 2 millones en el presupuesto FY 2027–2028**, priorizando formación docente, privacidad y equidad.
- **35+ estados** ya tienen guía oficial de AI de su Department of Education (junio 2026).

**Cómo entrar ahora, que es distinto de cómo se entraba antes.** Contra un deadline futuro se vende "te ayudo a cumplir". Contra uno vencido se vende algo más fuerte: **ya adoptaron un documento, y casi con certeza no adoptaron el gate técnico que el documento declara** — a nivel nacional sólo 18% de los docentes reporta tener política escrita, y el camino de menor esfuerzo para un distrito apurado fue copiar el modelo estatal. Entonces la conversación de apertura no es un pitch, es una **auditoría de brecha**: tomar la política que el distrito ya adoptó, y mostrar cuáles de sus cláusulas no están forzadas por ninguna configuración. Cada cláusula sin gate es una línea de alcance.

Ohio es además el **mercado de referencia** de este patrón: es el único estado donde se puede preguntar qué pasó después del deadline, y el pilot program de Virginia es una de las pocas partidas de dinero público con monto que la KB tiene identificada.

**Por qué escala.** El mismo pack se reimplanta distrito por distrito cambiando un archivo de policy por estado. California AB 1159 (prohíbe entrenar modelos con datos de alumnos) se expresa como una bandera de retención; Oklahoma y Maryland como gates de decisión; Idaho S.B. 1227 agrega los requisitos de AI literacy y formación, que ya están cubiertos por el track docente. Es el trabajo más replicable de la KB, con un mandato legal con fecha detrás.

**Tiempo estimado:** 6–8 semanas el primer distrito; 2–3 semanas cada distrito siguiente del mismo estado. **Licencias:** el agente y los gates son MIT; Moodle queda intacto detrás de su punto de extensión.

---

## P8 — Fábrica de lecciones en la voz del docente (teacher-facing, el ángulo menos disputado)

*Agregado en la tercera pasada del 2026-09-30. Ataca el gap 8 de `intel/trends.md`.*

**Problema.** Todo el mercado construye tutores para *alumnos*. El comprador que menos resistencia opone es el **docente**, porque el dolor es medible: quien usa AI semanalmente ahorra **5,9 horas por semana** (Gallup). Pero la capa teacher-facing es propietaria entera — MagicSchool, Brisk, Diffit, Curipod, Eduaide.AI, SchoolAI — y un distrito que quiere esas capacidades sin SaaS por alumno no tiene de dónde partir. Y el rechazo docente no es a la AI: es a que genere material que no suena a ellos.

- **Motor:** [Claw-ED](https://github.com/SirhanMacx/Claw-ED) (MIT, 59 ★, Python) — se apunta a una carpeta de lecciones viejas del docente, **infiere su estilo**, y emite el bundle completo: DOCX de docente, DOCX de alumno y PPTX de slides, más versiones diferenciadas, juegos y evaluaciones. 48+ tools, alineación a estándares estatales, cualquier provider LLM. Interfaz CLI + bot de Telegram con la misma memoria
- **Pedagogía como guía:** [education-agent-skills](https://github.com/GarethManning/education-agent-skills) (CC BY-SA 4.0 ⚠️) — 165 skills evidence-grounded en 20 dominios
- **Destino del material:** [Moodle](https://github.com/moodle/moodle) (GPL-3.0) vía plugin del AI subsystem, materializando salida como actividades [H5P](https://github.com/h5p/h5p-php-library) cuando conviene que viva en el curso
- **Evaluación y corrección:** [gradescope-mcp](https://github.com/Yuanpeng-Li/gradescope-mcp) (MIT) si el cliente ya usa Gradescope; si no, ver el gap 9 y **no prometer grading automático**
- **Gate de política:** [tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT, Go) para registrar qué se generó, con qué modelo y quién lo aprobó

**Wiring.** Claw-ED corre **local-first**, que es la mitad del argumento: el material histórico del docente —su propiedad intelectual— no sale de la máquina ni de la red de la escuela. Se lo apunta a un corpus de lecciones por docente (o por departamento, si se quiere una voz institucional). Las skills de `education-agent-skills` se cargan como guía pedagógica para que el bundle no sea sólo estilísticamente fiel sino didácticamente defendible. La salida va a un directorio de revisión: **nada se publica al alumno sin aprobación explícita del docente**, y esa aprobación se registra vía `tutor-mcp` con timestamp y autor. Recién aprobado, un plugin del AI subsystem de Moodle sube el material al curso (H5P para lo interactivo, DOCX/PPTX como recurso). El bot de Telegram es el canal de baja fricción: el docente pide algo desde el celular y recibe los archivos en el chat.

**Por qué este patrón se vende distinto.** No hay que convencer a nadie de que un agente enseñe. El agente **no toca al alumno**: produce borradores para un docente que decide. Eso lo saca del alcance de las restricciones de alto impacto de Oklahoma, Maryland, del Annex III europeo y de la AI Basic Act coreana, porque no hay decisión automatizada sobre el estudiante. Es el patrón con **menos superficie regulatoria y el ROI más fácil de medir** (horas docentes) de toda la KB — el lugar natural para un primer piloto que después habilita los patrones de tutoría.

⚠️ **Riesgos a declarar.** Claw-ED tiene **59 ★ y es de un solo autor**: verificar continuidad antes de comprometerlo en un contrato largo, y prever el costo de mantenerlo forkeado. `education-agent-skills` es **CC BY-SA 4.0** (share-alike): usable como guía, revisar con legal antes de empaquetar derivados en un entregable cerrado.

**Tiempo estimado:** 3–5 semanas — el más corto de la KB, porque no hay plataforma que desplegar. **Licencias:** Claw-ED MIT; la advertencia está en las skills, no en el motor.

---

## P9 — Agente adentro del SIS, sin fricción de licencia (lado administrativo)

*Agregado en la tercera pasada del 2026-09-30. Es el patrón que el gap 7 declaraba imposible hasta hoy.*

**Problema.** Los datos que más valen para un agente —matrícula, asistencia, legajos, comunicación con familias— viven en el SIS, y hasta esta pasada la KB sostenía que el agente **siempre** tenía que quedar afuera, porque todo SIS open source era copyleft. Con [GegoK12](https://github.com/Gego-K12/gegok12) (**MIT**, 54 ★, 97 forks, último commit 2026-09-23, PHP 8.4 + Laravel 12, **con sistema de plugins**) eso dejó de ser cierto.

- **Base:** GegoK12 (MIT) — core de 26 módulos: alumnos, admisiones, asistencia, tareas, biblioteca, staff, avisos, comunicación con padres. API-first, instalador visual o Docker
- **Punto de extensión:** su propio sistema de plugins — referencia: [`Plugin-Hello-Teacher`](https://github.com/Gego-K12/Plugin-Hello-Teacher)
- **Gate de decisiones auditables:** [tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT, Go) — decisiones con razón y timestamp
- **Capa de conformidad:** el mismo archivo de policy por jurisdicción del **P7**
- **Si el alcance incluye tutoría:** [DeepTutor](https://github.com/HKUDS/DeepTutor) (Apache-2.0) contra el estado del alumno que el SIS ya tiene

**Wiring.** El agente se empaqueta como **plugin de GegoK12**, corriendo en el mismo proceso Laravel y leyendo el modelo de datos directo, sin capa de sincronización, sin ETL y sin un segundo sistema de identidad. Eso es lo que la arquitectura de sidecar obligaba a construir y mantener. Como el core es MIT, **el plugin puede ser propietario del cliente sin contaminar nada** — MIT no impone share-alike. Los casos de uso de arranque son los administrativos aburridos y de ROI inmediato: triage de admisiones, seguimiento de ausentismo con alerta temprana, borradores de comunicación a familias en su idioma. Toda escritura sobre un registro de alumno pasa por `tutor-mcp` y queda auditada; las decisiones de alto impacto quedan detrás de confirmación humana, igual que en P7.

**Cuándo NO usar este patrón — leer antes de proponerlo.** Tres condiciones lo descartan:

1. **El cliente ya tiene un SIS.** Nadie migra de SIS por poder meter un agente adentro: el SIS es el sistema de registro de la institución y la migración es un proyecto en sí mismo. Esto sirve para **implementaciones nuevas** o instituciones que ya iban a cambiar.
2. **El alcance necesita exámenes o cobranzas.** Son **módulos Pro pagos** (USD 100–250 cada uno). Se pueden comprar —licencia lifetime por dominio con fuente incluido— pero hay que **cotizarlo de entrada**. Descubrirlo a mitad del proyecto es el modo de falla obvio.
3. **El cliente exige madurez de proyecto.** 54 ★ y un solo vendor (GegoSoft) es riesgo de continuidad. Para una institución grande, OpenEduCat (LGPL-3.0, más adoptado) con el agente afuera sigue siendo la opción conservadora, y está bien elegirla.

**Tiempo estimado:** 5–7 semanas para el primer caso administrativo sobre una instalación nueva. **Licencias:** core MIT + plugin propietario del cliente = la combinación más limpia que la KB puede ofrecer en el lado administrativo. Contrastar con el resto de la capa SIS (RosarioSIS GPL-2.0, openSIS GPL, OpenEduCat LGPL-3.0), donde el agente va afuera.

---

## P10 — Probar que el tutor enseña, no que responde (agregado en el pase 4, transversal a todas las regiones)

**Problema.** Todos los patrones anteriores construyen un tutor. **Ninguno mide si enseña.** Es el hueco que aparece en cuanto el comprador es institucional: un rector, un ministerio o un inspector no compra "el alumno conversó con la AI", compra evidencia de aprendizaje. Y ahora hay tres compradores distintos pidiendo lo mismo por razones distintas:

- **EMEA:** el expediente del Annex III (2027-12-02) exige documentar cómo decide el sistema.
- **North America:** los estatutos de Oklahoma, Maryland e Idaho prohíben que la AI sea base primaria de decisiones de alto impacto — hay que mostrar en qué se basó.
- **LATAM:** **65% de los estudiantes teme que la AI vuelva el aprendizaje superficial** (DEC LATAM 2026, 30.000+ respuestas). Acá el comprador de la evidencia es la propia comunidad educativa.

Hasta este pase la KB no tenía con qué responder. Ahora sí, y las piezas son MIT o CC.

**Las tres preguntas son distintas y cada una tiene su repo:**

| Pregunta | Pieza | Licencia | Stars |
|----------|-------|----------|-------|
| ¿Qué sabe el alumno ahora? | **[pyKT](https://github.com/pykt-team/pykt-toolkit)** — 10+ modelos DLKT sobre 7+ datasets | MIT ✅ | 441 |
| ¿Cuándo hay que volver a preguntárselo? | **[py-fsrs](https://github.com/open-spaced-repetition/py-fsrs)** — scheduler DSR, 21 parámetros | MIT ✅ | 499 |
| ¿El agente respondió *pedagógicamente bien*? | **[MathTutorBench](https://github.com/eth-lre/mathtutorbench)** (reward models + leaderboard) y **[UnifyingAITutorEvaluation](https://github.com/kaushal0494/UnifyingAITutorEvaluation)** (8 dimensiones + MRBench) | CC BY 4.0 / CC BY-SA 4.0 ⚠️ | 42 / 32 |

**Wiring concreto.**

1. **Instrumentar el tutor existente** — el de P1, P2 o P3, da igual cuál. Cada turno emite un evento `(alumno, skill, ítem, correcto/incorrecto, timestamp)`. Sin esto no hay nada que medir, y es el 80% del trabajo real.
2. **`pyKT` como servicio de estado, offline primero.** Entrenar un modelo DLKT (empezar por `simpleKT` o `AKT`, que son las baselines fuertes del propio toolkit) sobre el histórico del cliente. Exponerlo como un servicio con un endpoint `mastery(alumno, skill) → probabilidad`. **Correrlo en batch antes que en línea:** la primera versión no necesita estar en el loop del agente, necesita producir la curva de mastery del cohort.
3. **El agente consulta antes de decidir qué preguntar.** Acá está el hueco que el gap 5 declara abierto: **no existe `pyKT` detrás de MCP**, así que esta pieza se construye. Es un servidor MCP fino con una tool `get_mastery` y una tool `record_attempt`, siguiendo el diseño de `tutor-mcp` (MIT, 42 ★, Go) pero con un modelo DLKT entrenable atrás en vez de su BKT propio. **Es la pieza de IP del patrón** — chica, y la única que no está hecha.
4. **`py-fsrs` programa el repaso** con la probabilidad de mastery de `pyKT` como señal de dificultad inicial, en vez del default.
5. **El benchmark corre en CI, no una vez.** Los diálogos del tutor se puntúan contra las 8 dimensiones de MRBench (y contra MathTutorBench si el dominio es matemática) **en cada cambio de prompt o de modelo**. Un cambio de prompt que sube la satisfacción y baja la calidad pedagógica es exactamente el fallo que este paso atrapa, y es invisible sin él.
6. **La salida es un reporte, y es el entregable.** Curva de mastery por skill y por cohorte, retención a 30/60/90 días, y puntaje pedagógico por dimensión con su evolución. Eso es lo que se le muestra al rector, al ministerio y al inspector.

**Lo que hay que construir vs. lo que se toma hecho.** Se toman hechos `pyKT`, `py-fsrs` y los dos benchmarks. Se construye el servidor MCP del paso 3 y el reporte del paso 6. **Esa proporción es el argumento comercial:** el cliente paga integración y evidencia, no investigación.

⚠️ **La trampa de licencia, y es la que muerde en este patrón justamente.** `pyKT` y `py-fsrs` son MIT, sin problema. Pero **MRBench es CC BY-SA 4.0**, y el uso natural acá es *derivar un benchmark propio con los diálogos del cliente* — que es exactamente lo que dispara el share-alike. **MathTutorBench es CC BY 4.0** (sólo atribución) y no tiene ese problema. Decidirlo antes de empezar: o el benchmark derivado se publica bajo la misma licencia, o se construye sobre MathTutorBench, o se escribe una taxonomía propia inspirada en las 8 dimensiones sin reusar el dataset. Las tres son defendibles; descubrirlo al final no.

**Tiempo estimado:** 6–8 semanas sobre un tutor ya desplegado (la instrumentación del paso 1 domina). **Dónde venderlo primero:** EMEA como anexo de calidad del expediente de P4; LATAM como respuesta directa al 65%; North America como la evidencia que los estatutos de decisiones de alto impacto obligan a tener.

**Por qué es el patrón con menos competencia de esta KB:** los benchmarks están premiados en EMNLP 2025 y NAACL 2025 y tienen 42 y 32 estrellas. **La academia los produjo y la industria no los adoptó.** Operacionalizar lo que ya está publicado y validado es un trabajo mucho más barato y más defendible que construir un evaluador propio, y hoy no lo está haciendo casi nadie.

---

## P11 — Gate de seguridad pedagógica (agregado en el pase 5; transversal, se vende primero en EMEA y North America)

**Problema.** P10 mide si el tutor *enseña bien*. Este mide si **enseña mal siendo amable**, que es un modo de falla distinto y el que un docente reconoce al instante: el tutor revela la respuesta antes de tiempo, le da la razón al alumno que insiste con una idea equivocada, o abandona el andamiaje cuando el alumno se frustra. Un tutor con 95% de exactitud puede fallar en todas esas y **los benchmarks de exactitud no lo ven**.

**El dato que justifica la arquitectura, y es lo que lo hace vendible.** Según ELBench (9 modelos), el módulo de *safety* está **anti-correlacionado con el de enseñanza práctica**: los modelos más seguros enseñan peor. Si se sostiene, **no existe el modelo que resuelva las dos cosas eligiéndolo bien** — hay que componer. Eso convierte "poné un gate de seguridad" de preferencia de arquitecto en requisito justificado por evidencia. Y de EduGuardBench (14 modelos): el modo de falla dominante es la **incompetencia**, no la toxicidad — o sea que el guardrail genérico de contenido que el cliente ya tiene **no cubre este riesgo**.

**Las piezas, todas verificadas y las dos centrales MIT:**

| Rol | Pieza | Licencia | Stars |
|-----|-------|----------|-------|
| Taxonomía de daño pedagógico + dataset de evaluación | **[SafeTutors](https://github.com/RadiantCrystal/SafeTutors)** — 11 dimensiones, 48 sub-riesgos, 5.955 instancias (3.135 single-turn + 2.820 multi-turn), matemática/física/química | MIT ✅ | 0 |
| Fidelidad pedagógica transversal a materia | **[EduBench](https://github.com/ybai-nlp/EduBench)** — 9 contextos, 4.000+ situaciones, 12 dimensiones, incluye 4 escenarios docentes | MIT ✅ | 29 |
| Seguridad adversaria del modelo como docente | **[EduGuardBench](https://github.com/YL1N/EduGuardBench)** — SATA + prompts adversarios de mala conducta académica | ⚠️ sin licencia | 4 |
| Motor de scoring por rúbrica ponderada | **[rubric](https://github.com/paper-instruments/rubric)** — criterio por criterio, single-pass u holístico, Pydantic | MIT ✅ | 75 |

**Wiring concreto.**

1. **Mapear las 11 dimensiones de daño de SafeTutors al contexto del cliente.** No se usan las 11 en producción: se eligen las que aplican al nivel y la materia, y se escribe para cada una qué cuenta como falla *en este despliegue*. Es una hora de trabajo con el equipo pedagógico del cliente y es el paso que hace que el resto signifique algo.
2. **Cargar el dataset como suite de regresión.** Los 3.135 escenarios single-turn corren rápido; los 2.820 multi-turn son los que atrapan el abandono de andamiaje, que por definición no aparece en un solo turno. Correr los dos.
3. **Scoring con `rubric` (MIT)** y no con un prompt de juicio ad hoc: rúbricas ponderadas explícitas, salida validada con Pydantic, reproducible. Que el criterio esté versionado en el repo es lo que lo vuelve auditable.
4. **`EduBench` para lo que SafeTutors no cubre** — es transversal a materia y trae los cuatro escenarios docentes, así que cubre el caso teacher-facing (P8) que SafeTutors no mira.
5. **El gate en el pipeline, con umbral que bloquea.** Corre en CI en cada cambio de prompt, de modelo o de temperatura. **Un cambio que sube la satisfacción del alumno y baja el puntaje de sycophancy es el fallo exacto que este gate atrapa** — y es el más probable, porque optimizar satisfacción es optimizar adulación.
6. **En runtime, el gate va aparte del modelo docente.** Por la anti-correlación: el modelo que enseña bien no es el que hay que usar para juzgar si se pasó de amable. Modelo docente + evaluador separado, y el evaluador puede ser más chico y más barato.
7. **La salida es el anexo de riesgos.** Puntaje por dimensión de daño, evolución entre releases, y los casos que fallaron con su transcripción. **En un expediente de Annex III eso no es QA: es el análisis de riesgos.**

**Lo que se toma hecho vs. lo que se construye.** Se toman SafeTutors, EduBench y `rubric`. Se construye el mapeo del paso 1, la integración en CI del paso 5 y el reporte del paso 7. **Proporción deliberadamente parecida a P10:** el cliente paga integración y evidencia.

⚠️ **Licencias.** `SafeTutors`, `EduBench` y `rubric` son **MIT** — es la primera vez en esta KB que un patrón de evaluación no arrastra fricción de Creative Commons. **`EduGuardBench` no declara licencia**: usarlo para leer y diseñar, **no** incorporar sus datasets a un entregable. Si hace falta el ángulo adversario dentro del entregable, escribir prompts propios siguiendo su estructura.

⚠️ **Y lo que hay que verificar antes de ponerlo en una slide:** los hallazgos de anti-correlación (ELBench) y de incompetencia dominante (EduGuardBench) **no pudieron verificarse en la fuente primaria** — `arxiv.org` y `ojs.aaai.org` están bloqueados en el entorno donde se investigó. Son el argumento central del patrón: abrir los papers antes de presentarlos.

**Tiempo estimado:** 3–4 semanas sobre un tutor ya desplegado e instrumentado; 5–6 si hay que instrumentarlo. **Dónde venderlo primero:** **EMEA**, como el anexo de riesgos del expediente Annex III de P4 (llegar con la taxonomía de 11 dimensiones ya mapeada gana contra un integrador que llega con "medimos accuracy"); **North America**, como la auditoría que los estatutos de decisiones de alto impacto obligan a tener; **LATAM**, ver P13.

---

## P12 — `pyBKT` detrás de MCP: la pieza que cinco proyectos intentaron y ninguno terminó (agregado en el pase 5)

**Problema.** El gap 5 de esta KB lleva cinco pasadas diciendo que nadie cosió bien knowledge tracing con agentes LLM. El pase 5 encontró que **cinco servidores MCP independientes** exponen mastery a un agente —`knowledge-graph-mcp`, `student-progress-tracker`, `tejpalvirk/student`, `knowledge-forest-mcp`, `Teacher-MCP`— y que **ninguno usa una librería de knowledge tracing entrenable**: todos implementan su propia heurística (SM-2, fórmulas de pesos fijas, reglas de evidencia). Los tres más grandes suman **3 estrellas y 23 commits**.

**Por qué eso es una oportunidad y no una categoría saturada.** Cinco autores sin relación llegaron al mismo patrón en la misma ventana: el problema está validado sin que haya que evangelizarlo. Y el trabajo dejó de ser inventar el patrón — pasó a ser **hacerlo bien una vez**, con una librería publicada atrás en vez de una heurística.

**La pieza central, y es la novedad del pase 5:**

| Rol | Pieza | Licencia | Stars | Nota |
|-----|-------|----------|-------|------|
| Modelo de mastery **interpretable** | **[pyBKT](https://github.com/CAHLR/pyBKT)** — BKT y variantes, parámetros por alumno y por ítem. EDM 2021, CAHLR/UC Berkeley | MIT ✅ | **281** | **Procedencia estadounidense** — la respuesta al gap 4 |
| Modelo de mastery **potente** | **[pyKT](https://github.com/pykt-team/pykt-toolkit)** — 10+ modelos DLKT sobre PyTorch | MIT ✅ | 441 | APAC (Jinan University) |
| Scheduling de repaso | **[py-fsrs](https://github.com/open-spaced-repetition/py-fsrs)** | MIT ✅ | 499 | — |
| Referencia de diseño MCP | **[tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp)** — BKT propio detrás de MCP, en Go | MIT ✅ | 42 | Copiar la forma de las tools, no el modelo |

**Wiring concreto.**

1. **Elegir el modelo según el cliente, y decirlo explícito.** **`pyBKT` si hay regulador o licitación**: BKT bayesiano es menos potente que DLKT y **mucho más fácil de defender** cuando preguntan por qué el sistema decidió lo que decidió — los parámetros tienen significado (prior, learn, guess, slip) y se pueden mostrar en una tabla. **`pyKT` si el cliente tiene volumen de datos y quiere el techo más alto.** Para un primer engagement regulado, pyBKT.
2. **Entrenar offline sobre el histórico del cliente.** pyBKT necesita secuencias `(alumno, skill, correcto/incorrecto)`; casi cualquier LMS las tiene en la tabla de intentos. Empezar con el modelo base, después las variantes que individualizan por alumno o por ítem.
3. **Servidor MCP fino, y es la IP del patrón.** Dos tools y nada más al principio: `get_mastery(alumno, skill) → probabilidad` y `record_attempt(alumno, skill, resultado)`. Seguir la forma de `tutor-mcp` (que ya resolvió el diseño de las tools) con **pyBKT atrás en vez de un BKT propio**. FastMCP en Python es el camino corto porque pyBKT es Python.
4. **El agente consulta antes de decidir qué preguntar, no después.** Esto es todo el punto: el tutor deja de elegir el próximo ítem por heurística de prompt y lo elige por probabilidad de mastery. Es la diferencia entre un chatbot con memoria y un sistema adaptativo.
5. **`py-fsrs` toma la probabilidad de pyBKT como dificultad inicial** en vez del default, y programa el repaso.
6. **Cerrar el loop con P11 o P10.** El mastery es la métrica de resultado; el gate pedagógico es la métrica de proceso. Juntas son el reporte que compra una institución.

**Lo que se construye:** el servidor MCP del paso 3, y es chico — dos tools sobre una librería que ya funciona. **Lo que se toma hecho:** el modelo (pyBKT/pyKT), el scheduler (py-fsrs) y el diseño de las tools (tutor-mcp). **Eso es el argumento de estimación: semanas, no trimestres, y ninguna investigación.**

⚠️ **Verificado de primera mano en el pase 5:** `pyKT` sigue sin mencionar MCP ni interfaz de serving en su documentación (441 ★, 811 commits). El hueco sigue abierto — pero conviene re-verificarlo cada ciclo, porque con cinco proyectos empujando en esa dirección es el gap con más probabilidad de cerrarse solo.

**Tiempo estimado:** 4–6 semanas (paso 2 y paso 3 dominan; el paso 2 depende de cuán limpia esté la tabla de intentos del cliente). **Dónde venderlo:** como el motor adaptativo de P1, y como el sustrato de evidencia de P10. **Para un cliente con restricción de procedencia de software, `pyBKT` es la única ruta** — ver gap 4.

---

## P13 — Cerrar la tijera de LATAM: 73,5% enseña con AI, 9% puede medirla (agregado en el pase 5, LATAM)

**Problema, con fuente.** UNESCO IESALC encuestó **200 instituciones de educación superior en 19 países** de América Latina y el Caribe (campo agosto–octubre 2025). **73,5% implementa AI en enseñanza y aprendizaje. 9,0% tiene un mecanismo formal de evaluación. 18,5% tiene política institucional transversal. 26,0% tiene estrategia formal.**

**64 puntos entre enseñar con AI y poder medirla** — la tijera más ancha que esta KB documentó en cualquier región.

**Por qué este patrón y no "construyamos un tutor LATAM".** El gap 2 dice que LATAM no produce tutores con tracción, y la conclusión tentadora es construir uno. Es la peor opción: competir contra DeepTutor (40.6k ★) y OpenMAIC (39.7k ★) con un producto nuevo. **Cerrar el gap de medición, en cambio, es integrar cuatro librerías MIT que ya existen** — y el comprador ya declaró que le falta.

**Las piezas:** `EduBench` (MIT, transversal a materia — importa porque las instituciones LATAM no son sólo STEM), `SafeTutors` (MIT, 11 dimensiones de daño), `pyBKT` (MIT, mastery interpretable **y de procedencia no-china**, que en licitación pública de la región importa), `rubric` (MIT, scoring). Todo el stack es MIT: **no hay conversación de legal que frene el proyecto.**

**Wiring concreto.**

1. **Entrar por el presupuesto que ya existe.** ⚠️ **Sólo 8,0% de las instituciones tiene presupuesto asignado a AI.** Este proyecto **no se vende como línea nueva de gasto y va a fracasar si se intenta.** Se vende contra **acreditación, aseguramiento de la calidad, cumplimiento o reporte a ministerio** — rubros donde "mecanismo formal de evaluación" ya tiene partida y ya tiene un dueño con incentivo.
2. **Empezar por el inventario, no por el software.** Qué herramientas AI se están usando ya en la institución, en qué cursos, con qué autorización. En una institución del 73,5% que no está en el 18,5% con política, **nadie tiene esa lista** — y producirla es un entregable valioso en sí mismo, cobrable, y de dos semanas.
3. **Instrumentar un piloto, no la institución entera.** Dos o tres cursos con volumen de intentos en el LMS (Moodle o Chamilo, que son los que dominan la región). Emitir eventos `(alumno, skill, ítem, resultado)`.
4. **`pyBKT` sobre el histórico de esos cursos** → curva de mastery por cohorte. Primera evidencia cuantitativa que la institución tiene de que la AI ayuda o no.
5. **`EduBench` + `SafeTutors` sobre el tutor en uso** — incluso si es una herramienta de tercero. Medir lo que ya se usa, en vez de proponer reemplazarlo, es lo que hace que el proyecto entre sin pelear contra nadie internamente.
6. **El entregable es el mecanismo, no el reporte.** Política institucional (cubre el 18,5%), proceso de evaluación con umbrales (cubre el 9,0%), y el reporte periódico que el proceso produce. Es exactamente lo que la encuesta dice que falta, dicho en el vocabulario de la encuesta.

**A quién golpear primero, con dato:** adopción por tipo de institución — **privadas sin fines de lucro 84%, públicas 68%, privadas con fines de lucro 52%**. Las privadas sin fines de lucro son el segmento más maduro y el de ciclo de compra más corto: empezar ahí y usar el caso para entrar al sector público, que es el volumen y el ciclo largo.

**El argumento de cierre con la comunidad educativa:** la KB ya documentó que **65% de los estudiantes LATAM teme que la AI vuelva superficial el aprendizaje** (DEC, 30.000+ respuestas). Este patrón es la única respuesta que no es retórica: medición publicada. Sirve igual para el consejo académico que para el gremio docente.

**Tiempo estimado:** 6–8 semanas para el piloto completo (pasos 2–6), de los cuales el inventario del paso 2 es facturable por separado y sirve de puerta de entrada. **Composición:** es P11 + P12 empaquetados en el lenguaje institucional de la región, no patrones nuevos.

---

## P14 — Calificar sin que califique el modelo (agregado en el pase 5; North America primero, aplica donde haya prohibición de grading automático)

**Problema.** Los estatutos de EE. UU. que esta KB documenta (Ohio, Virginia, Oklahoma, Maryland, Idaho) y el Annex III del EU AI Act **no prohíben la AI en evaluación: prohíben que la decisión de calificación sea automática.** Es una distinción implementable, y casi nadie la está vendiendo bien — se vende "AI para corregir" y se choca con el regulador, o no se vende nada.

**Y el gap 6 de esta KB explica por qué hay poco con qué construir:** el grading agéntico open source más maduro que existe, `llmgrader` (NYU, 240 commits, en producción en un curso de maestría, con MCP e integración a Gradescope), tiene **licencia de investigación custom — "PySilicon Research License", no OSI — y no se puede usar en un entregable.** El gap no era que nadie lo construyera; era que quien lo construyó bien no lo liberó.

**La arquitectura que cumple sin perder el beneficio: la nota la pone un componente determinista y el LLM sólo explica.**

| Rol | Pieza | Licencia | Nota |
|-----|-------|----------|------|
| **La nota** (código) | **[Autograder.io](https://github.com/eecs-autograder/autograder.io)** — casos de test, sandbox Docker | ⚠️ verificar por componente | U. de Michigan, **~5.000 alumnos/semestre**. El único dato de escala de producción de toda esta capa |
| **La nota** (no-código) | **[rubric](https://github.com/paper-instruments/rubric)** — rúbricas ponderadas, salida validada | MIT ✅ | 75 ★ |
| El incumbente que no se va a cambiar | **[gradescope-mcp](https://github.com/Yuanpeng-Li/gradescope-mcp)** — 34 tools, escrituras tras confirmación | MIT ✅ | 8 ★ |
| Artefacto de corrección auditable | **[AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent)** — Lab/Exam/Grading como DSL validado, review humano obligatorio | MIT ✅ | 0 ★ — seguir, no usar |
| Que el gate no sea adulador | **P11** (`SafeTutors`, `EduBench`) | MIT ✅ | — |

**Wiring concreto.**

1. **Separar explícitamente dos decisiones que el cliente tiene mezcladas:** *cuánto vale esta respuesta* (determinista, auditable, apelable) y *por qué* (generado, útil, no vinculante). Escribirlo en el diseño antes de tocar código, porque es lo que se le muestra al abogado del distrito.
2. **La nota sale de un test o de una rúbrica, nunca de un modelo.** Código → Autograder.io u otro runner de tests. Respuesta abierta → `rubric` con criterios ponderados versionados en el repo. **Lo determinista no es sólo cumplimiento: es reproducible y sobrevive una apelación de nota**, que es el riesgo operativo real de un distrito.
3. **El LLM explica el resultado que ya existe.** Recibe la respuesta del alumno, el resultado de los tests o del criterio, y produce feedback formativo: qué concepto falta, qué caso falló y por qué. **Nunca recibe la pregunta "¿qué nota merece?".** Esa separación en el prompt es el control técnico que se audita.
4. **Revisión humana en el medio, con el artefacto correcto.** El diseño de `AI-Teaching-Agent` es el modelo a copiar: DSL validado, review obligatorio, previews de examen sin respuestas ni referencias de corrección. Con 0 ★ **no se usa como dependencia** — se copia el diseño.
5. **Si el cliente ya tiene Gradescope, orquestarlo y no reemplazarlo** (`gradescope-mcp`, MIT). Sigue siendo la recomendación del gap 6 y esta pasada no encontró nada que la cambie.
6. **Medir el explicador con P11.** Un feedback formativo que revela la respuesta completa o que le da la razón al alumno para no desmotivarlo **es exactamente la falla que SafeTutors mide**. Sin este paso, el paso 3 introduce el riesgo que el paso 1 quiso evitar.
7. **El entregable de cumplimiento:** diagrama de flujo de decisión mostrando que la nota nunca pasa por el modelo, el registro de revisión humana, y los criterios versionados con su historial. Eso responde el estatuto.

⚠️ **Lo que no hay que hacer, y es la tentación:** usar `llmgrader` porque es el más maduro. Su licencia no lo permite. Sirve como **referencia de diseño** —sus rúbricas en XML y sus trazas de corrección son buenas ideas— y nada más.

⚠️ **`eecs-autograder/autograder.io` es el repo de documentación e issues y no declara licencia**; el código vive en otros repos de la organización. Verificar la licencia del componente concreto antes de cotizar.

**Tiempo estimado:** 5–7 semanas para código (Autograder.io hace el trabajo pesado); 8–10 para respuesta abierta (la rúbrica es donde se va el tiempo, y es trabajo pedagógico con el cliente, no de ingeniería). **Dónde venderlo primero:** **North America**, distritos y universidades con estatuto vigente — es el patrón que convierte una prohibición en una especificación, y llegar con la arquitectura ya resuelta gana contra quien llega a pedir una excepción.

---

## P15 — Memoria de aprendizaje conforme al estándar: el LRS como capa 0 (agregado en el pase 6; transversal, y es la base de P1, P10 y P14)

**El problema que resuelve.** Todo tutor con AI llega a la misma pregunta del director académico: *"¿esto dónde queda guardado, y cómo sé lo que el sistema decidió?"*. La respuesta habitual —"en nuestra base de datos"— no sirve ante un auditor, no se integra con el LMS ni con el SIS, y hay que rehacerla en cada engagement. Existe una respuesta estándar desde hace una década y esta KB no la tenía registrada hasta el pase 6: **xAPI / IEEE 9274.1.1**, implementado por un **Learning Record Store**.

**Por qué se propone antes que el tutor.** Es barato, es infraestructura que el cliente entiende, y convierte cada patrón posterior en auditable sin trabajo extra. Los mandatos de supervisión humana de EE. UU. (gap regulatorio de `intel/market.md`), el EU AI Act y la clasificación de Vietnam de la evaluación automatizada como alto riesgo piden todos lo mismo: **registro de qué decidió el sistema, cuándo y con qué evidencia.** Eso es literalmente lo que un LRS almacena.

### Las piezas, todas verificadas en el pase 6

| Capa | Pieza | Licencia | Por qué esta |
|---|---|---|---|
| Almacén | **`lrsql`** — https://github.com/yetanalytics/lrsql | Apache-2.0 ✅ | Corre sobre el PostgreSQL (14–18) que el cliente ya opera. No agrega infraestructura nueva al diagrama |
| Almacén (alternativa Open edX) | **`Ralph`** — https://github.com/openfun/ralph | MIT ✅ | Convierte tracking logs de Open edX a xAPI de fábrica. Mismo origen que Richie (OpenFun, Francia) |
| Puente al agente | **`learnmcp-xapi`** — https://github.com/DavidLMS/learnmcp-xapi | MIT ✅ | Tres tools MCP: registrar statement, consultar progreso, gestionar vocabulario. Ya soporta `lrsql` y Ralph |
| Estimador de mastery | **`pyBKT`** — https://github.com/CAHLR/pyBKT | MIT ✅ | **Esta es la pieza que hay que construir/integrar** — no viene hecha. BKT bayesiano, interpretable, UC Berkeley. Alternativa: `pyKT` (MIT, DLKT, más potente y menos defendible) |
| Scheduling de repaso | **`py-fsrs`** — https://github.com/open-spaced-repetition/py-fsrs | MIT ✅ | Decide *cuándo* volver sobre un concepto, una vez que el LRS sabe cómo le fue |
| Agente | El que corresponda al engagement | — | El tutor deja de tener memoria propia: escribe y lee del LRS |

**Las seis piezas son permisivas.** Es el primer patrón de esta KB que se arma completo sin una sola licencia con fricción.

### El wiring

1. **Levantar el LRS.** `lrsql` contra el Postgres existente (o `Ralph` si el cliente está sobre Open edX). Definir el perfil xAPI del proyecto: qué verbos se usan (`attempted`, `answered`, `mastered`, `asked-for-hint`) y sobre qué objetos.
2. **Instrumentar el origen de eventos.** Si hay LMS, sus eventos ya salen (Ralph los convierte desde Open edX; Moodle y Canvas salen por sus propios plugins/LTI). Si el tutor es la única superficie, lo instrumenta el paso 3.
3. **Conectar `learnmcp-xapi` al LRS** y dárselo al agente como servidor MCP. Desde acá el tutor ya **registra** cada interacción como statement y **consulta** el historial antes de responder. Esto solo ya entrega el argumento de auditabilidad — sin ningún modelo de mastery todavía.
4. **La pieza propia: el estimador.** Un servicio que lee los statements del LRS, los mapea a secuencias `(alumno, skill, correcto/incorrecto)`, entrena `pyBKT` y expone `P(mastery | skill, alumno)`. Se publica como **tool MCP adicional** junto a las tres de `learnmcp-xapi`. Es el componente que el pase 5 buscó en cinco repos y no encontró bien hecho en ninguno.
5. **Cerrar el lazo con scheduling.** `py-fsrs` toma la estimación de mastery y decide el próximo repaso. El agente pregunta al MCP qué toca antes de elegir el ejercicio.
6. **Evaluar que efectivamente enseña.** `MathTutorBench` o `EduBench` sobre las respuestas del tutor, y `SafeTutors` como gate de seguridad pedagógica (ver **P10** y **P11**). El LRS da la trazabilidad; estos dan la calidad.

### Plazo y alcance

**6–8 semanas** para los pasos 1–3 (LRS + instrumentación + MCP, auditable end-to-end). **+4–6 semanas** para los pasos 4–5 (estimador de mastery y scheduling). El corte entre ambos es limpio y conviene venderlo así: **la primera mitad entrega cumplimiento y no depende de que el modelo de mastery funcione**, lo que la vuelve mucho más fácil de aprobar.

### Dónde se vende primero

- **North America** — donde hay mandato distrital con **supervisión humana obligatoria** (Idaho, Maryland, Oklahoma, Virginia): el LRS *es* la evidencia de supervisión. Combina con **P7** y **P14**.
- **EMEA** — expediente del EU AI Act (**P4**), con el argumento extra de que `Ralph` y `learnmcp-xapi` son artefactos europeos y MIT (soberanía tecnológica, que puntúa en licitación).
- **LATAM** — es la respuesta directa a la tijera de la región: 50%+ de docentes usando AI y <10% de instituciones con lineamientos. El LRS es el instrumento más barato para pasar de "se usa" a "se puede medir y gobernar". Combina con **P13**.
- **APAC** — obligatorio donde la evaluación automatizada es alto riesgo (**Vietnam**) y bajo el AI Basic Act coreano. Combina con **P5**.

⚠️ **Lo que NO hay que prometer.** Ningún LRS estima mastery: son almacenes conformes al estándar. La inferencia es siempre desarrollo propio (paso 4). Y `learnmcp-xapi` tiene **32 commits** — sirve como referencia de integración o base a forkear (es MIT), **no como dependencia de producción sin revisarlo**. Si el cliente ya tiene un LRS, lo más probable es que sea **Learning Locker**, que es **GPL-3.0**: en ese caso el servicio propio va afuera y se habla por la API estándar, sin tocar el core.

## Nota de licencias para todos los patrones

| Licencia | Repos en estos patrones | Implicancia |
|----------|-------------------------|-------------|
| **MIT / Apache-2.0** ✅ | DeepTutor, OpenMAIC, NOMAD, OATutor, Educhain, tutor-mcp, py-fsrs, gradescope-mcp, AITutor-EvalKit, Kolibri, OpenOLAT, Richie, Oppia, XBlock, LLMs-from-scratch, minimind, **Bloom**, **ai-engineering-from-scratch**, **learn-claude-code**, **tiny-llm**, **Claw-ED**, **AI-Teaching-Agent**, y del pase 5: **pyBKT**, **EduBench**, **SafeTutors**, **rubric**, **Aila**, y los 5 servidores MCP de mastery | Sin fricción. Base de todo lo que Globant construye |
| **MIT con open-core** ⚠️ | **GegoK12** | El core (26 de 38 módulos) es MIT de verdad y admite plugin propietario. Pero **12 módulos son Pro pagos, USD 100–250 cada uno — entre ellos exámenes y fees**. La licencia no es el problema; el alcance sí. Cotizar los módulos Pro de entrada |
| **MIT reciente** ⚠️ | **OpenMAIC** | Relicenciado de **AGPL-3.0 a MIT en v0.3.0 (2026-06-28)**. Es permisivo hoy, pero la licencia tiene ~3 meses: si el cliente audita procedencia, declarar que el historial previo es AGPL |
| **BSD-3-Clause** ✅ | OpenTutorAI-CE | Permisiva. Sólo exige atribución y no usar el nombre del proyecto para endosar derivados |
| **GPL-2.0** ⚠️ | RosarioSIS, openSIS | Copyleft, **no** de red. El agente va afuera leyendo por API; no modificar el SIS |
| **GPL-3.0** ⚠️ | Moodle, Chamilo, H5P | No modificar el core. Integrar por plugin del AI subsystem |
| **AGPL-3.0** ⚠️ | Open edX, Canvas, Frappe LMS | Copyleft de red: modificar el core y servirlo por SaaS obliga a publicar el fuente. Integrar por XBlock (Apache-2.0) o LTI 1.3 |
| **CC BY-SA 4.0** ⚠️ | education-agent-skills, **UnifyingAITutorEvaluation / MRBench** | Contenido share-alike, no código. Revisar con legal antes de derivados cerrados. **Es la licencia que muerde en P10**, porque derivar un benchmark con datos del cliente dispara el share-alike |
| **Sin licencia declarada** 🚫 | **EduGuardBench**, **OmniEdu**, `awesome-ai-llm4education` | *Pase 5.* Sin LICENSE el default es todos los derechos reservados. Leer y citar sí; **empaquetar no**. En P11, EduGuardBench se usa para diseñar, no se incorpora |
| **Licencia de investigación custom** 🚫 | **llmgrader** (NYU) | *Pase 5.* "PySilicon Research License", © 2026 Sundeep Rangan, leída en el archivo. No es OSI. Es el grading agéntico más maduro que existe y **no se puede usar** — referencia de diseño en P14, nada más |

---
*Ver `intel/market.md` para la oportunidad por región y `intel/trends.md` para los gaps que estos patrones atacan.*
