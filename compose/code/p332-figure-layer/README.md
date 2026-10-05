---
industry: education
region: Global
updated: 2026-10-05
---

# `p332-figure-layer` — la capa de BINARIOS de un corpus OER, y la extension que miente

> Nuevo en el **pase 107**. Corre las tres acciones que el pase 106 pre-registro.

## Que preguntas contesta

Tres que esta base trataba como una sola, o como ninguna:

1. **¿Que formato tiene realmente un activo?** — la **firma de bytes**, no la extension (`P332`).
2. **¿De quien es una FIGURA?** — su `sha256` cruzado contra los arboles `media/` del titular, con
   el acierto desglosado **por obra citada** (`P334`).
3. **¿De que cuelga una unidad de `tutoring/` con `oer` vacio?** — del `oer` y el `license` de su
   **problema padre**.

Y una cuarta contra esta base misma: **¿que afirmaciones de identidad de licencia se apoyan en un
`sha256` sin nombrar la familia al lado?** (`P329`).

## Los hallazgos

🔴 **`P332` — la extension es falsa en 2.443 de 2.443.** Los archivos `.gif` de
`CAHLR/OATutor-Content` (`main`, sha `1925dec`) son **1.358 PNG · 938 JPEG · 147 WEBP · 0 GIF**
(**0,0 %** de cumplimiento). El `media/` del titular que se pudo abrir (`col30309`) tiene **706**
archivos y **cero** GIF: **un barrido por extension devuelve «0 solapamiento» con varianza cero
desde una premisa falsa. Por `sha256` devuelve 36.**

🔴 **`P334` — el titular de una figura vive en una obra distinta de la que el item cita.** Los
**36** aciertos byte-identicos citan `introductory-statistics` y sus bytes se publican en
`osbooks-statistics` (`col30309`). Benigno aqui —`col30309` es una de las dos colecciones
permisivas de `P328`— y grave como regla.

🟢 **La herencia implicita de cesion existe y es de 9.971 unidades.** De las **12.999** unidades de
`tutoring/` con `oer` vacio, **9.971 (76,7 %)** cuelgan de un problema que cita OpenStax — sobre un
umbral pre-registrado de 60 %. 🔴 **Y en 3.876 el padre tampoco declara cesion.**

🔴 **`P333` — una huella tomada por sustitucion de comando no es la huella del archivo.**
`fa4e32e5e622` / 1.083 B era el `LICENSE` de `bibo242/blackboard-mcp` **menos su salto final**; el
payload da **1.084 B / `d65abf96e389134e`**. 🟢 **La familia no se movio en 5 de 5 remediciones.**

## Invocaciones, con su cifra

| que prueba | invocacion | hoy |
|---|---|---|
| los controles de los tres instrumentos, sin red y sin corpus | `python3 test_p332.py` | 🟢 **27/27** |
| el formato REAL por firma de bytes (`P332`) | `python3 sniff_format.py RAIZ --ext .gif` | 🔴 **GIF 0 de 2.443 (0,0 %)** |
| el formato del arbol del titular | `python3 sniff_format.py .../osbooks-statistics/media` | 🔵 **706**: 499 JPEG · 206 PNG · 1 `OLE/CFB` |
| acciones A y B: figura ↔ cesion declarada, y `oer` vacio ↔ padre | `python3 measure.py RAIZ` | 🔵 **2.443** figuras · 🟢 **9.971/12.999 = 76,7 %** |
| el cruce por BYTES, por obra citada (`P334`) | `python3 intersect_media.py RAIZ DIR_MEDIA` | 🔴 **36 de 2.443 (1,47 %)**, **36/36 en una sola obra** |
| accion C: `P329` contra los `.md` de esta base | `python3 sweep_sha_claims.py .` | 🔵 **27 correctas** · 🔴 **43 en la clase** |
| accion C, segunda mitad: remedir la FAMILIA del payload | `sh remeasure_family.sh` | 🟢 **5 de 5 sin cambio de familia** · 🔴 **1 huella corregida** |

