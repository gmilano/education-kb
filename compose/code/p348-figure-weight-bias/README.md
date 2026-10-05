---
industry: education
region: Global
updated: 2026-10-05
---

# `P348` — contar por FIGURA sobresamplea justo las unidades que no ceden

Artefactos y suite del **pase 111 (2026-10-05)**. Corren la **accion C** pre-registrada por el
pase 110, sobre el censo ya materializado de `CAHLR/OATutor-Content`
(sha `1925decc91567faf6203bdb41b9d52b14891426f`).

## El veredicto: REFUTADA, y por dos motivos que se apilan

| clausula pre-registrada por el pase 110 | pedia | medido | veredicto |
|---|---|---|---|
| *«la tasa `RESOLUBLE` sobre las 13.371 cae **por debajo** del 58,0 %»* | < 58,0 % | 🔴 **76,4 %** | **REFUTADA** |
| rama de refutacion: *«que suba o quede igual (±2 pp)»* | — | 🔸 **+18,4 pp** | **dispara** |
| el motivo previsto: *«las figuras viven en los problemas de OpenStax, que traen `CC BY 4.0`»* | — | 🔴 **al reves** | tener figura es predictor **NEGATIVO** |

## Y los dos numeros no eran comparables

El 58,0 % cuenta **archivos de figura** (2.443). El 76,4 % cuenta **problemas** (13.371). Puestos
en la misma unidad:

| conjunto | unidades | `RESOLUBLE` | tasa |
|---|---|---|---|
| corpus completo | 13.371 | 10.210 | 🟢 **76,4 %** |
| unidades **con** figura | 1.586 | 1.005 | 🔴 **63,4 %** |
| unidades **sin** figura | 11.785 | 9.205 | 🟢 **78,1 %** |
| *(el conteo del pase 110, por figura)* | *2.443 figuras* | *1.418* | *58,0 %* |

🔵 **Los 5,3 pp que separan 58,0 de 63,4 son FORMA DEL DENOMINADOR, no cesion.** Es `P344` otra
vez, un pase despues y en otra forma: ahi el denominador excluia los casos que importaban, aca
pesa de mas unos sobre otros.

## El mecanismo, medido y no supuesto

| clase de cesion de la unidad | unidades | figuras | figuras/unidad |
|---|---|---|---|
| `RESOLUBLE` | 1.005 | 1.418 | 1,411 |
| `AUSENTE` | 385 | 586 | 1,522 |
| `VERSION-SIN-VARIANTE` | 99 | 146 | 1,475 |
| 🔴 `NO-ES-CESION` | 97 | 293 | **3,021** |

**Factor de sesgo (no-resoluble / resoluble): 1,250.** Las unidades mal cedidas cargan **25,0 %
mas figuras por unidad**, y la PEOR cubeta —`NO-ES-CESION`, que es una URL de fuente y no concede
nada— carga **mas del doble**. Por eso el conteo ponderado por figura sale mas bajo: no mide peor
cesion, mide que lo mal cedido trae mas archivos.

## Lo que cambia para un presupuesto

🔴 **La tasa del corpus es 76,4 %, no 58,0 %.** Usar el 58,0 % como tasa del corpus —que es
exactamente lo que la pre-registracion queria concluir— **subestima la entregabilidad en
18,4 pp**. Y el enunciado commensurable sobre la capa de figura es **−13,0 pp contra el corpus**,
no −18,4.

🔵 **Dato lateral que acota la negociacion: los 10.210 `RESOLUBLE` llevan UN SOLO identificador,
`CC BY 4.0`.** No hay que negociar seis licencias: hay una. Y las dos cubetas sucias estan
separadas por lado: los **402** `VERSION-SIN-VARIANTE` son todos la cadena literal `CC4.0` y los
**402** caen del lado **NO-OPENSTAX**; los **54** `NO-RECONOCIDO` son todos la cadena `openstax`
y caen todos del lado **OPENSTAX**.

## Que hay aca

| archivo | que es |
|---|---|
| `sesgo.py` | el instrumento. **Reusa** `clasificar` de `p345-oer-four-forms` por import, no por copia |
| `censo-cesion.2026-10-05.tsv` | las **13.371** unidades con clase de cesion, figura si/no, n de figuras y lado |
| `resultado.2026-10-05.txt` | la corrida |
| `test_p348.py` | **21** aserciones, 0 fallos (`Python 3.11.15`) |

## El control que vuelve medible al instrumento

🟢 **Reproduce el 1.418 / 2.443 = 58,0 % del pase 110 AL ENTERO.** Sin eso, la comparacion seria
contra otro instrumento y el hallazgo no existiria. La suite lo exige
(`test_REPLICA_el_58_por_ciento_del_pase_110_AL_ENTERO`), y exige tambien que toda figura resuelva
a una unidad del censo: un hueco de JOIN saldria `AUSENTE` y se leeria como falta de cesion.
