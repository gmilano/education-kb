#!/bin/sh
# P273 -- la ligadura de proveedor de una plataforma puede vivir en un DIRECTORIO del nucleo,
# y entonces el MANIFIESTO de runtime es un instrumento CIEGO (no un veredicto negativo).
# Registra el bucle corrido A MANO en el pase 92 -- y en ESTE pase la ejecucion VOLVIO
# (primera vez en once pases: 58,67,79,80,81,84,86,89,90,91 la tenian NEGADA), asi que
# este script SE CORRIO y sus 8 refs coinciden EXACTO con la medicion manual: 0,0,5,5,6,6,6,6.
# Suites del arbol en el mismo pase: 41/41 verdes (39 py + 2 sh).
set -u
code() { curl -s -o /dev/null -w '%{http_code}' -m 20 "$1"; }
RAW=https://raw.githubusercontent.com

# --- P274: un path de DIRECTORIO da 404 en este canal SIEMPRE. Sin este control,
# --- "probe el directorio y dio 404" se lee como ausencia y es un artefacto del canal.
p274_demo() {
  echo "dir-que-existe      $(code "$RAW/moodle/moodle/MOODLE_503_STABLE/public/ai")"
  echo "archivo-en-ese-dir  $(code "$RAW/moodle/moodle/MOODLE_503_STABLE/public/ai/provider/openai/version.php")"
}

# Compuerta de calibracion por repo: sin un malo que de 404, no se publica NINGUN negativo.
gate() { # $1=repo
  good=$(code "$RAW/$1/HEAD/README.md"); bad=$(code "$RAW/$1/zzz-fake-ref-92/README.md")
  [ "$good" = "200" ] && [ "$bad" = "404" ] || { echo "NO-CLAIM: canal no calibrado ($1)" >&2; return 1; }
}

# Cuenta proveedores en un DIRECTORIO del nucleo, por ref, con control negativo en el MISMO dir.
# $1=repo  $2=dir  $3=sufijo  $4..=refs
scan_dir() {
  repo=$1; dir=$2; suf=$3; shift 3
  gate "$repo" || return 1
  for ref in "$@"; do
    # El control prueba que la REF existe: sin el, un 404 del archivo es ambiguo.
    [ "$(code "$RAW/$repo/$ref/README.md")" = "200" ] || { echo "$repo	$ref	REF-NO-RESUELTA	NO-CLAIM"; continue; }
    # Control negativo en el mismo directorio y la misma ref (P249).
    [ "$(code "$RAW/$repo/$ref/$dir/ZzzFake92$suf")" = "404" ] || { echo "$repo	$ref	CTRL-NO-404	NO-CLAIM"; continue; }
    n=0; hit=""
    # OJO (P270): los nombres son los REALES leidos del listado del arbol, no conjeturados.
    # "OpenAi.php" da 404 y ese 404 mide el NOMBRE, no la ausencia del proveedor.
    for p in OpenAi DeepSeek Gemini Mistral Grok Anthropic Ollama; do
      if [ "$(code "$RAW/$repo/$ref/$dir/$p$suf")" = "200" ]; then n=$((n+1)); hit="$hit,$p"; fi
    done
    echo "$repo	$ref	$n/7	${hit#,}"
  done
}

p274_demo
scan_dir chamilo/chamilo-lms src/CoreBundle/AiProvider Provider.php \
  v1.11.40 1.11.x v2.0.0 2.0 v3.0.0 v3.0.1 3.0 master
