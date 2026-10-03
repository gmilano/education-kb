#!/bin/bash
# P183 — the PACKAGE layer: does the cession travel with the artefact a client installs?
#
# Pass 65 (P179) split the license column into IDENTIFIER (a manifest field naming a
# license, carrying no holder, no year, no line of text) and CESSION (a grant with holder,
# year and text).  It measured that split on 7 GitHub rows: 5 identifier / 2 cession.
#
# This instrument asks the same question of the rows that have NO GitHub URL and name a
# package by its registry.  Three readings per package, which are three different claims:
#
#   REG-ID       the registry metadata declares a license identifier
#   TARBALL-TEXT the published artefact CONTAINS a license text file
#   PROMISED     the manifest lists a license file in `files` that the artefact lacks
#
# Only TARBALL-TEXT is something a legal office can read.  REG-ID without it is the P179
# identifier, at the layer where it matters most: the artefact is what gets installed.
#
# D5 -- A NAME IS NOT A PACKAGE: the first build queried npm, and EXITED on the first
# channel that answered.  Two rows of this KB cite a PyPI package whose NAME also exists on
# npm as an unrelated upload (`clawed`, `educhain`), so the npm-first build published the
# wrong artefact's license under the row's name.  The instrument now queries BOTH channels
# and emits one line per channel; reconciling the row to the channel it cites is the
# reader's job, and the output makes it possible.  The npm-first build is kept beside this
# one as a dated negative control.
#
# TSV: pkg · channel · reg_license · tarball_license_file · bytes · verdict
pkg="$1"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
found=0
emit(){ printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$pkg" "$1" "$2" "$3" "$4" "$5"; found=1; }

enc=$(printf '%s' "$pkg" | sed 's|/|%2F|')

# ---- npm ----
if curl -sf --max-time 30 "https://registry.npmjs.org/$enc" -o "$TMP/npm.json" 2>/dev/null; then
  lic=$(python3 - "$TMP/npm.json" <<'PY'
import json,sys
d=json.load(open(sys.argv[1]))
v=d.get("dist-tags",{}).get("latest")
m=d.get("versions",{}).get(v,{})
l=m.get("license") or m.get("licenses") or d.get("license")
if isinstance(l,dict): l=l.get("type","")
if isinstance(l,list): l=",".join(x.get("type",str(x)) if isinstance(x,dict) else str(x) for x in l)
print(f"{v}\t{l or '-'}\t{','.join(m.get('files') or []) or '-'}\t{m.get('dist',{}).get('tarball','')}")
PY
)
  ver=$(printf '%s' "$lic" | cut -f1); id=$(printf '%s' "$lic" | cut -f2)
  files=$(printf '%s' "$lic" | cut -f3); tgz=$(printf '%s' "$lic" | cut -f4)
  lf="-"; bytes="-"
  if [ -n "$tgz" ] && curl -sf --max-time 60 "$tgz" -o "$TMP/p.tgz"; then
    ent=$(tar tzf "$TMP/p.tgz" 2>/dev/null | grep -iE '/(licen[sc]e|copying|notice|unlicense)([.-][a-z0-9]+)?$' | head -1)
    if [ -n "$ent" ]; then
      lf="${ent#package/}"
      bytes=$(tar xzf "$TMP/p.tgz" -O "$ent" 2>/dev/null | wc -c | tr -d ' ')
    fi
  else
    lf="TARBALL-UNREACHABLE"
  fi
  v="REG-ID-ONLY"
  [ "$lf" != "-" ] && [ "$lf" != "TARBALL-UNREACHABLE" ] && v="TARBALL-TEXT"
  [ "$id" = "-" ] && [ "$lf" = "-" ] && v="NO-DECLARATION"
  [ "$lf" = "-" ] && printf '%s' "$files" | grep -qiE '(^|,)(licen[sc]e|LICENSE)' && v="PROMISED-ABSENT"
  emit "npm@$ver" "$id" "$lf" "$bytes" "$v"
fi

# ---- PyPI ----
if curl -sf --max-time 30 "https://pypi.org/pypi/$pkg/json" -o "$TMP/pypi.json" 2>/dev/null; then
  out=$(python3 - "$TMP/pypi.json" <<'PY'
import json,sys
d=json.load(open(sys.argv[1])); i=d["info"]
lic=i.get("license") or "-"
lic=(lic.splitlines() or ["-"])[0][:60]
le=i.get("license_expression") or "-"
cls=[c for c in (i.get("classifiers") or []) if c.startswith("License ::")]
url=""
for f in d["urls"]:
    if f["packagetype"]=="sdist": url=f["url"]; break
if not url and d["urls"]: url=d["urls"][0]["url"]
print(f"{i['version']}\t{lic if lic!='-' else (le if le!='-' else (cls[0] if cls else '-'))}\t{url}")
PY
)
  ver=$(printf '%s' "$out" | cut -f1); id=$(printf '%s' "$out" | cut -f2); url=$(printf '%s' "$out" | cut -f3)
  lf="-"; bytes="-"
  if [ -n "$url" ] && curl -sf --max-time 60 "$url" -o "$TMP/s.bin"; then
    case "$url" in
      *.whl|*.zip) ent=$(python3 -c "
import zipfile,sys,re
z=zipfile.ZipFile(sys.argv[1])
for n in z.namelist():
    if re.search(r'(^|/)(licen[sc]e|copying|notice)([.-][a-z0-9]+)?\$', n, re.I): print(n); break
" "$TMP/s.bin" 2>/dev/null)
        [ -n "$ent" ] && { lf="$ent"; bytes=$(python3 -c "
import zipfile,sys; print(len(zipfile.ZipFile(sys.argv[1]).read(sys.argv[2])))" "$TMP/s.bin" "$ent"); } ;;
      *) ent=$(tar tzf "$TMP/s.bin" 2>/dev/null | grep -iE '/(licen[sc]e|copying|notice)([.-][a-z0-9]+)?$' | head -1)
         [ -n "$ent" ] && { lf="${ent#*/}"; bytes=$(tar xzf "$TMP/s.bin" -O "$ent" 2>/dev/null | wc -c | tr -d ' '); } ;;
    esac
  else
    lf="SDIST-UNREACHABLE"
  fi
  v="REG-ID-ONLY"
  [ "$lf" != "-" ] && [ "$lf" != "SDIST-UNREACHABLE" ] && v="TARBALL-TEXT"
  [ "$id" = "-" ] && [ "$lf" = "-" ] && v="NO-DECLARATION"
  emit "pypi@$ver" "$id" "$lf" "$bytes" "$v"
fi

[ "$found" = "0" ] && emit "NONE" "-" "-" "-" "REGISTRY-404"
exit 0
