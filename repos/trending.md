---
industry: education
region: Global
updated: 2026-09-30
---

# 📈 Repos trending — education

> **APPEND-ONLY.** Cada corrida agrega una sección fechada arriba y conserva la historia abajo.

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
