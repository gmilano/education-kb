---
industry: education
region: Global
updated: 2026-10-04
---

# `p276-provider-allowlist` — el conteo del pase 92 estaba acotado por su lista de nombres, y su "replicación" compartía el punto ciego

> Nuevo en el **pase 93 del 2026-10-04**. Corrige una cifra que el pase 92 publicó en los
> ocho archivos de contenido y en su tendencia **720** como *confirmada por segunda mano*.

## 🔴 La corrección, y lo que la hace grave

El pase 92 midió Chamilo con `p273-platform-provider-dir/sweep_provider_dir.sh` y publicó:

> *«`v3.0.0`, `v3.0.1`, `3.0`, `master` → **6** proveedores (OpenAI, DeepSeek, Gemini,
> Mistral, Grok, **+ Anthropic**)»*, matriz `0,0,5,5,6,6,6,6`.

Y lo celebró como réplica: *«sus **8** refs coinciden EXACTO con la medición manual […]
**segunda cifra de esta base confirmada por segunda mano**»*.

🔴 **Enumerado el directorio, en `v3.0.x` hay SIETE clases `*Provider.php`, no seis. La
séptima es `ClaudeProvider.php`.**

🔴 **Y la réplica no era independiente.** El script y la medición manual sondeaban la
**misma lista de nombres candidatos** —`OpenAi DeepSeek Gemini Mistral Grok Anthropic
Ollama`— y `Claude` **no estaba en ella**, mientras `Ollama` —que no existe en Chamilo— sí.
Las dos coincidieron porque compartían el punto ciego, no porque la cifra fuera correcta.

**P276**: *un conteo obtenido sondeando una lista de NOMBRES CANDIDATOS está acotado por la
lista, no por el repo. Dos canales que sondean la misma lista no se validan entre sí:
comparten su punto ciego. Un conteo sólo es un conteo si ENUMERA.*

🔵 **El pase 92 tenía razón en el método y lo aplicó a medias.** Su propio `P270` ya decía
que el nombre debía salir del listado del árbol y no de una conjetura (`OpenAi.php` → 404,
`OpenAiProvider.php` → 200). Lo cumplió para **hallar** los nombres y lo rompió para
**contarlos**: el bucle quedó escrito contra una lista fija.

⚠️ **Y el acierto de Moodle fue suerte del denominador:** enumerado `public/ai/provider/`
(ver `p275`), Moodle da **7** y son exactamente los 7 que el pase 92 sondeó. El punto ciego
existía en los dos barridos; sólo mordió donde un nombre caía fuera de la lista.

## El instrumento correcto no es el listado del directorio: es la ALLOWLIST

Enumerar el directorio corrige el conteo pero sigue siendo indirecto — un árbol puede traer
clases que la plataforma no registra. La respuesta a *«¿qué puede configurar un
administrador?»* está en `AiProviderFactory`, que **rechaza toda clave fuera de su mapa**:

```php
$possibleProviders = [ 'openai' => 'OpenAi', 'deepseek' => 'DeepSeek', 'grok' => 'Grok',
  'mistral' => 'Mistral', 'gemini' => 'Gemini', 'claude' => 'Claude',
  'anthropic' => 'Anthropic' ];
// ...
if (!isset($possibleProviders[$providerName])) {
    error_log('[AI] Unsupported provider in config: "'.$providerName.'". Skipping.');
    continue;
}
```

Datos crudos: [`allowlist.2026-10-04.tsv`](allowlist.2026-10-04.tsv).

| ref | claves admitidas | n | vs. pase 92 |
|---|---|---|---|
| `v1.11.40`, `1.11.x` | — (no existe el factory) | **0** | 🟢 sostenido |
| `v2.0.0`, `2.0` | `openai deepseek grok mistral gemini` | **5** | 🟢 sostenido |
| `v3.0.0`, `v3.0.1`, `3.0`, `master` | **+ `claude` `anthropic`** | **7** | 🔴 **CORREGIDO (decía 6)** |

🟢 **La matriz correcta es `0,0,5,5,7,7,7,7`.** Y el cero de `1.11` **no** se publica por el
404 del factory: está confirmado por **enumeración** del árbol (`src/CoreBundle/AiProvider`
no existe en esa ref, y sus dos proveedores viven en `plugin/ai_helper/src/{openai,deepseek}/`
— 15 archivos listados). `P274` prohibía justo el atajo del 404.

## 🔵 Siete CLAVES, seis VENDORS: los dos números son distintos y los dos hacen falta

```php
final class AnthropicProvider extends ClaudeProvider {
    protected function getProviderKey(): string { return 'anthropic'; }
    protected function getProviderLabel(): string { return 'Anthropic'; }
}
```

`ClaudeProvider` es la implementación (y su `textApiUrl` por omisión es
`https://api.anthropic.com/v1/messages`, modelo `claude-sonnet-4-6`); `AnthropicProvider`
la **extiende** y sólo cambia la clave de configuración y la etiqueta.

