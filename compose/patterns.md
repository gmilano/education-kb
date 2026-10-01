---
industry: education
region: Global
updated: 2026-10-01
---

# 🧩 Patrones de composición — Education

> Recetas concretas: repos nombrados, licencias verificadas, wiring explícito y estimación.
> Todos los repos citados fueron verificados vía WebFetch el 2026-09-30; los del pase 11, el 2026-10-01 (ver `agents/top.md`).
> **Pase 26:** +4 patrones — **P50** (el perfil de competencia por MCP, con las 6 tools de CaSS **medidas** en vez de
> inferidas), **P51** (el conector MCP de Moodle que no existe, construido sobre el patrón del que sí existe para
> Canvas), **P52** (la capa agéntica de biblioteca sobre el bus de Kafka de FOLIO, Apache-2.0) y **P53** (*early warning*
> con humano decidiendo, que es el único envoltorio facturable de la capa predictiva en las cuatro regiones).
> **Pase 25:** +2 patrones — **P48** (del acervo QTI viejo a la aserción de competencia: migración → banco de ítems →
> entrega **certificada** → evidencia xAPI filtrada → competencia en CaSS, **todo MIT/Apache-2.0**) y **P49** (integridad
> de examen **sin** AI de vigilancia, que saca el entregable del **Annex III** en vez de buscar la pieza de proctoring que
> no existe en open source permisivo).
> **Pase 11:** +2 patrones — **P25** (riesgo de abandono conforme al Anexo III, la capa con presupuesto ya asignado y sin oferta open source) y **P26** (agente docente sobre la ontología curricular nacional ya publicada).
> **Pase 27:** **+4 patrones y una corrección.** 🔴 **P51 queda con premisa falsa** —el conector MCP de Moodle **sí existe y es MIT**— y lo reemplazan **P54** (corrección y devolución sobre Moodle con **compuerta humana**, el último tramo del gap 6, con piezas que ya escriben), **P55** (el conector de **Open edX**, que es el único que de verdad no existe), **P56** (**SCORM** como formato de salida de la capa generativa: cero integración, offline) y **P57** (evidencia por MCP cotizada sobre lo que CaSS **realmente** expone — 6 de 61 operaciones, con insignias y autoría de marcos **fuera**).

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
  - 🔴 **Corregido en el pase 10:** el **código** de OATutor es MIT y no está en discusión; **el contenido sí**. OATutor declara en su README que su contenido es **CC BY 4.0**, y el archivo `LICENSE` de los bundles de OpenStax en GitHub dice **CC BY-NC-SA** — incluido **Calculus Volume 1**, que OATutor declara curar (verificado 3 de 3 bundles: Calculus, Biology, College Physics). **NonCommercial prohíbe el uso en un entregable facturado y ShareAlike obliga a abrir la derivación.** Antes de usar este contenido en un proyecto pago hay que leer **el campo de licencia de cada ítem JSON** —que es donde OATutor dice que está la licencia real— y producir el manifiesto de **P22**. Ver el **trend 22** y el **gap 17**
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

## P16 — Entrenar el estimador de mastery sin un dataset que se pueda usar (agregado en el pase 7; transversal, y es la condición de posibilidad de P1, P12 y P15)

**El problema que resuelve, y es el que P15 dejó abierto sin decirlo.** P15 termina en el paso 4 —"la pieza propia: el estimador"— y lo presenta como integración de `pyBKT`, que es MIT. Lo es. Pero un modelo de knowledge tracing **no se instala: se entrena**, y cuando se va a buscar con qué, la licencia se da vuelta (ver `repos/foundations.md`, capa de datos de entrenamiento):

| Dataset | Volumen | Licencia | ¿Sirve en un entregable facturado? |
|---|---|---|---|
| **EdNet** | 131,4M interacciones, 784k alumnos | ⚠️ **CC BY-NC 4.0** | **No** |
| **FoundationalASSIST** | 1,7M, el único en inglés con respuestas reales y distractores | ⚠️ **CC BY-NC 4.0** + gated | **No** |
| **XES3G5M** | 5,5M interacciones, 18k alumnos, 7.652 preguntas, 865 KC | **MIT** ✅ | **Sí**, y es **chino, matemática, tercer grado** |

**La consecuencia no es legal, es de arquitectura y de cronograma:** si el dataset de producción tiene que ser el del cliente, entonces **el LRS no es la fase de conformidad, es la fase que fabrica el activo**. Y el proyecto tiene un arranque en frío que hay que presupuestar en vez de descubrirlo en la semana 10.

### El wiring, en tres fases con un corte comercial limpio

**Fase A — Validar la arquitectura con `XES3G5M` (2–3 semanas).** Entrenar `pyBKT` (y opcionalmente un DLKT de `pyKT`) sobre `XES3G5M`, que es **MIT** y por lo tanto el único que se puede tocar sin pasar por legal. El entregable no es un modelo: es el **pipeline probado** —ingesta, mapeo a secuencias `(alumno, skill, correcto)`, entrenamiento, métricas de AUC/accuracy, serving detrás de MCP— y la evidencia de que funciona end-to-end.

⚠️ **El error que hay que evitar acá, y es fácil de cometer:** presentar el modelo entrenado sobre `XES3G5M` como el modelo del cliente. Es matemática de tercer grado en chino. Sirve para demostrar que el pipeline entrena y mide; **no transfiere** a la materia, el nivel ni el idioma del cliente. En la propuesta va escrito como *validación de arquitectura*, con esas palabras.

**Fase B — Arranque en frío, con el LRS produciendo el dataset (6–10 semanas, solapada con el uso real).** Es P15 en su totalidad —`lrsql` (Apache-2.0) o `Ralph` (MIT) instrumentado desde el día 1, statements xAPI con el perfil de verbos del proyecto— y mientras el histórico se acumula, el tutor **no miente sobre lo que sabe**:

1. **Arrancar con `py-fsrs`** (MIT) como única política de secuenciación. FSRS no necesita histórico de la población: funciona por alumno desde la primera interacción, con parámetros por defecto. Es la respuesta correcta al día 1.
2. **Prerequisitos declarados a mano**, no aprendidos: un grafo de conceptos del currículo del cliente, que es trabajo de experto de dominio y no de ML. Da adaptación defendible sin ningún modelo entrenado.
3. **Medir la cobertura del dataset propio** como KPI visible del proyecto: interacciones por skill y por alumno. `pyBKT` empieza a dar estimaciones útiles cuando hay volumen por skill, y conviene que el cliente vea crecer ese número en vez de esperar un hito opaco.

**Fase C — Reentrenar con los datos del cliente y recién ahí prometer mastery (4–6 semanas, cuando la fase B dio volumen).** El mismo pipeline de la fase A, ahora sobre los statements del LRS. Acá el modelo sí es del cliente, los datos no tienen fricción de licencia porque son suyos, y la estimación es defendible ante un regulador porque es interpretable (`pyBKT` es BKT bayesiano) y porque el expediente de cómo se llegó a ella está en el LRS.

### Las piezas

| Rol | Pieza | Licencia | Nota |
|---|---|---|---|
| Dataset de validación | **`XES3G5M`** — https://github.com/ai4ed/XES3G5M | **MIT** ✅ | El único grande reutilizable. Chino, matemática, 3.er grado |
| Estimador | **`pyBKT`** — https://github.com/CAHLR/pyBKT | MIT ✅ | Interpretable, UC Berkeley. Preferible a DLKT ante un regulador |
| Estimador (alternativa potente) | **`pyKT`** — https://github.com/pykt-team/pykt-toolkit | MIT ✅ | 10+ modelos DLKT. Más potente, menos explicable. Origen China (gap 4) |
| Scheduling día 1 | **`py-fsrs`** — https://github.com/open-spaced-repetition/py-fsrs | MIT ✅ | **La pieza que hace viable el arranque en frío** |
| Almacén / fábrica de dataset | **`lrsql`** o **`Ralph`** | Apache-2.0 / MIT ✅ | Ver **P15** |
| Transporte al agente | **`learnmcp-xapi`** | MIT ✅ | 32 commits: base a forkear, no dependencia |

**Todas las piezas son permisivas.** La fricción de este patrón **no está en el código: está en los datos**, y es exactamente lo que P1, P12 y P15 no decían.

### Plazo y alcance

**12–19 semanas** de punta a punta, con un corte comercial limpio: la **fase A** (2–3 semanas) es un PoC vendible por separado que demuestra capacidad técnica sin comprometer plazos de producto; las **fases B+C** son el proyecto real. Vender A y B juntas y C como opción condicionada al volumen de datos es más honesto y se cotiza mejor que prometer "tutor adaptativo" en un solo bloque.

### Dónde se vende primero

- **Cliente con restricción de procedencia de software (cualquier región).** Acá el patrón **deja de ser opcional**. La ruta alternativa occidental que el pase 5 armó (`pyBKT` + `Aila` + `MathTutorBench` + `SafeTutors`) se sostiene en código y se rompe en datos: el único dataset permisivo es chino. Entrenar con datos propios es la **única** salida, y este patrón es cómo se hace sin que el cronograma explote. Ver gap 4.
- **North America** — combina con **P7** y **P14**. Y hay un argumento regulatorio que cae justo: **California AB 1159 prohíbe usar datos de estudiantes para entrenar modelos**, así que la fase C necesita base legal explícita y acotada al cliente. Un patrón que ya separa validación (datos de terceros) de producción (datos propios, con consentimiento) es el que se puede defender; uno que entrena sobre todo lo que encuentra, no.
- **EMEA** — el expediente del EU AI Act (**P4**) pide trazabilidad de los datos de entrenamiento, no sólo del modelo. Este patrón la produce como subproducto.
- **LATAM** — es la forma de atacar la tijera de la región (**P13**) sin depender de datasets que no existen en español: el histórico se fabrica. Encaja con la institucionalidad nueva del Observatorio de UNESCO/CEPAL, que necesita precisamente referencias metodológicas.

⚠️ **Lo que NO hay que prometer.** (1) Un modelo de mastery funcionando el día 1: no existe sin histórico, y decirlo temprano es más barato que corregirlo en la semana 10. (2) Que el modelo de la fase A transfiere al dominio del cliente: no transfiere. (3) Usar `EdNet` o `FoundationalASSIST` en el entregable: son **CC BY-NC** y un engagement es comercial — valen para investigación interna o un paper, nada más.

## P17 — Conformidad de accesibilidad como entregable auditable (agregado en el pase 8; **EMEA primero**, y es la única obligación de esta KB con fecha ya cumplida)

**El problema que resuelve.** Toda plataforma de e-learning y todo LMS que se ofrezca en la UE está alcanzado por el **European Accessibility Act**, en vigor desde el **2025-06-28**, con **WCAG 2.1 AA** como referencia técnica. A diferencia del AI Act —cuyo Annex III todavía se está escalonando— **esta fecha ya pasó**. Y a diferencia de la evaluación pedagógica, que hay que explicarle al cliente por qué la necesita, acá el cliente ya sabe que la necesita y suele no saber cómo demostrarla.

**Por qué es el patrón más fácil de vender de los dieciocho.** No compite con nada: no hay incumbente open source, no hay que desplazar a un proveedor, y el presupuesto **ya existe** — vive en cumplimiento y en compras públicas, no en innovación. En licitación pública europea la accesibilidad no es un diferencial, es un criterio de admisibilidad.

### Las piezas, todas verificadas en el pase 8

| Pieza | Licencia | Rol |
|---|---|---|
| **accessibility-agents** (419 ★, 374 commits) | **MIT** ✅ | El motor. Corre dentro de Claude Code / Copilot / Codex / Gemini CLI y revisa WCAG 2.2 AA sobre código, documentos (incluye PDF y ePub, que es donde vive el material didáctico) y markdown |
| **uisight** (128 ★) / **a11y-agents-kit** (34 ★) | **MIT** ✅ | Medición de contraste, área táctil y *theme drift*; `uisight` expone **servidor MCP**, así que el agente la consulta sin pegamento propio. **Las tres piezas de este patrón son MIT** |
| **LRS** (`lrsql` Apache-2.0 / `Ralph` MIT) | ✅ | Donde queda el registro fechado de cada verificación. Es lo que convierte un reporte en expediente |
| La plataforma del cliente | según caso | Moodle, Open edX, Canvas — sin forkear, como siempre |

### El wiring

1. **Auditoría base** con `accessibility-agents` sobre el tema del LMS, los componentes propios y el material (PDF y ePub incluidos). Sale un inventario de hallazgos WCAG 2.2 AA con severidad.
2. **Remediación** por punto de extensión — tema y plugin, nunca el core copyleft.
3. **Gate en CI:** los agentes corren en cada pull request, así que el código nuevo no puede volver a romper la conformidad. **Este paso es el producto**; la auditoría sola la hace cualquiera y caduca en un sprint.
4. **Expediente:** cada corrida escribe un *statement* al LRS. Lo que se entrega no es un PDF de auditoría, es **la serie temporal que demuestra conformidad sostenida** — que es lo que un regulador pide y lo que una auditoría puntual no puede dar.
5. **Autoría humana sobre las excepciones.** Donde la remediación automática no aplica, la decisión queda documentada y firmada por una persona.

### Plazo y alcance
**4–6 semanas** para auditoría + gate en CI + expediente sobre una plataforma. La remediación del material histórico se cotiza aparte y por volumen: es la parte grande y la que el cliente subestima siempre.

### Dónde se vende primero
**EMEA**, por el EAA, y en particular en licitación pública. **North America** entra por la vía de Section 508 y de las obligaciones de IDEA sobre materiales accesibles. **LATAM** entra más tarde y por otra puerta — la de inclusión educativa, no la de cumplimiento.

⚠️ **Lo que no promete este patrón:** que la plataforma sea *pedagógicamente* accesible para un alumno con discapacidad cognitiva. WCAG mide acceso técnico. La adaptación del contenido es **P18**, es otro trabajo, y mezclarlos en una sola propuesta es prometer de más.

## P18 — Asistente de educación especial donde redactar el IEP está prohibido (agregado en el pase 8; **North America primero**)

**El problema que resuelve, y es un problema de encuadre antes que técnico.** El docente de educación especial es el más sobrecargado del sistema y el primero que pide ayuda de AI. Pero el open source que apareció en el pase 8 apunta casi todo a **redactar y gestionar el IEP**, y esa es precisamente la tarea que las jurisdicciones de EE. UU. están cerrando: **Delaware** prohíbe usar AI para objetivos de IEP, evaluación docente y calificación subjetiva, y el marco de **Nueva York** prohíbe usar AI para el desarrollo de planes **IEP o 504**.

**La consecuencia comercial es directa: un producto que redacta IEP es invendible en los distritos más grandes del país.** Lo vendible es todo el resto del flujo, con el docente como autor de la decisión.

### La arquitectura de referencia ya existe y es `tero`

`tero` (MIT, 111 commits, Chile) implementa exactamente la postura que esta restricción obliga: ***el agente propone, el docente decide*** — **el modelo no escribe ningún archivo sin aprobación humana explícita**, y está anclado a instrumentos normativos nacionales (MINEDUC, Decreto 83, Ley 21.719) en vez de a un currículo genérico. Con **0 ★ no es una dependencia de producto**; es la referencia de diseño, y es reutilizable porque es MIT.

### Las piezas

| Pieza | Licencia | Rol |
|---|---|---|
| **`tero`** (0 ★, 111 commits) | **MIT** ✅ | Referencia de arquitectura del gate humano y de la vinculación a norma. Reutilizable |
| **`Aila`** (35 ★, 1.188 commits, Oak National Academy) | **MIT** ✅ ⚠️ *"internal use"* | Referencia teacher-facing **en producción**, la única de la KB con escala real |
| **`accessibility-agents`** (419 ★) | **MIT** ✅ | Garantiza que el material que el agente produce sea **él mismo accesible** — si el entregable para un alumno con discapacidad no cumple WCAG, el proyecto se contradice |
| **`EduBench`** + **`SafeTutors`** | **MIT** ✅ | El expediente de calidad y de seguridad pedagógica. Ver **P10** y **P11** |
| **LRS** (`lrsql` / `Ralph`) | Apache-2.0 / MIT ✅ | Registro de qué propuso el agente, qué aprobó el docente y qué rechazó. **Bajo IDEA, la trazabilidad de la decisión es la defensa del distrito** |
| **`noggimigo`** (1 ★) | **MIT** ✅ | Idea reutilizable, no dependencia: **latencia de respuesta como señal de carga cognitiva** |

### El wiring, con el límite adelante

1. **Entrada:** la acomodación **ya decidida y ya firmada** por el equipo de IEP se carga como configuración. **El sistema nunca la genera ni la sugiere.** Este límite es la primera línea de la propuesta, no una nota al pie.
2. **Adaptación de material** contra esa acomodación: nivel de lectura, segmentación, apoyo visual, texto-a-voz, andamiaje.
3. **Gate humano obligatorio** al estilo `tero`: el docente aprueba, edita o rechaza antes de que algo llegue al alumno.
4. **Verificación de accesibilidad** del artefacto producido con `accessibility-agents` (P17).
5. **Evidencia al LRS:** propuesta, decisión docente, versión entregada, resultado.
6. **Medición pedagógica** con `EduBench` y `SafeTutors` antes de entregar.

### Plazo y alcance
**8–10 semanas** para un piloto de una materia en un distrito. El trabajo caro no es el agente: es **mapear el vocabulario de acomodaciones del distrito** a transformaciones concretas de material, y eso es trabajo con los docentes, no con el modelo.

### Dónde se vende primero
**North America**, donde IDEA crea la obligación y la prohibición de IEP automatizado crea el encuadre. **EMEA** entra combinado con **P17** (EAA). **LATAM** entra por Chile, donde el Decreto 83 cumple el papel de IDEA y donde `tero` y `Ronda` dan contraparte técnica local — ver el **gap 2**.

⚠️ **Las dos frases que no se pueden decir en esta venta:** que el sistema «escribe IEPs» y que «decide acomodaciones». Las dos están prohibidas en jurisdicciones concretas y las dos son innecesarias — el valor está en las horas de preparación de material, que es donde el docente efectivamente se consume.

## Nota de licencias para todos los patrones

⚠️ **Agregado en el pase 7 del 2026-10-01 — esta tabla cubre repos, y para los patrones que entrenan un modelo (P1, P10, P12, P15, P16) eso no alcanza.** La licencia del **dataset** es una dimensión aparte y es donde vive el riesgo con más frecuencia:

| Dataset de knowledge tracing | Licencia | En un entregable facturado |
|---|---|---|
| **XES3G5M** | **MIT** ✅ | **Usable** — chino, matemática, 3.er grado: sirve para validar arquitectura, no para producción |
| **EdNet** | ⚠️ CC BY-NC 4.0 | **No usable** — sólo investigación interna |
| **FoundationalASSIST** | ⚠️ CC BY-NC 4.0 + gated | **No usable** — sólo investigación interna |

**La regla práctica:** todo patrón que entrene algo entrena **con los datos del cliente**, y por eso el LRS de **P15** es dependencia de fase 1. Ver **P16**.

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

## P19 — De la evidencia de aprendizaje a la credencial verificable (agregado en el pase 9; **transversal, se vende primero en EMEA y APAC**)

**El problema que resuelve.** El cliente puede demostrar que el alumno estudió y no puede demostrar que el alumno
**sabe** de una forma que un tercero verifique sin llamarlo por teléfono. Es el tramo que cierra todo lo que esta KB
viene construyendo: el LRS registra la evidencia (P15), el estimador de mastery decide si hay dominio (P16), y hasta este
pase **nadie convertía esa decisión en un artefacto portable y verificable**. Ese hueco es el **gap 13**.

**Por qué es vendible ahora y no antes.** Las piezas de emisión y verificación son **MIT** y existen; lo que no existe es
el pegamento. Y la demanda está medida: **46% de las instituciones de LATAM y el Caribe ya ofrecen microcredenciales**, y
los tres obstáculos declarados del segmento son **estandarización (82%)**, **preparación institucional (76%)** y
**reconocimiento formal (71%)** — los tres se atacan con conformidad al estándar, que es exactamente lo que este patrón entrega.

### Las piezas, todas verificadas en el pase 9

| Capa | Pieza | Licencia | Por qué esta |
|------|-------|----------|--------------|
| Evidencia | `lrsql` o `Ralph` (LRS xAPI) | Apache-2.0 ✅ | Ya es la capa 0 de P15. **Es la que fabrica el dato**, no un anexo de conformidad |
| Dominio | `pyBKT` (MIT, 281 ★) o `pyKT` (MIT, 441 ★) | MIT ✅ | La decisión «domina / no domina» tiene que salir de un modelo publicado y reproducible, no de un LLM. ⚠️ Entrenar con datos del cliente — ver **gap 11** y **P16** |
| Competencia | `esco-skill-extractor` | **MIT** ✅ | Traduce el objetivo de aprendizaje del cliente al vocabulario **ESCO/ISCO**. **Es la pieza que hace reconocible la credencial fuera de la institución** |
| Emisión | `digitalcredentials/issuer-coordinator` | **MIT** ✅ | **W3C VC API** + formato **Open Badges 3.0**, con revocación y suspensión desde el día uno |
| Verificación | `digitalcredentials/verifier-plus` | **MIT** ✅ | El lado del empleador: copiar/pegar, archivo, URL o **QR** |
| Billetera | `digitalcredentials/learner-credential-wallet` | **MIT** ✅ | El lado del alumno. ⚠️ **Fijar versión**: la gobernanza pasó a OpenWallet Foundation Labs tras la v2.2.10 |
| Entrada al LMS | `1EdTech/lti-1-3-php-library` | Apache-2.0 ✅ | El agente entra como herramienta LTI 1.3 conforme, sin forkear el LMS |

### El wiring

1. **El LRS es la fuente de verdad.** Toda interacción se escribe como statement xAPI (P15). Sin esto el resto no tiene insumo.
2. **El estimador decide, no el modelo de lenguaje.** `pyBKT` consume las secuencias del LRS y emite una probabilidad de
   dominio por concepto. El LLM explica y acompaña; **no firma el juicio**.
3. **El mapa a ESCO se hace una vez, en diseño.** `esco-skill-extractor` corre sobre los objetivos de aprendizaje del
   cliente —no sobre cada alumno— y produce la tabla «concepto interno → competencia ESCO». Esa tabla es un entregable
   revisable por el cliente y es lo que hace la credencial legible para un empleador.
4. **El umbral es una decisión humana documentada.** «Dominio ≥ 0,85 sostenido en dos evaluaciones separadas» se define
   con el cliente y se versiona. Es el corazón del expediente de conformidad.
5. **`issuer-coordinator` emite la credencial** cuando se cruza el umbral: OB 3.0 firmado, con la competencia ESCO adentro.
6. **Revocación desde el primer día.** Se configura el servicio de estado antes de emitir la primera credencial — un
   esquema de credenciales sin revocación es inauditable, y reconstruirlo después obliga a reemitir todo.
7. **Billetera y verificador** cierran el circuito hacia alumno y empleador.

### Plazo y alcance

**8–10 semanas** para un piloto con un programa y un conjunto acotado de competencias, suponiendo LRS ya desplegado
(si no, sumar las 3–4 semanas de P15). El trabajo real no es criptográfico —eso lo resuelven las piezas MIT— sino
**el mapa a ESCO y la definición del umbral**, que son conversaciones con el cliente.

### Dónde se vende primero

**EMEA**, porque ESCO es el vocabulario europeo y porque el marco de credenciales está en política pública (⚠️ el stack
de la Comisión está archivado en GitHub y vive en `code.europa.eu`, bloqueado para esta sesión — **abrirlo antes de
cotizar**, gap 14). Después **APAC**, donde Filipinas tiene microcredenciales en TVET vía **TESDA** y un marco de la
**CHED** en consulta pública, y donde el consorcio **MICROCASA** articula España, Italia, Indonesia, Malasia y Filipinas.
**LATAM** tiene el 46% de instituciones ya ofreciendo microcredenciales y fragmentación de reconocimiento: el argumento
ahí es conformidad al estándar como atajo al reconocimiento transfronterizo.

---

## P20 — Evaluación conforme a QTI 3 con autoría asistida (agregado en el pase 9; **transversal, y es el camino de entrada al cliente institucional grande**)

**El problema que resuelve.** El cliente quiere generar evaluaciones con AI y necesita que los ítems **vivan en su
plataforma de examen y sobrevivan a un cambio de proveedor**. Generar preguntas con un LLM a un formato propio es un
callejón: no entra en el LMS, no se audita y no migra. QTI 3 es el formato que sí.

**La decisión de arquitectura que define el patrón.** La plataforma QTI madura es **TAO** (`oat-sa/tao-core`,
**22.533 commits**) y es **GPL-2.0**. Hay dos caminos y conviene elegirlo explícito:

- **Camino A — TAO desplegada tal cual.** Cuando el cliente quiere plataforma completa (autoría, entrega, scoring,
  roles). **No se forkea**: se despliega y la AI va al lado, entregando QTI XML por webhook/LTI. Misma receta que Moodle.
- **Camino B — componente embebido, sin fricción de licencia.** Cuando el entregable es producto del cliente,
  **`amp-up-io/qti3-item-player`** (**MIT**, **certificación de conformidad QTI 3 Basic y Advanced «Delivery» de
  1EdTech**) es el runtime de entrega y la autoría se construye arriba. **Es la única pieza certificada de toda esta KB**,
  y es el argumento más fuerte que existe para decir «conforme» sin que sea una afirmación propia.

### Las piezas

| Función | Pieza | Licencia |
|---------|-------|----------|
| Generación de ítems | `Educhain` (MCQs, lesson plans, flashcards desde PDF/URL/YouTube) | MIT ✅ |
| Entrega y scoring | `amp-up-io/qti3-item-player` (camino B) o **TAO** (camino A) | MIT ✅ / GPL-2.0 ⚠️ |
| Gate de calidad pedagógica | `EduBench` (transversal a materia, incluye **Automatic Grading** y generación de preguntas) | MIT ✅ |
| Gate de seguridad pedagógica | `SafeTutors` (11 dimensiones de daño, 48 sub-riesgos) | MIT ✅ |
| Matrícula y devolución de notas | `LongsightGroup/oneroster` (OneRoster 1.1/1.2) | MIT ✅ |
| Montaje en el LMS del cliente | `1EdTech/lti-1-3-php-library` | Apache-2.0 ✅ |

### El wiring

1. `Educhain` genera ítems candidatos desde el material del cliente.
2. **Se serializan a QTI 3 XML** — no a un JSON propio. Este paso es el que hace portable todo lo demás.
3. `EduBench` y `SafeTutors` corren como **gate automático** sobre el lote: el ítem que no pasa no llega al revisor.
4. **Revisión humana obligatoria** del lote que pasó el gate. El docente aprueba; el modelo propone (la postura de `tero`).
5. El ítem aprobado se carga en el runtime QTI y **el response processing lo ejecuta la plataforma**, no el LLM — lo que
   mantiene la nota fuera del modelo, que es lo que exigen las jurisdicciones con prohibición de grading automático (P14).
6. `oneroster` devuelve las notas al SIS; LTI 1.3 monta la experiencia dentro del LMS.

### Plazo y alcance

**6–8 semanas** por el camino B con un banco de ítems de una materia. El camino A depende del despliegue de TAO y suma
2–3 semanas. Lo que no hay que subestimar es la **serialización a QTI 3**: el estándar es grande y conviene acotar los
tipos de interacción soportados en el alcance (elección múltiple, respuesta corta y emparejamiento cubren la mayoría).

### Dónde se vende primero

Donde ya hay plataforma de examen y obligación de auditoría: **EMEA** (expediente EU AI Act, P4) y **North America**
(distritos y estados con prohibición de calificación automática, P7 y P14). Es además el patrón que mejor convive con un
incumbente: no reemplaza el LMS, se le enchufa por LTI.

---

