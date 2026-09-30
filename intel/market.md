---
industry: education
region: Global
updated: 2026-09-30
---

# 🗺️ Mapa de mercado — Education

> Key players, market map y oportunidades por región.
> Investigado 2026-09-30. Las estimaciones de tamaño de mercado varían mucho entre firmas: se listan todas con su fuente en vez de elegir una.

## Tamaño de mercado

**AI en educación, 2026** — las estimaciones no coinciden, y el rango importa:

| Fuente | Estimación 2026 |
|--------|-----------------|
| HolonIQ | $12.3B |
| Grand View Research | $11.4B |
| Research and Markets | $10.6B |
| MarkWide Research | $8.7B |

Rango: **$8.7B – $12.3B**. Usar el rango, no un número puntual, en material de cliente.

- Proyección a 2030: **$42.48B**, CAGR ~41.5%
- Segmento AI tutors específicamente: **$2.7B** en 2026
- EE. UU.: $2.01B (2025) → $32.64B (2034) proyectado
- APAC: **$987M**

**Señal de demanda:** 83% de las instituciones declara planes de desplegar AI teaching assistants para 2026.

### Agregado en la segunda pasada del 2026-09-30

Más estimaciones, que ensanchan el rango en vez de cerrarlo — razón de más para no citar un número puntual:

| Métrica | Valor | Fuente |
|---------|-------|--------|
| AI en educación, 2025 | $7.05B – $7.57B | agregadores de mercado |
| Proyección 2034 | **>$112B** | idem |
| GenAI aplicada a la enseñanza | $1.53B (2025) → **$2.19B (2026)**, CAGR 43.5% | reporte sectorial |

**Adopción docente — los números duros que sirven en una propuesta:**

- **60% de los docentes de EE. UU. usa herramientas de AI** (Gallup, n=2.232).
- Adopción **34% (2023) → 61% (2026)**: casi se duplicó en tres años.
- Quien la usa **semanalmente ahorra 5,9 horas por semana**. Es el único número de ROI del sector que está medido en tiempo docente y no en percepción — usarlo.
- **Sólo 18% de los docentes de EE. UU. tiene alguna política escrita** sobre uso de AI (marzo 2026).

Ese último dato es el más accionable de toda esta pasada. Ver el punto 1 de North America y la tendencia nueva en `intel/trends.md`.

## Players globales

| Empresa | Tipo | Fortaleza | Debilidad |
|---------|------|-----------|-----------|
| **Khan Academy / Khanmigo** | Non-profit, AI tutor | Define la categoría. De 68k a **1.4M usuarios en 18 meses**; de 45 a **380+ distritos escolares**. Credibilidad pedagógica que ningún vendor comercial iguala | Modelo non-profit limita velocidad comercial; dependencia de un proveedor LLM externo |
| **Duolingo** | Consumer, language | IPO completado, **>$1B de revenue**, 47.7M DAU, 15% en el tier premium con AI. Mejor loop de engagement del sector | Un solo dominio (idiomas). Difícil de extender a currículo formal |
| **Coursera** | MOOC / credenciales | 12.0% de citation share; el default para credenciales universitarias | Margen comprimido; el contenido se comoditiza con GenAI |
| **MagicSchool** | Teacher-facing AI | 8.0% citation share; **líder en herramientas para docentes**, no para alumnos — el ángulo menos disputado | Producto de features, poco foso defensivo |
| **Udemy** | Marketplace | 6.5% citation share; sobrevivió pivoteando a enterprise | Calidad heterogénea; marca débil en educación formal |
| **MasterClass** | Premium content | 5.5% citation share; halo de marca | No es educación medible; entretenimiento aspiracional |
| **Chegg / Course Hero / Quizlet / Study.com** | Legacy SEO | Nada defendible hoy | **Fuera del top 15** del AI Visibility Index 2026. Colapsos de tráfico documentados por AI Overviews. Son el caso de estudio de qué le pasa a un negocio educativo construido sobre SEO |
| **Google** | Big tech | Distribución (Classroom, Workspace) | Integra AI en herramientas existentes en vez de construir plataforma educativa dedicada — deja el vertical abierto |

