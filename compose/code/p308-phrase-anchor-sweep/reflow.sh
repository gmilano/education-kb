#!/bin/sh
# reflow.sh <width> -- hard-wrap stdin at <width> columns, breaking ONLY on spaces.
#
# This is not a synthetic mutation.  It is the transformation an editor applies when a
# maintainer runs fill-paragraph over a licence file -- Emacs `fill-column` defaults to 70,
# `fmt` to 75 -- and the one `prettier --prose-wrap` applies to a `LICENSE.md`.
#
# The INVERSE direction (paragraphs joined into single long lines) is already in this base as
# a REAL, found specimen: `p288-agpl-casefold/fixtures/agpl-3.0-kuali-kfs-reflowed.LICENSE`
# (kuali/kfs, 33.755 B) ships exactly that shape and cost this base P288.  So the axis is
# real in both directions and documented in this repo; what this instrument varies is the
# WIDTH, over payloads that are themselves real and fetched first-hand.
#
# DECLARED LIMIT (P286).  A width this instrument applies is not a width found in the wild.
# This measures FRAGILITY OF AN ANCHOR -- whether the classifier's answer depends on where
# the newlines fall -- and it does NOT measure how many repos ship a payload already wrapped
# that way.  The population rate is UNMEASURED and is not estimated here: enumerating the
# 215-slug inventory in batch is denied by the environment (`[Exfil Scouting]`, the same
# blocker the pase 96 declared).
fold -s -w "$1"
