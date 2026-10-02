---
industry: education
region: Global
updated: 2026-10-02
---

# `openedx-course-generator` — el plan de POSTs de un curso, con su número

**Escrito en el pase 45 del 2026-10-02 (acción 2, gap 94 CERRADO).** Cierra el costo de **P55**: convierte «cotizar la
generación de un curso en Open edX» en **un artefacto con cantidad de llamadas**, que es lo que se pone en una
propuesta. **Open edX no se levanta en ningún momento.**

## El número, para el outline de ejemplo

| Magnitud | Valor |
|---|---|
| Leer el curso | **1 llamada** — `GET /api/contentstore/v1/course_index/{course_id}` devuelve `course_structure`, el *outline* anidado completo |
| Escribir el curso | **17 llamadas** — un `POST /api/contentstore/v1/xblock/` por bloque |
| Total | **18** |
| Olas secuenciales | **4** = profundidad del outline (capítulo → secuencia → vertical → bloques) |
| Ola más ancha | **8 POSTs paralelizables** |

🔵 **La fórmula, que es lo transferible: `llamadas = 1 + bloques`, en `profundidad` olas secuenciales, y dentro de cada
ola los hermanos van en paralelo.** El encadenado `locator → parent_locator` obliga a la secuencia **entre niveles**, no
entre hermanos, porque el POST devuelve el `locator` del bloque nuevo y por eso el recorrido **no necesita un GET
extra**.

## 🔴 El hallazgo del pase: tres estatus para un mismo defecto, y sólo uno es el correcto

Medido sobre `openedx/edx-platform` @ `master` leyendo el código, no la documentación. Un cuerpo mal formado se reporta
de tres maneras distintas, y **dos mandan al operador al lugar equivocado**:

| Cuerpo | Respuesta del servidor | Por qué, con el sitio exacto |
|---|---|---|
| sin `parent_locator` | 🔴 **403** | `XblockViewSet.initial()` deriva `course_key` **del cuerpo crudo**; si falta, queda `None`, y `HasCourseAuthorAccess.has_permission` hace `if not course_key: return False` (`rest_api/v1/views/permissions.py:25`). **Un defecto de cuerpo se reporta como falla de autorización** |
| sin `category` | 🔴 **500** | `XblockSerializer` declara **todos** sus campos `required=False`, así que la validación pasa; después `_create_block_core` hace el subscript pelado `request.json["category"]` (`view_handlers.py:864`) |
| con un campo inesperado | 🟢 **400** | `XblockSerializer` extiende `StrictSerializer`, que lanza `ValidationError` por cada clave de más (`rest_api/serializers/common.py:40-49`) |

🔵 **Precisión que el pase 44 no tenía, y que cambia el diagnóstico:** `category` se lee **dos veces** —
`request.json.get("category")` en la línea 834, que alimenta el chequeo de permisos, y el subscript pelado en la 864—.
Así que un POST sin `category` **pasa el control de autorización** y revienta después. Y **`parent_locator` también es
un subscript pelado** (línea 832), pero no llega a ejecutarse: el 403 del `permission_class` lo frena antes.

🟢 **Y una corrección a favor del upstream, por lectura de primera mano:** el `create` del `v1` **sí** corre el
serializer — lleva `@validate_request_with_serializer` además de `@expect_json_in_class_view`
(`rest_api/v1/views/xblock.py:239-243`). El serializer **se ejecuta y es estricto con las claves de más**; lo que no
puede hacer es atrapar las dos claves que el handler exige, porque **las declara opcionales a las dos**.

**Consecuencia de diseño, y es la razón de ser de `validate_outline()`:** el cliente valida `parent_locator`,
`category`, el orden de niveles y la lista blanca de campos **antes de emitir cualquier cosa**. No es defensa en
profundidad: es que **dos de los tres estatus del servidor son diagnósticos falsos**.

## Qué hay

| Archivo | Qué es |
|---|---|
| `generate.py` | `validate_outline()` · `plan()` (olas con referencias simbólicas `$path`) · `cost()` · `execute()`. **Sólo stdlib.** |
| `stub.py` | El *stub* del endpoint. **No es un mock que dice sí:** reproduce los cuatro comportamientos leídos del árbol (400 / 403 / 500 / 200) y devuelve `locator` con la forma real `block-v1:<org>+<course>+<run>+type@<category>+block@<32 hex>`. |
| `outline.example.json` | Un curso de 2 módulos / 3 secuencias / 4 verticales / 8 componentes = 17 bloques. |
| `test_plan.py` | **33 aserciones.** |

## Cómo se corre

```
python3 generate.py [outline.json]   # imprime el costo y las olas
python3 test_plan.py                 # 33 aserciones; sale 0 si todas pasan
```

## Qué prueba

🟢 **Las tres cosas que la acción 2 pedía, por ejecución:**

1. **Ningún POST se emite antes de tener el `locator` de su padre** — verificado en el plan (los padres preceden a los
   hijos en el orden de olas) **y** en la reposición contra el *stub*, acumulando los locators realmente devueltos.
2. **Los hermanos se agrupan en lotes paralelizables** — cada ola contiene exactamente un nivel del outline, y **ninguna
   petición de una ola depende de otra de la misma ola**.
3. **Un POST sin `category` se rechaza en el cliente** — `validate_outline()` y `plan()` las dos levantan `OutlineError`
   antes de tocar el transporte, *porque el servidor devuelve 500 y no 400*.

🟢 **Y las que agregó la medición:** un cuerpo sin `parent_locator` se rechaza en el cliente (el servidor da 403); una
clave de más se rechaza en el cliente (el servidor da 400); un nivel fuera de orden se rechaza; y el *stub* **castiga
de verdad** los tres casos, con los tres estatus distintos, sin aceptar ninguno de los cuerpos malos.

## ⚠️ Qué NO prueba

- **El transporte es un *stub*.** No hay autenticación JWT, ni `course_key` real, ni `modulestore`. Lo medido es **la
  forma del plan y su costo**, que es la parte que se cotiza.
- **No valida `category` contra los XBlocks instalados.** No puede: en un curso **el servidor tampoco lo hace** —
  `XblockSerializer.category` es un `CharField(required=False)` **sin `choices`**, y el único enum del árbol
  (`["html","problem","video"]`) aplica **sólo** si el padre es un `LibraryUsageLocator`. La lista `LEAF_CATEGORIES` de
  `generate.py` es **una convención de esta KB**, no una restricción del upstream, y está declarada como tal.
- **No cubre el camino de *clipboard* ni el import de biblioteca v2**, que devuelven 4 y 5 claves en vez de 2.
