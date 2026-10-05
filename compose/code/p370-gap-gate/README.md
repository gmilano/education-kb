---
industry: education
region: Global
updated: 2026-10-05
---

# `p370-gap-gate/` — la compuerta simétrica: un hueco DECLARADO

**Qué prueba:** que un hueco que esta base declara sobre su propio contenido («LATAM: CERO
repositorios») se pueda **falsar contra el índice propio**, y que un hueco de **CANAL**
(«este canal no encuentra código de LATAM») **no** quede marcado por filas del índice.

## Por qué existe, y es un defecto de esta base que vivió 15 pases

`p311-duplicate-alta-gate/` existe desde el pase 100 porque un ALTA estaba por publicarse
sobre piezas que la base YA TENÍA. Contesta **«¿esto ya está acá?»** para lo que ENTRA.

🔴 **Nada contestaba la pregunta simétrica para lo que se declara AUSENTE.** Un hueco es
una afirmación sobre el CONTENIDO PROPIO —igual que un alta— y por lo tanto es falsable
contra el índice propio. Se publicaba sin control, y se re-publicaba como **racha**.

Las dos instancias que encontró el pase 115, en archivos y ejes distintos:

| Lo declarado | Dónde | Lo que la base ya tenía |
|---|---|---|
| «**CERO repositorios de origen LATAM**», 4º pase consecutivo | `intel/market.md:11`, `:179` | **12 repos UBICADOS en LATAM** en el índice propio, entre ellos `LabSirius/TutorIA` (**MIT**, Universidad Tecnológica de Pereira, financiado por el **SNCTI** colombiano, marcado **ACTIVO** por esta misma base) y `JOSETRA44/DUTIC-mcp`, cuya propia fila dice ser «*la primera puerta de LMS LATAM con licencia verificada de esta KB*» |
| «la capa de evaluación pedagógica es `pedagogy-benchmark`, **12 estrellas**» | pase 114 | `eth-lre/mathtutorbench` (**43 ★**, CC BY 4.0, ETH Zurich + CU Boulder, EMNLP 2025 oral) en `repos/foundations.md:4262` **desde el pase 4** |

## La discriminación que lo hace una compuerta y no un contador de «CERO»

El pase 113 escribió su hueco **con el alcance puesto** —«*no se publica como “LATAM no
produce código” — se publica como lo que es: **este canal no encuentra código de LATAM***»—
y hasta nombró una pieza LATAM propia en la misma oración. El **titular** del pase 114
conservó el número y soltó el alcance («*la capa de CÓDIGO de LATAM sigue abierta*»),
mientras el **ledger del mismo pase** (`:179`) sí lo mantuvo.

🔵 Por eso el caso **obligatorio** de la suite es que las dos oraciones reales del árbol
salgan con veredicto **OPUESTO**, y que el titular y el ledger del **mismo pase** también
divergan. Si el gate marcara las tres, sería un contador de la palabra «CERO».

## Invocación y cifras

| Qué | Invocación | Hoy |
|---|---|---|
| la suite (corre **sin** el corpus; las fixtures son líneas reales del árbol) | `python3 test_gap_gate.py` | 🟢 **27/27** |
| el barrido de huecos declarados del árbol | `python3 gap_gate.py --sweep ../../..` | 🔴 **2 `CONTRADICHO`** · ⚠️ **27 `NO-CLAIM`** de **29** con región |

🔴 **El resultado que manda no son los 2 contradichos: son los 27 `NO-CLAIM`.** De 29
huecos declarados con región, **27 no traen ningún marcador de alcance**, así que esta base
no puede distinguir sus huecos de CANAL de sus huecos de ÍNDICE — y un hueco sin alcance no
es auditable ni a favor ni en contra.

🔴 **Segundo límite, y lo encontró la PUBLICACIÓN de este mismo pase: el barrido no distingue
una AFIRMACIÓN de una CITA de esa afirmación.** Medido antes de publicar: **2 `CONTRADICHO`
de 29**. Medido después, con las secciones del pase 115 ya escritas: **4 de 37** — y las 2
nuevas son **este pase citando el hueco refutado para explicarlo**. ⚠️ **El defecto sigue
siendo 2; el delta es el instrumento midiéndose a sí mismo.** Es exactamente la clase de
META-MENCIÓN que `p351-star-digit-sweep/` tuvo que aprender a clasificar, reaparecida en un
instrumento nuevo — así que la cifra citable es **la de antes de publicar**, y la de después
necesita el clasificador de citas que este barrido todavía no tiene.

⚠️ **Tercer límite, de granularidad:** su unidad es la **oración**, y un calificador que vive
en la oración SIGUIENTE le es invisible. Por eso el
ledger del pase 114 sale `CONTRADICHO` en el barrido y `SOSTENIDO` en la suite, que lee el
párrafo completo. **La suite es la lectura autoritativa; el `2` del barrido es cota
superior.**

## Tres formas de nombrar una región, y sólo una ubica

`placed_in()` separa la UBICACIÓN de la MENCIÓN, porque las tres aparecen en filas reales:

- 🟢 **ubicación** — `| … | 🟢 **LATAM** (Brasil) |`: la región encabeza la celda.
- 🔴 **mercado** — `fuerte en LATAM y EMEA hispanohablante` (`chamilo-lms`): es dónde se
  USA, no de dónde es (**P368**).
- 🔴 **prosa del pase** — `el primer alta LATAM de esta KB en ocho pases`.

Medido: **12 ubicados** / **5 que sólo mencionan**, de 17 slugs con «LATAM» en su fila.
⚠️ El piso es **12 y no 13** por el tope de 140 caracteres de celda, que descarta la
ubicación —legítima— de `DaviPac/Classroom-mcp`, cuya celda es larga porque documenta su
propio método (`TIMEZONE=America/Recife`, indicio de CONFIGURACIÓN y no antropónimo).

## La tercera pregunta de región

`lib/region.py` documenta **dos** contratos opuestos (VALIDADOR de campo, DETECTOR de
celda) y los dos presuponen un portador **delimitado**. Sobre la oración `La capa de CODIGO
de LATAM sigue abierta` devuelve `set()` con los **dos** valores de `strict`, porque la
oración no es una celda.

🔴 Y el detector de celda, en **su** contrato (`strict=True`, su default), **no ve la fila
real de `TutorIA`**: la celda mezcla región con atribución y la rechaza por residuo. Usarlo
acá habría hecho que el gate **SOSTENGA el hueco falso**, coincidiendo con el pase 114 por
el motivo contrario — falso negativo del instrumento. Está afirmado en
`TestFalsoNegativoDelDetectorDeCelda`.

🔵 Así que `region_in_prose()` se declara como **tercera** pregunta en vez de estirar una de
las dos con un argumento no default, que es el defecto que **P265**/**P266** ya pagaron.
