# Canvas LMS MCP Server

[![npm version](https://img.shields.io/npm/v/@charlie.act7/canvas-mcp-server)](https://www.npmjs.com/package/@charlie.act7/canvas-mcp-server)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Integración avanzada para Canvas Virtual Classroom con Inteligencia Artificial.

Este proyecto es un servidor de **Model Context Protocol (MCP)** para **Canvas LMS**. Funciona como un puente que permite a asistentes de Inteligencia Artificial (como Claude Desktop, Claude Code, Cursor, Windsurf, Cline, Roo Code, GitHub Copilot, Continue, Zed, Codex CLI, n8n, etc.) consultar y administrar tus cursos de Canvas mediante instrucciones en lenguaje natural.

---

- [¿Cómo funciona?](#cómo-funciona)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Guía de Instalación](#guía-de-instalación)
    - [Paso 1: Obtener credenciales de Canvas](#paso-1-obtener-credenciales-de-canvas)
    - [Paso 2: Configurar tu Cliente de IA](#paso-2-configurar-tu-cliente-de-ia)
- [Configuración por Consola (CLI)](#configuración-por-consola-cli)
- [Herramientas y Recursos Soportados](#herramientas-y-recursos-soportados)
- [Desarrollo Local](#desarrollo-local)
- [Licencia](#licencia)

---

## ¿Cómo funciona?

Cuando utilizas este servidor, la comunicación fluye de la siguiente manera:

```mermaid
graph LR
    User([Usuario]) -->|Instrucción en Lenguaje Natural| AI["Asistente de IA (Claude)"]
    AI -->|Petición MCP| MCP["Canvas MCP Server"]
    MCP -->|API REST - HTTPS| Canvas["Canvas LMS"]
    Canvas -->|Respuesta| MCP
    MCP -->|Datos procesados| AI
    AI -->|Respuesta amigable| User
```

1. **Tú le pides algo al asistente** (por ejemplo: _"Crea una tarea para el próximo viernes"_).
2. **El asistente detecta la intención** y se comunica con el **Canvas MCP Server** enviándole los parámetros necesarios.
3. **El servidor realiza la llamada segura** a la API de Canvas.
4. **Canvas procesa la acción** y devuelve el resultado.
5. **El asistente te confirma el éxito de la operación** en lenguaje natural.

---

## Ejemplos de Uso

Aquí tienes algunos ejemplos de consultas y acciones reales que puedes pedirle a tu asistente:

> [!TIP]
> **Ahorro de Tokens y Eficiencia:** Siempre que sea posible, especifica el ID o la URL directa de Canvas (por ejemplo, `https://[tu_institucion].instructure.com/courses/[codigo_curso]/assignments/[codigo_actividad]`) en tus instrucciones. Esto evita que la IA tenga que buscar y escanear todos tus recursos, lo que resulta en respuestas mucho más rápidas y un ahorro significativo de tokens.

### Para Consultar Información y Auditar Cursos

- _"¿Qué cursos tengo activos este semestre? Verifica si existen múltiples paralelos o secciones."_
- _"Muéstrame las entregas pendientes de calificar para la actividad 'Ensayo 1: Introducción a la Sociología' en Sociología 101."_
- _"¿Cuáles son los estudiantes registrados en el Grupo A de la clase de Química?"_
- _"Verifica si la tarea 'Propuesta de Proyecto' tiene una rúbrica activa asociada. Si es así, obtén sus criterios."_

### Para Administrar y Crear Contenido Académico

- _"Crea un nuevo módulo llamado 'Semana 1: Fundamentos' en mi curso."_
- _"Agrega un Subencabezado 'LECTURAS OBLIGATORIAS' dentro del módulo 'Semana 1' y enlaza la página del sílabo."_
- _"En mi curso de Negocios, crea una tarea llamada 'Estudio de Caso 1: Análisis de Mercado'. Agrega una tabla de instrucciones con columnas para Criterios, Requisitos y Puntaje."_

### Gestión de Calificaciones y Asistencia

- _"Para la tarea 'Estudio de Caso 1', busca a todos los estudiantes que no hayan entregado. Ponles un 0 de nota y agrégales el comentario: 'Actividad no entregada. Si tienes una justificación válida, por favor comunícate con el docente.'"_
- _"Califica la entrega de Juan en 'Ensayo 1' con un 90 basado en la rúbrica, y agrega un comentario: '¡Excelente trabajo! El análisis está muy bien estructurado, aunque podrías profundizar un poco más en las conclusiones. ¡Sigue así!'"_

---

## Guía de Instalación

Para guías detalladas paso a paso para todos los clientes de IA y editores soportados (Windsurf, Cline, Roo Code, Copilot, Continue, Zed, LibreChat, Custom GPTs), consulta [`llms-install.md`](llms-install.md).

### Paso 1: Obtener credenciales de Canvas

1. Inicia sesión en tu cuenta de **Canvas LMS**.
2. Dirígete a **Cuenta (Account)** > **Configuración (Settings)** en el menú lateral.
3. Baja hasta la sección **Integraciones Aprobadas (Approved Integrations)** y haz clic en **+ Nuevo token de acceso (+ New Access Token)**.
4. Escribe un propósito (ej. "Asistente Claude") y haz clic en **Generar token**.
5. Copia el token generado inmediatamente y guárdalo en un lugar seguro.

> [!IMPORTANT]
> También necesitarás el dominio de tu Canvas. Es la dirección web de tu escuela/universidad, por ejemplo: `miuniversidad.instructure.com`.

---

### Paso 2: Configurar tu Cliente de IA

#### Opción A: Claude Desktop (Aplicación de Escritorio)

1. Abre tu archivo de configuración de Claude Desktop:
    - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
    - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
2. Agrega la configuración del servidor Canvas bajo `mcpServers`:

```json
{
    "mcpServers": {
        "canvas": {
            "command": "npx",
            "args": ["-y", "@charlie.act7/canvas-mcp-server"],
            "env": {
                "CANVAS_API_TOKEN": "TU_TOKEN_DE_ACCESO_AQUÍ",
                "CANVAS_API_DOMAIN": "miuniversidad.instructure.com"
            }
        }
    }
}
```

#### Opción B: Claude Code (CLI)

```bash
claude mcp add canvas \
  --env CANVAS_API_TOKEN=TU_TOKEN_DE_ACCESO_AQUÍ \
  --env CANVAS_API_DOMAIN=miuniversidad.instructure.com \
  -- npx -y @charlie.act7/canvas-mcp-server@latest
```

---

## Configuración por Consola (CLI)

Si prefieres configurar las credenciales de manera local e interactiva en tu terminal para desarrollo, puedes ejecutar:

```bash
npx @charlie.act7/canvas-mcp-server config
```

---

## Herramientas y Recursos Soportados

<details>
<summary><b>Ver Lista Detallada de Herramientas y Recursos Soportados</b></summary>

### Lista de Herramientas

El servidor expone internamente 117 herramientas organizadas por categorías:

| Categoría                        | Herramientas Incluidas                                                     |
| -------------------------------- | -------------------------------------------------------------------------- |
| **Cursos (Courses)**             | Listar cursos, detalles del curso, configuración básica                    |
| **Módulos (Modules)**            | Listar y gestionar módulos del curso                                       |
| **Páginas (Pages)**              | Listar páginas de contenido, leer el HTML de una página                    |
| **Archivos (Files)**             | Listar archivos cargados en el curso                                       |
| **Anuncios (Announcements)**     | Listar y crear anuncios para el curso                                      |
| **Tareas (Assignments)**         | Listar, crear, actualizar tareas y modificar fechas de entrega masivamente |
| **Entregas (Submissions)**       | Ver entregas y archivos adjuntos de alumnos                                |
| **Calificaciones (Grading)**     | Calificar entregas de tareas, auditar notas del curso                      |
| **Exámenes (Quizzes)**           | Listar quizzes, gestionar preguntas y modificar fechas límite              |
| **Estudiantes (Students)**       | Roster de alumnos, progreso de aprendizaje y detalles                      |
| **Grupos (Groups)**              | Listar y gestionar grupos de estudiantes                                   |
| **Calendario (Calendar)**        | Listar y crear eventos o recordatorios en la agenda                        |
| **Rúbricas (Rubrics)**           | Crear y gestionar rúbricas de evaluación                                   |
| **Comunicación (Communication)** | Enviar mensajes directos, gestionar foros y discusiones                    |
| **Access Tokens**                | Gestión de tokens de API y auto-renovación                                 |

### Recursos MCP Soportados

Para clientes compatibles con recursos directos:

- `canvas://courses/{id}/readme` — Resumen general formateado de un curso.
- `canvas://courses/{id}/pages/{slug}` — Contenido HTML directo de páginas de Canvas.

</details>

---

## Desarrollo Local

1. **Instalar Dependencias:**
    ```bash
    npm install
    ```
2. **Compilar el Proyecto (TypeScript a JavaScript):**
    ```bash
    npm run build
    ```
3. **Ejecutar Servidor en Modo Stdio (MCP):**
    ```bash
    npm start
    ```
4. **Ejecutar Servidor HTTP con Documentación Swagger:**
    ```bash
    npm run start:http
    ```
    Visita `http://localhost:3000` para ver la interfaz de Swagger.

---

## Licencia

Este proyecto está bajo la licencia MIT. Creado por [Charlie Cárdenas Toledo](https://github.com/charlie-act7).
