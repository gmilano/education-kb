#!/bin/bash
# POSITIVE control, the second real shape (p1040-ecl-corpus-census/holder.sh):
# `set -u` plus a bare $1. Must classify as `usage`, not `crash`.
set -u
echo "slug	holder_line"
echo "processing $1"
