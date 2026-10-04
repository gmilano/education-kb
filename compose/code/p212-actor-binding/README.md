---
industry: education
region: Global
updated: 2026-10-04
---

# P212 — ¿De dónde sale el ACTOR? El eje ortogonal a la escalera del pase 71 (pase 72 del 2026-10-03)

**De dónde sale.** El pase 71 construyó la escalera de cuatro peldaños de la **compuerta de
escritura** (**P207**) y escribió su propia cota sobre `nitsuah/bb-mcp`: *«la política se hace
cumplir, la IDENTIDAD no se autentica»*. **Esa cota no es un defecto de una pieza: es un SEGUNDO
EJE.** La compuerta dice qué se niega el servidor a **hacer**; el *actor binding* dice **para
quién** se lo niega. Una tabla de política evaluada contra un actor que el llamador **declara** es
una tabla de política evaluada contra una entrada auto-declarada.

**Peldaños, de más fuerte a más débil.** El peldaño se lee del **código** o del contrato de
configuración del proyecto, nunca de una afirmación del README:

| | Clase | Qué significa |
|---|---|---|
| **A1** | `ACTOR-FROM-UPSTREAM-SESSION` | el actor es el dueño de la credencial guardada; **la plataforma upstream decide sus derechos** y el llamador no puede nombrar otro actor |
| **A2** | `ACTOR-FROM-LOCAL-CONFIG` | declarado al desplegar, **fijado del lado del servidor**, y un valor en conflicto **en la llamada se rechaza** |
| **A3** | `ACTOR-FROM-CALL-ARGUMENT` | el llamador dice quién es **en cada llamada** |
| **A4** | `NO-ACTOR-MODELLED` | una sola credencial de sitio hace todo; el **sujeto** es un argumento y **no hay actor** |

**Resultado (`result.2026-10-03.tsv`, 7 piezas, cada fila con el archivo y la línea que decide).**

**El sub-caso que no entra en un peldaño y se registra como tal:** `oliverhruby/edupage-mcp` usa
una credencial upstream **real** (fuerza de A1) pero **llega en una llamada a tool** y un segundo
tool —`switch_to_student`— **cambia el actor a mitad de sesión sin re-autenticar**. El peldaño
solo no describe la pieza; el *switch* sí.

**El hallazgo:** cruzado con la escalera de P207, en las tres piezas de arriba el orden está
**INVERTIDO** — peldaño 2 de compuerta (la política más rica) con A3 de actor (el más débil);
peldaño 3 de compuerta (el más débil que es código) con A1 de actor (el más fuerte). Es la misma
anti-correlación que el pase 55 midió sobre otro par de ejes.

```
./bind_axis.sh
```
