#!/bin/bash
# Action 1 of pass 69 -- IDENTITY of a package row: WHICH TREE is the project?
#
# Pass 68 proved the question matters: 4 of the 5 double-registry names were two DISTINCT
# ARTEFACTS, and `canvas-lms-mcp` is two live projects sharing a name.  This instrument asks the
# same question of the SINGLE-registry names, which pass 68 did not sweep on the argument that a
# name living in one registry "has nothing to contradict itself with".  `clawed` refutes that: its
# npm entry contradicts nobody and is not the project either.
#
# Four verdicts, as the action specified:
#   IDENTITY-DECLARED           the registry brings `repository` AND it resolves
#   IDENTITY-DECLARED-BUT-DEAD  it brings `repository` and the repo 404s on every cell
#   IDENTITY-PROVEN             no `repository`, but sha256(LICENSE) matches a tree (P193)
#   IDENTITY-UNKNOWN            neither
#
# The action's own condition: ASK for the declared repository, do not just read it off the
# manifest.  Reachability goes through resolve_repo.sh (a MATRIX, see P198) -- a single
# HEAD/README.md probe calls live repos dead.
#
# TSV: pkg · channel · declared_repo · resolve · lic_file · bytes · sha256(12) · verdict
pkg="$1"; chan="$2"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
HERE="$(cd "$(dirname "$0")" && pwd)"
enc=$(printf '%s' "$pkg" | sed 's|/|%2F|')
repo="-"; lf="-"; bytes="-"; sha="-"

norm(){ printf '%s' "$1" | sed -e 's|^git+||' -e 's|^ssh://||' -e 's|^git://|https://|' \
  -e 's|^git@github.com:|https://github.com/|' -e 's|\.git$||' \
  | grep -oE 'github\.com/[^/]+/[^/#?]+' | sed 's|github\.com/||' | head -1; }

if [ "$chan" = "npm" ]; then
  curl -sf --max-time 30 "https://registry.npmjs.org/$enc" -o "$TMP/r.json" || { echo -e "$pkg\tnpm\tREGISTRY-404\t-\t-\t-\t-\tIDENTITY-UNKNOWN"; exit 0; }
  read -r rawrepo tgz < <(python3 - "$TMP/r.json" <<'PY'
import json,sys
d=json.load(open(sys.argv[1])); v=d.get("dist-tags",{}).get("latest"); m=d.get("versions",{}).get(v,{})
r=m.get("repository") or d.get("repository") or ""
if isinstance(r,dict): r=r.get("url","")
print((r or "-"), m.get("dist",{}).get("tarball","-"))
PY
)
  [ -n "$tgz" ] && [ "$tgz" != "-" ] && curl -sf --max-time 60 "$tgz" -o "$TMP/p.tgz" && {
    ent=$(tar tzf "$TMP/p.tgz" 2>/dev/null | grep -iE '/(licen[sc]e|copying|notice|unlicense)([.-][a-z0-9]+)?$' | head -1)
    [ -n "$ent" ] && { lf="${ent#package/}"; tar xzf "$TMP/p.tgz" -O "$ent" > "$TMP/L" 2>/dev/null
      bytes=$(wc -c < "$TMP/L" | tr -d ' '); sha=$(sha256sum "$TMP/L" | cut -c1-12); }; }
else
  curl -sf --max-time 30 "https://pypi.org/pypi/$pkg/json" -o "$TMP/r.json" || { echo -e "$pkg\tpypi\tREGISTRY-404\t-\t-\t-\t-\tIDENTITY-UNKNOWN"; exit 0; }
  read -r rawrepo url < <(python3 - "$TMP/r.json" <<'PY'
import json,sys
d=json.load(open(sys.argv[1])); i=d["info"]
cands=[]
pu=i.get("project_urls") or {}
for k in ("Repository","Source","Source Code","Homepage","homepage","repository","Code","GitHub"):
    if pu.get(k): cands.append(pu[k])
for k,v in pu.items():
    if v and "github.com" in v: cands.append(v)
if i.get("home_page"): cands.append(i["home_page"])
r=next((c for c in cands if "github.com" in c), "-")
u=""
for f in d["urls"]:
    if f["packagetype"]=="sdist": u=f["url"]; break
if not u and d["urls"]: u=d["urls"][0]["url"]
print(r, u or "-")
PY
)
  [ -n "$url" ] && [ "$url" != "-" ] && curl -sf --max-time 60 "$url" -o "$TMP/s.bin" && {
    case "$url" in
      *.whl|*.zip) python3 - "$TMP/s.bin" "$TMP/L" <<'PY' > "$TMP/n" 2>/dev/null
import zipfile,sys,re
z=zipfile.ZipFile(sys.argv[1])
for n in z.namelist():
    if re.search(r'(^|/)(licen[sc]e|copying|notice)([.-][a-z0-9]+)?$', n, re.I):
        open(sys.argv[2],'wb').write(z.read(n)); print(n); break
PY
        ent=$(cat "$TMP/n" 2>/dev/null) ;;
      *) ent=$(tar tzf "$TMP/s.bin" 2>/dev/null | grep -iE '/(licen[sc]e|copying|notice)([.-][a-z0-9]+)?$' | head -1)
         [ -n "$ent" ] && tar xzf "$TMP/s.bin" -O "$ent" > "$TMP/L" 2>/dev/null ;;
    esac
    [ -n "$ent" ] && [ -s "$TMP/L" ] && { lf="${ent#*/}"; bytes=$(wc -c < "$TMP/L" | tr -d ' '); sha=$(sha256sum "$TMP/L" | cut -c1-12); }; }
fi

repo=$(norm "$rawrepo"); [ -z "$repo" ] && repo="-"
if [ "$repo" != "-" ]; then
  res=$(./"$(basename "$HERE")"/../../../compose/code/p198-identity-sweep/resolve_repo.sh "$repo" 2>/dev/null || "$HERE/resolve_repo.sh" "$repo")
  st=$(printf '%s' "$res" | cut -f1); cell=$(printf '%s' "$res" | cut -f2)
  if [ "$st" = "RESOLVES" ]; then v="IDENTITY-DECLARED"; else v="IDENTITY-DECLARED-BUT-DEAD"; fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$pkg" "$chan" "$repo" "$cell" "$lf" "$bytes" "$sha" "$v"
else
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$pkg" "$chan" "NO-REPOSITORY-FIELD" "-" "$lf" "$bytes" "$sha" "IDENTITY-UNKNOWN"
fi
exit 0
