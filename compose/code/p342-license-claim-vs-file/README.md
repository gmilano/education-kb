# `P342` / `P343` — una afirmacion de licencia no es una cesion, y un prefijo goloso roba digitos

Artefactos y suite del **pase 109 (2026-10-05)**. Las aserciones corren contra los TSV, no contra
la prosa de los `.md`.

## Que hay aca

| archivo | que es |
|---|---|
| `sweep_p340.sh` | la sonda de la **accion B**: 10 nombres de archivo de licencia × 2 ramas, contra `raw.githubusercontent.com`, con familia de licencia leida del payload |
| `p340-sweep.2026-10-05.tsv` | **300 filas** = 15 repos × 10 nombres × 2 ramas |
| `actionC.sh` | la sonda de la **accion C**: mide en UN MISMO ACTO bytes, `sha256` del archivo completo, `sha256` del archivo **sin su ultimo byte**, y el ultimo byte |
| `actionC-fingerprints.2026-10-05.tsv` | los 5 payloads alcanzables |
| `targets.txt` | el conjunto barrido, con el repo inventado de control |
| `test_p342.py` | **32 aserciones**, 0 fallos (`Python 3.11.15`) |

## El control negativo no es opcional

`gmilano/repo-inventado-p109-control` va **en el mismo lote** y da **20/20 · 404**. Sin el, un 404
de este barrido no se distingue de un canal caido — y este arbol ya tuvo pases enteros perdidos por
esa confusion (`P320`).

## `P342` — el hallazgo

`Javi111003/OlivIA-RAG` estaba publicado **dos veces** por esta base como *«sin licencia»*. Medido:

- `main/README.md` linea **3**: `[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)`
- `main/README.md` linea **50**: `├── LICENSE                  # Licencia del proyecto`
- el archivo: **404 en 20/20 sondas**, con `README.md` → 200 como testigo de alcance.

**El repo afirma MIT dos veces y no tiene el texto.** Eso no es «sin licencia» (descarte): es
`P314` — cesion a pedir por escrito al titular, **citando su propia afirmacion**. La pieza es
recuperable por una gestion, y es **LATAM con señal de primera mano** (tutor de ingreso a la
universidad cubana, curriculo cubano nombrado en el payload).

Se distingue de sus vecinos por **donde** vive la afirmacion:

| patron | donde | accion |
|---|---|---|
| `P340` | otra **ortografia** de archivo (`LICENCE`, `LICENSE.TXT`) | ampliar la lista de nombres — la cesion existe |
| `P314` | **palabra** en el cuerpo del README | pedir el texto |
| `P342` | **badge y/o entrada de arbol** que apunta a una **RUTA** inexistente | pedir la cesion citando la afirmacion |

## `P343` — el defecto de este pase, y su primer diagnostico tambien estaba mal

```
$ echo "bytes 35.121 B tail" | sed -E 's/^.*([0-9]{1,3}[.,][0-9]{3}) B.*$/[\1]/'
[5.121]
```

El primer enunciado culpo al cuantificador acotado `{1,3}`. **La suite lo refuto:** esa expresion,
sola, captura `35.121` entero. La causa real es el **prefijo goloso `^.*` sin frontera izquierda**
en el grupo de captura: `[0-9]{1,3}` se satisface con un digito, asi que al motor le alcanza con
cederle el `5`.

Y POSIX ERE no da con que frenarlo, las dos propiedades verificadas en la suite:

- **no hay cuantificadores perezosos**: `sed -E 's/^.*?X/[LAZY]/'` sobre `aXbXc` → `[LAZY]c`.
- **no hay *lookbehind***: `(?<![0-9])` → `sed: Invalid preceding regular expression`.

⇒ La correccion no es una asercion de frontera: hay que anclar por el separador o extraer con PCRE.

La **misma** corrida dejo una segunda instancia sin numeros: una fila cuyo campo «repo» es
`master/LICENSE.TXT` — una ruta —, porque el patron de slug tambien encaja en un camino.

🟢 **Lo que atrapo las dos fue la huella:** `93178a43d6d3` coincide exacto con el archivo de
35.121 B, imposible si fuera 30 KB mas chico. **El conteo de bytes y la huella son redundantes solo
cuando los dos estan bien.**

## Correr

```sh
python3 test_p342.py            # 32 aserciones
bash sweep_p340.sh out.tsv targets.txt
bash actionC.sh < cTargets.tsv  # (repo<TAB>rama/ruta por linea)
```
