---
industry: education
region: Global
updated: 2026-10-02
---

# El *tarball* de npm reabre DOS canales que esta base había dado por cerrados — pase 49

```sh
python3 probe.py @ink-waffle/sisu-mcp
python3 probe.py @imazhar101/mcp-canvas-server --json
python3 test_probe.py        # 19/19, sin red
```

**Dos clases de cifra estaban declaradas NO reproducibles en este entorno, y las dos lo eran por el
mismo motivo: se asumía que el único canal era el que está bloqueado.**

| Clase | Estado declarado | Canal que sí funciona |
|---|---|---|
| **`tools`** — **326 cifras** en los ocho archivos | 🔴 «exige el paquete instalado» | 🟢 `registry.npmjs.org` sirve el *tarball*: la superficie se cuenta **estáticamente** |
| **licencias** | 🔴 cerrado desde el pase 37 (`github.com` → **403**, `api.github.com` → 200 negando acceso) | 🟢 `raw.githubusercontent.com` → **200**, y el *tarball* trae su propio `package.json` |

🔵 **Y el canal de licencias se verificó repo por repo:** `raw.githubusercontent.com/<org>/<repo>/main/LICENSE`
devolvió **200** para Paper2Slides, VideoAgent, VideoRAG, DeepTutor y OpenMAIC, mientras
`github.com/<org>/<repo>` devolvía **403** para los cinco. **El canal no estaba cerrado: estaba mal
elegido.**

## 🔴 El hallazgo que más plata vale: la superficie de LMS más grande de esta KB no tiene licencia

| Paquete | Licencia (registro) | Licencia (manifiesto) | ¿Archivo de licencia? | Repositorio | Superficie |
|---|---|---|---|---|---|
| **`@imazhar101/mcp-canvas-server`** 2.1.3 | 🔴 **ninguna** | 🔴 **ninguna** | 🔴 **ninguno** | 🔴 **no publicado** | 🔴 **227 tools** |
| `@ink-waffle/sisu-mcp` 0.1.0 | MIT | MIT | 🔴 ninguno | 🔴 **no publicado** | **12 tools** |
| `@signdocs-brasil/mcp-server` 0.11.2 | MIT | MIT | 🟢 `LICENSE` | 🔴 no publicado | **26 tools** (37 registros) |
| `@timadey/proctor` 1.2.6 | MIT | MIT | 🔴 ninguno | 🟢 `github.com/Timadey/proctor` | 0 (no es MCP) |
| `@longsightgroup/qti3-cli` 0.13.1 | MIT | MIT | 🟢 `LICENSE.md` | 🟢 `github.com/LongsightGroup/qti3` | 0 (es CLI) |
| `@timeback/oneroster` 0.3.3 | 🔴 **ninguna** | 🔴 **ninguna** | 🔴 **ninguno** | 🔴 **no publicado** | 0 |

🔴 **`@imazhar101/mcp-canvas-server` expone 227 herramientas sobre Canvas LMS y NO declara licencia
en ningún canal.** Es la superficie de herramientas más grande de esta base y, tal como está
publicada, **es inusable para una entrega**: sin licencia no hay permiso, y el default legal es
«todos los derechos reservados». 🔵 **No es un número flojo: es un bloqueo comercial**, y se mide en
un comando.

### Las 227 están verificadas por dos conteos independientes

| Instrumento | Valor |
|---|---|
| nombres de tool distintos en `dist/servers/canvas/src/tools/` | **227** |
| ocurrencias de `inputSchema` en el mismo árbol | **227** |
| por archivo, en los **18** archivos de `tools/` | **coinciden uno a uno** |

`user-tools.js` **39**, `page-tools.js` **21**, `file-tools.js` **20**, `submission-tools.js` **20**,
`module-tools.js` **18**, `enrollment-tools.js` **15**, y así hasta
`lti-launch-definition-tools.js` **1**.

## ⚠️ Un CAMPO de licencia no es TEXTO de licencia, y la diferencia tiene consecuencias

El probe informa las dos cosas por separado, porque son hechos distintos:

- **`@ink-waffle/sisu-mcp`** —la única puerta de SIS de educación superior de esta base— dice **MIT en
  dos artefactos independientes** (el documento del registro y el `package.json` embarcado), y
  **no existe texto de licencia en ningún canal**: no hay archivo en el *tarball* y **no hay
  repositorio publicado**. ⚠️ El bloqueante del pase 47 (*«licencia sin segunda fuente»*) **baja de
  grado —la segunda fuente existe— y no se cierra: lo que falta ya no es la fuente, es el texto y el
  código.** Se embarca `dist/` compilado.
- **`@timadey/proctor`** declara `"license": "MIT"` **y lista `LICENSE` en su propio `files`**, o sea
  que el manifiesto **promete** embarcar un archivo que **no existe**: `LICENSE` y `LICENSE.md` dan
  **404** en `main` y en `master` mientras `README.md` da **200** en las dos.
  🟢 **Eso mejora el gap: la intención MIT está documentada dos veces**, así que no es un vacío de
  licencia sino un defecto de documentación — y **confirma que el PR de un archivo es el arreglo
  correcto**, porque agrega el archivo que el manifiesto ya promete.

## Los tres patrones de registro que hay en la práctica

El probe cuenta **nombres distintos**, no ocurrencias, y los tres patrones hacen falta:

1. `registerTool("nombre", …)` — el SDK actual (`sisu-mcp`, `signdocs-brasil`).
2. **`getToolDefinitions()` devolviendo `[{name, description, inputSchema}]`** — el SDK viejo, y
   **el motivo por el que la primera versión de este probe reportó 0 tools para un servidor que
   expone 227**.
3. `.tool(` / `setRequestHandler(` — contados como ocurrencias.

⚠️ **El patrón 2 obliga a exigir `name` Y `inputSchema` juntos:** `name:` aparece en **cada
propiedad de cada esquema**, así que buscar `name:` solo sobrecuenta por un orden de magnitud. Hay un
control para eso (`"una propiedad de esquema llamada 'name' no se cuenta como tool"`).

⚠️ **Y ocurrencias ≠ superficie:** `@signdocs-brasil/mcp-server` registra **37** veces **26**
herramientas, porque embarca dos *builds*. Publicar 37 infla la superficie un **42 %**.
