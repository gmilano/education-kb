#!/usr/bin/env bash
# emit_placements.sh — turn the census into a COMMITTED, address-keyed
# placement file, the way `orgs.region.tsv` is a committed org-keyed one.
#
# Usage: ./emit_placements.sh <result.tsv> > addresses.region.tsv
#
# P115-U. THE UNIT IS THE ADDRESS, NOT THE ORG, AND THAT IS WHY THIS IS A
# SECOND FILE RATHER THAN AN EDIT TO THE FIRST.
# `Gap 403` asked for `orgs.region.tsv` to be EXTENDED. It cannot be, from
# this evidence: `orgs.region.tsv` is keyed on the ORG and says "every
# repository under `openfun/` is EMEA", which is a claim about an
# institution. p115's evidence is per-REPOSITORY — one org can perfectly well
# hold a repo whose root metadata names a Finnish maintainer and another
# whose root metadata names a Japanese one, and folding either into an org
# verdict would be inventing the other.
#
# So the shelf now carries TWO placement files at TWO units. Neither
# supersedes the other and a later pass should read their UNION, preferring
# the address row where both speak — because the address row is evidence from
# the repository itself, while the org row is this KB's record of an
# institution's home.
#
# Only `placed` and `typed` rows are emitted. `contested` is deliberately
# absent: a row with two regions in its own metadata has no single value for
# a closed field, and writing one would be the exact failure `P115-K` exists
# to prevent.
set -uo pipefail
res="${1:?result tsv}"

cat <<'HDR'
# address<TAB>region<TAB>layer<TAB>class<TAB>evidence
#
# P115-U. Address-keyed regional placement, read from evidence the repository
# COMMITS about itself. Produced by `emit_placements.sh` from the census TSV;
# do not hand-edit — re-run the instrument.
#
# `region` is the brief's closed vocabulary: North America | EMEA | APAC | LATAM.
#
# layer `0`     = a structured metadata file at the repository ROOT.
# layer `typed` = a TYPED ISO-3166 `country:` field (CITATION.cff schema),
#                 which is the only place on this shelf where a region is
#                 DECLARED rather than inferred from an address.
#
# `class` is what KIND of address placed the row, classified structurally and
# never from a name (P115-V):
#   `academic`   a registry-restricted academic suffix: `.edu`, `.ac.<cc>`,
#                `.edu.<cc>`. The strongest evidence short of a typed field.
#   `government` `.gov`, `.mil`, `.gov.<cc>`, `.gob.<cc>`.
#   `other`      a company or PERSONAL domain whose ccTLD happens to be in
#                the region. P800's rule asks for an INSTITUTION; this class
#                does not supply one, and a reader should weigh it as such.
#
# NOT in this file, on purpose:
#   - `contested` rows. Two regions in a row's own metadata gives no single
#     value for a closed field (P115-K).
#   - anything read from a NESTED metadata file (P115-N) or from a README
#     (layer R). Both are measured in the census TSV and neither places.
#
HDR

awk -F'\t' 'NR>1 && ($21=="placed" || $21=="typed") {
  layer = ($21=="typed" ? "typed" : "0")
  ev    = ($21=="typed" ? "country: " toupper($23) : $25)
  kl    = ($21=="typed" ? "typed" : $26)
  printf "%s\t%s\t%s\t%s\t%s\n", $1, $20, layer, kl, ev
}' "$res" | sort
