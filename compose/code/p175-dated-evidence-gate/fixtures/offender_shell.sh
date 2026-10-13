#!/usr/bin/env bash
# POSITIVE CONTROL - frozen from a real shape in this repository.
# Writes a dated evidence file under a date that is a literal in the script.
# The gate MUST flag this.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
printf 'repo\tverdict\n' > "$DIR/verdict.2026-10-11.tsv"
printf 'a\tb\n' >> "$DIR/verdict.2026-10-11.tsv"
