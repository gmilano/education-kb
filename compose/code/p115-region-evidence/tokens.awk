# tokens.awk -- STAGE B. Harvest ADDRESS tokens from the bodies of the
# evidence blobs stage A selected, scoped to declared KEYS.
#
# Usage: awk -f tokens.awk kinds.tsv body-stream
#        kinds.tsv : <sha> TAB <layer>:<kind>   (layer 0 = root, 1 = nested, R = readme)
#        body-stream: output of `git cat-file --batch`
#
# Output
#   D <layer> <domain>   a domain harvested from an email or a URL
#   K <layer> <cc>       an ISO-3166 alpha-2 code read from a TYPED field
#   I <token>            a layer-I institution word seen in the README
#   C <key> <value>      counters
#
# LAYER 0 = a structured metadata file AT THE REPOSITORY ROOT -- the
#           repository's own declaration about itself.
# LAYER 1 = the same kinds of file NESTED in the tree.
# LAYER R = the root README.
#
# P115-N. THE DEPTH SPLIT IS NOT TIDINESS, IT IS THE DIFFERENCE BETWEEN A
# RIGHT ANSWER AND A CONFIDENT WRONG ONE, AND THE SMOKE TEST PROVED IT ON THE
# LARGEST ROW OF THIS SHELF BEFORE THE CENSUS RAN.
# Read flat -- every structured file in the tree, root and nested alike --
# `moodle/moodle` comes back `contested` on the evidence of
# `gjcampbell.co.uk`, `tubo-world.de` and `www.mullie.eu`: the maintainer
# emails of three third-party libraries Moodle BUNDLES under `lib/`. Moodle
# HQ is in Perth. The flat read does not merely fail to place the row, it
# offers two European countries for an Australian project, and `region` is a
# field this KB FILTERS on.
# P115-F excludes `vendor/` and `node_modules/`; it cannot exclude `lib/`,
# because `lib/` is also where a project keeps its own code. Depth can:
# a declaration at the ROOT is the repository's, and one nested under it
# belongs to whatever is nested there. Layer 1 is still measured and still
# reported -- as a CONTRAST, never folded into layer 0.
#
# ---------------------------------------------------------------------------
# P115-H. A TOKEN COUNTS IN LAYER S ONLY IF IT SITS ON A LINE THAT CARRIES A
# DECLARED KEY. The alternative -- harvest every address in the file -- reads
# a package.json's `"repository"` and `"dependencies"` as affiliation, and on
# this shelf that would place most rows at the forge they are hosted on.
#
# THE ERROR THIS RULE CARRIES, STATED HERE RATHER THAN DISCOVERED LATER:
# a MINIFIED json file is one line, so every key matches at once and the scope
# widens to the whole file. Minified metadata is rare (`package.json` is
# written by hand and by `npm init`, both pretty-printed) but it is not
# impossible, and where it happens this instrument reads MORE than it claims
# to. It never reads less. `C wideline` counts the lines that matched 4+
# distinct keys, which is the measurement of how often it happened.
#
# P115-I. ONLY EMAILS AND URLs ARE HARVESTED, NEVER BARE HOSTNAMES.
# An affiliation string reading "University of Helsinki" places nothing here,
# and one reading "helsinki.fi" places nothing either. The rule costs real
# placements and it cannot mistake `package.json` or `1.2.3` for a host --
# and on a field this KB FILTERS on, an under-count that cannot invent a
# country is the only error worth having (P800).

BEGIN { OFS = "\t" }

# ---- phase 1: the sha -> kind map ----------------------------------------
NR == FNR {
  if ($0 ~ /^[0-9a-f]+\t/) { split($0, a, "\t"); kindof[a[1]] = a[2] }
  next
}
# the map's value is `<layer>:<kind>`, layer in { 0, 1, R }:
#   0  a structured metadata file at the repository ROOT
#   1  a structured metadata file NESTED in the tree
#   R  the root README

# ---- phase 2: the batch stream -------------------------------------------
# P112-H, carried: the header lines of a `cat-file --batch` stream interleave
# with content and are DELIMITERS, never content.
#
# P115-L. THE HEADER TEST IS WRITTEN WITHOUT AN INTERVAL EXPRESSION ON
# PURPOSE. The awk on this image is `mawk 1.3.4 20240123`, and it does not
# compile `/^[0-9a-f]{40}( |$)/` -- it aborts the whole program with
# `REcompile() - panic: values still on machine stack`. The suite's first run
# found it, on real repositories, before the census did. Field tests cost
# nothing here and they compile everywhere, so the rule is: no interval
# expression in this instrument's hot path.
$1 ~ /^[0-9a-f]+$/ && (length($1) == 40 || length($1) == 64) {
  if (NF >= 2 && ($2 == "blob" || $2 == "tree" || $2 == "commit" || $2 == "tag" || $2 == "missing")) {
    cur = $1
    if (cur in kindof) { split(kindof[cur], kk, ":"); layer = kk[1]; kind = kk[2] }
    else               { layer = ""; kind = "" }
    nblob++
    next
  }
}

