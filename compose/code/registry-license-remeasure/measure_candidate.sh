#!/bin/bash
# P115 + the pase-52 CORRECTED tarball anchor (case-insensitive, still anchored to package/ root)
NAMES20="LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt COPYING.md LICENSE-MIT LICENSE-APACHE LICENSE-APACHE-2.0 LICENSE.rst LICENCE LICENCE.md license license.md License License.md LICENSE-MIT.md UNLICENSE COPYRIGHT NOTICE"
ANCHOR='^package/(licen[cs]e|copying)([._-][A-Za-z0-9]+)?$'
code(){ curl -s -m 12 -o /dev/null -w "%{http_code}" "$1" 2>/dev/null; }
for P in "$@"; do
  echo "########## $P"
  J=$(curl -s -m 25 "https://registry.npmjs.org/$P/latest")
  eval "$(printf '%s' "$J" | python3 -c '
import sys,json
d=json.load(sys.stdin)
r=d.get("repository")
if isinstance(r,dict): r=r.get("url","")
r=(r or "").replace("git+","").replace("git://","https://").replace(".git","")
slug=""
if "github.com" in r: slug=r.split("github.com")[-1].lstrip(":/")
print("VER=%r"%d.get("version",""))
print("LIC=%r"%(d.get("license") or "NONE"))
print("SLUG=%r"%slug)
print("DESC=%r"%(d.get("description","") or "")[:150])
print("TB=%r"%d.get("dist",{}).get("tarball",""))
' 2>/dev/null)"
  echo "  version=$VER  campo-licencia=$LIC  repo=${SLUG:-NINGUNO}"
  echo "  desc=$DESC"
  if [ -n "$SLUG" ]; then
    found=""
    for br in main master; do
      for f in $NAMES20; do
        if [ "$(code "https://raw.githubusercontent.com/$SLUG/$br/$f")" = "200" ]; then
          t=$(curl -s -m 12 "https://raw.githubusercontent.com/$SLUG/$br/$f" | tr -d '\r' | grep -m1 -vE '^[[:space:]]*$' | cut -c1-70)
          echo "  REPO-TEXTO: $br:$f -> $t"; found=1; break 2
        fi
      done
    done
    if [ -z "$found" ]; then
      rc=""
      for br in main master develop; do
        if [ "$(code "https://raw.githubusercontent.com/$SLUG/$br/README.md")" = "200" ]; then rc="$br"; break; fi
      done
      if [ -n "$rc" ]; then echo "  REPO-TEXTO: 🔴 sin licencia (20 nombres x 2 ramas 404; $rc/README.md=200)"
      else echo "  REPO-TEXTO: ⚠️ indeterminado (el canal no llego al repo)"; fi
    fi
  fi
  if [ -n "$TB" ]; then
    T=$(mktemp); curl -s -m 60 -o "$T" "$TB"
    L=$(tar -tzf "$T" 2>/dev/null)
    FN=$(printf '%s\n' "$L" | grep -i -m1 -E "$ANCHOR")
    REC=$(printf '%s\n' "$L" | grep -icE 'licen[cs]e|copying')
    if [ -n "$FN" ]; then
      echo "  TARBALL: $FN -> $(tar -xzOf "$T" "$FN" 2>/dev/null | tr -d '\r' | grep -m1 -vE '^[[:space:]]*$' | cut -c1-70)  [raiz=1 recursivo=$REC]"
    else
      echo "  TARBALL: 🔴 sin texto en la raiz del paquete [raiz=0 recursivo=$REC]"
    fi
    MLIC=$(tar -xzOf "$T" package/package.json 2>/dev/null | python3 -c 'import sys,json;print(json.load(sys.stdin).get("license","NONE"))' 2>/dev/null)
    echo "  MANIFIESTO-en-tarball: license=$MLIC"
    rm -f "$T"
  fi
done
