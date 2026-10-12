#!/bin/sh
# p142-dead-repo-recovery — ACTION DE: does anything in @owen-x-tech/canvas-mcp 1.1.0 point
# at a surviving repository, now that `owentaylor/canvas-mcp` is unreadable?
#
# Channels tried, in order, and all of them reported whether they found anything or not:
#   1. every URL in the published payload (README, package.json, build output, dist UI)
#   2. source-map `sources` / `sourceRoot` -- the usual place an absolute author path leaks
#   3. CI config, .npmignore residue, changelog and issue URLs
#   4. registry metadata OUTSIDE the payload: maintainers, _npmUser, publish host
#   5. `git ls-remote` over candidate owner spellings, against a nonexistent control
#
# 🔴 `curl -sI https://github.com/<owner>/<repo>` answers 403 for EVERY repository through this
# environment's proxy, live or dead, so it is not used. `git ls-remote` with prompts disabled is
# the only valid liveness probe here, and every negative is read against the control.
set -e
PKG='@owen-x-tech/canvas-mcp'; VER='1.1.0'
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
curl -sS --max-time 60 "https://registry.npmjs.org/$PKG" -o "$TMP/meta.json"
TARBALL=$(python3 -I -c "import json;print(json.load(open('$TMP/meta.json'))['versions']['$VER']['dist']['tarball'])")
curl -sS --max-time 120 -o "$TMP/p.tgz" "$TARBALL"
mkdir -p "$TMP/x" && tar -xzf "$TMP/p.tgz" -C "$TMP/x"

echo "== 1/3 pointers in the payload =="
grep -rhoE 'https?://[A-Za-z0-9._~:/?#@!$&+,;=%-]+' "$TMP/x" 2>/dev/null \
  | sed 's/[.,)">'"'"']*$//' | sort -u
echo "== 2 source-map sources =="
python3 -I - "$TMP/x" <<'PY'
import glob, json, sys
for f in sorted(glob.glob(sys.argv[1] + "/package/build/*.map")):
    m = json.load(open(f))
    print(f.rsplit("/", 1)[-1], "sources=", m.get("sources"),
          "sourceRoot=", repr(m.get("sourceRoot")))
PY
echo "== 3 CI / ignore residue =="
find "$TMP/x" \( -name '.github' -o -name '*.yml' -o -name '*.yaml' -o -name '.npmignore' \
     -o -name 'CHANGELOG*' \) -print | sed "s|$TMP/x/||" || true
echo "(nothing listed above means nothing shipped)"
echo "== 4 registry metadata outside the payload =="
python3 -I -c "
import json
d=json.load(open('$TMP/meta.json'))
print('maintainers:', d.get('maintainers'))
for v,m in d['versions'].items():
    print(v, '_npmUser=', m.get('_npmUser'))
"
echo "== 5 ls-remote over candidate spellings (control last, must be unreadable) =="
for c in owentaylor/canvas-mcp owen-x-tech/canvas-mcp OwenTaylor/canvas-mcp \
         owentaylor/canvas-mcp-server owen-taylor/canvas-mcp ogsoccer2006/canvas-mcp \
         owenxtech/canvas-mcp owen-x-tech/canvas gmilano/definitely-not-a-real-repo-p142; do
  if GIT_TERMINAL_PROMPT=0 timeout 45 git ls-remote "https://github.com/$c" >/dev/null 2>&1
  then printf '%-42s READABLE\n' "$c"; else printf '%-42s unreadable\n' "$c"; fi
done
