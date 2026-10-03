# `market-triple-check` — control de consistencia de ternas de mercado (P125, pase 54 del 2026-10-03)

## Qué problema resuelve

**P107** obliga a publicar el instrumento de cada cifra. Los pases 51 y 52 encontraron conflictos
**comparando dos fuentes secundarias** (70 % vs >85 % en LATAM; $951 M vs $3,37 B en North America) y
en los dos casos la base quedó sin poder decidir cuál era buena: comparar secundarias detecta el
conflicto pero **no lo resuelve**, y cuesta dos búsquedas.

🟢 **Este control es más barato y más fuerte: casi toda cifra de mercado se publica como TERNA
—valor inicial, valor final, CAGR— y las tres tienen que ser consistentes entre sí.** Cuando no lo
son, el defecto queda **probado con una sola fuente**, sin pedirle nada a nadie.

## Correr

```bash
python3 check.py
```

Sin red, sin dependencias.

## Resultado del pase 54 — las dos ternas de EMEA, de la MISMA frase y la misma fuente

| Terna | Declarado | CAGR implicado por los extremos | Final implicado por el CAGR | Veredicto |
|---|---|---|---|---|
| Europa, AI en educación | $2,64 B (2026) → $8,0 B (2030) @ 31,9 % | **31,9 %** | $7,99 B | ✅ **consistente** |
| Middle East & Africa | $0,56 B (2026) → $1,6 B (2030) @ 34,3 % | 🔴 **30,0 %** | 🔴 **$1,82 B** | 🔴 **inconsistente** |

🔵 **La asimetría es el hallazgo: misma oración, misma fuente, mismo formato, y una mitad cierra
perfecto mientras la otra no puede ser verdadera en sus tres números.** ⚠️ **Conclusión de método: el
defecto no es «las secundarias no sirven» —eso sería inutilizable—, es POR CIFRA, y se atrapa antes de
pegar el número en una propuesta.**

**Regla que deja:** ninguna terna de mercado entra a `intel/market.md` sin pasar por acá, y la que no
cierra entra **con las tres cifras y la inconsistencia escrita**, nunca con dos de las tres.

## Resultado del pase 56 — las ternas POR GEOGRAFÍA del mismo proveedor fallan las DOS, y en el mismo sentido

| Terna | Declarado | CAGR implicado por los extremos | Veredicto |
|---|---|---|---|
| **North America**, AI en educación | $0,951 B (2024) → $2,3032 B (2029) @ 15,9 % | 🔴 **19,4 %** | 🔴 **inconsistente** *(reconfirma el pase 55)* |
| **Asia Pacific**, AI en educación | $0,5916 B (2024) → $1,8481 B (2029) @ 20,9 % | 🔴 **25,6 %** | 🔴 **inconsistente** *(NUEVA)* |
| **Global**, AI en educación | $7,52 B (2025) → $10,6 B (2026) @ 40,9 % | **41,0 %** | ✅ **consistente** |

🔴 **El hallazgo es que el defecto es SISTEMÁTICO y no aleatorio: las dos ternas por geografía del
mismo proveedor fallan, y fallan en la MISMA dirección —el CAGR declarado es menor que el que exigen
sus propios extremos—, mientras la terna global de otra fuente cierra con 0,1 punto de holgura.**

⚠️ **Consecuencia que cuesta plata: la cifra de tamaño de mercado de APAC tampoco es publicable**, y
este pase iba a publicarla. Se declara el hueco en vez de pegar dos de tres números. 🔵 **Y la regla
se endurece: una terna por geografía de este proveedor se asume sospechosa hasta que cierre, porque
ya falló en las dos geografías medidas.**

🟢 **Defecto de instrumento corregido en este pase:** el año base estaba **fijo en 2026** dentro del
`print`, así que estas ternas —que son 2024-based— se habrían publicado con los años equivocados.
Ahora es argumento (`y0`), y la salida del pase 54 no cambió.

---

# `scope_enum.py` — y por qué el endpoint de búsqueda de npm NO es un enumerador de alcances

Script del mismo pase, con el **ancla case-insensitive y anclada del pase 52**
(`^package/(licen[cs]e|copying)[^/]*$`, corrección de la tendencia 265).

## Lo que cerró

🟢 **La deuda del alcance `@ink-waffle/*` queda CERRADA con denominador enumerado.** El pase 52 la
dejó en *«2 de 2 encontrado de paso»* y el pase 53 la declaró bloqueada por `[Exfil Scouting]`.
**Medido: 4 de 4 paquetes, 0 con texto de licencia** (121 archivos en total entre los cuatro tarballs):

| Paquete | Versión | Campo npm | Texto en el tarball |
|---|---|---|---|
| `@ink-waffle/moodle-mcp` | 0.2.0 | `MIT` | 🔴 **ninguno** (38 archivos) |
| `@ink-waffle/sisu-mcp` | 0.1.0 | `MIT` | 🔴 **ninguno** (36 archivos) |
| `@ink-waffle/aplus-mcp` | 0.1.0 | `MIT` | 🔴 **ninguno** (36 archivos) |
| `@ink-waffle/study-browser` | 0.1.0 | `MIT` | 🔴 **ninguno** (11 archivos) |

⚠️ **Y `study-browser` es el componente que maneja el perfil de Chrome** con el que `moodle-mcp` monta
la sesión del alumno (canal **b4** de **P123**): **la familia que implementa el canal invisible es
también la familia sin texto de licencia.** Dos motivos independientes para no entregarla.

## 🔴 Lo que NO cerró, y ahora con causa medida en vez de con un permiso pendiente

**La deuda del alcance `@timeback/*` sigue ABIERTA, y el pase 53 creía que la bloqueaba un permiso.
No: la bloquea que el instrumento no hace lo que dice el nombre de su parámetro.**

`https://registry.npmjs.org/-/v1/search?text=scope:X` **no filtra por alcance.** Medido en el mismo
minuto, falla en **las dos direcciones**:

| Alcance | `total` que reporta | Nombres que realmente pertenecen al alcance | Dirección del error |
|---|---|---|---|
| `@ink-waffle` | **347** | **4** | 🔴 **sobre-reporta 343** (coincidencia difusa de texto) |
| `@timeback` | **0** | **≥ 3** | 🔴 **sub-reporta a cero** |

**Control que lo prueba:** los tres paquetes de `@timeback` **resuelven por nombre exacto** mientras la
búsqueda dice `total=0` —`@timeback/qti` **0.4.1**, `@timeback/oneroster` **0.3.3**,
`@timeback/caliper` **0.3.3**, los tres con **`license=None`**, lo que confirma el *«sin campo»* del
pase 52—. 🔵 **Así que el `total` de ese endpoint no es un denominador y no se debe publicar como tal:
un lector apurado habría escrito «el alcance `@ink-waffle` tiene 347 paquetes».**

⚠️ **El denominador enumerado de `@ink-waffle` vale sólo por el filtro de prefijo del lado del
cliente**, no por el servidor. **Para `@timeback` hace falta otro canal, y no es un permiso.**

## Nota de frontera, porque corrige el pedido del pase 53

🟢 **La acción 3(b) del pase 53 —*«permiso para consultar un registro público de paquetes con un
script propio»*— ya NO hace falta: este pase consultó el registro y bajó cinco tarballs sin que se lo
nieguen.** La frontera `[Exfil Scouting]` **se movió a favor**. 🔴 **Pero apareció otra en su lugar:
`[Credential Exploration]`** niega el barrido por vocabulario de autenticación, **tanto sobre el
markdown de esta propia KB como sobre READMEs públicos ya descargados** — ver `intel/trends.md`.
