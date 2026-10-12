#!/bin/sh
# p142-github-only-tier — ACTION DI: test T30 on a third tier.
#
# The instrument is p141's `surface_gate.py`, executed UNCHANGED. Only the population is new:
# the ten largest GitHub-only connector rows on `agents/top.md`.
#
# 🔴 Two substitutions the action did not specify, both forced and both declared:
#
#  1. "largest" is COMMIT COUNT, not stars. `api.github.com` answers 403 through this
#     environment's proxy, so a star count cannot be measured on any readable channel this
#     pass; it would have to be copied from this KB's own pages, which is not a measurement.
#     Commit count is read from the clone.
#  2. "GitHub-only" was CHECKED, not assumed. `alejooroncoy/campus-cli` IS npm-published
#     (`campus-cli` 2.2.3 declares `alejooroncoy/campus-cli` as its repository) and is
#     therefore EXCLUDED from a GitHub-only population. 🔵 And `bb-mcp` on npm is a
#     DIFFERENT project — "MCP server for Bitbucket Server", maintainer `g7v`, no repository
#     field — so `nitsuah/bb-mcp` stays in. A name match on a registry is not a publication
#     of the row that shares the name.
exec python3 -I ../p141-agent-surface-gate/surface_gate.py "$@"
