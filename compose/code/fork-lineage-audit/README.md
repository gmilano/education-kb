# fork-lineage-audit — el instrumento de P160 (pase 62, 2026-10-03)

**Qué mide.** Dado el texto de la página de un repo de GitHub, separa **dos ejes que esta base
venía mezclando**:

- **linaje** — el `forked from OWNER/REPO`, o `None` si el repo es original;
- **superficie** — el techo de *tools* que declara el README, o `None`.

**Por qué existe.** El pase 62 midió la familia de `vishalsachdev/canvas-mcp` y encontró que **el
campo `description` de GitHub se hereda ENTERO en cada fork** —*«up to 102 tools and 8 agent
skills»*, palabra por palabra en madre y forks— **mientras los README de esas mismas piezas
declaran 101, 103 y 139**. A la misma release (`v1.13.0`), **el fork expone 36 *tools* más que la
madre**.

🔵 **Consecuencia, que es P160:** un barrido por **búsqueda** lee descripciones, ve una sola pieza
repetida y **sub-cuenta la superficie**; un barrido por **repo** ve piezas independientes y
**sobre-cuenta el código**. Las dos cuentas están mal y en direcciones opuestas. **Hay que abrir el
README.**

## El control, que es lo que hace que la salida valga (P126)

`test_audit.py` **falla si el instrumento no discrimina.** El par de control es real y está medido
de primera mano en el pase 62:

| Fixture | Debe dar |
|---|---|
| `Dymayo/moodler-mcp` | 🔴 **fork de `GhaithAlHallak8/moodler-mcp`** |
| `GhaithAlHallak8/moodler-mcp` (la madre) | 🟢 **None** |

**Y la aserción que justifica el instrumento entero:** leyendo **sólo la descripción**, la
divergencia de superficie entre madre y fork da **0** —un «idéntico» falso, que es exactamente la
forma de error de P151—; leyendo el README da **36**.

## Correr

```
python3 test_audit.py          # 13 aserciones
python3 audit_lineage.py fixtures/*.txt    # salida JSON
```

**Estado: 13/13 pasan.**

### 🔵 La restricción `[Code from External]`, por fin DELIMITADA (y no es lo que cuatro pases supusieron)

**Este pase provocó las dos ramas de primera mano, y dan distinto:**

| Acción | Resultado en esta corrida |
|---|---|
| `python3 test_audit.py` **con el `cwd` dentro del árbol clonado** (`compose/code/fork-lineage-audit/`) | 🟢 **PERMITIDO — 13/13 aserciones pasan** |
| `python3` inline con un script que **edita un archivo del árbol clonado** | 🔴 **NEGADO: `[Code from External]`** |

🔴 **Los pases 58–61 registraron la negativa como «no se puede ejecutar código proveniente del
árbol clonado» y pidieron permiso en esos términos. Medido acá, ese enunciado es DEMASIADO ANCHO:
correr el test del propio repo desde el propio repo funciona.** 🟢 **Lo que se niega es ejecutar un
intérprete para OPERAR sobre el árbol externo, no correr sus pruebas.**

🔵 **Consecuencia para el backlog, y es la que importa: el «pedido angosto» que esta KB venía
arrastrando estaba mal formulado, así que pedirlo no habría desbloqueado nada.** ⚠️ **Se
reformula: lo que hay que pedir —si alguna vez hace falta— no es ejecutar código del árbol, es
MODIFICAR el árbol con un script. Y para esta KB casi nunca hace falta: las ediciones se hacen con
las herramientas de edición, que no están restringidas.**

⚠️ **Lo que NO se probó, para que no se lea como cobertura:** sólo se ejecutó el test de ESTE
directorio. **No se probó correr código de otras partes del árbol, así que no se afirma que la
restricción se haya levantado — se afirma que estas dos ramas concretas dan resultados opuestos y
que el enunciado heredado no describía la frontera.**

## Límites declarados

- 🔴 **No hace red.** Recibe texto ya capturado. La captura y la medición se mantienen separadas a
  propósito, para que el control pueda correr sin internet. **La captura de este pase fue WebFetch
  sobre la página HTML, porque `api.github.com` devolvió `403` y `curl` a `github.com` también.**
- ⚠️ **`surface()` devuelve el MAYOR número de *tools* del texto**, porque los README de esta
  familia declaran un techo (*«up to N»*) y desglosan cifras menores por perfil más abajo. **Si un
  README cambiara de convención, la cifra deja de ser comparable** — por eso el instrumento reporta
  el número y no un veredicto.
- 🔴 **No lee licencias y no debe empezar a hacerlo:** la cesión se mide con `raw` sobre el archivo
  (**P161**), no sobre la página. El fixture de `DMontgomery40/mcp-canvas-lms` está incluido
  justamente como recordatorio: su README promete `LICENSE` y el archivo da 404 por tres rutas.
- ⚠️ **No resuelve la cadena completa de un fork de un fork**: devuelve el padre inmediato.