**Lectura estratégica:** los ganadores de 2026 son los que tienen *relación institucional* (Khanmigo con distritos, Coursera con universidades) o *loop de producto* (Duolingo). Los que tenían tráfico se quedaron sin nada. Para Globant, el cliente que paga es la institución y el ministerio, no el alumno.

## Oferta open source por región

Dónde se produce el software educativo abierto, que no es donde está la demanda:

| Región | Qué produce |
|--------|-------------|
| **APAC** | **Domina la oferta de agentes.** DeepTutor (HKU, 40.6k ★), OpenMAIC (Tsinghua, 39.7k ★), Educhain (India), Moodle (Australia), Frappe LMS + OpenEduCat (India) |
| **North America** | Plataformas e investigación: Open edX (MIT/Harvard), Canvas, Oppia, OATutor (UC Berkeley), Kolibri, Project NOMAD (38.8k ★) |
| **EMEA** | Plataformas de compliance y contenido: OpenOLAT (Suiza), Chamilo (Bélgica/España), Richie (Francia), H5P (Noruega), AITutor-EvalKit (MBZUAI, Abu Dhabi), education-agent-skills (UK) |
| **LATAM** | **Gap declarado.** Ver abajo |

## Opportunities by region

### North America

**Contexto.** Adopción ya ocurrió, sin gobernanza: el uso de AI por estudiantes saltó de 66% a **92% en un año**; ~90% de universitarios la usan como herramienta principal de investigación; 83% de los docentes K-12 usan GenAI. Regulación fragmentada: 24 estados con leyes o resoluciones desde 2025, **134 proyectos de ley en 31 estados** en 2026, y **cero estándares federales vinculantes** de currículo AI a mayo 2026. El Department of Education prioriza AI en discretionary grants desde 2026-05-13.

**Oportunidades.**
1. **Compliance multi-estado como producto.** California AB 1159 prohíbe usar datos de estudiantes para entrenar modelos; Oklahoma y Maryland prohíben que la AI tome decisiones de alto impacto sobre alumnos; Idaho SB 1227 exige framework estatal, estándares de AI literacy, formación docente y prohíbe que la AI reemplace docentes. Un distrito que opera en varios estados no tiene cómo cumplir 134 reglas distintas a mano. **Capa de policy-as-config sobre el LMS** — el diferenciador es auditabilidad, no el modelo.
2. **Human-in-the-loop obligatorio como arquitectura.** Donde la ley prohíbe decisiones automáticas de alto impacto, el patrón de `tutor-mcp` (decisiones pedagógicas auditables) y `gradescope-mcp` (escrituras detrás de confirmación explícita) es exactamente el diseño requerido. Vender el gate, no el automatismo.
3. **Currículo AI para créditos de CS.** Georgia y Mississippi ya embuten AI en créditos de computer science. `LLMs-from-scratch` y `minimind` (ambos Apache-2.0) son material listo para curricularizar.
4. **Captura de discretionary grants.** Hay dinero federal etiquetado para AI desde mayo 2026; el ciclo de grants premia propuestas con arquitectura y evaluación definidas, que es justamente lo que un studio puede aportar a un distrito.

**Actualización 2026-09-30 (pase 2) — de "134 proyectos" a tres leyes con fecha.** El detalle legislativo ahora es específico y tiene deadline, lo que lo convierte en pipeline y no en contexto:

