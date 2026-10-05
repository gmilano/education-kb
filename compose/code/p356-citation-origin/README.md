---
industry: education
region: Global
updated: 2026-10-05
---

# `P356` — las 21 citas colgadas de `P354`, repartidas por ORIGEN

Artefactos y suite del **pase 112 (2026-10-05)**. Corre la **accion D** pre-registrada por el
pase 111, que pedia clasificar cada colgada entre **anunciada y nunca escrita** (`P295`/`P297`) o
**error de numeracion**, y predijo **≥14** de la primera clase.

## Invocacion

```sh
python3 origin.py [raiz-del-kb]   # el reparto, con el archivo que define cada numero
python3 test_origin.py            # la suite: 16/16
```

## El resultado

| clase | cuantas | quienes |
|---|---|---|
| **ANUNCIADA** (deuda documental real) | 🔴 **15** | `P127`, `P128`, `P129`, `P130`, `P132`, `P133`, `P134`, `P135`, `P173`, `P174`, `P175`, `P240`, `P252`, `P282`, `P293` |
| **DEFINIDA-FUERA** | 🟢 **3** | `P245` (`agents/top.md`), `P279` (`repos/foundations.md`), `P281` (`agents/trending.md` + `intel/market.md`) |
| **INSTRUMENTO** (codigo y README propios) | 🟢 **3** | `P239`, `P280`, `P283` |
| **error de numeracion** | 🟢 **0** | — |

🟢 **CONFIRMADA en la letra: 15 ≥ 14.** 🔴 **Con un TERCER resultado que la pre-registracion no
admitia: 6 de las 21 no son deuda**, y la causa es del instrumento que las conto.

## El defecto de ALCANCE, medido

En `audit_patterns.py`, **`definitions()` lee un solo archivo** (`compose/patterns.md`) mientras
**`citations()` barre todos** los `**/*.md`. Un numero definido con **la misma convencion de
encabezado que el auditor ya reconoce**, pero en otro archivo, sale colgado y nada lo marca.

🔵 **Es distinto de `P354`:** ahi el ancla no reconocia una **ortografia**; aca el ancla es correcta
y lo que esta mal es el **conjunto de archivos** sobre el que se aplica. Ortografia contra
**alcance**. Familia del denominador: `P344`, `P351`, y esta.

## Los controles negativos, y por que estos

- **Un encabezado que MENCIONA un numero no lo DEFINE.** La primera medicion de este pase uso un
  `grep` con `[^0-9]*` antes del numero y leyo *«## Capa de escritura del lado DOCENTE — el agujero
  de P129, cerrado»* como definicion de `P129`: habria convertido **2 de las 21** en falsos
  `DEFINIDA-FUERA`. El arreglo fue **reusar las regex del propio auditor** (`P237`) y cambiar
  **solo** el conjunto de archivos.
- **Control positivo:** las cuatro convenciones reales (`## P142 —`, `` ### `P348` — ``,
  `## Receta P149 —`, rango `## P145—P148`) **si** definen.
- **Procedencia:** ninguno de los dos directorios de instrumento puede aportar una definicion al
  barrido. ⚠️ **La primera version de este control afirmaba `142 not in WHERE` y estaba MAL** —
  `P142` si esta definida, en `patterns.md`, y legitimamente: es el control positivo del propio
  auditor. El control correcto mira la **PROCEDENCIA**, no el numero. Es `P126` en su forma de
  siempre: el control medía otra cosa que la que decía.

## Lo que esta accion NO hace

⚠️ **Se detiene en CLASIFICAR.** No escribe ninguna de las 15 secciones faltantes: inventar la
definicion de un patron ajeno es **fabricar doctrina** (`P286`), y la suite verifica que no se
escribieron. La peor sigue siendo **`P135` — 84 citas en negrita, 0 definiciones** — y ahora se
sabe que es deuda *documental* y **no** un error de numeracion, que es lo que la accion existia
para decidir.
