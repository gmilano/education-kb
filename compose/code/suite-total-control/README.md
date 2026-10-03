# `suite-total-control/` — la regla de P126, hecha ejecutable

**Qué prueba:** que un contador de aserciones **por vocabulario** (el instrumento casero que el
pase 55 escribió a mano) acierta en una suite que emite `PASS` y **se equivoca en una que emite
`ok`**, mientras el lector del **total propio** de la suite acierta en las dos.

**Por qué existe:** el pase 55 contó a mano las aserciones de `unitime-mcp-gate` y
`openedx-course-generator` —las dos únicas que entonces no publicaban su total— y el instrumento
casero produjo un falso positivo (**tendencia 313**, **P126**). El control positivo que lo habilitó
**sólo ejercitó suites que emiten `PASS`**, así que nunca tocó el caso donde el instrumento falla.
El pase 55 nombró el control que faltaba —*«una suite que emita `PASS` y otra que emita `ok`»*— y
esta carpeta es ese control.

**La afirmación central es NEGATIVA**, que es lo que le da poder:

| Instrumento | fixture A (`PASS`) | fixture B (`ok`) |
|---|---|---|
| contador por vocabulario (`^PASS`) | **3** ✅ | 🔴 **0** (declara 4) |
| lector del total propio | **3** ✅ | **4** ✅ |

🔴 **Un control que corra solamente el fixture A deja pasar el instrumento roto** — y eso es
exactamente lo que pasó. La suite lo afirma como aserto, no como prosa.

## Invocación

```sh
python3 test_control.py              # fixtures solamente — OFFLINE, sin red
python3 test_control.py --inventory  # + qué invocaciones de compose/code/ publican total propio
```

**Hoy: 10/10** con fixtures solamente. El modo `--inventory` corre las invocaciones reales del
repositorio y **declara las que todavía no publican un total propio** en vez de afirmar que todas
lo hacen; algunas intentan red y pueden quedar colgadas o negadas por egreso, así que el modo
`--inventory` **no** es el número publicable de esta carpeta.

## La regla que esta carpeta deja escrita

1. **Antes de escribir un instrumento a mano se corre el que este repositorio ya versiona**
   (`patterns-figure-audit/extract_figures.py`).
2. **Un control positivo sólo habilita un instrumento si ejercita el caso donde ese instrumento
   puede fallar.** Dos suites que comparten vocabulario no son dos casos: son el mismo caso dos veces.
3. **Una suite que no publica su propio total invita al instrumento casero.** Las dos que faltaban
   se corrigieron en el pase 56 y las dos reprodujeron su cifra contada a mano (**46** y **33**),
   lo que confirma que el defecto nunca estuvo en el número sino en cómo había que obtenerlo.
