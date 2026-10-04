#!/bin/sh
# P253 — barrido REGISTRY-FIRST de identidad de paquete.
#
# Orden que importa, y es el inverso del que uso el pase 83:
#   1. al REGISTRO por el nombre (autoritativo: existe / no existe, mantenedor, repository+directory)
#   2. al ARBOL por el manifiesto, en profundidad 0 Y en los subdirectorios que el registro nombro
#
# Precondicion (P249): el canal se CALIBRA antes de creerle un negativo.
#   registry.npmjs.org  -> 200 a un paquete que existe, 404 a uno que no
#   raw.githubusercontent.com -> 200 a un archivo que existe, 404 a uno que no
# Si un canal no discrimina, este script NO corre: un 404 suyo no seria evidencia.
#
# Uso:  sh sweep_identity.sh <nombre-de-paquete> [...]
set -u
R=https://registry.npmjs.org

calibrate () {
  g=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 25 "$R/express")
  b=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 25 "$R/no-such-package-p253-control")
  if [ "$g" = "200" ] && [ "$b" = "404" ]; then
    echo "CALIBRATED registry.npmjs.org good=$g bad=$b" >&2
    return 0
  fi
  echo "NO-CLAIM registry.npmjs.org no discrimina (good=$g bad=$b): un 404 no es evidencia" >&2
  return 1
}

calibrate || exit 2

printf 'pkg_name\thttp\tlatest\tmaintainers\tpub_repo\tpub_dir\n'
for p in "$@"; do
  enc=$(printf '%s' "$p" | sed 's|/|%2F|')
  code=$(curl -sS -o /tmp/p253.$$ -w '%{http_code}' --max-time 30 "$R/$enc" 2>/dev/null)
  if [ "$code" = "200" ]; then
    python3 - "$p" "$code" /tmp/p253.$$ <<'PY'
import json, sys
p, code, f = sys.argv[1], sys.argv[2], sys.argv[3]
d = json.load(open(f))
lat = d.get('dist-tags', {}).get('latest', '-')
m = ','.join(sorted({(x.get('name') if isinstance(x, dict) else str(x))
                     for x in d.get('maintainers', [])})) or '-'
v = d.get('versions', {}).get(lat, {})
r = v.get('repository')
url = (r.get('url') if isinstance(r, dict) else r) or '-'
dirc = (r.get('directory') if isinstance(r, dict) else None) or '-'
print('\t'.join([p, code, lat, m, str(url), str(dirc)]))
PY
  else
    # ⚠️ Solo informativo si el nombre vino DECLARADO por un arbol.
    # Un 404 sobre un nombre conjeturado se marca para que identity.py lo deje UNDETERMINED.
    printf '%s\t%s\t-\t-\t-\t-\n' "$p" "$code"
  fi
done
rm -f /tmp/p253.$$