kind == "" { next }

{
  line = $0
  sub(/\r$/, "", line)

  if (layer == "R") {
    harvest(line, "R")
    institutions(line)
    next
  }

  # ---- layer S: does this line carry a declared key? -------------------
  low = tolower(line)
  if (keyed(low, kind)) harvest(line, layer)

  # a TYPED country field. CITATION.cff only -- `country: FI` is ISO-3166
  # alpha-2 by the schema, which makes it the one place on a shelf where a
  # region is declared outright instead of inferred from an address.
  if (kind == "cff" && layer == "0" && low ~ /^[ \t-]*country[ \t]*:/) {
    cc = line
    sub(/^[^:]*:[ \t]*/, "", cc)
    gsub(/["'\r \t]/, "", cc)
    if (cc ~ /^[A-Za-z][A-Za-z]$/) print "K", "0", tolower(cc)
  }
}

# ---------------------------------------------------------------------------
function keyed(low, k,   n, i, keys, c) {
  if (k == "cff")           keys = "affiliation:|email:|website:|url:|institution:|department:|address:"
  else if (k == "codemeta" || k == "zenodo")
                            keys = "\"affiliation\"|\"email\"|\"url\"|\"publisher\"|\"provider\"|\"sponsor\"|\"funder\""
  else if (k == "npm" || k == "composer")
                            keys = "\"author\"|\"maintainers\"|\"contributors\"|\"homepage\"|\"email\"|\"url\"|\"bugs\"|\"funding\"|\"publisher\"|\"organization\""
  else if (k == "pytoml" || k == "setupcfg")
                            keys = "author|maintainer|homepage|home-page|url|documentation"
  else if (k == "setuppy")  keys = "author|maintainer|url|project_urls|homepage"
  else if (k == "maven")    keys = "<url>|<email>|<organization|<organizationurl>|<developer"
  else if (k == "cargo")    keys = "authors|homepage|documentation"
  else if (k == "gomod")    keys = "^module "
  else if (k == "pubspec")  keys = "homepage|author|repository|issue_tracker"
  else if (k == "rdesc")    keys = "^maintainer:|^author:|^url:"
  else if (k == "gemspec")  keys = "email|homepage|authors"
  else return 0

  n = split(keys, keyv, "|")
  c = 0
  for (i = 1; i <= n; i++) if (low ~ keyv[i]) c++
  if (c >= 4) nwide++
  return (c > 0)
}

# emails and URLs only (P115-I)
function harvest(s, layer,   t, host, rest) {
  # --- emails ---
  rest = s
  while (match(rest, /[A-Za-z0-9._%+-]+@[A-Za-z0-9]([A-Za-z0-9.-]*[A-Za-z0-9])?\.[A-Za-z][A-Za-z]+/)) {
    t = substr(rest, RSTART, RLENGTH)
    rest = substr(rest, RSTART + RLENGTH)
    host = t
    sub(/^[^@]*@/, "", host)
    emit(layer, host, "email")
  }
  # --- URLs ---
  rest = s
  while (match(rest, /(https?:\/\/|\/\/)[A-Za-z0-9][A-Za-z0-9.-]*\.[A-Za-z][A-Za-z]+/)) {
    t = substr(rest, RSTART, RLENGTH)
    rest = substr(rest, RSTART + RLENGTH)
    host = t
    sub(/^(https?:)?\/\//, "", host)
    emit(layer, host, "url")
  }
  # --- `module <path>` in go.mod carries no scheme ---
  if (s ~ /^module[ \t]+[A-Za-z0-9.-]+\.[A-Za-z][A-Za-z]+\//) {
    host = s
    sub(/^module[ \t]+/, "", host)
    sub(/\/.*$/, "", host)
    emit(layer, host, "module")
  }
}

function emit(layer, host, how) {
  gsub(/[",'<>();]/, "", host)
  sub(/\.$/, "", host)
  host = tolower(host)
  if (host == "" || host !~ /\./) return
  print "D", layer, host, how
  nD++
}

# layer I: p800's grep, kept as a CANDIDATE count and never a placement
function institutions(s,   low, t) {
  low = tolower(s)
  if (low ~ /universi|ministr|ministè|minister|government|gobierno|instituto|institut|hochschule|école|universidad|universidade|akadem|national agency|school district|consortium|foundation/) {
    nI++
    if (nI <= 3) { t = s; gsub(/\t/, " ", t); print "I", substr(t, 1, 120) }
  }
}

END {
  print "C", "blobs", nblob + 0
  print "C", "domains", nD + 0
  print "C", "wideline", nwide + 0
  print "C", "inst_lines", nI + 0
}
