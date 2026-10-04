#!/usr/bin/env python3
"""P276 — el conjunto de proveedores de una plataforma se lee de su ALLOWLIST, no de un listado.

Contexto, y es una correccion de esta base a si misma:

El pase 92 publico «Chamilo liga 6 proveedores en el nucleo» y celebro que su script
(`p273-platform-provider-dir/sweep_provider_dir.sh`) REPLICARA la cifra por un segundo
canal: «8/8 refs coinciden EXACTO (0,0,5,5,6,6,6,6)». 🔴 La replicacion no era
independiente: el script y la medicion manual sondeaban la MISMA lista de nombres
candidatos --`OpenAi DeepSeek Gemini Mistral Grok Anthropic Ollama`-- y `Claude` no
estaba en ella. Las dos coincidieron porque compartian el punto ciego.

Enumerado el directorio (ver `p275-tree-enumeration/`), en `v3.0.x` hay SIETE clases
`*Provider.php`, no seis: la septima es `ClaudeProvider.php`.

**P276**: *un conteo obtenido sondeando una lista de NOMBRES CANDIDATOS esta acotado por
la lista, no por el repo. Dos canales que sondean la misma lista no se validan entre si:
comparten su punto ciego. Un conteo solo es un conteo si ENUMERA.*

Y el instrumento correcto no es ni el sondeo ni el listado de directorio, sino la
ALLOWLIST que la plataforma aplica en tiempo de ejecucion: `AiProviderFactory` rechaza
toda clave que no este en su mapa `$possibleProviders` (`'Unsupported provider in config'`
-> `continue`). Esa lista es la respuesta a «que puede configurar un administrador».

Uso:  python3 extract_allowlist.py FUENTE_DEL_FACTORY.php
      python3 extract_allowlist.py -   (lee stdin)
Salida: TSV `clave<TAB>prefijo_de_clase`, una linea por proveedor admitido.
"""
import re
import sys

# El mapa se declara como  $possibleProviders = [ 'clave' => 'Prefijo', ... ];
OPEN_RE = re.compile(r"\$possibleProviders\s*=\s*\[")
PAIR_RE = re.compile(r"""['"]([A-Za-z0-9_]+)['"]\s*=>\s*['"]([A-Za-z0-9_]+)['"]""")


def extract(src):
    """Devuelve [(clave, prefijo)] del mapa $possibleProviders.

    Solo lee el bloque que ARRANCA en la declaracion y TERMINA en el primer `];`.
    Leer el archivo entero traeria los mapas vecinos (`$typeSuffix`, `$typeInterface`),
    que tienen la misma forma sintactica y NO son proveedores.
    """
    m = OPEN_RE.search(src)
    if not m:
        return []
    rest = src[m.end():]
    end = rest.find("];")
    block = rest if end == -1 else rest[:end]
    return PAIR_RE.findall(block)


def main(argv):
    if not argv:
        print(__doc__.strip().splitlines()[-3], file=sys.stderr)
        return 2
    src = sys.stdin.read() if argv[0] == "-" else open(argv[0], encoding="utf-8").read()
    rows = extract(src)
    if not rows:
        # 🔴 Sin mapa no se publica «cero proveedores»: se publica NO-CLAIM. Un archivo
        # que no declara allowlist puede estar en otra version del factory, no vacio.
        print("NO-CLAIM\tsin-mapa-possibleProviders", file=sys.stderr)
        return 1
    for key, prefix in rows:
        print(f"{key}\t{prefix}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
