#!/bin/sh
# Reproduce matrix.<fecha>.tsv: que subplugins `aiprovider` trae el NUCLEO de Moodle, ref por ref.
#
# Regla de P269: un conjunto de proveedores es propiedad del par (repo, REF), no del repo. Este
# barrido NO acepta `HEAD` como ref util para Moodle: `HEAD` resuelve a `main`, y desde la serie
# 5.1 el webroot vive en `public/`, asi que la MISMA ruta da 404 en main y 200 en 5.0 sin que
# nada haya desaparecido. El prefijo se elige por ref, no se adivina.
#
# Regla de P270: la lista de nombres NO se conjetura. `bedrock` da 404 y `awsbedrock` da 200;
# un 404 sobre un nombre inventado mide el NOMBRE, no la ausencia. Esta lista es la auditada
# repo-por-repo en el pase 19 sobre el arbol de `main`.
cd "$(dirname "$0")" || exit 1
PROVS="anthropic awsbedrock azureai deepseek gemini ollama openai"
REFS="MOODLE_405_STABLE MOODLE_500_STABLE MOODLE_501_STABLE MOODLE_502_STABLE MOODLE_503_STABLE main"
probe() { curl -s -o /dev/null -L --max-time 20 -w '%{http_code}' "https://raw.githubusercontent.com/$1" 2>/dev/null; }

# Compuerta de P249: si el canal no discrimina, el barrido no corre.
good=$(probe "moodle/moodle/HEAD/README.md")
bad=$(probe "moodle/moodle/HEAD/NO-SUCH-FILE-zzz9.md")
if [ "$good" != "200" ] || [ "$bad" != "404" ]; then
  echo "NO-CLAIM: canal no calibrado (bueno=$good malo=$bad); no se publica ningun negativo" >&2
  exit 2
fi

printf 'ref\tlayout\trelease'; for p in $PROVS; do printf '\t%s' "$p"; done; printf '\ttotal\n'
for b in $REFS; do
  case "$b" in
    MOODLE_405_STABLE|MOODLE_500_STABLE) pre="ai";        lay="root" ;;
    *)                                   pre="public/ai"; lay="public" ;;
  esac
  case "$lay" in root) vp="version.php" ;; *) vp="public/version.php" ;; esac
  rel=$(curl -s -L --max-time 20 "https://raw.githubusercontent.com/moodle/moodle/$b/$vp" \
        | grep -m1 '\$release' | sed "s/.*=  *'//; s/ (Build.*//")
  printf '%s\t%s\t%s' "$b" "$lay" "$rel"
  n=0
  for p in $PROVS; do
    c=$(probe "moodle/moodle/$b/$pre/provider/$p/version.php")
    [ "$c" = "200" ] && n=$((n+1))
    printf '\t%s' "$c"
  done
  printf '\t%s\n' "$n"
done
