"""KNOWN LIMIT, frozen as a fixture rather than fixed: the real shape in
mcp-allowlist-gateway/gateway.py prints its usage line in SPANISH. The current
cue list is English-only, so this classifies as `other`. The suite asserts
`other` so the limit is VISIBLE and the next pass that fixes it will see the
test change."""
import sys

print("uso: gateway.py -- <comando del servidor upstream>")
sys.exit(2)
