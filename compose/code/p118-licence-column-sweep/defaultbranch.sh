#!/usr/bin/env bash
# P118-B. Default branch over the GIT transport. `git ls-remote --symref HEAD`
# answers for every public repository while BOTH REST endpoints are gated:
#   /repos/{o}/{r}        403 to curl, 403 to gh, denied to the MCP relay
#   /search/repositories  403 to curl, 403 to gh, 200 to the MCP relay
# Four transports, and git is the only one that needs no session scope.
# v1 of this instrument read whichever of main/master/develop answered FIRST,
# which is NOT the default branch: frappe/frappe develops on `develop` and its
# `master` carries a stale MIT file, elgg/elgg defaults to `7.x`.
set -u
slug="$1"
ref=$(git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null | awk '/^ref:/{print $2; exit}')
if [ -z "$ref" ]; then printf '%s\t-\tUNREACHABLE\n' "$slug"; else printf '%s\t%s\tOK\n' "$slug" "${ref#refs/heads/}"; fi
