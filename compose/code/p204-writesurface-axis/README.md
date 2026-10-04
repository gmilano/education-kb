---
industry: education
region: Global
updated: 2026-10-04
---

# p204 — Barrido de licencia por PAYLOAD + el segundo eje (escritura) · pase 70 del 2026-10-03

## Qué hace `sweep_payload_license.sh`

Mide el `LICENSE` de una lista de slugs **por payload**, no por el campo de un registro ni por la
API de GitHub: pide `raw.githubusercontent.com/<slug>/<rama>/<nombre>` y, cuando devuelve 200,
registra **bytes**, **`sha256`** y la **línea de titular**.

```bash
./sweep_payload_license.sh owner/repo owner2/repo2 > result.$(date +%F).tsv
```

Prueba `main` y `master` × `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE`.

## Por qué este canal y no la API

🔴 **En el entorno de este pase, `api.github.com` y `github.com` devolvieron HTTP 403** (proxy).
`raw.githubusercontent.com` respondió 200. **Ninguna cifra de licencia del pase 70 sale de la API**,
y ése es el canal que **P172** prefiere de todos modos: el payload es la cesión, el campo del
registro es una afirmación sobre la cesión.

## Resultado de la tanda (`result.2026-10-03.tsv`)

| slug | veredicto |
|---|---|
| `oliverhruby/edupage-mcp` | 🟢 MIT, 1.070 B, `Copyright (c) 2026 Oliver Hrubý` → `HOLDER-MATCH` |
| `buriro-ezekia/mwalimulens-agent` | 🟢 Apache-2.0, 11.357 B, `sha256:c71d239df917`, prístina → `NOT-APPLICABLE` |
| `mazhar266/fedena` | 🟢 Apache-2.0, 11.357 B, **mismo hash** (`LICENSE.md`, rama `master`) |
| `classroomio/classroomio` | 🔴 **AGPL-3.0**, 34.523 B, `sha256:8486a10c4393`, boilerplate FSF |
| `gibbonedu/core` | 🔴 **GPL-3.0**, 35.121 B, `sha256:93178a43d6d3`, boilerplate FSF |
| `YeetingWaterbottle/canvas-mcp` | 🔴 **1.071 B / `5385a26e2fac` — byte a byte igual al upstream `vishalsachdev/canvas-mcp`: es un FORK** |
| `hesham0-0nasser/tutor-lms-mcp` | 🔴 `NO-CESSION` — árbol real (`master/README.md` → 200), **sin archivo de licencia en 5 nombres × 2 ramas** |
| `projectfedena/fedena` | 🔴 **no resuelve** — 404 en README y en los 5 nombres × 2 ramas |

## ⚠️ Dos limitaciones conocidas de este instrumento, las dos encontradas EN este pase

1. 🔴 **No distingue «árbol muerto» de «árbol sin LICENSE».** Hay que confirmar la existencia del
   árbol por separado, con **otra** celda. En este pase eso separó a `hesham0-0nasser/tutor-lms-mcp`
   (árbol vivo, sin cesión) de `projectfedena/fedena` (no resuelve).
2. 🔴 **Un sondeo por nombre único produce falsos negativos** (**P198**): `mazhar266/fedena` se
   declaró muerto en el primer sondeo porque **no tiene README**, y resuelve perfectamente en
   `master/LICENSE.md`, `master/Gemfile` y `master/config/routes.rb`. **La reachability es una
   MATRIZ.**

## El segundo eje — lo que este script NO mide (y por eso existe P204)

🔵 La licencia es **un** eje. `oliverhruby/edupage-mcp` lo pasa con nota perfecta y es la pieza más
riesgosa del pase. El segundo eje se contesta leyendo el README y la lista de tools:

| Pregunta | `edupage-mcp` |
|---|---|
| ¿Tiene superficie de escritura? | 🔴 sí (mensajes, comedor, cambio de cuenta de alumno) |
| ¿Compuerta en código? | 🔴 no — sólo prosa: *«Use them with care»* |
| ¿API documentada por el proveedor? | 🔴 no — *«EduPage's undocumented endpoints»* vía `edupage-api` |

**Acción obligatoria cuando las tres respuestas caen así: envolver con
`compose/code/mcp-allowlist-gateway/` y no prometer estabilidad de la integración.**
