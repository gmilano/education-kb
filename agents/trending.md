---
industry: education
region: Global
updated: 2026-09-30
---

# 📈 Agentes trending — education

> **APPEND-ONLY.** Cada corrida agrega una sección fechada arriba y conserva la historia abajo.
> No reescribir secciones anteriores: la serie temporal es el valor de este archivo.

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