- **Tres estados ya tienen estatutos de AI para K-12 sancionados: Maryland, Idaho y Oklahoma.** Los tres obligan a la agencia estatal a emitir guías, a los distritos a adoptar política alineada, y preservan control humano sobre notas y disciplina.
- **Maryland S.B. 720 — "Artificial Intelligence Ready Schools Act":** guía estatal actualizada periódicamente, política distrital alineada, **un AI coordinator designado por distrito**, un AI Education Collaborative estatal y desarrollo profesional pago a nivel estado.
- **Oklahoma S.B. 1734 — "Responsible Technology in Schools Act":** **cada distrito debe adoptar una política de AI escrita antes del ciclo escolar 2027-28**; uso human-in-the-loop dirigido por el docente; prohíbe que la AI sea base primaria de calificación, disciplina, placement u otras decisiones de alto impacto.
- **Idaho S.B. 1227:** framework de AI generativa que cubre privacidad, salvaguardas de compra, transparencia, integridad académica, estándares de AI literacy y formación docente.
- Volumen 2026: **77 proyectos sobre AI en instrucción de aula en 27 estados** (de los 134 totales en 31 estados).

**La oportunidad más clara del ciclo, y es aritmética:** Oklahoma obliga a *todos* sus distritos a tener política escrita antes de 2027-28, y a nivel nacional **sólo 18% de los docentes tiene hoy alguna política escrita**. Un mandato con fecha contra un 82% de incumplimiento. El entregable no es un modelo: es un **policy pack** — política escrita, formación docente, gates de human-in-the-loop configurados en el LMS y evidencia de auditoría — replicable distrito por distrito. Ver el patrón P7 en `compose/patterns.md`.

### EMEA

**Contexto.** Regulación primero, adopción después — lo inverso a Norteamérica. La fecha de aplicación de sistemas de alto riesgo del Annex III del EU AI Act (que **incluye AI en evaluación**) se corrió de 2026-08-02 a **2027-12-02** por el acuerdo del Digital Omnibus on AI. Las escuelas quedan responsables de auditar el uso de AI. Casos que caen en alto riesgo: **corrección automática de exámenes, aprendizaje adaptativo, proctoring y predicción de deserción** — o sea, casi todo lo interesante. La Comisión Europea con la OCDE y aval del G7 publicó un borrador de AI Literacy Framework para primaria y secundaria.

**Oportunidades.**
1. **Diciembre 2027 no es un botón de snooze — es el tamaño exacto de la ventana de consultoría.** 26 meses para que cada institución tenga sus sistemas de evaluación auditados y documentados. El entregable es el expediente de conformidad, y se vende ahora, no en 2027.
2. **Evaluación auditable sobre base permisiva.** **OpenOLAT (Apache-2.0, Suiza)** es el mejor punto de partida de la KB para esto: assessment serio + licencia que no contamina + credibilidad regional DACH. Combinar con `AITutor-EvalKit` para evidencia de calidad pedagógica documentada.
3. **AI soberana / on-premise.** El appetite de EMEA por no mandar datos de menores a una API de EE. UU. es real. Moodle + Ollama como provider local resuelve residencia de datos sin desarrollo custom.
4. **AI literacy alineada al framework CE/OCDE.** Hay un estándar naciente con aval del G7 y ningún proveedor consolidado alineado a él. Ser el primero en mapear currículo contra ese framework es posición defendible.
5. **Compliance en alemán.** ILIAS lidera en compliance en el mercado germanófono; es un segmento con exigencia documental alta y poca competencia de studios.

**Actualización 2026-09-30 (pase 2).** Confirmado el encuadre: la AI educativa cae **predominantemente en alto riesgo** — plataformas de aprendizaje adaptativo, corrección automática y sistemas de orientación escolar están los tres en Annex III. La enforcement del AI Act arrancó el **2026-08-02** con la AI Office y las autoridades nacionales; el **Digital Omnibus on AI, en vigor desde el 2026-07-27**, corrió las obligaciones de Annex III **16 meses, al 2027-12-02**. Es decir: el régimen ya está operativo y vigilado, sólo se diferió la parte de alto riesgo. No vender el diferimiento como permiso para esperar — las obligaciones de transparencia y alfabetización no se movieron.

