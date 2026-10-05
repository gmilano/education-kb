---
industry: education
region: Global
updated: 2026-10-05
---

# `p387-shared-date-control` — la coincidencia de fecha NO es evidencia de fusión

**Pase 118 del 2026-10-05.** Control negativo que a `P381` le faltaba.

## El caso

`P381` (pase 117) cazó un par falso: **el nombre de un instrumento con la fecha de otro**, las dos
mitades reales y falso sólo el PAR. Este pase encontró el caso espejo:

| Instrumento | Emisor | Fecha | ¿Verificado? |
|---|---|---|---|
| *Framework Act* en vigor | **Corea del Sur** | **2026-01-22** | 🟢 sí |
| *Model AI Governance Framework for Agentic AI* publicado | **IMDA, Singapur** | **2026-01-22** | 🟢 sí — anunciado por la ministra **Josephine Teo** en el **WEF de Davos 2026** |

🟢 **La fecha compartida es REAL en los dos casos.** Dos instrumentos de dos jurisdicciones
distintas cayeron el mismo día porque **los dos se cronometraron contra Davos**, no porque una
fuente haya cruzado mitades.

## El hallazgo

🔴 **Un detector de `P381` que dispare por fecha repetida produce acá un FALSO POSITIVO.** Hay una
razón estructural para que las fechas se agrupen: **los reguladores cronometran los anuncios contra
el mismo calendario internacional** (Davos, cumbres, inicios de año fiscal).

**Regla de una línea:** un veredicto de **FUSIÓN** exige que, **para cada instrumento del par**,
emisor y fecha hayan sido verificados **por separado**. Sin verificación por instrumento el
veredicto es `UNVERIFIABLE`, **nunca** `FUSION`.

## El gate

- **emisores distintos** ⇒ `DISTINCT-INSTRUMENTS`, comparta o no la fecha. **La fecha nunca gana
  sobre el emisor.**
- **mismo emisor + nombres distintos + misma fecha** ⇒ `FUSION` (esto sí es lo que `P381` caza).
- **alguno sin verificar** ⇒ `UNVERIFIABLE`.

## Uso

```
python3 fusion_verdict.py pairs.json    # veredicto por par
python3 test_fusion_verdict.py          # 7/7
```

El primer caso de la suite es el control negativo real: Corea + Singapur ⇒ `DISTINCT-INSTRUMENTS`.

## Estado

🟢 **Implementado con suite de 7 casos, 7/7.**
