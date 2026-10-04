#!/bin/sh
# P275 -- enumera el arbol COMPLETO de una (repo, ref) con un clon sin blobs.
#
# Retira el limite que el pase 92 declaro en su propio canal: `WebFetch` sobre las
# paginas `tree/` de github.com TRUNCA los listados largos, y por eso ILIAS quedo
# medido en el tramo A-L (corto en `LegalDocuments`) con veredicto "sostenido CON
# LIMITE". Un clon `--filter=blob:none --no-checkout --depth 1` baja commit y arboles
# sin blobs y `git ls-tree` enumera completo: sobre ILIAS el clon tarda < 1 s.
#
# CONTROLES (sin ellos no se publica ningun negativo):
#   C1  ref inventada -> el clon DEBE fallar. Si no falla, el canal no discrimina.
#   C2  compuerta de LAYOUT (P278): la ruta de componentes depende de la ref.
#       `components/ILIAS` da 180 en release_11 y CERO en release_9, donde estan en
#       `Modules`+`Services`. Un cero sin compuerta mide la RUTA, no el arbol.
#   C3  control POSITIVO: sobre Moodle el barrido debe devolver los 7 proveedores
#       conocidos. Un instrumento que no reproduce un positivo conocido no sostiene
#       una ausencia.
set -u
WORK=${WORK:-$(mktemp -d)}

# Enumera: $1=repo $2=ref -> imprime los directorios (una ruta por linea)
tree_dirs() {
  d="$WORK/$(echo "$1-$2" | tr '/.' '--')"
  [ -d "$d" ] || git clone -q --filter=blob:none --no-checkout --depth 1 \
    -b "$2" "https://github.com/$1" "$d" 2>/dev/null || return 1
  git -C "$d" ls-tree -d --name-only -r HEAD 2>/dev/null
}

# C1 -- el canal tiene que RECHAZAR una ref inventada.
gate_ref() {
  if tree_dirs "$1" zzz-fake-ref-93 >/dev/null 2>&1; then
    echo "NO-CLAIM: el canal no discrimina refs ($1)" >&2; return 1
  fi
  return 0
}

# C2 -- cuenta directorios bajo una ruta; 0 significa "ruta no poblada en esta ref".
# `grep -c` ya imprime 0 y ADEMAS sale con codigo 1 cuando no hay coincidencias, asi
# que un `|| echo 0` emite DOS lineas y el `[ ]` de abajo recibe "0\n0". Se absorbe el
# codigo de salida sin agregar salida.
count_under() { # $1=listado  $2=prefijo ("" = nivel superior del repo)
  if [ -z "$2" ] || [ "$2" = "." ]; then
    n=$(grep -c '^[^/]*$' "$1" 2>/dev/null) || n=0
  else
    n=$(grep -c "^$2/[^/]*$" "$1" 2>/dev/null) || n=0
  fi
  echo "${n:-0}"
}

# Cuenta componentes de AI comparando el ULTIMO SEGMENTO completo, no por subcadena:
# `ai` como subcadena casa con Mail / MainMenu / Container / ScormAicc, y publicar eso
# serian cinco componentes de AI inventados en ILIAS. Ver `test_layout.py`.
count_ai() { # $1=listado
  awk -F/ '{n=tolower($NF)}
    n=="ai"||n=="aiprovider"||n=="chatbot"||n=="llm"||n=="assistant"||
    n=="openai"||n=="genai"||n=="copilot" {c++} END{print c+0}' "$1"
}

scan() { # $1=repo  $2=ref  $3..=rutas candidatas
  repo=$1; ref=$2; shift 2
  L="$WORK/list-$(echo "$repo-$ref" | tr '/.' '--').txt"
  tree_dirs "$repo" "$ref" > "$L" 2>/dev/null || { echo "$repo	$ref	CLONE-FAIL	NO-CLAIM"; return; }
  [ -s "$L" ] || { echo "$repo	$ref	ARBOL-VACIO	NO-CLAIM"; return; }
  # 🔴 `found` es una bandera APARTE y no se deduce de `layout`. Primera version de este
  # script usaba `[ -z "$layout" ]` como "no encontrado", y la ruta del RAIZ del repo es
  # justamente la cadena VACIA: `openeducat_erp` daba LAYOUT-NO-ENCONTRADO teniendo sus
  # 15 modulos contados (n=15). Es la misma clase de defecto que `P250` registro con
  # `UNCLASSIFIED`: un centinela que colisiona con un valor real de dato.
  layout=""; total=0; found=0
  for p in "$@"; do
    n=$(count_under "$L" "$p")
    if [ "$n" -gt 0 ]; then
      found=1
      layout="$layout${layout:+ }${p:-<raiz>}"
      total=$((total+n))
    fi
  done
  ai=$(count_ai "$L")
  if [ "$found" -eq 0 ]; then
    # P278: ninguna ruta candidata esta poblada -> el cero mide la ruta.
    echo "$repo	$ref	LAYOUT-NO-ENCONTRADO	NO-CLAIM	dirs_totales=$(wc -l < "$L")"
  elif [ "$ai" -eq 0 ]; then
    echo "$repo	$ref	$layout	SIN-AI-EN-NUCLEO	componentes=$total	arbol=$(wc -l < "$L")"
  else
    echo "$repo	$ref	$layout	TIENE-AI:$ai	componentes=$total	arbol=$(wc -l < "$L")"
  fi
}

echo "== C1: compuerta de ref inventada =="
gate_ref ILIAS-eLearning/ILIAS && echo "ILIAS: ref falsa RECHAZADA (canal discrimina)"

echo "== ILIAS, las cuatro refs, con compuerta de layout (C2) =="
for ref in release_9 release_10 release_11 trunk; do
  scan ILIAS-eLearning/ILIAS "$ref" components/ILIAS Modules Services
done

echo "== C3: control POSITIVO sobre Moodle (deben salir los 7 proveedores) =="
L="$WORK/moodle.txt"
if tree_dirs moodle/moodle MOODLE_503_STABLE > "$L"; then
  echo "proveedores: $(grep -c '^public/ai/provider/[^/]*$' "$L")"
  grep '^public/ai/provider/[^/]*$' "$L" | sed 's|.*/||' | tr '\n' ' '; echo
fi

echo "== Resto de la capa de plataforma, arbol completo =="
scan frappe/erpnext develop erpnext
scan frappe/education develop education
scan openeducat/openeducat_erp 18.0 ""
