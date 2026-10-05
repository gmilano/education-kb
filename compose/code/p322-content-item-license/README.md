---
industry: education
region: Global
updated: 2026-10-05
---

# `p322-content-item-license` — la licencia de un item es un CAMPO, y un campo se puede llenar MAL

> Nuevo en el **pase 104 del 2026-10-05**. Corre la **accion C pre-registrada** (`OATutor`) y la
> confirma en la forma pero la **falsifica en la magnitud**: el eje de licencia por capa existe,
> y ademas el estante de contenido **se contradice con su propio README**.

## Que se pre-registro, y que salio

El pase 103 dejo escrito, como pista fundacional:

> *«`OATutor` — codigo MIT mas cinco semestres de material didactico bajo CC BY 4.0 […] los dos
> especimenes previos eran corpus de investigacion; este seria una PLATAFORMA desplegable. Un
> corpus `NC` limita un paper; **material didactico `CC BY` dentro de un producto limita el
> producto**.»*

Medido, con el arbol **enumerado** (`P275`) y cada cesion leida del **payload**:

| | pre-registrado | medido | veredicto |
|---|---|---|---|
| el codigo es **MIT** | si | 🟢 **MIT**, `LICENSE` 1.104 B, `(c) 2023 Zachary A. Pardos — CAHL research lab` | **CONFIRMADA** |
| el contenido es **CC BY 4.0** | si, en bloque | 🔴 **75,7 %** de los items; **24,3 % NO** | **FALSIFICADA en la magnitud** |
| es una **plataforma**, no un corpus | si | 🟢 LMS desplegable en GitHub Pages, middleware LTI para Canvas | **CONFIRMADA** |

## `P322` — el README dice «all content» y los campos del propio repo dicen que no

`OATutor-Content/README.md` declara, textual:

> *«All content in this repository is made available under the Creative Commons Attribution 4.0
> International (CC BY 4.0) license. Attribution is given within each json file, indicating the
> authoring organization and license for each hint, scaffold, and problem.»*

Son **dos** afirmaciones, y la segunda **falsifica** a la primera. Medidas **1.216 de 13.371**
problemas (muestreo **sistematico**, cada 11-esimo del arbol ordenado — reproducible, no aleatorio
sin semilla). Datos crudos: [`result-step11.2026-10-05.tsv`](result-step11.2026-10-05.tsv).

| clase | n | % | que es |
|---|---|---|---|
| `CC-BY-4.0` | 920 | **75,7 %** | la cesion que el README promete |
| `VACIA` | 235 | **19,3 %** | 🔴 campo presente y **vacio** |
| `OTRO` | 44 | **3,6 %** | 🔴 `CC4.0` (38) y `openstax` (6) — no nombran clausulas |
| `URL-NO-LICENCIA` | 17 | **1,4 %** | 🔴 el caso peor: una **URL que no es de licencia** |

🟢 **Dos muestras sistematicas independientes concuerdan**: con `STEP=33` (n=406) da 76,4 % / 19,9 %
/ 2,7 % / 1,0 %; con `STEP=11` (n=1.216) da 75,7 % / 19,3 % / 3,6 % / 1,4 %. Ver
[`result.2026-10-05.tsv`](result.2026-10-05.tsv).

🔴 **El caso peor, con nombre y archivo.** Los **17** `URL-NO-LICENCIA` estan **todos** en el mismo
curso (`Combined Data100 Worksheets`) y su campo `license` apunta a **PDFs de examenes y
solucionarios** de un curso de Berkeley, por ejemplo
`https://ds100.org/sp26/assets/exams/fa25/fa25_final_sol.pdf`. En **15 de 17** el valor es
**identico** al campo `oer` del mismo item: el mecanismo esta a la vista — **se copio la URL de
PROCEDENCIA al campo de CESION**. Un puntero a la fuente no es un permiso del titular (`P314`), y
este es el estado que **pasa cualquier compuerta que pregunte «hay algo?»** y no cede nada.

## `P323` — el borde de capa puede ser OTRO REPOSITORIO

🔴 **`OATutor` tiene un solo archivo de licencia fuera de `node_modules`: su `LICENSE` MIT, y es
CORRECTO para lo que cubre.** El contenido **no esta en ese repo**: entra por un **submodulo**.

