---
industry: education
region: Global
updated: 2026-10-04
---

# Fixture de P267 — CONTROL POSITIVO del barrido de grafias

La tabla de abajo es una tabla regional legitima: su primera columna es de region y nombra
las cuatro. Pero **dos** de las cuatro estan escritas fuera del vocabulario cerrado, y el
detector de `p239` las normaliza sin reportarlas. Si `measure_variants.py` no encuentra
exactamente esas dos, el cero que publica sobre el arbol real no vale nada.

| Región | Dato |
|---|---|
| **North America** | grafia de vocabulario, con negrita: NO es hallazgo |
| **EMEA** | idem |
| **latam** | 🔴 hallazgo `CASO` |
| **North-America** | 🔴 hallazgo `SEPARADOR` |
| APAC | grafia exacta, sin markup: NO es hallazgo |