### APAC

**Contexto.** Mercado de **$987M**, con China, India y Japón dominando por inversión e infraestructura. Regulación heterogénea y ése es el punto:
- **China** — el marco más restrictivo y completo de la región, sobre tres leyes fundacionales.
- **Japón** — segundo AI Basic Plan aprobado por el Gabinete el 14 de julio; la AI Promotion Act es deliberadamente flexible y pro-innovación. Motor demográfico: población que envejece y necesidad de calidad de enseñanza con menos docentes.
- **India** — en julio de 2026 el gobierno señaló que podría ir a legislación de AI dedicada; adopción fuerte vía plataformas de educación online.
- **Japón y Corea del Sur** tienen protección de datos estricta específica para AI en educación.

**Oportunidades.**
1. **APAC es proveedor, no sólo mercado.** Los dos mejores agentes educativos open source del mundo salen de acá: **DeepTutor (HKU) y OpenMAIC (Tsinghua)**, ambos ~40k ★ y con licencia permisiva. Un engagement APAC arranca con ventaja de código, y además con acceso a los maintainers.
2. **Orquestación multi-jurisdicción.** Un grupo educativo regional que opera en China + Japón + India + Singapur enfrenta cuatro regímenes incompatibles. Nodos de política por jurisdicción en el grafo del agente (patrón P5) es un diseño vendible y difícil de copiar.
3. **Japón: calidad docente con menos docentes.** El driver no es costo, es escasez demográfica. Un asistente que amplifica al docente que queda, no que lo reemplaza, encaja con la AI Promotion Act y con la resistencia cultural al reemplazo.
4. **India: escala y multilingüismo.** Volumen enorme, presupuesto por alumno bajo, muchos idiomas. `Educhain` (MIT, India) + Frappe LMS / OpenEduCat (stack indio) es una combinación culturalmente y técnicamente nativa.

**Actualización 2026-09-30 (pase 2) — currículo obligatorio, con fechas.** Lo que cambia la conversación en APAC no es la regulación: es que dos países pasaron AI a currículo **obligatorio nacional**, y son los únicos dos del mundo que lo hicieron.

- **India: AI y pensamiento computacional obligatorios desde 3.º grado (Class 3), arrancando el ciclo 2026-27.** Es el deadline más grande y más cercano de la KB: implica material curricular, formación docente masiva y plataforma, en múltiples idiomas y con presupuesto por alumno bajo.
- **China: currículo nacional de AI obligatorio desde el ciclo 2025-26.** Ya en ejecución.
- **Singapur — el orden de operaciones es la ventaja:** estrategia Smart Nation apuntando a liderazgo en AI hacia 2030, **formación docente prometida en todos los niveles para 2026**, y un centro de investigación financiado por el estado que **pilotea las herramientas antes de desplegarlas en el aula**. Para un studio, Singapur es el mercado donde la evidencia de evaluación pedagógica se pide de entrada.
- **Japón:** además del segundo AI Basic Plan, se espera que los libros de texto digitales puedan ser texto oficial **hacia el ciclo escolar 2030**, y está levantando institutos de testing y assurance.
- **Mercado AI de APAC (todo, no sólo educación): ~$102B (2025) → >$735B (2030)**, con India como el de crecimiento más rápido.
- **Movimiento de incumbentes:** TAL (China) pivoteó a **hardware** de aprendizaje con AI, Gauth de ByteDance se volvió una de las apps educativas más usadas del mundo, y PhysicsWallah (India) lanzó su propio tutor AI. En APAC el competidor no es un edtech occidental: es una plataforma local con distribución masiva.

