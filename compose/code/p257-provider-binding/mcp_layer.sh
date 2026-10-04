#!/bin/sh
# Complemento de P257: ¿la pieza es un SERVIDOR MCP? Se mide por la dependencia de
# runtime del SDK de MCP, no por el nombre del repo (`-mcp` en el slug es prosa).
# TSV: slug \t manifest \t is_mcp \t verdict
here=$(cd "$(dirname "$0")" && pwd)
RAW=https://raw.githubusercontent.com
slug="$1"
for fn in package.json requirements.txt pyproject.toml; do
  out=$(curl -s --max-time 25 -w "\n%{http_code}" "$RAW/${slug}/HEAD/${fn}" 2>/dev/null)
  code=$(printf '%s' "$out" | tail -1)
  if [ "$code" = "200" ]; then
    printf '%s' "$out" | sed '$d' | python3 -c "
import sys, classify_binding as cb
kind='$fn'; slug='$slug'
t=sys.stdin.read()
deps=cb.parse_manifest(kind,t) or []
mcp=[d for d in deps if d=='mcp' or d=='fastmcp' or d=='@modelcontextprotocol/sdk' or d.startswith('mcp-')]
v=cb.classify(kind,t)[0]
print('%s\t%s\t%s\t%s' % (slug, kind, 'MCP-SERVER' if mcp else 'NOT-MCP', v))
"
    exit 0
  fi
done
printf '%s\t-\tNO-CLAIM\tNO-CLAIM\n' "$slug"
