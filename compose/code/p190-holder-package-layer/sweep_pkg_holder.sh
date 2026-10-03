#!/bin/bash
# P190 -- the HOLDER question at the PACKAGE layer: action 2 of pass 67, "the holder sweep
# with the ENLARGED denominator", executed where P184 could not reach.
#
# P184 (pass 66) read the holder of the 160 license files that P170 had measured at a repo
# ref.  Every one of those lives in a GITHUB TREE.  The rows this KB cites by REGISTRY have
# no repo ref, so P184's denominator never contained them -- yet the artefact a client
# actually installs is the tarball, not the tree.
#
# This instrument does not re-implement either half (P126 rule 1).  It composes:
#   - reach + tarball location: the channel proven by p183-nongithub-denominator
#   - holder extraction + classification: extract_holder.py, imported from p184 unchanged
#
# THE ADAPTATION, AND IT IS NOT COSMETIC: P184 classifies a holder against a repo slug
# `owner/repo`.  A package has no slug.  Its identity is the DECLARED repository when it
# declares one, and otherwise the maintainer (npm) or author (PyPI).  So this instrument
# passes the declared repo when present and the maintainer handle when absent, and emits
# WHICH of the two it compared against -- because a HOLDER-MATCH against a maintainer
# handle is a weaker claim than one against a declared repository, and the output has to
# say which claim it is making.
#
# TSV: pkg . channel . compared_against . identity . verdict . holder . family . bytes . licfile
set -u
P184=../p184-holder-mismatch
one() {
  pkg="$1"; ch="$2"
  TMP=$(mktemp -d); trap 'rm -rf "$TMP"' RETURN
  enc=$(printf '%s' "$pkg" | sed 's|/|%2F|')
  tgz=""; ident=""; basis=""
  if [ "$ch" = "npm" ]; then
    curl -sf --max-time 30 "https://registry.npmjs.org/$enc" -o "$TMP/m.json" || { printf '%s\t%s\tREG-UNREACHABLE\t-\t-\t-\t-\t-\t-\n' "$pkg" "$ch"; return; }
    read -r tgz ident basis <<<"$(python3 - "$TMP/m.json" <<'PY'
import json,sys
d=json.load(open(sys.argv[1]))
v=d.get("dist-tags",{}).get("latest"); m=d.get("versions",{}).get(v,{})
r=m.get("repository") or d.get("repository")
if isinstance(r,dict): r=r.get("url","")
r=(r or "").replace("git+","").replace("git://","").replace("https://github.com/","").replace(".git","").strip("/")
if r and r.count("/")==1: print(m.get("dist",{}).get("tarball",""), r, "DECLARED-REPO")
else:
    mt=(d.get("maintainers") or [{}])[0].get("name","-")
    print(m.get("dist",{}).get("tarball",""), mt, "MAINTAINER")
PY
)"
  else
    curl -sf --max-time 30 "https://pypi.org/pypi/$enc/json" -o "$TMP/m.json" || { printf '%s\t%s\tREG-UNREACHABLE\t-\t-\t-\t-\t-\t-\n' "$pkg" "$ch"; return; }
    read -r tgz ident basis <<<"$(python3 - "$TMP/m.json" <<'PY'
import json,sys
d=json.load(open(sys.argv[1])); i=d.get("info",{})
u=(i.get("project_urls") or {})
repo=""
for k in ("Repository","Homepage","Source","Bug Tracker"):
    val=u.get(k) or ""
    if "github.com/" in val:
        repo=val.split("github.com/")[1].strip("/").replace(".git","")
        repo="/".join(repo.split("/")[:2]); break
if not repo and "github.com/" in (i.get("home_page") or ""):
    repo="/".join((i["home_page"].split("github.com/")[1]).strip("/").split("/")[:2])
url=""
for f in d.get("urls") or []:
    if f.get("packagetype")=="sdist": url=f.get("url"); break
