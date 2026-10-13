#!/usr/bin/env bash
# NEGATIVE CONTROL - takes its date from the clock, so each run writes its own
# file and nothing is overwritten. The gate MUST stay silent on this.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STAMP="$(date +%F)"
printf 'repo\tverdict\n' > "$DIR/result.$STAMP.tsv"
