---
industry: education
region: Global
updated: 2026-10-05
---

# `p328-cession-narrowing` — la cesion de un OER se ESTRECHA entre ediciones

> Nuevo en el **pase 106**. Corre las tres acciones que el pase 105 pre-registro.

## Que pregunta contesta

Dos preguntas que esta base trataba como una:

1. **¿Que edicion cita un item?** — el campo `oer` del dato.
2. **¿Que cede el titular a ESA edicion?** — el `md:license` de su `collection.xml`, **en la ref
   correspondiente**.

El veredicto es la **comparacion**. Un item no puede ampliar lo que su titular otorga.

## El hallazgo

🔴 **De las 10 colecciones que existen con el MISMO `collection-id` en los dos refs de su
repositorio, 10 de 10 pasan de `CC BY 4.0` (`1e`) a `CC BY-NC-SA 4.0` (`main`). Cero
contraejemplos.** 22 colecciones medidas en `main`, **2** permisivas (`physics` `col12081`,
`statistics` `col30309`).

⚠️ **Por que no se veia: el slug CAMBIA de nombre entre ediciones** (`precalculus` →
`precalculus-2e`), asi que un barrido por slug ve dos obras distintas. **La identidad es el
`collection-id`** (`P289` en un campo nuevo).

## Invocaciones, con su cifra

| que prueba | invocacion | hoy |
|---|---|---|
| el veredicto, el estrechamiento y los controles negativos | `python3 test_verdict.py` | 🟢 **36/36** |
| cesion por `(coleccion, ref)` leida del payload del titular | `python3 sweep_osbooks.py osbooks-college-algebra-bundle …` | 🔵 **36 filas** · 🔴 **10 estrechan** |
| el censo del arbol del redistribuidor | `python3 census.py /ruta/a/OATutor-Content` | 🔴 **8.312 CONTRADICE** de **82.492** unidades |
| huella cruda vs normalizada (`P327`) | `python3 sweep_norm.py slugs.openstax.txt` | 🟢 **familias 9/9 iguales** · 🔴 **2 colapsos** |

🔵 **El canal se calibra antes de cualquier veredicto** (`P249`): si `raw.githubusercontent.com` no
da **200** a una URL buena **y 404** a una inventada, el barrido sale con `NO-CLAIM` y codigo 2.

## Los controles negativos que importan

- una coleccion que vive en **un solo** ref **no** estrecha nada;
- una cesion que **no cambia** no es estrechamiento;
- de `NC-SA` a `CC BY` es **ampliacion**, no estrechamiento (control de **direccion**);
- `by-nc-sa` **contiene** la subcadena `by` y **no** debe clasificar como `CC BY 4.0` (`P299`);
- un campo `license` **vacio** es **AUSENCIA**, no permiso → `SIN-DECLARAR`, nunca `CORRECTO`;
- sin cesion medida del titular **no hay veredicto**: `NO-CLAIM`, ni a favor ni en contra (`P253`);
- `CC4.0` **no nombra clausulas** ⇒ no resuelve ⇒ `NO-CLAIM`;
- las **dos** formas de URL de OpenStax (`/details/books/X` y `/books/X`) tienen que extraer la
  misma obra — el extractor del pase 105 perdia una.

## Datos versionados

| archivo | que es |
|---|---|
| `osbooks-cesion.tsv` | 36 filas: `(repo, ref, slug, collection-id, url, familia)` |
| `norm-openstax.2026-10-05.tsv` | huella cruda y normalizada de las 9 cesiones del titular |
| `norm-agentes.2026-10-05.tsv` | idem sobre los 69 slugs del cohorte de agentes |
| `censo.2026-10-05.txt` | el censo completo de las 82.492 unidades |

## Defecto propio corregido en este mismo pase (`P330`)

🔴 La v1 de `sweep_norm.py` capturaba con `subprocess.run(..., text=True)`, que aplica *universal
newlines* y convierte **CRLF → LF antes de hashear**: la columna «bytes crudos» **no era cruda**
(21.013 en vez de 21.442 B, o sea las **429** terminaciones de linea) y reportaba **0 colapsos** en
el cohorte donde el colapso es real. 🔵 **Lo delato una aritmetica que no cerraba, no un test
rojo.** Se captura en **binario**.

## Lo que este instrumento NO contesta

- la capa de **imagenes**: 2.443 `.gif` sin medir (accion A del pase 107);
- las **12.999** unidades con `oer` vacio, que no son sinteticas ni atribuidas (accion B del 107);
- la **familia** de una cesion a partir de su huella: eso lo contesta `lib/license_family.sh`
  por bloque de titulo (`P171`), **nunca el `sha256`** (`P329`).