🔴 **Así que el `6` del pase 92 no era «6 clases»: era un conteo acotado por su lista que
coincide con el número de VENDORS por casualidad.** Las dos cifras correctas son:

- **7 claves configurables** (lo que un administrador puede poner en el JSON)
- **6 vendors distintos** (`claude` y `anthropic` pegan al mismo endpoint)

**El eje necesita las dos columnas.** Para una propuesta: *«Chamilo 3 soporta 7 opciones de
proveedor»* es cierto y *«soporta 7 modelos de 7 empresas»* es falso.

## 🔴 P277 — la superficie de CAPACIDAD no es uniforme, y ahí se cae el "swap de proveedor"

Cada clase declara qué tipos de servicio implementa, y el factory sólo registra un
(proveedor, tipo) si la clase satisface la interfaz de ese tipo.
Datos crudos: [`capability-v3.0.1.2026-10-04.tsv`](capability-v3.0.1.2026-10-04.tsv).

| clave | clase | text | image | video | document | document_process | tipos |
|---|---|---|---|---|---|---|---|
| `openai` | `OpenAiProvider` | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | **5 / 5** |
| `grok` | `GrokProvider` | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 4 / 5 |
| `gemini` | `GeminiProvider` | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 4 / 5 |
| `deepseek` | `DeepSeekProvider` | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 2 / 5 |
| `mistral` | `MistralProvider` | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 2 / 5 |
| `claude` | `ClaudeProvider` | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 2 / 5 |
| `anthropic` | `AnthropicProvider` (hereda) | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 2 / 5 |

**P277**: *el conjunto de proveedores y el conjunto de CAPACIDADES por proveedor son dos
mediciones distintas. Un «swap de proveedor» es gratis sólo en los tipos que las dos clases
implementan; en los demás el swap es un desarrollo.*

🔴 **Lo que esto le hace a la afirmación «Chamilo es intercambiable de proveedor»:** es
verdadera en **text** y **document** (7 de 7), se cae a **3 de 7** en imagen y video, y a
**1 de 7** en `document_process` — **sólo OpenAI**. Un cliente que compró *«cambiamos de
proveedor cuando quieras»* y usa procesamiento de documentos **no tiene a dónde cambiar**.

🔵 **Y el default no se elige: lo decide el ORDEN del JSON.**
`$this->defaultProvider = array_key_first($config) ?? 'openai'` — la primera clave del
ajuste `ai_helpers.ai_providers` gana. Además un tipo sólo se habilita si está
**explícitamente presente** en la config de ese proveedor, y si la clase no satisface su
interfaz el factory lo **descarta con `error_log` y sigue**: la capacidad se pierde en
silencio, sin error visible en la interfaz.

## Dos aristas de herencia, y sin las dos el veredicto sale al revés

🔴 **Herencia de CLASE.** `AnthropicProvider` no declara `implements` propio. Un lector de
`implements` que no resuelva `extends` publicaría *«anthropic: cero capacidades»*.

🔴 **Herencia de INTERFAZ.** **Ningún** proveedor declara `AiVideoProviderInterface`, que es
la que el factory exige para el tipo `video`. Los tres que hacen video declaran
`AiVideoJobProviderInterface`, y medido en el payload:
`interface AiVideoJobProviderInterface extends AiVideoProviderInterface`. Comparando nombres
literalmente el veredicto sería *«cero proveedores de video»* **teniendo tres**.

⚠️ **Y una interfaz declarada no es un tipo registrable.** `OpenAiProvider` declara **seis**
interfaces pero llega a **cinco** tipos: `AiSearchMediaTextProviderInterface` no está en el
mapa `$typeInterface`, así que no habilita ningún (proveedor, tipo). *«Seis interfaces»* no
se publica como *«seis capacidades»*.

## Suites y canal

```
python3 test_allowlist.py    # 12/12 verdes
python3 extract_allowlist.py AiProviderFactory.php
python3 capability.py OpenAiProvider.php DeepSeekProvider.php ...
```

🟢 La suite fija el defecto del pase 92 como caso de prueba
(`test_el_punto_ciego_del_pase_92`) para que la corrección no se pierda, y fija el defecto
que el propio parser podía cometer: `$possibleProviders` tiene vecinos sintácticamente
idénticos (`$typeSuffix`, `$typeInterface`), y un regex sin corte en el primer `];`
devolvería `text` / `image` / `video` **como si fueran proveedores** — tres entidades
inventadas. El extractor corta en el bloque y el test lo verifica.

⚠️ **Cota:** el payload se lee de `raw.githubusercontent.com` por ref exacta. Mide lo que
el repo declara, no lo que una instalación tiene configurado; qué proveedores están
*activos* es propiedad del ajuste `ai_helpers.ai_providers` de cada institución y no se
puede leer del repo.