**Oportunidad agregada — el deadline indio de 2026-27 es el más grande de la KB.** `Educhain` (MIT, India) para generación de contenido multilingüe + `ai-engineering-from-scratch` y `minimind` (los dos permisivos) como material, sobre Frappe LMS u OpenEduCat (stack indio). El comprador no es una escuela, es un estado o un grupo educativo de escala.

### LATAM

**Contexto.** 47% de despliegue de AI empresarial en 2026. Solo **Brasil (65.89), Chile (63.19) y Uruguay (62.21)** entran en el top 50 global de AI readiness. El dato que define la oportunidad: **13 de los 19 países de América Latina y el Caribe no enseñan adopción temprana de AI en las escuelas**, con un cuello de botella declarado en formación avanzada que limita la capacidad de la región de producir sus propias soluciones.

Regulación en formación, toda hacia gobernanza basada en riesgo: en Brasil el **PL 2.338/2023** sigue pendiente, con modelo de riesgo y penalidades severas; México incorporó **opt-out para decisiones automatizadas** en su última ley de protección de datos y el Congreso empuja reformas laborales y de derechos de autor sobre uso de imagen y AI. Brasil firmó un acuerdo de regulación de AI y tecnología con la UE en junio de 2026 — señal de que va a converger hacia el modelo europeo, no el estadounidense.

**Activo regional:** **Latam-GPT** (CENIA, Chile, lanzado feb-2026): Llama-3.1-70B, **230.000M+ de palabras**, 60+ instituciones de 15 países de LAC, español y portugués con lenguas indígenas planificadas, entrenado sobre fuentes de educación, salud, políticas públicas y comunidades indígenas. Gratuito para empresas e instituciones públicas. Pesos en Hugging Face: `latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0`.

**Oportunidades.**
1. **AI literacy a nivel sistema educativo, no a nivel escuela.** 13 de 19 países sin enseñanza temprana de AI no es un problema de producto, es un programa de ministerio. Currículo + formación docente + plataforma, con `minimind` y `LLMs-from-scratch` (Apache-2.0) como material base. El comprador es el ministerio y el financiador suele ser el BID.
2. **Latam-GPT como argumento de soberanía.** Modelo regional, gratuito, entrenado en contexto cultural propio. Permite ofrecer tutoría en español/portugués sin dependencia de un proveedor de EE. UU. y sin costo de licencia de modelo. Es el diferenciador que ningún competidor global puede replicar rápido.
3. **Offline-first por infraestructura, no por ideología.** **Kolibri (MIT)** y **Project NOMAD (Apache-2.0, 38.8k ★)** + Ollama dan tutoría con AI donde la conectividad no es confiable. Para escuelas rurales de Brasil, México, Perú y Centroamérica esto es la diferencia entre proyecto y piloto fallido.
4. **Brasil primero, y con lente europeo.** Es el país más preparado, el mercado más grande y acaba de firmar con la UE: el trabajo de conformidad que se haga para EU AI Act es reutilizable para el PL 2.338. Vender el mismo expediente dos veces.
5. **Chamilo como base de bajo costo.** Es el LMS más liviano de self-hostear, con adopción real en LATAM hispanohablante. Menor costo de infra por institución importa cuando el presupuesto por alumno es bajo.

**Actualización 2026-09-30 (pase 2) — la asimetría que define la región.** LATAM capta **1,1% de la inversión global en AI** pero **adopta al 47%, por encima del promedio global de 45%**. Brasil creció +1.400% en adopción y México 52%. Se adopta mucho más de lo que se invierte: la región compra e implementa, no financia producto propio. Para un studio eso es favorable — el gasto va a servicios e implementación, no a licencias de producto local.

Regulación, mapa ampliado (todo converge al modelo europeo basado en riesgo):

