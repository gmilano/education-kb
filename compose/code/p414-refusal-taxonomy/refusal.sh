#!/bin/sh
# p414 — refusal TAXONOMY: a tunnel refusal and an authorization refusal are different facts.
# Columns: host-layer http, bytes, whether a BODY came back, and the named reason.
printf '%-58s %-6s %-7s %-6s %s\n' URL HTTP BYTES BODY CLASS
for u in "$@"; do
  out=$(curl -sS --max-time 12 -o body.tmp -w '%{http_code} %{size_download}' "$u" 2>err.tmp)
  code=$(echo "$out" | awk '{print $1}'); size=$(echo "$out" | awk '{print $2}')
  [ -z "$code" ] && code=000; [ -z "$size" ] && size=0
  if grep -q 'CONNECT tunnel failed' err.tmp 2>/dev/null; then
    cls="TUNNEL-REFUSED (proxy allowlist; CONNECT 403, no body)"
  elif [ "$code" = "403" ] && [ "$size" -gt 0 ]; then
    cls="AUTHZ-REFUSED (tunnel OK; 403 WITH readable body)"
  elif [ "$code" = "200" ]; then cls="SERVED"
  elif [ "$code" = "404" ] && [ "$size" -gt 0 ]; then cls="SEMANTIC-404 (host answered)"
  else cls="OTHER($code)"; fi
  b=$([ "$size" -gt 0 ] && echo yes || echo no)
  printf '%-58s %-6s %-7s %-6s %s\n' "$(echo $u|cut -c1-58)" "$code" "$size" "$b" "$cls"
done
rm -f body.tmp err.tmp
