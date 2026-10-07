#!/usr/bin/env python3
"""Hijo del sweep: corre UN instrumento .py SIN argumentos bajo un audit hook y
cuenta los archivos NO-codigo del repositorio que abre.

Por que un audit hook y no un tracer: `strace` esta disponible pero envolver
codigo del arbol clonado en un tracer no esta permitido en este entorno.
`sys.addaudithook` es Python puro, corre en el mismo proceso que el instrumento
y mide exactamente lo que hace falta: la apertura efectiva de un archivo.

Imprime una sola linea:  <codigo_de_salida>\t<archivos_juzgados_leidos>
"""
import io
import os
import runpy
import sys

# .py / .pyc son CODIGO: importarlos no es juzgar una entrada.  Todo lo demas
# bajo la raiz del repo (markdown, tsv, json, txt, fixtures) si lo es.
CODIGO = (".py", ".pyc")


def main(argv):
    if len(argv) < 2:
        print(
            "P542-NO-INPUT\tREFUSED: uso: readcount.py <instrumento.py> <raiz_repo>",
            file=sys.stderr,
        )
        return 2
    objetivo, raiz = argv[0], os.path.realpath(argv[1])
    leidos = set()

    def hook(evento, args):
        if evento == "open" and args and isinstance(args[0], str):
            p = os.path.realpath(args[0])
            if p.startswith(raiz) and not p.endswith(CODIGO) and os.path.exists(p):
                leidos.add(p)

    sys.addaudithook(hook)
    # El instrumento debe verse invocado SIN argumentos: es la condicion del gap.
    sys.argv = [os.path.basename(objetivo)]
    codigo = 0
    silencio = io.StringIO()
    out_real, err_real = sys.stdout, sys.stderr
    sys.stdout = sys.stderr = silencio
    try:
        runpy.run_path(objetivo, run_name="__main__")
    except SystemExit as e:
        codigo = e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
    except BaseException as e:  # noqa: BLE001 - un instrumento que explota NO es un pase
        codigo = "EXC:" + type(e).__name__
    finally:
        sys.stdout, sys.stderr = out_real, err_real
    print(f"{codigo}\t{len(leidos)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