- **Brasil** — PL 2.338/2023 **aprobado por el Senado en diciembre de 2024**, pendiente en Cámara de Diputados. Clasificación por riesgo, obligaciones de transparencia, evaluación de impacto algorítmico y **registro nacional de sistemas de alto riesgo**. La propuesta más completa de LATAM.
- **Chile** — proyecto de ley de AI en trámite, enfoque basado en riesgo **explícitamente similar al EU AI Act**.
- **Colombia** — **CONPES 4144 (2025)**, hoja de ruta nacional de desarrollo de AI.
- **Perú** — discutiendo normas sobre usos sensibles (manipulación electoral, discriminación algorítmica).
- **México** — opt-out de decisiones automatizadas en su ley de datos. Mercado AI: $3,2B (2024) → **$5,5B (2026)**.

**Cuentas de referencia que ya declararon el deadline:** el **Tec de Monterrey** (México) está **rediseñando más de 44 programas universitarios para integrar AI completamente hacia 2026**, y la **PUC de Chile** lleva adelante *ConectIA* con Microsoft para integración institucional en el mismo horizonte. Son los dos compradores-faro de la región: lo que hacen define lo que el resto licita. UNESCO además publicó un estudio de **200 prácticas educativas de América Latina y el Caribe** que ya integran AI — es el mejor catálogo de casos regionales disponible para material de cliente.

**Oportunidad agregada — vender el expediente de riesgo una vez y cobrarlo cuatro veces.** Brasil (PL 2.338), Chile (proyecto basado en riesgo), Colombia (CONPES 4144) y el acuerdo Brasil–UE apuntan al mismo marco conceptual. Un expediente de conformidad hecho para EU AI Act se reusa en los cuatro. Combinado con la asimetría 1,1%/47%: la región tiene apetito de implementación y poca capacidad propia de producir la gobernanza.

**Gap declarado (LATAM), refinado en el pase 2.** Se buscó explícitamente en español y portugués. **Sí existen agentes educativos open source de origen latinoamericano, y ninguno tiene tracción medible:** `H1bertto/professor-agent` (Brasil, MIT, **0 ★**) y `ANTONIOALGMAR/StudyAgent` (Brasil, **sin licencia**, 2 ★) — el segundo, sin licencia, no es legalmente reutilizable ni siquiera si el código sirviera. `studyield/studyield`, que aparecía como plataforma en 12 idiomas, **da 404**. Conclusión anterior (ninguno con tracción medible) Latam-GPT es un *modelo fundacional*, no un framework de agentes ni una plataforma de tutoría. Esto significa: (a) no hay punto de partida regional que reusar, y (b) es espacio abierto — un agente de tutoría open source diseñado en LATAM, en español y portugués, sobre Latam-GPT, no tiene competencia hoy. Se declara como hueco confirmado, no como falta de búsqueda.

## Posicionamiento Globant

**Dónde el studio gana en educación:**

1. **Integración sobre plataformas copyleft sin contaminar el IP del cliente.** La mitad del stack educativo es GPL/AGPL. Saber integrar por XBlock, plugins del AI subsystem de Moodle y LTI 1.3 — en vez de forkear — es capacidad técnica escasa y vendible.
2. **Compliance como entregable, no como checklist.** EU AI Act Annex III en 2027-12-02 y 134 proyectos de ley estatales en EE. UU. crean demanda de arquitecturas auditables. El expediente de conformidad es el producto.
3. **Ventaja de huella global real.** La oferta open source está en APAC, la demanda regulada en EMEA y Norteamérica, y el gap de capacidades en LATAM. Globant tiene presencia en las cuatro. Portar DeepTutor/OpenMAIC (APAC) a un marco de conformidad EMEA, o a un programa de ministerio LATAM, es arbitraje que un player regional no puede hacer.
4. **LATAM con producto propio.** Es el único de los cuatro donde no hay incumbente open source. Latam-GPT + Kolibri/NOMAD offline + currículo de AI literacy es una oferta que se puede construir una vez y vender a varios ministerios.

---
*Fuentes en `intel/trends.md`. Cifras de mercado con rango explícito: no reportar un número puntual sin la fuente.*
