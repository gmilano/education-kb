---
industry: education
region: EMEA
updated: 2026-10-02
---

# El post-procesador que marca un paquete SCORM ya construido — gap 100, cerrado con código, **y corrige el gap 97**

**Pase 47 del 2026-10-02, acción 1.** El pase 46 probó dos cosas y dejó una sin medir: que el
marcador **es legal** dentro de `<metadata>` de un manifiesto SCORM (gap 97, *«a favor»*), y que
**el generador no lo puede emitir** porque `buildManifest`/`buildManifest12` de
`scorm-mcp-server` arman el manifiesto como **literal de cadena** sin parámetro de extensión
(gap 100). Esta carpeta es el tramo que faltaba entre *«esta KB tiene el componente»* y *«esta KB
marca un curso entregable»*, **sin tocar upstream**.

## 🔴 Lo que no estaba medido, y cambia la conclusión del pase 46

**El mismo generador emite DOS dialectos, y sus comodines no coinciden.** Medido con `grep` sobre
los dos esquemas que `scorm-mcp-server` empaqueta:

| Esquema | `grp.any` | Puntos de extensión |
|---|---|---|
| `schemas/imscp_v1p1.xsd` (SCORM 2004) | `processContents="lax"` | **9** |
| `schemas12/imscp_rootv1p1p2.xsd` (SCORM 1.2) | 🔴 **`processContents="strict"`** | **9** |

Bajo `strict` el validador **tiene que encontrar** una declaración global del elemento foráneo.
Un marcador en un *namespace* que nadie importó **no es «desconocido pero tolerado»: es
INVÁLIDO.** Verbatim de `xmllint`:

```
Element '{urn:globant:aiact:50-2}aiGenerated': No matching global element
declaration available, but demanded by the strict wildcard.
```

⚠️ **Así que el gap 97 queda correcto para 2004 y FALSO para 1.2**, y la frase *«el marcador DEBE
declarar su propio namespace»* era necesaria pero **no suficiente**. La condición completa:
**debe declarar su propio *namespace* Y, en SCORM 1.2, el conjunto de esquemas del validador debe
importar una declaración para él.** `aiact-50-2.xsd`, al lado de este archivo, es esa declaración.

## 🔴 Y el hallazgo que no es sobre el marcador: `scorm_validate` rechaza los metadatos del propio estándar

`src/validate.ts` arma el conjunto de esquemas de SCORM 1.2 con un `wrapper12.xsd` que importa
**dos** de los **tres** *namespaces* que el repo empaqueta en `schemas12/`: entran
`imscp_rootv1p1p2` y `adlcp_rootv1p2`, y **queda afuera `imsmd_rootv1p2p1`** —el esquema de
metadatos LOM, que está en el repo y nadie importa—. Consecuencia, medida:

| Caso (SCORM 1.2) | `wrapper12.xsd` como viene | + una línea de `import` |
|---|---|---|
| manifiesto base | 🟢 `validates` | 🟢 `validates` |
| `<m:aiGenerated>` foráneo | 🔴 `fails` | 🔴 `fails` (necesita **su** XSD) |
| `<m:aiGenerated>` + `aiact-50-2.xsd` importado | — | 🟢 **`validates`** |
| marcador en `<imsmd:lom><imsmd:classification>` | 🔴 **`fails`** | 🟢 **`validates`** |
| 🔴 **un paquete con SÓLO metadatos LOM estándar de SCORM 1.2** | 🔴 **`fails`** | 🟢 **`validates`** |

🔴 **La última fila es el *bug*, y no es nuestro marcador: es el modo canónico y documentado de
poner metadatos en un `imsmanifest.xml` de SCORM 1.2.** `scorm_validate` lo reporta
`schema-valid: failed` sobre un paquete perfectamente conforme. 🟢 **Y el arreglo es **una línea**
—`<xsd:import namespace="…imsmd_rootv1p2p1" schemaLocation="imsmd_rootv1p2p1.xsd"/>`— sobre un
esquema que el repo ya trae.** Queda anotado como **PR corto a upstream**, y es el segundo de los
dos que esta base le debe a `giacomomaria81/scorm-mcp-server`.

⚠️ **Lo que esto le cuesta a un estudio hoy:** un curso SCORM 1.2 marcado **o simplemente con
metadatos LOM** falla el `schema-valid` de la herramienta que esta KB recomienda para validarlo.
**La pieza no está rota; el validador sí**, y decirlo con el número adelante es la diferencia
entre un hallazgo y una sorpresa en la demo.