```
[submodule "src/content-sources/oat"]
	path = src/content-sources/oatutor
	url = https://github.com/CAHLR/OATutor-Content
```

🔴 **Y `CAHLR/OATutor-Content` tiene CERO archivos de licencia en 51.929 rutas enumeradas** —
aserido por el arbol, y confirmado por un segundo canal (sonda de 7 nombres de licencia en la raiz,
404 en los 7). Su unica cesion vive en el **README** y en el **campo por item**.

**`P323`**: *el borde entre capa de codigo y capa de contenido puede no ser un directorio sino un
**submodulo**, y entonces un barrido que lee el `LICENSE` de la raiz del repo padre ve **MIT**, ve
un arbol **sin contenido** y ve **cero** archivos de licencia de contenido — y las tres lecturas son
ciertas y las tres enganan.* Es una topologia **nueva** frente a `P315` (licencia de datos en un
subdirectorio del mismo repo) y `P317` (corpus vendoreado sin declaracion).

🔵 **Por que cambia una cotizacion, y no es lo que la pista decia.** La pista del pase 103 suponia
el riesgo en el `CC BY` —atribucion dentro del producto del cliente—. `CC BY` es **barato** de
cumplir: se atribuye y listo. 🔴 **El riesgo medido es otro: el 24,3 % que NO dice `CC BY 4.0` es
material del que no se sabe que se puede hacer**, y en el curso de Data100 lo que hay en el campo
de licencia es el enlace al examen del que salio el problema.

## El hueco que NO se pudo cerrar, y queda pre-registrado

🔴 **Los vacios NO son ruido: se concentran por curso, y el patron apunta a la procedencia.**

| curso | n | `CC BY 4.0` | tasa |
|---|---|---|---|
| `Chemistry 1A Summer Content` | 11 | 0 | **0,0 %** |
| `Pre-Calculus Essentials (UC Berkeley Math 1B)` | 12 | 0 | **0,0 %** |
| `Combined Data100 Worksheets` | 17 | 0 | **0,0 %** (17 `URL-NO-LICENCIA`) |
| `Solid Foundations: Trigonometry` | 19 | 0 | **0,0 %** (15 `CC4.0`) |
| `Solid Foundations: Algebra` | 25 | 0 | **0,0 %** (23 `CC4.0`) |
| 🔴 `OpenStax: Calculus Volume 1` | 75 | 1 | **1,3 %** |
| `SJSU 1018` | 54 | 25 | 46,3 % |
| `OpenStax: University Physics` | 34 | 17 | 50,0 % |
| `OpenStax: Pre-Calculus` | 186 | 131 | 70,4 % |
| 🟢 `OpenStax: Introductory Stats` | 81 | 79 | 97,5 % |
| 🟢 `OpenStax: College Algebra` | 139 | 136 | 97,8 % |
| 🟢 `OpenStax: Intermediate Algebra` | 164 | 164 | **100 %** |
| 🟢 `OpenStax: Elementary Algebra` | 182 | 182 | **100 %** |

🟢 **Lo medido de primera mano:** el etiquetado es **casi perfecto** en los libros de OpenStax de
algebra y estadistica, y **se derrumba** en `Calculus Volume 1` y en todo lo que **no** es OpenStax.
**21 cursos, 5 de ellos con 0 %.**

🔴 **Lo que este pase NO pudo medir, y por eso no se publica como cesion:** `openstax.org` da
**403 por egress** con `curl` **y** con el fetcher, y `creativecommons.org` tambien. El canal
secundario (ediciones derivadas en Pressbooks, Clemson, UMN, UConn) dice de forma concordante que
**`Calculus Volume 1` es `CC BY-NC-SA 4.0`** mientras el resto de los libros citados son `CC BY 4.0`
— **pero eso viene de agregadores y de obras derivadas, no del titular, y `P314` ya le costo a esta
base publicar una licencia leida de un canal secundario.** Se dice en vez de callarse, y **no**
entra como cesion.

### 🔴 Accion pre-registrada para el pase 105, con su numero escrito ANTES de correrla

**Accion:** leer la licencia de los **7** libros que `OATutor-Content` nombra, **del titular**
(`openstax.org`), en cuanto un canal lo alcance.