## P21 — Due diligence de interoperabilidad: el entregable que el pase 9 convirtió en vendible (agregado en el pase 9; transversal)

**El problema que resuelve, y es real porque esta KB se lo encontró de frente.** La documentación del sector sigue
citando como «la implementación open source» de estos estándares a repos que **ya no existen**. Verificado el 2026-10-01:
`concentricsky/badgr-server` → **404**; `1EdTech/caliper-php` → **404** (puesto en privado por 1EdTech, según el banner
del fork de la Universidad de Michigan); `IMSGlobal/caliper-python` → **404**; los dos repos de credenciales de la
Comisión Europea → **archivados** y mudados a un dominio distinto.

Un equipo que arranca un proyecto de credenciales o de analítica conforme leyendo listicles **va a construir sobre una
URL muerta**, y lo va a descubrir después de haber cotizado.

**El entregable.** Un informe corto y fechado, por estándar (OB 3.0 / W3C VC, QTI, OneRoster, Caliper, LTI, xAPI), con:

1. **Qué URL resuelve hoy** y qué devuelve la que todo el mundo cita. Verificado, no inferido.
2. **La licencia leída en el archivo `LICENSE`**, no la del README ni la del listicle. Esta KB lleva registradas tres
   trampas de este tipo: `FreeLingo` (prensa dice MIT, el repo dice AGPL-3.0), `Teacher-Hub` (*«MIT — free for
   non-commercial use»*, que se contradice), y `openbadgeslib` (**licencia partida**: LGPLv3 la librería, BSD-2-Clause el CLI).
   **Cuarta trampa, agregada en el pase 10 y es la peor de las cuatro:** los bundles de OpenStax en GitHub dicen
   **CC BY-NC-SA** en su `LICENSE` mientras `OATutor` y `openstax-mcp-server` declaran **CC BY 4.0** en su README, sobre el
   mismo contenido. **Y acá el `LICENSE` del repo tampoco alcanza:** OATutor declara que la licencia está **por ítem**, dentro
   de cada JSON. La regla se endurece — **la licencia del contenido no es la licencia del código, y se lee en el ítem**.
3. **La conformidad certificada**, donde exista. En esta capa vale más que las estrellas: `qti3-item-player` tiene
   **30 ★** y certificación de 1EdTech; el repo de 205 ★ de la capa **es una especificación, no código**.
4. **La cadena de custodia.** Quién mantiene hoy. `learner-credential-wallet` pasó del **DCC at MIT** a **OpenWallet
   Foundation Labs** tras la v2.2.10 (jun-2026), y la organización se renombró a **Digital Credentials Commons**.
5. **La recomendación de pinneo**: versión fijada y, donde el riesgo lo justifique, **fork propio en el repositorio del
   cliente** — que es precisamente lo que tuvo que hacer la Universidad de Michigan con Caliper.

**Plazo:** 1–2 semanas. **Cuándo venderlo:** como fase 0 de P19 o P20, o suelto ante un cliente que ya tiene un proyecto
de credenciales en marcha y no sabe sobre qué está construido.

**Por qué es defendible cobrarlo.** No es una búsqueda en GitHub: es **verificación de primera mano de la URL, del archivo
de licencia y del estado de mantenimiento**, en una capa donde las tres cosas cambiaron en los últimos dos años y donde
la fuente secundaria está desactualizada de forma sistemática. Y el costo de no hacerlo se paga entero en implementación.


## P22 — Corpus curricular con licencia auditable: el manifiesto por ítem como entregable (agregado en el pase 10; **transversal, y es condición de posibilidad de P1, P8 y P10**)

**El problema que resuelve.** Todo patrón de esta KB que enseñe algo asume que hay contenido. Diez pasadas no preguntaron de
dónde sale ni con qué licencia. Cuando se pregunta, aparece esto: los bundles de OpenStax en GitHub dicen **CC BY-NC-SA** en
su archivo `LICENSE` (3 de 3 verificados), el ITS que los curó y el servidor MCP que los sirve dicen **CC BY 4.0** en su
README, y el **metadato** del catálogo de referencia del sector (OER Commons / ISKME) es **NonCommercial**.
**NonCommercial prohíbe exactamente el uso de un entregable facturado; ShareAlike obliga a abrir la derivación hecha para el
cliente.** Es el riesgo de licencia más caro de esta KB porque **se descubre después de haber ingestado el corpus**.

**Las piezas, todas verificadas en el pase 10**

