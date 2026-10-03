---
industry: education
region: Global
updated: 2026-10-03
---

# `p191-spec-license-sweep` — el régimen de la capa de ESTÁNDARES se parte por PUBLICADOR × TIPO DE ARTEFACTO (acción 3 del pase 67, pase 68 del 2026-10-03)

Ejecuta la **acción 3 del pase 67**, que era *«la acción nueva y la de mayor consecuencia
comercial»*: barrer `SPEC-LICENSE` sobre la capa de estándares después de descubrir que
`1EdTech/openbadges-specification` cede la *Specification Document License* de IMS Global, que
**niega los derivados**.

## La hipótesis, y por qué CAE EN UNA TERCERA RAMA

La acción escribió dos ramas:

> *«si **MÁS DE UNA** de las 15 trae una licencia de documento que niega derivados, entonces
> `SPEC-LICENSE` es el régimen **DOMINANTE** de la capa de estándares […]; si **sólo ocurre en Open
> Badges**, es una propiedad de IMS/1EdTech y no de la capa.»*

🔴 **Medido: son DOS —`openbadges-specification` y `caliper-spec`—, así que por la letra de la
hipótesis gana la primera rama. Y la primera rama es FALSA.** Las dos que niegan derivados pertenecen
**al mismo publicador**, y los otros dos organismos de estándares medidos ceden **Apache-2.0 sobre el
documento mismo**. El reparto no tiene ni una excepción:

| Publicador | Tipo de artefacto | Régimen medido | n |
|---|---|---|---|
| 🔴 **1EdTech / IMS Global** | **documento de especificación** | **`SPEC-NO-DERIVATIVES` + `REGISTERED-USERS`** | **2** |
| 🟢 1EdTech / IMS Global | software del organismo | **Apache-2.0** | **4** |
| 🟢 **ADL · Ed-Fi Alliance** | **documento de especificación** | **Apache-2.0** | **2** |
| 🟢 Ed-Fi Alliance | software | Apache-2.0 | 1 (medido en la capa de paquete, **P190**) |

🔵 **La variable discriminante NO es *«ser un estándar»*: son DOS ejes, el PUBLICADOR y el TIPO DE
ARTEFACTO.** `1EdTech × documento` es la única celda cerrada de las cuatro. **El mismo organismo cede
su SOFTWARE bajo Apache-2.0** (OpenCASE, el validador de Open Badges, el validador de credenciales
digitales, la librería LTI 1.3), **y otro organismo cede su DOCUMENTO bajo Apache-2.0** — `xAPI-Spec`
es un repositorio de puros `.md` normativos, y es permisivo.

### 🔵 Y el defecto de método que esto deja escrito (**P194**)

⚠️ **Un umbral sobre un CONTEO no puede distinguir una propiedad de la CAPA de una propiedad del
PUBLICADOR cuando la muestra está desbalanceada por publicador.** La hipótesis preguntó *«¿más de
una?»* sobre 15 filas donde 1EdTech aporta la mayoría de los repos de especificación: *«más de una»*
estaba casi garantizado por la composición de la muestra, no por el régimen. 🟢 **La pregunta que sí
discrimina es la TABULACIÓN CRUZADA, y cuesta lo mismo.**

## La consecuencia comercial, que es la razón por la que la acción existía

🔴 **Sobre Open Badges y Caliper:** implementar contra el estándar **no pide permiso**; publicar *«la
versión del cliente»* del documento **no está concedido** y se tramita con el organismo.
🟢 **Sobre xAPI y Ed-Fi: un perfil derivado del documento SÍ se puede publicar**, con atribución
Apache-2.0 y sin trámite. ⚠️ **Por eso la frase *«la capa de estándares está cerrada»* —que esta KB
publicó en tres archivos tras el pase 67— es falsa para la mitad de la capa, y este pase la corrige.**

## 🔴 El hueco que aparece solo, y es de los que importan: xAPI 2.0 ya no vive en GitHub

⚠️ **`adlnet/xAPI-Spec` (952 ★, 403 forks, Apache-2.0, 11.525 B) es la versión 1.0.3 y su propio
README la declara VIEJA:** *«This is an old version of the specification found at 1.0.3. The current
version of the specification is xAPI 2.0.»* 🔴 **La versión vigente es **IEEE 9274.1.1-2023** y vive
en `https://opensource.ieee.org/xapi/xapi-base-standard-documentation` — un GitLab propio del IEEE,
fuera de GitHub.**