**Prediccion falsable:** *`Calculus Volume 1` declarara en el titular una licencia **distinta** de
`CC BY 4.0` —se espera `CC BY-NC-SA 4.0`—, y sera el **unico** o uno de a lo sumo **dos** de los 7
en esa condicion.* Combinada con la tasa **ya medida** (1,3 %, la mas baja de los cursos OpenStax),
eso sostendria que **el campo vacio no es descuido sino la huella de una procedencia que no es
`CC BY 4.0`**.

🔵 **Que la refuta:** que `openstax.org` declare `CC BY 4.0` para `Calculus Volume 1`. Entonces la
correlacion medida en este pase es **ruido**, el vacio es descuido de autoria, y `P322` se queda
solo con la magnitud —que igual se sostiene sola—.

⚠️ **Lo que NO puede pasar es rellenar con el canal secundario:** si el egress sigue cerrado, se
dice *no se pudo correr*, como hizo el pase 96.

**Segunda accion:** resolver que significa **`CC4.0`** (38 items, cursos `Solid Foundations`). No
nombra clausulas: `CC BY 4.0` y `CC BY-NC-SA 4.0` son ambas «CC 4.0». **Prediccion: los 38 saldran
de una sola plantilla de autoria y resolveran a una unica familia.**

## Dos defectos de ESTE instrumento, encontrados por el instrumento mismo

Los dos son de la familia `P171`/`P319` —el instrumento reporta un estado que **no midio**— y los
dos nacieron en este pase. Se registran porque el barrido **ya habia emitido un TSV con ellos**.

