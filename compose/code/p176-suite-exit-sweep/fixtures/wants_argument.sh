#!/bin/bash
# POSITIVE control, frozen from the real shape found in p115-region-evidence/crosstab.sh:
# a shell script that refuses to run without its first positional argument, and
# prints NONE of the cues an argparse exit prints. Must classify as `usage`.
set -u
: "${1:?result tsv}"
echo "would process $1"