| Pieza | Licencia | Rol |
|---|---|---|
| [DSpace](https://github.com/DSpace/DSpace) | **BSD-3-Clause** ✅ | El repositorio donde vive el corpus **con su metadato de licencia por ítem**. 25.385 commits: es la pieza madura y permisiva de la capa |
| [LibreTexts/shapeshift](https://github.com/LibreTexts/shapeshift) | **MIT** ✅ | Extracción y transformación de contenido a formatos de exportación. Es el paso de ingesta, y es permisivo aunque la plataforma LibreTexts sea GPL-3.0 |
| [openstax-mcp-server](https://github.com/pythpythpython/openstax-mcp-server) | **MIT** (código) ✅ | El puente MCP hacia el agente. **Se forkea y se le corrige la declaración de licencia**, que es incorrecta en su README |
| Currículo de **Oak National Academy** | **OGL v3.0** (uso comercial permitido) ⚠️ verificar | El corpus de arranque limpio. Y `Aila` (MIT) es el asistente que ya lo usa |
| [learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) + LRS | **MIT** ✅ | Registrar qué ítem se usó con qué alumno, que es también la evidencia de atribución |

**El wiring, y el orden importa**

1. **Fase 0 — inventario de licencias, antes de ingestar nada.** Por cada fuente candidata: abrir el **archivo `LICENSE`**
   (no el README, no el badge, no el listicle) y, cuando la fuente declare licencia **por ítem**, leer el campo del ítem.
   Clasificar en tres baldes: **apta para uso comercial** (CC BY, OGL, dominio público), **ShareAlike** (usable, contamina la
   derivación) y **NonCommercial** (inutilizable en entregable pago).
2. **Fase 1 — ingesta con el metadato pegado al dato.** `shapeshift` extrae; cada ítem entra a `DSpace` **con su campo de
   licencia, su atribución y su fuente**. Un ítem sin licencia conocida no entra: se registra en la lista de excluidos.
3. **Fase 2 — el corpus del cliente se arma sólo con el balde apto.** Regla dura: **un corpus mezclado es del color de su
   ítem más restrictivo.** Si entra un ítem NC, el corpus entero es NC.
4. **Fase 3 — el agente consulta vía MCP** (fork de `openstax-mcp-server` o adaptador propio contra `DSpace`), y **cada
   respuesta puede citar la atribución del ítem que usó**, que es lo que CC BY exige y casi nadie implementa.
5. **Fase 4 — el manifiesto es el entregable.** Un documento fechado: qué ítems, qué licencia cada uno, qué quedó afuera y
   por qué, y qué obligaciones de atribución quedan vivas en producción.

**Plazo y alcance.** Fase 0 sola: **1–2 semanas**, y se vende suelta como due diligence de contenido (es hermana de **P21**,
que hace lo mismo con los estándares). Fases 0–4 sobre un dominio acotado: **6–8 semanas**.

**Dónde se vende primero.** **EMEA**, por dos razones que se refuerzan: el expediente auditable es lo que pide el EU AI Act,
y el único corpus con licencia explícitamente apta para uso comercial que encontró esta KB —Oak National Academy, OGL v3.0—
es británico. Después **North America**, donde el dinero público nuevo de Q1 2026 está etiquetado **«AI responsable»**.

**Por qué es defendible cobrarlo.** Porque el costo de no hacerlo es rehacer el corpus entero después de la auditoría legal
del cliente, y porque el hallazgo que lo motiva está verificado: **dos fuentes de primera mano declaran licencias
incompatibles sobre el mismo contenido**, y la que la industria repite es la equivocada en al menos tres títulos.

## P23 — Forkear Sunbird para un sistema educativo nacional (agregado en el pase 10; **APAC, LATAM y África**)

**El problema que resuelve.** Hasta el pase 9, la respuesta de esta KB a «plataforma para un ministerio» era Moodle
(GPL-3.0) u Open edX (AGPL-3.0). Las dos obligan a explicarle al cliente que la plataforma abierta que le proponemos lo
compromete a publicar sus modificaciones — y con AGPL, también si la sirve por red. **Sunbird elimina esa conversación.**

**Por qué Sunbird y no otra cosa**

- **MIT** ✅ — el agente vive **adentro**, no al lado.
- **38.046 commits** en el portal. Es la plataforma con más trabajo acumulado de toda esta KB después de TAO, y a diferencia
  de TAO es permisiva.
- **El fork es el modelo de adopción, no un accidente:** **317 forks contra 41 estrellas**, porque cada estado indio levanta
  su instancia. Eso es el precedente de venta: no hay que explicar que *se puede* forkear por jurisdicción — ya se hizo
  decenas de veces.
- **Escala demostrada:** sostiene **DIKSHA**, **180 M+ alumnos**, **290.000+ contenidos**, **36 idiomas**, **4.950 M+
  sesiones**. ⚠️ Cifras de fuente secundaria; lo verificado de primera mano es el repo.
- **Digital Public Good** reconocido por la DPGA — que ante un ministerio o un organismo multilateral es un argumento
  de compra, no un detalle.

**Las piezas**

| Pieza | Licencia | Rol |
|---|---|---|
| [SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** ✅ | El portal web. Se forkea al repositorio del cliente y se fija la versión por tag |
| [sunbird-devops](https://github.com/project-sunbird/sunbird-devops) | **MIT** ✅ | El despliegue. 392 forks: es lo que ejecuta la jurisdicción |
| [SunbirdEd-mobile-app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) | **MIT** ✅ | Android con **consumo offline**. Es lo que hace viable el patrón en ruralidad (converge con **P3**) |
| [sunbird-telemetry-sdk](https://github.com/project-sunbird/sunbird-telemetry-sdk) | **MIT** ✅ | Telemetría nativa, que se puentea a la capa **LRS/xAPI** del pase 6 (**P15**) |
| [Kolibri](https://github.com/learningequality/kolibri) | **MIT** ✅ | Alternativa/complemento offline donde no haya infraestructura para Sunbird completo |
| Agente pedagógico | según el caso | El tutor o el asistente docente, adentro de la plataforma, no como SaaS externo |

**El wiring, en tres fases con corte comercial limpio**

1. **Fase 1 — instancia soberana.** Fork de `SunbirdEd-portal` al repositorio del ministerio, despliegue con
   `sunbird-devops`, versión fijada por tag. Entregable: plataforma corriendo con contenido del cliente y **sin obligación de
   apertura de las modificaciones**.
2. **Fase 2 — telemetría y medición.** `sunbird-telemetry-sdk` puenteado a un LRS xAPI (**P15**), que es la base para
   cualquier medición posterior y para entrenar el estimador de mastery con datos propios (**P16**, que existe justamente
   porque los datasets públicos son NonCommercial).
3. **Fase 3 — el agente adentro.** Tutor o asistente docente sobre el contenido de la plataforma, con el corpus auditado por
   **P22** y el gate de seguridad pedagógica de **P11** antes de abrirlo a alumnos.

**Plazo y alcance.** Fase 1: **6–10 semanas** según integración de identidad y datos existentes. Las tres: **5–7 meses**.

**Dónde se vende primero.** **APAC** —el precedente es local y verificable, y en Singapur el requisito de que la AI viva
dentro de la plataforma estatal (Student Learning Space) empuja exactamente a esta arquitectura— y después **LATAM** y
**África**, donde el patrón de compra es **ministerio + organismo multilateral** y el sello de Digital Public Good pesa.
Para LATAM es además más corto que forkear Moodle, y encaja con la línea de base ya medida por UNESCO/UNU en 19 países.

**La objeción que va a aparecer, y cómo se contesta.** *«41 estrellas, ¿está vivo?»* — 38.046 commits, 317 forks y la
plataforma escolar de India corriendo encima. Ver el **trend 23**: en infraestructura pública **la estrella mide atención de
desarrolladores y el fork mide organizaciones en producción**.

## P24 — Ed-Fi como columna de datos antes del agente (agregado en el pase 10; **North America, K-12**)

**El problema que resuelve.** El pase 9 cubrió los estándares que **mueven** datos educativos —OneRoster (matrícula y notas),
Caliper (eventos), QTI (ítems), Open Badges (credencial)— y dejó afuera el que los **guarda**: el expediente longitudinal del
alumno. En K-12 de EE. UU. eso es **Ed-Fi**, está adoptado a nivel estatal, y **es Apache-2.0**. Un proyecto que mete un
agente en un distrito sin pasar por ahí termina construyendo un silo que el estado no puede leer.

**Las piezas**

| Pieza | Licencia | Rol |
|---|---|---|
| [Ed-Fi-ODS](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | **Apache-2.0** ✅ | Operational Data Store + API. **Se despliega y se consume por API; no se forkea el ODS** |
| [Ed-Fi-Data-Standard](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | **Apache-2.0** ✅ | El modelo de datos. Es el contrato al que hay que programar |
| [LTI 1.3](https://github.com/1EdTech/lti-1-3-php-library) | **Apache-2.0** ✅ | Cómo entra el agente al LMS del distrito sin forkearlo (**P20**) |
| LRS xAPI (`lrsql` / `Ralph`) + [learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | **MIT/Apache** ✅ | La evidencia granular de aprendizaje, que es de otra granularidad que el expediente (**P15**) |
| [tero](https://github.com/marcorojasb/tero) | **MIT** ✅ | La postura de diseño obligatoria en EE. UU.: *el agente propone, el docente decide* (**P18**) |

**El wiring**

1. **Leer, no escribir, al principio.** El agente consume el expediente por la **Ed-Fi ODS API** para contextualizar
   (historia del alumno, cursos, secciones) y **no escribe nada** en el ODS en la fase 1. Es lo que hace aceptable el
   proyecto ante el área de datos del distrito.
2. **La evidencia nueva va al LRS, no al ODS.** xAPI para el detalle de interacción (**P15**); el ODS guarda el expediente
   oficial. Mezclarlos es el error que hace que el distrito pierda la trazabilidad.
3. **La decisión pedagógica queda del lado humano.** Donde haya calificación, componente determinista + explicación del
   modelo (**P14**), porque varios estados prohíben el grading automático.
4. **La credencial, al final** (**P19**), con Open Badges 3.0 cuando corresponda.

**Plazo y alcance.** Integración de lectura contra una instancia Ed-Fi existente: **4–6 semanas**. Con despliegue del ODS:
**3–4 meses**.

**Dónde se vende primero.** **North America**, y el momento es bueno: **41,7%** del crecimiento global del mercado 2026-2030
es de la región y el dinero público nuevo de Q1 2026 (**USD 169 M**) está etiquetado **«AI responsable»** — que es
precisamente lo que describe esta arquitectura. Es también el contra-argumento concreto al programa a nivel país del
incumbente: **soberanía del dato del alumno, sobre un estándar que el estado ya adoptó.**

---
*Ver `intel/market.md` para la oportunidad por región y `intel/trends.md` para los gaps que estos patrones atacan.*

## P25 — Riesgo de abandono conforme al Anexo III, con el humano en el lazo (agregado en el pase 11; **EMEA y North America primero**, y es la capa con presupuesto ya asignado)

**El problema que resuelve, y es el único de esta KB donde el cliente ya tiene la partida abierta.** Toda institución
de educación superior compra *student success* / *early alert*. El open source de esa capa **no existe** (gap 18:
110 repos MIT con techo de 6 ★, el tope entrenado con datos sintéticos, el stack de Apereo archivado). Y la
regulación lo nombra: el **Anexo III del EU AI Act** cubre la evaluación de resultados de aprendizaje, el screening
de postulantes y el monitoreo de exámenes, con fecha **2027-12-02** (Reglamento (UE) 2026/1744). En EE. UU.,
**Oklahoma y Maryland exigen supervisión humana y prohíben que la AI tome decisiones de alto impacto sobre un
alumno**, y **California AB 1159 prohíbe usar datos de alumnos para entrenar modelos**.

**La consecuencia de diseño, y hay que ponerla adelante: el entregable no es el modelo, es el expediente.** Un
modelo de riesgo sin expediente de conformidad es invendible en las dos regiones donde está el dinero.

### Las piezas, todas verificadas en el pase 11

| Capa | Pieza | Licencia | Por qué esta |
|---|---|---|---|
| Motor predictivo | **Analytics API del core de Moodle** | GPL-3.0 (es el core) | Define modelos como *indicadores + target*, los evalúa y entrena internamente, con el target de alumno en riesgo incluido. **Es la base más sólida que existe hoy**, y se extiende por los puntos de extensión del core sin forkear |
| Alternativa / almacén | **OpenLRW** · https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW | **ECL-2.0** ✅ | Si el cliente no es Moodle: *learning record warehouse* que habla **xAPI + IMS Caliper + IMS OneRoster** a la vez — los tres formatos que una universidad realmente tiene. 62 ★, push del 2026-08-04 |
| Telemetría de origen | `yetanalytics/lrsql` o `openfun/ralph` *(capa del pase 6)* | Apache-2.0 ✅ | Donde el agente y el LMS escriben los statements que alimentan el modelo. Ver **P15** |
| Estado del alumno | **pyBKT** (MIT) o **pyKT** (MIT) *(capa del pase 5)* | MIT ✅ | El riesgo de abandono y el mastery son ejes distintos y se venden juntos: un alumno que no domina el prerrequisito es la explicación del riesgo, no un dato aparte. ⚠️ Pero leer el gap 11: **los datasets de knowledge tracing son NonCommercial**, y el entrenamiento se hace con datos del cliente |
| Explicabilidad | **SHAP** por caso | Apache-2.0/MIT ✅ | No opcional: es lo que convierte "el sistema marcó a este alumno" en algo que un tutor puede discutir y un auditor puede revisar |
| **Evidencia de que la intervención sirve** | **Terracotta** · https://github.com/terracotta-education/terracotta | **Apache-2.0** ✅ | RCT dentro del LMS con **consentimiento informado oculto al docente**, filtrado de no-consintientes y remoción de identificadores en las exportaciones. 2.572 commits, push del 2026-09-30 |
| Datos de arranque | **OULAD** (CC BY 4.0) y **UCI 697** (CC BY 4.0 ⚠️ confirmar) | CC BY 4.0 ✅ | Para calibrar el pipeline antes de tocar datos del cliente. ⚠️ **No son el modelo final:** UCI 697 son 4.424 alumnos portugueses de hace una década |
| Expediente | **P4** / **P17** de esta KB | — | La forma del entregable de conformidad ya está resuelta en esta KB para evaluación auditable y accesibilidad. Acá se reusa |

### El wiring

1. **Capa 0 — telemetría antes que modelo.** LRS o OpenLRW recibiendo eventos del LMS y del agente. Sin esto no hay features temporales, y las features temporales son las que predicen (ver abajo).
2. **Features conductuales y temporales, explícitamente sin atributos protegidos.** Logins, asistencia, entrega de trabajos, latencia de entrega, racha de inactividad. **El benchmark de supervivencia sobre OULAD reporta que la señal dominante es temporal y conductual, no demográfica ni estructural** (arXiv 2604.08870 🔴 sin verificar de primera mano). Eso no es una restricción ética que cueste performance: **es el hallazgo que permite no usar los atributos protegidos sin perder exactitud**, y es el argumento que aprueba el sistema ante un DPO.
3. **Modelo en la Analytics API de Moodle** (indicadores + target) o pipeline propio sobre OpenLRW. **Entrenado con datos del cliente, nunca con los del alumno en jurisdicciones donde eso está prohibido** — en California, AB 1159 lo prohíbe de frente.
4. **Salida a persona, no a sistema.** El score va a la bandeja de un tutor con su explicación SHAP y una acción sugerida. **El sistema nunca ejecuta la consecuencia** — ni baja al alumno de categoría, ni cambia su inscripción, ni le manda la notificación automática. Esto es simultáneamente el requisito de supervisión humana del Anexo III y la prohibición de Oklahoma y Maryland: **una sola decisión de arquitectura cubre las dos regulaciones.**
5. **Auditoría de equidad como artefacto publicado, no como párrafo.** Métricas por subgrupo, con el resultado en el expediente. **Ninguno de los repos verificados en el pase 11 publica esto**, y es la diferencia entre un entregable y un notebook.
6. **Terracotta para medir la intervención.** Grupo de tratamiento y control sobre la misma tarea, con el consentimiento ya resuelto. Al final del ciclo se puede decir cuánto bajó el abandono **y con qué intervalo de confianza**, en vez de mostrar la curva del modelo.

### Plazo y alcance

- **Fase 1 — telemetría + expediente (6-8 semanas).** LRS/OpenLRW desplegado, inventario de features, evaluación de impacto y diseño de supervisión humana firmados. **Esta fase se puede vender sola y es la que el cliente aprueba sin discutir**, porque es lo que ya le exige su propio comité.
- **Fase 2 — modelo + explicabilidad + auditoría de equidad (8-10 semanas).**
- **Fase 3 — RCT con Terracotta y medición del efecto (un ciclo académico).** Es la fase que produce el caso de referencia.

### Dónde se vende primero

- **EMEA:** la fecha es el driver. **2027-12-02** son ~14 meses, exactamente el plazo de un programa de conformidad institucional. Y los dos datasets de referencia son europeos y CC BY.
- **North America:** el driver no es una fecha sino una prohibición vigente que deja al cliente con presupuesto y sin forma legal de gastarlo como pensaba. **La fase 1 y el punto 4 del wiring son literalmente el producto.** 38% del mercado global.
- **LATAM:** el método ya existe y es local —papers brasileños con features validadas sobre datos reales de institutos federales, ausentismo como predictor dominante— y el dato está en el SIS. Lo que falta es la ingeniería. Ver `intel/market.md`.
- **APAC:** Vietnam ya nombró la **evaluación automatizada y el monitoreo del comportamiento** como alto riesgo en educación; se vende como P5 multi-jurisdicción con este patrón adentro.

### ⚠️ Lo que no hay que prometer en este patrón

- **No proponer ningún repo de la capa predictiva de GitHub como base de producto.** Techo de 6 ★, datos sintéticos, licencias ausentes o `NOASSERTION`. Sirven para leer feature engineering, nada más.
- **No proponer Apereo SSP, OpenDashboard ni LearningAnalyticsProcessor.** Verificado en el pase 11: el primero no tiene repo localizable, el segundo está declarado *(Deprecated)* y su reemplazo se abandonó en 2020, el tercero no tiene push desde enero de 2023.
- **No presentar métricas de los papers como métricas esperables.** Los accuracy de 0,87 y los AUC de 0,96 que circulan en esta capa están medidos sobre 4.424 registros de una institución europea. Con los datos del cliente, el número se mide; no se promete.

## P26 — Agente docente conforme al currículo nacional, con la ontología ya publicada (agregado en el pase 11; **APAC primero, EMEA segundo**)

**El problema que resuelve.** El patrón **P8** (fábrica de lecciones en la voz del docente) y el **P6** (AI literacy a
escala de sistema educativo) chocan siempre con la misma pieza: **el currículo nacional estructurado.** Es el artefacto
más caro de construir de un agente docente —hay que leer el currículo oficial, modelarlo, validarlo y mantenerlo— y es
el que ningún ministerio quiere pagar dos veces. **El pase 11 encontró que, para dos países, ya está publicado.**

### Las piezas

| Pieza | Licencia | Región | Qué aporta |
|---|---|---|---|
| **korean-elementary-learning-map** · https://github.com/DECK6/korean-elementary-learning-map | **MIT** ✅ | APAC (Corea del Sur, currículo revisado 2022) | **620 anclas de estándares de logro, 1.956 temas, 2.293 relaciones de prerrequisito, 152 clusters**, 11 materias, grados 1-6. **JSON y RDF/Turtle**, con *competency questions* en **SPARQL** y restricciones **SHACL**. ⚠️ Construcción independiente, **no producto oficial del Ministerio** |
| **OpenDidactia** · https://github.com/nmarafo/OpenDidactia | CC BY-SA 4.0 ⚠️ | EMEA (España, LOMLOE) | Esquemas de Programación Didáctica y Situación de Aprendizaje para 17 comunidades + 2 ciudades autónomas, con DUA y rúbricas. ⚠️ **Share-alike:** derivar el esquema para el cliente dispara la obligación de publicar |
| **mentar** · https://github.com/avps82/mentar | AGPL-3.0-only ⚠️ | — | Referencia de cómo se consume: **934 nodos de concepto en 157 plantillas curriculares** (ACARA v9 de Australia, India, Singapur, EE. UU.) con **checker determinístico** en vez de dejar que el modelo valide |
| **Gnos** · https://github.com/madhvantyagi/Gnos | **MIT** ✅ | — | *Teaching harness* cuyo registro de evidencia distingue **"vio la explicación" / "resolvió con ayuda" / "resolvió solo"** — la granularidad que el grafo de prerrequisitos necesita para decidir el siguiente nodo |
| **Alvarmethod** · https://github.com/vasanthsreeram/Alvarmethod | **MIT** ✅ | — | El loop pedagógico como skill portable: *probe → plan (DAG) → teach → lock-in*. **El `plan` es exactamente un recorrido sobre el grafo de prerrequisitos**, así que las dos piezas encajan sin adaptador |
| **pyBKT** / **pyKT** | MIT ✅ | — | Estimación de mastery por nodo del grafo |

### El wiring

1. **El grafo de prerrequisitos es la fuente de verdad, no el prompt.** Se carga la ontología (JSON para la aplicación, RDF/Turtle si el cliente ya tiene triple store) y se validan las restricciones **SHACL** en CI: si el ministerio cambia el currículo, el build falla antes que el agente alucine.
2. **`Alvarmethod` para el loop, con el `plan` recorriendo el grafo** en vez de pidiéndole al LLM que invente la secuencia. La diferencia es auditable: el plan de estudio queda trazado contra anclas de estándares oficiales.
3. **`pyBKT` estima mastery por nodo**, y las *competency questions* SPARQL de la ontología se reusan como consultas de cobertura: "¿qué estándares de 4.º grado cubrió este alumno?" es una consulta, no un reporte a mano.
4. **`Gnos` para la captura de evidencia** con la distinción de los tres niveles de ayuda. Sin eso, el mastery se estima sobre "respondió bien" y vale poco.
5. **El checker determinístico de `mentar` como patrón** —no como dependencia, que es AGPL—: **el LLM explica, un verificador no-LLM corrige.** Es la única forma de que el agente no le dé por bueno un error a un chico.
6. **Telemetría a LRS** (P15) para que la cobertura curricular sea un dato consultable por el ministerio y no una captura de pantalla.

### Plazo y alcance

- **6-8 semanas** para un piloto de una materia y un grado sobre un currículo **que ya tiene ontología publicada** (Corea del Sur hoy; España con la advertencia de licencia).
- **12-16 semanas** si hay que **construir la ontología** del país. Esa es la fase cara, y el gap 19 dice que conviene mirar primero si alguien ya la publicó: Brasil (BNCC), Reino Unido, Australia (ACARA, que `mentar` ya consume) y los estándares estatales de EE. UU. son candidatos sin verificar.

### Dónde se vende primero

- **APAC:** es la única región con la pieza **MIT**, completa y formalmente validada. Un engagement de currículo nacional empieza con el artefacto más caro ya resuelto y sin fricción de licencia.
- **EMEA:** España tiene el esquema, pero es **CC BY-SA**. Se puede usar como referencia y **hay que decidir adelante** si el esquema derivado se publica o se construye uno propio — es una decisión comercial, no técnica, y tomarla tarde cuesta.
- **LATAM:** la BNCC de Brasil es el equivalente obvio y **nadie verificó si está publicada en formato estructurado.** Si no lo está, construirla con autoría local es exactamente el tipo de aporte que el gap 2 recomienda, y es reusable en todo el país.

## P27 — Biblioteca de skills pedagógicas permisiva y con *eval* desde el día uno (agregado en el pase 12; **LATAM primero por autoría, North America y EMEA por demanda regulada**)

**El problema que resuelve.** Todos los patrones anteriores de esta KB arrancan desplegando algo: Moodle con plugin
(P1), OpenMAIC (P1), Sunbird forkeado (P23), Ed-Fi como columna de datos (P24). Eso pone el primer entregable a
semanas de distancia y mete al cliente en costo de infraestructura antes de que haya visto valor pedagógico. **El
estándar Agent Skills permite entregar pedagogía sin desplegar nada** —el artefacto es Markdown y corre en el harness
que el cliente ya paga— y el pase 12 midió que **la vertical educativa no ocupó ese canal: pierde 58× contra la
científica.** El hueco no es técnico ni de licencia: está vacío.

**Y el diferencial del patrón no es publicar la biblioteca: es publicarla medida.** Ninguno de los siete paquetes
pedagógicos que existen en el mundo tiene *eval* (gap 20). Una biblioteca que nazca con suite de evaluación no es la
octava de la lista: es la primera medible.

### Las piezas

| Pieza | Licencia | Qué aporta |
|---|---|---|
| **scientific-agent-skills** · https://github.com/K-Dense-AI/scientific-agent-skills | **MIT** ✅ | **La arquitectura de referencia**, y es copiable: 181 skills + 100+ bases de datos + 70+ workflows, con 47.2k ★ de validación. **Se copia la estructura, no el contenido** |
| **learning-commons-org/agent-skills** · https://github.com/learning-commons-org/agent-skills | **Apache-2.0** ✅ | El patrón de *guardrails* por workflow docente y alineación a estándares K-12. Es el único de la capa pensado para cumplimiento curricular, y es empaquetable |
| **book-to-skill** · https://github.com/virgiliojr94/book-to-skill | **MIT** ✅ | Pipeline contenido → skill: `SKILL.md` con modelos mentales (~4k tokens), un archivo por capítulo on-demand, glosario, patrones, cheatsheet. **Procesa local** |
| **UnifyingAITutorEvaluation** · https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | Taxonomía de evaluación de tutor. **Usar para medir internamente, no empaquetar** |
| **MathTutorBench** · https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | Capacidades pedagógicas abiertas en matemática. Atribución, sin *share-alike* |
| **EduGuardBench** · https://github.com/YL1N/EduGuardBench · **EduBench** · https://github.com/ybai-nlp/EduBench | ver sus filas en `agents/top.md` | Seguridad pedagógica y cobertura de escenarios educativos |
| **universal-examprep-skill** · https://github.com/ZeKaiNie/universal-examprep-skill | **MIT** ✅ | Referencia de **cita de página sobre la fuente** como mecanismo anti-alucinación. Es el patrón a copiar, y es permisivo |
| ⚠️ **education-agent-skills** · https://github.com/GarethManning/education-agent-skills | **CC BY-SA 4.0** ⚠️ | 165 skills en 20 dominios. **Referencia de cobertura de dominios — NO derivar de acá si el entregable es cerrado** |

### El wiring

1. **Fijar la taxonomía de dominios antes de escribir una skill.** Se lee `education-agent-skills` (20 dominios) y
   `scientific-agent-skills` (181 skills) **como mapa de cobertura**, y se decide el subconjunto propio. ⚠️ Leer no es
   derivar: el texto se escribe de cero con autoría propia, porque CC BY-SA contamina el derivado.
2. **Estructura por skill, copiada de la arquitectura MIT:** `SKILL.md` con el modelo mental y el índice (~4k tokens),
   un archivo por sub-tema cargado on-demand, glosario, patrones y cheatsheet de decisión. Es lo que hace que una
   biblioteca de 100+ skills no reviente el contexto.
3. **Los *guardrails* van en la skill, no en el prompt del usuario**, con el patrón de `learning-commons-org/agent-skills`
   (Apache-2.0, derivable): qué verificar primero, qué ignorar, qué formato de salida, contra qué estándar se alineó.
4. **Atribución obligatoria a la fuente**, con el patrón de `universal-examprep-skill`: toda afirmación curricular cita
   el material de origen con página. Es lo que convierte la skill en artefacto auditable y no en opinión del modelo.
5. **Contenido:** `book-to-skill` convierte el corpus del cliente —o un OER con licencia apta— en skill estructurada.
   ⚠️ **La advertencia del pase 10 es acá donde más pega:** la licencia de la fuente se verifica **antes** de convertir,
   porque el Markdown de salida **no arrastra el archivo `LICENSE`** y después no se ve. Los bundles de OpenStax en
   GitHub dicen **CC BY-NC-SA** en los tres títulos revisados.
6. **La suite de eval es parte del repo, no un anexo.** Cada release corre MathTutorBench (capacidad pedagógica),
   EduGuardBench (seguridad) y la taxonomía de UnifyingAITutorEvaluation (calidad de feedback) **contra las skills**,
   y publica el resultado versionado. Esto no existe hoy en ninguna de las siete bibliotecas del mundo.
7. **Versionado semántico y changelog pedagógico.** Una skill es un artefacto de comportamiento: si cambia, cambia la
   enseñanza. Sin SemVer no hay forma de que una escuela declare qué versión usó en el ciclo.

### Plazo y alcance

- **2-3 semanas** para una biblioteca vertical de 10-15 skills de una materia y un nivel, con eval corriendo en CI.
  **No hay infraestructura que desplegar**, y ése es el punto: es el entregable más rápido de toda esta KB.
- **8-10 semanas** para cobertura de 60-80 skills multi-materia con suite de eval completa y changelog pedagógico.
- **Costo de infraestructura: cero.** Corre en Claude Code, Codex, Cursor, Antigravity, Gemini CLI o Copilot CLI — los
  seis leen el mismo `SKILL.md`, así que el artefacto es portable y no genera *lock-in* de harness.

⚠️ **Lo que este patrón NO entrega, y hay que decirlo antes de cotizar.** Una skill no produce evidencia de
aprendizaje: no hay telemetría, no hay credencial y no hay registro institucional. Si el cliente necesita acreditar,
este patrón es la **capa pedagógica** y hay que combinarlo con P15 (telemetría a LRS) y P19-P21 (credenciales). Un
piloto de skills es barato de empezar y **no es acreditable tal como viene.**

### Dónde se vende primero

- **LATAM:** es el vacío medido del pase 12 —**cero** bibliotecas de skills educativas de origen LATAM o en español,
  contra 1 de EMEA, 4 de APAC y 1 de North America— y es la región de origen de Globant, donde el contenido pedagógico
  en español ya está. Es el gap más barato de cerrar de los veinte declarados y el único donde la autoría regional es
  en sí misma el diferencial. `tero` (MIT, Chile) ya demostró que un artefacto chico y permisivo de origen chileno
  entra en esta KB por mérito propio.
- **North America:** es donde está la **demanda regulada**. Cuatro estados (MD, ID, OK, VA) exigen política distrital
  de AI con supervisión humana, y una skill con *guardrails* y atribución **deja rastro en texto revisable** — la forma
  de evidencia que ese mandato pide. La oferta open source en esa capa es un repo de 35 ★.
- **EMEA:** el Anexo III exige trazabilidad de **cómo** se tomó la decisión pedagógica, y una skill es texto auditable
  —se lee, se versiona, se diferencia—, mucho más fácil de documentar frente a un auditor que un modelo fine-tuneado.
  Pero el activo europeo de referencia es **CC BY-SA**, así que el entregable defendible es una biblioteca permisiva
  propia, no un derivado del británico.
- **APAC:** es la región que **ya está produciendo** esta capa (4 de 7 paquetes). Entrar acá es competir, no llenar un
  hueco. El ángulo distinto es el eval: ninguno de los cuatro lo tiene.

## P28 — Retención del alumno sobre el SRS que ya está instalado, en vez de construir el motor (agregado en el pase 12; **transversal a las cuatro regiones**)

**El problema que resuelve.** El pase 5 encontró **cinco servidores MCP de mastery** —grafo de prerrequisitos,
scheduler, esquema de progreso— construidos por cinco autores sin relación, **ninguno arriba de 1 ★**. La lectura de
entonces fue "validación de mercado". El pase 12 agrega el término de comparación que faltaba y da vuelta la
conclusión: **`anki-mcp-server` tiene 499 ★ con la misma tecnología y la misma licencia**, y la diferencia es que no
inventa el modelo de dominio: expone el que el alumno **ya tiene instalado**.

Dicho de otro modo: el motor de repetición espaciada es un problema resuelto, desplegado en más de 3 millones de
dispositivos sólo en Android, y con el algoritmo moderno (**FSRS**) integrado de fábrica desde la versión 23.10 (2023).
**Construirlo de nuevo es la forma más cara de llegar a peor.**

### Las piezas

| Pieza | Licencia | Qué aporta |
|---|---|---|
| **Anki** · https://github.com/ankitects/anki | **AGPL-3.0-or-later** ⚠️ (porciones de contribuyentes BSD-3; verificado en el archivo `LICENSE`) | El SRS de facto: 31.7k ★, **+3 M de usuarios sólo en Android**, FSRS integrado desde 23.10. **Corre en la máquina del alumno** |
| **anki-mcp-server** · https://github.com/ankimcp/anki-mcp-server | **MIT** ✅ | 499 ★, 254 commits, v0.22.0 (beta declarada). Puente MCP: crear, leer y revisar mazos en lenguaje natural desde el agente |
| **AnkiConnect** (add-on, v25.11.9.0 del 2025-11-02) | — | La API HTTP local sobre `localhost` que es **la frontera de proceso** del patrón |
| **py-fsrs** · https://github.com/open-spaced-repetition/py-fsrs | **MIT** ✅ | FSRS del lado del servidor **para razonar y simular**, no para reimplantar el scheduler |
| **pyBKT** · https://github.com/CAHLR/pyBKT · **pyKT** · https://github.com/pykt-team/pykt-toolkit | **MIT** ✅ | Mastery por concepto, que es la pregunta que el SRS **no** responde (el SRS sabe cuándo repasar una tarjeta, no si el alumno domina el tema) |
| **Gnos** · https://github.com/madhvantyagi/Gnos | **MIT** ✅ | Registro de evidencia con los tres niveles de ayuda ("vio la explicación" / "resolvió con ayuda" / "resolvió solo") |

### 🔴 La condición de licencia, y es la que hace viable el patrón

**Anki es AGPL-3.0-or-later.** En el resto de esta KB eso sería una advertencia fuerte. Acá no lo es, por arquitectura:

- **No se forkea Anki ni se enlaza contra su código.** Se le habla por **AnkiConnect**, una API HTTP sobre `localhost`,
  desde un **proceso separado** (`anki-mcp-server`, MIT).
- Es exactamente la regla 2 que esta KB ya tenía escrita en `repos/foundations.md`: *«la lógica propietaria vive en un
  servicio aparte — el agente es un proceso separado con su propia licencia, hablando por API/MCP»*.
- **Anki corre en el dispositivo del alumno, no en infraestructura del cliente.** No hay distribución de un derivado y
  no hay servicio de red operado por el cliente: los dos disparadores de la AGPL quedan afuera.

⚠️ **Lo que sí hay que revisar con legal:** empaquetar, redistribuir o preinstalar Anki —o un *fork* con marca del
cliente— como parte del entregable. Ahí la AGPL aplica de lleno. Proponerlo como **cliente que el alumno ya tiene**
es otra cosa.

### El wiring

1. **El agente enseña; Anki retiene.** Terminada una sesión de tutoría (cualquiera de los tutores de P1, P7 o P27), el
   agente emite las tarjetas de lo trabajado **vía `anki-mcp-server`** al mazo del alumno. No hay base de datos de
   repaso del lado del cliente.
2. **El scheduler no se toca.** FSRS ya está en Anki. `py-fsrs` se usa del lado servidor **sólo para simular** —"¿cuánta
   carga de repaso genera este plan de estudio en 8 semanas?"— y para dimensionar el currículo, nunca para decidir el
   intervalo. Esa decisión queda en el cliente del alumno.
3. **El mastery es otra pregunta y necesita otra pieza.** `pyBKT` estima dominio **por concepto** a partir de la
   evidencia; el SRS sólo sabe de tarjetas. Las dos señales se combinan: *tarjeta vencida* (Anki) + *concepto no
   dominado* (pyBKT) = el tema vuelve a la sesión de tutoría, no sólo al mazo.
4. **La evidencia se captura con la distinción de `Gnos`**, porque "respondió bien" sin saber si fue con ayuda hace que
   el mastery estimado valga poco.
5. **La telemetría institucional va por LRS (P15), no por Anki.** Anki es del alumno y es local: lo que la institución
   necesita saber —cobertura, progreso, riesgo— se emite como xAPI desde el agente, no leyendo el mazo. **Esto es
   también lo que mantiene el patrón del lado correcto de la privacidad:** el historial de repaso nunca sale del
   dispositivo.

### Plazo y alcance

- **2-3 semanas** para enchufar `anki-mcp-server` a un tutor existente y tener emisión de tarjetas funcionando.
- **5-7 semanas** con mastery (`pyBKT`) y captura de evidencia (`Gnos`) combinados, más la emisión xAPI al LRS.
- ⚠️ **`anki-mcp-server` declara estado beta (v0.22.0).** Es la pieza más joven del patrón y la que hay que fijar por
  versión y cubrir con tests de integración propios antes de ponerla en un entregable.

### Dónde se vende primero

**Es transversal a las cuatro regiones**, y es uno de los pocos patrones de esta KB del que se puede decir eso con
fundamento: Anki no depende de currículo nacional, de estándar de interoperabilidad ni de régimen regulatorio, porque
corre del lado del alumno.

- **Donde más rinde** es en preparación de examen y certificación profesional, que es donde el SRS ya es la herramienta
  que el alumno elige solo. `kaogong-skill` (APAC) y `universal-examprep-skill` son la evidencia de que ese segmento
  está demandando exactamente esto.
- **Y donde conviene decirlo explícitamente en la propuesta** es en EMEA: el historial de repaso **no sale del
  dispositivo**, así que la capa de retención no agrega superficie de alto riesgo bajo el Anexo III ni datos personales
  nuevos que gobernar. Es un argumento de arquitectura, no de cumplimiento, y es más fuerte por eso.

---

## P29 — Capa pedagógica sobre la pila de práctica que ya está instalada (agregado en el pase 13; **North America y EMEA primero**, y es el patrón de menor costo de entrada de toda esta KB)

**El patrón invierte el orden de operaciones de P1.** P1 construye el tutor y después le busca dónde enchufarse. Acá la
infraestructura ya existe, es **BSD-3-Clause**, está desplegada desde 2014 y **ya trae runtime de agente**: lo único que
se construye es la capa pedagógica. Aplica a cualquier cliente donde **el trabajo del alumno sea ejecutable** —ciencia
de datos, ingeniería, programación, estadística, física computacional, formación técnica—.

### Las piezas, todas verificadas vía WebFetch en el pase 13

| Pieza | Licencia | Stars | Rol |
|---|---|---|---|
| https://github.com/jupyterhub/ltiauthenticator | **BSD-3-Clause** ✅ | 73 | **Entrada por LTI 1.3** desde el LMS del cliente. Probado contra **Open edX, Canvas y Moodle** |
| https://github.com/jupyterhub/jupyterhub | **BSD-3-Clause** ✅ | **8.300** | Entorno aislado por alumno, en el navegador |
| https://github.com/jupyter/nbgrader | **BSD-3-Clause** ✅ | **1.400** | Asignación, recolección, autocorrección, **tests ocultos** y tramo de corrección **manual**. v0.9.6 del 2026-09-30 |
| https://github.com/ucbds-infra/otter-grader | **BSD-3-Clause** ✅ | 161 | Alternativa a nbgrader **cuando el cliente no va a operar JupyterHub** |
| https://github.com/jupyterlab/jupyter-ai | **BSD-3-Clause** ✅ | **4.400** | **La capa de agente, y no hay que construirla.** ACP + servidores MCP propios |
| https://github.com/DavidLMS/learnmcp-xapi | MIT ✅ | 15 | Puente MCP → **xAPI**: convierte la actividad en evidencia conforme al estándar |
| https://github.com/yetanalytics/lrsql | Apache-2.0 ✅ | — | **LRS**: el almacén de evidencia (capa 0 del patrón **P15**) |
| https://github.com/CAHLR/pyBKT | MIT ✅ | 281 | Estimación de **mastery** sobre la evidencia (gap 5, patrón **P12**) |

**Cero copyleft en la pila. Cero NonCommercial. Cero fork del core del LMS.**

### El wiring

1. **El alumno entra desde el LMS que ya usa.** `ltiauthenticator` con **LTI 1.3**: el alumno hace clic en la actividad
   dentro de Moodle, Canvas u Open edX y aterriza autenticado en su entorno. **No se forkea el core AGPL/GPL del LMS**,
   que es la regla que `repos/foundations.md` viene recomendando desde la tercera pasada.
2. **El docente escribe el assignment una vez.** En `nbgrader`: celdas autocorregidas, **tests ocultos** que el alumno no
   ve, y tramos marcados para corrección manual. El artefacto es del docente, así que **no hay problema de licencia de
   contenido** (gap 15, pase 10) y **no hay fuente de datos no controlada** —que es exactamente lo que el inciso (a) de
   la ley de Vietnam castiga (trend 31)—.
3. **La corrección determinística corre primero, y el modelo no participa.** `nbgrader` autocorrige contra los tests. La
   nota de esa parte **la produce código, no un LLM**. Esto es lo que vuelve el patrón defendible donde la decisión
   automatizada está prohibida (Oklahoma, Maryland, Anexo III, Vietnam inciso (b)).
4. **Recién acá entra el agente, y sólo para explicar.** `jupyter-ai` dentro del notebook, con un servidor **MCP** propio
   que recibe *(el test que falló, el caso de prueba, el código del alumno)* y devuelve **feedback formativo**: qué
   concepto falta, no cuál es la respuesta. Es el ángulo que el pase 5 ya había identificado como correcto —«explicación
   y feedback sobre tests que ya corrieron»— y ahora tiene dónde vivir.
5. **La evidencia sale al LRS.** `learnmcp-xapi` emite las sentencias xAPI a `lrsql`: qué intentó, cuántas veces, qué
   test falló, qué explicación recibió. Eso es el expediente, y es la pieza que ninguna herramienta propietaria entrega.
6. **El mastery se estima sobre evidencia real del cliente.** `pyBKT` sobre las sentencias del LRS. ⚠️ **En California,
   AB 1159 prohíbe usar datos de estudiantes para *entrenar* modelos**: acá el uso es **estimación/inferencia**, no
   entrenamiento, y esa distinción hay que **escribirla en la propuesta**, no asumirla.
7. **El docente decide.** Ninguna nota sumativa se emite sin revisión humana; el tramo manual de `nbgrader` es el lugar
   donde eso ya está previsto por diseño.

### Plazo y alcance

- **Fase 1 (3–4 semanas):** LTI 1.3 + JupyterHub + nbgrader sobre una materia piloto, con los assignments existentes del
  docente migrados. Entregable: la cohorte corrige automáticamente lo ejecutable.
- **Fase 2 (4–5 semanas):** servidor MCP de feedback formativo + `jupyter-ai` en el notebook. Entregable: explicación por
  test fallado, con el docente revisando una muestra.
- **Fase 3 (4–6 semanas):** `learnmcp-xapi` + `lrsql` + `pyBKT`. Entregable: tablero de mastery por concepto y expediente
  de evidencia por alumno.
- **Total: 11–15 semanas**, y las tres fases tienen corte comercial limpio: la fase 1 ya es valor entregado sin AI.

### Dónde se vende primero

- **North America.** La pila es de autoría local (Jupyter/NumFOCUS; `otter-grader` del **DSEP de UC Berkeley**) y está
  desplegada en **UC Berkeley y Cal Poly**: la infraestructura es familiar y el argumento de no-decisión-automatizada
  encaja con lo que **Oklahoma y Maryland** exigen y con lo que **CA AB 1159** restringe.
- **EMEA, y es la mejor propuesta de la región.** Ya está instalada en la **Universidad de Edimburgo** y en **Aalto**. El
  cliente no necesita migrar nada: necesita **el expediente de conformidad del Anexo III (2027-12-02)** sobre lo que ya
  corre. Es **P4 aplicado a P29**, y se vende como auditoría + remediación, no como plataforma.
- **APAC, con el reloj más corto.** El vencimiento educativo de **Vietnam es 2027-09-01**, antes que el europeo. El
  diseño de los pasos 3 y 4 —corrección determinística, LLM sólo explicando— es la respuesta directa al inciso (b).
- **LATAM.** Aplica igual, y es más barato que cualquier plataforma: dentro del **87% de instituciones que ya usan AI con
  herramientas de propósito general** (trend 32), esto es lo primero que convierte ese uso informal en algo gobernado.

### ⚠️ Dónde NO proponerlo

**Si el trabajo del alumno no se ejecuta, este patrón no aplica.** Para derecho, historia, lengua o ciencias sociales no
hay análogo —es el **gap 21**— y el incumbente de la corrección de prosa sigue siendo propietario (**gap 6**, mitad no
cerrada): ahí el camino sigue siendo orquestar Gradescope (`gradescope-mcp`) y el patrón **P14**. Presentar P29 a una
facultad de humanidades es un error de encaje que se detecta en la primera reunión.

---

## P30 — Acreditar la competencia pedagógica del asistente contra el examen del Estado (agregado en el pase 13; **LATAM primero por autoría, North America segundo por educación especial**)

**El problema que resuelve.** Esta KB tiene desde el pase 4 un stack de evaluación pedagógica que nadie usa (gap 1:
*«el estándar existe, está publicado en los venues principales, y sigue sin adoptarse»*). La razón práctica es que
ninguno de esos benchmarks responde la pregunta que hace el comprador institucional, que no es *«¿qué tan bueno es tu
modelo?»* sino **«¿por qué debería creer que esto sabe enseñar?»**. `pedagogy-benchmark` responde exactamente eso, porque
**la vara no la puso un laboratorio: la puso el Estado**, y es la misma con la que se habilita a un docente humano.

### Las piezas, verificadas en el pase 13 y en pasadas anteriores

| Pieza | Licencia | Stars | Qué acredita |
|---|---|---|---|
| https://github.com/AI-for-Education/pedagogy-benchmark | **MIT** ✅ | 12 | **CDPK (920 preguntas)**: conocimiento pedagógico general, transversal a materias, edades y subdominios. **SEND (223)**: educación especial. Fuente: exámenes de habilitación docente de la **Agencia de la Calidad de la Educación** y el **CPEIP del Ministerio de Educación de Chile**. arXiv 2506.18710 |
| https://github.com/kaushal0494/UnifyingAITutorEvaluation | CC BY-SA 4.0 ⚠️ | 32 | Taxonomía de **8 dimensiones** pedagógicas ante el error del alumno (MRBench). NAACL 2025 |
| https://github.com/eth-lre/mathtutorbench | CC BY 4.0 ⚠️ | 42 | **Enseñanza en diálogo**: andamiaje, no resolución. EMNLP 2025 (Oral) |
| https://github.com/ybai-nlp/EduBench | **MIT** ✅ | 29 | 9 contextos educativos, transversal a materia, con cuatro escenarios docentes |
| https://github.com/RadiantCrystal/SafeTutors | **MIT** ✅ | 0 | **Daño pedagógico**: si enseña mal siendo amable |

**El reparto de trabajo entre ellas es el punto, y es lo que ninguna sola cubre:** `pedagogy-benchmark` mide
**conocimiento declarativo** (sabe pedagogía), `MathTutorBench` y `UnifyingAITutorEvaluation` miden **conducta en
diálogo** (sabe enseñar), `SafeTutors` mide **daño**. Presentar una sola como «evaluación pedagógica» es el error que el
pase 7 marcó con `ProHist-Bench`.

### El wiring

1. **Correr CDPK contra la configuración concreta del cliente** —el modelo elegido, con su *system prompt*, sus skills y
   su RAG—, no contra el modelo desnudo. Lo que se acredita es **el producto**, no el proveedor del LLM.
2. **Correr `SEND` aparte y reportarlo aparte.** Es la pieza que decide la venta en educación especial y **no conviene
   promediarla** con CDPK: un asistente puede estar bien en pedagogía general y mal en discapacidad, y ese promedio
   esconde exactamente el riesgo que el distrito teme.
3. **Agregar la capa conductual**: `MathTutorBench` + las 8 dimensiones de `UnifyingAITutorEvaluation` sobre diálogos
   reales del piloto. ⚠️ `UnifyingAITutorEvaluation` es **CC BY-SA 4.0**: derivar un benchmark propio con datos del
   cliente **dispara el *share-alike***. Usarlo como vara de medición es limpio; derivarlo y no publicar, no.
4. **Agregar el gate de seguridad**: `SafeTutors` (patrón **P11**) como criterio de bloqueo, no como métrica informativa.
5. **El entregable es un expediente, no un número.** *Dossier de competencia pedagógica*: resultado por subdominio, el
   delta contra el modelo base, los casos fallados con su transcripción, y el criterio de regresión para la próxima
   versión. **Eso es lo que firma un ministerio o un distrito**, y es reusable como artefacto de conformidad bajo el
   Anexo III, la ley de Vietnam y los estatutos estatales de EE. UU.

### Plazo y alcance

- **2 semanas** para el dossier CDPK + SEND sobre una configuración existente. Es un entregable corto y autónomo: se
  puede vender como diagnóstico de entrada antes de cualquier desarrollo.
- **+3 semanas** para la capa conductual y el gate de seguridad sobre diálogos del piloto.
- **Total 5 semanas**, y es el patrón más barato de esta KB después de **P27**.

### Dónde se vende primero

- **LATAM, y el argumento es de autoría.** Ante un ministerio de la región el pitch no es *«les traemos una
  herramienta»*: es **«la vara con la que el mundo está midiendo a estos modelos son los exámenes docentes de Chile, y
  ustedes producen ese mismo activo sin capitalizarlo»**. Los exámenes de habilitación, las pruebas estandarizadas y los
  marcos de competencias de los ministerios son datos de evaluación de altísimo costo de producción. **Extenderlos a más
  países de la región es un entregable de política pública que no compite con ningún proveedor.** Ver el **gap 22**.
- **North America, por educación especial.** El pase 8 documentó que redactar el IEP con AI está prohibido o restringido
  en varios estados, y el patrón **P18** puso el límite adelante (*el agente propone, el docente decide*). Lo que le
  faltaba a P18 era **cómo demostrarle al distrito que el asistente es competente** sin tocar la decisión protegida.
  **`SEND` es ese instrumento**, y es MIT. Con **35+ estados con guía oficial** y **cuatro que obligan a política
  distrital** (Maryland, Idaho, Oklahoma, Virginia), el dossier es material de cumplimiento, no marketing.
- **EMEA y APAC** lo consumen como insumo del expediente de conformidad (**P4**), no como producto propio.

### ⚠️ Los límites, y van en la primera página del dossier

- **12 estrellas y 5 commits.** `pedagogy-benchmark` es un artefacto de investigación: **se usa como vara de medición en
  un entregable, no se empaqueta como dependencia de producto.** Pinear el commit.
- **Mide conocimiento declarativo, no calidad de intervención.** Responder un examen de habilitación no es enseñarle a
  un chico. Por eso los pasos 3 y 4 no son opcionales.
- 🔴 **El paper (arXiv 2506.18710) no se pudo abrir** en el pase 13 —`arxiv.org` bloqueado por el proxy—. Licencia,
  conteos, composición CDPK/SEND y la atribución a Chile **sí** están verificados en la página del repo. **Abrir el paper
  antes de citar metodología en un entregable.**

---

## P31 — Publicar el currículo nacional como marco CASE conforme, y usarlo de eje del agente docente (agregado en el pase 14; **las cuatro regiones, con artefacto distinto en cada una**)

Es el patrón que cierra el gap 19 y abre el 23. Resuelve el problema más caro de cualquier agente docente —el mapa de
qué se enseña, en qué grado, en qué orden y con qué prerrequisitos— **sin construirlo**, y lo deja publicado contra un
estándar auditable en vez de en un JSON propietario del proyecto.

### Las piezas, todas verificadas vía WebFetch el 2026-10-01

**Capa 0 — el esquema curricular, uno por región:**

| Región | Artefacto | Licencia | Qué trae |
|---|---|---|---|
| **EMEA** | [`fh-yarbouh/oak-curriculum-ontology`](https://github.com/fh-yarbouh/oak-curriculum-ontology) (0 ★) | **OGL-3.0** datos + **MIT** código | 50.948 *key learning points*, **11.207 *misconceptions***, 7.432 prerrequisitos, 160 *threads*, 12 materias, 38 *shapes* SHACL |
| **LATAM** | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) (19 ★) | **MIT** código + **CC BY 4.0** datos | 1.721 aprendizagens, JSON/SQLite/CSV, proveniencia por registro |
| **North America** | [`commonstandardsproject/api`](https://github.com/commonstandardsproject/api) (44 ★) | **Apache-2.0** | Estándares de los 50 estados + distritos, API en vivo |
| **APAC** | [`DECK6/korean-elementary-learning-map`](https://github.com/DECK6/korean-elementary-learning-map) | **MIT** | 620 anclas, 1.956 temas, **2.293 prerrequisitos**, SPARQL + SHACL |

**Capa 1 — publicación conforme:** [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) (**Apache-2.0**, 9 ★),
**certificado para CASE Service v1.0 y CASE v1.1 con fecha 2026-02-17**. Alternativa Python:
[`infosign/compeito`](https://github.com/infosign/compeito) (**Apache-2.0**, 3 ★), que además importa CFPackages de
OpenSALT/OpenCASE y CSV compatible OpenSALT.

**Capa 2 — verificación:** [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) (**MIT**, 2 ★), que
valida CASE 1.1 y otros diez estándares en el mismo *pipeline*.

**Capa 3 — puente al agente:** [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) (**MIT**, 14 ★) es la
**implementación de referencia** del puente: cinco herramientas MCP (`bncc_lookup`, `bncc_buscar`, `bncc_listar`,
`bncc_mapa_de_foco`, `bncc_estatisticas`) sobre 1.717 habilidades. Para los otros tres países **hay que escribirlo**, y
este repo es el molde.

**Capa 4 — el agente:** cualquiera de la tabla principal de `agents/top.md`. Para generación de material docente, la
referencia sigue siendo el patrón **P8**.

### El wiring

1. **Ingerir el esquema de la región** en su formato nativo (RDF para Inglaterra y Corea, JSON para Brasil y EE. UU.).
   Pinear el commit o la versión del *dump*: el currículo cambia por acto administrativo y hay que poder decir contra
   qué versión se generó cada material.
2. **Cargar el marco en OpenCASE** y publicarlo por su API CASE v1.1. Acá se gana lo que ningún JSON propio da: el
   currículo queda **direccionable por URI estable, versionado y consumible por cualquier herramienta certificada**.
3. **Pasar `conform-ed`** como *gate* de CI sobre el endpoint publicado. Entregable: reporte de conformidad firmado.
4. **Exponerlo al agente por MCP**, siguiendo el diseño de `bncc-mcp`: *lookup* por código, búsqueda por palabra clave
   con filtros, listado por componente y año, y —la herramienta que de verdad importa— **la capa de priorización**.
5. **Anclar cada artefacto que el agente genere** (lección, ítem de evaluación, *feedback*) **al URI CASE del punto
   curricular**. Eso es lo que convierte «el agente generó una lección» en «la lección cubre el estándar X.Y.Z, y acá
   está la traza».

### Por qué este patrón se vende, en una frase por región

- **EMEA:** las **11.207 *misconceptions*** inglesas son conocimiento de diagnóstico que no se deriva de un documento
  oficial con un *script* — se construye con docentes. Es el insumo que le faltaba a **P8** para dejar de depender de
  prompt y pasar a depender de datos, y está publicado con licencia comercial.
- **North America:** el mandato de política distrital (pase 12, patrón **P7**) exige material **alineado a estándar
  estatal y auditable**. El eje de los 50 estados ya existe en Apache-2.0: deja de ser alcance a cotizar.
- **LATAM:** el **Mapa de Foco del Instituto Reúna** (396 habilidades priorizadas con capa pedagógica) es un juicio
  curricular institucional que ningún modelo puede inventar sin alucinar, y ya está expuesto por MCP con licencia MIT.
- **APAC:** el coreano trae **2.293 relaciones de prerrequisito**, que es lo que un tutor adaptativo necesita para
  secuenciar (ver **P1** y **P26**).

### Plazo y alcance

- **3-4 semanas** donde el esquema ya existe y hay puente MCP (Brasil).
- **5-7 semanas** donde el esquema existe y hay que escribir el puente MCP (Inglaterra, EE. UU., Corea).
- **El gap 23 es el entregable vendible por sí solo:** publicar un currículo nacional como marco CASE conforme es
  trabajo de **días** una vez ingerido el dato, y **nadie lo hizo todavía en ningún país**. Es un activo reutilizable
  en todo el sistema educativo y auditable contra estándar.

### ⚠️ Los límites, y van en la primera página

- **Atribución obligatoria, y no es cosmética.** OGL-3.0 y CC BY 4.0 exigen acreditar a Oak National Academy y al MEC
  **en el producto**. Es una obligación de entregable: hay que diseñarla, no descubrirla en revisión legal.
- **La licencia del código no es la del dato.** Ver advertencia 2 de la nota de método del pase 14.
- 🔴 **Australia queda afuera hasta verificar licencia.** MRAC existe (RDF/XML, JSON, SPARQL, v9.0) pero
  `www.australiancurriculum.edu.au` está **bloqueado por el proxy de esta sesión** y los términos de reuso **no se
  leyeron**. No cotizar MRAC sin abrirlos.
- **España es *share-alike*.** `OpenDidactia` es **CC BY-SA 4.0**: contamina derivados. Para un entregable comercial en
  España, tratarlo como referencia, no como dependencia.
- **0 estrellas no es 0 valor, pero sí es 0 soporte.** `oak-curriculum-ontology` tiene 0 ★: se *forkea* y se pinea, y
  el cliente tiene que saber que el mantenimiento es del proyecto, no de una comunidad.
- **No se eligió OpenSALT, y es a propósito:** tiene 45 ★ —cinco veces más que OpenCASE— pero su último estable
  (3.2.0, septiembre de 2023) apunta a **CASE v1.0**. En capas de estándar el criterio es la fecha de certificación,
  no la estrella (tendencia 33).

---

## P32 — Evaluación de lectura oral que corre en el aula y no sale del dispositivo (agregado en el pase 14; **LATAM y APAC primero por volumen, EMEA y North America por régimen de privacidad**)

Es el primer patrón de esta KB con voz, y ataca la habilidad más evaluada de los primeros años de escolaridad del
mundo: **leer en voz alta, medida en palabras por minuto y exactitud.** Hasta el pase 14 esta KB no tenía ninguna
pieza para eso (ver gap 24).

### Las piezas, verificadas el 2026-10-01

| Rol | Pieza | Licencia | ★ |
|---|---|---|---|
| **Evaluación de pronunciación y fluidez** | [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | **MIT** ✅ | **85** |
| **ASR base / adaptación a voz infantil** | [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | **Apache-2.0** ✅ | **15.5k** |
| **Memoria de aprendizaje conforme a estándar** | LRS xAPI de la capa del pase 6 (ver **P15**) | — | — |
| **Eje curricular** | el artefacto de **P31** de la región | ver P31 | — |
| **Corpus de referencia** | [`jimbozhang/speechocean762`](https://github.com/jimbozhang/speechocean762) | 🔴 **sin `LICENSE`** | 198 |

### El wiring, con el límite adelante

1. **El texto a leer sale del eje curricular de P31**, no de una lista suelta: el nivel de dificultad queda anclado
   al punto curricular y al grado, y eso es lo que vuelve comparable la medición entre aulas y entre años.
2. **La captura y el puntaje corren en el dispositivo**, con `OpenPronounce` autoalojado. Devuelve puntaje 0-100,
   **PER y WER**, confianza por palabra (0-1), distancia acústica por **DTW** y **prosodia (F0 y energía)**. De ahí se
   derivan las dos métricas que el sistema escolar usa: **palabras por minuto y exactitud**.
3. **🔴 El audio del menor no sale del dispositivo. Nunca.** Lo que se envía al LRS es **la métrica**, no la voz: PPM,
   exactitud, puntaje por fonema y el URI curricular. Esto no es una preferencia de arquitectura — es la condición
   que vuelve el despliegue proponible (ver límites).
4. **Persistir en el LRS vía xAPI** (**P15**), de modo que la progresión de fluidez sea una serie temporal auditable y
   no una captura de pantalla de una app.
5. **El docente decide la intervención.** El sistema devuelve *qué fonemas y qué palabras fallan*, con transcripción
   IPA; **no clasifica al alumno, no le asigna nivel y no deriva a educación especial.** Ver límites.
6. **Opcional, y es donde hay trabajo nuevo:** envolver el paso 2 en un **servidor MCP de cinco herramientas**
   siguiendo el molde de `bncc-mcp`, para que un agente de `agents/top.md` pueda pedir la evaluación y razonar sobre
   el resultado. **Eso no existe hoy en ninguna parte — es el gap 24**, y es la pieza que convierte este patrón en un
   tutor de lectura en vez de un instrumento de medición.

### Plazo y alcance

- **4-6 semanas** para el instrumento de medición en inglés (pasos 1-5), que es donde el corpus y los modelos están.
- **+6-10 semanas** para español o portugués, **y la mayor parte es recalibración**, no desarrollo: hay que construir
  un conjunto de validación local con voz infantil. **Es alcance propio y presupuesto propio.**
- **+3-4 semanas** para el servidor MCP del paso 6.

### Dónde se vende primero

- **LATAM y APAC por volumen y por política:** la alfabetización inicial es prioridad declarada de los sistemas
  educativos de las dos regiones, y **la arquitectura en el dispositivo encaja con despliegues de conectividad
  intermitente** — que es el mismo argumento del patrón **P3** (offline-first) y de Kolibri.
- **EMEA y North America por régimen:** procesar voz de menores **sin que el audio salga del dispositivo** es
  exactamente lo que piden el Anexo III del EU AI Act y los estatutos estatales de EE. UU. que prohíben usar datos de
  alumnos para entrenar modelos (**California e Idaho**, pase 14). Un competidor que use un servicio de nube por uso
  tiene que justificar la transferencia; este patrón no tiene que justificar nada porque no transfiere.

### ⚠️ Los límites, y son más duros que en el resto de los patrones

- 🔴 **No hay corpus permisivo en español ni en portugués.** El de referencia (`speechocean762`, 198 ★) es **inglés con
  L1 mandarín y no tiene archivo de licencia** — el README afirma uso comercial permitido, pero eso es prosa, no un
  instrumento auditable. **Conseguir los términos por escrito antes de cotizar, y no prometer cifras de precisión en
  español o portugués basadas en resultados publicados sobre ese corpus.**
- 🔴 **Fluidez no es comprensión, y confundirlas es el error pedagógico clásico de esta capa.** PPM y exactitud miden
  decodificación. Un alumno puede leer rápido y preciso sin entender nada. **El instrumento mide una cosa y hay que
  decir cuál.**
- 🔴 **Esto no diagnostica dislexia ni ninguna condición, y no deriva a educación especial.** La capa del pase 8 dejó
  escrito que el open source de educación especial «apunta a la tarea que se está prohibiendo»: redactar o decidir
  sobre el alumno con discapacidad. **Este patrón produce una métrica para que un humano decida** (ver **P18**), y esa
  frontera va en la primera página de la propuesta, no en un anexo.
- **Sesgo de acento y de variedad dialectal.** Un modelo entrenado con una variedad del español penaliza a hablantes
  de otra, y en LATAM eso se superpone con nivel socioeconómico y con población indígena. **Es riesgo de equidad
  medible y hay que medirlo**, no declararlo resuelto.
- **La pieza más fina de la región no se puede usar:** `carrera-lectora` (Chile, 1.º-4.º básico, 40 textos graduados,
  pedagogía intercultural, en el dispositivo) **no tiene licencia**. No proponerla. Pedir que la pongan es, por costo
  sobre beneficio, una de las mejores acciones disponibles en esta KB.

---

## P33 — Integridad por procedencia en vez de por detección: marcar lo que el tutor genera (agregado en el pase 15; **EMEA primero por obligación legal, LATAM segundo por norma de declaración**)

Es el patrón que cierra el **gap 25** y que le pone código a la oferta que esta KB recomienda desde el pase 4 sin
tenerlo. Y es el único patrón de esta KB cuyo entregable **tiene fecha legal**: **2026-12-02**.

**La idea entera en una línea:** dejar de preguntar *«¿esto lo escribió una AI?»* —que no tiene respuesta
confiable— y empezar a preguntar *«¿esto lo escribió **nuestro** tutor?»*, que se responde con una verificación
criptográfica.

### Por qué no se hace con detectores, y conviene tenerlo escrito antes de la reunión

La capa forense existe, es permisiva y está publicada en ICLR, ICML y ACL. **Y no se puede usar para producir
una consecuencia sobre un alumno:**

| Medición | Valor |
|---|---|
| FPR sobre escritura de **no nativos de inglés** (TOEFL, 7 detectores) | **61,3 %** |
| FPR sobre universitarios nativos | ~2,9 % |
| FPR sobre 1.180 abstracts académicos **pre-2018** | **5,85 %** + 20 % «incierto» |
| Longitud mínima para que el score sirva | **~80 palabras** |
| Efecto de la paráfrasis | **caídas grandes** (RAID) |

**La cuenta de Vanderbilt:** 1 % de FPR sobre 75.000 trabajos = **~750 acusaciones injustas por año**. Desactivaron
el detector; **más de 50 universidades** hicieron lo mismo. Y existe `humanizar-es` (MIT), que **usa Binoculars y
Fast-DetectGPT como función objetivo** para reescribir español hasta que dejen de marcarlo, distribuido como
*skill* para seis harnesses de agente. **Esa carrera no se gana.** La de procedencia sí, porque marcar en el
origen no es un clasificador que se pueda optimizar en contra.

### Las piezas, verificadas repo por repo vía WebFetch el 2026-10-01

| Rol | Pieza | Licencia | Señal |
|---|---|---|---|
| **Marcar el texto en generación** | **SynthID-Text** — `huggingface/transformers` → `src/transformers/generation/watermarking.py` | **Apache-2.0** ✅ | `SynthIDTextWatermarkLogitsProcessor`, `SynthIDTextWatermarkDetector`, `BayesianDetectorModel`. Copyright HuggingFace + Google DeepMind |
| **Probar que el marcado aguanta** | [`THU-BPM/MarkLLM`](https://github.com/THU-BPM/MarkLLM) | **Apache-2.0** ✅ | **1.100 ★**, 23+ algoritmos, **12 herramientas** de detectabilidad/robustez/calidad. EMNLP 2024 Demo |
| **Manifiesto de procedencia firmado** | [`contentauth/c2pa-rs`](https://github.com/contentauth/c2pa-rs) · [`c2pa-python`](https://github.com/contentauth/c2pa-python) | **MIT *y* Apache-2.0** (dual) ✅ | **1.907** / 344 commits. Spec **C2PA 2.4**, *CAWG identity assertion* |
| **Entrada al LMS sin forkearlo** | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) (ver **P21**) | **Apache-2.0** ✅ | Ya en esta KB desde el pase 9 |
| **Registro de la evidencia** | LRS xAPI del pase 6 — `lrsql` / `Ralph` (ver **P15**) | Apache-2.0 / MIT ✅ | Ya en esta KB |
| **Triage, nunca sanción** | [`fast-detect-gpt`](https://github.com/baoguangsheng/fast-detect-gpt) (MIT) o [`sloptotal`](https://github.com/pablocaeg/sloptotal) (MIT, 23 motores, CPU) | MIT ✅ | **Opcional, y con el límite puesto por diseño** |

### El wiring

1. **El tutor marca su propia salida.** Donde el agente llama a `generate()` sobre Transformers, se agrega un
   `WatermarkingConfig` de SynthID-Text. **No es un servicio nuevo ni un proveedor nuevo: es un parámetro.** La
   clave de marcado es del cliente y vive donde viven sus secretos.
2. **Cada salida sale con manifiesto C2PA firmado** (`c2pa-python`): qué modelo, qué versión, qué timestamp, bajo
   qué identidad institucional (*CAWG identity assertion*). Esto es el tramo con ingeniería real —custodia de
   claves y política de firma— y es el entregable que el cliente no puede hacer solo.
3. **El LMS entrega por LTI 1.3** (P21). El alumno entrega su trabajo; el servicio de verificación corre
   `SynthIDTextWatermarkDetector` contra la clave de la institución y valida el manifiesto C2PA si lo hay.
4. **El resultado es una de tres cosas, y ninguna es una acusación:**
   - **Marca válida de nuestro tutor** → uso declarado y verificado. Se registra en el LRS como evento xAPI.
     En LATAM, **esto es el cumplimiento de la norma de declaración**, automatizado.
   - **Sin marca** → no dice nada sobre autoría. Es el estado por defecto de todo texto humano y de todo texto
     generado fuera de la institución.
   - **Marca válida de otra institución o proveedor** → procedencia externa verificada.
5. **MarkLLM produce la evidencia de robustez** —detectabilidad, resistencia a edición y paráfrasis, impacto en
   calidad— que el **Artículo 50(2)** exige al pedir un marcado *«effective, interoperable, robust and reliable»*.
   **Ese informe es un entregable facturable**, no un anexo técnico.
6. **El detector forense, si entra, entra con el límite en el código:** produce **cola de revisión docente**, nunca
   una marca en el expediente, nunca una notificación automática al alumno, y **nunca como insumo único**. El
   umbral se fija con la institución y se documenta. Si el cliente pide sanción automática, **esa es la línea**:
   el **61,3 %** lo convierte en discriminación medible contra el alumnado que escribe inglés como L2.

### Lo que hay que construir, y es chico

**El puente no existe en ninguna forma open source.** No hay plugin de Moodle, XBlock de Open edX, herramienta LTI
ni servidor MCP que marque o verifique. Lo que hay en el directorio de Moodle son **envoltorios de servicios
propietarios** —Compilatio (plugin GPL-3.0, 821 instalaciones), Originality.ai, Copyleaks— que además **detectan**
en vez de marcar. El trabajo es: el servicio de verificación, la política de firma, la herramienta LTI y el
mapeo a xAPI. **Semanas, sobre infraestructura Apache-2.0 madura.**

### Plazos y por qué el orden regional es ése

| Región | Gancho | Urgencia |
|---|---|---|
| **EMEA** | **Obligación legal**: Art. 50 en vigor 2026-08-02; marcado legible por máquina para sistemas ya en mercado **2026-12-02**. Code of Practice adopta **C2PA** como estándar de facto | 🔴 **62 días** |
| **LATAM** | **Norma de declaración** ya vigente en México, Colombia y Chile (a veces con entrega de prompts). El paso 4 **la cumple automáticamente**. Y lo instalado (Turnitin Originality en UNAM, Tec, UAM, BUAP, UdeG) no la cumple | 🟡 Alta: >80 % de las IES mexicanas sin reglamento propio — ventana de definición |
| **North America** | Sin obligación. El gancho es **exposición**: 50+ universidades apagaron la detección y **no compraron reemplazo** | 🟡 Hueco abierto |
| **APAC** | **Australia**: 26 de 35 universidades (73 %) ya tienen la política de AI dentro de integridad académica — *owner* y presupuesto resueltos | 🟢 Entrada por organigrama |

**Estimación:** 6-8 semanas para el tramo EMEA con el informe de robustez de MarkLLM incluido; 4-5 si el cliente
ya tiene el tutor sobre Transformers y sólo falta C2PA + verificación + LTI.

### Lo que este patrón NO resuelve, y hay que decirlo en la primera reunión

- **Sólo cubre el texto que generó el sistema propio.** El ensayo escrito con un modelo externo no lleva marca y
  nunca la va a llevar. El patrón convierte un problema irresoluble en uno **parcial pero cierto**, más un
  **régimen de declaración** para el resto. Vender esto como «detectamos todo» es mentir y se cae en la primera
  prueba.
- **No reemplaza el rediseño de la evaluación.** Las instituciones que apagaron la detección adoptaron escritura
  en clase, defensa oral y consignas que integran AI. El patrón **convive** con eso; no lo sustituye.
- ⚠️ **No pedir evidencia de proceso sin una vía alternativa.** *«Mostrá el historial de versiones»* **no lo puede
  producir un alumno que escribe hablando**. Choca de frente con la capa de accesibilidad del pase 8 y con la de
  habla del pase 14. Si el entregable incluye evidencia de proceso, **el camino alternativo es parte del alcance**,
  no una excepción a gestionar después.
- **La detección de proceso por pulsaciones no es una opción.** Todo lo que existe es propietario (GPTZero
  Authorship, Grammarly Authorship, Turnitin Clarity, Draftback) y hay literatura de 2026 que sostiene que la
  señal **no distingue a quien compone de quien transcribe un borrador** — 🔴 **no verificable desde esta sesión,
  `arxiv.org` bloqueado por el proxy**. Anotado como pista.
- 🔴 **Verificar la fecha del Code of Practice contra la fuente oficial** antes de citarla: dos fuentes secundarias
  dan 10 de junio y 20 de julio de 2026. Las fechas de vigencia (2026-08-02) y de marcado (2026-12-02) sí son
  consistentes.


---

## P34 — Entrenar el modelo de mastery sin que el dato del alumno salga de la institución (agregado en el pase 16; **transversal, y es la salida técnica al gap 11**)

**El problema que resuelve, y lo venía arrastrando esta KB desde el pase 7.** El gap 11 estableció que los
datasets de knowledge tracing son NonCommercial salvo uno (chino), y concluyó que para un cliente con restricción
de procedencia **entrenar con los datos propios es la única opción**. El pase 16 le agrega la condición que
faltaba: bajo la *school official exception* de **FERPA**, el dato que la institución cede al proveedor sólo
puede usarse **para el fin por el que se cedió**, y usarlo para entrenar un modelo comercial general es
típicamente una violación. O sea: «entrenar con los datos propios» no es una licencia para llevarse el dato.

**La salida no es legal, es arquitectónica, y tiene tres variantes según lo que el cliente permita.**

### Las piezas, todas verificadas en el pase 16

| Pieza | Licencia | ★ | Rol |
|---|---|---|---|
| **Flower** | Apache-2.0 ✅ | 7.2k | Orquesta el entrenamiento federado. El modelo viaja, el dato no |
| **PySyft** | Apache-2.0 ✅ | 10.0k | Variante más estricta: el **cómputo** viaja y el dueño del dato lo ejecuta |
| **Opacus** | Apache-2.0 ✅ | 2.0k | DP sobre el entrenamiento PyTorch; contador de presupuesto en vivo |
| **OpenDP** | MIT ✅ | 437 | La garantía **formal** que va en el expediente. Harvard |
| **pyKT** / **pyBKT** | MIT ✅ | 441 / 281 | El modelo de mastery en sí (ya en esta KB desde los pases 4 y 5) |
| **FedGKT** | ⚠️ sin licencia | 1 | **Referencia de arquitectura, no dependencia.** Ya hace exactamente esto sobre Flower |

### El wiring

1. **Capa 0 — el dato se queda donde está.** Cada escuela/campus corre un cliente Flower contra su propio LRS
   (`lrsql` o Ralph, Apache-2.0/MIT, de **P15**). Ninguna interacción cruza el borde institucional.
2. **Capa 1 — el modelo federa.** `pyKT` (o `pyBKT` si hace falta interpretabilidad ante regulador) se entrena por
   rondas FedAvg/FedProx sobre Flower. Lo que viaja son **pesos**, no secuencias de alumno.
3. **Capa 2 — presupuesto de privacidad.** `Opacus` sobre el entrenamiento local, con ε declarado y registrado por
   ronda. Acá es donde el DPIA del Artículo 35 encuentra su evidencia.
4. **Capa 3 — el expediente.** `OpenDP` para las estadísticas agregadas que se publican hacia afuera (dashboards de
   dirección, reportes a ministerio). Es la pieza que un comité de ética reconoce sin discusión.
5. **Capa 4 — el entregable de demostración.** `synthcity` genera el dataset sintético con el que se demuestra el
   sistema, se licita y se hace QA, **sin tocar dato real en ningún momento del ciclo de venta**.

**La arquitectura no es especulativa:** `FedGKT` ya la implementa —grafos de conocimiento personales de 722
conceptos, 1.401 aristas de prerrequisito anotadas por expertos, FedAvg/FedProx sobre Flower, dataset Junyi de 25M
interacciones—. Tiene **1 estrella y no declara licencia**, así que se lee y se reimplementa; no se depende de él.

### Plazo y alcance

**8–10 semanas** para el piloto con dos instituciones federadas, incluyendo el DPIA. El multiplicador está en que
la institución número tres en adelante entra sin renegociar el tratamiento de datos: la arquitectura ya responde
la pregunta.

### Dónde se vende primero

**EMEA** (el DPIA del Artículo 35 es obligación, no argumento) y **North America K-12** (donde FERPA + COPPA
cierran la vía centralizada). En **APAC-India** el argumento es la Sección 9 de la DPDP y las sanciones de hasta
₹200 crore. En **LATAM-Brasil**, el Art. 14 de la LGPD más los informes semestrales a la ANPD.

### ⚠️ Lo que no hay que prometer en este patrón

- **Federado no es anonimato.** Sin DP encima, los pesos filtran. Si se promete privacidad, `Opacus` no es opcional.
- **DP cuesta exactitud.** Hay que medirla con `diffprivlib` antes de comprometer métricas de mastery, no después.
- **No usar `SDV`** para el dataset sintético de demostración, por mucho que sea el nombre conocido: su BUSL 1.1
  excluye explícitamente el uso comercial que este patrón hace. `synthcity`.

---

## P35 — El expediente de privacidad como entregable de entrada (agregado en el pase 16; **EMEA y North America primero**, y es la venta más chica de toda esta KB)

**Por qué existe este patrón.** Los 34 patrones anteriores venden **capacidad**. Éste vende el permiso para
ejercerla, y es el único de la KB cuyo alcance cabe en semanas y cuyo comprador (DPO, CISO, dirección jurídica) no
es el mismo que el de los demás. Sirve como puerta de entrada cuando el cliente todavía no compró el sistema.

### El entregable, que son cuatro artefactos y nada más

1. **DPIA del Artículo 35** (EMEA) o evaluación equivalente. Es **obligación legal** antes de usar una herramienta
   de AI que procese dato de alumnos, y el EDPB pide además el *balancing test* de interés legítimo documentado por
   actividad de tratamiento. La mayoría de las instituciones no lo tiene hecho para sus herramientas de AI ya
   desplegadas.
2. **Inventario de dato biométrico**, que es el que nadie hizo. Desde el **2026-04-22** la regla COPPA enmendada
   cuenta **voiceprints**, faceprints, huellas y huellas de palma como información personal. Cualquier función de
   voz —y la capa de lectura oral del pase 14 es exactamente eso— entra. Si el despliegue toca **Illinois**, BIPA
   exige consentimiento escrito con daños de **1.000 a 5.000 USD por violación**.
3. **Política de retención y borrado por escrito.** La COPPA enmendada **prohíbe la retención indefinida** y exige
   política escrita con borrado en plazo. Es el punto donde más despliegues educativos fallan, porque los logs de
   LMS y LRS se guardan «por las dudas».
4. **Matriz de base legal por flujo de dato**, incluida la frontera FERPA: qué dato se usa para prestar el servicio
   y qué dato **no puede** ir a entrenamiento de modelo general.

### Las piezas técnicas que lo vuelven demostrable

El expediente no es sólo papel. Lo que lo hace defendible es poder mostrar la implementación:

- **`OpenDP`** (MIT, Harvard) para las estadísticas agregadas publicadas — garantía formal, no promesa.
- **`Opacus`** (Apache-2.0) con ε registrado si hay entrenamiento.
- **`synthcity`** (Apache-2.0) para que los ambientes de desarrollo, demo y QA **no contengan dato real**, que es
  la mitigación más barata y la que más impresiona en una auditoría.
- **`Flower`** (Apache-2.0) si hay más de una institución.

### Plazo y alcance

**3–5 semanas.** Es el entregable más chico de esta KB y el único que se puede vender sin que el cliente haya
decidido todavía qué sistema de AI quiere.

### Dónde se vende primero

**EMEA**, porque el DPIA es obligatorio y la institución ya sabe que lo debe. **North America**, porque el reloj
COPPA **ya venció el 2026-04-22** y la conversación no es de preparación sino de exposición: a diferencia del
Artículo 50 europeo, acá no queda plazo que administrar. **LATAM-Brasil** tiene su propia versión con fecha:
plataformas con más de **1 millón de usuarios menores de 18** deben publicar **informes semestrales de impacto** y
presentarlos a la **ANPD**.

### ⚠️ Lo que no hay que prometer en este patrón

- **No es asesoría legal.** El entregable es el expediente técnico y la evidencia de implementación; la firma
  jurídica la pone el cliente o su estudio.
- **No prometer «cumplimiento COPPA» como estado binario.** Se entrega el inventario, la mitigación y la
  trazabilidad; quien declara conformidad es el operador.
- **No proponer este patrón solo en mercados sin obligación.** Donde no hay regla exigible, el argumento es
  exposición legal y no cumplimiento, y se vende distinto.

---

## P36 — El `privacy provider` del LMS como capa 0 del agente (agregado en el pase 17; **transversal, y es condición de posibilidad de P1, P15, P16 y P34**)

**El problema que resuelve, en una línea:** el dato del alumno ya está en el LMS y el LMS ya tiene la máquina para
gobernarlo, pero **ningún agente la usa** (gap 29). Y en Moodle no es opcional: el núcleo **obliga a todo plugin**
que guarde dato del alumno a saber declararlo, exportarlo y borrarlo.

**Por qué es «capa 0» y no un patrón más:** P1, P15, P16 y P34 tocan dato real del alumno. **Ninguno es
desplegable en una institución que tome en serio un pedido de borrado si el plugin que los sostiene no implementa
el contrato de privacidad del LMS.** Esto va antes, no después.

### Las piezas, verificadas en el pase 17

| Pieza | Licencia | Rol |
|---|---|---|
| https://github.com/moodle/moodle | GPL-3.0 ⚠️ | Privacy API en el núcleo (obliga a los plugins) + `tool_dataprivacy` (pedidos, delegado de protección de datos, retención) + `tool_policy` |
| https://github.com/openedx/edx-platform | AGPL-3.0 ⚠️ | `scripts/user_retirement` (6 scripts) + `lms/djangoapps/bulk_user_retirement` (API REST de retiro masivo) |
| https://github.com/openeducat/openeducat_erp | LGPL-3.0 ⚠️ | Variante autohospedada donde **la institución es el responsable del dato**: el argumento FERPA más corto de esta KB |
| `learnmcp-xapi` + el LRS de la capa del pase 6 | ver `repos/foundations.md` | Donde queda la evidencia de aprendizaje, que es **también** dato personal y entra en el mismo expediente |

### El wiring

1. **Inventario de contextos.** Enumerar dónde vive dato del alumno: LMS, LRS (xAPI), memoria del agente, logs de
   inferencia. **La memoria del agente es la que siempre se olvida**, y el gap 27 ya midió que ninguno de los 31
   agentes declara qué hace con ella.
2. **Implementar el `privacy provider` en el plugin propio** (Moodle): declarar metadatos de qué se guarda,
   exportar por contexto y borrar por usuario y por contexto. Para un plugin que **no** persiste nada, el
   `null_provider` es la declaración correcta — y declararlo es trabajo, no es nada.
3. **Conectar el retiro** (Open edX): orquestar los seis scripts y el endpoint REST desde la automatización del
   cliente; definir qué pasa con el dato en sistemas externos.
4. **Política de retención escrita**, con período configurado en `tool_dataprivacy` y borrado al cumplirse el
   propósito. Es lo que COPPA enmendada exige desde el **2026-04-22** y lo que AB 1159 refuerza.
5. **Expediente de evidencia:** por cada pedido, qué se exportó, qué se borró, de qué contextos y cuándo.

### Plazo y alcance

**4 a 6 semanas** para una institución con un LMS y un agente. **Casi no es software**: el `privacy provider` es
la única pieza de código y es chica. El resto es inventario, configuración, política y evidencia — más barato de
construir y más difícil de copiar que un plugin.

### Dónde se vende primero

**North America**, por dos razones concretas y no por madurez de mercado: el incidente de **Instructure/Canvas**
(tendencia 44) dejó a las instituciones sin poder responder qué dato de sus alumnos se expuso, y **sólo el 11 %**
de los distritos tiene evaluación rigurosa de privacidad. Después **LATAM**, donde el **vacío regulatorio juega a
favor** por única vez: este patrón entrega capacidad verificable sin ningún régimen que certificar (ver
`intel/market.md`, `### LATAM`). Y **APAC vía Australia**, el único régimen de la región con **consecuencia
aplicada** (Privacy Act + Notifiable Data Breaches, con resultados publicados por la OAIC).

### ⚠️ Lo que no hay que prometer en este patrón

- **No prometer cumplimiento.** Open edX lo niega por escrito: *«User retirement is not a compliance guarantee.
  The Open edX software makes no claim of satisfying any law or regulation.»* El cumplimiento es del **operador
  del sitio**. (Cita de snippet; `docs.openedx.org` bloqueado en esta sesión — resolver contra la fuente oficial
  antes de citarla.)
- **No forkear el LMS.** Moodle se extiende, Open edX se invoca. Un fork de AGPL-3.0 es el peor resultado posible.
- **No asumir paridad en Canvas.** No se verificó un toolset de retiro equivalente. Es alcance a dimensionar.
- **No prometer borrado de lo que ya salió hacia un modelo.** El Privacy API borra el registro, **no el modelo**.
  Eso es P37.

---

## P37 — Expediente de procedencia del dato de entrenamiento (agregado en el pase 17; **North America primero, y es obligatorio en California desde el 2027-07-01**)

**El problema:** **California AB 1159** (firmada **2026-09-13**) prohíbe usar información cubierta del alumno
—incluidos **identificadores únicos persistentes**— para **entrenar AI generativa o desarrollar modelos**, salvo
uso **estrictamente de propósito educativo y en beneficio de la institución correspondiente**. La **HESIPA**
extiende el régimen a **educación superior** desde el **2027-07-01**.

**Por qué esto es un patrón y no una nota legal:** la excepción es defendible **sólo si se puede probar**, y
**ninguna pieza open source produce esa prueba** (gap 30). Entrenar un modelo central con dato de muchas
instituciones para servir a todas —la arquitectura por defecto de la industria— **no cae obviamente dentro**.

### Las piezas

| Pieza | Licencia | Rol |
|---|---|---|
| `Flower` (capa del pase 16) | Apache-2.0 ✅ | Entrenamiento federado: el dato **no sale** de la institución. Es la mitad arquitectónica de la excepción |
| `Opacus` / `diffprivlib` / Google DP (capa del pase 16) | Apache-2.0 / MIT ✅ | Presupuesto de privacidad medible sobre el entrenamiento |
| `pyKT` / `pyBKT` | MIT ✅ | El modelo de *mastery* que se entrena, y el que AB 1159 toca |
| Privacy API de Moodle / retiro de Open edX (**P36**) | GPL-3.0 / AGPL-3.0 ⚠️ | De dónde sale el inventario de qué dato de qué alumno entró |
| `synthcity` | Apache-2.0 ✅ | Para demo, licitación y desarrollo **sin tocar dato real**: saca de alcance la pregunta entera |

### El wiring

1. **Clasificar el propósito, por institución.** La excepción es *propósito educativo estricto* **y** *beneficio
   de esa institución*. Si el modelo sirve a varias, hay que poder sostener el beneficio de cada una.
2. **Federado por defecto** donde haya dato de alumno de California: el dato no sale, el modelo viaja.
3. **Manifiesto por corrida de entrenamiento:** qué institución, qué contextos, qué rango temporal, qué
   identificadores (y la constancia de que **no** entraron identificadores únicos persistentes fuera de la
   excepción), qué presupuesto de privacidad.
4. **Atar el manifiesto al inventario de P36**, que es la única fuente que sabe qué dato existía.
5. **Ruta de borrado del modelo**, no sólo del registro: qué pasa cuando un alumno pide borrado y su dato entró a
   un entrenamiento.

### Plazo y alcance

**6 a 8 semanas** sobre una arquitectura federada que ya exista; **12 a 14** si hay que migrar de entrenamiento
central a federado.

⚠️ **Lo que este patrón NO puede prometer todavía, y hay que decirlo antes de cotizar:** el paso 5 —deshacer el
entrenamiento— **no tiene solución verificada en esta KB**. El pase 17 **no buscó `machine unlearning`** y lo deja
anotado como la acción del próximo pase (ver la nota de método). Hasta entonces, la respuesta honesta a «¿y si un
alumno pide borrado después de que su dato entrenó el modelo?» es **reentrenar sin ese dato**, con el costo que
eso tenga, y el manifiesto del paso 3 es lo que vuelve ese reentrenamiento acotado en vez de total. **Tampoco se
midió el costo de producir la evidencia** sobre una arquitectura federada real.

### Dónde se vende primero

**California**, por fecha: **2027-07-01** para educación superior, ~2,9 millones de estudiantes. Después el resto
de **North America** como anticipación (**134 proyectos en 31 estados** en 2026). Y **EMEA** como argumento
complementario: no hay prohibición de insumo equivalente, pero el **GDPR ya se aplica directamente** al
procesamiento de dato de alumnos y la base legal del entrenamiento es la misma pregunta con otro nombre.

## P38 — El derecho al olvido que alcanza al modelo, no sólo al registro (agregado en el pase 18; **EMEA primero por GDPR art. 17, North America segundo por AB 1159**)

**El problema, y es una promesa que el sector ya está haciendo sin poder cumplirla.** Una institución con un tutor
adaptativo en producción recibe un pedido de supresión. Ejecuta el flujo del LMS —`tool_dataprivacy` en Moodle, los
scripts de retiro en Open edX— y borra las filas del alumno. **El estimador de *mastery* sigue conteniendo lo que
aprendió de ese alumno.** El pase 17 lo escribió en una línea: *«borra el registro, no el modelo»*. Este patrón es
la parte que faltaba.

**Por qué ahora.** En **EMEA** el derecho de supresión del **GDPR art. 17** es directamente exigible y no distingue
entre la fila y el modelo. En **North America**, **California AB 1159** (firmada 2026-09-13) prohíbe usar
información cubierta del alumno para entrenar AI generativa o desarrollar modelos salvo la excepción de propósito
educativo, con **HESIPA** extendiéndolo a educación superior desde el **2027-07-01**: un modelo ya entrenado con
dato que no debía entrar necesita una vía de remediación, y la remediación es esta.

**El wiring, y bifurca según el modelo de dominio — esto es lo que decide el presupuesto:**

```
                 ┌─ pedido de supresión aprobado ─┐
   Moodle núcleo │  admin/tool/dataprivacy        │  (GPL-3.0, YA INSTALADO)
   (4.5+ / 5.0)  │  classes/privacy/provider.php  │  patrón: ai/provider/openai
                 └────────────┬───────────────────┘
                              │  ⚠️ este disparador NO EXISTE (gap 32) — es el trabajo de integración
                              ▼
                 ┌────────────────────────────────┐
                 │  orquestador de borrado        │  ← lo que se construye
                 └───────┬────────────────┬───────┘
                         │                │
        modelo = BKT ────┘                └──── modelo = deep KT
        pyBKT (MIT)                             pyKT (MIT)
             │                                       │
             ▼                                       ▼
   REAJUSTE sin el alumno                   torchunlearn (MIT) · SalUn (MIT)
   (EM, pocos parámetros, barato)           unlearning aproximado sobre pesos
             │                                       │
             ▼                                       ▼
   ✅ EXACT UNLEARNING                     ⚠️ APROXIMADO → el entregable
   la garantía más fuerte                  incluye la MÉTRICA DE VERIFICACIÓN
```

**Las piezas, todas con licencia verificada:**

| Rol | Pieza | Licencia |
|---|---|---|
| Pedido de borrado y declaración | Moodle núcleo: `admin/tool/dataprivacy`, `admin/tool/policy`, patrón `ai/provider/openai/classes/privacy/provider.php` | GPL-3.0 (ya instalado) |
| Referencia de `privacy provider` más completa de la comunidad | https://github.com/jeanlucio/moodle-local_aihub (4 interfaces) | GPL-3.0 |
| Estimador BKT → reajuste exacto | `pyBKT` | MIT |
| Estimador deep KT → unlearning aproximado | `pyKT` + https://github.com/Harry24k/machine-unlearning-pytorch | MIT + MIT |
| Método de unlearning con mejor costo/resultado | https://github.com/OPTML-Group/Unlearn-Saliency (SalUn, ICLR 2024 Spotlight) | MIT |
| Si el componente es un LLM afinado | https://github.com/locuslab/open-unlearning (12 métodos, TOFU/MUSE/WMDP) | MIT |
| Métricas de verificación del olvido | `open-unlearning` (10+ métricas) + https://github.com/tamlhp/awesome-machine-unlearning | MIT |

**La decisión de arquitectura que este patrón fuerza, y es contraintuitiva:** **elegir BKT en vez de deep knowledge
tracing puede ser la decisión de cumplimiento correcta aun si predice algo peor.** Con BKT el borrado es exacto,
barato y demostrable ante un regulador; con deep KT es aproximado y hay que presupuestar la verificación. Esta KB
venía recomendando `pyBKT` por madurez y licencia (pase 5, **P12**); este pase le agrega el argumento legal.

⚠️ **Lo que este patrón NO promete.** El disparador LMS → modelo **no existe en abierto** (gap 32): es trabajo de
integración de tamaño acotado, no una pieza que se instala. Y para deep KT, *«unlearning aproximado»* significa que
**queda residuo medible**: el entregable es el borrado **más** la métrica, y si el cliente necesita garantía
absoluta sobre un modelo deep, la única respuesta honesta sigue siendo reentrenar. No vender «olvido garantizado»
sobre deep KT.

⚠️ **Y el algoritmo específico de esta industria no está disponible.** **PrivacyCD / HIF** (arXiv 2511.03966) hace
exactamente esto para modelos de *cognitive diagnosis* y argumenta que los métodos genéricos son subóptimos frente
a su estructura heterogénea. **No publica código** (gap 31). Si aparece, este patrón cambia de forma y mejora.

---

## P39 — Plugin de AI para el LMS del cliente con el expediente de privacidad incluido de fábrica (agregado en el pase 18; **transversal, y es la venta más chica que cierra el gap 29**)

**El problema.** El cliente ya tiene Moodle y quiere una capacidad agéntica propia —no la del núcleo— sobre el
dato que ya tiene. El pase 17 estableció que el `privacy provider` no es opcional: el núcleo **lo exige a todo
plugin**. Hasta este pase, esta KB tenía que decir que no había referencia publicada. **Ahora hay cuatro, y tres
están en el núcleo.**

**La receta, y el orden importa porque la capa 0 es la declaración, no la funcionalidad:**

1. **Elegir el proveedor contra lo que el núcleo ya trae.** `openai`, `azureai` y `ollama` **están en el núcleo
   con su `privacy provider`** → no se cotizan. `bedrock` y `anthropic` **no están** (verificado, 404) → el
   proveedor y su `privacy provider` son alcance propio.
2. **Copiar el patrón canónico del núcleo:** `ai/provider/openai/classes/privacy/provider.php`. Tres interfaces
   —`metadata\provider`, `request\core_userlist_provider`, `request\plugin\provider`— y, **si el plugin no guarda
   nada local**, los seis métodos de export/borrado vacíos y sólo `add_external_location_link` poblado. Es
   exactamente lo que hizo Ferrara para Gemini, y funciona.
3. **Si el plugin SÍ guarda, no copiar esa forma.** Hay que implementar los seis de verdad. La referencia completa
   es `jeanlucio/moodle-local_aihub` (GPL-3.0, Brasil), que es la única de la capa con **cuatro** interfaces
   —agrega `user_preference_provider`— y declara tabla de base, 6 preferencias de usuario y 4 enlaces externos.
4. **Poner el gate humano en el camino de escritura**, no después. `mod_aigradedassign` lo tiene resuelto: el
   resultado de la AI **no afecta nota ni compleción hasta que un tutor aprueba o edita** la nota y el texto. Es
   el diseño de **P18** y es lo que exigen Oklahoma S.B. 1734 y Maryland S.B. 720.
5. **Si la promesa es que el dato no sale, usar la arquitectura de red, no una declaración.**
   `sngdtechnologies/ai-moodle-security` (**BSD-2-Clause** — la única licencia permisiva de la capa) es la
   referencia: Ollama on-site, Moodle y el modelo en redes internas **sin egreso**, sólo el proxy expuesto.
6. **Escribir la línea de «explicitly» en el expediente.** Incluso `aiprovider_ollama` declara envío externo, y la
   cadena del núcleo dice *«No user data is explicitly sent»*: no manda identidad, pero `prompttext` viaja.
   **Acotar el contenido del prompt es responsabilidad del entregable**, y decirlo por escrito evita la discusión.

**Por qué es la venta más chica de esta KB y conviene ofrecerla primero.** No requiere modelo propio, ni dato de
entrenamiento, ni infraestructura nueva: es un plugin con su declaración de privacidad bien hecha sobre un LMS que
el cliente ya opera. Es la **capa 0** de **P1**, **P15**, **P16** y **P34** (ver **P36**), y es el único entregable
de esta KB que se puede completar y auditar sin tocar el modelo del alumno.

⚠️ **Advertencia de licencia que decide la cotización.** De las piezas de la comunidad en esta capa, **las dos
usables son GPL-3.0** (`local_aihub`, `aiprovider_gemini`) — lo cual es lo esperable y lo correcto para un plugin
de Moodle, porque el núcleo es GPL-3.0+ y lo exige. `mod_aigradedassign` **no tiene archivo `LICENSE`** (sólo el
header GPL en el fuente) y `tool_aiconnect` **no muestra licencia**: a efectos de cotización se tratan como **sin
licencia**, y lo que corresponde es abrir un *issue* pidiendo el archivo. **Un plugin derivado de Moodle va a ser
GPL-3.0 de todos modos** — eso no es un obstáculo para el engagement, pero sí hay que decirlo antes de firmar.

## P40 — Propagar la supresión del LMS a la telemetría y al modelo, sin evento porque no hay evento (agregado en el pase 19; **EMEA y North America primero por régimen, LATAM con instrumento local**)

**Problema.** Un cliente aprueba un pedido de supresión en Moodle. El LMS borra sus filas. **El LRS sigue teniendo la
historia de aprendizaje del alumno y el modelo de mastery sigue teniendo su influencia en los pesos.** El pase 19
midió los tres eslabones y el del medio no borra ni en la especificación. Este patrón es el eslabón que falta,
construido con lo que hay.

**Lo que hay que saber antes de diseñarlo, y es lo que el pase 19 refutó.** No se puede hacer con un observer:

- `tool_dataprivacy` **no emite ningún evento** — 187 archivos, **cero** `trigger()`.
- `api::update_request_status()` (por donde pasa `approve_data_request()`) es **una escritura de base de datos**: setea
  `status`, `dpo`, `dpocomment` y hace `update()`. Sin evento, sin hook, sin notificación.
- El único observer registrado va **hacia adentro**: `\core\event\user_deleted` → **crear** un pedido.

> 🔴 **ACTUALIZACIÓN DEL PASE 22 — el disparador que este patrón declara inexistente SÍ existe, pero en la otra
> plataforma, y es Apache-2.0.** Todo lo de arriba sigue siendo cierto **para Moodle**. Para **Open edX** no: el plugin
> oficial `openedx/platform-plugin-aspects` (**Apache-2.0**, 528 commits) trae el **`UserRetirementSink`**, que
> **escucha la señal Django `USER_RETIRE_LMS_MISC` y elimina la PII del usuario de ClickHouse** (verificado de primera
> mano en su README). O sea: **en Open edX el disparador es una señal del framework con un listener permisivo ya
> escrito.**
>
> **Lo que esto cambia en la cotización de este patrón:**
> - **Cliente Open edX** → el extremo del disparador **deja de ser desarrollo** y pasa a ser **configuración más
>   verificación**. Lo que hay que auditar es *qué* borra (ver abajo), no *si* dispara.
> - **Cliente Moodle** → sigue siendo el sondeo del mecanismo (a), **pero ya no hay que diseñarlo de cero**: el
>   `UserRetirementSink` es la **implementación de referencia**, permisiva y en producción, del lado que recibe.
> - ⚠️ **Y no hay que sobrevenderlo:** ese sink borra **PII** (tablas de perfil), **no el registro de eventos**, que
>   Aspects conserva con el argumento de que queda *anonimizado*. Eso es el **gap 37** y está sin resolver. Ver **P45**.

**Entonces hay dos mecanismos posibles, y el (a) es el que se cotiza.**

**(a) Reloj de estado sobre `tool_dataprivacy_request` — recomendado.**

1. **Plugin `local_` propio** (GPL-3.0 por derivación del núcleo; es un plugin de Moodle, no se puede evitar) con una
   **tarea programada** (`\core\task\scheduled_task`, cada 5–15 min) que consulta
   `tool_dataprivacy_request` por filas con `type = DATAREQUEST_TYPE_DELETE` y `status` en
   `{APPROVED, COMPLETE, DELETED}` que aún no tengan marca propia de propagación.
2. **Tabla de control propia** (`local_<x>_propagation`) con `requestid`, `userid`, `stage`, `attempts`, `completed`.
   Es lo que suple la ausencia de evento: **el idempotente lo pone el plugin, no Moodle**.
3. **Fan-out en dos ramas**, cada una con su propio reintento:
   - **Telemetría.** `DELETE` de los *statements* del actor en el LRS. ⚠️ **Acá está el trabajo a medida, y hay que
     cotizarlo explícitamente:** xAPI **no define supresión** y `lrsql` (Apache-2.0) y Ralph (MIT) **no la documentan**
     (gap 33). Sobre `lrsql` es `DELETE` en SQL contra el esquema de statements; sobre Ralph, contra el backend
     (Elasticsearch/Mongo). **No es una llamada de API soportada: es intervención en el almacén, y el cliente tiene que
     firmar que lo entiende.** Si el cliente ya tiene **Learning Locker** (GPL-3.0), existe API de borrado — ⚠️ no
     verificada por esta KB, confirmar antes de prometerla.
   - **Modelo.** Si el estimador es **`pyBKT`** (MIT, no PyTorch): **reajustar desde cero sin el alumno** — barato, y da
     ***exact unlearning***, la garantía más fuerte que existe. Si es **`pyKT`** (MIT, PyTorch): *unlearning* aproximado
     con **`torchunlearn`** (MIT) **más la métrica de verificación con las métricas de *membership inference* de
     `OpenUnlearning`** (MIT). **Sin esa métrica el entregable es una promesa; con ella es un número.**
4. **Registro de auditoría** de cada etapa, con fecha y resultado, que es lo que se adjunta al expediente (**P35**).

**(b) Disparar desde afuera, si el cliente ya tiene orquestación.** Exponer el borrado como web-service y llamarlo desde
el sistema que ya coordina identidad. **Antecedente conocido:** `local_gdpr_deleteuserdata` (GPL-3.0, Dorel Manolescu),
que expone el borrado del Privacy API como web-service. ⚠️ **Antecedente de diseño, no dependencia:** es de **2018-07-08**
y declara requerir **Moodle 3.5** cuando el núcleo va por **5.3**; `moodle.org` está bloqueado por el proxy de esta
sesión y **no se localizó repositorio en GitHub**. Leer el patrón, no instalar el plugin.

**Contramedida obligatoria del mismo patrón, por P-MIA (tendencia 50).** Si el proyecto expone un **dashboard de
mastery**, el vector de estado de conocimiento **no se publica crudo**: ruido o cuantización sobre el vector expuesto, o
control de acceso por rol para que el vector completo no salga del lado docente. **Razón:** P-MIA (arXiv 2511.04716)
revierte los vectores de estado **desde las visualizaciones de radar** y con eso infiere pertenencia al entrenamiento.
**La decisión —cuánto ruido, qué rol ve qué— se escribe en el expediente**, porque es exactamente el tipo de
compensación entre explicabilidad (Anexo III) y minimización (GDPR) que un auditor quiere ver justificada.

**Piezas, todas verificadas en el pase 19:** Moodle 5.x (`core_ai` como plantilla de `privacy provider`, **GPL-3.0**) ·
`lrsql` **Apache-2.0** o Ralph **MIT** · `pyBKT` **MIT** / `pyKT` **MIT** · `torchunlearn` **MIT** · `OpenUnlearning`
**MIT** · plugin propio **GPL-3.0**.

**Tiempo estimado:** 6–8 semanas para la rama de telemetría + modelo BKT; **10–12** si el estimador es deep knowledge
tracing (la métrica de verificación es la mitad del trabajo).

**Por qué se vende.** Es la respuesta a *«¿y si un padre pide que borren todo?»*, que ningún cliente puede contestar hoy
y que **tres regímenes ya exigen**: art. 17 del GDPR (EMEA), **AB 1159** + leyes estatales (North America), **Ley 21.719**
chilena y marco brasileño (LATAM). Y es honesto en su alcance: **no promete borrado estándar de la telemetría, porque el
estándar no lo tiene** — cotiza la intervención en el almacén como lo que es.

⚠️ **Límite declarado:** el mecanismo (a) está **verificado en el fuente** (esquema, flujo de `update_request_status()`,
ausencia de eventos con control negativo) pero **no ejecutado contra una instancia de Moodle**. Es diseño leído del
código, no integración probada.

## P41 — Tutor con procedencia obligatoria y abstención fuera de alcance, para el inciso (1) de la Decisión 33 de Vietnam (agregado en el pase 19; **APAC primero por obligación con fecha, transversal por calidad**)

**Problema.** La **Decisión 33** de Vietnam clasifica como **alto riesgo** el *«contenido automatizado para apoyar el
autoaprendizaje del alumno usando **fuentes de datos no controladas**»*. Eso **no describe un modelo peligroso: describe
la arquitectura por defecto de casi todo tutor LLM** — un RAG apuntado a material arbitrario, o un modelo contestando de
memoria. Un tutor que no puede decir **de dónde salió cada afirmación** cae en el inciso.

**Y esta vez la contraparte no es una recomendación: son dos repos verificados en el pase 19.**

1. **Capa de enseñanza con citación obligatoria — `universal-examprep-skill`** (**MIT**, 299 ★, 181 commits). Declara
   **citación `archivo p.N` en cada concepto enseñado** y **100 % de abstención fuera de alcance**. Ingesta PDF/PPTX/DOCX/
   Markdown del material **del curso**, examina con las preguntas reales de la materia y registra errores. Instalable
   como skill en 40+ agentes. **Es el inciso (1) contestado con una propiedad declarada del artefacto**, no con una
   política.
2. **Aislamiento del corpus — `lumen`** (GPL-3.0, 88 ★, 828 commits) como **referencia de arquitectura**: RAG **con
   alcance por curso y citación, detrás de un único autorizador**, con aislamiento explícito para que cursos privados y
   clonados no filtren datos, decisiones del agente auditables en una tabla `llm_calls`. ⚠️ GPL-3.0: se copia el diseño
   (autorizador único + *scoping* por curso + log de decisiones), no el código, si el entregable es cerrado.
3. **Procedencia del material de origen — `openstax-mcp-server`** (MIT el código) con **la advertencia del pase 10
   puesta**: su README declara el contenido CC BY 4.0 y los bundles de OpenStax en GitHub dicen **CC BY-NC-SA** en los
   tres títulos verificados. **«Fuente controlada» implica licencia verificada título por título**, no sólo origen
   conocido. Para currículo nacional, los esquemas del pase 14 y **P31**.
4. **Marcado de lo generado — SynthID-Text** (Apache-2.0, dentro de Hugging Face Transformers, **P33**): cierra el otro
   extremo, porque lo que el tutor **genera** también tiene que ser distinguible de la fuente.
5. **Telemetría de la decisión — `learnmcp-xapi`** (MIT) sobre `lrsql` (Apache-2.0): deja registro de qué se enseñó con
   qué evidencia, que es lo que un régimen de alto riesgo audita. ⚠️ **Con el gap 33 declarado en el contrato:** ese
   almacén **no sabe borrar**; si el proyecto necesita supresión, entra **P40**.

**Alcance regulatorio, con fechas reales.** Vietnam: **2027-03-01** para un sistema nuevo (**5 meses desde hoy**),
**2027-09-01** si ya operaba antes del 2026-08-15 (**11 meses**) — **el sistema nuevo tiene menos plazo**. Y el mismo
entregable sirve, sin rehacerlo, para el **Anexo III** europeo (2027-12-02), para los mandatos de supervisión humana de
**Oklahoma y Maryland**, y para el inciso (2) de Vietnam vía **P5**.

**Tiempo estimado:** 6–8 semanas. **Por qué es la venta de entrada en APAC:** es chica, tiene fecha legal, y el
diferenciador —**citación con número de página y abstención fuera de alcance**— es verificable por el cliente en una
demo de diez minutos, no en una auditoría de seis meses.


## P42 — El expediente de conformidad como corrida reproducible, no como documento (agregado en el pase 20; **transversal, y es el que vuelve ejecutables P4, P10, P11, P17 y P39**)

**El problema que resuelve, y es un problema de esta KB antes que de un cliente.** Cinco patrones de este archivo
prometen un *expediente de conformidad* —**P4** (Anexo III europeo), **P10** (probar que el tutor enseña), **P11**
(gate de seguridad pedagógica), **P17** (accesibilidad), **P39** (privacidad)— y hasta el pase 19 ninguno decía **con
qué herramienta se corre la prueba**. El entregable era un documento. Un documento no se vuelve a correr cuando el
cliente cambia de modelo, y en 2026 el cliente cambia de modelo cada trimestre.

**Lo que cambia:** la máquina existe, es permisiva, y la publican reguladores. El entregable pasa de *informe* a
**pipeline que se vuelve a correr en cada cambio de modelo y emite el mismo informe con datos nuevos**.

### Las piezas, todas verificadas vía WebFetch en el pase 20

| Capa | Pieza | Licencia | Rol |
|---|---|---|---|
| Ejecutor | `aiverify-foundation/moonshot` (353 ★) | **Apache-2.0** | *Benchmarking* + *red-teaming*: alucinación, contenido indeseable, **divulgación de dato del alumno**, vulnerabilidad adversaria |
| Pipeline | `aiverify-foundation/moonshot-cicd` (14 ★) | **Apache-2.0** | La misma corrida dentro de CI/CD, con Docker y S3. **Es la pieza que vuelve el expediente reproducible** |
| Mapeo regulatorio | `compl-ai/compl-ai` (211 ★) | **Apache-2.0** | 29 benchmarks sobre los **6 principios núcleo del EU AI Act**. La pieza del expediente europeo |
| Sustrato de evals | `UKGovernmentBEIS/inspect_ai` (2.900 ★) | **MIT** | Donde se escribe la prueba pedagógica que no existe. 200+ evals pre-construidas, *model-graded* |
| Extensión de datos | `aiverify-foundation/moonshot-data` (45 ★) | **Apache-2.0** | Donde entra el dataset educativo como *recipe* / *cookbook* |
| Extensión de código | `aiverify-foundation/aiverify-developer-tools` (9 ★) | **Apache-2.0** | Donde entra el algoritmo de test propio |
| Informe | `aiverify-foundation/moonshot-ui` (12 ★) | **Apache-2.0** | Salida **HTML con gráficos** + JSON: lo que lee un comité de ética o una inspección |
| Contenido pedagógico | `EduBench` · `SafeTutors` | **MIT** | El qué se mide: 9 contextos educativos, 4.000+ situaciones, 12 dimensiones; y el daño |
| Contenido pedagógico | `MathTutorBench` · `UnifyingAITutorEvaluation` | CC BY 4.0 / **CC BY-SA 4.0** ⚠️ | Taxonomía de 8 dimensiones y *reward models* de calidad de enseñanza. **El share-alike se dispara si se deriva un benchmark propio con dato del cliente** |

### El wiring, y es el trabajo del gap 35

```
   EduBench (MIT) ─┐
  SafeTutors (MIT) ─┼──► empaquetado como *recipe* / cookbook ──► moonshot-data (Apache-2.0)
                    │         ⚠️ ESTE PASO NO EXISTE (gap 35) — es el trabajo de integración
                    │
  prueba pedagógica ┴──► plugin de test ──► aiverify-developer-tools (Apache-2.0)
                                                      │
   agente educativo del cliente ◄───── evalúa ────────┤
                                                      ▼
                                              moonshot-cicd  (corre en cada deploy)
                                                      │
                            ┌─────────────────────────┴────────────────────────┐
                            ▼                                                  ▼
                 moonshot-ui → informe HTML                      compl-ai → mapeo a los 6
                 (comité de ética, inspección)                   principios del EU AI Act
```

**Las tres fases, con corte comercial limpio:**

1. **Fase 1 — la corrida base, sin nada educativo (2–3 semanas).** `moonshot-cicd` sobre el agente del cliente con los
   *cookbooks* del Starter Kit de IMDA ya existentes: alucinación, contenido indeseable, **divulgación de datos**,
   prompts adversarios. **Ya entrega valor** y no depende de cerrar ningún gap. Es la demo de diez minutos.
2. **Fase 2 — la capa pedagógica (4–6 semanas).** Empaquetar `EduBench` y `SafeTutors` (**MIT, sin fricción**) como
   *recipes* y escribir la prueba pedagógica propia sobre `inspect_ai`. **Acá se cierra el gap 35**, y es el
   diferenciador: nadie en el mercado tiene esto, porque los tres catálogos de la capa declaran cobertura de
   **derecho, medicina y finanzas** y no de educación.
3. **Fase 3 — el mapeo regulatorio (3–4 semanas, sólo EMEA).** Mapear las pruebas a los 6 principios de `compl-ai`
   para el expediente del **Anexo III**. Sólo tiene sentido donde el régimen es exigible.

**Plazo y alcance.** Fase 1: **2–3 semanas**. Las tres: **3–4 meses**.

### Dónde se vende primero, y hay un orden

1. **LATAM** — es donde el desajuste es mayor y la competencia, nula: **Brasil** (PL 2338/2023 pide **evaluación de
   impacto algorítmico** y **auditorías periódicas**), **Chile** (Ley 21.719 vigente + proyecto con auditoría para alto
   riesgo) y **México** (**auditoría al menos anual** de alto riesgo) legislan la auditoría y **la región no produce
   una sola herramienta que la ejecute**. Motor de compra normativo + cero oferta local.
2. **EMEA** — es donde el régimen es **vinculante** (aplicación desde el **2026-08-02**, Anexo III el **2027-12-02**) y
   donde la pieza mapeada es local (`compl-ai`, ETH Zürich). Fase 3 obligatoria.
3. **North America** — el argumento de entrada es el **crosswalk a NIST AI RMF**: no es software exótico, está mapeado
   al marco federal que el cliente ya conoce. Y con **134 proyectos de ley en 31 estados**, el comprador ya tiene el
   problema.
4. **APAC** — es donde nació la herramienta, así que el diferenciador no es traerla: es **la capa educativa que le
   falta**.

⚠️ **Lo que este patrón NO promete, y hay que decirlo en la primera reunión.**

- **No certifica.** `aiverify` declara por escrito que no define estándares éticos y **no garantiza** que el sistema
  evaluado esté libre de riesgos o sesgos. Se entrega **evidencia reproducible**, que es lo que una auditoría pide.
- **El marco de Singapur es voluntario** (sin penalidad, sin registro, sin *enforcement*). Moonshot es **herramienta**
  en un proyecto europeo, nunca **cumplimiento** europeo.
- **No hay crosswalk directo de AI Verify al EU AI Act** — sólo a **NIST AI RMF** (oct-2023) y a **ISO/IEC 42001:2023**
  (jun-2024). Al AI Act se llega **indirecto por ISO 42001**.
- **`aiverify` no evalúa agentes** (tabular e imagen supervisados). El tutor se prueba con Moonshot, Inspect o COMPL-AI.
- **`LLM-Evals-Catalogue` no tiene licencia declarada**: se lee para orientarse, **no se incorpora** a un entregable.
- **`MathTutorBench` es CC BY 4.0 y `UnifyingAITutorEvaluation` es CC BY-SA 4.0.** Derivar un benchmark propio con dato
  del cliente **dispara el share-alike** del segundo. Las dos piezas limpias son `EduBench` y `SafeTutors` (MIT).

**El bonus de posicionamiento, y no cuesta nada extra.** Como las dos puntas son MIT y Apache-2.0, la capa educativa se
puede **contribuir hacia arriba**: a `moonshot-data`, a `compl-ai` (ETH Zürich) o al `LLM-Evals-Catalogue` del
regulador singapurense. Un entregable de cliente se convierte en **la referencia pública de evaluación educativa de la
industria**, que es exactamente el hueco que los tres catálogos declaran tener.

## P43 — El alumno simulado que de verdad no sabe, para evaluar al tutor sin poner chicos adelante (agregado en el pase 20; **transversal, y es la pieza que le faltaba a P10**)

**El problema que resuelve.** **P10** promete *probar que el tutor enseña, no que responde*, y el **gap 1** viene
diciendo desde el pase 4 que el estándar de evaluación pedagógica **existe, está premiado en EMNLP, NAACL y ACL, y no
se adopta en producción**. Una de las razones prácticas de esa no-adopción es que **medir enseñanza requiere un alumno
que no sepa**, y las dos opciones conocidas son malas: poner alumnos reales (lento, caro y, con menores, regulado — ver
el pase 16) o pedirle a un LLM que *«actúe como principiante»*, que **no funciona**: el modelo se escapa hacia
explicaciones de experto y el diálogo deja de medir lo que se quería medir.

**La pieza nueva, y es educativa.** `GEMLab-HKU/Unlearn_and_Relearn` (**MIT**, 4 ★, 22 commits, Universidad de Hong
Kong) ataca exactamente eso: aplica **machine unlearning** para volver **genuinamente novato** a un modelo que sabe, de
forma **configurable (10–50% de olvido)**, y después mide cuánto **recupera** cuando se le enseña. Arquitectura de tres
etapas y un loop de tres partes **Coach / Teachable Agent / Judge**.

### Las piezas

| Pieza | Licencia | Rol |
|---|---|---|
| `GEMLab-HKU/Unlearn_and_Relearn` | **MIT** ✅ | **Arquitectura de referencia.** Unlearning por destilación con intervención → relearning → loop Coach/Teachable Agent/Judge |
| `torchunlearn` (`machine-unlearning-pytorch`) | **MIT** ✅ | Los 20 algoritmos de *unlearning* si hay que reimplementar la etapa 1 |
| `UnifyingAITutorEvaluation` | CC BY-SA 4.0 ⚠️ | La taxonomía de **8 dimensiones** contra la que se puntúa al tutor |
| `MathTutorBench` | CC BY 4.0 ⚠️ | *Reward models* entrenados de calidad de enseñanza y leaderboard |
| `EduBench` · `SafeTutors` | **MIT** ✅ | Las piezas limpias: 9 contextos educativos y seguridad pedagógica |
| `moonshot` / `inspect_ai` | **Apache-2.0** / **MIT** ✅ | Donde corre todo esto como prueba repetible (ver **P42**) |

### El wiring

1. **Fabricar el alumno.** Tomar un modelo abierto y aplicarle *unlearning* sobre los **componentes de conocimiento
   específicos** de la materia del engagement, al nivel de olvido que corresponda al curso (el repo parametriza 10–50%).
2. **Enseñarle con el tutor del cliente.** El tutor a evaluar toma el rol de **Coach** contra el *Teachable Agent*.
3. **Medir recuperación, no satisfacción.** La métrica es **cuánto conocimiento recupera el alumno simulado**, puntuado
   con la taxonomía de 8 dimensiones y los *reward models* de `MathTutorBench`. **Es la métrica que P10 siempre quiso y
   no tenía cómo producir:** no mide si la respuesta del tutor es buena, mide si **el alumno aprendió**.
4. **Empaquetarlo como prueba.** Entra como *recipe* en **P42** y se vuelve a correr en cada cambio de modelo.

**Plazo y alcance.** Prueba de concepto sobre una materia: **4–6 semanas**. Como capa de evaluación integrada a P42:
**2–3 meses**.

**Dónde se vende primero.** **EMEA** y **North America**, por la misma razón y es regulatoria: donde hay supervisión
humana obligatoria y prohibición de decisiones de alto impacto (Oklahoma, Maryland) o evaluación de conformidad previa
(Anexo III), **evaluar al tutor sin exponer alumnos reales es un argumento de cumplimiento, no sólo de ingeniería**. Y
en **North America** hay un filo extra: **AB 1159 prohíbe usar dato de alumnos para entrenar modelos** — un alumno
sintético producido por *unlearning* **no es dato de alumno**.

⚠️ **Lo que este patrón NO promete.**

- **4 estrellas y 0 forks.** Es **arquitectura de referencia, no dependencia** — mismo criterio con el que el pase 8
  trató a `tero`. Hay que leer el código antes de comprometerlo en un plan.
- **El paper no se verificó de primera mano:** `arxiv.org` y `link.springer.com` están bloqueados por el proxy de
  egreso de esta sesión. Lo verificado es el **repo** (licencia MIT, 22 commits, autoría GEMLab-HKU).
- **No cierra el gap 34 y no hay que presentarlo como privacidad.** Este *unlearning* es **pedagógico**: borra para
  fabricar un alumno, no para proteger a uno. El derecho al olvido sobre el modelo de *mastery* sigue siendo el **gap
  34**, y su camino es **P38** / **P40**.
- **El alumno simulado no reemplaza la validación con alumnos reales** para un despliegue. Reemplaza la **iteración**:
  permite cien corridas antes de la primera clase, no evitar la primera clase.

## P44 — La supresión del alumno en la telemetría, que resulta que ya estaba implementada: encenderla, evidenciarla y propagarla (agregado en el pase 21; **EMEA primero por art. 17, North America por AB 1159, LATAM con la Ley 21.719 chilena**)

**Problema.** Esta KB vendió durante seis pasadas que el almacén de telemetría del alumno **no sabía borrar**, y que
intervenirlo era alcance a medida. **Es falso**, y el pase 21 lo verificó leyendo el código de los tres LRS (ver la
tendencia **54**). El trabajo real es otro, es mucho más chico, y es el que este patrón empaqueta: **encender una
capacidad que viene apagada, producir la evidencia que la capacidad no produce, y conectar el disparador que
efectivamente no existe.**

**Por qué es el patrón de menor costo de entrada de toda esta KB.** No hay que construir el borrado. Hay que
configurar, instrumentar y conectar.

### Las piezas, todas ya verificadas en esta KB

| Pieza | Licencia | Rol en este patrón |
|---|---|---|
| **`lrsql`** (Yet Analytics) | **Apache-2.0** ✅ | El almacén. **Trae el primitivo**: `DELETE /admin/agents` por `actor-ifi`, cascada sobre 7 tablas, transaccional |
| **Moodle** `tool_dataprivacy` | GPL-3.0 ⚠️ | El lado donde el pedido de supresión **se registra y se aprueba** (pase 19). No forkear: plugin |
| **`learnmcp-xapi`** | **MIT** ✅ | El puente agente ↔ LRS que esta KB ya recomienda. Declara `lrsql` como backend |
| **OpenUnlearning** | **MIT** ✅ | Sólo si el alcance incluye el modelo. Es el **gap 34**, y no hay que prometerlo acá |

### El wiring, en tres pasos, y el tercero es el único que es desarrollo

**Paso 1 — encender el primitivo. Es una variable de entorno, no una historia de usuario.**

```bash
# lrsql, config de producción: viene en false
LRSQL_ENABLE_ADMIN_DELETE_ACTOR=true
```

Con el flag apagado **la ruta no se registra** (`routes.clj:407`), así que el síntoma es un 404 y no un 403 — conviene
saberlo antes de depurarlo. Encendido, la supresión de un alumno es **una llamada**:

```
DELETE /admin/agents        body: { "actor-ifi": "mbox::mailto:alumno@escuela.edu" }
  └─> delete-actor-and-dependents!   (una transacción, 7 tablas)
        statement_to_statement · statement_to_activity · attachment · xapi_statement
        agent_profile_document · state_document · actor
        └─> statement_to_actor se borra por ON DELETE CASCADE
```

**Paso 2 — producir la evidencia, porque el producto no la produce.** Acá se cierra el **gap 36**. `lrsql` responde
`200` con el `actor-ifi` que le mandaste y **descarta el conteo de filas afectadas**, que el SQL ya calcula
(`-- :result :affected`). Dos caminos, y conviene hacer los dos:

- **El entregable del cliente:** envolver la llamada en un servicio propio que, **antes** de borrar, cuente los
  statements del actor (`GET /xapi/statements?agent=…`), **después** vuelva a contar, y registre el par
  *(antes, después, timestamp, operador, id del pedido en `tool_dataprivacy`)* en un registro append-only. **Eso es el
  expediente del art. 17**, y es lo que un régimen de alto riesgo audita.
- **La contribución hacia arriba:** devolver el `:affected` en el body del interceptor. Son pocas líneas sobre un repo
  **Apache-2.0**, el dato ya existe, y convierte un entregable de cliente en posicionamiento público — el mismo
  movimiento que el pase 20 identificó para el gap 35.

**Paso 3 — el disparador, que es el único trabajo real y hay que cotizarlo como integración.**

```
Moodle tool_dataprivacy              ⚠️ ESTE PASO NO EXISTE — es el trabajo de integración
  pedido aprobado  ──────────?──────────▶  DELETE /admin/agents   ──▶  ✅ borra
       │                                                                    │
       │ no hay evento de "borrado completado"                              │ no hay evento
       │ (pase 19, verificado en el árbol de Moodle)                        │ (pase 21)
       ▼                                                                    ▼
  hay que sondear tool_dataprivacy_request.status            hay que registrar el conteo uno mismo
```

Ninguno de los dos extremos emite evento, así que el pegamento es **un sondeo más un registro**, no una suscripción.
**Y la limitación está reconocida por un proveedor, lo que la vuelve defendible en una propuesta:** el Feature Wiki de
**ILIAS** declara por escrito que al borrar un objeto xAPI/cmi5 el dato personal **persiste en el LRS** y que ILIAS
**no tiene forma de borrarlo** (tendencia **55**). No es una carencia que invente esta KB.

### Cómo se cotiza, que es lo que cambió

| | Lo que esta KB cotizaba hasta el pase 20 | Lo que corresponde cotizar |
|---|---|---|
| Borrado en el LRS | **Desarrollo a medida** sobre el almacén, o asumir copyleft | **Configuración.** Una variable de entorno |
| Evidencia | No estaba identificada | **Servicio chico + registro append-only** (gap 36) |
| Disparador LMS→LRS | Desarrollo | **Desarrollo** — sigue siendo esto, y es lo único |

### ⚠️ Lo que este patrón NO promete

- **No alcanza al modelo.** Borra el **registro** (statements, documentos de estado y perfil, el actor). **No borra la
  influencia del dato sobre el estimador de *mastery***: eso es el **gap 34** y el camino es **P38**. Prometer "derecho
  al olvido" sin decir esto es prometer de más.
- **No es conformidad con el estándar, y hay que escribirlo en el contrato.** **xAPI / IEEE 9274.1.1 no define
  supresión** —define *voiding*, que marca sin borrar—. El endpoint de `lrsql` es **extensión propia del producto**: si
  el cliente cambia de LRS, **esto no es portable**.
- 🔴 **Con Ralph sobre ClickHouse este patrón no se puede ejecutar — y CORRECCIÓN DEL PASE 22: eso no es una
  elección del cliente, es el default de Open edX.** El pase 21 escribió esta advertencia como condicional (*«si el
  cliente ya eligió ese backend por analítica»*). **No es condicional.** El plugin de analítica **oficial** de Open
  edX —**Aspects**, `openedx/tutor-contrib-aspects`, Apache-2.0, 2.269 commits— **instala Ralph sobre ClickHouse**,
  junto con Superset, Vector, event-routing-backends y dbt. Un cliente con Open edX y analítica **no eligió** el
  backend difícil de borrar: lo tiene de fábrica. **Hay que levantarlo en el discovery como supuesto por default**,
  no al llegar al expediente de privacidad.
  **Y la razón hay que decirla bien:** ClickHouse no tiene `UPDATE`/`DELETE` de propósito general al estilo OLTP, pero
  **sí** tiene borrado liviano sobre MergeTree detrás de un setting y mutaciones `ALTER TABLE … DELETE`. La
  imposibilidad **práctica** se sostiene —no transaccional, dependiente de versión, y el backend ClickHouse de Ralph
  no lo expone en la API del LRS—, pero *«el motor no puede»* es falso y un arquitecto del cliente lo va a corregir.
  ⚠️ Dependiente de versión, no verificado de primera mano. Ver **P45** y el **gap 37**.
- **Con Learning Locker, cuatro condiciones más:** el flag `ENABLE_STATEMENT_DELETION` (en `false` el worker descarta
  el job **en silencio**), la **ventana UTC** de borrado y la dependencia del proceso *scheduler* que rescata los jobs
  fuera de ventana, el hecho de que **`done:true` no significa borrado** (hay que comparar `deleteCount` contra
  `total`), y que **`terminate` no es rollback**. Más el dato que decide: **el código no se mueve desde el
  2021-11-16** (tendencia **56**).
- **El borrado no es reversible y no hay confirmación previa.** `delete-actor-and-dependents!` corre en una
  transacción y no tiene *dry-run*. El conteo previo del paso 2 cumple además esa función: **es la única oportunidad de
  ver qué se va a borrar antes de borrarlo.**

---

## P45 — El expediente de supresión sobre Open edX + Aspects: la plataforma donde el disparador ya existe y lo que falta es la auditoría de qué se borró de verdad (agregado en el pase 22; **EMEA primero por art. 17, North America por AB 1159, transversal por Anexo III**)

**Problema.** Un cliente sobre **Open edX** con analítica tiene, sin haberlo decidido, el stack oficial **Aspects**:
Ralph sobre ClickHouse, Superset, dbt. Cuando llega un pedido del art. 17, pasan dos cosas al mismo tiempo y las dos
hay que decirlas: **(1)** el disparador existe —el `UserRetirementSink` escucha `USER_RETIRE_LMS_MISC` y borra la PII
de ClickHouse—, y **(2)** lo que queda en la telemetría es el **registro conductual completo**, conservado con el
argumento de que está *anonimizado*. **El entregable de este patrón no es construir el borrado: es auditar y
evidenciar qué se borró, y cerrar por contrato lo que no.**

**Por qué es distinto de P44.** P44 es el patrón para **`lrsql`**: ahí el primitivo de borrado es excelente
(por `actor-ifi`, 7 tablas, transaccional) y **viene apagado**. Acá el primitivo es **parcial** (PII sí, eventos no) y
**viene encendido**. Son dos ventas distintas: P44 enciende y evidencia; **P45 audita, acota y documenta.**

### Las piezas, todas verificadas en esta KB

| Pieza | Licencia | Rol en este patrón |
|---|---|---|
| **`tutor-contrib-aspects`** · `openedx` | **Apache-2.0** ✅ | El stack que el cliente **ya tiene**: ClickHouse + Superset + Ralph + Vector + event-routing-backends + dbt |
| **`platform-plugin-aspects`** · `openedx` | **Apache-2.0** ✅ | Donde vive el **`UserRetirementSink`** y el flag `ASPECTS_ENABLE_PII`. **Es el archivo que hay que leer**, no el que hay que escribir |
| **Open edX** `user_retirement` | AGPL-3.0 ⚠️ | El lado donde el pedido se registra y se aprueba. **No forkear:** el sink entra por señal, es el punto de extensión limpio |
| **`inspect_ai`** (UK AISI) | **MIT** ✅ | Para empaquetar la auditoría como **corrida reproducible** y no como documento. Es **P42** aplicado acá |
| **OpenUnlearning** | **MIT** ✅ | Sólo si el alcance incluye el modelo. Es el **gap 34** y **no hay que prometerlo** |

### El wiring, en cuatro pasos, y el único desarrollo real es el paso 3

**Paso 1 — leer el sink antes de prometer nada. Es el paso que decide si el resto del patrón es vendible.**
Hay que contestar la pregunta del **gap 37** sobre la instancia del cliente: cuando corre el `UserRetirementSink`,
**¿qué le pasa al identificador del actor en las tablas de eventos — se borra, se rota o se deja?**

```
UserRetirementSink  ──escucha──▶  señal Django USER_RETIRE_LMS_MISC
       │
       ├──▶ borra PII en ClickHouse:  user_profile · external_id · auth_user
       │                               (gobernado por ASPECTS_ENABLE_PII)
       │
       └──▶ ❓ tablas de eventos / statements xAPI  ── ¿actor-ifi?
                 • si se BORRA o se ROTA  → la postura de Aspects es defendible, escribirlo así
                 • si se DEJA             → es dato personal pseudonimizado, y hay que decirlo en el contrato
```

**Si se deja, la frase que corresponde en la propuesta no es «cumplimos el art. 17»**, es *«se suprime la
identificación directa y se conserva el registro de actividad pseudonimizado, cuya base legal de retención hay que
declarar»*. Esa frase es defendible; la otra no.

**Paso 2 — verificar que el control de privacidad no esté sorteado.** El **PR #1328** de `tutor-contrib-aspects`
documenta que el *job* manual de *backfill* volcaba `user_profile` / `external_id` a ClickHouse **aun con
`ASPECTS_ENABLE_PII=False`**, *«sorteando exactamente la protección que ese setting existe para dar»*. 🔴 **Está
cerrado sin mergear (2026-09-16).** Entonces: comprobar en la versión del cliente si el *check* de PII está en el
camino manual **además** del automático. **Si no está, el flag no es un control y no se puede escribir como tal en un
expediente.**

**Paso 3 — producir la evidencia, porque el producto no la produce.** Es el mismo trabajo que el paso 2 de **P44** y
es el único desarrollo: envolver la retirada en un servicio propio que **cuente antes y después** —statements del
actor, filas en las tablas de PII— y registre el par *(antes, después, timestamp, operador, id del pedido de
retirement)* en un registro **append-only**. Sobre ClickHouse el conteo se hace con SQL directo contra las tablas de
eventos, que es más fácil que en P44: **la analítica ya está instalada y Superset ya está ahí para mostrarlo.** Ese
registro **es** el expediente del art. 17.

**Paso 4 — empaquetarlo como corrida reproducible (P42), no como PDF.** La auditoría de los pasos 1–3 se escribe como
*eval* sobre **`inspect_ai`** (MIT): dado un usuario de prueba, retirarlo y **afirmar** que las tablas de PII quedaron
vacías y que el identificador de actor hizo lo que el paso 1 determinó. Así el expediente **se vuelve a correr en cada
upgrade de Aspects** en vez de envejecer — y los upgrades de Aspects son frecuentes (2.269 commits).

### Cómo se cotiza

| | Lo que parecía | Lo que corresponde cotizar |
|---|---|---|
| Disparador LMS → telemetría | Desarrollo (como en Moodle) | **Ya existe.** Lectura y verificación del sink |
| Borrado de PII | Desarrollo | **Ya existe y viene encendido.** Verificación |
| Borrado del registro de eventos | Se asumía incluido | 🔴 **NO existe.** Es decisión de retención y **cláusula contractual**, no desarrollo |
| Evidencia | No estaba identificada | **Servicio chico + registro append-only** (igual que P44) |
| Repetibilidad | — | ***Eval* sobre `inspect_ai`** (P42) |

### ⚠️ Lo que este patrón NO promete

- **No borra el registro de aprendizaje, y ésa es la parte que el cliente cree que está comprando.** Aspects conserva
  los eventos. Si el cliente necesita supresión real del registro conductual sobre Open edX, **el stack oficial no la
  da** y hay que discutir arquitectura: migrar la telemetría a **`lrsql`** (Apache-2.0, y entonces es **P44**, que sí
  borra por actor en cascada) o aceptar y declarar la retención. **Esa conversación va al principio del proyecto.**
- **No alcanza al modelo.** Igual que P44: borra registro, no influencia en los pesos. Es el **gap 34**, camino **P38**.
- **No está cerrado el gap 37, y el paso 1 es literalmente ir a cerrarlo.** Esta KB **no verificó de primera mano** qué
  pasa con el identificador del actor: el ADR de PII de Aspects vive en `docs.openedx.org`, bloqueado por el proxy en
  el pase 22. **No presentar la lectura optimista ni la pesimista como hecho verificado** — el paso 1 existe para
  contestarlo sobre la instancia real, que además es la única respuesta que importa.
- **Y la limitación está reconocida por dos proveedores, lo que la vuelve defendible.** El Feature Wiki de **ILIAS**
  declara por escrito que el dato personal **persiste en el LRS** al borrar un objeto xAPI/cmi5 (tendencia **55**), y
  Aspects documenta su retención **en su propia decisión de arquitectura**. **No es una carencia que invente esta KB.**

## P46 — La evidencia de borrado en el LRS, parcheada por backend: el upstream chico que convierte un `200` vacío en un expediente (agregado en el pase 23; **EMEA primero por art. 17, North America por AB 1159, transversal por Anexo III**)

**Qué problema resuelve.** P44 y P45 llegan los dos al mismo muro: se puede *borrar* el dato del alumno en la telemetría,
pero no se puede *probar* qué se borró. `lrsql` responde `{:status 200 :body params}`, que es un eco del `actor-ifi` que
mandó el cliente — **no es prueba de nada** ante un expediente del art. 17 o de **AB 1159** (operativa el **2027-07-01**).
Este patrón es el parche, y el pase 23 lo dimensionó leyendo los tres backends (tendencia **60**).

**Las piezas, todas verificadas de primera mano sobre el árbol clonado (HEAD del 2026-10-01):**

| Pieza | Licencia | Rol |
|---|---|---|
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | **Apache-2.0** ✅ | El LRS a parchear. Apache-2.0 → **el upstream es viable y el fork también** |
| [openfun/ralph](https://github.com/openfun/ralph) | **MIT** ✅ | Alternativa de LRS si el cliente está en Open edX — **pero no tiene `DELETE` en ningún router**, así que acá no aplica: el parche es sobre `lrsql` |
| [openedx/tutor-contrib-aspects](https://github.com/openedx/tutor-contrib-aspects) | **Apache-2.0** ✅ | Quien dispara el borrado aguas arriba (P44/P45) |

**El wiring, y es distinto en cada backend — ésa es la parte que hay que presupuestar:**

1. **Encender la ruta.** `LRSQL_ENABLE_ADMIN_DELETE_ACTOR=true`. Viene en `false`, y apagada el síntoma es **404, no 403**
   (`src/main/lrsql/admin/routes.clj:407`). Sin esto no hay nada que parchear.
2. **SQLite — recoger los siete conteos que ya se calculan.** En
   `src/db/sqlite/lrsql/sqlite/record.clj:169–176` las siete queries se invocan como expresiones sueltas y Clojure
   devuelve sólo la séptima. Envolver en `let`, bindear las siete y devolver un mapa por tabla
   (`{:statement-to-statement n :statement-to-activity n :attachment n :xapi-statement n :agent-profile-document n
   :state-document n :actor n}`). **~8 líneas, el dato ya está: sólo se está tirando.**
3. **PostgreSQL / MariaDB — partir el SQL antes de poder recoger nada.** En los dos,
   `delete-actor-and-dependents!` es **un** nombre HugSQL con **siete `DELETE` adentro**, así que hay un solo número
   disponible. Para obtener el desglose hay que **partirlo en siete queries con nombre**, como SQLite ya las tiene, y
   después aplicar el paso 2. **Es refactor de SQL, no plomería.**
4. **Devolver el conteo en vez del eco.** En `src/main/lrsql/admin/interceptors/lrs_management.clj:23–33`, el cuerpo es
   `(adp/-delete-actor lrs params)` **como expresión suelta cuyo retorno se descarta**, y la respuesta es
   `{:status 200 :body params}`. Bindear ese retorno y devolverlo junto al `actor-ifi`, el timestamp y el admin que
   ejecutó.
5. **Persistir el expediente fuera del LRS.** El conteo en la respuesta HTTP se pierde con la sesión: escribirlo en una
   tabla de auditoría propia (o en el `llm_calls`-style de la aplicación) con `actor-ifi` **hasheado**, timestamp, admin,
   backend y el mapa de conteos. Eso es lo que se adjunta al expediente.

**Estimación:** 2–3 semanas incluyendo el *upstream* de los pasos 2–4 (Apache-2.0, cambio chico, sin dependencias nuevas).
Si el cliente no quiere esperar el *merge*, el fork es legal y el *rebase* es barato porque el cambio toca 4 archivos.

🔴 **Lo que hay que decir en la propuesta, y es incómodo pero es el hallazgo del pase.** La ventaja que esta KB le vende a
`lrsql` —*«corre sobre la base de datos que el cliente ya opera»*— **no se extiende a la evidencia**. Un despliegue sobre
SQLite llega al desglose de siete tablas con ~8 líneas; **el mismo producto sobre PostgreSQL no pasa de un número sin tocar
el SQL.** Cuando el alcance incluya prueba de supresión, **el motor de base de datos es una decisión de cumplimiento, no de
infraestructura**: hay que preguntarlo en el *discovery*.

> 🔴 **SUPERADO POR EL PASE 24 (2026-10-01) — este patrón queda reemplazado por P47, y la advertencia de abajo ya
> está contestada.** Se midió ejecutando: el driver **no** entrega un solo valor por limitación del SQL — entrega
> **los siete conteos en orden** (`[7, 2, 3, 8, 5, 6, 1]`) por el bucle `getMoreResults()` de JDBC estándar, así que
> **no hay que partir el SQL** y el parche del gap 36 es más chico que lo estimado acá. El número que hoy se ve es el
> del **primer** `DELETE`, y vale **`0`** para el alumno sin sub-sentencias. Y apareció el **gap 38**: en MariaDB/MySQL
> el borrado **falla entero** si `allowMultiQueries` quedó apagado. **Usar P47**, que incluye el paso 0 de verificación.
> Se conserva este patrón por su cadena de razonamiento y por las coordenadas del parche, que siguen siendo válidas.

⚠️ **Lo que no está medido, y no se infiere.** Cuál de los siete `DELETE` reporta el driver JDBC en el `:execute`
multi-sentencia de PostgreSQL/MariaDB (el primero, el último o la suma) **no se verificó ejecutando**. La lectura del código
prueba que hay **un solo valor disponible**, que es lo que sostiene el patrón; el valor exacto es la acción que el pase 23
deja escrita: levantar `lrsql` sobre PostgreSQL, borrar un actor con datos en las siete tablas y leerlo.

- **No alcanza al modelo.** Igual que P44 y P45: esto audita el registro, no la influencia en los pesos. Sigue siendo el
  **gap 34**, camino **P38**.

---

## P47 — El expediente de supresión del LRS con el desglose que ya está en el cable, y la verificación de que el borrado puede ocurrir (agregado en el pase 24; **EMEA primero por art. 17, North America por AB 1159, transversal por Anexo III**)

**Este patrón reemplaza la estimación de P46, no la contradice en su objetivo.** P46 se escribió sobre la lectura del pase
23 —que el desglose por tabla exigía partir el SQL— y sobre una incógnita declarada: *cuál* de los siete `DELETE` reporta el
driver. **El pase 24 lo midió y las dos cosas cambian:** el desglose **ya vuelve completo** por JDBC estándar, y el número
que hoy se ve es el del **primer** `DELETE`, que vale **`0`** para el alumno típico. P47 es P46 con la plomería medida, más
una verificación previa que P46 no tenía porque nadie sabía que hacía falta.

### Paso 0 — la verificación que va antes de todo lo demás, y que puede cancelar el resto (gap 38)

🔴 **Antes de prometer un expediente de supresión sobre `lrsql` con MariaDB o MySQL, hay que comprobar que el borrado
puede siquiera ejecutarse.** Medido en el pase 24: con `allowMultiQueries` en el default del driver (`false`),
`delete-actor-and-dependents!` **falla entera** con error **1064 / SQLState 42000**. Y lrsql trae el parámetro sólo como
*fallback* de aero, así que **cualquier** uso de `LRSQL_DB_PROPERTIES` —o de `LRSQL_DB_JDBC_URL`— lo apaga en silencio.

| Qué preguntar en el *discovery* | Por qué | Qué hacer si la respuesta es la mala |
|---|---|---|
| ¿El backend es MariaDB o MySQL? | Si es PostgreSQL o SQLite, el paso 0 no aplica | Seguir al paso 1 |
| ¿Está definida `LRSQL_DB_PROPERTIES`? | Si está, **reemplazó** el default y `allowMultiQueries=true` ya no está | Re-agregarlo **al string del operador**, no en vez de él: `allowMultiQueries=true&<lo-que-ya-tenía>` |
| ¿Está definida `LRSQL_DB_JDBC_URL`? | Override total de las propiedades | Agregar `allowMultiQueries=true` a la query de la URL |
| ¿Hay un test que pruebe un borrado de actor de punta a punta? | **No existe en el proyecto** | Es el primer entregable: el test de regresión que detecta el apagón de configuración |

**Entregable del paso 0, y es media jornada:** un *preflight* que corre contra el despliegue del cliente, borra un actor
sintético con filas en las siete tablas y falla ruidosamente si el resultado no es el esperado. **Eso solo ya vale como
venta chica**, porque convierte un fallo que aparece el día del expediente en un fallo que aparece en CI.

### Paso 1 — recoger el desglose entero, que es la corrección a P46

**No hay que partir el SQL.** Medido sobre PostgreSQL 16.14 + pgjdbc 42.7.4 y MariaDB 10.11.14 + Connector/J 3.4.1, con el
DDL y el SQL propios de lrsql: el driver parte la cadena multi-sentencia y entrega **los siete conteos en el orden de los
siete `DELETE`**.

| | |
|---|---|
| **Lo que hay hoy** | un conteo: el del **primer** `DELETE` (`statement_to_statement`) |
| **Lo que ya está disponible** | `[st2st, st2activ, attachment, xapi_statement, agent_profile, state_document, actor]` — medido: `[7, 2, 3, 8, 5, 6, 1]` |
| **Dónde está el parche** | en la capa que **recoge** el resultado, no en el SQL ni en el driver: hay que drenar `getMoreResults()` en vez de leer un conteo |
| **Qué NO hay que hacer** | cablear el conteo único «porque ya está». **Vale `0` para el alumno sin sub-sentencias** — 25 filas borradas, el expediente diría `0` |

🔴 **La trampa, escrita para que no se repita:** un expediente que afirma «0 filas borradas» sobre una supresión exitosa es
**peor** que el `200` vacío que el pase 21 denunció. El `200` vacío no afirma nada; el `0` afirma algo falso y es
exactamente lo que un auditor usa para decir que el borrado no ocurrió.

### Paso 2 — contar aparte lo que se va en cascada, porque no aparece en ningún conteo

`statement_to_actor` —**la tabla que vincula al alumno con su rastro**— no la borra ninguno de los siete `DELETE`. Se va
sólo por `ON DELETE CASCADE` desde `xapi_statement`, y **las filas en cascada no se cuentan en ningún *update count* de
JDBC**. En el fixture del pase 24 eran **10 filas** y ninguna medición las vio.

| Motor | De dónde sale la cascada | Qué verificar en el despliegue |
|---|---|---|
| **MariaDB** | Nativa en la tabla (`statement_fk_stactor`) | `information_schema.referential_constraints` → `delete_rule = CASCADE` |
| **PostgreSQL** | **Por migración** (`add-statement-to-actor-cascading-delete!`) | `pg_constraint` → que `statement_fk` diga `ON DELETE CASCADE`. **En un despliegue viejo sin migrar no está** |

**Entonces el expediente honesto hace una de dos cosas:** un `SELECT count(*)` sobre `statement_to_actor` **antes** del
borrado y lo declara como línea propia, o dice explícitamente que ese número no se cuenta. Las dos son defendibles; omitirlo
sin decirlo, no.

### El stack, nombrado

| Pieza | Repo | Licencia | Rol |
|---|---|---|---|
| LRS | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** ✅ | El almacén y el sitio de los tres parches |
| Transformación LMS → xAPI | [`openedx/event-routing-backends`](https://github.com/openedx/event-routing-backends) | **Apache-2.0** ✅ | De donde viene el dato (ver **P45**) |
| Disparador del lado LMS | [`openedx/platform-plugin-aspects`](https://github.com/openedx/platform-plugin-aspects) | **Apache-2.0** ✅ | `UserRetirementSink` — el evento que inicia la cadena |
| Orquestación del expediente | [`temporalio/temporal`](https://github.com/temporalio/temporal) | **MIT** ✅ | Durabilidad y reintento del flujo de supresión (ver **P40**) |
| Conformidad como corrida | [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) | **MIT** ✅ | El expediente como corrida reproducible (ver **P42**) |

### Plazo y alcance

| | |
|---|---|
| **Paso 0 (preflight + test de regresión)** | **0,5–1 semana.** Es la venta más chica de esta KB y la más defendible: evita un fallo de cumplimiento, no agrega una capacidad |
| **Paso 1 (drenar los siete conteos)** | **1–2 semanas** incluyendo el *upstream* a Yet Analytics. Baja respecto de P46 porque no hay refactor de SQL |
| **Paso 2 (cascada declarada)** | **0,5 semana** |
| **Expediente completo sobre un despliegue existente** | **4–6 semanas**, encadenado con **P45** si el LMS es Open edX |

### Advertencias

- **No alcanza al modelo.** Igual que P44, P45 y P46: esto audita el registro, no la influencia en los pesos. Sigue siendo
  el **gap 34**, camino **P38**.
- **Un eslabón sigue inferido.** Qué devuelve exactamente `next.jdbc` con `:result :affected` no se midió —`repo.clojars.org`
  responde **403** por el proxy de egreso— así que **dónde** vive el parche del paso 1 (adaptador de HugSQL, `next.jdbc` o el
  interceptor de lrsql) hay que confirmarlo antes de presupuestar el *upstream*. Que el desglose **esté disponible** sí está
  medido, y es lo que sostiene el patrón.
- **El *blast radius* del gap 38 no está enumerado.** Que el borrado de actor sea la única consulta multi-sentencia del
  producto es lo que se desprende de cuatro pases de lectura, pero no se contó. Si hubiera otras, el paso 0 es más urgente,
  no menos.

---

## P48 — Del acervo de ítems viejo a la aserción de competencia, todo permisivo: migración QTI → banco → entrega certificada → evidencia xAPI → competencia en CaSS (agregado en el pase 25; **North America primero por acervo instalado, transversal por licencia**)

**Qué resuelve, en los términos en que el cliente lo pide:** *«tenemos veinte años de ítems en QTI 2.1, queremos práctica
adaptativa y queremos poder decir qué sabe cada alumno»*. Hasta el pase 24 esta KB **no podía armar esta cadena completa**:
le faltaban el banco de ítems, la migración y la pieza de aserción. **Las tres aparecieron este pase, y las tres son
permisivas.**

### Las piezas, todas verificadas de primera mano el 2026-10-01

| Rol en la cadena | Repo | Licencia | ★ | Nota decisiva |
|---|---|---|---|---|
| **Migración + banco + autoría** | https://github.com/LongsightGroup/qti3 | **MIT** ✅ | 5 | 12 paquetes, 667 commits. **Migra QTI 1.2 y QTI 2.x → autoría QTI 3** y escribe **paquete de banco de ítems**. 🚫 **No certificado**, lo dice su README |
| **Entrega al candidato** | https://github.com/amp-up-io/qti3-item-player | **MIT** ✅ | **30** | ✅ **Certificado 1EdTech: QTI 3 Basic *y* Advanced «Delivery»**. Sólo entrega — no autoría, no banco |
| **Entrada al LMS** | https://github.com/Cvmcosta/ltijs | **Apache-2.0** ✅ | **373** | Node/TS. Launches, Deep Linking, **AGS** (devolver notas), NRPS, Dynamic Registration. **La más traccionada de su capa** |
| *(alternativa por stack)* | `UOC/spring-boot-lti-advantage` (MIT, Java) · `dmitry-viskov/pylti1.3` (MIT, 138 ★, Python) · `1EdTech/lti-1-3-php-library` (Apache-2.0, 124 ★, PHP) | ✅ | — | **Elegir por el stack del cliente, no por el de esta KB** (es el sesgo que corrigió el pase 25) |
| **Telemetría** | `yetanalytics/lrsql` *(ya en la KB)* | **Apache-2.0** ✅ | — | LRS xAPI. ⚠️ **Leer antes el paso 0 de P47** si va con MariaDB/MySQL (gap 38) |
| **Minimización de telemetría** | https://github.com/yetanalytics/xapipe | **Apache-2.0** ✅ | 17 | *LRSPipe*. **Filtra por *statement template* y por *pattern* de un xAPI Profile**: decide qué sale y qué no |
| **Perfil xAPI** | https://github.com/adlnet/xapi-profiles | **Apache-2.0** ✅ | 60 | La especificación. Grupo **IEEE p9274.2.1** activo |
| **Aserción de competencia** | https://github.com/cassproject/CASS | **Apache-2.0** ✅ | **62** | Marcos + **aserciones de logro** + perfil del aprendiz. Cartuchos **IMS CASE**, **xAPI**, **Open Badges 2.0** y 🔵 **MCP** |
| **Modelo de qué sabe el alumno** | `pykt-team/pykt-toolkit` *(ya en la KB)* | **MIT** ✅ | 441 | *Knowledge tracing* profundo, para elegir el próximo ítem |

### El wiring, en cinco pasos, y sólo dos son desarrollo

1. **Migrar e inventariar (`LongsightGroup/qti3`).** Correr el paquete de migración sobre el acervo QTI 1.2/2.x y escribir el **paquete de banco de ítems**. Salida: ítems QTI 3 de autoría, con *«typed diagnostics»* — o sea, **el inventario de lo que no migró limpio es parte del entregable**, y eso es lo que se le reporta al cliente por volumen.
2. **Entregar con la pieza certificada (`amp-up-io/qti3-item-player`).** El banco alimenta al *player* certificado. ⚠️ **Esta separación es el núcleo del patrón y va escrita en la propuesta:** el sello de 1EdTech cubre **la entrega**, que es lo que el cliente audita; la autoría y el banco van con la pieza no certificada. Prometer *«todo certificado»* es falso.
3. **Montar como *tool* LTI (`ltijs`).** *Launch* OIDC desde el LMS del cliente, y **las notas vuelven por AGS** al *gradebook* — sin exportaciones manuales. Es configuración más pegamento, no desarrollo de plataforma.
4. **Drenar evidencia de proceso a xAPI, filtrada (`lrsql` + `xapipe`).** Las interacciones con el ítem salen como sentencias xAPI; **`xapipe` filtra por el *statement template* del perfil** antes de que lleguen al LRS de largo plazo. **Esto es minimización por construcción**, no una política escrita: lo que el perfil no contempla, no viaja.
5. **Asertar la competencia (`CaSS`).** El resultado del ítem se convierte en **aserción de logro** contra el marco de competencias por el cartucho **xAPI** o **IMS CASE**, y queda disponible como **Open Badges 2.0**. 🔵 **Y por el cartucho MCP, un tutor de `agents/top.md` lee el marco y escribe la aserción sin adaptador propio** (⚠️ ver la advertencia del gap 40).

**Los dos pasos que son desarrollo real son el 1 y el 5** —la limpieza del acervo migrado y el mapeo ítem→competencia—.
Los pasos 2, 3 y 4 son integración de piezas que ya hacen lo que hace falta.

### Dónde se vende primero

| Región | Gancho |
|---|---|
| **North America** | **El acervo instalado y el costo de salida del proveedor de assessment.** El estándar curricular ya está (`commonstandardsproject/api`, 50 estados; **Ed-Fi**, Apache-2.0). Cotizable **por volumen de ítems**, unidad que el cliente ya cuenta |
| **EMEA** | Como pieza de **P49**: integridad sin proctoring. Y el marco de competencias puede anclarse a la ontología de Oak (`oak-curriculum-ontology`, 50.948 *key learning points*) |
| **LATAM** | Entra por **gobernanza**: el 45 % de las instituciones de LAC con guía formal de AI (vs. 70 % en Europa y North America) necesita **resultado medible**, y la aserción de competencia es exactamente eso |
| **APAC** | ⚠️ **Con cuidado:** evaluación y aprendizaje adaptativo están alcanzados por el **AI Basic Act** coreano (vigente 2026-01-22) y por el **Annex III** europeo. Ir con el expediente de **P42** desde el día uno |

### Plazo y alcance

| | |
|---|---|
| **Piloto (un curso, un marco, sin migración)** | **4–6 semanas** |
| **Migración de acervo** | **depende del volumen**, y se cotiza por ítem: el *diagnostics* tipado del paso 1 da la curva real tras la primera tanda |
| **Cadena completa con aserción y badges** | **10–14 semanas** |

### ⚠️ Lo que este patrón NO promete

- **La certificación no cubre la cadena, cubre la entrega.** Dicho arriba, repetido acá porque es el error fácil.
- **El cartucho MCP está declarado, no medido** (**gap 40**). El paso 5 funciona igual por xAPI o IMS CASE; **lo que no se puede prometer todavía es el *«sin adaptador»***.
- **`LongsightGroup/qti3` tiene 5 ★.** La tracción es baja; lo que sostiene la elección son **667 commits y 12 paquetes publicados**, y que **es el único camino open source desde QTI viejo**. Si el cliente exige respaldo comercial, esto es un riesgo que se declara.
- **No incluye proctoring**, y es deliberado: ver **P49** y la tendencia **64**.

---

## P49 — Integridad de examen sin AI de vigilancia: sacar el entregable del Annex III en vez de buscar la pieza que no existe (agregado en el pase 25; **EMEA primero por Annex III, APAC por el AI Basic Act coreano, transversal por licencia**)

**El patrón empieza con un «no».** Cuando el cliente pide *«proctoring con AI»*, la respuesta correcta no es buscar la
pieza: **este pase barrió la capa entera y no existe ninguna opción open source permisiva y productiva** (tendencia
**64**). Y el *proctoring* es **la única función educativa que el Annex III del EU AI Act nombra explícitamente** como
alto riesgo (aplicable **2027-12-02**); Corea del Sur ya la alcanza como *high-impact AI* desde el **2026-01-22**.

### Lo que hay, y por qué ninguna sirve

| Pieza | Licencia | ★ | Por qué se descarta |
|---|---|---|---|
| `vardanagarwal/Proctoring-AI` | **MIT** ✅ | **635** | 🔴 **Pesos de uso no comercial** (*facial landmarks*), por su propio README. Código permisivo, modelo no. Y es demo de investigación |
| `openedx/edx-proctoring` | ⚠️ AGPL-3.0 | 68 | Copyleft fuerte: inviable para un SaaS multicliente |
| `oat-sa/lib-lti1p3-core` | ⚠️ GPL-2.0 | 37 | **La única certificada en *LTI 1.3 Proctoring Services*** — y copyleft |
| `sudosylabs/Proctor` | ⚠️ AGPL-3.0 | 0 | *«has not published a supported production release»* |
| `kamlendras/OpenProctor` | ⚠️ AGPL-3.0 | 15 | 37 commits, sin releases |

### El wiring de la alternativa, en cuatro pasos

1. **Variabilizar el ítem en vez de vigilar al candidato (`LongsightGroup/qti3`, MIT).** Usar el ***writer* de banco de ítems** para generar **familias de variantes** del mismo ítem y **aleatorizar por candidato**. El fraude por copia entre pares se vuelve ineficaz **sin mirar a nadie por la cámara**.
2. **Entregar con la pieza certificada (`amp-up-io/qti3-item-player`, MIT, certificada «Delivery»),** con límite de tiempo y navegación controlada por la propia especificación QTI 3.
3. **Devolver notas por AGS (`ltijs`, Apache-2.0, 373 ★)** al *gradebook* del LMS: la traza de calificación queda en el sistema de registro del cliente, no en una herramienta aparte.
4. **Evidencia de proceso en xAPI, minimizada (`lrsql` + `yetanalytics/xapipe`, los dos Apache-2.0).** Secuencia de respuestas, tiempos por ítem y revisiones — **filtrado por *statement template* del perfil**, así que **no se recoge biometría ni video**: no hay dato de categoría especial que custodiar, porque no se capturó.

### Por qué es mejor negocio que el proctoring que el cliente pidió

| | Proctoring con AI | P49 |
|---|---|---|
| **Clasificación EU AI Act** | 🔴 **Annex III, alto riesgo** (2027-12-02): expediente, evaluación de impacto, auditoría | ✅ **Fuera del Annex III** — no hay inferencia sobre la persona |
| **Dato tratado** | Rostro, mirada, voz, ambiente — **categoría especial**, y de **menores** en K-12 | Respuestas, tiempos y secuencia: dato académico |
| **Licencia disponible** | AGPL/GPL o pesos no comerciales | **MIT y Apache-2.0 de punta a punta** |
| **Lo que se discute con el cliente** | Falsos positivos, sesgo, reclamos, prensa | Diseño de la evaluación |

🔵 **El argumento de venta, en una línea:** *«no le instalamos vigilancia: le rediseñamos el examen para que la vigilancia
no sea necesaria — y le sacamos el proyecto del Anexo III de paso»*. En EMEA el ahorro es **regulatorio y cuantificable**;
en las otras regiones se vende por **licencia y por costo**.

### Plazo y alcance

| | |
|---|---|
| **Diagnóstico de integridad + diseño de variantes sobre un examen real** | **2–3 semanas** |
| **Implementación completa (banco variabilizado + entrega + AGS + xAPI filtrado)** | **8–10 semanas** |
| **Encadenado con P48** | Comparte los pasos 1-4: si el cliente ya va a P48, **P49 es incremental** |

### ⚠️ Lo que este patrón NO promete

- **No elimina el fraude, cambia su economía.** Un candidato con ayuda externa presencial no es detectado. **Lo que elimina es la copia escalable** — y eso hay que decirlo, porque un cliente que necesite certificación de alto riesgo (habilitaciones profesionales, exámenes de estado) **probablemente siga necesitando proctoring supervisado**, y entonces la respuesta honesta es un proveedor comercial cerrado, no open source.
- **La aleatorización por variantes no está medida en esta KB.** Que `LongsightGroup/qti3` escriba paquetes de banco de ítems está **verificado**; que su *writer* soporte el patrón de familias de variantes que pide el paso 1 **está inferido de la descripción de los paquetes**, no probado. **Es el gap 39.**
- **La equivalencia psicométrica entre variantes es trabajo propio** y no lo cubre ninguna pieza de esta tabla: si las variantes no son de dificultad equivalente, la nota deja de ser comparable. Para un examen de consecuencia alta, eso requiere análisis de ítems que esta cadena no incluye.

## P50 — Perfil de competencia por MCP, con las tools medidas (pase 26)

**Problema que resuelve.** Un cliente con un acervo de cursos quiere responder, por alumno, *«¿qué sabe esta persona?»*
— no *«¿qué cursos aprobó?»*. Es la pregunta que paga un proyecto de competencias, y hasta el pase 25 esta KB la
describía sin tener con qué ejecutarla: la capa CASE hospeda marcos y **no registra logro**.

**Qué cambia respecto de P48.** P48 tenía el paso 4 **inferido de una línea de README**. **Este pase lo midió:** el
cartucho MCP de CaSS genera **6 tools y 3 resource templates** (51 paths en el spec, 0 errores de validación), y dos de
ellas son exactamente los extremos de la cadena. **P50 es P48 con el paso 4 verificado y cotizable.**

**Piezas, todas verificadas y todas permisivas:**

| Pieza | Licencia | Rol |
|------|----------|-----|
| `cassproject/CASS` | **Apache-2.0** ✅ | Marcos de competencia + **aserciones de logro** + cómputo de perfil. **Expone MCP en `/api/mcp`** |
| `DavidLMS/learnmcp-xapi` | **MIT** ✅ | Puente MCP hacia el LRS: registra statements y consulta progreso |
| `yetanalytics/lrsql` | **Apache-2.0** ✅ | El LRS de almacenamiento (xAPI 2.0 / IEEE 9274.1.1) |
| `vishalsachdev/canvas-mcp` | **MIT** ✅ | Si el cliente es Canvas: trae la actividad real (entregas, notas, módulos) |

**Wiring, con los nombres de tool medidos:**

```
Actividad del alumno (Canvas vía canvas-mcp  |  o el LMS del cliente)
        │
        ▼
  [Agente orquestador]  ── record_evidence ──▶  CaSS   POST /api/xapi/statement
        │                  (xAPI statement: actor + verb + competencia)
        │
        ├── learnmcp-xapi ─▶ lrsql        (historial crudo, consulta de progreso)
        │
        ▼
  get_learner_profile ──▶ CaSS   GET /api/profile/latest
        (frameworkId, subject, targetDateTime)  ──▶  perfil de competencia computado
```

**Las dos llamadas que cierran el patrón, con su firma real:**

- `record_evidence` → `POST /api/xapi/statement`, requiere `body`. `readOnlyHint: false`.
- `get_learner_profile` → `GET /api/profile/latest`, parámetros `frameworkId`, `subject`, `flushCache`, `cache`,
  `targetDateTime`. `readOnlyHint: true`, `idempotentHint: true` → **se puede cachear y reintentar sin efectos**.

**`targetDateTime` es el parámetro que hay que vender.** Permite preguntar *«¿qué sabía esta persona en tal fecha?»* —
es decir, **el perfil es histórico, no sólo actual**. Eso habilita el entregable que un área de RRHH o una acreditadora
pide y que casi ningún producto da: *la evolución de la competencia en el tiempo*, con evidencia trazable detrás.

🔴 **Las dos restricciones de cotización, y no son menores:**

1. **Por MCP se escribe un statement por llamada.** `POST /api/xapi/statements` (el *bulk*) está **`x-mcp-ignore`**, como
   otros 44 paths. **No cotizar ingestión masiva de telemetría por esta puerta**: para lotes, API REST por fuera de MCP.
   Ver el **gap 41**.
2. **El *handshake* MCP real no está medido.** Se midió la **generación** de las tools (determinista, y confirmada por
   tres fuentes independientes), no su **invocación**: eso necesita Elasticsearch. **Antes de firmar, hacer
   `initialize` + `tools/list` contra `/api/mcp`** — es la acción 1 del pase 27. Estimación: una tarde con Docker.

**Estimación.** 3–4 semanas para el circuito completo sobre un marco de competencias existente, asumiendo que el LMS ya
expone la actividad. El riesgo no es técnico: es **tener el marco de competencias del cliente en CASE**, que suele ser
el trabajo de verdad.

## P51 — ~~El conector MCP de Moodle que no existe, construido sobre el que sí existe~~ 🔴 **PREMISA FALSA — CORREGIDO EN EL PASE 27** (pase 26)

> 🔴 **Este patrón se construyó sobre una afirmación falsa y queda reemplazado por P54 y P55.** El pase 26 declaró que *«el único conector MCP de Moodle es `csmediapro/moodle-mcp-server`, AGPL-3.0, 10 tools sólo de lectura»*. **Existen al menos tres, y dos son MIT:** `peancor/moodle-mcp-server` (**MIT**, 43 ★, 13 forks, **8 tools, cuatro de escritura**, incluidas `provide_assignment_feedback` y `provide_quiz_feedback`) y `MarcosNahuel/moodle-mcp` (**MIT**, 59 commits, **40 tools** en 10 dominios **+ `ws_raw`**). El error fue de **muestreo** —los directorios de MCP rankean por promoción, **gap 49**—, no de lectura: lo que el pase 26 dijo de `csmediapro` es correcto.
>
> **Qué hacer en su lugar:** para Moodle, **no hay que construir el conector — hay que endurecer y componer los dos que existen**, que es un proyecto mucho más corto: ver **P54** (corrección y devolución con compuerta humana). La ausencia real del eje conector **está en Open edX** (**gap 48**): ver **P55**.
>
> **Lo que de este patrón sigue siendo válido y por eso se conserva entero abajo:** la tabla de decisiones de diseño de `canvas-mcp` —descubrimiento de tools, separación de perfiles, *agent skills*, chequeo WCAG— **es exactamente lo que hay que portar**, y ahora se porta a Open edX en vez de a Moodle. ⚠️ Con una salvedad de cifra: el conteo de tools de `canvas-mcp` **varía por versión** (40+, 80+, 116) y **no es citable como número fijo**; «102–103» era la lectura del README en el pase 26.

**El hueco, medido.** `canvas-mcp` (**MIT**, 269 ★, 815 commits) da **hasta 102–103 tools** sobre Canvas, con lado
alumno y lado docente. **Para Moodle —el LMS más instalado del planeta— el único conector MCP es `csmediapro/moodle-mcp-server`:
AGPL-3.0, 0 ★, 0 forks, 10 tools sólo de lectura, y las capas útiles (*Reporting*, *Analytics*, *Directory*,
*Compliance*) son plugins premium que se venden aparte.** Ver el **gap 43**.

**Por qué es patrón y no sólo oportunidad: `canvas-mcp` ya resolvió los problemas de diseño.** No hay que inventar la
arquitectura, hay que portarla:

| Decisión de diseño de `canvas-mcp` | Por qué importa al portarla a Moodle |
|-----------------------------------|--------------------------------------|
| **`search_canvas_tools`** — descubrimiento de tools | Con 100+ tools **no se puede volcar el catálogo al contexto**. El agente busca la herramienta. Moodle Web Services tiene **cientos** de funciones: sin esto, el conector es inusable |
| **Separación alumno / docente / *learning designer*** | Son tres perfiles con permisos distintos. Moodle tiene *capabilities* por rol: el mapeo es directo |
| **8 *agent skills* además de las tools** | Las tareas compuestas (corregir una tanda, armar un módulo) no son una tool: son un procedimiento |
| ***Learning Designer*** con **chequeo WCAG** | Conecta con la capa de accesibilidad del pase 8 y con el **EAA** (vigente 2025-06-28). Es el diferenciador regulatorio en EMEA |

**Wiring:**

```
[Agente]  ──MCP──▶  moodle-mcp (a construir, licencia a elegir)
                        │
                        ▼
                Moodle Web Services (REST/token)   ◀── sin modificar el LMS
                        │
                        ├── core_course_*, core_enrol_*, mod_assign_*, gradereport_*
                        └── capabilities por rol → perfiles alumno / docente

  Opcional, y es el combo que esta KB recomienda:
  [Agente] ──MCP──▶ learnmcp-xapi ──▶ lrsql     (telemetría conforme al estándar)
  [Agente] ──MCP──▶ CaSS                        (competencia, P50)
```

⚠️ **La decisión de licencia hay que tomarla a conciencia, y es la trampa del patrón.** **El core de Moodle es GPL-3.0**,
pero **un conector que habla con Moodle Web Services por HTTP no es obra derivada de Moodle**: es un cliente de su API.
**Se puede licenciar permisivo.** Lo que **no** se puede es forkear `moodle-mcp-server` (AGPL-3.0) y relicenciar. **El
camino limpio es construir desde cero contra la API documentada**, tomando de `canvas-mcp` (MIT) las decisiones de
diseño —que es legítimo— y no su código si no se respeta el MIT (que es trivial de respetar: atribución).

**Estimación.** 4–6 semanas para un conector de ~30 tools útiles con descubrimiento. **El valor no está en el número de
tools: está en `search_canvas_tools`** — sin descubrimiento, un conector de Moodle es un catálogo que no entra en el
contexto.

## P52 — La capa agéntica de biblioteca sobre el bus de eventos que ya está puesto (pase 26)

**La vertical que esta KB abrió en el pase 26 y que no tiene ni una pieza agéntica.** Y es la más fácil de todas las que
inventarió esta base, por un motivo concreto: **FOLIO ya publica los eventos.**

| Pieza | Licencia | Rol |
|------|----------|-----|
| `folio-org/platform-complete` | **Apache-2.0** ✅ | Ensamblado de la plataforma: fija el conjunto compatible de releases + infra Docker |
| `folio-org/mod-inventory` | **Apache-2.0** ✅ | *Instances* / *holdings* / *items*, **import por Kafka**, **MARC**, *authority linking*, **multi-tenant** |
| `DavidLMS/learnmcp-xapi` + `lrsql` | **MIT** / **Apache-2.0** ✅ | Si se quiere registrar el uso como evidencia de aprendizaje |

**Wiring — y el punto es que no se parchea nada:**

```
FOLIO (Apache-2.0, multi-tenant)
   │
   ├── mod-inventory ──Kafka──▶  [consumidor agéntico]   ◀── NO se parchea el core
   │                                   │
   │                                   ├─ recomendación por curso/competencia
   │                                   ├─ enriquecimiento de catálogo (MARC → lenguaje natural)
   │                                   └─ descubrimiento conversacional sobre el OPAC
   │
   └── API HTTP por tenant ──▶ lectura de holdings/items
                                        │
                     opcional ──────────▼
                        learnmcp-xapi ──▶ lrsql  (el préstamo como statement xAPI)
```

**Por qué el modelo de despliegue de FOLIO es la mitad del valor.** Es **modular y multi-tenant por diseño**: el módulo
agéntico se despliega **al lado**, consume Kafka y expone su propia API, **sin tocar el core y sin bloquear upgrades**.
Es la diferencia con Koha (**GPL-3.0+**, Perl, monolítico), donde la capa AI va necesariamente por fuera contra la
interfaz y hay que leer la GPL antes de tocar algo.

⚠️ **La advertencia de lectura que hay que poner en la propuesta.** `platform-complete` tiene **15 ★** y `mod-inventory`
**4 ★**. **No aplicar el umbral de estrellas:** son 3.096 y 2.402 commits, 27 y 15 forks, y un consorcio de bibliotecas
universitarias detrás. **Para software de consorcio las estrellas miden moda; los commits y las implantaciones miden
vida.** Mismo patrón que Apereo y `UniTime`.

**Regla de decisión.** Cliente **con Koha** → capa AI por fuera, GPL leída. Cliente **eligiendo o migrando** → **FOLIO**,
por la licencia **y** por el bus. **Estimación:** 3 semanas para el consumidor de Kafka + descubrimiento conversacional
sobre un tenant de prueba. Ver el **gap 45**.

## P53 — *Early warning* con humano decidiendo: el único envoltorio facturable de la capa predictiva (pase 26)

**El problema de forma, y es el patrón más importante de este pase.** La capa de *student success* open source es de
**2013–2014**, es **GPL**, y no vive en GitHub (**gap 47**). Y es **la que más presión regulatoria tiene encima**: el
**Annex III** del EU AI Act la clasifica de alto riesgo, **Oklahoma y Maryland prohíben la decisión autónoma sobre el
alumno**, **Delaware y Nueva York** prohíben el IEP automatizado, y **Colorado y Texas** agregaron requisitos. **Seis
estados y un reglamento europeo sobre una capa cuyo software libre tiene doce años.**

🔴 **La trampa que este patrón evita, dicha sin suavizar.** *La misma pieza técnica tiene dos envoltorios, y sólo uno se
puede facturar.* Un modelo que predice riesgo de abandono y **dispara una acción** —baja de curso, reasignación, alerta
automática al tutor con recomendación— **es ilegal en dos estados y de alto riesgo en EMEA**. El mismo modelo que
**ordena una cola de revisión humana** no cae en la prohibición de decisión autónoma. **No es un matiz de redacción: es
la diferencia entre un entregable y un pasivo.**

**Piezas (y hay que decir que la de modelado es permisiva y la de producto no existe):**

| Pieza | Licencia | Rol |
|------|----------|-----|
| `pykt-team/pykt-toolkit` / `pyBKT` | **MIT** ✅ | El modelado del alumno. **Permisivo** — pero ⚠️ **verificar la licencia de los *datasets*** (casi todos **CC BY-NC**, ver gap 11) |
| `lrsql` + `learnmcp-xapi` | **Apache-2.0** / **MIT** ✅ | La telemetría conforme al estándar que alimenta el modelo |
| Capa de producto (*early alert*, cola, expediente) | 🔴 **no existe permisiva** | **FlightPath** es GPLv3+ de 2013 y sin repo en GitHub. **Esto es el desarrollo** |

**Wiring — y el recuadro del medio es el patrón:**

```
LMS / SIS  ──▶  lrsql (xAPI)  ──▶  pyKT / pyBKT   ──▶  score de riesgo
                                                            │
                                   ┌────────────────────────▼─────────────────────────┐
                                   │  COLA DE REVISIÓN HUMANA                         │
                                   │  · ordena por riesgo, NO actúa                   │
                                   │  · muestra los features que pesaron              │
                                   │  · exige decisión de un tutor identificado       │
                                   │  · escribe expediente: quién, cuándo, por qué    │
                                   └────────────────────────┬─────────────────────────┘
                                                            ▼
                                            intervención (humana) + statement xAPI
```

**Las cuatro propiedades que hacen al entregable defendible en las cuatro regiones**, y conviene listarlas así en la
propuesta: **(1)** el sistema **ordena**, no decide; **(2)** la decisión la toma **una persona identificada**;
**(3)** el alumno puede saber **qué features pesaron** (explicabilidad, que es lo que el Annex III pide);
**(4)** queda **expediente** de quién decidió qué y cuándo — que es lo que convierte una inspección en un trámite.

**Y el argumento de venta que viene del usuario final, no del regulador:** el pase 23 midió que **65 % de los alumnos
en LATAM teme el aprendizaje superficial**. Un sistema que explícitamente pone un humano a decidir sobre su caso **es
también el argumento pedagógico**, no sólo el de cumplimiento. **En LATAM esto se vende por pedagogía defendible; en
EMEA y North America, por cumplimiento.** Mismo entregable, dos relatos.

**Estimación.** 6–8 semanas: 2 de modelado sobre datos del cliente (con la licencia de los datasets verificada) y 4–6
de la capa de cola + expediente, **que es la que no existe y es la que se factura**. Ver el **gap 47** y la tendencia **68**.


## P54 — Asistente de corrección sobre Moodle con compuerta humana: el último tramo del gap 6, con piezas MIT que ya escriben (pase 27)

**Por qué este patrón existe recién ahora.** El **gap 6** —corrección y devolución— lleva abierto desde el pase 2 con
el mismo diagnóstico: la demanda está probada (Singapur construyó tres asistentes de devolución, cerrados) y la oferta
open source **analizaba sin escribir**. El resultado del análisis **no volvía al expediente del alumno**, y ese último
tramo se cotizaba como desarrollo. **El pase 27 encontró la pieza que lo cierra**, y es MIT.

**Las piezas, todas verificadas:**

| Pieza | Licencia | Rol |
|---|---|---|
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** ✅ | **El que escribe.** `get_student_submissions` → `provide_assignment_feedback` / `provide_quiz_feedback` |
| [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) | **MIT** ✅ | **El que cubre el resto**: 40 tools (gradebook, grupos, calendario) **+ `ws_raw`** para lo que falte |
| **Moodle** | GPL-3.0+ | El LMS, **sin modificar** — todo entra por Web Services con token |
| `MathTutorBench` / `pedagogy-benchmark` | MIT | **El *eval* pedagógico**, para medir la calidad de la devolución (gap 1, P10) |
| `learnmcp-xapi` + **lrsql** | permisivas | **La evidencia append-only** de cada devolución escrita |

**Wiring, y la compuerta es el punto del patrón:**

```
[Docente] ──── revisa y firma ────┐
                                  │  (nada se escribe sin este paso)
[Agente] ──MCP──▶ moodle-mcp-server ──▶ Moodle Web Services ──▶ nota + comentario
   │                                         (LMS sin modificar)
   ├──MCP──▶ moodle-mcp (40 tools) ──▶ gradebook / grupos / calendario
   ├──▶ eval pedagógico (MathTutorBench) ──▶ puntaje de la devolución, antes de mostrarla
   └──MCP──▶ learnmcp-xapi ──▶ lrsql  ──▶ statement por cada escritura (quién, qué, cuándo)
```

🔴 **La razón regulatoria por la que la compuerta no es opcional ni es un detalle de UX.** **Oklahoma y Maryland
prohíben que la AI tome decisiones de alto impacto sobre un alumno**, y una nota lo es. El patrón **no es «la AI
corrige»**: es **«la AI instruye el expediente y la persona firma»** —exactamente el encuadre que el bloque de North
America viene sosteniendo— y el `provide_*_feedback` es **el punto donde se inserta la firma**. En **North America**
eso lo hace vendible; en **APAC** la compuerta **ya es política pública** (plataforma estatal + supervisión docente), así
que no hay que argumentarla, hay que instrumentarla.

**Estimación: 4–6 semanas.** ⚠️ **Lo que hay que decirle al cliente sin maquillar:** `peancor/moodle-mcp-server` tiene
**10 commits** y 8 tools — **es el punto de partida del último tramo, no un sistema de corrección**. El trabajo real
del proyecto es la compuerta, el *eval* y la evidencia; el conector se endurece, no se adopta tal cual.

## P55 — El conector MCP de Open edX, que es el único que de verdad no existe (pase 27)

**Reemplaza a P51**, cuyo premisa era falsa (ver la corrección al final de este archivo). **Acá la ausencia está
medida y es real:** búsqueda en modo extendido, **ningún conector MCP para Open edX** (**gap 48**).

**Por qué es el patrón de mayor valor comercial de esta KB en este momento:**

1. **Es el LMS de la huella pública grande** — los programas nacionales de **LATAM e India** corren sobre Open edX.
2. **Es la región de menor presupuesto.** En LATAM, **8 % de instituciones tiene presupuesto dedicado a AI** y
   **73,5 % ya enseña con AI**: el entregable tiene que correr **sobre lo que ya está pagado**, y eso es Open edX.
3. **La arquitectura está resuelta dos veces** (Canvas y Moodle): no hay que diseñar, hay que portar.
4. **El cliente ya llega con telemetría impuesta:** si corre Open edX con analítica, corre **Aspects → Ralph sobre
   ClickHouse sin haberlo elegido** (pase 22). El conector es la puerta que falta sobre un stack ya decidido.

**La decisión de diseño a portar, que es lo que hace esto barato — de `MarcosNahuel/moodle-mcp`:**

| Decisión | Por qué importa en Open edX |
|---|---|
| **Fachadas de alto nivel, no un tool por endpoint** | 40 tools en 10 dominios en vez de cientos. Un catálogo volcado **no cabe en el contexto** y vuelve el conector inusable |
| **`ws_raw` como escape hatch** | Lo que la fachada no cubra sigue alcanzable **sin esperar una release**. Es la válvula que evita el bloqueo |
| **Descubrimiento de tools** (`search_canvas_tools` en `canvas-mcp`) | Con catálogo grande, el agente **busca** la herramienta |
| **Separación alumno / docente / diseñador** | Open edX tiene roles por curso: el mapeo es directo |

**Wiring:**

```
[Agente] ──MCP──▶ openedx-mcp (A CONSTRUIR — licencia a elegir, MIT recomendada)
                       │
                       ▼
        APIs REST de Open edX  ◀── sin parchear la plataforma
        (Course Blocks · Enrollment · Grades · Studio/CMS)
                       │
                       ▼
        Aspects / Ralph / ClickHouse  ◀── la analítica que el cliente ya tiene
```

🔴 **Lo que hay que medir ANTES de cotizar, y es la acción 1 que el pase 27 deja escrita:** si Open edX expone una
**superficie REST estable y versionada** equivalente a los Web Services de Moodle. **Si la hay, este patrón se cotiza a
6–8 semanas. Si no la hay, ésa es la razón por la que nadie lo construyó** — y es un hallazgo igual de valioso que el
conector. **No se promete el patrón antes de esa verificación.**

## P56 — SCORM como formato de salida de la capa generativa: aterrizar en el LMS que el cliente ya tiene, sin integrarse con él (pase 27)

**El problema que resuelve, y es el más común de todos.** Esta KB tiene una capa generativa fuerte —**OpenMAIC** (MIT,
tema → clase interactiva multi-agente), **Educhain** (MIT, YouTube → curso)— y un cliente que dice *«muy bien, y cómo
entra esto a mi LMS»*. La respuesta por integración es un conector por plataforma. **La respuesta por formato es un
paquete que cualquier LMS importa desde hace veinte años.**

| Pieza | Licencia | Rol |
|---|---|---|
| **OpenMAIC** / **Educhain** | MIT ✅ | Generan el contenido |
| [`giacomomaria81/scorm-mcp-server`](https://github.com/giacomomaria81/scorm-mcp-server) | **MIT** ✅ | `scorm_package` (HTML → SCORM **2004 4.ª ed.** o **1.2**), `scorm_validate`, `scorm_selftest` |
| **Moodle · Open edX · Canvas · cualquier LMS** | — | **Importan SCORM sin desarrollo** |

**Wiring:**

```
[tema / PDF / video]
      │
      ▼
OpenMAIC · Educhain ──▶ HTML del módulo
      │
      ▼
scorm_package  ──▶  .zip SCORM (assets inlineados como data URI → 100 % offline,
      │               runtime que reporta completion, progreso, tiempo y resume)
      ▼
scorm_validate ──▶  conformidad verificada ANTES de entregar
      │
      ▼
[LMS del cliente]  ◀── importación estándar, cero integración
```

**Las tres razones por las que este patrón gana más seguido de lo que parece:**

1. **Cero integración, cero permisos.** No hay token de API, no hay plugin, no hay revisión de seguridad del LMS. Es el
   camino más corto del laboratorio al aula.
2. 🔴 **El `resume` y el reporte de progreso vienen puestos.** El paquete reporta *completion*, progreso y tiempo — es
   decir **produce la telemetría mínima** sin que haya que montar un LRS en la primera etapa.
3. **Offline de verdad.** Al inlinear cada asset como data URI, el módulo corre sin red. Conecta directo con
   **Project NOMAD** (Apache-2.0, servidor de conocimiento offline) y con los despliegues de baja conectividad — que es
   buena parte de la huella educativa pública de **LATAM** y **APAC**.

**Estimación: 2–3 semanas** para el primer módulo validado de punta a punta. ⚠️ **El límite a declarar:** SCORM
**no lleva la conversación de vuelta** — es contenido empaquetado, no un tutor en vivo. Para interacción con el alumno
hace falta el conector del LMS (**P54**, **P55**) o xAPI. **SCORM es la vía de entrada, no el destino.**

## P57 — Evidencia de competencia por MCP, cotizada sobre la superficie que CaSS realmente expone (pase 27)

**Refina P50** con la medición por adaptador del pase 27, que es lo que separa una propuesta cotizable de una promesa.

**Lo que SÍ entra por MCP en `cassproject/CASS`** (Apache-2.0, medido por anotación, **2 canales**):

| Tool | Operación | Uso |
|---|---|---|
| `get_learner_profile` | `GET /api/profile/latest` | Leer el perfil de competencia computado |
| **`record_evidence`** | `POST /api/xapi/statement` | **Escribir evidencia — un statement por llamada** |
| `search_data` · `get_object` · `save_object` | CRUD JSON-LD | Marcos y objetos |
| `server_status` | `GET /api/ping` | Salud |

🔴 **Lo que NO entra, y hay que decirlo en la propuesta porque está excluido a propósito:**

| Capa | Operaciones ocultas | Consecuencia de cotización |
|---|---|---|
| **CASE** (`caseAdapter` + `caseIngest`) | **13** | **Autoría de marcos de competencia: por REST, fuera de MCP** |
| **CEASN** | 6 | Fuera de MCP |
| **Open Badges** | **5** | 🔴 **Emisión de insignias: fuera de MCP.** Y el adaptador es **OB 2.0** (`w3id.org/openbadges/v2`), **no 3.0** |
| **Bulk xAPI** (`POST /api/xapi/statements`) | — | 🔴 **Ingestión masiva de telemetría NO entra por MCP.** Un statement por llamada |

**Las frases que se pueden decir y las que no.** ✅ *«El perfil de competencia se lee por MCP»*, *«la evidencia se
registra por MCP, de a un statement»*. 🔴 *«Emitimos insignias por MCP»*, *«autoramos el marco por MCP»*, *«ingestamos
la telemetría histórica por MCP»* — **las tres son falsas**. Y si el cliente pide **OB 3.0 / W3C VC**, **CaSS no es la
pieza que las emite.**

**Checklist de despliegue — y el primer ítem es el que hace fallar esto en silencio:**

1. 🔴 **Verificar `CASS_LOOPBACK` antes que nada.** El adaptador pide el spec por loopback
   (`fetch(CASS_LOOPBACK + '/swagger.json')`, default `http://localhost/api/`, **puerto 80**). Si ese `fetch` falla,
   **hace `return` y la ruta `/api/mcp` no se monta — con el servidor arrancando normalmente.** El síntoma es *«no veo
   herramientas»*, no *«no arranca»*. Con proxy, puerto no estándar o HTTPS mal resuelto, **la superficie de agente
   desaparece sin error visible**.
2. Verificar que `DISABLED_ADAPTERS` **no** contenga `mcp`.
3. Elasticsearch en `:9200` — el *probe* sólo pide `GET /` y salud **`yellow`/`green`**.
4. `initialize` + `tools/list` contra **`POST /api/mcp`** y **comparar con las 6 declaradas**.

⚠️ **El asterisco que este patrón todavía lleva, dicho con precisión:** las 6 tools están confirmadas **por
declaración en el código, por dos métodos independientes** (ejecución del generador en el pase 26, conteo estático de
anotaciones en el pase 27) — **no por invocación**. Nadie hizo el `tools/list` real. **Alcanza para cotizar el catálogo
y el alcance; no alcanza para prometer latencia, forma de respuesta ni comportamiento de sesión.** Ver el **gap 40**.
