---
industry: education
region: Global
updated: 2026-10-05
---

# `p386-pristine-dedup-gate` — con licencia prístina, el fingerprint vale 0 bits de procedencia

**Pase 118 del 2026-10-05.** Invalida el deduplicador que el propio `P379` (pase 117) había
propuesto: el par (`sha256` de `LICENSE`, titular).

## El defecto, medido

| Repo | ★ | Qué es | Licencia |
|---|---|---|---|
| `buriro-ezekia/mwalimulens-agent` | 0 | Agente de evidencia longitudinal de aprendizaje (EMEA/África) | Apache-2.0 |
| `mazhar266/fedena` | **5** | **ERP escolar** / gestión de campus (Ruby on Rails) | Apache-2.0 |
| `webtech-network/autograder` | **61** | **Autocorrector** con rúbrica, sandbox y GitHub Actions | Apache-2.0 |

🔴 **Los tres comparten `sha256:c71d239df917` y no comparten NADA más.** No hay fork, no hay
linaje, no hay titular común: hay un `LICENSE` de Apache-2.0 que son **11.357 B fijos sin el nombre
del titular adentro**. Esta base ya los tenía etiquetados `NOT-APPLICABLE` por `P184`.

🔴 **Por qué rompe el deduplicador:** con licencia prístina el par se vuelve
**(constante, constante)** — `c71d239df917` + `NOT-APPLICABLE` — así que deduplicar por ese par
**fusiona en UNA entidad a todos los proyectos Apache-2.0 no emparentados del estante.** El mismo
patrón aparece con GPL-3.0.

## El gate

1. Leer el `LICENSE` de la **rama por defecto** (`P269`: el conjunto es propiedad del par
   *(repo, ref)*).
2. Detectar boilerplate prístino por tamaño conocido (Apache-2.0 = **11.357 B**, GPL-3.0 =
   **35.187 B**, GPL-2.0 = **18.092 B**, MPL-2.0 = **7.651 B**) **y** titular ausente.
3. 🔴 **Si el titular está AUSENTE, el deduplicador se ABSTIENE.** No fusionar, no contar linaje,
   no inferir fork.
4. Si el titular está **PRESENTE**, deduplicar por (`sha256`, titular) — ahí sí transporta linaje
   (confirmado en las familias `canvas-mcp`, `purdue-mcp` y `ai-tutor`).

**Regla de una línea:** el hash del `LICENSE` responde *«¿qué licencia es?»* y **no** responde
*«¿de quién viene?»*.

## Alcance, y es mayor de lo que parece

⚠️ **Apache-2.0 es la licencia que el comprador público de EMEA prefiere.** En ese terreno el
fingerprint de licencia **no prueba procedencia**: hay que probarla por árbol de archivos y
encabezados de fuente. En una *due diligence* de plataforma, este paso no es opcional.

## Uso

```
python3 dedup_gate.py rows.json      # agrupa, o se abstiene
python3 test_dedup_gate.py           # 10/10
```

La suite incluye el **control negativo**: el par ingenuo de `P379` **sí** funde los 3 repos ajenos,
y el gate **no**.

## Estado

🟢 **Implementado con suite de 10 casos, 10/10.**
