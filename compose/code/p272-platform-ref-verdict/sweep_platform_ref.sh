#!/bin/sh
# P272 -- le pone REF a los veredictos de plataforma del pase 90.
# Registra el bucle corrido A MANO en el pase 91 para que un pase futuro lo reproduzca.
# NO se ejecuto desde este archivo en el pase 91 (ejecucion de codigo del arbol: NEGADA),
# asi que este README no publica columna "Hoy" ni total de aserciones (regla de P107).
set -u
code() { curl -s -o /dev/null -w '%{http_code}' -m 20 "$1"; }
RAW=https://raw.githubusercontent.com
# Compuerta de calibracion: sin un malo que de 404, no se publica NINGUN negativo.
gate() { # $1=repo $2=ctrl_path
  good=$(code "$RAW/$1/HEAD/$2"); bad=$(code "$RAW/$1/zzz-fake-ref-91/$2")
  [ "$good" = "200" ] && [ "$bad" = "404" ] || { echo "NO-CLAIM: canal no calibrado ($1)" >&2; return 1; }
}
# $1=repo $2=ctrl $3=manifiesto $4..=refs
scan() {
  repo=$1; ctrl=$2; man=$3; shift 3
  gate "$repo" "$ctrl" || return 1
  for ref in "$@"; do
    c=$(code "$RAW/$repo/$ref/$ctrl")
    # El control prueba que la REF existe. Sin el, un 404 del manifiesto es ambiguo.
    [ "$c" = "200" ] || { echo "$repo	$ref	REF-NO-RESUELTA	-	NO-CLAIM"; continue; }
    tok=$(curl -s -m 30 "$RAW/$repo/$ref/$man" \
      | grep -ioE '^(litellm|langchain[a-z-]*|openai|anthropic|ollama|vertexai|google-generativeai)[=><~ ]*[0-9.]*' \
      | sort -u | tr '\n' ',')
    [ -n "$tok" ] && v=TIENE-PROVEEDOR || v=SIN-PROVEEDOR
    echo "$repo	$ref	200	${tok:--}	$v"
  done
}
scan openedx/edx-platform README.rst requirements/edx/base.txt \
  open-release/quince.master open-release/redwood.master open-release/sumac.master master
scan instructure/canvas-lms Gemfile Gemfile master prod