🔴 **`E1` — la comilla en la ruta.** `xargs -I{}` **procesa comillas**, asi que
`content-pool/a343428l'hopital2/…` (la regla de **L'Hopital**) llegaba al `curl` **sin** la comilla.
Resultado: `404`, y **dos filas fantasma** con una ruta que **no existe en el arbol**. Arreglado con
`-d '\n'`. Control **C11**.

🔴 **`E2` — el codigo HTTP no se miraba.** `curl -s` sin comprobar el status entrega el **cuerpo de
error** como si fuera payload: el clasificador recibio `404: Not Found`. **Sobrevivio de
casualidad** —ese texto no parsea como JSON—; **un 404 que devolviera JSON se habria publicado como
dato**. Ahora se exige `200` y lo irrecuperable sale como `NO-LEIDA`, que es un estado del **canal**
y no una clase de licencia: no se mezcla en la tasa.

🟢 **El TSV publicado esta validado fila por fila**: 1.216 filas para 1.216 rutas muestreadas, cada
`path` verificado contra la muestra, 0 fantasmas, 0 faltantes. Una fila (`af69facexpolog12`) fue un
**transitorio de red** y se re-leyo **en serie** antes de entrar.

## Invocacion

```sh
python3 test_classify.py                                  # OFFLINE, 10/10
sh test_quoting.sh                                        # OFFLINE, 2/2 (C11)
WORK=/tmp/t322 STEP=33 bash sweep_items.sh    > result.$(date +%F).tsv        # serie
WORK=/tmp/t322 STEP=11 PAR=12 bash sweep_parallel.sh > result-step11.$(date +%F).tsv
```

**Hoy: 10/10 en `test_classify.py` + 2/2 en `test_quoting.sh`.** Los controles, y por que cada uno existe:

| Control | Que afirma | Por que |
|---|---|---|
| **C1** | la `CC BY 4.0` canonica se reconoce | el positivo conocido: sin el, ningun negativo vale |
| **C2** | `license: ""` es `VACIA`, **no** `CC BY` | contar el vacio como «hereda el README» es asumir lo que hay que medir |
| **C3** | una URL que no es de licencia es su propia clase | el caso peor: parece lleno y no cede nada |
| **C4** | **sin campo** != **campo vacio** | son dos estados distintos del dato y se cuentan aparte |
| **C5** | `by-nc-sa` **no** se lee como `CC BY` | `P312`: la compuerta se abria sobre las familias que existe para atrapar |
| **C6** | `CC BY 3.0` **no** es `CC BY 4.0` | la VERSION es parte de la cesion |
| **C7** | un nombre sin URL es cesion **mas debil**, aparte | no se mezcla con la canonica |
| **C8** | `license: null` es ausencia | `null` no es el string `'None'` |
| **C9** | 🔴 el **nombre de archivo** no es el dato | `…/a95836f13.1driverslicense.json` es un problema sobre una **licencia de conducir**: el barrido de RUTAS de este pase devolvio **8 falsos positivos** por esto |
| **C10** | una URL OSI no se promueve a cesion CC en silencio | alcance declarado del modulo |
| **C11** | 🔴 una ruta con **comilla** sobrevive al barrido — y el modo viejo **pierde** la comilla | es `E1` como aserto, en sus **dos** mitades: `C11b` reproduce la ruta fantasma exacta (`a343428lhopital2`). Sin el, el defecto es prosa (`test_quoting.sh`) |

## Limites declarados

- 🔴 **Es una MUESTRA, no un censo.** 1.216 de 13.371 (9,1 %). Las tasas **por curso** de los cursos
  chicos (`Matematik 4`, n=4; `Data 8`, n=9) **no sostienen un porcentaje**: se publican con su `n`
  al lado para que el lector no los lea como tasa.
- 🔴 **Solo el problema, no el paso ni la pista.** El arbol tiene **18.051** JSON de `tutoring/`
  (pistas y andamios) que este barrido **no** toca. El README promete atribucion *«for each hint,
  scaffold, and problem»*: **dos tercios de esa promesa quedan sin medir**.
- 🔴 **La licencia del campo no se valida contra el titular.** Que un item **diga** `CC BY 4.0` no
  prueba que OpenStax **ceda** eso para ese problema; es la accion pre-registrada de arriba.
- 🟢 **El denominador es de items, no de repos** (`P289`): 13.371 problemas en **un** repo.

---

## 🟢 CORRIDA en el pase 105 del 2026-10-05 — y el resultado es al reves de lo que esta seccion predijo

La accion pre-registrada de arriba **se corrio**. Instrumento:
[`../p326-titleholder-book-license/`](../p326-titleholder-book-license/).

| clausula pre-registrada aca | pedia | medido | veredicto |
|---|---|---|---|
| `Calculus Volume 1` ≠ `CC BY 4.0` en el titular | si | 🟢 **`CC BY-NC-SA 4.0`** | **CONFIRMADA** |
| el **unico** o uno de a lo sumo **dos** de los 7 | ≤ 2 | 🔴 **7 de las 8** ediciones citadas medibles son `NC-SA`; **11 de 13** libros del titular | **FALSIFICADA** |
| *«el campo vacio es la huella de una procedencia que no es `CC BY 4.0`»* | correlacion | 🔴 **no hay correlacion** | **FALSIFICADA** |
| unidad: *«los **7** libros»* | 7 | 🔴 **10** ediciones distintas citadas por los items | **denominador equivocado** |
| segunda accion: `CC4.0` resuelve a una sola familia | si | 🟢 **una sola plantilla** (`oer: OATutor.io`, autoria propia de OATutor) 🔴 **pero `CC4.0` no nombra clausulas, asi que la familia no resuelve** | **CONFIRMADA en la forma** |

🟢 **Y la prohibicion se respeto:** `openstax.org` sigue en **000**, y la cesion **no** se tomo de
agregadores. Se leyo del **payload del titular** en la organizacion `openstax` de GitHub
(`osbooks-*`), que es **otro canal del MISMO titular** (`P326-A`).

🟢 **El muestreo sistematico de este instrumento queda VALIDADO por el censo** de los 13.371
problemas: **76,4 / 19,0 / 3,4 / 1,2 %** contra **75,7 / 19,3 / 3,6 / 1,4 %** con `STEP=11`.
🔴 **Lo que le faltaba a este instrumento no era precision: era el segundo campo.** `oer` dice
**quien es el titular**, y sin el, *«el campo dice `CC BY 4.0`»* no se puede contrastar con nada —
**8.312 items (62,2 %) lo dicen contra un titular que cede `NC-SA`**. Ver **`P326`** y la receta
**`R-105-CESION-CONTRA-TITULAR`**, que **invierte** a `R-104-CAPA-DE-CONTENIDO`.

⚠️ **Correccion de conteo de este archivo:** publicaba **18.051** JSON de `tutoring/` sin medir; la
enumeracion del arbol da **18.054**.
