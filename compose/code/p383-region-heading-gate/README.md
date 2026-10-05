---
industry: education
region: Global
updated: 2026-10-05
---

# `p383-region-heading-gate` — gatear los ENCABEZADOS, que es donde el compilador infiere el tipo

**Pase 117 del 2026-10-05.** Tercer gate de esta base: `p311` gatea **altas**, `p370-gap-gate` gatea
**huecos declarados**, y nada gateaba los **encabezados**.

## Qué mide

El encargo es explícito: las oportunidades van bajo **un solo** `## Opportunities by region`, con
**un `###` por región**, y `region` es vocabulario **cerrado**:
`North America | EMEA | APAC | LATAM | Global`.

Medición sobre `intel/market.md` al abrir el pase 117:

| Medición | Valor |
|---|---|
| Bloques `## Opportunities by region` | **27** (el encargo pide 1) |
| Bloques que cubren las 4 regiones | **27 / 27** ✅ |
| `### North America` / `EMEA` / `APAC` / `LATAM` | **27 cada uno** ✅ |
| Secciones sólo-LATAM | **0** ✅ |
| `region:` de frontmatter fuera de vocabulario (8 archivos) | **0** ✅ |
| 🔴 `###` **fuera de vocabulario** hermanos de las regiones | **24** |

## El hallazgo: el daño está en el NIVEL, no en el 27

Dentro de esos bloques hay **24 encabezados `###` que no son regiones** y que son **hermanos
sintácticos** de los que sí lo son. Ejemplos literales:

- `🔴 Brechas declaradas de este pase, por región`
- `🔵 Lo que las cuatro regiones dicen JUNTAS este pase, y no dice ninguna sola`
- `Agregado en el pase 43 del 2026-10-02 — el barrido regional **no** se agotó: …` (~180 caracteres)

Un compilador que aplique la regla natural «*todo `###` bajo `## Opportunities by region` es una
región*» no produce 4 entidades: produce **28**, y **24 son basura con emoji en el nombre**. Es la
misma familia del defecto que el encargo narra para `region:` («*cada variante se vuelve su propio
cubo y el filtro deja de funcionar*»), **un nivel más abajo**.

**La prueba en miniatura, dentro del propio listado:** aparecen `por región` **y** `por region`, con
y sin tilde, **1 vez cada una** ⇒ dos cubos para un concepto. El daño del vocabulario abierto, ya
materializado, a escala 2.

## El gate

Sobre cada archivo con un `## Opportunities by region`:

1. Localizar los bloques `## Opportunities by region`. **Si hay más de 1, reportarlo**, pero no es la
   falla bloqueante: la cobertura regional se sostiene en los 27.
2. Para cada bloque, listar sus `###` hijos.
3. **FALLA** todo `###` cuyo texto no sea exactamente uno de los 5 valores del vocabulario cerrado.
4. **FALLA** toda región del vocabulario que aparezca 0 veces en un bloque (cobertura incompleta).
5. **FALLA** toda sección sólo-LATAM (LATAM presente y ≥1 de las otras 3 ausente).

## Remedio, sin reescribir historia

La base es **append-only** por diseño, así que el remedio **no** es editar los 24 encabezados viejos.
Es:

- **de acá en adelante**, toda prosa que no sea una región va a `####` o a un `##` propio, nunca a un
  `###` dentro del bloque de oportunidades;
- el compilador lee como región **sólo** los `###` del vocabulario cerrado, y **descarta** el resto en
  vez de inferir.

**Regla de una línea:** el nivel de encabezado es un **contrato de tipo**, no una decisión de
estética. Si `###` significa «región», entonces nada que no sea una región puede ser `###`.

## Estado

🟢 **Medido este pase** (27 bloques, 24 instancias fuera de vocabulario, 27/27 de cobertura regional).
⚠️ Pre-registrado como regla para los pases siguientes; la verificación de que el pase 117 **no**
agregó instancias nuevas está en la validación de cierre de este pase.