if not url and (d.get("urls") or []): url=d["urls"][0].get("url","")
print(url, repo or (i.get("author") or "-").replace(" ","_"), "DECLARED-REPO" if repo else "AUTHOR")
PY
)"
  fi
  [ -z "${tgz:-}" ] && { printf '%s\t%s\tNO-ARTEFACT-URL\t%s\t-\t-\t-\t-\t-\n' "$pkg" "$ch" "${ident:--}"; return; }
  curl -sf --max-time 90 "$tgz" -o "$TMP/a.bin" || { printf '%s\t%s\tARTEFACT-UNREACHABLE\t%s\t-\t-\t-\t-\t-\n' "$pkg" "$ch" "${ident:--}"; return; }
  # list members, pick the first license-shaped path
  if tar tzf "$TMP/a.bin" >"$TMP/list" 2>/dev/null; then kind=tar; else
    python3 -c "import zipfile,sys;[print(n) for n in zipfile.ZipFile(sys.argv[1]).namelist()]" "$TMP/a.bin" >"$TMP/list" 2>/dev/null && kind=zip || { printf '%s\t%s\tARTEFACT-UNREADABLE\t%s\t-\t-\t-\t-\t-\n' "$pkg" "$ch" "${ident:--}"; return; }
  fi
  lf=$(grep -iE '(^|/)(LICEN[CS]E|COPYING)(\.(md|txt|rst))?$' "$TMP/list" | head -1)
  [ -z "$lf" ] && { printf '%s\t%s\tNO-LICENSE-IN-ARTEFACT\t%s\t-\t-\t-\t-\t-\n' "$pkg" "$ch" "${ident:--}"; return; }
  if [ "$kind" = tar ]; then tar xzf "$TMP/a.bin" -O "$lf" >"$TMP/lic" 2>/dev/null; else
    python3 -c "import zipfile,sys;open(sys.argv[3],'wb').write(zipfile.ZipFile(sys.argv[1]).read(sys.argv[2]))" "$TMP/a.bin" "$lf" "$TMP/lic" 2>/dev/null; fi
  [ ! -s "$TMP/lic" ] && { printf '%s\t%s\tLICENSE-EMPTY\t%s\t-\t-\t-\t-\t%s\n' "$pkg" "$ch" "${ident:--}" "$lf"; return; }
  fam=$(python3 "$P184/../p172-payload-license-sweep/extract_license.py" <"$TMP/lic" 2>/dev/null | head -1)
  [ "$fam" = "-" ] && fam=""
  [ -z "$fam" ] && fam=$(head -5 "$TMP/lic" | grep -oiE 'MIT|Apache License|GNU AFFERO|GNU GENERAL|ISC|BSD' | head -1)
  [ -z "$fam" ] && fam="UNKNOWN"
  case "$fam" in *MIT*) fam=MIT;; *Apache*|*APACHE*) fam=Apache-2.0;; *AFFERO*) fam=AGPL-3.0;; *GENERAL*) fam=GPL-3.0;; *ISC*) fam=ISC;; esac
  out=$(python3 "$P184/extract_holder.py" "$ident" "$fam" <"$TMP/lic" 2>/dev/null)
  verdict=$(printf '%s' "$out" | cut -f2); holder=$(printf '%s' "$out" | cut -f3)
  # D8 -- the UNFILLED copyright line.  `opencode-sit` ships `Copyright (c) 2026` with NO
  # NAME, and extract_holder.py's permissive path then takes the next prose line
  # ("Permission is hereby granted...") as the holder.  That is P184's own D6 failure in a
  # family its filter does not cover: D6 taught that a license text is kilobytes of prose
  # ABOUT copyright, so any body line can impersonate a holder.  P184 already has the right
  # class for this -- NO-HOLDER, written for the unfilled Apache appendix -- so this is a
  # reclassification into an existing class, not a new verdict.  Guard: a copyright line
  # whose remainder after the year is empty means the grant names nobody.
  if printf '%s' "$holder" | grep -qiE '^(permission|the above|this software|redistribution)'; then
    if grep -qiE '^[[:space:]]*copyright[^[:alnum:]]*(\(c\))?[[:space:]]*[0-9]{4}([[:space:]]*[-,][[:space:]]*[0-9]{4})?[[:space:]]*$' "$TMP/lic"; then
      verdict="NO-HOLDER"; holder="(copyright line present, no name filled in)"
    fi
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$pkg" "$ch" "$basis" "$ident" "${verdict:-EXTRACT-FAILED}" "${holder:--}" "$fam" "$(wc -c <"$TMP/lic")" "$lf"
}
while IFS=$'\t' read -r p c; do [ -n "${p:-}" ] && one "$p" "$c"; done < "${1:-targets.tsv}"
