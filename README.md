---
industry: education
region: Global
updated: 2026-10-10
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

## Pase 91 — 2026-10-10

**El hallazgo principal: el instrumento de esta KB tenía un alcance que nunca tuvo, y eso movió una cifra publicada.**

`grant-ladder-v2` probaba **12** nombres de archivo. Seis filas del shelf afirmaban *"17 candidate filenames"*
y otras cinco *"16 names"*. **Tres números para un solo instrumento, y ninguno era el del instrumento.**

- 🔴 **No fue cosmético: produjo un FALSO NEGATIVO.** [`frappe/lms`](https://github.com/frappe/lms) lleva su
  licencia en **`license.txt`** (minúscula), un nombre que v2 **nunca probó**. El TSV del pase 90 lo registra
  como `NO-LICENCE-PAYLOAD`; el `verticals/solutions.md` del **mismo commit** lo publica correctamente como
  **AGPL-3.0, 33 893 B** — hallado a mano. El negativo automático y el positivo verificado convivían.
- 🟢 **`grant-ladder-v3` prueba 24 nombres e imprime la cuenta** (`--count`, `--names`).
  **Un negativo cuyo denominador no se puede imprimir no es una medición.**
- 🟢 **Efecto sobre los mismos 92 slugs, mismo día, mismos SHAs:** `NO-LICENCE-PAYLOAD` **6 → 5**,
  `AGPL-3.0` **11 → 12**, `OTHER/unclassified` **2 → 0** (ECL-2.0 ya se clasifica por nombre).
  **El *"6 de 92, ~1 en 15"* del pase 90 se corrige a *5 de 92, ~1 en 18*.** El mundo no cambió; el alcance sí.

**Una afirmación de cinco pases, FALSIFICADA cambiando una palabra de la consulta:**

- 🔴 Esta KB publicó en tres archivos que *"no existe checker de accesibilidad con IA bajo licencia permisiva"*.
  🟢 **Existen tres, todos MIT, hallados en la primera consulta dirigida:**
  [`tomaszboloz/WCAG-Accessibility-Skills`](https://github.com/tomaszboloz/WCAG-Accessibility-Skills),
  [`Community-Access/accessibility-agents`](https://github.com/Community-Access/accessibility-agents),
  [`9mtm/WCAG-Checker`](https://github.com/9mtm/WCAG-Checker).
- 🔵 **La causa es transferible: la consulta nombraba la INDUSTRIA.** *"accessibility checker education"*
  devuelve plugins de LMS, y el plugin de LMS de este espacio (`UDOIT`) es GPL y no usa IA — así que la
  búsqueda devolvía "nada usable" con toda honestidad. Buscar **el estándar** (**WCAG**) los devuelve de
  inmediato. 🟢 **`P955`: una herramienta de cumplimiento se llama como el estándar que aplica, no como el
  sector que la compra.**
- 🔴 **Y la fila más capaz del tier es inusable:** `qed42/ai-accessibility-checker` se publica como MIT y
  **no tiene payload de licencia en 24 nombres**.

**Otros resultados del pase:**

- 🟢 **120 slugs resueltos.** Control de dos lados: cuatro slugs inventados `ABSENT`, `moodle/moodle`
  **35 147 B** en nueve corridas, idéntico byte a byte a siete pases previos.
- 🔴 🆕 **El riesgo de licencia migró del repositorio al CORPUS** (`P957`).
  [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) otorga **cuatro
  licencias en UN archivo**: código **MIT**, prompts **CC-BY-4.0**, y **dos corpus anotados CC-BY-NC-SA-4.0**.
  **La cláusula no-comercial cae exactamente sobre los corpus — la parte que lo hace un evaluador con
  evidencia y no una plantilla de prompt.** 🔵 **La pregunta no es "¿es permisivo?" sino "¿la parte permisiva
  es la parte valiosa?".**
- 🟢 🆕 **Categoría nueva: el mandato curricular.** Cuatro jurisdicciones ya **obligan a enseñar IA** en vez de
  solo regular sistemas de IA: **China** (MoE, ≥8 h/año desde los seis años, Sep 2025), **Singapur** (MoE,
  Mar 2026, todas las escuelas en 2027), **India** (**CBSE**, Clases 3–8, ciclo 2026-27, notificación del
  9 Abr 2026) y la **UE** (AI Act Art. 4, alfabetización del personal, **ya vigente y NO diferida a 2027**).
  🔴 **Y toda la oferta permisiva de currículo de IA de este shelf está escrita para desarrolladores adultos:
  nada cubre primaria.** Ver `P91-G` y `Gap 367`.
- 🟢 **`Gap 365` descargado:** `topics/scorm` página 2. La cola es delgada (máx. 20★) pero **tres filas
  importan**, y una es estratégica: [`edly-io/pxc`](https://github.com/edly-io/pxc) (**Apache-2.0**) es un
  **estándar propuesto para reemplazar SCORM + H5P + LTI**, publicado por el vendor comercial de Open edX.
- 🔴 **`topics/lms` está contaminado por colisión de siglas** (`Gap 368`): 4 de 20 filas de la página 2 no son
  plataformas de aprendizaje — **LMS = *Least Mean Squares*** y **LMS = *Library* Management System**.
  **80 % de precisión contra ~100 % en la página 1.**
- 🟢 **LATAM colocada y corregida.** 🆕 [`mumuki/mumuki-laboratory`](https://github.com/mumuki/mumuki-laboratory)
  (AGPL-3.0, Argentina, práctica de programación con corrección automática en aulas reales).
  🔴 **Tres cifras distintas circulan atadas al número 30 %**; solo una está respaldada — para cobertura de
  políticas institucionales usar el **26 %** medido por UNESCO IESALC.
- 🟢 **EMEA tiene números por primera vez en esta KB** (HEPI, trabajo de campo Dic 2025, n=1 054 UK:
  **36 %** se siente alentado por su institución, **38 %** recibe herramientas de IA) y una fila permisiva
  nueva en el tier de plataformas: [`openfun/richie`](https://github.com/openfun/richie) (**MIT**, France
  Université Numérique) — la capa de portal que al tier le faltaba.
- 🔴 **ADL deja sin licencia sus propias especificaciones: 3 de 5 repos** (`Gap 354` endurecido). **La suite
  oficial de conformidad SCORM 2004 no puede redistribuirse en un entregable.**

## `compose/code/grant-ladder-v3/` — el instrumento

`curl -sI https://github.com/<slug>` **no discrimina** bajo el proxy de egreso de estas sesiones: devuelve 403
para un slug real y uno inventado por igual, y con `-sI` imprime solo el `200 Connection Established` del
proxy — que pases anteriores tomaron por una página viva. `api.github.com` igual. **Lo que sí discrimina:**
`git ls-remote --symref` (existencia, rama, SHA) y `raw.githubusercontent.com/<slug>/<SHA>/<file>` (licencia).
Control de dos lados en cada corrida. Ver `compose/code/grant-ladder-v3/README.md`. 🆕 **Y un positivo nuevo en el mapa de oráculos: `WebFetch`
renderiza `github.com/topics/<t>` con estrellas y el total del topic, mientras `curl` en la misma URL da 403.**

## Uso

1. **Nuevo engagement**: leer `intel/market.md` + `repos/foundations.md`
2. **Proponer solución AI**: `agents/top.md` + `compose/patterns.md`
3. **Mantenerse al día**: correr `ingest/update.sh` semanalmente
4. **Verificar antes de citar**: `compose/code/patterns-figure-audit/extract_figures.py --check`
   remide las cifras de `compose/patterns.md` que salen de suites propias. **Una cifra de una suite
   se vence cuando la suite crece**, y el pase 47 encontró dos vencidas

---
*Red de KBs Globant AI Studios → [globant-kb](../globant-kb/)*
