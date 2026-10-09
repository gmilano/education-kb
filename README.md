---
industry: education
region: Global
updated: 2026-10-09
---

# 📚 Education KB

> Knowledge base de la industria **Education** para Globant AI Studios.
> Tutores AI, evaluación automática, personalización del aprendizaje, LMS agents

## Estructura

```
education-kb/
├── agents/        # Agentes AI open source de la industria
├── repos/         # Repos MIT/Apache como punto de partida
├── verticals/     # Plataformas verticales customizables con AI
├── intel/         # Mercado, players, tendencias
├── compose/       # Recetas: cómo componer soluciones
├── ingest/        # Scripts de actualización automática
└── compose/code/  # Código ejecutable y probado, no prosa
```

## Pase 90 — 2026-10-09

**El hallazgo principal: el tier de plataformas permisivas sí existe, y es ~9, no 2 ni 0.**

Esta KB afirmó durante seis pases que el tier de plataformas era `8 de 8 copyleft`. El pase 89 lo corrigió a
`2 de 10`. Ese número también estaba mal, por un factor de cuatro. Medición del pase 90, con criterio de
pertenencia declarado **antes** de contar:

- 🟢 **9 plataformas permisivas**, 4 de grado productivo con despliegues institucionales con nombre.
- 🟢 **[`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) — MIT, 816★, TU München** — plataforma
  universitaria en producción con tres subsistemas LLM ya integrados: **Iris** (tutor), **Athena** (feedback),
  **Hyperion** (autoría de ejercicios con IA). MIT + producción + IA nativa: la combinación que esta KB
  sostenía que no existía.

**Dos causas del fallo, y la segunda es la transferible:**

1. Ningún censo declaró su criterio de pertenencia: cada pase reportaba la mezcla de licencias de la muestra
   que le dejó el anterior.
2. 🔵 **Una familia de licencias que el instrumento no conocía.** `Sakai` y `Opencast` son **ECL-2.0**
   (Educational Community License), aprobada por OSI, derivada de Apache-2.0, **permisiva**. El clasificador
   devolvió `OTHER/unclassified`, y lo no clasificado se lee como riesgo y se descarta.
   **Una industria con su propia familia de licencias será subcontada como copyleft por herramientas genéricas.**

**Otros resultados del pase:**

- 🟢 **92 slugs resueltos** (3 ABSENT, 6 sin payload de licencia), licencia leída del payload con SHA fijado.
- 🟢 **Categoría nueva: la *skill* de agente como unidad de entrega.** ~1 de cada 4 filas de `topics/ai-tutor`
  son skills para harnesses de agentes, no aplicaciones — y todas las verificadas son MIT.
- 🔴 **`frappe/lms` es AGPL-3.0, no MIT** (un artículo comparativo muy citado lo publica como MIT).
  **`plastic-labs/tutor-gpt` es GPL-3.0**, no permisiva. **`microsoft/autogen` tiene licencia partida**:
  `LICENSE` CC-BY-4.0, `LICENSE-CODE` MIT.
- 🟢 **LATAM colocada, no vacía:** `aprende-brasil` (MIT, pt-BR), `i-educar` (LGPL-3.0, el mayor sistema
  educativo libre de Brasil), `Agente-editor-inet` (GPL-3.0, escuelas técnicas INET). **Todas encontradas
  consultando en portugués y español; el barrido en inglés no devolvió nada para la región.**
- 🔴 **Hueco declarado:** no existe checker de accesibilidad o alineación instruccional con IA bajo licencia
  permisiva. `ucfopen/UDOIT` es GPL-3.0 y no usa IA.

## `compose/code/grant-ladder-v2/` — el instrumento

`curl -sI https://github.com/<slug>` **no discrimina** bajo el proxy de egreso de estas sesiones: devuelve 403
para un slug real y uno inventado por igual, y con `-sI` imprime solo el `200 Connection Established` del
proxy — que pases anteriores tomaron por una página viva. `api.github.com` igual. **Lo que sí discrimina:**
`git ls-remote --symref` (existencia, rama, SHA) y `raw.githubusercontent.com/<slug>/<SHA>/<file>` (licencia).
Control de dos lados en cada corrida. Ver `compose/code/grant-ladder-v2/README.md`.

## Uso

1. **Nuevo engagement**: leer `intel/market.md` + `repos/foundations.md`
2. **Proponer solución AI**: `agents/top.md` + `compose/patterns.md`
3. **Mantenerse al día**: correr `ingest/update.sh` semanalmente
4. **Verificar antes de citar**: `compose/code/patterns-figure-audit/extract_figures.py --check`
   remide las cifras de `compose/patterns.md` que salen de suites propias. **Una cifra de una suite
   se vence cuando la suite crece**, y el pase 47 encontró dos vencidas

---
*Red de KBs Globant AI Studios → [globant-kb](../globant-kb/)*