🔵 **El canal se calibra antes de cualquier veredicto** (`P249`): si `raw.githubusercontent.com` no
da **200** a una URL buena **y 404** a una inventada, el barrido sale con `NO-CLAIM` y codigo 2.
Lo mismo si el arbol no esta materializado.

## Los controles negativos que importan

- un **PNG llamado `.gif` sigue siendo PNG**: es el control que define el hallazgo;
- **`RIFF` solo NO es WEBP** — un WAV tambien empieza con `RIFF`: se exigen las **dos** anclas;
- una firma desconocida **no se adivina**: sale como `OTRO:<hex>`, nunca como el formato mas
  parecido;
- un `sha256` **inventado** no interseca; la interseccion de un lado consigo mismo da su propio
  tamano;
- las **dos** formas de URL de OpenStax (`/details/books/X` y `/books/X`) tienen que extraer la
  **misma** obra, y `precalculus` ≠ `precalculus-2e` (`P328`: la edicion es parte de la identidad);
- un `oer` **vacio** no se atribuye a nadie, y un dominio **parecido** (`notopenstax.example`) no
  cuenta como OpenStax;
- `by-nc-sa` **contiene** la subcadena `by` y **no** debe clasificar como `CC BY 4.0` (`P299`);
- un `license` **vacio** es **AUSENCIA**, no permiso → `SIN-DECLARAR`, nunca `CORRECTO`;
- 🔴 **un `sha256` NO es una familia de licencia** (`P329`): `familia("sha256:5385a26e…")` tiene que
  dar `NO-RESUELVE`;
- en la accion C, una linea con huella + verbo de identidad **+ familia nombrada** es la forma
  **CORRECTA** y debe salir de la clase — el control negativo esta adentro de la regla;
- quitar el **primer** byte da otra huella que quitar el **ultimo**: el defecto de `P333` es del
  salto final, no de «un byte cualquiera».

## Datos versionados

| archivo | que es |
|---|---|
| `accion-a-b.2026-10-05.tsv` | las 2.443 figuras con `(problema, ruta, clase de oer, familia)` + el cruce de la accion B |
| `interseccion-col30309.2026-10-05.tsv` | el acierto por obra citada y los **36** pares `(item, figura, obra, archivo del titular, sha256)` |
| `formato-gif.2026-10-05.txt` | el censo de formato de los 2.443 `.gif` |
| `formato-titular-col30309.2026-10-05.txt` | el censo de formato de los 706 `media/` del titular |

## Lo que este instrumento NO contesta

- **21 de las 22 colecciones** del titular: el clon **en lote** quedo denegado y el mismo clon
  **nombrado** paso (`P335`). Es la mitad del denominador y va a la accion A del pase 108.
- la **identidad perceptual**: una figura re-codificada (mismo dibujo, otro formato) **no** es
  byte-identica y este instrumento la cuenta como del redistribuidor. 🔵 **Las 1.117 repeticiones
  del corpus (2.443 archivos → 1.326 imagenes distintas) sugieren que el eje vale la pena.**
- los **455** items de titular no resuelto (`docs.google.com`, `drive.google.com`): el egress a
  Google Docs sigue sin medirse.
- la **familia** de una cesion a partir de su huella: eso lo contesta `lib/license_family.sh` por
  bloque de titulo (`P171`), **nunca el `sha256`** (`P329`).
- 🔴 **la diferencia entre PROSA y CERCA DE CODIGO**, y es una cota de `sweep_sha_claims.py` medida
  en el mismo pase que lo estrena: re-corrido **despues** de escribir el pase 107 da **88** archivos
  / **30** correctas / **44** en la clase, y la unica linea que el pase agrego a la clase es el
  bloque de codigo con el que `P333` muestra la forma MALA (`compose/patterns.md:221`). ⚠️ **Un
  ejemplo de lo que NO hay que hacer no es una afirmacion de identidad: es un falso positivo de la
  regla, y la regla no lo distingue.** 🔵 **Por eso la cifra publicada del pase 107 se midio contra
  el arbol de `HEAD` (87 `.md` / 27 / 43), antes de escribir una linea.**