🔴 **Y este entorno no lo alcanza por ningún canal: `curl` devuelve `000` (conexión fallida) y
WebFetch devuelve `EGRESS_BLOCKED` explícito para `opensource.ieee.org`.** 🔵 **Lo que eso significa
para esta KB, y es el patrón **P195**: sus CUATRO instrumentos de licencia apuntan a
`raw.githubusercontent.com` —por repo (`p170`), por payload (`p172`), por registro (`p183`) y por
titular (`p184`/`p190`)—, así que un estándar que MIGRA fuera de GitHub se cae de todos los
denominadores a la vez, y se cae en silencio.** ⚠️ **La cesión Apache-2.0 que este barrido midió es la
del documento ARCHIVADO. Sobre la licencia del documento VIGENTE esta KB no tiene medición, y se
declara así en vez de heredar la del archivado.** (ADL anuncia xAPI 2.0 como *«the first open-source
standard in the history of IEEE»*, pero es **afirmación de la fuente, sin archivo leído** — **P107**.)

## El canal, medido este pase

| Canal | Resultado | Uso |
|---|---|---|
| `raw.githubusercontent.com/<slug>/HEAD/<path>` | 🟢 **200** | el probe de este instrumento |
| `api.github.com/repos/<slug>` | 🔴 **403** | bloqueado por el proxy de egress |
| `github.com/<slug>/tree/HEAD/` por `curl` | 🔴 **400** | bloqueado |
| `github.com/<slug>/tree/HEAD/` por **WebFetch** | 🟢 **200** | **el único listado de directorio abierto** |
| `opensource.ieee.org` | 🔴 **000 / EGRESS_BLOCKED** | hueco declarado |

⚠️ **Por eso la enumeración de subdirectorios de versión NO es scripteable acá:** se hizo con WebFetch
y su resultado está congelado en `targets.tsv`, que es la razón por la que la lista de objetivos es
DATO y no un glob. 🔵 **Y la enumeración rindió el dato que la acción no esperaba: los subdirectorios
de versión son una propiedad de UN repositorio.** `openbadges-specification` tiene `ob_v2p0`,
`ob_v2p1`, `ob_v3p0`; `caliper-spec`, `xAPI-Spec` y `Ed-Fi-Standard` **no tienen subdirectorio de
versión** y su licencia está en la raíz. ⚠️ **Así que *«en un repo de estándar la licencia es por
VERSIÓN»* (**P187**, pase 67) vale para Open Badges y no se generaliza a la capa.**

## 🔴 La separación que este instrumento hace y el del pase 67 no hacía

**`REPO-UNREACHABLE` ≠ `ABSENT-AT-THIS-NAME`.** Es la lección de **P187** aplicada al instrumento que
la descubrió: un 404 en un NOMBRE no es una ausencia de cesión. Antes de escribir una ausencia, el
barrido pregunta si el REPOSITORIO contesta (`README.md`). 🔴 **Rindió de entrada: `1EdTech/caliper-php`,
`IMSGlobal/caliper-python` y `Ed-Fi-Alliance-OSS/Ed-Fi-SDK-MCP` dan 404 también en el README — son
repos que no resuelven, no licencias faltantes**, y dos de los tres ya figuraban `UNREACHABLE` en
`p170`. ⚠️ **`Ed-Fi-SDK-MCP` es el caso interesante: el *slug* sale del campo `repository` del paquete
npm, y NO RESUELVE — mientras el artefacto publicado sí embarca Apache-2.0 (11.558 B, **P190**). La
cesión existe en el paquete y el repositorio que el paquete declara no existe.**

## Reproducir

```bash
cd compose/code/p191-spec-license-sweep
python3 test_classify.py              # 8/8
bash sweep_spec.sh targets.tsv > out.tsv
awk -F'\t' '$5==200{p=($1~/^(1EdTech|IMSGlobal)/)?"1EdTech/IMS":"otro"; print p"\t"$4"\t"$6}' out.tsv | sort | uniq -c
```

## Lo que NO mide, declarado

⚠️ **CLR, QTI, OneRoster y LTI no tienen repositorio de ESPECIFICACIÓN en GitHub.** Buscados en la
org (`github.com/orgs/1EdTech/repositories?q=spec`, el único listado abierto), sólo aparecen
`openbadges-specification` y `caliper-spec`. **Sus documentos viven en `standards.1edtech.org`, que
esta corrida no leyó.** 🔵 **Así que el veredicto `1EdTech × documento` está medido sobre **2** repos,
que son **todos los que la org publica en GitHub** — no sobre los 7 estándares que la vertical nombra.
La inferencia *«los otros cinco serán iguales»* es plausible y NO está medida, y se escribe así.**
⚠️ **Y las 15 filas de la vertical son en su mayoría librerías CLIENTE, no documentos: la capa
«estándares» de esta KB mezcla dos tipos de artefacto, que es justo el eje que este pase midió.**