## Los dos portadores, y por qué hay dos

| | `CARRIER_FOREIGN` | `CARRIER_LOM` |
|---|---|---|
| Forma | `<m:aiGenerated value="true"><m:span start end/></m:aiGenerated>` | `<imsmd:lom><imsmd:classification>` con `purpose` + `keyword` |
| Tramos | 🟢 **tipados**, atributos enteros | ⚠️ **cadenas** (`ai-generated-span:67-131`): hay que parsear |
| XSD extra | no en 2004; **sí** en 1.2 | **ninguno** |
| 2004 como viene | 🟢 valida | 🟢 valida |
| 1.2 como viene | 🔴 falla | 🔴 falla (por el *bug* de arriba) |
| 1.2 con el arreglo de una línea | 🔴 falla igual | 🟢 **valida** |

🔵 **Por omisión: `foreign` en 2004, `lom` en 1.2** —el que valida contra el conjunto de esquemas
que cada dialecto realmente arma—. **Y el portador portátil es `lom`**, porque valida en 2004
**también**: si hace falta **una** forma para los dos dialectos, es ésa, y se paga en estructura.

## Las cuatro aserciones que pedía la acción, y dónde están

| | Qué pedía | Dónde |
|---|---|---|
| **A1** | el ZIP resultante sigue validando contra `imscp_v1p1.xsd` | `[A1] 2004 + foreign marker validates` |
| **A2** | el manifiesto **sin** marcador **también** validaba (control de que la prueba mide algo) | `[A2] control:` ×2, los dos dialectos |
| **A3** | **re-inyectar es idempotente** | `[A3]` ×6: `inject(inject(x)) == inject(x)` byte a byte, el marcador aparece **exactamente una vez**, y re-inyectar **ACTUALIZA** los tramos en vez de agregarlos |
| **A4** | un paquete **sin** `<metadata>` se rechaza con un error claro en vez de corromperse | `[A4]` ×4, y **no se escribe ningún archivo de salida** |

🔵 **Un cuidado que la acción no pedía y que había que tomar:** `<metadata>` es legal también en
`organization`, `item`, `resource` y `file` —son **nueve** las ranuras—, así que *«insertar antes
del primer `</metadata>`»* **no es una simplificación, es un error**: en un paquete cuyo único
`<metadata>` cuelga de un `resource`, el marcado del **curso** quedaría grapado a **un archivo**.
El módulo usa `xml.parsers.expat` y su `CurrentByteIndex` para tomar el `</metadata>` **de nivel
manifiesto**, y la prueba `[A4]` usa exactamente ese paquete como caso.

## Correr las pruebas

```sh
python3 test_pack.py                       # 27 checks estructurales, sólo stdlib
SCORM_SCHEMAS=/ruta/a/scorm-mcp-server/schemas \
SCORM_SCHEMAS12=/ruta/a/scorm-mcp-server/schemas12 \
  python3 test_pack.py --with-xmllint      # 37: agrega la matriz de conformidad real
```

Resultado sobre Python 3.11 y `xmllint` 2.9 (libxml 20914):

```
27/27 checks passed          (sin xmllint)
37/37 checks passed          (con los dos directorios de esquemas)
```

🔵 **Las dos cifras se declaran las dos a propósito**, que es la regla que la acción 2 de este
mismo pase dejó escrita: **una cifra de aserciones sin su invocación es una cifra que nadie puede
reproducir.**

## Lo que esto NO resuelve

- **No clasifica, y ahora se sabe que nadie lo hace.** La acción 3 de este pase midió las 33
  filas expuestas: **cero emiten un límite dentro del texto generado**
  ([`../aiact-50-2-spans/`](../aiact-50-2-spans/README.md)). 🔵 **Pero marcar el curso ENTERO como
  generado no necesita clasificador, y eso es lo que este módulo entrega hoy.**
- **No es una marca de agua.** `sign_hook()` de [`../aiact-50-2-marking/`](../aiact-50-2-marking/README.md)
  sigue siendo una costura declarada y **vacía** (**gap 98**).
- **No parchea el generador.** `buildManifestFor` sigue sin gancho (**gap 100** por el camino
  largo: el PR a upstream). Este módulo es el camino barato y **no toca upstream**.
- **No es asesoramiento legal**, y el texto primario del Reglamento (UE) 2024/1689 sigue
  inalcanzable (**gap 92**, cuatro canales). Para educación la fecha que esta base tiene
  confirmada **por tres canales secundarios concordantes, no por primaria**, es **Anexo III →
  2027-12-02**.
